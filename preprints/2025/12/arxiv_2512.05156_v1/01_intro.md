---
authors:
- Igor Halperin
doc_id: arxiv:2512.05156v1
family_id: arxiv:2512.05156
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons
  and Manage Hallucinations
url_abs: http://arxiv.org/abs/2512.05156v1
url_html: https://arxiv.org/html/2512.05156v1
venue: arXiv q-fin
version: 1
year: 2025
---


Igor Halperin
  
Fidelity Investments
The author acknowledges the assistance of Claude Code and Claude Sonnet 4.5 in developing code, generating and analyzing data, and preparing this manuscript.
All remaining errors are the author’s own. The views expressed herein are those of the author and do not necessarily reflect the views of his employer. Code and data available at: <https://github.com/ighalp/semantic-faithfulness-sdm>. Email for correspondence: ighalp@gmail.com.

(December 4, 2025)

###### Abstract

Evaluating faithfulness of Large Language Models (LLMs) to a given task is a complex challenge. We propose two new unsupervised metrics for faithfulness evaluation using insights from information theory and thermodynamics. Our approach treats an LLM as a bipartite information engine where hidden layers act as a Maxwell demon controlling transformations of context CC into answer AA via prompt QQ.
We model Question-Context-Answer (QCA) triplets as probability distributions over shared topics. Topic transformations from CC to QQ and AA are modeled as transition matrices 𝐐\mathbf{Q} and 𝐀\mathbf{A} encoding the query goal and actual result, respectively. Our semantic faithfulness (SF) metric quantifies faithfulness for any given QCA triplet by the Kullback-Leibler (KL) divergence between these matrices. Both matrices are inferred simultaneously via convex optimization of this KL divergence, and the final SF metric is obtained by mapping the minimal divergence onto the unit interval [0,1], where higher scores indicate greater faithfulness.
Furthermore, we propose a thermodynamics-based semantic entropy production (SEP) metric in answer generation, and show that high faithfulness generally implies low entropy production. The SF and SEP metrics can be used jointly or separately for LLM evaluation and hallucination control. We demonstrate our framework on LLM summarization of corporate SEC 10-K filings.

## 1 Introduction

Large Language Models (LLMs) have demonstrated remarkable capabilities in generating human-like text, answering questions, and summarizing information. However, ensuring that their outputs are factually grounded and faithful to a provided source context is a persistent and crucial challenge. Large deviations of LLM outputs
from those expected according to their prompts, often referred to
as faithfulness hallucinations, pose a major barrier to the deployment of LLMs in high-stakes domains such as medicine, law, and finance.

Current evaluation methods often rely on human annotators, which is expensive and not scalable, or on other LLMs for assessment, which can introduce its own biases and inaccuracies. There is a pressing need for automated, quantitative, and interpretable metrics that can reliably measure the faithfulness of an LLM’s response to a given context.

