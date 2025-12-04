---
authors:
- Mainak Singha
doc_id: arxiv:2512.03107v1
family_id: arxiv:2512.03107
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts
  Hallucination Rate by 92%'
url_abs: http://arxiv.org/abs/2512.03107v1
url_html: https://arxiv.org/html/2512.03107v1
venue: arXiv q-fin
version: 1
year: 2025
---


Mainak Singha
  
Astrophysics Science Division, NASA, Goddard Space Flight Center,
  
8800 Greenbelt Road, MD 20771
  
Department of Physics, The Catholic University of America, Washington, DC 20064
  
mainak.singha@nasa.gov, singham@cua.edu

###### Abstract

Large language models (LLMs) produce fluent but unsupported answers—*hallucinations*—limiting safe deployment in high-stakes domains. We propose ECLIPSE, a framework that treats hallucination as a mismatch between a model’s *semantic entropy* and the *capacity* of available evidence. We combine entropy estimation via multi-sample clustering with a novel *perplexity decomposition* that measures how models use retrieved evidence. We prove that under mild conditions, the resulting entropy–capacity objective is strictly convex with a unique stable optimum. We evaluate on a controlled financial question answering dataset with GPT-3.5-turbo (n=200n=200 balanced samples with synthetic hallucinations), where ECLIPSE achieves ROC AUC of 0.89 and average precision of 0.90, substantially outperforming a semantic entropy-only baseline (AUC 0.50). A controlled ablation with Claude-3-Haiku, which lacks token-level log probabilities, shows AUC dropping to 0.59 with coefficient magnitudes decreasing by 95%—demonstrating that ECLIPSE is a *logprob-native* mechanism whose effectiveness depends on calibrated token-level uncertainties. The perplexity decomposition features exhibit the largest learned coefficients, confirming that evidence utilization is central to hallucination detection. We position this work as a controlled mechanism study; broader validation across domains and naturally occurring hallucinations remains future work.

## 1 Introduction

Large language models have become integral to decision support in finance [wu2023bloomberggpt], healthcare [singhal2023large], and law [cui2023chatlaw]. However, their tendency to produce confident but factually incorrect statements—commonly termed *hallucinations*—poses significant risks in these high-stakes domains [ji2023survey, huang2023survey]. Hallucinations are particularly dangerous because models often express them with high apparent certainty, making them difficult to detect through simple confidence thresholds [xiong2024can].

Existing hallucination detection methods primarily measure model uncertainty through semantic entropy [kuhn2023semantic] or self-consistency checks [manakul2023selfcheckgpt]. However, uncertainty alone provides an incomplete picture: a model may exhibit honest uncertainty when evidence is weak, or dangerous overconfidence when evidence is strong but ignored. We argue that hallucination risk depends fundamentally on the *relationship* between two quantities: the model’s expressed certainty and the quality of available evidence.

We propose ECLIPSE (Entropy–Capacity Logprob-Native Inference for Predicting Spurious Emissions), a framework that makes this entropy–capacity trade-off explicit. We call a method *logprob-native* if its core signal relies directly on token-level log probabilities and degrades substantially when those probabilities are replaced by uninformative proxies. Unlike semantic entropy alone, which cannot distinguish honest uncertainty from evidence-ignoring behavior, ECLIPSE decomposes perplexity to measure *how* models use evidence. Unlike Semantic Entropy Probes (SEPs), which require white-box access to hidden states, ECLIPSE achieves comparable detection performance using only API-accessible log probabilities. Unlike SelfCheckGPT, which relies on self-consistency across generations, ECLIPSE directly measures the evidence–answer relationship through perplexity decomposition.

Our contributions are:

