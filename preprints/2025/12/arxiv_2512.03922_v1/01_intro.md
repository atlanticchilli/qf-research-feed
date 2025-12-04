---
authors:
- Julian Gutierrez
doc_id: arxiv:2512.03922v1
family_id: arxiv:2512.03922
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Co-evolutionary Approach for Heston Calibration
url_abs: http://arxiv.org/abs/2512.03922v1
url_html: https://arxiv.org/html/2512.03922v1
venue: arXiv q-fin
version: 1
year: 2025
---


Julian Gutierrez1
  
1Department of Mathematics, Dartmouth College, Hanover, NH, USA

(November 2025)

###### Abstract

We evaluate a co-evolutionary calibration framework for the Heston model in which a genetic algorithm (GA) over parameters is coupled to an evolving neural inverse map from option surfaces to parameters. While GA-history sampling can reduce training loss quickly and yields strong in-sample fits to the target surface, learning-curve diagnostics show a widening train–validation gap across generations, indicating substantial overfitting induced by the concentrated and less diverse dataset. In contrast, a broad, space-filling dataset generated via Latin hypercube sampling (LHS) achieves nearly comparable calibration accuracy while delivering markedly better out-of-sample stability across held-out surfaces. These results suggest that apparent improvements from co-evolutionary data generation largely reflect target-specific specialization rather than a more reliable global inverse mapping, and that maintaining dataset diversity is critical for robust amortized calibration.

Keywords: Heston model calibration, neuro-evolution, dataset, Latin Hypercube Sampling, Inverse neural surrogate

## 1 Introduction

Modern options trading and risk management require model calibration that is both accurate and fast. In production settings, parameters must be updated routinely—often daily and sometimes intraday—across many underlyings and maturities, under tight latency constraints. A calibration routine that is numerically fragile or too slow can negate the practical value of an otherwise expressive pricing model (BuchelEtAl2022; LiuEtAl2019).

The classical Black–Scholes framework (BlackScholes1973) remains foundational due to its analytical tractability and physical interpretability, yet its diffusion-only dynamics with constant volatility do not reproduce the systematic skew and curvature observed in implied-volatility surfaces. This empirical mismatch has motivated richer parametric models that capture these features, including stochastic volatility and jumps in returns Heston1993; CarrEtAl2002; HorvathEtAl2021.

Despite their improved fit, these models shift the central difficulty from pricing to calibration. Fitting a stochastic-volatility model entails solving a high-dimensional inverse problem that is typically nonconvex and computationally expensive, since each objective evaluation requires pricing an entire surface across strikes and maturities via numerical integration. As a result, calibration can become the dominant bottleneck in real-time pipelines (GilliSchumann2011; CuiEtAl2017; LiuEtAl2019).

Calibration is typically posed as minimizing the difference between market option quotes and model prices over a grid of strikes and maturities. For stochastic-volatility models—especially Heston-type specifications—this objective is generally nonconvex and exhibits multiple local minima, making optimizer choice consequential (GilliSchumann2011; OrtizEtAl2022; LiuEtAl2019). One class of approaches utilize global optimizers—simulated annealing, particle swarm optimization, differential evolution, and related evolutionary algorithms—which do not require derivatives and tend to be less sensitive to initialization (GilliSchumann2010; GilliSchumann2011; MugandaKasamani2023; HaringHochreiter2015). The drawback is computational: these methods often need a large number of iterations and objective evaluations, and the burden grows quickly with model dimension, which is problematic when calibrating multi-parameter dynamics to a full surface. A second strand uses gradient schemes, running a local optimizer from a set of initial points and selecting the best result; these can be substantially faster than global search when only a small number of starts is needed (CuiEtAl2017; OrtizEtAl2022). However, gradient-based methods often struggle because the objective is not smoothly differentiable or gradients are not readily available, so one must resort to finite-difference approximations that can be expensive and inaccurate. The Heston family is a representative case where both prices and sensitivities are often obtained through inverse-Fourier or other numerical integration procedures, so gradient computation can be noisy, and the integrands may become discontinuous or highly oscillatory for certain parameter combinations—precisely the regimes that can occur during search (CuiEtAl2017; ZhangEtAl2024).

Recent work has increasingly shifted toward machine-learning-based calibration to bypass several of these numerical difficulties. The common idea is to move expensive computation to an offline phase and deploy a learned mapping online: once a network is trained, inference is essentially instantaneous and can be executed at scale across many underlyings and surfaces. This amortized workflow is especially attractive in trading contexts because training can be performed before the market opens, while the calibrated parameters produced at runtime can be fed directly into pricing and risk systems with minimal latency (LiuEtAl2019; HorvathEtAl2021; BuchelEtAl2022). Moreover, neural surrogates can reduce reliance on fragile numerical derivatives by replacing—or serving as a warm-start for—gradient-based iterative solvers with a direct approximation of the inverse map from an observed surface to model parameters (LiuEtAl2019; ZhangEtAl2024).

