---
authors:
- Takaaki Shiotani
- Takaki Hayashi
- Yuta Koike
doc_id: arxiv:2601.01871v1
family_id: arxiv:2601.01871
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On lead-lag estimation of non-synchronously observed point processes
url_abs: http://arxiv.org/abs/2601.01871v1
url_html: https://arxiv.org/html/2601.01871v1
venue: arXiv q-fin
version: 1
year: 2026
---


Takaaki Shiotani
Graduate School of Mathematical Sciences, The University of Tokyo, 3-8-1 Komaba, Meguro-ku, Tokyo 153-8914 Japan
  
Takaki Hayashi
Graduate School of Business Administration, Keio University, 4-1-1 Hiyoshi, Yokohama 223-8526, Japan
  
Yuta Koike11footnotemark: 1

###### Abstract

This paper introduces a new theoretical framework for analyzing lead-lag relationships between point processes, with a special focus on applications to high-frequency financial data.
In particular, we are interested in lead-lag relationships between two sequences of order arrival timestamps.
The seminal work of Dobrev and Schaumburg proposed model-free measures of cross-market trading activity based on cross-counts of timestamps.
While their method is known to yield reliable results, it faces limitations because its original formulation inherently relies on discrete-time observations, an issue we address in this study.
Specifically, we formulate the problem of estimating lead-lag relationships in two point processes as that of estimating the shape of the cross-pair correlation function (CPCF) of a bivariate stationary point process, a quantity well-studied in the neuroscience and spatial statistics literature.
Within this framework, the prevailing lead-lag time is defined as the location of the CPCF’s sharpest peak.
Under this interpretation, the peak location in Dobrev and Schaumburg’s cross-market activity measure can be viewed as an estimator of the lead-lag time in the aforementioned sense.
We further propose an alternative lead-lag time estimator based on kernel density estimation and show that it possesses desirable theoretical properties and delivers superior numerical performance.
Empirical evidence from high-frequency financial data demonstrates the effectiveness of our proposed method.

Keywords: Bandwidth selection; cross-correlation histogram; cross-pair correlation function; high-frequency data; non-synchronicity; lead-lag effect.

## 1 Introduction

Empirical research on lead-lag relationships between two financial time series has long been an active area of study in finance.
Their identification is fundamental to understanding price discovery and may provide practitioners with opportunities for excess profits.
In modern financial markets, such relationships can persist only over very short horizons, even on the order of one millisecond or less.
Therefore, lower-frequency or coarsely aggregated data inevitably fail to find the fine structure of these relationships.
This motivates the use of *tick data*, i.e., raw high-frequency data that records all transactions as they arrive randomly and *non-synchronously*. In particular, handling non-synchronicity is a central issue when estimating lead–lag relationships from such data.

Most existing studies have examined high-frequency lead-lag dynamics using price series.
Prominent approaches include methods based on estimating the cross-covariance function [hoffmann2013estimation, de1997high, huth2014high], wavelet analysis [hayashi2017multi, hayashi2018wavelet], local spectral estimation [koike2021inference], Hawkes process-based multi-asset models [bacry2013some, da2017correlation] and the multi-asset lagged adjustment model of [buccheri2021high].
Among these, hoffmann2013estimation introduced a simple cross-covariance estimator that can be computed directly from non-synchronously observed returns and proposed estimating the prevailing lead-lag time by locating its maximizer.
Although their method yields sensible empirical implications due to its intuitive interpretation [huth2014high, bollen2017tail, bangsgaard2024lead, dao2018ultra, alsayed2014ultra, poutre2024profitability], the resulting lead-lag time estimates are often unstable and unreliable [huth2014high, hayashi2017jpn, bangsgaard2024lead], presumably because high-frequency price series are affected by market microstructure noise.
As an alternative method, dobrev2017high proposed model-free measurements of the lead-lag relationship between two assets based on cross-counts of their order arrivals.
Their estimator of lead–lag time has been shown to produce highly stable and reliable estimates in practice; see [dobrev2017high, hayashi2017jpn].

However, the Dobrev–Schaumburg method is essentially descriptive, and it is not immediately clear what underlying quantity the method actually estimates.111Although [dobrev2023high] discuss some asymptotic properties of their measurements when the two timestamp series are independent, they do not clearly specify the underlying estimands.
Indeed, as we show in [Section 2](https://arxiv.org/html/2601.01871v1#S2 "2 The Dobrev–Schaumburg method ‣ On lead-lag estimation of non-synchronously observed point processes"), there exist situations in which their method performs poorly in practice, particularly when the data contain relatively few observations.
Moreover, implementing their method requires partitioning the observation period into equi-spaced buckets, and the choice of bucket size has a substantial impact on the results.
Yet, because the method is “model-free,” it does not offer a statistical explanation for why such sensitivity arises.

To address these issues, we reformulate the Dobrev–Schaumburg method from a point process perspective.
This viewpoint reveals that their measurements essentially estimate shape characteristics of the *cross-pair correlation function* (CPCF) of a bivariate point process generated by order arrivals; see [Section 3](https://arxiv.org/html/2601.01871v1#S3 "3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") for definitions.
Accordingly, the Dobrev–Schaumburg estimator of lead-lag time can be interpreted as an estimator of the CPCF’s sharpest peak location.
This interpretation also clarifies that the instability observed in their method arises when the bucket size is chosen too small relative to a range that is permissible given the properties of the underlying data.
At the same time, because their estimator can only take values that are integer multiples of the bucket size, using a larger bucket size results in excessively coarse estimates.
To overcome these limitations, we propose a nonparametric, kernel-based estimator of the lead–lag time, together with a data-driven bandwidth selection procedure. We show both theoretically and empirically that this new estimator produces stable and accurate results even in settings where the Dobrev–Schaumburg method fails.

The remainder of the paper is organized as follows.
[Section 2](https://arxiv.org/html/2601.01871v1#S2 "2 The Dobrev–Schaumburg method ‣ On lead-lag estimation of non-synchronously observed point processes") provides a detailed explanation of the Dobrev–Schaumburg method.
[Section 3](https://arxiv.org/html/2601.01871v1#S3 "3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") introduces a point process framework that clarifies the theoretical meaning of the Dobrev–Schaumburg method.
[Section 4](https://arxiv.org/html/2601.01871v1#S4 "4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") proposes an alternative estimator of the lead-lag time within this framework and develops its theoretical properties.
[Section 5](https://arxiv.org/html/2601.01871v1#S5 "5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes") demonstrates its superior numerical performance through a comprehensive Monte Carlo study.
[Section 6](https://arxiv.org/html/2601.01871v1#S6 "6 Empirical illustration ‣ On lead-lag estimation of non-synchronously observed point processes") presents an empirical application that illustrates the effectiveness of our proposed estimator using real data.
[Section 7](https://arxiv.org/html/2601.01871v1#S7 "7 Concluding remarks ‣ On lead-lag estimation of non-synchronously observed point processes") concludes by summarizing our main contributions and discussing directions for future research.
The appendix contains mathematical proofs and additional implementation details.

##### Notation

The cardinality of a finite set SS is denoted by |S||S|.
Leb\operatorname{Leb} denotes the Lebesgue measure.
The Borel σ\sigma-algebra of a topological space SS is denoted by ℬ​(S)\mathcal{B}(S).
For a real-valued function ff defined on a set SS, we set ‖f‖∞=supx∈S|f​(x)|\|f\|\_{\infty}=\sup\_{x\in S}|f(x)|.
Also, we denote by arg​maxx∈S⁡f​(x)\operatorname\*{arg\,max}\_{x\in S}f(x) the set of maximizers of ff on SS.
For a random variable XX and p≥1p\geq 1, we set ‖X‖p:=(E⁡[|X|p])1/p\|X\|\_{p}:=(\operatorname{E}[|X|^{p}])^{1/p}.
The underlying probability space is denoted by (Ω,ℱ,P)(\Omega,\mathcal{F},\operatorname{P}).
We interpret 1/0=∞1/0=\infty by convention.

## 2 The Dobrev–Schaumburg method

Suppose that we have tick data for two financial assets, with timestamps given by 0≤t11<⋯<tn11≤T0\leq t^{1}\_{1}<\cdots<t^{1}\_{n\_{1}}\leq T and 0≤t12<⋯<tn22≤T0\leq t^{2}\_{1}<\cdots<t^{2}\_{n\_{2}}\leq T.
Throughout the paper, we assume that T≥1T\geq 1 is an integer and timestamps are expressed in seconds when working with real data.; hence we may regard TT as a large integer. dobrev2017high proposed measuring the lead-lag relationship between two assets using the following procedure.

First, divide the observation interval [0,T][0,T] into equi-spaced time buckets Ikh:=(k​h,(k+1)​h]I^{h}\_{k}:=(kh,(k+1)h], k=0,1,…,T/h−1k=0,1,\dots,T/h-1, where h>0h>0 is chosen so that h−1∈ℕh^{-1}\in\mathbb{N}.
We interpret a situation where an event for asset 2 occurs with a lag ℓ∈ℤ\ell\in\mathbb{Z} after an event for asset 1 as the existence of timestamps ti1,tj2t^{1}\_{i},t^{2}\_{j} and a bucket index k∈{|ℓ|,|ℓ|+1,…,T/h−1−|ℓ|}k\in\{|\ell|,|\ell|+1,\dots,T/h-1-|\ell|\} such that ti1∈Ikht^{1}\_{i}\in I^{h}\_{k} and tj2∈Ik+ℓht^{2}\_{j}\in I^{h}\_{k+\ell}.
By calculating the number of such bucket indices, we obtain a measure of the lead-lag effect of asset 1 on asset 2 with lag ℓ\ell.
Based on this idea, dobrev2017high introduced the *raw cross-market activity* at offset ℓ\ell as

|  |  |  |
| --- | --- | --- |
|  | 𝒳hraw​(ℓ):=∑k=|ℓ|T/h−1−|ℓ|1{∃ti1∈Ikh,∃tj2∈Ik+ℓh}.\mathcal{X}^{\mathrm{raw}}\_{h}(\ell):=\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{\exists t^{1}\_{i}\in I^{h}\_{k},\,\exists t^{2}\_{j}\in I^{h}\_{k+\ell}\}}. |  |

To adjust the degree of freedom, they also defined the *relative cross-market activity* as

|  |  |  |
| --- | --- | --- |
|  | 𝒳hrel​(ℓ):=𝒳hraw​(ℓ)min⁡{∑k=|ℓ|T/h−1−|ℓ|1{∃ti1∈Ikh},∑k=|ℓ|T/h−1−|ℓ|1{∃ti+ℓ2∈Ikh}}.\mathcal{X}^{\mathrm{rel}}\_{h}(\ell):=\frac{\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)}{\min\left\{\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{\exists t^{1}\_{i}\in I^{h}\_{k}\}},\ \sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{\exists t^{2}\_{i+\ell}\in I^{h}\_{k}\}}\right\}}. |  |

Computing 𝒳hraw​(ℓ)\mathcal{X}^{\mathrm{raw}}\_{h}(\ell) and 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell) requires choosing a value of hh.
In [dobrev2017high], hh is set to 1 millisecond, which is chosen in an ad-hoc manner by considering the time granularity of the data.
Here, 1 millisecond is the minimum time unit available in their dataset for the S&P 500 cash market.

By definition, the larger value of 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell) indicates a stronger lead-lag effect in which asset 2 follows asset 1 after a delay of ℓ​h\ell h.
Motivated by this, dobrev2017high proposed identifying the prevailing lead-lag time by locating the peak of the map ℓ↦𝒳hrel​(ℓ)\ell\mapsto\mathcal{X}^{\mathrm{rel}}\_{h}(\ell).
Specifically, given a search grid
𝒢h\mathcal{G}\_{h}, the lead-lag time is estimated by

|  |  |  |
| --- | --- | --- |
|  | θ^hD​S=ℓ^​h,where ​ℓ^∈arg​maxℓ∈𝒢h⁡𝒳hrel​(ℓ).\hat{\theta}\_{h}^{DS}=\hat{\ell}h,\quad\text{where }\hat{\ell}\in\operatorname\*{arg\,max}\_{\ell\in\mathcal{G}\_{h}}\mathcal{X}^{\mathrm{rel}}\_{h}(\ell). |  |

We refer to θ^hD​S\hat{\theta}\_{h}^{DS} as the *DS estimator*.
In what follows, we assume the true lead-lag time lies within the interval (−r,r)(-r,r) for some known positive constant rr, and define 𝒢h:={ℓ∈ℤ:|ℓ​h|≤r}\mathcal{G}\_{h}:=\{\ell\in\mathbb{Z}:|\ell h|\leq r\}.

As mentioned in the introduction, several empirical studies have reported that the DS estimator yields stable and interpretable estimates of lead-lag time.
However, there are cases where the estimator performs poorly, particularly when the dataset contains relatively few observations.
[Fig. 1](https://arxiv.org/html/2601.01871v1#S2.F1 "In 2 The Dobrev–Schaumburg method ‣ On lead-lag estimation of non-synchronously observed point processes") illustrates this issue, showing the relative cross-market activity measure computed from best-quote updates on two U.S. stock exchanges, NASDAQ and BATS, for the MNST stock on August 12, 2015.
In this example, the values of the cross-market activity measure fluctuate heavily, making it difficult to identify the peak reliability.
Yet, due to the “model-free” nature of the Dobrev–Schaumburg method, no statistical interpretation is provided for the origin of such instability.
One goal of this study is to establish a theoretical foundation for their approach and fill this gap.

![Refer to caption](pics/MNST_with_CPCF.png)


Figure 1: Contrast functions: DS vs ours. MNST, NASDAQ vs BATS (quote, Aug. 12, 2015). The cross-market activity measure 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell) is indicated by the red line, while the kernel density estimator gh^​(u)g\_{\hat{h}}(u) with the Lepski-selected bandwith (see [Section 4](https://arxiv.org/html/2601.01871v1#S4 "4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")) is indicated by the blue line. The unit of the horizontal axis is seconds.

## 3 Proposed framework

To clarify the statistical meaning of the Dobrev–Schaumburg method, we model the observed timestamps (ti1)i=1n1(t^{1}\_{i})\_{i=1}^{n\_{1}} and (tj2)j=1n2(t^{2}\_{j})\_{j=1}^{n\_{2}} as realizations of a bivariate point process on the real line.
Specifically, for each a=1,2a=1,2, we consider the timestamps (tia)(t^{a}\_{i}) to be a result of observing a point process NaN\_{a} on ℝ\mathbb{R} over the interval [0,T][0,T].
That is, Na​(A)=|{i:tia∈A}|N\_{a}(A)=|\{i:t^{a}\_{i}\in A\}| for a Borel set A⊂[0,T]A\subset[0,T].
Here and below, we mainly follow the mathematical formulation of point processes described in [daley2006introduction, daley2007introduction] and refer to these monographs for unexplained concepts and notation (see also [shiotani2024statistical, Section 2.2] for a summary).
With this formulation, we can rewrite 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell) as

|  |  |  |
| --- | --- | --- |
|  | 𝒳hrel​(ℓ)=∑k=|ℓ|T/h−1−|ℓ|1{N1​(Ikh)>0,N2​(Ik+ℓh)>0}min⁡{∑k=|ℓ|T/h−1−|ℓ|1{N1​(Ikh)>0},∑k=|ℓ|T/h−1−|ℓ|1{N2​(Ik+ℓh)>0}}.\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)=\frac{\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{1}(I\_{k}^{h})>0,\ N\_{2}(I\_{k+\ell}^{h})>0\}}}{\min\left\{\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{1}(I\_{k}^{h})>0\}},\ \sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{2}(I\_{k+\ell}^{h})>0\}}\right\}}. |  |

Using this expression, we can relate 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell) to the *cross-pair correlation function (CPCF)* of NN.

To state the theoretical result formally, we introduce several assumptions and notation.
We assume that N=(N1,N2)N=(N\_{1},N\_{2}) is a simple stationary bivariate point process on ℝ\mathbb{R} with intensities λ1,λ2∈(0,∞)\lambda\_{1},\lambda\_{2}\in(0,\infty).
Note that we use the term “intensity” in the same sense as in [daley2006introduction] (see page 47 ibidem).
By [daley2006introduction, Proposition 3.3.IV], we have λa=E⁡[Na​((0,1])]\lambda\_{a}=\operatorname{E}[N\_{a}((0,1])] for a=1,2a=1,2.
We also assume that there exists a locally integrable function λ12:ℝ→[0,∞]\lambda\_{12}:\mathbb{R}\to[0,\infty] such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[N1​(A1)​N2​(A2)]=∫A1×A2λ12​(y−x)​𝑑x​𝑑y\operatorname{E}[N\_{1}(A\_{1})N\_{2}(A\_{2})]=\int\_{A\_{1}\times A\_{2}}\lambda\_{12}(y-x)dxdy |  | (3.1) |

for any bounded A1,A2∈ℬ​(ℝ)A\_{1},A\_{2}\in\mathcal{B}(\mathbb{R}).
We refer to λ12\lambda\_{12} as the *cross-intensity function*222In neuroscience, the term “cross-intensity function” usually refers to the functions λ12​(u)/λ1\lambda\_{12}(u)/\lambda\_{1} or λ12​(u)/λ2\lambda\_{12}(u)/\lambda\_{2} (see e.g. [bryant1973correlations]).
We follow the terminology used in spatial statistics [hessellund2022semiparametric, hessellund2022second].
In the terminology of point process theory, λ12\lambda\_{12} is a density of the reduced cross-moment measure of NN (cf. [daley2006introduction, Section 8.3]). of NN.
The CPCF of NN is the function g:ℝ→[0,∞]g:\mathbb{R}\to[0,\infty] defined as

|  |  |  |
| --- | --- | --- |
|  | g​(u)=λ12​(u)λ1​λ2(u∈ℝ).g(u)=\frac{\lambda\_{12}(u)}{\lambda\_{1}\lambda\_{2}}\qquad(u\in\mathbb{R}). |  |

The cross-intensity function can be related to the cross-covariance function between the infinitesimal increments of N1N\_{1} and N2N\_{2} in the following sense (cf. ([A.11](https://arxiv.org/html/2601.01871v1#A1.E11 "Equation A.11 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"))):

|  |  |  |
| --- | --- | --- |
|  | ν12​(u):=limh↓0Cov⁡(N1​(0,h],N2​(u,u+h])h2=λ12​(u)−λ1​λ2a.e. ​u.\nu\_{12}(u):=\lim\_{h\downarrow 0}\frac{\operatorname{Cov}(N\_{1}(0,h],N\_{2}(u,u+h])}{h^{2}}=\lambda\_{12}(u)-\lambda\_{1}\lambda\_{2}\quad\text{a.e. }u. |  |

The function ν12\nu\_{12} is called the *covariance density* of NN.
In this sense, g​(u)g(u) measures the cross-covariation between N1​(⋅)N\_{1}(\cdot) and N2(⋅+u)N\_{2}(\cdot+u).

We also need the notion of α\alpha-mixing (or strong mixing) for point processes.
Recall that the α\alpha-mixing coefficient of two sub-σ\sigma-algebras 𝒢\mathcal{G} and ℋ\mathcal{H} of ℱ\mathcal{F} is defined as

|  |  |  |
| --- | --- | --- |
|  | α(𝒢,ℋ):=sup{|P(C∩D)−P(C)P(D)|:C∈𝒢,D∈ℋ}.\alpha(\mathcal{G},\mathcal{H}):=\sup\{|\operatorname{P}(C\cap D)-\operatorname{P}(C)\operatorname{P}(D)|:C\in\mathcal{G},D\in\mathcal{H}\}. |  |

For E∈ℬ​(ℝ)E\in\mathcal{B}(\mathbb{R}), we denote by N∩E=(Ni∩E)i=12N\cap E=(N\_{i}\cap E)\_{i=1}^{2} the restriction of NN to EE, i.e. (Ni∩E)​(A)=Ni​(A∩E)(N\_{i}\cap E)(A)=N\_{i}(A\cap E) for i=1,2i=1,2 and A∈ℬ​(ℝ)A\in\mathcal{B}(\mathbb{R}).
Also, E⊕r:={x∈ℝ:|y−x|<r​ for some ​y∈E}E\oplus r:=\{x\in\mathbb{R}:|y-x|<r\text{ for some }y\in E\} denotes the rr-enlargement of EE.
Moreover, given a bivariate point process M=(M1,M2)M=(M\_{1},M\_{2}) on ℝ\mathbb{R}, σ​(M)\sigma(M) denotes the σ\sigma-algebra generated by ⋃i=12{Mi​(A):A∈ℬ​(ℝ)}\bigcup\_{i=1}^{2}\{M\_{i}(A):A\in\mathcal{B}(\mathbb{R})\}.
As α\alpha-mixing coefficients of NN, we adopt the following definition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αc1,c2N(m;r)=sup{α​(σ​(N∩E1),σ​(N∩E2)):E1=⋃j∈J1Ij⊕r,E2=⋃j∈J2Ij⊕r,|J1|≤c1,|J2|≤c2,d(J1,J2)≥m,J1,J2⊂ℤ},m,c1,c2,r≥0,\begin{split}\alpha\_{c\_{1},c\_{2}}^{N}(m;r)=\sup\Bigl\{&\alpha(\sigma(N\cap E\_{1}),\sigma(N\cap E\_{2})):E\_{1}=\bigcup\_{j\in J\_{1}}I\_{j}\oplus r,\,E\_{2}=\bigcup\_{j\in J\_{2}}I\_{j}\oplus r,\\ &|J\_{1}|\leq c\_{1},\,|J\_{2}|\leq c\_{2},\,d(J\_{1},J\_{2})\geq m,\,J\_{1},J\_{2}\subset\mathbb{Z}\Bigr\},\quad m,c\_{1},c\_{2},r\geq 0,\end{split} |  | (3.2) |

where Ij:=Ij1=(j,j+1]I\_{j}:=I\_{j}^{1}=(j,j+1] and d(J1,J2):=inf{|j1−j2|:j1∈J1,j2∈J2}d(J\_{1},J\_{2}):=\inf\{|j\_{1}-j\_{2}|:j\_{1}\in J\_{1},\,j\_{2}\in J\_{2}\}.
This definition is a minor variant of the one used in [shiotani2024statistical], where they use (j−12,j+12](j-\frac{1}{2},j+\frac{1}{2}] instead of IjI\_{j}.
This difference is inessential, and we just adopt the present definition to (slightly) simplify our technical arguments.

###### Remark 3.1 (Mixing coefficients as a continuous-time process).

Since NN can be regarded as a stochastic process indexed by ℝ\mathbb{R}, we can also define the α\alpha-mixing coefficients in this sense [brillinger1976estimation]:

|  |  |  |
| --- | --- | --- |
|  | αprocN​(τ):=supt∈ℝα​(σ​(N∩(−∞,t)),σ​(N∩(t+τ,∞))),τ≥0.\alpha^{N}\_{\text{proc}}(\tau):=\sup\_{t\in\mathbb{R}}\alpha\left(\sigma(N\cap(-\infty,t)),\,\sigma(N\cap(t+\tau,\infty))\right),\qquad\tau\geq 0. |  |

Our definition is weaker than this version in the sense that we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | αc1,c2N​(m;r)≤αprocN​(m−2​r)\alpha^{N}\_{c\_{1},c\_{2}}(m;r)\leq\alpha^{N}\_{\text{proc}}(m-2r) |  | (3.3) |

for all c1,c2,r≥0c\_{1},c\_{2},r\geq 0 and m≥2​rm\geq 2r.
For the case of point processes, it is important to work with the weaker version because it is sometimes difficult to bound the left hand side of ([3.3](https://arxiv.org/html/2601.01871v1#S3.E3 "Equation 3.3 ‣ Remark 3.1 (Mixing coefficients as a continuous-time process). ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) uniformly in c1,c2≥0c\_{1},c\_{2}\geq 0; see [poinas2019mixing, Proposition 2.8] and [shiotani2024statistical, Lemma 10.13] for example.

We impose the following regularity conditions on NN.

1. [A1]

   (i) For every p≥1p\geq 1, there exists a constant Bp>0B\_{p}>0 such that maxi=1,2⁡λi−1​‖Ni​((0,1])‖p≤Bp\max\_{i=1,2}\lambda\_{i}^{-1}\|N\_{i}((0,1])\|\_{p}\leq B\_{p}.

   (ii) For any p,q≥1p,q\geq 1, there exists a constant Bp,q>0B\_{p,q}>0 such that
   αp,pN​(m;r1)≤Bp,q​m−q\alpha\_{p,p}^{N}(m;r\_{1})\leq B\_{p,q}m^{-q}
   for all m∈ℕm\in\mathbb{N}, where r1:=r+1r\_{1}:=r+1.

This assumption is fairly reasonable in the literature and is satisfied by many standard point process models such as the Hawkes process and Neyman-Scott process as long as their kernels satisfy some regularity conditions; see [Section 5.1](https://arxiv.org/html/2601.01871v1#S5.SS1 "5.1 Models ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes") for details.

Under [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and additional technical assumptions, we have the following asymptotic representation of Dobrev–Schaumburg’s cross-market activity measure:

###### Proposition 3.1.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Assume also that gg is bounded and

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxℓ∈𝒢h⁡E⁡[N1​(I0h)​{N1​(I0h)−1}​N2​(Iℓh)]=o​(h1+ϖ),maxℓ∈𝒢h⁡E⁡[N1​(I0h)​N2​(Iℓh)​{N2​(Iℓh)−1}]=o​(h1+ϖ)\begin{split}\max\_{\ell\in\mathcal{G}\_{h}}\operatorname{E}[N\_{1}(I\_{0}^{h})\{N\_{1}(I\_{0}^{h})-1\}N\_{2}(I\_{\ell}^{h})]&=o(h^{1+\varpi}),\\ \max\_{\ell\in\mathcal{G}\_{h}}\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})\{N\_{2}(I\_{\ell}^{h})-1\}]&=o(h^{1+\varpi})\end{split} |  | (3.4) |

as h→0h\to 0 for ϖ=1\varpi=1.
Moreover, assume h=hT≍T−γh=h\_{T}\asymp T^{-\gamma} as T→∞T\to\infty for some 0<γ<10<\gamma<1.
Then

|  |  |  |
| --- | --- | --- |
|  | maxℓ∈𝒢h⁡|𝒳hrel​(ℓ)h−(λ1∨λ2)​∫ℝ1h​Ktri​(u−ℓ​hh)​g​(u)​𝑑u|→p0,\displaystyle\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)}{h}-(\lambda\_{1}\vee\lambda\_{2})\int\_{\mathbb{R}}\frac{1}{h}K^{\mathrm{tri}}\left(\frac{u-\ell h}{h}\right)g(u)du\right|\to^{p}0, |  |

where Ktri​(x)=(1−|x|)​1[−1,1]​(x)K^{\mathrm{tri}}(x)=(1-|x|)1\_{[-1,1]}(x).

###### Remark 3.2 (On condition ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"))).

The quantities on the left hand sides of ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) can be related to the factorial moment measures of orders (2,1) and (1,2) of NN (see Section 2.3 of [shiotani2024statistical] for the definition).
In particular, ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) holds for ϖ=1\varpi=1 if these measures have bounded densities with respect to the Lebesgue measure.
Since each factorial moment measure can be expressed as a sum of factorial cumulant measures through [shiotani2024statistical, Eq.(2.5)] (see also [brillinger1972spectral, Eq.(3.21)]), its density can be computed for the Hawkes process via [jovanovic2015cumulants, Eq.(39)] and the Neyman-Scott process via [shiotani2024statistical, Eq.(5.2)], respectively; hence, one can in principle verify ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) under appropriate assumptions on their kernels.
We do not pursue this point further because this condition is unnecessary for the theoretical development of our new estimator proposed in the next section.

Under the assumptions of [Proposition 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), we have maxℓ∈𝒢h⁡|𝒳hrel​(ℓ)/h−(λ1∨λ2)​g​(ℓ​h)|→p0\max\_{\ell\in\mathcal{G}\_{h}}|\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)/h-(\lambda\_{1}\vee\lambda\_{2})g(\ell h)|\to^{p}0 if gg is continuous.
Hence, the cross-market activity measure can be interpreted as an estimator for the CPCF up to a multiplicative constant.
Moreover, if gg has a unique maximizer θ∗\theta^{\*} in (−r,r)(-r,r), the above result implies that θ^hD​S\hat{\theta}\_{h}^{DS} is a consistent estimator of θ∗\theta^{\*} as T→∞T\to\infty.
For further understanding of theoretical properties of θ^hD​S\hat{\theta}\_{h}^{DS}, we study its rate of convergence.
For this purpose, we introduce the following assumption on gg:

1. [A2]

   There exist constants θ∗∈(−r,r)\theta^{\*}\in(-r,r), α∈(0,1)∪(1,∞)\alpha\in(0,1)\cup(1,\infty), b>1b>1 and δ>0\delta>0 such that the following conditions hold:

   1. (i)

      If α>1\alpha>1, supu∈ℝg​(u)≤b\sup\_{u\in\mathbb{R}}g(u)\leq b and

      |  |  |  |
      | --- | --- | --- |
      |  | min⁡{sup0<u−θ∗<δg​(θ∗)−g​(u)|u−θ∗|α−1,sup0<θ∗−u<δg​(θ∗)−g​(u)|u−θ∗|α−1}≤b\min\left\{\sup\_{0<u-\theta^{\*}<\delta}\frac{g(\theta^{\*})-g(u)}{|u-\theta^{\*}|^{\alpha-1}},\sup\_{0<\theta^{\*}-u<\delta}\frac{g(\theta^{\*})-g(u)}{|u-\theta^{\*}|^{\alpha-1}}\right\}\leq b |  |

      and

      |  |  |  |
      | --- | --- | --- |
      |  | inf0<|u−θ∗|<δg​(θ∗)−g​(u)|u−θ∗|α−1≥1b\inf\_{0<|u-\theta^{\*}|<\delta}\frac{g(\theta^{\*})-g(u)}{|u-\theta^{\*}|^{\alpha-1}}\geq\frac{1}{b} |  |

      and

      |  |  |  |
      | --- | --- | --- |
      |  | sup|u−θ∗|≥δg​(u)≤g​(θ∗)−1b.\sup\_{|u-\theta^{\*}|\geq\delta}g(u)\leq g(\theta^{\*})-\frac{1}{b}. |  |
   2. (ii)

      If α<1\alpha<1,

      |  |  |  |
      | --- | --- | --- |
      |  | max⁡{inf0<u−θ∗<δg​(u)|u−θ∗|α−1,inf−δ<u−θ∗<0g​(u)|u−θ∗|α−1}≥1b.\max\left\{\inf\_{0<u-\theta^{\*}<\delta}\frac{g(u)}{|u-\theta^{\*}|^{\alpha-1}},\inf\_{-\delta<u-\theta^{\*}<0}\frac{g(u)}{|u-\theta^{\*}|^{\alpha-1}}\right\}\geq\frac{1}{b}. |  |

      Moreover, there exist a constant α<α0≤1\alpha<\alpha\_{0}\leq 1 and a measurable function g0:ℝ→[0,∞]g\_{0}:\mathbb{R}\to[0,\infty] such that ‖g0‖L1/(1−α0)​([−r1,r1])≤b\|g\_{0}\|\_{L^{1/(1-\alpha\_{0})}([-r\_{1},r\_{1}])}\leq b and

      |  |  |  |
      | --- | --- | --- |
      |  | g​(u)≤b​(g0​(u)+|u−θ∗|α−1)for all ​u∈[−r1,r1].g(u)\leq b\left(g\_{0}(u)+|u-\theta^{\*}|^{\alpha-1}\right)\quad\text{for all }u\in[-r\_{1},r\_{1}]. |  |

Under [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](i)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i1 "Item [A2](i) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), gg is bounded and θ∗\theta^{\*} is the unique maximizer of gg.
By contrast, under [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](ii)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i2 "Item [A2](ii) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), gg diverges at θ∗\theta^{\*} and is therefore unbounded.
We allow gg to have poles other than θ∗\theta^{\*} through an auxiliary function g0g\_{0}; however, the condition ‖g0‖L1/(1−α0)​([−r1,r1])<∞\|g\_{0}\|\_{L^{1/(1-\alpha\_{0})}([-r\_{1},r\_{1}])}<\infty ensures that θ∗\theta^{\*} remains the “sharpest” peak location of gg.
We call θ∗\theta^{\*} the *lead-lag (time) parameter*.
We allow gg to be unbounded motivated by several empirical observations: (i) Dobrev–Schaumburg’s cross-market activity measure often exhibits extremely sharp peaks (see e.g. [dobrev2017high, Fig. 7]); (ii) shiotani2024statistical found that their semiparametric model fits Japanese stock market data better when the CPCF is unbounded; (iii) rambaldi2018detection report that intensity burst occurrences across different foreign exchange rates exhibit lead-lag relationships.

###### Remark 3.3 (Relation to mode estimation).

Our formulation of the lead-lag parameter estimation problem is naturally connected to mode estimation for a probability density function, once the CPCF is replaced by the density.
[[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") is motivated by this observation.
In fact, wegman1971note classifies the problem of mode estimation for unimodal distributions into three types, labeling cases with bounded density as Type I, cases with unbounded density as Type II, and cases without density as Type III.
In this classification, [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](i)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i1 "Item [A2](i) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") corresponds to Type I, and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](ii)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i2 "Item [A2](ii) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") corresponds to Type II.
For the purpose of analyzing the convergence rate, we assume that the CPCF behaves like a power function |u−θ∗|α−1|u-\theta^{\*}|^{\alpha-1} in a neighborhood of θ∗\theta^{\*}.
When α>1\alpha>1, this assumptions is analogous to the conditions studied in [arias2022estimation] (see Section 1.1 ibidem).
When α<1\alpha<1, it corresponds to the analogue of condition [H-III] in [bercu2002estimation].
Note that the case α=1\alpha=1 is excluded simply because the power function |u−θ∗|α−1|u-\theta^{\*}|^{\alpha-1} becomes constant in that case.

Under [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), we set

