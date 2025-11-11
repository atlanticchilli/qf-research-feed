---
authors:
- Panagiotis G. Papaioannou
- Athanassios N. Yannacopoulos
doc_id: arxiv:2511.05030v2
family_id: arxiv:2511.05030
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold
  Geometries'
url_abs: http://arxiv.org/abs/2511.05030v2
url_html: https://arxiv.org/html/2511.05030v2
venue: arXiv q-fin
version: 2
year: 2025
---


Panagiotis G. Papaioannou
  
Athanassios N. Yannacopoulos

(Received: date / Accepted: date)

###### Abstract

We introduce a Geometry-Informed Model for financial forecasting by embedding high-dimensional market data onto constant-curvature 2-manifolds. Guided by the uniformization theorem,Thurston1997, we model market dynamics as Brownian motion on spherical (S2S^{2}), Euclidean (R2R^{2}), and hyperbolic (H2H^{2}) geometries. We further include the torus (T​²T\texttwosuperior), a compact, flat manifold admissible as a quotient space of the Euclidean plane-—anticipating its relevance for capturing cyclical dynamics,doCarmoCurves. Manifold learning techniques infer the latent curvature from financial data, revealing the torus as the best-performing geometry. We interpret this result through a macroeconomic lens: the torus’s circular dimensions align with endogenous cycles in output, interest rates, and inflation described by IS-LM theory Hicks1937. Our findings demonstrate the value of integrating differential geometry with data-driven inference for financial modeling,LopezDePrado2018AFML; CapponiLehalle2023.

## 1 Introduction

Financial markets are characterized by their complex, non-linear behaviors, posing significant challenges for modeling and prediction. While traditional approaches to market analysis rely heavily on statistical tools and Euclidean assumptions, these methods often fail to account for deeper geometric structures inherent in the data. A novel perspective can be gained by incorporating concepts from differential geometry, particularly the classification of 2-manifolds into three geometries: spherical, Euclidean, and hyperbolic.Thurston1997

The geometrization theorem, which underpins this classification, provides a foundational framework for understanding how spaces can be decomposed into simpler geometric components,Perelman2002. This insight, central to modern differential geometry, suggests that many complex systems, including financial markets, may exhibit characteristics aligning with one or more of these geometric types. As in physics and network science, the widespread application of geometric methods and their potential in financial market analysis is actively explored under active research,CapponiLehalle2023; SimonianFabozzi2019; LopezDePrado2018AFML; LopezDePrado2020MLAM; NoguerAlonso2021FinEAS. Recent studies explore the application of manifold learning techniques to financial market analysis and time series forecasting. These methods aim to extract low-dimensional representations of complex, high-dimensional data, revealing intrinsic structures and patterns (Y2017Nonlinear; G2018Nonlinear; Y2020Manifold). In Jansen2023 several trading practice applications and concepts are outlined, as well. Manifold learning approaches have been used for early warning systems in financial markets (Y2017Nonlinear; G2018Nonlinear), phase space reconstruction of financial time series (Y2014Manifold), and visualization of market states (Y2020Manifold). Researchers have also developed novel algorithms, such as information metric-based manifold learning (Y2017Nonlinear) and kernel entropy manifold learning (Y2014kernel), to improve the accuracy of financial analysis and prediction. Beyond finance, manifold learning techniques have been applied to various time series analysis tasks, including electroencephalography signal analysis (P2018Multivariate) and forecasting of high-dimensional time series (P2021Time), demonstrating their versatility in capturing complex dynamics across different domains.Perelman2002

Brownian motion, a stochastic process traditionally studied in Euclidean spaces, is a powerful tool for modeling random dynamics. Extending Brownian motion to spherical and hyperbolic geometries (Hsu2002; IkedaWatanabe1989) enables the representation of processes influenced by curvature and global topological features. Studies have explored diffusion on spheres (Gomez2021geometrical; M2000Brownian) and hyperbolic spaces (L2007Hyperbolic, Hsu2002StochasticAO), as well as fractional Brownian motion in both geometries (J2005Spherical). The effects of curvature on Brownian motion have been investigated using Riemann normal coordinates (Castro-Villarreal, 2010) and the Smoluchowski equation (Pavel2014Intrinsic). Research has shown that positive curvature slows diffusion, while negative curvature accelerates it (Pavel2010Brownian). The concept of Brownian motion has been generalized to metric spaces of constant curvature (S1981Brownian). Additionally, studies have examined the hydrodynamics of curved membranes and their impact on particulate mobility (Henle2010Hydrodynamics), providing insights into diffusion on biological structures like vesicles and membrane tethers.Hsu2002; IkedaWatanabe1989

Financial markets exhibit complex, nonlinear dynamics that may be better understood through non-Euclidean geometric frameworks (E2006Geometry; Ilinski1999Gauge;Ilinski2001; Emami2021; KellerRessel2021). These markets can be modeled using projective geometry, fiber bundles, and fractal geometry to capture their intricate structures and behaviors (E2006Geometry; Ilinski1999Gauge; B2004MIS; Lipton2001FX; Lipton2018SelectedWorks). Researchers have developed methods to incorporate non-Euclidean geometric information into filtering and machine learning algorithms, improving their accuracy in financial applications (Anastasis2017Geometric). Network geometry measures, such as discrete Ricci curvatures, can be used to analyze market instability and systemic risk (Samal2021Network). The concept of ”dark volatility,” a hidden factor influencing market behavior, has been explored using Einstein warped product manifolds (Pincak2023possible). These geometric approaches provide powerful tools for modeling asset behavior, forecasting volatility, and evaluating investment risks with greater precision (B2004MIS; Humphrey2011Financial).(Ilinski2001; KellerRessel2021; Emami2021)

This paper introduces a new methodology that leverages the interplay between geometry, stochastic processes, and machine learning to analyze and predict financial market behavior. The proposed approach consists of three steps:

1. 1.

   Brownian Motion Construction: Simulate Brownian motions within spherical, Euclidean, and hyperbolic geometries to represent market dynamics.
2. 2.

   Geometry Inference: Apply local gaussian curvature analysis, to infer the underlying geometry from observed trajectories.
3. 3.

   Market Prediction: Use the inferred geometry to inform predictions of future market behavior, leveraging the geometric context to enhance accuracy.

The key idea is to treat financial market dynamics as trajectories embedded in geometrically diverse spaces. This approach allows us to move beyond traditional Euclidean-based analyses, uncovering the ”shape” of market data and providing insights into its structural properties. For example, spherical geometry might correspond to cyclic or periodic market behaviors, Euclidean geometry to stable trends, and hyperbolic geometry to highly volatile and chaotic dynamics. By connecting geometric theory with practical market analysis, this work offers contributions in both theory and application. Theoretically, it bridges the abstract mathematical classification of 2-manifolds with stochastic processes and financial modeling. Practically, it provides a new tool for market prediction that is particularly well-suited for analyzing non-linear and non-stationary systems.

This study aims to demonstrate that the geometric classification of trajectories, combined with stochastic modeling and machine learning, can significantly improve the understanding and prediction of financial markets. The results highlight the power of geometry-informed models in capturing complex behaviors, offering new avenues for research and application in finance and beyond.

## 2 Methodology

##### Roadmap.

