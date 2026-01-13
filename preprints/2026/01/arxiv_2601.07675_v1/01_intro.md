---
authors:
- Kishan Padayachy
- Ronald Richman
- Mario V. Wüthrich
doc_id: arxiv:2601.07675v1
family_id: arxiv:2601.07675
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data'
url_abs: http://arxiv.org/abs/2601.07675v1
url_html: https://arxiv.org/html/2601.07675v1
venue: arXiv q-fin
version: 1
year: 2026
---


Kishan Padayachy111insureAI, kishan@insureai.co
  
Ronald Richman222insureAI, ronaldrichman@gmail.com
  
Mario V. Wüthrich333Department of Mathematics, ETH Zurich,
mario.wuethrich@math.ethz.ch

(January 12, 2026)

###### Abstract

We introduce Tab-TRM (Tabular-Tiny Recursive Model), a network architecture that adapts the recursive latent reasoning paradigm of Tiny Recursive Models (TRMs) to insurance modeling. Drawing inspiration from both the Hierarchical Reasoning Model (HRM) and its simplified successor TRM, the Tab-TRM model makes predictions by reasoning over the input features. It maintains two learnable latent tokens - an answer token and a reasoning state - that are iteratively refined by a compact, parameter-efficient recursive network. The recursive processing layer repeatedly updates the reasoning state given the full token sequence and then refines the answer token, in close analogy with iterative insurance pricing schemes. Conceptually, Tab-TRM bridges classical actuarial workflows - iterative generalized linear model fitting and minimum-bias calibration - on the one hand, and modern machine learning, in terms of Gradient Boosting Machines, on the other.

Keywords: Tiny Recursive Models, Hierarchical Reasoning, Insurance Pricing, Regression, Tabular Deep Learning, Credibility Theory, Recursive Neural Networks

## 1 Introduction