|  |  |  |
| --- | --- | --- |
|  | βα:=α∨(2​α−1)={αif ​α<1,2​α−1if ​α>1.\beta\_{\alpha}:=\alpha\vee(2\alpha-1)=\begin{cases}\alpha&\text{if }\alpha<1,\\ 2\alpha-1&\text{if }\alpha>1.\end{cases} |  |

###### Theorem 3.1.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and h=hT≍T−γh=h\_{T}\asymp T^{-\gamma} as T→∞T\to\infty for some 0<γ<1/βα0<\gamma<1/\beta\_{\alpha}.
Moreover, assume ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) for ϖ=α\varpi=\alpha.
Then, θ^hD​S=θ∗+Op​(h)\hat{\theta}\_{h}^{DS}=\theta^{\*}+O\_{p}(h) as T→∞T\to\infty.

Since θ^hD​S\hat{\theta}\_{h}^{DS} is, by construction, an integer multiple of hh, [Theorem 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") implies that its convergence rate is exactly of order O​(h)O(h).
In particular, the accuracy of θ^hD​S\hat{\theta}\_{h}^{DS} improves as hh becomes smaller.
Given the definition of 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell), however, it is meaningless to choose hh smaller than the minimum time unit in the data.
In this sense, it is reasonable that dobrev2017high set hh equal to the minimum time resolution.