We first formalize Brownian motion constrained to embedded surfaces and derive explicit SDEs for the three geometries we use (Euclidean, spherical, hyperbolic), plus the torus via an intrinsic chart (Sec. [3.2](https://arxiv.org/html/2511.05030v2#S3.SS2 "3.2 Explicit SDEs by geometry ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")). We then specify the logarithmic/exponential maps that move between the manifold and its tangent space (Sec. [3.4](https://arxiv.org/html/2511.05030v2#S3.SS4 "3.4 Logarithmic and exponential mappings ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")), followed by data-driven estimation of manifold parameters (sphere radius; torus radii; hyperboloid axes) directly from the observed 3D path (Sec. [3.5](https://arxiv.org/html/2511.05030v2#S3.SS5 "3.5 Data-driven estimation of manifold parameters ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")). Next, we describe our curvature-based geometry inference with a torus topological check (Sec. [3.6](https://arxiv.org/html/2511.05030v2#S3.SS6 "3.6 Local Gaussian Curvature Based Geometry Inference ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")), and the forecasting pipeline: chart →\to log map →\to tangent-space PCA & time-series forecast →\to exponential map (Sec. [3.7](https://arxiv.org/html/2511.05030v2#S3.SS7 "3.7 Forecasting in manifold space and baseline comparison ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")). We close with the explicit native-space baseline comparator and the translation from forecasts to volatility-scaled Profit and Loss (PnL) and portfolio construction (Sec. [3.9](https://arxiv.org/html/2511.05030v2#S3.SS9 "3.9 Real-Finance Data Pipeline: Expanding PCA, Eigenportfolios, and Forecasting ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")). Simulation scenarios and additional implementation details are summarized in the Appendix to keep the section compact.

## 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms

### 3.1 Ambient formulation and curvature drift

Let M⊂ℝ3M\subset\mathbb{R}^{3} be a C2C^{2} embedded surface (2-manifold) with unit normal n​(x)n(x) at x∈Mx\in M and tangent projector

|  |  |  |
| --- | --- | --- |
|  | P​(x)=I−n​(x)​n​(x)⊤∈ℝ3×3.P(x)\;=\;I-n(x)\,n(x)^{\top}\in\mathbb{R}^{3\times 3}. |  |

Brownian motion constrained to MM is the Stratonovich SDE (Hsu2002)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=P​(Xt)∘d​Bt,dX\_{t}\;=\;P(X\_{t})\circ dB\_{t}, |  | (1) |

where BtB\_{t} is standard Brownian motion in ℝ3\mathbb{R}^{3}. In Ito form this becomes (Hsu2002)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=P​(Xt)​d​Bt−12​H​(Xt)​d​t,dX\_{t}\;=\;P(X\_{t})\,dB\_{t}\;-\;\frac{1}{2}\,H(X\_{t})\,dt, |  | (2) |

where H​(x)H(x) is the *mean curvature vector*, normal to MM, that enforces the constraint (heuristically, −12​H-\tfrac{1}{2}H pulls the path back onto MM). For an *implicit* surface M={x:ϕ​(x)=0}M=\{x:\phi(x)=0\} with ∇ϕ​(x)≠0\nabla\phi(x)\neq 0, we use

|  |  |  |
| --- | --- | --- |
|  | n​(x)=∇ϕ​(x)‖∇ϕ​(x)‖,P​(x)=I−n​(x)​n​(x)⊤,n(x)\;=\;\frac{\nabla\phi(x)}{\|\nabla\phi(x)\|},\qquad P(x)\;=\;I-n(x)n(x)^{\top}, |  |

and compute H​(x)H(x) either analytically (when available) or via the implementation used in our simulator (Appendix [B](https://arxiv.org/html/2511.05030v2#A2 "Appendix B Implementation details for SDEs and curvature terms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")).

### 3.2 Explicit SDEs by geometry

##### Euclidean (ℝ3\mathbb{R}^{3})(unconstained ambient).

Trivial case (no constraint). With coordinates Xt=(Xt(1),Xt(2),Xt(3))X\_{t}=(X\_{t}^{(1)},X\_{t}^{(2)},X\_{t}^{(3)}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=d​Bt.dX\_{t}\;=\;dB\_{t}. |  | (3) |

##### Sphere S2​(R)S^{2}(R) (radius RR).

With ϕ​(x)=‖x‖2−R2\phi(x)=\|x\|^{2}-R^{2}, we have n​(x)=x/‖x‖n(x)=x/\|x\| and

|  |  |  |
| --- | --- | --- |
|  | P​(x)=I−x​x⊤R2,H​(x)=2R2​x.P(x)=I-\frac{x\,x^{\top}}{R^{2}},\qquad H(x)=\frac{2}{R^{2}}\,x. |  |

Hence the Ito SDE on S2​(R)S^{2}(R) is (Hsu2002)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(I−Xt​Xt⊤R2)​d​Bt−1R2​Xt​d​t.dX\_{t}\;=\;\Big(I-\frac{X\_{t}X\_{t}^{\top}}{R^{2}}\Big)\,dB\_{t}\;-\;\frac{1}{R^{2}}X\_{t}\,dt. |  | (4) |

For R=1R=1 this reduces to d​Xt=(I−Xt​Xt⊤)​d​Bt−Xt​d​tdX\_{t}=(I-X\_{t}X\_{t}^{\top})dB\_{t}-X\_{t}\,dt.

##### Torus T2​(R,r)T^{2}(R,r) (major radius RR, minor radius rr).

We work both in implicit embedding and in intrinsic angles.

* •

  *Implicit embedding:* ϕ​(x)=(R−x12+x22)2+x32−r2=0\displaystyle\phi(x)=\big(R-\sqrt{x\_{1}^{2}+x\_{2}^{2}}\big)^{2}+x\_{3}^{2}-r^{2}=0. Then

  |  |  |  |
  | --- | --- | --- |
  |  | n​(x)=∇ϕ​(x)‖∇ϕ​(x)‖,P​(x)=I−n​(x)​n​(x)⊤,n(x)=\frac{\nabla\phi(x)}{\|\nabla\phi(x)\|},\qquad P(x)=I-n(x)n(x)^{\top}, |  |

  and we evolve ([2](https://arxiv.org/html/2511.05030v2#S3.E2 "In 3.1 Ambient formulation and curvature drift ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) with this projector and the corresponding H​(x)H(x) (Appendix [B](https://arxiv.org/html/2511.05030v2#A2 "Appendix B Implementation details for SDEs and curvature terms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")).
* •

  *Intrinsic chart (θ,φ)∈[0,2​π)2(\theta,\varphi)\in[0,2\pi)^{2}:*

  |  |  |  |
  | --- | --- | --- |
  |  | Ψ​(θ,φ)=((R+r​cos⁡φ)​cos⁡θ(R+r​cos⁡φ)​sin⁡θr​sin⁡φ).\Psi(\theta,\varphi)=\begin{pmatrix}(R+r\cos\varphi)\cos\theta\\[1.99997pt] (R+r\cos\varphi)\sin\theta\\[1.99997pt] r\sin\varphi\end{pmatrix}. |  |

  The metric is diagonal: gθ​θ=(R+r​cos⁡φ)2g\_{\theta\theta}=(R+r\cos\varphi)^{2}, gφ​φ=r2g\_{\varphi\varphi}=r^{2},doCarmoRiemannian, hence gθ​θ=(R+r​cos⁡φ)−2g^{\theta\theta}=(R+r\cos\varphi)^{-2}, gφ​φ=r−2g^{\varphi\varphi}=r^{-2} and |g|=r​(R+r​cos⁡φ)\sqrt{|g|}=r(R+r\cos\varphi). The Ito SDE realizing generator 12​Δg\tfrac{1}{2}\Delta\_{g} is

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | d​θt\displaystyle d\theta\_{t} | =1R+r​cos⁡φt​d​Wt(1),\displaystyle=\frac{1}{R+r\cos\varphi\_{t}}\,dW\_{t}^{(1)}, |  | (5) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | d​φt\displaystyle d\varphi\_{t} | =1r​d​Wt(2)−sin⁡φt2​r​(R+r​cos⁡φt)​d​t.\displaystyle=\frac{1}{r}\,dW\_{t}^{(2)}\;-\;\frac{\sin\varphi\_{t}}{2r\,(R+r\cos\varphi\_{t})}\,dt. |  | (6) |

  Cartesian positions follow by Xt=Ψ​(θt,φt)X\_{t}=\Psi(\theta\_{t},\varphi\_{t}).

##### Hyperbolic H2H^{2} (hyperboloid model).

Use parameters (u,v)∈ℝ×[0,2​π)(u,v)\in\mathbb{R}\times[0,2\pi) and constants a>0a>0, c>0c>0:

|  |  |  |
| --- | --- | --- |
|  | Φ​(u,v)=(a​cosh⁡u​cos⁡va​cosh⁡u​sin⁡vc​sinh⁡u).\Phi(u,v)=\begin{pmatrix}a\cosh u\cos v\\ a\cosh u\sin v\\ c\sinh u\end{pmatrix}. |  |

Then gu​u=E​(u)=a2​sinh2⁡u+c2​cosh2⁡ug\_{uu}=E(u)=a^{2}\sinh^{2}u+c^{2}\cosh^{2}u, gv​v=G​(u)=a2​cosh2⁡ug\_{vv}=G(u)=a^{2}\cosh^{2}u,doCarmoRiemannian, so gu​u=1/Eg^{uu}=1/E, gv​v=1/Gg^{vv}=1/G, |g|=E​(u)​G​(u)=a​cosh⁡u​E​(u)\sqrt{|g|}=\sqrt{E(u)G(u)}=a\cosh u\,\sqrt{E(u)}. The Ito SDE (generator 12​Δg\tfrac{1}{2}\Delta\_{g}) reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ut\displaystyle du\_{t} | =1E​(ut)​d​Wt(1)+12​∂u[ln⁡(|g|​gu​u)]u=ut​d​t\displaystyle=\frac{1}{\sqrt{E(u\_{t})}}\,dW\_{t}^{(1)}\;+\;\frac{1}{2}\,\partial\_{u}\!\left[\ln\!\big(\sqrt{|g|}\,g^{uu}\big)\right]\_{u=u\_{t}}\,dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1E​(ut)​d​Wt(1)+12​(tanh⁡ut−E′​(ut)2​E​(ut))​d​t,\displaystyle=\frac{1}{\sqrt{E(u\_{t})}}\,dW\_{t}^{(1)}\;+\;\frac{1}{2}\left(\tanh u\_{t}-\frac{E^{\prime}(u\_{t})}{2E(u\_{t})}\right)dt, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​vt\displaystyle dv\_{t} | =1G​(ut)​d​Wt(2)=1a​cosh⁡ut​d​Wt(2),\displaystyle=\frac{1}{\sqrt{G(u\_{t})}}\,dW\_{t}^{(2)}\;=\;\frac{1}{a\cosh u\_{t}}\,dW\_{t}^{(2)}, |  | (8) |

with E′​(u)=2​(a2+c2)​sinh⁡u​cosh⁡uE^{\prime}(u)=2(a^{2}+c^{2})\sinh u\cosh u. Cartesian positions are Xt=Φ​(ut,vt)X\_{t}=\Phi(u\_{t},v\_{t}).

Remark (ambient implementation). We also implement ([2](https://arxiv.org/html/2511.05030v2#S3.E2 "In 3.1 Ambient formulation and curvature drift ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) directly in ℝ3\mathbb{R}^{3} using P​(x)P(x) and a closed-form mean-curvature drift H​(x)H(x) for each implicit surface; formulas above and the implementation are equivalent modulo time discretization (Appendix [B](https://arxiv.org/html/2511.05030v2#A2 "Appendix B Implementation details for SDEs and curvature terms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")).

### 3.3 Nonlinear forecasting via machine learning regressors

Beyond the linear Vector AutoRegression (VAR) model, we also tested two nonlinear regressors—*Random Forests (RF)* and *Gaussian Process Regression (GP)*—to assess whether local nonlinearities in the tangent-space coordinates could enhance predictive accuracy.
Both approaches share the same input representation, where the target variable yty\_{t} (one coordinate of the tangent vector series) is regressed on its LL most recent lags:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟={(𝐱t,yt)}t=LT−1,𝐱t=[yt−1,yt−2,…,yt−L]⊤.\mathcal{D}=\{(\mathbf{x}\_{t},y\_{t})\}\_{t=L}^{T-1},\qquad\mathbf{x}\_{t}=[y\_{t-1},y\_{t-2},\dots,y\_{t-L}]^{\top}. |  | (9) |

At each step, the models are trained on 𝒟\mathcal{D} and used to predict y^T+1=f​(𝐱T)\widehat{y}\_{T+1}=f(\mathbf{x}\_{T}), where f​(⋅)f(\cdot) denotes the learned regression mapping.

##### Random Forest regression.

A Random Forest (breiman2001random) constructs an ensemble of BB regression trees {fb​(⋅)}b=1B\{f\_{b}(\cdot)\}\_{b=1}^{B}, each trained on a bootstrap resample of 𝒟\mathcal{D} and a random subset of predictors.
The forecast corresponds to the ensemble mean:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^T+1(RF)=1B​∑b=1Bfb​(𝐱T),\widehat{y}\_{T+1}^{(\mathrm{RF})}=\frac{1}{B}\sum\_{b=1}^{B}f\_{b}(\mathbf{x}\_{T}), |  | (10) |

where each fbf\_{b} partitions the lagged feature space ℝL\mathbb{R}^{L} into piecewise-constant regions and averages the training observations within the corresponding leaf.
RF models approximate nonlinear relationships and capture variable interactions without assuming parametric structure.
In our implementation, we used B=100B=100 trees and a memory length of L=5L=5 lags for all tangent coordinates (xt,yt,zt)(x\_{t},y\_{t},z\_{t}).

##### Gaussian Process regression.

The Gaussian Process (GP) model treats the regression function f​(⋅)f(\cdot) as a random function drawn from a Gaussian process prior:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(⋅)∼𝒢​𝒫​(m​(⋅),k​(⋅,⋅)),f(\cdot)\sim\mathcal{GP}(m(\cdot),k(\cdot,\cdot)), |  | (11) |

with mean function m​(⋅)m(\cdot) (set to zero) and covariance kernel k​(𝐱,𝐱′)k(\mathbf{x},\mathbf{x}^{\prime}) encoding smoothness and correlation structure.
Given training data 𝒟\mathcal{D}, the posterior predictive distribution at a new input 𝐱T\mathbf{x}\_{T} is Gaussian:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(yT+1|𝐱T,𝒟)=𝒩​(𝐤T⊤​(K+σn2​I)−1​𝐲,k​(𝐱T,𝐱T)−𝐤T⊤​(K+σn2​I)−1​𝐤T),p(y\_{T+1}\,|\,\mathbf{x}\_{T},\mathcal{D})=\mathcal{N}\big(\mathbf{k}\_{T}^{\top}(K+\sigma\_{n}^{2}I)^{-1}\mathbf{y},\;k(\mathbf{x}\_{T},\mathbf{x}\_{T})-\mathbf{k}\_{T}^{\top}(K+\sigma\_{n}^{2}I)^{-1}\mathbf{k}\_{T}\big), |  | (12) |

where KK is the kernel matrix with [K]i​j=k​(𝐱i,𝐱j)[K]\_{ij}=k(\mathbf{x}\_{i},\mathbf{x}\_{j}), and 𝐤T=[k​(𝐱1,𝐱T),…,k​(𝐱N,𝐱T)]⊤\mathbf{k}\_{T}=[k(\mathbf{x}\_{1},\mathbf{x}\_{T}),\dots,k(\mathbf{x}\_{N},\mathbf{x}\_{T})]^{\top}.
The mean of this posterior gives the forecast:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^T+1(GP)=𝐤T⊤​(K+σn2​I)−1​𝐲.\widehat{y}\_{T+1}^{(\mathrm{GP})}=\mathbf{k}\_{T}^{\top}(K+\sigma\_{n}^{2}I)^{-1}\mathbf{y}. |  | (13) |

We used a Matérn kernel with an additive constant term,

|  |  |  |  |
| --- | --- | --- | --- |
|  | k​(𝐱,𝐱′)=kMatern​(𝐱,𝐱′)+kconst​(𝐱,𝐱′),k(\mathbf{x},\mathbf{x}^{\prime})=k\_{\mathrm{Matern}}(\mathbf{x},\mathbf{x}^{\prime})+k\_{\mathrm{const}}(\mathbf{x},\mathbf{x}^{\prime}), |  | (14) |

which balances smooth local trends with global level shifts, providing flexibility for financial data where both slow drifts and abrupt changes can occur.

##### Forecast integration.

In the forecasting pipeline, both RF and GP models operate on the tangent-space coordinates and provide one-step-ahead predictions v^t+1\widehat{v}\_{t+1}, which are then lifted back to the manifold via the exponential map,

|  |  |  |  |
| --- | --- | --- | --- |
|  | x^t+1=expμ^⁡(v^t+1),\widehat{x}\_{t+1}=\exp\_{\widehat{\mu}}(\widehat{v}\_{t+1}), |  | (15) |

thus preserving the geometric structure of the original process. For our analysis, we used a rolling window framework for both ML methods, using 25 observations (trading days) for training and predicting one-step ahead points.

### 3.4 Logarithmic and exponential mappings

Let Tx​MT\_{x}M denote the tangent plane at x∈Mx\in M.Pennec2018; doCarmoRiemannian

##### Sphere S2​(R)S^{2}(R).

For unit vectors μ,p∈S2​(R)\mu,p\in S^{2}(R) define θ=arccos⁡(μ⋅pR2)∈[0,π]\theta=\arccos\!\big(\tfrac{\mu\cdot p}{R^{2}}\big)\in[0,\pi]. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | logμ⁡(p)\displaystyle\log\_{\mu}(p) | ={𝟎,p=μ,θsin⁡θ​Πμ​p,p≠μ,\displaystyle=\begin{cases}\mathbf{0},&p=\mu,\\[3.50006pt] \dfrac{\theta}{\sin\theta}\;\Pi\_{\mu}\,p,&p\neq\mu,\end{cases} |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | expμ⁡(v)\displaystyle\exp\_{\mu}(v) | =cos⁡(‖v‖/R)​μ+R​sin⁡(‖v‖/R)​v‖v‖,v∈Tμ​S2​(R).\displaystyle=\cos\!\big(\|v\|/R\big)\,\mu\;+\;R\,\sin\!\big(\|v\|/R\big)\,\dfrac{v}{\|v\|},\qquad v\in T\_{\mu}S^{2}(R). |  | (17) |

See Pennec2018; doCarmoRiemannian for closed forms.

##### Torus T2​(R,r)T^{2}(R,r) (angle chart).doCarmoCurves

Use angles (θ,φ)∈[0,2​π)2(\theta,\varphi)\in[0,2\pi)^{2}. For base point (θ0,φ0)(\theta\_{0},\varphi\_{0}) and point (θ,φ)(\theta,\varphi),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log(θ0,φ0)⁡(θ,φ)\displaystyle\log\_{(\theta\_{0},\varphi\_{0})}(\theta,\varphi) | =(wrap​(θ−θ0),wrap​(φ−φ0)),\displaystyle=\big(\mathrm{wrap}(\theta-\theta\_{0}),\;\mathrm{wrap}(\varphi-\varphi\_{0})\big), |  | (18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | exp(θ0,φ0)⁡(Δ​θ,Δ​φ)\displaystyle\exp\_{(\theta\_{0},\varphi\_{0})}(\Delta\theta,\Delta\varphi) | =(θ0+Δ​θ,φ0+Δ​φ)mod2​π,\displaystyle=\big(\theta\_{0}+\Delta\theta,\;\varphi\_{0}+\Delta\varphi\big)\bmod 2\pi, |  | (19) |

where wrap​(α)=((α+π)mod2​π)−π\mathrm{wrap}(\alpha)=((\alpha+\pi)\bmod 2\pi)-\pi is the [−π,π)[-\pi,\pi) minimizer. Mapping to ℝ3\mathbb{R}^{3} uses Ψ\Psi above.

##### Hyperbolic (hyperboloid chart).doCarmoRiemannian

In coordinates (u,v)(u,v) with metric diag​(E​(u),G​(u))\mathrm{diag}(E(u),G(u)),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log(u0,v0)⁡(u,v)\displaystyle\log\_{(u\_{0},v\_{0})}(u,v) | =(u−u0,wrap​(v−v0)),\displaystyle=\big(u-u\_{0},\;\mathrm{wrap}(v-v\_{0})\big), |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | exp(u0,v0)⁡(Δ​u,Δ​v)\displaystyle\exp\_{(u\_{0},v\_{0})}(\Delta u,\Delta v) | =(u0+Δ​u,v0+Δ​vmod2​π),\displaystyle=\big(u\_{0}+\Delta u,\;v\_{0}+\Delta v\bmod 2\pi\big), |  | (21) |

then lift to ℝ3\mathbb{R}^{3} via Φ\Phi. For small moves these coincide with the Riemannian log/exp in these orthogonal coordinates.

##### Karcher mean and tangent PCA.Karcher1977; Pennec2018

Given points {xi}⊂M\{x\_{i}\}\subset M, we compute the intrinsic (Karcher) mean μ⋆\mu^{\star} by iterating μ←expμ⁡(1N​∑ilogμ⁡(xi))\mu\leftarrow\exp\_{\mu}\!\big(\tfrac{1}{N}\sum\_{i}\log\_{\mu}(x\_{i})\big) until convergence. We then project data to Tμ⋆​MT\_{\mu^{\star}}M with logμ⋆⁡(xi)\log\_{\mu^{\star}}(x\_{i}) and perform PCA there (this is the “tangent-PCA” used in our forecasting pipeline).

### 3.5 Data-driven estimation of manifold parameters

A key ingredient of our pipeline is that the geometry is not treated as fixed; instead, its *intrinsic parameters* are inferred on the fly from the observed 3D path {xt=(xt,yt,zt)}t≤t⋆\{x\_{t}=(x\_{t},y\_{t},z\_{t})\}\_{t\leq t^{\star}}. This subsection formalizes the estimation steps we implement for the sphere, torus and one–sheeted hyperboloid, matching the code used in our experiments.CazalsPouget2005; CohenSteiner2006

##### Notation.

Let M​(ϑ)M(\vartheta) denote a parametric surface embedded in ℝ3\mathbb{R}^{3} with parameter vector ϑ\vartheta (e.g., radius RR on the sphere; major/minor radii (R,r)(R,r) on the torus; semi–axes (a,b,c)(a,b,c) on the hyperboloid). Given a stream {xt}\{x\_{t}\} up to time t⋆t^{\star}, we estimate ϑ^t⋆\widehat{\vartheta}\_{t^{\star}} and then work in the corresponding chart for mapping, forecasting and lifting. Throughout, angles are unwrapped *mod* 2​π2\pi using the shortest–-arc convention to preserve continuity in the tangent space (see ([23](https://arxiv.org/html/2511.05030v2#S3.E23 "In Torus 𝑇²⁢(𝑅,𝑟): method–-of-–moments from toroidal coordinates ‣ 3.5 Data-driven estimation of manifold parameters ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) below).

#### Sphere S2​(R)S^{2}(R): Karcher mean and radius

For spherical segments, we first compute a *Karcher (Fréchet) mean* μ^∈S2\widehat{\mu}\in S^{2} of the points {xt/‖xt‖}\{x\_{t}/\|x\_{t}\|\} by iterating μ←expμ⁡(1n​∑tlogμ⁡(xt))\mu\leftarrow\exp\_{\mu}\!\big(\tfrac{1}{n}\sum\_{t}\log\_{\mu}(x\_{t})\big) until convergence;Karcher1977

An estimate of the radius follows from

|  |  |  |
| --- | --- | --- |
|  | R^t⋆=arg​minR>0​∑t≤t⋆(‖xt‖−R)2=1t⋆​∑t≤t⋆‖xt‖.\widehat{R}\_{t^{\star}}\;=\;\operatorname\*{arg\,min}\_{R>0}\,\sum\_{t\leq t^{\star}}\big(\|x\_{t}\|-R\big)^{2}\;=\;\frac{1}{t^{\star}}\sum\_{t\leq t^{\star}}\|x\_{t}\|. |  |

This R^\widehat{R} is needed since we wish to keep track of the physical scale;

#### Torus T2​(R,r)T^{2}(R,r): method–-of-–moments from toroidal coordinates

We convert Cartesian observations to toroidal angles (θt,ϕt)(\theta\_{t},\phi\_{t}) and the auxiliary radial quantity ρt=xt2+yt2\rho\_{t}=\sqrt{x\_{t}^{2}+y\_{t}^{2}} : a standard torus (major radius RR, minor radius rr) in the *Reinhardt* parameterization is

|  |  |  |
| --- | --- | --- |
|  | x=(R+r​cos⁡ϕ)​cos⁡θ,y=(R+r​cos⁡ϕ)​sin⁡θ,z=r​sin⁡ϕ.x=(R+r\cos\phi)\cos\theta,\quad y=(R+r\cos\phi)\sin\theta,\quad z=r\sin\phi. |  |

From ρt=xt2+yt2=R+r​cos⁡ϕt\rho\_{t}=\sqrt{x\_{t}^{2}+y\_{t}^{2}}=R+r\cos\phi\_{t} it follows that
𝔼​[ρt]=R,Var⁡(ρt)=r22​if ​ϕt∼Unif.\mathbb{E}[\rho\_{t}]=R,\quad\operatorname{Var}(\rho\_{t})=\tfrac{r^{2}}{2}\ \text{if }\phi\_{t}\sim\text{Unif}.
We adopt a simple method of moments on the *minor angle* and its cosine (normalized units):

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^=1t⋆​∑t≤t⋆cos⁡ϕt,r^=1t⋆​∑t≤t⋆(cos⁡ϕt−R^)2,\widehat{R}\;=\;\frac{1}{t^{\star}}\sum\_{t\leq t^{\star}}\cos\phi\_{t},\qquad\widehat{r}\;=\;\sqrt{\frac{1}{t^{\star}}\sum\_{t\leq t^{\star}}\big(\cos\phi\_{t}-\widehat{R}\big)^{2}}, |  | (22) |

In practice, for stability we use R^\widehat{R} from ([22](https://arxiv.org/html/2511.05030v2#S3.E22 "In Torus 𝑇²⁢(𝑅,𝑟): method–-of-–moments from toroidal coordinates ‣ 3.5 Data-driven estimation of manifold parameters ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) while the *instantaneous* tube radius is proxied by the latest ρt⋆\rho\_{t^{\star}}, which helps track slow deformations of the tube thickness in non–stationary segments. doCarmoCurves

Tangent space steps use the 2​π2\pi wrapped *shortest arc* differences

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​θt=((θt−θ0+π)mod2​π)−π,Δ​ϕt=((ϕt−ϕ0+π)mod2​π)−π,\Delta\theta\_{t}\;=\;((\theta\_{t}-\theta\_{0}+\pi)\bmod 2\pi)-\pi,\qquad\Delta\phi\_{t}\;=\;((\phi\_{t}-\phi\_{0}+\pi)\bmod 2\pi)-\pi, |  | (23) |

#### One sheeted hyperboloid x2/a2+y2/b2−z2/c2=1x^{2}/a^{2}+y^{2}/b^{2}-z^{2}/c^{2}=1: nonlinear Least Squares

For hyperbolic patches we assume the one–sheeted quadratic model

|  |  |  |
| --- | --- | --- |
|  | F​(x,y,z;a,b,c)=x2a2+y2b2−z2c2−1= 0.F(x,y,z;a,b,c)\;=\;\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}-\frac{z^{2}}{c^{2}}-1\;=\;0. |  |

Given {xt}\{x\_{t}\}, we fit (a,b,c)(a,b,c) by nonlinear least squares

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a^,b^,c^)∈arg⁡mina,b,c>0​∑t≤t⋆F​(xt,yt,zt;a,b,c)2,(\widehat{a},\widehat{b},\widehat{c})\;\in\;\arg\min\_{a,b,c>0}\ \sum\_{t\leq t^{\star}}F(x\_{t},y\_{t},z\_{t};a,b,c)^{2}, |  | (24) |

just before transforming the stream to hyperbolic coordinates and entering the log, forecast, exp cycle

The coordinate chart uses (u,v)(u,v) with
x=a​cosh⁡u​cos⁡v,y=b​cosh⁡u​sin⁡v,z=c​sinh⁡ux=a\cosh u\cos v,\ y=b\cosh u\sin v,\ z=c\sinh u,
and the forward/backward conversions are handled by implementing the numerically stable choice u=arcsinh⁡(z/c)u=\operatorname{arcsinh}(z/c) and v=atan2⁡(y/b,x/a)v=\operatorname{atan2}(y/b,x/a)).

On this chart, the log map again uses shortest arc wrapping on vv and simple differencing on uu; the exp map re–adds those increments around the base point. doCarmoRiemannian

#### Chart transition inside the ’motion mixing’ framework

At each step t⋆t^{\star}, the pipeline (i) picks/updates the active geometry M​(ϑ^t⋆)M(\widehat{\vartheta}\_{t^{\star}}), (ii) *re–charts* the recent window to the intrinsic coordinates of MM, (iii) applies *tangent space* PCA/forecasting, and (iv) lifts the predicted tangent vector back to ℝ3\mathbb{R}^{3} through the geometry exp map and its embedding.

Concretely:

Sphere (S). 
xt↦x~t:=xt‖xt‖∈S2​(R)→logμ^vt∈Tμ^​S2​(R)→PGA + forecastv^t+1→expμ^x^t+1.x\_{t}\;\mapsto\;\tilde{x}\_{t}:=\frac{x\_{t}}{\|x\_{t}\|}\in S^{2}(R)\;\xrightarrow{\ \log\_{\widehat{\mu}}\ }\;v\_{t}\in T\_{\widehat{\mu}}S^{2}(R)\;\xrightarrow{\ \text{PGA + forecast}\ }\;\widehat{v}\_{t+1}\;\xrightarrow{\ \exp\_{\widehat{\mu}}\ }\;\widehat{x}\_{t+1}.

Torus (T). 
xt↦(θt,ϕt)→log(θ0,ϕ0)vt→PGA + forecastv^t+1→exp(θ0,ϕ0)(θ^,ϕ^)→Ψ(R^,r^)x^t+1,x\_{t}\;\mapsto\;(\theta\_{t},\phi\_{t})\;\xrightarrow{\ \log\_{(\theta\_{0},\phi\_{0})}\ }\;v\_{t}\;\xrightarrow{\ \text{PGA + forecast}\ }\;\widehat{v}\_{t+1}\;\xrightarrow{\ \exp\_{(\theta\_{0},\phi\_{0})}\ }\;(\widehat{\theta},\widehat{\phi})\;\xrightarrow{\ \Psi\_{(\widehat{R},\widehat{r})}\ }\;\widehat{x}\_{t+1},
where Ψ(R,r):S1×S1→ℝ3\Psi\_{(R,r)}:S^{1}\times S^{1}\to\mathbb{R}^{3} is the standard torus embedding.

Hyperbolic (H). 
xt↦(ut,vt)→log(u0,v0)wt→PGA + forecastw^t+1→exp(u0,v0)(u^,v^)→Φ(a^,b^,c^)x^t+1,x\_{t}\;\mapsto\;(u\_{t},v\_{t})\;\xrightarrow{\ \log\_{(u\_{0},v\_{0})}\ }\;w\_{t}\;\xrightarrow{\ \text{PGA + forecast}\ }\;\widehat{w}\_{t+1}\;\xrightarrow{\ \exp\_{(u\_{0},v\_{0})}\ }\;(\widehat{u},\widehat{v})\;\xrightarrow{\ \Phi\_{(\widehat{a},\widehat{b},\widehat{c})}\ }\;\widehat{x}\_{t+1},
where Φ(a,b,c)\Phi\_{(a,b,c)} embeds the hyperbolic chart (e.g., hyperboloid model) into ℝ3\mathbb{R}^{3}.

By explicitly re–estimating (R^)(\widehat{R}) or (R^,r)(\widehat{R},r) or (a^,b^,c^)(\widehat{a},\widehat{b},\widehat{c}) at each step (or on an expanding/rolling schedule), we avoid confusing the *learned geometry* with the auxiliary linear reduction used inside the tangent space,Pennec2018. The code performs these updates right before building the log–-tangent cloud and forecasting the principal coordinates.

#### Numerical considerations

* •

  Angle wrapping. All angular differences use the shortest–arc rule ([23](https://arxiv.org/html/2511.05030v2#S3.E23 "In Torus 𝑇²⁢(𝑅,𝑟): method–-of-–moments from toroidal coordinates ‣ 3.5 Data-driven estimation of manifold parameters ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) to keep tangent vectors small and numerically stable on compact directions (torus S1×S1S^{1}{\times}S^{1} and the angular coordinate vv on the hyperboloid).
* •

  Stability at small steps. Spherical log/exp guard against sin⁡θ≈0\sin\theta\!\approx\!0 and ‖v‖≈0\|v\|\!\approx\!0 (returning zeros or the base point), preventing blow–ups when points are nearly aligned.
* •

  Robust lifting. The torus and hyperboloid use explicit closed–form embeddings for *lifting* the predicted coordinates back to ℝ3\mathbb{R}^{3}, ensuring that x^t+1\widehat{x}\_{t+1} lies on M​(ϑ^t⋆)M(\widehat{\vartheta}\_{t^{\star}}) by construction.

### 3.6 Local Gaussian Curvature Based Geometry Inference

We infer the latent geometry directly from the data via a *local differential–geometric fit* combined with *topological validation*. The pipeline operates on a 3D trajectory
Xt=(xt,yt,zt)∈ℝ3X\_{t}=(x\_{t},y\_{t},z\_{t})\in\mathbb{R}^{3} obtained either from simulation or from real data after a 3D embedding (e.g., expanding-window PCA of returns). We show the dynamics of the simulations and from the real data in [1](https://arxiv.org/html/2511.05030v2#S3.F1 "Figure 1 ‣ 3.6 Local Gaussian Curvature Based Geometry Inference ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries").

![Refer to caption](images/CartesianPathDFMain_1.png)

(a) Scenario 1

![Refer to caption](images/CartesianPathDFMain_2.png)

(b) Scenario 2

![Refer to caption](images/CartesianPathDFMain_3.png)

(c) Scenario 3

![Refer to caption](images/CartesianPathDFMain_4.png)

(d) Scenario 4

![Refer to caption](images/CartesianPathDFMain_5.png)

(e) Scenario 5

![Refer to caption](images/CartesianPathDFMain_6.png)

(f) Scenario 6

![Refer to caption](images/CartesianPathDFMain_7.png)

(g) Scenario 7

![Refer to caption](images/CartesianPathDFMain_PCA3D.png)

(h) Financial data 3D PCA embedding

Figure 1: Simulated Brownian-motion scenarios: time-series panels (a–g) and the corresponding 3D PCA embedding (h).

At each time tt we consider a window 𝒲t={Xs:s∈[t0,t]}\mathcal{W}\_{t}=\{X\_{s}:s\in[t\_{0},t]\} ( expanding) with |𝒲t|≥m0|\mathcal{W}\_{t}|\geq m\_{0} points and compute a local quadratic Monge patch fit,CazalsPouget2005; CohenSteiner2006,

|  |  |  |  |
| --- | --- | --- | --- |
|  | z=a​x2+b​x​y+c​y2+d​x+e​y+fover ​𝒲t,z\;=\;ax^{2}+bxy+cy^{2}+dx+ey+f\quad\text{over }\mathcal{W}\_{t}, |  | (25) |

by weighted least squares. Writing A=[x2,x​y,y2,x,y, 1]A=\big[x^{2},\,xy,\,y^{2},\,x,\,y,\,\mathbf{1}\big] and β=(a,b,c,d,e,f)⊤\beta=(a,b,c,d,e,f)^{\top},
the estimator is

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^t=arg⁡minβ⁡‖Wt​(A​β−z)‖22=(A⊤​Wt2​A)−1​A⊤​Wt2​z,\hat{\beta}\_{t}\;=\;\arg\min\_{\beta}\;\|W\_{t}(A\beta-z)\|\_{2}^{2}\;=\;(A^{\top}W\_{t}^{2}A)^{-1}A^{\top}W\_{t}^{2}z, |  | (26) |

where Wt=diag​(w1,…,w|𝒲t|)W\_{t}=\mathrm{diag}(\,w\_{1},\dots,w\_{|\mathcal{W}\_{t}|}\,) is optional exponential weighting
(*recent* samples weighted more), with wi∝e−α​(t−si)w\_{i}\propto e^{-\alpha(t-s\_{i})}.
Given a^t,b^t,c^t\hat{a}\_{t},\hat{b}\_{t},\hat{c}\_{t}, the *local Gaussian curvature* at time tt is (Monge gauge approximation),CazalsPouget2005,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt≈4​a^t​c^t−b^t2(1+4​a^t2+b^t2+4​c^t2)2.K\_{t}\;\approx\;\frac{4\hat{a}\_{t}\hat{c}\_{t}-\hat{b}\_{t}^{2}}{\big(1+4\hat{a}\_{t}^{2}+\hat{b}\_{t}^{2}+4\hat{c}\_{t}^{2}\big)^{2}}. |  | (27) |

Operationally, we pre-smooth (x,y,z)(x,y,z) (short moving average) and compute KtK\_{t} on an expanding or rolling window with a minimal sample size m0m\_{0} (see Appendix for defaults).

Towards validating that the method approximates satisfactorily the underlying Gaussian curvature, Fig. [2](https://arxiv.org/html/2511.05030v2#S3.F2 "Figure 2 ‣ 3.6 Local Gaussian Curvature Based Geometry Inference ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries") recovers the expected signatures on benchmarks—-K>0K>0 on S2S^{2}, mixed KK on T2T^{2}, and K<0K<0 on H2H^{2}—and yields plausible, intermittent curvature on the finance path; “uniformly sampled” means draws from each surface’s Riemannian (area) measure (density ∝d​A\propto dA).doCarmoRiemannian

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sphere ​S2​(R):\displaystyle\textbf{Sphere }S^{2}(R): | x​(θ,φ)=(R​cos⁡θ​sin⁡φ,R​sin⁡θ​sin⁡φ,R​cos⁡φ),\displaystyle x(\theta,\varphi)=\big(R\cos\theta\,\sin\varphi,\;R\sin\theta\,\sin\varphi,\;R\cos\varphi\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (θ,φ)∈[0,2​π)×[0,π],d​A=R2​sin⁡φ​d​θ​d​φ.\displaystyle(\theta,\varphi)\in[0,2\pi)\times[0,\pi],\hskip 18.49988ptdA=R^{2}\sin\varphi\,d\theta\,d\varphi. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Torus ​T2​(R,r):\displaystyle\textbf{Torus }T^{2}(R,r): | x​(θ,ϕ)=((R+r​cos⁡ϕ)​cos⁡θ,(R+r​cos⁡ϕ)​sin⁡θ,r​sin⁡ϕ),\displaystyle x(\theta,\phi)=\big((R+r\cos\phi)\cos\theta,\;(R+r\cos\phi)\sin\theta,\;r\sin\phi\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (θ,ϕ)∈[0,2​π)2,d​A=r​(R+r​cos⁡ϕ)​d​θ​d​ϕ.\displaystyle(\theta,\phi)\in[0,2\pi)^{2},\hskip 18.49988ptdA=r\,(R+r\cos\phi)\,d\theta\,d\phi. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hyperboloid:\displaystyle\textbf{Hyperboloid}: | x​(u,v)=(A​cosh⁡u​cos⁡v,A​cosh⁡u​sin⁡v,c​sinh⁡u),\displaystyle x(u,v)=\big(A\cosh u\cos v,\;A\cosh u\sin v,\;c\sinh u\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | v∈[0,2​π),u∈[umin,umax],d​A=A​cosh⁡u​A2​sinh2⁡u+c2​cosh2⁡u​d​u​d​v.\displaystyle v\in[0,2\pi),\;u\in[u\_{\min},u\_{\max}],\qquad dA=A\cosh u\,\sqrt{A^{2}\sinh^{2}u+c^{2}\cosh^{2}u}\,du\,dv. |  |

Practical uniform sampling:
(i) S2S^{2}: sample U,V∼Unif​(0,1)U,V\!\sim\!\mathrm{Unif}(0,1), set θ=2​π​U\theta=2\pi U, cos⁡φ=1−2​V\cos\varphi=1-2V.
(ii) T2T^{2}: sample θ∼Unif​[0,2​π)\theta\!\sim\!\mathrm{Unif}[0,2\pi) and ϕ\phi by rejection with target ∝R+r​cos⁡ϕ\propto R+r\cos\phi.
(iii) Hyperboloid: sample v∼Unif​[0,2​π)v\!\sim\!\mathrm{Unif}[0,2\pi) and uu on [umin,umax][u\_{\min},u\_{\max}] with target proportional to the uu–marginal of d​AdA.

![Refer to caption](images/curvature_plot_sphere.png)

(a) Sphere S2S^{2} (uniform sampling)

![Refer to caption](images/curvature_plot_torus.png)

(b) Torus T2T^{2} (uniform sampling)

![Refer to caption](images/curvature_plot_hyperboloid.png)

(c) Hyperboloid H2H^{2} (uniform sampling)

![Refer to caption](images/curvature_plot_ExpWindow_PCA_3D.png)

(d) Finance path (expanding-window PCA 3D)

Figure 2: Local Gaussian curvature estimates KK across benchmark shapes and the real-data embedded path. The benchmarks provide sign/scale references; the finance panel shows intermittent, regime-like curvature bursts.

##### Geometry decision from KtK\_{t}.

Since K>0K>0 on spheres, K<0K<0 on hyperbolic patches, and K≈0K\approx 0 in flat regions, we use thresholds 0<κ+≪10<\kappa\_{+}\ll 1, 0<κ−≪10<\kappa\_{-}\ll 1 to define

|  |  |  |
| --- | --- | --- |
|  | Sphere-like if, ​Kt≥κ+,\text{\bf Sphere-like if, }K\_{t}\geq\kappa\_{+},\quad |  |

|  |  |  |
| --- | --- | --- |
|  | Hyperbolic-like if, ​Kt≤−κ−,\text{\bf Hyperbolic-like if, }K\_{t}\leq-\kappa\_{-},\quad |  |

|  |  |  |
| --- | --- | --- |
|  | Flat (Euclidean-like) if, ​|Kt|<min⁡(κ+,κ−).\text{\bf Flat (Euclidean-like) if, }|K\_{t}|<\min(\kappa\_{+},\kappa\_{-}). |  |

However, tori are *mixed-curvature* surfaces (both signs occur), so we complement KtK\_{t} with a topological test.

##### Topological validation via persistent homology (Torus test).

We form a *Takens embedding*, Takens1981, over the window (Takens1981) 𝒲t\mathcal{W}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯t=[Xs,Xs−τ,…,Xs−(m−1)​τ]∈ℝ3​m,\mathcal{T}\_{t}\;=\;\big[\,X\_{s},\,X\_{s-\tau},\,\dots,\,X\_{s-(m-1)\tau}\,\big]\in\mathbb{R}^{3m}, |  | (28) |

with delay τ\tau and embedding dimension mm. We compute Vietoris Rips persistent homology of 𝒯t\mathcal{T}\_{t} and count persistent 1-cycles (Betti 11 features),EdelsbrunnerHarer2010; Ghrist2008. A torus satisfies β1=2\beta\_{1}=2 (and β2=1\beta\_{2}=1),EdelsbrunnerHarer2010, so we flag

|  |  |  |
| --- | --- | --- |
|  | Torus-like if ​#​{H1​ lifetimes>ϵ}≥2\text{\bf Torus-like if }\ \#\{\text{H}\_{1}\text{ lifetimes}>\epsilon\}\ \geq 2 |  |

|  |  |  |
| --- | --- | --- |
|  | (optionally: and ​#​{H2​ lifetimes>ϵ}≥1)\quad(\text{optionally: and }\#\{\text{H}\_{2}\text{ lifetimes}>\epsilon\}\geq 1) |  |

with persistence threshold ϵ\epsilon calibrated to the scale of the point cloud,Gidea2018; Ismail2022; Arvanitis2024. *In the current context, we implement the basic β1\beta\_{1}–based detector over sliding windows*.

##### Final geometry decision rule.

For each window:

|  |  |  |
| --- | --- | --- |
|  | If Torus-like: geometry =T2;\text{If Torus-like: geometry }=T^{2}; |  |

|  |  |  |
| --- | --- | --- |
|  | else if ​Kt≥κ+:S2;\text{else if }K\_{t}\geq\kappa\_{+}:S^{2}; |  |

|  |  |  |
| --- | --- | --- |
|  | else if ​Kt≤−κ−:H2;\text{else if }K\_{t}\leq-\kappa\_{-}:H^{2}; |  |

|  |  |  |
| --- | --- | --- |
|  | else: Euclidean. |  |

Notes. 
(i) We use expanding windows for stability on real data and rolling windows in stress tests;
(ii) exponential weighting (α>0\alpha>0) emphasizes recency in the quadratic fit;
(iii) the torus test can be run on the joint (x,y,z)(x,y,z) embedding or on the scalar curvature series KtK\_{t} (scalar Takens) with similar thresholds.

### 3.7 Forecasting in manifold space and baseline comparison

##### Manifold-aware forecasting

1. 1.

   *Regime inference:* Infer geometry using local gaussian curvature information - section [3.6](https://arxiv.org/html/2511.05030v2#S3.SS6 "3.6 Local Gaussian Curvature Based Geometry Inference ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")
2. 2.

   *Tangent velocities:* Compute vt=P​(Xt−1)​(Xt−Xt−1)v\_{t}=P(X\_{t-1})\,(X\_{t}-X\_{t-1}) to approximate intrinsic velocity.
3. 3.

   *Tangent PCA:* Project vtv\_{t} on top-dd principal axes to obtain coefficients ct∈ℝdc\_{t}\in\mathbb{R}^{d}.Jolliffe2002
4. 4.

   *Time-series models:* Fit VAR(pp), to {ct}\{c\_{t}\} and forecast c^t+1:t+h\hat{c}\_{t+1:t+h}. We use rolling window VAR(p=25p=25) in our application.
5. 5.

   *Lift back:* Reconstruct v^t+k\hat{v}\_{t+k} from c^t+k\hat{c}\_{t+k}, update X^t+k\hat{X}\_{t+k} on MM via expX^t+k−1⁡(v^t+k)\exp\_{\hat{X}\_{t+k-1}}(\hat{v}\_{t+k}) (or ambient step with projection), yielding path forecasts.

##### Baseline (Native-space) forecasting — explicit comparator.

We *explicitly compare* against a geometry-agnostic baseline that applies the same predictors *directly in the input space*: fit VAR to the raw ℝ3\mathbb{R}^{3} series {Xt}\{X\_{t}\} (or its first differences) without manifold embeddings or tangent/PCA steps, and produce X^t+1:t+hnative\hat{X}^{\text{native}}\_{t+1:t+h}. All training windows, horizons, and hyperparameters are matched to ensure a fair comparison. LopezDePrado2018AFML; Jansen2023; Jolliffe2002

Input time series
X1:T∈ℝ3X\_{1:T}\in\mathbb{R}^{3}

Geometry inference
Curvature KtK\_{t} + PH torus flag

Tangent velocity
vt=P​(Xt−1)​(Xt−Xt−1)v\_{t}=P(X\_{t-1})(X\_{t}-X\_{t-1})

Tangent PCA
ct∈ℝdc\_{t}\in\mathbb{R}^{d}

Forecasters
VAR / GP / RF on ctc\_{t}

Lift back
v^t+1→X^t+1\hat{v}\_{t+1}\!\rightarrow\!\hat{X}\_{t+1}

Allocation
Inverse-vol + tilt
Curvature gating
MM


Baseline (native space)
Inverse-vol and VAR/GP/RF directly on XtX\_{t}
No curvature/PH

Figure 3: Flow chart of the manifold-aware pipeline – geometry (MM) via curvature KtK\_{t} and persistent homology – with an explicit native-space baseline.

Sphere S2S^{2}Torus T2T^{2}Hyperbolic H2H^{2}Tx​S2T\_{x}S^{2}Ty​T2T\_{y}T^{2}Tz​H2T\_{z}H^{2}logx\log\_{x}expx\exp\_{x}logy\log\_{y}expy\exp\_{y}logz\log\_{z}expz\exp\_{z}


Tangent PCA ⇒\;\Rightarrow\; VAR / GP / RF forecasts ⇒\;\Rightarrow\; Lift back to manifold


Figure 4: Manifold embedding (log), tangent-space forecasting, and lifting (exp). Labels are placed *inside* the geometry boxes.

![Refer to caption](images/figure_sphere_logexp_predict.png)


Figure 5: Sphere S2S^{2}: log map to tangent at μ\mu, prediction v^\hat{v}, and lift X^=expμ⁡(v^)\hat{X}=\exp\_{\mu}(\hat{v}).

![Refer to caption](images/figure_torus_logexp_predict.png)


Figure 6: Torus T2T^{2}: log map, tangent-space prediction, and lifting back via expμ\exp\_{\mu}.

![Refer to caption](images/figure_hyperbolic_logexp_predict.png)


Figure 7: Hyperbolic H2H^{2}: log map, tangent-space prediction, and lifting via expμ\exp\_{\mu}.

### 3.8 Euclidean Null Control: Correlated Brownian Motions

To verify that our pipeline does *not* confuse linear factor structure (e.g., PCA geometry) with *intrinsic* manifold geometry, we run a Euclidean “null” experiment based on correlated Brownian motions. This control is designed to isolate what PCA can explain in a flat space and to demonstrate that our curvature/topology inference remains neutral (flat) when no curved geometry is present.

##### Construction (flat ℝn\mathbb{R}^{n} model).

Fix n≥3n\geq 3, horizon TT, and an equicorrelation level ρ∈[0,1)\rho\in[0,1).
Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σρ=ρ​ 11⊤+(1−ρ)​In(PSD, full-rank for ​ρ<1),\Sigma\_{\rho}\;=\;\rho\,\bm{1}\bm{1}^{\top}+(1-\rho)\,I\_{n}\qquad(\text{PSD, full-rank for }\rho<1), |  | (29) |

and let LL be a Cholesky factor of Σρ\Sigma\_{\rho}.
Generate i.i.d. standard normal innovations Zt∼𝒩​(0,In)Z\_{t}\sim\mathcal{N}(0,I\_{n}) and set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Wt=L​Zt∼𝒩​(0,Σρ),Wt=∑s=1tΔ​Ws,t=1,…,T.\Delta W\_{t}\;=\;L\,Z\_{t}\;\sim\;\mathcal{N}(0,\Sigma\_{\rho}),\qquad W\_{t}\;=\;\sum\_{s=1}^{t}\Delta W\_{s},\quad t=1,\dots,T. |  | (30) |

Thus {Wt}\{W\_{t}\} is a *multivariate Brownian motion in flat ℝn\mathbb{R}^{n}* with constant diffusion Σρ\Sigma\_{\rho} (no curvature, no manifold constraints).RevuzYor1999

##### What this controls for.

In the equicorrelation model, any structure is purely *linear correlation*. If one performs PCA on the cross-section,

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ1= 1+(n−1)​ρ,λ2=⋯=λn= 1−ρ,\lambda\_{1}\;=\;1+(n-1)\rho,\qquad\lambda\_{2}=\cdots=\lambda\_{n}\;=\;1-\rho, |  | (31) |

revealing one dominant “market” factor and n−1n{-}1 equal idiosyncratic directions. Projecting trajectories onto the top 2–3 PCs is a *linear* rotation/scale; it does *not* induce curvature.Jolliffe2002
Hence, if our method were merely “learning PCA’s geometry,” it would incorrectly report non-flat geometry here. The null control checks that it does not.

##### Embedding and diagnostics.

To match the rest of our pipeline, we form a 3D time series Xt∈ℝ3X\_{t}\in\mathbb{R}^{3} either by:
(i) selecting three coordinates of WtW\_{t}, or
(ii) projecting WtW\_{t} onto the first three PCs (purely linear compression).
On this 3D path we then compute:

1. 1.

   Local Gaussian curvature KtK\_{t} via a weighted quadratic Monge patch fit
   z=a​x2+b​x​y+c​y2+d​x+e​y+fz=ax^{2}+bxy+cy^{2}+dx+ey+f on rolling/expanding windows (Section [4.2](https://arxiv.org/html/2511.05030v2#S4.SS2 "4.2 Curvature statistics and regime assignment (finance path) ‣ 4 Results ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")).
2. 2.

   Topological torus test via Takens embedding and persistent homology
   (looking for two persistent H1H\_{1} cycles).

##### Expected outcome under the null.

Because the data live in an *affine* (flat) subspace:

* •

  Kt≈0K\_{t}\approx 0 up to finite-sample noise. For any small thresholds κ+,κ−>0\kappa\_{+},\kappa\_{-}>0,

  |  |  |  |
  | --- | --- | --- |
  |  | ℙ​(|Kt|<min⁡(κ+,κ−))​is high,\mathbb{P}\big(|K\_{t}|<\min(\kappa\_{+},\kappa\_{-})\big)\;\text{is high,} |  |

  so the decision rule classifies as *Euclidean/flat*.
* •

  The persistent homology *does not* show two long-lived 1-cycles, hence no torus flag.

##### Forecasting and allocation implications.

In a flat regime:

* •

  Tangent-space PCA of increments and native-space modeling are *effectively equivalent* (both are linear).
* •

  The curvature gating λt\lambda\_{t} satisfies λt≃1\lambda\_{t}\simeq 1 (no expansion/contraction).
* •

  Portfolio weights collapse to the baseline inverse-vol rule (plus any small return tilt), with no systematic advantage to manifold-aware steps.

This Euclidean null control demonstrates that our procedure *does not* mistake PCA’s linear factor structure for intrinsic manifold geometry. Curvature/topology estimators remain flat when the data-generating process is flat, and any gains observed in the main experiments arise from genuine nonlinear geometric structure rather than artifacts of linear dimension reduction.

### 3.9 Real-Finance Data Pipeline: Expanding PCA, Eigenportfolios, and Forecasting

We apply our methodology to a broad multi-asset universe (equities, sectors, rates, credit, commodities, volatility indices; full tickers in Appendix [A](https://arxiv.org/html/2511.05030v2#A1 "Appendix A Data Universe and Pre-processing ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")). Raw daily prices (Yahoo Finance) ; log-returns are formed and basic long-only (LO) and risk-parity (RP) benchmark series are computed for reference. The LO and RP benchmarks (the latter built via inverse-volatility scaling) are saved alongside the panel of returns for later comparison.

##### Expanding-window PCA and 3D embedding (eigenportfolios).

Let Rt∈ℝNR\_{t}\in\mathbb{R}^{N} denote the cross-section of asset returns at time tt. For t≥t0t\geq t\_{0}, we standardize the history {R1,…,Rt}\{R\_{1},\dots,R\_{t}\} and compute PCA loadings {u1,t,u2,t,u3,t}\{u\_{1,t},u\_{2,t},u\_{3,t}\} and eigenvalues {λ1,t,λ2,t,λ3,t}\{\lambda\_{1,t},\lambda\_{2,t},\lambda\_{3,t}\} on an *expanding* window (Jolliffe2002; Avellaneda2022; LopezDePrado2020MLAM. To avoid look-ahead, eigenportfolio ii at time tt uses the *lagged* loadings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi,t=ui,t−1⊤​Rt,i=1,2,3,p\_{i,t}\;=\;u\_{i,t-1}^{\top}R\_{t},\qquad i=1,2,3, |  | (32) |

so pi,tp\_{i,t} is the (out-of-sample) return of the iith eigenportfolio. Stacking the three principal sleeves yields a *3D embedded path* in cumulative form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=(∑s≤tp1,s,∑s≤tp2,s,∑s≤tp3,s)⊤∈ℝ3,X\_{t}\;=\;\Big(\,\sum\_{s\leq t}p\_{1,s},\ \sum\_{s\leq t}p\_{2,s},\ \sum\_{s\leq t}p\_{3,s}\,\Big)^{\top}\in\mathbb{R}^{3}, |  | (33) |

which serves as the input trajectory for our geometry-aware predictor. We display the expanding window curvature estimation for the PCA embedded financial dataset in Figure [8](https://arxiv.org/html/2511.05030v2#S3.F8 "Figure 8 ‣ Expanding-window PCA and 3D embedding (eigenportfolios). ‣ 3.9 Real-Finance Data Pipeline: Expanding PCA, Eigenportfolios, and Forecasting ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")

![Refer to caption](images/PCA_3D_Plot_and_Curvature.png)


Figure 8: PCA projections evolution (Upper panel) and curvature estimation (Lower panel) for the real financial dataset. xx is PC1 (1st eigenportfolio), yy is the PC2 (2nd eigenportfolio) and zz the PC3 projection (3rd eigenportfolio), respectively

##### Geometry signal on finance: local curvature on the PCA path.

On the 3D path XtX\_{t} we estimate the *local Gaussian curvature* KtK\_{t} by fitting quadratic Monge patches on rolling/expanding neighborhoods (Section [4.2](https://arxiv.org/html/2511.05030v2#S4.SS2 "4.2 Curvature statistics and regime assignment (finance path) ‣ 4 Results ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")). This series feeds the allocation rules and the curvature-aware benchmarks reported later.

##### Forecasting on the embedded path.

Given X1:tX\_{1:t}, we forecast the next embedded point X^t+1\widehat{X}\_{t+1} either (i) *natively in the 3D Euclidean path* or (ii) *geometry-aware* by choosing a geometry M∈{ℝ2,S2,T2,H2}M\in\{\mathbb{R}^{2},S^{2},T^{2},H^{2}\}, mapping to the tangent space via logμ\log\_{\mu}, forecasting principal tangent coefficients (VAR / GP / RF), and lifting back via expμ\exp\_{\mu} (Section [4.2](https://arxiv.org/html/2511.05030v2#S4.SS2 "4.2 Curvature statistics and regime assignment (finance path) ‣ 4 Results ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")).

##### Translating forecasts to trading signals and PnL.Maillard2010; Roncalli2013

Let Δ​Xt+1=Xt+1−Xt\Delta X\_{t+1}=X\_{t+1}-X\_{t} be realized 3D increments and Δ​X^t+1=X^t+1−Xt\widehat{\Delta X}\_{t+1}=\widehat{X}\_{t+1}-X\_{t}. We form directional, volatility-scaled signals on each coordinate k∈{x,y,z}k\in\{x,y,z\} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | sk,t+1=sign⁡(Δ​X^k,t+1)σ^k,ts\_{k,t+1}\;=\;\frac{\operatorname{sign}(\widehat{\Delta X}\_{k,t+1})}{\widehat{\sigma}\_{k,t}} |  | (34) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​X¯k,t(500)=1500​∑j=0499Δ​Xk,t−j,σ^k,t(500)=1499​∑j=0499(Δ​Xk,t−j−Δ​X¯k,t(500))2.\bar{\Delta X}\_{k,t}^{(500)}=\frac{1}{500}\sum\_{j=0}^{499}\Delta X\_{k,t-j},\qquad\widehat{\sigma}\_{k,t}^{(500)}=\sqrt{\frac{1}{499}\sum\_{j=0}^{499}\!\left(\Delta X\_{k,t-j}-\bar{\Delta X}\_{k,t}^{(500)}\right)^{2}}\,. |  | (35) |

and computes coordinate PnL by pnlk,t+1=sk,t+1​Δ​Xk,t+1\,\mathrm{pnl}\_{k,t+1}=s\_{k,t+1}\,\Delta X\_{k,t+1}\,.
  
  
Annualized Sharpe ratios, Sh​[]\mathrm{Sh}[], are reported as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sh​[pnlk]=252​pnl¯kstdev​(pnlk),pnlTot,t=∑k∈{x,y,z}pnlk,t.\mathrm{Sh}[\mathrm{pnl}\_{k}]\;=\;\sqrt{252}\,\frac{\overline{\mathrm{pnl}}\_{k}}{\mathrm{stdev}(\mathrm{pnl}\_{k})}\,,\qquad\mathrm{pnl}\_{\text{Tot},t}\;=\;\sum\_{k\in\{x,y,z\}}\mathrm{pnl}\_{k,t}. |  | (36) |

### 3.10 Eigenvalue-Weighted Sleeves from *3D PCA Space* (Expanding SVD)

In the finance application we first build the *embedded 3D PCA path* of eigenportfolios
(Section [3.9](https://arxiv.org/html/2511.05030v2#S3.SS9 "3.9 Real-Finance Data Pipeline: Expanding PCA, Eigenportfolios, and Forecasting ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")): for each date tt we have

|  |  |  |
| --- | --- | --- |
|  | Xt=(X1,t,X2,t,X3,t)⊤∈ℝ3,X\_{t}\;=\;\big(X\_{1,t},\,X\_{2,t},\,X\_{3,t}\big)^{\top}\in\mathbb{R}^{3}, |  |

where the coordinates are the out-of-sample cumulative eigenportfolio sleeves (PC1, PC2, PC3). *Then*, within this 3D space, we compute an *expanding-window SVD/PCA* to obtain time-varying variance levels and use those *3D-space eigenvalues* to weight the sleeves,Jolliffe2002.

Let Δ​Xs:=Xs−Xs−1\Delta X\_{s}:=X\_{s}-X\_{s-1} and fix an expanding window 𝒲t={1,…,t}\mathcal{W}\_{t}=\{1,\dots,t\}.
Define the 3×33\times 3 sample covariance on 𝒲t\mathcal{W}\_{t},

|  |  |  |
| --- | --- | --- |
|  | Σt(3​D)=1|𝒲t|​∑s∈𝒲t(Δ​Xs−Δ​X¯t)​(Δ​Xs−Δ​X¯t)⊤,Δ​X¯t=1|𝒲t|​∑s∈𝒲tΔ​Xs.\Sigma^{(3D)}\_{t}\;=\;\frac{1}{|\mathcal{W}\_{t}|}\sum\_{s\in\mathcal{W}\_{t}}\big(\Delta X\_{s}-\overline{\Delta X}\_{t}\big)\big(\Delta X\_{s}-\overline{\Delta X}\_{t}\big)^{\top},\qquad\overline{\Delta X}\_{t}=\frac{1}{|\mathcal{W}\_{t}|}\sum\_{s\in\mathcal{W}\_{t}}\Delta X\_{s}. |  |

Compute the spectral decomposition (equivalently, SVD of the 3×|𝒲t|3\times|\mathcal{W}\_{t}| matrix of Δ​Xs\Delta X\_{s})

|  |  |  |
| --- | --- | --- |
|  | Σt(3​D)=Qt​Λt​Qt⊤,Λt=diag​(λ1​(t),λ2​(t),λ3​(t)),λ1​(t)≥λ2​(t)≥λ3​(t)≥0.\Sigma^{(3D)}\_{t}\;=\;Q\_{t}\,\Lambda\_{t}\,Q\_{t}^{\top},\qquad\Lambda\_{t}=\mathrm{diag}\!\big(\lambda\_{1}(t),\lambda\_{2}(t),\lambda\_{3}(t)\big),\;\;\lambda\_{1}(t)\!\geq\!\lambda\_{2}(t)\!\geq\!\lambda\_{3}(t)\!\geq\!0. |  |

These λi​(t)\lambda\_{i}(t) are the *expanding-window eigenvalues in the 3D PCA space*

##### Eigenvalue-driven sleeve weights in 3D space.

We map the variance levels into normalized sleeve weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci,t=λi​(t)λ1​(t)+λ2​(t)+λ3​(t),i=1,2,3,C\_{i,t}\;=\;\frac{\lambda\_{i}(t)}{\lambda\_{1}(t)+\lambda\_{2}(t)+\lambda\_{3}(t)}\,,\qquad i=1,2,3, |  | (37) |

so that directions with larger expanding-window energy in the 3D PCA space receive higher allocation.

##### Forecast integration and portfolio return.

Let X^t+1\widehat{X}\_{t+1} be the predicted point from either (i) the *native-space* forecaster, or
(ii) the *geometry-aware* (log–forecast–exp) forecaster; define
Δ​X^i,t+1=X^i,t+1−Xi,t\widehat{\Delta X}\_{i,t+1}=\widehat{X}\_{i,t+1}-X\_{i,t} and the directional signal
si,t+1=sign​(Δ​X^i,t+1)s\_{i,t+1}=\mathrm{sign}(\widehat{\Delta X}\_{i,t+1}). The eigenvalue-weighted eigenportfolio return is

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1(eig, 3​D)=∑i=13Ci,t​si,t+1​pi,t+1,pi,t+1​ the out-of-sample return of sleeve ​i.r^{(\mathrm{eig},\,3D)}\_{t+1}\;=\;\sum\_{i=1}^{3}C\_{i,t}\;s\_{i,t+1}\;p\_{i,t+1},\qquad p\_{i,t+1}\text{ the out-of-sample return of sleeve }i. |  | (38) |

All evaluation metrics (MAE/RMSE/Sign, Sharpe, cumulative PnL) are computed identically across (i) and (ii) to ensure a fair comparison; results are reported in Section [4](https://arxiv.org/html/2511.05030v2#S4 "4 Results ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries").SimonianLopezdePradoFabozzi2024

##### Design intent.

This makes the *allocation* responsive to the *expanding-window variance structure *of the 3D PCA space itself** (via λi​(t)\lambda\_{i}(t)), while the *forecasting layer* tests whether geometry-aware predictions improve the *directional timing* si,t+1s\_{i,t+1} relative to a Euclidean baseline.

##### Curvature-aware aggregation and geometry-weighted benchmarks.

Beyond the pure RP eigenportfolios framework, we also report:
(i) a *curvature-gated* aggregation that buckets timestamps by KtK\_{t} (negative/near-zero/positive) and averages the appropriate geometry-run PnLs (torus / Euclidean / all geometries) and
(ii) expanding-window geometry weighting by ex-post Sharpe/returns as a sanity check. These appear in the merged report alongside LO and RP asset benchmarks.

Design intent.
This setup ensures the following:
(i) the 3D embedding reflects *time-varying* linear structure (eigenportfolios) while all *nonlinear* effects are captured by curvature/topology on the embedded path;
(ii) forecasts are compared *like-for-like* against a native-space baseline that applies the same predictors without manifold steps; and
(iii) portfolio construction is neutral (inverse-vol) and modular curvature gating is reported separately so its incremental value can be isolated.

## 4 Results

### 4.1 ’Forecast to Trading’ Evaluation Design

We assess the methodology on (i) *simulated* regimes and (ii) *real finance* data (Section [3.9](https://arxiv.org/html/2511.05030v2#S3.SS9 "3.9 Real-Finance Data Pipeline: Expanding PCA, Eigenportfolios, and Forecasting ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")). Because trading payoff is highly sensitive to *direction*, we report both statistical errors (MAE/RMSE) and trading metrics (Sharpe/Sortino/Calmar, hit-rate). All comparisons are *like-for-like* between:

* •

  Native-space forecasts in the 3D PCA embedding, and
* •

  Geometry-aware forecasts (log–-forecast-–exp) on M∈{ℝ2,S2,T2,H2}M\in\{\mathbb{R}^{2},S^{2},T^{2},H^{2}\}.

Inputs, windows, and forecaster class are held fixed across arms.

### 4.2 Curvature statistics and regime assignment (finance path)

Using the expanding-window estimator on the 3D PCA path, we analyze the series {Kt}\{K\_{t}\} (4491 non-missing points, from 2007 to 2025). Basic distributional facts:

|  |  |  |
| --- | --- | --- |
|  | mean​(K)=−0.0207,sd​(K)=0.0186,\text{mean}(K)=-0.0207,\quad\text{sd}(K)=0.0186,\quad |  |

|  |  |  |
| --- | --- | --- |
|  | min⁡K=−0.125,Q25=−0.0247,Q50=−0.0186,\min K=-0.125,\quad\mathrm{Q}\_{25}=-0.0247,\ \mathrm{Q}\_{50}=-0.0186,\ |  |

|  |  |  |
| --- | --- | --- |
|  | Q75=−0.0088,max⁡K=0.0142.\mathrm{Q}\_{75}=-0.0088,\ \max K=0.0142. |  |

With curvature thresholds (κ+,κ−)=(+0.01,−0.01)(\kappa\_{+},\kappa\_{-})=(+0.01,-0.01), the time share by regime is:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Kt≤κ−)⏟hyperbolic-like=73.9%,ℙ​(|Kt|≤0.01)⏟near-flat=24.4%,ℙ​(Kt≥κ+)⏟spherical-like=1.7%.\underbrace{\mathbb{P}(K\_{t}\leq\kappa\_{-})}\_{\text{hyperbolic-like}}=73.9\%,\qquad\underbrace{\mathbb{P}(|K\_{t}|\leq 0.01)}\_{\text{near-flat}}=24.4\%,\qquad\underbrace{\mathbb{P}(K\_{t}\geq\kappa\_{+})}\_{\text{spherical-like}}=1.7\%. |  |

At looser thresholds (e.g., τ=0.005\tau=0.005) the near-flat share rises to 18.4%18.4\% and the positive share remains small (3.3%3.3\%), while 78.3%78.3\% remains negative. Serial dependence is strong (ACF(1)=0.997=0.997), indicating *persistent* curvature regimes rather than high-frequency noise.

##### Time segmentation (annual shares, τ=0.01\tau=0.01).

A compact, label-based classification by year assigns “hyperbolic-like” when ℙ​(Kt≤−0.01)>50%\mathbb{P}(K\_{t}\leq-0.01)>\!50\% and ℙ​(Kt≥0.01)<10%\mathbb{P}(K\_{t}\geq 0.01)<10\%; “Euclidean/flat-like” when ℙ​(|Kt|≤0.01)>60%\mathbb{P}(|K\_{t}|\leq 0.01)>\!60\% and both tails are small; and “torus-like (mixed)” when both tails are material (>10%>\!10\% each). The resulting picture is:

* •

  2007–-2010: Euclidean/flat-like (near-flat share dominates; mean KK mild negative).
* •

  2011––2020: Hyperbolic-like (negative curvature dominates; virtually no positive tail).
* •

  2021: *Torus-like (mixed)* — ℙ​(Kt≤−0.01)≈48%\mathbb{P}(K\_{t}\leq-0.01)\approx 48\%, ℙ​(|Kt|≤0.01)≈25%\mathbb{P}(|K\_{t}|\leq 0.01)\approx 25\%, ℙ​(Kt≥0.01)≈26%\mathbb{P}(K\_{t}\geq 0.01)\approx 26\%.
* •

  2022–-2025: Strongly hyperbolic-like (negative share ≈100%\approx 100\%, increasingly negative mean KK).

##### Interpretation.

At face value, the *sign* distribution is skewed negative (hyperbolic-like), but two features align with a *toroidal scaffold* dominating the overall dynamics:
(i) the presence of both negative and positive curvature episodes (albeit asymmetric), and
(ii) extended stretches of near-flat curvature between negative bursts.
On a standard torus T2​(R,r)T^{2}(R,r) the Gaussian curvature varies with the minor angle ϕ\phi,

|  |  |  |
| --- | --- | --- |
|  | K​(ϕ)=cos⁡ϕr​[R+r​cos⁡ϕ],K(\phi)=\frac{\cos\phi}{r\,[R+r\cos\phi]}, |  |

so trajectories that spend more time near the inner saddle (ϕ≈π\phi\!\approx\!\pi) naturally produce a distribution with large negative mass, occasional small positive excursions (outer bulge, ϕ≈0\phi\!\approx\!0), and plateaus near K≈0K\!\approx\!0 when the path lingers on transition bands. This is exactly what we observe: long negative runs (median run length ≈14\approx 14 time points; max ∼3000\sim 3000), short positive runs (median ≈3\approx 3), and nontrivial flat intervals.

Assignment. Aggregating across 2007 to 2025, the curvature statistics point to *hyperbolic-biased toroidal dynamics*: topologically consistent with one (or multiple) torii, but with the path predominantly visiting the saddle side (negative KK), punctuated by mixed-curvature episodes (notably 2021) and near-flat interludes. This reconciles (a) the dominance of negative curvature in the estimator with (b) the empirical finding that toroidal embeddings often deliver the strongest predictive sleeves and portfolio lift when those mixed/periodic phases emerge.

### 4.3 Topological validation via persistent homology

We provide a topological check for *toroidal* behavior in the real-data embedding by estimating the homology of a delay-embedded attractor (Takens’ embedding, Takens1981) built from the 3D PCA path (and, where informative, from individual sleeves). The exhibit comprises: (i) a Takens attractor plot and (ii) persistent homology summaries (diagrams/barcodes) up to H2H\_{2}. The torus test is *heuristic but informative*: a T2T^{2}-like attractor typically shows one connected component (β0=1\beta\_{0}\!=\!1), *two* long-lived 1-cycles (β1≈2\beta\_{1}\!\approx\!2), and, in dense surface samples, a weak 2-class (β2≈1\beta\_{2}\!\approx\!1). Trajectory samples often recover the two H1H\_{1} classes cleanly, with H2H\_{2} less stable.

##### Takens embedding and filtration.

Given a univariate coordinate xtx\_{t} (e.g., a PCA sleeve) or a multivariate series Xt∈ℝ3X\_{t}\in\mathbb{R}^{3}, we construct a delay map

|  |  |  |
| --- | --- | --- |
|  | 𝒯m,τ​(xt)=(xt,xt−τ,…,xt−(m−1)​τ)∈ℝm,\mathcal{T}\_{m,\tau}(x\_{t})=\big(x\_{t},\ x\_{t-\tau},\ \dots,\ x\_{t-(m-1)\tau}\big)\in\mathbb{R}^{m}, |  |

(or stack sleeves to get ℝ3​m\mathbb{R}^{3m}), choose (m,τ)(m,\tau) via standard criteria (mutual information / first ACF minimum; false nearest neighbors), standardize the cloud, and compute Vietoris–Rips persistence up to dimension 2. We summarize HkH\_{k} by lifetimes ℓ=b−d\ell=b-d (birth bb, death dd), the number of long bars, and null-comparisons.

![Refer to caption](images/H1_max_lifetime_timeseries.png)

(a) H1 max lifetime (time series)

![Refer to caption](images/n_persistent_H1_timeseries.png)

(b) # persistent H1 loops (time series)

![Refer to caption](images/torus_flag_annual_bar.png)

(c) Annual share of torus-flagged windows

![Refer to caption](images/scatter_H1max_vs_nH1.png)

(d) H1 max lifetime vs #H1 loops (flag split)

Figure 9: Persistent homology diagnostics on the real-data embedding. High *H1* lifetimes (a) co-occur with elevated counts of persistent 1-cycles (b); year-by-year, torus-like intervals dominate (c). The moderate positive association in (d) indicates that when the two principal loops of a torus persist strongly, overall 1-dimensional topological activity is also elevated.

##### Topological evidence for a torus-like manifold (real data).

Visual inspection of the emerged torus-like shape is displayed in Figure [10](https://arxiv.org/html/2511.05030v2#S4.F10 "Figure 10 ‣ Topological evidence for a torus-like manifold (real data). ‣ 4.3 Topological validation via persistent homology ‣ 4 Results ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries"). The behavior directs us on thinking more heavily on the existence of multiple torii, with different radii ’stitched’ together in a ’smooth’ way – a statement which we try to quantify using the TDA analysis below.

![Refer to caption](images/takens_attractor.png)


Figure 10: Taken’s embedding and the emergence of a torus-like shape

Under the computational topological data analysis framework, across 4,251 windows, the torus test is satisfied in 88.4% of cases, with 20 contiguous “torus” runs; the three longest spans (2007–2013, 2015–2019, 2021–2023) show elevated topological persistence (e.g., mean H1H\_{1} max lifetime up to 1.34 in 2021–2023). A moderate association between H1H\_{1} max lifetime and the number of persistent 1-cycles (ρ=0.374\rho\!=\!0.374) suggests that when the two principal loops are strong, overall 1D topological activity is also high. Taken together, these diagnostics are *consistent with* a torus-like, two-cycle latent geometry dominating much of the sample, in line with the curvature analysis.

We call an interval *torus-like* if, on a sliding window, the following hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | #​{long H1 bars}≥2,ℓ1(1)+ℓ2(1)∑jℓj(1)≥ρ⋆,ℓ2(1)≥q0.95null,\#\{\text{long $H\_{1}$ bars}\}\ \geq 2,\qquad\frac{\ell^{(1)}\_{1}+\ell^{(1)}\_{2}}{\sum\_{j}\ell^{(1)}\_{j}}\ \geq\ \rho\_{\star},\qquad\ell^{(1)}\_{2}\geq q\_{0.95}^{\text{null}}, |  | (39) |

where ℓ1(1)≥ℓ2(1)\ell^{(1)}\_{1}\geq\ell^{(1)}\_{2} are the top two H1H\_{1} lifetimes, ρ⋆∈[0.4,0.7]\rho\_{\star}\in[0.4,0.7] is a concentration threshold, and q0.95nullq\_{0.95}^{\text{null}} is the 95th percentile of the top-H1H\_{1} lifetime computed from a *null ensemble* preserving low-order statistics (e.g., phase-randomized surrogates or equicorrelated Brownian surrogates). This controls for spurious loops created by noise or purely Euclidean drift.

### 4.4 Trading Translation and PnL Construction

Let Xt=(X1,t,X2,t,X3,t)⊤X\_{t}=(X\_{1,t},X\_{2,t},X\_{3,t})^{\top} be the expanding-PCA 3D path of eigenportfolio cumulatives and X^t+1\widehat{X}\_{t+1} the one step ahead prediction.

##### Directional signals.

For sleeve i∈{1,2,3}i\in\{1,2,3\} define the predicted increment and sign:

|  |  |  |
| --- | --- | --- |
|  | Δ​X^i,t+1=X^i,t+1−Xi,t,si,t+1=sign⁡(Δ​X^i,t+1)∈{−1,0,1}.\widehat{\Delta X}\_{i,t+1}=\widehat{X}\_{i,t+1}-X\_{i,t},\qquad s\_{i,t+1}=\operatorname{sign}\big(\widehat{\Delta X}\_{i,t+1}\big)\in\{-1,0,1\}. |  |

##### 500-day volatility scale (per sleeve).

With trailing window 500,

|  |  |  |
| --- | --- | --- |
|  | Δ​X¯i,t(500)=1500​∑j=0499Δ​Xi,t−j,σ^i,t(500)=1499​∑j=0499(Δ​Xi,t−j−Δ​X¯i,t(500))2.\bar{\Delta X}\_{i,t}^{(500)}=\frac{1}{500}\sum\_{j=0}^{499}\Delta X\_{i,t-j},\quad\widehat{\sigma}\_{i,t}^{(500)}=\sqrt{\frac{1}{499}\sum\_{j=0}^{499}\big(\Delta X\_{i,t-j}-\bar{\Delta X}\_{i,t}^{(500)}\big)^{2}}. |  |

##### Coordinate PnL and total.

The volatility scaled PnL of sleeve ii is

|  |  |  |
| --- | --- | --- |
|  | pnli,t+1=si,t+1σ^i,t(500)​Δ​Xi,t+1,pnlTot,t+1=13​∑i=13pnli,t+1,\mathrm{pnl}\_{i,t+1}=\frac{s\_{i,t+1}}{\widehat{\sigma}\_{i,t}^{(500)}}\,\Delta X\_{i,t+1},\qquad\mathrm{pnl}\_{\mathrm{Tot},t+1}=\tfrac{1}{3}\sum\_{i=1}^{3}\mathrm{pnl}\_{i,t+1}, |  |

with annualized Sharpe Sh=252​pnl¯/stdev​(pnl)\mathrm{Sh}=\sqrt{252}\,\overline{\mathrm{pnl}}/\mathrm{stdev}(\mathrm{pnl}).
For *eigenvalue weighted* sleeves (Section [3.10](https://arxiv.org/html/2511.05030v2#S3.SS10 "3.10 Eigenvalue-Weighted Sleeves from 3D PCA Space (Expanding SVD) ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")), we also form

|  |  |  |
| --- | --- | --- |
|  | rt+1(eig,3​D)=∑i=13Ci,t​si,t+1​pi,t+1,Ci,t=λi​(t)∑j=13λj​(t),r^{(\mathrm{eig},3D)}\_{t+1}=\sum\_{i=1}^{3}C\_{i,t}\,s\_{i,t+1}\,p\_{i,t+1},\quad C\_{i,t}=\frac{\lambda\_{i}(t)}{\sum\_{j=1}^{3}\lambda\_{j}(t)}, |  |

where pi,t+1p\_{i,t+1} is the out-of-sample eigenportfolio return and λi​(t)\lambda\_{i}(t) are the expanding-window *3D-space* eigenvalues.Bailey2014DSR; Bailey2014PBO

### 4.5 Simulated Regimes: Cross–Manifold Performance

Table 1: Cross–manifold performance on simulated data,Hsu2002; doCarmoRiemannian. Best MAE/RMSE/MAPE and Sharpe per data–manifold block highlighted.

| Data Manifold | MAE | RMSE | MAPE (%) | Sharpe Ratios (x,y,z) | Model Geometry |
| --- | --- | --- | --- | --- | --- |
| 𝕊2\mathbb{S}^{2} | 0.100.10 | 0.670.67 | 304.20304.20 | 0.021, −-0.020, −-0.301 | VAR (ℝ3\mathbb{R}^{3}) |
| 0.260.26 | 0.300.30 | 153.19153.19 | −-0.158, −-0.207, −-0.484 | 𝕊2\mathbb{S}^{2} GIM |
| 0.390.39 | 0.510.51 | 205.47205.47 | −-0.199, −-0.282, 0.215 | 𝕋2\mathbb{T}^{2} GIM |
| 0.02 | 0.04 | 49.59 | 0.407, 0.022, 0.020 | ℍ2\mathbb{H}^{2} GIM |
| 𝕋2\mathbb{T}^{2} | 11.1911.19 | 321.87321.87 | 24 693.7724\,693.77 | −-0.119, 0.590, 0.228 | VAR (ℝ3\mathbb{R}^{3}) |
| 0.71 | 0.99 | 245.98 | 1.871, 2.777, 2.483 | 𝕊2\mathbb{S}^{2} GIM |
| 0.900.90 | 1.321.32 | 554.40554.40 | −-0.817, −-0.751, 0.502 | 𝕋2\mathbb{T}^{2} GIM |
| 0.770.77 | 1.131.13 | 383.95383.95 | 1.425, 1.896, −-0.067 | ℍ2\mathbb{H}^{2} GIM |
| ℝ3\mathbb{R}^{3} | 0.130.13 | 0.860.86 | 636.79636.79 | −-0.018, 0.129, −-0.009 | VAR (ℝ3\mathbb{R}^{3}) |
| 0.200.20 | 0.280.28 | 376.74376.74 | −-0.152, 0.038, −-0.580 | 𝕊2\mathbb{S}^{2} GIM |
| 0.380.38 | 0.510.51 | 871.02871.02 | −-0.336, −-0.086, 0.052 | 𝕋2\mathbb{T}^{2} GIM |
| 0.030.03 | 0.050.05 | 118.70118.70 | −-0.195, 0.141, −-0.104 | ℍ2\mathbb{H}^{2} GIM |
| ℍ2\mathbb{H}^{2} | 0.840.84 | 18.5318.53 | 1066.881066.88 | 0.074, 0.186, −-0.056 | VAR (ℝ3\mathbb{R}^{3}) |
| 0.220.22 | 0.280.28 | 203.06203.06 | 0.116, 0.421, 0.252 | 𝕊2\mathbb{S}^{2} GIM |
| 0.360.36 | 0.470.47 | 311.37311.37 | −-0.400, −-0.458, 0.276 | 𝕋2\mathbb{T}^{2} GIM |
| 0.12 | 0.21 | 131.43 | 0.381, 0.037, 0.014 | ℍ2\mathbb{H}^{2} GIM |

### 4.6 Validation on Correlated Brownian Motions – CBMs (Euclidean Null)

To check that geometry performance is not a PCA artifact, we evaluate on equicorrelated CBMs projected to 3D .

##### High correlation ρ=0.9\rho=0.9:

* •

  Euclidean: Total Sharpe 0.211\mathbf{0.211}
* •

  Spherical: −0.119-0.119  Toroidal: −0.172-0.172  Hyperbolic: −0.109-0.109

##### Moderate correlation ρ=0.6\rho=0.6:

* •

  Toroidal: Total Sharpe 0.273\mathbf{0.273}
* •

  Euclidean: 0.0970.097  Spherical: −0.337-0.337  Hyperbolic: −0.310-0.310

##### Summary.

On *flat* CBMs (ρ=0.9\rho{=}0.9), Euclidean dominates; with weaker correlation (ρ=0.6\rho{=}0.6) a toroidal slice can outperform, consistent with cyclical structure emerging after projection. Together with Section [3.8](https://arxiv.org/html/2511.05030v2#S3.SS8 "3.8 Euclidean Null Control: Correlated Brownian Motions ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries"), these controls indicate that the gains reported earlier in the real financial data are associated with *intrinsic* curvature/cyclicity captured by the manifold step, not PCA alone.

### 4.7 Financial Data: Coordinate Sharpe by Geometry,Maillard2010; Roncalli2013

Table 2: Sharpe ratios by geometry and coordinate (from prior version; reported as-is). Best per column in bold.

| Geometry | xx | yy | zz | Total |
| --- | --- | --- | --- | --- |
| Euclidean (E) | −0.112-0.112 | −0.368-0.368 | −0.442-0.442 | −0.322-0.322 |
| Spherical (S) | 0.177 | 0.338 | −0.037-0.037 | 0.273 |
| Toroidal (T) | 0.161 | −0.252-0.252 | 0.721 | 0.274 |
| Hyperbolic (H) | −0.094-0.094 | −0.284-0.284 | 0.357 | −0.065-0.065 |

To put these results in context, we compare the geometry-informed strategies against conventional benchmark portfolios: the equally weighted long only (LO) portfolio of all assets, and a risk parity portfolio (RP) that balances contributions to volatility. Over the same 2005 to 2025 period, the equally weighted portfolio achieved a Sharpe ratio of roughly 0.39 and the RP portfolio about 0.44. The standout is the toroidal zz coordinate (Sharpe 0.7210.721), consistent with a latent *cyclic* component amplified by a T2T^{2} embedding. In other words, a trading strategy informed by the toroidal geometry signals would have outperformed a passive diversified portfolio, highlighting the practical value of the geometric approach. Notably, even the spherical model’s Sharpe (0.270.27) is on par with the benchmarks, while the Euclidean forecast model’s negative Sharpe is clearly inferior. These findings reinforce that embedding financial time series in an appropriate curved space can extract predictive signals that traditional methods overlook. (Summary table of best performing strategies vs benchmarks in Table [3](https://arxiv.org/html/2511.05030v2#S4.T3 "Table 3 ‣ 4.7 Financial Data: Coordinate Sharpe by Geometry,Maillard2010; Roncalli2013 ‣ 4 Results ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries"),Avellaneda2022)

Table 3: Summary Table : Strategy-level Sharpe ratios (2005–-2025). Geometry-Informed Modeling (GIM) variants vs. benchmarks.

|  |  |
| --- | --- |
| Strategy (configuration) | Sharpe |
| GIM (integrated: eigenvalue weighting + curvature gating) | 0.64 |
| Long-Only benchmark (equally weighted) | 0.3900.390 |
| Risk Parity benchmark (inverse-vol) | 0.4390.439 |
| Native PCA VAR (Euclidean baseline, weighted) | −0.386-0.386 |
| Best single sleeve (toroidal zz-coordinate) | 0.721 |

The toroidal zz-sleeve (0.721) is a *concentrated, ex post* winner; it fully loads on one predictive direction and enjoys the strongest regime episodes, but it also carries higher *selection risk* and sensitivity to geometry mis–specification. By contrast, the integrated GIM (0.64) is an *ex ante ensemble* that (i) diversifies across sleeves via expanding-–SVD eigenvalue weights, (ii) applies curvature gating to scale risk in adverse geometry, and (iii) hedges against transient regime flips. These safeguards intentionally trade a slice of peak Sharpe for *stability, lower selection error, and reduced drawdown/turnover*. In other words, the single best sleeve sets a performance *upper bound* for that specific regime, whereas the integrated portfolio is designed to be more robust across regimes. As an upgrade, we could tune this trade-off by shrinking the curvature gate or increasing the “temperature” of eigenvalue weights to move the ensemble closer to the concentrated sleeve – leaving this to be part of our future research on the topic.

##### Integrated GIM (eigenvalue + curvature) outperforms all baselines.

When we combine the geometry aware forecaster with *expanding-–SVD eigenvalue weighting* of sleeves (Ci,tC\_{i,t} from the 3D PCA space) and *curvature gating* of the risk budget (with torus split when flagged), the full GIM attains an annualized Sharpe of around 0.64 on the real data test set—-*the highest across all configurations*. This exceeds the RP baseline (0.4390.439, +0.199+\!0.199), and LO (0.3900.390, +0.248+\!0.248), and dominates the native space baselines (−0.386/−0.289-0.386/-0.289). The lift is consistent with (i) concentrating exposure on currently energetic modes via λi​(t)\lambda\_{i}(t), (ii) scaling total risk with regime curvature (λt\lambda\_{t} expands in trending/negative-–curvature phases and contracts in mean reverting/positive curvature phases), and (iii) honoring toroidal two-–cycle structure when present. Because inputs, predictors, and PnL translation are held fixed relative to the baselines, these gains isolate the added value of *geometry informed variance structure and regime awareness*.

#### 4.7.1 Augmenting VAR with machine-learning predictors

To test whether generic nonlinear learning methods can extract residual structure beyond the manifold-informed VAR, we extended the tangent-space forecasting system by incorporating *Random Forest (RF)* and *Gaussian Process Regression (GP)* models as auxiliary predictors.
Specifically, each manifold coordinate (x,y,z)(x,y,z) was forecasted using VAR, RF, and GP individually, and their outputs were combined through a linear ensemble to assess whether local nonlinearities not captured by the linear VAR could improve out-of-sample predictive accuracy.

While both RF and GP models offer flexible functional forms, their results show only marginal differences relative to the baseline VAR.
Table [4](https://arxiv.org/html/2511.05030v2#S4.T4 "Table 4 ‣ 4.7.1 Augmenting VAR with machine-learning predictors ‣ 4.7 Financial Data: Coordinate Sharpe by Geometry,Maillard2010; Roncalli2013 ‣ 4 Results ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries") summarizes their performance across geometries.
In both setups, the toroidal configuration continues to dominate with Sharpe ratios in the range 0.380.38–0.470.47, whereas Euclidean and spherical geometries remain negative, and hyperbolic slightly positive.
This finding suggests that the core predictive information arises primarily from the manifold’s geometric organization rather than from generic nonlinear learners.

Table 4: Comparative forecasting performance (Sharpe ratios) for manifold geometries using Gaussian Process (GP) and Random Forest (RF) predictors (2005–2025).

|  |  |  |
| --- | --- | --- |
| Geometry / Coordinate | GP | RF |
| xx (Euclidean) | −0.1039-0.1039 | 0.02920.0292 |
| yy (Euclidean) | 0.00090.0009 | −0.2689-0.2689 |
| zz (Euclidean) | −0.4099-0.4099 | −0.5331-0.5331 |
| xx (Sphere) | −0.0326-0.0326 | −0.0318-0.0318 |
| yy (Sphere) | 0.22500.2250 | 0.25470.2547 |
| zz (Sphere) | −0.3606-0.3606 | −0.3709-0.3709 |
| xx (Torus) | 0.30130.3013 | 0.22300.2230 |
| yy (Torus) | −0.2570-0.2570 | −0.1551-0.1551 |
| zz (Torus) | 0.4052 | 0.4867 |
| xx (Hyperbolic) | 0.09650.0965 | −0.1095-0.1095 |
| yy (Hyperbolic) | 0.03120.0312 | −0.1599-0.1599 |
| zz (Hyperbolic) | 0.09460.0946 | 0.17320.1732 |
| Aggregate by Geometry |  |  |
| Euclidean | −0.3965-0.3965 | −0.5403-0.5403 |
| Sphere | −0.3484-0.3484 | −0.3560-0.3560 |
| Torus | 0.3783 | 0.4677 |
| Hyperbolic | 0.09820.0982 | 0.15110.1511 |

* •

  Note. Both Gaussian Process and Random Forest regressors cannot provide any significant marginal improvements relative to the geometry-informed VAR baseline. The toroidal configuration remains the most predictive, consistent with the cyclic market dynamics revealed by curvature analysis.

## 5 Discussion and Future Research

### 5.1 IS–LM foundations for (multi-)torus dynamics: a mathematical sketch

##### Caveat.

The connection we outline is *hypothetical*. It shows how standard macro adjustment equations *could* generate (i) one or more cyclical degrees of freedom and (ii) a phase representation that naturally lives on a torus (or a product of tori). In that sense, we simply outline an assumption, a hypothesis on the connection and we do not claim any structural identification in this paper.

#### 1. IS–LM(+Phillips) linear core and oscillatory modes,Hicks1937

Let y:=Y−Y⋆y:=Y-Y^{\star} be the output gap, r:=i−i⋆r:=i-i^{\star} the (policy/market) rate gap, and π:=Π−Π⋆\pi:=\Pi-\Pi^{\star} the inflation gap. A minimalist continuous-time linear adjustment writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | y˙=−ρ​y−σ​r+ηt,r˙=ϕ​y−χ​r+ψ​π+νt,π˙=κ​y−ϑ​π+ξt,(ρ,σ,ϕ,χ,ψ,κ,ϑ)>0,\begin{aligned} \dot{y}&=-\rho\,y\;-\;\sigma\,r\;+\;\eta\_{t},\\ \dot{r}&=\ \phi\,y\;-\;\chi\,r\;+\;\psi\,\pi\;+\;\nu\_{t},\\ \dot{\pi}&=\ \kappa\,y\;-\;\vartheta\,\pi\;+\;\xi\_{t},\end{aligned}\quad(\rho,\sigma,\phi,\chi,\psi,\kappa,\vartheta)>0, |  | (40) |

with small shocks (ηt,νt,ξt)(\eta\_{t},\nu\_{t},\xi\_{t}). In matrix form 𝐬˙=A​𝐬+𝐮t\dot{\mathbf{s}}=A\,\mathbf{s}+\mathbf{u}\_{t} for 𝐬=(y,r,π)⊤\mathbf{s}=(y,r,\pi)^{\top} and

|  |  |  |
| --- | --- | --- |
|  | A=[−ρ−σ0ϕ−χψκ0−ϑ].A=\begin{bmatrix}-\rho&-\sigma&0\\ \ \phi&-\chi&\ \psi\\ \ \kappa&0&-\vartheta\end{bmatrix}. |  |

The (y,r)(y,r)-subsystem has complex eigenvalues (oscillatory adjustment,Benhabib1979; Barnett2008) iff

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ρ−χ)2< 4​σ​ϕ.(\rho-\chi)^{2}\;<\;4\,\sigma\,\phi. |  | (41) |

Coupling to π\pi via (ψ,κ)(\psi,\kappa) adds a further feedback loop. For parameter regions near a Hopf boundary, the linear core exhibits *one* dominant oscillatory mode; additional macro blocks (below) provide further cycles.

##### Note on “Hopf”.Kuznetsov2013

“Hopf” refers to the *Hopf bifurcation*: in a smooth system x˙=f​(x,α)\dot{x}=f(x,\alpha), an equilibrium undergoes a qualitative change when the Jacobian has a simple pair of purely imaginary eigenvalues ±i​ω0\pm i\omega\_{0} at α=α0\alpha=\alpha\_{0} (others stable) and the real part crosses zero transversally. Locally, dynamics on the 2D center manifold reduce to

|  |  |  |
| --- | --- | --- |
|  | z˙=(μ+i​ω0)​z−c​|z|2​z+⋯,z∈ℂ,μ=α−α0,\dot{z}=(\mu+i\omega\_{0})z-c|z|^{2}z+\cdots,\quad z\in\mathbb{C},\ \mu=\alpha-\alpha\_{0}, |  |

so for a *supercritical* Hopf (Rec>0\real c>0, μ>0\mu>0) a stable limit cycle appears with one phase θ∈S1\theta\in S^{1}. If a second weakly coupled Hopf mode coexists (e.g., another macro block), two phases (θ,ϕ)∈S1×S1(\theta,\phi)\in S^{1}\times S^{1} arise, i.e. a torus T2T^{2} (and, with several blocks, a product of tori).

#### 2. Hopf reduction and phase dynamics (one torus)

Near a (supercritical) Hopf set of ([40](https://arxiv.org/html/2511.05030v2#S5.E40 "In 1. IS–LM(+Phillips) linear core and oscillatory modes,Hicks1937 ‣ 5.1 IS–LM foundations for (multi-)torus dynamics: a mathematical sketch ‣ 5 Discussion and Future Research ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")), the macro state admits a two-dimensional center manifold with normal form

|  |  |  |  |
| --- | --- | --- | --- |
|  | z˙=(μ+i​ω)​z−c​|z|2​z+εt,z∈ℂ,μ,ω∈ℝ,Re(c)>0,\dot{z}\;=\;(\mu+i\,\omega)\,z\;-\;c\,|z|^{2}z\;+\;\varepsilon\_{t},\qquad z\in\mathbb{C},\ \ \mu,\omega\in\mathbb{R},\ \ \real(c)>0, |  | (42) |

whose stable limit cycle (for μ>0\mu>0) has amplitude |z|=μ/Re(c)|z|=\sqrt{\mu/\real(c)}. Writing z=ρ​ei​θz=\rho e^{i\theta},

|  |  |  |
| --- | --- | --- |
|  | ρ˙=μ​ρ−Re(c)⁡ρ3+…,θ˙=ω+ζ​(ρ)+…,\dot{\rho}\;=\;\mu\,\rho-\real(c)\,\rho^{3}+\ldots,\qquad\dot{\theta}\;=\;\omega+\zeta(\rho)+\ldots, |  |

so the long-run dynamics reduce to a *single* phase variable θ∈S1\theta\in S^{1} (one circle). If a second, weakly coupled Hopf mode is present (e.g., from an additional macro block), we obtain two phases (θ,ϕ)∈S1×S1(\theta,\phi)\in S^{1}\times S^{1}, i.e., a *torus* T2T^{2}.

#### 3. From one torus to several: a multi-block macro

Empirically, multiple macro-financial subsystems can oscillate: a core IS–LM block; a credit/liquidity (financial accelerator) block; an external (open-economy IS–LM–BP) block; a term-structure block, etc. A parsimonious representation treats each block s=1,…,Ss=1,\dots,S as a weakly nonlinear oscillator with complex state z(s)z^{(s)}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | z˙(s)=(μs+i​ωs)​z(s)−cs​|z(s)|2​z(s)+∑ℓ≠sΓs​ℓ​(z(ℓ),z(s))+εt(s).\dot{z}^{(s)}\;=\;\big(\mu\_{s}+i\,\omega\_{s}\big)z^{(s)}\;-\;c\_{s}|z^{(s)}|^{2}z^{(s)}\;+\;\sum\_{\ell\neq s}\Gamma\_{s\ell}\big(z^{(\ell)},z^{(s)}\big)\;+\;\varepsilon\_{t}^{(s)}. |  | (43) |

Writing z(s)=ρs​ei​θ(s)z^{(s)}=\rho\_{s}e^{i\theta^{(s)}} and projecting on the limit cycles (ρs≈ρs⋆\rho\_{s}\approx\rho\_{s}^{\star}), we obtain a *phase network,Ikeda2012*,

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ˙(s)=ωs+∑ℓ≠s[κθ​θ(s​ℓ)​sin⁡(θ(ℓ)−θ(s)−αθ​θ(s​ℓ))+κθ​ϕ(s​ℓ)​sin⁡(ϕ(ℓ)−θ(s)−αθ​ϕ(s​ℓ))]+σθ(s)​W˙t(s),\dot{\theta}^{(s)}\;=\;\omega\_{s}\;+\;\sum\_{\ell\neq s}\!\!\Big[\kappa\_{\theta\theta}^{(s\ell)}\sin\!\big(\theta^{(\ell)}-\theta^{(s)}-\alpha\_{\theta\theta}^{(s\ell)}\big)\;+\;\kappa\_{\theta\phi}^{(s\ell)}\sin\!\big(\phi^{(\ell)}-\theta^{(s)}-\alpha\_{\theta\phi}^{(s\ell)}\big)\Big]\;+\;\sigma^{(s)}\_{\theta}\,\dot{W}\_{t}^{(s)}, |  | (44) |

(and analogously for a second phase ϕ(s)\phi^{(s)} if block ss has two distinct cycles). Collecting the phases

|  |  |  |
| --- | --- | --- |
|  | Φt=(θt(1),ϕt(1),…,θt(S),ϕt(S))∈T2​S=S1×S1⏟block 1×⋯×S1×S1⏟block S,\Phi\_{t}\;=\;\big(\theta\_{t}^{(1)},\phi\_{t}^{(1)},\ \ldots,\ \theta\_{t}^{(S)},\phi\_{t}^{(S)}\big)\ \in\ T^{2S}\;=\;\underbrace{S^{1}\times S^{1}}\_{\text{block 1}}\times\cdots\times\underbrace{S^{1}\times S^{1}}\_{\text{block $S$}}, |  |

the latent macro state evolves on a *product of tori*. This is what we mean by “multiple torii”: several two-cycle subsystems, each contributing its own S1×S1S^{1}\times S^{1} factor.

##### Slowly varying cycle strengths (time-varying radii).

Policy stance or global liquidity can modulate the effective cycle amplitudes. A simple parameterization is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρs⋆​(t)=Rs​(ζt),0<Rs​(⋅)<∞,\rho\_{s}^{\star}(t)\;=\;R\_{s}\big(\zeta\_{t}\big),\qquad 0<R\_{s}(\cdot)<\infty, |  | (45) |

for a slowly moving driver ζt\zeta\_{t}; geometrically, this induces a *torus bundle* with time-varying “radii” (cycle strengths).

#### 4. From macro phases to the asset embedding

Let Xt∈ℝ3X\_{t}\in\mathbb{R}^{3} denote the 3D asset embedding (our eigenportfolio coordinates). A reduced-form map from macro phases to the conditional drift is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Δ​Xt+1∣ℱt]=G​(Φt),G​(Φ)=∑s=1S∑m,n∈ℤCm,n(s)​[cos⁡(m​θ(s)+n​ϕ(s))sin⁡(m​θ(s)+n​ϕ(s))cos⁡(m​θ(s)−n​ϕ(s))],\mathbb{E}[\Delta X\_{t+1}\mid\mathcal{F}\_{t}]\;=\;G\big(\Phi\_{t}\big),\quad G(\Phi)\;=\;\sum\_{s=1}^{S}\ \sum\_{m,n\in\mathbb{Z}}C^{(s)}\_{m,n}\,\begin{bmatrix}\cos(m\theta^{(s)}+n\phi^{(s)})\\ \sin(m\theta^{(s)}+n\phi^{(s)})\\ \cos(m\theta^{(s)}-n\phi^{(s)})\end{bmatrix}, |  | (46) |

with slowly varying loadings Cm,n(s)C^{(s)}\_{m,n}. Under mild smoothness and time-scale separation, the embedded path inherits the *topology* (loops) of the underlying T2​ST^{2S} and displays local curvature patterns (negative/near-zero/positive) as the phases traverse saddle/transition/compact bands of the induced geometry.

#### 5. What “multi–torus” implies for our diagnostics

* •

  Curvature. Mixtures of cycles produce *mixed* Gaussian curvature with a negative skew if trajectories frequent “saddle” corridors (amplification-dominant passages), interspersed with near-zero bands (slow transitions) and occasional positive patches (constraint-dominant).
* •

  Persistent homology. Windows with two *dominant* cycles exhibit two long H1H\_{1} features; when additional blocks become energetic, extra (weaker) H1H\_{1} loops may appear. The strength of the top two loops should co-move with cycle amplitudes ρs⋆​(t)\rho\_{s}^{\star}(t) in ([45](https://arxiv.org/html/2511.05030v2#S5.E45 "In Slowly varying cycle strengths (time-varying radii). ‣ 3. From one torus to several: a multi-block macro ‣ 5.1 IS–LM foundations for (multi-)torus dynamics: a mathematical sketch ‣ 5 Discussion and Future Research ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")).
* •

  Spectral content. The embedded coordinates should show peaks near the macro cycle frequencies {ωs}\{\omega\_{s}\} (possibly time-varying), with cross-modulation when couplings in ([44](https://arxiv.org/html/2511.05030v2#S5.E44 "In 3. From one torus to several: a multi-block macro ‣ 5.1 IS–LM foundations for (multi-)torus dynamics: a mathematical sketch ‣ 5 Discussion and Future Research ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) tighten.

##### Why this matters for our GIM.

Working in charts aligned with the local geometry (log map →\to tangent forecast →\to exp map) lets the forecaster track *where on the torus(es)* the system currently moves. The eigenvalue weighting concentrates on sleeves that presently carry the strongest cycle energy, while curvature gating tempers risk in amplification-heavy passages. Our empirical outperformance is *consistent with* this picture, without pinning down a single structural model.

A stylized IS–LM(+extensions) can sustain one or more weakly coupled limit cycles. Near Hopf regimes and with additional macro blocks, the latent state admits a phase representation on T2​ST^{2S} (a product of tori) with slowly varying radii. If such a structure is relevant, it offers a parsimonious rationale for the torus-like geometric and topological signatures we document, and for the gains from geometry-aware forecasting. Establishing causality requires a dedicated macro–finance state-space estimation and is left for future work.

##### Portfolio Management Context

However, in the context of trading/portfolio management applications, we model *assets*, not macro variables - yet some macro cycles may leave a geometric imprint usable for forecasting. A minimal, testable set of assumptions under which sharing information between the macro (phase) space and the asset PCA space is valid is:

* •

  Low–dimensional driver (A1). There exists a latent macro state ζt=(θt,ϕt)∈S1×S1\zeta\_{t}=(\theta\_{t},\phi\_{t})\in S^{1}\times S^{1} such that the *conditional* mean of the embedded increments is a smooth function of ζt\zeta\_{t}:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼​[Δ​Xt+1∣ℱt]=g​(ζt),g∈C1,‖∇g‖<∞.\mathbb{E}[\Delta X\_{t+1}\mid\mathcal{F}\_{t}]\;=\;g(\zeta\_{t}),\qquad g\in C^{1},\ \ \|\nabla g\|<\infty. |  |
* •

  Factor alignment (A2). Asset excess returns admit a conditional factor model

  |  |  |  |
  | --- | --- | --- |
  |  | rt+1=B​(ζt)​ft+1+ut+1,𝔼​[ut+1∣ℱt]=0,r\_{t+1}\;=\;B(\zeta\_{t})\,f\_{t+1}+u\_{t+1},\quad\mathbb{E}[u\_{t+1}\mid\mathcal{F}\_{t}]=0, |  |

  where the top PCA eigenportfolios span the space of priced factors ft+1f\_{t+1} up to rotation; thus the 3D PCA path XtX\_{t} captures the common macro–driven component.
* •

  Slow variation / time–scale separation (A3). Loadings B​(ζt)B(\zeta\_{t}) and the PCA basis/eigenvalues vary *slowly* at the forecast horizon:
  ‖B​(ζt+1)−B​(ζt)‖=o​(1),\|B(\zeta\_{t+1})-B(\zeta\_{t})\|=o(1),
  so expanding-window PCA and eigenvalue weights track the evolving subspace without introducing spurious curvature.
* •

  Weak feedback (A4). Macro phases are not instantaneously determined by asset prices (no simultaneity at tt); any feedback is *lagged* or small, so using ζt\zeta\_{t} (or its geometric proxies) for prediction avoids circularity.
* •

  No-arbitrage consistency (A5). Risk premia are functions of ζt\zeta\_{t} (via B​(ζt)B(\zeta\_{t}) and prices of risk), so that conditioning on ζt\zeta\_{t} (or its geometric signature such as local curvature KtK\_{t}) is economically meaningful and not eliminated by static arbitrage.
* •

  Measurement invariance (A6). The geometry inferred from XtX\_{t} is invariant to orthogonal rotations of the PCA coordinates; hence torus-/hyperbolic-like signatures reflect the *state’s* topology, not an arbitrary basis choice.

Under (A1)–(A6) the map ζt↦(𝔼​[Δ​Xt+1∣ℱt],Var⁡[Δ​Xt+1∣ℱt])\zeta\_{t}\mapsto(\mathbb{E}[\Delta X\_{t+1}\mid\mathcal{F}\_{t}],\operatorname{Var}[\Delta X\_{t+1}\mid\mathcal{F}\_{t}]) is well-defined and sufficiently smooth, legitimizing the use of geometry-informed forecasts and geometry-modulated allocation on asset returns. Practically, these assumptions can be probed via (i) rotation tests on PCA sleeves, (ii) stability tests for B​(⋅)B(\cdot) across subsamples, and (iii) event studies verifying that identified macro shocks shift the geometric proxies (KtK\_{t}, phase speeds) before changes in expected returns.

##### Machine Learners Contribution

: Further experiments incorporating machine-learning forecasts (RF and GP) as auxiliary predictors to the VAR confirmed that generic nonlinear learners add little incremental value once curvature and manifold structure are accounted for.
Both GP and RF models produced similar ranking of geometries—with the torus remaining the dominant topology—but their absolute gains were modest.
This outcome reinforces the interpretation that market predictability arises less from complex functional approximations and more from the geometric and topological constraints shaping the evolution of financial states.

### 5.2 Future research agenda (testable directions)

##### (A) Macro–GIM coupling in a state-space (hypothesis testing).

Embed a small macro block 𝐦t\mathbf{m}\_{t} (output gap, inflation, term structure, liquidity indicators) alongside geometric phases (θt,ϕt)(\theta\_{t},\phi\_{t}) in a joint state-space. Estimate via particle/MCMC filters on S1×S1S^{1}\times S^{1} with observation in ℝ3\mathbb{R}^{3}. Test whether shocks to 𝐦t\mathbf{m}\_{t} *shift* curvature regimes and phase speeds, and whether geometry improves macro nowcasts.

##### (B) Geometry-aware nowcasting.

Combine GIM with mixed-frequency nowcasting: update (θt,ϕt)(\theta\_{t},\phi\_{t}) and the tangent-space forecasts as high-frequency data arrive, and reweight sleeves by expanding-SVD eigenvalues and curvature gates. This evaluates whether real-time macro signals *enhance* geometry-aware timing.NoguerAlonso2021FinEAS

##### (C) Identification and causality.

Use event studies (policy announcements, macro releases) and geometry-aware Granger tests to assess if curvature/phase changes *precede* or *follow* macro innovations. This distinguishes descriptive fit from predictive content.

##### (D) Multi-torus/multi-sector structure.

Allow several coupled tori {(θt(s),ϕt(s))}s\{(\theta\_{t}^{(s)},\phi\_{t}^{(s)})\}\_{s} to represent sectoral/sovereign cycles; study whether cross-couplings explain the observed curvature skew better than a single-torus hypothesis.

##### (E) Model class extensions.

* •

  *Riemannian dynamics:* Specify VAR/GP directly on Tμ​MT\_{\mu}M with curvature-corrected propagation and compare to Euclidean projections.
* •

  *Time-varying shape parameters:* Let (Rt,rt)(R\_{t},r\_{t}) for T2T^{2} or (at,bt,ct)(a\_{t},b\_{t},c\_{t}) for the hyperboloid evolve stochastically; jointly estimate with forecasts.
* •

  *SPD-covariance coupling:* Model sleeve covariances on the SPD manifold (Log–Euclidean or affine-invariant) and fuse with torus phases to capture variance–phase interactions.

##### (F) Policy sensitivity and stress tests.

Simulate counterfactuals under alternative policy rules (LM slope, reaction coefficients) and quantify how curvature regimes and portfolio outcomes *might* change. This frames geometry as a compact policy-sensitivity diagnostic.

##### (G) Robustness and external validity.

Replicate across markets and horizons; vary expanding-window lengths; perform (i) geometry-aware forecast, (ii) eigenvalue weighting, (iii) curvature gating, to isolate contributions. Where possible, preregister hypotheses about curvature shifts around known macro events.

Summary. Our evidence is *consistent* with—but does not establish—a torus-like macro–financial geometry in which two interacting cycles produce the observed curvature mix. Treating this as a working hypothesis suggests concrete tests (state-space coupling, event identification, multi-torus structures) and practical extensions (nowcasting + GIM) that can clarify whether the geometry carries independent predictive content or simply organizes existing macro signals more effectively.

## 6 Appendices

## Appendix A Data Universe and Pre-processing

The dataset used in this study encompasses a broad spectrum of financial assets, covering the period from January 1, 2005, to August 3, 2025. The assets include:

* •

  Broad Market Indices: S&P 500 (SPY), NASDAQ-100 (QQQ), Dow Jones Industrial Average (DIA), Russell 2000 (IWM), MSCI Emerging Markets (EEM), and MSCI EAFE (EFA).
* •

  Sector ETFs: Technology Select Sector SPDR (XLK), Financial Select Sector SPDR (XLF), Health Care Select Sector SPDR (XLV), Energy Select Sector SPDR (XLE), Consumer Discretionary Select Sector SPDR (XLY), Consumer Staples Select Sector SPDR (XLP), Utilities Select Sector SPDR (XLU), Industrial Select Sector SPDR (XLI), and Materials Select Sector SPDR (XLB).
* •

  Bond ETFs: iShares 20+ Year Treasury Bond ETF (TLT), iShares 7-10 Year Treasury Bond ETF (IEF), iShares 1-3 Year Treasury Bond ETF (SHY), iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD), iShares iBoxx $ High Yield Corporate Bond ETF (HYG), iShares TIPS Bond ETF (TIP), and iShares MBS ETF (MBB).
* •

  Commodity ETFs: SPDR Gold Shares (GLD), iShares Silver Trust (SLV), Invesco DB Agriculture Fund (DBA), Teucrium Corn Fund (CORN), Invesco DB Base Metals Fund (DBB), Aberdeen Standard Physical Platinum Shares ETF (PPLT), and Aberdeen Standard Physical Palladium Shares ETF (PALL).
* •

  Oil ETFs: United States Oil Fund (USO), ProShares Ultra Bloomberg Crude Oil (UCO), Invesco DB Oil Fund (DBO), and SPDR S&P Oil & Gas Exploration & Production ETF (XOP).
* •

  Non-U.S. ETFs: iShares MSCI ACWI ex U.S. ETF (ACWX), Vanguard FTSE All-World ex-US ETF (VEU), iShares MSCI Europe ETF (IEUR), iShares MSCI Pacific ex Japan ETF (EPP), iShares Latin America 40 ETF (ILF), iShares MSCI Canada ETF (EWC), iShares MSCI United Kingdom ETF (EWU), iShares MSCI South Korea ETF (EWY), iShares MSCI Australia ETF (EWA), iShares MSCI Taiwan ETF (EWT), and Vanguard FTSE Emerging Markets ETF (VWO).
* •

  Dividend and Volatility ETFs: Vanguard Dividend Appreciation ETF (VIG), iShares Select Dividend ETF (DVY), SPDR S&P Dividend ETF (SDY), and ProShares VIX Short-Term Futures ETF (VIXY).
* •

  Alternative ETFs: iShares Clean Energy ETF (ICLN) and Global X Lithium & Battery Tech ETF (LIT).

This diverse dataset provides comprehensive coverage of global financial markets, enabling robust testing of the proposed methodologies across various asset classes and economic regimes.

## Appendix B Implementation details for SDEs and curvature terms

##### Ambient Euler Maruyama.

We discretize ([2](https://arxiv.org/html/2511.05030v2#S3.E2 "In 3.1 Ambient formulation and curvature drift ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) with step hh:

|  |  |  |
| --- | --- | --- |
|  | Xk+1=Xk+P​(Xk)​Δ​Wk−12​H​(Xk)​h,Δ​Wk∼𝒩​(0,h​I3).X\_{k+1}\;=\;X\_{k}\;+\;P(X\_{k})\,\Delta W\_{k}\;-\;\frac{1}{2}H(X\_{k})\,h,\quad\Delta W\_{k}\sim\mathcal{N}(0,hI\_{3}). |  |

For M=S2M=S^{2} we use P​(x)=I−x​x⊤‖x‖2P(x)=I-\frac{xx^{\top}}{\|x\|^{2}} and H​(x)=2‖x‖2​xH(x)=\frac{2}{\|x\|^{2}}x. For the torus we use the implicit form ϕ​(x)=(R−x12+x22)2+x32−r2\phi(x)=\big(R-\sqrt{x\_{1}^{2}+x\_{2}^{2}}\big)^{2}+x\_{3}^{2}-r^{2} with P​(x)=I−∇ϕ​∇ϕ⊤‖∇ϕ‖2P(x)=I-\frac{\nabla\phi\,\nabla\phi^{\top}}{\|\nabla\phi\|^{2}} and a consistent mean-curvature drift (implemented in closed form). Hyperbolic segments use the implicit quadratic form ϕ​(x)=a1​x12+a2​x22+a3​x32−1\phi(x)=a\_{1}x\_{1}^{2}+a\_{2}x\_{2}^{2}+a\_{3}x\_{3}^{2}-1 with signature (+,−,+)(+,-,+), projector from the gradient, and corresponding curvature drift.

##### Intrinsic charts.

For torus and hyperbolic we also implement the intrinsic SDEs ([5](https://arxiv.org/html/2511.05030v2#S3.E5 "In 2nd item ‣ Torus 𝑇²⁢(𝑅,𝑟) (major radius 𝑅, minor radius 𝑟). ‣ 3.2 Explicit SDEs by geometry ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries"))–([6](https://arxiv.org/html/2511.05030v2#S3.E6 "In 2nd item ‣ Torus 𝑇²⁢(𝑅,𝑟) (major radius 𝑅, minor radius 𝑟). ‣ 3.2 Explicit SDEs by geometry ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")) and ([7](https://arxiv.org/html/2511.05030v2#S3.E7 "In Hyperbolic 𝐻² (hyperboloid model). ‣ 3.2 Explicit SDEs by geometry ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries"))–([8](https://arxiv.org/html/2511.05030v2#S3.E8 "In Hyperbolic 𝐻² (hyperboloid model). ‣ 3.2 Explicit SDEs by geometry ‣ 3 Geometry-Constrained Stochastic Dynamics: Explicit Forms ‣ The Shape of Markets: Machine learning modeling and Prediction Using 2-Manifold Geometries")), then map to ℝ3\mathbb{R}^{3} via Ψ\Psi and Φ\Phi respectively at output time.

## Appendix C Scenario catalog

We use seven scenarios of length TT:

* •

  Scen. 1 (Pattern): [S2,H2,ℝ3][S^{2},H^{2},\mathbb{R}^{3}] blocks of length 500, repeated thrice, ending with S2S^{2}.
* •

  Scen. 2 (Random order): a randomized permutation of S2,H2,ℝ3S^{2},H^{2},\mathbb{R}^{3} blocks of length 500, ending with S2S^{2}.
* •

  Scen. 3 (Pure S2S^{2}): one S2S^{2} segment of length 5000.
* •

  Scen. 4 (Pure T2T^{2}): one torus segment of length 5000 (angle chart simulation, output in ℝ3\mathbb{R}^{3}).
* •

  Scen. 5 (Pure Euclid): one ℝ3\mathbb{R}^{3} Brownian segment of length 5000.
* •

  Scen. 6 (Pure H2H^{2}): one hyperbolic segment of length 5000 (absorbing threshold to prevent numeric explosion).
* •

  Scen. 7 (Comprehensive): repeated rotation of S2,H2,ℝ3,T2S^{2},H^{2},\mathbb{R}^{3},T^{2} blocks (e.g., 5 cycles ×\times 4 blocks ×\times 500 points).

## Appendix D Coordinate transforms,doCarmoCurves; doCarmoRiemannian

##### Spherical ↔\leftrightarrow Cartesian (radius RR).

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Cart ← Sph:x=R​sin⁡ϕ​cos⁡θ,y=R​sin⁡ϕ​sin⁡θ,z=R​cos⁡ϕ.\displaystyle\text{Cart $\leftarrow$ Sph:}\quad x=R\sin\phi\,\cos\theta,\;\;y=R\sin\phi\,\sin\theta,\;\;z=R\cos\phi. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Sph ← Cart:R=‖x‖,θ=arctan⁡2​(y,x),ϕ=arccos⁡(z/‖x‖).\displaystyle\text{Sph $\leftarrow$ Cart:}\quad R=\|x\|,\;\;\theta=\arctan 2(y,x),\;\;\phi=\arccos(z/\|x\|). |  |

##### Torus ↔\leftrightarrow Cartesian.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Cart ← Torus:x=(R+r​cos⁡φ)​cos⁡θ,y=(R+r​cos⁡φ)​sin⁡θ,z=r​sin⁡φ.\displaystyle\text{Cart $\leftarrow$ Torus:}\quad x=(R+r\cos\varphi)\cos\theta,\;\;y=(R+r\cos\varphi)\sin\theta,\;\;z=r\sin\varphi. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Torus ← Cart:θ=arctan⁡2​(y,x),φ=arctan⁡2​(z,x2+y2−R).\displaystyle\text{Torus $\leftarrow$ Cart:}\quad\theta=\arctan 2(y,x),\;\;\varphi=\arctan 2\!\big(z,\ \sqrt{x^{2}+y^{2}}-R\big). |  |

##### Hyperboloid (rotational) ↔\leftrightarrow Cartesian.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Cart ← Hyp:x=a​cosh⁡u​cos⁡v,y=a​cosh⁡u​sin⁡v,z=c​sinh⁡u.\displaystyle\text{Cart $\leftarrow$ Hyp:}\quad x=a\cosh u\cos v,\;\;y=a\cosh u\sin v,\;\;z=c\sinh u. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Hyp ← Cart:v=arctan⁡2​(y/a,x/a),u=arcsinh​(z/c).\displaystyle\text{Hyp $\leftarrow$ Cart:}\quad v=\arctan 2(y/a,x/a),\;\;u=\mathrm{arcsinh}(z/c). |  |

For regime transitions we convert once at the beginning of the new segment, simulate in the appropriate chart if needed, and always output in Cartesian space for continuity.