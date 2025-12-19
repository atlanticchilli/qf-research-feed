---
authors:
- Liying Zhang
- Ying Gao
doc_id: arxiv:2512.16115v1
family_id: arxiv:2512.16115
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: An Efficient Machine Learning Framework for Option Pricing via Fourier Transform
url_abs: http://arxiv.org/abs/2512.16115v1
url_html: https://arxiv.org/html/2512.16115v1
venue: arXiv q-fin
version: 1
year: 2025
---


Liying Zhang, Ying Gao
School of Mathematical Science, China University of Mining and Technology, Beijing 100083, China, lyzhang@lsec.cc.ac.cn School of Mathematical Science, China University of Mining and Technology, Beijing 100083, China, SQT2300702044@student.cumtb.edu.cn

###### Abstract

The increasing need for rapid recalibration of option pricing models in dynamic markets places stringent computational demands on data generation and valuation algorithms. In this work, we propose a hybrid algorithmic framework that integrates the smooth offset algorithm (SOA) with supervised machine learning models for the fast pricing of multiple path-independent options under exponential Lévy dynamics. Building upon the SOA-generated dataset, we train neural networks, random forests, and gradient boosted decision trees to construct surrogate pricing operators. Extensive numerical experiments demonstrate that, once trained, these surrogates achieve order-of-magnitude acceleration over direct SOA evaluation. Importantly, the proposed framework overcomes key numerical limitations inherent to fast Fourier transform–based methods, including the consistency of input data and the instability in deep out-of-the-money option pricing.

Keywords: Option Pricing, Machine Learning, Fast Fourier Transform.

## 1 Introduction

