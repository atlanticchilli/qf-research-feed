---
authors:
- Nicolas Baradel
doc_id: arxiv:2511.20837v1
family_id: arxiv:2511.20837
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Constrained deep learning for pricing and hedging european options in incomplete
  markets
url_abs: http://arxiv.org/abs/2511.20837v1
url_html: https://arxiv.org/html/2511.20837v1
venue: arXiv q-fin
version: 1
year: 2025
---


Nicolas Baradel111Inria, CMAP, CNRS, École polytechnique, Institut Polytechnique de Paris, 91200 Palaiseau, nicolas.baradel@polytechnique.edu.

###### Abstract

In incomplete financial markets, pricing and hedging European options lack a unique no-arbitrage solution due to unhedgeable risks. This paper introduces a constrained deep learning approach to determine option prices and hedging strategies that minimize the Profit and Loss (P&L) distribution around zero. We employ a single neural network to represent the option price function, with its gradient serving as the hedging strategy, optimized via a loss function enforcing the self-financing portfolio condition.
A key challenge arises from the non-smooth nature of option payoffs (e.g., vanilla calls are non-differentiable at-the-money, while digital options are discontinuous), which conflicts with the inherent smoothness of standard neural networks. To address this, we compare unconstrained networks against constrained architectures that explicitly embed the terminal payoff condition, drawing inspiration from PDE-solving techniques.
Our framework assumes two tradable assets: the underlying and a liquid call option capturing volatility dynamics. Numerical experiments evaluate the method on simple options with varying non-smoothness, the exotic Equinox option, and scenarios with market jumps for robustness. Results demonstrate superior P&L distributions, highlighting the efficacy of constrained networks in handling realistic payoffs.
This work advances machine learning applications in quantitative finance by integrating boundary constraints, offering a practical tool for pricing and hedging in incomplete markets.

## 1 Introduction

In incomplete financial markets, no unique no-arbitrage price exists for derivative securities. This paper proposes a constrained deep-learning framework that simultaneously prices and hedges European options in such environments by determining an initial premium and a dynamic hedging strategy that minimize the dispersion of the terminal profit-and-loss (P&L) distribution.

