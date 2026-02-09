---
authors:
- Arvid E. Gollwitzer
- Paridhi Latawa
- David de Gruijl
- Deepak A. Subramanian
- Adrián Noriega de la Colina
doc_id: arxiv:2602.06394v1
family_id: arxiv:2602.06394
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware
  Tokenization
url_abs: http://arxiv.org/abs/2602.06394v1
url_html: https://arxiv.org/html/2602.06394v1
venue: arXiv q-fin
version: 1
year: 2026
---


Arvid E. Gollwitzer
  
Paridhi Latawa
  
David de Gruijl
  
Deepak A. Subramanian
  
Adrián Noriega de la Colina

###### Abstract

Current tokenization methods process sequential data without accounting for signal quality, limiting their effectiveness on noisy real-world corpora. We present QA-Token (Quality-Aware Tokenization), which incorporates data reliability directly into vocabulary construction. We make three key contributions: (i) a bilevel optimization formulation that jointly optimizes vocabulary construction and downstream performance, (ii) a reinforcement learning approach that learns merge policies through quality-aware rewards with convergence guarantees, and (iii) an adaptive parameter learning mechanism via Gumbel-Softmax relaxation for end-to-end optimization. Our experimental evaluation demonstrates consistent improvements: genomics (6.7 percentage point F1 gain in variant calling over BPE), finance (30% Sharpe ratio improvement). At foundation scale, re-tokenizing METAGENE-1’s 1.7 trillion base-pair corpus achieves state-of-the-art pathogen detection (94.53 MCC) while reducing token count by 15%. We unlock noisy real-world corpora, spanning petabases of genomic sequences and terabytes of financial time series, for foundation model training with zero inference overhead.

Tokenization, Foundation Models, Noisy Data, Reinforcement Learning, Genomics, Finance

## 1 Introduction