Many actuarial prediction problems such as pricing, reserving and experience analysis in insurance are closely related to the field of tabular machine learning; this connection has been increasingly explored in recent years. Over roughly the past decade, a growing actuarial literature has explored deep learning as a complement or alternative to classical generalized linear models (GLMs); see, for example, Wüthrich and Merz ([2023](https://arxiv.org/html/2601.07675v1#bib.bib26)) for an overview of actuarial learning tools, Richman ([2021a](https://arxiv.org/html/2601.07675v1#bib.bib16), [b](https://arxiv.org/html/2601.07675v1#bib.bib17)) for a two-part review of AI in actuarial science, and Wüthrich et al. ([2025](https://arxiv.org/html/2601.07675v1#bib.bib27)) for a wide ranging actuarial treatment of these tools.

A foundational contribution in tabular machine learning was made by Guo and Berkhahn ([2016](https://arxiv.org/html/2601.07675v1#bib.bib9)), who showed that categorical variables can be mapped into low-dimensional continuous *entity embeddings* learned jointly with the prediction task. This approach addresses the high dimensionality and sparsity of one-hot encodings of categorical variables, it allows similar categories to cluster in the embedding space, and it improves generalization - properties that are particularly valuable in insurance where high-cardinality categorical features such as vehicle type, occupation and region are ubiquitous. Building on this idea, early actuarial work demonstrated that feed-forward neural networks (FNNs) with entity embeddings for categorical covariates can be viewed as GLMs on top of learned feature transformations (Richman, [2021b](https://arxiv.org/html/2601.07675v1#bib.bib17)). With the right exposure handling, log-links and deviance-based loss functions, such architectures already deliver strong performance on pricing benchmarks while preserving core actuarial structures such as multiplicative tariffs and offsets.

In parallel, gradient boosting machines (GBMs) - in particular XGBoost - have become a de facto benchmark for predictive performance on tabular insurance data. Noll et al. ([2018](https://arxiv.org/html/2601.07675v1#bib.bib13)) compared GLMs, FNNs and GBMs on a French motor third-party liability (MTPL) portfolio and found that GBMs and neural networks consistently outperform GLMs in terms of Poisson deviance scoring, while remaining computationally tractable. GBMs excel at capturing complex feature interactions through sequential tree construction, though they lack the smooth gradient-based optimization and representation-learning capabilities of FNNs.

Several architectures aim to combine the interpretability of GLMs with the flexibility of neural networks. The *Combined Actuarial Neural Network* (CANN) of Schelldorfer and Wüthrich ([2019](https://arxiv.org/html/2601.07675v1#bib.bib22)) nests a classical GLM within a neural network via a skip-connection, allowing the network to learn residual corrections to the GLM baseline. This structure ensures that the model never performs worse than the GLM and can systematically identify missing interactions. The *LocalGLMnet* of Richman and Wüthrich ([2023](https://arxiv.org/html/2601.07675v1#bib.bib21)) takes a different approach: it allows the GLM regression coefficients themselves to be feature-dependent functions learned by a neural network. This yields a model that behaves locally as a GLM - with interpretable, policy-specific coefficients - while globally capturing nonlinear effects and interactions.

More recently, several architectures have explicitly imported modern representation-learning ideas into actuarial modeling while preserving key actuarial concepts. The *Credibility Transformer* adapts the Transformer architecture to tabular insurance data by embedding each covariate as a token and introducing a special *credibility token*. This token combines global portfolio information with observation-specific information through a credibility-weighted average, mirroring Bühlmann credibility inside an attention mechanism (Richman et al., [2025a](https://arxiv.org/html/2601.07675v1#bib.bib18)). Building on the Credibility Transformer, the In-Context Learning Enhanced Credibility Transformer (ICL-CT) attaches a *context batch* of similar insurance risks to each target policy. An in-context learning mechanism then allows the model to adapt its internal representation to local risk patterns and even generalize to unseen categorical levels (Padayachy et al., [2025](https://arxiv.org/html/2601.07675v1#bib.bib15)); in fact, this idea is very close to the foundation models used in large language models (LLMs). These examples illustrate a general pattern: deep learning models tailored to actuarial structure - exposure offsets, credibility, tariff factors - can be both accurate and interpretable.

In parallel with the actuarial deep-learning literature, LLMs have driven a rapid resurgence of interest in machine reasoning. A key observation is that LLMs which struggle with multi-step computations can dramatically improve when trained to emit intermediate steps into a “scratchpad” before producing the final answer (Nye et al., [2021](https://arxiv.org/html/2601.07675v1#bib.bib14)). This idea, popularized as *chain-of-thought* (CoT) prompting (Wei et al., [2022](https://arxiv.org/html/2601.07675v1#bib.bib25)), has inspired a range of post-training methods and test-time compute strategies for enhancing reasoning; see Appendix [C](https://arxiv.org/html/2601.07675v1#A3 "Appendix C LLM Reasoning Background ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") for details.

A complementary direction, pursued by the Hierarchical Reasoning Model (HRM) and Tiny Recursive Model (TRM), is to perform iterative refinement in a *latent* space rather than through explicit CoT text.444An interesting parallel to this is credibility; usually credibility is applied in the output space of rates, but in Richman et al. ([2025a](https://arxiv.org/html/2601.07675v1#bib.bib18)) it is applied in the latent embedding space of the model. HRM couples two Transformer-based recurrent modules that operate at different effective time scales: a fast low-level module and a slower high-level module. By recursing over a small number of latent tensors, using deep supervision across multiple “supervision steps” and an adaptive computation time mechanism, HRM achieves large effective depth with modest parameter count and demonstrates strong performance on Sudoku-Extreme, Maze-Hard and ARC-AGI, using only around 1,000 training examples and no pre-training or CoT supervision (Wang et al., [2025](https://arxiv.org/html/2601.07675v1#bib.bib24)). The *Tiny Recursive Model* (TRM) of Jolicoeur-Martineau ([2025](https://arxiv.org/html/2601.07675v1#bib.bib11)) provides a compelling simplification: it replaces the two-level structure with a single tiny network that jointly updates an embedded candidate answer 𝐚\mathbf{a} and an auxiliary latent state 𝒛\bm{z} that acts as a scratchpad of intermediate computations. At each reasoning step, the model first refines 𝒛\bm{z} given the input 𝒙\bm{x}, the current answer 𝐚\mathbf{a}, and the current state 𝒛\bm{z}, and then proposes an improved answer 𝐚\mathbf{a} conditioned on the updated 𝒛\bm{z}. TRM explicitly avoids fixed-point gradient approximations and the extra forward passes required by adaptive computation time in HRM, yet substantially improves on HRM across these benchmarks.

### 1.1 Motivation and Research Gap

From the perspective of actuarial science, LLM-based reasoning is conceptually important - it shows that explicit, multi-step computation can be learned and exploited by neural network models - but the approaches are not directly applicable as a drop-in solution for insurance pricing. Actuaries typically seek compact architectures that can be trained on a single portfolio without access to web-scale CoT data, reinforcement learning infrastructure, or the computational budgets required by test-time compute (TTC). At the same time, the grid-based benchmarks on which HRM and TRM excel share interesting structural parallels with actuarial tabular data: (i) inputs are naturally decomposed into a small, fixed set of tokens (grid cells or tariff factors); (ii) the prediction task requires combining evidence from multiple tokens to produce a single output; and (iii) iterative refinement - whether of Sudoku cell values or tariff relativities - is a natural inductive bias, well exploited by GBMs.

To date, both HRM and TRM have been evaluated almost exclusively on structured grid-based reasoning problems, where inputs and outputs are discrete symbols and the objective is exact sequence-to-sequence prediction. Here, we explore whether the same ideas - latent recursion over a small set of tokens, deep supervision, and tiny networks - translate to traditional tabular modeling problems, where the goals are accurate point forecasts for insurance pricing. We utilize the fact that tabular data have several structural features that are particularly well-suited to the TRM philosophy: (i) each feature can naturally be treated as a separate token; (ii) the number of tokens is small and fixed for a given insurance tariff structure; and (iii) a model that repeatedly refines a low-dimensional answer representation 𝐚\mathbf{a} and a global latent scratchpad 𝒛\bm{z} provides a natural inductive bias for capturing complex feature interactions without resorting to very wide or very deep FNNs.

### 1.2 Contributions

In this work we bring TRM-style latent recursion to actuarial tabular modeling. Our contributions are fourfold. First, we present, to our knowledge, the first adaptation of Tiny Recursive Models to insurance pricing or tabular machine learning. In the context of pricing, we represent each policy as a short sequence of feature tokens augmented with answer and latent reasoning tokens and introduce a practical architecture for TRM-style tabular modeling with a “tiny” recursive processing layer that repeatedly updates a global latent state and an answer token. Third, we provide empirical validation on the classical benchmark of the French MTPL data of Dutang et al. ([2024](https://arxiv.org/html/2601.07675v1#bib.bib6)), and we show that Tab-TRM achieves a strong Poisson deviance score with a very small network. Finally, we relate the advantages of tiny recursive reasoning models - previously demonstrated on synthetic and symbolic puzzles - to noisy, mixed-type tabular data, and we discuss how the architecture sits alongside other architectures such as the credibility-based Transformers and in-context learning architectures, highlighting parallels with iterative GLM fitting and GBMs.

To make Tab-TRM accessible to actuarial practitioners, it is helpful to emphasise parallels with familiar workflows. The recursive refinement of (𝐚,𝒛)(\mathbf{a},\bm{z}) can be viewed as a *learned analogue of iterative GLM fitting*. Instead of Iteratively Reweighted Least Squares (IRLS), a tiny shared network learns how to map a “working predictor” and latent tariff structure to a slightly improved one. Each recursion step is analogous to another pass through the portfolio, updating relativities and rebalancing as indications and constraints are reassessed. Another analogy is to Recurrent Neural Networks (RNNs): if one “unrolls” the recursive core over its inner and outer iterations, the effective computation closely resembles that of a RNN unrolled in time, but with two key differences: the state space is explicitly split into an answer component and a reasoning component, and deep supervision can in principle be applied at several checkpoints rather than relying on very long backpropagation through time. In this sense, Tab-TRM can be seen as a bridge between classical actuarial algorithms and RNNs that iterate hidden states over time.

##### Structure of the paper.

The remainder of this paper is organised as follows. Section [2](https://arxiv.org/html/2601.07675v1#S2 "2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") presents the Tab-TRM architecture, covering the tokenization of tabular inputs, the recursive reasoning core, and the Poisson decoder. Section [3](https://arxiv.org/html/2601.07675v1#S3 "3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") provides complementary interpretations of Tab-TRM, including connections to state-space models and gradient boosting. Section [4](https://arxiv.org/html/2601.07675v1#S4 "4 Application: French MTPL Data ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") demonstrates the methodology on the benchmark French MTPL portfolio, detailing feature encodings and hyper-parameter optimization. Section [5](https://arxiv.org/html/2601.07675v1#S5 "5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") reports empirical results, including Poisson deviance scores, interpretability diagnostics, and analysis of the learned representations. Section [6](https://arxiv.org/html/2601.07675v1#S6 "6 Linearized Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") explores a fully linearized variant of Tab-TRM and provides a state-space analysis of the learned dynamics. Section [7](https://arxiv.org/html/2601.07675v1#S7 "7 Discussion ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") relates Tab-TRM to classical actuarial workflows and other network architectures. Section [8](https://arxiv.org/html/2601.07675v1#S8 "8 Conclusion ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") concludes and outlines directions for future work. Supplementary material in the appendix includes algorithm pseudo code and hyper-parameter search ranges.

## 2 Methodology

In this section we formalize the non-life insurance claims frequency prediction problem, describe how the TRMs of Jolicoeur-Martineau ([2025](https://arxiv.org/html/2601.07675v1#bib.bib11)) are adapted to tabular insurance data, and present the resulting Tab-TRM architecture and its training procedure.

### 2.1 Problem Formulation - Poisson Claims Frequencies

To keep things simple we focus on non-life insurance claims frequency modeling using the Poisson model, and the ideas presented here can easily be adapted to other actuarial forecast problems.
The goal is to estimate the expected claim frequency for each insurance policy, conditional on observed risk characteristics (covariates, features). Formally, for each insurance policy i=1,…,ni=1,\dots,n, we observe the tuple

|  |  |  |
| --- | --- | --- |
|  | (𝒙i,𝒄i,vi,yi),(\bm{x}\_{i},\bm{c}\_{i},v\_{i},y\_{i}), |  |

where 𝒙i∈ℝpr\bm{x}\_{i}\in\mathbb{R}^{p\_{r}} is a vector of continuous covariates, 𝒄i∈ℕpc\bm{c}\_{i}\in\mathbb{N}^{p\_{c}} is a vector of categorical covariates, vi>0v\_{i}>0 is the exposure (time at risk), and yi∈ℕ0y\_{i}\in\mathbb{N}\_{0} is the observed claim count (response). Our objective is to learn a regression function Fθ:ℝpr×ℕpc→ℝ>0F\_{\theta}\colon\mathbb{R}^{p\_{r}}\times\mathbb{N}^{p\_{c}}\to\mathbb{R}\_{>0} that maps from the covariate space to the
positive real line, such that Fθ​(𝒙i,𝒄i)F\_{\theta}(\bm{x}\_{i},\bm{c}\_{i}) gives us a good approximation to the true (unknown) expected claim frequency λ​(𝒙i,𝒄i)\lambda(\bm{x}\_{i},\bm{c}\_{i}) of policyholder ii, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Yi∣𝒙i,𝒄i,vi]=vi​λ​(𝒙i,𝒄i), for all i=1,…,n.\mathbb{E}[Y\_{i}\mid\bm{x}\_{i},\bm{c}\_{i},v\_{i}]=v\_{i}\,\lambda(\bm{x}\_{i},\bm{c}\_{i}),\qquad\text{ for all $i=1,\ldots,n$.} |  | (1) |

Lifting this to a full statistical model, we furthermore assume a Poisson model for the claim counts

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi∣𝒙i,𝒄i,vi∼Poisson​(vi​λ​(𝒙i,𝒄i)).Y\_{i}\mid\bm{x}\_{i},\bm{c}\_{i},v\_{i}\sim\mathrm{Poisson}\left(v\_{i}\,\lambda(\bm{x}\_{i},\bm{c}\_{i})\right). |  | (2) |

We then try to approximate λ​(⋅)\lambda(\cdot) from a parametrized class of regression functions {Fθ​(⋅)}θ\{F\_{\theta}(\cdot)\}\_{\theta}.
For example, in the classical GLM setting with log-link function, we have the parametrized
class log⁡(Fθ​(𝒙i,𝒄i))=β0+𝒙i⊤​𝜷r+∑jγci​j\log(F\_{\theta}(\bm{x}\_{i},\bm{c}\_{i}))=\beta\_{0}+\bm{x}\_{i}^{\top}\bm{\beta}\_{r}+\sum\_{j}\gamma\_{c\_{ij}}, with intercept β0\beta\_{0}, 𝜷r\bm{\beta}\_{r} are the regression coefficients for the continuous covariates and γci​j\gamma\_{c\_{ij}} are factor-level effects for the categorical covariates (typically implemented by dummy coding), and θ\theta collects all these model parameters. Here, we instead model and learn Fθ​(⋅)F\_{\theta}(\cdot) via a TRM architecture while retaining the Poisson likelihood structure ([2](https://arxiv.org/html/2601.07675v1#S2.E2 "Equation 2 ‣ 2.1 Problem Formulation - Poisson Claims Frequencies ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) with the exposure offset. The TRM outputs estimates Fθ^​(𝒙i,𝒄i)F\_{\widehat{\theta}}(\bm{x}\_{i},\bm{c}\_{i}), and the model is trained by minimizing the Poisson deviance loss, which corresponds to maximum likelihood estimation under the Poisson assumption ([2](https://arxiv.org/html/2601.07675v1#S2.E2 "Equation 2 ‣ 2.1 Problem Formulation - Poisson Claims Frequencies ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")), assuming independence between the
policies i=1,…,ni=1,\ldots,n.

### 2.2 From HRM to TRM to Tab-TRM

The HRM of Wang et al. ([2025](https://arxiv.org/html/2601.07675v1#bib.bib24)) is a recurrent Transformer architecture with two interacting latent states (𝒛L,𝒛H)(\bm{z}\_{L},\bm{z}\_{H}), updated at different effective time scales by two networks fLf\_{L} and fHf\_{H}. Through repeated application of these networks, together with a one-step gradient approximation derived from deep equilibrium models, a HRM achieves very large effective depth with modest parameter count and shows strong performance on algorithmic benchmarks; we also refer to Bai et al. ([2019](https://arxiv.org/html/2601.07675v1#bib.bib2)) for the underlying equilibrium-gradient ideas. Two additional ingredients are important for HRMs. First, *deep supervision* is used: the model is trained over multiple “supervision steps”, with reuse of the latent states (𝒛L,𝒛H)(\bm{z}\_{L},\bm{z}\_{H}) across steps and per-step losses, which effectively emulate a very deep network without long backpropagation-through-time. Second, an *adaptive computational time (ACT)* mechanism is introduced, whereby a Q-learning based halting head decides how many supervision steps to apply to each example, with an extra forward pass used to define the continuation target.

TRMs of Jolicoeur-Martineau ([2025](https://arxiv.org/html/2601.07675v1#bib.bib11)) show that much of HRM’s benefit can be retained, and in fact improved, with a much simpler design. TRMs reinterpret the two HRM latent states as an embedded solution or *answer token* 𝐚\mathbf{a} and an auxiliary *latent reasoning token* 𝒛\bm{z}. A single tiny network is then applied recursively in two roles: repeatedly refining 𝒛\bm{z}, given (𝒙,𝐚,𝒛)(\bm{x},\mathbf{a},\bm{z}), and then updating 𝐚\mathbf{a}, given (𝐚,𝒛)(\mathbf{a},\bm{z}). The recursion is organised into an inner loop of mm latent reasoning updates of 𝒛\bm{z}, an outer loop of TT answer updates of 𝐚\mathbf{a}, and a set of NsupN\_{\text{sup}} repeated passes with deep supervision, in which (𝐚,𝒛)(\mathbf{a},\bm{z}) are carried across passes and detached from the computational graph. TRM abandons the HRM fixed-point gradient approximation and instead backpropagates through a full recursion block. This change substantially improves generalization on the same puzzle benchmarks while still using a single two-layer network with only a few million parameters.

We now introduce Tab-TRM, a specialization of the TRM framework to regression problems on tabular insurance data. Let 𝒙∈ℝpr\bm{x}\in\mathbb{R}^{p\_{r}} and 𝒄∈ℕpc\bm{c}\in\mathbb{N}^{p\_{c}} denote the continuous and categorical covariates for a single policy. Tab-TRM constructs the regression function Fθ​(𝒙,𝒄)F\_{\theta}(\bm{x},\bm{c}) by maintaining two latent vectors per policy: an *answer embedding* 𝐚∈ℝda\mathbf{a}\in\mathbb{R}^{d\_{a}} and a *reasoning embedding* 𝒛∈ℝdz\bm{z}\in\mathbb{R}^{d\_{z}}, both initialized as learned parameters and prepended as prefix tokens to the input sequence. Given an input representation formed by embedding each covariate component into a dd-dimensional space, the full sequence takes the form

|  |  |  |
| --- | --- | --- |
|  | [𝐚,𝒛,𝒆1,…,𝒆L]∈ℝda×ℝdz×ℝd×L,[\mathbf{a},\bm{z},\bm{e}\_{1},\ldots,\bm{e}\_{L}]~\in~\mathbb{R}^{d\_{a}}\times\mathbb{R}^{d\_{z}}\times\mathbb{R}^{d\times L}, |  |

where L=pr+pcL=p\_{r}+p\_{c}, and 𝒆j∈ℝd\bm{e}\_{j}\in\mathbb{R}^{d} represents the dd-dimensional embedding of the jj-th covariate component, for details on embeddings we also refer to
Richman et al. ([2025a](https://arxiv.org/html/2601.07675v1#bib.bib18)).

The Tab-TRM applies a recursive update scheme comprising TT outer iterations of answer refinements, each containing mm inner iterations of reasoning refinements.
Formally, let fzf\_{z} and faf\_{a} denote the reasoning and answer update networks, respectively. We flatten the current sequence to a vector and apply fzf\_{z} to update the reasoning token, then use the refined reasoning token alongside the answer token as input to faf\_{a}. At outer step t≥0t\geq 0 and inner step 0≤s≤m−10\leq s\leq m-1, the updates are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒛(t,s+1)\displaystyle\bm{z}^{(t,s+1)} | =𝒛(t,s)+fz​(Flatten⁡([𝐚(t),𝒛(t,s),𝒆1,…,𝒆L])),\displaystyle=\bm{z}^{(t,s)}+f\_{z}\left(\operatorname{Flatten}\left([\mathbf{a}^{(t)},\bm{z}^{(t,s)},\bm{e}\_{1},\ldots,\bm{e}\_{L}]\right)\right), |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐚(t+1)\displaystyle\mathbf{a}^{(t+1)} | =𝐚(t)+fa​(Concat⁡(𝐚(t),𝒛(t,m))),\displaystyle=\mathbf{a}^{(t)}+f\_{a}\left(\operatorname{Concat}\left(\mathbf{a}^{(t)},\bm{z}^{(t,m)}\right)\right), |  | (4) |

where 𝒛(t,m)\bm{z}^{(t,m)} is the reasoning state after all mm inner iterations, and we initialize the inner loop by 𝒛(t,0)=𝒛(t−1,m)\bm{z}^{(t,0)}=\bm{z}^{(t-1,m)}. Both updates are residual connections. The final answer embedding 𝐚(T)\mathbf{a}^{(T)} is passed through a linear head followed by an exponential activation to produce estimate Fθ​(𝒙,𝒄)∈ℝ>0F\_{\theta}(\bm{x},\bm{c})\in\mathbb{R}\_{>0}, preserving the log-link structure of Poisson GLMs.

Finally, the TRM output Fθ​(𝒙,𝒄)F\_{\theta}(\bm{x},\bm{c}) is multiplied with
the exposure viv\_{i}, and the model is trained by minimizing the Poisson deviance loss. Three architectural departures from the original TRM are noteworthy. First, we employ separate networks fzf\_{z} and faf\_{a} rather than a single shared network, since in the tabular setting the 𝒛\bm{z}-update conditions on all tokens (including the covariates), whereas the 𝐚\mathbf{a}-update conditions only on the current answer and reasoning states (𝐚,𝒛)(\mathbf{a},\bm{z}). Second, we replace the attention-based message passing of TRM with a purely FNN architecture, because policies correspond to short token sequences (typically L≤20L\leq 20), we concatenate all tokens into a single vector and process them through a FNN. Third, we omit both deep supervision and the ACT halting mechanism; the short sequence length and moderate recursion depth (T⋅m≈16T\cdot m\approx 16 to 6464 total steps) permit full gradient flow through the entire unrolled computation without memory or stability issues.

The remainder of this section details the construction of the input sequence, Section [2.3](https://arxiv.org/html/2601.07675v1#S2.SS3 "2.3 Covariate Tokens and Prefix Latent Tokens ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), the recursive core that implements equations ([3](https://arxiv.org/html/2601.07675v1#S2.E3 "Equation 3 ‣ 2.2 From HRM to TRM to Tab-TRM ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"))–([4](https://arxiv.org/html/2601.07675v1#S2.E4 "Equation 4 ‣ 2.2 From HRM to TRM to Tab-TRM ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")), Section [2.4](https://arxiv.org/html/2601.07675v1#S2.SS4 "2.4 Tiny Recursive Reasoning Core ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), and the output head that produces the final prediction, Section [2.5](https://arxiv.org/html/2601.07675v1#S2.SS5 "2.5 Decoder, Poisson Deviance Loss and Metrics ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data").

### 2.3 Covariate Tokens and Prefix Latent Tokens

For each policy i=1,…,ni=1,\ldots,n we assume that the continuous and categorical feature vectors (𝒙i,𝒄i)(\bm{x}\_{i},\bm{c}\_{i}) are transformed into L=pr+pcL=p\_{r}+p\_{c} embeddings

|  |  |  |
| --- | --- | --- |
|  | 𝒆i,1,…,𝒆i,L∈ℝd,\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\in\mathbb{R}^{d}, |  |

using a feature-specific encoding pipeline; for the French MTPL portfolio this pipeline is described in Section [4.2](https://arxiv.org/html/2601.07675v1#S4.SS2 "4.2 Feature Transformations, Embeddings and Tokens ‣ 4 Application: French MTPL Data ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), and for more details we also refer to Richman et al. ([2025a](https://arxiv.org/html/2601.07675v1#bib.bib18)).

Following the Tab-TRM philosophy, we introduce two additional *prefix tokens* representing the current answer and the latent reasoning state. Concretely, we maintain two trainable vectors

|  |  |  |
| --- | --- | --- |
|  | 𝐚(0)∈ℝda,𝒛(0)∈ℝdz,\mathbf{a}^{(0)}\in\mathbb{R}^{d\_{a}},\qquad\bm{z}^{(0)}\in\mathbb{R}^{d\_{z}}, |  |

which are initialized the same across all policies. These are tiled across the entire sample and prepended to the feature tokens, yielding the initial sequence, for policies i=1,…,ni=1,\ldots,n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑺i(0)=[𝐚(0),𝒛(0),𝒆i,1,…,𝒆i,L].\bm{S}\_{i}^{(0)}=\bigl[\,\mathbf{a}^{(0)},\bm{z}^{(0)},\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr]. |  | (5) |

Note that the prefix tokens may have different dimensions dad\_{a} and dzd\_{z} than the feature tokens dd; in our implementation we project all tokens to a common working dimension before flattening. We do not use positional encodings because each token position corresponds to a fixed, named tariff factor (covariate component); the token ordering is fixed and acts as an implicit feature identity. This keeps the architecture as simple as possible: the only structural distinction is between the two prefix tokens and the LL feature tokens.

For clarity, Table [1](https://arxiv.org/html/2601.07675v1#S2.T1 "Table 1 ‣ 2.3 Covariate Tokens and Prefix Latent Tokens ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") summarises the key dimensions used in the French MTPL application in Section [4](https://arxiv.org/html/2601.07675v1#S4 "4 Application: French MTPL Data ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), below.

Table 1: Summary of key dimensions for the French MTPL application.

| Symbol | Description | Example Value |
| --- | --- | --- |
| LL | Number of feature tokens | 9 |
| d=da=dzd=d\_{a}=d\_{z} | Token embedding dimension | 28 |
| L+2L+2 | Total sequence length (incl. 𝐚,𝒛\mathbf{a},\bm{z}) | 11 |
| (L+2)​d(L+2)d | Flattened input dimension to fzf\_{z} | 308 |

### 2.4 Tiny Recursive Reasoning Core

The core of Tab-TRM is a small recursive network that repeatedly refines the latent scratchpad 𝒛\bm{z} and the answer token 𝐚\mathbf{a}, reusing the same parameters at each recursion step. This mirrors the TRM idea of a tiny network that learns an “improvement operator” for (𝐚,𝒛)(\mathbf{a},\bm{z}), rather than a deep stack of separate layers.

Let 𝑺i(t)\bm{S}\_{i}^{(t)} denote the token sequence after t=1,…,Tt=1,\ldots,T *outer* iterations

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑺i(t)=[𝐚i(t),𝒛i(t),𝒆i,1,…,𝒆i,L],\bm{S}\_{i}^{(t)}=\bigl[\,\mathbf{a}\_{i}^{(t)},\bm{z}\_{i}^{(t)},\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr], |  | (6) |

with 𝐚i(t)∈ℝda\mathbf{a}\_{i}^{(t)}\in\mathbb{R}^{d\_{a}} and 𝒛i(t)∈ℝdz\bm{z}\_{i}^{(t)}\in\mathbb{R}^{d\_{z}} being
the first two tokens (answer and latent state). Each outer iteration consists of two stages: an inner recursion that updates 𝒛i(t)\bm{z}\_{i}^{(t)} mm times given the current sequence, and a single answer update that refines 𝐚i(t)\mathbf{a}\_{i}^{(t)}, see ([3](https://arxiv.org/html/2601.07675v1#S2.E3 "Equation 3 ‣ 2.2 From HRM to TRM to Tab-TRM ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"))-([4](https://arxiv.org/html/2601.07675v1#S2.E4 "Equation 4 ‣ 2.2 From HRM to TRM to Tab-TRM ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")). Note that only in the initial token ([5](https://arxiv.org/html/2601.07675v1#S2.E5 "Equation 5 ‣ 2.3 Covariate Tokens and Prefix Latent Tokens ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) the answer and the reasoning token are not instance dependent.

We use two small FNNs for these updates: a network fzf\_{z} for the latent recursion, and a network faf\_{a} for the answer update. The depth of each FNN is a hyper-parameter (0–5 hidden layers) with GELU activation function; in the Optuna-selected configuration that we will present later both FNNs have zero hidden layers, yielding a single affine map followed by a GELU nonlinear activation. All parameters in fzf\_{z} and faf\_{a} are shared across all inner and outer iterations.

#### Stage 1: Latent Recursion on 𝒛\bm{z}

Given 𝑺i(t)\bm{S}\_{i}^{(t)}, we initialise

|  |  |  |
| --- | --- | --- |
|  | 𝑺i(t,0)=𝑺i(t),𝒛i(t,0)=𝒛i(t).\bm{S}\_{i}^{(t,0)}=\bm{S}\_{i}^{(t)},\qquad\bm{z}\_{i}^{(t,0)}=\bm{z}\_{i}^{(t)}. |  |

For s=0,…,m−1s=0,\dots,m-1 we perform a residual update of 𝒛i(t)\bm{z}\_{i}^{(t)}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒖i(t,s)\displaystyle\bm{u}\_{i}^{(t,s)} | =Flatten⁡(𝑺i(t,s))∈ℝda+dz+L​d,\displaystyle=\operatorname{Flatten}\bigl(\bm{S}\_{i}^{(t,s)}\bigr)\in\mathbb{R}^{d\_{a}+d\_{z}+Ld}, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒖~i(t,s)\displaystyle\tilde{\bm{u}}\_{i}^{(t,s)} | =LayerNorm⁡(𝒖i(t,s)),\displaystyle=\operatorname{LayerNorm}\bigl(\bm{u}\_{i}^{(t,s)}\bigr), |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ​𝒛i(t,s+1)\displaystyle\Delta\bm{z}\_{i}^{(t,s+1)} | =fz​(𝒖~i(t,s)),\displaystyle=f\_{z}\bigl(\tilde{\bm{u}}\_{i}^{(t,s)}\bigr), |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒛i(t,s+1)\displaystyle\bm{z}\_{i}^{(t,s+1)} | =𝒛i(t,s)+Δ​𝒛i(t,s+1),\displaystyle=\bm{z}\_{i}^{(t,s)}+\Delta\bm{z}\_{i}^{(t,s+1)}, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑺i(t,s+1)\displaystyle\bm{S}\_{i}^{(t,s+1)} | =𝑺i(t,s)​ with token 1 replaced by ​𝒛i(t,s+1).\displaystyle=\bm{S}\_{i}^{(t,s)}\text{ with token 1 replaced by }\bm{z}\_{i}^{(t,s+1)}. |  | (11) |

After mm inner steps we write 𝒛i(t+1):=𝒛i(t,m)\bm{z}\_{i}^{(t+1)}:=\bm{z}\_{i}^{(t,m)}.
This stage corresponds to the TRM latent recursion, where 𝒛\bm{z} is repeatedly updated from (𝐚,𝒛,𝒙,𝒄)(\mathbf{a},\bm{z},\bm{x},\bm{c}), except that here the “input” (𝒙,𝒄)(\bm{x},\bm{c}) is the short sequence of feature tokens and the update is implemented by a tiny FNN rather than a Transformer block.

#### Stage 2: Answer Update from (𝐚,𝒛)(\mathbf{a},\bm{z})

We next refine the answer token using the updated latent state. We form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑺~i(t)\displaystyle\tilde{\bm{S}}\_{i}^{(t)} | =LayerNorm⁡([𝐚i(t),𝒛i(t+1),𝒆i,1,…,𝒆i,L]),\displaystyle=\operatorname{LayerNorm}\left(\bigl[\,\mathbf{a}\_{i}^{(t)},\bm{z}\_{i}^{(t+1)},\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr]\right), |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐚~i(t)\displaystyle\tilde{\mathbf{a}}\_{i}^{(t)} | =𝑺~i(t)​[0],𝒛~i(t+1)=𝑺~i(t)​[1],\displaystyle=\tilde{\bm{S}}^{(t)}\_{i}[0],\qquad\tilde{\bm{z}}\_{i}^{(t+1)}=\tilde{\bm{S}}^{(t)}\_{i}[1], |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ​𝐚i(t+1)\displaystyle\Delta\mathbf{a}\_{i}^{(t+1)} | =fa​(Concat⁡(𝐚~i(t),𝒛~i(t+1))),\displaystyle=f\_{a}\bigl(\operatorname{Concat}\bigl(\tilde{\mathbf{a}}\_{i}^{(t)},\tilde{\bm{z}}\_{i}^{(t+1)}\bigr)\bigr), |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐚i(t+1)\displaystyle\mathbf{a}\_{i}^{(t+1)} | =𝐚i(t)+Δ​𝐚i(t+1),\displaystyle=\mathbf{a}\_{i}^{(t)}+\Delta\mathbf{a}\_{i}^{(t+1)}, |  | (15) |

where in ([13](https://arxiv.org/html/2601.07675v1#S2.E13 "Equation 13 ‣ Stage 2: Answer Update from (𝐚,𝒛) ‣ 2.4 Tiny Recursive Reasoning Core ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")), we select tokens 0 and 1 of 𝑺~i(t)\tilde{\bm{S}}\_{i}^{(t)} reflecting the answer and the reasoning tokens.
We then assemble the next outer sequence as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑺i(t+1)=[𝐚i(t+1),𝒛i(t+1),𝒆i,1,…,𝒆i,L].\bm{S}\_{i}^{(t+1)}=\bigl[\,\mathbf{a}\_{i}^{(t+1)},\bm{z}\_{i}^{(t+1)},\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr]. |  | (16) |

#### Outer Recursion and Effective Depth

The outer recursion is repeated TT times,

|  |  |  |
| --- | --- | --- |
|  | 𝑺i(0)↦𝑺i(1)↦⋯↦𝑺i(T)=[𝐚i(T),𝒛i(T),𝒆i,1,…,𝒆i,L],\bm{S}\_{i}^{(0)}\;\mapsto\;\bm{S}\_{i}^{(1)}\;\mapsto\;\cdots\;\mapsto\;\bm{S}\_{i}^{(T)}=\bigl[\,\mathbf{a}\_{i}^{(T)},\bm{z}\_{i}^{(T)},\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr], |  |

yielding a final answer token 𝐚i(T)\mathbf{a}\_{i}^{(T)}.

Let nlayersn\_{\text{layers}} denote the number of affine layers inside fzf\_{z} and faf\_{a} (two in our experiments). A single forward pass through Tab-TRM has an effective depth of order

|  |  |  |
| --- | --- | --- |
|  | neff≈nlayers​m​T,n\_{\text{eff}}\approx n\_{\text{layers}}\,m\,T, |  |

even though the number of *distinct* parameters is tiny. For a typical configuration with m=6m=6 and T=3T=3, the effective depth is comparable to a 4040 to 5050 layer FNN, but with far fewer parameters and a much stronger inductive bias: the network is forced to implement a general-purpose “improvement operator” that can be applied repeatedly.

In contrast to HRM and TRM on grid-based puzzles, where deep supervision and ACT are used to manage memory and training cost, we simply backpropagate through all m​TmT latent updates and TT answer updates. This is feasible here because the sequence length L+2L+2 is small and the per-step networks are tiny. Conceptually, our recursion corresponds to one TRM supervision step with all updates unrolled.

### 2.5 Decoder, Poisson Deviance Loss and Metrics

We interpret the final answer tokens 𝐚i(T)\mathbf{a}\_{i}^{(T)} as a compact representation of the policy’s risk profile.
We then select a small FNN fo:ℝda→ℝf\_{o}:\mathbb{R}^{d\_{a}}\to\mathbb{R} to map the answer token to the prediction. Using the exponential output activation, we set for the estimated expected frequency

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fθ​(𝒙i,𝒄i)=exp⁡(fo​(𝐚i(T))),F\_{\theta}(\bm{x}\_{i},\bm{c}\_{i})=\exp\left(f\_{o}(\mathbf{a}^{(T)}\_{i})\right), |  | (17) |

which ensures compatibility with the Poisson GLM form ([2](https://arxiv.org/html/2601.07675v1#S2.E2 "Equation 2 ‣ 2.1 Problem Formulation - Poisson Claims Frequencies ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")). For the network
fof\_{o} we select a FNN of depth 2 and GELU activations; for a detailed exposition of FNN we refer to Chapter 5 of Wüthrich et al. ([2025](https://arxiv.org/html/2601.07675v1#bib.bib27)).

This gives us a parametrized class {Fθ}θ\{F\_{\theta}\}\_{\theta} of regression functions, where the parameter θ\theta collects all the token embedding parameters of 𝒙\bm{x} and 𝒄\bm{c} and the network parameters of the three networks fzf\_{z}, faf\_{a} and fof\_{o}. We train these weights by maximizing the Poisson log-likelihood which is equivalent to minimizing the Poisson deviance loss, see Chapter 2 of Wüthrich et al. ([2025](https://arxiv.org/html/2601.07675v1#bib.bib27)).
The Poisson deviance loss is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ;𝒟)=2|𝒟|​∑i∈𝒟[vi​Fθ​(𝒙i,𝒄i)−yi−yi​log⁡(vi​Fθ​(𝒙i,𝒄i)yi)],{\cal L}(\theta;\mathcal{D})=\frac{2}{|\mathcal{D}|}\sum\_{i\in\mathcal{D}}\left[v\_{i}F\_{\theta}(\bm{x}\_{i},\bm{c}\_{i})-y\_{i}-y\_{i}\log\left(\frac{v\_{i}F\_{\theta}(\bm{x}\_{i},\bm{c}\_{i})}{y\_{i}}\right)\right], |  | (18) |

we refer to Table 2.2 in Wüthrich et al. ([2025](https://arxiv.org/html/2601.07675v1#bib.bib27)). We use this Poisson deviance loss ([18](https://arxiv.org/html/2601.07675v1#S2.E18 "Equation 18 ‣ 2.5 Decoder, Poisson Deviance Loss and Metrics ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) to train the model on a training sample 𝒟train\mathcal{D}\_{\rm train} to determine θ^\widehat{\theta}, and it is used for model validation on an independent hold-out test sample 𝒟test\mathcal{D}\_{\rm test}.

### 2.6 Optimization and Hyper-parameter Search

We implement Tab-TRM in Keras and train it with the AdamW optimizer (decoupled weight decay), with learning rate, weight decay, Adam β2\beta\_{2}, and dropout rates treated as hyper-parameters. Mild ℓ1\ell\_{1}–ℓ2\ell\_{2} penalties are applied to the continuous encoding weights and categorical embeddings; when searching through the hyper-parameters we found that setting the value of the ℓ1\ell\_{1} and ℓ2\ell\_{2} penalties to the same value yielded the best results. Training is performed with mini-batches of size 4,0964{,}096, a 10% validation split, early stopping on validation loss, and we reduce the learning rate by a factor of 0.50.5 when the validation loss does not improve for 55 epochs.

The architecture is controlled by a small set of interpretable hyper-parameters. These include the embedding dimension dd (shared across all tokens, typically not exceeding 60); the inner recursion depth mm and the number of outer iterations TT; the numbers and widths of hidden layers in fzf\_{z}, faf\_{a} and fof\_{o}, dropout rates and regularization strengths; and the AdamW learning rate and β2\beta\_{2} parameter. We performed global hyper-parameter optimization with Optuna (Akiba et al., [2019](https://arxiv.org/html/2601.07675v1#bib.bib1)). For each trial we sample a configuration within pre-specified bounds, instantiate Tab-TRM with this configuration, train on 𝒟train\mathcal{D}\_{\mathrm{train}} with early stopping on a 10% validation subset, reload the best checkpoint (as measured by the validation loss), and report the *validation* Poisson deviance loss as the trial objective. After selecting the hyper-parameters, we evaluate the final model on the hold-out test sample and report the test Poisson deviance loss once. The search space and bounds are summarized in Appendix [B](https://arxiv.org/html/2601.07675v1#A2 "Appendix B Hyper-parameter Search Space ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data").

## 3 Interpreting Tab-TRM

The recursive structure of Tab-TRM admits several complementary interpretations that connect to well-established modeling frameworks. In this section we first show that Tab-TRM can be viewed as a discrete-time state-space model, Section [3.1](https://arxiv.org/html/2601.07675v1#S3.SS1 "3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), and secondly draw a connection to gradient boosting through a stagewise-additive lens, Section [3.2](https://arxiv.org/html/2601.07675v1#S3.SS2 "3.2 A Stagewise-Additive View: Tab-TRM as Recurrent Boosting ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"). These perspectives provide insight into the model’s behavior and facilitate comparison with classical actuarial and machine learning methods.

### 3.1 Connection to State-Space Models

Tab-TRM can be viewed as a deterministic state-space system evolving in a learned latent space. For a fixed policy, the feature tokens 𝒆1,…,𝒆L\bm{e}\_{1},\dots,\bm{e}\_{L} are constant, so the recursion acts only on the latent state (𝐚,𝒛)(\mathbf{a},\bm{z}). It is therefore natural to define the state

|  |  |  |
| --- | --- | --- |
|  | 𝒔(t)=(𝐚(t)𝒛(t))∈ℝda+dz,\bm{s}^{(t)}\;=\;\begin{pmatrix}\mathbf{a}^{(t)}\\ \bm{z}^{(t)}\end{pmatrix}\in\mathbb{R}^{d\_{a}+d\_{z}}, |  |

and to interpret each outer recursion step as a discrete “time” index. The inner loop updates 𝒛(t)\bm{z}^{(t)} mm times using the current answer token and the fixed features, yielding 𝒛(t+1)\bm{z}^{(t+1)}, and then the outer update refines 𝐚(t)\mathbf{a}^{(t)}. This defines a deterministic nonlinear transition map of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒔(t+1)=ℱθ​(𝒔(t);𝒆1,…,𝒆L),\bm{s}^{(t+1)}\;=\;\mathcal{F}\_{\theta}\left(\bm{s}^{(t)};\bm{e}\_{1},\dots,\bm{e}\_{L}\right), |  | (19) |

where ℱθ\mathcal{F}\_{\theta} is the composition of the mm inner updates of fzf\_{z} and the single outer update of faf\_{a}, see ([3](https://arxiv.org/html/2601.07675v1#S2.E3 "Equation 3 ‣ 2.2 From HRM to TRM to Tab-TRM ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"))-([4](https://arxiv.org/html/2601.07675v1#S2.E4 "Equation 4 ‣ 2.2 From HRM to TRM to Tab-TRM ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")). The observation equation is the decoder applied to the answer token,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fθ(t)​(𝒙i,𝒄i)=exp⁡(fo​(𝐚i(t))),{F}\_{\theta}^{(t)}(\bm{x}\_{i},\bm{c}\_{i})=\exp\left(f\_{o}(\mathbf{a}\_{i}^{(t)})\right), |  | (20) |

with fo​(⋅)f\_{o}(\cdot) being the decoder FNN, see ([17](https://arxiv.org/html/2601.07675v1#S2.E17 "Equation 17 ‣ 2.5 Decoder, Poisson Deviance Loss and Metrics ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")). Thus, the full Tab-TRM is a nonlinear state-space model in a learned basis, with constant inputs given by the embedded covariates.

##### From nonlinear to linear recursion.

In the full Tab-TRM, the update maps fzf\_{z} and faf\_{a} are small FNNs with nonlinear activations (GELU in our implementation). For example, a two-layer update has the form

|  |  |  |
| --- | --- | --- |
|  | fz​(𝐮)=𝑾z(2)​ϕ​(𝑾z(1)​𝐮+𝒃z(1))+𝒃z(2),fa​(𝐯)=𝑾a(2)​ϕ​(𝑾a(1)​𝐯+𝒃a(1))+𝒃a(2),f\_{z}(\mathbf{u})=\bm{W}^{(2)}\_{z}\,\phi\left(\bm{W}^{(1)}\_{z}\mathbf{u}+\bm{b}^{(1)}\_{z}\right)+\bm{b}^{(2)}\_{z},\quad f\_{a}(\mathbf{v})=\bm{W}^{(2)}\_{a}\,\phi\left(\bm{W}^{(1)}\_{a}\mathbf{v}+\bm{b}^{(1)}\_{a}\right)+\bm{b}^{(2)}\_{a}, |  |

so the transition ℱθ\mathcal{F}\_{\theta} is nonlinear because of the nonlinearity of ϕ​(⋅)\phi(\cdot). The linear modification is obtained by *removing the activations* (i.e., setting ϕ\phi to the identity) and, equivalently, using zero hidden layers (a single affine map) for both fzf\_{z} and faf\_{a}. In that case

|  |  |  |
| --- | --- | --- |
|  | fz​(𝐮)=𝑾z​𝐮+𝒃z,fa​(𝐯)=𝑾a​𝐯+𝒃a,f\_{z}(\mathbf{u})=\bm{W}\_{z}\mathbf{u}+\bm{b}\_{z},\qquad f\_{a}(\mathbf{v})=\bm{W}\_{a}\mathbf{v}+\bm{b}\_{a}, |  |

so the recursion becomes exactly linear in (𝐚,𝒛)(\mathbf{a},\bm{z}) and in the feature tokens. With residual connections this remains a linear update, and if LayerNorm is disabled the state transition is strictly linear. If LayerNorm is retained, the dynamics are a linear map followed by normalization (piecewise-linear), so the state-space form remains a close local approximation. The observation equation remains the same exponential decoder, so the overall model is linear in state evolution with a GLM-style nonlinear readout.

##### Linear reformulation (exact state-space form).

Let 𝒆¯=1L​∑ℓ=1L𝒆ℓ\bar{\bm{e}}=\frac{1}{L}\sum\_{\ell=1}^{L}\bm{e}\_{\ell} denote the mean feature token. For expositional clarity, we present the linear reformulation using this averaged representation; the actual implementation uses the full concatenated vector [𝒆1,…,𝒆L][\bm{e}\_{1},\ldots,\bm{e}\_{L}] with position-specific weight blocks, which is equivalent to the mean-token form under tied weights across positions. We write the linear updates as

|  |  |  |
| --- | --- | --- |
|  | Δ​𝒛=𝑾z​z​𝒛+𝑾a​z​𝐚+𝑾f​𝒆¯+𝒃z,Δ​𝐚=𝑾a​a​𝐚+𝑾z​a​𝒛+𝒃a,\Delta\bm{z}=\bm{W}\_{zz}\bm{z}+\bm{W}\_{az}\mathbf{a}+\bm{W}\_{f}\bar{\bm{e}}+\bm{b}\_{z},\qquad\Delta\mathbf{a}=\bm{W}\_{aa}\mathbf{a}+\bm{W}\_{za}\bm{z}+\bm{b}\_{a}, |  |

with residual connections. Define 𝑨z=𝑰+𝑾z​z\bm{A}\_{z}=\bm{I}+\bm{W}\_{zz} and the inner-loop sum

|  |  |  |
| --- | --- | --- |
|  | 𝑺sum=∑k=0m−1𝑨zk.\bm{S}\_{\mathrm{sum}}=\sum\_{k=0}^{m-1}\bm{A}\_{z}^{k}. |  |

After mm inner updates, the reasoning state is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒛(t+1)=𝑨zm​𝒛(t)+𝑺sum​(𝑾a​z​𝐚(t)+𝑾f​𝒆¯+𝒃z).\bm{z}^{(t+1)}=\bm{A}\_{z}^{m}\bm{z}^{(t)}+\bm{S}\_{\mathrm{sum}}\bigl(\bm{W}\_{az}\mathbf{a}^{(t)}+\bm{W}\_{f}\bar{\bm{e}}+\bm{b}\_{z}\bigr). |  | (21) |

The outer update gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐚(t+1)=(𝑰+𝑾a​a)​𝐚(t)+𝑾z​a​𝒛(t+1)+𝒃a.\mathbf{a}^{(t+1)}=\bigl(\bm{I}+\bm{W}\_{aa}\bigr)\mathbf{a}^{(t)}+\bm{W}\_{za}\bm{z}^{(t+1)}+\bm{b}\_{a}. |  | (22) |

Stacking these yields an exact linear state-space system

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒔(t+1)=𝑨​𝒔(t)+𝑩​𝒆¯+𝒄,\bm{s}^{(t+1)}=\bm{A}\,\bm{s}^{(t)}+\bm{B}\,\bar{\bm{e}}+\bm{c}, |  | (23) |

with block matrices

|  |  |  |
| --- | --- | --- |
|  | 𝑨=[𝑰+𝑾a​a+𝑾z​a​𝑺sum​𝑾a​z𝑾z​a​𝑨zm𝑺sum​𝑾a​z𝑨zm],𝑩=[𝑾z​a​𝑺sum​𝑾f𝑺sum​𝑾f],𝒄=[𝒃a+𝑾z​a​𝑺sum​𝒃z𝑺sum​𝒃z].\bm{A}=\begin{bmatrix}\bm{I}+\bm{W}\_{aa}+\bm{W}\_{za}\bm{S}\_{\mathrm{sum}}\bm{W}\_{az}&\bm{W}\_{za}\bm{A}\_{z}^{m}\\[1.99997pt] \bm{S}\_{\mathrm{sum}}\bm{W}\_{az}&\bm{A}\_{z}^{m}\end{bmatrix},~\bm{B}=\begin{bmatrix}\bm{W}\_{za}\bm{S}\_{\mathrm{sum}}\bm{W}\_{f}\\[1.99997pt] \bm{S}\_{\mathrm{sum}}\bm{W}\_{f}\end{bmatrix},~\bm{c}=\begin{bmatrix}\bm{b}\_{a}+\bm{W}\_{za}\bm{S}\_{\mathrm{sum}}\bm{b}\_{z}\\[1.99997pt] \bm{S}\_{\mathrm{sum}}\bm{b}\_{z}\end{bmatrix}. |  |

Equation ([23](https://arxiv.org/html/2601.07675v1#S3.E23 "Equation 23 ‣ Linear reformulation (exact state-space form). ‣ 3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) is an exact deterministic linear state-space model with constant input 𝒆¯\bar{\bm{e}}, followed by the same decoder as in the nonlinear case. We will come back to this in Section [6.1](https://arxiv.org/html/2601.07675v1#S6.SS1 "6.1 Linear Update Architecture ‣ 6 Linearized Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), below.

### 3.2 A Stagewise-Additive View: Tab-TRM as Recurrent Boosting

Gradient boosting (Friedman, [2001](https://arxiv.org/html/2601.07675v1#bib.bib7)) constructs an additive predictor of the form

|  |  |  |
| --- | --- | --- |
|  | FM​(x)=F0​(x)+∑m=1Mνm​hm​(x),F\_{M}(x)=F\_{0}(x)+\sum\_{m=1}^{M}\nu\_{m}h\_{m}(x), |  |

where each weak learner hmh\_{m} is fitted to (pseudo-)residuals under the current model and νm\nu\_{m} is a shrinkage coefficient.
Tab-TRM admits a closely related *stagewise correction* interpretation. Let

|  |  |  |
| --- | --- | --- |
|  | ηi(t)=fo​(𝐚i(t))=log⁡Fθ(t)​(𝒙i,𝒄i)\eta\_{i}^{(t)}=f\_{o}\left(\mathbf{a}\_{i}^{(t)}\right)=\log F^{(t)}\_{\theta}(\bm{x}\_{i},\bm{c}\_{i}) |  |

denote the model’s log-prediction at outer iteration tt, where fo:ℝda→ℝf\_{o}:\mathbb{R}^{d\_{a}}\to\mathbb{R} is the decoder mapping the answer token to a scalar. The outer recursion updates 𝐚\mathbf{a} via residual increments:

|  |  |  |
| --- | --- | --- |
|  | 𝐚i(t+1)=𝐚i(t)+fa​(Concat⁡(𝐚~i(t),𝒛~i(t+1))).\mathbf{a}\_{i}^{(t+1)}=\mathbf{a}\_{i}^{(t)}+f\_{a}\left(\operatorname{Concat}\left(\tilde{\mathbf{a}}\_{i}^{(t)},\tilde{\bm{z}}\_{i}^{(t+1)}\right)\right). |  |

If fof\_{o} is linear (or locally linear), then η(t)\eta^{(t)} evolves approximately additively:

|  |  |  |
| --- | --- | --- |
|  | ηi(t+1)≈ηi(t)+⟨∇fo​(𝐚i(t)),fa​(Concat⁡(𝐚~i(t),𝒛~i(t+1)))⟩⏟=Δ​ηi(t),\eta\_{i}^{(t+1)}\approx\eta\_{i}^{(t)}+\underbrace{\left\langle\nabla f\_{o}(\mathbf{a}\_{i}^{(t)}),\,f\_{a}\left(\operatorname{Concat}\left(\tilde{\mathbf{a}}\_{i}^{(t)},\tilde{\bm{z}}\_{i}^{(t+1)}\right)\right)\right\rangle}\_{=\Delta\eta\_{i}^{(t)}}, |  |

so that after TT outer steps the log-prediction decomposes as

|  |  |  |
| --- | --- | --- |
|  | ηi(T)≈ηi(0)+∑t=0T−1Δ​ηi(t).\eta\_{i}^{(T)}\approx\eta\_{i}^{(0)}+\sum\_{t=0}^{T-1}\Delta\eta\_{i}^{(t)}. |  |

This structure resembles boosting in that the predictor is refined by repeated additive corrections. However, there is a key architectural difference: whereas standard gradient boosting fits a *new* weak learner at each stage, Tab-TRM reuses the *same* small networks fzf\_{z} and faf\_{a} across all refinement steps. Computational depth therefore increases without introducing additional parameter sets, yielding a form of *recurrent boosting* where the correction operator is learned once and applied repeatedly.

## 4 Application: French MTPL Data

We now demonstrate Tab-TRM on the benchmark French MTPL data of Dutang et al. ([2024](https://arxiv.org/html/2601.07675v1#bib.bib6)); we use the cleaned data of Wüthrich and Merz ([2023](https://arxiv.org/html/2601.07675v1#bib.bib26)). The goal is to model the claim frequency using the methodology of Section [2](https://arxiv.org/html/2601.07675v1#S2 "2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), together with an insurance-specific feature encoding pipeline.

### 4.1 Data and Baseline Formulation

Each observation corresponds to a single exposure period and contains several components. The response variable Yi∈{0,1,2,…}Y\_{i}\in\{0,1,2,\dots\} records the number of reported claims, while vi>0v\_{i}>0 denotes the exposure. The available covariates are split into two groups: a vector 𝒙i=(xi,1,…,xi,pr)\bm{x}\_{i}=(x\_{i,1},\dots,x\_{i,p\_{r}}) of pr=5p\_{r}=5 continuous tariff variables and a vector 𝒄i=(ci,1,…,ci,pc)\bm{c}\_{i}=(c\_{i,1},\dots,c\_{i,p\_{c}}) of pc=4p\_{c}=4 categorical tariff variables. In addition, a split indicator assigns each observation either to a training set or to a test set. We focus on the claim counts variable and calibrate a Poisson model

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi∣𝒙i,𝒄i,vi∼Poisson​(μi), with mean ​μi=vi​Fθ​(𝒄i,𝒙i).Y\_{i}\mid\bm{x}\_{i},\bm{c}\_{i},v\_{i}\sim\mathrm{Poisson}(\mu\_{i}),\qquad\text{ with mean }\mu\_{i}=v\_{i}F\_{\theta}(\bm{c}\_{i},\bm{x}\_{i}). |  | (24) |

As a simple reference we consider the null Poisson baseline on the training set, not considering any covariates, having empirical expected frequency estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^null=∑i∈𝒟trainYi∑i∈𝒟trainvi,\widehat{\lambda}\_{\mathrm{null}}=\frac{\sum\_{i\in\mathcal{D}\_{\mathrm{train}}}Y\_{i}}{\sum\_{i\in\mathcal{D}\_{\mathrm{train}}}v\_{i}}, |  | (25) |

which coincides with the intercept-only model of a Poisson GLM with log⁡vi\log v\_{i} as offset.

### 4.2 Feature Transformations, Embeddings and Tokens

For the French MTPL dataset we make the encoding pipeline of Section [2.3](https://arxiv.org/html/2601.07675v1#S2.SS3 "2.3 Covariate Tokens and Prefix Latent Tokens ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") concrete. The aim is to construct L=pr+pc=9L=p\_{r}+p\_{c}=9 feature tokens per policy, each living in ℝd\mathbb{R}^{d}, that serve as the Tab-TRM input sequence.

#### Continuous tariff variables

For each continuous component (xi,j)j=1pr(x\_{i,j})\_{j=1}^{p\_{r}} we first apply a robust, smooth clipping transformation, following the quantile-based preprocessing of Holzmüller et al. ([2024](https://arxiv.org/html/2601.07675v1#bib.bib10)). On the training set we compute empirical quantiles

|  |  |  |  |
| --- | --- | --- | --- |
|  | qj,0<qj,1<qj,2<qj,3<qj,4,q\_{j,0}<q\_{j,1}<q\_{j,2}<q\_{j,3}<q\_{j,4}, |  | (26) |

corresponding to the 0th, 25th, 50th, 75th and 100th percentiles of {xi,j:i∈𝒟train}\{x\_{i,j}:i\in\mathcal{D}\_{\mathrm{train}}\}. A positive scale sjs\_{j} is derived from the spread of the distribution (we use an inter-quantile range based on ([26](https://arxiv.org/html/2601.07675v1#S4.E26 "Equation 26 ‣ Continuous tariff variables ‣ 4.2 Feature Transformations, Embeddings and Tokens ‣ 4 Application: French MTPL Data ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")), with safeguards against degeneracies), and we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi,j=sj​(xi,j−qj,2),x~i,j=zi,j1+(zi,j/3)2.z\_{i,j}=s\_{j}\bigl(x\_{i,j}-q\_{j,2}\bigr),\qquad\tilde{x}\_{i,j}=\frac{z\_{i,j}}{\sqrt{1+(z\_{i,j}/3)^{2}}}. |  | (27) |

Near the median qj,2q\_{j,2} this transform is approximately linear, while for large positive or negative deviations it saturates smoothly towards values in (−3,3)(-3,3), limiting the influence of outliers while preserving rank information. The identical (qj,2,sj)(q\_{j,2},s\_{j}) statistics are reused at prediction time.

To allow nonlinear effects of continuous factors while keeping the model low-capacity, we apply a learnable piecewise-linear encoding (PLE), inspired by Gorishniy et al. ([2022](https://arxiv.org/html/2601.07675v1#bib.bib8)) and adapted to actuarial data following Richman et al. ([2025a](https://arxiv.org/html/2601.07675v1#bib.bib18)). For each normalized feature x~i,j\tilde{x}\_{i,j} we compute, on the pooled train normalized data, a grid of empirical deciles

|  |  |  |
| --- | --- | --- |
|  | dj,0<dj,1<…<dj,K,K=10,d\_{j,0}<d\_{j,1}<\ldots<d\_{j,K},\qquad K=10, |  |

and initialize a custom Keras layer that maintains log bin-widths whose exponentials yield positive widths, accumulates these widths (plus a trainable start value) to form a monotone set of bin boundaries bj,0,…,bj,Kb\_{j,0},\dots,b\_{j,K} and maps x~i,j\tilde{x}\_{i,j} to a (K+1)(K+1)-dimensional vector ψj​(x~i,j)\psi\_{j}(\tilde{x}\_{i,j}) of piecewise-linear basis functions that are localized between these boundaries. We then obtain a dd-dimensional continuous embedding via

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐬i,j=ψj​(x~i,j)∈ℝK+1,𝒆i,jcont=Φ​(𝑾jcont​𝐬i,j+𝐛jcont)∈ℝd,\mathbf{s}\_{i,j}=\psi\_{j}(\tilde{x}\_{i,j})\in\mathbb{R}^{K+1},\qquad\bm{e}\_{i,j}^{\mathrm{cont}}=\Phi\left(\bm{W}\_{j}^{\mathrm{cont}}\mathbf{s}\_{i,j}+\mathbf{b}\_{j}^{\mathrm{cont}}\right)\in\mathbb{R}^{d}, |  | (28) |

with 𝑾jcont\bm{W}\_{j}^{\mathrm{cont}} and 𝐛jcont\mathbf{b}\_{j}^{\mathrm{cont}} trainable and Φ\Phi a GELU activation. Mild ℓ1\ell\_{1}–ℓ2\ell\_{2} penalties are applied to these weights. From an actuarial point of view, this acts as a learned rating curve for each continuous rating factor, initialized at decile-based knots and allowed to adapt during training.

#### Categorical rating factors

Each categorical rating factor (ci,j)j=1pc(c\_{i,j})\_{j=1}^{p\_{c}} takes values in a finite set {0,…,Mj}\{0,\dots,M\_{j}\} after label encoding. We associate an embedding matrix 𝐄jcat∈ℝ(Mj+1)×d\mathbf{E}\_{j}^{\mathrm{cat}}\in\mathbb{R}^{(M\_{j}+1)\times d} and map

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒆i,jcat=𝐄jcat​[ci,j]∈ℝd,\bm{e}\_{i,j}^{\mathrm{cat}}=\mathbf{E}\_{j}^{\mathrm{cat}}[c\_{i,j}]\in\mathbb{R}^{d}, |  | (29) |

corresponding to level ci,jc\_{i,j} taken by policy ii, i.e.,
𝒆i,jcat\bm{e}\_{i,j}^{\mathrm{cat}} is the (ci,j+1)(c\_{i,j}+1)-st row of 𝐄jcat\mathbf{E}\_{j}^{\mathrm{cat}}.
We apply light ℓ1\ell\_{1}–ℓ2\ell\_{2} regularization to encourage shrinkage of rarely used levels.

#### Token representation for Tab-TRM

For each policy i=1,…,ni=1,\ldots,n we now have pr=5p\_{r}=5 continuous embeddings 𝒆i,1cont,…,𝒆i,prcont\bm{e}\_{i,1}^{\mathrm{cont}},\dots,\bm{e}\_{i,p\_{r}}^{\mathrm{cont}} and pc=4p\_{c}=4 categorical embeddings 𝒆i,1cat,…,𝒆i,pccat\bm{e}\_{i,1}^{\mathrm{cat}},\dots,\bm{e}\_{i,p\_{c}}^{\mathrm{cat}}. We stack them into L=9L=9 feature tokens

|  |  |  |
| --- | --- | --- |
|  | [𝒆i,1,…,𝒆i,L]⊤=[𝒆i,1cont,…,𝒆i,prcont,𝒆i,1cat,…,𝒆i,pccat]⊤∈ℝL×d.\bigl[\,\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr]^{\top}=\bigl[\,\bm{e}\_{i,1}^{\mathrm{cont}},\dots,\bm{e}\_{i,p\_{r}}^{\mathrm{cont}},\bm{e}\_{i,1}^{\mathrm{cat}},\dots,\bm{e}\_{i,p\_{c}}^{\mathrm{cat}}\,\bigr]^{\top}\in\mathbb{R}^{L\times d}. |  |

These tokens are fed into Tab-TRM by prepending the learned answer and latent tokens as in ([5](https://arxiv.org/html/2601.07675v1#S2.E5 "Equation 5 ‣ 2.3 Covariate Tokens and Prefix Latent Tokens ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) and ([6](https://arxiv.org/html/2601.07675v1#S2.E6 "Equation 6 ‣ 2.4 Tiny Recursive Reasoning Core ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) for t≥1t\geq 1,

|  |  |  |
| --- | --- | --- |
|  | 𝑺i(0)=[𝐚(0),𝒛(0),𝒆i,1,…,𝒆i,L] and 𝑺i(t)=[𝐚i(t),𝒛i(t),𝒆i,1,…,𝒆i,L],\bm{S}\_{i}^{(0)}=\bigl[\,\mathbf{a}^{(0)},\bm{z}^{(0)},\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr]\qquad\text{ and }\qquad\bm{S}\_{i}^{(t)}=\bigl[\,\mathbf{a}\_{i}^{(t)},\bm{z}\_{i}^{(t)},\bm{e}\_{i,1},\dots,\bm{e}\_{i,L}\,\bigr], |  |

by applying the recursive core of Section [2.4](https://arxiv.org/html/2601.07675v1#S2.SS4 "2.4 Tiny Recursive Reasoning Core ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"). No positional encodings are used; the organisation follows the actuarial separation between tariff factors and the global latent states (𝐚,𝒛)(\mathbf{a},\bm{z}).

### 4.3 Training Setup and Evaluation on the French MTPL Portfolio

We train Tab-TRM on the French MTPL data, using the same training-test partition as in Wüthrich et al. ([2025](https://arxiv.org/html/2601.07675v1#bib.bib27)). We use the Poisson deviance loss ([18](https://arxiv.org/html/2601.07675v1#S2.E18 "Equation 18 ‣ 2.5 Decoder, Poisson Deviance Loss and Metrics ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")), with the optimization and hyper-parameter search set-up as described in Section [2.6](https://arxiv.org/html/2601.07675v1#S2.SS6 "2.6 Optimization and Hyper-parameter Search ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"). For each Optuna trial we sample a candidate set of architectural and optimization hyper-parameters (embedding dimension dd, recursion depths mm and TT, widths and depths of fzf\_{z} and faf\_{a}, dropout rates, regularization strengths, AdamW parameters), train the model with early stopping on a 10% validation subset of the training data, reload the best checkpoint and compute the Poisson deviance loss ([18](https://arxiv.org/html/2601.07675v1#S2.E18 "Equation 18 ‣ 2.5 Decoder, Poisson Deviance Loss and Metrics ‣ 2 Methodology ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) on the hold-out test set. Since we use the identical training-test split as in many other studies, the out-of-sample Poisson deviance losses are directly comparable.

## 5 Results

### 5.1 Hyper-parameter Selection and Model Performance

Hyper-parameters are selected via Optuna, using the validation Poisson deviance loss as the objective. We conducted the search in two stages. First, a broad search over the full hyper-parameter space (see Table [4](https://arxiv.org/html/2601.07675v1#A2.T4 "Table 4 ‣ Appendix B Hyper-parameter Search Space ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) revealed that the best validation scores were consistently achieved with *single-layer* networks for both fzf\_{z} and faf\_{a} - that is, zero hidden layers in each update function. A second, focused Optuna run restricted to single-layer configurations then identified the final architecture, reported in Table [2](https://arxiv.org/html/2601.07675v1#S5.T2 "Table 2 ‣ 5.1 Hyper-parameter Selection and Model Performance ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"). To reduce variance, we train a 10-run nagging ensemble (Richman and Wüthrich, [2022](https://arxiv.org/html/2601.07675v1#bib.bib20)) - averaging predictions across independently initialised runs - which improves test deviance from 23.630×10−223.630\times 10^{-2} (single run) to 23.589×10−223.589\times 10^{-2}, with mean per-run deviance 23.666×10−223.666\times 10^{-2}.

This finding is noteworthy: Tab-TRM achieves competitive performance using zero-hidden-layer networks for fzf\_{z} and faf\_{a}, that is, a single affine projection followed by a GELU activation. Even these minimal nonlinear operators, when composed recursively m×Tm\times T times through the Tab-TRM core, are sufficient to learn complex risk structures. This supports the TRM philosophy that computational depth through parameter reuse can substitute for model width and architectural complexity.

Table 2: Optuna-selected hyper-parameters (best validation deviance).

|  |  |
| --- | --- |
| Hyper-parameter | Value |
| Embedding dimension d=da=dzd=d\_{a}=d\_{z} | 28 |
| Outer steps TT | 6 |
| Inner iterations mm | 3 |
| Output FNN layer 1 hidden units | 19 |
| Output FNN layer 2 hidden units | 124 |
| Dropout (FNN1) | 0.2821 |
| Dropout (FNN2) | 0.4991 |
| ℓ1\ell\_{1}–ℓ2\ell\_{2} regularization | 2.2539×10−52.2539\times 10^{-5} |
| Learning rate | 0.0021755 |
| Weight decay | 0.0239601 |
| Adam β2\beta\_{2} | 0.9594 |

We compare the Tab-TRM results against a range of benchmark models from the actuarial deep learning literature. Table [3](https://arxiv.org/html/2601.07675v1#S5.T3 "Table 3 ‣ 5.1 Hyper-parameter Selection and Model Performance ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") reports in-sample and out-of-sample Poisson deviance losses (in units of 10−210^{-2}) for classical models, FNNs, and recent transformer-based architectures. Benchmark results are taken from Wüthrich and Merz ([2023](https://arxiv.org/html/2601.07675v1#bib.bib26)), Brauer ([2024](https://arxiv.org/html/2601.07675v1#bib.bib3)) and Richman et al. ([2025a](https://arxiv.org/html/2601.07675v1#bib.bib18), [b](https://arxiv.org/html/2601.07675v1#bib.bib19)).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | # | In-sample | | Out-of-sample | |
| Model | Param. | Poisson loss | | Poisson loss | |
| Null model (intercept-only) | 1 | 25.213 |  | 25.445 |  |
| Poisson GLM3 | 50 | 24.084 |  | 24.102 |  |
| Poisson GAM | (66.7) | 23.920 |  | 23.956 |  |
| Plain-vanilla FNN | 792 | 23.728 | (±\pm 0.026) | 23.819 | (±\pm 0.017) |
| Ensemble plain-vanilla FNN | 792 | 23.691 |  | 23.783 |  |
| CAFFT | 27,133 | 23.715 | (±\pm 0.047) | 23.807 | (±\pm 0.017) |
| Ensemble CAFFT | 27,133 | 23.630 |  | 23.726 |  |
| Credibility Transformer | 1,746 | 23.641 | (±\pm 0.053) | 23.788 | (±\pm 0.040) |
| Ensemble Credibility Transformer | 1,746 | 23.562 |  | 23.711 |  |
| Tree-like PIN | 4,147 | 23.593 | (±\pm 0.046) | 23.740 | (±\pm 0.025) |
| Ensemble Tree-like PIN | 4,147 | 23.522 |  | 23.667 |  |
| Tab-TRM | 14,820 | 23.570 | (±\pm 0.027) | 23.666 | (±\pm 0.027) |
| Ensemble Tab-TRM | 14,820 | 23.496 |  | 23.589 |  |

Table 3: Number of parameters, in-sample and out-of-sample Poisson deviance losses (units are in 10−210^{-2}). Benchmark models are taken from Wüthrich and Merz ([2023](https://arxiv.org/html/2601.07675v1#bib.bib26)), Brauer ([2024](https://arxiv.org/html/2601.07675v1#bib.bib3)), Richman et al. ([2025a](https://arxiv.org/html/2601.07675v1#bib.bib18), [b](https://arxiv.org/html/2601.07675v1#bib.bib19)). Tab-TRM results are for the Optuna-selected configurations.

Tab-TRM achieves an out-of-sample Poisson deviance loss of 23.630×10−223.630\times 10^{-2} (single run) and 23.589×10−223.589\times 10^{-2} (nagging ensemble), which is competitive with the best network architectures in the table. Tab-TRM uses 14,820 trainable parameters, about 45% fewer than CAFFT (27,133) and within an order of magnitude of other compact tabular architectures such as the Tree-like PIN (4,147) and Credibility Transformer (1,746). The architecture trades model size for computational depth through parameter reuse across recursion steps.

### 5.2 Interpretability Analysis

To understand how Tab-TRM refines its predictions, we analyze the learned representations and recursive dynamics on a random subset of 512 test policies. For each policy we extract the initial token sequence from the trained encoder, run the recursive layer for T=6T=6 outer steps with m=3m=3 inner iterations, and record the answer token 𝐚\mathbf{a} and reasoning token 𝒛\bm{z} after each outer step. Per-step predictions are computed by passing the current 𝐚\mathbf{a} token and exposure through the decoder.

#### Token dynamics and convergence

Figure [1](https://arxiv.org/html/2601.07675v1#S5.F1 "Figure 1 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") reports the evolution of token magnitudes and predictions across outer steps. The left panel shows the mean ℓ2\ell\_{2} norm of 𝐚\mathbf{a} and 𝒛\bm{z} with ±1\pm 1 standard deviation bands; the right panel displays the distribution of per-step predictions (median, interquartile range, and mean). Both token magnitudes and prediction distributions stabilize within a few steps, with most adjustment occurring early in the recursion. This rapid convergence is consistent with the TRM design: the recursive core learns an improvement operator that quickly refines an initial estimate rather than building up a prediction from scratch.

Figure [2](https://arxiv.org/html/2601.07675v1#S5.F2 "Figure 2 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") visualizes the token trajectories in a 2-dimensional PCA space, where the basis is fit to all 𝐚\mathbf{a} and 𝒛\bm{z} vectors across outer steps. The 𝐚\mathbf{a} trajectories collapse toward a common region of the embedding space, while 𝒛\bm{z} remains more dispersed across policies. This pattern supports the intended role of each token: 𝒛\bm{z} acts as a flexible workspace that integrates policy-specific feature evidence, while 𝐚\mathbf{a} converges to the final risk indication.

#### Feature alignment and attribution

To understand how the model weights different covariates, we compute the cosine similarity (alignment) between each input feature embedding and the answer token at each outer step. Figure [3](https://arxiv.org/html/2601.07675v1#S5.F3 "Figure 3 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") reports the mean alignment across the test subset, along with the change in alignment from the first to the final step for both 𝐚\mathbf{a} and 𝒛\bm{z}. This reveals how the recursion progressively reweighs evidence across features, with some covariates gaining influence while others are downweighted.

Figure [4](https://arxiv.org/html/2601.07675v1#S5.F4 "Figure 4 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") provides a complementary view through gradient-based attribution. For each policy we compute ∇𝐚μ^\nabla\_{\mathbf{a}}\hat{\mu} from the decoder and project this gradient onto each input feature embedding; μ^\hat{\mu} reflects the estimated mean, see ([24](https://arxiv.org/html/2601.07675v1#S4.E24 "Equation 24 ‣ 4.1 Data and Baseline Formulation ‣ 4 Application: French MTPL Data ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")). The resulting attribution scores indicate which feature directions are most aligned with the final prediction, offering a saliency-style interpretation of the model’s decision.

#### Update dynamics and linear structure

Figure [5](https://arxiv.org/html/2601.07675v1#S5.F5 "Figure 5 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") summarises the step-to-step changes Δ​𝐚\Delta\mathbf{a} and Δ​𝒛\Delta\bm{z} across transitions between successive outer steps. The left panel shows update magnitudes as boxplots; the right panel reports direction consistency, defined as the norm of the mean of unit-normalized update vectors. The 𝐚\mathbf{a} updates are smaller and more directionally consistent than those of 𝒛\bm{z}, confirming that the answer token follows a stable refinement trajectory while the reasoning token explores more freely.

To quantify how much of the recursive dynamics can be explained by linear operations, we fit least-squares surrogates of the form Δ​𝐚(t)=At​[𝐚(t),𝒛(t),𝒆1,…,𝒆L]⊤+𝐜t\Delta\mathbf{a}^{(t)}=A\_{t}[\mathbf{a}^{(t)},\bm{z}^{(t)},\bm{e}\_{1},\ldots,\bm{e}\_{L}]^{\top}+\mathbf{c}\_{t}, and similarly for 𝒛(t)\bm{z}^{(t)}. Figure [6](https://arxiv.org/html/2601.07675v1#S5.F6 "Figure 6 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") reports the R2R^{2} of these fits (left) and the relative coefficient norms grouped by state tokens versus categorical and continuous feature embeddings (right). The high R2R^{2} values indicate that the update dynamics are well-approximated by linear maps in the learned basis.

Figure [7](https://arxiv.org/html/2601.07675v1#S5.F7 "Figure 7 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") extends this analysis by reporting per-step R2R^{2} for models using the full context versus state-only inputs, along with the spectral radius of the estimated per-step update operator AtA\_{t}. The spectral radii of the per-step updates remain moderate, indicating that individual refinement steps do not amplify state norms excessively. These diagnostics reinforce the state-space interpretation of Section [3.1](https://arxiv.org/html/2601.07675v1#S3.SS1 "3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"): Tab-TRM behaves as a near-linear dynamical system with a nonlinear observation equation. Note that Section [6](https://arxiv.org/html/2601.07675v1#S6 "6 Linearized Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") presents a complementary analysis for a fully linearized variant, where the effective outer-step transition matrix has spectral radius 1.441.44, the dynamics are thus finite-step refinements rather than strict contractions to a fixed point.

#### Local coefficients

Figures [8](https://arxiv.org/html/2601.07675v1#S5.F8 "Figure 8 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") and [9](https://arxiv.org/html/2601.07675v1#S5.F9 "Figure 9 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") report coefficient-style effects for categorical and continuous variables by differentiating the log-prediction log⁡μ^\log\hat{\mu} with respect to each scaled input. The former figure shows the mean derivative ∂log⁡μ^/∂xj\partial\log\hat{\mu}/\partial x\_{j} with ±1\pm 1 standard deviation across policies; the latter figure aggregates these derivatives within the learned piecewise-linear encoder bins to recover per-bin slope profiles for the continuous variables. These “local coefficients” provide an actuarial interpretation of the model’s response to changes in each covariate.

#### Key insights

The interpretability analyses yield two complementary sets of insights: one concerning the Tab-TRM architecture itself, and one concerning the risk structure of the French MTPL data.

*Insights about the model.* The recursive dynamics of Tab-TRM are remarkably well approximated by linear operations in the learned embedding space (R2>0.9R^{2}>0.9 for the linear surrogates). This validates the state-space interpretation developed in Section [3.1](https://arxiv.org/html/2601.07675v1#S3.SS1 "3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), and it explains why even zero-hidden-layer update networks achieve competitive performance: the model’s expressive power comes primarily from (i) the nonlinear feature encoders (piecewise-linear embeddings for continuous variables, entity embeddings for categorical variables), (ii) the recursive composition of updates, and (iii) the decoder. The moderate per-step spectral radii indicate stable refinement dynamics within the chosen recursion budget. The answer token 𝐚\mathbf{a} follows a consistent refinement direction across policies, while the reasoning token 𝒛\bm{z} acts as a flexible scratchpad that integrates heterogeneous feature evidence before distilling it into the final prediction.

*Insights about the French MTPL data.* The feature alignment and gradient attribution analyses (Figures [3](https://arxiv.org/html/2601.07675v1#S5.F3 "Figure 3 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")–[4](https://arxiv.org/html/2601.07675v1#S5.F4 "Figure 4 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")) reveal which tariff factors most strongly influence the predicted claim frequency. Among the continuous variables, the bonus-malus level and the driver age show the largest alignment shifts and attribution scores, consistent with their well-documented importance in European motor pricing. Vehicle power and vehicle age also contribute meaningfully, while population density exhibits a more moderate effect. Among the categorical variables, region and vehicle brand emerge as the most influential, reflecting geographic risk variation and fleet-specific effects. The local coefficient curves in Figure [8](https://arxiv.org/html/2601.07675v1#S5.F8 "Figure 8 ‣ Key insights ‣ 5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") further reveal nonlinear rating structures: for instance, claim frequency decreases with driver age until middle age and then flattens, while the bonus-malus effect is approximately log-linear. These patterns align with standard actuarial intuition and with findings from classical GLM analyses of the same portfolio, providing confidence that Tab-TRM has learned economically meaningful risk relationships rather than spurious correlations.

Taken together, these analyses reveal that Tab-TRM relies less on deep nonlinear composition and more on repeated, largely linear refinements. Early recursion steps move the prediction into the appropriate region; later steps apply smaller corrections. The reasoning token 𝒛\bm{z} integrates feature evidence, while the answer token 𝐚\mathbf{a} stabilizes into the final prediction.

![Refer to caption](figures/trm_token_dynamics.png)


Figure 1: Token magnitude and prediction refinement. Left: mean ℓ2\ell\_{2} norms of 𝐚\mathbf{a} and 𝒛\bm{z} across outer steps with ±1\pm 1 standard deviation bands over 512 random test policies. Right: per-step predictions computed from the 𝐚\mathbf{a} token and exposure; line is the median, shaded band is the interquartile range, dashed line is the mean.

![Refer to caption](figures/trm_pca_trajectories.png)


Figure 2: Token trajectories in PCA space. PCA basis is fit to all 𝐚\mathbf{a} and 𝒛\bm{z} token vectors across outer steps for the 512-policy test subset. Faint lines show 80 random trajectories; bold lines highlight five policies selected by final prediction percentiles (5, 25, 50, 75, 95). Markers denote start (after the first outer step, open) and end (after the final outer step, filled) positions.

![Refer to caption](figures/trm_insight_feature_attention.png)


Figure 3: Feature-to-token alignment. Left: mean cosine similarity between each feature embedding (encoder feature tokens) and the 𝐚\mathbf{a} token at each outer step for the 512-policy test subset. Right: alignment shift (final minus initial) for both 𝐚\mathbf{a} and 𝒛\bm{z}.

![Refer to caption](figures/trm_insight_attribution.png)


Figure 4: Gradient-based feature attribution. For each policy, we compute ∇𝐚μ^\nabla\_{\mathbf{a}}\hat{\mu} from the decoder and project it onto each encoder feature embedding; bars show mean attribution with ±\pm1 standard deviation across the 512-policy test subset.

![Refer to caption](figures/trm_insight_updates.png)


Figure 5: Token update decomposition on the 512-policy test subset. Left: distribution of update magnitudes ∥Δ​𝐚∥\lVert\Delta\mathbf{a}\rVert and ∥Δ​𝒛∥\lVert\Delta\bm{z}\rVert by transition (differences between successive outer steps). Right: direction consistency defined as ∥mean​(Δ/∥Δ∥)∥\lVert\mathrm{mean}(\Delta/\lVert\Delta\rVert)\rVert across samples.

![Refer to caption](figures/trm_linear_update_surrogate.png)


Figure 6: Linear surrogate of update dynamics. Left: R2R^{2} of least-squares fits predicting Δ​𝐚\Delta\mathbf{a} and Δ​𝒛\Delta\bm{z} from concatenated [𝐚(t),𝒛(t),e1,…,eL][\mathbf{a}^{(t)},\bm{z}^{(t)},e\_{1},\dots,e\_{L}]. Right: relative coefficient norm by group (tokens vs categorical/continuous feature embeddings), showing which components contribute most to each update.

![Refer to caption](figures/trm_linear_update_diagnostics.png)


Figure 7: Linearity diagnostics by recursion step. Left: per-step R2R^{2} of linear fits for Δ​𝐚(t)\Delta\mathbf{a}^{(t)} and Δ​𝒛(t)\Delta\bm{z}^{(t)}, shown for models using the full feature context and using (𝐚(t),𝒛(t))(\mathbf{a}^{(t)},\bm{z}^{(t)}) only. Right: spectral radius of the effective linear update map 𝑰+At\bm{I}+A\_{t} (solid) and of the update operator AtA\_{t} itself (dashed), estimated from least-squares fits on the concatenated state.

![Refer to caption](figures/trm_local_coefficients_main.png)


Figure 8: Local coefficient analysis for categorical and continuous features. Mean ∂log⁡μ^/∂xj\partial\log\hat{\mu}/\partial x\_{j} with ±\pm1 standard deviation across the 512-policy test subset (inputs use the scaled continuous variables from the data pipeline).

![Refer to caption](figures/trm_local_coefficients_curves.png)


Figure 9: Local coefficient analysis for categorical and continuous features. Per-bin averages of ∂log⁡μ^/∂xj\partial\log\hat{\mu}/\partial x\_{j} using the learned piecewise-linear encoder bin edges, shown as coefficient curves for each continuous variable.

### 5.3 Test-time recursion selection

We evaluate test-time recursion by varying outer steps TT and inner iterations mm on a held-out validation subset (10% of the training set, random sample). For each (T,m)(T,m) we run the recursive layer starting from the validation tokens, compute predictions from the final 𝐚\mathbf{a} token and exposure, and report the Poisson deviance loss, see Figure [10](https://arxiv.org/html/2601.07675v1#S5.F10 "Figure 10 ‣ 5.3 Test-time recursion selection ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"). The validation minimum occurs at T=6T=6, m=3m=3 with a Poisson deviance loss of 23.890×10−223.890\times 10^{-2}, close to the Optuna selection score. Applying this configuration on the test set yields a Poisson deviance loss of 23.650×10−223.650\times 10^{-2} for the best single model; the nagging ensemble remains at 23.589×10−223.589\times 10^{-2}.

![Refer to caption](figures/trm_test_time_recursion.png)


Figure 10: Validation deviance heatmap over recursion settings. Outer steps T∈{1,2,3,4,5,6,8,10}T\in\{1,2,3,4,5,6,8,10\} and inner iterations m∈{0,1,2,3,4,5,6,8}m\in\{0,1,2,3,4,5,6,8\} are evaluated on the 10% validation subset; markers denote the best validation and training configurations, respectively.

## 6 Linearized Tab-TRM

The interpretability analyses of Section [5.2](https://arxiv.org/html/2601.07675v1#S5.SS2 "5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") revealed that the per-step updates Δ​𝐚(t)\Delta\mathbf{a}^{(t)} and Δ​𝒛(t)\Delta\bm{z}^{(t)} are well-approximated by linear maps in the learned embedding space, with R2R^{2} values exceeding 0.80.8 across recursion steps. This near-linearity motivates a natural question: *What happens if we enforce exact linearity in the update networks?* In this section we explore a fully linearized variant of Tab-TRM, which provides both a simpler model and a concrete instantiation of the state-space interpretation developed in Section [3.1](https://arxiv.org/html/2601.07675v1#S3.SS1 "3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data").

### 6.1 Linear Update Architecture

In the linearized model, we remove all nonlinear activations from the update networks fzf\_{z} and faf\_{a}, replacing them with single affine maps. The feature encoders (piecewise-linear embeddings for continuous variables, entity embeddings for categorical variables) and the FNN decoder remain unchanged, only the recursive core becomes linear.

Let 𝒆¯=1L​∑ℓ=1L𝒆ℓ\bar{\bm{e}}=\frac{1}{L}\sum\_{\ell=1}^{L}\bm{e}\_{\ell} denote the mean feature token. The inner-loop updates become

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒛(t,s+1)=𝒛(t,s)+𝑾z​z​𝒛(t,s)+𝑾a​z​𝐚(t)+𝑾f​𝒆¯+𝒃z,s=0,…,m−1,\bm{z}^{(t,s+1)}=\bm{z}^{(t,s)}+\bm{W}\_{zz}\bm{z}^{(t,s)}+\bm{W}\_{az}\mathbf{a}^{(t)}+\bm{W}\_{f}\bar{\bm{e}}+\bm{b}\_{z},\qquad s=0,\ldots,m-1, |  | (30) |

and the outer-loop update is with 𝒛(t+1)=𝒛(t,m)\bm{z}^{(t+1)}=\bm{z}^{(t,m)}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐚(t+1)=𝐚(t)+𝑾a​a​𝐚(t)+𝑾z​a​𝒛(t+1)+𝒃a.\mathbf{a}^{(t+1)}=\mathbf{a}^{(t)}+\bm{W}\_{aa}\mathbf{a}^{(t)}+\bm{W}\_{za}\bm{z}^{(t+1)}+\bm{b}\_{a}. |  | (31) |

These updates are linear in the state (𝐚,𝒛)(\mathbf{a},\bm{z}) and in the feature tokens. With LayerNorm disabled, the recursion is an exact linear state-space model of the form ([23](https://arxiv.org/html/2601.07675v1#S3.E23 "Equation 23 ‣ Linear reformulation (exact state-space form). ‣ 3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")); with LayerNorm retained, the dynamics are a linear map followed by normalization (piecewise-linear). The observation equation remains the FNN decoder with exponential output activation

|  |  |  |
| --- | --- | --- |
|  | μ^i=vi​exp⁡(fo​(𝐚i(T)))=vi​Fθ​(𝒙i,𝒄i),\hat{\mu}\_{i}=v\_{i}\,\exp\left(f\_{o}(\mathbf{a}\_{i}^{(T)})\right)=v\_{i}\,F\_{\theta}(\bm{x}\_{i},\bm{c}\_{i}), |  |

so the overall model is linear in latent dynamics with a GLM-style nonlinear readout.

### 6.2 Predictive Performance

To test whether the near-linearity observed in Section [5.2](https://arxiv.org/html/2601.07675v1#S5.SS2 "5.2 Interpretability Analysis ‣ 5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") is sufficient for prediction, we trained the fully linearized Tab-TRM variant (nonlinear activations removed from fzf\_{z} and faf\_{a}; encoder and decoder unchanged). Using a 10-run nagging ensemble, the test Poisson deviance losses ranged from 23.695×10−223.695\times 10^{-2} to 23.780×10−223.780\times 10^{-2} (mean 23.742×10−223.742\times 10^{-2}), with an ensemble deviance of 23.698×10−223.698\times 10^{-2} and the best single run at 23.695×10−223.695\times 10^{-2}. While these results are slightly worse than the full Tab-TRM ensemble studied in Section [5](https://arxiv.org/html/2601.07675v1#S5 "5 Results ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), nonetheless, it is remarkable that a model consisting of multivariate linear models can achieve reasonable performance. This suggests that the recursive learning in Tab-TRM, which performs function composition in latent space, is a powerful mechanism for tabular machine learning.

One way of understanding the success of this linear version of the TRM model is to consider that, in the optimal parameter settings of the TRM model found here, the tokens (𝐚,𝒛)(\mathbf{a},\bm{z}) and the feature tokens are embedded into a very high-dimensional space (d=28d=28). This can be thought of a fine-grained binning of the continuous covariates via the numerical embeddings and, likewise, the categorical covariates are embedded into a very high-dimensonal space. These fine-grained input embeddings adequately capture the complexity of the French MTPL data and the TRM merely needs to select and rearrange this fine-grained representation so that it is suitable for prediction. Exactly for this reason, non-linearity in the TRM recursion is not important, in other words, it is easy to extract the relevant information from these large embeddings. To test this hypothesis, we reran the TRM model with the same hyperparameters but with d=4d=4 (i.e., a low-dimensional embedding). The test Poisson deviance losses ranged from 23.644×10−223.644\times 10^{-2} to 23.737×10−223.737\times 10^{-2} (mean 23.706×10−223.706\times 10^{-2}), with an ensemble deviance of 23.651×10−223.651\times 10^{-2} and the best single run at 23.644×10−223.644\times 10^{-2}. Reestimating the correlation of the updates Δ​𝐚(t)\Delta\mathbf{a}^{(t)} and Δ​𝒛(t)\Delta\bm{z}^{(t)} with the feature tokens, we find that, in this case of lower-dimensional reprsentations, these updates are not nearly as well approximated by linear maps as before, with significant reductions in the R2R^{2} values to values of apprximately 0.80.8 and 0.50.5 for the Δ​𝐚(t)\Delta\mathbf{a}^{(t)} and Δ​𝒛(t)\Delta\bm{z}^{(t)} updates, respectively. We conclude that, while the recursion in the TRM model can deal with complex non-linear updates to extract relevant information from embeddings if needed, nonetheless, in the case of the French data a more optimal approach is to use larger embeddings to model the complexity and rely on linear recursive updates.

### 6.3 State-Space Diagnostics

The linear formulation permits direct analysis of the transition dynamics. Following the derivation in Section [3.1](https://arxiv.org/html/2601.07675v1#S3.SS1 "3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"), we can express the system as

|  |  |  |
| --- | --- | --- |
|  | 𝒔(t+1)=𝑨​𝒔(t)+𝑩​𝒆¯+𝒄,\bm{s}^{(t+1)}=\bm{A}\,\bm{s}^{(t)}+\bm{B}\,\bar{\bm{e}}+\bm{c}, |  |

where 𝒔(t)=[𝐚(t),𝒛(t)]⊤\bm{s}^{(t)}=[\mathbf{a}^{(t)},\bm{z}^{(t)}]^{\top} is the stacked state vector and 𝑨\bm{A}, 𝑩\bm{B}, 𝒄\bm{c} are the block matrices defined in ([23](https://arxiv.org/html/2601.07675v1#S3.E23 "Equation 23 ‣ Linear reformulation (exact state-space form). ‣ 3.1 Connection to State-Space Models ‣ 3 Interpreting Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data")).

Figure [11](https://arxiv.org/html/2601.07675v1#S6.F11 "Figure 11 ‣ 6.4 Implications ‣ 6 Linearized Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") shows the eigenvalue spectrum of the effective outer-step transition matrix 𝑨\bm{A}. The spectral radius is 1.441.44, implying that the linearized dynamics are not strictly contractive. The recursion therefore acts as a finite-step refinement rather than a convergence-to-fixed-point mechanism.
Figure [12](https://arxiv.org/html/2601.07675v1#S6.F12 "Figure 12 ‣ 6.4 Implications ‣ 6 Linearized Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") reports the step response of the linearized model to individual feature tokens, showing how each encoded feature drives the evolution of the answer token 𝐚\mathbf{a} over outer steps. Features with larger step responses have a stronger immediate influence on the predicted rate. Figure [13](https://arxiv.org/html/2601.07675v1#S6.F13 "Figure 13 ‣ 6.4 Implications ‣ 6 Linearized Tab-TRM ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data") computes the steady-state feature influence via (𝑰−𝑨)−1​𝑩(\bm{I}-\bm{A})^{-1}\bm{B}, which gives the long-run contribution of each feature direction to the latent answer assuming the dynamics were to continue indefinitely. The signed bars reveal which features push the predicted rate up versus down.

### 6.4 Implications

These results reinforce the interpretability narrative developed throughout this paper. Tab-TRM behaves like a linear dynamical system in a learned basis, with the nonlinear feature encoders defining that basis and the recursive core applying repeated linear refinements. The strong performance of the linearized model (within 0.1×10−20.1\times 10^{-2} of the full model) demonstrates that the nonlinear depth of the update networks is not essential for predictive accuracy. Instead, the key inductive bias lies in the recursive state-space structure itself.
This architecture of nonlinear encoding, linear latent dynamics and nonlinear decoding is reminiscent of classical state-space models in control theory and time-series analysis, but here learned end-to-end from insurance data. When LayerNorm is enabled inside the recursion, the linear diagnostics are approximate but remain informative, since LayerNorm preserves linear directions while normalizing the scale.

![Refer to caption](figures/trm_linear_eigs.png)


Figure 11: Eigenvalue spectrum of the linearized Tab-TRM transition matrix 𝑨\bm{A}. The unit circle is shown for reference. The spectral radius of 1.441.44 indicates that the dynamics are not strictly contractive, supporting the interpretation of the recursion as a finite-step refinement rather than convergence to a fixed point.

![Refer to caption](figures/trm_linear_step_response.png)


Figure 12: Step responses of the linearized Tab-TRM to individual feature tokens. Each curve shows the evolution of the answer token norm ‖𝐚(t)‖\|\mathbf{a}^{(t)}\| over outer steps when only one feature token is active. Features with larger step responses have stronger immediate influence on the predicted rate.

![Refer to caption](figures/trm_linear_fixed_point.png)


Figure 13: Steady-state feature influence for the linearized Tab-TRM, computed via (𝑰−𝑨)−1​𝑩(\bm{I}-\bm{A})^{-1}\bm{B} and projected onto the mean answer direction. Bars show signed contributions: positive values indicate features that increase the predicted claim frequency, negative values indicate features that decrease it.

## 7 Discussion

From a machine-learning perspective, Tab-TRM is closely related to classical recurrent neural network (RNN) architectures, but with a structure that is particularly amenable to actuarial interpretation.
If we unroll the recursive core of Tab-TRM over its mm inner iterations and TT outer blocks, we obtain a computation graph that resembles a RNN unrolled over m​TmT time steps: a fixed “cell” (the tiny feed-forward reasoning core) is applied repeatedly to a hidden state. The key difference is that the hidden state here is split into two parts, (𝐚,𝒛)(\mathbf{a},\bm{z}), with a specific semantic role, namely, 𝒛\bm{z} is the scratchpad that accumulates reasoning about the features, and 𝐚\mathbf{a} is the candidate answer.

Gated architectures such as LSTMs and GRUs were introduced to mitigate vanishing gradients by allowing networks to learn when to remember, forget and update different components of the hidden state. Conceptually, Tab-TRM takes a complementary route: it keeps the state *very small* (just two tokens) and gains depth through recursion and parameter sharing rather than heavy gating. The pair (𝐚,𝒛)(\mathbf{a},\bm{z}) plays a role reminiscent of an LSTM’s pair of states (cell state and hidden state), in that one component acts as long-lived memory and the other as a more immediate predictor (naturally through the different updating speeds).

Classical deep learning for tabular data often tries to improve performance by stacking more feed-forward layers. Both HRM and TRM suggest an alternative, namely, keep the network tiny and reuse it many times, using recursion and deep supervision to emulate large effective depth without the parameter blow-up and overfitting risk of very wide or very deep FNNs; see Bai et al. ([2019](https://arxiv.org/html/2601.07675v1#bib.bib2)). In our setting, this is particularly attractive because insurance datasets, even when they contain hundreds of thousands of policies, may still be small relative to the capacity of modern deep networks. By placing most of the “depth” into the recursion rather than into separate parametrized layers, Tab-TRM lives in the same conceptual space as equilibrium and recurrent models, but with a design and loss function that actuaries are already familiar with.

Both the original TRM and our Tab-TRM experiments reveal a *less is more* phenomenon: smaller networks with more recursion often outperform larger networks with fewer recursion steps. This can be explained in several ways. From an overfitting perspective, when training data are limited, large networks quickly memorize the training set, whereas constraining the network to be tiny and reusing its parameters across many recursion steps effectively regularizes the model while still achieving large effective depth. From an architectural perspective, parameter sharing across recursion steps acts as a strong inductive bias, forcing the network to learn a general-purpose “improvement operator” rather than separate transformations for each layer. Finally, viewed from an algorithmic standpoint, the recursive structure encodes a prior that the optimal prediction can be reached through iterative refinement.

## 8 Conclusion

We have introduced Tab-TRM (Tabular-Tiny Recursive Model), an architecture that brings the recursive latent reasoning paradigm of TRMs to tabular insurance pricing. Architecturally, we have demonstrated how to tokenize tabular insurance data via categorical embeddings and piecewise-linear continuous encodings and how to augment the resulting token sequence with learned answer (𝐚\mathbf{a}) and reasoning (𝒛\bm{z}) prefix tokens, thereby enabling TRM-style iterative refinement in a classical Poisson GLM setting. Empirically, on a large French MTPL portfolio, Tab-TRM achieves the best test Poisson deviance score with fewer trainable parameters than comparable architectures, confirming that the “less is more” principle extends from symbolic reasoning to noisy tabular regression. Conceptually, we have established parallels between Tab-TRM’s recursive computation and classical actuarial procedures such as GLMs, IRLS and modern tabular machine learning in the form of GBMs, making the architecture interpretable to practitioners and highlighting its role as a bridge between traditional actuarial workflows and modern latent recurrent architectures.

We have highlighted the close connection of the Tab-TRM to state-space models. In the case of larger embedding dimensions, the learned state-space dynamics is almost linear, as the nonlinearity can be taken care off by the embeddings and the readout.

Several directions remain for future investigation. The current work focuses on claim frequency; extending Tab-TRM to severity distributions e.g., gamma or log-normal, and to combined frequency-severity models is a natural next step. Insurance portfolios have inherent temporal structure: policy years, claims history, and development triangles. Incorporating this structure into the recursive framework, e.g., by carrying (𝐚,𝒛)(\mathbf{a},\bm{z}) across time periods, could enable more sophisticated experience rating schemes. Finally, a formal analysis of Tab-TRM’s approximation properties and generalization behavior would provide deeper understanding of when and why recursive reasoning helps.

## Acknowledgements

We kindly thank Darren Cohen from insureAI for the suggestion to consider TRM in the context of insurance pricing.

## References

* Akiba et al. (2019)

  Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A next-generation hyperparameter optimization framework.
  Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.
* Bai et al. (2019)

  Bai, S., Kolter, J.Z., & Koltun, V. (2019).
  Deep equilibrium models.
  In *Advances in Neural Information Processing Systems*.
* Brauer (2024)

  Brauer, A. (2024).
  Enhancing actuarial non-life pricing models via transformers.
  *European Actuarial Journal*, 14(3), 991–1012.
* Chollet (2019)

  Chollet, F. (2019).
  On the measure of intelligence.
  *arXiv preprint arXiv:1911.01547*.
* DeepSeek-AI (2025)

  DeepSeek-AI (2025).
  DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning.
  *arXiv preprint arXiv:2501.12948*.
* Dutang et al. (2024)

  Dutang, C., Charpentier, A., & Gallic, E. (2024).
  Insurance dataset.
  <https://github.com/dutangc/CASdatasets>
* Friedman (2001)

  Friedman, J.H. (2001).
  Greedy function approximation: A gradient boosting machine.
  *Annals of Statistics*, 29(5), 1189–1232.
* Gorishniy et al. (2022)

  Gorishniy, Y., Rubachev, I., & Babenko, A. (2022).
  On embeddings for numerical features in tabular deep learning.
  *Advances in Neural Information Processing Systems*, 35, 24991–25004.
* Guo and Berkhahn (2016)

  Guo, C. & Berkhahn, F. (2016).
  Entity embeddings of categorical variables.
  *arXiv preprint arXiv:1604.06737*.
* Holzmüller et al. (2024)

  Holzmüller, D., Grinsztajn, L., & Obst, B. (2024).
  Better by default: Strong pre-tuned MLPs and boosting algorithms without hyperparameter selection.
  *Advances in Neural Information Processing Systems*, 37.
* Jolicoeur-Martineau (2025)

  Jolicoeur-Martineau, A. (2025).
  Less is more: Recursive reasoning with tiny networks.
  *arXiv preprint arXiv:2510.04871*.
* Lambert et al. (2025)

  Lambert, N., Liu, T., Raju, K., Jaech, A., Liusie, A., Gurnee, W., & Gandhi, S. (2025).
  Reinforcement learning with verifiable rewards implicitly incentivizes correct reasoning in base LLMs.
  *arXiv preprint arXiv:2506.14245*.
* Noll et al. (2018)

  Noll, A., Salzmann, R., & Wüthrich, M.V. (2018).
  Case study: French motor third-party liability claims.
  *SSRN Working Paper 3164764*.
* Nye et al. (2021)

  Nye, M., Andreassen, A.J., Gur-Ari, G., Michalewski, H., Austin, J., Biber, D., Dohan, D., Lewkowycz, A., Bosma, M., Luan, D., Sutton, C., & Odena, A. (2021).
  Show your work: Scratchpads for intermediate computation with language models.
  *arXiv preprint arXiv:2112.00114*.
* Padayachy et al. (2025)

  Padayachy, K., Richman, R., Scognamiglio, S., & Wüthrich, M.V. (2025).
  In-context learning enhanced credibility transformer.
  *arXiv preprint arXiv:2509.08122*.
* Richman (2021a)

  Richman, R. (2021a).
  AI in actuarial science – a review of recent advances – part 1.
  *Annals of Actuarial Science*, 15(2), 207–229.
* Richman (2021b)

  Richman, R. (2021b).
  AI in actuarial science – a review of recent advances – part 2.
  *Annals of Actuarial Science*, 15(2), 230–258.
* Richman et al. (2025a)

  Richman, R., Scognamiglio, S., & Wüthrich, M.V. (2025a).
  The credibility transformer.
  *European Actuarial Journal*, forthcoming.
  Also available as *arXiv preprint arXiv:2409.16653*.
* Richman et al. (2025b)

  Richman, R., Scognamiglio, S., & Wüthrich, M.V. (2025b).
  Tree-like pairwise interaction networks.
  *arXiv preprint arXiv:2508.15678*.
* Richman and Wüthrich (2022)

  Richman, R. & Wüthrich, M.V. (2022).
  Nagging predictors.
  *Risks*, 10(12), 231.
* Richman and Wüthrich (2023)

  Richman, R. & Wüthrich, M.V. (2023).
  LocalGLMnet: Interpretable deep learning for tabular data.
  *Scandinavian Actuarial Journal*, 2023(1), 71–95.
* Schelldorfer and Wüthrich (2019)

  Schelldorfer, J. & Wüthrich, M.V. (2019).
  Nesting classical actuarial models into neural networks.
  *SSRN Working Paper 3320525*.
* Snell et al. (2024)

  Snell, C., Lee, J., Xu, K., & Kumar, A. (2024).
  Scaling LLM test-time compute optimally can be more effective than scaling model parameters.
  *arXiv preprint arXiv:2408.03314*.
* Wang et al. (2025)

  Wang, G., Li, J., Sun, Y., Chen, X., Liu, C., Wu, Y., Lu, M., Song, S., & Abbasi Yadkori, Y. (2025).
  Hierarchical reasoning model.
  *arXiv preprint arXiv:2506.21734*.
* Wei et al. (2022)

  Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q.V., & Zhou, D. (2022).
  Chain-of-thought prompting elicits reasoning in large language models.
  *Advances in Neural Information Processing Systems*, 35, 24824–24837.
* Wüthrich and Merz (2023)

  Wüthrich, M.V. & Merz, M. (2023).
  *Statistical Foundations of Actuarial Learning and its Applications*.
  Springer, Cham.
* Wüthrich et al. (2025)

  Wüthrich, M.V., Richman, R., Avanzi, B., Lindholm, M., Mayer, M., Schelldorfer, J., & Scognamiglio, S. (2025).
  AI tools for actuaries.
  *SSRN Working Paper 5162304*.

## Appendix A Algorithm Pseudo Code

See Algorithm [1](https://arxiv.org/html/2601.07675v1#alg1 "Algorithm 1 ‣ Appendix A Algorithm Pseudo Code ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data").

Algorithm 1  Tab-TRM Forward Pass

0:  Policy features (𝒙i,𝒄i)(\bm{x}\_{i},\bm{c}\_{i}), exposure viv\_{i}

0:  Embedding functions {ϕj}j=1pr\{\phi\_{j}\}\_{j=1}^{p\_{r}} for continuous and {ψj}j=1pc\{\psi\_{j}\}\_{j=1}^{p\_{c}} for categorical features

0:  Initial tokens 𝐚(0),𝒛(0)\mathbf{a}^{(0)},\bm{z}^{(0)}

0:  Networks fz,fa,fof\_{z},f\_{a},f\_{o}

0:  Inner iterations mm, outer iterations TT

1:  // Tokenize features

2:  for j=1j=1 to prp\_{r} do

3:   Compute x~i,j\tilde{x}\_{i,j} using ([27](https://arxiv.org/html/2601.07675v1#S4.E27 "Equation 27 ‣ Continuous tariff variables ‣ 4.2 Feature Transformations, Embeddings and Tokens ‣ 4 Application: French MTPL Data ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data"))

4:   𝒆i,j←ϕj​(x~i,j)\bm{e}\_{i,j}\leftarrow\phi\_{j}(\tilde{x}\_{i,j}) {Continuous embedding}

5:  end for

6:  for j=1j=1 to pcp\_{c} do

7:   𝒆i,pr+j←ψj​(ci,j)\bm{e}\_{i,p\_{r}+j}\leftarrow\psi\_{j}(c\_{i,j}) {Categorical embedding}

8:  end for

9:  // Initialize sequence

10:  𝑺i(0)←[𝐚(0),𝒛(0),𝒆i,1,…,𝒆i,pr+pc]\bm{S}\_{i}^{(0)}\leftarrow[\mathbf{a}^{(0)},\bm{z}^{(0)},\bm{e}\_{i,1},\ldots,\bm{e}\_{i,p\_{r}+p\_{c}}]

11:  // Outer recursion

12:  for t=1t=1 to TT do

13:   𝒛i(t,0)←𝒛i(t−1)\bm{z}\_{i}^{(t,0)}\leftarrow\bm{z}\_{i}^{(t-1)}, 𝑺i(t,0)←𝑺i(t−1)\bm{S}\_{i}^{(t,0)}\leftarrow\bm{S}\_{i}^{(t-1)}

14:   // Inner recursion (Stage 1: update z\bm{z})

15:   for s=0s=0 to m−1m-1 do

16:    𝒖i←Flatten⁡(𝑺i(t,s))\bm{u}\_{i}\leftarrow\operatorname{Flatten}(\bm{S}\_{i}^{(t,s)})

17:    𝒖~i←LayerNorm⁡(𝒖i)\tilde{\bm{u}}\_{i}\leftarrow\operatorname{LayerNorm}(\bm{u}\_{i})

18:    Δ​𝒛i(t,s+1)←fz​(𝒖~i)\Delta\bm{z}\_{i}^{(t,s+1)}\leftarrow f\_{z}(\tilde{\bm{u}}\_{i})

19:    𝒛i(t,s+1)←𝒛i(t,s)+Δ​𝒛i(t,s+1)\bm{z}\_{i}^{(t,s+1)}\leftarrow\bm{z}\_{i}^{(t,s)}+\Delta\bm{z}\_{i}^{(t,s+1)}

20:    Update 𝑺i(t,s+1)\bm{S}\_{i}^{(t,s+1)} by replacing token 1 with 𝒛i(t,s+1)\bm{z}\_{i}^{(t,s+1)}

21:   end for

22:   𝒛i(t)←𝒛i(t,m)\bm{z}\_{i}^{(t)}\leftarrow\bm{z}\_{i}^{(t,m)}

23:   𝑺i(t,m)←[𝐚i(t−1),𝒛i(t),𝒆i,1,…,𝒆i,pr+pc]\bm{S}\_{i}^{(t,m)}\leftarrow[\mathbf{a}\_{i}^{(t-1)},\bm{z}\_{i}^{(t)},\bm{e}\_{i,1},\ldots,\bm{e}\_{i,p\_{r}+p\_{c}}]

24:   𝑺~i←LayerNorm⁡(𝑺i(t,m))\tilde{\bm{S}}\_{i}\leftarrow\operatorname{LayerNorm}(\bm{S}\_{i}^{(t,m)})

25:   Extract 𝐚~i(t−1),𝒛~i(t)\tilde{\mathbf{a}}\_{i}^{(t-1)},\tilde{\bm{z}}\_{i}^{(t)} as tokens 0 and 1 of 𝑺~i\tilde{\bm{S}}\_{i}

26:   // Answer update (Stage 2: update 𝐚\mathbf{a})

27:   Δ​𝐚i(t)←fa​([𝐚~i(t−1),𝒛~i(t)])\Delta\mathbf{a}\_{i}^{(t)}\leftarrow f\_{a}([\tilde{\mathbf{a}}\_{i}^{(t-1)},\tilde{\bm{z}}\_{i}^{(t)}])

28:   𝐚i(t)←𝐚i(t−1)+Δ​𝐚i(t)\mathbf{a}\_{i}^{(t)}\leftarrow\mathbf{a}\_{i}^{(t-1)}+\Delta\mathbf{a}\_{i}^{(t)}

29:   𝑺i(t)←[𝐚i(t),𝒛i(t),ei,1,…,ei,pr+pc]\bm{S}\_{i}^{(t)}\leftarrow[\mathbf{a}\_{i}^{(t)},\bm{z}\_{i}^{(t)},e\_{i,1},\ldots,e\_{i,p\_{r}+p\_{c}}]

30:  end for

31:  // Decode to Poisson log-link prediction

32:  λ^i←exp⁡(fo​(𝐚i(T)))\hat{\lambda}\_{i}\leftarrow\exp(f\_{o}(\mathbf{a}\_{i}^{(T)}))

33:  μ^i←vi​λ^i\hat{\mu}\_{i}\leftarrow v\_{i}\,\hat{\lambda}\_{i}

34:  return μ^i\hat{\mu}\_{i}

## Appendix B Hyper-parameter Search Space

See Table [4](https://arxiv.org/html/2601.07675v1#A2.T4 "Table 4 ‣ Appendix B Hyper-parameter Search Space ‣ Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data").

Table 4: Hyper-parameter search space for Tab-TRM (Optuna ranges)

| Hyper-parameter | Range | Type |
| --- | --- | --- |
| Embedding dimension dd | [16,60][16,60] | Integer |
| Inner iterations nn | [1,8][1,8] | Integer |
| Outer iterations TT | [1,6][1,6] | Integer |
| fzf\_{z} hidden layers | [0,5][0,5] | Integer |
| faf\_{a} hidden layers | [0,5][0,5] | Integer |
| fzf\_{z} hidden units | [16,128][16,128] | Integer |
| faf\_{a} hidden units | [16,128][16,128] | Integer |
| Dropout (core) | [0.05,0.5][0.05,0.5] | Float |
| Dropout (decoder) | [0.05,0.5][0.05,0.5] | Float |
| ℓ1\ell\_{1}–ℓ2\ell\_{2} strength | [0,10−4][0,10^{-4}] | Float |
| Weight decay | [10−3,4×10−2][10^{-3},4\times 10^{-2}] | Float |
| Learning rate | [10−4,2×10−2][10^{-4},2\times 10^{-2}] | Float |
| Adam β2\beta\_{2} | [0.9,0.99][0.9,0.99] | Float |

## Appendix C LLM Reasoning Background

This appendix provides additional context on LLM reasoning methods that motivate the latent recursion approach adopted in Tab-TRM.

##### Chain-of-thought prompting and its limitations.

Chain-of-thought (CoT) prompting explicitly asks the model to “think step by step” and emit a natural-language solution trace before giving the final answer (Wei et al., [2022](https://arxiv.org/html/2601.07675v1#bib.bib25)). This simple intervention can dramatically improve accuracy on many benchmark datasets, but it comes with costs: long responses, higher latency, sensitivity to the phrasing of the prompt, and the risk that the generated reasoning is partially incorrect even when the final answer happens to be right.

##### Post-training methods for reasoning.

On the training side, there is now a spectrum of *post-training* methods that aim to enhance reasoning by shaping the model’s intermediate computations. One line of work performs supervised fine-tuning (SFT) on curated or synthetic CoT corpora, treating full reasoning traces as targets rather than only the final answer. A more recent and influential approach is *reinforcement learning with verifiable rewards* (RLVR) (Lambert et al., [2025](https://arxiv.org/html/2601.07675v1#bib.bib12)), which trains models using reinforcement learning where rewards are based on objective, programmatically verifiable criteria, e.g., whether a mathematical answer is correct or whether generated code passes a test suite. The DeepSeek-R1 model (DeepSeek-AI, [2025](https://arxiv.org/html/2601.07675v1#bib.bib5)) publicly demonstrated this approach, showing that large-scale reinforcement learning with rule-based rewards for accuracy and format can induce emergent CoT reasoning without extensive supervised fine-tuning on reasoning traces.

##### Reasoning benchmarks.

A particularly challenging benchmark for evaluating reasoning capabilities is the *Abstraction and Reasoning Corpus* (ARC), introduced by Chollet ([2019](https://arxiv.org/html/2601.07675v1#bib.bib4)) as a measure of general fluid intelligence. ARC tasks present small coloured grids where the solver must infer an abstract transformation rule from a handful of input-output examples and apply it to a new test input. The benchmark is designed to require core human cognitive priors (objectness, goal-directedness, symmetry, counting), rather than pattern-matching on large corpora. Similar grid-based reasoning benchmarks include Sudoku-Extreme (completing 9×99\times 9 puzzles with minimal initial clues) and Maze-Hard (navigating 30×3030\times 30 grid mazes). These benchmarks share a common structure: discrete symbolic inputs arranged on a grid, a need for multi-step logical inference, and exact sequence-to-sequence prediction.

##### Test-time compute.

To tackle such benchmarks, CoT prompting at inference is often combined with *test-time compute* (TTC): instead of sampling a single CoT, one draws many candidate traces and either takes a majority vote over the final answers or selects the trace with the highest estimated reward (Snell et al., [2024](https://arxiv.org/html/2601.07675v1#bib.bib23)). This approach can outperform a single-pass baseline without increasing the number of model parameters, but it further inflates inference cost and still relies on the model’s ability to generate coherent natural-language explanations, which may not align with the underlying computation.