---
authors:
- Andrea Conti
- Giacomo Morelli
doc_id: arxiv:2512.11731v1
family_id: arxiv:2512.11731
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Transfer Learning (Il)liquidity
url_abs: http://arxiv.org/abs/2512.11731v1
url_html: https://arxiv.org/html/2512.11731v1
venue: arXiv q-fin
version: 1
year: 2025
---


Andrea Conti
Department of Social and Economic Sciences,
Sapienza University of Rome,
00185 Rome, Italy
E-mail: <andrea.conti@uniroma1.it>.
  
Giacomo Morelli
Corresponding author:
Department of Statistical Sciences,
Sapienza University of Rome,
00185 Rome, Italy.
E-mail: <giacomo.morelli@uniroma1.it>

Abstract

The estimation of the Risk Neutral Density (RND) implicit in option prices is challenging, especially in illiquid markets. We introduce the Deep Log-Sum-Exp Neural Network, an architecture that leverages Deep and Transfer learning to address RND estimation in the presence of irregular and illiquid strikes. We prove key statistical properties of the model and the consistency of the estimator. We illustrate the benefits of transfer learning to improve the estimation of the RND in severe illiquidity conditions through Monte Carlo simulations, and we test it empirically on SPX data, comparing it with popular estimation methods. Overall, our framework shows recovery of the RND in conditions of extreme illiquidity with as few as three option quotes.

Keywords: Risk Neutral Density, Illiquidity, Transfer Learning, Neural Network, Deep Learning.

JEL classification: G12, G13, C45, C53, C58, C63.

## 1 Introduction

The risk-neutral density (RND) describes the risk-neutral distribution of prices at a specified horizon and combines expected outcomes with the market risk appetite. The correct estimation of the RND is central in asset pricing and financial risk management as it is used for pricing, hedging, construction of optimal portfolios, and market timing ([kostakis2011market]). This importance is amplified when option markets are illiquid and option quotes are scarce, since the resulting market incompleteness leaves infinitely many risk-neutral densities admissible ([almeida2023nonparametric]). In addition, as the expiration approaches the bid-ask spread increases ([hsieh2019volatility]), reducing the liquidity and making the recovery of the RND harder when it matters most.

Classical methods to estimate the RND fall into two broad classes: (i) parametric methods assume a specific RND shape or distributional form and estimate the parameters from option quotes; (ii) nonparametric methods estimate the RND by minimizing a data-driven criterion over a rich function class, typically with the addition of shape restrictions implied by no-arbitrage conditions. Parametric approaches can be further distinguished into expansion methods ([JARROW1982347]), generalized distribution and moment methods ([garcia2011estimation]), and mixture methods ([giacomini2008mixtures], [li2024parametric]). Nonparametric methods consist of maximum entropy approaches ([bondarenko2003estimation], [rompolis2010retrieving]), kernel regression estimations ([ait1998nonparametric], [ait2003nonparametric], [FENG20161]), and curve-fitting methods ([lu2021sieve], [frasso2022direct]).

The dense literature on RND estimation reflects the difficulty of the problem. Nonetheless, most approaches still rely on the assumption of market completeness, and the estimation of the RND in the presence of liquidity frictions remains unexplored, despite being a major challenge ([anthonisz2017asset], [glebkin2023illiquidity]).

In practice, quotes are available only at discrete and irregular strikes, even for the most liquid and traded stock options whereas much of the literature assumes frictionless and sufficiently broad option markets, restricting the estimation of the RND to a fine grid of strikes over a compact set. For example, a non-exhaustive list of examples covers approaches such as parametric expansion, generalized and mixture methods ([rompolis2008recovering], [li2024parametric]); and nonparametric methods based on curve fitting approaches ([monteiro2008recovering], [lai2014comparison], [frasso2022direct]). In other cases, the problem of data sparsity is confined to the tails ([bollinger2023principled]) and managed by extrapolation or non-arbitrage constraints. In any case, there is no ad-hoc method to estimate the RND in a situation of severe and structural illiquidity.

Furthermore, RND extraction is highly sensitive to grid design and numerical conditioning so that irregular strike spacing and the use of global or high-degree polynomial bases make the fit ill-conditioned ([ait2003nonparametric], [Jackwerth2004]). Consequently, approaches that infer the RND by twice differentiating the pricing function with respect to the strike ([Litzenberger1978]) amplify market noise and may lead to unstable results in settings with sparse and irregular quotes. It is essential to note that market noise, in addition to rendering highly sensitive fitting approaches such as entropy-based methods undesirable ([FENG20161]), can also lead to violation of asset-pricing theory and no-arbitrage principles. For example, curve-fitting approaches first interpolate the implied volatility curve and then derive the RND from the fitted curve. However, when market quotes are sparse and noisy, these methods can yield concave shapes.

We develop a framework to estimate the RND from European option prices in a setup of irregular, discrete, and illiquid quotes, filling the aforementioned gaps. We propose a deep learning model, Deep Log-Sum-Exp Neural Network (Deep-LSE), and prove key statistical properties such as its capacity to approximate any convex function and the consistency of the estimator. Our approach relies on transfer learning to overcome the difficulties of estimating the RND in conditions of illiquidity. We first train the model on a liquid proxy with dense, reliable option quotes, then transfer the learned structure to the illiquid target market, where a light fine-tune on sparse observations leverages the proxy-induced prior to stabilize pricing and for estimating the RND. We test our framework in a simulation environment using the [bates1996jumps], [kou2002jump], [andersen2002empirical] and Three-Factor double exponential stochastic volatility jump diffusion models ([andersen2015risk]), and empirically test it on SPX option data. We first estimate the ground truth RND from the full, liquid cross-section. We then emulate illiquidity by censoring most option quotes and fit our model on this reduced sample using transfer learning, hence enforcing the conditions of an illiquid market. Comparing the ground truth RND to the illiquid-fit RND reveals the model robustness under severe illiquidity and provides a clear visual check of model performance. Overall, our framework allows for the estimation of the RND in a situation of extreme market illiquidity, having as few as three option quotes available.

We contribute to the literature in two ways.
First, from a modelling perspective, our work contributes to a novel nonparametric approach to estimate the RND of illiquid option prices. Specifically, the combination of deep learning and transfer learning theory to address illiquidity is an approach new to the literature. We fit the implied volatility curve through Deep-LSE. Then, we use transfer learning to address the challenge of irregular, discrete, and illiquid quotes. The model learns on a liquid proxy and transfers the knowledge to the illiquid options market. We, thus, enrich the recent literature on nonparametric risk-neutral density estimation ([dalderop2020nonparametric], [almeida2023nonparametric], [qu2025estimating]) by introducing a novel deep-learning model that is specifically constructed for illiquid markets, rather than relying on methods developed for liquid conditions. Overall, the Deep Log-Sum-Exp Neural Network is a novel machine learning algorithm for regression tasks. It builds on the individual strengths of the Input Convex Neural Network ([amos2017input]) and the Log-Sum-Exp class of functions ([calafiore2019log]) to obtain a final model that ensures convexity and a deep, multilayer, Neural Network architecture. The latter is a crucial characteristic during the transfer learning phase where a deep architecture helps to embed knowledge and makes the transfer more effective.

Second, on theoretical grounds, we prove convexity in inputs, which is a crucial feature to interpolate implied volatilities. This property becomes critical in illiquid market conditions, where the lack of dense quotes and of reliable prior information on the volatility surface would otherwise leave the interpolation problem insufficiently constrained. We obtain analytical bounds that link the Deep-LSE model with the max-affine class function, which allows us to prove the Universal Approximation theorem for the Deep-LSE. This result establishes that the Deep-LSE architecture is expressive enough to approximate the implied volatility curve while preserving the convex structure required for stable fitting and interpolation even in conditions of extreme illiquidity. In addition, we prove the consistency of the estimator.

