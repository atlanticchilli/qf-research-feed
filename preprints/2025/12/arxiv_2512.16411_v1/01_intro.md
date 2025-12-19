---
authors:
- Matthieu Garcin
- Louis Perot
doc_id: arxiv:2512.16411v1
family_id: arxiv:2512.16411
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Asymptotic and finite-sample distributions of one- and two-sample empirical
  relative entropy, with application to change-point detection
url_abs: http://arxiv.org/abs/2512.16411v1
url_html: https://arxiv.org/html/2512.16411v1
venue: arXiv q-fin
version: 1
year: 2025
---


Matthieu Garcina,{}^{\text{a,}}, Louis Perotb{}^{\text{b}}
Corresponding author: matthieu.garcin@m4x.org.
  
a{}^{\text{a}} De Vinci Higher Education, De Vinci Research Center, Paris, France.
  
b{}^{\text{b}} Département de mathématiques et applications, École normale supérieure, 45 rue d’Ulm, 75005 Paris, France.
  
Acknowledgements: MG acknowledges the support of the Chair “Deep Finance Statistics” between QRT, Ecole Polytechnique and its foundation. The authors would like to thank Olivier Benhamou for useful discussions and support.

(December 18, 2025)

###### Abstract

Relative entropy, as a divergence metric between two distributions, can be used for offline change-point detection and extends classical methods that mainly rely on moment-based discrepancies. To build a statistical test suitable for this context, we study the distribution of empirical relative entropy and derive several types of approximations: concentration inequalities for finite samples, asymptotic distributions, and Berry-Esseen bounds in a pre-asymptotic regime. For the latter, we introduce a new approach to obtain Berry-Esseen inequalities for nonlinear functions of sum statistics under some convexity assumptions. Our theoretical contributions cover both one- and two-sample empirical relative entropies. We then detail a change-point detection procedure built on relative entropy and compare it, through extensive simulations, with classical methods based on moments or on information criteria. Finally, we illustrate its practical relevance on two real datasets involving temperature series and volatility of stock indices.

Keywords – Berry-Esseen bounds, concentration inequalities, information theory, Kullback-Leibler divergence, structural break detection, two-sample divergence testing

## 1 Introduction