Nevertheless, [Theorem 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") also imposes a constraint on the order of hh, requiring that hh converge to 0 more slowly than T−1/βαT^{-1/\beta\_{\alpha}}.
Moreover, this constraint is not a technical artifact of the proof; it is essential, because we show that T−1/βαT^{-1/\beta\_{\alpha}} gives a minimax lower bound on the convergence rate of any estimator of θ∗\theta^{\*} under the assumptions of [Theorem 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), at least when α<2\alpha<2 (see [4.2](https://arxiv.org/html/2601.01871v1#S4.Thmrmk2 "Remark 4.2. ‣ 4.2 Minimax lower bound for the convergence rate ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")).
Therefore, it is theoretically impossible for the conclusion of [Theorem 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") to hold when h≪T−1/βαh\ll T^{-1/\beta\_{\alpha}}.

Note that na/T→λa>0n\_{a}/T\to\lambda\_{a}>0 as T→∞T\to\infty a.s. for each a=1,2a=1,2 under [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Hence, for θ^hD​S\hat{\theta}\_{h}^{DS} to perform properly, hh must be chosen based on n1,n2n\_{1},n\_{2} (the sample sizes) and α\alpha (the sharpness of the CPCF peak).
Specifically, hh should be taken larger when n1n\_{1} and n2n\_{2} are smaller and/or when α\alpha is larger.
This provides one explanation for the poor performance of the Dobrev–Schaumburg method in the example shown in [Fig. 1](https://arxiv.org/html/2601.01871v1#S2.F1 "In 2 The Dobrev–Schaumburg method ‣ On lead-lag estimation of non-synchronously observed point processes").
That is, in that dataset, setting h=1​μ​sh=1~\mu\text{s} was likely far too small, given the relatively small numbers of observations (n1,n2)=(28048,11287)(n\_{1},n\_{2})=(28048,11287).

These observations indicate that the choice of hh plays a crucial role in the implementation of the DS estimator.
However, the DS estimator should be interpreted as an estimator of an interval containing the lead-lag parameter, rather than the parameter itself, which makes data-driven selection of hh difficult.
For these reasons, in the next section, we propose a new lead-lag time estimator based on kernel density estimation and demonstrate that it can overcome this issue.

## 4 New estimator

[Proposition 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") suggests that 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell) would be asymptotically equivalent to a discretized version of a kernel density estimator for gg based on the triangular kernel.
This naturally motivates us to consider kernel density estimators for gg directly.

Formally, let K:ℝ→ℝK:\mathbb{R}\to\mathbb{R} be a kernel function and h=hT>0h=h\_{T}>0 a bandwidth parameter such that h→0h\to 0 as T→∞T\to\infty.
We then consider the following statistic:

|  |  |  |
| --- | --- | --- |
|  | g^h​(u)=Tn1​n2​∫(0,T]2Kh​(y−x−u)​N1​(d​x)​N2​(d​y),u∈ℝ,\hat{g}\_{h}(u)=\frac{T}{n\_{1}n\_{2}}\int\_{(0,T]^{2}}K\_{h}(y-x-u)N\_{1}(dx)N\_{2}(dy),\qquad u\in\mathbb{R}, |  |

where Kh​(t)=h−1​K​(t/h)K\_{h}(t)=h^{-1}K(t/h) for t∈ℝt\in\mathbb{R}.
We estimate θ∗\theta^{\*} by taking a maximizer of g^h\hat{g}\_{h}.
That is, we define a random variable θ^h\hat{\theta}\_{h} satisfying

|  |  |  |
| --- | --- | --- |
|  | θ^h∈arg​maxu∈[−r,r]⁡g^h​(u).\hat{\theta}\_{h}\in\operatorname\*{arg\,max}\_{u\in[-r,r]}\hat{g}\_{h}(u). |  |

The practical procedure for computing θ^h\hat{\theta}\_{h} and its computational complexity are described in Appendix [B](https://arxiv.org/html/2601.01871v1#A2 "Appendix B Implementation and computational complexity ‣ On lead-lag estimation of non-synchronously observed point processes").

When the uniform kernel is used as the kernel function, g^h\hat{g}\_{h} is essentially equivalent to the so-called cross-correlation histogram in neuroscience and has long been applied to investigate relationships between neuronal spikes (see e.g. [bryant1973correlations]).
This line of work has motivated statisticians to investigate the theoretical properties of g^h\hat{g}\_{h} [cox1972multivariate, brillinger1975statistical, brillinger1976estimation, ellis1991density].
Nevertheless, to the best of our knowledge, no prior research has addressed the case where gg is unbounded, nor the asymptotic behavior of the maximizer of g^h\hat{g}\_{h}.

We impose the following assumption on the kernel.

1. [K]

   KK is non-negative, continuous at 0, of bounded variation and supported on [−1,1][-1,1] such that K​(0)>0K(0)>0, ∫−∞∞K​(t)​𝑑t=1\int\_{-\infty}^{\infty}K(t)dt=1 and arg​maxu∈[−r,r]⁡g^h​(u)≠∅\operatorname\*{arg\,max}\_{u\in[-r,r]}\hat{g}\_{h}(u)\neq\emptyset a.s.

Assumption [[K]](https://arxiv.org/html/2601.01871v1#S4.I1.i1 "Item [K] ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") holds for the uniform kernel K=12​1[−1,1]K=\frac{1}{2}1\_{[-1,1]} and the triangular kernel K=KtriK=K^{\mathrm{tri}}, for example.

###### Theorem 4.1.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[K]](https://arxiv.org/html/2601.01871v1#S4.I1.i1 "Item [K] ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").
Let η>0\eta>0 be a constant.
Then, there exist constants A>1A>1 and 0<h0<10<h\_{0}<1 depending only on α,α0,δ,b\alpha,\alpha\_{0},\delta,b and KK such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | P⁡(|θ^h−θ∗|>A​h)≤CT​hβα+ε\operatorname{P}(|\hat{\theta}\_{h}-\theta^{\*}|>Ah)\leq\frac{C}{\sqrt{Th^{\beta\_{\alpha}+\varepsilon}}} |  | (4.1) |

for all h≤h0∧T−ηh\leq h\_{0}\wedge T^{-\eta} and ε>0\varepsilon>0, where C>0C>0 is a constant depending only on r,α,δ,br,\alpha,\delta,b, (Bp)p≥1(B\_{p})\_{p\geq 1}, (Bp,q)p,q≥1(B\_{p,q})\_{p,q\geq 1}, ε,η\varepsilon,\eta and ‖K‖∞\|K\|\_{\infty}.
In particular, θ^h=θ∗+Op​(h)\hat{\theta}\_{h}=\theta^{\*}+O\_{p}(h) as T→∞T\to\infty if h=hT≍T−γh=h\_{T}\asymp T^{-\gamma} for some 0<γ<1/βα0<\gamma<1/\beta\_{\alpha}.

By [Theorem 4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes"), θ^h\hat{\theta}\_{h} estimates θ∗\theta^{\*} at the same convergence rate as θ^hD​S\hat{\theta}\_{h}^{DS}.
Moreover, unlike the DS estimator, we do not require assumption ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")).
In particular, by selecting the bandwidth appropriately, our estimator nearly attains the minimax optimal convergence rate T−1/βαT^{-1/\beta\_{\alpha}} (see [Theorem 4.3](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Minimax lower bound for the convergence rate ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")).
The next subsection discusses methods for selecting the bandwidth in a data-driven way.

###### Remark 4.1 (Relation to kernel mode estimation).

In light of [3.3](https://arxiv.org/html/2601.01871v1#S3.Thmrmk3 "Remark 3.3 (Relation to mode estimation). ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), our estimator is closely related to a mode estimator obtained by maximizing a kernel density estimator.
Following [chacon2020modal], we refer to this type of estimator as the kernel mode estimator.

For i.i.d. data with density ff and unique population mode θ∗\theta^{\*},
parzen1962estimation established the asymptotic normality of the kernel mode estimator when ff is of class C2C^{2} and f′′​(θ∗)<0f^{\prime\prime}(\theta^{\*})<0. This setting is a particular case of [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") with α=3\alpha=3.
Notably, with a suitable bandwidth choice, the kernel mode estimator nearly achieves the convergence rate n−1/5n^{-1/5}, where nn is the sample size. Since β3=5\beta\_{3}=5, our estimator enjoys an analogous property.
hasminskii1979lower proved that the rate n−1/5n^{-1/5} is minimax optimal in this setting, but it can be improved under additional smoothness assumptions on the density and the kernel; see e.g. [eddy1980optimum, klemela2005adaptive, vieu1996note].

Without smoothness assumptions on the density, abraham2003simple and herrmann2004rates obtained convergence rates for the kernel mode estimator and its variant under conditions analogous to [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](i)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i1 "Item [A2](i) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
In this scenario, arias2022estimation established the minimax optimal rate and developed an adaptive estimation procedure.
The convergence rate in this setting is n−1/(2​α−1)n^{-1/(2\alpha-1)}, which again analogous to ours.
To the best of our knowledge, apart from the work of [bercu2002estimation], no results exist for mode estimation under assumptions analogous to [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](ii)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i2 "Item [A2](ii) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
bercu2002estimation investigated a histogram-type estimator, which can be viewed as a discretized kernel mode estimator, and showed that its convergence rate can be made arbitrarily close to n−1/αn^{-1/\alpha} by selecting the bin width appropriately.
This behavior is also analogous to that of our estimator.

Finally, to our knowledge, the asymptotic distribution of the kernel mode estimator remains unknown for non-smooth densities.
We conjecture that it may be non-Gaussian when α<3/2\alpha<3/2, drawing a parallel to location parameter estimation in the presence of density singularities (cf. [ibragimov2013statistical, Chapter VI]).

### 4.1 Bandwidth selection by Lepski’s method

In the classical setting of i.i.d. observations and kernel density estimation, bandwidth selection is typically based on minimizing the mean integrated squared error (MISE) of the kernel estimator; see, for example, [tsybakov2008nonparametric, Chapter 1].
In kernel estimation of moment density functions for point processes, analogous MISE-type criteria are also standard [guan2007least, jalilian2018fast].

However, for our purposes, a global loss criterion such as MISE is not entirely satisfactory, because the object of interest is not the function gg itself but the location θ∗\theta^{\ast} of its peak.
Intuitively, a global criterion aims to fit the entire curve, including regions where gg is only moderately large or small, whereas the estimation error of θ∗\theta^{\ast} may be governed almost exclusively by the local behaviour of gg in a small neighbourhood of the peak, which may even be singular under condition [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii).
A closely related issue has been recognized in the literature on nonparametric modal regression with i.i.d. observation; see, for example, Section 4.2 in chen2018modal.
Motivated by recent works in this context [chen2016nonparametric, zhou2019bandwidth], we investigate loss-minimization approaches based on cross-validation in Appendix [C](https://arxiv.org/html/2601.01871v1#A3 "Appendix C Bandwidth selection by cross-validation ‣ On lead-lag estimation of non-synchronously observed point processes").

Here, we instead adopt an adaptive estimation strategy based on a Lepski-type method, i.e., a pairwise comparison of estimators with different bandwidths.
Our approach was particularly inspired by klemela2005adaptive, who has developed a Lepski-type method for mode estimation from i.i.d. data.
For textbook treatments of Lepski’s method, we refer to [gine2016mathematical, Section 8.2].

Fix constants a>1a>1, γmax>0\gamma\_{\max}>0 and jmin∈ℕj\_{\min}\in\mathbb{N}.
We consider the following set as candidates for bandwidths:

|  |  |  |
| --- | --- | --- |
|  | ℋT:={a−j:jmin≤j≤⌈loga⁡(Tγmax)⌉,j∈ℤ}.\mathcal{H}\_{T}:=\{a^{-j}:j\_{\min}\leq j\leq\lceil\log\_{a}(T^{\gamma\_{\max}})\rceil,\,j\in\mathbb{Z}\}. |  |

For every h∈ℋTh\in\mathcal{H}\_{T}, set

|  |  |  |
| --- | --- | --- |
|  | ℳh:=arg​maxu∈[−r,r]⁡g^h​(u).\mathcal{M}\_{h}:=\operatorname\*{arg\,max}\_{u\in[-r,r]}\hat{g}\_{h}(u). |  |

We define

|  |  |  |
| --- | --- | --- |
|  | h^:=min⁡{h∈ℋT:d¯​(ℳh,ℳh′)≤AT​h′​ for all ​h′∈ℋT​ with ​h′≥h},\hat{h}:=\min\left\{h\in\mathcal{H}\_{T}:\bar{d}(\mathcal{M}\_{h},\mathcal{M}\_{h^{\prime}})\leq A\_{T}h^{\prime}\text{ for all }h^{\prime}\in\mathcal{H}\_{T}\text{ with }h^{\prime}\geq h\right\}, |  |

where ATA\_{T} is a positive constant and

|  |  |  |
| --- | --- | --- |
|  | d¯(ℳh,ℳh′):=sup{|x−y|:x∈ℳh,y∈ℳh′}.\bar{d}(\mathcal{M}\_{h},\mathcal{M}\_{h^{\prime}}):=\sup\left\{|x-y|:x\in\mathcal{M}\_{h},\,y\in\mathcal{M}\_{h^{\prime}}\right\}. |  |

###### Theorem 4.2.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[K]](https://arxiv.org/html/2601.01871v1#S4.I1.i1 "Item [K] ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").
Also, assume 1/βα≤γmax1/\beta\_{\alpha}\leq\gamma\_{\max}.
Further, assume AT→∞A\_{T}\to\infty and AT=o​(Tc)A\_{T}=o(T^{c}) for any c>0c>0 as T→∞T\to\infty.
Then, θ^h^=θ∗+Op​(T−γ)\hat{\theta}\_{\hat{h}}=\theta^{\*}+O\_{p}(T^{-\gamma}) for any 0<γ<1/βα0<\gamma<1/\beta\_{\alpha}.

[Theorem 4.2](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.1 Bandwidth selection by Lepski’s method ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") shows that the estimator θ^h^\hat{\theta}\_{\hat{h}} nearly achieves the optimal convergence rate T−1/βαT^{-1/\beta\_{\alpha}} without requiring the precise value of α\alpha.
This result is numerically validated in [Section 5.3](https://arxiv.org/html/2601.01871v1#S5.SS3 "5.3 Convergence rate and dependence on hyperparameters of Lepski’s method ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes"), where we also assess the robustness of the estimator with respect to the choice of the tuning parameter ATA\_{T}.
We will see that setting ATA\_{T} to a constant multiple of log⁡log⁡T\log\log T performs reasonably well.

### 4.2 Minimax lower bound for the convergence rate

In this subsection, we show that when [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") hold, T−1/βαT^{-1/\beta\_{\alpha}} gives a minimax lower bound for the convergence rate of any estimator for θ∗\theta^{\*}.
For this purpose, we consider a subclass of models for NN satisfying [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), which is specified as follows.
Given a probability density function gg on ℝ\mathbb{R}, we consider a probability measure Pg\operatorname{P}\_{g} on (Ω,ℱ)(\Omega,\mathcal{F}) having the following properties:

1. (i)

   N1=∑i=1∞δtiN\_{1}=\sum\_{i=1}^{\infty}\delta\_{t\_{i}} is a Poisson process on ℝ\mathbb{R} with unit intensity under Pg\operatorname{P}\_{g}.
2. (ii)

   N2N\_{2} is of the form N2=∑i=1∞δti+γiN\_{2}=\sum\_{i=1}^{\infty}\delta\_{t\_{i}+\gamma\_{i}}, where (γi)i=1∞(\gamma\_{i})\_{i=1}^{\infty} is a sequence of i.i.d. random variables independent of N1N\_{1} such that the law of γ1\gamma\_{1} has density gg under Pg\operatorname{P}\_{g}.

Under Pg\operatorname{P}\_{g}, NN is a bivariate Poisson process on ℝ\mathbb{R} in the sense of [daley2006introduction, Example 6.3(e)], where we have Q1=Q2=0Q\_{1}=Q\_{2}=0 and Q3​(d​x​d​y)=g​(y−x)​d​x​d​yQ\_{3}(dxdy)=g(y-x)dxdy in their notation.
In particular, under Pg\operatorname{P}\_{g}, the CPCF of NN is given by gg.

We write 𝒢​(θ∗,α,δ,b)\mathcal{G}(\theta^{\*},\alpha,\delta,b) for the class of probability density functions g:ℝ→[0,∞]g:\mathbb{R}\to[0,\infty] supported on [−1,1][-1,1] and satisfying the conditions of [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Note that if g∈𝒢​(θ∗,α,δ,b)g\in\mathcal{G}(\theta^{\*},\alpha,\delta,b), then NN satisfies [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") for some family of constants (Bp)p≥1(B\_{p})\_{p\geq 1}.
In fact, [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") is evident, while [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i) follows from the fact that both N1N\_{1} and N2N\_{2} are Poisson processes on ℝ\mathbb{R} with unit intensity.
Finally, since gg is supported on [−1,1][-1,1], αc1,c2N​(m;r1)=0\alpha\_{c\_{1},c\_{2}}^{N}(m;r\_{1})=0 for m≥m0m\geq m\_{0}, where m0m\_{0} depends only on rr. Hence, [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) is also satisfied.
Given this consideration, the following theorem shows that T−1/βαT^{-1/\beta\_{\alpha}} gives a minimax lower bound for the convergence rate of any estimator for θ∗\theta^{\*} under [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"):

###### Theorem 4.3.

For any α∈(0,1)∪(1,∞)\alpha\in(0,1)\cup(1,\infty), there exists a constant b>0b>0 such that

|  |  |  |
| --- | --- | --- |
|  | lim infT→∞infθ^Tsup|θ|≤2​ρTsupg∈𝒢​(θ,α,1/2,b)Pg⁡(|θ^T−θ|≥ρT)>0,\liminf\_{T\to\infty}\inf\_{\hat{\theta}\_{T}}\sup\_{|\theta|\leq 2\rho\_{T}}\sup\_{g\in\mathcal{G}(\theta,\alpha,1/2,b)}\operatorname{P}\_{g}\left(|\hat{\theta}\_{T}-\theta|\geq\rho\_{T}\right)>0, |  |

where ρT:=T−1/βα\rho\_{T}:=T^{-1/\beta\_{\alpha}} and the infimum is taken over all estimators based on N∩[0,T]N\cap[0,T], i.e. all σ​(N∩[0,T])\sigma(N\cap[0,T])-measurable random variables.

###### Remark 4.2.

Since the cumulant measure of order (p,q)(p,q) of NN vanishes if p∧q>1p\wedge q>1, condition ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) holds whenever ϖ=1\varpi=1, and also holds for ϖ<2\varpi<2 when gg is bounded.
Therefore, T−1/βαT^{-1/\beta\_{\alpha}} is also a minimax lower bound for the convergence rate of any estimator for θ∗\theta^{\*} under the assumptions of [Theorem 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") when α<2\alpha<2.

## 5 Simulation study

Bivariate Hawkes and Neyman–Scott processes equipped with gamma kernels are used to model the relationship between two series of timestamps in high-frequency financial data; for instance, see [potiron2025mutually] and [shiotani2024statistical], respectively.
In our experiments, we employ “lagged” variants of these models as the data-generating processes.
Using simulated data, we numerically investigate the accuracy, convergence rate, and tuning parameter sensitivity of the DS estimator and our proposed estimator.
We adopt the triangular kernel KtriK\_{\mathrm{tri}} for the kernel method in all numerical experiments in this paper.

### 5.1 Models

#### 5.1.1 Lagged bivariate Hawkes process with gamma kernels

First, we introduce a bivariate Hawkes process with conditional intensity functions

|  |  |  |
| --- | --- | --- |
|  | λi​(t)=μi+∑tk,1<tϕi​1​(t−tk,1)+∑tk,2<tϕi​2​(t−tk,2),i=1,2,\lambda\_{i}(t)=\mu\_{i}+\sum\_{t\_{k,1}<t}\phi\_{i1}(t-t\_{k,1})+\sum\_{t\_{k,2}<t}\phi\_{i2}(t-t\_{k,2}),\qquad i=1,2, |  |

where {tk,i}\{t\_{k,i}\} denotes the kk-th event time in the ii-th component.
We parameterize the kernel functions as
ϕi​j​(t)=αi​j​hi​j​(t)\phi\_{ij}(t)=\alpha\_{ij}h\_{ij}(t) for t>0t>0, where αi​j>0\alpha\_{ij}>0
is the branching ratio and hi​j​(t)h\_{ij}(t) is a probability density function
on (0,∞)(0,\infty).

In this study, we adopt gamma kernels. Specifically, we assume that hi​jh\_{ij} follows a gamma density Γ​(Di​j,βi​j)\Gamma(D\_{ij},\beta\_{ij}):

|  |  |  |
| --- | --- | --- |
|  | hi​j​(t)=βi​jDi​jΓ​(Di​j)​tDi​j−1​e−βi​j​t,t>0,h\_{ij}(t)=\frac{\beta\_{ij}^{D\_{ij}}}{\Gamma(D\_{ij})}t^{D\_{ij}-1}e^{-\beta\_{ij}t},\qquad t>0, |  |

where Di​j>0D\_{ij}>0 is the shape parameter and βi​j>0\beta\_{ij}>0 is the rate
parameter. When Di​j=1D\_{ij}=1, this specification reduces to the classical
exponential kernel, so the exponential Hawkes model is included as a special case.
We write 𝝁=(μ1,μ2)⊤\boldsymbol{\mu}=(\mu\_{1},\mu\_{2})^{\top} for the baseline
intensity vector, and
𝜶=(αi​j)1≤i,j≤2\boldsymbol{\alpha}=(\alpha\_{ij})\_{1\leq i,j\leq 2},
𝜷=(βi​j)1≤i,j≤2\boldsymbol{\beta}=(\beta\_{ij})\_{1\leq i,j\leq 2},
and 𝑫=(Di​j)1≤i,j≤2\boldsymbol{D}=(D\_{ij})\_{1\leq i,j\leq 2}
for the matrices of branching ratios, rate parameters, and shape parameters,
respectively. We then collect all kernel and baseline parameters into

|  |  |  |
| --- | --- | --- |
|  | η=(𝝁,𝜶,𝜷,𝑫)∈(0,∞)2×(0,∞)2×2×(0,∞)2×2×(0,∞)2×2.\eta=(\boldsymbol{\mu},\boldsymbol{\alpha},\boldsymbol{\beta},\boldsymbol{D})\in(0,\infty)^{2}\times(0,\infty)^{2\times 2}\times(0,\infty)^{2\times 2}\times(0,\infty)^{2\times 2}. |  |

We assume the spectral radius of 𝜶\boldsymbol{\alpha} is smaller than 1 to ensure stationarity.
Following bacry2012non, the intensity is

|  |  |  |
| --- | --- | --- |
|  | Λ=(λ1​(η),λ2​(η))⊤=(I2−𝜶)−1​𝝁\Lambda=(\lambda\_{1}(\eta),\lambda\_{2}(\eta))^{\top}=(I\_{2}-\boldsymbol{\alpha})^{-1}\boldsymbol{\mu} |  |

(Eq.(3) in [bacry2012non]), and the CPCF is

|  |  |  |
| --- | --- | --- |
|  | g​(u;η,θ)=1+ν12​(u;η)λ1​(η)​λ2​(η),u∈ℝ,g(u;\eta,\theta)=1+\frac{\nu\_{12}(u;\eta)}{\lambda\_{1}(\eta)\,\lambda\_{2}(\eta)},\qquad u\in\mathbb{R}, |  |

where ν12\nu\_{12} is the (1, 2) component of the infinitesimal covariance matrix ν\nu of the bivariate Hawkes process (Eq.(8) in [bacry2012non]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν12​(u)=(Ψ​(u)​Σ+Σ​Ψ⊤​(−u)+Ψ~∗Σ​Ψ⊤​(u))1,2u∈ℝ,\nu\_{12}(u)=\Bigl(\Psi(u)\Sigma+\Sigma\Psi^{\top}(-u)+\widetilde{\Psi}\*\Sigma\Psi^{\top}(u)\Bigr)\_{1,2}\qquad u\in\mathbb{R}, |  | (5.1) |

where Σ=diag​{λ1,λ2}\Sigma=\mathrm{diag}\{\lambda\_{1},\lambda\_{2}\},
Ψ​(u)=(Ψi​j​(u))1≤i,j≤2\Psi(u)=(\Psi\_{ij}(u))\_{1\leq i,j\leq 2} is defined by

|  |  |  |
| --- | --- | --- |
|  | Ψ​(u)=∑m=1∞Φ(∗m)​(u),Φ(∗m)=Φ∗⋯∗Φ⏟m​times,\Psi(u)=\sum\_{m=1}^{\infty}\Phi^{(\*m)}(u),\qquad\Phi^{(\*m)}=\underbrace{\Phi\*\cdots\*\Phi}\_{m\ \text{times}}, |  |

with kernel matrix
Φ​(u)=(ϕi​j​(u))1≤i,j≤2\Phi(u)=\bigl(\phi\_{ij}(u)\bigr)\_{1\leq i,j\leq 2}
and ∗\* denoting the matrix convolution,
and Ψ~​(u)=Ψ​(−u),u∈ℝ\widetilde{\Psi}(u)=\Psi(-u),u\in\mathbb{R}.

In addition,
let θ∈ℝ\theta\in\mathbb{R} denote the lead-lag parameter.
Given a realization of the bivariate Hawkes process N=(N10,N20)N=(N\_{1}^{0},N\_{2}^{0}), we call the shifted process (N1,N2)=(N10,N20(⋅−θ))(N\_{1},N\_{2})=(N\_{1}^{0},\,N\_{2}^{0}(\cdot-\theta)) a *lagged bivariate Hawkes process with gamma kernels (LBHPG)*.
Its distribution is denoted by

|  |  |  |
| --- | --- | --- |
|  | LBHPG​(η,θ).\mathrm{LBHPG}(\eta,\theta). |  |

For the shifted process LBHPG​(η,θ)\mathrm{LBHPG}(\eta,\theta), the intensity is still Λ\Lambda, while the cross–covariance density is simply shifted:

|  |  |  |
| --- | --- | --- |
|  | ν12​(u−θ;η),u∈ℝ.\nu\_{12}(u-\theta;\eta),\qquad u\in\mathbb{R}. |  |

Also, we have the cross-pair correlation function (CPCF) of LBHPG​(η,θ)\mathrm{LBHPG}(\eta,\theta) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(u;η,θ)=1+ν12​(u−θ;η)λ1​(η)​λ2​(η),u∈ℝ.g(u;\eta,\theta)=1+\frac{\nu\_{12}(u-\theta;\eta)}{\lambda\_{1}(\eta)\,\lambda\_{2}(\eta)},\qquad u\in\mathbb{R}. |  | (5.2) |

In the simulation study, we restrict to the case of common rate parameters, that is, βi​j≡β\beta\_{ij}\equiv\beta for all i,j∈{1,2}i,j\in\{1,2\}. In such cases,
LBHPG​(η,θ)\mathrm{LBHPG}(\eta,\theta) satisfies [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) with α=min⁡{D12,D21}\alpha=\min\{D\_{12},D\_{21}\} if min⁡{D12,D21}<1\min\{D\_{12},D\_{21}\}<1 (diverging gamma kernel(s)) and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i) with α=2\alpha=2 if D11=D21=D12=D22=1D\_{11}=D\_{21}=D\_{12}=D\_{22}=1 (exponential kernels).
The former can be obtained by the reproducibility of gamma densities and the local behavior of bilateral gamma densities at the origin [kuchler2008shapes, Thm. 6.1]. For details, see Appendix [A.7](https://arxiv.org/html/2601.01871v1#A1.SS7 "A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes").
The latter follows from the explicit formula for the CPCF for bivariate Hawkes processes with exponential kernels, which can be obtained by [bacry2015hawkes, Example 3].
The moment condition [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i) is guaranteed thanks to Theorem 1 in [leblanc2024exponential].
We also have a bound on the strong mixing rate [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) from Theorem 3.1 in [boly2023mixing], since the gamma kernels decay geometrically.
Therefore, LBHPG​(η,θ)\mathrm{LBHPG}(\eta,\theta) satisfies the assumptions in Theorem [4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") with a (smoothing) kernel satisfying Assumption [K] in such special cases.

#### 5.1.2 Lagged bivariate Neyman-Scott process with gamma kernels

First, we recall the construction of a bivariate Neyman-Scott process on ℝ\mathbb{R}
following Section 5.1 in shiotani2024statistical. Let 𝒞\mathcal{C} be a homogeneous
Poisson (parent) process on ℝ\mathbb{R} with intensity λ>0\lambda>0. For i=1,2i=1,2 and each
c∈𝒞c\in\mathcal{C}, let Mi​(c)M\_{i}(c) be the number of offspring in the component ii from the parent cc.
We assume that {Mi​(c)}c∈𝒞\{M\_{i}(c)\}\_{c\in\mathcal{C}} are i.i.d. copies of a ℤ≥0\mathbb{Z}\_{\geq 0}-valued
random variable MiM\_{i} with finite mean
σi=𝔼​[Mi]∈(0,∞),i=1,2.\sigma\_{i}=\mathbb{E}[M\_{i}]\in(0,\infty),i=1,2.
For simplicity, we assume that MiM\_{i} follows a Poisson distribution Poi​(σi),i=1,2\mathrm{Poi}(\sigma\_{i}),i=1,2.
Conditional on Mi​(c)M\_{i}(c), the temporal offsets {di​(c,m)}m=1Mi​(c)\{d\_{i}(c,m)\}\_{m=1}^{M\_{i}(c)} of the
offspring are i.i.d. with density fif\_{i}, independent over i,c,mi,c,m and independent of
𝒞\mathcal{C} and {Mi​(c)}\{M\_{i}(c)\}.
Then, let

|  |  |  |
| --- | --- | --- |
|  | Ni0=∑c∈𝒞∑m=1Mi​(c)δc+di​(c,m),i=1,2.N\_{i}^{0}=\sum\_{c\in\mathcal{C}}\sum\_{m=1}^{M\_{i}(c)}\delta\_{c+d\_{i}(c,m)},\qquad i=1,2. |  |

We call N0=(N10,N20)N^{0}=(N\_{1}^{0},N\_{2}^{0}) a bivariate Neyman-Scott process.

N0N^{0} is stationary with intensities

|  |  |  |
| --- | --- | --- |
|  | λi​(ξ)=λ​σi,i=1,2.\lambda\_{i}(\xi)=\lambda\,\sigma\_{i},\qquad i=1,2. |  |

Moreover, the cross–intensity
of (N10,N20)(N\_{1}^{0},N\_{2}^{0}) is

|  |  |  |
| --- | --- | --- |
|  | λ12​(u;ξ)=λ2​σ1​σ2+λ​σ1​σ2​∫ℝf1​(s;τ1)​f2​(u+s;τ2)​𝑑s,u∈ℝ,\lambda\_{12}(u;\xi)=\lambda^{2}\sigma\_{1}\sigma\_{2}+\lambda\sigma\_{1}\sigma\_{2}\int\_{\mathbb{R}}f\_{1}(s;\tau\_{1})f\_{2}(u+s;\tau\_{2})\,ds,\qquad u\in\mathbb{R}, |  |

see Eq.(5.2) and the subsequent calculation in [shiotani2024statistical].
Therefore, the cross–pair correlation function (CPCF) of the bivariate
Neyman-Scott process is

|  |  |  |
| --- | --- | --- |
|  | g​(u;ξ)=λ12​(u;ξ)λ1​(ξ)​λ2​(ξ)=1+1λ​∫ℝf1​(s;τ1)​f2​(u+s;τ2)​𝑑s,u∈ℝ,g(u;\xi)=\frac{\lambda\_{12}(u;\xi)}{\lambda\_{1}(\xi)\lambda\_{2}(\xi)}=1+\frac{1}{\lambda}\int\_{\mathbb{R}}f\_{1}(s;\tau\_{1})f\_{2}(u+s;\tau\_{2})\,ds,\qquad u\in\mathbb{R}, |  |

where ξ\xi collects all parameters introduced above.

In this simulation study, we adopt gamma dispersal kernels as in the NBNSP-G model
of Shiotani and Yoshida [shiotani2024statistical]. Specifically, for i=1,2i=1,2 we assume that

|  |  |  |
| --- | --- | --- |
|  | fi​(u;τi)=liαiΓ​(αi)​uαi−1​e−li​u​1(0,∞)​(u),u∈ℝ,f\_{i}(u;\tau\_{i})=\frac{l\_{i}^{\alpha\_{i}}}{\Gamma(\alpha\_{i})}u^{\alpha\_{i}-1}e^{-l\_{i}u}1\_{(0,\infty)}(u),\qquad u\in\mathbb{R}, |  |

where τi=(αi,li)\tau\_{i}=(\alpha\_{i},l\_{i}), αi>0\alpha\_{i}>0 is the shape parameter and li>0l\_{i}>0 is the
rate parameter of the gamma law. We then collect the parameters as

|  |  |  |
| --- | --- | --- |
|  | ξ=(λ,σ1,σ2,α1,α2,l1,l2)∈(0,∞)7.\xi=(\lambda,\sigma\_{1},\sigma\_{2},\alpha\_{1},\alpha\_{2},l\_{1},l\_{2})\in(0,\infty)^{7}. |  |

Let θ∈ℝ\theta\in\mathbb{R} denote the lead–lag parameter. Given a realization
N0=(N10,N20)N^{0}=(N\_{1}^{0},N\_{2}^{0}) of the bivariate Neyman-Scott process with gamma kernels described above, we define the lagged process by shifting the second component:

|  |  |  |
| --- | --- | --- |
|  | (N1,N2)=(N10,N20(⋅−θ)).(N\_{1},N\_{2})=\bigl(N\_{1}^{0},\,N\_{2}^{0}(\,\cdot\,-\theta)\bigr). |  |

We refer to N=(N1,N2)N=(N\_{1},N\_{2}) as the *lagged bivariate Neyman-Scott process with gamma kernels (LBNSPG)* and denote its distribution by

|  |  |  |
| --- | --- | --- |
|  | LBNSPG​(ξ,θ).\mathrm{LBNSPG}(\xi,\theta). |  |

The intensities of LBNSPG​(ξ,θ)\mathrm{LBNSPG}(\xi,\theta) are still given by
λ1​(ξ)\lambda\_{1}(\xi) and λ2​(ξ)\lambda\_{2}(\xi), while the cross–intensity is simply shifted:

|  |  |  |
| --- | --- | --- |
|  | λ12​(u−θ;ξ),u∈ℝ.\lambda\_{12}(u-\theta;\xi),\qquad u\in\mathbb{R}. |  |

Consequently, the CPCF of LBNSPG​(ξ,θ)\mathrm{LBNSPG}(\xi,\theta) is

|  |  |  |
| --- | --- | --- |
|  | g​(u;ξ,θ)=λ12​(u−θ;ξ)λ1​(ξ)​λ2​(ξ)=1+1λ​p​(u−θ;τ1,τ2),\displaystyle g(u;\xi,\theta)=\frac{\lambda\_{12}(u-\theta;\xi)}{\lambda\_{1}(\xi)\lambda\_{2}(\xi)}=1+\frac{1}{\lambda}p(u-\theta;\tau\_{1},\tau\_{2}), |  |
|  |  |  |
| --- | --- | --- |
|  | p​(u;τ1,τ2)=∫ℝf1​(s;τ1)​f2​(u+s;τ2)​𝑑s,u∈ℝ.\displaystyle p(u;\tau\_{1},\tau\_{2})=\int\_{\mathbb{R}}f\_{1}(s;\tau\_{1})f\_{2}(u+s;\tau\_{2})\,ds,\qquad u\in\mathbb{R}. |  |

The function p​(⋅;α1,α2,l1,l2)p(\cdot;\alpha\_{1},\alpha\_{2},l\_{1},l\_{2}) is the density of a bilateral gamma distribution.
Küchler and Tappe [kuchler2008shapes] provide a detailed analysis of the shapes of bilateral gamma densities, including unimodality and the local behavior near zero (see Theorem 6.1 therein).
Combining their results with the above representation shows that g​(⋅;ξ,θ)g(\cdot;\xi,\theta) is strictly unimodal with the peak at θ\theta whenever the parameters are symmetric, i.e., α1=α2\alpha\_{1}=\alpha\_{2} and l1=l2l\_{1}=l\_{2}.
We restrict attention to such symmetric cases in our simulation experiments.
Under this restriction, LBNSPG​(ξ,θ)\mathrm{LBNSPG}(\xi,\theta) satisfies [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) if α1+α2<1\alpha\_{1}+\alpha\_{2}<1 and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i) if α1+α2>1\alpha\_{1}+\alpha\_{2}>1, with α=min⁡{α1+α2,3}\alpha=\min\{\alpha\_{1}+\alpha\_{2},3\} in both cases.

Note that LBNSPG​(ξ,0)\mathrm{LBNSPG}(\xi,0) is the special case (setting the noise process to zero and the distribution of MiM\_{i} to Poisson) of the NBNSP-G model introduced in Section 6.1 in [shiotani2024statistical].
Therefore, LBNSPG​(ξ,0)\mathrm{LBNSPG}(\xi,0) satisfies condition [NS] in [shiotani2024statistical], so that Lemma 10.13 there bounds the α\alpha–mixing coefficients of LBNSPG​(ξ,θ)\mathrm{LBNSPG}(\xi,\theta) in terms of the tail probabilities of the dispersal kernels:
for all c1≥0c\_{1}\geq 0 and m≥2​r+2m\geq 2r+2,

|  |  |  |
| --- | --- | --- |
|  | αc1,∞N​(m;r):=supc2≥0αc1,c2N​(m;r)≤8​m​λ​(m+1+2​r)​∑i=12σi​∫|z|≥m/2−2​rfi​(z;τi)​𝑑z.\alpha^{N}\_{c\_{1},\infty}(m;r):=\sup\_{c\_{2}\geq 0}\alpha^{N}\_{c\_{1},c\_{2}}(m;r)\leq 8m\lambda\;(m+1+2r)\sum\_{i=1}^{2}\sigma\_{i}\int\_{|z|\geq m/2-2r}f\_{i}(z;\tau\_{i})\,dz. |  |

Since the gamma kernels have geometrically decaying tails, this implies that
αc1,∞​(m;r1)\alpha\_{c\_{1},\infty}(m;r\_{1}) decreases faster than any power of mm, so Assumption [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) holds for LBNSPG​(ξ,θ)\mathrm{LBNSPG}(\xi,\theta).
Moreover, since the Poisson-distributed MiM\_{i} possesses moments of all orders, Lemma 10.14 in [shiotani2024statistical] yields finiteness of moments of Ni​((0,1])N\_{i}((0,1]) of all orders, so that Assumption [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i) is satisfied.
Therefore, LBNSPG​(ξ,θ)\mathrm{LBNSPG}(\xi,\theta) fulfills Assumptions
[[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and thus is in the scope of Theorem [4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") if α1=α2\alpha\_{1}=\alpha\_{2}, l1=l2l\_{1}=l\_{2}, and α1+α2≠1\alpha\_{1}+\alpha\_{2}\neq 1.

#### 5.1.3 Model and parameter specifications in the simulation studies

We consider two types of bivariate stationary point process models, each with three sets of parameter values.
The models are labeled as
hawkes\_gamma\_sym,
hawkes\_gamma\_asym, hawkes\_exp, ns\_gamma\_1, ns\_gamma\_2, and ns\_gamma\_3.

| Name | Family | α\alpha | βα\beta\_{\alpha} | The convergence rate T−1/βαT^{-1/\beta\_{\alpha}} |
| --- | --- | --- | --- | --- |
| hawkes\_gamma\_sym | LBHPG | 0.4 | 0.4 | T−5/2T^{-5/2} |
| hawkes\_gamma\_asym | LBHPG | 0.4 | 0.4 | T−5/2T^{-5/2} |
| hawkes\_exp | LBHPG | 2 | 3 | T−1/2T^{-1/2} |
| ns\_gamma\_1 | LBNSPG | 0.8 | 0.8 | T−5/4T^{-5/4} |
| ns\_gamma\_2 | LBNSPG | 1.6 | 2.2 | T−5/11T^{-5/11} |
| ns\_gamma\_3 | LBNSPG | 3 | 5 | T−1/5T^{-1/5} |

Table 1: Values of α\alpha (the “sharpness” parameter of the CPCF gg in [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"); smaller values imply sharper functions), βα=α∨(2​α−1)\beta\_{\alpha}=\alpha\vee(2\alpha-1), and the minimax lower bound on the convergence rate T−1/βαT^{-1/\beta\_{\alpha}} in Theorem [4.3](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Minimax lower bound for the convergence rate ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") for each model.

All LBHPG models share

|  |  |  |
| --- | --- | --- |
|  | 𝝁=(0.2,0.2)⊤,𝜶=(0.10.10.10.1),𝜷=(10101010).\boldsymbol{\mu}=(0.2,0.2)^{\top},\qquad\boldsymbol{\alpha}=\begin{pmatrix}0.1&0.1\\ 0.1&0.1\end{pmatrix},\qquad\boldsymbol{\beta}=\begin{pmatrix}10&10\\ 10&10\end{pmatrix}. |  |

We use three specifications for the shape matrix 𝑫\boldsymbol{D} to cover different degrees of regularity and asymmetry:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hawkes\_gamma\_sym:\displaystyle\texttt{hawkes\\_gamma\\_sym}:\quad | 𝑫=(0.40.40.40.4);\displaystyle\boldsymbol{D}=\begin{pmatrix}0.4&0.4\\ 0.4&0.4\end{pmatrix}; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | hawkes\_gamma\_asym:\displaystyle\texttt{hawkes\\_gamma\\_asym}:\quad | 𝑫=(0.40.40.80.4);\displaystyle\boldsymbol{D}=\begin{pmatrix}0.4&0.4\\ 0.8&0.4\end{pmatrix}; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | hawkes\_exp:\displaystyle\texttt{hawkes\\_exp}:\quad | 𝑫=(1111).\displaystyle\boldsymbol{D}=\begin{pmatrix}1&1\\ 1&1\end{pmatrix}. |  |

For the LBNSPG models, we fix

|  |  |  |
| --- | --- | --- |
|  | λ=0.1,σ1=σ2=4\lambda=0.1,\qquad\sigma\_{1}=\sigma\_{2}=4 |  |

and use symmetric dispersal shape and rate parameters.
We select three settings to vary the smoothness of the CPCF around the peak:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ns\_gamma\_1:\displaystyle\texttt{ns\\_gamma\\_1}: | (α1,α2)=(0.4,0.4),(l1,l2)=(10,10),\displaystyle\quad(\alpha\_{1},\alpha\_{2})=(0.4,0.4),\quad(l\_{1},l\_{2})=(10,10), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ns\_gamma\_2:\displaystyle\texttt{ns\\_gamma\\_2}: | (α1,α2)=(0.8,0.8),(l1,l2)=(10,10),\displaystyle\quad(\alpha\_{1},\alpha\_{2})=(0.8,0.8),\quad(l\_{1},l\_{2})=(10,10), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ns\_gamma\_3:\displaystyle\texttt{ns\\_gamma\\_3}: | (α1,α2)=(2.0,2.0),(l1,l2)=(100,100).\displaystyle\quad(\alpha\_{1},\alpha\_{2})=(2.0,2.0),\quad(l\_{1},l\_{2})=(100,100). |  |

### 5.2 Accuracy

In this experiment, we compare the accuracy of the lead-lag time estimators using the root mean squared error (RMSE) across the six scenarios.

For each pair of observation time interval length T∈{1000,2000,4000,8000}T\in\{1000,2000,4000,8000\} and the estimator, we generate 50005000 Monte Carlo replicates of sample paths.
In every replicate, the true lead-lag time is drawn as θ∗∼𝒰​(−0.1,0.1)\theta^{\*}\sim\mathcal{U}(-0.1,0.1).
For a given estimator θ^\hat{\theta}, we report

|  |  |  |
| --- | --- | --- |
|  | RMSE=(15000​∑b=15000(θ^(b)−θ∗(b))2)1/2,\mathrm{RMSE}=\left(\frac{1}{5000}\sum\_{b=1}^{5000}\bigl(\hat{\theta}^{(b)}-\theta^{\*(b)}\bigr)^{2}\right)^{1/2}, |  |

where θ^(b)\hat{\theta}^{(b)} and θ∗(b)\theta^{\*(b)} denote the estimate and the true lead-lag time in replicate bb.
Randomizing θ∗\theta^{\*} across replicates summarizes performance averaged over a range of lead-lag values rather than at a single fixed θ∗\theta^{\*}.
The lead-lag time parameter is supposed to be in (−1,1)(-1,1), i.e., we set r=1r=1.
The bandwidth grid is {10−1,10−2,10−3,10−4,10−5,10−6}\{10^{-1},10^{-2},10^{-3},10^{-4},10^{-5},10^{-6}\} for both the Lepski method and DS estimators.
For the Lepski method, we set AT=log⁡log⁡TA\_{T}=\log\log T.
When the contrast function has multiple maximizers on (−r,r)(-r,r), we select the minimum as a deterministic tie-breaking rule.

![Refer to caption](simulations/graphs/rmse_all_scenarios.png)


Figure 2: RMSE of the estimators for the lead-lag time across six scenarios.
Each panel uses log–log axes with bandwidth hh on the x-axis and RMSE on the y-axis.
Dashed lines with markers trace the DS estimator over the bandwidth grid, while solid horizontal lines show the kernel estimator with the Lepski-selected bandwidth.
Colors indicate the observation-window length T∈{1000,2000,4000,8000}T\in\{1000,2000,4000,8000\} and are shared across panels.

Figure [2](https://arxiv.org/html/2601.01871v1#S5.F2 "Figure 2 ‣ 5.2 Accuracy ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes") illustrates two systematic patterns.
First, the performance of the DS estimator is sensitive to the bucket width hh. For each TT, the RMSE curves as a function of hh are typically U-shaped: small buckets lead to high variance due to the scarcity of joint activations, whereas larger buckets introduce a discretization bias because the lead-lag time is constrained to a coarse grid. Moreover, the value of hh that minimizes the RMSE depends on both the underlying model and the observation window length TT.
This confirms that, in practice, the DS estimator requires model-specific tuning of hh.

Second, the kernel estimator with Lepski’s bandwidth selection achieves lower RMSE than the DS estimator for almost all combinations of TT and data-generating process.
In Figure [2](https://arxiv.org/html/2601.01871v1#S5.F2 "Figure 2 ‣ 5.2 Accuracy ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes"), the horizontal solid lines corresponding to the Lepski estimator lie close to (and often below) the best DS RMSE over the grid in each panel. Importantly, this improvement is obtained without any manual tuning of the bandwidth: once the grid ℋ𝒯\mathcal{H\_{T}} and the slowly diverging constant AT=log⁡log⁡TA\_{T}=\log\log T are fixed, the procedure automatically adapts the smoothing level to the data. This demonstrates the main practical advantage of the proposed approach over the DS method.

### 5.3 Convergence rate and dependence on hyperparameters of Lepski’s method

In this experiment, we investigate the convergence rate of the Lepski estimator, as shown in Theorem [4.2](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.1 Bandwidth selection by Lepski’s method ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").
We also examine how the estimator behaves as the tuning parameter ATA\_{T} varies.

As in the previous experiment, for each observation-window length T∈{1000,2000,4000,8000}T\in\{1000,2000,4000,8000\} and each estimator, we generate 5000 Monte Carlo replicates of sample paths.
In every replicate, the true lead-lag time is drawn as θ∗∼𝒰​(−0.1,0.1)\theta^{\*}\sim\mathcal{U}(-0.1,0.1).
The lead-lag time parameter is supposed to be in (−1,1)(-1,1), i.e., we set r=1r=1.
The bandwidth grid is {10−1,10−2,10−3,10−4,10−5,10−6}\{10^{-1},10^{-2},10^{-3},10^{-4},10^{-5},10^{-6}\}.

![Refer to caption](simulations/graphs/sensitivity_lepski_all_scenarios.png)


Figure 3: RMSE versus observation window TT (log–log scale) across all simulation settings and ATA\_{T} schedules. Theoretical T−1/βαT^{-1/\beta\_{\alpha}} slopes are shown as dashed lines.

Figure [3](https://arxiv.org/html/2601.01871v1#S5.F3 "Figure 3 ‣ 5.3 Convergence rate and dependence on hyperparameters of Lepski’s method ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes") investigates the convergence rate of the Lepski estimator. In each scenario, the RMSE is plotted against TT on a log–log scale together with the theoretical slope T−1/βαT^{-1/\beta\_{\alpha}} derived from the minimax lower bound in Theorem [4.3](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Minimax lower bound for the convergence rate ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").
Across all six models, the empirical curves for the Lepski estimator are nearly parallel to the guideline.
Thus, the proposed estimator may attain the optimal convergence rate given by our theory.

The figure also compares three schedules for the tuning parameter ATA\_{T}: 0.5​log⁡log⁡T0.5\log\log T, log⁡log⁡T\log\log T, and 2​log⁡log⁡T2\log\log T.
Across all six models, the three RMSE curves are close and exhibit similar slopes, indicating that the convergence rate is robust to the choice of ATA\_{T} within this range.
The differences across schedules are mostly level shifts, so the precise constant in front of log⁡log⁡T\log\log T is not critical for achieving the minimax rate.

## 6 Empirical illustration

An outstanding feature of the method depicted in dobrev2017high is that the DS estimator can effectively capture the fastest speed of information transmission between two geographically separated markets, which is typically close to the speed of light.
Specifically, they analyzed the lead-lag relationships between the cash and futures markets for the 10-Year U.S. Treasury Note and for the S&P 500 index.
The DS estimator stably detected sharp peaks of the cross-market activity measures at 5 milliseconds, which is consistent with the optical propagation time between the futures exchange (in Aurora, Illinois) and the cash market platform (in Secaucus, New Jersey).
In this section, we investigate whether this finding continues to hold even for geographically closer markets, for which sub-millisecond estimates are required to detect such relationships.

More precisely, we examine the lead-lag relationships between the quotes of a single stock on two different exchanges: the NASDAQ (located in Carteret, New Jersey) and BATS (located in Secaucus, New Jersey).
According to [Tiv2020, Table 2], the optical propagation time between the NASDAQ and BATS exchanges is approximately 0.1 milliseconds.
We obtain the timestamps of updates of the best quotes on each exchange in August 2015 from the Daily TAQ dataset, which provides every quote reported to the consolidated tape by all Consolidated Trade Association (CTA) and Unlisted Trading Privileges (UTP) participants.
According to [BM2019], the microsecond timestamps were fully implemented in this dataset on August 6, 2015.
For this reason, we focus on the sample period beginning on August 6, 2015, comprising 18 trading days.
Our analysis covers the component stocks of the NASDAQ-100 in 2015, totally 108 stocks.
We restrict attention to transactions occurring between 9:45 and 15:45, discarding the first and last 15 minutes of the trading day in order to avoid non-stationarities commonly observed at the open and close.

In the Daily TAQ data, each quote record contains two timestamps: Time and Participant Timestamp, which refer to the timestamps published by Securities Information Processors (SIPs) and exchange matching engines, respectively.
Following [BM2019], we refer to the former as the *SIP timestamp* and the latter as the *participant timestamp*.
See [BM2019, Section 2] and [hasbrouck2021price, Section 4] for the institutional background.
In this study, we use the participant timestamp because our preliminary analysis suggests that the SIP timestamp is heavily contaminated by *reporting latencies* in the terminology of [BM2019].
Specifically, even when multiple market events occur simultaneously and share the same participant timestamp, they often receive different SIP timestamps, causing artificial misalignment across market events [schwenkparticipant, wu2025latency, tivnan2018price].
Moreover, reporting latencies fluctuate dynamically due to various latency sources, and their distribution is heavy-tailed (cf. [holden2023blink, wu2025latency] and [BM2019, Appendix]), making it difficult to disentangle their effects from genuine lead–lag behavior.
For these reasons, we rely on participant timestamps.
Developing a lead–lag estimator that is robust to such timestamp contamination would be an interesting direction for future research.

For each trading day and for each stock, we compute both our kernel estimator θ^h\hat{\theta}\_{h} and the DS estimator θ^hD​S\hat{\theta}^{DS}\_{h}.
For the kernel estimator, we use the triangular kernel and select the bandwidth via the Lepski type method proposed in [Section 4.1](https://arxiv.org/html/2601.01871v1#S4.SS1 "4.1 Bandwidth selection by Lepski’s method ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes"), with ℋT={1​μ​s,10​μ​s,100​μ​s,1000​μ​s}\mathcal{H}\_{T}=\{1~\mu\text{s},10~\mu\text{s},100~\mu\text{s},1000~\mu\text{s}\}, AT=log⁡log⁡TA\_{T}=\log\log T and T=21600T=21600 (the number of seconds in 6 trading hours).
For the DS estimator, we consider two bucket sizes: h=1​μ​sh=1~\mu\text{s} and h=100​μ​sh=100~\mu\text{s}.
The former corresponds to the minimum time unit, as suggested in [dobrev2017high], whereas the latter is motivated by the physical transmission time of approximately 100 μ\mus between the two exchanges (cf. [Tiv2020, Table 2]).
We set r=10​msr=10~\text{ms} for the search range for lead-lag parameters.

[Fig. 4](https://arxiv.org/html/2601.01871v1#S6.F4 "In 6 Empirical illustration ‣ On lead-lag estimation of non-synchronously observed point processes") presents violin plots of the lead-lag time estimates for the three estimators.
The estimates of θ^h^\hat{\theta}\_{\hat{h}} cluster around several values, most notably around 95 μ\mus and 130 μ\mus.
These values have clear physical interpretations: According to [Tiv2020, Table 2], the transmission time between NASDAQ and BATS is approximately 95 μ\mus via hybrid laser link and 128 μ\mus via fiber optic cable.
This also suggests that, in our sample, NASDAQ generally leads BATS in updating best quotes, which is an intuitive result given that all the stocks analyzed are listed on NASDAQ, and NASDAQ tends to have greater market participation.

We observe a similar clustering pattern for the DS estimator with h=1​μ​sh=1~\mu\text{s}, although these estimates appear to cluster slightly more around 130 μ\mus than 95 μ\mus.
However, they also exhibit a few negative “outliers”, an issue not present in the kernel estimator.
Using a larger bucket size h=100​μ​sh=100~\mu\text{s} eliminates such outliers, but the coarse discretization inherent in the DS estimator significantly distorts the estimated lead–lag parameters.

To highlight the differences between our estimator and the DS estimator with h=1​μ​sh=1~\mu\text{s}, [Fig. 5](https://arxiv.org/html/2601.01871v1#S6.F5 "In 6 Empirical illustration ‣ On lead-lag estimation of non-synchronously observed point processes") presents a scatter plot of the two sets of estimates, color-coded by n1​n2\sqrt{n\_{1}n\_{2}}, the geometric mean of the sample sizes.
The two estimators yield similar values in many cases, but their estimates diverge as one or both of n1n\_{1} and n2n\_{2} become small. This observation aligns with our theoretical finding that the bucket size in the DS estimator should be increased when the sample size decreases (cf. the discussion following [Theorem 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")).

![Refer to caption](x1.png)


Figure 4: Violin plots of the daily lead-lag time estimates between quotes on the NASDAQ and BATS exchanges, computed for all the component stocks of the NASDAQ-100 in August 6–31, 2015.
The top panel shows the entire plots, while the bottom panel zooms in on the interval from 0.07 ms to 0.27 ms.
The smoothing bandwidths for the violin plots are selected by sheather1991reliable’s method implemented as the R function bw.SJ().
The horizontal axis is expressed in milliseconds. A positive estimate implies that the NASDAQ leads the BATS and vice versa.

![Refer to caption](x2.png)


Figure 5: Scatter plot of the estimates of θ^hD​S\hat{\theta}^{DS}\_{h} with h=1​μ​sh=1~\mu\text{s} versus θ^h^\hat{\theta}\_{\hat{h}}, color-coded by the geometric mean of the sample sizes.
The values are expressed in milliseconds.
The dotted line is the 45-degree line.

## 7 Concluding remarks

In this paper, we have established a theoretical foundation for timestamp-based lead-lag analysis from a point process perspective.
Within this framework, the method of dobrev2017high for analyzing lead-lag relationships can be interpreted as an estimator of the cross-pair correlation function (CPCF) of the bivariate point process generated by two timestamp series.
Accordingly, the prevailing lead-lag time is naturally defined as the location of the sharpest peak of this CPCF.
We have proposed estimating this lead-lag time by maximizing a kernel density estimator of the CPCF.
Theoretically, our estimator nearly attains the optimal convergence rate for estimating the lead-lag time, provided that the bandwidth of the kernel estimator is chosen appropriately.
To this end, we have introduced a Lepski type bandwidth selection method.
In practice, our procedure addresses several shortcomings of the Dobrev–Schaumburg estimator that arise from its discrete nature.
We have demonstrated the superior performance of our estimator through comprehensive simulation studies and an illustrative empirical analysis.

Finally, we discuss several directions for future research to extend the applicability of our framework.
First, extending the proposed method to non-stationary settings is of practical interest.
Since financial market activity typically varies over time, the stationarity assumption imposed in this study may be restrictive for certain empirical applications. A promising avenue is to adopt the concept of transition-invariant cross-pair correlation function (see, e.g., [shaw2021globally]), which allows time-varying intensities while preserving a stable lead-lag structure that depends only on the time lag. Developing similar methods for such inhomogeneous settings would allow more accurate estimation of the lead-lag time.
Second, in practical applications, timestamp series may be contaminated by observation noise.
In such cases, a noise-robust estimator of the lead-lag parameter is required.
This problem is closely related to deconvolution, which has been studied by [cucala2008intensity] in the context of intensity function estimation for point processes and by [meister2011general] in the context of mode estimation for i.i.d. data.
Third, empirical CPCF estimates for high-frequency timestamps often exhibit multiple peaks.
These naturally arise because information transmission between two markets is bidirectional (as documented in [dobrev2017high]) and because transmission speeds differ across market participants.
While this paper focuses solely on the sharpest peak, identifying all “significant” peaks would also be of interest.
Similar questions have been studied in the classical literature on mode estimation; see [chacon2020modal, Section 3] and references therein.
Fourth, it is also worth investigating how the lead-lag parameter is affected by order types, size, and market conditions such as spread and depth. By treating these attributes as marks, we can analyze the lead-lag relationships between marked point processes.

## Appendix

## Appendix A Proofs

Throughout the discussion, we use the following notation and convention.
For two real numbers x,yx,y, we write x≲yx\lesssim y if x≤C​yx\leq Cy for some constant C>0C>0 depending only on r,α,α0,δ,b,(Bp)p≥1,(Bp,q)p,q≥1,εr,\alpha,\alpha\_{0},\delta,b,(B\_{p})\_{p\geq 1},(B\_{p,q})\_{p,q\geq 1},\varepsilon and ‖K‖∞\|K\|\_{\infty}.
For a real-valued function ff defined on [−r1,r1][-r\_{1},r\_{1}], we write ‖f‖Lp=‖f‖Lp​([−r1,r1])\|f\|\_{L^{p}}=\|f\|\_{L^{p}([-r\_{1},r\_{1}])} for each p∈[1,∞]p\in[1,\infty] for short.
We set g0≡1g\_{0}\equiv 1 whenever [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](i)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i1 "Item [A2](i) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") is assumed.

### A.1 Preliminaries

First, we can easily deduce from the definition of the cross-intensity function ([3.1](https://arxiv.org/html/2601.01871v1#S3.E1 "Equation 3.1 ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) that

|  |  |  |
| --- | --- | --- |
|  | E⁡[∫D×ℝφ​(y−x)​N1​(d​x)​N2​(d​y)]=Leb⁡(D)​λ1​λ2​∫ℝφ​(u)​g​(u)​𝑑u\operatorname{E}\left[\int\_{D\times\mathbb{R}}\varphi(y-x)N\_{1}(dx)N\_{2}(dy)\right]=\operatorname{Leb}(D)\lambda\_{1}\lambda\_{2}\int\_{\mathbb{R}}\varphi(u)g(u)du |  |

for any Borel function φ:ℝ→[0,∞]\varphi:\mathbb{R}\to[0,\infty] and D∈ℬ​(ℝ)D\in\mathcal{B}(\mathbb{R}).
We refer to this identity as Campbell’s formula in the following.

Next, we prove two auxiliary estimates that play a basic role throughout our discussion.
The first is a moment inequality for a sum of dependent random variables in terms of the α\alpha-mixing coefficients ([3.2](https://arxiv.org/html/2601.01871v1#S3.E2 "Equation 3.2 ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) and is a simple consequence of [doukhan1999new, Theorem 2] with a truncation argument.

###### Lemma A.1.

Let (Xj)j=0T−1(X\_{j})\_{j=0}^{T-1} be a sequence of random variables such that XjX\_{j} is σ​(N∩(Ij⊕r1))\sigma(N\cap(I\_{j}\oplus r\_{1}))-measurable for all jj.
Suppose also that max0≤j≤T−1⁡E⁡[Xjq]<∞\max\_{0\leq j\leq T-1}\operatorname{E}[X\_{j}^{q}]<\infty for some even integer q≥2q\geq 2.
Then, there exists a constant CqC\_{q} depending only on qq such that for any M,τ>0M,\tau>0,

|  |  |  |
| --- | --- | --- |
|  | ∥∑j=0T−1(Xj−E[Xj])∥q≤Cq{(TτMmax0≤j≤T−1E[|Xj|]+TM2∑m=τ∞αq,qN(m;r1))1/2+T1/qM(∑m=0∞(m+1)q−2αq,qN(m;r1))1/q}+2Tmax0≤j≤T−1∥Xj1{|Xj|>M}∥q.\left\|\sum\_{j=0}^{T-1}(X\_{j}-\operatorname{E}[X\_{j}])\right\|\_{q}\leq C\_{q}\left\{\left(T\tau M\max\_{0\leq j\leq T-1}\operatorname{E}[|X\_{j}|]+TM^{2}\sum\_{m=\tau}^{\infty}\alpha^{N}\_{q,q}(m;r\_{1})\right)^{1/2}\right.\\ \left.+T^{1/q}M\left(\sum\_{m=0}^{\infty}(m+1)^{q-2}\alpha^{N}\_{q,q}(m;r\_{1})\right)^{1/q}\right\}+2T\max\_{0\leq j\leq T-1}\left\|X\_{j}1\_{\{|X\_{j}|>M\}}\right\|\_{q}. |  |

###### Proof.

Set Yj:=Xj​1{|Xj|≤M}Y\_{j}:=X\_{j}1\_{\{|X\_{j}|\leq M\}} for j=0,1,…,T−1j=0,1,\dots,T-1.
By the triangle inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∑j=0T−1(Xj−E⁡[Xj])−∑j=0T−1(Yj−E⁡[Yj])‖q≤∑j=0T−1‖Xj​1{|Xj|>M}−E⁡[Xj​1{|Xj|>M}]‖q≤2​T​max0≤j≤T−1⁡‖Xj​1{|Xj|>M}‖q.\begin{split}\left\|\sum\_{j=0}^{T-1}(X\_{j}-\operatorname{E}[X\_{j}])-\sum\_{j=0}^{T-1}(Y\_{j}-\operatorname{E}[Y\_{j}])\right\|\_{q}&\leq\sum\_{j=0}^{T-1}\left\|X\_{j}1\_{\{|X\_{j}|>M\}}-\operatorname{E}[X\_{j}1\_{\{|X\_{j}|>M\}}]\right\|\_{q}\\ &\leq 2T\max\_{0\leq j\leq T-1}\left\|X\_{j}1\_{\{|X\_{j}|>M\}}\right\|\_{q}.\end{split} |  | (A.1) |

Meanwhile, for any integers 0≤j1≤⋯≤jp≤T−10\leq j\_{1}\leq\cdots\leq j\_{p}\leq T-1 such that jk+1−jk=mj\_{k+1}-j\_{k}=m for some 0≤k<p0\leq k<p and m≥0m\geq 0, we have

|  |  |  |
| --- | --- | --- |
|  | |Cov⁡[Yj1​⋯​Yjk,Yjk+1​⋯​Yjp]|≤min⁡{2​Mp−1​max0≤j≤T−1⁡E⁡[|Xj|], 4​Mp​αp,pN​(m;r1)},\begin{split}|\operatorname{Cov}[Y\_{j\_{1}}\cdots Y\_{j\_{k}},Y\_{j\_{k+1}}\cdots Y\_{j\_{p}}]|\leq\min\left\{2M^{p-1}\max\_{0\leq j\leq T-1}\operatorname{E}[|X\_{j}|],\,4M^{p}\alpha^{N}\_{p,p}(m;r\_{1})\right\},\end{split} |  |

where the second upper bound follows by the covariance inequality under strong mixing (see e.g. Lemma 3 in [Doukhan1994, Section 1.2]).
Hence, we can apply [doukhan1999new, Theorem 2] to YjY\_{j} with M=M,γ=C=1M=M,\gamma=C=1 and

|  |  |  |
| --- | --- | --- |
|  | θm=min⁡{M​max0≤j≤T−1⁡E⁡[|Xj|], 4​M2​αq,qN​(m;r1)}\theta\_{m}=\min\left\{M\max\_{0\leq j\leq T-1}\operatorname{E}[|X\_{j}|],\,4M^{2}\alpha^{N}\_{q,q}(m;r\_{1})\right\} |  |

in their notation.
Hence, there exists a constant CqC\_{q} depending only on qq such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[|∑j=0T−1(Yj−E⁡[Yj])|q]\displaystyle\operatorname{E}\left[\left|\sum\_{j=0}^{T-1}(Y\_{j}-\operatorname{E}[Y\_{j}])\right|^{q}\right] | ≤Cq​{(T​∑m=0T−1θm)q/2+Mq−2​T​∑m=0T−1(m+1)q−2​θm}\displaystyle\leq C\_{q}\left\{\left(T\sum\_{m=0}^{T-1}\theta\_{m}\right)^{q/2}+M^{q-2}T\sum\_{m=0}^{T-1}(m+1)^{q-2}\theta\_{m}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cq{(2TτMmax0≤j≤T−1E[|Xj|]+4TM2∑m=τ∞αq,qN(m;r1))q/2\displaystyle\leq C\_{q}\left\{\left(2T\tau M\max\_{0\leq j\leq T-1}\operatorname{E}[|X\_{j}|]+4TM^{2}\sum\_{m=\tau}^{\infty}\alpha^{N}\_{q,q}(m;r\_{1})\right)^{q/2}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +4TMq∑m=0∞(m+1)q−2αq,qN(m;r1)}.\displaystyle\left.\qquad\qquad+4TM^{q}\sum\_{m=0}^{\infty}(m+1)^{q-2}\alpha^{N}\_{q,q}(m;r\_{1})\right\}. |  |

Combining this with ([A.1](https://arxiv.org/html/2601.01871v1#A1.E1 "Equation A.1 ‣ Proof. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives the desired result.
∎

The second is an estimate for the kernel-smoothed CPCF.

###### Lemma A.2.

Suppose that KK is bounded and supported on [−1,1][-1,1].
For h∈(0,1]h\in(0,1], define a function fh:ℝ→[0,∞)f\_{h}:\mathbb{R}\to[0,\infty) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | fh​(u)=∫ℝKh​(v−u)​g​(v)​𝑑v=∫ℝK​(t)​g​(u+h​t)​𝑑t,u∈ℝ.f\_{h}(u)=\int\_{\mathbb{R}}K\_{h}(v-u)g(v)dv=\int\_{\mathbb{R}}K(t)g(u+ht)dt,\qquad u\in\mathbb{R}. |  | (A.2) |

Suppose also that there exist constants θ∗∈[−r,r]\theta^{\*}\in[-r,r], α~∈(0,1]\tilde{\alpha}\in(0,1], b>1b>1 and a function g0∈L11−α~​([−r1,r1])g\_{0}\in L^{\frac{1}{1-\tilde{\alpha}}}([-r\_{1},r\_{1}]) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(u)≤b​{g0​(u)+|u−θ∗|α~−1}for all ​u∈[−r1,r1].g(u)\leq b\left\{g\_{0}(u)+|u-\theta^{\*}|^{\tilde{\alpha}-1}\right\}\quad\text{for all }u\in[-r\_{1},r\_{1}]. |  | (A.3) |

Then we have

|  |  |  |
| --- | --- | --- |
|  | fh​(u)≤2α~​‖K‖∞​b​(‖g0‖L1/(1−α~)+2α~)​hα~−1for all u∈[−r,r].f\_{h}(u)\leq 2^{\tilde{\alpha}}\|K\|\_{\infty}b\left(\|g\_{0}\|\_{L^{1/(1-\tilde{\alpha})}}+\frac{2}{\tilde{\alpha}}\right)h^{\tilde{\alpha}-1}\quad\text{for all $u\in[-r,r]$}. |  |

###### Proof.

Fix u∈[−r,r]u\in[-r,r].
([A.3](https://arxiv.org/html/2601.01871v1#A1.E3 "Equation A.3 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives

|  |  |  |
| --- | --- | --- |
|  | fh(u)≤b(∫ℝKh(v−u)g0(v)dv+∫ℝK(t)|u−θ∗+ht|α~−1dt)=:b(I+II).\displaystyle f\_{h}(u)\leq b\left(\int\_{\mathbb{R}}K\_{h}(v-u)g\_{0}(v)dv+\int\_{\mathbb{R}}K(t)|u-\theta^{\*}+ht|^{\tilde{\alpha}-1}dt\right)=:b(I+II). |  |

Since KhK\_{h} is supported on [−h,h]⊂[−1,1][-h,h]\subset[-1,1], we can rewrite II as

|  |  |  |
| --- | --- | --- |
|  | I=∫−r1r1Kh​(v−u)​g0​(v)​𝑑v.I=\int\_{-r\_{1}}^{r\_{1}}K\_{h}(v-u)g\_{0}(v)dv. |  |

Hence, Young’s convolution inequality gives I≤‖Kh‖L1/α~​‖g0‖L1/(1−α~)I\leq\|K\_{h}\|\_{L^{1/\tilde{\alpha}}}\|g\_{0}\|\_{L^{1/(1-\tilde{\alpha})}}.
Since

|  |  |  |
| --- | --- | --- |
|  | ‖Kh‖L1/α~≤(2​h​‖Kh‖∞1/α~)α~≤2α~​hα~−1​‖K‖∞,\|K\_{h}\|\_{L^{1/\tilde{\alpha}}}\leq\left(2h\|K\_{h}\|\_{\infty}^{1/\tilde{\alpha}}\right)^{\tilde{\alpha}}\leq 2^{\tilde{\alpha}}h^{\tilde{\alpha}-1}\|K\|\_{\infty}, |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | I≤2α~​hα~−1​‖K‖∞​‖g0‖L1/(1−α~).I\leq 2^{\tilde{\alpha}}h^{\tilde{\alpha}-1}\|K\|\_{\infty}\|g\_{0}\|\_{L^{1/(1-\tilde{\alpha})}}. |  | (A.4) |

Meanwhile, for any c∈ℝc\in\mathbb{R}, a straightforward computation shows

|  |  |  |
| --- | --- | --- |
|  | ∫−11|c+h​t|α~−1​𝑑t={||c+h|α~−|c−h|α~|α~​hif ​|c|>h,|c+h|α~+|c−h|α~α~​hif ​|c|≤h.\displaystyle\int\_{-1}^{1}|c+ht|^{\tilde{\alpha}-1}dt=\begin{cases}\displaystyle\frac{\left||c+h|^{\tilde{\alpha}}-|c-h|^{\tilde{\alpha}}\right|}{\tilde{\alpha}h}&\text{if }|c|>h,\\ \displaystyle\frac{|c+h|^{\tilde{\alpha}}+|c-h|^{\tilde{\alpha}}}{\tilde{\alpha}h}&\text{if }|c|\leq h.\end{cases} |  |

Noting that |xα~−yα~|≤|x−y|α~|x^{\tilde{\alpha}}-y^{\tilde{\alpha}}|\leq|x-y|^{\tilde{\alpha}} for any x,y≥0x,y\geq 0, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | supc∈ℝ∫−11|c+h​t|α~−1​𝑑t≤21+α~α~​hα~−1.\sup\_{c\in\mathbb{R}}\int\_{-1}^{1}|c+ht|^{\tilde{\alpha}-1}dt\leq\frac{2^{1+\tilde{\alpha}}}{\tilde{\alpha}}h^{\tilde{\alpha}-1}. |  | (A.5) |

Therefore, I​I≤‖K‖∞​21+α~α~​hα~−1II\leq\|K\|\_{\infty}\frac{2^{1+\tilde{\alpha}}}{\tilde{\alpha}}h^{\tilde{\alpha}-1} since KK is supported on [−1,1][-1,1].
Combining this with ([A.4](https://arxiv.org/html/2601.01871v1#A1.E4 "Equation A.4 ‣ Proof. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives the desired result.
∎

### A.2 Proof of Proposition [3.1](https://arxiv.org/html/2601.01871v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")

In the following two lemmas, we deal with the numerator and denominator of 𝒳hrel​(ℓ)\mathcal{X}^{\mathrm{rel}}\_{h}(\ell) separately.

###### Lemma A.3.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Suppose that there exist constants θ∗∈[−r,r]\theta^{\*}\in[-r,r], α~∈(0,1]\tilde{\alpha}\in(0,1], b>1b>1 and a function g0∈L1/(1−α~)​([−r1,r1])g\_{0}\in L^{1/(1-\tilde{\alpha})}([-r\_{1},r\_{1}]) such that ([A.3](https://arxiv.org/html/2601.01871v1#A1.E3 "Equation A.3 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds.
Assume also h=hT≍T−γh=h\_{T}\asymp T^{-\gamma} as T→∞T\to\infty for some γ>0\gamma>0.
Then, for any ε>0\varepsilon>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[maxℓ∈𝒢h⁡|𝒳hraw​(ℓ)−Th​E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]|]=O​(1+T​hα~−ε).\operatorname{E}\left[\max\_{\ell\in\mathcal{G}\_{h}}\left|\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)-\frac{T}{h}\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]\right|\right]=O\left(1+\sqrt{Th^{\tilde{\alpha}-\varepsilon}}\right). |  | (A.6) |

###### Proof.

Set

|  |  |  |
| --- | --- | --- |
|  | 𝒳h0​(ℓ):=∑k=0T/h−11{N1​(Ikh)>0,N2​(Ik+ℓh)>0}.\mathcal{X}^{0}\_{h}(\ell):=\sum\_{k=0}^{T/h-1}1\_{\{N\_{1}(I\_{k}^{h})>0,\ N\_{2}(I\_{k+\ell}^{h})>0\}}. |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝒳hraw​(ℓ)−𝒳h0​(ℓ)|\displaystyle|\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)-\mathcal{X}^{0}\_{h}(\ell)| | ≤∑k=0|ℓ|−11{N1​(Ikh)>0}+∑k=T/h−|ℓ|T/h−11{N1​(Ikh)>0}\displaystyle\leq\sum\_{k=0}^{|\ell|-1}1\_{\{N\_{1}(I\_{k}^{h})>0\}}+\sum\_{k=T/h-|\ell|}^{T/h-1}1\_{\{N\_{1}(I\_{k}^{h})>0\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤N1​((0,|ℓ|​h])+N1​((T−|ℓ|​h,T]),\displaystyle\leq N\_{1}((0,|\ell|h])+N\_{1}((T-|\ell|h,T]), |  |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[maxℓ∈𝒢h⁡|𝒳hraw​(ℓ)−𝒳h0​(ℓ)|]≤E⁡[N1​((0,r])]+E⁡[N1​((T−r,T])]=2​λ1​r=O​(1).\operatorname{E}\left[\max\_{\ell\in\mathcal{G}\_{h}}|\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)-\mathcal{X}^{0}\_{h}(\ell)|\right]\leq\operatorname{E}[N\_{1}((0,r])]+\operatorname{E}[N\_{1}((T-r,T])]=2\lambda\_{1}r=O(1). |  | (A.7) |

Also, E⁡[𝒳h0​(ℓ)]=(T/h)​E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]\operatorname{E}[\mathcal{X}^{0}\_{h}(\ell)]=(T/h)\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}] by stationarity.
Therefore, ([A.6](https://arxiv.org/html/2601.01871v1#A1.E6 "Equation A.6 ‣ Lemma A.3. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) follows once we show

|  |  |  |
| --- | --- | --- |
|  | E⁡[maxℓ∈𝒢h⁡|𝒳h0​(ℓ)−E⁡[𝒳h0​(ℓ)]|]=O​(T​hα~−ε).\operatorname{E}\left[\max\_{\ell\in\mathcal{G}\_{h}}\left|\mathcal{X}^{0}\_{h}(\ell)-\operatorname{E}[\mathcal{X}^{0}\_{h}(\ell)]\right|\right]=O\left(\sqrt{Th^{\tilde{\alpha}-\varepsilon}}\right). |  |

For any p>1p>1, Jensen’s inequality gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[maxℓ∈𝒢h⁡|𝒳h0​(ℓ)−E⁡[𝒳h0​(ℓ)]|]\displaystyle\operatorname{E}\left[\max\_{\ell\in\mathcal{G}\_{h}}\left|\mathcal{X}^{0}\_{h}(\ell)-\operatorname{E}[\mathcal{X}^{0}\_{h}(\ell)]\right|\right] | ≤‖maxℓ∈𝒢h⁡|𝒳h0​(ℓ)−E⁡[𝒳h0​(ℓ)]|‖p\displaystyle\leq\left\|\max\_{\ell\in\mathcal{G}\_{h}}\left|\mathcal{X}^{0}\_{h}(\ell)-\operatorname{E}[\mathcal{X}^{0}\_{h}(\ell)]\right|\right\|\_{p} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|𝒢h|1/p​maxℓ∈𝒢h⁡‖𝒳h0​(ℓ)−E⁡[𝒳h0​(ℓ)]‖p.\displaystyle\leq|\mathcal{G}\_{h}|^{1/p}\max\_{\ell\in\mathcal{G}\_{h}}\left\|\mathcal{X}^{0}\_{h}(\ell)-\operatorname{E}[\mathcal{X}^{0}\_{h}(\ell)]\right\|\_{p}. |  |

Let pp be an even integer such that p≥4ε​(1∧γ)p\geq\frac{4}{\varepsilon(1\wedge\gamma)}. Then we have |𝒢h|1/p=O​(h−ε/4)|\mathcal{G}\_{h}|^{1/p}=O(h^{-\varepsilon/4}).
Therefore, it suffices to prove

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxℓ∈𝒢h⁡‖𝒳h0​(ℓ)−E⁡[𝒳h0​(ℓ)]‖p=O​(T​hα~−ε/2).\max\_{\ell\in\mathcal{G}\_{h}}\left\|\mathcal{X}^{0}\_{h}(\ell)-\operatorname{E}[\mathcal{X}^{0}\_{h}(\ell)]\right\|\_{p}=O\left(\sqrt{Th^{\tilde{\alpha}-\varepsilon/2}}\right). |  | (A.8) |

For each ℓ∈𝒢h\ell\in\mathcal{G}\_{h}, set

|  |  |  |
| --- | --- | --- |
|  | Yj​(ℓ):=∑k=j/h(j+1)/h−11{N1​(Ikh)>0,N2​(Ik+ℓh)>0},Y\_{j}(\ell):=\sum\_{k=j/h}^{(j+1)/h-1}1\_{\{N\_{1}(I\_{k}^{h})>0,N\_{2}(I\_{k+\ell}^{h})>0\}}, |  |

so that
𝒳h0​(ℓ)=∑j=0T−1Yj​(ℓ)\mathcal{X}^{0}\_{h}(\ell)=\sum\_{j=0}^{T-1}Y\_{j}(\ell).
Observe that Yj​(ℓ)Y\_{j}(\ell) is σ​(N∩(Ij⊕r))\sigma(N\cap(I\_{j}\oplus r))-measurable.
Also, since

|  |  |  |
| --- | --- | --- |
|  | Yj​(ℓ)≤∑k=j/h(j+1)/h−1N1​(Ikh)=N1​(Ij),\displaystyle Y\_{j}(\ell)\leq\sum\_{k=j/h}^{(j+1)/h-1}N\_{1}(I\_{k}^{h})=N\_{1}(I\_{j}), |  |

[[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | supj‖Yj​(ℓ)‖q≤‖N1​(Ij)‖q≲λ1\sup\_{j}\|Y\_{j}(\ell)\|\_{q}\leq\|N\_{1}(I\_{j})\|\_{q}\lesssim\lambda\_{1} |  | (A.9) |

for any q≥1q\geq 1.
Therefore, applying [Lemma A.1](https://arxiv.org/html/2601.01871v1#A1.Thmlemma1 "Lemma A.1. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") to (Yj​(ℓ))j=0T−1(Y\_{j}(\ell))\_{j=0}^{T-1} with M=h−ε/4M=h^{-\varepsilon/4} and τ=⌊h−ε/4⌋\tau=\lfloor h^{-\varepsilon/4}\rfloor gives

|  |  |  |
| --- | --- | --- |
|  | ∥𝒳h0(ℓ)−E[𝒳h0(ℓ)]∥p≤Cp{(Th−ε/2E[Y0(ℓ)]+Th−ε/2∑m=⌊h−ε/4⌋∞αp,pN(m;r1))1/2+T1/ph−ε/4(∑m=0∞(m+1)p−2αp,pN(m;r1))1/p}+2T∥Y0(ℓ)1{Y0​(ℓ)>h−ε/4}∥p,\left\|\mathcal{X}^{0}\_{h}(\ell)-\operatorname{E}[\mathcal{X}^{0}\_{h}(\ell)]\right\|\_{p}\leq C\_{p}\left\{\left(Th^{-\varepsilon/2}\operatorname{E}[Y\_{0}(\ell)]+Th^{-\varepsilon/2}\sum\_{m=\lfloor h^{-\varepsilon/4}\rfloor}^{\infty}\alpha^{N}\_{p,p}(m;r\_{1})\right)^{1/2}\right.\\ \left.+T^{1/p}h^{-\varepsilon/4}\left(\sum\_{m=0}^{\infty}(m+1)^{p-2}\alpha^{N}\_{p,p}(m;r\_{1})\right)^{1/p}\right\}+2T\left\|Y\_{0}(\ell)1\_{\{Y\_{0}(\ell)>h^{-\varepsilon/4}\}}\right\|\_{p}, |  |

where CpC\_{p} is a constant depending only on pp and λ1\lambda\_{1}.
By [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii),

|  |  |  |
| --- | --- | --- |
|  | ∑m=⌊h−ε/4⌋∞αp,pN​(m;r1)=O​(hα~)and∑m=0∞(m+1)p−2​αp,pN​(m;r1)=O​(1).\displaystyle\sum\_{m=\lfloor h^{-\varepsilon/4}\rfloor}^{\infty}\alpha^{N}\_{p,p}(m;r\_{1})=O(h^{\tilde{\alpha}})\quad\text{and}\quad\sum\_{m=0}^{\infty}(m+1)^{p-2}\alpha^{N}\_{p,p}(m;r\_{1})=O(1). |  |

Also, we have ‖Y0​(ℓ)​1{Y0​(ℓ)>h−ε/4}‖p≤hp​ε/4​(E⁡[Y0​(ℓ)p2+p])1/p=O​(T−1)\|Y\_{0}(\ell)1\_{\{Y\_{0}(\ell)>h^{-\varepsilon/4}\}}\|\_{p}\leq h^{p\varepsilon/4}(\operatorname{E}[Y\_{0}(\ell)^{p^{2}+p}])^{1/p}=O(T^{-1}) by ([A.9](https://arxiv.org/html/2601.01871v1#A1.E9 "Equation A.9 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
Therefore, ([A.8](https://arxiv.org/html/2601.01871v1#A1.E8 "Equation A.8 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) follows once we show

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxℓ⁡E⁡[Y0​(ℓ)]=O​(hα~).\max\_{\ell}\operatorname{E}[Y\_{0}(\ell)]=O\left(h^{\tilde{\alpha}}\right). |  | (A.10) |

Observe that

|  |  |  |
| --- | --- | --- |
|  | E⁡[Y0​(ℓ)]=h−1​E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]≤h−1​E⁡[N1​(I0h)​N2​(Iℓh)]\operatorname{E}[Y\_{0}(\ell)]=h^{-1}\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]\leq h^{-1}\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})] |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[N1​(I0h)​N2​(Iℓh)]\displaystyle\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})] | =λ1​λ2​∫ℝ21I0h​(x)​1Iℓh​(x+u)​g​(u)​𝑑x​𝑑u\displaystyle=\lambda\_{1}\lambda\_{2}\int\_{\mathbb{R}^{2}}1\_{I\_{0}^{h}}(x)1\_{I\_{\ell}^{h}}(x+u)g(u)dxdu |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =λ1​λ2​h2​∫ℝKhtri​(u−ℓ​h)​g​(u)​𝑑u.\displaystyle=\lambda\_{1}\lambda\_{2}h^{2}\int\_{\mathbb{R}}K^{\mathrm{tri}}\_{h}(u-\ell h)g(u)du. |  | (A.11) |

Therefore, ([A.10](https://arxiv.org/html/2601.01871v1#A1.E10 "Equation A.10 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) follows from [Lemma A.2](https://arxiv.org/html/2601.01871v1#A1.Thmlemma2 "Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes").
∎

###### Lemma A.4.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"). Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxℓ∈𝒢h⁡|1T​∑k=|ℓ|T/h−1−|ℓ|1{N1​(Ikh)>0}−P⁡(N1​(I0h)>0)h|=Op​(1T),maxℓ∈𝒢h⁡|1T​∑k=|ℓ|T/h−1−|ℓ|1{N2​(Ik+ℓh)>0}−P⁡(N2​(I0h)>0)h|=Op​(1T)\begin{split}&\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{1}{T}\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{1}(I\_{k}^{h})>0\}}-\frac{\operatorname{P}(N\_{1}(I\_{0}^{h})>0)}{h}\right|=O\_{p}\left(\frac{1}{\sqrt{T}}\right),\\ &\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{1}{T}\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{2}(I\_{k+\ell}^{h})>0\}}-\frac{\operatorname{P}(N\_{2}(I\_{0}^{h})>0)}{h}\right|=O\_{p}\left(\frac{1}{\sqrt{T}}\right)\end{split} |  | (A.12) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxℓ∈𝒢h⁡|1T​min⁡{∑k=|ℓ|T/h−1−|ℓ|1{N1​(Ikh)>0},∑k=|ℓ|T/h−1−|ℓ|1{N2​(Ik+ℓh)>0}}−λ1∧λ2|→p0\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{1}{T}\min\left\{\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{1}(I\_{k}^{h})>0\}},\ \sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{2}(I\_{k+\ell}^{h})>0\}}\right\}-\lambda\_{1}\wedge\lambda\_{2}\right|\to^{p}0 |  | (A.13) |

as T→∞T\to\infty.

###### Proof.

([A.13](https://arxiv.org/html/2601.01871v1#A1.E13 "Equation A.13 ‣ Lemma A.4. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) follows from (LABEL:ds-denom1) and the definition of intensity (cf. Eq.(3.3.4) of [daley2006introduction]), so it remains to prove (LABEL:ds-denom1).
We only prove the first equation of (LABEL:ds-denom1) because the second can be shown by almost the same argument.

First, the same argument as in the proof of ([A.7](https://arxiv.org/html/2601.01871v1#A1.E7 "Equation A.7 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives

|  |  |  |
| --- | --- | --- |
|  | E⁡[maxℓ∈𝒢h⁡|∑k=|ℓ|T/h−1−|ℓ|1{N1​(Ikh)>0}−∑k=0T/h−11{N1​(Ikh)>0}|]=O​(1).\displaystyle\operatorname{E}\left[\max\_{\ell\in\mathcal{G}\_{h}}\left|\sum\_{k=|\ell|}^{T/h-1-|\ell|}1\_{\{N\_{1}(I\_{k}^{h})>0\}}-\sum\_{k=0}^{T/h-1}1\_{\{N\_{1}(I\_{k}^{h})>0\}}\right|\right]=O(1). |  |

Hence it suffices to show

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​∑k=0T/h−11{N1​(Ikh)>0}=P⁡(N1​(I0h)>0)h+Op​(1T).\frac{1}{T}\sum\_{k=0}^{T/h-1}1\_{\{N\_{1}(I\_{k}^{h})>0\}}=\frac{\operatorname{P}(N\_{1}(I\_{0}^{h})>0)}{h}+O\_{p}\left(\frac{1}{\sqrt{T}}\right). |  | (A.14) |

We rewrite the left hand side as

|  |  |  |
| --- | --- | --- |
|  | 1T​∑k=0T/h−11{N1​(Ikh)>0}=1T​∑j=0T−1Xj,\frac{1}{T}\sum\_{k=0}^{T/h-1}1\_{\{N\_{1}(I\_{k}^{h})>0\}}=\frac{1}{T}\sum\_{j=0}^{T-1}X\_{j}, |  |

where Xj:=∑k=j/h(j+1)/h−11{N1​(Ikh)>0}X\_{j}:=\sum\_{k=j/h}^{(j+1)/h-1}1\_{\{N\_{1}(I\_{k}^{h})>0\}}.
Observe that XjX\_{j} is σ​(N∩Ij)\sigma(N\cap I\_{j})-measurable.
Hence,

|  |  |  |
| --- | --- | --- |
|  | Var⁡[∑j=0T−1Xj]≤∑j,m=0T−1|Cov⁡[Xj,Xj+m]|≤8​∑j,m=0T−1‖Xj‖4​‖Xm‖4​α1,1​(m;0)≲T​‖X0‖42,\displaystyle\operatorname{Var}\left[\sum\_{j=0}^{T-1}X\_{j}\right]\leq\sum\_{j,m=0}^{T-1}|\operatorname{Cov}[X\_{j},X\_{j+m}]|\leq 8\sum\_{j,m=0}^{T-1}\|X\_{j}\|\_{4}\|X\_{m}\|\_{4}\sqrt{\alpha\_{1,1}(m;0)}\lesssim T\|X\_{0}\|\_{4}^{2}, |  |

where the second inequality follows by Theorem 3 in [Doukhan1994, Section 1.2] and the third by [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii).
Since |X0|≤N1​(I0)|X\_{0}|\leq N\_{1}(I\_{0}), we obtain

|  |  |  |
| --- | --- | --- |
|  | ∑j=0T−1Xj=∑j=0T−1E⁡[Xj]+Op​(T)=Th​E⁡[1{N1​(I0h)>0}]+Op​(T).\sum\_{j=0}^{T-1}X\_{j}=\sum\_{j=0}^{T-1}\operatorname{E}[X\_{j}]+O\_{p}(\sqrt{T})=\frac{T}{h}\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0\}}]+O\_{p}(\sqrt{T}). |  |

Since E⁡[1{N1​(I0h)>0}]=P⁡(N1​(I0h)>0)\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0\}}]=\operatorname{P}(N\_{1}(I\_{0}^{h})>0), we obtain ([A.14](https://arxiv.org/html/2601.01871v1#A1.E14 "Equation A.14 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
∎

###### Proof of [Proposition 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").

Since gg is bounded, ([A.3](https://arxiv.org/html/2601.01871v1#A1.E3 "Equation A.3 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds for b=supx∈ℝ|g​(x)|b=\sup\_{x\in\mathbb{R}}|g(x)|, α~=1\tilde{\alpha}=1 and g0≡0g\_{0}\equiv 0 (with θ∗\theta^{\*} arbitrary).
Also, by assumption, T​hα~+ε→∞Th^{\tilde{\alpha}+\varepsilon}\to\infty as T→∞T\to\infty for some ε>0\varepsilon>0.
Hence, [Lemma A.3](https://arxiv.org/html/2601.01871v1#A1.Thmlemma3 "Lemma A.3. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxℓ∈𝒢h⁡|𝒳hraw​(ℓ)T​h−E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]h2|→p0.\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)}{Th}-\frac{\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]}{h^{2}}\right|\to^{p}0. |  | (A.15) |

This particularly gives maxℓ∈𝒢h⁡𝒳hraw​(ℓ)/T​h=Op​(1)\max\_{\ell\in\mathcal{G}\_{h}}\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)/Th=O\_{p}(1).
Combining this with ([A.13](https://arxiv.org/html/2601.01871v1#A1.E13 "Equation A.13 ‣ Lemma A.4. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives

|  |  |  |
| --- | --- | --- |
|  | maxℓ∈𝒢h⁡|𝒳hrel​(ℓ)h−1λ1∧λ2​E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]h2|→p0.\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)}{h}-\frac{1}{\lambda\_{1}\wedge\lambda\_{2}}\frac{\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]}{h^{2}}\right|\to^{p}0. |  |

Since λ1​λ2/(λ1∧λ2)=λ1∨λ2\lambda\_{1}\lambda\_{2}/(\lambda\_{1}\wedge\lambda\_{2})=\lambda\_{1}\vee\lambda\_{2}, we complete the proof once we show

|  |  |  |
| --- | --- | --- |
|  | maxℓ∈𝒢h⁡|E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]h2−λ1​λ2​∫ℝKhtri​(u−ℓ​h)​g​(u)​𝑑u|=o​(1).\displaystyle\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]}{h^{2}}-\lambda\_{1}\lambda\_{2}\int\_{\mathbb{R}}K^{\mathrm{tri}}\_{h}(u-\ell h)g(u)du\right|=o(1). |  |

Observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≤E⁡[N1​(I0h)​N2​(Iℓh)]−E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]\displaystyle\leq\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})]-\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E⁡[(N1​(I0h)−1)+⋅N2​(Iℓh)]+E⁡[1{N1​(I0h)>0}​(N2​(Iℓh)−1)+]\displaystyle=\operatorname{E}[(N\_{1}(I\_{0}^{h})-1)\_{+}\cdot N\_{2}(I\_{\ell}^{h})]+\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0\}}(N\_{2}(I\_{\ell}^{h})-1)\_{+}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E⁡[N1​(I0h)​(N1​(I0h)−1)+⋅N2​(Iℓh)]+E⁡[N1​(I0h)​N2​(Iℓh)​(N2​(Iℓh)−1)+]\displaystyle\leq\operatorname{E}[N\_{1}(I\_{0}^{h})(N\_{1}(I\_{0}^{h})-1)\_{+}\cdot N\_{2}(I\_{\ell}^{h})]+\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})(N\_{2}(I\_{\ell}^{h})-1)\_{+}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E⁡[N1​(I0h)​(N1​(I0h)−1)​N2​(Iℓh)]+E⁡[N1​(I0h)​N2​(Iℓh)​(N2​(Iℓh)−1)].\displaystyle=\operatorname{E}[N\_{1}(I\_{0}^{h})(N\_{1}(I\_{0}^{h})-1)N\_{2}(I\_{\ell}^{h})]+\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})(N\_{2}(I\_{\ell}^{h})-1)]. |  |

Since we assume ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")) for ϖ=1\varpi=1, we obtain

|  |  |  |
| --- | --- | --- |
|  | maxℓ∈𝒢h⁡|E⁡[N1​(I0h)​N2​(Iℓh)]−E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]|=o​(h2).\max\_{\ell\in\mathcal{G}\_{h}}\left|\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})]-\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]\right|=o(h^{2}). |  |

Combining this with ([A.11](https://arxiv.org/html/2601.01871v1#A1.E11 "Equation A.11 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives the desired result.
∎

### A.3 Proof of Theorem [3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")

The following lemma summarizes identifiability conditions implied by [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").

###### Lemma A.5.

Assume [[K]](https://arxiv.org/html/2601.01871v1#S4.I1.i1 "Item [K] ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") and define the function fhf\_{h} as in ([A.2](https://arxiv.org/html/2601.01871v1#A1.E2 "Equation A.2 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).

1. (a)

   Assume [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](i)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i1 "Item [A2](i) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"). Then, for some σ∈{−1,1}\sigma\in\{-1,1\}, there exist constants A>1A>1 and 0<h0<10<h\_{0}<1 depending only on α,b,δ\alpha,b,\delta such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | fh​(θ∗+σ​v)−supu∈[−r,r]:|u−θ∗|>A​hfh​(u)≥hα−1for all h<h0 and v∈[h,2​h].f\_{h}(\theta^{\*}+\sigma v)-\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u)\geq h^{\alpha-1}\quad\text{for all $h<h\_{0}$ and $v\in[h,2h]$}. |  | (A.16) |
2. (b)

   Assume [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")[[A2](ii)](https://arxiv.org/html/2601.01871v1#S3.I2.i1.I1.i2 "Item [A2](ii) ‣ Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
   Then, for some σ∈{−1,1}\sigma\in\{-1,1\}, there exist constants A>1,c>0A>1,c>0 and 0<h0<10<h\_{0}<1 depending only on α,α0,b,δ,K\alpha,\alpha\_{0},b,\delta,K such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | fh​(θ∗+σ​v)−supu∈[−r,r]:|u−θ∗|>A​hfh​(u)≥c​hα−1for all h<h0 and v∈[0,h].f\_{h}(\theta^{\*}+\sigma v)-\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u)\geq ch^{\alpha-1}\quad\text{for all $h<h\_{0}$ and $v\in[0,h]$.} |  | (A.17) |

###### Proof.

[(a)](https://arxiv.org/html/2601.01871v1#A1.I1.i1 "Item (a) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") By assumption, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup0<σ​(u−θ∗)<δg​(θ∗)−g​(u)|u−θ∗|α−1≤b\sup\_{0<\sigma(u-\theta^{\*})<\delta}\frac{g(\theta^{\*})-g(u)}{|u-\theta^{\*}|^{\alpha-1}}\leq b |  | (A.18) |

for some σ∈{−1,1}\sigma\in\{-1,1\}.
Also, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(u)≤g​(θ∗)−b−1​min⁡{1,|u−θ∗|α−1}g(u)\leq g(\theta^{\*})-b^{-1}\min\left\{1,|u-\theta^{\*}|^{\alpha-1}\right\} |  | (A.19) |

for all u∈ℝu\in\mathbb{R}.
Now, for any A>1A>1, we have by [[K]](https://arxiv.org/html/2601.01871v1#S4.I1.i1 "Item [K] ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") and ([A.19](https://arxiv.org/html/2601.01871v1#A1.E19 "Equation A.19 ‣ Proof. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | supu∈[−r,r]:|u−θ∗|>A​hfh​(u)\displaystyle\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u) | ≤g​(θ∗)−b−1​supu∈[−r,r]:|u−θ∗|>A​h∫−11K​(t)​min⁡{1,|u−θ∗+h​t|α−1}​𝑑t\displaystyle\leq g(\theta^{\*})-b^{-1}\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}\int\_{-1}^{1}K(t)\min\left\{1,|u-\theta^{\*}+ht|^{\alpha-1}\right\}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤g​(θ∗)−b−1​min⁡{1,(A−1)α−1​hα−1}.\displaystyle\leq g(\theta^{\*})-b^{-1}\min\left\{1,(A-1)^{\alpha-1}h^{\alpha-1}\right\}. |  |

Meanwhile, by ([A.18](https://arxiv.org/html/2601.01871v1#A1.E18 "Equation A.18 ‣ Proof. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")), we have for all h<δ/3h<\delta/3 and v∈[h,2​h]v\in[h,2h],

|  |  |  |
| --- | --- | --- |
|  | fh​(θ∗+σ​v)≥g​(θ∗)−b​∫−11K​(t)​|σ​v+h​t|α−1​𝑑t≥g​(θ∗)−b​(3​h)α−1.\displaystyle f\_{h}(\theta^{\*}+\sigma v)\geq g(\theta^{\*})-b\int\_{-1}^{1}K(t)|\sigma v+ht|^{\alpha-1}dt\geq g(\theta^{\*})-b(3h)^{\alpha-1}. |  |

Combining these estimates gives

|  |  |  |
| --- | --- | --- |
|  | fh​(θ∗+σ​v)−supu∈[−r,r]:|u−θ∗|>A​hfh​(u)≥b−1​min⁡{1,(A−1)α−1​hα−1}−b​(3​h)α−1.\displaystyle f\_{h}(\theta^{\*}+\sigma v)-\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u)\geq b^{-1}\min\left\{1,(A-1)^{\alpha-1}h^{\alpha-1}\right\}-b(3h)^{\alpha-1}. |  |

Therefore, if A≥1+(b+3α−1​b2)1/(α−1)A\geq 1+(b+3^{\alpha-1}b^{2})^{1/(\alpha-1)} and h<min⁡{δ/3,{b​(3α−1​b+1)}−1/(α−1)}h<\min\{\delta/3,\,\{b(3^{\alpha-1}b+1)\}^{-1/(\alpha-1)}\}, we have ([A.16](https://arxiv.org/html/2601.01871v1#A1.E16 "Equation A.16 ‣ Item (a) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).

[(b)](https://arxiv.org/html/2601.01871v1#A1.I1.i2 "Item (b) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") By assumption, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf0<σ​(u−θ∗)<δg​(u)|u−θ∗|α−1≥1b\inf\_{0<\sigma(u-\theta^{\*})<\delta}\frac{g(u)}{|u-\theta^{\*}|^{\alpha-1}}\geq\frac{1}{b} |  | (A.20) |

for some σ∈{−1,1}\sigma\in\{-1,1\}.
Also, we have inft∈[−δ0,δ0]K​(t)≥K​(0)/2>0\inf\_{t\in[-\delta\_{0},\delta\_{0}]}K(t)\geq K(0)/2>0 for some 0<δ0<10<\delta\_{0}<1 by [[K]](https://arxiv.org/html/2601.01871v1#S4.I1.i1 "Item [K] ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").
Combining this with ([A.20](https://arxiv.org/html/2601.01871v1#A1.E20 "Equation A.20 ‣ Proof. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")), we have for all h<δ/2h<\delta/2 and v∈[0,h]v\in[0,h]

|  |  |  |
| --- | --- | --- |
|  | fh​(θ∗+σ​v)≥K​(0)2​b​∫0δ0|v+h​t|α−1​𝑑t≥K​(0)2​b​hα−1​∫0δ0(1+t)α−1​𝑑t≥K​(0)​δ04​b​hα−1.\displaystyle f\_{h}(\theta^{\*}+\sigma v)\geq\frac{K(0)}{2b}\int\_{0}^{\delta\_{0}}|v+ht|^{\alpha-1}dt\geq\frac{K(0)}{2b}h^{\alpha-1}\int\_{0}^{\delta\_{0}}(1+t)^{\alpha-1}dt\geq\frac{K(0)\delta\_{0}}{4b}h^{\alpha-1}. |  |

Meanwhile, applying ([A.4](https://arxiv.org/html/2601.01871v1#A1.E4 "Equation A.4 ‣ Proof. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) to α~=α0\tilde{\alpha}=\alpha\_{0} gives

|  |  |  |
| --- | --- | --- |
|  | ∫ℝKh​(v−u)​g0​(v)​𝑑v≤2α0​hα0−1​‖K‖∞​b.\int\_{\mathbb{R}}K\_{h}(v-u)g\_{0}(v)dv\leq 2^{\alpha\_{0}}h^{\alpha\_{0}-1}\|K\|\_{\infty}b. |  |

Hence, for any A>1A>1, we have by [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[K]](https://arxiv.org/html/2601.01871v1#S4.I1.i1 "Item [K] ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")

|  |  |  |  |
| --- | --- | --- | --- |
|  | supu∈[−r,r]:|u−θ∗|>A​hfh​(u)\displaystyle\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u) | ≤b​‖K‖∞​(2α0​hα0−1​b+supu∈[−r,r]:|u−θ∗|>A​h∫−11|u−θ∗+h​t|α−1​𝑑t)\displaystyle\leq b\|K\|\_{\infty}\left(2^{\alpha\_{0}}h^{\alpha\_{0}-1}b+\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}\int\_{-1}^{1}|u-\theta^{\*}+ht|^{\alpha-1}dt\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​b​‖K‖∞​(b​hα0−1+hα−1(A−1)1−α).\displaystyle\leq 2b\|K\|\_{\infty}\left(bh^{\alpha\_{0}-1}+\frac{h^{\alpha-1}}{(A-1)^{1-\alpha}}\right). |  |

Therefore, if AA is sufficiently large such that

|  |  |  |
| --- | --- | --- |
|  | 2​‖K‖∞​b(A−1)1−α≤K​(0)​δ08​b,\frac{2\|K\|\_{\infty}b}{(A-1)^{1-\alpha}}\leq\frac{K(0)\delta\_{0}}{8b}, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | fh​(θ∗+σ​v)−supu∈[−r,r]:|u−θ∗|>A​hfh​(u)≥K​(0)​δ08​b​hα−1−2​b2​‖K‖∞​hα0−1.\displaystyle f\_{h}(\theta^{\*}+\sigma v)-\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u)\geq\frac{K(0)\delta\_{0}}{8b}h^{\alpha-1}-2b^{2}\|K\|\_{\infty}h^{\alpha\_{0}-1}. |  |

Consequently, ([A.17](https://arxiv.org/html/2601.01871v1#A1.E17 "Equation A.17 ‣ Item (b) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds if

|  |  |  |
| --- | --- | --- |
|  | h0≤min⁡{δ2,(K​(0)​δ032​‖K‖∞​b3)1/(α0−α)}andc≤K​(0)​δ016​b.h\_{0}\leq\min\left\{\frac{\delta}{2},\ \left(\frac{K(0)\delta\_{0}}{32\|K\|\_{\infty}b^{3}}\right)^{1/(\alpha\_{0}-\alpha)}\right\}\quad\text{and}\quad c\leq\frac{K(0)\delta\_{0}}{16b}. |  |

This completes the proof.
∎

###### Proof of [Theorem 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").

Observe that ([A.3](https://arxiv.org/html/2601.01871v1#A1.E3 "Equation A.3 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds for α~=α∧1\tilde{\alpha}=\alpha\wedge 1 under [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Hence, [Lemma A.3](https://arxiv.org/html/2601.01871v1#A1.Thmlemma3 "Lemma A.3. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") gives

|  |  |  |
| --- | --- | --- |
|  | h1−α​maxℓ∈𝒢h⁡|𝒳hraw​(ℓ)T​h−E​[1{N1​(I0h)>0,N2​(Iℓh)>0}]h2|=O​(hαT+1T​hβα+ε)for any ​ε>0,h^{1-\alpha}\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)}{Th}-\frac{E[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]}{h^{2}}\right|=O\left(\frac{h^{\alpha}}{T}+\frac{1}{\sqrt{Th^{\beta\_{\alpha}+\varepsilon}}}\right)\quad\text{for any }\varepsilon>0, |  |

where we used the identity 2​α−α∧1=βα2\alpha-\alpha\wedge 1=\beta\_{\alpha}.
Also, by the proof of [Proposition 3.1](https://arxiv.org/html/2601.01871v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and ([3.4](https://arxiv.org/html/2601.01871v1#S3.E4 "Equation 3.4 ‣ Proposition 3.1. ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")),

|  |  |  |
| --- | --- | --- |
|  | maxℓ∈𝒢h⁡|E⁡[N1​(I0h)​N2​(Iℓh)]−E⁡[1{N1​(I0h)>0,N2​(Iℓh)>0}]|h2=o​(hα−1).\max\_{\ell\in\mathcal{G}\_{h}}\frac{\left|\operatorname{E}[N\_{1}(I\_{0}^{h})N\_{2}(I\_{\ell}^{h})]-\operatorname{E}[1\_{\{N\_{1}(I\_{0}^{h})>0,N\_{2}(I\_{\ell}^{h})>0\}}]\right|}{h^{2}}=o(h^{\alpha-1}). |  |

Now, define the function fhf\_{h} in ([A.2](https://arxiv.org/html/2601.01871v1#A1.E2 "Equation A.2 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) with K=KtriK=K^{\mathrm{tri}}.
Recall that h≍T−γh\asymp T^{-\gamma} with 0<γ<1/βα0<\gamma<1/\beta\_{\alpha}.
Therefore, combining the above two equations with ([A.11](https://arxiv.org/html/2601.01871v1#A1.E11 "Equation A.11 ‣ Proof. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")), we obtain

|  |  |  |
| --- | --- | --- |
|  | h1−α​maxℓ∈𝒢h⁡|𝒳hraw​(ℓ)T​h−λ1​λ2​fh​(ℓ​h)|→p0.h^{1-\alpha}\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)}{Th}-\lambda\_{1}\lambda\_{2}f\_{h}(\ell h)\right|\to^{p}0. |  |

Combining this with [Lemma A.2](https://arxiv.org/html/2601.01871v1#A1.Thmlemma2 "Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") particularly gives maxℓ∈𝒢h⁡𝒳hraw​(ℓ)/T​h=Op​(hα~−1)\max\_{\ell\in\mathcal{G}\_{h}}\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)/Th=O\_{p}(h^{\tilde{\alpha}-1}).
Hence, by [Lemma A.4](https://arxiv.org/html/2601.01871v1#A1.Thmlemma4 "Lemma A.4. ‣ A.2 Proof of Proposition 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"),

|  |  |  |
| --- | --- | --- |
|  | h1−α​maxℓ∈𝒢h⁡|P⁡(N1​(I0h)>0)∧P⁡(N2​(I0h)>0)h2​𝒳hrel​(ℓ)−𝒳hraw​(ℓ)T​h|→p0.h^{1-\alpha}\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\operatorname{P}(N\_{1}(I\_{0}^{h})>0)\wedge\operatorname{P}(N\_{2}(I\_{0}^{h})>0)}{h^{2}}\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)-\frac{\mathcal{X}^{\mathrm{raw}}\_{h}(\ell)}{Th}\right|\to^{p}0. |  |

Therefore, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | h1−α​Δ¯T→p0asT→∞,h^{1-\alpha}\bar{\Delta}\_{T}\to^{p}0\qquad\text{as}\quad T\to\infty, |  | (A.21) |

where

|  |  |  |
| --- | --- | --- |
|  | Δ¯T:=maxℓ∈𝒢h⁡|P⁡(N1​(I0h)>0)∧P⁡(N2​(I0h)>0)λ1​λ2​h2​𝒳hrel​(ℓ)−fh​(ℓ​h)|.\bar{\Delta}\_{T}:=\max\_{\ell\in\mathcal{G}\_{h}}\left|\frac{\operatorname{P}(N\_{1}(I\_{0}^{h})>0)\wedge\operatorname{P}(N\_{2}(I\_{0}^{h})>0)}{\lambda\_{1}\lambda\_{2}h^{2}}\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)-f\_{h}(\ell h)\right|. |  |

We turn to the main body of the proof.
Consider the case α>1\alpha>1.
Then, by [Lemma A.5](https://arxiv.org/html/2601.01871v1#A1.Thmlemma5 "Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"), for some σ∈{−1,1}\sigma\in\{-1,1\}, there exist constants A>1A>1 and 0<h0<10<h\_{0}<1 depending only on α,b,δ\alpha,b,\delta such that ([A.16](https://arxiv.org/html/2601.01871v1#A1.E16 "Equation A.16 ‣ Item (a) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds.
We can find an integer ℓ∗\ell^{\*} such that ℓ∗​h=θ∗+σ​v\ell^{\*}h=\theta^{\*}+\sigma v for some v∈[h,2​h]v\in[h,2h].
Observe that ℓ∗∈𝒢h\ell^{\*}\in\mathcal{G}\_{h} for sufficiently small hh.
Then, since θ^hD​S\hat{\theta}\_{h}^{DS} is a maximizer of 𝒢h∋ℓ↦𝒳hrel​(ℓ)∈[0,∞)\mathcal{G}\_{h}\ni\ell\mapsto\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)\in[0,\infty), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | P⁡(|θ^hD​S−θ∗|>(A+4)​h)\displaystyle\operatorname{P}\left(|\hat{\theta}\_{h}^{DS}-\theta^{\*}|>(A+4)h\right) | ≤P⁡(|θ^hD​S−ℓ∗​h|>(A+2)​h)\displaystyle\leq\operatorname{P}\left(|\hat{\theta}\_{h}^{DS}-\ell^{\*}h|>(A+2)h\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤P⁡(𝒳hrel​(ℓ∗)≤maxℓ∈𝒢h:|ℓ−ℓ∗|>A+2⁡𝒳hrel​(ℓ))\displaystyle\leq\operatorname{P}\left(\mathcal{X}^{\mathrm{rel}}\_{h}(\ell^{\*})\leq\max\_{\ell\in\mathcal{G}\_{h}:|\ell-\ell^{\*}|>A+2}\mathcal{X}^{\mathrm{rel}}\_{h}(\ell)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤P⁡(fh​(ℓ∗​h)≤maxℓ∈𝒢h:|ℓ−ℓ∗|>A+2⁡fh​(ℓ​h)+2​Δ¯T)\displaystyle\leq\operatorname{P}\left(f\_{h}(\ell^{\*}h)\leq\max\_{\ell\in\mathcal{G}\_{h}:|\ell-\ell^{\*}|>A+2}f\_{h}(\ell h)+2\bar{\Delta}\_{T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤P⁡(fh​(ℓ∗​h)≤maxℓ∈𝒢h:|ℓ​h−θ∗|>A​h⁡fh​(ℓ​h)+2​Δ¯T).\displaystyle\leq\operatorname{P}\left(f\_{h}(\ell^{\*}h)\leq\max\_{\ell\in\mathcal{G}\_{h}:|\ell h-\theta^{\*}|>Ah}f\_{h}(\ell h)+2\bar{\Delta}\_{T}\right). |  |

Hence, ([A.16](https://arxiv.org/html/2601.01871v1#A1.E16 "Equation A.16 ‣ Item (a) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives P⁡(|θ^hD​S−θ∗|>(A+4)​h)≤P⁡(2​Δ¯T≥hα−1)\operatorname{P}(|\hat{\theta}\_{h}^{DS}-\theta^{\*}|>(A+4)h)\leq\operatorname{P}\left(2\bar{\Delta}\_{T}\geq h^{\alpha-1}\right).
Thus we obtain the desired result by ([A.21](https://arxiv.org/html/2601.01871v1#A1.E21 "Equation A.21 ‣ Proof of Theorem 3.1. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).

Next, consider the case α<1\alpha<1.
Then, by [Lemma A.5](https://arxiv.org/html/2601.01871v1#A1.Thmlemma5 "Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"), for some σ∈{−1,1}\sigma\in\{-1,1\}, there exist constants A>1,c>0A>1,c>0 and 0<h0<10<h\_{0}<1 depending only on α,α0,b,δ\alpha,\alpha\_{0},b,\delta such that ([A.17](https://arxiv.org/html/2601.01871v1#A1.E17 "Equation A.17 ‣ Item (b) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds.
We can find an integer ℓ∗\ell^{\*} such that ℓ∗​h=θ∗+σ​v\ell^{\*}h=\theta^{\*}+\sigma v for some v∈[0,h]v\in[0,h].
Then, a similar argument to the above shows P⁡(|θ^hD​S−θ∗|>(A+2)​h)→0\operatorname{P}(|\hat{\theta}\_{h}^{DS}-\theta^{\*}|>(A+2)h)\to 0 as T→∞T\to\infty.
∎

### A.4 Proof of Theorem [4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")

Set α~:=α∧1\tilde{\alpha}:=\alpha\wedge 1.
Note that α~≤βα\tilde{\alpha}\leq\beta\_{\alpha}.
Since the left hand side of ([4.1](https://arxiv.org/html/2601.01871v1#S4.E1 "Equation 4.1 ‣ Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")) is always bounded by 1, we may assume T​hβα+ε≥1Th^{\beta\_{\alpha}+\varepsilon}\geq 1 without loss of generality.

Let us consider the following statistic:

|  |  |  |
| --- | --- | --- |
|  | g~h​(u):=n1T​λ1​n2T​λ2​g^h​(u)=1T​λ1​λ2​∫(0,T]2Kh​(y−x−u)​N1​(d​x)​N2​(d​y),u∈ℝ.\tilde{g}\_{h}(u):=\frac{n\_{1}}{T\lambda\_{1}}\frac{n\_{2}}{T\lambda\_{2}}\hat{g}\_{h}(u)=\frac{1}{T\lambda\_{1}\lambda\_{2}}\int\_{(0,T]^{2}}K\_{h}(y-x-u)N\_{1}(dx)N\_{2}(dy),\quad u\in\mathbb{R}. |  |

Observe that θ^h\hat{\theta}\_{h} is also a maximizer of g~h​(u)\tilde{g}\_{h}(u) over u∈[−r,r]u\in[-r,r].
Also, we can rewrite it as g~h​(u)=∑j=0T−1Xj0​(u)\tilde{g}\_{h}(u)=\sum\_{j=0}^{T-1}X^{0}\_{j}(u), where

|  |  |  |
| --- | --- | --- |
|  | Xj0​(u)=1T​λ1​λ2​∫Ij×(0,T]Kh​(y−x−u)​N1​(d​x)​N2​(d​y).X^{0}\_{j}(u)=\frac{1}{T\lambda\_{1}\lambda\_{2}}\int\_{I\_{j}\times(0,T]}K\_{h}(y-x-u)N\_{1}(dx)N\_{2}(dy). |  |

We introduce an edge-corrected version of Xj0​(u)X\_{j}^{0}(u) as

|  |  |  |
| --- | --- | --- |
|  | Xj​(u)=1T​λ1​λ2​∫Ij×ℝKh​(y−x−u)​N1​(d​x)​N2​(d​y).X\_{j}(u)=\frac{1}{T\lambda\_{1}\lambda\_{2}}\int\_{I\_{j}\times\mathbb{R}}K\_{h}(y-x-u)N\_{1}(dx)N\_{2}(dy). |  |

It is not difficult to see that (Xj​(u))j∈ℤ(X\_{j}(u))\_{j\in\mathbb{Z}} is stationary.
We first show that replacing Xj0​(u)X\_{j}^{0}(u) by Xj​(u)X\_{j}(u) does not matter for our argument.

###### Lemma A.6.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Assume also that KK is bounded and supported on [−1,1][-1,1].
Then,

|  |  |  |
| --- | --- | --- |
|  | E⁡[supu∈[−r,r]|g~h​(u)−∑j=0T−1Xj​(u)|]≲1T​h.\operatorname{E}\left[\sup\_{u\in[-r,r]}\left|\tilde{g}\_{h}(u)-\sum\_{j=0}^{T-1}X\_{j}(u)\right|\right]\lesssim\frac{1}{Th}. |  |

###### Proof.

Since KhK\_{h} is supported on [−h,h]⊂[−1,1][-h,h]\subset[-1,1], Xj0​(u)=Xj​(u)X\_{j}^{0}(u)=X\_{j}(u) if r1<j<T−1−r1r\_{1}<j<T-1-r\_{1} for any u∈[−r,r]u\in[-r,r].
Therefore,

|  |  |  |
| --- | --- | --- |
|  | |g~h​(u)−∑j=0T−1Xj​(u)|≤‖K‖∞T​h​λ1​λ2​∑0≤j≤r1​ or ​T−1−r1≤j≤T−1N1​(Ij)​N2​(Ij⊕r1).\displaystyle\left|\tilde{g}\_{h}(u)-\sum\_{j=0}^{T-1}X\_{j}(u)\right|\leq\frac{\|K\|\_{\infty}}{Th\lambda\_{1}\lambda\_{2}}\sum\_{0\leq j\leq r\_{1}\text{ or }T-1-r\_{1}\leq j\leq T-1}N\_{1}(I\_{j})N\_{2}(I\_{j}\oplus r\_{1}). |  |

Hence, the desired result follows by [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i).
∎

Next, set

|  |  |  |
| --- | --- | --- |
|  | ΔT​(u):=∑j=0T−1{Xj​(u)−E⁡[Xj​(u)]},u∈[−r,r].\Delta\_{T}(u):=\sum\_{j=0}^{T-1}\left\{X\_{j}(u)-\operatorname{E}[X\_{j}(u)]\right\},\qquad u\in[-r,r]. |  |

Our next aim is to establish a sufficiently fast convergence of supu∈[−r,r]|ΔT​(u)|\sup\_{u\in[-r,r]}|\Delta\_{T}(u)|.
We first develop pointwise moment bounds.

###### Lemma A.7.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Assume also that KK is bounded and supported on [−1,1][-1,1].
If an even integer p>2p>2 satisfies T​hp​ε/4≤1Th^{p\varepsilon/4}\leq 1, then

|  |  |  |
| --- | --- | --- |
|  | h1−α~​supu∈[−r,r]‖ΔT​(u)‖p≲CpT​hα~+ε/2,\displaystyle h^{1-\tilde{\alpha}}\sup\_{u\in[-r,r]}\left\|\Delta\_{T}(u)\right\|\_{p}\lesssim\frac{C\_{p}}{\sqrt{Th^{\tilde{\alpha}+\varepsilon/2}}}, |  |

where CpC\_{p} is a constant depending only on pp.

###### Proof.

Fix u∈[−r,r]u\in[-r,r].
Since KhK\_{h} is supported on [−h,h]⊂[−1,1][-h,h]\subset[-1,1], we can rewrite Xj​(u)X\_{j}(u) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xj​(u)=1T​λ1​λ2​∫Ij×(Ij⊕r1)Kh​(y−x−u)​N1​(d​x)​N2​(d​y).X\_{j}(u)=\frac{1}{T\lambda\_{1}\lambda\_{2}}\int\_{I\_{j}\times(I\_{j}\oplus r\_{1})}K\_{h}(y-x-u)N\_{1}(dx)N\_{2}(dy). |  | (A.22) |

Hence, Xj​(u)X\_{j}(u) is σ​(N∩(Ij⊕r1))\sigma(N\cap(I\_{j}\oplus r\_{1}))-measurable for every jj.
Also, since ‖Kh‖∞≤h−1​‖K‖∞\|K\_{h}\|\_{\infty}\leq h^{-1}\|K\|\_{\infty}, we obtain for any q>1q>1

|  |  |  |  |
| --- | --- | --- | --- |
|  | max0≤j≤T−1⁡‖Xj​(u)‖q=‖X0​(u)‖q≲1T​h​λ1​λ2​‖N1​(I0)​N2​(I0⊕r1)‖q≲1T​h.\max\_{0\leq j\leq T-1}\|X\_{j}(u)\|\_{q}=\|X\_{0}(u)\|\_{q}\lesssim\frac{1}{Th\lambda\_{1}\lambda\_{2}}\|N\_{1}(I\_{0})N\_{2}(I\_{0}\oplus r\_{1})\|\_{q}\lesssim\frac{1}{Th}. |  | (A.23) |

Therefore, applying [Lemma A.1](https://arxiv.org/html/2601.01871v1#A1.Thmlemma1 "Lemma A.1. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") to (Xj​(u))j=0T−1(X\_{j}(u))\_{j=0}^{T-1} with M=h−ε/4/(T​h)M=h^{-\varepsilon/4}/(Th) and τ=⌊h−ε/4⌋\tau=\lfloor h^{-\varepsilon/4}\rfloor gives

|  |  |  |
| --- | --- | --- |
|  | ∥ΔT(u)∥p≤Cp{(h−ε/2hE[|X0(u)|]+h−ε/2T​h2∑m=⌊h−ε/4⌋∞αp,pN(m;r1))1/2+T1/p​h−ε/4T​h(∑m=0∞(m+1)p−2αp,pN(m;r1))1/p}+2T∥X0(u)1{X0​(u)>h−ε/4/(T​h)}∥p,\left\|\Delta\_{T}(u)\right\|\_{p}\leq C\_{p}\left\{\left(\frac{h^{-\varepsilon/2}}{h}\operatorname{E}[|X\_{0}(u)|]+\frac{h^{-\varepsilon/2}}{Th^{2}}\sum\_{m=\lfloor h^{-\varepsilon/4}\rfloor}^{\infty}\alpha^{N}\_{p,p}(m;r\_{1})\right)^{1/2}\right.\\ \left.+\frac{T^{1/p}h^{-\varepsilon/4}}{Th}\left(\sum\_{m=0}^{\infty}(m+1)^{p-2}\alpha^{N}\_{p,p}(m;r\_{1})\right)^{1/p}\right\}+2T\left\|X\_{0}(u)1\_{\{X\_{0}(u)>h^{-\varepsilon/4}/(Th)\}}\right\|\_{p}, |  |

where CpC\_{p} is a constant depending only on pp.
By [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii),

|  |  |  |
| --- | --- | --- |
|  | ∑m=⌊h−ε/4⌋∞αp,pN​(m;r1)≲hα~and∑m=0∞(m+1)p−2​αp,pN​(m;r1)≲1.\displaystyle\sum\_{m=\lfloor h^{-\varepsilon/4}\rfloor}^{\infty}\alpha^{N}\_{p,p}(m;r\_{1})\lesssim h^{\tilde{\alpha}}\quad\text{and}\quad\sum\_{m=0}^{\infty}(m+1)^{p-2}\alpha^{N}\_{p,p}(m;r\_{1})\lesssim 1. |  |

Also, since ([A.3](https://arxiv.org/html/2601.01871v1#A1.E3 "Equation A.3 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds under [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes"), Campbell’s formula and [Lemma A.2](https://arxiv.org/html/2601.01871v1#A1.Thmlemma2 "Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") give

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[X0​(u)]=1T​∫−11K​(t)​g​(u+h​t)​𝑑t≲1T​∫−11(1+|u−θ∗+h​t|α~−1)​𝑑t≲1T​h1−α~.\operatorname{E}[X\_{0}(u)]=\frac{1}{T}\int\_{-1}^{1}K(t)g(u+ht)dt\lesssim\frac{1}{T}\int\_{-1}^{1}\left(1+|u-\theta^{\*}+ht|^{\tilde{\alpha}-1}\right)dt\lesssim\frac{1}{Th^{1-\tilde{\alpha}}}. |  | (A.24) |

Moreover, by ([A.23](https://arxiv.org/html/2601.01871v1#A1.E23 "Equation A.23 ‣ Proof. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")),

|  |  |  |
| --- | --- | --- |
|  | ‖X0​(u)​1{X0​(u)>h−ε/4/(T​h)}‖p≤(T​hh−ε/4)p​(E⁡[X0​(u)p2+p])1/p≲hp​ε/4T​h.\displaystyle\left\|X\_{0}(u)1\_{\{X\_{0}(u)>h^{-\varepsilon/4}/(Th)\}}\right\|\_{p}\leq\left(\frac{Th}{h^{-\varepsilon/4}}\right)^{p}(\operatorname{E}[X\_{0}(u)^{p^{2}+p}])^{1/p}\lesssim\frac{h^{p\varepsilon/4}}{Th}. |  |

Since T​hp​ε/4≤1Th^{p\varepsilon/4}\leq 1, we obtain

|  |  |  |
| --- | --- | --- |
|  | h1−α~​‖ΔT​(u)‖p≲Cp​(1T​hα~+ε/2+1T​hα~+ε/2).\displaystyle h^{1-\tilde{\alpha}}\left\|\Delta\_{T}(u)\right\|\_{p}\lesssim C\_{p}\left(\frac{1}{\sqrt{Th^{\tilde{\alpha}+\varepsilon/2}}}+\frac{1}{Th^{\tilde{\alpha}+\varepsilon/2}}\right). |  |

Since we assume T​hα~+ε/2≥T​hβα+ε≥1Th^{\tilde{\alpha}+\varepsilon/2}\geq Th^{\beta\_{\alpha}+\varepsilon}\geq 1, this gives the desired result.
∎

To upgrade [Lemma A.7](https://arxiv.org/html/2601.01871v1#A1.Thmlemma7 "Lemma A.7. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") to a moment bound for supu∈[−r,r]|ΔT​(u)|\sup\_{u\in[-r,r]}|\Delta\_{T}(u)|, we need the following technical lemma.

###### Lemma A.8.

Let FF be a bounded non-decreasing function on ℝ\mathbb{R}.
For any h,ρ>0h,\rho>0, there exist finite points −r=u0≤u1≤⋯≤uN=r-r=u\_{0}\leq u\_{1}\leq\dots\leq u\_{N}=r and universal constants C,d≥1C,d\geq 1 such that N≤C​ρ−dN\leq C\rho^{-d} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | supu∈[−r,r]min0≤a≤N−1​∫−r1r1{Fh​(v−ua)−Fh​(v−ua+1)}​g​(v)​𝑑v≤2​ρ​‖F‖∞h​∫−r1r1g​(u)​𝑑u.\sup\_{u\in[-r,r]}\min\_{0\leq a\leq N-1}\int\_{-r\_{1}}^{r\_{1}}\left\{F\_{h}(v-u\_{a})-F\_{h}(v-u\_{a+1})\right\}g(v)dv\leq 2\rho\frac{\|F\|\_{\infty}}{h}\int\_{-r\_{1}}^{r\_{1}}g(u)du. |  | (A.25) |

###### Proof.

Without loss of generality, we may assume ∫−r1r1g​(u)​𝑑u>0\int\_{-r\_{1}}^{r\_{1}}g(u)du>0 since otherwise the asserted claim is trivial.

By the proof of [gine2016mathematical, Proposition 3.6.12], 𝒢:={Fh(⋅−u):u∈[−r,r]}\mathcal{G}:=\{F\_{h}(\cdot-u):u\in[-r,r]\} is a VC subgraph class of functions.
Also, 𝒢\mathcal{G} admits an envelope ‖F‖∞/h\|F\|\_{\infty}/h.
Therefore, by [gine2016mathematical, Theorem 3.3.9], there exist finite points −r=s0<s1<⋯<sL=r-r=s\_{0}<s\_{1}<\dots<s\_{L}=r and universal constants C,d≥1C,d\geq 1 such that L≤C​ρ−dL\leq C\rho^{-d} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | supu∈[−r,r]min0≤a≤L​∫ℝ|Fh​(v−u)−Fh​(v−sa)|​Q​(d​v)≤ρ​‖F‖∞h,\sup\_{u\in[-r,r]}\min\_{0\leq a\leq L}\int\_{\mathbb{R}}\left|F\_{h}(v-u)-F\_{h}(v-s\_{a})\right|Q(dv)\leq\rho\frac{\|F\|\_{\infty}}{h}, |  | (A.26) |

where QQ is a probability measure on (ℝ,ℬ​(ℝ))(\mathbb{R},\mathcal{B}(\mathbb{R})) defined as

|  |  |  |
| --- | --- | --- |
|  | Q​(A)=∫A∩[−r1,r1]g​(u)​𝑑u∫−r1r1g​(u)​𝑑u,A∈ℬ​(ℝ).Q(A)=\frac{\int\_{A\cap[-r\_{1},r\_{1}]}g(u)du}{\int\_{-r\_{1}}^{r\_{1}}g(u)du},\qquad A\in\mathcal{B}(\mathbb{R}). |  |

Next, define a function ψ:ℝ→ℝ\psi:\mathbb{R}\to\mathbb{R} as

|  |  |  |
| --- | --- | --- |
|  | ψ​(u)=∫−r1r1Fh​(v−u)​g​(v)​𝑑v=∫ℝF​(t)​g​(u+h​t)​1[−r1,r1]​(u+h​t)​𝑑t,u∈ℝ.\psi(u)=\int\_{-r\_{1}}^{r\_{1}}F\_{h}(v-u)g(v)dv=\int\_{\mathbb{R}}F(t)g(u+ht)1\_{[-r\_{1},r\_{1}]}(u+ht)dt,\qquad u\in\mathbb{R}. |  |

Then, ([A.26](https://arxiv.org/html/2601.01871v1#A1.E26 "Equation A.26 ‣ Proof. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives

|  |  |  |
| --- | --- | --- |
|  | supu∈[−r,r]min0≤a≤L⁡|ψ​(u)−ψ​(sa)|≤ρ​‖F‖∞h​∫−r1r1g​(u)​𝑑u.\sup\_{u\in[-r,r]}\min\_{0\leq a\leq L}|\psi(u)-\psi(s\_{a})|\leq\rho\frac{\|F\|\_{\infty}}{h}\int\_{-r\_{1}}^{r\_{1}}g(u)du. |  |

Also, since gg is non-negative and FF is non-decreasing, ψ\psi is non-increasing.
Moreover, since g​1[−r1,r1]∈L1​(ℝ)g1\_{[-r\_{1},r\_{1}]}\in L^{1}(\mathbb{R}) and FF is bounded, ψ\psi is continuous (see e.g. [malliavin1995integration, Lemma 1.8.1]).
Consequently, for every a=0,…,L−1a=0,\dots,L-1, there exists a point ta∈[sa,sa+1]t\_{a}\in[s\_{a},s\_{a+1}] such that ψ​(ta)={ψ​(sa)+ψ​(sa+1)}/2\psi(t\_{a})=\{\psi(s\_{a})+\psi(s\_{a+1})\}/2 by the intermediate value theorem.
Observe that ψ​(sa)−ψ​(ta)=ψ​(ta)−ψ​(sa+1)={ψ​(sa)−ψ​(sa+1)}/2\psi(s\_{a})-\psi(t\_{a})=\psi(t\_{a})-\psi(s\_{a+1})=\{\psi(s\_{a})-\psi(s\_{a+1})\}/2.
Moreover, since ψ\psi is non-increasing,

|  |  |  |
| --- | --- | --- |
|  | min0≤a′≤L⁡|ψ​(ta)−ψ​(sa′)|={ψ​(sa)−ψ​(ta)}∧{ψ​(ta)−ψ​(sa+1)}=ψ​(sa)−ψ​(sa+1)2.\min\_{0\leq a^{\prime}\leq L}|\psi(t\_{a})-\psi(s\_{a^{\prime}})|=\{\psi(s\_{a})-\psi(t\_{a})\}\wedge\{\psi(t\_{a})-\psi(s\_{a+1})\}=\frac{\psi(s\_{a})-\psi(s\_{a+1})}{2}. |  |

Therefore, we obtain the desired points by setting u2​a=sau\_{2a}=s\_{a} and u2​a+1=tau\_{2a+1}=t\_{a} for a=0,…,L−1a=0,\dots,L-1 and u2​L=sLu\_{2L}=s\_{L}.
∎

Combining the previous two lemmas, we can derive the following uniform moment bound for ΔT​(u)\Delta\_{T}(u):

###### Lemma A.9.

Assume [[A1]](https://arxiv.org/html/2601.01871v1#S3.I1.i1 "Item [A1] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes") and [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Assume also that KK is of bounded variation and supported on [−1,1][-1,1].
If h≤min⁡{T−η, 1/2}h\leq\min\{T^{-\eta},\,1/2\} for some η>0\eta>0, then

|  |  |  |
| --- | --- | --- |
|  | E⁡[h1−α~​supu∈[−r,r]|ΔT​(u)|]≲CηT​hα~+ε,\displaystyle\operatorname{E}\left[h^{1-\tilde{\alpha}}\sup\_{u\in[-r,r]}\left|\Delta\_{T}(u)\right|\right]\lesssim\frac{C\_{\eta}}{\sqrt{Th^{\tilde{\alpha}+\varepsilon}}}, |  |

where CηC\_{\eta} depends only on η\eta.

###### Proof.

Since KK is of bounded variation and supported on [−1,1][-1,1], there exist two non-decreasing functions F1,F2F\_{1},F\_{2} on ℝ\mathbb{R} such that K=(F1−F2)​1[−1,1]K=(F\_{1}-F\_{2})1\_{[-1,1]} and |F1|∨|F2|≤‖K‖∞|F\_{1}|\vee|F\_{2}|\leq\|K\|\_{\infty}.
Therefore, without loss of generality, we may assume that KK is of the form K=F​1[−1,1]K=F1\_{[-1,1]} with FF a non-decreasing function on ℝ\mathbb{R}.
In the remainder of the proof, we proceed in two steps.

##### Step 1.

For ρ=h/T1/α~\rho=h/T^{1/\tilde{\alpha}}, let −r=u0≤u1≤⋯≤uN=r-r=u\_{0}\leq u\_{1}\leq\dots\leq u\_{N}=r and d≥1d\geq 1 be as in [Lemma A.8](https://arxiv.org/html/2601.01871v1#A1.Thmlemma8 "Lemma A.8. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes").
Inserting the equi-spaced points −r+k​ρ-r+k\rho (k=1,…,⌊2​r/ρ⌋)(k=1,\dots,\lfloor 2r/\rho\rfloor) into the sequence (ua)a=0N(u\_{a})\_{a=0}^{N} if necessary, we may assume max0≤a≤N−1⁡(ua+1−ua)≤ρ\max\_{0\leq a\leq N-1}(u\_{a+1}-u\_{a})\leq\rho while ([A.25](https://arxiv.org/html/2601.01871v1#A1.E25 "Equation A.25 ‣ Lemma A.8. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) still holds. Note that this operation increases the number of points at most ⌊2​r/ρ⌋\lfloor 2r/\rho\rfloor, so we have N≲ρ−dN\lesssim\rho^{-d}.

For each u∈[−r,r]u\in[-r,r], set

|  |  |  |
| --- | --- | --- |
|  | X~j​(u):=1T​λ1​λ2​∫Ij×ℝ1[−h,h]⊕ρ​(y−x−u)​Fh​(y−x−u)​N1​(d​x)​N2​(d​y),j=0,1,…,T−1\widetilde{X}\_{j}(u):=\frac{1}{T\lambda\_{1}\lambda\_{2}}\int\_{I\_{j}\times\mathbb{R}}1\_{[-h,h]\oplus\rho}(y-x-u)F\_{h}(y-x-u)N\_{1}(dx)N\_{2}(dy),\quad j=0,1,\dots,T-1 |  |

and

|  |  |  |
| --- | --- | --- |
|  | Δ~T​(u):=∑j=0T−1{X~j​(u)−E⁡[X~j​(u)]}.\widetilde{\Delta}\_{T}(u):=\sum\_{j=0}^{T-1}\left\{\widetilde{X}\_{j}(u)-\operatorname{E}[\widetilde{X}\_{j}(u)]\right\}. |  |

In Step 2, we will show

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[h1−α~​supu∈[−r,r]|ΔT​(u)|]≲E⁡[h1−α~​max0≤a≤N⁡|Δ~T​(ua)|]+1T​hα~.\operatorname{E}\left[h^{1-\tilde{\alpha}}\sup\_{u\in[-r,r]}|\Delta\_{T}(u)|\right]\lesssim\operatorname{E}\left[h^{1-\tilde{\alpha}}\max\_{0\leq a\leq N}|\widetilde{\Delta}\_{T}(u\_{a})|\right]+\frac{1}{\sqrt{Th^{\tilde{\alpha}}}}. |  | (A.27) |

Given this estimate, we can prove the claim of the lemma as follows.
Since N≲ρ−d≤h−d​{1+1/(α~​η)}N\lesssim\rho^{-d}\leq h^{-d\{1+1/(\tilde{\alpha}\eta)\}}, we have N1/p≲h−ε/4N^{1/p}\lesssim h^{-\varepsilon/4} for a sufficiently large even integer pp depending only on α\alpha and η\eta.
Observe that Jensen’s inequality gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[h1−α~​max0≤a≤N⁡|Δ~T​(ua)|]\displaystyle\operatorname{E}\left[h^{1-\tilde{\alpha}}\max\_{0\leq a\leq N}\left|\widetilde{\Delta}\_{T}(u\_{a})\right|\right] | ≤h1−α~​(E⁡[max0≤a≤N⁡|Δ~T​(ua)|p])1/p≤(N+1)1/p​h1−α~​max0≤a≤N⁡‖Δ~T​(ua)‖p.\displaystyle\leq h^{1-\tilde{\alpha}}\left(\operatorname{E}\left[\max\_{0\leq a\leq N}\left|\widetilde{\Delta}\_{T}(u\_{a})\right|^{p}\right]\right)^{1/p}\leq(N+1)^{1/p}h^{1-\tilde{\alpha}}\max\_{0\leq a\leq N}\left\|\widetilde{\Delta}\_{T}(u\_{a})\right\|\_{p}. |  |

Meanwhile, define a function K~:ℝ→ℝ\widetilde{K}:\mathbb{R}\to\mathbb{R} as K~​(u)=2​F​(2​u)​1[−1,1]⊕T−1/α~​(2​u)\widetilde{K}(u)=2F(2u)1\_{[-1,1]\oplus T^{-1/\tilde{\alpha}}}(2u) for u∈ℝu\in\mathbb{R}. Observe that K~\widetilde{K} is supported on [−1,1][-1,1] and bounded by 2​‖K‖∞2\|K\|\_{\infty}.
Moreover, we can rewrite X~j​(u)\widetilde{X}\_{j}(u) as

|  |  |  |
| --- | --- | --- |
|  | X~j​(u)=1T​λ1​λ2​∫Ij×ℝK~2​h​(y−x−u)​N1​(d​x)​N2​(d​y).\widetilde{X}\_{j}(u)=\frac{1}{T\lambda\_{1}\lambda\_{2}}\int\_{I\_{j}\times\mathbb{R}}\tilde{K}\_{2h}(y-x-u)N\_{1}(dx)N\_{2}(dy). |  |

Therefore, we can apply [Lemma A.7](https://arxiv.org/html/2601.01871v1#A1.Thmlemma7 "Lemma A.7. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") to Δ~T​(u)\widetilde{\Delta}\_{T}(u) and thus obtain

|  |  |  |
| --- | --- | --- |
|  | E⁡[h1−α~​max0≤a≤N⁡|Δ~T​(ua)|]≲(N+1)1/pT​hα~+ε/2≲1T​hα~+ε.\displaystyle\operatorname{E}\left[h^{1-\tilde{\alpha}}\max\_{0\leq a\leq N}\left|\widetilde{\Delta}\_{T}(u\_{a})\right|\right]\lesssim\frac{(N+1)^{1/p}}{\sqrt{Th^{\tilde{\alpha}+\varepsilon/2}}}\lesssim\frac{1}{\sqrt{Th^{\tilde{\alpha}+\varepsilon}}}. |  |

Combining this with ([A.27](https://arxiv.org/html/2601.01871v1#A1.E27 "Equation A.27 ‣ Step 1. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives the claim of the lemma.

##### Step 2.

It remains to prove ([A.27](https://arxiv.org/html/2601.01871v1#A1.E27 "Equation A.27 ‣ Step 1. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
Fix u∈[−r,r]u\in[-r,r]. We can find an index 0≤a<N0\leq a<N such that ua≤u≤ua+1u\_{a}\leq u\leq u\_{a+1}.
Since u−ua≤ua+1−ua≤ρu-u\_{a}\leq u\_{a+1}-u\_{a}\leq\rho and FF is non-decreasing, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xj​(u)\displaystyle X\_{j}(u) | =1T​λ1​λ2​∫Ij×ℝ1[−h,h]​(y−x−u)​Fh​(y−x−u)​N1​(d​x)​N2​(d​y)≤X~j​(ua)\displaystyle=\frac{1}{T\lambda\_{1}\lambda\_{2}}\int\_{I\_{j}\times\mathbb{R}}1\_{[-h,h]}(y-x-u)F\_{h}(y-x-u)N\_{1}(dx)N\_{2}(dy)\leq\widetilde{X}\_{j}(u\_{a}) |  |

for all jj.
Campbell’s formula gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[X~j​(ua)]\displaystyle\operatorname{E}[\widetilde{X}\_{j}(u\_{a})] | =1T​∫ℝ1[−h,h]⊕ρ​(v−ua)​Kh​(v−ua)​g​(v)​𝑑v\displaystyle=\frac{1}{T}\int\_{\mathbb{R}}1\_{[-h,h]\oplus\rho}(v-u\_{a})K\_{h}(v-u\_{a})g(v)dv |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1T​∫−r1r11[−h,h]⊕ρ​(v−ua)​Kh​(v−ua)​g​(v)​𝑑v,\displaystyle=\frac{1}{T}\int\_{-r\_{1}}^{r\_{1}}1\_{[-h,h]\oplus\rho}(v-u\_{a})K\_{h}(v-u\_{a})g(v)dv, |  |

where the second equality follows from ua∈[−r,r]u\_{a}\in[-r,r] and h+ρ≤2​h≤1h+\rho\leq 2h\leq 1.
Observe that 1[−h,h]⊕ρ​(v−ua)=1Jh,u​(v−u)1\_{[-h,h]\oplus\rho}(v-u\_{a})=1\_{J\_{h,u}}(v-u) with Jh,u:=([−h,h]⊕ρ)+(ua−u)J\_{h,u}:=([-h,h]\oplus\rho)+(u\_{a}-u).
Note that Jh,u⊃[−h,h]J\_{h,u}\supset[-h,h] because u−ua≤ρu-u\_{a}\leq\rho.
Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |E⁡[X~j​(ua)]−1T​∫−r1r11[−h,h]​(v−u)​Kh​(v−ua)​g​(v)​𝑑v|\displaystyle\left|\operatorname{E}[\widetilde{X}\_{j}(u\_{a})]-\frac{1}{T}\int\_{-r\_{1}}^{r\_{1}}1\_{[-h,h]}(v-u)K\_{h}(v-u\_{a})g(v)dv\right| | ≤‖K‖∞T​h​∫−r1r11Jh,u∖[−h,h]​(v−u)​g​(v)​𝑑v.\displaystyle\leq\frac{\|K\|\_{\infty}}{Th}\int\_{-r\_{1}}^{r\_{1}}1\_{J\_{h,u}\setminus[-h,h]}(v-u)g(v)dv. |  |

Noting that ‖g0‖L1/(1−α~/2)≲1\|g\_{0}\|\_{L^{1/(1-\tilde{\alpha}/2)}}\lesssim 1 by Jensen’s inequality (if α<1\alpha<1) and ∫−r1r1|u−θ∗|α−11−α~/2​𝑑u≲1\int\_{-r\_{1}}^{r\_{1}}|u-\theta^{\*}|^{\frac{\alpha-1}{1-\tilde{\alpha}/2}}du\lesssim 1 because α−11−α~/2>−1\frac{\alpha-1}{1-\tilde{\alpha}/2}>-1, we have ‖g‖L1/(1−α~/2)≲1\|g\|\_{L^{1/(1-\tilde{\alpha}/2)}}\lesssim 1 by [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes").
Then, since Leb⁡(Jh,u∖[−h,h])≲ρ\operatorname{Leb}(J\_{h,u}\setminus[-h,h])\lesssim\rho, Young’s inequality gives

|  |  |  |
| --- | --- | --- |
|  | |E⁡[X~j​(ua)]−1T​∫−r1r11[−h,h]​(v−u)​Kh​(v−ua)​g​(v)​𝑑v|≲ρα~/2T​h.\displaystyle\left|\operatorname{E}[\widetilde{X}\_{j}(u\_{a})]-\frac{1}{T}\int\_{-r\_{1}}^{r\_{1}}1\_{[-h,h]}(v-u)K\_{h}(v-u\_{a})g(v)dv\right|\lesssim\frac{\rho^{\tilde{\alpha}/2}}{Th}. |  |

Meanwhile, by Campbell’s formula again,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[Xj​(u)]\displaystyle\operatorname{E}[X\_{j}(u)] | =1T​∫ℝ1[−h,h]​(v−u)​Kh​(v−u)​g​(v)​𝑑v.\displaystyle=\frac{1}{T}\int\_{\mathbb{R}}1\_{[-h,h]}(v-u)K\_{h}(v-u)g(v)dv. |  |

Therefore, ([A.25](https://arxiv.org/html/2601.01871v1#A1.E25 "Equation A.25 ‣ Lemma A.8. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives

|  |  |  |
| --- | --- | --- |
|  | |E⁡[Xj​(u)]−1T​∫−r1r11[−h,h]​(v−u)​Kh​(v−ua)​g​(v)​𝑑v|≲ρT​h.\displaystyle\left|\operatorname{E}[X\_{j}(u)]-\frac{1}{T}\int\_{-r\_{1}}^{r\_{1}}1\_{[-h,h]}(v-u)K\_{h}(v-u\_{a})g(v)dv\right|\lesssim\frac{\rho}{Th}. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | Xj​(u)−E⁡[Xj​(u)]≤X~j​(ua)−E⁡[X~j​(ua)]+C0​ρα~/2T​h,\displaystyle X\_{j}(u)-\operatorname{E}[X\_{j}(u)]\leq\widetilde{X}\_{j}(u\_{a})-\operatorname{E}[\widetilde{X}\_{j}(u\_{a})]+C\_{0}\frac{\rho^{\tilde{\alpha}/2}}{Th}, |  |

where C0>0C\_{0}>0 is a constant depending only on r,α,α0,δ,b,(Bp)p≥1,(Bp,q)p,q≥1,εr,\alpha,\alpha\_{0},\delta,b,(B\_{p})\_{p\geq 1},(B\_{p,q})\_{p,q\geq 1},\varepsilon and ‖K‖∞\|K\|\_{\infty}.
Similarly, we also have

|  |  |  |
| --- | --- | --- |
|  | Xj​(u)−E⁡[Xj​(u)]≥X~j​(ua+1)−E⁡[X~j​(ua+1)]−C0​ρα~/2T​h.\displaystyle X\_{j}(u)-\operatorname{E}[X\_{j}(u)]\geq\widetilde{X}\_{j}(u\_{a+1})-\operatorname{E}[\widetilde{X}\_{j}(u\_{a+1})]-C\_{0}\frac{\rho^{\tilde{\alpha}/2}}{Th}. |  |

Thus, we conclude

|  |  |  |
| --- | --- | --- |
|  | supu∈[−r,r]|ΔT​(u)|≤max0≤a≤N⁡|Δ~T​(ua)|+C0​ρα~/2h.\sup\_{u\in[-r,r]}|\Delta\_{T}(u)|\leq\max\_{0\leq a\leq N}|\widetilde{\Delta}\_{T}(u\_{a})|+C\_{0}\frac{\rho^{\tilde{\alpha}/2}}{h}. |  |

Therefore, ([A.27](https://arxiv.org/html/2601.01871v1#A1.E27 "Equation A.27 ‣ Step 1. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) follows from the definition of ρ\rho.
∎

###### Proof of [Theorem 4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").

Define the function fhf\_{h} by ([A.2](https://arxiv.org/html/2601.01871v1#A1.E2 "Equation A.2 ‣ Lemma A.2. ‣ A.1 Preliminaries ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) and
set Δ¯T:=supu∈[−r,r]|g~h​(u)−fh​(u)|\bar{\Delta}\_{T}:=\sup\_{u\in[-r,r]}\left|\tilde{g}\_{h}(u)-f\_{h}(u)\right|.
Since E⁡[Xj​(u)]=fh​(u)\operatorname{E}[X\_{j}(u)]=f\_{h}(u) for all jj, [Lemma A.6](https://arxiv.org/html/2601.01871v1#A1.Thmlemma6 "Lemma A.6. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[Δ¯T]≲E⁡[supu∈[−r,r]|ΔT​(u)|]+1T​h.\operatorname{E}\left[\bar{\Delta}\_{T}\right]\lesssim\operatorname{E}\left[\sup\_{u\in[-r,r]}|\Delta\_{T}(u)|\right]+\frac{1}{Th}. |  | (A.28) |

Now, consider the case α>1\alpha>1.
Then, by [Lemma A.5](https://arxiv.org/html/2601.01871v1#A1.Thmlemma5 "Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"), for some σ∈{−1,1}\sigma\in\{-1,1\}, there exist constants A>1A>1 and 0<h0<10<h\_{0}<1 depending only on α,b,δ\alpha,b,\delta such that ([A.16](https://arxiv.org/html/2601.01871v1#A1.E16 "Equation A.16 ‣ Item (a) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds.
Since θ^h\hat{\theta}\_{h} is a maximizer of [−r,r]∋u↦g~h​(u)∈[0,∞)[-r,r]\ni u\mapsto\tilde{g}\_{h}(u)\in[0,\infty), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | P⁡(|θ^h−θ∗|>A​h)\displaystyle\operatorname{P}\left(|\hat{\theta}\_{h}-\theta^{\*}|>Ah\right) | ≤P⁡(g~h​(θ∗+σ​h)≤supu∈[−r,r]:|u−θ∗|>A​hg~h​(u))\displaystyle\leq\operatorname{P}\left(\tilde{g}\_{h}(\theta^{\*}+\sigma h)\leq\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}\tilde{g}\_{h}(u)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤P⁡(fh​(θ∗+σ​h)≤supu∈[−r,r]:|u−θ∗|>A​hfh​(u)+2​Δ¯T).\displaystyle\leq\operatorname{P}\left(f\_{h}(\theta^{\*}+\sigma h)\leq\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u)+2\bar{\Delta}\_{T}\right). |  |

Therefore, ([A.16](https://arxiv.org/html/2601.01871v1#A1.E16 "Equation A.16 ‣ Item (a) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) gives P⁡(|θ^h−θ∗|>A​h)≤P⁡(2​Δ¯T≥hα−1)\operatorname{P}\left(|\hat{\theta}\_{h}-\theta^{\*}|>Ah\right)\leq\operatorname{P}\left(2\bar{\Delta}\_{T}\geq h^{\alpha-1}\right).
Hence, the desired result follows by Markov’s inequality, ([A.28](https://arxiv.org/html/2601.01871v1#A1.E28 "Equation A.28 ‣ Proof of Theorem 4.1. ‣ Step 2. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) and [Lemma A.9](https://arxiv.org/html/2601.01871v1#A1.Thmlemma9 "Lemma A.9. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes").

Next, consider the case α<1\alpha<1.
Then, by [Lemma A.5](https://arxiv.org/html/2601.01871v1#A1.Thmlemma5 "Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"), for some σ∈{−1,1}\sigma\in\{-1,1\}, there exist constants A>1,c>0A>1,c>0 and 0<h0<10<h\_{0}<1 depending only on α,α0,b,δ,K\alpha,\alpha\_{0},b,\delta,K such that ([A.17](https://arxiv.org/html/2601.01871v1#A1.E17 "Equation A.17 ‣ Item (b) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds.
Since θ^h\hat{\theta}\_{h} is a maximizer of [−r,r]∋u↦g~h​(u)∈[0,∞)[-r,r]\ni u\mapsto\tilde{g}\_{h}(u)\in[0,\infty),

|  |  |  |  |
| --- | --- | --- | --- |
|  | P⁡(|θ^h−θ∗|>A​h)\displaystyle\operatorname{P}\left(|\hat{\theta}\_{h}-\theta^{\*}|>Ah\right) | ≤P⁡(g~h​(θ∗)≤supu∈[−r,r]:|u−θ∗|>A​hg~h​(u))\displaystyle\leq\operatorname{P}\left(\tilde{g}\_{h}(\theta^{\*})\leq\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}\tilde{g}\_{h}(u)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤P⁡(fh​(θ∗)≤supu∈[−r,r]:|u−θ∗|>A​hfh​(u)+2​Δ¯T)\displaystyle\leq\operatorname{P}\left(f\_{h}(\theta^{\*})\leq\sup\_{u\in[-r,r]:|u-\theta^{\*}|>Ah}f\_{h}(u)+2\bar{\Delta}\_{T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤P⁡(2​Δ¯T≥c​hα−1),\displaystyle\leq\operatorname{P}\left(2\bar{\Delta}\_{T}\geq ch^{\alpha-1}\right), |  |

where the last line follows from ([A.17](https://arxiv.org/html/2601.01871v1#A1.E17 "Equation A.17 ‣ Item (b) ‣ Lemma A.5. ‣ A.3 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
Therefore, the desired result follows by Markov’s inequality, ([A.28](https://arxiv.org/html/2601.01871v1#A1.E28 "Equation A.28 ‣ Proof of Theorem 4.1. ‣ Step 2. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) and [Lemma A.9](https://arxiv.org/html/2601.01871v1#A1.Thmlemma9 "Lemma A.9. ‣ A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") again.
∎

### A.5 Proof of Theorem [4.2](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.1 Bandwidth selection by Lepski’s method ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")

Below we assume TT is sufficiently large TT such that jmin≤loga⁡(Tmaxγ)j\_{\min}\leq\log\_{a}(T^{\gamma}\_{\max}).
For 0<γ≤γmax0<\gamma\leq\gamma\_{\max}, we write h∗​(γ)h^{\*}(\gamma) for the largest element h∈ℋTh\in\mathcal{H}\_{T} such that h≤T−γh\leq T^{-\gamma}.
Note that h∗​(γ)h^{\*}(\gamma) is well-defined because γ≤γmax\gamma\leq\gamma\_{\max}.
Also, a​h∗​(γ)>T−γah^{\*}(\gamma)>T^{-\gamma} for sufficiently large TT by construction, so h∗​(γ)≍T−γh^{\*}(\gamma)\asymp T^{-\gamma} as T→∞T\to\infty.

###### Lemma A.10.

Under the assumptions of [Theorem 4.2](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.1 Bandwidth selection by Lepski’s method ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes"), for any 0<γ<1/βα0<\gamma<1/\beta\_{\alpha}, P⁡(h^>T−γ)→0\operatorname{P}(\hat{h}>T^{-\gamma})\to 0 as T→∞T\to\infty.

###### Proof.

Write h∗=h∗​(γ)h^{\*}=h^{\*}(\gamma) for short.
Observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | P⁡(h^>T−γ)\displaystyle\operatorname{P}(\hat{h}>T^{-\gamma}) | ≤P⁡(h^>h∗)≤P⁡(d¯​(ℳh∗,ℳh′)>AT​h′​ for some ​h′∈ℋT​ with ​h′≥h∗)\displaystyle\leq\operatorname{P}(\hat{h}>h^{\*})\leq\operatorname{P}(\bar{d}(\mathcal{M}\_{h^{\*}},\mathcal{M}\_{h^{\prime}})>A\_{T}h^{\prime}\text{ for some }h^{\prime}\in\mathcal{H}\_{T}\text{ with }h^{\prime}\geq h^{\*}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑h′∈ℋT:h′≥h∗P⁡(d¯​(ℳh∗,ℳh′)>AT​h′).\displaystyle\leq\sum\_{h^{\prime}\in\mathcal{H}\_{T}:h^{\prime}\geq h^{\*}}\operatorname{P}(\bar{d}(\mathcal{M}\_{h^{\*}},\mathcal{M}\_{h^{\prime}})>A\_{T}h^{\prime}). |  |

Since d¯​(ℳh∗,ℳh′)≤d¯​(ℳh∗,{θ∗})+d¯​(ℳh′,{θ∗})\bar{d}(\mathcal{M}\_{h^{\*}},\mathcal{M}\_{h^{\prime}})\leq\bar{d}(\mathcal{M}\_{h^{\*}},\{\theta^{\*}\})+\bar{d}(\mathcal{M}\_{h^{\prime}},\{\theta^{\*}\}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | P⁡(h^>T−γ)\displaystyle\operatorname{P}(\hat{h}>T^{-\gamma}) | ≤∑h′∈ℋT:h′≥h∗{P⁡(d¯​(ℳh∗,{θ∗})>AT​h′/2)+P⁡(d¯​(ℳh′,{θ∗})>AT​h′/2)}\displaystyle\leq\sum\_{h^{\prime}\in\mathcal{H}\_{T}:h^{\prime}\geq h^{\*}}\left\{\operatorname{P}(\bar{d}(\mathcal{M}\_{h^{\*}},\{\theta^{\*}\})>A\_{T}h^{\prime}/2)+\operatorname{P}(\bar{d}(\mathcal{M}\_{h^{\prime}},\{\theta^{\*}\})>A\_{T}h^{\prime}/2)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​|ℋT|​maxh∈ℋT:h≥h∗⁡P⁡(d¯​(ℳh,{θ∗})>AT​h/2).\displaystyle\leq 2|\mathcal{H}\_{T}|\max\_{h\in\mathcal{H}\_{T}:h\geq h^{\*}}\operatorname{P}(\bar{d}(\mathcal{M}\_{h},\{\theta^{\*}\})>A\_{T}h/2). |  |

For every h∈ℋTh\in\mathcal{H}\_{T}, we can find a random variable θ~h∈ℳh\tilde{\theta}\_{h}\in\mathcal{M}\_{h} such that |θ~h−θ∗|>AT​h/2|\tilde{\theta}\_{h}-\theta^{\*}|>A\_{T}h/2 on the event d¯​(ℳh,{θ∗})>AT​h/2\bar{d}(\mathcal{M}\_{h},\{\theta^{\*}\})>A\_{T}h/2. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | P⁡(h^>T−γ)\displaystyle\operatorname{P}(\hat{h}>T^{-\gamma}) | ≤2​|ℋT|​maxh∈ℋT:h≥h∗⁡P⁡(|θ~h−θ∗|>AT​h/2).\displaystyle\leq 2|\mathcal{H}\_{T}|\max\_{h\in\mathcal{H}\_{T}:h\geq h^{\*}}\operatorname{P}(|\tilde{\theta}\_{h}-\theta^{\*}|>A\_{T}h/2). |  |

Thus, for any ε>0\varepsilon>0, [Theorem 4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") gives

|  |  |  |
| --- | --- | --- |
|  | P⁡(h^T>T−γ)=O​(|ℋT|​maxh∈ℋT:h≥h∗⁡1T​hβα+ε)=O​(|ℋT|T​(h∗)βα+ε).\displaystyle\operatorname{P}(\hat{h}\_{T}>T^{-\gamma})=O\left(|\mathcal{H}\_{T}|\max\_{h\in\mathcal{H}\_{T}:h\geq h^{\*}}\frac{1}{\sqrt{Th^{\beta\_{\alpha}+\varepsilon}}}\right)=O\left(\frac{|\mathcal{H}\_{T}|}{\sqrt{T(h^{\*})^{\beta\_{\alpha}+\varepsilon}}}\right). |  |

Since γ<1/βα\gamma<1/\beta\_{\alpha} and |ℋT|=O​(log⁡T)|\mathcal{H}\_{T}|=O(\log T), we obtain the desired result by taking ε\varepsilon so that γ​(βα+ε)<1\gamma(\beta\_{\alpha}+\varepsilon)<1.
∎

###### Proof of [Theorem 4.2](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.1 Bandwidth selection by Lepski’s method ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").

Let γ′\gamma^{\prime} be a constant such that γ<γ′<1/βα\gamma<\gamma^{\prime}<1/\beta\_{\alpha}. Then, AT​T−γ′=o​(T−γ)A\_{T}T^{-\gamma^{\prime}}=o(T^{-\gamma}) by assumption.
Hence it is enough to prove P⁡(|θ^h^−θ∗|>2​AT​T−γ′)→0\operatorname{P}(|\hat{\theta}\_{\hat{h}}-\theta^{\*}|>2A\_{T}T^{-\gamma^{\prime}})\to 0.
Moreover, thanks to [Lemma A.10](https://arxiv.org/html/2601.01871v1#A1.Thmlemma10 "Lemma A.10. ‣ A.5 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"), it suffices to show

|  |  |  |
| --- | --- | --- |
|  | P⁡(|θ^h^−θ∗|>2​AT​T−γ′,h^≤T−γ′)→0.\operatorname{P}(|\hat{\theta}\_{\hat{h}}-\theta^{\*}|>2A\_{T}T^{-\gamma^{\prime}},\hat{h}\leq T^{-\gamma^{\prime}})\to 0. |  |

On the event h^≤T−γ′\hat{h}\leq T^{-\gamma^{\prime}}, we have h^≤h∗​(γ′)\hat{h}\leq h^{\*}(\gamma^{\prime}), so

|  |  |  |
| --- | --- | --- |
|  | |θ^h^−θ∗|≤|θ^h^−θ^h∗​(γ′)|+|θ^h∗​(γ′)−θ∗|≤AT​h∗​(γ′)+|θ^h∗​(γ′)−θ∗|≤AT​T−γ′+|θ^h∗​(γ′)−θ∗|,\displaystyle|\hat{\theta}\_{\hat{h}}-\theta^{\*}|\leq|\hat{\theta}\_{\hat{h}}-\hat{\theta}\_{h^{\*}(\gamma^{\prime})}|+|\hat{\theta}\_{h^{\*}(\gamma^{\prime})}-\theta^{\*}|\leq A\_{T}h^{\*}(\gamma^{\prime})+|\hat{\theta}\_{h^{\*}(\gamma^{\prime})}-\theta^{\*}|\leq A\_{T}T^{-\gamma^{\prime}}+|\hat{\theta}\_{h^{\*}(\gamma^{\prime})}-\theta^{\*}|, |  |

where the second inequality follows by the definition of h^\hat{h}.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | P⁡(|θ^h^−θ∗|>2​AT​T−γ′,h^≤T−γ′)≤P⁡(|θ^h∗​(γ′)−θ∗|>AT​T−γ′).\operatorname{P}(|\hat{\theta}\_{\hat{h}}-\theta^{\*}|>2A\_{T}T^{-\gamma^{\prime}},\hat{h}\leq T^{-\gamma^{\prime}})\leq\operatorname{P}(|\hat{\theta}\_{h^{\*}(\gamma^{\prime})}-\theta^{\*}|>A\_{T}T^{-\gamma^{\prime}}). |  |

Since P⁡(|θ^h∗​(γ′)−θ∗|>AT​T−γ′)→0\operatorname{P}(|\hat{\theta}\_{h^{\*}(\gamma^{\prime})}-\theta^{\*}|>A\_{T}T^{-\gamma^{\prime}})\to 0 by [Theorem 4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes"), we obtain the desired result.
∎

### A.6 Proof of Theorem [4.3](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Minimax lower bound for the convergence rate ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes")

The proof of [Theorem 4.3](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Minimax lower bound for the convergence rate ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes") relies on Theorem 2.2 in [tsybakov2008nonparametric], which requires the notion of the Hellinger distance.
Recall that the Hellinger distance between two probability measures PP and QQ defined on a common measurable space (𝒳,𝒜)(\mathcal{X},\mathcal{A}) is defined as

|  |  |  |
| --- | --- | --- |
|  | H​(P,Q):=∫𝒳(d​Pd​ν−d​Qd​ν)2​𝑑ν,H(P,Q):=\sqrt{\int\_{\mathcal{X}}\left(\sqrt{\frac{dP}{d\nu}}-\sqrt{\frac{dQ}{d\nu}}\right)^{2}d\nu}, |  |

where ν\nu is any σ\sigma-finite measure on (𝒳,𝒜)(\mathcal{X},\mathcal{A}) dominating both PP and QQ.
By Lemmas 2.9 and 2.10(1) in [strasser1985mathematical],

|  |  |  |  |
| --- | --- | --- | --- |
|  | H2​(P,Q)=2​(1−∫𝒳d​Qd​P​𝑑P),H^{2}(P,Q)=2\left(1-\int\_{\mathcal{X}}\sqrt{\frac{dQ}{dP}}dP\right), |  | (A.29) |

where d​Q/d​P:=d​Qa/d​PdQ/dP:=dQ^{a}/dP with QaQ^{a} the absolutely continuous part of QQ with respect to PP.
Note that strasser1985mathematical defines the Hellinger distance as H​(P,Q)/2H(P,Q)/\sqrt{2} in our notation.

###### Proof of [Theorem 4.3](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Minimax lower bound for the convergence rate ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes").

Define a point process N~\tilde{N} on ℝ2\mathbb{R}^{2} as N~:=∑i=1∞δ(ti,ti+γi)\tilde{N}:=\sum\_{i=1}^{\infty}\delta\_{(t\_{i},t\_{i}+\gamma\_{i})}.
Since N1(⋅)=N~(⋅×ℝ)N\_{1}(\cdot)=\tilde{N}(\cdot\times\mathbb{R}) and N2(⋅)=N~(ℝ×⋅)N\_{2}(\cdot)=\tilde{N}(\mathbb{R}\times\cdot), we have σ​(N∩[0,T])⊂σ​(N~∩[0,T]2)\sigma(N\cap[0,T])\subset\sigma(\tilde{N}\cap[0,T]^{2}).
Also, with DT:=[0,T]×[−1,T+1]D\_{T}:=[0,T]\times[-1,T+1], we evidently have σ​(N~∩[0,T]2)⊂σ​(N~∩DT)\sigma(\tilde{N}\cap[0,T]^{2})\subset\sigma(\tilde{N}\cap D\_{T}).
Therefore, it suffices to show that there exists a constant b>0b>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infT→∞infθ~Tsup|θ|≤2​ρTsupg∈𝒢​(θ,α,1/2,b)Pg⁡(|θ~T−θ|≥ρT)>0,\liminf\_{T\to\infty}\inf\_{\tilde{\theta}\_{T}}\sup\_{|\theta|\leq 2\rho\_{T}}\sup\_{g\in\mathcal{G}(\theta,\alpha,1/2,b)}\operatorname{P}\_{g}\left(|\tilde{\theta}\_{T}-\theta|\geq\rho\_{T}\right)>0, |  | (A.30) |

where the infimum is taken over all estimators based on N~∩DT\tilde{N}\cap D\_{T}.
For every probability density gg on ℝ\mathbb{R}, we denote by PT,gP\_{T,g} the law of N~∩DT\tilde{N}\cap D\_{T} induced on (𝒩DT#,ℬ​(𝒩DT#))(\mathcal{N}^{\#}\_{D\_{T}},\mathcal{B}(\mathcal{N}^{\#}\_{D\_{T}})) under Pg\operatorname{P}\_{g}, where 𝒩DT#\mathcal{N}^{\#}\_{D\_{T}} denotes the space of all counting measures on DTD\_{T} equipped with the w#w^{\#}-topology; see [daley2006introduction, Appendix A2.6] and [daley2007introduction, Definition 9.1.II] for details.
According to Eq.(2.9) and Theorem 2.2 in [tsybakov2008nonparametric], we obtain ([A.30](https://arxiv.org/html/2601.01871v1#A1.E30 "Equation A.30 ‣ Proof of Theorem 4.3. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) once we find gT∈𝒢​(2​ρT,α,1/2,b)g\_{T}\in\mathcal{G}(2\rho\_{T},\alpha,1/2,b) and g0∈𝒢​(0,α,1/2,b)g\_{0}\in\mathcal{G}(0,\alpha,1/2,b) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supT→∞H2​(PT,gT,PT,g0)<2.\limsup\_{T\to\infty}H^{2}(P\_{T,g\_{T}},P\_{T,g\_{0}})<2. |  | (A.31) |

Let us compute H2​(PT,gT,PT,g0)H^{2}(P\_{T,g\_{T}},P\_{T,g\_{0}}).
Observe that N~\tilde{N} can be viewed as a cluster process on ℝ\mathbb{R} with centre process N1N\_{1} and component processes {δ(ti,ti+γi):i∈ℕ}\{\delta\_{(t\_{i},t\_{i}+\gamma\_{i})}:i\in\mathbb{N}\}.
Hence, by Proposition 6.3.III in [daley2006introduction], the probability generating functional (p.g.fl) of N~\tilde{N} under Pg\operatorname{P}\_{g} for g∈{g0,gT}g\in\{g\_{0},g\_{T}\} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gg​(φ)\displaystyle G\_{g}(\varphi) | =exp⁡(−∫ℝ(1−∫ℝφ​(x,y)​g​(y−x)​𝑑y)​𝑑x)\displaystyle=\exp\left(-\int\_{\mathbb{R}}\left(1-\int\_{\mathbb{R}}\varphi(x,y)g(y-x)dy\right)dx\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(∫ℝ2(φ​(x,y)−1)​g​(y−x)​𝑑x​𝑑y)\displaystyle=\exp\left(\int\_{\mathbb{R}^{2}}\left(\varphi(x,y)-1\right)g(y-x)dxdy\right) |  |

for every measurable function φ:ℝ2→(0,1]\varphi:\mathbb{R}^{2}\to(0,1] such that the support of 1−φ1-\varphi is bounded.
Since gg is supported on [−1,1][-1,1],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gg​(1−1DT+φ​1DT)\displaystyle G\_{g}(1-1\_{D\_{T}}+\varphi 1\_{D\_{T}}) | =e−T​exp⁡(∫[0,T]×ℝφ​(x,y)​g​(y−x)​𝑑x​𝑑y).\displaystyle=e^{-T}\exp\left(\int\_{[0,T]\times\mathbb{R}}\varphi(x,y)g(y-x)dxdy\right). |  |

Therefore, in view of Eq.(5.5.14) in [daley2006introduction], the local Janossy densities of N~\tilde{N} on DTD\_{T} under Pg\operatorname{P}\_{g} are given by

|  |  |  |
| --- | --- | --- |
|  | jn,g​((x1,y1),…,(xn,yn)∣DT)=e−T​∏i=1ng​(yi−xi)​1[0,T]​(xi)(n=1,2,…).j\_{n,g}((x\_{1},y\_{1}),\dots,(x\_{n},y\_{n})\mid D\_{T})=e^{-T}\prod\_{i=1}^{n}g(y\_{i}-x\_{i})1\_{[0,T]}(x\_{i})\quad(n=1,2,\dots). |  |

This gives

|  |  |  |
| --- | --- | --- |
|  | d​PT,gTd​PT,g0​(N~)=∏i:ti∈[0,T]gT​(γi)g0​(γi)Pg0-a.s.\frac{dP\_{T,g\_{T}}}{dP\_{T,g\_{0}}}(\tilde{N})=\prod\_{i:t\_{i}\in[0,T]}\frac{g\_{T}(\gamma\_{i})}{g\_{0}(\gamma\_{i})}\quad\text{$\operatorname{P}\_{g\_{0}}$-a.s.} |  |

Here, recall that d​PT,gT/d​PT,g0:=d​PT,gTa/d​PT,g0dP\_{T,g\_{T}}/dP\_{T,g\_{0}}:=dP\_{T,g\_{T}}^{a}/dP\_{T,g\_{0}} with PT,gTaP\_{T,g\_{T}}^{a} the absolutely continuous part of PT,gTP\_{T,g\_{T}} with respect to PT,g0P\_{T,g\_{0}}.
Thus, by ([A.29](https://arxiv.org/html/2601.01871v1#A1.E29 "Equation A.29 ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")),

|  |  |  |
| --- | --- | --- |
|  | H2(PT,gT,PT,g0)=2(1−Eg0[∏i:ti∈[0,T]gT​(γi)g0​(γi)])=:2(1−aT),\displaystyle H^{2}(P\_{T,g\_{T}},P\_{T,g\_{0}})=2\left(1-\operatorname{E}\_{g\_{0}}\left[\prod\_{i:t\_{i}\in[0,T]}\sqrt{\frac{g\_{T}(\gamma\_{i})}{g\_{0}(\gamma\_{i})}}\right]\right)=:2(1-a\_{T}), |  |

where Eg0\operatorname{E}\_{g\_{0}} denotes expectation under Pg0\operatorname{P}\_{g\_{0}}.
Therefore, ([A.31](https://arxiv.org/html/2601.01871v1#A1.E31 "Equation A.31 ‣ Proof of Theorem 4.3. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) follows once we show
lim infT→∞aT>0.\liminf\_{T\to\infty}a\_{T}>0.
Recall that under Pg0\operatorname{P}\_{g\_{0}}, (γi)i=1∞(\gamma\_{i})\_{i=1}^{\infty} is i.i.d. with common density g0g\_{0} and independent of N1N\_{1}.
Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | aT\displaystyle a\_{T} | =Eg0⁡[(∫gT​(x)​g0​(x)​𝑑x)N1​([0,T])].\displaystyle=\operatorname{E}\_{g\_{0}}\left[\left(\int\sqrt{g\_{T}(x)g\_{0}(x)}dx\right)^{N\_{1}([0,T])}\right]. |  |

Since N1​([0,T])N\_{1}([0,T]) follows the Poisson distribution with intensity TT under Pg0\operatorname{P}\_{g\_{0}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | aT\displaystyle a\_{T} | =exp⁡(T​(∫gT​(x)​g0​(x)​𝑑x−1))=exp⁡(−T2​∫(gT​(x)−g0​(x))2​𝑑x).\displaystyle=\exp\left(T\left(\int\sqrt{g\_{T}(x)g\_{0}(x)}dx-1\right)\right)=\exp\left(-\frac{T}{2}\int\left(\sqrt{g\_{T}(x)}-\sqrt{g\_{0}(x)}\right)^{2}dx\right). |  |

Therefore, we complete the proof once we show that there exists a constant b>0b>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(gT​(x)−g0​(x))2​𝑑x=O​(T−1)\int\left(\sqrt{g\_{T}(x)}-\sqrt{g\_{0}(x)}\right)^{2}dx=O(T^{-1}) |  | (A.32) |

for some gT∈𝒢​(2​ρT,α,1/2,b)g\_{T}\in\mathcal{G}(2\rho\_{T},\alpha,1/2,b) and g0∈𝒢​(0,α,1/2,b)g\_{0}\in\mathcal{G}(0,\alpha,1/2,b).

##### Case 1: 0<α<10<\alpha<1.

For every θ∈[0,1]\theta\in[0,1], define a function fθ:ℝ→[0,∞)f\_{\theta}:\mathbb{R}\to[0,\infty) as

|  |  |  |
| --- | --- | --- |
|  | fθ​(x)=α​|x−θ|α−1​1[−1,0)​(x−θ)(x∈ℝ).f\_{\theta}(x)=\alpha|x-\theta|^{\alpha-1}1\_{[-1,0)}(x-\theta)\quad(x\in\mathbb{R}). |  |

By construction, we evidently have fθ∈𝒢​(θ,α,1/2,b)f\_{\theta}\in\mathcal{G}(\theta,\alpha,1/2,b) for some constant b>0b>0 depending only on α\alpha.
Moreover, since f0f\_{0} satisfies Eq.(1.9) of [ibragimov2013statistical, Chapter VI] in a neighborhood of z=0z=0 with α=α−1\alpha=\alpha-1, p≡1p\equiv 1 and q≡0q\equiv 0 in their notation, f0f\_{0} has one singularity of order α−1\alpha-1 located at 0 in the sense of Definition 1.1 of [ibragimov2013statistical, Chapter VI].
Therefore, Theorem 1.1 in [ibragimov2013statistical, Chapter VI] gives ([A.32](https://arxiv.org/html/2601.01871v1#A1.E32 "Equation A.32 ‣ Proof of Theorem 4.3. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) for gT=f2​ρTg\_{T}=f\_{2\rho\_{T}} and g0=f0g\_{0}=f\_{0}.

##### Case 2: α>1\alpha>1.

We employ a minor variant of the construction used in the proof of [arias2022estimation, Theorem 2].
For every θ∈[0,1/2)\theta\in[0,1/2), define functions ψθ:ℝ→ℝ\psi\_{\theta}:\mathbb{R}\to\mathbb{R} and fθ:ℝ→ℝf\_{\theta}:\mathbb{R}\to\mathbb{R} as

|  |  |  |
| --- | --- | --- |
|  | ψθ​(x)=(|x|α−1−(2​θ)α−1)​1(−2​θ,0]​(x)+(|x|α−1+(2​θ)α−1−2α​|x−θ|α−1)​1(0,2​θ)​(x),x∈ℝ\displaystyle\psi\_{\theta}(x)=(|x|^{\alpha-1}-(2\theta)^{\alpha-1})1\_{(-2\theta,0]}(x)+\left(|x|^{\alpha-1}+(2\theta)^{\alpha-1}-2^{\alpha}|x-\theta|^{\alpha-1}\right)1\_{(0,2\theta)}(x),\quad x\in\mathbb{R} |  |

and

|  |  |  |
| --- | --- | --- |
|  | fθ​(x)=α2​(α−1)​(1−|x|α−1+ψθ​(x))​1[−1,1]​(x),x∈ℝ.\displaystyle f\_{\theta}(x)=\frac{\alpha}{2(\alpha-1)}\left(1-|x|^{\alpha-1}+\psi\_{\theta}(x)\right)1\_{[-1,1]}(x),\quad x\in\mathbb{R}. |  |

Observe that fθ≥0f\_{\theta}\geq 0 and

|  |  |  |
| --- | --- | --- |
|  | ∫−∞∞fθ​(x)​𝑑x=α2​α−1​(∫−11(1−|x|α−1)​𝑑x+∫−2​θ2​θ|x|α−1​𝑑x−2α​∫02​θ|x−θ|α−1​𝑑x)=1.\displaystyle\int\_{-\infty}^{\infty}f\_{\theta}(x)dx=\frac{\alpha}{2\alpha-1}\left(\int\_{-1}^{1}(1-|x|^{\alpha-1})dx+\int\_{-2\theta}^{2\theta}|x|^{\alpha-1}dx-2^{\alpha}\int\_{0}^{2\theta}|x-\theta|^{\alpha-1}dx\right)=1. |  |

Hence fθf\_{\theta} is a probability density function on ℝ\mathbb{R}.
Moreover, we have for all x∈[−1,1]x\in[-1,1]

|  |  |  |  |
| --- | --- | --- | --- |
|  | 22−α​|x−θ|α−1≤2​(α−1)α​(fθ​(θ)−fθ​(x))≤2α​|x−θ|α−1.2^{2-\alpha}|x-\theta|^{\alpha-1}\leq\frac{2(\alpha-1)}{\alpha}\left(f\_{\theta}(\theta)-f\_{\theta}(x)\right)\leq 2^{\alpha}|x-\theta|^{\alpha-1}. |  | (A.33) |

In fact, a straightforward computation shows

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​(α−1)α​(fθ​(θ)−fθ​(x))\displaystyle\frac{2(\alpha-1)}{\alpha}\left(f\_{\theta}(\theta)-f\_{\theta}(x)\right) | ={2​(2​θ)α−1if −2​θ<x≤0,2α​|x−θ|α−1if ​0<x<2​θ,|x|α−1+(2​θ)α−1otherwise.\displaystyle=\begin{cases}2(2\theta)^{\alpha-1}&\text{if }-2\theta<x\leq 0,\\ 2^{\alpha}|x-\theta|^{\alpha-1}&\text{if }0<x<2\theta,\\ |x|^{\alpha-1}+(2\theta)^{\alpha-1}&\text{otherwise}.\end{cases} |  |

Hence ([A.33](https://arxiv.org/html/2601.01871v1#A1.E33 "Equation A.33 ‣ Case 2: 𝛼>1. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) is evident if 0<x<2​θ0<x<2\theta.
If −2​θ<x≤0-2\theta<x\leq 0, then θ≤|x−θ|≤3​θ\theta\leq|x-\theta|\leq 3\theta, so
2​(2​θ)α−1≤2α​|x−θ|α−12(2\theta)^{\alpha-1}\leq 2^{\alpha}|x-\theta|^{\alpha-1}
and
2​(2​θ)α−1≥2​(2​|x−θ|/3)α−1≥22−α​|x−θ|α−12(2\theta)^{\alpha-1}\geq 2(2|x-\theta|/3)^{\alpha-1}\geq 2^{2-\alpha}|x-\theta|^{\alpha-1}. Hence ([A.33](https://arxiv.org/html/2601.01871v1#A1.E33 "Equation A.33 ‣ Case 2: 𝛼>1. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds.
Also, Jensen’s inequality gives
|x−θ|α−1≤2α−2​(|x|α−1+θα−1)≤2α−2​(|x|α−1+(2​θ)α−1).|x-\theta|^{\alpha-1}\leq 2^{\alpha-2}(|x|^{\alpha-1}+\theta^{\alpha-1})\leq 2^{\alpha-2}(|x|^{\alpha-1}+(2\theta)^{\alpha-1}).
Hence the lower bound of ([A.33](https://arxiv.org/html/2601.01871v1#A1.E33 "Equation A.33 ‣ Case 2: 𝛼>1. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds if |x|≥2​θ|x|\geq 2\theta.
Moreover, if x≤−2​θx\leq-2\theta, then |x|≥2​θ|x|\geq 2\theta and |x−θ|=θ−x≥−x=|x||x-\theta|=\theta-x\geq-x=|x|, so

|  |  |  |
| --- | --- | --- |
|  | |x|α−1+(2​θ)α−1≤2​|x|α−1≤2​|x−θ|α−1.\displaystyle|x|^{\alpha-1}+(2\theta)^{\alpha-1}\leq 2|x|^{\alpha-1}\leq 2|x-\theta|^{\alpha-1}. |  |

If x≥2​θx\geq 2\theta, then x−θ≥θx-\theta\geq\theta and thus

|  |  |  |
| --- | --- | --- |
|  | |x|α−1+(2​θ)α−1≤2α−2​|x−θ|α−1+3⋅2α−2​θα−1≤2α​|x−θ|α−1,\displaystyle|x|^{\alpha-1}+(2\theta)^{\alpha-1}\leq 2^{\alpha-2}|x-\theta|^{\alpha-1}+3\cdot 2^{\alpha-2}\theta^{\alpha-1}\leq 2^{\alpha}|x-\theta|^{\alpha-1}, |  |

where the first inequality is by Jensen’s inequality.
Therefore, the upper bound of ([A.33](https://arxiv.org/html/2601.01871v1#A1.E33 "Equation A.33 ‣ Case 2: 𝛼>1. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) also holds if |x|≥2​θ|x|\geq 2\theta.
Consequently, fθ∈𝒢​(θ,α,1/2,b)f\_{\theta}\in\mathcal{G}(\theta,\alpha,1/2,b) for some constant b>0b>0 depending only on α\alpha.

Now, Eq.(2.27) of [tsybakov2008nonparametric] gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(fθ​(x)−f0​(x))2​𝑑x\displaystyle\int\left(\sqrt{f\_{\theta}(x)}-\sqrt{f\_{0}(x)}\right)^{2}dx | ≤∫−11(fθ​(x)f0​(x)−1)2​f0​(x)​𝑑x\displaystyle\leq\int\_{-1}^{1}\left(\frac{f\_{\theta}(x)}{f\_{0}(x)}-1\right)^{2}f\_{0}(x)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =α2​(α−1)​∫−2​θ2​θψθ​(x)21−|x|α−1​𝑑x≤α2​(α−1)​3​(2​θ)2​α−11−(2​θ)α−1.\displaystyle=\frac{\alpha}{2(\alpha-1)}\int\_{-2\theta}^{2\theta}\frac{\psi\_{\theta}(x)^{2}}{1-|x|^{\alpha-1}}dx\leq\frac{\alpha}{2(\alpha-1)}\frac{3(2\theta)^{2\alpha-1}}{1-(2\theta)^{\alpha-1}}. |  |

Hence ([A.32](https://arxiv.org/html/2601.01871v1#A1.E32 "Equation A.32 ‣ Proof of Theorem 4.3. ‣ A.6 Proof of Theorem 4.3 ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) holds for gT=f2​ρTg\_{T}=f\_{2\rho\_{T}} and g0=f0g\_{0}=f\_{0}.
∎

### A.7 Proof of Assumption [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) for LBHPG with gamma kernels

In this section, we show that LBHPG\mathrm{LBHPG} with common rate parameters βi​j≡β>0,i,j=1,2\beta\_{ij}\equiv\beta>0,i,j=1,2 satisfies [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) with α=min⁡{D12,D21}\alpha=\min\{D\_{12},D\_{21}\} when min⁡{D12,D21}<1\min\{D\_{12},D\_{21}\}<1 and the stationary assumption (spectral radius ρ​(𝜶)\rho(\boldsymbol{\alpha}) of the matrix 𝜶\boldsymbol{\alpha} is smaller than 11) holds.
Let

|  |  |  |
| --- | --- | --- |
|  | ha​(t):=βaΓ​(a)​ta−1​e−β​t​𝟏(0,∞)​(t),t∈ℝ,a>0,h\_{a}(t):=\frac{\beta^{a}}{\Gamma(a)}t^{a-1}e^{-\beta t}\mathbf{1}\_{(0,\infty)}(t),\qquad t\in\mathbb{R},a>0, |  |

𝑯=(hDi​j)1≤i,j≤2\boldsymbol{H}=(h\_{D\_{ij}})\_{1\leq i,j\leq 2} , α∗=min⁡{D12,D21}(<1)\alpha\_{\*}=\min\{D\_{12},D\_{21}\}(<1), and D∗=min⁡{D11,D12,D21,D22}D\_{\*}=\min\{D\_{11},D\_{12},D\_{21},D\_{22}\}.
Then, we have Φ=𝜶⊙𝑯\Phi=\boldsymbol{\alpha}\odot\boldsymbol{H} by definition, where ⊙\odot is the Hadamard product.
Recall Ψ=∑m≥1Φ(∗m)\Psi=\sum\_{m\geq 1}\Phi^{(\*m)} converges in L1​(ℝ)L^{1}(\mathbb{R}) componentwise.

By ([5.1](https://arxiv.org/html/2601.01871v1#S5.E1 "Equation 5.1 ‣ 5.1.1 Lagged bivariate Hawkes process with gamma kernels ‣ 5.1 Models ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes")) and ([5.2](https://arxiv.org/html/2601.01871v1#S5.E2 "Equation 5.2 ‣ 5.1.1 Lagged bivariate Hawkes process with gamma kernels ‣ 5.1 Models ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes")) , it is sufficient to show the following proposition:

###### Proposition A.1.

Under the assumptions above, there exist C>0C>0 and δ>0\delta>0 such that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | αi​j​hDi​j​(u)\displaystyle\alpha\_{ij}h\_{D\_{ij}}(u) | ≤Ψi​j​(u),\displaystyle\leq\Psi\_{ij}(u), | u>0,(i,j)∈{(1,2),(2,1)},\displaystyle u>0,\ (i,j)\in\{(1,2),(2,1)\}, |  | (A.34) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | max⁡{Ψ12​(u),Ψ21​(u)}\displaystyle\max\{\Psi\_{12}(u),\Psi\_{21}(u)\} | ≤C​uα∗−1,\displaystyle\leq Cu^{\alpha\_{\*}-1}, | 0<u<δ,\displaystyle 0<u<\delta, |  | (A.35) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 0≤∫ℝΨi​1​(s)​Ψi​2​(s+u)​𝑑s\displaystyle 0\leq\int\_{\mathbb{R}}\Psi\_{i1}(s)\Psi\_{i2}(s+u)\,ds | ≤C​|u|α∗−1,\displaystyle\leq C|u|^{\alpha\_{\*}-1}, | 0<|u|<δ,i∈{1,2}.\displaystyle 0<|u|<\delta,i\in\{1,2\}. |  | (A.36) |

In the following, we first provide several lemmas and then use them to establish
Proposition [A.1](https://arxiv.org/html/2601.01871v1#A1.Thmproposition1 "Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes").
Before proceeding, we decompose Ψ\Psi as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ=Ψs+Ψb,\Psi=\Psi^{s}+\Psi^{b}, |  | (A.37) |

where

|  |  |  |
| --- | --- | --- |
|  | Ψs:=∑m=1M−1Φ(∗m),Ψb:=∑m=M∞Φ(∗m),M=⌈1/D∗⌉+1.\Psi^{s}:=\sum\_{m=1}^{M-1}\Phi^{(\*m)},\qquad\Psi^{b}:=\sum\_{m=M}^{\infty}\Phi^{(\*m)},\qquad M=\lceil 1/D\_{\*}\rceil+1. |  |

###### Lemma A.11.

For m≥1m\geq 1, i,j∈{1,2}i,j\in\{1,2\} and t>0t>0,

|  |  |  |
| --- | --- | --- |
|  | (Φ(∗m))i​j​(t)=∑(i0,…,im)∈{1,2}m+1,i0=j,im=i(∏ℓ=1mαiℓ​iℓ−1)​h∑ℓ=1mDiℓ​iℓ−1​(t).(\Phi^{(\*m)})\_{ij}(t)=\sum\_{\begin{subarray}{c}(i\_{0},\dots,i\_{m})\in\{1,2\}^{m+1},\\ i\_{0}=j,\;i\_{m}=i\end{subarray}}\Bigl(\prod\_{\ell=1}^{m}\alpha\_{i\_{\ell}i\_{\ell-1}}\Bigr)\,h\_{\sum\_{\ell=1}^{m}D\_{i\_{\ell}i\_{\ell-1}}}(t). |  |

###### Proof.

The result follows from the gamma distribution’s reproducibility.
∎

###### Lemma A.12.

For every a≥1a\geq 1, ‖ha‖∞≤β\|h\_{a}\|\_{\infty}\leq\beta.

###### Proof.

Fix a≥1a\geq 1.
Since the gamma density hah\_{a} is log-concave on [0,∞)[0,\infty), we have

|  |  |  |
| --- | --- | --- |
|  | ‖ha‖∞≤1σa\|h\_{a}\|\_{\infty}\leq\frac{1}{\sigma\_{a}} |  |

by [saumard2014log, Eq. (5.8)], where σa\sigma\_{a} is the standard deviation of hah\_{a}.
Since the standard deviation of hah\_{a} is σa=a/β\sigma\_{a}=\sqrt{a}/\beta, we conclude that

|  |  |  |
| --- | --- | --- |
|  | ‖ha‖∞≤βa≤β.\|h\_{a}\|\_{\infty}\leq\frac{\beta}{\sqrt{a}}\leq\beta. |  |

∎

###### Lemma A.13.

Each component of Ψb\Psi^{b} is bounded on ℝ\mathbb{R}.

###### Proof.

By Lemma [A.11](https://arxiv.org/html/2601.01871v1#A1.Thmlemma11 "Lemma A.11. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"), for m≥Mm\geq M every component of Φ(∗m)\Phi^{(\*m)} is a gamma density
with shape parameter at least m​D∗>1mD\_{\*}>1. Hence Lemma [A.12](https://arxiv.org/html/2601.01871v1#A1.Thmlemma12 "Lemma A.12. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") yields

|  |  |  |
| --- | --- | --- |
|  | ‖(Φ(∗m))i​j‖∞≤β​∑(i0,…,im)∈{1,2}m+1,i0=j,im=i∏ℓ=1mαiℓ​iℓ−1=β​(𝜶m)i​j.\|(\Phi^{(\*m)})\_{ij}\|\_{\infty}\leq\beta\sum\_{\begin{subarray}{c}(i\_{0},\dots,i\_{m})\in\{1,2\}^{m+1},\\ i\_{0}=j,\;i\_{m}=i\end{subarray}}\prod\_{\ell=1}^{m}\alpha\_{i\_{\ell}i\_{\ell-1}}=\beta(\boldsymbol{\alpha}^{m})\_{ij}. |  |

Since ρ​(𝜶)<1\rho(\boldsymbol{\alpha})<1, the series ∑m≥1𝜶m\sum\_{m\geq 1}\boldsymbol{\alpha}^{m} converges entrywise, hence
∑m≥M(𝜶m)i​j<∞\sum\_{m\geq M}(\boldsymbol{\alpha}^{m})\_{ij}<\infty and therefore

|  |  |  |
| --- | --- | --- |
|  | ‖Ψi​jb‖∞≤∑m=M∞‖(Φ(∗m))i​j‖∞≤β​∑m≥M(𝜶m)i​j<∞.\|\Psi^{b}\_{ij}\|\_{\infty}\leq\sum\_{m=M}^{\infty}\|(\Phi^{(\*m)})\_{ij}\|\_{\infty}\leq\beta\sum\_{m\geq M}(\boldsymbol{\alpha}^{m})\_{ij}<\infty. |  |

∎

###### Proof of Proposition [A.1](https://arxiv.org/html/2601.01871v1#A1.Thmproposition1 "Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes").

Throughout the proof, C>0C>0 and δ>0\delta>0 denote generic constants.

Proof of ([A.34](https://arxiv.org/html/2601.01871v1#A1.E34 "Equation A.34 ‣ Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
Since Ψ=∑m≥1Φ(∗m)\Psi=\sum\_{m\geq 1}\Phi^{(\*m)} and each term is nonnegative, we have Ψi​j≥Φi​j=αi​j​hDi​j\Psi\_{ij}\geq\Phi\_{ij}=\alpha\_{ij}h\_{D\_{ij}}
on (0,∞)(0,\infty), which yields ([A.34](https://arxiv.org/html/2601.01871v1#A1.E34 "Equation A.34 ‣ Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).

Proof of ([A.35](https://arxiv.org/html/2601.01871v1#A1.E35 "Equation A.35 ‣ Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
Fix (i,j)∈{(1,2),(2,1)}(i,j)\in\{(1,2),(2,1)\}. By ([A.37](https://arxiv.org/html/2601.01871v1#A1.E37 "Equation A.37 ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")),

|  |  |  |
| --- | --- | --- |
|  | Ψi​j​(u)=Ψi​js​(u)+Ψi​jb​(u),u>0.\Psi\_{ij}(u)=\Psi^{s}\_{ij}(u)+\Psi^{b}\_{ij}(u),\qquad u>0. |  |

By Lemma [A.11](https://arxiv.org/html/2601.01871v1#A1.Thmlemma11 "Lemma A.11. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") and the definition of Ψs\Psi^{s} as a finite sum,
Ψi​js\Psi^{s}\_{ij} is a finite nonnegative linear combination of gamma densities hah\_{a} (with common rate β\beta) whose shape parameters satisfy a≥Di​j≥α∗a\geq D\_{ij}\geq\alpha\_{\*}.
Hence, there exists Cs>0C\_{s}>0 such that Ψi​js​(u)≤Cs​uα∗−1\Psi^{s}\_{ij}(u)\leq C\_{s}u^{\alpha\_{\*}-1} for all u∈(0,1)u\in(0,1).
Moreover, Lemma [A.13](https://arxiv.org/html/2601.01871v1#A1.Thmlemma13 "Lemma A.13. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes") gives ‖Ψi​jb‖∞<∞\|\Psi^{b}\_{ij}\|\_{\infty}<\infty.
Choose δ∈(0,1)\delta\in(0,1) so that uα∗−1≥1u^{\alpha\_{\*}-1}\geq 1 on (0,δ)(0,\delta). Then for u∈(0,δ)u\in(0,\delta),

|  |  |  |
| --- | --- | --- |
|  | Ψi​j​(u)≤Cs​uα∗−1+‖Ψi​jb‖∞≤(Cs+‖Ψi​jb‖∞)​uα∗−1.\Psi\_{ij}(u)\leq C\_{s}u^{\alpha\_{\*}-1}+\|\Psi^{b}\_{ij}\|\_{\infty}\leq(C\_{s}+\|\Psi^{b}\_{ij}\|\_{\infty})\,u^{\alpha\_{\*}-1}. |  |

Taking the maximum over (i,j)=(1,2),(2,1)(i,j)=(1,2),(2,1) yields ([A.35](https://arxiv.org/html/2601.01871v1#A1.E35 "Equation A.35 ‣ Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).

Proof of ([A.36](https://arxiv.org/html/2601.01871v1#A1.E36 "Equation A.36 ‣ Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
Fix i∈{1,2}i\in\{1,2\} and set

|  |  |  |
| --- | --- | --- |
|  | Ii​(u):=∫ℝΨi​1​(s)​Ψi​2​(s+u)​𝑑s,u∈ℝ.I\_{i}(u):=\int\_{\mathbb{R}}\Psi\_{i1}(s)\Psi\_{i2}(s+u)\,ds,\qquad u\in\mathbb{R}. |  |

Non-negativity implies Ii​(u)≥0I\_{i}(u)\geq 0. We will prove the upper bound.

Using ([A.37](https://arxiv.org/html/2601.01871v1#A1.E37 "Equation A.37 ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) and ∫ℝf​(s)​g​(s+u)​𝑑s≤‖f‖1​‖g‖∞\int\_{\mathbb{R}}f(s)g(s+u)\,ds\leq\|f\|\_{1}\|g\|\_{\infty} for nonnegative f,gf,g, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ii​(u)\displaystyle I\_{i}(u) | =∫ℝ(Ψi​1s+Ψi​1b)​(s)​(Ψi​2s+Ψi​2b)​(s+u)​𝑑s\displaystyle=\int\_{\mathbb{R}}(\Psi^{s}\_{i1}+\Psi^{b}\_{i1})(s)\,(\Psi^{s}\_{i2}+\Psi^{b}\_{i2})(s+u)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫ℝΨi​1s​(s)​Ψi​2s​(s+u)​𝑑s+‖Ψi​1‖1​‖Ψi​2b‖∞+‖Ψi​1b‖∞​‖Ψi​2‖1,\displaystyle\leq\int\_{\mathbb{R}}\Psi^{s}\_{i1}(s)\Psi^{s}\_{i2}(s+u)\,ds+\|\Psi\_{i1}\|\_{1}\|\Psi^{b}\_{i2}\|\_{\infty}+\|\Psi^{b}\_{i1}\|\_{\infty}\|\Psi\_{i2}\|\_{1}, |  |

where we used Ψi​ks≤Ψi​k\Psi^{s}\_{ik}\leq\Psi\_{ik} and Ψi​kb≤Ψi​k\Psi^{b}\_{ik}\leq\Psi\_{ik}.
Since ‖Φi​j‖1=αi​j\|\Phi\_{ij}\|\_{1}=\alpha\_{ij} and ‖(Φ(∗m))i​j‖1=(𝜶m)i​j\|(\Phi^{(\*m)})\_{ij}\|\_{1}=(\boldsymbol{\alpha}^{m})\_{ij}, the assumption
ρ​(𝜶)<1\rho(\boldsymbol{\alpha})<1 implies ‖Ψi​k‖1=∑m≥1(𝜶m)i​k<∞\|\Psi\_{ik}\|\_{1}=\sum\_{m\geq 1}(\boldsymbol{\alpha}^{m})\_{ik}<\infty.
By Lemma [A.13](https://arxiv.org/html/2601.01871v1#A1.Thmlemma13 "Lemma A.13. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"), ‖Ψi​kb‖∞<∞\|\Psi^{b}\_{ik}\|\_{\infty}<\infty. Hence, the last two terms are finite constants
independent of uu, and since α∗<1\alpha\_{\*}<1 we may shrink δ∈(0,1)\delta\in(0,1) so that these constants are absorbed by
C​|u|α∗−1C|u|^{\alpha\_{\*}-1} on 0<|u|<δ0<|u|<\delta (using |u|α∗−1≥1|u|^{\alpha\_{\*}-1}\geq 1 there).
Therefore, it suffices to show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝΨi​1s​(s)​Ψi​2s​(s+u)​𝑑s≤C​|u|α∗−1,0<|u|<δ.\int\_{\mathbb{R}}\Psi^{s}\_{i1}(s)\Psi^{s}\_{i2}(s+u)\,ds\leq C|u|^{\alpha\_{\*}-1},\qquad 0<|u|<\delta. |  | (A.38) |

For a,b>0a,b>0, define

|  |  |  |
| --- | --- | --- |
|  | fa,bBG​(u):=∫ℝha​(s)​hb​(s+u)​𝑑s,u∈ℝ.f^{\mathrm{BG}}\_{a,b}(u):=\int\_{\mathbb{R}}h\_{a}(s)\,h\_{b}(s+u)\,ds,\qquad u\in\mathbb{R}. |  |

Then, fa,bBGf^{\mathrm{BG}}\_{a,b} is the probability density function of a bilateral gamma distribution [kuchler2008shapes] with parameters
  
(α+,λ+,α−,λ−)=(b,β,a,β)(\alpha\_{+},\lambda\_{+},\alpha\_{-},\lambda\_{-})=(b,\beta,a,\beta).
By kuchler2008shapes, as u→0u\to 0 the density satisfies
fa,bBG​(u)=O​(|u|a+b−1)f^{\mathrm{BG}}\_{a,b}(u)=O(|u|^{a+b-1}) if a+b<1a+b<1, and fa,bBG​(u)=O​(M​(|u|))f^{\mathrm{BG}}\_{a,b}(u)=O(M(|u|)) if a+b=1a+b=1, where MM is slowly varying at 0. If a+b>1a+b>1, then fa,bBGf^{\mathrm{BG}}\_{a,b} is bounded in a neighborhood of 0.
Consequently, for any a,b>0a,b>0 with a+b>α∗a+b>\alpha\_{\*}, there exists Ca,b>0C\_{a,b}>0 and
δa,b∈(0,1)\delta\_{a,b}\in(0,1) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | fa,bBG​(u)≤Ca,b​|u|α∗−1,0<|u|<δa,bf^{\mathrm{BG}}\_{a,b}(u)\leq C\_{a,b}|u|^{\alpha\_{\*}-1},\qquad 0<|u|<\delta\_{a,b} |  | (A.39) |

since α∗<1\alpha^{\*}<1 by the assumption.
Next, by Lemma [A.11](https://arxiv.org/html/2601.01871v1#A1.Thmlemma11 "Lemma A.11. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes"),
each Ψi​ks\Psi^{s}\_{ik} is a finite nonnegative linear combination of gamma densities hah\_{a}. Hence, the left-hand side of
([A.38](https://arxiv.org/html/2601.01871v1#A1.E38 "Equation A.38 ‣ Proof of Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) is a finite nonnegative linear combination of fa,bBG​(u)f^{\mathrm{BG}}\_{a,b}(u).
If i=1i=1, then Ψ12s\Psi^{s}\_{12} only involves shapes b≥D12≥α∗b\geq D\_{12}\geq\alpha\_{\*}, while shapes aa in Ψ11s\Psi^{s}\_{11} are strictly positive; thus a+b>α∗a+b>\alpha\_{\*}.
If i=2i=2, then Ψ21s\Psi^{s}\_{21} only involves shapes a≥D21≥α∗a\geq D\_{21}\geq\alpha\_{\*}, while shapes bb in Ψ22s\Psi^{s}\_{22} are strictly
positive; thus again a+b>α∗a+b>\alpha\_{\*}.
Therefore, ([A.39](https://arxiv.org/html/2601.01871v1#A1.E39 "Equation A.39 ‣ Proof of Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")) applies to all pairs (a,b)(a,b) appearing in the linear combination, we can
take a common δ>0\delta>0 and C>0C>0, which yields ([A.38](https://arxiv.org/html/2601.01871v1#A1.E38 "Equation A.38 ‣ Proof of Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")). This proves ([A.36](https://arxiv.org/html/2601.01871v1#A1.E36 "Equation A.36 ‣ Proposition A.1. ‣ A.7 Proof of Assumption [A2](ii) for LBHPG with gamma kernels ‣ Appendix A Proofs ‣ On lead-lag estimation of non-synchronously observed point processes")).
∎

## Appendix B Implementation and computational complexity

In this section, we discuss the efficient computation of the kernel density estimator g^h​(u)\hat{g}\_{h}(u) and the search strategy for its maximizer θ^h\hat{\theta}\_{h}.
In our implementation, the expected time complexity for computing θ^h\hat{\theta}\_{h} from observations on [0,T][0,T] with bandwidth hh scales as

|  |  |  |
| --- | --- | --- |
|  | {O​(T​log⁡T+T2​h),under Assumption [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i),O​(T​log⁡T+T2​hα),under Assumption [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii) with ​0<α<1.\begin{cases}O\!\left(T\log T+T^{2}h\right),&\text{under Assumption~\ref{ass:cpcf}(i)},\\ O\!\left(T\log T+T^{2}h^{\alpha}\right),&\text{under Assumption~\ref{ass:cpcf}(ii) with }0<\alpha<1.\end{cases} |  |

This is better than a naive O​(T2)O(T^{2}) approach that evaluates g^h​(u)\hat{g}\_{h}(u) at each candidate uu by summing over all pairs, especially when the bandwidth hh is small.

### B.1 Algorithm for computing g^h\hat{g}\_{h} on a grid

Directly evaluating g^h\hat{g}\_{h} on a grid {u1,…,uM}⊂ℝ\{u\_{1},\dots,u\_{M}\}\subset\mathbb{R} may be computationally expensive, roughly scaling with the product of the grid size and the number of data pairs.
To reduce computational cost, we employ an algorithm that iterates over relevant timestamp pairs and distributes their kernel weights onto nearby grid points.
This approach is particularly efficient when the bandwidth hh is small relative to the grid’s range.

Let N1N\_{1} and N2N\_{2} be the underlying point processes, observed over the window [0,T][0,T], and let
𝒯i:={ti,1<⋯<ti,ni}⊂[0,T],ni:=Ni​([0,T]),i=1,2\mathcal{T}\_{i}:=\{t\_{i,1}<\cdots<t\_{i,n\_{i}}\}\subset[0,T],\ n\_{i}:=N\_{i}([0,T]),\ i=1,2
denote the corresponding observed event times.
Let 𝒰={u1<⋯<uM}\mathcal{U}=\{u\_{1}<\cdots<u\_{M}\} be a sorted grid where we wish to evaluate the estimator, and define
umin:=u1u\_{\min}:=u\_{1} and umax:=uMu\_{\max}:=u\_{M}.
For any a<ba<b, define the set of relevant pairs in the lag window [a,b][a,b] and the corresponding set of differences by

|  |  |  |
| --- | --- | --- |
|  | 𝒫​(a,b):={(x,y)∈𝒯1×𝒯2:y−x∈[a,b]},Npairs​(a,b):=|𝒫​(a,b)|,\mathcal{P}(a,b):=\{(x,y)\in\mathcal{T}\_{1}\times\mathcal{T}\_{2}:\ y-x\in[a,b]\},\qquad N\_{\mathrm{pairs}}(a,b):=|\mathcal{P}(a,b)|, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝒟​(a,b):={y−x:(x,y)∈𝒫​(a,b)}⊂[a,b].\mathcal{D}(a,b):=\{y-x:\ (x,y)\in\mathcal{P}(a,b)\}\subset[a,b]. |  |

Algorithm [1](https://arxiv.org/html/2601.01871v1#alg1 "Algorithm 1 ‣ B.1 Algorithm for computing 𝑔̂_ℎ on a grid ‣ Appendix B Implementation and computational complexity ‣ On lead-lag estimation of non-synchronously observed point processes") outlines the procedure.
Instead of fixing uu and summing over all pairs, we iterate through each observed time x∈𝒯1x\in\mathcal{T}\_{1}.
Using binary search in 𝒯2\mathcal{T}\_{2}, we identify the range of y∈𝒯2y\in\mathcal{T}\_{2} for which the difference
d=y−xd=y-x lies within the lag window [umin−h,umax+h][u\_{\min}-h,\,u\_{\max}+h], i.e., the set of lags that can influence at least one grid point through a bandwidth-hh kernel.
For each such difference dd, we find the subset of grid points in 𝒰∩[d−h,d+h]\mathcal{U}\cap[d-h,d+h] (again via binary search) and accumulate the kernel contribution at those grid points.
Throughout this section, we assume that KK is supported on [−1,1][-1,1].

Algorithm 1  Computation of g^h​(u)\hat{g}\_{h}(u) on a grid

Sorted event times 𝒯1\mathcal{T}\_{1}, 𝒯2\mathcal{T}\_{2}, sorted grid 𝒰={u1,…,uM}\mathcal{U}=\{u\_{1},\dots,u\_{M}\}, bandwidth hh,

kernel KK supported on [−1,1][-1,1].

Values G=(G1,…,GM)G=(G\_{1},\dots,G\_{M}) corresponding to (g^h​(u1),…,g^h​(uM))(\hat{g}\_{h}(u\_{1}),\dots,\hat{g}\_{h}(u\_{M})).

Initialize G←(0,…,0)G\leftarrow(0,\dots,0)

umin←u1,umax←uMu\_{\min}\leftarrow u\_{1},\quad u\_{\max}\leftarrow u\_{M}

for x∈𝒯1x\in\mathcal{T}\_{1} do

Identify indices [jstart,jend][j\_{\text{start}},j\_{\text{end}}] for 𝒯2∩[x+umin−h,x+umax+h]\mathcal{T}\_{2}\cap[x+u\_{\min}-h,\ x+u\_{\max}+h]

for j←jstartj\leftarrow j\_{\text{start}} to jendj\_{\text{end}} do

y←𝒯2​[j]y\leftarrow\mathcal{T}\_{2}[j]

d←y−xd\leftarrow y-x

Identify indices [kstart,kend][k\_{\text{start}},k\_{\text{end}}] for 𝒰∩[d−h,d+h]\mathcal{U}\cap[d-h,\ d+h]

for k←kstartk\leftarrow k\_{\text{start}} to kendk\_{\text{end}} do

Gk←Gk+1h​K​(d−ukh)G\_{k}\leftarrow G\_{k}+\frac{1}{h}K\!\left(\frac{d-u\_{k}}{h}\right)

end for

end for

end for

Scale GG by Tn1​n2\frac{T}{n\_{1}n\_{2}}, i.e., G←Tn1​n2​GG\leftarrow\frac{T}{n\_{1}n\_{2}}G

return GG

##### Computational complexity.

Only pairs in the lag window [umin−h,umax+h][u\_{\min}-h,\ u\_{\max}+h] contribute to g^h\hat{g}\_{h} evaluated on 𝒰\mathcal{U}, and the number of such pairs is
Npairs​(umin−h,umax+h)N\_{\mathrm{pairs}}(u\_{\min}-h,\ u\_{\max}+h).
For each x∈𝒯1x\in\mathcal{T}\_{1}, we locate the index range of
𝒯2∩[x+umin−h,x+umax+h]\mathcal{T}\_{2}\cap[x+u\_{\min}-h,\ x+u\_{\max}+h] by binary search in 𝒯2\mathcal{T}\_{2}, which costs O​(log⁡n2)O(\log n\_{2}) per xx
(and thus O​(n1​log⁡n2)O(n\_{1}\log n\_{2}) in total).
For each relevant pair (x,y)∈𝒫​(umin−h,umax+h)(x,y)\in\mathcal{P}(u\_{\min}-h,\ u\_{\max}+h) with d=y−xd=y-x, we perform a binary search on 𝒰\mathcal{U} to locate
𝒰∩[d−h,d+h]\mathcal{U}\cap[d-h,d+h], which costs O​(log⁡M)O(\log M), and then update all grid points in that subarray.
Let Mh:=supu∈ℝ|𝒰∩[u−h,u+h]|M\_{h}:=\sup\_{u\in\mathbb{R}}|\mathcal{U}\cap[u-h,u+h]| denote the maximum local grid occupancy at scale hh.
Thus, the total complexity is bounded by

|  |  |  |
| --- | --- | --- |
|  | O​(n1​log⁡n2+Npairs​(umin−h,umax+h)​(log⁡M+Mh)).O\!\left(n\_{1}\log n\_{2}+N\_{\mathrm{pairs}}(u\_{\min}-h,\ u\_{\max}+h)\bigl(\log M+M\_{h}\bigr)\right). |  |

This is significantly faster than the naive O​(M⋅Npairs​(umin−h,umax+h))O\!\left(M\cdot N\_{\mathrm{pairs}}(u\_{\min}-h,\ u\_{\max}+h)\right) approach when Mh≪MM\_{h}\ll M,
which typically occurs when the bandwidth hh is small.
As suggested by Theorem [4.1](https://arxiv.org/html/2601.01871v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 New estimator ‣ On lead-lag estimation of non-synchronously observed point processes"), small bandwidths are desirable in practice, especially when gg exhibits a sharp peak,
where the proposed implementation yields a substantial computational gain.

### B.2 Finding the maximizer of g^h\hat{g}\_{h}

To compute the estimator θ^h\hat{\theta}\_{h}, we need to find the global maximizer of g^h​(u)\hat{g}\_{h}(u) within the range [−r,r][-r,r].
The objective function g^h\hat{g}\_{h} may have many local optima, making it difficult for standard numerical optimization to converge to the global maximum.
However, when KK is piecewise linear, g^h​(u)\hat{g}\_{h}(u) is also piecewise linear.
Hence, a maximizer over [−r,r][-r,r] can be found by evaluating g^h\hat{g}\_{h} only at the kink locations induced by the differences d=y−xd=y-x,
x∈𝒯1x\in\mathcal{T}\_{1}, y∈𝒯2y\in\mathcal{T}\_{2}.

Let 𝒟r,h:=𝒟​(−r−h,r+h)\mathcal{D}\_{r,h}:=\mathcal{D}(-r-h,\ r+h) denote the set of lag differences in the window [−r−h,r+h][-r-h,r+h].
In particular, for the triangular kernel Ktri​(x)=(1−|x|)​𝟏[−1,1]​(x)K^{\mathrm{tri}}(x)=(1-|x|)\mathbf{1}\_{[-1,1]}(x), the function may change slope only at
u=d−h,u=d,u=d+hu=d-h,\ u=d,\ u=d+h for each lag difference d∈𝒟r,hd\in\mathcal{D}\_{r,h}.
Therefore, to obtain the maximizer θ^h\hat{\theta}\_{h}, it suffices to evaluate g^h\hat{g}\_{h} on the candidate set

|  |  |  |
| --- | --- | --- |
|  | 𝒰kink:=(𝒟r,h∪(𝒟r,h+h)∪(𝒟r,h−h)∪{−r,r})∩[−r,r].\mathcal{U}\_{\mathrm{kink}}:=\Bigl(\mathcal{D}\_{r,h}\ \cup\ \bigl(\mathcal{D}\_{r,h}+h\bigr)\ \cup\ \bigl(\mathcal{D}\_{r,h}-h\bigr)\cup\ \{-r,r\}\Bigr)\cap[-r,r]. |  |

In an implementation, it is recommended to remove duplicates in 𝒰kink\mathcal{U}\_{\mathrm{kink}}
before sorting; otherwise the grid may contain repeated points and incur unnecessary work.

##### Computational complexity.

The set 𝒟r,h\mathcal{D}\_{r,h} can be constructed while enumerating the relevant pairs 𝒫​(−r−h,r+h)\mathcal{P}(-r-h,r+h), which takes
O​(Npairs​(−r−h,r+h))O\!\left(N\_{\mathrm{pairs}}(-r-h,\ r+h)\right) time up to constant-factor overhead.
Building 𝒰kink\mathcal{U}\_{\mathrm{kink}} from 𝒟r,h\mathcal{D}\_{r,h} is linear in |𝒰kink||\mathcal{U}\_{\mathrm{kink}}|, and we may sort
𝒰kink\mathcal{U}\_{\mathrm{kink}} once to apply Algorithm [1](https://arxiv.org/html/2601.01871v1#alg1 "Algorithm 1 ‣ B.1 Algorithm for computing 𝑔̂_ℎ on a grid ‣ Appendix B Implementation and computational complexity ‣ On lead-lag estimation of non-synchronously observed point processes").
Evaluating g^h\hat{g}\_{h} on 𝒰kink\mathcal{U}\_{\mathrm{kink}} using Algorithm [1](https://arxiv.org/html/2601.01871v1#alg1 "Algorithm 1 ‣ B.1 Algorithm for computing 𝑔̂_ℎ on a grid ‣ Appendix B Implementation and computational complexity ‣ On lead-lag estimation of non-synchronously observed point processes") has the same form as above, with MM replaced by
|𝒰kink||\mathcal{U}\_{\mathrm{kink}}| and with MhM\_{h} defined as above but computed on the grid 𝒰kink\mathcal{U}\_{\mathrm{kink}}:

|  |  |  |
| --- | --- | --- |
|  | O​(n1​log⁡n2+Npairs​(−r−h,r+h)​(log⁡|𝒰kink|+Mh)).O\!\left(n\_{1}\log n\_{2}+N\_{\mathrm{pairs}}(-r-h,\ r+h)\bigl(\log|\mathcal{U}\_{\mathrm{kink}}|+M\_{h}\bigr)\right). |  |

Finally, the maximizer is obtained by a single pass over the evaluated values, which costs O​(|𝒰kink|)O(|\mathcal{U}\_{\mathrm{kink}}|).

##### Scaling in TT and hh.

For the simple stationary bivariate point process N=(N1,N2)N=(N\_{1},N\_{2}) with intensities λ1,λ2\lambda\_{1},\lambda\_{2} and CPCF gg, we have E⁡[ni]=λi​T\operatorname{E}[n\_{i}]=\lambda\_{i}T for i=1,2i=1,2.
Moreover, by the definition of the cross-intensity function, we have

|  |  |  |
| --- | --- | --- |
|  | E⁡[Npairs​(a,b)]=∫(0,T]2𝟏​{y−x∈[a,b]}​λ12​(y−x)​𝑑x​𝑑y≈λ1​λ2​T​∫abg​(u)​𝑑u.\operatorname{E}\!\left[N\_{\mathrm{pairs}}(a,b)\right]=\int\_{(0,T]^{2}}\mathbf{1}\{y-x\in[a,b]\}\,\lambda\_{12}(y-x)\,dx\,dy\approx\lambda\_{1}\lambda\_{2}\,T\int\_{a}^{b}g(u)\,du. |  |

If T≫r+hT\gg r+h and [a,b]⊂[−r−h,r+h][a,b]\subset[-r-h,r+h], then E⁡[Npairs​(a,b)]≍λ1​λ2​T​∫abg​(u)​𝑑u\operatorname{E}[N\_{\mathrm{pairs}}(a,b)]\asymp\lambda\_{1}\lambda\_{2}\,T\int\_{a}^{b}g(u)\,du.
In particular,

|  |  |  |
| --- | --- | --- |
|  | E⁡[Npairs​(−r−h,r+h)]=O​(T),E⁡[n1​log⁡n2]=O​(T​log⁡T),\operatorname{E}\!\left[N\_{\mathrm{pairs}}(-r-h,r+h)\right]=O(T),\qquad\operatorname{E}[n\_{1}\log n\_{2}]=O(T\log T), |  |

where the hidden constant depends on gg through its mass on [−r−h,r+h][-r-h,r+h].

Next, note that |𝒰kink|≤3​|𝒟r,h|+2≤3​Npairs​(−r−h,r+h)+2|\mathcal{U}\_{\mathrm{kink}}|\leq 3|\mathcal{D}\_{r,h}|+2\leq 3N\_{\mathrm{pairs}}(-r-h,r+h)+2,
so |𝒰kink|=O​(T)|\mathcal{U}\_{\mathrm{kink}}|=O(T) in expectation, and the one-time sorting cost is O​(T​log⁡T)O(T\log T).
For the local update cost on the kink grid, observe that for any u∈[−r,r]u\in[-r,r],

|  |  |  |
| --- | --- | --- |
|  | |𝒰kink∩[u−h,u+h]|≤ 3​|𝒟r,h∩[u−2​h,u+2​h]|+2≤ 3​Npairs​(u−2​h,u+2​h)+2.|\mathcal{U}\_{\mathrm{kink}}\cap[u-h,u+h]|\;\leq\;3\,|\mathcal{D}\_{r,h}\cap[u-2h,u+2h]|+2\;\leq\;3\,N\_{\mathrm{pairs}}(u-2h,u+2h)+2. |  |

Taking expectations yields

|  |  |  |
| --- | --- | --- |
|  | E⁡[|𝒰kink∩[u−h,u+h]|]=O​(T​∫u−2​hu+2​hg​(v)​𝑑v).\operatorname{E}\!\left[|\mathcal{U}\_{\mathrm{kink}}\cap[u-h,u+h]|\right]=O\!\left(T\int\_{u-2h}^{u+2h}g(v)\,dv\right). |  |

Taking the supremum over u∈[−r,r]u\in[-r,r] gives the worst-case bound

|  |  |  |
| --- | --- | --- |
|  | Mh=O​(T​supu∈[−r,r]∫u−2​hu+2​hg​(v)​𝑑v).M\_{h}=O\!\left(T\sup\_{u\in[-r,r]}\int\_{u-2h}^{u+2h}g(v)\,dv\right). |  |

In particular, if gg is bounded (e.g., under [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(i)), then
∫u−2​hu+2​hg​(v)​𝑑v=O​(h)\int\_{u-2h}^{u+2h}g(v)\,dv=O(h) uniformly in uu, so Mh=O​(T​h)M\_{h}=O(Th) and the expected time bound
reduces to O​(T​log⁡T+T2​h)O(T\log T+T^{2}h).
If gg is unbounded at θ∗\theta^{\ast} as in [[A2]](https://arxiv.org/html/2601.01871v1#S3.I2.i1 "Item [A2] ‣ 3 Proposed framework ‣ On lead-lag estimation of non-synchronously observed point processes")(ii), then
∫θ∗−2​hθ∗+2​hg​(v)​𝑑v=O​(hα)\int\_{\theta^{\ast}-2h}^{\theta^{\ast}+2h}g(v)\,dv=O(h^{\alpha}).
Thus, we may have Mh=O​(T​hα)M\_{h}=O(Th^{\alpha}), leading to an expected time bound of O​(T​log⁡T+T2​hα)O(T\log T+T^{2}h^{\alpha}).
On the other hand, the naive implementation costs O​(Npairs×|𝒰kink|)≈O​(T2)O(N\_{\mathrm{pairs}}\times|\mathcal{U}\_{\mathrm{kink}}|)\approx O(T^{2}).

## Appendix C Bandwidth selection by cross-validation

In this section, we introduce additional bandwidth-selection methods for the estimator θ^h\hat{\theta}\_{h} based on cross-validation and assess their performance in simulation studies.

In the context of modal regression, chen2016nonparametric propose choosing the bandwidth by minimizing the size of prediction sets associated with the modal regression function, while zhou2019bandwidth introduce a cross-validation criterion (CVM) that penalizes the squared distance between the responses and the estimated modal set and includes an explicit penalty for the number of modes.
Motivated by these developments, we design a cross-validation scheme that directly evaluates how well the maximizer set obtained from the training part of the point process predicts the empirical lag differences observed in the test part.

Fix an integer Kcv≥2K\_{\mathrm{cv}}\geq 2 and split the observation window [0,T][0,T] into KcvK\_{\mathrm{cv}} disjoint subintervals
I1,…,IKcvI\_{1},\dots,I\_{K\_{\mathrm{cv}}} of equal length. Here KcvK\_{\mathrm{cv}} denotes the number of folds. For the jjth fold, we regard IjI\_{j} as a test interval and
[0,T]∖Ij[0,T]\setminus I\_{j} as the corresponding training interval.
On the training interval we compute the kernel estimator g^h(−j)\hat{g}\_{h}^{(-j)} based on
N∩([0,T]∖Ij)N\cap([0,T]\setminus I\_{j}) and its (possibly set-valued) maximizer set

|  |  |  |
| --- | --- | --- |
|  | Mh(−j):=arg​maxu∈[−r,r]⁡g^h(−j)​(u),h∈ℋT,M\_{h}^{(-j)}:=\operatorname\*{arg\,max}\_{u\in[-r,r]}\hat{g}^{(-j)}\_{h}(u),\qquad h\in\mathcal{H}\_{T}, |  |

where ℋT\mathcal{H}\_{T} is the finite bandwidth grid.

For a set
M⊂[−r,r]M\subset[-r,r] and z∈ℝz\in\mathbb{R} we write

|  |  |  |
| --- | --- | --- |
|  | d​(z,M):=infu∈M|z−u|d(z,M):=\inf\_{u\in M}|z-u| |  |

for the distance from zz to MM. Given a test interval IjI\_{j}, we define the set of observed lag
differences restricted to [−r,r][-r,r] by

|  |  |  |
| --- | --- | --- |
|  | Δj(r):={y−x;x∈𝒯1,j,y∈𝒯2,j,−r≤y−x≤r},\Delta\_{j}(r):=\bigl\{y-x;x\in\mathcal{T}\_{1,j},\ y\in\mathcal{T}\_{2,j},\ -r\leq y-x\leq r\bigr\}, |  |

where 𝒯i,j\mathcal{T}\_{i,j} denotes the (finite) set of event times of NiN\_{i} that fall in IjI\_{j}
for i∈{1,2}i\in\{1,2\}. We interpret Δj​(r)\Delta\_{j}(r) as a multiset, i.e., lag differences are counted
with multiplicity, and write nj:=|Δj​(r)|n\_{j}:=|\Delta\_{j}(r)| for the number of elements.
In practice, the fold length should be chosen large relative to rr so that each IjI\_{j} contains
enough pairs with lag in [−r,r][-r,r].
When nj≥1n\_{j}\geq 1, we enumerate the elements of Δj​(r)\Delta\_{j}(r) as (dj,1,…,dj,nj)(d\_{j,1},\dots,d\_{j,n\_{j}}) (in an arbitrary order) and introduce the
distances

|  |  |  |
| --- | --- | --- |
|  | δj,ℓ​(M):=d​(dj,ℓ,M),ℓ=1,…,nj,\delta\_{j,\ell}(M):=d(d\_{j,\ell},M),\qquad\ell=1,\dots,n\_{j}, |  |

with order statistics
δj,(1)​(M)≤⋯≤δj,(nj)​(M)\delta\_{j,(1)}(M)\leq\cdots\leq\delta\_{j,(n\_{j})}(M).
Fix a trimming parameter τ∈(0,1]\tau\in(0,1] and a minimum count nmin∈ℕn\_{\min}\in\mathbb{N}, and set

|  |  |  |
| --- | --- | --- |
|  | kj:=max⁡{⌈τ​nj⌉,nmin},εj​(M):={δj,(kj)​(M),nj≥kj,+∞,nj<kj.k\_{j}:=\max\{\lceil\tau n\_{j}\rceil,\ n\_{\min}\},\qquad\varepsilon\_{j}(M):=\begin{cases}\delta\_{j,(k\_{j})}(M),&n\_{j}\geq k\_{j},\\[2.0pt] +\infty,&n\_{j}<k\_{j}.\end{cases} |  |

If nj<kjn\_{j}<k\_{j}, we set Lnearest​(M;Ij)=+∞L\_{\mathrm{nearest}}(M;I\_{j})=+\infty, regardless of MM, effectively discarding bandwidths for which the test fold contains too few lag differences.
Under this notation, we consider the following loss functions on IjI\_{j} for a finite candidate maximizer set M⊂[−r,r]M\subset[-r,r] (so |M||M| is its cardinality):

* •

  MSE-type loss:

  |  |  |  |
  | --- | --- | --- |
  |  | Lmse​(M;Ij):=|M|2nj​∑ℓ=1njδj,ℓ​(M)2,L\_{\mathrm{mse}}(M;I\_{j}):=\frac{|M|^{2}}{n\_{j}}\sum\_{\ell=1}^{n\_{j}}\delta\_{j,\ell}(M)^{2}, |  |

  with the convention that folds with nj=0n\_{j}=0 are excluded from the CV average.
  The factor |M|2|M|^{2} penalizes bandwidths that produce many maximizers, playing a stabilizing role in the spirit of zhou2019bandwidth.
* •

  Nearest-range loss:

  |  |  |  |
  | --- | --- | --- |
  |  | Lnearest​(M;Ij):=Leb​({x∈ℝ:d​(x,M)≤εj​(M)}).L\_{\mathrm{nearest}}(M;I\_{j}):=\mathrm{Leb}\bigl(\{x\in\mathbb{R}:d(x,M)\leq\varepsilon\_{j}(M)\}\bigr). |  |

  The set
  {x∈ℝ:d​(x,M)≤ε}\{x\in\mathbb{R}:d(x,M)\leq\varepsilon\} is the ε\varepsilon-neighborhood of MM, and
  Leb​(⋅)\mathrm{Leb}(\cdot) is its total length. By construction, εj​(M)\varepsilon\_{j}(M) is chosen
  so that at least kj=max⁡{⌈τ​nj⌉,nmin}k\_{j}=\max\{\lceil\tau n\_{j}\rceil,n\_{\min}\} of the test lag differences
  lie within distance εj​(M)\varepsilon\_{j}(M) of MM, so Lnearest​(M;Ij)L\_{\mathrm{nearest}}(M;I\_{j}) is the
  length of the smallest neighborhood of MM covering that trimmed fraction. The minimum
  count nminn\_{\min} improves numerical stability. This loss function is based on the
  prediction set approach of chen2016nonparametric.

Let J:={j∈{1,…,Kcv}:nj≥1}J:=\{j\in\{1,\dots,K\_{\mathrm{cv}}\}:n\_{j}\geq 1\} denote the set of folds with at least one lag
difference in [−r,r][-r,r].
Given a choice of loss function L∈{Lmse,Lnearest}L\in\{L\_{\mathrm{mse}},L\_{\mathrm{nearest}}\}, we define the
KcvK\_{\mathrm{cv}}-fold CV score for h∈ℋTh\in\mathcal{H}\_{T} by

|  |  |  |
| --- | --- | --- |
|  | CV​(h):=1|J|​∑j∈JL​(Mh(−j);Ij).\mathrm{CV}(h):=\frac{1}{|J|}\sum\_{j\in J}L\bigl(M\_{h}^{(-j)};I\_{j}\bigr). |  |

Our cross-validated bandwidth is then chosen as

|  |  |  |
| --- | --- | --- |
|  | h^CV∈arg⁡minh∈ℋT⁡CV​(h)\hat{h}\_{\mathrm{CV}}\in\arg\min\_{h\in\mathcal{H}\_{T}}\mathrm{CV}(h) |  |

If the minimizer is not unique, we select the smallest hh in ℋT\mathcal{H}\_{T}.
We finally obtain the adaptive estimator θ^h^CV\hat{\theta}\_{\hat{h}\_{\mathrm{CV}}}.

To compare the performance of different loss functions and their accompanying tuning parameters, we conduct a series of simulation experiments under the following common design. The candidate bandwidths are h∈{10−1,10−2,10−3,10−4,10−5,10−6}h\in\{10^{-1},10^{-2},10^{-3},10^{-4},10^{-5},10^{-6}\}, r=1r=1, and the observation window is [0,T][0,T]. The observation horizon takes the values T∈{1000,2000,4000,8000}T\in\{1000,2000,4000,8000\}; for each combination of model, estimator, and TT, we generate 50005000 Monte Carlo replicates.
The cross-validation criteria considered are the nearest-range loss LnearestL\_{\mathrm{nearest}} with trimming levels τ∈{0.01,0.025,0.05}\tau\in\{0.01,0.025,0.05\} and the MSE-type loss LmseL\_{\mathrm{mse}}.
For comparison, we also include the Lepski selector with AT=log⁡log⁡TA\_{T}=\log\log T.
In the plots, the nearest-range CV curves for different τ\tau are distinguished by a red color gradient; the MSE-based CV curves are shown in blue; and the curve of the Lepski estimator is shown in green.
We set Kcv=5K\_{\mathrm{cv}}=5 and nmin=5n\_{\min}=5. For reference, each panel also shows the theoretical rate T−1/βαT^{-1/\beta\_{\alpha}} as a black dashed line.

![Refer to caption](simulations/graphs/sensitivity_cv_all_scenarios_nearest2-mse-lepski_loglogt.png)


Figure 6: Performance comparisons between the bandwidth-selection methods across scenarios: RMSE versus TT on log–log axes for CV using LnearestL\_{\mathrm{nearest}} (red gradient by τ\tau), CV using LmseL\_{\mathrm{mse}} (blue), and Lepski’s method with AT=log⁡log⁡TA\_{T}=\log\log T (green); the dashed black line shows the theoretical rate T−1/βαT^{-1/\beta\_{\alpha}}.

Figure [6](https://arxiv.org/html/2601.01871v1#A3.F6 "Figure 6 ‣ Appendix C Bandwidth selection by cross-validation ‣ On lead-lag estimation of non-synchronously observed point processes") compares the finite-sample performance of the different bandwidth selection schemes across the six data-generating models described in Section [5.1](https://arxiv.org/html/2601.01871v1#S5.SS1 "5.1 Models ‣ 5 Simulation study ‣ On lead-lag estimation of non-synchronously observed point processes"). Several systematic patterns emerge.

First, the cross-validation criterion based on the MSE-type loss is somewhat unstable.
In five out of the six models, the RMSE of the MSE-CV estimator decreases only slowly, and sometimes not at all, as TT increases, compared to the theoretical slope. This suggests that the MSE-type loss is not well-suited to selecting the bandwidth for our cases.

The nearest-range loss LnearestL\_{\mathrm{nearest}} behaves more favorably, but its performance depends on the trimming parameter τ\tau. For models with sharper CPCFs, i.e., with α\alpha smaller than 11, smaller values of τ\tau tend to work better.
In contrast, for smoother models with α>1\alpha>1, larger values of τ\tau become competitive or even preferable.
In other words, the optimal choice of τ\tau appears to be α\alpha-dependent: aggressive trimming is beneficial when gg has a very sharp peak, whereas milder trimming is adequate when gg is flatter around its maximum.
A notable exception is the asymmetric Hawkes model (hawkes\_gamma\_asym).
In this case, the nearest-range CV estimator improves more slowly and less regularly with TT
across the τ\tau-values considered. One possible contributing factor is that
LnearestL\_{\mathrm{nearest}} is built from symmetric neighborhoods of the estimated maximizer set,
while the within-fold lag differences in this asymmetric setting may be skewed in finite samples;
in such cases, symmetric neighborhoods may be less informative for selecting hh.

When compared with the Lepski-type procedure, the nearest-range CV estimator is inferior in the small-α\alpha models. Indeed, for hawkes\_gamma\_sym, hawkes\_gamma\_asym, and ns\_gamma\_1, the Lepski estimator shows lower RMSE.
For smoother models with α>1\alpha>1, however, the best-tuned nearest-range CV estimator becomes competitive.
Overall, these experiments indicate that cross-validation based on LnearestL\_{\mathrm{nearest}} is a promising alternative, but it may require a delicate choice of τ\tau.

Taken together, our findings suggest the following practical recommendation.
Among the bandwidth selectors we have examined, the Lepski method stands out as the most robust option. It requires only the slowly diverging threshold ATA\_{T}, shows stable behavior across all models, and nearly attains the minimax rate T−1/βαT^{-1/\beta\_{\alpha}} both theoretically and in numerical experiments.
Nearest-range cross-validation can be competitive, especially for smoother CPCFs, but it requires
choosing the trimming level τ\tau in addition to the bandwidth, and its best choice is not yet
well understood theoretically.
For this reason, we currently recommend the Lepski-type bandwidth choice as a default method for estimating the lead-lag time.

##### Acknowledgements

We thank participants at the “Big Data and Artificial Intelligence in Econometrics, Finance, and Statistics” workshop at University of Chicago, October 2-4, 2025, the quantitative finance seminar at National University of Singapore, October 24, 2025, the KAKENHI symposium at Tsukuba University, October 30-31, 2025, Nakanoshima Workshop at Osaka University, December 5-6, 2025, and CFE-CMStatistics 2025 at University of London, December 13-15, 2025, for insightful comments and constructive suggestions on this work.
Takaaki Shiotani’s work was partly supported by Grant-in-Aid for JSPS Fellows (25KJ0933) and World-leading Innovative Graduate Study for Frontiers of Mathematical Sciences and Physics.
Yuta Koike’s work was partly supported by JST CREST Grant Number JPMJCR2115 and JSPS KAKENHI Grant Numbers JP22H00834, JP22H01139.