A central practical question in these approaches is how to construct a training dataset that is both informative and efficient. A common strategy is to generate synthetic training examples by sampling the model’s parameter space using space-filling designs such as Latin hypercube sampling (LHS), pricing a large collection of surfaces, and training a network to learn the inverse mapping (LiuEtAl2019). While this is conceptually straightforward, it introduces an implicit modeling choice: it is not obvious which parameter ranges should be sampled, how wide the sampling domain should be, or whether it is preferable to concentrate samples near the market-relevant region rather than covering the parameter space broadly (HorvathEtAl2021). In other words, the success of amortized calibration depends not only on network architecture, but also on a prior over parameters encoded by the training distribution.

To investigate this trade-off, we introduce a dual-population co-evolutionary calibration framework that couples parameter search with neuro-evolution of an inverse mapping. At each generation, a genetic algorithm maintains a population of candidate parameter vectors and identifies an elite subset based on calibration error to the target market surface. The elite parameters are then used to generate model-implied option surfaces, and these elite (surface, parameter) pairs define the incremental training set for a simultaneously evolving population of neural networks. Each network implements an inverse map from a flattened option surface to the model parameter vector, and evolves both in weights and architecture through crossover and mutation operators. Network fitness is evaluated using a direct calibration score obtained by pricing the target surface using the network’s predicted parameters. The best-performing networks are then used to inject new candidate parameters into the GA population by evaluating the networks on the target surface and adding small perturbations to their predictions, replacing the weakest GA individuals. This establishes a closed feedback loop in which GA elites define the training signal for the inverse networks, and the inverse networks, in turn, provide targeted proposals that accelerate subsequent global search.

Empirically, this framework allows us to test the often unstated assumption that “sampling closer to the true parameters” yields a better inverse model than broad coverage. In our experiments, we find that inverse networks trained on LHS-generated datasets can outperform networks trained solely on GA-history datasets, indicating that diversity in parameter-space coverage is critical for learning a stable inverse map. We also find that NN-based seeding improves the convergence speed of the GA relative to a plain GA baseline, but this acceleration alone does not compensate for the loss in training diversity when the dataset is generated purely from optimizer history. These results suggest that while market-guided sampling is appealing, inverse calibration benefits from training distributions that remain sufficiently space-filling, and they motivate hybrid strategies that retain broad coverage while still leveraging optimizer feedback.

## 2 The Heston stochastic-volatility model

### 2.1 Risk-neutral dynamics and parameters

In the Heston model (Heston1993) we work under a risk-neutral measure ℚ\mathbb{Q} with constant risk-free rate rr. In the Heston model, the underlying price StS\_{t} and its instantaneous variance vtv\_{t} jointly evolve as a coupled diffusion with correlated Brownian shocks:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​St\displaystyle dS\_{t} | =r​St​d​t+vt​St​d​W1,t,\displaystyle=rS\_{t}\,dt+\sqrt{v\_{t}}\,S\_{t}\,dW\_{1,t}, |  | (1) |
|  | d​vt\displaystyle dv\_{t} | =κ​(λ−vt)​d​t+σ​vt​d​W2,t,\displaystyle=\kappa(\lambda-v\_{t})\,dt+\sigma\sqrt{v\_{t}}\,dW\_{2,t}, |  |
|  | 𝔼ℚ​[d​W1,t​d​W2,t]\displaystyle\mathbb{E}^{\mathbb{Q}}[dW\_{1,t}\,dW\_{2,t}] | =ρ​d​t.\displaystyle=\rho\,dt. |  |

The parameter vector governing the variance process is

|  |  |  |  |
| --- | --- | --- | --- |
|  | θH:=(κ,λ,σ,ρ,v0),\theta\_{H}:=(\kappa,\lambda,\sigma,\rho,v\_{0}), |  | (2) |

where κ>0\kappa>0 controls mean reversion, λ>0\lambda>0 is the long-run variance level, σ>0\sigma>0 is the vol-of-vol, ρ∈[−1,1]\rho\in[-1,1] is the return–variance correlation, and v0>0v\_{0}>0 is the initial variance.

A practical consideration (both for numerical stability and data generation) is to enforce constraints that keep the variance process well-behaved; a common sufficient condition for strict positivity is the Feller constraint 2​κ​λ>σ22\kappa\lambda>\sigma^{2} (CoxIngersollRoss1985; Feller1951).

### 2.2 Semi-analytical pricing via Fourier inversion

For calibration, we require fast evaluation of model prices across a grid of strikes and maturities. Heston admits a semi-analytical pricing expression for European calls based on Fourier inversion. Let τ\tau denote time to maturity and KK the strike, and define the full input tuple

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ:=(κ,λ,σ,ρ,v0,S0,r,τ,K).\theta:=(\kappa,\lambda,\sigma,\rho,v\_{0},S\_{0},r,\tau,K). |  | (3) |

Following ZhangEtAl2024 then the time-0 call price can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(θ)=S0​Π1−K​e−r​τ​Π2,C(\theta)=S\_{0}\Pi\_{1}-Ke^{-r\tau}\Pi\_{2}, |  | (4) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π1=12+1π​∫0∞ℜ⁡(φτ​(u−i)i​u​e−i​u​k)​𝑑u,Π2=12+1π​∫0∞ℜ⁡(φτ​(u)i​u​e−i​u​k)​𝑑u,\Pi\_{1}=\frac{1}{2}+\frac{1}{\pi}\int\_{0}^{\infty}\Re\!\left(\frac{\varphi\_{\tau}(u-i)}{iu}e^{-iuk}\right)\,du,\qquad\Pi\_{2}=\frac{1}{2}+\frac{1}{\pi}\int\_{0}^{\infty}\Re\!\left(\frac{\varphi\_{\tau}(u)}{iu}e^{-iuk}\right)\,du, |  | (5) |

