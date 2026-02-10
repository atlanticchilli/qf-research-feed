---
authors:
- Matthew Siper
- Muhammad Umair Nasir
- Ahmed Khalifa
- Lisa Soros
- Jay Azhang
- Julian Togelius
doc_id: arxiv:2602.07659v1
family_id: arxiv:2602.07659
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Continuous Program Search
url_abs: http://arxiv.org/abs/2602.07659v1
url_html: https://arxiv.org/html/2602.07659v1
venue: arXiv q-fin
version: 1
year: 2026
---


Matthew Siper
Nof1New YorkNYUSA
[m@thenof1.com](mailto:m@thenof1.com)
, 
Muhammad Umair Nasir
Nof1New YorkNYUSA
[2396876@students.wits.ac.za](mailto:2396876@students.wits.ac.za)
, 
Ahmed Khalifa
Nof1New YorkNYUSA
[aak538@nyu.edu](mailto:aak538@nyu.edu)
, 
Lisa Soros
Nof1New YorkNYUSA
[lisa.soros@gmail.com](mailto:lisa.soros@gmail.com)
, 
Jay Azhang
Nof1New YorkNYUSA
[j@thenof1.com](mailto:j@thenof1.com)
 and 
Julian Togelius
Nof1New YorkNYUSA
[julian@togelius.com](mailto:julian@togelius.com)

###### Abstract.

Genetic Programming yields interpretable programs, but small syntactic mutations can induce large, unpredictable behavioral shifts, degrading locality and sample efficiency. We frame this as an operator-design problem: learn a continuous program space where latent distance has behavioral meaning, then design mutation operators that exploit this structure without changing the evolutionary optimizer.

We make locality measurable by tracking action-level divergence under controlled latent perturbations, identifying an empirical trust region for behavior-local continuous variation. Using a compact trading-strategy DSL with four semantic components (long/short entry and exit), we learn a matching block-factorized embedding and compare isotropic Gaussian mutation over the full latent space to geometry-compiled mutation that restricts updates to semantically paired entry–exit subspaces and proposes directions using a learned flow-based model trained on logged mutation outcomes.

Under identical (μ+λ)(\mu+\lambda) evolution strategies and fixed evaluation budgets across five assets, the learned mutation operator discovers strong strategies using an order of magnitude fewer evaluations and achieves the highest median out-of-sample Sharpe ratio. Although isotropic mutation occasionally attains higher peak performance, geometry-compiled mutation yields faster, more reliable progress, demonstrating that semantically aligned mutation can substantially improve search efficiency without modifying the underlying evolutionary algorithm.

Genetic Programming, Evolutionary Search, Latent Space Optimization, Disentanglement, Algorithmic Trading.

![Refer to caption](x1.png)


(a) Evaluation budget required to discover strong solutions.

![Refer to caption](x2.png)


(b) Final out-of-sample Sharpe distributions.

Figure 1. 
Geometry-aware mutation improves search efficiency and typical performance under a fixed optimizer.
Both panels compare mutation operators under the same (μ+λ)(\mu+\lambda) evolution strategy and identical evaluation budgets.
(Left) shows that geometry-compiled flow-based mutation reaches high-quality strategies using an order of magnitude fewer evaluations than isotropic and dual-block Gaussian baselines.
(Right) reports final out-of-sample Sharpe distributions at the full budget, where the learned operator achieves the highest median performance while remaining competitive in peak outcomes.

## 1. Introduction

Symbolic programs are a natural representation for policies and decision rules in program synthesis, control, and algorithmic trading: they are interpretable, compositional, and amenable to grammatical and type-based constraints. A persistent challenge for Genetic Programming (GP), however, is *locality*. Small syntactic edits—such as operator changes or subtree replacements—can induce large, unpredictable behavioral shifts, degrading stability, credit assignment, and sample efficiency. As a result, evolutionary search often expends substantial evaluation budget before discovering useful solutions.

Embedding programs into a continuous search space offers a potential remedy, as it enables incremental variation through small latent perturbations. However, continuous search is only effective when the representation provides a reliable correspondence between *latent distance* and *behavioral change*. When this link is weak, even powerful optimizers struggle: inefficiency arises not from the evolutionary loop itself, but from a mismatch between how variation is applied and how program behavior responds.

We therefore focus on *latent behavioral geometry*: the relationship between movements in latent space and changes in decoded program behavior. Continuous variation is meaningful only within regions where small perturbations produce small, predictable behavioral effects. Outside these regions, decoding failures and unintended cross-talk between program components can render search unstable and inefficient. Understanding and exploiting this geometry is essential for designing effective mutation operators.

Our approach is to make latent behavioral geometry explicit and measurable, then leverage it to design mutation operators under a *fixed* evolutionary algorithm. We first characterize locality using controlled latent perturbations, measuring (i) decode validity, (ii) structural change via normalized AST edit distance, and (iii) behavioral change via action-sequence divergence. Together, these diagnostics identify an empirical trust region in which continuous mutations remain valid and behavior-local.