We consider a general incomplete market driven by Brownian motion. The hedging portfolio is required to be self-financing, starts from the initial premium, and aims to replicate the option payoff at maturity as closely as possible. While neural-network approaches to pricing and hedging are not new, see e.g. [[8](https://arxiv.org/html/2511.20837v1#bib.bib8)], revisited in [[5](https://arxiv.org/html/2511.20837v1#bib.bib5)]. Recent contributions have explored reinforcement learning [[7](https://arxiv.org/html/2511.20837v1#bib.bib7)], transaction costs [[4](https://arxiv.org/html/2511.20837v1#bib.bib4)], jumps [[1](https://arxiv.org/html/2511.20837v1#bib.bib1)], and other market frictions [[6](https://arxiv.org/html/2511.20837v1#bib.bib6)].

Our approach departs from these works in two key respects. First, a *single* neural network outputs both the option price (as its value) and the hedging strategy (as its gradient with respect to the tradable assets), extending the classical complete-market representation in which the delta is the derivative of the price. Second, we explicitly address incomplete markets, whereas many recent deep-learning methods either assume completeness or compute only the price (e.g. BSDE-based solvers in jump-diffusion settings [[2](https://arxiv.org/html/2511.20837v1#bib.bib2)]).

A well-known practical difficulty when using neural networks for option pricing is enforcing the terminal payoff condition. Vanilla call payoffs are non-differentiable and digital payoffs are discontinuous; standard smooth activations struggle to represent them accurately at maturity without introducing spurious non-smoothness earlier. Even smooth payoffs pose challenges for boundary enforcement in PDE solvers [[3](https://arxiv.org/html/2511.20837v1#bib.bib3), [10](https://arxiv.org/html/2511.20837v1#bib.bib10)]. We therefore adopt and extend constrained architectures that embed the terminal condition by construction.

Numerical experiments are conducted in a market with two tradable assets (the underlying stock and a liquid vanilla call option written on it). We compare unconstrained networks against several constrained formulations on payoffs of increasing non-smoothness, including an exotic Equinox option. Performance is benchmarked against the classical Black–Scholes delta hedge by comparing terminal P&L distributions.

The paper is organized as follows. Section 2 presents the financial setting, the neural-network architecture, the gradient-based hedging strategy, and different strategies for embedding the terminal payoff. Section 3 contains numerical results: we first introduce a stochastic-volatility model with stochastic correlation (making the market incomplete), then compare loss functions and constraint methods on simple and exotic options, and finally assess robustness to jumps and misspecification of the model.

## 2 The framework

This section introduces the mathematical setting, the self-financing condition for the hedging portfolio, the neural network architecture used to simultaneously produce the option price and hedging strategy, and the techniques employed to enforce (possibly non-smooth) terminal payoff conditions.

### 2.1 General framework

Let Ω:=C​([0,T],ℝd∘)\Omega:=C([0,T],\mathbb{R}^{d\_{\circ}}) represent the space of continuous functions from [0,T][0,T] to ℝd∘\mathbb{R}^{d\_{\circ}}, where T>0T>0 and functions start at value 0 at time 0. We define the canonical process by W​(ω)=ωW(\omega)=\omega, and let ℙ\mathbb{P} denote the Wiener measure on the Borel sets of Ω\Omega. Consequently, W=(Wi)1≤i≤d∘W=(W^{i})\_{1\leq i\leq d\_{\circ}} consists of d∘d\_{\circ} independent Brownian motions. The filtration (ℱt)0≤t≤T(\mathcal{F}\_{t})\_{0\leq t\leq T} is the (augmented) canonical filtration generated by WW.

We consider d<d∘d<d\_{\circ} tradable risky assets whose price process Z=(Zi)1≤i≤dZ=(Z^{i})\_{1\leq i\leq d} is an ℝd\mathbb{R}^{d}-valued, ℱ\mathcal{F}-adapted semimartingale. The market also contains a risk-free asset with constant interest rate r∈ℝr\in\mathbb{R}.

Our goal is to hedge as well as possible a European claim pays g​(ZT)g(Z\_{T}) at maturity TT, where g:ℝd→ℝg:\mathbb{R}^{d}\to\mathbb{R} is a (possibly non-smooth) measurable payoff function.

###### Definition 2.1 (Self-financing portfolio).

A portfolio is specified by its initial value V0∈ℝV\_{0}\in\mathbb{R} and an ℝd\mathbb{R}^{d}-valued predictable process ΔZ=(ΔZ,i)1≤i≤d\Delta^{Z}=(\Delta^{Z,i})\_{1\leq i\leq d} representing the number of shares held in each risky asset. The portfolio value process (Vt)0≤t≤T(V\_{t})\_{0\leq t\leq T} is self-financing if, for all 0≤t≤s≤T0\leq t\leq s\leq T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vs=Vt+∫tsr​(Vu−⟨ΔuZ⋅Zu⟩)​𝑑u+∫ts⟨ΔuZ⋅d​Zu⟩,V\_{s}=V\_{t}+\int\_{t}^{s}r\left(V\_{u}-\langle\Delta\_{u}^{Z}\cdot Z\_{u}\rangle\right)du+\int\_{t}^{s}\langle\Delta\_{u}^{Z}\cdot dZ\_{u}\rangle, |  | (2.1) |

In discrete rebalancing (constant holdings on [t,s][t,s]), this simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vs=er​(s−t)​(Vt−⟨ΔtZ⋅Zt⟩)+⟨ΔtZ⋅Zs⟩.V\_{s}=e^{r(s-t)}\left(V\_{t}-\langle\Delta\_{t}^{Z}\cdot Z\_{t}\rangle\right)+\langle\Delta\_{t}^{Z}\cdot Z\_{s}\rangle. |  | (2.2) |

In a complete market with no frictions, there exists a unique no-arbitrage price process p​(t,Zt)p(t,Z\_{t}) and a hedging strategy ΔtZ=∇zp​(t,Zt)\Delta^{Z}\_{t}=\nabla\_{z}p(t,Z\_{t}) such that the self-financing portfolio perfectly replicates the payoff:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(t,Zt)+∫tTr​(p​(u,Zu)−⟨∇zp​(u,Zu)⋅Zu⟩)​𝑑u+∫tT⟨∇zp​(u,Zu)⋅d​Zu⟩=g​(ZT).p(t,Z\_{t})+\int\_{t}^{T}r\left(p(u,Z\_{u})-\langle\nabla^{z}p(u,Z\_{u})\cdot Z\_{u}\rangle\right)du+\int\_{t}^{T}\langle\nabla^{z}p(u,Z\_{u})\cdot dZ\_{u}\rangle=g(Z\_{T}). |  | (2.3) |

In an incomplete market, no such perfect replication is possible in general. The price is not unique and perfect hedging cannot be achieved. Our goal is therefore to approximate a pricing function p​(t,z)p(t,z) whose spatial gradient ∇zp​(t,z)\nabla\_{z}p(t,z) serves as a hedging strategy, chosen so that the self-financing portfolio yields a terminal value as close as possible to g​(ZT)g(Z\_{T}) in a suitable sense. The next subsections introduce a deep neural network to achieve this objective while properly enforcing the (possibly non-smooth) terminal condition p​(T,z)=g​(z)p(T,z)=g(z).

### 2.2 Neural network

We represent the candidate pricing function using a fully connected (feedforward) deep neural network. We define the input dimension as di​n≥1d\_{in}\geq 1, representing the number of variables in the input x∈ℝdi​nx\in\mathbb{R}^{d\_{in}}. For simplicity, we set the output dimension to 1, meaning the network produces a single output value. The network consists of L≥2L\geq 2 layers, with the number of neurons in each layer denoted by (Dℓ)1≤ℓ≤L(D\_{\ell})\_{1\leq\ell\leq L}. Specifically:

* •

  The first layer (input layer) has D1=di​nD\_{1}=d\_{in} neurons.
* •

  The last layer (output layer) has DL=1D\_{L}=1 neuron.
* •

  The L−2L-2 layers in between are hidden layers, each with Dℓ=DD\_{\ell}=D neurons for simplicity, where 2≤ℓ≤L−12\leq\ell\leq L-1.

A feedforward neural network NN is a function that maps an input x∈ℝdi​nx\in\mathbb{R}^{d\_{in}} to an output in ℝ\mathbb{R}. It is defined as a composition of transformations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x↦AL∘ϕ∘AL−1∘…∘ϕ∘A1​(x).x\mapsto A\_{L}\circ\phi\circ A\_{L-1}\circ\ldots\circ\phi\circ A\_{1}(x). |  | (2.4) |

where:

* •

  AℓA\_{\ell} for 1≤ℓ≤L1\leq\ell\leq L are affine transformations, defined as Aℓ​(x)=𝒲ℓ​x+βℓA\_{\ell}(x)=\mathcal{W}\_{\ell}x+\beta\_{\ell}. Here, 𝒲ℓ\mathcal{W}\_{\ell} is a weight matrix, and βℓ\beta\_{\ell} is a bias vector.
* •

  The dimensions of these transformations are: A1A\_{1} maps from ℝdi​n\mathbb{R}^{d\_{in}} to ℝD\mathbb{R}^{D};
    
  A2,…,AL−1A\_{2},\ldots,A\_{L-1} map from ℝD\mathbb{R}^{D} to ℝD\mathbb{R}^{D}; and ALA\_{L} maps from ℝD\mathbb{R}^{D} to ℝ\mathbb{R}.
* •

  ϕ:ℝ↦I⊂ℝ\phi:\mathbb{R}\mapsto I\subset\mathbb{R} is a nonlinear activation function (where II is either ℝ\mathbb{R} or a subinterval), applied element-wise to the output of each affine transformation. For example, for a vector (x1,…,xD)(x\_{1},\ldots,x\_{D}) we have ϕ​(x1,…,xD)=(ϕ​(x1),…,ϕ​(xD))\phi(x\_{1},\ldots,x\_{D})=(\phi(x\_{1}),\ldots,\phi(x\_{D})).

The parameters of the neural network are the weight matrices (Wℓ)1≤ℓ≤L(W\_{\ell})\_{1\leq\ell\leq L} and bias vectors (βℓ)1≤ℓ≤L(\beta\_{\ell})\_{1\leq\ell\leq L} collectively denoted as θ\theta. The total number of parameters, mL,Dm\_{{}\_{L,D}}, is calculated as

|  |  |  |
| --- | --- | --- |
|  | mL,D=∑ℓ=1LDℓ​(1+Dℓ)=(1+di​n)​D+(L−2)​D​(1+D)+(1+D)m\_{{}\_{L,D}}=\sum\_{\ell=1}^{L}D\_{\ell}(1+D\_{\ell})=(1+d\_{in})D+(L-2)D(1+D)+(1+D) |  |

accounting for the weights and biases across all layers, thus θ∈ℝmL,D\theta\in\mathbb{R}^{m\_{{}\_{L,D}}}. We denote the neural network of ([2.4](https://arxiv.org/html/2511.20837v1#S2.E4 "In 2.2 Neural network ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) with parameter θ\theta as NθN\_{\theta}, and the set of all such networks with LL layers and DD neurons per hidden layer as (Nθ)θ∈ℝmL,D(N\_{\theta})\_{\theta\in\mathbb{R}^{m\_{{}\_{L,D}}}}.

We also define the set of all neural networks with LL layers and varying hidden layer sizes:

|  |  |  |
| --- | --- | --- |
|  | 𝒩L:=⋃D≥0(Nθ)θ∈ℝmL,D.\mathcal{N}\_{L}:=\bigcup\_{D\geq 0}(N\_{\theta})\_{\theta\in\mathbb{R}^{m\_{{}\_{L,D}}}}. |  |

##### Universal approximation theorem ([[12](https://arxiv.org/html/2511.20837v1#bib.bib12), Theorem 3.1]).

Let ϕ\phi be a continuous activation function. If ϕ\phi is non-polynomial, then for any L≥3L\geq 3, on any compact set K⊂ℝdi​nK\subset\mathbb{R}^{d\_{in}}, the set 𝒩L\mathcal{N}\_{L} is dense in C​(K)C(K), the set of continuous functions defined on KK equipped the uniform norm.

The smoothness of NθN\_{\theta} is inherited from ϕ\phi: if ϕ∈C∞​(ℝ)\phi\in C^{\infty}(\mathbb{R}), then Nθ∈C∞​(ℝdin)N\_{\theta}\in C^{\infty}(\mathbb{R}^{d\_{\text{in}}}). Standard smooth activations (tanh, sigmoid, softplus, etc.) therefore yield infinitely differentiable pricing functions: desirable away from maturity but problematic at t=Tt=T, where many option payoffs are only continuous (vanilla call/put) or even discontinuous (digital, barrier, and many exotic options).

Using non-smooth activations such as ReLU resolves the terminal issue to some extent, but introduces non-differentiability everywhere, including far before maturity, where the true price function is typically smooth.

These conflicting requirements (smoothness before maturity and possible non-smoothness exactly at maturity) motivate the constrained architectures introduced in the next subsection.

### 2.3 Deep learning

We consider a European claim with (possibly parameterised) payoff g​(ZT,P)g(Z\_{T},P), where P∈ℝk1P\in\mathbb{R}^{k\_{1}} collects contractual parameters (strike, barrier, etc.). To increase expressive power and allow the network to reference liquid hedging instruments with their own parameters, we introduce an auxiliary input vector K∈ℝk2K\in\mathbb{R}^{k\_{2}}.

The candidate price at time tt is represented by a neural network:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (t,z,K,P)↦Nθ​(T−t,z,K,P),(t,z,K,P)\mapsto N\_{\theta}(T-t,z,K,P), |  | (2.5) |

where T−tT-t is time-to-maturity, z∈ℝdz\in\mathbb{R}^{d} are the current levels of the tradable risky assets, and θ\theta denotes the trainable parameters.

As in the complete-market case, the hedging strategy in the risky assets is obtained directly from the network via automatic differentiation:

* •

  NθN\_{\theta} represents the option price,
* •

  ∇zNθ\nabla^{z}N\_{\theta} provides the hedging strategy.

In a complete, frictionless market, there exists θ∗\theta^{\*} such that the self-financing portfolio initialised at V0=Nθ∗​(T,Z0,K,P)V\_{0}=N\_{\theta^{\*}}(T,Z\_{0},K,P) and rebalanced according to ([2.3](https://arxiv.org/html/2511.20837v1#S2.E3 "In 2.1 General framework ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) perfectly replicates the payoff:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nθ∗​(0,ZT,K,P)=g​(ZT,P)ℙ​-a.s.N\_{\theta^{\*}}(0,Z\_{T},K,P)=g(Z\_{T},P)\quad\mathbb{P}\text{-a.s.} |  | (2.6) |

In an incomplete market with discrete hedging, NθN\_{\theta} satisfies the following approximation for Δ​t>0\Delta t>0:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Nθ​(T−(t+Δ​t),Zt+Δ​t,K,P)\displaystyle N\_{\theta}(T-(t+\Delta t),Z\_{t+\Delta t},K,P) | ≈er​Δ​t​(Nθ​(T−t,Zt,K,P)−⟨ΔtZ⋅Zt⟩)\displaystyle\approx e^{r\Delta t}\left(N\_{\theta}(T-t,Z\_{t},K,P)-\langle\Delta\_{t}^{Z}\cdot Z\_{t}\rangle\right) |  | (2.7) |
|  |  | +⟨ΔtZ⋅Zt+Δ​t⟩,\displaystyle\quad+\langle\Delta\_{t}^{Z}\cdot Z\_{t+\Delta t}\rangle, |  |
|  | Nθ​(0,ZT,K,P)\displaystyle N\_{\theta}(0,Z\_{T},K,P) | ≈g​(ZT,P).\displaystyle\approx g(Z\_{T},P). |  |

We therefore train the network by minimizing the expected deviation from the discrete-time self-financing condition. In ([2.7](https://arxiv.org/html/2511.20837v1#S2.E7 "In 2.3 Deep learning ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) forces the network to discover a price NθN\_{\theta} and corresponding hedge ∇zNθ\nabla^{z}N\_{\theta}, enabling the neural network to simultaneously learn the option price and hedging strategy by leveraging their interdependence.

### 2.4 Training objective and loss functions

We generate nn independent Monte Carlo paths of the tradable assets ZZ on a time grid 0=t0<t1<⋯<tm=T0=t\_{0}<t\_{1}<\cdots<t\_{m}=T, together with fixed or randomly drawn contract parameters PiP^{i} and auxiliary hedging-instrument parameters KiK^{i}. This yields the simulated dataset:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (tj,Ztji,Ki,Pi)0≤j≤m1≤i≤n.\left(t\_{j},Z\_{t\_{j}}^{i},K^{i},P^{i}\right)\_{0\leq j\leq m}^{1\leq i\leq n}. |  | (2.8) |

The network is trained by minimizing a composite loss that simultaneously enforces the discrete-time self-financing condition along each path and the terminal payoff condition. The latter loss is:

|  |  |  |
| --- | --- | --- |
|  | ℓT​(θ)=∑i=1n(Nθ​(0,ZTi,Ki,Pi)−g​(ZTi,Pi))2.\ell\_{T}(\theta)=\sum\_{i=1}^{n}\left(N\_{\theta}(0,Z\_{T}^{i},K^{i},P^{i})-g(Z\_{T}^{i},P^{i})\right)^{2}. |  |

To measure hedging performance, we introduce the following two loss functions.

###### Definition 2.2 (Self-financing approach).

Based on ([2.7](https://arxiv.org/html/2511.20837v1#S2.E7 "In 2.3 Deep learning ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")), we define the associated loss over nn paths:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓpathS​F​(θ)\displaystyle\ell\_{\texttt{path}}^{SF}(\theta) | :=∑i=1n∑j=0m−1((Nθ(T−tj,Ztji,Ki,Pi)−⟨ΔtjZ⋅Ztji⟩)er​(tj+1−tj)\displaystyle=\sum\_{i=1}^{n}\sum\_{j=0}^{m-1}\left(\left(N\_{\theta}(T-t\_{j},Z\_{t\_{j}}^{i},K^{i},P^{i})-\langle\Delta\_{t\_{j}}^{Z}\cdot Z\_{t\_{j}}^{i}\rangle\right)e^{r(t\_{j+1}-t\_{j})}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +⟨ΔtjZ⋅Ztj+1i⟩−Nθ(T−tj+1,Ztj+1i,Ki,Pi))2.\displaystyle\qquad\left.+\langle\Delta\_{t\_{j}}^{Z}\cdot Z\_{t\_{j+1}}^{i}\rangle-N\_{\theta}(T-t\_{j+1},Z\_{t\_{j+1}}^{i},K^{i},P^{i})\right)^{2}. |  |

where ΔtjZ:=∇zNθ​(T−tj,Ztji,Ki,Pi)\Delta\_{t\_{j}}^{Z}:=\nabla^{z}N\_{\theta}(T-t\_{j},Z\_{t\_{j}}^{i},K^{i},P^{i}).

###### Definition 2.3 (Profit and Loss approach).

Based on ([2.3](https://arxiv.org/html/2511.20837v1#S2.E3 "In 2.1 General framework ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")), we define the associated loss over nn paths:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓpathP​L​(θ)\displaystyle\ell\_{\texttt{path}}^{PL}(\theta) | :=∑i=1n(∑j=0m−1Nθ(T,Z0i,Ki,Pi)er​T−⟨ΔtjZ⋅Ztji⟩er​(T−tj)\displaystyle=\sum\_{i=1}^{n}\left(\sum\_{j=0}^{m-1}N\_{\theta}(T,Z\_{0}^{i},K^{i},P^{i})e^{rT}-\langle\Delta\_{t\_{j}}^{Z}\cdot Z\_{t\_{j}}^{i}\rangle e^{r(T-t\_{j})}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +⟨ΔtjZ⋅Ztj+1i⟩er​(T−tj+1)−g(ZTi,Pi))2.\displaystyle\qquad\left.+\langle\Delta\_{t\_{j}}^{Z}\cdot Z\_{t\_{j+1}}^{i}\rangle e^{r(T-t\_{j+1})}-g(Z\_{T}^{i},P^{i})\right)^{2}. |  |

where ΔtjZ:=∇zNθ​(T−tj,Ztji,Ki,Pi)\Delta\_{t\_{j}}^{Z}:=\nabla^{z}N\_{\theta}(T-t\_{j},Z\_{t\_{j}}^{i},K^{i},P^{i}).

The full training objective is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(θ):=ℓpathD​(θ)+λT​ℓT​(θ),\ell(\theta):=\ell\_{\texttt{path}}^{D}(\theta)+\lambda\_{T}\ell\_{T}(\theta), |  | (2.9) |

where λT>0\lambda\_{T}>0 is a hyperparameter controlling the strength of terminal payoff enforcement and D∈{S​F,P​L}D\in\{SF,PL\} according to the context.

Parameters θ\theta are estimated by stochastic gradient descent on mini-batches of paths and time steps. At iteration kk, a random subset Λ​(k)⊂{1,…,n}×{0,…,m−1}\Lambda(k)\subset\{1,\dots,n\}\times\{0,\dots,m-1\} of size C​a​r​d​(Λ​(k))≪n×mCard(\Lambda(k))\ll n\times m is sampled uniformly, and gradients are computed via automatic differentiation and backpropagation through time.

### 2.5 Constrained architectures for non-smooth payoffs

The function gg for the terminal condition is not always smooth, i.e. not always differentiable or even not continuous. For the simple vanilla call option, the payoff is continuous but not differentiable in the strike price. For the digital option, it is not even continuous. In general, the price is smooth before the maturity but not at the maturity.

Standard feedforward networks with smooth activations produce infinitely differentiable functions everywhere in their domain. This poses a fundamental difficulty when pricing derivatives whose payoff is not differentiable or even discontinuous. The true price is typically smooth on time-to-maturity T−t∈(0,T]T-t\in(0,T] but inherits the payoff’s irregularity at T−t=0T-t=0.

Using non-smooth activations such as ReLU removes global differentiability and therefore destroys the desirable pre-maturity smoothness that diffusion-driven prices exhibit.

For a payoff gg, we fix a reference function

|  |  |  |
| --- | --- | --- |
|  | f​(t,z,P),(t,z,P)∈[0,T]×ℝd×ℝk1,f(t,z,P),\quad(t,z,P)\in[0,T]\times\mathbb{R}^{d}\times\mathbb{R}^{k\_{1}}, |  |

that is continuously differentiable on (0,T]×ℝd×ℝk1(0,T]\times\mathbb{R}^{d}\times\mathbb{R}^{k\_{1}} the terminal condition:

|  |  |  |
| --- | --- | --- |
|  | f​(0,z,P)=g​(z,P),(z,P)∈ℝd×ℝk1.f(0,z,P)=g(z,P),\quad(z,P)\in\mathbb{R}^{d}\times\mathbb{R}^{k\_{1}}. |  |

Typical choices for ff are closed-form prices from tractable complete-market proxies as Black-Scholes or more sophisticated models. The candidate price is then represented as the convex combination

|  |  |  |  |
| --- | --- | --- | --- |
|  | N¯θ​(T−s,z,K,P):=w​(s,T)​f​(T−s,z,P)+w′​(s,T)​Nθ​(T−s,z,K,P),\overline{N}\_{\theta}(T-s,z,K,P):=w(s,T)f(T-s,z,P)+w^{\prime}(s,T)N\_{\theta}(T-s,z,K,P), |  | (2.10) |

where ww and w′w^{\prime} user-chosen smooth weighting functions. The hedging strategy is obtained by automatic differentiation of N¯θ\overline{N}\_{\theta}:

|  |  |  |
| --- | --- | --- |
|  | ΔtZ=∇zN¯θ​(T−t,z,K,P).\Delta^{Z}\_{t}=\nabla\_{z}\overline{N}\_{\theta}(T-t,z,K,P). |  |

We investigate the four architectures summarized below:

###### Definition 2.4.

We introduce four specific cases of ([2.10](https://arxiv.org/html/2511.20837v1#S2.E10 "In 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")).

* •

  Unconstrained: w:=0w:=0 and w′:=1w^{\prime}:=1 corresponds to the plain neural network; no terminal condition enforced by construction.
* •

  Zero-target: w​(s,T):=sTw(s,T):=\frac{s}{T} and w′:=1w^{\prime}:=1 corresponds to the case where the network NθN\_{\theta} is only required to output zero at T−t=0T-t=0, considerably easing the fitting of non-smooth payoffs while leaving pre-maturity behavior nearly unconstrained.
* •

  Control-variate: w:=1w:=1 and w′:=1w^{\prime}:=1 corresponds to the classical control-variate Monte Carlo: ff persistently contributes and NθN\_{\theta} learns the residual correction.
* •

  Constrained: w​(s,T):=sTw(s,T):=\frac{s}{T} and w′:=1−ww^{\prime}:=1-w corresponds to the case where the terminal condition N¯θ​(0,z,K,P)=g​(z,P)\overline{N}\_{\theta}(0,z,K,P)=g(z,P) is satisfied exactly for any parameters θ\theta, eliminating terminal payoff error entirely.

We analyze all cases outlined in Definition [2.4](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme4 "Definition 2.4. ‣ 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"). The Unconstrained approach imposes no constraints, representing a standard neural network. The Zero Target method mitigates the non-smoothness of the terminal condition without significantly affecting the solution away from maturity. The Control Variate approach is similar to Zero Target but assigns a constant weight of 1 to the function ff, which serves as a control-variate. Finally, the Constrained approach enforces a strict condition at maturity, ensuring the payoff is always satisfied for any neural network.

## 3 Numerical results

We now assess the practical performance of the proposed framework in an incomplete market featuring stochastic volatility and stochastic correlation between the underlying and its volatility process. The market is driven by d∘=3d\_{\circ}=3 independent Brownian motions but only d=2d=2 assets are tradable: the underlying stock and one liquid vanilla option used as a hedging instrument, making perfect replication impossible, even in continuous-time.

We first demonstrate that the P&L loss (Definition [2.3](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme3 "Definition 2.3 (Profit and Loss approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) systematically dominates the self-financing loss (Definition [2.2](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme2 "Definition 2.2 (Self-financing approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) in terms of out-of-sample P&L distribution sharpness. We then systematically compare the four architectures of Definition [2.4](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme4 "Definition 2.4. ‣ 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (Unconstrained, Zero-target, Control-variate, and Constrained) on a range of simple payoffs of different irregularity, and an exotic one: the Equinox option.

### 3.1 The market model

We define a market model through the following triplet of stochastic processes.

###### Definition 3.1.

Let μ∈ℝ,a>0,σ∘>0,ξ>0,γ∈[0.5,1],b>0,p∘∈ℝ,χ>0\mu\in\mathbb{R},a>0,\sigma\_{\circ}>0,\xi>0,\gamma\in[0.5,1],b>0,p\_{\circ}\in\mathbb{R},\chi>0. For initial conditions (x,σ,p)∈(ℝ+)2×ℝ(x,\sigma,p)\in(\mathbb{R}\_{+})^{2}\times\mathbb{R} at time t∈[0,T]t\in[0,T], and for s∈[t,T]s\in[t,T], the processes are given by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xst,x\displaystyle X\_{s}^{t,x} | =x+∫tsμ​Xut,x​𝑑u+∫tsΣut,σ​Xut,x​𝑑Wu1,\displaystyle=x+\int\_{t}^{s}\mu X\_{u}^{t,x}du+\int\_{t}^{s}\Sigma\_{u}^{t,\sigma}X\_{u}^{t,x}dW\_{u}^{1}, |  | (3.1) |
|  | Σst,σ\displaystyle\Sigma\_{s}^{t,\sigma} | =σ+∫ts−a​(Σut,σ−σ∘)​d​u+∫tsξ​(Σut,σ)γ​d​(ρut,p​Wu1+1−(ρut,p)2​Wu2),\displaystyle=\sigma+\int\_{t}^{s}-a(\Sigma\_{u}^{t,\sigma}-\sigma\_{\circ})du+\int\_{t}^{s}\xi(\Sigma\_{u}^{t,\sigma})^{\gamma}d(\rho\_{u}^{t,p}W\_{u}^{1}+\sqrt{1-(\rho\_{u}^{t,p})^{2}}W\_{u}^{2}), |  |
|  | Pst,p\displaystyle P\_{s}^{t,p} | =p+∫ts−b​(Put,p−p∘)​d​u+∫tsχ​𝑑Wu3,\displaystyle=p+\int\_{t}^{s}-b(P\_{u}^{t,p}-p\_{\circ})du+\int\_{t}^{s}\chi dW\_{u}^{3}, |  |

where the correlation process is defined as ρt,p:=tanh⁡(Pt,p)\rho^{t,p}:=\tanh(P^{t,p}).

In this model, Xt,xX^{t,x} represents the underlying price with stochastic volatility Σt,σ\Sigma^{t,\sigma}, which reverts to a long-term mean σ∘\sigma\_{\circ} at rate aa. The volatility Σt,σ\Sigma^{t,\sigma} is correlated with Xt,xX^{t,x} via a stochastic correlation ρt,p\rho^{t,p}, driven by the process Pt,pP^{t,p}, which itself exhibits mean reversion to p∘p\_{\circ}. The term ρut,p​Wu1+1−(ρut,p)2​Wu2\rho^{t,p}\_{u}W\_{u}^{1}+\sqrt{1-(\rho^{t,p}\_{u})^{2}}W\_{u}^{2} ensures a unit-variance Brownian motion with correlation ρt,p\rho^{t,p} to W1W^{1}.

###### Remark 3.2.

The process (Xt,x,Σt,σ,Pt,p)(X^{t,x},\Sigma^{t,\sigma},P^{t,p}) in Definition [3.1](https://arxiv.org/html/2511.20837v1#S3.Thmtheoreme1 "Definition 3.1. ‣ 3.1 The market model ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") admits a unique strong solution under the specified conditions.

For simplicity, we henceforth denote (X,Σ,P)(X,\Sigma,P) as (Xt,x,Σt,σ,Pt,p)(X^{t,x},\Sigma^{t,\sigma},P^{t,p}).

#### 3.1.1 The tradable assets

Of the processes introduced in Definition [3.1](https://arxiv.org/html/2511.20837v1#S3.Thmtheoreme1 "Definition 3.1. ‣ 3.1 The market model ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"), not all are tradable assets. We now define those that are.

###### Definition 3.3 (Tradable assets).

The market includes two tradable assets:

* •

  The underlying XX.
* •

  A European call option C​(K)C(K) with strike K>0K>0.

The price of the call option C​(K)C(K) at time s∈[t,T]s\in[t,T] is modeled as the Black-Scholes price with instantaneous volatility Σs\Sigma\_{s}:

|  |  |  |
| --- | --- | --- |
|  | Cs​(K):=B​S​(T−s,Xs,Σs,r,K),C\_{s}(K):=BS(T-s,X\_{s},\Sigma\_{s},r,K), |  |

where B​S​(u,x,σ,r,K)BS(u,x,\sigma,r,K) denotes the Black-Scholes price of a European call option with time to maturity u∈[0,T]u\in[0,T], underlying price x>0x>0, volatility σ>0\sigma>0, interest rate r∈ℝr\in\mathbb{R}, and strike K>0K>0.

This framework establishes an incomplete market, as there are two tradable assets but three independent sources of randomness (the Brownian motions W1,W2,W3W^{1},W^{2},W^{3}). Consequently, perfect hedging of a derivative is unattainable, though our goal is to minimize the hedging error.

#### 3.1.2 The neural network

Recall that we seek to determine the price and hedging strategy for a European option with payoff g​(XT,P)g(X\_{T},P) where P∈ℝk1P\in\mathbb{R}^{k\_{1}} for k1≥1k\_{1}\geq 1 represents the option’s parameters (e.g., strike price or barrier level). The neural network of ([2.5](https://arxiv.org/html/2511.20837v1#S2.E5 "In 2.3 Deep learning ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) is in our context:

|  |  |  |
| --- | --- | --- |
|  | (t,x,c,K,P)↦Nθ​(T−t,x,c,K,P),(t,x,c,K,P)\mapsto N\_{\theta}(T-t,x,c,K,P), |  |

where θ\theta denotes the trainable parameters, T−tT-t is the time to maturity, xx is the price of the underlying asset XtX\_{t}, cc is the price of the tradable call option CtC\_{t}, and K>0K>0 is the strike price of the tradable call option C​(K)C(K).

Finally,

* •

  NθN\_{\theta} represents the option price,
* •

  ∂xNθ\partial\_{x}N\_{\theta} and ∂cNθ\partial\_{c}N\_{\theta} provide the hedging strategies for the underlying asset and the tradable call option, respectively.

#### 3.1.3 Evaluation criterion

To assess the performance of the trained neural network in pricing and hedging, we evaluate its out-of-sample hedging error on paths simulated from the true data-generating process ([3.1](https://arxiv.org/html/2511.20837v1#S3.E1 "In Definition 3.1. ‣ 3.1 The market model ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")).

Consider an option with time to maturity TT, initial underlying price X0=xX\_{0}=x, initial call price C0=cC\_{0}=c, strike KK, and additional option parameter PP. The neural network approximates the price function as Nθ​(T,x,c,K,P)N\_{\theta}(T,x,c,K,P).

Given a discretized time grid 0=t0<t1<⋯<tm=T0=t\_{0}<t\_{1}<\cdots<t\_{m}=T, the network defines the hedging strategy at each rebalancing date tjt\_{j} as the gradients of the approximated value function:

|  |  |  |
| --- | --- | --- |
|  | Δtjx:=∂xNθ​(T−tj,Xtj,Ctj,K,P),Δtjc:=∂cNθ​(T−tj,Xtj,Ctj,K,P).\Delta\_{t\_{j}}^{x}:=\partial\_{x}N\_{\theta}(T-t\_{j},X\_{t\_{j}},C\_{t\_{j}},K,P),\quad\Delta\_{t\_{j}}^{c}:=\partial\_{c}N\_{\theta}(T-t\_{j},X\_{t\_{j}},C\_{t\_{j}},K,P). |  |

At maturity TT, the option payoff g​(XT,P)g(X\_{T},P) is delivered.

The discounted Profit-and-Loss of the hedged position for a single simulated path ii is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P&Li:=Nθ​(T,x,c,K,P)\displaystyle P\&L\_{i}=N\_{\theta}(T,x,c,K,P) | +∑j=0m−1(Δtjx​(Xtj+1−Xtj)+Δtjc​(Ctj+1−Ctj))​e−r​tj+1\displaystyle+\sum\_{j=0}^{m-1}\left(\Delta\_{t\_{j}}^{x}(X\_{t\_{j+1}}-X\_{t\_{j}})+\Delta\_{t\_{j}}^{c}(C\_{t\_{j+1}}-C\_{t\_{j}})\right)e^{-rt\_{j+1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −g​(XT,P)​e−r​T.\displaystyle-g(X\_{T},P)e^{-rT}. |  |

Alternatively, the P&L could be computed at maturity by multiplying by er​Te^{rT}.

For nn independent Monte Carlo trajectories (Xtji,Ctji)0≤j≤m,1≤i≤n(X\_{t\_{j}}^{i},C\_{t\_{j}}^{i})\_{0\leq j\leq m,1\leq i\leq n} from the model in ([3.1](https://arxiv.org/html/2511.20837v1#S3.E1 "In Definition 3.1. ‣ 3.1 The market model ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")), we obtain (P&Li)1≤i≤n(P\&L\_{i})\_{1\leq i\leq n}. The empirical distribution of these P&L values is analyzed to assess hedging effectiveness, using metrics such as mean, standard-deviation, and quantiles.

### 3.2 Shortcomings of the self-financing approach compared to profit and loss

Consider a European call option with maturity TT and terminal payoff g​(XT,P):=(XT−P)+g(X\_{T},P):=(X\_{T}-P)^{+}, where P>0P>0 is the strike price. We simulate trajectories using the stochastic volatility model from Definition [3.1](https://arxiv.org/html/2511.20837v1#S3.Thmtheoreme1 "Definition 3.1. ‣ 3.1 The market model ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"), with the parameters reported in Table [1](https://arxiv.org/html/2511.20837v1#S3.T1 "Table 1 ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") for the dynamics of the underlying asset, volatility and the stochastic correlation.

|  |  |  |
| --- | --- | --- |
|  | ParametersValueμ0a5σ∘0.2ξ0.5γ0.7b5p∘−0.3χ0.5\begin{array}[]{|c|c|}\hline\cr\text{Parameters}&\text{Value}\\ \hline\cr\mu&0\\ a&5\\ \sigma\_{\circ}&0.2\\ \xi&0.5\\ \gamma&0.7\\ b&5\\ p\_{\circ}&-0.3\\ \chi&0.5\\ \hline\cr\end{array} |  |

  


Table 1: Parameters for the model in Definition [3.1](https://arxiv.org/html/2511.20837v1#S3.Thmtheoreme1 "Definition 3.1. ‣ 3.1 The market model ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

#### 3.2.1 Comparison of the different loss functions

The neural network is a fully-connected multilayer perceptron [[13](https://arxiv.org/html/2511.20837v1#bib.bib13)] with three layers, each containing 32 neurons, and tanh\tanh activation functions. The network parameters θ\theta are trained using the Adam optimiser [[9](https://arxiv.org/html/2511.20837v1#bib.bib9)] implemented in PyTorch [[11](https://arxiv.org/html/2511.20837v1#bib.bib11)].

For each market configuration considered in Definition [2.4](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme4 "Definition 2.4. ‣ 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"), we train the network separately using two different objective functions:

For each case of Definition [2.4](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme4 "Definition 2.4. ‣ 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"), we train the network separately using two different objective functions:

* •

  the *self-financing loss* introduced in Definition [2.2](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme2 "Definition 2.2 (Self-financing approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"),
* •

  the *P&L loss* introduced in Definition [2.3](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme3 "Definition 2.3 (Profit and Loss approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

The purpose of this section is to demonstrate that, *across all specifications in Definition [2.4](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme4 "Definition 2.4. ‣ 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")*, the P&L loss systematically delivers superior out-of-sample hedging performance compared with the classical self-financing loss.

In the figures reporting the neural network prices, we also display the Black–Scholes price (computed with the initial volatility σ∘\sigma\_{\circ}) purely as a familiar benchmark. This Black–Scholes value is neither the true theoretical price (which does not admit a closed form in our incomplete market with discrete hedging) nor the target of the training procedure.

Trained parameters are denoted θ^\widehat{\theta} and are obtained after 10510^{5} optimisation epochs.

##### The unconstrained case

In this first setting, we use the neural network directly as the pricing and hedging function:
N¯θ=Nθ\overline{N}\_{\theta}=N\_{\theta}.

Figure [1](https://arxiv.org/html/2511.20837v1#S3.F1 "Figure 1 ‣ The unconstrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") displays the learned pricing functions together with the true terminal payoff for a fixed initial volatility σ∘\sigma\_{\circ}. The left panel corresponds to the network trained with the self-financing (replication) loss, and the right panel to the network trained with the direct P&L loss.

![Refer to caption](x1.png)


(a) Self-financing loss.

![Refer to caption](x2.png)


(b) P&L loss.

Figure 1: Pricing functions learned in the unconstrained case with T=2T=2, K=1.2K=1.2, and P=1P=1.

Both networks struggle to fit the kink of the payoff exactly at-the-money because NθN\_{\theta} is continuously differentiable while the call payoff is not. This well-known limitation of smooth approximations is visible near XT=KX\_{T}=K.

The out-of-sample hedging performance is shown in Figure [2](https://arxiv.org/html/2511.20837v1#S3.F2 "Figure 2 ‣ The unconstrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") and quantified in Table [2](https://arxiv.org/html/2511.20837v1#S3.T2 "Table 2 ‣ The unconstrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"). All P&L figures are expressed as percentages of the Black-Scholes initial price.

![Refer to caption](x3.png)


(a) Self-financing loss

![Refer to caption](x4.png)


(b) P&L loss

Figure 2: Empirical P&L distributions for the neural network hedge and the Black–Scholes delta hedge in the unconstrained case. T=2,K=1.2,P=1T=2,K=1.2,P=1, and X0=1X\_{0}=1.



| Statistic | Black-Scholes hedging | Neural Network hedging (SF) | Neural Network hedging (PL) |
| --- | --- | --- | --- |
| Mean | -1.839 % | 11.739 % | -0.572 % |
| S.D. | 16.11 % | 15.80 % | 12.84 % |
| Quantile 1%1\% | -47.93 % | -30.64 % | -37.14 % |
| Quantile 10%10\% | -21.26 % | -6.37 % | -15.51 % |
| Quantile 90%90\% | 17.11 % | 31.97 % | 14.82 % |
| Quantile 99%99\% | 35.61 % | 49.67 % | 31.46 % |

Table 2: Summary statistics of the P&L distributions shown in Figure [2](https://arxiv.org/html/2511.20837v1#S3.F2 "Figure 2 ‣ The unconstrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

The network trained with the self-financing loss tends to overestimate the option price and delivers hedging errors comparable to a Black–Scholes delta hedge. In contrast, the network trained with the direct P&L loss produces a nearly unbiased price and significantly reduces the dispersion of the terminal P&L.

Despite these gains, the difficulty of fitting the non-differentiable payoff at maturity remains in both cases (Figure [1](https://arxiv.org/html/2511.20837v1#S3.F1 "Figure 1 ‣ The unconstrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")). For more exotic options, the payoff can even be discontinuous, making the problem considerably harder.

The next three approaches are specifically designed to better handle non-smooth terminal conditions.

##### The zero-target case

This framework corresponds to:

|  |  |  |
| --- | --- | --- |
|  | N¯θ​(T−t,x,c,K,P)=sT​f​(T−t,x,c,K,P)+Nθ​(T−t,x,c,K,P),\overline{N}\_{\theta}(T-t,x,c,K,P)=\frac{s}{T}f(T-t,x,c,K,P)+N\_{\theta}(T-t,x,c,K,P), |  |

where f​(0,x,c,K,P)=g​(x,P)f(0,x,c,K,P)=g(x,P). We use the Black-Scholes formula with constant volatility σ∘\sigma\_{\circ} from Table [1](https://arxiv.org/html/2511.20837v1#S3.T1 "Table 1 ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"), i.e. in our context:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(T−t,x,c,K,P)\displaystyle f(T-t,x,c,K,P) | :=B​S​(T−t,x,P)\displaystyle=BS(T-t,x,P) |  | (3.2) |
|  |  | =x​Φ​[d1​(T−t,x,P)]−P​e−r​(T−t)​Φ​[d1​(T−t,x,P)−σ∘​T−t],\displaystyle=x\Phi[d\_{1}(T-t,x,P)]-Pe^{-r(T-t)}\Phi[d\_{1}(T-t,x,P)-\sigma\_{\circ}\sqrt{T-t}], |  |

where

|  |  |  |
| --- | --- | --- |
|  | d1​(T−t,x,P):=1σ∘​T−t​[log⁡(xP)+(r+σ∘22)​(T−t)].d\_{1}(T-t,x,P):=\frac{1}{\sigma\_{\circ}\sqrt{T-t}}\left[\log\left(\frac{x}{P}\right)+\left(r+\frac{\sigma\_{\circ}^{2}}{2}\right)(T-t)\right]. |  |

Figure [3](https://arxiv.org/html/2511.20837v1#S3.F3 "Figure 3 ‣ The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") shows the resulting pricing functions. Thanks to the embedding, the terminal condition is now almost perfectly matched in both training objectives.

![Refer to caption](x5.png)


(a) Self-financing loss

![Refer to caption](x6.png)


(b) P&L loss

Figure 3: Pricing functions in the zero-target case, T=2,K=1.2,P=1T=2,K=1.2,P=1.

The out-of-sample hedging performance is presented in Figure [4](https://arxiv.org/html/2511.20837v1#S3.F4 "Figure 4 ‣ The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") and Table [3](https://arxiv.org/html/2511.20837v1#S3.T3 "Table 3 ‣ The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (expressed as percentages of the Black-Scholes price model).

To evaluate the hedging strategy’s effectiveness, we compare its Profit and Loss (P&L) distribution to that of the Black-Scholes model in Figure [4](https://arxiv.org/html/2511.20837v1#S3.F4 "Figure 4 ‣ The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (with the Self-Financing loss on the left and the P&L loss on the right) and we provide some statistics about the distributions in Table [3](https://arxiv.org/html/2511.20837v1#S3.T3 "Table 3 ‣ The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

![Refer to caption](x7.png)


(a) Self-financing loss

![Refer to caption](x8.png)


(b) P&L loss

Figure 4: Empirical P&L distributions for the neural network hedge and the Black–Scholes delta hedge in the zero-target case. T=2,K=1.2,P=1T=2,K=1.2,P=1 and X0=1X\_{0}=1.



| Statistic | Black-Scholes hedging | Neural Network hedging (SF) | Neural Network hedging (PL) |
| --- | --- | --- | --- |
| Mean | -1.839 % | 19.11 % | 1.209 % |
| S.D. | 16.11 % | 15.40 % | 12.57 % |
| Quantile 1%1\% | -47.93 % | -20.71 % | -34.42 % |
| Quantile 10%10\% | -21.26 % | 0.87 % | -12.98 % |
| Quantile 90%90\% | 17.11 % | 38.38 % | 15.87 % |
| Quantile 99%99\% | 35.61 % | 56.01 % | 34.42 % |

Table 3: Summary statistics of the P&L distributions shown in Figure [4](https://arxiv.org/html/2511.20837v1#S3.F4 "Figure 4 ‣ The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

Again, the neural network’s hedging strategy and price using the Self-Financing loss yields modest results. The price is overestimated and the quality of the hedge is similar to the one of Black-Scholes. The P&L loss approach based on Definition [2.3](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme3 "Definition 2.3 (Profit and Loss approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") outperforms the self-financing approach.

##### The control-variate case

We set :

|  |  |  |
| --- | --- | --- |
|  | N¯θ​(T−t,x,c,K,P)=f​(T−t,x,c,K,P)+Nθ​(T−t,x,c,K,P)\overline{N}\_{\theta}(T-t,x,c,K,P)=f(T-t,x,c,K,P)+N\_{\theta}(T-t,x,c,K,P) |  |

where ff is chosen as the Black-Scholes formula in ([3.2](https://arxiv.org/html/2511.20837v1#S3.E2 "In The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")).

Figure [5](https://arxiv.org/html/2511.20837v1#S3.F5 "Figure 5 ‣ The control-variate case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") shows the prices obtained, for a fixed volatility of σ∘\sigma\_{\circ}, with the Self Financing loss (Figure [5(a)](https://arxiv.org/html/2511.20837v1#S3.F5.sf1 "In Figure 5 ‣ The control-variate case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") on the left) and with the P&L loss (Figure [5(b)](https://arxiv.org/html/2511.20837v1#S3.F5.sf2 "In Figure 5 ‣ The control-variate case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") on the right).

![Refer to caption](x9.png)


(a) Self-financing loss.

![Refer to caption](x10.png)


(b) P&L loss.

Figure 5: Pricing functions in the control-variate case, T=2,K=1.2,P=1T=2,K=1.2,P=1.

The terminal condition is well fitted. We observe again that the Self-Financing approach gives higher prices.

To evaluate the hedging strategy’s effectiveness, we compare its Profit and Loss (P&L) distribution to that of the Black-Scholes model in Figure [6](https://arxiv.org/html/2511.20837v1#S3.F6 "Figure 6 ‣ The control-variate case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (with the Self-Financing loss on the left and the P&L loss on the right) and we provide some statistics about the distributions in Table [4](https://arxiv.org/html/2511.20837v1#S3.T4 "Table 4 ‣ The control-variate case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

![Refer to caption](x11.png)


(a) Self-financing loss.

![Refer to caption](x12.png)


(b) P&L loss.

Figure 6: Empirical P&L distributions for the neural network hedge and the Black–Scholes delta hedge in the control-variate case. T=2,K=1.2,P=1T=2,K=1.2,P=1 and X0=1X\_{0}=1.



| Statistic | Black-Scholes hedging | Neural Network hedging (SF) | Neural Network hedging (PL) |
| --- | --- | --- | --- |
| Mean | -1.839 % | 16.181 % | 0.407 % |
| S.D. | 16.11 % | 15.80 % | 12.21 % |
| Quantile 1%1\% | -47.93 % | -21.19 % | -34.45 % |
| Quantile 10%10\% | -21.26 % | -0.17 % | -14.04 % |
| Quantile 90%90\% | 17.11 % | 34.01 % | 14.22 % |
| Quantile 99%99\% | 35.61 % | 50.61 % | 32.40 % |

Table 4: Summary statistics of the P&L distributions shown in Figure [6](https://arxiv.org/html/2511.20837v1#S3.F6 "Figure 6 ‣ The control-variate case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

Again, the neural network’s hedging strategy and price using the Self-Financing loss yields modest results. The price is overestimated and the quality of the hedge is similar to the one of Black-Scholes. The P&L loss approach based on Definition [2.3](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme3 "Definition 2.3 (Profit and Loss approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") outperforms the self-financing approach.

##### The constrained case

In this approach,

|  |  |  |
| --- | --- | --- |
|  | N¯θ​(T−t,x,c,K,P)=sT​f​(T−t,x,c,K,P)+(1−sT)​Nθ​(T−t,x,c,K,P)\overline{N}\_{\theta}(T-t,x,c,K,P)=\frac{s}{T}f(T-t,x,c,K,P)+\left(1-\frac{s}{T}\right)N\_{\theta}(T-t,x,c,K,P) |  |

where ff is the Black-Scholes formula in ([3.2](https://arxiv.org/html/2511.20837v1#S3.E2 "In The zero-target case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")).

Figure [7](https://arxiv.org/html/2511.20837v1#S3.F7 "Figure 7 ‣ The constrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") shows the prices obtained, for a fixed volatility of σ∘\sigma\_{\circ}, with the Self Financing loss on the left and the P&L loss on the right.

![Refer to caption](x13.png)


(a) Self-financing loss.

![Refer to caption](x14.png)


(b) P&L loss.

Figure 7: Pricing functions in the control-variate case, T=2,K=1.2,P=1T=2,K=1.2,P=1.

The terminal condition is perfectly reproduced in both training settings. We observe again that the Self-Financing approach gives higher prices. Out-of-sample hedging performance is shown in Figure [8](https://arxiv.org/html/2511.20837v1#S3.F8 "Figure 8 ‣ The constrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") and summarized in Table [5](https://arxiv.org/html/2511.20837v1#S3.T5 "Table 5 ‣ The constrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (P&L expressed as percentages of the initial model price).

![Refer to caption](x15.png)


(a) Self-financing loss.

![Refer to caption](x16.png)


(b) P&L loss.

Figure 8: Empirical P&L distributions for the neural network hedge and the Black–Scholes delta hedge in the control-variate case. T=2,K=1.2,P=1T=2,K=1.2,P=1 and X0=1X\_{0}=1.



| Statistic | Black-Scholes hedging | Neural Network hedging (SF) | Neural Network hedging (PL) |
| --- | --- | --- | --- |
| Mean | -1.839 % | 13.960 % | -0.183 % |
| S.D. | 16.11 % | 14.54 % | 12.48 % |
| Quantile 1%1\% | -47.93 % | -24.27 % | -35.54 % |
| Quantile 10%10\% | -21.26 % | -2.90 % | -14.58 % |
| Quantile 90%90\% | 17.11 % | 32.06 % | 14.68 % |
| Quantile 99%99\% | 35.61 % | 49.25 % | 31.67 % |

Table 5: Summary statistics of the P&L distributions shown in Figure [8](https://arxiv.org/html/2511.20837v1#S3.F8 "Figure 8 ‣ The constrained case ‣ 3.2.1 Comparison of the different loss functions ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

The pattern observed in the previous cases repeats: the self-financing loss produces a significantly upward-biased price and hedging errors comparable to those of a plain Black–Scholes strategy. By contrast, the P&L loss yields an almost unbiased initial price and markedly lower P&L dispersion, confirming its clear superiority also when a control-variate structure is used.

#### 3.2.2 Conclusion

Across all architectures considered in Definition [2.4](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme4 "Definition 2.4. ‣ 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"), the direct P&L loss (Definition [2.3](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme3 "Definition 2.3 (Profit and Loss approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) consistently delivers superior out-of-sample hedging performance compared with the classical self-financing loss. We therefore discard the self-financing loss as a standalone objective and retain only the P&L loss for the remainder of the study.

Nevertheless, the pure P&L loss has one important limitation: the loss function only directly constrains the price at maturity. Formally, if N¯θ^\overline{N}\_{\widehat{\theta}} is the trained network and b​(t)b(t) is any deterministic function such that b​(T)=0b(T)=0, then the modified function

|  |  |  |
| --- | --- | --- |
|  | N¯θ^​(t,x,c,K,P)+b​(t)\overline{N}\_{\widehat{\theta}}(t,x,c,K,P)+b(t) |  |

yields the same P&L loss as N¯θ^\overline{N}\_{\widehat{\theta}}. This behavior is observed empirically. To obtain coherent prices at all times while preserving strong hedging performance, we combine the two losses with suitable weights. In our experiments, assigning a weight of 5 to the self-financing loss and 1 to the P&L loss proves effective.

An alternative simple regularization consists of including paths that start at random intermediate dates. In that case, dates close to maturity naturally receive higher weight in the Monte Carlo average.

Table [6](https://arxiv.org/html/2511.20837v1#S3.T6 "Table 6 ‣ 3.2.2 Conclusion ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") summarises the out-of-sample P&L performance of the P&L-trained networks under the four terminal-condition treatments.

| Statistic | Black-Scholes | Unconstrained | Zero-target | Control-variate | Constrained |
| --- | --- | --- | --- | --- | --- |
| Mean | -1.839 % | -0.572 % | 1.209 % | 0.407 % | -0.183 % |
| S.D. | 16.11 % | 12.84 % | 12.57 % | 12.21 % | 12.48 % |
| Quantile 1%1\% | -47.93 % | -37.14 % | -34.42 % | -34.45 % | -35.54 % |
| Quantile 10%10\% | -21.26 % | -15.51 % | -12.98 % | -14.04 % | -14.58 % |
| Quantile 90%90\% | 17.11 % | 14.82 % | 15.87 % | 14.22 % | 14.68 % |
| Quantile 99%99\% | 35.61 % | 31.46 % | 34.42 % | 32.40 % | 31.67 % |

Table 6: Summary statistics of the P&L distributions.

We also compare the four methods for handling the terminal condition. The pricing charts show that the Unconstrained approach struggles to fit the payoff kink at-the-money at maturity. Nevertheless, Table [6](https://arxiv.org/html/2511.20837v1#S3.T6 "Table 6 ‣ 3.2.2 Conclusion ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") reveals very similar overall hedging performance across all variants.
The only noticeable difference is that the Unconstrained case has a slightly higher P&L standard deviation (roughly 2% to 5%) than the three methods that explicitly enforce the terminal payoff.

### 3.3 Results on other simple options

Having established in the previous section that the direct P&L loss (Definition [2.3](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme3 "Definition 2.3 (Profit and Loss approach). ‣ 2.4 Training objective and loss functions ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) systematically dominates the self-financing loss, we now retain only the P&L loss and compare the four terminal condition treatments of Definition [2.4](https://arxiv.org/html/2511.20837v1#S2.Thmtheoreme4 "Definition 2.4. ‣ 2.5 Constrained architectures for non-smooth payoffs ‣ 2 The framework ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") on two additional elementary payoffs :

* •

  the square option: g​(XT,K)=(XT−K)2g(X\_{T},K)=(X\_{T}-K)^{2} (smooth payoff),
* •

  the digital (binary) option: g​(XT,K)=𝟏{XT>K}g(X\_{T},K)=\mathbf{1}\_{\{X\_{T}>K\}} (discontinuous payoff).

These two contracts provide useful contrasts with the vanilla call studied earlier: the square payoff is infinitely differentiable, while the digital payoff is discontinuous at the strike.
When a baseline function ff is required (zero-target, control-variate, and constrained cases), we use the exact Black–Scholes price of the corresponding payoff assuming constant volatility σ∘\sigma\_{\circ} (Table [1](https://arxiv.org/html/2511.20837v1#S3.T1 "Table 1 ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")).

#### 3.3.1 The square option

The square option has payoff g​(XT,P)=(XT−P)2g(X\_{T},P)=(X\_{T}-P)^{2}. Because the terminal condition is smooth, we expect the embedding of ff to be less critical than for non-smooth payoffs.

Figure [9](https://arxiv.org/html/2511.20837v1#S3.F9 "Figure 9 ‣ 3.3.1 The square option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") shows the learned pricing function, while Figure [10](https://arxiv.org/html/2511.20837v1#S3.F10 "Figure 10 ‣ 3.3.1 The square option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") displays the corresponding out-of-sample P&L distributions. Numerical summary statistics are reported in Table [7](https://arxiv.org/html/2511.20837v1#S3.T7 "Table 7 ‣ 3.3.1 The square option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (P&L expressed as percentages of the Black–Scholes benchmark price of the square option).

![Refer to caption](x17.png)


(a) Unconstrained.

![Refer to caption](x18.png)


(b) Zero-target.

![Refer to caption](x19.png)


(c) Control-variate.

![Refer to caption](x20.png)


(d) Constrained.

Figure 9: Pricing functions for the square option with T=2,K=1.2,P=1T=2,K=1.2,P=1.



![Refer to caption](x21.png)


(a) Unconstrained.

![Refer to caption](x22.png)


(b) Zero-target.

![Refer to caption](x23.png)


(c) Control-variate.

![Refer to caption](x24.png)


(d) Constrained.

Figure 10: Empirical P&L distributions for the neural network hedge and the Black–Scholes delta hedge for the square option with T=2,K=1.2,P=1T=2,K=1.2,P=1 and X0=1X\_{0}=1.



| Statistic | Black-Scholes | Unconstrained | Zero-target | Control-variate | Constrained |
| --- | --- | --- | --- | --- | --- |
| Mean | -2.994 % | 0.046 % | -0.315 % | -4.547 % | -1.895 % |
| S.D. | 28.09 % | 19.77 % | 16.46 % | 17.21 % | 17.19 % |
| Quantile 1%1\% | -82.82 % | -62.23 % | -43.71 % | -47.40 % | -45.84 % |
| Quantile 10%10\% | -34.47 % | -21.26 % | -16.62 % | -21.16 % | -19.03 % |
| Quantile 90%90\% | 27.19 % | 18.65 % | 15.47 % | 10.63 % | 13.86 % |
| Quantile 99%99\% | 62.29 % | 38.14 % | 47.79 % | 43.69 % | 47.98 % |

Table 7: Summary P&L statistics for the square option.

Even though the payoff is perfectly smooth, the Unconstrained approach, while producing the most accurate initial price, still delivers the poorest hedging performance, exactly as observed for the vanilla call. Its P&L standard deviation is approximately 15–20% higher than that of the three methods that explicitly embed the terminal condition, and its 1% quantile is substantially worse. Enforcing the exact payoff at maturity is critical for robust out-of-sample hedging, regardless of the smoothness of the terminal condition.

#### 3.3.2 The digital option

We finally consider a digital call with payoff g​(XT,P)=𝟏{XT>P}g(X\_{T},P)=\mathbf{1}\_{\{X\_{T}>P\}}. This contract is the most challenging of the three because the terminal payoff is discontinuous at the strike. As before, whenever a baseline function ff is required (zero-target, control-variate, and constrained cases), we use the exact Black–Scholes digital price computed with constant volatility σ∘\sigma\_{\circ}.

Figure [11](https://arxiv.org/html/2511.20837v1#S3.F11 "Figure 11 ‣ 3.3.2 The digital option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") displays the learned pricing function, Figure [12](https://arxiv.org/html/2511.20837v1#S3.F12 "Figure 12 ‣ 3.3.2 The digital option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") the out-of-sample P&L distributions, and Table [8](https://arxiv.org/html/2511.20837v1#S3.T8 "Table 8 ‣ 3.3.2 The digital option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") the corresponding summary statistics (P&L expressed as percentages of the Black–Scholes digital call price).

![Refer to caption](x25.png)


(a) Unconstrained.

![Refer to caption](x26.png)


(b) Zero-target.

![Refer to caption](x27.png)


(c) Control-variate.

![Refer to caption](x28.png)


(d) Constrained.

Figure 11: Pricing functions for the digital option with T=2,K=1.2,P=1T=2,K=1.2,P=1.



![Refer to caption](x29.png)


(a) Unconstrained.

![Refer to caption](x30.png)


(b) Zero-target.

![Refer to caption](x31.png)


(c) Control-variate.

![Refer to caption](x32.png)


(d) Constrained.

Figure 12: Empirical P&L distributions for the neural network hedge and the Black–Scholes delta hedge for the digital call option with T=2,K=1.2,P=1T=2,K=1.2,P=1 and X0=1X\_{0}=1.



| Statistic | Black-Scholes | Unconstrained | Zero-target | Control-variate | Constrained |
| --- | --- | --- | --- | --- | --- |
| Mean | -2.345 % | -3.856 % | -0.479 % | -1.950 % | -0.996 % |
| S.D. | 30.06 % | 28.41 % | 28.59 % | 28.11 % | 29.46 % |
| Quantile 1%1\% | -99.54 % | -122.30 % | -85.39 % | -95.96 % | -94.63 % |
| Quantile 10%10\% | -22.73 % | -22.55 % | -15.89 % | -18.57 % | -19.08 % |
| Quantile 90%90\% | 17.76 % | 15.60 % | 18.17 % | 15.13 % | 17.31 % |
| Quantile 99%99\% | 98.29 % | 76.56 % | 99.94 % | 95.45 % | 98.97 % |

Table 8: Summary P&L statistics for the digital option.

The Unconstrained method gives the least accurate price (see Figure [11(a)](https://arxiv.org/html/2511.20837v1#S3.F11.sf1 "In Figure 11 ‣ 3.3.2 The digital option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")). In terms of hedging, the standard deviations of the P&L are very similar across all four approaches, with the Constrained method being marginally the highest. Overall, the three methods that embed the terminal condition do not show a decisive advantage in variance reduction for this strongly discontinuous payoff. Nevertheless, the Unconstrained approach still exhibits the worst downside risk, with the most negative 1% quantile.

#### 3.3.3 Conclusion

Our analysis of the square option, with its smooth payoff (XT−P)2(X\_{T}-P)^{2}, shows that the Unconstrained method, despite delivering a seemingly accurate initial price, performs the worst in terms of hedging effectiveness. Among the methods that incorporate the baseline function ff to embed the terminal condition, the Zero-Target approach achieves the best overall performance for this contract.

For the digital option, which has a discontinuous payoff, the Unconstrained method struggles significantly with the terminal condition and produces the least accurate price. The other three methods also exhibit minor fitting imperfections for the payoff but outperform the Unconstrained case in pricing accuracy. In terms of P&L standard deviation, all approaches yield comparable results; however, the Unconstrained method consistently displays the worst tail quantiles, indicating poorer protection in extreme scenarios.

Although a call-spread approximation could have been used for the digital option, our purpose was precisely to handle a genuinely difficult payoff. We now proceed with the Equinox option, an exotic contract with a complex payoff structure, to further assess the robustness of the proposed neural network approaches on challenging terminal conditions.

### 3.4 The Equinox option

We introduce a more structured exotic contract that we call the Equinox option. Its payoff at the final horizon T+RT+R is defined, for parameters R>0R>0, B>0B>0, P>0P>0, G≥0G\geq 0, as

|  |  |  |
| --- | --- | --- |
|  | g​(XT+R,(B,P,G))=𝟏{XT≤B}​(XT+R−P)++G​𝟏{XT>B}.g(X\_{T+R},(B,P,G))=\mathbf{1}\_{\{X\_{T}\leq B\}}(X\_{T+R}-P)^{+}+G\mathbf{1}\_{\{X\_{T}>B\}}. |  |

The contract therefore naturally decomposes into two components:

|  |  |  |
| --- | --- | --- |
|  | g​(XT+R,(B,P,G))=g1​(XT+R,(R,B,P))+G​g2​(XT+R,B),g(X\_{T+R},(B,P,G))=g\_{1}(X\_{T+R},(R,B,P))+Gg\_{2}(X\_{T+R},B), |  |

where:

|  |  |  |
| --- | --- | --- |
|  | g1​(XT+R,(R,B,P))=𝟏{XT≤B}​(XT+R−P)+andg2​(XT+R,B)=𝟏{XT>B}.g\_{1}(X\_{T+R},(R,B,P))=\mathbf{1}\_{\{X\_{T}\leq B\}}(X\_{T+R}-P)^{+}\quad\text{and}\quad g\_{2}(X\_{T+R},B)=\mathbf{1}\_{\{X\_{T}>B\}}. |  |

At time TT (time-to-maturity RR) the barrier event is revealed, and:

* •

  The payoff of g1g\_{1} is either 0 or equivalent to a call option with time to maturity RR and strike price PP.
* •

  The payoff of g2g\_{2} at maturity is either 0 or 1, resembling a digital option, adjusted for interest rates over the period [T,T+R][T,T+R], as estimated in Section [3.3.2](https://arxiv.org/html/2511.20837v1#S3.SS3.SSS2 "3.3.2 The digital option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

To price and hedge the Equinox option over the first period [0,T][0,T] using our neural network framework requires addressing the terminal condition at time TT:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g1′​(XT,(R,B,P))=𝟏{XT≤B}​Call​(R,XT,CT,K,P),g\_{1}^{\prime}(X\_{T},(R,B,P))=\mathbf{1}\_{\{X\_{T}\leq B\}}\text{Call}(R,X\_{T},C\_{T},K,P), |  | (3.3) |

where Call​(R,XT,CT,P)\text{Call}(R,X\_{T},C\_{T},P) is the fair price at time TT of a call with remaining maturity RR and strike PP. We propose the following practical implementation:

* •

  Train a first neural network Call using N¯θ∘∘\overline{N}\_{\theta^{\circ}}^{\circ} on vanilla calls using the methodology developed in Section [3.2](https://arxiv.org/html/2511.20837v1#S3.SS2 "3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").
* •

  Train a second neural network N¯θ\overline{N}\_{\theta} with the payoff 𝟏{XT≤B}​N¯θ^∘∘​(R,XT,CT,K,P)\mathbf{1}\_{\{X\_{T}\leq B\}}\overline{N}\_{\widehat{\theta}^{\circ}}^{\circ}(R,X\_{T},C\_{T},K,P).

A suitable function ff is:

|  |  |  |
| --- | --- | --- |
|  | f​(T−s,x,c,K,R,B,P)=h​(T−s,x,B)×N¯θ^∘∘​(R+(T−s),x,c,K,P),f(T-s,x,c,K,R,B,P)=h(T-s,x,B)\times\overline{N}\_{\widehat{\theta}^{\circ}}^{\circ}(R+(T-s),x,c,K,P), |  |

where hh represents the price of a digital option in the Black-Scholes model. Note that this is not the standard Black-Scholes price, as XTX\_{T} and XT+RX\_{T+R} are not independent.

We then consider two modeling strategies:

##### Two separate networks.

Train independently:

* •

  Nθ11​(t,x,c,K,R,B,P)N\_{\theta^{1}}^{1}(t,x,c,K,R,B,P) for the g1g\_{1} component (using the embedding ff above in the zero-target/control-variate/constrained setting),
* •

  Nθ22​(t,x,c,K,R,B)N\_{\theta^{2}}^{2}(t,x,c,K,R,B) for the pure digital g2g\_{2} component (Section [3.3.2](https://arxiv.org/html/2511.20837v1#S3.SS3.SSS2 "3.3.2 The digital option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")).

The Equinox price is then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nθ11​(R+T−t,x,c,K,R,B,P)+G​e−r​(R+T−t)​Nθ22​(R+T−t,x,c,K,B).N\_{\theta^{1}}^{1}(R+T-t,x,c,K,R,B,P)+Ge^{-r(R+T-t)}N\_{\theta^{2}}^{2}(R+T-t,x,c,K,B). |  | (3.4) |

##### Single end-to-end network.

Train one global network Nθ​(R+T−t,x,c,K,R,B,P,G)N\_{\theta}(R+T-t,x,c,K,R,B,P,G) directly on the full payoff gg using the P&L loss, with an appropriate embedding that combines the two baseline functions above (weighted by GG).

#### 3.4.1 Equinox option with two neural networks

We train two independent neural networks trained with the P&L loss.

* •

  Nθ11N\_{\theta^{1}}^{1} is dedicated to the barrier-call component with payoff g1g\_{1},
* •

  Nθ22N\_{\theta^{2}}^{2} is the digital option with payoff g2g\_{2}.

Together, these networks yield the Equinox option price and hedge, as specified in ([3.4](https://arxiv.org/html/2511.20837v1#S3.E4 "In Two separate networks. ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")).

We present the results. Figure [13](https://arxiv.org/html/2511.20837v1#S3.F13 "Figure 13 ‣ 3.4.1 Equinox option with two neural networks ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") shows the estimated price for specific parameters of Nθ11N\_{\theta^{1}}^{1}, which addresses only the payoff g1g\_{1}, excluding the digital option.

![Refer to caption](x33.png)


(a) Unconstrained.

![Refer to caption](x34.png)


(b) Zero-target.

![Refer to caption](x35.png)


(c) Control-variate.

![Refer to caption](x36.png)


(d) Constrained.

Figure 13: Pricing functions for the pure barrier-call component (G=0G=0) with parameters B=1B=1, P=0.8P=0.8, R=1R=1, T=2,K=1T=2,K=1.



![Refer to caption](x37.png)


(a) Unconstrained.

![Refer to caption](x38.png)


(b) Zero-target.

![Refer to caption](x39.png)


(c) Control-variate.

![Refer to caption](x40.png)


(d) Constrained.

Figure 14: Pricing functions for the full Equinox option with the parameters G=0.1G=0.1, B=1B=1, P=0.8P=0.8, R=1R=1, T=2,K=1T=2,K=1.

The Unconstrained version again struggles severely with the complex terminal condition (especially visible when G=0G=0), producing distorted pricing curves far from the true continuation value.

![Refer to caption](x41.png)


(a) Unconstrained.

![Refer to caption](x42.png)


(b) Zero-target.

![Refer to caption](x43.png)


(c) Control-variate.

![Refer to caption](x44.png)


(d) Constrained.

Figure 15: Empirical P&L distributions for the neural network hedge for the Equinox option with parameters B=1B=1, P=0.8P=0.8, R=1R=1, T=2,K=1T=2,K=1, and X0=1X\_{0}=1.



| Statistic | Unconstrained | Zero-target | Control-variate | Constrained |
| --- | --- | --- | --- | --- |
| Mean | 23.273 % | 8.903 % | 18.306 % | 11.396 % |
| S.D. | 64.89 % | 59.20 % | 57.06 % | 58.86 % |
| Quantile 1%1\% | -186.60 % | -160.57 % | -151.35 % | -155.88 % |
| Quantile 10%10\% | -33.17 % | -35.42 % | -23.52 % | -32.71 % |
| Quantile 90%90\% | 93.76 % | 57.69 % | 64.53 % | 60.81 % |
| Quantile 99%99\% | 209.69 % | 226.87 % | 223.67 % | 223.65 % |

Table 9: P&L statistics for the pure barrier-call component with G=0G=0 (in % of the Zero-target price).



| Statistic | Unconstrained | Zero-target | Control-variate | Constrained |
| --- | --- | --- | --- | --- |
| Mean | 12.269 % | 4.738 % | 9.689 % | 6.192 % |
| S.D. | 24.47 % | 18.77 % | 17.94 % | 18.95 % |
| Quantile 1%1\% | -56.35 % | -36.31 % | -30.70 % | -32.17 % |
| Quantile 10%10\% | -13.44 % | -11.82 % | -6.05 % | -11.99 % |
| Quantile 90%90\% | 43.43 % | 24.92 % | 27.96 % | 26.87 % |
| Quantile 99%99\% | 79.91 % | 61.84 % | 72.86 % | 71.95 % |

Table 10: P&L statistics for the full Equinox option with G=0.1G=0.1 (in % of the Zero-target price).

The Unconstrained method produces the least accurate results. Methods that incorporate the payoff condition yield a more accurate price and a better hedge. In the unconstrained framework, the standard deviation for the call component of the Equinox option is 10% to 14% higher than other methods (Table [9](https://arxiv.org/html/2511.20837v1#S3.T9 "Table 9 ‣ 3.4.1 Equinox option with two neural networks ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")), and for the full Equinox option, it is 29% to 36% higher (Table [10](https://arxiv.org/html/2511.20837v1#S3.T10 "Table 10 ‣ 3.4.1 Equinox option with two neural networks ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")). However, in all cases, the price appears to be overestimated.

#### 3.4.2 Equinox option with a single neural network

We estimate the neural network NθN\_{\theta}, that directly outputs the price and hedging strategy of the full Equinox option for any cash amount GG (in practice, G∈[0,0.15]G\in[0,0.15]). The network takes GG as an extra input dimension and is trained end-to-end with the P&L loss. Although this approach does not exploit the exact linearity in GG, it turns out to deliver the best overall performance.

Figures [16](https://arxiv.org/html/2511.20837v1#S3.F16 "Figure 16 ‣ 3.4.2 Equinox option with a single neural network ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") and [17](https://arxiv.org/html/2511.20837v1#S3.F17 "Figure 17 ‣ 3.4.2 Equinox option with a single neural network ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") display the learned price G=0G=0 and G=0.1G=0.1, respectively.

![Refer to caption](x45.png)


(a) Unconstrained.

![Refer to caption](x46.png)


(b) Zero-target.

![Refer to caption](x47.png)


(c) Control-variate.

![Refer to caption](x48.png)


(d) Constrained.

Figure 16: Pricing functions for the Equinox option with G=0G=0 (pure barrier-call component) with parameters B=1B=1, P=0.8P=0.8, R=1R=1, T=2,K=1T=2,K=1.



![Refer to caption](x49.png)


(a) Unconstrained.

![Refer to caption](x50.png)


(b) Zero-target.

![Refer to caption](x51.png)


(c) Control-variate.

![Refer to caption](x52.png)


(d) Constrained.

Figure 17: Pricing functions for the full Equinox option with G=0.1G=0.1, and B=1B=1, P=0.8P=0.8, R=1R=1, T=2,K=1T=2,K=1.

Out-of-sample hedging P&L are reported in Tables [11](https://arxiv.org/html/2511.20837v1#S3.T11 "Table 11 ‣ 3.4.2 Equinox option with a single neural network ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (G=0G=0) and [12](https://arxiv.org/html/2511.20837v1#S3.T12 "Table 12 ‣ 3.4.2 Equinox option with a single neural network ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") (G=0.1G=0.1). All P&L figures are expressed as percentages of the Zero-target model price.

![Refer to caption](x53.png)


(a) Unconstrained.

![Refer to caption](x54.png)


(b) Zero-target.

![Refer to caption](x55.png)


(c) Control-variate.

![Refer to caption](x56.png)


(d) Constrained.

Figure 18: Empirical P&L distributions for the neural network hedge for the Equinox option with parameters B=1B=1, P=0.8P=0.8, R=1R=1, T=2,K=1T=2,K=1, and X0=1X\_{0}=1.



| Statistics (G=0G=0) | Unconstrained | Zero-target | Control-variate | Constrained |
| --- | --- | --- | --- | --- |
| Mean | -8.764 % | -3.218 % | -1.200 % | 10.501 % |
| S.D. | 61.34 % | 58.92 % | 58.32 % | 57.37 % |
| Quantile 1%1\% | -189.42 % | -170.88 % | -183.38 % | -147.91 % |
| Quantile 10%10\% | -60.36 % | -49.30 % | -56.85 % | -27.48 % |
| Quantile 90%90\% | 48.99 % | 43.70 % | 43.63 % | 60.20 % |
| Quantile 99%99\% | 198.69 % | 208.58 % | 186.13 % | 231.32 % |

Table 11: P&L statistics for the pure barrier-call G=0G=0.



| Statistics (G=0.1G=0.1) | Unconstrained | Zero-target | Control-variate | Constrained |
| --- | --- | --- | --- | --- |
| Mean | -1.774 % | -1.451 % | -1.191 % | 4.864 % |
| S.D. | 19.05 % | 17.64 % | 17.94 % | 17.19 % |
| Quantile 1%1\% | -57.45 % | -43.04 % | -49.76 % | -30.20 % |
| Quantile 10%10\% | -21.64 % | -17.48 % | -21.90 % | -8.78 % |
| Quantile 90%90\% | 18.17 % | 15.44 % | 15.55 % | 23.15 % |
| Quantile 99%99\% | 55.47 % | 61.84 % | 51.53 % | 71.23 % |

Table 12: P&L statistics for the pure barrier-call G=0.1G=0.1.

The single-network approach clearly dominates the two-network strategy of Section [3.4.1](https://arxiv.org/html/2511.20837v1#S3.SS4.SSS1 "3.4.1 Equinox option with two neural networks ‣ 3.4 The Equinox option ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"). The Control Variate method achieves the highest price accuracy, while it also exhibits a slightly lower standard deviation, albeit with reduced price accuracy compared to other methods. The Unconstrained method again produces the largest standard deviation among the neural network hedges, exceeding the three methods that embed the terminal condition by 4% to 7% for G=0G=0 and by 6% to 11% for G=0.1G=0.1.

### 3.5 Robustness with jumps

To test the robustness of our deep-hedging framework to sudden regime shifts and model misspecification, we extend the stochastic-volatility model of Definition [3.1](https://arxiv.org/html/2511.20837v1#S3.Thmtheoreme1 "Definition 3.1. ‣ 3.1 The market model ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") by adding pure upward jumps to the volatility process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σst,σ=σ\displaystyle\Sigma\_{s}^{t,\sigma}=\sigma | +∫ts−a​(Σut,σ−σ∘)​d​u+∫tsξ​(Σut,σ)γ​d​(ρut,p​Wu1+1−(ρut,p)2​Wu2)\displaystyle+\int\_{t}^{s}-a(\Sigma\_{u}^{t,\sigma}-\sigma\_{\circ})du+\int\_{t}^{s}\xi(\Sigma\_{u}^{t,\sigma})^{\gamma}d(\rho\_{u}^{t,p}W\_{u}^{1}+\sqrt{1-(\rho\_{u}^{t,p})^{2}}W\_{u}^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫tsκ​𝑑Nu,\displaystyle+\int\_{t}^{s}\kappa dN\_{u}, |  |

where (Nt)0≤t≤T(N\_{t})\_{0\leq t\leq T} is an independent Poisson process with intensity λ>0\lambda>0, and κ>0\kappa>0 is the fixed jump size.

We keep all other parameters from Table [1](https://arxiv.org/html/2511.20837v1#S3.T1 "Table 1 ‣ 3.2 Shortcomings of the self-financing approach compared to profit and loss ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") and focus exclusively on the digital option (Section [3.3.2](https://arxiv.org/html/2511.20837v1#S3.SS3.SSS2 "3.3.2 The digital option ‣ 3.3 Results on other simple options ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) priced and hedged with the Zero-target embedding. We train three separate networks with λ∈{0, 0.5, 2}\lambda\in\{0,\;0.5,\;2\} and test each of them out-of-sample under all three true intensities.

![Refer to caption](x57.png)


Figure 19: Network trained with no volatility jumps λ=0\lambda=0. P&L density under true intensity λ∈{0, 0.5, 2}\lambda\in\{0,\;0.5,\;2\}.

Figure [19](https://arxiv.org/html/2511.20837v1#S3.F19 "Figure 19 ‣ 3.5 Robustness with jumps ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets") shows the network trained in the original jump-free model. When a moderate number of jumps occurs in reality, (λ=0.5)(\lambda=0.5), performance degrades gracefully: the distribution widens and the left tail becomes slightly heavier, but hedging remains reasonably effective. At high intensity (λ=2\lambda=2), however, the hedge collapses, with catastrophic losses on a non-negligible fraction of paths.

![Refer to caption](x58.png)


(a) Trained with λ=0.5\lambda=0.5.

![Refer to caption](x59.png)


(b) Trained with λ=2\lambda=2.

Figure 20: Networks trained with jumps. P&L density under true intensity λ∈{0, 0.5, 2}\lambda\in\{0,\;0.5,\;2\}.

In Figure [20](https://arxiv.org/html/2511.20837v1#S3.F20 "Figure 20 ‣ 3.5 Robustness with jumps ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets"), we examine a model with jumps to assess whether the neural network can still hedge the option effectively and to analyze the P&L behavior under model misspecifications.

The network trained with λ=0.5\lambda=0.5 (Figure [20(a)](https://arxiv.org/html/2511.20837v1#S3.F20.sf1 "In Figure 20 ‣ 3.5 Robustness with jumps ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) delivers excellent hedging performance under the correctly specified model (green curve) and degrades only mildly when tested under λ=0\lambda=0 (no jumps) or λ=2\lambda=2 (four times more jumps). In particular, its behavior under severe upward misspecification (λ=2\lambda=2 in reality) is dramatically better than the collapse observed in Figure [19](https://arxiv.org/html/2511.20837v1#S3.F19 "Figure 19 ‣ 3.5 Robustness with jumps ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets").

The network trained with high intensity λ=2\lambda=2 (Figure [20(b)](https://arxiv.org/html/2511.20837v1#S3.F20.sf2 "In Figure 20 ‣ 3.5 Robustness with jumps ‣ 3 Numerical results ‣ Constrained deep learning for pricing and hedging european options in incomplete markets")) is naturally more conservative. Its in-sample performance is somewhat worse than the λ=0.5\lambda=0.5 case (wider distribution), but it remains remarkably stable when tested on lower intensities, including the original jump-free world.

## 4 Conclusion

We modified the neural network to embed the terminal condition, particularly to handle non-smooth payoffs in incomplete markets, leveraging the self-financing property. For simple options, this approach significantly improved hedging performance, even for smooth payoffs, reducing the standard deviation of the P&L by up to 20%. For the exotic Equinox option, we explored two approaches: one separating the digital option component, using two simpler neural networks, and another using a single neural network. The single network approach proved more accurate, achieving a P&L standard deviation up to 10% lower when embedding the terminal condition. Robustness tests under a model with jumps further demonstrated the resilience of the Zero Target method, particularly when trained with moderate jump intensity, although performance declined under severe model misspecifications. Our approach advances the application of neural networks in quantitative finance by effectively addressing payoff non-smoothness and market incompleteness.

## Acknowledgments

Nicolas Baradel acknowledges the financial support provided by the *Fondation Natixis* and is grateful to Olivier Croissant, Michel Crouhy, Noureddine Lehdili, Nadhem Meziou, and Denis Talay for numerous fruitful discussions and insightful comments that significantly improved the paper.

## References

* [1]

  Nacira Agram, Bernt Øksendal, and Jan Rems.
  Deep learning for quadratic hedging in incomplete jump market.
  Digital Finance, 6(3):463–499, 2024.
* [2]

  Clémence Alasseur, Zakaria Bensaid, Roxana Dumitrescu, and Xavier Warin.
  Deep learning algorithms for fbsdes with jumps: applications to
  option pricing and a mfg model for smart grids.
  arXiv preprint arXiv:2401.03245, 2024.
* [3]

  Jens Berg and Kaj Nyström.
  A unified deep artificial neural network approach to partial
  differential equations in complex geometries.
  Neurocomputing, 317:28–41, 2018.
* [4]

  Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [5]

  Robert Culkin and Sanjiv R Das.
  Machine learning in finance: the case of deep learning for option
  pricing.
  Journal of Investment Management, 15(4):92–100, 2017.
* [6]

  Simon Fecamp, Joseph Mikael, and Xavier Warin.
  Deep learning for discrete-time hedging in incomplete markets.
  Journal of computational Finance, 25(2), 2020.
* [7]

  Igor Halperin.
  Qlbs: Q-learner in the black-scholes(-merton) worlds.
  The Journal of Derivatives, 28(1):99–122, 2020.
* [8]

  James M Hutchinson, Andrew W Lo, and Tomaso Poggio.
  A nonparametric approach to pricing and hedging derivative securities
  via learning networks.
  The journal of Finance, 49(3):851–889, 1994.
* [9]

  Diederik P. Kingma and Jimmy Ba.
  Adam: A method for stochastic optimization.
  Proceedings of the International Conference on Learning
  Representations (ICLR), 2015.
* [10]

  Zeyu Liu, Yantao Yang, and Qing-Dong Cai.
  Solving differential equation with constrained multilayer feedforward
  network.
  arXiv preprint arXiv:1904.06619, 2019.
* [11]

  Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang, Zachary
  DeVito, Zeming Lin, Alban Desmaison, Luca Antiga, and Adam Lerer.
  Automatic differentiation in pytorch.
  NIPS 2017 Autodiff Workshop, 2017.
  Presented at the NIPS 2017 Workshop on Automatic Differentiation.
* [12]

  Allan Pinkus.
  Approximation theory of the mlp model in neural networks.
  Acta numerica, 8:143–195, 1999.
* [13]

  Frank Rosenblatt.
  The perceptron: a probabilistic model for information storage and
  organization in the brain.
  Psychological review, 65(6):386, 1958.