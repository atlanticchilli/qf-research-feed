---
authors:
- Steven Campbell
- Ting-Kam Leonard Wong
doc_id: arxiv:2510.25740v1
family_id: arxiv:2510.25740
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A mathematical study of the excess growth rate
url_abs: http://arxiv.org/abs/2510.25740v1
url_html: https://arxiv.org/html/2510.25740v1
venue: arXiv q-fin
version: 1
year: 2025
---


Steven Campbell
Department of Statistics, Columbia University
[sc5314@columbia.edu](mailto:sc5314@columbia.edu)
 and 
Ting-Kam Leonard Wong
Department of Statistical Sciences, University of Toronto
[tkl.wong@utoronto.ca](mailto:tkl.wong@utoronto.ca)

###### Abstract.

We study the excess growth rate—a fundamental logarithmic functional arising in portfolio theory—from the perspective of information theory. We show that the excess growth rate can be connected to the Rényi and cross entropies, the Helmholtz free energy, L. Campbell’s measure of average code length and large deviations. Our main results consist of three axiomatic characterization theorems of the excess growth rate, in terms of (i) the relative entropy, (ii) the gap in Jensen’s inequality, and (iii) the logarithmic divergence that generalizes the Bregman divergence. Furthermore, we study maximization of the excess growth rate and compare it with the growth optimal portfolio. Our results not only provide theoretical justifications of the significance of the excess growth rate, but also establish new connections between information theory and quantitative finance.

###### Key words and phrases:

Excess growth rate, axiomatic characterization, relative entropy, Jensen gap, logarithmic divergence, functional equation, large deviation

## 1. Introduction

This paper offers a mathematical study of the excess growth rate that originated from portfolio theory and, as we will show, has rich connections with information theory and geometry, probability, and statistical physics. We aim to: (i) demonstrate these relations; (ii) formulate and prove axiomatic characterization theorems of the excess growth rate; and (iii) study maximization of the (expected) excess growth rate.

To motivate the definition of the excess growth rate, consider n≥1n\geq 1 financial assets, such as stocks, whose prices are strictly positive. The case n=1n=1 is both financially and mathematically trivial, but is included for completeness. Throughout this paper, we denote the closed and open unit simplex in ℝn\mathbb{R}^{n} by

|  |  |  |  |
| --- | --- | --- | --- |
| (1.1) |  | Δn:={𝐱∈[0,1]n:∑i=1nxi=1},Δn∘:={𝐱∈(0,1]n:∑i=1nxi=1},\Delta\_{n}:=\left\{\mathbf{x}\in[0,1]^{n}:\sum\_{i=1}^{n}x\_{i}=1\right\},\quad\Delta\_{n}^{\circ}:=\left\{\mathbf{x}\in(0,1]^{n}:\sum\_{i=1}^{n}x\_{i}=1\right\}, |  |

where 𝐱=(x1,…,xn)\mathbf{x}=(x\_{1},\ldots,x\_{n}).111We adopt the convention that Δ1=Δ1∘:={1}\Delta\_{1}=\Delta\_{1}^{\circ}:=\{1\} and thus use (0,1](0,1] in the definition of Δn∘\Delta\_{n}^{\circ}. For a given holding period like a month, let 𝝅=(π1,…,πn)∈Δn\boldsymbol{\pi}=(\pi\_{1},\ldots,\pi\_{n})\in\Delta\_{n} be the vector of initial portfolio weights, so that πi≥0\pi\_{i}\geq 0 is the initial proportion of wealth invested in asset ii. By construction, we have ∑i=1nπi=1\sum\_{i=1}^{n}\pi\_{i}=1. Suppose Ri∈(0,∞)R\_{i}\in(0,\infty) is the gross return of asset ii over the holding period. That is, an investment of one dollar yields RiR\_{i} dollars at the end of the holding period. Then ∑i=1nπi​Ri\sum\_{i=1}^{n}\pi\_{i}R\_{i} is the gross return of the portfolio, and log⁡(∑i=1nπi​Ri)\log\left(\sum\_{i=1}^{n}\pi\_{i}R\_{i}\right) is its log return. By Jensen’s inequality, this is greater than or equal to ∑i=1nπi​log⁡Ri\sum\_{i=1}^{n}\pi\_{i}\log R\_{i}, the weighted average log return of the assets. The excess growth rate Γ​(𝝅,𝐑)\Gamma(\boldsymbol{\pi},\mathbf{R}) is defined as the gap log⁡(∑i=1nπi​Ri)−∑i=1nπi​log⁡Ri\log\left(\sum\_{i=1}^{n}\pi\_{i}R\_{i}\right)-\sum\_{i=1}^{n}\pi\_{i}\log R\_{i}.

For technical purposes, in Definition [1.1](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem1 "Definition 1.1 (Excess growth rate). ‣ 1. Introduction ‣ A mathematical study of the excess growth rate") below we shall allow Ri=0R\_{i}=0 whenever πi=0\pi\_{i}=0. For 𝐱∈[0,∞)n\mathbf{x}\in[0,\infty)^{n}, let supp⁡(𝐱)⊆[n]:={1,…,n}\operatorname{supp}(\mathbf{x})\subseteq[n]:=\{1,\ldots,n\} be the support of 𝐱\mathbf{x} defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (1.2) |  | supp⁡(𝐱):={i∈[n]:xi>0}.\operatorname{supp}(\mathbf{x}):=\{i\in[n]:x\_{i}>0\}. |  |

(Our notations are consistent with those in Leinster’s book [[38](https://arxiv.org/html/2510.25740v1#bib.bib38)].) Define

|  |  |  |  |
| --- | --- | --- | --- |
| (1.3) |  | 𝒟n:={(𝝅,𝐑)∈Δn×[0,∞)n:supp⁡(𝝅)⊂supp⁡(𝐑)}\mathcal{D}\_{n}:=\{(\boldsymbol{\pi},\mathbf{R})\in\Delta\_{n}\times[0,\infty)^{n}:\operatorname{supp}(\boldsymbol{\pi})\subset\operatorname{supp}(\mathbf{R})\} |  |

as well as the slice

|  |  |  |  |
| --- | --- | --- | --- |
| (1.4) |  | 𝒟n​(𝝅∣⋅):={𝐑∈[0,∞)n:(𝝅,𝐑)∈𝒟n}.\begin{split}\mathcal{D}\_{n}(\boldsymbol{\pi}\mid\cdot)&:=\{\mathbf{R}\in[0,\infty)^{n}:(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n}\}.\end{split} |  |

###### Definition 1.1 (Excess growth rate).

For n≥1n\geq 1 and (𝛑,𝐑)∈𝒟n(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n}, we define the excess growth rate of 𝐑\mathbf{R} weighted by 𝛑\boldsymbol{\pi} by

|  |  |  |  |
| --- | --- | --- | --- |
| (1.5) |  | Γ​(𝝅,𝐑):=log⁡(∑i∈supp⁡(𝝅)πi​Ri)−∑i∈supp⁡(𝝅)πi​log⁡Ri.\Gamma(\boldsymbol{\pi},\mathbf{R}):=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}R\_{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log R\_{i}. |  |

An empirical illustration using US stock data is given in Figure [1](https://arxiv.org/html/2510.25740v1#S2.F1 "Figure 1 ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") in Section [2.1](https://arxiv.org/html/2510.25740v1#S2.SS1 "2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"). By an abuse of notation (following again [[38](https://arxiv.org/html/2510.25740v1#bib.bib38)]), we use the same symbol Γ\Gamma for each of the functions Γ=Γn:𝒟n→ℝ+:=[0,∞)\Gamma=\Gamma\_{n}:\mathcal{D}\_{n}\rightarrow\mathbb{R}\_{+}:=[0,\infty), n≥1n\geq 1. Note that similar conventions are used throughout information theory. For example, the symbol H​(𝐩∥𝐪)H(\mathbf{p}\;\|\;\mathbf{q}) is used to denote the relative entropy regardless of the dimension. We write Γn\Gamma\_{n} (and similarly for other quantities) if there is a need to emphasize the dimension.

Since Ri>0R\_{i}>0 whenever i∈supp⁡(𝝅)i\in\operatorname{supp}(\boldsymbol{\pi}), the right hand side of ([1.5](https://arxiv.org/html/2510.25740v1#S1.E5 "In Definition 1.1 (Excess growth rate). ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")) is well-defined and finite. We may express the excess growth rate probabilistically as

|  |  |  |  |
| --- | --- | --- | --- |
| (1.6) |  | Γ​(𝝅,𝐑)=φ​(𝔼𝝅​[R])−𝔼𝝅​[φ​(R)],\Gamma(\boldsymbol{\pi},\mathbf{R})=\varphi(\mathbb{E}\_{\boldsymbol{\pi}}[R])-\mathbb{E}\_{\boldsymbol{\pi}}[\varphi(R)], |  |

where RR is a non-negative random variable with probability mass function ℙ𝝅​(R=Ri)=πi\mathbb{P}\_{\boldsymbol{\pi}}(R=R\_{i})=\pi\_{i}, and φ​(⋅)=log⁡(⋅)\varphi(\cdot)=\log(\cdot) is the logarithm. Since log⁡(⋅)\log(\cdot) is strictly concave, Γ​(𝝅,𝐑)=0\Gamma(\boldsymbol{\pi},\mathbf{R})=0 if and only if RR is constant on supp⁡(𝝅)\operatorname{supp}(\boldsymbol{\pi}). When n=1n=1 the simplex Δn\Delta\_{n} reduces to a singleton, and the excess growth rate vanishes identically.

###### Remark 1.2.

1. (i)

   Note that

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (1.7) |  | eΓ​(𝝅,𝐑)=∑i∈supp⁡(𝝅)πi​Ri∏i∈supp⁡(𝝅)Riπie^{\Gamma(\boldsymbol{\pi},\mathbf{R})}=\frac{\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}R\_{i}}{\prod\_{i\in\operatorname{supp}(\boldsymbol{\pi})}R\_{i}^{\pi\_{i}}} |  |

   is the ratio between the arithmetic and geometric means of the gross returns weighted by 𝝅\boldsymbol{\pi}. The non-negativity of Γ​(𝝅,𝐑)\Gamma(\boldsymbol{\pi},\mathbf{R}) can also be seen from the inequality of arithmetic and geometric means.
2. (ii)

   Let (𝝅,𝐑)∈𝒟n(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n} and define 𝐫=log⁡𝐑:=(log⁡Ri)1≤i≤n∈[−∞,∞)n\mathbf{r}=\log\mathbf{R}:=(\log R\_{i})\_{1\leq i\leq n}\in[-\infty,\infty)^{n}. Thus, ri=log⁡Rir\_{i}=\log R\_{i} is the log return of asset ii and conversely 𝐑=e𝐫:=(eri)1≤i≤n∈𝒟n​(𝝅∣⋅)\mathbf{R}=e^{\mathbf{r}}:=(e^{r\_{i}})\_{1\leq i\leq n}\in\mathcal{D}\_{n}(\boldsymbol{\pi}\mid\cdot) (we let log⁡x=−∞\log x=-\infty if x≤0x\leq 0 and e−∞=0e^{-\infty}=0). The excess growth rate can be expressed in terms of the log returns as

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (1.8) |  | γ​(𝝅,𝐫):=log⁡(∑i∈supp⁡(𝐩)πi​eri)−∑i∈supp⁡(𝐩)πi​ri,\gamma(\boldsymbol{\pi},\mathbf{r}):=\log\left(\sum\_{i\in\operatorname{supp}(\mathbf{p})}\pi\_{i}e^{r\_{i}}\right)-\sum\_{i\in\operatorname{supp}(\mathbf{p})}\pi\_{i}r\_{i}, |  |

   which is the difference between the exponential mean222This is also the (weighted) log–sum–exp function which is popular in machine learning. log⁡(∑i∈supp⁡(𝐩)πi​eri)\log\left(\sum\_{i\in\operatorname{supp}(\mathbf{p})}\pi\_{i}e^{r\_{i}}\right) and the arithmetic mean of 𝐫\mathbf{r} weighted by 𝝅\boldsymbol{\pi}. In Section [3.2](https://arxiv.org/html/2510.25740v1#S3.SS2 "3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") we briefly discuss the exponential mean as a member of the family of quasiarithmetic means. Note that γ​(𝝅,𝐫)\gamma(\boldsymbol{\pi},\mathbf{r}) is convex in 𝐫\mathbf{r} when 𝝅\boldsymbol{\pi} is fixed, and concave in 𝝅\boldsymbol{\pi} when 𝐫\mathbf{r} is fixed. Taylor expanding ([1.8](https://arxiv.org/html/2510.25740v1#S1.E8 "In item (ii) ‣ Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")) about 𝐫=0\mathbf{r}=0 shows that

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (1.9) |  | γ​(𝝅,𝐫)=∑i∈supp⁡(𝐩)πi​ri2−(∑i∈supp⁡(𝐩)πi​ri)2+o​(∑i∈supp⁡(𝐩)ri2).\gamma(\boldsymbol{\pi},\mathbf{r})=\sum\_{i\in\operatorname{supp}(\mathbf{p})}\pi\_{i}r\_{i}^{2}-\left(\sum\_{i\in\operatorname{supp}(\mathbf{p})}\pi\_{i}r\_{i}\right)^{2}+o\left(\sum\_{i\in\operatorname{supp}(\mathbf{p})}r\_{i}^{2}\right). |  |

   The leading order term, which is quadratic in 𝐫\mathbf{r}, is the variance of 𝐫\mathbf{r} weighted by 𝝅\boldsymbol{\pi}. In Section [3.3](https://arxiv.org/html/2510.25740v1#S3.SS3 "3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") we relate this expansion with the Fisher–Rao metric.
3. (iii)

   The excess growth rate can be extended beyond the discrete setting. In particular, ([1.6](https://arxiv.org/html/2510.25740v1#S1.E6 "In 1. Introduction ‣ A mathematical study of the excess growth rate")) makes sense if we let 𝝅\boldsymbol{\pi} be a probability measure on a measurable space 𝒳\mathcal{X}, and RR be a non-negative random variable on 𝒳\mathcal{X} such that R>0R>0 𝝅\boldsymbol{\pi}-almost surely. In this paper we focus on the discrete setting.

It is also useful to think of the excess growth rate as a divergence between the initial prices 𝐗\mathbf{X} and the final prices 𝐘\mathbf{Y}. As we shall see, this is analogous to the relative entropy which is a divergence between a pair of probability distributions.

###### Definition 1.3 (Excess growth rate as a divergence).

For n≥1n\geq 1 and 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n}, we define Γ𝛑(⋅∥⋅):𝒟(𝛑∣⋅)×𝒟(𝛑∣⋅)→ℝ+\Gamma\_{\boldsymbol{\pi}}(\cdot\;\|\;\cdot):\mathcal{D}(\boldsymbol{\pi}\mid\cdot)\times\mathcal{D}(\boldsymbol{\pi}\mid\cdot)\rightarrow\mathbb{R}\_{+} by

|  |  |  |  |
| --- | --- | --- | --- |
| (1.10) |  | Γ𝝅​(𝐘∥𝐗):=log⁡(∑i∈supp⁡(𝝅)πi​YiXi)−∑i∈supp⁡(𝝅)πi​log⁡YiXi,\Gamma\_{\boldsymbol{\pi}}(\mathbf{Y}\;\|\;\mathbf{X}):=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\frac{Y\_{i}}{X\_{i}}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log\frac{Y\_{i}}{X\_{i}}, |  |

where 𝐗=(X1,…,Xn)\mathbf{X}=(X\_{1},\ldots,X\_{n}) and 𝐘=(Y1,…,Yn)\mathbf{Y}=(Y\_{1},\ldots,Y\_{n}).

Clearly, we have Γπ​(a​𝐘∥a​𝐗)=Γ𝝅​(𝐘∥𝐗)\Gamma\_{\pi}(a\mathbf{Y}\;\|\;a\mathbf{X})=\Gamma\_{\boldsymbol{\pi}}(\mathbf{Y}\;\|\;\mathbf{X}) for a>0a>0. This is a special case of numéraire invariance which will be proved in Proposition [2.3](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem3 "Proposition 2.3 (Numéraire invariance). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") below. It is also clear that generally Γ𝝅​(𝐘∥𝐗)≠Γ𝝅​(𝐗∥𝐘)\Gamma\_{\boldsymbol{\pi}}(\mathbf{Y}\;\|\;\mathbf{X})\neq\Gamma\_{\boldsymbol{\pi}}(\mathbf{X}\;\|\;\mathbf{Y}). Financially, this means that the excess growth rate is not invariant under time reversal, as expected.

To the best of our knowledge, the concept of “excess growth” in finance was first introduced (in a continuous time set-up using stochastic calculus) in [[32](https://arxiv.org/html/2510.25740v1#bib.bib32)]. Later, it became an essential concept in stochastic portfolio theory [[26](https://arxiv.org/html/2510.25740v1#bib.bib26), [30](https://arxiv.org/html/2510.25740v1#bib.bib30)]. Independently, the authors of [[8](https://arxiv.org/html/2510.25740v1#bib.bib8)] introduced the quantity Γ​(𝝅,𝐑)\Gamma(\boldsymbol{\pi},\mathbf{R}) and called it the diversification return. Our definition follows that of [[48](https://arxiv.org/html/2510.25740v1#bib.bib48)]. Also see [[54](https://arxiv.org/html/2510.25740v1#bib.bib54)] for a textbook treatment in which the term volatility effect is used. Further discussion of the related literature will be given in Section [2.1](https://arxiv.org/html/2510.25740v1#S2.SS1 "2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), where we establish several properties of the excess growth rate, including a new chain rule (Theorem [2.5](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem5 "Theorem 2.5 (Chain rule (general)). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), and briefly explain some financial applications.

The excess growth rate does not only appear in finance.
In the rest of Section [2](https://arxiv.org/html/2510.25740v1#S2 "2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), we show that it can be readily linked to various concepts in information theory, statistical physics and probability. In particular, we show:

* •

  the excess growth rate can be interpreted in terms of the Helmholtz free energy, and has a variational representation (Section [2.2](https://arxiv.org/html/2510.25740v1#S2.SS2 "2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"));
* •

  the difference between L. Campbell’s measure of average code length [[15](https://arxiv.org/html/2510.25740v1#bib.bib15)] and Shannon’s one can be expressed in terms of the excess growth rate (Section [2.3](https://arxiv.org/html/2510.25740v1#S2.SS3 "2.3. Information-theoretic interpretation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"));
* •

  the excess growth rate emerges in a large deviation principle of the scaled Dirichlet distribution (Definition [2.10](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem10 "Definition 2.10 (Scaled Dirichlet distribution). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), analogous to how the relative entropy features in Sanov’s theorem (Section [2.4](https://arxiv.org/html/2510.25740v1#S2.SS4 "2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")).

Several more connections, including correspondences with the Rényi divergence and cross-entropy, and the logarithmic divergence [[49](https://arxiv.org/html/2510.25740v1#bib.bib49), [50](https://arxiv.org/html/2510.25740v1#bib.bib50), [63](https://arxiv.org/html/2510.25740v1#bib.bib63)] in information geometry, can also be found in the paper. In fact, the excess growth rate can be expressed directly in terms of the relative entropy using algebraic operations on the simplex in compositional data analysis (Lemma [3.4](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem4 "Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")). Nevertheless, our body of results go well beyond this identity.

In Section [3](https://arxiv.org/html/2510.25740v1#S3 "3. Characterization theorems ‣ A mathematical study of the excess growth rate"), we present a collection of three novel axiomatic characterization theorems that uniquely determine the excess growth rate (possibly up to a multiplicative constant) based on natural invariance and analytic properties. Axiomatic characterizations of various information-theoretic quantities have been studied by many researchers, beginning with Shannon himself [[59](https://arxiv.org/html/2510.25740v1#bib.bib59), Theorem 2] (another classic is Rényi’s paper [[56](https://arxiv.org/html/2510.25740v1#bib.bib56)]). To give a flavor of some of the ideas involved, consider the fundamental additive property of the Shannon entropy:

|  |  |  |
| --- | --- | --- |
|  | H​(𝐩⊗𝐪)=H​(𝐩)+H​(𝐪),H(\mathbf{p}\otimes\mathbf{q})=H(\mathbf{p})+H(\mathbf{q}), |  |

where 𝐩⊗𝐪\mathbf{p}\otimes\mathbf{q} denotes the product distribution. This property is closely related to the functional equation f​(x​y)=f​(x)+f​(y)f(xy)=f(x)+f(y), x,y>0x,y>0, whose general solution (assuming only that f:(0,∞)→ℝf:(0,\infty)\rightarrow\mathbb{R} is Lebesgue measurable) is f​(x)=c​log⁡xf(x)=c\log x, c∈ℝc\in\mathbb{R}.333This functional equation is equivalent to Cauchy’s equation ([3.13](https://arxiv.org/html/2510.25740v1#S3.E13 "In 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) which plays an important role in the proof of our second characterization theorem. A comprehensive mathematical study of axiomatic characterizations of information measures and related quantities, as well as detailed historical discussions, can be found in Leinster’s book [[38](https://arxiv.org/html/2510.25740v1#bib.bib38)] which is primarily motivated by diversity measures in biology. In fact, Leinster’s book provided the initial impetus for the development of this paper.444We thank Martin Larsson for bringing this reference to our attention. For more recent axiomatic characterizations we refer the reader to [[9](https://arxiv.org/html/2510.25740v1#bib.bib9)] and the references therein.

Our three characterization theorems highlight different aspects of the excess growth rate and further reinforce its importance. They also differ from existing axiomatic characterizations of the exponential mean (see Remark [1.2](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem2 "Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate") and a discussion in Section [3.2](https://arxiv.org/html/2510.25740v1#S3.SS2 "3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")). We state the main ideas of our characterizations as follows:

* •

  Our first characterization (Theorem [3.20](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem20 "Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), proved in Section [3.1](https://arxiv.org/html/2510.25740v1#S3.SS1 "3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), shows that the excess growth rate is completely determined by the financial properties established in Section [2.1](https://arxiv.org/html/2510.25740v1#S2.SS1 "2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"). Our proof is based on a characterization of relative entropy, its relation with the excess growth rate (Lemma [3.4](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem4 "Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), as well as a delicate analysis of boundary values.
* •

  In Section [3.2](https://arxiv.org/html/2510.25740v1#S3.SS2 "3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), we provide an axiomatic characterization (Theorem [3.13](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem13 "Theorem 3.13 (Characterization II). ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) of the gap in Jensen’s inequality ([1.6](https://arxiv.org/html/2510.25740v1#S1.E6 "In 1. Introduction ‣ A mathematical study of the excess growth rate")), for a general “generating function” φ\varphi, and show in this setting that the logarithmic case φ​(⋅)=c​log⁡(⋅)\varphi(\cdot)=c\log(\cdot), which leads to the excess growth rate, is characterized by numéraire invariance.
* •

  In Section [3.3](https://arxiv.org/html/2510.25740v1#S3.SS3 "3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), we exploit the fact that the excess growth rate is a member of the family of logarithmic divergences introduced by Pal and the second author [[49](https://arxiv.org/html/2510.25740v1#bib.bib49)] (this is analogous to the fact that the relative entropy on the simplex is a Bregman divergence). We show in Theorem [3.20](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem20 "Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") that the excess growth rate is the unique logarithmic divergence which is perturbation invariant; this is closely related to numéraire invariance. A by-product of this result is a characterization of (negative) cross-entropy within the family of exponentially concave functions on the simplex.

The significance of the excess growth rate in portfolio selection leads naturally to maximization of this quantity. In Section [4](https://arxiv.org/html/2510.25740v1#S4 "4. Optimization ‣ A mathematical study of the excess growth rate") we study two versions of this problem, first in a deterministic setting (max𝝅∈Δn⁡γ​(𝝅,𝐫)\max\_{\boldsymbol{\pi}\in\Delta\_{n}}\gamma(\boldsymbol{\pi},\mathbf{r}) where 𝐫\mathbf{r} is fixed), then in a probabilistic setting where we maximize the expected excess growth rate 𝔼​[γ​(𝝅,𝐫)]\mathbb{E}[\gamma(\boldsymbol{\pi},\mathbf{r})] assuming 𝐫\mathbf{r} is a random vector. In the deterministic case, we derive an explicit characterization of the solution and, via a variational representation, link it with the perspective function in convex analysis. In the probabilistic case, we derive a first-order condition for the optimizer and compare this problem with the classical growth optimal portfolio [[17](https://arxiv.org/html/2510.25740v1#bib.bib17), Chapter 16].

As discussed in Remark [1.4](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem4 "Remark 1.4 (Information theory and quantitative finance). ‣ 1. Introduction ‣ A mathematical study of the excess growth rate") below, information theory and quantitative finance share deep connections. In this paper, we show that the excess growth rate fosters new synergies between the two fields. Our results suggest many directions for future research, some of which are discussed in Section [5](https://arxiv.org/html/2510.25740v1#S5 "5. Conclusion ‣ A mathematical study of the excess growth rate").

###### Remark 1.4 (Information theory and quantitative finance).

Interactions between information theory and quantitative finance began soon after Shannon’s inaugural paper [[59](https://arxiv.org/html/2510.25740v1#bib.bib59)]. In [[36](https://arxiv.org/html/2510.25740v1#bib.bib36)], Kelly showed that in repeated investment or gambling situations, the value of side information can be quantified by *mutual information*, a fundamental information-theoretic quantity that arises in the definition of channel capacity. Kelly’s work (and that of Breiman [[14](https://arxiv.org/html/2510.25740v1#bib.bib14)] among others) led to the concept of *growth optimal portfolio*, also called the *numéraire portfolio*, which has profound implications in finance [[40](https://arxiv.org/html/2510.25740v1#bib.bib40)]. Intuitively, optimal investment and information theory are intimately related because successful investment and efficient data transmission/extraction both hinge on predicting the future (asset returns or source alphabets). Among the many subsequent works, we highlight [[2](https://arxiv.org/html/2510.25740v1#bib.bib2)] which investigates the *asymptotic equipartition property* in the context of growth optimal investment, and the *universal portfolio* [[17](https://arxiv.org/html/2510.25740v1#bib.bib17)] which is the financial analogue of universal coding. In [[47](https://arxiv.org/html/2510.25740v1#bib.bib47)], it was shown that regret
guarantees of universal portfolio algorithms imply time-uniform
concentration inequalities for bounded random variables. For further details and other classical connections, we refer the reader to Chapters 6 and 16 of [[17](https://arxiv.org/html/2510.25740v1#bib.bib17)]. Recently, the financial perspective on information theory has been fruitfully extended to optimal hypothesis testing using *ee-values* [[37](https://arxiv.org/html/2510.25740v1#bib.bib37), [55](https://arxiv.org/html/2510.25740v1#bib.bib55)].

## 2. Excess growth rate: properties and interpretations

In this section, we study several properties of the excess growth rate, and show that it arises naturally not only in finance but also in statistical physics, information theory, and probability theory.

### 2.1. Basic properties and financial intuition

We establish some mathematical properties of the excess growth rate, some of which were given in [[48](https://arxiv.org/html/2510.25740v1#bib.bib48)]. All of these properties have clear financial meanings that will be carefully explained. In Section [3.1](https://arxiv.org/html/2510.25740v1#S3.SS1 "3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), we show that these properties (as well as Lebesgue measurability) uniquely characterize the excess growth rate up to a multiplicative constant.

We begin with two properties that are immediate from the definition. Given 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and a permutation σ\sigma of [n][n], we define

|  |  |  |
| --- | --- | --- |
|  | 𝐱​σ:=(xσ​(1),…,xσ​(n))∈ℝn.\mathbf{x}\sigma:=(x\_{\sigma(1)},\ldots,x\_{\sigma(n)})\in\mathbb{R}^{n}. |  |

###### Proposition 2.1 (Permutation invariance).

For any (𝛑,𝐑)∈𝒟n(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n} and permutation σ\sigma of [n][n], we have Γ​(𝛑​σ,𝐑​σ)=Γ​(𝛑,𝐑)\Gamma(\boldsymbol{\pi}\sigma,\mathbf{R}\sigma)=\Gamma(\boldsymbol{\pi},\mathbf{R}).

###### Proposition 2.2 (Dependence on support).

For 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n} and 𝐑,𝐑′∈𝒟n​(𝛑∣⋅)\mathbf{R},\mathbf{R}^{\prime}\in\mathcal{D}\_{n}(\boldsymbol{\pi}\mid\cdot), we have Γ​(𝛑,𝐑)=Γ​(𝛑,𝐑′)\Gamma(\boldsymbol{\pi},\mathbf{R})=\Gamma(\boldsymbol{\pi},\mathbf{R}^{\prime}) if Ri=Ri′R\_{i}=R\_{i}^{\prime} for i∈supp⁡(𝛑)i\in\operatorname{supp}(\boldsymbol{\pi}). In particular, Γ​(𝛑,𝐑)=0\Gamma(\boldsymbol{\pi},\mathbf{R})=0 if 𝐑\mathbf{R} is constant on supp⁡(𝛑)\operatorname{supp}(\boldsymbol{\pi}).

Together, Propositions [2.1](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem1 "Proposition 2.1 (Permutation invariance). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") and [2.2](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem2 "Proposition 2.2 (Dependence on support). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") state that the excess growth rate is invariant under relabeling the assets (and their returns), and depends only on the assets whose holdings are strictly positive.

###### Proposition 2.3 (Numéraire invariance).

For (𝛑,𝐑)∈𝒟n(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n} and a>0a>0, we have
Γ​(𝛑,a​𝐑)=Γ​(𝛑,𝐑)\Gamma(\boldsymbol{\pi},a\mathbf{R})=\Gamma(\boldsymbol{\pi},\mathbf{R}). Equivalently, we have
Γ𝛑​(b​𝐘∥a​𝐗)=Γ𝛑​(𝐘∥𝐗)\Gamma\_{\boldsymbol{\pi}}(b\mathbf{Y}\;\|\;a\mathbf{X})=\Gamma\_{\boldsymbol{\pi}}(\mathbf{Y}\;\|\;\mathbf{X}) for any 𝐗,𝐘∈𝒟n​(𝛑∣⋅)\mathbf{X},\mathbf{Y}\in\mathcal{D}\_{n}(\boldsymbol{\pi}\mid\cdot) and a,b>0a,b>0.

###### Proof.

From ([1.5](https://arxiv.org/html/2510.25740v1#S1.E5 "In Definition 1.1 (Excess growth rate). ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")) and the additive property of logarithms, we have

|  |  |  |
| --- | --- | --- |
|  | Γ​(𝝅,a​𝐑)=log⁡(∑i∈supp⁡(𝝅)πi​(a​Ri))−∑i∈supp⁡(𝝅)πi​log⁡(a​Ri)=log⁡(∑i∈supp⁡(𝝅)πi​Ri)+log⁡a−∑i∈supp⁡(𝝅)πi​log⁡Ri−log⁡a=Γ​(𝝅,𝐑).∎\begin{split}\Gamma(\boldsymbol{\pi},a\mathbf{R})&=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}(aR\_{i})\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log(aR\_{i})\\ &=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}R\_{i}\right)+\log a-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log R\_{i}-\log a\\ &=\Gamma(\boldsymbol{\pi},\mathbf{R}).\qed\end{split} |  |

Here is the financial interpretation of Proposition [2.3](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem3 "Proposition 2.3 (Numéraire invariance). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"). Suppose that that we express the gross return RiR\_{i} of asset i∈supp⁡(𝝅)i\in\operatorname{supp}(\boldsymbol{\pi}) as YiXi\frac{Y\_{i}}{X\_{i}}, where XiX\_{i} and YiY\_{i} are, respectively, the initial and final prices. For concreteness, let us fix XiX\_{i} and YiY\_{i} as the dollar values. In financial terms, we say that the numéraire is cash (with respect to a fixed currency). Now, suppose that we measure prices in terms of another asset (e.g. the value of the S&P500 Index) whose price moves from QQ to Q′Q^{\prime}, both of which are assumed to be positive. That is, we define the relative prices of asset ii by X~i=Xi/Q\tilde{X}\_{i}=X\_{i}/Q and Y~i=Yi/Q′\tilde{Y}\_{i}=Y\_{i}/Q^{\prime}; these are the prices under the new numéraire. Then, the relative gross return is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | R~i:=Y~iX~i=Yi/Q′Xi/Q=QQ′​YiXi=QQ′​Ri.\tilde{R}\_{i}:=\frac{\tilde{Y}\_{i}}{\tilde{X}\_{i}}=\frac{Y\_{i}/Q^{\prime}}{X\_{i}/Q}=\frac{Q}{Q^{\prime}}\frac{Y\_{i}}{X\_{i}}=\frac{Q}{Q^{\prime}}R\_{i}. |  |

Thus, we have 𝐑~:=(R~1,…,R~n)=a​𝐑\tilde{\mathbf{R}}:=(\tilde{R}\_{1},\ldots,\tilde{R}\_{n})=a\mathbf{R}, where a=QQ′>0a=\frac{Q}{Q^{\prime}}>0. Numéraire invariance states that the excess growth rate is independent of the choice of the numéraire. This property makes the excess growth rate an appropriate measure of relative volatility which is different from the more familiar absolute volatility. For example, suppose that all assets fall by 50%50\% in dollar value. Then, the market is volatile in absolute terms, but there is no relative volatility. In particular, all portfolios of these assets earn the same return −50%-50\% regardless of their allocation.

By numéraire invariance, for each nn, the function Γ:𝒟n→ℝ+\Gamma:\mathcal{D}\_{n}\rightarrow\mathbb{R}\_{+} is characterized by its restriction to

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | 𝒜n:=𝒟n∩(Δn×Δn).\mathcal{A}\_{n}:=\mathcal{D}\_{n}\cap(\Delta\_{n}\times\Delta\_{n}). |  |

We define the slice 𝒜n​(𝝅∣⋅)\mathcal{A}\_{n}(\boldsymbol{\pi}\mid\cdot) analogously (see ([1.9](https://arxiv.org/html/2510.25740v1#S1.E9 "In item (ii) ‣ Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate"))). Specifically, for (𝝅,𝐑)∈𝒟n(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | Γ​(𝝅,𝐑)=Γ​(𝝅,𝒞𝝅​[𝐑]),\Gamma(\boldsymbol{\pi},\mathbf{R})=\Gamma(\boldsymbol{\pi},\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{R}]), |  |

where 𝒞𝝅:𝒟n​(𝝅∣⋅)→𝒜n​(𝝅∣⋅)\mathcal{C}\_{\boldsymbol{\pi}}:\mathcal{D}\_{n}(\boldsymbol{\pi}\mid\cdot)\rightarrow\mathcal{A}\_{n}(\boldsymbol{\pi}\mid\cdot) is the closure with respect to (the support of) 𝝅\boldsymbol{\pi}, defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | (𝒞𝝅​[𝐱])i:={xi/∑j∈supp⁡(𝝅)xj,if ​i∈supp⁡(𝝅),0,otherwise.\left(\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{x}]\right)\_{i}:=\left\{\begin{array}[]{ll}x\_{i}/\sum\_{j\in\operatorname{supp}(\boldsymbol{\pi})}x\_{j},&\text{if }i\in\operatorname{supp}(\boldsymbol{\pi}),\\ 0,&\text{otherwise.}\\ \end{array}\right. |  |

If the relevant support is [n][n] (so that 𝐱∈(0,∞)n\mathbf{x}\in(0,\infty)^{n}), we simply write 𝒞​[𝐱]\mathcal{C}[\mathbf{x}] which is an element of Δn∘\Delta\_{n}^{\circ}. We introduce several related algebraic operations for later use:

* •

  Hadamard (componentwise) product:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.5) |  | (𝐱𝐲)i:=xi​yi,𝐱,𝐲∈ℝn.(\mathbf{x}\mathbf{y})\_{i}:=x\_{i}y\_{i},\quad\mathbf{x},\mathbf{y}\in\mathbb{R}^{n}. |  |
* •

  Componentwise inverse:

  |  |  |  |
  | --- | --- | --- |
  |  | (𝐱−1)i:=1xi,𝐱∈(0,∞)n.(\mathbf{x}^{-1})\_{i}:=\frac{1}{x\_{i}},\quad\mathbf{x}\in(0,\infty)^{n}. |  |
* •

  Perturbation operation with respect to 𝝅∈Δn\boldsymbol{\pi}\in\Delta\_{n}:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝐱⊕𝝅𝐲:=𝒞𝝅​[𝐱𝐲],𝐱,𝐲∈𝒜n​(𝝅∣⋅).\mathbf{x}\oplus\_{\boldsymbol{\pi}}\mathbf{y}:=\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{x}\mathbf{y}],\quad\mathbf{x},\mathbf{y}\in\mathcal{A}\_{n}(\boldsymbol{\pi}\mid\cdot). |  |

  We write 𝐱⊕𝐲\mathbf{x}\oplus\mathbf{y} when the support is [n][n].
* •

  Powering operation:

  |  |  |  |
  | --- | --- | --- |
  |  | α⊗𝐱:=𝒞​[(xiα)1≤i≤n],(𝐱,α)∈Δn∘×ℝ.\alpha\otimes\mathbf{x}:=\mathcal{C}[(x\_{i}^{\alpha})\_{1\leq i\leq n}],\quad(\mathbf{x},\alpha)\in\Delta\_{n}^{\circ}\times\mathbb{R}. |  |

It is well known in compositional data analysis [[1](https://arxiv.org/html/2510.25740v1#bib.bib1), [24](https://arxiv.org/html/2510.25740v1#bib.bib24), [25](https://arxiv.org/html/2510.25740v1#bib.bib25)] that the open simplex Δn∘\Delta\_{n}^{\circ} becomes an (n−1)(n-1)-dimensional real vector space if we regard ⊕\oplus as vector addition and ⊗\otimes as scalar multiplication. The additive identity (zero element) is the barycenter 𝐞¯=𝐞¯n:=(1n,…,1n)\bar{\mathbf{e}}=\bar{\mathbf{e}}\_{n}:=(\frac{1}{n},\ldots,\frac{1}{n}), and vector subtraction is given by

|  |  |  |
| --- | --- | --- |
|  | 𝐱⊖𝐲:=𝒞​[𝐱𝐲−1],𝐱,𝐲∈Δn∘.\mathbf{x}\ominus\mathbf{y}:=\mathcal{C}[\mathbf{x}\mathbf{y}^{-1}],\quad\mathbf{x},\mathbf{y}\in\Delta\_{n}^{\circ}. |  |

For a general 𝝅∈Δn\boldsymbol{\pi}\in\Delta\_{n} (whose support may be a strict subset of [n][n]), and for 𝐱,𝐲∈𝒜n​(𝝅∣⋅)\mathbf{x},\mathbf{y}\in\mathcal{A}\_{n}(\boldsymbol{\pi}\mid\cdot), we define the generalized difference 𝐱⊖𝝅𝐲∈𝒜n​(𝝅∣⋅)\mathbf{x}\ominus\_{\boldsymbol{\pi}}\mathbf{y}\in\mathcal{A}\_{n}(\boldsymbol{\pi}\mid\cdot) by

|  |  |  |
| --- | --- | --- |
|  | (𝐱⊖𝝅𝐲)i:={(xi/yi)/∑j∈supp⁡(𝝅)(xj/yj),if ​i∈supp⁡(𝝅),0,otherwise.(\mathbf{x}\ominus\_{\boldsymbol{\pi}}\mathbf{y})\_{i}:=\left\{\begin{array}[]{ll}(x\_{i}/y\_{i})/\sum\_{j\in\operatorname{supp}(\boldsymbol{\pi})}(x\_{j}/y\_{j}),&\text{if }i\in\operatorname{supp}(\boldsymbol{\pi}),\\ 0,&\text{otherwise.}\\ \end{array}\right. |  |

The chain rules, to be stated next, tell us how to decompose the excess growth rate of a composite portfolio, i.e., a portfolio of portfolios. These are the key properties in our first characterization of the excess growth rate in Section [3.1](https://arxiv.org/html/2510.25740v1#S3.SS1 "3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

Let n,k1,…,kn≥1n,k\_{1},\ldots,k\_{n}\geq 1 be integers and let

|  |  |  |
| --- | --- | --- |
|  | 𝝅∈Δn,𝐩1∈Δk1,…,𝐩n∈Δkn.\boldsymbol{\pi}\in\Delta\_{n},\quad\mathbf{p}^{1}\in\Delta\_{k\_{1}},\ldots,\mathbf{p}^{n}\in\Delta\_{k\_{n}}. |  |

Write 𝐩i=(p1i,…,pkii)\mathbf{p}^{i}=(p\_{1}^{i},\ldots,p\_{k\_{i}}^{i}) and 𝐩=(𝐩1,…,𝐩n)\mathbf{p}=(\mathbf{p}^{1},\ldots,\mathbf{p}^{n}). The composite distribution 𝝅∘𝐩\boldsymbol{\pi}\circ\mathbf{p} is

|  |  |  |  |
| --- | --- | --- | --- |
| (2.6) |  | 𝝅∘𝐩:=(π1​p11,…,π1​pk11,…,πn​p1n,…,πn​pknn)=(π1​𝐩1,…,πn​𝐩n)∈Δk1+⋯+kn.\begin{split}\boldsymbol{\pi}\circ\mathbf{p}&:=(\pi\_{1}p\_{1}^{1},\ldots,\pi\_{1}p\_{k\_{1}}^{1},\ldots,\pi\_{n}p\_{1}^{n},\ldots,\pi\_{n}p\_{k\_{n}}^{n})\\ &=(\pi\_{1}\mathbf{p}^{1},\ldots,\pi\_{n}\mathbf{p}^{n})\in\Delta\_{k\_{1}+\cdots+k\_{n}}.\end{split} |  |

We index its components by (𝝅,𝐩)i,j=πi​pji(\boldsymbol{\pi},\mathbf{p})\_{i,j}=\pi\_{i}p\_{j}^{i}, where (i,j)∈[n]×[ki](i,j)\in[n]\times[k\_{i}]. Financially, we may think of the ii-th conditional distribution 𝐩i\mathbf{p}^{i} as a portfolio consisting of kik\_{i} assets, and the composite portfolio holds the nn portfolios as individual assets. We allow some of the assets to overlap. For example, the capital corresponding to the weights p11p\_{1}^{1} and p12p\_{1}^{2} can be invested in the same asset. This can be enforced by letting the gross returns R11R\_{1}^{1} and R12R\_{1}^{2} be equal.

The following version of the chain rule was formulated in [[48](https://arxiv.org/html/2510.25740v1#bib.bib48)]. Throughout the paper, we denote the Euclidean inner product by ⟨𝐱,𝐲⟩\langle\mathbf{x},\mathbf{y}\rangle.

###### Proposition 2.4 (Chain rule (first version)).

Let n,k1,…,kn≥1n,k\_{1},\ldots,k\_{n}\geq 1,

|  |  |  |
| --- | --- | --- |
|  | 𝝅∈Δn,𝐩=(𝐩1,…,𝐩n)∈Δk1×⋯×Δkn,\boldsymbol{\pi}\in\Delta\_{n},\quad\mathbf{p}=(\mathbf{p}^{1},\ldots,\mathbf{p}^{n})\in\Delta\_{k\_{1}}\times\cdots\times\Delta\_{k\_{n}}, |  |

and let

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(𝐑1,…,𝐑n)∈∏i=1n𝒟ki​(𝐩i∣⋅).\mathbf{R}=(\mathbf{R}^{1},\ldots,\mathbf{R}^{n})\in\prod\_{i=1}^{n}\mathcal{D}\_{k\_{i}}(\mathbf{p}^{i}\mid\cdot). |  |

Denote

|  |  |  |
| --- | --- | --- |
|  | ⟨⟨𝐩,𝐑⟩⟩:=(⟨𝐩1,𝐑1⟩,…,⟨𝐩n,𝐑n⟩)∈(0,∞)n.\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle:=(\langle\mathbf{p}^{1},\mathbf{R}^{1}\rangle,\ldots,\langle\mathbf{p}^{n},\mathbf{R}^{n}\rangle)\in(0,\infty)^{n}. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | Γ​(𝝅∘𝐩,𝐑)=Γ​(𝝅,⟨⟨𝐩,𝐑⟩⟩)+∑i∈supp⁡(𝝅)πi​Γ​(𝐩i,𝐑i).\begin{split}&\Gamma(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{R})=\Gamma(\boldsymbol{\pi},\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle)+\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\Gamma(\mathbf{p}^{i},\mathbf{R}^{i}).\end{split} |  |

Consider a portfolio of k1+⋯+knk\_{1}+\cdots+k\_{n} assets with weights 𝝅∘𝐩\boldsymbol{\pi}\circ\mathbf{p}. Its excess growth rate is equal to Γ​(𝝅∘𝐩,𝐑)\Gamma(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{R}). The chain rule states that we may decompose it as a sum of two parts. First, consider the portfolio of portfolios, where “asset ii” is the ii-th portfolio with gross return ⟨𝐩i,𝐑i⟩\langle\mathbf{p}^{i},\mathbf{R}^{i}\rangle. This gives the excess growth rate Γ​(𝝅,⟨⟨𝐩,𝐑⟩⟩)\Gamma(\boldsymbol{\pi},\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle). Note that the gross returns RjiR\_{j}^{i} of the individual “atomic” assets enter indirectly through ⟨⟨𝐩,𝐑⟩⟩\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle (in [[38](https://arxiv.org/html/2510.25740v1#bib.bib38)] this property is called modularity). The second term is the weighted sum of the excess growth rates Γ​(𝐩i,𝐑i)\Gamma(\mathbf{p}^{i},\mathbf{R}^{i}) of the individual portfolios. The reader should note that this property is reminiscent of the chain rule of relative entropy (see ([3.4](https://arxiv.org/html/2510.25740v1#S3.E4 "In item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"))). The precise algebraic relationships between the relative entropy and excess growth rate are given in Lemma [3.4](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem4 "Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

###### Proof of Proposition [2.4](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem4 "Proposition 2.4 (Chain rule (first version)). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate").

By definition of Γ​(𝝅∘𝐩,𝐑)\Gamma(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{R}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(𝝅∘𝐩,𝐑)=log⁡(∑i∈supp⁡(𝝅)∑j∈supp⁡(𝐩i)πi​pji​Rji)−∑i∈supp⁡(𝝅)∑j∈supp⁡(𝐩i)πi​pji​log⁡Rji.log⁡(∑i∈supp⁡(𝝅)πi​⟨𝐩i,𝐑i⟩)−∑i∈supp⁡(𝝅)πi​(∑j∈supp⁡(𝐩i)pji​log⁡Rji)=log⁡(∑i∈supp⁡(𝝅)πi​⟨𝐩i,𝐑i⟩)−∑i∈supp⁡(𝝅)πi​log⁡⟨𝐩i,𝐑i⟩+∑i∈supp⁡(𝝅)πi​(log⁡⟨𝐩i,𝐑i⟩−∑j∈supp⁡(𝐩i)pji​log⁡Rji)=Γ​(𝝅,⟨⟨𝐩,𝐑⟩⟩)+∑i∈supp⁡(𝝅)πi​Γ​(𝐩i,𝐑i).∎\displaystyle\begin{split}&\Gamma(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{R})\\ &=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\sum\_{j\in\operatorname{supp}(\mathbf{p}^{i})}\pi\_{i}p\_{j}^{i}R\_{j}^{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\sum\_{j\in\operatorname{supp}(\mathbf{p}^{i})}\pi\_{i}p\_{j}^{i}\log R\_{j}^{i}.\\ &\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\langle\mathbf{p}^{i},\mathbf{R}^{i}\rangle\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\left(\sum\_{j\in\operatorname{supp}(\mathbf{p}^{i})}p\_{j}^{i}\log R\_{j}^{i}\right)\\ &=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\langle\mathbf{p}^{i},\mathbf{R}^{i}\rangle\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log\langle\mathbf{p}^{i},\mathbf{R}^{i}\rangle\\ &\quad+\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\left(\log\langle\mathbf{p}^{i},\mathbf{R}^{i}\rangle-\sum\_{j\in\operatorname{supp}(\mathbf{p}^{i})}p\_{j}^{i}\log R\_{j}^{i}\right)\\ &=\Gamma(\boldsymbol{\pi},\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle)+\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\Gamma(\mathbf{p}^{i},\mathbf{R}^{i}).\qed\end{split} | |  |

Our characterization theorem in Section [3.1](https://arxiv.org/html/2510.25740v1#S3.SS1 "3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") requires a more general version of the chain rule. To motivate it, we extend the financial context of ([2.4](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem4 "Proposition 2.4 (Chain rule (first version)). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")). Now, suppose that the nn portfolios hold assets in nn countries with different currencies (or, more generally, different numéraires). To compute the excess growth rate of the composite portfolio, we need to express all returns using a common currency (numéraire). In the statement below, we think of ai≥0a\_{i}\geq 0 as the conversion factor for the assets in the ii-th portfolio; when ai>0a\_{i}>0, it plays the role of the factor QQ′\frac{Q}{Q^{\prime}} in ([2.1](https://arxiv.org/html/2510.25740v1#S2.E1 "In 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")).

###### Theorem 2.5 (Chain rule (general)).

Let n,k1,…,kn≥1n,k\_{1},\ldots,k\_{n}\geq 1,

|  |  |  |
| --- | --- | --- |
|  | 𝝅∈Δn,𝐩=(𝐩1,…,𝐩n)∈Δk1×⋯×Δkn,\boldsymbol{\pi}\in\Delta\_{n},\quad\mathbf{p}=(\mathbf{p}^{1},\ldots,\mathbf{p}^{n})\in\Delta\_{k\_{1}}\times\cdots\times\Delta\_{k\_{n}}, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(𝐑1,…,𝐑n)∈∏i=1n𝒟ki​(𝐩i∣⋅)and𝐚=(a1,…,an)∈𝒟n​(𝝅∣⋅).\mathbf{R}=(\mathbf{R}^{1},\ldots,\mathbf{R}^{n})\in\prod\_{i=1}^{n}\mathcal{D}\_{k\_{i}}(\mathbf{p}^{i}\mid\cdot)\quad\text{and}\quad\mathbf{a}=(a\_{1},\ldots,a\_{n})\in\mathcal{D}\_{n}(\boldsymbol{\pi}\mid\cdot). |  |

Define

|  |  |  |
| --- | --- | --- |
|  | 𝐚∘𝐑:=(a1​𝐑1,…,an​𝐑n)∈𝒟k1+⋯+kn​(𝝅∘𝐩∣⋅).\mathbf{a}\circ\mathbf{R}:=(a\_{1}\mathbf{R}^{1},\ldots,a\_{n}\mathbf{R}^{n})\in\mathcal{D}\_{k\_{1}+\cdots+k\_{n}}(\boldsymbol{\pi}\circ\mathbf{p}\mid\cdot). |  |

Then, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | Γ​(𝝅∘𝐩,𝐚∘𝐑)=Γ​(𝝅,𝐚​⟨⟨𝐩,𝐑⟩⟩)+∑i∈supp⁡(𝝅)πi​Γ​(𝐩i,𝐑i).\Gamma(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{a}\circ\mathbf{R})=\Gamma(\boldsymbol{\pi},\mathbf{a}\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle)+\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\Gamma(\mathbf{p}^{i},\mathbf{R}^{i}). |  |

Here 𝐚​⟨⟨𝐩,𝐑⟩⟩\mathbf{a}\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle is the componentwise product (see ([2.5](https://arxiv.org/html/2510.25740v1#S2.E5 "In 1st item ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"))).

###### Proof.

The proof is similar to that of Proposition [2.4](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem4 "Proposition 2.4 (Chain rule (first version)). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), and proceeds by expanding

|  |  |  |
| --- | --- | --- |
|  | Γ​(𝝅∘𝐩,𝐚∘𝐑)=log⁡(∑i∈supp⁡(𝝅)∑j∈supp⁡(𝐩i)πi​pji​ai​Rji)−∑i∈supp⁡(𝝅)∑j∈supp⁡(𝐩i)πi​pji​log⁡(ai​Rji).\begin{split}&\Gamma(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{a}\circ\mathbf{R})\\ &=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\sum\_{j\in\operatorname{supp}(\mathbf{p}^{i})}\pi\_{i}p\_{j}^{i}a\_{i}R\_{j}^{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\sum\_{j\in\operatorname{supp}(\mathbf{p}^{i})}\pi\_{i}p\_{j}^{i}\log(a\_{i}R\_{j}^{i}).\end{split} |  |

We omit the details of the computation.
∎

###### Remark 2.6.

The general chain rule contains as special cases the first chain rule (Proposition [2.4](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem4 "Proposition 2.4 (Chain rule (first version)). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) and the numéraire invariance property (Proposition [2.3](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem3 "Proposition 2.3 (Numéraire invariance). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")). To recover the first chain rule, let a1=⋯=an=1a\_{1}=\cdots=a\_{n}=1. To recover the numéraire invariance property, let k1=⋯=kn=1k\_{1}=\cdots=k\_{n}=1 and a1=⋯=an=a>0a\_{1}=\cdots=a\_{n}=a>0.

In the remainder of this subsection we discuss briefly two financial applications of the excess growth rate. The reader who is primarily interested in the mathematical development may skip them without loss of continuity.

First, the excess growth rate, when accumulated over time, captures the profit of a portfolio gained by rebalancing. By rebalancing, we mean the adjustment of positions through trading rather than buy-and-hold. The simplest situation, which can be considerably generalized (see [[48](https://arxiv.org/html/2510.25740v1#bib.bib48), [49](https://arxiv.org/html/2510.25740v1#bib.bib49), [64](https://arxiv.org/html/2510.25740v1#bib.bib64)]), is a portfolio that periodically rebalances to the same set of weights. For concreteness, consider a portfolio of nn stocks that rebalances to the weights given by 𝝅∈Δn\boldsymbol{\pi}\in\Delta\_{n} at the beginning of each month. Let 𝐑​(1),…,𝐑​(T)∈(0,∞)n\mathbf{R}(1),\ldots,\mathbf{R}(T)\in(0,\infty)^{n} denote the gross returns of the stocks in TT months, and let 𝐫​(t)=log⁡𝐑​(t)\mathbf{r}(t)=\log\mathbf{R}(t) be the monthly log return. The total gross return of the rebalanced portfolio over TT months is given by compounding the monthly gross returns:555For simplicity, here we assume implicitly that there are no transaction costs.

|  |  |  |
| --- | --- | --- |
|  | ∏t=1T⟨𝝅,𝐑​(t)⟩.\prod\_{t=1}^{T}\langle\boldsymbol{\pi},\mathbf{R}(t)\rangle. |  |

The log return, which is additive over time, is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.9) |  | log⁡(∏t=1T⟨𝝅,𝐑​(t)⟩)=∑t=1Tlog⁡⟨𝝅,𝐑​(t)⟩=∑t=1N(log⁡⟨𝝅,𝐑​(t)⟩−⟨𝝅,𝐫​(t)⟩+⟨𝝅,𝐫​(t)⟩)=⟨𝝅,∑t=1T𝐫​(t)⟩+∑t=1TΓ​(𝝅,𝐑​(t)).\begin{split}\log\left(\prod\_{t=1}^{T}\langle\boldsymbol{\pi},\mathbf{R}(t)\rangle\right)&=\sum\_{t=1}^{T}\log\langle\boldsymbol{\pi},\mathbf{R}(t)\rangle\\ &=\sum\_{t=1}^{N}\left(\log\langle\boldsymbol{\pi},\mathbf{R}(t)\rangle-\langle\boldsymbol{\pi},\mathbf{r}(t)\rangle+\langle\boldsymbol{\pi},\mathbf{r}(t)\rangle\right)\\ &=\left\langle\boldsymbol{\pi},\sum\_{t=1}^{T}\mathbf{r}(t)\right\rangle+\sum\_{t=1}^{T}\Gamma(\boldsymbol{\pi},\mathbf{R}(t)).\end{split} |  |

That is, the log return of the rebalanced portfolio is the sum of the weighted average log return of the stocks and the accumulated excess growth rate. Since the accumulated excess growth rate is increasing, it contributes positively to the portfolio’s log return. In particular, if we consider two price paths along which the stocks have the same initial and final prices, the rebalanced portfolio earns more over the path that has a larger accumulated excess growth rate. This analysis can be expanded to explain the empirical observation that a systematically rebalanced portfolio often (but not always) outperforms a capitalization-weighted benchmark portfolio over long horizons.666This phenomenon is sometimes called volatility pumping or volatility harvesting, see [[10](https://arxiv.org/html/2510.25740v1#bib.bib10), [11](https://arxiv.org/html/2510.25740v1#bib.bib11)] and the references therein. Also see [[58](https://arxiv.org/html/2510.25740v1#bib.bib58)] for a recent empirical study.

![Refer to caption](x1.png)


Figure 1. Excess growth rates of the largest 500500 stocks, over consecutive 2020-day periods and equally weighted, of the US stock market from 19621962 to 20242024. We show both the per period excess growth rate and its aggregate through time.

Second, the excess growth rate, which is invariant under change of numéraire, measures the relative volatility of a stock market. That is, how much the stocks’ returns differ from each other. Intuitively, a market that is relatively volatile offers more opportunities to construct portfolios that may outperform the market. For precise statements in stochastic portfolio theory, see [[27](https://arxiv.org/html/2510.25740v1#bib.bib27), [29](https://arxiv.org/html/2510.25740v1#bib.bib29)] in the references therein. In fact, it can be argued that a portfolio should rebalance more frequently when the market is relatively more volatile, especially when transaction costs cannot be neglected [[50](https://arxiv.org/html/2510.25740v1#bib.bib50), [64](https://arxiv.org/html/2510.25740v1#bib.bib64)]. In Figure [1](https://arxiv.org/html/2510.25740v1#S2.F1 "Figure 1 ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), which adopts the data-set and methodology used in [[16](https://arxiv.org/html/2510.25740v1#bib.bib16), Section 4],777Specifically, we use data from The CRSP US Stock Databases, see <https://www.crsp.org/products/research-products/crsp-us-stock-databases>. The data-set can be processed using codes on the following repository: <https://github.com/stevenacampbell/Macroscopic-Properties-of-Equity-Markets>.. we illustrate the relative volatility of the US stock market. For each (non-overlapping) 2020-day period between 1962 and 2024,888A year has about 252 trading days, or roughly 21 days per month. we identify the returns 𝐑​(t)\mathbf{R}(t) of the 500500 largest stocks of the US stock market, and compute the excess growth rate Γ​(𝝅,𝐑​(t))\Gamma(\boldsymbol{\pi},\mathbf{R}(t)) where 𝝅=𝐞¯500\boldsymbol{\pi}=\bar{\mathbf{e}}\_{500} is equally weighted. Note that due to rank switching (as well as events such as initial public offering and delisting) the set of the top 500500 stocks changes over time. From the figure, we see that the cumulative excess growth rate increases steadily but sometimes abruptly. The series of per period excess growth rate exhibit clustering of volatility which is typical in financial time series. Periods with high relative volatility can often be identified with major economic events such as the financial crisis in 2008 and COVID-19 in early 2020. For other studies of the excess growth rate in financial economics and portfolio management, we refer the reader to [[5](https://arxiv.org/html/2510.25740v1#bib.bib5), [31](https://arxiv.org/html/2510.25740v1#bib.bib31), [41](https://arxiv.org/html/2510.25740v1#bib.bib41), [43](https://arxiv.org/html/2510.25740v1#bib.bib43), [62](https://arxiv.org/html/2510.25740v1#bib.bib62)] and their references.

### 2.2. Free energy and variational representation

We relate the excess growth rate with the Helmholtz free energy and state a variational representation. Recall that the relative entropy
H(⋅∥⋅)H(\cdot\;\|\;\cdot) is given on Δn×Δn\Delta\_{n}\times\Delta\_{n}, n≥1n\geq 1, by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.10) |  | H​(𝐩∥𝐪)={∑i=1npi​log⁡piqi,if ​supp⁡(𝐩)⊂supp⁡(𝐪);+∞,otherwise.H(\mathbf{p}\;\|\;\mathbf{q})=\left\{\begin{array}[]{ll}\sum\_{i=1}^{n}p\_{i}\log\frac{p\_{i}}{q\_{i}},&\text{if }\operatorname{supp}(\mathbf{p})\subset\operatorname{supp}(\mathbf{q});\\ +\infty,&\text{otherwise.}\end{array}\right. |  |

Consider a physical system with nn possible states and let 𝝅∈Δn\boldsymbol{\pi}\in\Delta\_{n} be a reference distribution that represents the multiplicities of states. Let 𝐄=(E1,…,En)∈ℝn\mathbf{E}=(E\_{1},\ldots,E\_{n})\in\mathbb{R}^{n} represent the energies of the states and β>0\beta>0 be the inverse temperature. Consider the (weighted) Gibbs distribution 𝐩⋆=𝐩⋆​(𝝅,𝐄,β)∈Δn\mathbf{p}^{\star}=\mathbf{p}^{\star}(\boldsymbol{\pi},\mathbf{E},\beta)\in\Delta\_{n} given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.11) |  | pi⋆:={1Z​(𝝅,𝐄,β)​πi​e−β​Ei,if ​i∈supp⁡(𝝅);0,otherwise,p\_{i}^{\star}:=\left\{\begin{array}[]{ll}\frac{1}{Z(\boldsymbol{\pi},\mathbf{E},\beta)}\pi\_{i}e^{-\beta E\_{i}},&\text{if }i\in\operatorname{supp}(\boldsymbol{\pi});\\ 0,&\text{otherwise,}\\ \end{array}\right. |  |

where Z​(𝝅,𝐄,β)Z(\boldsymbol{\pi},\mathbf{E},\beta) is the partition function given by

|  |  |  |
| --- | --- | --- |
|  | Z​(𝝅,𝐄,β):=∑j∈supp⁡(𝝅)πj​e−β​Ej.Z(\boldsymbol{\pi},\mathbf{E},\beta):=\sum\_{j\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{j}e^{-\beta E\_{j}}. |  |

By construction, we have supp⁡(𝐩⋆)⊂supp⁡(𝝅)\operatorname{supp}(\mathbf{p}^{\star})\subset\operatorname{supp}(\boldsymbol{\pi}). In this context, the Helmholtz free energy is the quantity

|  |  |  |  |
| --- | --- | --- | --- |
| (2.12) |  | A​(𝝅,𝐄,β):=−1β​log⁡Z​(𝝅,𝐄,β)=−1β​log⁡(∑j∈supp⁡(𝝅)πj​e−β​Ej).A(\boldsymbol{\pi},\mathbf{E},\beta):=-\frac{1}{\beta}\log Z(\boldsymbol{\pi},\mathbf{E},\beta)=\frac{-1}{\beta}\log\left(\sum\_{j\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{j}e^{-\beta E\_{j}}\right). |  |

(See, for example, [[52](https://arxiv.org/html/2510.25740v1#bib.bib52), Chapter 3] for the physical background.) On the other hand, the average energy of the system with respect to the reference distribution 𝝅\boldsymbol{\pi} is given by

|  |  |  |
| --- | --- | --- |
|  | U​(𝝅,𝐄):=∑j∈supp⁡(𝝅)πj​Ej.U(\boldsymbol{\pi},\mathbf{E}):=\sum\_{j\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{j}E\_{j}. |  |

Letting 𝐑=exp⁡(−β​𝐄)∈(0,∞)n\mathbf{R}=\exp(-\beta\mathbf{E})\in(0,\infty)^{n}, we have the identity

|  |  |  |  |
| --- | --- | --- | --- |
| (2.13) |  | Γ​(𝝅,𝐑)=β​(U​(𝝅,𝐄)−A​(𝝅,𝐄,β)).\Gamma(\boldsymbol{\pi},\mathbf{R})=\beta(U(\boldsymbol{\pi},\mathbf{E})-A(\boldsymbol{\pi},\mathbf{E},\beta)). |  |

That is, the excess growth rate is, up to a multiplicative constant, the difference between the reference average energy and the Helmholtz free energy.

The distribution 𝐩⋆\mathbf{p}^{\star} given by ([2.11](https://arxiv.org/html/2510.25740v1#S2.E11 "In 2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) can be justified by Gibb’s variational principle [[53](https://arxiv.org/html/2510.25740v1#bib.bib53), Proposition 4.7] of the free energy (or equivalently the log–exp–sum in ([1.8](https://arxiv.org/html/2510.25740v1#S1.E8 "In item (ii) ‣ Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate"))):

|  |  |  |  |
| --- | --- | --- | --- |
| (2.14) |  | A​(𝝅,𝐄,β)=inf𝐩∈Δn{⟨𝐩,𝐄⟩+1β​H​(𝐩∥𝝅)},A(\boldsymbol{\pi},\mathbf{E},\beta)=\inf\_{\mathbf{p}\in\Delta\_{n}}\left\{\langle\mathbf{p},\mathbf{E}\rangle+\frac{1}{\beta}H(\mathbf{p}\;\|\;\boldsymbol{\pi})\right\}, |  |

and the infimum is attained uniquely by 𝐩=𝐩⋆\mathbf{p}=\mathbf{p}^{\star}. From this and ([2.13](https://arxiv.org/html/2510.25740v1#S2.E13 "In 2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), we immediately obtain a variational representation of the excess growth rate which will be further explored in Section [4.3](https://arxiv.org/html/2510.25740v1#S4.SS3 "4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate").

###### Proposition 2.7 (Variational representation).

For 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n} and 𝐫∈ℝn\mathbf{r}\in\mathbb{R}^{n}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.15) |  | γ​(𝝅,𝐫)=sup𝐩∈Δn{⟨𝐩−𝝅,𝐫⟩−H​(𝐩∥𝝅)},\gamma(\boldsymbol{\pi},\mathbf{r})=\sup\_{\mathbf{p}\in\Delta\_{n}}\Bigl\{\langle\mathbf{p}-\boldsymbol{\pi},\mathbf{r}\rangle-H(\mathbf{p}\;\|\;\boldsymbol{\pi})\Bigr\}, |  |

Moreover, the unique maximizer of ([2.15](https://arxiv.org/html/2510.25740v1#S2.E15 "In Proposition 2.7 (Variational representation). ‣ 2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) is 𝐩⋆=𝛑⊕𝛑𝒞​[e𝐫]\mathbf{p}^{\star}=\boldsymbol{\pi}\oplus\_{\boldsymbol{\pi}}\mathcal{C}[e^{\mathbf{r}}].

###### Proof.

We omit the proof as this result is classical. We only note that the support of the optimal 𝐩\mathbf{p} must be contained in that of 𝝅\boldsymbol{\pi} as otherwise H​(𝐩∥𝝅)=∞H(\mathbf{p}\;\|\;\boldsymbol{\pi})=\infty. Also, the optimizer is unique since H(⋅∥𝝅)H(\cdot\;\|\;\boldsymbol{\pi}) is strictly convex on the set {𝐩∈Δn:supp⁡(𝐩)⊂supp⁡(𝝅)}\{\mathbf{p}\in\Delta\_{n}:\operatorname{supp}(\mathbf{p})\subset\operatorname{supp}(\boldsymbol{\pi})\}.
∎

### 2.3. Information-theoretic interpretation

We show that the excess growth rate can be expressed in terms of L. Campbell’s measure of average code length [[15](https://arxiv.org/html/2510.25740v1#bib.bib15)]. Mathematically, the relation is essentially the same as the one in ([2.13](https://arxiv.org/html/2510.25740v1#S2.E13 "In 2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")).

Fix n≥1n\geq 1. Let 𝝅=(π1,…,πn)∈Δn∘\boldsymbol{\pi}=(\pi\_{1},\ldots,\pi\_{n})\in\Delta\_{n}^{\circ} be a probability distribution and ℓ=(ℓ1,…,ℓn)∈ℤ>0n\boldsymbol{\ell}=(\ell\_{1},\ldots,\ell\_{n})\in\mathbb{Z}\_{>0}^{n} be a set of codeword lengths over an alphabet 𝒳\mathcal{X} of size D≥2D\geq 2.

###### Definition 2.8 (Campbell’s measure of expected code length).

Consider the distribution 𝛑\boldsymbol{\pi} and the vector ℓ\boldsymbol{\ell} of codeword lengths as described above. For ρ>0\rho>0, we define

|  |  |  |  |
| --- | --- | --- | --- |
| (2.16) |  | Lρ​(𝝅,ℓ):=1ρ​logD⁡(∑i=1nπi​Dρ​ℓi).L\_{\rho}(\boldsymbol{\pi},\boldsymbol{\ell}):=\frac{1}{\rho}\log\_{D}\left(\sum\_{i=1}^{n}\pi\_{i}D^{\rho\ell\_{i}}\right). |  |

The idea is to consider a cost which is exponential in the length of the codeword. Campbell’s measure is obtained by normalizing the expected value of Dρ​ℓD^{\rho\ell} by the logarithmic transformation 1ρ​logD⁡(⋅)\frac{1}{\rho}\log\_{D}(\cdot) (this is an exponential mean; see Remark [1.2](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem2 "Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")(ii))). This can be contrasted with Shannon’s expected code length

|  |  |  |
| --- | --- | --- |
|  | S​(𝝅,ℓ):=∑i=1nπi​ℓi,S(\boldsymbol{\pi},\boldsymbol{\ell}):=\sum\_{i=1}^{n}\pi\_{i}\ell\_{i}, |  |

which is recovered in the limit

|  |  |  |
| --- | --- | --- |
|  | limρ→0Lρ​(𝝅,ℓ)=S​(𝝅,ℓ).\lim\_{\rho\rightarrow 0}L\_{\rho}(\boldsymbol{\pi},\boldsymbol{\ell})=S(\boldsymbol{\pi},\boldsymbol{\ell}). |  |

At the other extreme, we have limρ→∞Lρ​(𝝅,ℓ)=max1≤i≤n⁡ℓi\lim\_{\rho\rightarrow\infty}L\_{\rho}(\boldsymbol{\pi},\boldsymbol{\ell})=\max\_{1\leq i\leq n}\ell\_{i}. In [[15](https://arxiv.org/html/2510.25740v1#bib.bib15)], Campbell established source coding theorems under which the asymptotic optimal value of Lρ​(𝝅,ℓ)L\_{\rho}(\boldsymbol{\pi},\boldsymbol{\ell})—for long sequences of input symbols—is the Rényi entropy. Also see [[6](https://arxiv.org/html/2510.25740v1#bib.bib6)] and the references therein for other extensions and applications of Campbell’s measure.

We observe that the difference Lρ​(𝝅,ℓ)−S​(𝝅,ℓ)L\_{\rho}(\boldsymbol{\pi},\boldsymbol{\ell})-S(\boldsymbol{\pi},\boldsymbol{\ell}) between Campbell’s and Shannon’s expected lengths is, up to a multiplicative constant, an excess growth rate.

###### Proposition 2.9 (Excess growth rate in Campbell’s measure).

Let n≥1n\geq 1, 𝛑∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ}, ℓ∈ℤ>0n\boldsymbol{\ell}\in\mathbb{Z}\_{>0}^{n} and ρ>0\rho>0. Define

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(R1,…,Rn),where ​Ri=Dρ​ℓi,\mathbf{R}=(R\_{1},\ldots,R\_{n}),\quad\text{where }R\_{i}=D^{\rho\ell\_{i}}, |  |

be the vector of exponentiated code lengths. Then, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.17) |  | Lρ​(𝝅,ℓ)−S​(𝝅,ℓ)=1ρ​log⁡D​Γ​(𝝅,𝐑)L\_{\rho}(\boldsymbol{\pi},\boldsymbol{\ell})-S(\boldsymbol{\pi},\boldsymbol{\ell})=\frac{1}{\rho\log D}\Gamma(\boldsymbol{\pi},\mathbf{R}) |  |

###### Proof.

We have

|  |  |  |
| --- | --- | --- |
|  | Lρ​(𝝅,ℓ)=1ρ​logD⁡(∑i=1nπi​Ri)=1ρ​log⁡D​log⁡(∑i=1nπi​Ri).L\_{\rho}(\boldsymbol{\pi},\boldsymbol{\ell})=\frac{1}{\rho}\log\_{D}\left(\sum\_{i=1}^{n}\pi\_{i}R\_{i}\right)=\frac{1}{\rho\log D}\log\left(\sum\_{i=1}^{n}\pi\_{i}R\_{i}\right). |  |

On the other hand, we have

|  |  |  |
| --- | --- | --- |
|  | S​(𝝅,ℓ)=∑i=1nπi​ℓi=1ρ​∑i=1nπi​logD⁡Ri=1ρ​log⁡D​∑i=1nπi​log⁡Ri.S(\boldsymbol{\pi},\boldsymbol{\ell})=\sum\_{i=1}^{n}\pi\_{i}\ell\_{i}=\frac{1}{\rho}\sum\_{i=1}^{n}\pi\_{i}\log\_{D}R\_{i}=\frac{1}{\rho\log D}\sum\_{i=1}^{n}\pi\_{i}\log R\_{i}. |  |

We obtain ([2.17](https://arxiv.org/html/2510.25740v1#S2.E17 "In Proposition 2.9 (Excess growth rate in Campbell’s measure). ‣ 2.3. Information-theoretic interpretation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) by taking the difference.
∎

### 2.4. Probabilistic interpretations

In this subsection, we prove two results that provide probabilistic interpretations of the excess growth rate in terms of the scaled Dirichlet distribution. We fix n≥2n\geq 2.

To motivate the first result, recall that the relative entropy arises in Sanov’s theorem in the theory of large deviations. Let 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ}. For N≥1N\geq 1, let

|  |  |  |
| --- | --- | --- |
|  | 𝐐N∼Multinomial​(N,𝐩)\mathbf{Q}\_{N}\sim\mathrm{Multinomial}(N,\mathbf{p}) |  |

be an nn-dimensional multinomial random vector. Let μ𝐩,N\mu\_{\mathbf{p},N} be the law of 1N​𝐐N\frac{1}{N}\mathbf{Q}\_{N}. In other words, μ𝐩,N\mu\_{\mathbf{p},N} represents the law of the empirical distribution of NN independent samples from the categorical distribution on the state space [n][n] with weights 𝐩\mathbf{p}. Then, it can shown that the family (μ𝐩,N)N≥1(\mu\_{\mathbf{p},N})\_{N\geq 1} satisfies the large deivation principle (LDP) with rate NN and rate function

|  |  |  |  |
| --- | --- | --- | --- |
| (2.18) |  | I​(𝐪)=H​(𝐪∥𝐩),𝐪∈ΔN∘.I(\mathbf{q})=H(\mathbf{q}\;\|\;\mathbf{p}),\quad\mathbf{q}\in\Delta\_{N}^{\circ}. |  |

In particular, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.19) |  | limN→∞1N​log⁡μ𝐩,N​(S)=−inf𝐪∈SH​(𝐪∥𝐩).\lim\_{N\rightarrow\infty}\frac{1}{N}\log\mu\_{\mathbf{p},N}(S)=-\inf\_{\mathbf{q}\in S}H(\mathbf{q}\;\|\;\mathbf{p}). |  |

for sufficiently regular Borel subsets SS of Δn∘\Delta\_{n}^{\circ}. In Theorem [2.15](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem15 "Theorem 2.15 (Excess growth rate as rate function). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")(ii) below, we recall the definition of LDP in the context of the excess growth rate. We refer the reader to [[20](https://arxiv.org/html/2510.25740v1#bib.bib20)] for a comprehensive treatment of large deviation theory, and [[17](https://arxiv.org/html/2510.25740v1#bib.bib17), Chapter 11] for an introduction with a focus on information-theoretic concepts.

Analogously, we show that the excess growth rate arises in the large deviation principle of another stochastic model involving the scaled Dirichlet distribution [[44](https://arxiv.org/html/2510.25740v1#bib.bib44), [45](https://arxiv.org/html/2510.25740v1#bib.bib45)]. This extends the formulation in [[51](https://arxiv.org/html/2510.25740v1#bib.bib51), Section 3.1] and [[66](https://arxiv.org/html/2510.25740v1#bib.bib66), Example III.18] which is restricted to the case 𝝅=𝐞¯=(1n,…,1n)\boldsymbol{\pi}=\bar{\mathbf{e}}=(\frac{1}{n},\ldots,\frac{1}{n}). For α,β∈(0,∞)\alpha,\beta\in(0,\infty), we let Gamma​(α,β)\mathrm{Gamma}(\alpha,\beta) be the gamma distribution on ℝ+\mathbb{R}\_{+} with shape parameter α\alpha and rate parameter β\beta.

###### Definition 2.10 (Scaled Dirichlet distribution).

The scaled Dirichlet distribution 𝒮​𝒟​(𝛂,𝛃)\mathcal{SD}(\boldsymbol{\alpha},\boldsymbol{\beta}), with parameters 𝛂=(α1,…,αn)\boldsymbol{\alpha}=(\alpha\_{1},\ldots,\alpha\_{n}) and 𝛃=(β1,…,βn)\boldsymbol{\beta}=(\beta\_{1},\ldots,\beta\_{n}) in (0,∞)n(0,\infty)^{n}, is the distribution of the Δn∘\Delta\_{n}^{\circ}-valued random vector

|  |  |  |  |
| --- | --- | --- | --- |
| (2.20) |  | 𝐘=𝒞​[𝐗],𝐗=(X1,…,Xn),\mathbf{Y}=\mathcal{C}[\mathbf{X}],\quad\mathbf{X}=(X\_{1},\ldots,X\_{n}), |  |

where X1,…,XnX\_{1},\ldots,X\_{n} are jointly independent with Xi∼Gamma​(αi,βi)X\_{i}\sim\mathrm{Gamma}(\alpha\_{i},\beta\_{i}).

When 𝜷=(β,…,β)\boldsymbol{\beta}=(\beta,\ldots,\beta) is a constant vector, then 𝒮​𝒟​(𝜶,𝜷)\mathcal{SD}(\boldsymbol{\alpha},\boldsymbol{\beta}) reduces to the Dirichlet distribution 𝒟​(𝜶)\mathcal{D}(\boldsymbol{\alpha}) with parameter 𝜶\boldsymbol{\alpha}. The scaled Dirichlet distribution can be traced to the works of Savage and Dickey [[21](https://arxiv.org/html/2510.25740v1#bib.bib21)] in the 1960s. It was studied in [[44](https://arxiv.org/html/2510.25740v1#bib.bib44), [45](https://arxiv.org/html/2510.25740v1#bib.bib45)] as a more flexible version of the Dirichlet distribution to model simplex-valued (or compositional) data.

The following lemma shows that the scaled Dirichlet distribution can be expressed in terms of the usual Dirichlet distribution and the simplicial operations introduced in Section [2.1](https://arxiv.org/html/2510.25740v1#S2.SS1 "2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate").

###### Lemma 2.11.

Let 𝛂,𝛃∈(0,∞)n\boldsymbol{\alpha},\boldsymbol{\beta}\in(0,\infty)^{n}. Then 𝒮​𝒟​(𝛂,𝛃)\mathcal{SD}(\boldsymbol{\alpha},\boldsymbol{\beta}) is equal to the distribution of

|  |  |  |  |
| --- | --- | --- | --- |
| (2.21) |  | 𝐘=𝒞​[𝜷−1]⊕𝐙,\mathbf{Y}=\mathcal{C}[\boldsymbol{\beta}^{-1}]\oplus\mathbf{Z}, |  |

where 𝐙∼𝒟​(𝛂)\mathbf{Z}\sim\mathcal{D}(\boldsymbol{\alpha}). In particular, we have 𝒮​𝒟​(𝛂,𝛃)=𝒮​𝒟​(𝛂,c​𝛃)\mathcal{SD}(\boldsymbol{\alpha},\boldsymbol{\beta})=\mathcal{SD}(\boldsymbol{\alpha},c\boldsymbol{\beta}) for any c>0c>0.

###### Proof.

Suppose 𝐘∼𝒮​𝒟​(𝜶,𝜷)\mathbf{Y}\sim\mathcal{SD}(\boldsymbol{\alpha},\boldsymbol{\beta}) is expressed as ([2.20](https://arxiv.org/html/2510.25740v1#S2.E20 "In Definition 2.10 (Scaled Dirichlet distribution). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")). Recall that if X~∼Gamma​(a,b)\tilde{X}\sim\mathrm{Gamma}(a,b), then c​X~∼Gamma​(a,bc)c\tilde{X}\sim\mathrm{Gamma}(a,\frac{b}{c}). So Z~i:=βi​Xi∼Gamma​(αi,1)\tilde{Z}\_{i}:=\beta\_{i}X\_{i}\sim\mathrm{Gamma}(\alpha\_{i},1), and 𝐙:=𝒞​[𝐙~]∼𝒟​(𝜶)\mathbf{Z}:=\mathcal{C}[\tilde{\mathbf{Z}}]\sim\mathcal{D}(\boldsymbol{\alpha}). It follows that

|  |  |  |
| --- | --- | --- |
|  | 𝐘=𝒞​[𝐗]=𝒞​[𝜷−1⊙𝐙~]=𝒞​[𝜷−1]⊕𝐙.\mathbf{Y}=\mathcal{C}[\mathbf{X}]=\mathcal{C}[\boldsymbol{\beta}^{-1}\odot\tilde{\mathbf{Z}}]=\mathcal{C}[\boldsymbol{\beta}^{-1}]\oplus\mathbf{Z}. |  |

∎

We proceed to write down the density of 𝒮​𝒟​(𝜶,𝜷)\mathcal{SD}(\boldsymbol{\alpha},\boldsymbol{\beta}). On Δn∘\Delta\_{n}^{\circ}, we take as reference measure the Aitchison measure λn\lambda\_{n} defined by

|  |  |  |
| --- | --- | --- |
|  | d​λn​(𝐲):=1n​∏i=1nyi​d​y1​⋯​d​yn−1,𝐲∈Δn∘.\mathrm{d}\lambda\_{n}(\mathbf{y}):=\frac{1}{\sqrt{n}\prod\_{i=1}^{n}y\_{i}}\mathrm{d}y\_{1}\cdots\mathrm{d}y\_{n-1},\quad\mathbf{y}\in\Delta\_{n}^{\circ}. |  |

More precisely, in the above equation we regard the Lebesgue measure d​y1​⋯​d​yn−1\mathrm{d}y\_{1}\cdots\mathrm{d}y\_{n-1} on

|  |  |  |
| --- | --- | --- |
|  | {(y1,…,yn−1)∈(0,1)n−1:y1+⋯+yn−1<1}\{(y\_{1},\ldots,y\_{n-1})\in(0,1)^{n-1}:y\_{1}+\cdots+y\_{n-1}<1\} |  |

as a measure on Δn∘\Delta\_{n}^{\circ} through the measurable bijection

|  |  |  |
| --- | --- | --- |
|  | (y1,…,yn−1)↔(y1,…,yn−1,1−∑i=1n−1yi).(y\_{1},\ldots,y\_{n-1})\leftrightarrow\left(y\_{1},\ldots,y\_{n-1},1-\sum\_{i=1}^{n-1}y\_{i}\right). |  |

By [[44](https://arxiv.org/html/2510.25740v1#bib.bib44), (11)], the density of 𝒮​𝒟​(𝜶,𝜷)\mathcal{SD}(\boldsymbol{\alpha},\boldsymbol{\beta}) with respect to the Aitchison measure λn\lambda\_{n} is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.22) |  | Γ​(∑i=1nαi)​n∏i=1nΓ​(αi)​∏i=1n(βi​yi)αi(∑i=1nβi​yi)∑i=1nαi,𝐲∈Δn∘,\frac{\Gamma\left(\sum\_{i=1}^{n}\alpha\_{i}\right)\sqrt{n}}{\prod\_{i=1}^{n}\Gamma(\alpha\_{i})}\frac{\prod\_{i=1}^{n}(\beta\_{i}y\_{i})^{\alpha\_{i}}}{\left(\sum\_{i=1}^{n}\beta\_{i}y\_{i}\right)^{\sum\_{i=1}^{n}\alpha\_{i}}},\quad\mathbf{y}\in\Delta\_{n}^{\circ}, |  |

where Γ​(⋅)\Gamma(\cdot) is the gamma function (not to be confused with the excess growth rate).

###### Remark 2.12.

The Aitchison measure is the Haar measure on (Δn∘,⊕)(\Delta\_{n}^{\circ},\oplus) (as a topological commutative group) which is unique up to a multiplicative constant.

To formulate an LDP involving the excess growth rate, we parameterize 𝜶\boldsymbol{\alpha} and 𝜷\boldsymbol{\beta} as follows. Let 𝝅∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ} and let σ>0\sigma>0 be a noise parameter whose role is analogous to that of 1N\frac{1}{N} in ([2.19](https://arxiv.org/html/2510.25740v1#S2.E19 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")). For 𝐱∈(0,∞)n\mathbf{x}\in(0,\infty)^{n}, we define

|  |  |  |  |
| --- | --- | --- | --- |
| (2.23) |  | μ𝝅,𝐱,σ:=𝒮​𝒟​(𝜶=1σ​𝝅,𝜷=𝝅⊙𝐱−1).\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma}:=\mathcal{SD}\left(\boldsymbol{\alpha}=\frac{1}{\sigma}\boldsymbol{\pi},\boldsymbol{\beta}=\boldsymbol{\pi}\odot\mathbf{x}^{-1}\right). |  |

By Lemma [2.11](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), μ𝝅,𝐱,σ\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma} is the distribution of the random vector

|  |  |  |  |
| --- | --- | --- | --- |
| (2.24) |  | 𝐘=(𝒞​[𝐱]⊖𝝅)⊕𝐙,𝐙∼𝒟​(1σ​𝝅).\mathbf{Y}=(\mathcal{C}[\mathbf{x}]\ominus\boldsymbol{\pi})\oplus\mathbf{Z},\quad\mathbf{Z}\sim\mathcal{D}\left(\frac{1}{\sigma}\boldsymbol{\pi}\right). |  |

Since 𝐘\mathbf{Y} depends on 𝐱\mathbf{x} only via 𝒞​[𝐱]\mathcal{C}[\mathbf{x}], we may assume without loss of generality that 𝐱∈Δn∘\mathbf{x}\in\Delta\_{n}^{\circ}. We obtain the density of μ𝝅,𝐱,σ\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma} by plugging ([2.23](https://arxiv.org/html/2510.25740v1#S2.E23 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) into ([2.22](https://arxiv.org/html/2510.25740v1#S2.E22 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")).

###### Lemma 2.13 (Density of μ𝝅,𝐱,σ\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma}).

For 𝛑,𝐱∈Δn∘\boldsymbol{\pi},\mathbf{x}\in\Delta\_{n}^{\circ} and σ>0\sigma>0, the density of μ𝛑,𝐱,σ\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma} with respect to λn\lambda\_{n} is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.25) |  | f​(𝐲∣𝝅,𝐱,σ):=Γ​(1σ)​n∏i=1nΓ​(πiσ)​e−1σ​H​(𝝅)​e−1σ​Γ𝝅​(𝐲∥𝐱),𝐲∈Δn∘,f(\mathbf{y}\mid\boldsymbol{\pi},\mathbf{x},\sigma):=\frac{\Gamma(\frac{1}{\sigma})\sqrt{n}}{\prod\_{i=1}^{n}\Gamma(\frac{\pi\_{i}}{\sigma})}e^{\frac{-1}{\sigma}H(\boldsymbol{\pi})}e^{\frac{-1}{\sigma}\Gamma\_{\boldsymbol{\pi}}(\mathbf{y}\;\|\;\mathbf{x})},\quad\mathbf{y}\in\Delta\_{n}^{\circ}, |  |

where H​(𝛑)=−∑i=1nπi​log⁡πiH(\boldsymbol{\pi})=-\sum\_{i=1}^{n}\pi\_{i}\log\pi\_{i} is the Shannon entropy of 𝛑\boldsymbol{\pi}.

###### Remark 2.14 (The case of equal weights).

If 𝛑=𝐞¯\boldsymbol{\pi}=\bar{\mathbf{e}} is the barycenter (zero element) of Δn∘\Delta\_{n}^{\circ}, then in ([2.24](https://arxiv.org/html/2510.25740v1#S2.E24 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) (with 𝐱∈Δn∘\mathbf{x}\in\Delta\_{n}^{\circ}) we have 𝐱⊖𝛑=𝐱\mathbf{x}\ominus\boldsymbol{\pi}=\mathbf{x} and 𝐘=𝐱⊕𝐙\mathbf{Y}=\mathbf{x}\oplus\mathbf{Z}, where 𝐙∼𝒟​(σn,…,σn)\mathbf{Z}\sim\mathcal{D}(\frac{\sigma}{n},\ldots,\frac{\sigma}{n}). This recovers to the Dirichlet perturbation model studied in [[51](https://arxiv.org/html/2510.25740v1#bib.bib51), [60](https://arxiv.org/html/2510.25740v1#bib.bib60), [66](https://arxiv.org/html/2510.25740v1#bib.bib66)].

###### Theorem 2.15 (Excess growth rate as rate function).

Let n≥2n\geq 2 and 𝛑∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ}.

* (i)

  We have

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.26) |  | limσ↓0sup𝐱,𝐲∈Δn∘|−σlogf(𝐲∣𝝅,𝐱,σ)−Γ𝝅(𝐲∥𝐱)|=0.\lim\_{\sigma\downarrow 0}\sup\_{\mathbf{x},\mathbf{y}\in\Delta\_{n}^{\circ}}\left|-\sigma\log f(\mathbf{y}\mid\boldsymbol{\pi},\mathbf{x},\sigma)-\Gamma\_{\boldsymbol{\pi}}(\mathbf{y}\;\|\;\mathbf{x})\right|=0. |  |
* (ii)

  For 𝐱∈Δn∘\mathbf{x}\in\Delta\_{n}^{\circ}, the family (μ𝝅,𝐱,σ)σ>0\left(\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma}\right)\_{\sigma>0} of probability distributions on Δn∘\Delta\_{n}^{\circ} satisfy the large deviation principle with rate 1σ\frac{1}{\sigma} and rate function I​(𝐲)=Γ𝝅​(𝐲∥𝐱)I(\mathbf{y})=\Gamma\_{\boldsymbol{\pi}}(\mathbf{y}\;\|\;\mathbf{x}). By definition, this means that for every closed subset FF and every open subset GG of Δn∘\Delta\_{n}^{\circ}, we have

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.27) |  | lim supσ↓0σ​log⁡μ𝝅,𝐱,σ​(F)≤−inf𝐲∈FΓ𝝅​(𝐲∥𝐱),lim infσ↓0σ​log⁡μ𝝅,𝐱,σ​(G)≥−inf𝐲∈GΓ𝝅​(𝐲∥𝐱).\begin{split}\limsup\_{\sigma\downarrow 0}\sigma\log\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma}(F)&\leq-\inf\_{\mathbf{y}\in F}\Gamma\_{\boldsymbol{\pi}}(\mathbf{y}\;\|\;\mathbf{x}),\\ \liminf\_{\sigma\downarrow 0}\sigma\log\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma}(G)&\geq-\inf\_{\mathbf{y}\in G}\Gamma\_{\boldsymbol{\pi}}(\mathbf{y}\;\|\;\mathbf{x}).\end{split} |  |

###### Proof.

(i) From ([2.25](https://arxiv.org/html/2510.25740v1#S2.E25 "In Lemma 2.13 (Density of 𝜇_{𝝅,𝐱,𝜎}). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.28) |  | −σ​log⁡f​(𝐲∣𝝅,𝐱,σ)−Γ𝝅​(𝐲∣𝐱)=−σ​log⁡Γ​(1σ)−σ​log⁡n+σ​∑i=1nlog⁡Γ​(πiσ)−H​(𝝅),\begin{split}&-\sigma\log f(\mathbf{y}\mid\boldsymbol{\pi},\mathbf{x},\sigma)-\Gamma\_{\boldsymbol{\pi}}(\mathbf{y}\mid\mathbf{x})\\ &=-\sigma\log\Gamma\left(\frac{1}{\sigma}\right)-\sigma\log\sqrt{n}+\sigma\sum\_{i=1}^{n}\log\Gamma\left(\frac{\pi\_{i}}{\sigma}\right)-H(\boldsymbol{\pi}),\end{split} |  |

which is independent of 𝐱\mathbf{x} and 𝐲\mathbf{y} (this gives the sup\sup in ([2.26](https://arxiv.org/html/2510.25740v1#S2.E26 "In item (i) ‣ Theorem 2.15 (Excess growth rate as rate function). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"))).

By Stirling’s approximation

|  |  |  |
| --- | --- | --- |
|  | log⁡Γ​(z)=z​log⁡z−z+O​(log⁡z),as ​z→∞,\log\Gamma(z)=z\log z-z+O(\log z),\quad\text{as }z\rightarrow\infty, |  |

the last expression in ([2.28](https://arxiv.org/html/2510.25740v1#S2.E28 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) is equal to

|  |  |  |
| --- | --- | --- |
|  | −log⁡1σ−1−σ​log⁡n+∑i=1n(πi​log⁡πiσ+πi)−H​(𝝅)+o​(1)=H​(𝝅)−H​(𝝅)+σ​log⁡n+o​(1)=o​(1)→0,as ​σ↓0.\begin{split}&-\log\frac{1}{\sigma}-1-\sigma\log\sqrt{n}+\sum\_{i=1}^{n}\left(\pi\_{i}\log\frac{\pi\_{i}}{\sigma}+\pi\_{i}\right)-H(\boldsymbol{\pi})+o(1)\\ &=H(\boldsymbol{\pi})-H(\boldsymbol{\pi})+\sigma\log\sqrt{n}+o(1)=o(1)\rightarrow 0,\quad\text{as }\sigma\downarrow 0.\end{split} |  |

This gives the desired result ([2.26](https://arxiv.org/html/2510.25740v1#S2.E26 "In item (i) ‣ Theorem 2.15 (Excess growth rate as rate function). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")). In particular, from the computation above we have the limit

|  |  |  |
| --- | --- | --- |
|  | limσ↓0σ​log⁡(Γ​(1σ)∏i=1nΓ​(πiσ))=H​(𝝅).\lim\_{\sigma\downarrow 0}\sigma\log\left(\frac{\Gamma\left(\frac{1}{\sigma}\right)}{\prod\_{i=1}^{n}\Gamma\left(\frac{\pi\_{i}}{\sigma}\right)}\right)=H(\boldsymbol{\pi}). |  |

(ii) This is an immediate consequence of the uniform limit in (i). Since the argument is standard in the theory of large deviation and is not needed in the rest of the paper, we omit the details.
∎

Our second result expresses the excess growth rate as a Rényi divergence between members of the family (μ𝝅,𝐱,σ)𝐱∈Δn∘(\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma})\_{\mathbf{x}\in\Delta\_{n}^{\circ}}. (Here 𝝅∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ} and σ>0\sigma>0 are fixed and we may regard 𝐱\mathbf{x} as a location parameter.) To give a classical analogue, consider the squared Mahalanobis distance [[42](https://arxiv.org/html/2510.25740v1#bib.bib42)] on ℝn\mathbb{R}^{n} defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.29) |  | dM2​(𝐱,𝐲):=(𝐱−𝐲)⊤​Σ−1​(𝐱−𝐲),d\_{\mathrm{M}}^{2}(\mathbf{x},\mathbf{y}):=(\mathbf{x}-\mathbf{y})^{\top}\Sigma^{-1}(\mathbf{x}-\mathbf{y}), |  |

where 𝐱,𝐲∈ℝd\mathbf{x},\mathbf{y}\in\mathbb{R}^{d} are considered column vectors and Σ∈ℝn×n\Sigma\in\mathbb{R}^{n\times n} is a given strictly positive definite matrix. It is well known that dM2d\_{\mathrm{M}}^{2} expresses, up to a constant, the relative entropy between members of the normal location family {𝒩​(𝐱,Σ)}𝐱∈ℝn\{\mathcal{N}(\mathbf{x},\Sigma)\}\_{\mathbf{x}\in\mathbb{R}^{n}} (note that the covariance matrix Σ\Sigma is kept fixed):

|  |  |  |  |
| --- | --- | --- | --- |
| (2.30) |  | H​(𝒩​(𝐱,Σ)∥𝒩​(𝐲,Σ))=12​dM2​(𝐱,𝐲),𝐱,𝐲∈ℝd.H(\mathcal{N}(\mathbf{x},\Sigma)\;\|\;\mathcal{N}(\mathbf{y},\Sigma))=\frac{1}{2}d\_{\mathrm{M}}^{2}(\mathbf{x},\mathbf{y}),\quad\mathbf{x},\mathbf{y}\in\mathbb{R}^{d}. |  |

A characterization of the Mahalanobis distance is given in Theorem [3.15](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem15 "Theorem 3.15 (Characterization of squared Mahalanobis distance as a Bregman divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") below.

###### Remark 2.16.

The identity ([2.30](https://arxiv.org/html/2510.25740v1#S2.E30 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) is a special case of the general result that the relative entropy between members of an exponential family of probability distributions can be expressed as a Bregman divergence [[4](https://arxiv.org/html/2510.25740v1#bib.bib4)].

For α>0\alpha>0, the Rényi divergence of order α\alpha is defined for probability measures μ1,μ2\mu\_{1},\mu\_{2} on a (measurable) state space 𝒳\mathcal{X} by

|  |  |  |
| --- | --- | --- |
|  | Hα​(μ1∥μ2):=1α−1​log⁡(∫𝒳(d​μ1d​μ2)α​dμ2),H\_{\alpha}(\mu\_{1}\;\|\;\mu\_{2}):=\frac{1}{\alpha-1}\log\left(\int\_{\mathcal{X}}\left(\frac{\mathrm{d}\mu\_{1}}{\mathrm{d}\mu\_{2}}\right)^{\alpha}\mathrm{d}\mu\_{2}\right), |  |

when μ1\mu\_{1} is absolutely continuous with respect to μ2\mu\_{2}, and is +∞+\infty otherwise. If d​μ1=f1​d​ν\mathrm{d}\mu\_{1}=f\_{1}\mathrm{d}\nu and d​μ2=f2​d​ν\mathrm{d}\mu\_{2}=f\_{2}\mathrm{d}\nu where ν\nu is a common dominating measure, then the Rényi divergence can be expressed via the densities f1,f2f\_{1},f\_{2} by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.31) |  | Hα​(μ1∥μ2)=1α−1​log⁡(∫𝒳f1α​f21−α​dν).H\_{\alpha}(\mu\_{1}\;\|\;\mu\_{2})=\frac{1}{\alpha-1}\log\left(\int\_{\mathcal{X}}f\_{1}^{\alpha}f\_{2}^{1-\alpha}\mathrm{d}\nu\right). |  |

See [[61](https://arxiv.org/html/2510.25740v1#bib.bib61)] for a summary of the properties of the Rényi divergence.

###### Theorem 2.17 (Excess growth rate as Rényi divergence).

For n≥2n\geq 2, 𝛑∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ}, σ>0\sigma>0 and 𝐱,𝐲∈Δn∘\mathbf{x},\mathbf{y}\in\Delta\_{n}^{\circ}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.32) |  | H1+σ​(μ𝝅,𝐲,σ∥μ𝝅,𝐱,σ)=1σ​Γ𝝅​(𝐲∥𝐱).H\_{1+\sigma}(\mu\_{\boldsymbol{\pi},\mathbf{y},\sigma}\;\|\;\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma})=\frac{1}{\sigma}\Gamma\_{\boldsymbol{\pi}}(\mathbf{y}\;\|\;\mathbf{x}). |  |

###### Proof.

Fix 𝝅∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ} and σ>0\sigma>0. By Lemma [2.13](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem13 "Lemma 2.13 (Density of 𝜇_{𝝅,𝐱,𝜎}). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), we have

|  |  |  |
| --- | --- | --- |
|  | f​(𝐳∣𝝅,𝐱,σ)=C​e−1σ​Γ​(𝐳∥𝐱),f(\mathbf{z}\mid\boldsymbol{\pi},\mathbf{x},\sigma)=Ce^{\frac{-1}{\sigma}\Gamma(\mathbf{z}\;\|\;\mathbf{x})}, |  |

where Γ​(𝐳∥𝐱):=Γ𝝅​(𝐳∥𝐱)\Gamma(\mathbf{z}\;\|\;\mathbf{x}):=\Gamma\_{\boldsymbol{\pi}}(\mathbf{z}\;\|\;\mathbf{x}) and

|  |  |  |
| --- | --- | --- |
|  | C=C𝝅,σ:=Γ​(1σ)​n∏i=1nΓ​(πiσ)​e−1σ​H​(𝝅).C=C\_{\boldsymbol{\pi},\sigma}:=\frac{\Gamma(\frac{1}{\sigma})\sqrt{n}}{\prod\_{i=1}^{n}\Gamma(\frac{\pi\_{i}}{\sigma})}e^{\frac{-1}{\sigma}H(\boldsymbol{\pi})}. |  |

Let 𝐱,𝐲∈Δn∘\mathbf{x},\mathbf{y}\in\Delta\_{n}^{\circ} be given, and consider

|  |  |  |
| --- | --- | --- |
|  | σ​H1+σ​(μ𝝅,𝐲,σ∥μ𝝅,𝐱,σ)=σ​1(1+σ)−1​log⁡(∫Δn∘f​(𝐳∣𝝅,𝐲,σ)1+σ​f​(𝐳∣𝝅,𝐱,σ)−σ​dλn​(𝐳))=log⁡(C​∫Δn∘e−1+σσ​Γ​(𝐳∥𝐲)+Γ​(𝐳∥𝐱)​dλn​(𝐳)).\begin{split}&\sigma H\_{1+\sigma}(\mu\_{\boldsymbol{\pi},\mathbf{y},\sigma}\;\|\;\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma})\\ &=\sigma\frac{1}{(1+\sigma)-1}\log\left(\int\_{\Delta\_{n}^{\circ}}f(\mathbf{z}\mid\boldsymbol{\pi},\mathbf{y},\sigma)^{1+\sigma}f(\mathbf{z}\mid\boldsymbol{\pi},\mathbf{x},\sigma)^{-\sigma}\mathrm{d}\lambda\_{n}(\mathbf{z})\right)\\ &=\log\left(C\int\_{\Delta\_{n}^{\circ}}e^{-\frac{1+\sigma}{\sigma}\Gamma(\mathbf{z}\;\|\;\mathbf{y})+\Gamma(\mathbf{z}\;\|\;\mathbf{x})}\mathrm{d}\lambda\_{n}(\mathbf{z})\right).\end{split} |  |

To evaluate the integral, consider the identity

|  |  |  |  |
| --- | --- | --- | --- |
| (2.33) |  | ∫Δn∘C​e−1σ​Γ​(𝐳∥𝐲)​dλn​(𝐳)≡1,𝐱∈Δn∘.\int\_{\Delta\_{n}^{\circ}}Ce^{\frac{-1}{\sigma}\Gamma(\mathbf{z}\;\|\;\mathbf{y})}\mathrm{d}\lambda\_{n}(\mathbf{z})\equiv 1,\quad\mathbf{x}\in\Delta\_{n}^{\circ}. |  |

In fact, by numéraire invariance (Proposition [2.3](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem3 "Proposition 2.3 (Numéraire invariance). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), the identity holds for 𝐲∈(0,∞)n\mathbf{y}\in(0,\infty)^{n}. Let ∇𝐯\nabla\_{\mathbf{v}} be the directional derivative, with respect to 𝐲\mathbf{y}, in the direction

|  |  |  |
| --- | --- | --- |
|  | 𝐯=(yi2xi)1≤i≤n∈ℝn.\mathbf{v}=\left(\frac{y\_{i}^{2}}{x\_{i}}\right)\_{1\leq i\leq n}\in\mathbb{R}^{n}. |  |

Differentiating under the integral sign in ([2.33](https://arxiv.org/html/2510.25740v1#S2.E33 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")),999This can be justified using Remark [2.12](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem12 "Remark 2.12. ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") and standard estimates. we have

|  |  |  |
| --- | --- | --- |
|  | C​∫Δn∘e−1σ​Γ​(𝐳∥𝐲)​∇𝐯Γ​(𝐳∥𝐲)​dλn​(𝐳)=1.C\int\_{\Delta\_{n}^{\circ}}e^{\frac{-1}{\sigma}\Gamma(\mathbf{z}\;\|\;\mathbf{y})}\nabla\_{\mathbf{v}}\Gamma(\mathbf{z}\;\|\;\mathbf{y})\mathrm{d}\lambda\_{n}(\mathbf{z})=1. |  |

Noting that

|  |  |  |
| --- | --- | --- |
|  | ∇𝐯Γ​(𝐳∥𝐲)=∑i−πi​ziyi2∑jπj​zjyj​yi2xi+∑iπiyi​yi2xi=−∑iπi​zixi∑iπi​ziyi+∑iπi​yixi,\nabla\_{\mathbf{v}}\Gamma(\mathbf{z}\;\|\;\mathbf{y})=\sum\_{i}\frac{-\pi\_{i}\frac{z\_{i}}{y\_{i}^{2}}}{\sum\_{j}\pi\_{j}\frac{z\_{j}}{y\_{j}}}\frac{y\_{i}^{2}}{x\_{i}}+\sum\_{i}\frac{\pi\_{i}}{y\_{i}}\frac{y\_{i}^{2}}{x\_{i}}=-\frac{\sum\_{i}\pi\_{i}\frac{z\_{i}}{x\_{i}}}{\sum\_{i}\pi\_{i}\frac{z\_{i}}{y\_{i}}}+\sum\_{i}\pi\_{i}\frac{y\_{i}}{x\_{i}}, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | ∑iπi​yixi=C​∫Δn∘e−1σ​Γ​(𝐳∥𝐲)​∑iπi​zixi∑iπi​zjyj​dλn​(𝐳).\sum\_{i}\pi\_{i}\frac{y\_{i}}{x\_{i}}=C\int\_{\Delta\_{n}^{\circ}}e^{\frac{-1}{\sigma}\Gamma(\mathbf{z}\;\|\;\mathbf{y})}\frac{\sum\_{i}\pi\_{i}\frac{z\_{i}}{x\_{i}}}{\sum\_{i}\pi\_{i}\frac{z\_{j}}{y\_{j}}}\mathrm{d}\lambda\_{n}(\mathbf{z}). |  |

Observe that we may rearrange the above as

|  |  |  |
| --- | --- | --- |
|  | eΓ​(𝐲∥𝐱)+∑iπi​log⁡yixi=C​∫Δn∘e−1σ​Γ​(𝐳∥𝐲)​eΓ​(𝐳∥𝐱)+∑iπi​log⁡zixieΓ​(𝐳∥𝐲)+∑iπi​log⁡ziyi​dλn​(𝐳)⇒eΓ​(𝐲∥𝐱)=C​∫Δn∘e−1+σσ​Γ​(𝐳∥𝐲)​eΓ​(𝐳∥𝐱)​dλn​(𝐳).\begin{split}&e^{\Gamma(\mathbf{y}\;\|\;\mathbf{x})+\sum\_{i}\pi\_{i}\log\frac{y\_{i}}{x\_{i}}}=C\int\_{\Delta\_{n}^{\circ}}\frac{e^{\frac{-1}{\sigma}\Gamma(\mathbf{z}\;\|\;\mathbf{y})}e^{\Gamma(\mathbf{z}\;\|\;\mathbf{x})+\sum\_{i}\pi\_{i}\log\frac{z\_{i}}{x\_{i}}}}{e^{\Gamma(\mathbf{z}\;\|\;\mathbf{y})+\sum\_{i}\pi\_{i}\log\frac{z\_{i}}{y\_{i}}}}\mathrm{d}\lambda\_{n}(\mathbf{z})\\ &\Rightarrow e^{\Gamma(\mathbf{y}\;\|\;\mathbf{x})}=C\int\_{\Delta\_{n}^{\circ}}e^{-\frac{1+\sigma}{\sigma}\Gamma(\mathbf{z}\;\|\;\mathbf{y})}e^{\Gamma(\mathbf{z}\;\|\;\mathbf{x})}\mathrm{d}\lambda\_{n}(\mathbf{z}).\end{split} |  |

We obtain ([2.32](https://arxiv.org/html/2510.25740v1#S2.E32 "In Theorem 2.17 (Excess growth rate as Rényi divergence). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) by taking logarithm on both sides.
∎

###### Remark 2.18.

The identity ([2.32](https://arxiv.org/html/2510.25740v1#S2.E32 "In Theorem 2.17 (Excess growth rate as Rényi divergence). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")) can also be derived by showing that the family {μ𝛑,𝐱,σ}𝐱∈Δn∘\{\mu\_{\boldsymbol{\pi},\mathbf{x},\sigma}\}\_{\mathbf{x}\in\Delta\_{n}^{\circ}} can be reparameterized as a *λ\lambda-exponential family* in the sense of [[66](https://arxiv.org/html/2510.25740v1#bib.bib66), Definition III.1], and using the fact that the logarithmic divergence of a suitable potential function is the Rényi divergence [[66](https://arxiv.org/html/2510.25740v1#bib.bib66), Theorem III.14]. This result extends the relation in Remark [2.16](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem16 "Remark 2.16. ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") beyond the standard exponential family. In fact, the direct proof given above, which is shorter but may appear to be tricky, is motivated by this general theory. See, in particular, the proof of [[63](https://arxiv.org/html/2510.25740v1#bib.bib63), Theorem 13] and [[66](https://arxiv.org/html/2510.25740v1#bib.bib66), Example III.18].

## 3. Characterization theorems

In this section, we prove three characterization theorems for the excess growth rate that highlight different aspects of this quantity.

### 3.1. Via relative entropy

Our first characterization theorem shows that the properties of the excess growth rate discussed in Section [2.1](https://arxiv.org/html/2510.25740v1#S2.SS1 "2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), together with Lebesgue measurability, uniquely characterize it (as a family (Γ:𝒟n→ℝ+)n≥1(\Gamma:\mathcal{D}\_{n}\rightarrow\mathbb{R}\_{+})\_{n\geq 1}) up to a proportional constant. Our proof makes use of an algebraic relation between the excess growth rate and the relative entropy (Lemma [3.4](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem4 "Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), as well as an axiomatic characterization of the latter.

For easy reference, we gather here the relevant properties.

###### Assumption 3.1.

Consider a family of functions (G:𝒟n→ℝ)n≥1(G:\mathcal{D}\_{n}\rightarrow\mathbb{R})\_{n\geq 1}.

1. (A1)

   G​(𝝅,𝐑)G(\boldsymbol{\pi},\mathbf{R}) is (jointly) Lebesgue measurable.
2. (A2)

   G​(𝝅​σ,𝐑​σ)=G​(𝝅,𝐑)G(\boldsymbol{\pi}\sigma,\mathbf{R}\sigma)=G(\boldsymbol{\pi},\mathbf{R}) for every permutation σ\sigma.
3. (A3)

   G​(𝝅,𝐑)=G​(𝐩,𝐑′)G(\boldsymbol{\pi},\mathbf{R})=G(\mathbf{p},\mathbf{R}^{\prime}) if Ri=Ri′R\_{i}=R\_{i}^{\prime} for i∈supp⁡(𝝅)i\in\operatorname{supp}(\boldsymbol{\pi}).
4. (A4)

   G​(𝝅,𝐑)=0G(\boldsymbol{\pi},\mathbf{R})=0 if 𝐑\mathbf{R} is constant on supp⁡(𝝅)\operatorname{supp}(\boldsymbol{\pi}).
5. (A5)

   For (𝝅,𝐚)∈𝒟n(\boldsymbol{\pi},\mathbf{a})\in\mathcal{D}\_{n}, ki≥1k\_{i}\geq 1, (𝐩i,𝐑i)∈𝒟ki(\mathbf{p}^{i},\mathbf{R}^{i})\in\mathcal{D}\_{k\_{i}}, 𝐩=(𝐩1,…,𝐩n)\mathbf{p}=(\mathbf{p}^{1},\dots,\mathbf{p}^{n}) and 𝐑=(𝐑1,…,𝐑n)\mathbf{R}=(\mathbf{R}^{1},\dots,\mathbf{R}^{n}), the following *chain rule* holds:

   |  |  |  |
   | --- | --- | --- |
   |  | G​(𝝅∘𝐩,𝐚∘𝐑)=G​(𝝅,𝐚​⟨⟨𝐩,𝐑⟩⟩)+∑i=1nπi​G​(𝐩i,𝐑i).G(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{a}\circ\mathbf{R})=G(\boldsymbol{\pi},\mathbf{a}\langle\!\!\!\langle\mathbf{p},\mathbf{R}\rangle\!\!\!\rangle)+\sum\_{i=1}^{n}\pi\_{i}G(\mathbf{p}^{i},\mathbf{R}^{i}). |  |

Assumption [(A1)](https://arxiv.org/html/2510.25740v1#S3.I1.i1 "item (A1) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") asks for a minimal degree of regularity to rule out pathological functions. [(A2)](https://arxiv.org/html/2510.25740v1#S3.I1.i2 "item (A2) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") is the permutation invariance of Proposition [2.1](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem1 "Proposition 2.1 (Permutation invariance). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"). [(A3)](https://arxiv.org/html/2510.25740v1#S3.I1.i3 "item (A3) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") highlights that only the returns of stocks included in the portfolio matter, and [(A4)](https://arxiv.org/html/2510.25740v1#S3.I1.i4 "item (A4) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") reflects the obvious fact that there is no benefit from diversification if all stocks in the portfolio have identical returns (Proposition [2.2](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem2 "Proposition 2.2 (Dependence on support). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")). Finally, [(A5)](https://arxiv.org/html/2510.25740v1#S3.I1.i5 "item (A5) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") is the general chain rule given in Theorem [2.5](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem5 "Theorem 2.5 (Chain rule (general)). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"). From Remark [2.6](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"), [(A5)](https://arxiv.org/html/2510.25740v1#S3.I1.i5 "item (A5) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") implies the numéraire invariance property G​(𝝅,a​𝐑)=G​(𝝅,𝐑)G(\boldsymbol{\pi},a\mathbf{R})=G(\boldsymbol{\pi},\mathbf{R}), a>0a>0.

###### Theorem 3.2 (Characterization I).

Let (G:𝒟n→ℝ)n≥1(G:\mathcal{D}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} be a family of functions. The following are equivalent:

* (i)

  The family satisfies [(A1)](https://arxiv.org/html/2510.25740v1#S3.I1.i1 "item (A1) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(A5)](https://arxiv.org/html/2510.25740v1#S3.I1.i5 "item (A5) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").
* (ii)

  G=c​ΓG=c\Gamma for some c∈ℝc\in\mathbb{R}.

We have seen in Section [2.1](https://arxiv.org/html/2510.25740v1#S2.SS1 "2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") that the family (c​Γ)n≥1(c\Gamma)\_{n\geq 1} satisfies [(A1)](https://arxiv.org/html/2510.25740v1#S3.I1.i1 "item (A1) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(A5)](https://arxiv.org/html/2510.25740v1#S3.I1.i5 "item (A5) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"); nothing is changed by multiplying Γ\Gamma by a constant. To prove the converse, we adopt the following strategy:

1. 1.

   Use numéraire invariance (from [(A5)](https://arxiv.org/html/2510.25740v1#S3.I1.i5 "item (A5) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) to reduce (G:𝒟n→ℝ)n≥1(G:\mathcal{D}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} to an equivalent family (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} of functions that take simplex-valued arguments.
2. 2.

   Using algebraic relations between the excess growth rate and the relative entropy (Lemma [3.4](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem4 "Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), as well as an axiomatic characterization of the latter (Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), derive the characterization when the domain of the reduced functions from Step 1 is restricted to Δn∘×Δn∘\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}.
3. 3.

   Extend the characterization to the full domain.

Step 1. Recall the set 𝒜n\mathcal{A}\_{n} defined by ([2.2](https://arxiv.org/html/2510.25740v1#S2.E2 "In 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")). Clearly, if (G:𝒟n→ℝ)n≥1(G:\mathcal{D}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} is numéraire invariant, it is characterized by its restriction to 𝒜n\mathcal{A}\_{n} (see ([2.3](https://arxiv.org/html/2510.25740v1#S2.E3 "In 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"))). We cast Theorem [3.2](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem2 "Theorem 3.2 (Characterization I). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") in the following equivalent form.

###### Theorem 3.3.

Let (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\to\mathbb{R})\_{n\geq 1} be a family of functions. The following are equivalent:

* (i)

  The family satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") where:

  1. (B1)

     𝖦​(𝝅,𝐫)\mathsf{G}(\boldsymbol{\pi},\mathbf{r}) is (jointly) Lebesgue measurable.
  2. (B2)

     𝖦​(𝝅​σ,𝐫​σ)=𝖦​(𝝅,𝐫)\mathsf{G}(\boldsymbol{\pi}\sigma,\mathbf{r}\sigma)=\mathsf{G}(\boldsymbol{\pi},\mathbf{r}) for every permutation σ\sigma.
  3. (B3)

     𝖦​(𝝅,𝐫)=𝖦​(𝝅,𝒞𝝅​[𝐫])\mathsf{G}(\boldsymbol{\pi},\mathbf{r})=\mathsf{G}(\boldsymbol{\pi},\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{r}]).
  4. (B4)

     𝖦​(𝝅,𝐫)=0\mathsf{G}(\boldsymbol{\pi},\mathbf{r})=0 if 𝒞𝝅​[𝐫]=𝐞¯𝝅\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{r}]=\overline{\mathbf{e}}\_{\boldsymbol{\pi}}, where 𝐞¯𝝅\overline{\mathbf{e}}\_{\boldsymbol{\pi}} is the barycenter on the support of 𝝅∈Δn\boldsymbol{\pi}\in\Delta\_{n} defined by 𝐞¯𝝅:=𝒞𝝅​[𝐞¯n]\overline{\mathbf{e}}\_{\boldsymbol{\pi}}:=\mathcal{C}\_{\boldsymbol{\pi}}[\bar{\mathbf{e}}\_{n}].
  5. (B5)

     For (𝝅,𝐚)∈𝒜n(\boldsymbol{\pi},\mathbf{a})\in\mathcal{A}\_{n}, ki≥1k\_{i}\geq 1, (𝐩i,𝐫i)∈𝒜ki(\mathbf{p}^{i},\mathbf{r}^{i})\in\mathcal{A}\_{k\_{i}}, 𝐩=(𝐩1,…,𝐩n)\mathbf{p}=(\mathbf{p}^{1},\dots,\mathbf{p}^{n}) and 𝐫=(𝐫1,…,𝐫n)\mathbf{r}=(\mathbf{r}^{1},\dots,\mathbf{r}^{n}), we have

     |  |  |  |
     | --- | --- | --- |
     |  | 𝖦​(𝝅∘𝐩,𝐚∘𝐫)=𝖦​(𝝅,𝒞𝝅​[𝐚​⟨⟨𝐩,𝐫⟩⟩])+∑i=1nπi​𝖦​(𝐩i,𝐫i).\mathsf{G}(\boldsymbol{\pi}\circ\mathbf{p},\mathbf{a}\circ\mathbf{r})=\mathsf{G}(\boldsymbol{\pi},\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{a}\langle\!\!\!\langle\mathbf{p},\mathbf{r}\rangle\!\!\!\rangle])+\sum\_{i=1}^{n}\pi\_{i}\,\mathsf{G}(\mathbf{p}^{i},\mathbf{r}^{i}). |  |
* (ii)

  𝖦=c​Γ\mathsf{G}=c\Gamma for some c∈ℝc\in\mathbb{R}.

It is easy to see that Theorem [3.2](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem2 "Theorem 3.2 (Characterization I). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and Theorem [3.3](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") are equivalent. Given a family (G:𝒟n→ℝ)n≥1(G:\mathcal{D}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} that satisfies [(A1)](https://arxiv.org/html/2510.25740v1#S3.I1.i1 "item (A1) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(A5)](https://arxiv.org/html/2510.25740v1#S3.I1.i5 "item (A5) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), let 𝖦\mathsf{G} be the restriction of GG to 𝒜n\mathcal{A}\_{n} (for each n≥1n\geq 1). For this choice, it can be easily verified that [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") hold. Similarly, if (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), we can define G​(𝝅,𝐑)=𝖦​(𝝅,𝒞𝝅​[𝐑])G(\boldsymbol{\pi},\mathbf{R})=\mathsf{G}(\boldsymbol{\pi},\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{R}]) and recover [(A1)](https://arxiv.org/html/2510.25740v1#S3.I1.i1 "item (A1) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(A5)](https://arxiv.org/html/2510.25740v1#S3.I1.i5 "item (A5) ‣ Assumption 3.1. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

Step 2. The key observation is the following link between the excess growth rate and the relative entropy. It is a slight extension of [[51](https://arxiv.org/html/2510.25740v1#bib.bib51), Lemma 2].

###### Lemma 3.4 (Excess growth rate as relative entropy).

For (𝛑,𝐫)∈𝒜n(\boldsymbol{\pi},\mathbf{r})\in\mathcal{A}\_{n} we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | Γ​(𝝅,𝐫)=H​(𝝅∥𝝅⊕𝝅𝐫)\Gamma(\boldsymbol{\pi},\mathbf{r})=H(\boldsymbol{\pi}\;\|\;\boldsymbol{\pi}\oplus\_{\boldsymbol{\pi}}\mathbf{r}) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | Γ(𝝅,𝐫⊖𝝅𝝅)=H(𝝅∥𝒞𝝅[𝐫]).\Gamma(\boldsymbol{\pi},\mathbf{r}\ominus\_{\boldsymbol{\pi}}\boldsymbol{\pi})=H\left(\boldsymbol{\pi}\;\middle\|\;\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{r}]\right). |  |

###### Proof.

Write 𝝅⊕𝝅𝐫=(1Z​πi​ri)1≤i≤n\boldsymbol{\pi}\oplus\_{\boldsymbol{\pi}}\mathbf{r}=(\frac{1}{Z}\pi\_{i}r\_{i})\_{1\leq i\leq n}, where Z=∑j∈supp⁡(𝝅)πj​rjZ=\sum\_{j\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{j}r\_{j} is a normalizing constant. We verify ([3.1](https://arxiv.org/html/2510.25740v1#S3.E1 "In Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) by a direct computation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(𝝅∥𝝅⊕𝝅𝐫)\displaystyle H(\boldsymbol{\pi}\;\|\;\boldsymbol{\pi}\oplus\_{\boldsymbol{\pi}}\mathbf{r}) | =∑i∈supp⁡(𝝅)πi​log⁡(πi1Z​πi​ri)\displaystyle=\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log\left(\frac{\pi\_{i}}{\frac{1}{Z}\pi\_{i}r\_{i}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i∈supp⁡(𝝅)πi​log⁡Zri\displaystyle=\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log\frac{Z}{r\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡Z​∑i∈supp⁡(𝝅)πi−∑i∈supp⁡(𝝅)πi​log⁡ri\displaystyle=\log Z\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log r\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡(∑i∈supp⁡(𝝅)πi​ri)−∑i∈supp⁡(𝝅)πi​log⁡ri\displaystyle=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}r\_{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log r\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Γ​(𝝅,𝐫).\displaystyle=\Gamma(\boldsymbol{\pi},\mathbf{r}). |  |

To prove ([3.2](https://arxiv.org/html/2510.25740v1#S3.E2 "In Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), write Z~:=∑i∈supp⁡(𝝅)ri/πi\tilde{Z}:=\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}r\_{i}/\pi\_{i}. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(𝝅,𝐫⊖𝝅𝝅)\displaystyle\Gamma(\boldsymbol{\pi},\mathbf{r}\ominus\_{\boldsymbol{\pi}}\boldsymbol{\pi}) | =log⁡(∑i∈supp⁡(𝝅)πi​ri/πiZ~)−∑i∈supp⁡(𝝅)πi​log⁡(ri/πiZ~)\displaystyle=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\frac{r\_{i}/\pi\_{i}}{\tilde{Z}}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log\left(\frac{r\_{i}/\pi\_{i}}{\tilde{Z}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡(∑i∈supp⁡(𝝅)ri)−∑i∈supp⁡(𝝅)πi​log⁡(riπi)\displaystyle=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}r\_{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log\left(\frac{r\_{i}}{\pi\_{i}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i∈supp⁡(𝝅)πi​log⁡(πiri/∑j∈supp⁡(𝝅)rj)\displaystyle=\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log\left(\frac{\pi\_{i}}{r\_{i}/\sum\_{j\in\operatorname{supp}(\boldsymbol{\pi})}r\_{j}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =H​(𝝅∥𝒞𝝅​[𝐫]).∎\displaystyle=H(\boldsymbol{\pi}\;\|\;\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{r}]).\qed |  |

###### Remark 3.5.

Let 𝐩,𝐪∈𝒜n​(𝛑∣⋅)\mathbf{p},\mathbf{q}\in\mathcal{A}\_{n}(\boldsymbol{\pi}\mid\cdot). From Definition [1.3](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem3 "Definition 1.3 (Excess growth rate as a divergence). ‣ 1. Introduction ‣ A mathematical study of the excess growth rate") and the previous result, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | Γ𝝅​(𝐪∥𝐩)=H​(𝝅∥𝝅⊕𝝅(𝐪⊖𝝅𝐩)).\Gamma\_{\boldsymbol{\pi}}(\mathbf{q}\;\|\;\mathbf{p})=H(\boldsymbol{\pi}\;\|\;\boldsymbol{\pi}\oplus\_{\boldsymbol{\pi}}(\mathbf{q}\ominus\_{\boldsymbol{\pi}}\mathbf{p})). |  |

Lemma [3.4](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem4 "Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") suggests that if a family (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), then I​(𝐩∥𝐪):=𝖦​(𝐩,𝐪⊖𝐩𝐩)I(\mathbf{p}\;\|\;\mathbf{q}):=\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p}), defined for (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n} and n≥1n\geq 1, is a constant multiple of the relative entropy. To this end, we will make use of the following characterization of the relative entropy on the *interior* of the simplex. It is a slight variant of existing characterizations of relative entropy (cf. [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Section 3.5]). Since it differs slightly in its domain and aspects of its assumptions, we provide a proof and a technical discussion in Appendix [A](https://arxiv.org/html/2510.25740v1#A1 "Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate").

###### Proposition 3.6 (Characterization of relative entropy on the open simplex).

Let (I(⋅∥⋅):Δn∘×Δn∘→ℝ)n≥1(I(\cdot\;\|\;\cdot):\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}\to\mathbb{R})\_{n\geq 1} be a family of functions. The following are equivalent:

* (i)

  The family satisfies [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C4)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i4 "item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") where:

  1. (C1)

     I(⋅∥⋅)I(\cdot\;\|\;\cdot) is separately Lebesgue measurable: for each fixed 𝐩\mathbf{p},
     the map 𝐩↦I​(𝐩∥𝐪)\mathbf{p}\mapsto I(\mathbf{p}\;\|\;\mathbf{q}) is Lebesgue measurable and for each fixed 𝐪\mathbf{q} the map 𝐩↦I​(𝐩∥𝐪)\mathbf{p}\mapsto I(\mathbf{p}\;\|\;\mathbf{q}) is Lebesgue measurable.
  2. (C2)

     I​(𝐩​σ∥𝐪​σ)=I​(𝐩∥𝐪)I(\mathbf{p}\sigma\;\|\;\mathbf{q}\sigma)=I(\mathbf{p}\;\|\;\mathbf{q}) for every permutation σ\sigma.
  3. (C3)

     I​(𝐩∥𝐩)=0I(\mathbf{p}\;\|\;\mathbf{p})=0 for all 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ};
  4. (C4)

     For (𝐩,𝐪)∈Δn∘×Δn∘(\mathbf{p},\mathbf{q})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}, and (𝝁i,𝝂i)∈Δki∘×Δki∘(\boldsymbol{\mu}^{i},\boldsymbol{\nu}^{i})\in\Delta\_{k\_{i}}^{\circ}\times\Delta\_{k\_{i}}^{\circ} for ki≥1k\_{i}\geq 1, i=1,…,ni=1,\dots,n, the following chain rule holds:

     |  |  |  |  |
     | --- | --- | --- | --- |
     | (3.4) |  | I​(𝐩∘𝝁∥𝐪∘𝝂)=I​(𝐩∥𝐪)+∑i=1npi​I​(𝝁i∥𝝂i).\displaystyle I(\mathbf{p}\circ\boldsymbol{\mu}\;\|\;\mathbf{q}\circ\boldsymbol{\nu})=I(\mathbf{p}\;\|\;\mathbf{q})+\sum\_{i=1}^{n}p\_{i}I(\boldsymbol{\mu}^{i}\;\|\;\boldsymbol{\nu}^{i}). |  |
* (ii)

  I(⋅∥⋅)=cH(⋅∥⋅)I(\cdot\;\|\;\cdot)=cH(\cdot\;\|\;\cdot) for some c∈ℝc\in\mathbb{R}.

With this characterization in mind, we establish a link between [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C4)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i4 "item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") through the function 𝖦​(𝐩,𝐪⊖𝐩𝐩)\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p}). For (𝝅,𝐫)∈𝒜n(\boldsymbol{\pi},\mathbf{r})\in\mathcal{A}\_{n}, we let

|  |  |  |
| --- | --- | --- |
|  | m𝝅​(𝐫):=∑i∈supp⁡(𝝅)ri>0m\_{\boldsymbol{\pi}}(\mathbf{r}):=\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}r\_{i}>0 |  |

for the mass that 𝐫\mathbf{r} puts on the support of 𝝅\boldsymbol{\pi}.

###### Lemma 3.7.

Suppose that (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\to\mathbb{R})\_{n\geq 1} satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). Define (I(⋅∥⋅):𝒜n→ℝ)n≥1(I(\cdot\;\|\;\cdot):\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} by I​(𝐩∥𝐪)=𝖦​(𝐩,𝐪⊖𝐩𝐩)I(\mathbf{p}\;\|\;\mathbf{q})=\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p}). Then the family (I(⋅∥⋅):𝒜n→ℝ)n≥1(I(\cdot\;\|\;\cdot):\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") with Δn∘×Δn∘\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ} replaced by 𝒜n\mathcal{A}\_{n} and the following version of the *chain rule*:

1. (C4′)

   For (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n}, ki≥1k\_{i}\geq 1, (𝝁i,𝝂i)∈𝒜ki(\boldsymbol{\mu}^{i},\boldsymbol{\nu}^{i})\in\mathcal{A}\_{k\_{i}}, 𝝁=(𝝁1,…,𝝁n)\boldsymbol{\mu}=(\boldsymbol{\mu}^{1},\dots,\boldsymbol{\mu}^{n}), and 𝝂=(𝝂1,…,𝝂n)\boldsymbol{\nu}=(\boldsymbol{\nu}^{1},\dots,\boldsymbol{\nu}^{n}), we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (3.5) |  | I​(𝐩∘𝝁∥𝐪∘𝝂)=𝖦​(𝐩,(𝐪⊖𝐩𝐩)⊕𝐩𝐡𝝁​(𝝂))+∑i=1npi​I​(𝝁i∥𝝂i),I(\mathbf{p}\circ\boldsymbol{\mu}\;\|\;\mathbf{q}\circ\boldsymbol{\nu})=\mathsf{G}(\mathbf{p},(\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})\oplus\_{\mathbf{p}}\mathbf{h}\_{\boldsymbol{\mu}}(\boldsymbol{\nu}))+\sum\_{i=1}^{n}p\_{i}I(\boldsymbol{\mu}^{i}\;\|\;\boldsymbol{\nu}^{i}), |  |

   where

   |  |  |  |
   | --- | --- | --- |
   |  | 𝐡𝝁​(𝝂):=(m𝝁i​(𝝂i)∑j=1nm𝝁j​(𝝂j))1≤i≤n∈Δn∘.\mathbf{h}\_{\boldsymbol{\mu}}(\boldsymbol{\nu}):=\left(\frac{m\_{\boldsymbol{\mu}^{i}}(\boldsymbol{\nu}^{i})}{\sum\_{j=1}^{n}m\_{\boldsymbol{\mu}^{j}}(\boldsymbol{\nu}^{j})}\right)\_{1\leq i\leq n}\in\Delta\_{n}^{\circ}. |  |

   In particular, when 𝝁\boldsymbol{\mu} and 𝝂\boldsymbol{\nu} are chosen so that supp⁡(𝝁i)=supp⁡(𝝂i)\operatorname{supp}(\boldsymbol{\mu}^{i})=\operatorname{supp}(\boldsymbol{\nu}^{i}) for all i=1,…,ni=1,\dots,n, then ([3.5](https://arxiv.org/html/2510.25740v1#S3.E5 "In item (C4′) ‣ Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) reduces to ([3.4](https://arxiv.org/html/2510.25740v1#S3.E4 "In item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")).

###### Proof.

We treat each property in turn.101010Note that [(B3)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i3 "item (B3) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") is not used here but will be needed in Step 3 below.

[(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") (on 𝒜n\mathcal{A}\_{n} and similarly below): This follows immediately from the joint measurability asserted in [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and composition with the measurable operation ⊖𝐩\ominus\_{\mathbf{p}}.

[(C2)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i2 "item (C2) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"): It is easy to check that (𝐪​σ⊖𝐩𝐩​σ)=(𝐪⊖𝐩𝐩)​σ(\mathbf{q}\sigma\ominus\_{\mathbf{p}}\mathbf{p}\sigma)=(\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})\sigma for any (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n} and permutation σ\sigma. Using this with [(B2)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i2 "item (B2) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") we obtain

|  |  |  |
| --- | --- | --- |
|  | I​(𝐩​σ∥𝐪​σ)=𝖦​(𝐩​σ,(𝐪​σ⊖𝐩𝐩​σ))=𝖦​(𝐩​σ,(𝐪⊖𝐩𝐩)​σ)=𝖦​(𝐩,(𝐪⊖𝐩𝐩))=I​(𝐩∥𝐪).I(\mathbf{p}\sigma\;\|\;\mathbf{q}\sigma)=\mathsf{G}\bigl(\mathbf{p}\sigma,(\mathbf{q}\sigma\ominus\_{\mathbf{p}}\mathbf{p}\sigma)\bigr)=\mathsf{G}\bigl(\mathbf{p}\sigma,(\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})\sigma\bigr)=\mathsf{G}\bigl(\mathbf{p},(\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})\bigr)=I(\mathbf{p}\;\|\;\mathbf{q}). |  |

[(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"): Observe that 𝐩⊖𝐩𝐩=𝐞¯𝐩\mathbf{p}\ominus\_{\mathbf{p}}\mathbf{p}=\overline{\mathbf{e}}\_{\mathbf{p}}. Therefore, by [(B4)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i4 "item (B4) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") we have

|  |  |  |
| --- | --- | --- |
|  | I​(𝐩∥𝐩)=𝖦​(𝐩,𝐩⊖𝐩𝐩)=𝖦​(𝐩,𝐞¯𝐩)=0.I(\mathbf{p}\;\|\;\mathbf{p})=\mathsf{G}(\mathbf{p},\mathbf{p}\ominus\_{\mathbf{p}}\mathbf{p})=\mathsf{G}(\mathbf{p},\overline{\mathbf{e}}\_{\mathbf{p}})=0. |  |

[(C4′)](https://arxiv.org/html/2510.25740v1#S3.I6.i4 "item (C4′) ‣ Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"): Consider

|  |  |  |
| --- | --- | --- |
|  | I​(𝐩∘𝝁∥𝐪∘𝝂)=𝖦​(𝐩∘𝝁,(𝐪∘𝝂)⊖𝐩∘𝝁(𝐩∘𝝁)).I(\mathbf{p}\circ\boldsymbol{\mu}\;\|\;\mathbf{q}\circ\boldsymbol{\nu})=\mathsf{G}(\mathbf{p}\circ\boldsymbol{\mu},(\mathbf{q}\circ\boldsymbol{\nu})\ominus\_{\mathbf{p}\circ\boldsymbol{\mu}}(\mathbf{p}\circ\boldsymbol{\mu})). |  |

In order to invoke the chain rule [(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), we express (𝐪∘𝝂)⊖𝐩∘𝝁(𝐩∘𝝁)(\mathbf{q}\circ\boldsymbol{\nu})\ominus\_{\mathbf{p}\circ\boldsymbol{\mu}}(\mathbf{p}\circ\boldsymbol{\mu}) as a composite distribution. Let ZZ be the normalizing constant in the definition of (𝐪∘𝝂)⊖𝐩∘𝝁(𝐩∘𝝁)(\mathbf{q}\circ\boldsymbol{\nu})\ominus\_{\mathbf{p}\circ\boldsymbol{\mu}}(\mathbf{p}\circ\boldsymbol{\mu}):

|  |  |  |
| --- | --- | --- |
|  | Z=∑(i,j)∈supp⁡(𝐩∘𝝁)(𝐪∘𝝂)i,j(𝐩∘𝝁)i,j=∑i∈supp⁡(𝐩)qipi​∑j∈supp⁡(𝝁i)νjiμji=∑i∈supp⁡(𝐩)qipi​Zi,\displaystyle Z=\sum\_{(i,j)\in\operatorname{supp}(\mathbf{p}\circ\boldsymbol{\mu})}\frac{(\mathbf{q}\circ\boldsymbol{\nu})\_{i,j}}{(\mathbf{p}\circ\boldsymbol{\mu})\_{i,j}}=\sum\_{i\in\operatorname{supp}(\mathbf{p})}\frac{q\_{i}}{p\_{i}}\sum\_{j\in\operatorname{supp}(\boldsymbol{\mu}^{i})}\frac{\nu^{i}\_{j}}{\mu^{i}\_{j}}=\sum\_{i\in\operatorname{supp}(\mathbf{p})}\frac{q\_{i}}{p\_{i}}Z\_{i}, |  |

where Zi=∑j∈supp⁡(𝝁i)νjiμjiZ\_{i}=\sum\_{j\in\operatorname{supp}(\boldsymbol{\mu}^{i})}\frac{\nu^{i}\_{j}}{\mu^{i}\_{j}} is strictly positive since (𝝁i,𝝂i)∈𝒜ki(\boldsymbol{\mu}^{i},\boldsymbol{\nu}^{i})\in\mathcal{A}\_{k^{i}}.
Write

|  |  |  |  |
| --- | --- | --- | --- |
|  | ((𝐪∘𝝂)⊖𝐩∘𝝁(𝐩∘𝝁))i,j\displaystyle\left((\mathbf{q}\circ\boldsymbol{\nu})\ominus\_{\mathbf{p}\circ\boldsymbol{\mu}}(\mathbf{p}\circ\boldsymbol{\mu})\right)\_{i,j} | =1Z​qi​νjipi​μji​𝟙supp⁡(𝐩)​(i)​𝟙supp⁡(𝝁i)​(j)\displaystyle=\frac{1}{Z}\frac{q\_{i}\nu\_{j}^{i}}{p\_{i}\mu\_{j}^{i}}\mathds{1}\_{\operatorname{supp}(\mathbf{p})}(i)\mathds{1}\_{\operatorname{supp}(\boldsymbol{\mu}^{i})}(j) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(qipi​ZiZ​𝟙supp⁡(𝐩)​(i))⋅(νji/μjiZi​𝟙supp⁡(𝝁i)​(j))\displaystyle=\left(\frac{\frac{q\_{i}}{p\_{i}}Z\_{i}}{Z}\mathds{1}\_{\operatorname{supp}(\mathbf{p})}(i)\right)\cdot\left(\frac{\nu\_{j}^{i}/\mu\_{j}^{i}}{Z\_{i}}\mathds{1}\_{\operatorname{supp}(\boldsymbol{\mu}^{i})}(j)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(𝝆∘𝝃)i,j,\displaystyle=(\boldsymbol{\rho}\circ\boldsymbol{\xi})\_{i,j}, |  |

where 𝝆=(ρ1,…,ρn)∈𝒜n​(𝐩∣⋅)\boldsymbol{\rho}=(\rho\_{1},\ldots,\rho\_{n})\in\mathcal{A}\_{n}(\mathbf{p}\mid\cdot) with

|  |  |  |
| --- | --- | --- |
|  | ρi=qipi​ZiZ​𝟙supp⁡(𝐩)​(i),i=1,…,n,\rho\_{i}=\frac{\frac{q\_{i}}{p\_{i}}Z\_{i}}{Z}\mathds{1}\_{\operatorname{supp}(\mathbf{p})}(i),\quad i=1,\ldots,n, |  |

and 𝝃=(𝝃1,…,𝝃n)\boldsymbol{\xi}=(\boldsymbol{\xi}^{1},\ldots,\boldsymbol{\xi}^{n}) with

|  |  |  |
| --- | --- | --- |
|  | 𝝃i=𝝂i⊖𝝁i𝝁i∈𝒜ki𝝁i,i=1,…,n.\boldsymbol{\xi}^{i}=\boldsymbol{\nu}^{i}\ominus\_{\boldsymbol{\mu}^{i}}\boldsymbol{\mu}^{i}\in\mathcal{A}\_{k\_{i}}^{\boldsymbol{\mu}^{i}},\quad i=1,\ldots,n. |  |

Therefore, we may apply [(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") to obtain,

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(𝐩∘𝝁∥𝐪∘𝝂)\displaystyle I(\mathbf{p}\circ\boldsymbol{\mu}\;\|\;\mathbf{q}\circ\boldsymbol{\nu}) | =𝖦​(𝐩∘𝝁,(𝐪∘𝝂)⊖𝐩∘𝝁(𝐩∘𝝁))\displaystyle=\mathsf{G}(\mathbf{p}\circ\boldsymbol{\mu},(\mathbf{q}\circ\boldsymbol{\nu})\ominus\_{\mathbf{p}\circ\boldsymbol{\mu}}(\mathbf{p}\circ\boldsymbol{\mu})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖦​(𝐩∘𝝁,𝝆∘𝝃)\displaystyle=\mathsf{G}(\mathbf{p}\circ\boldsymbol{\mu},\boldsymbol{\rho}\circ\boldsymbol{\xi}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖦​(𝐩,𝒞​[𝝆​⟨⟨μ,𝝃⟩⟩])+∑i=1npi​𝖦​(𝝁i,𝝃i)\displaystyle=\mathsf{G}(\mathbf{p},\mathcal{C}[\boldsymbol{\rho}\langle\!\!\!\langle\mu,\boldsymbol{\xi}\rangle\!\!\!\rangle])+\sum\_{i=1}^{n}p\_{i}\mathsf{G}(\boldsymbol{\mu}^{i},\boldsymbol{\xi}^{i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖦​(𝐩,𝒞​[𝝆​⟨⟨μ,𝝃⟩⟩])+∑i=1npi​I​(𝝁i∥𝝂i),\displaystyle=\mathsf{G}(\mathbf{p},\mathcal{C}[\boldsymbol{\rho}\langle\!\!\!\langle\mu,\boldsymbol{\xi}\rangle\!\!\!\rangle])+\sum\_{i=1}^{n}p\_{i}I(\boldsymbol{\mu}^{i}\;\|\;\boldsymbol{\nu}^{i}), |  |

where the last equality follows from the definitions of 𝝃i\boldsymbol{\xi}^{i} and IkiI\_{k\_{i}}:

|  |  |  |
| --- | --- | --- |
|  | 𝖦​(𝝁i,𝝃i)=𝖦​(𝝁i,𝝂i⊖𝝁i𝝁i)=I​(𝝁i∥𝝂i).\mathsf{G}(\boldsymbol{\mu}^{i},\boldsymbol{\xi}^{i})=\mathsf{G}(\boldsymbol{\mu}^{i},\boldsymbol{\nu}^{i}\ominus\_{\boldsymbol{\mu}^{i}}\boldsymbol{\mu}^{i})=I(\boldsymbol{\mu}^{i}\;\|\;\boldsymbol{\nu}^{i}). |  |

It remains to show that 𝒞​[𝝆​⟨⟨μ,𝝃⟩⟩]=(𝐪⊖𝐩𝐩)⊕𝐩𝐡𝝁​(𝝂)\mathcal{C}[\boldsymbol{\rho}\langle\!\!\!\langle\mu,\boldsymbol{\xi}\rangle\!\!\!\rangle]=(\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})\oplus\_{\mathbf{p}}\mathbf{h}\_{\boldsymbol{\mu}}(\boldsymbol{\nu}). To simplify the notation, for non-zero 𝐱,𝐲∈[0,∞)n\mathbf{x},\mathbf{y}\in[0,\infty)^{n} we write 𝐱∝𝐲\mathbf{x}\propto\mathbf{y} if 𝐲=c​𝐱\mathbf{y}=c\mathbf{x} for some c>0c>0. Clearly, 𝐱,𝐲∈Δn\mathbf{x},\mathbf{y}\in\Delta\_{n} are equal if and only if 𝐱∝𝐲\mathbf{x}\propto\mathbf{y}. Since

|  |  |  |
| --- | --- | --- |
|  | 𝒞​[𝝆​⟨⟨μ,𝝃⟩⟩]∝(ρi​⟨𝝁i,𝝃i⟩)i∝(qipi​Zi​𝟙supp⁡(𝐩)​(i)​(∑j=1nμji​ξji))i=(qipi​𝟙supp⁡(𝐩)​(i)​∑j=1nμji​(νji/μji)​𝟙supp⁡(𝝁i)​(j)∑ℓ=1ki(νℓi/μℓi)​𝟙supp⁡(𝝁j)​(ℓ))i=(qipi​𝟙supp⁡(𝐩)​(i)​m𝝁i​(𝝂i))i∝(𝐪⊖𝐩𝐩)⊕𝐩𝐡𝝁​(𝝂),\begin{split}\mathcal{C}[\boldsymbol{\rho}\langle\!\!\!\langle\mu,\boldsymbol{\xi}\rangle\!\!\!\rangle]&\propto\left(\rho\_{i}\langle\boldsymbol{\mu}^{i},\boldsymbol{\xi}^{i}\rangle\right)\_{i}\\ &\propto\left(\frac{q\_{i}}{p\_{i}}Z\_{i}\mathds{1}\_{\operatorname{supp}(\mathbf{p})}(i)\left(\sum\_{j=1}^{n}\mu\_{j}^{i}\xi\_{j}^{i}\right)\right)\_{i}\\ &=\left(\frac{q\_{i}}{p\_{i}}\mathds{1}\_{\operatorname{supp}(\mathbf{p})}(i)\sum\_{j=1}^{n}\mu\_{j}^{i}\frac{(\nu\_{j}^{i}/\mu\_{j}^{i})\mathds{1}\_{\operatorname{supp}(\boldsymbol{\mu}^{i})}(j)}{\sum\_{\ell=1}^{k\_{i}}(\nu\_{\ell}^{i}/\mu\_{\ell}^{i})\mathds{1}\_{\operatorname{supp}(\boldsymbol{\mu}^{j})}(\ell)}\right)\_{i}\\ &=\left(\frac{q\_{i}}{p\_{i}}\mathds{1}\_{\operatorname{supp}(\mathbf{p})}(i)m\_{\boldsymbol{\mu}^{i}}(\boldsymbol{\nu}^{i})\right)\_{i}\\ &\propto(\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})\oplus\_{\mathbf{p}}\mathbf{h}\_{\boldsymbol{\mu}}(\boldsymbol{\nu}),\end{split} |  |

the claim is proved and we have the chain rule in ([3.5](https://arxiv.org/html/2510.25740v1#S3.E5 "In item (C4′) ‣ Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")). Finally, note that if supp⁡(𝝁i)=supp⁡(𝝂i)\operatorname{supp}(\boldsymbol{\mu}^{i})=\operatorname{supp}(\boldsymbol{\nu}^{i}) then 𝐡𝝁​(𝝂)=𝐞¯n\mathbf{h}\_{\boldsymbol{\mu}}(\boldsymbol{\nu})=\bar{\mathbf{e}}\_{n}. Hence ([3.5](https://arxiv.org/html/2510.25740v1#S3.E5 "In item (C4′) ‣ Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) reduces to ([3.4](https://arxiv.org/html/2510.25740v1#S3.E4 "In item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")).
∎

###### Lemma 3.8 (Characterization on Δn∘×Δn∘\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}).

Theorem [3.3](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") holds if the domain 𝒜n\mathcal{A}\_{n} of 𝖦\mathsf{G} and [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") is replaced by Δn∘×Δn∘\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}.111111If (𝛑,𝐫)∈Δn∘×Δn∘(\boldsymbol{\pi},\mathbf{r})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}, then 𝒞𝛑​[𝐫]=𝐫\mathcal{C}\_{\boldsymbol{\pi}}[\mathbf{r}]=\mathbf{r}. Thus [(B3)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i3 "item (B3) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") holds automatically and may be removed.

###### Proof.

We only need to show (i) implies (ii). Given a family (𝖦:Δn∘×Δn∘→ℝ)n≥1(\mathsf{G}:\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}\rightarrow\mathbb{R})\_{n\geq 1} that satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), define I​(𝐩∥𝐪)=𝖦​(𝐩,𝐪⊖𝐩)I(\mathbf{p}\;\|\;\mathbf{q})=\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\mathbf{p}) for (𝐩,𝐪)∈Δn∘×Δn∘(\mathbf{p},\mathbf{q})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}. From Lemma [3.7](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem7 "Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), (I:Δn×Δn→ℝ)n≥1(I:\Delta\_{n}\times\Delta\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C4)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i4 "item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). By Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), there exists c∈ℝc\in\mathbb{R} such that for all n≥1n\geq 1 we have

|  |  |  |
| --- | --- | --- |
|  | 𝖦​(𝐩,𝐪⊖𝐩)=c​H​(𝐩∥𝐪),(𝐩,𝐪)∈Δn∘×Δn∘.\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\mathbf{p})=cH(\mathbf{p}\;\|\;\mathbf{q}),\quad(\mathbf{p},\mathbf{q})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}. |  |

Since ⊖\ominus is invertible on Δn∘\Delta\_{n}^{\circ}, we get (by Lemma [3.4](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem4 "Lemma 3.4 (Excess growth rate as relative entropy). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"))

|  |  |  |
| --- | --- | --- |
|  | 𝖦​(𝐩,𝐪)=c​H​(𝐩∥𝐩⊕𝐪)=c​Γ​(𝐩,𝐪),(𝐩,𝐪)∈Δn∘×Δn∘.∎\mathsf{G}(\mathbf{p},\mathbf{q})=cH(\mathbf{p}\;\|\;\mathbf{p}\oplus\mathbf{q})=c\Gamma(\mathbf{p},\mathbf{q}),\quad(\mathbf{p},\mathbf{q})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}.\qed |  |

Step 3. We extend the characterization from Δn∘×Δn∘\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ} to all of 𝒜n\mathcal{A}\_{n}. To do so, we need two auxiliary results that address the boundary values. For 𝐩∈[0,∞)n\mathbf{p}\in[0,\infty)^{n} with support supp⁡(𝐩)={j1,…,jd}≠∅\operatorname{supp}(\mathbf{p})=\{j\_{1},\dots,j\_{d}\}\neq\emptyset (ordered according to increasing index j1<j2<⋯<jdj\_{1}<j\_{2}<\cdots<j\_{d}),
we define the *coordinate projection operator* Π𝐩:[0,∞)n→[0,∞)d\Pi\_{\mathbf{p}}:[0,\infty)^{n}\to[0,\infty)^{d}, d=|supp⁡(𝐩)|d=|\operatorname{supp}(\mathbf{p})|, by

|  |  |  |
| --- | --- | --- |
|  | (Π𝐩​[𝐪])i:=qji,i=1,…,d.\big(\Pi\_{\mathbf{p}}[\mathbf{q}]\big)\_{i}:=q\_{j\_{i}},\qquad i=1,\dots,d. |  |

In words, Π𝐩​[𝐪]\Pi\_{\mathbf{p}}[\mathbf{q}] restricts 𝐪\mathbf{q} to the coordinates in supp⁡(𝐩)\operatorname{supp}(\mathbf{p}). Note that

|  |  |  |
| --- | --- | --- |
|  | (𝐩,𝐪)∈𝒜n⇒Π𝐩​[𝒞𝐩​[𝐪]]∈Δ|supp⁡(𝐩)|∘.(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n}\Rightarrow\Pi\_{\mathbf{p}}[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]]\in\Delta\_{|\operatorname{supp}(\mathbf{p})|}^{\circ}. |  |

For clarity, in the following we sometimes use IkI\_{k} and 𝖦k\mathsf{G}\_{k} to show explicitly the underlying dimension.

###### Lemma 3.9.

Suppose (I(⋅∥⋅):𝒜n→ℝ)n≥1(I(\cdot\;\|\;\cdot):\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and [(C4′)](https://arxiv.org/html/2510.25740v1#S3.I6.i4 "item (C4′) ‣ Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). Then, there exists a Lebesgue measurable function φ:(0,1]→ℝ\varphi:(0,1]\to\mathbb{R} with φ​(1)=0\varphi(1)=0 such that
for every (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n} we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | I​(𝐩∥𝐪)=φ​(m𝐩​(𝐪))+I|supp⁡(𝐩)|​(Π𝐩​[𝐩]∥Π𝐩​[𝒞𝐩​[𝐪]]).I(\mathbf{p}\;\|\;\mathbf{q})=\varphi(m\_{\mathbf{p}}(\mathbf{q}))+I\_{|\operatorname{supp}(\mathbf{p})|}(\Pi\_{\mathbf{p}}[\mathbf{p}]\;\|\;\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]). |  |

###### Proof.

Fix (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n} and set d=|supp⁡(𝐩)|∈[n]d=|\operatorname{supp}(\mathbf{p})|\in[n].
Write 𝐩^=Π𝐩​[𝐩]∈Δd∘\hat{\mathbf{p}}=\Pi\_{\mathbf{p}}[\mathbf{p}]\in\Delta\_{d}^{\circ} and 𝐪^=Π𝐩​[𝒞𝐩​[𝐪]]∈Δd∘\hat{\mathbf{q}}=\Pi\_{\mathbf{p}}[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]]\in\Delta\_{d}^{\circ}.

Case 1. d=nd=n. Then 𝐩^=𝐩\hat{\mathbf{p}}=\mathbf{p}, 𝐪^=𝐪\hat{\mathbf{q}}=\mathbf{q} and m𝐩​(𝐪)=1m\_{\mathbf{p}}(\mathbf{q})=1. The identity ([3.6](https://arxiv.org/html/2510.25740v1#S3.E6 "In Lemma 3.9. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) holds by letting φ​(1)=0\varphi(1)=0.

Case 2. d<nd<n. After permuting coordinates (using [(C2)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i2 "item (C2) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) if necessary, we may assume supp⁡(𝐩)={1,…,d}\operatorname{supp}(\mathbf{p})=\{1,\dots,d\}. Let m=m𝐩​(𝐪)∈(0,1]m=m\_{\mathbf{p}}(\mathbf{q})\in(0,1]. Next, define 𝐪^′∈Δn−d\hat{\mathbf{q}}^{\prime}\in\Delta\_{n-d} through q^i′=qi+d/(1−m)\hat{q}^{\prime}\_{i}=q\_{i+d}/(1-m) for i=1,…,n−di=1,\dots,n-d to account for the renormalized values of 𝐪\mathbf{q} off the support of 𝐩\mathbf{p}. If m=1m=1, we may take any arbitrary 𝐪^′∈Δn−d\hat{\mathbf{q}}^{\prime}\in\Delta\_{n-d}. By construction, we may represent 𝐩\mathbf{p} and 𝐪\mathbf{q} as the compositions

|  |  |  |
| --- | --- | --- |
|  | 𝐩=(1,0)∘(𝐩^,𝐪^′),𝐪=(m,1−m)∘(𝐪^,𝐪^′).\mathbf{p}=(1,0)\circ(\hat{\mathbf{p}},\hat{\mathbf{q}}^{\prime}),\quad\mathbf{q}=(m,1-m)\circ(\hat{\mathbf{q}},\hat{\mathbf{q}}^{\prime}). |  |

Since ((1,0),(m,1−m))∈𝒜2((1,0),(m,1-m))\in\mathcal{A}\_{2} and supp⁡(𝐩^)=supp⁡(𝐪^)=[d]\operatorname{supp}(\hat{\mathbf{p}})=\operatorname{supp}(\hat{\mathbf{q}})=[d], the special case in [(C4′)](https://arxiv.org/html/2510.25740v1#S3.I6.i4 "item (C4′) ‣ Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") applies and we obtain

|  |  |  |
| --- | --- | --- |
|  | I​(𝐩∥𝐪)=I2​((1,0)∥(m,1−m))+Id​(𝐩^∥𝐪^).I(\mathbf{p}\;\|\;\mathbf{q})=I\_{2}((1,0)\;\|\;(m,1-m))+I\_{d}(\hat{\mathbf{p}}\;\|\;\hat{\mathbf{q}}). |  |

Thus ([3.6](https://arxiv.org/html/2510.25740v1#S3.E6 "In Lemma 3.9. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) holds with φ​(m):=I2​((1,0)∥(m,1−m))\varphi(m):=I\_{2}((1,0)\;\|\;(m,1-m)). Measurability of φ\varphi follows from [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and that φ​(1)=0\varphi(1)=0 follows from [(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").
∎

###### Lemma 3.10.

Suppose that (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and define I​(𝐩∥𝐪)=𝖦​(𝐩,𝐪⊖𝐩𝐩)I(\mathbf{p}\;\|\;\mathbf{q})=\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p}) for (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n}. Then for (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n} we have

|  |  |  |
| --- | --- | --- |
|  | I​(𝐩∥𝐪)=I|supp⁡(𝐩)|​(Π𝐩​[𝐩]∥Π𝐩​[𝒞𝐩​[𝐪]]).I(\mathbf{p}\;\|\;\mathbf{q})=I\_{|\operatorname{supp}(\mathbf{p})|}(\Pi\_{\mathbf{p}}[\mathbf{p}]\;\|\;\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]). |  |

In particular, the function φ\varphi from Lemma [3.9](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem9 "Lemma 3.9. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") vanishes identically.

###### Proof.

Since (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), Lemma [3.7](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem7 "Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") implies that (I:𝒜n→ℝ)n≥1(I:\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and [(C4′)](https://arxiv.org/html/2510.25740v1#S3.I6.i4 "item (C4′) ‣ Lemma 3.7. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). By Lemma [3.9](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem9 "Lemma 3.9. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), there exists a measurable φ​(⋅)\varphi(\cdot) on (0,1](0,1] with φ​(1)=0\varphi(1)=0 satisfying ([3.6](https://arxiv.org/html/2510.25740v1#S3.E6 "In Lemma 3.9. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")). We claim that φ​(⋅)≡0\varphi(\cdot)\equiv 0.

Fix nn and 𝐩∈Δn\mathbf{p}\in\Delta\_{n} be such that |supp⁡(𝐩)|<n|\operatorname{supp}(\mathbf{p})|<n. For α∈(0,1]\alpha\in(0,1], let 𝐪(α)∈𝒜n​(𝐩∣⋅)\mathbf{q}^{(\alpha)}\in\mathcal{A}\_{n}(\mathbf{p}\mid\cdot) be such that 𝒞𝐩​[𝐪(α)]=𝐩\mathcal{C}\_{\mathbf{p}}[\mathbf{q}^{(\alpha)}]=\mathbf{p} and m𝐩​(𝐪(α))=αm\_{\mathbf{p}}(\mathbf{q}^{(\alpha)})=\alpha. Such a 𝐪(α)\mathbf{q}^{(\alpha)} can always be constructed by multiplying the coordinates of 𝐩\mathbf{p} by α\alpha and distributing the remaining mass 1−α1-\alpha arbitrarily on [n]∖supp⁡(𝐩)[n]\setminus\operatorname{supp}(\mathbf{p}).
Then, by Lemma [3.9](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem9 "Lemma 3.9. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and [(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(𝐩∥𝐪(α))\displaystyle I(\mathbf{p}\;\|\;\mathbf{q}^{(\alpha)}) | =φ(m𝐩(𝐪(α)))+I|supp⁡(𝐩)|(Π𝐩[𝐩]∥Π𝐩[𝒞𝐩[𝐪(α)]])\displaystyle=\varphi(m\_{\mathbf{p}}(\mathbf{q}^{(\alpha)}))+I\_{|\operatorname{supp}(\mathbf{p})|}\left(\Pi\_{\mathbf{p}}[\mathbf{p}]\;\middle\|\;\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}^{(\alpha)}]\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =φ​(α)+I|supp⁡(𝐩)|​(Π𝐩​[𝐩]∥Π𝐩​[𝐩])=φ​(α).\displaystyle=\varphi(\alpha)+I\_{|\operatorname{supp}(\mathbf{p})|}(\Pi\_{\mathbf{p}}[\mathbf{p}]\;\|\;\Pi\_{\mathbf{p}}[\mathbf{p}])=\varphi(\alpha). |  |

On the other hand, I​(𝐩∥𝐪(α))=𝖦​(𝐩,𝐪(α)⊖𝐩𝐩)I(\mathbf{p}\;\|\;\mathbf{q}^{(\alpha)})=\mathsf{G}(\mathbf{p},\mathbf{q}^{(\alpha)}\ominus\_{\mathbf{p}}\mathbf{p}), and a direct calculation shows that 𝐪(α)⊖𝐩𝐩=𝐞¯𝐩\mathbf{q}^{(\alpha)}\ominus\_{\mathbf{p}}\mathbf{p}=\overline{\mathbf{e}}\_{\mathbf{p}},
the uniform distribution on supp⁡(𝐩)\operatorname{supp}(\mathbf{p}). By [(B4)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i4 "item (B4) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), 𝖦​(𝐩,𝐞¯𝐩)=0\mathsf{G}(\mathbf{p},\overline{\mathbf{e}}\_{\mathbf{p}})=0, hence I​(𝐩∥𝐪(α))=0I(\mathbf{p}\;\|\;\mathbf{q}^{(\alpha)})=0. Therefore, φ​(α)=0\varphi(\alpha)=0 for all α∈(0,1]\alpha\in(0,1], and so φ​(⋅)≡0\varphi(\cdot)\equiv 0.
∎

We are now ready to complete the proof of Theorem [3.3](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") (and therefore, of Theorem [3.2](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem2 "Theorem 3.2 (Characterization I). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") as well).

###### Proof of Theorem [3.3](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

We have seen that (c​Γ)n≥1(c\Gamma)\_{n\geq 1} satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). On the other hand, suppose that the collection (𝖦:𝒜n→ℝ)n≥1(\mathsf{G}:\mathcal{A}\_{n}\rightarrow\mathbb{R})\_{n\geq 1} satisfies [(B1)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i1 "item (B1) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(B5)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i5 "item (B5) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). By Lemma [3.8](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem8 "Lemma 3.8 (Characterization on Δ_𝑛^∘×Δ_𝑛^∘). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), there exists a c∈ℝc\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | 𝖦​(𝐩,𝐪)=c​Γ​(𝐩,𝐪),for all n and ​(𝐩,𝐪)∈Δn∘×Δn∘.\mathsf{G}(\mathbf{p},\mathbf{q})=c\Gamma(\mathbf{p},\mathbf{q}),\quad\text{for all $n$ and }(\mathbf{p},\mathbf{q})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}. |  |

Next, observe that for any (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n},

|  |  |  |
| --- | --- | --- |
|  | (Π𝐩​[𝐩],Π𝐩​[𝒞𝐩​[𝐪]])∈Δ|supp⁡(𝐩)|∘×Δ|supp⁡(𝐩)|∘\left(\Pi\_{\mathbf{p}}[\mathbf{p}],\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]\right)\in\Delta\_{|\operatorname{supp}(\mathbf{p})|}^{\circ}\times\Delta\_{|\operatorname{supp}(\mathbf{p})|}^{\circ} |  |

and moreover, (Π𝐩​[𝒞𝐩​[𝐪]]⊖𝐩Π𝐩​[𝐩])∈Δn∘(\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]\ominus\_{\mathbf{p}}\Pi\_{\mathbf{p}}[\mathbf{p}])\in\Delta\_{n}^{\circ}. Therefore, by Lemma [3.10](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") (and writing I​(𝐩∥𝐪)=𝖦​(𝐩,𝐪⊖𝐩𝐩)I(\mathbf{p}\;\|\;\mathbf{q})=\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖦​(𝐩,𝐪⊖𝐩𝐩)\displaystyle\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p}) | =I​(𝐩∥𝐪)\displaystyle=I(\mathbf{p}\;\|\;\mathbf{q}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =I|supp⁡(𝐩)|​(Π𝐩​[𝐩]∥Π𝐩​[𝒞𝐩​[𝐪]])\displaystyle=I\_{|\operatorname{supp}(\mathbf{p})|}(\Pi\_{\mathbf{p}}[\mathbf{p}]\;\|\;\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖦|supp⁡(𝐩)|​(Π𝐩​[𝐩],Π𝐩​[𝒞𝐩​[𝐪]]⊖𝐩Π𝐩​[𝐩])\displaystyle=\mathsf{G}\_{|\operatorname{supp}(\mathbf{p})|}\left(\Pi\_{\mathbf{p}}[\mathbf{p}],\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]\ominus\_{\mathbf{p}}\Pi\_{\mathbf{p}}[\mathbf{p}]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​Γ|supp⁡(𝐩)|​(Π𝐩​[𝐩],Π𝐩​[𝒞𝐩​[𝐪]]⊖𝐩Π𝐩​[𝐩]).\displaystyle=c\Gamma\_{|\operatorname{supp}(\mathbf{p})|}\left(\Pi\_{\mathbf{p}}[\mathbf{p}],\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]\ominus\_{\mathbf{p}}\Pi\_{\mathbf{p}}[\mathbf{p}]\right). |  |

One readily checks that

|  |  |  |
| --- | --- | --- |
|  | Γ|supp⁡(𝐩)|​(Π𝐩​[𝐩],Π𝐩​[𝒞𝐩​[𝐪]]⊖Π𝐩​[𝐩])=Γ​(𝐩,𝐪⊖𝐩𝐩),\Gamma\_{|\operatorname{supp}(\mathbf{p})|}\left(\Pi\_{\mathbf{p}}[\mathbf{p}],\Pi\_{\mathbf{p}}\left[\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]\right]\ominus\Pi\_{\mathbf{p}}[\mathbf{p}]\right)=\Gamma\left(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p}\right), |  |

and hence

|  |  |  |
| --- | --- | --- |
|  | 𝖦​(𝐩,𝐪⊖𝐩𝐩)=c​Γ​(𝐩,𝐪⊖𝐩𝐩),(𝐩,𝐪)∈𝒜n.\mathsf{G}(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p})=c\Gamma\left(\mathbf{p},\mathbf{q}\ominus\_{\mathbf{p}}\mathbf{p}\right),\quad(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n}. |  |

Unwinding by writing 𝒞𝐩​[𝐪]=(𝐪⊕𝐩𝐩)⊖𝐩𝐩\mathcal{C}\_{\mathbf{p}}[\mathbf{q}]=(\mathbf{q}\oplus\_{\mathbf{p}}\mathbf{p})\ominus\_{\mathbf{p}}\mathbf{p}, we see that this implies

|  |  |  |
| --- | --- | --- |
|  | 𝖦​(𝐩,𝒞𝐩​[𝐪])=c​Γ​(𝐩,𝐪).\mathsf{G}(\mathbf{p},\mathcal{C}\_{\mathbf{p}}[\mathbf{q}])=c\Gamma\left(\mathbf{p},\mathbf{q}\right). |  |

Finally, we invoke [(B3)](https://arxiv.org/html/2510.25740v1#S3.I4.ix1.I1.i3 "item (B3) ‣ item (i) ‣ Theorem 3.3. ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") to obtain

|  |  |  |
| --- | --- | --- |
|  | 𝖦​(𝐩,𝐪)=𝖦​(𝐩,𝒞𝐩​[𝐪])=c​Γ​(𝐩,𝐪),(𝐩,𝐪)∈𝒜n,\mathsf{G}(\mathbf{p},\mathbf{q})=\mathsf{G}(\mathbf{p},\mathcal{C}\_{\mathbf{p}}[\mathbf{q}])=c\Gamma\left(\mathbf{p},\mathbf{q}\right),\quad(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n}, |  |

which completes the proof.
∎

### 3.2. Via Jensen gap

In this subsection, we characterize the excess growth rate

|  |  |  |
| --- | --- | --- |
|  | Γ​(𝝅,𝐑)=log⁡(∑i∈supp⁡(𝝅)πi​Ri)−∑i∈supp⁡(𝝅)πi​log⁡Ri,(𝝅,𝐑)∈𝒜n,\Gamma(\boldsymbol{\pi},\mathbf{R})=\log\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}R\_{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\log R\_{i},\quad(\boldsymbol{\pi},\mathbf{R})\in\mathcal{A}\_{n}, |  |

where n≥2n\geq 2 is fixed, as the gap in Jensen’s inequality with respect to the logarithm which is strictly concave.

We say that g:𝒜n→ℝg:\mathcal{A}\_{n}\rightarrow\mathbb{R} is a gap function if there exists φ:(0,∞)→ℝ\varphi:(0,\infty)\rightarrow\mathbb{R} (which may be neither convex nor concave) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.7) |  | g​(𝝅,𝐑)=φ​(∑i∈supp⁡(𝝅)πi​Ri)−∑i∈supp⁡(𝝅)πi​φ​(Ri),(𝝅,𝐑)∈𝒜n.g(\boldsymbol{\pi},\mathbf{R})=\varphi\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}R\_{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\varphi(R\_{i}),\quad(\boldsymbol{\pi},\mathbf{R})\in\mathcal{A}\_{n}. |  |

We call φ\varphi the generator of gg. Thus, Γ\Gamma is the gap function with generator φ=log\varphi=\log. Note that since Ri>0R\_{i}>0 for i∈supp⁡(𝝅)i\in\operatorname{supp}(\boldsymbol{\pi}), φ\varphi only needs to be defined on (0,∞)(0,\infty).

###### Lemma 3.11 (Uniqueness of generator).

The generator of a gap function is unique up to the addition of an affine function. More precisely, if gg is a gap function and φ\varphi and φ~\tilde{\varphi} are generators (that is, ([3.7](https://arxiv.org/html/2510.25740v1#S3.E7 "In 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) holds for both φ\varphi and φ~\tilde{\varphi}), then φ​(R)−φ~​(R)≡a​R+b\varphi(R)-\tilde{\varphi}(R)\equiv aR+b for some a,b∈ℝa,b\in\mathbb{R}.

###### Proof.

Let 0<R¯<R¯0<\underaccent{\bar}{R}<\bar{R} be given, and let

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(R¯,R¯,1,…,1)∈(0,∞)n.\mathbf{R}=(\underaccent{\bar}{R},\bar{R},1,\ldots,1)\in(0,\infty)^{n}. |  |

For R∈[R¯,R¯]R\in[\underaccent{\bar}{R},\bar{R}], consider

|  |  |  |
| --- | --- | --- |
|  | 𝝅​(R):=(R¯−RR¯−R¯,R−R¯R¯−R¯,0,…,0)∈Δn.\boldsymbol{\pi}(R):=\left(\frac{\bar{R}-R}{\bar{R}-\underaccent{\bar}{R}},\frac{R-\underaccent{\bar}{R}}{\bar{R}-\underaccent{\bar}{R}},0,\ldots,0\right)\in\Delta\_{n}. |  |

Then ⟨𝝅​(R),𝐑⟩=R\langle\boldsymbol{\pi}(R),\mathbf{R}\rangle=R and we have

|  |  |  |
| --- | --- | --- |
|  | g​(𝝅,𝐑)=φ​(R)−R¯−RR¯−R¯​φ​(R¯)−R−R¯R¯−R¯​φ​(R¯)=φ~​(R)−R¯−RR¯−R¯​φ~​(R¯)−R−R¯R¯−R¯​φ~​(R¯).\begin{split}g(\boldsymbol{\pi},\mathbf{R})&=\varphi(R)-\frac{\bar{R}-R}{\bar{R}-\underaccent{\bar}{R}}\varphi(\underaccent{\bar}{R})-\frac{R-\underaccent{\bar}{R}}{\bar{R}-\underaccent{\bar}{R}}\varphi(\bar{R})\\ &=\tilde{\varphi}(R)-\frac{\bar{R}-R}{\bar{R}-\underaccent{\bar}{R}}\tilde{\varphi}(\underaccent{\bar}{R})-\frac{R-\underaccent{\bar}{R}}{\bar{R}-\underaccent{\bar}{R}}\tilde{\varphi}(\bar{R}).\end{split} |  |

It follows that φ​(R)−φ~​(R)\varphi(R)-\tilde{\varphi}(R) is affine in RR on [R¯,R¯][\underaccent{\bar}{R},\bar{R}]. Since R¯,R¯\underaccent{\bar}{R},\bar{R} are arbitrary (and the intercept and slope remain the same upon extension of the domain), φ−φ~\varphi-\tilde{\varphi} is affine on (0,∞)(0,\infty) and the lemma is proved.
∎

Our goal is the characterize the excess growth rate among the family of gap functions. For 𝐑∈[0,∞)n∖{𝟎}\mathbf{R}\in[0,\infty)^{n}\setminus\{\mathbf{0}\} (where 𝟎=(0,…,0){\bf 0}=(0,\ldots,0) is the zero vector), we define

|  |  |  |
| --- | --- | --- |
|  | 𝒟n(⋅∣𝐑):={𝝅∈Δn:(𝝅,𝐑)∈𝒟n}\mathcal{D}\_{n}(\cdot\mid\mathbf{R}):=\{\boldsymbol{\pi}\in\Delta\_{n}:(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n}\} |  |

be the slice of 𝒟n\mathcal{D}\_{n} given the second slot. Consider the following assumptions on g:𝒜n→ℝg:\mathcal{A}\_{n}\rightarrow\mathbb{R}.

###### Assumption 3.12.

1. (D1)

   For every 𝐑∈[0,∞)n∖{𝟎}\mathbf{R}\in[0,\infty)^{n}\setminus\{\mathbf{0}\}, the map 𝝅↦g​(𝝅,𝐑)\boldsymbol{\pi}\mapsto g(\boldsymbol{\pi},\mathbf{R}) is concave on 𝒟n(⋅∣𝐑)\mathcal{D}\_{n}(\cdot\mid\mathbf{R}).
2. (D2)

   g​(𝝅,𝐑)=0g(\boldsymbol{\pi},\mathbf{R})=0 if 𝐑\mathbf{R} is constant on supp⁡(𝝅)\operatorname{supp}(\boldsymbol{\pi}).
3. (D3)

   g​(𝝅,α​𝐑)=g​(𝝅,𝐑)g(\boldsymbol{\pi},\alpha\mathbf{R})=g(\boldsymbol{\pi},\mathbf{R}) for all (𝝅,𝐑)∈𝒟n(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n} and α>0\alpha>0.
4. (D4)

   For m∈(0,∞)m\in(0,\infty) and 𝐑∈[0,∞)n∖{𝟎}\mathbf{R}\in[0,\infty)^{n}\setminus\{\mathbf{0}\}, let Cm,𝐑⊂𝒟n(⋅∣𝐑)C\_{m,\mathbf{R}}\subset\mathcal{D}\_{n}(\cdot\mid\mathbf{R}) be the constant mean set (which is convex) defined by

   |  |  |  |
   | --- | --- | --- |
   |  | Cm,𝐑:={𝝅∈𝒟n(⋅∣𝐑):⟨𝝅,𝐑⟩=m}.C\_{m,\mathbf{R}}:=\{\boldsymbol{\pi}\in\mathcal{D}\_{n}(\cdot\mid\mathbf{R}):\langle\boldsymbol{\pi},\mathbf{R}\rangle=m\}. |  |

   Then, for any mm and 𝐑\mathbf{R}, the map 𝝅↦g​(𝝅,𝐑)\boldsymbol{\pi}\mapsto g(\boldsymbol{\pi},\mathbf{R}) is affine on Cm,𝐑C\_{m,\mathbf{R}}:

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (3.8) |  | g​(𝝅,𝐑)=⟨𝐚​(𝐑),𝝅⟩+b​(m),𝝅∈Cm,𝐑,g(\boldsymbol{\pi},\mathbf{R})=\langle\mathbf{a}(\mathbf{R}),\boldsymbol{\pi}\rangle+b(m),\quad\boldsymbol{\pi}\in C\_{m,\mathbf{R}}, |  |

   for some gradient 𝐚​(𝐑)∈ℝn\mathbf{a}(\mathbf{R})\in\mathbb{R}^{n} that depends only on 𝐑\mathbf{R} and is Lebesgue measurable in 𝐑\mathbf{R}, and the intercept b​(m)∈ℝb(m)\in\mathbb{R} depends only on mm and is Lebesgue measurable in mm.

Note that [(D3)](https://arxiv.org/html/2510.25740v1#S3.I7.i3 "item (D3) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") encodes numéraire invariance. In Section [3.1](https://arxiv.org/html/2510.25740v1#S3.SS1 "3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), numéraire invariance allows us to restrict the domain of 𝐑\mathbf{R} to the simplex; the main argument is then driven by the chain rule. Here, numéraire invariance is the key property that distinguishes the excess growth rate (again up to a multiplicative constant) among other gap functions. To motivate [(D4)](https://arxiv.org/html/2510.25740v1#S3.I7.i4 "item (D4) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), assume that gg is a gap function whose generator φ\varphi is Lebesgue measurable. On the constant mean set Dm,𝐑D\_{m,\mathbf{R}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.9) |  | g​(𝝅,𝐑)=φ​(m)−∑i=1nπi​φ​(Ri),\begin{split}g(\boldsymbol{\pi},\mathbf{R})=\varphi(m)-\sum\_{i=1}^{n}\pi\_{i}\varphi(R\_{i}),\end{split} |  |

which is affine in 𝝅\boldsymbol{\pi}. We may take 𝐚​(𝐑)=(−φ​(Ri))1≤i≤n\mathbf{a}(\mathbf{R})=(-\varphi(R\_{i}))\_{1\leq i\leq n} and b​(m)=φ​(m)b(m)=\varphi(m) which are Lebesgue measurable in 𝐑\mathbf{R} and mm respectively.

###### Theorem 3.13 (Characterization II).

Let n≥2n\geq 2 and let g:𝒜n→ℝg:\mathcal{A}\_{n}\rightarrow\mathbb{R} be (jointly) Lebesgue measurable.

* (i)

  gg is a gap function with a Lebesgue measurable generator if and only if it satisfies [(D2)](https://arxiv.org/html/2510.25740v1#S3.I7.i2 "item (D2) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and [(D4)](https://arxiv.org/html/2510.25740v1#S3.I7.i4 "item (D4) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). In this case, the generator φ\varphi (which is unique up to an affine function by Lemma [3.11](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem11 "Lemma 3.11 (Uniqueness of generator). ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) is concave if and only if [(D1)](https://arxiv.org/html/2510.25740v1#S3.I7.i1 "item (D1) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") holds.
* (ii)

  gg satisfies [(D2)](https://arxiv.org/html/2510.25740v1#S3.I7.i2 "item (D2) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(D4)](https://arxiv.org/html/2510.25740v1#S3.I7.i4 "item (D4) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") if and only if g=c​Γg=c\Gamma for some c∈ℝc\in\mathbb{R}. In this case, c≥0c\geq 0 if and only if [(D1)](https://arxiv.org/html/2510.25740v1#S3.I7.i1 "item (D1) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") holds.

Despite the importance of Jensen’s inequality, we have not been able to locate axiomatic characterizations of its gap in the literature.
Before proving Theorem [3.13](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem13 "Theorem 3.13 (Characterization II). ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), we compare it with known results about the quasiarithmetic mean of which the exponential mean in ([1.8](https://arxiv.org/html/2510.25740v1#S1.E8 "In item (ii) ‣ Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")) is a member. For further details, see [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Chapter 5] and [[33](https://arxiv.org/html/2510.25740v1#bib.bib33), Chapter 4].

Let ϕ:I→J\phi:I\rightarrow J be a homeomorphism between real intervals. Following [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Definition 5.1.1], we define the quasiarithmetic mean on II generated by ϕ\phi be the family (Mϕ:Δn×In→I)n≥1(M\_{\phi}:\Delta\_{n}\times I^{n}\rightarrow I)\_{n\geq 1} where

|  |  |  |  |
| --- | --- | --- | --- |
| (3.10) |  | Mϕ​(𝝅,𝐫):=ϕ−1​(∑i=1nπi​ϕ​(ri)),(𝝅,𝐫)∈Δn×In.M\_{\phi}(\boldsymbol{\pi},\mathbf{r}):=\phi^{-1}\left(\sum\_{i=1}^{n}\pi\_{i}\phi(r\_{i})\right),\quad(\boldsymbol{\pi},\mathbf{r})\in\Delta\_{n}\times I^{n}. |  |

Taking ϕ=exp⁡(⋅):I=ℝ→J=(0,∞)\phi=\exp(\cdot):I=\mathbb{R}\rightarrow J=(0,\infty) recovers the exponential mean which is the first term of the excess growth rate γ​(𝝅,𝐫)\gamma(\boldsymbol{\pi},\mathbf{r}) expressed in terms of the log returns.

The following result, which characterizes the (unweighted) exponential mean, can be found in [[33](https://arxiv.org/html/2510.25740v1#bib.bib33), Theorem 4.15]:

###### Proposition 3.14 (Characterization of unweighted exponential mean).

Fix n≥1n\geq 1 and let 𝖬:ℝn→ℝ\mathsf{M}:\mathbb{R}^{n}\rightarrow\mathbb{R} be an unweighted quasiarithmetic mean, i.e., 𝖬​(⋅)=𝖬ϕ​(𝐞¯n,⋅)\mathsf{M}(\cdot)=\mathsf{M}\_{\phi}(\bar{\mathbf{e}}\_{n},\cdot) for some ϕ:(0,∞)→J\phi:(0,\infty)\rightarrow J. The following are equivalent:

* (i)

  𝖬\mathsf{M} is difference scale invariant, in the sense that

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.11) |  | 𝖬​(𝐫+s​𝟏)=𝖬​(𝐫)+s,s∈ℝ.\mathsf{M}(\mathbf{r}+s\mathbf{1})=\mathsf{M}(\mathbf{r})+s,\quad s\in\mathbb{R}. |  |
* (ii)

  𝖬​(⋅)=Mϕ​(𝐞¯n,⋅)\mathsf{M}(\cdot)=M\_{\phi}(\bar{\mathbf{e}}\_{n},\cdot) where ϕ​(x)=eα​x\phi(x)=e^{\alpha x} for some α∈ℝ∖{0}\alpha\in\mathbb{R}\setminus\{0\} or ϕ​(x)=x\phi(x)=x.

The property of difference scale invariance ([3.11](https://arxiv.org/html/2510.25740v1#S3.E11 "In item (i) ‣ Proposition 3.14 (Characterization of unweighted exponential mean). ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), when expressed in terms of 𝐑=e𝐫\mathbf{R}=e^{\mathbf{r}}, corresponds to the numéraire invariance of the excess growth rate; see the role of [(D3)](https://arxiv.org/html/2510.25740v1#S3.I7.i3 "item (D3) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") in Theorem [3.13](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem13 "Theorem 3.13 (Characterization II). ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")(ii). Also, see [[33](https://arxiv.org/html/2510.25740v1#bib.bib33), Theorem 4.10] which provides a list of properties which characterize the (unweighted) quasi-arithmetic mean (for some ϕ\phi) as a family (𝖬:ℝn→ℝ)n≥1(\mathsf{M}:\mathbb{R}^{n}\rightarrow\mathbb{R})\_{n\geq 1} of functions. Together, these two results characterize the (unweighted) exponential mean.

The theory of generalized means, or more generally the theory of aggregation functions (see [[33](https://arxiv.org/html/2510.25740v1#bib.bib33)]) and value (as in [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Chapter 7]), answers the question “what is the value of the whole in terms of its parts.” There, properties such as monotonicity (𝐱≤𝐲⇒𝖬​(𝐱)≤𝖬​(𝐲)\mathbf{x}\leq\mathbf{y}\Rightarrow\mathsf{M}(\mathbf{x})\leq\mathsf{M}(\mathbf{y})) are natural and crucial. On the other hand, the excess growth rate, as the difference between the exponential and arithmetic means (see ([1.8](https://arxiv.org/html/2510.25740v1#S1.E8 "In item (ii) ‣ Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate"))), focuses on how the returns differ from each other (so monotonicity no longer plays a role). This perspective distinguishes our study from that of generalized means.

###### Proof of Theorem [3.13](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem13 "Theorem 3.13 (Characterization II). ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

(i) Let gg be a gap function. Clearly, it satisfies [(D2)](https://arxiv.org/html/2510.25740v1#S3.I7.i2 "item (D2) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). From ([3.9](https://arxiv.org/html/2510.25740v1#S3.E9 "In 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), it is affine on any constant mean set Dm,𝐑D\_{m,\mathbf{R}} with

|  |  |  |
| --- | --- | --- |
|  | 𝐚=𝐚​(𝐑)=(−φ​(Ri))1≤i≤nandb=b​(m)=φ​(m).\mathbf{a}=\mathbf{a}(\mathbf{R})=(-\varphi(R\_{i}))\_{1\leq i\leq n}\quad\text{and}\quad b=b(m)=\varphi(m). |  |

Since gg is measurable, it is easy to see that φ\varphi is measurable. For example, for any 0<R¯<R¯0<\underaccent{\bar}{R}<\bar{R}, consider

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(R¯,R¯,1,…,1)∈(0,∞)n\mathbf{R}=\left(\underaccent{\bar}{R},\bar{R},1,\ldots,1\right)\in(0,\infty)^{n} |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝝅t=(1−t,t,0,…,0)∈𝒟n(⋅∣𝐑)=Δn,t∈[0,1].\boldsymbol{\pi}\_{t}=(1-t,t,0,\ldots,0)\in\mathcal{D}\_{n}(\cdot\mid\mathbf{R})=\Delta\_{n},\quad t\in[0,1]. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | g​(𝝅t,𝐑)=φ​((1−t)​R¯+t​R¯)−(1−t)​φ​(R¯)−t​φ​(R¯)g(\boldsymbol{\pi}\_{t},\mathbf{R})=\varphi((1-t)\underaccent{\bar}{R}+t\bar{R})-(1-t)\varphi(\underaccent{\bar}{R})-t\varphi(\bar{R}) |  |

is measurable in tt. It follows that φ\varphi is measurable on [R¯,R¯][\underaccent{\bar}{R},\bar{R}]. Since R¯,R\underaccent{\bar}{R},R are arbitrary, we have that φ\varphi is measurable on (0,∞)(0,\infty). Hence gg also satisfies [(D4)](https://arxiv.org/html/2510.25740v1#S3.I7.i4 "item (D4) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

Next, suppose that gg satisfies [(D2)](https://arxiv.org/html/2510.25740v1#S3.I7.i2 "item (D2) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and [(D4)](https://arxiv.org/html/2510.25740v1#S3.I7.i4 "item (D4) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). Then, there exist measurable functions 𝐚:ℝn→ℝn\mathbf{a}:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n} and b:(0,∞)→ℝb:(0,\infty)\rightarrow\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | g​(𝝅,𝐑)=⟨𝐚​(𝐑),𝝅⟩+b​(⟨𝝅,𝐑⟩),(𝝅,𝐑)∈𝒟n.g(\boldsymbol{\pi},\mathbf{R})=\langle\mathbf{a}(\mathbf{R}),\boldsymbol{\pi}\rangle+b(\langle\boldsymbol{\pi},\mathbf{R}\rangle),\quad(\boldsymbol{\pi},\mathbf{R})\in\mathcal{D}\_{n}. |  |

Define φ=b\varphi=b which is measurable. Letting 𝝅=𝐞i\boldsymbol{\pi}=\mathbf{e}\_{i} be the ii-basis vector, we have

|  |  |  |
| --- | --- | --- |
|  | 0=g​(𝝅,𝐑)=ai​(𝐑)+b​(⟨𝝅,𝐑⟩)=ai​(𝐑)+φ​(Ri),0=g(\boldsymbol{\pi},\mathbf{R})=a\_{i}(\mathbf{R})+b(\langle\boldsymbol{\pi},\mathbf{R}\rangle)=a\_{i}(\mathbf{R})+\varphi(R\_{i}), |  |

where the first equality holds by [(D2)](https://arxiv.org/html/2510.25740v1#S3.I7.i2 "item (D2) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). It follows that 𝐚​(𝐑)=(−φ​(Ri))1≤i≤n\mathbf{a}(\mathbf{R})=(-\varphi(R\_{i}))\_{1\leq i\leq n}, and we have

|  |  |  |
| --- | --- | --- |
|  | g​(𝝅,𝐑)=φ​(⟨𝝅,𝐑⟩)−∑i=1nπi​φ​(Ri)=φ​(∑i∈supp⁡(𝝅)πi​Ri)−∑i∈supp⁡(𝝅)πi​φ​(Ri).g(\boldsymbol{\pi},\mathbf{R})=\varphi(\langle\boldsymbol{\pi},\mathbf{R}\rangle)-\sum\_{i=1}^{n}\pi\_{i}\varphi(R\_{i})=\varphi\left(\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}R\_{i}\right)-\sum\_{i\in\operatorname{supp}(\boldsymbol{\pi})}\pi\_{i}\varphi(R\_{i}). |  |

Thus, gg is a gap function whose generator is measurable.

Given that gg is a gap function, it is immediate to see that its generator φ\varphi is concave if and only if 𝝅↦g​(𝝅,𝐑)\boldsymbol{\pi}\mapsto g(\boldsymbol{\pi},\mathbf{R}) is concave on 𝒟n(⋅∣𝐑)\mathcal{D}\_{n}(\cdot\mid\mathbf{R}) for every 𝐑∈[0,∞)n∖{𝟎}\mathbf{R}\in[0,\infty)^{n}\setminus\{\mathbf{0}\}.

(ii) Suppose g=c​Γg=c\Gamma for some c∈ℝc\in\mathbb{R}, so that gg is a gap function with generator φ=c​log\varphi=c\log. From (i), gg satisfies [(D2)](https://arxiv.org/html/2510.25740v1#S3.I7.i2 "item (D2) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and [(D4)](https://arxiv.org/html/2510.25740v1#S3.I7.i4 "item (D4) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). That gg satisfies [(D3)](https://arxiv.org/html/2510.25740v1#S3.I7.i3 "item (D3) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") is a consequence of Proposition [2.3](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem3 "Proposition 2.3 (Numéraire invariance). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") (numéraire invariance).

Now, suppose gg satisfies [(D2)](https://arxiv.org/html/2510.25740v1#S3.I7.i2 "item (D2) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(D4)](https://arxiv.org/html/2510.25740v1#S3.I7.i4 "item (D4) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). From (i), gg is a gap function with a measurable generator φ\varphi. We aim to use [(D3)](https://arxiv.org/html/2510.25740v1#S3.I7.i3 "item (D3) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") to show that φ\varphi is equal to c​logc\log plus an affine function, for some c∈ℝc\in\mathbb{R}. If so, we have g=c​Γg=c\Gamma.

For α>0\alpha>0, consider the function kα:(0,∞)→ℝk\_{\alpha}:(0,\infty)\rightarrow\mathbb{R} defined by

|  |  |  |
| --- | --- | --- |
|  | kα​(u):=φ​(α​u)−φ​(u),u∈(0,∞).k\_{\alpha}(u):=\varphi(\alpha u)-\varphi(u),\quad u\in(0,\infty). |  |

Also define h:(0,∞)→ℝh:(0,\infty)\rightarrow\mathbb{R} by

|  |  |  |
| --- | --- | --- |
|  | h​(α):=φ​(α)−φ​(1)=kα​(1).h(\alpha):=\varphi(\alpha)-\varphi(1)=k\_{\alpha}(1). |  |

Note that h​(1)=0h(1)=0. Our strategy is to derive functional equations for kαk\_{\alpha} and hh.

Step 1: kαk\_{\alpha} is affine. Fix 0<u<v0<u<v. For t∈[0,1]t\in[0,1], consider

|  |  |  |
| --- | --- | --- |
|  | 𝝅=(1−t,t,0,…,0)∈Δnand𝐑=(u,v,1,…,1)∈(0,∞)n.\boldsymbol{\pi}=(1-t,t,0,\ldots,0)\in\Delta\_{n}\quad\text{and}\quad\mathbf{R}=(u,v,1,\ldots,1)\in(0,\infty)^{n}. |  |

By [(D3)](https://arxiv.org/html/2510.25740v1#S3.I7.i3 "item (D3) ‣ Assumption 3.12. ‣ 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), which is the homogeneity property g​(𝝅,α​𝐑)=g​(𝝅,𝐑)g(\boldsymbol{\pi},\alpha\mathbf{R})=g(\boldsymbol{\pi},\mathbf{R}), we have

|  |  |  |
| --- | --- | --- |
|  | φ​((1−t)​α​u+t​α​v)−(1−t)​φ​(α​u)−t​φ​(α​v)=φ​((1−t)​u+t​v)−(1−t)​φ​(u)−t​φ​(v).\varphi\left((1-t)\alpha u+t\alpha v\right)-(1-t)\varphi(\alpha u)-t\varphi(\alpha v)=\varphi((1-t)u+tv)-(1-t)\varphi(u)-t\varphi(v). |  |

Writing this in terms of kαk\_{\alpha} gives

|  |  |  |
| --- | --- | --- |
|  | kα​((1−t)​u+t​v)=(1−t)​kα​(u)+t​kφ​(v).k\_{\alpha}((1-t)u+tv)=(1-t)k\_{\alpha}(u)+tk\_{\varphi}(v). |  |

Thus, kαk\_{\alpha} is affine on (0,∞)(0,\infty), and there exist unique aα,bα∈ℝa\_{\alpha},b\_{\alpha}\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | kα​(u)=aα​u+bα,u∈(0,∞).k\_{\alpha}(u)=a\_{\alpha}u+b\_{\alpha},\quad u\in(0,\infty). |  |

Step 2: aαa\_{\alpha} is affine in α\alpha. Observe that

|  |  |  |
| --- | --- | --- |
|  | kα​(u)=φ​(α​u)−φ​(u)=[h​(α​u)+φ​(1)]−[h​(u)+φ​(1)]=h​(α​u)−h​(u).k\_{\alpha}(u)=\varphi(\alpha u)-\varphi(u)=[h(\alpha u)+\varphi(1)]-[h(u)+\varphi(1)]=h(\alpha u)-h(u). |  |

On the other hand, we have

|  |  |  |
| --- | --- | --- |
|  | kα​(1)=aα+bα=φ​(α)−φ​(1)=h​(α).k\_{\alpha}(1)=a\_{\alpha}+b\_{\alpha}=\varphi(\alpha)-\varphi(1)=h(\alpha). |  |

And so,

|  |  |  |
| --- | --- | --- |
|  | h​(α​u)=h​(u)+h​(α)+aα​(u−1),α,u∈(0,∞).h(\alpha u)=h(u)+h(\alpha)+a\_{\alpha}(u-1),\quad\alpha,u\in(0,\infty). |  |

Swapping α\alpha and uu gives

|  |  |  |
| --- | --- | --- |
|  | h​(u​α)=h​(α)+h​(u)=au​(α−1).h(u\alpha)=h(\alpha)+h(u)=a\_{u}(\alpha-1). |  |

Equating the two expression gives

|  |  |  |
| --- | --- | --- |
|  | 0=aα​(u−1)−au​(α−1).0=a\_{\alpha}(u-1)-a\_{u}(\alpha-1). |  |

Thus, for any α,u∈(0,∞)∖{1}\alpha,u\in(0,\infty)\setminus\{1\} we have

|  |  |  |
| --- | --- | --- |
|  | aαα−1=auu−1.\frac{a\_{\alpha}}{\alpha-1}=\frac{a\_{u}}{u-1}. |  |

We conclude that there is a constant r∈ℝr\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | aα=r​(α−1).a\_{\alpha}=r(\alpha-1). |  |

Step 3: Cauchy’s functional equation for h~​(u):=h​(u)−r​u+r\tilde{h}(u):=h(u)-ru+r. From Step 2, we have

|  |  |  |
| --- | --- | --- |
|  | h​(α​u)=h​(u)+h​(α)+r​(α−1)​(u−1),α,u∈(0,∞).h(\alpha u)=h(u)+h(\alpha)+r(\alpha-1)(u-1),\quad\alpha,u\in(0,\infty). |  |

Rearranging yields

|  |  |  |
| --- | --- | --- |
|  | (h​(α​u)−r​α​u+r)=(h​(α)−r​α+r)+(h​(u)−r​u+r).(h(\alpha u)-r\alpha u+r)=(h(\alpha)-r\alpha+r)+(h(u)-ru+r). |  |

Letting h~​(u)=h​(u)−r​u+r\tilde{h}(u)=h(u)-ru+r, we have the functional equation

|  |  |  |  |
| --- | --- | --- | --- |
| (3.12) |  | h~​(α​u)=h~​(α)+h~​(u),α,u∈(0,∞).\tilde{h}(\alpha u)=\tilde{h}(\alpha)+\tilde{h}(u),\quad\alpha,u\in(0,\infty). |  |

If we make the exponential change of variables α=ex\alpha=e^{x}, u=eyu=e^{y}, x,y∈ℝx,y\in\mathbb{R}, and let ψ​(x):=h~​(ex)\psi(x):=\tilde{h}(e^{x}), then ([3.12](https://arxiv.org/html/2510.25740v1#S3.E12 "In 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) is equivalent to Cauchy’s functional equation

|  |  |  |  |
| --- | --- | --- | --- |
| (3.13) |  | ψ​(x+y)=ψ​(x)+ψ​(y),x,y∈ℝ.\psi(x+y)=\psi(x)+\psi(y),\quad x,y\in\mathbb{R}. |  |

Since ψ\psi is measurable, there exists c∈ℝc\in\mathbb{R} such that ([3.13](https://arxiv.org/html/2510.25740v1#S3.E13 "In 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) ψ​(x)≡c​x\psi(x)\equiv cx, see [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Theorem 1.1.8]. Unwinding the transformations, we have

|  |  |  |
| --- | --- | --- |
|  | h~​(u)=c​log⁡u,u>0.\tilde{h}(u)=c\log u,\quad u>0. |  |

(Alternatively, we may apply directly [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Corollary 1.1.11] to ([3.12](https://arxiv.org/html/2510.25740v1#S3.E12 "In 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")).) It follows that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.14) |  | φ​(u)=h​(u)+φ​(1)=h~​(u)+r​u−r+φ​(1)=c​log⁡u+(φ​(1)−r)+r​u.\varphi(u)=h(u)+\varphi(1)=\tilde{h}(u)+ru-r+\varphi(1)=c\log u+(\varphi(1)-r)+ru. |  |

Thus, φ\varphi is equal to c​log⁡uc\log u plus an affine function. Finally, we note that φ\varphi given by ([3.14](https://arxiv.org/html/2510.25740v1#S3.E14 "In 3.2. Via Jensen gap ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) is concave if and only if c≥0c\geq 0.
∎

### 3.3. Via logarithmic divergence and cross-entropy

In this subsection, we consider the excess growth rate as the divergence Γ𝝅​(𝐘∥𝐗)\Gamma\_{\boldsymbol{\pi}}(\mathbf{Y}\;\|\;\mathbf{X}) (see Definition [1.3](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem3 "Definition 1.3 (Excess growth rate as a divergence). ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")). We fix n≥2n\geq 2 and, for simplicity, restrict 𝝅∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ} so that 𝐗,𝐘∈(0,∞)n\mathbf{X},\mathbf{Y}\in(0,\infty)^{n}. By numéraire invariance, we may replace 𝐗\mathbf{X} and 𝐘\mathbf{Y} by 𝐩=𝒞​[𝐗]\mathbf{p}=\mathcal{C}[\mathbf{X}] and 𝐪=𝒞​[𝐘]\mathbf{q}=\mathcal{C}[\mathbf{Y}] respectively, and hence regard Γ𝝅(⋅∥⋅)\Gamma\_{\boldsymbol{\pi}}(\cdot\;\|\;\cdot) as a divergence on Δn∘\Delta\_{n}^{\circ}. We characterize the excess growth rate as the unique logarithmic divergence (Definition [3.17](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem17 "Definition 3.17 (Logarithmic divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) which is perturbation invariant in the sense of ([3.22](https://arxiv.org/html/2510.25740v1#S3.E22 "In item (i) ‣ Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) below. In fact, our result can be equivalently stated as a characterization theorem for the cross-entropy.

To motivate our result, we first prove a characterization of the Mahalanobis distance ([2.29](https://arxiv.org/html/2510.25740v1#S2.E29 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")).121212This result is probably known by experts but we are unable to find an exact reference in the literature. The closest result we could locate, proved in [[46](https://arxiv.org/html/2510.25740v1#bib.bib46)], states that the squared Mahalanobis distance is the only Bregman divergence on ℝn\mathbb{R}^{n} which is symmetric in the sense that 𝐁ϕ​(𝐲∥𝐱)=𝐁ϕ​(𝐱∥𝐲)\mathbf{B}\_{\phi}(\mathbf{y}\;\|\;\mathbf{x})=\mathbf{B}\_{\phi}(\mathbf{x}\;\|\;\mathbf{y}) for all 𝐱,𝐲\mathbf{x},\mathbf{y}.  Recall that the Bregman divergence [[13](https://arxiv.org/html/2510.25740v1#bib.bib13)] of a differentiable convex function ϕ\phi on a convex subset of ℝn\mathbb{R}^{n} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.15) |  | Bϕ​(𝐲∥𝐱):=ϕ​(𝐲)−ϕ​(𝐱)−∇𝐲−𝐱ϕ​(𝐱).B\_{\phi}(\mathbf{y}\;\|\;\mathbf{x}):=\phi(\mathbf{y})-\phi(\mathbf{x})-\nabla\_{\mathbf{y}-\mathbf{x}}\phi(\mathbf{x}). |  |

When ϕ\phi is strictly convex, we have Bϕ​(𝐲∥𝐱)=0B\_{\phi}(\mathbf{y}\;\|\;\mathbf{x})=0 only if 𝐱=𝐲\mathbf{x}=\mathbf{y}. If ϕ:ℝn→ℝ\phi:\mathbb{R}^{n}\rightarrow\mathbb{R} is a quadratic function of the form ϕ​(𝐱)=12​𝐱⊤​A​𝐱+𝐛⊤​𝐱+𝐜\phi(\mathbf{x})=\frac{1}{2}\mathbf{x}^{\top}A\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+\mathbf{c} where AA is an n×nn\times n positive semidefinite matrix and 𝐛,𝐜∈ℝn\mathbf{b},\mathbf{c}\in\mathbb{R}^{n} (we regard 𝐱\mathbf{x} as a column vector), then

|  |  |  |
| --- | --- | --- |
|  | Bϕ​(𝐲∥𝐱)=(𝐲−𝐱)⊤​A​(𝐲−𝐱),𝐱,𝐲∈ℝn,B\_{\phi}(\mathbf{y}\;\|\;\mathbf{x})=(\mathbf{y}-\mathbf{x})^{\top}A(\mathbf{y}-\mathbf{x}),\quad\mathbf{x},\mathbf{y}\in\mathbb{R}^{n}, |  |

is a squared Mahalanobis distance (provided AA is strictly positive definite).

###### Theorem 3.15 (Characterization of squared Mahalanobis distance as a Bregman divergence).

Let ϕ:ℝn→ℝ\phi:\mathbb{R}^{n}\rightarrow\mathbb{R} be C2C^{2} (twice continuously differentiable) and strictly convex.131313It is possible to assume only that ϕ\phi is C1C^{1}. We assume C2C^{2} to shorten the proof. The following are equivalent:

* (i)

  Bϕ(⋅∥⋅)B\_{\phi}(\cdot\;\|\;\cdot) is invariant under translation, in the sense that

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.16) |  | Bϕ​(𝐲+𝐳∥𝐱+𝐳)=Bϕ​(𝐲∥𝐱),𝐱,𝐲,𝐳∈ℝn.B\_{\phi}(\mathbf{y}+\mathbf{z}\;\|\;\mathbf{x}+\mathbf{z})=B\_{\phi}(\mathbf{y}\;\|\;\mathbf{x}),\quad\mathbf{x},\mathbf{y},\mathbf{z}\in\mathbb{R}^{n}. |  |
* (ii)

  ϕ​(𝐱)=12​𝐱⊤​A​𝐱+𝐛⊤​𝐱+𝐜\phi(\mathbf{x})=\frac{1}{2}\mathbf{x}^{\top}A\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+\mathbf{c} for some strictly positive definite matrix A∈ℝn×nA\in\mathbb{R}^{n\times n} and 𝐛,𝐜∈ℝn\mathbf{b},\mathbf{c}\in\mathbb{R}^{n}.

In particular, any translation invariant Bregman divergence is a squared Mahalanobis distance.

###### Proof.

It is clear that (ii) implies (i). Assume ϕ\phi satisfies (i). Expanding and rearranging ([3.16](https://arxiv.org/html/2510.25740v1#S3.E16 "In item (i) ‣ Theorem 3.15 (Characterization of squared Mahalanobis distance as a Bregman divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), we have, for 𝐱,𝐲,𝐳∈ℝn\mathbf{x},\mathbf{y},\mathbf{z}\in\mathbb{R}^{n},

|  |  |  |
| --- | --- | --- |
|  | (ϕ​(𝐲+𝐳)−ϕ​(𝐲))−(ϕ​(𝐱+𝐳)−ϕ​(𝐱))=⟨∇ϕ​(𝐱+𝐳)−∇ϕ​(𝐱),𝐲−𝐱⟩.(\phi(\mathbf{y}+\mathbf{z})-\phi(\mathbf{y}))-(\phi(\mathbf{x}+\mathbf{z})-\phi(\mathbf{x}))=\langle\nabla\phi(\mathbf{x}+\mathbf{z})-\nabla\phi(\mathbf{x}),\mathbf{y}-\mathbf{x}\rangle. |  |

Differentiating with respect to 𝐲\mathbf{y} gives

|  |  |  |
| --- | --- | --- |
|  | ϕ​(𝐲+𝐳)−ϕ​(𝐲)=ϕ​(𝐱+𝐳)−∇ϕ​(𝐱),\phi(\mathbf{y}+\mathbf{z})-\phi(\mathbf{y})=\phi(\mathbf{x}+\mathbf{z})-\nabla\phi(\mathbf{x}), |  |

which is independent of 𝐲\mathbf{y}. Letting 𝐳=t​𝐯\mathbf{z}=t\mathbf{v} for 𝐯∈ℝn\mathbf{v}\in\mathbb{R}^{n}, dividing both sides by t≠0t\neq 0 and letting t→0t\rightarrow 0 shows that the Hessian ∇2ϕ​(𝐲)\nabla^{2}\phi(\mathbf{y}) is a constant matrix AA. It follows that ϕ\phi is quadratic. Since ϕ\phi is strictly convex, AA is strictly positive definite. Hence (ii) holds and the theorem is proved.
∎

###### Remark 3.16 (Characterization of relative entropy as a Bregman divergence).

The negative Shannon entropy ϕ​(𝐩)=−H​(𝐩)\phi(\mathbf{p})=-H(\mathbf{p}) is differentiable and strictly convex in 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ}. It is well known (see e.g. [[4](https://arxiv.org/html/2510.25740v1#bib.bib4), Chapter 1]) that the induced Bregman divergence is the relative entropy:

|  |  |  |
| --- | --- | --- |
|  | B−H​(𝐩∥𝐪)=H​(𝐩∥𝐪),𝐩,𝐪∈Δn∘.B\_{-H}(\mathbf{p}\;\|\;\mathbf{q})=H(\mathbf{p}\;\|\;\mathbf{q}),\quad\mathbf{p},\mathbf{q}\in\Delta\_{n}^{\circ}. |  |

We are unaware of a characterization of the relative entropy (within the family of Bregman divergences) which is a direct analogy of Theorem [3.15](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem15 "Theorem 3.15 (Characterization of squared Mahalanobis distance as a Bregman divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") or Theorem [3.20](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem20 "Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") below. What we could find is the following result by Amari [[3](https://arxiv.org/html/2510.25740v1#bib.bib3), Corollary]: the relative entropy is the unique Bregman divergence which is also an ff-divergence.

Our third and last characterization of the excess growth rate is analogous to Theorem [3.15](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem15 "Theorem 3.15 (Characterization of squared Mahalanobis distance as a Bregman divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), except that a different kind of divergence is required. By an exponentially concave function on Δn∘\Delta\_{n}^{\circ}, we mean a function φ:Δn∘→ℝ\varphi:\Delta\_{n}^{\circ}\rightarrow\mathbb{R} such that Φ=eφ\Phi=e^{\varphi} is concave on Δn∘\Delta\_{n}^{\circ}. Clearly, if φ\varphi is exponentially concave then φ\varphi itself is concave. The following definition is taken from [[49](https://arxiv.org/html/2510.25740v1#bib.bib49)].

###### Definition 3.17 (Logarithmic divergence).

Let φ\varphi be differentiable and exponentially concave on Δn∘\Delta\_{n}^{\circ}. Its logarithmic divergence is the function Lφ(⋅∥⋅):Δn∘×Δn∘→ℝ+L\_{\varphi}(\cdot\;\|\;\cdot):\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}\rightarrow\mathbb{R}\_{+} defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.17) |  | Lφ​(𝐪∥𝐩):=log⁡(1+∇𝐪−𝐩φ​(𝐩))−(φ​(𝐪)−φ​(𝐩)),(𝐪,𝐩)∈Δn∘×Δn∘.L\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p}):=\log\left(1+\nabla\_{\mathbf{q}-\mathbf{p}}\varphi(\mathbf{p})\right)-\left(\varphi(\mathbf{q})-\varphi(\mathbf{p})\right),\quad(\mathbf{q},\mathbf{p})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ}. |  |

The logarithmic divergence is a logarithmic generalization of the Bregman divergence ([3.15](https://arxiv.org/html/2510.25740v1#S3.E15 "In 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")). To illustrate this point and to see that the logarithmic divergence is well defined, let φ\varphi be exponentially concave and consider Φ=eφ\Phi=e^{\varphi} which is a positive concave function on Δn∘\Delta\_{n}^{\circ}. For 𝐩,𝐪∈Δn∘\mathbf{p},\mathbf{q}\in\Delta\_{n}^{\circ}, concavity of Φ\Phi implies that

|  |  |  |
| --- | --- | --- |
|  | Φ​(𝐩)+∇𝐪−𝐩Φ​(𝐩)≥Φ​(𝐪).\Phi(\mathbf{p})+\nabla\_{\mathbf{q}-\mathbf{p}}\Phi(\mathbf{p})\geq\Phi(\mathbf{q}). |  |

Dividing both sides by Φ​(𝐩)>0\Phi(\mathbf{p})>0, we have

|  |  |  |
| --- | --- | --- |
|  | 1+∇𝐪−𝐩φ​(𝐩)≥Φ​(𝐪)Φ​(𝐩)=eφ​(𝐪)−φ​(𝐩)>0.1+\nabla\_{\mathbf{q}-\mathbf{p}}\varphi(\mathbf{p})\geq\frac{\Phi(\mathbf{q})}{\Phi(\mathbf{p})}=e^{\varphi(\mathbf{q})-\varphi(\mathbf{p})}>0. |  |

We obtain the logarithmic divergence by taking the logarithm and then the difference. To wit, exponential concavity of φ\varphi leads to a logarithmic first-order approximation based at 𝐩\mathbf{p}; it is more accurate than the usual linear approximation since log⁡(1+∇𝐪−𝐩φ​(𝐩))≤∇𝐪−𝐩φ​(𝐩)\log(1+\nabla\_{\mathbf{q}-\mathbf{p}}\varphi(\mathbf{p}))\leq\nabla\_{\mathbf{q}-\mathbf{p}}\varphi(\mathbf{p}). See [[49](https://arxiv.org/html/2510.25740v1#bib.bib49), [50](https://arxiv.org/html/2510.25740v1#bib.bib50), [63](https://arxiv.org/html/2510.25740v1#bib.bib63), [64](https://arxiv.org/html/2510.25740v1#bib.bib64), [65](https://arxiv.org/html/2510.25740v1#bib.bib65), [66](https://arxiv.org/html/2510.25740v1#bib.bib66)] for in-depth studies of the logarithmic divergence motivated by portfolio theory and information geometry [[4](https://arxiv.org/html/2510.25740v1#bib.bib4)], as well as further extensions.

Following [[49](https://arxiv.org/html/2510.25740v1#bib.bib49)] (also see [[26](https://arxiv.org/html/2510.25740v1#bib.bib26), Example 3.1.6]),the excess growth rate can be expressed as a logarithmic divergence. Recall that the cross-entropy H×​(𝐩∥𝐪)H^{\times}(\mathbf{p}\;\|\;\mathbf{q}) is defined for 𝐩,𝐪∈Δn∘\mathbf{p},\mathbf{q}\in\Delta\_{n}^{\circ} by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.18) |  | H×​(𝐩∥𝐪):=−∑i=1npi​log⁡qi.H^{\times}(\mathbf{p}\;\|\;\mathbf{q}):=-\sum\_{i=1}^{n}p\_{i}\log q\_{i}. |  |

###### Proposition 3.18 (Excess growth rate as a logarithmic divergence).

For 𝛑=(π1,…,πn)∈Δn∘\boldsymbol{\pi}=(\pi\_{1},\ldots,\pi\_{n})\in\Delta\_{n}^{\circ}, the function φ​(⋅)=−H×​(𝛑∥⋅)\varphi(\cdot)=-H^{\times}(\boldsymbol{\pi}\;\|\;\cdot) is exponentially concave on Δn∘\Delta\_{n}^{\circ}. Moreover, its logarithmic divergence is the excess growth rate:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.19) |  | Lφ​(𝐪∥𝐩)=Γ𝝅​(𝐪∥𝐩),𝐩,𝐪∈Δn∘.L\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p})=\Gamma\_{\boldsymbol{\pi}}(\mathbf{q}\;\|\;\mathbf{p}),\quad\mathbf{p},\mathbf{q}\in\Delta\_{n}^{\circ}. |  |

###### Proof.

For completeness, we provide a sketch of the proof. Consider φ​(𝐩)=−H×​(𝝅∥𝐩)=∑i=1nπi​log⁡pi\varphi(\mathbf{p})=-H^{\times}(\boldsymbol{\pi}\;\|\;\mathbf{p})=\sum\_{i=1}^{n}\pi\_{i}\log p\_{i}. Note that Φ​(𝐩)=eφ​(𝐩)=∏i=1npiπi\Phi(\mathbf{p})=e^{\varphi(\mathbf{p})}=\prod\_{i=1}^{n}p\_{i}^{\pi\_{i}} is the weighted geometric mean that is concave in 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ}. Hence φ\varphi is exponentially concave. A direct computation shows that

|  |  |  |
| --- | --- | --- |
|  | 1+∇𝐪−𝐩φ​(𝐩)=∑i=1nπi​qipi.1+\nabla\_{\mathbf{q}-\mathbf{p}}\varphi(\mathbf{p})=\sum\_{i=1}^{n}\pi\_{i}\frac{q\_{i}}{p\_{i}}. |  |

It follows from ([3.17](https://arxiv.org/html/2510.25740v1#S3.E17 "In Definition 3.17 (Logarithmic divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) that

|  |  |  |
| --- | --- | --- |
|  | Lφ​(𝐪∥𝐩)=log⁡(∑i=1nπi​qipi)−∑i=1nπi​log⁡qipi=Γ𝝅​(𝐪∥𝐩).∎\begin{split}L\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p})&=\log\left(\sum\_{i=1}^{n}\pi\_{i}\frac{q\_{i}}{p\_{i}}\right)-\sum\_{i=1}^{n}\pi\_{i}\log\frac{q\_{i}}{p\_{i}}=\Gamma\_{\boldsymbol{\pi}}(\mathbf{q}\;\|\;\mathbf{p}).\qed\end{split} |  |

We give another fundamental example of logarithmic divergence that can be expressed in terms of information-theoretic quantities.

###### Example 3.19 (Rényi divergence).

Let λ∈(0,1)\lambda\in(0,1) and α=1λ∈(1,∞)\alpha=\frac{1}{\lambda}\in(1,\infty). Consider

|  |  |  |
| --- | --- | --- |
|  | φ​(𝐩)=(α−1)​Hα​(λ⊗𝐩),𝐩∈Δn∘,\varphi(\mathbf{p})=(\alpha-1)H\_{\alpha}(\lambda\otimes\mathbf{p}),\quad\mathbf{p}\in\Delta\_{n}^{\circ}, |  |

where Hα​(𝐩):=11−α​log⁡(∑i=1nxiα)H\_{\alpha}(\mathbf{p}):=\frac{1}{1-\alpha}\log\left(\sum\_{i=1}^{n}x\_{i}^{\alpha}\right) is the Rényi entropy of order α\alpha. Then φ\varphi is exponentially concave and its logarithmic divergence is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.20) |  | Lφ​(𝐪∥𝐩)=(α−1)​Hα​(λ⊗𝐪∥λ⊗𝐩),L\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p})=(\alpha-1)H\_{\alpha}(\lambda\otimes\mathbf{q}\;\|\;\lambda\otimes\mathbf{p}), |  |

where Hα​(𝐩∥𝐪)=1α−1​log⁡(∑i=1npiα​qi1−α)H\_{\alpha}(\mathbf{p}\;\|\;\mathbf{q})=\frac{1}{\alpha-1}\log\left(\sum\_{i=1}^{n}p\_{i}^{\alpha}q\_{i}^{1-\alpha}\right) is the Rényi divergence of order α\alpha (this is a special case of ([2.31](https://arxiv.org/html/2510.25740v1#S2.E31 "In 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"))). The details can be found in [[64](https://arxiv.org/html/2510.25740v1#bib.bib64), Proposition 2]. General relationships between the logarithmic divergence and Rényi entropy/divergence are developed in [[63](https://arxiv.org/html/2510.25740v1#bib.bib63), [66](https://arxiv.org/html/2510.25740v1#bib.bib66)].

We set out to characterize the excess growth rate within the family of logarithmic divergences. To simplify the proof, we impose some regularity conditions on φ\varphi. We say that an exponentially concave function φ:Δn∘→ℝ\varphi:\Delta\_{n}^{\circ}\rightarrow\mathbb{R} is regular if it is C4C^{4} on Δn∘\Delta\_{n}^{\circ} and, for each 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ} and 𝐯∈ℝn∖{0}\mathbf{v}\in\mathbb{R}^{n}\setminus\{0\} with v1+⋯+vn=0v\_{1}+\cdots+v\_{n}=0 (that is, 𝐯\mathbf{v} is tangent to Δn∘\Delta\_{n}^{\circ}), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.21) |  | d2d​t2|t=0​Φ​(𝐩+t​𝐯)<0,where ​Φ=eφ.\left.\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\right|\_{t=0}\Phi(\mathbf{p}+t\mathbf{v})<0,\quad\text{where }\Phi=e^{\varphi}. |  |

In particular, ([3.21](https://arxiv.org/html/2510.25740v1#S3.E21 "In 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) implies that Φ\Phi is strictly concave.

###### Theorem 3.20 (Characterization III).

Let φ:Δn∘→ℝ\varphi:\Delta\_{n}^{\circ}\rightarrow\mathbb{R} be regular exponentially concave. The following are equivalent:

* (i)

  Lφ(⋅∥⋅)L\_{\varphi}(\cdot\;\|\;\cdot) is invariant under perturbations, in the sense that

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.22) |  | Lφ​(𝐪⊕𝐡∥𝐩⊕𝐡)=Lφ​(𝐪∥𝐩)for ​𝐩,𝐪,𝐡∈Δn∘,L\_{\varphi}(\mathbf{q}\oplus\mathbf{h}\;\|\;\mathbf{p}\oplus\mathbf{h})=L\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p})\quad\text{for }\mathbf{p},\mathbf{q},\mathbf{h}\in\Delta\_{n}^{\circ}, |  |
* (ii)

  φ=−H×​(𝝅∥⋅)+c\varphi=-H^{\times}(\boldsymbol{\pi}\;\|\;\cdot)+c for some 𝝅∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ} and c∈ℝc\in\mathbb{R}.

In particular, any perturbation invariant logarithmic divergence is an excess growth rate.

![Refer to caption](x2.png)


Figure 2. A path 𝐩​(t)\mathbf{p}(t) (in black) on Δn∘\Delta\_{n}^{\circ} and its perturbation 𝐪​(t)=𝐩​(t)⊕𝐡\mathbf{q}(t)=\mathbf{p}(t)\oplus\mathbf{h} (in grey).

We illustrate the perturbation invariance property ([3.22](https://arxiv.org/html/2510.25740v1#S3.E22 "In item (i) ‣ Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) in Figure [2](https://arxiv.org/html/2510.25740v1#S3.F2 "Figure 2 ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"). Consider a simulated path (𝐩​(t))t=0T(\mathbf{p}(t))\_{t=0}^{T} in Δn∘\Delta\_{n}^{\circ}.141414Here n=3n=3, T=500T=500 and the path is generated in terms of a 33-dimensional Brownian bridge. For some 𝐡∈Δn∘\mathbf{h}\in\Delta\_{n}^{\circ}, let 𝐪​(t)=𝐩​(t)⊕𝐡\mathbf{q}(t)=\mathbf{p}(t)\oplus\mathbf{h} be a perturbed path. The perturbation appears to be non-linear in the figure, but it is an ordinary translation in the Aitchison vector space (Δn∘,⊕,⊗)(\Delta\_{n}^{\circ},\oplus,\otimes). Now, ([3.22](https://arxiv.org/html/2510.25740v1#S3.E22 "In item (i) ‣ Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) implies that

|  |  |  |
| --- | --- | --- |
|  | ∑t=0TLφ​(𝐩​(t+1)∥𝐩​(t))=∑t=0TLφ​(𝐪​(t+1)∥𝐪​(t)).\sum\_{t=0}^{T}L\_{\varphi}(\mathbf{p}(t+1)\;\|\;\mathbf{p}(t))=\sum\_{t=0}^{T}L\_{\varphi}(\mathbf{q}(t+1)\;\|\;\mathbf{q}(t)). |  |

That is, the two paths have the same cumulative (relative) volatility. Perturbation invariance is closely related to numéraire invariance. Observe that ([3.22](https://arxiv.org/html/2510.25740v1#S3.E22 "In item (i) ‣ Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) is equivalent to the identity

|  |  |  |  |
| --- | --- | --- | --- |
| (3.23) |  | Lφ​(𝐩⊕𝐫∥𝐩)=Lφ​(𝐪⊕𝐫∥𝐪),𝐩,𝐪,𝐫∈Δn∘.L\_{\varphi}(\mathbf{p}\oplus\mathbf{r}\;\|\;\mathbf{p})=L\_{\varphi}(\mathbf{q}\oplus\mathbf{r}\;\|\;\mathbf{q}),\quad\mathbf{p},\mathbf{q},\mathbf{r}\in\Delta\_{n}^{\circ}. |  |

(To see this, in ([3.22](https://arxiv.org/html/2510.25740v1#S3.E22 "In item (i) ‣ Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) replace 𝐪\mathbf{q} by 𝐩⊕𝐫\mathbf{p}\oplus\mathbf{r} and 𝐡\mathbf{h} by 𝐪⊖𝐩\mathbf{q}\ominus\mathbf{p}.) In ([3.23](https://arxiv.org/html/2510.25740v1#S3.E23 "In 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")), we regard 𝐫=𝒞​[𝐑]\mathbf{r}=\mathcal{C}[\mathbf{R}] as the (normalized) gross return. If 𝐩\mathbf{p} is the (normalized) initial price of the assets, then 𝐩⊕𝐫\mathbf{p}\oplus\mathbf{r} is the (normalized) final prices. The identity ([3.23](https://arxiv.org/html/2510.25740v1#S3.E23 "In 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) states that the logarithmic divergence depends only on the returns and is independent of the initial prices. Theorem [3.20](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem20 "Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") states that the excess growth rate is the only logarithmic divergence (subject to the imposed regularity conditions) with this property. We believe the regularity conditions can be partially relaxed but do not pursue this further in this paper.

###### Proof of Theorem [3.20](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem20 "Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

151515This result was claimed in [[50](https://arxiv.org/html/2510.25740v1#bib.bib50), Example 3.10] without proof. We provide a complete argument here.

We first show that (ii) implies (i). Suppose that φ=−H​(𝝅,⋅)+c\varphi=-H(\boldsymbol{\pi},\cdot)+c for some 𝝅∈Δn∘\boldsymbol{\pi}\in\Delta\_{n}^{\circ} and c∈ℝc\in\mathbb{R}. Since φ\varphi and −H​(𝝅,⋅)-H(\boldsymbol{\pi},\cdot) only differ by a constant, they induce the same logarithmic divergence. By Proposition [3.18](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem18 "Proposition 3.18 (Excess growth rate as a logarithmic divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") (and numéraire invariance of Γ\Gamma), we have Lφ​(𝐪∥𝐩)=Γ​(𝝅,𝐪⊖𝐩)L\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p})=\Gamma(\boldsymbol{\pi},\mathbf{q}\ominus\mathbf{p}). Since the perturbation operation is commutative on Δn∘\Delta\_{n}^{\circ}, we have

|  |  |  |
| --- | --- | --- |
|  | Lφ​(𝐪⊕𝐫∥𝐩⊕𝐫)=Γ(𝝅,((𝐪⊕𝐫)⊖(𝐩⊕𝐫))=Γ​(𝝅,𝐪⊖𝐩)=Lφ​(𝐪∥𝐩).\begin{split}L\_{\varphi}(\mathbf{q}\oplus\mathbf{r}\;\|\;\mathbf{p}\oplus\mathbf{r})&=\Gamma(\boldsymbol{\pi},((\mathbf{q}\oplus\mathbf{r})\ominus(\mathbf{p}\oplus\mathbf{r}))\\ &=\Gamma(\boldsymbol{\pi},\mathbf{q}\ominus\mathbf{p})\\ &=L\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p}).\end{split} |  |

Hence 𝐋φ\mathbf{L}\_{\varphi} is invariant under perturbation.

The proof of the converse is more delicate. We will use tools from stochastic portfolio theory and information geometry, which will be introduced as needed, to derive differential implications of the functional equation ([3.22](https://arxiv.org/html/2510.25740v1#S3.E22 "In item (i) ‣ Theorem 3.20 (Characterization III). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")). Suppose 𝐋φ\mathbf{L}\_{\varphi} is invariant under perturbation. Define a mapping 𝝅:Δn∘→ℝn\boldsymbol{\pi}:\Delta\_{n}^{\circ}\rightarrow\mathbb{R}^{n} by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.24) |  | 𝝅i​(𝐩):=xi​(1+∇𝐞i−𝐩φ​(𝐩)),i=1,…,n,\boldsymbol{\pi}\_{i}(\mathbf{p}):=x\_{i}\left(1+\nabla\_{\mathbf{e}\_{i}-\mathbf{p}}\varphi(\mathbf{p})\right),\quad i=1,\ldots,n, |  |

where (𝐞1,…,𝐞n)(\mathbf{e}\_{1},\ldots,\mathbf{e}\_{n}) is the standard basis of ℝn\mathbb{R}^{n}. Since Φ\Phi is strictly concave, by [[49](https://arxiv.org/html/2510.25740v1#bib.bib49), Proposition 6] we have that 𝝅​(𝐩)∈Δn∘\boldsymbol{\pi}(\mathbf{p})\in\Delta\_{n}^{\circ} for 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ}. Hence, 𝝅\boldsymbol{\pi} is a mapping from Δn∘\Delta\_{n}^{\circ} into itself. We call 𝝅\boldsymbol{\pi} the portfolio map generated by φ\varphi. We claim that 𝝅​(𝐩)\boldsymbol{\pi}(\mathbf{p}) is constant in 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ}. By an abuse of notation, we have 𝝅​(𝐩)≡𝝅\boldsymbol{\pi}(\mathbf{p})\equiv\boldsymbol{\pi} for some element 𝝅\boldsymbol{\pi} of Δn∘\Delta\_{n}^{\circ}. On the other hand, the portfolio map generated by the exponentially concave function −H​(𝝅,⋅)-H(\boldsymbol{\pi},\cdot) is the constant 𝝅\boldsymbol{\pi} [[26](https://arxiv.org/html/2510.25740v1#bib.bib26), Example 3.1.6]. Then, by [[49](https://arxiv.org/html/2510.25740v1#bib.bib49), Proposition 6(i)], we have that φ=−H​(𝝅,⋅)+c\varphi=-H(\boldsymbol{\pi},\cdot)+c for some c∈ℝc\in\mathbb{R}. (This is a variant of the classical fact that if two functions have the same gradient on a domain then they differ by a constant.)

To show that 𝝅​(⋅)\boldsymbol{\pi}(\cdot) is a constant mapping, we switch to another coordinate system on Δn∘\Delta\_{n}^{\circ} under which the meaning of invariance under perturbation is more apparent. For 𝐱∈Δn∘\mathbf{x}\in\Delta\_{n}^{\circ}, we define its exponential coordinates 𝜽=(θ1,…,θn)∈ℝn−1\boldsymbol{\theta}=(\theta\_{1},\ldots,\theta\_{n})\in\mathbb{R}^{n-1} by

|  |  |  |
| --- | --- | --- |
|  | θi=log⁡qiqn,i=1,…,n−1.\theta\_{i}=\log\frac{q\_{i}}{q\_{n}},\quad i=1,\ldots,n-1. |  |

Similarly, let ϕ=(ϕ1,…,ϕn)\boldsymbol{\phi}=(\phi\_{1},\ldots,\phi\_{n}) be the exponential coordinates of 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ}. Now, it is easy to verify that the exponential coordinates of 𝐪⊕𝐩\mathbf{q}\oplus\mathbf{p} are

|  |  |  |
| --- | --- | --- |
|  | log⁡(𝐪⊕𝐩)i(𝐪⊕𝐩)n=θi+ϕi,i=1,…,n−1.\log\frac{(\mathbf{q}\oplus\mathbf{p})\_{i}}{(\mathbf{q}\oplus\mathbf{p})\_{n}}=\theta\_{i}+\phi\_{i},\quad i=1,\ldots,n-1. |  |

That is, the exponential coordinate system is an isomorphism between the commutative groups (Δn∘,⊕)(\Delta\_{n}^{\circ},\oplus) and (ℝn−1,+)(\mathbb{R}^{n-1},+).

Let 𝐋~φ:ℝn−1×ℝn−1→ℝ+\widetilde{\mathbf{L}}\_{\varphi}:\mathbb{R}^{n-1}\times\mathbb{R}^{n-1}\rightarrow\mathbb{R}\_{+} be the logarithmic divergence of φ\varphi written in exponential coordinates:

|  |  |  |
| --- | --- | --- |
|  | 𝐋~φ​(𝜽∥ϕ):=𝐋φ​(𝐪∥𝐩).\widetilde{\mathbf{L}}\_{\varphi}(\boldsymbol{\theta}\;\|\;\boldsymbol{\phi}):=\mathbf{L}\_{\varphi}(\mathbf{q}\;\|\;\mathbf{p}). |  |

The assumption that 𝐋φ\mathbf{L}\_{\varphi} is invariant under perturbation is equivalent to the condition that 𝐋~φ\widetilde{\mathbf{L}}\_{\varphi} is invariant under translation:

|  |  |  |
| --- | --- | --- |
|  | L~φ​(𝜽+𝐡∥ϕ+𝐡)=L~φ​(𝜽∥ϕ),𝜽,ϕ,𝐡∈ℝn−1.\widetilde{L}\_{\varphi}(\boldsymbol{\theta}+\mathbf{h}\;\|\;\boldsymbol{\phi}+\mathbf{h})=\widetilde{L}\_{\varphi}(\boldsymbol{\theta}\;\|\;\boldsymbol{\phi}),\quad\boldsymbol{\theta},\boldsymbol{\phi},\mathbf{h}\in\mathbb{R}^{n-1}. |  |

For 𝜽∈ℝn−1\boldsymbol{\theta}\in\mathbb{R}^{n-1}, we define

|  |  |  |
| --- | --- | --- |
|  | gi​j​(𝜽):=−∂∂θi​∂∂ϕj​L~φ​(𝜽∥ϕ)|ϕ=𝜽,i,j=1,…,n−1.g\_{ij}(\boldsymbol{\theta}):=-\left.\frac{\partial}{\partial\theta\_{i}}\frac{\partial}{\partial\phi\_{j}}\widetilde{L}\_{\varphi}(\boldsymbol{\theta}\;\|\;\boldsymbol{\phi})\right|\_{\boldsymbol{\phi}=\boldsymbol{\theta}},\quad i,j=1,\ldots,n-1. |  |

In information geometry (see [[4](https://arxiv.org/html/2510.25740v1#bib.bib4), Chapter 6]), the matrix (gi​j​(𝜽))(g\_{ij}(\boldsymbol{\theta})) represents the Riemannian metric on Δn∘\Delta\_{n}^{\circ} induced by the divergence 𝐋φ\mathbf{L}\_{\varphi}, when expressed under the exponential coordinate system. The assumption that φ\varphi is regular implies that the matrix (gi​j​(𝜽))(g\_{ij}(\boldsymbol{\theta})) is symmetric and strictly positive definite (see [[50](https://arxiv.org/html/2510.25740v1#bib.bib50), Theorem 4.5]). We denote its inverse by (gi​j​(𝜽))(g^{ij}(\boldsymbol{\theta})).

Furthermore, we define (using the C4C^{4} condition)

|  |  |  |
| --- | --- | --- |
|  | Γi​j​k​(𝜽):=−∂∂θi​∂∂θj​∂∂ϕi​L~φ​(𝜽∥ϕ)|ϕ=𝜽,i,j,k=1,…,n−1,\Gamma\_{ijk}(\boldsymbol{\theta}):=-\left.\frac{\partial}{\partial\theta\_{i}}\frac{\partial}{\partial\theta\_{j}}\frac{\partial}{\partial\phi\_{i}}\widetilde{L}\_{\varphi}(\boldsymbol{\theta}\;\|\;\boldsymbol{\phi})\right|\_{\boldsymbol{\phi}=\boldsymbol{\theta}},\quad i,j,k=1,\ldots,n-1, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Γi​jk​(𝜽):=∑ℓ=1n−1Γi​j​ℓ​(𝜽)​gℓ​k​(𝜽),i,j,k=1,…,n−1.\Gamma\_{ij}^{k}(\boldsymbol{\theta}):=\sum\_{\ell=1}^{n-1}\Gamma\_{ij\ell}(\boldsymbol{\theta})g^{\ell k}(\boldsymbol{\theta}),\quad i,j,k=1,\ldots,n-1. |  |

These are the Christoffel symbols of the so-called primal affine connection induced by the divergence.
By [[50](https://arxiv.org/html/2510.25740v1#bib.bib50), Theorem 4.7], we have the identity

|  |  |  |  |
| --- | --- | --- | --- |
| (3.25) |  | Γi​jk​(𝜽)=δi​j​k−δi​k​𝝅j​(𝜽)−δj​k​𝝅i​(𝜽),𝜽∈Δn∘,\Gamma\_{ij}^{k}(\boldsymbol{\theta})=\delta\_{ijk}-\delta\_{ik}\boldsymbol{\pi}\_{j}(\boldsymbol{\theta})-\delta\_{jk}\boldsymbol{\pi}\_{i}(\boldsymbol{\theta}),\quad\boldsymbol{\theta}\in\Delta\_{n}^{\circ}, |  |

where δi​j​k\delta\_{ijk}, δi​k\delta\_{ik} and δj​k\delta\_{jk} are Kronecker deltas and 𝝅​(𝜽):=𝝅​(𝐩)\boldsymbol{\pi}(\boldsymbol{\theta}):=\boldsymbol{\pi}(\mathbf{p}) is the portfolio map expressed in exponential coordinates.

The key observation is that since L~φ\widetilde{L}\_{\varphi} is translation invariant, the Christoffel symbols Γi​jk​(𝜽)\Gamma\_{ij}^{k}(\boldsymbol{\theta}) are constant in 𝜽\boldsymbol{\theta}. Differentiating ([3.25](https://arxiv.org/html/2510.25740v1#S3.E25 "In 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) with respect to θℓ\theta\_{\ell} gives

|  |  |  |
| --- | --- | --- |
|  | −δi​k​∂∂θℓ​𝝅j​(𝜽)−δj​k​∂∂θℓ​𝝅i​(𝜽)=0,i,j,k,ℓ=1,…,n−1.-\delta\_{ik}\frac{\partial}{\partial\theta\_{\ell}}\boldsymbol{\pi}\_{j}(\boldsymbol{\theta})-\delta\_{jk}\frac{\partial}{\partial\theta\_{\ell}}\boldsymbol{\pi}\_{i}(\boldsymbol{\theta})=0,\quad i,j,k,\ell=1,\ldots,n-1. |  |

Now, setting i=j=ki=j=k gives

|  |  |  |
| --- | --- | --- |
|  | ∂∂θℓ​𝝅i​(𝜽)=0,i,ℓ=1,…,n−1.\frac{\partial}{\partial\theta\_{\ell}}\boldsymbol{\pi}\_{i}(\boldsymbol{\theta})=0,\quad i,\ell=1,\ldots,n-1. |  |

It follows that 𝝅​(𝜽)\boldsymbol{\pi}(\boldsymbol{\theta}) is constant in 𝜽\boldsymbol{\theta} (and hence 𝝅​(𝐩)\boldsymbol{\pi}(\mathbf{p}) is constant in 𝐩\mathbf{p}), and the claim is proved.
∎

###### Remark 3.21 (Excess growth rate and the Fisher–Rao metric).

In Remark [1.2](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem2 "Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")(ii) we computed the Taylor approximation of γ​(𝛑,𝐫)\gamma(\boldsymbol{\pi},\mathbf{r}) when 𝛑≈0\boldsymbol{\pi}\approx 0. A similar computation, applied to Γ𝛑​(𝐩+t​𝐯∥𝐩)\Gamma\_{\boldsymbol{\pi}}(\mathbf{p}+t\mathbf{v}\;\|\;\mathbf{p}) for 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ} and 𝐯∈ℝn\mathbf{v}\in\mathbb{R}^{n} tangent to Δn∘\Delta\_{n}^{\circ} (i.e., ∑i=1nvi=0\sum\_{i=1}^{n}v\_{i}=0), shows that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.26) |  | Γ𝝅​(𝐩+t​𝐯∥𝐩)=t22​∑i,j=1nπi​(δi​j−πj)pi​pj​vi​vj+o​(t2),as ​t→0.\Gamma\_{\boldsymbol{\pi}}(\mathbf{p}+t\mathbf{v}\;\|\;\mathbf{p})=\frac{t^{2}}{2}\sum\_{i,j=1}^{n}\frac{\pi\_{i}(\delta\_{ij}-\pi\_{j})}{p\_{i}p\_{j}}v\_{i}v\_{j}+o(t^{2}),\quad\text{as }t\rightarrow 0. |  |

In information geometric language (see [[4](https://arxiv.org/html/2510.25740v1#bib.bib4), Chapter 6]), this expansion defines the Riemannian metric induced by Γ𝛑(⋅∥⋅)\Gamma\_{\boldsymbol{\pi}}(\cdot\;\|\;\cdot) as a *divergence* (also called a *contrast function* on Δn∘\Delta\_{n}^{\circ}. Letting 𝛑=𝐩\boldsymbol{\pi}=\mathbf{p} gives

|  |  |  |
| --- | --- | --- |
|  | Γ𝐩​(𝐩+t​𝐯∥𝐩)=t22​∑i=1nvi2pi+o​(t2).\Gamma\_{\mathbf{p}}(\mathbf{p}+t\mathbf{v}\;\|\;\mathbf{p})=\frac{t^{2}}{2}\sum\_{i=1}^{n}\frac{v\_{i}^{2}}{p\_{i}}+o(t^{2}). |  |

Thus, we recover the Fisher–Rao metric ‖𝐯‖𝐩2:=∑i=1nvi2pi\|\mathbf{v}\|\_{\mathbf{p}}^{2}:=\sum\_{i=1}^{n}\frac{v\_{i}^{2}}{p\_{i}} at 𝐩∈Δn∘\mathbf{p}\in\Delta\_{n}^{\circ}. Further details can be found in [[49](https://arxiv.org/html/2510.25740v1#bib.bib49), Section 2.6] and [[50](https://arxiv.org/html/2510.25740v1#bib.bib50)].

## 4. Optimization

Our goal in this section is to study maximization of the (expected) excess growth rate.
For a random log return vector 𝐫\mathbf{r} with values in ℝn\mathbb{R}^{n}, we consider

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | max𝝅∈Δn⁡𝔼​[γ​(𝝅,𝐫)].\max\_{\boldsymbol{\pi}\in\Delta\_{n}}\ \mathbb{E}\big[\gamma(\boldsymbol{\pi},\mathbf{r})\big]. |  |

In the special case where 𝐫\mathbf{r} is deterministic (constant), this reduces to

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | max𝝅∈Δn⁡γ​(𝝅,𝐫).\max\_{\boldsymbol{\pi}\in\Delta\_{n}}\ \gamma(\boldsymbol{\pi},\mathbf{r}). |  |

### 4.1. Motivations

As we observed in ([2.9](https://arxiv.org/html/2510.25740v1#S2.E9 "In 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), the log-wealth of a constant rebalanced portfolio admits a decomposition161616The decomposition is more complex for portfolios whose holdings change over time; see [[48](https://arxiv.org/html/2510.25740v1#bib.bib48)] and [[26](https://arxiv.org/html/2510.25740v1#bib.bib26), Corollary 1.1.6] for the continuous-time analogue. in which the excess growth rate captures a rebalancing premium arising from the cross-sectional dispersion of asset returns. The other component is the weighted average log return of the assets. When all assets have the same average log return, excess growth rate maximization ([4.1](https://arxiv.org/html/2510.25740v1#S4.E1 "In 4. Optimization ‣ A mathematical study of the excess growth rate")) agrees with log-wealth maximization and leads to the growth optimal portfolio (Remark [4.13](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem13 "Remark 4.13 (Growth optimal portfolio). ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")). Because the (expected) excess growth rate depends primarily on the covariance structure of the returns and the diversification decision 𝝅\boldsymbol{\pi}—rather than on hard-to-estimate expected returns—it is comparatively robust and less model-sensitive. Targeting a higher excess growth rate thus aligns with constructing portfolios that (i) diversify across stocks, (ii) systematically “harvest” market volatility, and (iii) outperform relative to buy-and-hold benchmarks under suitable conditions on market diversity (see [[26](https://arxiv.org/html/2510.25740v1#bib.bib26), Chapters 1–2]). In this sense, excess growth rate maximization isolates the component of growth attainable from rebalancing alone, independent of growth rates that are difficult to forecast. For these reasons, optimization of the excess growth rate is both practically appealing and theoretically informative.

The deterministic problem ([4.2](https://arxiv.org/html/2510.25740v1#S4.E2 "In 4. Optimization ‣ A mathematical study of the excess growth rate")) is also of independent interest: we show that it has an *explicit solution* that provides insight into the structure of γ​(𝝅,𝐫)\gamma(\boldsymbol{\pi},\mathbf{r}). Moreover, after a transformation, this solution can be used to solve two fundamental variational problems over pairs of distributions (𝝅,𝐪)∈Δn×Δn(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | sup(𝝅,𝐪)∈Δn×Δn{⟨𝐪−𝝅,𝐫⟩−λ​H​(𝐪∥𝝅)},\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}}\Bigl\{\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle-\lambda\,H(\mathbf{q}\;\|\;\boldsymbol{\pi})\Bigr\}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | sup(𝝅,𝐪)∈Δn×Δn:H​(𝐪∥𝝅)≤η⟨𝐪−𝝅,𝐫⟩,η≥0.\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}:\ H(\mathbf{q}\;\|\;\boldsymbol{\pi})\leq\eta}\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle,\qquad\eta\geq 0. |  |

For this reason, we first treat the deterministic optimization ([4.2](https://arxiv.org/html/2510.25740v1#S4.E2 "In 4. Optimization ‣ A mathematical study of the excess growth rate")) in Section [4.2](https://arxiv.org/html/2510.25740v1#S4.SS2 "4.2. Maximizing the excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate"), followed by the link to the variational problems in Section [2.2](https://arxiv.org/html/2510.25740v1#S2.SS2 "2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"). The generalization to ([4.1](https://arxiv.org/html/2510.25740v1#S4.E1 "In 4. Optimization ‣ A mathematical study of the excess growth rate")) is treated at the end in Section [4.4](https://arxiv.org/html/2510.25740v1#S4.SS4 "4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate"). See [[22](https://arxiv.org/html/2510.25740v1#bib.bib22), [41](https://arxiv.org/html/2510.25740v1#bib.bib41)] for other formulations of excess growth rate optimization.

###### Remark 4.1.

As γ​(𝛑,⋅)\gamma(\boldsymbol{\pi},\cdot) is convex it may also seem natural to ask about minimizing the excess growth rate with respect to 𝐫\mathbf{r}, but this is uninteresting since any constant vector attains the minimum, γ​(𝛑,𝟏)=0\gamma(\boldsymbol{\pi},\mathbf{1})=0 (Proposition [2.2](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem2 "Proposition 2.2 (Dependence on support). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")).

### 4.2. Maximizing the excess growth rate

Consider the Lagrangian for the deterministic concave maximization problem ([4.2](https://arxiv.org/html/2510.25740v1#S4.E2 "In 4. Optimization ‣ A mathematical study of the excess growth rate")):

|  |  |  |
| --- | --- | --- |
|  | ℒ​(𝝅,λ,𝝁)=log⁡(∑i=1nπi​eri)−∑i=1nπi​ri−λ​(∑i=1nπi−1)+∑i=1nμi​πi,\mathcal{L}(\boldsymbol{\pi},\lambda,\boldsymbol{\mu})=\log\!\left(\sum\_{i=1}^{n}\pi\_{i}e^{r\_{i}}\right)-\sum\_{i=1}^{n}\pi\_{i}r\_{i}-\lambda\left(\sum\_{i=1}^{n}\pi\_{i}-1\right)+\sum\_{i=1}^{n}\mu\_{i}\pi\_{i}, |  |

where the multiplier λ∈ℝ\lambda\in\mathbb{R} enforces ∑i=1nπi=1\sum\_{i=1}^{n}\pi\_{i}=1 and the mulipliers μj≥0\mu\_{j}\geq 0 enforce πi≥0\pi\_{i}\geq 0. The feasible set Δn\Delta\_{n} is nonempty, compact, and convex. Moreover, Slater’s condition holds: there exists a strictly feasible point for the inequality constraints that satisfies the equality constraint, e.g. 𝐞¯n=(1/n,…,1/n)\bar{\mathbf{e}}\_{n}=(1/n,\ldots,1/n).
As a result, strong duality holds (see [[12](https://arxiv.org/html/2510.25740v1#bib.bib12), Section 5.2.3]) and the Karush–Kuhn–Tucker (KKT) conditions are necessary and sufficient for optimality.

At any maximizer, the KKT conditions require

|  |  |  |
| --- | --- | --- |
|  | ∂ℒ∂πi=eri∑j=1nπj​erj−ri−λ+μi=0,\frac{\partial\mathcal{L}}{\partial\pi\_{i}}=\frac{e^{r\_{i}}}{\sum\_{j=1}^{n}\pi\_{j}e^{r\_{j}}}-r\_{i}-\lambda+\mu\_{i}=0, |  |

together with

|  |  |  |
| --- | --- | --- |
|  | μi≥0,πi≥0,μi​πi=0​(complementary slackness),∑i=1nπi=1.\mu\_{i}\geq 0,\quad\pi\_{i}\geq 0,\quad\mu\_{i}\pi\_{i}=0\ \text{(complementary slackness)},\quad\sum\_{i=1}^{n}\pi\_{i}=1. |  |

In particular, if πi>0\pi\_{i}>0 then μi=0\mu\_{i}=0 and

|  |  |  |
| --- | --- | --- |
|  | eri∑j=1nπj​erj−ri=λ,\frac{e^{r\_{i}}}{\sum\_{j=1}^{n}\pi\_{j}e^{r\_{j}}}-r\_{i}=\lambda, |  |

while for πi=0\pi\_{i}=0 we have

|  |  |  |
| --- | --- | --- |
|  | eri∑j=1nπj​erj−ri≤λ.\frac{e^{r\_{i}}}{\sum\_{j=1}^{n}\pi\_{j}e^{r\_{j}}}-r\_{i}\leq\lambda. |  |

This leads us to the following structural characterization of any optimizer. In the sequel we will see that as long as 𝐫\mathbf{r} has distinct entries the optimizer is unique.

###### Lemma 4.2.

If 𝐫∈ℝn\mathbf{r}\in\mathbb{R}^{n} has n≥2n\geq 2 distinct coordinates, any maximizer 𝛑⋆\boldsymbol{\pi}^{\star} of ([4.2](https://arxiv.org/html/2510.25740v1#S4.E2 "In 4. Optimization ‣ A mathematical study of the excess growth rate")) is supported on *exactly* two indices; i.e., |supp⁡(𝛑⋆)|=2\lvert\operatorname{supp}(\boldsymbol{\pi}^{\star})\rvert=2. In particular, 𝛑⋆\boldsymbol{\pi}^{\star} has support on the maximum and minimum of 𝐫\mathbf{r}, r(n)r\_{(n)} and r(1)r\_{(1)}.

###### Proof.

Let Z:=∑j=1nπj⋆​erj>0Z:=\sum\_{j=1}^{n}\pi\_{j}^{\star}e^{r\_{j}}>0 and define

|  |  |  |
| --- | --- | --- |
|  | hλ​(x):=exZ−x−λ,λ∈ℝ.h\_{\lambda}(x):=\frac{e^{x}}{Z}-x-\lambda,\quad\lambda\in\mathbb{R}. |  |

Then hλ′′​(x)=ex/Z>0h\_{\lambda}^{\prime\prime}(x)=e^{x}/Z>0, so hλh\_{\lambda} is strictly convex and has at most two distinct zeros. From the KKT condition, for every ii in supp⁡(𝝅⋆)\operatorname{supp}(\boldsymbol{\pi}^{\star}) we must have hλ​(ri)=0h\_{\lambda}(r\_{i})=0. Since the rir\_{i} are assumed to be distinct, we conclude |supp⁡(𝝅⋆)|≤2\lvert\operatorname{supp}(\boldsymbol{\pi}^{\star})\rvert\leq 2.

On the other hand, |supp⁡(𝝅)|=1\lvert\operatorname{supp}(\boldsymbol{\pi})\rvert=1 gives γ​(𝝅,𝐫)=0\gamma(\boldsymbol{\pi},\mathbf{r})=0, which is suboptimal whenever 𝐫\mathbf{r} is not constant, because for any i≠ji\neq j and 𝝅′:=12​(𝐞i+𝐞j)∈Δn\boldsymbol{\pi}^{\prime}:=\frac{1}{2}(\mathbf{e}\_{i}+\mathbf{e}\_{j})\in\Delta\_{n},

|  |  |  |
| --- | --- | --- |
|  | γ​(𝝅′,𝐫)=log⁡(eri+erj2)−ri+rj2>0.\gamma(\boldsymbol{\pi}^{\prime},\mathbf{r})=\log\!\Bigl(\tfrac{e^{r\_{i}}+e^{r\_{j}}}{2}\Bigr)-\tfrac{r\_{i}+r\_{j}}{2}>0. |  |

Finally, to see that πi⋆>0\pi\_{i}^{\star}>0 if and only if ri∈{r(1),r(n)}r\_{i}\in\{r\_{(1)},r\_{(n)}\} we observe that the KKT conditions imply that hλ​(ri)≤0h\_{\lambda}(r\_{i})\leq 0 for all ii. By strict convexity and the fact that limx→±∞hλ​(x)=+∞\lim\_{x\to\pm\infty}h\_{\lambda}(x)=+\infty the sublevel set {x:hλ​(x)≤0}\{x:h\_{\lambda}(x)\leq 0\} is a compact interval [u,v][u,v] with hλ​(u)=hλ​(v)=0h\_{\lambda}(u)=h\_{\lambda}(v)=0. Moreover,

|  |  |  |
| --- | --- | --- |
|  | hλ​(x)<0​for all ​x∈(u,v),hλ​(x)>0​for all ​x∉[u,v].h\_{\lambda}(x)<0\ \text{for all }x\in(u,v),\qquad h\_{\lambda}(x)>0\ \text{for all }x\notin[u,v]. |  |

As hλ​(ri)≤0h\_{\lambda}(r\_{i})\leq 0 for *every* ii, ri∈[u,v]r\_{i}\in[u,v] for all ii. Since the rir\_{i} are distinct, (u,v)(u,v) is non-empty. In particular,

|  |  |  |
| --- | --- | --- |
|  | u≤mini⁡ri=r(1)andmaxi⁡ri=r(n)≤v.u\leq\min\_{i}r\_{i}=r\_{(1)}\quad\text{and}\quad\max\_{i}r\_{i}=r\_{(n)}\leq v. |  |

But uu and vv themselves are necessarily entries of 𝐫\mathbf{r} as we have already established that 𝐫\mathbf{r} contains the two unique roots {x:hλ​(x)=0}\{x:h\_{\lambda}(x)=0\}. Thus we necessarily have

|  |  |  |
| --- | --- | --- |
|  | u=r(1)andv=r(n).u=r\_{(1)}\quad\text{and}\quad v=r\_{(n)}. |  |

Consequently, the only indices with hλ​(ri)=0h\_{\lambda}(r\_{i})=0 are those achieving the minimum and maximum of 𝐫\mathbf{r} as claimed.
∎

This result allows us to obtain an explicit equation for the maximum and the optimal allocation 𝝅⋆\boldsymbol{\pi}^{\star}. The intuition is very much in the spirit of “volatility harvesting.” By comparison to the wealth maximizing strategy (which would invest solely in the stock with the highest return), the optimal strategy for the excess growth rate allocates capital to the most extreme returns; both largest *and* smallest.

###### Theorem 4.3.

Suppose 𝐫∈ℝn\mathbf{r}\in\mathbb{R}^{n} has n≥2n\geq 2 distinct coordinates. Then

|  |  |  |
| --- | --- | --- |
|  | max𝝅∈Δn⁡γ​(𝝅,𝐫)=log⁡(er(n)−er(1)r(n)−r(1))−er(n)​r(1)−er(1)​r(n)er(n)−er(1)−1.\max\_{\boldsymbol{\pi}\in\Delta\_{n}}\gamma(\boldsymbol{\pi},\mathbf{r})=\log\!\Bigl(\tfrac{e^{r\_{(n)}}-e^{r\_{(1)}}}{r\_{(n)}-r\_{(1)}}\Bigr)-\frac{e^{r\_{(n)}}r\_{(1)}-e^{r\_{(1)}}r\_{(n)}}{e^{r\_{(n)}}-e^{r\_{(1)}}}-1. |  |

Moreover, the unique optimizer 𝛑⋆\boldsymbol{\pi}^{\star} is supported on two points:

|  |  |  |
| --- | --- | --- |
|  | πi⋆⋆=eri⋆−erj⋆−(ri⋆−rj⋆)​erj⋆(ri⋆−rj⋆)​(eri⋆−erj⋆),πj⋆⋆=1−πi⋆⋆,πk⋆=0(k∉{i⋆,j⋆}),\pi\_{i^{\star}}^{\star}=\frac{\,e^{r\_{i^{\star}}}-e^{r\_{j^{\star}}}-(r\_{i^{\star}}-r\_{j^{\star}})e^{r\_{j^{\star}}}\,}{(r\_{i^{\star}}-r\_{j^{\star}})\,(e^{r\_{i^{\star}}}-e^{r\_{j^{\star}}})},\quad\pi\_{j^{\star}}^{\star}=1-\pi\_{i^{\star}}^{\star},\quad\pi\_{k}^{\star}=0\ \ (k\notin\{i^{\star},j^{\star}\}), |  |

where the indices {i⋆,j⋆}\{i^{\star},j^{\star}\} attain the maximum and minimum of 𝐫\mathbf{r}, respectively; i.e., ri⋆=r(n)r\_{i^{\star}}=r\_{(n)} and rj⋆=r(1)r\_{j^{\star}}=r\_{(1)}.

###### Proof.

Fix distinct indices {i,j}\{i,j\} and parameterize 𝝅\boldsymbol{\pi} by

|  |  |  |
| --- | --- | --- |
|  | πi=t,πj=1−t,t∈[0,1],πk=0(k∉{i,j}).\pi\_{i}=t,\quad\pi\_{j}=1-t,\quad t\in[0,1],\qquad\pi\_{k}=0\ \ (k\notin\{i,j\}). |  |

Define the univariate objective

|  |  |  |
| --- | --- | --- |
|  | fi​j​(t):=γ​(𝝅,𝐫)=log⁡(t​eri+(1−t)​erj)−(t​ri+(1−t)​rj).f\_{ij}(t):=\gamma(\boldsymbol{\pi},\mathbf{r})=\log\!\bigl(te^{r\_{i}}+(1-t)e^{r\_{j}}\bigr)-\bigl(tr\_{i}+(1-t)r\_{j}\bigr). |  |

From Lemma [4.2](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.2. Maximizing the excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") we conclude that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | max𝝅∈Δn⁡γ​(𝝅,𝐫)=max1≤i<j≤n⁡{maxt∈[0,1]⁡fi​j​(t)}=maxt∈[0,1]⁡fi⋆​j⋆​(t).\max\_{\boldsymbol{\pi}\in\Delta\_{n}}\gamma(\boldsymbol{\pi},\mathbf{r})=\max\_{1\leq i<j\leq n}\left\{\max\_{t\in[0,1]}f\_{ij}(t)\right\}=\max\_{t\in[0,1]}f\_{i^{\star}j^{\star}}(t). |  |

So, it suffices to treat the inner maximization problem for fixed i≠ji\not=j. One computes

|  |  |  |
| --- | --- | --- |
|  | fi​j′​(t)=eri−erjt​eri+(1−t)​erj−(ri−rj),fi​j′′​(t)=−(eri−erj)2(t​eri+(1−t)​erj)2<0.f\_{ij}^{\prime}(t)=\frac{e^{r\_{i}}-e^{r\_{j}}}{te^{r\_{i}}+(1-t)e^{r\_{j}}}-(r\_{i}-r\_{j}),\qquad f\_{ij}^{\prime\prime}(t)=-\frac{(e^{r\_{i}}-e^{r\_{j}})^{2}}{\bigl(te^{r\_{i}}+(1-t)e^{r\_{j}}\bigr)^{2}}<0. |  |

Thus fi​jf\_{ij} is strictly concave on [0,1][0,1]. It is standard to check that fi​jf\_{ij} is maximized at

|  |  |  |
| --- | --- | --- |
|  | ti​j⋆=eri−erj−(ri−rj)​erj(ri−rj)​(eri−erj)∈(0,1),t\_{ij}^{\star}=\frac{\,e^{r\_{i}}-e^{r\_{j}}-(r\_{i}-r\_{j})e^{r\_{j}}\,}{(r\_{i}-r\_{j})\,(e^{r\_{i}}-e^{r\_{j}})}\in(0,1), |  |

and the corresponding maximal value simplifies to

|  |  |  |
| --- | --- | --- |
|  | maxt∈[0,1]⁡fi​j​(t)=log⁡(eri−erjri−rj)−eri​rj−erj​rieri−erj−1> 0for ​ri≠rj.\max\_{t\in[0,1]}f\_{ij}(t)=\log\!\Bigl(\frac{e^{r\_{i}}-e^{r\_{j}}}{r\_{i}-r\_{j}}\Bigr)-\frac{e^{r\_{i}}r\_{j}-e^{r\_{j}}r\_{i}}{e^{r\_{i}}-e^{r\_{j}}}-1\;>\;0\quad\text{for }r\_{i}\neq r\_{j}. |  |

Combining this with ([4.5](https://arxiv.org/html/2510.25740v1#S4.E5 "In 4.2. Maximizing the excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) completes the proof.
∎

###### Remark 4.4.

If 𝐫\mathbf{r} has repeated coordinates, we may aggregate equal entries; the same conclusions hold upon reducing to the list of distinct values. In particular, any maximizer is supported on exactly two distinct values of 𝐫\mathbf{r} unless 𝐫\mathbf{r} is constant, in which case any 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n} is optimal.

### 4.3. Variational interpretation

Before turning to the optimization *in expectation*, we address the implications of this explicit solution on the variational problems ([4.3](https://arxiv.org/html/2510.25740v1#S4.E3 "In 4.1. Motivations ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) and ([4.4](https://arxiv.org/html/2510.25740v1#S4.E4 "In 4.1. Motivations ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")). The link to the penalized problem ([4.3](https://arxiv.org/html/2510.25740v1#S4.E3 "In 4.1. Motivations ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) is easy to see by leveraging the analysis in Section [2.2](https://arxiv.org/html/2510.25740v1#S2.SS2 "2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"). Namely, from Proposition [2.7](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem7 "Proposition 2.7 (Variational representation). ‣ 2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") we obtain

|  |  |  |
| --- | --- | --- |
|  | sup(𝝅,𝐪)∈Δn×Δn{⟨𝐪−𝝅,𝐫⟩−H​(𝐪∥𝝅)}=sup𝝅∈Δnγ​(𝝅,𝐫),\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}}\Bigl\{\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle-H(\mathbf{q}\;\|\;\boldsymbol{\pi})\Bigr\}=\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}\gamma(\boldsymbol{\pi},\mathbf{r}), |  |

and we understand the form of the optimal 𝐪\mathbf{q} for fixed 𝝅\boldsymbol{\pi}. More generally, for λ>0\lambda>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(𝝅,𝐪)∈Δn×Δn{⟨𝐪−𝝅,𝐫⟩−λ​H​(𝐪∥𝝅)}\displaystyle\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}}\Bigl\{\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle-\lambda\,H(\mathbf{q}\;\|\;\boldsymbol{\pi})\Bigr\} | =sup𝝅∈Δn{λ​log⁡(∑i=1nπi​eri/λ)−∑i=1nπi​ri}\displaystyle=\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}\left\{\lambda\log\!\left(\sum\_{i=1}^{n}\pi\_{i}e^{r\_{i}/\lambda}\right)-\sum\_{i=1}^{n}\pi\_{i}r\_{i}\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.6) |  |  | =λ​sup𝝅∈Δnγ​(𝝅,𝐫/λ).\displaystyle=\lambda\,\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda). |  |

So, the maximization of γ​(𝝅,𝐫)\gamma(\boldsymbol{\pi},\mathbf{r}) in Theorem [4.3](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2. Maximizing the excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") provides us with the solution to ([4.6](https://arxiv.org/html/2510.25740v1#S4.E6 "In 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) which we collect in the next proposition.

###### Proposition 4.5.

Suppose 𝐫∈ℝn\mathbf{r}\in\mathbb{R}^{n} has n≥2n\geq 2 distinct coordinates. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(𝝅,𝐪)∈Δn×Δn\displaystyle\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}} | {⟨𝐪−𝝅,𝐫⟩−λ​H​(𝐪∥𝝅)}\displaystyle\Bigl\{\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle-\lambda\,H(\mathbf{q}\;\|\;\boldsymbol{\pi})\Bigr\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​log⁡(er(n)/λ−er(1)/λr(n)−r(1))−er(n)/λ​r(1)−er(1)/λ​r(n)er(n)/λ−er(1)/λ+λ​log⁡λ−λ.\displaystyle=\lambda\log\!\Bigl(\tfrac{e^{r\_{(n)}/\lambda}-e^{r\_{(1)}/\lambda}}{r\_{(n)}-r\_{(1)}}\Bigr)-\frac{e^{r\_{(n)}/\lambda}r\_{(1)}-e^{r\_{(1)}/\lambda}r\_{(n)}}{e^{r\_{(n)}/\lambda}-e^{r\_{(1)}/\lambda}}+\lambda\log\lambda-\lambda. |  |

Moreover, for the (unique) indices {i⋆,j⋆}\{i^{\star},j^{\star}\} that attain the maximum and minimum of 𝐫\mathbf{r}, respectively, the optimal pair (𝛑⋆,𝐪⋆)(\boldsymbol{\pi}^{\star},\mathbf{q}^{\star}) are given by

|  |  |  |
| --- | --- | --- |
|  | πi⋆⋆=eri⋆/λ−erj⋆/λ−λ−1​(ri⋆−rj⋆)​erj⋆/λλ−1​(ri⋆−rj⋆)​(eri⋆/λ−erj⋆/λ),πj⋆⋆=1−πi⋆⋆,πk⋆=0(k∉{i⋆,j⋆})\pi\_{i^{\star}}^{\star}=\frac{\,e^{r\_{i^{\star}}/\lambda}-e^{r\_{j^{\star}}/\lambda}-\lambda^{-1}(r\_{i^{\star}}-r\_{j^{\star}})e^{r\_{j^{\star}}/\lambda}\,}{\lambda^{-1}(r\_{i^{\star}}-r\_{j^{\star}})\,(e^{r\_{i^{\star}}/\lambda}-e^{r\_{j^{\star}}/\lambda})},\quad\pi\_{j^{\star}}^{\star}=1-\pi\_{i^{\star}}^{\star},\quad\pi\_{k}^{\star}=0\ \ (k\notin\{i^{\star},j^{\star}\}) |  |

and 𝐪⋆=𝛑⋆⊕𝛑⋆𝒞​[e𝐫/λ]\mathbf{q}^{\star}=\boldsymbol{\pi}^{\star}\oplus\_{\boldsymbol{\pi}^{\star}}\mathcal{C}[e^{\mathbf{r}/\lambda}].

Financially, we can interpret this problem as finding the two portfolios 𝝅,𝐪\boldsymbol{\pi},\mathbf{q} whose holdings differ maximally in their average log returns when subject to a relative entropy penalization. The optimal pair has support on the two most extreme returns and 𝐪⋆\mathbf{q}^{\star} tilts away from 𝝅⋆\boldsymbol{\pi}^{\star} towards the rescaled return profile λ−1​𝐫\lambda^{-1}\mathbf{r}.

Next, we link the excess growth rate γ​(𝝅,⋅)\gamma(\boldsymbol{\pi},\cdot) to the constrained optimization problem ([4.4](https://arxiv.org/html/2510.25740v1#S4.E4 "In 4.1. Motivations ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) through a perspective transformation.171717The *perspective* of a function f​(𝐫)f(\mathbf{r}) is given by 𝔭​(λ,𝐫):=λ​f​(𝐫/λ)\mathfrak{p}(\lambda,\mathbf{r}):=\lambda f(\mathbf{r}/\lambda) for λ∈(0,∞)\lambda\in(0,\infty). When ff is convex (concave), 𝔭:(0,∞)×ℝn→ℝ\mathfrak{p}:(0,\infty)\times\mathbb{R}^{n}\to\mathbb{R} is *jointly* convex (concave) (cf. [[12](https://arxiv.org/html/2510.25740v1#bib.bib12), Section 3.2.6]). The perspective of 𝐫↦γ​(𝝅,𝐫)\mathbf{r}\mapsto\gamma(\boldsymbol{\pi},\mathbf{r}) has already appeared in ([4.6](https://arxiv.org/html/2510.25740v1#S4.E6 "In 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")). For a radius η≥0\eta\geq 0 we first define the objective

|  |  |  |  |
| --- | --- | --- | --- |
| (4.7) |  | Φη​(𝐫):=sup𝐪∈Δn:H​(𝐪∥𝝅)≤η⟨𝐪−𝝅,𝐫⟩.\Phi\_{\eta}(\mathbf{r}):=\sup\_{\mathbf{q}\in\Delta\_{n}:\ H(\mathbf{q}\;\|\;\boldsymbol{\pi})\leq\eta}\,\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle. |  |

###### Lemma 4.6 (Perspective duality).

Fix n≥2n\geq 2 and 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n}. For η≥0\eta\geq 0 and 𝐫∈ℝn\mathbf{r}\in\mathbb{R}^{n}

|  |  |  |  |
| --- | --- | --- | --- |
| (4.8) |  | Φη​(𝐫)=infλ>0{λ​γ​(𝝅,1λ​𝐫)+η​λ},\Phi\_{\eta}(\mathbf{r})=\inf\_{\lambda>0}\Bigl\{\lambda\,\gamma\Bigl(\boldsymbol{\pi},\frac{1}{\lambda}\mathbf{r}\Bigr)+\eta\,\lambda\Bigr\}, |  |

with the convention

|  |  |  |  |
| --- | --- | --- | --- |
| (4.9) |  | λ​γ​(𝝅,1λ​𝐫)→maxi∈supp⁡(𝝅)⁡ri−⟨𝝅,𝐫⟩asλ↓0.\lambda\,\gamma\Bigl(\boldsymbol{\pi},\frac{1}{\lambda}\mathbf{r}\Bigr)\rightarrow\max\_{i\in\operatorname{supp}(\boldsymbol{\pi})}r\_{i}-\langle\boldsymbol{\pi},\mathbf{r}\rangle\quad\text{as}\quad\lambda\downarrow 0. |  |

###### Proof.

Consider the (partial) Lagrangian

|  |  |  |
| --- | --- | --- |
|  | ℒ​(𝐪,λ):=⟨𝐪−𝝅,𝐫⟩−λ​(H​(𝐪∥𝝅)−η),𝐪∈Δn,λ>0.\mathcal{L}(\mathbf{q},\lambda):=\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle-\lambda\bigl(H(\mathbf{q}\;\|\;\boldsymbol{\pi})-\eta\bigr),\qquad\mathbf{q}\in\Delta\_{n},\ \lambda>0. |  |

For each fixed λ>0\lambda>0, the map 𝐪↦ℒ​(𝐪,λ)\mathbf{q}\mapsto\mathcal{L}(\mathbf{q},\lambda) is continuous and concave on the compact convex set
Δn\Delta\_{n}, while for fixed 𝐪\mathbf{q} the map
λ↦ℒ​(𝐪,λ)\lambda\mapsto\mathcal{L}(\mathbf{q},\lambda) is affine. Hence Sion’s minimax theorem yields

|  |  |  |
| --- | --- | --- |
|  | Φη​(𝐫)=sup𝐪∈Δninfλ>0ℒ​(𝐪,λ)=infλ>0sup𝐪∈Δnℒ​(𝐪,λ).\Phi\_{\eta}(\mathbf{r})=\sup\_{\mathbf{q}\in\Delta\_{n}}\inf\_{\lambda>0}\mathcal{L}(\mathbf{q},\lambda)=\inf\_{\lambda>0}\sup\_{\mathbf{q}\in\Delta\_{n}}\mathcal{L}(\mathbf{q},\lambda). |  |

If λ>0\lambda>0, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.10) |  | sup𝐪∈Δnℒ​(𝐪,λ)=λ​sup𝐪∈Δn{⟨𝐪−𝝅,𝐫λ⟩−H​(𝐪∥𝝅)}+η​λ.\sup\_{\mathbf{q}\in\Delta\_{n}}\mathcal{L}(\mathbf{q},\lambda)=\lambda\sup\_{\mathbf{q}\in\Delta\_{n}}\Bigl\{\Bigl\langle\mathbf{q}-\boldsymbol{\pi},\frac{\mathbf{r}}{\lambda}\Bigr\rangle-H(\mathbf{q}\;\|\;\boldsymbol{\pi})\Bigr\}+\eta\lambda. |  |

By Theorem [2.7](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem7 "Proposition 2.7 (Variational representation). ‣ 2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate") the inner supremum in ([4.10](https://arxiv.org/html/2510.25740v1#S4.E10 "In 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) equals γ​(𝝅,𝐫/λ)\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda), giving

|  |  |  |
| --- | --- | --- |
|  | sup𝐪∈Δnℒ​(𝐪,λ)=λ​γ​(𝝅,𝐫/λ)+η​λ.\sup\_{\mathbf{q}\in\Delta\_{n}}\mathcal{L}(\mathbf{q},\lambda)=\lambda\,\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda)+\eta\lambda. |  |

Combining the case λ>0\lambda>0 with the well-known fact that λ​log​∑iπi​eri/λ\lambda\log\sum\_{i}\pi\_{i}e^{r\_{i}/\lambda}
approximates maxi:πi>0⁡ri\max\_{i:\pi\_{i}>0}r\_{i} as λ↓0\lambda\downarrow 0 yields
([4.8](https://arxiv.org/html/2510.25740v1#S4.E8 "In Lemma 4.6 (Perspective duality). ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) and ([4.9](https://arxiv.org/html/2510.25740v1#S4.E9 "In Lemma 4.6 (Perspective duality). ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")).
∎

The maximizer of this constrained optimization can be characterized as follows.

###### Lemma 4.7.

Set ℳ𝛑​(𝐫):=arg⁡maxi∈supp⁡(𝛑)⁡ri\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r}):=\arg\max\_{i\in\operatorname{supp}(\boldsymbol{\pi})}r\_{i} and define η¯​(⋅)\overline{\eta}(\cdot) and 𝐪​(⋅)\mathbf{q}(\cdot) through

|  |  |  |
| --- | --- | --- |
|  | η¯​(𝐫):=−log⁡(∑j∈ℳ𝝅​(𝐫)πj),qi​(𝐫)=πi​exp⁡(ri)∑j=1nπj​exp⁡(rj)=𝝅⊕𝝅𝒞​[e𝐫].\overline{\eta}(\mathbf{r}):=-\log\left(\sum\_{j\in\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r})}\pi\_{j}\right),\quad q\_{i}(\mathbf{r})=\frac{\pi\_{i}\exp(r\_{i})}{\sum\_{j=1}^{n}\pi\_{j}\exp(r\_{j})}=\boldsymbol{\pi}\oplus\_{\boldsymbol{\pi}}\mathcal{C}[e^{\mathbf{r}}]. |  |

Then:

1. (a)

   If 0≤η<η¯​(𝐫)0\leq\eta<\overline{\eta}(\mathbf{r}), the infimum in ([4.8](https://arxiv.org/html/2510.25740v1#S4.E8 "In Lemma 4.6 (Perspective duality). ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) is attained at any λ⋆>0\lambda^{\star}>0 satisfying181818The case η=0\eta=0 is solved by setting λ⋆=∞\lambda^{\star}=\infty which we identify with 𝐪⋆=limλ↑∞𝐪​(𝐫/λ)=𝝅\mathbf{q}^{\star}=\lim\_{\lambda\uparrow\infty}\mathbf{q}(\mathbf{r}/\lambda)=\boldsymbol{\pi}. H​(𝐪​(𝐫/λ⋆)∥𝝅)=ηH(\mathbf{q}(\mathbf{r}/\lambda^{\star})\;\|\;\boldsymbol{\pi})=\eta and the maximizer in ([4.7](https://arxiv.org/html/2510.25740v1#S4.E7 "In 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) is given by 𝐪⋆=𝐪​(𝐫/λ⋆)\mathbf{q}^{\star}=\mathbf{q}(\mathbf{r}/\lambda^{\star}).
2. (b)

   If η≥η¯​(𝐫)\eta\geq\overline{\eta}(\mathbf{r}) then the infimum in ([4.8](https://arxiv.org/html/2510.25740v1#S4.E8 "In Lemma 4.6 (Perspective duality). ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) is achieved in the limit λ↓0\lambda\downarrow 0, and any
   𝐪⋆\mathbf{q}^{\star} supported on ℳ𝝅​(𝐫)\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r}) with H​(𝐪⋆∥𝝅)≤ηH(\mathbf{q}^{\star}\|\boldsymbol{\pi})\leq\eta is optimal for ([4.7](https://arxiv.org/html/2510.25740v1#S4.E7 "In 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")). In particular, the distribution

   |  |  |  |
   | --- | --- | --- |
   |  | 𝐪i⋆=πi∑j∈ℳ𝝅​(𝐫)πj​ 1{i∈ℳ𝝅​(𝐫)}=limλ↓0qi​(𝐫/λ)\mathbf{q}^{\star}\_{i}=\frac{\pi\_{i}}{\sum\_{j\in\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r})}\pi\_{j}}\,\mathbf{1}\_{\{i\in\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r})\}}=\lim\_{\lambda\downarrow 0}q\_{i}(\mathbf{r}/\lambda) |  |

   satisfies
   H​(𝐪⋆∥𝝅)=η¯​(𝐫)H(\mathbf{q}^{\star}\|\boldsymbol{\pi})=\overline{\eta}(\mathbf{r}).

###### Proof.

First, observe that 𝐪​(𝐫/λ)=∇𝐫γ​(𝝅,𝐫/λ)+𝝅\mathbf{q}(\mathbf{r}/\lambda)=\nabla\_{\mathbf{r}}\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda)+\boldsymbol{\pi} and define for λ>0\lambda>0

|  |  |  |
| --- | --- | --- |
|  | φ𝐫,η​(λ):=λ​γ​(𝝅,𝐫/λ)+η​λ.\varphi\_{\mathbf{r},\eta}(\lambda):=\lambda\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda)+\eta\lambda. |  |

Then from Lemma [4.6](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem6 "Lemma 4.6 (Perspective duality). ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") Φη​(𝐫)=infλ≥0φ𝐫,η​(λ)\Phi\_{\eta}(\mathbf{r})=\inf\_{\lambda\geq 0}\varphi\_{\mathbf{r},\eta}(\lambda), and from Theorem [2.7](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem7 "Proposition 2.7 (Variational representation). ‣ 2.2. Free energy and variational representation ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate"),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.11) |  | γ​(𝝅,𝐫/λ)\displaystyle\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda) | =⟨𝐪​(𝐫/λ)−𝝅,𝐫/λ⟩−H​(𝐪​(𝐫/λ)∥𝝅)\displaystyle=\langle\mathbf{q}(\mathbf{r}/\lambda)-\boldsymbol{\pi},\mathbf{r}/\lambda\rangle-H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨∇𝐫γ​(𝝅,𝐫/λ),𝐫/λ⟩−H​(𝐪​(𝐫/λ)∥𝝅).\displaystyle=\langle\nabla\_{\mathbf{r}}\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda),\mathbf{r}/\lambda\rangle-H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi}). |  |

Differentiating and using ([4.11](https://arxiv.org/html/2510.25740v1#S4.E11 "In 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ𝐫,η′​(λ)\displaystyle\varphi^{\prime}\_{\mathbf{r},\eta}(\lambda) | =γ​(𝝅,𝐫/λ)−⟨∇𝐫γ​(𝝅,𝐫/λ),𝐫/λ⟩+η=η−H​(𝐪​(𝐫/λ)∥𝝅),\displaystyle=\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda)-\Bigl\langle\nabla\_{\mathbf{r}}\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda),\mathbf{r}/\lambda\Bigr\rangle+\eta=\eta-H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | φ𝐫,η′′​(λ)\displaystyle\varphi^{\prime\prime}\_{\mathbf{r},\eta}(\lambda) | =−∂λH​(𝐪​(𝐫/λ)∥𝝅).\displaystyle=-\partial\_{\lambda}H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi}). |  |

Since γ​(𝝅,⋅)\gamma(\boldsymbol{\pi},\cdot) is convex, so is its perspective g𝝅​(λ,𝐫):=λ​γ​(𝝅,𝐫/λ)g\_{\boldsymbol{\pi}}(\lambda,\mathbf{r}):=\lambda\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda) (cf. [[12](https://arxiv.org/html/2510.25740v1#bib.bib12), Section 3.2.6]). In particular, λ↦λ​γ​(𝝅,𝐫/λ)\lambda\mapsto\lambda\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda), and by extension φ𝐫,η​(⋅)\varphi\_{\mathbf{r},\eta}(\cdot), is convex. We may conclude that

|  |  |  |
| --- | --- | --- |
|  | −∂λH​(𝐪​(𝐫/λ)∥𝝅)=φ𝐫,η′′​(λ)≥0-\partial\_{\lambda}H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi})=\varphi^{\prime\prime}\_{\mathbf{r},\eta}(\lambda)\geq 0 |  |

from which it follows that λ↦H​(𝐪​(𝐫/λ)∥𝝅)\lambda\mapsto H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi}) is decreasing.

As λ↓0\lambda\downarrow 0, the distribution 𝐪​(𝐫/λ)\mathbf{q}(\mathbf{r}/\lambda) concentrates on the set ℳ𝝅​(𝐫)\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r}) with the limit

|  |  |  |
| --- | --- | --- |
|  | qi​(𝐫/λ)→πi∑j∈ℳ𝝅​(𝐫)πj​ 1{i∈ℳ𝝅​(𝐫)}q\_{i}(\mathbf{r}/\lambda)\rightarrow\frac{\pi\_{i}}{\sum\_{j\in\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r})}\pi\_{j}}\,\mathbf{1}\_{\{i\in\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r})\}} |  |

whereas qi​(𝐫/λ)→πiq\_{i}(\mathbf{r}/\lambda)\rightarrow\pi\_{i} as λ→∞\lambda\to\infty.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | limλ↓0H(𝐪(𝐫/λ)∥𝝅)=−log(∑j∈ℳ𝝅​(𝐫)πj)=:η¯(𝐫),limλ↑∞H(𝐪(𝐫/λ)∥𝝅)=0.\lim\_{\lambda\downarrow 0}H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi})=-\log\!\Bigl(\sum\_{j\in\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r})}\pi\_{j}\Bigr)=:\overline{\eta}(\mathbf{r}),\qquad\lim\_{\lambda\uparrow\infty}H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi})=0. |  |

We consider now two cases. If 𝐫\mathbf{r} is constant on the support of 𝝅\boldsymbol{\pi} then η¯​(𝐫)=0\overline{\eta}(\mathbf{r})=0 and 𝐪​(𝐫/λ)≡𝝅\mathbf{q}(\mathbf{r}/\lambda)\equiv\boldsymbol{\pi}. In particular, φ′​(λ)=η≥0\varphi^{\prime}(\lambda)=\eta\geq 0 for all λ>0\lambda>0 and the minimum can be attained by sending λ↓0\lambda\downarrow 0.

Suppose instead that 𝐫\mathbf{r} is not constant on the support of 𝝅\boldsymbol{\pi} so that η¯​(𝐫)>0\overline{\eta}(\mathbf{r})>0. Because φ′​(λ)=η−H​(𝐪​(𝐫/λ)∥𝝅)\varphi^{\prime}(\lambda)=\eta-H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi}) and H​(𝐪​(𝐫/λ)∥𝝅)∈[0,η¯​(𝐫)]H(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi})\in[0,\overline{\eta}(\mathbf{r})] decreases in λ\lambda, there exists a λ⋆≥0\lambda^{\star}\geq 0 with φ′​(λ⋆)=0\varphi^{\prime}(\lambda^{\star})=0 (equivalently, H​(𝐪​(𝐫/λ)∥𝝅)=ηH(\mathbf{q}(\mathbf{r}/\lambda)\;\|\;\boldsymbol{\pi})=\eta) if and only if 0≤η<η¯​(𝐫)0\leq\eta<\overline{\eta}(\mathbf{r}). If η≥η¯​(𝐫)\eta\geq\overline{\eta}(\mathbf{r}) then φ′​(λ)≥0\varphi^{\prime}(\lambda)\geq 0 for all λ>0\lambda>0 and the infimum of φ\varphi is achieved in the limit λ↓0\lambda\downarrow 0. In this case, Φη​(𝐫)=maxi∈supp⁡(𝝅)⁡ri−⟨𝝅,𝐫⟩\Phi\_{\eta}(\mathbf{r})=\max\_{i\in\operatorname{supp}(\boldsymbol{\pi})}r\_{i}-\langle\boldsymbol{\pi},\mathbf{r}\rangle, and any 𝐪⋆\mathbf{q}^{\star} supported on ℳ𝝅​(𝐫)\mathcal{M}\_{\boldsymbol{\pi}}(\mathbf{r}) with
H​(𝐪⋆∥𝝅)≤ηH(\mathbf{q}^{\star}\;\|\;\boldsymbol{\pi})\leq\eta is optimal.
∎

###### Remark 4.8.

It is not hard to check that the solution λ⋆\lambda^{\star} to H​(𝐪​(𝐫/λ⋆)∥𝛑)=ηH(\mathbf{q}(\mathbf{r}/\lambda^{\star})\;\|\;\boldsymbol{\pi})=\eta in Lemma [4.7](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")(a) is unique as long as 𝐫\mathbf{r} is not constant on supp⁡(𝛑)\operatorname{supp}(\boldsymbol{\pi}).

We can now use the connections developed in Lemmas [4.6](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem6 "Lemma 4.6 (Perspective duality). ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")–[4.7](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") with the excess growth rate maximization in Theorem [4.3](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2. Maximizing the excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") to solve the constrained optimization problem in ([4.4](https://arxiv.org/html/2510.25740v1#S4.E4 "In 4.1. Motivations ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")). We formalize this final link in the following proposition.

###### Proposition 4.9.

Let 𝐫∈ℝn\mathbf{r}\in\mathbb{R}^{n} have n≥2n\geq 2 distinct coordinates. Then for any η≥0\eta\geq 0

|  |  |  |
| --- | --- | --- |
|  | sup(𝝅,𝐪)∈Δn×Δn:H​(𝐪∥𝝅)≤η⟨𝐪−𝝅,𝐫⟩\displaystyle\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}:\ H(\mathbf{q}\;\|\;\boldsymbol{\pi})\leq\eta}\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (4.12) |  | =infλ>0{λ​log⁡(er(n)/λ−er(1)/λr(n)−r(1))−er(n)/λ​r(1)−er(1)/λ​r(n)er(n)/λ−er(1)/λ+λ​log⁡λ+λ​(η−1)}.\displaystyle=\inf\_{\lambda>0}\Bigg\{\lambda\log\!\Bigl(\tfrac{e^{r\_{(n)}/\lambda}-e^{r\_{(1)}/\lambda}}{r\_{(n)}-r\_{(1)}}\Bigr)-\frac{e^{r\_{(n)}/\lambda}r\_{(1)}-e^{r\_{(1)}/\lambda}r\_{(n)}}{e^{r\_{(n)}/\lambda}-e^{r\_{(1)}/\lambda}}+\lambda\log\lambda+\lambda(\eta-1)\Bigg\}. |  |

Moreover, for the (unique) indices {i⋆,j⋆}\{i^{\star},j^{\star}\} that attain the maximum and minimum of 𝐫\mathbf{r}, respectively, define the pair (𝛑​(λ),𝐪​(λ))(\boldsymbol{\pi}(\lambda),\mathbf{q}(\lambda)) by

|  |  |  |
| --- | --- | --- |
|  | πi⋆​(λ)=eri⋆/λ−erj⋆/λ−λ−1​(ri⋆−rj⋆)​erj⋆/λλ−1​(ri⋆−rj⋆)​(eri⋆/λ−erj⋆/λ),πj⋆​(λ)=1−πi⋆​(λ),\pi\_{i^{\star}}(\lambda)=\frac{\,e^{r\_{i^{\star}}/\lambda}-e^{r\_{j^{\star}}/\lambda}-\lambda^{-1}(r\_{i^{\star}}-r\_{j^{\star}})e^{r\_{j^{\star}}/\lambda}\,}{\lambda^{-1}(r\_{i^{\star}}-r\_{j^{\star}})\,(e^{r\_{i^{\star}}/\lambda}-e^{r\_{j^{\star}}/\lambda})},\quad\pi\_{j^{\star}}(\lambda)=1-\pi\_{i^{\star}}(\lambda), |  |

πk​(λ)=0\pi\_{k}(\lambda)=0 for (k∉{i⋆,j⋆})(k\notin\{i^{\star},j^{\star}\}), and 𝐪​(λ)=𝛑​(λ)⊕𝛑​(λ)𝒞​[e𝐫/λ]\mathbf{q}(\lambda)=\boldsymbol{\pi}(\lambda)\oplus\_{\boldsymbol{\pi}(\lambda)}\mathcal{C}[e^{\mathbf{r}/\lambda}]. For any λ⋆\lambda^{\star} solving191919We are assured of the existence of at least one solution. If η=0\eta=0 we identify the solution with the limit limλ↑∞𝛑​(λ)=limλ↑∞𝐪​(λ)=12​(𝐞i⋆+𝐞j⋆)\lim\_{\lambda\uparrow\infty}\boldsymbol{\pi}(\lambda)=\lim\_{\lambda\uparrow\infty}\mathbf{q}(\lambda)=\frac{1}{2}(\mathbf{e}\_{i^{\star}}+\mathbf{e}\_{j^{\star}}).

|  |  |  |
| --- | --- | --- |
|  | H​(𝐪​(λ⋆)∥𝝅​(λ⋆))=ηH(\mathbf{q}(\lambda^{\star})\;\|\;\boldsymbol{\pi}(\lambda^{\star}))=\eta |  |

the choice 𝛑⋆=𝛑​(λ⋆)\boldsymbol{\pi}^{\star}=\boldsymbol{\pi}(\lambda^{\star}) and 𝐪⋆=𝐪​(λ⋆)\mathbf{q}^{\star}=\mathbf{q}(\lambda^{\star}) is optimal.

###### Proof.

By using Lemma [4.6](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem6 "Lemma 4.6 (Perspective duality). ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") we can rewrite the constrained joint maximization of ([4.4](https://arxiv.org/html/2510.25740v1#S4.E4 "In 4.1. Motivations ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(𝝅,𝐪)∈Δn×Δn:H​(𝐪∥𝝅)≤η⟨𝐪−𝝅,𝐫⟩\displaystyle\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}:\ H(\mathbf{q}\;\|\;\boldsymbol{\pi})\leq\eta}\left\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\right\rangle | =sup𝝅∈Δnsup𝐪∈Δn:H​(𝐪∥𝝅)≤η⟨𝐪−𝝅,𝐫⟩\displaystyle=\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}\sup\_{\mathbf{q}\in\Delta\_{n}:\ H(\mathbf{q}\;\|\;\boldsymbol{\pi})\leq\eta}\,\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =sup𝝅∈Δninfλ>0{λ​γ​(𝝅,𝐫/λ)+η​λ}\displaystyle=\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}\inf\_{\lambda>0}\Bigl\{\lambda\,\gamma\Bigl(\boldsymbol{\pi},\mathbf{r}/\lambda\Bigr)+\eta\,\lambda\Bigr\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =infλ>0{λ​sup𝝅∈Δnγ​(𝝅,𝐫/λ)+η​λ}.\displaystyle=\inf\_{\lambda>0}\Bigl\{\lambda\,\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}\gamma\Bigl(\boldsymbol{\pi},\mathbf{r}/\lambda\Bigr)+\eta\,\lambda\Bigr\}. |  |

The interchange of inf{…}\inf\{\dots\} and sup{…}\sup\{\dots\} is justified by Sion’s minimax theorem as Δn\Delta\_{n} is convex and compact, (0,∞)(0,\infty) is convex, 𝝅↦γ​(𝝅,𝐫)\boldsymbol{\pi}\mapsto\gamma(\boldsymbol{\pi},\mathbf{r}) is concave, and λ↦λ​γ​(𝝅,𝐫/λ)\lambda\mapsto\lambda\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda) is convex (cf. [[12](https://arxiv.org/html/2510.25740v1#bib.bib12), Section 3.2.6]).

To see the characterization of the solution, we observe from ([4.6](https://arxiv.org/html/2510.25740v1#S4.E6 "In 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) and Proposition [4.5](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​sup𝝅∈Δnγ​(𝝅,𝐫/λ)\displaystyle\lambda\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}\gamma(\boldsymbol{\pi},\mathbf{r}/\lambda) | =sup(𝝅,𝐪)∈Δn×Δn{⟨𝐪−𝝅,𝐫⟩−λ​H​(𝐪∥𝝅)}\displaystyle=\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}}\Bigl\{\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\rangle-\lambda\,H(\mathbf{q}\;\|\;\boldsymbol{\pi})\Bigr\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨𝐪​(λ)−𝝅​(λ),𝐫⟩−λ​H​(𝐪​(λ)∥𝝅​(λ))\displaystyle=\langle\mathbf{q}(\lambda)-\boldsymbol{\pi}(\lambda),\mathbf{r}\rangle-\lambda\,H(\mathbf{q}(\lambda)\;\|\;\boldsymbol{\pi}(\lambda)) |  |

Proposition [4.5](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") also recovers ([4.12](https://arxiv.org/html/2510.25740v1#S4.E12 "In Proposition 4.9. ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")).
Define the functions

|  |  |  |
| --- | --- | --- |
|  | g​(𝝅,λ):=λ​γ​(𝝅,𝐫/λ),f​(λ):=sup𝝅∈Δng​(𝝅,λ)+η​λg(\boldsymbol{\pi},\lambda):=\lambda\gamma\Bigl(\boldsymbol{\pi},\mathbf{r}/\lambda\Bigr),\quad f(\lambda):=\sup\_{\boldsymbol{\pi}\in\Delta\_{n}}g(\boldsymbol{\pi},\lambda)+\eta\,\lambda |  |

so that

|  |  |  |
| --- | --- | --- |
|  | sup(𝝅,𝐪)∈Δn×Δn:H​(𝐪∥𝝅)≤η⟨𝐪−𝝅,𝐫⟩=infλ>0f​(λ).\sup\_{(\boldsymbol{\pi},\mathbf{q})\in\Delta\_{n}\times\Delta\_{n}:\ H(\mathbf{q}\;\|\;\boldsymbol{\pi})\leq\eta}\left\langle\mathbf{q}-\boldsymbol{\pi},\mathbf{r}\right\rangle=\inf\_{\lambda>0}f(\lambda). |  |

Observe that since λ↦λ​γ​(𝝅,𝐫/λ)\lambda\mapsto\lambda\gamma\Bigl(\boldsymbol{\pi},\mathbf{r}/\lambda\Bigr) is convex for each 𝝅\boldsymbol{\pi}, g​(𝝅,⋅)g(\boldsymbol{\pi},\cdot) is convex and (as a maximum of convex functions) so is f​(λ)f(\lambda). Moreover, since 𝐫\mathbf{r} has distinct entries we are assured that 𝝅​(λ)\boldsymbol{\pi}(\lambda) is the unique optimizer. Since Δn\Delta\_{n} is compact, by Danskin’s Theorem (cf. [[7](https://arxiv.org/html/2510.25740v1#bib.bib7), Proposition A.3.2])

|  |  |  |
| --- | --- | --- |
|  | f′​(λ)=∂λg​(𝝅​(λ),λ)+η.f^{\prime}(\lambda)=\partial\_{\lambda}g(\boldsymbol{\pi}(\lambda),\lambda)+\eta. |  |

Repeating the argument in Lemma [4.7](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.3. Variational interpretation ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") we see that

|  |  |  |
| --- | --- | --- |
|  | ∂λg​(𝝅​(λ),λ)=−H​(𝐪​(λ)∥𝝅​(λ)).\partial\_{\lambda}g(\boldsymbol{\pi}(\lambda),\lambda)=-H(\mathbf{q}(\lambda)\;\|\;\boldsymbol{\pi}(\lambda)). |  |

Thus, to minimize f​(λ)f(\lambda) we search for a solution λ⋆\lambda^{\star} of f′​(λ⋆)=0f^{\prime}(\lambda^{\star})=0, which is equivalently given by the solution to

|  |  |  |
| --- | --- | --- |
|  | H​(𝐪​(λ⋆)∥𝝅​(λ⋆))=η.H(\mathbf{q}(\lambda^{\star})\;\|\;\boldsymbol{\pi}(\lambda^{\star}))=\eta. |  |

Moreover, since f​(λ)f(\lambda) is convex we have f′′​(λ)≥0f^{\prime\prime}(\lambda)\geq 0 and we conclude,

|  |  |  |
| --- | --- | --- |
|  | 0≥−f′′​(λ)=∂λH​(𝐪​(λ)∥𝝅​(λ)).0\geq-f^{\prime\prime}(\lambda)=\partial\_{\lambda}H(\mathbf{q}(\lambda)\;\|\;\boldsymbol{\pi}(\lambda)). |  |

That is, λ↦H​(𝐪​(λ)∥𝝅​(λ))\lambda\mapsto H(\mathbf{q}(\lambda)\;\|\;\boldsymbol{\pi}(\lambda)) is continuous and decreasing. As λ↑∞\lambda\uparrow\infty we see that 𝝅​(λ)→12​(𝐞i⋆+𝐞j⋆)\boldsymbol{\pi}(\lambda)\to\frac{1}{2}(\mathbf{e}\_{i^{\star}}+\mathbf{e}\_{j^{\star}}), while as λ↓0\lambda\downarrow 0, 𝝅​(λ)→𝐞j⋆\boldsymbol{\pi}(\lambda)\to\mathbf{e}\_{j^{\star}}. In the limit λ↑∞\lambda\uparrow\infty we find that similarly 𝐪​(λ)→12​(𝐞i⋆+𝐞j⋆)\mathbf{q}(\lambda)\to\frac{1}{2}(\mathbf{e}\_{i^{\star}}+\mathbf{e}\_{j^{\star}}) while as λ↓0\lambda\downarrow 0 we have 𝐪​(λ)→𝐞i⋆\mathbf{q}(\lambda)\to\mathbf{e}\_{i^{\star}}. Hence

|  |  |  |
| --- | --- | --- |
|  | limλ↓0H​(𝐪​(λ)∥𝝅​(λ))=∞,limλ↑∞H​(𝐪​(λ)∥𝝅​(λ))=0.\lim\_{\lambda\downarrow 0}H(\mathbf{q}(\lambda)\;\|\;\boldsymbol{\pi}(\lambda))=\infty,\qquad\lim\_{\lambda\uparrow\infty}H(\mathbf{q}(\lambda)\;\|\;\boldsymbol{\pi}(\lambda))=0. |  |

We conclude that there must be a solution for any 0≤η<∞0\leq\eta<\infty which completes the proof.
∎

### 4.4. Maximizing the expected excess growth rate

We now turn to the optimization of the *expected* excess growth rate introduced in ([4.1](https://arxiv.org/html/2510.25740v1#S4.E1 "In 4. Optimization ‣ A mathematical study of the excess growth rate")).
Let 𝐑:=e𝐫∈ℝ+n\mathbf{R}:=e^{\mathbf{r}}\in\mathbb{R}\_{+}^{n} and 𝐦:=𝔼​[𝐫]\mathbf{m}:=\mathbb{E}[\mathbf{r}].
To distinguish this problem from the deterministic objective γ​(𝝅,𝐫)\gamma(\boldsymbol{\pi},\mathbf{r}) of Section [4.2](https://arxiv.org/html/2510.25740v1#S4.SS2 "4.2. Maximizing the excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate"), we define the function J:Δn→ℝJ:\Delta\_{n}\to\mathbb{R} through

|  |  |  |  |
| --- | --- | --- | --- |
| (4.13) |  | J​(𝝅):=𝔼​[γ​(𝝅,𝐫)]=𝔼​[log⁡(⟨𝝅,𝐑⟩)]−⟨𝝅,𝐦⟩.J(\boldsymbol{\pi}):=\mathbb{E}\Big[\gamma(\boldsymbol{\pi},\mathbf{r})\Big]=\mathbb{E}\Big[\log\left(\langle\boldsymbol{\pi},\mathbf{R}\rangle\right)\Big]-\langle\boldsymbol{\pi},\mathbf{m}\rangle. |  |

To ensure JJ is well defined and finite on Δn\Delta\_{n}, we impose mild integrability assumptions on 𝐫\mathbf{r} (stated below).

###### Assumption 4.10.

Let 𝐫\mathbf{r} be an ℝn\mathbb{R}^{n}–valued random vector such that 𝔼​[|ri|]<∞\mathbb{E}[|r\_{i}|]<\infty for all 1≤i≤n1\leq i\leq n.

Under Assumption [4.10](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem10 "Assumption 4.10. ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") we are assured the finiteness of the objective (i.e., J​(𝝅)∈ℝJ(\boldsymbol{\pi})\in\mathbb{R}) since

|  |  |  |
| --- | --- | --- |
|  | J​(𝝅)≤𝔼​[maxi⁡{ri}]−⟨𝝅,𝐦⟩≤2​∑i=1n𝔼​[|ri|]<∞J(\boldsymbol{\pi})\leq\mathbb{E}\left[\max\_{i}\{r\_{i}\}\right]-\langle\boldsymbol{\pi},\mathbf{m}\rangle\leq 2\sum\_{i=1}^{n}\mathbb{E}\left[|r\_{i}|\right]<\infty |  |

and by choosing any i∈supp⁡(𝝅)i\in\operatorname{supp}(\boldsymbol{\pi}),

|  |  |  |
| --- | --- | --- |
|  | J​(𝝅)≥log⁡(πi)+𝔼​[ri]−∑j=1n𝔼​[|rj|]≥−2​∑j=1n𝔼​[|rj|]>−∞.J(\boldsymbol{\pi})\geq\log(\pi\_{i})+\mathbb{E}[r\_{i}]-\sum\_{j=1}^{n}\mathbb{E}\left[|r\_{j}|\right]\geq-2\sum\_{j=1}^{n}\mathbb{E}\left[|r\_{j}|\right]>-\infty. |  |

Our main result is the following necessary and sufficient first-order condition.

###### Theorem 4.11 (First-order condition).

Under Assumption [4.10](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem10 "Assumption 4.10. ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate"), a portfolio 𝛑⋆∈Δn\boldsymbol{\pi}^{\star}\in\Delta\_{n} maximizes J​(⋅)J(\cdot) if and only if for every 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
| (4.14) |  | 𝔼​[⟨𝝅,𝐑⟩⟨𝝅⋆,𝐑⟩]≤ 1+⟨𝝅−𝝅⋆,𝐦⟩,\mathbb{E}\left[\frac{\langle\boldsymbol{\pi},\mathbf{R}\rangle}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right]\ \leq\ 1+\langle\boldsymbol{\pi}-\boldsymbol{\pi}^{\star},\mathbf{m}\rangle, |  |

with equality in ([4.14](https://arxiv.org/html/2510.25740v1#S4.E14 "In Theorem 4.11 (First-order condition). ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) whenever 𝛑\boldsymbol{\pi} is supported on supp⁡(𝛑⋆)\operatorname{supp}(\boldsymbol{\pi}^{\star}).

###### Proof.

Since γ\gamma is concave in 𝝅\boldsymbol{\pi}, we see that J​(𝝅)J(\boldsymbol{\pi}) is concave in 𝝅\boldsymbol{\pi}. In Lemma [B.2](https://arxiv.org/html/2510.25740v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Superdifferential set for the excess growth rate ‣ A mathematical study of the excess growth rate") of the Appendix we provide a direct characterization of the superdifferential set ∂Δn+J​(𝝅)\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}) (see Definition [B.1](https://arxiv.org/html/2510.25740v1#A2.Thmtheorem1 "Definition B.1. ‣ Appendix B Superdifferential set for the excess growth rate ‣ A mathematical study of the excess growth rate")). Our approach is slightly more technical but avoids imposing additional integrability conditions on 𝐫\mathbf{r}.

By standard convex analysis, we have that 𝝅⋆\boldsymbol{\pi}^{\star} is a maximizer of J​(⋅)J(\cdot) if and only if
𝟎∈∂Δn+J​(𝝅⋆)\mathbf{0}\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}^{\star}) (cf. [[57](https://arxiv.org/html/2510.25740v1#bib.bib57), Theorem 27.4]). That is, in view of Lemma [B.2](https://arxiv.org/html/2510.25740v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Superdifferential set for the excess growth rate ‣ A mathematical study of the excess growth rate"), there is a λ∈ℝ\lambda\in\mathbb{R} and a 𝝁∈ℝ+n\boldsymbol{\mu}\in\mathbb{R}^{n}\_{+} with μi=0\mu\_{i}=0 on supp⁡(𝝅⋆)\operatorname{supp}(\boldsymbol{\pi}^{\star}) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.15) |  | 𝔼​[𝐑⟨𝝅⋆,𝐑⟩]−𝐦−λ​𝟏+𝝁=𝟎,\mathbb{E}\left[\frac{\mathbf{R}}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right]-\mathbf{m}-\lambda\mathbf{1}+\boldsymbol{\mu}=\mathbf{0}, |  |

where 𝟎\mathbf{0} is the zero vector. Consequently, for any optimal 𝝅⋆\boldsymbol{\pi}^{\star}, we have the following inequality for all ii:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Ri⟨𝝅⋆,𝐑⟩]−mi≤λ\mathbb{E}\left[\frac{R\_{i}}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right]-m\_{i}\leq\lambda |  |

and moreover, equality holds for all i∈supp⁡(𝝅⋆)i\in\operatorname{supp}(\boldsymbol{\pi}^{\star}). Multiplying by the coordinates of an arbitrary portfolio 𝝅∈Δn\boldsymbol{\pi}\in\Delta\_{n} we get

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[πi​Ri⟨𝝅⋆,𝐑⟩]−πi​mi≤πi​λ.\mathbb{E}\left[\frac{\pi\_{i}R\_{i}}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right]-\pi\_{i}m\_{i}\leq\pi\_{i}\lambda. |  |

Summing over ii we get

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨𝝅,𝐑⟩⟨𝝅⋆,𝐑⟩]−⟨𝝅,𝐦⟩≤λ.\mathbb{E}\left[\frac{\langle\boldsymbol{\pi},\mathbf{R}\rangle}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right]-\langle\boldsymbol{\pi},\mathbf{m}\rangle\leq\lambda. |  |

In particular, if supp⁡(𝝅)⊆supp⁡(𝝅∗)\operatorname{supp}(\boldsymbol{\pi})\subseteq\operatorname{supp}(\boldsymbol{\pi}^{\*}) then equality holds at all non-zero coordinates and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨𝝅,𝐑⟩⟨𝝅⋆,𝐑⟩]−⟨𝝅,𝐦⟩=λ,supp⁡(𝝅)⊆supp⁡(𝝅⋆).\mathbb{E}\left[\frac{\langle\boldsymbol{\pi},\mathbf{R}\rangle}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right]-\langle\boldsymbol{\pi},\mathbf{m}\rangle=\lambda,\qquad\operatorname{supp}(\boldsymbol{\pi})\subseteq\operatorname{supp}(\boldsymbol{\pi}^{\star}). |  |

Taking 𝝅≡𝝅⋆\boldsymbol{\pi}\equiv\boldsymbol{\pi}^{\star} in the above we see that

|  |  |  |
| --- | --- | --- |
|  | 1−⟨𝝅⋆,𝐦⟩=λ.1-\langle\boldsymbol{\pi}^{\star},\mathbf{m}\rangle=\lambda. |  |

The necessity of ([4.14](https://arxiv.org/html/2510.25740v1#S4.E14 "In Theorem 4.11 (First-order condition). ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) holding at any optimizer 𝝅⋆\boldsymbol{\pi}^{\star} (with equality if supp⁡(𝝅)⊆supp⁡(𝝅⋆)\operatorname{supp}(\boldsymbol{\pi})\subseteq\operatorname{supp}(\boldsymbol{\pi}^{\star})) follows.

Sufficiency can be seen by choosing 𝝅=𝐞j∈Δn\boldsymbol{\pi}=\mathbf{e}\_{j}\in\Delta\_{n} for j=1,…,nj=1,\dots,n and defining

|  |  |  |  |
| --- | --- | --- | --- |
| (4.16) |  | μj=1+⟨𝐞j−𝝅⋆,𝐦⟩−𝔼​[⟨𝐞j,𝐑⟩⟨𝝅⋆,𝐑⟩]≥0,j=1,…,n.\mu\_{j}=1+\langle\mathbf{e}\_{j}-\boldsymbol{\pi}^{\star},\mathbf{m}\rangle-\mathbb{E}\left[\frac{\langle\mathbf{e}\_{j},\mathbf{R}\rangle}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right]\geq 0,\quad j=1,\dots,n. |  |

Since by hypothesis μj=0\mu\_{j}=0 if supp⁡(𝐞j)={j}⊆supp⁡(𝝅⋆)\operatorname{supp}(\mathbf{e}\_{j})=\{j\}\subseteq\operatorname{supp}(\boldsymbol{\pi}^{\star}), we recover ([4.15](https://arxiv.org/html/2510.25740v1#S4.E15 "In 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) with λ=1−⟨𝝅⋆,𝐦⟩\lambda=1-\langle\boldsymbol{\pi}^{\star},\mathbf{m}\rangle by using ([4.16](https://arxiv.org/html/2510.25740v1#S4.E16 "In 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) and evaluating ([4.14](https://arxiv.org/html/2510.25740v1#S4.E14 "In Theorem 4.11 (First-order condition). ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) at 𝝅=𝐞j∈Δn\boldsymbol{\pi}=\mathbf{e}\_{j}\in\Delta\_{n} j=1,…,nj=1,\dots,n.
∎

###### Remark 4.12.

By Taylor expanding as in ([1.9](https://arxiv.org/html/2510.25740v1#S1.E9 "In item (ii) ‣ Remark 1.2. ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")) for small ri≈0r\_{i}\approx 0,

|  |  |  |
| --- | --- | --- |
|  | J​(𝝅)≈12​𝔼​[Var𝝅​(𝐫)]=12​(∑iπi​𝔼​[ri2]−∑i,jπi​πj​𝔼​[ri​rj]),J(\boldsymbol{\pi})\approx\tfrac{1}{2}\,\mathbb{E}\!\bigl[\mathrm{Var}\_{\boldsymbol{\pi}}(\mathbf{r})\bigr]=\frac{1}{2}\left(\sum\_{i}\pi\_{i}\,\mathbb{E}[r\_{i}^{2}]-\sum\_{i,j}\pi\_{i}\pi\_{j}\,\mathbb{E}[r\_{i}r\_{j}]\right), |  |

which is a concave quadratic form in 𝛑\boldsymbol{\pi} in terms of the second moments of 𝐫\mathbf{r}. While directly solving ([4.13](https://arxiv.org/html/2510.25740v1#S4.E13 "In 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")) is challenging, this provides a tractable quadratic program that can be used to approximate the solution when the values of 𝐫\mathbf{r} are small (e.g., when 𝐫\mathbf{r} represents the log returns over short time horizons). This is particularly relevant in the continuous-time limit where this approximation leads to the (continuous time) excess growth rate. Related optimization problems in this setting have been proposed in [[22](https://arxiv.org/html/2510.25740v1#bib.bib22), [26](https://arxiv.org/html/2510.25740v1#bib.bib26), [41](https://arxiv.org/html/2510.25740v1#bib.bib41)].

###### Remark 4.13 (Growth optimal portfolio).

If the linear term is absent, the objective

|  |  |  |
| --- | --- | --- |
|  | 𝝅↦𝔼​[log⁡⟨𝝅,𝐑⟩]\boldsymbol{\pi}\mapsto\mathbb{E}\left[\log\langle\boldsymbol{\pi},\mathbf{R}\rangle\right] |  |

is the classical *log–wealth (growth rate) maximization* problem (c.f. [[18](https://arxiv.org/html/2510.25740v1#bib.bib18), Chapter 16]). An optimal portfolio for this objective, 𝛑G\boldsymbol{\pi}^{G}, is said to be *growth optimal*. The analogue of Theorem [4.11](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem11 "Theorem 4.11 (First-order condition). ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") for 𝛑G\boldsymbol{\pi}^{G} is given in [[18](https://arxiv.org/html/2510.25740v1#bib.bib18), Theorems 16.2.1–16.2.2]. There, it is shown that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨𝝅,𝐑⟩⟨𝝅G,𝐑⟩]≤ 1,𝝅∈Δn,\mathbb{E}\left[\frac{\langle\boldsymbol{\pi},\mathbf{R}\rangle}{\langle\boldsymbol{\pi}^{G},\mathbf{R}\rangle}\right]\ \leq\ 1,\quad\boldsymbol{\pi}\in\Delta\_{n}, |  |

with equality holding if supp⁡(𝛑)⊆supp⁡(𝛑G)\operatorname{supp}(\boldsymbol{\pi})\subseteq\operatorname{supp}(\boldsymbol{\pi}^{G}).

As a corollary, we obtain the following estimate on the relative growth rates by Jensen’s inequality.

###### Corollary 4.14.

Let 𝛑⋆\boldsymbol{\pi}^{\star} maximize J​(⋅)J(\cdot). Then, for all 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n}

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[log⁡(⟨𝝅,𝐑⟩⟨𝝅⋆,𝐑⟩)]≤log⁡(1+⟨𝝅−𝝅⋆,𝐦⟩).\mathbb{E}\left[\log\left(\frac{\langle\boldsymbol{\pi},\mathbf{R}\rangle}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right)\right]\ \leq\ \log\left(1+\langle\boldsymbol{\pi}-\boldsymbol{\pi}^{\star},\mathbf{m}\rangle\right). |  |

###### Remark 4.15.

From Corollary [4.14](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem14 "Corollary 4.14. ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") we see that if 𝛑G\boldsymbol{\pi}^{G} is the growth optimal portfolio then

|  |  |  |
| --- | --- | --- |
|  | 0≤𝔼​[log⁡(⟨𝝅G,𝐑⟩⟨𝝅⋆,𝐑⟩)]≤log⁡(1+⟨𝝅G−𝝅⋆,𝐦⟩).0\leq\mathbb{E}\left[\log\left(\frac{\langle\boldsymbol{\pi}^{G},\mathbf{R}\rangle}{\langle\boldsymbol{\pi}^{\star},\mathbf{R}\rangle}\right)\right]\ \leq\ \log\left(1+\langle\boldsymbol{\pi}^{G}-\boldsymbol{\pi}^{\star},\mathbf{m}\rangle\right). |  |

Namely, the growth rate of 𝛑⋆\boldsymbol{\pi}^{\star} cannot be too much worse than the optimal rate. Its shortfall is controlled both by the deviation of 𝛑⋆\boldsymbol{\pi}^{\star} from 𝛑G\boldsymbol{\pi}^{G} and the expected returns 𝐦\mathbf{m}. Indeed, if 𝐦\mathbf{m} is a *constant vector* (i.e. all stocks have the same *expected* return) then ⟨𝛑G−𝛑⋆,𝐦⟩=0\langle\boldsymbol{\pi}^{G}-\boldsymbol{\pi}^{\star},\mathbf{m}\rangle=0 and 𝛑⋆\boldsymbol{\pi}^{\star} is also growth optimal. We can also use this chain of inequalities to conclude

|  |  |  |
| --- | --- | --- |
|  | ⟨𝝅⋆,𝐦⟩≤⟨𝝅G,𝐦⟩.\langle\boldsymbol{\pi}^{\star},\mathbf{m}\rangle\leq\langle\boldsymbol{\pi}^{G},\mathbf{m}\rangle. |  |

That is, the log-optimal portfolio not only has a higher growth rate than 𝛑⋆\boldsymbol{\pi}^{\star}, but also allocates more to securities with the *largest* expected log-returns.

## 5. Conclusion

Beginning with the financial definition of the excess growth rate, we demonstrate its rich connections with information-theoretic quantities, characterize it axiomatically from three complementary perspectives, and study its maximization that modifies the classical growth optimal portfolio. We conclude this paper by highlighting several natural questions related to our work.

1. 1.

   Motivated again by Leinster’s book [[38](https://arxiv.org/html/2510.25740v1#bib.bib38)], one may ask if there are (financially) meaningful deformations of the excess growth rate, analogous to how the Rényi divergence deforms the relative entropy. If so, a natural follow-up question is to derive axiomatic characterization theorems that show these deformations are, in a sense, canonical. The divergence in Example [3.19](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem19 "Example 3.19 (Rényi divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), which involves the Rényi divergence and corresponds to the so-called diversity-weighted portfolio in stochastic portfolio theory, seems to be a reasonable candidate.
2. 2.

   As shown in [[37](https://arxiv.org/html/2510.25740v1#bib.bib37), [55](https://arxiv.org/html/2510.25740v1#bib.bib55)], intuition and techniques from mathematical finance are instrumental in many modern developments in information theory, statistical inference, and hypothesis testing (Remark [1.4](https://arxiv.org/html/2510.25740v1#S1.Thmtheorem4 "Remark 1.4 (Information theory and quantitative finance). ‣ 1. Introduction ‣ A mathematical study of the excess growth rate")). Can the excess growth rate, or analogous financial quantities, contribute to this development?
3. 3.

   Our theoretical study of maximization of the (expected) excess growth rate covers only the basic one-period setting. From the practical perspective, it is both interesting and necessary to consider extensions to dynamic (multi-period or continuous-time) settings, as well as transaction costs and model uncertainty. One may also ask if there are relations with (suitable generalizations of) the asymptotic equipartition property and Cover’s universal portfolio.
4. 4.

   Closely related to the relative volatility (quantified by the excess growth rate) of a stock market is the concept of market diversity. Market diversity measures the concentration of a stock market. It is high when capital is spread more evenly among the different companies, and it is low when a small number of big companies dominate the entire market. In stochastic portfolio theory, it is typically quantified by the Shannon entropy (see [[28](https://arxiv.org/html/2510.25740v1#bib.bib28)]). Currently (2025), the diversity of the US market is rather low (relative to the historical average) due to the emergence of large technology companies. In fact, changes in market diversity tend to correlate with the performance of active large cap fund managers relative to the market; see [[16](https://arxiv.org/html/2510.25740v1#bib.bib16), Section 3] for detailed discussions and an empirical study. A shortcoming of Shannon entropy (and similar quantities) is that it does not take into account the similarities between stocks. For example, stocks in the same industry sector tend to be more correlated with each other. In [[39](https://arxiv.org/html/2510.25740v1#bib.bib39)] (also see [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Chapter 5]), generalized diversity measures (and hence entropies) were defined for probability distributions on a finite set equipped with a similarity matrix. It is interesting to adapt their approach to stock markets and study implications for portfolio selection.202020This problem was suggested to us by Martin Larsson (private communication).

## Acknowledgment

S. Campbell acknowledges support from an NSERC Postdoctoral Fellowship (PDF‑599675-2025) and a CDFT Research Grant. T.-K. L. Wong acknowledges support from the NSERC Discovery Grant RGPIN-2025-06021. The authors thank Martin Larsson for pointing us to Leinster’s book [[38](https://arxiv.org/html/2510.25740v1#bib.bib38)] which inspired us to derive axiomatic characterizations of the excess growth rate. T.-K. L. Wong would also like to thank Soumik Pal with whom many important ideas in this paper, including the first chain rule of the excess growth rate (Proposition [2.4](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem4 "Proposition 2.4 (Chain rule (first version)). ‣ 2.1. Basic properties and financial intuition ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), the logarithmic divergence ([3.17](https://arxiv.org/html/2510.25740v1#S3.E17 "In Definition 3.17 (Logarithmic divergence). ‣ 3.3. Via logarithmic divergence and cross-entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")) and large deviations of the Dirichlet perturbation (see Remark [2.14](https://arxiv.org/html/2510.25740v1#S2.Thmtheorem14 "Remark 2.14 (The case of equal weights). ‣ 2.4. Probabilistic interpretations ‣ 2. Excess growth rate: properties and interpretations ‣ A mathematical study of the excess growth rate")), were first developed.

## Appendix

## Appendix A Proof of Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")

The proof of this result takes three ingredients. The first is a recursion formula for I(⋅∥⋅)I(\cdot\;\|\;\cdot) that is also satisfied by the relative entropy. The second ingredient is a functional equation in four variables that must be satisfied by B​(x,y):=I2​((x,1−x)∥(y,1−y))B(x,y):=I\_{2}((x,1-x)\;\|\;(y,1-y)) given the recursion formula. The third is a characterization of the symmetric separately measurable solutions to this equation that vanish on the diagonal. This latter result makes use of the general solution of an auxiliary functional equation due to [[23](https://arxiv.org/html/2510.25740v1#bib.bib23)].

###### Remark A.1.

We provide here some historical context for our approach and also highlight why the specific structure in Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") necessitates a dedicated analysis. As will be seen, the domain (𝐩,𝐪)∈Δn∘×Δn∘(\mathbf{p},\mathbf{q})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ} leads to some subtleties that must be carefully checked.

In [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Section 3.5], Leinster provides the characterization in Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") on the larger domain (𝐩,𝐪)∈𝒜n(\mathbf{p},\mathbf{q})\in\mathcal{A}\_{n} and also dispenses with measurability in the first argument. However, his proof (see [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Lemma 3.5.3]) fundamentally requires information about I(⋅∥⋅)I(\cdot\;\|\;\cdot) outside of Δn∘×Δn∘\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ} and so cannot be directly adapted for our purposes. Instead, our proof follows an alternative line of argumentation that is well understood in the literature (see, for instance, the historical remarks in [[38](https://arxiv.org/html/2510.25740v1#bib.bib38), Section 3.5] and Section 2.1 of the survey [[19](https://arxiv.org/html/2510.25740v1#bib.bib19)] where a result of this flavor is attributed to Kannappan and Ng). Indeed, under a related set of assumptions a characterization of relative entropy is proven in Kannappan’s book (see [[34](https://arxiv.org/html/2510.25740v1#bib.bib34), Section 10.2f]).

The arguments employed in [[34](https://arxiv.org/html/2510.25740v1#bib.bib34), Section 10.2f] leverage Kannappan’s work with Ng in [[35](https://arxiv.org/html/2510.25740v1#bib.bib35)]. Importantly, the paper [[35](https://arxiv.org/html/2510.25740v1#bib.bib35)] enables a characterization of the solution to the functional equation ([A.1](https://arxiv.org/html/2510.25740v1#A1.E1 "In Lemma A.3. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")) on the domain x,y∈[0,1)x,y\in[0,1) x+u∈[0,1]x+u\in[0,1], y,v,y+v∈(0,1)y,v,y+v\in(0,1). For our purposes we need a characterization on the restricted domain x,u,y,v,x+u,y+v∈(0,1)x,u,y,v,x+u,y+v\in(0,1). Fortunately, we may substitute the result of [[35](https://arxiv.org/html/2510.25740v1#bib.bib35)] with a more general result that was proved a few years later by Ebanks, Kannappan and Ng [[23](https://arxiv.org/html/2510.25740v1#bib.bib23)]. This result allows us to recover the same characterization using similar arguments, but without including the additional boundary points in the domain of the functional equation. Since we are unable to locate the precise characterization postulated in Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") in the literature, we provide a complete proof here.

For notational convenience we use the leave-one-out notation 𝐩(−i)∈ℝn−1\mathbf{p}^{(-i)}\in\mathbb{R}^{n-1} to denote the deletion of coordinate ii from the vector 𝐩∈ℝn\mathbf{p}\in\mathbb{R}^{n} when n≥2n\geq 2.

###### Lemma A.2.

If In(⋅∥⋅)I\_{n}(\cdot\;\|\;\cdot) satisfies [(C2)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i2 "item (C2) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C4)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i4 "item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") then for any (𝐩,𝐪)∈Δn∘×Δn∘(\mathbf{p},\mathbf{q})\in\Delta\_{n}^{\circ}\times\Delta\_{n}^{\circ} and n≥3n\geq 3 it satisfies the recursion

|  |  |  |
| --- | --- | --- |
|  | In(𝐩∥𝐪)=I2((pi,1−pi)∥(qi,1−qi))+(1−pi)In−1(𝐩(−i)1−pi∥𝐪(−i)1−qi),I\_{n}(\mathbf{p}\;\|\;\mathbf{q})=I\_{2}((p\_{i},1-p\_{i})\;\|\;(q\_{i},1-q\_{i}))+(1-p\_{i})I\_{n-1}\left(\frac{\mathbf{p}^{(-i)}}{1-p\_{i}}\;\middle\|\;\frac{\mathbf{q}^{(-i)}}{1-q\_{i}}\right), |  |

for i=1,…,ni=1,\ldots,n.

###### Proof.

We can write

|  |  |  |
| --- | --- | --- |
|  | 𝐩=(p1,1−p1)∘((1),(p21−p1,…,pn1−p1))\mathbf{p}=(p\_{1},1-p\_{1})\circ\left((1),\left(\frac{p\_{2}}{1-p\_{1}},\dots,\frac{p\_{n}}{1-p\_{1}}\right)\right) |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝐪=(q1,1−q1)∘((1),(q21−q1,…,qn1−q1))\mathbf{q}=(q\_{1},1-q\_{1})\circ\left((1),\left(\frac{q\_{2}}{1-q\_{1}},\dots,\frac{q\_{n}}{1-q\_{1}}\right)\right) |  |

Observe that (p1,1−p1),(q1,1−q2)∈Δ2∘,1∈Δ1∘(p\_{1},1-p\_{1}),(q\_{1},1-q\_{2})\in\Delta\_{2}^{\circ},1\in\Delta\_{1}^{\circ} and 𝐩(−1)1−p1,𝐪(−1)1−q1∈Δn−1∘\frac{\mathbf{p}^{(-1)}}{1-p\_{1}},\frac{\mathbf{q}^{(-1)}}{1-q\_{1}}\in\Delta\_{n-1}^{\circ}. By the chain rule [(C4)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i4 "item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") and the fact that I1​((1)∥(1))=0I\_{1}((1)\|(1))=0 (see [(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | In​(𝐩∥𝐪)\displaystyle I\_{n}(\mathbf{p}\;\|\;\mathbf{q}) | =I2((p1,1−p1)∥(q1,1−q1))+(1−p1)In−1(𝐩(−1)1−p1∥𝐪(−1)1−q1).\displaystyle=I\_{2}((p\_{1},1-p\_{1})\|(q\_{1},1-q\_{1}))+(1-p\_{1})I\_{n-1}\left(\frac{\mathbf{p}^{(-1)}}{1-p\_{1}}\;\middle\|\;\frac{\mathbf{q}^{(-1)}}{1-q\_{1}}\right). |  |

By permutation invariance [(C2)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i2 "item (C2) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), the index i=1i=1 is arbitrary.
∎

###### Lemma A.3.

If In(⋅∥⋅)I\_{n}(\cdot\;\|\;\cdot) satisfies [(C2)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i2 "item (C2) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C4)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i4 "item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") then B​(x,y):=I2​((x,1−x)∥(y,1−y))B(x,y):=I\_{2}((x,1-x)\;\|\;(y,1-y)) for x,y∈(0,1)x,y\in(0,1) satisfies the functional equation

|  |  |  |  |
| --- | --- | --- | --- |
| (A.1) |  | B​(x,y)+(1−x)​B​(u1−x,v1−y)=B​(u,v)+(1−u)​B​(x1−u,y1−v)B(x,y)+(1-x)B\left(\frac{u}{1-x},\frac{v}{1-y}\right)=B(u,v)+(1-u)B\left(\frac{x}{1-u},\frac{y}{1-v}\right) |  |

on the (open) triangular domain x,y,u,v,x+u,y+v∈(0,1)x,y,u,v,x+u,y+v\in(0,1).

###### Proof.

Applying Lemma [A.2](https://arxiv.org/html/2510.25740v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate") with n=3n=3 and i≠j∈{1,2,3}i\neq j\in\{1,2,3\} we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | I3​(𝐩∥𝐪)\displaystyle I\_{3}(\mathbf{p}\;\|\;\mathbf{q}) | =I2​((pi,1−pi)∥(qi,1−qi))\displaystyle=I\_{2}((p\_{i},1-p\_{i})\;\|\;(q\_{i},1-q\_{i})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−pi)I2((pj1−pi,1−pj1−pi)∥(qj1−qi,1−qj1−qi))\displaystyle\quad+(1-p\_{i})I\_{2}\left(\left(\frac{p\_{j}}{1-p\_{i}},1-\frac{p\_{j}}{1-p\_{i}}\right)\;\middle\|\;\left(\frac{q\_{j}}{1-q\_{i}},1-\frac{q\_{j}}{1-q\_{i}}\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =B​(pi,qi)+(1−pi)​B​(pj1−pi,qj1−qi).\displaystyle=B(p\_{i},q\_{i})+(1-p\_{i})B\left(\frac{p\_{j}}{1-p\_{i}},\frac{q\_{j}}{1-q\_{i}}\right). |  |

Swapping the choice of indices and repeating the argument

|  |  |  |
| --- | --- | --- |
|  | I3​(𝐩∥𝐪)=B​(pj,qj)+(1−pj)​B​(pi1−pj,qi1−qj).\displaystyle I\_{3}(\mathbf{p}\;\|\;\mathbf{q})=B(p\_{j},q\_{j})+(1-p\_{j})B\left(\frac{p\_{i}}{1-p\_{j}},\frac{q\_{i}}{1-q\_{j}}\right). |  |

Equating these two expressions recovers ([A.1](https://arxiv.org/html/2510.25740v1#A1.E1 "In Lemma A.3. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")).
∎

###### Lemma A.4.

If B​(⋅,⋅)B(\cdot,\cdot) is a separately measurable solution to ([A.1](https://arxiv.org/html/2510.25740v1#A1.E1 "In Lemma A.3. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")) satisfying

|  |  |  |
| --- | --- | --- |
|  | B​(x,y)=B​(1−x,1−y)andB​(x,x)=0,x,y∈(0,1),B(x,y)=B(1-x,1-y)\quad\text{and}\quad B(x,x)=0,\quad x,y\in(0,1), |  |

then there exists a c∈ℝc\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | B​(x,y)=c​H​((x,1−x)∥(y,1−y)),x,y∈(0,1).B(x,y)=cH((x,1-x)\;\|\;(y,1-y)),\quad x,y\in(0,1). |  |

###### Proof.

Fix y,v∈(0,1)y,v\in(0,1) with y+v∈(0,1)y+v\in(0,1). Writing

|  |  |  |
| --- | --- | --- |
|  | k​(z)=B​(z,y1−v),g​(z)=B​(z,v1−y),f​(z)=B​(z,y),h​(z)=B​(z,v),k(z)=B\left(z,\frac{y}{1-v}\right),\ g(z)=B\left(z,\frac{v}{1-y}\right),\ f(z)=B(z,y),\ h(z)=B(z,v), |  |

we may rewrite the functional equation for BB as

|  |  |  |
| --- | --- | --- |
|  | f​(x)+(1−x)​g​(u1−x)=h​(u)+(1−u)​k​(x1−u)f(x)+(1-x)g\left(\frac{u}{1-x}\right)=h(u)+(1-u)k\left(\frac{x}{1-u}\right) |  |

for x,u,x+u∈(0,1)x,u,x+u\in(0,1). This is exactly the equation in [[34](https://arxiv.org/html/2510.25740v1#bib.bib34), Corollary 10.7c] (see also the original paper [[23](https://arxiv.org/html/2510.25740v1#bib.bib23)]) for the identity M​(x)≡xM(x)\equiv x. As the identity map is both additive and multiplicative we get by [[34](https://arxiv.org/html/2510.25740v1#bib.bib34), Corollary 10.7c] the general solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)\displaystyle f(x) | =x​L​(x)+(1−x)​L​(1−x)+η3​x−η2​(1−x)+η5,\displaystyle=x\,L(x)+(1-x)\,L(1-x)+\eta\_{3}\,x-\eta\_{2}\,(1-x)+\eta\_{5}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)\displaystyle g(x) | =x​L​(x)+(1−x)​L​(1−x)+η1​x+η2,\displaystyle=x\,L(x)+(1-x)\,L(1-x)+\eta\_{1}\,x+\eta\_{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)\displaystyle h(x) | =x​L​(x)+(1−x)​L​(1−x)+η1​x−η4​(1−x)+η5,\displaystyle=x\,L(x)+(1-x)\,L(1-x)+\eta\_{1}\,x-\eta\_{4}\,(1-x)+\eta\_{5}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | k​(x)\displaystyle k(x) | =x​L​(x)+(1−x)​L​(1−x)+η3​x+η4,\displaystyle=x\,L(x)+(1-x)\,L(1-x)+\eta\_{3}\,x+\eta\_{4}, |  |

where L​(⋅)L(\cdot) is a solution to the logarithmic equation

|  |  |  |  |
| --- | --- | --- | --- |
| (A.2) |  | L​(x​y)=L​(x)+L​(y),x,y∈(0,1),L(xy)=L(x)+L(y),\qquad x,y\in(0,1), |  |

and ηi\eta\_{i}, i=1,…,5i=1,\dots,5 are constants. Note that a priori all of the constants depend on y,v,y+v∈(0,1)y,v,y+v\in(0,1). Since B​(⋅,y)B(\cdot,y) is Lebesgue measurable for each y∈(0,1)y\in(0,1), so too are the functions f,g,h,k,Lf,g,h,k,L. As the Lebesgue measurable solution to the logarithmic equation is L​(x)=c​log⁡(x)L(x)=c\log(x) for some c∈ℝc\in\mathbb{R}, we can make this identification.

Define the binary entropy

|  |  |  |
| --- | --- | --- |
|  | ℰ​(x)=−x​log⁡x−(1−x)​log⁡(1−x),x∈(0,1).\mathcal{E}(x)=-x\log x-(1-x)\log(1-x),\quad x\in(0,1). |  |

By emphasizing the dependence of the constants on the parameters v,yv,y and substituting the form of the f,g,h,kf,g,h,k in terms of BB, we arrive at the equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(x,y)\displaystyle B(x,y) | =−c​(y,v)​ℰ​(x)+η3​(y,v)​x−η2​(y,v)​(1−x)+η5​(y,v),\displaystyle=-c(y,v)\mathcal{E}(x)+\eta\_{3}(y,v)\,x-\eta\_{2}(y,v)\,(1-x)+\eta\_{5}(y,v), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(x,v1−y)\displaystyle B\left(x,\frac{v}{1-y}\right) | =−c​(y,v)​ℰ​(x)+η1​(y,v)​x+η2​(y,v),\displaystyle=-c(y,v)\mathcal{E}(x)+\eta\_{1}(y,v)\,x+\eta\_{2}(y,v), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(x,v)\displaystyle B(x,v) | =−c​(y,v)​ℰ​(x)+η1​(y,v)​x−η4​(y,v)​(1−x)+η5​(y,v),\displaystyle=-c(y,v)\mathcal{E}(x)+\eta\_{1}(y,v)\,x-\eta\_{4}(y,v)\,(1-x)+\eta\_{5}(y,v), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(x,y1−v)\displaystyle B\left(x,\frac{y}{1-v}\right) | =−c​(y,v)​ℰ​(x)+η3​(y,v)​x+η4​(y,v).\displaystyle=-c(y,v)\mathcal{E}(x)+\eta\_{3}(y,v)\,x+\eta\_{4}(y,v). |  |

Isolating the first and third equations we see that:

|  |  |  |
| --- | --- | --- |
|  | B​(x,y)=−c​(y,v)​ℰ​(x)+a1​(y,v)​x+b1​(y,v),B(x,y)=-c(y,v)\mathcal{E}(x)+a\_{1}(y,v)\,x+b\_{1}(y,v), |  |

|  |  |  |
| --- | --- | --- |
|  | B​(x,v)=−c​(y,v)​ℰ​(x)+a2​(y,v)​x+b2​(y,v)B(x,v)=-c(y,v)\mathcal{E}(x)+a\_{2}(y,v)\,x+b\_{2}(y,v) |  |

where a1​(y,v)=η3​(y,v)+η2​(y,v)a\_{1}(y,v)=\eta\_{3}(y,v)+\eta\_{2}(y,v), a2​(y,v)=η1​(y,v)+η4​(y,v)a\_{2}(y,v)=\eta\_{1}(y,v)+\eta\_{4}(y,v), b1​(y,v)=η5​(y,v)−η2​(y,v)b\_{1}(y,v)=\eta\_{5}(y,v)-\eta\_{2}(y,v) and b2​(y,v)=η5​(y,v)−η4​(y,v)b\_{2}(y,v)=\eta\_{5}(y,v)-\eta\_{4}(y,v).
Fix yy and take any v1,v2∈(0,1)v\_{1},v\_{2}\in(0,1) with v1+y,v2+y∈(0,1)v\_{1}+y,v\_{2}+y\in(0,1). Substituting these into the first equation and subtracting gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =−(c​(y,v1)−c​(y,v2))​ℰ​(x)+(a1​(y,v1)−a1​(y,v2))​x+(b1​(y,v1)−b1​(y,v2))\displaystyle=-(c(y,v\_{1})-c(y,v\_{2}))\mathcal{E}(x)+(a\_{1}(y,v\_{1})-a\_{1}(y,v\_{2}))x+(b\_{1}(y,v\_{1})-b\_{1}(y,v\_{2})) |  |

for all x,y,x+y∈(0,1)x,y,x+y\in(0,1). This implies

|  |  |  |
| --- | --- | --- |
|  | c​(y,v1)=c​(y,v2),a1​(y,v1)=a1​(y,v2),b1​(y,v1)=b1​(y,v2).\displaystyle c(y,v\_{1})=c(y,v\_{2}),\quad a\_{1}(y,v\_{1})=a\_{1}(y,v\_{2}),\quad b\_{1}(y,v\_{1})=b\_{1}(y,v\_{2}). |  |

Repeating this argument with the second equation gives us

|  |  |  |
| --- | --- | --- |
|  | c​(y1,v)=c​(y2,v),a2​(y1,v)=a2​(y2,v),b2​(y1,v)=b2​(y2,v).\displaystyle c(y\_{1},v)=c(y\_{2},v),\quad a\_{2}(y\_{1},v)=a\_{2}(y\_{2},v),\quad b\_{2}(y\_{1},v)=b\_{2}(y\_{2},v). |  |

Since these holds for all admissible v1,v2v\_{1},v\_{2} given yy (respectively, all admissible y1,y2y\_{1},y\_{2} given vv) we conclude212121This conclusion is tacitly using that {ℰ​(x),x,1}\{\mathcal{E}(x),x,1\} are linearly independent on (0,1)(0,1). that c​(y,v)≡cc(y,v)\equiv c is constant and that a1​(y,v),b2​(y,v)a\_{1}(y,v),b\_{2}(y,v) do not depend on vv (respectively, a2​(y,v),b2​(y,v)a\_{2}(y,v),b\_{2}(y,v) do not depend on yy). Thus, we deduce that B​(⋅,⋅)B(\cdot,\cdot) takes the form

|  |  |  |  |
| --- | --- | --- | --- |
| (A.3) |  | B​(x,y)=−c​ℰ​(x)+a​(y)​x+b​(y),x,y∈(0,1),B(x,y)=-c\mathcal{E}(x)+a(y)x+b(y),\ \ \ x,y\in(0,1), |  |

in terms of two univariate functions a,b:(0,1)↦ℝa,b:(0,1)\mapsto\mathbb{R}.

The equation ([A.3](https://arxiv.org/html/2510.25740v1#A1.E3 "In Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")) appears in exactly this form in [[34](https://arxiv.org/html/2510.25740v1#bib.bib34), Equation (10.50)]. By exploiting symmetry, we may employ analogous arguments to [[34](https://arxiv.org/html/2510.25740v1#bib.bib34)] in order to recover their [[34](https://arxiv.org/html/2510.25740v1#bib.bib34), Equation (10.50a)] and deduce that

|  |  |  |  |
| --- | --- | --- | --- |
| (A.4) |  | B​(x,y)=−c​ℰ​(x)+x​ℓ​(y)+(1−x)​ℓ​(1−y),x,y∈(0,1),B(x,y)=-c\mathcal{E}(x)+x\ell(y)+(1-x)\ell(1-y),\ \ \ x,y\in(0,1), |  |

where ℓ​(⋅)\ell(\cdot) is another solution of the logarithmic equation ([A.2](https://arxiv.org/html/2510.25740v1#A1.E2 "In Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")).

With this verification complete, we can now make use of ([A.4](https://arxiv.org/html/2510.25740v1#A1.E4 "In Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")) to complete the proof. Consider the sequence of functions 𝔟n​(y)=B​(xn,y)\mathfrak{b}\_{n}(y)=B(x\_{n},y) for xn↑1x\_{n}\uparrow 1. Each function is Lebesgue measurable by the measurability of y↦B​(x,y)y\mapsto B(x,y) for each xx. Passing to the limit we define

|  |  |  |
| --- | --- | --- |
|  | 𝔟∞​(y):=limn→∞𝔟n​(y)=ℓ​(y),y∈(0,1).\mathfrak{b}\_{\infty}(y):=\lim\_{n\to\infty}\mathfrak{b}\_{n}(y)=\ell(y),\ \ \ y\in(0,1). |  |

As the pointwise limit of Lebesgue measurable functions, 𝔟∞​(y)=ℓ​(y)\mathfrak{b}\_{\infty}(y)=\ell(y) is Lebesgue measurable. Hence, ℓ​(⋅)\ell(\cdot) is a *Lebesgue measurable* solution of ([A.2](https://arxiv.org/html/2510.25740v1#A1.E2 "In Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")) and so, there exists a c′∈ℝc^{\prime}\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ℓ​(y)=c′​log⁡(y),y∈(0,1).\ell(y)=c^{\prime}\log(y),\ \ \ y\in(0,1). |  |

Using the property B​(x,x)=0B(x,x)=0 we arrive at the identity

|  |  |  |
| --- | --- | --- |
|  | c​ℰ​(x)=c′​[x​log⁡(x)+(1−x)​log⁡(1−x)]=c′​ℰ​(x),x∈(0,1),c\mathcal{E}(x)=c^{\prime}\left[x\log(x)+(1-x)\log(1-x)\right]=c^{\prime}\mathcal{E}(x),\quad x\in(0,1), |  |

from which it necessarily follows that c′=cc^{\prime}=c. Putting this all together,

|  |  |  |
| --- | --- | --- |
|  | B​(x,y)=−c​[ℰ​(x)−x​log⁡(y)−(1−x)​log⁡(1−y)]=−c​H​((x,1−x),(y,1−y)).B(x,y)=-c\left[\mathcal{E}(x)-x\log(y)-(1-x)\log(1-y)\right]=-cH((x,1-x),(y,1-y)). |  |

Absorbing −c-c into a single constant completes the proof.
∎

With these ingredients we readily complete the proof of Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

###### Proof of Proposition [3.6](https://arxiv.org/html/2510.25740v1#S3.Thmtheorem6 "Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate").

That relative entropy satisfies [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C4)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i4 "item (C4) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") is a standard verification, so we focus on the converse implication.

First, note that the equality I1=c​H1I\_{1}=cH\_{1} trivially holds for n=1n=1 as Δ1∘={1}\Delta\_{1}^{\circ}=\{1\}. Indeed, I1​(1∥ 1)=c​H​(1∥ 1)=0I\_{1}(1\;\|\;1)=cH(1\;\|\;1)=0. Then, by Lemma [A.3](https://arxiv.org/html/2510.25740v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate") and Assumption [(C1)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i1 "item (C1) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate"), B​(x,y)=I2​((x,1−x)∥(y,1−y))B(x,y)=I\_{2}((x,1-x)\;\|\;(y,1-y)) is a separately measurable solution of the functional equation ([A.1](https://arxiv.org/html/2510.25740v1#A1.E1 "In Lemma A.3. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate")). By the permutation invariance and vanishing properties [(C2)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i2 "item (C2) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate")–[(C3)](https://arxiv.org/html/2510.25740v1#S3.I5.ix1.I1.i3 "item (C3) ‣ item (i) ‣ Proposition 3.6 (Characterization of relative entropy on the open simplex). ‣ 3.1. Via relative entropy ‣ 3. Characterization theorems ‣ A mathematical study of the excess growth rate") of I2(⋅∥⋅)I\_{2}(\cdot\;\|\;\cdot) we also get

|  |  |  |
| --- | --- | --- |
|  | B​(x,y)=B​(1−x,1−y)andB​(x,x)=0,x,y∈(0,1).B(x,y)=B(1-x,1-y)\quad\text{and}\quad B(x,x)=0,\quad x,y\in(0,1). |  |

So, by Lemma [A.4](https://arxiv.org/html/2510.25740v1#A1.Thmtheorem4 "Lemma A.4. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate") we conclude that there exists a c∈ℝc\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | I2​((x,1−x)∥(y,1−y))=c​H​((x,1−x)∥(y,1−y)),x,y∈(0,1).I\_{2}((x,1-x)\;\|\;(y,1-y))=cH((x,1-x)\;\|\;(y,1-y)),\qquad x,y\in(0,1). |  |

To extend this to general n≥2n\geq 2, we use that relative entropy satisfies the recursion of Lemma [A.2](https://arxiv.org/html/2510.25740v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate"). Applying Lemma [A.2](https://arxiv.org/html/2510.25740v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proof of Proposition 3.6 ‣ A mathematical study of the excess growth rate") for n=3n=3 and using that I2=c​HI\_{2}=cH yields

|  |  |  |
| --- | --- | --- |
|  | I3​(𝐩∥𝐪)=c​H​(𝐩∥𝐪),𝐩,𝐪∈Δ3∘.I\_{3}(\mathbf{p}\;\|\;\mathbf{q})=cH(\mathbf{p}\;\|\;\mathbf{q}),\qquad\mathbf{p},\mathbf{q}\in\Delta\_{3}^{\circ}. |  |

Iterating this recursion for n=4,5,…n=4,5,\dots completes the proof for general nn.
∎

## Appendix B Superdifferential set for the excess growth rate

###### Definition B.1.

For 𝛑∈Δn\boldsymbol{\pi}\in\Delta\_{n}, the superdifferential set of JJ at 𝛑\boldsymbol{\pi} relative to Δn\Delta\_{n} is

|  |  |  |
| --- | --- | --- |
|  | ∂Δn+J​(𝝅):={𝐪∈ℝn:J​(𝝅′)−J​(𝝅)≤⟨𝐪,𝝅′−𝝅⟩∀𝝅′∈Δn}.\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}):=\bigl\{\mathbf{q}\in\mathbb{R}^{n}:\ J(\boldsymbol{\pi}^{\prime})-J(\boldsymbol{\pi})\leq\langle\mathbf{q},\boldsymbol{\pi}^{\prime}-\boldsymbol{\pi}\rangle\ \ \forall\,\boldsymbol{\pi}^{\prime}\in\Delta\_{n}\bigr\}. |  |

###### Lemma B.2.

Under Assumption [4.10](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem10 "Assumption 4.10. ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate")
𝐠∈∂Δn+J​(𝛑)\mathbf{g}\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}) if and only if there exists λ∈ℝ\lambda\in\mathbb{R} and a 𝛍∈ℝ+n\boldsymbol{\mu}\in\mathbb{R}^{n}\_{+} with μi=0\mu\_{i}=0 on supp⁡(𝛑)\operatorname{supp}(\boldsymbol{\pi}) such that222222Note that Assumption [4.10](https://arxiv.org/html/2510.25740v1#S4.Thmtheorem10 "Assumption 4.10. ‣ 4.4. Maximizing the expected excess growth rate ‣ 4. Optimization ‣ A mathematical study of the excess growth rate") is not sufficient to guarantee that 𝐠\mathbf{g} has finite coordinates. However, the expectation is always non-negative and therefore well defined.

|  |  |  |
| --- | --- | --- |
|  | 𝐠=𝔼​[𝐑⟨𝝅,𝐑⟩]−𝐦−λ​𝟏+𝝁∈ℝn.\mathbf{g}=\mathbb{E}\left[\frac{\mathbf{R}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right]-\mathbf{m}-\lambda\mathbf{1}+\boldsymbol{\mu}\in\mathbb{R}^{n}. |  |

In particular, ∂Δn+J​(𝛑)≠∅\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi})\not=\emptyset if and only if 𝔼​[Ri⟨𝛑,𝐑⟩]<∞\mathbb{E}\left[\frac{R\_{i}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right]<\infty for all i∈{1,…,n}i\in\{1,\dots,n\}.

###### Proof.

Consider the normal cone to the simplex at 𝝅∈Δn\boldsymbol{\pi}\in\Delta\_{n}

|  |  |  |  |
| --- | --- | --- | --- |
|  | NΔn​(𝝅)\displaystyle N\_{\Delta\_{n}}(\boldsymbol{\pi}) | :={𝐯∈ℝn:⟨𝐯,𝝅′−𝝅⟩≤0∀𝝅′∈Δn}.\displaystyle:=\{\mathbf{v}\in\mathbb{R}^{n}:\ \langle\mathbf{v},\boldsymbol{\pi}^{\prime}-\boldsymbol{\pi}\rangle\leq 0\ \ \forall\,\boldsymbol{\pi}^{\prime}\in\Delta\_{n}\}. |  |

Any 𝐯∈NΔn​(𝝅)\mathbf{v}\in N\_{\Delta\_{n}}(\boldsymbol{\pi}) admits a representation 𝐯=λ​𝟏−𝝁\mathbf{v}=\lambda\mathbf{1}-\boldsymbol{\mu} where λ∈ℝ\lambda\in\mathbb{R}, μi=0\mu\_{i}=0 if i∈supp⁡(𝝅)i\in\operatorname{supp}(\boldsymbol{\pi}) and μi≥0\mu\_{i}\geq 0 otherwise. We observe that if 𝐠∈∂Δn+J​(𝝅)\mathbf{g}\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}) and 𝐯∈NΔn​(𝝅)\mathbf{v}\in N\_{\Delta\_{n}}(\boldsymbol{\pi}) then (𝐠−𝐯)∈∂Δn+J​(𝝅)(\mathbf{g}-\mathbf{v})\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}).

We now search for a particular element of the supergradient set. We begin with the assumption that 𝔼​[Ri⟨𝝅,𝐑⟩]<∞\mathbb{E}\left[\frac{R\_{i}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right]<\infty for all ii otherwise the claimed form of 𝐠\mathbf{g} cannot be a member of ∂Δn+J​(𝝅)\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}). For x,y>0x,y>0, log⁡y−log⁡x≤y−xx\log y-\log x\leq\frac{y-x}{x}. With
x=⟨𝝅,𝐑⟩x=\langle\boldsymbol{\pi},\mathbf{R}\rangle and y=⟨𝝅′,𝐑⟩y=\langle\boldsymbol{\pi}^{\prime},\mathbf{R}\rangle this yields

|  |  |  |
| --- | --- | --- |
|  | log⁡⟨𝝅′,𝐑⟩−log⁡⟨𝝅,𝐑⟩≤⟨𝝅′−𝝅,𝐑⟩⟨𝝅,𝐑⟩=⟨𝝅′−𝝅,𝐑⟨𝝅,𝐑⟩⟩.\log\langle\boldsymbol{\pi}^{\prime},\mathbf{R}\rangle-\log\langle\boldsymbol{\pi},\mathbf{R}\rangle\leq\frac{\langle\boldsymbol{\pi}^{\prime}-\boldsymbol{\pi},\mathbf{R}\rangle}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}=\left\langle\boldsymbol{\pi}^{\prime}-\boldsymbol{\pi},\frac{\mathbf{R}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right\rangle. |  |

Taking expectations and adding the remaining linear term we conclude

|  |  |  |  |
| --- | --- | --- | --- |
| (B.1) |  | J​(𝝅′)−J​(𝝅)≤⟨𝝅′−𝝅,𝔼​[𝐑⟨𝝅,𝐑⟩]−𝐦⟩.J(\boldsymbol{\pi}^{\prime})-J(\boldsymbol{\pi})\leq\left\langle\boldsymbol{\pi}^{\prime}-\boldsymbol{\pi},\mathbb{E}\left[\frac{\mathbf{R}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right]-\mathbf{m}\right\rangle. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | 𝐠⋆​(𝝅)=𝔼​[𝐑⟨𝝅,𝐑⟩]−𝐦.\mathbf{g}^{\star}(\boldsymbol{\pi})=\mathbb{E}\left[\frac{\mathbf{R}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right]-\mathbf{m}. |  |

By ([B.1](https://arxiv.org/html/2510.25740v1#A2.E1 "In Appendix B Superdifferential set for the excess growth rate ‣ A mathematical study of the excess growth rate")) 𝐠⋆​(𝝅)∈∂Δn+J​(𝝅)\mathbf{g}^{\star}(\boldsymbol{\pi})\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}) (and also (𝐠⋆−𝐯)∈∂Δn+J​(𝝅)(\mathbf{g}^{\star}-\mathbf{v})\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}) for 𝐯∈NΔn​(𝝅)\mathbf{v}\in N\_{\Delta\_{n}}(\boldsymbol{\pi})).

Next, we argue that on the relative interior of any face of Δn\Delta\_{n} where πi>0\pi\_{i}>0 the iith coordinate of 𝐠⋆​(𝝅)\mathbf{g}^{\star}(\boldsymbol{\pi}) defines the partial derivative. Here and in what follows we make regular use of the inequality

|  |  |  |
| --- | --- | --- |
|  | 0≤Ri⟨𝝅,𝐑⟩≤1πi0\leq\frac{R\_{i}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\leq\frac{1}{\pi\_{i}} |  |

when πi>0\pi\_{i}>0. Combining this with the inequality |log⁡(1+x)|≤|x|/(1−|x|)|\log(1+x)|\leq|x|/(1-|x|) for x∈(−1,∞)x\in(-1,\infty) we have for all h∈ℝh\in\mathbb{R} with |h|≤πi/2|h|\leq\pi\_{i}/2 (since Ri>0R\_{i}>0 and ⟨𝝅,𝐑⟩>0\langle\boldsymbol{\pi},\mathbf{R}\rangle>0)

|  |  |  |
| --- | --- | --- |
|  | |log⁡⟨𝝅+h​𝐞i,𝐑⟩−log⁡⟨𝝅,𝐑⟩h|=|1h​log⁡(1+h​Ri⟨𝝅,𝐑⟩)|\displaystyle\left|\frac{\log\langle\boldsymbol{\pi}+h\mathbf{e}\_{i},\mathbf{R}\rangle-\log\langle\boldsymbol{\pi},\mathbf{R}\rangle}{h}\right|=\left|\frac{1}{h}\log\left(1+h\frac{R\_{i}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right)\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Ri⟨𝝅,𝐑⟩1−|h|​Ri⟨𝝅,𝐑⟩≤1πi1−|h|​1πi≤2πi<∞.\displaystyle\leq\frac{\frac{R\_{i}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}}{1-|h|\frac{R\_{i}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}}\leq\frac{\frac{1}{\pi\_{i}}}{1-|h|\frac{1}{\pi\_{i}}}\leq\frac{2}{\pi\_{i}}<\infty. |  |

The second inequality follows from the monotonicity of x↦x/(1−x)x\mapsto x/(1-x) on (−∞,1)(-\infty,1). So, by the dominated convergence theorem,

|  |  |  |
| --- | --- | --- |
|  | ∂πiJ​(𝝅)=𝔼​[Ri⟨𝝅,𝐑⟩]−mi.\partial\_{\pi\_{i}}J(\boldsymbol{\pi})=\mathbb{E}\left[\frac{R\_{i}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right]-m\_{i}. |  |

We claim that if 𝐠∈∂Δn+J​(𝝅)\mathbf{g}\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}) then 𝐠=𝐠⋆​(𝝅)−𝐯\mathbf{g}=\mathbf{g}^{\star}(\boldsymbol{\pi})-\mathbf{v} for some 𝐯∈NΔn​(𝝅)\mathbf{v}\in N\_{\Delta\_{n}}(\boldsymbol{\pi}). Since we necessarily have that the coordinates of 𝐠\mathbf{g} are finite, if this were true the expectations in 𝐠⋆​(𝝅)\mathbf{g}^{\star}(\boldsymbol{\pi}) would also have to be finite. For a set of “active” indices S⊂{1,…,n}S\subset\{1,\dots,n\} we define the face

|  |  |  |
| --- | --- | --- |
|  | ΔS:={𝝅′∈Δn:πi′=0​∀i∉S}\Delta\_{S}:=\{\boldsymbol{\pi}^{\prime}\in\Delta\_{n}:\pi\_{i}^{\prime}=0\ \forall i\not\in S\} |  |

and the relative interior of the face,

|  |  |  |
| --- | --- | --- |
|  | ri​(ΔS):={𝝅′∈Δn:πi′=0​∀i∉S​and​πi′>0​∀i∈S}.\mathrm{ri}(\Delta\_{S}):=\{\boldsymbol{\pi}^{\prime}\in\Delta\_{n}:\pi\_{i}^{\prime}=0\ \forall i\not\in S\ \text{and}\ \pi\_{i}^{\prime}>0\ \forall i\in S\}. |  |

For fixed 𝝅\boldsymbol{\pi}, choose S=supp⁡(𝝅)S=\operatorname{supp}(\boldsymbol{\pi}) so 𝝅∈ri​(ΔS)\boldsymbol{\pi}\in\mathrm{ri}(\Delta\_{S}). We define the tangent space to ΔS\Delta\_{S} (embedded in ℝn\mathbb{R}^{n}) at this 𝝅\boldsymbol{\pi} as

|  |  |  |
| --- | --- | --- |
|  | TS​(𝝅):={𝐭∈ℝn:ti=0​∀i∉S,∑i=1nti=0}.T\_{S}(\boldsymbol{\pi}):=\left\{\mathbf{t}\in\mathbb{R}^{n}:t\_{i}=0\ \forall i\not\in S,\ \sum\_{i=1}^{n}t\_{i}=0\right\}. |  |

Let 𝐭∈TS​(𝝅)\mathbf{t}\in T\_{S}(\boldsymbol{\pi}) and 𝐠∈∂Δn+J​(𝝅)\mathbf{g}\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}). Then, for sufficiently small ϵ>0\epsilon>0, 𝝅+ϵ​𝐭∈ΔS\boldsymbol{\pi}+\epsilon\mathbf{t}\in\Delta\_{S} and so,

|  |  |  |
| --- | --- | --- |
|  | J​(𝝅+ϵ​𝐭)−J​(𝝅)≤⟨𝐠,ϵ​𝐭⟩.J(\boldsymbol{\pi}+\epsilon\mathbf{t})-J(\boldsymbol{\pi})\leq\langle\mathbf{g},\epsilon\mathbf{t}\rangle. |  |

Dividing by ϵ\epsilon and sending ϵ↓0\epsilon\downarrow 0, we have (by using the differentiability of J​(𝝅)J(\boldsymbol{\pi}) on the relative interior),

|  |  |  |
| --- | --- | --- |
|  | ⟨𝐠⋆​(𝝅),𝐭⟩≤⟨𝐠,𝐭⟩.\langle\mathbf{g}^{\star}(\boldsymbol{\pi}),\mathbf{t}\rangle\leq\langle\mathbf{g},\mathbf{t}\rangle. |  |

Repeating the argument for −𝐭∈TS​(𝝅)-\mathbf{t}\in T\_{S}(\boldsymbol{\pi}) we have

|  |  |  |
| --- | --- | --- |
|  | −⟨𝐠⋆​(𝝅),𝐭⟩≤−⟨𝐠,𝐭⟩.-\langle\mathbf{g}^{\star}(\boldsymbol{\pi}),\mathbf{t}\rangle\leq-\langle\mathbf{g},\mathbf{t}\rangle. |  |

Taking together ⟨𝐠⋆​(𝝅)−𝐠,𝐭⟩=0\langle\mathbf{g}^{\star}(\boldsymbol{\pi})-\mathbf{g},\mathbf{t}\rangle=0. But this implies that 𝐠−𝐠⋆​(𝝅)\mathbf{g}-\mathbf{g}^{\star}(\boldsymbol{\pi}) is orthogonal to every 𝐭∈TS​(𝝅)\mathbf{t}\in T\_{S}(\boldsymbol{\pi}). In particular, for the coordinates i∈Si\in S we must have gi=gi⋆​(𝝅)−λg\_{i}=g^{\star}\_{i}(\boldsymbol{\pi})-\lambda for some λ∈ℝ\lambda\in\mathbb{R}.

With this characterization of the coordinates in SS, consider the perturbation 𝐭=𝐞k−𝐞j\mathbf{t}=\mathbf{e}\_{k}-\mathbf{e}\_{j} for k∉Sk\not\in S and j∈Sj\in S. Once more, for sufficiently small ϵ>0\epsilon>0 we have that 𝝅+ϵ​𝐭∈Δn\boldsymbol{\pi}+\epsilon\mathbf{t}\in\Delta\_{n}. It follows that

|  |  |  |
| --- | --- | --- |
|  | J​(𝝅+ϵ​𝐭)−J​(𝝅)≤⟨𝐠,ϵ​𝐭⟩.J(\boldsymbol{\pi}+\epsilon\mathbf{t})-J(\boldsymbol{\pi})\leq\langle\mathbf{g},\epsilon\mathbf{t}\rangle. |  |

Dividing by ϵ\epsilon and sending ϵ↓0\epsilon\downarrow 0 we have that

|  |  |  |  |
| --- | --- | --- | --- |
| (B.2) |  | lim supϵ↓0J​(𝝅+ϵ​𝐭)−J​(𝝅)ϵ≤gk−gj=gk−gj⋆​(𝝅)+λ.\limsup\_{\epsilon\downarrow 0}\frac{J(\boldsymbol{\pi}+\epsilon\mathbf{t})-J(\boldsymbol{\pi})}{\epsilon}\leq g\_{k}-g\_{j}=g\_{k}-g\_{j}^{\star}(\boldsymbol{\pi})+\lambda. |  |

At the same time, we may apply the inequality log⁡(1+x)≥x/(1+x)\log(1+x)\geq x/(1+x) for x∈(−1,∞)x\in(-1,\infty) to conclude that for sufficiently small ϵ>0\epsilon>0

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡⟨𝝅+ϵ​𝐭,𝐑⟩−log⁡⟨𝝅,𝐑⟩\displaystyle\log\langle\boldsymbol{\pi}+\epsilon\mathbf{t},\mathbf{R}\rangle-\log\langle\boldsymbol{\pi},\mathbf{R}\rangle | =log⁡(⟨𝝅,𝐑⟩+ϵ​(Rk−Rj))−log⁡⟨𝝅,𝐑⟩\displaystyle=\log\left(\langle\boldsymbol{\pi},\mathbf{R}\rangle+\epsilon(R\_{k}-R\_{j})\right)-\log\langle\boldsymbol{\pi},\mathbf{R}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡(1+ϵ​(Rk−Rj)⟨𝝅,𝐑⟩)\displaystyle=\log\left(1+\frac{\epsilon(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥ϵ​(Rk−Rj)⟨𝝅,𝐑⟩1+ϵ​(Rk−Rj)⟨𝝅,𝐑⟩.\displaystyle\geq\frac{\frac{\epsilon(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}}{1+\frac{\epsilon(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}}. |  |

That is,

|  |  |  |
| --- | --- | --- |
|  | lim infϵ↓0log⁡⟨𝝅+ϵ​𝐭,𝐑⟩−log⁡⟨𝝅,𝐑⟩ϵ≥(Rk−Rj)⟨𝝅,𝐑⟩.\liminf\_{\epsilon\downarrow 0}\frac{\log\langle\boldsymbol{\pi}+\epsilon\mathbf{t},\mathbf{R}\rangle-\log\langle\boldsymbol{\pi},\mathbf{R}\rangle}{\epsilon}\geq\frac{(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}. |  |

Moreover since Rk≥0R\_{k}\geq 0, and j∈supp⁡(𝝅)j\in\operatorname{supp}(\boldsymbol{\pi}) we have that

|  |  |  |
| --- | --- | --- |
|  | ϵ​(Rk−Rj)⟨𝝅,𝐑⟩≥−ϵ​Rj⟨𝝅,𝐑⟩≥−ϵπj.\frac{\epsilon(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\geq-\frac{\epsilon R\_{j}}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\geq-\frac{\epsilon}{\pi\_{j}}. |  |

Specifically, as x↦x/(1+x)x\mapsto x/(1+x) is increasing on (−1,∞)(-1,\infty) the following inequalities hold for all ϵ≤πj/2\epsilon\leq\pi\_{j}/2:

|  |  |  |
| --- | --- | --- |
|  | 1ϵ​(log⁡⟨𝝅+ϵ​𝐭,𝐑⟩−log⁡⟨𝝅,𝐑⟩)≥(Rk−Rj)⟨𝝅,𝐑⟩1+ϵ​(Rk−Rj)⟨𝝅,𝐑⟩≥−1πj1−ϵπi≥−2πj.\frac{1}{\epsilon}\left(\log\langle\boldsymbol{\pi}+\epsilon\mathbf{t},\mathbf{R}\rangle-\log\langle\boldsymbol{\pi},\mathbf{R}\rangle\right)\geq\frac{\frac{(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}}{1+\frac{\epsilon(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}}\geq\frac{-\frac{1}{\pi\_{j}}}{1-\frac{\epsilon}{\pi\_{i}}}\geq-\frac{2}{\pi\_{j}}. |  |

This supplies a uniform lower bound, so by taking expectations and applying Fatou’s lemma we have

|  |  |  |  |
| --- | --- | --- | --- |
| (B.3) |  | lim infϵ↓0J​(𝝅+ϵ​𝐭)−J​(𝝅)ϵ≥𝔼​[(Rk−Rj)⟨𝝅,𝐑⟩]−(mk−mj)=gk⋆​(𝝅)−gj⋆​(𝝅).\liminf\_{\epsilon\downarrow 0}\frac{J(\boldsymbol{\pi}+\epsilon\mathbf{t})-J(\boldsymbol{\pi})}{\epsilon}\geq\mathbb{E}\left[\frac{(R\_{k}-R\_{j})}{\langle\boldsymbol{\pi},\mathbf{R}\rangle}\right]-(m\_{k}-m\_{j})=g^{\star}\_{k}(\boldsymbol{\pi})-g^{\star}\_{j}(\boldsymbol{\pi}). |  |

Combining our estimates ([B.2](https://arxiv.org/html/2510.25740v1#A2.E2 "In Appendix B Superdifferential set for the excess growth rate ‣ A mathematical study of the excess growth rate")) and ([B.3](https://arxiv.org/html/2510.25740v1#A2.E3 "In Appendix B Superdifferential set for the excess growth rate ‣ A mathematical study of the excess growth rate")) we have232323It is clear here that 𝐠⋆​(𝝅)\mathbf{g}^{\star}(\boldsymbol{\pi}) must be finite since −mj≤gj⋆​(𝝅)≤1/πj−mj-m\_{j}\leq g\_{j}^{\star}(\boldsymbol{\pi})\leq 1/\pi\_{j}-m\_{j} for all j∈Sj\in S, and −mk≤gk⋆​(𝝅)≤gk+λ-m\_{k}\leq g\_{k}^{\star}(\boldsymbol{\pi})\leq g\_{k}+\lambda for k∉Sk\not\in S.

|  |  |  |
| --- | --- | --- |
|  | gk⋆​(𝝅)−gj⋆​(𝝅)≤gk−gj⋆​(𝝅)+λ.g^{\star}\_{k}(\boldsymbol{\pi})-g^{\star}\_{j}(\boldsymbol{\pi})\leq g\_{k}-g\_{j}^{\star}(\boldsymbol{\pi})+\lambda. |  |

Equivalently, gk⋆​(𝝅)−λ≤gkg^{\star}\_{k}(\boldsymbol{\pi})-\lambda\leq g\_{k}.
Letting μk:=gk−(gk⋆​(𝝅)−λ)≥0\mu\_{k}:=g\_{k}-(g^{\star}\_{k}(\boldsymbol{\pi})-\lambda)\geq 0 for all k∉Sk\not\in S and μj=0\mu\_{j}=0 for j∈Sj\in S recovers the claimed representation for any 𝐠∈∂Δn+J​(𝝅)\mathbf{g}\in\partial\_{\Delta\_{n}}^{+}J(\boldsymbol{\pi}).
∎

## References

* [1]

  J. Aitchison.
  Principles of compositional data aanalysis.
  In Lecture Notes-Monograph Series, pages 73–81. Institute of Mathematical Statistics, 1994.
* [2]

  P. H. Algoet and T. M. Cover.
  Asymptotic optimality and asymptotic equipartition properties of log-optimum investment.
  The Annals of Probability, pages 876–898, 1988.
* [3]

  S.-I. Amari.
  α\alpha-divergence is unique, belonging to both ff-divergence and Bregman divergence classes.
  IEEE Transactions on Information Theory, 55(11):4925–4931, 2009.
* [4]

  S.-I. Amari.
  Information Geometry and Its Applications.
  Springer, 2016.
* [5]

  A. Banner, R. Fernholz, V. Papathanakos, J. Ruf, and D. Schofield.
  Diversification, volatility, and surprising alpha.
  Journal of Investment Consulting, 19(1):23–30, 2019.
* [6]

  J.-F. Bercher.
  Source coding with escort distributions and Rényi entropy bounds.
  Physics Letters A, 373(36):3235–3238, 2009.
* [7]

  D. Bertsekas.
  Convex optimization theory, volume 1.
  Athena Scientific, 2009.
* [8]

  D. G. Booth and E. F. Fama.
  Diversification returns and asset contributions.
  Financial Analysts Journal, 48(3):26–32, 1992.
* [9]

  D. Bordoli and R. Iijima.
  Convex cost of information via statistical divergence.
  arXiv preprint arXiv:2509.00229, 2025.
* [10]

  P. Bouchey, V. Nemtchinov, A. Paulsen, and D. M. Stein.
  Volatility harvesting: Why does diversifying and rebalancing create portfolio growth.
  The Journal of Wealth Management, 15(2):26–35, 2012.
* [11]

  P. Bouchey, V. Nemtchinov, and T.-K. L. Wong.
  Volatility harvesting in theory and practice.
  The Journal of Wealth Management, 18(3):89, 2015.
* [12]

  S. P. Boyd and L. Vandenberghe.
  Convex optimization.
  Cambridge University Press, 2004.
* [13]

  L. M. Bregman.
  The relaxation method of finding the common point of convex sets and its application to the solution of problems in convex programming.
  USSR Computational Mathematics and Mathematical Physics, 7(3):200–217, 1967.
* [14]

  L. Breiman.
  Optimal gambling systems for favorable games.
  In Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Contributions to the Theory of Statistics, volume 4, pages 65–79. University of California Press, 1961.
* [15]

  L. L. Campbell.
  A coding theorem and Rényi’s entropy.
  Information and Control, 8(4):423–429, 1965.
* [16]

  S. Campbell, Q. Song, and T.-K. L. Wong.
  Macroscopic properties of equity markets: stylized facts and portfolio performance.
  Quantitative Finance, 2025.
  Forthcoming.
* [17]

  T. M. Cover and J. A. Thomas.
  Elements of Information Theory.
  John Wiley & Sons, second edition, 2006.
* [18]

  T. M. Cover and J. A. Thomas.
  Elements of information theory.
  John Wiley & Sons, 2nd edition, 2006.
* [19]

  I. Csiszár.
  Axiomatic characterizations of information measures.
  Entropy, 10(3):261–273, 2008.
* [20]

  A. Dembo.
  Large Deviations: Techniques and Applications.
  Springer, 2009.
* [21]

  J. M. Dickey.
  Three multidimensional-integral identities with Bayesian applications.
  The Annals of Mathematical Statistics, pages 1615–1628, 1968.
* [22]

  C. Ding and H. Qi.
  An optimization study of diversification return portfolios.
  arXiv preprint arXiv:2303.01657, 2023.
* [23]

  B. Ebanks, P. Kannappan, and C. Ng.
  Generalized fundamental equation of information of multiplicative type.
  Aequationes Math, 32(1):19–31, 1987.
* [24]

  J. J. Egozcue, V. Pawlowsky-Glahn, G. Mateu-Figueras, and C. Barcelo-Vidal.
  Isometric logratio transformations for compositional data analysis.
  Mathematical Geology, 35(3):279–300, 2003.
* [25]

  I. Erb and N. Ay.
  The information-geometric perspective of compositional data analysis.
  In Advances in Compositional Data Analysis: Festschrift in Honour of Vera Pawlowsky-Glahn, pages 21–43. Springer, 2021.
* [26]

  E. R. Fernholz.
  Stochastic Portfolio Theory.
  Springer, 2002.
* [27]

  E. R. Fernholz, I. Karatzas, and J. Ruf.
  Volatility and arbitrage.
  The Annals of Applied Probability, 28(1):378–417, 2018.
* [28]

  R. Fernholz.
  On the diversity of equity markets.
  Journal of Mathematical Economics, 31(3):393–417, 1999.
* [29]

  R. Fernholz and I. Karatzas.
  Relative arbitrage in volatility-stabilized markets.
  Annals of Finance, 1(2):149–177, 2005.
* [30]

  R. Fernholz and I. Karatzas.
  Stochastic portfolio theory: an overview.
  In P. G. Ciarlet, editor, Handbook of Numerical Analysis, volume 15, pages 89–167. Elsevier, 2009.
* [31]

  R. Fernholz and C. Maguire Jr.
  The statistics of statistical arbitrage.
  Financial Analysts Journal, 63(5):46–52, 2007.
* [32]

  R. Fernholz and B. Shay.
  Stochastic portfolio theory and stock market equilibrium.
  The Journal of Finance, 37(2):615–624, 1982.
* [33]

  M. Grabisch, J.-L. Marichal, R. Mesiar, and E. Pap.
  Aggregation Functions.
  Cambridge University Press, 2009.
* [34]

  P. Kannappan.
  Functional Equations and Inequalities with Applications.
  Springer Science & Business Media, 2009.
* [35]

  P. Kannappan and C. Ng.
  On a generalized fundamental equation of information.
  Canadian Journal of Mathematics, 35(5):862–872, 1983.
* [36]

  J. L. Kelly.
  A new interpretation of information rate.
  The Bell System Technical Journal, 35(4):917–926, 1956.
* [37]

  M. Larsson, A. Ramdas, and J. Ruf.
  The numeraire ee-variable and reverse information projection.
  The Annals of Statistics, 53(3):1015–1043, 2025.
* [38]

  T. Leinster.
  Entropy and Diversity: The Axiomatic Approach.
  Cambridge University Press, 2021.
* [39]

  T. Leinster and C. A. Cobbold.
  Measuring diversity: the importance of species similarity.
  Ecology, 93(3):477–489, 2012.
* [40]

  L. C. MacLean, E. O. Thorp, and W. T. Ziemba.
  The Kelly Capital Growth Investment Criterion: Theory and Practice.
  World Scientific, 2011.
* [41]

  J.-M. Maeso and L. Martellini.
  Maximizing an equity portfolio excess growth rate: a new form of smart beta strategy?
  Quantitative Finance, 20(7):1185–1197, 2020.
* [42]

  P. C. Mahalanobis.
  On the generalized distance in statistics (reprint).
  Sankhyā: The Indian Journal of Statistics, Series A, 80:S1–S7, 2018.
* [43]

  D. Mantilla-Garcia, J. Malagon, and J. R. Aldana-Galindo.
  Can the portfolio excess growth rate explain the predictive power of idiosyncratic volatility?
  Finance Research Letters, 47:102577, 2022.
* [44]

  G. Mateu-Figueras, G. S. Monti, and J. Egozcue.
  Distributions on the simplex revisited.
  In Advances in Compositional Data Analysis: Festschrift in Honour of Vera Pawlowsky-Glahn, pages 61–82. Springer, 2021.
* [45]

  G. S. Monti, G. Mateu-Figueras, V. Pawlowsky-Glahn, and J. J. Egozcue.
  The shifted-scaled Dirichlet distribution in the simplex.
  In Proceedings of the 4th International Workshop on Compositional Data Analysis, 2011.
* [46]

  F. Nielsen, J.-D. Boissonnat, and R. Nock.
  Bregman voronoi diagrams: properties, algorithms and applications.
  arXiv preprint arXiv:0709.2196, 2007.
* [47]

  F. Orabona and K.-S. Jun.
  Tight concentrations and confidence sequences from the regret of universal portfolio.
  IEEE Transactions on Information Theory, 70(1):436–455, 2023.
* [48]

  S. Pal and T.-K. L. Wong.
  Energy, entropy, and arbitrage.
  arXiv preprint arXiv:1308.5376, 2013.
* [49]

  S. Pal and T.-K. L. Wong.
  The geometry of relative arbitrage.
  Mathematics and Financial Economics, 10(3):263–293, 2016.
* [50]

  S. Pal and T.-K. L. Wong.
  Exponentially concave functions and a new information geometry.
  The Annals of Probability, 46(2):1070–1113, 2018.
* [51]

  S. Pal and T.-K. L. Wong.
  Multiplicative Schrödinger problem and the Dirichlet transport.
  Probability Theory and Related Fields, 178(1):613–654, 2020.
* [52]

  R. K. Pathria and P. D. Beale.
  Statistical Mechanics.
  Academic Press, fourth edition, 2021.
* [53]

  Y. Polyanskiy and Y. Wu.
  Information Theory: From Coding to Learning.
  Cambridge University Press, 2025.
* [54]

  E. E. Qian.
  Portfolio Rebalancing.
  CRC Press, 2018.
* [55]

  A. Ramdas and R. Wang.
  Hypothesis testing with ee-values.
  arXiv preprint arXiv:2410.23614, 2024.
* [56]

  A. Rényi.
  On measures of entropy and information.
  In Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, volume 1: Contributions to the Theory of Statistics, volume 4, pages 547–562. University of California Press, 1961.
* [57]

  R. T. Rockafellar.
  Convex Analysis.
  Princeton University Press, 1997.
* [58]

  J. Ruf and K. Xie.
  The impact of proportional transaction costs on systematically generated portfolios.
  SIAM Journal on Financial Mathematics, 11(3):881–896, 2020.
* [59]

  C. E. Shannon.
  A mathematical theory of communication.
  The Bell System Technical Journal, 27(3):379–423, 1948.
* [60]

  X. Tian, T.-K. L. Wong, J. Yang, and J. Zhang.
  Maximum likelihood estimation for the λ\lambda-exponential family.
  arXiv preprint arXiv:2505.03582, 2025.
* [61]

  T. Van Erven and P. Harremos.
  Rényi divergence and Kullback-Leibler divergence.
  IEEE Transactions on Information Theory, 60(7):3797–3820, 2014.
* [62]

  S. Willenbrock.
  Diversification return, portfolio rebalancing, and the commodity return puzzle.
  Financial Analysts Journal, 67(4):42–49, 2011.
* [63]

  T.-K. L. Wong.
  Logarithmic divergences from optimal transport and Rényi geometry.
  Information Geometry, 1(1):39–78, 2018.
* [64]

  T.-K. L. Wong.
  Information geometry in portfolio theory.
  In Geometric Structures of Information, pages 105–136. Springer, 2019.
* [65]

  T.-K. L. Wong and J. Yang.
  Logarithmic divergences: geometry and interpretation of curvature.
  In International Conference on Geometric Science of Information, pages 413–422. Springer, 2019.
* [66]

  T.-K. L. Wong and J. Zhang.
  Tsallis and Rényi deformations linked via a new λ\lambda-duality.
  IEEE Transactions on Information Theory, 68(8):5353–5373, 2022.