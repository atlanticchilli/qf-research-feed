---
authors:
- Ali Atiah Alzahrani
doc_id: arxiv:2510.10728v1
family_id: arxiv:2510.10728
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization
url_abs: http://arxiv.org/abs/2510.10728v1
url_html: https://arxiv.org/html/2510.10728v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ali Atiah Alzahrani
Public Investment Fund (PIF)†RiyadhSaudi Arabia

###### Abstract.

We study high-dimensional path-dependent problems in quantitative finance and present a deep BSDE/2BSDE solver that couples truncated log-signatures with a Neural RDE backbone, aligning stochastic analysis with modern sequence-to-path learning. A CVaR-tilted terminal objective improves left-tail calibration, and an optional second-order (2BSDE) head supplies curvature information for risk-sensitive stochastic control. Across Asian and barrier pricing and portfolio control, the solver improves accuracy, tail fidelity, and stability at comparable budgets; for example, at d=200d=200 it attains CVaR0.99=9.80%\mathrm{CVaR}\_{0.99}=9.80\% versus 12.00−13.10%12.00\!-\!13.10\% for strong baselines, and achieves the lowest HJB residual (0.011)(0.011) with the lowest ∥Z∥\lVert Z\rVert/∥Γ∥\lVert\Gamma\rVert RMSEs. These results realize the workshop’s “two-way bridge”: stochastic tools inform representations and losses, while AI methods expand solvable financial models at scale.

Path-dependent PDEs, BSDE and 2BSDE/HJB, log-signature features, Neural CDE/RDE, Malliavin weights, CVaR-tilted training, Asian/barrier options, portfolio control.

††copyright: none††conference: ACM International Conference on AI in Finance; 2025; Singapore††booktitle: Proceedings of the ACM International Conference on AI in Finance (ICAIF ’25)††journalyear: 202511footnotetext: Corresponding author: alialzahrani@pif.gov.sa22footnotetext: The views expressed are those of the authors and do not
necessarily reflect the views of the Public Investment Fund (PIF). This
material is for research purposes only and does not constitute investment advice.33footnotetext: Code: <https://github.com/AliAtiah/SigRDE>.

## 1. Introduction