where k=ln⁡Kk=\ln K and φτ​(u)\varphi\_{\tau}(u) is the characteristic function of ln⁡(Sτ)\ln(S\_{\tau}). Put prices follow immediately from put–call parity.

Because calibrations repeatedly evaluate these integrals, the specific characteristic-function representation matters: formulas can suffer from branch-cut instabilities due to complex logarithms. A numerically stable specification is

|  |  |  |  |
| --- | --- | --- | --- |
|  | φτ​(u)=exp⁡(Cτ​(u)+Dτ​(u)​v0+i​u​ln⁡S0),\varphi\_{\tau}(u)=\exp\!\big(C\_{\tau}(u)+D\_{\tau}(u)\,v\_{0}+iu\ln S\_{0}\big), |  | (6) |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Cτ​(u)\displaystyle C\_{\tau}(u) | =i​r​u​τ+κ​λσ2​((κ−i​ρ​σ​u−d​(u))​τ−2​ln⁡(1−g​(u)​e−d​(u)​τ1−g​(u))),\displaystyle=iru\tau+\frac{\kappa\lambda}{\sigma^{2}}\left((\kappa-i\rho\sigma u-d(u))\tau-2\ln\!\left(\frac{1-g(u)e^{-d(u)\tau}}{1-g(u)}\right)\right), |  | (7) |
|  | Dτ​(u)\displaystyle D\_{\tau}(u) | =κ−i​ρ​σ​u−d​(u)σ2​(1−e−d​(u)​τ1−g​(u)​e−d​(u)​τ),\displaystyle=\frac{\kappa-i\rho\sigma u-d(u)}{\sigma^{2}}\left(\frac{1-e^{-d(u)\tau}}{1-g(u)e^{-d(u)\tau}}\right), |  |
|  | g​(u)\displaystyle g(u) | =κ−i​ρ​σ​u−d​(u)κ−i​ρ​σ​u+d​(u),d​(u)=(κ−i​ρ​σ​u)2+σ2​(i​u+u2).\displaystyle=\frac{\kappa-i\rho\sigma u-d(u)}{\kappa-i\rho\sigma u+d(u)},\qquad d(u)=\sqrt{(\kappa-i\rho\sigma u)^{2}+\sigma^{2}(iu+u^{2})}. |  |

### 2.3 Calibration objective

Given market quotes over a strike–maturity grid {(Km,τm)}m=1M\{(K\_{m},\tau\_{m})\}\_{m=1}^{M}, calibration is posed as an inverse problem: find θH\theta\_{H} minimizing a pricing-misfit objective, typically least squares over observed prices,

|  |  |  |  |
| --- | --- | --- | --- |
|  | θH⋆∈arg⁡minθH∈ΘH⁡1M​∑m=1M(C​(θH;S0,r,τm,Km)−Cmmkt)2,\theta\_{H}^{\star}\in\arg\min\_{\theta\_{H}\in\Theta\_{H}}\frac{1}{M}\sum\_{m=1}^{M}\Big(C(\theta\_{H};S\_{0},r,\tau\_{m},K\_{m})-C^{\text{mkt}}\_{m}\Big)^{2}, |  | (8) |

subject to our feasibility constraints.

## 3 Co-evolutionary approach

Our calibration method couples a global parameter search with an evolving inverse map from option surfaces to Heston parameters. The algorithm maintains two populations that interact through a feedback loop: (i) a genetic algorithm (GA) over Heston parameter vectors and (ii) a population of neural networks trained and evolved to predict parameters from a target surface.

### 3.1 Population structure

At generation gg, the GA population is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫GA(g)={θ1(g),θ2(g),…,θN(g)},θn(g)∈ℝ5,\mathcal{P}\_{\mathrm{GA}}^{(g)}=\{\theta\_{1}^{(g)},\theta\_{2}^{(g)},\dots,\theta\_{N}^{(g)}\},\qquad\theta\_{n}^{(g)}\in\mathbb{R}^{5}, |  | (9) |

where θ=(κ,λ,σ,ρ,v0)\theta=(\kappa,\lambda,\sigma,\rho,v\_{0}) denotes the Heston parameter vector. In parallel, we maintain a neural population

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫NN(g)={NN1(g),NN2(g),…,NNM(g)}.\mathcal{P}\_{\mathrm{NN}}^{(g)}=\{\mathrm{NN}\_{1}^{(g)},\mathrm{NN}\_{2}^{(g)},\dots,\mathrm{NN}\_{M}^{(g)}\}. |  | (10) |

Each network implements an inverse mapping

|  |  |  |  |
| --- | --- | --- | --- |
|  | fi:ℝK​T→Θ,Θ⊂ℝ5,f\_{i}:\mathbb{R}^{KT}\to\Theta,\qquad\Theta\subset\mathbb{R}^{5}, |  | (11) |

