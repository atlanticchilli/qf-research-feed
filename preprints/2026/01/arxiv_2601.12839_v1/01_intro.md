---
authors:
- Gyuyeon Na
- Minjung Park
- Soyoun Kim
- Jungbin Shin
- Sangmi Chai
doc_id: arxiv:2601.12839v1
family_id: arxiv:2601.12839
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under
  Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded
  Context and Path-Level Explanations
url_abs: http://arxiv.org/abs/2601.12839v1
url_html: https://arxiv.org/html/2601.12839v1
venue: arXiv q-fin
version: 1
year: 2026
---


Gyuyeon Na1
These authors contributed equally to this work.
  
Minjung Park211footnotemark: 1
  
Soyoun Kim111footnotemark: 1
  
Jungbin Shin1
  
Sangmi Chai1,3
  
1AI and Business Analytics, Ewha Womans University, Seoul, Republic of Korea
  
2Department of Business Administration, Kumoh National Institute of Technology, Gumi, Republic of Korea
  
3Coretrustlink, Seoul, Republic of Korea
  
amy-na@ewha.ac.kr,
mjpark@kumoh.ac.kr,
sykim07@ewha.ac.kr,
patra33@ewha.ac.kr ,
smchai@ewha.ac.kr
Corresponding author.

###### Abstract

Detecting anomalous trajectories in decentralized crypto-networks is fundamentally challenged by extreme label scarcity and the adaptive evasion strategies of illicit actors.
While Graph Neural Networks (GNNs) effectively capture local structural patterns, they struggle to internalize multi-hop, logic-driven motifs—such as fund dispersal and layering—that characterize sophisticated money laundering, limiting their forensic accountability under regulations like the FATF Travel Rule.

To address this limitation, we propose *Relational Domain-Logic Integration (RDLI)*, a framework that embeds expert-derived heuristics as differentiable, logic-aware latent signals within representation learning.
Unlike static rule-based approaches, RDLI enables the detection of complex transactional flows that evade standard message passing.
To further account for market volatility, we incorporate a *Retrieval-Grounded Context (RGC)* module that conditions anomaly scoring on regulatory and macroeconomic context, mitigating false positives caused by benign regime shifts. Under extreme label scarcity (0.01%), RDLI outperforms state-of-the-art GNN baselines by 28.9% in F1-score.
A micro-expert user study (n=24n=24) further confirms that RDLI’s path-level explanations significantly improve trustworthiness, perceived usefulness, and clarity compared to existing methods (p<0.001p<0.001), highlighting the importance of integrating domain logic with contextual grounding for both accuracy and explainability.

## 1 Introduction

The rapid proliferation of decentralized finance (DeFi) has introduced unprecedented challenges to global financial stability, necessitating a paradigm shift in anomaly detection systems. Under the updated FATF Travel Rule, cryptocurrency service providers are no longer judged solely on detection accuracy; they are now mandated to provide interpretable and verifiable rationales for every flagged transaction. Consequently, modern anomaly detection has evolved from a purely predictive task into a multi-dimensional challenge that demands both high precision and regulatory-grade auditability.

However, satisfying these dual requirements is particularly arduous in the cryptocurrency domain due to two structural barriers. First, *extreme label scarcity* persists as a defining characteristic: illicit actors continuously evolve their tactics, rendering historical labels rapidly obsolete and leaving only a minute fraction of reliable ground truth for training. Second, although contemporary Graph Neural Networks (GNNs) are effective at capturing localized interactions, they frequently suffer from inherent *“black-box” limitations*. As a result, they fail to decode long-horizon, logic-driven motifs—such as complex fund dispersal and layering patterns—that are emblematic of sophisticated financial malfeasance. This disconnect creates a critical mismatch between purely data-driven modeling approaches and the practical interpretive needs of forensic investigators.

To bridge this gap, we propose *Relational Domain-Logic Integration (RDLI)*, a novel framework that transcends the limitations of standard message-passing architectures by embedding expert-derived heuristics directly into the representation learning process. Our key contributions are three-fold:

* •

  Logic-Aware Latent Signals. We formalize expert typologies into differentiable, logic-aware latent signals, enabling the recovery of multi-hop flow dynamics that conventional GNNs frequently bypass.
* •

  Retrieval-Grounded Context (RGC). We introduce a contextual conditioning module that integrates real-time regulatory updates and macroeconomic shifts, effectively filtering out *benign regime changes* that commonly induce false positives in volatile cryptocurrency markets.
* •

  Path-Level Explainability. Unlike post-hoc attribution methods such as SHAP, RDLI generates causal, path-level explanations that directly map flagged activities to salient subgraphs and domain-logic cues, ensuring audit-ready transparency.