1. 1.

   Theoretical framework: We introduce a joint objective over semantic entropy HH and evidence capacity CC and prove it is strictly convex under mild conditions (Theorem [4](https://arxiv.org/html/2512.03107v1#Thmtheorem4 "Theorem 4 (Stability and convexity). ‣ 3.3 Joint Objective and Stability ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%")), providing a principled foundation for hallucination risk modeling and, in future work, control.
2. 2.

   Perplexity decomposition: We extract features (LQL\_{Q}, LQ​EL\_{QE}, Δ​L\Delta L) that decompose *how* models use evidence, enabling fine-grained detection of evidence-ignoring behavior.
3. 3.

   Empirical validation: On our controlled financial QA dataset (n=200n=200), ECLIPSE achieves 0.89 AUC using only API access (Figure [1](https://arxiv.org/html/2512.03107v1#S4.F1 "Figure 1 ‣ Results. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%")), indicating that logprob-native, grey-box detectors can reach strong performance without hidden-state access.
4. 4.

   Mechanism validation: We show through controlled ablation that ECLIPSE is logprob-native: without real log probabilities, performance drops from 0.89 to 0.59 AUC, only modestly above chance (Figure [5](https://arxiv.org/html/2512.03107v1#S4.F5 "Figure 5 ‣ 4.3 Mechanism Validation: Claude-3-Haiku Ablation ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%")).

## 2 Related Work

#### Hallucination in language models.

The phenomenon of LLM hallucination has received substantial attention [ji2023survey, zhang2023siren, huang2023survey]. Hallucinations manifest in various forms: factual errors [min2023factscore], entity confusion [dziri2022origin], and fabricated citations [liu2023evaluating]. Maynez et al. [maynez2020faithfulness] categorize hallucinations in abstractive summarization as intrinsic (contradicting source) or extrinsic (unverifiable from source). Our work focuses on the latter in retrieval-augmented settings.

#### Uncertainty quantification in LLMs.

Gal and Ghahramani [gal2016dropout] established dropout-based uncertainty estimation for neural networks. For LLMs, Kadavath et al. [kadavath2022language] demonstrated that models can partially assess their own uncertainty but degrade out-of-distribution. Kuhn et al. [kuhn2023semantic] introduced semantic entropy, which clusters sampled outputs by meaning and computes entropy over clusters. Lin et al. [lin2024generating] extended this with conformal prediction for calibrated uncertainty sets. We build on semantic entropy but augment it with evidence capacity to distinguish honest uncertainty from hallucination.

#### Hallucination detection methods.

SelfCheckGPT [manakul2023selfcheckgpt] samples multiple responses and measures consistency, achieving strong results on biography generation. Semantic Entropy Probes (SEPs) [kossen2024semantic] train linear classifiers on hidden states, reaching 0.85–0.90 AUC but requiring white-box model access. SAPLMA [azaria2023internal] similarly uses hidden state classifiers. Min et al. [min2023factscore] decompose responses into atomic facts and verify each against knowledge sources. Unlike these approaches, ECLIPSE achieves comparable performance using only API access while providing interpretable coefficients.

#### Retrieval-augmented generation.

RAG systems [lewis2020retrieval, guu2020realm, izacard2022atlas] ground model outputs in retrieved documents but do not eliminate hallucinations [shuster2021retrieval]. Shi et al. [shi2023large] show that irrelevant context can degrade performance. Yoran et al. [yoran2024making] propose filtering retrieved passages by relevance. Our perplexity decomposition specifically targets the failure mode where models ignore relevant evidence.

#### Calibration and selective prediction.

Guo et al. [guo2017calibration] demonstrated that modern neural networks are poorly calibrated. Temperature scaling [guo2017calibration] and Platt scaling [platt1999probabilistic] provide post-hoc calibration. Selective prediction frameworks [el2010foundations, geifman2017selective] enable models to abstain when uncertain. Varshney et al. [varshney2022investigating] apply selective prediction to question answering. ECLIPSE provides a principled abstention signal based on both uncertainty and evidence quality.

#### Information-theoretic approaches.

Xu et al. [xu2020understanding] analyze neural text generation through the lens of information theory. Holtzman et al. [holtzman2020curious] identify the “likelihood trap” where high-probability text is often degenerate. Our capacity measure draws on information-theoretic intuitions, quantifying mutual information between evidence and answer through log-likelihood differences.

## 3 Method: ECLIPSE

### 3.1 Problem Setup

We consider a language model pθ​(A∣Q,E)p\_{\theta}(A\mid Q,E) that answers query QQ given evidence EE, producing answer AA. We seek to estimate the probability that AA is hallucinated—unsupported or contradicted by EE. This setting captures retrieval-augmented generation, where EE consists of retrieved documents, as well as grounded QA tasks where EE is provided context.

### 3.2 Entropy–Capacity Model

We introduce four quantities that form the foundation of our framework.

###### Definition 1 (Semantic entropy).

Let H≥0H\geq 0 denote the model’s uncertainty over semantically distinct answers to (Q,E)(Q,E), estimated via multi-sample clustering as described in Section [3.4](https://arxiv.org/html/2512.03107v1#S3.SS4 "3.4 Estimating Entropy and Capacity ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%").

###### Definition 2 (Evidence capacity).

Let CC measure how informative the evidence EE is about the answer. High capacity indicates that EE strongly constrains the answer distribution; low or negative capacity indicates weak or misleading evidence.

###### Definition 3 (Preferred entropy).

Let Hpref​(C,Q)H\_{\text{pref}}(C,Q) denote the entropy level that would be optimal for task performance alone, encoding how concentrated the answer distribution should be given capacity CC.

We model hallucination probability through a logistic function that depends on the deviation of entropy from its preferred level:

|  |  |  |  |
| --- | --- | --- | --- |
|  | phall​(H,C)=σ​(a​(H−Hpref​(C,Q))−b​C+c),p\_{\text{hall}}(H,C)=\sigma\big(a(H-H\_{\text{pref}}(C,Q))-bC+c\big), |  | (1) |

where a,b>0a,b>0, c∈ℝc\in\mathbb{R}, and σ​(z)=1/(1+e−z)\sigma(z)=1/(1+e^{-z}) is the logistic function. The key insight is that risk depends on *misalignment* between actual and preferred entropy. Both overconfidence (H≪HprefH\ll H\_{\text{pref}}) and underconfidence (H≫HprefH\gg H\_{\text{pref}}) can indicate problems, but the nature of the problem differs.

### 3.3 Joint Objective and Stability

We define a joint objective that balances task performance against hallucination risk:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒtotal​(H∣C,Q)=α​(H−Hpref​(C,Q))2+λ​phall​(H,C),\mathcal{L}\_{\text{total}}(H\mid C,Q)=\alpha(H-H\_{\text{pref}}(C,Q))^{2}+\lambda\,p\_{\text{hall}}(H,C), |  | (2) |

where α>0\alpha>0 controls preference for staying near the task-optimal entropy and λ>0\lambda>0 scales the hallucination penalty. The following theorem establishes when this objective is well-behaved.

###### Theorem 4 (Stability and convexity).

If α>λ​a2/8\alpha>\lambda a^{2}/8, then ℒtotal​(H∣C,Q)\mathcal{L}\_{\text{total}}(H\mid C,Q) is strictly convex in HH, admits a unique global minimizer H∗​(C,Q)H^{\*}(C,Q), and gradient descent converges from any initialization.

We provide a complete proof in Appendix [A](https://arxiv.org/html/2512.03107v1#A1 "Appendix A Complete Proof of Theorem 4 ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%"). The condition α>λ​a2/8\alpha>\lambda a^{2}/8 ensures that the quadratic task term dominates the curvature of the logistic penalty, preventing non-convexity.

#### Relationship to implementation.

The entropy–capacity objective (Eqs. ([1](https://arxiv.org/html/2512.03107v1#S3.E1 "In 3.2 Entropy–Capacity Model ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%"))–([2](https://arxiv.org/html/2512.03107v1#S3.E2 "In 3.3 Joint Objective and Stability ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%"))) and Theorem [4](https://arxiv.org/html/2512.03107v1#Thmtheorem4 "Theorem 4 (Stability and convexity). ‣ 3.3 Joint Objective and Stability ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") provide a conceptual framework that establishes when an entropy controller would be stable and well-behaved. In this work, we do not directly optimize this objective during training. Instead, we use it as a *design prior* for feature engineering: the model predicts coefficient signs (e.g., wH>0w\_{H}>0, wCeff<0w\_{C\_{\text{eff}}}<0, wΔ​L<0w\_{\Delta L}<0) that we verify empirically in Section [4](https://arxiv.org/html/2512.03107v1#S4 "4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%"). We estimate HH and capacity-related features and learn a calibrated detector via logistic regression (Eq. ([5](https://arxiv.org/html/2512.03107v1#S3.E5 "In 3.5 Calibrated Hallucination Model ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%"))). The theoretical framework guides feature design and provides interpretability, while the empirical model delivers the operational detector.

### 3.4 Estimating Entropy and Capacity

We implement both quantities using only API access (text generation and log probabilities).

#### Semantic entropy.

Following Kuhn et al. [kuhn2023semantic], we generate KK answers {A1,…,AK}\{A\_{1},\ldots,A\_{K}\} from pθ(⋅∣Q,E)p\_{\theta}(\cdot\mid Q,E) and cluster them by factual content. For financial QA, we extract (entity, attribute, value) triples using pattern matching and named entity recognition. We assign two answers to the same cluster if their extracted facts match within tolerance (numeric values within 1% relative error). This yields clusters {C1,…,Cm}\{C\_{1},\ldots,C\_{m}\} with empirical probabilities pj=|Cj|/Kp\_{j}=|C\_{j}|/K. We compute:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^=−∑j=1mpj​log⁡pj.\hat{H}=-\sum\_{j=1}^{m}p\_{j}\log p\_{j}. |  | (3) |

#### Perplexity-based capacity.

We measure how evidence changes answer log-likelihood:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^eff=[log⁡pθ​(A∗∣Q,E)−log⁡pθ​(A∗∣Q)]⋅wcons,\hat{C}\_{\text{eff}}=\big[\log p\_{\theta}(A^{\*}\mid Q,E)-\log p\_{\theta}(A^{\*}\mid Q)\big]\cdot w\_{\text{cons}}, |  | (4) |

where A∗A^{\*} is the model’s top answer and wcons∈[0,1]w\_{\text{cons}}\in[0,1] penalizes contradictory evidence. This difference quantifies how much the evidence supports the answer—positive values indicate support, near-zero values suggest evidence is being ignored, and negative values indicate conflict.

#### Perplexity decomposition.

Beyond aggregate capacity, we extract features that decompose *how* models use evidence:

* •

  LQ=log⁡pθ​(A∗∣Q)L\_{Q}=\log p\_{\theta}(A^{\*}\mid Q): Answer likelihood without evidence
* •

  LQ​E=log⁡pθ​(A∗∣Q,E)L\_{QE}=\log p\_{\theta}(A^{\*}\mid Q,E): Answer likelihood with evidence
* •

  Δ​L=LQ​E−LQ\Delta L=L\_{QE}-L\_{Q}: Capacity lift (how much evidence helps)
* •

  ratio=LQ​E/LQ\text{ratio}=L\_{QE}/L\_{Q}: Normalized capacity measure
* •

  pmaxp\_{\max}: Maximum token probability (model confidence)

These features enable the model to learn fine-grained patterns about evidence utilization that aggregate measures miss.

### 3.5 Calibrated Hallucination Model

Guided by the entropy–capacity design prior established above, we now define the operational detector. Given feature vector 𝐱=(H,Ceff,LQ,LQ​E,Δ​L,ratio,pmax)⊤\mathbf{x}=(H,C\_{\text{eff}},L\_{Q},L\_{QE},\Delta L,\text{ratio},p\_{\max})^{\top} and labeled data, we fit a logistic regression model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^hall=σ​(𝐰⊤​𝐱+β)\hat{p}\_{\text{hall}}=\sigma(\mathbf{w}^{\top}\mathbf{x}+\beta) |  | (5) |

with L2L\_{2} regularization and balanced class weights.

## 4 Experiments

### 4.1 Dataset Construction

We construct 100 financial QA pairs from SEC filings (10-K, 10-Q) and earnings call transcripts. Each pair consists of a query, evidence passage, and answer. We create both grounded and hallucinated variants for each pair, yielding 200 balanced samples (100 hallucinated, 100 clean).

We generate hallucinated answers through four perturbation types: (1) *wrong numbers*: changing numeric values by 10–50%; (2) *entity swaps*: substituting company or executive names; (3) *contradictions*: inverting directional claims (e.g., “increased” →\rightarrow “decreased”); and (4) *fabrications*: introducing facts absent from evidence. We manually verify each example to ensure hallucinated answers are fluent but factually inconsistent with the evidence.

### 4.2 Primary Evaluation: GPT-3.5-turbo

#### Setup.

We compute H^\hat{H} from K=10K=10 samples at temperature 0.7 using the fact-clustering procedure. We extract perplexity features using OpenAI’s API with logprobs=True. We evaluate using stratified 5-fold cross-validation, ensuring each fold preserves the 50/50 hallucinated/clean split. We train logistic regression with L2L\_{2} regularization (C=1.0C=1.0) and balanced class weights. All model training and threshold selection (F1-optimizing threshold) is performed on training folds only; metrics are reported on held-out folds and averaged. For statistical significance, we use a bootstrap test (1000 iterations with replacement) over the full dataset to estimate AUC confidence intervals.

#### Results.

Table [1](https://arxiv.org/html/2512.03107v1#S4.T1 "Table 1 ‣ Results. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") reports detection performance. ECLIPSE achieves ROC AUC of 0.891 and average precision of 0.89. Bootstrap confidence intervals (1000 resamples) show ECLIPSE AUC of [0.842, 0.933] compared to entropy-only baseline [0.423, 0.578]. The intervals do not overlap, confirming statistically significant improvement (p<0.05p<0.05). Figure [1](https://arxiv.org/html/2512.03107v1#S4.F1 "Figure 1 ‣ Results. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") compares ECLIPSE to baseline methods, showing substantial improvement over entropy-only approaches and competitive performance with methods requiring hidden state access. Figure [4](https://arxiv.org/html/2512.03107v1#S4.F4 "Figure 4 ‣ Coverage analysis. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") demonstrates that at 30% coverage, ECLIPSE reduces hallucination rate by 92% relative to entropy-only detection.

Table 1: ECLIPSE hallucination detection performance with GPT-3.5-turbo on financial QA (n=200n=200 balanced samples). Bootstrap confidence intervals computed from 1000 resamples.

|  |  |
| --- | --- |
| Metric | Value |
| ROC AUC | 0.891±0.0230.891\pm 0.023 |
| Bootstrap 95% CI | [0.842,0.933][0.842,0.933] |
| Average Precision | 0.892±0.0180.892\pm 0.018 |
| Precision | 0.809±0.0340.809\pm 0.034 |
| Recall | 0.930±0.0290.930\pm 0.029 |
| F1 Score | 0.865±0.0250.865\pm 0.025 |
| Entropy-only baseline | |
| ROC AUC | 0.501±0.0390.501\pm 0.039 |
| Bootstrap 95% CI | [0.423,0.578][0.423,0.578] |

![Refer to caption](x1.png)


Figure 1: ROC curves for ECLIPSE and entropy-only baseline on our financial QA dataset. ECLIPSE achieves AUC of 0.89, substantially outperforming the entropy-only baseline (0.50). The shaded region indicates the area under the ECLIPSE curve.

#### Coefficient analysis.

Table [2](https://arxiv.org/html/2512.03107v1#S4.T2 "Table 2 ‣ Coefficient analysis. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") shows learned coefficients with theoretical predictions. Six of seven features match expected signs. The perplexity decomposition features (LQ​EL\_{QE}: +1.73, Δ​L\Delta L: −1.60-1.60, ratio: −1.76-1.76) exhibit the largest magnitudes, confirming they drive discrimination. Figure [2](https://arxiv.org/html/2512.03107v1#S4.F2 "Figure 2 ‣ Coefficient analysis. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") visualizes these coefficients.

Table 2: Learned coefficients for ECLIPSE with GPT-3.5-turbo. We indicate whether each coefficient matches the theoretically expected sign. Six of seven features match predictions.

| Feature | Coefficient | Expected Sign | Match |
| --- | --- | --- | --- |
| HH (entropy) | +0.595+0.595 | ++ | ✓ |
| CeffC\_{\text{eff}} (capacity) | −0.708-0.708 | −- | ✓ |
| LQL\_{Q} | +0.673+0.673 | ++ | ✓ |
| LQ​EL\_{QE} | +1.728+1.728 | ++ | ✓ |
| Δ​L\Delta L (capacity lift) | −1.604-1.604 | −- | ✓ |
| ratio | −1.756-1.756 | −- | ✓ |
| pmaxp\_{\max} | +0.796+0.796 | −- | ×\times |

![Refer to caption](x2.png)


Figure 2: Learned coefficients sorted by absolute magnitude. Green bars indicate coefficients matching theoretical predictions; the red bar (pmaxp\_{\max}) shows an unexpected positive sign. The perplexity decomposition features (LQ​EL\_{QE}, ratio, Δ​L\Delta L) dominate, confirming that evidence utilization drives detection.

The positive coefficient for pmaxp\_{\max} (expected negative) reveals an interesting finding: high token confidence predicts *increased* hallucination risk in our data. This aligns with the “overconfidence” phenomenon noted by Xiong et al. [xiong2024can], where models produce peaked distributions over memorized but contextually inappropriate content.

#### Ablation study.

Table [3](https://arxiv.org/html/2512.03107v1#S4.T3 "Table 3 ‣ Ablation study. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") and Figure [3](https://arxiv.org/html/2512.03107v1#S4.F3 "Figure 3 ‣ Ablation study. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") decompose feature contributions. Entropy alone achieves AUC 0.50; adding capacity improves to 0.68 (+0.18); adding perplexity decomposition reaches 0.89 (+0.21). Each component provides meaningful lift.

Table 3: Ablation study showing contribution of each feature group. Each row adds features to the previous configuration. Numbers from final model configuration with bootstrap validation.

| Features | AUC | Improvement |
| --- | --- | --- |
| HH only | 0.50 | — |
| +Ceff+C\_{\text{eff}} | 0.68 | +0.18 |
| +LQ,LQ​E+L\_{Q},L\_{QE} | 0.81 | +0.13 |
| +Δ​L+\Delta L, ratio, pmaxp\_{\max} (Full) | 0.89 | +0.08 |

![Refer to caption](x3.png)


Figure 3: Ablation study showing incremental AUC improvement as features are added. Entropy alone achieves 0.50; capacity adds +0.18; perplexity decomposition adds +0.21 more. The full model achieves 0.89, representing a 78% relative improvement over entropy-only detection.

#### Coverage analysis.

For deployment scenarios where models must abstain on uncertain predictions, we evaluate coverage versus hallucination rate trade-offs. Figure [4](https://arxiv.org/html/2512.03107v1#S4.F4 "Figure 4 ‣ Coverage analysis. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") shows that ECLIPSE substantially outperforms entropy-only detection across all coverage levels. At 30% coverage (accepting only the most confident 30% of predictions), ECLIPSE achieves 3.3% hallucination rate compared to entropy-only’s 43.3%—a 92% relative reduction. Even at 90% coverage, ECLIPSE maintains 44.4% hallucination rate versus 51.1% for entropy-only, demonstrating consistent improvement across the coverage spectrum.

![Refer to caption](x4.png)


Figure 4: Coverage vs hallucination rate for ECLIPSE and entropy-only baseline. At any given coverage level, ECLIPSE achieves substantially lower hallucination rates. At 30% coverage, ECLIPSE reduces hallucination rate by 92% relative to entropy-only detection (3.3% vs 43.3%).

### 4.3 Mechanism Validation: Claude-3-Haiku Ablation

To test whether ECLIPSE depends specifically on access to real log probabilities, we conduct an ablation using Claude-3-Haiku, which does not expose token-level log probabilities through its API. We estimate log probabilities heuristically based on answer properties, providing noisy proxies for true values.

Table [4](https://arxiv.org/html/2512.03107v1#S4.T4 "Table 4 ‣ 4.3 Mechanism Validation: Claude-3-Haiku Ablation ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") reports results. AUC drops from 0.89 to 0.59—statistically above chance (bootstrap SE ≈\approx 0.02) but operationally weak, representing only a modest improvement over random guessing. More revealing is the coefficient analysis in Table [5](https://arxiv.org/html/2512.03107v1#S4.T5 "Table 5 ‣ 4.3 Mechanism Validation: Claude-3-Haiku Ablation ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") and Figure [5](https://arxiv.org/html/2512.03107v1#S4.F5 "Figure 5 ‣ 4.3 Mechanism Validation: Claude-3-Haiku Ablation ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%"): magnitudes collapse by 90–96%, and the key feature Δ​L\Delta L flips sign.

Table 4: ECLIPSE performance with Claude-3-Haiku using estimated log probabilities (n=800n=800 samples). Performance drops substantially compared to GPT-3.5-turbo with real log probabilities.

| Metric | Value |
| --- | --- |
| ROC AUC | 0.593 |
| Average Precision | 0.604 |
| F1 Score | 0.595 |




Table 5: Coefficient comparison between GPT-3.5-turbo (real log probabilities) and Claude-3-Haiku (estimated). The ratio column shows what fraction of the GPT coefficient magnitude is retained. Coefficients collapse dramatically when log probabilities are unavailable.

| Feature | GPT-3.5 | Claude | Retained |
| --- | --- | --- | --- |
| HH | +0.595+0.595 | +0.051+0.051 | 9% |
| CeffC\_{\text{eff}} | −0.708-0.708 | −0.335-0.335 | 47% |
| LQL\_{Q} | +0.673+0.673 | +0.110+0.110 | 16% |
| LQ​EL\_{QE} | +1.728+1.728 | +0.070+0.070 | 4% |
| Δ​L\Delta L | −1.604-1.604 | +0.070+0.070 | (wrong sign) |
| ratio | −1.756-1.756 | −0.129-0.129 | 7% |
| pmaxp\_{\max} | +0.796+0.796 | +0.000+0.000 | 0% |

![Refer to caption](x5.png)


Figure 5: Coefficient comparison between GPT-3.5-turbo (real log probabilities) and Claude-3-Haiku (estimated). Blue bars show GPT coefficients; orange bars show Claude coefficients. Red percentages indicate what fraction of the GPT magnitude is retained. Coefficients collapse by 90–96% when real log probabilities are unavailable, and Δ​L\Delta L flips sign, confirming that ECLIPSE is logprob-native.

This ablation provides strong evidence that ECLIPSE is *logprob-native*. The method exploits structured token-level uncertainty; when that signal degrades to noise, the learned “physics” disappears and the model reduces to near-random guessing. This validates our theoretical motivation: perplexity decomposition is not incidental but essential.

### 4.4 Feature Visualization

Figure [6](https://arxiv.org/html/2512.03107v1#S4.F6 "Figure 6 ‣ 4.4 Feature Visualization ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") shows the distribution of key features for clean versus hallucinated samples. Hallucinated answers exhibit higher entropy, lower capacity, and smaller capacity lift—consistent with the theoretical model and learned coefficient signs.

![Refer to caption](x6.png)


Figure 6: Feature distributions for clean (green) and hallucinated (red) samples. (a) Hallucinated answers show higher semantic entropy. (b) Hallucinated answers show lower effective capacity. (c) Hallucinated answers show smaller or negative capacity lift, indicating the model ignores evidence.

Figure [7](https://arxiv.org/html/2512.03107v1#S4.F7 "Figure 7 ‣ 4.4 Feature Visualization ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") visualizes the joint distribution of entropy HH and capacity lift Δ​L\Delta L, the two features with the largest coefficient magnitudes. Clean samples cluster in the upper-left (low entropy, high evidence use); hallucinated samples cluster in the lower-right (high entropy, low evidence use). The learned decision boundary achieves clean separation.

![Refer to caption](x7.png)


Figure 7: Scatter plot of semantic entropy (HH) versus capacity lift (Δ​L\Delta L) with fitted decision boundary. Clean samples (green) exhibit low entropy and high capacity lift; hallucinated samples (red) exhibit high entropy and low or negative capacity lift. The boundary achieves clear separation, illustrating the entropy–capacity trade-off.

### 4.5 Comparison to Prior Work

Table [6](https://arxiv.org/html/2512.03107v1#S4.T6 "Table 6 ‣ 4.5 Comparison to Prior Work ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") contextualizes ECLIPSE relative to published hallucination detection methods. Important caveat: These ranges come from different papers evaluated on different datasets; they are not direct comparisons on shared benchmarks. We do not claim to match or exceed these methods on standardized test sets. Our 0.89 AUC on financial QA suggests the logprob-native approach is promising, but establishing performance on common benchmarks (e.g., TruthfulQA, HaluEval) remains important future work. The primary contribution is the interpretable, logprob-native mechanism, not a claim of universal superiority.

Table 6: Qualitative comparison to prior hallucination detection methods. Important: Numbers are from original publications evaluated on different datasets (SelfCheckGPT on WikiBio, Semantic Entropy on TriviaQA, SEPs on various benchmarks). These are not direct comparisons on shared test sets. Our results (0.89 AUC) are on the financial QA dataset described in Section [4](https://arxiv.org/html/2512.03107v1#S4 "4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%"). We include this table for orientation only; establishing performance on standardized benchmarks remains future work.

| Method | Access | AUC Range | Source |
| --- | --- | --- | --- |
| SelfCheckGPT | Black-box | 0.78–0.82 | [manakul2023selfcheckgpt] |
| Semantic Entropy | Grey-box | 0.80–0.85 | [kuhn2023semantic] |
| SEPs | White-box | 0.85–0.90 | [kossen2024semantic] |
| ECLIPSE (ours) | Grey-box | 0.89 | This work |

## 5 Discussion

#### The overconfidence finding.

The positive pmaxp\_{\max} coefficient contradicts the naive expectation that high confidence indicates correctness. Instead, we find that high token-level confidence predicts increased hallucination risk. This aligns with observations that models are “confidently wrong” when hallucinating [xiong2024can]—producing peaked distributions over memorized but contextually inappropriate content. For practitioners, this suggests treating raw confidence as a risk factor rather than a safety signal.

#### Why perplexity decomposition works.

The ablation in Table [3](https://arxiv.org/html/2512.03107v1#S4.T3 "Table 3 ‣ Ablation study. ‣ 4.2 Primary Evaluation: GPT-3.5-turbo ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") shows that perplexity features contribute +0.21 AUC beyond entropy and capacity alone (0.68 →\rightarrow 0.89). These features capture whether the model actually *uses* evidence: a large positive Δ​L\Delta L indicates evidence improved answer likelihood (grounded); near-zero Δ​L\Delta L indicates evidence was ignored (hallucination risk). This is precisely the failure mode that plagues retrieval-augmented systems [shi2023large].

#### Logprob-native mechanism.

The Claude ablation (Figure [5](https://arxiv.org/html/2512.03107v1#S4.F5 "Figure 5 ‣ 4.3 Mechanism Validation: Claude-3-Haiku Ablation ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%")) demonstrates that ECLIPSE is not performing generic calibration. When log probabilities are estimated noise, coefficient magnitudes collapse 90–96% and key features flip sign. The method requires access to *meaningful* token-level uncertainty; it cannot extract signal from uninformative proxies. This has implications for API providers: exposing log probabilities enables substantially better hallucination detection.

#### Cross-paper comparisons and benchmarking.

Table [6](https://arxiv.org/html/2512.03107v1#S4.T6 "Table 6 ‣ 4.5 Comparison to Prior Work ‣ 4 Experiments ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") compares our results to prior work, but these numbers come from different papers on different datasets. We do not claim to match or exceed these methods on standardized benchmarks; such evaluation requires shared test sets and identical experimental protocols. Our 0.89 AUC on financial QA suggests the approach is promising, but establishing performance relative to baselines on common benchmarks (e.g., TruthfulQA, HaluEval) remains important future work. The primary contribution is the interpretable, logprob-native mechanism, not a claim of universal superiority.

## 6 Limitations

#### Scale and domain.

We evaluate on 200 samples from financial QA with primarily synthetic hallucinations (constructed perturbations). While results are statistically significant (bootstrap 95% CI for AUC: [0.85, 0.93]), this represents a small, controlled case study in a single domain. The dataset does not include naturally occurring model hallucinations at scale, which may exhibit different characteristics. Broader validation requires: (1) naturally hallucinated responses from prompted models, (2) multiple domains beyond finance (medical, legal, open-domain QA), and (3) larger sample sizes (n≥1000n\geq 1000) for tighter confidence intervals and more robust cross-validation. We position this work as a *controlled mechanism study* demonstrating the logprob-native detection principle, not as a comprehensive benchmark evaluation.

#### API dependence.

ECLIPSE requires log probability access, which some APIs (Claude, Gemini) do not expose. The Claude ablation quantifies this limitation: without real log probabilities, performance degrades substantially. This dependency is fundamental to our approach and cannot be circumvented through heuristic estimation.

#### Entropy estimation limitations.

We use K=10K=10 samples at temperature 0.7 to estimate semantic entropy due to API cost constraints. This yields noisy entropy estimates that may miss multimodal structure; larger KK (e.g., 50–100 samples) would likely yield more stable estimates and sharper discrimination. Additionally, our semantic clustering is heuristic (spaCy NER + regex + thresholds) and tailored to financial QA; more robust semantic coders (e.g., entailment models) would likely improve entropy quality.

#### Feature design and potential circularity.

Our capacity feature (CeffC\_{\text{eff}}) includes an explicit contradiction penalty (wconsw\_{\text{cons}}) that is aligned with our labeling protocol (identifying synthetic contradictions). This may inflate performance on this controlled dataset compared to naturally occurring hallucinations. Additionally, features (LQL\_{Q}, LQ​EL\_{QE}, Δ​L\Delta L, ratio) exhibit multicollinearity by construction; while coefficients remain qualitatively stable, absolute magnitudes may be less interpretable than in orthogonal feature sets.

#### Claude ablation confounds.

Our Claude-3-Haiku ablation changes both the model family and the availability of log probabilities; the coefficient collapse is therefore a joint effect of noisy logprob proxies *and* model differences (training data, architecture, API behavior). In future work we plan to simulate logprob unavailability within a single model family to isolate the effect more cleanly. Nonetheless, the dramatic magnitude reduction (90–96%) provides strong evidence that structured token-level uncertainty is essential.

#### Adversarial robustness.

Our capacity estimator measures evidence utilization but does not protect against coherent but globally false evidence. An adversary could craft internally consistent but factually incorrect context that receives high capacity scores. Integration with external fact verification [min2023factscore] remains important for adversarial robustness.

#### Detection versus control.

We focus on hallucination detection. While Theorem [4](https://arxiv.org/html/2512.03107v1#Thmtheorem4 "Theorem 4 (Stability and convexity). ‣ 3.3 Joint Objective and Stability ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%") establishes properties for entropy control, we do not implement explicit control mechanisms (temperature scheduling, constrained decoding). Developing practical controllers that track optimal entropy remains future work.

## 7 Conclusion

We introduced ECLIPSE, a framework for hallucination detection that makes the entropy–capacity trade-off explicit. The key insight is that hallucination risk depends on the relationship between model uncertainty and evidence quality—not uncertainty alone. By decomposing perplexity into features capturing evidence utilization, ECLIPSE achieves 0.89 AUC on our financial QA dataset using only API access.

The controlled Claude ablation validates ECLIPSE as logprob-native: without real log probabilities, performance drops from 0.89 to 0.59 AUC. This demonstrates that perplexity decomposition is essential, not incidental. The interpretable coefficients provide insight into model behavior, revealing that high token confidence paradoxically predicts increased hallucination risk.

For practitioners, ECLIPSE can wrap existing LLMs without modification, providing calibrated hallucination probabilities for selective prediction. The framework offers a verification layer for autonomous systems where understanding when to trust model outputs is critical for safe deployment.

#### Reproducibility.

We plan to release the financial QA dataset, ECLIPSE implementation, and all experimental code upon acceptance to facilitate replication and extension of this work.

## Appendix A Complete Proof of Theorem [4](https://arxiv.org/html/2512.03107v1#Thmtheorem4 "Theorem 4 (Stability and convexity). ‣ 3.3 Joint Objective and Stability ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%")

We prove that under the condition α>λ​a2/8\alpha>\lambda a^{2}/8, the objective ℒtotal​(H∣C,Q)\mathcal{L}\_{\text{total}}(H\mid C,Q) is strictly convex in HH, admits a unique global minimizer, and gradient descent converges from any initialization.

#### Setup.

We write the objective as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒtotal​(H)=α​(H−Hpref)2+λ​σ​(z​(H)),\mathcal{L}\_{\text{total}}(H)=\alpha(H-H\_{\text{pref}})^{2}+\lambda\sigma(z(H)), |  | (6) |

where we suppress the dependence on (C,Q)(C,Q) for clarity and define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | z​(H)=a​(H−Hpref)−b​C+c.z(H)=a(H-H\_{\text{pref}})-bC+c. |  | (7) |

#### First derivative.

We compute the first derivative of ℒtotal\mathcal{L}\_{\text{total}} with respect to HH. Using the chain rule and the identity σ′​(z)=σ​(z)​(1−σ​(z))\sigma^{\prime}(z)=\sigma(z)(1-\sigma(z)):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​ℒtotald​H\displaystyle\frac{d\mathcal{L}\_{\text{total}}}{dH} | =dd​H​[α​(H−Hpref)2]+dd​H​[λ​σ​(z​(H))]\displaystyle=\frac{d}{dH}\left[\alpha(H-H\_{\text{pref}})^{2}\right]+\frac{d}{dH}\left[\lambda\sigma(z(H))\right] |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​α​(H−Hpref)+λ​σ′​(z)⋅d​zd​H\displaystyle=2\alpha(H-H\_{\text{pref}})+\lambda\sigma^{\prime}(z)\cdot\frac{dz}{dH} |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​α​(H−Hpref)+λ​a​σ​(z)​(1−σ​(z)).\displaystyle=2\alpha(H-H\_{\text{pref}})+\lambda a\sigma(z)(1-\sigma(z)). |  | (10) |

#### Second derivative.

We differentiate again to obtain the second derivative:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d2​ℒtotald​H2\displaystyle\frac{d^{2}\mathcal{L}\_{\text{total}}}{dH^{2}} | =dd​H​[2​α​(H−Hpref)]+dd​H​[λ​a​σ​(z)​(1−σ​(z))]\displaystyle=\frac{d}{dH}\left[2\alpha(H-H\_{\text{pref}})\right]+\frac{d}{dH}\left[\lambda a\sigma(z)(1-\sigma(z))\right] |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​α+λ​a⋅dd​H​[σ​(z)​(1−σ​(z))].\displaystyle=2\alpha+\lambda a\cdot\frac{d}{dH}\left[\sigma(z)(1-\sigma(z))\right]. |  | (12) |

We compute the derivative of σ​(z)​(1−σ​(z))\sigma(z)(1-\sigma(z)) with respect to HH. Let u=σ​(z)u=\sigma(z). Then:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​H​[u​(1−u)]\displaystyle\frac{d}{dH}[u(1-u)] | =d​ud​H​(1−u)+u​d​(1−u)d​H\displaystyle=\frac{du}{dH}(1-u)+u\frac{d(1-u)}{dH} |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =d​ud​H​(1−u)−u​d​ud​H\displaystyle=\frac{du}{dH}(1-u)-u\frac{du}{dH} |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =d​ud​H​(1−2​u).\displaystyle=\frac{du}{dH}(1-2u). |  | (15) |

Since d​ud​H=σ′​(z)⋅d​zd​H=a​σ​(z)​(1−σ​(z))=a​u​(1−u)\frac{du}{dH}=\sigma^{\prime}(z)\cdot\frac{dz}{dH}=a\sigma(z)(1-\sigma(z))=au(1-u), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​H​[u​(1−u)]=a​u​(1−u)​(1−2​u).\frac{d}{dH}[u(1-u)]=au(1-u)(1-2u). |  | (16) |

Substituting back:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d2​ℒtotald​H2\displaystyle\frac{d^{2}\mathcal{L}\_{\text{total}}}{dH^{2}} | =2​α+λ​a⋅a​σ​(z)​(1−σ​(z))​(1−2​σ​(z))\displaystyle=2\alpha+\lambda a\cdot a\sigma(z)(1-\sigma(z))(1-2\sigma(z)) |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​α+λ​a2​σ​(z)​(1−σ​(z))​(1−2​σ​(z)).\displaystyle=2\alpha+\lambda a^{2}\sigma(z)(1-\sigma(z))(1-2\sigma(z)). |  | (18) |

#### Bounding the nonlinear term.

We establish a bound on |σ​(z)​(1−σ​(z))​(1−2​σ​(z))||\sigma(z)(1-\sigma(z))(1-2\sigma(z))|.

Let u=σ​(z)∈(0,1)u=\sigma(z)\in(0,1). We seek to bound |f​(u)||f(u)| where f​(u)=u​(1−u)​(1−2​u)f(u)=u(1-u)(1-2u).

First, we note that u​(1−u)∈(0,0.25]u(1-u)\in(0,0.25] for u∈(0,1)u\in(0,1), with maximum at u=0.5u=0.5.

Second, |1−2​u|∈[0,1]|1-2u|\in[0,1] for u∈[0,1]u\in[0,1], with maximum at u∈{0,1}u\in\{0,1\}.

To find the maximum of |f​(u)||f(u)|, we take the derivative and set it to zero:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(u)\displaystyle f(u) | =u​(1−u)​(1−2​u)\displaystyle=u(1-u)(1-2u) |  | (19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(u−u2)​(1−2​u)\displaystyle=(u-u^{2})(1-2u) |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =u−2​u2−u2+2​u3\displaystyle=u-2u^{2}-u^{2}+2u^{3} |  | (21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =u−3​u2+2​u3.\displaystyle=u-3u^{2}+2u^{3}. |  | (22) |

Taking the derivative:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f′​(u)\displaystyle f^{\prime}(u) | =1−6​u+6​u2\displaystyle=1-6u+6u^{2} |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =6​u2−6​u+1.\displaystyle=6u^{2}-6u+1. |  | (24) |

Setting f′​(u)=0f^{\prime}(u)=0 and solving via the quadratic formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u=6±36−2412=6±1212=12±36.u=\frac{6\pm\sqrt{36-24}}{12}=\frac{6\pm\sqrt{12}}{12}=\frac{1}{2}\pm\frac{\sqrt{3}}{6}. |  | (25) |

This yields u1=12−36≈0.211u\_{1}=\frac{1}{2}-\frac{\sqrt{3}}{6}\approx 0.211 and u2=12+36≈0.789u\_{2}=\frac{1}{2}+\frac{\sqrt{3}}{6}\approx 0.789.

Evaluating at u1u\_{1}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(u1)\displaystyle f(u\_{1}) | =u1​(1−u1)​(1−2​u1)\displaystyle=u\_{1}(1-u\_{1})(1-2u\_{1}) |  | (26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈0.211⋅0.789⋅0.578\displaystyle\approx 0.211\cdot 0.789\cdot 0.578 |  | (27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈0.096.\displaystyle\approx 0.096. |  | (28) |

Evaluating at u2u\_{2}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(u2)\displaystyle f(u\_{2}) | =u2​(1−u2)​(1−2​u2)\displaystyle=u\_{2}(1-u\_{2})(1-2u\_{2}) |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈0.789⋅0.211⋅(−0.578)\displaystyle\approx 0.789\cdot 0.211\cdot(-0.578) |  | (30) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈−0.096.\displaystyle\approx-0.096. |  | (31) |

Therefore, |f​(u)|≤16​3≈0.096<0.25|f(u)|\leq\frac{1}{6\sqrt{3}}\approx 0.096<0.25 for all u∈(0,1)u\in(0,1).

For a simpler (though looser) bound sufficient for our purposes, we use:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |u​(1−u)​(1−2​u)|≤u​(1−u)⋅|1−2​u|≤0.25⋅1=0.25.|u(1-u)(1-2u)|\leq u(1-u)\cdot|1-2u|\leq 0.25\cdot 1=0.25. |  | (32) |

#### Establishing strict convexity.

Using the bound |σ​(z)​(1−σ​(z))​(1−2​σ​(z))|≤0.25|\sigma(z)(1-\sigma(z))(1-2\sigma(z))|\leq 0.25, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d2​ℒtotald​H2≥2​α−λ​a2⋅0.25=2​α−λ​a24.\frac{d^{2}\mathcal{L}\_{\text{total}}}{dH^{2}}\geq 2\alpha-\lambda a^{2}\cdot 0.25=2\alpha-\frac{\lambda a^{2}}{4}. |  | (33) |

For the second derivative to be strictly positive for all HH, we require:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​α−λ​a24>0⇔α>λ​a28.2\alpha-\frac{\lambda a^{2}}{4}>0\quad\Leftrightarrow\quad\alpha>\frac{\lambda a^{2}}{8}. |  | (34) |

#### Conclusions.

Under the condition α>λ​a2/8\alpha>\lambda a^{2}/8:

1. 1.

   Strict convexity: Since d2​ℒtotald​H2>0\frac{d^{2}\mathcal{L}\_{\text{total}}}{dH^{2}}>0 for all H∈ℝH\in\mathbb{R}, the function ℒtotal\mathcal{L}\_{\text{total}} is strictly convex in HH.
2. 2.

   Unique minimizer: A strictly convex function on ℝ\mathbb{R} has at most one critical point, which must be a global minimum. Since ℒtotal​(H)→∞\mathcal{L}\_{\text{total}}(H)\to\infty as H→±∞H\to\pm\infty (the quadratic term dominates), a global minimum exists and is unique.
3. 3.

   Gradient descent convergence: For strictly convex functions with Lipschitz continuous gradients, gradient descent with appropriate step size converges to the unique global minimum from any initialization.

This completes the proof. ∎

## Appendix B Hallucination Taxonomy

We categorize hallucinations in our dataset into four types, with approximate frequencies:

| Type | Example | Frequency |
| --- | --- | --- |
| Wrong number | Evidence states revenue of $81.8B; answer claims $94.2B | 35% |
| Entity swap | Evidence discusses Satya Nadella; answer attributes to Sundar Pichai | 25% |
| Contradiction | Evidence states “revenue decreased”; answer claims “revenue increased” | 25% |
| Fabrication | Answer includes acquisition or metric not mentioned in evidence | 15% |

Table 7: Hallucination types in our financial QA dataset.

## Appendix C Computational Cost

We report the API cost breakdown for ECLIPSE feature extraction:

| Component | API Calls per Example |
| --- | --- |
| Semantic entropy (K=10K=10 samples) | 10 |
| LQL\_{Q} scoring (no evidence) | 1 |
| LQ​EL\_{QE} scoring (with evidence) | 1 |
| Total | 12 |

Table 8: API calls required per example. At approximately $0.002 per 1K tokens (GPT-3.5-turbo), total cost is roughly $0.01 per example for feature extraction.

## Appendix D Hyperparameter Settings

| Parameter | Value |
| --- | --- |
| Number of samples KK | 10 |
| Temperature for sampling | 0.7 |
| Numeric tolerance for clustering | 1% relative error |
| Logistic regression regularization CC | 1.0 |
| Class weight balancing | Enabled |
| Cross-validation folds | 5 |

Table 9: Hyperparameter settings used in experiments.

## Appendix E Semantic Clustering Algorithm

We provide a detailed specification of the semantic clustering procedure used to compute entropy H^\hat{H}.

#### Step 1: Fact extraction.

For each generated answer AiA\_{i} (i=1,…,Ki=1,\ldots,K):

1. 1.

   Extract named entities (companies, people, locations) using spaCy v3.5 NER.
2. 2.

   Identify numeric values and their associated units via regex patterns.
3. 3.

   Extract (entity, attribute, value) triples. For example, from “Microsoft’s revenue increased to $211B,” we extract: (Microsoft, revenue, 211B).
4. 4.

   Normalize numeric values to three significant figures.
5. 5.

   Identify directional claims (increased, decreased, stable) via keyword matching.

#### Step 2: Cluster assignment.

We assign answers AiA\_{i} and AjA\_{j} to the same cluster CkC\_{k} if:

1. 1.

   Entity sets overlap by ≥50%\geq 50\% (Jaccard similarity).
2. 2.

   All numeric values match within 1% relative error.
3. 3.

   Directional claims are consistent (both say “increased” or both say “decreased”).

#### Step 3: Entropy computation.

Given clusters {C1,…,Cm}\{C\_{1},\ldots,C\_{m}\}, we compute empirical probabilities pj=|Cj|/Kp\_{j}=|C\_{j}|/K and semantic entropy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^=−∑j=1mpj​log⁡pj.\hat{H}=-\sum\_{j=1}^{m}p\_{j}\log p\_{j}. |  | (35) |

#### Edge cases.

* •

  If an answer contains multiple conflicting facts, we split it into sub-answers and assign each to the appropriate cluster.
* •

  If no numeric or entity facts are extracted (rare for financial QA), we fall back to exact string matching with case normalization.

## Appendix F Logistic Regression Details

We fit the calibrated hallucination model using scikit-learn 1.3.0 with the following settings:

* •

  Solver: lbfgs (limited-memory BFGS)
* •

  Regularization: ℓ2\ell\_{2} penalty with C=1.0C=1.0
* •

  Class weights: Balanced (inversely proportional to class frequencies)
* •

  Maximum iterations: 1000
* •

  Feature scaling: StandardScaler (zero mean, unit variance) applied before regression

The wconsw\_{\text{cons}} term in Eq. ([4](https://arxiv.org/html/2512.03107v1#S3.E4 "In Perplexity-based capacity. ‣ 3.4 Estimating Entropy and Capacity ‣ 3 Method: ECLIPSE ‣ Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%")) is computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wcons={1.0if no facts in ​A∗​ contradict ​E0.5if some facts contradict ​E0.0if all facts contradict ​Ew\_{\text{cons}}=\begin{cases}1.0&\text{if no facts in }A^{\*}\text{ contradict }E\\ 0.5&\text{if some facts contradict }E\\ 0.0&\text{if all facts contradict }E\end{cases} |  | (36) |

Contradiction detection uses the same fact extraction pipeline: we check whether extracted triples from A∗A^{\*} directly conflict with triples from EE (e.g., opposite directional claims about the same entity-attribute pair).