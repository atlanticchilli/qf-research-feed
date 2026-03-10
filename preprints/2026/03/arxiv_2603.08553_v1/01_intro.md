---
authors:
- Saeed Asadi
- Jonathan Yu-Meng Li
doc_id: arxiv:2603.08553v1
family_id: arxiv:2603.08553
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios'
url_abs: http://arxiv.org/abs/2603.08553v1
url_html: https://arxiv.org/html/2603.08553v1
venue: arXiv q-fin
version: 1
year: 2026
---


Saeed Asadi       Jonathan Yu-Meng Li
  
Telfer School of Management
  
University of Ottawa
  
sasad053@uottawa.ca, jonathan.li@telfer.uottawa.ca

###### Abstract

We propose Generative Adversarial Regression (GAR), a framework for learning conditional risk scenarios through generators aligned with downstream risk objectives. GAR builds on a regression characterization of conditional risk for elicitable functionals, including quantiles, expectiles, and jointly elicitable pairs. We extend this principle from point prediction to generative modeling by training generators whose policy-induced risk matches that of real data under the same context. To ensure robustness across all policies, GAR adopts a minimax formulation in which an adversarial policy identifies worst-case discrepancies in risk evaluation while the generator adapts to eliminate them. This structure preserves alignment with the risk functional across a broad class of policies rather than a fixed, pre-specified set. We illustrate GAR through a tail-risk instantiation based on jointly elicitable (VaR,ES)(\mathrm{VaR},\mathrm{ES}) objectives. Experiments on S&P 500 data show that GAR produces scenarios that better preserve downstream risk than unconditional, econometric, and direct predictive baselines while remaining stable under adversarially selected policies.

Keywords: Generative Models, Conditional Scenarios, Risk Measures, Elicitability, Value-at-Risk (VaR), Expected Shortfall (ES), Robust Optimization

## 1 Introduction

Scenario generators are a standard tool in risk-sensitive decision pipelines. They produce plausible future trajectories, which are then propagated through downstream decision policies to generate outcomes on which a risk functional is evaluated. This workflow appears broadly across risk management applications, including finance, operations, and other settings where decisions must remain reliable under uncertain future trajectories.

A central requirement for scenario generators in practice is *conditionality*: risk depends on the current state, and scenario generators are expected to adapt to covariates that summarize the relevant context. In financial risk management—our motivating application—this requirement underlies stress testing and regulatory emphasis on specific market regimes. The same principle applies more generally whenever risk varies systematically with observed conditions.

Beyond the challenges of generating high-dimensional objects such as trajectories and incorporating conditional information, scenario generators often suffer from *risk misalignment*. In practice, generators are typically trained to make synthetic trajectories distributionally similar to historical ones under generic discrepancy criteria. Yet downstream risk is evaluated only after scenarios are mapped into outcomes by a policy, and distributional similarity at the trajectory level does not, in general, target the decision-relevant aspects of the conditional distribution that determine the resulting risk. This gap is particularly pronounced in high-dimensional settings and for risk functionals that emphasize rare-but-consequential events: discrepancies that appear negligible under standard distributional metrics can translate into materially incorrect risk assessments once a downstream policy extracts the relevant signal.

