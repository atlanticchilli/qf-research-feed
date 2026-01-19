---
authors:
- Rushikesh Handal
- Masanori Hirano
doc_id: arxiv:2601.11097v1
family_id: arxiv:2601.11097
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold
  Network-Based BSDE Solver'
url_abs: http://arxiv.org/abs/2601.11097v1
url_html: https://arxiv.org/html/2601.11097v1
venue: arXiv q-fin
version: 1
year: 2026
---


Rushikesh Handal
Preferred Networks, Inc.TokyoJapan
 and 
Masanori Hirano
[research@mhirano.jp](mailto:research@mhirano.jp)
[0000-0001-5883-8250](https://orcid.org/0000-0001-5883-8250 "ORCID identifier")
Preferred Networks, Inc.TokyoJapan

(2025)

###### Abstract.

High-dimensional option pricing and hedging present significant challenges in quantitative finance, where traditional PDE-based methods struggle with the curse of dimensionality. The BSDE framework offers a computationally efficient alternative to PDE-based methods, and recently proposed deep BSDE solvers, generally utilizing conventional Multi-Layer Perceptrons (MLPs), build upon this framework to provide a scalable alternative to numerical BSDE solvers. In this research, we show that although such MLP-based deep BSDEs demonstrate promising results in option pricing, there remains room for improvement regarding hedging performance. To address this issue, we introduce KANHedge, a novel BSDE-based hedger that leverages Kolmogorov-Arnold Networks (KANs) within the BSDE framework. Unlike conventional MLP approaches that use fixed activation functions, KANs employ learnable B-spline activation functions that provide enhanced function approximation capabilities for continuous derivatives. We comprehensively evaluate KANHedge on both European and American basket options across multiple dimensions and market conditions. Our experimental results demonstrate that while KANHedge and MLP achieve comparable pricing accuracy, KANHedge provides improved hedging performance. Specifically, KANHedge achieves considerable reductions in hedging cost metrics, demonstrating enhanced risk control capabilities.

BSDE, Option Pricing and Hedging, Kolmogorov-Arnold Networks

††copyright: acmlicensed††journalyear: 2025††doi: XXXXXXX.XXXXXXX††conference: ; ; ††ccs: Applied computing Economics††ccs: Computing methodologies Neural networks††ccs: Mathematics of computing Markov processes

## 1. Introduction

Financial derivatives, particularly options, are fundamental instruments in modern quantitative finance, providing essential mechanisms for risk management, portfolio optimization, and hedging strategies. These financial contracts grant holders specific rights to trade underlying assets under predetermined conditions, making their accurate valuation and effective hedging critical for financial institutions and market participants (Black and Scholes, [1973](https://arxiv.org/html/2601.11097v1#bib.bib11 "The pricing of options and corporate liabilities")). The complexity of modern financial markets demands sophisticated approaches to derivative pricing, especially when dealing with high-dimensional options where the computational burden increases substantially with the number of underlying state variables.

The classical approach to option pricing, as established by Black and Scholes (Black and Scholes, [1973](https://arxiv.org/html/2601.11097v1#bib.bib11 "The pricing of options and corporate liabilities")), formulates the problem as a partial differential equation (PDE). While this framework works well for simple, single-dimensional problems, real-world financial applications often involve high-dimensional scenarios, such as basket options that depend on multiple underlying assets. In such cases, traditional PDE-based methods face the ”curse of dimensionality,” where computational complexity grows exponentially with the number of dimensions, making direct numerical solutions intractable (Bellman, [1966](https://arxiv.org/html/2601.11097v1#bib.bib17 "Dynamic programming")).

To address the curse of dimensionality, the Backward Stochastic Differential Equation (BSDE) formulation has emerged as a powerful alternative approach (Pardoux and Peng, [1992](https://arxiv.org/html/2601.11097v1#bib.bib25 "Backward stochastic differential equations and quasilinear parabolic partial differential equations")). The BSDE framework, connected to PDEs through the Feynman-Kac theorem, transforms the pricing problem into a stochastic optimization problem that avoids explicit computation of high-dimensional Hessian matrices. Traditional numerical methods for BSDEs, such as finite difference schemes (e.g., (Teng and Zhao, [2021](https://arxiv.org/html/2601.11097v1#bib.bib18 "High-order combined multi-step scheme for solving forward backward stochastic differential equations"))) and regression-based approaches (e.g., (Gobet et al., [2005](https://arxiv.org/html/2601.11097v1#bib.bib19 "A regression-based monte carlo method to solve backward stochastic differential equations"))), have shown some success but still face limitations with respect to convergence when the number of dimensions increases (Bellman, [1966](https://arxiv.org/html/2601.11097v1#bib.bib17 "Dynamic programming")), (Lemor et al., [2006](https://arxiv.org/html/2601.11097v1#bib.bib20 "Rate of convergence of an empirical regression method for solving generalized backward stochastic differential equations")).

Recent advances in machine learning have revolutionized the BSDE approach to high-dimensional option pricing. One such machine learning approach is the Multi-Layer Perceptron (MLP) based methods, part of a family of models called Deep BSDEs, which have shown promising results in pricing high-dimensional options (Han et al., [2018](https://arxiv.org/html/2601.11097v1#bib.bib1 "Solving high-dimensional partial differential equations using deep learning"); Huré et al., [2020](https://arxiv.org/html/2601.11097v1#bib.bib4 "Deep backward schemes for high-dimensional nonlinear pdes")), particularly in their ability to directly estimate the option’s delta (price sensitivity) either as a direct model output (Han et al., [2018](https://arxiv.org/html/2601.11097v1#bib.bib1 "Solving high-dimensional partial differential equations using deep learning")) or by using automatic differentiation capabilities of MLPs (Raissi, [2024](https://arxiv.org/html/2601.11097v1#bib.bib21 "Forward–backward stochastic neural networks: deep learning of high-dimensional partial differential equations")), which is essential for dynamic hedging strategies. These deep learning methods can effectively handle the curse of dimensionality by parameterizing the solution functions with neural networks, enabling practical solutions to previously intractable problems.

Other types of architectures like Recurrent Neural Networks (RNNs) (Chan-Wai-Nam et al., [2019](https://arxiv.org/html/2601.11097v1#bib.bib26 "Machine learning for semi linear pdes"); Kapllani and Teng, [2024](https://arxiv.org/html/2601.11097v1#bib.bib27 "Deep learning algorithms for solving high-dimensional nonlinear backward stochastic differential equations")) or Long Short-Term Memory (LSTM) networks (Kapllani and Teng, [2024](https://arxiv.org/html/2601.11097v1#bib.bib27 "Deep learning algorithms for solving high-dimensional nonlinear backward stochastic differential equations")) have been utilized to replace standard MLPs to solve the general form of BSDEs. (Kapllani and Teng, [2024](https://arxiv.org/html/2601.11097v1#bib.bib27 "Deep learning algorithms for solving high-dimensional nonlinear backward stochastic differential equations")) find that neither RNNs nor LSTMs improve the accuracy of the BSDE solution, i.e., the initial value of the solution corresponding to the underlying PDE (option price in the case of option-related PDEs). Furthermore, they find that in the case of LSTMs, the approximation error increases, which they attribute to the fact that LSTMs violate the Markovian property of BSDEs. Similar arguments can be made about any attention-based model based on (Vaswani et al., [2023](https://arxiv.org/html/2601.11097v1#bib.bib28 "Attention is all you need")) or convolutional neural network based model used in (Widianto et al., [2023](https://arxiv.org/html/2601.11097v1#bib.bib30 "European high-dimensional option pricing using backward stochastic differential equation-based convolutional neural network")) that utilize sequences of past information. Hence, in this research we focus on the simpler and often used MLPs as the baseline architecture in Deep BSDEs.

Despite being successful at estimating option prices, Deep BSDEs face significant limitations when it comes to estimating the deltas required for effective hedging. Obtaining precise delta information from neural networks remains problematic regardless of the estimation approach used. Methods that rely on automatic differentiation for delta calculation (Raissi, [2024](https://arxiv.org/html/2601.11097v1#bib.bib21 "Forward–backward stochastic neural networks: deep learning of high-dimensional partial differential equations")) do not guarantee smooth delta estimates, which is also highlighted in their work. Barring special cases like digital options or barrier options, a smooth delta is required for stable hedging; otherwise leading to gamma spikes. While approaches that directly model deltas using MLPs (Han et al., [2018](https://arxiv.org/html/2601.11097v1#bib.bib1 "Solving high-dimensional partial differential equations using deep learning")) offer better control compared to automatic differentiation, the accuracy from the option pricing task does not translate into accurate delta estimation (Hientzsch, [2019](https://arxiv.org/html/2601.11097v1#bib.bib29 "Introduction to solving quant finance problems with time-stepped fbsde and deep learning")). Thus, efficient hedging is still an open issue when it comes to Deep BSDE solvers.

Compared to MLPs, Kolmogorov-Arnold Networks (KANs), recently introduced in the literature (Liu et al., [2025](https://arxiv.org/html/2601.11097v1#bib.bib5 "KAN: kolmogorov-arnold networks")), offer a fundamentally different approach to functional approximation based on the Kolmogorov-Arnold representation theorem. Unlike MLPs that rely on fixed activation functions with learnable weights, KANs employ learnable activation functions (typically B-splines) on the edges of the network, providing enhanced flexibility for continuous function modeling. This architectural design is particularly well-suited for delta estimation, as KANs naturally produce smoother derivatives and, more generally, more accurate approximations for continuous functions (Liu et al., [2025](https://arxiv.org/html/2601.11097v1#bib.bib5 "KAN: kolmogorov-arnold networks")).

In this work, we introduce KANHedge, a novel method that leverages KANs for solving high-dimensional option pricing and hedging problems via the BSDE methodology. The major architectural difference with MLP-based Deep BSDE solvers such as in (Han et al., [2018](https://arxiv.org/html/2601.11097v1#bib.bib1 "Solving high-dimensional partial differential equations using deep learning")) is that at each intermediate time step, we model the option’s delta using a KAN. The central research question we aim to answer in this work is: Does KANHedge provide improved hedging performance compared to conventional MLP-based BSDE solvers in high-dimensional settings?

To answer the research question, we conduct option pricing and hedging experiments using both high-dimensional European and American-style basket options with varying market conditions and dimensions. We find that although both MLP-based Deep BSDE solvers and KANHedge lead to similar option pricing accuracy with pricing errors below 1%1\%, the hedging performance of KANHedge is better across all experimental settings. Utilizing the deltas estimated at each time step, we rely on a pure delta hedging strategy to derive the hedging cost distribution. In our set of experiments, KANHedge results in up to 9%9\% improvements across the hedging cost metrics, measured using the conditional value at risk utility function. This improved performance of KANHedge can be attributed to improved delta estimation at each discrete time step.

## 2. Related Work

Option pricing and hedging have been addressed through several distinct methodological approaches, each with specific advantages and limitations that inform our work. In this section, we focus on related research that combine machine learning aspects with conventional pricing and hedging tasks.

PDE-Based Approaches: Recent advances in solving high-dimensional PDEs have enabled efficient option pricing beyond traditional finite difference or tree-based methods. The Deep Parametric PDE Method (Glau and Wunderlich, [2022](https://arxiv.org/html/2601.11097v1#bib.bib24 "The deep parametric pde method and applications to option pricing")) enables efficient option pricing across high-dimensional parameter spaces by training neural networks on families of PDEs. Similarly, the Deep Galerkin Method (Sirignano and Spiliopoulos, [2018](https://arxiv.org/html/2601.11097v1#bib.bib23 "DGM: a deep learning algorithm for solving partial differential equations")) provides a mesh-free approach to solve high-dimensional option pricing PDEs using deep learning. However, generally, PDE-based solvers face challenges in ensuring accuracy, generalization, and training efficiency, with empirical studies concluding that BSDE-based methods offer superior price estimates compared to PDE-solvers across various settings (Assabumrungrat et al., [2023](https://arxiv.org/html/2601.11097v1#bib.bib14 "Error analysis of option pricing via deep pde solvers: empirical study")). Our proposed KANHedge model falls into this BSDE category, offering the computational advantages of this approach.

Direct Hedging Approaches: Alternative methodologies such as (Buehler et al., [2019](https://arxiv.org/html/2601.11097v1#bib.bib3 "Deep hedging"); Hirano et al., [2023](https://arxiv.org/html/2601.11097v1#bib.bib22 "Adversarial deep hedging: learning to hedge without price process modeling")) directly model the hedging output at each time step, enabling estimation of optimal hedging strategies and option prices based on a variety of issuer-specific target utility functions. These approaches can be extended to higher-dimensional settings for basket option pricing and delta computation. However, these studies primarily target European-style options and their applicability to American-style options, where early exercise estimation is crucial in addition to delta computation, is not straightforward. In contrast to these methods, KANHedge, which incorporates criteria for early execution of the option, offers more straightforward applicability to American-style options.

KAN-based PDE solvers: The seminal work in (Liu et al., [2025](https://arxiv.org/html/2601.11097v1#bib.bib5 "KAN: kolmogorov-arnold networks")) demonstrated the potential of KANs in solving PDEs using a simple Poisson equation. (Wang et al., [2025](https://arxiv.org/html/2601.11097v1#bib.bib31 "Kolmogorov–arnold-informed neural network: a physics-informed deep learning framework for solving forward and inverse problems based on kolmogorov–arnold networks")) combined KANs with physics-informed neural networks to solve PDEs in computational mechanics, where they find that KANs significantly outperform MLPs in terms of accuracy. Compared to these PDE solvers, KANHedge enjoys the simplicity of BSDEs and, to the best of our knowledge, is among the early applications of KANs in BSDE solving.

KAN-based Option Pricing: Although KAN architecture is proposed recently, initial studies have begun applying KANs to option pricing. (Handal et al., [2024](https://arxiv.org/html/2601.11097v1#bib.bib13 "KANOP: a data-efficient option pricing model using kolmogorov-arnold networks")) replaces the basis functions used in conventional Least Square Monte Carlo (LSMC) methodology with a KAN network to price American-style options. While their approach provides improved price estimates, they only apply it to pricing tasks with a single underlying asset. Furthermore, its applicability as a hedging tool remains unstudied. Compared to their approach, KANHedge extends naturally to higher-dimensional settings and provides both pricing and hedging capabilities through the BSDE framework.

## 3. Foundational Mathematics

This section establishes the mathematical framework underlying our approach, progressing from general PDE formulations to the BSDE methodology that enables our KAN-based solution.

Following notation from (Han et al., [2018](https://arxiv.org/html/2601.11097v1#bib.bib1 "Solving high-dimensional partial differential equations using deep learning")), we consider a general class of semilinear parabolic PDEs of the form:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | ∂u∂t+12​tr​(Γ​ΓT​∇2u)+μT​∇u+f​(x,t,u,ΓT​∇u)=0,\frac{\partial u}{\partial t}+\frac{1}{2}\text{tr}(\Gamma\Gamma^{T}\nabla^{2}u)+\mu^{T}\nabla u+f(x,t,u,\Gamma^{T}\nabla u)=0, |  |

with tt denoting time and TT as the final time, terminal condition u​(x,T)=g​(x)u(x,T)=g(x). Here u​(x,t)u(x,t) is the solution, x∈ℝdx\in\mathbb{R}^{d} represents the state variables, Γ​(x,t)∈ℝd×d\Gamma(x,t)\in\mathbb{R}^{d\times d} is the diffusion matrix, μ​(x,t)∈ℝd\mu(x,t)\in\mathbb{R}^{d} is the drift vector and ff is the nonlinear term. Note that xx varies with time, but for ease of notation we use xx instead of xtx\_{t}.

This general formulation encompasses a wide range of European-style financial derivative pricing problems, including those with stochastic volatility, and complex payoff structures. High-dimensional option pricing problems represent a special case of the semilinear parabolic PDEs discussed above. For basket options involving dd underlying assets S1,S2,…,SdS\_{1},S\_{2},\ldots,S\_{d}, the option value V​(S1,S2,…,Sd,t)V(S\_{1},S\_{2},\ldots,S\_{d},t) satisfies the multidimensional Black-Scholes (BS) PDE:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | ∂V∂t+12​∑i,j=1dσi​j​Si​Sj​∂2V∂Si​∂Sj+r​∑i=1dSi​∂V∂Si−r​V=0.\frac{\partial V}{\partial t}+\frac{1}{2}\sum\_{i,j=1}^{d}\sigma\_{ij}S\_{i}S\_{j}\frac{\partial^{2}V}{\partial S\_{i}\partial S\_{j}}+r\sum\_{i=1}^{d}S\_{i}\frac{\partial V}{\partial S\_{i}}-rV=0. |  |

This corresponds to the PDE framework with the specific forms for the individual components given as:

* •

  x=(S1,…,Sd)Tx=(S\_{1},\ldots,S\_{d})^{T} representing the vector of asset prices
* •

  u​(x,t)=V​(x,t)u(x,t)=V(x,t) representing the option value as a function of asset price vector and time
* •

  μ​(x,t)=r⋅x\mu(x,t)=r\cdot x representing the risk-neutral drift vector with rr as the risk-free rate
* •

  Γ​(x,t)=diag​(x)⋅Σ\Gamma(x,t)=\text{diag}(x)\cdot\Sigma where Σ\Sigma is the volatility matrix and σi​j\sigma\_{ij} are its elements
* •

  f​(x,t,u,σT​∇u)=−r​Vf(x,t,u,\sigma^{T}\nabla u)=-rV representing the linear discounting
* •

  g​(x)=Payoff​(x)g(x)=\text{Payoff}(x) representing the terminal payoff function

The high-dimensional formulation faces the notorious “curse of dimensionality”, where traditional numerical methods require computational resources that grow exponentially with the number of underlying assets. The main challenge in high-dimensional settings is the computation of the Hessian matrix ∇2u\nabla^{2}u, which requires O​(d2)O(d^{2}) evaluations and becomes prohibitively expensive as dd increases. For basket options with even modest dimensions (e.g., d≥5d\geq 5), direct numerical solution becomes computationally intractable using conventional finite difference or finite element approaches.

To alleviate this issue, the Feynman-Kac theorem establishes a fundamental connection between semilinear parabolic PDEs and BSDEs. Specifically, if (Yt,Zt)(Y\_{t},Z\_{t}) is the solution to the BSDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3) |  | d​Yt\displaystyle dY\_{t} | =−f​(Xt,t,Yt,Zt)​d​t+ZtT​d​Wt,\displaystyle=-f(X\_{t},t,Y\_{t},Z\_{t})dt+Z\_{t}^{T}dW\_{t}, |  |
|  | YT\displaystyle Y\_{T} | =g​(XT),\displaystyle=g(X\_{T}), |  |

where XtX\_{t} follows the stochastic differential equation:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | d​Xt=μ​(Xt,t)​d​t+Γ​(Xt,t)​d​Wt,dX\_{t}=\mu(X\_{t},t)dt+\Gamma(X\_{t},t)dW\_{t}, |  |

then u​(x,t)=Ytu(x,t)=Y\_{t} when Xt=xX\_{t}=x, and ΓT​(x,t)​∇u​(x,t)=Zt\Gamma^{T}(x,t)\nabla u(x,t)=Z\_{t}. Here WtW\_{t} is a dd-dimensional standard Brownian motion with correlation matrix Λ\Lambda.

This connection is crucial because the BSDE formulation avoids explicit computation of the Hessian and hence, the curse of dimensionality is significantly mitigated.

American options introduce the additional complexity of optimal early exercise. The option holder can choose to exercise at any stopping time τ≤T\tau\leq T, leading to the optimal stopping problem:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | Yt=supτ∈[t,T]𝔼​[e−r​(τ−t)​h​(Xτ)|ℱt],Y\_{t}=\sup\_{\tau\in[t,T]}\mathbb{E}[e^{-r(\tau-t)}h(X\_{\tau})|\mathcal{F}\_{t}], |  |

where h​(x)h(x) is the intrinsic value function. Following the seminal approach by (El Karoui et al., [1997](https://arxiv.org/html/2601.11097v1#bib.bib6 "Reflected solutions of backward sde’s, and related obstacle problems for pde’s")), this optimal stopping problem can be formulated as a reflected BSDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6) |  | d​Yt\displaystyle dY\_{t} | =−f​(Xt,t,Yt,Zt)​d​t+ZtT​d​Wt+d​Kt,\displaystyle=-f(X\_{t},t,Y\_{t},Z\_{t})dt+Z\_{t}^{T}dW\_{t}+dK\_{t}, |  |
|  | YT\displaystyle Y\_{T} | =g​(XT),\displaystyle=g(X\_{T}), |  |
|  | Yt\displaystyle Y\_{t} | ≥Φ​(Xt)​ for all ​t∈[0,T],\displaystyle\geq\Phi(X\_{t})\text{ for all }t\in[0,T], |  |
|  | ∫0T\displaystyle\int\_{0}^{T} | (Yt−Φ​(Xt))​d​Kt=0,\displaystyle(Y\_{t}-\Phi(X\_{t}))dK\_{t}=0, |  |

where KtK\_{t} is a non-decreasing process that ensures the constraint Yt≥Φ​(Xt)Y\_{t}\geq\Phi(X\_{t}). Φ​(Xt)\Phi(X\_{t}) is a Markovian continuous process growth bounded by a polynomial function, and generally h​(Xt)h(X\_{t}) can be used as a substitute.
In practice, this reflected BSDE can be approximated using a penalty method:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | d​Yt=−f​(Xt,t,Yt,Zt)​d​t+ZtT​d​Wt+λ​(h​(Xt)−Yt)+​d​t,dY\_{t}=-f(X\_{t},t,Y\_{t},Z\_{t})dt+Z\_{t}^{T}dW\_{t}+\lambda(h(X\_{t})-Y\_{t})^{+}dt, |  |

where λ>0\lambda>0 is a penalty parameter and (⋅)+=max⁡(⋅,0)(\cdot)^{+}=\max(\cdot,0).

European options correspond to the case where there is no early exercise constraint. This can be viewed as setting the penalty parameter λ=0\lambda=0 in the American option formulation, resulting in the standard BSDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (8) |  | d​Yt\displaystyle dY\_{t} | =−f​(Xt,t,Yt,Zt)​d​t+ZtT​d​Wt,\displaystyle=-f(X\_{t},t,Y\_{t},Z\_{t})dt+Z\_{t}^{T}dW\_{t}, |  |
|  | YT\displaystyle Y\_{T} | =g​(XT).\displaystyle=g(X\_{T}). |  |

This unified framework allows us to handle both European and American options within the same mathematical setting, simply by adjusting the penalty term.

## 4. Methodology

This section presents our novel KANHedge method, which integrates KANs into the deep BSDE methodology for high-dimensional option pricing and hedging. We begin by discretizing the BSDE formulation, then detail the neural network approximation strategy, and finally introduce our KAN-based approach that addresses the limitations of traditional MLP methods.

Following the approach established in deep BSDE literature (Han et al., [2017](https://arxiv.org/html/2601.11097v1#bib.bib2 "Deep learning-based numerical methods for high-dimensional parabolic partial differential equations and backward stochastic differential equations"), [2018](https://arxiv.org/html/2601.11097v1#bib.bib1 "Solving high-dimensional partial differential equations using deep learning")), we discretize the continuous-time BSDE using an Euler-Maruyama scheme. Consider a uniform time grid:

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | 0=t0<t1<⋯<tN=T,with ​Δ​t=TN.0=t\_{0}<t\_{1}<\cdots<t\_{N}=T,\quad\text{with }\Delta t=\frac{T}{N}. |  |

The forward stochastic differential equation for the underlying asset prices is discretized as:

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | Stn+1=Stn+μ​(Stn,tn)​Δ​t+σ​(Stn,tn)​Δ​Wn,S\_{t\_{n+1}}=S\_{t\_{n}}+\mu(S\_{t\_{n}},t\_{n})\Delta t+\sigma(S\_{t\_{n}},t\_{n})\Delta W\_{n}, |  |

where Δ​Wn=Wtn+1−Wtn∼𝒩​(0,Δ​t⋅Id)\Delta W\_{n}=W\_{t\_{n+1}}-W\_{t\_{n}}\sim\mathcal{N}(0,\Delta t\cdot I\_{d}) are independent Gaussian increments. The general form of BSDE is correspondingly discretized as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (11) |  | Ytn+1\displaystyle Y\_{t\_{n+1}} | =Ytn−[f​(Xtn,tn,Ytn,Ztn)+λ​(h​(Xtn)−Ytn)+]​Δ​t\displaystyle=Y\_{t\_{n}}-[f(X\_{t\_{n}},t\_{n},Y\_{t\_{n}},Z\_{t\_{n}})+\lambda(h(X\_{t\_{n}})-Y\_{t\_{n}})^{+}]\Delta t |  |
|  |  | +ZtnT​Δ​Wn.\displaystyle\quad+Z\_{t\_{n}}^{T}\Delta W\_{n}. |  |

The key insight of the deep BSDE method proposed in (Han et al., [2017](https://arxiv.org/html/2601.11097v1#bib.bib2 "Deep learning-based numerical methods for high-dimensional parabolic partial differential equations and backward stochastic differential equations"), [2018](https://arxiv.org/html/2601.11097v1#bib.bib1 "Solving high-dimensional partial differential equations using deep learning")) is to parameterize the unknown quantities using neural networks. Specifically, the initial option value Y0=u0Y\_{0}=u\_{0} is treated as a trainable scalar parameter and the gradient process ZtZ\_{t} at each time step is approximated by neural networks:

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | Ztn≈Zθn​(Xtn),n=0,1,…,N−1,Z\_{t\_{n}}\approx Z\_{\theta\_{n}}(X\_{t\_{n}}),\quad n=0,1,\ldots,N-1, |  |

where Zθn:ℝd→ℝdZ\_{\theta\_{n}}:\mathbb{R}^{d}\rightarrow\mathbb{R}^{d} are neural networks with trainable parameters θn\theta\_{n}. The training objective minimizes the terminal condition error:

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | ℒ​(Θ)=𝔼​[(YTΘ−g​(XT))2],\mathcal{L}(\Theta)=\mathbb{E}[(Y\_{T}^{\Theta}-g(X\_{T}))^{2}], |  |

where YTΘY\_{T}^{\Theta} is the terminal value obtained by forward simulation using the parameterized networks. This expectation is approximated using Monte Carlo sampling:

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | ℒℳ​(Θ)≈1M​∑i=1M(YTΘ,(i)−g​(XT(i)))2,\mathcal{L\_{M}}(\Theta)\approx\frac{1}{M}\sum\_{i=1}^{M}(Y\_{T}^{\Theta,(i)}-g(X\_{T}^{(i)}))^{2}, |  |

where MM is the batch size and (i)(i) denotes the ii-th Monte Carlo path.

### 4.1. Traditional MLP-Based Approach

In existing deep BSDE methods, the delta networks ZθnZ\_{\theta\_{n}} are typically implemented as MLPs:

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | Ztn≈MLPθn​(Xtn).Z\_{t\_{n}}\approx\text{MLP}\_{\theta\_{n}}(X\_{t\_{n}}). |  |

A major architectural point in MLPs is piecewise linear activations like ReLU. KANHedge, described in the following section, leverages the KAN model that provides an alternative to the linear activation functions.

### 4.2. KANHedge

Our KANHedge method replaces the MLP networks with KANs, which, in theory, offer better functional approximation capabilities for continuous functions. A KAN layer transforms an input 𝐱∈ℝnin\mathbf{x}\in\mathbb{R}^{n\_{\text{in}}} to an output 𝐲∈ℝnout\mathbf{y}\in\mathbb{R}^{n\_{\text{out}}} via:

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | yj=∑i=1ninϕj,i​(xi),y\_{j}=\sum\_{i=1}^{n\_{\text{in}}}\phi\_{j,i}(x\_{i}), |  |

where each ϕj,i\phi\_{j,i} is a learnable univariate function, typically implemented as a B-spline:

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | ϕj,i​(x)=wb⋅b​(x)+ws⋅spline​(x).\phi\_{j,i}(x)=w\_{b}\cdot b(x)+w\_{s}\cdot\text{spline}(x). |  |

Here, b​(x)b(x) is a simple base function (e.g., SiLU), spline​(x)\text{spline}(x) is a B-spline function with learnable control points, and wb,wsw\_{b},w\_{s} are learnable weights.

We model the delta networks ZθnZ\_{\theta\_{n}} with a KAN architecture:

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | Ztn≈KANθn​(Xtn).Z\_{t\_{n}}\approx\text{KAN}\_{\theta\_{n}}(X\_{t\_{n}}). |  |

B-spline basis functions in KANs naturally produce smooth outputs, crucial for accurate delta computation. The advantages of KANs for modeling continuous smooth functions have been demonstrated in (Liu et al., [2025](https://arxiv.org/html/2601.11097v1#bib.bib5 "KAN: kolmogorov-arnold networks")), but they use simpler toy examples for illustration.

The overall training algorithm for KANHedge is given below:

Algorithm 1  KANHedge Training Algorithm

1:Input: Time steps NN, batch size MM, learning rate α\alpha

2:Initialize: u0u\_{0}, KAN parameters {θn}n=0N−1\{\theta\_{n}\}\_{n=0}^{N-1}

3:for each training epoch do

4:  for each mini-batch do

5:   Sample initial conditions {X0(i)}i=1M\{X\_{0}^{(i)}\}\_{i=1}^{M}

6:   Set Y0(i)=u0Y\_{0}^{(i)}=u\_{0} for all ii

7:   for n=0,1,…,N−1n=0,1,\ldots,N-1 do

8:     Compute Ztn(i)=KANθn​(Xtn(i))Z\_{t\_{n}}^{(i)}=\text{KAN}\_{\theta\_{n}}(X\_{t\_{n}}^{(i)})

9:     Generate Δ​Wn(i)∼𝒩​(0,Δ​t⋅Λ)\Delta W\_{n}^{(i)}\sim\mathcal{N}(0,\Delta t\cdot\Lambda)

10:     Update Xtn+1(i)=Xtn(i)+μ​Δ​t+σ​Δ​Wn(i)X\_{t\_{n+1}}^{(i)}=X\_{t\_{n}}^{(i)}+\mu\Delta t+\sigma\Delta W\_{n}^{(i)}

11:     Update Ytn+1(i)=Ytn(i)−f​Δ​t+(Ztn(i))T​Δ​Wn(i)Y\_{t\_{n+1}}^{(i)}=Y\_{t\_{n}}^{(i)}-f\Delta t+(Z\_{t\_{n}}^{(i)})^{T}\Delta W\_{n}^{(i)}

12:             +λ​(h​(Xtn(i))−Ytn(i))+​Δ​t+\lambda(h(X\_{t\_{n}}^{(i)})-Y\_{t\_{n}}^{(i)})^{+}\Delta t

13:   end for

14:   Compute MSE loss: ℒ=1M​∑i=1M(YT(i)−g​(XT(i)))2\mathcal{L}=\frac{1}{M}\sum\_{i=1}^{M}(Y\_{T}^{(i)}-g(X\_{T}^{(i)}))^{2}

15:   Update parameters: Θ←Θ−α​∇Θℒ\Theta\leftarrow\Theta-\alpha\nabla\_{\Theta}\mathcal{L}

16:  end for

17:end for

18:Return: Trained parameters Θ∗\Theta^{\*} and u0u\_{0}

## 5. Experimental Setup

We evaluate the proposed KANHedge method through European and American-style basket option experiments designed to test both pricing accuracy and hedging performance in high-dimensional basket option settings.
The choice of basket options allows us to systematically increase dimensionality while maintaining economic relevance, as basket options are widely traded instruments in equity and commodity markets.

### 5.1. European Basket Options

For our first experimental setup, we consider equal-weight geometric European basket call options following the framework established by (Chen and Wan, [2021](https://arxiv.org/html/2601.11097v1#bib.bib9 "Deep neural network framework based on backward stochastic differential equations for pricing and hedging american options in high dimensions")). The geometric basket construction provides several analytical advantages that make it particularly suitable for validating our KANHedge methodology.

Problem Formulation:
We consider a basket of dd assets with price processes S1,S2,…,SdS\_{1},S\_{2},\ldots,S\_{d}, with equal volatility σ\sigma, that follow correlated geometric Brownian motions such that d​⟨W(i),W(j)⟩t=ρi​j​d​td\langle W^{(i)},W^{(j)}\rangle\_{t}=\rho\_{ij}dt; with ρi​j=ρ\rho\_{ij}=\rho for i≠ji\neq j and 11 otherwise. The risk-free rate is given as rfr\_{f}. The geometric basket is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | Gt=∏i=1d(Si)1/d,\displaystyle G\_{t}=\prod\_{i=1}^{d}(S\_{i})^{1/d}, |  |

The payoff at maturity TT is given by Φ​(ST)=max⁡(GT−K,0)\Phi(S\_{T})=\max\left(G\_{T}-K,0\right).

Analytical Solution and Benchmarking:
A key advantage of this basket option is that it admits an analytical solution under the BS framework (Black and Scholes, [1973](https://arxiv.org/html/2601.11097v1#bib.bib11 "The pricing of options and corporate liabilities")). The geometric basket GtG\_{t} follows a single geometric Brownian motion with equivalent volatility σG\sigma\_{G} and an equivalent risk-free rate rGr\_{G} (Chen and Wan, [2021](https://arxiv.org/html/2601.11097v1#bib.bib9 "Deep neural network framework based on backward stochastic differential equations for pricing and hedging american options in high dimensions")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (20) |  | σG2\displaystyle\sigma\_{G}^{2} | =1+(d−1)​ρd​σ2,and\displaystyle=\frac{1+(d-1)\rho}{d}\sigma^{2},\text{and} |  |
|  | rG\displaystyle r\_{G} | =rf−12​(σG2−σ2).\displaystyle=r\_{f}-\frac{1}{2}(\sigma\_{G}^{2}-\sigma^{2}). |  |

This allows us to compute exact option prices using the standard BS formula.

Experimental Configuration:
To systematically evaluate the performance of our KANHedge, we design a controlled experimental setup with a baseline configuration and targeted parameter variations. Our baseline configuration consists of a 10-dimensional geometric basket call option with the following market parameters: initial asset prices Si0=10S\_{i}^{0}=10 for all i=1,…,di=1,\ldots,d, σ=0.1\sigma=0.1, rf=0.01r\_{f}=0.01, ρ=0.3\rho=0.3 and an at-the-money strike price K=10K=10.

To assess the robustness and sensitivity of our approach, we systematically vary individual market parameters. Specifically, we examine:

* •

  Increased market volatility with σi=0.2\sigma\_{i}=0.2 to test performance under higher uncertainty
* •

  Modified correlation structure to evaluate sensitivity to asset dependencies
* •

  Out-of-the-money options with K=11K=11 to assess performance across different moneyness levels
* •

  Higher dimensionality scenarios to validate scalability properties

This experimental design allows us to isolate the impact of each market parameter on our method’s pricing and hedging performance.

### 5.2. American Basket Options

Our second experimental study focuses on American-style basket options, following the setup of (Hanbali and Linders, [2019](https://arxiv.org/html/2601.11097v1#bib.bib8 "American-type basket option pricing: a simple two-dimensional partial differential equation")). American options present additional computational challenges due to the optimal stopping problem, making them ideal for testing the robustness of our KANHedge method in complex scenarios without analytical solutions.

Problem Formulation:
We consider American put options on arithmetic average baskets with payoff:

|  |  |  |  |
| --- | --- | --- | --- |
| (21) |  | Φ​(St)=max⁡(K−1d​∑i=1dSi,0).\displaystyle\Phi(S\_{t})=\max\left(K-\frac{1}{d}\sum\_{i=1}^{d}S\_{i},0\right). |  |

Following (Longstaff and Schwartz, [2001](https://arxiv.org/html/2601.11097v1#bib.bib7 "Valuing american options by simulation: a simple least-squares approach")), we employ LSMC with polynomial basis functions up to order 3 to estimate reference option prices. To maintain computational tractability in high-dimensional settings, our LSMC implementation uses the arithmetic mean of all stock prices S¯t=1d​∑i=1dSi\bar{S}\_{t}=\frac{1}{d}\sum\_{i=1}^{d}S\_{i} as the primary modeling variable, rather than considering all combinations of individual asset prices. This dimensionality reduction approach significantly reduces the complexity of the LSMC regression for high-dimensional basket options while maintaining sufficient accuracy for benchmarking purposes.

Experimental Configuration:
The American basket experiments follow the benchmark configuration from (Hanbali and Linders, [2019](https://arxiv.org/html/2601.11097v1#bib.bib8 "American-type basket option pricing: a simple two-dimensional partial differential equation")), using an equally weighted basket of d=8d=8 assets. The experimental parameters are:

* •

  Initial asset prices: Si0=4.0S\_{i}^{0}=4.0 for all i=1,…,8i=1,\ldots,8
* •

  Volatilities: σ1∈{0.3,0.9}\sigma\_{1}\in\{0.3,0.9\} for the first asset, σ2=0.6\sigma\_{2}=0.6, σ3=0.1\sigma\_{3}=0.1, σ4=0.9\sigma\_{4}=0.9, σ5=0.3\sigma\_{5}=0.3, σ6=0.7\sigma\_{6}=0.7, σ7=0.8\sigma\_{7}=0.8, σ8=0.2\sigma\_{8}=0.2
* •

  Risk-free rate: rf=0.01r\_{f}=0.01, Time to maturity: T=1T=1 year
* •

  Correlation structure: ρi​j∈{0.3,0.8}\rho\_{ij}\in\{0.3,0.8\} for i≠ji\neq j, ρi​i=1\rho\_{ii}=1
* •

  Strike prices: K∈{3.5,4.0,4.5}K\in\{3.5,4.0,4.5\}

This comprehensive parameter grid allows us to evaluate our method across different market conditions: varying levels of volatility heterogeneity (through the first asset’s volatility), different correlation regimes, multiple moneyness levels, and various time horizons.

The positive risk-free rate (rf=0.01r\_{f}=0.01) is particularly important for American put options as it creates conditions where early exercise becomes optimal when the basket value falls sufficiently below the strike price. This occurs because the discounted value of receiving the strike price immediately can exceed the expected discounted payoff from holding the option until maturity. This early exercise feature provides a rigorous test of our method’s ability to capture optimal stopping decisions based on the current basket value, which is essential for accurate American option pricing and hedging.

Our experimental design deliberately uses a constant interest rate model, which is simpler than stochastic interest rate frameworks such as the Cox-Ingersoll-Ross (CIR) model (Cox et al., [1985](https://arxiv.org/html/2601.11097v1#bib.bib16 "A theory of the term structure of interest rates")). This choice allows us to isolate the performance of our KAN-based approach on the core challenge of high-dimensional American option pricing without the additional complexity of stochastic interest rates.

### 5.3. Evaluation criteria

Our evaluation framework encompasses both pricing accuracy and hedging performance. Pricing accuracy enables it to compare the option value estimated by a model against a benchmark, which is the same metrics used in (Chen and Wan, [2021](https://arxiv.org/html/2601.11097v1#bib.bib9 "Deep neural network framework based on backward stochastic differential equations for pricing and hedging american options in high dimensions"); Hanbali and Linders, [2019](https://arxiv.org/html/2601.11097v1#bib.bib8 "American-type basket option pricing: a simple two-dimensional partial differential equation")). Hedging performance, on the other hand, allows it to compare deltas estimated by each model across all time steps and paths. All evaluation metrics are computed on out-of-sample data using 10,000 simulated paths for the underlying assets to ensure robust statistical assessment of model performance and generalization capabilities.

Pricing Evaluation:
Pricing accuracy serves as the fundamental metric for validating our KANHedge method. We assess the accuracy using the pricing error, which is measured as the percentage difference between the model price estimate u0Mu\_{0}^{M} and the target price u0Tu\_{0}^{T} as:

|  |  |  |  |
| --- | --- | --- | --- |
| (22) |  | Price Error=100⋅|u0M−u0T|u0T.\displaystyle\text{Price Error}=100\cdot\frac{|u\_{0}^{M}-u\_{0}^{T}|}{u\_{0}^{T}}. |  |

For the European geometric basket, we leverage the availability of analytical BS solutions to compute the exact option price as the target. For American basket options, where no analytical solutions exist, we use LSMC as the reference pricing method. While LSMC introduces its own approximation error, it provides a widely accepted benchmark for American option pricing in the literature (Hanbali and Linders, [2019](https://arxiv.org/html/2601.11097v1#bib.bib8 "American-type basket option pricing: a simple two-dimensional partial differential equation"); Chen and Wan, [2021](https://arxiv.org/html/2601.11097v1#bib.bib9 "Deep neural network framework based on backward stochastic differential equations for pricing and hedging american options in high dimensions")). For convergence of LSMC we use 100,000 simulated paths.

Hedging Cost Analysis:
Beyond pricing accuracy, the quality of hedging strategies is crucial for practical applications. Following a similar methodology to that of (Negyesi and Oosterlee, [2025](https://arxiv.org/html/2601.11097v1#bib.bib10 "A deep bsde approach for the simultaneous pricing and delta-gamma hedging of large portfolios consisting of high-dimensional multi-asset bermudan options"); Buehler et al., [2019](https://arxiv.org/html/2601.11097v1#bib.bib3 "Deep hedging"); Hirano et al., [2023](https://arxiv.org/html/2601.11097v1#bib.bib22 "Adversarial deep hedging: learning to hedge without price process modeling")), we evaluate hedging performance through the hedging cost, which measures the actual cost of maintaining a hedged portfolio. From the option issuer’s perspective, the option premium is the value that mitigates the cost of hedging, calculated using some issuer-specific utility function across the hedging cost distribution, and a more efficient hedger leads to a smaller hedging cost (Buehler et al., [2019](https://arxiv.org/html/2601.11097v1#bib.bib3 "Deep hedging")).

Similar to (Buehler et al., [2019](https://arxiv.org/html/2601.11097v1#bib.bib3 "Deep hedging"); Hirano et al., [2023](https://arxiv.org/html/2601.11097v1#bib.bib22 "Adversarial deep hedging: learning to hedge without price process modeling")), the hedging cost focuses solely on the rebalancing costs, cash account evolution, and final payoff settlement. Crucially, this evaluation methodology ensures that model comparison is based exclusively on the quality of delta estimates produced by each model, rather than on the price estimate from the BSDE. This separation provides a direct assessment of a model’s capability as a hedging instrument, independent of its option valuation performance. The hedging cost CC is computed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (23) |  | C=e−r​τ​[−∑n=1NδtnM​(Stn−Stn−1)T−er​Δ​t⋅Dtn−1+Φ​(Sτ)],\displaystyle C=e^{-r\tau}\left[-\sum\_{n=1}^{N}\delta^{M}\_{t\_{n}}(S\_{t\_{n}}-S\_{t\_{n-1}})^{T}-e^{r\Delta t}\cdot D\_{t\_{n-1}}+\Phi(S\_{\tau})\right], |  |

where:

* •

  Δ​t\Delta t is the discrete time step and τ\tau is the exercise time τ\tau
* •

  The first term captures the cost of delta rebalancing across all assets
* •

  The second term accounts for the interest earned/paid on the cash account
* •

  The third term represents the option payoff at exercise time τ\tau (at maturity TT for European options, or at optimal early exercise time for American options)
* •

  The entire hedging cost is discounted from exercise time τ\tau to initial time t0t\_{0} using the factor e−r​τe^{-r\tau}, ensuring that costs from different samples and exercise times are comparable on a present value basis
* •

  After early exercise (i.e., after τ\tau), δ\delta becomes 0 and no cash flows occur in the cash account

Using the hedging cost distribution across all the evaluation sample paths, various target risk measures such as mean, CVaR (Conditional Value at Risk), Entropic Risk Measure (ERM), etc., can be applied to get the optimal option price (Buehler et al., [2019](https://arxiv.org/html/2601.11097v1#bib.bib3 "Deep hedging")). A better hedging strategy should result in a lower hedging cost metrics across these risk measures.

In this research, to assess the tail risk in hedging performance, we employ CVaR at the 95%95\% confidence level for the hedging cost comparison. This measure implies an option issuer who wants to mitigate their losses in the tail region rather than over the entire distribution. With the Value at Risk (VaR) at confidence level α\alpha given as:

|  |  |  |  |
| --- | --- | --- | --- |
| (24) |  | VaRα=inf{x∈ℝ:P​(C>x)≤1−α},\text{VaR}\_{\alpha}=\inf\{x\in\mathbb{R}:P(C>x)\leq 1-\alpha\}, |  |

the CVaR, normalized by the target option price to ensure scale invariance is given as:

|  |  |  |  |
| --- | --- | --- | --- |
| (25) |  | C​V​a​Rα=𝔼​[C|C≥VaRα]|u0T|,\displaystyle{CVaR}\_{\alpha}=\frac{\mathbb{E}[C|C\geq\text{VaR}\_{\alpha}]}{|u\_{0}^{T}|}, |  |

where u0Tu\_{0}^{T} is the BS option price for European options or the LSMC reference price for American options. This normalization allows for meaningful comparison across different option values and market conditions.

## 6. Results

We present comprehensive experimental results evaluating KANHedge model against traditional MLP-based approaches across both European geometric basket options and American basket options.

### 6.1. European Geometric Basket Options

Table [1](https://arxiv.org/html/2601.11097v1#S6.T1 "Table 1 ‣ 6.1. European Geometric Basket Options ‣ 6. Results ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver") presents results for European geometric basket option experiments with setup provided in Section [5.1](https://arxiv.org/html/2601.11097v1#S5.SS1 "5.1. European Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"), where we can leverage analytical BS solutions for exact benchmarking.

Table 1. European Geometric Basket Option Results

| Configuration | Method | Price Error (%) | CVaR |
| --- | --- | --- | --- |
| Baseline | MLP | 0.314 | 1.438 |
| KANHedge | 0.055 | 1.409 |
| High Volatility | MLP | 1.212 | 1.397 |
| KANHedge | 0.943 | 1.350 |
| High Correlation | MLP | 0.849 | 1.376 |
| KANHedge | 0.864 | 1.318 |
| Out-of-Money | MLP | 0.912 | 1.819 |
| KANHedge | 0.685 | 1.787 |
| Higher dimension | MLP | 0.998 | 1.911 |
| KANHedge | 0.831 | 1.883 |

* •

  Price errors are relative to analytical BS solutions. CVaR evaluates normalized hedging cost at 95% confidence level. Bold indicates best performance.

The pricing errors for both models are in the range of 1%1\% for all sets of variations, indicating that u0u\_{0} is roughly the same irrespective of the model used. The distinction comes in the hedging cost where KANHedge outperforms the MLP model, with improvements ranging from 2.01%2.01\% for the baseline case and increasing up to 4.25%4.25\% under increased volatility.

We illustrate the hedging cost distribution for the baseline in Figure [1](https://arxiv.org/html/2601.11097v1#S6.F1 "Figure 1 ‣ 6.1. European Geometric Basket Options ‣ 6. Results ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"). Although the distributions mostly overlap for the two models, the MLP model has a slightly wider right tail leading to a higher hedging cost CVaR. For the sake of brevity, we only show the distribution for the baseline case, but the overall trend is similar for other sets of experimental variations.

![Refer to caption](figures/eu_hedge_cost.png)

Normalized Hedge cost distribution for baseline experiment

Figure 1. Normalized Hedging Cost Distribution for European Geometric Basket Option: Baseline. KANHedge (red) shows slightly better hedging cost compared to MLP (green) when tail risk is used as hedging cost.

### 6.2. American Basket Options

Table [2](https://arxiv.org/html/2601.11097v1#S6.T2 "Table 2 ‣ 6.2. American Basket Options ‣ 6. Results ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver") presents results for American basket options following the experimental configuration described in Section [5.2](https://arxiv.org/html/2601.11097v1#S5.SS2 "5.2. American Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"). Since no analytical solutions exist, pricing accuracy is measured against LSMC benchmarks.

Table 2. American Basket Option Results

| Configuration | Method | Price Error (%) | CVaR |
| --- | --- | --- | --- |
| σ1=0.3\sigma\_{1}=0.3, ρ=0.3\rho=0.3, K=35K=35 | MLP | 0.586 | 1.664 |
| KANHedge | 0.374 | 1.522 |
| σ1=0.3\sigma\_{1}=0.3, ρ=0.3\rho=0.3, K=40K=40 | MLP | 0.257 | 1.540 |
| KANHedge | 0.108 | 1.397 |
| σ1=0.3\sigma\_{1}=0.3, ρ=0.3\rho=0.3, K=45K=45 | MLP | 0.551 | 1.602 |
| KANHedge | 0.172 | 1.486 |
| σ1=0.3\sigma\_{1}=0.3, ρ=0.8\rho=0.8, K=35K=35 | MLP | 0.279 | 1.479 |
| KANHedge | 0.080 | 1.376 |
| σ1=0.3\sigma\_{1}=0.3, ρ=0.8\rho=0.8, K=40K=40 | MLP | 0.213 | 1.416 |
| KANHedge | 0.352 | 1.330 |
| σ1=0.3\sigma\_{1}=0.3, ρ=0.8\rho=0.8, K=45K=45 | MLP | 0.004 | 1.374 |
| KANHedge | 0.370 | 1.280 |
| σ1=0.9\sigma\_{1}=0.9, ρ=0.3\rho=0.3, K=35K=35 | MLP | 0.174 | 1.441 |
| KANHedge | 0.093 | 1.334 |
| σ1=0.9\sigma\_{1}=0.9, ρ=0.3\rho=0.3, K=40K=40 | MLP | 0.327 | 1.359 |
| KANHedge | 0.301 | 1.281 |
| σ1=0.9\sigma\_{1}=0.9, ρ=0.3\rho=0.3, K=45K=45 | MLP | 0.231 | 1.338 |
| KANHedge | 0.426 | 1.225 |
| σ1=0.9\sigma\_{1}=0.9, ρ=0.8\rho=0.8, K=35K=35 | MLP | 0.149 | 1.286 |
| KANHedge | 0.154 | 1.216 |
| σ1=0.9\sigma\_{1}=0.9, ρ=0.8\rho=0.8, K=40K=40 | MLP | 0.089 | 1.347 |
| KANHedge | 0.035 | 1.250 |
| σ1=0.9\sigma\_{1}=0.9, ρ=0.8\rho=0.8, K=45K=45 | MLP | 0.083 | 1.282 |
| KANHedge | 0.153 | 1.225 |

* •

  Price errors are relative to LSMC reference values. CVaR evaluates normalized hedging cost at 95% confidence level. Bold indicates best performance.

A similar trend is observed in the case of American basket options where pricing errors for both models are within 1%1\%, with no clear advantage to either model. As for the hedging cost, KANHedge outperforms the MLP model in all experimental variations with improvements ranging from 4.44%4.44\% to 9.28%9.28\%. The larger improvements in the case of American options can be attributed to the increased volatility levels across the assets in the basket.

We illustrate the hedging cost distribution for the 1s​t1^{st} experiment with σ1=0.3\sigma\_{1}=0.3, ρ=0.3\rho=0.3, K=35K=35 in Figure [2](https://arxiv.org/html/2601.11097v1#S6.F2 "Figure 2 ‣ 6.2. American Basket Options ‣ 6. Results ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"). KANHedge shows a clear improvement over MLP with a more concentrated hedging cost in the tail region. Here too, for the sake of brevity, we only show the hedging cost distribution for a single variation, but the overall trend is the same across other combinations of parameters.

![Refer to caption](figures/am_hedge_cost.png)

Normalized Hedge cost distribution for $\sigma\_{1}=0.3$, $\rho=0.3$, $K=35$

Figure 2. Normalized Hedging Cost Distribution for American Basket Option: σ1=0.3\sigma\_{1}=0.3, ρ=0.3\rho=0.3, K=35K=35. KANHedge (red) shows better hedging cost compared to MLP (green) when tail risk is used as hedging cost.

## 7. Discussion

The experimental results reveal important insights into the differences between KANHedge and MLP architectures for option pricing and hedging applications, particularly highlighting the distinction between pricing accuracy and hedging quality.

The comparable pricing accuracy between KANHedge and MLP suggests that both architectures possess sufficient representational capacity to learn the underlying option valuation. This finding indicates that the choice between KANHedge and MLP should not be primarily driven by pricing accuracy considerations, as both methods can effectively approximate the complex high-dimensional pricing functions inherent in basket options.

However, the consistently improved hedging cost performance of KANHedge reveals a more nuanced architectural advantage. The CVaR improvements across all experiments demonstrate that KANHedge results in better gradient estimation capabilities. This distinction is critical for practical applications, where different option issuers can have different utility functions to be optimized over the hedging cost distribution. Although in our research we use CVaR as the target utility, a more concentrated distribution, as is the case in Figure [2](https://arxiv.org/html/2601.11097v1#S6.F2 "Figure 2 ‣ 6.2. American Basket Options ‣ 6. Results ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"), should result in lower hedging cost metrics over other utility functions such as Value at Risk or ERM.

The improved delta estimation of KANHedge can potentially be attributed to the smoother and learnable activation functions in the architecture. B-spline basis functions used in KANs have the ability to produce smoother and more accurate derivatives compared to MLPs with piecewise linear activations like ReLU. To illustrate this advantage, we consider a variant of the geometric basket option experiments; we change the number of dimensions to 1 in the baseline case of the experiments. The resulting option is nothing but a simple European option. The resulting delta at some random intermediate time step t10t\_{10} is given in Figure [3](https://arxiv.org/html/2601.11097v1#S7.F3 "Figure 3 ‣ 7. Discussion ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").

![Refer to caption](figures/european_option_deltas_7.png)

Deltas estimated by KANHedge and MLP model compared against BS model delta for single dimension European option

Figure 3. Delta estimation for single-dimensional European call option. KANHedge (red) shows superior approximation to the analytical Black-Scholes delta (blue) compared to MLP (green), particularly in out-of-the-money regions.

The advantage of KANHedge in modeling a smooth delta function becomes clear in this simple European option setting. Prices estimated by both models are within 1%1\% of the BS price, but deltas produced by KANHedge align closely with the BS delta in this simple experiment. Although the BS delta is only near-optimal in the discrete time setting, smaller volatility, as is the case in the example, makes the BS delta a good indicator of the optimal delta.

To focus solely on the gradient modeling capabilities of KANHedge, we rely on a delta hedging approach. The smoother and more accurate delta estimation indicates that KANHedge can potentially lead to better gamma estimates for options. We leave pricing and delta-gamma hedging of portfolios of multiple options as a future research direction.

## 8. Conclusion

In this study, we proposed KANHedge, a previously unexplored method that leverages Kolmogorov-Arnold Networks for high-dimensional option pricing and hedging via backward stochastic differential equations. The key idea in this research is to replace traditional MLPs, used to model the option’s delta at each discrete time step, with KANs, which employ learnable B-spline activation functions, thus providing enhanced function approximation capabilities for continuous derivatives. Through comprehensive experiments on both European and American basket options, we demonstrated that while KANHedge and MLP achieve comparable pricing accuracy, KANHedge provides improved delta estimation resulting in improved hedging capabilities. Our experimental results reveal that KANHedge achieves lower hedging cost metrics, measured with CVaR, with improvements up to 4%4\% for European basket options and up to 9%9\% for American basket options.

## References

* R. Assabumrungrat, K. Minami, and M. Hirano (2023)
  Error analysis of option pricing via deep pde solvers: empirical study.
  External Links: 2311.07231,
  [Link](https://arxiv.org/abs/2311.07231)
  Cited by: [§2](https://arxiv.org/html/2601.11097v1#S2.p2.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* R. Bellman (1966)
  Dynamic programming.
  science 153 (3731),  pp. 34–37.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p2.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§1](https://arxiv.org/html/2601.11097v1#S1.p3.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* F. Black and M. Scholes (1973)
  The pricing of options and corporate liabilities.
  Journal of political economy 81 (3),  pp. 637–654.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p1.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§1](https://arxiv.org/html/2601.11097v1#S1.p2.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.1](https://arxiv.org/html/2601.11097v1#S5.SS1.p3.3 "5.1. European Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* H. Buehler, L. Gonon, J. Teichmann, and B. Wood (2019)
  Deep hedging.
  Quantitative Finance 19 (8),  pp. 1271–1291.
  Cited by: [§2](https://arxiv.org/html/2601.11097v1#S2.p3.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p3.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p4.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p5.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* Q. Chan-Wai-Nam, J. Mikael, and X. Warin (2019)
  Machine learning for semi linear pdes.
  Journal of scientific computing 79 (3),  pp. 1667–1712.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p5.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* Y. Chen and J. W. Wan (2021)
  Deep neural network framework based on backward stochastic differential equations for pricing and hedging american options in high dimensions.
  Quantitative Finance 21 (1),  pp. 45–67.
  Cited by: [§5.1](https://arxiv.org/html/2601.11097v1#S5.SS1.p1.1 "5.1. European Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.1](https://arxiv.org/html/2601.11097v1#S5.SS1.p3.3 "5.1. European Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p1.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p2.3 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* J. C. Cox, J. E. Ingersoll, S. A. Ross, et al. (1985)
  A theory of the term structure of interest rates.
  Econometrica 53 (2),  pp. 385–407.
  Cited by: [§5.2](https://arxiv.org/html/2601.11097v1#S5.SS2.p7.1 "5.2. American Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* N. El Karoui, C. Kapoudjian, E. Pardoux, S. Peng, and M. Quenez (1997)
  Reflected solutions of backward sde’s, and related obstacle problems for pde’s.
  the Annals of Probability 25 (2),  pp. 702–737.
  Cited by: [§3](https://arxiv.org/html/2601.11097v1#S3.p12.1 "3. Foundational Mathematics ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* K. Glau and L. Wunderlich (2022)
  The deep parametric pde method and applications to option pricing.
  Applied Mathematics and Computation 432,  pp. 127355.
  Cited by: [§2](https://arxiv.org/html/2601.11097v1#S2.p2.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* E. Gobet, J. Lemor, and X. Warin (2005)
  A regression-based monte carlo method to solve backward stochastic differential equations.
  The Annals of Applied Probability 15 (3),  pp. 2172 – 2202.
  External Links: [Document](https://dx.doi.org/10.1214/105051605000000412),
  [Link](https://doi.org/10.1214/105051605000000412)
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p3.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* J. Han, A. Jentzen, and W. E (2018)
  Solving high-dimensional partial differential equations using deep learning.
  Proceedings of the National Academy of Sciences 115 (34),  pp. 8505–8510.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p4.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§1](https://arxiv.org/html/2601.11097v1#S1.p6.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§1](https://arxiv.org/html/2601.11097v1#S1.p8.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§3](https://arxiv.org/html/2601.11097v1#S3.p2.1 "3. Foundational Mathematics ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§4](https://arxiv.org/html/2601.11097v1#S4.p2.1 "4. Methodology ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§4](https://arxiv.org/html/2601.11097v1#S4.p5.2 "4. Methodology ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* J. Han, A. Jentzen, et al. (2017)
  Deep learning-based numerical methods for high-dimensional parabolic partial differential equations and backward stochastic differential equations.
  Communications in mathematics and statistics 5 (4),  pp. 349–380.
  Cited by: [§4](https://arxiv.org/html/2601.11097v1#S4.p2.1 "4. Methodology ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§4](https://arxiv.org/html/2601.11097v1#S4.p5.2 "4. Methodology ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* H. Hanbali and D. Linders (2019)
  American-type basket option pricing: a simple two-dimensional partial differential equation.
  Quantitative Finance 19 (10),  pp. 1689–1704.
  Cited by: [§5.2](https://arxiv.org/html/2601.11097v1#S5.SS2.p1.1 "5.2. American Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.2](https://arxiv.org/html/2601.11097v1#S5.SS2.p4.1 "5.2. American Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p1.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p2.3 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* R. Handal, K. Matoya, Y. Wang, and M. Hirano (2024)
  KANOP: a data-efficient option pricing model using kolmogorov-arnold networks.
  External Links: 2410.00419,
  [Link](https://arxiv.org/abs/2410.00419)
  Cited by: [§2](https://arxiv.org/html/2601.11097v1#S2.p5.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* B. Hientzsch (2019)
  Introduction to solving quant finance problems with time-stepped fbsde and deep learning.
  External Links: 1911.12231,
  [Link](https://arxiv.org/abs/1911.12231)
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p6.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* M. Hirano, K. Minami, and K. Imajo (2023)
  Adversarial deep hedging: learning to hedge without price process modeling.
  External Links: 2307.13217,
  [Link](https://arxiv.org/abs/2307.13217)
  Cited by: [§2](https://arxiv.org/html/2601.11097v1#S2.p3.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p3.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p4.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* C. Huré, H. Pham, and X. Warin (2020)
  Deep backward schemes for high-dimensional nonlinear pdes.
  Mathematics of Computation 89 (324),  pp. 1547–1579.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p4.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* L. Kapllani and L. Teng (2024)
  Deep learning algorithms for solving high-dimensional nonlinear backward stochastic differential equations.
  Discrete and Continuous Dynamical Systems - B 29 (4),  pp. 1695–1729.
  External Links: ISSN 1553-524X,
  [Link](http://dx.doi.org/10.3934/dcdsb.2023151),
  [Document](https://dx.doi.org/10.3934/dcdsb.2023151)
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p5.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* J. Lemor, E. Gobet, and X. Warin (2006)
  Rate of convergence of an empirical regression method for solving generalized backward stochastic differential equations.
  Bernoulli 12 (5),  pp. 889–916.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p3.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* Z. Liu, Y. Wang, S. Vaidya, F. Ruehle, J. Halverson, M. Soljačić, T. Y. Hou, and M. Tegmark (2025)
  KAN: kolmogorov-arnold networks.
  External Links: 2404.19756,
  [Link](https://arxiv.org/abs/2404.19756)
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p7.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§2](https://arxiv.org/html/2601.11097v1#S2.p4.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§4.2](https://arxiv.org/html/2601.11097v1#S4.SS2.p5.1 "4.2. KANHedge ‣ 4. Methodology ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* F. A. Longstaff and E. S. Schwartz (2001)
  Valuing american options by simulation: a simple least-squares approach.
  The review of financial studies 14 (1),  pp. 113–147.
  Cited by: [§5.2](https://arxiv.org/html/2601.11097v1#S5.SS2.p3.1 "5.2. American Basket Options ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* B. Negyesi and C. W. Oosterlee (2025)
  A deep bsde approach for the simultaneous pricing and delta-gamma hedging of large portfolios consisting of high-dimensional multi-asset bermudan options.
  External Links: 2502.11706,
  [Link](https://arxiv.org/abs/2502.11706)
  Cited by: [§5.3](https://arxiv.org/html/2601.11097v1#S5.SS3.p3.1 "5.3. Evaluation criteria ‣ 5. Experimental Setup ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* E. Pardoux and S. Peng (1992)
  Backward stochastic differential equations and quasilinear parabolic partial differential equations.
  In Stochastic Partial Differential Equations and Their Applications, B. L. Rozovskii and R. B. Sowers (Eds.),
  Berlin, Heidelberg,  pp. 200–217.
  External Links: ISBN 978-3-540-47015-1
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p3.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* M. Raissi (2024)
  Forward–backward stochastic neural networks: deep learning of high-dimensional partial differential equations.
  In Peter Carr Gedenkschrift: Research Advances in Mathematical Finance,
   pp. 637–655.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p4.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver"),
  [§1](https://arxiv.org/html/2601.11097v1#S1.p6.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* J. Sirignano and K. Spiliopoulos (2018)
  DGM: a deep learning algorithm for solving partial differential equations.
  Journal of computational physics 375,  pp. 1339–1364.
  Cited by: [§2](https://arxiv.org/html/2601.11097v1#S2.p2.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* L. Teng and W. Zhao (2021)
  High-order combined multi-step scheme for solving forward backward stochastic differential equations.
  Journal of Scientific Computing 87 (3),  pp. 81.
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p3.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin (2023)
  Attention is all you need.
  External Links: 1706.03762,
  [Link](https://arxiv.org/abs/1706.03762)
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p5.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* Y. Wang, J. Sun, J. Bai, C. Anitescu, M. S. Eshaghi, X. Zhuang, T. Rabczuk, and Y. Liu (2025)
  Kolmogorov–arnold-informed neural network: a physics-informed deep learning framework for solving forward and inverse problems based on kolmogorov–arnold networks.
  Computer Methods in Applied Mechanics and Engineering 433,  pp. 117518.
  Cited by: [§2](https://arxiv.org/html/2601.11097v1#S2.p4.1 "2. Related Work ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").
* A. E. W. Widianto, E. R. M. Putri, I. Mukhlash, and M. Iqbal (2023)
  European high-dimensional option pricing using backward stochastic differential equation-based convolutional neural network.
  In Proceedings of the 2023 6th International Conference on Mathematics and Statistics,
  ICoMS ’23, New York, NY, USA,  pp. 120–125.
  External Links: ISBN 9798400700187,
  [Link](https://doi.org/10.1145/3613347.3613366),
  [Document](https://dx.doi.org/10.1145/3613347.3613366)
  Cited by: [§1](https://arxiv.org/html/2601.11097v1#S1.p5.1 "1. Introduction ‣ KANHedge: Efficient Hedging of High-Dimensional Options Using Kolmogorov-Arnold Network-Based BSDE Solver").