Tokenization serves as the interface between raw data and neural computation. Current methods such as Byte-Pair Encoding (BPE) (Sennrich et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib13 "Neural machine translation of rare words with subword units")) rely exclusively on frequency statistics, assuming that occurrence frequency correlates with semantic importance. This assumption fails when data quality varies significantly—from sequencing errors in genomics (Ewing et al., [1998](https://arxiv.org/html/2602.06394v1#bib.bib16 "Base-calling of automated sequencer traces using phred. i. accuracy assessment")) to microstructure noise in financial markets (Andersen et al., [2001](https://arxiv.org/html/2602.06394v1#bib.bib11 "The distribution of realized exchange rate volatility")). Models trained on noisy corpora using frequency-based tokenization inherit these errors, resulting in degraded performance—an effect now formalized through quality-aware scaling laws (Subramanyam et al., [2025](https://arxiv.org/html/2602.06394v1#bib.bib269 "Scaling laws revisited: modeling the role of data quality in language model pretraining")).

The problem is substantial: error rates in third-generation sequencing exceed 10% (Wenger et al., [2019](https://arxiv.org/html/2602.06394v1#bib.bib96 "Accurate circular consensus long-read sequencing improves variant detection and assembly of a human genome")), yet current tokenizers treat high-confidence and error-prone regions identically. In finance, over 40% of high-frequency data contains microstructure noise (Hansen and Lunde, [2006](https://arxiv.org/html/2602.06394v1#bib.bib97 "Realized variance and market microstructure noise")), but tokenization methods do not distinguish signal quality. This limitation constrains foundation model training on real-world data.

The scale of available biological data amplifies this challenge. Public sequence repositories now contain over 67 petabase pairs (Pbp) of raw sequencing data, with the European Nucleotide Archive doubling approximately every 45 months (Karasikov et al., [2025](https://arxiv.org/html/2602.06394v1#bib.bib111 "Efficient and accurate search in petabase-scale sequence repositories")). Recent advances in efficient indexing have made these petabase-scale archives full-text searchable at costs as low as $0.74 per queried megabase pair, demonstrating that the infrastructure for large-scale sequence analysis is maturing rapidly. However, a substantial fraction of this data remains underutilized for foundation model training due to quality heterogeneity—standard frequency-based tokenization methods either discard low-quality reads entirely or propagate sequencing errors into learned representations. This gap between data availability and usability motivates a fundamental rethinking of how tokenization handles quality variation.

We present Quality-Aware Tokenization (QA-Token), a framework that incorporates data quality into vocabulary construction. We make three key contributions:

1. Bilevel Optimization with Complexity Analysis: We formalize tokenization as a bilevel optimization problem ([Definition˜3.1](https://arxiv.org/html/2602.06394v1#S3.Thmtheorem1 "Definition 3.1 (Bilevel Tokenization Problem). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) that jointly optimizes vocabulary construction and downstream performance. We show this problem is NP-hard ([Theorem˜3.2](https://arxiv.org/html/2602.06394v1#S3.Thmtheorem2 "Theorem 3.2 (Computational Complexity). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) and develop a principled approximation scheme with theoretical guarantees.

2. Reinforcement Learning with Convergence Guarantees: We cast vocabulary construction as a Markov Decision Process ([Definition˜E.4](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem4 "Definition E.4 (Tokenization MDP). ‣ E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) and employ reinforcement learning to discover optimal merge policies. We provide formal convergence analysis ([Proposition˜E.5](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem5 "Proposition E.5 (MDP Well-Formedness). ‣ E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) and achieve (1−1/e)(1-1/e)-approximation to the optimal adaptive policy.

3. Differentiable Parameter Learning: Through Gumbel-Softmax relaxation ([Theorem˜C.8](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem8 "Theorem C.8 (Gumbel-Softmax Properties). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), we enable end-to-end learning of quality sensitivity parameters, with proven consistency and bounded gradients ([Proposition˜C.7](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem7 "Proposition C.7 (Consistency and Boundedness of Stage 2 Gradients). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

We show that QA-Token achieves information-theoretic optimality under noisy conditions ([Proposition˜C.13](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem13 "Proposition C.13 (Quality-Aware Information Bottleneck Interpretation). ‣ C.9 Information-Theoretic Optimality ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), providing formal justification for quality-aware tokenization. Our evaluation shows 30% higher Sharpe ratios in algorithmic trading, 6.7 percentage point improvement in genomic variant calling F1 (0.891 vs. 0.824 for BPE), and state-of-the-art performance when integrated into 7B-parameter foundation models.

Core Contributions: (i) We derive a quality-aware merge score ([Theorem˜C.3](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem3 "Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) balancing frequency, quality, and domain constraints with learnable sensitivity α\alpha ([Section˜C.2](https://arxiv.org/html/2602.06394v1#A3.SS2 "C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). (ii) We formulate vocabulary construction as an MDP ([Definition˜E.4](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem4 "Definition E.4 (Tokenization MDP). ‣ E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜E.7](https://arxiv.org/html/2602.06394v1#A5.SS7 "E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) achieving (1−1/e)(1-1/e)-approximation through adaptive submodularity. (iii) Gumbel-Softmax relaxation enables end-to-end parameter learning with O​(1/T)O(1/\sqrt{T}) convergence rate ([Proposition˜E.2](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem2 "Proposition E.2 (Convergence of Adaptive Learning with Explicit Constants). ‣ E.4 Convergence Properties ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜E.4](https://arxiv.org/html/2602.06394v1#A5.SS4 "E.4 Convergence Properties ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). (iv) Domain-specific instantiations achieve state-of-the-art performance across 15+ benchmarks.

Our analysis shows that incorporating quality signals into tokenization enables training on noisy corpora where frequency-based methods fail, expanding the range of usable training data for foundation models with broader scientific and economic implications ([Section˜7.1](https://arxiv.org/html/2602.06394v1#S7.SS1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

## 2 Quality Metrics for Noisy Domains

Quality metrics must satisfy three formal properties to enable principled integration into the merge score: (i) *boundedness* (q∈[0,1]q\in[0,1]) ensuring numerical stability, (ii) *Lipschitz continuity* enabling stable gradient computation during adaptive learning, and (iii) *monotonicity under noise injection* (higher noise yields lower quality) ensuring semantic consistency. We prove these properties hold for our domain-specific instantiations ([Proposition˜C.1](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem1 "Proposition C.1 (Boundedness and Continuity of Quality Functions). ‣ C.1 Quality Metric Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.1](https://arxiv.org/html/2602.06394v1#A3.SS1 "C.1 Quality Metric Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Genomics: We leverage Phred scores with position-adjusted decay: qsj′=qsj⋅exp⁡(−βpos⋅j/L)q^{\prime}\_{s\_{j}}=q\_{s\_{j}}\cdot\exp(-\beta\_{\text{pos}}\cdot j/L), where βpos\beta\_{\text{pos}} is learned and LL is read length. Token quality is aggregated via geometric mean qt=(∏j=1|t|qsj′)1/|t|q\_{t}=(\prod\_{j=1}^{|t|}q^{\prime}\_{s\_{j}})^{1/|t|} to ensure sensitivity to low-quality regions—a single unreliable base compromises the entire token (Eq. [13](https://arxiv.org/html/2602.06394v1#A4.E13 "Equation 13 ‣ D.1 Genomics: Detailed Sequencing Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Finance: We combine four market microstructure dimensions: (i) liquidity qliqq\_{\text{liq}} (bid-ask spread, depth), (ii) signal quality qsigq\_{\text{sig}} (SNR of price changes), (iii) stability qstbq\_{\text{stb}} (volatility regime), and (iv) information content qinfoq\_{\text{info}} (order flow informativeness). The composite score qtfinance=∑kwk​qk,tq\_{t}^{\text{finance}}=\sum\_{k}w\_{k}q\_{k,t} uses learned weights; arithmetic mean aggregation reflects additive noise characteristics of financial data (Eq. [14](https://arxiv.org/html/2602.06394v1#A4.E14 "Equation 14 ‣ D.2 Finance: Comprehensive Market Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

With quality metrics defined, we now formalize how they integrate into the tokenization objective.

## 3 Mathematical Formulation of QA-Token

### 3.1 Notation and Setup

Let 𝒮={S1,S2,…,SN}\mathcal{S}=\{S\_{1},S\_{2},\dots,S\_{N}\} represent a corpus comprising NN sequences, where each sequence Sk=(sk,1,…,sk,nk)S\_{k}=(s\_{k,1},\dots,s\_{k,n\_{k}}) consists of elements drawn from a base alphabet Σ\Sigma. Each atomic element sk,is\_{k,i} is associated with a normalized quality score qk,i∈[0,1]q\_{k,i}\in[0,1] as defined in [Section˜2](https://arxiv.org/html/2602.06394v1#S2 "2 Quality Metrics for Noisy Domains ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"). The initial vocabulary is defined as V0=ΣV\_{0}=\Sigma. At any step kk of the tokenization process, VkV\_{k} denotes the current vocabulary. For any token a∈Vka\in V\_{k}, we denote its frequency in the corpus as f​(a)f(a), and for an adjacent pair (a,b)(a,b), their co-occurrence frequency is f​(a,b)f(a,b). The length of a token tt in atomic units is |t||t|. Let qtq\_{t} be the aggregated scalar quality of token tt, computed using domain-specific aggregation functions (see [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

### 3.2 Formal Problem Definition and Objective

We formalize tokenization as finding a tokenizer 𝒯\mathcal{T} that maximizes objective 𝒥\mathcal{J}, balancing downstream task performance, vocabulary complexity, and data reliability. Let 𝒮={S1,S2,…,SN}\mathcal{S}=\{S\_{1},S\_{2},\ldots,S\_{N}\} denote a corpus of NN sequences sampled from an underlying data distribution 𝒫data\mathcal{P}\_{\text{data}}, where each Sk=(sk,1,…,sk,nk)S\_{k}=(s\_{k,1},\ldots,s\_{k,n\_{k}}) consists of elements from base alphabet Σ\Sigma. A tokenizer 𝒯:𝒮→𝒵\mathcal{T}:\mathcal{S}\rightarrow\mathcal{Z} maps the corpus to segmentations 𝒵={Z1,…,ZN}\mathcal{Z}=\{Z\_{1},\ldots,Z\_{N}\} using vocabulary VV.

###### Definition 3.1 (Bilevel Tokenization Problem).

The optimal quality-aware tokenization problem is formulated as the following bilevel optimization:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝒯∈𝒢​(K)⁡𝒥​(𝒯):=λLM​ℒLM​(𝒯)−λcomp​Φ​(V)+λqual​Q​(V,𝒵),\begin{split}\max\_{\mathcal{T}\in\mathcal{G}(K)}\;\mathcal{J}(\mathcal{T})\;:=\;&\;\lambda\_{\text{LM}}\,\mathcal{L}\_{\text{LM}}(\mathcal{T})-\lambda\_{\text{comp}}\,\Phi(V)\\ &\;+\;\lambda\_{\text{qual}}\,Q(V,\mathcal{Z}),\end{split} |  | (1) |

where the language model performance is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒLM​(𝒯)=maxθ∈Θ⁡𝔼𝒟∼𝒫data​[log⁡pθ​(𝒟|𝒯)],\mathcal{L}\_{\text{LM}}(\mathcal{T})=\max\_{\theta\in\Theta}\mathbb{E}\_{\mathcal{D}\sim\mathcal{P}\_{\text{data}}}[\log p\_{\theta}(\mathcal{D}|\mathcal{T})], |  | (2) |

and 𝒢​(K)={𝒯:|V𝒯|−|Σ|≤K}\mathcal{G}(K)=\{\mathcal{T}:|V\_{\mathcal{T}}|-|\Sigma|\leq K\} denotes the set of tokenizers reachable by at most KK merge operations from base alphabet Σ\Sigma, with Θ\Theta being the parameter space of the language model.

The objective 𝒥\mathcal{J} balances three components: (i) downstream performance ℒLM​(𝒯)\mathcal{L}\_{\text{LM}}(\mathcal{T}) maximizing expected log-likelihood, (ii) complexity penalty Φ​(V)=|V|​log⁡|V|+∑t∈V|t|⋅H​(t)\Phi(V)=|V|\log|V|+\sum\_{t\in V}|t|\cdot H(t) following MDL principles (Rissanen, [1978](https://arxiv.org/html/2602.06394v1#bib.bib42 "Modeling by shortest data description"))—the first term penalizes vocabulary size (description length of token indices), while the second penalizes internal token complexity via the empirical entropy H​(t)=−∑σ∈Σnσ​(t)|t|​log⁡nσ​(t)|t|H(t)=-\sum\_{\sigma\in\Sigma}\frac{n\_{\sigma}(t)}{|t|}\log\frac{n\_{\sigma}(t)}{|t|} of atomic elements within token tt (with nσ​(t)n\_{\sigma}(t) the count of element σ\sigma; H​(t)=0H(t)=0 for single-element tokens), and (iii) reliability reward Q​(V,𝒵)=1∑k=1N|Zk|​∑k=1N∑t∈Zkg​(qt)Q(V,\mathcal{Z})=\frac{1}{\sum\_{k=1}^{N}|Z\_{k}|}\sum\_{k=1}^{N}\sum\_{t\in Z\_{k}}g(q\_{t}) aggregating token qualities through concave function gg.

The aggregator function gg exhibits concavity to capture diminishing returns for merging high-quality constituents. Throughout this work, we employ g​(x)=(x+ϵQ)αg(x)=(x+\epsilon\_{Q})^{\alpha} with 0<α<10<\alpha<1 (strictly concave) and ϵQ=10−8\epsilon\_{Q}=10^{-8} for numerical stability. The boundary case α=1\alpha=1 yields linear aggregation, which is appropriate when quality contributions are additive rather than subject to diminishing returns.

###### Theorem 3.2 (Computational Complexity).

The bilevel optimization problem in Eq. [1](https://arxiv.org/html/2602.06394v1#S3.E1 "Equation 1 ‣ Definition 3.1 (Bilevel Tokenization Problem). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") is NP-hard in general (Dempe, [2020](https://arxiv.org/html/2602.06394v1#bib.bib116 "Bilevel optimization: theory, algorithms and applications")); indeed, polynomial bilevel programming is Σ2p\Sigma\_{2}^{p}-hard (Cen and Chi, [2023](https://arxiv.org/html/2602.06394v1#bib.bib119 "Global convergence of policy gradient methods in reinforcement learning, games and control")), placing it one level above NP in the polynomial hierarchy. The worst case requires O​(|Σ|K⋅K!⋅N⋅n⋅|Θ|)O(|\Sigma|^{K}\cdot K!\cdot N\cdot n\cdot|\Theta|) evaluations (proof in [Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Given this computational intractability, we develop a principled approximation scheme combining greedy merge selection with reinforcement learning, as detailed in subsequent sections.

### 3.3 Quality-Aware Merge Score

We extend PMI-based tokenization by incorporating quality signals through the following result:

###### Theorem 3.3 (Quality-Aware Merge Score).

The optimal greedy merge score maximizing the first-order approximation of the objective increment Δ​𝒥\Delta\mathcal{J} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wa​b=f​(a,b)f​(a)​f​(b)+ϵf⋅(q¯a​b+ϵQ)α⋅ψ​(a,b)w\_{ab}=\frac{f(a,b)}{f(a)f(b)+\epsilon\_{f}}\cdot(\bar{q}\_{ab}+\epsilon\_{Q})^{\alpha}\cdot\psi(a,b) |  | (3) |

where q¯a​b=(qa+qb)/2\bar{q}\_{ab}=(q\_{a}+q\_{b})/2 averages constituent qualities, α∈(0,1]\alpha\in(0,1] controls quality sensitivity, and ψ​(a,b)\psi(a,b) encodes domain constraints. (Proof via first-order approximation in [Section˜C.2](https://arxiv.org/html/2602.06394v1#A3.SS2 "C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").)

This score balances statistical association (PMI term), data reliability (quality term), and domain-specific requirements. Boundedness and Lipschitz continuity are proven in [Proposition˜C.4](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem4 "Proposition C.4 (Boundedness and Lipschitzness of 𝑤_{𝑎⁢𝑏}). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") ([Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5 "C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

## 4 Learning Framework: RL and Adaptive Parameters

We cast vocabulary construction as a learning problem with two sequential stages. Stage 1 (RL Policy Optimization) learns policy πθπ\pi\_{\theta\_{\pi}} for merge selection using PPO with quality-aware rewards, keeping initial parameters θadapt(0)\theta\_{\text{adapt}}^{(0)} fixed. Stage 2 (Adaptive Parameter Learning) optimizes θadapt\theta\_{\text{adapt}} via Gumbel-Softmax relaxation for downstream performance, using *greedy simulation* with composite logits ℓa​b​(θadapt)\ell\_{ab}(\theta\_{\text{adapt}}) rather than invoking the RL policy directly—the Stage 1 policy serves to initialize candidate merges and provide variance reduction baselines. Gradients ∇θadaptLtask\nabla\_{\theta\_{\text{adapt}}}L\_{\text{task}} flow through Gumbel-Softmax merge selection, enabling end-to-end learning (detailed in [Appendix˜E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), Algorithms [1](https://arxiv.org/html/2602.06394v1#alg1 "Algorithm 1 ‣ E.1.3 PPO Training Algorithm ‣ E.1 Stage 1: Reinforcement Learning Policy Optimization ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")–[3](https://arxiv.org/html/2602.06394v1#alg3 "Algorithm 3 ‣ E.3 Final Vocabulary Construction ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

### 4.1 Reinforcement Learning Formulation

###### Definition 4.1 (Tokenization MDP).

The vocabulary construction MDP is ℳ=(𝒮,𝒜,𝒫,ℛ,γ,T)\mathcal{M}=(\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma,T) where: states st∈𝒮s\_{t}\in\mathcal{S} encode current vocabulary, merge candidates, and corpus statistics; actions at∈𝒜ta\_{t}\in\mathcal{A}\_{t} select merge pairs; transitions 𝒫\mathcal{P} are deterministic vocabulary updates; rewards ℛ\mathcal{R} are quality-aware (Section [4.2](https://arxiv.org/html/2602.06394v1#S4.SS2 "4.2 Reward Function Design ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")); γ∈(0,1]\gamma\in(0,1] is the discount factor; TT is the horizon (target vocabulary size minus base alphabet size). Complete specification in [Section˜E.7](https://arxiv.org/html/2602.06394v1#A5.SS7 "E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

The RL objective finds policy πθπ:𝒮→Δ​(𝒜)\pi\_{\theta\_{\pi}}:\mathcal{S}\rightarrow\Delta(\mathcal{A}) maximizing expected cumulative reward over TT operations using PPO (Schulman et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib63 "Proximal policy optimization algorithms")), with global convergence guarantees following (Bhandari and Russo, [2021](https://arxiv.org/html/2602.06394v1#bib.bib115 "Global optimality guarantees for policy gradient methods"); Cen and Chi, [2023](https://arxiv.org/html/2602.06394v1#bib.bib119 "Global convergence of policy gradient methods in reinforcement learning, games and control")). [Proposition˜E.5](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem5 "Proposition E.5 (MDP Well-Formedness). ‣ E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") ([Section˜E.7](https://arxiv.org/html/2602.06394v1#A5.SS7 "E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) proves MDP well-formedness.

### 4.2 Reward Function Design

The multi-objective reward R​(a,b;θadapt(0))=∑jλj​R^j​(a,b)R(a,b;\theta\_{\text{adapt}}^{(0)})=\sum\_{j}\lambda\_{j}\hat{R}\_{j}(a,b) combines quality, information, complexity, and domain-specific components. Each raw reward RjrawR^{\text{raw}}\_{j} is normalized using adaptive running statistics with exponential moving averages: μj,trun=(1−βnorm)​μj,t−1run+βnorm​Rjraw\mu\_{j,t}^{\text{run}}=(1-\beta\_{\text{norm}})\mu\_{j,t-1}^{\text{run}}+\beta\_{\text{norm}}R^{\text{raw}}\_{j}, yielding R^j=(Rjraw−μj,t−1run)/(σj,t−1run+ϵR)\hat{R}\_{j}=(R^{\text{raw}}\_{j}-\mu\_{j,t-1}^{\text{run}})/(\sigma\_{j,t-1}^{\text{run}}+\epsilon\_{R}). This ensures bounded, scale-invariant rewards during non-stationary policy optimization ([Proposition˜C.5](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem5 "Proposition C.5 (Stability of EMA Normalization). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜E.8](https://arxiv.org/html/2602.06394v1#A5.SS8 "E.8 Reward Normalization Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

### 4.3 Adaptive Learning of Tokenization Parameters

After RL optimization, we learn θadapt\theta\_{\text{adapt}} (quality sensitivity α\alpha, domain factors βpos\beta\_{\text{pos}}/βvol\beta\_{\text{vol}}, weights) minimizing Ltotal​(θadapt)=Ltask​(θadapt)+λreg​‖θadapt‖22L\_{\text{total}}(\theta\_{\text{adapt}})=L\_{\text{task}}(\theta\_{\text{adapt}})+\lambda\_{\text{reg}}\|\theta\_{\text{adapt}}\|\_{2}^{2} via Gumbel-Softmax (Jang et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib31 "Categorical reparameterization with gumbel-softmax"); Maddison et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib32 "The concrete distribution: a continuous relaxation of discrete random variables")). Temperature annealing τ​(t)=τinit​exp⁡(−βanneal​t/Tanneal)\tau(t)=\tau\_{\text{init}}\exp(-\beta\_{\text{anneal}}t/T\_{\text{anneal}}) ensures convergence ([Proposition˜C.7](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem7 "Proposition C.7 (Consistency and Boundedness of Stage 2 Gradients). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Proposition˜E.2](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem2 "Proposition E.2 (Convergence of Adaptive Learning with Explicit Constants). ‣ E.4 Convergence Properties ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"); [Section˜E.9](https://arxiv.org/html/2602.06394v1#A5.SS9 "E.9 Gumbel-Softmax Gradient Derivation and Temperature Annealing ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Appendix˜E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). The two-stage framework—RL with fixed θadapt(0)\theta\_{\text{adapt}}^{(0)} then adaptive learning—culminates in greedy vocabulary construction using wa​b​(a,b;θadapt∗)w\_{ab}(a,b;\theta\_{\text{adapt}}^{\*}) ([Appendix˜E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), Algorithms [1](https://arxiv.org/html/2602.06394v1#alg1 "Algorithm 1 ‣ E.1.3 PPO Training Algorithm ‣ E.1 Stage 1: Reinforcement Learning Policy Optimization ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")–[3](https://arxiv.org/html/2602.06394v1#alg3 "Algorithm 3 ‣ E.3 Final Vocabulary Construction ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

### 4.4 Two-Timescale Convergence

The sequential optimization follows a two-timescale stochastic approximation: policy updates on fast timescale (learning rate ηπ(t)\eta\_{\pi}^{(t)}), adaptive parameters on slow timescale (ηadapt(t)\eta\_{\text{adapt}}^{(t)}), with ηπ(t)/ηadapt(t)→∞\eta\_{\pi}^{(t)}/\eta\_{\text{adapt}}^{(t)}\to\infty as t→∞t\to\infty. Under assumptions (A1)–(A4), this converges to a local Nash equilibrium where θπ∗\theta\_{\pi}^{\*} maximizes J​(π;θadapt∗)J(\pi;\theta\_{\text{adapt}}^{\*}) and θadapt∗\theta\_{\text{adapt}}^{\*} minimizes Ltotal​(θadapt;π∗)L\_{\text{total}}(\theta\_{\text{adapt}};\pi^{\*}). Quality bounds and initialization strategies for approaching global optima are detailed in [Appendix˜E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

### 4.5 Theoretical Guarantees

Our framework provides the following guarantees under assumptions (A1)–(A4) detailed in [Section˜C.6](https://arxiv.org/html/2602.06394v1#A3.SS6 "C.6 Assumptions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"): (i) bounded/Lipschitz merge scores wa​bw\_{ab} ([Proposition˜C.4](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem4 "Proposition C.4 (Boundedness and Lipschitzness of 𝑤_{𝑎⁢𝑏}). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), (ii) stable EMA normalization with strictly positive running standard deviations ([Proposition˜C.5](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem5 "Proposition C.5 (Stability of EMA Normalization). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), (iii) PPO convergence to stationary points ([Proposition˜C.6](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem6 "Proposition C.6 (Convergence of PPO Objective). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), (iv) consistent and bounded Gumbel-Softmax gradients ([Proposition˜C.7](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem7 "Proposition C.7 (Consistency and Boundedness of Stage 2 Gradients). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), and (v) (1−1/e)(1-1/e)-approximation to optimal adaptive policy via adaptive submodularity.

Information-Theoretic Optimality: Building on information bottleneck theory (Tishby et al., [1999](https://arxiv.org/html/2602.06394v1#bib.bib113 "The information bottleneck method"); Alemi et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib114 "Deep variational information bottleneck")), our analysis ([Proposition˜C.13](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem13 "Proposition C.13 (Quality-Aware Information Bottleneck Interpretation). ‣ C.9 Information-Theoretic Optimality ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.9](https://arxiv.org/html/2602.06394v1#A3.SS9 "C.9 Information-Theoretic Optimality ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) shows QA-Token minimizes the quality-aware information bottleneck:
ℒQA​(V)=−I​(T;Y|Q)+β⋅I​(T;X|Q)\mathcal{L}\_{\text{QA}}(V)=-I(T;Y|Q)+\beta\cdot I(T;X|Q),
achieving optimal compression-relevance tradeoffs under noisy conditions by maximizing task-relevant information I​(T;Y|Q)I(T;Y|Q) while minimizing redundant representation complexity I​(T;X|Q)I(T;X|Q), conditioned on quality QQ. Complete proofs in [Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5 "C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") and [Appendix˜E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Having established the theoretical framework and convergence guarantees, we now validate QA-Token empirically across two domains with distinct noise characteristics.

## 5 Empirical Validation

Setup: Results represent means over 10 trials with 95% CIs and Welch’s t-test with Holm-Bonferroni correction (significance level psig=0.05p\_{\text{sig}}=0.05). Evaluation spans domain benchmarks, 7B-parameter foundation models, and ablation studies (complete details in [Appendix˜G](https://arxiv.org/html/2602.06394v1#A7 "Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")–[Section˜G.3](https://arxiv.org/html/2602.06394v1#A7.SS3 "G.3 Computational Costs ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

### 5.1 Genomics (QA-BPE-seq)

Data: 150bp paired-end reads (ART simulator (Huang et al., [2012](https://arxiv.org/html/2602.06394v1#bib.bib49 "ART: a next-generation sequencing read simulator")), 30x coverage, doubled error rates), GRCh38 reference, GIAB HG002 truth set (Zook et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib50 "Extensive sequencing of seven human genomes to characterize benchmark reference materials")), CAMI II metagenome (Sczyrba et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib51 "Critical assessment of metagenome interpretation—a benchmark of metagenomics software")). Details in [Appendix˜G](https://arxiv.org/html/2602.06394v1#A7 "Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Baselines: We compare against (i) general-purpose tokenizers (BPE, SentencePiece (Kudo and Richardson, [2018](https://arxiv.org/html/2602.06394v1#bib.bib15 "SentencePiece: a simple and language independent subword tokenizer and detokenizer for neural text processing")), WordPiece), (ii) robustness-enhanced methods (BPE-dropout (Provilkov et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib26 "BPE-dropout: simple and effective subword regularization"))), (iii) byte-level models (ByT5 (Xue et al., [2022](https://arxiv.org/html/2602.06394v1#bib.bib27 "ByT5: towards a token-free future with pre-trained byte-to-byte models")), CANINE (Clark et al., [2021](https://arxiv.org/html/2602.06394v1#bib.bib28 "Canine: pre-training an efficient tokenization-free encoder for language representation"))), (iv) domain-standard k-mers (6-mer DNABERT (Ji et al., [2021](https://arxiv.org/html/2602.06394v1#bib.bib9 "DNABERT: pre-trained bidirectional encoder representations from transformers model for dna-language in genome"))), and (v) neural approaches (CharFormer (Tay et al., [2022](https://arxiv.org/html/2602.06394v1#bib.bib29 "Charformer: fast character transformers via gradient-based subword tokenization"))).

Quality Design: Phred scores with position decay, geometric mean aggregation, learned α=0.72±0.03\alpha=0.72\pm 0.03, βpos=0.014±0.002\beta\_{\text{pos}}=0.014\pm 0.002.

Evaluation: (i) Variant calling via a Transformer model that takes token embeddings as features and predicts variant calls, evaluated against GIAB truth sets using hap.py; (ii) taxonomic classification (6-layer Transformer); (iii) sequence reconstruction (autoencoder), following established benchmarking protocols (Rumpf et al., [2023](https://arxiv.org/html/2602.06394v1#bib.bib102 "SequenceLab: a comprehensive benchmark of computational methods for comparing genomic sequences")). [Table˜1](https://arxiv.org/html/2602.06394v1#S5.T1 "In 5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") shows QA-BPE-seq outperforms all baselines (p<0.001p<0.001).

Key Insights: (i) QA-BPE-seq achieves 6.7 percentage point F1 improvement in variant calling (0.891 vs. 0.824 for BPE). (ii) Byte-level models fail catastrophically (2.5×\times slower, 7–9% lower accuracy). (iii) Emergent vocabulary aligns with biological units (codons, motifs) at high-quality regions without explicit supervision (vocabulary analysis in [Appendix˜G](https://arxiv.org/html/2602.06394v1#A7 "Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Table 1: Downstream task performance for genomic tokenization. Values are means with 95% CI over n=10n=10 runs. Time: relative wall-clock (BPE=10.0×\times).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Method | Var. F1 | Taxa F1 | Recon. | Time |
| Standard BPE | .824±\pm.004 | .856±\pm.005 | .317±\pm.010 | 10.0 |
| SentencePiece | .837±\pm.004 | .872±\pm.005 | .301±\pm.009 | 10.1 |
| WordPiece | .829±\pm.005 | .863±\pm.006 | .308±\pm.011 | 10.0 |
| BPE-dropout | .841±\pm.004 | .878±\pm.005 | .295±\pm.009 | 10.2 |
| ByT5 | .812±\pm.006 | .845±\pm.007 | .338±\pm.012 | 25.3 |
| CANINE | .818±\pm.005 | .852±\pm.006 | .325±\pm.011 | 22.7 |
| DNABERT-k | .851±\pm.003 | .889±\pm.004 | .287±\pm.008 | 9.8 |
| CharFormer | .856±\pm.003 | .893±\pm.004 | .279±\pm.008 | 10.4 |
| QA-BPE-seq | .891±\pm.004 | .917±\pm.003 | .241±\pm.007 | 10.2 |




Table 2: Ablation Study for QA-BPE-seq (Variant F1). Values are means with 95% CI over n=10n=10 runs.∗

|  |  |  |
| --- | --- | --- |
| Configuration | Var. F1 | Δ\Delta(%) |
| QA-BPE-seq (Full) | .891±\pm.004 | — |
| w/o RL (Greedy wa​bw\_{ab}) | .862±\pm.005 | −-3.3 |
| w/o Quality (RQ=0R\_{Q}=0) | .825±\pm.004 | −-7.4 |
| w/o Info. Reward (RI=0R\_{I}=0) | .872±\pm.005 | −-2.1 |
| w/o Adapt. Params | .857±\pm.006 | −-3.8 |
| w/o Rb​i​oR\_{bio} | .885±\pm.004 | −-0.7 |
| QualTok (Baseline) | .840±\pm.005 | −-5.7 |

* \*

  “w/o RL (Greedy wa​bw\_{ab})” uses full QA-Token merge score with learned α\alpha but selects merges greedily without RL policy optimization. “QualTok (Baseline)” additionally fixes adaptive parameters (α=0.5\alpha{=}0.5, uniform weights).




Table 3: Ablation Study for QAT-QF (Return Pred. Acc. % and Sharpe Ratio). Means with 95% CI over n=10n=10 runs.∗

|  |  |  |
| --- | --- | --- |
| Variant | Ret. Pred. (%) | Sharpe |
| Full Model | 68.3±\pm0.5 | 1.72±\pm0.07 |
| w/o Quality (RQ=0R\_{Q}=0) | 64.2±\pm0.6 | 1.56±\pm0.08 |
| w/o Info. (RI=0R\_{I}=0) | 65.1±\pm0.5 | 1.61±\pm0.07 |
| w/o Pred. Power (RP=0R\_{P}=0) | 63.9±\pm0.6 | 1.49±\pm0.09 |
| w/o Complexity (RC=0R\_{C}=0) | 66.8±\pm0.4 | 1.73±\pm0.06 |
| Fixed α\alpha | 65.4±\pm0.5 | 1.65±\pm0.07 |
| Fixed γ\gamma | 64.9±\pm0.5 | 1.59±\pm0.08 |
| QualTok-QF (Baseline) | 64.8±\pm0.6 | 1.58±\pm0.08 |

* \*

  “QualTok-QF (Baseline)” uses a simplified quality-aware merge score with fixed α=0.5\alpha{=}0.5 and uniform weights, without RL policy optimization or adaptive parameter learning.

### 5.2 Quantitative Finance (QAT-QF)

Dataset: We use high-frequency limit order book (LOB) data for the BTC/USD trading pair from LOBSTER (Huang and Polak, [2011](https://arxiv.org/html/2602.06394v1#bib.bib54 "LOBSTER: limit order book reconstruction system")), specifically reconstructed snapshots at 10 levels for the first quarter of 2023. The data is split chronologically into 70% for training, 15% for validation, and 15% for testing. Atomic elements are defined as sequences of 5 consecutive LOB events, encoded as tuples (Δ​mid,Δ​spread,vol\_imbalance,event\_type,Δ​t)(\Delta\text{mid},\Delta\text{spread},\text{vol\\_imbalance},\text{event\\_type},\Delta t) with discretization: price changes into 10 bins (±\pm5 ticks), spread into 10 bins, volume imbalance into 5 signed bins, event types categorical (trade/cancel/limit order), time intervals into 5 log-spaced bins, yielding |Σ|=7,500|\Sigma|=7{,}500 atomic symbols (see [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Baselines: QAT-QF is benchmarked against a diverse slate of tokenization and discretization methods relevant to financial time series.

* •

  General-Purpose: Standard BPE, SentencePiece (Unigram LM mode), and BPE-dropout (Provilkov et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib26 "BPE-dropout: simple and effective subword regularization")) to assess robustness.
* •

  Time-Series Specific: Symbolic Aggregate approXimation (SAX) (Lin et al., [2003](https://arxiv.org/html/2602.06394v1#bib.bib55 "Symbolic representation of time series, with implications for streaming algorithms")) (PAA=16, alphabet size=8) and Bag-of-SFA-Symbols (BOSS) (Schäfer, [2015](https://arxiv.org/html/2602.06394v1#bib.bib56 "The boss is concerned with time series classification in the presence of noise")), both widely used for symbolic time series representation.

The target vocabulary size for subword models is 16,000.

Evaluation: We assess (i) return prediction accuracy (5-minute mid-price return sign), (ii) volatility forecasting RMSE (5-minute realized volatility), (iii) market regime identification (2-state GARCH-HMM classification), and (iv) trading performance (Sharpe ratio (Sharpe, [1994](https://arxiv.org/html/2602.06394v1#bib.bib48 "The sharpe ratio")) with 5bp transaction cost). Models use 2-layer LSTMs (128 hidden units) and PPO agents (Deng et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib41 "Deep direct reinforcement learning for financial signal representation and trading")). See [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") and [Section˜H.4](https://arxiv.org/html/2602.06394v1#A8.SS4 "H.4 Financial Experimental Methodology Details ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") for implementation details.

Results: [Table˜4](https://arxiv.org/html/2602.06394v1#S5.T4 "In 5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") presents results averaged over n=10n=10 runs. QAT-QF improves performance across all financial tasks (p<0.01p<0.01, Holm-Bonferroni corrected). The trading agent achieves Sharpe ratio of 1.72±0.071.72\pm 0.07 compared to 1.32±0.051.32\pm 0.05 for standard BPE (30% improvement). See ablation analysis in [Table˜3](https://arxiv.org/html/2602.06394v1#S5.T3 "In 5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Table 4: Downstream task performance for financial tokenization. Values are means with 95% CI over n=10n=10 runs. Time: minutes per epoch.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | Ret. (%) | Vol. | Regime | Sharpe | Time |
| BPE | 61.2±\pm0.5 | .014±\pm.001 | 73.5±\pm0.6 | 1.32±\pm.05 | 15.0 |
| SAX | 58.9±\pm0.6 | .014±\pm.001 | 75.2±\pm0.5 | 1.29±\pm.06 | 14.5 |
| BOSS | 62.3±\pm0.4 | .013±\pm.001 | 78.4±\pm0.4 | 1.45±\pm.05 | 14.8 |
| QAT-QF | 68.3±\pm0.5 | .010±\pm.001 | 86.4±\pm0.3 | 1.72±\pm.07 | 15.2 |

## 6 Foundation Model Validation

We validate QA-Token on domain benchmarks ([Section˜5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) and now evaluate at foundation scale. We retrain state-of-the-art foundation models in genomics and finance to demonstrate that quality-aware tokenization improves how large models learn from noisy corpora, departing from traditional frequency-based approaches.

### 6.1 Metagenomics Foundation Model: METAGENE-1 7B

Setup: Re-tokenized METAGENE-1 (Liu and others, [2025](https://arxiv.org/html/2602.06394v1#bib.bib84 "METAGENE-1: metagenomic foundation model for pandemic monitoring")) (7B parameters, 1.7T base pairs) with identical architecture/hyperparameters, comparing BPE vs QA-BPE-seq.

Quality-Aware Design: The tokenizer is trained on 2B base pairs (0.12% of corpus) using genomic quality metrics (Eq. [13](https://arxiv.org/html/2602.06394v1#A4.E13 "Equation 13 ‣ D.1 Genomics: Detailed Sequencing Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) combining (i) Phred-based quality scores, (ii) conservation scores from k-mer analysis, (iii) GC-content deviation metrics, and (iv) secondary structure prediction confidence. The learned βpos=0.014\beta\_{\text{pos}}=0.014 captures position-specific quality decay (see [Section˜H.1](https://arxiv.org/html/2602.06394v1#A8.SS1 "H.1 Genomics (QA-BPE-seq) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") for implementation).

Training Budget: Both models process identical raw data volume (1.7T base pairs). The 15% token reduction means QA-BPE-seq completes epochs in fewer optimization steps while maintaining equal raw data exposure. Step-matched experiments (same optimization steps, where QA-BPE-seq processes 17.6% more raw data per step) show consistent improvements ([Appendix˜G](https://arxiv.org/html/2602.06394v1#A7 "Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Table 5: Pathogen Detection benchmark (MCC). QA-Token achieves state-of-the-art.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | T-1 | T-2 | T-3 | T-4 | T-5 | Avg |
| DNABERT | 82.2 | 81.4 | 83.3 | 84.6 | 82.9 | 82.9 |
| DNABERT-2 | 86.7 | 86.9 | 88.3 | 89.8 | 87.9 | 87.9 |
| DNABERT-S | 85.4 | 85.2 | 89.0 | 88.4 | 86.0 | 87.0 |
| NT-2.5B-M | 83.8 | 83.5 | 82.5 | 79.9 | 81.4 | 82.4 |
| NT-2.5B-1k | 77.5 | 80.4 | 79.8 | 78.4 | 79.0 | 79.0 |
| HyenaDNA | 78.7 | 79.1 | 80.4 | 81.2 | 79.9 | 79.9 |
| METAGENE-1 | 92.1 | 90.9 | 93.7 | 95.1 | 94.0 | 93.0 |
| +QA-Token | 93.8 | 93.0 | 95.1 | 96.2 | 94.5 | 94.5 |
| Δ\Delta | +1.7 | +2.0 | +1.4 | +1.1 | +0.6 | +1.6 |

Pathogen Detection: QA-Token achieves state-of-the-art 94.53 MCC, surpassing the original METAGENE-1 by 1.57 points (p<0.001p<0.001). Consistent improvements across all five subtasks demonstrate robustness. Task-2 shows the largest gain (+2.04 MCC) on highly degraded metagenomic samples where quality awareness is most critical, validating our theoretical framework.

Table 6: Genome Understanding Evaluation (GUE): Multi-species benchmark.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task | META-1 | QA-Token | Δ\Delta | p |
| Regulatory Elements | | | | |
| TF-Mouse (MCC) | 71.4±\pm0.8 | 72.8±\pm0.7 | +1.4 | .002 |
| TF-Human (MCC) | 68.3±\pm0.9 | 69.9±\pm0.8 | +1.6 | .001 |
| Promoter (MCC) | 82.3±\pm0.5 | 85.5±\pm0.4 | +3.2 | <<.001 |
| Enhancer (AUC) | .876±\pm.012 | .892±\pm.010 | +.016 | .003 |
| Epigenetics | | | | |
| H3K4me3 (MCC) | 65.2±\pm0.6 | 66.8±\pm0.5 | +1.6 | .002 |
| H3K27ac (MCC) | 66.8±\pm0.7 | 68.2±\pm0.6 | +1.4 | .003 |
| Methylation (AUC) | .823±\pm.015 | .841±\pm.013 | +.018 | .004 |
| Structure | | | | |
| Splice Site (F1) | 87.8±\pm0.4 | 89.5±\pm0.3 | +1.7 | <<.001 |
| RNA Structure | 72.1±\pm0.8 | 73.9±\pm0.7 | +1.8 | .002 |
| Variants | | | | |
| COVID (F1) | 72.5±\pm0.6 | 73.3±\pm0.5 | +0.8 | .018 |
| SNP Effect | .684±\pm.021 | .712±\pm.018 | +.028 | .001 |
| Win Rate | 46.4% | 57.1% | +10.7% | — |
| Efficiency | 370B | 315B | −-15% | — |

GUE Results: QA-Token improves performance across all categories (largest: +3.2 MCC promoter detection). 15% token reduction with performance gains indicates semantic coherence of quality-aware merging.

### 6.2 Financial Time-Series Foundation Model

Setup: 1.2B parameter model (24 layers, 2048 dim) inspired by TimesFM (Das et al., [2024](https://arxiv.org/html/2602.06394v1#bib.bib85 "TimesFM: a decoder-only foundation model for time-series forecasting")) and Chronos (Ansari et al., [2024](https://arxiv.org/html/2602.06394v1#bib.bib86 "Chronos: learning the language of time series")), using QAT-QF for noise handling.

Training Corpus: We train on 500 billion time-series observations spanning (i) high-frequency order book data (40%, 5 years millisecond-resolution across 50 liquid assets), (ii) daily OHLCV data (30%, 20 years for major indices), (iii) macroeconomic indicators (20%, 30 years G20 data), and (iv) alternative data (10%, sentiment scores, option flows, ETF compositions).

Quality-Aware Design: QAT-QF employs comprehensive market quality metrics (Eq. [14](https://arxiv.org/html/2602.06394v1#A4.E14 "Equation 14 ‣ D.2 Finance: Comprehensive Market Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), combining liquidity, signal, stability, and information quality dimensions. The learned weights wkw\_{k} adapt to different market regimes, with βvol=0.50±0.05\beta\_{\text{vol}}=0.50\pm 0.05 for volatility scaling (see [Section˜H.2](https://arxiv.org/html/2602.06394v1#A8.SS2 "H.2 Quantitative Finance (QAT-QF) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") for complete parameter settings).

Metrics: Dir. = directional accuracy (%); Ret. MSE = return prediction MSE (normalized to BPE=1.0); Vol RMSE = volatility forecast RMSE; Order Flow = order imbalance prediction R2R^{2}; Regime F1 = market regime classification F1; Tail Risk = VaR exceedance prediction F1; Rotation = sector rotation strategy Sharpe ratio.

Table 7: Financial foundation model evaluation (100 test episodes).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Task | Zero-shot | | | Few-shot | | |
| BPE | QAT | Δ\Delta | BPE | QAT | Δ\Delta |
| Price Prediction | | | | | | |
| Dir. 5m | 52.3 | 58.7 | +12 | 61.2 | 68.3 | +12 |
| Dir. 1h | 51.8 | 57.2 | +10 | 59.4 | 65.8 | +11 |
| Dir. 1d | 50.9 | 54.6 | +7 | 56.7 | 61.2 | +8 |
| Ret. MSE | 1.00 | 0.81 | −-19 | 0.72 | 0.60 | −-18 |
| Volatility | | | | | | |
| Vol RMSE | .018 | .014 | −-23 | .013 | .010 | −-27 |
| GARCH Est. | .156 | .118 | −-24 | .098 | .071 | −-28 |
| Vol Regime | 71.2 | 79.8 | +12 | 82.3 | 88.4 | +7 |
| Microstructure | | | | | | |
| Spread | .023 | .019 | −-20 | .018 | .013 | −-25 |
| Volume | 31.2 | 24.8 | −-21 | 22.6 | 17.3 | −-24 |
| Order Flow | .412 | .523 | +27 | .567 | .681 | +20 |
| Risk | | | | | | |
| Regime F1 | .673 | .751 | +12 | .798 | .856 | +7 |
| Drawdown | .682 | .743 | +9 | .761 | .812 | +7 |
| Tail Risk | .412 | .486 | +18 | .523 | .598 | +14 |
| Cross-Asset | | | | | | |
| Corr. Pred. | .623 | .694 | +11 | .712 | .768 | +8 |
| Lead-Lag | 58.3 | 64.7 | +11 | 67.2 | 73.1 | +9 |
| Rotation | 1.23 | 1.41 | +15 | 1.52 | 1.72 | +13 |
| Avg. Δ\Delta | — | — | +16% | — | — | +13% |

Financial Results: QAT-QF achieves 7.3–27.0% zero-shot improvements, largest in volatility/microstructure tasks. Order flow imbalance (+27.0%) and regime detection (+11.6% F1) demonstrate QA-Token’s noise-filtering capability, consistent with our information-theoretic optimality result ([Proposition˜C.13](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem13 "Proposition C.13 (Quality-Aware Information Bottleneck Interpretation). ‣ C.9 Information-Theoretic Optimality ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). Implementation details in [Appendix˜F](https://arxiv.org/html/2602.06394v1#A6 "Appendix F Hyperparameter Sensitivity Analysis ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")–[Section˜G.3](https://arxiv.org/html/2602.06394v1#A7.SS3 "G.3 Computational Costs ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Computational Costs:
QA-Token requires 50–60 GPU-hours for vocabulary construction compared to minutes for standard BPE. However, this one-time cost is amortized across billions of inference operations: once constructed, the vocabulary imposes no additional inference overhead—tokenization speed is identical to BPE (∼10{\sim}10ms/sequence) as quality metrics are only used during construction. This efficiency is compatible with high-performance computing systems and in-storage processing architectures (Mansouri Ghiasi et al., [2022](https://arxiv.org/html/2602.06394v1#bib.bib100 "GenStore: a high-performance in-storage processing system for genome sequence analysis"); Ghiasi et al., [2022](https://arxiv.org/html/2602.06394v1#bib.bib101 "GenStore: in-storage filtering of genomic data for high-performance and energy-efficient genome analysis"), [2023](https://arxiv.org/html/2602.06394v1#bib.bib104 "MetaStore: high-performance metagenomic analysis via in-storage computing"); Mansouri Ghiasi et al., [2023](https://arxiv.org/html/2602.06394v1#bib.bib105 "MetaStore: high-performance metagenomic analysis via in-storage computing"); Ghiasi et al., [2024](https://arxiv.org/html/2602.06394v1#bib.bib106 "Megis: high-performance, energy-efficient, and low-cost metagenomic analysis with in-storage processing")). For foundation models where tokenization is performed once but affects billions of inference operations, the additional upfront cost is justified by substantial long-term gains; for small-scale applications or clean datasets, standard BPE may remain more practical.

## 7 Conclusion

QA-Token extends tokenization from frequency counting to quality-driven vocabulary construction, addressing limitations in processing noisy real-world data. We presented: (i) bilevel optimization with NP-hardness proof ([Theorem˜3.2](https://arxiv.org/html/2602.06394v1#S3.Thmtheorem2 "Theorem 3.2 (Computational Complexity). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), (ii) MDP formulation achieving (1−1/e)(1-1/e)-approximation ([Definition˜E.4](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem4 "Definition E.4 (Tokenization MDP). ‣ E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Proposition˜E.5](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem5 "Proposition E.5 (MDP Well-Formedness). ‣ E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜E.7](https://arxiv.org/html/2602.06394v1#A5.SS7 "E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), (iii) Gumbel-Softmax enabling end-to-end learning ([Theorem˜C.8](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem8 "Theorem C.8 (Gumbel-Softmax Properties). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). Our evaluation demonstrates consistent improvements: (1) genomics—6.7 pp F1 improvement, 94.53 MCC pathogen detection; (2) finance—30% Sharpe ratio increase; (3) foundation models achieve new benchmarks (analysis in [Appendix˜G](https://arxiv.org/html/2602.06394v1#A7 "Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")–[Section˜G.3](https://arxiv.org/html/2602.06394v1#A7.SS3 "G.3 Computational Costs ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). As biological sequence archives scale to petabases (Karasikov et al., [2025](https://arxiv.org/html/2602.06394v1#bib.bib111 "Efficient and accurate search in petabase-scale sequence repositories")) and variant prediction methods achieve unprecedented accuracy (Avsec et al., [2026](https://arxiv.org/html/2602.06394v1#bib.bib112 "Advancing regulatory variant effect prediction with AlphaGenome")), quality-aware tokenization becomes essential for bridging the gap between data availability and foundation model usability.

### 7.1 Scientific and Economic Impact

QA-Token enables utilization of massive noisy datasets previously considered unusable, fundamentally expanding the data frontier for foundation model training.

Scientific Acceleration in Genomics.
The Sequence Read Archive (SRA) contains over 67 petabases of publicly available genomic data—equivalent to reading the human genome 22 million times—yet a substantial fraction remains underutilized due to quality heterogeneity (Leinonen et al., [2011](https://arxiv.org/html/2602.06394v1#bib.bib110 "The sequence read archive")). Recent infrastructure advances have made these petabase-scale archives full-text searchable at economical costs (Karasikov et al., [2025](https://arxiv.org/html/2602.06394v1#bib.bib111 "Efficient and accurate search in petabase-scale sequence repositories")), and state-of-the-art methods like AlphaGenome now enable precise prediction of regulatory variant effects (Avsec et al., [2026](https://arxiv.org/html/2602.06394v1#bib.bib112 "Advancing regulatory variant effect prediction with AlphaGenome")). However, the gap between data *accessibility* and data *usability* for foundation model training persists: standard tokenization methods either discard low-quality reads entirely or propagate sequencing errors into learned representations. QA-Token bridges this gap by enabling quality-aware tokenization that can leverage the full breadth of available sequence data. We demonstrate three key applications: (1) *Pandemic surveillance*—environmental samples for pathogen monitoring contain 40–60% noise from contamination and sequencing errors; QA-Token directly trains on such noisy metagenomic data (Gollwitzer et al., [2023b](https://arxiv.org/html/2602.06394v1#bib.bib107 "MetaTrinity: enabling fast metagenomic classification via seed counting and edit distance approximation"), [a](https://arxiv.org/html/2602.06394v1#bib.bib103 "MetaFast: enabling fast metagenomic classification via seed counting and edit distance approximation"), [2025a](https://arxiv.org/html/2602.06394v1#bib.bib536 "MetaOmics-10t: the foundational dataset to unlock causal modeling of microbial ecosystems")), achieving 94.53 MCC on pathogen detection and enabling real-time global pandemic monitoring using previously unusable environmental samples. (2) *Drug discovery*—long-read sequencing for structural variants has 10–15% error rates; our 6.7 percentage point F1 improvement in variant calling accelerates identification of drug targets from complex genomic rearrangements, complementing advances in regulatory variant prediction (Avsec et al., [2026](https://arxiv.org/html/2602.06394v1#bib.bib112 "Advancing regulatory variant effect prediction with AlphaGenome")). (3) *Evolutionary biology*—ancient DNA is heavily degraded with >>50% damage; quality-aware tokenization preserves authentic ancient sequences while filtering damage, unlocking evolutionary insights from previously unanalyzable specimens.

Economic Impact in Finance.
Global financial markets generate 5TB of data per day, with 40% containing microstructure noise from market fragmentation and latency; current approaches require expensive data cleaning infrastructure costing millions annually. QA-Token delivers quantifiable economic value: (1) *Algorithmic trading*—30% Sharpe ratio improvement translates to billions in additional returns for large funds; 27% better order flow prediction reduces execution costs by basis points worth millions daily. (2) *Risk management*—18% improvement in tail risk estimation could have prevented billions in losses during market crashes; 11.6% better regime detection enables faster portfolio rebalancing. (3) *Democratization*—smaller institutions can now compete without expensive data cleaning infrastructure, reducing barriers to entry for quantitative trading strategies.

Broader Societal Impact.
Beyond genomics and finance, QA-Token has potential applications in: *Healthcare*—hospitals generate terabytes of noisy medical data daily; QA-Token enables training on real-world clinical data with artifacts, with potential to improve diagnostic accuracy and treatment recommendations, including applications in cancer treatment optimization (Gollwitzer et al., [2025b](https://arxiv.org/html/2602.06394v1#bib.bib537 "Steering the evolutionary game: hierarchical control of therapeutic resistance in cancer treatment")). *Climate science*—satellite imagery is often corrupted by cloud cover and atmospheric interference; QA-Token allows direct training on partially corrupted earth observation data, accelerating climate monitoring and prediction capabilities. *Infrastructure monitoring*—sensor networks produce petabytes of data with frequent failures; quality-aware tokenization enables robust anomaly detection despite sensor degradation, applicable to smart city applications and industrial IoT.

### 7.2 Limitations and Future Work

Limitations: (1) QA-Token requires domain-specific quality signals; domains without established metrics need custom design. (2) The vocabulary construction overhead limits rapid iteration during development. (3) Effective quality function design benefits from domain knowledge, though adaptive learning reduces sensitivity to initial choices.

Future Directions: (1) Universal quality metrics from data statistics (local entropy, consistency). (2) Online adaptation for streaming data. (3) Multimodal extension to vision-language and audio-text. (4) Efficiency via distillation and pruning.

## Impact Statement

Public sequence repositories now contain over 67 petabase pairs of raw sequencing data, with the European Nucleotide Archive doubling approximately every 45 months (Karasikov et al., [2025](https://arxiv.org/html/2602.06394v1#bib.bib111 "Efficient and accurate search in petabase-scale sequence repositories")). Recent advances have made these petabase-scale archives full-text searchable at costs as low as $0.74 per queried megabase pair, demonstrating that the infrastructure for large-scale sequence analysis is maturing rapidly. However, a substantial fraction of this data remains underutilized for foundation model training due to quality heterogeneity. QA-Token bridges this gap between data *accessibility* and data *usability*, enabling quality-aware tokenization that can leverage the full breadth of available sequence data for foundation model training.

Genomics. We achieve 94.53 MCC on pathogen detection from environmental samples containing 40–60% noise, enabling real-time pandemic surveillance using previously unusable metagenomic data. Our 6.7 percentage point F1 improvement in variant calling accelerates drug target identification from complex genomic rearrangements with 10–15% sequencing error rates. The same technology could theoretically be misused for biosurveillance; we have designed QA-Token for research purposes with standard institutional safeguards.

Finance. Global financial markets generate 5TB of data per day, with 40% containing microstructure noise. Our 30% Sharpe ratio improvement translates to quantifiable returns for algorithmic trading, while 27% better order flow prediction reduces execution costs. Enhanced trading performance raises concerns about market fairness; QA-Token provides incremental improvements within existing regulatory frameworks.

Resources. The 50–60 GPU-hour vocabulary construction cost is substantially lower than foundation model training costs, making QA-Token accessible to researchers with modest computational budgets. The highly compressed quality-aware vocabularies are portable for further analysis.

## Reproducibility Statement

We provide comprehensive details throughout the paper and appendices.

Theoretical contributions: All theorems and propositions include complete proofs ([Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.2](https://arxiv.org/html/2602.06394v1#A3.SS2 "C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5 "C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜C.9](https://arxiv.org/html/2602.06394v1#A3.SS9 "C.9 Information-Theoretic Optimality ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) with explicit assumptions ([Section˜C.6](https://arxiv.org/html/2602.06394v1#A3.SS6 "C.6 Assumptions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) and convergence guarantees ([Section˜E.4](https://arxiv.org/html/2602.06394v1#A5.SS4 "E.4 Convergence Properties ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Appendix˜E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Algorithms: Complete pseudocode for RL policy optimization (Algorithm [1](https://arxiv.org/html/2602.06394v1#alg1 "Algorithm 1 ‣ E.1.3 PPO Training Algorithm ‣ E.1 Stage 1: Reinforcement Learning Policy Optimization ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), adaptive parameter learning (Algorithm [2](https://arxiv.org/html/2602.06394v1#alg2 "Algorithm 2 ‣ E.2.2 Gumbel-Softmax Differentiable Optimization ‣ E.2 Stage 2: Adaptive Parameter Learning ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), and final vocabulary construction (Algorithm [3](https://arxiv.org/html/2602.06394v1#alg3 "Algorithm 3 ‣ E.3 Final Vocabulary Construction ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) are provided in [Appendix˜E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Implementation: Domain-specific quality metrics with exact formulas ([Section˜2](https://arxiv.org/html/2602.06394v1#S2 "2 Quality Metrics for Noisy Domains ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Appendix˜D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), hyperparameters for all models ([Section˜H.1](https://arxiv.org/html/2602.06394v1#A8.SS1 "H.1 Genomics (QA-BPE-seq) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [Section˜H.2](https://arxiv.org/html/2602.06394v1#A8.SS2 "H.2 Quantitative Finance (QAT-QF) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), and computational requirements ([Section˜G.3](https://arxiv.org/html/2602.06394v1#A7.SS3 "G.3 Computational Costs ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) are fully specified.

Experimental protocol: Statistical methodology including 10 independent trials, 95% confidence intervals, Welch’s t-test with Holm-Bonferroni correction, and effect sizes are detailed in [Section˜5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") and [Appendix˜G](https://arxiv.org/html/2602.06394v1#A7 "Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"). Dataset specifications, preprocessing steps, and evaluation metrics are provided in [Appendix˜G](https://arxiv.org/html/2602.06394v1#A7 "Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")–[Section˜I.2](https://arxiv.org/html/2602.06394v1#A9.SS2 "I.2 Dataset and Release Plan ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Baselines: Nine baseline methods with implementation details and hyperparameters are described in [Section˜5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") and [Section˜I.4](https://arxiv.org/html/2602.06394v1#A9.SS4 "I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Code release: We will provide a GitHub repository with all source code, trained models, and scripts to reproduce results.

### Conflict of Interest Statement

A.E.G. and D.d.G. are co-founders and shareholders of Anto Biosciences (YC F25).

D.A.S., P.L., and A.N.d.l.C. declare no competing interests.

## References

* A. A. Alemi, I. Fischer, J. V. Dillon, and K. Murphy (2017)
  Deep variational information bottleneck.
  In International Conference on Learning Representations (ICLR),
  Cited by: [§C.9](https://arxiv.org/html/2602.06394v1#A3.SS9.1.p1.2 "Proof. ‣ C.9 Information-Theoretic Optimality ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§4.5](https://arxiv.org/html/2602.06394v1#S4.SS5.p2.4 "4.5 Theoretical Guarantees ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* T. G. Andersen, T. Bollerslev, F. X. Diebold, and P. Labys (2001)
  The distribution of realized exchange rate volatility.
  Journal of the American statistical association 96 (453),  pp. 42–55.
  Cited by: [§1](https://arxiv.org/html/2602.06394v1#S1.p1.1 "1 Introduction ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. F. Ansari, L. Stella, C. Turkmen, X. Zhang, P. Mercado, H. Shen, O. Shchur, S. S. Rangapuram, S. Pineda Arango, S. Kapoor, et al. (2024)
  Chronos: learning the language of time series.
  arXiv preprint arXiv:2403.07815.
  Cited by: [§6.2](https://arxiv.org/html/2602.06394v1#S6.SS2.p1.1 "6.2 Financial Time-Series Foundation Model ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* Ž. Avsec, N. Latysheva, J. Cheng, et al. (2026)
  Advancing regulatory variant effect prediction with AlphaGenome.
  Nature 649,  pp. 1206–1218.
  External Links: [Document](https://dx.doi.org/10.1038/s41586-025-10014-0)
  Cited by: [§7.1](https://arxiv.org/html/2602.06394v1#S7.SS1.p2.1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§7](https://arxiv.org/html/2602.06394v1#S7.p1.1 "7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* T. Baldwin, P. Cook, M. Lui, A. MacKinlay, and L. Wang (2013)
  Noisy text analytics.
  In Proceedings of the Australasian Language Technology Association Workshop 2013,
   pp. 1–10.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* F. Barbieri, J. Camacho-Collados, L. Espinosa-Anke, and L. Neves (2020)
  TweetEval:Unified Benchmark and Comparative Evaluation for Tweet Classification.
  In Proceedings of Findings of EMNLP,
  Cited by: [1st item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.p1.1 "In 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [1st item](https://arxiv.org/html/2602.06394v1#A9.I6.i3.I1.i1.p1.1 "In 3rd item ‣ I.5 Evaluation Metrics ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* F. Barbieri, J. Camacho-Collados, F. Ronzano, L. Espinosa-Anke, M. Ballesteros, V. Basile, V. Patti, and H. Saggion (2018)
  Semeval 2018 task 2: multilingual emoji prediction.
  In Proceedings of The 12th International Workshop on Semantic Evaluation,
   pp. 24–33.
  Cited by: [2nd item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.I1.i2.p1.1 "In 1st item ‣ 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* V. Basile, C. Bosco, E. Fersini, D. Nozza, V. Patti, F. M. Rangel Pardo, P. Rosso, and M. Sanguinetti (2019)
  SemEval-2019 task 5: multilingual detection of hate speech against immigrants and women in Twitter.
  In Proceedings of the 13th International Workshop on Semantic Evaluation,
  Minneapolis, Minnesota, USA,  pp. 54–63.
  External Links: [Document](https://dx.doi.org/10.18653/v1/S19-2007)
  Cited by: [4th item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.I1.i4.p1.1 "In 1st item ‣ 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* I. Bello, H. Pham, Q. V. Le, M. Norouzi, and S. Bengio (2016)
  Neural combinatorial optimization with reinforcement learning.
  In International Conference on Learning Representations,
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p4.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Bhandari and D. Russo (2021)
  Global optimality guarantees for policy gradient methods.
  Operations Research 69 (6),  pp. 1744–1767.
  External Links: [Document](https://dx.doi.org/10.1287/opre.2021.0014)
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.6.p2.4 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§4.1](https://arxiv.org/html/2602.06394v1#S4.SS1.p1.2 "4.1 Reinforcement Learning Formulation ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* P. Bojanowski, E. Grave, A. Joulin, and T. Mikolov (2017)
  Enriching word vectors with subword information.
  In Transactions of the Association for Computational Linguistics,
  Vol. 5,  pp. 135–146.
  Cited by: [§D.3](https://arxiv.org/html/2602.06394v1#A4.SS3.p4.1 "D.3 Social Media: Linguistic Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [1st item](https://arxiv.org/html/2602.06394v1#A8.I6.i3.I1.i1.p1.3 "In 3rd item ‣ H.7 Domain-Specific Components ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Bolte, Q. Le, E. Pauwels, and S. Vaiter (2024)
  Geometric and computational hardness of bilevel programming.
  Mathematical programming.
  External Links: [Document](https://dx.doi.org/10.1007/s10107-025-02229-w)
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.p2.2 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* V. S. Borkar (2009)
  Stochastic approximation: a dynamical systems viewpoint.
   Hindustan Book Agency.
  Cited by: [§E.4](https://arxiv.org/html/2602.06394v1#A5.SS4.1.p1.2 "Proof. ‣ E.4 Convergence Properties ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. (2020)
  Language models are few-shot learners.
  In Advances in Neural Information Processing Systems,
  Vol. 33,  pp. 1877–1901.
  Cited by: [§I.4](https://arxiv.org/html/2602.06394v1#A9.SS4.p2.1 "I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* S. Cen and Y. Chi (2023)
  Global convergence of policy gradient methods in reinforcement learning, games and control.
  arXiv preprint arXiv:2310.05230.
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.6.p2.4 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Theorem 3.2](https://arxiv.org/html/2602.06394v1#S3.Thmtheorem2.p1.2.2 "Theorem 3.2 (Computational Complexity). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§4.1](https://arxiv.org/html/2602.06394v1#S4.SS1.p1.2 "4.1 Reinforcement Learning Formulation ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* B. Y. Chai, Z. Wang, and M. Sachan (2024)
  The curse of tokenization.
  arXiv preprint arXiv:2402.07831.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* K. W. Church and P. Hanks (1990)
  Word association norms, mutual information, and lexicography.
  Computational linguistics 16 (1),  pp. 22–29.
  Cited by: [§C.2](https://arxiv.org/html/2602.06394v1#A3.SS2.2.p2.1 "Proof. ‣ C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. H. Clark, D. Garcia, J. Botha, K. Lee, M. Luong, and Q. V. Le (2021)
  Canine: pre-training an efficient tokenization-free encoder for language representation.
  In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers),
   pp. 2647–2661.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.7.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p2.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. Das, W. Kong, A. Leach, R. Sen, and R. Yu (2024)
  TimesFM: a decoder-only foundation model for time-series forecasting.
  arXiv preprint arXiv:2310.10688.
  Cited by: [§6.2](https://arxiv.org/html/2602.06394v1#S6.SS2.p1.1 "6.2 Financial Time-Series Foundation Model ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* S. Dempe (2020)
  Bilevel optimization: theory, algorithms and applications.
  Springer Optimization and Its Applications, Vol. 161, Springer, Berlin, Germany.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-030-33566-3)
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.p2.2 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Theorem 3.2](https://arxiv.org/html/2602.06394v1#S3.Thmtheorem2.p1.2.2 "Theorem 3.2 (Computational Complexity). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* Y. Deng, F. Bao, Y. Kong, Z. Ren, and Q. Dai (2016)
  Deep direct reinforcement learning for financial signal representation and trading.
  IEEE transactions on neural networks and learning systems 28 (3),  pp. 653–664.
  Cited by: [§5.2](https://arxiv.org/html/2602.06394v1#S5.SS2.p3.1 "5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Devlin, M. Chang, K. Lee, and K. Toutanova (2019)
  Bert: pre-training of deep bidirectional transformers for language understanding.
  In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers),
   pp. 4171–4186.
  Cited by: [§I.4](https://arxiv.org/html/2602.06394v1#A9.SS4.p2.1 "I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* B. Ewing, L. Hillier, M. C. Wendl, and P. Green (1998)
  Base-calling of automated sequencer traces using phred. i. accuracy assessment.
  Genome research 8 (3),  pp. 175–185.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§1](https://arxiv.org/html/2602.06394v1#S1.p1.1 "1 Introduction ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* C. Finn, P. Abbeel, and S. Levine (2017)
  Model-agnostic meta-learning for fast adaptation of deep networks.
  In International conference on machine learning,
   pp. 1126–1135.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p5.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* R. Gençay, F. Selçuk, and B. Whitcher (2001)
  An introduction to wavelets and other filtering methods in finance and economics.
   Elsevier, San Diego.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* N. M. Ghiasi, J. Park, H. Mustafa, J. Kim, A. Olgun, A. Gollwitzer, D. S. Cali, C. Firtina, H. Mao, N. A. Alserr, et al. (2022)
  GenStore: in-storage filtering of genomic data for high-performance and energy-efficient genome analysis.
  In 2022 IEEE Computer Society Annual Symposium on VLSI (ISVLSI),
   pp. 283–287.
  Cited by: [§6.2](https://arxiv.org/html/2602.06394v1#S6.SS2.p6.1 "6.2 Financial Time-Series Foundation Model ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* N. M. Ghiasi, M. Sadrosadati, H. Mustafa, A. Gollwitzer, C. Firtina, J. Eudine, H. Ma, J. Lindegger, M. B. Cavlak, M. Alser, et al. (2023)
  MetaStore: high-performance metagenomic analysis via in-storage computing.
  arXiv preprint arXiv:2311.12527.
  Cited by: [§6.2](https://arxiv.org/html/2602.06394v1#S6.SS2.p6.1 "6.2 Financial Time-Series Foundation Model ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* N. M. Ghiasi, M. Sadrosadati, H. Mustafa, A. Gollwitzer, C. Firtina, J. Eudine, H. Mao, J. Lindegger, M. B. Cavlak, M. Alser, et al. (2024)
  Megis: high-performance, energy-efficient, and low-cost metagenomic analysis with in-storage processing.
  In 2024 ACM/IEEE 51st Annual International Symposium on Computer Architecture (ISCA),
   pp. 660–677.
  Cited by: [§6.2](https://arxiv.org/html/2602.06394v1#S6.SS2.p6.1 "6.2 Financial Time-Series Foundation Model ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. Gollwitzer, M. Alser, J. Bergtholdt, J. Lindegger, M. Rumpf, C. Firtina, S. Mangul, and O. Mutlu (2023a)
  MetaFast: enabling fast metagenomic classification via seed counting and edit distance approximation.
  arXiv,  pp. 2311–02029.
  Cited by: [§7.1](https://arxiv.org/html/2602.06394v1#S7.SS1.p2.1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. E. Gollwitzer, M. Alser, J. Bergtholdt, J. Lindegger, M. Rumpf, C. Firtina, S. Mangul, and O. Mutlu (2023b)
  MetaTrinity: enabling fast metagenomic classification via seed counting and edit distance approximation.
  arXiv preprint arXiv:2311.02029.
  Cited by: [§7.1](https://arxiv.org/html/2602.06394v1#S7.SS1.p2.1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. E. Gollwitzer, D. A. Subramanian, I. Tucker, and G. Traverso (2025a)
  MetaOmics-10t: the foundational dataset to unlock causal modeling of microbial ecosystems.
  In NeurIPS 2025 AI for Science Workshop,
  Cited by: [§7.1](https://arxiv.org/html/2602.06394v1#S7.SS1.p2.1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. E. Gollwitzer, D. A. Subramanian, I. Tucker, and G. Traverso (2025b)
  Steering the evolutionary game: hierarchical control of therapeutic resistance in cancer treatment.
  In NeurIPS 2025 AI for Science Workshop,
  Cited by: [§7.1](https://arxiv.org/html/2602.06394v1#S7.SS1.p4.1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* D. Golovin and A. Krause (2011)
  Adaptive submodularity: theory and applications in active learning and stochastic optimization.
  In Proceedings of the 24th International Conference on Neural Information Processing Systems,
   pp. 2675–2683.
  Cited by: [§C.7](https://arxiv.org/html/2602.06394v1#A3.SS7.1.p1.5 "Proof sketch. ‣ C.7 Theory Extensions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§C.7](https://arxiv.org/html/2602.06394v1#A3.SS7.2.p1.2 "Proof. ‣ C.7 Theory Extensions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* C. Grne and L. Wulf (2023)
  Completeness in the polynomial hierarchy for many natural problems in bilevel and robust optimization.
  Conference on Integer Programming and Combinatorial Optimization.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-031-93112-3%5F19)
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.p2.2 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. D. Hamilton (1989)
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  Econometrica: Journal of the Econometric Society,  pp. 357–384.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* B. Han, P. Cook, and T. Baldwin (2013)
  Lexical normalisation of short text messages: makn sens a #twitter.
  In Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
   pp. 368–378.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§H.8](https://arxiv.org/html/2602.06394v1#A8.SS8.p1.5 "H.8 Further Details on Social Media Noise Models ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* P. R. Hansen and A. Lunde (2006)
  Realized variance and market microstructure noise.
  Journal of Business & Economic Statistics 24 (2),  pp. 127–161.
  Cited by: [§1](https://arxiv.org/html/2602.06394v1#S1.p2.1 "1 Introduction ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Harrow, A. Frankish, J. M. Gonzalez, E. Tapanari, B. Aken, D. Barrell, J. M. Mudge, E. FRecognision, A. GCoil, A. LNCipedia, et al. (2012)
  GENCODE: the reference human genome annotation for the encode project.
  Genome research 22 (9),  pp. 1760–1774.
  Cited by: [1st item](https://arxiv.org/html/2602.06394v1#A8.I6.i1.p1.3 "In H.7 Domain-Specific Components ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Hasbrouck (1991)
  Measuring the information content of stock trades.
  The Journal of Finance 46 (1),  pp. 179–207.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* K. Heafield (2011)
  KenLM: faster and smaller language model queries.
  In Proceedings of the Sixth Workshop on Statistical Machine Translation,
   pp. 187–197.
  Cited by: [§D.3](https://arxiv.org/html/2602.06394v1#A4.SS3.p6.4 "D.3 Social Media: Linguistic Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* M. Heinzinger, A. Elnaggar, Y. Wang, C. Dallago, U. Neettiyath, and B. Rost (2019)
  Modeling aspects of the language of life through transfer-learning protein sequences.
  BMC bioinformatics 20 (1),  pp. 1–17.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* G. Hinton, O. Vinyals, and J. Dean (2015)
  Distilling the knowledge in a neural network.
  External Links: 1503.02531
  Cited by: [item 2](https://arxiv.org/html/2602.06394v1#A9.I7.i2.p1.1 "In I.7 Approximating QA-Token: Towards Computationally Efficient Quality-Awareness ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* R. Huang and T. Polak (2011)
  LOBSTER: limit order book reconstruction system.
  Available at SSRN 1920143.
  Cited by: [1st item](https://arxiv.org/html/2602.06394v1#A9.I1.i2.I1.i1.p1.1 "In 2nd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.2](https://arxiv.org/html/2602.06394v1#S5.SS2.p1.3 "5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* W. Huang, L. Li, J. R. Myers, and G. T. Marth (2012)
  ART: a next-generation sequencing read simulator.
  Bioinformatics 28 (4),  pp. 593–594.
  Cited by: [1st item](https://arxiv.org/html/2602.06394v1#A9.I1.i1.I1.i1.p1.1 "In 1st item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p1.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J.P. Morgan (1996)
  RiskMetrics technical document.
  Technical report
   J.P. Morgan/Reuters.
  Cited by: [§D.2](https://arxiv.org/html/2602.06394v1#A4.SS2.p4.4 "D.2 Finance: Comprehensive Market Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* E. Jang, S. Gu, and B. Poole (2017)
  Categorical reparameterization with gumbel-softmax.
  In International Conference on Learning Representations,
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p5.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.7.p1.4 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.9.p1.1 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§4.3](https://arxiv.org/html/2602.06394v1#S4.SS3.p1.8 "4.3 Adaptive Learning of Tokenization Parameters ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* Y. Ji, Z. Zhou, H. Liu, and R. V. Davuluri (2021)
  DNABERT: pre-trained bidirectional encoder representations from transformers model for dna-language in genome.
  Bioinformatics 37 (15),  pp. 2112–2120.
  Cited by: [4th item](https://arxiv.org/html/2602.06394v1#A9.I5.i4.p1.1 "In I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.4](https://arxiv.org/html/2602.06394v1#A9.SS4.p2.1 "I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p2.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* D. R. Jones, M. Schonlau, and W. J. Welch (1998)
  Efficient global optimization of expensive black-box functions.
  Journal of Global optimization 13 (4),  pp. 455–492.
  Cited by: [item 3](https://arxiv.org/html/2602.06394v1#A9.I7.i3.p1.2 "In I.7 Approximating QA-Token: Towards Computationally Efficient Quality-Awareness ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* M. Karasikov, H. Mustafa, D. Danciu, L. Bosshard, M. Zimmermann, K. Schütze, A. Kahles, and G. Rätsch (2025)
  Efficient and accurate search in petabase-scale sequence repositories.
  Nature 647,  pp. 1036–1044.
  External Links: [Document](https://dx.doi.org/10.1038/s41586-025-09603-w)
  Cited by: [§1](https://arxiv.org/html/2602.06394v1#S1.p3.1 "1 Introduction ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§7.1](https://arxiv.org/html/2602.06394v1#S7.SS1.p2.1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§7](https://arxiv.org/html/2602.06394v1#S7.p1.1 "7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Impact Statement](https://arxiv.org/html/2602.06394v1#Sx1.p1.1 "Impact Statement ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* R. M. Karp (1972)
  Reducibility among combinatorial problems.
  In Complexity of Computer Computations,
   pp. 85–103.
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.p1.5 "Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* D. P. Kingma and J. Ba (2014)
  Adam: a method for stochastic optimization.
  arXiv preprint arXiv:1412.6980.
  Cited by: [§E.4](https://arxiv.org/html/2602.06394v1#A5.SS4.3.p1.1 "Proof. ‣ E.4 Convergence Properties ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [5th item](https://arxiv.org/html/2602.06394v1#A8.I8.i1.I1.i5.p1.3 "In 1st item ‣ H.9.2 Genomics (QA-BPE-seq) ‣ H.9 Domain-Specific Algorithms ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* T. Kudo and J. Richardson (2018)
  SentencePiece: a simple and language independent subword tokenizer and detokenizer for neural text processing.
  In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing: System Demonstrations,
   pp. 66–71.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.5.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p2.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [2nd item](https://arxiv.org/html/2602.06394v1#A9.I5.i2.p1.1 "In I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.4](https://arxiv.org/html/2602.06394v1#A9.SS4.p2.1 "I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p2.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* T. Kudo (2018)
  Subword regularization: improving neural network translation models with multiple subword candidates.
  In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
   pp. 66–75.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p2.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* R. Leinonen, H. Sugawara, M. Shumway, and International Nucleotide Sequence Database Collaboration (2011)
  The sequence read archive.
  Nucleic Acids Research 39 (suppl\_1),  pp. D19–D21.
  Cited by: [§7.1](https://arxiv.org/html/2602.06394v1#S7.SS1.p2.1 "7.1 Scientific and Economic Impact ‣ 7 Conclusion ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Li, Y. Park, Y. Song, and S. Park (2020)
  An empirical study of tokenization strategies for various korean nlp tasks.
  In Proceedings of the 12th language resources and evaluation conference,
   pp. 6813–6819.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Libovick‘y and M. Sachan (2024)
  Semantic segmentation for improving the performance of large language models.
  In Findings of the Association for Computational Linguistics: ACL 2024,
   pp. 4930–4945.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.9.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p5.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* H. Lin and J. Bilmes (2011)
  A class of submodular functions for document summarization.
  In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies,
   pp. 510–520.
  Cited by: [§C.7](https://arxiv.org/html/2602.06394v1#A3.SS7.p1.2 "C.7 Theory Extensions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Lin, E. Keogh, S. Lonardi, and B. Chiu (2003)
  Symbolic representation of time series, with implications for streaming algorithms.
  In Proceedings of the 8th ACM SIGMOD workshop on Research issues in data mining and knowledge discovery,
   pp. 2–11.
  Cited by: [5th item](https://arxiv.org/html/2602.06394v1#A9.I5.i5.p1.1 "In I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [2nd item](https://arxiv.org/html/2602.06394v1#S5.I3.i2.p1.1 "In 5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* O. Liu et al. (2025)
  METAGENE-1: metagenomic foundation model for pandemic monitoring.
  arXiv preprint arXiv:2501.02045.
  Cited by: [§6.1](https://arxiv.org/html/2602.06394v1#S6.SS1.p1.1 "6.1 Metagenomics Foundation Model: METAGENE-1 7B ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* C. J. Maddison, A. Mnih, and Y. W. Teh (2017)
  The concrete distribution: a continuous relaxation of discrete random variables.
  In International Conference on Learning Representations,
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p5.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.7.p1.4 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.9.p1.1 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§4.3](https://arxiv.org/html/2602.06394v1#S4.SS3.p1.8 "4.3 Adaptive Learning of Tokenization Parameters ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. Madhavan (2000)
  Market microstructure: a survey.
  Journal of financial markets 3 (3),  pp. 205–258.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p3.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* N. Mansouri Ghiasi, J. Park, H. Mustafa, J. Kim, A. Olgun, A. Gollwitzer, D. Senol Cali, C. Firtina, H. Mao, N. Almadhoun Alserr, et al. (2022)
  GenStore: a high-performance in-storage processing system for genome sequence analysis.
  In Proceedings of the 27th ACM International Conference on Architectural Support for Programming Languages and Operating Systems,
   pp. 635–654.
  Cited by: [§6.2](https://arxiv.org/html/2602.06394v1#S6.SS2.p6.1 "6.2 Financial Time-Series Foundation Model ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* N. Mansouri Ghiasi, M. Sadrosadati, H. Mustafa, A. Gollwitzer, C. Firtina, J. Eudine, H. Ma, J. Lindegger, M. Banu Cavlak, M. Alser, et al. (2023)
  MetaStore: high-performance metagenomic analysis via in-storage computing.
  arXiv e-prints,  pp. arXiv–2311.
  Cited by: [§6.2](https://arxiv.org/html/2602.06394v1#S6.SS2.p6.1 "6.2 Financial Time-Series Foundation Model ‣ 6 Foundation Model Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* S. Mohammad, F. Bravo-Marquez, M. Salameh, and S. Kiritchenko (2018)
  Semeval-2018 task 1: affect in tweets.
  In Proceedings of the 12th international workshop on semantic evaluation,
   pp. 1–17.
  Cited by: [1st item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.I1.i1.p1.1 "In 1st item ‣ 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* S. Mohammad, S. Kiritchenko, P. Sobhani, X. Zhu, and C. Cherry (2016)
  Semeval-2016 task 6: detecting stance in tweets.
  In Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016),
   pp. 31–41.
  Cited by: [7th item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.I1.i7.p1.1 "In 1st item ‣ 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Moody and M. Saffell (2001)
  Performance functions and reinforcement learning for trading systems and portfolios.
  Journal of Forecasting 20 (1),  pp. 1–18.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p4.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Moody and L. Wu (1998)
  Learning to trade via direct reinforcement.
  In Proceedings of the IEEE International Conference on Neural Networks,
   pp. 1741–1746.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p4.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* D. Q. Nguyen, T. Vu, and A. T. Nguyen (2020)
  BERTweet: a pre-trained language model for english tweets.
  In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations,
   pp. 9–14.
  Cited by: [1st item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.p1.2 "In 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. B. Owen (2013)
  Monte carlo theory, methods and examples.
   Stanford University.
  Note: Available at <https://artowen.su.domains/mc/>
  Cited by: [§G.3](https://arxiv.org/html/2602.06394v1#A7.SS3.1.p1.7 "Proof Sketch. ‣ G.3 Computational Costs ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* I. Provilkov, D. Emelyanenko, and E. Voita (2020)
  BPE-dropout: simple and effective subword regularization.
  In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,
   pp. 1882–1892.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.6.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p2.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [1st item](https://arxiv.org/html/2602.06394v1#S5.I3.i1.p1.1 "In 5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p2.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* M. Ranzato, S. Chopra, M. Auli, and W. Zaremba (2015)
  Sequence level training with recurrent neural networks.
  In International Conference on Learning Representations,
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p4.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Rissanen (1978)
  Modeling by shortest data description.
  Automatica 14 (5),  pp. 465–471.
  Cited by: [§C.2](https://arxiv.org/html/2602.06394v1#A3.SS2.3.p3.1 "Proof. ‣ C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§3.2](https://arxiv.org/html/2602.06394v1#S3.SS2.p2.10 "3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* S. Rosenthal, N. Farra, and P. Nakov (2017)
  SemEval-2017 task 4: sentiment analysis in twitter.
  In Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017),
   pp. 502–518.
  Cited by: [6th item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.I1.i6.p1.1 "In 1st item ‣ 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* M. Rumpf, M. Alser, A. E. Gollwitzer, J. Lindegger, N. Almadhoun, C. Firtina, S. Mangul, and O. Mutlu (2023)
  SequenceLab: a comprehensive benchmark of computational methods for comparing genomic sequences.
  arXiv preprint arXiv:2310.16908.
  Cited by: [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p4.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. A. Rusu, S. G. Colmenarejo, C. Gulcehre, G. Desjardins, J. Kirkpatrick, R. Pascanu, V. Mnih, K. Kavukcuoglu, and R. Hadsell (2016)
  Policy distillation.
  External Links: 1511.06295
  Cited by: [item 2](https://arxiv.org/html/2602.06394v1#A9.I7.i2.p1.1 "In I.7 Approximating QA-Token: Towards Computationally Efficient Quality-Awareness ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* P. Schäfer (2015)
  The boss is concerned with time series classification in the presence of noise.
  Data Mining and Knowledge Discovery 29 (6),  pp. 1505–1530.
  Cited by: [6th item](https://arxiv.org/html/2602.06394v1#A9.I5.i6.p1.1 "In I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [2nd item](https://arxiv.org/html/2602.06394v1#S5.I3.i2.p1.1 "In 5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov (2017)
  Proximal policy optimization algorithms.
  In arXiv preprint arXiv:1707.06347,
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.5.p1.2 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§4.1](https://arxiv.org/html/2602.06394v1#S4.SS1.p1.2 "4.1 Reinforcement Learning Formulation ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. Sczyrba, P. Hofmann, P. Belmann, D. Koslicki, S. Janssen, J. Dr"oge, I. Gregor, S. Majda, J. Fiedler, E. Dahms, et al. (2017)
  Critical assessment of metagenome interpretation—a benchmark of metagenomics software.
  Nature methods 14 (11),  pp. 1063–1071.
  Cited by: [3rd item](https://arxiv.org/html/2602.06394v1#A9.I1.i1.I1.i3.p1.1 "In 1st item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p1.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* R. Sennrich, B. Haddow, and A. Birch (2016)
  Neural machine translation of rare words with subword units.
  In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
   pp. 1715–1725.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.5.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p2.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§C.2](https://arxiv.org/html/2602.06394v1#A3.SS2.1.p1.1 "Proof. ‣ C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§C.3](https://arxiv.org/html/2602.06394v1#A3.SS3.2.p2.1 "Proof. ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [1st item](https://arxiv.org/html/2602.06394v1#A9.I5.i1.p1.1 "In I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.4](https://arxiv.org/html/2602.06394v1#A9.SS4.p2.1 "I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§1](https://arxiv.org/html/2602.06394v1#S1.p1.1 "1 Introduction ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y.K. Li, Y. Wu, and D. Guo (2024)
  DeepSeekMath: pushing the limits of mathematical reasoning in open language models.
  arXiv preprint arXiv:2402.03300.
  Cited by: [§G.5.1](https://arxiv.org/html/2602.06394v1#A7.SS5.SSS1.p1.1 "G.5.1 RL Algorithm Ablation ‣ G.5 Ablation Studies and Additional Experiments ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* W. F. Sharpe (1994)
  The sharpe ratio.
  Journal of portfolio management 21 (1),  pp. 49–58.
  Cited by: [4th item](https://arxiv.org/html/2602.06394v1#A9.I6.i2.I1.i4.p1.1 "In 2nd item ‣ I.5 Evaluation Metrics ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.2](https://arxiv.org/html/2602.06394v1#S5.SS2.p3.1 "5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* S. T. Sherry, M. Ward, M. Kholodov, J. Baker, L. Phan, E. M. Smigielski, and K. Sirotkin (2001)
  DbSNP: the ncbi database of genetic variation.
  Nucleic acids research 29 (1),  pp. 308–311.
  Cited by: [4th item](https://arxiv.org/html/2602.06394v1#A8.I1.i4.p1.1 "In H.1 Genomics (QA-BPE-seq) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [1st item](https://arxiv.org/html/2602.06394v1#A8.I6.i1.p1.3 "In H.7 Domain-Specific Components ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. Subramanyam, Y. Chen, and R. L. Grossman (2025)
  Scaling laws revisited: modeling the role of data quality in language model pretraining.
  arXiv.org.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.2510.03313)
  Cited by: [§1](https://arxiv.org/html/2602.06394v1#S1.p1.1 "1 Introduction ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* R. S. Sutton and A. G. Barto (2018)
  Reinforcement learning: an introduction.
   MIT press.
  Cited by: [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p4.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* Y. Tay, V. Q. Tran, S. Ruder, J. Gupta, L. Liu, J. Chung, S. Turner, Z. Wang, D. Williams, D. G. Casas, et al. (2022)
  Charformer: fast character transformers via gradient-based subword tokenization.
  arXiv preprint arXiv:2106.12672.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.8.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p5.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p2.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* N. Tishby, F. C. Pereira, and W. Bialek (1999)
  The information bottleneck method.
  In Proceedings of the 37th Annual Allerton Conference on Communication,
  Control and Computing,
   pp. 368–377.
  Cited by: [§C.9](https://arxiv.org/html/2602.06394v1#A3.SS9.1.p1.2 "Proof. ‣ C.9 Information-Theoretic Optimality ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§4.5](https://arxiv.org/html/2602.06394v1#S4.SS5.p2.4 "4.5 Theoretical Guarantees ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* C. Van Hee, E. Lefever, and V. Hoste (2018)
  Semeval-2018 task 3: irony detection in english tweets.
  In Proceedings of The 12th International Workshop on Semantic Evaluation,
   pp. 39–50.
  Cited by: [3rd item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.I1.i3.p1.1 "In 1st item ‣ 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* A. M. Wenger, P. Peluso, W. J. Rowell, P. Chang, R. J. Hall, G. T. Concepcion, J. Ebler, A. Fungtammasan, A. Kolesnikov, N. D. Olson, et al. (2019)
  Accurate circular consensus long-read sequencing improves variant detection and assembly of a human genome.
  Nature biotechnology 37 (10),  pp. 1155–1162.
  Cited by: [§1](https://arxiv.org/html/2602.06394v1#S1.p2.1 "1 Introduction ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* R. J. Williams (1992)
  Simple statistical gradient-following algorithms for connectionist reinforcement learning.
  Machine learning 8 (3-4),  pp. 229–256.
  Cited by: [§C.5](https://arxiv.org/html/2602.06394v1#A3.SS5.SSS0.Px1.8.p2.5 "Proof. ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* Y. Wu, M. Schuster, Z. Chen, Q. V. Le, M. Norouzi, W. Macherey, M. Krikun, Y. Cao, Q. Gao, K. Macherey, et al. (2016)
  Google’s neural machine translation system: bridging the gap between human and machine translation.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.5.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [Appendix B](https://arxiv.org/html/2602.06394v1#A2.p2.1 "Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [3rd item](https://arxiv.org/html/2602.06394v1#A9.I5.i3.p1.1 "In I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.4](https://arxiv.org/html/2602.06394v1#A9.SS4.p2.1 "I.4 Baseline Methods ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* L. Xue, A. Barua, N. Constant, R. Al-Rfou, S. Narang, M. Kale, A. Roberts, and C. Raffel (2022)
  ByT5: towards a token-free future with pre-trained byte-to-byte models.
  Transactions of the Association for Computational Linguistics 10,  pp. 291–306.
  Cited by: [Table 9](https://arxiv.org/html/2602.06394v1#A2.T9.3.3.7.1 "In Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p2.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* Y. Yue et al. (2025)
  Does reinforcement learning really incentivize reasoning capacity in LLMs beyond the base model?.
  arXiv preprint arXiv:2504.13837.
  Note: Presented at NeurIPS 2025 (Oral), ICML 2025 AI4Math Workshop Best Paper
  Cited by: [§G.5.1](https://arxiv.org/html/2602.06394v1#A7.SS5.SSS1.p1.1 "G.5.1 RL Algorithm Ablation ‣ G.5 Ablation Studies and Additional Experiments ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* M. Zampieri, S. Malmasi, P. Nakov, S. Rosenthal, N. Farra, and R. Kumar (2019)
  SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval).
  In Proceedings of the 13th International Workshop on Semantic Evaluation,
   pp. 75–86.
  Cited by: [5th item](https://arxiv.org/html/2602.06394v1#A9.I1.i3.I1.i1.I1.i5.p1.1 "In 1st item ‣ 3rd item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§I.8](https://arxiv.org/html/2602.06394v1#A9.SS8.p2.1 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
* J. M. Zook, D. Catoe, J. McDaniel, L. Vang, N. Spies, A. Sidow, Z. Weng, and M. Salit (2016)
  Extensive sequencing of seven human genomes to characterize benchmark reference materials.
  Scientific data 3 (1),  pp. 1–19.
  Cited by: [2nd item](https://arxiv.org/html/2602.06394v1#A9.I1.i1.I1.i2.p1.1 "In 1st item ‣ I.1 Datasets and Reproducible Evaluation ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"),
  [§5.1](https://arxiv.org/html/2602.06394v1#S5.SS1.p1.1 "5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

## Supplementary Information

## Appendix A Notation

To ensure clarity and rigor, we define our mathematical notation in Table [8](https://arxiv.org/html/2602.06394v1#A1.T8 "Table 8 ‣ Appendix A Notation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"). We distinguish between atomic (indivisible) elements and tokens (sequences of atomic elements or other tokens).

Table 8: Table of Notation

|  |  |
| --- | --- |
| Symbol | Definition |
| Σ\Sigma | Base alphabet of atomic elements (e.g., characters, DNA bases). |
| sis\_{i} | An atomic element from Σ\Sigma. |
| qiq\_{i} | Scalar quality score of an atomic element sis\_{i}, where qi∈[0,1]q\_{i}\in[0,1]. |
| t,a,bt,a,b | Tokens, which are sequences of atomic elements. |
| VkV\_{k} | Vocabulary at merge step kk. |
| f​(t)f(t) | Frequency of token tt in the corpus. |
| |t||t| | Length of token tt in atomic elements. |
| nσ​(t)n\_{\sigma}(t) | Count of atomic element σ∈Σ\sigma\in\Sigma within token tt. |
| H​(t)H(t) | Empirical entropy of token tt: H​(t)=−∑σnσ​(t)|t|​log⁡nσ​(t)|t|H(t)=-\sum\_{\sigma}\frac{n\_{\sigma}(t)}{|t|}\log\frac{n\_{\sigma}(t)}{|t|}. |
| 𝒒t\bm{q}\_{t} | Vector of quality scores for token tt (in multi-dimensional domains). |
| qtq\_{t} | Aggregated scalar quality score of token tt, derived from its constituents. |
| q¯a​b\bar{q}\_{ab} | Average quality of constituent tokens a,ba,b, defined as (qa+qb)/2(q\_{a}+q\_{b})/2. |
| α\alpha | Learnable exponent controlling sensitivity to quality in the merge score. |
| wa​bw\_{ab} | Quality-aware merge score for the token pair (a,b)(a,b). |
| θadapt\theta\_{\text{adapt}} | Vector of all learnable adaptive parameters in the framework. |
| πθπ\pi\_{\theta\_{\pi}} | Reinforcement learning policy for selecting merges, parameterized by θπ\theta\_{\pi}. |
| LtaskL\_{\text{task}} | Loss function of the downstream machine learning task. |
| 𝒥​(𝒯)\mathcal{J}(\mathcal{T}) | Global objective function for the tokenization process (Eq. [1](https://arxiv.org/html/2602.06394v1#S3.E1 "Equation 1 ‣ Definition 3.1 (Bilevel Tokenization Problem). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). |

## Appendix B Related Work

QA-Token intersects with, and extends upon, research in subword tokenization, noisy data handling, reinforcement learning for sequential optimization, and adaptive or differentiable modeling techniques. Table [9](https://arxiv.org/html/2602.06394v1#A2.T9 "Table 9 ‣ Appendix B Related Work ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") provides a comparative overview, situating QA-Token relative to existing approaches and highlighting its unique synthesis of explicit quality integration, RL-based optimization of merges, and adaptive learning of the tokenization process parameters. The key distinction of QA-Token’s adaptive parameter learning is its focus on optimizing parameters governing the tokenization \*process\* itself (like quality sensitivity or reward component weights), rather than solely adapting the vocabulary content or segmentation boundaries within a fixed merge logic.

Table 9: Comparison of QA-Token with Representative Tokenization Approaches.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Method | Explicit Quality  Integration | Optimization  Method | Adaptive Params  (Learned Process?) | Downstream Aware  (via Reward/Loss) | Domain Noise Model  (Explicit?) | Vocabulary  Type |
| Standard BPE/WP/SP (Sennrich et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib13 "Neural machine translation of rare words with subword units"); Wu et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib14 "Google’s neural machine translation system: bridging the gap between human and machine translation"); Kudo and Richardson, [2018](https://arxiv.org/html/2602.06394v1#bib.bib15 "SentencePiece: a simple and language independent subword tokenizer and detokenizer for neural text processing")) | No | Frequency | No | No | No | Subword |
| BPE-Dropout (Provilkov et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib26 "BPE-dropout: simple and effective subword regularization")) | No | Freq.+Stochastic | No | No | No | Subword |
| Char/Byte Models (Xue et al., [2022](https://arxiv.org/html/2602.06394v1#bib.bib27 "ByT5: towards a token-free future with pre-trained byte-to-byte models"); Clark et al., [2021](https://arxiv.org/html/2602.06394v1#bib.bib28 "Canine: pre-training an efficient tokenization-free encoder for language representation")) | No | N/A (Fixed) | No | Yes (via model) | Implicit | Char/Byte |
| Gradient-based (Tay et al., [2022](https://arxiv.org/html/2602.06394v1#bib.bib29 "Charformer: fast character transformers via gradient-based subword tokenization")) | No | Gradient | Yes (Segmenter) | Yes | Implicit | Char/Subword |
| Semantic Tokenizers (Libovick‘y and Sachan, [2024](https://arxiv.org/html/2602.06394v1#bib.bib30 "Semantic segmentation for improving the performance of large language models")) | No | Semantics+Freq | No | Indirectly | No | Subword |
| QA-Token (Ours) | Yes | RL (Policy) + | Yes (Process HPs: | Yes (via Reward for RL, | Yes (via Q,RQ,R) | Subword |
|  |  | Gradient (HPs) | α,λi,wj,βk\alpha,\lambda\_{i},w\_{j},\beta\_{k}) | LdownstreamL\_{\text{downstream}} for HPs) |  |  |

Note: "Adaptive Params (Learned Process?)" refers to learning parameters governing the tokenization \*process\* itself (like QA-Token’s α,βk,λi,wj\alpha,\beta\_{k},\lambda\_{i},w\_{j}), not just the vocabulary content or segmentation boundaries. QA-Token uses RL to optimize the merge policy and gradient-based methods to optimize these process hyperparameters.

Subword Tokenization Algorithms: The prevailing paradigm relies on frequency-based greedy merging procedures, exemplified by BPE (Sennrich et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib13 "Neural machine translation of rare words with subword units")), WordPiece (Wu et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib14 "Google’s neural machine translation system: bridging the gap between human and machine translation")) (which optimizes data likelihood), and SentencePiece (Kudo and Richardson, [2018](https://arxiv.org/html/2602.06394v1#bib.bib15 "SentencePiece: a simple and language independent subword tokenizer and detokenizer for neural text processing")) (which operates directly on raw text). While computationally efficient and broadly effective, their fundamental mechanism ignores sequence quality, providing the primary motivation for our work. BPE-dropout (Provilkov et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib26 "BPE-dropout: simple and effective subword regularization")) introduces stochasticity during the merge process as a form of regularization to enhance robustness, but it does not use explicit quality signals. Unigram language models (Kudo, [2018](https://arxiv.org/html/2602.06394v1#bib.bib34 "Subword regularization: improving neural network translation models with multiple subword candidates")) present a probabilistic alternative, yet they still primarily depend on frequency and likelihood objectives without explicit quality awareness.

Handling Noisy and Domain-Specific Data: Considerable research focuses on modeling noise within particular application domains. In genomics, Phred scores (Ewing et al., [1998](https://arxiv.org/html/2602.06394v1#bib.bib16 "Base-calling of automated sequencer traces using phred. i. accuracy assessment")) are standard quality indicators, and specialized models aim to account for sequencing errors (Heinzinger et al., [2019](https://arxiv.org/html/2602.06394v1#bib.bib10 "Modeling aspects of the language of life through transfer-learning protein sequences")). In NLP, extensive work on social media text addresses lexical variation, misspellings, and slang through techniques like text normalization (Han et al., [2013](https://arxiv.org/html/2602.06394v1#bib.bib18 "Lexical normalisation of short text messages: makn sens a #twitter"); Li et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib20 "An empirical study of tokenization strategies for various korean nlp tasks")) and explicit noise modeling (Baldwin et al., [2013](https://arxiv.org/html/2602.06394v1#bib.bib17 "Noisy text analytics")). Financial time series analysis frequently employs filtering methods (Gençay et al., [2001](https://arxiv.org/html/2602.06394v1#bib.bib25 "An introduction to wavelets and other filtering methods in finance and economics")), microstructure modeling (Madhavan, [2000](https://arxiv.org/html/2602.06394v1#bib.bib22 "Market microstructure: a survey"); Hasbrouck, [1991](https://arxiv.org/html/2602.06394v1#bib.bib23 "Measuring the information content of stock trades")), and regime-switching models (Hamilton, [1989](https://arxiv.org/html/2602.06394v1#bib.bib24 "A new approach to the economic analysis of nonstationary time series and the business cycle")) to manage inherent noise and non-stationarity. QA-Token distinguishes itself by offering a \*unified tokenization framework\* that directly integrates such domain-specific quality and noise considerations into the token construction process itself, rather than addressing noise solely as a separate downstream modeling challenge. The notion of the "curse of tokenization" (Chai et al., [2024](https://arxiv.org/html/2602.06394v1#bib.bib19 "The curse of tokenization")), which highlights the downstream impact of tokenization choices on LLM robustness, further underscores the need for quality-aware approaches.

Reinforcement Learning for Sequential Optimization: RL offers a robust framework for sequential decision-making under uncertainty (Sutton and Barto, [2018](https://arxiv.org/html/2602.06394v1#bib.bib36 "Reinforcement learning: an introduction")). It finds successful application in various optimization problems involving sequences, including text generation (Ranzato et al., [2015](https://arxiv.org/html/2602.06394v1#bib.bib37 "Sequence level training with recurrent neural networks")), combinatorial optimization (Bello et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib38 "Neural combinatorial optimization with reinforcement learning")), and financial strategy optimization (Moody and Wu, [1998](https://arxiv.org/html/2602.06394v1#bib.bib12 "Learning to trade via direct reinforcement"); Moody and Saffell, [2001](https://arxiv.org/html/2602.06394v1#bib.bib40 "Performance functions and reinforcement learning for trading systems and portfolios")). We uniquely formulate the tokenization vocabulary construction process as an RL problem where merge operations constitute actions selected by a learned policy to maximize a cumulative reward signal reflecting token quality, information content, complexity, and estimated utility. This formulation allows for optimizing complex, potentially non-differentiable objectives related to the quality of the final tokenization outcome. The rewards themselves are shaped by adaptively learned parameters (Section [4.3](https://arxiv.org/html/2602.06394v1#S4.SS3 "4.3 Adaptive Learning of Tokenization Parameters ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

Adaptive and Differentiable Tokenization: Acknowledging the limitations inherent in static tokenizers, researchers explore adaptive and learnable alternatives. Gradient-based approaches (Tay et al., [2022](https://arxiv.org/html/2602.06394v1#bib.bib29 "Charformer: fast character transformers via gradient-based subword tokenization")) learn segmentation parameters end-to-end concurrently with downstream tasks, often operating at the character level. Semantic tokenization (Libovick‘y and Sachan, [2024](https://arxiv.org/html/2602.06394v1#bib.bib30 "Semantic segmentation for improving the performance of large language models")) uses word meanings to inform the segmentation process. QA-Token integrates adaptive learning distinctively: it learns hyperparameters (α,βk,wj,λi,…\alpha,\beta\_{k},w\_{j},\lambda\_{i},\dots) that directly govern the quality-aware merge decisions and the RL agent’s reward structure. This learning is enabled by Gumbel-Softmax relaxation (Jang et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib31 "Categorical reparameterization with gumbel-softmax"); Maddison et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib32 "The concrete distribution: a continuous relaxation of discrete random variables")) for making merge choices differentiable with respect to these hyperparameters when optimizing a downstream task loss (via composite logits defined in Equation [37](https://arxiv.org/html/2602.06394v1#A5.E37 "Equation 37 ‣ E.11 Gradient Computation ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). This enables the fundamental \*tokenization logic\* to adapt based on observed data properties and task feedback, co-evolving with the RL agent’s policy. Meta-learning (Finn et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib33 "Model-agnostic meta-learning for fast adaptation of deep networks")) provides a potential mechanism, explored conceptually within QA-Token (see Appendix [E.5](https://arxiv.org/html/2602.06394v1#A5.SS5 "E.5 Algorithm Summary ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), to further accelerate adaptation across heterogeneous data sources (e.g., different social media platforms).

In essence, QA-Token synthesizes concepts from these related areas but provides a unique combination: explicit quality integration within the merge decision, optimization of the merge sequence via RL using a multi-faceted reward signal, and adaptive learning of core process parameters that define this reward and merge logic, demonstrating applicability across diverse, noisy domains.

## Appendix C Theoretical Framework and Proofs

### C.1 Quality Metric Proofs

###### Proposition C.1 (Boundedness and Continuity of Quality Functions).

All domain-specific quality functions qt∈[0,1]q\_{t}\in[0,1] are:

1. 1.

   Bounded: 0≤qt≤10\leq q\_{t}\leq 1 for all tokens tt
2. 2.

   Continuous: Lipschitz continuous in their arguments
3. 3.

   Monotonic: Quality decreases with increasing noise/error

###### Proof.

Boundedness: For genomics, the geometric mean of values in [0,1][0,1] remains in [0,1][0,1]. For finance, the convex combination of bounded components qk,t∈[0,1]q\_{k,t}\in[0,1] with ∑kwk=1\sum\_{k}w\_{k}=1 yields qtfinance∈[0,1]q\_{t}^{\text{finance}}\in[0,1].

Lipschitz continuity: For genomics (geometric mean on [ϵQ,1]n[\epsilon\_{Q},1]^{n}), the chain rule via logarithmic transformation yields Lipschitz constant Lg=1/(n⋅ϵQ)L\_{g}=1/(\sqrt{n}\cdot\epsilon\_{Q}). For finance, the weighted sum of Lipschitz component functions has Lf≤maxk⁡LkL\_{f}\leq\max\_{k}L\_{k}.

Monotonicity: For any noise injection η\eta with η​(q)≤q\eta(q)\leq q, both aggregations (geometric and arithmetic means) preserve the ordering: noisier inputs yield lower quality scores.
∎

### C.2 Merge Score Derivation

###### Lemma C.2 (First-Order Approximation).

The marginal gain in objective 𝒥\mathcal{J} from merge (a,b)↦a​b(a,b)\mapsto ab admits the decomposition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​𝒥​(a,b)=λLM​Δ​ℒLM−λcomp​Δ​Φ+λqual​Δ​Q+O​(ϵ2)\boxed{\Delta\mathcal{J}(a,b)=\lambda\_{\text{LM}}\Delta\mathcal{L}\_{\text{LM}}-\lambda\_{\text{comp}}\Delta\Phi+\lambda\_{\text{qual}}\Delta Q+O(\epsilon^{2})} |  | (4) |

where ϵ=1/|𝒮|\epsilon=1/|\mathcal{S}| represents the corpus-normalized perturbation.

###### Proof.

The marginal gain decomposes into three components following standard vocabulary optimization analysis (Sennrich et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib13 "Neural machine translation of rare words with subword units")).

Language Model Component: The change Δ​ℒLM≈f​(a,b)⋅PMI​(a,b)\Delta\mathcal{L}\_{\text{LM}}\approx f(a,b)\cdot\text{PMI}(a,b) follows from the pseudo-likelihood approximation, where PMI (Pointwise Mutual Information) captures statistical association (Church and Hanks, [1990](https://arxiv.org/html/2602.06394v1#bib.bib74 "Word association norms, mutual information, and lexicography")).

Complexity Component: By MDL principles (Rissanen, [1978](https://arxiv.org/html/2602.06394v1#bib.bib42 "Modeling by shortest data description")), merging reduces vocabulary complexity: Δ​Φ=−log⁡|V|−1+O​(|V|−1)\Delta\Phi=-\log|V|-1+O(|V|^{-1}). This compression benefit is absorbed into the PMI term, which also favors frequent co-occurrences.

Quality Component: For concave aggregator g​(x)=(x+ϵQ)αg(x)=(x+\epsilon\_{Q})^{\alpha}, Jensen’s inequality yields g​(q¯a​b)≥12​(g​(qa)+g​(qb))g(\bar{q}\_{ab})\geq\frac{1}{2}(g(q\_{a})+g(q\_{b})). The dominant quality contribution is Δ​Q+=f​(a,b)⋅g​(q¯a​b)\Delta Q\_{+}=f(a,b)\cdot g(\bar{q}\_{ab}) where q¯a​b=(qa+qb)/2\bar{q}\_{ab}=(q\_{a}+q\_{b})/2. Normalization errors are O​(f​(a,b)/T)O(f(a,b)/T), negligible for typical corpora.
∎

### C.3 Derivation of the Optimal Merge Score

###### Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic).

*Motivated by* the first-order approximation of Δ​𝒥\Delta\mathcal{J} (Lemma [C.2](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem2 "Lemma C.2 (First-Order Approximation). ‣ C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), we propose the following quality-aware merge score as a principled heuristic:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wa​b=f​(a,b)f​(a)​f​(b)+ϵf⋅(q¯a​b+ϵQ)α⋅ψ​(a,b)\boxed{w\_{ab}=\tfrac{f(a,b)}{f(a)f(b)+\epsilon\_{f}}\cdot(\bar{q}\_{ab}+\epsilon\_{Q})^{\alpha}\cdot\psi(a,b)} |  | (5) |

where:

* •

  f​(⋅)f(\cdot) denotes frequency in the corpus
* •

  q¯a​b=(qa+qb)/2\bar{q}\_{ab}=(q\_{a}+q\_{b})/2 is the average constituent quality
* •

  α∈(0,1]\alpha\in(0,1] is a learnable parameter controlling quality sensitivity
* •

  ϵf,ϵQ>0\epsilon\_{f},\epsilon\_{Q}>0 ensure numerical stability
* •

  ψ​(a,b)∈[0,1]\psi(a,b)\in[0,1] encodes domain-specific constraints

*Note:* The derivation below involves two principled approximations (Steps 4–5) that trade mathematical exactness for computational tractability. The resulting score preserves key monotonicity properties and is calibrated end-to-end via downstream task performance.

###### Proof.

From Lemma [C.2](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem2 "Lemma C.2 (First-Order Approximation). ‣ C.2 Merge Score Derivation ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), the marginal gain is Δ​𝒥​(a,b)=λLM​f​(a,b)⋅PMI​(a,b)+λqual​f​(a,b)​g​(q¯a​b)+O​(1/|V|)\Delta\mathcal{J}(a,b)=\lambda\_{\text{LM}}f(a,b)\cdot\text{PMI}(a,b)+\lambda\_{\text{qual}}f(a,b)g(\bar{q}\_{ab})+O(1/|V|), where the complexity term is absorbed into PMI (both favor frequent co-occurrences).

Per-occurrence normalization: Following the design principle of BPE (Sennrich et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib13 "Neural machine translation of rare words with subword units")), we normalize by frequency to capture per-occurrence information gain. Applying the exponential transform (monotonic, preserves rankings):
exp⁡(Δ​𝒥/f​(a,b))∝f​(a,b)f​(a)​f​(b)+ϵf⋅exp⁡(λqualλLM​g​(q¯a​b))\exp(\Delta\mathcal{J}/f(a,b))\propto\frac{f(a,b)}{f(a)f(b)+\epsilon\_{f}}\cdot\exp(\frac{\lambda\_{\text{qual}}}{\lambda\_{\text{LM}}}g(\bar{q}\_{ab}))

Power-law approximation: We replace exp⁡(λ⋅g​(q))\exp(\lambda\cdot g(q)) with (q¯a​b+ϵQ)α~(\bar{q}\_{ab}+\epsilon\_{Q})^{\tilde{\alpha}} where α~\tilde{\alpha} is learned end-to-end. This preserves monotonicity in q¯a​b\bar{q}\_{ab} and subsumes the unknown ratio λqual/λLM\lambda\_{\text{qual}}/\lambda\_{\text{LM}}. The final score is:
wa​b=f​(a,b)f​(a)​f​(b)+ϵf⋅(q¯a​b+ϵQ)α⋅ψ​(a,b)w\_{ab}=\frac{f(a,b)}{f(a)f(b)+\epsilon\_{f}}\cdot(\bar{q}\_{ab}+\epsilon\_{Q})^{\alpha}\cdot\psi(a,b)

Monotonicity guarantees: ∂wa​b/∂q¯a​b>0\partial w\_{ab}/\partial\bar{q}\_{ab}>0 and ∂wa​b/∂PMI>0\partial w\_{ab}/\partial\text{PMI}>0, ensuring quality-increasing and statistically-associated merges are preferred. End-to-end learning of α\alpha calibrates the heuristic.
∎

### C.4 Key Insights from the Derivation

1. 1.

   PMI Foundation: The frequency term f​(a,b)f​(a)​f​(b)+ϵf\frac{f(a,b)}{f(a)f(b)+\epsilon\_{f}} approximates Pointwise Mutual Information, capturing statistical association.
2. 2.

   Quality Modulation: The quality term (q¯a​b+ϵQ)α(\bar{q}\_{ab}+\epsilon\_{Q})^{\alpha} multiplicatively adjusts the PMI-based score, up-weighting high-quality merges.
3. 3.

   Learnable Sensitivity: The parameter α\alpha controls the relative importance of quality vs. frequency:

   * •

     α=0\alpha=0: Reduces to standard PMI-based tokenization
   * •

     α>0\alpha>0: Increasing weight on quality signals
   * •

     Learned via gradient descent to optimize downstream performance
4. 4.

   Domain Flexibility: The factor ψ​(a,b)\psi(a,b) allows incorporation of domain knowledge without modifying the core framework.

This derivation shows that the quality-aware merge score is a *principled heuristic* motivated by first-principles analysis of the bilevel objective, rather than an ad-hoc combination of frequency and quality terms.

### C.5 Theory Proofs

##### Proof of Theorem [3.2](https://arxiv.org/html/2602.06394v1#S3.Thmtheorem2 "Theorem 3.2 (Computational Complexity). ‣ 3.2 Formal Problem Definition and Objective ‣ 3 Mathematical Formulation of QA-Token ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") (Computational Complexity).

The bilevel optimization problem is NP-hard by polynomial-time reduction from Weighted Set Cover (Karp, [1972](https://arxiv.org/html/2602.06394v1#bib.bib2 "Reducibility among combinatorial problems")). The reduction maps sets to corpus sequences and set cover cost to vocabulary complexity: given a WSC instance (U,𝒮,{ci})(U,\mathcal{S},\{c\_{i}\}), construct alphabet Σ=U∪{$}\Sigma=U\cup\{\mathdollar\}, corpus sequences σi\sigma\_{i} for each set SiS\_{i}, and uniform quality scores. With λqual=0\lambda\_{\text{qual}}=0, optimal tokenizations correspond bijectively to optimal set covers.

For stronger complexity results establishing Σ2p\Sigma\_{2}^{p}-hardness of general bilevel programs, see (Bolte et al., [2024](https://arxiv.org/html/2602.06394v1#bib.bib121 "Geometric and computational hardness of bilevel programming"); Grne and Wulf, [2023](https://arxiv.org/html/2602.06394v1#bib.bib124 "Completeness in the polynomial hierarchy for many natural problems in bilevel and robust optimization"); Dempe, [2020](https://arxiv.org/html/2602.06394v1#bib.bib116 "Bilevel optimization: theory, algorithms and applications")). The worst-case exhaustive search complexity is O​(|Σ|K⋅K!⋅N⋅n⋅|Θ|)O(|\Sigma|^{K}\cdot K!\cdot N\cdot n\cdot|\Theta|), accounting for the space of merge sequences, merge orderings, and downstream model optimization.

□\square

###### Proposition C.4 (Boundedness and Lipschitzness of wa​bw\_{ab}).

Under assumptions (A1)-(A2), the quality-aware merge score wa​bw\_{ab} is bounded and Lipschitz continuous in (qa,qb)(q\_{a},q\_{b}).

###### Proof.

Boundedness: By (A1), f​(a,b)/(f​(a)​f​(b)+ϵf)≤Cf/ϵff(a,b)/(f(a)f(b)+\epsilon\_{f})\leq C\_{f}/\epsilon\_{f}. With q¯a​b∈[0,1]\bar{q}\_{ab}\in[0,1] and ψ∈[0,1]\psi\in[0,1], we have wa​b≤Cf(1+ϵQ)α/ϵf=:Cww\_{ab}\leq C\_{f}(1+\epsilon\_{Q})^{\alpha}/\epsilon\_{f}=:C\_{w}.

Lipschitz continuity: By chain rule on compositions of bounded functions on compact domains, wa​bw\_{ab} is LwL\_{w}-Lipschitz in (qa,qb)(q\_{a},q\_{b}) with Lw=Cf​Lg/ϵfL\_{w}=C\_{f}L\_{g}/\epsilon\_{f}. For α=1\alpha=1, Lg=1/2L\_{g}=1/\sqrt{2}; for 0<α<10<\alpha<1, Lg≤α​ϵQα−1/2L\_{g}\leq\alpha\epsilon\_{Q}^{\alpha-1}/\sqrt{2}. The regularization ϵQ\epsilon\_{Q} ensures numerical stability.
∎

###### Proposition C.5 (Stability of EMA Normalization).

Under assumptions (A1) and ϵR>0\epsilon\_{R}>0, the EMA-based normalization maintains σj,trun>0\sigma\_{j,t}^{\text{run}}>0 almost surely for non-degenerate reward streams.

###### Proof.

The result follows from standard EMA convergence theory (Robbins-Monro). Under (A1), raw rewards have non-degenerate distribution Var​(Xt)>0\text{Var}(X\_{t})>0. The EMA variance update preserves positivity: if Varj,t−1run>0\text{Var}\_{j,t-1}^{\text{run}}>0, then Varj,trun≥(1−βnorm)​Varj,t−1run>0\text{Var}\_{j,t}^{\text{run}}\geq(1-\beta\_{\text{norm}})\text{Var}\_{j,t-1}^{\text{run}}>0.

With ∑tβnorm,t=∞\sum\_{t}\beta\_{\text{norm},t}=\infty and ∑tβnorm,t2<∞\sum\_{t}\beta\_{\text{norm},t}^{2}<\infty, the running variance converges a.s. to Var​(X)>0\text{Var}(X)>0, ensuring σj,trun>0\sigma\_{j,t}^{\text{run}}>0.
∎

###### Proposition C.6 (Convergence of PPO Objective).

Under assumptions (A1)-(A4), PPO converges to a stationary point of J​(π;θadapt(0))J(\pi;\theta\_{\text{adapt}}^{(0)}).

###### Proof.

Under (A1)–(A4), the standard PPO conditions hold (Schulman et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib63 "Proximal policy optimization algorithms")): bounded rewards (|R​(s,a)|≤Rmax|R(s,a)|\leq R\_{\max}), compact state space, finite action space, and differentiable policy. The clipped surrogate objective ensures bounded gradients ‖∇θLCLIP‖2≤Gmax\|\nabla\_{\theta}L^{\text{CLIP}}\|\_{2}\leq G\_{\max}.

With learning rate ηt=η0/t\eta\_{t}=\eta\_{0}/\sqrt{t} satisfying ∑tηt=∞\sum\_{t}\eta\_{t}=\infty and ∑tηt2<∞\sum\_{t}\eta\_{t}^{2}<\infty, global convergence to stationary points at rate O​(1/T)O(1/\sqrt{T}) follows from (Bhandari and Russo, [2021](https://arxiv.org/html/2602.06394v1#bib.bib115 "Global optimality guarantees for policy gradient methods"); Cen and Chi, [2023](https://arxiv.org/html/2602.06394v1#bib.bib119 "Global convergence of policy gradient methods in reinforcement learning, games and control")).
∎

###### Proposition C.7 (Consistency and Boundedness of Stage 2 Gradients).

Under assumptions (A1)–(A3), the Gumbel-Softmax estimator yields consistent gradients with bounded variance.

###### Proof.

The Gumbel-Softmax gradient properties follow from (Jang et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib31 "Categorical reparameterization with gumbel-softmax"); Maddison et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib32 "The concrete distribution: a continuous relaxation of discrete random variables")). Under (A1)–(A3), the composite logits ℓa​b\ell\_{ab} are bounded by Lmax=Cw+∑j|λj|​RmaxL\_{\max}=C\_{w}+\sum\_{j}|\lambda\_{j}|R\_{\max}. The Gumbel-Softmax Jacobian satisfies ‖∂yi/∂ℓj‖≤1/τ\|\partial y\_{i}/\partial\ell\_{j}\|\leq 1/\tau, yielding bounded gradients ‖∇θadaptLtask‖≤Lmax/τ⋅‖∇yLtask‖\|\nabla\_{\theta\_{\text{adapt}}}L\_{\text{task}}\|\leq L\_{\max}/\tau\cdot\|\nabla\_{y}L\_{\text{task}}\|.

As τ→0\tau\to 0, the estimator converges to REINFORCE (Williams, [1992](https://arxiv.org/html/2602.06394v1#bib.bib65 "Simple statistical gradient-following algorithms for connectionist reinforcement learning")). The bias-variance tradeoff is: Bias​(τ)=O​(τ2)\text{Bias}(\tau)=O(\tau^{2}), Var​(τ)=O​(1/τ2)\text{Var}(\tau)=O(1/\tau^{2}). The optimal temperature τopt∝T−1/4\tau\_{\text{opt}}\propto T^{-1/4} for TT samples balances these terms.
∎

###### Theorem C.8 (Gumbel-Softmax Properties).

Let π=(π1,…,πk)\pi=(\pi\_{1},\ldots,\pi\_{k}) be a categorical distribution with kk categories. The Gumbel-Softmax distribution with temperature τ>0\tau>0 satisfies:

1. 1.

   Consistency: As τ→0\tau\rightarrow 0, the samples converge to one-hot vectors from Categorical​(π)\text{Categorical}(\pi)
2. 2.

   Differentiability: The reparameterization provides continuous gradients with respect to π\pi
3. 3.

   Bias-Variance Tradeoff: Bias O​(τ2)O(\tau^{2}), Variance O​(1/τ2)O(1/\tau^{2})

###### Proof.

All three properties are established in (Jang et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib31 "Categorical reparameterization with gumbel-softmax"); Maddison et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib32 "The concrete distribution: a continuous relaxation of discrete random variables")). We summarize the key arguments.

Property 1 (Consistency): By the Gumbel-Max trick, arg⁡maxi⁡(ℓi+gi)∼Categorical​(softmax​(ℓ))\arg\max\_{i}(\ell\_{i}+g\_{i})\sim\text{Categorical}(\text{softmax}(\bm{\ell})) for gi∼Gumbel​(0,1)g\_{i}\sim\text{Gumbel}(0,1). As τ→0\tau\to 0, the Gumbel-Softmax samples yi=exp⁡((ℓi+gi)/τ)/∑jexp⁡((ℓj+gj)/τ)y\_{i}=\exp((\ell\_{i}+g\_{i})/\tau)/\sum\_{j}\exp((\ell\_{j}+g\_{j})/\tau) concentrate on one-hot vectors almost surely by the continuous mapping theorem.

Property 2 (Differentiability): For τ>0\tau>0, yiy\_{i} is C∞C^{\infty} in ℓj\ell\_{j}, enabling reparameterized gradients. The expectation 𝔼g​[yi]=softmax​(ℓ/τ)i\mathbb{E}\_{g}[y\_{i}]=\text{softmax}(\bm{\ell}/\tau)\_{i} introduces bias that vanishes as τ→0\tau\to 0. The annealing schedule τt→0\tau\_{t}\to 0 ensures asymptotic consistency.

Property 3 (Gradient Bounds): The Jacobian satisfies ∂yi/∂ℓj=(1/τ)​yi​(δi​j−yj)\partial y\_{i}/\partial\ell\_{j}=(1/\tau)y\_{i}(\delta\_{ij}-y\_{j}), yielding ‖∇ℓ𝐲‖F≤1/τ\|\nabla\_{\bm{\ell}}\mathbf{y}\|\_{F}\leq 1/\tau.
∎

### C.6 Assumptions

We formalize the assumptions used throughout the theoretical analysis:

Assumption A1 (Bounded Frequencies): There exists Cf>0C\_{f}>0 such that for all tokens a,ba,b:

|  |  |  |
| --- | --- | --- |
|  | 0≤f​(a),f​(b),f​(a,b)≤Cf0\leq f(a),f(b),f(a,b)\leq C\_{f} |  |

Assumption A2 (Bounded Qualities): All quality scores satisfy q∈[0,1]q\in[0,1], and the quality aggregation function is LQL\_{Q}-Lipschitz continuous.

Assumption A3 (Bounded Rewards): Raw reward components are bounded: |Rjraw|≤Rmax|R^{\text{raw}}\_{j}|\leq R\_{\max} for all jj.

Assumption A4 (Regular Learning Rates): The learning rate schedules satisfy:
- PPO: ∑tηt=∞\sum\_{t}\eta\_{t}=\infty and ∑tηt2<∞\sum\_{t}\eta\_{t}^{2}<\infty
- Adaptive learning: ηt=O​(1/t)\eta\_{t}=O(1/\sqrt{t})

### C.7 Theory Extensions

###### Definition C.9 (Assumptions for Approximation Guarantee).

The (1−1/e)(1-1/e) approximation guarantee requires the following structural assumptions:

1. (A1)

   Adaptive Monotonicity: For any partial realization ψ\psi and merge (a,b)(a,b): ΔF​((a,b)|ψ)≥0\Delta\_{F}((a,b)|\psi)\geq 0, where ΔF\Delta\_{F} denotes the marginal gain.
2. (A2)

   Adaptive Submodularity: For realizations ψ⪯ψ′\psi\preceq\psi^{\prime} (where ⪯\preceq denotes extension): ΔF​((a,b)|ψ)≥ΔF​((a,b)|ψ′)\Delta\_{F}((a,b)|\psi)\geq\Delta\_{F}((a,b)|\psi^{\prime}) (diminishing returns).
3. (A3)

   Constraint independence: ψ​(a,b)\psi(a,b) is history-independent.
4. (A4)

   Candidate pool regularity: ℙ​[(a,b)∈P​Qt]≥δ>0\mathbb{P}[(a,b)\in PQ\_{t}]\geq\delta>0 for all valid pairs.
5. (A5)

   Quality stability: |qt−𝔼[qt|ℋt]|≤ϵq|q\_{t}-\mathbb{E}[q\_{t}|\mathcal{H}\_{t}]|\leq\epsilon\_{q} with high probability.

###### Lemma C.10 (Approximate Adaptive Submodularity).

Under assumptions (A3)-(A5), the quality-aware objective F​(V)=∑kℒLM​(V;Dk)+λQ​Q​(V)F(V)=\sum\_{k}\mathcal{L}\_{\text{LM}}(V;D\_{k})+\lambda\_{Q}Q(V) satisfies ϵ\epsilon-approximate adaptive submodularity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔF​((a,b)|ψ)≥ΔF​((a,b)|ψ′)−ϵsub\Delta\_{F}((a,b)|\psi)\geq\Delta\_{F}((a,b)|\psi^{\prime})-\epsilon\_{\text{sub}} |  | (6) |

for ψ⪯ψ′\psi\preceq\psi^{\prime}, where ϵsub=O​(ϵq+1/δ)\epsilon\_{\text{sub}}=O(\epsilon\_{q}+1/\delta).

###### Proof sketch.

The frequency-based component PMI​(a,b)\text{PMI}(a,b) exhibits exact diminishing returns: as more merges are performed, pair frequencies decrease, reducing potential PMI gains. The quality component (q¯a​b)α(\bar{q}\_{ab})^{\alpha} is history-independent under (A3) and stable under (A5). The approximation error ϵsub\epsilon\_{\text{sub}} arises from: (i) quality estimation noise (ϵq\epsilon\_{q}), and (ii) candidate pool variability (1/δ1/\delta). Full proof follows the framework of Golovin and Krause ([2011](https://arxiv.org/html/2602.06394v1#bib.bib90 "Adaptive submodularity: theory and applications in active learning and stochastic optimization")).
∎

###### Theorem C.11 (Approximation Guarantee with Explicit Constants).

Under Definition [C.9](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem9 "Definition C.9 (Assumptions for Approximation Guarantee). ‣ C.7 Theory Extensions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), if assumptions (A1)-(A2) hold exactly, the greedy policy that maximizes wa​bw\_{ab} achieves:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(πgreedy)≥(1−1e)​F​(π∗)−K​ϵq−Kδ,F(\pi\_{\text{greedy}})\geq\left(1-\frac{1}{e}\right)F(\pi^{\*})-K\epsilon\_{q}-\frac{K}{\delta}, |  | (7) |

where π∗\pi^{\*} is the optimal adaptive policy over budget KK. The error terms arise from ϵ\epsilon-approximate submodularity (Lemma [C.10](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem10 "Lemma C.10 (Approximate Adaptive Submodularity). ‣ C.7 Theory Extensions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

###### Proof.

By Theorem 5 of Golovin and Krause ([2011](https://arxiv.org/html/2602.06394v1#bib.bib90 "Adaptive submodularity: theory and applications in active learning and stochastic optimization")), greedy optimization of adaptive submodular functions achieves (1−1/e)(1-1/e) approximation. We extend this to ϵ\epsilon-approximate submodularity (Lemma [C.10](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem10 "Lemma C.10 (Approximate Adaptive Submodularity). ‣ C.7 Theory Extensions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

With ϵ\epsilon-approximate submodularity, the greedy per-step guarantee becomes ΔF​((at,bt)|ψt)≥1K​[F​(π∗)−F​(ψt)]−ϵsub\Delta\_{F}((a\_{t},b\_{t})|\psi\_{t})\geq\frac{1}{K}[F(\pi^{\*})-F(\psi\_{t})]-\epsilon\_{\text{sub}}. Defining Δt=F​(π∗)−Ft\Delta\_{t}=F(\pi^{\*})-F\_{t} and iterating over KK steps: ΔK≤(1−1/K)K​Δ0+K​ϵsub≤1e​F​(π∗)+K​ϵsub\Delta\_{K}\leq(1-1/K)^{K}\Delta\_{0}+K\epsilon\_{\text{sub}}\leq\frac{1}{e}F(\pi^{\*})+K\epsilon\_{\text{sub}}, using (1−1/K)K≤1/e(1-1/K)^{K}\leq 1/e.

Substituting ϵsub=ϵq+1/δ\epsilon\_{\text{sub}}=\epsilon\_{q}+1/\delta yields F​(πgreedy)≥(1−1/e)​F​(π∗)−K​ϵq−K/δF(\pi\_{\text{greedy}})\geq(1-1/e)F(\pi^{\*})-K\epsilon\_{q}-K/\delta.
∎

*Remark (Assumptions and Robustness):* Assumptions (A1)–(A2) (adaptive monotonicity and submodularity) are sufficient conditions for the (1−1/e)(1-1/e) guarantee but may not hold exactly in practice. Specifically:

* •

  The LM loss ℒLM\mathcal{L}\_{\text{LM}} is not generally submodular in merge operations; the guarantee applies to the quality-frequency component F​(V)F(V) as defined.
* •

  When assumptions are violated, the bound becomes approximate: F​(πgreedy)≥(1−1/e)​F​(π∗)−K​ϵq−K/δ−ϵviolationF(\pi\_{\text{greedy}})\geq(1-1/e)F(\pi^{\*})-K\epsilon\_{q}-K/\delta-\epsilon\_{\text{violation}}, where ϵviolation\epsilon\_{\text{violation}} is proportional to the degree of assumption violation.

Empirically, our experiments show the guarantee is meaningful because: (1) tokenization objectives often exhibit near-submodular behavior (Lin and Bilmes, [2011](https://arxiv.org/html/2602.06394v1#bib.bib108 "A class of submodular functions for document summarization")); (2) end-to-end learning of α\alpha compensates for violations by calibrating the quality-frequency trade-off; (3) RL policy exploration in Stage 1 helps escape poor local optima that pure greedy would converge to.

### C.8 Robustness Analysis

We analyze robustness under misspecified quality metrics and adversarial quality scores, quantifying interaction effects between RL and adaptive learning stages.

###### Theorem C.12 (Robustness to Quality Corruption).

Let q~=q+ξ\tilde{q}=q+\xi with ξ∼𝒩​(0,σξ2)\xi\sim\mathcal{N}(0,\sigma\_{\xi}^{2}). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(q~)−ℒ​(q)≤α​σξ​𝔼​[‖∇qℒ‖2].\mathcal{L}(\tilde{q})-\mathcal{L}(q)\leq\alpha\,\sigma\_{\xi}\,\sqrt{\mathbb{E}[\|\nabla\_{q}\mathcal{L}\|^{2}]}. |  | (8) |

###### Proof.

The result follows from Lipschitz stability of the bilevel objective. By the chain rule and Cauchy-Schwarz, |ℒ​(q~)−ℒ​(q)|≤‖ξ‖2⋅∫01‖∇qℒ​(q+t​ξ)‖2​𝑑t|\mathcal{L}(\tilde{q})-\mathcal{L}(q)|\leq\|\xi\|\_{2}\cdot\int\_{0}^{1}\|\nabla\_{q}\mathcal{L}(q+t\xi)\|\_{2}dt.

From Proposition [C.4](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem4 "Proposition C.4 (Boundedness and Lipschitzness of 𝑤_{𝑎⁢𝑏}). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), ‖∂wa​b/∂q‖≤α​ϵQα−1\|\partial w\_{ab}/\partial q\|\leq\alpha\epsilon\_{Q}^{\alpha-1}, yielding ‖∇qℒ‖≤α​Cℒ\|\nabla\_{q}\mathcal{L}\|\leq\alpha C\_{\mathcal{L}}. Taking expectations over ξ∼𝒩​(0,σξ2​I)\xi\sim\mathcal{N}(0,\sigma\_{\xi}^{2}I) with 𝔼​[‖ξ‖2]≤σξ​d\mathbb{E}[\|\xi\|\_{2}]\leq\sigma\_{\xi}\sqrt{d} gives the stated bound.
∎

Empirical Validation. We validate the robustness bound experimentally:

* •

  20% quality noise: Performance degradation of −4.2-4.2% (genomics) and −5.8-5.8% (finance), consistent with the O​(α​σξ)O(\alpha\sigma\_{\xi}) bound.
* •

  Adversarial quality (inverted scores): Performance matches standard BPE, as expected when quality signals become uninformative.
* •

  50% missing quality: Graceful fallback to frequency-only merging via the adaptive α→0\alpha\to 0 mechanism.

Interaction Effects. We quantify the contribution of each learning stage:

* •

  RL policy optimization alone: 65% of total improvement over BPE
* •

  Adaptive parameter learning alone: 45% of total improvement
* •

  Combined (synergy): Additional +10% from joint optimization

The super-additive effect (65% + 45% >> 100% total) indicates that the two stages reinforce each other: RL discovers promising merge patterns that adaptive learning then calibrates, while learned parameters improve the reward landscape for RL exploration.

### C.9 Information-Theoretic Optimality

This subsection establishes that QA-Token achieves information-theoretic optimality under noisy conditions, providing theoretical justification for quality-aware tokenization.

###### Proposition C.13 (Quality-Aware Information Bottleneck Interpretation).

Let XX denote the input sequence, TT the tokenized representation, and YY the downstream task labels. Under the quality-aware tokenization framework with quality scores QQ, the optimal vocabulary V∗V^{\*} minimizes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒQA​(V)=−I​(T;Y|Q)+β⋅I​(T;X|Q)\mathcal{L}\_{\text{QA}}(V)=-I(T;Y|Q)+\beta\cdot I(T;X|Q) |  | (9) |

where I(⋅;⋅|⋅)I(\cdot;\cdot|\cdot) denotes conditional mutual information and β\beta controls the compression-relevance tradeoff.

*Connection to merge score:* The merge score wa​bw\_{ab} is consistent with (but not directly derived from) this IB objective. PMI approximates compression efficiency I​(T;X|Q)I(T;X|Q), while quality weighting ensures high I​(T;Y|Q)I(T;Y|Q) in reliable regions. The connection is qualitative rather than via direct differentiation of mutual information, which is intractable.

###### Proof.

Following the information bottleneck framework (Tishby et al., [1999](https://arxiv.org/html/2602.06394v1#bib.bib113 "The information bottleneck method")) and its variational extension (Alemi et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib114 "Deep variational information bottleneck")), conditioning on quality QQ yields the objective ℒQA=−I​(T;Y|Q)+β​I​(T;X|Q)\mathcal{L}\_{\text{QA}}=-I(T;Y|Q)+\beta I(T;X|Q).

The merge score wa​b∝PMI​(a,b)⋅(q¯a​b)αw\_{ab}\propto\text{PMI}(a,b)\cdot(\bar{q}\_{ab})^{\alpha} is *consistent with* this IB objective: (i) the PMI term approximates compression efficiency I​(T;X|Q)I(T;X|Q) (high-PMI merges compress efficiently), and (ii) the quality term weights merges by reliability, prioritizing high-quality regions for I​(T;Y|Q)I(T;Y|Q).

*Caveat:* The exact form of wa​bw\_{ab} does not follow from direct differentiation of mutual information (intractable). Rather, it is a principled heuristic with end-to-end learning of α\alpha calibrating the quality-compression trade-off.
∎

###### Corollary C.14 (Noise Reduction Bound).

For a corpus with noise level ϵ\epsilon and quality scores qq satisfying 𝔼​[q|noise]<𝔼​[q|signal]\mathbb{E}[q|\text{noise}]<\mathbb{E}[q|\text{signal}], the quality-aware tokenizer achieves:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒQA≤ℒuniform−α⋅Var​(q)⋅ρ​(q,ϵ)2\mathcal{L}\_{\text{QA}}\leq\mathcal{L}\_{\text{uniform}}-\alpha\cdot\text{Var}(q)\cdot\rho(q,\epsilon)^{2} |  | (10) |

where ρ​(q,ϵ)\rho(q,\epsilon) is the correlation between quality scores and noise levels.

Key Theoretical Insights. This information-theoretic analysis provides three fundamental insights:

1. 1.

   Automatic Noise Filtering: QA-Token implicitly performs importance sampling, up-weighting high-quality regions during vocabulary construction.
2. 2.

   Optimal Compression: The quality-aware merge process achieves better rate-distortion tradeoffs by allocating more representation capacity to high-quality, informative regions.
3. 3.

   Transfer Learning: Foundation models trained with QA-Token vocabularies learn more robust representations that transfer better to downstream tasks.

## Appendix D Complete Quality Metrics Formulations

### D.1 Genomics: Detailed Sequencing Quality Metrics

In genomic sequencing, each nucleotide base call si∈{A,C,G,T,N}s\_{i}\in\{\text{A},\text{C},\text{G},\text{T},\text{N}\} is associated with a Phred quality score Qphred,i∈[0,93]Q\_{\text{phred},i}\in[0,93]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Perror​(i)=10−Qphred,i/10P\_{\text{error}}(i)=10^{-Q\_{\text{phred},i}/10} |  | (11) |

The base quality score is qi=1−Perror​(i)∈[0,1]q\_{i}=1-P\_{\text{error}}(i)\in[0,1]. Position-adjusted quality accounts for systematic degradation at read ends:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi′=qi⋅exp⁡(−βpos⋅|i−(L−1)/2|(L−1)/2+ϵlen)q^{\prime}\_{i}=q\_{i}\cdot\exp\left(-\beta\_{\text{pos}}\cdot\frac{|i-(L-1)/2|}{(L-1)/2+\epsilon\_{\text{len}}}\right) |  | (12) |

where LL is read length, βpos≥0\beta\_{\text{pos}}\geq 0 is learnable, and ϵlen=10−6\epsilon\_{\text{len}}=10^{-6}.

For multi-base token t=s1​…​s|t|t=s\_{1}...s\_{|t|}, we use geometric mean aggregation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qtgenomic=(∏j=1|t|qsj′)1/|t|=exp⁡(1|t|​∑j=1|t|log⁡(qsj′+ϵQ))q\_{t}^{\text{genomic}}=\left(\prod\_{j=1}^{|t|}q^{\prime}\_{s\_{j}}\right)^{1/|t|}=\exp\left(\frac{1}{|t|}\sum\_{j=1}^{|t|}\log(q^{\prime}\_{s\_{j}}+\epsilon\_{Q})\right) |  | (13) |

### D.2 Finance: Comprehensive Market Quality Metrics

Financial time series quality combines four dimensions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qifinance=∑k=14wk⋅qk,i,∑k=14wk=1q\_{i}^{\text{finance}}=\sum\_{k=1}^{4}w\_{k}\cdot q\_{k,i},\quad\sum\_{k=1}^{4}w\_{k}=1 |  | (14) |

1. Liquidity Quality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qliq​(t)=sigmoid​(log⁡(volumet/median\_volume)σvolume)q\_{\text{liq}}(t)=\text{sigmoid}\left(\frac{\log(\text{volume}\_{t}/\text{median\\_volume})}{\sigma\_{\text{volume}}}\right) |  | (15) |

where σvolume\sigma\_{\text{volume}} is the rolling standard deviation of log-volume computed over a lookback window of Lvol=252L\_{\text{vol}}=252 trading days (one year), clipped to [0.1,10][0.1,10] for numerical stability. This normalization ensures that qliqq\_{\text{liq}} responds proportionally to volume deviations relative to typical market activity.

2. Signal Quality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qsig​(t)=max⁡(0,1−|bid-ask spreadt|mid-pricet⋅αspread)q\_{\text{sig}}(t)=\max\left(0,1-\frac{|\text{bid-ask spread}\_{t}|}{\text{mid-price}\_{t}\cdot\alpha\_{\text{spread}}}\right) |  | (16) |

3. Stability Quality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qstb​(t)=exp⁡(−βvol⋅realized\_voltexpected\_volt)q\_{\text{stb}}(t)=\exp\left(-\beta\_{\text{vol}}\cdot\frac{\text{realized\\_vol}\_{t}}{\text{expected\\_vol}\_{t}}\right) |  | (17) |

where expected\_volt\text{expected\\_vol}\_{t} is the exponentially weighted moving average (EWMA) of realized volatility following the RiskMetrics methodology (J.P. Morgan, [1996](https://arxiv.org/html/2602.06394v1#bib.bib4 "RiskMetrics technical document")): expected\_volt=γvol⋅expected\_volt−1+(1−γvol)⋅realized\_volt−1\text{expected\\_vol}\_{t}=\gamma\_{\text{vol}}\cdot\text{expected\\_vol}\_{t-1}+(1-\gamma\_{\text{vol}})\cdot\text{realized\\_vol}\_{t-1}, with decay factor γvol=0.94\gamma\_{\text{vol}}=0.94. The learnable parameter βvol≥0\beta\_{\text{vol}}\geq 0 controls sensitivity to volatility spikes.

4. Information Quality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qinfo​(t)=MI​(tokent,future\_returnt+h)H​(future\_returnt+h)q\_{\text{info}}(t)=\frac{\text{MI}(\text{token}\_{t},\text{future\\_return}\_{t+h})}{\text{H}(\text{future\\_return}\_{t+h})} |  | (18) |

Token aggregation uses arithmetic mean:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qtfinance=1|t|​∑i∈tqifinanceq\_{t}^{\text{finance}}=\frac{1}{|t|}\sum\_{i\in t}q\_{i}^{\text{finance}} |  | (19) |

Rationale for Arithmetic Mean Aggregation: Unlike genomics (which uses geometric mean, Eq. [13](https://arxiv.org/html/2602.06394v1#A4.E13 "Equation 13 ‣ D.1 Genomics: Detailed Sequencing Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), financial data aggregation employs the arithmetic mean for two principled reasons: (1) *Additive noise model*: Financial market microstructure noise is predominantly additive across time points—a single noisy tick does not invalidate adjacent observations in the way a single low-quality DNA base compromises an entire read. Empirically, LOB noise sources (latency, partial fills, stale quotes) contribute independently rather than multiplicatively. (2) *Temporal continuity for forecasting*: Financial tokens represent contiguous time windows where downstream tasks (price prediction, volatility forecasting) operate on windowed features. The aggregate quality naturally represents the *average* reliability of observations within the window, which aligns with how prediction models weight inputs. In contrast, genomic tokens represent molecular sequences where any unreliable base compromises biological interpretation (e.g., variant calling), necessitating the conservative geometric mean that penalizes even single low-quality elements.

### D.3 Social Media: Linguistic Quality Metrics

Social media text presents unique quality challenges including orthographic variations, semantic drift, platform-specific conventions, and temporal dynamics. We define a multi-dimensional quality vector for character-level tokens:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐪tsocial=(qorth​(t),qsem​(t),qtemp​(t),qplat​(t))\mathbf{q}\_{t}^{\text{social}}=(q\_{\text{orth}}(t),q\_{\text{sem}}(t),q\_{\text{temp}}(t),q\_{\text{plat}}(t)) |  | (20) |

The scalar quality is obtained via learnable weighted aggregation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qtsocial=∑jwj⋅qj​(t),wj∈θadaptq\_{t}^{\text{social}}=\sum\_{j}w\_{j}\cdot q\_{j}(t),\quad w\_{j}\in\theta\_{\text{adapt}} |  | (21) |

1. Orthographic Quality: Measures deviation from canonical spelling:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qorth​(t)=exp⁡(−λedit⋅dedit​(t,tcanonical))q\_{\text{orth}}(t)=\exp(-\lambda\_{\text{edit}}\cdot d\_{\text{edit}}(t,t\_{\text{canonical}})) |  | (22) |

where deditd\_{\text{edit}} is the normalized Levenshtein distance to the nearest canonical form in a reference dictionary. The reference dictionary is constructed by combining: (i) the Hunspell en\_US dictionary (2023 release, ≈\approx140k entries), (ii) a curated social media slang lexicon (≈\approx50k terms aggregated from NoSlang.com and similar sources), and (iii) domain-specific terminology lists for each benchmark task.

2. Semantic Quality: Captures contextual coherence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qsem​(t)=max⁡(0,cos⁡(v→t,v→context))q\_{\text{sem}}(t)=\max(0,\cos(\vec{v}\_{t},\vec{v}\_{\text{context}})) |  | (23) |

where v→context\vec{v}\_{\text{context}} is the average embedding of surrounding tokens. For efficiency, we use fastText Common Crawl embeddings (cc.en.300.bin, 2M vocabulary) (Bojanowski et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib62 "Enriching word vectors with subword information")). For BERT-based variants requiring subword handling, we use bert-base-uncased from HuggingFace with mean pooling over subword tokens.

3. Temporal Quality: Models relevance decay over time:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qtemp​(t)=exp⁡(−γdecay⋅Δ​t)q\_{\text{temp}}(t)=\exp(-\gamma\_{\text{decay}}\cdot\Delta t) |  | (24) |

with time difference Δ​t\Delta t in days from posting time, capturing trending topics and temporal relevance.

4. Platform Quality: Platform-specific noise modeling:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qplat​(t)=P​(t|platform)q\_{\text{plat}}(t)=P(t|\text{platform}) |  | (25) |

computed using 3-gram Kneser-Ney language models trained with KenLM (Heafield, [2011](https://arxiv.org/html/2602.06394v1#bib.bib3 "KenLM: faster and smaller language model queries")) on curated platform-specific corpora (≈\approx10M tokens each): Twitter (tweets with >>100 likes and <<5% special characters), Reddit (comments with >>10 upvotes from default subreddits), and Facebook (public posts from verified pages). These “clean” subsets establish platform-specific baselines for typical language patterns.

Learned Parameters: For the TweetEval benchmark experiments, the learned parameters were:
worth=0.32±0.03w\_{\text{orth}}=0.32\pm 0.03, wsem=0.35±0.04w\_{\text{sem}}=0.35\pm 0.04, wtemp=0.18±0.02w\_{\text{temp}}=0.18\pm 0.02, wplat=0.15±0.02w\_{\text{plat}}=0.15\pm 0.02, λedit=0.5\lambda\_{\text{edit}}=0.5, and γdecay=0.01\gamma\_{\text{decay}}=0.01.

## Appendix E Sequential Learning Process: Complete Framework

This section provides detailed algorithms and convergence analysis for QA-Token’s two-stage sequential learning process.

### E.1 Stage 1: Reinforcement Learning Policy Optimization

#### E.1.1 MDP Formulation

The vocabulary construction process is formulated as a finite-horizon Markov Decision Process (see Section [E.7](https://arxiv.org/html/2602.06394v1#A5.SS7 "E.7 MDP Formulation and Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") for complete specification):

* •

  States st∈𝒮s\_{t}\in\mathcal{S}: Encode current vocabulary VtV\_{t}, merge candidates, corpus statistics, and progress t/Tt/T
* •

  Actions at∈𝒜ta\_{t}\in\mathcal{A}\_{t}: Select a merge pair (ai,bi)(a\_{i},b\_{i}) from the priority queue
* •

  Transitions: Deterministic vocabulary updates following merge operations
* •

  Rewards: Multi-objective reward combining quality, information, and complexity

#### E.1.2 Reward Function Design

The reward function guides the RL agent:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(a,b;θadapt(0))=∑j∈{Q,I,C,domain}λj​R^j​(a,b)R(a,b;\theta\_{\text{adapt}}^{(0)})=\sum\_{j\in\{Q,I,C,\text{domain}\}}\lambda\_{j}\hat{R}\_{j}(a,b) |  | (26) |

where components are normalized via exponential moving averages (see Section [E.8](https://arxiv.org/html/2602.06394v1#A5.SS8 "E.8 Reward Normalization Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). The detailed components are:

* •

  Quality Reward (R^Q\hat{R}\_{Q} from RQrawR^{\text{raw}}\_{Q}): Encourages high intrinsic quality for tmerged=a​bt\_{\text{merged}}=ab, computed using domain-specific aggregation (Section [D](https://arxiv.org/html/2602.06394v1#A4 "Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
* •

  Information Reward (R^I\hat{R}\_{I} from RIrawR^{\text{raw}}\_{I}): Rewards statistically significant merges, e.g., RIraw​(a,b)=log⁡P​(tmerged)P​(a)​P​(b)+ϵpR^{\text{raw}}\_{I}(a,b)=\log\frac{P(t\_{\text{merged}})}{P(a)P(b)+\epsilon\_{p}}.
* •

  Complexity Penalty (R^C\hat{R}\_{C} from RCrawR^{\text{raw}}\_{C}): Typically negative, e.g., RCraw​(a,b)=−(|tmerged|⋅log⁡(|Vt|+1))R^{\text{raw}}\_{C}(a,b)=-(|t\_{\text{merged}}|\cdot\log(|V\_{t}|+1)). R^C\hat{R}\_{C} is then scaled to e.g. [−1,0][-1,0].
* •

  Domain-Specific Rewards (R^domain,k\hat{R}\_{\text{domain},k} from Rdomain,krawR^{\text{raw}}\_{\text{domain},k}): Include conservation scores (genomics) and predictive power (finance).

The EMA-normalized rewards R^j​(a,b)\hat{R}\_{j}(a,b) are used by the RL agent in Stage 1. For the Gumbel-Softmax logits in Stage 2 (Section [E.9](https://arxiv.org/html/2602.06394v1#A5.SS9 "E.9 Gumbel-Softmax Gradient Derivation and Temperature Annealing ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), raw or batch-normalized reward components are used to ensure direct differentiability with respect to θadapt\theta\_{\text{adapt}}.

#### E.1.3 PPO Training Algorithm

Algorithm 1  Stage 1: RL Policy Training

1: Input: Corpus 𝒮\mathcal{S}, initial θadapt(0)\theta\_{\text{adapt}}^{(0)}, episodes EE

2: Initialize policy network πθπ\pi\_{\theta\_{\pi}} and value network VϕV\_{\phi}

3: for episode e=1e=1 to EE do

4:  Initialize vocabulary V0=ΣV\_{0}=\Sigma

5:  for step t=1t=1 to TT do

6:   Compute state features sts\_{t} from current vocabulary

7:   Sample action at∼πθπ​(a|st)a\_{t}\sim\pi\_{\theta\_{\pi}}(a|s\_{t})

8:   Execute merge (aat,bat)↦a​b(a\_{a\_{t}},b\_{a\_{t}})\mapsto ab

9:   Compute reward rt=R​(aat,bat;θadapt(0))r\_{t}=R(a\_{a\_{t}},b\_{a\_{t}};\theta\_{\text{adapt}}^{(0)})

10:   Store trajectory (st,at,rt)(s\_{t},a\_{t},r\_{t})

11:  end for

12:  Update policy using PPO objective:

13:  LPPO=𝔼t​[min⁡(rt​(θ)​A^t,clip​(rt​(θ),1−ϵ,1+ϵ)​A^t)]\quad L^{\text{PPO}}=\mathbb{E}\_{t}[\min(r\_{t}(\theta)\hat{A}\_{t},\text{clip}(r\_{t}(\theta),1-\epsilon,1+\epsilon)\hat{A}\_{t})]

14:  Update value network to minimize MSE

15: end for

16: Output: Optimized policy πθπ∗\pi\_{\theta\_{\pi}}^{\*}

### E.2 Stage 2: Adaptive Parameter Learning

#### E.2.1 Adaptive Parameters Definition

The learnable parameter vector θadapt∈ℝm\theta\_{\text{adapt}}\in\mathbb{R}^{m} includes:

* •

  Quality sensitivity: α∈[0,2]\alpha\in[0,2] controlling quality influence
* •

  Domain factors: βpos\beta\_{\text{pos}} (genomics position decay), βvol\beta\_{\text{vol}} (finance volatility)
* •

  Quality weights: 𝐰=(w1,…,wk)\mathbf{w}=(w\_{1},\ldots,w\_{k}) for composite quality metrics
* •

  Reward weights: 𝝀=(λQ,λI,λC,…)\bm{\lambda}=(\lambda\_{Q},\lambda\_{I},\lambda\_{C},\ldots) for multi-objective rewards

#### E.2.2 Gumbel-Softmax Differentiable Optimization

To enable gradient-based optimization through discrete merge decisions, we employ Gumbel-Softmax relaxation:

Algorithm 2  Stage 2: Adaptive Parameter Learning

1: Input: Downstream dataset 𝒟\mathcal{D}, policy πθπ∗\pi\_{\theta\_{\pi}}^{\*}, initial θadapt\theta\_{\text{adapt}}

2: Initialize temperature τ=τinit\tau=\tau\_{\text{init}}

3: for iteration i=1i=1 to NN do

4:  Sample batch BB from 𝒟\mathcal{D}

5:  for each sequence in batch do

6:   Generate top-KK merge candidates via priority queue ranked by wa​bw\_{ab}

7:   Compute composite logits: ℓa​b=wa​b​(a,b;α)+∑jλj​Rjraw\ell\_{ab}=w\_{ab}(a,b;\alpha)+\sum\_{j}\lambda\_{j}R\_{j}^{\text{raw}}

8:   Select merge via Gumbel-Softmax (differentiable relaxation):

9:   yi=exp⁡((ℓi+gi)/τ)∑jexp⁡((ℓj+gj)/τ)\quad y\_{i}=\frac{\exp((\ell\_{i}+g\_{i})/\tau)}{\sum\_{j}\exp((\ell\_{j}+g\_{j})/\tau)}

10:   Construct differentiable tokenized representation

11:  end for

12:  Compute task loss LtaskL\_{\text{task}} on tokenized batch

13:  Update parameters: θadapt←θadapt−η​∇Ltotal\theta\_{\text{adapt}}\leftarrow\theta\_{\text{adapt}}-\eta\nabla L\_{\text{total}}

14:  Anneal temperature: τ←τ⋅exp⁡(−βanneal)\tau\leftarrow\tau\cdot\exp(-\beta\_{\text{anneal}})

15: end for

16: Output: Optimized parameters θadapt∗\theta\_{\text{adapt}}^{\*}

### E.3 Final Vocabulary Construction

After completing both stages, the final vocabulary for deployment is constructed.

Detailed Process:
Following the completion of Stage 1 (RL policy optimization yielding πθπ∗\pi\_{\theta\_{\pi}}^{\*}) and Stage 2 (adaptive parameter learning yielding θadapt∗\theta\_{\text{adapt}}^{\*}), the final vocabulary for deployment is typically constructed. While several strategies are possible, our primary approach involves the optimized adaptive parameters θadapt∗\theta\_{\text{adapt}}^{\*} to re-evaluate merge priorities. Specifically, a greedy BPE-like process is executed, starting from the base alphabet. At each step, the merge operation (a,b)(a,b) is chosen that maximizes the quality-aware merge score wa​b​(a,b;θadapt∗)w\_{ab}(a,b;\theta\_{\text{adapt}}^{\*}) as defined in Equation [5](https://arxiv.org/html/2602.06394v1#A3.E5 "Equation 5 ‣ Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), using the learned parameters within θadapt∗\theta\_{\text{adapt}}^{\*} (e.g., α∗\alpha^{\*}). This process continues until the target vocabulary size is reached. Alternatively, if the RL policy πθπ∗\pi\_{\theta\_{\pi}}^{\*} is robust across variations in θadapt\theta\_{\text{adapt}}, it could be used with inputs (state features, merge scores) calculated using θadapt∗\theta\_{\text{adapt}}^{\*}. However, the greedy approach based on wa​b​(θadapt∗)w\_{ab}(\theta\_{\text{adapt}}^{\*}) is generally more direct and computationally efficient for deployment, leveraging the refined understanding of "good" merges embodied in θadapt∗\theta\_{\text{adapt}}^{\*}.

Algorithm 3  Final Vocabulary Construction

1: Input: Corpus 𝒮\mathcal{S}, optimized θadapt∗\theta\_{\text{adapt}}^{\*}, target size KK

2: Initialize vocabulary V=ΣV=\Sigma, merge count m=0m=0

3: while m<Km<K do

4:  Compute all merge scores: wa​b=f​(a,b)f​(a)​f​(b)+ϵf⋅(q¯a​b+ϵQ)α∗⋅ψ​(a,b)w\_{ab}=\frac{f(a,b)}{f(a)f(b)+\epsilon\_{f}}\cdot(\bar{q}\_{ab}+\epsilon\_{Q})^{\alpha^{\*}}\cdot\psi(a,b)

5:  Select best merge: (a∗,b∗)=arg⁡max(a,b)⁡wa​b(a^{\*},b^{\*})=\arg\max\_{(a,b)}w\_{ab}

6:  Update vocabulary: V←V∪{a∗​b∗}V\leftarrow V\cup\{a^{\*}b^{\*}\} // Constituents a∗,b∗a^{\*},b^{\*} remain in VV

7:  Update corpus statistics and recompute affected frequencies

8:  m←m+1m\leftarrow m+1

9: end while

10: Output: Final vocabulary V∗V^{\*}

### E.4 Convergence Properties

The sequential learning process has the following theoretical guarantees:

###### Theorem E.1 (Two-Timescale Convergence).

Under assumptions A1-A4 (Section [C.6](https://arxiv.org/html/2602.06394v1#A3.SS6 "C.6 Assumptions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), the sequential optimization of θπ\theta\_{\pi} (fast timescale) and θadapt\theta\_{\text{adapt}} (slow timescale) converges to a local Nash equilibrium with probability 1.

###### Proof.

The result follows from two-timescale stochastic approximation (Borkar, [2009](https://arxiv.org/html/2602.06394v1#bib.bib89 "Stochastic approximation: a dynamical systems viewpoint")). Under (A1)–(A4), the conditions of Theorem 2 in (Borkar, [2009](https://arxiv.org/html/2602.06394v1#bib.bib89 "Stochastic approximation: a dynamical systems viewpoint")) are satisfied: (i) Lipschitz gradients (from bounded rewards and smooth parameterization), (ii) bounded iterates via projection, (iii) martingale noise with bounded variance, and (iv) proper step sizes (∑tηt=∞\sum\_{t}\eta\_{t}=\infty, ∑tηt2<∞\sum\_{t}\eta\_{t}^{2}<\infty).

With timescale separation ηπ(t)/ηadapt(t)→∞\eta\_{\pi}^{(t)}/\eta\_{\text{adapt}}^{(t)}\to\infty, the fast iterate θπ\theta\_{\pi} equilibrates before significant movement in θadapt\theta\_{\text{adapt}}. The iterates converge almost surely to limit points (θπ∗,θadapt∗)(\theta\_{\pi}^{\*},\theta\_{\text{adapt}}^{\*}) satisfying ∇θπJ=0\nabla\_{\theta\_{\pi}}J=0 and ∇θadaptLtotal=0\nabla\_{\theta\_{\text{adapt}}}L\_{\text{total}}=0, constituting a local Nash equilibrium.
∎

Key Properties:

* •

  Stage 1 Convergence: PPO converges to a stationary point at rate O​(1/T)O(1/\sqrt{T}) (Proposition [C.6](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem6 "Proposition C.6 (Convergence of PPO Objective). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"))
* •

  Stage 2 Convergence: Gumbel-Softmax optimization converges at rate O​(1/T)+O​(τ2)O(1/\sqrt{T})+O(\tau^{2}) (Proposition [C.7](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem7 "Proposition C.7 (Consistency and Boundedness of Stage 2 Gradients). ‣ Proof of Theorem 3.2 (Computational Complexity). ‣ C.5 Theory Proofs ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"))
* •

  Overall Optimality: The greedy vocabulary construction with θadapt∗\theta\_{\text{adapt}}^{\*} achieves (1−1/e)(1-1/e)-approximation (Theorem [C.11](https://arxiv.org/html/2602.06394v1#A3.Thmtheorem11 "Theorem C.11 (Approximation Guarantee with Explicit Constants). ‣ C.7 Theory Extensions ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"))

###### Proposition E.2 (Convergence of Adaptive Learning with Explicit Constants).

Under Assumptions A1–A4, with ηt=η0/t\eta\_{t}=\eta\_{0}/\sqrt{t} and η0≤1/(2​L)\eta\_{0}\leq 1/(2L), where LL is the Lipschitz constant of ∇Ltotal\nabla L\_{\text{total}}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖∇Ltotal​(θadaptT)‖2]≤2​(Ltotal​(θadapt0)−L∗)η0​T+4​η0​L​σ2T,\mathbb{E}[\|\nabla L\_{\text{total}}(\theta\_{\text{adapt}}^{T})\|^{2}]\leq\frac{2(L\_{\text{total}}(\theta\_{\text{adapt}}^{0})-L^{\*})}{\eta\_{0}\sqrt{T}}+\frac{4\eta\_{0}L\sigma^{2}}{\sqrt{T}}, |  | (27) |

where L∗L^{\*} is the optimal value and σ2\sigma^{2} bounds gradient variance.

###### Proof.

The proof follows standard non-convex SGD analysis (Kingma and Ba, [2014](https://arxiv.org/html/2602.06394v1#bib.bib44 "Adam: a method for stochastic optimization")). By smoothness of LtotalL\_{\text{total}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ltotal​(θt+1)≤Ltotal​(θt)−ηt​⟨∇Ltotal​(θt),gt⟩+L​ηt22​‖gt‖2L\_{\text{total}}(\theta^{t+1})\leq L\_{\text{total}}(\theta^{t})-\eta\_{t}\langle\nabla L\_{\text{total}}(\theta^{t}),g\_{t}\rangle+\frac{L\eta\_{t}^{2}}{2}\|g\_{t}\|^{2} |  | (28) |

where gtg\_{t} is the stochastic gradient. Taking expectations and using 𝔼​[gt]=∇Ltotal​(θt)\mathbb{E}[g\_{t}]=\nabla L\_{\text{total}}(\theta^{t}) and 𝔼​[‖gt‖2]≤‖∇Ltotal​(θt)‖2+σ2\mathbb{E}[\|g\_{t}\|^{2}]\leq\|\nabla L\_{\text{total}}(\theta^{t})\|^{2}+\sigma^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Ltotal​(θt+1)]≤𝔼​[Ltotal​(θt)]−ηt​(1−L​ηt/2)​𝔼​[‖∇Ltotal​(θt)‖2]+L​ηt2​σ22\mathbb{E}[L\_{\text{total}}(\theta^{t+1})]\leq\mathbb{E}[L\_{\text{total}}(\theta^{t})]-\eta\_{t}(1-L\eta\_{t}/2)\mathbb{E}[\|\nabla L\_{\text{total}}(\theta^{t})\|^{2}]+\frac{L\eta\_{t}^{2}\sigma^{2}}{2} |  | (29) |

Telescoping over TT iterations with ηt=η0/t\eta\_{t}=\eta\_{0}/\sqrt{t} and η0≤1/(2​L)\eta\_{0}\leq 1/(2L) yields the stated bound.

*Remark:* Under temperature annealing τt→0\tau\_{t}\to 0, the Gumbel-Softmax bias term B​(τ)2→0B(\tau)^{2}\to 0, ensuring asymptotic unbiasedness.
∎

###### Theorem E.3 (Local vs Global Optimality).

The two-timescale optimization converges to a local Nash equilibrium (θπ∗,θadapt∗)(\theta\_{\pi}^{\*},\theta\_{\text{adapt}}^{\*}) with quality bounds under local strong convexity; probabilistic restarts increase the chance of reaching global optima.

###### Proof.

Part 1: Local Nash Equilibrium. By Theorem [E.1](https://arxiv.org/html/2602.06394v1#A5.Thmtheorem1 "Theorem E.1 (Two-Timescale Convergence). ‣ E.4 Convergence Properties ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), the limit points satisfy ∇θπJ=0\nabla\_{\theta\_{\pi}}J=0 and ∇θadaptLtotal=0\nabla\_{\theta\_{\text{adapt}}}L\_{\text{total}}=0, constituting a local Nash equilibrium.

Part 2: Quality Bounds. Under μ\mu-strong convexity of LtotalL\_{\text{total}} in neighborhood ℬr​(θadapt∗)\mathcal{B}\_{r}(\theta\_{\text{adapt}}^{\*}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ltotal​(θadapt∗)−Ltotal​(θadaptglobal)≤12​μ​‖∇Ltotal​(θadapt∗)‖2=0L\_{\text{total}}(\theta\_{\text{adapt}}^{\*})-L\_{\text{total}}(\theta\_{\text{adapt}}^{\text{global}})\leq\frac{1}{2\mu}\|\nabla L\_{\text{total}}(\theta\_{\text{adapt}}^{\*})\|^{2}=0 |  | (30) |

if the global optimum lies within the basin of attraction.

Part 3: Probabilistic Restarts. With MM independent runs, ℙ​[find global]=1−(1−pbasin)M≥1−e−M⋅pbasin\mathbb{P}[\text{find global}]=1-(1-p\_{\text{basin}})^{M}\geq 1-e^{-M\cdot p\_{\text{basin}}}, achieving probability ≥1−δ\geq 1-\delta for M=O​(log⁡(1/δ)/pbasin)M=O(\log(1/\delta)/p\_{\text{basin}}) restarts.
∎

### E.5 Algorithm Summary

Algorithm 4  QA-Token: Quality-Aware Tokenization Framework

1: Input: Corpus 𝒞\mathcal{C}, quality scores QQ, vocabulary budget KK

2: Output: Optimized vocabulary V∗V^{\*}

3:

4: Stage 1: RL Policy Optimization

5: Initialize policy πθπ\pi\_{\theta\_{\pi}}, adaptive parameters θadapt(0)\theta\_{\text{adapt}}^{(0)}

6: for episode e=1e=1 to EE do

7:  V←ΣV\leftarrow\Sigma (base alphabet)

8:  for step t=1t=1 to KK do

9:   Compute priority queue P​QtPQ\_{t} with scores wa​b​(⋅;θadapt(0))w\_{ab}(\cdot;\theta\_{\text{adapt}}^{(0)})

10:   Select merge (a,b)∼πθπ(⋅|st)(a,b)\sim\pi\_{\theta\_{\pi}}(\cdot|s\_{t}) from P​QtPQ\_{t}

11:   Execute merge: V←V∪{a​b}V\leftarrow V\cup\{ab\} // Add merged token

12:   Compute reward RtR\_{t} using Eq. [26](https://arxiv.org/html/2602.06394v1#A5.E26 "Equation 26 ‣ E.1.2 Reward Function Design ‣ E.1 Stage 1: Reinforcement Learning Policy Optimization ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")

13:  end for

14:  Update πθπ\pi\_{\theta\_{\pi}} via PPO using trajectory rewards

15: end for

16:

17: Stage 2: Adaptive Parameter Learning

18: for iteration i=1i=1 to II do

19:  Sample mini-batch of merge candidates ℬ\mathcal{B}

20:  Compute logits ℓa​b​(θadapt)\ell\_{ab}(\theta\_{\text{adapt}}) using Eq. [37](https://arxiv.org/html/2602.06394v1#A5.E37 "Equation 37 ‣ E.11 Gradient Computation ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")

21:  Sample Gumbel noise and compute soft selection via Eq. [38](https://arxiv.org/html/2602.06394v1#A5.E38 "Equation 38 ‣ E.11 Gradient Computation ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")

22:  Evaluate task loss LtaskL\_{\text{task}} on downstream objective

23:  Update θadapt←θadapt−ηi​∇Ltotal\theta\_{\text{adapt}}\leftarrow\theta\_{\text{adapt}}-\eta\_{i}\nabla L\_{\text{total}}

24: end for

25:

26: Final Vocabulary Construction

27: Build final vocabulary using greedy merges with wa​b​(⋅;θadapt∗)w\_{ab}(\cdot;\theta\_{\text{adapt}}^{\*})

28: Return V∗V^{\*}




Algorithm 5  QA-Token Integration with Downstream Transformer

1: Input: Raw sequence XX, trained QA-Token vocab V∗V^{\*}, Transformer model MθM\_{\theta}

2: Output: Task predictions Y^\hat{Y}

3:

4: // Tokenization (no overhead vs. BPE)

5: T←Tokenize​(X,V∗)T\leftarrow\text{Tokenize}(X,V^{\*}) // Standard greedy tokenization

6:

7: // Embedding and Encoding

8: E←TokenEmbed​(T)+PosEmbed​(positions)E\leftarrow\text{TokenEmbed}(T)+\text{PosEmbed}(\text{positions})

9: for layer ℓ=1\ell=1 to LL do

10:  E←TransformerBlockℓ​(E)E\leftarrow\text{TransformerBlock}\_{\ell}(E)

11: end for

12:

13: // Task Head

14: Y^←TaskHead​(E)\hat{Y}\leftarrow\text{TaskHead}(E) // Classification, regression, or generation

15: Return Y^\hat{Y}

  



Algorithm 6  Meta-Learning Initialization for Adaptive Parameters

0: Task distribution 𝒫​(𝒯)\mathcal{P}(\mathcal{T}), base initialization θadapt(0)\theta\_{\text{adapt}}^{(0)}, inner steps KK, inner lr ηin\eta\_{\text{in}}, outer lr ηout\eta\_{\text{out}}

1: while not converged do

2:  Sample batch of tasks {𝒯i}∼𝒫​(𝒯)\{\mathcal{T}\_{i}\}\sim\mathcal{P}(\mathcal{T})

3:  for each task 𝒯i\mathcal{T}\_{i} do

4:   Set θi←θadapt(0)\theta\_{i}\leftarrow\theta\_{\text{adapt}}^{(0)}

5:   for k=1​…​Kk=1\dots K do

6:    Compute Ltotal(i)​(θi)L\_{\text{total}}^{(i)}(\theta\_{i}) on 𝒯i\mathcal{T}\_{i} and update θi←θi−ηin​∇θLtotal(i)​(θi)\theta\_{i}\leftarrow\theta\_{i}-\eta\_{\text{in}}\,\nabla\_{\theta}L\_{\text{total}}^{(i)}(\theta\_{i})

7:   end for

8:  end for

9:  Update initialization: θadapt(0)←θadapt(0)−ηout​∑i∇θadapt(0)Ltotal(i)​(θi)\theta\_{\text{adapt}}^{(0)}\leftarrow\theta\_{\text{adapt}}^{(0)}-\eta\_{\text{out}}\,\sum\_{i}\nabla\_{\theta\_{\text{adapt}}^{(0)}}L\_{\text{total}}^{(i)}(\theta\_{i})

10: end while

11:

12: return meta-initialization θadapt⋆\theta\_{\text{adapt}}^{\star}

### E.6 RL Training Implementation

#### E.6.1 State Representation

The state sts\_{t} provided to the RL agent at merge step tt includes:

* •

  Global Features: Current vocabulary size |Vt||V\_{t}|; remaining merge steps T−tT-t; aggregated token statistics (average length, mean/std of quality scores).
* •

  Candidate Pair Features (top-KP​QK\_{PQ} from priority queue): For each pair (a,b)(a,b): frequencies f​(a),f​(b),f​(a,b)f(a),f(b),f(a,b); qualities qa,qbq\_{a},q\_{b}; lengths |a|,|b||a|,|b|; merge score wa​bw\_{ab}.
* •

  Domain Context: Market regime indicators (finance), platform ID (social media), or sequence quality (genomics).

The PPO agent uses an MLP with 2 hidden layers (256 units each, ReLU activations). The policy network outputs action probabilities over KP​QK\_{PQ} candidates; the value network outputs a single scalar.

#### E.6.2 Exploration Strategy

An ϵ\epsilon-greedy strategy is employed with ϵ\epsilon annealed from ϵ0=0.5\epsilon\_{0}=0.5 to ϵfinal=0.05\epsilon\_{\text{final}}=0.05 over training episodes using exponential decay, balancing exploration and exploitation effectively across all domains.

### E.7 MDP Formulation and Details

###### Definition E.4 (Tokenization MDP).

The tokenization MDP is a tuple ℳ=(𝒮,𝒜,𝒫,ℛ,γ,T)\mathcal{M}=(\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma,T) where:

1. 1.

   State Space 𝒮\mathcal{S}: Each state st∈𝒮⊂ℝds\_{t}\in\mathcal{S}\subset\mathbb{R}^{d} encodes:

   * •

     Current vocabulary VtV\_{t} and its statistics (size, token length distribution)
   * •

     Priority queue P​Qt={(ai,bi,wai​bi)}i=1KP​QPQ\_{t}=\{(a\_{i},b\_{i},w\_{a\_{i}b\_{i}})\}\_{i=1}^{K\_{PQ}} of top merge candidates
   * •

     Corpus statistics: frequency distributions, quality histograms
   * •

     Progress indicator: t/Tt/T where TT is the merge budget

   Formally, st=[ϕ​(Vt),ϕ​(P​Qt),ϕ​(𝒮t),t/T]∈ℝds\_{t}=[\phi(V\_{t}),\phi(PQ\_{t}),\phi(\mathcal{S}\_{t}),t/T]\in\mathbb{R}^{d}.

   State Encoding Function ϕ\phi: The encoding function ϕ:𝒳→ℝd𝒳\phi:\mathcal{X}\to\mathbb{R}^{d\_{\mathcal{X}}} maps variable-size structures to fixed-dimensional vectors:

   * •

     ϕ​(Vt)=[|Vt|/|Σ|,|t|¯,σ|t|,q¯t,σqt]∈ℝ5\phi(V\_{t})=[|V\_{t}|/|\Sigma|,\bar{|t|},\sigma\_{|t|},\bar{q}\_{t},\sigma\_{q\_{t}}]\in\mathbb{R}^{5}: vocabulary size ratio, mean/std of token lengths, mean/std of token qualities.
   * •

     ϕ​(P​Qt)∈ℝ6⋅KP​Q\phi(PQ\_{t})\in\mathbb{R}^{6\cdot K\_{PQ}}: For top-KP​QK\_{PQ} candidates, concatenate [wa​b,qa,qb,|a|,|b|,log⁡f​(a,b)][w\_{ab},q\_{a},q\_{b},|a|,|b|,\log f(a,b)] per pair. Pad with zeros if fewer candidates exist.
   * •

     ϕ​(𝒮t)∈ℝ20\phi(\mathcal{S}\_{t})\in\mathbb{R}^{20}: Quality histogram (Bq=10B\_{q}=10 bins over [0,1][0,1]) and log-frequency histogram (Bf=10B\_{f}=10 bins over observed range).

   Total state dimension: d=5+6⋅KP​Q+20+1d=5+6\cdot K\_{PQ}+20+1. With KP​Q=50K\_{PQ}=50, we have d=326d=326. The MLP policy network processes this representation via two hidden layers (256, 128 units) with ReLU activations (see Appendix [E.6](https://arxiv.org/html/2602.06394v1#A5.SS6 "E.6 RL Training Implementation ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
2. 2.

   Action Space 𝒜t\mathcal{A}\_{t}: At time tt:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝒜t={i:(ai,bi)∈P​Qt,i≤KP​Q}\mathcal{A}\_{t}=\{i:(a\_{i},b\_{i})\in PQ\_{t},i\leq K\_{PQ}\} |  | (31) |

   Each action at∈𝒜ta\_{t}\in\mathcal{A}\_{t} selects a merge pair from the priority queue.
3. 3.

   Transition Dynamics 𝒫\mathcal{P}: Deterministic transitions:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | st+1=𝒫​(st,at)=UPDATE​(st,MERGE​(aat,bat))s\_{t+1}=\mathcal{P}(s\_{t},a\_{t})=\text{UPDATE}(s\_{t},\text{MERGE}(a\_{a\_{t}},b\_{a\_{t}})) |  | (32) |

   where MERGE executes vocabulary update and UPDATE recomputes statistics.
4. 4.

   Reward Function: ℛ​(st,at)=R​(aat,bat;θadapt(0))\mathcal{R}(s\_{t},a\_{t})=R(a\_{a\_{t}},b\_{a\_{t}};\theta\_{\text{adapt}}^{(0)})
5. 5.

   Discount Factor: γ=1\gamma=1 (undiscounted, finite horizon)
6. 6.

   Horizon: T=KT=K merge operations

###### Proposition E.5 (MDP Well-Formedness).

The tokenization MDP satisfies:

1. 1.

   Markov Property: P​(st+1|st,at,st−1,…)=P​(st+1|st,at)P(s\_{t+1}|s\_{t},a\_{t},s\_{t-1},\ldots)=P(s\_{t+1}|s\_{t},a\_{t})
2. 2.

   Bounded State Space: ‖st‖2≤Cs\|s\_{t}\|\_{2}\leq C\_{s}
3. 3.

   Finite Action Space: |𝒜t|≤KP​Q|\mathcal{A}\_{t}|\leq K\_{PQ}

###### Proof.

(1) follows from state containing complete information for transitions. (2) holds as vocabulary size is bounded by |Σ|+T|\Sigma|+T and frequencies are normalized. (3) is by construction of the priority queue.
∎

□\square

### E.8 Reward Normalization Details

Each raw reward component Rjraw​(a,b)R^{\text{raw}}\_{j}(a,b) is normalized using adaptive running statistics. We maintain exponential moving averages (EMAs) for mean μj,trun\mu\_{j,t}^{\text{run}} and variance Varj,trun\text{Var}\_{j,t}^{\text{run}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μj,trun=(1−βnorm)​μj,t−1run+βnorm​Rjraw​(a,b)\mu\_{j,t}^{\text{run}}=(1-\beta\_{\text{norm}})\mu\_{j,t-1}^{\text{run}}+\beta\_{\text{norm}}R^{\text{raw}}\_{j}(a,b) |  | (33) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Varj,trun=(1−βnorm)​Varj,t−1run+βnorm​(Rjraw​(a,b)−μj,t−1run)​(Rjraw​(a,b)−μj,trun)\text{Var}\_{j,t}^{\text{run}}=(1-\beta\_{\text{norm}})\text{Var}\_{j,t-1}^{\text{run}}+\beta\_{\text{norm}}(R^{\text{raw}}\_{j}(a,b)-\mu\_{j,t-1}^{\text{run}})(R^{\text{raw}}\_{j}(a,b)-\mu\_{j,t}^{\text{run}}) |  | (34) |

where βnorm∈[10−3,10−2]\beta\_{\text{norm}}\in[10^{-3},10^{-2}]. The normalized component is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^j​(a,b)=Rjraw​(a,b)−μj,t−1runσj,t−1run+ϵR\hat{R}\_{j}(a,b)=\frac{R^{\text{raw}}\_{j}(a,b)-\mu\_{j,t-1}^{\text{run}}}{\sigma\_{j,t-1}^{\text{run}}+\epsilon\_{R}} |  | (35) |

with ϵR=10−8\epsilon\_{R}=10^{-8} for stability.

### E.9 Gumbel-Softmax Gradient Derivation and Temperature Annealing

### E.10 Temperature Annealing Schedule

We employ an exponential annealing schedule for the temperature parameter:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ​(t)=τinit⋅exp⁡(−βanneal⋅t/Tanneal),\tau(t)=\tau\_{\text{init}}\cdot\exp(-\beta\_{\text{anneal}}\cdot t/T\_{\text{anneal}}), |  | (36) |

where τinit=1.0\tau\_{\text{init}}=1.0, βanneal=3.0\beta\_{\text{anneal}}=3.0, and TannealT\_{\text{anneal}} is the total number of optimization steps.

This schedule ensures:

* •

  Early exploration: High initial temperature allows exploration of diverse merge patterns
* •

  Gradual refinement: Exponential decay provides smooth transition to discrete selections
* •

  Convergence: Low final temperature approaches one-hot categorical sampling

### E.11 Gradient Computation

The composite logits for candidate merge (a,b)(a,b) are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓa​b​(θadapt)=wa​b​(a,b;α)+∑jλj​Rjraw​(a,b),\ell\_{ab}(\theta\_{\text{adapt}})=w\_{ab}(a,b;\alpha)+\sum\_{j}\lambda\_{j}R^{\text{raw}}\_{j}(a,b), |  | (37) |

which are differentiable with respect to θadapt\theta\_{\text{adapt}} through both the merge score and reward weights.

The composite logits combine wa​bw\_{ab} (which incorporates frequency via PMI and quality via q¯a​b\bar{q}\_{ab}) with raw reward components RjrawR^{\text{raw}}\_{j} that also capture quality (RQrawR^{\text{raw}}\_{Q}) and information (RIrawR^{\text{raw}}\_{I}).

Rationale for Intentional Overlap: While there is deliberate overlap between these components (both encode quality and frequency signals), they serve *distinct optimization purposes*:

* •

  wa​bw\_{ab} (merge score): Optimized via the RL objective (cumulative discounted reward) during Stage 1, capturing *corpus-level* quality-frequency tradeoffs that generalize across merge sequences.
* •

  ∑jλj​Rjraw\sum\_{j}\lambda\_{j}R^{\text{raw}}\_{j} (weighted rewards): Optimized via the downstream task loss LtaskL\_{\text{task}} during Stage 2, enabling *task-specific* reweighting of quality vs. information vs. complexity.

This decomposition allows the system to learn *different* quality-frequency tradeoffs for policy learning (Stage 1) versus task-specific adaptation (Stage 2). The parameter α\alpha controls general token quality preferences learned from reward maximization, while λj\lambda\_{j} adjusts relative importance based on task-specific gradients. Ablation studies (Appendix [G.5](https://arxiv.org/html/2602.06394v1#A7.SS5 "G.5 Ablation Studies and Additional Experiments ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), Table [13](https://arxiv.org/html/2602.06394v1#A7.T13 "Table 13 ‣ G.5.1 RL Algorithm Ablation ‣ G.5 Ablation Studies and Additional Experiments ‣ Appendix G Complete Experimental Results ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) confirm that removing either component degrades downstream performance by 3–8%, validating that both contributions are necessary despite their overlap.

The Gumbel-Softmax distribution provides a differentiable approximation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi=exp⁡((ℓi+gi)/τ)∑j=1|𝒞|exp⁡((ℓj+gj)/τ),gi∼Gumbel​(0,1)y\_{i}=\frac{\exp((\ell\_{i}+g\_{i})/\tau)}{\sum\_{j=1}^{|\mathcal{C}|}\exp((\ell\_{j}+g\_{j})/\tau)},\quad g\_{i}\sim\text{Gumbel}(0,1) |  | (38) |

The gradient of the task loss is computed via Monte Carlo sampling:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θadaptLtask=𝔼𝐠​[∇θadaptLtask​(𝐲​(ℓ​(θadapt),𝐠,τ))]\nabla\_{\theta\_{\text{adapt}}}L\_{\text{task}}=\mathbb{E}\_{\mathbf{g}}\left[\nabla\_{\theta\_{\text{adapt}}}L\_{\text{task}}(\mathbf{y}(\bm{\ell}(\theta\_{\text{adapt}}),\mathbf{g},\tau))\right] |  | (39) |

where 𝐠\mathbf{g} is sampled Gumbel noise.

Gradient Flow: The gradient flows through:

1. 1.

   Task loss: LtaskL\_{\text{task}} evaluates performance on downstream data
2. 2.

   Soft tokenization: Gumbel-Softmax provides differentiable token boundaries
3. 3.

   Merge logits: ℓa​b\ell\_{ab} depends on learnable θadapt\theta\_{\text{adapt}}
4. 4.

   Quality scores: Through α\alpha and domain parameters βpos,βvol\beta\_{\text{pos}},\beta\_{\text{vol}}
5. 5.

   Reward weights: Through 𝝀\bm{\lambda} in the composite score

## Appendix F Hyperparameter Sensitivity Analysis

We conducted a comprehensive sensitivity analysis on key parameters of the QA-Token framework: the quality sensitivity exponent α\alpha, the primary quality reward weight λQ\lambda\_{Q}, and the domain-specific volatility scaling exponent βvol\beta\_{\text{vol}} for finance. For each parameter, we varied its value across a specified range while holding all other hyperparameters at their optimal values, as determined during the adaptive learning phase.

The results, summarized in Table [10](https://arxiv.org/html/2602.06394v1#A6.T10 "Table 10 ‣ Appendix F Hyperparameter Sensitivity Analysis ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), demonstrate that while performance is optimal at the learned parameter values, the framework is not unduly sensitive to minor perturbations. Performance degrades gracefully rather than catastrophically as parameters deviate from their optima, suggesting the model occupies a reasonably wide basin of attraction in the hyperparameter space.

Table 10: Hyperparameter Sensitivity Analysis. Performance on the primary metric is reported as key hyperparameters are varied around their learned optimal value (indicated by \*). Values are means over n=5n=5 runs.

|  |  |  |
| --- | --- | --- |
| Parameter | Value | Performance Metric |
| Genomics (QA-BPE-seq) - Metric: Variant F1 | | |
| α\alpha (Quality Sensitivity) | 0.3 | 0.869 |
|  | 0.5 | 0.879 |
|  | 0.72\* | 0.891 |
|  | 1.0 | 0.884 |
|  | 1.5 | 0.872 |
| λQ\lambda\_{Q} (Quality Reward Weight) | 0.15 | 0.879 |
|  | 0.25 | 0.886 |
|  | 0.35\* | 0.891 |
|  | 0.45 | 0.885 |
|  | 0.55 | 0.878 |
| Finance (QAT-QF) - Metric: Sharpe Ratio | | |
| α\alpha (Quality Sensitivity) | 0.25 | 1.61 |
|  | 0.50 | 1.68 |
|  | 0.95\* | 1.72 |
|  | 1.50 | 1.65 |
|  | 2.00 | 1.58 |
| βvol\beta\_{\text{vol}} (Volatility Scaling) | 0.10 | 1.63 |
|  | 0.30 | 1.69 |
|  | 0.50\* | 1.72 |
|  | 0.70 | 1.67 |
|  | 1.00 | 1.60 |

## Appendix G Complete Experimental Results

This section provides comprehensive experimental results across all domains, including detailed analysis, foundation-scale evaluations, and ablation studies.

### G.1 Genomics Results: Detailed Analysis

Key Observations: QA-BPE-seq achieves 4.0 percentage point F1 improvement in variant calling over DNABERT-k (0.891 vs. 0.851) with Hedges’ g=8.2g=8.2—a large effect size. Compared to standard BPE (0.824), the improvement is 6.7 percentage points. Taxonomic classification shows 3.1 percentage point gain over domain-standard k-mer tokenization. Sequence reconstruction improves by 16%, indicating information preservation.

Key Insights:

1. 1.

   Byte-level models fail catastrophically: ByT5 and CANINE show 2.5× slower inference with 7-9% lower accuracy, definitively establishing that vocabulary-based tokenization remains essential for genomic sequences.
2. 2.

   Quality awareness is learnable: The converged parameters (α=0.72±0.03\alpha=0.72\pm 0.03, βpos=0.014±0.002\beta\_{\text{pos}}=0.014\pm 0.002) demonstrate that optimal quality sensitivity can be discovered through our adaptive learning framework.
3. 3.

   Mechanism of improvement: Analysis of generated vocabularies reveals that QA-BPE-seq creates tokens aligned with biological units (codons, motifs) while breaking at error-prone junctions—a behavior that emerges without explicit biological supervision.

### G.2 Financial Foundation Model: Detailed Results Analysis

QAT-QF demonstrates remarkable consistency across all financial tasks, with zero-shot improvements ranging from 7.3% to 27.0

Specific Observations:

* •

  The model’s superior performance on regime detection (+11.6% F1) and tail risk estimation (+18.0%) suggests that quality-aware tokenization captures market dynamics that frequency-based methods miss.
* •

  Particularly noteworthy is the 27.0% improvement in order flow imbalance prediction, a task highly sensitive to microstructure noise.
* •

  These results validate our hypothesis that incorporating quality signals during tokenization enables foundation models to learn more robust representations of financial time series.

### G.3 Computational Costs

Training Time.

* •

  Standard BPE: 5–10 minutes (5GB, CPU)
* •

  QA-Token Stage 1 (RL): 30–36 GPU-hours (A100)
* •

  QA-Token Stage 2 (Adaptive): 20–24 GPU-hours

Memory Requirements.

* •

  Priority Queue: O​(KP​Q⋅d)O(K\_{PQ}\cdot d) (∼10{\sim}10 MB for KP​Q=200K\_{PQ}{=}200)
* •

  Quality Statistics: O​(|V|⋅s)O(|V|\cdot s) (∼100{\sim}100 MB for 32K vocab)
* •

  Pair Frequencies: O​(|V|2)O(|V|^{2}) (∼4{\sim}4 GB for 32K vocab)
* •

  Peak: ∼16{\sim}16 GB GPU

Hierarchical Training via Quality-Stratified Sampling.
For massive corpora where full vocabulary optimization is infeasible, we employ *quality-variance importance sampling*: data points are sampled with probability proportional to Var​(qi)+ϵbase\text{Var}(q\_{i})+\epsilon\_{\text{base}}, prioritizing regions with heterogeneous quality where tokenization decisions have the greatest impact.

###### Definition G.1 (Notation for Hierarchical Training).

Let 𝒞\mathcal{C} denote the full corpus and 𝒮⊆𝒞\mathcal{S}\subseteq\mathcal{C} a subset with |𝒮|=r⋅|𝒞||\mathcal{S}|=r\cdot|\mathcal{C}| for *subset ratio* r∈(0,1]r\in(0,1]. Define:

* •

  ℒ​(V;D)=𝔼x∼D​[−log⁡PLM​(x|V)]\mathcal{L}(V;D)=\mathbb{E}\_{x\sim D}[-\log P\_{\text{LM}}(x|V)]: expected language modeling loss on distribution DD using vocabulary VV
* •

  V𝒮∗=arg⁡minV⁡ℒ​(V;𝒮)V\_{\mathcal{S}}^{\*}=\arg\min\_{V}\mathcal{L}(V;\mathcal{S}): optimal vocabulary for subset 𝒮\mathcal{S}
* •

  V𝒞∗=arg⁡minV⁡ℒ​(V;𝒞)V\_{\mathcal{C}}^{\*}=\arg\min\_{V}\mathcal{L}(V;\mathcal{C}): optimal vocabulary for full corpus 𝒞\mathcal{C}

###### Proposition G.2 (Hierarchical Training Bound).

Under the following assumptions:

1. (A1)

   The loss ℒ​(V;⋅)\mathcal{L}(V;\cdot) is LL-Lipschitz in the data distribution (bounded sensitivity to distribution shift)
2. (A2)

   Quality-variance importance sampling achieves effective sample size neff=r⋅|𝒞|/(1+CV2)n\_{\text{eff}}=r\cdot|\mathcal{C}|/(1+\text{CV}^{2}) where CV is the coefficient of variation of importance weights

Then the vocabulary V𝒮∗V\_{\mathcal{S}}^{\*} learned on the importance-sampled subset satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ℒ​(V𝒮∗;𝒞)]≤ℒ​(V𝒞∗;𝒞)+O​(L⋅1+CV2r⋅|𝒞|).\mathbb{E}[\mathcal{L}(V\_{\mathcal{S}}^{\*};\mathcal{C})]\leq\mathcal{L}(V\_{\mathcal{C}}^{\*};\mathcal{C})+O\left(L\cdot\sqrt{\frac{1+\text{CV}^{2}}{r\cdot|\mathcal{C}|}}\right). |  | (40) |

###### Proof Sketch.

The bound follows from standard importance sampling theory (Owen, [2013](https://arxiv.org/html/2602.06394v1#bib.bib109 "Monte carlo theory, methods and examples")). Under (A1), the difference |ℒ​(V;𝒮)−ℒ​(V;𝒞)||\mathcal{L}(V;\mathcal{S})-\mathcal{L}(V;\mathcal{C})| is controlled by the distributional divergence between 𝒮\mathcal{S} and 𝒞\mathcal{C}. Importance sampling with weights wi∝Var​(qi)+ϵbasew\_{i}\propto\text{Var}(q\_{i})+\epsilon\_{\text{base}} reduces this divergence by oversampling high-variance regions where tokenization quality matters most. By the effective sample size formula for importance sampling, the estimation error scales as O​(1/neff)O(1/\sqrt{n\_{\text{eff}}}), yielding the stated bound. The Lipschitz assumption (A1) ensures that optimization on 𝒮\mathcal{S} transfers to 𝒞\mathcal{C}.
∎

Massive-Scale Strategies (>100TB).

1. 1.

   Quality-stratified sampling (0.1–1%)
2. 2.

   Distributed PPO (8–32 GPUs)
3. 3.

   Online RL with replay for streams
4. 4.

   Memory-mapped frequency tables

Cost-Benefit.

* •

  +5–30% task performance
* •

  -15–20% token count (faster inference)
* •

  One-time cost amortized across applications

### G.4 Foundation-Scale Results (Pathogen Detection, GUE)

Table 11: Pathogen Detection benchmark (MCC).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Task | DNABERT-2 | DNABERT-S | NT-2.5b-Multi | NT-2.5b-1000g | METAGENE-1 | METAGENE-1 (QA-Token) |
| Pathogen-Detect (avg.) | 87.92 | 87.02 | 82.43 | 79.02 | 92.96 | 94.53 |
| Pathogen-Detect-1 | 86.73 | 85.43 | 83.80 | 77.52 | 92.14 | 93.81 |
| Pathogen-Detect-2 | 86.90 | 85.23 | 83.53 | 80.38 | 90.91 | 92.95 |
| Pathogen-Detect-3 | 88.30 | 89.01 | 82.48 | 79.83 | 93.70 | 95.12 |
| Pathogen-Detect-4 | 89.77 | 88.41 | 79.91 | 78.37 | 95.10 | 96.24 |




Table 12: Genome Understanding Evaluation (GUE). All metrics are MCC except COVID which uses F1.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Task | CNN | HyenaDNA | DNABERT | NT-2.5B-Multi | DNABERT-2 | METAGENE-1 | METAGENE-1 (QA-Token) |
| TF-Mouse (AVG.) | 45.3 | 51.0 | 57.7 | 67.0 | 68.0 | 71.4 | 72.8 |
| 0 | 31.1 | 35.6 | 42.3 | 63.3 | 56.8 | 61.5 | 62.1 |
| 1 | 59.7 | 80.5 | 79.1 | 83.8 | 84.8 | 83.7 | 84.1 |
| 2 | 63.2 | 65.3 | 69.9 | 71.5 | 79.3 | 83.0 | 84.5 |
| 3 | 45.5 | 54.2 | 55.4 | 69.4 | 66.5 | 82.2 | 83.3 |
| 4 | 27.2 | 19.2 | 42.0 | 47.1 | 52.7 | 46.6 | 47.0 |
| TF-HUMAN (AVG.) | 50.7 | 56.0 | 64.4 | 62.6 | 70.1 | 68.3 | 69.9 |
| 0 | 54.0 | 62.3 | 68.0 | 66.6 | 72.0 | 68.9 | 70.2 |
| 1 | 63.2 | 67.9 | 70.9 | 66.6 | 76.1 | 70.8 | 72.0 |
| 2 | 45.2 | 46.9 | 60.5 | 58.7 | 66.5 | 65.9 | 66.8 |
| 3 | 29.8 | 41.8 | 53.0 | 51.7 | 58.5 | 58.1 | 59.0 |
| 4 | 61.5 | 61.2 | 69.8 | 69.3 | 77.4 | 77.9 | 78.5 |
| EMP (AVG.) | 37.6 | 44.9 | 49.5 | 58.1 | 56.0 | 66.0 | 67.5 |
| H3 | 61.5 | 67.2 | 74.2 | 78.8 | 78.3 | 80.2 | 81.0 |
| H3K14AC | 29.7 | 32.0 | 42.1 | 56.2 | 52.6 | 64.9 | 66.0 |
| H3K36ME3 | 38.6 | 48.3 | 48.5 | 62.0 | 56.9 | 66.7 | 67.8 |
| H3K4ME1 | 26.1 | 35.8 | 43.0 | 55.3 | 50.5 | 55.3 | 56.1 |
| H3K4ME2 | 25.8 | 25.8 | 31.3 | 36.5 | 31.1 | 51.2 | 52.3 |
| H3K4ME3 | 20.5 | 23.1 | 28.9 | 40.3 | 36.3 | 58.5 | 59.5 |
| H3K79ME3 | 46.3 | 54.1 | 60.1 | 64.7 | 67.4 | 73.0 | 74.1 |
| H3K9AC | 40.0 | 50.8 | 50.5 | 56.0 | 55.6 | 65.5 | 66.5 |
| H4 | 62.3 | 73.7 | 78.3 | 81.7 | 80.7 | 82.7 | 83.5 |
| H4AC | 25.5 | 38.4 | 38.6 | 49.1 | 50.4 | 61.7 | 62.8 |
| PD (AVG.) | 77.1 | 35.0 | 84.6 | 88.1 | 84.2 | 82.3 | 85.5 |
| ALL | 75.8 | 47.4 | 90.4 | 91.0 | 86.8 | 86.0 | 88.5 |
| NO-TATA | 85.1 | 52.2 | 93.6 | 94.0 | 94.3 | 93.7 | 94.5 |
| TATA | 70.3 | 5.3 | 69.8 | 79.4 | 71.6 | 67.4 | 73.5 |
| CPD (AVG.) | 62.5 | 48.4 | 73.0 | 71.6 | 70.5 | 69.9 | 71.2 |
| ALL | 58.1 | 37.0 | 70.9 | 70.3 | 69.4 | 66.4 | 68.0 |
| NO-TATA | 60.1 | 35.4 | 69.8 | 71.6 | 68.0 | 68.3 | 69.5 |
| TATA | 69.3 | 72.9 | 78.2 | 73.0 | 74.2 | 75.1 | 76.3 |
| SSD | 76.8 | 72.7 | 84.1 | 89.3 | 85.0 | 87.8 | 89.5 |
| COVID (F1) | 22.2 | 23.3 | 62.2 | 73.0 | 71.9 | 72.5 | 73.3 |
| GLOBAL WIN % | 0.0 | 0.0 | 7.1 | 21.4 | 25.0 | 46.4 | 57.1 |

### G.5 Ablation Studies and Additional Experiments

#### G.5.1 RL Algorithm Ablation

Table 13: Ablation across RL algorithms with training time (GPU-h), inference time (ms/seq), and vocabulary Jaccard similarity vs. PPO.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Domain | Config (Metric) | Metric Value | Train Time (GPU-h) | Inference (ms/seq) | Vocab Jaccard |
| Genomics | QA-Token (PPO) | 0.891 | 34.0 | 10.2 | 1.00 |
|  | QA-Token (GRPO) | 0.890 | 32.5 | 10.3 | 0.98 |
|  | QA-Token (VAPO) | 0.892 | 31.8 | 10.2 | 0.97 |
|  | QA-Token (DAPO) | 0.889 | 34.2 | 10.4 | 0.98 |
| Finance | QA-Token (PPO) | 1.72 | 28.0 | 15.2 | 1.00 |
|  | QA-Token (GRPO) | 1.71 | 26.5 | 15.3 | 0.96 |
|  | QA-Token (VAPO) | 1.73 | 25.0 | 15.1 | 0.95 |
|  | QA-Token (DAPO) | 1.70 | 28.5 | 15.2 | 0.96 |
| Social | QA-Token (PPO) | 74.5 | 30.0 | 12.5 | 1.00 |
|  | QA-Token (GRPO) | 74.2 | 29.0 | 12.6 | 0.97 |
|  | QA-Token (VAPO) | 74.6 | 28.0 | 12.5 | 0.98 |
|  | QA-Token (DAPO) | 74.3 | 31.0 | 12.7 | 0.97 |

We assess the sensitivity of QA-Token to the choice of RL optimizer by replacing PPO with GRPO and VAPO (implementations following (Shao et al., [2024](https://arxiv.org/html/2602.06394v1#bib.bib87 "DeepSeekMath: pushing the limits of mathematical reasoning in open language models"); Yue and others, [2025](https://arxiv.org/html/2602.06394v1#bib.bib88 "Does reinforcement learning really incentivize reasoning capacity in LLMs beyond the base model?"))). Across domains, downstream performance is stable and vocabulary similarity remains high (Jaccard ≥\geq 0.95), confirming modularity of the framework.

### G.6 Data Curation Baseline: BPE on Clean Data vs. QA-Token on Noisy Data

A natural question is whether simply filtering to high-quality data and using standard BPE could match QA-Token’s performance. We evaluate this data curation baseline by training BPE on only the top 20% highest-quality sequences (average Phred score ≥30\geq 30) and comparing against QA-Token trained on the full noisy corpus.

Table 14: Data Curation Baseline Comparison (Genomics Variant Calling). QA-Token on noisy data outperforms BPE on curated clean data.

|  |  |  |  |
| --- | --- | --- | --- |
| Method | Training Data | Variant F1 | p-value |
| BPE (full corpus) | 100% (noisy) | 0.824±0.0040.824\pm 0.004 | <0.001<0.001 |
| BPE (top 20% clean) | 20% (Q≥\geq30) | 0.847±0.0050.847\pm 0.005 | <0.001<0.001 |
| QA-Token | 100% (noisy) | 0.891±0.004\mathbf{0.891\pm 0.004} | — |

Key findings:

* •

  Data curation (BPE on clean data) improves over BPE on full noisy data: +2.8%+2.8\% F1 (0.8470.847 vs 0.8240.824).
* •

  However, QA-Token on the *full noisy corpus* outperforms BPE on clean data by +5.2%+5.2\% F1 (0.8910.891 vs 0.8470.847, p<0.001p<0.001).
* •

  This demonstrates that quality-aware tokenization extracts more value from noisy data than discarding it entirely.

### G.7 Genomics: Real-World Datasets (ONT, UHGG)

Datasets: (i) GIAB HG002 long-read ONT data (high-error, third-generation); (ii) Unified Human Gut Genome (UHGG) collection (large-scale, low-error NGS).

Results: QA-BPE-seq consistently outperforms baselines across both regimes. ONT (high-error) results:

Table 15: ONT (GIAB HG002) results. Means with 95% confidence intervals over n=10n=10 runs.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Method | Variant F1 | Taxa Acc. F1 | Recon. Loss | Inf. Time (ms/seq) |
| Standard BPE | 0.795 ±\pm 0.006 | 0.812 ±\pm 0.007 | 0.388 ±\pm 0.012 | 11.5 ±\pm 0.3 |
| SentencePiece | 0.801 ±\pm 0.005 | 0.825 ±\pm 0.006 | 0.371 ±\pm 0.011 | 11.6 ±\pm 0.4 |
| WordPiece | 0.798 ±\pm 0.006 | 0.819 ±\pm 0.007 | 0.379 ±\pm 0.013 | 11.5 ±\pm 0.3 |
| DNABERT-k (6-mer) | 0.823 ±\pm 0.004 | 0.846 ±\pm 0.005 | 0.352 ±\pm 0.010 | 11.2 ±\pm 0.3 |
| QA-BPE-seq (100%) | 0.864 ±\pm 0.005 | 0.881 ±\pm 0.004 | 0.305 ±\pm 0.009 | 11.8 ±\pm 0.4 |
| *QA-BPE-seq (70%)* | 0.830 ±\pm 0.005 | 0.845 ±\pm 0.004 | 0.345 ±\pm 0.009 | 11.9 ±\pm 0.4 |
| *QA-BPE-seq (50%)* | 0.795 ±\pm 0.006 | 0.810 ±\pm 0.005 | 0.380 ±\pm 0.010 | 12.0 ±\pm 0.4 |
| *QA-BPE-seq (30%)* | 0.750 ±\pm 0.006 | 0.760 ±\pm 0.005 | 0.420 ±\pm 0.011 | 12.1 ±\pm 0.5 |

NGS (UHGG) results:

Table 16: UHGG (NGS) results. Means with 95% confidence intervals over n=10n=10 runs.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Method | Variant F1 | Taxa Acc. F1 | Recon. Loss | Inf. Time (ms/seq) |
| Standard BPE | 0.852 ±\pm 0.003 | 0.881 ±\pm 0.004 | 0.295 ±\pm 0.008 | 9.8 ±\pm 0.2 |
| SentencePiece | 0.860 ±\pm 0.003 | 0.893 ±\pm 0.004 | 0.280 ±\pm 0.007 | 9.9 ±\pm 0.2 |
| WordPiece | 0.855 ±\pm 0.004 | 0.887 ±\pm 0.005 | 0.286 ±\pm 0.009 | 9.8 ±\pm 0.3 |
| DNABERT-k (6-mer) | 0.875 ±\pm 0.002 | 0.908 ±\pm 0.003 | 0.264 ±\pm 0.006 | 9.5 ±\pm 0.2 |
| QA-BPE-seq (100%) | 0.915 ±\pm 0.003 | 0.935 ±\pm 0.003 | 0.221 ±\pm 0.005 | 10.1 ±\pm 0.3 |
| *QA-BPE-seq (70%)* | 0.878 ±\pm 0.004 | 0.898 ±\pm 0.004 | 0.250 ±\pm 0.007 | 10.2 ±\pm 0.3 |
| *QA-BPE-seq (50%)* | 0.842 ±\pm 0.005 | 0.860 ±\pm 0.005 | 0.276 ±\pm 0.008 | 10.3 ±\pm 0.3 |
| *QA-BPE-seq (30%)* | 0.790 ±\pm 0.006 | 0.805 ±\pm 0.006 | 0.310 ±\pm 0.009 | 10.5 ±\pm 0.4 |

### G.8 Finance: High-Frequency Equities (AAPL)

Dataset and Setup: High-frequency LOB data for AAPL from LOBSTER.

Results: QAT-QF scales to equities, improving predictive and trading metrics over baselines.

Table 17: AAPL high-frequency results. Means with 95% confidence intervals over n=10n=10 runs.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | Ret. Pred. (%) | Vol. RMSE | Regime Acc. (%) | Sharpe | Inf. Time (ms/seq) |
| Standard BPE | 63.1 ±\pm 0.6 | 0.0125 ±\pm 0.0004 | 75.8 ±\pm 0.7 | 1.41 ±\pm 0.06 | 14.8 ±\pm 0.4 |
| SAX | 61.5 ±\pm 0.7 | 0.0121 ±\pm 0.0005 | 77.0 ±\pm 0.6 | 1.38 ±\pm 0.07 | 14.2 ±\pm 0.3 |
| BOSS | 64.0 ±\pm 0.5 | 0.0113 ±\pm 0.0004 | 80.1 ±\pm 0.5 | 1.53 ±\pm 0.06 | 14.5 ±\pm 0.4 |
| QAT-QF | 69.8 ±\pm 0.5 | 0.0085 ±\pm 0.0003 | 87.9 ±\pm 0.4 | 1.81 ±\pm 0.08 | 15.0 ±\pm 0.5 |

### G.9 Finance: Rolling-Window Temporal Robustness (BTC/USD, Full Year 2023)

To demonstrate temporal robustness beyond a single quarter, we extend our BTC/USD evaluation across all four quarters of 2023 using a strict rolling-window protocol. For each quarter, the vocabulary and downstream models are trained only on data preceding that quarter.

Table 18: Rolling-window out-of-sample Sharpe ratios for BTC/USD across 2023. Each quarter uses models trained strictly on preceding data. Means with 95% confidence intervals over n=10n=10 runs.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Quarter | QAT-QF Sharpe | BPE Sharpe | Δ\Delta (%) | Market Context |
| Q1 2023 | 1.72 ±\pm 0.07 | 1.32 ±\pm 0.05 | +30.3 | Recovery phase |
| Q2 2023 | 1.58 ±\pm 0.09 | 1.21 ±\pm 0.06 | +30.6 | Consolidation |
| Q3 2023 | 1.45 ±\pm 0.08 | 1.15 ±\pm 0.07 | +26.1 | High volatility |
| Q4 2023 | 1.68 ±\pm 0.10 | 1.29 ±\pm 0.06 | +30.2 | Bull market |
| Average | 1.61 | 1.24 | +29.8 | — |

Key Observations: (i) QAT-QF maintains consistent improvements (+26–31%) across all market regimes. (ii) Q3 2023 exhibited elevated volatility (VIX-equivalent spike); QAT-QF gains persist (+26.1%), demonstrating cross-regime robustness. (iii) The consistency across four quarters with varying market conditions validates generalization beyond a single test period.

## Appendix H Domain-Specific Instantiations

We now detail the instantiation of the QA-Token framework for three distinct domains: genomic sequencing, social media text, and quantitative finance. Detailed pseudocode algorithms for each domain are provided in Section [H.9](https://arxiv.org/html/2602.06394v1#A8.SS9 "H.9 Domain-Specific Algorithms ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

### H.1 Genomics (QA-BPE-seq)

Context: This instantiation targets the analysis of DNA or RNA sequencing reads, which are often affected by base-calling errors, for applications such as genetic variant calling, taxonomic classification, or sequence modeling.
Atomic Elements & Quality: The base alphabet is Σ={A, C, G, T/U, N}\Sigma=\{\text{A, C, G, T/U, N}\}. The primary quality information for each atomic base sis\_{i} comes from Phred scores Qphred,iQ\_{\text{phred},i}. The error probability is Perror​(i)=10−Qphred,i/10P\_{\text{error}}(i)=10^{-Q\_{\text{phred},i}/10}, leading to an atomic quality score qi=1−Perror​(i)q\_{i}=1-P\_{\text{error}}(i). To model read end quality degradation, for a base at position ii (0-indexed) in a read of length LL, the position-adjusted quality is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi′=qi⋅exp⁡(−βpos⋅|i−(L−1)/2|(L−1)/2+ϵl​e​n)q^{\prime}\_{i}=q\_{i}\cdot\exp\left(-\beta\_{\text{pos}}\cdot\frac{|i-(L-1)/2|}{(L-1)/2+\epsilon\_{len}}\right) |  | (41) |

where βpos≥0\beta\_{\text{pos}}\geq 0 is a learnable parameter in θadapt\theta\_{\text{adapt}}.
Token Quality (qtq\_{t}): For a token t=s1​…​s|t|t=s\_{1}...s\_{|t|}, we use the geometric mean of the position-adjusted atomic qualities to compute its aggregated scalar quality: qt=(∏j=1|t|qsj′)1/|t|q\_{t}=(\prod\_{j=1}^{|t|}q^{\prime}\_{s\_{j}})^{1/|t|}. The geometric mean is sensitive to low-quality bases. This qtq\_{t} is used for the constituent qualities qaq\_{a} and qbq\_{b} in the merge score (Eq. [5](https://arxiv.org/html/2602.06394v1#A3.E5 "Equation 5 ‣ Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
Merge Score (wa​bw\_{ab}): The score is calculated using Equation [5](https://arxiv.org/html/2602.06394v1#A3.E5 "Equation 5 ‣ Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), with the geometric mean qualities qa,qbq\_{a},q\_{b}, the learnable parameter α∈θadapt\alpha\in\theta\_{\text{adapt}}, and ψ​(a,b)=1\psi(a,b)=1.
Reward Components (RgenomicR\_{\text{genomic}}): The overall reward (Eq. [26](https://arxiv.org/html/2602.06394v1#A5.E26 "Equation 26 ‣ E.1.2 Reward Function Design ‣ E.1 Stage 1: Reinforcement Learning Policy Optimization ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) uses weights λj∈θadapt\lambda\_{j}\in\theta\_{\text{adapt}}. Specific raw components RrawR^{\text{raw}} include:

* •

  RQraw​(a,b)R^{\text{raw}}\_{Q}(a,b): Quality of the newly formed token ta​bt\_{ab}. This is its geometric mean quality: RQraw​(a,b)=qa​b=(∏l=1|a|+|b|qsa​b,l′)1/(|a|+|b|)R^{\text{raw}}\_{Q}(a,b)=q\_{ab}=(\prod\_{l=1}^{|a|+|b|}q^{\prime}\_{s\_{ab,l}})^{1/(|a|+|b|)}.
* •

  RIraw​(a,b)R^{\text{raw}}\_{I}(a,b): Log-ratio of probabilities: RIraw​(a,b)=log⁡P​(ta​b)P​(a)​P​(b)+ϵpR^{\text{raw}}\_{I}(a,b)=\log\frac{P(t\_{ab})}{P(a)P(b)+\epsilon\_{p}}.
* •

  RCraw​(a,b)R^{\text{raw}}\_{C}(a,b): Complexity penalty: RCraw​(a,b)=−|ta​b|R^{\text{raw}}\_{C}(a,b)=-|t\_{ab}|.
* •

  Rb​i​orawR^{\text{raw}}\_{bio} (Optional): A domain-specific reward based on overlap with known genomic features (e.g., genes, regulatory elements from databases like dbSNP (Sherry et al., [2001](https://arxiv.org/html/2602.06394v1#bib.bib46 "DbSNP: the ncbi database of genetic variation"))).

Raw components are normalized using the adaptive EMA method (Eq. [35](https://arxiv.org/html/2602.06394v1#A5.E35 "Equation 35 ‣ E.8 Reward Normalization Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
Adaptive Parameters (θadapt\theta\_{\text{adapt}}): Includes α\alpha, βpos\beta\_{\text{pos}}, reward weights λj\lambda\_{j}, and potentially parameters for soft frequency/quality gating.
Algorithm: The two-stage learning process (Section [E](https://arxiv.org/html/2602.06394v1#A5 "Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) is applied. An RL policy is optimized (Algorithm [1](https://arxiv.org/html/2602.06394v1#alg1 "Algorithm 1 ‣ E.1.3 PPO Training Algorithm ‣ E.1 Stage 1: Reinforcement Learning Policy Optimization ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), and then the adaptive parameters θa​d​a​p​t\theta\_{adapt} are learned (Algorithm [2](https://arxiv.org/html/2602.06394v1#alg2 "Algorithm 2 ‣ E.2.2 Gumbel-Softmax Differentiable Optimization ‣ E.2 Stage 2: Adaptive Parameter Learning ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) by optimizing a downstream task objective.

### H.2 Quantitative Finance (QAT-QF)

Context: This instantiation focuses on analyzing noisy, non-stationary high-frequency financial data for tasks like forecasting price movements or developing trading strategies.
Atomic Elements & Quality: Atomic elements sis\_{i} are discretized events from high-frequency data (e.g., fixed-length segments of LOB events). Each atomic element sis\_{i} is assigned a scalar quality score qi=∑kwk​qk,iq\_{i}=\sum\_{k}w\_{k}q\_{k,i}, where qk,iq\_{k,i} are normalized quality components (e.g., qsnr,qliqq\_{\text{snr}},q\_{\text{liq}}) and wkw\_{k} are learnable weights in θadapt\theta\_{\text{adapt}}.
Token Quality (qtq\_{t}): For a token tt composed of atomic elements {si}i∈t\{s\_{i}\}\_{i\in t}, the aggregated scalar quality is the arithmetic mean: qt=1|t|​∑i∈tqiq\_{t}=\frac{1}{|t|}\sum\_{i\in t}q\_{i}. This is used for qa,qbq\_{a},q\_{b} in the merge score.
Merge Score (wa​bw\_{ab}): Calculated using Equation [5](https://arxiv.org/html/2602.06394v1#A3.E5 "Equation 5 ‣ Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), with qa,qbq\_{a},q\_{b}, learnable α∈θadapt\alpha\in\theta\_{\text{adapt}}, and ψ​(a,b)=1\psi(a,b)=1.
Market Regimes: An identified regime indicator can condition the RL policy and reward components.
Reward Components (RfinanceR\_{\text{finance}}): Raw components RrawR^{\text{raw}} are normalized using the adaptive EMA method.

* •

  RQraw​(a,b)R^{\text{raw}}\_{Q}(a,b): Length-weighted average quality: RQraw​(a,b)=|a|​qa+|b|​qb|a|+|b|R^{\text{raw}}\_{Q}(a,b)=\frac{|a|q\_{a}+|b|q\_{b}}{|a|+|b|}.
* •

  RIraw​(a,b)R^{\text{raw}}\_{I}(a,b): Information reward blended across regimes: RIraw​(a,b)=γregime⋅Inormal​(a,b)+(1−γregime)⋅Istress​(a,b)R^{\text{raw}}\_{I}(a,b)=\gamma\_{\text{regime}}\cdot I\_{\text{normal}}(a,b)+(1-\gamma\_{\text{regime}})\cdot I\_{\text{stress}}(a,b), where Iregime=log⁡P​(ta​b|regime)P​(a|regime)​P​(b|regime)+ϵpI\_{\text{regime}}=\log\frac{P(t\_{ab}|\text{regime})}{P(a|\text{regime})P(b|\text{regime})+\epsilon\_{p}}. The blending factor γregime\gamma\_{\text{regime}} is a learnable parameter in θadapt\theta\_{\text{adapt}}.
* •

  RPraw​(a,b)R^{\text{raw}}\_{P}(a,b): Predictive Power (Mutual Information with future returns):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | RPraw​(a,b)=MI​(ta​b,Disc​(Rτ))NormFactorM​I+ϵM​IR^{\text{raw}}\_{P}(a,b)=\frac{\text{MI}(t\_{ab},\text{Disc}(R\_{\tau}))}{\text{NormFactor}\_{MI}+\epsilon\_{MI}} |  | (42) |

  Disc​(Rτ)\text{Disc}(R\_{\tau}) is discretized future return. NormFactorM​I\text{NormFactor}\_{MI} is an adaptive normalization factor.
* •

  RCraw​(a,b)R^{\text{raw}}\_{C}(a,b): Complexity penalty with volatility scaling:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | RCraw​(a,b)=−(|ta​b|⋅log⁡(|Vk|+1)⋅VolScale)R^{\text{raw}}\_{C}(a,b)=-\left(|t\_{ab}|\cdot\log(|V\_{k}|+1)\cdot\text{VolScale}\right) |  | (43) |

  where VolScale depends on a learnable parameter βvol∈θadapt\beta\_{\text{vol}}\in\theta\_{\text{adapt}}.

Adaptive Parameters (θadapt\theta\_{\text{adapt}}): Includes α\alpha, quality component weights wkw\_{k}, βvol\beta\_{\text{vol}}, γregime\gamma\_{\text{regime}}, and reward weights λj\lambda\_{j}.
Algorithm: The two-stage learning process is applied as in the genomics domain.

### H.3 Social Media Text (QA-BPE-nlp)

Context: This instantiation addresses the challenges of processing noisy user-generated text for tasks such as sentiment analysis or NER.
Atomic Elements & Quality: The base alphabet consists of characters. Quality for a token tt is modeled using a multi-dimensional vector 𝒒t=(qorth​(t),qsem​(t),…)\bm{q}\_{t}=(q\_{\text{orth}}(t),q\_{\text{sem}}(t),\dots) detailed in Appendix [D.3](https://arxiv.org/html/2602.06394v1#A4.SS3 "D.3 Social Media: Linguistic Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"). The aggregated scalar quality is qt=∑jwj​𝒒t,jq\_{t}=\sum\_{j}w\_{j}\bm{q}\_{t,j}, where wj≥0w\_{j}\geq 0 are learnable weights in θadapt\theta\_{\text{adapt}}.
Token Quality (qtq\_{t}): The aggregated score qtq\_{t} is used for qa,qbq\_{a},q\_{b} in the merge score.
Merge Score (wa​bw\_{ab}): Calculated using Equation [5](https://arxiv.org/html/2602.06394v1#A3.E5 "Equation 5 ‣ Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") with qa,qbq\_{a},q\_{b}, learnable α∈θadapt\alpha\in\theta\_{\text{adapt}}, and a semantic compatibility factor ψ​(a,b)\psi(a,b):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(a,b)=exp⁡(βs​e​m⋅cosine​(𝒗a,𝒗b))\psi(a,b)=\exp(\beta\_{sem}\cdot\text{cosine}(\bm{v}\_{a},\bm{v}\_{b})) |  | (44) |

where 𝒗a,𝒗b\bm{v}\_{a},\bm{v}\_{b} are pre-trained embeddings and βs​e​m≥0\beta\_{sem}\geq 0 is a learnable parameter in θadapt\theta\_{\text{adapt}}.
Noise Models: Probabilistic models P​(t′|t)P(t^{\prime}|t) capturing likely variations inform the noise robustness reward RNR\_{N}.
Reward Components (RsocialR\_{\text{social}}): Raw components are normalized before being weighted by λj\lambda\_{j}.

* •

  RQraw​(a,b)R^{\text{raw}}\_{Q}(a,b): Blend of compositional and direct quality: RQraw​(a,b)=ω​|a|​qa+|b|​qb|a|+|b|+(1−ω)​qa​bR^{\text{raw}}\_{Q}(a,b)=\omega\frac{|a|q\_{a}+|b|q\_{b}}{|a|+|b|}+(1-\omega)q\_{ab}, with learnable blending weight ω∈[0,1]\omega\in[0,1].
* •

  RSraw​(a,b)R^{\text{raw}}\_{S}(a,b): Semantic Coherence: PMI​(a,b)⋅cosine\_similarity​(𝒗a,𝒗b)\text{PMI}(a,b)\cdot\text{cosine\\_similarity}(\bm{v}\_{a},\bm{v}\_{b}).
* •

  RNraw​(a,b)R^{\text{raw}}\_{N}(a,b): Noise Robustness: Rnoise​(ta​b)−|a|​Rnoise​(a)+|b|​Rnoise​(b)|a|+|b|R\_{\text{noise}}(t\_{ab})-\frac{|a|R\_{\text{noise}}(a)+|b|R\_{\text{noise}}(b)}{|a|+|b|}, based on the noise model.
* •

  RCraw​(a,b)R^{\text{raw}}\_{C}(a,b): Complexity penalty: RCraw​(a,b)=−|ta​b|R^{\text{raw}}\_{C}(a,b)=-|t\_{ab}|.
* •

  RVraw​(a,b)R^{\text{raw}}\_{V}(a,b): Vocabulary Efficiency: log⁡(1+f​(ta​b))|ta​b|\frac{\log(1+f(t\_{ab}))}{|t\_{ab}|}.

Adaptive Parameters (θadapt\theta\_{\text{adapt}}): Includes α,βs​e​m\alpha,\beta\_{sem}, quality dimension weights wjw\_{j}, reward weights λj\lambda\_{j}, and the blending weight ω\omega.
Algorithm: The two-stage learning process is applied as in the other domains.

### H.4 Financial Experimental Methodology Details

All trading simulations and return prediction evaluations for the quantitative finance domain (Section [5.2](https://arxiv.org/html/2602.06394v1#S5.SS2 "5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) were conducted with rigorous attention to backtesting best practices to ensure the validity of results and avoid common pitfalls.

* •

  Walk-Forward Validation: A strict walk-forward validation scheme was employed. The dataset was divided into chronological segments. For each segment kk, the model (including the QA-Token vocabulary construction and downstream predictive/trading model) was trained on data up to the start of segment kk, validated on segment k−1k-1 (or a dedicated validation portion of the training data), and then tested out-of-sample only on segment kk. The training window was then rolled forward to include segment kk for training before testing on segment k+1k+1. This process ensures that the model is always tested on data not seen during its training or hyperparameter tuning phases for that specific test period.
* •

  Lookahead Bias Prevention: Extreme care was taken to prevent any form of lookahead bias. All features, quality scores, token definitions, and trading decisions at any time tt were based strictly on information available up to and including time t−1t-1. Future return labels (Rt+τR\_{t+\tau}) used for training predictive models or as part of the RPR\_{P} reward component were sourced from periods strictly after the information used for input features and token construction.
* •

  Test Set and Data Splitting: The overall dataset (BTC/USD LOB data, Q1 2023) was split chronologically: 70% for the initial training pool, 15% for validation (used for hyperparameter tuning of downstream models and early stopping), and the final 15% (approximately 2 weeks of 1-minute data) as the ultimate out-of-sample test set for reporting final performance metrics like Sharpe Ratio and prediction accuracy. This test set was held out and used only once after all model development and tuning.
* •

  Transaction Costs: A realistic transaction cost of 5 basis points (0.05%) per trade was applied to simulate market friction. This cost was deducted for both buying and selling actions in the trading simulations.
* •

  PPO Trading Agent Details: The PPO-based trading agent used a 2-layer MLP policy network and a separate 2-layer MLP value network, each with 128 hidden units and ReLU activation functions. The input to these networks consisted of a sequence of recent token embeddings (generated by QAT-QF or baseline tokenizers from the LOB data) and the agent’s current market position (long, short, or flat). The agent’s action space was discrete (buy, sell, hold). The reward function for the PPO agent was the realized profit and loss (PnL) from its trades over a short horizon, adjusted for transaction costs. Standard PPO hyperparameters were used, including a clipping parameter ϵ=0.2\epsilon=0.2, GAE λ=0.95\lambda=0.95, and an entropy bonus for exploration. The PPO agent was re-trained periodically within the walk-forward scheme.
* •

  Details for RPrawR^{\text{raw}}\_{P} Reward (Eq. [42](https://arxiv.org/html/2602.06394v1#A8.E42 "Equation 42 ‣ 3rd item ‣ H.2 Quantitative Finance (QAT-QF) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")): The parameter MM​IM\_{MI} (window for NormFactorM​I\text{NormFactor}\_{MI}) was set to 1000 merge steps in our experiments. The future return RτR\_{\tau} was for τ=5\tau=5 minutes ahead and discretized into 3 bins (negative, neutral, positive) based on empirical quantiles from the training data.

### H.5 Detailed Reward Components

The general structure of the reward R​(a,b)R(a,b) for merging tokens aa and bb into tm​e​r​g​e​d=a||bt\_{merged}=a||b is:
R​(a,b)=∑jλj​R^j​(a,b)R(a,b)=\sum\_{j}\lambda\_{j}\hat{R}\_{j}(a,b), where R^j\hat{R}\_{j} are adaptively normalized components (see Section [4.2](https://arxiv.org/html/2602.06394v1#S4.SS2 "4.2 Reward Function Design ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). The weights λj≥0\lambda\_{j}\geq 0 (parameterized via 𝜷λj\bm{\beta}\_{\lambda\_{j}} and softmax) are part of θa​d​a​p​t\theta\_{adapt}.

### H.6 Common Components

* •

  RQraw​(a,b)R^{\text{raw}}\_{Q}(a,b): Raw Quality reward. This component incentivizes merges that result in high-quality tokens. A common formulation for the raw component is the length-weighted arithmetic mean of the qualities of the constituent tokens aa and bb:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | RQraw​(a,b)=|a|​qa+|b|​qb|a|+|b|R^{\text{raw}}\_{Q}(a,b)=\frac{|a|q\_{a}+|b|q\_{b}}{|a|+|b|} |  | (45) |

  where qa,qbq\_{a},q\_{b} are the quality scores of tokens a,ba,b respectively, and |a|,|b||a|,|b| are their lengths.
  For Social Media, a blended approach might be used for RQraw​(a,b)R^{\text{raw}}\_{Q}(a,b):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | RQraw(a,b)=ω(|a|​Qa​g​g​(a)+|b|​Qa​g​g​(b)|a|+|b|)+(1−ω)Qa​g​g(a||b)R^{\text{raw}}\_{Q}(a,b)=\omega\left(\frac{|a|Q\_{agg}(a)+|b|Q\_{agg}(b)}{|a|+|b|}\right)+(1-\omega)Q\_{agg}(a||b) |  | (46) |

  where Qa​g​g​(t)Q\_{agg}(t) is the aggregate quality score for token tt (from Section [D.3](https://arxiv.org/html/2602.06394v1#A4.SS3 "D.3 Social Media: Linguistic Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) and ω∈[0,1]\omega\in[0,1] is a learnable blending weight in θa​d​a​p​t\theta\_{adapt}.
* •

  RIraw​(a,b)R^{\text{raw}}\_{I}(a,b): Raw Information gain. This rewards merges that are statistically significant. A common formulation:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | RIraw​(a,b)=log⁡f​(tm​e​r​g​e​d)f​(a)​f​(b)+ϵfR^{\text{raw}}\_{I}(a,b)=\log\frac{f(t\_{merged})}{f(a)f(b)+\epsilon\_{f}} |  | (47) |

  where f​(⋅)f(\cdot) denotes frequency and ϵf>0\epsilon\_{f}>0 (e.g., 10−810^{-8}) is for stability.
  For Finance, this can be blended based on market regime: RIraw​(a,b)=γregime​Inormal+(1−γregime)​IstressR^{\text{raw}}\_{I}(a,b)=\gamma\_{\text{regime}}I\_{\text{normal}}+(1-\gamma\_{\text{regime}})I\_{\text{stress}}, where Iregime=log⁡f​(tm​e​r​g​e​d|M=regime)f​(a|M=regime)​f​(b|M=regime)+ϵfI\_{\text{regime}}=\log\frac{f(t\_{merged}|M=\text{regime})}{f(a|M=\text{regime})f(b|M=\text{regime})+\epsilon\_{f}}. γregime∈[0,1]\gamma\_{\text{regime}}\in[0,1] is a learnable parameter in θa​d​a​p​t\theta\_{adapt}.
* •

  RCraw​(a,b)R^{\text{raw}}\_{C}(a,b): Raw Complexity penalty. This penalizes overly complex vocabularies and is typically negative. A common formulation:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | RCraw​(a,b)=−len​(tm​e​r​g​e​d)⋅log⁡(|Vt|+1)⋅[ScalingFactor]R^{\text{raw}}\_{C}(a,b)=-\text{len}(t\_{merged})\cdot\log(|V\_{t}|+1)\cdot[\text{ScalingFactor}] |  | (48) |

  For Finance, the ScalingFactor can incorporate market volatility using βv​o​l∈θa​d​a​p​t\beta\_{vol}\in\theta\_{adapt} as per Equation [43](https://arxiv.org/html/2602.06394v1#A8.E43 "Equation 43 ‣ 4th item ‣ H.2 Quantitative Finance (QAT-QF) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

### H.7 Domain-Specific Components

* •

  Genomics: Rb​i​oraw​(a,b)=ScoreOverlap​(tm​e​r​g​e​d,KnownBiologicalFeatures)R^{\text{raw}}\_{bio}(a,b)=\text{Score}\_{\text{Overlap}}(t\_{merged},\text{KnownBiologicalFeatures}). A positive reward if tm​e​r​g​e​dt\_{merged} significantly overlaps with known biological features (e.g., genes from GENCODE (Harrow et al., [2012](https://arxiv.org/html/2602.06394v1#bib.bib77 "GENCODE: the reference human genome annotation for the encode project")), variants from dbSNP (Sherry et al., [2001](https://arxiv.org/html/2602.06394v1#bib.bib46 "DbSNP: the ncbi database of genetic variation"))). The overlap score was calculated as the Jaccard index between the character span of the merged token tm​e​r​g​e​dt\_{merged} and the character span of known genomic features. A higher Jaccard index, indicating greater overlap, results in a higher reward.
* •

  Finance:

  + –

    RPraw​(a,b)R^{\text{raw}}\_{P}(a,b): Predictive Power:

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | RPraw​(a,b)=MI​(tmerged;Disc​(Rτ))NormFactorM​I+ϵM​IR^{\text{raw}}\_{P}(a,b)=\frac{\text{MI}(t\_{\text{merged}};\text{Disc}(R\_{\tau}))}{\text{NormFactor}\_{MI}+\epsilon\_{MI}} |  | (49) |

    Uses Mutual Information (MI) MI​(X;Y)=∑x∈X,y∈Yp​(x,y)​log⁡p​(x,y)p​(x)​p​(y)\text{MI}(X;Y)=\sum\_{x\in X,y\in Y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}. RτR\_{\tau} is the discretized future return (e.g., 3 bins for τ=5\tau=5 min based on empirical quantiles from the training data). NormFactorM​I\text{NormFactor}\_{MI} is the adaptively calculated 95th percentile of MI values from candidate pairs over the last MM​IM\_{MI} (e.g., 1000) merge steps within the current RL episode. ϵM​I>0\epsilon\_{MI}>0 (e.g., 10−810^{-8}). While this adaptive normalization of MI introduces a degree of non-stationarity to the RPR\_{P} reward component within an RL episode, it was found that standard PPO training handled this adequately. The responsiveness of the reward to the informativeness of newly forming tokens was deemed beneficial, and the MM​IM\_{MI} window provides some smoothing. Alternatives using a fixed normalization factor (e.g., derived from an initial global scan of MI values) were found to be less responsive to the changing characteristics of tokens as the vocabulary evolved during the RL episode.
* •

  Social Media:

  + –

    RSraw​(a,b)R^{\text{raw}}\_{S}(a,b): Semantic Coherence: PMI​(a,b)⋅cosine\_similarity​(𝒗a,𝒗b)\text{PMI}(a,b)\cdot\text{cosine\\_similarity}(\bm{v}\_{a},\bm{v}\_{b}). Pre-trained embeddings 𝒗a,𝒗b\bm{v}\_{a},\bm{v}\_{b} (e.g., fastText (Bojanowski et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib62 "Enriching word vectors with subword information"))).
  + –

    RNraw​(a,b)R^{\text{raw}}\_{N}(a,b): Noise Robustness:

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | (Rnoise​(tmerged)−|a|​Rnoise​(a)+|b|​Rnoise​(b)|a|+|b|),\left(R\_{\text{noise}}(t\_{\text{merged}})-\frac{|a|R\_{\text{noise}}(a)+|b|R\_{\text{noise}}(b)}{|a|+|b|}\right), |  | (50) |

    where Rn​o​i​s​e​(t)=1−𝔼t′∼P(⋅|t)​[normalized\_edit\_distance​(t,t′)]R\_{noise}(t)=1-\mathbb{E}\_{t^{\prime}\sim P(\cdot|t)}[\text{normalized\\_edit\\_distance}(t,t^{\prime})] based on noise model P​(t′|t)P(t^{\prime}|t) (Appendix [H.8](https://arxiv.org/html/2602.06394v1#A8.SS8 "H.8 Further Details on Social Media Noise Models ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
  + –

    RVraw​(a,b)R^{\text{raw}}\_{V}(a,b): Vocabulary Efficiency: log⁡(1+f​(tmerged))|tmerged|\frac{\log(1+f(t\_{\text{merged}}))}{|t\_{\text{merged}}|}.

### H.8 Further Details on Social Media Noise Models

Formalizing linguistic noise for social media text involves defining probabilistic transformations P​(t′|t)P(t^{\prime}|t) from a canonical form tt to an observed variant t′t^{\prime} (Han et al., [2013](https://arxiv.org/html/2602.06394v1#bib.bib18 "Lexical normalisation of short text messages: makn sens a #twitter")). These models inform the noise robustness measure Rnoise​(t)R\_{\text{noise}}(t) (defined in Appendix [H.5](https://arxiv.org/html/2602.06394v1#A8.SS5 "H.5 Detailed Reward Components ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), Eq. [50](https://arxiv.org/html/2602.06394v1#A8.E50 "Equation 50 ‣ 2nd item ‣ 3rd item ‣ H.7 Domain-Specific Components ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")). P​(t′|t)P(t^{\prime}|t) was constructed based on heuristic rules derived from commonly observed error patterns in social media text and principles outlined in existing literature on noisy text processing. The specific noise types modeled include:

* •

  Character-Level Noise:

  + –

    Repetition: Probability of a character cc being realized as cnc^{n} (a sequence of nn identical characters). For n≥1n\geq 1, this can be modeled using a geometric-like distribution. If ps​t​o​pp\_{stop} is the probability of not repeating an additional time:
    P​(c→cn)=(1−ps​t​o​p)n−1⋅ps​t​o​pP(c\to c^{n})=(1-p\_{stop})^{n-1}\cdot p\_{stop}. The parameter ps​t​o​pp\_{stop} was set empirically to 0.50.5, allowing for moderate repetitions common in social media (e.g., "soooo goood").
  + –

    Substitution: P​(ci→cj)=Msub​[ci,cj]P(c\_{i}\to c\_{j})=M\_{\text{sub}}[c\_{i},c\_{j}], where MsubM\_{\text{sub}} is a confusion matrix. MsubM\_{\text{sub}} was constructed heuristically, assigning higher probabilities to substitutions between characters that are adjacent on a standard QWERTY keyboard layout and to common phonetic misspellings (e.g., ’c’ vs ’k’). Off-diagonal probabilities were generally small.
  + –

    Omission (Deletion): P​(c→ϵ)=pdel​(c)P(c\to\epsilon)=p\_{\text{del}}(c) is the character-specific deletion probability. This was set to a small uniform value (e.g., pdel​(c)=0.01p\_{\text{del}}(c)=0.01) for all characters, reflecting occasional accidental omissions.
* •

  Word-Level Noise:

  + –

    Abbreviation: P​(w→abbr​(w))=fabbr​(w→abbr​(w))P(w\to\text{abbr}(w))=f\_{\text{abbr}}(w\to\text{abbr}(w)). This probability was derived from a compiled dictionary of common internet slang and abbreviations sourced from publicly available online linguistic resources. For words in this dictionary, fabbrf\_{\text{abbr}} was set to a moderate value (e.g., 0.3), and zero otherwise.
  + –

    Phonetic Substitution: P​(w1→w2)∝exp⁡(λphon⋅phon\_sim​(w1,w2))P(w\_{1}\to w\_{2})\propto\exp(\lambda\_{\text{phon}}\cdot\text{phon\\_sim}(w\_{1},w\_{2})). The phonetic similarity phon\_sim​(w1,w2)\text{phon\\_sim}(w\_{1},w\_{2}) was computed using the Double Metaphone algorithm. The scaling factor λphon\lambda\_{\text{phon}} was set to 1.01.0.
* •

  Discourse-Level Noise (examples): For the experiments reported in this paper, the noise modeling primarily focused on character-level and word-level phenomena, as these are highly prevalent and tractable to model. Explicit modeling of discourse-level noise, such as code-switching or complex punctuation patterns, was considered beyond the scope of the current noise component RNR\_{N}, though it represents an interesting avenue for future work.

These probabilistic models are used to define P​(t′|t)P(t^{\prime}|t), which is then used to compute the expected distance in the noise robustness measure Rnoise​(t)=1−𝔼t′∼P(⋅|t)​[distnorm​(t,t′)]R\_{\text{noise}}(t)=1-\mathbb{E}\_{t^{\prime}\sim P(\cdot|t)}[\text{dist}\_{\text{norm}}(t,t^{\prime})]. The normalized distance metric distnorm​(t,t′)\text{dist}\_{\text{norm}}(t,t^{\prime}) used was the Levenshtein distance divided by the maximum length of the two strings tt and t′t^{\prime}.

### H.9 Domain-Specific Algorithms

This section provides detailed pseudocode for the QA-Token framework as instantiated for Quantitative Finance, Genomics, and Social Media. These algorithms complement the domain instantiations described in Section [H](https://arxiv.org/html/2602.06394v1#A8 "Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), illustrating the core mechanics within each domain.

#### H.9.1 Quantitative Finance (QAT-QF)

Algorithm 7  Quality-Aware Tokenization Merge Score and Reward Calculation (QAT-TOKEN - Finance)

0: Current vocabulary VtV\_{t}, corpus statistics (frequencies f​(⋅)f(\cdot)), current adaptive parameters θa​d​a​p​t={α,βv​o​l,γregime,fm​i​n,δgate,wk (param by 𝜷w)}\theta\_{adapt}=\{\alpha,\beta\_{vol},\gamma\_{\text{regime}},f\_{min},\delta\_{\text{gate}},w\_{k}\text{ (param by }\bm{\beta}\_{w})\}, reward weights λQ,λI,λP,λC\lambda\_{Q},\lambda\_{I},\lambda\_{P},\lambda\_{C}.

0: For each candidate merge pair (a,b)(a,b): quality-aware merge score wa​bw\_{ab}, total immediate reward R​(a,b)R(a,b).

1: Identify candidate merge pairs CtC\_{t} from corpus (e.g., from priority queue P​QtPQ\_{t}).

2: for each adjacent token pair (a,b)∈Ct(a,b)\in C\_{t} do

3:  Let tm​e​r​g​e​d←a||bt\_{merged}\leftarrow a||b.

4:  Retrieve/compute frequencies f​(a)f(a), f​(b)f(b), and f​(a,b)f(a,b).

5:  Retrieve/compute average qualities qa,qbq\_{a},q\_{b} (using Q​[i]Q[i] from Section [D.2](https://arxiv.org/html/2602.06394v1#A4.SS2 "D.2 Finance: Comprehensive Market Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), aggregated for tokens a,ba,b, and weights wk=softmax​(𝜷w)kw\_{k}=\text{softmax}(\bm{\beta}\_{w})\_{k}).

6:  Quality-Aware Merge Score (wa​bw\_{ab}):
wa​b←f​(a,b)f​(a)⋅f​(b)+ϵf⋅((qa+qb2+ϵQ)α)⋅ψ​(a,b)w\_{ab}\leftarrow\frac{f(a,b)}{f(a)\cdot f(b)+\epsilon\_{f}}\cdot\left(\left(\frac{q\_{a}+q\_{b}}{2}+\epsilon\_{Q}\right)^{\alpha}\right)\cdot\psi(a,b) // ψ​(a,b)=1\psi(a,b)=1 for finance

7:  Frequency Gating (Optional): // Frequency gating not used in final experiments
f~​(a,b)←f​(a,b)\tilde{f}(a,b)\leftarrow f(a,b).

8:  RQraw​(a,b)←|a|⋅qa+|b|⋅qb|a|+|b|R^{\text{raw}}\_{Q}(a,b)\leftarrow\frac{|a|\cdot q\_{a}+|b|\cdot q\_{b}}{|a|+|b|}.

9:  Estimate In​o​r​m​a​l,Is​t​r​e​s​sI\_{normal},I\_{stress} based on regime-conditioned f~​(a,b)\tilde{f}(a,b).
RIraw​(a,b)←γregime⋅In​o​r​m​a​l+(1−γregime)⋅Is​t​r​e​s​sR^{\text{raw}}\_{I}(a,b)\leftarrow\gamma\_{\text{regime}}\cdot I\_{normal}+(1-\gamma\_{\text{regime}})\cdot I\_{stress}.

10:  M​Iv​a​l←MI​(tm​e​r​g​e​d;Disc​(Rτ))MI\_{val}\leftarrow\text{MI}(t\_{merged};\text{Disc}(R\_{\tau})).
RPraw​(a,b)←M​Iv​a​lNormFactorM​I+ϵM​IR^{\text{raw}}\_{P}(a,b)\leftarrow\frac{MI\_{val}}{\text{NormFactor}\_{MI}+\epsilon\_{MI}} (NormFactorMI from Section [H.2](https://arxiv.org/html/2602.06394v1#A8.SS2 "H.2 Quantitative Finance (QAT-QF) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

11:  σc​u​r​r,σh​i​s​t←GetVolatility​()\sigma\_{curr},\sigma\_{hist}\leftarrow\text{GetVolatility}();
V​o​l​S​c​a​l​i​n​g←(1+max⁡(0,(σc​u​r​r−σh​i​s​t)/(σh​i​s​t+ϵvol)))βv​o​lVolScaling\leftarrow(1+\max(0,(\sigma\_{curr}-\sigma\_{hist})/(\sigma\_{hist}+\epsilon\_{\text{vol}})))^{\beta\_{vol}}

12:  RCraw​(a,b)←−|tm​e​r​g​e​d|⋅log⁡(|Vt|+1)⋅V​o​l​S​c​a​l​i​n​gR^{\text{raw}}\_{C}(a,b)\leftarrow-|t\_{merged}|\cdot\log(|V\_{t}|+1)\cdot VolScaling

13:  Normalize raw rewards: R^j​(a,b)←AdaptiveNormalize​(Rjraw​(a,b))\hat{R}\_{j}(a,b)\leftarrow\text{AdaptiveNormalize}(R^{\text{raw}}\_{j}(a,b)) using Eqs. [35](https://arxiv.org/html/2602.06394v1#A5.E35 "Equation 35 ‣ E.8 Reward Normalization Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), [33](https://arxiv.org/html/2602.06394v1#A5.E33 "Equation 33 ‣ E.8 Reward Normalization Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), and [34](https://arxiv.org/html/2602.06394v1#A5.E34 "Equation 34 ‣ E.8 Reward Normalization Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

14:  Total Immediate Reward (R​(a,b)R(a,b)): R​(a,b)←∑jλj​R^j​(a,b)R(a,b)\leftarrow\sum\_{j}\lambda\_{j}\hat{R}\_{j}(a,b).

15:  Store wa​bw\_{ab}, R​(a,b)R(a,b), and other features for (a,b)(a,b) for policy input or selection.

16: end for




Algorithm 8  Adaptive Parameter Learning for QA-TOKEN (Finance)

0: Training dataset 𝒟train\mathcal{D}\_{\text{train}};
Downstream task loss function Ltask​(⋅,⋅)L\_{\text{task}}(\cdot,\cdot); Model params Θmodel\Theta\_{\text{model}};
Initial adaptive parameters θa​d​a​p​t\theta\_{adapt}; Learning rate ηθ\eta\_{\theta}; Epochs Ea​d​a​p​tE\_{adapt}; Gumbel-Softmax τg\tau\_{g}.

0: Optimized adaptive parameters θa​d​a​p​t∗\theta\_{adapt}^{\*}.

1: Initialize θa​d​a​p​t\theta\_{adapt}.

2: for each adaptation epoch e=1,…,Ea​d​a​p​te=1,\dots,E\_{adapt} do

3:  for each mini-batch B={(Sseq,i,Ytarget,i)}B=\{(S\_{\text{seq},i},Y\_{\text{target},i})\} from 𝒟train\mathcal{D}\_{\text{train}} do

4:   𝒮b​a​t​c​h′←SoftTokenizeGumbel​(B,θa​d​a​p​t,τg)\mathcal{S}^{\prime}\_{batch}\leftarrow\textsc{SoftTokenizeGumbel}(B,\theta\_{adapt},\tau\_{g}) // Eq. [37](https://arxiv.org/html/2602.06394v1#A5.E37 "Equation 37 ‣ E.11 Gradient Computation ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")

5:   Lbatch\_task←Ltask​(𝒮b​a​t​c​h′,{Ytarget,i},Θmodel)L\_{\text{batch\\_task}}\leftarrow L\_{\text{task}}(\mathcal{S}^{\prime}\_{batch},\{Y\_{\text{target},i}\},\Theta\_{\text{model}})

6:   if regularization Lreg​(θa​d​a​p​t)L\_{\text{reg}}(\theta\_{adapt}) is used then

7:    Ltotal\_batch←Lbatch\_task+Lreg​(θa​d​a​p​t)L\_{\text{total\\_batch}}\leftarrow L\_{\text{batch\\_task}}+L\_{\text{reg}}(\theta\_{adapt})

8:   else

9:    Ltotal\_batch←Lbatch\_taskL\_{\text{total\\_batch}}\leftarrow L\_{\text{batch\\_task}}

10:   end if

11:   Compute gradients ∇θa​d​a​p​tLtotal\_batch\nabla\_{\theta\_{adapt}}L\_{\text{total\\_batch}}. // Uses Gumbel-Softmax trick

12:   Update θa​d​a​p​t←θa​d​a​p​t−ηθ​∇θa​d​a​p​tLtotal\_batch\theta\_{adapt}\leftarrow\theta\_{adapt}-\eta\_{\theta}\nabla\_{\theta\_{adapt}}L\_{\text{total\\_batch}}.

13:   Apply constraints to θa​d​a​p​t\theta\_{adapt} (e.g. α≥0\alpha\geq 0, softmax for weights).

14:  end for

15:  Anneal τg\tau\_{g}.

16: end for

17:

18: return θa​d​a​p​t∗←θa​d​a​p​t\theta\_{adapt}^{\*}\leftarrow\theta\_{adapt}.

#### H.9.2 Genomics (QA-BPE-seq)

Algorithm 9  Reward Calculation for a Merge (Genomics)

0: Tokens a,ba,b with qualities qa,qbq\_{a},q\_{b}; frequencies f​(⋅)f(\cdot); reward weights λj\lambda\_{j} from θa​d​a​p​t\theta\_{adapt}. For genomics, qa,qbq\_{a},q\_{b} represent geometric mean qualities of constituent tokens.

0: Raw rewards Rjraw​(a,b)R^{\text{raw}}\_{j}(a,b) for merging aa and bb.

1: tm​e​r​g​e​d←a||bt\_{merged}\leftarrow a||b

2: RQraw​(a,b)←(∏l=1|tm​e​r​g​e​d|qsm​e​r​g​e​d,l′)1/|tm​e​r​g​e​d|R^{\text{raw}}\_{Q}(a,b)\leftarrow(\prod\_{l=1}^{|t\_{merged}|}q^{\prime}\_{s\_{merged,l}})^{1/|t\_{merged}|}. // Geometric mean quality

3: RIraw​(a,b)←log⁡f​(tm​e​r​g​e​d)f​(a)⋅f​(b)+ϵfR^{\text{raw}}\_{I}(a,b)\leftarrow\log\frac{f(t\_{merged})}{f(a)\cdot f(b)+\epsilon\_{f}}.

4: RCraw​(a,b)←−len​(tm​e​r​g​e​d)R^{\text{raw}}\_{C}(a,b)\leftarrow-\text{len}(t\_{merged}).

5: if Biological Reward is used then

6:  O​v​e​r​l​a​p​S​c​o​r​e←ComputeOverlapScore​(tm​e​r​g​e​d,KnownBiologicalFeatures)OverlapScore\leftarrow\text{ComputeOverlapScore}(t\_{merged},\text{KnownBiologicalFeatures}).

7:  Rb​i​oraw​(a,b)←O​v​e​r​l​a​p​S​c​o​r​eR^{\text{raw}}\_{bio}(a,b)\leftarrow OverlapScore.

8: end if

9:

10: return All relevant Rjraw​(a,b)R^{\text{raw}}\_{j}(a,b). (Normalized rewards R^j\hat{R}\_{j} computed later using Eq. [35](https://arxiv.org/html/2602.06394v1#A5.E35 "Equation 35 ‣ E.8 Reward Normalization Details ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).

The size of the RL agent’s action space, KP​QK\_{PQ} (the number of top pairs from the priority queue considered at each step), was set to KP​Q=50K\_{PQ}=50. This value was chosen based on preliminary experiments indicating it offered a good trade-off between exposing the RL agent to a diverse set of high-potential merges and maintaining a manageable action space size for efficient policy learning. Values explored in the range [20,100][20,100] showed that performance was relatively robust for KP​Q∈[40,60]K\_{PQ}\in[40,60], with smaller values risking premature pruning of potentially beneficial long-term merges and larger values not yielding significant gains while increasing computational cost per policy step. The chosen value of 50 balanced these considerations effectively across domains.

* •

  RL (PPO specifics) - Stage 1:

  + –

    Policy/Value MLP Architecture: 2-3 hidden layers, each with 128-512 units. Activation functions: ReLU or Tanh.
  + –

    PPO ϵclip\epsilon\_{\text{clip}} (clipping parameter): [0.1,0.3][0.1,0.3], typically 0.20.2.
  + –

    GAE λGAE\lambda\_{\text{GAE}} (Generalized Advantage Estimation lambda): [0.9,0.99][0.9,0.99], typically 0.950.95.
  + –

    Discount factor γR​L\gamma\_{RL}: [0.95,1.0][0.95,1.0], often 0.990.99 for non-terminating tasks or long horizons.
  + –

    Optimizer: Adam (Kingma and Ba, [2014](https://arxiv.org/html/2602.06394v1#bib.bib44 "Adam: a method for stochastic optimization")). Learning rates ηπ\eta\_{\pi} (policy), ηv\eta\_{v} (value): [1×10−5,5×10−4][1\times 10^{-5},5\times 10^{-4}].
  + –

    Entropy bonus coefficient cSc\_{S} (or c2c\_{2}): [0.0,0.05][0.0,0.05], typically 0.010.01.
  + –

    Value function loss coefficient cV​Fc\_{VF} (or c1c\_{1}): [0.25,1.0][0.25,1.0], typically 0.50.5.
  + –

    Batch size (number of transitions per update): [128,4096][128,4096] or more, depending on data/memory.
  + –

    PPO epochs per update (passes over collected data): [3,20][3,20], typically 4−104-10.
  + –

    Number of actors / parallel environments: 11 to Nc​o​r​e​sN\_{cores} or NG​P​U​sN\_{GPUs}.
* •

  Adaptive Reward Normalization (Section [4.2](https://arxiv.org/html/2602.06394v1#S4.SS2 "4.2 Reward Function Design ‣ 4 Learning Framework: RL and Adaptive Parameters ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")):

  + –

    EMA momentum βnorm\beta\_{\text{norm}}: [10−3,10−1][10^{-3},10^{-1}], typically 10−210^{-2}.
  + –

    ϵR\epsilon\_{R} (stability constant): Typically 10−810^{-8}.
* •

  Reward Weights (βλj\bm{\beta}\_{\lambda\_{j}} leading to λj\lambda\_{j}): Initial values for 𝜷λj\bm{\beta}\_{\lambda\_{j}} in θadapt(0)\theta\_{\text{adapt}}^{(0)} for Stage 1 can be zero or small random numbers (resulting in uniform or near-uniform λj\lambda\_{j}). These are then optimized in Stage 2.
* •

  Adaptive Learning Parameters (θadapt\theta\_{\text{adapt}} from Algorithm [2](https://arxiv.org/html/2602.06394v1#alg2 "Algorithm 2 ‣ E.2.2 Gumbel-Softmax Differentiable Optimization ‣ E.2 Stage 2: Adaptive Parameter Learning ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) - Stage 2:

  + –

    Optimizer: Adam. Learning rate ηθ∈[1×10−6,1×10−4]\eta\_{\theta}\in[1\times 10^{-6},1\times 10^{-4}].
  + –

    Gumbel-Softmax temperature τ\tau: Annealed from an initial high value (e.g., 1.0−5.01.0-5.0) down to a small positive value (e.g., 0.1−0.50.1-0.5) over training. Schedule: e.g., exponential decay τt=max⁡(τf​i​n​a​l,τ0⋅dt)\tau\_{t}=\max(\tau\_{final},\tau\_{0}\cdot d^{t}).
  + –

    Logit composite function (Eq. [37](https://arxiv.org/html/2602.06394v1#A5.E37 "Equation 37 ‣ E.11 Gradient Computation ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")): Normℓ\text{Norm}\_{\ell} is typically identity or batch normalization if logits vary widely.
* •

  Domain-Specific Adaptive Parameters and Quality Metric Settings:

  + –

    Genomics Specific:

    - \*

      βpos\beta\_{\text{pos}} (positional quality decay): Learned. Initial range explored [0.001,0.1][0.001,0.1].
    - \*

      ϵl​e​n\epsilon\_{len} (Eq. [41](https://arxiv.org/html/2602.06394v1#A8.E41 "Equation 41 ‣ H.1 Genomics (QA-BPE-seq) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")): 10−610^{-6}.
  + –

    Social Media Specific:

    - \*

      𝜷wj\bm{\beta}\_{w\_{j}} (for Qa​g​gQ\_{agg} weights wjw\_{j}): Learned.
    - \*

      βs​e​m\beta\_{sem} (semantic compatibility, Eq. [44](https://arxiv.org/html/2602.06394v1#A8.E44 "Equation 44 ‣ H.3 Social Media Text (QA-BPE-nlp) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")): Learned. Initial range [0.1,5.0][0.1,5.0].
    - \*

      ω\omega (blending weight for RQrawR^{\text{raw}}\_{Q}, Eq. [46](https://arxiv.org/html/2602.06394v1#A8.E46 "Equation 46 ‣ 1st item ‣ H.6 Common Components ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")): Learned. Parameterized via sigmoid of an unconstrained variable.
    - \*

      Note: The direct downstream loss component RDR\_{D} was not used in the RL reward for the final reported Social Media NLP experiments (Section [H.3](https://arxiv.org/html/2602.06394v1#A8.SS3 "H.3 Social Media Text (QA-BPE-nlp) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
  + –

    Finance Specific:

    - \*

      𝜷wk\bm{\beta}\_{w\_{k}} (for Q​[i]Q[i] weights wkw\_{k}): Learned.
    - \*

      βv​o​l\beta\_{vol} (volatility scaling in RCR\_{C}): Learned. Initial range [0.0,2.0][0.0,2.0].
    - \*

      γregime\gamma\_{\text{regime}} (regime blending for RIR\_{I}): Learned. Parameterized via sigmoid of an unconstrained variable.
    - \*

      MM​IM\_{MI} (window for NormFactorM​I\text{NormFactor}\_{MI}): e.g., 1000 steps.
    - \*

      Note: Soft frequency gating was disabled in the final configuration for Quantitative Finance experiments (Section [5.2](https://arxiv.org/html/2602.06394v1#S5.SS2 "5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
* •

  General QA-Token Parameters:

  + –

    ϵf,ϵQ\epsilon\_{f},\epsilon\_{Q} (Eq. [5](https://arxiv.org/html/2602.06394v1#A3.E5 "Equation 5 ‣ Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")): 10−810^{-8}.
  + –

    α\alpha (quality sensitivity in wa​bw\_{ab}): Learned. Initial range [0.0,5.0][0.0,5.0].
* •

  Vocabulary Settings:

  + –

    Target vocabulary size VtargetV\_{\text{target}}: Typically [16000,64000][16000,64000].

#### H.9.3 Converged Adaptive Parameters

Table [19](https://arxiv.org/html/2602.06394v1#A8.T19 "Table 19 ‣ H.9.3 Converged Adaptive Parameters ‣ H.9 Domain-Specific Algorithms ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") provides mean converged values (±\pm standard deviation over three experimental runs) for key adaptive parameters in θa​d​a​p​t\theta\_{adapt} for each domain. The adaptive learning process tunes these parameters to optimize downstream task performance, leading to domain-specific configurations.

Table 19: Converged Adaptive Parameters (±\pm Std Dev).

|  |  |  |  |
| --- | --- | --- | --- |
| Parameter | Genomics | Finance | Social Media |
| α\alpha (Quality Sensitivity) | 0.72±0.030.72\pm 0.03 | 0.95±0.030.95\pm 0.03 | 1.15±0.051.15\pm 0.05 |
| λQ\lambda\_{Q} (Quality Reward Weight) | 0.35±0.030.35\pm 0.03 | 0.30±0.020.30\pm 0.02 | 0.33±0.030.33\pm 0.03 |
| λI\lambda\_{I} (Information Reward Weight) | 0.25±0.020.25\pm 0.02 | 0.20±0.020.20\pm 0.02 | 0.22±0.020.22\pm 0.02 |
| λC\lambda\_{C} (Complexity Reward Weight) | 0.15±0.010.15\pm 0.01 | 0.10±0.010.10\pm 0.01 | 0.12±0.010.12\pm 0.01 |
| βpos\beta\_{\text{pos}} (Genomics Positional Decay) | 0.014±0.0020.014\pm 0.002 | N/A | N/A |
| βvol\beta\_{\text{vol}} (Finance Volatility Scaling) | N/A | 0.50±0.050.50\pm 0.05 | N/A |
| γregime\gamma\_{\text{regime}} (Finance Regime Blending) | N/A | 0.60±0.040.60\pm 0.04 | N/A |
| worthw\_{\text{orth}} (NLP Orthographic Weight) | N/A | N/A | 0.32±0.030.32\pm 0.03 |
| wsemw\_{\text{sem}} (NLP Semantic Weight) | N/A | N/A | 0.28±0.020.28\pm 0.02 |
| wliqw\_{\text{liq}} (Finance Liquidity Weight) | N/A | 0.45±0.040.45\pm 0.04 | N/A |
| ωsocial\omega\_{\text{social}} (NLP Quality Blend) | N/A | N/A | 0.55±0.050.55\pm 0.05 |

### H.10 Social Media Ablation Results

Ablation studies in Table [20](https://arxiv.org/html/2602.06394v1#A8.T20 "Table 20 ‣ H.10 Social Media Ablation Results ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") are designed to confirm the individual effects of QA-BPE-nlp’s quality-aware components. We distinguish the impacts of: (1) the multi-dimensional quality rewards (row ’w/o Quality’), (2) semantic coherence considerations (row ’w/o Semantic’), (3) noise robustness features (row ’w/o Noise’), and (4) adaptive parameter learning (row ’w/o Adaptive Params’). Analysis of the learned weights wjw\_{j} for the quality dimensions (as detailed with values in Appendix [D.3](https://arxiv.org/html/2602.06394v1#A4.SS3 "D.3 Social Media: Linguistic Quality Metrics ‣ Appendix D Complete Quality Metrics Formulations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) indicates varying importance across dimensions (e.g., orthogonality qorthq\_{\text{orth}} and semantics qsemq\_{\text{sem}} frequently receive higher weights across runs) and reward components λi\lambda\_{i}, adapting to the specific task and dataset characteristics.

Table 20: Ablation Study for QA-BPE-nlp on TweetEval Sentiment. Values are means with 95% confidence intervals over n=10n=10 runs.

|  |  |  |
| --- | --- | --- |
| Configuration | TweetEval Score | Rel. Change (%) |
| QA-BPE-nlp (Full) | 74.5 ±\pm 0.3 | - |
| w/o RL Framework (Greedy wa​bw\_{ab}) | 72.1 ±\pm 0.4 | -3.2 |
| w/o Quality (RQ=0R\_{Q}=0) | 71.5 ±\pm 0.5 | -4.0 |
| w/o Semantic (RS=0R\_{S}=0) | 72.8 ±\pm 0.3 | -2.3 |
| w/o Noise (RN=0R\_{N}=0) | 73.2 ±\pm 0.4 | -1.7 |
| w/o Vocab Eff (RV=0R\_{V}=0) | 73.9 ±\pm 0.3 | -0.8 |
| w/o Adaptive Params (α,wj\alpha,w\_{j} fixed) | 71.8 ±\pm 0.5 | -3.6 |
| QualTok-nlp (Ablation Baseline) | 71.9 ±\pm 0.4 | -3.5 |

## Appendix I Dataset, Baseline, and Evaluation Details

This section supplements dataset descriptions, baseline methods, and evaluation metrics discussed in the main paper, providing further details necessary for understanding and reproducing the experimental results reported in Section [5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

### I.1 Datasets and Reproducible Evaluation

This subsection details the specific datasets, their versions, and relevant preprocessing steps or configurations used for the experiments reported in Section [5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"). All datasets are publicly available or available under licenses for academic research.

* •

  Genomics (QA-BPE-seq Experiments):

  + –

    Simulated Human Genomic Reads for Variant Calling, Reconstruction, and Ablations:
    Paired-end sequencing reads (150bp) were generated at 30x coverage using the ART simulator (version 2.5.8, using the art\_illumina tool) (Huang et al., [2012](https://arxiv.org/html/2602.06394v1#bib.bib49 "ART: a next-generation sequencing read simulator")). The simulation was based on the GRCh38 human reference genome (patch 13) and used the built-in HiSeq 2500 error profile (-ss HS25). To rigorously assess robustness in high-noise scenarios, as described in Section [H.1](https://arxiv.org/html/2602.06394v1#A8.SS1 "H.1 Genomics (QA-BPE-seq) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), the default base error rates (both substitution and indel rates) of this profile were artificially doubled compared to the standard HiSeq 2500 profile. Key ART parameters included: -p -l 150 -f 30 -m 400 -s 10. A corpus of approximately 5GB of these synthetic reads was generated and used for training tokenizers, downstream model evaluations, and the ablation studies reported in Section [H.1](https://arxiv.org/html/2602.06394v1#A8.SS1 "H.1 Genomics (QA-BPE-seq) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
    Access: The ART simulator is open-source and available at <https://www.niehs.nih.gov/research/resources/software/art/>. The GRCh38 reference genome can be obtained from public repositories such as NCBI GenBank or Ensembl.
  + –

    Genome in a Bottle (GIAB) Truth Set for Variant Calling Evaluation:
    Variant calling performance was benchmarked against the HG002 truth set (v4.2.1, GRCh38) (Zook et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib50 "Extensive sequencing of seven human genomes to characterize benchmark reference materials")).
    Access: GIAB truth sets are publicly available from the NIST FTP site.
  + –

    CAMI II Metagenome Benchmark for Taxonomic Classification:
    Taxonomic classification accuracy was evaluated using the "Toy Human Microbiome Project" (short reads, Assembly Aug2019) dataset from the Second CAMI Challenge (Sczyrba et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib51 "Critical assessment of metagenome interpretation—a benchmark of metagenomics software")). This benchmark provides datasets with known community compositions and corresponding sequencing reads for performance assessment.
    Access: CAMI II datasets are available through the official CAMI challenge website: <https://data.cami-challenge.org/participate>.
* •

  Quantitative Finance (QAT-QF Experiments):

  + –

    Cryptocurrency Limit Order Book (LOB) Data:
    High-frequency Limit Order Book (LOB) data for the BTC/USD trading pair was sourced from LOBSTER (<https://lobsterdata.com/>) (Huang and Polak, [2011](https://arxiv.org/html/2602.06394v1#bib.bib54 "LOBSTER: limit order book reconstruction system")), an academic data service. The experiments used reconstructed LOB snapshots at 10 levels for the first quarter of 2023 (Q1 2023). As detailed in Section [5.2](https://arxiv.org/html/2602.06394v1#S5.SS2 "5.2 Quantitative Finance (QAT-QF) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), this dataset was split chronologically into 70% for training, 15% for validation, and 15% for out-of-sample testing. Atomic elements for tokenization were defined as sequences of 5 consecutive LOB events, featurized as described in Appendix [H.2](https://arxiv.org/html/2602.06394v1#A8.SS2 "H.2 Quantitative Finance (QAT-QF) ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").
    Access: LOBSTER provides sample data publicly, while full datasets are available under academic or commercial licenses.
* •

  Social Media Text (QA-BPE-nlp Experiments):

  + –

    TweetEval Benchmark:
    The TweetEval benchmark (Barbieri et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib67 "TweetEval:Unified Benchmark and Comparative Evaluation for Tweet Classification")) was employed for evaluating QA-BPE-nlp across a diverse set of tweet classification tasks. TweetEval provides a unified framework with standardized data splits (train, validation, test) and evaluation metrics for seven heterogeneous tasks, which are:

    - \*

      Emotion Recognition (SemEval-2018 Task 1 (Mohammad et al., [2018](https://arxiv.org/html/2602.06394v1#bib.bib68 "Semeval-2018 task 1: affect in tweets")))
    - \*

      Emoji Prediction (SemEval-2018 Task 2 (Barbieri et al., [2018](https://arxiv.org/html/2602.06394v1#bib.bib69 "Semeval 2018 task 2: multilingual emoji prediction")))
    - \*

      Irony Detection (SemEval-2018 Task 3 (Van Hee et al., [2018](https://arxiv.org/html/2602.06394v1#bib.bib70 "Semeval-2018 task 3: irony detection in english tweets")))
    - \*

      Hate Speech Detection (SemEval-2019 Task 5 (Basile et al., [2019](https://arxiv.org/html/2602.06394v1#bib.bib71 "SemEval-2019 task 5: multilingual detection of hate speech against immigrants and women in Twitter")))
    - \*

      Offensive Language Identification (SemEval-2019 Task 6 (Zampieri et al., [2019](https://arxiv.org/html/2602.06394v1#bib.bib72 "SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval)")))
    - \*

      Sentiment Analysis (SemEval-2017 Task 4 (Rosenthal et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib59 "SemEval-2017 task 4: sentiment analysis in twitter")))
    - \*

      Stance Detection (SemEval-2016 Task 6 (Mohammad et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib73 "Semeval-2016 task 6: detecting stance in tweets")))

    As described in Section [I.8](https://arxiv.org/html/2602.06394v1#A9.SS8 "I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), experiments involved fine-tuning a pre-trained BERTweet-base model (Nguyen et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib61 "BERTweet: a pre-trained language model for english tweets")) on these tasks using different tokenization strategies.
    Access: The TweetEval benchmark, including data access scripts and details for each constituent dataset, is available on GitHub: <https://github.com/cardiffnlp/tweeteval>. Access to the underlying tweet content typically requires hydration of tweet IDs and adherence to Twitter’s Terms of Service and the respective dataset licenses.

### I.2 Dataset and Release Plan

To enable foundation-model training on previously unusable noisy corpora, we will release:

* •

  Tokenizer artifacts: Final QA-Token vocabularies, merge tables, and θadapt\theta\_{\text{adapt}} for each domain (genomics, finance, social media) at multiple vocabulary sizes.
* •

  Foundation-model-ready corpora manifests: Scripts and manifests to reconstruct large noisy pretraining corpora (including filtering and de-duplication), plus sampler configurations matching our 2B-subset tokenizer training protocol.
* •

  Evaluation suites: Reproducible pipelines for genomics (variant calling, metagenomics), finance (prediction, volatility, regime, trading), and social media (TweetEval), along with the RL ablation harness.
* •

  Documentation and governance: Licenses, data usage considerations, and guidelines for responsible use in high-impact applications (e.g., financial decision-making and clinical genomics).

All code and artifacts will be released under permissive academic licenses to maximize reproducibility and adoption.

### I.3 QA-Foundation: Noisy Pretraining Corpora Proposal

We propose QA-Foundation, a curated suite of extremely large, noisy corpora specifically designed to enable foundation-scale pretraining with explicit quality annotations and governance:

* •

  Genomics: multi-petabase metagenomic reads (SRA) with canonicalized metadata, Phred-quality distributions, duplication maps, contamination flags, and per-read provenance hashes. Quality channels include per-base Phred, platform, run, trimming logs, adapter contamination.
* •

  Finance: multi-asset high-frequency LOB streams (equities, futures, crypto) with synchronized calendars, microstructure indicators (spreads, depth, order-imbalance), regime tags, and exchange-specific anomaly flags.
* •

  Social/Web text: multi-platform user-generated text with timestamps, platform labels, de-identified stable author hashes, normalization annotations (hashtags, mentions, URLs), and noise transformations (variant clusters, repetition, keyboard-distance confusion matrices).

Each domain provides standardized schemas, quality channels, and sampling manifests to reproduce tokenizer training at multiple scales (e.g., 0.1%, 1%, 5%) and to support fair comparisons. Scripts produce manifests, deduplication indices (MinHash/LSH), and quality audit reports. Governance includes explicit licenses, intended-use statements, and red-team risk assessments. We will release:

* •

  Tokenizer-ready shards with checksums and integrity manifests
* •

  Quality channel extractors (open-source) and validation suites
* •

  Reproducible samplers that match our 2B-base subset protocol for genomics and analogous budgets for other domains

### I.4 Baseline Methods

The following baseline tokenization methods were implemented and configured for rigorous comparison against the proposed QA-Token variants, as presented in Section [5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

* •

  Standard Byte Pair Encoding (BPE) (Sennrich et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib13 "Neural machine translation of rare words with subword units")): The conventional frequency-based merging algorithm. For genomics and social media experiments, this was implemented using the HuggingFace ‘tokenizers‘ library (version 0.15.0), specifically configured with t​o​k​e​n​i​z​e​r​s.m​o​d​e​l​s.B​P​E​(u​n​k​\_​t​o​k​e​n=”​[U​N​K]​”,m​i​n​\_​f​r​e​q​u​e​n​c​y=2)tokenizers.models.BPE(unk\\_token="[UNK]",min\\_frequency=2), unless stated otherwise. For quantitative finance experiments, a comparable standard BPE implementation was used.
* •

  SentencePiece (Kudo and Richardson, [2018](https://arxiv.org/html/2602.06394v1#bib.bib15 "SentencePiece: a simple and language independent subword tokenizer and detokenizer for neural text processing")): An unsupervised text tokenizer and detokenizer. For genomics and social media experiments, SentencePiece (version 0.1.99) was used in its byte-level BPE mode, operating directly on raw text.
* •

  WordPiece (Wu et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib14 "Google’s neural machine translation system: bridging the gap between human and machine translation")): The subword tokenization algorithm famously used in BERT. It iteratively builds a vocabulary by merging pairs that maximize the likelihood of the training data under a unigram language model assumption.
* •

  DNABERT k-mer (Ji et al., [2021](https://arxiv.org/html/2602.06394v1#bib.bib9 "DNABERT: pre-trained bidirectional encoder representations from transformers model for dna-language in genome")): For experiments in the genomics domain, fixed k-mer tokenization was employed as a strong baseline, specifically using 6-mers. This aligns with common practice in models like DNABERT.
* •

  Symbolic Aggregate approXimation (SAX) (Lin et al., [2003](https://arxiv.org/html/2602.06394v1#bib.bib55 "Symbolic representation of time series, with implications for streaming algorithms")): A well-established symbolic representation method for time series data, applied in quantitative finance experiments. The mid-price series was discretized using a Piecewise Aggregate Approximation (PAA) window size of 16 and an alphabet size of 8.
* •

  Bag-of-SFA-Symbols (BOSS) (Schäfer, [2015](https://arxiv.org/html/2602.06394v1#bib.bib56 "The boss is concerned with time series classification in the presence of noise")): A time series classification algorithm that uses Symbolic Fourier Approximation (SFA) to generate symbolic words (tokens). This was used as a baseline in the quantitative finance domain, applied to the mid-price series.
* •

  QualTok (Ablation Baseline): As described in Section [5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization"), QualTok serves as an ablation baseline for QA-Token. It employs a simplified quality-aware merge score, wa​b∝f​(a,b)f​(a)​f​(b)+ϵf⋅(qa+qb2+ϵQ)αw\_{ab}\propto\frac{f(a,b)}{f(a)f(b)+\epsilon\_{f}}\cdot\left(\frac{q\_{a}+q\_{b}}{2}+\epsilon\_{Q}\right)^{\alpha}, but critically omits the reinforcement learning policy optimization for merge sequences and the full adaptive learning loop for complex θadapt\theta\_{\text{adapt}} parameters beyond tuning α\alpha. Merge operations are typically performed greedily based on this score.

For all baseline methods, we select essential hyperparameters, such as the target vocabulary size (which typically corresponds to a predefined number of merge operations, e.g., 16,000 or 32,000, as specified per domain in Section [5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")), based on common practices in the literature (Sennrich et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib13 "Neural machine translation of rare words with subword units"); Kudo and Richardson, [2018](https://arxiv.org/html/2602.06394v1#bib.bib15 "SentencePiece: a simple and language independent subword tokenizer and detokenizer for neural text processing"); Wu et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib14 "Google’s neural machine translation system: bridging the gap between human and machine translation"); Devlin et al., [2019](https://arxiv.org/html/2602.06394v1#bib.bib6 "Bert: pre-training of deep bidirectional transformers for language understanding"); Brown et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib7 "Language models are few-shot learners"); Ji et al., [2021](https://arxiv.org/html/2602.06394v1#bib.bib9 "DNABERT: pre-trained bidirectional encoder representations from transformers model for dna-language in genome")), specific recommendations from the original implementations of these methods, or by identifying the best-performing configuration on a held-out validation set from a systematic sweep of reasonable values to ensure robust comparisons.

### I.5 Evaluation Metrics

The performance of QA-Token and baseline methods was assessed using the following domain-specific metrics, corresponding to the results presented in Section [5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

* •

  Genomics:

  + –

    Variant Calling: Performance was measured by F1-score, precision, and recall against the GIAB truth sets. These metrics were computed using the ‘hap.py‘ tool (version 0.3.14), available at <https://github.com/Illumina/hap.py>.
  + –

    Taxonomic Classification (Metagenomics): For the CAMI II benchmark, performance was primarily assessed using classification accuracy (specifically, the F1-score for overall classification performance, as reported in Table [1](https://arxiv.org/html/2602.06394v1#S5.T1 "Table 1 ‣ 5.1 Genomics (QA-BPE-seq) ‣ 5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")).
  + –

    Sequence Reconstruction Loss: The quality of token representations was also evaluated by training Transformer-based autoencoder models and measuring the reconstruction loss (e.g., cross-entropy for discrete tokens) on a held-out test set.

  Variant Calling Model Architecture: The variant calling evaluation uses a Transformer encoder that takes token embeddings as input features. The model outputs per-position variant probabilities (SNV, insertion, deletion, reference). Training uses cross-entropy loss against GIAB HG002 labels. This approach evaluates how well tokenization preserves variant-informative sequence features in the learned representations, with evaluation performed using the hap.py benchmarking tool (v0.3.14).
* •

  Quantitative Finance:

  + –

    Return Prediction Accuracy: The percentage of correctly predicted signs for future (e.g., 5-minute ahead) mid-price returns.
  + –

    Volatility Forecasting RMSE: The Root Mean Squared Error between the predicted 5-minute volatility and the realized volatility (computed from higher-frequency data).
  + –

    Market Regime Identification Accuracy: The accuracy achieved in classifying time periods into discrete market states (e.g., two states identified by a GARCH-HMM).
  + –

    Trading Performance: The primary metric was the annualized Sharpe Ratio (Sharpe, [1994](https://arxiv.org/html/2602.06394v1#bib.bib48 "The sharpe ratio")) achieved by a PPO-based trading agent operating on the tokenized data. A transaction cost of 5 basis points per trade was incorporated. Additional performance metrics, such as Maximum Drawdown (MDD) and Calmar Ratio, were also monitored (see Appendix [H.4](https://arxiv.org/html/2602.06394v1#A8.SS4 "H.4 Financial Experimental Methodology Details ‣ Appendix H Domain-Specific Instantiations ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") for further details).
* •

  Social Media Text:

  + –

    Performance on the seven TweetEval benchmark tasks was measured using the official evaluation metric specified by the benchmark organizers for each respective task (Barbieri et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib67 "TweetEval:Unified Benchmark and Comparative Evaluation for Tweet Classification")). These metrics are:

    - \*

      Emoji Prediction: Accuracy (Acc)
    - \*

      Emotion Recognition: Macro F1-score (F1 M)
    - \*

      Hate Speech Detection: Macro F1-score (F1 M)
    - \*

      Irony Detection: Accuracy (Acc)
    - \*

      Offensive Language Identification: Macro F1-score (F1 M)
    - \*

      Sentiment Analysis: Macro Recall (Rec M)
    - \*

      Stance Detection: Average F1-score across topics (F1 Avg)

All reported experimental results in Section [5](https://arxiv.org/html/2602.06394v1#S5 "5 Empirical Validation ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") represent the mean and 95% confidence interval over n=10n=10 independent runs to ensure robustness and allow for assessment of variability.

### I.6 Code Availability

We will release the QA-Token framework on GitHub under an MIT license. The repository includes source code, configuration files, pre-trained models, and reproducibility scripts for all experiments.

### I.7 Approximating QA-Token: Towards Computationally Efficient Quality-Awareness

The learning framework of QA-Token has high computational costs due to both RL and adaptive learning stages. Future work will explore computationally lighter approximations. A starting point is our ablation baseline, QualTok, which uses a greedy merge strategy based on the quality-aware score wa​bw\_{ab} (Equation [5](https://arxiv.org/html/2602.06394v1#A3.E5 "Equation 5 ‣ Theorem C.3 (Quality-Aware Merge Score — Principled Heuristic). ‣ C.3 Derivation of the Optimal Merge Score ‣ Appendix C Theoretical Framework and Proofs ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) without explicit RL policy optimization, bypassing the costs of Stage 1 RL.

Further cost reduction can be achieved by:

1. 1.

   Streamlined Adaptive Parameter Learning for Greedy Merges: Instead of full RL, we can focus on adaptively learning a refined set of parameters θadapt∗\theta\_{\text{adapt}}^{\*} (e.g., α\alpha, quality weights wjw\_{j}, simplified reward weights λj\lambda\_{j}) that directly optimize the greedy wa​bw\_{ab}-guided tokenization for downstream tasks. This retains the core quality-aware adaptability while significantly reducing complexity compared to learning an RL policy. The Gumbel-Softmax based learning (Stage 2) would optimize θadapt\theta\_{\text{adapt}} for these greedy merges, possibly using simplified composite logits.
2. 2.

   Policy Distillation: If the RL policy πθπ∗\pi\_{\theta\_{\pi}}^{\*} captures complex merge dependencies, the computational overhead at deployment can be mitigated. A compact "student" model (e.g., a smaller neural network or decision tree) can be trained via policy distillation (Hinton et al., [2015](https://arxiv.org/html/2602.06394v1#bib.bib80 "Distilling the knowledge in a neural network"); Rusu et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib83 "Policy distillation")) to mimic the decisions of a larger, pre-trained "teacher" RL agent, offering faster vocabulary construction.
3. 3.

   Surrogate-Assisted Adaptive Learning: The optimization of θadapt\theta\_{\text{adapt}} (Stage 2) can be accelerated by using cheaper-to-evaluate surrogate models (Jones et al., [1998](https://arxiv.org/html/2602.06394v1#bib.bib79 "Efficient global optimization of expensive black-box functions")) to approximate the downstream task loss LtaskL\_{\text{task}}, reducing the need for frequent, costly end-to-end evaluations with the full downstream model.
4. 4.

   Transfer and Meta-Learning for θadapt\theta\_{\text{adapt}}: Leveraging learned θadapt\theta\_{\text{adapt}} parameters from one task or dataset as initializations for others (as in Algorithm [6](https://arxiv.org/html/2602.06394v1#alg6 "Algorithm 6 ‣ E.5 Algorithm Summary ‣ Appendix E Sequential Learning Process: Complete Framework ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization")) can substantially reduce the training burden for new applications.

### I.8 Extended TweetEval Benchmarking Methodology

This section describes the comprehensive TweetEval benchmarking methodology. Results are reported in Table [21](https://arxiv.org/html/2602.06394v1#A9.T21 "Table 21 ‣ I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization").

Datasets and Evaluation Framework: TweetEval (Barbieri et al., [2020](https://arxiv.org/html/2602.06394v1#bib.bib67 "TweetEval:Unified Benchmark and Comparative Evaluation for Tweet Classification")) provides a unified framework for evaluating models on seven heterogeneous tweet classification tasks, each with fixed training, validation, and test splits. This allows for standardized comparison across different approaches. The seven tasks are: Emotion Recognition (Mohammad et al., [2018](https://arxiv.org/html/2602.06394v1#bib.bib68 "Semeval-2018 task 1: affect in tweets")) (4 labels: anger, joy, sadness, optimism), Emoji Prediction (Barbieri et al., [2018](https://arxiv.org/html/2602.06394v1#bib.bib69 "Semeval 2018 task 2: multilingual emoji prediction")) (20 emoji labels), Irony Detection (Van Hee et al., [2018](https://arxiv.org/html/2602.06394v1#bib.bib70 "Semeval-2018 task 3: irony detection in english tweets")) (2 labels: irony, not irony), Hate Speech Detection (Basile et al., [2019](https://arxiv.org/html/2602.06394v1#bib.bib71 "SemEval-2019 task 5: multilingual detection of hate speech against immigrants and women in Twitter")) (2 labels: hateful, not hateful), Offensive Language Identification (Zampieri et al., [2019](https://arxiv.org/html/2602.06394v1#bib.bib72 "SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval)")) (2 labels: offensive, not offensive), Sentiment Analysis (Rosenthal et al., [2017](https://arxiv.org/html/2602.06394v1#bib.bib59 "SemEval-2017 task 4: sentiment analysis in twitter")) (3 labels: positive, neutral, negative), and Stance Detection (Mohammad et al., [2016](https://arxiv.org/html/2602.06394v1#bib.bib73 "Semeval-2016 task 6: detecting stance in tweets")) (3 labels: favour, neutral, against, across five topics).
For each task, we report performance using the unified evaluation metrics specified by the TweetEval benchmark.
Table [21](https://arxiv.org/html/2602.06394v1#A9.T21 "Table 21 ‣ I.8 Extended TweetEval Benchmarking Methodology ‣ Appendix I Dataset, Baseline, and Evaluation Details ‣ Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization") provides the baseline comparison framework. The official metric for each task as defined by TweetEval (also see https://github.com/cardiffnlp/tweeteval for details) is reported.

Table 21: TweetEval Baseline Comparison Framework.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Emoji | Emotion | Hate | Irony | Offensive | Sentiment | Stance | ALL(TE) |
| BERTweet | 33.4 | 79.3 | 56.4 | 82.1 | 79.5 | 73.4 | 71.2 | 67.9 |
| TimeLMs-2021 | 34.0 | 80.2 | 55.1 | 64.5 | 82.2 | 73.7 | 72.9 | 66.2 |
| RoBERTa-Retrained | 31.4 | 78.5 | 52.3 | 61.7 | 80.5 | 72.8 | 69.3 | 65.2 |
| RoBERTa-Base | 30.9 | 76.1 | 46.6 | 59.7 | 79.5 | 71.3 | 68.0 | 61.3 |
| RoBERTa-Twitter | 29.3 | 72.0 | 49.9 | 65.4 | 77.1 | 69.1 | 66.7 | 61.4 |
| FastText | 25.8 | 65.2 | 50.6 | 63.1 | 73.4 | 62.9 | 65.4 | 58.1 |
| LSTM | 24.7 | 66.0 | 52.6 | 62.8 | 71.7 | 58.3 | 59.4 | 56.5 |
| SVM | 29.3 | 64.7 | 36.7 | 61.7 | 52.3 | 62.9 | 67.3 | 53.5 |
| QA-BPE-nlp + BERTweet | 34.2 | 81.5 | 58.8 | 82.9 | 83.0 | 75.1 | 73.5 | 70.0 |