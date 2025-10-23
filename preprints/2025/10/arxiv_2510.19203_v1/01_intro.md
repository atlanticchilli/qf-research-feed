---
authors:
- Yuntao Wu
- Lynn Tao
- Ing-Haw Cheng
- Charles Martineau
- Yoshio Nozawa
- John Hull
- Andreas Veneris
doc_id: arxiv:2510.19203v1
family_id: arxiv:2510.19203
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Aligning Multilingual News for Stock Return Prediction
url_abs: http://arxiv.org/abs/2510.19203v1
url_html: https://arxiv.org/html/2510.19203v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yuntao Wu
[winstonyt.wu@mail.utoronto.ca](mailto:winstonyt.wu@mail.utoronto.ca)
[0009-0006-6269-1603](https://orcid.org/0009-0006-6269-1603 "ORCID identifier")
University of TorontoTorontoOntarioCanada
, 
Lynn Tao
[lynnyl.tao@mail.utoronto.ca](mailto:lynnyl.tao@mail.utoronto.ca)
[0009-0000-3856-2146](https://orcid.org/0009-0000-3856-2146 "ORCID identifier")
University of TorontoTorontoOntarioCanada
, 
Ing-Haw Cheng
[inghaw.cheng@rotman.utoronto.ca](mailto:inghaw.cheng@rotman.utoronto.ca)
[0000-0002-4872-7888](https://orcid.org/0000-0002-4872-7888 "ORCID identifier")
University of TorontoTorontoOntarioCanada
, 
Charles Martineau
[charles.martineau@rotman.utoronto.ca](mailto:charles.martineau@rotman.utoronto.ca)
[0000-0002-6896-184X](https://orcid.org/0000-0002-6896-184X "ORCID identifier")
University of TorontoTorontoOntarioCanada
, 
Yoshio Nozawa
[yoshio.nozawa@rotman.utoronto.ca](mailto:yoshio.nozawa@rotman.utoronto.ca)
[0000-0002-6395-2688](https://orcid.org/0000-0002-6395-2688 "ORCID identifier")
University of TorontoTorontoOntarioCanada
, 
John Hull
[john.hull@rotman.utoronto.ca](mailto:john.hull@rotman.utoronto.ca)
[0000-0003-4290-3374](https://orcid.org/0000-0003-4290-3374 "ORCID identifier")
University of TorontoTorontoOntarioCanada
 and 
Andreas Veneris
[veneris@eecg.toronto.edu](mailto:veneris@eecg.toronto.edu)
[0000-0002-6309-8821](https://orcid.org/0000-0002-6309-8821 "ORCID identifier")
University of TorontoTorontoOntarioCanada

(2025)

###### Abstract.

News spreads rapidly across languages and regions, but translations may lose subtle nuances. We propose a method to align sentences in multilingual news articles using optimal transport, identifying semantically similar content across languages. We apply this method to align more than 140,000 pairs of Bloomberg English and Japanese news articles covering around 3500 stocks in Tokyo exchange over 2012-2024. Aligned sentences are sparser, more interpretable, and exhibit higher semantic similarity. Return scores constructed from aligned sentences show stronger correlations with realized stock returns, and long-short trading strategies based on these alignments achieve 10% higher Sharpe ratios than analyzing the full text sample.

international markets, natural language processing, multilingual analysis, optimal transport, return predictions

††copyright: none††copyright: acmlicensed††journalyear: 2025††ccs: Computing methodologies Natural language processing††ccs: Applied computing Economics

## 1. Introduction

Financial markets increasingly reflect a complex interplay of global information flows. News about firms, policy decisions, or macro conditions often appears first in local languages and subsequently in global reporting.
Translating this multilingual content into English or a single canonical language may obscure subtle inflections, domain-specific nuances, or phrasing differences that carry predictive value.
When multilingual sources independently cover similar topics, they may emphasize different angles or priorities, so treating them as direct translations risks losing information.
Finding sementic alignment across different languages could better capture shared meaning, and potentially uncover predictive structure.

Recent advances in natural language processing (NLP) of transformer based large language models (LLMs), especially bidirectional encoder representations from transformers (BERT), suggest a path forward (Vaswani et al., [2017](https://arxiv.org/html/2510.19203v1#bib.bib20); Devlin et al., [2019](https://arxiv.org/html/2510.19203v1#bib.bib6)).
Chen et al. ([2022](https://arxiv.org/html/2510.19203v1#bib.bib5)) demonstrate that embeddings from LLMs can extract nuanced, contextual features from news text that outperform traditional bag-of-words and sentiment models in return prediction tasks.
They show that across 16 global equity markets and 13 languages, LLM-based representations generate superior performance in forecasting returns.
Their findings underscore that rich text representations, beyond surface counts or sentiment scores, can capture incremental predictive information.

Nevertheless, LLM embeddings typically operate at the document level, and do not explicitly connect content across languages.
In multilingual news corpora, matching semantically similar passages remains a challenge: naive cosine similarity-based methods tend to be dense and uninformative, and statistical alignments may fail when the coverage diverges across languages.

In this paper, we propose a sentence-level alignment method based on optimal transport, enabling more interpretable and sparse maps between languages.
Concretely, we embed sentences from English and foreign language articles using a multilingual encoder (LaBSE (Feng et al., [2022](https://arxiv.org/html/2510.19203v1#bib.bib9))), then compute an optimal transport plan to align semantically close sentences.
The resulting sparse alignment highlights which sentence pairs truly share similar meanings.
We then aggregate aligned, unaligned, and full-text embeddings to build return scores and test them in long-short strategies.
The long-short portfolios based on aligned embeddings yield an idealized Sharpe ratios of 4.36, outperforming the embeddings based on full or unaligned texts.

## 2. Related Work

The most closely related study is Durand et al. ([2023](https://arxiv.org/html/2510.19203v1#bib.bib8)), which uses pre-calculated sentiment scores from Thomson Reuters News Analytics for English and Japanese news to examine how language-specific sentiment predicts movements in the Japanese stock market. In contrast, we provide interpretable, sentence-level alignments and link English and Japanese news content to the cross-section of Japanese stock returns.

Statistical machine translation (SMT) explicitly aligns words or phrases to facilitate translation. Early methods perform alignments at various granularities—word, phrase, or sentence (Brown et al., [1988](https://arxiv.org/html/2510.19203v1#bib.bib3); Gale and Church, [1993](https://arxiv.org/html/2510.19203v1#bib.bib11); ibm, [2015](https://arxiv.org/html/2510.19203v1#bib.bib2); Gal and Blunsom, [2013](https://arxiv.org/html/2510.19203v1#bib.bib10))—but typically assume one-to-one correspondences. In contrast, multilingual news about the same company may cover different aspects and lack direct correspondence. Our goal is not translation, but to identify semantically similar or distinct content that is informative for stock return prediction. Ideas from SMT, however, motivate our approach to sentence-level alignment.

Recently, Dou and Neubig ([2021](https://arxiv.org/html/2510.19203v1#bib.bib7)) use optimal transport to align words across languages for improved translation and cross-lingual transfer learning, fine-tuning models on short parallel sentences. We extend this approach to sentence-level alignment in longer documents. Longer articles often contain many stopwords, which can dilute word-level embeddings, whereas sentence-level alignment better captures semantic meaning. A major challenge is the lack of “gold standard” alignments at scale, which we address by leveraging optimal transport for unsupervised, interpretable sentence alignment applicable to financial prediction.

## 3. Data

We collect global news articles from the Bloomberg terminal news feed covering the period 2008–2024.111Bloomberg provided us access to the data under a non-disclosure agreement.
For each unique story identifier, we retain only the final update published within 24 hours of its initial appearance on Bloomberg.
We then align news articles with stock prices and returns based on release times: articles published between 30 minutes before market open on day t−1t-1 and 30 minutes before market open on day tt are associated with day tt’s prices and returns. For example, the Tokyo market opens at 9:00 am, an article released at 8:28 am on day tt is linked to the stock price and return on day tt, while an article released at 8:50 am on day tt is associated with the stock price and return on day t+1t+1.
In our experiments, we include English and foreign-language articles that are explicitly associated with a single stock ticker with a ticker score ≥75\geq 75, indicating medium-to-high relevance to that stock.
For each stock ss and trading day tt, we concatenate all associated English articles into a single composite article ℰt,s\mathcal{E}\_{t,s}, and all associated foreign-language articles into ℱt,s\mathcal{F}\_{t,s}.
We focus primarily on the Japanese market, which has the richest foreign-language coverage in the news feed. In the preprocessed dataset, this corresponds on average to approximately 35,000 English articles and 27,000 Japanese articles annually, spanning about 3,500 stocks traded on the Tokyo Stock Exchange.
By comparison, the Hong Kong, Taiwan, and mainland Chinese exchanges yield fewer than 10,000 English articles and 3,700 Chinese (simplified or traditional) articles annually, covering fewer than 1,000 stocks in each exchange, starting from 2012, while the Chinese coverage ranks the second among non-English news in the dataset.
After concatenation in the Japanese market, we obtain an average of 17,807 stock-days222A stock-day is defined as a trading day for a given stock. per year with both English and Japanese news available.
Stock return data are obtained from Compustat Global using WRDS for the period 2008–2024.

## 4. Methodology

Our objective is to align English and foreign-language articles at the sentence level for each stock-day. We seek to identify pairs of sentences that capture similar semantic content, while minimizing misalignments, thereby enhancing interpretability of the results.

### Text Preprocessing

Starting from the raw dataset, we retain only articles whose body text is updated within 24 hours of their initial publication on Bloomberg. For each article, we remove Bloomberg-specific headers and footers, keeping only the main body. Within each paragraph, line breaks are removed to ensure continuous text. We do not remove numbers or stopwords, since they may help preserve sentence structure when processed by machine learning models. Articles shorter than 100 characters or longer than 100,000 characters in any language are excluded.

### Sentencizing and Embedding

We use spaCy (Honnibal et al., [2020](https://arxiv.org/html/2510.19203v1#bib.bib12)) monolingual models to split each article into sentences, yielding
  
ℰt,s={Et,s,1,…,Et,s,n}\mathcal{E}\_{t,s}=\left\{E\_{t,s,1},...,E\_{t,s,n}\right\} for English articles and ℱt,s={Ft,s,1,…,Ft,s,m}\mathcal{F}\_{t,s}=\left\{F\_{t,s,1},...,F\_{t,s,m}\right\} for foreign-language articles.
Each sentence is then embedded using the pre-trained LaBSE model (Feng et al., [2022](https://arxiv.org/html/2510.19203v1#bib.bib9)), a language-agnostic encoder that assigns similar embeddings to semantically equivalent text across languages. The resulting embeddings are normalized and stacked into matrices Xt,sE∈ℝn×768X\_{t,s}^{E}\in\mathbb{R}^{n\times 768} and Xt,sF∈ℝm×768X\_{t,s}^{F}\in\mathbb{R}^{m\times 768} for English and foreign language articles, respectively.

### Optimal Transport for Alignments

Optimal transport (OT) (Monge, [1781](https://arxiv.org/html/2510.19203v1#bib.bib14); Kantorovich, [1942](https://arxiv.org/html/2510.19203v1#bib.bib13); Santambrogio, [2015](https://arxiv.org/html/2510.19203v1#bib.bib17)) provides a principled way to map probability mass from one distribution to another while minimizing transport cost. The original Monge formulation (Monge, [1781](https://arxiv.org/html/2510.19203v1#bib.bib14)) is often intractable and may not even admit a solution unless restrictive conditions are met (Caffarelli et al., [2002](https://arxiv.org/html/2510.19203v1#bib.bib4)). Instead, we adopt the Kantorovich formulation (Kantorovich, [1942](https://arxiv.org/html/2510.19203v1#bib.bib13)), and in particular its discrete version as described in (Peyré and Cuturi, [2020](https://arxiv.org/html/2510.19203v1#bib.bib16); Dou and Neubig, [2021](https://arxiv.org/html/2510.19203v1#bib.bib7)). Let {xi}i=1n\left\{x\_{i}\right\}\_{i=1}^{n} and {yj}j=1m\left\{y\_{j}\right\}\_{j=1}^{m} denote two point sets with associated probability distributions pxp\_{x} and pyp\_{y}, where ∑i=1npxi=1\sum\_{i=1}^{n}p\_{x\_{i}}=1 and ∑j=1mpyj=1\sum\_{j=1}^{m}p\_{y\_{j}}=1. The cost of moving mass from xix\_{i} to yjy\_{j} is given by ci​j=c​(xi,yj)c\_{ij}=c(x\_{i},y\_{j}). The optimal transport problem seeks a transport plan γi​j≥0\gamma\_{ij}\geq 0 that minimizes the total cost of moving probability mass:

|  |  |  |
| --- | --- | --- |
|  | minγ⁡{∑i​jci​j​γi​j:γi​j≥0,∑iγi​j=pyj,∑jγi​j=pxi}\min\_{\gamma}\left\{\sum\_{ij}c\_{ij}\gamma\_{ij}:\gamma\_{ij}\geq 0,\sum\_{i}\gamma\_{ij}=p\_{y\_{j}},\sum\_{j}\gamma\_{ij}=p\_{x\_{i}}\right\} |  |

The resulting transport plan is self-normalized and sparse (Dou and Neubig, [2021](https://arxiv.org/html/2510.19203v1#bib.bib7); Swanson et al., [2020](https://arxiv.org/html/2510.19203v1#bib.bib19)), making it more effective than pure cosine similarities. In practice, the optimal γ\gamma is approximated via entropic regularization using the Sinkhorn algorithm (Sinkhorn, [1964](https://arxiv.org/html/2510.19203v1#bib.bib18)). Computational efficiency can be further improved by exploiting sparse and low-rank matrix structures (Wang and Qiu, [2025](https://arxiv.org/html/2510.19203v1#bib.bib21)), yielding up to a tenfold speedup in our setting and making large-scale analysis feasible.
A large value of γi​j\gamma\_{ij} indicates that xix\_{i} and yjy\_{j} are likely to have similar semantics.

In this paper, we follow Dou and Neubig ([2021](https://arxiv.org/html/2510.19203v1#bib.bib7)) but extend the method from word-level to sentence-level alignments. Specifically, the English and foreign-language articles, Xt,sEX\_{t,s}^{E} and Xt,sFX\_{t,s}^{F}, are treated as two high-dimensional point sets consisting of nn and mm each. Sentences are assigned equal probability mass, i.e., uniformly distributed. The cost matrix is defined using pairwise cosine distance,

|  |  |  |
| --- | --- | --- |
|  | ci​j=1−Xt,s,iE⋅Xt,s,jFc\_{ij}=1-X\_{t,s,i}^{E}\cdot X\_{t,s,j}^{F} |  |

and scaled to [0,1][0,1] with min-max normalization.

We compute transport plans in both directions: source-to-target (foreign to English) and target-to-source (English to foreign), denoted γ\gamma and γ′\gamma^{\prime}.
For each row ii in γ\gamma, we identify the maximum element γi​jm​a​x\gamma\_{ij\_{max}}. If γi​jm​a​x\gamma\_{ij\_{max}} falls within the top 5% of column jm​a​xj\_{max}, we mark a forward alignment, producing the binary forward alignment matrix A∈{0,1}n×mA\in\left\{0,1\right\}^{n\times m}. The backward alignment matrix B∈{0,1}m×nB\in\left\{0,1\right\}^{m\times n} is computed analogously.333Due to sparsity, one could instead apply a global threshold to directly enforce one-to-one mappings.
Because news coverage varies across languages, it is possible that for a given stock-day, content reported in one language is not covered in the other. In such cases, OT may still produce spurious alignments. To filter these out, we use the raw pairwise cosine similarity matrix ξi​j=Xt,s,iE⋅Xt,s,jF\xi\_{ij}=X\_{t,s,i}^{E}\cdot X\_{t,s,j}^{F}, and retain only alignments where ξi​j≥ξt​h​r​e​s\xi\_{ij}\geq\xi\_{thres}, where ξt​h​r​e​s\xi\_{thres} is a hyperparameter that is dependent on the distribution of cosine similarities of the embedding model. We choose ξt​h​r​e​s=0.6\xi\_{thres}=0.6 for LaBSE.
The final alignment matrix is obtained as the intersection of three matrices:

|  |  |  |
| --- | --- | --- |
|  | 𝒜=A∗BT∗(ξi​j≥ξt​h​r​e​s),\mathcal{A}=A\*B^{T}\*(\xi\_{ij}\geq\xi\_{thres}), |  |

where ∗\* denotes elementwise multiplication.

### Aggregating Embeddings

Once the alignment matrix 𝒜\mathcal{A} is obtained, we aggregate sentence embeddings based on alignment status.
Specifically, we average the embeddings of aligned sentences (𝒜i​j=1\mathcal{A}\_{ij}=1) in each language to obtain the aligned embeddings Xt,sE,AX\_{t,s}^{E,A} and Xt,sF,AX\_{t,s}^{F,A}, and similarly average unaligned senteces (𝒜i​j=0\mathcal{A}\_{ij}=0) to obtain Xt,sE,U​AX\_{t,s}^{E,UA} and Xt,sF,U​AX\_{t,s}^{F,UA}. We also compute the average embeddings over all sentences to produce global embeddings Xt,sE,F​u​l​lX\_{t,s}^{E,Full} and Xt,sF,F​u​l​lX\_{t,s}^{F,Full}. Each aggregated embedding is a 768-dimensional vector.
For notation, we denote these aggregated embeddings by Xt,sl,kX\_{t,s}^{l,k}, where l∈{E,F}l\in\left\{E,F\right\} indicates the language and k∈{A,U​A,F​u​l​l}k\in\left\{A,UA,Full\right\} indicates the aggregate type. The superscript Full may be omitted.

### Return Score Constructions

Let Rett,sO​C\text{Ret}\_{t,s}^{OC} denote the open-close return for stock ss on day tt. We use Ridge regression with weights ww to associate return scores to the embeddings, following (Chen et al., [2022](https://arxiv.org/html/2510.19203v1#bib.bib5)):

|  |  |  |
| --- | --- | --- |
|  | arg⁡minw⁡‖Xt,sl,k​w−Rett,sO​C‖22+λ​‖w‖22,\arg\min\_{w}\left\|X\_{t,s}^{l,k}w-\text{Ret}\_{t,s}^{OC}\right\|\_{2}^{2}+\lambda\left\|w\right\|\_{2}^{2}, |  |

with regularization parameter λ\lambda selected by cross validation over the search space [10,20,30,…,100][10,20,30,...,100], with optimal values typically chosen as 90 or 100.
We adopt a rolling window framework: for each year yy, the model is trained on data from year y−5y-5 through yy and then used to generate return scores Ret^t,sO​C,l,k=Xt,sl,k​w\hat{\text{Ret}}\_{t,s}^{OC,l,k}=X\_{t,s}^{l,k}w (denoted Softt,sl,k\text{Soft}\_{t,s}^{l,k}) for day tt in year y+1y+1. This procedure, repeated for years 2012–2024, ensures that return scores are always computed using past data, avoiding look-ahead bias. The analysis period for evaluation is 2018–2024.

## 5. Results

### Alignment Sparsity

Figure [1](https://arxiv.org/html/2510.19203v1#S5.F1 "Figure 1 ‣ Alignment Sparsity ‣ 5. Results ‣ Aligning Multilingual News for Stock Return Prediction") illustrates the sparsity of different alignment methods applied to news articles discussing the Bank of Japan (8301.T) on 2023-01-04. We compare pure cosine similarities, normalized via Softmax or Entmax (Peters et al., [2019](https://arxiv.org/html/2510.19203v1#bib.bib15)), and optimal transport. Both Softmax and Entmax produce dense transport plan matrices, whereas optimal transport yields a sparse matrix with non-zero values concentrated in relatively few locations. This sparsity facilitates the selection of a global threshold for filtering aligned sentence pairs. Some examples of aligned sentences are provided in the Appendix. In the dataset, updates to a single news article may be reported as several stories with slight rephrasing, resulting in multiple possible alignments.

Figure [2](https://arxiv.org/html/2510.19203v1#S5.F2 "Figure 2 ‣ Alignment Sparsity ‣ 5. Results ‣ Aligning Multilingual News for Stock Return Prediction")(a) reports the average proportion of aligned and unaligned sentences within each article, where “JP” refers to Japanese news and “EN” to English news. Overall, approximately 30–50% of sentences are aligned in more recent years. Note that spaCy’s sentencizing may occasionally be inaccurate, particularly for articles containing bullet points, which can affect the total sentence count.
Figure [2](https://arxiv.org/html/2510.19203v1#S5.F2 "Figure 2 ‣ Alignment Sparsity ‣ 5. Results ‣ Aligning Multilingual News for Stock Return Prediction")(b) shows the number of stock-days with aligned and unaligned sentences. Most stock-days contain at least one aligned and one unaligned sentence pair.

![Refer to caption](tables/JP/plots_0.95/sample_SOFTMAX.jpg)


(a) Softmax (Cosine Similarity)

![Refer to caption](tables/JP/plots_0.95/sample_ENTMAX.jpg)


(b) Entmax (Cosine Similarity)

![Refer to caption](tables/JP/plots_0.95/sample_OT_SPLR.jpg)


(c) Optimal Transport

Figure 1. Sparsity of Different Alignment Methods††:



![Refer to caption](tables/JP/plots_0.95/alignment_sentence_count_jp.jpg)


(a) Proportion of Sentences Aligned

![Refer to caption](tables/JP/plots_0.95/alignment_story_count_LaBSE.jpg)


(b) Number of Stock-days with Aligned and Unaligned Sentences

Figure 2. Alignments Found for Japanese News Articles††:

### Similarity of Semantics and Return Scores

Table [1](https://arxiv.org/html/2510.19203v1#S5.T1 "Table 1 ‣ Similarity of Semantics and Return Scores ‣ 5. Results ‣ Aligning Multilingual News for Stock Return Prediction") summarizes the distribution of cosine similarities for embeddings of aligned (Xt,sE,AX\_{t,s}^{E,A} and Xt,sF,AX\_{t,s}^{F,A}), unaligned (Xt,sE,U​AX\_{t,s}^{E,UA} and Xt,sF,U​AX\_{t,s}^{F,UA}) and full articles (Xt,sEX\_{t,s}^{E} and Xt,sFX\_{t,s}^{F}) across the entire data sample from 2012 to 2024.
As one would expect:
(1) Aligned embeddings exhibit the highest average cosine similarity 0.80.8, with low variance, reflecting strong semantic similarity.
(2) Unaligned embeddings generally show lower cosine similarities, averaging around 0.53 with higher standard deviation. Potentially, the current alignment parameters may be too strict, producing false negatives.
(3) Full-article embeddings fall in between, with an average similarity of 0.750.75.
Varying the cosine similarity cutoff thresholds has minimal impact, indicating that the optimal transport-based alignment robustly identifies semantically similar content.

Table [2](https://arxiv.org/html/2510.19203v1#S5.T2 "Table 2 ‣ Similarity of Semantics and Return Scores ‣ 5. Results ‣ Aligning Multilingual News for Stock Return Prediction") reports correlations between return scores computed from different aggregated embeddings. Given that we work with daily returns across more than 70,000 observations from 2018 to 2024, it is challenging to achieve high correlations with realized returns.
Nevertheless, consistent patterns emerge: return scores derived from aligned embeddings (Softl,A\text{Soft}^{l,A}) tend to exhibit higher correlations, while scores from unaligned embeddings (Softl,U​A\text{Soft}^{l,UA}) show lower correlations.

Table 1. Sentence Level Cosine Similarity

| Alignment | mean | std | 5% | 50% | 95% |
| --- | --- | --- | --- | --- | --- |
| Aligned | 0.79 | 0.06 | 0.66 | 0.81 | 0.87 |
| Unaligned | 0.53 | 0.20 | 0.18 | 0.54 | 0.81 |
| Full | 0.75 | 0.09 | 0.59 | 0.76 | 0.86 |




Table 2. Return Score Correlations

|  | Ret | SoftEN,A | SoftEN,UA | SoftEN | SoftJP,A | SoftJP,UA | SoftJP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ret | 1.00 | 0.02 | 0.03 | 0.03 | 0.02 | 0.01 | 0.03 |
| SoftEN,A | 0.02 | 1.00 | 0.41 | 0.67 | 0.67 | 0.38 | 0.57 |
| SoftEN,UA | 0.03 | 0.41 | 1.00 | 0.76 | 0.49 | 0.47 | 0.50 |
| SoftEN | 0.03 | 0.67 | 0.76 | 1.00 | 0.62 | 0.41 | 0.62 |
| SoftJP,A | 0.02 | 0.67 | 0.49 | 0.62 | 1.00 | 0.44 | 0.72 |
| SoftJP,UA | 0.01 | 0.38 | 0.47 | 0.41 | 0.44 | 1.00 | 0.71 |
| SoftJP | 0.03 | 0.57 | 0.50 | 0.62 | 0.72 | 0.71 | 1.00 |

### Impact on Trading Strategy

To assess whether commonly discussed information influences investor behavior and market performance, we implement a long-short trading strategy based on the constructed return scores. On each trading day with at least 20 traded stocks, we rank the stocks by their predicted return scores Softt,sl,k\text{Soft}\_{t,s}^{l,k}, and divide them into quantiles. Long the stocks in the top-quantile and short the stocks in the bottom-quantile. Let RettO​C,L,l,k\text{Ret}\_{t}^{OC,L,l,k} and RettO​C,S,l,k\text{Ret}\_{t}^{OC,S,l,k} denote the average long and short returns on day tt, for each language ll and alignment type kk. The long-short return is defined as

|  |  |  |
| --- | --- | --- |
|  | LStl,k=RettO​C,L,l,k−RettO​C,S,l,k.\text{LS}\_{t}^{l,k}=\text{Ret}\_{t}^{OC,L,l,k}-\text{Ret}\_{t}^{OC,S,l,k}. |  |

We compute the distributional statistics of LStl,k\text{LS}\_{t}^{l,k}, as well as Sharpe ratios for the resulting portfolios.
Table [3](https://arxiv.org/html/2510.19203v1#S5.T3 "Table 3 ‣ Impact on Trading Strategy ‣ 5. Results ‣ Aligning Multilingual News for Stock Return Prediction") summarizes the results.
The geometric mean of the daily long-short returns is calculated as

|  |  |  |
| --- | --- | --- |
|  | (∏t=1T(1+LStl,k))1/T−1,\left(\prod\_{t=1}^{T}(1+\text{LS}\_{t}^{l,k})\right)^{1/T}-1, |  |

where TT is the total number of trading days from 2018 to 2024. The daily Sharpe ratio is computed as mean​(LStl,k)std​(LStl,k)\frac{\text{mean}(\text{LS}\_{t}^{l,k})}{\text{std}(\text{LS}\_{t}^{l,k})}, and the annualized Sharpe ratio is daily Sharpe ratio multiplied by 252\sqrt{252}.
In the Japanese market, the full embedding of Japanese news generates higher Sharpe than English news. This means that Japanese news typically have higher association with the returns in Tokyo exchange.
In the Japanese market, portfolios based on the full embeddings of Japanese news achieve higher Sharpe ratios than those based on English news, indicating that Japanese news generally has stronger predictive power for returns on the Tokyo Stock Exchange. Portfolios constructed from aligned embeddings exhibit even higher Sharpe ratios for both Japanese and English texts, suggesting that sentences capturing common themes across languages provide clearer signals of stock performance. In contrast, unaligned embeddings tend to be noisier and less informative.

Table 3. Strategy Summary

| Alignment | Lang | Geo Mean | Mean | Std | 5% | 50% | 95% | Sharpe | Ann. Sharpe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Aligned | JP | 0.35% | 0.36% | 1.32% | -1.76% | 0.39% | 2.31% | 0.27 | 4.36 |
|  | EN | 0.28% | 0.29% | 1.34% | -1.86% | 0.23% | 2.46% | 0.22 | 3.42 |
| Unaligned | JP | 0.17% | 0.18% | 1.34% | -1.98% | 0.16% | 2.29% | 0.13 | 2.12 |
|  | EN | 0.23% | 0.24% | 1.29% | -1.66% | 0.16% | 2.45% | 0.18 | 2.91 |
| Full | JP | 0.30% | 0.31% | 1.23% | -1.59% | 0.27% | 2.38% | 0.25 | 3.98 |
|  | EN | 0.24% | 0.25% | 1.16% | -1.65% | 0.17% | 2.20% | 0.21 | 3.40 |

## 6. Conclusion

In this paper, we use optimal transport to align semantically similar sentences in multilingual news articles. Compared to pure cosine similarities, optimal transport produces sparser and more interpretable alignments. Sentences identified as aligned exhibit high semantic similarity, and return scores derived from these aligned sentences show stronger correlations with realized returns. In a long-short trading strategy, portfolios based on aligned sentences achieve higher Sharpe ratios, indicating that commonly discussed themes across languages provide more informative signals for predicting stock returns.
Future directions for this research include: (1) extending the approach to additional markets and languages, and (2) improving thresholding techniques to reduce false negatives in the alignment process.

###### Acknowledgements.

This research was carried out at Rotman School of Management, FinHub Financial Innovation Lab, University of Toronto. We gratefully acknowledges financial support and insightful discussions from Royal Bank of Canada (RBC) Capital Markets. New York, NY and Toronto, ON, Canada.

## References

* (1)
* ibm (2015)

  2015.
  IBM Models.
  <https://smt.wiki/IBM_Models>.


  SMT Research Survey Wiki, accessed 26 Oct 2015.
* Brown et al. (1988)

  Peter F. Brown, John
  Cocke, Stephen A. Della Pietra,
  Vincent J. Della Pietra, Frederick
  Jelinek, Robert L. Mercer, and Paul S.
  Roossin. 1988.
  A Statistical Approach to Language Translation. In
  *Proceedings of the 12th International Conference on
  Computational Linguistics (COLING 1988), Volume 1*.
  Budapest, Hungary, 71–76.
* Caffarelli et al. (2002)

  Luis A. Caffarelli,
  Mikhail Feldman, and Robert J. McCann.
  2002.
  Constructing Optimal Maps for Monge’s Transport
  Problem as a Limit of Strictly Convex Costs.
  *Journal of the American Mathematical
  Society* 15, 1 (2002),
  1–26.

  <http://www.jstor.org/stable/827090>
* Chen et al. (2022)

  Yifei Chen, Bryan Kelly,
  and Dacheng Xiu. 2022.
  Expected Returns and Large Language Models.



  <https://ssrn.com/abstract=4416687>
* Devlin et al. (2019)

  Jacob Devlin, Ming-Wei
  Chang, Kenton Lee, and Kristina
  Toutanova. 2019.
  BERT: Pre-training of Deep Bidirectional
  Transformers for Language Understanding. In
  *Proceedings of the 2019 Conference of the North
  American Chapter of the Association for Computational Linguistics: Human
  Language Technologies, Volume 1 (Long and Short Papers)*,
  Jill Burstein, Christy
  Doran, and Thamar Solorio (Eds.).
  Association for Computational Linguistics,
  Minneapolis, Minnesota, 4171–4186.

  <https://doi.org/10.18653/v1/N19-1423>
* Dou and Neubig (2021)

  Zi-Yi Dou and Graham
  Neubig. 2021.
  Word Alignment by Fine-tuning Embeddings on
  Parallel Corpora. In *Proceedings of the 16th
  Conference of the European Chapter of the Association for Computational
  Linguistics: Main Volume*, Paola Merlo,
  Jorg Tiedemann, and Reut Tsarfaty
  (Eds.). Association for Computational Linguistics,
  Online, 2112–2128.

  <https://doi.org/10.18653/v1/2021.eacl-main.181>
* Durand et al. (2023)

  Robert B. Durand, Joyce
  Khuu, and Lee A. Smales.
  2023.
  Lost in translation. When sentiment metrics for one
  market are derived from two different languages.
  *Journal of Behavioral and Experimental
  Finance* 39 (2023),
  100825.

  <https://doi.org/10.1016/j.jbef.2023.100825>
* Feng et al. (2022)

  Fangxiaoyu Feng, Yinfei
  Yang, Daniel Cer, Naveen Arivazhagan,
  and Wei Wang. 2022.
  Language-agnostic BERT Sentence Embedding. In
  *Proceedings of the 60th Annual Meeting of the
  Association for Computational Linguistics (Volume 1: Long Papers)*,
  Smaranda Muresan,
  Preslav Nakov, and Aline Villavicencio
  (Eds.). Association for Computational Linguistics,
  Dublin, Ireland, 878–891.

  <https://doi.org/10.18653/v1/2022.acl-long.62>
* Gal and Blunsom (2013)

  Yarin Gal and Phil
  Blunsom. 2013.
  *A Systematic Bayesian Treatment of the IBM
  Alignment Models*.
  Technical Report.
  University of Cambridge.

  <https://arxiv.org/pdf/1306.4082.pdf>
  Archived from the original (PDF) on 4 Mar 2016.
* Gale and Church (1993)

  William A. Gale and
  Kenneth W. Church. 1993.
  A Program for Aligning Sentences in Bilingual
  Corpora.
  *Computational Linguistics*
  19, 1 (1993),
  75–102.

  <https://aclanthology.org/J93-1004/>
* Honnibal et al. (2020)

  Matthew Honnibal, Ines
  Montani, Sofie Van Landeghem, and
  Adriane Boyd. 2020.
  spaCy: Industrial-strength Natural Language
  Processing in Python.
  *Zenodo* (2020).

  <https://doi.org/10.5281/zenodo.1212303>
* Kantorovich (1942)

  Leonid V. Kantorovich.
  1942.
  On the Translocation of Mass.
  *Doklady Akademii Nauk SSSR*
  37, 7–8 (1942),
  199–201.


  In Russian: “O peremeschenii mass”.
* Monge (1781)

  Gaspard Monge.
  1781.
  Mémoire sur la théorie des déblais et des
  remblais.
  *Histoire de l’Académie Royale des Sciences
  de Paris* (1781).
* Peters et al. (2019)

  Ben Peters, Vlad Niculae,
  and André FT Martins.
  2019.
  Sparse Sequence-to-Sequence Models. In
  *Proceedings of the 57th Annual Meeting of the
  Association for Computational Linguistics*,
  Anna Korhonen, David
  Traum, and Lluís Màrquez (Eds.).
  Association for Computational Linguistics,
  Florence, Italy, 1504–1519.

  <https://doi.org/10.18653/v1/P19-1146>
* Peyré and Cuturi (2020)

  Gabriel Peyré and Marco
  Cuturi. 2020.
  Computational Optimal Transport.


  arXiv:1803.00567 [stat.ML]
  <https://arxiv.org/abs/1803.00567>
* Santambrogio (2015)

  Filippo Santambrogio.
  2015.
  *Optimal Transport for Applied
  Mathematicians: Calculus of Variations, PDEs, and Modeling*.
  Progress in Nonlinear Differential Equations and Their
  Applications, Vol. 87.
  Birkhäuser Cham.

  [https://doi.org/10.1007/978‐3‐319‐20828‐2](https://doi.org/10.1007/978%E2%80%903%E2%80%90319%E2%80%9020828%E2%80%902)
* Sinkhorn (1964)

  Richard Sinkhorn.
  1964.
  A Relationship Between Arbitrary Positive Matrices
  and Doubly Stochastic Matrices.
  *The Annals of Mathematical Statistics*
  35, 2 (1964),
  876–879.

  <http://www.jstor.org/stable/2238545>
* Swanson et al. (2020)

  Kyle Swanson, Lili Yu,
  and Tao Lei. 2020.
  Rationalizing Text Matching: Learning Sparse
  Alignments via Optimal Transport. In *Proceedings
  of the 58th Annual Meeting of the Association for Computational
  Linguistics*, Dan Jurafsky,
  Joyce Chai, Natalie Schluter, and
  Joel Tetreault (Eds.). Association for
  Computational Linguistics, Online,
  5609–5626.

  <https://doi.org/10.18653/v1/2020.acl-main.496>
* Vaswani et al. (2017)

  Ashish Vaswani, Noam
  Shazeer, Niki Parmar, Jakob Uszkoreit,
  Llion Jones, Aidan N Gomez,
  Ł ukasz Kaiser, and Illia Polosukhin.
  2017.
  Attention is All you Need. In
  *Advances in Neural Information Processing
  Systems*, I. Guyon,
  U. Von Luxburg, S. Bengio,
  H. Wallach, R. Fergus,
  S. Vishwanathan, and R. Garnett
  (Eds.), Vol. 30. Curran Associates,
  Inc.

  <https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf>
* Wang and Qiu (2025)

  Chenrui Wang and Yixuan
  Qiu. 2025.
  The Sparse-Plus-Low-Rank Quasi-Newton Method for
  Entropic-Regularized Optimal Transport. In
  *Forty-second International Conference on Machine
  Learning*.

  <https://openreview.net/forum?id=WCkMkMcqpb>

## Appendix A Sample Aligned Sentences

In this appendix, we compare the sentence alignments produced by Softmax, Entmax, and Optimal Transport for a Japanese news article about the Bank of Japan (8301.T) published on 2023-01-04. For Softmax and Entmax, we select alignments corresponding to the top 5% probabilities across the entire matrix. The results are summarized in Table [4](https://arxiv.org/html/2510.19203v1#A1.T4 "Table 4 ‣ Appendix A Sample Aligned Sentences ‣ Aligning Multilingual News for Stock Return Prediction"), where correct alignments are manually identified and highlighted in bold. We also observe that semantic similarity plays the key role: aligned pairs may differ in numerical values, or in some cases, involve sentences that are not direct translations but still convey related meanings.

Table 4. Sample Aligned Sentences

![[Uncaptioned image]](tables/JP/plots_0.95/example_alignment.png)