This paper proposes *Generative Adversarial Regression (GAR)*, a risk-aligned framework for conditional scenario generation in high dimensions. GAR leverages a regression characterization of conditional risk, available for risk functionals satisfying the property of elicitability ([[7](#bib.bib3 "Making and evaluating point forecasts")]). Rather than treating scenario generation and risk evaluation as separate stages, GAR defines the regression target directly as the policy-induced risk implied by the generator under the same context. In this way, the generator is trained to align its outputs with the downstream risk functional itself, rather than with an intermediate notion of distributional similarity.

A central bottleneck in this design is the choice of policies used to evaluate risk. Downstream policies are not fixed in practice—owing to re-tuning, changing constraints, or evolving objectives—and existing approaches often rely on guarantees tied to a finite, pre-specified set of policies. To overcome this limitation, GAR incorporates robustness to policy shift through a minimax formulation. The generator is trained against an adversarial policy that searches for worst-case discrepancies in risk evaluation, thereby ensuring risk-alignment beyond any fixed finite policy set.

#### Related work

Conditional generative models for time series. Conditional simulation of time series is commonly approached through conditional generative models, most notably Conditional GANs and their variants. In finance, an early wave of work uses generative models to simulate market trajectories, learning the joint distribution of time-series paths from historical data ([[15](#bib.bib46 "Modeling financial time-series with generative adversarial networks"), [18](#bib.bib29 "Time-series generative adversarial networks"), [17](#bib.bib32 "Quant gans: deep generation of financial time series")]). For conditional generation, several papers adopt the Conditional-GAN framework ([[13](#bib.bib7 "Conditional generative adversarial nets")]) to condition on market covariates or state summaries ([[6](#bib.bib73 "Time series simulation by conditional generative adversarial networks"), [11](#bib.bib88 "Generative adversarial networks for financial trading strategies fine-tuning and combination"), [12](#bib.bib52 "Sig-wasserstein gans for conditional time series generation"), [16](#bib.bib36 "Fin-gan: forecasting and classifying financial time series via generative adversarial networks")]). With the exception of approaches that incorporate domain-specific objectives (e.g., [[16](#bib.bib36 "Fin-gan: forecasting and classifying financial time series via generative adversarial networks")]), most of this literature trains generators using generic distributional discrepancy criteria such as Jensen–Shannon or Wasserstein-type divergences. While effective for matching overall distributional mass, such criteria are not tailored to downstream risk and may underweight rare but consequential events.

Tail-aware modeling and evaluation.
A complementary line of work targets heavy tails and extremes by blending generative modeling with tools from extreme value theory. For example, Pareto-GAN ([[9](#bib.bib33 "Pareto gan: extending the representational power of gans to heavy-tailed distributions")]) leverages EVT to better match marginal tail behavior, but its performance can hinge on accurate tail-index estimation, which is statistically demanding in practice. More broadly, tail matching is not, by itself, a risk-aligned notion of fidelity: many risk functionals—such as expectiles or distortion-based criteria—depend on the full distribution, not merely its asymptotic tails. From a risk-management perspective, scenario generators should therefore be judged by whether they reproduce the distributional features that matter for the chosen risk criterion and downstream decisions, rather than by generic trajectory similarity or tail fit alone.

Risk-aligned scoring for generators.
Most closely related to our work, [[3](#bib.bib67 "TAIL-gan: learning to simulate tail risk scenarios")] is an early effort to train market scenario generators directly against a risk functional. It fits an *unconditional* GAN using strictly consistent scoring rules for the elicitable VaR/ES pair, with downstream tail-risk evaluations serving as the learning signal.
The framework, however, remains unconditional and anchors calibration to an exogenously specified, fixed collection of benchmark policies, rendering performance sensitive to policy choice. More fundamentally for our setting, while scoring rules and elicitability are classical tools—widely used in the traditional literature on regression and forecast evaluation ([[7](#bib.bib3 "Making and evaluating point forecasts")]), their use as a *regression foundation for conditional generative modeling* has remained largely absent—in particular, to derive a regression characterization of *conditional* risk and embed it directly in scenario generation. GAR fills this gap by exploiting elicitability to define a conditional regression target and coupling it with an *adversarial* policy mechanism that identifies worst-case policies, yielding risk-aligned, context-aware scenario learning without reliance on a fixed benchmark set.

In the remainder of the paper, Sections [2](#S2 "2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") formalize conditional risk scenario generation and present GAR, which learns conditional scenarios via an elicitability-driven regression target and an adversarial policy mechanism to reduce dependence on a fixed benchmark set. Section [3](#S3 "3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") details implementation and algorithms, Section [4](#S4 "4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") presents an empirical study on S&P 500 data, and Section [5](#S5 "5 Conclusion ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") concludes.

## 2 Generative Adversarial Regression (GAR)

We study conditional scenario generation for downstream risk-sensitive decision making. We observe a dataset

|  |  |  |
| --- | --- | --- |
|  | 𝒟={(ci,yi)}i=1N\mathcal{D}=\{(c\_{i},y\_{i})\}\_{i=1}^{N} |  |

consisting of independent draws from the joint distribution of random variables (C,Y)(C,Y) defined on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). Here, C:Ω→ℝdcC:\Omega\to\mathbb{R}^{d\_{c}} denotes observable covariates (context), and Y:Ω→ℝM×TY:\Omega\to\mathbb{R}^{M\times T} denotes a high-dimensional scenario. In financial applications, YY represents a multivariate return or price trajectory over TT periods across MM assets, while CC summarizes prevailing market conditions. The formulation applies more broadly to any setting where high-dimensional trajectories are conditioned on observable context.

### 2.1 Conditional Risk Scenario Generation

The objective of conditional scenario generation is to learn a mechanism that, for each fixed cc, produces samples from the conditional law ℒ​(Y∣C=c)\mathcal{L}(Y\mid C=c). Formally, this corresponds to specifying a measurable mapping

|  |  |  |
| --- | --- | --- |
|  | G:Ω×ℝdc→ℝM×TG:\Omega\times\mathbb{R}^{d\_{c}}\to\mathbb{R}^{M\times T} |  |

such that, for each fixed cc, the random element G​(⋅,c)G(\cdot,c) has distribution ℒ​(Y∣C=c)\mathcal{L}(Y\mid C=c).

In practice, we parameterize the generator GG through a latent-variable construction. Let Z∼FZZ\sim F\_{Z} be a random variable independent of CC. A parametric conditional generator is then specified by

|  |  |  |
| --- | --- | --- |
|  | Gθ:ℝdz×ℝdc→ℝM×T,G\_{\theta}:\mathbb{R}^{d\_{z}}\times\mathbb{R}^{d\_{c}}\to\mathbb{R}^{M\times T}, |  |

and, given context cc, synthetic scenarios are generated as

|  |  |  |
| --- | --- | --- |
|  | Yθ=Gθ​(Z,c).Y\_{\theta}=G\_{\theta}(Z,c). |  |

Standard training objectives aim to match ℒ​(Gθ​(Z,c))\mathcal{L}(G\_{\theta}(Z,c)) to ℒ​(Y∣C=c)\mathcal{L}(Y\mid C=c) under a chosen distributional discrepancy. However, in high-dimensional time-series settings, distribution matching is intrinsically difficult. More importantly, small discrepancies under generic metrics may translate into substantial downstream errors once decisions and risk evaluations are applied.

To formalize downstream relevance, let π:ℝM×T→𝒰T\pi:\mathbb{R}^{M\times T}\to\mathcal{U}^{T} be a policy (decision rule)
that maps a scenario to an action sequence, and let A:ℝM×T×𝒰T→ℝA:\mathbb{R}^{M\times T}\times\mathcal{U}^{T}\to\mathbb{R}
be a deterministic aggregator.
Define a policy-induced measurable functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(Y):=A​(Y,π​(Y)),Π:ℝM×T→ℝ.\Pi(Y):=A\big(Y,\pi(Y)\big),\qquad\Pi:\mathbb{R}^{M\times T}\to\mathbb{R}. |  | (1) |

For brevity, we refer to Π\Pi as the policy-induced functional throughout, and denote LΠ=Π​(Y)L\_{\Pi}=\Pi(Y) as the real outcome. Given a conditional generator GθG\_{\theta}, the same policy induces a synthetic outcome

|  |  |  |
| --- | --- | --- |
|  | Lθ,Π=Π​(Yθ)=Π​(Gθ​(Z,c)).L\_{\theta,\Pi}=\Pi(Y\_{\theta})=\Pi\left(G\_{\theta}(Z,c)\right). |  |

##### Elicitable risk functional

Let ρ\rho be a law-invariant risk functional of primary interest (e.g., VaR/ES or an expectile). From a risk-management perspective, a conditional generator is meaningful only if it preserves policy-induced conditional risk, in the sense that

|  |  |  |
| --- | --- | --- |
|  | ρ​(Lθ,Π∣C=c)≈ρ​(LΠ∣C=c)​for​all​relevant​c​and​admissible​Π.\rho(L\_{\theta,\Pi}\mid C=c)\approx\rho(L\_{\Pi}\mid C=c)\;\;{\rm for\;all\;relevant\;}c\;{\rm and\;admissible\;}\Pi. |  |

The central challenge is to achieve such risk alignment uniformly over contexts and across a broad class of policies. To proceed, we impose first a structural assumption on the risk functional.

###### Assumption 1 (Elicitability; [[7](#bib.bib3 "Making and evaluating point forecasts")]).

The risk functional ρ\rho is elicitable on a class of distributions 𝒫\mathcal{P}. That is, there exists a scoring function
S:ℝd×ℝ→ℝS:\mathbb{R}^{d}\times\mathbb{R}\to\mathbb{R} such that for any L∼μ∈𝒫L\sim\mu\in\mathcal{P},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(L)∈arg⁡mina∈ℝd⁡𝔼​[S​(a,L)],\rho(L)\in\arg\min\_{a\in\mathbb{R}^{d}}\ \mathbb{E}\big[S(a,L)\big], |  | (2) |

and the score is strictly consistent if the minimizer is unique almost surely.

Examples of elicitable risk functionals include quantiles, expectiles, and jointly elicitable pairs such as (VaR,ES).

### 2.2 Elements of GAR

We now outline GAR in three steps.

##### Step 1: Conditional risk as regression

We first address the problem of learning conditional risk across different contexts cc. Under the elicitability assumption, conditional risk admits a regression characterization. For a fixed policy-induced functional Π\Pi and context cc, applying elicitability conditionally yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(LΠ∣C=c)∈arg⁡mina∈ℝd⁡𝔼​[S​(a,LΠ)∣C=c].\rho(L\_{\Pi}\mid C=c)\in\arg\min\_{a\in\mathbb{R}^{d}}\ \mathbb{E}\big[S(a,L\_{\Pi})\mid C=c\big]. |  | (3) |

Consider minimizing the unconditional expected score over measurable predictors a​(⋅)a(\cdot):

|  |  |  |  |
| --- | --- | --- | --- |
|  | mina​(⋅)⁡𝔼​[S​(a​(C),LΠ)].\min\_{a(\cdot)}\ \mathbb{E}\big[S(a(C),L\_{\Pi})\big]. |  | (4) |

By the law of iterated expectations, the objective decomposes pointwise in cc. Strict consistency therefore implies that any minimizer satisfies

|  |  |  |
| --- | --- | --- |
|  | a​(c)=ρ​(LΠ∣C=c)​for​almost​every​c.a(c)=\rho(L\_{\Pi}\mid C=c)\;{\rm for\;almost\;every\;}c. |  |

Hence, learning the conditional risk function c↦ρ​(LΠ∣C=c)c\mapsto\rho(L\_{\Pi}\mid C=c) reduces to solving a regression problem ([4](#S2.E4 "In Step 1: Conditional risk as regression ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) under the strictly consistent score.

##### Step 2: Generative regression

Our objective, however, is not merely to estimate the conditional risk a​(c)a(c), but to train a *conditional generator* GθG\_{\theta} whose induced outcomes reproduce the correct downstream risk. Fix a policy-induced functional Π\Pi. For each context cc, the generator GθG\_{\theta} produces a synthetic
scenario Gθ​(Z,c)G\_{\theta}(Z,c), which induces the synthetic outcome Π​(Gθ​(Z,c))\Pi\left(G\_{\theta}(Z,c)\right). The generator therefore determines the conditional risk

|  |  |  |  |
| --- | --- | --- | --- |
|  | aθ,Π​(c):=ρ​(Π​(Gθ​(Z,C))∣C=c).a\_{\theta,\Pi}(c):=\rho\big(\Pi(G\_{\theta}(Z,C))\mid C=c\big). |  | (5) |

Embedding this generator-implied predictor into the regression formulation ([4](#S2.E4 "In Step 1: Conditional risk as regression ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) yields the generative regression objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ⁡𝔼​[S​(aθ,Π​(C),LΠ)]=minθ⁡𝔼​[S​(ρ​(Π​(Gθ​(Z,C))∣C),Π​(Y))].\min\_{\theta}\ \mathbb{E}\Big[S\big(a\_{\theta,\Pi}(C),\ L\_{\Pi}\big)\Big]=\min\_{\theta}\ \mathbb{E}\Big[S\Big(\rho\big(\Pi(G\_{\theta}(Z,C))\mid C\big),\ \Pi(Y)\Big)\Big]. |  | (6) |

This objective trains the generator GθG\_{\theta} to align the generator-implied conditional risk ρ​(Lθ,Π∣C)\rho(L\_{\theta,\Pi}\mid C) with the true conditional risk ρ​(LΠ∣C)\rho(L\_{\Pi}\mid C) under the strictly consistent score.

A remaining challenge is to ensure risk alignment not only for a fixed Π\Pi but across a class of admissible policies. A natural extension averages the objective over a finite benchmark set {Πk}k=1K\{\Pi\_{k}\}\_{k=1}^{K}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ⁡1K​∑k=1K𝔼​[S​(ρ​(Πk​(Gθ​(Z,C))∣C),Πk​(Y))].\min\_{\theta}\ \frac{1}{K}\sum\_{k=1}^{K}\mathbb{E}\Big[S\Big(\rho\big(\Pi\_{k}(G\_{\theta}(Z,C))\mid C\big),\ \Pi\_{k}(Y)\Big)\Big]. |  | (7) |

While this enforces risk alignment for the chosen benchmark strategies, performance remains guaranteed only for that fixed collection and may not generalize beyond it.

##### Step 3: Adversarial policy robustification (GAR)

To address this limitation, GAR replaces the finite benchmark set with a rich admissible policy class and trains the generator against the worst-case policy in that class.

Let {Πϕ}ϕ∈Φ\{\Pi\_{\phi}\}\_{\phi\in\Phi} denote a parameterized family of admissible policy-induced functionals. GAR solves the minimax problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ⁡maxϕ∈Φ⁡𝔼​[S​(ρ​(Πϕ​(Gθ​(Z,C))∣C),Πϕ​(Y))].\min\_{\theta}\ \max\_{\phi\in\Phi}\ \mathbb{E}\Big[S\Big(\rho\big(\Pi\_{\phi}(G\_{\theta}(Z,C))\mid C\big),\ \Pi\_{\phi}(Y)\Big)\Big]. |  | (8) |

The inner maximization identifies policies under which the discrepancy between real and synthetic conditional risk is largest under the score SS, while the outer minimization adjusts the generator to eliminate these discrepancies. Consequently, the learned generator preserves policy-induced conditional risk uniformly over contexts and across the admissible policy class, rather than being calibrated to a fixed, potentially brittle set of policies.

## 3 End-to-End Training and Optimization of GAR

In this section, we operationalize the three core elements of GAR and describe the end-to-end procedure used to solve the minimax objective in ([8](#S2.E8 "In Step 3: Adversarial policy robustification (GAR) ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")). Specifically, we detail (i) the choice of elicitable risk targets and strictly consistent scoring rules, (ii) the estimation of generator-implied conditional risk, and (iii) the adversarial policy class together with alternating stochastic updates for the GAR minimax objective. To highlight the distinction between GAR and existing unconditional approaches calibrated to a fixed set of benchmark policies, Figure [1](#S3.F1 "Figure 1 ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") contrasts the corresponding training pipelines.

![Refer to caption](2603.08553v1/uncon-nonrob.png)


(a) Baseline: unconditional + fixed trading strategies

![Refer to caption](2603.08553v1/con-rob.png)


(b) GAR

Figure 1: 
Comparison of training pipelines.
([1(a)](#S3.F1.sf1 "In Figure 1 ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) Baseline framework: an unconditional generator produces scenarios that are evaluated under a fixed set of policies to obtain outcomes.
([1(b)](#S3.F1.sf2 "In Figure 1 ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) Proposed framework: the generator conditions on context and is trained in a min–max game against an adversarial policy, encouraging risk estimates that are robust to worst-case policies.

### 3.1 Risk Targets and Strictly Consistent Scores

In this subsection, we specify the scoring functions used to estimate the conditional risk ρ​(L∣C=c)\rho(L\mid C=c) in ([3](#S2.E3 "In Step 1: Conditional risk as regression ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")).

We focus on three risk functionals: Value at Risk (VaR), Expected Shortfall (ES), and the
expectile. For a scalar random variable LL with cumulative distribution function FLF\_{L},
their definitions are

|  |  |  |
| --- | --- | --- |
|  | V​a​Rα​(L):=inf{ℓ∈ℝ:FL​(ℓ)≥α},E​Sα​(L):=1α​∫0αV​a​Rβ​(L)​𝑑β.VaR\_{\alpha}(L)\;:=\;\inf\big\{\,\ell\in\mathbb{R}:F\_{L}(\ell)\geq\alpha\,\big\},\qquad ES\_{\alpha}(L)\;:=\;\frac{1}{\alpha}\int\_{0}^{\alpha}VaR\_{\beta}(L)\,d\beta. |  |

The τ\tau-expectile is defined as the unique solution m∈ℝm\in\mathbb{R} to

|  |  |  |
| --- | --- | --- |
|  | τ​𝔼​[(L−m)+]=(1−τ)​𝔼​[(L−m)−],\tau\,\mathbb{E}\big[(L-m)^{+}\big]\;=\;(1-\tau)\,\mathbb{E}\big[(L-m)^{-}\big], |  |

where (x)+:=max⁡{x,0}(x)^{+}:=\max\{x,0\} and (x)−:=max⁡{−x,0}(x)^{-}:=\max\{-x,0\}.

Let ℓ\ell denote a realization of LL. Strictly consistent scores for scalar elicitable functionals include the quantile (VaR) score

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sα​(a,ℓ)=|α−𝟙{ℓ≤a}|​|ℓ−a|,S\_{\alpha}(a,\ell)\;=\;\bigl|\alpha-\mathbbm{1}\_{\{\ell\leq a\}}\bigr|\,|\ell-a|, |  | (9) |

and the expectile score

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sτ​(a,ℓ)=|τ−𝟙{ℓ≤a}|​(ℓ−a)2.S\_{\tau}(a,\ell)\;=\;\bigl|\tau-\mathbbm{1}\_{\{\ell\leq a\}}\bigr|\,(\ell-a)^{2}. |  | (10) |

However, E​SαES\_{\alpha} is not elicitable on its own, whereas the pair
(V​a​Rα,E​Sα)(VaR\_{\alpha},ES\_{\alpha}) is jointly elicitable and admits strictly consistent scoring functions. A broad class of such scores is given by [[5](#bib.bib17 "Expected shortfall is jointly elicitable with value at risk - implications for backtesting")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sα​(a,ℓ)\displaystyle S\_{\alpha}\big(a,\ell\big) | =(𝟙{ℓ≤v}−α)​(H1​(v)−H1​(ℓ))+1α​H2′​(e)​ 1{ℓ≤v}​(v−ℓ)\displaystyle=\left(\mathbbm{1}\_{\{\ell\leq v\}}-\alpha\right)\big(H\_{1}(v)-H\_{1}(\ell)\big)+\frac{1}{\alpha}H\_{2}^{\prime}(e)\,\mathbbm{1}\_{\{\ell\leq v\}}(v-\ell) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +H2′​(e)​(e−v)−H2​(e),\displaystyle\quad+H\_{2}^{\prime}(e)(e-v)-H\_{2}(e), |  | (11) |

where a:=(v,e)a:=(v,e), H1H\_{1} and H2H\_{2} are functions with H1H\_{1} increasing, and H2H\_{2} differentiable, strictly increasing,
and strictly convex.

In our experiments, we follow [[5](#bib.bib17 "Expected shortfall is jointly elicitable with value at risk - implications for backtesting")] and set
H1​(v)=vH\_{1}(v)=v and H2​(e)=s​exp⁡(e/s)H\_{2}(e)=s\exp(e/s) with scale s>0s>0. See [[1](#bib.bib16 "Backtesting expected shortfall")] for an
alternative specification of (H1,H2)(H\_{1},H\_{2}).

##### Remark

In ([11](#S3.E11 "In 3.1 Risk Targets and Strictly Consistent Scores ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")), the indicator 𝟙{ℓ≤v}\mathbbm{1}\_{\{\ell\leq v\}} is non-differentiable, so we replace it with the smooth surrogate

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟙{ℓ≤v}≈σk(v−ℓ):=11+exp⁡(−k​(v−ℓ)),\mathbbm{1}\_{\{\ell\leq v\}}\approx\sigma\_{k}(v-\ell):=\frac{1}{1+\exp(-k(v-\ell))}, |  | (12) |

with sharpness parameter k>0k>0, enabling stable backpropagation through the score.

### 3.2 Estimation of Generator-Implied Conditional Risk

For a fixed context cc and policy-induced functional Πϕ\Pi\_{\phi}, we approximate the generator-implied conditional distribution of the synthetic outcome Πϕ​(Gθ​(Z,c))\Pi\_{\phi}(G\_{\theta}(Z,c)) via Monte Carlo sampling. Specifically, for a sample size NM​CN\_{MC}, draw i.i.d. latent samples z1,…,zNM​C∼FZz\_{1},\dots,z\_{N\_{MC}}\sim F\_{Z} and form synthetic scenarios y^s=Gθ​(zs,c)\hat{y}\_{s}=G\_{\theta}(z\_{s},c) and outcomes l^s=Πϕ​(y^s)\hat{l}\_{s}=\Pi\_{\phi}(\hat{y}\_{s}), s=1,…,NM​Cs=1,\dots,N\_{MC}.

We then estimate the generator-implied conditional risk

|  |  |  |
| --- | --- | --- |
|  | aθ,Πϕ​(c):=ρ​(Πϕ​(Gθ​(Z,C))∣C=c)∈ℝda\_{\theta,\Pi\_{\phi}}(c):=\rho\!\left(\Pi\_{\phi}(G\_{\theta}(Z,C))\mid C=c\right)\in\mathbb{R}^{d} |  |

by a plug-in estimator computed from the empirical distribution of
{l^s}s=1NM​C\{\hat{l}\_{s}\}\_{s=1}^{N\_{MC}}, yielding a^θ,Πϕ​(c)=ρ​({l^s}s=1NM​C)\hat{a}\_{\theta,\Pi\_{\phi}}(c)=\rho(\{\hat{l}\_{s}\}\_{s=1}^{N\_{MC}}) (with a slight abuse of notation, we use ρ\rho both for the risk functional on distributions and for its plug-in version acting on sample).
For (VaRα,ESα)(\mathrm{VaR}\_{\alpha},\mathrm{ES}\_{\alpha}) this corresponds to the empirical quantile and tail average,
respectively. The estimate a^θ,Πϕ​(c)\hat{a}\_{\theta,\Pi\_{\phi}}(c) is the input to the scoring function in ([8](#S2.E8 "In Step 3: Adversarial policy robustification (GAR) ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ⁡maxϕ∈Φ⁡𝔼​[S​(a^θ,Πϕ​(C),Πϕ​(Y))].\min\_{\theta}\ \max\_{\phi\in\Phi}\ \mathbb{E}\Big[S\Big(\hat{a}\_{\theta,\Pi\_{\phi}}(C),\ \Pi\_{\phi}(Y)\Big)\Big]. |  | (13) |

### 3.3 Policy Class and Alternating Min–Max Optimization

##### Policy parameterization.

Recall ([1](#S2.E1 "In 2.1 Conditional Risk Scenario Generation ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")): for any policy π\pi, the scalar outcome is Π​(Y)=A​(Y,π​(Y))\Pi(Y)=A\big(Y,\pi(Y)\big). In our adversarial instantiation, given a scenario y∈ℝM×Ty\in\mathbb{R}^{M\times T}, the policy πϕ\pi\_{\phi} outputs an action sequence

|  |  |  |  |
| --- | --- | --- | --- |
|  | πϕ​(y)=[wϕ​(y1:1),wϕ​(y1:2),…,wϕ​(y1:T−1)],wϕ​(⋅)∈ℝM,\pi\_{\phi}(y)=\big[w\_{\phi}(y\_{1:1}),\;w\_{\phi}(y\_{1:2}),\;\dots,\;w\_{\phi}(y\_{1:T-1})\big],\qquad w\_{\phi}(\cdot)\in\mathbb{R}^{M}, |  | (14) |

where wϕw\_{\phi} is *causal* (non-anticipative), i.e., at time tt it depends only on the history y1:ty\_{1:t}. Such a mapping can be parameterized by a standard temporal model (e.g., a recurrent model); details of our implementation are given in Appendix [B](#A2 "Appendix B Generator and Policy Architectures ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").

Applying the deterministic aggregator AA, we obtain the policy-induced functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πϕ​(y)=A​(y,πϕ​(y)):=∑t=1T−1∑j=1M(wϕ​(y1:t))j​Δ​yj,t,Δ​yj,t:=yj,t+1−yj,t,\Pi\_{\phi}(y)=A\big(y,\pi\_{\phi}(y)\big):=\sum\_{t=1}^{T-1}\sum\_{j=1}^{M}\big(w\_{\phi}(y\_{1:t})\big)\_{j}\,\Delta y\_{j,t},\qquad\Delta y\_{j,t}:=y\_{j,t+1}-y\_{j,t}, |  | (15) |

where (wϕ​(y1:t))j\big(w\_{\phi}(y\_{1:t})\big)\_{j} denotes the jj-th component of wϕ​(y1:t)∈ℝMw\_{\phi}(y\_{1:t})\in\mathbb{R}^{M}.

To avoid degenerate adversarial policies that exploit unbounded leverage, we constrain the policy’s outputs to have a fixed total gross exposure κ>0\kappa>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖wϕ​(y1:t)‖1=κ,t=1,…,T−1,\big\|w\_{\phi}(y\_{1:t})\big\|\_{1}=\kappa,\qquad t=1,\dots,T-1, |  | (16) |

In practice, we obtain wϕ​(y1:t)w\_{\phi}(y\_{1:t}) by taking the unconstrained output hth\_{t} of the policy model and applying the normalization

|  |  |  |
| --- | --- | --- |
|  | wϕ​(y1:t)=κ​ht‖ht‖1,w\_{\phi}(y\_{1:t})=\kappa\,\frac{h\_{t}}{\|h\_{t}\|\_{1}}, |  |

which enforces ([16](#S3.E16 "In Policy parameterization. ‣ 3.3 Policy Class and Alternating Min–Max Optimization ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")).

##### Optimization (alternating stochastic min–max).

We optimize ([8](#S2.E8 "In Step 3: Adversarial policy robustification (GAR) ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) via alternating stochastic gradient steps. For a minibatch
{(ci,yi)}i=1B\{(c\_{i},y\_{i})\}\_{i=1}^{B}, we (i) update the policy parameters ϕ\phi to increase the score discrepancy,

|  |  |  |
| --- | --- | --- |
|  | ϕ←ϕ+ηϕ​∇ϕ1B​∑i=1BS​(a^θ,Πϕ​(ci),Πϕ​(yi)),\phi\leftarrow\phi+\eta\_{\phi}\nabla\_{\phi}\frac{1}{B}\sum\_{i=1}^{B}S\!\left(\hat{a}\_{\theta,\Pi\_{\phi}}(c\_{i}),\ \Pi\_{\phi}(y\_{i})\right), |  |

and then (ii) update the generator parameters θ\theta to decrease it,

|  |  |  |
| --- | --- | --- |
|  | θ←θ−ηθ​∇θ1B​∑i=1BS​(a^θ,Πϕ​(ci),Πϕ​(yi)),\theta\leftarrow\theta-\eta\_{\theta}\nabla\_{\theta}\frac{1}{B}\sum\_{i=1}^{B}S\!\left(\hat{a}\_{\theta,\Pi\_{\phi}}(c\_{i}),\ \Pi\_{\phi}(y\_{i})\right), |  |

where a^θ,Πϕ​(c)\hat{a}\_{\theta,\Pi\_{\phi}}(c) is the Monte Carlo estimate of the generator-implied conditional risk. The min–max optimization procedure is detailed in Algorithm [1](#alg1 "Algorithm 1 ‣ Optimization (alternating stochastic min–max). ‣ 3.3 Policy Class and Alternating Min–Max Optimization ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").

Algorithm 1  Alternating stochastic min–max training (GAR)

1:Training set 𝒟trn\mathcal{D}\_{\mathrm{trn}}, learning rates ηθ,ηϕ\eta\_{\theta},\eta\_{\phi}, Monte Carlo sample size NM​CN\_{MC}

2:Initialize θ←θ0\theta\leftarrow\theta\_{0}, ϕ←ϕ0\phi\leftarrow\phi\_{0}

3:for epoch n=1n=1 to NN do

4:  for minibatch ℬ={(ci,yi)}⊂𝒟trn\mathcal{B}=\{(c\_{i},y\_{i})\}\subset\mathcal{D}\_{\mathrm{trn}} do

5:Adversary update (ascent; freeze θ\theta)

6:   Freeze θ\theta

7:   for each (ci,yi)∈ℬ(c\_{i},y\_{i})\in\mathcal{B} do

8:     for s=1s=1 to NM​CN\_{MC} do

9:      Draw zs∼FZz\_{s}\sim F\_{Z}

10:      Generate synthetic scenarios y^i,s←Gθ​(zs,ci)\hat{y}\_{i,s}\leftarrow G\_{\theta}(z\_{s},c\_{i})

11:      Compute synthetic outcomes l^i,s←Πϕ​(y^i,s)\hat{l}\_{i,s}\leftarrow\Pi\_{\phi}(\hat{y}\_{i,s})

12:     end for

13:     Estimate risk a^i←ρ​({l^i,s}s=1NM​C)\hat{a}\_{i}\leftarrow\rho\!\left(\{\hat{l}\_{i,s}\}\_{s=1}^{N\_{MC}}\right)

14:     Compute real outcomes li←Πϕ​(yi)l\_{i}\leftarrow\Pi\_{\phi}(y\_{i})

15:     Compute score ℓi←S​(a^i,li)\ell\_{i}\leftarrow S(\hat{a}\_{i},l\_{i})

16:   end for

17:   ℒ^​(ϕ)←1|ℬ|​∑(ci,yi)∈ℬℓi\hat{\mathcal{L}}(\phi)\leftarrow\frac{1}{|\mathcal{B}|}\sum\_{(c\_{i},y\_{i})\in\mathcal{B}}\ell\_{i}

18:   ϕ←ϕ+ηϕ​∇ϕℒ^​(ϕ)\phi\leftarrow\phi+\eta\_{\phi}\nabla\_{\phi}\hat{\mathcal{L}}(\phi)

19:Generator update (descent; freeze ϕ\phi)

20:   Freeze ϕ\phi

21:   for each (ci,yi)∈ℬ(c\_{i},y\_{i})\in\mathcal{B} do

22:     for s=1s=1 to NM​CN\_{MC} do

23:      Draw zs∼FZz\_{s}\sim F\_{Z}

24:      Generate synthetic scenarios y^i,s←Gθ​(zs,ci)\hat{y}\_{i,s}\leftarrow G\_{\theta}(z\_{s},c\_{i})

25:      Compute synthetic outcomes l^i,s←Πϕ​(y^i,s)\hat{l}\_{i,s}\leftarrow\Pi\_{\phi}(\hat{y}\_{i,s})

26:     end for

27:     Estimate risk a^i←ρ​({l^i,s}s=1NM​C)\hat{a}\_{i}\leftarrow\rho\!\left(\{\hat{l}\_{i,s}\}\_{s=1}^{N\_{MC}}\right)

28:     Compute real outcomes li←Πϕ​(yi)l\_{i}\leftarrow\Pi\_{\phi}(y\_{i})

29:     Compute score ℓi←S​(a^i,li)\ell\_{i}\leftarrow S(\hat{a}\_{i},l\_{i})

30:   end for

31:   ℒ^​(θ)←1|ℬ|​∑(ci,yi)∈ℬℓi\hat{\mathcal{L}}(\theta)\leftarrow\frac{1}{|\mathcal{B}|}\sum\_{(c\_{i},y\_{i})\in\mathcal{B}}\ell\_{i}

32:   θ←θ−ηθ​∇θℒ^​(θ)\theta\leftarrow\theta-\eta\_{\theta}\nabla\_{\theta}\hat{\mathcal{L}}(\theta)

33:  end for

34:end for



![Refer to caption](2603.08553v1/loss_curve_enc.png)


(a) Encoder–Linear

![Refer to caption](2603.08553v1/loss_curve_lstm.png)


(b) Encoder–LSTM

Figure 2: Training/validation score curves for two generator architectures. Each experiment is repeated five times with different random seeds. The dotted line indicates the lowest attainable in-sample score. Scores are visualized with mean (solid lines) and standard deviation (shaded areas).

## 4 Numerical Experiments

We evaluate three conditional generator architectures GθG\_{\theta} (Encoder–LSTM, Encoder–Linear, and Simple–Linear; Appendix [B](#A2 "Appendix B Generator and Policy Architectures ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) in two complementary settings. First, to quantify the impact of conditionality, we fix two classes of policies and train the conditional generators under the fixed-policy objective ([7](#S2.E7 "In Step 2: Generative regression ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")), then compare against the baseline models; results are summarized in Table [1](#S4.T1 "Table 1 ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios"). Second, to study robustness to policy shift, we activate the min–max framework by treating the policy stage as an adversary and train the conditional generators via ([8](#S2.E8 "In Step 3: Adversarial policy robustification (GAR) ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")), comparing them with their fixed-policy counterparts trained under ([7](#S2.E7 "In Step 2: Generative regression ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")); results are reported in Table [2](#S4.T2 "Table 2 ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Model | VaR–ES score SαS\_{\alpha} (↓) | | | VaR viol. rate (%) |
| Train | Validation | Test | (at α=5%\alpha=5\%) |
| Unconditional | −3.747-3.747 | −3.806-3.806 | −3.765-3.765 | 1.21.2 |
| DCC–GARCH | −3.545-3.545 | −3.754-3.754 | −3.774-3.774 | 14.814.8 |
| Direct | −3.669-3.669 | −3.744-3.744 | −3.760-3.760 | 1.51.5 |
| Encoder–LSTM | -3.932 | -3.950 | -3.929 | 6.66.6 |
| Encoder–Linear | −3.911-3.911 | −3.922-3.922 | −3.920-3.920 | 2.52.5 |
| Simple–Linear | −3.887-3.887 | −3.922-3.922 | −3.922-3.922 | 2.12.1 |

Table 1: Comparison of conditional generators and baselines on the joint VaR–ES score SαS\_{\alpha} (Boldface indicates the best value in each column) and the VaR violation rate at α=5%\alpha=5\% (closer to 5%5\% indicates better calibration). The violation rate is the fraction of periods in which the realized PnL falls below the model’s VaR0.05\mathrm{VaR}\_{0.05}.

In our financial risk-management application, the policy specializes to a trading strategy applied to a price/return trajectory, and the resulting outcome is the portfolio profit-and-loss (PnL). We use daily log-returns of the following S&P 500 stocks: AAPL, INTC, T, F, BAC, NEE, MU, AMD, PFE, from 1984-06-01 to 2025-08-20, and split the dataset into training, validation, and test sets with a 80–10–10 ratio. Each sample is formed by taking the preceding 5 daily returns as conditioning information and the subsequent 10-day return path as the realized scenario. We evaluate all models using the strictly consistent joint scoring function Sα​(v,e,x)S\_{\alpha}(v,e,x) in ([11](#S3.E11 "In 3.1 Risk Targets and Strictly Consistent Scores ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) for (VaR, ES), and additionally report the VaR violation rate.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | Training Phase | | Evaluation Phase | |
|  | | Train | Validation | Benchmark | Worst-Case |
| Encoder-LSTM | Adversarial | -3.864 | -3.885 | -3.921 | -3.888 |
|  | Fixed | -3.932 | -3.950 | -3.929 | -3.558 |
| Encoder-Linear | Adversarial | -3.762 | -3.806 | -3.921 | -3.781 |
|  | Fixed | -3.911 | -3.922 | -3.920 | -1.349 |
| Simple-Linear | Adversarial | -3.799 | -3.858 | -3.855 | -3.761 |
|  | Fixed | -3.887 | 3.922 | -3.922 | 1.233 |

Table 2: Performance of conditional generators under *Fixed* and *Adversarial* training using the joint VaR–ES score Sα​(⋅)S\_{\alpha}(\cdot) (lower is better). Columns under *Training Phase* report train/validation scores obtained during each model’s own training regime (fixed-policy objective ([7](#S2.E7 "In Step 2: Generative regression ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) for *Fixed*, min–max objective ([8](#S2.E8 "In Step 3: Adversarial policy robustification (GAR) ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) for *Adversarial*). Columns under *Evaluation Phase* report test scores under benchmark (mean-reversion and trend-following) and worst-case strategies. Boldface in the Evaluation Phase highlights the better value (lower score) between *Fixed* and *Adversarial* for each architecture.

##### Conditionality impact

To quantify the value of conditioning information, we fix two classes of trading strategies—mean reversion and trend following—and compare the conditional generators with three baseline models: an unconditional generator, a Dynamic Conditional Correlation GARCH (DCC–GARCH) model, and a direct (scenario-free) linear model.

The unconditional generator is trained using the framework demonstrated in Figure [1(a)](#S3.F1.sf1 "In Figure 1 ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios"). Mathematically,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐆∗∈arg⁡minGθ⁡1K​∑k=1K𝔼​[Sα​(v​(Πk​(Gθ​(Z))),e​(Πk​(Gθ​(Z))),Πk​(Y))].\displaystyle\mathbf{G}^{\*}\in\arg\min\_{G\_{\theta}}\frac{1}{K}\sum\_{k=1}^{K}\mathbb{E}\big[S\_{\alpha}\!\big(v(\Pi\_{k}(G\_{\theta}(Z))),\,e(\Pi\_{k}(G\_{\theta}(Z))),\,\Pi\_{k}(Y)\big)\big]. |  | (17) |

This baseline model allows us to evaluate the contribution of conditioning information to scenario generation and risk estimation. Our second baseline is DCC–GARCH model ([[4](#bib.bib14 "Dynamic conditional correlation")]), a classical econometric approach for time-varying conditional covariance modeling. We fit univariate GARCH(1,1) models to each asset to capture idiosyncratic volatility dynamics, and then estimate a dynamic correlation structure to model evolving cross-asset dependence. We adopt the (1,1) specification because, among the alternative GARCH(p,q)(p,q) configurations we considered, it achieved the lowest Bayesian Information Criterion (BIC) while remaining parsimonious and standard in empirical risk-management practice. The resulting parametric model is used to simulate multivariate return scenarios.

To disentangle the benefit of conditional *scenario generation* from simply using conditioning information, we also consider a baseline that directly maps the same conditioning information to risk estimates. We call this model a direct linear model. Specifically, we fit two linear regressions to predict VaR and ES at quantile level α\alpha. Let c∈ℝM×Tc\in\mathbb{R}^{M\times T} denote the conditioning information across MM assets and TT time steps, and let cvec∈ℝD{c}^{\mathrm{vec}}\in\mathbb{R}^{D} be its vectorization with D=M×TD=M\times T. For KK strategies, the model estimates

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR^α​(c)=cvec⊤​𝐖VaR+𝐛VaR,ES^α​(c)=cvec⊤​𝐖ES+𝐛ES,\displaystyle\widehat{\text{VaR}}\_{\alpha}({c})={c}^{\mathrm{vec}\,\top}\mathbf{W}\_{\text{VaR}}+\mathbf{b}\_{\text{VaR}},\quad\widehat{\text{ES}}\_{\alpha}({c})={c}^{\mathrm{vec}\,\top}\mathbf{W}\_{\text{ES}}+\mathbf{b}\_{\text{ES}}, |  | (18) |

where 𝐖VaR,𝐖ES∈ℝD×K\mathbf{W}\_{\text{VaR}},\mathbf{W}\_{\text{ES}}\in\mathbb{R}^{D\times K} and 𝐛VaR,𝐛ES∈ℝK\mathbf{b}\_{\text{VaR}},\mathbf{b}\_{\text{ES}}\in\mathbb{R}^{K}. We use the same conditioning information as for the target conditional generators.

Figure [2](#S3.F2 "Figure 2 ‣ Optimization (alternating stochastic min–max). ‣ 3.3 Policy Class and Alternating Min–Max Optimization ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") shows the training and validation loss curves for the Encoder–LSTM and Encoder–Linear architectures. The dotted horizontal line represents an oracle benchmark, computed under the idealization that the estimated VaR and ES coincide with the realized outcomes (vi=ei=liv\_{i}=e\_{i}=l\_{i} for all ii). Under this assumption, the scoring function Sα​((vi,ei),li)S\_{\alpha}((v\_{i},e\_{i}),l\_{i}) reduces to −2​exp⁡(li/2)-2\exp(l\_{i}/2), yielding the empirical mean
ℒmin=−2N​∑i=1Nexp⁡(li/2)\mathcal{L}\_{\min}=-\frac{2}{N}\sum\_{i=1}^{N}\exp(l\_{i}/2)
over the training sample. This quantity represents the lowest attainable in-sample score under perfect forecasts and serves as a benchmark for assessing convergence quality.

Table [1](#S4.T1 "Table 1 ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") shows that all three conditional generators (Encoder–LSTM, Encoder–Linear, Simple–Linear) outperform the baselines on the joint VaR–ES score across the training, validation, and test splits. The consistent gap between the conditional generators and the unconditional generator highlights the value of market context for extreme-scenario generation. Encoder–LSTM achieves the best overall score, suggesting that explicitly modeling temporal structure improves risk-sensitive scenario generation.

Among the baselines, the unconditional generator performs best on the training and validation splits, while DCC–GARCH is slightly stronger on the test split. The direct linear model, which uses the same conditioning information but does not generate scenarios, is consistently weaker than the unconditional generator and is also outperformed by DCC–GARCH on validation and test, highlighting the benefit of distributional (scenario-based) modeling for conditional risk estimation.

For VaR calibration at α=5%\alpha=5\%, a well-calibrated VaR0.05\mathrm{VaR}\_{0.05} should be violated about 5%5\% of the time. Violation rates below 5%5\% indicate conservative VaR estimates (tail-risk overestimation), whereas rates above 5%5\% indicate aggressive VaR estimates, i.e., tail-risk underestimation. In Table [1](#S4.T1 "Table 1 ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios"), Encoder–LSTM records a 6.6%6.6\% violation rate, which is slightly above target but closest to 5%5\%. DCC–GARCH has a much higher rate (14.8%14.8\%), indicating substantial tail-risk underestimation. The remaining models are conservative: Encoder–Linear (2.5%2.5\%) and Simple–Linear (2.1%2.1\%) are closest among them, followed by Direct (1.5%1.5\%) and Unconditional (1.2%1.2\%).

![Refer to caption](2603.08553v1/combined_pnl_kde_overlay.png)


Figure 3: Sensitivity to conditioning information at PnL-level. Kernel density estimates of PnL for two strategy classes (mean reversion, trend following) under two market conditioning sample A and B, for fixed-policy and adversarial-policy training. Bottom panels: full PnL distribution; top panels: left tail (5% quantile region).

![Refer to caption](2603.08553v1/trajectories.png)


Figure 4: Sensitivity to conditioning information at Trajectory-level. For each asset and time step, densities of extreme scenarios contributing to the left tail of the PnL under two conditioning samples A and B, for adversarial-policy (top rows) and fixed-policy (bottom rows) training.

##### Adversarial policy training

Table [2](#S4.T2 "Table 2 ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") compares three conditional generator architectures trained under (i) the fixed-policy objective ([7](#S2.E7 "In Step 2: Generative regression ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")) and (ii) the adversarial (min–max) objective ([8](#S2.E8 "In Step 3: Adversarial policy robustification (GAR) ‣ 2.2 Elements of GAR ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")), and evaluates each model on benchmark strategies (mean reversion and trend following) and worst-case strategies. On benchmark strategies, the two training regimes achieve similar performance, and adversarial training is not consistently better across architectures. On worst-case strategies, however, adversarially trained models consistently outperform their fixed-policy counterparts in all three architectures, with larger gains for the simpler architectures and a smaller gap for Encoder–LSTM. Overall, these results indicate that the main benefit of adversarial training is robustness to policy shift rather than universal improvement on benchmark strategies, while the stronger stability of Encoder–LSTM suggests better inherent generalization from a more expressive temporal architecture.

To illustrate how conditioning and training regime affect the generator and downstream risk, Figures [3](#S4.F3 "Figure 3 ‣ Conditionality impact ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") and [4](#S4.F4 "Figure 4 ‣ Conditionality impact ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") examine sensitivity at two levels. Figure [3](#S4.F3 "Figure 3 ‣ Conditionality impact ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") shows the PnL level, with kernel density estimates of PnL under two strategy classes (mean reversion, trend following) and two conditioning samples, zooming on the full distribution and the left tail to show how conditioning and training regime alter tail behavior. Figure [4](#S4.F4 "Figure 4 ‣ Conditionality impact ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios") moves to the trajectory-level: for each asset and time step, we overlay densities of extreme scenarios that drive the left tail of the PnL distribution under two conditioning states, comparing fixed-policy and adversarial-policy training.

## 5 Conclusion

We proposed Generative Adversarial Regression (GAR), a framework for conditional scenario generation that aligns generative objectives with downstream risk. GAR exploits elicitability and strictly consistent scoring rules to cast conditional risk estimation as a regression problem within generative modeling. A minimax formulation with an adversarial policy ensures robustness under policy shift. Empirical results on S&P 500 data with jointly elicitable (VaR, ES) show that GAR outperforms unconditional generators, DCC–GARCH, and linear direct model baselines in fixed-policy settings, while remaining stable under worst-case policies, in contrast to the degradation observed for fixed-policy trained counterparts.

## References

* [1]
  C. Acerbi and B. Szecely (2014)
  Backtesting expected shortfall.
  Risk Magazine.
  Cited by: [§3.1](#S3.SS1.p4.4 "3.1 Risk Targets and Strictly Consistent Scores ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [2]
  K. Cho, B. van Merrienboer, D. Bahdanau, and Y. Bengio (2014)
  On the properties of neural machine translation: encoder-decoder approaches.
  External Links: 1409.1259,
  [Link](https://arxiv.org/abs/1409.1259)
  Cited by: [Appendix B](#A2.SS0.SSS0.Px4.p1.7 "Adversarial policy ‣ Appendix B Generator and Policy Architectures ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [3]
  R. Cont, M. Cucuringu, R. Xu, and C. Zhang (2023)
  TAIL-gan: learning to simulate tail risk scenarios.
  arXiv preprint, arXiv:2203.01664v3.
  Cited by: [§1](#S1.SS0.SSSx1.p3.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [4]
  R. Engle (2002)
  Dynamic conditional correlation.
  Journal of Business & Economic Statistics 20 (3),  pp. 339–350.
  External Links: [Document](https://dx.doi.org/10.1198/073500102288618487),
  [Link](https://doi.org/10.1198/073500102288618487),
  https://doi.org/10.1198/073500102288618487
  Cited by: [§4](#S4.SS0.SSS0.Px1.p3.1 "Conditionality impact ‣ 4 Numerical Experiments ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [5]
  T. Fissler, J. F. Ziegel, and T. Gneiting (2015)
  Expected shortfall is jointly elicitable with value at risk - implications for backtesting.
  External Links: 1507.00244,
  [Link](https://arxiv.org/abs/1507.00244)
  Cited by: [§3.1](#S3.SS1.p3.4 "3.1 Risk Targets and Strictly Consistent Scores ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios"),
  [§3.1](#S3.SS1.p4.4 "3.1 Risk Targets and Strictly Consistent Scores ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [6]
  R. Fu, J. Chen, S. Zeng, Y. Zhuang, and A. Sudjianto (2019)
  Time series simulation by conditional generative adversarial networks.
  arXiv preprint, arXiv:1904.11419.
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [7]
  T. Gneiting (2011)
  Making and evaluating point forecasts.
  Journal of the American Statistical Association 106 (494),  pp. 746–762.
  External Links: [Document](https://dx.doi.org/10.1198/jasa.2011.r10138)
  Cited by: [§1](#S1.SS0.SSSx1.p3.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios"),
  [§1](#S1.p4.1 "1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios"),
  [Assumption 1](#Thmassumption1 "Assumption 1 (Elicitability; [7]). ‣ Elicitable risk functional ‣ 2.1 Conditional Risk Scenario Generation ‣ 2 Generative Adversarial Regression (GAR) ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [8]
  S. Hochreiter and J. Schmidhuber (1997)
  Long short-term memory.
  Neural computation 9 (8),  pp. 1735–1780.
  Cited by: [Appendix B](#A2.SS0.SSS0.Px3.p1.9 "Encoder-LSTM ‣ Appendix B Generator and Policy Architectures ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [9]
  T. Huster, J. E. Cohen, Z. Lin, K. Chan, C. Kamhoua, N. Leslie, C. J. Chiang, and V. Sekar (2021)
  Pareto gan: extending the representational power of gans to heavy-tailed distributions.
  arXiv preprint, arXiv:2101.09113v1.
  Cited by: [§1](#S1.SS0.SSSx1.p2.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [10]
  D. P. Kingma and J. Ba (2017)
  Adam: a method for stochastic optimization.
  External Links: 1412.6980,
  [Link](https://arxiv.org/abs/1412.6980)
  Cited by: [Table 3](#A1.T3.6.10.3.1.1 "In Appendix A Configuration ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [11]
  A. S. Koshiyama, N. Firoozye, and P. C. Treleaven (2019)
  Generative adversarial networks for financial trading strategies fine-tuning and combination.
  CoRR, abs/1901.01751.
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [12]
  S. Liao, H. Ni, M. Sabate-Vidales, L. Szpruch, M. Wiese, and B. Xiao (2023)
  Sig-wasserstein gans for conditional time series generation.
  Mathematical Finance,  pp. 1–49.
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [13]
  M. Mirza and S. Osindero (2014)
  Conditional generative adversarial nets.
  External Links: 1411.1784,
  [Link](https://arxiv.org/abs/1411.1784)
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [14]
  L. N. Smith and N. Topin (2017)
  Super-convergence: very fast training of residual networks using large learning rates.
  CoRR abs/1708.07120.
  External Links: [Link](http://arxiv.org/abs/1708.07120),
  1708.07120
  Cited by: [Table 3](#A1.T3.6.8.3.1.1 "In Appendix A Configuration ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [15]
  S. Takahashi, Y. Chen, and K. Tanaka-Ishii (2019)
  Modeling financial time-series with generative adversarial networks.
  Physical A, 527.
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [16]
  M. Vuletić, F. Prenzel, and M. Cucuringu (2024)
  Fin-gan: forecasting and classifying financial time series via generative adversarial networks.
  Quantitative Finance 24,  pp. 175–199.
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [17]
  M. Wiese, R. Knobloch, R. Korn, and P. Kretschmer (2020)
  Quant gans: deep generation of financial time series.
  Quantitative Finance, 20:9,  pp. 1419–1440.
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").
* [18]
  J. Yoon, D. Jarrett, and M. van der Schaar (2019)
  Time-series generative adversarial networks.
  Vancouver, BC, Canada, December,  pp. 8–14.
  Cited by: [§1](#S1.SS0.SSSx1.p1.1 "Related work ‣ 1 Introduction ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios").

## Appendix A Configuration

|  |  |  |
| --- | --- | --- |
|  | Configuration | Values |
| Optimization | Initial learning rate | 10−1010^{-10} |
|  | Learning rate schedule | OneCycleLR ([[14](#bib.bib12 "Super-convergence: very fast training of residual networks using large learning rates")]) |
|  | Batch size | 128 |
|  | Optimization algorithm | Adam ([[10](#bib.bib11 "Adam: a method for stochastic optimization")]) |
| Data setup | Number of assets | 9 |
|  | Conditioning window length | 5 |
|  | Generated trajectory length | 10 |
| Architecture | Simple-linear | layers: 2, hidden dim: 4, activation: LeakyReLU |
|  | Encoder-linear | layers: 2, hidden dim: 4, activation: LeakyReLU |
|  | Encoder-LSTM | LSTM layers: 1, decoder layers: 1, hidden dim: 4 |
|  | Adversarial policy | GRU layers: 3, Portfolio cap (total gross exposure, κ\kappa): 1 |
| Sampling | Monte Carlo sample size | 2,000 |
|  | Latent noise distribution | 𝒩​(0,I)\mathcal{N}(0,\mathrm{I}) |
| Risk and  scoring setup | H1,H2H\_{1},H\_{2} | H1​(v)=v,H2​(e)=s​exp⁡(e/s),s=2H\_{1}(v)=v,\;H\_{2}(e)=s\,\exp(e/s),\;s=2 |
|  | Quantile (α\alpha) | 0.05 |

Table 3: Model and experiment configuration details.

## Appendix B Generator and Policy Architectures

This section summarizes the architectural components used in our experiments. We first detail the three generator architectures and then present the policy architecture used for adversarial training. Throughout, a single training sample consists of
a conditioning window c∈ℝM×Tcc\in\mathbb{R}^{M\times T\_{c}} (past returns for MM assets over
TcT\_{c} days) and a target scenario y∈ℝM×Ty\in\mathbb{R}^{M\times T} (future returns over TT
days). The generator produces y^∈ℝM×T\hat{y}\in\mathbb{R}^{M\times T} from conditioning information cc and latent noise z∈ℝdzz\in\mathbb{R}^{d\_{z}}.

##### Simple-linear

The Simple-linear generator applies the same feedforward network independently to each asset, acting only along the time dimension. We define per-asset input

|  |  |  |
| --- | --- | --- |
|  | h0,j:=[z,cj⁣⋅]∈ℝdz+Tc,h\_{0,j}:=[z,c\_{j\cdot}]\in\mathbb{R}^{d\_{z}+T\_{c}}, |  |

where cj⁣⋅c\_{j\cdot} denotes the jj-th row of cc, i.e., the conditioning sequence for asset jj, and [z,cj⁣⋅][z,c\_{j\cdot}] denotes the vector obtained by stacking zz and cj⁣⋅c\_{j\cdot}. Per-asset output is

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^j=WL⋅σ​(WL−1​…​σ​(W1​h0,j+b1)​⋯+bL−1)+bL∈ℝT,\displaystyle\hat{y}\_{j}=W\_{L}\cdot\sigma(W\_{L-1}\dots\sigma(W\_{1}h\_{0,j}+b\_{1})\cdots+b\_{L-1})+b\_{L}\in\mathbb{R}^{T}, |  | (19) |

where σ\sigma is an activation function (e.g., ReLU) and γ:=(W1,…,WL,b1,…,bL)\gamma:=(W\_{1},\dots,W\_{L},b\_{1},\dots,b\_{L})
represent all the parameters in the neural network. The full generator output is obtained by stacking rows,

|  |  |  |
| --- | --- | --- |
|  | y^=G​(z,c;γ):=[y^1⊤⋮y^M⊤]∈ℝM×T,\hat{y}=G(z,c;\gamma):=\begin{bmatrix}\hat{y}\_{1}^{\top}\\ \vdots\\ \hat{y}\_{M}^{\top}\end{bmatrix}\in\mathbb{R}^{M\times T}, |  |

This architecture imposes no
temporal or cross-asset inductive bias beyond the shared per-asset network.

##### Encoder-linear

The Encoder-linear generator uses a global encoder over both assets and time, followed by a
decoder. Let c¯∈ℝM​Tc\bar{c}\in\mathbb{R}^{MT\_{c}} denote the vectorization of c. The encoder takes
h0E:=c¯h^{\mathrm{E}}\_{0}:=\bar{c} and produces the encoded representation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^=E​(c¯;ϕ):=WL1E⋅σ​(WL1−1E​⋯​σ​(W1E​h0E+b1E)​⋯+bL1−1E)+bL1E∈ℝdh,\displaystyle\hat{H}=\mathrm{E}(\bar{c};\phi):=W^{\mathrm{E}}\_{L\_{1}}\cdot\sigma(W^{\mathrm{E}}\_{L\_{1}-1}\cdots\sigma(W^{\mathrm{E}}\_{1}h^{\mathrm{E}}\_{0}+b^{E}\_{1})\cdots+b^{E}\_{L\_{1}-1})+b^{\mathrm{E}}\_{L\_{1}}\in\mathbb{R}^{d\_{h}}, |  | (20) |

with encoder parameters ϕ:=(W1E,…,WL1E,b1E,…,bL1E)\phi:=(W^{\mathrm{E}}\_{1},\dots,W^{\mathrm{E}}\_{L\_{1}},b^{\mathrm{E}}\_{1},\dots,b^{\mathrm{E}}\_{L\_{1}}). The decoder input is the joint vector h0D:=[H^,z]∈ℝdh+dzh^{\mathrm{D}}\_{0}:=[\hat{H},z]\in\mathbb{R}^{d\_{h}+d\_{z}}, and the decoder output is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y^=D​(H^,z;θ):=WL2D⋅σ​(WL2−1D​⋯​σ​(W1D​h0D+b1D)​⋯+bL2−1D)+bL2D∈ℝM​T,\displaystyle\hat{Y}=D(\hat{H},z;\theta):=W^{\mathrm{D}}\_{L\_{2}}\cdot\sigma(W^{\mathrm{D}}\_{L\_{2}-1}\cdots\sigma(W^{\mathrm{D}}\_{1}h^{\mathrm{D}}\_{0}+b^{D}\_{1})\cdots+b^{D}\_{L\_{2}-1})+b^{\mathrm{D}}\_{L\_{2}}\in\mathbb{R}^{MT}, |  | (21) |

with parameters θ:=(W1D,…,WL2D,b1D,…,bL2D)\theta:=(W^{\mathrm{D}}\_{1},\dots,W^{\mathrm{D}}\_{L\_{2}},b^{\mathrm{D}}\_{1},\dots,b^{\mathrm{D}}\_{L\_{2}}). Then we reshape the output Y^∈ℝM​T\hat{Y}\in\mathbb{R}^{MT} to
y^∈ℝM×T\hat{y}\in\mathbb{R}^{M\times T}. This architecture learns a non-linear global encoding of the conditioning panel cc while
keeping a simple fully connected decoder.

##### Encoder-LSTM

The Encoder–LSTM generator uses a recurrent encoder over time with cross-sectional inputs.
We view the conditioning window as a time series of cross-sectional vectors

|  |  |  |
| --- | --- | --- |
|  | c=(c1,…,cTc),ct∈ℝM,c=(c\_{1},\dots,c\_{T\_{c}}),\qquad c\_{t}\in\mathbb{R}^{M}, |  |

where ctc\_{t} collects the MM asset returns at time tt. The encoder is a Long Short-Term
Memory (LSTM) network ([[8](#bib.bib13 "Long short-term memory")]) with input dimension MM and hidden
dimension dhd\_{h} with parameters ϕ\phi. For each layer l=1,…,Ll=1,\dots,L, the hidden state htl∈ℝdhh\_{t}^{l}\in\mathbb{R}^{d\_{h}} and cell state stl∈ℝdhs\_{t}^{l}\in\mathbb{R}^{d\_{h}} are updated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | htl,stl=fLSTM​(ht−1l,st−1l,xtl;ϕ)\displaystyle h\_{t}^{l},s\_{t}^{l}=f\_{\mathrm{LSTM}}(h\_{t-1}^{l},s\_{t-1}^{l},x\_{t}^{l};\phi) |  | (22) |

using the standard LSTM function. (h0,s0)(h\_{0},s\_{0}) default to zeros if not provided. The input xtlx\_{t}^{l} to layer ll is

|  |  |  |
| --- | --- | --- |
|  | xtl={ctfor ​l=1,htl−1for ​l≥2.x\_{t}^{l}=\begin{cases}c\_{t}&\text{for }l=1,\\ h\_{t}^{l-1}&\text{for }l\geq 2.\end{cases} |  |

The encoder representation is the final hidden state,

|  |  |  |
| --- | --- | --- |
|  | H^=E​(c;ϕ):=hTcL∈ℝdh.\hat{H}=\mathrm{E}(c;\phi):=h\_{T\_{c}}^{L}\in\mathbb{R}^{d\_{h}}. |  |

The decoder is identical to the Encoder-linear case: it maps (H^,z)(\hat{H},z) to a vector in
ℝM​T\mathbb{R}^{MT} and reshapes it to an M×TM\times T trajectory matrix. This variant allows the encoder to exploit both temporal and cross-asset structure in the
conditioning information.

##### Adversarial policy

Recall ([14](#S3.E14 "In Policy parameterization. ‣ 3.3 Policy Class and Alternating Min–Max Optimization ‣ 3 End-to-End Training and Optimization of GAR ‣ Generative Adversarial Regression (GAR): Learning Conditional Risk Scenarios")): for a scenario y∈ℝM×Ty\in\mathbb{R}^{M\times T}, the policy πϕ\pi\_{\phi} outputs action sequences

|  |  |  |  |
| --- | --- | --- | --- |
|  | πϕ​(y)=[wϕ​(y1:1),wϕ​(y1:2),…,wϕ​(y1:T−1)],wϕ​(⋅)∈ℝM.\pi\_{\phi}(y)=\big[w\_{\phi}(y\_{1:1}),\ w\_{\phi}(y\_{1:2}),\ \ldots,\ w\_{\phi}(y\_{1:T-1})\big],\qquad w\_{\phi}(\cdot)\in\mathbb{R}^{M}. |  | (23) |

We implement wϕw\_{\phi} using a multi-layer Gated Recurrent Unit (GRU) ([[2](#bib.bib1 "On the properties of neural machine translation: encoder-decoder approaches")]) with parameters ϕ\phi. For each layer l=1,…,Ll=1,\ldots,L and time t=1,…,T−1t=1,\ldots,T-1, the hidden state htl∈ℝdhh\_{t}^{l}\in\mathbb{R}^{d\_{h}} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | htl=fGRU​(ht−1l,xtl;ϕ),h\_{t}^{l}=f\_{\mathrm{GRU}}(h\_{t-1}^{l},\,x\_{t}^{l};\,\phi), |  | (24) |

with h0l=𝟎h\_{0}^{l}=\mathbf{0}. We set dh=Md\_{h}=M so that the final hidden state can be interpreted as asset-wise raw actions. The input xtlx\_{t}^{l} to layer ll is

|  |  |  |
| --- | --- | --- |
|  | xtl={ytfor ​l=1,htl−1for ​l≥2.x\_{t}^{l}=\begin{cases}y\_{t}&\text{for }l=1,\\ h\_{t}^{l-1}&\text{for }l\geq 2.\end{cases} |  |

The raw actions at time tt is

|  |  |  |  |
| --- | --- | --- | --- |
|  | wϕ​(y1:t)=htLfor ​t=1,…,T−1.w\_{\phi}(y\_{1:t})=h\_{t}^{L}\quad\text{for }t=1,\ldots,T-1. |  | (25) |

These raw actions are then normalized before use in the aggregator.

BETA