Deep learning has unlocked high-dimensional solvers for semilinear parabolic PDEs via the BSDE representation (Han et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib17)), with subsequent advances in local-in-time training (DBDP) (Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19), [2020](https://arxiv.org/html/2510.10728v1#bib.bib20)), variance-reduced operator splitting (Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2), [2021](https://arxiv.org/html/2510.10728v1#bib.bib3)), and fully nonlinear formulations through 2BSDEs (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)). Yet many problems of practical interest in quantitative finance are *path-dependent*—from Asian and barrier features to history-aware portfolio control—so the value functional u​(t,X⋅⁣≤t)u(t,X\_{\cdot\leq t}) depends on the entire trajectory. Functional Itô calculus and PPDE theory formalize this non-Markovian setting and its link to BSDEs (Dupire, [2019](https://arxiv.org/html/2510.10728v1#bib.bib10); Cont and Fournié, [2013](https://arxiv.org/html/2510.10728v1#bib.bib9); Ekren et al., [2011](https://arxiv.org/html/2510.10728v1#bib.bib11)), but neural solvers often struggle to encode long-range path information without exploding parameters or memory. We address this gap with a specialized deep BSDE architecture that couples truncated log-signature encoders with a Neural Rough Differential Equation (Neural RDE) backbone for (Yt,Zt)(Y\_{t},Z\_{t}): signatures provide a principled, hierarchical summary of paths as iterated integrals (Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13)), while Neural CDE/RDE models evolve hidden states in continuous time with adjoint memory and stable long-horizon gradients (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24); Fang et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib12)). This pairing directly targets the information bottleneck in path dependence, retains Monte-Carlo flexibility, and integrates naturally with finance-specific enhancements: a *risk-sensitive* BSDE objective (CVaR-tilted terminal mismatch) to improve left-tail calibration, and a 2BSDE-compatible second-order head for HJB-type control where we systematically compare *Malliavin* versus *autograd* Hessian estimators under identical time discretizations (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)). Our evaluation plan centers on high-dimensional path-dependent pricing (e.g., Asian options) and stochastic-volatility portfolio control, reporting absolute/relative error, runtime, peak memory, and seed-level confidence intervals, alongside ablations on signature depth, RDE vector-field width, multistep depth, and Γ\Gamma estimation. In line with the workshop’s *two-way dialogue*, stochastic analysis informs the design of representations, losses, and estimators, while modern deep sequence-to-path models extend the frontier of solvable financial models to d≫1d\!\gg\!1 with improved stability and tail fidelity (Han et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib17); Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19); Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2), [b](https://arxiv.org/html/2510.10728v1#bib.bib4); Dupire, [2019](https://arxiv.org/html/2510.10728v1#bib.bib10); Cont and Fournié, [2013](https://arxiv.org/html/2510.10728v1#bib.bib9); Fang et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib12)).

## 2. Background and Related Work

High–dimensional BSDE/PDE solvers.
Deep neural solvers for semilinear parabolic PDEs via BSDEs have progressed from global end-to-end training (Han et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib17)) to variance- and stability-focused schemes such as DBDP (local-in-time windows with analysis and error bounds) (Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19), [2020](https://arxiv.org/html/2510.10728v1#bib.bib20)) and Deep Splitting (operator decomposition) (Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2), [2021](https://arxiv.org/html/2510.10728v1#bib.bib3)). In parallel, mesh-free solvers like DGM (Sirignano and Spiliopoulos, [2018](https://arxiv.org/html/2510.10728v1#bib.bib30)) and PINNs (Raissi et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib26)) introduced residual minimization perspectives that complement BSDE training. For fully nonlinear problems, second-order BSDEs (2BSDEs) provide a probabilistic representation of HJB equations (Soner et al., [2012](https://arxiv.org/html/2510.10728v1#bib.bib31)); neural instantiations combine BSDE heads with second-order structure and physics penalties (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)). Alternative Monte-Carlo lines—regression-based BSDEs (Gobet et al., [2005](https://arxiv.org/html/2510.10728v1#bib.bib16); Bouchard and Touzi, [2004](https://arxiv.org/html/2510.10728v1#bib.bib6)) and branching-diffusion representations for semilinear PDEs (Henry-Labordère et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib18))—further illuminate the variance/bias trade-offs that modern deep BSDE pipelines must control.

Path dependence and PPDEs.
Path dependence arises when the value functional depends on the entire history X⋅⁣≤tX\_{\cdot\leq t}. Functional Itô calculus and viscosity solutions for PPDEs formalize this non-Markovian regime and its link to (2)BSDEs (Dupire, [2019](https://arxiv.org/html/2510.10728v1#bib.bib10); Cont and Fournié, [2013](https://arxiv.org/html/2510.10728v1#bib.bib9); Ekren et al., [2011](https://arxiv.org/html/2510.10728v1#bib.bib11)). Neural approaches include PDGM with LSTMs (Saporito and Zhang, [2021](https://arxiv.org/html/2510.10728v1#bib.bib29)), signature-aware BSDEs (Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13)), and Neural RDE solvers tailored to PPDEs (Fang et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib12)). These works point to two complementary levers for high-dd path problems: (i) principled summaries of history and (ii) stable continuous-time hidden dynamics.

Signatures and Neural CDE/RDEs.
The signature of a path (and its log-signature) provides a universal, hierarchical set of iterated integrals with strong approximation properties for path functionals (Lyons, [1998](https://arxiv.org/html/2510.10728v1#bib.bib23); Chevyrev and Kormilitzin, [2016](https://arxiv.org/html/2510.10728v1#bib.bib8)). Efficient software has made high-order signatures practical (Reizenstein and Graham, [2015](https://arxiv.org/html/2510.10728v1#bib.bib27)), and deep variants (e.g., deep signature transforms) have shown strong empirical performance on sequential data (Bonnier et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib5)). In parallel, neural differential equations move representation learning into continuous time: Neural ODEs offer adjoint-based memory efficiency (Chen et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib7)); Neural CDEs/RDEs further align the model class with controlled/rough dynamics and have demonstrated stable long-horizon gradients (Kidger et al., [2020](https://arxiv.org/html/2510.10728v1#bib.bib22); Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24)). In finance, combining log-signatures with Neural RDE/CDE backbones is a natural fit for PPDE/BSDE training, enabling controllable path expressivity and continuous-time state propagation (Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13); Fang et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib12)).

Estimating (Z,Γ)(Z,\Gamma) and variance reduction.
Reliable estimation of the martingale integrand ZZ and second-order object Γ\Gamma is crucial for both pricing and control. Classical Malliavin-weight identities supply low-variance regression targets for ZZ and higher-order quantities (Fournié et al., [1999](https://arxiv.org/html/2510.10728v1#bib.bib14); Glasserman, [2003](https://arxiv.org/html/2510.10728v1#bib.bib15)). In the deep BSDE setting, these targets can be blended with direct heads and drift-residual penalties to stabilize training, particularly for HJB/2BSDEs where second-order information enters the driver (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)). Regression-based BSDE estimators (Gobet et al., [2005](https://arxiv.org/html/2510.10728v1#bib.bib16); Bouchard and Touzi, [2004](https://arxiv.org/html/2510.10728v1#bib.bib6)) inform practical choices of basis/heads, while local-in-time training (DBDP) reduces variance in long horizons (Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19)).

Risk-sensitive and tail-aware training.
When left-tail fidelity matters (e.g., barrier features, drawdown-aware control), risk-sensitive objectives help align learning with evaluation. Conditional Value-at-Risk (CVaR) (Rockafellar and Uryasev, [2000](https://arxiv.org/html/2510.10728v1#bib.bib28)) provides a convex, quantile-focused surrogate that can be injected into terminal mismatch losses, improving tail calibration without materially harming mean error in practice. In control, risk-sensitive formulations have a long history (Jacobson, [1973](https://arxiv.org/html/2510.10728v1#bib.bib21)) and dovetail naturally with 2BSDE/HJB training (Soner et al., [2012](https://arxiv.org/html/2510.10728v1#bib.bib31); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)).

Positioning.
Compared to Markovian-first deep BSDE designs (Han et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib17); Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19); Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2)), our architecture is *natively* path-aware: truncated log-signatures summarize history with tunable fidelity, a Neural RDE backbone yields adjoint-memory training and stable long-horizon gradients (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24)), and optional 2BSDE heads supply second-order structure for HJB control (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)). This combination targets the dominant failure modes in high-dd path dependence (information bottlenecks and long-horizon instability) while remaining compatible with Malliavin stabilization and CVaR-tilted objectives (Fournié et al., [1999](https://arxiv.org/html/2510.10728v1#bib.bib14); Rockafellar and Uryasev, [2000](https://arxiv.org/html/2510.10728v1#bib.bib28)).

## 3. Method

We consider a dd–dimensional Itô process with *path–dependent* drift and diffusion

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | d​𝐗t=𝐛​(t,𝐗⋅⁣≤t)​d​t+𝝈​(t,𝐗⋅⁣≤t)​d​𝐖t,𝐗0=𝐱0.\mathmakebox[c]{\mathrm{d}\mathbf{X}\_{t}=\mathbf{b}\!\left(t,\mathbf{X}\_{\cdot\leq t}\right)\,\mathrm{d}t+\bm{\sigma}\!\left(t,\mathbf{X}\_{\cdot\leq t}\right)\,\mathrm{d}\mathbf{W}\_{t},\qquad\mathbf{X}\_{0}=\mathbf{x}\_{0}.} |  |

where 𝐗⋅⁣≤t\mathbf{X}\_{\cdot\leq t} denotes the full history on [0,t][0,t] and 𝐖\mathbf{W} is an mm-dimensional Brownian motion. Let g​(𝐗⋅⁣≤T)g(\mathbf{X}\_{\cdot\leq T}) be a path-dependent terminal functional (e.g., Asian payoff, drawdown penalty), and let the driver ff admit path-dependence and second-order terms as needed for fully nonlinear control (HJB) cases. Functional Itô/PPDE theory (Dupire, [2019](https://arxiv.org/html/2510.10728v1#bib.bib10); Cont and Fournié, [2013](https://arxiv.org/html/2510.10728v1#bib.bib9); Ekren et al., [2011](https://arxiv.org/html/2510.10728v1#bib.bib11)) yields a (possibly non-Markovian) BSDE/2BSDE representation:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | YT=g​(𝐗⋅⁣≤T),\displaystyle\mathmakebox[c]{Y\_{T}=g\!\left(\mathbf{X}\_{\cdot\leq T}\right),} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | d​Yt=−f​(t,𝐗⋅⁣≤t,Yt,𝐙t,𝚪t)​d​t+𝐙t​d​𝐖t,\displaystyle\mathmakebox[c]{\mathrm{d}Y\_{t}=-\,f\!\bigl(t,\mathbf{X}\_{\cdot\leq t},Y\_{t},\mathbf{Z}\_{t},\bm{\Gamma}\_{t}\bigr)\,\mathrm{d}t+\mathbf{Z}\_{t}\,\mathrm{d}\mathbf{W}\_{t},} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | 𝚪t≈Dx2​u​(t,𝐗⋅⁣≤t)(2BSDE/HJB)\displaystyle\mathmakebox[c]{\bm{\Gamma}\_{t}\approx D\_{x}^{2}u\!\left(t,\mathbf{X}\_{\cdot\leq t}\right)\quad\text{(2BSDE/HJB)}} |  |

where Yt=u​(t,𝐗⋅⁣≤t)Y\_{t}=u\!\left(t,\mathbf{X}\_{\cdot\leq t}\right) is the (path-functional) value process, 𝐙t\mathbf{Z}\_{t} is the martingale integrand (vector), and 𝚪t\bm{\Gamma}\_{t} is the second-order object (matrix) needed for fully nonlinear PDEs (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)). Our aim is to approximate (Y,𝐙,𝚪)\big(Y,\mathbf{Z},\bm{\Gamma}\big) in high dimension with *native* path awareness and stable long-horizon training.

### 3.1 Signature–RDE BSDE architecture

A central challenge is representing X⋅⁣≤tX\_{\cdot\leq t} compactly. We encode history using a *truncated log-signature* of the (time-augmented) path (Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13)):

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | 𝐬t=LogSig(m)⁡(𝐗~[0,t])∈ℝD​(m,d+1),𝐗~t:=[t;𝐗t]∈ℝd+1\mathmakebox[c]{\mathbf{s}\_{t}=\operatorname{LogSig}^{(m)}\!\bigl(\tilde{\mathbf{X}}\_{[0,t]}\bigr)\in\mathbb{R}^{D(m,d+1)},\quad\tilde{\mathbf{X}}\_{t}:=[\,t;\,\mathbf{X}\_{t}\,]\in\mathbb{R}^{d+1}} |  |

where mm is the truncation depth and D​(m,d+1)D(m,d{+}1) the resulting feature dimension. The log-signature yields a hierarchy of iterated integrals that is universal for path functionals and controllably expressive via mm.

As overviewed in Figure [1](https://arxiv.org/html/2510.10728v1#acmlabel1 "Figure 1 ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization"), the Signature–RDE couples a log-signature encoder with a Neural RDE backbone and optional 2BSDE head. We then evolve a hidden state 𝐡t∈ℝp\mathbf{h}\_{t}\in\mathbb{R}^{p} by a *Neural Rough Differential Equation (Neural RDE)* driven by a controlled path 𝐔t\mathbf{U}\_{t} built from 𝐬t\mathbf{s}\_{t} (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24); Fang et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib12)):

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | d​𝐡t=Fθ​(𝐡t)​d​𝐔t,𝐡0=hinit​(𝐱0)\mathmakebox[c]{\mathrm{d}\mathbf{h}\_{t}=F\_{\theta}\!\left(\mathbf{h}\_{t}\right)\,\mathrm{d}\mathbf{U}\_{t},\qquad\mathbf{h}\_{0}=h\_{\mathrm{init}}\!\left(\mathbf{x}\_{0}\right)} |  |

with UU a piecewise-smooth interpolation (time-augmented, optionally including low-order log-signature increments) so that the vector field Fθ:ℝp→ℝp×qF\_{\theta}:\mathbb{R}^{p}\!\to\!\mathbb{R}^{p\times q} is learned and the RDE is solved numerically (log-ODE or tailored CDE integrator). We decode the BSDE quantities via *heads*

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | Yt=gY​(𝐡t),𝐙t=gZ​(𝐡t)​𝚺t1/2,𝚪t=Sym⁡(gΓ​(𝐡t))\mathmakebox[c]{Y\_{t}=g\_{Y}(\mathbf{h}\_{t}),\quad\mathbf{Z}\_{t}=g\_{Z}(\mathbf{h}\_{t})\,\bm{\Sigma}\_{t}^{1/2},\quad\bm{\Gamma}\_{t}=\operatorname{Sym}\!\bigl(g\_{\Gamma}(\mathbf{h}\_{t})\bigr)} |  |

where 𝚺t:=𝝈​(t,𝐗⋅⁣≤t)​𝝈​(t,𝐗⋅⁣≤t)⊤\bm{\Sigma}\_{t}:=\bm{\sigma}\!\big(t,\mathbf{X}\_{\cdot\leq t}\big)\,\bm{\sigma}\!\big(t,\mathbf{X}\_{\cdot\leq t}\big)^{\!\top} and Sym​(𝐀):=12​(𝐀+𝐀⊤)\mathrm{Sym}(\mathbf{A}):=\tfrac{1}{2}\!\left(\mathbf{A}+\mathbf{A}^{\top}\right) enforces symmetry of 𝚪t\bm{\Gamma}\_{t}. For Markovian special cases, ([7](https://arxiv.org/html/2510.10728v1#S3.E7 "In 3.1 Signature–RDE BSDE architecture ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")) subsumes 𝐙t=∇xu​𝝈\mathbf{Z}\_{t}=\nabla\_{x}u\,\bm{\sigma}; for PPDEs we interpret Dx​uD\_{x}u as Dupire’s vertical derivative (Dupire, [2019](https://arxiv.org/html/2510.10728v1#bib.bib10)).

#### Multistep/local training.

To reduce variance and improve conditioning, we employ DBDP-style local training windows of length KK (Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19), [2020](https://arxiv.org/html/2510.10728v1#bib.bib20)): for grid 0=t0<⋯<tN=T0=t\_{0}<\dots<t\_{N}=T, the RDE is unrolled on [tk,tk+K][t\_{k},t\_{k+K}] with overlapping windows, sharing θ\theta globally, akin to multishooting. This preserves the continuous-time dynamics of ([6](https://arxiv.org/html/2510.10728v1#S3.E6 "In 3.1 Signature–RDE BSDE architecture ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")) while retaining the variance advantages of local fits.

### 3.2 Discretization and simulation

Let {tn}n=0N\{t\_{n}\}\_{n=0}^{N} be a uniform grid with Δ​t\Delta t. We simulate MM paths by Euler–Maruyama

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | 𝐗tn+1=𝐗tn+𝐛​(tn,𝐗⋅⁣≤tn)​Δ​t+𝝈​(tn,𝐗⋅⁣≤tn)​Δ​𝐖n\mathmakebox[c]{\mathbf{X}\_{t\_{n+1}}=\mathbf{X}\_{t\_{n}}+\mathbf{b}\!\left(t\_{n},\mathbf{X}\_{\cdot\leq t\_{n}}\right)\,\Delta t+\bm{\sigma}\!\left(t\_{n},\mathbf{X}\_{\cdot\leq t\_{n}}\right)\,\Delta\mathbf{W}\_{n}} |  |

and form 𝐬tn\mathbf{s}\_{t\_{n}} by incremental log-signature updates (cached for efficiency). The RDE ([6](https://arxiv.org/html/2510.10728v1#S3.E6 "In 3.1 Signature–RDE BSDE architecture ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")) is integrated with a fixed-order solver; gradients use the continuous-adjoint to obtain O​(N)O(N) memory. At each grid point we evaluate the heads ([7](https://arxiv.org/html/2510.10728v1#S3.E7 "In 3.1 Signature–RDE BSDE architecture ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")). For fully nonlinear cases we also compute Γtn\Gamma\_{t\_{n}}.

### 3.3 Risk-sensitive and physics-informed losses

We combine a terminal-mismatch objective with a discretized BSDE residual and a risk-sensitive (tail-aware) weighting:

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | ℒterm=𝔼​[(1+η​ 1​{ΔT2≥Qq​(ΔT2)})​ΔT2]\displaystyle\mathmakebox[c]{\mathcal{L}\_{\mathrm{term}}=\mathbb{E}\!\left[\bigl(1+\eta\,\mathbb{1}\{\Delta\_{T}^{2}\geq Q\_{q}(\Delta\_{T}^{2})\}\bigr)\,\Delta\_{T}^{2}\right]} |  |
|  |  |  |
| --- | --- | --- |
|  | ΔT≔YtN−g​(𝐗⋅⁣≤T),q∈[0.90,0.99],η>0\displaystyle\mathmakebox[c]{\Delta\_{T}\coloneqq Y\_{t\_{N}}-g\!\bigl(\mathbf{X}\_{\cdot\leq T}\bigr),\quad q\in[0.90,0.99],\ \eta>0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | ℒdrift=𝔼​[∑n=0N−11Δ​t​‖Ytn+1−Ytn+ftn​Δ​t−𝐙tn​Δ​𝐖n‖2]\displaystyle\mathmakebox[c]{\mathcal{L}\_{\mathrm{drift}}=\mathbb{E}\!\left[\sum\_{n=0}^{N-1}\frac{1}{\Delta t}\left\|\,Y\_{t\_{n+1}}-Y\_{t\_{n}}+f\_{t\_{n}}\,\Delta t-\mathbf{Z}\_{t\_{n}}\,\Delta\mathbf{W}\_{n}\,\right\|^{2}\right]} |  |
|  |  |  |
| --- | --- | --- |
|  | ftn≔f​(tn,𝐗⋅⁣≤tn,Ytn,𝐙tn,𝚪tn)\displaystyle\mathmakebox[c]{f\_{t\_{n}}\coloneqq f\!\bigl(t\_{n},\mathbf{X}\_{\cdot\leq t\_{n}},Y\_{t\_{n}},\mathbf{Z}\_{t\_{n}},\bm{\Gamma}\_{t\_{n}}\bigr)} |  |

The tilt in ([9](https://arxiv.org/html/2510.10728v1#S3.E9 "In 3.3 Risk-sensitive and physics-informed losses ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")) emphasizes the worst (1−q)(1{-}q) tail of the terminal error (a CVaR-style surrogate) and is plug-compatible with any BSDE scheme. For HJB/2BSDE we optionally add a second-order “physics” penalty:

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | ℒ2​n​d=𝔼​[∑n=0N−1‖ℋ​(tn,𝐗tn;Ytn,𝐙tn,𝚪tn)‖+2]\mathmakebox[c]{\mathcal{L}\_{\mathrm{2nd}}=\mathbb{E}\!\left[\sum\_{n=0}^{N-1}\!\left\|\,\mathcal{H}\!\left(t\_{n},\mathbf{X}\_{t\_{n}};\,Y\_{t\_{n}},\mathbf{Z}\_{t\_{n}},\bm{\Gamma}\_{t\_{n}}\right)\,\right\|\_{+}^{2}\right]} |  |

where ℋ\mathcal{H} denotes the discretized HJB residual (e.g., sup/inf over controls). The final loss is

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | ℒ=λT​ℒterm+λB​ℒdrift+λ2​ℒ2​n​d\mathmakebox[c]{\mathcal{L}=\lambda\_{T}\,\mathcal{L}\_{\mathrm{term}}+\lambda\_{B}\,\mathcal{L}\_{\mathrm{drift}}+\lambda\_{2}\,\mathcal{L}\_{\mathrm{2nd}}} |  |

with (λT,λB,λ2)(\lambda\_{T},\lambda\_{B},\lambda\_{2}) chosen via validation.

### 3.4 Estimating ZZ and Γ\Gamma: direct vs. Malliavin

We explore three estimators under identical discretization:

(A) Direct heads. Learn gZ,gΓg\_{Z},g\_{\Gamma} in ([7](https://arxiv.org/html/2510.10728v1#S3.E7 "In 3.1 Signature–RDE BSDE architecture ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")) end-to-end by minimizing ([12](https://arxiv.org/html/2510.10728v1#S3.E12 "In 3.3 Risk-sensitive and physics-informed losses ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")). This is flexible but may be noisy when the drift residual is small compared to martingale noise.

(B) Malliavin weights for ZZ. For small Δ​t\Delta t, a classical Malliavin argument gives the local identity (schematically, suppressing conditioning)

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | 𝐙tn≈1Δ​t​𝔼​[Ytn+1​∫tntn+1(𝝈−1)𝖳​(s,𝐗⋅⁣≤s)​d𝐖s]\mathmakebox[c]{\mathbf{Z}\_{t\_{n}}\;\approx\;\frac{1}{\Delta t}\,\mathbb{E}\!\left[Y\_{t\_{n+1}}\int\_{t\_{n}}^{t\_{n+1}}(\bm{\sigma}^{-1})^{\mathsf{T}}\!\bigl(s,\mathbf{X}\_{\cdot\leq s}\bigr)\,\mathrm{d}\mathbf{W}\_{s}\right]} |  |

which we realize by a *regression* target Z^tn\hat{Z}\_{t\_{n}} on simulated paths and add a supervised term

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | ℒZ=αZ​𝔼​[∑n=0N−1‖𝐙tn−𝐙^tn‖2]\mathmakebox[c]{\mathcal{L}\_{Z}=\alpha\_{Z}\,\mathbb{E}\!\left[\sum\_{n=0}^{N-1}\left\|\,\mathbf{Z}\_{t\_{n}}-\hat{\mathbf{Z}}\_{t\_{n}}\,\right\|^{2}\right]} |  |

(C) Malliavin/second-order for Γ\Gamma. Analogously, second-order weights (or finite-difference in antithetic directions) provide a low-variance proxy Γ^tn\hat{\Gamma}\_{t\_{n}}; we add

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | ℒΓ=αΓ​𝔼​[∑n=0N−1‖𝚪tn−𝚪^tn‖F2]\mathmakebox[c]{\mathcal{L}\_{\Gamma}=\alpha\_{\Gamma}\,\mathbb{E}\!\left[\sum\_{n=0}^{N-1}\left\|\,\bm{\Gamma}\_{t\_{n}}-\hat{\bm{\Gamma}}\_{t\_{n}}\,\right\|\_{F}^{2}\right]} |  |

The *hybrid* objective ℒ+ℒZ+ℒΓ\mathcal{L}{+}\mathcal{L}\_{Z}{+}\mathcal{L}\_{\Gamma} stabilizes training in fully nonlinear regimes (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)). In Markovian limits, Z=∇xu​σZ=\nabla\_{x}u\,\sigma recovers the gradient interpretation; in PPDEs, Dx​uD\_{x}u is Dupire’s vertical derivative (Dupire, [2019](https://arxiv.org/html/2510.10728v1#bib.bib10)).

### 3.5 Computational complexity and memory

For MM paths, NN steps, hidden width pp, and signature depth mm (dimension DD), a forward pass costs

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | 𝒪​(M​N​[d2⏟SDE+D⏟LogSig+p2⏟RDE+p​(d+d2)⏟heads])\mathmakebox[c]{\mathcal{O}\!\bigl(MN\,[\underbrace{d^{2}}\_{\text{SDE}}+\underbrace{D}\_{\text{LogSig}}+\underbrace{p^{2}}\_{\text{RDE}}+\underbrace{p(d{+}d^{2})}\_{\text{heads}}]\bigr)} |  |

The continuous-adjoint for the RDE yields O​(N)O(N) memory in NN, rather than storing all intermediate htnh\_{t\_{n}} (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24)). Log-signature updates are incremental and can be parallelized over paths; we normalize by layernorm to reduce dynamic range.

### 3.6 Consistency sketch

Assume (i) Lipschitz b,σ,fb,\sigma,f in appropriate functional norms; (ii) universal approximation of continuous controlled vector fields by FθF\_{\theta} on compact sets; (iii) universal approximation of continuous functionals of paths by truncated log-signatures as m→∞m\to\infty; and (iv) a stable RDE integrator. Then there exists a sequence of parameters (θ,gY,gZ,gΓ)(\theta,g\_{Y},g\_{Z},g\_{\Gamma}), depths mm, and widths pp such that the induced processes (Yθ,Zθ,Γθ)(Y^{\theta},Z^{\theta},\Gamma^{\theta}) satisfy

|  |  |  |
| --- | --- | --- |
|  | limm,p→∞limN→∞𝔼​[supt∈[0,T](|Ytθ−Yt|2+‖𝐙tθ−𝐙t‖2+‖𝚪tθ−𝚪t‖F2)]= 0\mathmakebox[c]{\lim\_{m,p\to\infty}\,\lim\_{N\to\infty}\,\mathbb{E}\!\left[\sup\_{t\in[0,T]}\!\bigl(\,|Y\_{t}^{\theta}-Y\_{t}|^{2}+\|\mathbf{Z}\_{t}^{\theta}-\mathbf{Z}\_{t}\|^{2}+\|\bm{\Gamma}\_{t}^{\theta}-\bm{\Gamma}\_{t}\|\_{F}^{2}\bigr)\right]\;=\;0} |  |

The argument combines universal approximation for CDE/RDE flows and the density of signatures for path functionals, with standard stability of BSDE solutions. This justifies increasing (m,p)(m,p) and grid refinement until validation error saturates (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24); Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13); Han et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib17); Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19)).

### 3.7 Practical details

We use time-augmentation [t;Xt][t;X\_{t}], gradient clipping on RDE adjoints, symmetry projection for Γ\Gamma, and a small entropic penalty on Γ\Gamma to discourage ill-conditioned Hessians. Calibration follows a two-phase schedule: (1) warm-start with (λT,λB,λ2)=(1,1,0)(\lambda\_{T},\lambda\_{B},\lambda\_{2})=(1,1,0) and small tail tilt (η≈0.5)(\eta\!\approx\!0.5); (2) enable ℒ2​n​d\mathcal{L}\_{\mathrm{2nd}} and increase tail focus (η∈[1,3],q∈[0.95,0.99])(\eta\!\in\![1,3],\,q\!\in\![0.95,0.99]) once terminal error stabilizes. Multistep window KK is chosen so that each window contains ≈10\approx\!10–2020 steps; we report robustness to KK.

Input: Grid {tn}0:N\{t\_{n}\}\_{0:N}, batch MM, signature depth mm, window KK, weights (λT,λB,λ2)(\lambda\_{T},\lambda\_{B},\lambda\_{2}), tilt (q,η)(q,\eta), b,σb,\sigma, driver ff, HJB residual ℋ\mathcal{H}

Output: Parameters Θ={θ,gY,gZ,gΓ}\Theta=\{\theta,g\_{Y},g\_{Z},g\_{\Gamma}\}

1exInitialize Θ←Θ0\Theta\!\leftarrow\!\Theta\_{0}, optimizer 𝒪\mathcal{O}, warm-start schedules for (λT,λB,λ2)(\lambda\_{T},\lambda\_{B},\lambda\_{2}) and (q,η)(q,\eta)

for *iter =1,2,…=1,2,\dots* do

(X,Δ​W,𝐬)←ForwardSimulate​(M,N,b,σ,m)(X,\Delta W,\mathbf{s})\leftarrow\textsc{ForwardSimulate}(M,N,b,\sigma,m)

// Euler–Maruyama + incremental LogSig(m)

ℒterm,ℒdrift,ℒ2​n​d←0\mathcal{L}\_{\mathrm{term}},\mathcal{L}\_{\mathrm{drift}},\mathcal{L}\_{\mathrm{2nd}}\leftarrow 0

for *k=0k=0 to N−KN{-}K step K*stride*K\_{\text{stride}}* do

U←BuildControlledPaths(𝐬,k:k+K)U\leftarrow\textsc{BuildControlledPaths}(\mathbf{s},k{:}k{+}K)

h←IntegrateRDE​(Fθ,U,hinit​(Xtk))h\leftarrow\textsc{IntegrateRDE}(F\_{\theta},U,h\_{\mathrm{init}}(X\_{t\_{k}}))

// log-ODE/CDE solver with adjoint

(Y,Z,Γ)←DecodeHeads​(h,Σ)(Y,Z,\Gamma)\leftarrow\textsc{DecodeHeads}(h,\Sigma)

// Y=gY​(h)Y{=}g\_{Y}(h), Z=gZ​(h)​Σ1/2Z{=}g\_{Z}(h)\Sigma^{1/2}, Γ=Sym​(gΓ​(h))\Gamma{=}\mathrm{Sym}(g\_{\Gamma}(h))

(ℒT,ℒB)←BSDELoss​(Y,Z,Δ​W,f;q,η)(\mathcal{L}\_{T},\mathcal{L}\_{B})\leftarrow\textsc{BSDELoss}(Y,Z,\Delta W,f;q,\eta)

// CVaR-tilted terminal + drift residual

ℒterm+=ℒT\mathcal{L}\_{\mathrm{term}}\mathrel{+}=\mathcal{L}\_{T},  ℒdrift+=ℒB\mathcal{L}\_{\mathrm{drift}}\mathrel{+}=\mathcal{L}\_{B}

if *use\_HJB* then

ℒ2​n​d+=∥ℋ(⋅;Y,Z,Γ)∥+2\mathcal{L}\_{\mathrm{2nd}}\mathrel{+}=\|\mathcal{H}(\cdot;Y,Z,\Gamma)\|\_{+}^{2}

end if

if *use\_Malliavin* then

(Z^,Γ^)←MalliavinTargets​(Y,Δ​W)(\hat{Z},\hat{\Gamma})\leftarrow\textsc{MalliavinTargets}(Y,\Delta W); ℒdrift+=αZ∥Z−Z^∥2+αΓ∥Γ−Γ^∥F2\mathcal{L}\_{\mathrm{drift}}\mathrel{+}=\alpha\_{Z}\|Z{-}\hat{Z}\|^{2}+\alpha\_{\Gamma}\|\Gamma{-}\hat{\Gamma}\|\_{F}^{2}

end if

end for

ℒ←λT​ℒterm+λB​ℒdrift+λ2​ℒ2​n​d\mathcal{L}\leftarrow\lambda\_{T}\mathcal{L}\_{\mathrm{term}}+\lambda\_{B}\mathcal{L}\_{\mathrm{drift}}+\lambda\_{2}\mathcal{L}\_{\mathrm{2nd}}

Γ←Sym​(Γ)\Gamma\leftarrow\mathrm{Sym}(\Gamma); RegularizeAndClip(Γ)(\Gamma); Θ←𝒪​(Θ,∇Θℒ)\Theta\leftarrow\mathcal{O}(\Theta,\nabla\_{\Theta}\mathcal{L}); Curriculum(q,η,K)(q,\eta,K)

end for

Algorithm 1 Signature–RDE BSDE Training

## 4. Experiments

Goals.
We evaluate whether a *Signature–RDE (Sig–RDE) BSDE* solver improves accuracy, tail calibration, and training stability for (i) high-dimensional *path-dependent pricing* and (ii) *portfolio control* (fully nonlinear HJB/2BSDE), relative to strong deep BSDE baselines (Han et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib17); Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19); Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2), [2021](https://arxiv.org/html/2510.10728v1#bib.bib3), [b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)) and path-aware solvers (Saporito and Zhang, [2021](https://arxiv.org/html/2510.10728v1#bib.bib29); Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13); Fang et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib12)).

Tasks.
*T1:* Asian basket (50D, 100D); *T2:* Barrier (50D); *T3:* Portfolio control (10D) under stochastic volatility with risk-sensitive utility (HJB).
SDEs are discretized by Euler–Maruyama on a uniform grid NN; path dependence enters via running averages/extrema.
For T3 we assess both value-function quality and the induced allocations.

Baselines.
(B1) Deep BSDE (FFN); (B2) DBDP (Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19), [2020](https://arxiv.org/html/2510.10728v1#bib.bib20)); (B3) Deep Splitting (Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2), [2021](https://arxiv.org/html/2510.10728v1#bib.bib3)); (B4) PDGM/LSTM (Saporito and Zhang, [2021](https://arxiv.org/html/2510.10728v1#bib.bib29)); (B5) 2BSDE head (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)); (B6) *Discrete RNN* that consumes the raw time-augmented path with gated updates; and (B7) *Neural CDE* (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24)) that evolves a hidden state 𝐡t\mathbf{h}\_{t} under a learned continuous vector field driven by a spline interpolation of the observed path.
For fairness, we match parameter budgets, training grids, optimizers, and decoder heads (Eq. (7)) across methods.111Architectural details. The discrete RNN uses GRU cells with hidden width matched to our RDE width pp, layer normalization on inputs, and the same decoder heads as Eq. (7). Neural CDE uses a cubic interpolation for the controlled path and shares identical decoder heads.
We emphasize comparisons to the path-aware *Neural CDE* (B7) and *PDGM/LSTM* (B4), with *Discrete RNN* (B6) serving as the strongest discrete-time sequence baseline under matched budgets.

Expected tradeoffs.
Neural CDE should approach Sig–RDE on mean error with slightly weaker tail calibration (no explicit 𝚺1/2\bm{\Sigma}^{1/2} head coupling as in Eq. (7)), while the discrete RNN is more sensitive to horizon and step count.
Concretely, we anticipate:
(i) a higher NaN/overflow rate (%) and worse tail CVaR\mathrm{CVaR} for the RNN than for CDE ≈\approx Sig–RDE at matched parameters; and
(ii) lower runtime for CDE than RNN at similar width (adjoint memory and fewer stored states).

Metrics.
Primary: relative pricing error (RPE, %), absolute error (AE), and CVaRq\mathrm{CVaR}\_{q} of terminal mismatch (reported as relative % at q=0.95q{=}0.95).
Stability: NaN/overflow rate (%), BSDE residual RMS, and HJB residual ∥ℋ​(⋅)∥+\lVert\mathcal{H}(\cdot)\rVert\_{+}.
Efficiency: time/epoch (s), peak memory (GB), parameter count (M).
For T3 we also report 𝐙\mathbf{Z}- and 𝚪\bm{\Gamma}-RMSE against high-resolution references.

Implementation.
Defaults: log-signature depth m=3m{=}3, RDE width p=128p{=}128, window K=12K{=}12 (stride 6), tilt (q=0.95,η=1.5)(q{=}0.95,\eta{=}1.5); warm start (λT,λB,λ2)=(1,1,0)(\lambda\_{T},\lambda\_{B},\lambda\_{2}){=}(1,1,0), enabling λ2=0.2\lambda\_{2}{=}0.2 after 20%20\% of steps.
Decoders follow ([7](https://arxiv.org/html/2510.10728v1#S3.E7 "In 3.1 Signature–RDE BSDE architecture ‣ 3. Method ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")).
HJB experiments compare direct versus Malliavin stabilized heads (§3.4).
Hardware/stack: A100-40GB; PyTorch 2.x; signatures library.

### 4.1 Main results

Table 1. Path-dependent pricing (T1/T2). Mean±\pms.e. over 5 seeds. Lower is better for errors/time/memory.

Method
Dim
RPE (%)
CVaR0.95\mathrm{CVaR}\_{0.95} (%)
Time (s/epoch)
Peak (GB)
Params (M)

Ours: Sig–RDE
50
1.12±\pm0.12
2.95
89
6.2
1.8

Neural CDE
50
1.20±\pm0.14
3.10
93
6.3
1.8

RNN (discrete, no RDE)
50
1.38±\pm0.18
3.45
84
6.0
1.8

Ours (no-Sig)
50
1.30±\pm0.16
3.25
81
5.6
1.7

DBDP
50
1.47±\pm0.21
3.62
106
6.9
2.5

DeepSplit
50
1.34±\pm0.17
3.35
121
6.2
2.2

PDGM/LSTM
50
2.42±\pm0.34
5.25
149
7.1
2.6

Ours: Sig–RDE
100
1.62±\pm0.20
4.75
146
8.1
1.9

Neural CDE
100
1.72±\pm0.22
5.10
152
8.0
1.9

RNN (discrete, no RDE)
100
1.95±\pm0.27
5.70
132
7.4
1.9

DBDP
100
2.07±\pm0.29
5.95
191
9.2
2.7

DeepSplit
100
1.90±\pm0.26
5.45
209
8.8
2.3

#### T1/T2: Path-dependent pricing.

Under matched parameter budgets (means±\pm s.e., 5 seeds), *Signature–RDE* achieves lower error than the strongest continuous-time baseline (Table [1](https://arxiv.org/html/2510.10728v1#S4.T1 "Table 1 ‣ 4.1 Main results ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")).
At d=50d{=}50, RPE falls by 6.7%\mathbf{6.7\%} relative to Neural CDE (1.121.12 vs. 1.201.20), with a 4.8%\mathbf{4.8\%} reduction in CVaR0.95\mathrm{CVaR}\_{0.95} (2.952.95 vs. 3.103.10).
At d=100d{=}100, improvements persist (RPE −5.8%-\mathbf{5.8\%}, 1.621.62 vs. 1.721.72; CVaR0.95\mathrm{CVaR}\_{0.95} −6.9%-\mathbf{6.9\%}, 4.754.75 vs. 5.105.10).
Runtime remains comparable: 8989s/epoch at d=50d{=}50 (≈\approx4% faster than Neural CDE; 16–26% faster than DBDP/DeepSplit) and 146146s/epoch at d=100d{=}100 (≈\approx4% faster than Neural CDE; 24–30% faster than DBDP/DeepSplit), with similar peak memory to Neural CDE and lower than DBDP/DeepSplit.
Scaling behavior—the widening separation at higher dd—is visualized in Figure [2](https://arxiv.org/html/2510.10728v1#S4.F2 "Figure 2 ‣ 4.2 Scaling and tail calibration ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization").

#### T3: Portfolio control.

For the control task, coupling signatures with an RDE backbone and a 2BSDE head produces more stable second-order quantities and dynamics: Γ\Gamma RMSE and the HJB residual are consistently lower while utility remains competitive across seeds.
These metrics, reported in Table [2](https://arxiv.org/html/2510.10728v1#S4.T2 "Table 2 ‣ T3: Portfolio control. ‣ 4.1 Main results ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization"), indicate improved calibration of second-order structure without sacrificing efficiency (training budgets aligned with T1/T2).
Together with the T1/T2 pricing results, the evidence supports the hypothesis that continuous-time modeling with log-signature features yields robustness that strengthens as dimensionality grows.

Table 2. Portfolio control (T3; fully nonlinear HJB). Lower error is better; higher Utility is better.
*Note:* Neural CDE and RNN produce Γ\Gamma via the same decoder as Eq. (7); DBDP lacks a second-order head, so ‖Γ‖RMSE\|\Gamma\|\_{\text{RMSE}} is not applicable.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | ‖Z‖RMSE\|Z\|\_{\text{RMSE}} | ‖Γ‖RMSE\|\Gamma\|\_{\text{RMSE}} | HJB resid. | Utility | NaN (%) |
| Ours: Sig–RDE + 2BSDE | 0.097 | 0.142 | 0.011 | 1.33 | 0.3 |
| Neural CDE | 0.105 | 0.165 | 0.014 | 1.30 | 0.7 |
| RNN (no RDE) | 0.125 | 0.205 | 0.022 | 1.25 | 2.1 |
| Ours (direct hs) | 0.112 | 0.177 | 0.017 | 1.28 | 1.6 |
| 2BSDE | 0.119 | 0.192 | 0.020 | 1.27 | 2.6 |
| DBDP | 0.146 | – | 0.029 | 1.22 | 4.1 |



Input: Frozen parameters Θ⋆={θ⋆,gY⋆,gZ⋆,gΓ⋆}\Theta^{\star}=\{\theta^{\star},g\_{Y}^{\star},g\_{Z}^{\star},g\_{\Gamma}^{\star}\}; grid {tn}0:N\{t\_{n}\}\_{0:N}; signature depth mm; window KK; market inputs (b,σ)(b,\sigma); driver ff; path XX (or simulated paths); covariance Σ\Sigma

Output: Price u​(0,x)u(0,x) or value Yt0Y\_{t\_{0}}; control (if HJB) πt\pi\_{t} from (Zt,Γt)(Z\_{t},\Gamma\_{t})

1exif *MC* then

Simulate MM sample paths X(i)X^{(i)} (Euler–Maruyama) and increments Δ​W(i)\Delta W^{(i)}

end if

Compute incremental log-signatures 𝐬tn(i)←LogSig(m)​(X~[0,tn](i))\mathbf{s}\_{t\_{n}}^{(i)}\leftarrow\mathrm{LogSig}^{(m)}(\tilde{X}^{(i)}\_{[0,t\_{n}]})

for *k=0k=0 to N−KN{-}K step K*stride*K\_{\text{stride}}* do

U[tk,tk+​K](i)←BuildControlledPaths(𝐬(i),k:k+K)U^{(i)}\_{[t\_{k},t\_{k+}K]}\leftarrow\textsc{BuildControlledPaths}(\mathbf{s}^{(i)},k{:}k{+}K)

htk(i)←hinit​(Xtk(i))h^{(i)}\_{t\_{k}}\leftarrow h\_{\text{init}}(X^{(i)}\_{t\_{k}}); Integrate d​ht(i)=Fθ⋆​(ht(i))​d​Ut(i)dh^{(i)}\_{t}=F\_{\theta^{\star}}(h^{(i)}\_{t})\,dU^{(i)}\_{t} (no adjoint)

(Yt(i),Zt(i),Γt(i))←(gY⋆​(ht(i)),gZ⋆​(ht(i))​Σt1/2,Sym​(gΓ⋆​(ht(i))))(Y^{(i)}\_{t},Z^{(i)}\_{t},\Gamma^{(i)}\_{t})\leftarrow(g\_{Y}^{\star}(h^{(i)}\_{t}),~g\_{Z}^{\star}(h^{(i)}\_{t})\Sigma^{1/2}\_{t},~\mathrm{Sym}(g\_{\Gamma}^{\star}(h^{(i)}\_{t})))

if *HJB* then

Extract feedback control πt=Π​(Yt(i),Zt(i),Γt(i))\pi\_{t}=\Pi(Y^{(i)}\_{t},Z^{(i)}\_{t},\Gamma^{(i)}\_{t}) (problem-specific)

end if

end for

return *u^​(0,x):=1M​∑i=1MYt0(i)\widehat{u}(0,x):=\frac{1}{M}\sum\_{i=1}^{M}Y^{(i)}\_{t\_{0}} (pricing) or deployment policy πt\pi\_{t} (control).*

Algorithm 2 Inference/Valuation with Signature–RDE BSDE

### 4.2 Scaling and tail calibration

![Refer to caption](x1.png)


Figure 2. Scaling with dimension dd (T1). RPE vs. dd at fixed param count; time/epoch inset.

![Refer to caption](x2.png)


Figure 3. Tail calibration under CVaR tilt: CVaRq\mathrm{CVaR}\_{q} vs. q∈[0.90,0.99]q\in[0.90,0.99] (T1, d=100d{=}100).

Tail behaviour across dimension and quantiles.
As visualized in Figure [3](https://arxiv.org/html/2510.10728v1#S4.F3 "Figure 3 ‣ 4.2 Scaling and tail calibration ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization") and quantified in Table [3](https://arxiv.org/html/2510.10728v1#S4.T3 "Table 3 ‣ 4.2 Scaling and tail calibration ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization"), our method is uniformly best across *all* d∈{50,100,200}d\in\{50,100,200\} and q∈{0.90,0.95,0.975,0.99}q\in\{0.90,0.95,0.975,0.99\}, and the gap to baselines widens in the extreme tail and at higher dimension.
At d=200d{=}200 and q=0.99q{=}0.99, Sig–RDE attains 9.80%9.80\% versus 12.00%12.00\% for DeepSplit and 13.10%13.10\% for DBDP, i.e., 18.3% and 25.2% relative reductions, respectively; it also improves over Neural CDE (10.95%10.95\%) by 10.5% and over the discrete RNN (12.35%12.35\%) by 20.7%.
At d=100d{=}100 and q=0.95q{=}0.95, Sig–RDE (4.75%4.75\%) outperforms Neural CDE (5.10%5.10\%: 6.9% gain), the RNN (5.70%5.70\%: 16.7%), DeepSplit (5.45%5.45\%: 12.8%), and DBDP (5.95%5.95\%: 20.2%).
Even at d=50d{=}50, the advantage is visible in the far tail (q=0.99q{=}0.99): 4.90%4.90\% for Sig–RDE versus 6.20%6.20\% (DeepSplit, 21.0% reduction) and 6.80%6.80\% (DBDP, 27.9%).

Degradation with dimension.
All methods see larger CVaRq\mathrm{CVaR}\_{q} as dd grows, but the *ordering remains stable* and the absolute gap to feedforward/discrete baselines increases in the extreme tail (e.g., q=0.99q{=}0.99 gap to DeepSplit grows from 1.301.30 pp at d=50d{=}50 to 2.202.20 pp at d=200d{=}200).
This aligns with the hypothesis that continuous-time state propagation and path compression mitigate long-horizon accumulation effects (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24); Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13)).

Effect of tail tilt.
Increasing the CVaR tilt parameter η\eta steepens tail emphasis and improves CVaRq\mathrm{CVaR}\_{q} with only modest runtime cost; in practice we observe a broad, stable region for η∈[1,3]\eta\!\in[1,3] and q∈[0.95,0.99]q\!\in[0.95,0.99].
Within this range, the multiplicative inflation from CVaR0.90\mathrm{CVaR}\_{0.90} to CVaR0.99\mathrm{CVaR}\_{0.99} is roughly 2.2×2.2{\times} across methods (e.g., at d=100d{=}100 our 7.35/3.28≈2.247.35/3.28\!\approx\!2.24), yet Sig–RDE stays lowest at each quantile, indicating that the signature–RDE combination improves not only average error but also the shape of the left tail.

Table 3. Tail calibration for T1 at d∈{50,100,200}d\in\{50,100,200\} (smaller is better).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Dim | Method | CVaR0.90\mathrm{CVaR}\_{0.90} (%) | CVaR0.95\mathrm{CVaR}\_{0.95} (%) | CVaR0.975\mathrm{CVaR}\_{0.975} (%) | CVaR0.99\mathrm{CVaR}\_{0.99} (%) |
| 50 | Ours: Sig–RDE | 2.84 | 2.95 | 3.70 | 4.90 |
|  | Neural CDE | 2.95 | 3.10 | 4.10 | 5.30 |
|  | RNN (disc., no RDE) | 3.25 | 3.45 | 4.70 | 6.50 |
|  | DeepSplit | 3.10 | 3.35 | 4.55 | 6.20 |
|  | DBDP | 3.35 | 3.62 | 4.95 | 6.80 |
| 100 | Ours: Sig–RDE | 3.28 | 4.75 | 5.98 | 7.35 |
|  | Neural CDE | 3.70 | 5.10 | 6.55 | 8.35 |
|  | RNN (disc., no RDE) | 4.25 | 5.70 | 7.60 | 9.55 |
|  | DeepSplit | 4.05 | 5.45 | 7.30 | 9.15 |
|  | DBDP | 4.50 | 5.95 | 8.05 | 10.25 |
| 200 | Ours: Sig–RDE | 4.70 | 6.30 | 7.90 | 9.80 |
|  | Neural CDE | 5.05 | 6.55 | 8.65 | 10.95 |
|  | RNN (disc., no RDE) | 5.50 | 7.25 | 9.70 | 12.35 |
|  | DeepSplit | 5.35 | 7.10 | 9.40 | 12.00 |
|  | DBDP | 5.65 | 7.45 | 10.05 | 13.10 |

### 4.3 Ablations (what matters when)

![Refer to caption](x3.png)


Figure 4. Ablations on T1 (d=100d{=}100): signature depth mm, RDE width pp, window KK, and Malliavin.

Ablation and scaling summary.
Across the single–factor ablations in Table [4](https://arxiv.org/html/2510.10728v1#S4.T4 "Table 4 ‣ 4.3 Ablations (what matters when) ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization") (visualized in Figure [4](https://arxiv.org/html/2510.10728v1#S4.F4 "Figure 4 ‣ 4.3 Ablations (what matters when) ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")), we observe consistent improvements from richer path features and moderate capacity, with diminishing returns beyond a mid-range configuration. Increasing the *signature depth* from m=2m{=}2 to m=3m{=}3 reduces RPE by 12.0% (1.84→\rightarrow1.62) and CVaR0.95\mathrm{CVaR}\_{0.95} by 13.0% (5.45→\rightarrow4.74) at a modest time cost (138→\rightarrow146 s/epoch); moving to m=4m{=}4 yields smaller gains (1.62→\rightarrow1.58; 4.74→\rightarrow4.60) with higher time (161 s), suggesting m=3m{=}3–44 as a practical sweet spot for T1, and deeper truncations primarily benefiting strongly non-Markovian cases (Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13)). For *RDE width*, 64→\rightarrow128 tightens both RPE (1.75→\rightarrow1.62, 7.4%) and tail error (5.12→\rightarrow4.74, 7.4%), while 128→\rightarrow192 yields marginal accuracy changes (1.62→\rightarrow1.59; 4.74→\rightarrow4.64) at increased time (183 s), so we cap pp at 128–192. *Local windows* corroborate variance–bias trade-offs (Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19)): K=12K{=}12 improves over K=8K{=}8 (RPE 1.70→\rightarrow1.62; CVaR0.95\mathrm{CVaR}\_{0.95} 4.98→\rightarrow4.74) with little runtime change (139→\rightarrow146 s), whereas K=16K{=}16 offers only incremental accuracy with stiffer dynamics (172 s, slight NaN uptick). *Malliavin targets* reduce variance in Z,ΓZ,\Gamma and stabilize training (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)): CVaR0.95\mathrm{CVaR}\_{0.95} improves from 4.95 to 4.74 and NaN drops from 0.5% to 0.0% at essentially the same cost (146–148 s). Finally, removing signatures while keeping capacity fixed degrades tails: at d=50d{=}50 in Table [1](https://arxiv.org/html/2510.10728v1#S4.T1 "Table 1 ‣ 4.1 Main results ‣ 4. Experiments ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization"), RPE rises from 1.12% to 1.30% (+16%) and CVaR0.95\mathrm{CVaR}\_{0.95} from 2.95% to 3.25% (+10%), even though the no-signature model trains slightly faster. These results support the thesis that *continuous-time state propagation* (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24)) and *log-signature path compression* (Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13)) curb long-horizon error growth and improve left-tail fidelity at fixed budgets.

Table 4. Ablations on T1 (d=100d{=}100). Change one knob at a time; others at default (m=3m{=}3, p=128p{=}128, K=12K{=}12, CVaR tilt q=0.95,η=1.5q{=}0.95,\eta{=}1.5).

Setting
Value
RPE (%)
CVaR0.95\mathrm{CVaR}\_{0.95} (%)
Time (s/epoch)
NaN (%)

mm
2
1.84
5.45
138
0.1

mm
3
1.62
4.74
146
0.0

mm
4
1.58
4.60
161
0.0

pp
64
1.75
5.12
113
0.0

pp
128
1.62
4.74
146
0.0

pp
192
1.59
4.64
183
0.0

KK
8
1.70
4.98
139
0.0

KK
12
1.62
4.74
146
0.0

KK
16
1.60
4.66
172
0.2

Malliavin
off
1.65
4.95
146
0.5

Malliavin
on
1.62
4.74
148
0.0

### 4.4 Robustness & stress

We probe (i) timestep sensitivity (NN halved/doubled), (ii) vol-of-vol and correlation sweeps, and (iii) OOD drift/vol scales at inference. The Signature–RDE solver maintains monotone error decay with NN and degrades smoothly under parameter shifts (continuous-time hidden dynamics). Under stress vol-of-vol, Malliavin stabilization and moderate KK prevent gradient explosions.

## 5. Experimental Details and Reproducibility Card

We conduct all experiments on a single NVIDIA A100 (40 GB) using PyTorch 2.x with torchdiffeq/torchcde and a signature library, fixing deterministic seeds {13,31,71,97,123}\{13,31,71,97,123\}. Tasks comprise T1 (Asian basket) in dimensions d∈{20,50,100,200}d\in\{20,50,100,200\} under Black–Scholes dynamics with the drift/vol/correlation specified in the main text and a time–average payoff; T2 (Barrier) with d=50d{=}50 and an absorbing knock–out boundary; and T3 (Portfolio control) with d=10d{=}10 under stochastic volatility and a risk–sensitive utility, where an HJB residual term is enabled when indicated. Discretization uses a uniform grid with NN steps, Euler–Maruyama for the state process XX, and mini‐batch Monte Carlo; the grid, simulation, and cost setup are identical across all methods to ensure comparability. Architectures for our approach use signature depth m∈{2,3,4}m\in\{2,3,4\}, RDE hidden width p∈{64,128,192}p\in\{64,128,192\}, and window size K∈{8,12,16}K\in\{8,12,16\}; decoders gY,gZ,gΓg\_{Y},g\_{Z},g\_{\Gamma} are compact MLP heads, with a symmetry projection on Γ\Gamma and a mild spectral penalty. Training employs Adam/AdamW with cosine decay; we warm‐start without the HJB residual weight λ2\lambda\_{2} and enable it after 20% of steps, and we apply a CVaR tilt whose parameters (q,η)(q,\eta) are ramped linearly from (0.95,0.5)(0.95,0.5) to (0.99,1.5)(0.99,1.5) in late training. When Malliavin targets are enabled, we use antithetic sampling and pathwise weights for ZZ, while for Γ\Gamma we employ symmetricized finite‐difference control variates; all targets are computed under the same discretization to avoid bias. For accountability and measurement, we report wall–clock time per epoch (s), peak memory in GB (via the PyTorch profiler), parameter count in millions, and the exact commit hashes used. Fairness is enforced by giving all methods the same SDE simulation, time grids, cost settings, and matched parameter/time budgets; baselines are tuned via grid search following (Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19); Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2)).

![Refer to caption](x4.png)


Figure 5. Performance–diagnostics diagram (T1/T3): RPE vs. time/epoch with NaN contours (log-scale).

## 6. Discussion and Limitations

What the results suggest.
Across path-dependent pricing (T1/T2) and portfolio control (T3), the Signature–RDE backbone improves both average accuracy and *tail calibration* (see Figure [5](https://arxiv.org/html/2510.10728v1#S5.F5 "Figure 5 ‣ 5. Experimental Details and Reproducibility Card ‣ Deep Signature and Neural RDE Methods for Path-Dependent Portfolio Optimization")).
We read this as evidence that (i) truncated log-signatures capture long-range path information more economically than ad-hoc rolling features or discrete RNNs (Feng et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib13)), and (ii) continuous-time hidden dynamics with adjoint memory mitigate exploding/vanishing gradients on long horizons (Morrill et al., [2021](https://arxiv.org/html/2510.10728v1#bib.bib24); Fang et al., [2023](https://arxiv.org/html/2510.10728v1#bib.bib12)).
In fully nonlinear control, coupling with a 2BSDE head reduces variance and stabilizes second-order quantities (Beck et al., [2019b](https://arxiv.org/html/2510.10728v1#bib.bib4); Pham et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib25)).

When (not) to use signatures.
Deeper truncations (m>4m\!>\!4) offer diminishing returns in RPE but can still help CVaRq\mathrm{CVaR}\_{q} when the payoff depends strongly on path extremes (e.g., barriers). For weakly path-dependent tasks, Markovian encoders (no-Sig ablation) may suffice and are slightly cheaper.

Choice of RDE vs. discrete RNNs.
Discrete RNNs are competitive at short horizons and small dd; our gains increase with horizon and dimension, where continuous-time propagation and step-size control matter. The log-ODE/CDE integrator order trades accuracy for speed; our defaults target stable medium-order schemes.

Risk-sensitive objectives.
The CVaR-tilted terminal loss (§3.3) consistently improves left tails without harming mean accuracy when η∈[1,3]\eta\!\in\![1,3] and q∈[0.95,0.99]q\!\in\![0.95,0.99]. Very aggressive tilts can over-fit rare trajectories; we therefore warm-start without the tilt and enable it after terminal error plateaus.

Second-order (Γ\Gamma) estimation.
Direct Γ\Gamma heads are flexible but noisy; Malliavin/antithetic targets reduce variance and NaNs, especially under high vol-of-vol. Autograd Hessians remain useful as diagnostics but can be brittle on long grids. A hybrid target (supervised Γ^\hat{\Gamma} + physics residual) works best in our HJB runs.

Limitations.
(i) *Truncation bias:* finite log-signature depth introduces bias for highly irregular paths; adaptive depth or learned truncation could help.
(ii) *Integrator sensitivity:* low-order solvers speed training but can under-resolve stiff residuals; implicit or adaptive solvers would be beneficial at higher cost.
(iii) *Boundaries & constraints:* reflecting/absorbing boundaries (e.g., barriers with rebates) can degrade gradient signals; coupling with penalty methods or boundary local time terms is future work.
(iv) *Model risk:* misspecified drift/vol dynamics propagate to BSDE targets; robust training (e.g., distributional shifts) remains open.
(v) *Theory gap:* our consistency sketch leverages universal approximation of signatures/RDEs, but finite-sample error bounds for PPDEs with risk-tilted losses are not yet sharp.

Relation to the two-way dialogue.
We instantiate both directions of the workshop theme:
*Finance →\rightarrow AI*—functional Itô/PPDE and Malliavin calculus shape the representation and variance-reduced estimators, improving interpretability and robustness (Dupire, [2019](https://arxiv.org/html/2510.10728v1#bib.bib10); Cont and Fournié, [2013](https://arxiv.org/html/2510.10728v1#bib.bib9); Ekren et al., [2011](https://arxiv.org/html/2510.10728v1#bib.bib11));
and *AI →\rightarrow Finance*—deep sequence-to-path models extend solvability of path-dependent PPDE/BSDE problems to d≫1d\!\gg\!1 with controllable memory/runtime via truncation depth and local windows, building on scalable BSDE training paradigms (Han et al., [2018](https://arxiv.org/html/2510.10728v1#bib.bib17); Huré et al., [2019](https://arxiv.org/html/2510.10728v1#bib.bib19); Beck et al., [2019a](https://arxiv.org/html/2510.10728v1#bib.bib2), [2021](https://arxiv.org/html/2510.10728v1#bib.bib3)).
In line with the workshop’s focus on stochastic control/mean-field viewpoints and risk-sensitive optimization, our CVaR tilt and 2BSDE/HJB structure align robustness with tail risk.

## 7. Conclusion

We introduced a focused deep BSDE solver for path-dependent finance that pairs truncated log-signatures with a Neural RDE backbone and, for fully nonlinear control, a 2BSDE head. Across Asian path-dependent pricing (50D–200D) and stochastic-volatility portfolio control, the solver achieves lower errors and tighter tail calibration at comparable parameter budgets. At d=200d{=}200, CVaR0.99\mathrm{CVaR}\_{0.99} drops to 9.8%9.8\% (vs. 12.0​–​13.1%12.0\text{--}13.1\%) alongside smaller HJB residuals, indicating improved second-order consistency at scale. The key levers—signature depth, RDE width, local window length, and Malliavin targets—offer a practical recipe for trading accuracy, variance, and runtime: depth governs path-information capacity; width and the second-order head balance bias vs. variance; the local window KK trades stability against wall-clock; and Malliavin targets reduce gradient noise without inflating bias.

Outlook. Natural extensions include (i) adaptive signature depth with error-controlled integrators; (ii) mean-field control and McKean–Vlasov couplings; (iii) diffusion-model priors for path augmentation; (iv) distributionally robust drivers for model risk; and (v) theory for finite-sample error bounds and stability of CVaR-tilted objectives in PPDE/2BSDE settings. We will release seeds, configs, and logs for full reproducibility and invite the community to stress-test the design across broader PPDE/HJB benchmarks.

## References

* (1)
* Beck et al. (2019a)

  Christian Beck, Sebastian Becker, Patrick Cheridito, Arnulf Jentzen, and Ariel Neufeld. 2019a.
  Deep splitting method for parabolic PDEs.
  *arXiv preprint arXiv:1907.03452* (2019).
* Beck et al. (2021)

  Christian Beck, Sebastian Becker, Patrick Cheridito, Arnulf Jentzen, and Ariel Neufeld. 2021.
  Deep Splitting Method for Parabolic PDEs.
  *SIAM Journal on Scientific Computing* 43, 5 (2021), A3135–A3154.
  [doi:10.1137/19M1297919](https://doi.org/10.1137/19M1297919)
* Beck et al. (2019b)

  Christian Beck, Weinan E, and Arnulf Jentzen. 2019b.
  Machine learning approximation algorithms for high-dimensional fully nonlinear partial differential equations and second-order backward stochastic differential equations.
  *Journal of Nonlinear Science* 29, 4 (2019), 1563–1619.
  [doi:10.1007/s00332-018-9513-7](https://doi.org/10.1007/s00332-018-9513-7)
* Bonnier et al. (2019)

  Pierre Bonnier, Luca Ganassali, Ilya Chevyrev, and Terry Lyons. 2019.
  Deep Signature Transforms.
  *arXiv preprint* (2019).
  arXiv:1905.08494
* Bouchard and Touzi (2004)

  Bruno Bouchard and Nizar Touzi. 2004.
  Discrete-time Approximation and Monte-Carlo Simulation of Backward Stochastic Differential Equations.
  *Stochastic Processes and their Applications* 111, 2 (2004), 175–206.
  [doi:10.1016/j.spa.2004.01.001](https://doi.org/10.1016/j.spa.2004.01.001)
* Chen et al. (2018)

  Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, and David Duvenaud. 2018.
  Neural Ordinary Differential Equations. In *Advances in Neural Information Processing Systems (NeurIPS)*.
* Chevyrev and Kormilitzin (2016)

  Ilya Chevyrev and Andrey Kormilitzin. 2016.
  A Primer on the Signature Method in Machine Learning.
  *arXiv preprint* (2016).
  arXiv:1603.03788
* Cont and Fournié (2013)

  Rama Cont and David-Antoine Fournié. 2013.
  Functional Itô calculus and stochastic integral representation of martingales.
  *Annals of Probability* 41, 1 (2013), 109–133.
  [doi:10.1214/11-AOP721](https://doi.org/10.1214/11-AOP721)
* Dupire (2019)

  Bruno Dupire. 2019.
  Functional Itô calculus.
  *Quantitative Finance* 19, 5 (2019), 721–729.
  [doi:10.1080/14697688.2019.1575974](https://doi.org/10.1080/14697688.2019.1575974)
  Original preprint 2009.
* Ekren et al. (2011)

  Ibrahim Ekren, Christian Keller, Nizar Touzi, and Jianfeng Zhang. 2011.
  On viscosity solutions of path dependent PDEs.
  *arXiv preprint arXiv:1109.5971* (2011).
* Fang et al. (2023)

  Bowen Fang, Hao Ni, and Yue Wu. 2023.
  A Neural RDE-based Model for Solving Path-Dependent PDEs.
  *arXiv preprint arXiv:2306.01123* (2023).
* Feng et al. (2023)

  Qi Feng, Man Luo, and Zhaoyu Zhang. 2023.
  Deep Signature FBSDE Algorithm.
  *Numerical Algebra, Control and Optimization* 13, 2 (2023), 500–522.
  [doi:10.3934/naco.2022028](https://doi.org/10.3934/naco.2022028)
* Fournié et al. (1999)

  E. Fournié, J.-M. Lasry, J. Lebuchoux, P.-L. Lions, and N. Touzi. 1999.
  Applications of Malliavin Calculus to Monte Carlo Methods in Finance.
  *Finance and Stochastics* 3, 4 (1999), 391–412.
  [doi:10.1007/s007800050068](https://doi.org/10.1007/s007800050068)
* Glasserman (2003)

  Paul Glasserman. 2003.
  *Monte Carlo Methods in Financial Engineering*.
  Springer.
  [doi:10.1007/978-0-387-21617-1](https://doi.org/10.1007/978-0-387-21617-1)
* Gobet et al. (2005)

  Emmanuel Gobet, Jean-Philippe Lemor, and Xavier Warin. 2005.
  A Regression-based Monte Carlo Method to Solve Backward Stochastic Differential Equations.
  *Annals of Applied Probability* 15, 3 (2005), 2172–2202.
  [doi:10.1214/105051605000000412](https://doi.org/10.1214/105051605000000412)
* Han et al. (2018)

  Jiequn Han, Arnulf Jentzen, and Weinan E. 2018.
  Solving high-dimensional partial differential equations using deep learning.
  *Proceedings of the National Academy of Sciences* 115, 34 (2018), 8505–8510.
  [doi:10.1073/pnas.1718942115](https://doi.org/10.1073/pnas.1718942115)
* Henry-Labordère et al. (2019)

  Pierre Henry-Labordère, Xiaolu Tan, and Nizar Touzi. 2019.
  Branching Diffusion Representation of Semilinear PDEs and Monte Carlo Estimation.
  *Annals of Applied Probability* 29, 1 (2019), 315–352.
  [doi:10.1214/18-AAP1424](https://doi.org/10.1214/18-AAP1424)
* Huré et al. (2019)

  Côme Huré, Huyên Pham, and Xavier Warin. 2019.
  Deep backward dynamic programming for high-dimensional semilinear PDEs.
  *arXiv preprint arXiv:1902.01599* (2019).
* Huré et al. (2020)

  Côme Huré, Huyên Pham, and Xavier Warin. 2020.
  Deep backward schemes for high-dimensional nonlinear PDEs.
  *Math. Comp.* 89, 324 (2020), 1547–1579.
  [doi:10.1090/mcom/3514](https://doi.org/10.1090/mcom/3514)
* Jacobson (1973)

  David H. Jacobson. 1973.
  Optimal Stochastic Linear Systems with Exponential Performance Criteria and Their Relation to Deterministic Differential Games.
  *IEEE Trans. Automat. Control* 18, 2 (1973), 124–131.
  [doi:10.1109/TAC.1973.1100267](https://doi.org/10.1109/TAC.1973.1100267)
* Kidger et al. (2020)

  Patrick Kidger, James Morrill, James Foster, and Terry Lyons. 2020.
  Neural Controlled Differential Equations for Irregular Time Series. In *Advances in Neural Information Processing Systems (NeurIPS)*.
* Lyons (1998)

  Terry J. Lyons. 1998.
  Differential Equations Driven by Rough Signals.
  *Revista Matemática Iberoamericana* 14, 2 (1998), 215–310.
* Morrill et al. (2021)

  James Morrill, Cristopher Salvi, Patrick Kidger, James Foster, and Terry Lyons. 2021.
  Neural Rough Differential Equations for Long Time Series. In *Proceedings of the 38th International Conference on Machine Learning (ICML)* *(PMLR, Vol. 139)*. 7829–7839.

  <https://proceedings.mlr.press/v139/morrill21b/morrill21b.pdf>
* Pham et al. (2019)

  Huyên Pham, Xavier Warin, and Maximilien Germain. 2019.
  Neural networks-based backward scheme for fully nonlinear PDEs.
  *arXiv preprint arXiv:1908.00412* (2019).
* Raissi et al. (2019)

  Maziar Raissi, Paris Perdikaris, and George E. Karniadakis. 2019.
  Physics-informed Neural Networks: A Deep Learning Framework for Solving Forward and Inverse Problems Involving Nonlinear Partial Differential Equations.
  *J. Comput. Phys.* 378 (2019), 686–707.
  [doi:10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)
* Reizenstein and Graham (2015)

  Jeremy Reizenstein and Ben Graham. 2015.
  The iisignature Library: Efficient Calculation of Iterated-integral Signatures and Log Signatures.
  *arXiv preprint* (2015).
  arXiv:1511.01865
* Rockafellar and Uryasev (2000)

  R. Tyrrell Rockafellar and Stanislav Uryasev. 2000.
  Optimization of Conditional Value-at-Risk.
  *Journal of Risk* 2, 3 (2000), 21–41.
* Saporito and Zhang (2021)

  Yuri F. Saporito and Zhaoyu Zhang. 2021.
  Path-Dependent Deep Galerkin Method: A Neural Network Approach to Solve Path-Dependent Partial Differential Equations.
  *SIAM Journal on Financial Mathematics* 12, 3 (2021), 912–940.
  [doi:10.1137/20M1329597](https://doi.org/10.1137/20M1329597)
* Sirignano and Spiliopoulos (2018)

  Justin Sirignano and Konstantinos Spiliopoulos. 2018.
  DGM: A Deep Learning Algorithm for Solving Partial Differential Equations.
  *J. Comput. Phys.* 375 (2018), 1339–1364.
  [doi:10.1016/j.jcp.2018.08.029](https://doi.org/10.1016/j.jcp.2018.08.029)
* Soner et al. (2012)

  H. Mete Soner, Nizar Touzi, and Jianfeng Zhang. 2012.
  Wellposedness of Second Order Backward SDEs.
  *Probability Theory and Related Fields* 153, 1-2 (2012), 149–190.
  [doi:10.1007/s00440-011-0342-y](https://doi.org/10.1007/s00440-011-0342-y)