taking as input a flattened option-price surface on a K×TK\times T strike–maturity grid and outputting a parameter proposal in Θ\Theta, the feasible Heston parameter space.

The GA population 𝒫GA(g)\mathcal{P}\_{\mathrm{GA}}^{(g)} is advanced by elitist selection followed by variation in the feasible parameter space Θ\Theta. In each generation, the top fraction εGA\varepsilon\_{\mathrm{GA}} of parameter vectors are retained and forms the parent pool for reproduction. Offspring are generated by selecting two parents from this elite pool, applying crossover, and then applying mutation.

Table 1: Genetic-algorithm operators for Heston parameter evolution.

Operator
Probability
Choice set / rule
Constraint


Selection (elitism)
—
Preserve the top εGA\varepsilon\_{\mathrm{GA}} fraction by fitness
εGA∈(0,1)\varepsilon\_{\mathrm{GA}}\in(0,1).

Crossover (arithmetic)
px,GAp\_{\mathrm{x,GA}}
Select θp​1,θp​2\theta\_{p1},\theta\_{p2} from the elite pool and set
θchild=12​(θp​1+θp​2)\theta\_{\text{child}}=\tfrac{1}{2}(\theta\_{p1}+\theta\_{p2}).
Parents drawn from elites.

Mutation (Gaussian)
pm,GAp\_{\mathrm{m,GA}}
Perturb θ\theta as θ′=θ+ξ\theta^{\prime}=\theta+\xi, ξ∼𝒩​(0,σmut2​I)\xi\sim\mathcal{N}(0,\sigma\_{\mathrm{mut}}^{2}I).
Enforce θ′∈Θ\theta^{\prime}\in\Theta after mutation.

### 3.2 Network representation and variation

Each network NNi\mathrm{NN}\_{i} is defined by an architecture and its weights. We encode the architecture as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai=(Li,Hi,αi),A\_{i}=(L\_{i},H\_{i},\alpha\_{i}), |  | (12) |

where LiL\_{i} is the number of hidden layers, Hi=(hi,1,…,hi,Li)H\_{i}=(h\_{i,1},\dots,h\_{i,L\_{i}}) are hidden widths, and αi\alpha\_{i} is the activation type. The trainable parameters are

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi={(Wℓ,bℓ)}ℓ=1Li+1,W\_{i}=\{(W\_{\ell},b\_{\ell})\}\_{\ell=1}^{L\_{i}+1}, |  | (13) |

where WℓW\_{\ell} and bℓb\_{\ell} denote the weight matrix and bias vector of layer ℓ\ell. Let d0=K​Td\_{0}=KT be the input dimension, let dℓ=hi,ℓd\_{\ell}=h\_{i,\ell} for ℓ=1,…,Li\ell=1,\dots,L\_{i} be the hidden widths, and let dLi+1=5d\_{L\_{i}+1}=5 be the output dimension. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wℓ∈ℝdℓ×dℓ−1,bℓ∈ℝdℓ,ℓ=1,…,Li+1.W\_{\ell}\in\mathbb{R}^{d\_{\ell}\times d\_{\ell-1}},\qquad b\_{\ell}\in\mathbb{R}^{d\_{\ell}},\qquad\ell=1,\dots,L\_{i}+1. |  | (14) |

Networks evolve through (i) continuous variation of weights and (ii) occasional architecture changes. For weight evolution, we use arithmetic crossover and Gaussian mutation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wchild=12​(Wp​1+Wp​2),W′=W+Δ​W,Δ​W∼𝒩​(0,σw2​I).W\_{\text{child}}=\tfrac{1}{2}(W\_{p1}+W\_{p2}),\qquad W^{\prime}=W+\Delta W,\ \ \Delta W\sim\mathcal{N}(0,\sigma\_{\mathrm{w}}^{2}I). |  | (15) |

Table 2: Neural-network architecture search space and mutation operators.

Operator
Probability
Choice set / rule
Constraint


Add hidden layer
paddp\_{\mathrm{add}}
hnew∈{32,64,128,256}h\_{\text{new}}\in\{32,64,128,256\}
inserted if feasible

Remove hidden layer
prmp\_{\mathrm{rm}}
remove a randomly chosen layer
requires Li>1L\_{i}>1

Modify layer width
pmodp\_{\mathrm{mod}}
hi,ℓ←hnew,hnew∈{16,32,64,128,256,512}h\_{i,\ell}\leftarrow h\_{\text{new}},\ h\_{\text{new}}\in\{16,32,64,128,256,512\}
any ℓ∈{1,…,Li}\ell\in\{1,\dots,L\_{i}\}

Change activation
pαp\_{\alpha}
αi←αnew,αnew∈{ReLU,Tanh,LeakyReLU,ELU}\alpha\_{i}\leftarrow\alpha\_{\text{new}},\ \alpha\_{\text{new}}\in\{\mathrm{ReLU},\mathrm{Tanh},\mathrm{LeakyReLU},\mathrm{ELU}\}
—

Architecture crossover
—
Lchild=max⁡(Lp​1,Lp​2)L\_{\text{child}}=\max(L\_{p1},L\_{p2})
hybridize widths/activation

