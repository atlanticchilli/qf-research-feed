---
authors:
- Toshiaki Yamanaka
doc_id: arxiv:2512.04704v1
family_id: arxiv:2512.04704
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Coordinated Mean-Field Control for Systemic Risk
url_abs: http://arxiv.org/abs/2512.04704v1
url_html: https://arxiv.org/html/2512.04704v1
venue: arXiv q-fin
version: 1
year: 2025
---


Toshiaki Yamanaka
Whiting School of Engineering, Johns Hopkins University, Baltimore, MD, USA. Email: [tyamana1@jhu.edu](mailto:tyamana1@jhu.edu)

(December 4, 2025)

###### Abstract

We develop a robust linear-quadratic mean-field control framework for systemic risk under model uncertainty, in which a central bank jointly optimizes interest rate policy and supervisory monitoring intensity against adversarial distortions. Our model features multiple policy instruments with interactive dynamics, implemented via a variance weight that depends on the policy rate, generating coupling effects absent in single-instrument models. We establish viscosity solutions for the associated HJB–Isaacs equation, prove uniqueness via comparison principles, and provide verification theorems. The linear-quadratic structure yields explicit feedback controls derived from a coupled Riccati system, preserving analytical tractability despite adversarial uncertainty. Simulations reveal distinct loss-of-control regimes driven by robustness-breakdown and control saturation, alongside a pronounced asymmetry in sensitivity between the mean and variance channels. These findings demonstrate the importance of instrument complementarity in systemic risk modeling and control.

Keywords: Mean-field control, linear-quadratic mean-field control, systemic risk, central banking

Mathematics Subject Classification: 49N10, 49N80, 93E20

## 1 Introduction

##### Motivation.

In this paper, we study systemic risk by integrating insights from robust control and mean-field theory. Modern CBs (central banks) frequently operate as both *liquidity providers* and *prudential supervisors*. However, as detailed below, prior studies in financial mathematics do not incorporate multiple policy measures within a single robust control framework, and our work proposes a unified framework to address this limitation.