Rigorous evaluations on large-scale datasets demonstrate that, even under extreme label scarcity (0.01%), RDLI achieves an F1-score improvement of 28.9% over GNN-based baselines. In addition, a simulated forensic review with a micro-expert panel (n=24n=24) shows that the proposed approach significantly improves *Trustworthiness (TR)* and *Perceived Usefulness (PU)* compared to conventional feature-centric explanations, aligning with emerging regulatory and domain requirements Takei and Shudo ([2024](https://arxiv.org/html/2601.12839v1#bib.bib9 "FATF travel rule’s technical challenges and solution taxonomy")); Chen et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib32 "Health insurance fraud detection: the role of feature engineering and preprocessing techniques")).

Together, these results underscore the effectiveness of fusing domain-specific logic with contextual grounding to support robust, explainable, and institution-ready financial monitoring systems.

## 2 Related Work

### 2.1 Anomaly Detection under Structural Scarcity

Anomaly detection in financial transaction systems is fundamentally constrained by severe label scarcity, as anomalous activities are rare and often confirmed only through delayed investigations Chandola et al. ([2009](https://arxiv.org/html/2601.12839v1#bib.bib18 "Anomaly detection: a survey")); Carcillo et al. ([2021](https://arxiv.org/html/2601.12839v1#bib.bib25 "Scarff: a scalable framework for streaming credit card fraud detection")). This challenge is further compounded by the rapid evolution of illicit strategies, which renders historical labels obsolete and undermines the assumptions of supervised learning in operational settings Guidotti and others ([2019](https://arxiv.org/html/2601.12839v1#bib.bib20 "A survey of methods for explaining black box models")); Weber et al. ([2019](https://arxiv.org/html/2601.12839v1#bib.bib45 "Anti-money laundering in bitcoin: experimenting with graph convolutional networks for financial forensics")).

Recent work shows that graph-based detection models suffer from representation collapse and unstable generalization when label availability falls below critical thresholds Dou and others ([2020](https://arxiv.org/html/2601.12839v1#bib.bib19 "Enhancing graph neural network-based fraud detectors against camouflaged fraudsters")); Wang et al. ([2021](https://arxiv.org/html/2601.12839v1#bib.bib30 "Graph neural networks in financial fraud detection: a survey")). Even with data augmentation or semi-supervised extensions, performance often saturates under extreme scarcity Chalapathy and Chawla ([2022](https://arxiv.org/html/2601.12839v1#bib.bib22 "Deep learning for anomaly detection: a review")); Hu et al. ([2023](https://arxiv.org/html/2601.12839v1#bib.bib47 "Transaction-based classification and detection of illicit activities on blockchain")).

While some approaches leverage structural flow patterns or heuristic-driven signals to mitigate these limitations Li et al. ([2020](https://arxiv.org/html/2601.12839v1#bib.bib46 "FlowScope: spotting money laundering based on graphs")); Cheng et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib35 "Graph neural networks for financial fraud detection: a review")), they typically assume sufficient data completeness and fail to maintain robustness when both labels and reliable priors are scarce. These observations motivate the need for alternative paradigms that can sustain stable generalization under conditions of structural scarcity.

### 2.2 Knowledge-Integrated & Explainable Detection

To overcome data limitations, recent studies have explored the incorporation of expert heuristics into learning-based anomaly detection models. While some approaches treat expert rules as weak supervision or manually engineered features Xu et al. ([2024](https://arxiv.org/html/2601.12839v1#bib.bib24 "Challenges and pitfalls in real-world financial anomaly detection")), they often incur high maintenance costs and exhibit limited adaptability to evolving adversarial strategies Korycki and Krawczyk ([2023](https://arxiv.org/html/2601.12839v1#bib.bib26 "Adversarial concept drift detection under poisoning attacks for robust data stream mining")). In parallel, retrieval-augmented learning (RAL) methods have been proposed to enrich model predictions with external context; however, they primarily improve instance-level awareness and fail to structurally encode expert knowledge required for path-level reasoning Lewis et al. ([2020](https://arxiv.org/html/2601.12839v1#bib.bib23 "Retrieval-augmented generation for knowledge-intensive nlp tasks")).

From a regulatory compliance perspective, anomaly detection systems must also provide auditable and verifiable rationales. Prevailing post-hoc explanation techniques such as SHAP offer only coarse-grained feature attribution and are inherently incapable of capturing the sequential intent underlying money laundering behaviors Lundberg and Lee ([2017](https://arxiv.org/html/2601.12839v1#bib.bib42 "A unified approach to interpreting model predictions")). Although recent logic-based approaches have begun to address these challenges, they largely remain confined to closed-world assumptions and static knowledge representations, limiting their applicability in dynamic, real-world financial environments. These limitations highlight the need for frameworks that jointly integrate expert heuristics with external unstructured context to support both robust detection and regulatory-aligned explainability.

## 3 Proposed Method

We propose a unified *knowledge-guided anomaly detection framework*, termed *Relational Domain-Logic Integration (RDLI)*. As shown in Figure [1](https://arxiv.org/html/2601.12839v1#S3.F1 "Figure 1 ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations"), RDLI encodes expert knowledge into a shared representation layer that is utilized by multiple downstream predictors.

![Refer to caption](architecture3.png)


Figure 1: Overview of the RDLI framework

### 3.1 Expert Knowledge Graph Construction

We employ Large Language Models (LLMs) to automatically generate structured annotations from raw transaction contexts based on expert-defined typologies. These annotations are subsequently transformed into an *Expert Knowledge Graph* designed to capture hierarchical domain logic with high semantic density.

We formalize the Expert Knowledge Graph as a heterogeneous directed graph
𝒢=(𝒱,ℰ,𝒯,ϕ)\mathcal{G}=(\mathcal{V},\mathcal{E},\mathcal{T},\phi),
where 𝒱\mathcal{V} denotes the set of nodes and ℰ\mathcal{E} denotes the set of directed edges encoding hierarchical dependencies.
The node type mapping function ϕ:𝒱→𝒯\phi:\mathcal{V}\rightarrow\mathcal{T} assigns each node to a semantic category
𝒯={AT,SF,ST,KW}\mathcal{T}=\{\mathrm{AT},\mathrm{SF},\mathrm{ST},\mathrm{KW}\},
corresponding to *Anomaly Type*, *Subtype Family*, *Subtype*, and *Keyword*, respectively.

Edges are constructed to enforce a fixed hierarchical structure
AT→SF→ST→KW\mathrm{AT}\rightarrow\mathrm{SF}\rightarrow\mathrm{ST}\rightarrow\mathrm{KW},
ensuring that high-level anomaly concepts are progressively specialized into fine-grained evidential descriptors.

For a transaction xix\_{i}, we define an induced logic path PiP\_{i} as an ordered hierarchical sequence:

|  |  |  |
| --- | --- | --- |
|  | Pi=[vAT(i),vSF(i),vST(i),{vKW(i,k)}k=1Ki],P\_{i}=\bigl[v\_{\mathrm{AT}}^{(i)},\;v\_{\mathrm{SF}}^{(i)},\;v\_{\mathrm{ST}}^{(i)},\;\{v\_{\mathrm{KW}}^{(i,k)}\}\_{k=1}^{K\_{i}}\bigr], |  |

where v∈𝒱v\in\mathcal{V} denotes the concept nodes associated with transaction xix\_{i}, and KiK\_{i} represents the number of keyword-level evidential nodes activated for that transaction.

#### 3.1.1 LLM-based Structured Annotation Generation

In this study, expert typologies are incorporated into a LLM via carefully designed prompts, enabling the automatic generation of *structured, transaction-level annotations* from raw transaction and cluster contexts. We employ *Gemini-2.5-Flash* to produce controlled hierarchical semantic labels, keywords, and concise explanations, which are stored alongside original transaction attributes in a unified schema. The annotation process required 3,378 seconds and consumed 1,585,415 tokens, after which the generated texts were embedded using *text-embedding-004* for retrieval and similarity analysis.

##### Train-only Construction and Leakage Prevention

To enforce strict forecasting principles, the concept graph is constructed exclusively from the training split. Test transactions are projected into the pre-trained *DeepWalk* embedding space, with unseen concepts mapped to zero vectors to prevent information leakage. In addition, label-proximal fields (e.g., *Anomaly Type*) are excluded from direct predictive inputs and used only for structural context modeling.

### 3.2 Event-based Context Modeling

We propose a  Retrieval-Grounded Context (RGC) module to filter benign regime changes. The system extracts narratives from news APIs (e.g., GNews) to form a searchable corpus. Each transaction is vectorized using the Gemini embedding model, and relevant context is retrieved via cosine similarity: This retrieves external evidence (e.g., regulatory warnings) to enrich the latent representation.

|  |  |  |
| --- | --- | --- |
|  | sim​(q,d)=q⋅d‖q‖⋅‖d‖\text{sim}(q,d)=\frac{q\cdot d}{\|q\|\cdot\|d\|} |  |

Algorithm 1  RAG-Augmented LLM Annotation with Concept Graph Embedding and Prediction

Input: Transaction features X={xi}X=\{x\_{i}\}, cluster context C={ci}C=\{c\_{i}\}, expert KB 𝒦\mathcal{K}, event KB ℰ\mathcal{E}
  
Parameters: Train index set ℐt​r\mathcal{I}\_{tr}, test index set ℐt​e\mathcal{I}\_{te}, top-kk retrieval (kK,kE)(k\_{K},k\_{E})
  
Output: Anomaly score or label y^i\hat{y}\_{i} for each transaction

1:  Initialize empty annotation set 𝒜←∅\mathcal{A}\leftarrow\emptyset

2:  for each transaction ii do

3:   qi←BuildQuery​(xi,ci)q\_{i}\leftarrow\mathrm{BuildQuery}(x\_{i},c\_{i})

4:   𝒦i←RetrieveTopK​(qi,𝒦,kK)\mathcal{K}\_{i}\leftarrow\mathrm{RetrieveTopK}(q\_{i},\mathcal{K},k\_{K}) {expert insights (typology chunks)}

5:   ℰi←RetrieveTopK​(qi,ℰ,kE)\mathcal{E}\_{i}\leftarrow\mathrm{RetrieveTopK}(q\_{i},\mathcal{E},k\_{E}) {event evidence (event chunks)}

6:   ai←LLMAnnotate​(xi,ci,𝒦i,ℰi)a\_{i}\leftarrow\mathrm{LLMAnnotate}(x\_{i},c\_{i},\mathcal{K}\_{i},\mathcal{E}\_{i})

7:   Extract (ATi,SFi,STi,{KWi,1..k})(\mathrm{AT}\_{i},\mathrm{SF}\_{i},\mathrm{ST}\_{i},\{\mathrm{KW}\_{i,1..k}\}) from aia\_{i}

8:   𝒜←𝒜∪{ai}\mathcal{A}\leftarrow\mathcal{A}\cup\{a\_{i}\}

9:  end for

10:  Initialize train-only concept graph Gt​r←(𝒱t​r,ℰt​r)G\_{tr}\leftarrow(\mathcal{V}\_{tr},\mathcal{E}\_{tr})

11:  for each i∈ℐt​ri\in\mathcal{I}\_{tr} do

12:   Add nodes {ATi,SFi,STi,KWi,j}\{\mathrm{AT}\_{i},\mathrm{SF}\_{i},\mathrm{ST}\_{i},\mathrm{KW}\_{i,j}\} to 𝒱t​r\mathcal{V}\_{tr}

13:   Add edges ATi→SFi→STi→KWi,j\mathrm{AT}\_{i}\rightarrow\mathrm{SF}\_{i}\rightarrow\mathrm{ST}\_{i}\rightarrow\mathrm{KW}\_{i,j} to ℰt​r\mathcal{E}\_{tr}

14:  end for

15:  Z←DeepWalk​(Gt​r)Z\leftarrow\mathrm{DeepWalk}(G\_{tr}) {concept-level embeddings}

16:  for each transaction ii do

17:   ei←Pool​(Z,ai)e\_{i}\leftarrow\mathrm{Pool}(Z,a\_{i})

18:   ri←Concat​(xi,aic​a​t,ei)r\_{i}\leftarrow\mathrm{Concat}(x\_{i},a\_{i}^{cat},e\_{i})

19:  end for

20:  Train predictor fθf\_{\theta} on {(ri,yi)}i∈ℐt​r\{(r\_{i},y\_{i})\}\_{i\in\mathcal{I}\_{tr}}

21:  for each i∈ℐt​ei\in\mathcal{I}\_{te} do

22:   y^i←fθ​(ri)\hat{y}\_{i}\leftarrow f\_{\theta}(r\_{i})

23:  end for

24:  return {y^i}\{\hat{y}\_{i}\}

### 3.3 Model Architecture

This study adopts the unified knowledge-guided anomaly detection framework outlined in Algorithm [1](https://arxiv.org/html/2601.12839v1#alg1 "Algorithm 1 ‣ 3.2 Event-based Context Modeling ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").

Let 𝐡v∈ℝd\mathbf{h}\_{v}\in\mathbb{R}^{d} be the embedding vector of a node vv learned via DeepWalk. The semantic representation 𝐞i\mathbf{e}\_{i} for transaction ii is computed via an attention-weighted pooling over its associated logic path PiP\_{i}:

|  |  |  |
| --- | --- | --- |
|  | 𝐞i=∑v∈Piαv⋅𝐡v\mathbf{e}\_{i}=\sum\_{v\in P\_{i}}\alpha\_{v}\cdot\mathbf{h}\_{v} |  |

where αv\alpha\_{v} denotes the relevance weight of concept vv.Finally, the unified input vector 𝐫i\mathbf{r}\_{i} for downstream predictors is constructed by concatenating the raw feature vector 𝐱i\mathbf{x}\_{i}, the logic embedding 𝐞i\mathbf{e}\_{i}, and the retrieved context embedding 𝐜i\mathbf{c}\_{i}:

|  |  |  |
| --- | --- | --- |
|  | 𝐫i=Concat​(𝐱i,𝐞i,𝐜i)\mathbf{r}\_{i}=\text{Concat}(\mathbf{x}\_{i},\mathbf{e}\_{i},\mathbf{c}\_{i}) |  |

#### 3.3.1 Unified Knowledge-Guided Input Representation

For each transaction, we construct a unified feature representation with two components:
(i) *numeric and categorical transaction attributes* (e.g., value, direction, self-transfer flags), with categorical variables one-hot encoded; and
(ii) an optional *semantic embedding* derived from the expert knowledge graph by pooling *DeepWalk embeddings* of the transaction’s structured concepts.

Depending on the experimental setting, the semantic component is either *empty* (*feature-only*), a *graph-based embedding* (*KG*), or a KG embedding augmented via *retrieval-based alignment* (*KG+RAG*). All models share the same unified input format.

#### 3.3.2 Tree-based Predictor

We employ LightGBM as a strong tree-based baseline for tabular anomaly detection, following prior studies that adopt gradient-boosted decision trees for transaction-level anomaly modeling Jia et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib38 "LMAE4Eth: generalizable and robust ethereum fraud detection by exploring transaction semantics and masked graph embedding")).
The model takes the unified input representation as a fixed-length feature vector and learns non-linear decision boundaries through gradient-boosted decision trees.
As LightGBM does not explicitly model temporal or relational dependencies, it serves as a reference point to evaluate the benefits of sequential and graph-aware architectures.

#### 3.3.3 Neural Sequence Predictor

To capture temporal dependencies across transactions, we adopt a gated recurrent unit (GRU)-based neural anomaly model, following prior work on structural–temporal modeling for proactive anomaly detection Park et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib40 "HyPV-lead: proactive early-warning of cryptocurrency anomalies through data-driven structural–temporal modeling")).
Transaction streams are segmented into fixed-length sliding windows, each represented as a sequence of unified input vectors.
The GRU encoder processes each window and summarizes it into a latent representation via the final hidden state, which is subsequently passed to a sigmoid prediction head to estimate anomaly probability  Li et al. ([2019](https://arxiv.org/html/2601.12839v1#bib.bib7 "Reading selectively via binary input gated recurrent unit.")); Tan et al. ([2021](https://arxiv.org/html/2601.12839v1#bib.bib6 "Cooperative joint attentive network for patient outcome prediction on irregular multi-rate multivariate health data.")).

This architecture enables the model to detect anomalous behavior that emerges over multiple consecutive transactions, rather than from isolated events.

#### 3.3.4 Graph Neural Network Predictor

To model relational dependencies among transactions and addresses, we adopt a graph neural network (GNN)-based predictor following prior spatio-temporal graph learning frameworks Ghaffari et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib41 "STM-graph: a python framework for spatio-temporal mapping and graph neural network predictions")). Transactions or addresses are represented as nodes, while edges encode interaction or fund-flow relationships among them. We utilize GraphSAGE Hamilton et al. ([2017](https://arxiv.org/html/2601.12839v1#bib.bib5 "Inductive representation learning on large graphs")) as the GNN backbone to support inductive learning on evolving transaction graphs. Through fixed-size neighborhood sampling and aggregation, GraphSAGE enables efficient generalization to nodes that emerge in the temporal evaluation split.

Each node is initialized with a unified, knowledge-guided feature representation, allowing the GNN to jointly exploit structural dependencies and expert-informed semantic signals.
Compared to sequence-based models, GNNs explicitly model relational and spatial structures that are difficult to capture using time-series representations alone, making them well-suited for anomaly detection in evolving graph settings Wang et al. ([2019](https://arxiv.org/html/2601.12839v1#bib.bib3 "Robust embedding with multi-level structures for link prediction.")); Pareja et al. ([2020](https://arxiv.org/html/2601.12839v1#bib.bib28 "EvolveGCN: evolving graph convolutional networks for dynamic graphs")); Zhao et al. ([2021](https://arxiv.org/html/2601.12839v1#bib.bib2 "CSGNN: contrastive self-supervised graph neural network for molecular interaction prediction.")).

### 3.4 Explanation Scoring

To generate an explanation, we identify the salient subgraph by maximizing the alignment score between the transaction context and the knowledge path. The explanation score S​(Pi)S(P\_{i}) is formulated as:

|  |  |  |
| --- | --- | --- |
|  | S​(Pi)=maxP∈𝒩​(i)⁡(λ1⋅sim​(𝐱i,P)+λ2⋅sim​(ℰi,P))S(P\_{i})=\max\_{P\in\mathcal{N}(i)}\left(\lambda\_{1}\cdot\text{sim}(\mathbf{x}\_{i},P)+\lambda\_{2}\cdot\text{sim}(\mathcal{E}\_{i},P)\right) |  |

where 𝒩​(i)\mathcal{N}(i) is the set of candidate paths and ℰi\mathcal{E}\_{i} is the retrieved event context.

## 4 Experimental Setup

Detailed dataset construction specifications and hyperparameter settings are provided in the supplementary material. To ensure reproducibility, the source code and the stratified dataset subset are included in the supplementary submission.

### 4.1 Dataset and Prerocessing

| Dataset / Component | Details |
| --- | --- |
| LLM-Based Transaction Annotation | Subset: Stratified 0.01% of transactions LLM Role: Semantic inference (non-labeling) Key Fields: anomaly\_type, subtype\_family, subtype direction, is\_self\_transfer, coin\_infer coin, year, source\_file abs\_usd\_value, \_dt, date annotation, keyword1–keyword5 llm\_raw Expert-guided semantic enrichment used for KG construction. |
| Event Dataset | Purpose: Contextual grounding of anomalies Key Fields: event\_id, event\_title, event\_date published\_at, anomaly\_type, coin description, gate\_reason, text\_sample is\_anomaly, llm\_verified Aligns detected transaction patterns with real-world incidents. |
| Expert Knowledge Dataset | Format: Structured CSV knowledge base Key Fields: chunk\_id, chunk\_text sheet\_name, row\_idx Integrated via RAG to retrieve expert-defined typologies and explanations Ensures domain-grounded and interpretable annotations. |

Table 1: Overview of LLM-annotated transaction data, event context, and expert knowledge datasets

Experiments were conducted on a real-world cryptocurrency transaction dataset spanning from January 2020 to December 2024. To simulate extreme label scarcity while preserving the severe class imbalance observed in operational settings, we extracted a stratified subset containing only 0.01% of labeled instances. The dataset encompasses a diverse range of anomalous behaviors, including mixing activities (e.g., CoinJoin and Tornado Cash) and scam-related events (e.g., rug pulls). Detailed dataset statistics are summarized in Table [1](https://arxiv.org/html/2601.12839v1#S4.T1 "Table 1 ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").

To prevent information leakage and ensure a realistic evaluation setting, we applied both address-disjoint and temporal train–test splitting strategies. This experimental design follows established best practices in cryptocurrency anomaly detection and logic-aware learning under non-stationary environments Hoffman et al. ([2018](https://arxiv.org/html/2601.12839v1#bib.bib39 "Metrics for explainable ai: challenges and prospects")); Jia et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib38 "LMAE4Eth: generalizable and robust ethereum fraud detection by exploring transaction semantics and masked graph embedding")); Li et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib29 "Association-focused path aggregation for graph fraud detection")); Lei et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib36 "Large language models for cryptocurrency transaction analysis: a bitcoin case study")); Sun et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib37 "Ethereum fraud detection via joint transaction language model and graph representation learning")); Shyalika et al. ([2025](https://arxiv.org/html/2601.12839v1#bib.bib43 "NSF-map: neurosymbolic multimodal fusion for robust and interpretable anomaly prediction in assembly pipelines")); Thimonier et al. ([2024](https://arxiv.org/html/2601.12839v1#bib.bib33 "Retrieval augmented deep anomaly detection for tabular data")).

#### 4.1.1 Raw Transaction Dataset

This raw dataset serves as the foundational input for subsequent annotation,
knowledge enrichment, and model training.

#### 4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment

To incorporate domain expertise and enhance semantic interpretability, we enrich a stratified 0.01% subset of transactions using an LLM guided by expert-defined instructions and anomaly typologies. The resulting annotations are used to construct a transaction-centric knowledge graph that enables structured reasoning and explainable anomaly detection.

This design is grounded in classical research on knowledge representation and logical abstraction Levesque ([1984b](https://arxiv.org/html/2601.12839v1#bib.bib14 "Foundations of a functional approach to knowledge representation"), [a](https://arxiv.org/html/2601.12839v1#bib.bib15 "A logic of implicit and explicit belief")); Abelson et al. ([1985](https://arxiv.org/html/2601.12839v1#bib.bib4 "Structure and interpretation of computer programs")); Brachman and Schmolze ([1989](https://arxiv.org/html/2601.12839v1#bib.bib10 "An overview of the kl-one knowledge representation system")); Gottlob ([1992](https://arxiv.org/html/2601.12839v1#bib.bib12 "Complexity results for nonmonotonic logics")); Nebel ([2000](https://arxiv.org/html/2601.12839v1#bib.bib16 "On the compilability and expressive power of propositional planning formalisms")); Baumgartner et al. ([2001](https://arxiv.org/html/2601.12839v1#bib.bib8 "Visual web information extraction with lixto")); Gottlob et al. ([2002](https://arxiv.org/html/2601.12839v1#bib.bib13 "Hypertree decompositions and tractable queries")).

#### 4.1.3 Event Dataset

An external event dataset was incorporated to provide contextual grounding. The event dataset enables alignment between observed transaction patterns
and known real-world incidents, supporting context-aware interpretation
of detected anomalies.

#### 4.1.4 Expert Knowledge Dataset

Expert knowledge was compiled into a structured CSV-based knowledge base and integrated into a *Retrieval-Augmented Generation (RAG)* framework. This allows the LLM to retrieve relevant expert-defined typologies and descriptions during the annotation process.

To ensure leakage prevention, fair model comparison, and alignment with *realistic operational settings*, we applied the following sampling and splitting strategies:

1. 1.

   Address-disjoint sampling:
   Wallet addresses were strictly separated between training and evaluation sets to prevent information leakage and reflect deployment conditions.
2. 2.

   Temporal consistency:
   Transactions were chronologically ordered, with earlier data assigned to training, ensuring no future information was used.
3. 3.

   Stratified sampling:
   The original class imbalance between normal and anomalous transactions was preserved.
4. 4.

   Anomaly type coverage:
   Sampling constraints ensured minimal representation of major anomaly categories, avoiding bias toward specific types.
5. 5.

   Fixed sampling for fair comparison:
   A single *0.01%* sampled subset was extracted once and reused across all experiments to ensure consistent comparison.

### 4.2 Configurations and Evaluation

We compare three configurations: Feature-only (Baseline), Feature + KG, and RDLI (Feature + KG + CS). Performance is evaluated using F1-score and Recall, prioritizing the minimization of missed detections in compliance settings.

1. 1.

   Feature-only (Baseline):
   Uses raw transaction features with binary anomaly labels
   (0: normal, 1: anomalous), serving as a reference without external knowledge.
2. 2.

   Feature + KG:
   Augments baseline features with expert knowledge graph embeddings.
   The knowledge graph encodes domain heuristics and typology-based semantic
   relationships, which are transformed into vector representations using
   DeepWalk.
3. 3.

   RDLI (Feature + KG + CS):
   The full proposed model that integrates knowledge graph embeddings with
   contextual signals.

To evaluate performance under extreme label scarcity, we conduct experiments on both the full dataset and a stratified 0.01% subset. This design minimizes reliance on data scale while explicitly validating the effectiveness of knowledge integration. Class imbalance and anomaly-type coverage are preserved via stratified sampling.

Given the severe imbalance inherent in anomaly detection, we report macro-averaged *Accuracy*, *Precision*, *Recall*, *F1-score*, and *AUC-ROC*, with *Recall* prioritized to minimize missed anomalies. This setting reflects real-world cryptocurrency monitoring, where transaction dynamics and adversarial behaviors evolve continuously.

To assess robustness and generalizability, we further evaluate the model on the Kaggle *Credit Card Transactions Dataset* Choksi ([2023](https://arxiv.org/html/2601.12839v1#bib.bib1 "Credit card transactions dataset")) under identical conditions (0.01% labels, temporal split). The results demonstrate that  RDLI generalizes beyond cryptocurrency networks and maintains stable performance across heterogeneous financial domains.

### 4.3 Experimental Design for Simulated Explanation Evaluation

We conduct a simulated user study to examine how different explanation formats for the same anomalous cryptocurrency transaction influence user perception. A *micro-expert panel* (n=24n=24) was recruited, consisting of professionals with experience in virtual asset transactions, anomaly detection, and regulatory or compliance analysis.

Participants reviewed two realistic anomaly scenarios involving complex transaction flows and address relationships. For each scenario, they were presented with two explanation formats for the same detection outcome: (i) a *baseline feature-based explanation* summarizing observable transaction attributes, and (ii) an *RDLI explanation* that integrates structured expert knowledge and contextual information into a natural-language rationale.

Explanation quality was evaluated across seven constructs—*Trust (TR)*, *Perceived Usefulness (PU)*, *Perceived Ease of Use (PEOU)*, *Consistency (CON)*, *Explainability (EXP)*, *Clarity (CLA)*, and *Acceptance Intention (AI)*—using three to five items per construct on a five-point Likert scale. Survey items were adapted from validated instruments in prior work on explainable systems and usability, and comprehension checks were included to ensure response validity.

## 5 Experimental Results

### 5.1 Performance under Extreme Label Scarcity

This experiment examines the impact of *extreme label scarcity* on existing anomaly detection models and evaluates whether the proposed approach can mitigate this limitation. When trained on the full dataset, baseline models (LightGBM, GRU, and GNN) achieve stable performance, indicating that data-driven learning is effective under sufficient supervision. However, under severe label reduction (0.01%), all baseline models suffer substantial performance degradation, particularly in Recall and F1-score. This highlights the vulnerability of conventional anomaly detection methods in realistic low-label regimes, where rare anomalous behaviors are difficult to identify with limited supervision.

In contrast, the proposed model integrates *expert-heuristic knowledge* via a *knowledge graph (KG)* and *contextual signals (CS)*, maintaining robust performance even under extreme label scarcity. By explicitly encoding domain expertise and transaction-level context, it enables anomaly detection beyond purely data-driven patterns.

As shown in Table [2](https://arxiv.org/html/2601.12839v1#S5.T2 "Table 2 ‣ 5.1 Performance under Extreme Label Scarcity ‣ 5 Experimental Results ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations"), the proposed approach consistently improves *Recall* and *F1-score* over corresponding baselines trained under identical low-label conditions. These results suggest that anomaly detection performance is not solely driven by label volume, but critically depends on the systematic integration of expert heuristics and contextual information, particularly in regulated cryptocurrency environments with scarce and evolving labels.

| Backbone | Model Variant | Acc. | Prec. | Rec. | F1 | AUC |
| --- | --- | --- | --- | --- | --- | --- |
| LightGBM | Feature-only (Full) | 0.7870 | 0.8408 | 0.7870 | 0.8018 | 0.8518 |
| Feature-only (0.01%) | 0.7892 | 0.7796 | 0.7892 | 0.7825 | 0.8110 |
| RDLI (KG + CS) | 0.9963 | 0.9950 | 1.0000 | 0.9975 | 0.9996 |
| Δ\Delta (RDLI – Full) | 0.2093 | 0.1542 | 0.2130 | 0.1957 | 0.1478 |
| GRU | Feature-only (Full) | 0.7271 | 0.3999 | 0.5395 | 0.4593 | 0.6768 |
| Feature-only (0.01%) | 0.4139 | 0.8516 | 0.2437 | 0.3789 | 0.6883 |
| RDLI (KG + CS) | 0.7389 | 0.8898 | 0.7351 | 0.8051 | 0.8290 |
| Δ\Delta (RDLI – Full) | 0.0118 | 0.4899 | 0.1956 | 0.3458 | 0.1522 |
| GNN | Feature-only (Full) | 0.9043 | 0.7460 | 0.5291 | 0.6920 | 0.8438 |
| Feature-only (0.01%) | 0.6815 | 0.6472 | 0.6815 | 0.6243 | 0.6793 |
| RDLI (KG + CS) | 0.9129 | 0.9342 | 0.8235 | 0.8923 | 0.8823 |
| Δ\Delta (RDLI – Full) | 0.0086 | 0.1882 | 0.2944 | 0.2003 | 0.0385 |

Table 2: Performance comparison of RDLI under extreme label scarcity (0.01%).

### 5.2 Ablation Study

To identify the sources of performance gains, we conduct an ablation study across three backbones—*LightGBM*, *GRU*, and *GNN*—by incrementally adding or removing components under identical training conditions.

Across all backbones, *feature-only* configurations exhibit clear limitations under extreme label scarcity. This suggests that performance degradation arises not from insufficient model capacity, but from the absence of informative decision signals under limited supervision.

Incorporating *structural information* yields partial improvements, particularly for GRU and GNN models, indicating that relational patterns provide useful anomaly cues. However, these gains remain inconsistent across metrics, implying that structure alone is insufficient to resolve decision ambiguity.

The full configuration consistently achieves the most stable and balanced performance across all backbones, with *GNN-based models* benefiting most strongly. Overall, the results demonstrate that performance gains stem from the complementary integration of multiple components rather than any single module. Under extreme label scarcity, effective anomaly detection therefore depends more on principled integration of *structural* and *contextual* information than on labeled data volume.

| Backbone | Model Variant | Acc. | Prec. | Rec. | F1 | AUC |
| --- | --- | --- | --- | --- | --- | --- |
| LightGBM | Feature-only | 0.7892 | 0.7796 | 0.7892 | 0.7825 | 0.8110 |
| KG | 0.9808 | 0.9939 | 0.9799 | 0.9799 | 0.9994 |
| RDLI (KG + CS) | 0.9963 | 0.9950 | 1.0000 | 0.9975 | 0.9996 |
| GRU | Feature-only | 0.4139 | 0.8516 | 0.2437 | 0.3789 | 0.6883 |
| KG | 0.6306 | 0.8304 | 0.6239 | 0.7125 | 0.6783 |
| RDLI (KG + CS) | 0.7389 | 0.8898 | 0.7351 | 0.8051 | 0.8290 |
| GNN | Feature-only | 0.6815 | 0.6472 | 0.6815 | 0.6243 | 0.6793 |
| KG | 0.7086 | 0.6889 | 0.7124 | 0.6622 | 0.7318 |
| RDLI (KG + CS) | 0.9129 | 0.9342 | 0.8235 | 0.8923 | 0.8823 |

Table 3: Ablation study under extreme label scarcity (0.01%) on the cryptocurrency transaction dataset

### 5.3 Reproducibility Analysis on Card Transaction Data

To assess reproducibility and cross-domain robustness, we extended our evaluation to the publicly available Kaggle *Credit Card Transactions Dataset* Choksi ([2023](https://arxiv.org/html/2601.12839v1#bib.bib1 "Credit card transactions dataset")), under the same *extreme label scarcity* setting (0.01%). This experiment examines how RDLI behaves when the data topology shifts from decentralized crypto-flows to centralized banking transactions.

##### Performance on Tabular Baselines

The LightGBM-based RDLI configuration exhibits strong generalization, achieving an F1-score improvement of 7.65% over the feature-only baseline. This result indicates that even in traditional financial domains, injecting *logic-aware* embeddings effectively sharpens decision boundaries in tabular models.

##### Performance Divergence in Deep Models

For sequence-based (GRU) and graph-based (GNN) backbones, RDLI consistently improves performance, though absolute gains remain lower than in the cryptocurrency domain. We attribute this divergence to a *topological mismatch* between the two domains:

* •

  Episodic vs. Sequential. Credit card fraud is typically episodic, lacking the long-horizon dependencies required for GRUs to fully leverage sequential modeling.
* •

  Star-Graph vs. Flow-Network. Card transactions form shallow bipartite star graphs (User–Merchant), constraining GNN message passing compared to the deep flow networks of blockchains.

##### Compliance Implications

Despite these constraints, RDLI achieves a perfect Recall of 1.0 across all backbones. Given that missed fraud incurs significantly higher regulatory risk than false positives, this property highlights the framework’s *risk-averse suitability* for compliance-oriented deployments.

##### Discussion

Overall, this study delineates RDLI’s operating envelope: while it consistently enhances tabular baselines across domains, its full potential emerges in settings with *complex relational logic* and *deep sequential dependencies*, such as DeFi and AML investigations, where purely data-driven models often fail.

| Backbone | Model Variant | Acc. | Prec. | Rec. | F1 | AUC |
| --- | --- | --- | --- | --- | --- | --- |
| LightGBM | Feature-only | 0.9230 | 0.8461 | 0.9166 | 0.8800 | 0.9413 |
| KG | 0.9487 | 0.9166 | 0.9166 | 0.9166 | 0.9259 |
| RDLI (KG + CS) | 0.9744 | 1.0000 | 0.9166 | 0.9565 | 0.9320 |
| GRU | Feature-only | 0.9994 | 0.3333 | 1.0000 | 0.5000 | 0.9994 |
| KG | 0.9974 | 0.1111 | 1.0000 | 0.2000 | 0.9974 |
| RDLI (KG + CS) | 0.9929 | 0.0430 | 1.0000 | 0.0833 | 0.9929 |
| GNN | Feature-only | 0.9822 | 0.2534 | 0.9384 | 0.3970 | 0.9355 |
| KG | 0.9945 | 0.0833 | 1.0000 | 0.1538 | 0.9946 |
| RDLI (KG + CS) | 0.9972 | 0.2842 | 1.0000 | 0.4424 | 0.9984 |

Table 4: Ablation study under extreme label scarcity (0.01%) on the card transaction dataset.

### 5.4 Explainability Analysis

To benchmark the interpretability of standard anomaly detection models, we employ SHAP (SHapley Additive exPlanations), a widely adopted method for explaining predictions generated by “black-box” models Lundberg and Lee ([2017](https://arxiv.org/html/2601.12839v1#bib.bib42 "A unified approach to interpreting model predictions")).
Figure [2](https://arxiv.org/html/2601.12839v1#S5.F2 "Figure 2 ‣ The Need for Path-Level Reasoning ‣ 5.4 Explainability Analysis ‣ 5 Experimental Results ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations") visualizes the top-5 feature attributions for the LightGBM (Full) model.

##### The Illusion of Interpretability

At first glance, SHAP appears effective in highlighting global feature importance, identifying attributes such as *Value*, *Year*, and *DayOfWeek* as dominant predictors. However, within a forensic auditing context, this feature-centric representation reveals a critical semantic gap.

* •

  Atomistic vs. Relational Reasoning. SHAP decomposes a model prediction into independent feature contributions. In contrast, money laundering behavior is inherently relational: a high-value transaction is rarely suspicious in isolation, but rather due to its position within a broader transactional structure, such as a dispersal or “fan-out” pattern. SHAP is fundamentally unable to encode this sequential and relational logic.
* •

  Ambiguity of Intent. As illustrated in Figure [2](https://arxiv.org/html/2601.12839v1#S5.F2 "Figure 2 ‣ The Need for Path-Level Reasoning ‣ 5.4 Explainability Analysis ‣ 5 Experimental Results ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations"), distinct fraud typologies often exhibit overlapping SHAP value distributions. For instance, a high-value signal (red dot) may correspond equally to a legitimate VIP transfer, a theft-related movement, or a layering operation. Without explicit access to the underlying behavioral motif, auditors cannot reliably distinguish legitimate high-volume trading from illicit laundering activities.

##### The Need for Path-Level Reasoning

Consequently, while feature attribution methods such as SHAP provide statistical justification for model outputs, they fail to deliver the behavioral rationale demanded by regulatory frameworks such as the FATF Travel Rule. This limitation directly motivates the design of RDLI, which shifts the explanatory focus from isolating “suspicious features” to reconstructing the complete “suspicious path.” We empirically validate this hypothesis through the subsequent micro-expert user study.

![Refer to caption](shap.png)


Figure 2: SHAP-based top-5 feature importance for the LightGBM (Full) model.

### 5.5 Validating Operational Utility with Domain Experts

To assess the practical viability of the proposed framework, we conducted a simulated forensic review with a micro-expert panel (n=24n=24) consisting of professionals in anti-money laundering (AML). Participants were asked to review explanations for flagged anomalies under two conditions: a Baseline (Feature-centric) explanation and an RDLI (Path-centric) explanation.

As reported in Table 5, RDLI significantly outperformed the baseline across all evaluated psychometric constructs, with paired tt-tests indicating statistical significance at the p<0.001p<0.001 level. Qualitative feedback further revealed that baseline explanations imposed a high cognitive burden, requiring experts to manually infer behavioral intent from fragmented feature lists. In contrast, RDLI’s narrative, path-level structure functioned as a *cognitive scaffold*, closely aligning with investigators’ mental models and forensic reasoning processes. These results confirm that RDLI delivers the level of *audit-readiness* required for effective human–AI collaborative workflows in regulated financial environments.

| Anomaly Case | Measure | t-value | p-value |
| --- | --- | --- | --- |
| 1 | TR | -2.346 | <.004<.004 |
| 1 | PU | -3.342 | <.001<.001 |
| 1 | PEOU | -3.974 | <.001<.001 |
| 1 | CON | -5.003 | <.001<.001 |
| 1 | EXP | -6.859 | <.001<.001 |
| 1 | CLA | -2.421 | <.012<.012 |
| 2 | TR | -2.298 | <.001<.001 |
| 2 | PU | -4.243 | <.001<.001 |
| 2 | PEOU | -3.015 | <.021<.021 |
| 2 | CON | -4.463 | <.001<.001 |
| 2 | EXP | -5.972 | <.001<.001 |
| 2 | CLA | -3.194 | <.003<.003 |

Table 5: Paired tt-test results comparing baseline & RDLI explanations

## 6 Conclusion

This study addresses a central challenge in cryptocurrency anomaly detection: reconciling the demand for *audit-ready transparency* under regulations such as the FATF Travel Rule with the opacity and data sparsity of modern deep learning models. We argue that in high-stakes financial environments, purely data-driven approaches are insufficient to capture the adaptive nature of financial crime.

To bridge this gap, we proposed *Relational Domain-Logic Integration (RDLI)*, a framework that embeds expert heuristics as differentiable latent signals and anchors them with retrieval-grounded market context. Rather than memorizing surface-level patterns, *RDLI* reconstructs the underlying *logic of crime* through structured reasoning.

Empirically, *RDLI* demonstrates strong resilience under extreme label scarcity (0.01%), outperforming state-of-the-art GNN baselines by 28.9% in F1-score. Additional experiments on credit card transaction data and a micro-expert evaluation further confirm its robustness across financial domains and alignment with human expert reasoning.

Overall, this work advocates a shift from correlation-driven black-box models toward neuro-symbolic financial AI that explicitly integrates domain logic and context. We position *RDLI* as a step toward explainable, trustworthy, and regulation-compliant autonomous financial monitoring systems.

## References

* H. Abelson, G. J. Sussman, and J. Sussman (1985)
  Structure and interpretation of computer programs.
   MIT Press, Cambridge, Massachusetts.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* R. Baumgartner, S. Flesca, and G. Gottlob (2001)
  Visual web information extraction with lixto.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* R. J. Brachman and J. G. Schmolze (1989)
  An overview of the kl-one knowledge representation system.
  Readings in artificial intelligence and databases,  pp. 207–230.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* F. Carcillo, A. Dal Pozzolo, M. Snoeck, and G. Bontempi (2021)
  Scarff: a scalable framework for streaming credit card fraud detection.
  Artificial Intelligence Review.
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p1.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* R. Chalapathy and S. Chawla (2022)
  Deep learning for anomaly detection: a review.
  ACM Computing Surveys (CSUR) 54 (2),  pp. 1–38.
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p2.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* V. Chandola, A. Banerjee, and V. Kumar (2009)
  Anomaly detection: a survey.
  ACM Computing Surveys.
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p1.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Y. Chen, C. Zhao, and C. Nie (2025)
  Health insurance fraud detection: the role of feature engineering and preprocessing techniques.
  In Proceedings of the 2nd Guangdong-Hong Kong-Macao Greater Bay Area International Conference on Digital Economy and Artificial Intelligence,
   pp. 858–862.
  Cited by: [§1](https://arxiv.org/html/2601.12839v1#S1.p4.1 "1 Introduction ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* D. Cheng, Y. Zou, S. Xiang, and C. Jiang (2025)
  Graph neural networks for financial fraud detection: a review.
  Frontiers of Computer Science 19 (9),  pp. 199609.
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p3.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* P. Choksi (2023)
  Credit card transactions dataset.
  Note: <https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset>Kaggle, accessed 2025
  Cited by: [§4.2](https://arxiv.org/html/2601.12839v1#S4.SS2.p5.1 "4.2 Configurations and Evaluation ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations"),
  [§5.3](https://arxiv.org/html/2601.12839v1#S5.SS3.p1.1 "5.3 Reproducibility Analysis on Card Transaction Data ‣ 5 Experimental Results ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Y. Dou et al. (2020)
  Enhancing graph neural network-based fraud detectors against camouflaged fraudsters.
  In Proceedings of the 26th ACM SIGKDD Conference,
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p2.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* A. Ghaffari, H. Nguyen, L. Lovén, and E. Gilman (2025)
  STM-graph: a python framework for spatio-temporal mapping and graph neural network predictions.
  In Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM ’25),
  External Links: [Document](https://dx.doi.org/10.1145/3746252.3761645)
  Cited by: [§3.3.4](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS4.p1.1 "3.3.4 Graph Neural Network Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* G. Gottlob, N. Leone, and F. Scarcello (2002)
  Hypertree decompositions and tractable queries.
  Journal of Computer and System Sciences 64 (3),  pp. 579–627.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* G. Gottlob (1992)
  Complexity results for nonmonotonic logics.
  Journal of Logic and Computation 2 (3),  pp. 397–425.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* R. Guidotti et al. (2019)
  A survey of methods for explaining black box models.
  ACM Computing Surveys.
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p1.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* W. Hamilton, Z. Ying, and J. Leskovec (2017)
  Inductive representation learning on large graphs.
  Advances in neural information processing systems 30.
  Cited by: [§3.3.4](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS4.p1.1 "3.3.4 Graph Neural Network Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* R. R. Hoffman, S. T. Mueller, G. Klein, and J. Litman (2018)
  Metrics for explainable ai: challenges and prospects.
  arXiv preprint arXiv:1812.04608.
  Cited by: [§4.1](https://arxiv.org/html/2601.12839v1#S4.SS1.p2.1 "4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Z. Hu, S. Li, J. Liu, and Y. Tang (2023)
  Transaction-based classification and detection of illicit activities on blockchain.
  IEEE Transactions on Information Forensics and Security 18,  pp. 1234–1248.
  External Links: [Document](https://dx.doi.org/10.1109/TIFS.2023.3241234)
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p2.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Y. Jia, Y. Wang, J. Sun, Y. Tian, and P. Qian (2025)
  LMAE4Eth: generalizable and robust ethereum fraud detection by exploring transaction semantics and masked graph embedding.
  IEEE Transactions on Information Forensics and Security.
  Cited by: [§3.3.2](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS2.p1.1 "3.3.2 Tree-based Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations"),
  [§4.1](https://arxiv.org/html/2601.12839v1#S4.SS1.p2.1 "4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Ł. Korycki and B. Krawczyk (2023)
  Adversarial concept drift detection under poisoning attacks for robust data stream mining.
  Machine Learning 112 (10),  pp. 4013–4048.
  Cited by: [§2.2](https://arxiv.org/html/2601.12839v1#S2.SS2.p1.1 "2.2 Knowledge-Integrated & Explainable Detection ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Y. Lei, Y. Xiang, Q. Wang, R. Dowsley, T. H. Yuen, K. R. Choo, and J. Yu (2025)
  Large language models for cryptocurrency transaction analysis: a bitcoin case study.
  Note: arXiv preprint arXiv:2501.18158
  External Links: 2501.18158,
  [Link](https://arxiv.org/abs/2501.18158)
  Cited by: [§4.1](https://arxiv.org/html/2601.12839v1#S4.SS1.p2.1 "4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* H. J. Levesque (1984a)
  A logic of implicit and explicit belief.
  In Proceedings of the Fourth National Conference on Artificial Intelligence,
  Austin, Texas,  pp. 198–202.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* H. J. Levesque (1984b)
  Foundations of a functional approach to knowledge representation.
  Artificial Intelligence 23 (2),  pp. 155–212.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, et al. (2020)
  Retrieval-augmented generation for knowledge-intensive nlp tasks.
  Advances in neural information processing systems 33,  pp. 9459–9474.
  Cited by: [§2.2](https://arxiv.org/html/2601.12839v1#S2.SS2.p1.1 "2.2 Knowledge-Integrated & Explainable Detection ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* X. Li, S. Liu, Z. Li, X. Han, C. Shi, B. Hooi, H. Huang, and X. Cheng (2020)
  FlowScope: spotting money laundering based on graphs.
  In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI),
   pp. 4731–4738.
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p3.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Z. Li, P. Wang, H. Lu, and J. Cheng (2019)
  Reading selectively via binary input gated recurrent unit..
  In IJCAI,
   pp. 5074–5080.
  Cited by: [§3.3.3](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS3.p1.1 "3.3.3 Neural Sequence Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Z. Li, Y. Chen, T. Zhao, Z. Xu, Y. Liu, and P. S. Yu (2025)
  Association-focused path aggregation for graph fraud detection.
  In Proceedings of the 39th Annual Conference on Neural Information Processing Systems (NeurIPS 2025),
  Vancouver, Canada.
  Cited by: [§4.1](https://arxiv.org/html/2601.12839v1#S4.SS1.p2.1 "4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* S. M. Lundberg and S. Lee (2017)
  A unified approach to interpreting model predictions.
  In Advances in Neural Information Processing Systems,
  Cited by: [§2.2](https://arxiv.org/html/2601.12839v1#S2.SS2.p2.1 "2.2 Knowledge-Integrated & Explainable Detection ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations"),
  [§5.4](https://arxiv.org/html/2601.12839v1#S5.SS4.p1.1 "5.4 Explainability Analysis ‣ 5 Experimental Results ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* B. Nebel (2000)
  On the compilability and expressive power of propositional planning formalisms.
  Journal of Artificial Intelligence Research 12,  pp. 271–315.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.12839v1#S4.SS1.SSS2.p2.1 "4.1.2 LLM-Based Annotation and Knowledge Graph Enrichment ‣ 4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* A. Pareja, G. Domeniconi, J. Chen, T. Ma, T. Suzumura, H. Kanezashi, T. Kaler, T. B. Schardl, and C. E. Leiserson (2020)
  EvolveGCN: evolving graph convolutional networks for dynamic graphs.
  In Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence (AAAI-20),
   pp. 5363–5370.
  Cited by: [§3.3.4](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS4.p2.1 "3.3.4 Graph Neural Network Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* M. Park, S. Moon, H. Cha, G. Na, S. Kim, and S. Chai (2025)
  HyPV-lead: proactive early-warning of cryptocurrency anomalies through data-driven structural–temporal modeling.
  In Proc. IEEE Int. Conf. on Big Data (BigData),
  Cited by: [§3.3.3](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS3.p1.1 "3.3.3 Neural Sequence Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* C. Shyalika, R. Prasad, F. E. Kalach, R. Venkataramanan, R. Zand, R. Harik, and A. Sheth (2025)
  NSF-map: neurosymbolic multimodal fusion for robust and interpretable anomaly prediction in assembly pipelines.
  arXiv preprint arXiv:2505.06333.
  Cited by: [§4.1](https://arxiv.org/html/2601.12839v1#S4.SS1.p2.1 "4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* J. Sun, Y. Jia, Y. Wang, Y. Tian, and S. Zhang (2025)
  Ethereum fraud detection via joint transaction language model and graph representation learning.
  Information Fusion 120,  pp. 103074.
  Cited by: [§4.1](https://arxiv.org/html/2601.12839v1#S4.SS1.p2.1 "4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Y. Takei and K. Shudo (2024)
  FATF travel rule’s technical challenges and solution taxonomy.
  In 2024 IEEE International Conference on Blockchain and Cryptocurrency (ICBC),
   pp. 784–799.
  Cited by: [§1](https://arxiv.org/html/2601.12839v1#S1.p4.1 "1 Introduction ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Q. Tan, M. Ye, G. L. Wong, and P. C. Yuen (2021)
  Cooperative joint attentive network for patient outcome prediction on irregular multi-rate multivariate health data..
  In IJCAI,
   pp. 1586–1592.
  Cited by: [§3.3.3](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS3.p1.1 "3.3.3 Neural Sequence Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* H. Thimonier, F. Popineau, A. Rimmel, and B. Doan (2024)
  Retrieval augmented deep anomaly detection for tabular data.
  In Proceedings of the 33rd ACM international conference on information and knowledge management,
   pp. 2250–2259.
  Cited by: [§4.1](https://arxiv.org/html/2601.12839v1#S4.SS1.p2.1 "4.1 Dataset and Prerocessing ‣ 4 Experimental Setup ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* X. Wang, Q. Han, K. Liu, X. Cheng, H. Shen, B. Yang, Q. Yang, and W. Zhang (2021)
  Graph neural networks in financial fraud detection: a survey.
  IEEE Access 9,  pp. 140100–140117.
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p2.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Z. Wang, Z. Ren, C. He, P. Zhang, and Y. Hu (2019)
  Robust embedding with multi-level structures for link prediction..
  In IJCAI,
   pp. 5240–5246.
  Cited by: [§3.3.4](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS4.p2.1 "3.3.4 Graph Neural Network Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* M. Weber, G. Domeniconi, J. Chen, D. K. I. Weidele, C. Bellei, T. Robinson, and C. E. Leiserson (2019)
  Anti-money laundering in bitcoin: experimenting with graph convolutional networks for financial forensics.
  arXiv preprint.
  External Links: 1908.02591,
  [Link](https://arxiv.org/abs/1908.02591)
  Cited by: [§2.1](https://arxiv.org/html/2601.12839v1#S2.SS1.p1.1 "2.1 Anomaly Detection under Structural Scarcity ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* Z. Xu, Y. Liu, Y. Zhang, Y. Wang, Y. Zhang, and P. S. Yu (2024)
  Challenges and pitfalls in real-world financial anomaly detection.
  In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24), Industry Track,
  New York, NY, USA,  pp. 5051–5062.
  Cited by: [§2.2](https://arxiv.org/html/2601.12839v1#S2.SS2.p1.1 "2.2 Knowledge-Integrated & Explainable Detection ‣ 2 Related Work ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").
* C. Zhao, S. Liu, F. Huang, S. Liu, and W. Zhang (2021)
  CSGNN: contrastive self-supervised graph neural network for molecular interaction prediction..
  In IJCAI,
   pp. 3756–3763.
  Cited by: [§3.3.4](https://arxiv.org/html/2601.12839v1#S3.SS3.SSS4.p2.1 "3.3.4 Graph Neural Network Predictor ‣ 3.3 Model Architecture ‣ 3 Proposed Method ‣ Knowledge-Integrated Representation Learning for Crypto Anomaly Detection under Extreme Label Scarcity; Relational Domain-Logic Integration with Retrieval-Grounded Context and Path-Level Explanations").