When two parents have incompatible depth/width, we construct a hybrid offspring by taking

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lchild=max⁡(Lp​1,Lp​2),hℓ,child=⌊hℓ,p​1+hℓ,p​22⌋,L\_{\text{child}}=\max(L\_{p1},L\_{p2}),\qquad h\_{\ell,\text{child}}=\left\lfloor\frac{h\_{\ell,p1}+h\_{\ell,p2}}{2}\right\rfloor, |  | (16) |

and selecting the child’s activation function, αchild\alpha\_{\text{child}}, uniformly from the parents’ activations.

### 3.3 Feedback loop: data generation, training, and injection

Let ℰg⊂{1,…,N}\mathcal{E}\_{g}\subset\{1,\dots,N\} denote the elite GA indices at generation gg by calibration error against the target market surface). For each elite θj(g)\theta\_{j}^{(g)}, we compute the corresponding model-implied option surface S​(θj(g))S(\theta\_{j}^{(g)}), flatten it to sj(g)=flat​(S​(θj(g)))∈ℝK​Ts\_{j}^{(g)}=\mathrm{flat}(S(\theta\_{j}^{(g)}))\in\mathbb{R}^{KT}, and form the incremental dataset

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟g={(sj(g),θj(g)):j∈ℰg}.\mathcal{D}\_{g}=\{(s\_{j}^{(g)},\theta\_{j}^{(g)}):j\in\mathcal{E}\_{g}\}. |  | (17) |

Each network is updated on 𝒟g\mathcal{D}\_{g} using a squared-error objective,

|  |  |  |  |
| --- | --- | --- | --- |
|  | minWi​∑(s,θ)∈𝒟g‖NNi​(s;Wi)−θ‖22,\min\_{W\_{i}}\ \sum\_{(s,\theta)\in\mathcal{D}\_{g}}\left\|\mathrm{NN}\_{i}(s;W\_{i})-\theta\right\|\_{2}^{2}, |  | (18) |

implemented via a fixed number of gradient steps per generation.