We then exploit this structure using a compact, typed trading-strategy DSL that decomposes each strategy into four semantic components: long entry (LE), short entry (SE), long exit (LX), and short exit (SX). We learn continuous embeddings with a transformer-based VAE whose latent representation is explicitly factorized along these components. Perturbation and swap tests (Section [6](https://arxiv.org/html/2602.07659v1#S6 "6. Disentanglement and Latent Factorization ‣ Continuous Program Search")) verify that this factorization provides reliable, low cross-talk control over decoded behavior.

Rather than mutating all latent dimensions simultaneously, we design structured mutation operators that restrict updates to semantically meaningful subspaces. In particular, we exploit the directional structure of trading strategies by pairing long entry with long exit and short entry with short exit. These paired subspaces correspond to coherent trade lifecycles and enable targeted exploration that avoids incoherent offspring which simultaneously alter unrelated signals.

Finally, we ask whether mutation quality can be improved *within* these semantically constrained subspaces. Instead of sampling isotropic noise, we learn a geometry-compiled mutation operator that predicts behavior-improving update directions from logged evolutionary traces. The resulting flow-based mutation model proposes updates in a single forward pass and is applied only through direction-paired masks. Crucially, it serves as a drop-in replacement for standard mutation: the evolutionary loop, selection mechanism, and evaluation budget remain unchanged.

Across multiple assets and fixed evaluation budgets, this learned operator consistently discovers strong strategies using substantially fewer evaluations and achieves higher median out-of-sample performance than unstructured isotropic mutation. While unrestricted mutation occasionally attains higher peak outcomes, geometry-compiled mutation prioritizes efficiency and reliability, yielding faster and more robust evolutionary search.

#### Contributions.

This paper makes the following contributions:

* •

  Behavioral geometry diagnostics for program latent spaces.
  We introduce practical measurements of decode validity, structural change, and behavioral divergence to identify trust regions for behavior-local continuous variation.
* •

  A symbolic trading DSL enabling semantically aligned embeddings.
  We design a closed, typed language whose decomposition into entry and exit signals supports interpretable, component-aligned latent representations.
* •

  Structured mutation operators under a fixed optimizer.
  We show that restricting mutation to semantically paired subspaces improves search efficiency and reliability relative to isotropic full-latent mutation, without modifying the evolutionary algorithm.
* •

  A learned geometry-compiled mutation operator.
  We propose a flow-based mutation model trained on logged evolutionary traces that achieves faster discovery and higher median performance under identical (μ+λ)(\mu+\lambda) evolution strategies and budgets.

Together, these results demonstrate that aligning mutation structure with latent behavioral geometry can substantially improve the efficiency and robustness of continuous program search without changing the underlying evolutionary algorithm.

## 2. Related Work

Our work sits at the intersection of four areas.
These are Genetic Programming and symbolic policy search, continuous and latent-space evolution, disentangled representation learning, and learned variation operators.
Across these areas, many methods rely on some notion of locality.
Our focus is to make locality behavioral, measurable, and directly usable for operator design.

### 2.1. Genetic Programming and Symbolic Policy Search

Genetic Programming (GP) has a long history of producing interpretable programs for program synthesis, control, and decision-making (Koza, [1992](https://arxiv.org/html/2602.07659v1#bib.bib1 "Genetic programming: on the programming of computers by means of natural selection"); O’Neill, [2009](https://arxiv.org/html/2602.07659v1#bib.bib28 "Riccardo poli, william b. langdon, nicholas f. mcphee: a field guide to genetic programming: lulu. com, 2008, 250 pp, isbn 978-1-4092-0073-4")). A persistent challenge is locality. Small syntactic edits, such as replacing an operator or swapping a subtree, can cause large and hard-to-predict changes in behavior or fitness. This can make evolution unstable and sample-inefficient as programs grow. Many GP systems address this by constraining or structuring the representation. Examples include automatically defined functions (Koza, [1994](https://arxiv.org/html/2602.07659v1#bib.bib3 "Genetic programming ii: automatic discovery of reusable programs")), grammar-guided GP (Whigham, [1995](https://arxiv.org/html/2602.07659v1#bib.bib5 "Grammatically-based genetic programming")), and strongly typed GP (Montana, [1995](https://arxiv.org/html/2602.07659v1#bib.bib7 "Strongly typed genetic programming")). These methods improve validity and can make certain edits safer, but the search space remains discrete, and the behavioral meaning of a small syntactic edit is still difficult to quantify.

Other lines of work attack locality more directly through semantics.
Geometric Semantic GP defines operators in semantic space to induce smoother fitness landscapes (Moraglio et al., [2012](https://arxiv.org/html/2602.07659v1#bib.bib8 "Geometric semantic genetic programming")).
Related work also uses semantic information to shape operators and improve search dynamics (Pawlak et al., [2014](https://arxiv.org/html/2602.07659v1#bib.bib9 "Semantic backpropagation for designing search operators in genetic programming")).
These approaches highlight an important point.
Better locality often comes from aligning variation with what the program does, not only with how it is written.

Our approach targets the same locality problem, but through a continuous representation that we evaluate in behavioral terms.
Instead of proposing a new GP optimizer, we hold the optimizer fixed and study how representation geometry and mutation structure affect behavior.
We then use measured latent-to-behavior relationships to design mutation operators that are targeted, behavior-local, and easy to plug into standard evolutionary loops.

### 2.2. Continuous and Latent-Space Evolution

Evolving solutions in continuous spaces is common in neuroevolution and black-box optimization (Floreano et al., [2008](https://arxiv.org/html/2602.07659v1#bib.bib10 "Neuroevolution: from architectures to learning"); Stanley et al., [2019](https://arxiv.org/html/2602.07659v1#bib.bib11 "Designing neural networks through neuroevolution")).
Evolution strategies and related methods can be effective when small parameter changes lead to reasonably smooth changes in outcomes. Widely used examples include OpenAI-ES (Salimans et al., [2017](https://arxiv.org/html/2602.07659v1#bib.bib13 "Evolution strategies as a scalable alternative to reinforcement learning")) and CMA-ES (Hansen and Ostermeier, [2001](https://arxiv.org/html/2602.07659v1#bib.bib12 "Completely derandomized self-adaptation in evolution strategies")). A few recent papers explore embedding programs into continuous spaces and then optimizing those embeddings.
Neural Program Optimization (NPO) trains an autoencoder for programs and uses a continuous optimizer in the latent space, decoding candidates back to programs during search (Liskowski et al., [2020](https://arxiv.org/html/2602.07659v1#bib.bib15 "Program synthesis as latent continuous optimization: evolutionary search in neural embeddings")).
Lynch et al. (Lynch et al., [2020](https://arxiv.org/html/2602.07659v1#bib.bib17 "Program synthesis in a continuous space using grammars and variational autoencoders")) combine grammars with a variational autoencoder to construct a continuous space of programs, then apply evolutionary search in that space.
These papers demonstrate that latent-space search can work for program synthesis and related tasks (Bontrager et al., [2018](https://arxiv.org/html/2602.07659v1#bib.bib2 "Deepmasterprints: generating masterprints for dictionary attacks via latent variable evolution")).
They also motivate a key practical question.
What does a small latent move actually do to the resulting program?

Our work makes this question explicit and central.
We do not treat the latent space as a black box.
We measure decode validity under perturbation, structural change under perturbation, and behavioral change under perturbation.
This yields an empirical trust region that defines when continuous variation is behaviorally meaningful.
We then hold the optimizer fixed and change only the mutation operator. This isolates the effect of representation geometry and operator design from optimizer tuning.

### 2.3. Disentangled Representations and Structured Latents

Disentangled representation learning aims to separate underlying factors of variation in a way that supports independent control (Bengio et al., [2013](https://arxiv.org/html/2602.07659v1#bib.bib19 "Representation learning: a review and new perspectives")).
In VAEs, common approaches include objectives that encourage factor separation, such as β\beta-VAE (Higgins et al., [2017](https://arxiv.org/html/2602.07659v1#bib.bib20 "Beta-vae: learning basic visual concepts with a constrained variational framework")) and FactorVAE-style methods (Kim and Mnih, [2018](https://arxiv.org/html/2602.07659v1#bib.bib21 "Disentangling by factorising")).
The literature also proposes metrics to quantify disentanglement.
Examples include DCI (Eastwood and Williams, [2018](https://arxiv.org/html/2602.07659v1#bib.bib23 "A framework for the quantitative evaluation of disentangled representations")) and MIG (Chen et al., [2018](https://arxiv.org/html/2602.07659v1#bib.bib22 "Isolating sources of disentanglement in variational autoencoders")), along with critiques that show metrics can disagree and can be brittle in practice (Abdi et al., [2019](https://arxiv.org/html/2602.07659v1#bib.bib6 "A preliminary study of disentanglement with insights on the inadequacy of metrics")).

In many optimization settings, disentanglement is treated as a general quality of the embedding.
The hope is that a better representation will make search easier.
In our setting, we use a more operational notion that is directly tied to mutation.
We build an explicitly block-factorized latent aligned to the four semantic strategy parts in our DSL.
We then test whether perturbing one latent block changes only the corresponding decoded program part, including targeted perturbations and swap tests.
This turns disentanglement into a practical resource for operator design rather than a purely descriptive score.
We do not claim full statistical independence.
Our goal is controllable, behavior-local edits that are useful for evolution.

### 2.4. Learning Variation Operators and Generative Mutation Models

Learning better variation is a long-standing theme in evolutionary computation.
Model-based GP and estimation-of-distribution ideas replace hand-designed mutation with learned sampling mechanisms.
A recent example is Denoising Autoencoder Genetic Programming (DAE-GP).
It uses a denoising autoencoder model to generate new candidate programs, and it studies how the corruption process controls exploration and exploitation (Wittenberg et al., [2023](https://arxiv.org/html/2602.07659v1#bib.bib25 "Denoising autoencoder genetic programming: strategies to control exploration and exploitation in search")). Mutation Models is an earlier approach by Khalifa et al. (Khalifa et al., [2022](https://arxiv.org/html/2602.07659v1#bib.bib4 "Mutation models: learning to generate levels by imitating evolution")) where the mutation function is learned during evolution. This is done by training a small network to learn the mutation function using the evolutionary history while evolution is happening, and then reusing it as the mutation function itself to help direct the search.

We do not learn to generate whole programs directly.
Instead, we learn a conditional distribution over *latent perturbations* inside a measured trust region.
This keeps program validity in the existing decoder and makes the learned model a drop-in replacement for a mutation kernel.
Concretely, we train a conditional flow-based mutation model (Ho et al., [2020](https://arxiv.org/html/2602.07659v1#bib.bib26 "Denoising diffusion probabilistic models"); Song et al., [2021](https://arxiv.org/html/2602.07659v1#bib.bib27 "Denoising diffusion implicit models")) that proposes targeted block-level latent deltas.

## 3. Genetic Programming Trading Language (GPTL)

To study continuous program search in a controlled and reproducible way, we define the *Genetic Programming Trading Language* (GPTL).
GPTL is a small domain-specific language for expressing algorithmic financial trading strategies as symbolic programs.
It serves two purposes.
First, it provides a GP search space with strong safety guarantees.
Second, its structure cleanly separates a strategy into meaningful parts, which later supports a block-factorized continuous representation and block-wise mutation.

### 3.1. Language Design Goals

GPTL was designed with five goals in mind. First, it must be expressive enough to represent a broad set of common technical trading rules, including indicator-based entry and exit logic (a statistical rule-based system that uses price data determine when to buy or sell trades). Second, every generated program must be syntactically and semantically valid. This allows large-scale search without runtime failures caused by malformed programs. Third, program execution must be deterministic and bounded in time and memory. Fourth, programs must have a compact representation that can be embedded by sequence models. Fifth, and most important for this paper, the language must expose a modular strategy structure that makes it possible to treat different parts of a strategy independently during analysis and mutation. To satisfy this final goal, each GPTL strategy is decomposed into four Boolean signal expressions:

* •

  Long Entry (LE): if true, buy-to-enter a long position.
* •

  Short Entry (SE): if true, sell-to-enter a short position.
* •

  Long Exit (LX): if true, sell-to-close an existing long position.
* •

  Short Exit (SX): if true, buy-to-close an existing short position.

This decomposition mirrors the lifecycle of a trading position. It also gives us four clearly defined semantic components that can be represented as separate subtrees and, later, as separate latent blocks.

### 3.2. Syntax, Grammar, and Type System

A GPTL signal is a Boolean expression.
Boolean expressions are built from comparisons between numeric expressions, then combined with logical operators. Numeric expressions are formed from three sources. These are price fields, technical indicator calls, and constants. We use a closed, context-free grammar, which means programs can be parsed deterministically, and no out-of-grammar constructs are allowed. GPTL uses a simple static type system with two primitive types. The Numeric type includes price fields, constants, and indicator outputs. The Boolean type includes comparison results and logical expressions. Relational operators map Numeric inputs to Boolean. Logical operators take Boolean inputs.
No implicit type conversions are allowed. All operators have fixed arity and fixed type signatures. All programs are fully parenthesized during serialization to remove ambiguity. During generation and mutation, we enforce bounds on maximum tree depth and minimum structural complexity. These choices guarantee closure under the language rules. Any generated or mutated program is type-correct, syntactically valid, and executable.

### 3.3. Program Semantics and Execution Model

Programs are evaluated over discrete time series containing OHLCV fields (Open, High, Low, Close, and Volume) and precomputed technical indicators. These fields and values give you an indicator of the current state of the financial market at the given time. At each timestep, the four signals (LE, SE, LX, SX) are evaluated independently to Boolean values. Trading follows a deterministic event-driven model.
A long (short) position is opened when the corresponding entry signal is true and no long (short) position is already open. A position is closed when the corresponding exit signal is true. If multiple signals fire at the same timestep, fixed priority rules ensure deterministic behavior. All orders execute at the next-bar open. Given the same market data and parameters, evaluation is fully deterministic.

### 3.4. Abstract Syntax Tree Representation

Internally, each GPTL strategy is represented as a typed abstract syntax tree (AST).
Leaf nodes correspond to numeric terminals such as price fields and constants.
Internal nodes correspond to indicator calls, relational operators, and logical operators.
The four signal expressions are stored as four disjoint subtrees under dedicated signal roots.
This enables modular discrete mutation in program space and later enables a block-structured continuous representation aligned to the same four components.

### 3.5. Discrete Mutation Operators

GPTL includes a set of type-preserving mutation operators defined over the AST. These operators include subtree replacement, operator mutation, terminal mutation, and insertion or deletion (subjected to depth constraints). All operators preserve syntactic validity, type correctness, and grammar closure by construction. Mutations are local, bounded, and well-defined. They provide a baseline for discrete program-space evolutionary search. They also serve as a reference point for the continuous latent-space mutation operators studied later, which allows us to isolate the effects of representation geometry from the effects of the optimizer.

## 4. Learning Continuous Program Embeddings

To search over programs using continuous mutation, we need a continuous representation of a GPTL strategy. We learn this representation by training a transformer-based variational autoencoder (VAE) that maps a symbolic strategy to a real-valued latent vector and back again.
The model is designed to match the structure of GPTL.
Each strategy is composed of four signals (LE, SE, LX, SX), and our latent representation is explicitly organized into four corresponding latent blocks.
This gives us a representation that is easy to interpret at a high level and is directly usable for block-wise mutation during evolution.

### 4.1. Transformer VAE Architecture

Each GPTL strategy consists of four Boolean signal expressions.
These are long entry (LE), short entry (SE), long exit (LX), and short exit (SX).
We encode and decode each signal separately.
Concretely, each signal expression is serialized into a token sequence and passed through a shared transformer encoder.
The encoder outputs a latent distribution for that signal.
We then concatenate the four signal latents to obtain the full strategy embedding. This process of dividing the latent is called latent factorization.

Let zl​e,zs​e,zl​x,zs​xz\_{le},z\_{se},z\_{lx},z\_{sx} denote the latent vectors for the four signals.
The full strategy latent is

|  |  |  |
| --- | --- | --- |
|  | z=[zl​e,zs​e,zl​x,zs​x]∈ℝdlatenttotal,z=[z\_{le},z\_{se},z\_{lx},z\_{sx}]\in\mathbb{R}^{d\_{\text{latent}}^{\text{total}}}, |  |

where dlatenttotal=4×dlatentsignald\_{\text{latent}}^{\text{total}}=4\times d\_{\text{latent}}^{\text{signal}}.
This block structure aligns the representation with the four semantic components of the strategy and enables block-wise mutation operators during evolutionary search. Token sequences are embedded into a dmodel=512d\_{\text{model}}=512 dimensional space and augmented with sinusoidal positional encodings. The encoder uses four transformer encoder layers.
Each layer contains multi-head self-attention with eight heads and a feedforward network with hidden dimension 1024.
Residual connections, layer normalization, and dropout with probability 0.1 are applied throughout. To produce a single vector per signal, we aggregate the encoder outputs using masked mean pooling over non-padding tokens.
This pooled vector is projected into the parameters of a diagonal Gaussian latent distribution (μ,log⁡σ2)(\mu,\log\sigma^{2}) for that signal. The decoder mirrors the encoder with four transformer decoder layers. Each signal latent vector is projected to the model dimension and provided to the decoder through cross-attention as a single-token memory. We decode autoregressively with causal masking to generate the token sequence corresponding to the GPTL expression. A final linear projection maps decoder states to vocabulary logits.

### 4.2. Tokenization and Serialization

We use a grammar-aware tokenizer tailored to GPTL.
The vocabulary includes special tokens (PAD, SOS, EOS, UNK), logical and relational operators, price fields, indicator names, punctuation symbols, and discretized numeric tokens.
Numeric values are represented with fixed tokens such as <NUM:20> drawn from a bounded set.
All programs are fully parenthesized during serialization to ensure deterministic parsing and remove ambiguity.

### 4.3. Training Procedure

We generate a training set by randomized GPTL program synthesis.
Each strategy contains four independently generated signal trees represented as ASTs. We use a maximum depth of eight and enforce minimum depth constraints and valid operator arity to avoid degenerate expressions. Each generated strategy is compiled and evaluated on historical market data. Strategies that fail to compile or that produce no trades in any walk-forward fold are discarded. This filtering step removes inactive or ill-formed strategies. It does not apply any selection pressure toward profitability or any specific trading behavior. The final dataset contains 20,000 valid strategies. We split it into 80% training and 20% validation using a fixed random seed per model replicate.

#### Objective and optimization.

We train the VAE with teacher forcing using a reconstruction loss plus a KL regularizer,

|  |  |  |
| --- | --- | --- |
|  | ℒ=ℒrecon+β​ℒKL,\mathcal{L}=\mathcal{L}\_{\text{recon}}+\beta\mathcal{L}\_{\text{KL}}, |  |

where ℒrecon\mathcal{L}\_{\text{recon}} is token-level cross-entropy averaged across all four signals, and

|  |  |  |
| --- | --- | --- |
|  | ℒKL=−12​𝔼​[1+log⁡σ2−μ2−σ2].\mathcal{L}\_{\text{KL}}=-\tfrac{1}{2}\mathbb{E}\bigl[1+\log\sigma^{2}-\mu^{2}-\sigma^{2}\bigr]. |  |

We linearly anneal the KL weight β\beta from 0 to 0.1 over the first 50 training epochs to mitigate posterior collapse.

We optimize using a weighted decay Adam optimizer (AdamW) with learning rate 10−410^{-4} and weight decay 10−510^{-5}. We use cosine learning-rate annealing, gradient clipping at norm 1.0, and automatic mixed precision. All models are trained for 50 epochs with a batch size 128.
We retain the checkpoint with the lowest validation loss.

## 5. Latent Quality and Behavioral Geometry Diagnostics

This section answers two questions. First, does the VAE provide a usable continuous representation of programs, and second, when we take a small step in latent space, what happens to the decoded program? These questions determine whether continuous mutation is meaningful and what mutation scales are safe. We tested the quality across different latent dimension sizes by training models with dlatenttotal∈{16,32,64,128,256,512,1024,2048}d\_{\text{latent}}^{\text{total}}\in\{16,32,64,128,256,512,1024,2048\},
where for each latent dimension, we train five independent VAE models using different random initialization seeds.

### 5.1. Latent Quality Across Dimensions

We evaluate VAE quality across the latent-dimension sizes. For each latent size, we train five independent models and report aggregated results. Reconstruction accuracy measures strict round-trip fidelity, counted correctly only if all four signals match exactly after AST canonicalization. Normalized edit distance captures token-level distance between original and reconstruction, averaged across signals. Validity is the fraction of prior samples that decode into executable programs. Uniqueness detects mode collapse; novelty detects memorization. Table [2](https://arxiv.org/html/2602.07659v1#A3.T2 "Table 2 ‣ Appendix C Complete Latent Quality Tables ‣ Continuous Program Search") reveals a capacity trade-off: very small latents reconstruct poorly, very large latents decode less robustly, and intermediate sizes provide the best balance. We use intermediate sizes in subsequent analyses.

### 5.2. Locality and Behavioral Geometry

We measure latent behavioral geometry by asking: if we perturb a latent vector by a controlled amount, how does it change the program’s behavior? For each held-out strategy, we encode using the posterior mean and apply an isotropic Gaussian perturbation,

|  |  |  |
| --- | --- | --- |
|  | z′=z+ϵ​η,η∼𝒩​(0,I),z^{\prime}=z+\epsilon\eta,\quad\eta\sim\mathcal{N}(0,I), |  |

with ϵ∈{0.01,0.05,0.1,0.5,1.0,1.5,2.5,3.0,3.5,5.0}\epsilon\in\{0.01,0.05,0.1,0.5,1.0,1.5,2.5,3.0,3.5,5.0\}. For each perturbed latent, we measure three quantities: decode success (fraction producing valid programs), structural change (normalized AST edit distance), and behavioral change (action-sequence divergence on shared market data).

![Refer to caption](x3.png)


Figure 2. Action-sequence divergence between parent and perturbed strategies. Dark colors indicate behavior-local edits. For ϵ≤0.1\epsilon\leq 0.1, divergence remains low, defining a trust region. Beyond ϵ≥0.5\epsilon\geq 0.5, divergence increases sharply and decoding often fails (gray). This boundary motivates mutation scales in later experiments.

Figure [2](https://arxiv.org/html/2602.07659v1#S5.F2 "Figure 2 ‣ 5.2. Locality and Behavioral Geometry ‣ 5. Latent Quality and Behavioral Geometry Diagnostics ‣ Continuous Program Search") reports behavioral divergence as a function of ϵ\epsilon and latent dimensionality. Decode success and behavioral locality remain high for small perturbations (ϵ≤0.1\epsilon\leq 0.1), indicating that each strategy has a neighborhood where decoding is stable, and behavior changes predictably. Beyond ϵ≥0.5\epsilon\geq 0.5, decode success drops, structural distance grows, and behavioral divergence increases sharply. We treat this transition as an empirical *trust region* for continuous search: inside it, small latent edits yield predictable behavioral refinements; outside, mutations become unreliable. This motivates the geometry-aware operators in  [7.4](https://arxiv.org/html/2602.07659v1#S7.SS4 "7.4. Geometry-Compiled Mutation via Dual-Block Directional Flow (GCM) ‣ 7. Geometry-Aware Mutation Operators under a Fixed Optimizer ‣ Continuous Program Search").

## 6. Disentanglement and Latent Factorization

The mutation operators in this paper rely on a simple idea.
A strategy has four meaningful parts (LE, SE, LX, SX).
Our latent representation is explicitly split into four corresponding blocks.
For block-wise mutation to be reliable, changing one latent block should mainly change the matching strategy part, without unintentionally changing the other three parts.

In this section, we test that this is true in practice.
We treat *latent factorization* as the representation design.
We treat *signal-level disentanglement* as an empirical property of the trained model.
We present two direct tests.
The first asks whether small changes to one latent block stay confined to the intended signal.
The second asks whether we can swap blocks between two strategies and transfer only the corresponding signal.
Together, these tests show that the representation supports predictable, component-level control, which is the key requirement for the mutation operators studied later. These tests both prove disentanglement and zero cross-talk, respectively, and are presented in [D.2](https://arxiv.org/html/2602.07659v1#A4.SS2 "D.2. Signal Disentanglement Test ‣ Appendix D Additional Disentanglement Visualizations ‣ Continuous Program Search")

## 7. Geometry-Aware Mutation Operators under a Fixed Optimizer

This section evaluates three mutation operators for continuous program search. All methods use the same evolutionary loop, the same evaluation budget, and the same program embedding model.
The only difference is how new candidate latents are proposed.
This isolates the effect of mutation design from optimizer choice. All flow-based mutations (GCM) are generated using the inference procedure described in Algorithm [1](https://arxiv.org/html/2602.07659v1#alg1 "Algorithm 1 ‣ Training data and usage. ‣ 7.4. Geometry-Compiled Mutation via Dual-Block Directional Flow (GCM) ‣ 7. Geometry-Aware Mutation Operators under a Fixed Optimizer ‣ Continuous Program Search").

### 7.1. Experimental Setup

All methods use the same (μ+λ)(\mu+\lambda) evolution strategy (ES) in the learned latent space. We fix μ=34\mu=34 and λ=66\lambda=66.
Each run evaluates a total of 13201320 offspring, which corresponds to 100100 generations of λ\lambda offspring. Each candidate latent is decoded into a GPTL program and evaluated by deterministic backtesting. We report out-of-sample Sharpe on held-out test data under a walk-forward protocol explained in the following section. We aggregate results over multiple independent seeds. All mutation operators act in the same 128-dimensional latent space. The isotropic baseline perturbs the full latent vector, while the proposed operator restricts updates to semantically paired entry–exit subspaces corresponding to long-side or short-side trading logic.

### 7.2. Data Splits, Evaluation Protocol, and Trading Assumptions

All experiments use a fixed five-fold walk-forward evaluation protocol spanning 2008–2025. Each fold consists of approximately 2.5 years of training data, followed by a validation window of approximately 6.5 months and an out-of-sample test window of approximately 6 months. A strict 10-day embargo is enforced between consecutive splits to prevent lookahead bias. All reported results are based exclusively on test folds, and the same splits are used across all assets, mutation operators, and random seeds (see Table [3](https://arxiv.org/html/2602.07659v1#A4.T3 "Table 3 ‣ D.2. Signal Disentanglement Test ‣ Appendix D Additional Disentanglement Visualizations ‣ Continuous Program Search")). Strategies are evaluated using a deterministic backtesting engine with an initial equity of $10,000. Only one position may be held at a time, and position scaling is not allowed. Orders execute at the next-bar open with a transaction slippage cost of 0.1% and exchange fees of 0.05% per trade. Experiments are conducted independently on five liquid futures contracts: S&P 500 (ES), Natural Gas (NG), Crude Oil (CL), Silver (SI), and Euro FX (E6). No model selection, hyperparameter tuning, or operator design choices use information from the test folds.

### 7.3. Isotropic Gaussian Mutation

The isotropic baseline applies Gaussian mutation uniformly across the entire latent space. Given a parent latent 𝐳∈ℝ128\mathbf{z}\in\mathbb{R}^{128}, offspring are generated as

|  |  |  |
| --- | --- | --- |
|  | 𝐳′=𝐳+σ​ϵ,ϵ∼𝒩​(𝟎,𝐈128),\mathbf{z}^{\prime}=\mathbf{z}+\sigma\,\boldsymbol{\epsilon},\qquad\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{128}), |  |

so that all 128 latent dimensions are perturbed simultaneously without regard to semantic signal boundaries. This baseline reflects standard practice in latent-space evolutionary search and serves as an unstructured exploration reference.

### 7.4. Geometry-Compiled Mutation via Dual-Block Directional Flow (GCM)

We use the term *geometry-compiled mutation* (GCM) to refer to the general approach of learning behavior-aware mutation proposals from logged evolutionary traces; in this work, GCM is instantiated using a flow-matching model. The isotropic Gaussian baseline perturbs all 128 latent dimensions simultaneously, without regard to trading semantics.
We now introduce a learned mutation operator that restricts updates to semantically meaningful subspaces while improving proposal quality within those subspaces.
We refer to this operator as *geometry-compiled mutation* (GCM).

#### Dual-block directional mutation.

Trading strategies exhibit directional structure: long positions require coordinated entry and exit rules, as do short positions.
Accordingly, we define two direction-paired mutation subspaces.
Long Entry (LE) and Long Exit (LX) form the *long-side* pair, while Short Entry (SE) and Short Exit (SX) form the *short-side* pair.
Let the latent be ordered as

|  |  |  |
| --- | --- | --- |
|  | 𝐳=[𝐳(LE),𝐳(SE),𝐳(LX),𝐳(SX)]∈ℝ128,\mathbf{z}=[\mathbf{z}^{(\mathrm{LE})},\mathbf{z}^{(\mathrm{SE})},\mathbf{z}^{(\mathrm{LX})},\mathbf{z}^{(\mathrm{SX})}]\in\mathbb{R}^{128}, |  |

with each block in ℝ32\mathbb{R}^{32}.
We define two non-contiguous binary masks,

|  |  |  |
| --- | --- | --- |
|  | 𝐦long=[𝟏32,𝟎32,𝟏32,𝟎32],𝐦short=[𝟎32,𝟏32,𝟎32,𝟏32],\mathbf{m}\_{\text{long}}=[\mathbf{1}\_{32},\mathbf{0}\_{32},\mathbf{1}\_{32},\mathbf{0}\_{32}],\qquad\mathbf{m}\_{\text{short}}=[\mathbf{0}\_{32},\mathbf{1}\_{32},\mathbf{0}\_{32},\mathbf{1}\_{32}], |  |

which activate the long-side and short-side subspaces respectively.
At each generation, the mutation direction alternates deterministically between these two masks.

#### Learned mutation proposal.

Rather than sampling isotropic noise within the active subspace, GCM uses a learned flow-matching model to predict a behavior-improving update direction.
The model predicts a velocity field

|  |  |  |
| --- | --- | --- |
|  | 𝐯θ​(𝐳,ϕ)∈ℝ128,\mathbf{v}\_{\theta}(\mathbf{z},\boldsymbol{\phi})\in\mathbb{R}^{128}, |  |

conditioned on the full parent latent 𝐳\mathbf{z} and an 8-dimensional behavioral embedding ϕ\boldsymbol{\phi} computed from the parent strategy’s execution trace.
Unlike diffusion-based approaches, this formulation requires no iterative denoising or timestep conditioning: the update direction is predicted in a single forward pass.

At search time, the predicted velocity is applied only through the active direction-paired mask,

|  |  |  |
| --- | --- | --- |
|  | 𝐳′=𝐳+α​𝐦d​(g)⊙𝐯θ​(𝐳,ϕ)+𝜼,𝜼∼𝐦d​(g)⊙𝒩​(𝟎,σ2​𝐈),\mathbf{z}^{\prime}=\mathbf{z}+\alpha\,\mathbf{m}\_{d(g)}\odot\mathbf{v}\_{\theta}(\mathbf{z},\boldsymbol{\phi})+\boldsymbol{\eta},\qquad\boldsymbol{\eta}\sim\mathbf{m}\_{d(g)}\odot\mathcal{N}(\mathbf{0},\sigma^{2}\mathbf{I}), |  |

where d​(g)∈{long,short}d(g)\in\{\text{long},\text{short}\} denotes the active direction at generation gg.
Dual-block mutation updates 64 of the 128 latent dimensions per generation, focusing exploration on a coherent trade lifecycle rather than perturbing all signals simultaneously.

#### Training data and usage.

The flow model is trained offline using logged mutation traces collected under the same (μ+λ)(\mu+\lambda) evolution strategy used in our main experiments, but with isotropic Gaussian mutation as the proposal mechanism.
We collect traces across five assets and five independent runs per asset.
Each run evaluates λ=66\lambda=66 offspring per generation for 100100 generations, yielding 66006600 mutation attempts per run.
Each mutation record contains the parent latent 𝐳\mathbf{z}, the child latent 𝐳′\mathbf{z}^{\prime}, the associated behavioral embedding ϕ\boldsymbol{\phi}, validity flags, and parent and child fitness values.
During evolution, GCM is used solely as a drop-in replacement for the mutation kernel; the optimizer, evaluation budget, and selection procedure remain unchanged. Algorithm [1](https://arxiv.org/html/2602.07659v1#alg1 "Algorithm 1 ‣ Training data and usage. ‣ 7.4. Geometry-Compiled Mutation via Dual-Block Directional Flow (GCM) ‣ 7. Geometry-Aware Mutation Operators under a Fixed Optimizer ‣ Continuous Program Search") summarizes the inference-time mutation procedure used by the geometry-compiled flow operator within the (μ+λ)(\mu+\lambda) evolution strategy.

Algorithm 1  DBD-Flow mutation (inference-time) within (μ+λ)(\mu+\lambda)-ES

0: Flow model Fθ​(𝐳,ϕ)→𝜹fullF\_{\theta}(\mathbf{z},\boldsymbol{\phi})\rightarrow\boldsymbol{\delta}\_{\text{full}} (predicts a 128-dim improvement delta)

0: Parent latent 𝐳∈ℝ128\mathbf{z}\in\mathbb{R}^{128}, behavioral embedding ϕ∈ℝ8\boldsymbol{\phi}\in\mathbb{R}^{8}, generation index gg

0: Delta scale α\alpha (default 1.01.0), input noise σin\sigma\_{\text{in}} (default 0.00.0), output noise σout\sigma\_{\text{out}} (default 0.00.0)

0: Masks 𝐦long=[𝟏32,𝟎32,𝟏32,𝟎32]\mathbf{m}\_{\text{long}}=[\mathbf{1}\_{32},\mathbf{0}\_{32},\mathbf{1}\_{32},\mathbf{0}\_{32}] and 𝐦short=[𝟎32,𝟏32,𝟎32,𝟏32]\mathbf{m}\_{\text{short}}=[\mathbf{0}\_{32},\mathbf{1}\_{32},\mathbf{0}\_{32},\mathbf{1}\_{32}]

0: Mutated latent 𝐳′∈ℝ128\mathbf{z}^{\prime}\in\mathbb{R}^{128}

1: Select direction-paired mask:

2: if gmod2=0g\bmod 2=0 then

3:  𝐦←𝐦long\mathbf{m}\leftarrow\mathbf{m}\_{\text{long}} {Mutate (LE, LX)}

4: else

5:  𝐦←𝐦short\mathbf{m}\leftarrow\mathbf{m}\_{\text{short}} {Mutate (SE, SX)}

6: end if

7: Optional input exploration:

8: Sample ϵ∼𝒩​(𝟎,𝐈128)\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{128})

9: 𝐳~←𝐳+σin​ϵ\tilde{\mathbf{z}}\leftarrow\mathbf{z}+\sigma\_{\text{in}}\boldsymbol{\epsilon}

10: Predict full delta (one forward pass):

11: 𝜹full←Fθ​(𝐳~,ϕ)\boldsymbol{\delta}\_{\text{full}}\leftarrow F\_{\theta}(\tilde{\mathbf{z}},\boldsymbol{\phi})

12: Mask to the active direction-paired subspace:

13: 𝜹masked←𝐦⊙𝜹full\boldsymbol{\delta}\_{\text{masked}}\leftarrow\mathbf{m}\odot\boldsymbol{\delta}\_{\text{full}}

14: Optional output noise (active blocks only):

15: Sample ϵ′∼𝒩​(𝟎,𝐈128)\boldsymbol{\epsilon}^{\prime}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{128})

16: 𝜹←α​𝜹masked+σout​(𝐦⊙ϵ′)\boldsymbol{\delta}\leftarrow\alpha\,\boldsymbol{\delta}\_{\text{masked}}+\sigma\_{\text{out}}(\mathbf{m}\odot\boldsymbol{\epsilon}^{\prime})

17: Apply mutation:

18: 𝐳′←𝐳+𝜹\mathbf{z}^{\prime}\leftarrow\mathbf{z}+\boldsymbol{\delta}

19: return 𝐳′\mathbf{z}^{\prime}

### 7.5. Controlled Comparison

We compare mutation operators under identical (μ+λ)(\mu+\lambda) evolution strategy settings, evaluation budgets, and deterministic seeds to isolate the effect of mutation design.
Specifically, we evaluate:

1. (1)

   Isotropic Gaussian mutation, which perturbs all 128 latent dimensions simultaneously without regard to semantic structure;
2. (2)

   Dual-block Gaussian mutation, which restricts updates to semantically paired entry–exit subspaces (long-side or short-side) using isotropic noise;
3. (3)

   Geometry-compiled mutation (GCM), which uses a learned flow-based model to propose update directions within the same dual-block subspaces.

All methods are evaluated across five assets using the same evaluation budget.
Results are reported exclusively on out-of-sample test folds.
Table [1](https://arxiv.org/html/2602.07659v1#S7.T1 "Table 1 ‣ 7.5. Controlled Comparison ‣ 7. Geometry-Aware Mutation Operators under a Fixed Optimizer ‣ Continuous Program Search") summarizes median and maximum Sharpe ratios along with evaluation budget usage.

Table 1. Median and maximum out-of-sample Sharpe ratios and evaluation budget usage across all assets. Lower values of Pct. Budget Used indicate faster discovery of strong solutions.

| Method | Median Sharpe | Max Sharpe | Pct. Budget Used |
| --- | --- | --- | --- |
| Flow (GCM) | 1.152 | 1.518 | 13.7 |
| Isotropic | 1.005 | 1.607 | 88.5 |
| Dual-block | 0.890 | 1.941 | 100.0 |

### 7.6. Interpretation

The results reveal a clear trade-off between unstructured exploration and semantically aligned mutation.
Isotropic Gaussian mutation occasionally attains high peak Sharpe values, but typically requires most of the evaluation budget and exhibits high variance across runs.
In contrast, restricting mutation to semantically meaningful entry–exit subspaces substantially improves search efficiency and reliability.

The learned geometry-compiled mutation operator achieves the highest median out-of-sample Sharpe while using an order of magnitude less evaluation budget than both isotropic and dual-block Gaussian baselines. This indicates that learning behavior-aware mutation directions prioritizes consistent improvement over rare, high-variance outcomes.
Although GCM does not always achieve the highest absolute Sharpe, it discovers strong strategies much earlier and with greater consistency across assets and seeds.

Taken together, these results show that the primary benefit of geometry-aware mutation lies in faster and more reliable discovery rather than extreme peak optimization.

## 8. Discussion

This work examines continuous program search through the lens of *latent behavioral geometry*. Rather than assuming that continuous embeddings yield smooth or well-behaved search landscapes, we explicitly measure how latent perturbations translate into decoded program behavior. These measurements identify trust regions in which continuous mutation remains valid and behavior-local, providing a principled basis for mutation operator design.

Our results show that performance differences arise primarily from how mutation operators interact with this geometry, not from changes to the evolutionary optimizer. Unstructured isotropic mutation perturbs all signals simultaneously, often producing incoherent edits and requiring large evaluation budgets. Restricting mutation to semantically aligned entry–exit subspaces substantially improves efficiency by focusing exploration on coherent trade lifecycles. Learning mutation directions within these subspaces further accelerates discovery by biasing search toward behaviorally meaningful changes.

Importantly, the learned operator replaces only the mutation kernel. Selection, evaluation, and population dynamics are unchanged. The resulting gains therefore reflect more effective use of limited evaluation budgets rather than increased optimizer complexity or computational effort. While our experiments are conducted in a trading domain, the underlying principles are more general. Many GP systems rely on mutation operators whose behavioral effects are difficult to predict. Our results suggest that measuring latent behavioral geometry and aligning mutation structure with known semantic decompositions can significantly improve the efficiency and reliability of evolutionary search.

There are limitations to this approach. Our DSL admits a clear semantic decomposition into entry and exit signals; other domains may require different representations. Continuous mutation remains effective only within trust regions that preserve validity, limiting exploration radius. Extending these ideas to domains without obvious semantic partitions remains an important direction for future work.

## 9. Conclusion

Continuous program embeddings are only useful when small latent changes correspond to small, interpretable behavioral effects.
Rather than assuming this property, we measured it directly using controlled perturbations that track decode validity, structural change, and behavioral divergence. These diagnostics identify trust regions where continuous mutation is reliable.

We used this information to design semantically aligned mutation operators under a fixed evolutionary algorithm.
Restricting mutation to paired entry-exit subspaces improves efficiency and reliability relative to isotropic full-latent mutation. Learning geometry-compiled mutation directions within these subspaces further accelerates discovery, yielding higher median out-of-sample performance while using substantially less evaluation budget. The central takeaway is that aligning mutation structure with latent behavioral geometry can trade rare peak outcomes for faster, more robust evolutionary search—without modifying the underlying evolutionary algorithm.

## References

* A. H. Abdi, P. Abolmaesumi, and S. Fels (2019)
  A preliminary study of disentanglement with insights on the inadequacy of metrics.
  arXiv preprint arXiv:1911.11791.
  Cited by: [§2.3](https://arxiv.org/html/2602.07659v1#S2.SS3.p1.1 "2.3. Disentangled Representations and Structured Latents ‣ 2. Related Work ‣ Continuous Program Search").
* Y. Bengio, A. Courville, and P. Vincent (2013)
  Representation learning: a review and new perspectives.
  IEEE Transactions on Pattern Analysis and Machine Intelligence 35 (8),  pp. 1798–1828.
  Cited by: [§2.3](https://arxiv.org/html/2602.07659v1#S2.SS3.p1.1 "2.3. Disentangled Representations and Structured Latents ‣ 2. Related Work ‣ Continuous Program Search").
* P. Bontrager, A. Roy, J. Togelius, N. Memon, and A. Ross (2018)
  Deepmasterprints: generating masterprints for dictionary attacks via latent variable evolution.
  In 2018 IEEE 9th International Conference on Biometrics Theory, Applications and Systems (BTAS),
   pp. 1–9.
  Cited by: [§2.2](https://arxiv.org/html/2602.07659v1#S2.SS2.p1.1 "2.2. Continuous and Latent-Space Evolution ‣ 2. Related Work ‣ Continuous Program Search").
* R. T. Q. Chen, X. Li, R. B. Grosse, and D. K. Duvenaud (2018)
  Isolating sources of disentanglement in variational autoencoders.
  Advances in Neural Information Processing Systems 31.
  Cited by: [§2.3](https://arxiv.org/html/2602.07659v1#S2.SS3.p1.1 "2.3. Disentangled Representations and Structured Latents ‣ 2. Related Work ‣ Continuous Program Search").
* C. Eastwood and C. K. I. Williams (2018)
  A framework for the quantitative evaluation of disentangled representations.
  In International Conference on Learning Representations,
  Cited by: [§2.3](https://arxiv.org/html/2602.07659v1#S2.SS3.p1.1 "2.3. Disentangled Representations and Structured Latents ‣ 2. Related Work ‣ Continuous Program Search").
* D. Floreano, P. Dürr, and C. Mattiussi (2008)
  Neuroevolution: from architectures to learning.
  Evolutionary Intelligence 1 (1),  pp. 47–62.
  Cited by: [§2.2](https://arxiv.org/html/2602.07659v1#S2.SS2.p1.1 "2.2. Continuous and Latent-Space Evolution ‣ 2. Related Work ‣ Continuous Program Search").
* N. Hansen and A. Ostermeier (2001)
  Completely derandomized self-adaptation in evolution strategies.
  Evolutionary Computation 9 (2),  pp. 159–195.
  Cited by: [§2.2](https://arxiv.org/html/2602.07659v1#S2.SS2.p1.1 "2.2. Continuous and Latent-Space Evolution ‣ 2. Related Work ‣ Continuous Program Search").
* I. Higgins, L. Matthey, A. Pal, C. Burgess, X. Glorot, M. Botvinick, S. Mohamed, and A. Lerchner (2017)
  Beta-vae: learning basic visual concepts with a constrained variational framework.
  In International Conference on Learning Representations,
  Cited by: [§2.3](https://arxiv.org/html/2602.07659v1#S2.SS3.p1.1 "2.3. Disentangled Representations and Structured Latents ‣ 2. Related Work ‣ Continuous Program Search").
* J. Ho, A. Jain, and P. Abbeel (2020)
  Denoising diffusion probabilistic models.
  In Advances in Neural Information Processing Systems,
  Vol. 33.
  Cited by: [§2.4](https://arxiv.org/html/2602.07659v1#S2.SS4.p2.1 "2.4. Learning Variation Operators and Generative Mutation Models ‣ 2. Related Work ‣ Continuous Program Search").
* A. Khalifa, J. Togelius, and M. C. Green (2022)
  Mutation models: learning to generate levels by imitating evolution.
  In Proceedings of the 17th International Conference on the Foundations of Digital Games,
   pp. 1–9.
  Cited by: [§2.4](https://arxiv.org/html/2602.07659v1#S2.SS4.p1.1 "2.4. Learning Variation Operators and Generative Mutation Models ‣ 2. Related Work ‣ Continuous Program Search").
* H. Kim and A. Mnih (2018)
  Disentangling by factorising.
  In International Conference on Machine Learning,
   pp. 2649–2658.
  Cited by: [§2.3](https://arxiv.org/html/2602.07659v1#S2.SS3.p1.1 "2.3. Disentangled Representations and Structured Latents ‣ 2. Related Work ‣ Continuous Program Search").
* J. R. Koza (1992)
  Genetic programming: on the programming of computers by means of natural selection.
   MIT Press, Cambridge, MA.
  Cited by: [§2.1](https://arxiv.org/html/2602.07659v1#S2.SS1.p1.1 "2.1. Genetic Programming and Symbolic Policy Search ‣ 2. Related Work ‣ Continuous Program Search").
* J. R. Koza (1994)
  Genetic programming ii: automatic discovery of reusable programs.
   MIT Press, Cambridge, MA.
  Cited by: [§2.1](https://arxiv.org/html/2602.07659v1#S2.SS1.p1.1 "2.1. Genetic Programming and Symbolic Policy Search ‣ 2. Related Work ‣ Continuous Program Search").
* P. Liskowski, K. Krawiec, N. E. Toklu, and J. Swan (2020)
  Program synthesis as latent continuous optimization: evolutionary search in neural embeddings.
  In Proceedings of the 2020 Genetic and Evolutionary Computation Conference,
   pp. 359–367.
  External Links: [Document](https://dx.doi.org/10.1145/3377930.3390213)
  Cited by: [§2.2](https://arxiv.org/html/2602.07659v1#S2.SS2.p1.1 "2.2. Continuous and Latent-Space Evolution ‣ 2. Related Work ‣ Continuous Program Search").
* D. Lynch, J. McDermott, and M. O’Neill (2020)
  Program synthesis in a continuous space using grammars and variational autoencoders.
  In Parallel Problem Solving from Nature (PPSN XVI),
  Lecture Notes in Computer Science, Vol. 12270,  pp. 33–47.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-030-58115-2%5F3)
  Cited by: [§2.2](https://arxiv.org/html/2602.07659v1#S2.SS2.p1.1 "2.2. Continuous and Latent-Space Evolution ‣ 2. Related Work ‣ Continuous Program Search").
* D. J. Montana (1995)
  Strongly typed genetic programming.
  Evolutionary Computation 3 (2),  pp. 199–230.
  Cited by: [§2.1](https://arxiv.org/html/2602.07659v1#S2.SS1.p1.1 "2.1. Genetic Programming and Symbolic Policy Search ‣ 2. Related Work ‣ Continuous Program Search").
* A. Moraglio, K. Krawiec, and C. G. Johnson (2012)
  Geometric semantic genetic programming.
  In Parallel Problem Solving from Nature (PPSN),
   pp. 21–31.
  Cited by: [§2.1](https://arxiv.org/html/2602.07659v1#S2.SS1.p2.1 "2.1. Genetic Programming and Symbolic Policy Search ‣ 2. Related Work ‣ Continuous Program Search").
* M. O’Neill (2009)
  Riccardo poli, william b. langdon, nicholas f. mcphee: a field guide to genetic programming: lulu. com, 2008, 250 pp, isbn 978-1-4092-0073-4.
   Springer.
  Cited by: [§2.1](https://arxiv.org/html/2602.07659v1#S2.SS1.p1.1 "2.1. Genetic Programming and Symbolic Policy Search ‣ 2. Related Work ‣ Continuous Program Search").
* T. P. Pawlak, B. Wieloch, and K. Krawiec (2014)
  Semantic backpropagation for designing search operators in genetic programming.
  IEEE Transactions on Evolutionary Computation 19 (3),  pp. 326–340.
  Cited by: [§2.1](https://arxiv.org/html/2602.07659v1#S2.SS1.p2.1 "2.1. Genetic Programming and Symbolic Policy Search ‣ 2. Related Work ‣ Continuous Program Search").
* T. Salimans, J. Ho, X. Chen, S. Sidor, and I. Sutskever (2017)
  Evolution strategies as a scalable alternative to reinforcement learning.
  arXiv preprint arXiv:1703.03864.
  Cited by: [§2.2](https://arxiv.org/html/2602.07659v1#S2.SS2.p1.1 "2.2. Continuous and Latent-Space Evolution ‣ 2. Related Work ‣ Continuous Program Search").
* J. Song, C. Meng, and S. Ermon (2021)
  Denoising diffusion implicit models.
  In International Conference on Learning Representations,
  Cited by: [§2.4](https://arxiv.org/html/2602.07659v1#S2.SS4.p2.1 "2.4. Learning Variation Operators and Generative Mutation Models ‣ 2. Related Work ‣ Continuous Program Search").
* K. O. Stanley, J. Clune, J. Lehman, and R. Miikkulainen (2019)
  Designing neural networks through neuroevolution.
  Nature Machine Intelligence 1 (1),  pp. 24–35.
  Cited by: [§2.2](https://arxiv.org/html/2602.07659v1#S2.SS2.p1.1 "2.2. Continuous and Latent-Space Evolution ‣ 2. Related Work ‣ Continuous Program Search").
* P. A. Whigham (1995)
  Grammatically-based genetic programming.
  In Proceedings of the Workshop on Genetic Programming: From Theory to Real-World Applications,
  Cited by: [§2.1](https://arxiv.org/html/2602.07659v1#S2.SS1.p1.1 "2.1. Genetic Programming and Symbolic Policy Search ‣ 2. Related Work ‣ Continuous Program Search").
* D. Wittenberg, F. Rothlauf, and C. Gagné (2023)
  Denoising autoencoder genetic programming: strategies to control exploration and exploitation in search.
  Genetic Programming and Evolvable Machines 24 (2),  pp. 17.
  Cited by: [§2.4](https://arxiv.org/html/2602.07659v1#S2.SS4.p1.1 "2.4. Learning Variation Operators and Generative Mutation Models ‣ 2. Related Work ‣ Continuous Program Search").

## Appendix A Appendix

The appendices provide full technical details necessary for reproducibility and to support the empirical claims made in the main paper. All experiments can be reproduced using the specifications, datasets, and hyperparameters described below.

## Appendix B Full GPTL Grammar and Mutation Specifications

### B.1. Complete Grammar

GPTL programs are composed of four Boolean signal expressions (LE, SE, LX, SX), each defined by the following context-free grammar:

```
signal          ::= expr

expr            ::= expr ’&’ expr
                  | expr ’|’ expr
                  | ’~’ expr
                  | comparison

comparison      ::= numeric_expr relop numeric_expr
relop           ::= ’>’ | ’<’ | ’>=’ | ’<=’ | ’==’

numeric_expr    ::= indicator_call | field | constant
indicator_call  ::= IND ’(’ field ’,’ INT ’)’

field           ::= open | high | low | close | volume
constant        ::= FLOAT
```

All expressions are fully parenthesized during serialization. Operator precedence is fixed as NOT >> AND >> OR. The grammar is closed and guarantees syntactic validity.

### B.2. Static Typing Rules

GPTL enforces a strict static type system with two primitive types:

* •

  Numeric: price fields, constants, indicator outputs
* •

  Boolean: comparison results and logical expressions

Typing rules prohibit implicit coercions. All operators have fixed arity and type signatures, ensuring closure under mutation.

### B.3. Mutation Operators

All discrete mutation operators are type-preserving and grammar-safe:

* •

  Subtree replacement: Replace a randomly selected subtree with a newly sampled compatible subtree.
* •

  Operator mutation: Replace a logical or comparison operator with another operator of the same arity and type.
* •

  Terminal mutation: Resample numeric constants or indicator parameters within predefined bounds.
* •

  Insertion/deletion: Insert or remove subtrees subject to maximum depth constraints.

All mutations preserve syntactic validity, type correctness, and bounded execution.

### B.4. Program Dataset Generation

The GPTL training dataset is generated via randomized program synthesis. Each strategy consists of four independently generated signal trees with:

* •

  maximum AST depth: 8
* •

  minimum depth: 2
* •

  bounded numeric constants and indicator periods

Programs are compiled and evaluated on historical data. Strategies that fail to compile or produce zero trades in any walk-forward fold are discarded. No selection pressure toward profitability is applied.

## Appendix C Complete Latent Quality Tables

Table [2](https://arxiv.org/html/2602.07659v1#A3.T2 "Table 2 ‣ Appendix C Complete Latent Quality Tables ‣ Continuous Program Search") reports the full latent quality metrics across all evaluated latent dimensions, including reconstruction accuracy, normalized edit distance, consistency, validity, uniqueness, and novelty. Results are aggregated across five independently trained VAE models per dimension.

Table 2. Complete latent quality metrics across latent dimensionalities.

| Latent Dim. | Recon. Acc. | Norm. Edit Dist. | Consistency | Validity | Uniqueness | Novelty |
| --- | --- | --- | --- | --- | --- | --- |
| 16 | 0.006 ±\pm 0.003 | 0.746 ±\pm 0.022 | 1.000 ±\pm 0.000 | 0.896 ±\pm 0.021 | 0.991 ±\pm 0.006 | 0.952 ±\pm 0.010 |
| 32 | 0.057 ±\pm 0.007 | 0.596 ±\pm 0.017 | 1.000 ±\pm 0.000 | 0.954 ±\pm 0.019 | 0.999 ±\pm 0.001 | 0.965 ±\pm 0.009 |
| 64 | 0.242 ±\pm 0.016 | 0.385 ±\pm 0.008 | 1.000 ±\pm 0.000 | 0.975 ±\pm 0.014 | 1.000 ±\pm 0.000 | 0.977 ±\pm 0.005 |
| 128 | 0.414 ±\pm 0.012 | 0.289 ±\pm 0.007 | 1.000 ±\pm 0.000 | 0.978 ±\pm 0.007 | 1.000 ±\pm 0.000 | 0.974 ±\pm 0.005 |
| 256 | 0.446 ±\pm 0.017 | 0.278 ±\pm 0.009 | 1.000 ±\pm 0.000 | 0.942 ±\pm 0.025 | 1.000 ±\pm 0.000 | 0.983 ±\pm 0.008 |
| 512 | 0.496 ±\pm 0.008 | 0.280 ±\pm 0.003 | 1.000 ±\pm 0.000 | 0.926 ±\pm 0.021 | 1.000 ±\pm 0.000 | 0.991 ±\pm 0.007 |
| 1024 | 0.504 ±\pm 0.024 | 0.271 ±\pm 0.006 | 1.000 ±\pm 0.000 | 0.909 ±\pm 0.040 | 1.000 ±\pm 0.000 | 0.996 ±\pm 0.004 |
| 2048 | 0.519 ±\pm 0.010 | 0.270 ±\pm 0.003 | 1.000 ±\pm 0.000 | 0.893 ±\pm 0.029 | 1.000 ±\pm 0.000 | 1.000 ±\pm 0.000 |

## Appendix D Additional Disentanglement Visualizations

This appendix includes additional heatmaps and visualizations supporting Section 6, including:

* •

  Signal disentanglement heatmaps across multiple latent dimensions
* •

  Swap test results for all signal pairs
* •

  Sensitivity of disentanglement metrics to perturbation scale

All visualizations are computed using the same evaluation protocols described in the main text.

### D.1. Behavioral Embedding Φ\Phi and Trust-Region Binning

GCM conditions on a compact, interpretable behavioral embedding Φ​(⋅)∈ℝ8\Phi(\cdot)\in\mathbb{R}^{8} computed from a strategy’s execution trace under deterministic backtesting.
Let TT denote the number of evaluated bars in the backtest window.
Let post∈{−1,0,1}\text{pos}\_{t}\in\{-1,0,1\} denote the position at time tt, where 11 indicates long, −1-1 indicates short, and 0 indicates flat.

#### Market regime.

We define a simple market regime indicator using a 100-bar moving average of the close price.
Let ctc\_{t} be the close at time tt and let MA100​(c)t\text{MA}\_{100}(c)\_{t} be the 100-bar moving average.
We define

|  |  |  |
| --- | --- | --- |
|  | rt=𝕀​[ct>MA100​(c)t],r\_{t}=\mathbb{I}\left[c\_{t}>\text{MA}\_{100}(c)\_{t}\right], |  |

where rt=1r\_{t}=1 indicates an up regime and rt=0r\_{t}=0 indicates a down regime.
We compute all regime-based features over timesteps where MA100\text{MA}\_{100} is defined.

#### Regime exposure features.

Define indicators ℓt=𝕀​[post>0]\ell\_{t}=\mathbb{I}[\text{pos}\_{t}>0] and st=𝕀​[post<0]s\_{t}=\mathbb{I}[\text{pos}\_{t}<0].
The first four components of Φ\Phi measure the fraction of time spent in long or short positions during up or down regimes

|  |  |  |
| --- | --- | --- |
|  | ϕ1=1T​∑t=1Tℓt​(1−rt),ϕ2=1T​∑t=1Tst​(1−rt),\phi\_{1}=\frac{1}{T}\sum\_{t=1}^{T}\ell\_{t}(1-r\_{t}),\quad\phi\_{2}=\frac{1}{T}\sum\_{t=1}^{T}s\_{t}(1-r\_{t}), |  |

|  |  |  |
| --- | --- | --- |
|  | ϕ3=1T​∑t=1Tℓt​rt,ϕ4=1T​∑t=1Tst​rt.\phi\_{3}=\frac{1}{T}\sum\_{t=1}^{T}\ell\_{t}r\_{t},\quad\phi\_{4}=\frac{1}{T}\sum\_{t=1}^{T}s\_{t}r\_{t}. |  |

#### Event statistics.

We define an entry event as a transition from flat to non-flat.
We define an exit event as a transition from non-flat to flat.
Let NentryN\_{\text{entry}} be the number of entry events and NexitN\_{\text{exit}} be the number of exit events.
We define normalized entry and exit rates

|  |  |  |
| --- | --- | --- |
|  | ϕ5=NentryT,ϕ6=NexitT.\phi\_{5}=\frac{N\_{\text{entry}}}{T},\quad\phi\_{6}=\frac{N\_{\text{exit}}}{T}. |  |

We also compute hold durations in bars for each completed trade.
Let {hj}j=1J\{h\_{j}\}\_{j=1}^{J} be the set of hold durations for JJ completed trades.
We define normalized hold statistics

|  |  |  |
| --- | --- | --- |
|  | ϕ7=mean​({hj})T,ϕ8=std​({hj})T.\phi\_{7}=\frac{\text{mean}(\{h\_{j}\})}{T},\quad\phi\_{8}=\frac{\text{std}(\{h\_{j}\})}{T}. |  |

#### Behavioral step size, ρ\rho bins, and trust region.

Given a parent strategy and a decoded child strategy, we compute

|  |  |  |
| --- | --- | --- |
|  | ϕL​2=‖Φ​(child)−Φ​(parent)‖2.\phi\_{L2}=\left\lVert\Phi(\text{child})-\Phi(\text{parent})\right\rVert\_{2}. |  |

We discretize ϕL​2\phi\_{L2} into a four-level bin ρ\rho using fixed thresholds

|  |  |  |
| --- | --- | --- |
|  | ρ={tinyϕL​2∈[0,0.05)smallϕL​2∈[0.05,0.15)mediumϕL​2∈[0.15,0.35)largeϕL​2∈[0.35,∞).\rho=\begin{cases}\texttt{tiny}&\phi\_{L2}\in[0,0.05)\\ \texttt{small}&\phi\_{L2}\in[0.05,0.15)\\ \texttt{medium}&\phi\_{L2}\in[0.15,0.35)\\ \texttt{large}&\phi\_{L2}\in[0.35,\infty).\end{cases} |  |

We define the behavioral trust region as ϕL​2≤0.35\phi\_{L2}\leq 0.35.
GCM is trained on mutations within this trust region so that the learned operator focuses on behavior-local edits.
At inference time we typically request ρ=small\rho=\texttt{small} to remain within the empirically stable locality regime.

### D.2. Signal Disentanglement Test

The goal of this test is straightforward. We perturb one latent block and check whether the decoded program changes only in the matching signal expression. For a held-out set of encoded strategies, we use the block-factorized latent representation

|  |  |  |
| --- | --- | --- |
|  | z=[zl​e,zs​e,zl​x,zs​x],z=[z\_{le},z\_{se},z\_{lx},z\_{sx}], |  |

corresponding to long entry (LE), short entry (SE), long exit (LX), and short exit (SX).
For each strategy and each latent block zkz\_{k}, we perturb only that block,

|  |  |  |
| --- | --- | --- |
|  | zk′=zk+ϵ​η,η∼𝒩​(0,I),z^{\prime}\_{k}=z\_{k}+\epsilon\eta,\quad\eta\sim\mathcal{N}(0,I), |  |

and keep the other three blocks fixed.
We use ϵ=0.1\epsilon=0.1.
This value lies within the trust-region regime identified in Section [5.2](https://arxiv.org/html/2602.07659v1#S5.SS2 "5.2. Locality and Behavioral Geometry ‣ 5. Latent Quality and Behavioral Geometry Diagnostics ‣ Continuous Program Search").
Each perturbed latent is decoded using greedy decoding. For each perturbation, we compute the normalized token-level edit distance between the original and perturbed programs separately for each of the four signals. From these per-signal edit distances, we compute two summary metrics. Cross-talk is the fraction of total observed change that appears in *non-target* signals.
The target-only rate is the fraction of perturbations for which all observed changes are confined to the intended signal. Figure [3](https://arxiv.org/html/2602.07659v1#A4.F3 "Figure 3 ‣ D.2. Signal Disentanglement Test ‣ Appendix D Additional Disentanglement Visualizations ‣ Continuous Program Search") shows the average per-signal edit distance produced by perturbing each latent block.
The result is strongly diagonal.
Perturbing zl​ez\_{le} changes LE, perturbing zs​ez\_{se} changes SE, and so on.
Off-diagonal effects are negligible.
Cross-talk is effectively zero, and the target-only rate is 100%100\% across all evaluated signals.

![Refer to caption](x4.png)


Figure 3. Signal-level disentanglement under single-block perturbations (ϵ=0.3\epsilon=0.3, per-signal latent dimension = 32).
Rows indicate which latent block is perturbed.
Columns indicate which program signal changes.
Color shows the normalized token edit distance.
Perturbations affect only the intended signal, with negligible cross-talk.

These results show that the learned representation provides reliable component-level control.
Each latent block governs a distinct semantic part of the strategy.

Table 3. Walk-forward train, validation, and test folds used for all experiments. All results are reported on out-of-sample test folds with a 10-day embargo between splits to prevent lookahead bias.

| Fold | Train Start | Train End | Val Start | Val End | Test Start | Test End | Train Days | Val Days | Test Days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2008-01-01 | 2010-06-30 | 2010-06-30 | 2011-01-11 | 2011-01-21 | 2011-07-25 | 910 | 195 | 185 |
| 2 | 2011-07-25 | 2014-01-20 | 2014-01-20 | 2014-08-03 | 2014-08-13 | 2015-02-14 | 910 | 195 | 185 |
| 3 | 2015-02-14 | 2017-08-12 | 2017-08-12 | 2018-02-23 | 2018-03-05 | 2018-09-06 | 910 | 195 | 185 |
| 4 | 2018-09-06 | 2021-03-05 | 2021-03-05 | 2021-09-16 | 2021-09-26 | 2022-03-30 | 910 | 195 | 185 |
| 5 | 2022-03-30 | 2024-09-25 | 2024-09-25 | 2025-04-08 | 2025-04-18 | 2025-10-20 | 910 | 195 | 185 |