The option pricing problem is a core issue in the field of financial mathematics. Efficient and accurate pricing is crucial for the effective operation of financial markets and the realization of investors’ risk management goals. The development of option pricing theory relies heavily on mathematical models of stock price dynamics. Three prominent classes of models are particularly noteworthy. First, the Black-Scholes model ([[2](https://arxiv.org/html/2512.16115v1#bib.bib2)]) posits that the stock price process {St}0⩽t⩽T\{S\_{t}\}\_{0\leqslant t\leqslant T} follows a geometric Brownian motion (GBM) under the risk-neutral measure ℚ\mathbb{Q}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=r​St​d​t+σ​St​d​Btℚ,dS\_{t}=rS\_{t}dt+\sigma S\_{t}dB\_{t}^{\mathbb{Q}}, |  | (1.1) |

where rr denotes the risk-free rate, σ\sigma is the constant volatility, and BtℚB\_{t}^{\mathbb{Q}} is a standard Brownian motion under ℚ\mathbb{Q}. This framework, which assumes continuous sample paths and constant volatility, yields a closed-form solution for European options. Second, the Heston model (HM) ([[13](https://arxiv.org/html/2512.16115v1#bib.bib13)]) introduces a stochastic differential equation to characterize the dynamic evolution of volatility, with the specific form as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​St=r​St​d​t+Vt​St​d​Bt(1)​ℚ,d​Vt=κ​(θ−Vt)​d​t+σ​Vt​d​Bt(2)​ℚ,\left\{\begin{aligned} &dS\_{t}=rS\_{t}dt+\sqrt{V\_{t}}S\_{t}dB\_{t}^{(1)\mathbb{Q}},\\ &dV\_{t}=\kappa(\theta-V\_{t})dt+\sigma\sqrt{V\_{t}}dB\_{t}^{(2)\mathbb{Q}},\end{aligned}\right. |  | (1.2) |

where VtV\_{t} represents the instantaneous variance, κ\kappa the mean-reversion rate, and θ\theta the long-run variance level. While maintaining the assumption of continuous price trajectories, this model allows volatility to evolve stochastically, thereby accounting for leptokurtic asset returns. Third, exponential Lévy models accommodate discontinuous movements in stock prices through the inclusion of jump components ([[16](https://arxiv.org/html/2512.16115v1#bib.bib16)]). This category encompasses specifications such as jump-diffusion processes ([[20](https://arxiv.org/html/2512.16115v1#bib.bib20)]), the variance Gamma process ([[19](https://arxiv.org/html/2512.16115v1#bib.bib19)]), and the Carr–Geman–Madan–Yor (CGMY) process
([[6](https://arxiv.org/html/2512.16115v1#bib.bib6)]). By relaxing the path continuity assumption, exponential Lévy models are particularly adept at capturing the abrupt, large-scale movements frequently observed in financial markets.

Due to the complex mathematical operations in the aforementioned stock price models, closed-form solutions are often hard to derive. Consequently, numerical algorithms have become a key method to price both single and multiple options. For single option pricing, beyond the classical Monte Carlo method([[1](https://arxiv.org/html/2512.16115v1#bib.bib1), [22](https://arxiv.org/html/2512.16115v1#bib.bib22)]), and then various numerical pricing techniques have been developed in the financial field. An algorithm based on the binomial tree model introduced by Cox et al. ([[8](https://arxiv.org/html/2512.16115v1#bib.bib8)]) employs discrete-time approximation of asset price paths, establishing a flexible pricing framework for path-dependent derivatives such as American options. Boyle ([[3](https://arxiv.org/html/2512.16115v1#bib.bib3)]) subsequently developed an algorithm based on the trinomial tree model, incorporating an additional intermediate price movement to enhance numerical accuracy and convergence rate, with extensions to multi-asset options. Brennan et al. ([[4](https://arxiv.org/html/2512.16115v1#bib.bib4)]) demonstrate that the option pricing problem can be formulated as a partial differential equation (PDE) boundary value problem and can be effectively solved using the finite difference method. Meanwhile, this method is also useful for some path-dependent derivatives, such as American options, where early exercise
features transform the pricing task into a free boundary problem ([[24](https://arxiv.org/html/2512.16115v1#bib.bib24)]).

Although these methods offer distinct advantages in terms of flexibility, their application remains constrained, particularly in high-dimensional or high-precision pricing scenarios where computational costs increase substantially. Consequently, the development of efficient and robust pricing algorithms represents an ongoing research imperative. [[7](https://arxiv.org/html/2512.16115v1#bib.bib7)] proposes an algorithm based on Fourier transform (FT), which we refer to as the Carr-Madan algorithm (CMA). The CMA introduces an offset term to modify the option pricing formula, ensuring that its Fourier transform admits a closed-form expression, and subsequently recovers the option price via an inverse transform. To further improve efficiency, we leverage the relationship between the smoothness of a function and the decay rate of its Fourier transform tail to propose a novel offset term. This modification enhances the algorithm’s efficiency, and the corresponding improved method is termed the smooth offset algorithm (SOA).
Numerical experiments show that under two option types (European options and digital options) and three stock price models (GBM, HM, and EVGP), when error tolerances are equivalent, the operational efficiency of SOA is significantly superior to that of CMA, with its running time only accounting for 60%−70%60\%-70\% of CMA’s. Details are provided in Section [3](https://arxiv.org/html/2512.16115v1#S3 "3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform").

The research on algorithms for single option pricing is relatively mature. However, with the continuous expansion of business scales in financial institutions such as investment banks, the demand for pricing large-scale option portfolios has become increasingly prominent, and the traditional single option pricing algorithms can no longer meet the efficiency requirements of batch processing. Existing studies have also begun to focus on pricing algorithms for multiple options. For example, under the discrete-time framework, Derman and Kani proposed a pricing algorithm based on the implied binomial tree (IBT) model ([[9](https://arxiv.org/html/2512.16115v1#bib.bib9)]). This algorithm can derive the local volatility surface from observed market option prices, providing a flexible numerical tool for the fitting and pricing of multiple option portfolios. However, it relies on local volatility theory, requires the assumption of a unique volatility surface, and imposes strict constraints on input option data. The Brodie-Kaya (BK) algorithm proposed by Brodie and Kaya ([[5](https://arxiv.org/html/2512.16115v1#bib.bib5)]) constructs accurate simulation paths for stochastic volatility models, enabling batch pricing of options with various payoff structures through a single simulation and significantly improving the computational efficiency of the Monte Carlo method. Nevertheless, this algorithm is only applicable to affine diffusion processes and is difficult to extend to non-affine models such as exponential Lévy processes.

Compared with traditional algorithms, machine learning (ML) has seen growing adoption in option pricing.
Recent research increasingly leverages ML models to establish the mapping between option attributes and their theoretical prices. For example, [[15](https://arxiv.org/html/2512.16115v1#bib.bib15)] investigates ordinary least squares, radial basis function networks, multi-layer perceptron networks, and projection pursuit on the Black–Scholes option pricing problem. It demonstrates that ML models achieve accurate pricing and delta-hedging. Likewise, [[11](https://arxiv.org/html/2512.16115v1#bib.bib11)] analyzes basket call options. It shows that neural networks (NNs) can compute prices at a dramatically faster speed. This speed is approximately one million times faster than traditional methods, while maintaining satisfactory accuracy.
To address the problems of inadequate model accuracy and anti-noise stability in option pricing, [[17](https://arxiv.org/html/2512.16115v1#bib.bib17)] adopts an experimental evaluation strategy integrated with financial theories, investigates the application effect of ensemble learning and the interaction between sliding windows and noise, verifies the applicability of ensemble learning to option pricing, and clarifies the adaptation logic between the two as well as the influence law on the pricing stability of the model.
Other ML models address option pricing problems by numerically solving the associated PDEs through NNs. This method is commonly referred to as physics informed neural networks (PINNs) ([[10](https://arxiv.org/html/2512.16115v1#bib.bib10), [12](https://arxiv.org/html/2512.16115v1#bib.bib12), [21](https://arxiv.org/html/2512.16115v1#bib.bib21), [26](https://arxiv.org/html/2512.16115v1#bib.bib26)]). Although traditional machine learning models have achieved certain breakthroughs in pricing accuracy and efficiency, they still face core challenges in practical financial applications. The dynamic changes in market conditions require models to have rapid updating capabilities, while pricing models typically rely on large-scale data for training. Traditional numerical methods exhibit inefficiencies in data generation, and illiquid option contracts also suffer from data scarcity, making it difficult to support high-frequency iterations. Thus, we propose a pricing algorithm integrating SOA with machine learning. This algorithm uses option data generated by SOA as the training set, allowing the data-driven model to learn the mapping relationship between option attributes and their corresponding prices. Numerical experiments demonstrate that compared with fast Fourier transform (FFT) the machine learning models trained in this way is not constrained by input conditions and maintains good numerical stability.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2512.16115v1#S2 "2 Stock Price Models ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") presents the stock price models.
Section [3](https://arxiv.org/html/2512.16115v1#S3 "3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") briefly reviews CMA and introduces the theoretical foundations of the SOA method, with its advantages being verified through numerical experiments. The FFT-based
and ML-based frameworks are discussed in Section [4](https://arxiv.org/html/2512.16115v1#S4 "4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [5](https://arxiv.org/html/2512.16115v1#S5 "5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), with numerical experiments that compare them and the plain sequential pricing approach by SOA. Finally, Section [6](https://arxiv.org/html/2512.16115v1#S6 "6 Conclusions ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") concludes.

## 2 Stock Price Models

### 2.1 Unified Framework of Stock Price Models

This section incorporates three types of stock price models, namely geometric Brownian motion (GBM), Heston model (HM), and exponential variance Gamma process (EVGP), into a unified framework and derives the corresponding characteristic function for each model. Consider a stock price process {St}0⩽t⩽T\{S\_{t}\}\_{0\leqslant t\leqslant T} over the time interval [0,T][0,T]. Let {Xt}0⩽t⩽T\{X\_{t}\}\_{0\leqslant t\leqslant T} be a Lévy process under measure ℚ\mathbb{Q}, and the exponential Lévy process for the stock price is driven by the following stochastic differential equation (SDE):

|  |  |  |
| --- | --- | --- |
|  | d​St=r​St​d​t+St​d​Xt,0⩽t⩽T,dS\_{t}=rS\_{t}\,dt+S\_{t}\,dX\_{t},\qquad 0\leqslant t\leqslant T, |  |

where rr denotes the risk-free interest rate. The solution to this SDE can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​exp⁡[(r+ζ)​t+Xt]=S0​exp⁡(r​t+Xt†),0⩽t⩽T,S\_{t}=S\_{0}\exp\big[(r+\zeta)t+X\_{t}\big]=S\_{0}\exp(rt+X\_{t}^{\dagger}),\qquad 0\leqslant t\leqslant T, |  | (2.1) |

where Xt†=ζ​t+XtX\_{t}^{\dagger}=\zeta t+X\_{t}, and ζ\zeta serves as a compensator, ensuring that the discounted process {e−r​T​St}0⩽t⩽T\left\{e^{-rT}S\_{t}\right\}\_{0\leqslant t\leqslant T} is a martingale under measure ℚ\mathbb{Q}.
To integrate the three stock price models into a unified framework, we rewrite each of them in the form of (2.1) and derive the characteristic function of Xt†X\_{t}^{\dagger} using the characteristic function of XtX\_{t}, specifically ΦXt†​(z)=ei​ζ​z​t​ΦXt​(z).\Phi\_{X\_{t}^{\dagger}}(z)=e^{i\zeta zt}\Phi\_{X\_{t}}(z).

For the GBM, its compensator term is ζ=−12​σ2\zeta=-\frac{1}{2}\sigma^{2}, where Xt=σ​BtℚX\_{t}=\sigma B\_{t}^{\mathbb{Q}} with the characteristic function

|  |  |  |
| --- | --- | --- |
|  | ΦXt​(z)=exp⁡(−12​σ2​z2​t).\Phi\_{X\_{t}}(z)=\exp\left(-\frac{1}{2}\sigma^{2}z^{2}t\right). |  |

For the EVGP, its compensator term is given by
ζ=1ν​ln⁡(1−θ​ν−12​σ2​ν),\zeta=\frac{1}{\nu}\ln\left(1-\theta\nu-\frac{1}{2}\sigma^{2}\nu\right),
and the corresponding Lévy process is Xt=VGPt(θ,σ,ν)X\_{t}=\text{VGP}\_{t}^{(\theta,\sigma,\nu)} with the characteristic function

|  |  |  |
| --- | --- | --- |
|  | ΦVGPt(θ,σ,ν)​(z)=(1−i​z​θ​ν+12​σ2​ν​z2)−tν.\Phi\_{\text{VGP}\_{t}^{(\theta,\sigma,\nu)}}(z)=\left(1-iz\theta\nu+\frac{1}{2}\sigma^{2}\nu z^{2}\right)^{-\frac{t}{\nu}}. |  |

Especially, the Heston model is not an exponential Lévy process, and as a result, no explicit expression forXt†X\_{t}^{\dagger} can be obtained. However, the characteristic function of Xt†X^{\dagger}\_{t} can still be obtained by exploiting the log-price representation

|  |  |  |
| --- | --- | --- |
|  | ln⁡St=ln⁡S0+r​t+Xt†.\ln S\_{t}=\ln S\_{0}+rt+X\_{t}^{\dagger}. |  |

From this relation, the characteristic function of Xt†X\_{t}^{\dagger} can be derived

|  |  |  |
| --- | --- | --- |
|  | ΦXt†​(z)=𝔼​[ei​z​(ln⁡St−ln⁡S0−r​t)]=e−i​z​(ln⁡S0+r​t)​Φln⁡St​(z).\Phi\_{X\_{t}^{\dagger}}(z)=\mathbb{E}\left[e^{iz(\ln S\_{t}-\ln S\_{0}-rt)}\right]=e^{-iz(\ln S\_{0}+rt)}\Phi\_{\ln S\_{t}}(z). |  |

The closed-form expression of Φln⁡St​(z)\Phi\_{\ln S\_{t}}(z) is available ([[14](https://arxiv.org/html/2512.16115v1#bib.bib14)])
, and is given by

|  |  |  |
| --- | --- | --- |
|  | Φln⁡St​(z)=exp⁡[i​z​ln⁡S0+i​z​r​t+κ​θ​t​(κ−i​ρ​σ​z)σ2](cosh⁡τ​t2+κ−i​ρ​σ​zτ​sinh⁡τ​t2)2​κ​θσ2​exp⁡[−(z2+i​z)​V0τ​coth⁡τ​t2+κ−i​ρ​σ​z],\displaystyle\Phi\_{\ln S\_{t}}(z)=\frac{\exp\left[iz\ln S\_{0}+izrt+\frac{\kappa\theta t(\kappa-i\rho\sigma z)}{\sigma^{2}}\right]}{\left(\cosh\frac{\tau t}{2}+\frac{\kappa-i\rho\sigma z}{\tau}\sinh\frac{\tau t}{2}\right)^{\frac{2\kappa\theta}{\sigma^{2}}}}\exp\left[\frac{-\left(z^{2}+iz\right)V\_{0}}{\tau\operatorname{coth}\frac{\tau t}{2}+\kappa-i\rho\sigma z}\right], |  |

where τ=σ2​(z2+i​z)+(κ−i​ρ​σ​z)2\tau=\sqrt{\sigma^{2}\left(z^{2}+iz\right)+(\kappa-i\rho\sigma z)^{2}}, and V0V\_{0} is the initial variance.

###### Remark 2.1.

To simplify notation, the initial stock price S0S\_{0} is normalized to 1, and results for any arbitrary S0S\_{0} can be obtained by rescaling the normalized price. For European call options:

|  |  |  |
| --- | --- | --- |
|  | e−r​T​𝔼Q​[(ST−K)+]=S0​e−r​T​𝔼Q​[(exp⁡(r​T+XT†)−KS0)+],e^{-rT}\mathbb{E}^{Q}\left[(S\_{T}-K)^{+}\right]=S\_{0}e^{-rT}\mathbb{E}^{Q}\left[\left(\exp\left(rT+X\_{T}^{\dagger}\right)-\frac{K}{S\_{0}}\right)^{+}\right], |  |

where e−r​T​𝔼Q​[(exp⁡(r​T+XT†)−KS0)+]e^{-rT}\mathbb{E}^{Q}\left[\left(\exp\left(rT+X\_{T}^{\dagger}\right)-\frac{K}{S\_{0}}\right)^{+}\right] is the normalized price under S0′=1S\_{0}^{\prime}=1 and K′=KS0K^{\prime}=\frac{K}{S\_{0}} , and the true price needs to be multiplied by S0S\_{0}. Similarly, for digital options:

|  |  |  |
| --- | --- | --- |
|  | e−r​T​𝔼Q​[1{ST⩾K}]=e−r​T​𝔼Q​[1{exp⁡(r​T+XT†)⩾KS0}],e^{-rT}\mathbb{E}^{Q}\left[1\_{\{S\_{T}\geqslant K\}}\right]=e^{-rT}\mathbb{E}^{Q}\left[1\_{\left\{\exp\left(rT+X\_{T}^{\dagger}\right)\geqslant\frac{K}{S\_{0}}\right\}}\right], |  |

whose scaling factor is 1, meaning the normalized price equals the true price.

## 3 SOA for Single Option Pricing

### 3.1 Revised CMA

CMA modifies the original option pricing formula by introducing an offset term, ensuring that the FT of
the resulting expression exists and admits a close-form representation. Consider an European or digital option whose underlying stock price {St}0⩽t⩽T\left\{S\_{t}\right\}\_{0\leqslant t\leqslant T} follows exponential Lévy process with St=exp⁡(r​t+Xt†)S\_{t}=\exp\left(rt+X\_{t}^{\dagger}\right). The price function modified by the CM offset term is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(k)={V​(k)−e−r​T​(er​T−ek)+, for European options,V​(k)−e−r​T​1er​T⩾ek, for digital options.\hat{V}(k)=\begin{cases}V(k)-e^{-rT}\left(e^{rT}-e^{k}\right)^{+},\text{\,\,\,\,for European options},\\ V(k)-e^{-rT}\mathrm{1}\_{e^{rT}\geqslant e^{k}},\text{\,\,\,\,for digital options}.\end{cases} |  | (3.1) |

Then the FT of V^\hat{V} is given by

|  |  |  |
| --- | --- | --- |
|  | η​(z)=ℱ​[V^]​(z)={1i​z​(i​z+1)​ei​z​r​T​[Φ†​(z−i)−1], for European options,1i​z​e(i​z−1)​r​T​[Φ†​(z)−1], for digital options,\eta(z)=\mathcal{F}\left[{\hat{V}}\right](z)=\begin{cases}\frac{1}{iz(iz+1)}e^{izrT}\left[\Phi^{\dagger}(z-i)-1\right],\text{\,\,\,\,for European options},\\ \frac{1}{iz}e^{(iz-1)rT}\left[\Phi^{\dagger}(z)-1\right],\text{\,\,\,\,for digital options},\end{cases} |  |

where Φ†\Phi^{\dagger} is the FT of XT†X^{\dagger}\_{T}.

The function V^​(k)\hat{V}(k) can be obtained via the inverse FT of η\eta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(k)=ℱ−1​[η]​(k)=12​π​∫−∞∞e−i​z​k​η​(z)​𝑑z.\hat{V}(k)=\mathcal{F}^{-1}\left[\eta\right](k)=\frac{1}{2\pi}\int\_{-\infty}^{\infty}e^{-izk}\eta(z)dz. |  | (3.2) |

The integral in ([3.2](https://arxiv.org/html/2512.16115v1#S3.E2 "In 3.1 Revised CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) can only be evaluated numerically. Once V^​(k)\hat{V}(k) has been obtained, V​(k)V(k) is given by

|  |  |  |
| --- | --- | --- |
|  | V​(k)={V^​(k)+e−r​T​(er​T−ek)+, for European options,V^​(k)+e−r​T​1er​T⩾ek, for digital options.V(k)=\begin{cases}\hat{V}(k)+e^{-rT}\left(e^{rT}-e^{k}\right)^{+},\text{\,\,\,\,for European options},\\ \hat{V}(k)+e^{-rT}\mathrm{1}\_{e^{rT}\geqslant e^{k}},\text{\,\,\,\,for digital options}.\end{cases} |  |

To develop an algorithm that achieves better computational efficiency than CMA, it is essential to ensure that the tail of the function η\eta decays more rapidly. A faster tail decay rate accelerates the convergence of the numerical integration used to evaluate ([3.2](https://arxiv.org/html/2512.16115v1#S3.E2 "In 3.1 Revised CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")), thereby improving the overall efficiency.
The intuition behind this point is illustrated in Figure [1](https://arxiv.org/html/2512.16115v1#S3.F1 "Figure 1 ‣ 3.1 Revised CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), where two functions ηi,\eta\_{i}, i=1,2i=1,2 are considered. The objective is to evaluate integrals

|  |  |  |
| --- | --- | --- |
|  | ∫0∞ηi​(z)​𝑑z,i=1,2,\int\_{0}^{\infty}\eta\_{i}(z)dz,i=1,2, |  |

which are approximated using a truncation point B>0B>0:

|  |  |  |
| --- | --- | --- |
|  | ∫0∞ηi​(z)​𝑑z≈∫0Bηi​(z)​𝑑z,i=1,2.\int\_{0}^{\infty}\eta\_{i}(z)dz\approx\int\_{0}^{B}\eta\_{i}(z)dz,i=1,2. |  |

Figure 1: Impacts of Tail Decay Rates on the Convergence Speed of Numerical Integrations

![Refer to caption](Figures/CompareConvergenceSpeedTheoretical.png)

Evidently, this truncation introduces a larger approximation error for η2\eta\_{2} since the tail of η2\eta\_{2} decays more slowly. The vertical truncation line at z=Bz=B omits a non-negligible portion of the area beyond z=Bz=B. In contrast, η1\eta\_{1} exhibits a faster decay rate and approaches zero in the neighborhood of z=Bz=B, leading to a more accurate approximation. Consequently, to achieve comparable accuracy for η2\eta\_{2}, a larger truncation point BB must be selected. However, expanding the integration interval [0,B][0,B] requires a greater number of subintervals in the numerical integration, thereby increasing the computational cost. In the application of this paper, η\eta is the FT of V^\hat{V}, and thus the properties of V^\hat{V} must be closely linked to the tail decay rate of η\eta. Specifically, a smoother V^\hat{V} results in a faster decay of η\eta at its tail. See Theorem 2.5 in Reference [[25](https://arxiv.org/html/2512.16115v1#bib.bib25)] for details.

The CM offset term is defined as the discounted payoff evaluated at the terminal stock price, i.e. 𝔼ℚ​[ST]=er​T\mathbb{E}^{\mathbb{Q}}[S\_{T}]=e^{rT}. However, because the payoff function itself lacks smoothness, the resulting CM offset term also exhibits poor smoothness, which negatively affects convergence.
To address this issue, the smooth offset term in SOA is constructed by averaging the payoff values over a range of stock prices rather than evaluating it at a single point. This averaging operation improves the smoothness of the offset term and thereby accelerates the algorithm. The formal result is presented in Theorem [3.1](https://arxiv.org/html/2512.16115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Revised CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform").

###### Theorem 3.1.

Consider an European or digital option whose underlying stocks price {St}0⩽t⩽T\left\{S\_{t}\right\}\_{0\leqslant t\leqslant T} follows exponential Lévy process with St=exp⁡(r​t+Xt†)S\_{t}=\exp\left(rt+X\_{t}^{\dagger}\right). The price function modified by the smooth offset term is

|  |  |  |
| --- | --- | --- |
|  | V^​(k)={V​(k)−e−r​T​𝔼ℚ​[(ST∧−ek)+], for European options,V​(k)−e−r​T​𝔼ℚ​[𝟏ST∧⩾ek], for digital options,\hat{V}(k)=\begin{cases}V(k)-e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[(S\_{T}^{\wedge}-e^{k})^{+}\right],\text{\,\,\,\,for European options},\\ V(k)-e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[\mathbf{1}\_{S\_{T}^{\wedge}\geqslant e^{k}}\right],\text{\,\,\,\,for digital options},\end{cases} |  |

where ST∧S\_{T}^{\wedge} is the terminal value of process {St∧}0⩽t⩽T\left\{S\_{t}^{\wedge}\right\}\_{0\leqslant t\leqslant T} that follows SDE

|  |  |  |
| --- | --- | --- |
|  | {d​St∧=r​St∧​d​t+St∧​d​Btℚ,S0∧=1,\begin{cases}dS\_{t}^{\wedge}=rS\_{t}^{\wedge}dt+S\_{t}^{\wedge}dB\_{t}^{\mathbb{Q}},\\ S\_{0}^{\wedge}=1,\end{cases} |  |

which is a GBM under measure ℚ\mathbb{Q} with volatility 100%.
Then the FT of V^\hat{V} is given by

|  |  |  |
| --- | --- | --- |
|  | η​(z)=ℱ​[V^]​(z)={1i​z​(i​z+1)​ei​z​r​T​[Φ†​(z−i)−Φ∧​(z−i)], for European options,1i​z​e(i​z−1)​r​T​[Φ†​(z)−Φ∧​(z)], for digital options,\eta(z)=\mathcal{F}\left[{\hat{V}}\right](z)=\begin{cases}\frac{1}{iz(iz+1)}e^{izrT}\left[\Phi^{\dagger}(z-i)-\Phi^{\wedge}(z-i)\right],\text{\,\,\,\, for European options},\\ \frac{1}{iz}e^{(iz-1)rT}\left[\Phi^{\dagger}(z)-\Phi^{\wedge}(z)\right],\text{\,\,\,\,for digital options},\end{cases} |  |

where Φ†\Phi^{\dagger} is the FT of XT†X^{\dagger}\_{T} and function Φ∧\Phi^{\wedge} is the FT of random variable −T2+BTℚ-\frac{T}{2}+B\_{T}^{\mathbb{Q}}, given by

|  |  |  |
| --- | --- | --- |
|  | Φ∧​(z)=exp⁡[−T2​(i​z+z2)].\Phi^{\wedge}(z)=\exp\left[-\frac{T}{2}(iz+z^{2})\right]. |  |

###### Proof.

The smooth offset term
e−r​T​𝔼ℚ​[(ST∧−ek)+]e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[(S\_{T}^{\wedge}-e^{k})^{+}\right]
can be interpreted as the price of a virtual European option whose underlying stock price follows the process {St∧}0⩽t⩽T\left\{S\_{t}^{\wedge}\right\}\_{0\leqslant t\leqslant T}.
Since {St∧}0⩽t⩽T\left\{S\_{t}^{\wedge}\right\}\_{0\leqslant t\leqslant T} follows GBM, which is a special case of exponential Lévy processes.

Let V∧​(k)=e−r​T​𝔼ℚ​[(ST∧−ek)+]V^{\wedge}(k)=e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[(S\_{T}^{\wedge}-e^{k})^{+}\right]. Then V∧​(k)V^{\wedge}(k) denotes the price of the virtual European option mentioned above. It is worth noting that although {St}0⩽t⩽T\left\{S\_{t}\right\}\_{0\leqslant t\leqslant T} and {St∧}0⩽t⩽T\left\{S\_{t}^{\wedge}\right\}\_{0\leqslant t\leqslant T} are distinct processes, they share the same terminal expectation as the discounted value of each process must constitute a ℚ−\mathbb{Q}-martingale:

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[ST]=𝔼ℚ​[ST∧]=S0​er​T=er​T.\mathbb{E}^{\mathbb{Q}}\left[S\_{T}\right]=\mathbb{E}^{\mathbb{Q}}\left[S\_{T}^{\wedge}\right]=S\_{0}e^{rT}=e^{rT}. |  |

The modified price function can thus be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(k)=\displaystyle\hat{V}(k)= | V​(k)−V∧​(k)=[V​(k)−e−r​T​(𝔼ℚ​[ST]−ek)+]−[V∧​(k)−e−r​T​(𝔼ℚ​[ST∧]−ek)+].\displaystyle V(k)-V^{\wedge}(k)=\left[V(k)-e^{-rT}\left(\mathbb{E}^{\mathbb{Q}}\left[S\_{T}\right]-e^{k}\right)^{+}\right]-\left[V^{\wedge}(k)-e^{-rT}\left(\mathbb{E}^{\mathbb{Q}}\left[S\_{T}^{\wedge}\right]-e^{k}\right)^{+}\right]. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | VA​(k)=V​(k)−e−r​T​(𝔼ℚ​[ST]−ek)+​ and ​VB​(k)=V∧​(k)−e−r​T​(𝔼ℚ​[ST∧]−ek)+,V^{A}(k)=V(k)-e^{-rT}\left(\mathbb{E}^{\mathbb{Q}}\left[S\_{T}\right]-e^{k}\right)^{+}\text{\,\,and\,\,}V^{B}(k)=V^{\wedge}(k)-e^{-rT}\left(\mathbb{E}^{\mathbb{Q}}\left[S\_{T}^{\wedge}\right]-e^{k}\right)^{+}, |  |

and we obtain

|  |  |  |
| --- | --- | --- |
|  | ℱ​[VA]​(z)=1i​z​(i​z+1)​ei​z​r​T​[Φ†​(z−i)−1]\mathcal{F}\left[V^{A}\right](z)=\frac{1}{iz(iz+1)}e^{izrT}\left[\Phi^{\dagger}(z-i)-1\right] |  |

and

|  |  |  |
| --- | --- | --- |
|  | ℱ​[VB]​(z)=1i​z​(i​z+1)​ei​z​r​T​[Φ∧​(z−i)−1].\mathcal{F}\left[V^{B}\right](z)=\frac{1}{iz(iz+1)}e^{izrT}\left[\Phi^{\wedge}(z-i)-1\right]. |  |

Therefore, the FT of V^\hat{V} is

|  |  |  |
| --- | --- | --- |
|  | η​(z)=ℱ​[VA]​(z)−ℱ​[VB]​(z)=1i​z​(i​z+1)​ei​z​r​T​[Φ†​(z−i)−Φ∧​(z−i)].\eta(z)=\mathcal{F}\left[V^{A}\right](z)-\mathcal{F}\left[V^{B}\right](z)=\frac{1}{iz(iz+1)}e^{izrT}\left[\Phi^{\dagger}(z-i)-\Phi^{\wedge}(z-i)\right]. |  |

The proof is provided for European options, while digital options are treated analogously.
∎

The function V^​(k)\hat{V}(k) is obtained by applying the inverse FT to η​(z)\eta(z), i.e. V^​(k)=ℱ−1​[η]​(k)\hat{V}(k)=\mathcal{F}^{-1}\left[\eta\right](k), i.e.

|  |  |  |
| --- | --- | --- |
|  | V​(k)={V^​(k)+e−r​T​𝔼ℚ​[(ST∧−ek)+], for European options,V^​(k)+e−r​T​𝔼ℚ​[𝟏ST∧⩾ek], for digital options,V(k)=\begin{cases}\hat{V}(k)+e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[\left(S\_{T}^{\wedge}-e^{k}\right)^{+}\right],\text{\,\,\,\,for European options},\\ \hat{V}(k)+e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[\mathbf{1}\_{S\_{T}^{\wedge}\geqslant e^{k}}\right],\text{\,\,\,\,for digital options},\end{cases} |  |

where the smooth offset terms admit close-form expressions. Specifically, let FNF\_{N} be the cumulative density function of the standard normal distribution, and then we have

|  |  |  |
| --- | --- | --- |
|  | {e−r​T​𝔼ℚ​[(ST∧−ek)+]=FN​(d1)−ek−r​T​FN​(d2),e−r​T​𝔼ℚ​[𝟏ST∧⩾ek]=e−r​T​FN​(d2),d1,2=1T​[−k+(r±12)​T].\begin{cases}e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[\left(S\_{T}^{\wedge}-e^{k}\right)^{+}\right]=F\_{N}(d\_{1})-e^{k-rT}F\_{N}(d\_{2}),\\ e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[\mathbf{1}\_{S\_{T}^{\wedge}\geqslant e^{k}}\right]=e^{-rT}F\_{N}(d\_{2}),\\ d\_{1,2}=\frac{1}{\sqrt{T}}\left[-k+\left(r\pm\frac{1}{2}\right)T\right].\end{cases} |  |

To illustrate the contrast between the two offset terms, we draw offset terms for both option types in Figure [2](https://arxiv.org/html/2512.16115v1#S3.F2 "Figure 2 ‣ 3.1 Revised CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform").
It can be observed that the smooth offset terms eliminate the sharp corners at k=r​Tk=rT, resulting in continuous and differentiable curves.

Figure 2: CM and Smooth Offset Terms for European and digital options (rr=2.0%, TT=3 Months)

![Refer to caption](Figures/CompareTwoOffsetTerms.png)

Additionally, Figure [3](https://arxiv.org/html/2512.16115v1#S3.F3 "Figure 3 ‣ 3.1 Revised CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") compares the functions η\eta corresponding to different combinations of offset terms and option types under the settings given by Table [1](https://arxiv.org/html/2512.16115v1#S3.T1 "Table 1 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [2](https://arxiv.org/html/2512.16115v1#S3.T2 "Table 2 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") presented in section [3.2](https://arxiv.org/html/2512.16115v1#S3.SS2 "3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform").
These observations indicate that the η\eta functions derived from the smooth offset terms decay to 0 significantly faster than those based on the CM offset terms.
This advantage is particularly pronounced for digital options, whose payoff functions exhibit lower smoothness than European options.

Figure 3: Cases of η\eta under Different Settings for the Two Offset Terms

![Refer to caption](Figures/OffsetsAndDecayRate.png)

### 3.2 Numerical Experiments for SOA and CMA

We verify the advantages of SOA over CMA through numerical experiments. The tests cover two option types, including European and digital, as well as three stock price models, including GBM, HM and EVGP.
The specifications of the options and stock price models are summarized in Table [1](https://arxiv.org/html/2512.16115v1#S3.T1 "Table 1 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [2](https://arxiv.org/html/2512.16115v1#S3.T2 "Table 2 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), respectively. To verify the accuracy of CMA and SOA, appropriate computational benchmarks are required. When stock prices are assumed to follow GBM, closed-form solutions are available for both European and digital options, and these solutions serve as the benchmarks for this case. In contrast, for HM and EVGP, no closed-form expressions exist. Consequently, for these cases, MC methods are employed to generate benchmarks.

Table 1: Details of Options in the Numerical Experiment

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Option Type | Spot Price  (S0S\_{0}) | Strike Price  (KK) | Maturity  (TT) | Risk-free Rate  (rr) |
| European | 150.0150.0 | 100.0100.0 | 33 months (0.250.25) | 2.0%2.0\% |
| Digital | 150.0150.0 | 100.0100.0 | 33 months (0.250.25) | 2.0%2.0\% |




Table 2: Details of Stock Price Models in the Numerical Experiment

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Model Type |  |  |  | Parameters |
| GBM |  |  |  | σ=0.25\sigma=0.25 |
| HM |  |  |  | (κ,θ,σ,ρ,V0)=(2.30,0.36,0.10,0.60,0.49)(\kappa,\theta,\sigma,\rho,V\_{0})=(2.30,0.36,0.10,0.60,0.49) |
| EVGP |  |  |  | (θ,σ,ν)=(0.10,0.20,0.30)(\theta,\sigma,\nu)=(0.10,0.20,0.30) |

Hereafter, we elaborate on the specific implementation processes of CMA and SOA. The most important step of CMA or SOA is numerically evaluating the following integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(k)=12​π​∫−∞∞e−i​z​k​η​(z)​𝑑z=1π​∫0∞e−i​z​k​η​(z)​𝑑z.\hat{V}(k)=\frac{1}{2\pi}\int\_{-\infty}^{\infty}e^{-izk}\eta(z)dz=\frac{1}{\pi}\int\_{0}^{\infty}e^{-izk}\eta(z)dz. |  | (3.3) |

The integral in ([3.3](https://arxiv.org/html/2512.16115v1#S3.E3 "In 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) is numerically computed using the Simpson’s rule: given a truncation point BB , the interval [0,B][0,B] is divided into NN subintervals, and then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(k)≈Δ​zπ​∑j=0Nwj​e−i​j​k​Δ​z​η​(j​Δ​z),\hat{V}(k)\approx\frac{\Delta z}{\pi}\sum\_{j=0}^{N}w\_{j}e^{-ijk\Delta z}\eta(j\Delta z), |  | (3.4) |

where the weights wjw\_{j} are the weight coefficient corresponding to the node in Simpson’s numerical integration rule.

Equation ([3.4](https://arxiv.org/html/2512.16115v1#S3.E4 "In 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) better illustrates the advantages of SOA: the smoothness of V^\hat{V} leads to rapid tail decay of η\eta as z→∞z\to\infty, thereby allowing for a smaller truncation point BB to achieve relatively accurate option pricing. As shown in Figure [4](https://arxiv.org/html/2512.16115v1#S3.F4 "Figure 4 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), which plots the option price against BB for different cases, both CMA and SOA converge to the reference value. However, SOA attains convergence with a significantly smaller BB, while CMA exhibits slower convergence−-a difference that is particularly pronounced for digital options. Since SOA achieves satisfactory accuracy with a smaller BB, the number of subintervals NN required for the numerical integration in ([3.4](https://arxiv.org/html/2512.16115v1#S3.E4 "In 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) can be reduced, thus improving computational efficiency.

Figure 4: Relationship between Truncation Point BB and Option Prices

![Refer to caption](Figures/CompareConvergenceSpeed.png)

In practical applications, both CMA and SOA involve two tunable parameters: the truncation point (BB) and the number of subintervals in the numerical integration (NN). It is crucial to choose these parameters appropriately so that the algorithm can strike a balance between the accuracy and the efficiency. A value of BB that is too small leads to intolerable errors, whereas an excessively large value of BB increases computational cost. The choice of NN is inherently dependent on BB: as BB increases, a larger NN is required to maintain the desired level of accuracy.

To ensure a fair comparison of execution times between CMA and SOA, a systematic policy for determining BB and NN is required. When identical values of BB and NN are used for both algorithms, their execution times may appear similar. However, such a comparison is misleading, as it disregards the differences in accuracy. In particular, the error associated with CMA can be substantially larger than that of SOA if the selected BB and NN are insufficient for CMA to achieve convergence.

To address this issue, an algorithm is developed to determine the optimal parameter settings for CMA and SOA. The execution times of both algorithms are then compared under their respective optimal configurations, ensuring a fair performance evaluation. For the 66 cases, let {V(n,ℓ)}ℓ=16\left\{V^{(n,\ell)}\right\}\_{\ell=1}^{6} be the option prices computed numerically by either CMA or SOA, and {V(b,ℓ)}i=ℓℓ\left\{V^{(b,\ell)}\right\}\_{i=\ell}^{\ell} represent the corresponding benchmark prices.
The relative pricing error for the ℓth\ell^{\text{th}} case is defined as

|  |  |  |
| --- | --- | --- |
|  | eℓ=|V(n,ℓ)V(b,ℓ)−1|,ℓ=1,2,…,6,e\_{\ell}=\left\lvert\frac{V^{(n,\ell)}}{V^{(b,\ell)}}-1\right\rvert,\ell=1,2,...,6, |  |

and the mean relative pricing error across all cases is given by

|  |  |  |
| --- | --- | --- |
|  | e¯=16​∑ℓ=16eℓ,\bar{e}=\frac{1}{6}\sum\_{\ell=1}^{6}e\_{\ell}, |  |

which measures the overall accuracy of both algorithms.

The proposed search algorithm is based on a grid-search strategy.
A predefined error threshold, denoted by ethe\_{\text{th}}, is specified, and the mean relative pricing error e¯\bar{e} is evaluated over a range of (B,N)(B,N) pairs.
The optimal parameter pair is identified as the smallest (B,N)(B,N) combination that satisfies the condition e¯⩽eth\bar{e}\leqslant e\_{\text{th}}.

The settings of the search algorithm are specified as follows: Bmin=10,Bmax=2000,δ​B=10,ιmin=0.1,ιmax=5.0,δ​ι=0.1B\_{\min}=10,B\_{\max}=2000,\delta B=10,\iota\_{\min}=0.1,\iota\_{\max}=5.0,\delta\iota=0.1. The error threshold is set to eth=2​basis points (bps)e\_{\text{th}}=2\,\,\text{basis points (bps)}.
For prudential considerations, financial institutions typically require that the pricing discrepancy between different algorithms for the same derivative contract should not exceed 2020−30-30 bps, depending on the contract type.
Hence, the selected threshold ethe\_{\text{th}} in this paper is intentionally more stringent than those adopted in practice. The optimal parameters obtained from the search algorithm are as follows:

* •

  B∗=360,ι∗=1.6,N∗=⌊ι∗​B∗⌋=576B^{\*}=360,\iota^{\*}=1.6,N^{\*}=\lfloor\iota^{\*}B^{\*}\rfloor=576 for CMA (with mean error e¯=1.9716\bar{e}=1.9716 bps);
* •

  B∗=40,ι∗=1.6,N∗=⌊ι∗​B∗⌋=64B^{\*}=40,\iota^{\*}=1.6,N^{\*}=\lfloor\iota^{\*}B^{\*}\rfloor=64 for SOA (with mean error e¯=1.9789\bar{e}=1.9789 bps).

After obtaining the optimal parameters, to further quantify the computational efficiency of SOA relative to CMA, we estimate the ratio tSOAtCMA\frac{t\_{\text{SOA}}}{t\_{\text{CMA}}} using the linear regression model without an intercept term ([3.5](https://arxiv.org/html/2512.16115v1#S3.E5 "In 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | tSOA=β​tCMA+ε.t\_{\rm SOA}=\beta t\_{\rm CMA}+\varepsilon. |  | (3.5) |

The specific results are shown in Figure [5](https://arxiv.org/html/2512.16115v1#S3.F5 "Figure 5 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and Table [3](https://arxiv.org/html/2512.16115v1#S3.T3 "Table 3 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform").
The data exhibit a statistically significant linear relationship, with an estimated slope of β^=0.2259\hat{\beta}=0.2259, indicating that the computational time required by SOA is, on average, approximately 22.59%22.59\% of that required by CMA.

Figure 5: Relationship between the Execution Times of SOA and CMA

![Refer to caption](Figures/OLSCompareTimeOfExecution.png)



Table 3: Regression Results for ([3.5](https://arxiv.org/html/2512.16115v1#S3.E5 "In 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"))

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Coefficient | Estimate | Standard Error | t−t-Statistic | p−p-Value | 95%95\% Confidence Interval |
| β\beta | 0.22590.2259 | 1.05×10−31.05\times 10^{-3} | 236.450236.450 | 4.4587×10−1384.4587\times 10^{-138} | [0.2485,0.2527][0.2485,0.2527] |

## 4 FFT for Multiple Options Pricing

### 4.1 FFT-based Framework

In this section, we integrate SOA with the fast Fourier transform (FFT). It is noteworthy that although FFT is also employed in [[9](https://arxiv.org/html/2512.16115v1#bib.bib9)], their formulation is designed for single option pricing tasks, whereas we generalizes the FFT-based algorithm to handle multiple options simultaneously. In detail, it is natural to consider the application of FFT for multiple-option pricing tasks, as these tasks involve evaluating a set of summations of the form in ([3.4](https://arxiv.org/html/2512.16115v1#S3.E4 "In 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")). However, the framework is applicable only when all options share identical attributes, with strike prices being the sole varying attribute. Under this condition, pricing the entire option portfolio becomes equivalent to computing a discrete Fourier transform (DFT), which can be efficiently accelerated by FFT.

Suppose there are LL options with identical attributes, differing only in their strike prices. Denote the logarithms of these strike prices by k~1,k~2,…,k~L\tilde{k}\_{1},\tilde{k}\_{2},...,\tilde{k}\_{L}. Let k¯,k¯∈ℝ\underline{k},\overline{k}\in\mathbb{R} be two numbers satisfying

|  |  |  |
| --- | --- | --- |
|  | k¯<kmin<kmax<k¯,\underline{k}<k\_{\min}<k\_{\max}<\overline{k}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | kmin=min⁡{k~1,k~2,…,k~L},kmax=max⁡{k~1,k~2,…,k~L}.k\_{\min}=\min\{\tilde{k}\_{1},\tilde{k}\_{2},\ldots,\tilde{k}\_{L}\},\,\,k\_{\max}=\max\{\tilde{k}\_{1},\tilde{k}\_{2},\ldots,\tilde{k}\_{L}\}. |  |

In other words, an interval [k¯,k¯,]\left[\underline{k},\overline{k},\right] is needed to encompass the range [kmin,kmax]\left[k\_{\min},k\_{\max}\right].
The lower bound k¯\underline{k} is specified by the model developer, whereas the upper bound k¯\overline{k} is determined adaptively according to the procedure described later.

For any log-strike price kk, the approximation in ([3.4](https://arxiv.org/html/2512.16115v1#S3.E4 "In 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(k)≈1π​∫0Be−i​z​k​η​(z)​𝑑z≈Δ​zπ​∑j=0N−1wj​e−i​j​k​Δ​z​η​(zj),\hat{V}(k)\approx\frac{1}{\pi}\int\_{0}^{B}e^{-izk}\eta(z)dz\approx\frac{\Delta z}{\pi}\sum\_{j=0}^{N-1}w\_{j}e^{-ijk\Delta z}\eta(z\_{j}), |  | (4.1) |

where NN cannot be chosen arbitrarily and must be determined according to specific considerations. For the moment, it is assumed that a suitable value of NN has been identified, with the grid spacing Δ​z=BN−1\Delta z=\frac{B}{N-1}.
The grid points for the log-strike prices are generated as

|  |  |  |
| --- | --- | --- |
|  | kn=k¯+n​Δ​k,n=0,1,…,N−1,k\_{n}=\underline{k}+n\Delta k,n=0,1,...,N-1, |  |

where the largest element, kN−1k\_{N-1}, corresponds to the upper bound k¯\overline{k} introduced earlier.
Applying ([4.1](https://arxiv.org/html/2512.16115v1#S4.E1 "In 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) to knk\_{n} yields

|  |  |  |
| --- | --- | --- |
|  | V^​(kn)≈Δ​zπ​∑j=0N−1wj​e−i​j​(k¯+n​Δ​k)​Δ​z​η​(zj)=∑j=0N−1e−i​Δ​k​Δ​z​n​j​[Δ​zπ​wj​e−i​j​k¯​Δ​z​η​(zj)].\displaystyle\hat{V}(k\_{n})\approx\frac{\Delta z}{\pi}\sum\_{j=0}^{N-1}w\_{j}e^{-ij(\underline{k}+n\Delta k)\Delta z}\eta(z\_{j})=\sum\_{j=0}^{N-1}e^{-i\Delta k\Delta znj}\left[\frac{\Delta z}{\pi}w\_{j}e^{-ij\underline{k}\Delta z}\eta(z\_{j})\right]. |  |

To ensure that the above expression exactly matches the form of DFT, the grid spacings must satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​k​Δ​z=2​πN.\Delta k\Delta z=\frac{2\pi}{N}. |  | (4.2) |

We then define

|  |  |  |
| --- | --- | --- |
|  | xj=Δ​zπ​wj​e−i​j​k¯​Δ​z​η​(zj),j=0,1,…,N−1.x\_{j}=\frac{\Delta z}{\pi}w\_{j}e^{-ij\underline{k}\Delta z}\eta(z\_{j}),j=0,1,...,N-1. |  |

Evaluating these summations can be accelerated by FFT, as {V^​(kn)}n=0N−1\left\{\hat{V}(k\_{n})\right\}\_{n=0}^{N-1} represents the NN-point DFT of {xn}n=0N−1\left\{x\_{n}\right\}\_{n=0}^{N-1}. Once {V^​(kn)}n=0N−1\left\{\hat{V}(k\_{n})\right\}\_{n=0}^{N-1} is obtained, offset terms are added back to recover the option prices on the corresponding log-strike grids {kn}n=0N−1\left\{k\_{n}\right\}\_{n=0}^{N-1}.

Two remaining issues must be addressed. First, the log-strike prices of the option portfolio, denoted by {k~ℓ}ℓ=0L\left\{\tilde{k}\_{\ell}\right\}\_{\ell=0}^{L}, do not coincide with the grid points {kn}n=0N−1\left\{k\_{n}\right\}\_{n=0}^{N-1}. To obtain prices at the desired strikes, linear interpolation is applied. Second, to ensure that the linear interpolation can be performed for all indices ℓ\ell, the upper bound of the strike grid must cover the maximum log-strike price. This requires that

|  |  |  |  |
| --- | --- | --- | --- |
|  | k¯=kN−1>kmax⟹k¯+(N−1)​Δ​k>kmax.\overline{k}=k\_{N-1}>k\_{\max}\Longrightarrow\underline{k}+(N-1)\Delta k>k\_{\max}. |  | (4.3) |

By ([4.2](https://arxiv.org/html/2512.16115v1#S4.E2 "In 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | k¯=k¯+(N−1)2N​2​πB>kmax.\overline{k}=\underline{k}+\frac{(N-1)^{2}}{N}\frac{2\pi}{B}>k\_{\max}. |  | (4.4) |

Inequality ([4.4](https://arxiv.org/html/2512.16115v1#S4.E4 "In 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) provides some insights into the efficiency of SOA when combined with FFT. Since SOA requires a smaller truncation point BB than CMA, its corresponding 2​πB\frac{2\pi}{B} is larger. Consequently, the minimum value of NN needed to satisfy ([4.4](https://arxiv.org/html/2512.16115v1#S4.E4 "In 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) is smaller for SOA, allowing its FFT computations to be completed faster.

Additionally, to mitigate potential numerical instabilities of the FFT near the boundaries, a symmetry constraint is imposed:

|  |  |  |  |
| --- | --- | --- | --- |
|  | kmin−k¯=k¯−kmax.k\_{\min}-\underline{k}=\overline{k}-k\_{\max}. |  | (4.5) |

Combining ([4.4](https://arxiv.org/html/2512.16115v1#S4.E4 "In 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) and ([4.5](https://arxiv.org/html/2512.16115v1#S4.E5 "In 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")) yields

|  |  |  |
| --- | --- | --- |
|  | k¯=12​[kmin+kmax−(N−1)2N​2​πB].\underline{k}=\frac{1}{2}\left[k\_{\min}+k\_{\max}-\frac{(N-1)^{2}}{N}\frac{2\pi}{B}\right]. |  |

The optimal parameters identified in section [3.2](https://arxiv.org/html/2512.16115v1#S3.SS2 "3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") are B∗=360B^{\*}=360, N∗=576N^{\*}=576 for CMA and B∗=40B^{\*}=40, N∗=64N^{\*}=64 for SOA. The previously determined optimal parameters B∗B^{\*} and N∗N^{\*} remain applicable, as they satisfy all the above conditions.

Figure 6: Relationship between Prices Computed by CMA-FFT and CMA-OBO

![Refer to caption](Figures/FFTPriceCMAPriceCompare.png)



Figure 7: Relationship between Prices Computed by SOA-FFT and SOA-OBO

![Refer to caption](Figures/FFTPriceSOAPriceCompare.png)

### 4.2 Numerical Experiments for the FFT-based Framework

The settings listed in Tables [1](https://arxiv.org/html/2512.16115v1#S3.T1 "Table 1 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [2](https://arxiv.org/html/2512.16115v1#S3.T2 "Table 2 ‣ 3.2 Numerical Experiments for SOA and CMA ‣ 3 SOA for Single Option Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") are retained for the numerical experiments, except that the strike price is now varied from 50.050.0 to 150.0150.0 with a step size of 1.01.0. This configuration generates a portfolio consisting of 101101 options, which are priced using the FFT-based framework.

To evaluate the accuracy of the FFT-based algorithms, two comparative analyses are conducted. The first comparison examines the pricing consistency between CMA-FFT and CMA-OBO (see Figure [6](https://arxiv.org/html/2512.16115v1#S4.F6 "Figure 6 ‣ 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")), while the second compares SOA-FFT with SOA-OBO (see Figure [7](https://arxiv.org/html/2512.16115v1#S4.F7 "Figure 7 ‣ 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform")).

To evaluate computational efficiency, the execution times of CMA-FFT, SOA-OBO, and SOA-FFT are measured. Two pairwise comparisons are examined: tSOA-OBOt\_{\text{SOA-OBO}} & tSOA-FFTt\_{\text{SOA-FFT}} and tCMA-FFTt\_{\text{CMA-FFT}} & tSOA-FFTt\_{\text{SOA-FFT}}.
The results are presented in Figures [8](https://arxiv.org/html/2512.16115v1#S4.F8 "Figure 8 ‣ 4.2 Numerical Experiments for the FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [9](https://arxiv.org/html/2512.16115v1#S4.F9 "Figure 9 ‣ 4.2 Numerical Experiments for the FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), respectively.

Two linear regression models (without intercept) are fitted to estimate the ratios

|  |  |  |  |
| --- | --- | --- | --- |
|  | tSOA-FFT=βB​tSOA-OBO+ε,\displaystyle t\_{\text{SOA-FFT}}=\beta\_{B}t\_{\text{SOA-OBO}}+\varepsilon, |  | (4.6) |
|  | tSOA-FFT=βC​tCMA-FFT+ε.\displaystyle t\_{\text{SOA-FFT}}=\beta\_{C}t\_{\text{CMA-FFT}}+\varepsilon. |  |

The FFT-based framework shows numerical instability when pricing out-of-the-money options. This is evidenced by Figure [6](https://arxiv.org/html/2512.16115v1#S4.F6 "Figure 6 ‣ 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [7](https://arxiv.org/html/2512.16115v1#S4.F7 "Figure 7 ‣ 4.1 FFT-based Framework ‣ 4 FFT for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), where data points corresponding to higher option values lie close to the 45−45-degree line, indicating strong agreement between FFT prices and those obtained via standard CMA or SOA. In contrast, data points with lower option values deviate substantially from the 45−45-degree line, revealing pronounced pricing errors in certain out-of-the-money cases.
Furthermore, the SOA integrated with FFT not only shortens the execution time by over 97% compared with the standard SOA, greatly improving computational efficiency, but also consistently outperforms CMA when combined with FFT, with the execution time of SOA-FFT being approximately 57.58% of that of CMA-FFT.

Figure 8: Relationship between tSOA-OBOt\_{\text{SOA-OBO}} and tSOA-FFTt\_{\text{SOA-FFT}}

![Refer to caption](Figures/OLSCompareTimeOfExecution_SOA_OBO.png)



Figure 9: Relationship between tCMA-FFTt\_{\text{CMA-FFT}} and tSOA-FFTt\_{\text{SOA-FFT}}

![Refer to caption](Figures/OLSCompareTimeOfExecution_CMA_SOA_FFT.png)

## 5 ML for Multiple Options Pricing

### 5.1 ML-based Framework

ML techniques have been extensively applied to option pricing, where a trained ML model maps a feature vector 𝒙\bm{x} representing the set of attributes influencing the option price to a scalar output p​(𝒙)p(\bm{x}), the option price. The proposed ML-based framework comprises two components: the training stage and the forecasting stage, as illustrated in Figure [10](https://arxiv.org/html/2512.16115v1#S5.F10 "Figure 10 ‣ 5.1 ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform").

Figure 10: The ML-based Framework

Training Stage

Random OptionContracts Generator{𝒙n}n=1N\{\bm{x}\_{n}\}\_{n=1}^{N}SOAPricer{yn}n=1N\{y\_{n}\}\_{n=1}^{N}TrainingDataset{𝒙n,yn}n=1N\{\bm{x}\_{n},y\_{n}\}\_{n=1}^{N}MLAlgorithmℳθ\mathcal{M}\_{\theta}

Forecasting Stage

New OptionContractsℳθ\mathcal{M}\_{\theta}TheoreticalPrices

The objective of the training stage is to construct the training dataset and train a ML model capable of accurately mapping any feature vector 𝒙\boldsymbol{x} to its corresponding option price yy.
A sufficient number of data points must be collected prior to model training. The SOA algorithm is used to generate synthetic option contracts.
The feature vectors incorporate all relevant attributes of the option contracts: the option type (European or digital), spot price S0S\_{0}, strike price KK, maturity TT, risk-free rate rr, and the parameters of the underlying stock price models (σ,κ,θ,ρ,V0,ν)(\sigma,\kappa,\theta,\rho,V\_{0},\nu).

However, some attributes operate on vastly different numerical scales. Attributes T,rT,r and the parameters of stock price models are typically smaller than 11, whereas S0S\_{0}, KK can reach much larger magnitudes. For example, the close price of NVIDIA stock on August 29, 2025 was $​174.18\mathdollar 174.18, and strike prices of call options on NVIDIA shares ranged from $5050 to $365365. Such discrepancies in scale must be mitigated to ensure that all attributes contribute comparably and to accelerate the convergence of optimization algorithms such as gradient descent.

To achieve this normalization, we fix the spot price at S0=1S\_{0}=1 and transform the strike price as K′=KS0K^{\prime}=\frac{K}{S\_{0}}. This procedure is equivalent to rescaling both S0S\_{0} and KK by the factor 1S0\frac{1}{S\_{0}}, ensuring that all attributes lie on comparable numerical scales. Correspondingly, the outcomes must also be rescaled: for European options, the rescaled prices are the actual prices multiplied by 1S0\frac{1}{S\_{0}}, whereas for digital options, rescaling leaves the prices unchanged.
Furthermore, the option type is encoded as a binary variable:

|  |  |  |
| --- | --- | --- |
|  | OpType={1, if the option is European,0, if the option is digital.\text{OpType}=\left\{\begin{aligned} &1,\text{\,\,if the option is European},\\ &0,\text{\,\,if the option is digital}.\end{aligned}\right. |  |

After rescaling S0S\_{0}, KK and encoding the option type, the resulting feature vector (denoted by 𝒙∈ℝ11\bm{x}\in\mathbb{R}^{11}) is

|  |  |  |
| --- | --- | --- |
|  | 𝒙=[OpType,K′,T,r,σ,κ,θ,ρ,V0,ν].\bm{x}=\left[\text{OpType},K^{\prime},T,r,\sigma,\kappa,\theta,\rho,V\_{0},\nu\right]. |  |

The outcome corresponding to each feature vector 𝒙\bm{x} (denoted by yy) represents the rescaled option price computed by SOA, which is adopted for its superior efficiency over CMA. The actual option price yactualy^{\text{actual}} can be recovered from yy through

|  |  |  |
| --- | --- | --- |
|  | yactual=[(S0−1)​OpType+1]​y.y^{\text{actual}}=\left[\left(S\_{0}-1\right)\text{OpType}+1\right]y. |  |

The feature vector 𝒙\bm{x} includes parameters from all stock price models, resulting in redundant elements for a given data point. For example, when the stock prices follow EVGP, only σ\sigma, θ\theta, and ν\nu are relevant, whereas κ\kappa, ρ\rho, and V0V\_{0} are redundant and thus are set to −1-1. Accordingly, for a European option under EVGP, the feature vector takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒙=[1,K′,T,r,σ,−1,θ,−1,−1,ν].\bm{x}=\left[1,K^{\prime},T,r,\sigma,-1,\theta,-1,-1,\nu\right]. |  | (5.1) |

Other combinations of option types and stock price models are handled analogously.

Data points are generated by the random option contract generator in Figure [10](https://arxiv.org/html/2512.16115v1#S5.F10 "Figure 10 ‣ 5.1 ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"). All option attributes are generated by random sampling. Specifically, OpType is drawn from a Bernoulli distribution, Bernoulli​(12)\text{Bernoulli}\left(\tfrac{1}{2}\right), ensuring an equal number of European and digital options in the dataset. For each remaining attribute, lower and upper bounds L¯\underline{L} and L¯\overline{L} are specified, and samples are drawn from a uniform distribution over the interval [L¯,L¯]\left[\underline{L},\overline{L}\right]. The bounds used in the numerical experiments are summarized in Table [4](https://arxiv.org/html/2512.16115v1#S5.T4 "Table 4 ‣ 5.1 ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform").

To ensure that the trained ML models achieve sufficiently small pricing errors across the entire input domain defined in Table [4](https://arxiv.org/html/2512.16115v1#S5.T4 "Table 4 ‣ 5.1 ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), a large number of data points are required. Accordingly, we generate Ntrain=2×106N^{\text{train}}=2\times 10^{6} feature vectors {𝒙n}n=1Ntrain\left\{\bm{x}\_{n}\right\}\_{n=1}^{N^{\text{train}}}, each associated with a target value yny\_{n} computed via the SOA pricer in Figure [10](https://arxiv.org/html/2512.16115v1#S5.F10 "Figure 10 ‣ 5.1 ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"). This yields the training dataset {𝒙n,yn}n=1Ntrain\left\{\bm{x}\_{n},y\_{n}\right\}\_{n=1}^{N^{\text{train}}}.

The test dataset is constructed in the same manner and contains Ntest=10000N^{\text{test}}=10000 options, and the forecasting stage aims to compute the prices of these options using the trained ML model ℳθ\mathcal{M}\_{\theta}. In practical applications, however, the test dataset corresponds to real option contracts observed in production environments rather than simulated data.

Table 4: Bounds of Input Variables in the Random Sampling

|  |  |  |
| --- | --- | --- |
| Input Variable | Lower Bound L¯\underline{L} | Upper Bound L¯\overline{L} |
| S0S\_{0} | 140.0140.0 | 160.0160.0 |
| KK | 0.95​S00.95S\_{0} | 1.05​S01.05S\_{0} |
| TT | 0 months (0.00)(0.00) | 1212 months (1.00)(1.00) |
| rr | 0.0%0.0\% | 5.0%5.0\% |
| σ\sigma | 0.000.00 | 0.200.20 |
| κ\kappa | 0.000.00 | 0.200.20 |
| θ\theta | 0.000.00 | 0.200.20 |
| ρ\rho | 0.000.00 | 0.200.20 |
| V0V\_{0} | 0.000.00 | 0.200.20 |
| ν\nu | 0.000.00 | 0.200.20 |

### 5.2 Numerical Experiments for the ML-based Framework

#### 5.2.1 Training Neural Networks

An NN takes a feature vector 𝒙\bm{x} as input and transforms it into an output through a sequence of weighted linear operations and nonlinear activation functions. Various activation functions have been proposed in the literature, each introducing different forms of nonlinearity,
and the Leaky ReLU function is adopted in this paper. For vector inputs, SS is applied elementwise. The architecture of the NN employed in the numerical experiments comprises 11 layers in total, which includes one input dense layer with an input dimension of 11, five hidden dense layers, five Leaky ReLU activation layers, and one output dense layer with an output dimension of 1. Each of the hidden dense layers is configured with 128 neurons.

To train the NN efficiently, the mini-batch gradient descent algorithm is employed with a batch size of 256256.
The training process spans 30003000 epochs to ensure sufficient convergence.
To ensure numerical stability and attain high predictive accuracy, a carefully tuned learning rate schedule is employed. The initial learning rate is set to 3×10−63\times 10^{-6} and is decayed by a factor of 0.10.1 after every 500500 training epochs.
This configuration enables gradual and precise updates of the NN parameters during optimization.

Figure [11](https://arxiv.org/html/2512.16115v1#S5.F11 "Figure 11 ‣ 5.2.1 Training Neural Networks ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") illustrates the evolution of the mean MSE loss throughout the training process.For each epoch, the mean MSE loss is calculated as the average of the MSE losses across all mini-batches. As expected, the loss exhibits a consistent downward trend, indicating effective learning and stable convergence.
Once the NN is fully trained, it is applied to forecast out-of-sample option prices for data points in the test dataset.
These predicted prices are then compared with the true values obtained from the SOA. As shown in Figure [12](https://arxiv.org/html/2512.16115v1#S5.F12 "Figure 12 ‣ 5.2.1 Training Neural Networks ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), nearly all points lie close to the 45−45-degree line,
demonstrating that the predictions align closely with the actual outcomes and confirming the high accuracy of the NN.

Figure 11: Mean MSE Losses of All Epochs (Log Scale)

![Refer to caption](Figures/MLNNMeanMSE.png)



Figure 12: Out-of-sample Relationship between NN Predicted Prices and SOA Actual Prices

![Refer to caption](Figures/MLNNPriceCompare.png)

To measure the accuracy, let y^n\hat{y}\_{n} and ynactualy^{\text{actual}}\_{n} be the nthn^{\text{th}} predicted and actual prices of the nthn^{\text{th}} option in the test dataset, respectively, where n=1,2,…,Ntestn=1,2,...,N^{\text{test}}. Then for any ML model, the absolute pricing error is defined as

|  |  |  |
| --- | --- | --- |
|  | absolute pricing error=1Ntest​∑n=1Ntest(y^n−ynactual)2,\text{absolute pricing error}=\sqrt{\frac{1}{N^{\text{test}}}\sum\_{n=1}^{N^{\text{test}}}\left(\hat{y}\_{n}-y^{\text{actual}}\_{n}\right)^{2}}, |  |

and the relative pricing error is defined as

|  |  |  |
| --- | --- | --- |
|  | relative pricing error=1Ntest​∑n=1Ntest|y^nynactual−1|.\text{relative pricing error}=\frac{1}{N^{\text{test}}}\sum\_{n=1}^{N^{\text{test}}}\left\lvert\frac{\hat{y}\_{n}}{y^{\text{actual}}\_{n}}-1\right\rvert. |  |

For the fully trained NN, the absolute and relative pricing errors are 0.00090.0009 and 0.0417%0.0417\%, respectively.

#### 5.2.2 Training Ensemble Learning Models: Bagging and Boosting

Ensemble learning algorithms that utilize decision trees (DTs) as weak learners can generally be classified into two main categories: bagging and boosting. In this study, both approaches are examined. RFs represent the bagging paradigm, and GBDTs represent the boosting paradigm.

Overfitting and underfitting in RFs and GBDTs can be effectively mitigated by controlling the maximum depth of individual decision trees, which serves as a key hyperparameter. Shallow trees may fail to capture the underlying data patterns adequately, leading to underfitting. But excessively deep trees risk overfitting and substantially increasing computational costs.
To balance the model complexity and the generalization capability, the optimal value of the maximum depth is determined through grid search combined with cross-validation. The results indicate that the optimal maximum depth is 2020 for RF and 1515 for GBDT.
Figure [13](https://arxiv.org/html/2512.16115v1#S5.F13 "Figure 13 ‣ 5.2.2 Training Ensemble Learning Models: Bagging and Boosting ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [14](https://arxiv.org/html/2512.16115v1#S5.F14 "Figure 14 ‣ 5.2.2 Training Ensemble Learning Models: Bagging and Boosting ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") illustrate the relationship between the mean MSE loss obtained from cross-validation and the corresponding maximum depth.
As shown in these figures, increasing the maximum depth beyond 2020 for RF or 1515 for GBDT yields no substantial improvement in the mean MSE loss. In some cases, it even leads to worse mean MSE values due to overfitting.

Figure 13: Relationship between Cross-Validation MSE Loss (Log Scale) and RF Max Depth

![Refer to caption](Figures/MLRFCV.png)



Figure 14: Relationship between Cross-Validation MSE Loss (Log Scale) and GBDT Max Depth

![Refer to caption](Figures/MLGBDTCV.png)

During the training of RFs and GBDTs, the number of weak learners is set to 100100. The bootstrapping hyperparameter is fixed at 0.70.7, indicating that each weak learner is trained on a randomly selected subset comprising 70% of the total training dataset (0.7​Ntrain0.7N^{\text{train}}). Figure [15](https://arxiv.org/html/2512.16115v1#S5.F15 "Figure 15 ‣ 5.2.2 Training Ensemble Learning Models: Bagging and Boosting ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") compares the prices predicted by RF with those computed by SOA, while Figure [16](https://arxiv.org/html/2512.16115v1#S5.F16 "Figure 16 ‣ 5.2.2 Training Ensemble Learning Models: Bagging and Boosting ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") presents analogous results for GBDT. Both RF and GBDT exhibit high predictive accuracy for out-of-sample data. Consistent with the NN results, nearly all data points in Figure [15](https://arxiv.org/html/2512.16115v1#S5.F15 "Figure 15 ‣ 5.2.2 Training Ensemble Learning Models: Bagging and Boosting ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [16](https://arxiv.org/html/2512.16115v1#S5.F16 "Figure 16 ‣ 5.2.2 Training Ensemble Learning Models: Bagging and Boosting ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") lie close to the 45−45-degree line, confirming strong agreement between predicted and actual prices.

The absolute pricing errors are 0.00440.0044 for RF and 0.00080.0008 for GBDT, while the corresponding relative pricing errors are 0.1884%0.1884\% and 0.0668%0.0668\%, respectively.

Figure 15: Out-of-sample Relationship between RF Predicted Prices and SOA Actual Prices

![Refer to caption](Figures/MLRFPriceCompare.png)



Figure 16: Out-of-sample Relationship between GBDT Predicted Prices and SOA Actual Prices

![Refer to caption](Figures/MLGBDTPriceCompare.png)

#### 5.2.3 Execution Times

The execution times of the three ML algorithms are compared against that of SOA. The execution time of each algorithm is defined as the total time required to price all 1000010000 options in the test dataset. To mitigate the influence of hardware-induced randomness, the pricing process for the entire test dataset is repeated 100100 times for each algorithm.
Figure [17](https://arxiv.org/html/2512.16115v1#S5.F17 "Figure 17 ‣ 5.2.3 Execution Times ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"), [18](https://arxiv.org/html/2512.16115v1#S5.F18 "Figure 18 ‣ 5.2.3 Execution Times ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") and [19](https://arxiv.org/html/2512.16115v1#S5.F19 "Figure 19 ‣ 5.2.3 Execution Times ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") present the comparative execution times of NN, RF, and GBDT relative to standard SOA, respectively.

Figure 17: Relationship between NN Execution Time and SOA Execution Time

![Refer to caption](Figures/MLNeuralNetworkTimeOfExecution.png)



Figure 18: Relationship between RF Execution Time and SOA Execution Time

![Refer to caption](Figures/MLRandomForestTimeOfExecution.png)



Figure 19: Relationship between GBDT Execution Time and SOA Execution Time

![Refer to caption](Figures/MLGradientBoostingTimeOfExecution.png)

Let tNN,tRF,tGBDTt\_{\text{NN}},t\_{\text{RF}},t\_{\text{GBDT}} and tSOAt\_{\text{SOA}} be the execution times of NN, RF, GBDT, and SOA, respectively.
To quantify their relative computational efficiency, three linear regression models (without intercept) are fitted to estimate tNNtSOA\frac{t\_{\text{NN}}}{t\_{\text{SOA}}}, tRFtSOA\frac{t\_{\text{RF}}}{t\_{\text{SOA}}} and tGBDTtSOA\frac{t\_{\text{GBDT}}}{t\_{\text{SOA}}}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | tNN=βA​tSOA+ε,\displaystyle t\_{\text{NN}}=\beta\_{A}t\_{\text{SOA}}+\varepsilon, |  | (5.2) |
|  |  | tRF=βB​tSOA+ε,\displaystyle t\_{\text{RF}}=\beta\_{B}t\_{\text{SOA}}+\varepsilon, |  |
|  |  | tGBDT=βC​tSOA+ε.\displaystyle t\_{\text{GBDT}}=\beta\_{C}t\_{\text{SOA}}+\varepsilon. |  |

Regression results are summarized in Table [5](https://arxiv.org/html/2512.16115v1#S5.T5 "Table 5 ‣ 5.2.3 Execution Times ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"). The findings indicate that the execution times of NN, RF, and GBDT are approximately 0.18%,13.91%0.18\%,13.91\% and 3.81%3.81\% of SOA, respectively.
Accordingly, the improvements in computational efficiency are 99.82%99.82\% for NN, 86.09%86.09\% for RF and 96.19%96.19\% for GBDT.
All estimated regression coefficients are statistically significant and exhibit narrow confidence intervals, confirming the robustness and reliability of these results.

Table 5: Regression Results for ([5.2](https://arxiv.org/html/2512.16115v1#S5.E2 "In 5.2.3 Execution Times ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform"))

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Coefficient | Estimate | Standard Error | t−t-Statistic | p−p-Value | 95%95\% Confidence Interval |  |
| βA\beta\_{A} | 0.00180.0018 | 1.57×10−51.57\times 10^{-5} | 112.034112.034 | 4.3076×10−1064.3076\times 10^{-106} | [0.0017,0.0018][0.0017,0.0018] |  |
| βB\beta\_{B} | 0.13910.1391 | 1.07×10−31.07\times 10^{-3} | 129.181129.181 | 3.5673×10−1123.5673\times 10^{-112} | [0.1370,0.1413][0.1370,0.1413] |  |
| βC\beta\_{C} | 0.03810.0381 | 3.44×10−43.44\times 10^{-4} | 110.521110.521 | 1.6368×10−1051.6368\times 10^{-105} | [0.0374,0.0387][0.0374,0.0387] |  |

Table [6](https://arxiv.org/html/2512.16115v1#S5.T6 "Table 6 ‣ 5.2.3 Execution Times ‣ 5.2 Numerical Experiments for the ML-based Framework ‣ 5 ML for Multiple Options Pricing ‣ An Efficient Machine Learning Framework for Option Pricing via Fourier Transform") summarizes the performance of the three ML algorithms, including their absolute pricing errors, relative pricing errors, and execution times.
Among the evaluated algorithms, NN demonstrates the lowest absolute and relative pricing errors. It achieves computational efficiency comparable to the FFT-based framework which achieves an improvement in execution time of approximately 97.12%97.12\%.
While NNs demonstrate outstanding predictive performance and fast execution speed, their training process is considerably more computationally demanding than RF or GBDT. In comparison, GBDTs achieve similar gains in execution efficiency with much lower training complexity. Furthermore, GBDTs offer superior model interpretability and enhanced control over overfitting relative to NNs.
Therefore, both NN and GBDT are recommended for real-world applications, depending on the specific requirements and hardware availability.
When a sufficient number of data points are available and Graphics Processing Unit (GPU) resources are abundant, NN is undoubtedly the preferred choice. Otherwise, it is advisable for model developers to place greater emphasis on GBDT.

Table 6: Performances of Three ML Algorithms

|  |  |  |  |
| --- | --- | --- | --- |
| ML Algorithm | Absolute Pricing Error | Relative Pricing Error | Improvement in Execution Time |
| NN | 0.00050.0005 | 4.174.17 bps | 99.82% |
| RF | 0.00440.0044 | 18.8418.84 bps | 86.09% |
| GBDT | 0.00080.0008 | 6.686.68 bps | 96.19% |

While the FFT-based framework also delivers high computational speed, the ML-based framework demonstrates superior numerical stability and pricing accuracy.
Furthermore, the ML-based framework is less restrictive regarding input option attributes than the FFT-based framework.
Overall, the results indicate that the ML-based framework provides the most balanced performance between accuracy and efficiency, making it the most suitable approach for large-scale option pricing applications based on the FT.

## 6 Conclusions

This paper presents an efficient ML-based framework for multiple option pricing tasks where the options are path-independent and the underlying stock prices follow exponential Lévy processes.
The data generation is performed using an improved FT-based algorithm, termed SOA, developed as an enhancement of CMA. SOA leverages the theoretical relationship between the smoothness of a function and the tail decay rate of its FT, introducing a smooth offset term that replaces the original offset in CMA.
This modification substantially reduces computational cost while preserving pricing accuracy, making SOA particularly suitable for efficiently computing the outcomes for feature vectors in the large-scale datasets in the ML workflow.

Numerical experiments across two option types (European and digital) and three stock price models (GBM, HM, and EVGP) empirically confirm that SOA is substantially more efficient than CMA, typically requiring only 60%−70%60\%-70\% of the execution time of CMA under equivalent error tolerances.
The proposed ML-based framework further enhances flexibility and robustness. Three ML algorithms including NN, RF and GBDT are trained on the SOA-generated dataset. Comparative analyses indicate that all three models achieve high accuracy.
NN achieves the highest accuracy and the greatest improvement in execution time. Although GBDT exhibits slightly lower accuracy and a longer execution time than the NN, it strikes an effective balance among precision, interpretability, and computational efficiency. The selection between GBDT and NN should be guided by the nature of the task and the computational capabilities of the available hardware.
Although an alternative FFT-based framework provides computational acceleration through the FFT and represents a natural extension of SOA (or CMA), it suffers from numerical instability for deep out-of-the-money options and imposes strict requirements on input option attributes.
The ML-based framework overcomes these limitations, making it particularly suitable for practical deployment in financial institutions that price large and heterogeneous option portfolios.

## Acknowledgments

The authors would like to express their appreciation to the referees for their useful comments and the editors. Liying Zhang is supported by the National Natural Science Foundation of China (No. 11601514 and No. 11971458), the Fundamental Research Funds for the Central Universities (No. 2023ZKPYL02 and No. 2023JCCXLX01) and the Yueqi Youth Scholar Research Funds for the China University of Mining and Technology-Beijing (No. 2020YQLX03).

## References

* [1]
   Ballotta L, Kyriakou I. Monte Carlo simulation of the CGMY process and option pricing[J]. Journal of Futures Markets, 2014, 34(12), 1095–1121.
* [2]
   Black F, Scholes M. The pricing of options and corporate liabilities[J]. Journal of Political
  Economy, 1973, 81(3), 637–654.
* [3]
   Boyle P P. A lattice framework for option pricing with two state variables[J]. Journal of Financial and Quantitative Analysis, 1988, 23(1), 1–12.
* [4]
   Brennan M J, Schwartz E S. Finite difference methods and jump processes arising in the pricing of contingent claims: A synthesis[J]. Journal of Financial and Quantitative Analysis, 1978, 13(3), 461–474.
* [5]
   Broadie M, Kaya Ö. Exact simulation of stochastic volatility and other affine jump diffusion processes[J]. Operations Research, 2006, 54(2), 217–231.
* [6]
   Carr P, Geman H, Madan D B and Yor M. The fine structure of asset returns: an empirical investigation[J]. The Journal of Business, 2002, 75(2), 305–332.
* [7]
   Carr P, Madan D. Option valuation using the fast fourier transform[J]. Journal of Com-putational Finance, 1999, 2(4), 61–73.
* [8]
   Cox J C, Ross S A, Rubinstein M. Option pricing: a simplified approach[J]. Journal
  of Financial Economics, 1979, 7(3), 229–263.
* [9]
   Derman E, Kani I. The volatility smile and its implied tree[J]. Goldman Sachs Quantitative Strategies Research Notes, 1994, 2, 45–60.
* [10]
   Elbrächter D, Grohs P, Jentzen A, Schwab C. DNN expression rate analysis of high-dimensional pdes: application to option pricing[J]. Constructive Approximation, 2022, 55(1), 3–71.
* [11]
   Ferguson R, Green A. Deeply learning derivatives. arXiv:1809.02233, 2018.
* [12]
   Genlöv Brouwer C. Numerical investigation of the deep bsde solver for pricing European options[J]. 2025.
* [13]
   Heston S L. A closed-form solution for options with stochastic volatility with applications to bond and currency options[J]. The Review of Financial Studies, 1993, 6(2), 327–343.
* [14]
   Hirsa A. Computational methods in finance[M]. Chemical Rubber Company Press, 2012.
* [15]
   Hutchinson J M, Lo A W, Poggio T. A nonparametric approach to pricing and hedging derivative securities via learning networks[J]. The Journal of Finance, 1994, 49(3), 851–889.
* [16]
   Jeon Y, Mccurdy T H, Zhao X. News as sources of jumps in stock returns: Evidence from 21 million news articles for 9000 companies[J]. Journal of Financial Economics, 2022, 145(2), 1–17.
* [17]
   Li Z, Huang Q. Option pricing using ensemble learning. arXiv:2506.05799, 2025.
* [18]
   Lux T, Marchesi M. Volatility clustering in financial markets: a microsimulation of
  interacting agents[J]. International Journal of Theoretical and Applied Finance, 2000, 3(04), 675–702.
* [19]
   Madan D B, Carr P P, Chang E C. The variance gamma process and option pricing[J].
  Review of Finance, 1998, 2(1), 79–105.
* [20]
   Merton R C. Option pricing when underlying stock returns are discontinuous[J]. Journal of
  Financial Economics, 1976 ,3(1-2), 125–144.
* [21]
   Patel R G. Efficient deep learning methods for solving high-dimensional partial differential equations for applications in option pricing[D]. University of Toronto (Canada), 2022.
* [22]
   Poirot J, Tankov P. Monte carlo option pricing for tempered stable (CGMY) processes[J]. Asia-Pacific Financial Markets, 2006, 13(4), 327–344.
* [23]
   Rachev S T, Kim Y S. Bianchi, M. L. and Fabozzi, F. J. Financial models with Lévy processes and volatility clustering[M]. John Wiley and Sons, 2011.
* [24]
   Rapuch G. American options and the free boundary exercise region: a PDE approach[J]. Interfaces and Free Boundaries, 2005, 7(1), 79–98.
* [25]
  Stein E M, Shakarchi R. Fourier analysis: an introduction[M]. Princeton: Princeton University Press, 2003.
* [26]
   Wang X, Li J, Li J. A deep learning based numerical PDE method for option pricing[J]. Computational Economics, 2023, 62(1), 149–164.