Detecting abrupt changes in time series is crucial in many fields, from climatology [[61](https://arxiv.org/html/2512.16411v1#bib.bib61), [27](https://arxiv.org/html/2512.16411v1#bib.bib27)] to finance [[46](https://arxiv.org/html/2512.16411v1#bib.bib46), [5](https://arxiv.org/html/2512.16411v1#bib.bib5), [11](https://arxiv.org/html/2512.16411v1#bib.bib11)]. It enables one to assess the validity of a model over a given time interval and to specify models that appropriately describe or predict time series.

One of the most widespread online methods for change-point detection is the cumulative sum (CUSUM) procedure [[56](https://arxiv.org/html/2512.16411v1#bib.bib56)]. It tracks down significant deviations from the mean and is thus mainly based on moments. In this paper, we focus on offline methods. Beyond mean shifts, structural breaks may occur within parametric models when some parameters suddenly move to new values. Offline approaches in this setting may be based on moments or on information criteria [[67](https://arxiv.org/html/2512.16411v1#bib.bib67), [29](https://arxiv.org/html/2512.16411v1#bib.bib29)]. The latter case consists in finding the time partition that minimizes the information criterion for a model built as a succession of parameter regimes, each associated with a segment of the partition.

In an offline non-parametric setting, one aims at detecting variations in a non-parametric probability distribution [[43](https://arxiv.org/html/2512.16411v1#bib.bib43), [33](https://arxiv.org/html/2512.16411v1#bib.bib33)]. A distribution may indeed change without affecting the mean or the variance, which limits the relevance of moment-based approaches such as CUSUM [[26](https://arxiv.org/html/2512.16411v1#bib.bib26), [69](https://arxiv.org/html/2512.16411v1#bib.bib69)]. In this distribution-based framework, change-point detection amounts to assessing the statistical significance of the deviation between two empirical distributions. This is precisely the practical objective of the present paper.

Among the existing divergence metrics that could be used in this context, one can cite Wasserstein distance, Hellinger distance, Kolmogorov-Smirnov statistic, or relative entropy [[36](https://arxiv.org/html/2512.16411v1#bib.bib36), [33](https://arxiv.org/html/2512.16411v1#bib.bib33), [49](https://arxiv.org/html/2512.16411v1#bib.bib49)]. We will focus on the latter metric, which is the expectation of the log-likelihood ratio. This ratio is the statistic leading to the uniformly highest power among the statistical tests of probability divergence, under the assumptions of Neyman-Pearson lemma [[24](https://arxiv.org/html/2512.16411v1#bib.bib24)].

The use of relative entropy in the context of change-point detection was already mentioned sporadically in literature [[52](https://arxiv.org/html/2512.16411v1#bib.bib52), [42](https://arxiv.org/html/2512.16411v1#bib.bib42)]. But the challenge of knowing the exact distribution of empirical relative entropy often leads to the construction of statistical tests with a threshold based on simulated quantiles [[59](https://arxiv.org/html/2512.16411v1#bib.bib59)]. The theoretical objective of the present paper is to introduce approximations of this distribution. We focus on three types of them. The most natural is the asymptotic distribution, which may however not always be relevant in the context of change-point detection, where we may be interested in small samples, for example to rapidly draw an alert after a break. We obtain as well pre-asymptotic and finite-sample bounds of the distribution, based either on a Berry-Esseen approach or on concentration inequalities. One can then use these bounds, instead of the asymptotic approximation, to build conservative statistical tests. Our Berry-Esseen bounds are obtained for a nonlinear function of a sum statistic, whose limit distribution is non-Gaussian. Our inequality controls two effects: the classical speed of convergence for an approximation of our statistic and the error related to this approximation. This method can easily be replicated to other kinds of nonlinear statistics. We propose as well extensions to two samples, that is approximations of the distribution of the relative entropy between two empirical probabilities, which is particularly useful in the context of change-point detection. This question is challenging because relative entropy does not satisfy a triangle inequality and because its empirical version may become unbounded when the reference probability is estimated from few observations.

In a simulation study, we show the benefit of using change-point detection methods based on relative entropy, compared to methods based on moments or on information criteria. Two applications to a climate dataset and to financial time series highlight the practical relevance of the method. We study a daily time series of temperatures at Embrun, France, during more than 25 years, as well as six daily volatility series of stock indices, during about 20 years.

The paper is organized as follows. Section [2](https://arxiv.org/html/2512.16411v1#S2 "2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") introduces theoretical results about the distribution of empirical relative entropy. In Section [3](https://arxiv.org/html/2512.16411v1#S3 "3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), we present the change-point detection method based on relative entropy along with baseline approaches. Section [4](https://arxiv.org/html/2512.16411v1#S4 "4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") contains a simulation study and Section [5](https://arxiv.org/html/2512.16411v1#S5 "5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") the application to temperature and volatility series. Section [6](https://arxiv.org/html/2512.16411v1#S6 "6 Conclusion ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") concludes.

## 2 Distribution of empirical relative entropy

We want to compare to each other two discrete probability distributions, with a finite number of possible states, in order to build a statistical test of equality of the distributions. This can be done either by testing one after the other the equality of probabilities for each possible state of the random variable, or by aggregating all these probabilities in a single statistic, thus leading to a single test. It is the purpose of relative entropy.

After a brief introduction on the concept, we detail the asymptotic distribution of the empirical version of relative entropy, with either one or two samples. We also propose pre-asymptotic and finite-sample bounds of its distribution, deriving both a Berry-Esseen inequality and various concentration inequalities.

### 2.1 Relative entropy

We consider a discrete probability, with a finite number k≥2k\geq 2 of possible categories: p=(p1,…,pk)t∈(0,1)kp=(p\_{1},...,p\_{k})^{t}\in(0,1)^{k}, ZtZ^{t} standing for the transposed vector of ZZ. The Shannon entropy related to this categorical distribution is

|  |  |  |
| --- | --- | --- |
|  | H​(p)=−∑i=1kpi​log⁡(pi),H(p)=-\sum\_{i=1}^{k}p\_{i}\log(p\_{i}), |  |

where we use the convention 0​log⁡(0)=00\log(0)=0 [[21](https://arxiv.org/html/2512.16411v1#bib.bib21)]. The entropy quantifies the uncertainty of the distribution [[21](https://arxiv.org/html/2512.16411v1#bib.bib21), [31](https://arxiv.org/html/2512.16411v1#bib.bib31)]. The minimum uncertainty corresponds to a concentration in a single state, leading to the minimum entropy, H​(p)=0H(p)=0. The maximum entropy is reached by a uniform distribution, for which we get H​(p)=log⁡(k)H(p)=\log(k).

When working with data, we can calculate an empirical entropy, based on empirical probabilities. We observe X1X\_{1}, …, XnX\_{n}, iid random variables, which may be either discrete or continuous. We discretize these variables by defining kk possible states Ω1\Omega\_{1}, …, Ωk\Omega\_{k}, which may for example be intervals. We have ℙ​(Xj∈Ωi)=pi\mathbb{P}(X\_{j}\in\Omega\_{i})=p\_{i} for all j∈⟦1,n⟧j\in\llbracket 1,n\rrbracket and i∈⟦1,k⟧i\in\llbracket 1,k\rrbracket. We also define the empirical probability p^n=(p^n,1,…,p^n,k)t∈[0,1]k\widehat{p}\_{n}=(\widehat{p}\_{n,1},...,\widehat{p}\_{n,k})^{t}\in[0,1]^{k}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^n,i=1n​∑j=1n𝟙Xj∈Ωi.\widehat{p}\_{n,i}=\frac{1}{n}\sum\_{j=1}^{n}\mathds{1}\_{X\_{j}\in\Omega\_{i}}. |  | (1) |

The quantity H​(p^n)H(\widehat{p}\_{n}) is then the empirical entropy. The asymptotic distribution of the empirical entropy is either a chi-squared or a Gaussian distribution, depending on the nature of pp [[7](https://arxiv.org/html/2512.16411v1#bib.bib7), [78](https://arxiv.org/html/2512.16411v1#bib.bib78)].

One can also replace the probability pp by a conditional probability. It leads to the evaluation of the complexity of the dependence structure between two variables, what has been shown to be useful for time series, the presence of serial dependence being a useful asset for forecasting purposes [[16](https://arxiv.org/html/2512.16411v1#bib.bib16)]. It has been shown that the distribution of conditional Shannon entropy and of the close concept of mutual information is similar to the one of the non-conditional entropy [[53](https://arxiv.org/html/2512.16411v1#bib.bib53), [66](https://arxiv.org/html/2512.16411v1#bib.bib66), [15](https://arxiv.org/html/2512.16411v1#bib.bib15), [55](https://arxiv.org/html/2512.16411v1#bib.bib55)].

Relative entropy, sometimes also called Kullback-Leibler divergence, uses the concept of entropy to compare to each other two probability distributions, p,q∈(0,1)kp,q\in(0,1)^{k}:

|  |  |  |
| --- | --- | --- |
|  | DKL​(p∥q)=∑i=1kpi​log⁡piqi.D\_{\text{KL}}\left(p\|q\right)=\sum\_{i=1}^{k}p\_{i}\log\frac{p\_{i}}{q\_{i}}. |  |

Relative entropy is non-negative and not bounded. But, with a finite number of states, the infinity of the relative entropy is equivalent to the existence of a state ii for which pi≠0p\_{i}\neq 0 and qi=0q\_{i}=0. Relative entropy is not symmetric in pp and qq. When qq is uniform, relative entropy more simply writes DKL​(p∥q)=log⁡(k)−H​(p)D\_{\text{KL}}\left(p\|q\right)=\log(k)-H(p).

Again, replacing pp by its empirical counterpart p^n\widehat{p}\_{n} leads to an empirical relative entropy. But one can also use relative entropy to compare to each other two empirical probabilities. We deal with the two-sample framework in this paper, considering that the two datasets are generated in the same distribution pp. We are thus given iid observations X1,…,Xn+mX\_{1},...,X\_{n+m} with ℙ​(Xj∈Ωi)=pi\mathbb{P}(X\_{j}\in\Omega\_{i})=p\_{i} for all j∈⟦1,n+m⟧j\in\llbracket 1,n+m\rrbracket and i∈⟦1,k⟧i\in\llbracket 1,k\rrbracket. We define a first empirical probability based on nn observations, following equation ([1](https://arxiv.org/html/2512.16411v1#S2.E1 "In 2.1 Relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), and a second empirical probability based on mm other independent observations,

|  |  |  |
| --- | --- | --- |
|  | q^m,i=1m​∑j=n+1n+m𝟙Xj∈Ωi.\widehat{q}\_{m,i}=\frac{1}{m}\sum\_{j=n+1}^{n+m}\mathds{1}\_{X\_{j}\in\Omega\_{i}}. |  |

In what follows, we study both DKL​(p^n∥p)D\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right) and DKL​(p^n∥q^m)D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{m}\right). It is worth mentioning a specific challenge in the two-sample relative entropy: even though pi>0p\_{i}>0 whatever ii, one cannot guarantee that q^m,i≠0\widehat{q}\_{m,i}\neq 0. Beyond this trivial situation which leads to an infinite estimate, q^m,i\widehat{q}\_{m,i} can be lower than the true value pip\_{i} and amplify much the empirical relative entropy.

### 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy

We first focus on the asymptotic distribution of empirical relative entropy, with one or two samples, thanks to the central limit theorem. Then, an extension of Berry-Esseen bounds to a nonlinear function of a sum statistic provides us with a non-asymptotic expression converging in distribution toward the limit of the central limit theorem. We are assuming that the data are generated according to the probability pp, so that the theoretical relative entropy should be equal to zero. Because of a well-known bias, the empirical relative entropy is positive.

The main challenge, when studying the statistical properties of the empirical relative entropy, is that we have a nonlinear function of the observations. A Taylor expansion can however make the problem feasible. Unlike what is done in the classical delta method, the first-order term of the expansion is equal to zero, so we need a second-order expansion and thus a convergence toward a chi-squared distribution [[8](https://arxiv.org/html/2512.16411v1#bib.bib8), [54](https://arxiv.org/html/2512.16411v1#bib.bib54)]. Another possibility consists in using Wilks’ theorem [[70](https://arxiv.org/html/2512.16411v1#bib.bib70)].

Regarding the speed of convergence toward the chi-squared distribution, we would like to use a Berry-Esseen approach. However, the literature dedicated to Berry-Esseen pre-asymptotic bounds in the case of a nonlinear statistic is very recent and still narrow. The purpose of Berry-Esseen inequality is to provide an upper bound to the Kolmogorov-Smirnov statistic between the distribution of a finite-sample statistic and its limit according to the central limit theorem. When the statistic is a nonlinear function of the observations, it may be possible to linearise it and thus to express the divergence with respect to a Gaussian distribution [[58](https://arxiv.org/html/2512.16411v1#bib.bib58), [64](https://arxiv.org/html/2512.16411v1#bib.bib64)]. This solution is not relevant in our case because relative entropy requires at least a quadratic approximation and has a non-Gaussian limit. Divergence with respect to non-Gaussian distributions have been scarcely explored in the literature. One can cite a first attempt with a statistic equal to the square of the sum of the observations, the limit being χ12\chi^{2}\_{1} [[38](https://arxiv.org/html/2512.16411v1#bib.bib38)]. It is a first step but it is not enough in our case for which the limit is χk−12\chi^{2}\_{k-1}. Promising results have been obtained in multidimensional extensions, with a chi-square limit, but with a number of degrees of freedom higher than 9 [[9](https://arxiv.org/html/2512.16411v1#bib.bib9)] or 5 [[40](https://arxiv.org/html/2512.16411v1#bib.bib40), [41](https://arxiv.org/html/2512.16411v1#bib.bib41)], and a constant in the bound not explicitly specified or obtained by an indirect numerical procedure, requiring for example the number of integer vectors in a given ellipsoid [[39](https://arxiv.org/html/2512.16411v1#bib.bib39), Theorem 1]. A very recent article also puts forward a solution which is valid whatever the number of degrees of freedom of the chi-squared distribution, but with unspecified constants and a limited domain of validity that excludes the right tail of the distribution [[25](https://arxiv.org/html/2512.16411v1#bib.bib25)]. Unfortunately, the right tail is quite important for our application to a statistical test for change-point detection.

Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") gives the central limit of the one-sample relative entropy along with pre-asymptotic bounds in a Berry-Esseen approach. These bounds constitute a new result. We think it is one of the very rare attempts to obtain Berry-Esseen bounds for a statistic defined by a non-trivial nonlinear function of observations which does not converge to a Gaussian. It takes into account both the error of the quadratic approximation, known as the relative Pearson divergence, and the speed of convergence of this approximation. It exploits Raič’s theorem, which is a recent multivariate extension of Berry-Esseen inequality, with well-specified constants [[60](https://arxiv.org/html/2512.16411v1#bib.bib60)].

###### Theorem 1.

Let X1,…,XnX\_{1},...,X\_{n} be iid variables such that ℙ​(Xj∈Ωi)=pi\mathbb{P}(X\_{j}\in\Omega\_{i})=p\_{i} with p=(p1,…,pk)t∈(0,1)kp=(p\_{1},...,p\_{k})^{t}\in(0,1)^{k}. Then, when n→∞n\rightarrow\infty, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​n​DKL​(p^n∥p)​⟶d​χk−12,\boxed{2nD\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right)\overset{\text{d}}{\longrightarrow}\chi^{2}\_{k-1}}, |  | (2) |

where ⟶d\overset{\text{d}}{\longrightarrow} stands for the convergence in distribution. Let x>0x>0. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fχk−12​(κn,kdown​(x))−ℰn,k≤ℙ​(2​n​DKL​(p^n∥p)≤x)≤Fχk−12​(κn,kup​(x))+ℰn,k,\boxed{F\_{\chi^{2}\_{k-1}}\left(\kappa\_{n,k}^{\text{down}}(x)\right)-\mathcal{E}\_{n,k}\leq\mathbb{P}\left(2nD\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right)\leq x\right)\leq F\_{\chi^{2}\_{k-1}}\left(\kappa\_{n,k}^{\text{up}}(x)\right)+\mathcal{E}\_{n,k}}, |  | (3) |

where Fχk−12F\_{\chi^{2}\_{k-1}} is the cdf of the χk−12\chi^{2}\_{k-1} distribution,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰn,k=(42​(k−1)1/4+16)​∑i=1k(1−pi)3/2(n​pi)1/2,\mathcal{E}\_{n,k}=\left(42(k-1)^{1/4}+16\right)\sum\_{i=1}^{k}\frac{(1-p\_{i})^{3/2}}{(np\_{i})^{1/2}}, |  | (4) |

and where, for η∈{up,down}\eta\in\{\text{up},\text{down}\}, we have

|  |  |  |
| --- | --- | --- |
|  | κn,kη​(x)={min⁡{(−1)𝟙η=up​κn,k,r​(x)​|r∈{0,1,2},(−1)𝟙η=up​κn,k,r​(x)>​0}if ​27​x≤4​μ​nmin⁡{(−1)𝟙η=up​κn,k,>​(x)​|(−1)𝟙η=up​κn,k,>​(x)>​0}else,\sqrt{\kappa\_{n,k}^{\eta}(x)}=\left\{\begin{array}[]{ll}\min\{(-1)^{\mathds{1}\_{\eta=\text{up}}}\kappa\_{n,k,r}(x)|r\in\{0,1,2\},(-1)^{\mathds{1}\_{\eta=\text{up}}}\kappa\_{n,k,r}(x)>0\}&\text{if }27x\leq 4\mu n\\ \min\{(-1)^{\mathds{1}\_{\eta=\text{up}}}\kappa\_{n,k,>}(x)|(-1)^{\mathds{1}\_{\eta=\text{up}}}\kappa\_{n,k,>}(x)>0\}&\text{else,}\end{array}\right. |  |

with the convention min⁡(∅)=+∞\min(\emptyset)=+\infty, the notation μ=mini∈⟦1,k⟧⁡pi\mu=\min\_{i\in\llbracket 1,k\rrbracket}p\_{i}, as well as

|  |  |  |
| --- | --- | --- |
|  | κn,k,r​(x)=μ​n3​[2​cos⁡(13​arccos⁡(27​x2​μ​n−1)−2​r​π3)−1]\kappa\_{n,k,r}(x)=\frac{\sqrt{\mu n}}{3}\left[2\cos\left(\frac{1}{3}\arccos\left(\frac{27x}{2\mu n}-1\right)-\frac{2r\pi}{3}\right)-1\right] |  |

and

|  |  |  |
| --- | --- | --- |
|  | κn,k,>​(x)=μ​n33​[−μ​n9+3​x2+−μ​n​x3+94​x23+−μ​n9+3​x2−−μ​n​x3+94​x23]−μ​n3.\kappa\_{n,k,>}(x)=\sqrt[3]{\frac{\sqrt{\mu n}}{3}}\left[\sqrt[3]{-\frac{\mu n}{9}+\frac{3x}{2}+\sqrt{-\frac{\mu nx}{3}+\frac{9}{4}x^{2}}}+\sqrt[3]{-\frac{\mu n}{9}+\frac{3x}{2}-\sqrt{-\frac{\mu nx}{3}+\frac{9}{4}x^{2}}}\right]-\frac{\sqrt{\mu n}}{3}. |  |

Moreover, if n→∞n\rightarrow\infty, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | {κn,kup​(x)=x+x3/2μ​n+𝒪​(1n)κn,kdown​(x)=x−x3/2μ​n+𝒪​(1n).\left\{\begin{array}[]{ccl}\kappa\_{n,k}^{\text{up}}(x)&=&x+\frac{x^{3/2}}{\sqrt{\mu n}}+\mathcal{O}\left(\frac{1}{n}\right)\\ \kappa\_{n,k}^{\text{down}}(x)&=&x-\frac{x^{3/2}}{\sqrt{\mu n}}+\mathcal{O}\left(\frac{1}{n}\right).\end{array}\right. |  | (5) |

The proof of Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is postponed in Appendix [B](https://arxiv.org/html/2512.16411v1#A2 "Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

Formula ([3](https://arxiv.org/html/2512.16411v1#S2.E3 "In Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) gives pre-asymptotic bounds for the cdf of the empirical relative entropy. The bounds deal with two approximations. First, ℰn,k\mathcal{E}\_{n,k} is the Berry-Esseen component, related to the speed of convergence toward the asymptotic distribution. Second, the chi-squared cdf are not simple functions of xx as it would be the case if relative entropy was a simple quadratic function. The variable xx is to be replaced by κn,kup​(x)\kappa\_{n,k}^{\text{up}}(x) and κn,kdown​(x)\kappa\_{n,k}^{\text{down}}(x), which take into account the error of the quadratic approximation of relative entropy. These quantities are defined as the smallest positive solutions of a cubic equation. When nn increases, κn,kup​(x)\kappa\_{n,k}^{\text{up}}(x) and κn,kdown​(x)\kappa\_{n,k}^{\text{down}}(x) tend toward xx, as one can see in equation ([5](https://arxiv.org/html/2512.16411v1#S2.E5 "In Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")).

We think our approach can be reproduced for obtaining pre-asymptotic bounds for the cdf of some nonlinear function of sum statistics, under some convexity condition: considering a Taylor expansion of the nonlinear function, using Raič’s theorem to get the speed of convergence, taking into account a bound of the residual, which in our case is more subtle than the maximum third derivative, which is infinite.

The Berry-Esseen part of the bounds is uniform in xx. There is a recent effort in the literature to obtain non-uniform bounds in the linear framework [[57](https://arxiv.org/html/2512.16411v1#bib.bib57)]. Our problem could certainly benefit in the future from potential extensions of these non-uniform bounds to nonlinear functions of sum statistics.

For the two-sample problem, Theorem [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") proposes an asymptotic distribution. We haven’t found such a result in the literature but it is worth mentioning a close contribution with the asymptotic distribution of the two-sample Jeffreys divergence, which is a symmetric version of relative entropy [[37](https://arxiv.org/html/2512.16411v1#bib.bib37)].

###### Theorem 2.

Let X1,…,Xn+mX\_{1},...,X\_{n+m} be iid variables such that ℙ​(Xj∈Ωi)=pi\mathbb{P}(X\_{j}\in\Omega\_{i})=p\_{i} with p=(p1,…,pk)t∈(0,1)kp=(p\_{1},...,p\_{k})^{t}\in(0,1)^{k}. Then, when n→∞n\rightarrow\infty, m→∞m\rightarrow\infty, and nn+m→λ∈(0,1)\frac{n}{n+m}\rightarrow\lambda\in(0,1), we have

|  |  |  |
| --- | --- | --- |
|  | 2​n​mn+m​DK​L​(p^n∥q^m)​⟶d​χk−12.2\frac{nm}{n+m}D\_{KL}(\widehat{p}\_{n}\|\widehat{q}\_{m})\overset{\text{d}}{\longrightarrow}\chi^{2}\_{k-1}. |  |

The proof of Theorem [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is postponed in Appendix [C](https://arxiv.org/html/2512.16411v1#A3 "Appendix C Proof of Theorem 2 and Proposition 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

When the two samples have the same size, that is n=mn=m, DK​L​(p^n∥q^m)D\_{KL}(\widehat{p}\_{n}\|\widehat{q}\_{m}) is asymptotically distributed like χk−12/n\chi^{2}\_{k-1}/n. It is to be compared to the more concentrated asymptotic distribution of DK​L​(p^n∥p)D\_{KL}(\widehat{p}\_{n}\|p), which is χk−12/2​n\chi^{2}\_{k-1}/2n.

In the two-sample case, we do not propose Berry-Esseen bounds. Indeed, in the one-sample case, we were able to find an upper bound of the rest expressed as a simple function of the two probabilities. But in the two-sample case the rest of the quadratic approximation of relative entropy depends on the divergence between each empirical probability and the true probability, that is p^n,i−pi\widehat{p}\_{n,i}-p\_{i} and q^m,i−pi\widehat{q}\_{m,i}-p\_{i}, and not on the difference between the two empirical probabilities, p^n,i−q^m,i\widehat{p}\_{n,i}-\widehat{q}\_{m,i}. We can however propose a Berry-Esseen bound for the quadratic approximation instead of the relative entropy itself, as shown in Proposition [1](https://arxiv.org/html/2512.16411v1#Thmpro1 "Proposition 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). In Section [2.3](https://arxiv.org/html/2512.16411v1#S2.SS3 "2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), we will present finite-sample results in the two-sample case, directly applied to relative entropy.

###### Proposition 1.

With the assumptions of Theorem [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") and x>0x>0, we have

|  |  |  |
| --- | --- | --- |
|  | |ℙ​(n​mn+m​∑i=1k(p^i−q^i)2pi≤x)−Fχk−12​(x)|≤n2+m2(n​m)1/2​(n+m)​ℰn+m,k,\left|\mathbb{P}\left(\frac{nm}{n+m}\sum\_{i=1}^{k}\frac{\left(\widehat{p}\_{i}-\widehat{q}\_{i}\right)^{2}}{p\_{i}}\leq x\right)-F\_{\chi^{2}\_{k-1}}(x)\right|\leq\frac{n^{2}+m^{2}}{(nm)^{1/2}(n+m)}\mathcal{E}\_{n+m,k}, |  |

with ℰ.,.\mathcal{E}\_{.,.} defined in equation ([4](https://arxiv.org/html/2512.16411v1#S2.E4 "In Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")).

The proof of Proposition [1](https://arxiv.org/html/2512.16411v1#Thmpro1 "Proposition 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is postponed in Appendix [C](https://arxiv.org/html/2512.16411v1#A3 "Appendix C Proof of Theorem 2 and Proposition 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

When n=mn=m, the bound in Proposition [1](https://arxiv.org/html/2512.16411v1#Thmpro1 "Proposition 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is ℰ2​n,k\mathcal{E}\_{2n,k}, that is ℰn,k/21/2\mathcal{E}\_{n,k}/2^{1/2}.

### 2.3 Concentration inequalities for empirical relative entropy

Beside the Berry-Esseen bounds, one can obtain finite-sample bounds of the distribution of the empirical relative entropy by the mean of concentration inequalities. They in general offer simpler expressions than Berry-Esseen bounds, without referring to the limit distribution. Instead, they exploit various methods such as the method of types for the famous Sanov inequality, and a recursion technique or the moment-generating function in the two promising alternatives we present below. In addition, as we will see in Section [4.1](https://arxiv.org/html/2512.16411v1#S4.SS1 "4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), concentration inequalities give tighter bounds than the Berry-Esseen approach when nn is small.

In what follows, we expose three existing inequalities, with two among the most recent and promising ones, along with a small refinement for the last one. We propose as well a new concentration inequalities in the two-sample case.

Sanov inequality is the most well-known concentration inequality for relative entropy. It writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(DKL​(p^n∥p)≥x)≤(n+k−1)!n!​(k−1)!​e−n​x≤(n+1)k​e−n​x,\mathbb{P}\left(D\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right)\geq x\right)\leq\frac{(n+k-1)!}{n!(k-1)!}e^{-nx}\leq(n+1)^{k}e^{-nx}, |  | (6) |

some works focusing on the first inequality [[22](https://arxiv.org/html/2512.16411v1#bib.bib22), [54](https://arxiv.org/html/2512.16411v1#bib.bib54)], while others prefer the second one [[21](https://arxiv.org/html/2512.16411v1#bib.bib21), Theorem 11.2.1], which is a simpler bound, in particular when kk is large.

Based on a recursion technique, Mardia’s bounds improve Sanov inequality, in particular when one increases kk. There are several Mardia’s bounds, each of which apply to a specific range of values for kk. Among them, we focus on the one that demonstrated superior performance for the values of kk considered in our tests:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(DKL​(p^n∥p)≥x)≤6​e2π3/2​(n​e32​π​k)k/2​e−n​x.\mathbb{P}\left(D\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right)\geq x\right)\leq\frac{6e^{2}}{\pi^{3/2}}\left(\frac{ne^{3}}{2\pi k}\right)^{k/2}e^{-nx}. |  | (7) |

It holds when 3≤k≤2+n​e3/2​π3\leq k\leq 2+\sqrt{ne^{3}/2\pi} [[54](https://arxiv.org/html/2512.16411v1#bib.bib54)].

Agrawal proposed another concentration inequality exploiting the moment-generating function of the empirical relative entropy [[2](https://arxiv.org/html/2512.16411v1#bib.bib2)]. We expose it in the following proposition, along with a slightly improved version.

###### Proposition 2.

If x>(k−1)/nx>(k-1)/n, then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(DKL​(p^n∥p)≥x)≤ℳk,n1​(x)≤ℳk,n2​(x)≤ℳk,n3​(x),\mathbb{P}(D\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right)\geq x)\leq\mathcal{M}^{1}\_{k,n}(x)\leq\mathcal{M}^{2}\_{k,n}(x)\leq\mathcal{M}^{3}\_{k,n}(x), |  |

with

|  |  |  |
| --- | --- | --- |
|  | {ℳk,n1​(x)=inft∈[0,n)e−t​x​(∑j=0nn!n2​j​(n−j)!​tj)k−1ℳk,n2​(x)=e−n​x​(∑j=0nn!​enj​(n−j)!​(1−k−1n​x)j)k−1ℳk,n3​(x)=e−n​x​(e​n​xk−1)k−1.\left\{\begin{array}[]{ccl}\mathcal{M}^{1}\_{k,n}(x)&=&\inf\_{t\in[0,n)}e^{-tx}\left(\sum\_{j=0}^{n}\frac{n!}{n^{2j}(n-j)!}t^{j}\right)^{k-1}\\ \mathcal{M}^{2}\_{k,n}(x)&=&e^{-nx}\left(\sum\_{j=0}^{n}\frac{n!e}{n^{j}(n-j)!}\left(1-\frac{k-1}{nx}\right)^{j}\right)^{k-1}\\ \mathcal{M}^{3}\_{k,n}(x)&=&e^{-nx}\left(\frac{enx}{k-1}\right)^{k-1}.\end{array}\right. |  |

The proof of Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is postponed in Appendix [D](https://arxiv.org/html/2512.16411v1#A4 "Appendix D Proof of Proposition 2 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

The third bound in Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is the one put forward by Agrawal. As we will see in Section [4.1](https://arxiv.org/html/2512.16411v1#S4.SS1 "4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), it is both simple and very performing, compared to the ones of equations ([6](https://arxiv.org/html/2512.16411v1#S2.E6 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) and ([7](https://arxiv.org/html/2512.16411v1#S2.E7 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), at least when kk is small. The second bound, ℳk,n2​(x)\mathcal{M}^{2}\_{k,n}(x), slightly improves ℳk,n3​(x)\mathcal{M}^{3}\_{k,n}(x), but it is more appropriate when nn is small because it requires the calculation of a sum of nn terms. The algorithmic complexity for obtaining the first bound, ℳk,n1​(x)\mathcal{M}^{1}\_{k,n}(x), is even worse. Indeed, in addition to the sum of nn terms, it requires a numerical optimization.

We also remark, beyond the traditional e−n​xe^{-nx} of the concentration inequalities, that xx appears in other parts of the expression of the bounds of Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), whereas neither equation ([6](https://arxiv.org/html/2512.16411v1#S2.E6 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) nor equation ([7](https://arxiv.org/html/2512.16411v1#S2.E7 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) exhibits this. The consequence is that Agrawal’s bounds are closer to the true probability when xx is small, compared to other methods. When one looks for a quantile at a given probability, kk small or nn not too small lead to a small quantile and thus Agrawal’s formula provides us with a tighter upper bound of the quantile, compared to the alternatives of equations ([6](https://arxiv.org/html/2512.16411v1#S2.E6 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) and ([7](https://arxiv.org/html/2512.16411v1#S2.E7 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")). This will be confirmed in the study presented in Section [4.1](https://arxiv.org/html/2512.16411v1#S4.SS1 "4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

For building a concentration inequality in the two-sample framework, we can split relative entropy in two parts so that we can directly sum the upper bounds of the one-sample case. But such a decomposition does not naturally arise because there is no triangle inequality for relative entropy. Pinsker’s inequality shows however a correspondence between relative entropy and total variation, which could be used to obtain the desired decomposition. For discrete probabilities, it writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∑i=1k|pi−qi|)2≤2​DKL​(p∥q)≤(1mini∈⟦1,k⟧⁡qi−mini∈⟦1,k⟧⁡piqi)​(∑i=1k|pi−qi|)2,\left(\sum\_{i=1}^{k}|p\_{i}-q\_{i}|\right)^{2}\leq 2D\_{\text{KL}}\left(p\|q\right)\leq\left(\frac{1}{\min\_{i\in\llbracket 1,k\rrbracket}q\_{i}}-\min\_{i\in\llbracket 1,k\rrbracket}\frac{p\_{i}}{q\_{i}}\right)\left(\sum\_{i=1}^{k}|p\_{i}-q\_{i}|\right)^{2}, |  | (8) |

the left bound being the traditional Pinsker’s inequality [[68](https://arxiv.org/html/2512.16411v1#bib.bib68), [17](https://arxiv.org/html/2512.16411v1#bib.bib17)] and the right bound one of the reverse Pinsker’s inequalities [[62](https://arxiv.org/html/2512.16411v1#bib.bib62)], among several other versions [[14](https://arxiv.org/html/2512.16411v1#bib.bib14), [63](https://arxiv.org/html/2512.16411v1#bib.bib63)]. We note that (1/mini⁡qi)−(mini⁡pi/qi)≥k−1(1/\min\_{i}q\_{i})-(\min\_{i}p\_{i}/q\_{i})\geq k-1. We thus get, as an interesting side result, the following decomposition of relative entropy.

###### Proposition 3.

Let pp, qq, and rr be categorical distributions with kk categories. If mini∈⟦1,k⟧⁡qi>0\min\_{i\in\llbracket 1,k\rrbracket}q\_{i}>0, we have:

|  |  |  |
| --- | --- | --- |
|  | DKL​(p∥q)≤(2mini∈⟦1,k⟧⁡qi−2​mini∈⟦1,k⟧⁡piqi)​(DKL​(p∥r)+DKL​(q∥r)).D\_{\text{KL}}\left(p\|q\right)\leq\left(\frac{2}{\min\_{i\in\llbracket 1,k\rrbracket}q\_{i}}-2\min\_{i\in\llbracket 1,k\rrbracket}\frac{p\_{i}}{q\_{i}}\right)\left(D\_{\text{KL}}\left(p\|r\right)+D\_{\text{KL}}\left(q\|r\right)\right). |  |

The proof of Proposition [3](https://arxiv.org/html/2512.16411v1#Thmpro3 "Proposition 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is postponed in Appendix [E.1](https://arxiv.org/html/2512.16411v1#A5.SS1 "E.1 Proof of Proposition 3 ‣ Appendix E Proofs for two-sample concentration inequalities ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

In the particular case r=pr=p, it simplifies to

|  |  |  |
| --- | --- | --- |
|  | DKL​(p∥q)≤(2mini∈⟦1,k⟧⁡qi−2​mini∈⟦1,k⟧⁡piqi)​DKL​(q∥p).D\_{\text{KL}}\left(p\|q\right)\leq\left(\frac{2}{\min\_{i\in\llbracket 1,k\rrbracket}q\_{i}}-2\min\_{i\in\llbracket 1,k\rrbracket}\frac{p\_{i}}{q\_{i}}\right)D\_{\text{KL}}\left(q\|p\right). |  |

The scalar in front of the relative entropy on the right-hand side of the above equation can be very large when one considers a probability qq that is far from being uniform and a probability pp that largely diverges from qq. We also note that, in Proposition [3](https://arxiv.org/html/2512.16411v1#Thmpro3 "Proposition 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), the probabilities can be exchanged in each relative entropy of the right-hand side of the inequality. Therefore, DKL​(p∥r)+DKL​(q∥r)D\_{\text{KL}}\left(p\|r\right)+D\_{\text{KL}}\left(q\|r\right) can for example be replaced by DKL​(p∥r)+DKL​(r∥q)D\_{\text{KL}}\left(p\|r\right)+D\_{\text{KL}}\left(r\|q\right).

Using the one-sample Agrawal’s concentration inequality introduced in Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") along with the decomposition put forward in Proposition [3](https://arxiv.org/html/2512.16411v1#Thmpro3 "Proposition 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), we get a concentration inequality for the two-sample relative entropy, when the two samples are assumed to follow the same theoretical distribution. It is the purpose of Theorem [3](https://arxiv.org/html/2512.16411v1#Thmthm3 "Theorem 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

###### Theorem 3.

Let m,n>0m,n>0 and X1,…,Xn+mX\_{1},...,X\_{n+m} be iid variables such that ℙ​(Xj∈Ωi)=pi\mathbb{P}(X\_{j}\in\Omega\_{i})=p\_{i} with p=(p1,…,pk)t∈(0,1)kp=(p\_{1},...,p\_{k})^{t}\in(0,1)^{k}. We note

|  |  |  |
| --- | --- | --- |
|  | βm,n=2mini∈⟦1,k⟧⁡q^m,i−2​mini∈⟦1,k⟧⁡p^n,iq^m,i\beta\_{m,n}=\frac{2}{\min\_{i\in\llbracket 1,k\rrbracket}\widehat{q}\_{m,i}}-2\min\_{i\in\llbracket 1,k\rrbracket}\frac{\widehat{p}\_{n,i}}{\widehat{q}\_{m,i}} |  |

and we assume that mini∈⟦1,k⟧⁡q^m,i>0\min\_{i\in\llbracket 1,k\rrbracket}\widehat{q}\_{m,i}>0 and that x≥βm,n​(k−1)​(m+n)/m​nx\geq\beta\_{m,n}(k-1)(m+n)/mn. Then,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(DKL​(p^n∥q^m)≥x)≤ℳ~k,n,m1​(x)≤ℳ~k,n,m2​(x)≤ℳ~k,n,m3​(x),\boxed{\mathbb{P}\left(D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{m}\right)\geq x\right)\leq\widetilde{\mathcal{M}}^{1}\_{k,n,m}(x)\leq\widetilde{\mathcal{M}}^{2}\_{k,n,m}(x)\leq\widetilde{\mathcal{M}}^{3}\_{k,n,m}(x)}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | {ℳ~k,n,m1​(x)=infs∈[0,min⁡(m,n))e−s​x/βm,n​(∑i=0mm!m2​i​(m−i)!​si​∑j=0nn!n2​j​(n−j)!​sj)k−1ℳ~k,n,m2​(x)=e−σm,n,x​x/βm,n​(∑i=0mm!m2​i​(m−i)!​σm,n,xi​∑j=0nn!n2​j​(n−j)!​σm,n,xj)k−1ℳ~k,n,m3​(x)=e−σm,n,x​x/βm,n​((1−σm,n,xm)​(1−σm,n,xn))1−k\left\{\begin{array}[]{ccl}\widetilde{\mathcal{M}}^{1}\_{k,n,m}(x)&=&\inf\_{s\in[0,\min(m,n))}e^{-sx/\beta\_{m,n}}\left(\sum\_{i=0}^{m}\frac{m!}{m^{2i}(m-i)!}s^{i}\sum\_{j=0}^{n}\frac{n!}{n^{2j}(n-j)!}s^{j}\right)^{k-1}\\ \widetilde{\mathcal{M}}^{2}\_{k,n,m}(x)&=&e^{-\sigma\_{m,n,x}x/\beta\_{m,n}}\left(\sum\_{i=0}^{m}\frac{m!}{m^{2i}(m-i)!}\sigma\_{m,n,x}^{i}\sum\_{j=0}^{n}\frac{n!}{n^{2j}(n-j)!}\sigma\_{m,n,x}^{j}\right)^{k-1}\\ \widetilde{\mathcal{M}}^{3}\_{k,n,m}(x)&=&e^{-\sigma\_{m,n,x}x/\beta\_{m,n}}\left(\left(1-\frac{\sigma\_{m,n,x}}{m}\right)\left(1-\frac{\sigma\_{m,n,x}}{n}\right)\right)^{1-k}\end{array}\right. |  |

and

|  |  |  |
| --- | --- | --- |
|  | σm,n,x=n+m2−βm,n​(k−1)x−βm,n2​(k−1)2x2+(m−n)24.\sigma\_{m,n,x}=\frac{n+m}{2}-\frac{\beta\_{m,n}(k-1)}{x}-\sqrt{\frac{\beta\_{m,n}^{2}(k-1)^{2}}{x^{2}}+\frac{(m-n)^{2}}{4}}. |  |

The proof of Theorem [3](https://arxiv.org/html/2512.16411v1#Thmthm3 "Theorem 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is postponed in Appendix [E.2](https://arxiv.org/html/2512.16411v1#A5.SS2 "E.2 Proof of Theorem 3 ‣ Appendix E Proofs for two-sample concentration inequalities ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

When the two samples have the same size, that is m=nm=n, σm,n,x\sigma\_{m,n,x} becomes n−2​βn,n​(k−1)/xn-2\beta\_{n,n}(k-1)/x, the bounds simplify, and we get, for example,

|  |  |  |
| --- | --- | --- |
|  | ℳ~k,n,n3​(x)=e−n​x/βn,n​(e​n​x2​βn,n​(k−1))2​(k−1)\widetilde{\mathcal{M}}^{3}\_{k,n,n}(x)=e^{-nx/\beta\_{n,n}}\left(\frac{enx}{2\beta\_{n,n}(k-1)}\right)^{2(k-1)} |  |

or

|  |  |  |
| --- | --- | --- |
|  | ℳ~k,n,n2​(x)=e−n​x/βn,n​(e​∑i=0n(1−2​βn,n​(k−1)n​x)i​[∏j=0i−1(1−jn)])2​(k−1),\widetilde{\mathcal{M}}^{2}\_{k,n,n}(x)=e^{-nx/\beta\_{n,n}}\left(e\sum\_{i=0}^{n}\left(1-\frac{2\beta\_{n,n}(k-1)}{nx}\right)^{i}\left[\prod\_{j=0}^{i-1}\left(1-\frac{j}{n}\right)\right]\right)^{2(k-1)}, |  |

expression in which we have replace the ratio of factorials by a product that is equal but easier to compute for large values of nn.
When m→∞m\rightarrow\infty, we have

|  |  |  |
| --- | --- | --- |
|  | βm,n→βn=2mini∈⟦1,k⟧⁡qi−2​mini∈⟦1,k⟧⁡p^n,iqi,\beta\_{m,n}\rightarrow\beta\_{n}=\frac{2}{\min\_{i\in\llbracket 1,k\rrbracket}q\_{i}}-2\min\_{i\in\llbracket 1,k\rrbracket}\frac{\widehat{p}\_{n,i}}{q\_{i}}, |  |

as well as σm,n,x→σn,x=n−βn​(k−1)/x\sigma\_{m,n,x}\rightarrow\sigma\_{n,x}=n-\beta\_{n}(k-1)/x and

|  |  |  |
| --- | --- | --- |
|  | ℳ~k,n,m3​(x)→e−n​x/βn​(e​n​xβn​(k−1))k−1.\widetilde{\mathcal{M}}^{3}\_{k,n,m}(x)\rightarrow e^{-nx/\beta\_{n}}\left(\frac{enx}{\beta\_{n}(k-1)}\right)^{k-1}. |  |

We remark that this limit is different from the expression of ℳk,n3​(x)\mathcal{M}\_{k,n}^{3}(x) provided for the one-sample case in Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). The reason is the presence of βn\beta\_{n}, which should be 1 in order for the limit to match the one-sample case, but which in reality is higher than 2​(k−1)2(k-1). It thus appears that the reverse Pinsker’s inequality is quite pessimistic and that the βm,n\beta\_{m,n} of Theorem [3](https://arxiv.org/html/2512.16411v1#Thmthm3 "Theorem 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") is too large. In Section [4.1](https://arxiv.org/html/2512.16411v1#S4.SS1 "4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), we show that replacing βm,n\beta\_{m,n} by 1 leads to upper bounds that are numerically satisfying. We note ℳ~k,n,m2,⋆​(x)\widetilde{\mathcal{M}}^{2,\star}\_{k,n,m}(x) and ℳ~k,n,m3,⋆​(x)\widetilde{\mathcal{M}}^{3,\star}\_{k,n,m}(x) these new quantities. Even though we cannot prove it, we conjecture that Theorem [3](https://arxiv.org/html/2512.16411v1#Thmthm3 "Theorem 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") may apply for a large range of probabilities when one replaces βm,n\beta\_{m,n} by 1.

## 3 Change-point detection

Since relative entropy measures the divergence between two distributions, we can use it in the framework of change-point detection. The various bounds for the distribution of its empirical counterpart thus provide possible thresholds for a statistical test of change-point. We introduce the test along with some other traditional offline alternatives. One of them, based on a difference of AIC is close in some ways to our method. We will thus compare the two approaches.

### 3.1 Relative entropy and statistical tests for change-point detection

We adopt the classical formalism of change-point detection [[76](https://arxiv.org/html/2512.16411v1#bib.bib76)]. We consider a sequence X1,…,X2​nX\_{1},...,X\_{2n}. Under the null hypothesis, X1,…,X2​nX\_{1},...,X\_{2n} are identically distributed. Under the alternative hypothesis, there exists t⋆∈⟦2,2​n−1⟧t^{\star}\in\llbracket 2,2n-1\rrbracket such that X1,…,Xt⋆X\_{1},...,X\_{t^{\star}} are identically distributed and follow a discrete probability qq, whereas Xt⋆+1,…,X2​nX\_{t^{\star}+1},...,X\_{2n} are also identically distributed but follow another discrete probability pp.

Two families of tests exist, based either on an online statistic or on an offline statistic. In the online case, t⋆t^{\star} is close to 2​n2n and the sequential update of the statistic is supposed to lead to a rapid detection of the change-point [[72](https://arxiv.org/html/2512.16411v1#bib.bib72)]. CUSUM is a widespread statistic used in this framework [[56](https://arxiv.org/html/2512.16411v1#bib.bib56)] and online change-point detection often consists in detecting a change in the cumulative mean or in another moment. In the offline case, one generally focuses on t⋆=nt^{\star}=n [[47](https://arxiv.org/html/2512.16411v1#bib.bib47)], so that people consider a divergence statistic between the probabilities of the two sub-samples. The offline approach makes it possible to compare probabilities, parametric or nonparametric ones, instead of only moments.

In this article, we are interested in offline change-point detection, specifically when nn is not very large. Our test thus consists in X1,…,Xn∼qX\_{1},...,X\_{n}\sim q and Xn+1,…,X2​n∼pX\_{n+1},...,X\_{2n}\sim p, with H0H\_{0} corresponding to p=qp=q and H1H\_{1} to p≠qp\neq q. Translating the spirit of CUSUM in the offline approach, we propose two baseline change-point tests based on the comparison of the mean (respectively the variance) of the sub-samples X1,…,XnX\_{1},...,X\_{n} and Xn+1,…,X2​nX\_{n+1},...,X\_{2n}, using thus a t-test (resp. F-test), for which the asymptotic distribution is well known.

The method we put forward here is based on the empirical relative entropy DKL​(p^n∥q^n)D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{n}\right), with the two distributions p^n\widehat{p}\_{n} and q^n\widehat{q}\_{n} estimated on the two sub-samples. Since the exact cdf FH0,nF\_{H\_{0},n} of DKL​(p^n∥q^n)D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{n}\right) under H0H\_{0} is unknown, both in the one- and in the two-sample cases, simulations are often used to select a threshold corresponding to a given significance level [[59](https://arxiv.org/html/2512.16411v1#bib.bib59)]. Instead, using the two-sample asymptotic distribution of DKL​(p^n∥q^n)D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{n}\right), as described in Theorem [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), we have a good approximation of its true cdf under H0H\_{0}, provided that nn is not too small. For a more conservative approximation of FH0,nF\_{H\_{0},n}, specifically for small values of nn, we can use the two-sample concentration inequalities introduced in Theorem [3](https://arxiv.org/html/2512.16411v1#Thmthm3 "Theorem 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). Whatever the approximation F^H0,n\widehat{F}\_{H\_{0},n} of FH0,nF\_{H\_{0},n}, the quantile F^H0,n−1​(1−α)\widehat{F}^{-1}\_{H\_{0},n}(1-\alpha) provides us with a threshold that can be used to define a test of nominal significance level α\alpha. If DKL​(p^n∥q^n)D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{n}\right) is above F^H0,n−1​(1−α)\widehat{F}^{-1}\_{H\_{0},n}(1-\alpha), we reject H0H\_{0}.

The simulation study of Section [4](https://arxiv.org/html/2512.16411v1#S4 "4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") evaluates the different bounds of the cdf FH0,nF\_{H\_{0},n} and provides as well the actual significance level and the power of the statistical tests introduced above.

### 3.2 Another approach using AIC

Another possible offline method to detect a change-point consists in determining whether a single model for describing X1,…,X2​nX\_{1},...,X\_{2n} is more relevant than using a model for X1,…,XnX\_{1},...,X\_{n} and another one for Xn+1,…,X2​nX\_{n+1},...,X\_{2n}. This can be done by comparing information criteria in the two settings. This approach has been explored both for parametric models [[48](https://arxiv.org/html/2512.16411v1#bib.bib48), [29](https://arxiv.org/html/2512.16411v1#bib.bib29)] and nonparametric ones [[77](https://arxiv.org/html/2512.16411v1#bib.bib77), [44](https://arxiv.org/html/2512.16411v1#bib.bib44)].

Like in Section [3.1](https://arxiv.org/html/2512.16411v1#S3.SS1 "3.1 Relative entropy and statistical tests for change-point detection ‣ 3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), we consider the distributions q^n\widehat{q}\_{n} and p^n\widehat{p}\_{n}, empirical counterparts of the kk-categorical distributions qq and pp describing respectively the subsequence X1,…,XnX\_{1},...,X\_{n} and Xn+1,…,X2​nX\_{n+1},...,X\_{2n}. Thus, the likelihood of (X1,…,Xn)(X\_{1},...,X\_{n}) is ∏j=1nqXj=∏i=1kqin​q^n,i\prod\_{j=1}^{n}q\_{X\_{j}}=\prod\_{i=1}^{k}q\_{i}^{n\widehat{q}\_{n,i}}. Plugging the estimator q^n\widehat{q}\_{n} of qq in this expression and doing the same for (Xn+1,…,X2​n)(X\_{n+1},...,X\_{2n}) leads to the following log-likelihood of (X1,…,X2​n)(X\_{1},...,X\_{2n}) in the two-model case, which corresponds to H1H\_{1}:

|  |  |  |
| --- | --- | --- |
|  | ℓH1=n​∑i=1k{p^n,i​log⁡(p^n,i)+q^n,i​log⁡(q^n,i)}.\ell\_{H\_{1}}=n\sum\_{i=1}^{k}\left\{\widehat{p}\_{n,i}\log\left(\widehat{p}\_{n,i}\right)+\widehat{q}\_{n,i}\log\left(\widehat{q}\_{n,i}\right)\right\}. |  |

If a single model describes the sequence X1,…,X2​nX\_{1},...,X\_{2n}, that is under H0H\_{0}, the empirical probability of the category ii is (p^n,i+q^n,i)/2(\widehat{p}\_{n,i}+\widehat{q}\_{n,i})/2, so that the log-likelihood of (X1,…,X2​n)(X\_{1},...,X\_{2n}) is now

|  |  |  |
| --- | --- | --- |
|  | ℓH0=n​∑i=1k(p^n,i+q^n,i)​log⁡(p^n,i+q^n,i2).\ell\_{H\_{0}}=n\sum\_{i=1}^{k}\left(\widehat{p}\_{n,i}+\widehat{q}\_{n,i}\right)\log\left(\frac{\widehat{p}\_{n,i}+\widehat{q}\_{n,i}}{2}\right). |  |

Noting that we have k−1k-1 parameters in the one-model case and 2​(k−1)2(k-1) otherwise, we obtain the following criterion of difference of AICs between the approaches:

|  |  |  |
| --- | --- | --- |
|  | Δ​AIC⁡(p^n,q^n)=−2​(k−1)−2​(ℓH0−ℓH1).\Delta\operatorname{AIC}(\widehat{p}\_{n},\widehat{q}\_{n})=-2(k-1)-2\left(\ell\_{H\_{0}}-\ell\_{H\_{1}}\right). |  |

If Δ​AIC⁡(p^n,q^n)>0\Delta\operatorname{AIC}(\widehat{p}\_{n},\widehat{q}\_{n})>0 then the two-model approach is informationally more relevant and we validate the presence of a change-point.

### 3.3 Link between relative entropy and the AIC-based method

Writing, for all i∈⟦1,k⟧i\in\llbracket 1,k\rrbracket, that p^n,i=q^n,i+εi\widehat{p}\_{n,i}=\widehat{q}\_{n,i}+\varepsilon\_{i}, a second-order Taylor expansion provides us with

|  |  |  |
| --- | --- | --- |
|  | (p^n,i+q^n,i)​log⁡(p^n,i+q^n,i2)−p^n,i​log⁡(p^n,i)−q^n,i​log⁡(q^n,i)=−εi24​q^n,i+o​(εi2)\left(\widehat{p}\_{n,i}+\widehat{q}\_{n,i}\right)\log\left(\frac{\widehat{p}\_{n,i}+\widehat{q}\_{n,i}}{2}\right)-\widehat{p}\_{n,i}\log\left(\widehat{p}\_{n,i}\right)-\widehat{q}\_{n,i}\log\left(\widehat{q}\_{n,i}\right)=-\frac{\varepsilon\_{i}^{2}}{4\widehat{q}\_{n,i}}+o\left(\varepsilon\_{i}^{2}\right) |  |

and with

|  |  |  |
| --- | --- | --- |
|  | DKL​(p^n∥q^n)=∑i=1kεi+εi22​q^n,i+o​(εi2).D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{n}\right)=\sum\_{i=1}^{k}\varepsilon\_{i}+\frac{\varepsilon\_{i}^{2}}{2\widehat{q}\_{n,i}}+o\left(\varepsilon\_{i}^{2}\right). |  |

Since p^n,i\widehat{p}\_{n,i} and q^n,i\widehat{q}\_{n,i} are probabilities, we have ∑i=1kεi=0\sum\_{i=1}^{k}\varepsilon\_{i}=0 and finally

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​AIC⁡(q^n+ε,q^n)=−2​(k−1)+n​DKL​(q^n+ε∥q^n)+o​(‖ε‖22).\Delta\operatorname{AIC}(\widehat{q}\_{n}+\varepsilon,\widehat{q}\_{n})=-2(k-1)+nD\_{\text{KL}}\left(\widehat{q}\_{n}+\varepsilon\|\widehat{q}\_{n}\right)+o\left(\|\varepsilon\|\_{2}^{2}\right). |  | (9) |

Therefore, both approaches, based either on relative entropy or on a difference of AICs, are very close to each other, up to an affine transformation, as soon as the two subsequences have close probabilities. The method based on Δ​AIC\Delta\operatorname{AIC} is not a statistical test but equation ([9](https://arxiv.org/html/2512.16411v1#S3.E9 "In 3.3 Link between relative entropy and the AIC-based method ‣ 3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) gives a natural threshold on the relative entropy for determining whether there is a change-point in the sequence. This threshold is 2​(k−1)/n2(k-1)/n and is not based on any of the approximations presented in Section [2](https://arxiv.org/html/2512.16411v1#S2 "2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") of the distribution of the relative entropy.

The proximity between relative entropy and Δ​AIC\Delta\operatorname{AIC} is however not a surprise. Indeed, the justification of AIC comes from the expectation of the relative entropy between the data-generating distribution and an estimated parametric distribution, the number of parameters appearing because of this expectation [[3](https://arxiv.org/html/2512.16411v1#bib.bib3), [19](https://arxiv.org/html/2512.16411v1#bib.bib19)]. However, the fact that the first distribution is in practice replaced by an empirical distribution is overlooked in the AIC method, which thus clearly states an asymptotic framework. Extensions of AIC, like the corrected AIC [[45](https://arxiv.org/html/2512.16411v1#bib.bib45), [18](https://arxiv.org/html/2512.16411v1#bib.bib18)], may be used instead in order to better deal with small samples.

Change-point detection methods based either on the difference of AICs or on the relative entropy both depend on the discretization parameter kk. As we will see in the simulations of Section [4.2](https://arxiv.org/html/2512.16411v1#S4.SS2 "4.2 Detection of change-point assessed by simulations ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") and in the empirical study of Section [5](https://arxiv.org/html/2512.16411v1#S5 "5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), one detects a bigger number of change-points when kk is larger. Indeed, the differences between two distributions are more apparent with finer discretizations. We might therefore be inclined to increase kk but a limitation appears when we estimate a zero probability in some categories, because of a too large kk with respect to nn. Using continuous probabilities and the differential relative entropy would thus be an interesting extension of this work.

## 4 A simulation study

We want to compare all the bounds of the distribution of empirical relative entropy, provided in Section [2](https://arxiv.org/html/2512.16411v1#S2 "2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), with the distribution obtained by simulation, for various sample sizes. Then, we propose a comparison of the change-point detection methods introduced in Section [3](https://arxiv.org/html/2512.16411v1#S3 "3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), also based on simulations.

### 4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy

In this paragraph, we consider a uniform distribution for both pp and qq. Indeed, numerical experiments indicate that the distribution of empirical relative entropy obtained from simulations does not seem to be significantly affected by changes in the probabilities, provided that the number of categories remains unchanged and that we stay under H0H\_{0}: p=qp=q.

We first evaluate the distributions coming from the central limit theorem and Berry-Esseen-like bounds, introduced in Section [2.2](https://arxiv.org/html/2512.16411v1#S2.SS2 "2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). We display in Figure [1](https://arxiv.org/html/2512.16411v1#S4.F1.12 "Figure 1 ‣ 4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") the cdf of the empirical relative entropy obtained by simulations, along with the asymptotic distribution and Berry-Esseen bounds, for nn equal to 500,000500,000 or 2,000,0002,000,000 and k∈{2,4}k\in\{2,4\}.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 1: For p^n\widehat{p}\_{n} estimator of the uniform probability pp, asymptotic cdf of 2​n​DKL​(p^n∥p)2nD\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right) in xx (black dotted line) along with the Berry-Esseen bounds (grey dotted lines), as in Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), and cdf obtained by 1,000 simulations (black solid line). The size of the sample nn is 500,000 (left graphs) and 2,000,000 (right graphs), and the number of categories kk is 2 (top graphs) and 4 (bottom graphs).

In this pre-asymptotic setting, we observe that the asymptotic cdf is very close to to simulated one and that the Berry-Esseen bounds seem pessimistic when k=4k=4. This is not surprising since our bound ℰn,k\mathcal{E}\_{n,k} is based on a uniform multivariate extension of Berry-Esseen inequality. Indeed, there is currently no consensus on an optimal choice of the constant that appears there, unlike the univariate case. In order to have an idea of the minimum nn making the bounds relevant, we can stress that ℰn,k<1\mathcal{E}\_{n,k}<1 when n>1.37×105n>1.37\times 10^{5} (respectively n>3.36×103n>3.36\times 10^{3}) in the case k=4k=4 (resp. k=2k=2). One may also wonder about the role of κn,kdown​(x)\kappa\_{n,k}^{\text{down}}(x) and κn,kup​(x)\kappa\_{n,k}^{\text{up}}(x) in inequality [3](https://arxiv.org/html/2512.16411v1#S2.E3 "In Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). Their importance is very limited because they converge rapidly toward xx as nn goes to infinity. Specifically, in Figure [1](https://arxiv.org/html/2512.16411v1#S4.F1.12 "Figure 1 ‣ 4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), the differences x−κn,kdown​(x)x-\kappa\_{n,k}^{\text{down}}(x) and κn,kup​(x)−x\kappa\_{n,k}^{\text{up}}(x)-x are increasing in xx and reach 0.32%0.32\% (respectively 0.45%0.45\%, 0.64%0.64\%, 0.91%0.91\%) of xx, for x=10x=10, n=2,000,000n=2,000,000, and k=2k=2 (resp. n=2,000,000n=2,000,000 and k=4k=4, n=500,000n=500,000 and k=2k=2, n=500,000n=500,000 and k=4k=4).

We now focus on finite-sample distributions and concentration inequalities. We will let kk and nn vary around the baseline case n=100n=100, k=4k=4. We compare quantiles of the empirical relative entropy at 75%75\% and 95%95\%, in the one- and two-sample cases, following various methods: the empirical quantiles obtained from 10,000 simulations, the quantile in the asymptotic distribution of Theorems [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") and [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), and the quantiles obtained from concentration inequalities. Specifically, in the one-sample case, the considered bounds are the two Sanov’s bounds of equation ([6](https://arxiv.org/html/2512.16411v1#S2.E6 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), Mardia’s bound provided in equation ([7](https://arxiv.org/html/2512.16411v1#S2.E7 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), and Agrawal’s second and third bounds, ℳk,n2\mathcal{M}^{2}\_{k,n} and ℳk,n3\mathcal{M}^{3}\_{k,n}, defined in Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). With two samples, the only bounds considered are the extensions of the above Agrawal’s bounds, ℳ~k,n,n2,⋆\widetilde{\mathcal{M}}^{2,\star}\_{k,n,n} and ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n}, defined after Theorem [3](https://arxiv.org/html/2512.16411v1#Thmthm3 "Theorem 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), with the same size for the two subsamples.

Some of the concentration inequalities are valid under some condition. Agrawal’s condition x>(k−1)/nx>(k-1)/n is always verified in our results and we have to discard the case k=2k=2 for Mardia’s bound. In the two-sample case, we also constrain kk to be less than or equal to 8; otherwise, simulations sometimes lead to empty categories, and consequently to zero estimated probabilities q^n\widehat{q}\_{n}, when n=100n=100. This would cause the relative entropy to diverge to infinity.

The obtained quantiles, as functions of nn, are displayed in Figure [2](https://arxiv.org/html/2512.16411v1#S4.F2.12 "Figure 2 ‣ 4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). We observe that the quantile of the asymptotic distribution is very accurate: it only slightly underestimates the true quantile when nn is small (less than 50) and this underestimation becomes more pronounced the further we move into the tail of the distribution. Regarding concentration inequalities, Sanov’s bounds largely overestimate the quantile. Mardia’s bound is only slightly better than the best Sanov’s bound, whereas the two Agrawal’s bounds, which are very close to each other both in the one- and the two-sample cases, are significantly better than the other bounds, though not as accurate as the quantile of the asymptotic distribution.

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 2: Quantile of the relative entropy as a function of nn, at 75%75\% (left graphs) and 95%95\% (right graphs), for one (top graphs) or two samples (bottom graphs), according to the 10,000 simulations (red line), to the asymptotic distribution (black dashed line), to the second and third Agrawal’s bounds (grey dashed lines), to the two Sanov’s bounds (grey solid lines), and to Mardia’s bound (black solid line). Other parameters are k=4k=4 and pip\_{i} constant in ii.

Figure [3](https://arxiv.org/html/2512.16411v1#S4.F3.12 "Figure 3 ‣ 4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") shows the quantiles as functions of kk. The quantile at 95%95\% of the asymptotic distribution more clearly underestimates the true quantile when kk is larger. Once again, Sanov’s bounds are the least accurate. Mardia’s bound comes next but it increases more slowly with kk than the other concentration bounds do. This is consistent with its known reliability for large values of kk. Nevertheless, for the range of values considered for kk, Agrawal’s bounds are our best concentration bounds. The two versions are again very close to each other, both for one and two samples. For this reason, we will now only consider ℳk,n3\mathcal{M}^{3}\_{k,n} and ℳ~k,n,m3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,m}, whose expression is simpler than ℳk,n2\mathcal{M}^{2}\_{k,n} and ℳ~k,n,m2,⋆\widetilde{\mathcal{M}}^{2,\star}\_{k,n,m}.

![Refer to caption](x9.png)

![Refer to caption](x10.png)

![Refer to caption](x11.png)

![Refer to caption](x12.png)

Figure 3: Quantile of the relative entropy as a function of kk, at 75%75\% (left graphs) and 95%95\% (right graphs), for one (top graphs) or two samples (bottom graphs), according to the 10,000 simulations (red line), to the asymptotic distribution (black dashed line), to the second and third Agrawal’s bounds (grey dashed lines), to the two Sanov’s bounds (grey solid lines), and to Mardia’s bound (black solid line). Other parameters are n=100n=100 and pip\_{i} constant in ii.

### 4.2 Detection of change-point assessed by simulations

We now evaluate the propensity of the methods introduced in Section [3](https://arxiv.org/html/2512.16411v1#S3 "3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") to detect an existing change-point and not to trigger an alert when there is no change-point. The method put forward in this work is a statistical test on the empirical relative entropy, with various approximations of its distribution, but always in a two-sample context. The benchmark methods are a t-test, an F-test, and the Δ​AIC\Delta\operatorname{AIC} method.

Among all the possible models depicting a change-point, we use a simple parametric categorical model, with kk categories {1,2,…,k}\{1,2,...,k\} of ranked probability. For i∈⟦1,k⟧i\in\llbracket 1,k\rrbracket, it is defined by

|  |  |  |
| --- | --- | --- |
|  | πiϕ,k=e−ϕ​i∑j=1ke−ϕ​j,\pi^{\phi,k}\_{i}=\frac{e^{-\phi i}}{\sum\_{j=1}^{k}e^{-\phi j}}, |  |

which can be seen as either a finite version of a discrete exponential distribution [[6](https://arxiv.org/html/2512.16411v1#bib.bib6)] or a variation of the finite geometric distribution [[20](https://arxiv.org/html/2512.16411v1#bib.bib20)]. It is a simple way of modelling with a single parameter both the uniform distribution, when ϕ=0\phi=0, and disparity between categories, when ϕ≠0\phi\neq 0. In our change-point framework, we generate nn first i.i.d. variables in the distribution πϕ,k\pi^{\phi,k} then nn others in the distribution πϕ+ψ,k\pi^{\phi+\psi,k}. The presence of a change-point is thus characterized by ψ≠0\psi\neq 0. The closer ψ\psi is to zero, the less significant is the change-point. We use the same baseline case as in Section [4.1](https://arxiv.org/html/2512.16411v1#S4.SS1 "4.1 A simulation-based evaluation of the bounds of the distribution of relative entropy ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), that is n=100n=100, k=4k=4 and ϕ=0\phi=0, and we consider the following standalone variations: n=50n=50, k=6k=6, and ϕ=0.3\phi=0.3. In all the experiments, we consider a large range of values for ψ\psi: [−0.8,0.8][-0.8,0.8].

For a simulated trajectory of length 2​n2n, with or without a change-point, depending on the value of ψ\psi, we carry out the statistical tests of Section [3](https://arxiv.org/html/2512.16411v1#S3 "3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). For the tests based on relative entropy, we estimate an empirical probability for each category rather than the parameter of the distribution used to generate the data. For each test, we record its outcome and average it over 10,000 trajectories simulated with the same parameters. We then consider the proportion of times each test rejects the null hypothesis of no change-point.

Figure [4](https://arxiv.org/html/2512.16411v1#S4.F4.20 "Figure 4 ‣ 4.2 Detection of change-point assessed by simulations ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") gathers the results. The nominal confidence level is set at 95%95\%. Each curve intersects the Y-axis (ψ=0\psi=0) at a probability equal to one minus the actual confidence level. The size of each test can thus be read at this specific point of the corresponding graph. The Δ​AIC\Delta\operatorname{AIC} approach is liberal, producing more inappropriate rejections of H0H\_{0} than expected. The other tests are at or above the nominal confidence level, with two of them being even conservative: the F-test and the relative entropy test based on the ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n} approximation. The power of each test can be read directly from the graph when ψ≠0\psi\neq 0. It shows that the t-test is the most powerful, followed by the Δ​AIC\Delta\operatorname{AIC} method, the relative entropy test based on the asymptotic distribution, the one based on ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n}, and finally the F-test, which has some difficulties detecting change-points.

![Refer to caption](x13.png)

![Refer to caption](x14.png)

![Refer to caption](x15.png)

![Refer to caption](x16.png)

Figure 4: Proportion of the 10,000 simulated time series for which a change-point is detected, as a function of ψ\psi. The tests used are based i/ on the relative entropy with a threshold defined by the 95%95\% quantile in either the asymptotic two-sample distribution (solid black line) or the ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n} bound (dashed black line); ii/ on the Δ​AIC\Delta\operatorname{AIC} method (solid grey line); iii/ on the t-test with 95%95\% confidence (solid red line); iv/ on the F-test with 95%95\% confidence (dashed red line). The parameters are (k,n,ϕ)=(4,100,0)(k,n,\phi)=(4,100,0), except in the top right graph (ϕ=0.3\phi=0.3), in the bottom left graph (n=50n=50), and in the bottom right graph (k=6k=6).

Overall, the t-test seems the most appropriate for this example. However, this analysis, based on the sole average of random variables, cannot be as rich as an approach based on the full distribution, like tests on relative entropy. We thus consider another generating model, with states {1,2,3,4}\{1,2,3,4\} of probability q=(0.25,0.25,0.25,0.25)q=(0.25,0.25,0.25,0.25) for the first sub-sample and p=(p1,0.5−p1,0.5−p1,p1)p=(p\_{1},0.5-p\_{1},0.5-p\_{1},p\_{1}) for the second one. The variables have the same expectation in the first and in the second sub-samples, but not the same distribution. Figure [5](https://arxiv.org/html/2512.16411v1#S4.F5.20 "Figure 5 ‣ 4.2 Detection of change-point assessed by simulations ‣ 4 A simulation study ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") shows that the t-test is now unable to detect change-points when they exist. The Δ​AIC\Delta\operatorname{AIC} method is liberal again, whereas all the other methods have an appropriate actual confidence level.

![Refer to caption](x17.png)
  


Figure 5: Proportion of the 10,000 simulated time series for which a change-point is detected, as a function of p1p\_{1}, where the generating probability of the n=100n=100 first observations is q=(0.25,0.25,0.25,0.25)q=(0.25,0.25,0.25,0.25) and, for the next nn observations, p=(p1,0.5−p1,0.5−p1,p1)p=(p\_{1},0.5-p\_{1},0.5-p\_{1},p\_{1}). The tests used are based i/ on the relative entropy with a threshold defined by the 95%95\% quantile in either the asymptotic two-sample distribution (solid black line) or the ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n} bound (dashed black line); ii/ on the Δ​AIC\Delta\operatorname{AIC} method (solid grey line); iii/ on the t-test with 95%95\% confidence (solid red line); iv/ on the F-test with 95%95\% confidence (dashed red line).

The conclusions of the two examples indicate that change-point tests based on relative entropy are particularly relevant and do not seem to strongly depend on the way the data are generated.

## 5 Application to real data

This section presents an application of the method based on relative entropy to detect change-points. We study two datasets, one of temperature series and another one of volatility series.

### 5.1 Study of a climate dataset

Change-point detection in temperature time series is a well-established topic in the climatology literature, typically conducted on yearly or monthly averaged data. While CUSUM-type procedures are widespread [[28](https://arxiv.org/html/2512.16411v1#bib.bib28)], many existing approaches are designed for offline analysis. Most methods aim at detecting changes in the mean [[61](https://arxiv.org/html/2512.16411v1#bib.bib61)], or in linear or quadratic trends [[27](https://arxiv.org/html/2512.16411v1#bib.bib27), [65](https://arxiv.org/html/2512.16411v1#bib.bib65)]. Less frequently, nonparametric trend changes are considered, using for example wavelet-based techniques [[27](https://arxiv.org/html/2512.16411v1#bib.bib27)]. Depending on the specification, the significance of the change-point is assessed using information criteria such as Δ​AIC\Delta\operatorname{AIC} [[61](https://arxiv.org/html/2512.16411v1#bib.bib61), [65](https://arxiv.org/html/2512.16411v1#bib.bib65)], classical statistical tests [[28](https://arxiv.org/html/2512.16411v1#bib.bib28), [61](https://arxiv.org/html/2512.16411v1#bib.bib61)], or statistical tests in a simulated distribution under a specific noise assumption, for example a white Gaussian noise, a long-range noise [[13](https://arxiv.org/html/2512.16411v1#bib.bib13), [73](https://arxiv.org/html/2512.16411v1#bib.bib73)], or even an alpha-stable noise [[27](https://arxiv.org/html/2512.16411v1#bib.bib27)]. Besides, standard normal homogeneity tests (SNHT) are also widely used in climatology [[4](https://arxiv.org/html/2512.16411v1#bib.bib4), [28](https://arxiv.org/html/2512.16411v1#bib.bib28)]. The main purpose of SNHT is to detect artificial changes in a station’s time series, such as those caused by instrument replacement, by a comparison to the mean value of surrounding stations.

We use a public dataset of temperatures at Embrun (Hautes-Alpes, France), between January 1999 and December 2024, obtained from the website of Météo-France.111<https://donneespubliques.meteofrance.fr/>, station 7591. The dataset is sampled every 3 hours. We average it so that we get the daily and the weekly time series displayed in Figure [6](https://arxiv.org/html/2512.16411v1#S5.F6.fig1 "Figure 6 ‣ 5.1 Study of a climate dataset ‣ 5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). Of course, the seasonality is an important feature of such time series. We thus consider the distribution of daily or weekly temperatures in a one-year window. Then, we compare the distribution of two distinct years using relative entropy, like in the method described in Section [3](https://arxiv.org/html/2512.16411v1#S3 "3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). Constructed from high-resolution temporal data, this distribution-based approach therefore differs from the more commonly used climatological methods, which rely on yearly averages.

![Refer to caption](x18.png)

![Refer to caption](x19.png)

Figure 6: Daily (left) and weekly (right) average temperature at Embrun between January 1999 and December 2024.

Figure [7](https://arxiv.org/html/2512.16411v1#S5.F7.14 "Figure 7 ‣ 5.1 Study of a climate dataset ‣ 5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") shows this relative entropy, along with the bounds corresponding to the quantile at 99%99\% of various distributions: the one- and two-sample asymptotic distribution and Agrawal’s type bounds ℳk,n3\mathcal{M}^{3}\_{k,n} and ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n}. The Δ​AIC\Delta\operatorname{AIC} is very close to the affine transformation of the relative entropy, as expressed in equation ([9](https://arxiv.org/html/2512.16411v1#S3.E9 "In 3.3 Link between relative entropy and the AIC-based method ‣ 3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), so that we also display the threshold 2​(k−1)/n2(k-1)/n as a relevant approximation of the significance bound of the relative entropy. The two important parameters of our change-point detection method are nn and kk. The first one simply corresponds to the number of days or week in a year. Regarding kk, we consider a small value, 4, and a bigger one, 10 for daily and only 6 for weekly data. Indeed, when we simply consider 52 weekly observations, we get several probabilities equal to zero if we work with a fine discretization of 10 categories. We plot two curves showing the relative entropy between the year ending at the x-axis date and either the previous year or a reference year taken as the first year in the dataset.

![Refer to caption](x20.png)

![Refer to caption](x21.png)

![Refer to caption](x22.png)

![Refer to caption](x23.png)

Figure 7: Relative entropy between empirical probabilities estimated on a year of data finishing at the date indicated in abscissa and on either the previous year (red curve) or the first year of data (black curve). The categories are delimited by empirical quantiles on the whole dataset, of probabilities {1/k,2/k,…,(k−1)/k}\{1/k,2/k,...,(k-1)/k\}, where kk is either 4 (left graphs), 6 (bottom right graph), or 10 (top right graph). Dashed horizontal lines are confidence bounds at 99%99\%, obtained using the one- and two-sample asymptotic distributions (thin and thick red), as well as ℳk,n3\mathcal{M}^{3}\_{k,n} and ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n} (thin and thick black). The solid horizontal line corresponds to the value 2​(k−1)/n2(k-1)/n, where nn is the number of observations each year, for the daily (top graphs) or weekly sampling (bottom graphs).

The results shown in Figure [7](https://arxiv.org/html/2512.16411v1#S5.F7.14 "Figure 7 ‣ 5.1 Study of a climate dataset ‣ 5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") reveal several change-points. The greater kk, the finer the discretization of the probability and the higher the resolution of change-point detection. Increasing nn, by considering daily instead of weekly observations, also leads to the detection of more change-points. Although the weekly graphs show an upward trend in relative entropy, a large peak in three of the four graphs also indicates a strong change-point in 2007. It correspond to a particularly hot winter in 2006-2007. This is confirmed by a kernel density representation of the temperatures this year, compared to both the density the year before and the density during the first year of the dataset. See Figure [8](https://arxiv.org/html/2512.16411v1#S5.F8.fig1 "Figure 8 ‣ 5.1 Study of a climate dataset ‣ 5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). We see that the right tails coincide, whereas a large divergence appears in the left tails, in addition to the fluctuations in the bulk of the density. The bandwidth used for each density ranges between 1.3 and 1.7. It was selected so as to maximize a complexity criterion, thereby ensuring a good balance between underfitting and overfitting [[31](https://arxiv.org/html/2512.16411v1#bib.bib31)].

![Refer to caption](x24.png)

![Refer to caption](x25.png)

Figure 8: Kernel density estimates of the daily (left graph) and weekly (right graph) average temperature, with a complexity-based bandwidth. The data used correspond to a year of observations in 1999 (light grey), from July 2005 to June 2006 (dark grey), from July 2006 to June 2007 (black).

### 5.2 Study of a financial dataset

Volatility is a key quantity in financial markets, which leads investment decisions. Starting from a model in which volatility is a fixed parameter, a CUSUM method applied to squares of price returns was first proposed to detect a change-point in volatility [[46](https://arxiv.org/html/2512.16411v1#bib.bib46)]. The heteroscedastic nature of financial time series led to the introduction of stochastic processes of volatility, with serial dependence. However, the traditional CUSUM method too frequently misses the detection of change-points in this stochastic framework [[23](https://arxiv.org/html/2512.16411v1#bib.bib23)], requiring some adjustments [[50](https://arxiv.org/html/2512.16411v1#bib.bib50)]. Besides these online approaches, offline methods have been proposed to detect multiple change-points in the parameters of a stochastic volatility model like GARCH [[51](https://arxiv.org/html/2512.16411v1#bib.bib51), [5](https://arxiv.org/html/2512.16411v1#bib.bib5)]: they consist in finding the partition of time optimizing a least-square-based accuracy criterion along with a penalization, in the spirit of the methods based on information criteria described in Section [3.2](https://arxiv.org/html/2512.16411v1#S3.SS2 "3.2 Another approach using AIC ‣ 3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

While econometric models are usually defined in discrete time under regular sampling, quantitative finance research often turns to continuous-time volatility models, which can be discretized under irregular sampling schemes. Among these models, the rough volatility model, which is based on a geometric fractional Brownian motion (fBm), is very popular [[35](https://arxiv.org/html/2512.16411v1#bib.bib35)]. It makes it possible to depict serial dependence in volatility thanks to a single parameter, the Hurst exponent [[16](https://arxiv.org/html/2512.16411v1#bib.bib16)]. The propensity of this kind of model to forecast future volatility is promising [[30](https://arxiv.org/html/2512.16411v1#bib.bib30), [74](https://arxiv.org/html/2512.16411v1#bib.bib74), [12](https://arxiv.org/html/2512.16411v1#bib.bib12)]. However, some works suggest that the Hurst exponent is not enough to describe the serial dependence of volatility series, and that multifractal extensions [[32](https://arxiv.org/html/2512.16411v1#bib.bib32), [71](https://arxiv.org/html/2512.16411v1#bib.bib71)] or jumps [[1](https://arxiv.org/html/2512.16411v1#bib.bib1), [34](https://arxiv.org/html/2512.16411v1#bib.bib34)] are to be considered. The detection of change-points in volatility series is therefore crucial for identifying the time intervals in which the fBm framework remains valid. The solutions proposed in the literature consist in detecting jumps [[11](https://arxiv.org/html/2512.16411v1#bib.bib11)] or a change-point in the Hurst exponent using CUSUM [[10](https://arxiv.org/html/2512.16411v1#bib.bib10)] or using the local absolute variation [[75](https://arxiv.org/html/2512.16411v1#bib.bib75)].

We propose here to apply the change-point tests described in Section [3](https://arxiv.org/html/2512.16411v1#S3 "3 Change-point detection ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). The data are five daily time series of realized volatility computed with a five-minute discretization of prices of stock indices, imported from the formerly available Oxford-Man Institute of Quantitative Finance Realized Library: the AEX index, the CAC 40 index, the Nikkei 225 index (N225), the Oslo Exchange All-share index (OSEAX), and the S&P 500 index (SPX). The series starts on January 2000, except N225, which starts in February 2000 and OSEAX in September 2001. The end date of our sample is on the 12th April 2021. We import as well from Bloomberg the VIX, which is obtained from option prices on the SPX, in the same time period 2000-2021. Figure [9](https://arxiv.org/html/2512.16411v1#S5.F9.fig1 "Figure 9 ‣ 5.2 Study of a financial dataset ‣ 5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") shows the six time series.

![Refer to caption](x26.png)

![Refer to caption](x27.png)

![Refer to caption](x28.png)

![Refer to caption](x29.png)

![Refer to caption](x30.png)

![Refer to caption](x31.png)

Figure 9: Daily time series of realized volatility for AEX (top left graph), CAC 40 (top right), N225 (middle left), OSEAX (middle right), SPX (bottom left), followed by the VIX (bottom right).

For forecasting applications, we’re interested in the dependence structure of a volatility series. We therefore discretize each increment of the volatility process, depending on whether it is positive or negative, resulting in an indicator equal to 1 or 0 [[15](https://arxiv.org/html/2512.16411v1#bib.bib15), [16](https://arxiv.org/html/2512.16411v1#bib.bib16)]. We then consider a vector of three consecutive indicators, which has thus eight possible categories. We consider a window size nn, corresponding to one year of data, for estimating the categorical probabilities. We will also consider a smaller nn, with a three-month period. In the latter case, in order not to have zero probabilities, we reduce the number of categories to six, merging the two categories corresponding to a trend, that is (0,0,0)′(0,0,0)^{\prime} and (1,1,1)′(1,1,1)^{\prime}, and merging those defined by a strict alternation of 0s and 1s, that is (0,1,0)′(0,1,0)^{\prime} and (1,0,1)′(1,0,1)^{\prime}.

Depending on the series and the threshold selected, the relative entropy between two probabilities built with one year of data indicates a few change-points, as one can see in Figure [10](https://arxiv.org/html/2512.16411v1#S5.F10.10 "Figure 10 ‣ 5.2 Study of a financial dataset ‣ 5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). A clear change-point appears during the global financial crisis (around 2008-2009) for the VIX. Change-points are less obvious for realized volatilities in this period, even though the relative entropy of two consecutive years seems to be significant for SPX and N225, but not if the reference year is the first year. Other important change-points include the interval 2014-2015 for OSEAX. This can be explained by the Norwegian economy’s dependence on oil prices: the price of Brent crude fell by 50%50\% in less than a year starting in June 2014, which reshaped both the index’s sectoral composition and the serial dependence pattern of its volatility. The peaks in relative entropy for the N225 starting in March 2011 correspond to the major event of Fukushima accident. Interestingly, this appears as a single isolated peak in the realized volatility series, whereas the change-point indicator remains elevated for several months, more realistically reflecting the prolonged uncertainty following the event.

![Refer to caption](x32.png)

![Refer to caption](x33.png)

![Refer to caption](x34.png)

![Refer to caption](x35.png)

![Refer to caption](x36.png)

![Refer to caption](x37.png)

Figure 10: For each daily series of realized volatility for AEX (top left graph), CAC 40 (top right), N225 (middle left), OSEAX (middle right), SPX (bottom left), followed by the VIX (bottom right), relative entropy between empirical discrete probabilities estimated on a year of data finishing at the date indicated in abscissa and on either the previous year (red curve) or the first year of data (black curve). Dashed horizontal lines are confidence bounds at 99%99\%, obtained using the one- and two-sample asymptotic distributions (thin and thick red), as well as ℳk,n3\mathcal{M}^{3}\_{k,n} and ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n} (thin and thick black). The solid horizontal line corresponds to the value 2​(k−1)/n2(k-1)/n, where nn is the number of observations each year.

Figure [11](https://arxiv.org/html/2512.16411v1#S5.F11.10 "Figure 11 ‣ 5.2 Study of a financial dataset ‣ 5 Application to real data ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") displays the results for three-month windows for the realized volatility of SPX and VIX. Relative entropy is much more fluctuating. For the two series, a change-point is detected during the global financial crisis. The COVID-19 crisis (around 2020) also generates a change-point, whereas it was not obvious with one-year windows.

![Refer to caption](x38.png)

![Refer to caption](x39.png)

Figure 11: For the daily series of the realized volatility of SPX (left graph) and the series of VIX (right graph) relative entropy between empirical discrete probabilities estimated on three months of data finishing at the date indicated in abscissa and on either the previous year (red curve) or the first year of data (black curve). Dashed horizontal lines are confidence bounds at 99%99\%, obtained using the one- and two-sample asymptotic distributions (thin and thick red), as well as ℳk,n3\mathcal{M}^{3}\_{k,n} and ℳ~k,n,n3,⋆\widetilde{\mathcal{M}}^{3,\star}\_{k,n,n} (thin and thick black). The solid horizontal line corresponds to the value 2​(k−1)/n2(k-1)/n, where nn is the number of observations in the three-month window.

## 6 Conclusion

In this paper, we have been interested in the distribution of relative entropy, in the one- and two-sample cases. We have thus presented the asymptotic distribution along with Berry-Esseen bounds. For finite samples, we also have provided concentration bounds. All these approximations of the true distribution are useful for building change-point statistical tests. We have thus described a method based on relative entropy and compared it to more classical approaches thanks to extensive simulations. It highlights the limitations of moments-based tests in some situations, where modifications in the probability distribution do not make the first moments deviate, thus making the test based on relative entropy more general. Two applications to real data, namely climate and finance datasets, emphasize the practical relevance of this method. It makes the climate change visible and unveils modifications in the serial dependence of volatility that we can relate to macroeconomic events. Our theoretical findings rely on recent advances, including results on the multivariate Berry-Esseen inequality and on reverse Pinsker’s inequality. These tools do not yet exhibit the same level of theoretical maturity as classical results such as the univariate Berry-Esseen inequality or Pinsker’s inequality. Further advances on these two inequalities, for example regarding a non-uniform version of multivariate Berry-Esseen bounds, would directly strengthen our theoretical bounds and enhance the accuracy of our change-point application.

## References

* [1]

  E. Abi Jaber and N. De Carvalho.
  Reconciling rough volatility with jumps.
  SIAM journal on financial mathematics, 15(3):785–823, 2024.
* [2]

  R. Agrawal.
  Finite-sample concentration of the multinomial in relative entropy.
  IEEE transactions on information theory, 66(10):6297–6302,
  2020.
* [3]

  H. Akaike.
  Information theory and an extension of the maximum likelihood
  principle.
  In Selected papers of Hirotugu Akaike, pages 199–213.
  Springer, 1998.
* [4]

  H. Alexandersson.
  A homogeneity test applied to precipitation data.
  Journal of climatology, 6(6):661–675, 1986.
* [5]

  E. Andreou and E. Ghysels.
  Detecting multiple breaks in financial market volatility dynamics.
  Journal of applied econometrics, 17(5):579–600, 2002.
* [6]

  A. Barbiero and A. Hitaj.
  A new discrete exponential distribution: properties and applications.
  Journal of statistical theory and practice, 19(3):39, 2025.
* [7]

  G.P. Basharin.
  On a statistical estimate for the entropy of a sequence of
  independent random variables.
  Theory of probability & its applications, 4(3):333–336, 1959.
* [8]

  F. Bavaud.
  Information theory, relative entropy and statistics.
  In Formal theories of information: From Shannon to semantic
  information theory and general concepts of information, pages 54–78.
  Springer, 2009.
* [9]

  V. Bentkus and F. Götze.
  Uniform rates of convergence in the CLT for quadratic forms in
  multidimensional spaces.
  Probability theory and related fields, 109:367–416, 1997.
* [10]

  M. Bibinger.
  Cusum tests for changes in the Hurst exponent and volatility of
  fractional Brownian motion.
  Statistics & probability letters, 161:108725, 2020.
* [11]

  M. Bibinger, M. Jirak, and M. Vetter.
  Nonparametric change-point analysis of volatility.
  Annals of statistics, 45(4):1542–1578, 2017.
* [12]

  M. Bibinger, J. Yu, and C. Zhang.
  Modeling and forecasting realized volatility with multivariate
  fractional Brownian motion.
  Preprint, 2025.
* [13]

  R. Blender and K. Fraedrich.
  Long time memory in global warming simulations.
  Geophysical research letters, 30(14):1769, 2003.
* [14]

  J. Bretagnolle and C. Huber.
  Estimation des densités: risque minimax.
  Zeitschrift für Wahrscheinlichkeitstheorie und verwandte
  Gebiete, 47(2):119–137, 1979.
* [15]

  X. Brouty and M. Garcin.
  A statistical test of market efficiency based on information theory.
  Quantitative finance, 23(6):1003–1018, 2023.
* [16]

  X. Brouty and M. Garcin.
  Fractal properties, information theory, and market efficiency.
  Chaos, solitons & fractals, 180:114543, 2024.
* [17]

  C.L. Canonne.
  A short note on an inequality between KL and TV.
  Preprint, 2022.
* [18]

  J.E. Cavanaugh.
  Unifying the derivations for the Akaike and corrected Akaike
  information criteria.
  Statistics & probability letters, 33(2):201–208, 1997.
* [19]

  J.E. Cavanaugh and A.A. Neath.
  The Akaike information criterion: Background, derivation,
  properties, application, interpretation, and refinements.
  Wiley interdisciplinary reviews: computational statistics,
  11(3):e1460, 2019.
* [20]

  R. Chattamvelli and R. Shanmugam.
  Geometric distribution.
  In Discrete distributions in engineering and the applied
  sciences, pages 65–82. Springer, 2020.
* [21]

  T.M. Cover and J.A. Thomas.
  Elements of information theory.
  John Wiley & sons, second edition, 2006.
* [22]

  I. Csiszár.
  The method of types.
  IEEE transactions on information theory, 44(6):2505–2523,
  2002.
* [23]

  M. De Pooter and D. Van Dijk.
  Testing for changes in volatility in heteroskedastic time series – a
  further examination.
  Technical report, 2004.
* [24]

  S. Eguchi and J. Copas.
  Interpreting Kullback-Leibler divergence with the
  Neyman-Pearson lemma.
  Journal of multivariate analysis, 97(9):2034–2040, 2006.
* [25]

  X. Fang, S.-H. Liu, and Q.-M. Shao.
  Cramér-type moderate deviation for quadratic forms with a fast
  rate.
  Bernoulli, 29(3):2466–2491, 2023.
* [26]

  T. Flynn and S. Yoo.
  Change detection with the kernel cumulative sum algorithm.
  In 2019 IEEE 58th conference on decision and control (CDC),
  pages 6092–6099. IEEE, 2019.
* [27]

  C. Franzke.
  Nonlinear trends, long-range dependence, and climate noise properties
  of surface temperature.
  Journal of climate, 25(12):4172–4183, 2012.
* [28]

  C. Gallagher, R. Lund, and M. Robbins.
  Changepoint detection in climate time series with long-term trends.
  Journal of climate, 26(14):4994–5006, 2013.
* [29]

  Z. Gao, X. Xiao, Y.-P. Fang, J. Rao, and H. Mo.
  A selective review on information criteria in multiple change point
  detection.
  Entropy, 26(1):50, 2024.
* [30]

  M. Garcin.
  Forecasting with fractional Brownian motion: a financial
  perspective.
  Quantitative finance, 22(8):1495–1512, 2022.
* [31]

  M. Garcin.
  Complexity measure, kernel density estimation, bandwidth selection,
  and the efficient market hypothesis.
  In A. Sinha, editor, Select topics of econophysics. De Gruyter,
  2024.
* [32]

  M. Garcin and M. Grasselli.
  Long versus short time scales: the rough dilemma and beyond.
  Decisions in economics and finance, 45(1):257–278, 2022.
* [33]

  M. Garcin, J. Klein, and S. Laaribi.
  Estimation of time-varying kernel densities and chronology of the
  impact of COVID-19 on financial markets.
  Journal of applied statistics, 51(11):2157–2177, 2024.
* [34]

  M. Garcin, K. Sawaya, and T. Valade.
  Prediction of linear fractional stable motions using codifference,
  with application to non-Gaussian rough volatility.
  Preprint, 2025.
* [35]

  J. Gatheral, T. Jaisson, and M. Rosenbaum.
  Volatility is rough.
  Quantitative finance, 18(6):933–949, 2018.
* [36]

  A.L. Gibbs and F.E. Su.
  On choosing and bounding probability metrics.
  International statistical review, 70(3):419–435, 2002.
* [37]

  V. Glinskiy, A. Logachov, O. Logachova, H. Rojas, L. Serga, and A. Yambartsev.
  Asymptotic properties of a statistical estimator of the Jeffreys
  divergence: the case of discrete distributions.
  Mathematics, 12(21):3319, 2024.
* [38]

  F. Götze and A.N. Tikhomirov.
  Asymptotic expansions in non-central limit theorems for quadratic
  forms.
  Journal of theoretical probability, 18(4):757–811, 2005.
* [39]

  F. Götze and V.V. Ulyanov.
  Asymptotic distribution of χ2\chi^{2}-type statistics.
  Preprint, 2003.
* [40]

  F. Götze and A.Y. Zaitsev.
  Uniform rates of approximation by short asymptotic expansions in the
  CLT for quadratic forms.
  Journal of mathematical sciences, 176(2):162–189, 2011.
* [41]

  F. Götze and A.Y. Zaitsev.
  Explicit rates of approximation in the CLT for quadratic forms.
  Annals of probability, 42(1):354–397, 2014.
* [42]

  A. Hamadouche, A. Kouadri, and A. Bakdi.
  A modified Kullback divergence for direct fault detection in large
  scale systems.
  Journal of process control, 59:28–36, 2017.
* [43]

  A. Harvey and V. Oryshchenko.
  Kernel density estimation for time series data.
  International journal of forecasting, 28(1):3–14, 2012.
* [44]

  K. Haynes, P. Fearnhead, and I.A. Eckley.
  A computationally efficient nonparametric approach for changepoint
  detection.
  Statistics and computing, 27(5):1293–1305, 2017.
* [45]

  C.M. Hurvich and C.-L. Tsai.
  Regression and time series model selection in small samples.
  Biometrika, 76(2):297–307, 1989.
* [46]

  C. Inclan and G.C. Tiao.
  Use of cumulative sums of squares for retrospective detection of
  changes of variance.
  Journal of the American statistical association,
  89(427):913–923, 1994.
* [47]

  B. James, K.L. James, and D. Siegmund.
  Tests for a change-point.
  Biometrika, 74(1):71–83, 1987.
* [48]

  R.H. Jones and I. Dey.
  Determining one or more change points.
  Chemistry and physics of lipids, 76(1):1–6, 1995.
* [49]

  M. Kelbert.
  Survey of distances between the most popular distributions.
  Analytics, 2(1):225–245, 2023.
* [50]

  P. Kokoszka and R. Leipus.
  Change-point estimation in ARCH models.
  Bernoulli, 6(6):513–539, 2000.
* [51]

  M. Lavielle and E. Moulines.
  Least-squares estimation of an unknown number of shifts in a time
  series.
  Journal of time series analysis, 21(1):33–59, 2000.
* [52]

  S. Liu, M. Yamada, N. Collier, and M. Sugiyama.
  Change-point detection in time-series data by relative density-ratio
  estimation.
  Neural networks, 43:72–83, 2013.
* [53]

  Z.A. Lomnicki and S.K. Zaremba.
  The asymptotic distributions of estimators of the amount of
  transmitted information.
  Information and control, 2(3):260–284, 1959.
* [54]

  J. Mardia, J. Jiao, E. Tánczos, R.D. Nowak, and T. Weissman.
  Concentration inequalities for the empirical distribution of discrete
  distributions: beyond the method of types.
  Information and inference: a journal of the IMA,
  9(4):813–850, 2020.
* [55]

  M. Marinescu and C. Balcau.
  On the use of mutual information for testing independence.
  Preprint, 2025.
* [56]

  E.S. Page.
  Continuous inspection schemes.
  Biometrika, 41(1/2):100–115, 1954.
* [57]

  I. Pinelis.
  On the nonuniform Berry–Esseen bound.
  In Inequalities and extremal problems in probability and
  statistics, pages 103–138. Elsevier, 2017.
* [58]

  I. Pinelis and R. Molzon.
  Optimal-order bounds on the rate of convergence to normality in the
  multivariate delta method.
  Electronic journal of statistics, 10:1001–1063, 2016.
* [59]

  J. Plasse and N.M. Adams.
  Multiple changepoint detection in categorical data streams.
  Statistics and computing, 29(5):1109–1125, 2019.
* [60]

  M. Raič.
  A multivariate Berry–Esseen theorem with explicit constants.
  Bernoulli, 25(4A):2824–2853, 2019.
* [61]

  J. Reeves, J. Chen, X.L. Wang, R. Lund, and Q.Q. Lu.
  A review and comparison of changepoint detection techniques for
  climate data.
  Journal of applied meteorology and climatology, 46(6):900–915,
  2007.
* [62]

  I. Sason and S. Verdú.
  Upper bounds on the relative entropy and Rényi divergence as a
  function of total variation distance for finite alphabets.
  In 2015 IEEE information theory workshop-fall, pages
  214–218. IEEE, 2015.
* [63]

  I. Sason and S. Verdú.
  ff-divergence inequalities.
  IEEE transactions on information theory, 62(11):5973–6006,
  2016.
* [64]

  Q.-M. Shao and Z.-S. Zhang.
  Berry–Esseen bounds for multivariate nonlinear statistics with
  applications to M-estimators and stochastic gradient descent algorithms.
  Bernoulli, 28(3):1548–1576, 2022.
* [65]

  X. Shi, C. Beaulieu, R. Killick, and R. Lund.
  Changepoint detection: An analysis of the Central England
  temperature series.
  Journal of climate, 35(19):6329–6342, 2022.
* [66]

  A. Shternshis, P. Mazzarisi, and S. Marmi.
  Measuring market efficiency: The Shannon entropy of
  high-frequency financial time series.
  Chaos, solitons & fractals, 162:112403, 2022.
* [67]

  C. Truong, L. Oudre, and N. Vayatis.
  Selective review of offline change point detection methods.
  Signal processing, 167:107299, 2020.
* [68]

  A.B. Tsybakov.
  Introduction to nonparametric estimation.
  Springer science & business media, 2008.
* [69]

  P. Wang and W. Ning.
  Nonparametric CUSUM change-point detection procedures based on
  modified empirical likelihood.
  Computational statistics, 40:4991–5021, 2025.
* [70]

  S.S. Wilks.
  The large-sample distribution of the likelihood ratio for testing
  composite hypotheses.
  Annals of mathematical statistics, 9(1):60–62, 1938.
* [71]

  P. Wu, J.-F. Muzy, and E. Bacry.
  From rough to multifractal volatility: The log S-fBm model.
  Physica A: statistical mechanics and its applications,
  604:127919, 2022.
* [72]

  Y. Yu, O.H. Madrid Padilla, D. Wang, and A. Rinaldo.
  A note on online change point detection.
  Sequential analysis, 42(4):438–471, 2023.
* [73]

  N. Yuan, M. Ding, Y. Huang, Z. Fu, E. Xoplaki, and J. Luterbacher.
  On the long-term climate memory in the surface air temperature
  records over Antarctica: A nonnegligible factor for trend evaluation.
  Journal of climate, 28(15):5922–5934, 2015.
* [74]

  Q. Zhu, X. Diao, and C. Wu.
  Volatility forecast with the regularity modifications.
  Finance research letters, 58:104008, 2023.
* [75]

  Q. Zhu, X. Diao, and C Wu.
  A test for change points under the roughness of stochastic
  volatility: the case of the VIX index.
  Applied economics letters, 32(7):951–959, 2025.
* [76]

  S. Zhu, B. Chen, Z. Chen, and P. Yang.
  Asymptotically optimal one-and two-sample testing with kernels.
  IEEE transactions on information theory, 67(4):2074–2092,
  2021.
* [77]

  C. Zou, G. Yin, L. Feng, and Z. Wang.
  Nonparametric maximum likelihood approach to multiple change-point
  problems.
  Annals of statistics, 42(3):970–1002, 2014.
* [78]

  A.M. Zubkov.
  Limit distributions for a statistical estimate of the entropy.
  Theory of probability & its applications, 18(3):611–618,
  1974.

## Appendix A A useful lemma for proving Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")

###### Lemma 1.

The real solutions of the cubic equation a​x3+x2−d=0ax^{3}+x^{2}-d=0 are

|  |  |  |  |
| --- | --- | --- | --- |
|  | 13​a​[2​cos⁡(13​arccos⁡(27​a2​d−22)−2​r​π3)−1],\frac{1}{3a}\left[2\cos\left(\frac{1}{3}\arccos\left(\frac{27a^{2}d-2}{2}\right)-\frac{2r\pi}{3}\right)-1\right], |  | (10) |

with r∈{0,1,2}r\in\{0,1,2\}, when d≤4/27​a2d\leq 4/27a^{2}, and

|  |  |  |
| --- | --- | --- |
|  | −127​a3+d2​a+−4​d+27​d2​a2108​a43+−127​a3+d2​a−−4​d+27​d2​a2108​a43−13​a\sqrt[3]{-\frac{1}{27a^{3}}+\frac{d}{2a}+\sqrt{\frac{-4d+27d^{2}a^{2}}{108a^{4}}}}+\sqrt[3]{-\frac{1}{27a^{3}}+\frac{d}{2a}-\sqrt{\frac{-4d+27d^{2}a^{2}}{108a^{4}}}}-\frac{1}{3a} |  |

when d>4/27​a2d>4/27a^{2}. Moreover, when d>0d>0 and a→0a\rightarrow 0, we get three real roots. One diverges to +∞+\infty if a<0a<0 and to −∞-\infty if a>0a>0. The other two behave like:

|  |  |  |
| --- | --- | --- |
|  | {x0=d−d2​a+𝒪​(a2)x1=−d−d2​a+𝒪​(a2).\left\{\begin{array}[]{ccl}x\_{0}&=&\sqrt{d}-\frac{d}{2}a+\mathcal{O}(a^{2})\\ x\_{1}&=&-\sqrt{d}-\frac{d}{2}a+\mathcal{O}(a^{2}).\end{array}\right. |  |

###### Proof.

Defining yy by x+1/3​ax+1/3a, we get the following equation in yy: y3+p​y+q=0y^{3}+py+q=0, where p=−1/3​a2p=-1/3a^{2} and q=(2/27​a3)−(d/a)q=(2/27a^{3})-(d/a). The discriminant −(p/3)3−(q/2)2-(p/3)^{3}-(q/2)^{2} is equal to (4​d−27​d2​a2)/108​a4(4d-27d^{2}a^{2})/108a^{4}. There are two cases, depending on the value of dd. First, if d≤4/27​a2d\leq 4/27a^{2}, the discriminant is non-negative and there are three real roots (given below for the equation in xx), among which one is double when the discriminant is zero, after Cardano’s formula,

|  |  |  |
| --- | --- | --- |
|  | 13​a​[2​cos⁡(13​arccos⁡(27​a2​d−22)−2​r​π3)−1],\frac{1}{3a}\left[2\cos\left(\frac{1}{3}\arccos\left(\frac{27a^{2}d-2}{2}\right)-\frac{2r\pi}{3}\right)-1\right], |  |

where r∈{0,1,2}r\in\{0,1,2\}. If d>4/27​a2d>4/27a^{2}, the discriminant is non-negative and there is only one real root for the equation in xx,

|  |  |  |
| --- | --- | --- |
|  | −q2+(q2)2+(p3)33+−q2−(q2)2+(p3)33−13​a,\sqrt[3]{-\frac{q}{2}+\sqrt{\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3}}}+\sqrt[3]{-\frac{q}{2}-\sqrt{\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3}}}-\frac{1}{3a}, |  |

that is, when replacing pp and qq by their expression in aa and dd,

|  |  |  |
| --- | --- | --- |
|  | −127​a3+d2​a+−4​d+27​d2​a2108​a43+−127​a3+d2​a−−4​d+27​d2​a2108​a43−13​a.\sqrt[3]{-\frac{1}{27a^{3}}+\frac{d}{2a}+\sqrt{\frac{-4d+27d^{2}a^{2}}{108a^{4}}}}+\sqrt[3]{-\frac{1}{27a^{3}}+\frac{d}{2a}-\sqrt{\frac{-4d+27d^{2}a^{2}}{108a^{4}}}}-\frac{1}{3a}. |  |

When a→0a\rightarrow 0, the leading term in the discriminant is d/27​a4d/27a^{4}, which is positive if d>0d>0. Therefore, the solutions are like in equation ([10](https://arxiv.org/html/2512.16411v1#A1.E10 "In Lemma 1. ‣ Appendix A A useful lemma for proving Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")). We easily get the limit

|  |  |  |
| --- | --- | --- |
|  | lima→0​ 2​cos⁡(13​arccos⁡(27​a2​d−22)−2​r​π3)−1={0if ​r∈{0,1}−3if ​r=2.\underset{a\rightarrow 0}{\lim}\ 2\cos\left(\frac{1}{3}\arccos\left(\frac{27a^{2}d-2}{2}\right)-\frac{2r\pi}{3}\right)-1=\left\{\begin{array}[]{ll}0&\text{if }r\in\{0,1\}\\ -3&\text{if }r=2.\end{array}\right. |  |

In this asymptotic case, the root with r=2r=2 will diverge to +∞+\infty if a<0a<0 and to −∞-\infty if a>0a>0. For the two other roots, we apply a perturbative expansion. We start with the simplified problem corresponding to a=0a=0, that is x2−d=0x^{2}-d=0. The two solutions are d\sqrt{d} and −d-\sqrt{d}. Next, we consider the perturbation of the two roots:

|  |  |  |
| --- | --- | --- |
|  | {x0=d+β0​a+𝒪​(a2)x1=−d+β1​a+𝒪​(a2).\left\{\begin{array}[]{ccl}x\_{0}&=&\sqrt{d}+\beta\_{0}a+\mathcal{O}(a^{2})\\ x\_{1}&=&-\sqrt{d}+\beta\_{1}a+\mathcal{O}(a^{2}).\end{array}\right. |  |

Plugging x0x\_{0} in the cubic equation, we get

|  |  |  |
| --- | --- | --- |
|  | a​d3/2+2​d1/2​β0​a=𝒪​(a2),ad^{3/2}+2d^{1/2}\beta\_{0}a=\mathcal{O}(a^{2}), |  |

so that β0=−d/2\beta\_{0}=-d/2. Using the same approach for x1x\_{1}, we find as well that β1=−d/2\beta\_{1}=-d/2. We therefore get the result displayed in the lemma.
∎

## Appendix B Proof of Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")

The proof of Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") uses Lemma [1](https://arxiv.org/html/2512.16411v1#Thmlem1 "Lemma 1. ‣ Appendix A A useful lemma for proving Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), which is provided in Appendix [A](https://arxiv.org/html/2512.16411v1#A1 "Appendix A A useful lemma for proving Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

###### Proof.

The observations XjX\_{j} being independent of each other, the random vector n​p^nn\widehat{p}\_{n} is a multinomial variable of parameter pp. The multivariate central limit theorem thus gives

|  |  |  |
| --- | --- | --- |
|  | n​(p^n−p)​⟶d​𝒩​(0,diag⁡(p)−p​pt),\sqrt{n}\left(\widehat{p}\_{n}-p\right)\overset{\text{d}}{\longrightarrow}\mathcal{N}\left(0,\operatorname{diag}(p)-pp^{t}\right), |  |

where 𝒩​(μ,σ2)\mathcal{N}(\mu,\sigma^{2}) is the Gaussian distribution of mean μ\mu and variance σ2\sigma^{2}. As a consequence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​(p^n,1−p1p1⋮p^n,k−pkpk)​⟶d​𝒩​(0,Γk),\sqrt{n}\left(\begin{array}[]{c}\frac{\widehat{p}\_{n,1}-p\_{1}}{\sqrt{p\_{1}}}\\ \vdots\\ \frac{\widehat{p}\_{n,k}-p\_{k}}{\sqrt{p\_{k}}}\end{array}\right)\overset{\text{d}}{\longrightarrow}\mathcal{N}\left(0,\Gamma\_{k}\right), |  | (11) |

where Γk=Ik−u​ut\Gamma\_{k}=I\_{k}-uu^{t}, with IkI\_{k} the identity matrix and u=(p1,…,pk)tu=(\sqrt{p\_{1}},...,\sqrt{p\_{k}})^{t}. We now need the eigenspaces of Γk\Gamma\_{k}. Since Γk\Gamma\_{k} is real and symmetric, its eigenvectors form an orthogonal basis. First, uu is an eigenvector associated with the eigenvalue 0:

|  |  |  |
| --- | --- | --- |
|  | Γk​u=u−u​ut​u=(1−ut​u)​u=(1−∑i=1kpi)​u=0.\Gamma\_{k}u=u-uu^{t}u=(1-u^{t}u)u=\left(1-\sum\_{i=1}^{k}p\_{i}\right)u=0. |  |

Let’s consider any vector vv orthogonal to uu, that is ut​v=0u^{t}v=0. The space of all possible vectors vv is thus of dimension k−1k-1. Then, from the orthogonality condition, we easily get Γk​v=v\Gamma\_{k}v=v. Therefore, the eigenspace of Γk\Gamma\_{k} associated with the eigenvalue 1 is of dimension k−1k-1, which is also the rank of the matrix Γk\Gamma\_{k}. The nonzero eigenvalues of Γk\Gamma\_{k} being all equal to 1, we have the reduced spectral decomposition Γk=V​Ik−1​Vt=V​Vt\Gamma\_{k}=VI\_{k-1}V^{t}=VV^{t}, where V∈ℝk×(k−1)V\in\mathbb{R}^{k\times(k-1)} is a matrix whose columns are orthonormal unit-eigenvalue eigenvectors, so that Vt​V=Ik−1V^{t}V=I\_{k-1}.

Let us now focus on the empirical relative entropy, f​(p^n)f(\widehat{p}\_{n}), written as a function of p^n\widehat{p}\_{n}, where f​(q)=DKL​(q∥p)f(q)=D\_{\text{KL}}\left(q\|p\right). The function ff can be decomposed in a sum of kk univariate functions: f​(q)=∑i=1kfi​(qi)f(q)=\sum\_{i=1}^{k}f\_{i}(q\_{i}), where fi​(qi)=qi​log⁡(qi/pi)f\_{i}(q\_{i})=q\_{i}\log(q\_{i}/p\_{i}), fi′​(qi)=1+log⁡(qi/pi)f\_{i}^{\prime}(q\_{i})=1+\log(q\_{i}/p\_{i}), and fi(j)​(qi)=(−1)j​(j−2)!​qi1−jf\_{i}^{(j)}(q\_{i})=(-1)^{j}(j-2)!q\_{i}^{1-j} for j≥2j\geq 2. This decomposition eases the second-order Taylor expansion of ff, which can be seen as the sum of kk distinct expansions, and where we also note that fi​(pi)=0f\_{i}(p\_{i})=0 and fi′​(pi)=1f\_{i}^{\prime}(p\_{i})=1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(p^n)=12​∑i=1k(p^n,i−pi)2pi+∑i=1kRi​(p^n,i),f(\widehat{p}\_{n})=\frac{1}{2}\sum\_{i=1}^{k}\frac{(\widehat{p}\_{n,i}-p\_{i})^{2}}{p\_{i}}+\sum\_{i=1}^{k}R\_{i}(\widehat{p}\_{n,i}), |  | (12) |

with Ri​(p^n,i)=fi(3)​(ξn,i)​(p^n,i−pi)3/6=(pi−p^n,i)3/6​ξn,i2R\_{i}(\widehat{p}\_{n,i})=f\_{i}^{(3)}(\xi\_{n,i})(\widehat{p}\_{n,i}-p\_{i})^{3}/6=(p\_{i}-\widehat{p}\_{n,i})^{3}/6\xi\_{n,i}^{2}, where ξn,i\xi\_{n,i} is in the interval delimited by p^n,i\widehat{p}\_{n,i} and pip\_{i}.

From the decomposition Γk=V​Vt\Gamma\_{k}=VV^{t}, we can write the limit appearing in formula ([11](https://arxiv.org/html/2512.16411v1#A2.E11 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) as V​GVG, where G∈ℝk−1G\in\mathbb{R}^{k-1} is a standard Gaussian vector. Then,

|  |  |  |
| --- | --- | --- |
|  | ∑i=1kn​(p^n,i−pi)2pi​⟶d​Gt​Vt​V​G=Gt​G,\sum\_{i=1}^{k}\frac{n(\widehat{p}\_{n,i}-p\_{i})^{2}}{p\_{i}}\overset{\text{d}}{\longrightarrow}G^{t}V^{t}VG=G^{t}G, |  |

using the orthonormal property of VV. This limit follows a chi-square distribution χk−12\chi^{2}\_{k-1}. Moreover, since p^n,i​⟶ℙ​pi\widehat{p}\_{n,i}\overset{\mathbb{P}}{\longrightarrow}p\_{i}, we have ξn,i​⟶ℙ​pi\xi\_{n,i}\overset{\mathbb{P}}{\longrightarrow}p\_{i} and, by the continuous mapping theorem, (pi−p^n,i)/6​ξn,i2​⟶ℙ​0(p\_{i}-\widehat{p}\_{n,i})/6\xi\_{n,i}^{2}\overset{\mathbb{P}}{\longrightarrow}0, because pi≠0p\_{i}\neq 0. Therefore, n​Ri​(p^n,i)=n​(pi−p^n,i)2​(pi−p^n,i)/6​ξn,i2​⟶ℙ​0nR\_{i}(\widehat{p}\_{n,i})=n(p\_{i}-\widehat{p}\_{n,i})^{2}(p\_{i}-\widehat{p}\_{n,i})/6\xi\_{n,i}^{2}\overset{\mathbb{P}}{\longrightarrow}0, since it is a product of a sequence converging in distribution with a sequence converging in probability to zero. Finally, starting from equation ([12](https://arxiv.org/html/2512.16411v1#A2.E12 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), we see that 2​n​f​(p^n)2nf(\widehat{p}\_{n}) is a sum of a sequence converging in distribution to χk−12\chi^{2}\_{k-1} with kk sequences converging in probability to zero. Slutsky’s theorem thus leads to equation ([2](https://arxiv.org/html/2512.16411v1#S2.E2 "In Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")).

We now have to prove the second part of the theorem. We’re going to use a multivariate extension of Berry-Esseen theorem [[60](https://arxiv.org/html/2512.16411v1#bib.bib60)] and apply it first to the quadratic part of ff: the rest, namely the RiR\_{i} functions, will be considered in a second stage. We define Y1Y\_{1}, …, YnY\_{n}, iid vectors of ℝk\mathbb{R}^{k}, by

|  |  |  |
| --- | --- | --- |
|  | Yj=(𝟙Xj∈Ω1−p1n​p1,…,𝟙Xj∈Ωk−pkn​pk)t.Y\_{j}=\left(\frac{\mathds{1}\_{X\_{j}\in\Omega\_{1}}-p\_{1}}{\sqrt{np\_{1}}},...,\frac{\mathds{1}\_{X\_{j}\in\Omega\_{k}}-p\_{k}}{\sqrt{np\_{k}}}\right)^{t}. |  |

It is easy to see that 𝔼​(Yj)=0\mathbb{E}(Y\_{j})=0. We will need the expression of the third moment of the Euclidean norm of YjY\_{j}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(Yjt​Yj)3/2]=𝔼​[(∑i=1k(𝟙Xj∈Ωi−pi)2n​pi)3/2]=∑u=1kℙ​(Xj∈Ωu)​((1−pu)2n​pu+∑i≠upi2n​pi)3/2=1n3/2​∑u=1kpu​((1−pu)2pu+1−pu)3/2=1n3/2​∑u=1k(1−pu)3/2pu1/2.\begin{array}[]{ccl}\mathbb{E}\left[\left(Y\_{j}^{t}Y\_{j}\right)^{3/2}\right]&=&\mathbb{E}\left[\left(\sum\_{i=1}^{k}\frac{(\mathds{1}\_{X\_{j}\in\Omega\_{i}}-p\_{i})^{2}}{np\_{i}}\right)^{3/2}\right]\\ &=&\sum\_{u=1}^{k}\mathbb{P}(X\_{j}\in\Omega\_{u})\left(\frac{(1-p\_{u})^{2}}{np\_{u}}+\sum\_{i\neq u}\frac{p\_{i}^{2}}{np\_{i}}\right)^{3/2}\\ &=&\frac{1}{n^{3/2}}\sum\_{u=1}^{k}p\_{u}\left(\frac{(1-p\_{u})^{2}}{p\_{u}}+1-p\_{u}\right)^{3/2}\\ &=&\frac{1}{n^{3/2}}\sum\_{u=1}^{k}\frac{(1-p\_{u})^{3/2}}{p\_{u}^{1/2}}.\end{array} |  | (13) |

We also define W=∑j=1nYjW=\sum\_{j=1}^{n}Y\_{j}, whose ii-th component, for i∈⟦1,k⟧i\in\llbracket 1,k\rrbracket, is (p^n,i−pi)​(n/pi)1/2(\widehat{p}\_{n,i}-p\_{i})(n/p\_{i})^{1/2}, and

|  |  |  |
| --- | --- | --- |
|  | Θ=Wt​W=∑i=1kn​(p^n,i−pi)2pi.\Theta=W^{t}W=\sum\_{i=1}^{k}\frac{n(\widehat{p}\_{n,i}-p\_{i})^{2}}{p\_{i}}. |  |

The properties of multinomial variables indicate that the covariance matrix of the vector WW is Γk=V​Vt\Gamma\_{k}=VV^{t}, whose rank is k−1k-1 as explained above. Therefore, we can decompose WW in an orthonormal basis of dimension k−1k-1: we define a vector U∈ℝk−1U\in\mathbb{R}^{k-1} as Vt​WV^{t}W, so that W=V​UW=VU and Θ=Ut​U\Theta=U^{t}U. Then, it appears that U=∑j=1nTjU=\sum\_{j=1}^{n}T\_{j}, where Tj=Vt​YjT\_{j}=V^{t}Y\_{j}. By linearity, 𝔼​(Tj)=0\mathbb{E}(T\_{j})=0 and, using the independence of YjY\_{j} and YℓY\_{\ell} for ℓ≠j\ell\neq j, we have as well

|  |  |  |
| --- | --- | --- |
|  | ∑j=1n𝔼​(Tj​Tjt)=∑j=1nVt​𝔼​(Yj​Yjt)​V=Vt​𝔼​(W​Wt)​V=Vt​Γk​V=Vt​V​Vt​V=Ik−1.\begin{array}[]{ccl}\sum\_{j=1}^{n}\mathbb{E}(T\_{j}T\_{j}^{t})&=&\sum\_{j=1}^{n}V^{t}\mathbb{E}(Y\_{j}Y\_{j}^{t})V\\ &=&V^{t}\mathbb{E}(WW^{t})V\\ &=&V^{t}\Gamma\_{k}V\\ &=&V^{t}VV^{t}V=I\_{k-1}.\end{array} |  |

These conditions on UU and TjT\_{j} are the ones that are required for Raič’s multivariate Berry-Esseen theorem [[60](https://arxiv.org/html/2512.16411v1#bib.bib60), Theorem 1.1]. For a proper application of this theorem, two other assumptions are still to be verified. First, because Yj=V​TjY\_{j}=VT\_{j}, YjY\_{j} and TjT\_{j} have the same Euclidean norm, Yjt​Yj=Tjt​Vt​V​Tj=Tjt​TjY\_{j}^{t}Y\_{j}=T\_{j}^{t}V^{t}VT\_{j}=T\_{j}^{t}T\_{j}, so that 𝔼​[(Tjt​Tj)3/2]=∑u=1k(1−pu)3/2/n3/2​pu1/2\mathbb{E}\left[\left(T\_{j}^{t}T\_{j}\right)^{3/2}\right]=\sum\_{u=1}^{k}(1-p\_{u})^{3/2}/n^{3/2}p\_{u}^{1/2} after equation ([13](https://arxiv.org/html/2512.16411v1#A2.E13 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")). Second, the set 𝒜k−1,x={Z∈ℝk−1|Zt​Z≤x}\mathcal{A}\_{k-1,x}=\{Z\in\mathbb{R}^{k-1}|Z^{t}Z\leq x\} is convex because it is the sublevel set of a convex function. We now have all the conditions for applying Raič’s theorem [[60](https://arxiv.org/html/2512.16411v1#bib.bib60), Theorem 1.1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℙ​(Θ≤x)−Fχk−12​(x)|=|ℙ​(U∈𝒜k−1,x)−ℙ​(G∈𝒜k−1,x)|≤(42​(k−1)1/4+16)​∑j=1n𝔼​[(Tjt​Tj)3/2]≤(42​(k−1)1/4+16)​∑u=1k(1−pu)3/2(n​pu)1/2,\begin{array}[]{ccl}\left|\mathbb{P}\left(\Theta\leq x\right)-F\_{\chi^{2}\_{k-1}}(x)\right|&=&\left|\mathbb{P}\left(U\in\mathcal{A}\_{k-1,x}\right)-\mathbb{P}(G\in\mathcal{A}\_{k-1,x})\right|\\ &\leq&\left(42(k-1)^{1/4}+16\right)\sum\_{j=1}^{n}\mathbb{E}\left[\left(T\_{j}^{t}T\_{j}\right)^{3/2}\right]\\ &\leq&\left(42(k-1)^{1/4}+16\right)\sum\_{u=1}^{k}\frac{(1-p\_{u})^{3/2}}{(np\_{u})^{1/2}},\end{array} |  | (14) |

where G∈ℝk−1G\in\mathbb{R}^{k-1} is a standard Gaussian vector.

We now adapt the above Berry-Esseen inequality to include the residual ℛ=2​n​∑i=1kRi​(p^n,i)\mathcal{R}=2n\sum\_{i=1}^{k}R\_{i}(\widehat{p}\_{n,i}) of 2​n​f​(p^n)2nf(\widehat{p}\_{n}), given by the Taylor expansion displayed in equation [12](https://arxiv.org/html/2512.16411v1#A2.E12 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). If p^n,i≥pi\widehat{p}\_{n,i}\geq p\_{i}, then ξn,i≥pi\xi\_{n,i}\geq p\_{i} and we simply have |Ri​(p^n,i)|≤|pi−p^n,i|3/6​pi2|R\_{i}(\widehat{p}\_{n,i})|\leq|p\_{i}-\widehat{p}\_{n,i}|^{3}/6p\_{i}^{2}. If p^n,i<pi\widehat{p}\_{n,i}<p\_{i}, we cannot properly bound the residual of the second-order Taylor expansion with the same method and we need a more precise analysis. The non-truncated Taylor series provides, for x∈[0,p]x\in[0,p],

|  |  |  |
| --- | --- | --- |
|  | Ri​(x)=(x−pi)3​∑j=3∞(−1)j​(x−pi)j−3j​(j−1)​pij−1.R\_{i}(x)=(x-p\_{i})^{3}\sum\_{j=3}^{\infty}\frac{(-1)^{j}(x-p\_{i})^{j-3}}{j(j-1)p\_{i}^{j-1}}. |  |

Noting hi​(x)=Ri​(x)/(x−pi)3h\_{i}(x)=R\_{i}(x)/(x-p\_{i})^{3}, we have

|  |  |  |
| --- | --- | --- |
|  | hi′​(x)=∑j=3∞(pi−x)j−2​(j−3)j​(j−1)​pij−1,h^{\prime}\_{i}(x)=\sum\_{j=3}^{\infty}\frac{(p\_{i}-x)^{j-2}(j-3)}{j(j-1)p\_{i}^{j-1}}, |  |

which is non-negative whatever x≤pix\leq p\_{i}. Since we also have hi​(pi)=−1/6​pi2h\_{i}(p\_{i})=-1/6p\_{i}^{2} and hi​(0)=−1/2​pi2h\_{i}(0)=-1/2p\_{i}^{2}, we finally get maxx∈[0,pi]⁡|hi​(x)|=1/2​pi2\max\_{x\in[0,p\_{i}]}|h\_{i}(x)|=1/2p\_{i}^{2}. Combining this result with our analysis for x≥pix\geq p\_{i}, we find that 1/2​pi21/2p\_{i}^{2} is an upper bound for |h​(x)||h(x)| whatever x∈[0,1]x\in[0,1]. Then, noting that LqL^{q} norms are non-increasing functions of qq, and writing μ=mini∈⟦1,k⟧⁡pi\mu=\min\_{i\in\llbracket 1,k\rrbracket}p\_{i}, we get

|  |  |  |
| --- | --- | --- |
|  | |ℛ|≤2​n​∑i=1k|pi−p^n,i|32​pi2≤nμ​(∑i=1k|pi−p^n,ipi|2)3/2=Θ3/2μ​n.\left|\mathcal{R}\right|\leq 2n\sum\_{i=1}^{k}\frac{\left|p\_{i}-\widehat{p}\_{n,i}\right|^{3}}{2p\_{i}^{2}}\leq\frac{n}{\sqrt{\mu}}\left(\sum\_{i=1}^{k}\left|\frac{p\_{i}-\widehat{p}\_{n,i}}{\sqrt{p\_{i}}}\right|^{2}\right)^{3/2}=\frac{\Theta^{3/2}}{\sqrt{\mu n}}. |  |

Since 2​n​f​(p^n)=Θ+ℛ2nf(\widehat{p}\_{n})=\Theta+\mathcal{R} and (Θ≤x−ρ)⇒(Θ+ℛ≤x)⇒(Θ≤x+ρ)(\Theta\leq x-\rho)\Rightarrow(\Theta+\mathcal{R}\leq x)\Rightarrow(\Theta\leq x+\rho) for ρ≥|ℛ|\rho\geq|\mathcal{R}|, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Kn,kdown​(Θ)≤x)≤ℙ​(2​n​f​(p^n)≤x)≤ℙ​(Kn,kup​(Θ)≤x),\mathbb{P}\left(K\_{n,k}^{\text{down}}(\Theta)\leq x\right)\leq\mathbb{P}\left(2nf(\widehat{p}\_{n})\leq x\right)\leq\mathbb{P}\left(K\_{n,k}^{\text{up}}(\Theta)\leq x\right), |  | (15) |

where Kn,kup:z≥0↦z−(μ​n)−1/2​z3/2K\_{n,k}^{\text{up}}:z\geq 0\mapsto z-(\mu n)^{-1/2}z^{3/2} and Kn,kdown:z≥0↦z+(μ​n)−1/2​z3/2K\_{n,k}^{\text{down}}:z\geq 0\mapsto z+(\mu n)^{-1/2}z^{3/2}. Also, because of the convexity of ff [[21](https://arxiv.org/html/2512.16411v1#bib.bib21), Theorem 2.7.2], we have the convexity of the set {q|2​n​f​(q)≤x}\{q|2nf(q)\leq x\}. So we can refine formula ([15](https://arxiv.org/html/2512.16411v1#A2.E15 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) by taking into account a constraint of convexity, that is the three sets in this formula have to be convex. Noting that Kn,kup​(0)=Kn,kdown​(0)=0<xK\_{n,k}^{\text{up}}(0)=K\_{n,k}^{\text{down}}(0)=0<x and that (Θ=0)⇒(∀i,p^n,i=pi)⇒(2​n​f​(p^n)=0<x)(\Theta=0)\Rightarrow(\forall i,\widehat{p}\_{n,i}=p\_{i})\Rightarrow(2nf(\widehat{p}\_{n})=0<x), 0 belongs to the three intervals of admissible values of Θ\Theta and the convexity constraint modifies inequalities ([15](https://arxiv.org/html/2512.16411v1#A2.E15 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) in

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Θ∈[0,κn,kdown​(x)])≤ℙ​(2​n​f​(p^n)≤x)≤ℙ​(Θ∈[0,κn,kup​(x)]),\mathbb{P}\left(\Theta\in[0,\kappa\_{n,k}^{\text{down}}(x)]\right)\leq\mathbb{P}\left(2nf(\widehat{p}\_{n})\leq x\right)\leq\mathbb{P}\left(\Theta\in[0,\kappa\_{n,k}^{\text{up}}(x)]\right), |  |

where κn,kup​(x)\kappa\_{n,k}^{\text{up}}(x) (respectively κn,kdown​(x)\kappa\_{n,k}^{\text{down}}(x)) is the smallest positive root of z↦Kn,kup​(z)−xz\mapsto K\_{n,k}^{\text{up}}(z)-x (resp. z↦Kn,kdown​(z)−xz\mapsto K\_{n,k}^{\text{down}}(z)-x) if it exists, otherwise the probabilities are trivially equal to 1. An explicit expression for κn,kup​(x)\kappa\_{n,k}^{\text{up}}(x) and κn,kdown​(x)\kappa\_{n,k}^{\text{down}}(x) is obtained as the solution of a cubic equation, solved with Cardano’s formula. Indeed, using Lemma [1](https://arxiv.org/html/2512.16411v1#Thmlem1 "Lemma 1. ‣ Appendix A A useful lemma for proving Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") applied to z\sqrt{z}, with d=xd=x and a=−(μ​n)−1/2a=-(\mu n)^{-1/2} for κn,kup​(x)\kappa\_{n,k}^{\text{up}}(x) or a=(μ​n)−1/2a=(\mu n)^{-1/2} for κn,kdown​(x)\kappa\_{n,k}^{\text{down}}(x), we directly obtain the expression displayed in Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). We also have (μ​n)−1/2→0(\mu n)^{-1/2}\rightarrow 0 and Lemma [1](https://arxiv.org/html/2512.16411v1#Thmlem1 "Lemma 1. ‣ Appendix A A useful lemma for proving Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") provides us with the asymptotic behaviour of κn,kup​(x)\kappa\_{n,k}^{\text{up}}(x), namely

|  |  |  |
| --- | --- | --- |
|  | κn,kup​(x)=x+x2​μ​n+𝒪​(1n),\sqrt{\kappa\_{n,k}^{\text{up}}(x)}=\sqrt{x}+\frac{x}{2\sqrt{\mu n}}+\mathcal{O}\left(\frac{1}{n}\right), |  |

which gives

|  |  |  |
| --- | --- | --- |
|  | κn,kup​(x)=x+x3/2μ​n+𝒪​(1n).\kappa\_{n,k}^{\text{up}}(x)=x+\frac{x^{3/2}}{\sqrt{\mu n}}+\mathcal{O}\left(\frac{1}{n}\right). |  |

A similar idea makes it possible to lead to the result displayed in Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") for κn,kdown​(x)\kappa\_{n,k}^{\text{down}}(x).

Finally, we can use Raič’s theorem again, using directly formula ([14](https://arxiv.org/html/2512.16411v1#A2.E14 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) with a new value for xx:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(2​n​f​(p^n)≤x)≤ℙ​(Θ≤κn,kup​(x))≤Fχk−12​(κn,kup​(x))+|ℙ​(Θ≤κn,kup​(x))−Fχk−12​(κn,kup​(x))|≤Fχk−12​(κn,kup​(x))+(42​(k−1)1/4+16)​∑u=1k(1−pu)3/2(n​pu)1/2.\begin{array}[]{ccl}\mathbb{P}\left(2nf(\widehat{p}\_{n})\leq x\right)&\leq&\mathbb{P}\left(\Theta\leq\kappa\_{n,k}^{\text{up}}(x)\right)\\ &\leq&F\_{\chi^{2}\_{k-1}}(\kappa\_{n,k}^{\text{up}}(x))+\left|\mathbb{P}\left(\Theta\leq\kappa\_{n,k}^{\text{up}}(x)\right)-F\_{\chi^{2}\_{k-1}}(\kappa\_{n,k}^{\text{up}}(x))\right|\\ &\leq&F\_{\chi^{2}\_{k-1}}(\kappa\_{n,k}^{\text{up}}(x))+\left(42(k-1)^{1/4}+16\right)\sum\_{u=1}^{k}\frac{(1-p\_{u})^{3/2}}{(np\_{u})^{1/2}}.\end{array} |  |

We similarly get

|  |  |  |
| --- | --- | --- |
|  | ℙ​(2​n​f​(p^n)≤x)≥ℙ​(Θ≤κn,kdown​(x))≥Fχk−12​(κn,kdown​(x))−|ℙ​(Θ≤κn,kdown​(x))−Fχk−12​(κn,kup​(x))|\begin{array}[]{ccl}\mathbb{P}\left(2nf(\widehat{p}\_{n})\leq x\right)&\geq&\mathbb{P}\left(\Theta\leq\kappa\_{n,k}^{\text{down}}(x)\right)\\ &\geq&F\_{\chi^{2}\_{k-1}}(\kappa\_{n,k}^{\text{down}}(x))-\left|\mathbb{P}\left(\Theta\leq\kappa\_{n,k}^{\text{down}}(x)\right)-F\_{\chi^{2}\_{k-1}}(\kappa\_{n,k}^{\text{up}}(x))\right|\end{array} |  |

and we can now conclude with the statement of the theorem.
∎

## Appendix C Proof of Theorem [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") and Proposition [1](https://arxiv.org/html/2512.16411v1#Thmpro1 "Proposition 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")

We start by the proof of Theorem [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

###### Proof.

As seen in the proof of Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), the vector whose ii-th component, for i∈⟦1,k⟧i\in\llbracket 1,k\rrbracket, is n​(p^n,i−pi)/pi\sqrt{n}(\widehat{p}\_{n,i}-p\_{i})/\sqrt{p\_{i}} converges toward a Gaussian vector G1G\_{1} of covariance matrix Γk\Gamma\_{k}. We have the same result when considering m​(q^m,i−pi)/pi\sqrt{m}(\widehat{q}\_{m,i}-p\_{i})/\sqrt{p\_{i}}, with the convergence toward the Gaussian vector G2G\_{2} of covariance matrix Γk\Gamma\_{k} and independent of G1G\_{1}. Therefore, we get, for n,m→∞n,m\rightarrow\infty,

|  |  |  |
| --- | --- | --- |
|  | n​mn+m​(p^n,1−q^m,1p1⋮p^n,k−q^m,kpk)=n​mn+m​(p^n,1−p1p1⋮p^n,k−pkpk)−m​nn+m​(q^m,1−p1p1⋮q^m,k−pkpk)⟶d1−λ​G1−λ​G2,\begin{array}[]{ccl}\sqrt{\frac{nm}{n+m}}\left(\begin{array}[]{c}\frac{\widehat{p}\_{n,1}-\widehat{q}\_{m,1}}{\sqrt{p\_{1}}}\\ \vdots\\ \frac{\widehat{p}\_{n,k}-\widehat{q}\_{m,k}}{\sqrt{p\_{k}}}\end{array}\right)&=&\sqrt{n}\sqrt{\frac{m}{n+m}}\left(\begin{array}[]{c}\frac{\widehat{p}\_{n,1}-p\_{1}}{\sqrt{p\_{1}}}\\ \vdots\\ \frac{\widehat{p}\_{n,k}-p\_{k}}{\sqrt{p\_{k}}}\end{array}\right)-\sqrt{m}\sqrt{\frac{n}{n+m}}\left(\begin{array}[]{c}\frac{\widehat{q}\_{m,1}-p\_{1}}{\sqrt{p\_{1}}}\\ \vdots\\ \frac{\widehat{q}\_{m,k}-p\_{k}}{\sqrt{p\_{k}}}\end{array}\right)\\ &\overset{\text{d}}{\longrightarrow}&\sqrt{1-\lambda}G\_{1}-\sqrt{\lambda}G\_{2},\end{array} |  |

which, by independence, is a Gaussian vector of covariance matrix Γk\Gamma\_{k}.

The successive derivatives of the relative entropy are ∂piDK​L​(p∥q)=1+log⁡(pi/qi)\partial\_{p\_{i}}D\_{KL}(p\|q)=1+\log(p\_{i}/q\_{i}), ∂qiDK​L​(p∥q)=−pi/qi\partial\_{q\_{i}}D\_{KL}(p\|q)=-p\_{i}/q\_{i}, ∂pi​pi2DK​L​(p∥q)=1/pi\partial^{2}\_{p\_{i}p\_{i}}D\_{KL}(p\|q)=1/p\_{i}, ∂qi​qi2DK​L​(p∥q)=pi/qi2\partial^{2}\_{q\_{i}q\_{i}}D\_{KL}(p\|q)=p\_{i}/q\_{i}^{2}, and ∂pi​qi2DK​L​(p∥q)=−1/qi\partial^{2}\_{p\_{i}q\_{i}}D\_{KL}(p\|q)=-1/q\_{i}. Therefore, noting δn,i=p^n,i−pi\delta\_{n,i}=\widehat{p}\_{n,i}-p\_{i} and γm,i=q^m,i−pi\gamma\_{m,i}=\widehat{q}\_{m,i}-p\_{i}, a second-order Taylor expansion gives

|  |  |  |
| --- | --- | --- |
|  | DK​L​(p^n∥q^m)=∑i=1k[δn,i−γm,i+δn,i22​pi+γm,i22​pi−δn,i​γm,ipi+o​(δn,i2+γm,i2)]=∑i=1k(δn,i−γm,i)22​pi+o​(δn,i2+γm,i2)=∑i=1k(p^n,i−q^m,i)22​pi+o​(δn,i2+γm,i2).\begin{array}[]{ccl}D\_{KL}(\widehat{p}\_{n}\|\widehat{q}\_{m})&=&\sum\_{i=1}^{k}\left[\delta\_{n,i}-\gamma\_{m,i}+\frac{\delta\_{n,i}^{2}}{2p\_{i}}+\frac{\gamma\_{m,i}^{2}}{2p\_{i}}-\frac{\delta\_{n,i}\gamma\_{m,i}}{p\_{i}}+o\left(\delta\_{n,i}^{2}+\gamma\_{m,i}^{2}\right)\right]\\ &=&\sum\_{i=1}^{k}\frac{(\delta\_{n,i}-\gamma\_{m,i})^{2}}{2p\_{i}}+o\left(\delta\_{n,i}^{2}+\gamma\_{m,i}^{2}\right)\\ &=&\sum\_{i=1}^{k}\frac{(\widehat{p}\_{n,i}-\widehat{q}\_{m,i})^{2}}{2p\_{i}}+o\left(\delta\_{n,i}^{2}+\gamma\_{m,i}^{2}\right).\end{array} |  |

The leading term of this expansion is proportional to the Euclidean norm of the vector whose limit it the above Gaussian of covariance Γk\Gamma\_{k}. The framework is so exactly the same as in the proof of Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") and we can conclude that

|  |  |  |
| --- | --- | --- |
|  | 2​n​mn+m​DK​L​(p^n∥q^m)​⟶d​χk−12.2\frac{nm}{n+m}D\_{KL}(\widehat{p}\_{n}\|\widehat{q}\_{m})\overset{\text{d}}{\longrightarrow}\chi^{2}\_{k-1}. |  |

∎

We now prove Proposition [1](https://arxiv.org/html/2512.16411v1#Thmpro1 "Proposition 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").

###### Proof.

We define, for j∈⟦1,n+m⟧j\in\llbracket 1,n+m\rrbracket,

|  |  |  |
| --- | --- | --- |
|  | Yj=(𝟙Xj∈Ω1−p1(n+m)​p1,…,𝟙Xj∈Ωk−pk(n+m)​pk)tY\_{j}=\left(\frac{\mathds{1}\_{X\_{j}\in\Omega\_{1}}-p\_{1}}{\sqrt{(n+m)p\_{1}}},...,\frac{\mathds{1}\_{X\_{j}\in\Omega\_{k}}-p\_{k}}{\sqrt{(n+m)p\_{k}}}\right)^{t} |  |

and

|  |  |  |
| --- | --- | --- |
|  | Y~j={mn​Yjif ​j∈⟦1,n⟧−nm​Yjif ​j∈⟦n+1,n+m⟧.\widetilde{Y}\_{j}=\left\{\begin{array}[]{ll}\sqrt{\frac{m}{n}}Y\_{j}&\text{if }j\in\llbracket 1,n\rrbracket\\ -\sqrt{\frac{n}{m}}Y\_{j}&\text{if }j\in\llbracket n+1,n+m\rrbracket.\end{array}\right. |  |

Then, Y~1,…,Y~n+m\widetilde{Y}\_{1},...,\widetilde{Y}\_{n+m} are independent of each other and such that, noting W~=∑j=1n+mY~j\widetilde{W}=\sum\_{j=1}^{n+m}\widetilde{Y}\_{j}, we have 𝔼​(Y~j)=0\mathbb{E}(\widetilde{Y}\_{j})=0 and, after Theorem [2](https://arxiv.org/html/2512.16411v1#Thmthm2 "Theorem 2. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), ∑j=1n+m𝔼​(Y~j​Y~jt)=𝔼​(W~​W~t)=Γk\sum\_{j=1}^{n+m}\mathbb{E}(\widetilde{Y}\_{j}\widetilde{Y}\_{j}^{t})=\mathbb{E}(\widetilde{W}\widetilde{W}^{t})=\Gamma\_{k}, with the same Γk=V​Vt\Gamma\_{k}=VV^{t} as in the proof of Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"). Therefore, we can use Raič’s theorem again [[60](https://arxiv.org/html/2512.16411v1#bib.bib60), Theorem 1.1], applied to U~=Vt​W~\widetilde{U}=V^{t}\widetilde{W} and T~j=Vt​Y~j\widetilde{T}\_{j}=V^{t}\widetilde{Y}\_{j}, T~j\widetilde{T}\_{j} having the same Euclidean norm as Y~j\widetilde{Y}\_{j}. Noting

|  |  |  |
| --- | --- | --- |
|  | Θ~=W~t​W~=n​mn+m​∑i=1k(p^i−q^i)2pi,\widetilde{\Theta}=\widetilde{W}^{t}\widetilde{W}=\frac{nm}{n+m}\sum\_{i=1}^{k}\frac{\left(\widehat{p}\_{i}-\widehat{q}\_{i}\right)^{2}}{p\_{i}}, |  |

we can thus write, like in the proof of Theorem [1](https://arxiv.org/html/2512.16411v1#Thmthm1 "Theorem 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℙ​(Θ~≤x)−Fχk−12​(x)|≤(42​(k−1)1/4+16)​∑j=1n+m𝔼​[(Y~jt​Y~j)3/2].\left|\mathbb{P}\left(\widetilde{\Theta}\leq x\right)-F\_{\chi^{2}\_{k-1}}(x)\right|\leq\left(42(k-1)^{1/4}+16\right)\sum\_{j=1}^{n+m}\mathbb{E}\left[\left(\widetilde{Y}\_{j}^{t}\widetilde{Y}\_{j}\right)^{3/2}\right]. |  | (16) |

We know, from equation ([13](https://arxiv.org/html/2512.16411v1#A2.E13 "In Proof. ‣ Appendix B Proof of Theorem 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) the expression of 𝔼​[(Yjt​Yj)3/2]\mathbb{E}\left[\left(Y\_{j}^{t}Y\_{j}\right)^{3/2}\right], from which we deduce that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Y~jt​Y~j)3/2]={m3/2n3/2​(n+m)3/2​∑u=1k(1−pu)3/2pu1/2if ​j∈⟦1,n⟧n3/2m3/2​(n+m)3/2​∑u=1k(1−pu)3/2pu1/2if ​j∈⟦n+1,n+m⟧.\mathbb{E}\left[\left(\widetilde{Y}\_{j}^{t}\widetilde{Y}\_{j}\right)^{3/2}\right]=\left\{\begin{array}[]{ll}\frac{m^{3/2}}{n^{3/2}(n+m)^{3/2}}\sum\_{u=1}^{k}\frac{(1-p\_{u})^{3/2}}{p\_{u}^{1/2}}&\text{if }j\in\llbracket 1,n\rrbracket\\ \frac{n^{3/2}}{m^{3/2}(n+m)^{3/2}}\sum\_{u=1}^{k}\frac{(1-p\_{u})^{3/2}}{p\_{u}^{1/2}}&\text{if }j\in\llbracket n+1,n+m\rrbracket.\end{array}\right. |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | ∑j=1n+m𝔼​[(Y~jt​Y~j)3/2]=(m3/2n1/2​(n+m)3/2+n3/2m1/2​(n+m)3/2)​∑u=1k(1−pu)3/2pu1/2=m2+n2(n​m)1/2​(n+m)3/2​∑u=1k(1−pu)3/2pu1/2\begin{array}[]{ccl}\sum\_{j=1}^{n+m}\mathbb{E}\left[\left(\widetilde{Y}\_{j}^{t}\widetilde{Y}\_{j}\right)^{3/2}\right]&=&\left(\frac{m^{3/2}}{n^{1/2}(n+m)^{3/2}}+\frac{n^{3/2}}{m^{1/2}(n+m)^{3/2}}\right)\sum\_{u=1}^{k}\frac{(1-p\_{u})^{3/2}}{p\_{u}^{1/2}}\\ &=&\frac{m^{2}+n^{2}}{(nm)^{1/2}(n+m)^{3/2}}\sum\_{u=1}^{k}\frac{(1-p\_{u})^{3/2}}{p\_{u}^{1/2}}\end{array} |  |

and, combining it with equation ([16](https://arxiv.org/html/2512.16411v1#A3.E16 "In Proof. ‣ Appendix C Proof of Theorem 2 and Proposition 1 ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), we finally obtain the result displayed in Proposition [1](https://arxiv.org/html/2512.16411v1#Thmpro1 "Proposition 1. ‣ 2.2 Asymptotic and pre-asymptotic distributions of empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection").
∎

## Appendix D Proof of Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")

###### Proof.

We know that the moment-generating function of DKL​(p^n∥p)D\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right) is upper bounded by

|  |  |  |
| --- | --- | --- |
|  | M​(t)=(∑j=0nn!n2​j​(n−j)!​tj)k−1,M(t)=\left(\sum\_{j=0}^{n}\frac{n!}{n^{2j}(n-j)!}t^{j}\right)^{k-1}, |  |

for t∈[0,n)t\in[0,n) [[2](https://arxiv.org/html/2512.16411v1#bib.bib2), Proposition II.2, Lemmas II.4 and II.5]. So, using Chernoff inequality, we get the first bound displayed in Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), ℳk,n1​(x)\mathcal{M}^{1}\_{k,n}(x). The last bound, ℳk,n3​(x)\mathcal{M}^{3}\_{k,n}(x), is Agrawal’s bound, which relies on the fact that M​(t)≤MAgrawal​(t)=(1−t/n)−k+1M(t)\leq M\_{\text{Agrawal}}(t)=\left(1-t/n\right)^{-k+1} and on the optimisation in tt of the Chernoff bound inft∈[0,n)e−t​x​MAgrawal​(t)\inf\_{t\in[0,n)}e^{-tx}M\_{\text{Agrawal}}(t), the minimum being reached for tt equal to t⋆=n−(k−1)/x∈[0,n)t^{\star}=n-(k-1)/x\in[0,n) [[2](https://arxiv.org/html/2512.16411v1#bib.bib2), Theorem I.2]. Using this same value t⋆t^{\star} in M​(t)M(t), we get the middle bound, ℳk,n2​(x)\mathcal{M}^{2}\_{k,n}(x), which is higher than ℳk,n1​(x)\mathcal{M}^{1}\_{k,n}(x) because t⋆∈[0,n)t^{\star}\in[0,n), and lower than ℳk,n3​(x)\mathcal{M}^{3}\_{k,n}(x) because M​(t)≤MAgrawal​(t)M(t)\leq M\_{\text{Agrawal}}(t) for all t∈[0,n)t\in[0,n), including t⋆t^{\star}.
∎

## Appendix E Proofs for two-sample concentration inequalities

### E.1 Proof of Proposition [3](https://arxiv.org/html/2512.16411v1#Thmpro3 "Proposition 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")

###### Proof.

Noting ‖x‖1=∑i=1k|xi|\|x\|\_{1}=\sum\_{i=1}^{k}|x\_{i}|, we have, by triangular inequality ‖x−y‖1≤‖x‖1+‖y‖1\|x-y\|\_{1}\leq\|x\|\_{1}+\|y\|\_{1}, so, combining this with Young’s inequality, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖x−y‖12≤2​‖x‖12+2​‖y‖12.\|x-y\|\_{1}^{2}\leq 2\|x\|\_{1}^{2}+2\|y\|\_{1}^{2}. |  | (17) |

Using successively the right part of formula ([8](https://arxiv.org/html/2512.16411v1#S2.E8 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), formula ([17](https://arxiv.org/html/2512.16411v1#A5.E17 "In Proof. ‣ E.1 Proof of Proposition 3 ‣ Appendix E Proofs for two-sample concentration inequalities ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), and the left part of formula ([8](https://arxiv.org/html/2512.16411v1#S2.E8 "In 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")), we get

|  |  |  |
| --- | --- | --- |
|  | DKL​(p∥q)≤(12​mini⁡qi−mini⁡pi2​qi)​‖p−q‖12≤(1mini⁡qi−mini⁡piqi)​(‖p−r‖12+‖q−r‖12)≤(2mini⁡qi−2​mini⁡piqi)​(DKL​(p∥r)+DKL​(q∥r)).\begin{array}[]{ccl}D\_{\text{KL}}\left(p\|q\right)&\leq&\left(\frac{1}{2\min\_{i}q\_{i}}-\min\_{i}\frac{p\_{i}}{2q\_{i}}\right)\|p-q\|\_{1}^{2}\\ &\leq&\left(\frac{1}{\min\_{i}q\_{i}}-\min\_{i}\frac{p\_{i}}{q\_{i}}\right)\left(\|p-r\|\_{1}^{2}+\|q-r\|\_{1}^{2}\right)\\ &\leq&\left(\frac{2}{\min\_{i}q\_{i}}-2\min\_{i}\frac{p\_{i}}{q\_{i}}\right)\left(D\_{\text{KL}}\left(p\|r\right)+D\_{\text{KL}}\left(q\|r\right)\right).\end{array} |  |

∎

### E.2 Proof of Theorem [3](https://arxiv.org/html/2512.16411v1#Thmthm3 "Theorem 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")

###### Proof.

Using Proposition [3](https://arxiv.org/html/2512.16411v1#Thmpro3 "Proposition 3. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection") along with the independence of p^n\widehat{p}\_{n} and q^m\widehat{q}\_{m}, the moment-generating function of the two-sample relative entropy follows, for t≥0t\geq 0:

|  |  |  |
| --- | --- | --- |
|  | 𝔼[exp(tDKL(p^n∥q^m))]≤𝔼[exp(tβm,nDKL(p^n∥p)]𝔼[tβm,nDKL(q^m∥p))].\mathbb{E}\left[\exp\left(tD\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{m}\right)\right)\right]\leq\mathbb{E}\left[\exp\left(t\beta\_{m,n}D\_{\text{KL}}\left(\widehat{p}\_{n}\|p\right)\right]\mathbb{E}\left[t\beta\_{m,n}D\_{\text{KL}}\left(\widehat{q}\_{m}\|p\right)\right)\right]. |  |

According to Agrawal’s inequality, we thus have, for t∈[0,min⁡(m,n)/βm,n)t\in[0,\min(m,n)/\beta\_{m,n}) [[2](https://arxiv.org/html/2512.16411v1#bib.bib2), Theorem 1.3]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[exp⁡(t​DKL​(p^n∥q^m))]≤(1(1−t​βm,n/m)​(1−t​βm,n/n))k−1.\mathbb{E}\left[\exp\left(tD\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{m}\right)\right)\right]\leq\left(\frac{1}{(1-t\beta\_{m,n}/m)(1-t\beta\_{m,n}/n)}\right)^{k-1}. |  | (18) |

Therefore, by a substitution s=t​βm,ns=t\beta\_{m,n} and Chernoff inequality, we obtain, for x>0x>0, ℙ​(DKL​(p^n∥q^n)≥x)≤infs∈[0,min⁡(m,n))exp⁡(f​(s))\mathbb{P}\left(D\_{\text{KL}}\left(\widehat{p}\_{n}\|\widehat{q}\_{n}\right)\geq x\right)\leq\inf\_{s\in[0,\min(m,n))}\exp(f(s)), with

|  |  |  |
| --- | --- | --- |
|  | f​(s)=−s​xβm,n−(k−1)​log⁡(1−sm)−(k−1)​log⁡(1−sn).f(s)=-\frac{sx}{\beta\_{m,n}}-(k-1)\log\left(1-\frac{s}{m}\right)-(k-1)\log\left(1-\frac{s}{n}\right). |  |

We have f​(0)=0f(0)=0 and lims→min⁡(m,n)f​(s)=+∞\lim\_{s\rightarrow\min(m,n)}f(s)=+\infty. The derivative of ff is

|  |  |  |
| --- | --- | --- |
|  | f′​(s)=−xβm,n−(k−1)​(1s−m+1s−n).f^{\prime}(s)=-\frac{x}{\beta\_{m,n}}-(k-1)\left(\frac{1}{s-m}+\frac{1}{s-n}\right). |  |

Noting λ=x/βm,n​(k−1)\lambda=x/\beta\_{m,n}(k-1), ss is a zero of f′f^{\prime} iff

|  |  |  |
| --- | --- | --- |
|  | λ​s2+(2−λ​(n+m))​s+λ​m​n−m−n=0,\lambda s^{2}+(2-\lambda(n+m))s+\lambda mn-m-n=0, |  |

equation whose discriminant is 4+λ2​(m−n)2>04+\lambda^{2}(m-n)^{2}>0, leading to the two possible roots

|  |  |  |
| --- | --- | --- |
|  | {s⋆=λ​(n+m)−2−4+λ2​(m−n)22​λs∙=λ​(n+m)−2+4+λ2​(m−n)22​λ.\left\{\begin{array}[]{lll}s^{\star}&=&\frac{\lambda(n+m)-2-\sqrt{4+\lambda^{2}(m-n)^{2}}}{2\lambda}\\ s^{\bullet}&=&\frac{\lambda(n+m)-2+\sqrt{4+\lambda^{2}(m-n)^{2}}}{2\lambda}.\end{array}\right. |  |

By symmetry, one can assume m≤nm\leq n. The condition s⋆∈[0,min⁡(m,n))s^{\star}\in[0,\min(m,n)) gives, for the upper bound,

|  |  |  |
| --- | --- | --- |
|  | λ​(n+m)−2−4+λ2​(m−n)2<2​λ​m,\lambda(n+m)-2-\sqrt{4+\lambda^{2}(m-n)^{2}}<2\lambda m, |  |

that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(n−m)−2<4+λ2​(m−n)2.\lambda(n-m)-2<\sqrt{4+\lambda^{2}(m-n)^{2}}. |  | (19) |

When λ​(n−m)<2\lambda(n-m)<2, formula ([19](https://arxiv.org/html/2512.16411v1#A5.E19 "In Proof. ‣ E.2 Proof of Theorem 3 ‣ Appendix E Proofs for two-sample concentration inequalities ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) always holds. If λ​(n−m)≥2\lambda(n-m)\geq 2, then, after considering the square, formula ([19](https://arxiv.org/html/2512.16411v1#A5.E19 "In Proof. ‣ E.2 Proof of Theorem 3 ‣ Appendix E Proofs for two-sample concentration inequalities ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) simplifies to −4​λ​(n−m)<0-4\lambda(n-m)<0, which always holds since λ​(n−m)≥2\lambda(n-m)\geq 2. Now, the lower constraint s⋆≥0s^{\star}\geq 0 leads to

|  |  |  |
| --- | --- | --- |
|  | λ​(m+n)−2≥4+λ2​(m−n)2,\lambda(m+n)-2\geq\sqrt{4+\lambda^{2}(m-n)^{2}}, |  |

that is λ​(m+n)≥2\lambda(m+n)\geq 2 and λ≥(m+n)/m​n\lambda\geq(m+n)/mn. A direct calculation also shows that (m+n)/m​n>2/(m+n)(m+n)/mn>2/(m+n). On the other hand, the root s∙s^{\bullet} never falls in the interval [0,min⁡(m,n))[0,\min(m,n)). Indeed, still assuming m≤nm\leq n, the condition s∙<ms^{\bullet}<m requires

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(n−m)−2<−4+λ2​(m−n)2,\lambda(n-m)-2<-\sqrt{4+\lambda^{2}(m-n)^{2}}, |  | (20) |

which is never verified because, by the elementary inequality, 2​(4+λ2​(m−n)2)≥(2+λ​|m−n|)22(4+\lambda^{2}(m-n)^{2})\geq(2+\lambda|m-n|)^{2}, so that condition ([20](https://arxiv.org/html/2512.16411v1#A5.E20 "In Proof. ‣ E.2 Proof of Theorem 3 ‣ Appendix E Proofs for two-sample concentration inequalities ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) writes

|  |  |  |
| --- | --- | --- |
|  | λ​(n−m)−2<−12​(2+λ​|m−n|)\lambda(n-m)-2<-\frac{1}{\sqrt{2}}(2+\lambda|m-n|) |  |

and λ​(n−m)<2​(2−2)/(1+2)<0\lambda(n-m)<\sqrt{2}(2-\sqrt{2})/(1+\sqrt{2})<0, which contradicts the assumptions.

Therefore, when λ≥max⁡(2/(m+n),(m+n)/m​n)=(m+n)/m​n\lambda\geq\max(2/(m+n),(m+n)/mn)=(m+n)/mn, then f′​(0)≤0f^{\prime}(0)\leq 0 and the minimum of ff in the interval [0,min⁡(m,n))[0,\min(m,n)) is reached in s⋆s^{\star}. If λ<(m+n)/m​n\lambda<(m+n)/mn, then f′​(0)>0f^{\prime}(0)>0, with no root of f′f^{\prime} in [0,min⁡(m,n))[0,\min(m,n)), so that the minimum of ff in this interval is reached in 0. This provides us with the bound ℳ~k,n,m3​(x)\widetilde{\mathcal{M}}^{3}\_{k,n,m}(x), in which σm,n,x\sigma\_{m,n,x} is simply equal to s⋆s^{\star}.

Like in Proposition [2](https://arxiv.org/html/2512.16411v1#Thmpro2 "Proposition 2. ‣ 2.3 Concentration inequalities for empirical relative entropy ‣ 2 Distribution of empirical relative entropy ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection"), one can also modify formula ([18](https://arxiv.org/html/2512.16411v1#A5.E18 "In Proof. ‣ E.2 Proof of Theorem 3 ‣ Appendix E Proofs for two-sample concentration inequalities ‣ Asymptotic and finite-sample distributions of one- and two-sample empirical relative entropy, with application to change-point detection")) to use the true moment-generating function, so we get ℳ~k,n,m1​(x)\widetilde{\mathcal{M}}^{1}\_{k,n,m}(x) and ℳ~k,n,m2​(x)\widetilde{\mathcal{M}}^{2}\_{k,n,m}(x).
∎