The rest of the paper is organized as follows. In Section [2](https://arxiv.org/html/2512.11731v1#S2 "2 Deep Transfer Learning for illiquid RND Estimation of European options ‣ Transfer Learning (Il)liquidity"), we present the methodology of transfer and deep learning to estimate the RND in illiquid markets. We show in Section [3](https://arxiv.org/html/2512.11731v1#S3 "3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") the theoretical framework of the Deep Log-Sum-Exp Neural Network, and its theoretical properties. In Section [4](https://arxiv.org/html/2512.11731v1#S4 "4 Simulation Studies ‣ Transfer Learning (Il)liquidity"), we perform a Monte Carlo simulation analysis to evaluate our framework. Specifically, we simulate the Bates model and emulate the condition of an illiquid market. Then, we estimate the Deep-LSE model and perform transfer learning to fit it on illiquid strikes, and compare the result with quadratic splines. In Section [5](https://arxiv.org/html/2512.11731v1#S5 "5 Empirical Analysis ‣ Transfer Learning (Il)liquidity"), we apply our framework to SPX option data to highlight the benefits of the method in illiquid market conditions.

## 2 Deep Transfer Learning for illiquid RND Estimation of European options

In a complete and arbitrage-free market, [COX1976] show that the value VtV\_{t} of a European option with payoff function Φ​(St;K)\Phi(S\_{t};K) at time tt, with expiry TT, term τ=T−t\tau=T-t and strike KK, is

|  |  |  |
| --- | --- | --- |
|  | Vt​(K,T)=e−r​τ​∫0∞Φ​(ST;K)​ft,T​(ST)​𝑑ST,V\_{t}(K,T)=e^{-r\tau}\int\_{0}^{\infty}\Phi(S\_{T};K)\,f\_{t,T}(S\_{T})\,dS\_{T}, |  |

where rr is the risk-free rate, STS\_{T} is the terminal price of the underlying and ft,Tf\_{t,T} is the terminal risk-neutral distribution of the underlying equity. For European options, the payoff is Φ​(ST;K)=(ST−K)+\Phi(S\_{T};K)=(S\_{T}-K)^{+} for calls and Φ​(ST;K)=(K−ST)+\Phi(S\_{T};K)=(K-S\_{T})^{+} for puts. Taking the second derivative with respect to strike ([Litzenberger1978]) yields the risk-neutral density

|  |  |  |
| --- | --- | --- |
|  | er​τ​∂2Vt​(K,T)∂K2=ft,T​(K).e^{r\tau}\frac{\partial^{2}V\_{t}(K,T)}{\partial K^{2}}=f\_{t,T}(K). |  |

In theory, one needs a continuum of option prices across strike levels for a given term in order to estimate the RND. However, only a discrete set of strikes is listed and actively traded, and many of these options suffer from low trading activity and wide bid–ask spreads. As a result, the available quotes may be noisy and sparse, particularly for deep in–the–money or deep out–of–the–money strikes. This sparsity and illiquidity often found in the option panels make it difficult to construct a reliable, continuous option price function across strikes, which, in turn, complicates the accurate estimation of the underlying risk–neutral density.

We leverage transfer learning to overcome the challenges posed by severe market illiquidity. In general, transfer learning involves first training a model, then fine-tuning it on a different dataset, resulting in modifications to the original model. This allows the model to utilize information learned during the initial training phase, which is especially useful when the new setting has limited data. In our setup, we estimate the implied RND for an illiquid options market using information transferred from a similar and liquid market. The deep and transfer learning–based approach proceeds in two phases:

* (i)

  First step recovery. We introduce Deep-LSE to model the implied volatility function in a liquid option market, where the underlying (proxy) asset closely resembles that of the illiquid option market of interest.
* (ii)

  Second step recovery. We fine-tune the learned implied volatility function with the data available from the illiquid option market. This method allows us to model accurately the implied volatility function of the illiquid option market. The Deep-LSE has learned in the first training phase the general feature of an implied volatility function and is able to interpolate the illiquid implied volatility function even with just a few observations.

Our method belongs to nonparametric volatility smoothing approach, as we first interpolate the volatility curve and then reconstruct the RND. We illustrate the steps in Algorithm [1](https://arxiv.org/html/2512.11731v1#alg1 "Algorithm 1 ‣ 2 Deep Transfer Learning for illiquid RND Estimation of European options ‣ Transfer Learning (Il)liquidity").

Algorithm 1  Transfer-learning-based estimation of the risk-neutral density

1:Liquid option dataset 𝒟liq\mathcal{D}^{\mathrm{liq}}, illiquid option dataset 𝒟ill\mathcal{D}^{\mathrm{ill}}, Deep-LSE fθf\_{\theta}, risk-free rate rr, maturity TT, strike grid {Kg}g=1G\{K\_{g}\}\_{g=1}^{G}

2:Estimated risk-neutral density f^t,T\hat{f}\_{t,T} for the illiquid market

3:First Step Recovery: Pre-training (liquid market)

4:Initialize parameters θ\theta of fθf\_{\theta}

5:Train fθf\_{\theta} on 𝒟liq\mathcal{D}^{\mathrm{liq}} to fit the implied volatility surface

6:Set θ⋆←θ\theta^{\star}\leftarrow\theta

7:

8:Second Step Recovery: Transfer learning (illiquid market)

9:Initialize fϕf\_{\phi} with ϕ←θ⋆\phi\leftarrow\theta^{\star}

10:Fine-tune fϕf\_{\phi} on 𝒟ill\mathcal{D}^{\mathrm{ill}}

11:Set ϕ⋆←ϕ\phi^{\star}\leftarrow\phi

12:

13:Volatility smoothing and RND extraction

14:for each strike KgK\_{g} in {Kg}g=1G\{K\_{g}\}\_{g=1}^{G} do

15:  Build feature vector xgx\_{g} (moneyness)

16:  σ^imp​(Kg,T)←fϕ⋆​(xg)\hat{\sigma}^{\mathrm{imp}}(K\_{g},T)\leftarrow f\_{\phi^{\star}}(x\_{g})

17:  V^t​(Kg,T)←OptionPrice​(σ^imp​(Kg,T),Kg,T,r)\hat{V}\_{t}(K\_{g},T)\leftarrow\text{OptionPrice}\big(\hat{\sigma}^{\mathrm{imp}}(K\_{g},T),K\_{g},T,r\big)

18:end for

19:Approximate ∂2V^t/∂K2\partial^{2}\hat{V}\_{t}/\partial K^{2} on {Kg}\{K\_{g}\} (finite differences)

20:For each KgK\_{g}, set f^t,T​(Kg)←er​τ​∂2V^t/∂K2​(Kg,T)\hat{f}\_{t,T}(K\_{g})\leftarrow e^{r\tau}\,\partial^{2}\hat{V}\_{t}/\partial K^{2}(K\_{g},T)

21:return f^t,T\hat{f}\_{t,T} on the strike grid

## 3 Deep Log-Sum-Exp Neural Network

In this section, we present the Deep Log-Sum-Exp Neural Network and the application of Transfer Learning for the estimation of the RND in an illiquid option market. In theory, transfer learning can be applied to various machine learning algorithms. We choose a Deep Neural Network architecture to leverage the flexibility of transfer learning and for the performance as an interpolation function. The deep architecture is a crucial characteristic during the transfer learning phase as it helps to embed knowledge and makes the transfer more effective. We illustrate the Deep-LSE with LL layers, and discuss an example with two layers in Appendix [A](https://arxiv.org/html/2512.11731v1#A1 "Appendix A Architecture of the Deep-LSE ‣ Transfer Learning (Il)liquidity").

Let x∈ℝdx\in\mathbb{R}^{d} denote the input, for each layer ℓ=1,…,L\ell=1,\dots,L, let Kℓ∈ℕK\_{\ell}\in\mathbb{N} be the number of affine pieces (neurons) and let Tℓ>0T\_{\ell}>0 be the temperature parameters, and cout∈ℝc\_{\mathrm{out}}\in\mathbb{R} be a global output bias. For a vector u=(u1,…,um)⊤∈ℝmu=(u\_{1},\dots,u\_{m})^{\top}\in\mathbb{R}^{m} and T>0T>0, define

|  |  |  |
| --- | --- | --- |
|  | LSET⁡(u)=T​log⁡(∑i=1meui/T),as ​T↓0,LSET⁡(u)→maxi⁡ui.\operatorname{LSE}\_{T}(u)\;=\;T\,\log\!\Big(\sum\_{i=1}^{m}e^{\,u\_{i}/T}\Big),\qquad\text{as }T\downarrow 0,\ \operatorname{LSE}\_{T}(u)\to\max\_{i}u\_{i}. |  |

For each layer ℓ=1,…,L\ell=1,\dots,L and each affince piece k=1,…,Kℓk=1,\dots,K\_{\ell}, define an affine function

|  |  |  |
| --- | --- | --- |
|  | ℓk(ℓ)​(x)=ak(ℓ)​x⊤+bk(ℓ),ak(ℓ)∈ℝd,bk(ℓ)∈ℝ.\ell^{(\ell)}\_{k}(x)\;=\;a^{(\ell)}\_{k}{}^{\!\top}x+b^{(\ell)}\_{k},\qquad a^{(\ell)}\_{k}\in\mathbb{R}^{d},\;b^{(\ell)}\_{k}\in\mathbb{R}. |  |

Stack them into the layer-wise affine vector

|  |  |  |
| --- | --- | --- |
|  | L(ℓ)​(x)=[ℓ1(ℓ)​(x)⋮ℓKℓ(ℓ)​(x)]∈ℝKℓ.L^{(\ell)}(x)=\begin{bmatrix}\ell^{(\ell)}\_{1}(x)\\ \vdots\\ \ell^{(\ell)}\_{K\_{\ell}}(x)\end{bmatrix}\in\mathbb{R}^{K\_{\ell}}. |  |

Let A(ℓ)∈ℝKℓ×dA^{(\ell)}\in\mathbb{R}^{K\_{\ell}\times d} collect the row vectors
(ak(ℓ))⊤(a^{(\ell)}\_{k})^{\top} and let b(ℓ)∈ℝKℓb^{(\ell)}\in\mathbb{R}^{K\_{\ell}} collect the biases, then

|  |  |  |
| --- | --- | --- |
|  | L(ℓ)​(x)=A(ℓ)​x+b(ℓ).L^{(\ell)}(x)=A^{(\ell)}x+b^{(\ell)}. |  |

For each layer ℓ=2,…,L\ell=2,\dots,L and each affine piece k=1,…,Kℓk=1,\dots,K\_{\ell}, define a nonnegative skip weight from zℓ−1​(x)z\_{\ell-1}(x) to the kk-th affine piece of layer ℓ\ell by

|  |  |  |
| --- | --- | --- |
|  | αk(ℓ)=softplus⁡(ηk(ℓ)),ηk(ℓ)∈ℝ,\alpha^{(\ell)}\_{k}\;=\;\operatorname{softplus}\!\big(\eta^{(\ell)}\_{k}\big),\qquad\eta^{(\ell)}\_{k}\in\mathbb{R}, |  |

and collect them into

|  |  |  |
| --- | --- | --- |
|  | α(ℓ)=(α1(ℓ),…,αKℓ(ℓ))⊤∈ℝ≥0Kℓ.\alpha^{(\ell)}=(\alpha^{(\ell)}\_{1},\ldots,\alpha^{(\ell)}\_{K\_{\ell}})^{\top}\in\mathbb{R}^{K\_{\ell}}\_{\geq 0}. |  |

The first-layer scalar output is

|  |  |  |
| --- | --- | --- |
|  | z1​(x)=LSET1⁡(L(1)​(x))=LSET1⁡(A(1)​x+b(1))∈ℝ.z\_{1}(x)\;=\;\operatorname{LSE}\_{T\_{1}}\!\big(L^{(1)}(x)\big)\;=\;\operatorname{LSE}\_{T\_{1}}\!\big(A^{(1)}x+b^{(1)}\big)\in\mathbb{R}. |  |

For each ℓ=2,…,L\ell=2,\dots,L, define the score vector

|  |  |  |
| --- | --- | --- |
|  | S(ℓ)​(x)=[α1(ℓ)​zℓ−1​(x)+ℓ1(ℓ)​(x)⋮αKℓ(ℓ)​zℓ−1​(x)+ℓKℓ(ℓ)​(x)]=α(ℓ)​zℓ−1​(x)+L(ℓ)​(x)∈ℝKℓ,S^{(\ell)}(x)\;=\;\begin{bmatrix}\alpha^{(\ell)}\_{1}z\_{\ell-1}(x)+\ell^{(\ell)}\_{1}(x)\\ \vdots\\ \alpha^{(\ell)}\_{K\_{\ell}}z\_{\ell-1}(x)+\ell^{(\ell)}\_{K\_{\ell}}(x)\end{bmatrix}\;=\;\alpha^{(\ell)}\,z\_{\ell-1}(x)+L^{(\ell)}(x)\;\in\;\mathbb{R}^{K\_{\ell}}, |  |

which yields

|  |  |  |
| --- | --- | --- |
|  | S(ℓ)​(x)=α(ℓ)​zℓ−1​(x)+A(ℓ)​x+b(ℓ).S^{(\ell)}(x)\;=\;\alpha^{(\ell)}\,z\_{\ell-1}(x)+A^{(\ell)}x+b^{(\ell)}. |  |

The scalar output of layer ℓ\ell is then

|  |  |  |
| --- | --- | --- |
|  | zℓ​(x)=LSETℓ⁡(S(ℓ)​(x))=Tℓ​log⁡(∑k=1Kℓe(αk(ℓ)​zℓ−1​(x)+ℓk(ℓ)​(x))/Tℓ)∈ℝ.z\_{\ell}(x)\;=\;\operatorname{LSE}\_{T\_{\ell}}\!\big(S^{(\ell)}(x)\big)\;=\;T\_{\ell}\log\!\Big(\sum\_{k=1}^{K\_{\ell}}e^{\,(\alpha^{(\ell)}\_{k}z\_{\ell-1}(x)+\ell^{(\ell)}\_{k}(x))/T\_{\ell}}\Big)\in\mathbb{R}. |  |

Finally, the Deep-LSE output is

|  |  |  |
| --- | --- | --- |
|  | y​(x)=zL​(x)+cout.y(x)\;=\;z\_{L}(x)+c\_{\mathrm{out}}. |  |

In compact form, the LL-layer Deep-LSE can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | z1​(x)\displaystyle z\_{1}(x) | =LSET1⁡(A(1)​x+b(1)),\displaystyle=\operatorname{LSE}\_{T\_{1}}\!\big(A^{(1)}x+b^{(1)}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | zℓ​(x)\displaystyle z\_{\ell}(x) | =LSETℓ⁡(α(ℓ)​zℓ−1​(x)+A(ℓ)​x+b(ℓ)),ℓ=2,…,L,\displaystyle=\operatorname{LSE}\_{T\_{\ell}}\!\big(\alpha^{(\ell)}z\_{\ell-1}(x)+A^{(\ell)}x+b^{(\ell)}\big),\qquad\ell=2,\dots,L, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(x)\displaystyle y(x) | =zL​(x)+cout.\displaystyle=z\_{L}(x)+c\_{\mathrm{out}}. |  |

### 3.1 Convexity

In practice, the estimation of the RND from illiquid option quotes is a challenging task. A common approach involves fitting the implied volatility curve of the available option quotes, converting them back to option prices, and then differentiating twice with respect to the strike to obtain the RND ([Litzenberger1978]). The level, shape, and curvature of the implied volatility curve are unknown and cannot be inferred accurately from illiquid quotes. For this reason, another crucial aspect of our model is that it is convex in its inputs and always returns a convex function. This property encourages the network to learn a meaningful and general representation of the implied volatility curve even under extreme illiquidity, without imposing convexity as an explicit modelling assumption and data requirement.

Lemma [3.1](https://arxiv.org/html/2512.11731v1#S3.Thmassumption1 "Lemma 3.1 (Monotone convex composition). ‣ 3.1 Convexity ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") describes the preservation of convexity under composition, and then we show that the Deep-LSE architecture is indeed convex with respect to its inputs. In particular, denote by z(ℓ):ℝd→ℝKℓz^{(\ell)}:\mathbb{R}^{d}\to\mathbb{R}^{K\_{\ell}} the output of layer ℓ\ell obtained by applying a log-sum-exp activation LSETℓ\operatorname{LSE}\_{T\_{\ell}} to an affine function of (x,z(ℓ−1)​(x))(x,z^{(\ell-1)}(x)) with nonnegative skip coefficients α(ℓ)≥0\alpha^{(\ell)}\geq 0, then each z(ℓ)z^{(\ell)} is convex in xx, and so is the scalar network output y​(x)y(x). The proofs of results related to convexity are reported in Appendix [B.1](https://arxiv.org/html/2512.11731v1#A2.SS1 "B.1 Convexity ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity").

###### Lemma 3.1 (Monotone convex composition).

Let h:ℝm→ℝh:\mathbb{R}^{m}\to\mathbb{R} be convex and nondecreasing in each coordinate, and let fi:ℝd→ℝf\_{i}:\mathbb{R}^{d}\to\mathbb{R} be convex for i=1,…,mi=1,\dots,m. Then x↦h​(f1​(x),…,fm​(x))x\mapsto h\big(f\_{1}(x),\dots,f\_{m}(x)\big) is convex.

###### Theorem 3.2 (Convexity of deep-LSE network).

Fix L∈ℕL\in\mathbb{N}. For each layer ℓ=1,…,L\ell=1,\dots,L, let Kℓ∈ℕK\_{\ell}\in\mathbb{N},
A(ℓ)∈ℝKℓ×dA^{(\ell)}\in\mathbb{R}^{K\_{\ell}\times d}, b(ℓ)∈ℝKℓb^{(\ell)}\in\mathbb{R}^{K\_{\ell}},
and Tℓ>0T\_{\ell}>0. For ℓ≥2\ell\geq 2 let α(ℓ)∈ℝ≥0Kℓ\alpha^{(\ell)}\in\mathbb{R}^{K\_{\ell}}\_{\geq 0}
(elementwise nonnegative). Define

|  |  |  |
| --- | --- | --- |
|  | z(1)​(x)=LSET1⁡(A(1)​x+b(1)),S(ℓ)​(x)=α(ℓ)​z(ℓ−1)​(x)+A(ℓ)​x+b(ℓ)(ℓ≥2),z^{(1)}(x)\;=\;\operatorname{LSE}\_{T\_{1}}\!\big(A^{(1)}x+b^{(1)}\big),\qquad S^{(\ell)}(x)\;=\;\alpha^{(\ell)}z^{(\ell-1)}(x)+A^{(\ell)}x+b^{(\ell)}\ \ (\ell\geq 2), |  |

|  |  |  |
| --- | --- | --- |
|  | z(ℓ)​(x)=LSETℓ⁡(S(ℓ)​(x))(ℓ≥2),y​(x)=z(L)​(x)+cout.z^{(\ell)}(x)\;=\;\operatorname{LSE}\_{T\_{\ell}}\!\big(S^{(\ell)}(x)\big)\ \ (\ell\geq 2),\qquad y(x)=z^{(L)}(x)+c\_{\mathrm{out}}. |  |

Then y:ℝd→ℝy:\mathbb{R}^{d}\to\mathbb{R} is convex in xx, as each z(ℓ)z^{(\ell)} is convex.

We illustrate in Example [3.3](https://arxiv.org/html/2512.11731v1#S3.Thmassumption3 "Example 3.3 (Convexity of the Deep-LSE network with 2 layers.). ‣ 3.1 Convexity ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") the 2-layer case of our Deep-LSE.

###### Example 3.3 (Convexity of the Deep-LSE network with 2 layers.).

Fix T1,T2>0T\_{1},T\_{2}>0 and K1,K2∈ℕK\_{1},K\_{2}\in\mathbb{N}. Let

|  |  |  |
| --- | --- | --- |
|  | z1​(x)=LSET1⁡(A(1)​x+b(1))andy​(x)=LSET2⁡(α​z1​(x)+A(2)​x+b(2))+cout,z\_{1}(x)=\operatorname{LSE}\_{T\_{1}}\!\big(A^{(1)}x+b^{(1)}\big)\qquad\text{and}\qquad y(x)=\operatorname{LSE}\_{T\_{2}}\!\big(\alpha\,z\_{1}(x)+A^{(2)}x+b^{(2)}\big)+c\_{\mathrm{out}}, |  |

where A(1)∈ℝK1×dA^{(1)}\in\mathbb{R}^{K\_{1}\times d}, b(1)∈ℝK1b^{(1)}\in\mathbb{R}^{K\_{1}}, A(2)∈ℝK2×dA^{(2)}\in\mathbb{R}^{K\_{2}\times d}, b(2)∈ℝK2b^{(2)}\in\mathbb{R}^{K\_{2}}, and α=(α1,…,αK2)⊤∈ℝ≥0K2\alpha=(\alpha\_{1},\dots,\alpha\_{K\_{2}})^{\top}\in\mathbb{R}^{K\_{2}}\_{\geq 0} has nonnegative entries. Then y:ℝd→ℝy:\mathbb{R}^{d}\to\mathbb{R} is a convex function of xx.

### 3.2 Bounds

Given any number of layers ℓ=1,…​L\ell=1,...L, our model z(ℓ)​(x)z^{(\ell)}(x) is a combination of affine transformations, skip connection, and push-forward Log-Sum-Exp class of functions. This class of functions are important because  as ​T↓0,LSET⁡(u)→maxi⁡ui\text{ as }T\downarrow 0,\operatorname{LSE}\_{T}(u)\to\max\_{i}u\_{i}. In other words, it is possible to establish bounds between z(ℓ)​(x)z^{(\ell)}(x) and the max-affine class of functions. In turn, the max-affine class of functions is known to be a universal approximator of convex functions under certain conditions. By induction, we obtain the analytical bounds for ℓ\ell layers in Theorem [3.4](https://arxiv.org/html/2512.11731v1#S3.Thmassumption4 "Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity"). In Appendix [B.2](https://arxiv.org/html/2512.11731v1#A2.SS2 "B.2 Bounds ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity"), we report the proof.

###### Theorem 3.4 (Deep-LSE vs. deep max–affine: LL layers).

Fix L∈ℕL\in\mathbb{N} and, for each layer ℓ=1,…,L\ell=1,\dots,L, let Kℓ∈ℕK\_{\ell}\in\mathbb{N}, temperatures Tℓ>0T\_{\ell}>0, parameters A(ℓ)∈ℝKℓ×d,b(ℓ)∈ℝKℓA^{(\ell)}\in\mathbb{R}^{K\_{\ell}\times d},\quad b^{(\ell)}\in\mathbb{R}^{K\_{\ell}},
and skip vectors α(ℓ)=(α1(ℓ),…,αKℓ(ℓ))⊤∈ℝ≥0Kℓ\alpha^{(\ell)}=(\alpha^{(\ell)}\_{1},\dots,\alpha^{(\ell)}\_{K\_{\ell}})^{\top}\in\mathbb{R}^{K\_{\ell}}\_{\geq 0} for ℓ≥2\ell\geq 2.
Define the layerwise affine pieces

|  |  |  |
| --- | --- | --- |
|  | ℓk(ℓ)​(x)=⟨Ak,⋅(ℓ),x⟩+bk(ℓ),k=1,…,Kℓ,\ell^{(\ell)}\_{k}(x)\ =\ \big\langle A^{(\ell)}\_{k,\cdot},x\big\rangle+b^{(\ell)}\_{k},\quad k=1,\dots,K\_{\ell}, |  |

and the Deep-LSE recursion (scalar outputs at every layer)

|  |  |  |
| --- | --- | --- |
|  | z(1)​(x)=LSET1⁡({ℓk(1)​(x)}k=1K1),z(ℓ)​(x)=LSETℓ⁡({αk(ℓ)​z(ℓ−1)​(x)+ℓk(ℓ)​(x)}k=1Kℓ)(ℓ≥2).z^{(1)}(x)\ =\ \operatorname{LSE}\_{T\_{1}}\!\big(\{\ell^{(1)}\_{k}(x)\}\_{k=1}^{K\_{1}}\big),\qquad z^{(\ell)}(x)\ =\ \operatorname{LSE}\_{T\_{\ell}}\!\big(\{\alpha^{(\ell)}\_{k}\,z^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\}\_{k=1}^{K\_{\ell}}\big)\quad(\ell\geq 2). |  |

Let the deep max–affine surrogate be defined by

|  |  |  |
| --- | --- | --- |
|  | z¯(1)​(x)=maxi∈[K1]⁡ℓi(1)​(x),z¯(ℓ)​(x)=maxk∈[Kℓ]⁡(αk(ℓ)​z¯(ℓ−1)​(x)+ℓk(ℓ)​(x))(ℓ≥2).\bar{z}^{(1)}(x)\ =\ \max\_{i\in[K\_{1}]}\ \ell^{(1)}\_{i}(x),\qquad\bar{z}^{(\ell)}(x)\ =\ \max\_{k\in[K\_{\ell}]}\ \Big(\alpha^{(\ell)}\_{k}\,\bar{z}^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\Big)\quad(\ell\geq 2). |  |

For each ℓ\ell, set αmax(ℓ)=‖α(ℓ)‖∞=maxk⁡αk(ℓ)\alpha^{(\ell)}\_{\max}=\|\alpha^{(\ell)}\|\_{\infty}=\max\_{k}\alpha^{(\ell)}\_{k}, with the convention αmax(1)=1\alpha^{(1)}\_{\max}=1.
Then for every ℓ=1,…,L\ell=1,\dots,L and every x∈ℝdx\in\mathbb{R}^{d},

|  |  |  |  |
| --- | --- | --- | --- |
|  | z¯(ℓ)​(x)≤z(ℓ)​(x)≤z¯(ℓ)​(x)+Δℓ,\bar{z}^{(\ell)}(x)\ \leq\ z^{(\ell)}(x)\ \leq\ \bar{z}^{(\ell)}(x)\ +\ \Delta\_{\ell}, |  | (3.1) |

where Δℓ\Delta\_{\ell} satisfies the recursion

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ1=T1​log⁡K1,Δℓ=Tℓ​log⁡Kℓ+αmax(ℓ)​Δℓ−1(ℓ≥2),\Delta\_{1}=T\_{1}\log K\_{1},\qquad\Delta\_{\ell}\ =\ T\_{\ell}\log K\_{\ell}\ +\ \alpha^{(\ell)}\_{\max}\,\Delta\_{\ell-1}\quad(\ell\geq 2), |  | (3.2) |

and, equivalently, the closed form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δℓ=∑j=1ℓ(Tj​log⁡Kj​∏r=j+1ℓαmax(r)).\Delta\_{\ell}\ =\ \sum\_{j=1}^{\ell}\Bigg(T\_{j}\log K\_{j}\ \prod\_{r=j+1}^{\ell}\alpha^{(r)}\_{\max}\Bigg). |  | (3.3) |

where empty products are equal to 1. In particular, if the network output is y​(x)=z(L)​(x)+couty(x)=z^{(L)}(x)+c\_{\mathrm{out}} and
y¯​(x)=z¯(L)​(x)+cout\bar{y}(x)=\bar{z}^{(L)}(x)+c\_{\mathrm{out}}, then

|  |  |  |
| --- | --- | --- |
|  | y¯(x)≤y(x)≤y¯(x)+ΔLfor all x∈ℝd.\bar{y}(x)\ \ \leq\ y(x)\ \leq\ \bar{y}(x)\ +\ \Delta\_{L}\qquad\text{for all }x\in\mathbb{R}^{d}. |  |

We illustrate how to obtain the analytical bounds for a two-layer Deep-LSE model in Example [3.5](https://arxiv.org/html/2512.11731v1#S3.Thmassumption5 "Example 3.5 (Two-layer LSE vs. deep max-affine bounds). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity").

###### Example 3.5 (Two-layer LSE vs. deep max-affine bounds).

Fix T1,T2>0T\_{1},T\_{2}>0, integers K1,K2∈ℕK\_{1},K\_{2}\in\mathbb{N}, and data
A(1)∈ℝK1×dA^{(1)}\!\in\mathbb{R}^{K\_{1}\times d}, b(1)∈ℝK1b^{(1)}\!\in\mathbb{R}^{K\_{1}},
A(2)∈ℝK2×dA^{(2)}\!\in\mathbb{R}^{K\_{2}\times d}, b(2)∈ℝK2b^{(2)}\!\in\mathbb{R}^{K\_{2}},
and a nonnegative skip vector α=(α1,…,αK2)⊤∈ℝ≥0K2\alpha=(\alpha\_{1},\ldots,\alpha\_{K\_{2}})^{\top}\in\mathbb{R}^{K\_{2}}\_{\geq 0}.
Define

|  |  |  |
| --- | --- | --- |
|  | z1​(x)=LSET1⁡(A(1)​x+b(1)),y​(x)=LSET2⁡(α​z1​(x)+A(2)​x+b(2))+cout.z\_{1}(x)=\operatorname{LSE}\_{T\_{1}}\!\big(A^{(1)}x+b^{(1)}\big),\qquad y(x)=\operatorname{LSE}\_{T\_{2}}\!\big(\alpha\,z\_{1}(x)+A^{(2)}x+b^{(2)}\big)+c\_{\mathrm{out}}. |  |

Let the associated max-affine surrogates be

|  |  |  |
| --- | --- | --- |
|  | z¯1​(x)=maxi∈[K1]⁡⟨Ai,⋅(1),x⟩+bi(1),y¯​(x)=maxk∈[K2]⁡(αk​z¯1​(x)+⟨Ak,⋅(2),x⟩+bk(2))+cout.\bar{z}\_{1}(x)=\max\_{i\in[K\_{1}]}\big\langle A^{(1)}\_{i,\cdot},x\big\rangle+b^{(1)}\_{i},\qquad\bar{y}(x)=\max\_{k\in[K\_{2}]}\Big(\alpha\_{k}\,\bar{z}\_{1}(x)+\big\langle A^{(2)}\_{k,\cdot},x\big\rangle+b^{(2)}\_{k}\Big)+c\_{\mathrm{out}}. |  |

Then, with αmax=‖α‖∞=maxk⁡αk\alpha\_{\max}=\|\alpha\|\_{\infty}=\max\_{k}\alpha\_{k},

|  |  |  |
| --- | --- | --- |
|  | y¯​(x)≤y​(x)≤y¯​(x)+T2​log⁡K2+αmax​T1​log⁡K1for all ​x∈ℝd.\quad\bar{y}(x)\ \leq\ y(x)\ \leq\ \bar{y}(x)\;+\;T\_{2}\log K\_{2}\;+\;\alpha\_{\max}\,T\_{1}\log K\_{1}\quad\qquad\text{for all }x\in\mathbb{R}^{d}. |  |

The inequalities crucially use αk(ℓ)≥0\alpha^{(\ell)}\_{k}\geq 0 to preserve monotonicity across layers. In fact, z(ℓ−1)≥z¯(ℓ−1)z^{(\ell-1)}\geq\bar{z}^{(\ell-1)} implies αk(ℓ)​z(ℓ−1)≥αk(ℓ)​z¯(ℓ−1)\alpha^{(\ell)}\_{k}z^{(\ell-1)}\geq\alpha^{(\ell)}\_{k}\bar{z}^{(\ell-1)}.
In case some αk(ℓ)\alpha^{(\ell)}\_{k} were negative, the lower bound could fail. Notice also that Δℓ\Delta\_{\ell} is
independent of xx, hence the approximation error z(ℓ)−z¯(ℓ)z^{(\ell)}-\bar{z}^{(\ell)} is uniformly bounded over ℝd\mathbb{R}^{d}.

If, for some layer ℓ\ell, all coordinates of u(ℓ)​(x)u^{(\ell)}(x) coincide, then z(ℓ)​(x)=z¯(ℓ)​(x)+Tℓ​log⁡Kℓz^{(\ell)}(x)=\bar{z}^{(\ell)}(x)+T\_{\ell}\log K\_{\ell}, and the right-hand inequality is tight there. As Tj↓0T\_{j}\downarrow 0 for all jj, LSETj\operatorname{LSE}\_{T\_{j}} converges pointwise to the max, so Δℓ↓0\Delta\_{\ell}\downarrow 0 and z(ℓ)→z¯(ℓ)z^{(\ell)}\to\bar{z}^{(\ell)}. It is important to notice that the multiplicative term

|  |  |  |
| --- | --- | --- |
|  | ΔL=∑j=1L(Tj​log⁡Kj​∏r=j+1Lαmax(r))\Delta\_{L}=\sum\_{j=1}^{L}\Bigl(T\_{j}\log K\_{j}\,\prod\_{r=j+1}^{L}\alpha\_{\max}^{(r)}\Bigr) |  |

is crucial for the upper bound defined in Theorem [3.4](https://arxiv.org/html/2512.11731v1#S3.Thmassumption4 "Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity"). It makes the dependence on the nonnegative skips αmax(ℓ)\alpha\_{\max}^{(\ell)} explicit, and the behavior as depth grows is governed by the tail products

|  |  |  |
| --- | --- | --- |
|  | Pj,L=∏r=j+1Lαmax(r).P\_{j,L}=\prod\_{r=j+1}^{L}\alpha\_{\max}^{(r)}. |  |

Define the infinite-depth limit Δ∞=limL→∞ΔL\Delta\_{\infty}=\lim\_{L\to\infty}\Delta\_{L} if it exists

|  |  |  |
| --- | --- | --- |
|  | Δ∞=∑j=1∞(Tj​log⁡Kj​Pj,∞),Pj,∞=∏r=j+1∞αmax(r).\Delta\_{\infty}=\sum\_{j=1}^{\infty}\Bigl(T\_{j}\log K\_{j}\,P\_{j,\infty}\Bigr),\qquad P\_{j,\infty}=\prod\_{r=j+1}^{\infty}\alpha\_{\max}^{(r)}. |  |

So Δ∞<∞\Delta\_{\infty}<\infty if and only if this series converges. That reduces the question to when the infinite product Pj,∞P\_{j,\infty} decays fast enough.
A necessary and sufficient condition for the product is

|  |  |  |
| --- | --- | --- |
|  | ∏r=j+1∞αmax(r)=0⟺∑r=j+1∞log⁡αmax(r)=−∞.\prod\_{r=j+1}^{\infty}\alpha\_{\max}^{(r)}=0\quad\Longleftrightarrow\quad\sum\_{r=j+1}^{\infty}\log\alpha\_{\max}^{(r)}=-\infty. |  |

Thus, if ∑rlog⁡αmax(r)=−∞\sum\_{r}\log\alpha\_{\max}^{(r)}=-\infty, the skips are on average contracting, then Pj,∞=0P\_{j,\infty}=0 and the only remaining question is whether the weighted series of Tj​log⁡KjT\_{j}\log K\_{j} against these vanishing tails converges. If there exists q<1q<1 with αmax(ℓ)≤q\alpha\_{\max}^{(\ell)}\leq q for all sufficiently large ℓ\ell, then

|  |  |  |
| --- | --- | --- |
|  | Pj,L≤qL−j.P\_{j,L}\leq q^{\,L-j}. |  |

In addition, if Tj​log⁡Kj≤MT\_{j}\log K\_{j}\leq M (bounded temperatures and widths), then for every LL,

|  |  |  |
| --- | --- | --- |
|  | ∑j=1LqL−j=qL−1+qL−2+⋯+q1+q0=∑k=0L−1qk=1−qL1−q(q≠1).\sum\_{j=1}^{L}q^{L-j}=q^{L-1}+q^{L-2}+\cdots+q^{1}+q^{0}=\sum\_{k=0}^{L-1}q^{k}=\frac{1-q^{L}}{1-q}\quad(q\neq 1). |  |

|  |  |  |
| --- | --- | --- |
|  | ΔL≤M​∑j=1LqL−j=M​1−qL1−q≤M1−q,\Delta\_{L}\leq M\sum\_{j=1}^{L}q^{L-j}=M\frac{1-q^{L}}{1-q}\leq\frac{M}{1-q}, |  |

so ΔL\Delta\_{L} is uniformly bounded in depth and Δ∞≤M1−q.\Delta\_{\infty}\leq\frac{M}{1-q}. We enforce q<1q<1 with αmax(ℓ)≤q\alpha\_{\max}^{(\ell)}\leq q, and the bound for ℓ\ell layers-Deep-LSE network becomes

|  |  |  |
| --- | --- | --- |
|  | y¯(x)≤y(x)≤y¯(x)+M1−qfor all x∈ℝd.\bar{y}(x)\ \leq\ y(x)\ \ \leq\ \bar{y}(x)+\frac{M}{1-q}\qquad\text{for all }x\in\mathbb{R}^{d}. |  |

### 3.3 Universal Approximation

The result of Theorem [3.4](https://arxiv.org/html/2512.11731v1#S3.Thmassumption4 "Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") is crucial to link the class of functions of the Deep-LSE model to the max-affine function, a universal approximator of convex functions. We leverage these results of convex analysis to prove that our model is a universal approximator of convex functions and data points.
In our setup, we obtain the deep surrogate of max-affine functions because our framework accommodates ℓ≥1\ell\geq 1. For this reason, in Theorem [3.6](https://arxiv.org/html/2512.11731v1#S3.Thmassumption6 "Theorem 3.6 (Deep max–affine surrogate is a finite max of affines). ‣ 3.3 Universal Approximation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") we show that each layer of the deep max–affine surrogate preserves a piecewise–affine structure, so that the overall mapping can be interpreted as the pointwise maximum of finitely many affine functions. In particular, the network output remains a convex and continuous function of the input. The proofs are in Appendix [B.3](https://arxiv.org/html/2512.11731v1#A2.SS3 "B.3 Universal Approximation Theorem ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity").

###### Theorem 3.6 (Deep max–affine surrogate is a finite max of affines).

Let d,L∈ℕd,L\in\mathbb{N}, let Kℓ∈ℕK\_{\ell}\in\mathbb{N} for ℓ=1,…,L\ell=1,\dots,L, and fix parameters Ak(ℓ)∈ℝd,bk(ℓ)∈ℝ(ℓ=1,…,L;k=1,…,Kℓ)A\_{k}^{(\ell)}\in\mathbb{R}^{d},\quad b\_{k}^{(\ell)}\in\mathbb{R}\quad(\ell=1,\dots,L;\ k=1,\dots,K\_{\ell}) and strictly positive scalars αk(ℓ)>0\alpha\_{k}^{(\ell)}>0 for ℓ=2,…,L\ell=2,\dots,L and k=1,…,Kℓk=1,\dots,K\_{\ell}.
For x∈ℝdx\in\mathbb{R}^{d} define recursively

|  |  |  |
| --- | --- | --- |
|  | z¯(1)​(x)=max1≤k≤K1⁡(⟨Ak(1),x⟩+bk(1)),z¯(ℓ)​(x)=max1≤k≤Kℓ⁡(αk(ℓ)​z¯(ℓ−1)​(x)+⟨Ak(ℓ),x⟩+bk(ℓ))(ℓ≥2),\bar{z}^{(1)}(x)=\max\_{1\leq k\leq K\_{1}}\bigl(\langle A^{(1)}\_{k},x\rangle+b^{(1)}\_{k}\bigr),\qquad\bar{z}^{(\ell)}(x)=\max\_{1\leq k\leq K\_{\ell}}\Bigl(\alpha^{(\ell)}\_{k}\,\bar{z}^{(\ell-1)}(x)+\langle A^{(\ell)}\_{k},x\rangle+b^{(\ell)}\_{k}\Bigr)\ \ (\ell\geq 2), |  |

and set y¯​(x)=z¯(L)​(x)+cout\bar{y}(x)=\bar{z}^{(L)}(x)+c\_{\mathrm{out}} for some cout∈ℝc\_{\mathrm{out}}\in\mathbb{R}.
Define the path sets Pℓ={1,…,K1}×⋯×{1,…,Kℓ}P\_{\ell}=\{1,\dots,K\_{1}\}\times\cdots\times\{1,\dots,K\_{\ell}\} with |Pℓ|=∏j=1ℓKj<∞|P\_{\ell}|=\prod\_{j=1}^{\ell}K\_{j}<\infty.
Then there exist affine coefficients {(Ap[ℓ],bp[ℓ])}p∈Pℓ⊂ℝd×ℝ\{(A\_{p}^{[\ell]},b\_{p}^{[\ell]})\}\_{p\in P\_{\ell}}\subset\mathbb{R}^{d}\times\mathbb{R} such that, for every ℓ=1,…,L\ell=1,\dots,L,

|  |  |  |
| --- | --- | --- |
|  | z¯(ℓ)​(x)=maxp∈Pℓ⁡(⟨Ap[ℓ],x⟩+bp[ℓ])for all ​x∈ℝd,\bar{z}^{(\ell)}(x)=\max\_{p\in P\_{\ell}}\bigl(\langle A\_{p}^{[\ell]},x\rangle+b\_{p}^{[\ell]}\bigr)\quad\text{for all }x\in\mathbb{R}^{d}, |  |

with the recursion

|  |  |  |
| --- | --- | --- |
|  | A(k1)[1]=Ak1(1),b(k1)[1]=bk1(1),A(p,k)[ℓ]=αk(ℓ)​Ap[ℓ−1]+Ak(ℓ),b(p,k)[ℓ]=αk(ℓ)​bp[ℓ−1]+bk(ℓ),A^{[1]}\_{(k\_{1})}=A^{(1)}\_{k\_{1}},\quad b^{[1]}\_{(k\_{1})}=b^{(1)}\_{k\_{1}},\qquad A^{[\ell]}\_{(p,k)}=\alpha^{(\ell)}\_{k}\,A^{[\ell-1]}\_{p}+A^{(\ell)}\_{k},\quad b^{[\ell]}\_{(p,k)}=\alpha^{(\ell)}\_{k}\,b^{[\ell-1]}\_{p}+b^{(\ell)}\_{k}, |  |

for p∈Pℓ−1p\in P\_{\ell-1} and k∈{1,…,Kℓ}k\in\{1,\dots,K\_{\ell}\}.
Consequently,

|  |  |  |
| --- | --- | --- |
|  | y¯​(x)=maxp∈PL⁡(⟨Ap[L],x⟩+bp[L])+cout,\bar{y}(x)=\max\_{p\in P\_{L}}\bigl(\langle A^{[L]}\_{p},x\rangle+b^{[L]}\_{p}\bigr)+c\_{\mathrm{out}}, |  |

so y¯\bar{y} is a finite pointwise maximum of affine functions, hence convex and continuous.
Moreover, for p=(k1,…,kℓ)∈Pℓp=(k\_{1},\dots,k\_{\ell})\in P\_{\ell},

|  |  |  |
| --- | --- | --- |
|  | Ap[ℓ]=∑j=1ℓ(∏r=j+1ℓαkr(r))​Akj(j),bp[ℓ]=∑j=1ℓ(∏r=j+1ℓαkr(r))​bkj(j),A\_{p}^{[\ell]}=\sum\_{j=1}^{\ell}\Bigl(\prod\_{r=j+1}^{\ell}\alpha^{(r)}\_{k\_{r}}\Bigr)A^{(j)}\_{k\_{j}},\qquad b\_{p}^{[\ell]}=\sum\_{j=1}^{\ell}\Bigl(\prod\_{r=j+1}^{\ell}\alpha^{(r)}\_{k\_{r}}\Bigr)b^{(j)}\_{k\_{j}}, |  |

with the convention that an empty product equals 11.

The next is a universal approximation result for the Deep-LSE architecture on the class of continuous convex functions. Given a compact convex set K⊂ℝdK\subset\mathbb{R}^{d} and a continuous convex map f:K→ℝf:K\to\mathbb{R}, it asserts that, for any tolerance ε>0\varepsilon>0, one can choose the weights, nonnegative skip coefficients α(ℓ)\alpha^{(\ell)}, and temperatures Tℓ>0T\_{\ell}>0 of an LL-layer Deep-LSE network so that its class of functions are dense, in the uniform norm on KK, in the space of continuous convex functions on KK.

###### Theorem 3.7 (Uniform approximation on a compact convex set by an LL-layer Deep-LSE network).

Let K⊂ℝdK\subset\mathbb{R}^{d} be compact and convex, and let f:K→ℝf:K\to\mathbb{R} be continuous and convex.
Fix a depth L∈ℕL\in\mathbb{N} and widths K1,…,KL∈ℕK\_{1},\dots,K\_{L}\in\mathbb{N}. Consider the LL-layer Deep-LSE model with parameters

|  |  |  |
| --- | --- | --- |
|  | A(ℓ)∈ℝKℓ×d,b(ℓ)∈ℝKℓ,α(ℓ)∈ℝ≥0Kℓ​(ℓ≥2),Tℓ>0,A^{(\ell)}\in\mathbb{R}^{K\_{\ell}\times d},\quad b^{(\ell)}\in\mathbb{R}^{K\_{\ell}},\quad\alpha^{(\ell)}\in\mathbb{R}\_{\geq 0}^{K\_{\ell}}\ (\ell\geq 2),\quad T\_{\ell}>0, |  |

Then, for every ε>0\varepsilon>0, there exist parameters {A(ℓ),b(ℓ),α(ℓ)}ℓ=1L\{A^{(\ell)},b^{(\ell)},\alpha^{(\ell)}\}\_{\ell=1}^{L} with α(ℓ)≥0\alpha^{(\ell)}\geq 0 and positive temperatures {Tℓ}ℓ=1L\{T\_{\ell}\}\_{\ell=1}^{L} such that

|  |  |  |
| --- | --- | --- |
|  | supx∈K|y​(x)−f​(x)|<ε.\sup\_{x\in K}\,|y(x)-f(x)|\ <\ \varepsilon. |  |

### 3.4 Sieve M-Estimation

Consider a nonparametric regression problem

|  |  |  |
| --- | --- | --- |
|  | yi=f0​(xi)+ϵi,y\_{i}=f\_{0}(x\_{i})+\epsilon\_{i}, |  |

with i.i.d. errors such that 𝔼​[ϵi]=0\mathbb{E}[\epsilon\_{i}]=0, Var​(ϵi)=σ2<∞\mathrm{Var}(\epsilon\_{i})=\sigma^{2}<\infty, xi∈𝒳⊂ℝdx\_{i}\in\mathcal{X}\subset\mathbb{R}^{d}. The problem is the estimation of the unknown regression function f0f\_{0}, which can be achieved by minimizing the empirical squared error loss

|  |  |  |
| --- | --- | --- |
|  | f^n=argminf∈ℱQn(f)=argminf∈ℱ1n∑i=1n(yi−f(xi))2.(f0∈ℱ)\hat{f}\_{n}=\arg\min\_{f\in\mathcal{F}}Q\_{n}(f)=\arg\min\_{f\in\mathcal{F}}\frac{1}{n}\sum\_{i=1}^{n}\bigl(y\_{i}-f(x\_{i})\bigr)^{2}.\quad(f\_{0}\in\mathcal{F}) |  |

The objective of Sieve estimation is to minimize the squared error loss over a function space ℱn\mathcal{F}\_{n}, which approximates ℱ\mathcal{F} as the error tends to 0 and the sample size increases ([shen1994convergence], [shen2023asymptotic]).
Define the sequence of functions ℱ1⊆ℱ2⊂⋯⊂ℱn⊂⋯⊂ℱ\mathcal{F}\_{1}\subseteq\mathcal{F}\_{2}\subset\cdots\subset\mathcal{F}\_{n}\subset\cdots\subset\mathcal{F}
and assume ⋃n=1∞ℱn\bigcup\_{n=1}^{\infty}\mathcal{F}\_{n} is dense in ℱ\mathcal{F} with respect to a pseudo-metric dd, so that for every f∈ℱf\in\mathcal{F} there exists πn​f∈ℱn\pi\_{n}f\in\mathcal{F}\_{n} such that

|  |  |  |
| --- | --- | --- |
|  | d​(f,πn​f)→0.d(f,\pi\_{n}f)\to 0. |  |

A sieve estimator f^n\hat{f}\_{n} is over ℱn\mathcal{F}\_{n} satisfies

|  |  |  |
| --- | --- | --- |
|  | Qn​(f^n)≤inff∈ℱnQn​(f)+Op​(ηn),ηn→0.Q\_{n}(\hat{f}\_{n})\ \leq\ \inf\_{f\in\mathcal{F}\_{n}}Q\_{n}(f)+O\_{p}(\eta\_{n}),\qquad\eta\_{n}\to 0. |  |

In our setting, we define the sieve estimator as

|  |  |  |
| --- | --- | --- |
|  | ℱn={fθ:θ∈Θn,where for ​x∈ℝd​ℓk(ℓ)​(x)=⟨ak(ℓ),x⟩+bk(ℓ),zθ(1)​(x)=LSET1⁡((ℓk(1)​(x))k=1K1),zθ(ℓ)​(x)=LSETℓ⁡((αk(ℓ)​zθ(ℓ−1)​(x)+ℓk(ℓ)​(x))k=1Kℓ),ℓ≥2,fθ​(x)=zθ(L)​(x)+cout},\mathcal{F}\_{n}=\left\{f\_{\theta}:\theta\in\Theta\_{n},\ \text{where for }x\in\mathbb{R}^{d}\ \begin{aligned} &\ell^{(\ell)}\_{k}(x)=\langle a^{(\ell)}\_{k},x\rangle+b^{(\ell)}\_{k},\\[2.0pt] &z^{(1)}\_{\theta}(x)=\operatorname{LSE}\_{T\_{1}}\!\big((\ell^{(1)}\_{k}(x))\_{k=1}^{K\_{1}}\big),\\[2.0pt] &z^{(\ell)}\_{\theta}(x)=\operatorname{LSE}\_{T\_{\ell}}\!\big((\alpha^{(\ell)}\_{k}\,z^{(\ell-1)}\_{\theta}(x)+\ell^{(\ell)}\_{k}(x))\_{k=1}^{K\_{\ell}}\big),\ \ \ell\geq 2,\\[2.0pt] &f\_{\theta}(x)=z^{(L)}\_{\theta}(x)+c\_{\mathrm{out}}\end{aligned}\,\right\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Θn={θ:maxk⁡‖ak(ℓ)‖∗≤Sℓ(n),maxk⁡|bk(ℓ)|≤Bℓ(n),maxk⁡αk(ℓ)≤qℓ(n)<1,Tℓ≤Θℓ(n),Kℓ≤Kℓ(n),|cout|≤C(n)​for all ​ℓ}.\Theta\_{n}=\Bigl\{\theta:\ \begin{aligned} &\max\_{k}\|a\_{k}^{(\ell)}\|\_{\*}\leq S\_{\ell}^{(n)},\quad\max\_{k}|b\_{k}^{(\ell)}|\leq B\_{\ell}^{(n)},\quad\max\_{k}\alpha\_{k}^{(\ell)}\leq q\_{\ell}^{(n)}<1,\\ &T\_{\ell}\leq\Theta\_{\ell}^{(n)},\quad K\_{\ell}\leq K\_{\ell}^{(n)},\quad|c\_{\mathrm{out}}|\leq C^{(n)}\ \text{for all }\ell\end{aligned}\Bigr\}. |  |

where B,Vn,S→∞B,V\_{n},S\to\infty as n→∞n\to\infty.

#### 3.4.1 Existence-Measurability

We show in Theorem [3.8](https://arxiv.org/html/2512.11731v1#S3.Thmassumption8 "Theorem 3.8 (Finite Sieve Envelope). ‣ 3.4.1 Existence-Measurability ‣ 3.4 Sieve M-Estimation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") that our functional class is bounded. The result of finite measurability is a requirement for the Sieve class. In Appendix [B.4](https://arxiv.org/html/2512.11731v1#A2.SS4 "B.4 Sieve M-estimation and Consistency ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity"), we report the proof.

###### Theorem 3.8 (Finite Sieve Envelope).

Let 𝒳={x:‖x‖≤R}\mathcal{X}=\{x:\|x\|\leq R\} be a bounded input set. For each fixed nn, let the sieve

|  |  |  |
| --- | --- | --- |
|  | Θn={θ:maxk⁡‖ak(ℓ)‖∗≤Sℓ(n),maxk⁡|bk(ℓ)|≤Bℓ(n),maxk⁡αk(ℓ)≤qℓ(n)<1,Tℓ≤Θℓ(n),Kℓ≤Kℓ(n),|cout|≤C(n)​for all ​ℓ}.\Theta\_{n}=\Bigl\{\theta:\ \begin{aligned} &\max\_{k}\|a\_{k}^{(\ell)}\|\_{\*}\leq S\_{\ell}^{(n)},\quad\max\_{k}|b\_{k}^{(\ell)}|\leq B\_{\ell}^{(n)},\quad\max\_{k}\alpha\_{k}^{(\ell)}\leq q\_{\ell}^{(n)}<1,\\ &T\_{\ell}\leq\Theta\_{\ell}^{(n)},\quad K\_{\ell}\leq K\_{\ell}^{(n)},\quad|c\_{\mathrm{out}}|\leq C^{(n)}\ \text{for all }\ell\end{aligned}\Bigr\}. |  |

and let ℱn={fθ:θ∈Θn}\mathcal{F}\_{n}=\{\,f\_{\theta}:\theta\in\Theta\_{n}\,\} be the corresponding class of deep-LSE networks (scalar output).

Define

|  |  |  |
| --- | --- | --- |
|  | Vn=C(n)+∑ℓ=1L(R​Sℓ(n)+Bℓ(n)+Θℓ(n)​log⁡Kℓ(n))​∏r=ℓ+1Lqr(n).V\_{n}=C^{(n)}+\sum\_{\ell=1}^{L}\Bigl(R\,S\_{\ell}^{(n)}+B\_{\ell}^{(n)}+\Theta\_{\ell}^{(n)}\log K\_{\ell}^{(n)}\Bigr)\prod\_{r=\ell+1}^{L}q\_{r}^{(n)}. |  |

For each fixed nn,

|  |  |  |
| --- | --- | --- |
|  | supf∈ℱn‖f‖∞=supθ∈Θnsupx∈𝒳|fθ​(x)|≤Vn.\;\sup\_{f\in\mathcal{F}\_{n}}\|f\|\_{\infty}\;=\;\sup\_{\theta\in\Theta\_{n}}\ \sup\_{x\in\mathcal{X}}|f\_{\theta}(x)|\;\leq\;V\_{n}\;. |  |

The minimization of the empirical squared error over the sieve class ℱr\mathcal{F}\_{r} ensures that, for any fixed realization of the data, the criterion Qn​(f)Q\_{n}(f) is continuous in ff. Then, the existence of the sieve estimator follows once the set of functions ℱn\mathcal{F}\_{n} is compact in 𝒳\mathcal{X}. For fixed nn and fixed sample {xi}i=1n⊂𝒳\{x\_{i}\}\_{i=1}^{n}\subset\mathcal{X}, define the evaluation map

|  |  |  |
| --- | --- | --- |
|  | E:Θn⟶ℝn,E​(θ)=(fθ​(x1),…,fθ​(xn)).E:\Theta\_{n}\longrightarrow\mathbb{R}^{n},\qquad E(\theta)=\bigl(f\_{\theta}(x\_{1}),\,\ldots,\,f\_{\theta}(x\_{n})\bigr). |  |

Each point θ↦fθ​(xi)\theta\mapsto f\_{\theta}(x\_{i}) is continuous because the Deep-LSE is a composition of affine maps, and all network parameters are restricted to a compact set Θn\Theta\_{n} with Tℓ≥T¯ℓ>0T\_{\ell}\geq\underline{T}\_{\ell}>0. So EE is continuous and E​(Θn)E(\Theta\_{n}) is compact in ℝn\mathbb{R}^{n}.

Now, ‖f−g‖n\|f-g\|\_{n} coincides with the Euclidean norm of E​(θf)−E​(θg)E(\theta\_{f})-E(\theta\_{g}), up to 1/n1/\sqrt{n}. Therefore, the metric space (ℱn,∥⋅∥n)(\mathcal{F}\_{n},\|\cdot\|\_{n}) is isometric with respect to the compact set E​(Θn)⊂ℝnE(\Theta\_{n})\subset\mathbb{R}^{n}, and hence, ℱn\mathcal{F}\_{n} is compact under ∥⋅∥n\|\cdot\|\_{n}.

#### 3.4.2 Consistency

We obtain, in Theorem [3.9](https://arxiv.org/html/2512.11731v1#S3.Thmassumption9 "Theorem 3.9 (The LSE map is 1-Lipschitz). ‣ 3.4.2 Consistency ‣ 3.4 Sieve M-Estimation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity"), a basic Lipschitz estimate for the log-sum-exp activation which is a key result for the consistency of the estimator. It shows that the map LSET:ℝm→ℝ\mathrm{LSE}\_{T}:\mathbb{R}^{m}\to\mathbb{R} with u↦T​log⁡(∑i=1meui/T)u\mapsto T\log\!\Bigl(\sum\_{i=1}^{m}e^{u\_{i}/T}\Bigr) is 1 -Lipschitz with respect to standard norms, meaning that small changes in the input vector lead to proportionally small changes in the LSE output.

###### Theorem 3.9 (The LSE map is 11-Lipschitz).

For m∈ℕm\in\mathbb{N} and T>0T>0, define the LSE map

|  |  |  |
| --- | --- | --- |
|  | LSET:ℝm→ℝ,LSET​(u)=T​log⁡(∑i=1meui/T).\mathrm{LSE}\_{T}:\mathbb{R}^{m}\to\mathbb{R},\qquad\mathrm{LSE}\_{T}(u)=T\log\!\left(\sum\_{i=1}^{m}e^{u\_{i}/T}\right). |  |

Then LSET\mathrm{LSE}\_{T} is 11-Lipschitz with respect to ∥⋅∥∞\|\cdot\|\_{\infty}
(and also 11-Lipschitz with respect to ∥⋅∥2\|\cdot\|\_{2}):

|  |  |  |
| --- | --- | --- |
|  | |LSET(u)−LSET(v)|≤∥u−v∥∞and≤∥u−v∥2(∀u,v∈ℝm).\bigl|\mathrm{LSE}\_{T}(u)-\mathrm{LSE}\_{T}(v)\bigr|\leq\|u-v\|\_{\infty}\quad\text{and}\quad\leq\|u-v\|\_{2}\qquad(\forall\,u,v\in\mathbb{R}^{m}). |  |

In the Deep-LSE model, z(ℓ−1)​(x)∈ℝz^{(\ell-1)}(x)\in\mathbb{R} is a scalar. So

|  |  |  |
| --- | --- | --- |
|  | S(ℓ)​(x)=α(ℓ)​z(ℓ−1)​(x)+A(ℓ)​x+b(ℓ)∈ℝKℓS^{(\ell)}(x)=\alpha^{(\ell)}\,z^{(\ell-1)}(x)+A^{(\ell)}x+b^{(\ell)}\in\mathbb{R}^{K\_{\ell}} |  |

means, componentwise,

|  |  |  |
| --- | --- | --- |
|  | Sk(ℓ)​(x)=αk(ℓ)⏟scalar for unit ​k​z(ℓ−1)​(x)+ak(ℓ)⊤⏟∈ℝd​x+bk(ℓ)⏟scalar,k=1,…,Kℓ.S^{(\ell)}\_{k}(x)=\underbrace{\alpha^{(\ell)}\_{k}}\_{\text{scalar for unit }k}\,z^{(\ell-1)}(x)+\ \underbrace{a^{(\ell)\top}\_{k}}\_{\in\mathbb{R}^{d}}\,x+\ \underbrace{b^{(\ell)}\_{k}}\_{\text{scalar}},\qquad k=1,\ldots,K\_{\ell}. |  |

Although α(ℓ)\alpha^{(\ell)} is a vector across units, each unit uses one scalar αk(ℓ)\alpha^{(\ell)}\_{k}. The feature vector feeding each unit is (z(ℓ−1)​(x),x)∈ℝ1+d(\,z^{(\ell-1)}(x),\,x\,)\in\mathbb{R}^{1+d} ⇒\Rightarrow dimension d+1d+1. While parameters per unit are (αk(ℓ),ak(ℓ),bk(ℓ))(\alpha^{(\ell)}\_{k},\,a^{(\ell)}\_{k},\,b^{(\ell)}\_{k}) ⇒\Rightarrow d+2d+2 numbers (weights for d+1d+1 features plus the bias). In layer 1 there is no skip term ⇒K1​(d+1)\Rightarrow\ K\_{1}(d+1) parameters and in layers ℓ≥2\ell\geq 2 we have Kℓ​(d+2)K\_{\ell}(d+2) parameters each plus the final shift coutc\_{\mathrm{out}}. We obtain

|  |  |  |
| --- | --- | --- |
|  | mn=K1​(d+1)+∑ℓ=2LKℓ​(d+2)+1≍∑ℓ=1LKℓ​(d+2)+1.m\_{n}=K\_{1}(d+1)+\sum\_{\ell=2}^{L}K\_{\ell}(d+2)+1\ \asymp\ \sum\_{\ell=1}^{L}K\_{\ell}(d+2)+1. |  |

Theorem 14.5 in [anthony2009neural] states that for the class ℱ\mathcal{F} of functions computed by the network described above, if ϵ≤2​b\epsilon\leq 2b, then

|  |  |  |
| --- | --- | --- |
|  | 𝒩∞​(ϵ,ℱ,m)≤(4​e​m​b​W​(L​V)ℓϵ​(L​V−1))W.\mathcal{N}\_{\infty}(\epsilon,\mathcal{F},m)\;\leq\;\left(\frac{4\,e\,m\,b\,W\,(LV)^{\ell}}{\epsilon\,(LV-1)}\right)^{W}. |  |

To apply this result, we correct the mnm\_{n} term with a reparametrization trick of the Deep-LSE network. We create dd relay units r(1),…,r(L−1)r^{(1)},\ldots,r^{(L-1)} that copy the input coordinate-wise:

|  |  |  |
| --- | --- | --- |
|  | r(0)​(x)=x,r(ℓ)​(x)=r(ℓ−1)​(x)(ℓ=1,…,L−1),r^{(0)}(x)=x,\qquad r^{(\ell)}(x)=r^{(\ell-1)}(x)\quad(\ell=1,\ldots,L-1), |  |

each with the identity activation s​(t)=ts(t)=t and a single incoming edge of weight 11. Rewriting every layer ℓ≥2\ell\geq 2 to take inputs only from the previous layer

|  |  |  |
| --- | --- | --- |
|  | Sk(ℓ)​(x)=αk(ℓ)​z(ℓ−1)​(x)+(ak(ℓ))⊤​r(ℓ−1)​(x)+bk(ℓ).S\_{k}^{(\ell)}(x)=\alpha\_{k}^{(\ell)}\,z^{(\ell-1)}(x)+\bigl(a\_{k}^{(\ell)}\bigr)^{\!\top}r^{(\ell-1)}(x)+b\_{k}^{(\ell)}. |  |

This network computes the same functions as the original model, but all edges are between adjacent layers.
Then, the covering number becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | W\displaystyle W | =mn+d​(L−1)\displaystyle=m\_{n}+d(L-1) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑ℓ=1LKℓ​(d+2)+1+d​(L−1).\displaystyle=\sum\_{\ell=1}^{L}K\_{\ell}(d+2)+1+d(L-1). |  |

We combine together the approximation and stability properties of Deep-LSE networks in an asymptotic framework. Let ℱn\mathcal{F}\_{n} denote the Deep-LSE sieve class, and let Qn​(f)Q\_{n}(f) and Q¯n​(f)\overline{Q}\_{n}(f) be the empirical and population criteria, respectively, associated with a function from the sieve class f∈ℱnf\in\mathcal{F}\_{n}. The first result establishes that under a suitable growth condition (W​Vn2​log⁡(VnL​W)=o​(n)WV\_{n}^{2}\,\log\!\big(V\_{n}^{L}W\big)=o(n)) the empirical criterion Qn​(f)Q\_{n}(f) converges uniformly in probability to its population counterpart Q¯n​(f)\overline{Q}\_{n}(f) over f∈ℱnf\in\mathcal{F}\_{n}. We use this uniform approximation to prove the consistency of the Deep-LSE sieve estimator f^n∈ℱn\hat{f}\_{n}\in\mathcal{F}\_{n}. Specifically, if the network complexity, measured in terms of the widths and the number of affine pieces VnV\_{n}, grows slowly enough, then the empirical L2L^{2}-distance

|  |  |  |
| --- | --- | --- |
|  | ‖f^n−f0‖n=(1n​∑i=1n(f^n​(Xi)−f0​(Xi))2)1/2\|\hat{f}\_{n}-f\_{0}\|\_{n}=\Bigl(\tfrac{1}{n}\sum\_{i=1}^{n}\bigl(\hat{f}\_{n}(X\_{i})-f\_{0}(X\_{i})\bigr)^{2}\Bigr)^{1/2} |  |

converges to 0 in probability. In this sense, the Deep-LSE sieve estimator is asymptotically consistent.

###### Theorem 3.10 (Asymptotic behavior of Deep-LSE sieve class parameters).

Under the assumption

|  |  |  |
| --- | --- | --- |
|  | W​Vn2​log⁡(VnL​W)=o​(n)a​s​n→∞,WV\_{n}^{2}\,\log\!\big(V\_{n}^{L}W\big)=o(n)\quad as\ n\to\infty, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | supf∈ℱn|Qn​(f)−Q¯n​(f)|→p∗ 0a​s​n→∞.\sup\_{f\in\mathcal{F}\_{n}}\bigl|\,Q\_{n}(f)-\overline{Q}\_{n}(f)\,\bigr|\;\xrightarrow{\,p^{\*}\,}\;0\qquad as\ n\to\infty. |  |

Since QQ is continuous at f0∈ℱf\_{0}\in\mathcal{F} and Q​(f0)=σ2<∞Q(f\_{0})=\sigma^{2}<\infty, the function f0f\_{0} is a minimizer of the population risk ([shen2023asymptotic]). For any ε>0\varepsilon>0 we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | inff:‖f−f0‖n≥ε(Qn​(f)−Qn​(f0))\displaystyle\inf\_{\;f:\ \|f-f\_{0}\|\_{n}\geq\varepsilon}\Bigl(Q\_{n}(f)-Q\_{n}(f\_{0})\Bigr) | =inff:‖f−f0‖n≥ε1n​∑i=1n(f​(xi)−f0​(xi))2\displaystyle=\inf\_{\;f:\ \|f-f\_{0}\|\_{n}\geq\varepsilon}\frac{1}{n}\sum\_{i=1}^{n}\!\bigl(f(x\_{i})-f\_{0}(x\_{i})\bigr)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inff:‖f−f0‖n≥ε‖f−f0‖n2\displaystyle=\inf\_{\;f:\ \|f-f\_{0}\|\_{n}\geq\varepsilon}\|f-f\_{0}\|\_{n}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥ε2> 0.\displaystyle\geq\varepsilon^{2}\;>\;0. |  |

In other words, f0f\_{0} is a minimizer of the empirical risk QnQ\_{n} with respect to the norm ∥⋅∥n\|\cdot\|\_{n}. Hence, by Theorem [3.10](https://arxiv.org/html/2512.11731v1#S3.Thmassumption10 "Theorem 3.10 (Asymptotic behavior of Deep-LSE sieve class parameters). ‣ 3.4.2 Consistency ‣ 3.4 Sieve M-Estimation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") applied to QnQ\_{n} and QQ, we have that

|  |  |  |
| --- | --- | --- |
|  | ‖f^n−f0‖n→𝑝0.\|\hat{f}\_{n}-f\_{0}\|\_{n}\xrightarrow{p}0. |  |

The result of Theorem [3.10](https://arxiv.org/html/2512.11731v1#S3.Thmassumption10 "Theorem 3.10 (Asymptotic behavior of Deep-LSE sieve class parameters). ‣ 3.4.2 Consistency ‣ 3.4 Sieve M-Estimation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") allows us to identify optimal structural conditions for the Dee-LSE model. For example, let Rn=∑ℓ=1LKℓR\_{n}=\sum\_{\ell=1}^{L}K\_{\ell} be the total number of affine terms. For a fixed L,W≍c​(d)​RnL,W\asymp c(d)R\_{n}, the consistency condition becomes, up to constants,

|  |  |  |
| --- | --- | --- |
|  | Rn​Vn2​(log⁡Rn+L​log⁡Vn)=o​(n).R\_{n}V\_{n}^{2}\left(\log R\_{n}+L\log V\_{n}\right)=o(n). |  |

A possible scenario in which the condition is satisfied is Vn=O​(1)V\_{n}=O(1) and fixed depth. The condition gives Rn​log⁡Rn=o​(n)R\_{n}\log R\_{n}=o(n). So it grows almost linearly in nn and Rn=n(log⁡n)1+δR\_{n}=\frac{n}{(\log n)^{1+\delta}} is a possible solution. Another scenario consists in Vn=O​(1)V\_{n}=O(1) and the depth grows. Now Rn​(log⁡Rn+Ln)=o​(n)R\_{n}\left(\log R\_{n}+L\_{n}\right)=o(n), and a possible solutions is

|  |  |  |
| --- | --- | --- |
|  | Rn=n(log⁡n)1+δ,Ln=o​(log⁡n).R\_{n}=\frac{n}{(\log n)^{1+\delta}},\quad L\_{n}=o(\log n). |  |

#### 3.4.3 Optimal Stopping Criteria for Transfer Learning

Another key design choice concerns when to stop the transfer-learning fine-tuning step, which forms the second phase of the inference procedure. Our approach is simple, the second phase of the estimation procedure stops when the benefit of continuing it is outweighed by the costs. In practice, we quantify the cost by evaluating the divergence between the weights of the Deep-LSE during the first and second estimation steps. The rationale is that when divergence grows, the model is estimating a function that is far from the original (source) function, and hence, we identify the stopping criterion.

Let PP be a parameter prior centered at the pretrained weights w0w\_{0}. For concreteness, and to obtain explicit gradients, we take a Gaussian

|  |  |  |
| --- | --- | --- |
|  | P=𝒩​(w0,ΣP),Qt=𝒩​(μt,ΣQ),P=\mathcal{N}\!\big(w\_{0},\;\Sigma\_{P}\big),\qquad Q\_{t}=\mathcal{N}\!\big(\mu\_{t},\;\Sigma\_{Q}\big), |  |

where μt\mu\_{t} is the current iterate wtw\_{t} (the mean of QtQ\_{t}), and ΣQ\Sigma\_{Q} is the posterior covariance (isotropic τ2​I\tau^{2}I). The Bayes bounds control the true target risk R​(Qt)=𝔼w∼Qt​[R​(w)]R(Q\_{t})=\mathbb{E}\_{w\sim Q\_{t}}[R(w)] via the empirical target risk R^​(Qt)=𝔼w∼Qt​[R^​(w)]\widehat{R}(Q\_{t})=\mathbb{E}\_{w\sim Q\_{t}}[\widehat{R}(w)] as

|  |  |  |
| --- | --- | --- |
|  | R​(Qt)≤R^​(Qt)+KL​(Qt∥P)+ln⁡2​nδ2​(n−1)with probability at least ​1−δ.R(Q\_{t})\;\leq\;\widehat{R}(Q\_{t})\;+\;\sqrt{\frac{\mathrm{KL}(Q\_{t}\|P)\;+\;\ln\!\frac{2\sqrt{n}}{\delta}}{2(n-1)}}\qquad\text{with probability at least }1-\delta. |  |

For Q=𝒩​(μQ,ΣQ)Q=\mathcal{N}(\mu\_{Q},\Sigma\_{Q}), P=𝒩​(μP,ΣP)P=\mathcal{N}(\mu\_{P},\Sigma\_{P}) in ℝp\mathbb{R}^{p},

|  |  |  |
| --- | --- | --- |
|  | KL​(Q∥P)=12​(tr​(ΣP−1​ΣQ)+(μP−μQ)⊤​ΣP−1​(μP−μQ)−p+ln⁡detΣPdetΣQ).\mathrm{KL}(Q\|P)=\frac{1}{2}\Big(\mathrm{tr}(\Sigma\_{P}^{-1}\Sigma\_{Q})+(\mu\_{P}-\mu\_{Q})^{\top}\Sigma\_{P}^{-1}(\mu\_{P}-\mu\_{Q})-p+\ln\frac{\det\Sigma\_{P}}{\det\Sigma\_{Q}}\Big). |  |

while in the isotropic case ΣP=σ2​I\Sigma\_{P}=\sigma^{2}I, ΣQ=τ2​I\Sigma\_{Q}=\tau^{2}I,

|  |  |  |
| --- | --- | --- |
|  | KL​(Q∥P)=12​(τ2σ2​p+‖μQ−μP‖22σ2−p+p​ln⁡σ2τ2).\mathrm{KL}(Q\|P)=\frac{1}{2}\Big(\frac{\tau^{2}}{\sigma^{2}}\,p+\frac{\|\,\mu\_{Q}-\mu\_{P}\,\|\_{2}^{2}}{\sigma^{2}}-p+p\ln\frac{\sigma^{2}}{\tau^{2}}\Big). |  |

Define the objective

|  |  |  |
| --- | --- | --- |
|  | ℬ​(t)=R^​(Qt)⏟empirical fit+c​KL​(Qt∥P)\mathcal{B}(t)\;=\;\underbrace{\widehat{R}(Q\_{t})}\_{\text{empirical fit}}\;+\;c\;\sqrt{\mathrm{KL}(Q\_{t}\|P)}\! |  |

with c>0c>0 a constant. We use the early-stopping time t⋆t^{\star} at any stationary point when

|  |  |  |
| --- | --- | --- |
|  | dd​t​ℬ​(t)|t=t⋆=0⟺|dd​t​R^​(Qt)|=c​dd​t​KL​(Qt∥P)at ​t=t⋆.\frac{d}{dt}\,\mathcal{B}(t)\Big|\_{t=t^{\star}}=0\quad\Longleftrightarrow\quad\Big|\tfrac{d}{dt}\widehat{R}(Q\_{t})\Big|\;=\;c\;\tfrac{d}{dt}\sqrt{\mathrm{KL}(Q\_{t}\|P)}\ \ \text{at }t=t^{\star}. |  |

Intuitively, we stop when the marginal reduction in empirical loss equals the marginal increase in complexity, measured by the KL to the pretrained prior.

## 4 Simulation Studies

We perform a simulation study using the [bates1996jumps] stochastic volatility model. We simulate a cross-section of option prices and market conditions (liquid and illiquid), and compare the estimated RND with the ground truth implied by the data-generating process. For completeness, we also test the simulation study on the [kou2002jump], [andersen2002empirical], and Three-Factor Double Exponential Stochastic volatility ([andersen2015risk]) models in Appendix [C](https://arxiv.org/html/2512.11731v1#A3 "Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity"). The Bates stochastic volatility jump–diffusion model is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​St\displaystyle dS\_{t} | =St​[(r−λ​k)​d​t+vt​d​Wt(1)+(Jt−1)​d​Nt],\displaystyle=S\_{t}\Bigl[(r-\lambda k)\,dt+\sqrt{v\_{t}}\,dW\_{t}^{(1)}+(J\_{t}-1)\,dN\_{t}\Bigr], |  | (4.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​vt\displaystyle dv\_{t} | =κ​(θ−vt)​d​t+η​vt​d​Wt(2),\displaystyle=\kappa(\theta-v\_{t})\,dt+\eta\sqrt{v\_{t}}\,dW\_{t}^{(2)}, |  | (4.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨d​Wt(1),d​Wt(2)⟩\displaystyle\langle dW\_{t}^{(1)},dW\_{t}^{(2)}\rangle | =ρ​d​t,ℙ​(d​Nt=1)=λ​d​t.\displaystyle=\rho\,dt,\qquad\mathbb{P}(dN\_{t}=1)=\lambda\,dt. |  | (4.3) |

with k=𝔼​[Jt−1]=eμj+12​σj2−1k=\mathbb{E}[J\_{t}-1]=e^{\mu\_{j}+\frac{1}{2}\sigma\_{j}^{2}}-1 and Yt∼𝒩​(μj,σj2)Y\_{t}\sim\mathcal{N}(\mu\_{j},\sigma\_{j}^{2}). Here, St>0S\_{t}>0 denotes the stock price, vt>0v\_{t}>0 is the instantaneous variance, r∈ℝr\in\mathbb{R} is the risk-free rate, σ>0\sigma>0 is the (constant) diffusion volatility, μj∈ℝ\mu\_{j}\in\mathbb{R} and σj>0\sigma\_{j}>0 are the mean and standard deviation of the normal jump sizes YtY\_{t}, and kk is the mean relative jump size. The processes (Wt(1))t≥0(W\_{t}^{(1)})\_{t\geq 0} and (Wt(2))t≥0(W\_{t}^{(2)})\_{t\geq 0} form a two-dimensional Brownian motion with correlation ρ∈[−1,1]\rho\in[-1,1], (Nt)t≥0(N\_{t})\_{t\geq 0} is a Poisson process with jump intensity λ>0\lambda>0 independent of (Wt(1),Wt(2))(W\_{t}^{(1)},W\_{t}^{(2)}), and (Jt)t≥0(J\_{t})\_{t\geq 0} are i.i.d. lognormal jump multipliers given by Jt=eYtJ\_{t}=e^{Y\_{t}}. The parameters κ>0\kappa>0, θ>0\theta>0, and η>0\eta>0 are respectively the speed of mean reversion, the long-run mean, and the volatility of the variance process (vt)t≥0(v\_{t})\_{t\geq 0}. In Table [1](https://arxiv.org/html/2512.11731v1#S4.T1 "Table 1 ‣ 4 Simulation Studies ‣ Transfer Learning (Il)liquidity") we report the parameters we use for the simulation.

| S0S\_{0} | rr | v0v\_{0} | κ\kappa | θ\theta | η\eta | ρ\rho | λ\lambda | μj\mu\_{j} | σj\sigma\_{j} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 0.06 | 0.09 | 3.0 | 0.07 | 0.3 | -0.34 | 0.5 | -0.09 | 0.45 |

Table 1: Simulated parameters for Bates model

In Fig. [1](https://arxiv.org/html/2512.11731v1#S4.F1 "Figure 1 ‣ 4 Simulation Studies ‣ Transfer Learning (Il)liquidity"), the blue line is the implied volatility curve that we retrieve with the synthetic option prices, while the orange line is the proxy implied volatility (IV) curve. To obtain the target implied volatility curve, we assume it is a translation of the source implied volatility curve. Specifically, we apply a −10%-10\% decrease on the implied volatilities (y-axis) and a +20​$+20\mathdollar increase on the strikes (x-axis). In Appendix [C](https://arxiv.org/html/2512.11731v1#A3 "Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity"), we test the framework generating the proxy and illiquid stocks from two different data-generating processes, thereby obtaining two distinct implied volatilities directly, rather than translating the curve. We use the entire proxy to train the model, then, leveraging transfer learning, we fine-tune the pretrained model on the illiquid market observations. The illiquid strikes are simulated by random sampling in the interval of option prices that are 10%-25% out of the money (green illiquid strikes) and by random sampling in the interval of option prices that are 10%-25% in-the-money (orange illiquid strikes).
They are represented by orange and green dots, with the associated implied volatility and option prices.
The first experiment we perform involves emulating the condition of a severely illiquid market. In fact, we select only the three in-the-money strikes to represent the illiquid market (Strikes K=82,97,98K=82,97,98), and maturity one year.

![Refer to caption](setup.png)


Figure 1: Setup of implied volatility curves using Bates model. In blue, the illiquid target implied volatility. In orange, the liquid proxy we use to train the model.

For the estimation of the IV curve of the liquid proxy and illiquid target, we use the Deep-LSE model with 2 layers and 3 affine terms each. In Fig. [2](https://arxiv.org/html/2512.11731v1#S4.F2 "Figure 2 ‣ 4 Simulation Studies ‣ Transfer Learning (Il)liquidity"), we compare the estimate of the RND of our model versus the interpolation of quadratic splines. The blue curve is the ground-truth RND, while the orange and green represent the estimate of the RND of our model and quadratic splines, respectively. It is possible to observe how quadratic splines are not able to recover correctly the ground-truth illiquid RND, especially on the right tail. In contrast, our Deep-LSE, after performing transfer learning, produces a good fit of the RND.

![Refer to caption](rndfinalfit.png)


Figure 2: Illiquid RND recovery of Deep-LSE (orange curve) and quadratic splines (green curve) in comparison with the target ground truth simulated RND (blue curve).

In Fig. [3](https://arxiv.org/html/2512.11731v1#S4.F3.fig7 "Figure 3 ‣ 4 Simulation Studies ‣ Transfer Learning (Il)liquidity"), we observe the capacity of our Deep-LSE model to approximate convex functions. In this case, the convex function represents the implied volatility curve of the liquid, proxy, asset. During the learning process, the model starts learning the shape and curvature of the proxy implied volatility, and between iteration 6−86-8 it starts fitting a convex function. At the end of the learning process on the source data (liquid proxy), the model perfectly fits its implied volatility curve.

![Refer to caption](train1.png)

![Refer to caption](train2.png)

![Refer to caption](train3.png)

![Refer to caption](train4.png)

![Refer to caption](train5.png)

![Refer to caption](train6.png)

Figure 3: First step recovery - Source Deep-LSE Fit. The blue dots represent the implied volatility curve of option quotes of the liquid proxy asset while the blue solid line represents the fit of the interpolating function of the Deep-LSE model.

The second step of the estimation process of the illiquid RND involves performing transfer learning to fit the model on the (illiquid) target option data. To achieve this, we fine-tune with illiquid option data the model pre-trained on the liquid proxy.

We observe this process in Fig. [4](https://arxiv.org/html/2512.11731v1#S4.F4.fig7 "Figure 4 ‣ 4 Simulation Studies ‣ Transfer Learning (Il)liquidity"). The starting point is the orange curve represents the implied volatility curve that the model has learned from the simulated proxy implied volatility (red curve), and they coincide. As the fine-tuning continues, the green curve moves from the starting point, indicating that the model is learning the new function of the volatility curve of the illiquid target strikes (orange points). We observe that the model adapts to the illiquid strikes by adjusting the level, then its shape and convexity. At the end of the fine-tuning process, the model has learned with good approximation (green curve) the target implied volatility of the illiquid market (blue curve).

Overall, we observe in Fig. [4](https://arxiv.org/html/2512.11731v1#S4.F4.fig7 "Figure 4 ‣ 4 Simulation Studies ‣ Transfer Learning (Il)liquidity") that the Deep-LSE model is able to recover the IV surface and RND in conditions of extreme illiquidity, with as few as three option quotes. In addition, we gather recovery in areas where option quotes are missing.

![Refer to caption](train21.png)

![Refer to caption](train22.png)

![Refer to caption](train23.png)

![Refer to caption](train24.png)

![Refer to caption](train25.png)

![Refer to caption](train26.png)

Figure 4: Second step recovery - Target Deep-LSE Fit. The model only sees the illiquid (orange) quotes. The blue solid line is the true implied volatility function that the Deep-LSE recovers (green solid line). The solid orange and red curves represent the true and estimated IV curve of the first step.

## 5 Empirical Analysis

We test our framework empirically on the SPX option data which consists of January 2015 SPX option data for the source (proxy) and January 2016 SPX option data for the target.

We emulate the conditions of an illiquid market by censoring the data and using just three random quotes of call options. In particular, this allows us to recover the ground truth from the entire panel of option data, and then compare it with the estimate of the RND from our model, which we train using only three call option quotes with 1 month maturity.

We investigate two forms of severe market illiquidity by randomly selecting three in-the-money call option quotes in the first scenario and three out-of-the-money call option quotes in the second scenario described in Table [2](https://arxiv.org/html/2512.11731v1#S5.T2 "Table 2 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity"). We emphasize that these three option quotes constitute the only information on the terminal RND available to the models.

Table 2: Strikes and prices randomly sampled from in-the-money (ITM) and out-of-the-money (OTM) option quotes to emulate the conditions of an illiquid market.

|  |  |  |
| --- | --- | --- |
|  | Strike | Price |
|  | 1950 | 82.95 |
| Scenario 1 (ITM) | 1995 | 51.15 |
|  | 2180 | 0.45 |
|  | 2145 | 1.32 |
| Scenario 2 (OTM) | 2200 | 0.30 |
|  | 2230 | 0.125 |

Market data is noisy, and we illustrate in Fig. [5](https://arxiv.org/html/2512.11731v1#S5.F5 "Figure 5 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity") the smoothing approach required to recover the ground truth RND. After smoothing option prices, we differentiate twice the Black-Scholes function with respect to the strike to obtain the ground truth RND, which we recover from a dense set of option quotes.

![Refer to caption](setup2.png)


Figure 5: Smoothing approach to recover the ground truth RND. On the left panel, the liquid IV curve. On the right, the liquid pricing function for each strike.

In Fig. [6](https://arxiv.org/html/2512.11731v1#S5.F6 "Figure 6 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity") we illustrate the implied volatility curve of the proxy (blue curve) against the target implied volatility curve of the illiquid market (orange curve), where the green crosses represent the three illiquid strikes identified in Scenario 1. This setup with real option market data is particularly challenging because the proxy source data is heavily convex, while the target data comes from an implied volatility curve that is not convex.

![Refer to caption](_strikes_EA_case1.png)


Figure 6: Scenario 1 - Setup of implied volatility curves of the empirical analysis on SPX data. In orange, the illiquid target implied volatility. In blue, the liquid proxy we use to train the model. The green crosses are the illiquid strikes.

Similarly to the simulation studies, we use the Deep-LSE model with 2 layers and 3 affine terms each, as we find it strikes the right balance between flexibility and performance. In Fig. [7](https://arxiv.org/html/2512.11731v1#S5.F7 "Figure 7 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity") we illustrate the estimates of the illiquid RND, comparing the Deep-LSE model versus quadratic splines. It is possible to observe that the Deep-LSE model produces a tight recovery of the illiquid RND, particularly in the strike range of 2000−21002000-2100. By contrast, the recovery obtained from quadratic splines substantially deviates from the ground truth illiquid RND, particularly in right tail of the distribution. In Appendix [D](https://arxiv.org/html/2512.11731v1#A4 "Appendix D Additional Empirical Analysis ‣ Transfer Learning (Il)liquidity"), we report the details of the training process of Scenario 1, illustrating the estimation of the liquid proxy and the transfer to the illiquid target.

![Refer to caption](_final_EA_case1.png)


Figure 7: Scenario 1 - Illiquid RND recovery of Deep-LSE (blue solid curve) and quadratic splines (green solid line) in comparison with the illiquid ground truth RND (orange dotted line).

After the Deep-LSE model recovers the target implied volatility function of the target illiquid market, we compute the theoretical price of the option quotes on different strikes. Empirically, the model respects no-arbitrage constraints, as the pricing function of call options is monotone and convex.

We illustrate the validity of our framework under different illiquid market conditions by performing the same empirical analysis on a different set of illiquid strikes (Scenario 2) (Fig. [8](https://arxiv.org/html/2512.11731v1#S5.F8.fig3 "Figure 8 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity")). In the first experiment on 2015-2016 SPX data we randomly sample from the left tail consisting of in-the-money option quotes. From the same data, now we randomly sample on the right tail to test out-of-money strikes. The left panel of Fig. [8](https://arxiv.org/html/2512.11731v1#S5.F8.fig3 "Figure 8 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity") illustrates the three strikes sampled that represent illiquid market observations.

![Refer to caption](_case4_setup.png)

![Refer to caption](_case4_final.png)

Figure 8: Scenario 2 - Setup of implied volatility curves of the empirical analysis on SPX data. On the left panel, strikes selected (green crosses) on the illiquid target (orange) implied volatility curve. On the right panel, illiquid RND recovery of Deep-LSE model (blue solid line) and quadratic splines (green solid line) in comparison with the illiquid ground truth RND (orange dotted line).

In this Scenario, the Deep-LSE model shows an even better recovery with respect to Scenario 1. The right panel of Fig. [8](https://arxiv.org/html/2512.11731v1#S5.F8.fig3 "Figure 8 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity") plots the recovery of the illiquid RND for the Deep-LSE model (blue distribution) and quadratic splines (green distribution), comparing them to the ground truth RND (orange dotted distribution).

In Fig. [9](https://arxiv.org/html/2512.11731v1#S5.F9 "Figure 9 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity"), we highlight an additional benefit of our model, which guarantees convexity. With noisy and illiquid market quotes, traditional methods might produce concave fits for the implied volatility curve. By contrast, our framework adjusts robustly to illiquid conditions and still recovers a well–behaved RND. This is driven by the pretraining phase, during which they internalize the typical shape of the implied volatility surface and, by extension, of the corresponding risk–neutral density.

![Refer to caption](_case4_train.png)


Figure 9: Scenario 2 - Market noise and illiquidity might lead to a concave fit of quadratic splines in recovering the implied volatility curve of the illiquid market. The blue solid line is the IV curve of Deep-LSE, the orange solid line is the IV curve of quadratic splines, and blue dots constitute the target IV curve. The red dots are the illiquid strikes.

Furthermore, we recover option prices from the estimated RND and contrast them with market quotes, from which we infer the associated pricing errors. Let (St)t≥0(S\_{t})\_{t\geq 0} be the underlying price process under the risk–neutral measure ℚ\mathbb{Q}, and assume a constant continuously compounded interest rate rr. Let f^ℚ​(s;T)\hat{f}\_{\mathbb{Q}}(s;T) denote the estimated risk–neutral density of STS\_{T} on (0,∞)(0,\infty). The estimated price of a European call, in t=0t=0, with maturity TT and strike KK is

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^​(0;K,T)=e−r​T​𝔼ℚ​[(ST−K)+]=e−r​T​∫K∞(s−K)​f^ℚ​(s;T)​ds\hat{C}(0;K,T)=e^{-rT}\,\mathbb{E}^{\mathbb{Q}}\!\left[(S\_{T}-K)^{+}\right]=e^{-rT}\int\_{K}^{\infty}(s-K)\,\hat{f}\_{\mathbb{Q}}(s;T)\,\mathrm{d}s |  | (5.1) |

and we define the pricing error as C​(0;K,T)−C^​(0;K,T)C(0;K,T)-\hat{C}(0;K,T), where C​(0;K,T)C(0;K,T) is the price observed on the market. In Table [3](https://arxiv.org/html/2512.11731v1#S5.T3 "Table 3 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity"), we report the pricing error of popular methods to estimate the RND. Specifically, the Kernel-based nonparametric RND estimator replicates the local polynomial approach of [ait2003nonparametric], the Lognormal-Weibull Mixture implements the approach [li2024parametric], and Maximum-Entropy consists in the Positive Convolution method of [bondarenko2003estimation]. We infer the RND in all cases by using the same sets of illiquid quotes illustrated in Table [2](https://arxiv.org/html/2512.11731v1#S5.T2 "Table 2 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity"). The evaluation grid consists of equispaced strikes in the range 1900−21501900-2150, while the Mean Absolute Error (MAE) computes the average absolute error across all strikes.

In Table [3](https://arxiv.org/html/2512.11731v1#S5.T3 "Table 3 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity"), we observe the absolute pricing errors of Scenario 1, which corresponds to the scenario in which only three in-the-money option quotes are available on the market. In this extreme illiquid condition, the benchmarks are not able to fit the RND and extrapolate a meaningful pricing function. Among all benchmarks, our Deep-LSE is the model reports the lowest MAE and the best fit across the strike grid. Parametric models such as the Lognormal-Weibull Mixture, Normal and Lognormal approaches perform better than nonparametric methods such as the kernel-based and Maximum-Entropy approach. Similarly, we observe the absolute pricing errors of Scenario 2, which corresponds to the scenario in which only three out-of-the-money option quotes are available on the market. The Deep-LSE model presents the lowest MAE and absolute pricing error in the sample grid. Also in this case, the parametric model outperforms nonparametric approaches.

Table 3: Absolute Pricing Error - Scenario 1 and Scenario 2.

| Scenario 1: In-the-money illiquid option quotes | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1900 | 1950 | 2000 | 2050 | 2100 | 2150 | MAE |
| Kernel-based nonparametric | 14.56 | 13.56 | 10.82 | 7.74 | 5.19 | 1.35 | 8.87 |
| Deep-LSE | 0.20 | 0.69 | 0.26 | 0.28 | 0.45 | 0.27 | 0.53 |
| Lognormal-Weibull Mixture | 0.50 | 0.79 | 0.61 | 1.10 | 1.09 | 0.45 | 0.76 |
| Maximum-Entropy | 5.60 | 0.51 | 0.17 | 3.08 | 3.30 | 0.84 | 2.61 |
| Parametric Lognormal | 1.07 | 2.95 | 2.39 | 0.29 | 2.04 | 1.43 | 1.70 |
| Parametric Normal | 1.37 | 2.83 | 2.12 | 0.41 | 1.95 | 1.30 | 1.67 |
| Quadratic Splines | 0.19 | 0.57 | 1.30 | 1.96 | 1.64 | 0.56 | 1.03 |
| Scenario 2: Out-of-the-money illiquid option quotes | | | | | | | |
|  | 1900 | 1950 | 2000 | 2050 | 2100 | 2150 | MAE |
| Kernel-based nonparametric | 18.21 | 13.43 | 2.16 | 11.73 | 12.91 | 7.77 | 11.04 |
| Deep-LSE | 3.57 | 3.30 | 2.83 | 2.10 | 1.14 | 0.45 | 2.23 |
| Lognormal-Weibull Mixture | 9.64 | 16.07 | 19.18 | 11.97 | 3.36 | 0.32 | 10.94 |
| Maximum-Entropy | 112.11 | 102.08 | 87.45 | 63.89 | 29.67 | 0.18 | 65.70 |
| Parametric Lognormal | 20.60 | 28.47 | 42.27 | 22.40 | 6.90 | 1.35 | 29.80 |
| Parametric Normal | 52.01 | 41.62 | 26.93 | 12.45 | 3.23 | 0.26 | 22.75 |
| Quadratic Splines | 14.31 | 18.38 | 16.79 | 9.21 | 2.43 | 0.80 | 10.20 |

*Notes.* Results indicate, in unit of dollar, the absolute pricing error. We infer the RND by using three illiquid quotes of Scenario 1 and Scenario 2, as illustrated in Table [2](https://arxiv.org/html/2512.11731v1#S5.T2 "Table 2 ‣ 5 Empirical Analysis ‣ Transfer Learning (Il)liquidity"). We evaluate on evenly spaced strikes between 1900 and 2150, and report the Mean Absolute Error (MAE) as the average absolute pricing error across all strikes.

## 6 Concluding Remarks

We address the estimation of the risk-neutral density under illiquid market conditions. Such conditions arise frequently, not only in illiquid option markets, but also for options written on traded equities, and they pose a major challenge for reliable RND estimation. The Deep-LSE model overcomes these difficulties by learning the shape, location, and general form of the implied volatility function of a proxy and liquid market. It then transfers this knowledge to estimate the implied volatility function of the target illiquid market. The simulation study and empirical analysis show that the Deep-LSE model recovers the RND with as few as three option quotes, and yields the lowest pricing error with respect to popular RND estimation methods.

Appendix of ”Transfer Learning (Il)liquidity”

In Appendix [A](https://arxiv.org/html/2512.11731v1#A1 "Appendix A Architecture of the Deep-LSE ‣ Transfer Learning (Il)liquidity"), we show additional theoretical details related to the Deep-LSE model. Appendix [B](https://arxiv.org/html/2512.11731v1#A2 "Appendix B Proofs ‣ Transfer Learning (Il)liquidity") illustrates the proofs related to the convexity property of the Deep-LSE model (Appendix [B.1](https://arxiv.org/html/2512.11731v1#A2.SS1 "B.1 Convexity ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity")), the link between the Deep-LSE model and the class of max-affine functions (Appendix [B.2](https://arxiv.org/html/2512.11731v1#A2.SS2 "B.2 Bounds ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity")), and in Appendix [B.3](https://arxiv.org/html/2512.11731v1#A2.SS3 "B.3 Universal Approximation Theorem ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") we prove the Universal Approximation theorem of the Deep-LSE for convex functions. We conclude the theoretical framework by illustrating in Appendix [B.4](https://arxiv.org/html/2512.11731v1#A2.SS4 "B.4 Sieve M-estimation and Consistency ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") proofs related to Sieve-M estimation and consistency. Regarding the simulation studies (Appendix [C](https://arxiv.org/html/2512.11731v1#A3 "Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity")), we test the Deep-LSE in illiquid markets using the data-generating process of Kou-Heston (Appendix [C.1](https://arxiv.org/html/2512.11731v1#A3.SS1 "C.1 Kou-Heston Stochastic Volatility model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity")), Andersen-Benzoni-Lund (Appendix [C.2](https://arxiv.org/html/2512.11731v1#A3.SS2 "C.2 Andersen-Benzoni-Lund Multifactor Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity")), and the Three-Factor Double Exponential (Appendix [C.3](https://arxiv.org/html/2512.11731v1#A3.SS3 "C.3 Three-Factor Double Exponential Stochastic Volatility Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity")). In the end, we illustrate in Appendix [D](https://arxiv.org/html/2512.11731v1#A4 "Appendix D Additional Empirical Analysis ‣ Transfer Learning (Il)liquidity") additional details regarding the training process of the Deep-LSE model on SPX market data.

## Appendix A Architecture of the Deep-LSE

We present the architecture of the Deep-LSE with two layers. Let x∈ℝdx\in\mathbb{R}^{d} denote the input and K1,K2∈ℕK\_{1},K\_{2}\in\mathbb{N} be the number of affine pieces (neurons) in the first and second LSE layers, and let T1,T2>0T\_{1},T\_{2}>0 define their temperatures.

Let k=1,…,K1k=1,\dots,K\_{1}, define one affine function

|  |  |  |
| --- | --- | --- |
|  | ℓk(1)​(x)=ak(1)​x⊤+bk(1),ak(1)∈ℝd,bk(1)∈ℝ.\ell^{(1)}\_{k}(x)\;=\;a^{(1)}\_{k}{}^{\!\top}x+b^{(1)}\_{k},\qquad a^{(1)}\_{k}\in\mathbb{R}^{d},\;b^{(1)}\_{k}\in\mathbb{R}. |  |

Stack them into

|  |  |  |
| --- | --- | --- |
|  | L(1)​(x)=[ℓ1(1)​(x)⋮ℓK1(1)​(x)]∈ℝK1.L^{(1)}(x)=\begin{bmatrix}\ell^{(1)}\_{1}(x)\\ \vdots\\ \ell^{(1)}\_{K\_{1}}(x)\end{bmatrix}\in\mathbb{R}^{K\_{1}}. |  |

The first-layer scalar output is

|  |  |  |
| --- | --- | --- |
|  | z1​(x)=LSET1⁡(L(1)​(x))=T1​log⁡(∑k=1K1eℓk(1)​(x)/T1)∈ℝ.z\_{1}(x)\;=\;\operatorname{LSE}\_{T\_{1}}\!\big(L^{(1)}(x)\big)\;=\;T\_{1}\log\!\Big(\sum\_{k=1}^{K\_{1}}e^{\,\ell^{(1)}\_{k}(x)/T\_{1}}\Big)\in\mathbb{R}. |  |

In matrix form, A(1)∈ℝK1×dA^{(1)}\in\mathbb{R}^{K\_{1}\times d} collects the row vectors (ak(1))⊤(a^{(1)}\_{k})^{\top}, b(1)∈ℝK1b^{(1)}\in\mathbb{R}^{K\_{1}} collects the biases, then

|  |  |  |
| --- | --- | --- |
|  | L(1)​(x)=A(1)​x+b(1),z1​(x)=LSET1⁡(A(1)​x+b(1)).L^{(1)}(x)=A^{(1)}x+b^{(1)},\qquad z\_{1}(x)=\operatorname{LSE}\_{T\_{1}}\!\big(A^{(1)}x+b^{(1)}\big). |  |

For the second layer, let k=1,…,K2k=1,\dots,K\_{2}, define a second family of affines

|  |  |  |
| --- | --- | --- |
|  | ℓk(2)​(x)=ak(2)​x⊤+bk(2),ak(2)∈ℝd,bk(2)∈ℝ\ell^{(2)}\_{k}(x)\;=\;a^{(2)}\_{k}{}^{\!\top}x+b^{(2)}\_{k},\qquad a^{(2)}\_{k}\in\mathbb{R}^{d},\;b^{(2)}\_{k}\in\mathbb{R} |  |

and define αk≥0\alpha\_{k}\geq 0 the nonnegative skip weight from the first layer to the kk-th second-layer piece

|  |  |  |
| --- | --- | --- |
|  | αk=softplus⁡(ηk),ηk∈ℝ.\alpha\_{k}\;=\;\operatorname{softplus}(\eta\_{k}),\qquad\eta\_{k}\in\mathbb{R}. |  |

Form the second-layer score vector

|  |  |  |
| --- | --- | --- |
|  | S(2)​(x)=[α1​z1​(x)+ℓ1(2)​(x)⋮αK2​z1​(x)+ℓK2(2)​(x)]=α​z1​(x)+L(2)​(x)∈ℝK2,S^{(2)}(x)\;=\;\begin{bmatrix}\alpha\_{1}z\_{1}(x)+\ell^{(2)}\_{1}(x)\\ \vdots\\ \alpha\_{K\_{2}}z\_{1}(x)+\ell^{(2)}\_{K\_{2}}(x)\end{bmatrix}\;=\;\alpha\,z\_{1}(x)+L^{(2)}(x)\;\in\;\mathbb{R}^{K\_{2}}, |  |

where α=(α1,…,αK2)⊤∈ℝ≥0K2\alpha=(\alpha\_{1},\ldots,\alpha\_{K\_{2}})^{\top}\in\mathbb{R}^{K\_{2}}\_{\geq 0}, and

|  |  |  |
| --- | --- | --- |
|  | L(2)​(x)=[ℓ1(2)​(x)⋮ℓK2(2)​(x)]=A(2)​x+b(2),A(2)∈ℝK2×d,b(2)∈ℝK2.L^{(2)}(x)=\begin{bmatrix}\ell^{(2)}\_{1}(x)\\ \vdots\\ \ell^{(2)}\_{K\_{2}}(x)\end{bmatrix}=A^{(2)}x+b^{(2)},\quad A^{(2)}\in\mathbb{R}^{K\_{2}\times d},\;b^{(2)}\in\mathbb{R}^{K\_{2}}. |  |

The network output is the LSE over these scores plus the global bias

|  |  |  |
| --- | --- | --- |
|  | y​(x)=LSET2⁡(S(2)​(x))+cout=T2​log⁡(∑k=1K2e(αk​z1​(x)+ℓk(2)​(x))/T2)+cout∈ℝ.y(x)\;=\;\operatorname{LSE}\_{T\_{2}}\!\big(S^{(2)}(x)\big)+c\_{\text{out}}\;=\;T\_{2}\log\!\Big(\sum\_{k=1}^{K\_{2}}e^{\,(\alpha\_{k}z\_{1}(x)+\ell^{(2)}\_{k}(x))/T\_{2}}\Big)+c\_{\text{out}}\in\mathbb{R}. |  |

Alltogheter, this yields a compact expression for the 2-layer Deep-LSE

|  |  |  |  |
| --- | --- | --- | --- |
|  | z1​(x)\displaystyle z\_{1}(x) | =T1​log⁡(∑i=1K1e(ai(1)​x⊤+bi(1))/T1),\displaystyle=T\_{1}\log\!\Big(\sum\_{i=1}^{K\_{1}}e^{\,\big(a^{(1)}\_{i}{}^{\!\top}x+b^{(1)}\_{i}\big)/T\_{1}}\Big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(x)\displaystyle y(x) | =T2​log⁡(∑k=1K2exp⁡(αk​z1​(x)+ak(2)​x⊤+bk(2)T2))+cout.\displaystyle=T\_{2}\log\!\Bigg(\sum\_{k=1}^{K\_{2}}\exp\!\Big(\frac{\alpha\_{k}\,z\_{1}(x)+a^{(2)}\_{k}{}^{\!\top}x+b^{(2)}\_{k}}{T\_{2}}\Big)\Bigg)\;+\;c\_{\text{out}}. |  |

## Appendix B Proofs

### B.1 Convexity

Set f​(x)=(f1​(x),…,fm​(x))f(x)=(f\_{1}(x),\dots,f\_{m}(x)) and epi​h={(u,t):h​(u)≤t}\mathrm{epi}\,h=\{(u,t):\,h(u)\leq t\}, which is convex by convexity of hh. Since hh is nondecreasing, for any u≤vu\leq v componentwise and any tt with h​(v)≤th(v)\leq t we also have h​(u)≤th(u)\leq t, hence

|  |  |  |
| --- | --- | --- |
|  | {(x,t):h​(f​(x))≤t}={(x,t):∃u​s.t.​u≥f​(x)​and​(u,t)∈epi​h}.\{(x,t):\,h(f(x))\leq t\}\;=\;\{(x,t):\,\exists\,u\ \text{s.t.}\ u\geq f(x)\ \text{and}\ (u,t)\in\mathrm{epi}\,h\}. |  |

The right-hand side is the projection of the convex set {(x,u,t):u≥f​(x),(u,t)∈epi​h}\{(x,u,t):\ u\geq f(x),\ (u,t)\in\mathrm{epi}\,h\}, which is convex because u↦u−f​(x)u\mapsto u-f(x) has convex preimage when each fif\_{i} is convex. Therefore the epigraph of x↦h​(f​(x))x\mapsto h(f(x)) is convex.
∎

For u∈ℝmu\in\mathbb{R}^{m} and T>0T>0, LSET⁡(u)=T​log​∑i=1meui/T\operatorname{LSE}\_{T}(u)=T\log\!\sum\_{i=1}^{m}e^{u\_{i}/T} is convex and coordinate-wise nondecreasing: its gradient is the softmax pi​(u/T)≥0p\_{i}(u/T)\geq 0, and its Hessian is
  
1T​(Diag​(p)−p​p⊤)⪰0\frac{1}{T}\!\left(\mathrm{Diag}(p)-pp^{\top}\right)\succeq 0. Hence, precomposition with an affine map preserves convexity.

For the base step, take z(1)​(x)=LSET1⁡(A(1)​x+b(1))z^{(1)}(x)=\operatorname{LSE}\_{T\_{1}}(A^{(1)}x+b^{(1)}) is convex (affine precomposition of a convex function).

Regarding the inductive step, assume z(ℓ−1)z^{(\ell-1)} is convex. For each k≤Kℓk\leq K\_{\ell} set sk(ℓ)​(x)=αk(ℓ)​z(ℓ−1)​(x)+ak(ℓ)​x⊤+bk(ℓ)s^{(\ell)}\_{k}(x)=\alpha^{(\ell)}\_{k}z^{(\ell-1)}(x)+a^{(\ell)}\_{k}{}^{\top}x+b^{(\ell)}\_{k}, with ak(ℓ)⊤a^{(\ell)}\_{k}{}^{\top} the kkth row of A(ℓ)A^{(\ell)}. Because αk(ℓ)≥0\alpha^{(\ell)}\_{k}\geq 0 and z(ℓ−1)z^{(\ell-1)} is convex, sk(ℓ)s^{(\ell)}\_{k} is convex (nonnegative translation of a convex function plus an affine function).

Since LSETℓ\operatorname{LSE}\_{T\_{\ell}} is convex and nondecreasing in the arguments, the composition rule for convex functions implies z(ℓ)​(x)=LSETℓ⁡(s1(ℓ)​(x),…,sKℓ(ℓ)​(x))z^{(\ell)}(x)=\operatorname{LSE}\_{T\_{\ell}}\big(s^{(\ell)}\_{1}(x),\ldots,s^{(\ell)}\_{K\_{\ell}}(x)\big) is convex. By induction, all z(ℓ)z^{(\ell)} are convex. Adding the constant coutc\_{\mathrm{out}} does not affect convexity, so yy is convex.
∎

Each coordinate of L(1)​(x)=A(1)​x+b(1)L^{(1)}(x)=A^{(1)}x+b^{(1)} is affine, hence convex. For u∈ℝmu\in\mathbb{R}^{m} and T>0T>0,

|  |  |  |
| --- | --- | --- |
|  | LSET⁡(u)=T​log⁡(∑i=1meui/T)\operatorname{LSE}\_{T}(u)\;=\;T\log\!\Big(\sum\_{i=1}^{m}e^{u\_{i}/T}\Big) |  |

is convex in uu and coordinate-wise nondecreasing. Convexity follows from [calafiore2019log] since it is a log-Laplace transform. While coordinate-wise monotonicity follows since u≤vu\leq v componentwise implies ∑ieui/T≤∑ievi/T\sum\_{i}e^{u\_{i}/T}\leq\sum\_{i}e^{v\_{i}/T}, hence LSET⁡(u)≤LSET⁡(v)\operatorname{LSE}\_{T}(u)\leq\operatorname{LSE}\_{T}(v). Therefore, z1​(x)=LSET1⁡(L(1)​(x))z\_{1}(x)=\operatorname{LSE}\_{T\_{1}}(L^{(1)}(x)) is convex.

Regarding the second layer, for k=1,…,K2k=1,\dots,K\_{2} define

|  |  |  |
| --- | --- | --- |
|  | sk​(x)=αk​z1​(x)+ℓk(2)​(x)withℓk(2)​(x)=ak(2)​x⊤+bk(2).s\_{k}(x)\;=\;\alpha\_{k}\,z\_{1}(x)+\ell^{(2)}\_{k}(x)\quad\text{with}\quad\ell^{(2)}\_{k}(x)=a^{(2)}\_{k}{}^{\top}x+b^{(2)}\_{k}. |  |

Since αk≥0\alpha\_{k}\geq 0 and z1z\_{1} is convex, αk​z1\alpha\_{k}z\_{1} is convex; ℓk(2)\ell^{(2)}\_{k} is affine; hence sks\_{k} is convex because positive scaling and addition preserve convexity. Writing S(2)​(x)=(s1​(x),…,sK2​(x))⊤S^{(2)}(x)=(s\_{1}(x),\dots,s\_{K\_{2}}(x))^{\top}, each component is convex.

Similarly, h​(u)=LSET2⁡(u)h(u)=\operatorname{LSE}\_{T\_{2}}(u) is convex and coordinate-wise nondecreasing. Using Lemma [3.1](https://arxiv.org/html/2512.11731v1#S3.Thmassumption1 "Lemma 3.1 (Monotone convex composition). ‣ 3.1 Convexity ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") with h=LSET2h=\operatorname{LSE}\_{T\_{2}} and fk=skf\_{k}=s\_{k} yields that x↦LSET2⁡(S(2)​(x))x\mapsto\operatorname{LSE}\_{T\_{2}}(S^{(2)}(x)) is convex. Adding the constant bias coutc\_{\mathrm{out}} preserves convexity.
∎

### B.2 Bounds

For any T>0T>0, any K∈ℕK\in\mathbb{N}, and any v=(v1,…,vK)∈ℝKv=(v\_{1},\dots,v\_{K})\in\mathbb{R}^{K},

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxi⁡vi≤LSET⁡(v)≤maxi⁡vi+T​log⁡K.\max\_{i}v\_{i}\ \leq\ \operatorname{LSE}\_{T}(v)\ \leq\ \max\_{i}v\_{i}\ +\ T\log K. |  | (B.1) |

Moreover, LSET\operatorname{LSE}\_{T} is nondecreasing because if v≤wv\leq w, then
LSET⁡(v)≤LSET⁡(w)\operatorname{LSE}\_{T}(v)\leq\operatorname{LSE}\_{T}(w). Both properties are standard and follow from

|  |  |  |
| --- | --- | --- |
|  | LSET⁡(v)=T​log⁡(∑i=1Kevi/T)=maxi⁡vi+T​log​∑i=1Ke(vi−maxj⁡vj)/T,\operatorname{LSE}\_{T}(v)=T\log\!\Big(\sum\_{i=1}^{K}e^{v\_{i}/T}\Big)=\max\_{i}v\_{i}\ +\ T\log\!\sum\_{i=1}^{K}e^{(v\_{i}-\max\_{j}v\_{j})/T}, |  |

using that each exponent is ≤0\leq 0 and at least one is 0. Now, define the KℓK\_{\ell}-vector

|  |  |  |
| --- | --- | --- |
|  | u(ℓ)​(x)=(u1(ℓ)​(x),…,uKℓ(ℓ)​(x)),uk(ℓ)​(x)=αk(ℓ)​z(ℓ−1)​(x)+ℓk(ℓ)​(x)(ℓ≥2),u^{(\ell)}(x)\ =\ \big(u^{(\ell)}\_{1}(x),\dots,u^{(\ell)}\_{K\_{\ell}}(x)\big),\qquad u^{(\ell)}\_{k}(x)\ =\ \alpha^{(\ell)}\_{k}\,z^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\quad(\ell\geq 2), |  |

and for ℓ=1\ell=1 we simply write uk(1)​(x)=ℓk(1)​(x)u^{(1)}\_{k}(x)=\ell^{(1)}\_{k}(x). Then, by construction

|  |  |  |
| --- | --- | --- |
|  | z(ℓ)​(x)=LSETℓ⁡(u(ℓ)​(x)),z¯(ℓ)​(x)=maxk∈[Kℓ]⁡uk(ℓ)​(x)|z(ℓ−1)=z¯(ℓ−1).z^{(\ell)}(x)\ =\ \operatorname{LSE}\_{T\_{\ell}}\!\big(u^{(\ell)}(x)\big),\qquad\bar{z}^{(\ell)}(x)\ =\ \max\_{k\in[K\_{\ell}]}u^{(\ell)}\_{k}(x)\ \Big|\_{\,z^{(\ell-1)}\ =\ \bar{z}^{(\ell-1)}}. |  |

The theorem states that for each ℓ=1,…,L\ell=1,\dots,L, the bound Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") holds with Δℓ\Delta\_{\ell} as in Eq. [3.2](https://arxiv.org/html/2512.11731v1#S3.E2 "Equation 3.2 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity"). We prove this by induction on ℓ\ell, since we are generalizing to LL layers.
For the base case ℓ=1\ell=1 we have u(1)​(x)=(ℓk(1)​(x))k=1K1u^{(1)}(x)=(\ell^{(1)}\_{k}(x))\_{k=1}^{K\_{1}}, so

|  |  |  |
| --- | --- | --- |
|  | z(1)​(x)=LSET1⁡(u(1)​(x)),z¯(1)​(x)=maxi∈[K1]⁡ℓi(1)​(x).z^{(1)}(x)=\operatorname{LSE}\_{T\_{1}}\!\big(u^{(1)}(x)\big),\qquad\bar{z}^{(1)}(x)=\max\_{i\in[K\_{1}]}\ell^{(1)}\_{i}(x). |  |

Applying Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") with T=T1T=T\_{1} and K=K1K=K\_{1} gives

|  |  |  |
| --- | --- | --- |
|  | z¯(1)​(x)≤z(1)​(x)≤z¯(1)​(x)+T1​log⁡K1,\bar{z}^{(1)}(x)\ \leq\ z^{(1)}(x)\ \leq\ \bar{z}^{(1)}(x)+T\_{1}\log K\_{1}, |  |

which is Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") with Δ1=T1​log⁡K1\Delta\_{1}=T\_{1}\log K\_{1}.
By induction, assume Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") holds for some ℓ−1≥1\ell-1\geq 1, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | z¯(ℓ−1)​(x)≤z(ℓ−1)​(x)≤z¯(ℓ−1)​(x)+Δℓ−1for all ​x.\bar{z}^{(\ell-1)}(x)\ \leq\ z^{(\ell-1)}(x)\ \leq\ \bar{z}^{(\ell-1)}(x)+\Delta\_{\ell-1}\quad\text{for all }x. |  | (B.2) |

Regarding the lower bound at layer ℓ\ell, by definition and left inequality in Eq. [B.1](https://arxiv.org/html/2512.11731v1#A2.E1 "Equation B.1 ‣ B.2 Bounds ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity"),

|  |  |  |
| --- | --- | --- |
|  | z(ℓ)​(x)=LSETℓ⁡(u(ℓ)​(x))≥maxk⁡uk(ℓ)​(x)=maxk⁡(αk(ℓ)​z(ℓ−1)​(x)+ℓk(ℓ)​(x)).z^{(\ell)}(x)\ =\ \operatorname{LSE}\_{T\_{\ell}}\!\big(u^{(\ell)}(x)\big)\ \geq\ \max\_{k}u^{(\ell)}\_{k}(x)\ =\ \max\_{k}\Big(\alpha^{(\ell)}\_{k}\,z^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\Big). |  |

Using the left inequality in Eq. [B.2](https://arxiv.org/html/2512.11731v1#A2.E2 "Equation B.2 ‣ B.2 Bounds ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") (z(ℓ−1)≥z¯(ℓ−1)z^{(\ell-1)}\geq\bar{z}^{(\ell-1)}) and the fact that each αk(ℓ)≥0\alpha^{(\ell)}\_{k}\geq 0 (so the map t↦αk(ℓ)​tt\mapsto\alpha^{(\ell)}\_{k}t is nondecreasing), we obtain

|  |  |  |
| --- | --- | --- |
|  | z(ℓ)​(x)≥maxk⁡(αk(ℓ)​z¯(ℓ−1)​(x)+ℓk(ℓ)​(x))=z¯(ℓ)​(x),z^{(\ell)}(x)\ \geq\ \max\_{k}\Big(\alpha^{(\ell)}\_{k}\,\bar{z}^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\Big)\ =\ \bar{z}^{(\ell)}(x), |  |

proving the left side of Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") at layer ℓ\ell.

Regarding the upper bound at layer ℓ\ell we apply the right inequality in Eq. [B.1](https://arxiv.org/html/2512.11731v1#A2.E1 "Equation B.1 ‣ B.2 Bounds ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") to u(ℓ)​(x)u^{(\ell)}(x)

|  |  |  |  |
| --- | --- | --- | --- |
|  | z(ℓ)​(x)\displaystyle z^{(\ell)}(x) | =LSETℓ⁡(u(ℓ)​(x))\displaystyle=\operatorname{LSE}\_{T\_{\ell}}\!\big(u^{(\ell)}(x)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Tℓ​log⁡Kℓ+maxk⁡uk(ℓ)​(x)\displaystyle\leq T\_{\ell}\log K\_{\ell}\;+\;\max\_{k}u^{(\ell)}\_{k}(x) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Tℓ​log⁡Kℓ+maxk⁡(αk(ℓ)​z(ℓ−1)​(x)+ℓk(ℓ)​(x)).\displaystyle=T\_{\ell}\log K\_{\ell}\;+\;\max\_{k}\!\Big(\alpha^{(\ell)}\_{k}\,z^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\Big). |  | (B.3) |

Insert the upper bound from the induction hypothesis Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") into the rightmost term of Eq. [B.3](https://arxiv.org/html/2512.11731v1#A2.E3 "Equation B.3 ‣ B.2 Bounds ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity")

|  |  |  |
| --- | --- | --- |
|  | maxk⁡(αk(ℓ)​z(ℓ−1)​(x)+ℓk(ℓ)​(x))≤maxk⁡(αk(ℓ)​(z¯(ℓ−1)​(x)+Δℓ−1)+ℓk(ℓ)​(x)).\max\_{k}\Big(\alpha^{(\ell)}\_{k}\,z^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\Big)\ \leq\ \max\_{k}\Big(\alpha^{(\ell)}\_{k}\,\big(\bar{z}^{(\ell-1)}(x)+\Delta\_{\ell-1}\big)+\ell^{(\ell)}\_{k}(x)\Big). |  |

Split the contribution of Δℓ−1\Delta\_{\ell-1} out of the maximum using αk(ℓ)≤αmax(ℓ)\alpha^{(\ell)}\_{k}\leq\alpha^{(\ell)}\_{\max}

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxk⁡(αk(ℓ)​(z¯(ℓ−1)+Δℓ−1)+ℓk(ℓ))\displaystyle\max\_{k}\Big(\alpha^{(\ell)}\_{k}\,\big(\bar{z}^{(\ell-1)}+\Delta\_{\ell-1}\big)+\ell^{(\ell)}\_{k}\Big) | =maxk⁡(αk(ℓ)​z¯(ℓ−1)+ℓk(ℓ)+αk(ℓ)​Δℓ−1)\displaystyle=\max\_{k}\Big(\alpha^{(\ell)}\_{k}\,\bar{z}^{(\ell-1)}+\ell^{(\ell)}\_{k}\ +\ \alpha^{(\ell)}\_{k}\Delta\_{\ell-1}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤maxk⁡(αk(ℓ)​z¯(ℓ−1)+ℓk(ℓ))+αmax(ℓ)​Δℓ−1\displaystyle\leq\max\_{k}\Big(\alpha^{(\ell)}\_{k}\,\bar{z}^{(\ell-1)}+\ell^{(\ell)}\_{k}\Big)\ +\ \alpha^{(\ell)}\_{\max}\,\Delta\_{\ell-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =z¯(ℓ)​(x)+αmax(ℓ)​Δℓ−1.\displaystyle=\ \bar{z}^{(\ell)}(x)\ +\ \alpha^{(\ell)}\_{\max}\,\Delta\_{\ell-1}. |  |

Combining with Eq. [B.3](https://arxiv.org/html/2512.11731v1#A2.E3 "Equation B.3 ‣ B.2 Bounds ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") yields

|  |  |  |
| --- | --- | --- |
|  | z(ℓ)​(x)≤z¯(ℓ)​(x)+(Tℓ​log⁡Kℓ+αmax(ℓ)​Δℓ−1)⏟=⁣:Δℓ.z^{(\ell)}(x)\ \leq\ \bar{z}^{(\ell)}(x)\ +\ \underbrace{\Big(T\_{\ell}\log K\_{\ell}+\alpha^{(\ell)}\_{\max}\Delta\_{\ell-1}\Big)}\_{=:\ \Delta\_{\ell}}. |  |

This is the right side of Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") with the recursive definition Eq. [3.2](https://arxiv.org/html/2512.11731v1#S3.E2 "Equation 3.2 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity"). We have proved Eq. [3.1](https://arxiv.org/html/2512.11731v1#S3.E1 "Equation 3.1 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") for layer ℓ\ell assuming it for ℓ−1\ell-1. Together with the base case, the claim holds for all ℓ=1,…,L\ell=1,\dots,L.
Developing the linear recursion Eq. [3.2](https://arxiv.org/html/2512.11731v1#S3.E2 "Equation 3.2 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") gives

|  |  |  |
| --- | --- | --- |
|  | Δℓ=Tℓ​log⁡Kℓ+αmax(ℓ)​Δℓ−1=Tℓ​log⁡Kℓ+αmax(ℓ)​(Tℓ−1​log⁡Kℓ−1+αmax(ℓ−1)​Δℓ−2),\Delta\_{\ell}=T\_{\ell}\log K\_{\ell}+\alpha^{(\ell)}\_{\max}\Delta\_{\ell-1}=T\_{\ell}\log K\_{\ell}+\alpha^{(\ell)}\_{\max}\Big(T\_{\ell-1}\log K\_{\ell-1}+\alpha^{(\ell-1)}\_{\max}\Delta\_{\ell-2}\Big), |  |

and continue until Δ1=T1​log⁡K1\Delta\_{1}=T\_{1}\log K\_{1}. Collecting terms we obtain

|  |  |  |
| --- | --- | --- |
|  | Δℓ=∑j=1ℓ(Tj​log⁡Kj​∏r=j+1ℓαmax(r)),\Delta\_{\ell}=\sum\_{j=1}^{\ell}\Bigg(T\_{j}\log K\_{j}\ \prod\_{r=j+1}^{\ell}\alpha^{(r)}\_{\max}\Bigg), |  |

which is Eq. [3.3](https://arxiv.org/html/2512.11731v1#S3.E3 "Equation 3.3 ‣ Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity"). This expansion shows that the penalty temperature of each layer (Tj​log⁡KjT\_{j}\log K\_{j}) is amplified by the nonnegative skips. Finally, setting y​(x)=z(L)​(x)+couty(x)=z^{(L)}(x)+c\_{\mathrm{out}} and y¯​(x)=z¯(L)​(x)+cout\bar{y}(x)=\bar{z}^{(L)}(x)+c\_{\mathrm{out}} simply shifts both sides by the same constant, yielding

|  |  |  |
| --- | --- | --- |
|  | 0≤y​(x)−y¯​(x)=z(L)​(x)−z¯(L)​(x)≤ΔL.0\ \leq\ y(x)-\bar{y}(x)\ =\ z^{(L)}(x)-\bar{z}^{(L)}(x)\ \leq\ \Delta\_{L}. |  |

∎

In the first layer, by the standard LSE bounds,

|  |  |  |
| --- | --- | --- |
|  | z¯1​(x)≤z1​(x)≤z¯1​(x)+T1​log⁡K1.\bar{z}\_{1}(x)\ \leq\ z\_{1}(x)\ \leq\ \bar{z}\_{1}(x)+T\_{1}\log K\_{1}. |  |

In the second layer, lower bound, since LSET2\operatorname{LSE}\_{T\_{2}} is coordinatewise nondecreasing and dominates the pointwise maximum,

|  |  |  |
| --- | --- | --- |
|  | y​(x)−cout=LSET2⁡({αk​z1​(x)+⟨Ak,⋅(2),x⟩+bk(2)}k=1K2)≥maxk⁡(αk​z1​(x)+⟨Ak,⋅(2),x⟩+bk(2)).y(x)-c\_{\mathrm{out}}=\operatorname{LSE}\_{T\_{2}}\!\big(\{\alpha\_{k}z\_{1}(x)+\langle A^{(2)}\_{k,\cdot},x\rangle+b^{(2)}\_{k}\}\_{k=1}^{K\_{2}}\big)\geq\max\_{k}\big(\alpha\_{k}z\_{1}(x)+\langle A^{(2)}\_{k,\cdot},x\rangle+b^{(2)}\_{k}\big). |  |

Using z1​(x)≥z¯1​(x)z\_{1}(x)\geq\bar{z}\_{1}(x) from (1) and adding coutc\_{\mathrm{out}} gives y​(x)≥y¯​(x)y(x)\geq\bar{y}(x).
In the second layer, upper bound, again by the LSE bound,
set, for each kk,

|  |  |  |
| --- | --- | --- |
|  | uk​(x)=αk​z1​(x)+⟨Ak,⋅(2),x⟩+bk(2),u​(x)=(uk​(x))k=1K2∈ℝK2.u\_{k}(x)=\alpha\_{k}z\_{1}(x)+\langle A^{(2)}\_{k,\cdot},x\rangle+b^{(2)}\_{k},\qquad u(x)=(u\_{k}(x))\_{k=1}^{K\_{2}}\in\mathbb{R}^{K\_{2}}. |  |

Then y​(x)−cout=LSET2⁡(u​(x))y(x)-c\_{\mathrm{out}}=\operatorname{LSE}\_{T\_{2}}(u(x)), so applying the inequality with K=K2K=K\_{2}, T=T2T=T\_{2} to u​(x)u(x) yields

|  |  |  |
| --- | --- | --- |
|  | LSET2⁡(u​(x))≤T2​log⁡K2+maxk⁡uk​(x)=T2​log⁡K2+maxk⁡(αk​z1​(x)+⟨Ak,⋅(2),x⟩+bk(2)).\operatorname{LSE}\_{T\_{2}}(u(x))\ \leq\ T\_{2}\log K\_{2}+\max\_{k}u\_{k}(x)\ =\ T\_{2}\log K\_{2}+\max\_{k}\big(\alpha\_{k}z\_{1}(x)+\langle A^{(2)}\_{k,\cdot},x\rangle+b^{(2)}\_{k}\big). |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(x)−cout\displaystyle y(x)-c\_{\mathrm{out}} | ≤T2​log⁡K2+maxk⁡(αk​z1​(x)+⟨Ak,⋅(2),x⟩+bk(2))\displaystyle\leq T\_{2}\log K\_{2}+\max\_{k}\big(\alpha\_{k}z\_{1}(x)+\langle A^{(2)}\_{k,\cdot},x\rangle+b^{(2)}\_{k}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T2​log⁡K2+maxk⁡(αk​(z¯1​(x)+T1​log⁡K1)+⟨Ak,⋅(2),x⟩+bk(2))by (1) and ​αk≥0\displaystyle\leq T\_{2}\log K\_{2}+\max\_{k}\big(\alpha\_{k}(\bar{z}\_{1}(x)+T\_{1}\log K\_{1})+\langle A^{(2)}\_{k,\cdot},x\rangle+b^{(2)}\_{k}\big)\quad\text{by (1) and }\alpha\_{k}\geq 0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T2​log⁡K2+αmax​T1​log⁡K1+maxk⁡(αk​z¯1​(x)+⟨Ak,⋅(2),x⟩+bk(2)).\displaystyle=T\_{2}\log K\_{2}+\alpha\_{\max}T\_{1}\log K\_{1}+\max\_{k}\big(\alpha\_{k}\bar{z}\_{1}(x)+\langle A^{(2)}\_{k,\cdot},x\rangle+b^{(2)}\_{k}\big). |  |

Adding coutc\_{\mathrm{out}} yields the upper bound for y​(x)y(x).
∎

### B.3 Universal Approximation Theorem

We proceed by induction on the depth ℓ\ell to establish the max–affine representation of the theorem and the recursive formulas for (Ap[ℓ],bp[ℓ])(A\_{p}^{[\ell]},b\_{p}^{[\ell]}).

For the base case ℓ=1\ell=1, by definition,

|  |  |  |
| --- | --- | --- |
|  | z¯(1)​(x)=maxk1∈{1,…,K1}⁡(⟨Ak1(1),x⟩+bk1(1)),\bar{z}^{(1)}(x)=\max\_{k\_{1}\in\{1,\dots,K\_{1}\}}\bigl(\langle A^{(1)}\_{k\_{1}},x\rangle+b^{(1)}\_{k\_{1}}\bigr), |  |

so the statement holds with P1={1,…,K1}P\_{1}=\{1,\dots,K\_{1}\} and A(k1)[1]=Ak1(1)A^{[1]}\_{(k\_{1})}=A^{(1)}\_{k\_{1}}, b(k1)[1]=bk1(1)b^{[1]}\_{(k\_{1})}=b^{(1)}\_{k\_{1}}.

Regarding the induction step, assume for some ℓ≥2\ell\geq 2 that

|  |  |  |
| --- | --- | --- |
|  | z¯(ℓ−1)​(x)=maxp∈Pℓ−1⁡(⟨Ap[ℓ−1],x⟩+bp[ℓ−1]).\bar{z}^{(\ell-1)}(x)=\max\_{p\in P\_{\ell-1}}\bigl(\langle A^{[\ell-1]}\_{p},x\rangle+b^{[\ell-1]}\_{p}\bigr). |  |

Fix k∈{1,…,Kℓ}k\in\{1,\dots,K\_{\ell}\} and note the elementary identity valid for any finite family {rj}\{r\_{j}\} and any a>0a>0

|  |  |  |
| --- | --- | --- |
|  | a⋅maxj⁡rj=maxj⁡(a​rj).a\cdot\max\_{j}r\_{j}=\max\_{j}(a\,r\_{j}). |  |

Indeed, if M=maxj⁡rjM=\max\_{j}r\_{j} then a​M≥a​rjaM\geq ar\_{j} for all jj, hence a​M≥maxj⁡a​rjaM\geq\max\_{j}ar\_{j}, and equality follows by taking j⋆j^{\star} with rj⋆=Mr\_{j^{\star}}=M.
Applying this with a=αk(ℓ)>0a=\alpha^{(\ell)}\_{k}>0 and rp=⟨Ap[ℓ−1],x⟩+bp[ℓ−1]r\_{p}=\langle A^{[\ell-1]}\_{p},x\rangle+b^{[\ell-1]}\_{p}, we obtain

|  |  |  |
| --- | --- | --- |
|  | αk(ℓ)​z¯(ℓ−1)​(x)=maxp∈Pℓ−1⁡(αk(ℓ)​⟨Ap[ℓ−1],x⟩+αk(ℓ)​bp[ℓ−1]).\alpha^{(\ell)}\_{k}\,\bar{z}^{(\ell-1)}(x)=\max\_{p\in P\_{\ell-1}}\bigl(\alpha^{(\ell)}\_{k}\langle A^{[\ell-1]}\_{p},x\rangle+\alpha^{(\ell)}\_{k}b^{[\ell-1]}\_{p}\bigr). |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | z¯(ℓ)​(x)\displaystyle\bar{z}^{(\ell)}(x) | =maxk⁡(αk(ℓ)​z¯(ℓ−1)​(x)+⟨Ak(ℓ),x⟩+bk(ℓ))\displaystyle=\max\_{k}\Bigl(\alpha^{(\ell)}\_{k}\,\bar{z}^{(\ell-1)}(x)+\langle A^{(\ell)}\_{k},x\rangle+b^{(\ell)}\_{k}\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =maxk⁡maxp∈Pℓ−1⁡(⟨αk(ℓ)​Ap[ℓ−1]+Ak(ℓ),x⟩+αk(ℓ)​bp[ℓ−1]+bk(ℓ))\displaystyle=\max\_{k}\ \max\_{p\in P\_{\ell-1}}\Bigl(\big\langle\alpha^{(\ell)}\_{k}A^{[\ell-1]}\_{p}+A^{(\ell)}\_{k},\ x\big\rangle+\alpha^{(\ell)}\_{k}b^{[\ell-1]}\_{p}+b^{(\ell)}\_{k}\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =max(p,k)∈Pℓ−1×{1,…,Kℓ}⁡(⟨A(p,k)[ℓ],x⟩+b(p,k)[ℓ]),\displaystyle=\max\_{(p,k)\in P\_{\ell-1}\times\{1,\dots,K\_{\ell}\}}\bigl(\langle A^{[\ell]}\_{(p,k)},x\rangle+b^{[\ell]}\_{(p,k)}\bigr), |  |

where

|  |  |  |
| --- | --- | --- |
|  | A(p,k)[ℓ]=αk(ℓ)​Ap[ℓ−1]+Ak(ℓ),b(p,k)[ℓ]=αk(ℓ)​bp[ℓ−1]+bk(ℓ).A^{[\ell]}\_{(p,k)}=\alpha^{(\ell)}\_{k}A^{[\ell-1]}\_{p}+A^{(\ell)}\_{k},\qquad b^{[\ell]}\_{(p,k)}=\alpha^{(\ell)}\_{k}b^{[\ell-1]}\_{p}+b^{(\ell)}\_{k}. |  |

Thus the representation holds at depth ℓ\ell with index set Pℓ=Pℓ−1×{1,…,Kℓ}P\_{\ell}=P\_{\ell-1}\times\{1,\dots,K\_{\ell}\}, completing the induction.

The explicit formulas for Ap[ℓ]A\_{p}^{[\ell]} and bp[ℓ]b\_{p}^{[\ell]} follow by repeatedly substituting the above recursion along a path p=(k1,…,kℓ)∈Pℓp=(k\_{1},\dots,k\_{\ell})\in P\_{\ell}, yielding

|  |  |  |
| --- | --- | --- |
|  | Ap[ℓ]=∑j=1ℓ(∏r=j+1ℓαkr(r))​Akj(j),bp[ℓ]=∑j=1ℓ(∏r=j+1ℓαkr(r))​bkj(j).A\_{p}^{[\ell]}=\sum\_{j=1}^{\ell}\Bigl(\prod\_{r=j+1}^{\ell}\alpha^{(r)}\_{k\_{r}}\Bigr)A^{(j)}\_{k\_{j}},\qquad b\_{p}^{[\ell]}=\sum\_{j=1}^{\ell}\Bigl(\prod\_{r=j+1}^{\ell}\alpha^{(r)}\_{k\_{r}}\Bigr)b^{(j)}\_{k\_{j}}. |  |

Finally, y¯​(x)=z¯(L)​(x)+cout\bar{y}(x)=\bar{z}^{(L)}(x)+c\_{\mathrm{out}} is a finite maximum of affine functions plus a constant and hence y¯\bar{y} is convex and continuous.
∎

To establish the proof, we use two main results: the deep-LSE bound that links our model to max-affine functions, and the density result that links max-affine functions with any convex function.

The bound (proved in Theorem [3.4](https://arxiv.org/html/2512.11731v1#S3.Thmassumption4 "Theorem 3.4 (Deep-LSE vs. deep max–affine: 𝐿 layers). ‣ 3.2 Bounds ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity")) ensures that the Deep-LSE stays within the max-affine surrogate and ΔL\Delta\_{L} for all x∈ℝdx\in\mathbb{R}^{d}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y¯​(x)≤y​(x)≤y¯​(x)+ΔL,\bar{y}(x)\ \leq\ y(x)\ \leq\ \bar{y}(x)+\Delta\_{L}, |  | (B.4) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔL=∑j=1L(Tj​log⁡Kj​∏r=j+1Lαmax(r)),αmax(ℓ)=‖α(ℓ)‖∞​(αmax(1)=1).\Delta\_{L}\ =\ \sum\_{j=1}^{L}\Bigl(T\_{j}\log K\_{j}\prod\_{r=j+1}^{L}\alpha^{(r)}\_{\max}\Bigr),\qquad\alpha^{(\ell)}\_{\max}=\|\alpha^{(\ell)}\|\_{\infty}\ (\,\alpha^{(1)}\_{\max}=1\,). |  | (B.5) |

Most importantly, by Theorem [3.6](https://arxiv.org/html/2512.11731v1#S3.Thmassumption6 "Theorem 3.6 (Deep max–affine surrogate is a finite max of affines). ‣ 3.3 Universal Approximation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity") y¯​(x)\bar{y}(x) is still a pointwise max-affine function over the path set 𝒫={(k1,…,kL): 1≤kℓ≤Kℓ}\mathcal{P}=\{(k\_{1},\ldots,k\_{L}):\ 1\leq k\_{\ell}\leq K\_{\ell}\}

|  |  |  |
| --- | --- | --- |
|  | y¯​(x)=maxp∈𝒫⁡(⟨Ap,x⟩+bp).\bar{y}(x)=\max\_{p\in\mathcal{P}}\bigl(\langle A\_{p},x\rangle+b\_{p}\bigr). |  |

Let ℳ\mathcal{M} denote the class of deep max-affine surrogates realizable by the LL-layer architecture (set Tℓ=0T\_{\ell}=0 for all layers, allow arbitrary A(ℓ),b(ℓ)A^{(\ell)},b^{(\ell)}, and α(ℓ)≥0\alpha^{(\ell)}\geq 0).
By Theorem [3.6](https://arxiv.org/html/2512.11731v1#S3.Thmassumption6 "Theorem 3.6 (Deep max–affine surrogate is a finite max of affines). ‣ 3.3 Universal Approximation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity"), ℳ\mathcal{M} is the set of finite pointwise maxima of affine functions (max-affine functions). As a consequence, max-affine functions for continuous convex functions are dense on compact convex sets [huang2020convex]. Hence, for any η>0\eta>0, there exist parameters such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤f​(x)−y¯​(x)≤ηfor all ​x∈K.0\ \leq\ f(x)-\bar{y}(x)\ \leq\ \eta\qquad\text{for all }x\in K. |  | (B.6) |

Equivalently, supx∈K|f​(x)−y¯​(x)|≤η\sup\_{x\in K}|f(x)-\bar{y}(x)|\leq\eta with nonnegative difference.
For the same weights, choose any T1,…,TL>0T\_{1},\dots,T\_{L}>0. The bound Eq. [B.4](https://arxiv.org/html/2512.11731v1#A2.E4 "Equation B.4 ‣ B.3 Universal Approximation Theorem ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") yields, for all x∈Kx\in K,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤y​(x)−y¯​(x)≤ΔL.0\ \leq\ y(x)-\bar{y}(x)\ \leq\ \Delta\_{L}. |  | (B.7) |

Combining Eq. [B.6](https://arxiv.org/html/2512.11731v1#A2.E6 "Equation B.6 ‣ B.3 Universal Approximation Theorem ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") and Eq. [B.7](https://arxiv.org/html/2512.11731v1#A2.E7 "Equation B.7 ‣ B.3 Universal Approximation Theorem ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity"), for every x∈Kx\in K,

|  |  |  |
| --- | --- | --- |
|  | |y​(x)−f​(x)|≤|y​(x)−y¯​(x)|+|y¯​(x)−f​(x)|≤ΔL+η.|y(x)-f(x)|\ \leq\ |y(x)-\bar{y}(x)|+|\bar{y}(x)-f(x)|\ \leq\ \Delta\_{L}+\eta. |  |

Since ΔL\Delta\_{L} in Eq. [B.5](https://arxiv.org/html/2512.11731v1#A2.E5 "Equation B.5 ‣ B.3 Universal Approximation Theorem ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity") is linear in (T1,…,TL)(T\_{1},\dots,T\_{L}) with nonnegative coefficients, we can choose the temperatures small enough to ensure ΔL≤ε/2\Delta\_{L}\leq\varepsilon/2. For example

|  |  |  |
| --- | --- | --- |
|  | Tj=ε2j+1/(log⁡Kj​∏r=j+1Lαmax(r))(j=1,…,L)T\_{j}\ =\ \frac{\varepsilon}{2^{j+1}}\ \Big/\ \Bigl(\log K\_{j}\ \prod\_{r=j+1}^{L}\alpha^{(r)}\_{\max}\Bigr)\quad(j=1,\dots,L) |  |

implies ΔL≤∑j=1Lε/2j+1≤ε/2\Delta\_{L}\leq\sum\_{j=1}^{L}\varepsilon/2^{j+1}\leq\varepsilon/2.
Finally set η=ε/2\eta=\varepsilon/2 in Eq. [B.6](https://arxiv.org/html/2512.11731v1#A2.E6 "Equation B.6 ‣ B.3 Universal Approximation Theorem ‣ Appendix B Proofs ‣ Transfer Learning (Il)liquidity").
Then |y​(x)−f​(x)|≤ε|y(x)-f(x)|\leq\varepsilon for all x∈Kx\in K, hence supx∈K|y​(x)−f​(x)|≤ε\sup\_{x\in K}|y(x)-f(x)|\leq\varepsilon.

All layers are active because each Tℓ>0T\_{\ell}>0 and each layer participates in forming the surrogate y¯\bar{y} in Step 1.
∎

### B.4 Sieve M-estimation and Consistency

For a closed domain 𝒳={x∈ℝd:‖x‖≤R}\mathcal{X}=\{x\in\mathbb{R}^{d}:\ \|x\|\leq R\} with 0<R<∞0<R<\infty, define a vector norm ∥⋅∥\|\cdot\| on ℝd\mathbb{R}^{d} and its dual ∥⋅∥∗\|\cdot\|\_{\*} (so |⟨u,x⟩|≤‖u‖∗​‖x‖\lvert\langle u,x\rangle\rvert\leq\|u\|\_{\*}\,\|x\|).

For layer ℓ=1,…,L\ell=1,\ldots,L: width Kℓ∈ℕK\_{\ell}\in\mathbb{N}, temperature Tℓ>0T\_{\ell}>0, parameter rows ak(ℓ)∈ℝda^{(\ell)}\_{k}\in\mathbb{R}^{d} and biases bk(ℓ)∈ℝb^{(\ell)}\_{k}\in\mathbb{R} (k=1,…,Kℓk=1,\ldots,K\_{\ell}), and skip weights αk(ℓ)≥0\alpha^{(\ell)}\_{k}\geq 0 for ℓ≥2\ell\geq 2.
Recall the affine pieces defined as

|  |  |  |
| --- | --- | --- |
|  | ℓk(ℓ)​(x)=⟨ak(ℓ),x⟩+bk(ℓ).\ell^{(\ell)}\_{k}(x)=\langle a^{(\ell)}\_{k},\,x\rangle+b^{(\ell)}\_{k}. |  |

and the Deep-LSE recursion

|  |  |  |
| --- | --- | --- |
|  | z(1)​(x)=LSET1​((ℓk(1)​(x))k=1K1),z(ℓ)​(x)=LSETℓ​((αk(ℓ)​z(ℓ−1)​(x)+ℓk(ℓ)​(x))k=1Kℓ),ℓ≥2.z^{(1)}(x)=\mathrm{LSE}\_{T\_{1}}\!\bigl(\,(\ell^{(1)}\_{k}(x))\_{k=1}^{K\_{1}}\bigr),\qquad z^{(\ell)}(x)=\mathrm{LSE}\_{T\_{\ell}}\!\bigl(\,(\alpha^{(\ell)}\_{k}\,z^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x))\_{k=1}^{K\_{\ell}}\bigr),\ \ \ell\geq 2. |  |

whose output is

|  |  |  |
| --- | --- | --- |
|  | y​(x)=z(L)​(x)+cout.y(x)=z^{(L)}(x)+c\_{\mathrm{out}}. |  |

We define the sieve constraints for each ℓ\ell

|  |  |  |
| --- | --- | --- |
|  | Mℓ=maxk⁡‖ak(ℓ)‖∗≤Sℓ,Bℓ=maxk⁡|bk(ℓ)|≤B¯ℓ,qℓ=maxk⁡αk(ℓ)≤q<1,M\_{\ell}=\max\_{k}\|a^{(\ell)}\_{k}\|\_{\*}\leq S\_{\ell},\qquad B\_{\ell}=\max\_{k}|b^{(\ell)}\_{k}|\leq\bar{B}\_{\ell},\qquad q\_{\ell}=\max\_{k}\alpha^{(\ell)}\_{k}\leq q<1, |  |

|  |  |  |
| --- | --- | --- |
|  | Kℓ≤K¯ℓ,Tℓ≤Θℓ,|cout|≤C.K\_{\ell}\leq\bar{K}\_{\ell},\qquad T\_{\ell}\leq\Theta\_{\ell},\qquad|c\_{\mathrm{out}}|\leq C. |  |

Recall that for every ℓ≥1\ell\geq 1 and x∈ℝdx\in\mathbb{R}^{d} we have

|  |  |  |
| --- | --- | --- |
|  | z¯(ℓ)​(x)≤z(ℓ)​(x)≤z¯(ℓ)​(x)+Δℓ.\bar{z}^{(\ell)}(x)\leq z^{(\ell)}(x)\leq\bar{z}^{(\ell)}(x)+\Delta\_{\ell}. |  |

|  |  |  |
| --- | --- | --- |
|  | Δℓ=∑j=1ℓTj​log⁡Kj​∏r=j+1ℓmaxk⁡αk(ℓ)=∑j=1ℓTj​log⁡Kj​∏r=j+1ℓqr.\Delta\_{\ell}=\sum\_{j=1}^{\ell}T\_{j}\log K\_{j}\prod\_{r=j+1}^{\ell}\max\_{k}\alpha^{(\ell)}\_{k}\ =\sum\_{j=1}^{\ell}T\_{j}\log K\_{j}\prod\_{r=j+1}^{\ell}q\_{r}. |  |

and with Δ1=T1​log⁡K1\Delta\_{1}=T\_{1}\log K\_{1}.
In addition, throughout the proof, we use the basic properties of dual norms
Recall that z(ℓ)=z¯(ℓ)+εℓz^{(\ell)}=\bar{z}^{(\ell)}+\varepsilon\_{\ell} with 0≤εℓ≤Δℓ0\leq\varepsilon\_{\ell}\leq\Delta\_{\ell}, hence
|z(ℓ)|≤|z¯(ℓ)|+|εℓ|≤|z¯(ℓ)|+Δℓ|z^{(\ell)}|\leq|\bar{z}^{(\ell)}|+|\varepsilon\_{\ell}|\leq|\bar{z}^{(\ell)}|+\Delta\_{\ell}.
As a consequence, for all ℓ\ell and xx,

|  |  |  |
| --- | --- | --- |
|  | |z(ℓ)​(x)|≤|z¯(ℓ)​(x)|+Δℓ(A).\bigl|z^{(\ell)}(x)\bigr|\leq\bigl|\bar{z}^{(\ell)}(x)\bigr|+\Delta\_{\ell}\quad\text{(A)}. |  |

Now, by triangle inequality and dual norm inequality (|⟨u,v⟩|≤‖u‖∗​‖v‖)(|\langle u,v\rangle|\leq\|u\|\_{\*}\,\|v\|),

|  |  |  |
| --- | --- | --- |
|  | |ℓk(ℓ)​(x)|=|⟨ak(ℓ),x⟩+bk(ℓ)|≤|⟨ak(ℓ),x⟩|+|bk(ℓ)|≤‖ak(ℓ)‖∗​‖x‖+|bk(ℓ)|.\bigl|\ell^{(\ell)}\_{k}(x)\bigr|=\bigl|\langle a^{(\ell)}\_{k},x\rangle+b^{(\ell)}\_{k}\bigr|\leq\bigl|\langle a^{(\ell)}\_{k},x\rangle\bigr|+\bigl|b^{(\ell)}\_{k}\bigr|\leq\|a^{(\ell)}\_{k}\|\_{\*}\,\|x\|+\bigl|b^{(\ell)}\_{k}\bigr|. |  |

Now take supx∈𝒳\displaystyle\sup\_{x\in\mathcal{X}} with kk fixed. Since |bk(ℓ)|\lvert b\_{k}^{(\ell)}\rvert does not depend on xx

|  |  |  |
| --- | --- | --- |
|  | sup‖x‖≤R⟨a,x⟩=R∥a∥∗,sup‖x‖≤R|⟨a,x⟩|=R∥a∥∗\sup\_{\|x\|\leq R}\langle a,x\rangle=R\|a\|\_{\*}\quad,\quad\sup\_{\|x\|\leq R}\bigl|\langle a,x\rangle\bigr|=R\|a\|\_{\*} |  |

|  |  |  |
| --- | --- | --- |
|  | supx∈𝒳(|⟨ak(ℓ),x⟩|+|bk(ℓ)|)=‖ak(ℓ)‖∗​supx∈𝒳‖x‖+|bk(ℓ)|=‖ak(ℓ)‖∗​R+|bk(ℓ)|.\sup\_{x\in\mathcal{X}}\!\bigl(\,\lvert\langle a\_{k}^{(\ell)},x\rangle\rvert+\lvert b\_{k}^{(\ell)}\rvert\,\bigr)=\|a\_{k}^{(\ell)}\|\_{\*}\,\sup\_{x\in\mathcal{X}}\|x\|+\lvert b\_{k}^{(\ell)}\rvert=\|a\_{k}^{(\ell)}\|\_{\*}\,R+\lvert b\_{k}^{(\ell)}\rvert. |  |

Finally, we take maxk\max\_{k},

|  |  |  |
| --- | --- | --- |
|  | supx∈𝒳maxk|ℓk(ℓ)(x)|≤maxk(∥ak(ℓ)∥∗R+|bk(ℓ)|)≤Rmaxk∥ak(ℓ)∥∗+maxk|bk(ℓ)|=RMℓ+Bℓ≤RSℓ+B¯ℓ.(B)\sup\_{x\in\mathcal{X}}\ \max\_{k}\bigl|\ell\_{k}^{(\ell)}(x)\bigr|\;\leq\;\max\_{k}\Bigl(\|a\_{k}^{(\ell)}\|\_{\*}\,R+\lvert b\_{k}^{(\ell)}\rvert\Bigr)\;\leq\;R\max\_{k}\|a\_{k}^{(\ell)}\|\_{\*}+\max\_{k}\lvert b\_{k}^{(\ell)}\rvert\;=\;RM\_{\ell}+B\_{\ell}\;\leq\;R\,S\_{\ell}+\bar{B}\_{\ell}.\quad\text{(B)} |  |

which follows from Mℓ≤SℓM\_{\ell}\leq S\_{\ell} and Bℓ≤B¯ℓB\_{\ell}\leq\bar{B}\_{\ell}.
Now let

|  |  |  |
| --- | --- | --- |
|  | Aℓ=supx∈𝒳|z(ℓ)​(x)|.A\_{\ell}\;=\;\sup\_{x\in\mathcal{X}}\bigl|z^{(\ell)}(x)\bigr|. |  |

For ℓ=1\ell=1, combine (A) with (B) and Δ1≤Θ1​log⁡K1\Delta\_{1}\leq\Theta\_{1}\log K\_{1}

|  |  |  |  |
| --- | --- | --- | --- |
|  | A1\displaystyle A\_{1} | =supx∈𝒳|z(1)​(x)|≤supx∈𝒳|z¯(1)​(x)|+Δ1\displaystyle=\sup\_{x\in\mathcal{X}}\bigl|z^{(1)}(x)\bigr|\leq\sup\_{x\in\mathcal{X}}\bigl|\bar{z}^{(1)}(x)\bigr|+\Delta\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supx∈𝒳maxk⁡|ℓk(1)​(x)|+Θ1​log⁡K1≤R​S1+B¯1+Θ1​log⁡K1.\displaystyle\leq\sup\_{x\in\mathcal{X}}\max\_{k}\bigl|\ell^{(1)}\_{k}(x)\bigr|+\Theta\_{1}\log K\_{1}\leq RS\_{1}+\bar{B}\_{1}+\Theta\_{1}\log K\_{1}. |  |

For ℓ≥2\ell\geq 2, for each xx, by (A),

|  |  |  |  |
| --- | --- | --- | --- |
|  | |z(ℓ)​(x)|\displaystyle\bigl|z^{(\ell)}(x)\bigr| | ≤|z¯(ℓ)​(x)|+Δℓ\displaystyle\leq\bigl|\bar{z}^{(\ell)}(x)\bigr|+\Delta\_{\ell} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤maxk⁡|αk(ℓ)​z(ℓ−1)​(x)+ℓk(ℓ)​(x)|+Δℓ\displaystyle\leq\max\_{k}\bigl|\alpha^{(\ell)}\_{k}z^{(\ell-1)}(x)+\ell^{(\ell)}\_{k}(x)\bigr|+\Delta\_{\ell} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤maxk⁡(αk(ℓ)​|z(ℓ−1)​(x)|+|ℓk(ℓ)​(x)|)+Δℓ\displaystyle\leq\max\_{k}\bigl(\alpha^{(\ell)}\_{k}\bigl|z^{(\ell-1)}(x)\bigr|+\bigl|\ell^{(\ell)}\_{k}(x)\bigr|\bigr)+\Delta\_{\ell} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤qℓ​|z(ℓ−1)​(x)|+maxk⁡|ℓk(ℓ)​(x)|+Δℓ.\displaystyle\leq q\_{\ell}\bigl|z^{(\ell-1)}(x)\bigr|+\max\_{k}\bigl|\ell^{(\ell)}\_{k}(x)\bigr|+\Delta\_{\ell}. |  |

Taking supx∈𝒳\sup\_{x\in\mathcal{X}} and using (B) and Δℓ≤Θℓ​log⁡Kℓ\Delta\_{\ell}\leq\Theta\_{\ell}\log K\_{\ell} gives

|  |  |  |
| --- | --- | --- |
|  | Aℓ≤qℓ​Aℓ−1+R​Sℓ+B¯ℓ+Θℓ​log⁡Kℓ.A\_{\ell}\leq q\_{\ell}A\_{\ell-1}+RS\_{\ell}+\bar{B}\_{\ell}+\Theta\_{\ell}\log K\_{\ell}. |  |

with A1≤R​S1+B¯1+Θ1​log⁡K1A\_{1}\;\leq\;RS\_{1}+\bar{B}\_{1}+\Theta\_{1}\log K\_{1}.

To find the analytical formula for the recursion, define cℓ=R​Sℓ+B¯ℓ+Θℓ​log⁡Kℓc\_{\ell}=RS\_{\ell}+\bar{B}\_{\ell}+\Theta\_{\ell}\log K\_{\ell} so that

|  |  |  |
| --- | --- | --- |
|  | A1≤c1,and Aℓ≤qℓ​Aℓ−1+cℓ(ℓ≥2).A\_{1}\leq c\_{1},\quad\text{and }\quad A\_{\ell}\leq q\_{\ell}A\_{\ell-1}+c\_{\ell}\quad(\ell\geq 2). |  |

It is easy to show by induction,

|  |  |  |
| --- | --- | --- |
|  | AL≤qL​AL−1+cL≤qL​∑j=1L−1cj​∏r=j+1L−1qr+cL=∑j=1L−1cj​∏r=j+1Lqr+cL,A\_{L}\leq q\_{L}A\_{L-1}+c\_{L}\leq q\_{L}\sum\_{j=1}^{L-1}c\_{j}\prod\_{r=j+1}^{L-1}q\_{r}+c\_{L}=\sum\_{j=1}^{L-1}c\_{j}\prod\_{r=j+1}^{L}q\_{r}+c\_{L}, |  |

|  |  |  |
| --- | --- | --- |
|  | AL≤∑j=1Lcj​∏r=j+1Lqr=∑j=1L(R​Sj+B¯j+Θj​log⁡Kj)​∏r=j+1Lqr.\ A\_{L}\leq\sum\_{j=1}^{L}c\_{j}\prod\_{r=j+1}^{L}q\_{r}=\sum\_{j=1}^{L}\bigl(RS\_{j}+\bar{B}\_{j}+\Theta\_{j}\log K\_{j}\bigr)\prod\_{r=j+1}^{L}q\_{r}.\ |  |

Finally,

|  |  |  |
| --- | --- | --- |
|  | supx∈𝒳|y​(x)|≤|cout|+supx∈𝒳|z(L)​(x)|≤C+AL,\sup\_{x\in\mathcal{X}}|y(x)|\;\leq\;|c\_{\mathrm{out}}|+\sup\_{x\in\mathcal{X}}\bigl|z^{(L)}(x)\bigr|\;\leq\;C+A\_{L}, |  |

|  |  |  |
| --- | --- | --- |
|  | supx∈𝒳|y​(x)|≤C+∑j=1L(R​Sj+B¯j+Θj​log⁡Kj)​∏r=j+1Lqr\;\sup\_{x\in\mathcal{X}}|y(x)|\;\leq\;C+\sum\_{j=1}^{L}\Bigl(RS\_{j}+\bar{B}\_{j}+\Theta\_{j}\log K\_{j}\Bigr)\prod\_{r=j+1}^{L}q\_{r}\; |  |

|  |  |  |
| --- | --- | --- |
|  | supx∈𝒳|y​(x)|≤Vn\sup\_{x\in\mathcal{X}}|y(x)|\;\leq\;V\_{n}\; |  |

which is the envelope depending only on box constants
(Sj,B¯j,q,Θj,Kj,C,R)(S\_{j},\,\bar{B}\_{j},\,q,\,\Theta\_{j},\,K\_{j},\,C,\,R).
Since the right-hand side does not depend on xx and ff, we get

|  |  |  |
| --- | --- | --- |
|  | supθ∈Θnsupx∈𝒳|yθ​(x)|=supf∈ℱn‖f‖∞≤Vn.\sup\_{\theta\in\Theta\_{n}}\ \sup\_{x\in\mathcal{X}}|y\_{\theta}(x)|\;=\;\sup\_{f\in\mathcal{F}\_{n}}\|f\|\_{\infty}\;\leq\;V\_{n}\;. |  |

∎

Let S​(u)=∑i=1meui/TS(u)=\sum\_{i=1}^{m}e^{u\_{i}/T}. For j=1,…,mj=1,\dots,m,

|  |  |  |
| --- | --- | --- |
|  | ∂∂ujLSET(u)=T⋅1S​(u)⋅∂S​(u)∂uj=T⋅1S​(u)⋅1Teuj/T=euj/TS​(u)=:pj(u).\frac{\partial}{\partial u\_{j}}\mathrm{LSE}\_{T}(u)=T\cdot\frac{1}{S(u)}\cdot\frac{\partial S(u)}{\partial u\_{j}}=T\cdot\frac{1}{S(u)}\cdot\frac{1}{T}e^{u\_{j}/T}=\frac{e^{u\_{j}/T}}{S(u)}=:p\_{j}(u). |  |

Thus ∇LSET​(u)=p​(u)=(p1​(u),…,pm​(u))\nabla\mathrm{LSE}\_{T}(u)=p(u)=(p\_{1}(u),\ldots,p\_{m}(u)), where each pj​(u)∈(0,1)p\_{j}(u)\in(0,1) and
∑j=1mpj​(u)=1\sum\_{j=1}^{m}p\_{j}(u)=1; i.e., p​(u)p(u) is a probability vector (the softmax of u/Tu/T).

For any norm ∥⋅∥\|\cdot\| and dual ∥⋅∥∗\|\cdot\|\_{\*}, the mean value inequality gives

|  |  |  |
| --- | --- | --- |
|  | |LSET​(u)−LSET​(v)|≤supξ∈[u,v]‖∇LSET​(ξ)‖∗​‖u−v‖,\bigl|\mathrm{LSE}\_{T}(u)-\mathrm{LSE}\_{T}(v)\bigr|\leq\sup\_{\xi\in[u,v]}\bigl\|\nabla\mathrm{LSE}\_{T}(\xi)\bigr\|\_{\*}\,\|u-v\|, |  |

so the Lipschitz constant is supξ‖p​(ξ)‖∗\sup\_{\xi}\|p(\xi)\|\_{\*}.

Now consider the cases

if ∥⋅∥=∥⋅∥∞\|\cdot\|=\|\cdot\|\_{\infty}: 
∥⋅∥∗=∥⋅∥1\|\cdot\|\_{\*}=\|\cdot\|\_{1} and ‖p​(ξ)‖1=∑jpj​(ξ)=1\|p(\xi)\|\_{1}=\sum\_{j}p\_{j}(\xi)=1.

if ∥⋅∥=∥⋅∥2\|\cdot\|=\|\cdot\|\_{2}: 
∥⋅∥∗=∥⋅∥2\|\cdot\|\_{\*}=\|\cdot\|\_{2} and ‖p​(ξ)‖2≤‖p​(ξ)‖1=1\|p(\xi)\|\_{2}\leq\|p(\xi)\|\_{1}=1.

Therefore, the Lipschitz constant is 11 in both cases.
∎

To prove that

|  |  |  |
| --- | --- | --- |
|  | supf∈ℱn|Qn​(f)−Q¯n​(f)|→p∗ 0a​s​n→∞.\sup\_{f\in\mathcal{F}\_{n}}\bigl|\,Q\_{n}(f)-\overline{Q}\_{n}(f)\,\bigr|\;\xrightarrow{\,p^{\*}\,}\;0\qquad as\ n\to\infty. |  |

under a given growth condition of ℱn\mathcal{F}\_{n}, [shen2023asymptotic] shows that it suffices to have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ξ\displaystyle\mathbb{E}\_{\xi} | [supf∈ℱn|1n​∑i=1nξi​ϵi​(f​(xi)−f0​(xi))|]\displaystyle\!\left[\sup\_{f\in\mathcal{F}\_{n}}\left|\frac{1}{n}\sum\_{i=1}^{n}\xi\_{i}\epsilon\_{i}\bigl(f(x\_{i})-f\_{0}(x\_{i})\bigr)\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼ξ​[|1n​∑i=1nξi​ϵi​(fn∗​(xi)−f0​(xi))|]+K​∫02​Vnlog𝒩(η2​σ2+1,ℱn,∥⋅∥∞)n​𝑑η.\displaystyle\leq\mathbb{E}\_{\xi}\!\left[\left|\frac{1}{n}\sum\_{i=1}^{n}\xi\_{i}\epsilon\_{i}\bigl(f\_{n}^{\ast}(x\_{i})-f\_{0}(x\_{i})\bigr)\right|\right]+K\!\int\_{0}^{2V\_{n}}\!\sqrt{\frac{\log\mathcal{N}\!\left(\frac{\eta}{2\sqrt{\sigma^{2}}+1},\ \mathcal{F}\_{n},\ \|\cdot\|\_{\infty}\right)}{n}}\,d\eta. |  |

Regarding the first term, we apply the Universal Approximation theorem ([3.7](https://arxiv.org/html/2512.11731v1#S3.Thmassumption7 "Theorem 3.7 (Uniform approximation on a compact convex set by an 𝐿-layer Deep-LSE network). ‣ 3.3 Universal Approximation ‣ 3 Deep Log-Sum-Exp Neural Network ‣ Transfer Learning (Il)liquidity")) and choose fn∗=πn​f0f\_{n}^{\*}=\pi\_{n}f\_{0}. This means that supx∈𝒳|fn∗​(x)−f0​(x)|→0\sup\_{x\in\mathcal{X}}|f\_{n}^{\*}(x)-f\_{0}(x)|\to 0 as n→∞n\to\infty. Therefore, the first term is smaller than any ζ>0\zeta>0, for a sufficiently large nn.

Regarding the second term, we apply Theorem 14.5 of [anthony2009neural]

|  |  |  |
| --- | --- | --- |
|  | 𝒩∞​(ϵ,ℱ,m)≤(4​e​m​b​W​(L​V)ℓϵ​(L​V−1))W,\mathcal{N}\_{\infty}(\epsilon,\mathcal{F},m)\;\leq\;\left(\frac{4\,e\,m\,b\,W\,(LV)^{\ell}}{\epsilon\,(LV-1)}\right)^{W}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒩(12​σ2+1η,ℱn,∥⋅∥∞)\displaystyle\mathcal{N}\!\left(\frac{1}{2\sqrt{\sigma^{2}+1}}\,\eta,\ \mathcal{F}\_{n},\ \|\cdot\|\_{\infty}\right) | ≤((8​σ2+1)​e​[b]​[W]​(Vn)Lη​(Vn−1))W,\displaystyle\leq\left(\frac{(8\sqrt{\sigma^{2}+1})\,e\,[\,b\,][\,W\,]\left(V\_{n}\right)^{L}}{\eta\left(V\_{n}-1\right)}\right)^{\,W}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤((8​σ2+1)​e​[Vn]​[W]​(Vn)Lη​(Vn−1))W,\displaystyle\leq\ \left(\frac{(8\sqrt{\sigma^{2}+1})\,e\,[\,V\_{n}\,][\,W\,]\left(V\_{n}\right)^{L}}{\eta\left(V\_{n}-1\right)}\right)^{\,W}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =((8​σ2+1)​e​[W]​(Vn)L+1η​(Vn−1))W,\displaystyle=\ \left(\frac{(8\sqrt{\sigma^{2}+1})\,e\,[\,W\,]\left(V\_{n}\right)^{L+1}}{\eta\left(V\_{n}-1\right)}\right)^{\,W}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:B~W,d,Vnη−W,\displaystyle=:\ \tilde{B}\_{W,d,V\_{n}}\,\eta^{-W}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | B~W,d,Vn=((8​σ2+1)​e​[W]​(Vn)L+1Vn−1)W.\tilde{B}\_{W,d,V\_{n}}=\left(\frac{\bigl(8\sqrt{\sigma^{2}+1}\bigr)\,e[\,W\,]\,(V\_{n})^{L+1}}{V\_{n}-1}\right)^{\,W}. |  |

Now, let

|  |  |  |
| --- | --- | --- |
|  | BW,d,Vn=log⁡B~W,d,Vn−W.B\_{W,d,V\_{n}}=\log\tilde{B}\_{W,d,V\_{n}}-W. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | BW,d,Vn\displaystyle B\_{W,d,V\_{n}} | =W​(log⁡(8​σ2+1)​e​[W]​(Vn)L+1Vn−1−1),\displaystyle=W\left(\log\frac{\bigl(8\sqrt{\sigma^{2}+1}\bigr)\,e[\,W\,]\,(V\_{n})^{L+1}}{V\_{n}-1}-1\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =W​(log⁡W​(Vn)L+1Vn−1+log⁡(8​σ2+1)),\displaystyle=W\left(\log\frac{W\,(V\_{n})^{L+1}}{V\_{n}-1}+\log(8\sqrt{\sigma^{2}+1})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​W​log⁡W​(Vn)L+1Vn−1,\displaystyle\leq 2W\,\log\frac{W\,(V\_{n})^{L+1}}{V\_{n}-1}, |  |

that holds because VnL+1−Vn+1≥0V\_{n}^{L+1}-V\_{n}+1\geq 0 for all VnV\_{n} and L+1L+1 being even, so that

|  |  |  |
| --- | --- | --- |
|  | log⁡(W​VnL+1Vn−1)≥log⁡((2​σ2+1)​(Vn−1)Vn−1)=log⁡(2​σ2+1).\log\!\left(\frac{WV\_{n}^{L+1}}{V\_{n}-1}\right)\;\geq\;\log\!\left(\frac{(2\sqrt{\sigma^{2}+1})(V\_{n}-1)}{V\_{n}-1}\right)=\log\!\bigl(2\sqrt{\sigma^{2}+1}\bigr). |  |

Since VL+1−e​V+e≥0V^{L+1}-eV+e\geq 0 for all VV, we have VL+1V−1≥e\dfrac{V^{L+1}}{V-1}\geq e, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(W​VL+1V−1)\displaystyle\log\!\left(W\frac{V^{L+1}}{V-1}\right) | ≥log⁡(VL+1V−1)≥log⁡(e​(V−1)V−1)=1.\displaystyle\geq\log\!\left(\frac{V^{L+1}}{V-1}\right)\geq\log\!\left(\frac{e(V-1)}{V-1}\right)=1. |  |

But we also have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | BW,d,V\displaystyle B\_{W,d,V} | =log⁡B~W,d,V−W,\displaystyle=\log\tilde{B}\_{W,d,V}-W, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log((8​σ2+1)​e​W​(Vn)L+1Vn−1)W−W,\displaystyle=\log\left(\frac{\bigl(8\sqrt{\sigma^{2}+1}\bigr)\,eW(V\_{n})^{L+1}}{V\_{n}-1}\right)^{\,W}-W, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =W​[log⁡((8​σ2+1)​e​W​VL+1V−1)−1],\displaystyle=W\!\left[\log\!\left(\bigl(8\sqrt{\sigma^{2}+1}\bigr)e\,W\frac{V^{L+1}}{V-1}\right)-1\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =W​log⁡((8​σ2+1)​W​VL+1V−1),\displaystyle=W\,\log\!\left(\bigl(8\sqrt{\sigma^{2}+1}\bigr)W\frac{V^{L+1}}{V-1}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =W∗(ℝ>1),\displaystyle=W\*(\mathbb{R}>1), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥W.\displaystyle\geq W. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | H(12​σ2+1η,ℱn,∥⋅∥∞)\displaystyle H\!\left(\frac{1}{2\sqrt{\sigma^{2}+1}}\,\eta,\ \mathcal{F}\_{n},\ \|\cdot\|\_{\infty}\right) | =log𝒩(12​σ2+1η,ℱn,∥⋅∥∞),\displaystyle=\log\mathcal{N}\!\left(\frac{1}{2\sqrt{\sigma^{2}+1}}\,\eta,\ \mathcal{F}\_{n},\ \|\cdot\|\_{\infty}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤BW,d,Vn​(1+1η)since ​(B≥W).\displaystyle\leq B\_{W,d,V\_{n}}\!\left(1+\frac{1}{\eta}\right)\ \ \text{since }(B\geq W). |  |

As a result, for sufficiently large nn we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫02​VnH1/2(12​σ2+1η,ℱn,∥⋅∥∞)dη\displaystyle\int\_{0}^{2V\_{n}}H^{1/2}\!\left(\frac{1}{2\sqrt{\sigma^{2}}+1}\,\eta,\ \mathcal{F}\_{n},\ \|\cdot\|\_{\infty}\right)\,d\eta | ≤4​2​BW,d,Vn1/2​Vn.\displaystyle\leq 4\sqrt{2}\,B\_{W,d,V\_{n}}^{1/2}\,V\_{n}. |  |

Recall that

|  |  |  |
| --- | --- | --- |
|  | BW,d,Vn=log⁡B~W,d,Vn−W=W​log⁡((8​σ2+1)​W​VnL+1Vn−1).B\_{W,d,V\_{n}}=\log\tilde{B}\_{W,d,V\_{n}}-W=W\log\!\left((8\sqrt{\sigma^{2}+1})\,W\,\frac{V\_{n}^{L+1}}{V\_{n}-1}\right). |  |

Then the bound entropy integral becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫02​VnH(η2​σ2+1,ℱn,∥⋅∥∞)n​𝑑η\displaystyle\int\_{0}^{2V\_{n}}\!\sqrt{\frac{H\!\left(\frac{\eta}{2\sqrt{\sigma^{2}}+1},\,\mathcal{F}\_{n},\,\|\cdot\|\_{\infty}\right)}{n}}\;d\eta | ≤4​2​Vnn​BW,d,Vn,\displaystyle\leq 4\sqrt{2}\,\frac{V\_{n}}{\sqrt{n}}\;\sqrt{B\_{W,d,V\_{n}}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4​2​Vnn​W​[log⁡(VnL+1Vn−1)+log⁡((8​σ2+1)​W)].\displaystyle\leq 4\sqrt{2}\,\frac{V\_{n}}{\sqrt{n}}\;\sqrt{\,W\Bigg[\log\!\left(\frac{V\_{n}^{L+1}}{V\_{n}-1}\right)+\log\!\big((8\sqrt{\sigma^{2}+1})W\big)\Bigg]}. |  |

As Vn→∞V\_{n}\to\infty,

|  |  |  |
| --- | --- | --- |
|  | log⁡(VnL+1Vn−1)=log⁡VnL+o​(1),\log\!\left(\frac{V\_{n}^{L+1}}{V\_{n}-1}\right)=\log V\_{n}^{L}+o(1), |  |

so

|  |  |  |
| --- | --- | --- |
|  | BW,d,Vn≲W​[log⁡VnL+log⁡W+log⁡(8​σ2+1)+o​(1)]≤ 2​W​log⁡(VnL​W),\sqrt{B\_{W,d,V\_{n}}}\;\lesssim\;\sqrt{\,W\,[\log V\_{n}^{L}+\log W+\log(8\sqrt{\sigma^{2}+1})+o(1)]\,}\;\leq\;\sqrt{\,2W\,\log(V\_{n}^{L}W)\,}, |  |

because as log⁡VnL​W→∞, 8​σ2+1≤log⁡VnL​W\log V\_{n}^{L}W\to\infty,\ 8\sqrt{\sigma^{2}+1}\leq\log V\_{n}^{L}W.
Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫02​VnH(η2​σ2+1,ℱn,∥⋅∥∞)n​𝑑η\displaystyle\int\_{0}^{2V\_{n}}\!\sqrt{\frac{H\!\left(\frac{\eta}{2\sqrt{\sigma^{2}+1}},\,\mathcal{F}\_{n},\,\|\cdot\|\_{\infty}\right)}{n}}\;d\eta | ≤4​2​Vnn​ 2​W​log⁡(VnL​W),\displaystyle\leq 4\sqrt{2}\,\frac{V\_{n}}{\sqrt{n}}\;\sqrt{\,2W\,\log(V\_{n}^{L}W)\,}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =8​W​Vn2​log⁡(VnL​W)n.\displaystyle=8\,\sqrt{\frac{W\,V\_{n}^{2}\,\log(V\_{n}^{L}W)}{n}}\;. |  |

Under the assumptions W​Vn2​log⁡(VnL​W)=o​(n)a​s​n→∞,WV\_{n}^{2}\,\log\!\big(V\_{n}^{L}W\big)=o(n)\quad as\ n\to\infty, we have that

|  |  |  |
| --- | --- | --- |
|  | W​Vn2​log⁡(VnL​W)n<ζ8.\sqrt{\frac{W\,V\_{n}^{2}\,\log\!\big(V\_{n}^{L}W\big)}{n}}<\frac{\zeta}{8}\,. |  |

Finally, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ξ​[supf∈ℱn|1n​∑i=1nξi​ϵi​(f​(xi)−f0​(xi))|]\displaystyle\mathbb{E}\_{\xi}\!\Bigg[\sup\_{f\in\mathcal{F}\_{n}}\Bigl|\frac{1}{n}\sum\_{i=1}^{n}\xi\_{i}\epsilon\_{i}\bigl(f(x\_{i})-f\_{0}(x\_{i})\bigr)\Bigr|\Bigg] | ≤σ2+1​‖πn​f0−f0‖∞+4​2​K​Vnn​ 2​W​log⁡(VnL​W),\displaystyle\leq\sqrt{\sigma^{2}+1}\,\bigl\|\pi\_{n}f\_{0}-f\_{0}\bigr\|\_{\infty}+4\sqrt{2}K\,\frac{V\_{n}}{\sqrt{n}}\;\sqrt{\,2W\,\log(V\_{n}^{L}W)\,}, |  |

which goes to 0 as n→∞n\to\infty. This means that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼∗\displaystyle\mathbb{E}^{\*} | [supf∈ℱn|1n​∑i=1nϵi​(f​(xi)−f0​(xi))|]→n→∞0,\displaystyle\!\Bigg[\sup\_{f\in\mathcal{F}\_{n}}\Bigl|\frac{1}{n}\sum\_{i=1}^{n}\epsilon\_{i}\bigl(f(x\_{i})-f\_{0}(x\_{i})\bigr)\Bigr|\Bigg]\xrightarrow[n\to\infty]{}0, |  |

completing the proof.

∎

## Appendix C Additional Simulations

### C.1 Kou-Heston Stochastic Volatility model

The [kou2002jump] Stochastic Volatility model has the volatility evolution

|  |  |  |
| --- | --- | --- |
|  | d​Vt=κ​(θ−Vt)​d​t+σv​Vt​d​Wt(2)dV\_{t}=\kappa\left(\theta-V\_{t}\right)dt+\sigma\_{v}\sqrt{V\_{t}}dW\_{t}^{(2)} |  |

that is simulated using Euler-Maruyama. The asset price evolution is

|  |  |  |
| --- | --- | --- |
|  | d​St=St​[(r−q−λ​κJ)​d​t+Vt​d​Wt(1)+d​Jt]dS\_{t}=S\_{t}\left[\left(r-q-\lambda\kappa\_{J}\right)dt+\sqrt{V\_{t}}dW\_{t}^{(1)}+dJ\_{t}\right] |  |

d​JtdJ\_{t} is the jump component from a compound Poisson process using intensity λj\lambda\_{j} and double-exponential jump sizes

|  |  |  |
| --- | --- | --- |
|  | Y∼{Exp⁡(1/η1), with prob ​pup −Exp⁡(1/η2), with prob ​1−pup Y\sim\begin{cases}\operatorname{Exp}\left(1/\eta\_{1}\right),&\text{ with prob }p\_{\text{up }}\\ -\operatorname{Exp}\left(1/\eta\_{2}\right),&\text{ with prob }1-p\_{\text{up }}\end{cases} |  |

Two correlated Wiener processes using Cholesky

|  |  |  |
| --- | --- | --- |
|  | Corr⁡(d​Wt(1),d​Wt(2))=ρ\operatorname{Corr}\left(dW\_{t}^{(1)},dW\_{t}^{(2)}\right)=\rho |  |

|  |  |  |
| --- | --- | --- |
|  | d​Jt=∑i=1d​Nt(eYi−1),Nt∼Poisson⁡(λ​t),\mathrm{d}J\_{t}=\sum\_{i=1}^{\mathrm{d}N\_{t}}\!\Bigl(e^{Y\_{i}}-1\Bigr),\qquad N\_{t}\sim\operatorname{Poisson}(\lambda t), |  |

|  |  |  |
| --- | --- | --- |
|  | Yi∼{Exp​(1/η1),with probability ​pup,−Exp​(1/η2),with probability ​1−pup.Y\_{i}\sim\begin{cases}\mathrm{Exp}(1/\eta\_{1}),&\text{with probability }p\_{\text{up}},\\[4.0pt] -\mathrm{Exp}(1/\eta\_{2}),&\text{with probability }1-p\_{\text{up}}.\end{cases} |  |

|  |  |  |
| --- | --- | --- |
|  | κJ=𝔼​[eY−1]=pup​η1η1−1+(1−pup)​η2η2+1−1,η1>1,η2>−1.\kappa\_{J}=\mathbb{E}\!\bigl[e^{Y}-1\bigr]=p\_{\text{up}}\dfrac{\eta\_{1}}{\eta\_{1}-1}+(1-p\_{\text{up}})\dfrac{\eta\_{2}}{\eta\_{2}+1}-1,\quad\eta\_{1}>1,\;\eta\_{2}>-1. |  |

For risk-neutral simulation, one can use

|  |  |  |
| --- | --- | --- |
|  | St+Δ​t=St⋅exp⁡[(r−q−λ​(pup​η1η1−1+(1−pup)​η2η2+1−1)−12​Vt)​Δ​t+Vt​Δ​Wt(1)+Jt]S\_{t+\Delta t}=S\_{t}\cdot\exp\left[\left(r-q-\lambda\left(\frac{p\_{\mathrm{up}}\eta\_{1}}{\eta\_{1}-1}+\frac{\left(1-p\_{\mathrm{up}}\right)\eta\_{2}}{\eta\_{2}+1}-1\right)-\frac{1}{2}V\_{t}\right)\Delta t+\sqrt{V\_{t}}\Delta W\_{t}^{(1)}+J\_{t}\right] |  |

In Table [4](https://arxiv.org/html/2512.11731v1#A3.T4 "Table 4 ‣ C.1 Kou-Heston Stochastic Volatility model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") we report the parameters we use for the simulation. To construct the target implied volatility curve, we assume it is obtained by translating the source curve. In particular, we shift implied volatilities downward by 10% (y-axis) and increase strikes by 20​$20\mathdollar (x-axis).

| S0S\_{0} | rr | qq | v0v\_{0} | κ\kappa | θ\theta | σ\sigma | ρ\rho | λ\lambda | pupp\_{\text{up}} | η1\eta\_{1} | η2\eta\_{2} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 0.05 | 0.00 | 0.04 | 2.0 | 0.04 | 0.8 | -0.5 | 0.12 | 0.35 | 8.0 | 10.0 |

Table 4: Simulated parameters for Kou-Heston model.

We study two different situations of severe market illiquidity by randomly selecting three in-the-money call option quotes in Scenario 1 and three out-of-the-money call option quotes in Scenario 2. We emphasize that these three call option quotes constitute the only information on the terminal RND available to the models. In Fig. [10](https://arxiv.org/html/2512.11731v1#A3.F10.fig3 "Figure 10 ‣ C.1 Kou-Heston Stochastic Volatility model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity"), we report Scenario 1, which consists of three illiquid observations of in-the-money (ITM) options.

![Refer to caption](_setup_kou_heston.png)

![Refer to caption](_train_kou_heston.png)

Figure 10: Scenario 1 - On the left panel, the orange dots are the ITM strikes selected on the target illiquid implied volatility curve (blue solid line), and the orange solid line is the liquid source (proxy) implied volatility curve. On the right panel, the interpolation of the illiquid implied volatility curve of the Deep-LSE model (green solid line) and quadratic splines (red solid line).

We observe in Fig. [11](https://arxiv.org/html/2512.11731v1#A3.F11 "Figure 11 ‣ C.1 Kou-Heston Stochastic Volatility model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") the estimates of Deep-LSE and quadratic splines compared to the ground truth illiquid RND. It emerges that the Deep-LSE accurately recovers the illiquid RND.

![Refer to caption](_final_kou_heston.png)


Figure 11: Scenario 1 - Illiquid RND recovery of Deep-LSE (orange curve) and quadratic splines (green curve) in comparison with the illiquid target ground truth simulated RND (blue curve).

We also test the Deep-LSE model on out-of-the-money call options and illiquid strikes (Scenario 2), and Fig. [12](https://arxiv.org/html/2512.11731v1#A3.F12.fig3 "Figure 12 ‣ C.1 Kou-Heston Stochastic Volatility model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") illustrates this case.

![Refer to caption](iv_setup_case2_right.png)

![Refer to caption](fit_case2_right.png)

Figure 12: Scenario 2 - On the left panel, the orange dots are the OTM strikes selected on the target illiquid implied volatility curve (blue solid line), and the orange solid line is the liquid source (proxy) implied volatility curve. On the right panel, the interpolation of the illiquid implied volatility curve of the Deep-LSE model (green solid line) and quadratic splines (red solid line).

![Refer to caption](final_rnd_case2_right.png)


Figure 13: Scenario 2 - Illiquid RND recovery of Deep-LSE (orange curve) and quadratic splines (green curve) in comparison with the illiquid target ground truth simulated RND (blue curve).

In Fig. [13](https://arxiv.org/html/2512.11731v1#A3.F13 "Figure 13 ‣ C.1 Kou-Heston Stochastic Volatility model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity"), we observe that, also in Scenario 2, the Deep-LSE model recovers the illiquid RND better with respect to the quadratic splines.

### C.2 Andersen-Benzoni-Lund Multifactor Model

The [andersen2002empirical] model follows

|  |  |  |
| --- | --- | --- |
|  | d​St=St​[(μ−12​∑i=1nVt(i))​d​t+Vt​d​Zt+d​Jt]dS\_{t}=S\_{t}\left[\left(\mu-\frac{1}{2}\sum\_{i=1}^{n}V\_{t}^{(i)}\right)dt+\sqrt{V\_{t}}dZ\_{t}+dJ\_{t}\right] |  |

Where Vt=∑i=1nVt(i)V\_{t}=\sum\_{i=1}^{n}V\_{t}^{(i)}, d​ZtdZ\_{t} is a Brownian motion correlated with the volatility factors, and d​Jt∼∑k=1d​NtYkdJ\_{t}\sim\sum\_{k=1}^{dN\_{t}}Y\_{k}, where d​Nt∼Poisson⁡(λj​d​t)dN\_{t}\sim\operatorname{Poisson}\left(\lambda\_{j}dt\right), and Yk∼𝒩​(μj,σj2)Y\_{k}\sim\mathcal{N}\left(\mu\_{j},\sigma\_{j}^{2}\right) is the jump size. Each volatility factor Vt(i)V\_{t}^{(i)} follows a square-root process)

|  |  |  |
| --- | --- | --- |
|  | d​Vt(i)=κi​(θi−Vt(i))​d​t+σi​Vt(i)​d​Wt(i)dV\_{t}^{(i)}=\kappa\_{i}\left(\theta\_{i}-V\_{t}^{(i)}\right)dt+\sigma\_{i}\sqrt{V\_{t}^{(i)}}dW\_{t}^{(i)} |  |

Where d​Wt(i)dW\_{t}^{(i)} are independent Brownian motions (correlated with d​ZtdZ\_{t} ).
The correlation between d​ZtdZ\_{t} and d​Wt(i)dW\_{t}^{(i)} is handled via

|  |  |  |
| --- | --- | --- |
|  | d​Zt=∑i=1nρi​d​Wt(i)+1−∑i=1nρi2⋅d​Wt(0)dZ\_{t}=\sum\_{i=1}^{n}\rho\_{i}dW\_{t}^{(i)}+\sqrt{1-\sum\_{i=1}^{n}\rho\_{i}^{2}}\cdot dW\_{t}^{(0)} |  |

To simulate under the risk-neutral probability measure, one can use

|  |  |  |
| --- | --- | --- |
|  | μℚ=r−λj​(eμj+12​σj2−1).\mu\_{\mathbb{Q}}\;=\;r\;-\;\lambda\_{j}\!\left(e^{\,\mu\_{j}\;+\;\frac{1}{2}\,\sigma\_{j}^{2}}-1\right). |  |

In Table [5](https://arxiv.org/html/2512.11731v1#A3.T5 "Table 5 ‣ C.2 Andersen-Benzoni-Lund Multifactor Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") we report the parameters we use for the simulation. To construct the target implied volatility curve, we define two different set of parameters and obtain two distinct implied volatility curves. Regarding the first, we assume it is the liquid proxy, whereas the second is the illiquid target.

| Set | S0S\_{0} | rr | ρ\rho | κ1\kappa\_{1} | θ1\theta\_{1} | σ1\sigma\_{1} | v0,1v\_{0,1} | κ2\kappa\_{2} | θ2\theta\_{2} | σ2\sigma\_{2} | v0,2v\_{0,2} | κ3\kappa\_{3} | θ3\theta\_{3} | σ3\sigma\_{3} | v0,3v\_{0,3} | λj\lambda\_{j} | μj\mu\_{j} | σj\sigma\_{j} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 100 | 0.05 | [−0.3, 0.0, 0.3][-0.3,\ 0.0,\ 0.3] | 3.0 | 0.02 | 0.2 | 0.02 | 1.5 | 0.04 | 0.3 | 0.04 | 0.5 | 0.06 | 0.4 | 0.06 | 0.20 | 0.00 | 0.55 |
| 2 | 100 | 0.05 | [−0.3, 0.0, 0.3][-0.3,\ 0.0,\ 0.3] | 3.0 | 0.02 | 0.2 | 0.02 | 1.5 | 0.04 | 0.3 | 0.04 | 0.5 | 0.06 | 0.4 | 0.06 | 0.25 | 0.18 | 0.60 |

Table 5: Simulated parameters for Andersen-Benzoni-Lund model. Set 1 for the liquid proxy and set 2 for the illiquid target.

We examine two instances of severe market illiquidity by randomly selecting three in-the-money call option quotes for Scenario 1 and three out-of-the-money call option quotes for Scenario 2. We emphasize that these three option quotes constitute the only information on the terminal RND available to the models. In Fig. [14](https://arxiv.org/html/2512.11731v1#A3.F14.fig3 "Figure 14 ‣ C.2 Andersen-Benzoni-Lund Multifactor Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity"), we represent the first case under consideration (Scenario 1), which consists of three illiquid observations of in-the-money (ITM) call options.

![Refer to caption](iv_setup2_abl.png)

![Refer to caption](fit_abl.png)

Figure 14: Scenario 1 - On the left panel, the orange dots are the ITM strikes selected on the target illiquid implied volatility curve (blue solid line), and the orange solid line is the liquid source (proxy) implied volatility curve. On the right panel, the interpolation of the illiquid implied volatility curve of the Deep-LSE model (green solid line) and quadratic splines (red solid line).

We observe in Fig. [15](https://arxiv.org/html/2512.11731v1#A3.F15 "Figure 15 ‣ C.2 Andersen-Benzoni-Lund Multifactor Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") the estimates of Deep-LSE and quadratic splines compared to the ground truth illiquid RND. It emerges that the Deep-LSE accurately recovers the illiquid RND, while the estimate of the quadratic spline is erratic and does not approximate the target RND.

![Refer to caption](rnd_final_abl.png)


Figure 15: Scenario 1 - Illiquid RND recovery of Deep-LSE (orange curve) and quadratic splines (green curve) in comparison with the illiquid target ground truth simulated RND (blue curve).

We also test the Deep-LSE model on out-of-the-money call options and illiquid strikes (Scenario 2), and Fig. [16](https://arxiv.org/html/2512.11731v1#A3.F16.fig3 "Figure 16 ‣ C.2 Andersen-Benzoni-Lund Multifactor Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") illustrates this case.

![Refer to caption](iv_setup2_case2_abl.png)

![Refer to caption](iv_fit_abl2.png)

Figure 16: Scenario 2 - On the left panel, the orange dots are the OTM strikes selected on the target illiquid implied volatility curve (blue solid line), and the orange solid line is the liquid source (proxy) implied volatility curve. On the right panel, the interpolation of the illiquid implied volatility curve of the Deep-LSE model (green solid line) and quadratic splines (red solid line).

In Fig. [17](https://arxiv.org/html/2512.11731v1#A3.F17 "Figure 17 ‣ C.2 Andersen-Benzoni-Lund Multifactor Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity"), we observe that also in Scenario 2, the Deep-LSE model is able to recover the illiquid RND, while quadratic splines yield an inaccurate estimate.

![Refer to caption](final_rnd_abl2.png)


Figure 17: Scenario 2 - Illiquid RND recovery of Deep-LSE (orange curve) and quadratic splines (green curve) in comparison with the illiquid target ground truth simulated RND (blue curve).

### C.3 Three-Factor Double Exponential Stochastic Volatility Model

The three-factor double exponential stochastic volatility model of [andersen2015risk] models the forward price FtF\_{t} in the risk-neutral measure as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​FtFt−\displaystyle\frac{dF\_{t}}{F\_{t-}} | =V1,t​d​W1,tℚ+V2,t​d​W2,tℚ+η​Ut​d​W3,tℚ+∫ℝ2(ex−1)​μ~ℚ​(d​t,d​x,d​y)\displaystyle=\sqrt{V\_{1,t}}dW\_{1,t}^{\mathbb{Q}}+\sqrt{V\_{2,t}}dW\_{2,t}^{\mathbb{Q}}+\eta\sqrt{U\_{t}}dW\_{3,t}^{\mathbb{Q}}+\int\_{\mathbb{R}^{2}}\left(e^{x}-1\right)\widetilde{\mu}^{\mathbb{Q}}(dt,dx,dy) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​V1,t\displaystyle dV\_{1,t} | =κ1​(v¯1−V1,t)​d​t+σ1​V1,t​d​B1,tℚ+μv​∫ℝ2x2​1{x<0}​μ​(d​t,d​x,d​y)\displaystyle=\kappa\_{1}\left(\bar{v}\_{1}-V\_{1,t}\right)dt+\sigma\_{1}\sqrt{V\_{1,t}}dB\_{1,t}^{\mathbb{Q}}+\mu\_{v}\int\_{\mathbb{R}^{2}}x^{2}1\_{\{x<0\}}\mu(dt,dx,dy) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​V2,t\displaystyle dV\_{2,t} | =κ2​(v¯2−V2,t)​d​t+σ2​V2,t​d​B2,tℚ\displaystyle=\kappa\_{2}\left(\bar{v}\_{2}-V\_{2,t}\right)dt+\sigma\_{2}\sqrt{V\_{2,t}}dB\_{2,t}^{\mathbb{Q}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ut\displaystyle dU\_{t} | =−κu​Ut​d​t+μu​∫ℝ2[(1−ρu)​x2​1{x<0}+ρu​y2]​μ​(d​t,d​x,d​y)\displaystyle=-\kappa\_{u}U\_{t}dt+\mu\_{u}\int\_{\mathbb{R}^{2}}\left[\left(1-\rho\_{u}\right)x^{2}1\_{\{x<0\}}+\rho\_{u}y^{2}\right]\mu(dt,dx,dy) |  |

where (W1,tℚ,W2,tℚ,W3,tℚ,B1,tℚ,B2,tℚ)\left(W\_{1,t}^{\mathbb{Q}},W\_{2,t}^{\mathbb{Q}},W\_{3,t}^{\mathbb{Q}},B\_{1,t}^{\mathbb{Q}},B\_{2,t}^{\mathbb{Q}}\right) is a Brownian motion in five dimension with corr⁡(W1,tℚ,B1,tℚ)=ρ1\operatorname{corr}\left(W\_{1,t}^{\mathbb{Q}},B\_{1,t}^{\mathbb{Q}}\right)=\rho\_{1}, corr⁡(W2,tℚ,B2,tℚ)=ρ2\operatorname{corr}\left(W\_{2,t}^{\mathbb{Q}},B\_{2,t}^{\mathbb{Q}}\right)=\rho\_{2}, while the other Brownian motions are independent.

Jumps in the forward price FF and in the state vector (V1,V2,U)(V\_{1},V\_{2},U) are modeled by an
integer-valued counting measure μ\mu. Under the risk-neutral measure ℚ\mathbb{Q},
the jump intensity is

|  |  |  |
| --- | --- | --- |
|  | d​t⊗vtℚ​(d​x,d​y),dt\otimes v\_{t}^{\mathbb{Q}}(dx,dy), |  |

and the martingale jump measure is

|  |  |  |
| --- | --- | --- |
|  | μ~ℚ​(d​t,d​x,d​y)=μ​(d​t,d​x,d​y)−d​t​vtℚ​(d​x,d​y).\widetilde{\mu}^{\mathbb{Q}}(dt,dx,dy)=\mu(dt,dx,dy)-dt\,v\_{t}^{\mathbb{Q}}(dx,dy). |  |

The jump structure uses two components. The variable xx captures co-jumps in
FtF\_{t}, V1,tV\_{1,t} and UtU\_{t} (if ρu<1\rho\_{u}<1), while yy represents shocks
specific to UtU\_{t}, and may also affect return volatility when η>0\eta>0. The density is

|  |  |  |
| --- | --- | --- |
|  | vtℚ​(d​x,d​y)d​x​d​y={c−​(t)​𝟏{x<0}​λ−​e−λ−​|x|+c+​(t)​𝟏{x>0}​λ+​e−λ+​x,if ​y=0,c−​(t)​λ−​e−λ−​|y|,if ​x=0​ and ​y<0.\frac{v\_{t}^{\mathbb{Q}}(dx,dy)}{dx\,dy}=\begin{cases}c^{-}(t)\mathbf{1}\_{\{x<0\}}\lambda\_{-}e^{-\lambda\_{-}|x|}+c^{+}(t)\mathbf{1}\_{\{x>0\}}\lambda\_{+}e^{-\lambda\_{+}x},&\text{if }y=0,\\[6.0pt] c^{-}(t)\lambda\_{-}e^{-\lambda\_{-}|y|},&\text{if }x=0\text{ and }y<0.\end{cases} |  |

Thus, x≠0x\neq 0 (with y=0y=0) implies joint price–volatility jumps, whereas x=0x=0 and y<0y<0 yields independent jumps in UU. Positive jumps in UU are either independent of V1V\_{1} when ρu=1\rho\_{u}=1, or proportional to the jumps in V1V\_{1} when ρu=0\rho\_{u}=0. Price jumps follow a double-exponential law with tail parameters λ−\lambda\_{-} and λ+\lambda\_{+} for negative and positive jumps. For parsimony, the independent UU shocks share the same distribution as negative price jumps. Time-varying jump intensities are affine in the state

|  |  |  |  |
| --- | --- | --- | --- |
|  | c−​(t)\displaystyle c^{-}(t) | =c0−+c1−​V1,t,−+c2−​V2,t,−+cu−​Ut,−,\displaystyle=c\_{0}^{-}+c\_{1}^{-}V\_{1,t,-}+c\_{2}^{-}V\_{2,t,-}+c\_{u}^{-}U\_{t,-}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c+​(t)\displaystyle c^{+}(t) | =c0++c1+​V1,t,−+c2+​V2,t,−+cu+​Ut,−.\displaystyle=c\_{0}^{+}+c\_{1}^{+}V\_{1,t,-}+c\_{2}^{+}V\_{2,t,-}+c\_{u}^{+}U\_{t,-}. |  |

Under the three-factor double-exponential stochastic volatility model, the
spot diffusive variance of the forward return is

|  |  |  |
| --- | --- | --- |
|  | Vt=V1,t+V2,t+η2​Ut.V\_{t}=V\_{1,t}+V\_{2,t}+\eta^{2}U\_{t}. |  |

In Table [6](https://arxiv.org/html/2512.11731v1#A3.T6 "Table 6 ‣ C.3 Three-Factor Double Exponential Stochastic Volatility Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") we report the parameters we use for the simulation. To construct the target implied volatility curve, we define two different sets of parameters and obtain two distinct implied volatility curves. Regarding the first one, we assume it is the liquid proxy, while the second is the illiquid target.

|  |  |  |
| --- | --- | --- |
| Parameter | Liquid Proxy | Illiquid Target |
| TT | 1.0 | 1.0 |
| S0S\_{0} | 100 | 100 |
| rfr\_{f} | 0.05 | 0.05 |
| V​10V1\_{0} | 0.01 | 0.01 |
| V​20V2\_{0} | 0.04 | 0.04 |
| U0U\_{0} | 0.0 | 0.0 |
| κ1\kappa\_{1} | 10.0 | 10.0 |
| v¯1\bar{v}\_{1} | 0.01 | 0.01 |
| σ1\sigma\_{1} | 0.4 | 0.4 |
| ρ1\rho\_{1} | -0.9 | -0.9 |
| κ2\kappa\_{2} | 0.2 | 0.2 |
| v¯2\bar{v}\_{2} | 0.04 | 0.03 |
| σ2\sigma\_{2} | 0.12 | 0.06 |
| ρ2\rho\_{2} | -0.8 | -0.6 |
| κu\kappa\_{u} | 0.6 | 0.6 |
| η\eta | 0.0 | 0.0 |
| μv\mu\_{v} | 0.7 | 0.7 |
| μu\mu\_{u} | 10.0 | 10.0 |
| ρu\rho\_{u} | 0.001 | 0.001 |
| c−c\_{-} | (0.0, 6.0, 0.22, 10.0)(0.0,\,6.0,\,0.22,\,10.0) | (0.0, 1.0, 0.1, 7.0)(0.0,\,1.0,\,0.1,\,7.0) |
| c+c\_{+} | (0.3, 20.0, 18.0, 0.0)(0.3,\,20.0,\,18.0,\,0.0) | (0.05, 15.0, 18.0, 0.0)(0.05,\,15.0,\,18.0,\,0.0) |
| λ−\lambda\_{-} | 8.0 | 10.0 |
| λ+\lambda\_{+} | 6.0 | 5.7 |

Table 6: Simulated parameters for Three Factor Double Exponential model. Set 1 for the liquid proxy and set 2 for the illiquid target.

We study two situations of severe market illiquidity by randomly selecting three in-the-money call option quotes for Scenario 1 and three out-of-the-money call option quotes for Scenario 2. We emphasize that these three option quotes constitute the only information on the terminal RND available to the models. In Fig. [18](https://arxiv.org/html/2512.11731v1#A3.F18.fig3 "Figure 18 ‣ C.3 Three-Factor Double Exponential Stochastic Volatility Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity"), we represent the first case under consideration (Scenario 1), which consists of three illiquid observations of in-the-money (ITM) call options.

![Refer to caption](setup_case1_3fde.png)

![Refer to caption](fit_case1_3fde.png)

Figure 18: Scenario 1 - On the left panel, the orange dots are the ITM strikes selected on the target illiquid implied volatility curve (blue solid line), and the orange solid line is the liquid source (proxy) implied volatility curve. On the right panel, the interpolation of the illiquid implied volatility curve of the Deep-LSE model (green solid line) and quadratic splines (red solid line).

We observe in Fig. [19](https://arxiv.org/html/2512.11731v1#A3.F19 "Figure 19 ‣ C.3 Three-Factor Double Exponential Stochastic Volatility Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") the estimates of Deep-LSE and quadratic splines compared to the ground truth illiquid RND. The Deep-LSE accurately recovers the illiquid RND, while the quadratic spline recovers an unstable estimate of the illiquid RND.

![Refer to caption](rnd_final_case1_3fde.png)


Figure 19: Scenario 1 - Illiquid RND recovery of Deep-LSE (orange curve) and quadratic splines (green curve) in comparison with the illiquid target ground truth simulated RND (blue curve).

We also test the Deep-LSE model on out-of-the-money call options and illiquid strikes (Scenario 2), and Fig. [20](https://arxiv.org/html/2512.11731v1#A3.F20.fig3 "Figure 20 ‣ C.3 Three-Factor Double Exponential Stochastic Volatility Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") illustrates this case. We illustrate in Fig. [21](https://arxiv.org/html/2512.11731v1#A3.F21 "Figure 21 ‣ C.3 Three-Factor Double Exponential Stochastic Volatility Model ‣ Appendix C Additional Simulations ‣ Transfer Learning (Il)liquidity") the estimates of the Deep-LSE and quadratic splines versus the ground truth illiquid RND. We conclude that, also in this case, the Deep-LSE recovers the RND better than quadratic splines.

![Refer to caption](setup2_case2_3fde.png)

![Refer to caption](fit2_case2_3fde.png)

Figure 20: Scenario 2 - On the left panel, the orange dots are the OTM strikes selected on the target illiquid implied volatility curve (blue solid line), and the orange solid line is the liquid source (proxy) implied volatility curve. On the right panel, the interpolation of the illiquid implied volatility curve of the Deep-LSE model (green solid line) and quadratic splines (red solid line).

![Refer to caption](final_rnd2_case2_3fde.png)


Figure 21: Case 2 - Illiquid RND recovery of Deep-LSE (orange curve) and quadratic splines (green curve) in comparison with the illiquid target ground truth simulated RND (blue curve).

## Appendix D Additional Empirical Analysis

Regarding Scenario 1 of the empirical analysis on the SPX, Fig. [22](https://arxiv.org/html/2512.11731v1#A4.F22.fig7 "Figure 22 ‣ Appendix D Additional Empirical Analysis ‣ Transfer Learning (Il)liquidity") and Fig. [23](https://arxiv.org/html/2512.11731v1#A4.F23.fig7 "Figure 23 ‣ Appendix D Additional Empirical Analysis ‣ Transfer Learning (Il)liquidity") depict the learning process of the Deep-LSE from the source (proxy) data and from the illiquid target data respectively. Fig. [22](https://arxiv.org/html/2512.11731v1#A4.F22.fig7 "Figure 22 ‣ Appendix D Additional Empirical Analysis ‣ Transfer Learning (Il)liquidity") is the first step of the estimation procedure. The model receives as input the liquid proxy data (blue points), which consists of the 2015 SPX implied volatility recovered from market data. The data points of the implied volatility curve are heavily convex in the strike range of 2100−22002100-2200, making the learning process more challenging. In addition, the scale of the data (extremely small) and the right tail, which consists only of 4 observations, are additional challenges. Nonetheless, at iteration number 100, the approximation of the implied volatility curve is well calibrated.

![Refer to caption](emp1.png)

![Refer to caption](emp2.png)

![Refer to caption](emp3.png)

![Refer to caption](emp4.png)

![Refer to caption](emp5.png)

![Refer to caption](emp6.png)

Figure 22: First step recovery (Scenario 1) - Source Deep-LSE Fit. The blue dots represent the implied volatility curve of option quotes of the liquid proxy asset while the blue solid line represents the fit of the interpolating function of the Deep-LSE model.

Fig. [23](https://arxiv.org/html/2512.11731v1#A4.F23.fig7 "Figure 23 ‣ Appendix D Additional Empirical Analysis ‣ Transfer Learning (Il)liquidity") represents the second step of the estimation process to recover the illiquid RND. In this phase, we perform transfer learning, fine-tuning the model pre-trained on the liquid proxy, using the illiquid market data. The orange data points consist are the implied volatility of the liquid proxy (2015 SPX) data, and the orange curve is the implied volatility curve that the Deep-LSE estimates during the first phase.

![Refer to caption](emp21.png)

![Refer to caption](emp22.png)

![Refer to caption](emp23.png)

![Refer to caption](emp24.png)

![Refer to caption](emp25.png)

![Refer to caption](emp26.png)

Figure 23: Second step recovery (Scenario 1) - Target Deep-LSE Fit. The model only sees the illiquid (red) quotes. The blue dots are the true implied volatility quotes that the Deep-LSE recovers (blue solid line). The solid orange and red curves represent the estimated IV curve of the first step.

Now, the Deep-LSE model receives as input the illiquid option quotes (the three red points) from the observed SPX 2016 data. The three red points mimic the sparse quotes of an illiquid market, whereas in reality, one observes the full SPX implied volatility curve for 2016 (blue points). The blue points, therefore, represent the underlying true implied volatility surface, which we deliberately sparsify to emulate illiquid conditions. We observe how the model adapts the knowledge learned during the first phase to the target data points, effectively recovering the illiquid implied volatility curve and producing the blue solid curve.