Network fitness is assessed using (i) this surrogate prediction loss on 𝒟g\mathcal{D}\_{g} and (ii) a direct calibration score on the target surface. Specifically, given the observed target surface StargetS\_{\text{target}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^i=NNi​(flat​(Starget)),\hat{\theta}\_{i}=\mathrm{NN}\_{i}(\mathrm{flat}(S\_{\text{target}})), |  | (19) |

and the direct score is the calibration loss obtained by pricing with θ^i\hat{\theta}\_{i} and comparing to the target grid under the same metric used for GA evaluation.

Finally, the best-performing networks propose new GA candidates by evaluating the target surface and adding exploration noise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θinject=θ^i+ζ,ζ∼𝒩​(0,σinj2​I).\theta\_{\text{inject}}=\hat{\theta}\_{i}+\zeta,\qquad\zeta\sim\mathcal{N}(0,\sigma\_{\text{inj}}^{2}I). |  | (20) |

These injected candidates replace the weakest GA individuals, while the remainder of the GA population is advanced by standard elitist selection, arithmetic crossover, and Gaussian mutation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | θchild=12​(θp​1+θp​2),θ′=θ+ξ,ξ∼𝒩​(0,σmut2​I).\theta\_{\text{child}}=\tfrac{1}{2}(\theta\_{p1}+\theta\_{p2}),\qquad\theta^{\prime}=\theta+\xi,\ \ \xi\sim\mathcal{N}(0,\sigma\_{\mathrm{mut}}^{2}I). |  | (21) |

GA elites generate training signal for the inverse networks, and the networks return targeted proposals that accelerate subsequent global search.

![Refer to caption](top.png)

![Refer to caption](bottom.png)

Figure 1: Overview of the co-evolutionary calibration loop. A population of neural networks is trained and evolved using surfaces generated by elite GA candidates; top networks then propose parameter seeds that are injected into the GA, accelerating subsequent parameter evolution. The process repeats for a fixed number of generations.

## 4 Empirical results

We first evaluate the proposed co-evolutionary calibration method in a fully controlled synthetic setting, where the ground-truth Heston parameters are known and performance can be measured directly. The goals of these experiments are (i) to compare convergence behavior against a plain genetic algorithm baseline under a fixed compute budget, (ii) to quantify time-to-accuracy relative to a common local optimizer (LBFGS), and (iii) to test how the induced training-data distribution affects the performance and generalization of the learned inverse map. In particular, we compare inverse networks trained on (a) the concentrated dataset produced by the co-evolutionary loop and (b) a broad space-filling dataset generated via Latin hypercube sampling (LHS), isolating the role of dataset diversity versus target-focused sampling.

### 4.1 Experimental design and synthetic data generation

Synthetic option price surfaces are generated by first sampling a parameter vector
θ⋆=(κ,λ,σ,ρ,v0)\theta^{\star}=(\kappa,\lambda,\sigma,\rho,v\_{0}) at random from the feasible Heston parameter space Θ⊂ℝ5\Theta\subset\mathbb{R}^{5}. For each sampled θ⋆\theta^{\star}, we price European options on a fixed strike–maturity grid of size K×TK\times T using the semi-analytical Heston pricing engine described in Section 2, producing a surface
S​(θ⋆)∈ℝK×TS(\theta^{\star})\in\mathbb{R}^{K\times T}. The corresponding flattened representation
s⋆=flat​(S​(θ⋆))∈ℝK​Ts^{\star}=\mathrm{flat}(S(\theta^{\star}))\in\mathbb{R}^{KT} serves as the observation provided to inverse networks and as the target surface for calibration.

Table 3: Ranges of the Heston model parameters in Eq. (1), values come from ZhangEtAl2024

| Parameter | Range |
| --- | --- |
| κ\kappa | [ 0.005, 5][\,0.005,\ 5\,] |
| λ\lambda | [ 0, 1][\,0,\ 1\,] |
| σ\sigma | [ 0.1, 1][\,0.1,\ 1\,] |
| ρ\rho | [−0.95, 0][\,-0.95,\ 0\,] |
| v0v\_{0} | [ 0, 1][\,0,\ 1\,] |
| rr | [ 0, 0.10][\,0,\ 0.10\,] |
| τ\tau | [ 0.05, 1][\,0.05,\ 1\,] |

### 4.2 Hyperparameters

The synthetic experiments use fixed hyperparameters across all trials to isolate the effect of the proposed seeding mechanism. We group settings by (i) GA evolution of θ\theta-candidates, (ii) neuro-evolution, and (iii) neural-network training.

Table 4: Hyperparameters used in the synthetic experiments by component.

Component
Hyperparameter
Value
Notes

Genetic algorithm (GA)


NN
50
Number of θ\theta-candidates per generation.


GG
10
Same budget for GA and co-evolutionary runs.


εGA\varepsilon\_{\mathrm{GA}}
0.2
Defines elite parent pool used for crossover.


μGA\mu\_{\mathrm{GA}}
0.1
Per-parameter mutation probability.


px,GAp\_{\mathrm{x,GA}}
0.3


pm,GAp\_{\mathrm{m,GA}}
0.2


σmut\sigma\_{\mathrm{mut}}
0.05×0.05\times range
Gaussian noise scale as a fraction of each parameter’s box range.

Neuro-evolution (NN population + GA seeding)


MM
20
Number of networks evolved in parallel.


εNN\varepsilon\_{\mathrm{NN}}
0.2
Survival fraction in the NN population.


εinj\varepsilon\_{\mathrm{inj}}
0.2
Fraction of GA population replaced by NN-proposed seeds.


μw\mu\_{\mathrm{w}}
0.1
Probability of perturbing each weight.


σw\sigma\_{\mathrm{w}}
0.02
Std. dev. of Gaussian weight perturbations.


σinj\sigma\_{\mathrm{inj}}
0.01
Noise added to NN parameter predictions before injection.


parchp\_{\mathrm{arch}}
0.05


prmp\_{\mathrm{rm}}
0.3


paddp\_{\mathrm{add}}
0.3


pmodp\_{\mathrm{mod}}
0.5


pαp\_{\alpha}
0.2

Neural-network training (per-generation updates)


Optimization algorithm
Adam


Epochs per generation
5
Adam steps on the current training set.


Initial learning rate
0.001


Decay rate
0.9


Loss
MSE
Parameter-space regression loss.


Feedback epochs
2
Retraining on the latest GA-elite data.


Feedback frequency
1
Retrain every generation.


Training/Test set ratio
7:3


Batch size
64

### 4.3 Results

#### 4.3.1 Convergence comparison

We first compare convergence behavior on synthetic surfaces. We plot the calibration loss (RMSE) as a function of generation for (i) a plain GA evolving θ\theta-candidates directly and (ii) the proposed co-evolutionary method, in which the NN population proposes parameter seeds that are injected into the GA. The co-evolutionary curve descends more rapidly in the early generations and continues improving after the plain GA begins to plateau. This indicates that NN-driven injections provide informative proposals that accelerate global search and help sustain progress over a longer horizon under the same evolutionary budget.

![Refer to caption](ga.png)


Figure 2: Convergence on synthetic calibration targets. Calibration RMSE versus generation for a plain genetic algorithm (GA) baseline and the proposed co-evolutionary method (GA + parameter & architecture neuro-evolution). Under the same compute budget, the co-evolutionary method reduces error more quickly in early generations and continues improving after the GA plateaus, consistent with NN-based seeding accelerating and stabilizing the global search.

#### 4.3.2 Time to convergence distribution

To benchmark against a representative gradient-based local method, we additionally compare our evolutionary approach to LBFGS. For each synthetic target, we run LBFGS under the same pricing objective to obtain a reference calibration error level. We then define the *time-to-threshold* (TTT) as the smallest GA generation gg at which the evolutionary method first achieves an error no worse than this LBFGS reference. Repeating this procedure across nn independent synthetic targets yields a distribution of TTT values, which summarizes how many evolutionary generations are typically required to match the accuracy of a standard gradient routine.

![Refer to caption](time_to_threshold_violin.png)


Figure 3: Time-to-threshold relative to LBFGS on synthetic targets. The reported time-to-threshold is the first GA generation at which the evolutionary method matches that reference level RMSE. The distribution over n=20n=20 trials indicates that matching LBFGS-level accuracy typically requires around 264 generations to match the perforamnce of LBFGS.




Table 5: Summary of neural-architecture statistics over training generations. Reported values are computed over the NN population at each checkpoint.

Generation
Avg layers
Avg nodes
Std nodes
Min nodes
Max nodes
Most common arch.
Frequency
Primary act.
Act. div.


20
1.95
192.0
56.3
32
384
[128,64][128,64]
17/20
ReLU
2

40
1.95
179.2
37.0
64
256
[128,64][128,64]
14/20
ReLU
1

60
2.10
184.0
52.5
64
320
[128,64][128,64]
11/20
ReLU
2

80
2.05
188.8
75.0
64
320
[128,64][128,64]
9/20
ReLU
4

100
2.15
208.0
78.7
64
384
[128,64][128,64]
6/20
ReLU
3

The architecture-summary table suggests that the evolutionary pressure is not only shrinking loss but also gradually favoring higher-capacity models. The average depth increases from 1.95 layers at generation 20 to 2.15 layers by generation 100, alongside an increase in average total nodes from 192 to 208 and a rising spread in node counts (Std Nodes from 56.3 to 78.7, with Max Nodes returning to 384). At the same time, the initially dominant architecture
[128,64]
[128,64] becomes less ubiquitous (frequency declines from 17/20 to 6/20) and activation diversity increases from 1–2 up to 3–4, indicating a broader exploration of architectural variants later in evolution. Taken together, these trends are consistent with a slow drift toward deeper, more expressive networks as the incremental dataset grows, while the population becomes less concentrated around a single “default” design.

Table 6: Representative evolved architectures at generation 20.

| NN ID | Architecture | Num layers | Total nodes | Activation |
| --- | --- | --- | --- | --- |
| NN-1 | [128,64][128,64] | 2 | 192 | ReLU |
| NN-2 | [256,128][256,128] | 2 | 384 | ReLU |
| NN-3 | [32][32] | 1 | 32 | ELU |
| NN-4 | [32,128][32,128] | 2 | 160 | ELU |
| NN-5 | [64,32,32][64,32,32] | 3 | 128 | ReLU |




Table 7: Representative evolved architectures at generation 40.

| NN ID | Architecture | Num layers | Total nodes | Activation |
| --- | --- | --- | --- | --- |
| NN-1 | [128,64][128,64] | 2 | 192 | ReLU |
| NN-2 | [64,64][64,64] | 2 | 128 | ReLU |
| NN-3 | [64][64] | 1 | 64 | ReLU |
| NN-4 | [128,32][128,32] | 2 | 160 | ReLU |
| NN-5 | [32,128][32,128] | 2 | 160 | ReLU |




Table 8: Representative evolved architectures at generation 60.

| NN ID | Architecture | Num layers | Total nodes | Activation |
| --- | --- | --- | --- | --- |
| NN-1 | [128,64][128,64] | 2 | 192 | ReLU |
| NN-2 | [256][256] | 1 | 256 | ReLU |
| NN-3 | [64,32,128][64,32,128] | 3 | 224 | ReLU |
| NN-4 | [64][64] | 1 | 64 | Tanh |
| NN-5 | [32,128][32,128] | 2 | 160 | ReLU |




Table 9: Representative evolved architectures at generation 80.

| NN ID | Architecture | Num layers | Total nodes | Activation |
| --- | --- | --- | --- | --- |
| NN-1 | [128,64][128,64] | 2 | 192 | ReLU |
| NN-2 | [64,32][64,32] | 2 | 96 | ReLU |
| NN-3 | [64,256][64,256] | 2 | 320 | ReLU |
| NN-4 | [64,64][64,64] | 2 | 128 | ReLU |
| NN-5 | [128,64,64][128,64,64] | 3 | 256 | ReLU |




Table 10: Representative evolved architectures at generation 100.

| NN ID | Architecture | Num layers | Total nodes | Activation |
| --- | --- | --- | --- | --- |
| NN-1 | [128,64][128,64] | 2 | 192 | ReLU |
| NN-2 | [64,64][64,64] | 2 | 128 | ReLU |
| NN-3 | [128,32,32][128,32,32] | 3 | 192 | ReLU |
| NN-4 | [128,128,32][128,128,32] | 3 | 288 | ReLU |
| NN-5 | [128][128] | 1 | 128 | ReLU |

#### 4.3.3 Neural network improvement over generations

As the co-evolutionary loop progresses, the neural population is repeatedly retrained on an expanding set of GA-elite surface–parameter pairs, while its architecture is simultaneously perturbed by the mutation operators described in Section 3. This produces a moving target for learning: the dataset grows and shifts toward market-relevant regions, and the hypothesis class changes as depth, width, and activations evolve. To assess training quality across this process, we track the learning curves of representative networks at several generation checkpoints. The figure below reports the training and validation MSE as a function of epoch for checkpoints at generations 20, 40, 60, 80, and 100, illustrating how optimization dynamics and generalization behavior change as both the data stream and the architecture distribution evolve.

![Refer to caption](nn_loss_across_generations.png)


Figure 4: Neural-network training quality across co-evolution. Training (left) and validation (right) MSE learning curves for checkpoint generations g∈{20,40,60,80,100}g\in\{20,40,60,80,100\}. Curves reflect the combined effect of (i) an expanding GA-elite dataset and (ii) evolving NN architectures over generations.

#### 4.3.4 Overfitting analysis

As the neural population accumulates additional GA-elite training pairs across generations, the training curves exhibit a clear downward shift in loss, while the corresponding validation curves improve much more slowly and remain materially higher. This widening train–validation gap is consistent with the inverse networks becoming increasingly specialized to the narrow region of parameter space emphasized by optimizer history, rather than learning an inverse map that generalizes across held-out surfaces. In other words, the same feedback loop that produces highly relevant training examples for seeding can also concentrate the data distribution, making it easier to reduce training error while providing limited coverage for out-of-sample validation—a pattern that motivates our subsequent overfitting analysis and the comparison against space-filling datasets.

![Refer to caption](seed.png)

![Refer to caption](no_seed.png)

Figure 5: Training/validation loss for inverse networks trained on a space-filling LHS dataset versus GA-history data. Top: seeding/warm-start enabled. Bottom: seeding disabled. In both settings, GA-history sampling yields low training loss but substantially higher validation loss, consistent with overfitting to the target surface induced by a concentrated and less diverse training distribution. LHS sampling, while not concentrated near the target, learns a more stable inverse mapping with improved generalization across held-out surfaces.

#### 4.3.5 Real-surface calibration and LHS dataset comparison

We next calibrate to an SPX option price surface, using the S&P 500 index as the underlying (data from Yahoo Finance). This real-surface calibration provides the target surface used by the co-evolutionary loop, after which we compare two training-set constructions for the inverse network: (i) GA-history data collected from optimizer elites and (ii) a broad, space-filling dataset generated via Latin hypercube sampling, which isolates the effect of dataset diversity on generalization. In the LHS setting, we sample parameter vectors uniformly in the prescribed bounds and generate their corresponding model-implied surfaces under the same pricing engine and grid used throughout.

Table 11: SPX real-surface calibration progress and parameter error over generations. Parameter columns report relative error (%) for the co-evolutionary method.

Generation
Loss
κ\kappa (%)
λ\lambda (%)
σ\sigma (%)
ρ\rho (%)
v0v\_{0} (%)


20
0.000298
400.607415
42.589554
17.772964
27.881316
25.709461

40
0.000207
285.404704
38.461205
17.889609
27.070596
26.622294

60
0.000139
153.712397
34.734711
21.746060
25.347386
16.781899

80
0.000113
115.876770
31.543873
22.323575
24.976307
 6.892037

100
0.000083
 58.191643
27.517073
22.514355
24.685334
 6.235404




Table 12: U.S. Treasury rates used for the risk-free curve (weekly maturities).

| Maturity (weeks) | Rate (%) |
| --- | --- |
| 4 | 4.24 |
| 6 | 4.23 |
| 13 | 4.23 |
| 17 | 4.19 |
| 26 | 4.07 |
| 52 | 3.77 |




Table 13: Summary statistics for the SPX option sample used in the real-surface experiments.

| Ticker | # samples | Maturity (days) | Moneyness ln⁡(K/S0)\ln(K/S\_{0}) |
| --- | --- | --- | --- |
| SPX | 152 | [3, 255] | [-3.31, 0.774] |

Our final synthetic-data finding carries over to real-surface calibration: when the inverse network is trained primarily on GA-history data generated from the SPX target surface, it can produce parameter proposals whose implied prices track that same surface very closely. The figure below illustrates this effect for a representative strike slice: the co-evolutionary model-implied call prices align more tightly with market prices than the LHS-trained inverse model. However, given the earlier train–validation gap and the concentrated nature of optimizer-history sampling, this improvement is best interpreted as target-specific fitting rather than evidence of a uniformly better inverse mapping. In other words, GA-history training can yield superior in-sample replication of the target surface while sacrificing robustness away from that surface, whereas LHS provides broader coverage that typically improves out-of-sample stability.

![Refer to caption](lhs.png)


Figure 6: Representative strike slice for SPX call prices comparing market quotes to model-implied prices produced by inverse networks trained with GA-history (co-evolutionary) data versus a space-filling LHS dataset.

## 5 Conclusion

We proposed a dual-population co-evolutionary calibration framework for Heston in which a GA performs global parameter search while an evolving neural population learns an inverse mapping from option surfaces to parameters and provides warm-start seeds. Empirically, NN-driven injection accelerates GA convergence and sustains improvements beyond the point where a plain GA begins to plateau, and time-to-threshold experiments show that the evolutionary approach can reach LBFGS-level accuracy under the same pricing objective. At the same time, training inverse models exclusively on GA-history surfaces induces a concentrated data distribution and a widening train–validation gap, indicating overfitting to the target region. Comparisons against space-filling LHS datasets confirm that broader parameter-space coverage yields more stable and generalizable inverse mappings, even if it samples away from the target. In SPX calibration, GA-history-trained networks can reproduce the target surface more closely. However, due to the overfitting induced by optimizer-history sampling and the inherent ill-conditioning of Heston calibration, even small perturbations in the observed surface can map to parameter vectors far outside the training distribution, indicating that the apparent gains reflect target-specific fitting rather than a genuine improvement in learning a robust inverse mapping.