In this paper, we introduce a novel approach to this problem using insights from information theory [[5](https://arxiv.org/html/2512.05156v1#bib.bib5), [6](https://arxiv.org/html/2512.05156v1#bib.bib6)] and thermodynamics [[14](https://arxiv.org/html/2512.05156v1#bib.bib14), [15](https://arxiv.org/html/2512.05156v1#bib.bib15)].
First, we model a triplet (Q,C,A)(Q,C,A) of context CC, question QQ, and answer AA not as simple strings of text, but as distributions over a latent topic space. The process of transforming the initial text CC into the final LLM output AA can then be thought of as a transition between the initial topic distribution 𝐩c{\bf p}\_{c} of the context document into the final topic distribution 𝐩a{\bf p}\_{a}. We can write such relation as
𝐩a=𝐩cT​𝐀{\bf p}\_{a}={\bf p}\_{c}^{T}{\bf A},
where 𝐀{\bf A} is a N×NN\times N matrix (where NN is the number of topics) with all elements being non-negative and ∑j=1N𝐀i​j=1,∀i\sum\_{j=1}^{N}{\bf A}\_{ij}=1,\;\forall i.
We can now similarly introduce a ’goal interpretation’ matrix 𝐐{\bf Q} that should be consistent with the marginal distributions 𝐩c{\bf p}\_{c} and 𝐩q{\bf p}\_{q}, via the constraint
𝐩q=𝐩cT​𝐐{\bf p}\_{q}={\bf p}\_{c}^{T}{\bf Q}. The matrix
𝐐{\bf Q} should also satisfy the probability constraint
∑j=1N𝐐i​j=1,∀i\sum\_{j=1}^{N}{\bf Q}\_{ij}=1,\;\forall i.

The core idea of our approach is that a ”faithful” answer should transform the topics from the context in a way that is semantically similar to how the question ”queries” the topics from that same context. We formalize this intuition by defining two probabilistic transition matrices 𝐀{\bf A} and 𝐐{\bf Q} and propose minimizing their Kullback-Leibler (KL) divergence as an objective. The resulting minimal divergence value serves as our faithfulness score which we will call semantic faithfulness (SF) score. The SF metric is unsupervised, computable for a single (Question, Context, Answer) triplet, and provides a continuous measure of faithfulness, allowing for direct comparison between different LLM responses.

While the SF metric is based on the information-theoretic analysis, in this paper we also pursue a view of LLMs as information engines, and address thermodynamics of such engines [[14](https://arxiv.org/html/2512.05156v1#bib.bib14), [15](https://arxiv.org/html/2512.05156v1#bib.bib15)].
We conceptualize a LLM as a bipartite information engine made of two sub-systems XX and YY. Only one of these sub-systems (XX) is partially observed to the user via LLM’s API, while the second, unobserved sub-system YY conceptualizes the computational engine of the LLM. In the physics literature, such unobserved sub-systems of information engines are often referred to as Maxwell’s demons, and we will follow this terminology in this paper.

The thermodynamics-based analysis of the LLM as an information engine produces our second metric for evaluation of faithfulness and managing LLM hallucinations, which we call semantic entropy production (SEP). To the extend that LLM hallucinations can be thought of as noisy (i.e. entropy-increasing) distortions of information contained in context CC and user question QQ, the concept of entropy production as defined in physics [[14](https://arxiv.org/html/2512.05156v1#bib.bib14), [15](https://arxiv.org/html/2512.05156v1#bib.bib15)] offers a quantitative way to quantify such measure in the LLM answer generating process.
We believe that searching for LLM hallucinations using the semantic entropy production metric is a more theoretically grounded and empirically attractive idea than looking only into the marginal semantic entropy of LLM answers, as is done in the Semantic Entropy method [[8](https://arxiv.org/html/2512.05156v1#bib.bib8)], see below in Sect. [4.2](https://arxiv.org/html/2512.05156v1#S4.SS2 "4.2 Semantic Entropy or Semantic Entropy Production? ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations").

As we will show below, the SEP metric is easily computable using a part of our first algorithm for computing the SF metric. In certain cases discussed below, the SEP metric does not require any new optimization, and the SEP score can be computed directly off the SF score. Moreover, we will show that the SF and SEP scores are typically inversely related: a high SF score (high faithfulness) typically implies a low SEP score, and vice versa. This observation gives support to our SF metric, as well to the intuitive idea that faithfulness hallucinations can be thought of as LLM responses with extremely low semantic faithfulness.

We validate our framework experimentally on 10 Question-Context-Answer triplets from NVIDIA’s fiscal 2024 10-K disclosure, organized into two groups testing different question structures: comprehensive multi-topic risk analysis versus focused competitive threats analysis. Our results demonstrate that the proposed metrics successfully capture meaningful differences in semantic faithfulness, with question structure, and not just entropy magnitude, emerging as the key driver of faithfulness variation. LLM-as-a-Judge evaluation [[18](https://arxiv.org/html/2512.05156v1#bib.bib18)] confirms that higher ℱS\mathcal{F}\_{S} scores correlate with superior structural alignment and contextual grounding.

The paper is organized as follows.
In Sect. [2](https://arxiv.org/html/2512.05156v1#S2 "2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") we present our problem formulation and modeling framework, and define the semantic faithfulness (SF) metric.
In Sect. [3](https://arxiv.org/html/2512.05156v1#S3 "3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"), we present a lightweight numerical algorithm to compute the SF metric using the standard convex optimization software. In Sect. [4](https://arxiv.org/html/2512.05156v1#S4 "4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"), we model the LLM as a thermodynamics engine and compute the SEP metric.
Sect. [5](https://arxiv.org/html/2512.05156v1#S5 "5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") presents our experiments, and the final Sect. [6](https://arxiv.org/html/2512.05156v1#S6 "6 Conclusions ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") concludes.

## 2 Semantic Faithfulness

### 2.1 Problem formulation

In this paper, we consider a user interaction with a LLM viewed as a black box, and operated at the level of a single-step interaction when the user asks a question QQ about some context document set CC (e.g. to provide a summary of CC), and gets an answer AA from the LLM.
The black-box setting of our formulation implies that we do not have access to additional information such as internal activations, log-probs etc.

In practice, tasks such as a LLM-provided summarization are often ran a few (say, K=10K=10) times, and then the ’best’ answer is selected from KK candidate answers by analysing the resulting triplets (Qk,C,Ak)(Q\_{k},C,A\_{k}), with k=1,…,Kk=1,\ldots,K.
Instead of running the same question (prompt) KK times, we assume a more general setting where all questions QkQ\_{k} are constructed as semantically equivalent paraphrases of a given initial question QQ. As discussed in [[9](https://arxiv.org/html/2512.05156v1#bib.bib9)], prompt paraphrasing is useful to enrich the data and extract
more meaningful topic representations.
In what follows, we assume that triplets (Qk,C,Ak)(Q\_{k},C,A\_{k}) constitute the only available data for our analysis.

The main question here is of course how to define what we mean by the ’best’ answer. While multiple empirical schemes can be considered at this point, in general, ’the best’ means ’the most faithful to the provided context and question’. Our problem is therefore how to define the concept of a ’most faithful’ LLM response within our black box setting.

### 2.2 LLM as a Bipartite Information Engine: the LLM Maxwell’s Demon

We model an LLM as an information engine that consumes some input information (context CC and user question QQ), transforms it, and produces its output AA. Furthermore, this information engine has a bipartite structure: it is made of two interacting stochastic sub-systems XX and YY (thought of as a ’tape’ and ’controller’, respectively), that operate in consecutive steps. The first system XX (the ’tape’) is a part of the LLM exposed to the end user via a LLM user interface, roughly identified with the first and last layers of a neural network that implements the LLM. In particular, context CC and the LLM answer AA can be viewed as (noisy) observations of sub-system XX. This is achieved using a pre-trained sentence embedding model, and treating the sentence embedding vectors of CC and AA as noisy transforms of internal activations of the LLM in the process of answer generation.

In contrast, the second sub-system YY (the controller) is not exposed to the user. This sub-system controls the transformation on the input context CC into answer AA, as specified by the user question (prompt) QQ.
This sub-system conceptualizes the notion of Maxwell’s demon as an agent that converts information into work.111See e.g. [[14](https://arxiv.org/html/2512.05156v1#bib.bib14)] on the history of the concept of Maxwell demon since James Clerk Maxwell’s work to modern-day front lines of stochastic thermodynamics.
Sub-system YY is roughly identified with inner layers of the neural network.
While we do not observe states of sub-system YY either directly or indirectly, they should depend on embeddings of context CC and question QQ, to the extend that the latter define the task for the LLM.

The bipartite X​YXY-system proceeds in steps. First, the controller YY (the Maxwell demon) sets itself in a proper state by reading the user question QQ and the context documents CC. This informs the LLM about a transformation of CC needed to provide answer AA expected by the user. The controller then defines a policy for the text generation, which is further used as a control protocol for the evolution of sub-system XX from the initial state CC to the final state AA.
Importantly, the two sub-systems XX and YY of a bipartite information engine do not operate concurrently, but rather sequentially. This feature of bipartite systems make them amenable to theoretical analyses, see e.g. [[7](https://arxiv.org/html/2512.05156v1#bib.bib7)] for a review.

The bipartite X​YXY-system representing the LLM can be analyzed using methods of both information theory and thermodynamics. We start with the information-theoretic analysis, and then present a complimentary view based on thermodynamics.

### 2.3 Topical Representation

We view each of 𝒬\mathcal{Q}, 𝒞\mathcal{C}, and 𝒜\mathcal{A} as a collection of sentences. By analyzing the semantic embeddings of these sentences (e.g., using a pre-trained sentence transformer), we can identify a set of NN latent topics that span the semantic space of the triplet. We can then represent 𝒬\mathcal{Q}, 𝒞\mathcal{C}, and 𝒜\mathcal{A} as probability distributions over these NN topics. Let these marginal distributions be:

* •

  p(c)=(p1(c),…,pN(c))p^{(c)}=(p\_{1}^{(c)},\dots,p\_{N}^{(c)}), the topic distribution of the context.
* •

  p(q)=(p1(q),…,pN(q))p^{(q)}=(p\_{1}^{(q)},\dots,p\_{N}^{(q)}), the topic distribution of the question.
* •

  p(a)=(p1(a),…,pN(a))p^{(a)}=(p\_{1}^{(a)},\dots,p\_{N}^{(a)}), the topic distribution of the answer.

We assume that these marginal distributions can be empirically estimated from the text triplet. In particular, they can be easily computed using the Semantic Divergence Metrics (SDM) method recently developed in [[9](https://arxiv.org/html/2512.05156v1#bib.bib9), [10](https://arxiv.org/html/2512.05156v1#bib.bib10)]. The SDM approach performs a joint clustering of sentence embeddings for all sentences in Q​C​AQCA-triplets, and then identifies cluster topics by doing the term frequency analysis. Once clusters are found, all texts in the Q​C​AQCA triplet are converted into marginal probability distributions
p(q),p(c),p(a)p^{(q)},p^{(c)},p^{(a)} by counting frequencies of cluster assignments of their sentences.

We note here that while the SDM approach is assumed here as a practical and numerically inexpensive way to compute the marginal
distributions p(q),p(c),p(a)p^{(q)},p^{(c)},p^{(a)}, the method developed in this paper is agnostic to how these quantities are computed, and therefore in principle can be used alongside any other method that computes these marginal probabilities.

### 2.4 Information Flows as Topic Weights Transitions

To model the flow of information from the context to the answer and from the context to the question, we introduce two N×NN\times N transition matrices, 𝐐=[Qi​j]\mathbf{Q}=[Q\_{ij}] and 𝐀=[Ai​j]\mathbf{A}=[A\_{ij}], where:

* •

  Qi​jQ\_{ij} is the conditional probability that a unit of topical probability mass from topic ii in the context is mapped to topic jj in the question.
* •

  Ai​jA\_{ij} is the conditional probability that a unit of topical probability mass from topic ii in the context is mapped to topic jj in the answer.

For these matrices to be valid, they must be row-stochastic, meaning the rows sum to one:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1NQi​j=1and∑j=1NAi​j=1,∀i∈{1,…,N}.\sum\_{j=1}^{N}Q\_{ij}=1\quad\text{and}\quad\sum\_{j=1}^{N}A\_{ij}=1\quad,\forall i\in\{1,\dots,N\}. |  | (1) |

Furthermore, these matrices must explain the observed marginal distributions. By the law of total probability, they must satisfy the following linear constraints:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | pj(a)\displaystyle p\_{j}^{(a)} | =∑i=1Npi(c)​Ai​j,∀j∈{1,…,N}\displaystyle=\sum\_{i=1}^{N}p\_{i}^{(c)}A\_{ij},\quad\forall j\in\{1,\dots,N\} |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | pj(q)\displaystyle p\_{j}^{(q)} | =∑i=1Npi(c)​Qi​j,∀j∈{1,…,N}\displaystyle=\sum\_{i=1}^{N}p\_{i}^{(c)}Q\_{ij},\quad\forall j\in\{1,\dots,N\} |  | (3) |

Note that the first equation here can be interpreted as a (one-step) Markov chain process with transition matrix 𝐀{\bf A}, which describes the topic evolution from the context CC to the answer AA produced by the LLM. The transition process can be thought of as proceeding in a time step Δ​Ta\Delta T\_{a}.
On the other hand, we can similarly interpret the second equation in ([3](https://arxiv.org/html/2512.05156v1#S2.E3 "In 2.4 Information Flows as Topic Weights Transitions ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) as
a dynamic transition of the initial topic distribution into a new distribution according to the prompt. This transition occurs in a shorter time step Δ​Tq≪Δ​Ta\Delta T\_{q}\ll\Delta T\_{a}. Information in the user question (prompt) defines the objective (the desired ’semantic drift’) for the task of transformation of the context text into the answer text by the LLM.
Viewed from the point of view of the LLM as a bipartite X​YXY-system, the 𝐐{\bf Q}-dynamics are associated with an initial preparation of sub-system YY, while sub-system XX
evolves according to the 𝐀{\bf A}-dynamics. When the condition Δ​Tq≪Δ​Ta\Delta T\_{q}\ll\Delta T\_{a} holds, it means that sub-system XX remains idle for
a very short time Δ​Tq\Delta T\_{q} at the start of its response time period Δ​Ta\Delta T\_{a}.

We can expect that
matrices 𝐐{\bf Q} and 𝐀{\bf A} expressing, respectively, the ’objective’ and the ’result’ of the topic transformation of the initial context CC should be similar to each other.
Now consider our setting described above in Sect. [2.1](https://arxiv.org/html/2512.05156v1#S2.SS1 "2.1 Problem formulation ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"),
where we have a set of KK triplets
(Qi,C,Ai)(Q\_{i},C,A\_{i}) with i=1,…,Ki=1,\ldots,K enumerating the number of semantically equivalent prompt paraphrases.
If we had a metric (score) to compare these triplets, we would be able to pick a triplet with the highest score as the most faithful one.
As we will show in the next section, we can convert this idea into a lightweight numerical algorithm computing the faithfulness score for LLM answers.

### 2.5 Semantic Faithfulness Score

The constraints in Eqs.([1](https://arxiv.org/html/2512.05156v1#S2.E1 "In 2.4 Information Flows as Topic Weights Transitions ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"))-([3](https://arxiv.org/html/2512.05156v1#S2.E3 "In 2.4 Information Flows as Topic Weights Transitions ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) do not uniquely determine the matrices 𝐀\mathbf{A} and 𝐐\mathbf{Q}. There can be many transition dynamics that satisfy the marginals. The key idea of our method is to choose the pair of matrices (𝐀,𝐐)(\mathbf{A},\mathbf{Q}) that are minimally divergent from each other, reflecting the most ”parsimonious” explanation for the transformations. We quantify this divergence using the conditional Kullback-Leibler (KL) divergence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(𝐀∥𝐐)=∑i=1Npi(c)​∑j=1NAi​j​log⁡Ai​jQi​j.D(\mathbf{A}\parallel\mathbf{Q})=\sum\_{i=1}^{N}p\_{i}^{(c)}\sum\_{j=1}^{N}A\_{ij}\log\frac{A\_{ij}}{Q\_{ij}}. |  | (4) |

This objective measures the expected information-theoretic distance between the transition dynamics, where the expectation is taken over the starting topics as defined by the context distribution p(c)p^{(c)}.
The KL divergence ([4](https://arxiv.org/html/2512.05156v1#S2.E4 "In 2.5 Semantic Faithfulness Score ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) quantifies the information cost of encoding the transition matrix 𝐀{\bf A} in terms of transition matrix 𝐐{\bf Q} [[6](https://arxiv.org/html/2512.05156v1#bib.bib6)]. As in our framework it is the Maxwell demon YY that eventually controls both matrices
𝐐{\bf Q} and 𝐀{\bf A}, this information cost is carried by the Maxwell demon.

Our proposed faithfulness metric, which we call the Semantic Faithfulness (SF) score and denote as ℱS\mathcal{F}\_{S}, is defined in terms of the minimal value of this KL divergence ([4](https://arxiv.org/html/2512.05156v1#S2.E4 "In 2.5 Semantic Faithfulness Score ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")), obtained by jointly optimizing over 𝐀\mathbf{A} and 𝐐\mathbf{Q} subject to all constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱS:=11+Dm​i​n.Dm​i​n:=min𝐀∈𝒞𝐀,𝐐∈𝒞𝐐⁡D​(𝐀∥𝐐)\mathcal{F}\_{S}:=\frac{1}{1+D\_{min}}.\;\;\;D\_{min}:=\min\_{\mathbf{A}\in\mathcal{C}\_{\mathbf{A}},\mathbf{Q}\in\mathcal{C}\_{\mathbf{Q}}}D(\mathbf{A}\parallel\mathbf{Q}) |  | (5) |

Here 𝒞𝐀\mathcal{C}\_{\mathbf{A}} and 𝒞𝐐\mathcal{C}\_{\mathbf{Q}} denote constraint sets for transition matrices 𝐀{\bf A} and 𝐐{\bf{Q}}, respectively, according to Eqs.([1](https://arxiv.org/html/2512.05156v1#S2.E1 "In 2.4 Information Flows as Topic Weights Transitions ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"))-([3](https://arxiv.org/html/2512.05156v1#S2.E3 "In 2.4 Information Flows as Topic Weights Transitions ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")). As Dm​i​nD\_{min} can take values between zero and infinity, the
SF score 𝒞𝐀\mathcal{C}\_{\mathbf{A}} ranges from zero to one. Values of one are attained when the
two probability distributions 𝐀{\bf A} and 𝐐{\bf Q} coincide. This implies high faithfulness: the answer produces the same topical shifts that was implied by the question with respect to the context. Conversely, a small score suggests the answer’s topical focus diverges significantly from the question’s, indicating a potential lack of faithfulness.

We hasten to stress here that the minimal KL divergence Dm​i​nD\_{min}
defined in Eq.([5](https://arxiv.org/html/2512.05156v1#S2.E5 "In 2.5 Semantic Faithfulness Score ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) is a well-defined and unique quantity.
This follows
from the results of Csiszar and Tusnády [[4](https://arxiv.org/html/2512.05156v1#bib.bib4)], who showed that the problem of a joint minimization of KL divergence
D​(𝐀∥𝐐)D(\mathbf{A}\parallel\mathbf{Q}) has a solution as long as sets
𝒞𝐀\mathcal{C}\_{\mathbf{A}} and 𝒞𝐐\mathcal{C}\_{\mathbf{Q}} are convex, see also [[5](https://arxiv.org/html/2512.05156v1#bib.bib5)]. Furthermore, they also provided a constructive approach to find the solution by alternating minimization (AM) with respect to distributions
𝐀{\bf A} and 𝐐{\bf Q}.
When applied to the problem of joint minimization of D​(𝐀∥𝐐)D(\mathbf{A}\parallel\mathbf{Q}) under convex constraints, the AM method
of Csiszar and Tusnády is known as the Blahut-Arimoto (BA) algorithm [[3](https://arxiv.org/html/2512.05156v1#bib.bib3), [2](https://arxiv.org/html/2512.05156v1#bib.bib2)]. Convergence of the BA algorithm to a global minimum follows from joint convexity of D​(𝐀∥𝐐)D(\mathbf{A}\parallel\mathbf{Q}) in both its arguments, see [[6](https://arxiv.org/html/2512.05156v1#bib.bib6)], p.30.
In the following section, we will present details of an AM scheme for our setting.

## 3 Computing Semantic Faithfulness (Think Like the Demon!)

This section details the computational algorithm for finding the optimal matrices 𝐀\mathbf{A} and 𝐐\mathbf{Q} and thus computing the faithfulness score.

### 3.1 The Alternating Minimization (AM) Algorithm

The overall optimization problem is to find the pair of matrices (𝐀,𝐐)(\mathbf{A},\mathbf{Q}) that minimizes the objective function D​(𝐀∥𝐐)D(\mathbf{A}\parallel\mathbf{Q}) subject to their respective constraint sets, which we denote 𝒞𝐀\mathcal{C}\_{\mathbf{A}} and 𝒞𝐐\mathcal{C}\_{\mathbf{Q}}.
As mentioned above, this problem is jointly convex in 𝐀\mathbf{A} and
𝐐\mathbf{Q}, which provides convergence of the AM algorithm to a global minimum irrespective of a starting point.

The Alternating Minimization (AM) algorithm
[[4](https://arxiv.org/html/2512.05156v1#bib.bib4), [5](https://arxiv.org/html/2512.05156v1#bib.bib5), [6](https://arxiv.org/html/2512.05156v1#bib.bib6)] decomposes the joint optimization into a sequence of simpler sub-problems. Starting with an initial guess 𝐐(0)\mathbf{Q}^{(0)} for one matrix, the algorithm proceeds iteratively:

1. 1.

   A-update Step: With 𝐐(k)\mathbf{Q}^{(k)} held constant, solve for 𝐀(k+1)\mathbf{A}^{(k+1)}:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝐀(k+1)=arg​min𝐀∈𝒞𝐀⁡D​(𝐀∥𝐐(k))\mathbf{A}^{(k+1)}=\text{arg}\min\_{\mathbf{A}\in\mathcal{C}\_{\mathbf{A}}}D(\mathbf{A}\parallel\mathbf{Q}^{(k)}) |  |
2. 2.

   Q-update Step: With the newly computed 𝐀(k+1)\mathbf{A}^{(k+1)} held constant, solve for 𝐐(k+1)\mathbf{Q}^{(k+1)}:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝐐(k+1)=arg​min𝐐∈𝒞𝐐⁡D​(𝐀(k+1)∥𝐐)\mathbf{Q}^{(k+1)}=\text{arg}\min\_{\mathbf{Q}\in\mathcal{C}\_{\mathbf{Q}}}D(\mathbf{A}^{(k+1)}\parallel\mathbf{Q}) |  |

This process is repeated until a convergence criterion is met.
We next describe each step in this procedure to derive updating
rules for matrices 𝐀\mathbf{A} and 𝐐\mathbf{Q}.

### 3.2 A-update Step

For the A-update step, the objective is to minimize D​(𝐀∥𝐐)D(\mathbf{A}\parallel\mathbf{Q}) for a fixed 𝐐\mathbf{Q}, subject to the constraints defining 𝒞𝐀\mathcal{C}\_{\mathbf{A}}. The Lagrangian for this subproblem is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ1​(𝐀,𝝀,𝝁)=∑i,j=1Npi(c)​Ai​j​log⁡Ai​jQi​j+∑jλj​(∑i=1Npi(c)​Ai​j−pj(a))+∑i=1Nμi​pi(c)​(∑jAi​j−1)\mathcal{L}\_{1}(\mathbf{A},\text{$\lambda$},\text{$\mu$})=\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{A\_{ij}}{Q\_{ij}}+\sum\_{j}\lambda\_{j}\left(\sum\_{i=1}^{N}p\_{i}^{(c)}A\_{ij}-p\_{j}^{(a)}\right)+\sum\_{i=1}^{N}\mu\_{i}p\_{i}^{(c)}\left(\sum\_{j}A\_{ij}-1\right) |  | (6) |

where λj\lambda\_{j} and μi\mu\_{i} are Lagrange multipliers for the one-step evolution and row-stochasticity constraints, respectively. Here we additionally scaled the second (yet unknown) Lagrange multiplier
μi\mu\_{i} by the factor
pi(c)p\_{i}^{(c)} in order to simplify formulas to follow.

Setting the partial derivative of the Lagrangian with respect to Ai​jA\_{ij} to zero produces the solution for Ai​jA\_{ij}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai​j=Qi​j​e−λj−μi−1=Qi​j​e−λj∑j=1NQi​j​e−λjA\_{ij}=Q\_{ij}e^{-\lambda\_{j}-\mu\_{i}-1}=\frac{Q\_{ij}e^{-\lambda\_{j}}}{\sum\_{j=1}^{N}Q\_{ij}e^{-\lambda\_{j}}} |  | (7) |

Here at the last step we eliminated the normalization Lagrange
multipliers μi\mu\_{i} by enforcing the normalization constraint
∑j𝐀i​j=1\sum\_{j}{\bf A}\_{ij}=1.
To find the Lagrange multipliers λj\lambda\_{j}, we plug the solution back to Eq.([6](https://arxiv.org/html/2512.05156v1#S3.E6 "In 3.2 A-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) to obtain the dual Lagrangian
that should be maximized with respect to λj\lambda\_{j}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ1​(λ)=∑i,jpi(c)​log⁡(∑j=1N𝐐i​j​e−λj)−∑j=1Nλj​pj(a)\mathcal{L}\_{1}(\lambda)=\sum\_{i,j}p\_{i}^{(c)}\log\left(\sum\_{j=1}^{N}{\bf Q}\_{ij}e^{-\lambda\_{j}}\right)-\sum\_{j=1}^{N}\lambda\_{j}p\_{j}^{(a)} |  | (8) |

Equating the partial derivatives of this Lagrangian to zeros, we obtain equations for λj\lambda\_{j}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−λj​∑i=1Npi(c)​𝐐i​j∑j=1N𝐐i​j​e−λj=pj(a)e^{-\lambda\_{j}}\sum\_{i=1}^{N}\frac{p\_{i}^{(c)}{\bf Q}\_{ij}}{\sum\_{j=1}^{N}{\bf Q}\_{ij}e^{-\lambda\_{j}}}=p\_{j}^{(a)} |  | (9) |

Instead of relying on numerical convex optimization, these equations can be solved semi-analytically by converting them to fixed-point point equations for expressions
uj:=e−λju\_{j}:=e^{-\lambda\_{j}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uj=pj(a)∑i=1Npi(c)​𝐐i​j∑j=1N𝐐i​j​uj,uj:=e−λju\_{j}=\frac{p\_{j}^{(a)}}{\sum\_{i=1}^{N}\frac{p\_{i}^{(c)}{\bf Q}\_{ij}}{\sum\_{j=1}^{N}{\bf Q}\_{ij}u\_{j}}},\;\;u\_{j}:=e^{-\lambda\_{j}} |  | (10) |

and solving them by iterations. Once the fixed point 𝐮=𝐮⋆{\bf u}={\bf u}\_{\star} is found, we obtain matrix 𝐀{\bf A} using
Eq.([7](https://arxiv.org/html/2512.05156v1#S3.E7 "In 3.2 A-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai​j=Qi​j​uj∑j=1NQi​j​ujA\_{ij}=\frac{Q\_{ij}u\_{j}}{\sum\_{j=1}^{N}Q\_{ij}u\_{j}} |  | (11) |

Therefore, the AA-update step of our algorithm can be done semi-analytically.

### 3.3 Q-update Step

For the QQ-update step, the objective is to minimize D​(𝐀∥𝐐)D(\mathbf{A}\parallel\mathbf{Q}) for a fixed 𝐐\mathbf{Q}, subject to the constraints defining 𝒞𝐐\mathcal{C}\_{\mathbf{Q}}. The Lagrangian for this sub-problem is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2​(𝐐,𝝃,𝝁)=∑i,j=1Npi(c)​Ai​j​log⁡Ai​jQi​j+∑j=1Nξj​(∑ipi(c)​Qi​j−pj(q))+∑i=1Nνi​pi(c)​(∑jQi​j−1)\mathcal{L}\_{2}(\mathbf{Q},\text{$\xi$},\text{$\mu$})=\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{A\_{ij}}{Q\_{ij}}+\sum\_{j=1}^{N}\xi\_{j}\left(\sum\_{i}p\_{i}^{(c)}Q\_{ij}-p\_{j}^{(q)}\right)+\sum\_{i=1}^{N}\nu\_{i}p\_{i}^{(c)}\left(\sum\_{j}Q\_{ij}-1\right) |  | (12) |

where ξj\xi\_{j} and νi\nu\_{i} are the Lagrange multipliers for the one-step evolution and row-stochasticity constraints, respectively.
Setting the derivative ∂ℒ2∂Qi​j=0\frac{\partial\mathcal{L}\_{2}}{\partial Q\_{ij}}=0 gives:

|  |  |  |
| --- | --- | --- |
|  | −Ai​jQi​j+νi+ξj=0-\frac{A\_{ij}}{Q\_{ij}}+\nu\_{i}+\xi\_{j}=0 |  |

Solving for Qi​jQ\_{ij}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qi​j=Ai​jνi+ξjQ\_{ij}=\frac{A\_{ij}}{\nu\_{i}+\xi\_{j}} |  | (13) |

Plugging this solution back to Eq.([12](https://arxiv.org/html/2512.05156v1#S3.E12 "In 3.3 Q-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")), we obtain
the dual Lagrangian that should be maximized with respect to Lagrange multipliers 𝝃,𝝂\text{$\xi$},\text{$\nu$}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2​(𝝃,𝝂)=∑i,j=1Npi(c)​Ai​j​log⁡(νi+ξj)−∑i=1Npi(c)​νi−∑j=1Npj(q)​ξj+1\mathcal{L}\_{2}(\text{$\xi$},\text{$\nu$})=\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\left(\nu\_{i}+\xi\_{j}\right)-\sum\_{i=1}^{N}p\_{i}^{(c)}\nu\_{i}-\sum\_{j=1}^{N}p\_{j}^{(q)}\xi\_{j}+1 |  | (14) |

It is easy to verify that thus Lagrangian is separately concave in 𝝂\nu when 𝝃\xi fixed, and in 𝝃\xi when 𝝂\nu is fixed. Therefore, it can be quickly maximized using alternating maximization with respect to 𝝂\nu and 𝝃\xi while keeping the other parameter fixed.

The QQ-step and AA-step described here are iterated until convergence. The final Semantic Faithfulness calculation is summarized in Algorithm [1](https://arxiv.org/html/2512.05156v1#alg1 "Algorithm 1 ‣ 3.3 Q-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations").

Algorithm 1  The Semantic Faithfulness Algorithm

1:Input: Marginal distributions p(c)p^{(c)}, p(a)p^{(a)}, p(q)p^{(q)}, initial matrix 𝐐(0)\mathbf{Q}^{(0)}, tolerances ϵouter,ϵinner\epsilon\_{\text{outer}},\epsilon\_{\text{inner}}.

2:Initialize: Set outer loop counter k=0k=0.

3:repeat

4:// A-Step (Projection onto 𝒞𝐀\mathcal{C}\_{\mathbf{A}})

5:  Given 𝐐(k)\mathbf{Q}^{(k)}, find 𝐀(k+1)\mathbf{A}^{(k+1)} in two steps:

6:  Find scaling factors uju\_{j} for all jj by solving
Eq.([10](https://arxiv.org/html/2512.05156v1#S3.E10 "In 3.2 A-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"))

7:  Compute matrix 𝐀(k+1)\mathbf{A}^{(k+1)} using Eq.([11](https://arxiv.org/html/2512.05156v1#S3.E11 "In 3.2 A-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"))

8:// Q-Step (Projection onto 𝒞𝐐\mathcal{C}\_{\mathbf{Q}})

9:  Given 𝐀(k+1)\mathbf{A}^{(k+1)}, find 𝐐(k+1)\mathbf{Q}^{(k+1)} in two steps:

10:  Compute Lagrange multipliers 𝝃\xi and 𝝂\nu by alternating maximization:

11:  repeat

12:   Maximize the Lagrangian ([14](https://arxiv.org/html/2512.05156v1#S3.E14 "In 3.3 Q-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) for 𝝂\nu with keeping 𝝃\xi fixed.

13:   Maximize the Lagrangian ([14](https://arxiv.org/html/2512.05156v1#S3.E14 "In 3.3 Q-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) for 𝝃\xi with keeping 𝝂\nu fixed.

14:  until changes in 𝝂,𝝃\text{$\nu$},\text{$\xi$} are less than ϵinner\epsilon\_{\text{inner}}

15:  Compute the updated matrix: Qi​j(k+1)=Ai​j(k+1)νi+ξjQ\_{ij}^{(k+1)}=\frac{A\_{ij}^{(k+1)}}{\nu\_{i}+\xi\_{j}}.

16:// Check Convergence

17:  Increment k←k+1k\leftarrow k+1.

18:until change in objective function D​(𝐀(k)∥𝐐(k);p(c))D(\mathbf{A}^{(k)}\parallel\mathbf{Q}^{(k)};p^{(c)}) is less than ϵouter\epsilon\_{\text{outer}}

19:Output: Converged matrices 𝐀∗,𝐐∗\mathbf{A}^{\*},\mathbf{Q}^{\*}, the minimal divergence Dm​i​n=D​(𝐀∗∥𝐐∗)D\_{min}=D(\mathbf{A}^{\*}\parallel\mathbf{Q}^{\*}), the SF score ℱS=1/(1+Dm​i​n)\mathcal{F}\_{S}=1/(1+D\_{min}).

## 4 Semantic Entropy Production

So far we developed a semantic model for the process of text generation by a LLM as stochastic dynamics of transitions from the input context to the LLM answer, defined on a discrete-valued semantic (topic) space, and modulated by the user question that serves as a control variable.

Our analysis so far was only based on information-theoretic methods. Here we present a complimentary view of the same dynamics of the LLM as a bipartite X​YXY-information engine, this time analyzed as a physical engine. More specifically, we want to address thermodynamics of our bipartite information engine.
For a review of thermodynamics of information, see e.g. [[14](https://arxiv.org/html/2512.05156v1#bib.bib14)].

To recall the setting of our bipartite X​YXY model, both stochastic sub-systems XX and YY (the tape and controller, respectively) interact with each other and with their respective heat baths. We now want to explore transformations in sub-system XX, i.e. transitions from context CC to answer AA controlled by prompt QQ, from the point of view of thermodynamics.

In general, such transitions proceed out of equilibrium, due to both a non-equilibrium starting point (the context) and applied control by the prompt. Such non-equilibrium transitions are accompanied by entropy production. Entropy production quantifies the amount of time non-reversibility in a
given (non-equilibrium) process, and thus defines the direction of the arrow of time, see e.g. [[17](https://arxiv.org/html/2512.05156v1#bib.bib17)] for a review.

A part of entropy produced during such transitions is dissipated as heat into the environment of the system. If the environment needs to be kept at a fixed temperature, this implies that larger entropy production generally increases costs of cooling the system to maintain a fixed bath temperature. In its turn, this means that an optimal control should minimize entropy production.

In classical statistical mechanics, the concept of entropy production is normally defined at the level of a statistical ensemble of many trajectories of a statistical system with N→∞N\rightarrow\infty particles222More precisely, classical thermodynamics deals with macroscopic systems with N∼NAN\sim N\_{A} particles, where NA≃6.02×1023N\_{A}\simeq 6.02\times 10^{23} is the Avogadro constant., sampled from a given stochastic process.
In contrast, the modern field of stochastic thermodynamics
studies much smaller (’mesoscopic’) systems
where systems and ensembles can be really small, with N∼10−103N\sim 10-10^{3}. Furthermore, in stochastic thermodynamics, the concept of entropy production is defined at the level of both individual trajectories and ensembles of trajectories
[[15](https://arxiv.org/html/2512.05156v1#bib.bib15)].
The ability to compute entropy production in such mesoscopic systems at the level of single trajectories offers a possibility to monitor and control individual trajectories by choosing control protocols that minimize entropy production along these trajectories.

In our setting of of a user-LLM interaction with a given context CC, a dataset of KK triplets (Qk,C,Ak)(Q\_{k},C,A\_{k}) with k=1,…,Kk=1,\ldots,K can be viewed as a set of
triplets of transitions of sub-system XX between states C→AkC\rightarrow A\_{k} produced by ’actions’ QkQ\_{k} which effect the stage of controller YY. Importantly, we want to analyze and compute entropy production for each triplet separately in order to be able to compare them. On the other hand, each such triplet is itself
a small ensemble over topics contained in
(Qk,C,Ak)(Q\_{k},C,A\_{k}), as we do not observe individual ’topic trajectories’ that would start with a single topic, rather than the whole prompt-context combination Q,CQ,C.

This view of the LLM enables employing methods of computing entropy production from stochastic thermodynamics in our problem of comparison of individual Q​C​AQCA-triplets.
The prompt-answer pair that gives rise to the minimum entropy production may be suggested as the best (most efficient, least heat-dissipating) candidate in the set.

As shown in [[16](https://arxiv.org/html/2512.05156v1#bib.bib16)], total entropy production for a stochastic system is given by the KL divergence between the probabilities of the forward and backward (time-reversed) paths.
In our one-step setting, this produces the following expression for the total entropy production S.t​o​t\overset{\bm{.}}{S}\_{tot}:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | S.t​o​t\displaystyle\overset{\bm{.}}{S}\_{tot} | =\displaystyle= | ∑i,j=1Npi(c)​Ai​j​log⁡pi(c)​Ai​jpj(a)​Aj​iR=∑i,j=1Npi(c)​Ai​j​log⁡Ai​jAj​iR+∑i,j=1Npi(c)​Ai​j​log⁡pi(c)pj(a)\displaystyle\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{p\_{i}^{(c)}A\_{ij}}{p\_{j}^{(a)}A\_{ji}^{R}}=\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{A\_{ij}}{A\_{ji}^{R}}+\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{p\_{i}^{(c)}}{p\_{j}^{(a)}} |  | (15) |
|  |  | =\displaystyle= | ∑i,j=1Npi(c)​Ai​j​log⁡Ai​jAj​iR+H​[p(a)]−H​[p(c)]\displaystyle\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{A\_{ij}}{A\_{ji}^{R}}+H\left[p^{(a)}\right]-H\left[p^{(c)}\right] |  |

Here 𝐀R{\bf A}^{R} stands for the transition matrix of the time-reversed process. As this quantity is not directly measured from our data, Eq.([15](https://arxiv.org/html/2512.05156v1#S4.E15 "In 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) is not sufficient on its own for computing entropy production without additional assumptions or approximations.
Before we proceed with our estimation of this quantity, we pause to make a few remarks.

### 4.1 Decomposition of the Total Entropy Production

As discussed in [[16](https://arxiv.org/html/2512.05156v1#bib.bib16)], the structure of Eq.([15](https://arxiv.org/html/2512.05156v1#S4.E15 "In 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) suggests the following decomposition for the total entropy production:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S.t​o​t=S.m+S.\overset{\bm{.}}{S}\_{tot}=\overset{\bm{.}}{S}\_{m}+\overset{\bm{.}}{S} |  | (16) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | S.m=∑i,j=1Npi(c)​Ai​j​log⁡Ai​jAj​iR\overset{\bm{.}}{S}\_{m}=\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{A\_{ij}}{A\_{ji}^{R}} |  | (17) |

is the entropy (or, equivalently, heat) dissipated to the heat bath (medium), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | S.=∑i,j=1Npi(c)​Ai​j​log⁡pi(c)pj(a)=H​[p(a)]−H​[p(c)]\overset{\bm{.}}{S}=\sum\_{i,j=1}^{N}p\_{i}^{(c)}A\_{ij}\log\frac{p\_{i}^{(c)}}{p\_{j}^{(a)}}=H\left[p^{(a)}\right]-H\left[p^{(c)}\right] |  | (18) |

is the entropy change of sub-system XX. We next separately discuss these two contributions to the total entropy production S.t​o​t\overset{\bm{.}}{S}\_{tot} in sub-system XX.

### 4.2 Semantic Entropy or Semantic Entropy Production?

Let us consider first the sub-system XX entropy change term ([18](https://arxiv.org/html/2512.05156v1#S4.E18 "In 4.1 Decomposition of the Total Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")). It amounts to the difference H​[p(a)]−H​[p(c)]H\left[p^{(a)}\right]-H\left[p^{(c)}\right] of marginal final and initial entropies. The first term here is the semantic Shannon entropy of the LLM answer. This quantity was previously suggested on heuristic grounds in the Semantic Entropy (SE) method [[8](https://arxiv.org/html/2512.05156v1#bib.bib8)] as a metric for LLM hallucination control. As was noted in [[9](https://arxiv.org/html/2512.05156v1#bib.bib9)], one drawback of the SE method is that it does not account for complexity of the initial context (or prompt).

On the other hand, the present work suggests that it is entropy production, rather than the marginal entropy of the LLM answer, that may be a better metric for quantification of uncertainty and confidence of LLM answers. We see that the system entropy change
([18](https://arxiv.org/html/2512.05156v1#S4.E18 "In 4.1 Decomposition of the Total Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) appears a more meaningful way to quantify entropy of the LLM answer by computing its difference with entropy of the context. Furthermore, the concept of entropy production is intuitively related to the notion of LLM hallucinations as noisy (entropy-increasing) distortions of the input context and prompt data.

Now, the sub-system XX entropy change ([18](https://arxiv.org/html/2512.05156v1#S4.E18 "In 4.1 Decomposition of the Total Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) can be directly calculated from the marginal distribution, but it amounts only to one contribution into the total entropy production according to Eq.([16](https://arxiv.org/html/2512.05156v1#S4.E16 "In 4.1 Decomposition of the Total Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")). The other term S.m\overset{\bm{.}}{S}\_{m} defined
in Eq.([17](https://arxiv.org/html/2512.05156v1#S4.E17 "In 4.1 Decomposition of the Total Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) cannot be directly calculated as long as the reverse transition matrix 𝐀R{\bf A}^{R} is not known or estimated.
We will next propose a method to estimate the dissipated entropy
S.m\overset{\bm{.}}{S}\_{m} by computing its lower bound.

### 4.3 Lower Bound on Semantic Entropy Production

As the reverse transition matrix 𝐀R{\bf A}^{R} is not directly measured, the exact amount of entropy production according to Eq.([15](https://arxiv.org/html/2512.05156v1#S4.E15 "In 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) is unknown.
However, we can find a lower bound on entropy production in our process by minimizing the expression ([15](https://arxiv.org/html/2512.05156v1#S4.E15 "In 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) with respect to all possible reverse transition matrices 𝐀R{\bf A}^{R}, subject to all constraints that should be imposed on these matrices [[11](https://arxiv.org/html/2512.05156v1#bib.bib11)].
In our case, matrix 𝐀R{\bf A}^{R} should satisfy the marginal and normalization constraints

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1Npj(a)​Aj​iR=pi(c),∑i=1NAj​iR=1\sum\_{j=1}^{N}p\_{j}^{(a)}A\_{ji}^{R}=p\_{i}^{(c)},\;\;\;\sum\_{i=1}^{N}A\_{ji}^{R}=1 |  | (19) |

([19](https://arxiv.org/html/2512.05156v1#S4.E19 "In 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")). This produces the following Lagrangian function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒS​(𝐀R,𝝃,𝝂)=∑i,jpi(c)​Ai​j​log⁡Ai​jAi​jR+∑iξi​(∑ipj(a)​Aj​iR−pi(c))+∑jνj​pj(c)​(∑iAj​iR−1)\mathcal{L}\_{S}({\bf A}^{R},\text{$\xi$},\text{$\nu$})=\sum\_{i,j}p\_{i}^{(c)}A\_{ij}\log\frac{A\_{ij}}{A\_{ij}^{R}}+\sum\_{i}\xi\_{i}\left(\sum\_{i}p\_{j}^{(a)}A\_{ji}^{R}-p\_{i}^{(c)}\right)+\sum\_{j}\nu\_{j}p\_{j}^{(c)}\left(\sum\_{i}A\_{ji}^{R}-1\right) |  | (20) |

where ξj\xi\_{j} and νj\nu\_{j} are Lagrange multipliers.
Minimization of this Lagrangian with respect to 𝐀R{\bf A}^{R} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aj​iR=pi(c)ξi​pj(a)+νj​pj(c)​Ai​jA\_{ji}^{R}=\frac{p\_{i}^{(c)}}{\xi\_{i}p\_{j}^{(a)}+\nu\_{j}p\_{j}^{(c)}}A\_{ij} |  | (21) |

Plugging this back into ([20](https://arxiv.org/html/2512.05156v1#S4.E20 "In 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")), rescaling the optimization variables νj→νj​pj(c)/pj(a)\nu\_{j}\rightarrow\nu\_{j}p\_{j}^{(c)}/p\_{j}^{(a)} and simplifying the resulting expression, we obtain the dual Lagrangian that should be maximized with respect to the Lagrange multipliers:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ℒS​(𝝃,𝝂)\displaystyle\mathcal{L}\_{S}(\text{$\xi$},\text{$\nu$}) | =\displaystyle= | ∑i,jpi(c)​Ai​j​log⁡(ξi+νj)−∑ipi(c)​ξi−∑jpj(a)​νj+1\displaystyle\sum\_{i,j}p\_{i}^{(c)}A\_{ij}\log\left(\xi\_{i}+\nu\_{j}\right)-\sum\_{i}p\_{i}^{(c)}\xi\_{i}-\sum\_{j}p\_{j}^{(a)}\nu\_{j}+1 |  | (22) |
|  |  | =\displaystyle= | ℒ2​(𝝃,𝝂)+∑j=1Nνj​(pj(q)−pj(a))\displaystyle\mathcal{L}\_{2}(\text{$\xi$},\text{$\nu$})+\sum\_{j=1}^{N}\nu\_{j}\left(p\_{j}^{(q)}-p\_{j}^{(a)}\right) |  |

where ℒ2​(𝝃,𝝂)\mathcal{L}\_{2}(\text{$\xi$},\text{$\nu$}) is the Lagrangian defined in Eq.([14](https://arxiv.org/html/2512.05156v1#S3.E14 "In 3.3 Q-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")). Therefore, the remaining maximization in Eq.([22](https://arxiv.org/html/2512.05156v1#S4.E22 "In 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) can be done using the same objective functions in in the QQ-step of our Semantic Faithfulness algorithm, upon the substitution 𝐩(q)→𝐩(a){\bf p}^{(q)}\rightarrow{\bf p}^{(a)}. Alternatively, if the second term in the last expression in Eq.([22](https://arxiv.org/html/2512.05156v1#S4.E22 "In 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) is much smaller than the first term, the optimal value of ℒS​(𝝃,𝝂)\mathcal{L}\_{S}(\text{$\xi$},\text{$\nu$})
can be computed to the first order in the perturbation as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒS​(𝝃⋆,𝝂⋆)≃ℒ2​(𝝃⋆,𝝂⋆)+∑j=1Nνj⋆​(pj(q)−pj(a))\mathcal{L}\_{S}(\text{$\xi$}^{\star},\text{$\nu$}^{\star})\simeq\mathcal{L}\_{2}(\text{$\xi$}^{\star},\text{$\nu$}^{\star})+\sum\_{j=1}^{N}\nu\_{j}^{\star}\left(p\_{j}^{(q)}-p\_{j}^{(a)}\right) |  | (23) |

where 𝝃⋆,𝝂⋆\text{$\xi$}^{\star},\text{$\nu$}^{\star} are the optimal Lagrange multipliers for the Lagrangian ℒ2​(𝝃,𝝂)\mathcal{L}\_{2}(\text{$\xi$},\text{$\nu$}).
The final scheme is presented in Algorithm [2](https://arxiv.org/html/2512.05156v1#alg2 "Algorithm 2 ‣ 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations").

Algorithm 2  Semantic Entropy Production (SEP)

1:𝐀∗\mathbf{A}^{\*} (optimal transition matrix from Algorithm [1](https://arxiv.org/html/2512.05156v1#alg1 "Algorithm 1 ‣ 3.3 Q-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")), 𝐩(c)\mathbf{p}^{(c)}, 𝐩(a)\mathbf{p}^{(a)}

2:Initialize 𝝃,𝝂∈ℝ>0N\bm{\xi},\bm{\nu}\in\mathbb{R}^{N}\_{>0}

3:repeat

4:  𝝃\bm{\xi}-step: Maximize ℒS​(𝝃,𝝂)\mathcal{L}\_{S}(\bm{\xi},\bm{\nu}) w.r.t. 𝝃\bm{\xi} (fixing 𝝂\bm{\nu}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξi∗=argmaxξi​[∑jpi(c)​Ai​j∗​log⁡(ξi+νj)−pi(c)​ξi]\xi\_{i}^{\*}=\text{argmax}\_{\xi\_{i}}\left[\sum\_{j}p\_{i}^{(c)}A^{\*}\_{ij}\log(\xi\_{i}+\nu\_{j})-p\_{i}^{(c)}\xi\_{i}\right] |  | (24) |

5:  𝝂\bm{\nu}-step: Maximize ℒS​(𝝃,𝝂)\mathcal{L}\_{S}(\bm{\xi},\bm{\nu}) w.r.t. 𝝂\bm{\nu} (fixing 𝝃\bm{\xi}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | νj∗=argmaxνj​[∑ipi(c)​Ai​j∗​log⁡(ξi+νj)−pj(a)​νj]\nu\_{j}^{\*}=\text{argmax}\_{\nu\_{j}}\left[\sum\_{i}p\_{i}^{(c)}A^{\*}\_{ij}\log(\xi\_{i}+\nu\_{j})-p\_{j}^{(a)}\nu\_{j}\right] |  | (25) |

6:until convergence of ℒS​(𝝃,𝝂)\mathcal{L}\_{S}(\bm{\xi},\bm{\nu})

7:Recover Aj​iR=Ai​j∗ξi∗+νj∗A^{R}\_{ji}=\dfrac{A^{\*}\_{ij}}{\xi\_{i}^{\*}+\nu\_{j}^{\*}}

8:return SEP =D​(𝐀∗∥𝐀R)=∑i,jpi(c)​Ai​j∗​log⁡Ai​j∗Aj​iR=D(\mathbf{A}^{\*}\|\mathbf{A}^{R})=\sum\_{i,j}p\_{i}^{(c)}A^{\*}\_{ij}\log\dfrac{A^{\*}\_{ij}}{A^{R}\_{ji}}

### 4.4 Relationship Between Faithfulness and Entropy Production

The approximate expression ([23](https://arxiv.org/html/2512.05156v1#S4.E23 "In 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) suggests
a link between the (lower bound of) entropy production and
the Faithfulness Score ([5](https://arxiv.org/html/2512.05156v1#S2.E5 "In 2.5 Semantic Faithfulness Score ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")). As the first term in ([23](https://arxiv.org/html/2512.05156v1#S4.E23 "In 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) is exactly the quantity Dm​i​n=1/ℱS−1D\_{min}=1/\mathcal{F}\_{S}-1 (with added constraint penalties), Eq.([23](https://arxiv.org/html/2512.05156v1#S4.E23 "In 4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) can be written as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S.t​o​t=1/ℱS−1+∑j=1Nνj⋆​(pj(q)−pj(a))\overset{\bm{.}}{S}\_{tot}=1/\mathcal{F}\_{S}-1+\sum\_{j=1}^{N}\nu\_{j}^{\star}\left(p\_{j}^{(q)}-p\_{j}^{(a)}\right) |  | (26) |

When the correction term (the sum) is negligible, this yields the “naive” approximation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S.t​o​t≈Dm​i​n=1ℱS−1\overset{\bm{.}}{S}\_{tot}\approx D\_{min}=\frac{1}{\mathcal{F}\_{S}}-1 |  | (27) |

To explore the relationship between ℱS\mathcal{F}\_{S} and SEP beyond such naive approximation, we generated 100 synthetic QCA triplets that preserve the key statistical properties observed in the real data presented in next section. Specifically, we sampled distributions p​(Q)p(Q), p​(C)p(C), and p​(A)p(A) using Dirichlet distributions with concentration parameters
calibrated to match the sparsity patterns that we observe in real datasets: questions exhibit high sparsity (concentrated on few topics), contexts are more diffuse (spread across many topics),
and answers show intermediate sparsity.
We also preserved the empirical co-dependencies by sampling answer distributions conditionally on context distributions, reflecting the fact that LLM answers draw selectively from the provided context.
For each synthetic triplet, we computed both the SF (ℱS\mathcal{F}\_{S}), and SEP metrics using, respectively, Algorithms 1 and 2.
Figure [1](https://arxiv.org/html/2512.05156v1#S4.F1 "Figure 1 ‣ 4.4 Relationship Between Faithfulness and Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") presents a scatter plot of SF versus SEP, comparing the naive approximation ([27](https://arxiv.org/html/2512.05156v1#S4.E27 "In 4.4 Relationship Between Faithfulness and Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) with the exact calculation.

![Refer to caption](figures/SF_SEP_scatter.png)


Figure 1: Scatter plot of Semantic Faithfulness (ℱS\mathcal{F}\_{S}) versus Semantic Entropy Production (SEP) for n=100n=100 simulated QCA triplets. The solid red line shows the linear
regression fit (SEP =−1.76⋅ℱS+2.02=-1.76\cdot\mathcal{F}\_{S}+2.02), while the dashed green line shows the naive approximation SEP =1/ℱS−1=1/\mathcal{F}\_{S}-1 from Eq. ([27](https://arxiv.org/html/2512.05156v1#S4.E27 "In 4.4 Relationship Between Faithfulness and Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")).

This analysis of simulated triplets reveals a moderate negative correlation between ℱS\mathcal{F}\_{S} and SEP (Pearson r=−0.61r=-0.61), confirming that higher semantic faithfulness generally corresponds to lower entropy production. However, the relationship is weaker than the naive approximation SEP ≈1/ℱS−1\approx 1/\mathcal{F}\_{S}-1 would
suggest. A linear fit yields SEP =−1.76⋅ℱS+2.02=-1.76\cdot\mathcal{F}\_{S}+2.02, indicating that while the metrics are related, they capture distinct aspects of information flow in QCA triplets, and should therefore be
computed independently, without reliance on the naive approximation
([27](https://arxiv.org/html/2512.05156v1#S4.E27 "In 4.4 Relationship Between Faithfulness and Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")).

### 4.5 Final Metrics: Semantic Faithfulness and Semantic Entropy Production

Our framework provides two complementary metrics for LLM faithfulness evaluation:

1. 1.

   Semantic Faithfulness (SF): The score ℱS=1/(1+Dm​i​n)\mathcal{F}\_{S}=1/(1+D\_{min}) defined in Eq. ([5](https://arxiv.org/html/2512.05156v1#S2.E5 "In 2.5 Semantic Faithfulness Score ‣ 2 Semantic Faithfulness ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")), computed via the alternating minimization
   Algorithm [1](https://arxiv.org/html/2512.05156v1#alg1 "Algorithm 1 ‣ 3.3 Q-update Step ‣ 3 Computing Semantic Faithfulness (Think Like the Demon!) ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"). This metric quantifies the information-theoretic alignment between the question-induced and answer-induced topic transformations.
2. 2.

   Semantic Entropy Production (SEP): The lower bound on total entropy production S.t​o​t\overset{\bm{.}}{S}\_{tot} computed via a separate optimization as described in
   Section [4.3](https://arxiv.org/html/2512.05156v1#S4.SS3 "4.3 Lower Bound on Semantic Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations"). This metric quantifies the thermodynamic irreversibility of the answer generation process.

Our simulation results in Figure [1](https://arxiv.org/html/2512.05156v1#S4.F1 "Figure 1 ‣ 4.4 Relationship Between Faithfulness and Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") demonstrate
that SF and SEP are related but not redundant, as they capture distinct, though connected, aspects of QCA triplet quality.
Indeed, SF is the information-theoretic metric that captures the *semantic alignment* between question intent and answer content. On the other hand,
SEP captures the *thermodynamic efficiency* of the information transformation. We therefore recommend computing both metrics independently for comprehensive faithfulness evaluation. As a byproduct of the optimization algorithms, we also obtain the optimal
transition matrices 𝐐⋆\mathbf{Q}^{\star} and 𝐀⋆\mathbf{A}^{\star} that achieve the minimal divergence, providing interpretable representations of topic flow from context to question
and answer, see Figures [5](https://arxiv.org/html/2512.05156v1#S5.F5 "Figure 5 ‣ 5.4 Visualizations ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") and [6](https://arxiv.org/html/2512.05156v1#S5.F6 "Figure 6 ‣ 5.4 Visualizations ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") below for typical marginal distributions and optimal transition matrices, respectively, that are obtained with our datasets. Details of our datasets will be presented in the next section.

## 5 Experiments

We conducted experiments to validate our Semantic Faithfulness framework on a dataset of 10 rich Question-Context-Answer (QCA) triplets.333All code, data, and reproducibility materials are available at: <https://github.com/ighalp/semantic-faithfulness-sdm> Each triplet consisted of a carefully crafted question, a comprehensive multi-paragraph context document, and a detailed LLM-generated answer.

### 5.1 Dataset Construction

#### Context Document.

The context for all QCA triplets was extracted from NVIDIA Corporation’s fiscal year 2024 Annual Report (Form 10-K), specifically the comprehensive Risk Factors section (Item 1A). This section spans approximately 60,000 characters and provides detailed disclosures of risks across multiple categories:

* •

  Risks related to industry and markets (competitive dynamics, evolving customer needs)
* •

  Risks related to demand, supply, and manufacturing (supply chain dependencies, demand forecasting)
* •

  Risks related to global operations (macroeconomic factors, international exposure, cybersecurity)
* •

  Regulatory, legal, and governance risks (export controls, IP protection, tax policies)

#### Question Design Strategy.

To systematically investigate the relationship between question semantic structure and Semantic Faithfulness, we constructed 10 QCA triplets organized into two groups based on semantic focus:

* •

  Group A (Comprehensive Risk Analysis): 5 paraphrases of a broad multi-topic question covering NVIDIA’s entire risk landscape (supply chain, competition, product lifecycle, regulations, etc.). These paraphrases vary in phrasing and emphasis while maintaining the same comprehensive scope, resulting in moderate question entropy variation (CV ≈\approx 25%).
* •

  Group B (Competitive Threats Focus): 5 paraphrases of a qualitatively different question focused specifically on competitive dynamics (hyperscaler custom silicon, AMD/Intel alternatives, CUDA lock-in erosion, workload evolution). These paraphrases exhibit tight semantic clustering (CV ≈\approx 2%), with all questions converging on the competitive threat theme.

#### Answer-Question Generation.

All questions were answered using Claude Sonnet 4.5 (Anthropic), a state-of-the-art large language model. Each question shared the same context (NVIDIA 10-K Risk Factors disclosure, ∼\sim60,000 characters). Group A questions elicited comprehensive multi-section risk analyses (∼\sim15,000 characters) covering all major risk categories, while Group B questions produced focused competitive analyses (∼\sim20,000 characters) with detailed technical comparisons of alternative AI accelerators and strategic implications.
All answers were generated using Gemini-2.5-Pro LLM model.

#### Computational Pipeline.

For each QCA triplet, we computed semantic distributions over topics using the following efficient caching strategy:

1. 1.

   Embedding: All text was decomposed into sentences (1,514 total sentences across prompts, context, and answers) and embedded using the Qwen3-Embedding-0.6B model in a *single* embedding pass, producing dense vector representations cached to disk.
2. 2.

   Clustering: The joint embedding space was clustered into N=23N=23 semantic topics using the Upper-Bounded Deterministic Information Bottleneck (UDIB) algorithm [[10](https://arxiv.org/html/2512.05156v1#bib.bib10)] in a *single* clustering pass. The UDIB method simultaneously performs clustering and determines the optimal number of clusters by maximizing the information bottleneck objective, discretizing the continuous semantic space into interpretable topic distributions.
3. 3.

   Distributions: For each triplet’s question QQ, context CC, and answer AA, we computed the probability distribution over topics by aggregating sentence cluster assignments and normalizing counts to obtain pqp\_{q}, pcp\_{c}, and pap\_{a}.
4. 4.

   Caching: All embeddings, cluster labels, and distributions were pre-computed once and cached, enabling instantaneous metric evaluation across multiple runs without redundant computation (saving ∼\sim5-10 minutes per analysis).

### 5.2 Results

Table [1](https://arxiv.org/html/2512.05156v1#S5.T1 "Table 1 ‣ 5.2 Results ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") presents the computed metrics for all 10 QCA triplets. Context entropy H​(C)=3.279H(C)=3.279 bits is constant across all triplets as they share the same source
document. All entropy values are reported in bits.

Table 1: Entropy values and computed metrics for all QCA triplets.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Triplet | Group | H​(Q)H(Q) | H​(C)H(C) | H​(A)H(A) | S.\overset{\bm{.}}{S} | ℱS\mathcal{F}\_{S} | SEP |
| A0 | A | 1.447 | 3.279 | 3.905 | 0.627 | 0.472 | 0.771 |
| A1 | A | 2.000 | 3.279 | 3.864 | 0.585 | 0.477 | 0.596 |
| A2 | A | 3.122 | 3.279 | 4.107 | 0.829 | 0.577 | 0.076 |
| A3 | A | 2.922 | 3.279 | 4.022 | 0.744 | 0.502 | 0.149 |
| A4 | A | 2.500 | 3.279 | 4.129 | 0.851 | 0.516 | 0.202 |
| B0 | B | 2.683 | 3.279 | 3.672 | 0.393 | 0.523 | 0.242 |
| B1 | B | 2.585 | 3.279 | 3.666 | 0.387 | 0.477 | 0.280 |
| B2 | B | 2.777 | 3.279 | 3.596 | 0.318 | 0.528 | 0.225 |
| B3 | B | 2.689 | 3.279 | 3.664 | 0.386 | 0.489 | 0.103 |
| B4 | B | 2.624 | 3.279 | 3.663 | 0.384 | 0.500 | 0.227 |
| Group A mean | | 2.398 | 3.279 | 4.006 | 0.727 | 0.509 | 0.359 |
| Group B mean | | 2.671 | 3.279 | 3.652 | 0.374 | 0.503 | 0.215 |
| Overall mean | | 2.535 | 3.279 | 3.829 | 0.550 | 0.506 | 0.287 |

### 5.3 Analysis and Discussion

Our experimental results produced several important observations regarding the relationship between question structure, semantic faithfulness, and entropy production.

#### Meaningful Question Entropy Variation.

Our question set achieves meaningful entropy variation. All 10 triplets exhibit substantial question entropy (H​(Q)∈[1.447,3.122]H(Q)\in[1.447,3.122] bits, mean = 2.535 bits, CV = 18%). The
controlled two-group design demonstrates considerably different variance: Group B (competitive threats) shows tight clustering (CV = 2.4%), while Group A (comprehensive risk)
exhibits broader variation (CV = 25.5%).

#### Question Semantic Structure Impact.

Both groups exhibit similar mean Semantic Faithfulness (Group A: ℱS=0.509\mathcal{F}\_{S}=0.509, Group B: ℱS=0.503\mathcal{F}\_{S}=0.503), indicating that question type alone does not strongly
determine faithfulness in this dataset. However, individual triplet variation within groups (overall ℱS\mathcal{F}\_{S} range: [0.472, 0.577]) suggests that specific question-context
pairings matter more than broad question categories. We observe a positive correlation between H​(Q)H(Q) and ℱS\mathcal{F}\_{S} (Pearson r=0.695r=0.695, p=0.026p=0.026), see
Fig. [2](https://arxiv.org/html/2512.05156v1#S5.F2 "Figure 2 ‣ 5.4 Visualizations ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations").

#### Positive System Entropy Change.

The experimental results exhibit *positive* system entropy change S.=H​(A)−H​(C)\overset{\bm{.}}{S}=H(A)-H(C) across all triplets (mean: 0.550 bits, range: [0.318, 0.851] bits). This indicates that
the LLM systematically *increases* semantic uncertainty when generating answers: the answer distributions are more dispersed (higher entropy)
than the context distributions. Group A questions induce stronger entropy expansion (mean S.\overset{\bm{.}}{S} = 0.727 bits) compared to Group B (mean = 0.374 bits), suggesting that comprehensive
questions elicit more semantically diverse responses.

#### Semantic Entropy Production.

Our results reveal an interesting thermodynamic signature: while system entropy change S.=H​(A)−H​(C)\overset{\bm{.}}{S}=H(A)-H(C) is substantially positive (mean = 0.550 bits, indicating semantic
expansion), the SEP values show meaningful variation (mean = 0.287 bits, range: [0.076, 0.771] bits). Group A exhibits *higher* SEP (mean = 0.359 bits) than Group B (mean = 0.215
bits), consistent with Group A’s higher system entropy change.

Recall from stochastic thermodynamics that total entropy production decomposes as S˙tot=S.+S.m\dot{S}\_{\text{tot}}=\overset{\bm{.}}{S}+\overset{\bm{.}}{S}\_{m}, where S.m\overset{\bm{.}}{S}\_{m} represents dissipated heat from subsystem
XX (question-answer channel) to subsystem YY (LLM’s internal knowledge base) plus the environment, see Eq.([16](https://arxiv.org/html/2512.05156v1#S4.E16 "In 4.1 Decomposition of the Total Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")). Notably, in all triplets except A0, we observe SEP <S.<\overset{\bm{.}}{S}, which implies S.m<0\overset{\bm{.}}{S}\_{m}<0: the dissipated heat is *negative*. The physical interpretation is that to generate answers with higher entropy than the provided context
(semantic expansion), the LLM must draw information from its internal knowledge base (subsystem YY), effectively importing semantic structure that reduces the net entropy production
of the question-answering process. This negative heat flow indicates that subsystem XX *absorbs* rather than dissipates entropy.

The coefficient of variation for SEP (73%) indicates meaningful variation across triplets, suggesting that entropy production provides discriminative signal for comparing answer
quality beyond what ℱS\mathcal{F}\_{S} alone captures. The correlation between ℱS\mathcal{F}\_{S} and SEP is r=−0.612r=-0.612 (p=0.060p=0.060), see Fig. [3](https://arxiv.org/html/2512.05156v1#S5.F3 "Figure 3 ‣ 5.4 Visualizations ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations").

#### Algorithm Convergence and Robustness.

Both algorithms converged reliably for all triplets, achieving constraint satisfaction to numerical precision. The SF algorithm uses alternating A-step and Q-step optimization, while
the SEP algorithm employs L-BFGS-B optimization for dual Lagrangian maximization.

### 5.4 Visualizations

Figure [2](https://arxiv.org/html/2512.05156v1#S5.F2 "Figure 2 ‣ 5.4 Visualizations ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") shows a scatter plot of QCA triplets in the question entropy-semantic faithfulness plane.
Figure [3](https://arxiv.org/html/2512.05156v1#S5.F3 "Figure 3 ‣ 5.4 Visualizations ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") shows the relationship between ℱS\mathcal{F}\_{S} and SEP with regression lines for each group.
Figure [4](https://arxiv.org/html/2512.05156v1#S5.F4 "Figure 4 ‣ 5.4 Visualizations ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") shows the thermodynamic decomposition of SEP into system entropy change and dissipated heat.

![Refer to caption](figures/fig1_hq_vs_fs.png)


Figure 2: Scatter plot of QCA triplets in the question entropy-Semantic Faithfulness plane. The global fit across both groups produces positive Pearson correlation (r=0.695r=0.695, p=0.026p=0.026), indicating that higher question entropy is associated with higher semantic faithfulness. Group A (red) exhibits broader variation in both H​(Q)H(Q) and ℱS\mathcal{F}\_{S}, while
Group B (blue) shows tighter clustering.

![Refer to caption](figures/fig5_fs_vs_sep_updated.png)


Figure 3: Relationship between Semantic Faithfulness ℱS\mathcal{F}\_{S} and Semantic Entropy Production (SEP). The global correlation is negative (r=−0.612r=-0.612, p=0.060p=0.060), consistent
with the expectation that higher faithfulness corresponds to lower entropy production. Group A (red, comprehensive questions) shows strong within-group negative correlation (r=−0.804r=-0.804), while Group B (blue, competitive questions) shows no significant within-group correlation (r=0.121r=0.121).

![Refer to caption](figures/fig6_sep_components_updated.png)


Figure 4: Thermodynamic decomposition of SEP showing dissipated heat S.m\overset{\bm{.}}{S}\_{m} versus system entropy change S.=H​(A)−H​(C)\overset{\bm{.}}{S}=H(A)-H(C). Group A (red) exhibits higher system entropy change
and wider variation in dissipated heat, while Group B (blue) clusters at lower S.\overset{\bm{.}}{S} values. Negative S.m\overset{\bm{.}}{S}\_{m} values indicate that the LLM draws on its internal knowledge base to
offset entropy production during answer generation.

![Refer to caption](figures/Marginal_distributions.png)


Figure 5: Probability distributions over semantic topics for triplet A0. Left: Question distribution p​(Q)p(Q) is sparse, concentrated on a few semantic clusters. Center: Context
distribution p​(C)p(C) is more diffuse, covering many topics from the source document. Right: Answer distribution p​(A)p(A) shows intermediate sparsity, reflecting how the LLM selectively
addresses topics from the context to answer the question. These distributions serve as inputs to the SF and SEP algorithms.

![Refer to caption](figures/Q_star_A_star_matrices.png)


Figure 6: Optimal transition matrices 𝐐⋆\mathbf{Q}^{\star} (left, blue colormap) and 𝐀⋆\mathbf{A}^{\star} (right, green colormap) inferred by the alternating minimization algorithm for
triplet A0. The 𝐐⋆\mathbf{Q}^{\star} matrix encodes the optimal topic transformation from context to question, while 𝐀⋆\mathbf{A}^{\star} encodes the transformation from context to
answer. Both matrices exhibit sparse structure with probability mass concentrated along specific topic mappings. The Semantic Faithfulness score ℱS\mathcal{F}\_{S} quantifies how closely
these two matrices align.

### 5.5 Qualitative Evaluation with LLM-as-a-Judge

A fundamental question for any faithfulness metric is whether it aligns with human judgment: do answers with higher ℱS\mathcal{F}\_{S} and lower SEP correspond to what human evaluators
would reasonably identify as better responses? To investigate this hypothesis, we employ the LLM-as-a-Judge methodology [[18](https://arxiv.org/html/2512.05156v1#bib.bib18)], using Claude Sonnet 4.5 to simulate
the human process of evaluating multiple LLM-generated answers and selecting the best one.

Our hypothesis is that the Semantic Faithfulness metric ℱS\mathcal{F}\_{S} and Semantic Entropy Production (SEP) provide effective guidance for answer selection, capturing dimensions of
quality that human evaluators would recognize: structural alignment with question requirements, comprehensive coverage of requested topics, appropriate grounding in context, and
absence of tangential or repetitive content.

We compare answers with the highest and lowest ℱS\mathcal{F}\_{S} scores from a separate experimental run using Group A comprehensive risk questions.444The ℱS\mathcal{F}\_{S} values
reported in this section (0.872 and 0.250) differ from those in Table [1](https://arxiv.org/html/2512.05156v1#S5.T1 "Table 1 ‣ 5.2 Results ‣ 5 Experiments ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations") because they were computed in a different experimental session with different random
initialization. This variability is expected and does not affect the qualitative conclusions. For each pair, we present both answers to the LLM with instructions to
analyze faithfulness, completeness, coherence, and relevance. The qualitative analysis reported below is provided verbatim as generated by Claude Sonnet 4.5.

#### Group A Analysis (Comprehensive Risk Questions).

Answer A (ℱS=0.872\mathcal{F}\_{S}=0.872) produced a structured response organized around four numbered sections: (1) Supply Chain Dependencies and Demand Forecasting Challenges,
(2) Competitive Risks and Operational Challenges, (3) Impact of External Factors: Export Controls and Macroeconomics, and (4) Financial Illustration and Customer Concentration. The
answer maintains direct alignment with the question’s framework and concludes with a concise summary paragraph that ties all elements together.

Answer B (ℱS=0.250\mathcal{F}\_{S}=0.250) produced a longer response with an executive summary, more detailed subsections, and extensive bullet points. While covering similar
material, the answer includes additional elements such as cybersecurity threats and EU AI Act regulatory compliance, and provides a more extensive final section on “Implications for
Financial Health and Long-Term Standing.”

#### LLM Judge Evaluation.

The LLM judge scored both answers identically across all four evaluation criteria:

| Criterion | Answer A | Answer B | Diff | Better |
| --- | --- | --- | --- | --- |
| Faithfulness | 9/10 | 9/10 | 0 | = |
| Completeness | 9/10 | 9/10 | 0 | = |
| Coherence | 9/10 | 9/10 | 0 | = |
| Relevance | 9/10 | 9/10 | 0 | = |
| Overall | 9/10 | 9/10 | 0 | TIE |

The judge’s detailed explanation noted: “Both answers provide excellent, comprehensive assessments of NVIDIA’s vulnerabilities that are highly faithful to the context.” Key
observations include:

* •

  Both answers accurately describe supply chain dependencies on third-party manufacturers in geopolitically sensitive regions (Taiwan, China)
* •

  Both explain the long lead times (12+ months) and demand forecasting challenges
* •

  Both cite the same specific financial examples: inventory provisions for low-yielding Blackwell material (Q2 FY2025) and warranty liability from third-party component defects
  (FY2023)
* •

  Both discuss competitive risks from rivals and customers developing their own solutions
* •

  Both address customer concentration and export controls comprehensively

The judge characterized the differences as “stylistic rather than substantive”: Answer A is “slightly more focused and concise,” while Answer B is “slightly more comprehensive in
scope” with additional analytical framing.

#### Implications for Semantic Faithfulness Validation.

The LLM judge’s inability to distinguish between answers with substantially different ℱS\mathcal{F}\_{S} scores (0.872 vs 0.250) illustrates that these two evaluation approaches capture
different aspects of answer quality. While this paper reports only one detailed example, additional experiments (not included here) show that LLM judges sometimes agree and sometimes
disagree with ℱS\mathcal{F}\_{S}-based rankings. Notably, we observed cases where ℱS\mathcal{F}\_{S} correctly identified inferior answers that the LLM judge rated highly, while also failing to detect hallucinated content.

Such absence of coherence between the two approaches is neither surprising nor problematic: ℱS\mathcal{F}\_{S} measures information-theoretic alignment between the answer’s semantic distribution and the optimal channel
implied by the question-context pair, while LLM judges evaluate surface-level criteria such as coherence, completeness, and relevance. An answer can score well on traditional quality
metrics while exhibiting suboptimal information-theoretic alignment—for instance, by including contextually accurate but tangential topics that dilute focus on the question’s core
requirements.

We therefore recommend using ℱS\mathcal{F}\_{S} and LLM-based evaluation as *complementary* tools rather than expecting agreement. The Semantic Faithfulness metric provides a
principled, quantitative measure of alignment with implicit information requirements that subjective evaluation may miss, particularly for subtle semantic drift or hallucination.
Complete examples including question-answer pairs and precomputed distributions are available in the project repository’s data/cache/ directory.

============================================================================

## 6 Conclusions

This paper advances the Semantic Divergence Metrics (SDM) framework introduced in our previous work [[9](https://arxiv.org/html/2512.05156v1#bib.bib9), [10](https://arxiv.org/html/2512.05156v1#bib.bib10)] by developing principled information
theory-based metrics for LLM faithfulness evaluation. The original SDM framework proposed semantic uncertainty SHS\_{H} and semantic divergence KL[A||Q][A||Q] as heuristic measures of answer
quality, requiring free parameters such as weights balancing the Jensen-Shannon divergence and Wasserstein distance. While these metrics demonstrated practical utility, their
heuristic foundations and parameter sensitivity limit their theoretical guarantees and interpretability.

#### Theoretical Contributions.

We replace the original heuristic metrics of the SDM method with two measures derived from first principles of information theory and stochastic thermodynamics:

1. 1.

   Semantic Faithfulness ℱS\mathcal{F}\_{S}: Grounded in information theory, this metric quantifies how well the answer AA aligns with the question QQ by computing
   their minimal KL divergence subject to marginal constraints. This metric has no free parameters and is uniquely defined via the solution to a convex optimization problem (Algorithm
   1).
2. 2.

   Semantic Entropy Production (SEP): Grounded in stochastic thermodynamics, this metric quantifies entropy production in the LLM’s information processing by computing
   D​(A⋆∥A⋆R)D(A^{\star}\|A\_{\star}^{R})—the KL divergence between the optimal answer transition matrix 𝐀⋆{\bf A}\_{\star} and the optimal context-preserving matrix 𝐀⋆R{\bf A}\_{\star}^{R}. SEP decomposes according
   to Eq.([16](https://arxiv.org/html/2512.05156v1#S4.E16 "In 4.1 Decomposition of the Total Entropy Production ‣ 4 Semantic Entropy Production ‣ Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations")) into the change of entropy of sub-system X (the context-anwer channel) and the dissipated entropy/heat produced by this channel, and quantifies the amount of irreversibility in text generation.

The computational framework requires only: (1) an LLM as black box for answer generation, (2) lightweight sentence transformers for embedding (e.g., Qwen3-Embedding-0.6B),
and (3) standard Python scientific stack (scipy.optimize) for convex optimization. Importantly, both optimization problems are convex with guaranteed convergence to global
optima, as established by the Csiszár-Tusnády alternating minimization framework [[4](https://arxiv.org/html/2512.05156v1#bib.bib4), [5](https://arxiv.org/html/2512.05156v1#bib.bib5)]. Our algorithms reliably converge in 12–69 iterations (median: 18)
with constraint satisfaction to ∼10−7\sim 10^{-7} precision across all experimental triplets.

#### Experimental Validation.

We validated the framework on 10 question-context-answer triplets from NVIDIA’s fiscal 2024 10-K risk disclosure, organized into two groups: comprehensive multi-topic analysis (Group
A) and focused competitive threats analysis (Group B). Both groups achieved similar mean Semantic Faithfulness (ℱS≈0.51\mathcal{F}\_{S}\approx 0.51), while Group A exhibited higher SEP (mean
= 0.359 bits) than Group B (mean = 0.215 bits). This finding underscores the value of computing both metrics, as they capture complementary aspects of the LLM’s information
processing. Validation on larger and more diverse datasets remains an important direction for future work.

#### Complementary Metrics.

Our empirical analysis demonstrates that ℱS\mathcal{F}\_{S} and SEP, while correlated, capture distinct aspects of semantic faithfulness. ℱS\mathcal{F}\_{S} quantifies the preservation of
query-relevant information in the answer, whereas SEP measures the thermodynamic cost of the context-to-answer transformation. This complementarity suggests that both metrics should
be reported together for comprehensive evaluation of LLM outputs.

#### LLM-as-a-Judge Validation.

Qualitative evaluation using Claude Sonnet 4.5 showed that LLM judges and ℱS\mathcal{F}\_{S} capture different aspects of answer quality. While judges evaluate surface-level criteria
(coherence, completeness, relevance), ℱS\mathcal{F}\_{S} measures information-theoretic alignment. Additional experiments beyond those reported here revealed cases where the two
approaches disagreed—including instances where ℱS\mathcal{F}\_{S} correctly identified inferior answers that the LLM judge rated highly due to missed hallucinations. We recommend using
both as complementary evaluation tools.

#### Practical Applications and Broader Impact.

The proposed metrics address several critical challenges in LLM deployment:

1. 1.

   Answer selection and ranking: For summarization of complex domain-specific texts (financial disclosures, legal documents, technical reports), ℱS\mathcal{F}\_{S} and
   SEP provide quantitative guidance for selecting the most faithful response among multiple candidates.
2. 2.

   Hallucination detection: Jointly monitoring both metrics can detect when LLM responses diverge from information-theoretically optimal channels, providing early
   warning signals for potential hallucinations.
3. 3.

   Reference-free evaluation: Traditional text evaluation metrics such as BLEU [[13](https://arxiv.org/html/2512.05156v1#bib.bib13)] and ROUGE [[12](https://arxiv.org/html/2512.05156v1#bib.bib12)] are *reference-based*: they measure n-gram overlap between a candidate text and one or more ground-truth references, requiring human-authored gold-standard answers for comparison. In contrast, the SF metric ℱS\mathcal{F}\_{S} is *reference-free*: it quantifies information-theoretic alignment between an answer and the implicit requirements defined by the question-context pair, without requiring any ground-truth reference.
4. 4.

   Model governance: Organizations deploying LLMs in high-stakes domains require quantitative assurance that outputs align with provided context. The SDM framework
   provides auditable metrics grounded in mathematical principles rather than heuristic similarity scores.
5. 5.

   Prompt engineering: Our finding that comprehensive multi-topic questions with explicit structure achieve higher ℱS\mathcal{F}\_{S} provides actionable insights for
   prompt optimization.

#### Future Directions.

The present work suggests several future research and development directions:
(1) Evaluation of the SDM framework on larger and more diverse datasets across multiple domains;
(2) Integration with uncertainty quantification methods to detect when LLMs lack sufficient information in context to answer questions faithfully;
(3) Development of real-time monitoring dashboards for production LLM systems tracking ℱS\mathcal{F}\_{S} and SEP metrics across user interactions;
(4) Application to retrieval-augmented generation (RAG) systems to quantify faithfulness to retrieved documents;
(5) Extension to multi-turn conversations where context accumulates across dialogue turns;
(6) Fine-tuning embedding models for improved performance on domain-specific downstream tasks;
(7) Theoretical analysis of how model architecture, training objectives, and scale affect semantic faithfulness and entropy production characteristics.

## References

* [1]

  S. Amari, “Information Geometry and Its Applications”, Springer, Applied Mathematical Sciences Series, Vol. 194 (2016).
* [2]
   S. Arimoto, “An Algorithm to Compute the Capacity of Discrete Memoryless Channels”, IEEE Trans. IT, vol. 18, pp.14-20 (1972).
* [3]
   R. Blahut, “Computation of Channel Capacity and Rate-Distortion Functions”, IEEE Trans. IT, vol. 18, pp.460-473 (1972).
* [4]

  I. Csiszár and G. Tusnády, “Information Geometry and Alternating Minimization Procedures,” Statistics & Decisions, Supplement Issue, vol. 1, pp. 205-237, 1984.
* [5]
   I. Csiszár, “Information Theory and Statistics: A Tutorial”, Foundations and Trends® in Communications and Information Theory 1(4)
  ,
  DOI:10.1561/0100000004; https://www.researchgate.net/publication/220220640\_\\_Information\_\\_Theory\_\\_and\_\\_Statistics\_\\_A\_\\_Tutorial (2004).
* [6]

  T.M. Cover and J.A. Thomas, Elements of Information Theory, Wiley & Sons,‘1991.
* [7]

  J. Ehrich and D.A. Sivak, “Energy and Information Flows in Autonomous Systems”, Front. Phys., 05, Volume 11, https://doi.org/10.3389/fphy.2023.1108357 (2023); https://arxiv.org/abs/2209.10644 (2022).
* [8]

  Farquhar, S., Kossen, J., Kuhn, L., and Gal, Y., Detecting Hallucinations in Large Language Models Using Semantic Entropy. Nature, 630, 625-630 (2024)
* [9]

  I. Halperin, “Prompt-Response Semantic Divergence Metrics for Faithfulness Hallucination Detection in Large Language Models”,
  https://arxiv.org/abs/2508.10192;
  https://papers.ssrn.com/sol3/papers.cfm?abstract\_\\_id=5390586
  (2025).
* [10]

  I. Halperin, “Topic Identification in LLM Input-Output Pairs through the Lens of Information Bottleneck”, https://papers.ssrn.com/sol3/papers.cfm?abstract\_\\_id=5403971;
  https://arxiv.org/abs/2509.03533 (2025).
* [11]

  S. Ito, M. Oizumi, S.-I. Amari, “Unified Framework for the Entropy Production and the Stochastic Interaction Based on Information Geometry”, Phys. Rev. Research 2, 033048, https://arxiv.org/abs/1810.09545 (2020).
* [12]

  C.-Y. Lin, “ROUGE: A Package for Automatic Evaluation of Summaries”, Text Summarization Branches Out: Proceedings of the ACL-04 Workshop, pp. 74–81 (2004).
* [13]

  K. Papineni, S. Roukos, T. Ward, and W.-J. Zhu, “BLEU: A Method for Automatic Evaluation of Machine Translation”, Proceedings of the 40th Annual Meeting of the Association for
  Computational Linguistics (ACL), pp. 311–318, DOI: https://doi.org/10.3115/1073083.1073135 (2002).
* [14]

  J.M.R. Parrondo, J.M. Horowitz, T. Sagawa, “Thermodynamics of Information”, Nature Physics, DOI: 10.1038/NPHYS3230 (2015).
* [15]

  U. Seifert, “Stochastic Thermodynamics, Fluctuation Theorems, and Molecular Machines”, Rep. Prog. Phys. 75 126001, DOI 10.1088/0034-4885/75/12/126001, https://arxiv.org/abs/1205.4176 (2012).
* [16]

  U. Seifert, “Entropy Production Along a Stochastic Trajectory and an Integral Fluctuation Theorem”, Phys. Rev. Lett. 95, 040602, DOI: https://doi.org/10.1103/PhysRevLett.95.040602 (2005).
* [17]

  R.E. Spinney, I.J. Ford, “Fluctuation Relations: a Pedagogical Overview”, in Nonequilibrium Statistical Physics of Small Systems: Fluctuation Relations and Beyond Wiley-VCH, Weinheim, 2012; ISBN 978-3-527-41094-1; https://arxiv.org/abs/1201.6381 (2012).
* [18]

  L. Zheng et al., “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena”, in Advances in Neural Information Processing Systems 36 (NeurIPS 2023), arXiv:2306.05685 (2023).

.