While the full model and dynamics are presented in [section 2](https://arxiv.org/html/2512.04704v1#S2 "2 Model and dynamics ‣ Coordinated Mean-Field Control for Systemic Risk"), we begin by briefly introducing our model of multiple CB policy measures. First, CBs control interest rates via a policy rate utu\_{t}, a common component of banks’ funding costs. When utu\_{t} rises, maintaining liquidity becomes more expensive system-wide. We capture this by letting the variance weight depend on the policy rate, replacing the constant w2w\_{2} with w2​(ut)w\_{2}(u\_{t}) in the term w2​(ut)​vtw\_{2}(u\_{t})v\_{t}, where w2​(ut)=w¯2+κ​utw\_{2}(u\_{t})=\bar{w}\_{2}+\kappa u\_{t}, and w¯2+κ​umin>0\bar{w}\_{2}+\kappa u\_{\min}>0 ensures uniform positivity. w¯2\bar{w}\_{2} is the baseline penalty weight on variance.

Second, CBs allocate supervisory resources via a monitoring intensity πt\pi\_{t}. Greater scrutiny mitigates systemic dispersion but entails administrative costs captured by R​πt2R\pi\_{t}^{2}. Its effect on variance enters the variance dynamics via −χ​πt-\chi\pi\_{t} in v˙t\dot{v}\_{t}. Within our robust LQ (linear-quadratic)-MFC (mean-field control) framework with adversarial distortions bounded by relative-entropy (Kullback–Leibler [KL] [[37](https://arxiv.org/html/2512.04704v1#bib.bib37)]) divergence, the CB jointly optimizes utu\_{t} and πt\pi\_{t} to minimize a quadratic objective in the cross-sectional moments (mt,vt)(m\_{t},v\_{t}), subject to admissible bounds ut∈[umin,umax]u\_{t}\in[u\_{\min},u\_{\max}] and πt∈[0,πmax]\pi\_{t}\in[0,\pi\_{\max}].

This structure aligns with the institutional practice at the Federal Reserve, the ECB (European Central Bank), and the BoE (Bank of England), while preserving analytical tractability through linear dynamics, quadratic costs, and closed-form linear feedback. Both monetary and prudential policies are grounded in law,111Federal Reserve Act, Sections 2A and 21(4); Statute of the European System of Central Banks and of the European Central Bank, Articles 2, 18, and 25.2; Bank of England Act 1998, Sections 11 and 2A(1). and our model is consistent with this institutional foundation.

##### Related literature.

Financial contagion and systemic risk have been extensively studied in financial mathematics.222Closely related studies in economics include Freixas, Parigi, and Rochet [[26](https://arxiv.org/html/2512.04704v1#bib.bib26)], who analyze systemic risk in an interbank market and CB liquidity provision. Gai and Kapadia [[27](https://arxiv.org/html/2512.04704v1#bib.bib27)] develop a model of contagion in financial networks and identify phase transitions. One line of research focuses on the *network structure* of the financial system. Fouque and Ichiba [[25](https://arxiv.org/html/2512.04704v1#bib.bib25)] proposed a diffusion model of interbank lending that captures how banks’ lending preferences can lead to multiple defaults. Cont, Moussa, and Santos [[18](https://arxiv.org/html/2512.04704v1#bib.bib18)] introduced a metric for the systemic importance of financial institutions—the Contagion Index—to quantify contagion and systemic risk in a network of financial institutions. Amini, Cont, and Minca [[1](https://arxiv.org/html/2512.04704v1#bib.bib1)] analyzed distress propagation in large financial networks and established rigorous asymptotic results for the magnitude of contagion. Amini, Filipović, and Minca [[2](https://arxiv.org/html/2512.04704v1#bib.bib2)] studied how clearing all contracts through a central node affects a financial network.

Another major line of research adopts *mean-field* models. The general theory of mean-field systems was pioneered by Lasry and Lions [[38](https://arxiv.org/html/2512.04704v1#bib.bib38)] and by Huang, Malhamé, and Caines [[34](https://arxiv.org/html/2512.04704v1#bib.bib34)]. Comprehensive and foundational treatments are given in Bensoussan, Frehse, and Yam [[8](https://arxiv.org/html/2512.04704v1#bib.bib8)], Carmona [[12](https://arxiv.org/html/2512.04704v1#bib.bib12)], and Carmona and Delarue [[14](https://arxiv.org/html/2512.04704v1#bib.bib14), [15](https://arxiv.org/html/2512.04704v1#bib.bib15)].333Furthermore, linear-quadratic-Gaussian games with one major player interacting with a large number of minor players were analyzed by Huang [[33](https://arxiv.org/html/2512.04704v1#bib.bib33)]. Mean-field games between a dominating player and representative agents were studied by Bensoussan, Chau, and Yam [[9](https://arxiv.org/html/2512.04704v1#bib.bib9)]. Within the context of financial systemic risk, various studies have applied the mean-field framework. Carmona, Fouque, and Sun [[16](https://arxiv.org/html/2512.04704v1#bib.bib16)] proposed an MFG (mean-field game) model of interbank lending and borrowing, formulating the evolution of banks’ log-monetary reserves as a system of diffusion processes coupled through their drifts. Bo and Capponi [[11](https://arxiv.org/html/2512.04704v1#bib.bib11)] developed a mean-field model where banks are subject to sudden shocks affecting their monetary reserves. Sun [[47](https://arxiv.org/html/2512.04704v1#bib.bib47)] proposed an MFG model with an LQ cost structure, in which the CB acts as a central deposit institution. Hambly and Søjmark [[29](https://arxiv.org/html/2512.04704v1#bib.bib29)] introduced a dynamic mean-field model for systemic risk in large financial systems, where the mean-field limit is characterized by a nonlinear SPDE (stochastic PDE). Feinstein and Søjmark [[23](https://arxiv.org/html/2512.04704v1#bib.bib23)] proposed a dynamic contagion model with endogenous early defaults for a finite set of banks, reformulated as a stochastic particle system leading to a mean-field problem. Cuchiero, Reisinger, and Rigger [[21](https://arxiv.org/html/2512.04704v1#bib.bib21)] studied an MFC problem and computed the CB’s optimal strategy via a PG (policy gradient) method, where the CB controls the rate of capital injections to distressed institutions in order to limit defaults. Bayraktar, Guo, Tang, and Zhang [[6](https://arxiv.org/html/2512.04704v1#bib.bib6)] studied the problem of capital provision arising from systemic risk in a financial network modeled by SDEs, adopting a mean-field particle system approach.

Furthermore, Minca and Sulem [[40](https://arxiv.org/html/2512.04704v1#bib.bib40)] formulated an optimization problem for a government with a constrained budget seeking to maximize the total net worth of a financial system of banks and their creditors. Cont, Guo, and Xu [[19](https://arxiv.org/html/2512.04704v1#bib.bib19)] analyzed stochastic differential games involving singular controls, motivated by a dynamic model of interbank lending with benchmark rates. Veraart and Aldasoro [[48](https://arxiv.org/html/2512.04704v1#bib.bib48)] developed a framework for modeling risk and quantifying payment shortfalls in cleared markets with multiple central counterparties.

Comprehensive expositions of stochastic/optimal controls include Yong and Zhou [[50](https://arxiv.org/html/2512.04704v1#bib.bib50)], Fleming and Soner [[24](https://arxiv.org/html/2512.04704v1#bib.bib24)], Hansen and Sargent [[31](https://arxiv.org/html/2512.04704v1#bib.bib31)], Pham [[42](https://arxiv.org/html/2512.04704v1#bib.bib42)], and Bensoussan [[7](https://arxiv.org/html/2512.04704v1#bib.bib7)]. The LQ-MFC problem was considered by Carmona and Delarue ([[14](https://arxiv.org/html/2512.04704v1#bib.bib14)], Subsection 6.7.1). The LQ-MFC framework has been widely studied due to its analytical tractability and broad range of applications (*e.g.*, Basei and Pham [[4](https://arxiv.org/html/2512.04704v1#bib.bib4)] and Yong [[49](https://arxiv.org/html/2512.04704v1#bib.bib49)]). In the context of systemic risk, however, applications of the LQ-MFC framework to monetary policy transmission in banking remain largely unexplored. In a recent preprint, De Crescenzo, De Feo, and Pham [[22](https://arxiv.org/html/2512.04704v1#bib.bib22)] introduced an LQ non-exchangeable MFC problem that generalizes the LQ-MFC framework by incorporating heterogeneous interactions.

##### Scope and research positioning.

We focus on the aggregate liquidity management aspect of systemic risk, where a CB coordinates system-wide liquidity through multiple policy instruments. Our framework captures how common shocks and cross-sectional dispersion in liquidity create systemic vulnerabilities that require coordinated policy responses. The mean-reversion term −β​(Lti−mt)-\beta(L\_{t}^{i}-m\_{t}) in our model represents interbank adjustment mechanisms, and the variance dynamics capture heterogeneous stress across the banking sector.

##### Our contributions.

Our paper makes three primary contributions to the literature.

1. 1.

   We integrate robust control against model uncertainty into the LQ-MFC framework for systemic risk, allowing an adversary to distort the drift (θ\theta) and variance dynamics (ξ\xi) to capture worst-case model misspecification. We establish viscosity solutions for the resulting HJBI (HJB–Isaacs) equation and prove verification theorems that connect PDE solutions to optimal strategies.
2. 2.

   Unlike prior studies in financial mathematics, we model the joint optimization of interest rate policy and supervisory monitoring intensity with interactive dynamics via state-dependent variance weight w2​(ut)=w¯2+κ​utw\_{2}(u\_{t})=\bar{w}\_{2}+\kappa u\_{t}. This coupling, absent in single-instrument models, captures heterogeneous transmission mechanisms and institutional realities.
3. 3.

   Our analysis reveals complementarity between interest rate and monitoring policies under model uncertainty. Simulations show phase transitions from controllable to uncontrollable regimes, with asymmetric burdens on monetary versus supervisory tools—a phenomenon critical under model uncertainty.

The LQ structure preserves analytical tractability, yielding explicit Riccati equations and closed-form feedback policies that remain computationally feasible even with control bounds and state constraints. Owing to this analytical tractability, our model provides a tractable baseline that admits various meaningful extensions, as discussed in [section 5](https://arxiv.org/html/2512.04704v1#S5 "5 Discussion ‣ Coordinated Mean-Field Control for Systemic Risk").

##### Comparison to prior work.

While Sun [[47](https://arxiv.org/html/2512.04704v1#bib.bib47)] and Cuchiero, Reisinger, and Rigger [[21](https://arxiv.org/html/2512.04704v1#bib.bib21)] are related to our setting, our framework uniquely captures how a CB’s policy rate influences liquidity dispersion through the coupling parameter κ>0\kappa>0, providing a direct channel from monetary policy to systemic stability. Unlike De Crescenzo, De Feo, and Pham [[22](https://arxiv.org/html/2512.04704v1#bib.bib22)], our approach captures heterogeneous policy transmission through κ>0\kappa>0 within an exchangeable framework.

##### Outline of the paper.

The remainder of this paper is organized as follows. [Section 2](https://arxiv.org/html/2512.04704v1#S2 "2 Model and dynamics ‣ Coordinated Mean-Field Control for Systemic Risk") introduces the LQ-MFC framework with multiple policy instruments and robust control against adversarial distortions. [Section 3](https://arxiv.org/html/2512.04704v1#S3 "3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") establishes the theoretical foundations, including viscosity characterization, verification theorems, and the quadratic ansatz with its associated Riccati system. [Section 4](https://arxiv.org/html/2512.04704v1#S4 "4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") presents a comprehensive numerical analysis examining adversary strength, parameter sensitivity, and loss-of-control regimes. [Section 5](https://arxiv.org/html/2512.04704v1#S5 "5 Discussion ‣ Coordinated Mean-Field Control for Systemic Risk") discusses limitations and extensions, and [section 6](https://arxiv.org/html/2512.04704v1#S6 "6 Conclusion ‣ Coordinated Mean-Field Control for Systemic Risk") concludes. Technical proofs and propagation-of-chaos analysis are provided in the appendices.

## 2 Model and dynamics

##### Model setting.

Let LtiL\_{t}^{i} denote the liquidity gap of bank i∈[0,1]i\in[0,1], a continuum of agents. The CB chooses a policy rate utu\_{t} and a monitoring intensity πt\pi\_{t} from admissible sets ut∈𝒰:=[umin,umax]u\_{t}\in\mathcal{U}:=[u\_{\min},u\_{\max}] and πt∈𝒫:=[0,πmax]\pi\_{t}\in\mathcal{P}:=[0,\pi\_{\max}]. Controls (u,π)(u,\pi) and adversarial distortions (θ,ξ)(\theta,\xi) are progressively measurable and square-integrable. Denote the cross-sectional mean and variance by mt:=𝔼​[Lti]m\_{t}:=\mathbb{E}[L\_{t}^{i}] and vt:=Var​[Lti]v\_{t}:=\mathrm{Var}[L\_{t}^{i}]. Individual dynamics follow a linear McKean–Vlasov SDE with common and idiosyncratic Brownian motions (Bt,Wti)(B\_{t},W\_{t}^{i}):

|  |  |  |
| --- | --- | --- |
|  | d​Lti=[−β​(Lti−mt)+η​ut+θt]​d​t+σL​d​Wti+σc​d​Bt,dL\_{t}^{i}=\bigl[-\beta\,(L\_{t}^{i}-m\_{t})+\eta\,u\_{t}+\theta\_{t}\bigr]dt\,+\,\sigma\_{L}\,dW\_{t}^{i}\,+\,\sigma\_{c}\,dB\_{t}, |  |

where β>0\beta>0 captures interbank netting effects and η>0\eta>0 is the pass-through from utu\_{t} to funding costs. The term θt\theta\_{t} is a worst-case drift distortion chosen by an adversary.

###### Remark 2.1 (mean reversion mechanism).

The parameter β>0\beta>0 in the drift term −β​(Lti−mt)-\beta(L\_{t}^{i}-m\_{t}) captures the mean-reverting nature of liquidity dynamics via interbank netting and clearing mechanisms. This term generates a process in which deviations from the mean mtm\_{t} decay at rate β\beta. When Lti>mtL\_{t}^{i}>m\_{t} (excess liquidity), the negative drift pulls the bank’s position downward, while Lti<mtL\_{t}^{i}<m\_{t} (liquidity shortage) induces an upward drift. A higher β\beta represents more efficient interbank markets with faster redistribution of liquidity imbalances, while a lower β\beta reflects frictions in interbank interactions.

To derive the aggregate dynamics, we take expectations of d​LtidL\_{t}^{i}, which yields m˙t\dot{m}\_{t} because the linear mean-reversion terms cancel at the aggregate level. The variance dynamics follow from the model specification:

|  |  |  |
| --- | --- | --- |
|  | m˙t=η​ut+θt,v˙t=−2​β​vt+σL2+σc2+ξt−χ​πt,\dot{m}\_{t}\;=\;\eta\,u\_{t}+\theta\_{t},\quad\dot{v}\_{t}\;=\;-2\beta\,v\_{t}+\sigma\_{L}^{2}+\sigma\_{c}^{2}+\xi\_{t}-\chi\,\pi\_{t}, |  |

where σL2+σc2\sigma\_{L}^{2}+\sigma\_{c}^{2} is the effective variance forcing (Remark [2.3](https://arxiv.org/html/2512.04704v1#S2.Thmtheorem3 "Remark 2.3 (variance dynamics and common noise). ‣ Model setting. ‣ 2 Model and dynamics ‣ Coordinated Mean-Field Control for Systemic Risk")), ξt\xi\_{t} is a worst-case dispersion distortion, and χ>0\chi>0 measures the effectiveness of monitoring on variance.

###### Remark 2.2 (model specification).

We adopt a specification m˙t=η​ut+θt\dot{m}\_{t}\;=\;\eta\,u\_{t}+\theta\_{t} for the mean dynamics. This modeling choice preserves the LQ structure necessary for deriving closed-form solutions. It allows us to separate and identify two distinct channels of monetary policy transmission: the direct effect on mean liquidity through η\eta and the heterogeneous effect on liquidity dispersion through the variance penalty coupling w2​(ut)=w¯2+κ​utw\_{2}(u\_{t})=\bar{w}\_{2}+\kappa u\_{t}. While richer dynamics may be appealing, they may obscure these transmission mechanisms and sacrifice analytical tractability.

###### Remark 2.3 (variance dynamics and common noise).

While the underlying system includes common noise σc​d​Bt\sigma\_{c}dB\_{t}, standard aggregation implies that this term cancels in the cross-sectional dynamics d​(Lti−mt)d(L\_{t}^{i}-m\_{t}), leaving only idiosyncratic volatility σL\sigma\_{L} in the variance drift. We retain σc2\sigma\_{c}^{2} in the variance dynamics v˙t\dot{v}\_{t} as a conservative modeling choice that accounts for potential additional dispersion channels, such as heterogeneous bank sensitivities to common shocks, within the tractable LQ framework.

Under the parameter restriction σL2+σc2≥χ​πmax\sigma\_{L}^{2}+\sigma\_{c}^{2}\geq\chi\pi\_{\max}, the variance remains non-negative. This condition suffices because the optimal adversarial distortion ξt∗=2​λv​∂vV≥0\xi\_{t}^{\*}=2\lambda\_{v}\partial\_{v}V\geq 0 increases variance, so the binding constraint for non-negativity at v=0v=0 is maximum monitoring with no adversarial pressure. If vtv\_{t} reaches zero, the drift σL2+σc2+ξt−χ​πt≥0\sigma\_{L}^{2}+\sigma\_{c}^{2}+\xi\_{t}-\chi\pi\_{t}\geq 0 ensures it cannot become negative. The common noise BtB\_{t} implies a conditional McKean–Vlasov limit, where propagation-of-chaos and limit statements are understood conditional on the common filtration (see Appendix [A](https://arxiv.org/html/2512.04704v1#A1 "Appendix A Propagation-of-Chaos for the N-bank system ‣ Coordinated Mean-Field Control for Systemic Risk")). While we solve the problem at the level of deterministic moment dynamics (mt,vt)(m\_{t},v\_{t}), Appendix [A](https://arxiv.org/html/2512.04704v1#A1 "Appendix A Propagation-of-Chaos for the N-bank system ‣ Coordinated Mean-Field Control for Systemic Risk") shows that, as N→∞N\to\infty, the empirical mean and variance of the stochastic NN-bank system converge to (mt,vt)(m\_{t},v\_{t}).

The CB’s objective is to stabilize the system by minimizing the aggregate liquidity gap and its dispersion while limiting control efforts. Specifically, the CB minimizes a quadratic mean-field objective composed of running penalties on the squared mean gap mt2m\_{t}^{2}, the cross-sectional variance vtv\_{t}, and quadratic costs associated with monitoring πt2\pi\_{t}^{2}, and policy rate adjustments ut2u\_{t}^{2}. We include a terminal cost Gm​mT2+Gv​vTG\_{m}m\_{T}^{2}+G\_{v}v\_{T} to ensure the system is steered toward stability by the terminal time TT, penalizing any remaining aggregate imbalance mTm\_{T} or dispersion vTv\_{T}. To capture the interaction between monetary policy and variance vtv\_{t}, we introduce a variance weight w2​(ut)w\_{2}(u\_{t}) that depends on the policy rate:

|  |  |  |
| --- | --- | --- |
|  | J​(u,π)=∫0T(w1​mt2+w2​(ut)​vt+R​πt2+Ru​ut2)​𝑑t+Gm​mT2+Gv​vT,w2​(ut)=w¯2+κ​ut,J(u,\pi)=\int\_{0}^{T}\Big(w\_{1}m\_{t}^{2}+w\_{2}(u\_{t})v\_{t}+R\pi\_{t}^{2}+R\_{u}u\_{t}^{2}\Big)dt+G\_{m}m\_{T}^{2}+G\_{v}v\_{T},\quad w\_{2}(u\_{t})=\bar{w}\_{2}+\kappa u\_{t}, |  |

with w¯2>0\bar{w}\_{2}>0 and κ>0\kappa>0. We assume Ru>0R\_{u}>0, R>0R>0, and w¯2+κ​umin>0\bar{w}\_{2}+\kappa\,u\_{\min}>0 so that w2​(ut)w\_{2}(u\_{t}) is uniformly positive on 𝒰\mathcal{U}.

###### Remark 2.4 (terminal variance and cost structure).

Under the linear terminal penalty Gv​vTG\_{v}v\_{T}, the variance vTv\_{T} settles at a non-zero optimal equilibrium where the marginal cost of further variance reduction equals its marginal benefit against adversarial pressure ξ\xi and system noise σL2+σc2\sigma\_{L}^{2}+\sigma\_{c}^{2}. We adopt a linear penalty on vTv\_{T} because variance already represents the second moment of liquidity gaps (vt=𝔼​[(Lti−mt)2]v\_{t}=\mathbb{E}[(L\_{t}^{i}-m\_{t})^{2}], the cross-sectional variance). Thus, a linear penalty on vtv\_{t} constitutes a quadratic penalty on the underlying bank positions, preserving the LQ structure. A quadratic penalty Gv​vT2G\_{v}v\_{T}^{2} would penalize fourth moments, yielding vanishing marginal incentives near zero (∂v(v2)=2​v→0\partial\_{v}(v^{2})=2v\to 0). Our numerical experiments confirm that this quadratic penalty leads to higher terminal variance vTv\_{T} due to these weakened control incentives.

###### Remark 2.5 (motivation for κ>0\kappa>0).

The coupling term w2​(ut)=w¯2+κ​utw\_{2}(u\_{t})=\bar{w}\_{2}+\kappa u\_{t} captures the state-dependent nature of variance penalties, reflecting that monetary tightening affects banks heterogeneously based on their liquidity positions. In a general control setting, the cost of cross-sectional dispersion may depend on the aggregate policy stance, represented by a general weight function 𝒲​(ut)\mathcal{W}(u\_{t}). We assume 𝒲\mathcal{W} is smooth and admits a Taylor expansion around the neutral rate u∗=0u^{\*}=0: 𝒲​(ut)≈𝒲​(0)+𝒲′​(0)​ut+𝒪​(ut2).\mathcal{W}(u\_{t})\approx\mathcal{W}(0)+\mathcal{W}^{\prime}(0)u\_{t}+\mathcal{O}(u\_{t}^{2}). Identifying w¯2=𝒲​(0)\bar{w}\_{2}=\mathcal{W}(0) and κ=𝒲′​(0)\kappa=\mathcal{W}^{\prime}(0), our specification represents the first-order truncation of this general dependency. The assumption κ>0\kappa>0 implies that the marginal cost of dispersion increases with the policy rate (a tightening regime amplifies the penalty on heterogeneity). Retaining only the linear term preserves the LQ structure of the problem, allowing for the explicit Riccati characterization derived in [section 3.2.3](https://arxiv.org/html/2512.04704v1#S3.SS2.SSS3 "3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Including quadratic or higher-order terms in the weight would render the Hamiltonian non-quadratic in uu, destroying the Riccati property and requiring numerical methods that obscure the analytical characterization of optimal policy.

##### Robustness.

Robustness is imposed via a relative-entropy budget on the adversary. Nature selects (θt,ξt)(\theta\_{t},\xi\_{t}) subject to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T(θt2λm+ξt2λv)​𝑑t≤ρ,\int\_{0}^{T}\left(\frac{\theta\_{t}^{2}}{\lambda\_{m}}+\frac{\xi\_{t}^{2}}{\lambda\_{v}}\right)dt\;\leq\;\rho, |  | (1) |

with λm,λv>0\lambda\_{m},\lambda\_{v}>0 and budget ρ>0\rho>0. By convex duality, this constrained formulation is equivalent to a penalized (Lagrangian) formulation in which the running cost includes terms −θt24​λm−ξt24​λv-\frac{\theta\_{t}^{2}}{4\lambda\_{m}}-\frac{\xi\_{t}^{2}}{4\lambda\_{v}}, with λm\lambda\_{m} and λv\lambda\_{v} acting as Lagrange multipliers. We adopt this penalized formulation henceforth. The HJBI equation includes convex penalties that bound worst-case distortions and ensure well-posed Riccati equations. These relative-entropy penalties yield bounded linear worst-case feedback and ensure the Isaacs condition.

##### Value function and Riccati system.

The coupling term κ​ut​vt\kappa u\_{t}v\_{t} in the cost functional (through w2​(ut)=w¯2+κ​utw\_{2}(u\_{t})=\bar{w}\_{2}+\kappa u\_{t}) necessitates a full quadratic ansatz in both mm and vv, including cross-terms. With terminal cost Gm​mT2+Gv​vTG\_{m}m\_{T}^{2}+G\_{v}v\_{T}, we seek a value function of the form given in [Eq. 7](https://arxiv.org/html/2512.04704v1#S3.E7 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), and the HJBI reduces to a coupled system of Riccati ODEs in [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").

##### Feedback laws.

We write ∂mV\partial\_{m}V and ∂vV\partial\_{v}V for the partial derivatives of VV with respect to mm and vv, respectively. Solving the HJBI (derived via the Isaacs Hamiltonian in [section 3.1.2](https://arxiv.org/html/2512.04704v1#S3.SS1.SSS2 "3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")) yields linear feedback laws, implemented with projection onto admissible sets. Specifically, minimizing the Isaacs Hamiltonian H​(x,∇V)H(x,\nabla V) with respect to the controls uu and π\pi (before projection) yields the first-order conditions 2​Ru​u+(η​∂mV+κ​v)=02R\_{u}u+(\eta\partial\_{m}V+\kappa v)=0 and 2​R​π−χ​∂vV=0.2R\pi-\chi\partial\_{v}V=0. Solving these yields the linear feedback laws:

|  |  |  |
| --- | --- | --- |
|  | utfb=−κ​vt+η​∂mV2​Ru,πtfb=χ​∂vV2​R.u\_{t}^{\mathrm{fb}}=-\dfrac{\kappa v\_{t}+\eta\partial\_{m}V}{2R\_{u}},\qquad\pi\_{t}^{\mathrm{fb}}\;=\;\frac{\chi\,\partial\_{v}V}{2R}. |  |

The projected controls are:

|  |  |  |
| --- | --- | --- |
|  | ut∗=Π[umin,umax]​(utfb),πt∗=Π[0,πmax]​(πtfb).u\_{t}^{\*}\;=\;\Pi\_{[u\_{\min},u\_{\max}]}\!\bigl(u\_{t}^{\mathrm{fb}}\bigr),\qquad\pi\_{t}^{\*}\;=\;\Pi\_{[0,\pi\_{\max}]}\!\bigl(\pi\_{t}^{\mathrm{fb}}\bigr). |  |

Worst-case distortions are linear in value gradients and bounded:

|  |  |  |
| --- | --- | --- |
|  | θt∗= 2​λm​∂mV,ξt∗= 2​λv​∂vV.\theta\_{t}^{\*}\;=\;2\,\lambda\_{m}\,\partial\_{m}V,\qquad\xi\_{t}^{\*}\;=\;2\,\lambda\_{v}\,\partial\_{v}V. |  |

Comparative statics are piecewise-smooth with potential kinks at projection boundaries. For simulation, we restrict parameters to the region where the Riccati system admits a bounded solution.

###### Remark 2.6.

We adopt the penalized robust-control formulation, which is dual to a relative-entropy budget and implies that the Isaacs condition holds under our convexity/concavity assumptions. Parameters satisfy R>0R>0, Ru>0R\_{u}>0, and minu∈[umin,umax]⁡(w¯2+κ​u)>0\min\_{u\in[u\_{\min},u\_{\max}]}(\bar{w}\_{2}+\kappa u)>0, so the variance weight is uniformly positive. Interior feedback is implemented via projection onto admissible sets, and comparative statics are evaluated away from switching times.

## 3 Theoretical foundations

This section develops a framework linking the control formulation to solution concepts and implementable policies for robust mean-field models. We establish the DPP (dynamic programming principle, see, *e.g.,* Fleming and Soner [[24](https://arxiv.org/html/2512.04704v1#bib.bib24)]) and its associated HJBI equation. We then prove existence and uniqueness of viscosity solutions under regularity assumptions. A comparison principle yields uniqueness, and a verification theorem translates PDE solutions into optimal strategies, together providing a well-posed and operational framework for robust control.

Building on the general theory, we specialize to a robust LQ-MFC setting. Via square completion, we obtain explicit Isaacs and saddle-point structures and a quadratic value function, verified by a Riccati system. We derive closed-form feedback policies and conclude with comparative statics and robustness loss bounds that quantify sensitivity to parameters and misspecification (the details are provided in Appendix [C](https://arxiv.org/html/2512.04704v1#A3 "Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk")). Collectively, these results deliver both the theoretical guarantees and practical tools needed to analyze and implement robust policies in large-scale mean-field environments.

### 3.1 Viscosity solutions and the HJBI equation

In this subsection, we establish the viscosity characterization of the robust HJBI equation.

#### 3.1.1 Model primitives and admissible inputs

As introduced in [section 2](https://arxiv.org/html/2512.04704v1#S2 "2 Model and dynamics ‣ Coordinated Mean-Field Control for Systemic Risk"), let Xt=(mt,vt)∈ℝ×ℝ+X\_{t}=(m\_{t},v\_{t})\in\mathbb{R}\times\mathbb{R}\_{+} denote the moment state, with absolutely continuous dynamics X˙t=b​(Xt,ut,πt,θt,ξt)\dot{X}\_{t}=b(X\_{t},u\_{t},\pi\_{t},\theta\_{t},\xi\_{t}), where the drift function b:(ℝ×ℝ+)×𝒰×𝒫×ℝ2→ℝ2b:(\mathbb{R}\times\mathbb{R}\_{+})\times\mathcal{U}\times\mathcal{P}\times\mathbb{R}^{2}\to\mathbb{R}^{2} is defined by b​(x,u,π,θ,ξ):=(η​u+θ,−2​β​v+σL2+σc2+ξ−χ​π),b(x,u,\pi,\theta,\xi):=\big(\eta u+\theta,\;-2\beta v+\sigma\_{L}^{2}+\sigma\_{c}^{2}+\xi-\chi\pi\big), where x=(m,v)x=(m,v), u∈𝒰=[umin,umax]u\in\mathcal{U}=[u\_{\min},u\_{\max}], and π∈𝒫=[0,πmax]\pi\in\mathcal{P}=[0,\pi\_{\max}] are progressively measurable controls, while (θ,ξ)(\theta,\xi) are progressively measurable distortions.

The penalized running cost function is:

|  |  |  |
| --- | --- | --- |
|  | ℓ​(m,v,u,π,θ,ξ):=w1​m2+w2​(u)​v+R​π2+Ru​u2−θ24​λm−ξ24​λv,\ell(m,v,u,\pi,\theta,\xi):=w\_{1}m^{2}+w\_{2}(u)\,v+R\,\pi^{2}+R\_{u}\,u^{2}-\tfrac{\theta^{2}}{4\lambda\_{m}}-\tfrac{\xi^{2}}{4\lambda\_{v}}, |  |

with terminal cost function g​(x):=Gm​m2+Gv​vg(x):=G\_{m}m^{2}+G\_{v}v, where x=(m,v)x=(m,v) and w2​(u)=w¯2+κ​uw\_{2}(u)=\bar{w}\_{2}+\kappa u.

###### Assumption 3.1 (standing assumptions).

We assume the following.

1. 1.

   𝒰,𝒫\mathcal{U},\mathcal{P} are compact intervals. The processes ut,πt,θt,u\_{t},\pi\_{t},\theta\_{t}, and ξt\xi\_{t} are progressively measurable and square-integrable.
2. 2.

   For any admissible inputs (ut,πt,θt,ξt)(u\_{t},\pi\_{t},\theta\_{t},\xi\_{t}), the controlled ODE X˙s=b​(Xs,us,πs,θs,ξs)\dot{X}\_{s}=b\left(X\_{s},u\_{s},\pi\_{s},\theta\_{s},\xi\_{s}\right) with initial condition Xt=xX\_{t}=x admits a unique absolutely continuous solution on [t,T][t,T]. Moreover, the solution has at most linear growth in the state.
3. 3.

   The functions ℓ\ell and gg are continuous in all their arguments. The running cost function ℓ\ell is convex in (u,π)(u,\pi) and concave in (θ,ξ)(\theta,\xi). The map w2w\_{2} is continuous in uu.
4. 4.

   The admissible inputs (ut,πt,θt,ξt)(u\_{t},\pi\_{t},\theta\_{t},\xi\_{t}) are closed under concatenation at stopping times, and the cost functional is additive over time, ensuring the DPP.

Based on the framework of Petersen, James, and Dupuis [[41](https://arxiv.org/html/2512.04704v1#bib.bib41)], we adopt the following formulation.

###### Definition 3.2 (lower and upper values).

For (t,x)∈[0,T]×(ℝ×ℝ+)(t,x)\in[0,T]\times(\mathbb{R}\times\mathbb{R}\_{+}), define the lower value

|  |  |  |
| --- | --- | --- |
|  | V​(t,x):=inf(u,π)sup(θ,ξ)[∫tTℓ​(Xs,us,πs,θs,ξs)​𝑑s+g​(XT)],V(t,x):=\inf\_{(u,\pi)}\sup\_{(\theta,\xi)}\!\left[\int\_{t}^{T}\ell\!\left(X\_{s},u\_{s},\pi\_{s},\theta\_{s},\xi\_{s}\right)\,ds\;+\;g\!\left(X\_{T}\right)\right], |  |

and the upper value

|  |  |  |
| --- | --- | --- |
|  | V^​(t,x):=sup(θ,ξ)inf(u,π)[∫tTℓ​(Xs,us,πs,θs,ξs)​𝑑s+g​(XT)],\widehat{V}(t,x):=\sup\_{(\theta,\xi)}\inf\_{(u,\pi)}\!\left[\int\_{t}^{T}\ell\!\left(X\_{s},u\_{s},\pi\_{s},\theta\_{s},\xi\_{s}\right)\,ds\;+\;g\!\left(X\_{T}\right)\right], |  |

where the infimum and supremum are taken over admissible inputs.

###### Proposition 3.3 (DPP and terminal condition).

Under Assumption [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), both the lower value VV and the upper value V^\widehat{V} satisfy the DPP, and V​(T,x)=V^​(T,x)=g​(x),x∈ℝ×ℝ+.V(T,x)=\widehat{V}(T,x)=g(x),\quad x\in\mathbb{R}\times\mathbb{R}\_{+}.

#### 3.1.2 HJBI and viscosity characterization

###### Definition 3.4 (Isaacs Hamiltonian).

Let x=(m,v)x=(m,v) denote the state and p=(pm,pv)∈ℝ2p=(p\_{m},p\_{v})\in\mathbb{R}^{2} denote the adjoint variables. Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(x,p):=infu∈𝒰,π∈𝒫supθ,ξ∈ℝ{pm​(η​u+θ)+pv​(−2​β​v+σL2+σc2+ξ−χ​π)+ℓ​(m,v,u,π,θ,ξ)}.H(x,p):=\inf\_{u\in\mathcal{U},\ \pi\in\mathcal{P}}\ \sup\_{\theta,\xi\in\mathbb{R}}\Big\{p\_{m}(\eta u+\theta)+p\_{v}\big(-2\beta v+\sigma\_{L}^{2}+\sigma\_{c}^{2}+\xi-\chi\pi\big)+\ell(m,v,u,\pi,\theta,\xi)\Big\}. |  | (2) |

Direct maximization in (θ,ξ)(\theta,\xi) yields

|  |  |  |
| --- | --- | --- |
|  | supθ,ξ∈ℝ{pm​θ+pv​ξ−θ24​λm−ξ24​λv}=λm​pm2+λv​pv2,\sup\_{\theta,\xi\in\mathbb{R}}\Big\{p\_{m}\theta+p\_{v}\xi-\tfrac{\theta^{2}}{4\lambda\_{m}}-\tfrac{\xi^{2}}{4\lambda\_{v}}\Big\}\;=\;\lambda\_{m}p\_{m}^{2}+\lambda\_{v}p\_{v}^{2}, |  |

such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(x,p)=\displaystyle H(x,p)= | λm​pm2+λv​pv2\displaystyle\lambda\_{m}p\_{m}^{2}+\lambda\_{v}p\_{v}^{2} |  | (3) |
|  |  | +infu∈𝒰,π∈𝒫{w1​m2+w2​(u)​v+R​π2+Ru​u2+pm​η​u+pv​(−2​β​v+σL2+σc2−χ​π)}.\displaystyle+\inf\_{u\in\mathcal{U},\pi\in\mathcal{P}}\Big\{w\_{1}m^{2}+w\_{2}(u)v+R\pi^{2}+R\_{u}u^{2}+p\_{m}\eta u+p\_{v}(-2\beta v+\sigma\_{L}^{2}+\sigma\_{c}^{2}-\chi\pi)\Big\}. |  |

###### Proposition 3.5 (HJBI for the value function).

Under Assumption [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and the Isaacs condition (see Lions [[39](https://arxiv.org/html/2512.04704v1#bib.bib39)] and Fleming and Soner [[24](https://arxiv.org/html/2512.04704v1#bib.bib24)], Eq. XI(3.11)), the lower value VV is a viscosity solution of the HJBI equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂tV​(t,x)+H​(x,∇xV​(t,x))=0,V​(T,x)=g​(x).-\partial\_{t}V(t,x)+H\!\big(x,\nabla\_{x}V(t,x)\big)=0,\quad V(T,x)=g(x). |  | (4) |

Moreover, the upper value V^\widehat{V} is also a viscosity solution of

|  |  |  |
| --- | --- | --- |
|  | −∂tV^​(t,x)+H​(x,∇xV^​(t,x))=0,V^​(T,x)=g​(x).-\partial\_{t}\widehat{V}(t,x)+H\!\big(x,\nabla\_{x}\widehat{V}(t,x)\big)=0,\quad\widehat{V}(T,x)=g(x). |  |

###### Theorem 3.6 (viscosity characterization of the robust HJBI).

Under Assumption [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and the DPP for VV and V^\widehat{V}, the following hold:

1. 1.

   VV is a viscosity supersolution of −∂tϕ+H​(x,∇xϕ)=0-\partial\_{t}\phi+H(x,\nabla\_{x}\phi)=0 on [0,T)×(ℝ×ℝ+)[0,T)\times(\mathbb{R}\times\mathbb{R}\_{+}), bounded from below with at most polynomial growth, and satisfies V​(T,⋅)=g​(⋅)V(T,\cdot)=g(\cdot).
2. 2.

   V^\widehat{V} is a viscosity subsolution of the same equation with V^​(T,⋅)=g​(⋅)\widehat{V}(T,\cdot)=g(\cdot).
3. 3.

   If Isaacs’ condition holds (by convexity in (u,π)(u,\pi), concavity in (θ,ξ)(\theta,\xi), and compactness), then V=V^V=\widehat{V} and the common value is a viscosity solution of the HJBI.

The proof follows viscosity arguments for robust control problems and is deferred to Appendix [B.1](https://arxiv.org/html/2512.04704v1#A2.SS1 "B.1 Proof of Theorem 3.6 ‣ Appendix B Technical proofs ‣ Coordinated Mean-Field Control for Systemic Risk").

#### 3.1.3 Comparison principle for the robust HJBI

Let x=(m,v)∈ℝ×ℝ+x=(m,v)\in\mathbb{R}\times\mathbb{R}\_{+} and define the Isaacs Hamiltonian as in [Eq. 3](https://arxiv.org/html/2512.04704v1#S3.E3 "In Definition 3.4 (Isaacs Hamiltonian). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Consider the HJBI −∂tV​(t,x)+H​(x,∇xV​(t,x))=0,(t,x)∈[0,T)×(ℝ×ℝ+),-\partial\_{t}V(t,x)+H\big(x,\nabla\_{x}V(t,x)\big)=0,\quad(t,x)\in[0,T)\times(\mathbb{R}\times\mathbb{R}\_{+}), with terminal condition V​(T,x)=g​(x)=Gm​m2+Gv​vV(T,x)=g(x)=G\_{m}m^{2}+G\_{v}v.

###### Assumption 3.7 (structural and growth conditions).

We assume the following.

1. 1.

   Ru≥cu>0R\_{u}\geq c\_{u}>0 and minu∈[umin,umax]⁡w2​(u)≥cw>0\min\_{u\in[u\_{\min},u\_{\max}]}w\_{2}(u)\geq c\_{w}>0.
2. 2.

   The Hamiltonian H​(x,p)H(x,p) is continuous in (x,p)(x,p), locally Lipschitz in xx on bounded sets, with at most polynomial growth in xx and at most quadratic growth in pp.
3. 3.

   Any viscosity subsolution and supersolution considered are continuous, satisfy for some C,kC,k the bound |U​(t,x)|≤C​(1+|x|k)|U(t,x)|\leq C(1+|x|^{k}) uniformly in tt, and attain the terminal condition in the viscosity sense.
4. 4.

   State-constraint boundary at v=0v=0. We work on the closed set ℝ×ℝ+\mathbb{R}\times\mathbb{R}\_{+} with *constrained viscosity solutions* in the sense of Soner [[46](https://arxiv.org/html/2512.04704v1#bib.bib46)]. No boundary condition is prescribed at v=0v=0. Viscosity inequalities are tested with constrained semijets (*i.e.*, using interior test functions).

###### Theorem 3.8 (comparison principle and uniqueness).

Let UU be a bounded-from-below, polynomial growth viscosity subsolution of

|  |  |  |
| --- | --- | --- |
|  | −∂tU+H​(x,∇xU)≤0on ​[0,T)×(ℝ×ℝ+),-\partial\_{t}U+H(x,\nabla\_{x}U)\leq 0\quad\text{on }[0,T)\times(\mathbb{R}\times\mathbb{R}\_{+}), |  |

and WW be a viscosity supersolution of

|  |  |  |
| --- | --- | --- |
|  | −∂tW+H​(x,∇xW)≥0on ​[0,T)×(ℝ×ℝ+),-\partial\_{t}W+H(x,\nabla\_{x}W)\geq 0\quad\text{on }[0,T)\times(\mathbb{R}\times\mathbb{R}\_{+}), |  |

with U​(T,⋅)≤g​(⋅)≤W​(T,⋅)U(T,\cdot)\leq g(\cdot)\leq W(T,\cdot) and the growth in Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").

Then
U​(t,x)≤W​(t,x)​ for all ​(t,x)∈[0,T]×(ℝ×ℝ+).U(t,x)\leq W(t,x)\text{ for all }(t,x)\in[0,T]\times(\mathbb{R}\times\mathbb{R}\_{+}). Consequently, the viscosity solution to the HJBI is unique in the polynomial-growth class. In particular, if Isaacs’ condition holds so that V=V^V=\widehat{V}, then this common value is the unique viscosity solution.

The proof relies on the doubling-of-variables technique and is provided in Appendix [B.2](https://arxiv.org/html/2512.04704v1#A2.SS2 "B.2 Proof of Theorem 3.8 ‣ Appendix B Technical proofs ‣ Coordinated Mean-Field Control for Systemic Risk").

###### Remark 3.9.

The comparison principle holds under Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") because:

1. 1.

   HH is continuous in (x,p)(x,p), locally Lipschitz in xx, with polynomial/quadratic growth (Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(2)), ensuring Ishii–Lions stability (Ishii and Lions [[35](https://arxiv.org/html/2512.04704v1#bib.bib35)], and Crandall, Ishii, and Lions [[20](https://arxiv.org/html/2512.04704v1#bib.bib20)]).
2. 2.

   Polynomial growth bounds (Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(3)) provide barriers for the coercive penalization at infinity. If preferred, one can localize on bounded domains and let the radius →∞\to\infty instead of using the ζ\zeta-term (see Appendix [B.2](https://arxiv.org/html/2512.04704v1#A2.SS2 "B.2 Proof of Theorem 3.8 ‣ Appendix B Technical proofs ‣ Coordinated Mean-Field Control for Systemic Risk")).
3. 3.

   The state-constraint boundary at v=0v=0 (Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(4)) is handled via constrained semijets on the closed set, eliminating boundary terms in the comparison argument. The constrained viscosity framework ensures that test functions respect the state
   constraint at v=0v=0, and the doubling of variables is performed only on the interior
   of the domain where both UU and WW are tested with smooth functions.

###### Remark 3.10.

By the comparison principle, viscosity solutions are unique in the polynomial-growth class. Since [Theorem 3.6](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem6 "Theorem 3.6 (viscosity characterization of the robust HJBI). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(1)-(3) identify VV as a supersolution and V^\widehat{V} as a viscosity subsolution with the same terminal condition, we obtain V^≤V\widehat{V}\leq V. If, in addition, Isaacs’ condition holds as in [Theorem 3.6](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem6 "Theorem 3.6 (viscosity characterization of the robust HJBI). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(3), then V^=V\widehat{V}=V, and the value function is the unique viscosity solution to the HJBI.

#### 3.1.4 Existence for the robust HJBI

We work on the state space [0,T]×ℝ×ℝ+[0,T]\times\mathbb{R}\times\mathbb{R}\_{+} with the state-constraint boundary at v=0v=0, as in [section 3.1.3](https://arxiv.org/html/2512.04704v1#S3.SS1.SSS3 "3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Let HH denote the Isaacs Hamiltonian defined in [Eq. 3](https://arxiv.org/html/2512.04704v1#S3.E3 "In Definition 3.4 (Isaacs Hamiltonian). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Eliminating adversarial distortions via the KL dual yields the convex quadratic terms λm​pm2+λv​pv2\lambda\_{m}p\_{m}^{2}+\lambda\_{v}p\_{v}^{2} in HH.

As in Proposition [3.5](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem5 "Proposition 3.5 (HJBI for the value function). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), the robust HJBI equation is

|  |  |  |
| --- | --- | --- |
|  | −∂tV​(t,x)+H​(x,∇xV​(t,x))= 0,(t,x)∈[0,T)×(ℝ×ℝ+),-\partial\_{t}V(t,x)+H\big(x,\nabla\_{x}V(t,x)\big)\,=\,0,\qquad(t,x)\in[0,T)\times(\mathbb{R}\times\mathbb{R}\_{+}), |  |

with terminal condition V​(T,x)=g​(x)V(T,x)=g(x).

We retain the structural and growth conditions from Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") for HH. For control domains, we use one of the following options:

1. 1.

   Compact controls (default): the control sets 𝒰,𝒫\mathcal{U},\mathcal{P} are compact intervals (Assumption [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(1)).
2. 2.

   Unbounded but coercive: replace compactness by the following assumption.

###### Assumption 3.11 (coercive running cost).

For each fixed (t,m,v,θ,ξ)(t,m,v,\theta,\xi), the running cost
  
ℓ​(t,m,v,u,π,θ,ξ)\ell(t,m,v,u,\pi,\theta,\xi) is coercive in (u,π)(u,\pi), *i.e.,* ℓ​(t,m,v,u,π,θ,ξ)→+∞\ell(t,m,v,u,\pi,\theta,\xi)\to+\infty as ∥(u,π)∥→∞\lVert(u,\pi)\rVert\to\infty.

###### Theorem 3.12 (existence of a viscosity solution).

Under Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and either compact controls (Assumption [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(1)) or Assumption [3.11](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem11 "Assumption 3.11 (coercive running cost). ‣ 3.1.4 Existence for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), there exists a continuous viscosity solution VV to the HJBI with terminal condition gg, with at most polynomial growth. Moreover, if Isaacs’ condition holds so that the Isaacs Hamiltonian HH is well-defined, then VV coincides with the robust control value function defined via the DPP.

The existence is established via the convergence of a monotone approximation scheme (see Appendix [B.3](https://arxiv.org/html/2512.04704v1#A2.SS3 "B.3 Proof of Theorem 3.12 ‣ Appendix B Technical proofs ‣ Coordinated Mean-Field Control for Systemic Risk")).

### 3.2 Verification theorem and Riccati equation derivation

We continue under the previous setting. The Isaacs Hamiltonian HH is the one in [Eq. 3](https://arxiv.org/html/2512.04704v1#S3.E3 "In Definition 3.4 (Isaacs Hamiltonian). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Control sets 𝒰,𝒫\mathcal{U},\mathcal{P} are compact (Assumption [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(1)). Structural and growth assumptions are those in Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").

#### 3.2.1 Verification theorem for the robust HJBI

###### Theorem 3.13 (verification statement).

Let V∈C​([0,T]×(ℝ×ℝ+))V\in C([0,T]\times(\mathbb{R}\times\mathbb{R}\_{+})) with at most polynomial growth satisfy, in the viscosity sense,

|  |  |  |
| --- | --- | --- |
|  | −∂tV​(t,x)+H​(x,∇xV​(t,x))=0on ​[0,T)×(ℝ×ℝ+),V​(T,x)=g​(x).-\partial\_{t}V(t,x)+H\big(x,\nabla\_{x}V(t,x)\big)=0\quad\text{on }[0,T)\times(\mathbb{R}\times\mathbb{R}\_{+}),\qquad V(T,x)=g(x). |  |

Assume Isaacs’ condition holds so that the Isaacs Hamiltonian is well-defined (see [Theorem 3.6](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem6 "Theorem 3.6 (viscosity characterization of the robust HJBI). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(3)), and that measurable minimizers exist for the Hamiltonian, guaranteed by compactness of the action sets and continuity in the controls. Then VV coincides with the robust value function, and the feedback controls that minimize the Hamiltonian are optimal for the robust problem.

The proof follows verification arguments using the DPP and comparison principle. Details are in Appendix [B.4](https://arxiv.org/html/2512.04704v1#A2.SS4 "B.4 Proof of Theorem 3.13 ‣ Appendix B Technical proofs ‣ Coordinated Mean-Field Control for Systemic Risk").

###### Remark 3.14 (explicit selectors).

When w2​(u)=w¯2+κ​uw\_{2}(u)=\bar{w}\_{2}+\kappa u and no saturation occurs at the control bounds, the first-order conditions for the minimization in HH yield

|  |  |  |
| --- | --- | --- |
|  | 2​Ru​u∗+η​∂mV+κ​v=0,2​R​π∗−χ​∂vV=0,2R\_{u}\,u^{\*}+\eta\,\partial\_{m}V+\kappa v=0,\qquad 2R\,\pi^{\*}-\chi\,\partial\_{v}V=0, |  |

hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | u∗=−η​∂mV+κ​v2​Ru,π∗=χ​∂vV2​R.u^{\*}=-\frac{\eta\,\partial\_{m}V+\kappa v}{2R\_{u}},\qquad\pi^{\*}=\frac{\chi\,\partial\_{v}V}{2R}. |  | (5) |

Projection onto 𝒰\mathcal{U} and 𝒫\mathcal{P} enforces the bounds.

Fix (t,x)(t,x) and write qm=∂mV​(t,x)q\_{m}=\partial\_{m}V(t,x) and qv=∂vV​(t,x)q\_{v}=\partial\_{v}V(t,x) for the adjoint variables (co-states). Since the adversary’s model distortions are penalized by KL, their instantaneous cost is quadratic in θ\theta and ξ\xi, normalized as 14​λ\frac{1}{4\lambda} times the square. In the HJBI, this yields a pointwise optimization of a linear term minus that quadratic penalty. By the Legendre transform (*e.g.,* Bauschke and Combettes [[5](https://arxiv.org/html/2512.04704v1#bib.bib5)], Definition 13.1),

|  |  |  |
| --- | --- | --- |
|  | supz∈ℝ{z​q−14​λ​z2}=λ​q2,with maximizerz∗=2​λ​q.\sup\_{z\in\mathbb{R}}\Big\{z\,q-\tfrac{1}{4\lambda}\,z^{2}\Big\}=\lambda\,q^{2},\quad\text{with maximizer}\quad z^{\*}=2\lambda\,q. |  |

The coefficient 14​λ\tfrac{1}{4\lambda} arises from dualizing the relative-entropy budget in [Eq. 1](https://arxiv.org/html/2512.04704v1#S2.E1 "In Robustness. ‣ 2 Model and dynamics ‣ Coordinated Mean-Field Control for Systemic Risk"). The normalization is chosen so that the maximizer takes the form z∗=2​λ​qz^{\*}=2\lambda q. Thus, we have the following KL-dual convention:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supθ∈ℝ{θ​∂mV−14​λm​θ2}=λm​(∂mV)2,supξ∈ℝ{ξ​∂vV−14​λv​ξ2}=λv​(∂vV)2.\sup\_{\theta\in\mathbb{R}}\Big\{\theta\,\partial\_{m}V-\tfrac{1}{4\lambda\_{m}}\theta^{2}\Big\}=\lambda\_{m}\big(\partial\_{m}V\big)^{2},\qquad\sup\_{\xi\in\mathbb{R}}\Big\{\xi\,\partial\_{v}V-\tfrac{1}{4\lambda\_{v}}\xi^{2}\Big\}=\lambda\_{v}\big(\partial\_{v}V\big)^{2}. |  | (6) |

Under [Eq. 6](https://arxiv.org/html/2512.04704v1#S3.E6 "In Remark 3.14 (explicit selectors). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), the adversary solves the pointwise problems

|  |  |  |
| --- | --- | --- |
|  | supθ∈ℝ{θ​qm−14​λm​θ2},supξ∈ℝ{ξ​qv−14​λv​ξ2}.\sup\_{\theta\in\mathbb{R}}\Big\{\theta\,q\_{m}-\tfrac{1}{4\lambda\_{m}}\theta^{2}\Big\},\qquad\sup\_{\xi\in\mathbb{R}}\Big\{\xi\,q\_{v}-\tfrac{1}{4\lambda\_{v}}\xi^{2}\Big\}. |  |

Each objective is strictly concave. Differentiating gives the unique maximizers

|  |  |  |
| --- | --- | --- |
|  | θ∗=2​λm​qm,ξ∗=2​λv​qv.\theta^{\*}=2\lambda\_{m}\,q\_{m},\qquad\xi^{\*}=2\lambda\_{v}\,q\_{v}. |  |

Equivalently, completing the square shows

|  |  |  |
| --- | --- | --- |
|  | θ​qm−14​λm​θ2=λm​qm2−14​λm​(θ−2​λm​qm)2,\theta\,q\_{m}-\frac{1}{4\lambda\_{m}}\theta^{2}=\lambda\_{m}q\_{m}^{2}-\frac{1}{4\lambda\_{m}}\big(\theta-2\lambda\_{m}q\_{m}\big)^{2}, |  |

so the maximum value is λm​qm2\lambda\_{m}q\_{m}^{2} (and analogously λv​qv2\lambda\_{v}q\_{v}^{2} for ξ\xi). Substituting the maximizers adds the terms λm​(∂mV)2+λv​(∂vV)2\lambda\_{m}(\partial\_{m}V)^{2}+\lambda\_{v}(\partial\_{v}V)^{2} to the Isaacs Hamiltonian. The coefficients 14​λm\tfrac{1}{4\lambda\_{m}} and 14​λv\tfrac{1}{4\lambda\_{v}} are chosen so that supz{z​q−14​λ​z2}=λ​q2\sup\_{z}\{z\,q-\tfrac{1}{4\lambda}z^{2}\}=\lambda q^{2} and z∗=2​λ​qz^{\*}=2\lambda q hold.

#### 3.2.2 Existence of saddle points

We continue with the same framework. In [Theorem 3.15](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem15 "Theorem 3.15 (saddle point via square completion). ‣ 3.2.2 Existence of saddle points ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), we state that for our deterministic robust LQ setting, the Isaacs condition holds pointwise and there exist feedback (u∗,π∗,θ∗,ξ∗)(u^{\*},\pi^{\*},\theta^{\*},\xi^{\*}) that forms a saddle point for both the differential game and the HJBI.

###### Theorem 3.15 (saddle point via square completion).

Assume Ru>0R\_{u}>0, R>0R>0, λm>0\lambda\_{m}>0, λv>0\lambda\_{v}>0, and that 𝒰\mathcal{U} and 𝒫\mathcal{P} are compact convex intervals. Then for every (t,x)(t,x) with
p=∇xV​(t,x)=(∂mV​(t,x),∂vV​(t,x))p\,=\,\nabla\_{x}V(t,x)\,=\,(\partial\_{m}V(t,x),\,\partial\_{v}V(t,x)), we have:

1. 1.

   the min-max over (u,π)∈𝒰×𝒫(u,\pi)\in\mathcal{U}\times\mathcal{P} and the max over (θ,ξ)∈ℝ2(\theta,\xi)\in\mathbb{R}^{2} commute (Isaacs holds pointwise for HH), and
2. 2.

   there exist measurable feedback (u∗,π∗,θ∗,ξ∗)(u^{\*},\pi^{\*},\theta^{\*},\xi^{\*}) forming a saddle point for the differential game and for the HJBI.

Moreover, the optimal feedback coincides with the first-order minimizers/maximizers from [section 3.2.1](https://arxiv.org/html/2512.04704v1#S3.SS2.SSS1 "3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"):

|  |  |  |
| --- | --- | --- |
|  | (ut∗,πt∗,θt∗,ξt∗)=(Π𝒰​(−η​∂mV+κ​v2​Ru),Π𝒫​(χ​∂vV2​R), 2​λm​∂mV, 2​λv​∂vV)|(t,Xt).(u\_{t}^{\*},\pi\_{t}^{\*},\theta\_{t}^{\*},\xi\_{t}^{\*})\,=\,\Big(\Pi\_{\mathcal{U}}\!\big(-\tfrac{\eta\,\partial\_{m}V+\kappa v}{2R\_{u}}\big),\;\Pi\_{\mathcal{P}}\!\big(\tfrac{\chi\,\partial\_{v}V}{2R}\big),\;2\lambda\_{m}\,\partial\_{m}V,\;2\lambda\_{v}\,\partial\_{v}V\Big)\Big|\_{(t,X\_{t})}. |  |

Projection onto 𝒰\mathcal{U} and 𝒫\mathcal{P} enforces the bounds.

###### Proof.

Consider the objective function inside the curly braces in [Eq. 2](https://arxiv.org/html/2512.04704v1#S3.E2 "In Definition 3.4 (Isaacs Hamiltonian). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Square completion in (θ,ξ)(\theta,\xi) combines the linear drift terms with the quadratic penalties in ℓ\ell to yield adversarial maximizers with achieved value λm​pm2+λv​pv2\lambda\_{m}p\_{m}^{2}+\lambda\_{v}p\_{v}^{2}. Similarly, square completion in (u,π)(u,\pi) yields the unconstrained minimizers [Eq. 5](https://arxiv.org/html/2512.04704v1#S3.E5 "In Remark 3.14 (explicit selectors). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), while metric projections onto 𝒰\mathcal{U} and 𝒫\mathcal{P} enforce bounds. The mapping is continuous, strictly convex in (u,π)(u,\pi) and strictly concave in (θ,ξ)(\theta,\xi). Since the assumption w¯2+κ​umin>0\bar{w}\_{2}+\kappa\,u\_{\min}>0 ([section 2](https://arxiv.org/html/2512.04704v1#S2 "2 Model and dynamics ‣ Coordinated Mean-Field Control for Systemic Risk")) ensures w2​(u)>0w\_{2}(u)>0 for all u∈𝒰u\in\mathcal{U}, the objective remains strictly convex in uu. With 𝒰×𝒫\mathcal{U}\times\mathcal{P} compact and convex, Sion’s [[45](https://arxiv.org/html/2512.04704v1#bib.bib45)] minimax theorem applies: if XX is compact and convex, YY is convex, and f:X×Y→ℝf:X\times Y\to\mathbb{R} is convex and lower semicontinuous in x∈Xx\in X and concave and upper semicontinuous in y∈Yy\in Y, then

|  |  |  |
| --- | --- | --- |
|  | minx∈X​supy∈Yf​(x,y)=supy∈Yminx∈X⁡f​(x,y),\min\_{x\in X}\sup\_{y\in Y}f(x,y)\;=\;\sup\_{y\in Y}\min\_{x\in X}f(x,y), |  |

and when one side is compact and the other convex with the respective semicontinuity, the extrema are attained, yielding a saddle point. Applied here with X=𝒰×𝒫X=\mathcal{U}\times\mathcal{P}, Y=ℝ2Y=\mathbb{R}^{2}, and the objective function continuous, strictly convex in (u,π)(u,\pi) and strictly concave in (θ,ξ)(\theta,\xi), we obtain pointwise Isaacs equality for HH and a saddle point at the feedback above when p=∇xVp=\nabla\_{x}V. Admissibility follows from polynomial growth and compactness, and optimality follows from [Theorem 3.13](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem13 "Theorem 3.13 (verification statement). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") together with the DPP and the comparison principle.
∎

###### Remark 3.16 (optimality of projected controls).

Since the objective function in the Isaacs Hamiltonian [Eq. 2](https://arxiv.org/html/2512.04704v1#S3.E2 "In Definition 3.4 (Isaacs Hamiltonian). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") is strictly convex in (u,π)(u,\pi) and 𝒰×𝒫\mathcal{U}\times\mathcal{P} is convex and compact, the constrained minimum equals the metric projection of the unconstrained minimizer onto the admissible set. This justifies the computational strategy in [section 4](https://arxiv.org/html/2512.04704v1#S4 "4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"): solving the unconstrained first-order conditions and projecting onto 𝒰\mathcal{U} and 𝒫\mathcal{P} yields the optimal feedback.

###### Remark 3.17 (Riccati specialization).

If V​(t,x)V(t,x) is quadratic in (m,v)(m,v), the feedback is linear and the HJBI [Eq. 4](https://arxiv.org/html/2512.04704v1#S3.E4 "In Proposition 3.5 (HJBI for the value function). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") reduces to coupled Riccati equations in time. This observation motivates the quadratic ansatz [Eq. 7](https://arxiv.org/html/2512.04704v1#S3.E7 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").

###### Remark 3.18 (state constraint).

The state-constraint boundary at v=0v=0 is treated in the viscosity sense as in [section 3.1.4](https://arxiv.org/html/2512.04704v1#S3.SS1.SSS4 "3.1.4 Existence for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Projections Π𝒰\Pi\_{\mathcal{U}} and Π𝒫\Pi\_{\mathcal{P}} ensure admissibility on compact action sets.

#### 3.2.3 Quadratic value function ansatz

We proceed under the same assumptions as in [section 3.2.2](https://arxiv.org/html/2512.04704v1#S3.SS2.SSS2 "3.2.2 Existence of saddle points ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Existence of saddle points and the pointwise Isaacs property are given by [Theorem 3.15](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem15 "Theorem 3.15 (saddle point via square completion). ‣ 3.2.2 Existence of saddle points ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). While the viscosity framework guarantees existence and uniqueness in general, the LQ structure allows us to construct the solution explicitly via a quadratic ansatz, which we now pursue.

##### Quadratic candidate.

On the interior region (*i.e.*, away from the projection boundaries so that u=−η​∂mV+κ​v2​Ruu=-\tfrac{\eta\,\partial\_{m}V+\kappa v}{2R\_{u}} and π=χ​∂vV2​R\pi=\tfrac{\chi\,\partial\_{v}V}{2R}), consider the quadratic ansatz

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,m,v)=a0​(t)+a1​(t)​m+a2​(t)​v+a11​(t)​m2+a12​(t)​m​v+a22​(t)​v2,V(t,m,v)=a\_{0}(t)+a\_{1}(t)m+a\_{2}(t)v+a\_{11}(t)m^{2}+a\_{12}(t)mv+a\_{22}(t)v^{2}, |  | (7) |

so that ∂mV=a1+2​a11​m+a12​v\partial\_{m}V=a\_{1}+2a\_{11}m+a\_{12}v and ∂vV=a2+a12​m+2​a22​v\partial\_{v}V=a\_{2}+a\_{12}m+2a\_{22}v, with terminal conditions matching Gm​m2+Gv​vG\_{m}m^{2}+G\_{v}v at t=Tt=T and thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | a2​(T)=Gv,a11​(T)=Gm,a0​(T)=a1​(T)=a12​(T)=a22​(T)=0.a\_{2}(T)=G\_{v},\;a\_{11}(T)=G\_{m},\quad a\_{0}(T)=a\_{1}(T)=a\_{12}(T)=a\_{22}(T)=0. |  | (8) |

##### Riccati ODE system for the quadratic ansatz.

Let ∇V=(∂mV,∂vV)\nabla V=(\partial\_{m}V,\partial\_{v}V). Using the Isaacs Hamiltonian in [Eq. 2](https://arxiv.org/html/2512.04704v1#S3.E2 "In Definition 3.4 (Isaacs Hamiltonian). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and the KL-dual convention [Eq. 6](https://arxiv.org/html/2512.04704v1#S3.E6 "In Remark 3.14 (explicit selectors). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), adversarial maximizers and control minimizers coincide with the selectors in [Eq. 5](https://arxiv.org/html/2512.04704v1#S3.E5 "In Remark 3.14 (explicit selectors). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and [Theorem 3.15](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem15 "Theorem 3.15 (saddle point via square completion). ‣ 3.2.2 Existence of saddle points ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∗=2​λm​∂mV,ξ∗=2​λv​∂vV,(u∗​(x),π∗​(x))=(Π𝒰​(−η​∂mV+κ​v2​Ru),Π𝒫​(χ​∂vV2​R)),\theta^{\*}=2\lambda\_{m}\,\partial\_{m}V,\quad\xi^{\*}=2\lambda\_{v}\,\partial\_{v}V,\quad\Big(u^{\*}(x),\,\pi^{\*}(x)\Big)=\Big(\Pi\_{\mathcal{U}}\!\big(-\tfrac{\eta\,\partial\_{m}V+\kappa v}{2R\_{u}}\big),\;\Pi\_{\mathcal{P}}\!\big(\tfrac{\chi\,\partial\_{v}V}{2R}\big)\Big), |  | (9) |

where x=(m,v)x=(m,v) and with variance drift that includes −χ​π-\chi\,\pi.

Let Σ2:=σL2+σc2\Sigma^{2}:=\sigma\_{L}^{2}+\sigma\_{c}^{2}. Plugging these selectors into the HJBI −∂tV+H​(x,∇V)=0-\partial\_{t}V+H(x,\nabla V)=0 yields a polynomial identity in (m,v)(m,v). Equating coefficients of like monomials in (m,v)(m,v) yields a coupled Riccati-type ODE system for {ai​(⋅)}\{a\_{i}(\cdot)\} on [0,T][0,T] under the quadratic ansatz. The full system of six coupled Riccati ODEs is as follows (see Appendix [D](https://arxiv.org/html/2512.04704v1#A4 "Appendix D Derivation of the Riccati ODE system ‣ Coordinated Mean-Field Control for Systemic Risk")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | a˙0\displaystyle\dot{a}\_{0} | =Σ2​a2+(λm−η24​Ru)​a12+(λv−χ24​R)​a22,\displaystyle=\;\Sigma^{2}a\_{2}+\Big(\lambda\_{m}-\tfrac{\eta^{2}}{4R\_{u}}\Big)a\_{1}^{2}+\Big(\lambda\_{v}-\tfrac{\chi^{2}}{4R}\Big)a\_{2}^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a˙1\displaystyle\dot{a}\_{1} | =Σ2​a12+(4​λm−η2Ru)​a1​a11+(2​λv−χ22​R)​a2​a12,\displaystyle=\;\Sigma^{2}a\_{12}+\Big(4\lambda\_{m}-\tfrac{\eta^{2}}{R\_{u}}\Big)a\_{1}a\_{11}+\Big(2\lambda\_{v}-\tfrac{\chi^{2}}{2R}\Big)a\_{2}a\_{12}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a˙2\displaystyle\dot{a}\_{2} | =w¯2−2​β​a2+2​Σ2​a22+(2​λm−η22​Ru)​a1​a12+(4​λv−χ2R)​a2​a22−η​κ2​Ru​a1,\displaystyle=\;\bar{w}\_{2}-2\beta a\_{2}+2\Sigma^{2}a\_{22}+\Big(2\lambda\_{m}-\tfrac{\eta^{2}}{2R\_{u}}\Big)a\_{1}a\_{12}+\Big(4\lambda\_{v}-\tfrac{\chi^{2}}{R}\Big)a\_{2}a\_{22}-\tfrac{\eta\kappa}{2R\_{u}}a\_{1}, |  | (10) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a˙11\displaystyle\dot{a}\_{11} | =w1+(4​λm−η2Ru)​a112+(λv−χ24​R)​a122,\displaystyle=\;w\_{1}+\Big(4\lambda\_{m}-\tfrac{\eta^{2}}{R\_{u}}\Big)a\_{11}^{2}+\Big(\lambda\_{v}-\tfrac{\chi^{2}}{4R}\Big)a\_{12}^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a˙12\displaystyle\dot{a}\_{12} | =−2​β​a12−η​κRu​a11+(4​λm−η2Ru)​a11​a12+(4​λv−χ2R)​a12​a22,\displaystyle=\;-2\beta a\_{12}-\tfrac{\eta\kappa}{R\_{u}}a\_{11}+\Big(4\lambda\_{m}-\tfrac{\eta^{2}}{R\_{u}}\Big)a\_{11}a\_{12}+\Big(4\lambda\_{v}-\tfrac{\chi^{2}}{R}\Big)a\_{12}a\_{22}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a˙22\displaystyle\dot{a}\_{22} | =−4​β​a22−κ24​Ru−η​κ2​Ru​a12+(λm−η24​Ru)​a122+(4​λv−χ2R)​a222.\displaystyle=\;-4\beta a\_{22}-\tfrac{\kappa^{2}}{4R\_{u}}-\tfrac{\eta\kappa}{2R\_{u}}a\_{12}+\Big(\lambda\_{m}-\tfrac{\eta^{2}}{4R\_{u}}\Big)a\_{12}^{2}+\Big(4\lambda\_{v}-\tfrac{\chi^{2}}{R}\Big)a\_{22}^{2}. |  |

###### Remark 3.19.

The system governs the interior (unconstrained) regime. When projections are active, the selectors in [Eq. 9](https://arxiv.org/html/2512.04704v1#S3.E9 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") become piecewise, and the coefficient dynamics are piecewise with switching times determined by the projection boundaries. The scaling is consistent with the KL-dual convention [Eq. 6](https://arxiv.org/html/2512.04704v1#S3.E6 "In Remark 3.14 (explicit selectors). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") in which the running penalty adds −θ24​λm-\tfrac{\theta^{2}}{4\lambda\_{m}} and −ξ24​λv-\tfrac{\xi^{2}}{4\lambda\_{v}} to the Hamiltonian, yielding the multipliers in the system. The constant variance drift Σ2\Sigma^{2} enters linearly and affects only the equations for a0,a1,a2a\_{0},a\_{1},a\_{2}.

###### Theorem 3.20 (quadratic verification by cross-reference).

Let VV be given by the quadratic ansatz [Eq. 7](https://arxiv.org/html/2512.04704v1#S3.E7 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") with coefficients ai​(⋅){a\_{i}(\cdot)} on [0,T][0,T] and terminal condition [Eq. 8](https://arxiv.org/html/2512.04704v1#S3.E8 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Suppose the Riccati system in [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") admits a C1C^{1} solution on [0,T][0,T] with at most polynomial growth and that the assumptions hold (compact convex action sets, measurable selectors, Lipschitz dynamics, and Isaacs condition). Define feedback (u∗,π∗;θ∗,ξ∗)(u^{\*},\pi^{\*};\theta^{\*},\xi^{\*}) as in [Eq. 9](https://arxiv.org/html/2512.04704v1#S3.E9 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") with projections onto the admissible sets. Then VV is a viscosity solution of the HJBI with terminal condition V​(T,m,v)=Gm​m2+Gv​vV(T,m,v)=G\_{m}m^{2}+G\_{v}v, and

|  |  |  |
| --- | --- | --- |
|  | V​(t,x)=infu,πsupθ,ξJt,x​(u,π;θ,ξ)=supθ,ξinfu,πJt,x​(u,π;θ,ξ),V(t,x)\,=\,\inf\_{u,\pi}\,\sup\_{\theta,\xi}J\_{t,x}(u,\pi;\theta,\xi)\,=\,\sup\_{\theta,\xi}\,\inf\_{u,\pi}J\_{t,x}(u,\pi;\theta,\xi), |  |

with (u∗,π∗;θ∗,ξ∗)(u^{\*},\pi^{\*};\theta^{\*},\xi^{\*}) forming a saddle point.

###### Proof.

By [Theorem 3.13](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem13 "Theorem 3.13 (verification statement). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and the Isaacs/saddle-point result in [Theorem 3.15](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem15 "Theorem 3.15 (saddle point via square completion). ‣ 3.2.2 Existence of saddle points ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). The selectors [Eq. 9](https://arxiv.org/html/2512.04704v1#S3.E9 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") realize the Hamiltonian extremizers. Plugging them into the HJBI yields the polynomial identity in (m,v)(m,v), whose coefficient matching is equivalent to deriving [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Hence VV solves the HJBI in the viscosity sense with the stated terminal condition, and the value identity with the saddle point follows by Isaacs’ condition.
∎

###### Proposition 3.21 (global existence and breakdown threshold).

The Riccati system [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") admits a unique bounded solution on [0,T][0,T] for any time horizon T>0T>0 if and only if the adversary parameters satisfy the stability conditions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 4​λm≤η2Ruand4​λv≤χ2R.4\lambda\_{m}\leq\frac{\eta^{2}}{R\_{u}}\quad\text{and}\quad 4\lambda\_{v}\leq\frac{\chi^{2}}{R}. |  | (11) |

If these conditions are strictly satisfied, the solution remains bounded. If either condition is strictly violated (*i.e.,* 4​λm>η2Ru4\lambda\_{m}>\frac{\eta^{2}}{R\_{u}} or 4​λv>χ2R4\lambda\_{v}>\frac{\chi^{2}}{R}), there exists a critical horizon T∗<∞T^{\*}<\infty such that for any T>T∗T>T^{\*}, the solution to the Riccati system explodes, implying V​(0,m,v)=+∞V(0,m,v)=+\infty and the non-existence of a finite-cost robust control policy.

###### Proof.

The Riccati equations for the second-order coefficients a11,a12,a22a\_{11},a\_{12},a\_{22} form a closed subsystem. Consider the a11a\_{11} equation:

|  |  |  |
| --- | --- | --- |
|  | a˙11=w1+(4​λm−η2Ru)​a112+(λv−χ24​R)​a122.\dot{a}\_{11}=w\_{1}+\left(4\lambda\_{m}-\tfrac{\eta^{2}}{R\_{u}}\right)a\_{11}^{2}+\left(\lambda\_{v}-\tfrac{\chi^{2}}{4R}\right)a\_{12}^{2}. |  |

Let Cm=4​λm−η2RuC\_{m}=4\lambda\_{m}-\frac{\eta^{2}}{R\_{u}}. When the stability condition is violated (Cm>0C\_{m}>0), the coefficient a11​(t)a\_{11}(t) is bounded from below by the solution of the comparison ODE y˙=w1+Cm​y2\dot{y}=w\_{1}+C\_{m}y^{2} with y​(T)=Gmy(T)=G\_{m}. The solution to this ODE is of the form y​(t)∝tan⁡(w1​Cm​(T−t)+c)y(t)\propto\tan\left(\sqrt{w\_{1}C\_{m}}(T-t)+c\right).

The tangent function exhibits a vertical asymptote at a finite backward time distance T∗T^{\*} determined by the terminal value and coefficients. Consequently, for horizons T>T∗T>T^{\*}, the solution a11​(t)a\_{11}(t) explodes, causing the value function to become infinite. A similar argument applies to a22a\_{22} when 4​λv>χ2R4\lambda\_{v}>\frac{\chi^{2}}{R}. This establishes the non-existence of finite-cost robust control when the stability conditions are violated.
∎

###### Remark 3.22 (interior vs constrained regimes).

The Riccati ODEs in [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") govern the interior region where projections are inactive. Under Lipschitz state dynamics and compact action sets, admissible controls generate unique absolutely continuous trajectories, and polynomial growth of VV ensures integrability. In extensions with noise, viscosity well-posedness of the robust HJBI follows under standard comparison hypotheses (*e.g.,* continuity, properness, and structural conditions).

###### Remark 3.23 (piecewise dynamics in saturated regimes).

When a control saturates at its boundary, the structure of the Riccati system changes because the minimization (infimum over (u,π)(u,\pi)) in [Eq. 3](https://arxiv.org/html/2512.04704v1#S3.E3 "In Definition 3.4 (Isaacs Hamiltonian). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") is replaced by boundary evaluation.

1. 1.

   When πt=πmax\pi\_{t}=\pi\_{\max}, the optimal control becomes constant, and the term −(∂vV​χ)24​R-\frac{(\partial\_{v}V\chi)^{2}}{4R} in the optimized Hamiltonian is replaced by R​πmax2−∂vV​χ​πmaxR\pi\_{\max}^{2}-\partial\_{v}V\chi\pi\_{\max}. This alters the Riccati coefficients in [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). For instance, the quadratic self-interaction term −χ2R​a222-\frac{\chi^{2}}{R}a\_{22}^{2} in the a˙22\dot{a}\_{22} equation is removed, and linear terms in a22a\_{22} are modified.
2. 2.

   Analogous changes occur when utu\_{t} saturates.

While the value function VV remains C1C^{1} across switching boundaries, solving the exact piecewise system requires tracking switching surfaces. For computational tractability, our numerical implementation in [section 4](https://arxiv.org/html/2512.04704v1#S4 "4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") solves the interior Riccati system and projects the resulting controls onto 𝒰\mathcal{U} and 𝒫\mathcal{P} at each time step.

## 4 Simulations and robustness

Building on the theoretical foundations in [section 3](https://arxiv.org/html/2512.04704v1#S3 "3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), we perform simulations and assess robustness. Unless stated otherwise, the simulations in [section 4](https://arxiv.org/html/2512.04704v1#S4 "4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") are implemented in two stages using the parameters in [Table 1](https://arxiv.org/html/2512.04704v1#S4.T1 "In 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk").

First, we obtain the time-varying coefficients for the quadratic ansatz V​(t,m,v)V(t,m,v) by integrating the Riccati system [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") backward from the terminal condition g​(m,v)=Gm​m2+Gv​vg(m,v)=G\_{m}m^{2}+G\_{v}v, implemented as [Eq. 8](https://arxiv.org/html/2512.04704v1#S3.E8 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). We employ an implicit, L-stable (Laplace transform stable) Runge-Kutta method of Radau IIA type to handle the Riccati equations.

Second, we propagate the forward dynamics using an explicit Euler scheme on a uniform grid with step Δ​t\Delta t. At each step, we compute the unconstrained selectors using the value gradients ∂mV\partial\_{m}V and ∂vV\partial\_{v}V, and project the controls onto their admissible sets 𝒰\mathcal{U} and 𝒫\mathcal{P}. The variance is strictly enforced to be non-negative by flooring vtv\_{t} at zero. Adversarial distortions (θt,ξt)(\theta\_{t},\xi\_{t}) are computed via their KL-dual selectors, given by θt∗=2​λm​∂mV\theta^{\*}\_{t}=2\lambda\_{m}\partial\_{m}V and ξt∗=2​λv​∂vV\xi^{\*}\_{t}=2\lambda\_{v}\partial\_{v}V.

| Parameters | Values | Description |
| --- | --- | --- |
| (β,η,χ,σL,σc)(\beta,\eta,\chi,\sigma\_{L},\sigma\_{c}) | (0.25, 0.8, 0.5, 0.4, 0.3) | System parameters |
| (w1,w¯2,κ,Ru,R)(w\_{1},\bar{w}\_{2},\kappa,R\_{u},R) | (0.1, 0.5, 0.05, 0.5, 0.25) | Cost parameters |
| (Gm,Gv)(G\_{m},G\_{v}) | (0.5, 0.5) | Terminal cost weights |
| (λm,λv)(\lambda\_{m},\lambda\_{v}) | (0.02, 0.02) | Adversary strength parameters |
| (umin,umax,πmax)(u\_{\min},u\_{\max},\pi\_{\max}) | (-1.0, 1.0, 10.0) | Control bounds |
| (T,Δ​t)(T,\Delta t) | (10.0, 0.001) | Time parameters |
| (m0,v0)(m\_{0},v\_{0}) | (0.5, 1.0) | Initial conditions |

Table 1: Simulation parameters of the baseline model.

The baseline parameters in [Table 1](https://arxiv.org/html/2512.04704v1#S4.T1 "In 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") are chosen to ensure the robust control problem is well-posed. A bounded solution to the Riccati system requires the stabilizing control-cost terms to exceed the destabilizing adversarial terms. Our parameters strictly satisfy these conditions: η2Ru=1.28>4​λm=0.08\frac{\eta^{2}}{R\_{u}}=1.28>4\lambda\_{m}=0.08 for the mean and χ2R=1.00>4​λv=0.08\frac{\chi^{2}}{R}=1.00>4\lambda\_{v}=0.08 for the variance, guaranteeing a stable interior solution and allowing us to analyze the system’s response as λ\lambda increases.

###### Remark 4.1 (robustness-breakdown threshold).

The stability conditions determine the *robustness-breakdown* threshold (see Proposition [3.21](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem21 "Proposition 3.21 (global existence and breakdown threshold). ‣ Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")). If the adversary’s strength becomes too large (4​λm>η2Ru4\lambda\_{m}>\frac{\eta^{2}}{R\_{u}} or 4​λv>χ2R4\lambda\_{v}>\frac{\chi^{2}}{R}), the coefficient on the corresponding quadratic term in the Riccati system [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") (a112a\_{11}^{2} in the a˙11\dot{a}\_{11} equation or a222a\_{22}^{2} in the a˙22\dot{a}\_{22} equation) becomes positive. Solving backward from a finite terminal condition, such a solution explodes to infinity in finite time, implying that no finite-cost optimal policy exists. Thus, the breakdown threshold is linked to the critical value λ∗\lambda^{\*}, where the coefficient changes sign from negative to positive, and the robust control problem ceases to have a well-posed solution.

###### Remark 4.2 (baseline parameters).

Beyond stability, the baseline parameters shape the Riccati dynamics and optimal feedback structure. The control effectiveness ratio η2Ru=1.28>χ2R=1.00\frac{\eta^{2}}{R\_{u}}=1.28>\frac{\chi^{2}}{R}=1.00 implies that the mean channel dominates in the Riccati coefficients, explaining the system’s robustness to mean distortions but vulnerability to variance ambiguity. The cost weights w¯2=0.5>w1=0.1\bar{w}\_{2}=0.5>w\_{1}=0.1 weight variance reduction more heavily, which amplifies the a2a\_{2} and a22a\_{22} coefficients and drives active coordination between instruments. The terminal weights Gm=Gv=0.5G\_{m}=G\_{v}=0.5 impose symmetric penalties on final deviations. The mean-reversion β=0.25\beta=0.25 yields an autonomous variance decay rate 2​β=0.52\beta=0.5, which balances against the noise injection Σ2=σL2+σc2=0.25\Sigma^{2}=\sigma\_{L}^{2}+\sigma\_{c}^{2}=0.25. The coupling κ=0.05\kappa=0.05 introduces cross-terms in the Hamiltonian linking vtv\_{t} to the policy rate optimization, but remains small relative to w¯2\bar{w}\_{2} to preserve near-separability. Finally, the baseline adversary strengths λm=λv=0.02\lambda\_{m}=\lambda\_{v}=0.02 provide substantial headroom below the breakdown thresholds λm∗=0.32\lambda\_{m}^{\*}=0.32 and λv∗=0.25\lambda\_{v}^{\*}=0.25, enabling exploration of the transition to loss of control.

###### Remark 4.3 (over-monitoring and state constraints).

A structural consequence of the unconstrained formulation is *over-monitoring*, which arises because the interior Riccati solution yields a global quadratic value function without enforcing the state constraint at v=0v=0. A fully constrained formulation would require solving the HJBI equation with state-constraint boundary conditions in the viscosity sense of Soner [[46](https://arxiv.org/html/2512.04704v1#bib.bib46)], introducing regime-dependent dynamics that reduce πt\pi\_{t} once vtv\_{t} reaches zero. However, because the constraint introduces endogenous regime switching, the backward Riccati system and forward state dynamics must be solved jointly, necessitating numerical methods. We retain our unconstrained formulation to preserve analytical tractability, as it yields explicit feedback laws that transparently illustrate the coupling between monetary and supervisory policies.444CBs typically conduct bank monitoring even when a bank’s current liquidity conditions are sound, and our formulation is consistent with this institutional practice.

###### Remark 4.4 (scope of over-monitoring effects).

Over-monitoring primarily inflates the total cost JJ and control saturation metrics. State trajectories (mt,vt)(m\_{t},v\_{t}) and peak adversarial distortions are largely unaffected, as the variance floor at vt=0v\_{t}=0 effectively captures the stabilized dynamics. Robustness-breakdown thresholds (determined by Riccati stability) are also unaffected. However, the cost impact is parameter-dependent: high-χ\chi regimes, where the system reaches the boundary earlier and remains there longer, are disproportionately affected. Consequently, while the structural phase transitions in the loss-of-control analysis ([Figure 6](https://arxiv.org/html/2512.04704v1#S4.F6 "In 4.4 Loss of control ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")) remain valid, the iso-cost contours in high-χ\chi regions reflect this inefficiency.

### 4.1 Path simulations

We simulate finite-horizon paths of (mt,vt,ut,πt)(m\_{t},v\_{t},u\_{t},\pi\_{t}) under baseline parameters for different levels of adversary strength, as in [Algorithm 1](https://arxiv.org/html/2512.04704v1#alg1 "In 4.1 Path simulations ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk").

Algorithm 1  System dynamics ([Figure 1](https://arxiv.org/html/2512.04704v1#S4.F1 "In 4.1 Path simulations ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"))

1:Input: Parameter set pp, horizon TT, step Δ​t\Delta t, grid tn=n​Δ​tt\_{n}=n\Delta t.

2:Output: Trajectories of (m,v,u,π)(m,v,u,\pi) and distortions (θ,ξ)(\theta,\xi).

3:function Simulate(pp)

4:  Backward pass:

5:  Solve Riccati system ([Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")) for a​(t)a(t) on grid using Radau IIA.

6:  Forward pass:

7:  Initialize (m0,v0)(m\_{0},v\_{0}).

8:  for n=0,…,N−1n=0,\ldots,N-1 do

9:   Evaluate gradients ∂mV,∂vV\partial\_{m}V,\partial\_{v}V using a​(tn),mn,vna(t\_{n}),m\_{n},v\_{n}.

10:   Compute distortions: θn=2​λm​∂mV\theta\_{n}=2\lambda\_{m}\partial\_{m}V, ξn=2​λv​∂vV\xi\_{n}=2\lambda\_{v}\partial\_{v}V.

11:   Compute unconstrained controls (uunc,πunc)(u^{\text{unc}},\pi^{\text{unc}}) via [Eq. 9](https://arxiv.org/html/2512.04704v1#S3.E9 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").

12:   Project: un←clip​(uunc,umin,umax)u\_{n}\leftarrow\text{clip}(u^{\text{unc}},u\_{\min},u\_{\max}), πn←clip​(πunc,0,πmax)\pi\_{n}\leftarrow\text{clip}(\pi^{\text{unc}},0,\pi\_{\max}).

13:   Update:

14:   mn+1←mn+[η​un+θn]​Δ​t\quad m\_{n+1}\leftarrow m\_{n}+[\eta u\_{n}+\theta\_{n}]\Delta t

15:   vn+1←max⁡(0,vn+[−2​β​vn+Σ2+ξn−χ​πn]​Δ​t)\quad v\_{n+1}\leftarrow\max\big(0,v\_{n}+[-2\beta v\_{n}+\Sigma^{2}+\xi\_{n}-\chi\pi\_{n}]\Delta t\big)

16:  return Trajectories {(mn,vn,un,πn,θn,ξn)}n=0N\{(m\_{n},v\_{n},u\_{n},\pi\_{n},\theta\_{n},\xi\_{n})\}\_{n=0}^{N}.

![Refer to caption](fig_1.png)


Figure 1: System dynamics under different levels of adversary strength. Panels show trajectories for mean liquidity mtm\_{t}, variance vtv\_{t}, policy rate utu\_{t}, and monitoring intensity πt\pi\_{t}. As λ\lambda increases, vTv\_{T} is pushed upward, settling at a non-zero steady state in the strong-adversary case. Note in panels (a) to (c) that monitoring πt\pi\_{t} remains positive even after variance vtv\_{t} reaches zero, illustrating the over-monitoring discussed in Remarks [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [4.4](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem4 "Remark 4.4 (scope of over-monitoring effects). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk").

We call Simulate with four adversary strength scenarios: Negligible (λm=λv=10−10\lambda\_{m}=\lambda\_{v}=10^{-10}), Weak (λm=λv=0.005\lambda\_{m}=\lambda\_{v}=0.005), Baseline (λm=λv=0.02\lambda\_{m}=\lambda\_{v}=0.02), and Strong (λm=λv=0.15\lambda\_{m}=\lambda\_{v}=0.15), producing the trajectories shown in [Figure 1](https://arxiv.org/html/2512.04704v1#S4.F1 "In 4.1 Path simulations ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk").

Initially, the mean m0=0.5m\_{0}=0.5 reflects a liquidity shortage in the banking sector. The policy rate utu\_{t} starts around −0.3-0.3, an accommodative stance consistent with addressing this shortage. The variance v0=1.0v\_{0}=1.0 indicates heterogeneity in liquidity positions across banks. The monitoring intensity π0\pi\_{0} begins close to 11, reflecting the CB’s heightened monitoring in response to this initial stress (v0=1.0v\_{0}=1.0).

In [Figure 1](https://arxiv.org/html/2512.04704v1#S4.F1 "In 4.1 Path simulations ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"), the mean liquidity mtm\_{t} is steered from its initial value of 0.50.5 toward its terminal value mTm\_{T}, driven by the policy rate utu\_{t} which relaxes from its initial aggressive stance. The monitoring intensity πt\pi\_{t} decreases from its high initial value, steering the variance downward. As adversary strength λ\lambda increases, the final states for both mean and variance (mT,vT)(m\_{T},v\_{T}) become progressively higher. This effect is most clear in [Figure 1](https://arxiv.org/html/2512.04704v1#S4.F1 "In 4.1 Path simulations ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(d), where the variance settles at a non-zero value, consistent with the optimal equilibrium described in Remark [2.4](https://arxiv.org/html/2512.04704v1#S2.Thmtheorem4 "Remark 2.4 (terminal variance and cost structure). ‣ Model setting. ‣ 2 Model and dynamics ‣ Coordinated Mean-Field Control for Systemic Risk"). With a strong adversary, the total upward pressure on variance (Σ2+ξt∗\Sigma^{2}+\xi\_{t}^{\*}) exceeds the CB’s downward control force (χ​πt∗\chi\pi\_{t}^{\*}) near the terminal time. Consequently, vtv\_{t} settles at an equilibrium where the optimal monitoring condition holds (2​R​πt∗=χ​∂vV2R\pi\_{t}^{\*}=\chi\partial\_{v}V) and the variance drift balances to zero (2​β​vt=Σ2+ξt∗−χ​πt∗2\beta v\_{t}=\Sigma^{2}+\xi\_{t}^{\*}-\chi\pi\_{t}^{\*}).

### 4.2 Adversary strength analysis

We sweep the adversary strength parameters (λm,λv)(\lambda\_{m},\lambda\_{v}) and track indicators of control effectiveness, as in [Algorithm 2](https://arxiv.org/html/2512.04704v1#alg2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"). λm\lambda\_{m} and λv\lambda\_{v} govern the adversary’s capacity to distort the mean and variance channels, respectively. For any parameter tuple, we simulate state and control paths (mt,vt,ut,πt)(m\_{t},v\_{t},u\_{t},\pi\_{t}) over a finite horizon.

Algorithm 2  Adversary strength analysis ([Figure 2](https://arxiv.org/html/2512.04704v1#S4.F2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"))

1:Input: Baseline parameters p0p\_{0}, grid size NN.

2:Output: Cost and control metrics versus λ\lambda.

3:Part 1: Symmetric analysis

4:for λ∈linspace​(0,0.2,N)\lambda\in\text{linspace}(0,0.2,N) do

5:  Update: p←p0p\leftarrow p\_{0} with λm=λv=λ\lambda\_{m}=\lambda\_{v}=\lambda

6:  Simulate and store metrics

7:Part 2: Asymmetric analysis

8:Test cases: (λm,λv)∈{(0.001,0.1),(0.001,0.2),(0.1,0.001),(0.2,0.001)}(\lambda\_{m},\lambda\_{v})\in\{(0.001,0.1),(0.001,0.2),(0.1,0.001),(0.2,0.001)\}

9:for each (λm,λv)(\lambda\_{m},\lambda\_{v}) pair do

10:  Update: p←p0p\leftarrow p\_{0} with specified λm,λv\lambda\_{m},\lambda\_{v}

11:  Simulate and store metrics

12:Generate [Figure 2](https://arxiv.org/html/2512.04704v1#S4.F2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") plots from collected metrics

For visualization, we summarize performance across different levels of adversary strength by sweeping (λm,λv)(\lambda\_{m},\lambda\_{v}) over orders of magnitude and plotting: total cost JJ, average controls (u¯,π¯)(\bar{u},\bar{\pi}), and peak adversarial distortions (maxt⁡|θt|,maxt⁡|ξt|)(\max\_{t}|\theta\_{t}|,\max\_{t}|\xi\_{t}|). utu\_{t} remains non-positive, and its absolute value is not taken.

Our analysis of the λ\lambda parameters is conducted within the model’s stable robustness region. The coupled Riccati system in [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") only admits a finite, bounded solution if the stabilizing control terms are stronger than the destabilizing adversarial terms (Remark [4.1](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem1 "Remark 4.1 (robustness-breakdown threshold). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")). For our baseline parameters, this requires λm<0.32\lambda\_{m}<0.32 and λv<0.25\lambda\_{v}<0.25. We therefore restrict our λ\lambda sweeps to the range [0,0.2][0,0.2] to analyze the system’s behavior within this stable region, avoiding the breakdown of the Riccati solution.

![Refer to caption](fig_2.png)


Figure 2: Adversary strength analysis sweeping λ∈[0,0.2]\lambda\in[0,0.2]. (a) Total cost JJ, (b) average control levels, and (c) peak adversarial distortions. Within this stable region, JJ is primarily driven by λv\lambda\_{v}, while no control saturation occurs (see Remarks [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [4.4](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem4 "Remark 4.4 (scope of over-monitoring effects). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")).

As λ\lambda increases, JJ also increases. The rise is driven primarily by the growth in λv\lambda\_{v}, rather than λm\lambda\_{m} ([Figure 2](https://arxiv.org/html/2512.04704v1#S4.F2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(a)). Both utu\_{t} and πt\pi\_{t} adjust to λ\lambda ([Figure 2](https://arxiv.org/html/2512.04704v1#S4.F2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(b)). Within this range of λ\lambda, neither utu\_{t} nor πt\pi\_{t} reach its bounds (no saturation occurs). As λ\lambda increases, both maxt⁡|θt|\max\_{t}|\theta\_{t}| and maxt⁡|ξt|\max\_{t}|\xi\_{t}| grow ([Figure 2](https://arxiv.org/html/2512.04704v1#S4.F2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(c)).

We further analyze the robustness–efficiency trade-off, parameterized by the adversary strength λ\lambda (where larger λ\lambda implies a stronger adversary and weaker robustness), as in [Algorithm 3](https://arxiv.org/html/2512.04704v1#alg3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk").

Algorithm 3  Robustness–efficiency trade-off ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"))

1:Input: Grids {λmi}i=1I,{λvj}j=1J\{\lambda\_{m}^{i}\}\_{i=1}^{I},\{\lambda\_{v}^{j}\}\_{j=1}^{J}, baseline parameters p0p\_{0}.

2:Output: Heatmaps and trade-off curves.

3:Part 1: Heatmaps

4:for i=1→Ii=1\to I do

5:  for j=1→Jj=1\to J do

6:   Update parameters: p←p0p\leftarrow p\_{0} with λmi,λvj\lambda\_{m}^{i},\lambda\_{v}^{j}.

7:   Simulate and extract J​[i,j],u¯​[i,j],π¯​[i,j],vT​[i,j]J[i,j],\bar{u}[i,j],\bar{\pi}[i,j],v\_{T}[i,j].

8:Generate heatmaps (panels (a) to (d))

9:Part 2: Trade-off Curves

10:Fix λv=0.02\lambda\_{v}=0.02, extract u¯​(λm)\bar{u}(\lambda\_{m}) and π¯​(λm)\bar{\pi}(\lambda\_{m}) ⊳\triangleright Panel (e)

11:Fix λm=0.02\lambda\_{m}=0.02, extract u¯​(λv)\bar{u}(\lambda\_{v}) and π¯​(λv)\bar{\pi}(\lambda\_{v}) ⊳\triangleright Panel (f)

12:Plot trade-off curves

For each pair (λm,λv)(\lambda\_{m},\lambda\_{v}), the procedure first obtains time-varying quadratic value coefficients, and then uses these coefficients to compute optimal controls together with the associated adversarial distortions. From the forward simulation, the simulation aggregates the total cost JJ over the horizon, the average policy rate u¯\bar{u}, the average monitoring intensity π¯\bar{\pi}, and the terminal variance vTv\_{T}. Repeating this workflow on a grid in (λm,λv)(\lambda\_{m},\lambda\_{v}) maps the robustness–efficiency tradeoff. This sensitivity analysis is conducted over 100×100=10,000100\times 100=10,000 combinations of (λm,λv)∈[0.005,0.2]2(\lambda\_{m},\lambda\_{v})\in[0.005,0.2]^{2} on linearly spaced grids.

![Refer to caption](fig_3.png)


Figure 3: Robustness–efficiency tradeoff. (a)–(d): Heatmaps of cost, controls, and terminal variance over the (λm,λv)(\lambda\_{m},\lambda\_{v}) plane. (e)–(f): Cross-sectional policy response curves fixing one adversary parameter. The heatmaps show the asymmetric policy response to λm\lambda\_{m} and λv\lambda\_{v}, with JJ increasing along λv\lambda\_{v} but remaining insensitive to λm\lambda\_{m}.

[Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") summarizes the resulting robustness–efficiency landscape. The four heatmaps over (λm,λv)(\lambda\_{m},\lambda\_{v}) report JJ, u¯\bar{u}, π¯\bar{\pi}, and vTv\_{T} ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(a),(b),(c),(d)). [Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(a) decomposes [Figure 2](https://arxiv.org/html/2512.04704v1#S4.F2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(a). The total cost is minimized at lower λv\lambda\_{v} and increases as λv\lambda\_{v} rises, but not with λm\lambda\_{m} ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(a)). Both u¯\bar{u} and π¯\bar{\pi} decline with λm\lambda\_{m} ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(b),(c)). vTv\_{T} rises with λv\lambda\_{v} ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(d)).

The two trade-off plots show u¯\bar{u} (left axis) and π¯\bar{\pi} (right axis) ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(e),(f)). These plots decompose [Figure 2](https://arxiv.org/html/2512.04704v1#S4.F2 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(b): λm\lambda\_{m} varies with λv\lambda\_{v} fixed at 0.020.02 ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(e)), and λv\lambda\_{v} varies with λm\lambda\_{m} fixed at 0.020.02 ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(f)). Both u¯\bar{u} and π¯\bar{\pi} decline as λm\lambda\_{m} increases ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(e)), but they do not respond to increases in λv\lambda\_{v} ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(f)). utu\_{t} does not react to λv\lambda\_{v} because it is the controller for the mean, and πt\pi\_{t} shows little response because its value is largely anchored by non-adversarial parameters (w¯2\bar{w}\_{2} and β\beta).

Importantly, π¯\bar{\pi} decreases as λm\lambda\_{m} increases ([Figure 3](https://arxiv.org/html/2512.04704v1#S4.F3 "In 4.2 Adversary strength analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(c),(e)). When λm\lambda\_{m} rises, the adversarial distortion θt∗=2​λm​∂mV\theta\_{t}^{\*}=2\lambda\_{m}\partial\_{m}V becomes the dominant driver of instability, forcing the CB to prioritize the mean channel. This trade-off, captured by the coupled Riccati system, reduces the variance weight w2​(ut)w\_{2}(u\_{t}) (as utu\_{t} becomes more aggressive), which in turn lowers the marginal cost of variance ∂vV\partial\_{v}V, which in turn reduces the optimal monitoring intensity πt∗=χ​∂vV2​R\pi\_{t}^{\*}=\frac{\chi\partial\_{v}V}{2R}. This may be interpreted as a resource-allocation shift at the CB.

The total cost JJ consists essentially of w1​mt2,w2​(ut)​vt,R​πt2,w\_{1}m\_{t}^{2},w\_{2}(u\_{t})v\_{t},R\pi\_{t}^{2}, and Ru​ut2R\_{u}u\_{t}^{2}. When λv\lambda\_{v} increases while λm\lambda\_{m} remains fixed, the controls (ut,πt)(u\_{t},\pi\_{t}) and the mean mtm\_{t} stay stable, so their associated costs do not increase. However, since λv\lambda\_{v} increases the variance vtv\_{t} while πt\pi\_{t} remains almost unchanged, the term w2​(ut)​vtw\_{2}(u\_{t})v\_{t} rises, thereby increasing JJ (see Remarks [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [4.4](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem4 "Remark 4.4 (scope of over-monitoring effects). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")).

This asymmetric sensitivity reflects a general mechanism: the system is more vulnerable to adversarial pressure on the weaker control channel. Under our baseline parameters, the mean control effectiveness η2Ru=1.28\frac{\eta^{2}}{R\_{u}}=1.28 exceeds the variance control effectiveness χ2R=1.00\frac{\chi^{2}}{R}=1.00, making the variance channel more exposed. Consequently, JJ responds primarily to λv\lambda\_{v}. The direction of this asymmetry would reverse if χ2R>η2Ru\frac{\chi^{2}}{R}>\frac{\eta^{2}}{R\_{u}}.

### 4.3 Parameter sensitivity analysis

We then study how model primitives affect outcomes, as in [Algorithm 4](https://arxiv.org/html/2512.04704v1#alg4 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"). Adversary strength parameters are held fixed at λm=λv=0.02\lambda\_{m}=\lambda\_{v}=0.02. For each parameter configuration, we compute the total cost JJ, the terminal variance vTv\_{T}, and the saturation levels of the controls utu\_{t} and πt\pi\_{t}.

Algorithm 4  Parameter sensitivity ([Figure 4](https://arxiv.org/html/2512.04704v1#S4.F4 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")) and control saturation analysis ([Figure 5](https://arxiv.org/html/2512.04704v1#S4.F5 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"))

1:Input: Baseline p0p\_{0} (with λm=λv=0.02\lambda\_{m}=\lambda\_{v}=0.02); grids for each parameter ϑ∈{η,χ,β,κ,Ru,R}\vartheta\in\{\eta,\chi,\beta,\kappa,R\_{u},R\}.

2:Output: Sensitivity curves and saturation profiles.

3:for each parameter ϑ\vartheta do

4:  for each value ϑ′\vartheta^{\prime} in grid 𝒢ϑ\mathcal{G}\_{\vartheta} do

5:   Update parameters: p←p0p\leftarrow p\_{0} with ϑ←ϑ′\vartheta\leftarrow\vartheta^{\prime}.

6:   Simulate and compute metrics: J,vT,u¯,π¯,Su,SπJ,v\_{T},\bar{u},\bar{\pi},S\_{u},S\_{\pi}

7:  Generate panels in [Figure 4](https://arxiv.org/html/2512.04704v1#S4.F4 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"): J​(ϑ)J(\vartheta) and vT​(ϑ)v\_{T}(\vartheta)

8:  Generate panels in [Figure 5](https://arxiv.org/html/2512.04704v1#S4.F5 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"): Su​(ϑ)S\_{u}(\vartheta) and Sπ​(ϑ)S\_{\pi}(\vartheta)

![Refer to caption](fig_4.png)


Figure 4: Parameter sensitivity analysis. JJ and vTv\_{T} are most sensitive to χ\chi, β\beta, and RR. The increase in JJ with χ\chi (panel (b)) reflects the over-monitoring cost at the vt=0v\_{t}=0 boundary (Remarks [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [4.4](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem4 "Remark 4.4 (scope of over-monitoring effects). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")).

In both [Figures 4](https://arxiv.org/html/2512.04704v1#S4.F4 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [5](https://arxiv.org/html/2512.04704v1#S4.F5 "Figure 5 ‣ 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"), the dotted vertical line in each panel indicates the baseline value of the parameter being varied. The sensitivity analysis shows that, within the tested ranges, monitoring effectiveness χ\chi, mean reversion β\beta, and monitoring cost RR are the most influential parameters for both JJ and vTv\_{T} ([Figure 4](https://arxiv.org/html/2512.04704v1#S4.F4 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(b),(c),(f)).

In particular, when χ\chi increases, the variance drift becomes more sensitive
to monitoring ([Figure 4](https://arxiv.org/html/2512.04704v1#S4.F4 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(b)). While this makes variance reduction more
effective per unit of π\pi, high χ\chi drives vtv\_{t} to zero rapidly. At
vt=0v\_{t}=0, the variance drift satisfies v˙t=Σ2+ξt−χ​πt\dot{v}\_{t}=\Sigma^{2}+\xi\_{t}-\chi\pi\_{t}.
When χ​πt>Σ2+ξt\chi\pi\_{t}>\Sigma^{2}+\xi\_{t}, the control force exceeds noise plus
adversarial pressure, driving variance to zero and keeping it there. Under
baseline parameters with high χ\chi, this condition is satisfied, confirming
that vt=0v\_{t}=0 reflects genuine control dominance.

However, once vtv\_{t} reaches zero, the Riccati-based feedback
π∗=χ​∂vV2​R\pi^{\*}=\frac{\chi\partial\_{v}V}{2R} continues to prescribe positive monitoring,
but further variance reduction is impossible. The resulting over-monitoring cost
R​πt2R\pi\_{t}^{2} accumulates without benefit, which is the primary reason JJ rises
despite the improved monitoring effectiveness (see Remarks [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [4.4](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem4 "Remark 4.4 (scope of over-monitoring effects). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")).

Across the tested ranges, the pass-through η\eta, state-dependent weight κ\kappa, and policy rate cost RuR\_{u} are less influential for JJ and vTv\_{T} ([Figure 4](https://arxiv.org/html/2512.04704v1#S4.F4 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(a),(d),(e)).

![Refer to caption](fig_5.png)


Figure 5: Control saturation analysis. Increasing monitoring effectiveness χ\chi not only saturates πt\pi\_{t} but also drives utu\_{t} to its bound.

In the control saturation analysis, two parameters exhibit no saturation: neither utu\_{t} nor πt\pi\_{t} reaches its bounds over the sweep ([Figure 5](https://arxiv.org/html/2512.04704v1#S4.F5 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(a),(c)). This indicates that the optimal controls remain interior across those ranges. Saturation of πt\pi\_{t} tends to arise when χ\chi increases, κ\kappa rises, or RR declines ([Figure 5](https://arxiv.org/html/2512.04704v1#S4.F5 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(b),(d),(f)). Saturation of utu\_{t} emerges when χ\chi increases ([Figure 5](https://arxiv.org/html/2512.04704v1#S4.F5 "In 4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")(b)).

When χ\chi increases, χ2R\frac{\chi^{2}}{R} becomes stronger. The Riccati system responds by increasing the magnitude of the a12a\_{12} coupling term, which links variance vtv\_{t} to the mean controller utu\_{t}. This stronger coupling amplifies the variance contribution to the optimal policy rate ut∗=−η​(a1+2​a11​m+a12​v)+κ​v2​Ruu\_{t}^{\*}=-\frac{\eta(a\_{1}+2a\_{11}m+a\_{12}v)+\kappa v}{2R\_{u}}, creating a more negative ut∗u\_{t}^{\*} and causing the policy rate to saturate at its lower bound uminu\_{\min}.

### 4.4 Loss of control

We further analyze the saturation of the policy instruments identified in [section 4.3](https://arxiv.org/html/2512.04704v1#S4.SS3 "4.3 Parameter sensitivity analysis ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"). [Figure 6](https://arxiv.org/html/2512.04704v1#S4.F6 "In 4.4 Loss of control ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") presents the loss-of-control diagnostics over the (χ,β)(\chi,\beta) plane, produced according to [Algorithm 5](https://arxiv.org/html/2512.04704v1#alg5 "In 4.4 Loss of control ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"). The base layer is a heatmap of total time at bounds (the share of the horizon during which either control is at its limit), over which we overlay iso-cost contours of JJ. Axes place χ\chi on the horizontal and β\beta on the vertical. Adversary intensities are fixed at λm=λv=0.02\lambda\_{m}=\lambda\_{v}=0.02.

Algorithm 5  Loss-of-control map ([Figure 6](https://arxiv.org/html/2512.04704v1#S4.F6 "In 4.4 Loss of control ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk"))

1:Input: Baseline p0p\_{0}; grids for effectiveness χ\chi and reversion β\beta.

2:Output: Heatmap of saturation and iso-cost contours.

3:for each χi\chi\_{i} in grid, each βj\beta\_{j} in grid do

4:  Update p←p0p\leftarrow p\_{0} with χ←χi,β←βj\chi\leftarrow\chi\_{i},\beta\leftarrow\beta\_{j}.

5:  Stability Check:

6:  if Robustness-breakdown (4​λv>χ2R4\lambda\_{v}>\frac{\chi^{2}}{R} or 4​λm>η2Ru4\lambda\_{m}>\frac{\eta^{2}}{R\_{u}}) then

7:   Mark point (i,j)(i,j) as “Robustness-breakdown”

8:  else

9:   Simulate and compute metrics

10:   Hi​j←H\_{ij}\leftarrow Total time at bounds (Su+Sπ)(S\_{u}+S\_{\pi})

11:   Ji​j←J\_{ij}\leftarrow Total cost

12:Plot heatmap of Hi​jH\_{ij} with overlaid contours of Ji​jJ\_{ij}

![Refer to caption](fig_6.png)


Figure 6: Loss-of-control map over (χ,β)(\chi,\beta). This figure identifies the two distinct phase transitions: robustness-breakdown and control saturation. It shows total time at bounds, defined as the sum of saturation percentages for both controls (Su+Sπ∈[0,2]S\_{u}+S\_{\pi}\in[0,2]). Iso-cost contours overlay the saturation regions, and red crosses mark robustness-breakdown points. Note that the increasing trends in iso-cost contours in higher χ\chi regions reflect the over-monitoring cost (Remarks [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [4.4](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem4 "Remark 4.4 (scope of over-monitoring effects). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")).

[Figure 6](https://arxiv.org/html/2512.04704v1#S4.F6 "In 4.4 Loss of control ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") illustrates the central trade-off between the system’s inherent stability (provided by β\beta) and the CB’s monitoring effectiveness χ\chi. We identify two distinct phase transitions corresponding to a loss-of-control. First, a robustness-breakdown (the “Robustness-breakdown” points, see Remark [4.1](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem1 "Remark 4.1 (robustness-breakdown threshold). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")) occurs at χ≤4​λv​R\chi\leq\sqrt{4\lambda\_{v}R} (approximately 0.140.14 under baseline λv\lambda\_{v} and RR), where the CB’s stabilizing control term (χ2R\frac{\chi^{2}}{R}) is too weak to offset the destabilizing adversarial term (4​λv4\lambda\_{v}), preventing the Riccati system from admitting a stable solution. Second, the heatmap exhibits control saturation (the neighborhood of the “Saturated” point). The borderline of this saturated region represents the critical policy threshold where controls first reach their bounds. This saturation frontier is crossed when β\beta decreases (forcing the CB to compensate for the lack of inherent mean reversion) or when χ\chi increases. This latter effect is twofold: increasing χ\chi not only drives πt∗\pi\_{t}^{\*} to its bound (πm​a​x\pi\_{max}) but also causes utu\_{t} to saturate at its bound through the Riccati a12a\_{12} coupling. The “Baseline” reference point exists in the stable, interior region. Overall, the plot shows a phase transition from interior control to high boundary usage of policy instruments as χ\chi increases and β\beta declines, and the iso-cost contours broadly track these saturation gradients. At the baseline parameters, optimizing the CB’s objective JJ maintains the policy instruments within the interior region, but this property is lost as parameters approach the saturation frontier.

## 5 Discussion

##### Simulation results.

Our simulations show that the total cost JJ is highly sensitive to the variance adversary λv\lambda\_{v} but relatively insensitive to the mean adversary λm\lambda\_{m} within the stable region. This asymmetry is driven by the *net stabilizing margins* in the Riccati dynamics (defined by the difference between control effectiveness and adversarial pressure: η2Ru−4​λm\frac{\eta^{2}}{R\_{u}}-4\lambda\_{m} versus χ2R−4​λv\frac{\chi^{2}}{R}-4\lambda\_{v}). Under our baseline parameters, the stabilizing coefficient for the mean (η2Ru=1.28\frac{\eta^{2}}{R\_{u}}=1.28) exceeds that of the variance (χ2R=1.00\frac{\chi^{2}}{R}=1.00), creating a larger safety margin against adversarial distortions. Consequently, the optimal distortion ξt\xi\_{t} induces larger state deviations in vtv\_{t} compared to the effect of θt\theta\_{t} on mtm\_{t}. This effect is visible in the path simulations: while the baseline case is affected by over-monitoring at vt=0v\_{t}=0, a strong adversary overwhelms the control effort, preventing vtv\_{t} from settling at zero.

The parameter sweeps reveal complex coordination between controls. For example, when the mean adversary λm\lambda\_{m} increases, the monitoring policy πt\pi\_{t} decreases as the CB shifts resources to the mean channel via the w2​(ut)w\_{2}(u\_{t}) coupling. Notably, when monitoring effectiveness χ\chi is large, the total cost JJ can increase with χ\chi even though the value function V​(0,x0)V(0,x\_{0}) decreases. This reflects a structural limitation of applying unconstrained LQ feedback to state-constrained dynamics: high χ\chi drives the variance vtv\_{t} to its lower bound of zero, where the Riccati feedback continues to prescribe positive monitoring πt>0\pi\_{t}>0 based on the positive ∂vV\partial\_{v}V. The resulting over-monitoring accumulates as R​πt2R\pi\_{t}^{2} cost without yielding further variance reduction (Remark [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")). This coordination effect is also observed in the saturation regimes: increasing χ\chi not only causes πt\pi\_{t} to reach its bound, but effectively forces utu\_{t} to saturate at its bound by strengthening the a12a\_{12} Riccati coupling, demonstrating that the two policy tools are deeply linked via the cross-terms in the value function.

Finally, our loss-of-control analysis illustrates the central trade-off between the system’s inherent stability and the CB’s monitoring effectiveness. We identify two distinct, structural phase transitions. First, a robustness-breakdown occurs when the control power is insufficient to offset the adversarial strength (*e.g.,* when χ\chi is low), violating the Riccati stability condition (4​λv>χ2R4\lambda\_{v}>\frac{\chi^{2}}{R} or 4​λm>η2Ru4\lambda\_{m}>\frac{\eta^{2}}{R\_{u}}). Second, control saturation emerges when the unconstrained optimal feedback exceeds the admissible bounds, a regime triggered either when high χ\chi amplifies the feedback gain beyond πm​a​x\pi\_{max} or when low β\beta necessitates intervention beyond um​i​nu\_{min}.

##### Policy implications.

An important policy implication is that monetary policy utu\_{t} and bank monitoring πt\pi\_{t} are deeply coordinated and cannot be managed in isolation. Our model reveals critical, structural trade-offs. For instance, a strong monetary policy response to the mean adversary λm\lambda\_{m} optimally forces the CB to reduce πt\pi\_{t} as a resource-allocation shift—a direct, parameter-independent consequence of the w2​(ut)w\_{2}(u\_{t}) coupling. Furthermore, the robustness-breakdown is determined by the control channel with the minimum stability margin (the smaller of η2Ru−4​λm\frac{\eta^{2}}{R\_{u}}-4\lambda\_{m} and χ2R−4​λv\frac{\chi^{2}}{R}-4\lambda\_{v}). Since the Riccati solution explodes if the quadratic coefficient becomes positive for either channel, the model’s capacity to absorb uncertainty is limited by the tighter of these two margins. Under our baseline parameters where η2Ru>χ2R\frac{\eta^{2}}{R\_{u}}>\frac{\chi^{2}}{R}, the variance channel has the tighter margin, creating a specific vulnerability to λv\lambda\_{v} that would only reverse if χ2R\frac{\chi^{2}}{R} were increased significantly. Furthermore, increasing monitoring effectiveness χ\chi can trigger saturation in other policy tools due to complex Riccati feedback, or lead to inefficient over-monitoring when variance reaches its lower bound, where π∗∝∂vV\pi^{\*}\propto\partial\_{v}V continues to incur quadratic costs R​π2R\pi^{2} despite yielding zero marginal reduction in vtv\_{t}. These findings suggest that CBs must coordinate (jointly optimize) their policy instruments, accounting for the cross-channel feedback that links these tools.

##### Limitations.

Our analysis is subject to several limitations inherent to the LQ-MFC framework.

1. 1.

   Linear dynamics and quadratic objectives, while analytically transparent, may overlook nonlinearities that emerge under extreme stress.
2. 2.

   The assumption of continuous controls may ignore the discrete or binary nature of certain policy interventions, such as emergency lending facilities or bank resolution decisions.
3. 3.

   The LQ cost structure presumes symmetric penalties for deviations above and below targets, whereas CBs may face asymmetric loss functions in which undersupplying liquidity is far more costly than oversupplying it during crises.

These limitations suggest that the phase transitions we identify may occur at lower adversary strengths, implying greater fragility than our baseline model indicates. Furthermore, our unconstrained Riccati solution may not optimally handle the state constraint vt≥0v\_{t}\geq 0: when variance reaches zero, the feedback policy prescribes inefficient over-monitoring (see Remarks [4.3](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem3 "Remark 4.3 (over-monitoring and state constraints). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk") and [4.4](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem4 "Remark 4.4 (scope of over-monitoring effects). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")).

##### Potential model extensions.

Our framework serves as a tractable baseline that admits several extensions.

1. 1.

   Incorporating *jump-diffusions* would capture fire-sale shocks, where Poisson jumps model sudden asset liquidations generating discontinuous increases in cross-sectional dispersion.
2. 2.

   *Exogenous regime-switching* parameters could model transitions between normal and crisis states, where model coefficients depend on a finite Markov chain kt∈{1,…,K}k\_{t}\in\{1,\dots,K\} independent of the state.
3. 3.

   Introducing *network-weighted mean exposure* ∑jωi​j​Ltj\sum\_{j}\omega\_{ij}L\_{t}^{j} would capture heterogeneous spillovers and core–periphery dynamics.

These extensions would likely reinforce our understanding that the system’s true stability region may be narrower than our baseline model suggests. As detailed in our stability analysis, the system fails when the adversary’s strength overpowers the control channels. While exogenous regime switching remains tractable (yielding a system of
coupled Riccati equations), it would generally shrink the stability region,
as the coupled solution must remain bounded across all regime configurations. Furthermore, jump-diffusions would introduce a strictly positive, uncontrolled source of dispersion (λJ​𝔼​[Z2]\lambda\_{J}\mathbb{E}[Z^{2}]) that elevates the variance floor, reducing the effective buffer against destabilization. Together, these mechanisms suggest that the stable region identified in our baseline model may underestimate the system’s true fragility.

##### Future research directions.

When nonlinear monitoring costs or partial observability prevent closed-form Riccati solutions, numerical solutions to the robust MFC problem can be obtained using PG methods.555This provides a foundation for applying data-driven reinforcement learning to systemic risk management. Recent developments in PG methods include Giegrich, Reisinger, and Zhang [[28](https://arxiv.org/html/2512.04704v1#bib.bib28)], Reisinger, Stockinger, and Zhang [[43](https://arxiv.org/html/2512.04704v1#bib.bib43)], and Hambly, Xu, and Yang [[30](https://arxiv.org/html/2512.04704v1#bib.bib30)]. A natural extension is to formulate an MFG where individual banks optimize their liquidity positions while the CB sets aggregate policy. In this setting, the Riccati equations are replaced by a coupled forward-backward system, whose fixed point characterizes the equilibrium between banks and the CB. For recent developments in MFG formulations, see Cont and Hu [[17](https://arxiv.org/html/2512.04704v1#bib.bib17)]. Moreover, the single CB framework can be extended to include multiple regulatory authorities, in the spirit of Veraart and Aldasoro [[48](https://arxiv.org/html/2512.04704v1#bib.bib48)].666This aligns with institutional practice in Japan, where both the Financial Services Agency (primary regulator) and the Bank of Japan monitor banks.

## 6 Conclusion

##### Main contributions.

This paper contributes to the systemic risk literature in financial mathematics by developing a robust LQ-MFC framework that incorporates multiple coordinated policy instruments under model uncertainty. We jointly optimize interest rate policy utu\_{t} and supervisory monitoring intensity πt\pi\_{t} against worst-case distortions. The distinguishing feature is a variance weight w2​(ut)=w¯2+κ​utw\_{2}(u\_{t})=\bar{w}\_{2}+\kappa u\_{t} that depends on the policy rate, generating coupling effects between monetary policy and cross-sectional dispersion, creating control–variance interactions in the optimal control Hamiltonian. This coupling captures the heterogeneous transmission of monetary policy through the banking system, where higher policy rates amplify dispersion costs—a mechanism that emerges from bank heterogeneity but is absent when κ=0\kappa=0.

##### Theoretical foundations.

We establish viscosity solutions for the robust HJBI equation, prove uniqueness through comparison principles, and provide verification theorems for optimal feedback controls. The LQ structure with the coupling term κ\kappa leads to a modified Riccati system that admits closed-form solutions despite the control–state interactions. These analytical results maintain tractability and enable practical numerical implementation.

##### Instrument complementarity.

Our model demonstrates complementarity between interest rate and monitoring policies under model uncertainty. Monitoring primarily affects variance while interest rates target the mean, creating distinct stabilization channels. The policy rate–variance coupling through κ\kappa generates interaction effects: monetary policy influences cross-sectional dispersion, while heterogeneity feeds back into optimal rate-setting. Under robustness concerns, this coupling becomes particularly important as the adversary optimally targets the channel with lower control effectiveness (the smaller of η2Ru\frac{\eta^{2}}{R\_{u}} and χ2R\frac{\chi^{2}}{R}).

##### Coordinated policy responses.

Our simulations reveal that the system’s sensitivity to model uncertainty is driven by the net stabilizing margins. Under our baseline parameters, this results in a pronounced vulnerability to the variance adversary λv\lambda\_{v} while remaining robust to the mean adversary λm\lambda\_{m}. This asymmetry arises from the higher effectiveness of the interest rate policy relative to monitoring. Beyond this asymmetry, we identify fundamental coordination trade-offs. For instance, an increase in λm\lambda\_{m} forces a decrease in monitoring πt\pi\_{t} as the CB reallocates resources via the w2​(ut)w\_{2}(u\_{t}) coupling.

We further identify two distinct loss-of-control regimes: robustness-breakdown and control saturation. A breakdown threshold exists where system stability fails when the adversary’s influence overwhelms the CB’s control effectiveness. Separately, control saturation arises from complex Riccati interactions, even within the stable region. For instance, increasing monitoring effectiveness χ\chi not only drives πt\pi\_{t} to its bound but also raises total cost JJ (due to over-monitoring when vtv\_{t} reaches zero) and pushes the policy rate utu\_{t} to its bound via the a12a\_{12} Riccati coupling.

##### Possible extensions.

Important extensions include incorporating jump processes for sudden liquidity shocks and exogenous regime-switching dynamics (see [section 5](https://arxiv.org/html/2512.04704v1#S5 "5 Discussion ‣ Coordinated Mean-Field Control for Systemic Risk")). The framework developed here—combining robust control, mean-field approximations, and multiple instruments—offers a foundation for future developments.

## Appendix A Propagation-of-Chaos for the *N*-bank system

This appendix establishes PoC (Propagation-of-Chaos) for the NN-bank system, justifying the mean-field approximation used in the main text (see Carmona and Delarue [[13](https://arxiv.org/html/2512.04704v1#bib.bib13)]). While the main text analyzes deterministic moment dynamics, the underlying bank system is stochastic with both idiosyncratic and common noise.

Consider NN banks with liquidity gaps following:

|  |  |  |
| --- | --- | --- |
|  | d​Lti,N=[−β​(Lti,N−mtN)+η​ut+θt]​d​t+σL​d​Wti+σc​d​Bt,i=1,…,N,dL\_{t}^{i,N}=\Big[-\beta\big(L\_{t}^{i,N}-m\_{t}^{N}\big)+\eta\,u\_{t}+\theta\_{t}\Big]\,dt\;+\;\sigma\_{L}\,dW\_{t}^{i}\;+\;\sigma\_{c}\,dB\_{t},\quad i=1,\dots,N, |  |

where mtN=1N​∑j=1NLtj,Nm\_{t}^{N}=\tfrac{1}{N}\sum\_{j=1}^{N}L\_{t}^{j,N} is the empirical mean, {Wi}i=1N\{W^{i}\}\_{i=1}^{N} are i.i.d. standard Brownian motions, and BB is a common Brownian motion independent of all WiW^{i}.

Assume (L0i,N)i=1,…,N(L\_{0}^{i,N})\_{i=1,\dots,N} are i.i.d. with 𝔼​|L0i,N|2<∞\mathbb{E}|L\_{0}^{i,N}|^{2}<\infty (and 𝔼​|L0i,N|4<∞\mathbb{E}|L\_{0}^{i,N}|^{4}<\infty for Corollary [A.4](https://arxiv.org/html/2512.04704v1#A1.Thmtheorem4 "Corollary A.4 (convergence of moments). ‣ Appendix A Propagation-of-Chaos for the N-bank system ‣ Coordinated Mean-Field Control for Systemic Risk")), independent of (B,W1,…,WN)(B,W^{1},\dots,W^{N}). We use the conditional (common-noise) law and mean

|  |  |  |
| --- | --- | --- |
|  | μt:=ℒ(Lt∣ℱtB),mt:=𝔼[Lt∣ℱtB],ℱtB:=σ(Bs:s≤t).\mu\_{t}:=\mathcal{L}(L\_{t}\mid\mathcal{F}\_{t}^{B}),\quad m\_{t}:=\mathbb{E}[L\_{t}\mid\mathcal{F}\_{t}^{B}],\quad\mathcal{F}\_{t}^{B}:=\sigma(B\_{s}:s\leq t). |  |

The controls (ut,πt)(u\_{t},\pi\_{t}) and adversarial distortions (θt,ξt)(\theta\_{t},\xi\_{t}) are progressively measurable and bounded processes, chosen according to the robust control problem in [section 3](https://arxiv.org/html/2512.04704v1#S3 "3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Note that πt\pi\_{t} affects variance but not individual dynamics directly, while ξt\xi\_{t} enters only at the aggregate level.

###### Assumption A.1 (regularity for PoC).

The parameters satisfy β,η>0\beta,\eta>0 and σL,σc≥0\sigma\_{L},\sigma\_{c}\geq 0. Controls are bounded: ut∈[umin,umax]u\_{t}\in[u\_{\min},u\_{\max}], πt∈[0,πmax]\pi\_{t}\in[0,\pi\_{\max}]. Adversarial distortions satisfy |θt|≤Cθ|\theta\_{t}|\leq C\_{\theta} and |ξt|≤Cξ|\xi\_{t}|\leq C\_{\xi} for constants Cθ,CξC\_{\theta},C\_{\xi} determined by the KL penalty parameter λ\lambda.

Assumption [A.1](https://arxiv.org/html/2512.04704v1#A1.Thmtheorem1 "Assumption A.1 (regularity for PoC). ‣ Appendix A Propagation-of-Chaos for the N-bank system ‣ Coordinated Mean-Field Control for Systemic Risk") holds under Assumption [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk") on the baseline parameter region considered.

###### Lemma A.2 (uniform second moments).

Under Assumption [A.1](https://arxiv.org/html/2512.04704v1#A1.Thmtheorem1 "Assumption A.1 (regularity for PoC). ‣ Appendix A Propagation-of-Chaos for the N-bank system ‣ Coordinated Mean-Field Control for Systemic Risk"), there exists CT<∞C\_{T}<\infty such that, for all N≥1N\geq 1:

|  |  |  |
| --- | --- | --- |
|  | sup1≤i≤N𝔼​[sup0≤t≤T|Lti,N|2]≤CT​(1+𝔼​|L0i,N|2).\sup\_{1\leq i\leq N}\mathbb{E}\Big[\sup\_{0\leq t\leq T}|L\_{t}^{i,N}|^{2}\Big]\leq C\_{T}\big(1+\mathbb{E}|L\_{0}^{i,N}|^{2}\big). |  |

###### Proof.

Apply Ito’s formula to |Lti,N|2|L\_{t}^{i,N}|^{2}. The drift satisfies, using boundedness of ut,θtu\_{t},\theta\_{t} and 𝔼​[Lti,N​mtN]≤(𝔼​|Lti,N|2)1/2​(𝔼​|mtN|2)1/2\mathbb{E}[L\_{t}^{i,N}m\_{t}^{N}]\leq(\mathbb{E}|L\_{t}^{i,N}|^{2})^{1/2}(\mathbb{E}|m\_{t}^{N}|^{2})^{1/2},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[2​Lti,N​(−β​(Lti,N−mtN)+η​ut+θt)]≤−β​𝔼​|Lti,N|2+C​(1+𝔼​|Lti,N|2).\mathbb{E}\big[2L\_{t}^{i,N}(-\beta(L\_{t}^{i,N}-m\_{t}^{N})+\eta u\_{t}+\theta\_{t})\big]\leq-\beta\,\mathbb{E}|L\_{t}^{i,N}|^{2}+C\big(1+\mathbb{E}|L\_{t}^{i,N}|^{2}\big). |  |

The quadratic variation contributes σL2+σc2\sigma\_{L}^{2}+\sigma\_{c}^{2}. By the Burkholder–Davis–Gundy inequality (*e.g.,* Karatzas and Shreve [[36](https://arxiv.org/html/2512.04704v1#bib.bib36)], Theorem 3.28) and Young’s inequality (*e.g.,* Royden and Fitzpatrick [[44](https://arxiv.org/html/2512.04704v1#bib.bib44)], Section 7.2) applied to the martingale terms, followed by Gronwall’s inequality (*e.g.,* Øksendal [[51](https://arxiv.org/html/2512.04704v1#bib.bib51)], Chapter 5), we obtain the stated sup-in-time bound.
∎

###### Theorem A.3 (propagation-of-chaos).

Let (Lti)i≥1(L\_{t}^{i})\_{i\geq 1} be i.i.d. copies of the McKean–Vlasov limit solving

|  |  |  |
| --- | --- | --- |
|  | d​Lti=[−β​(Lti−mt)+η​ut+θt]​d​t+σL​d​Wti+σc​d​Bt,dL\_{t}^{i}=\big[-\beta(L\_{t}^{i}-m\_{t})+\eta u\_{t}+\theta\_{t}\big]\,dt+\sigma\_{L}\,dW\_{t}^{i}+\sigma\_{c}\,dB\_{t}, |  |

where mt=𝔼​[Lti∣ℱtB]m\_{t}=\mathbb{E}[L\_{t}^{i}\mid\mathcal{F}\_{t}^{B}]. Under Assumption [A.1](https://arxiv.org/html/2512.04704v1#A1.Thmtheorem1 "Assumption A.1 (regularity for PoC). ‣ Appendix A Propagation-of-Chaos for the N-bank system ‣ Coordinated Mean-Field Control for Systemic Risk") and synchronous coupling (same Brownian motions WiW^{i} and BB), there exists CT<∞C\_{T}<\infty such that

|  |  |  |
| --- | --- | --- |
|  | max1≤i≤N⁡𝔼​[sup0≤t≤T|Lti,N−Lti|2]1/2≤CT​N−1/2.\max\_{1\leq i\leq N}\mathbb{E}\Big[\sup\_{0\leq t\leq T}|L\_{t}^{i,N}-L\_{t}^{i}|^{2}\Big]^{1/2}\leq C\_{T}N^{-1/2}. |  |

###### Proof.

Let eti:=Lti,N−Ltie\_{t}^{i}:=L\_{t}^{i,N}-L\_{t}^{i}. By synchronous coupling, the noise cancels and

|  |  |  |
| --- | --- | --- |
|  | d​eti=−β​(eti−(mtN−mt))​d​t,dd​t​𝔼​|eti|2≤C​(𝔼​|eti|2+𝔼​|mtN−mt|2).de\_{t}^{i}=-\beta\big(e\_{t}^{i}-(m\_{t}^{N}-m\_{t})\big)\,dt,\quad\frac{d}{dt}\,\mathbb{E}|e\_{t}^{i}|^{2}\;\leq\;C\Big(\mathbb{E}|e\_{t}^{i}|^{2}+\mathbb{E}|m\_{t}^{N}-m\_{t}|^{2}\Big). |  |

Decompose the mean error with m¯tN:=1N​∑j=1NLtj\bar{m}\_{t}^{N}:=\tfrac{1}{N}\sum\_{j=1}^{N}L\_{t}^{j} (i.i.d. mean-field copies):

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|mtN−mt|2≤2​𝔼​|mtN−m¯tN|2+2​𝔼​|m¯tN−mt|2≤2N​∑j=1N𝔼​|Ltj,N−Ltj|2+2N​𝔼​[Var​(Lt∣ℱtB)].\mathbb{E}|m\_{t}^{N}-m\_{t}|^{2}\leq 2\,\mathbb{E}|m\_{t}^{N}-\bar{m}\_{t}^{N}|^{2}+2\,\mathbb{E}|\bar{m}\_{t}^{N}-m\_{t}|^{2}\leq\frac{2}{N}\sum\_{j=1}^{N}\mathbb{E}|L\_{t}^{j,N}-L\_{t}^{j}|^{2}+\frac{2}{N}\,\mathbb{E}\big[\mathrm{Var}(L\_{t}\mid\mathcal{F}\_{t}^{B})\big]. |  |

Plugging this into the differential inequality and applying Gronwall’s inequality yields 𝔼​|eti|2≤CT​N−1\mathbb{E}|e\_{t}^{i}|^{2}\leq C\_{T}N^{-1}, hence the stated N−1/2N^{-1/2} rate for the sup-in-time error by standard maximal inequalities.
∎

###### Corollary A.4 (convergence of moments).

Let vtN=1N​∑i=1N|Lti,N−mtN|2v\_{t}^{N}=\tfrac{1}{N}\sum\_{i=1}^{N}|L\_{t}^{i,N}-m\_{t}^{N}|^{2} be the empirical variance and assume 𝔼​|L0i,N|4<∞\mathbb{E}|L\_{0}^{i,N}|^{4}<\infty. Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|mtN−mt|]≤CT​N−1/2,𝔼​[|vtN−vt|]≤CT​N−1/2,\mathbb{E}[|m\_{t}^{N}-m\_{t}|]\leq C\_{T}N^{-1/2},\qquad\mathbb{E}[|v\_{t}^{N}-v\_{t}|]\leq C\_{T}N^{-1/2}, |  |

where vt=Var​(Lti∣ℱtB)v\_{t}=\mathrm{Var}(L\_{t}^{i}\mid\mathcal{F}\_{t}^{B}) is the conditional variance.

##### Convergence rates and finite-sample behavior.

We briefly discuss convergence rates for practical implementation.

###### Proposition A.5 (rate of convergence).

Let (mtN,vtN)(m^{N}\_{t},v^{N}\_{t}) denote the empirical mean and variance of the NN-bank system, and (mt,vt)(m\_{t},v\_{t}) the mean-field limits. Under Assumption [A.1](https://arxiv.org/html/2512.04704v1#A1.Thmtheorem1 "Assumption A.1 (regularity for PoC). ‣ Appendix A Propagation-of-Chaos for the N-bank system ‣ Coordinated Mean-Field Control for Systemic Risk"), for any T>0T>0,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T]|mtN−mt|2+|vtN−vt|2]≤C​(T)N,\mathbb{E}\left[\sup\_{t\in[0,T]}|m^{N}\_{t}-m\_{t}|^{2}+|v^{N}\_{t}-v\_{t}|^{2}\right]\leq\frac{C(T)}{N}, |  |

where C​(T)C(T) depends on the system parameters and grows polynomially in TT.

The O​(1/N)O(1/\sqrt{N}) convergence rate in L2L^{2} is standard for mean-field limits with Lipschitz coefficients. The mean-field limit becomes increasingly accurate for larger banking systems.

###### Remark A.6 (implications).

The dependence of the convergence constant C​(T)C(T) on terminal cost weights Gm,GvG\_{m},G\_{v} suggests that stronger terminal penalties require larger NN for accurate approximation. However, the robustness-breakdown thresholds (Remark [4.1](https://arxiv.org/html/2512.04704v1#S4.Thmtheorem1 "Remark 4.1 (robustness-breakdown threshold). ‣ 4 Simulations and robustness ‣ Coordinated Mean-Field Control for Systemic Risk")) are determined by the Riccati coefficients and remain valid independent of NN.

## Appendix B Technical proofs

### B.1 Proof of [Theorem 3.6](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem6 "Theorem 3.6 (viscosity characterization of the robust HJBI). ‣ 3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")

###### Proof.

We adapt the standard viscosity argument (*e.g.,* Øksendal and Sulem [[52](https://arxiv.org/html/2512.04704v1#bib.bib52)], Chapter 12) to absolutely continuous dynamics. Let (t0,x0)(t\_{0},x\_{0}) and φ∈C1\varphi\in C^{1} be such that V−φV-\varphi attains a local minimum at (t0,x0)(t\_{0},x\_{0}) with V​(t0,x0)=φ​(t0,x0)V(t\_{0},x\_{0})=\varphi(t\_{0},x\_{0}). For small δ>0\delta>0 and any stopping time τδ∈[t0,t0+δ]\tau\_{\delta}\in[t\_{0},t\_{0}+\delta], the DPP yields

|  |  |  |
| --- | --- | --- |
|  | V​(t0,x0)≤infu,πsupθ,ξ[∫t0τδℓ​(Xs,us,πs,θs,ξs)​𝑑s+V​(τδ,Xτδ)].V(t\_{0},x\_{0})\leq\inf\_{u,\pi}\sup\_{\theta,\xi}\Big[\int\_{t\_{0}}^{\tau\_{\delta}}\ell(X\_{s},u\_{s},\pi\_{s},\theta\_{s},\xi\_{s})\,ds+V(\tau\_{\delta},X\_{\tau\_{\delta}})\Big]. |  |

Since V≥φV\geq\varphi and they touch at (t0,x0)(t\_{0},x\_{0}),

|  |  |  |
| --- | --- | --- |
|  | 0≤infu,πsupθ,ξ[∫t0τδℓ​(⋅)​𝑑s+φ​(τδ,Xτδ)−φ​(t0,x0)].0\leq\inf\_{u,\pi}\sup\_{\theta,\xi}\Big[\int\_{t\_{0}}^{\tau\_{\delta}}\ell(\cdot)\,ds+\varphi(\tau\_{\delta},X\_{\tau\_{\delta}})-\varphi(t\_{0},x\_{0})\Big]. |  |

As XX is absolutely continuous and φ∈C1\varphi\in C^{1},

|  |  |  |
| --- | --- | --- |
|  | φ​(τδ,Xτδ)−φ​(t0,x0)=∫t0τδ(∂tφ+∇xφ⋅X˙s)​𝑑s+o​(δ),\varphi(\tau\_{\delta},X\_{\tau\_{\delta}})-\varphi(t\_{0},x\_{0})=\int\_{t\_{0}}^{\tau\_{\delta}}\Big(\partial\_{t}\varphi+\nabla\_{x}\varphi\cdot\dot{X}\_{s}\Big)\,ds+o(\delta), |  |

with o​(δ)/δ→0o(\delta)/\delta\to 0 uniformly by compactness of action sets. Dividing by δ\delta and letting δ↓0\delta\downarrow 0 yields

|  |  |  |
| --- | --- | --- |
|  | 0≥infu,πsupθ,ξ{ℓ​(x0,u,π,θ,ξ)+∂tφ​(t0,x0)+∇xφ​(t0,x0)⋅b​(x0,u,π,θ,ξ)},0\geq\inf\_{u,\pi}\sup\_{\theta,\xi}\Big\{\ell(x\_{0},u,\pi,\theta,\xi)+\partial\_{t}\varphi(t\_{0},x\_{0})+\nabla\_{x}\varphi(t\_{0},x\_{0})\cdot b(x\_{0},u,\pi,\theta,\xi)\Big\}, |  |

with b​(x,u,π,θ,ξ)=(η​u+θ,−2​β​v+σL2+σc2+ξ−χ​π)b(x,u,\pi,\theta,\xi)=(\eta u+\theta,\,-2\beta v+\sigma\_{L}^{2}+\sigma\_{c}^{2}+\xi-\chi\pi) as defined in [section 3.1.1](https://arxiv.org/html/2512.04704v1#S3.SS1.SSS1 "3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Optimizing in (θ,ξ)(\theta,\xi) gives the Hamiltonian representation. Hence

|  |  |  |
| --- | --- | --- |
|  | −∂tφ​(t0,x0)+H​(x0,∇xφ​(t0,x0))≥0,-\partial\_{t}\varphi(t\_{0},x\_{0})+H\big(x\_{0},\nabla\_{x}\varphi(t\_{0},x\_{0})\big)\geq 0, |  |

which proves Part 1. The terminal condition and Part 2 follow by the standard viscosity tests (*e.g.,* Fleming and Soner [[24](https://arxiv.org/html/2512.04704v1#bib.bib24)]) with functions touching from above/below at t=Tt=T. Part 3 follows from Isaacs’ condition, which is ensured under Assumption [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").
∎

### B.2 Proof of [Theorem 3.8](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem8 "Theorem 3.8 (comparison principle and uniqueness). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")

###### Proof.

We use doubling-of-variables and penalization (Crandall, Ishii, and Lions [[20](https://arxiv.org/html/2512.04704v1#bib.bib20)] and Fleming and Soner [[24](https://arxiv.org/html/2512.04704v1#bib.bib24)]), within the constrained viscosity framework on ℝ×ℝ+\mathbb{R}\times\mathbb{R}\_{+}.

##### Coercive penalization and sup of gaps.

Define, for α,γ>0\alpha,\gamma>0,

|  |  |  |
| --- | --- | --- |
|  | Ψα,γ​(t,s,x,y):=U​(t,x)−W​(s,y)−|x−y|22​α−|t−s|22​γ−ζ​(1+|x|2​q+|y|2​q),\Psi\_{\alpha,\gamma}(t,s,x,y):=U(t,x)-W(s,y)-\frac{|x-y|^{2}}{2\alpha}-\frac{|t-s|^{2}}{2\gamma}-\zeta\big(1+|x|^{2q}+|y|^{2q}\big), |  |

with small parameters ζ>0\zeta>0 and integer q≥1q\geq 1 dominating the polynomial growth. Let (tα,sα,xα,yα)(t\_{\alpha},s\_{\alpha},x\_{\alpha},y\_{\alpha}) maximize Ψα,γ\Psi\_{\alpha,\gamma} on [0,T]×[0,T]×(ℝ×ℝ+)2[0,T]\times[0,T]\times(\mathbb{R}\times\mathbb{R}\_{+})^{2}. By coercivity and growth control, |xα−yα|→0|x\_{\alpha}-y\_{\alpha}|\to 0 and |tα−sα|→0|t\_{\alpha}-s\_{\alpha}|\to 0 as α,γ↓0\alpha,\gamma\downarrow 0. Moreover, supΨα,γ→supt,x(U−W)\sup\Psi\_{\alpha,\gamma}\to\sup\_{t,x}(U-W) as α,γ↓0\alpha,\gamma\downarrow 0 then ζ↓0\zeta\downarrow 0.

##### Ishii’s lemma.

There exist jets

|  |  |  |
| --- | --- | --- |
|  | (aX,pX,X)∈𝒫¯2,+​U​(tα,xα),(aY,pY,Y)∈𝒫¯2,−​W​(sα,yα),(a\_{X},p\_{X},X)\in\overline{\mathcal{P}}^{2,+}U(t\_{\alpha},x\_{\alpha}),\quad(a\_{Y},p\_{Y},Y)\in\overline{\mathcal{P}}^{2,-}W(s\_{\alpha},y\_{\alpha}), |  |

with

|  |  |  |
| --- | --- | --- |
|  | aX=tα−sαγ,aY=−tα−sαγ,a\_{X}=\tfrac{t\_{\alpha}-s\_{\alpha}}{\gamma},\quad a\_{Y}=-\tfrac{t\_{\alpha}-s\_{\alpha}}{\gamma}, |  |

|  |  |  |
| --- | --- | --- |
|  | pX=xα−yαα−ζ​∇x(|x|2​q)|x=xα,pY=xα−yαα+z​e​t​a​∇y(|y|2​q)|y=yα.p\_{X}=\tfrac{x\_{\alpha}-y\_{\alpha}}{\alpha}-\zeta\,\nabla\_{x}\big(|x|^{2q}\big)\big|\_{x=x\_{\alpha}},\quad p\_{Y}=\tfrac{x\_{\alpha}-y\_{\alpha}}{\alpha}+zeta\,\nabla\_{y}\big(|y|^{2q}\big)\big|\_{y=y\_{\alpha}}. |  |

The second-order matrices are coupled in the standard way by Ishii’s lemma. Since the HJBI is first order, only the first-order components enter the inequalities below. The additional ζ\zeta-gradient terms vanish as ζ↓0\zeta\downarrow 0 uniformly on bounded sets.

##### Sub-/super- inequalities.

By the viscosity properties (with constrained semijets),

|  |  |  |
| --- | --- | --- |
|  | −aX+H​(xα,pX)≤0,−aY+H​(yα,pY)≥0.-a\_{X}+H(x\_{\alpha},p\_{X})\leq 0,\quad-a\_{Y}+H(y\_{\alpha},p\_{Y})\geq 0. |  |

Subtracting the second inequality from the first yields

|  |  |  |
| --- | --- | --- |
|  | H​(xα,pX)−H​(yα,pY)≤aX−aY=2​tα−sαγ.H(x\_{\alpha},p\_{X})-H(y\_{\alpha},p\_{Y})\leq a\_{X}-a\_{Y}=2\,\tfrac{t\_{\alpha}-s\_{\alpha}}{\gamma}. |  |

Hence, taking lim sup\limsup as α,γ↓0\alpha,\gamma\downarrow 0 and using continuity of HH together with |tα−sα|→0|t\_{\alpha}-s\_{\alpha}|\to 0, |xα−yα|→0|x\_{\alpha}-y\_{\alpha}|\to 0, and the fact that the ζ\zeta-terms vanish as ζ↓0\zeta\downarrow 0,

|  |  |  |
| --- | --- | --- |
|  | lim supα,γ↓0[H​(xα,pX)−H​(yα,pY)]≤0.\limsup\_{\alpha,\gamma\downarrow 0}\big[H(x\_{\alpha},p\_{X})-H(y\_{\alpha},p\_{Y})\big]\leq 0. |  |

##### Continuity and stability of HH.

By Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(2) and |xα−yα|→0|x\_{\alpha}-y\_{\alpha}|\to 0, |pX−pY|→0|p\_{X}-p\_{Y}|\to 0 (including the ζ\zeta-gradient contributions),

|  |  |  |
| --- | --- | --- |
|  | lim supα,γ↓0[H​(yα,pY)−H​(xα,pX)]≤0.\limsup\_{\alpha,\gamma\downarrow 0}\big[H(y\_{\alpha},p\_{Y})-H(x\_{\alpha},p\_{X})\big]\leq 0. |  |

Taking lim sup in the previous inequality yields zero, and the penalization construction implies supt,x(U​(t,x)−W​(t,x))≤0,\sup\_{t,x}\big(U(t,x)-W(t,x)\big)\leq 0, hence U≤WU\leq W on the whole domain.

##### Terminal time and boundary.

The time penalization and the viscosity attainment of U​(T,⋅)≤g≤W​(T,⋅)U(T,\cdot)\leq g\leq W(T,\cdot) preclude a positive gap at t=Tt=T. At v=0v=0, the constrained-viscosity framework on the closed set ℝ×ℝ+\mathbb{R}\times\mathbb{R}\_{+} (Assumption [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")(4)) applies. No explicit boundary condition is imposed, and test functions are taken from the interior.
∎

### B.3 Proof of [Theorem 3.12](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem12 "Theorem 3.12 (existence of a viscosity solution). ‣ 3.1.4 Existence for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")

###### Proof.

We construct time-discrete approximations VΔV^{\Delta} using a monotone, stable, and consistent semi-Lagrangian scheme with piecewise-constant controls, enforcing viability at v≥0v\geq 0 (no step leaves the domain). Set VΔ​(T,⋅)=gV^{\Delta}(T,\cdot)=g and, for tn=T−n​Δt\_{n}=T-n\Delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VΔ​(tn,x)=inf(u,π)∈𝒰×𝒫sup(θ,ξ)∈Θ×Ξ{Δ​ℓ~​(x,u,π,θ,ξ)+VΔ​(tn+1,x+Δ​b​(x,u,π,θ,ξ))},\displaystyle V^{\Delta}(t\_{n},x)=\inf\_{(u,\pi)\in\mathcal{U}\times\mathcal{P}}\;\sup\_{(\theta,\xi)\in\Theta\times\Xi}\Big\{\Delta\,\tilde{\ell}(x,u,\pi,\theta,\xi)+V^{\Delta}\big(t\_{n+1},\,x+\Delta\,b(x,u,\pi,\theta,\xi)\big)\Big\}, |  | (12) |

with the step restricted to x′=x+Δ​b​(⋅)x^{\prime}=x+\Delta\,b(\cdot) satisfying v′≥0v^{\prime}\geq 0. The KL penalty is absorbed in the running cost ℓ~\tilde{\ell}, which is coercive in (θ,ξ)(\theta,\xi). The scheme is monotone. Stability follows from either boundedness of controls (compact case) or the coercive lower bound in (u,π)(u,\pi) (unbounded case), together with at-most-linear growth of bb, and it is consistent with the HJBI.

By the Barles–Souganidis framework [[3](https://arxiv.org/html/2512.04704v1#bib.bib3)], monotone, stable, and consistent schemes for equations with a comparison principle converge to the unique viscosity solution. Using half-relaxed limits, VΔV^{\Delta} converges locally uniformly to VV. Polynomial growth follows from discrete Gronwall bounds for the Euler step and, in the unbounded case, the coercive quadratic terms in (u,π)(u,\pi).

Finally, if Isaacs’ condition holds (so HH is the common Isaacs Hamiltonian), the robust value function defined via the DPP is a viscosity solution of the same HJBI with the same growth. By comparison, it coincides with VV.
∎

### B.4 Proof of [Theorem 3.13](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem13 "Theorem 3.13 (verification statement). ‣ 3.2.1 Verification theorem for the robust HJBI ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk")

###### Proof.

By the DPP in Proposition [3.3](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem3 "Proposition 3.3 (DPP and terminal condition). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and [Theorem 3.8](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem8 "Theorem 3.8 (comparison principle and uniqueness). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), any viscosity solution with the prescribed growth and terminal condition must coincide with the robust value function. By Berge’s maximum theorem (Berge [[10](https://arxiv.org/html/2512.04704v1#bib.bib10)], Section VI-3), existence of measurable minimizers follows from compact action sets and continuity of the Hamiltonian in the controls. The standard super-/submartingale verification argument (*e.g.,* Pham [[42](https://arxiv.org/html/2512.04704v1#bib.bib42)], Section 3.5) applied to t↦Φ​(t,Xt)t\mapsto\Phi(t,X\_{t}) along admissible trajectories yields optimality of the minimizing feedback controls. The state-constraint boundary at v=0v=0 is handled in the viscosity sense as in [section 3.1.3](https://arxiv.org/html/2512.04704v1#S3.SS1.SSS3 "3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").
∎

## Appendix C Sensitivity analysis and comparative statics

In this appendix, we consider the Riccati sensitivity ODE and Lipschitz comparative statics for the value function. We also derive bounds on value function losses under drift misspecification.

### C.1 Setup and Riccati sensitivity ODE

Let a​(t)a(t) collect the six coefficients of the quadratic value function from [Eq. 7](https://arxiv.org/html/2512.04704v1#S3.E7 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), evolving under the interior Riccati map FF in the Riccati ODE system [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") with terminal vector aTa\_{T} in [Eq. 8](https://arxiv.org/html/2512.04704v1#S3.E8 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"). Denote parameters by the vector Θ\Theta. We restrict our analysis to a compact parameter set 𝒦\mathcal{K}.

We invoke the following local differentiability regularity and interior no-switching assumptions.

###### Assumption C.1 (local differentiability regularity and interior no-switching).

We assume:

1. 1.

   The primitives (b,ℓ,g)(b,\ell,g) and model coefficients (*e.g.*, η,κ,Ru,R,λm,λv,β,Σ2\eta,\kappa,R\_{u},R,\lambda\_{m},\lambda\_{v},\beta,\Sigma^{2}) are C1C^{1} in Θ\Theta on compact subsets of the parameter space, with locally bounded partial derivatives. The terminal map aT​(Θ)a\_{T}(\Theta) is C1C^{1} in Θ\Theta. On interior regions, the right-hand side FF in the Riccati ODE system [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") is C1C^{1} in (a,Θ)(a,\Theta) and locally Lipschitz in aa, uniformly on compacts.
2. 2.

   On the time interval under consideration, the projections in [Eq. 9](https://arxiv.org/html/2512.04704v1#S3.E9 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") are inactive. There exist δ>0\delta>0 and ε>0\varepsilon>0 such that, for the baseline parameter Θ\Theta and any Θ′\Theta^{\prime} with ‖Θ′−Θ‖≤ε\|\Theta^{\prime}-\Theta\|\leq\varepsilon (where Θ′∈𝒦\Theta^{\prime}\in\mathcal{K}), the selector arguments on [t,T][t,T] remain at least δ\delta away from the projection boundaries, uniformly along the closed-loop trajectories considered.

By the interior no-switching assumption (Assumption [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk")(2)), we remain in the interior (unconstrained) regime of the control selectors. The unconstrained optimizer stays strictly within the admissible sets. Therefore, the projections in [Eq. 9](https://arxiv.org/html/2512.04704v1#S3.E9 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") are inactive, and no threshold is crossed that would change the selector’s formula. Consequently, the selector law is smooth and time-continuous on the interval, with no regime switches or discontinuous shifts in the control law.

Fix a baseline Θ\Theta and a perturbation Θ′=Θ+δ​Θ\Theta^{\prime}=\Theta+\delta\Theta. Under Assumptions [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk") and away from selector switching surfaces, the Riccati flow is differentiable in Θ\Theta.

###### Lemma C.2 (Riccati sensitivity ODE).

Let Da​FD\_{a}F and DΘ​FD\_{\Theta}F denote the Jacobians of the interior Riccati map FF evaluated along the baseline trajectory t↦a​(t;Θ)t\mapsto a(t;\Theta). Then the directional derivative Δ​a​(t):=∂Θa​(t;Θ)​[δ​Θ]\Delta a(t):=\partial\_{\Theta}a(t;\Theta)[\delta\Theta] satisfies

|  |  |  |
| --- | --- | --- |
|  | dd​t​Δ​a​(t)=Da​F​(t,a​(t;Θ),Θ)​Δ​a​(t)+DΘ​F​(t,a​(t;Θ),Θ)​[δ​Θ],Δ​a​(T)=∂ΘaT​(Θ)​[δ​Θ],\frac{d}{dt}\Delta a(t)=D\_{a}F\big(t,a(t;\Theta),\Theta\big)\,\Delta a(t)+D\_{\Theta}F\big(t,a(t;\Theta),\Theta\big)[\delta\Theta],\quad\Delta a(T)=\partial\_{\Theta}a\_{T}(\Theta)[\delta\Theta], |  |

with variation-of-constants representation

|  |  |  |
| --- | --- | --- |
|  | Δ​a​(t)=Φ​(t,T)​Δ​a​(T)+∫tTΦ​(t,s)​DΘ​F​(s,a​(s;Θ),Θ)​[δ​Θ]​𝑑s,\Delta a(t)=\Phi(t,T)\,\Delta a(T)+\int\_{t}^{T}\Phi(t,s)\,D\_{\Theta}F\big(s,a(s;\Theta),\Theta\big)[\delta\Theta]\;ds, |  |

where Φ​(t,s)\Phi(t,s) is the principal solution of Φ˙​(t,s)=Da​F​(t,a​(t;Θ),Θ)​Φ​(t,s)\dot{\Phi}(t,s)=D\_{a}F\big(t,a(t;\Theta),\Theta\big)\,\Phi(t,s) with Φ​(s,s)=I\Phi(s,s)=I. If aTa\_{T} is Θ\Theta-independent (*e.g.*, fixed GmG\_{m} in a11​(T)=Gma\_{11}(T)=G\_{m}), then ∂ΘaT​(Θ)​[δ​Θ]=0\partial\_{\Theta}a\_{T}(\Theta)[\delta\Theta]=0.

###### Proof.

On any interval where Assumption [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk") holds, a​(⋅;Θ)a(\cdot;\Theta) solves the terminal-value ODE a˙​(t)=F​(t,a​(t;Θ),Θ)\dot{a}(t)=F\big(t,a(t;\Theta),\Theta\big) with a​(T)=aT​(Θ)a(T)=a\_{T}(\Theta), where FF is C1C^{1} in (a,Θ)(a,\Theta) and locally Lipschitz in aa. By C1C^{1}-dependence of ODE solutions on parameters (*e.g.*, Hartman [[32](https://arxiv.org/html/2512.04704v1#bib.bib32)], Chapter V), Θ↦a​(⋅;Θ)\Theta\mapsto a(\cdot;\Theta) is C1C^{1} on such intervals. Differentiating yields the stated linear variational equation and the variation-of-constants formula, with Φ\Phi the principal solution. If aTa\_{T} does not depend on Θ\Theta, then Δ​a​(T)=0\Delta a(T)=0. The conclusions hold piecewise between selector switching times. Across switches, use one-sided or generalized derivatives.
∎

###### Remark C.3 (computational aspects).

The sensitivity ODE in Lemma [C.2](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem2 "Lemma C.2 (Riccati sensitivity ODE). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk") can be solved numerically alongside the baseline Riccati system, providing gradient information for optimization or robustness analysis without requiring finite differences.

For x=(m,v)x=(m,v), Δ​V​(t,x)=∑i∂aiV​(t,x)​Δ​ai​(t)\Delta V(t,x)=\sum\_{i}\partial\_{a\_{i}}V(t,x)\,\Delta a\_{i}(t). In the interior, Δ​ϕ\Delta\phi follows by differentiating the selectors in [Eq. 9](https://arxiv.org/html/2512.04704v1#S3.E9 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") along a​(⋅;Θ)a(\cdot;\Theta); with active projections, use piecewise derivatives away from switching times and one-sided derivatives at switch times.

### C.2 Lipschitz comparative statics for the value function

###### Theorem C.4 (comparative statics: Lipschitz continuity of value).

Assume Assumptions [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk") and [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk") on an interval where selectors are inactive. Let 𝒦\mathcal{K} be a compact set of parameters. Suppose there exists a compact set 𝒜⊂ℝ6\mathcal{A}\subset\mathbb{R}^{6} such that, for every Θ∈𝒦\Theta\in\mathcal{K}, the Riccati trajectory t↦a​(t;Θ)t\mapsto a(t;\Theta) remains in 𝒜\mathcal{A} for all t∈[0,T]t\in[0,T]. Assume further that on [0,T]×𝒜×𝒦[0,T]\times\mathcal{A}\times\mathcal{K} the maps Da​FD\_{a}F and DΘ​FD\_{\Theta}F are bounded, and that aTa\_{T} is C1C^{1} with supΘ∈𝒦‖∂ΘaT​(Θ)‖<∞\sup\_{\Theta\in\mathcal{K}}\|\partial\_{\Theta}a\_{T}(\Theta)\|<\infty. Then, for any xx and t∈[0,T]t\in[0,T], there exists CT,𝒦>0C\_{T,\mathcal{K}}>0 such that for all Θ,Θ′∈𝒦\Theta,\Theta^{\prime}\in\mathcal{K},

|  |  |  |
| --- | --- | --- |
|  | |V​(t,x;Θ′)−V​(t,x;Θ)|≤CT,𝒦​(1+|x|2)​‖Θ′−Θ‖.|V(t,x;\Theta^{\prime})-V(t,x;\Theta)|\leq C\_{T,\mathcal{K}}\,(1+|x|^{2})\,\|\Theta^{\prime}-\Theta\|. |  |

If aTa\_{T} is Θ\Theta-independent, CT,𝒦C\_{T,\mathcal{K}} can be chosen without the terminal sensitivity term.

###### Proof.

Consider the line Θs=Θ+s​(Θ′−Θ)\Theta\_{s}=\Theta+s(\Theta^{\prime}-\Theta), s∈[0,1]s\in[0,1], and set δ​Θ=Θ′−Θ\delta\Theta=\Theta^{\prime}-\Theta. By Lemma [C.2](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem2 "Lemma C.2 (Riccati sensitivity ODE). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk"), for each ss the directional derivative Δ​as​(t):=∂Θa​(t;Θs)​[δ​Θ]\Delta a\_{s}(t):=\partial\_{\Theta}a(t;\Theta\_{s})[\delta\Theta] solves

|  |  |  |
| --- | --- | --- |
|  | dd​t​Δ​as​(t)=As​(t)​Δ​as​(t)+bs​(t),Δ​as​(T)=∂ΘaT​(Θs)​[δ​Θ],\frac{d}{dt}\Delta a\_{s}(t)=A\_{s}(t)\Delta a\_{s}(t)+b\_{s}(t),\quad\Delta a\_{s}(T)=\partial\_{\Theta}a\_{T}(\Theta\_{s})[\delta\Theta], |  |

with As​(t)=Da​F​(t,a​(t;Θs),Θs)A\_{s}(t)=D\_{a}F(t,a(t;\Theta\_{s}),\Theta\_{s}) and bs​(t)=DΘ​F​(t,a​(t;Θs),Θs)​[δ​Θ]b\_{s}(t)=D\_{\Theta}F(t,a(t;\Theta\_{s}),\Theta\_{s})[\delta\Theta]. By the boundedness assumptions on [0,T]×𝒜×𝒦[0,T]\times\mathcal{A}\times\mathcal{K}, Gronwall’s inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Δ​as​(t)‖\displaystyle\|\Delta a\_{s}(t)\| | ≤(‖∂ΘaT​(Θs)‖+∫tT‖DΘ​F​(r,⋅,⋅)‖​𝑑r)\displaystyle\leq\Big(\|\partial\_{\Theta}a\_{T}(\Theta\_{s})\|+\int\_{t}^{T}\|D\_{\Theta}F(r,\cdot,\cdot)\|\,dr\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp(∫tT∥DaF(r,⋅,⋅)∥dr)∥δΘ∥≤CT∥δΘ∥,\displaystyle\phantom{\leq}\times\exp\!\Big(\int\_{t}^{T}\|D\_{a}F(r,\cdot,\cdot)\|\,dr\Big)\,\|\delta\Theta\|\leq C\_{T}\,\|\delta\Theta\|, |  |

with CTC\_{T} uniform in s∈[0,1]s\in[0,1] and Θ∈𝒦\Theta\in\mathcal{K}. Since V​(t,x;Θ)V(t,x;\Theta) is quadratic in xx with coefficients a​(t;Θ)a(t;\Theta), its ss-derivative satisfies

|  |  |  |
| --- | --- | --- |
|  | |dd​s​V​(t,x;Θs)|≤C​(1+|x|2)​‖Δ​as​(t)‖≤C′​(1+|x|2)​‖δ​Θ‖.\Big|\frac{d}{ds}V(t,x;\Theta\_{s})\Big|\leq C(1+|x|^{2})\,\|\Delta a\_{s}(t)\|\leq C^{\prime}(1+|x|^{2})\,\|\delta\Theta\|. |  |

Integrating in s∈[0,1]s\in[0,1] yields the stated Lipschitz bound with CT,𝒦=C′C\_{T,\mathcal{K}}=C^{\prime}. If aTa\_{T} is independent of Θ\Theta, the term involving ‖∂ΘaT‖\|\partial\_{\Theta}a\_{T}\| drops from CTC\_{T}.
∎

### C.3 Robustness loss bounds under drift misspecification

Let Θ=(Θd,Θo)\Theta=(\Theta\_{d},\Theta\_{o}), where Θd\Theta\_{d} collects drift parameters that may be misspecified. Suppose the implemented controller is designed for Θ\Theta but the true model is Θ′=(Θd+δd,Θo)\Theta^{\prime}=(\Theta\_{d}+\delta\_{d},\Theta\_{o}) with ‖δd‖≤ε\left\lVert{\delta\_{d}}\right\rVert\leq\varepsilon.

###### Assumption C.5 (stability under misspecification).

Under the misspecified parameters Θ′=(Θd+δd,Θo)\Theta^{\prime}=(\Theta\_{d}+\delta\_{d},\Theta\_{o}) with ‖δd‖≤ε\|\delta\_{d}\|\leq\varepsilon, the closed-loop system remains stable and the state trajectory (mt,vt)(m\_{t},v\_{t}) remains in the domain ℝ×[0,vmax]\mathbb{R}\times[0,v\_{\max}] for some vmax<∞v\_{\max}<\infty.

###### Theorem C.6 (performance gap bound).

Let J​(t,x;ϕ;Θ′)J(t,x;\phi;\Theta^{\prime}) denote the realized cost when applying the feedback ϕ​(⋅;Θ)\phi(\cdot;\Theta) in the true model Θ′\Theta^{\prime}. Assume Assumptions [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), [3.11](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem11 "Assumption 3.11 (coercive running cost). ‣ 3.1.4 Existence for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), and [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk") hold on a compact parameter set 𝒦\mathcal{K} containing both Θ\Theta and Θ′\Theta^{\prime}, selectors are inactive on [t,T][t,T], the Hamiltonian is uniformly strongly convex in controls (and concave in adversarial terms, if present) with modulus μ>0\mu>0, and the model coefficients are uniformly Lipschitz in Θ\Theta on [t,T]×𝒜×𝒦[t,T]\times\mathcal{A}\times\mathcal{K}.

Then, there exists CT,𝒦>0C\_{T,\mathcal{K}}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 0≤J​(t,x;ϕ​(⋅;Θ);Θ′)−V​(t,x;Θ′)≤CT,𝒦​(1+|x|2)​ε2.0\leq J\big(t,x;\phi(\cdot;\Theta);\Theta^{\prime}\big)-V(t,x;\Theta^{\prime})\leq C\_{T,\mathcal{K}}\,(1+\lvert x\rvert^{2})\,\varepsilon^{2}. |  |

In particular, the first-order loss vanishes, and the robustness loss is quadratic in the magnitude of drift misspecification.

###### Proof.

Plug V​(⋅;Θ)V(\cdot;\Theta) into the true HJB/HJBI at Θ′\Theta^{\prime}. Since VV solves −∂tV+HΘ​(x,∇V)=0-\partial\_{t}V+H\_{\Theta}(x,\nabla V)=0 and the Hamiltonian is Lipschitz in parameters on [t,T]×𝒜×𝒦[t,T]\times\mathcal{A}\times\mathcal{K}, the pointwise residual

|  |  |  |
| --- | --- | --- |
|  | r​(t,x):=−∂tV​(t,x;Θ)+HΘ′​(x,∇V​(t,x;Θ))=HΘ′​(x,∇V​(t,x;Θ))−HΘ​(x,∇V​(t,x;Θ))r(t,x):=-\partial\_{t}V(t,x;\Theta)+H\_{\Theta^{\prime}}\big(x,\nabla V(t,x;\Theta)\big)=H\_{\Theta^{\prime}}\big(x,\nabla V(t,x;\Theta)\big)-H\_{\Theta}\big(x,\nabla V(t,x;\Theta)\big) |  |

is uniformly 𝒪​(ε)\mathcal{O}(\varepsilon) on [t,T]×𝒜[t,T]\times\mathcal{A}. Moreover, under the interior no-switching assumption (Assumption [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk")(2)), selectors are smooth, so the Lipschitz bound carries through the feedback map without kinks. Uniform strong convexity (in controls) and concavity (in adversarial terms, if present) with modulus μ>0\mu>0 imply the standard Hamiltonian error-to-policy suboptimality inequality. When a smooth WW is used to construct the feedback by minimizing the Θ′\Theta^{\prime}-Hamiltonian, the running suboptimality is controlled by the square of the Hamiltonian residual divided by μ\mu (this follows by completing the square around the Θ′\Theta^{\prime}-optimal control). Applying this with W=V​(⋅;Θ)W=V(\cdot;\Theta) yields a per-time integrand bounded by C​r​(t,Xt)2/μC\,r(t,X\_{t})^{2}/\mu. Since r=𝒪​(ε)r=\mathcal{O}(\varepsilon) uniformly, we obtain an 𝒪​(ε2)\mathcal{O}(\varepsilon^{2}) bound on the instantaneous gap.

To pass from integrands to total cost, evaluate along the closed-loop state XX driven by the implemented feedback ϕ​(⋅;Θ)\phi(\cdot;\Theta) under the true model Θ′\Theta^{\prime}. Under the standing linear-growth/Lipschitz assumptions (Assumptions [3.1](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem1 "Assumption 3.1 (standing assumptions). ‣ 3.1.1 Model primitives and admissible inputs ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), [3.7](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem7 "Assumption 3.7 (structural and growth conditions). ‣ 3.1.3 Comparison principle for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), [3.11](https://arxiv.org/html/2512.04704v1#S3.Thmtheorem11 "Assumption 3.11 (coercive running cost). ‣ 3.1.4 Existence for the robust HJBI ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), and [C.1](https://arxiv.org/html/2512.04704v1#A3.Thmtheorem1 "Assumption C.1 (local differentiability regularity and interior no-switching). ‣ C.1 Setup and Riccati sensitivity ODE ‣ Appendix C Sensitivity analysis and comparative statics ‣ Coordinated Mean-Field Control for Systemic Risk")), second moments of XX are bounded on [t,T][t,T] by Gronwall’s inequality, yielding 𝔼​[1+|Xt|2]≤C​(1+|x|2)\mathbb{E}[1+\lvert X\_{t}\rvert^{2}]\leq C\,(1+\lvert x\rvert^{2}). Combining the strong-convexity estimate with r=𝒪​(ε)r=\mathcal{O}(\varepsilon), integrating over [t,T][t,T], and using the moment bound yields 0≤J​(t,x;ϕ​(⋅;Θ);Θ′)−V​(t,x;Θ′)≤CT,𝒦​(1+|x|2)​ε2,0\leq J\big(t,x;\phi(\cdot;\Theta);\Theta^{\prime}\big)-V(t,x;\Theta^{\prime})\leq C\_{T,\mathcal{K}}\,(1+\lvert x\rvert^{2})\,\varepsilon^{2}, for a constant CT,𝒦C\_{T,\mathcal{K}} depending on μ\mu, Lipschitz and growth constants, and TT. Intuitively, the first-order term cancels by the envelope principle under interiority (no switching), so the leading error is quadratic in the drift misspecification. In the LQ case, the same ε2\varepsilon^{2} rate follows directly by completing the square in the closed-loop cost and bounding the perturbation terms.
∎

###### Remark C.7 (differentiability and higher-order terms).

If FF is C2C^{2} and trajectories remain in a compact set, one can expand a​(t;Θ′)a(t;\Theta^{\prime}) to second order and refine constants. In time-homogeneous LQ, explicit Riccati solutions yield closed-form sensitivity matrices and sharper constants.

## Appendix D Derivation of the Riccati ODE system

This appendix provides the full derivation for the Riccati ODE system [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").

##### The optimized Hamiltonian.

The derivation begins with the HJBI equation −∂tV+H​(x,∇V)=0.-\partial\_{t}V+H(x,\nabla V)=0. As shown in [section 3.1.2](https://arxiv.org/html/2512.04704v1#S3.SS1.SSS2 "3.1.2 HJBI and viscosity characterization ‣ 3.1 Viscosity solutions and the HJBI equation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), we can solve the inf\inf-sup\sup problem for the controls and distortions analytically. The Isaacs Hamiltonian H​(x,p)H(x,p) where x=(m,v)x=(m,v) and p=(pm,pv)=(∂mV,∂vV)p=(p\_{m},p\_{v})=(\partial\_{m}V,\partial\_{v}V) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H(x,p)=infu,πsupθ,ξ{\displaystyle H(x,p)=\inf\_{u,\pi}\sup\_{\theta,\xi}\Big\{ | pm​(η​u+θ)+pv​(−2​β​v+Σ2+ξ−χ​π)\displaystyle p\_{m}(\eta u+\theta)+p\_{v}\big(-2\beta v+\Sigma^{2}+\xi-\chi\pi\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +w1m2+(w¯2+κu)v+Rπ2+Ruu2−θ24​λm−ξ24​λv}.\displaystyle+w\_{1}m^{2}+(\bar{w}\_{2}+\kappa u)v+R\pi^{2}+R\_{u}u^{2}-\tfrac{\theta^{2}}{4\lambda\_{m}}-\tfrac{\xi^{2}}{4\lambda\_{v}}\Big\}. |  |

Solving the unconstrained optimization problems (by completing the square or first-order conditions) yields the optimized Hamiltonian H∗H^{\*}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H∗​(x,p)=\displaystyle H^{\*}(x,p)= | λm​pm2+λv​pv2+w1​m2+w¯2​v+pv​(−2​β​v+Σ2)−(η​pm+κ​v)24​Ru−χ2​pv24​R.\displaystyle\lambda\_{m}p\_{m}^{2}+\lambda\_{v}p\_{v}^{2}+w\_{1}m^{2}+\bar{w}\_{2}v+p\_{v}(-2\beta v+\Sigma^{2})-\frac{(\eta p\_{m}+\kappa v)^{2}}{4R\_{u}}-\frac{\chi^{2}p\_{v}^{2}}{4R}. |  |

##### The ansatz and gradients.

We use the quadratic ansatz from [Eq. 7](https://arxiv.org/html/2512.04704v1#S3.E7 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"): V​(t,m,v)=a0+a1​m+a2​v+a11​m2+a12​m​v+a22​v2,V(t,m,v)=a\_{0}+a\_{1}m+a\_{2}v+a\_{11}m^{2}+a\_{12}mv+a\_{22}v^{2}, where ai=ai​(t)a\_{i}=a\_{i}(t). The required derivatives are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tV\displaystyle\partial\_{t}V | =a˙0+a˙1​m+a˙2​v+a˙11​m2+a˙12​m​v+a˙22​v2,\displaystyle=\dot{a}\_{0}+\dot{a}\_{1}m+\dot{a}\_{2}v+\dot{a}\_{11}m^{2}+\dot{a}\_{12}mv+\dot{a}\_{22}v^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pm=∂mV\displaystyle p\_{m}=\partial\_{m}V | =a1+2​a11​m+a12​v,\displaystyle=a\_{1}+2a\_{11}m+a\_{12}v, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pv=∂vV\displaystyle p\_{v}=\partial\_{v}V | =a2+a12​m+2​a22​v.\displaystyle=a\_{2}+a\_{12}m+2a\_{22}v. |  |

##### Matching coefficients.

We substitute the ansatz and its gradients into the HJBI equation −∂tV+H∗​(x,∇V)=0-\partial\_{t}V+H^{\*}(x,\nabla V)=0. This creates a large polynomial in mm and vv. For the equation to hold for all (m,v)(m,v), the coefficients of each monomial (m2,v2,m​v,m,v,1m^{2},v^{2},mv,m,v,1) must be equal. We equate the coefficients from −∂tV-\partial\_{t}V (*e.g.,* −a˙11-\dot{a}\_{11}) with the corresponding coefficients from H∗H^{\*}. This is equivalent to setting a˙i\dot{a}\_{i} equal to the collected coefficients from H∗H^{\*}.

##### Coefficient of constant terms (yields a˙0\dot{a}\_{0}).

For the terms from H∗H^{\*} containing constants, we have: pv​(Σ2)⟹(a2)​Σ2=Σ2​a2p\_{v}(\Sigma^{2})\implies(a\_{2})\Sigma^{2}=\Sigma^{2}a\_{2},  λm​pm2⟹λm​(a1)2⟹λm​a12\lambda\_{m}p\_{m}^{2}\implies\lambda\_{m}(a\_{1})^{2}\implies\lambda\_{m}a\_{1}^{2} λv​pv2⟹λv​(a2)2⟹λv​a22\lambda\_{v}p\_{v}^{2}\implies\lambda\_{v}(a\_{2})^{2}\implies\lambda\_{v}a\_{2}^{2},  −(η​pm)24​Ru⟹−14​Ru​(η​a1)2=−η24​Ru​a12-\tfrac{(\eta p\_{m})^{2}}{4R\_{u}}\implies-\tfrac{1}{4R\_{u}}(\eta a\_{1})^{2}=-\tfrac{\eta^{2}}{4R\_{u}}a\_{1}^{2}, and −χ2​pv24​R⟹−χ24​R​(a2)2=−χ24​R​a22-\tfrac{\chi^{2}p\_{v}^{2}}{4R}\implies-\tfrac{\chi^{2}}{4R}(a\_{2})^{2}=-\tfrac{\chi^{2}}{4R}a\_{2}^{2}.

Therefore, a˙0=Σ2​a2+(λm−η24​Ru)​a12+(λv−χ24​R)​a22\dot{a}\_{0}=\Sigma^{2}a\_{2}+\Big(\lambda\_{m}-\tfrac{\eta^{2}}{4R\_{u}}\Big)a\_{1}^{2}+\Big(\lambda\_{v}-\tfrac{\chi^{2}}{4R}\Big)a\_{2}^{2}.

##### Coefficient of mm (yields a˙1\dot{a}\_{1}).

For the terms from H∗H^{\*} containing mm, we have: pv​(Σ2)⟹(a12​m)​Σ2⟹Σ2​a12p\_{v}(\Sigma^{2})\implies(a\_{12}m)\Sigma^{2}\implies\Sigma^{2}a\_{12},  λm​pm2⟹λm⋅2⋅(a1)​(2​a11​m)⟹4​λm​a1​a11\lambda\_{m}p\_{m}^{2}\implies\lambda\_{m}\cdot 2\cdot(a\_{1})(2a\_{11}m)\implies 4\lambda\_{m}a\_{1}a\_{11},  λv​pv2⟹λv⋅2⋅(a2)​(a12​m)⟹2​λv​a2​a12\lambda\_{v}p\_{v}^{2}\implies\lambda\_{v}\cdot 2\cdot(a\_{2})(a\_{12}m)\implies 2\lambda\_{v}a\_{2}a\_{12},  −(η​pm)24​Ru⟹−14​Ru⋅2⋅(η​a1)​(η​2​a11​m)⟹−η2Ru​a1​a11-\tfrac{(\eta p\_{m})^{2}}{4R\_{u}}\implies-\tfrac{1}{4R\_{u}}\cdot 2\cdot(\eta a\_{1})(\eta 2a\_{11}m)\implies-\tfrac{\eta^{2}}{R\_{u}}a\_{1}a\_{11}, and −χ2​pv24​R⟹−χ24​R⋅2⋅(a2)​(a12​m)⟹−χ22​R​a2​a12-\tfrac{\chi^{2}p\_{v}^{2}}{4R}\implies-\tfrac{\chi^{2}}{4R}\cdot 2\cdot(a\_{2})(a\_{12}m)\implies-\tfrac{\chi^{2}}{2R}a\_{2}a\_{12}.

Therefore, a˙1=Σ2​a12+(4​λm−η2Ru)​a1​a11+(2​λv−χ22​R)​a2​a12\dot{a}\_{1}=\Sigma^{2}a\_{12}+\Big(4\lambda\_{m}-\tfrac{\eta^{2}}{R\_{u}}\Big)a\_{1}a\_{11}+\Big(2\lambda\_{v}-\tfrac{\chi^{2}}{2R}\Big)a\_{2}a\_{12}.

##### Coefficient of vv (yields a˙2\dot{a}\_{2}).

For the terms from H∗H^{\*} containing vv, we have: w¯2​v⟹w¯2\bar{w}\_{2}v\implies\bar{w}\_{2},  pv​(−2​β​v)⟹(a2)​(−2​β​v)⟹−2​β​a2p\_{v}(-2\beta v)\implies(a\_{2})(-2\beta v)\implies-2\beta a\_{2},  pv​(Σ2)⟹(2​a22​v)​Σ2⟹2​Σ2​a22p\_{v}(\Sigma^{2})\implies(2a\_{22}v)\Sigma^{2}\implies 2\Sigma^{2}a\_{22},  λm​pm2⟹λm⋅2⋅(a1)​(a12​v)⟹2​λm​a1​a12\lambda\_{m}p\_{m}^{2}\implies\lambda\_{m}\cdot 2\cdot(a\_{1})(a\_{12}v)\implies 2\lambda\_{m}a\_{1}a\_{12},  λv​pv2⟹λv⋅2⋅(a2)​(2​a22​v)⟹4​λv​a2​a22\lambda\_{v}p\_{v}^{2}\implies\lambda\_{v}\cdot 2\cdot(a\_{2})(2a\_{22}v)\implies 4\lambda\_{v}a\_{2}a\_{22},  −(η​pm+κ​v)24​Ru⟹−14​Ru​[2​(η​a1)​(η​a12​v+κ​v)]⟹−η22​Ru​a1​a12−η​κ2​Ru​a1-\tfrac{(\eta p\_{m}+\kappa v)^{2}}{4R\_{u}}\implies-\tfrac{1}{4R\_{u}}[2(\eta a\_{1})(\eta a\_{12}v+\kappa v)]\implies-\tfrac{\eta^{2}}{2R\_{u}}a\_{1}a\_{12}-\tfrac{\eta\kappa}{2R\_{u}}a\_{1}, and −χ2​pv24​R⟹−χ24​R⋅2⋅(a2)​(2​a22​v)⟹−χ2R​a2​a22-\tfrac{\chi^{2}p\_{v}^{2}}{4R}\implies-\tfrac{\chi^{2}}{4R}\cdot 2\cdot(a\_{2})(2a\_{22}v)\implies-\tfrac{\chi^{2}}{R}a\_{2}a\_{22}.

Therefore, a˙2=w¯2−2​β​a2+2​Σ2​a22+(2​λm−η22​Ru)​a1​a12+(4​λv−χ2R)​a2​a22−η​κ2​Ru​a1\dot{a}\_{2}=\bar{w}\_{2}-2\beta a\_{2}+2\Sigma^{2}a\_{22}+\Big(2\lambda\_{m}-\tfrac{\eta^{2}}{2R\_{u}}\Big)a\_{1}a\_{12}+\Big(4\lambda\_{v}-\tfrac{\chi^{2}}{R}\Big)a\_{2}a\_{22}-\tfrac{\eta\kappa}{2R\_{u}}a\_{1}.

##### Coefficient of m2m^{2} (yields a˙11\dot{a}\_{11}).

For the terms from H∗H^{\*} containing m2m^{2}, we have: w1​m2⟹w1w\_{1}m^{2}\implies w\_{1},  λm​pm2⟹λm​(2​a11​m)2⟹4​λm​a112\lambda\_{m}p\_{m}^{2}\implies\lambda\_{m}(2a\_{11}m)^{2}\implies 4\lambda\_{m}a\_{11}^{2},  λv​pv2⟹λv​(a12​m)2⟹λv​a122\lambda\_{v}p\_{v}^{2}\implies\lambda\_{v}(a\_{12}m)^{2}\implies\lambda\_{v}a\_{12}^{2},  −(η​pm)24​Ru⟹−14​Ru​(η​(2​a11​m))2⟹−η2Ru​a112-\tfrac{(\eta p\_{m})^{2}}{4R\_{u}}\implies-\tfrac{1}{4R\_{u}}(\eta(2a\_{11}m))^{2}\implies-\tfrac{\eta^{2}}{R\_{u}}a\_{11}^{2}, and −χ2​pv24​R⟹−χ24​R​(a12​m)2⟹−χ24​R​a122-\tfrac{\chi^{2}p\_{v}^{2}}{4R}\implies-\tfrac{\chi^{2}}{4R}(a\_{12}m)^{2}\implies-\tfrac{\chi^{2}}{4R}a\_{12}^{2}.

Therefore, a˙11=w1+(4​λm−η2Ru)​a112+(λv−χ24​R)​a122\dot{a}\_{11}=w\_{1}+\Big(4\lambda\_{m}-\tfrac{\eta^{2}}{R\_{u}}\Big)a\_{11}^{2}+\Big(\lambda\_{v}-\tfrac{\chi^{2}}{4R}\Big)a\_{12}^{2}.

##### Coefficient of m​vmv (yields a˙12\dot{a}\_{12}).

For the terms from H∗H^{\*} containing m​vmv, we have: pv​(−2​β​v)⟹(a12​m)​(−2​β​v)⟹−2​β​a12p\_{v}(-2\beta v)\implies(a\_{12}m)(-2\beta v)\implies-2\beta a\_{12},  λm​pm2⟹λm⋅2⋅(2​a11​m)​(a12​v)⟹4​λm​a11​a12\lambda\_{m}p\_{m}^{2}\implies\lambda\_{m}\cdot 2\cdot(2a\_{11}m)(a\_{12}v)\implies 4\lambda\_{m}a\_{11}a\_{12},  λv​pv2⟹λv⋅2⋅(a12​m)​(2​a22​v)⟹4​λv​a12​a22\lambda\_{v}p\_{v}^{2}\implies\lambda\_{v}\cdot 2\cdot(a\_{12}m)(2a\_{22}v)\implies 4\lambda\_{v}a\_{12}a\_{22},  −(η​pm+κ​v)24​Ru⟹−14​Ru⋅2⋅(η​2​a11​m)​(η​a12​v+κ​v)⟹−η2Ru​a11​a12−η​κRu​a11-\tfrac{(\eta p\_{m}+\kappa v)^{2}}{4R\_{u}}\implies-\tfrac{1}{4R\_{u}}\cdot 2\cdot(\eta 2a\_{11}m)(\eta a\_{12}v+\kappa v)\implies-\tfrac{\eta^{2}}{R\_{u}}a\_{11}a\_{12}-\tfrac{\eta\kappa}{R\_{u}}a\_{11}, and −χ2​pv24​R⟹−χ24​R⋅2⋅(a12​m)​(2​a22​v)⟹−χ2R​a12​a22-\tfrac{\chi^{2}p\_{v}^{2}}{4R}\implies-\tfrac{\chi^{2}}{4R}\cdot 2\cdot(a\_{12}m)(2a\_{22}v)\implies-\tfrac{\chi^{2}}{R}a\_{12}a\_{22}.

Therefore, a˙12=−2​β​a12−η​κRu​a11+(4​λm−η2Ru)​a11​a12+(4​λv−χ2R)​a12​a22\dot{a}\_{12}=-2\beta a\_{12}-\tfrac{\eta\kappa}{R\_{u}}a\_{11}+\Big(4\lambda\_{m}-\tfrac{\eta^{2}}{R\_{u}}\Big)a\_{11}a\_{12}+\Big(4\lambda\_{v}-\tfrac{\chi^{2}}{R}\Big)a\_{12}a\_{22}.

##### Coefficient of v2v^{2} (yields a˙22\dot{a}\_{22}).

For the terms from H∗H^{\*} containing v2v^{2}, we have: pv​(−2​β​v)⟹(2​a22​v)​(−2​β​v)⟹−4​β​a22p\_{v}(-2\beta v)\implies(2a\_{22}v)(-2\beta v)\implies-4\beta a\_{22},  λm​pm2⟹λm​(a12​v)2⟹λm​a122\lambda\_{m}p\_{m}^{2}\implies\lambda\_{m}(a\_{12}v)^{2}\implies\lambda\_{m}a\_{12}^{2},  λv​pv2⟹λv​(2​a22​v)2⟹4​λv​a222\lambda\_{v}p\_{v}^{2}\implies\lambda\_{v}(2a\_{22}v)^{2}\implies 4\lambda\_{v}a\_{22}^{2},  −(η​pm+κ​v)24​Ru⟹−14​Ru​(η​a12​v+κ​v)2⟹−14​Ru​(η2​a122+2​η​κ​a12+κ2)-\tfrac{(\eta p\_{m}+\kappa v)^{2}}{4R\_{u}}\implies-\tfrac{1}{4R\_{u}}(\eta a\_{12}v+\kappa v)^{2}\implies-\tfrac{1}{4R\_{u}}(\eta^{2}a\_{12}^{2}+2\eta\kappa a\_{12}+\kappa^{2}), and −χ2​pv24​R⟹−χ24​R​(2​a22​v)2⟹−χ2R​a222-\tfrac{\chi^{2}p\_{v}^{2}}{4R}\implies-\tfrac{\chi^{2}}{4R}(2a\_{22}v)^{2}\implies-\tfrac{\chi^{2}}{R}a\_{22}^{2}.

Therefore, a˙22=−4​β​a22−κ24​Ru−η​κ2​Ru​a12+(λm−η24​Ru)​a122+(4​λv−χ2R)​a222\dot{a}\_{22}=-4\beta a\_{22}-\tfrac{\kappa^{2}}{4R\_{u}}-\tfrac{\eta\kappa}{2R\_{u}}a\_{12}+\Big(\lambda\_{m}-\tfrac{\eta^{2}}{4R\_{u}}\Big)a\_{12}^{2}+\Big(4\lambda\_{v}-\tfrac{\chi^{2}}{R}\Big)a\_{22}^{2}.

##### The final system.

Collecting the six results above yields the complete Riccati ODE system in [Eq. 10](https://arxiv.org/html/2512.04704v1#S3.E10 "In Riccati ODE system for the quadratic ansatz. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk"), which is solved backward from the terminal conditions ai​(T)a\_{i}(T) given in [Eq. 8](https://arxiv.org/html/2512.04704v1#S3.E8 "In Quadratic candidate. ‣ 3.2.3 Quadratic value function ansatz ‣ 3.2 Verification theorem and Riccati equation derivation ‣ 3 Theoretical foundations ‣ Coordinated Mean-Field Control for Systemic Risk").

##### Acknowledgments

The author is grateful to Ivana Alexandrova and to the late Thomas B. Woolf for their helpful comments. A preliminary abstract of this paper has been accepted for presentation at the 2nd Dolomites Winter School on Mean-Field Systems in Finance, Neurosciences, and AI (January 2026), and the author thanks the organizers for the opportunity.

## References

* Amini et al. [2016]

  H. Amini, R. Cont, and A. Minca.
  Resilience to contagion in financial networks.
  *Mathematical Finance*, 26:329–365, 2016.
  doi:[10.1111/mafi.12051](https://doi.org/10.1111/mafi.12051).
* Amini et al. [2020]

  H. Amini, D. Filipović, and A. Minca.
  Systemic risk in networks with a central node.
  *SIAM Journal on Financial Mathematics*, 11:60–98, 2020.
  doi:[10.1137/18M1184667](https://doi.org/10.1137/18M1184667).
* Barles and Souganidis [1991]

  G. Barles and P. E. Souganidis.
  Convergence of approximation schemes for fully nonlinear second order equations.
  *Asymptotic Analysis*, 4:271–283, 1991.
  doi:[10.3233/ASY-1991-4305](https://doi.org/10.3233/ASY-1991-4305).
* Basei and Pham [2019]

  M. Basei and H. Pham.
  A weak martingale approach to linear-quadratic McKean–Vlasov stochastic control problems.
  *Journal of Optimization Theory and Applications*, 181:347–382, 2019.
  doi:[10.1007/s10957-018-01453-z](https://doi.org/10.1007/s10957-018-01453-z).
* Bauschke and Combettes [2017]

  H. H. Bauschke and P. L. Combettes.
  *Convex Analysis and Monotone Operator Theory in Hilbert Spaces*.
  Springer, 2nd edition, 2017.
  doi:[10.1007/978-3-319-48311-5](https://doi.org/10.1007/978-3-319-48311-5).
* Bayraktar et al. [2025]

  E. Bayraktar, G. Guo, W. Tang, and Y. P. Zhang.
  Systemic robustness: A mean-field particle system approach.
  *Mathematical Finance*, 35:727–744, 2025.
  doi:[10.1111/mafi.12459](https://doi.org/10.1111/mafi.12459).
* Bensoussan [2018]

  A. Bensoussan.
  *Estimation and Control of Dynamical Systems*.
  Springer, 2018.
  doi:[10.1007/978-3-319-75456-7](https://doi.org/10.1007/978-3-319-75456-7).
* Bensoussan et al. [2013]

  A. Bensoussan, J. Frehse, and P. Yam.
  *Mean Field Games and Mean Field Type Control Theory*.
  Springer, 2013.
  doi:[10.1007/978-1-4614-8508-7](https://doi.org/10.1007/978-1-4614-8508-7).
* Bensoussan et al. [2016]

  A. Bensoussan, M. H. M. Chau, and S. C. P. Yam.
  Mean field games with a dominating player.
  *Applied Mathematics and Optimization*, 74:91–128, 2016.
  doi:[10.1007/s00245-015-9309-1](https://doi.org/10.1007/s00245-015-9309-1).
* Berge [1997]

  C. Berge.
  *Topological Spaces: Including a Treatment of Multi-Valued Functions, Vector Spaces and Convexity*.
  Dover Publications, 1997.
  Reprint of the 1963 English translation by E. M. Patterson.
* Bo and Capponi [2015]

  L. Bo and A. Capponi.
  Systemic risk in interbanking networks.
  *SIAM Journal on Financial Mathematics*, 6:386–424, 2015.
  doi:[10.1137/130937664](https://doi.org/10.1137/130937664).
* Carmona [2016]

  R. Carmona.
  *Lectures on BSDEs, Stochastic Control, and Stochastic Differential Games with Financial Applications*.
  SIAM, 2016.
  doi:[10.1137/1.9781611974249](https://doi.org/10.1137/1.9781611974249).
* Carmona and Delarue [2013]

  R. Carmona and F. Delarue.
  Probabilistic analysis of mean-field games.
  *SIAM Journal on Control and Optimization*, 51:2705–2734, 2013.
  doi:[10.1137/120883499](https://doi.org/10.1137/120883499).
* Carmona and Delarue [2018a]

  R. Carmona and F. Delarue.
  *Probabilistic Theory of Mean Field Games with Applications I: Mean Field FBSDEs, Control, and Games*.
  Springer, 2018a.
  doi:[10.1007/978-3-319-58920-6](https://doi.org/10.1007/978-3-319-58920-6).
* Carmona and Delarue [2018b]

  R. Carmona and F. Delarue.
  *Probabilistic Theory of Mean Field Games with Applications II: Mean Field Games with Common Noise and Master Equations*.
  Springer, 2018b.
  doi:[10.1007/978-3-319-56436-4](https://doi.org/10.1007/978-3-319-56436-4).
* Carmona et al. [2015]

  R. Carmona, J. Fouque, and L. Sun.
  Mean field games and systemic risk.
  *Communications in Mathematical Sciences*, 13:911–933, 2015.
  doi:[10.4310/CMS.2015.v13.n4.a4](https://doi.org/10.4310/CMS.2015.v13.n4.a4).
* Cont and Hu [2025]

  R. Cont and A. Hu.
  Homogenization and mean-field approximation for multi-player games, 2025.
  preprint, arXiv:2502.12389v1 [math.OC].
* Cont et al. [2013]

  R. Cont, A. Moussa, and E. B. Santos.
  Network structure and systemic risk in banking systems.
  In J. Fouque and J. A. Langsam, editors, *Handbook on Systemic Risk*, pages 327–368. Cambridge University Press, 2013.
  doi:[doi.org/10.1017/CBO9781139151184.018](https://doi.org/doi.org/10.1017/CBO9781139151184.018).
* Cont et al. [2021]

  R. Cont, X. Guo, and R. Xu.
  Interbank lending with benchmark rates: Pareto optima for a class of singular control games.
  *Mathematical Finance*, 31:1357–1393, 2021.
  doi:[10.1111/mafi.12325](https://doi.org/10.1111/mafi.12325).
* Crandall et al. [1992]

  M. G. Crandall, H. Ishii, and P.-L. Lions.
  User’s guide to viscosity solutions of second order partial differential equations.
  *Bulletin of the American Mathematical Society*, 27:1–67, 1992.
  doi:[10.1090/S0273-0979-1992-00266-5](https://doi.org/10.1090/S0273-0979-1992-00266-5).
* Cuchiero et al. [2024]

  C. Cuchiero, C. Reisinger, and S. Rigger.
  Optimal bailout strategies resulting from the drift controlled supercooled stefan problem.
  *Annals of Operations Research*, 336:1315–1349, 2024.
  doi:[10.1007/s10479-023-05293-7](https://doi.org/10.1007/s10479-023-05293-7).
* de Crescenzo et al. [2025]

  A. de Crescenzo, F. de Feo, and H. Pham.
  Linear-quadratic optimal control for non-exchangeable mean-field SDEs and applications to systemic risk, 2025.
  preprint, arXiv.2503.03318v1 [math.OC].
* Feinstein and Søjmark [2021]

  Z. Feinstein and A. Søjmark.
  Dynamic default contagion in heterogeneous interbank systems.
  *SIAM Journal on Financial Mathematics*, 12:SC83–SC97, 2021.
  doi:[10.1137/20M1376765](https://doi.org/10.1137/20M1376765).
* Fleming and Soner [2006]

  W. H. Fleming and H. M. Soner.
  *Controlled Markov Processes and Viscosity Solutions*.
  Springer, 2nd edition, 2006.
  doi:[10.1007/0-387-31071-1](https://doi.org/10.1007/0-387-31071-1).
* Fouque and Ichiba [2013]

  J. Fouque and T. Ichiba.
  Stability in a model of interbank lending.
  *SIAM Journal on Financial Mathematics*, 4:784–803, 2013.
  doi:[10.1137/110841096](https://doi.org/10.1137/110841096).
* Freixas et al. [2000]

  X. Freixas, B. M. Parigi, and J.-C. Rochet.
  Systemic risk, interbank relations, and liquidity provision by the central bank.
  *Journal of Money, Credit, and Banking*, 32:611–638, 2000.
  doi:[10.2307/2601198](https://doi.org/10.2307/2601198).
* Gai and Kapadia [2010]

  P. Gai and S. Kapadia.
  Contagion in financial networks.
  *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 466:2401–2423, 2010.
  doi:[10.1098/rspa.2009.0410](https://doi.org/10.1098/rspa.2009.0410).
* Giegrich et al. [2024]

  M. Giegrich, C. Reisinger, and Y. Zhang.
  Convergence of policy gradient methods for finite-horizon exploratory linear-quadratic control problems.
  *SIAM Journal on Control and Optimization*, 62:1060–1092, 2024.
  doi:[10.1137/22M1533517](https://doi.org/10.1137/22M1533517).
* Hambly and Søjmark [2019]

  B. Hambly and A. Søjmark.
  An SPDE model for systemic risk with endogenous contagion.
  *Finance and Stochastics*, 23:535–594, 2019.
  doi:[10.1007/s00780-019-00396-1](https://doi.org/10.1007/s00780-019-00396-1).
* Hambly et al. [2021]

  B. Hambly, R. Xu, and H. Yang.
  Policy gradient methods for the noisy linear quadratic regulator over a finite horizon.
  *SIAM Journal on Control and Optimization*, 59:3359–3391, 2021.
  doi:[10.1137/20M1382386](https://doi.org/10.1137/20M1382386).
* Hansen and Sargent [2008]

  L. P. Hansen and T. J. Sargent.
  *Robustness*.
  Princeton University Press, 2008.
* Hartman [2002]

  P. Hartman.
  *Ordinary Differential Equations*.
  SIAM, 2nd edition, 2002.
  doi:[10.1137/1.9780898719222](https://doi.org/10.1137/1.9780898719222).
* Huang [2010]

  M. Huang.
  Large-population LQG games involving a major player: The Nash certainty equivalence principle.
  *SIAM Journal on Control and Optimization*, 48:3318–3353, 2010.
  doi:[10.1137/080735370](https://doi.org/10.1137/080735370).
* Huang et al. [2006]

  M. Huang, R. P. Malhamé, and P. E. Caines.
  Large population stochastic dynamic games: Closed-loop McKean-Vlasov systems and the Nash certainty equivalence principle.
  *Communications in Information and Systems*, 6:221–252, 2006.
  doi:[10.4310/CIS.2006.v6.n3.a5](https://doi.org/10.4310/CIS.2006.v6.n3.a5).
* Ishii and Lions [1990]

  H. Ishii and P.-L. Lions.
  Viscosity solutions of fully nonlinear second-order elliptic partial differential equations.
  *Journal of Differential Equations*, 83:26–78, 1990.
  doi:[10.1016/0022-0396(90)90068-Z](https://doi.org/10.1016/0022-0396(90)90068-Z).
* Karatzas and Shreve [1998]

  I. Karatzas and S. E. Shreve.
  *Brownian Motion and Stochastic Calculus*.
  Springer, 2nd edition, 1998.
  doi:[10.1007/978-1-4612-0949-2](https://doi.org/10.1007/978-1-4612-0949-2).
* Kullback and Leibler [1951]

  S. Kullback and R. Leibler.
  On information and sufficiency.
  *Annals of Mathematical Statistics*, 22:79–86, 1951.
  doi:[10.1214/aoms/1177729694](https://doi.org/10.1214/aoms/1177729694).
* Lasry and Lions [2007]

  J.-M. Lasry and P.-L. Lions.
  Mean field games.
  *Japanese Journal of Mathematics*, 2:229–260, 2007.
  doi:[10.1007/s11537-007-0657-8](https://doi.org/10.1007/s11537-007-0657-8).
* Lions [1983]

  P. L. Lions.
  Optimal control of diffusion processes and Hamilton–Jacobi–Bellman equations part 2: viscosity solutions and uniqueness.
  *Communications in Partial Differential Equations*, 8:1229–1276, 1983.
  doi:[10.1080/03605308308820301](https://doi.org/10.1080/03605308308820301).
* Minca and Sulem [2014]

  A. Minca and A. Sulem.
  Optimal control of interbank contagion under complete information.
  *Statistics and Risk Modeling*, 31:23–48, 2014.
  doi:[10.1515/strm-2013-1165](https://doi.org/10.1515/strm-2013-1165).
* Petersen et al. [2000]

  I. R. Petersen, M. R. James, and P. Dupuis.
  Minimax optimal control of stochastic uncertain systems with relative entropy constraints.
  *IEEE Transactions on Automatic Control*, 45:398–412, 2000.
  doi:[10.1109/9.847720](https://doi.org/10.1109/9.847720).
* Pham [2009]

  H. Pham.
  *Continuous-time Stochastic Control and Optimization with Financial Applications*.
  Springer, 2009.
  doi:[10.1007/978-3-540-89500-8](https://doi.org/10.1007/978-3-540-89500-8).
* Reisinger et al. [2024]

  C. Reisinger, W. Stockinger, and Y. Zhang.
  A fast iterative PDE-based algorithm for feedback controls of nonsmooth mean-field control problems.
  *SIAM Journal on Scientific Computing*, 46:A2737–A2773, 2024.
  doi:[10.1137/21M1441158](https://doi.org/10.1137/21M1441158).
* Royden and Fitzpatrick [2010]

  H. L. Royden and P. M. Fitzpatrick.
  *Real Analysis*.
  Pearson, 4th edition, 2010.
* Sion [1958]

  M. Sion.
  On general minimax theorems.
  *Pacific Journal of Mathematics*, 8:171–176, 1958.
* Soner [1986]

  H. M. Soner.
  Optimal control with state-space constraint II.
  *SIAM Journal on Control and Optimization*, 24:1110–1122, 1986.
  doi:[10.1137/0324067](https://doi.org/10.1137/0324067).
* Sun [2018]

  L. Sun.
  Systemic risk and interbank lending.
  *Journal of Optimization Theory and Applications*, 179:400–424, 2018.
  doi:[10.1007/s10957-017-1185-1](https://doi.org/10.1007/s10957-017-1185-1).
* Veraart and Aldasoro [2025]

  L. A. M. Veraart and I. Aldasoro.
  Systemic risk in markets with multiple central counterparties.
  *Mathematical Finance*, 35:214–262, 2025.
  doi:[10.1111/mafi.12446](https://doi.org/10.1111/mafi.12446).
* Yong [2013]

  J. Yong.
  Linear-quadratic optimal control problems for mean-field stochastic differential equations.
  *SIAM Journal on Control and Optimization*, 51:2809–2838, 2013.
  doi:[10.1137/120892477](https://doi.org/10.1137/120892477).
* Yong and Zhou [1999]

  J. Yong and X. Y. Zhou.
  *Stochastic Controls: Hamiltonian Systems and HJB Equations*.
  Springer, 1999.
  doi:[10.1007/978-1-4612-1466-3](https://doi.org/10.1007/978-1-4612-1466-3).
* Øksendal [2003]

  B. Øksendal.
  *Stochastic Differential Equations: An Introduction with Applications*.
  Springer, 6th edition, 2003.
  doi:[10.1007/978-3-642-14394-6](https://doi.org/10.1007/978-3-642-14394-6).
* Øksendal and Sulem [2019]

  B. Øksendal and A. Sulem.
  *Applied Stochastic Control of Jump Diffusions*.
  Springer, 3rd edition, 2019.
  doi:[10.1007/978-3-030-02781-0](https://doi.org/10.1007/978-3-030-02781-0).