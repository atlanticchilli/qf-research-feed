---
authors:
- Sahab Zandi
- Kamesh Korangi
- Juan C. Moreno-Paredes
- María Óskarsdóttir
- Christophe Mues
- Cristián Bravo
doc_id: arxiv:2510.09407v1
family_id: arxiv:2510.09407
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'A multimodal approach to SME credit scoring integrating transaction and ownership
  networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which
  will be submitted for publication. Changes resulting from the publishing process,
  such as editing, corrections, structural formatting, and other quality control mechanisms
  may not be reflected in this document. This work is made available under a Creative
  Commons BY-NC-ND license. ΓΔΞΛ'
url_abs: http://arxiv.org/abs/2510.09407v1
url_html: https://arxiv.org/html/2510.09407v1
venue: arXiv q-fin
version: 1
year: 2025
---


Sahab Zandi
Department of Statistical and Actuarial Sciences, Western University, 1151 Richmond Street, London, Ontario, N6A 5B7, Canada.

Kamesh Korangi
University of Southampton Business School, University of Southampton, SO17 1BJ, United Kingdom.
Centre for Operational Research, Management Sciences and Information Systems, University of Southampton, SO17 1BJ, United Kingdom.

Juan C. Moreno-Paredes 222At the time this research was conducted, Dr Moreno-Paredes was with Santander UK plc.
Independent Researcher, 18 Hulse Road, Southampton, SO15 2QU, United Kingdom.

María Óskarsdóttir
School of Mathematical Sciences, University of Southampton, SO17 1BJ, United Kingdom.
Department of Computer Science, Reykjavík University, Menntavegur 1, 102 Reykjavík, Iceland.

Christophe Mues
University of Southampton Business School, University of Southampton, SO17 1BJ, United Kingdom.
Centre for Operational Research, Management Sciences and Information Systems, University of Southampton, SO17 1BJ, United Kingdom.

Cristián Bravo
Department of Statistical and Actuarial Sciences, Western University, 1151 Richmond Street, London, Ontario, N6A 5B7, Canada.

###### Abstract

Small and Medium-sized Enterprises (SMEs) are known to play a vital role in economic growth, employment, and innovation. However, they tend to face significant challenges in accessing credit due to limited financial histories, collateral constraints, and exposure to macroeconomic shocks. These challenges make an accurate credit risk assessment by lenders crucial, particularly since SMEs frequently operate within interconnected firm networks through which default risk can propagate. This paper presents and tests a novel approach for modelling the risk of SME credit, using a unique large data set of SME loans provided by a prominent financial institution. Specifically, our approach employs Graph Neural Networks to predict SME default using multilayer network data derived from common ownership and financial transactions between firms. We show that combining this information with traditional structured data not only improves application scoring performance, but also explicitly models contagion risk between companies. Further analysis shows how the directionality and intensity of these connections influence financial risk contagion, offering a deeper understanding of the underlying processes. Our findings highlight the predictive power of network data, as well as the role of supply chain networks in exposing SMEs to correlated default risk.

Keywords— OR
in Banking, SME Credit Risk, Supply Chains, Multimodal Learning, Graph Neural Networks

## 1 Introduction

Small and Medium-sized Enterprises (SMEs) are crucial contributors to global economic growth, innovation, and employment, yet they often face significant barriers in securing the credit necessary to accelerate growth. A primary challenge stems from their status as private entities, resulting in financial disclosures that tend to be more opaque compared to those of larger corporations. This complicates the credit risk assessment process for financial institutions and, therefore, affects both the availability and cost of essential funding for SMEs (Bakhtiari et al., [2020](https://arxiv.org/html/2510.09407v1#bib.bib5)). Traditionally, the assessment of corporate credit risk relied on financial ratios and historical performance data, with models such as Altman’s Z score (Altman, [1968](https://arxiv.org/html/2510.09407v1#bib.bib3)) widely used to predict the risk of bankruptcy. However, these models exhibit significant limitations when applied to SMEs, as the latter may lack standardised, audited, or publicly available financial information. This underscores the need for more robust approaches that can better capture the unique risk factors associated with SME lending.

SMEs are embedded in complex supply chain networks, where interconnectivity shapes the dynamics of credit risk (Jackson & Pernoud, [2021](https://arxiv.org/html/2510.09407v1#bib.bib30)). These networks introduce systemic interactions that affect default risk and financial stability (Allen & Gale, [2000](https://arxiv.org/html/2510.09407v1#bib.bib2)), which traditional credit risk models often do not capture (Thomas et al., [2017](https://arxiv.org/html/2510.09407v1#bib.bib58); Long et al., [2022](https://arxiv.org/html/2510.09407v1#bib.bib38)). A key factor in this context is correlated default, whereby the probability of one firm defaulting is related to that of another, due to shared economic conditions or sector-specific shocks (Nagpal & Bahar, [2001](https://arxiv.org/html/2510.09407v1#bib.bib45)). Ignoring such dependencies can lead to a misjudgment of systemic risk (Fenech et al., [2015](https://arxiv.org/html/2510.09407v1#bib.bib23)), which shows the necessity to incorporate network-based insights into credit risk models (Óskarsdóttir et al., [2019](https://arxiv.org/html/2510.09407v1#bib.bib47); Bravo & Óskarsdóttir, [2020](https://arxiv.org/html/2510.09407v1#bib.bib15)).

In this context, network science has emerged as a powerful tool for analysing such systems, due to its ability to reveal underlying structures and dependencies that traditional methods might overlook (Barabási & Pósfai, [2016](https://arxiv.org/html/2510.09407v1#bib.bib7)). Specifically, SMEs, and the different types of financial and operational interactions between them, can be conveniently represented as multilayer networks (Kivelä et al., [2014](https://arxiv.org/html/2510.09407v1#bib.bib31)). The latter are capable of drawing connections from multiple sources without forcing them into a single-layer structure, thus providing a richer and more nuanced view of these interactions. Hence, multilayer networks have proven to be effective in improving our understanding of risk propagation and contagion effects (Óskarsdóttir & Bravo, [2021](https://arxiv.org/html/2510.09407v1#bib.bib46)). The diversity of inter-firm relationships raises important questions about which types of connections are most predictive of risk. Moreover, the different layers in a multilayer network may contain either directed or undirected edges, depending on the nature of the underlying relationships. Whilst common ownership relationships are non-directional, there is extensive literature showing that adverse credit risk events or shocks can have ripple effects that extend both upstream and downstream through the supply chain (Spatareanu et al., [2023](https://arxiv.org/html/2510.09407v1#bib.bib54)), but that the magnitude of those effects may vary in either direction, depending on a variety of other factors (Agca et al., [2022](https://arxiv.org/html/2510.09407v1#bib.bib1)). Such effects may, among other things, be triggered by supplier-side losses on trade credit obligations or the customer’s supply of goods being affected, respectively. Thus, directionality and intensity can play a critical role in contagion dynamics, and ignoring these edge-level properties may obscure asymmetric dependencies. Hence, the ability to fully capture these different types of connection adds to the appeal of multilayer networks in this setting.

For network science to offer valuable insights into these interconnected risks, it needs to be supplemented with advanced modelling techniques that are capable of capturing not just the complexities of SME interactions but also the effects of more conventional, often numeric firm-level risk drivers. The ability to integrate unstructured (or semi-structured) data with structured data represents a major advancement in machine learning (Zhang et al., [2020b](https://arxiv.org/html/2510.09407v1#bib.bib67)). Empirical studies in other fields have shown that combining network data, which is considered semi-structured data, with structured data can indeed help improve the predictive model performance (Rao et al., [2023](https://arxiv.org/html/2510.09407v1#bib.bib50)). The concept of multimodal fusion (Zhao et al., [2024](https://arxiv.org/html/2510.09407v1#bib.bib70)), which involves the merging of diverse information channels (in a way that goes beyond simple concatenation), has been shown to provide more precise predictions than models based solely on unimodal data, in a variety of application settings ranging from sentiment and emotion analysis (Poria et al., [2017](https://arxiv.org/html/2510.09407v1#bib.bib48)) to corporate credit risk prediction (Tavakoli et al., [2025](https://arxiv.org/html/2510.09407v1#bib.bib57); Lu et al., [2025](https://arxiv.org/html/2510.09407v1#bib.bib40)). However, most applications in the latter setting have thus far focused on combining textual and numeric data modalities. In contrast, work on multimodal fusion that incorporates network data in the SME context remains scarce and largely unexplored.

Hence, this paper sets out a novel approach that integrates multilayer networks into SME credit risk modelling, explicitly addressing the correlations and contagion risks inherent among interconnected SMEs. Our study focuses on improving the precision of credit risk assessments for SMEs and gaining valuable insights by leveraging the information contained in these networks. Our research questions are thus:

1. 1.

   Does incorporating network data into predictive models improve their accuracy or provide a more in-depth understanding of how credit risk spreads among interconnected SMEs? If so, what is the most effective way to combine network data with structured data?
2. 2.

   Is it advantageous to use multilayer networks over single-layer networks, and which type of connection between SMEs proves to be more informative?
3. 3.

   What insights can be gained by considering the directionality and intensity of these connections?

The remainder of the paper is structured as follows. The next section reviews prior work on machine learning with network data and SME credit risk modelling. Section [3](https://arxiv.org/html/2510.09407v1#S3 "3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") details the methodology, including multilayer networks and the models created for this study. Section [4](https://arxiv.org/html/2510.09407v1#S4 "4 Experimental setup ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") discusses the data, network construction, and experiments conducted. Section [5](https://arxiv.org/html/2510.09407v1#S5 "5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") presents the experimental results. Section [6](https://arxiv.org/html/2510.09407v1#S6 "6 Discussion ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") highlights some discussion points and summarises our findings. Finally, the last section provides conclusions and suggests directions for future research.

## 2 Previous work

### 2.1 Modelling credit risk for SMEs using network data

Acknowledging that SMEs are susceptible to the financial distress of related businesses (Long et al., [2022](https://arxiv.org/html/2510.09407v1#bib.bib38)), a growing body of literature has sought to use network data to enhance credit risk modelling, by incorporating information on connections with suppliers, customers, financial institutions, or ownership ties. This approach is based on network theory, with Borgatti & Halgin ([2011](https://arxiv.org/html/2510.09407v1#bib.bib11)) demonstrating how the position of an organisation within a network can provide critical insights into its financial stability and performance. The objective has been to capture the mutual dependencies among firms and to better understand how financial distress propagates throughout an interconnected ecosystem (Berloco et al., [2021](https://arxiv.org/html/2510.09407v1#bib.bib9)).

In a financial network setting, Iori et al. ([2008](https://arxiv.org/html/2510.09407v1#bib.bib29)) examined overnight interbank lending, showing that centrality metrics indicate the systemic importance of a node. Extending this logic to SMEs, other studies suggested that the risk of a firm is affected by the financial health of its connected counterparts. Giesecke & Weber ([2004](https://arxiv.org/html/2510.09407v1#bib.bib24)) provided evidence that cyclical correlations and contagion between firms can amplify portfolio losses, whereas Beaver et al. ([2019](https://arxiv.org/html/2510.09407v1#bib.bib8)) showed that group affiliation — such as parent–subsidiary relationships — affects default risk through risk sharing within corporate structures. More recently, common ownership has emerged as another channel of contagion. Massa & Žaldokas ([2017](https://arxiv.org/html/2510.09407v1#bib.bib44)) showed that the presence of ownership links between firms influences credit conditions by altering monitoring incentives. Zhou et al. ([2022](https://arxiv.org/html/2510.09407v1#bib.bib71)) further found that firms are more likely to exhibit discreditable behaviour if they are thus tied to other discreditable firms, highlighting how reputational risks propagate along ownership structures. Another line of work derives inter-firm links from payment or transaction data. For example, Letizia & Lillo ([2019](https://arxiv.org/html/2510.09407v1#bib.bib36)) employed company payment networks and found evidence of risk homophily, as companies with similar credit ratings exhibited a higher probability of being connected. This finding shows how the composition of the neighbourhood relates to creditworthiness. More generally, these studies illustrate how financial links, ownership ties, and transactional networks each represent different channels of contagion — though most have focused on one type of connection at a time.

Several empirical studies have also sought to operationalise relational risk by extracting statistical features from inter-firm networks. Vinciotti et al. ([2019](https://arxiv.org/html/2510.09407v1#bib.bib60)) analysed how the number of financially linked firms and their default history influence the risk of SME credit, distilling relational information into a series of neighbour counts and binary indicators. Although informative, such aggregated measures simplify the heterogeneous financial health of counterparties into coarse indicators, limiting their ability to capture the dynamics of distress propagation. Other work has taken this further by modelling correlated default dependencies (Calabrese et al., [2019](https://arxiv.org/html/2510.09407v1#bib.bib17)) or employing multilayer network structures (Óskarsdóttir & Bravo, [2021](https://arxiv.org/html/2510.09407v1#bib.bib46)) to quantify contagion channels. Yet, such approaches tend to be assumption-driven, relying on pre-specified models of how dependencies or layers operate, rather than learning flexible relational representations directly from data.

In response to these limitations, this study develops a multimodal network learning framework that integrates both the structural position of SMEs within multilayer networks and the financial attributes of their connected firms. This design moves beyond pre-specified dependencies and aggregated neighbour statistics, instead embedding relational signals in a data-driven manner. The resulting framework provides a more fine-grained and dynamic representation of how inter-firm dependencies influence credit risk, enabling richer insights into the mechanisms of financial contagion in SME networks.

### 2.2 Modelling credit risk for SMEs using multimodal learning

The primary challenge in assessing SME credit risk lies in the diversity and informality of SME operations. Financial data on SMEs is often limited, making traditional credit scoring methods less effective. Furthermore, SMEs exhibit a high degree of heterogeneity in their operations, which financial ratios alone cannot fully capture (Smit & Watkins, [2012](https://arxiv.org/html/2510.09407v1#bib.bib53)). Advances in artificial intelligence have sparked interest in applying multimodal learning techniques (Ramachandram & Taylor, [2017](https://arxiv.org/html/2510.09407v1#bib.bib49)) to enhance the accuracy and reliability of credit risk assessments for small companies. The rationale for adopting multimodal learning is to integrate complementary information from diverse sources while reducing redundancy due to overlapping features across modalities. By allowing each modality to be represented with its own parameters, the framework preserves modality-specific information and avoids the oversimplification that can arise from forcing different data sources through a single shared representation (Baltrušaitis et al., [2018](https://arxiv.org/html/2510.09407v1#bib.bib6)).

In SME credit risk assessment, multimodal learning looks beyond financial ratios to include unstructured data sources such as social media engagement, online reviews, and news coverage. For example, Stevenson et al. ([2021](https://arxiv.org/html/2510.09407v1#bib.bib55)) employed a multimodal approach to predict small business default, incorporating both standard financial data and textual evaluations from loan officers. Mai et al. ([2019](https://arxiv.org/html/2510.09407v1#bib.bib43)) showed how the combination of textual data with traditional accounting-based ratios and market-based variables improved the prediction of corporate bankruptcy. Zhang et al. ([2022](https://arxiv.org/html/2510.09407v1#bib.bib69)) fused firm-level demographic attributes – such as age, size, industry, and geographic location – with behavioural financial data – such as payment histories, credit use, and transaction records – to assess the risk of SME credit in supply chain finance. Using accounting, market, and pricing data, Korangi et al. ([2023](https://arxiv.org/html/2510.09407v1#bib.bib32)) introduced a multimodal transformer-based framework to predict default probabilities for mid-cap companies. Tavakoli et al. ([2025](https://arxiv.org/html/2510.09407v1#bib.bib57)) developed multimodal models to predict external credit ratings by applying different fusion strategies to textual data originating from earnings call transcripts and numerical data.

Incorporating a network data modality into SME credit risk models represents another step forward, enabling a more comprehensive view of creditworthiness by considering the interdependencies that affect firm performance. Specifically, this study advances SME credit risk modelling by leveraging explicit inter-firm network information. Using multimodal learning, we derive novel insights into SME default risk from two distinct data modalities. Unlike previous studies that merged these heterogeneous data into a single modality (Vinciotti et al., [2019](https://arxiv.org/html/2510.09407v1#bib.bib60); Yin et al., [2020](https://arxiv.org/html/2510.09407v1#bib.bib64); Rishehchi Fayyaz et al., [2021](https://arxiv.org/html/2510.09407v1#bib.bib51)), we explicitly treat them as separate inputs, allowing independent learning of their respective contributions and combined representation through data fusion. This yields a richer depiction of SME credit risk, capturing how firm characteristics and inter-firm connections jointly influence the probability of default. Importantly, embedding the network structure directly into the risk representation also provides a lens to infer the mechanisms of financial contagion.

## 3 Methodology

In this section, we describe our methodology. First, we detail the process of building multilayer networks. Next, we describe the different types of graph neural networks (GNNs) that we use to encode topological dependencies in the networks. Following this, we elaborate on information fusion strategies and then describe the different models implemented in this study and their respective architectures.

### 3.1 Multilayer networks

Consider a network represented as G=(V,A,X)G=(V,A,X), where V={v1,v2,…,vn}V=\{v\_{1},v\_{2},...,v\_{n}\} denotes the collection of nodes, n=|V|n=|V| represents the total number of unique nodes and X∈ℝn×dX\in\mathbb{R}^{n\times d} is a feature matrix. In this matrix, XiX\_{i} is a column vector that contains the characteristics of node viv\_{i}, and dd is the number of features. The network is characterised by its supra-adjacency matrix, A∈ℝn​l×n​lA\in\mathbb{R}^{nl\times nl}, where ll denotes the number of layers. This matrix records the connectivity between pairs of nodes within the same layer and between pairs of nodes across different layers, that is, if viv\_{i} from layer kk and vjv\_{j} from layer mm are connected (1≤k,m≤l)(1\leq k,m\leq l), then A(k−1)​n+i,(m−1)​n+j=1A\_{(k-1)n+i,(m-1)n+j}=1; otherwise, the value is 0. In such a network, although every layer shares the same node set, the connections between them differ. Each layer is dedicated to a specific type of relationship, with edges within a layer linking nodes based on relatedness. In addition, a series of interlayer edges simply specify which nodes are identical. To dive deeper into the network’s structure, an embedding derived from the network is necessary, a process detailed in the subsequent subsection. Fig. [1](https://arxiv.org/html/2510.09407v1#S3.F1 "Figure 1 ‣ 3.1 Multilayer networks ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") illustrates a multilayer network along with its supra-adjacency matrix.

![Refer to caption](x1.png)


Figure 1: A multilayer network (left) and its supra adjacency matrix (right). Available under the CC-BY license from Zandi et al. ([2025](https://arxiv.org/html/2510.09407v1#bib.bib65)).

### 3.2 Graph neural networks

GNNs extend traditional neural networks to effectively process and learn from network-structured data. A distinct challenge in working with such networks is capturing the topological dependencies, as neighbouring nodes can influence each other. In this work, we trial two types of GNNs: GAT (Veličković et al., [2018](https://arxiv.org/html/2510.09407v1#bib.bib59)) and GIN (Xu et al., [2019](https://arxiv.org/html/2510.09407v1#bib.bib63)). These models are employed to extract topological relationships between a node and its neighbours and encode both the network’s structural information and the node features, thereby effectively capturing the information embedded in node connections.

#### 3.2.1 Graph attention networks

GAT is applied to each GG to obtain a hidden representation matrix ZZ. Each row of ZZ contains a node embedding, which means that for node viv\_{i} we have an embedding ZiZ\_{i}. The core component of GAT is an attention mechanism that computes the importance of each neighbour to a node. The attention coefficients are computed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αi​j=softmaxj(LeakyReLU(aT[Whi||Whj])).\displaystyle\alpha\_{ij}=\text{softmax}\_{j}\left(\text{LeakyReLU}\left(a^{T}[Wh\_{i}||Wh\_{j}]\right)\right). |  | (1) |

Here, hih\_{i} and hjh\_{j} are the embeddings of nodes viv\_{i} and vjv\_{j}, respectively, obtained from the previous layer (or initialised as the raw feature vectors XiX\_{i} and XjX\_{j} for the first layer). W∈ℝD×dW\in\mathbb{R}^{D\times d} is a learnable weight matrix where DD is the embedding dimension, aT∈ℝ1×2​Da^{T}\in\mathbb{R}^{1\times 2D} is a learnable weight vector, ∥\| denotes concatenation, and αi​j\alpha\_{ij} represents the attention coefficient indicating the importance of the features of node vjv\_{j} relative to node viv\_{i}. For each node, the GAT aggregates features from itself and its neighbours weighted by the attention coefficients. The updated embedding for node viv\_{i} is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi=∑vj∈N​(vi)∪{vi}αi​j​W​hj.\displaystyle Z\_{i}=\sum\_{{v\_{j}}\in N(v\_{i})\cup\{v\_{i}\}}\alpha\_{ij}Wh\_{j}. |  | (2) |

Here, ZiZ\_{i} represents the new embedding of node viv\_{i} after one GAT layer and N​(vi)N(v\_{i}) denotes the neighbours of node viv\_{i}. The embeddings are iteratively updated in each layer. Note that we also include the self-edge for each node. GAT often employs multihead attention for more stable learning. This means running several independent attention mechanisms in parallel and concatenating (or averaging) their outputs.

GATs are powerful because they dynamically assign importance to nodes’ neighbours, enabling the model to focus on the most relevant information in the network. This adaptability makes GATs effective for various network-based tasks where the structure and connectivity of the data are crucial.

#### 3.2.2 Graph isomorphism networks

GIN, a second type of GNN used in this study, was developed to address the limitations of the previous GNN in distinguishing between different network structures. The key concept behind GIN is to enable the model to have the same discriminative power as the Weisfeiler-Lehman (WL) network isomorphism test (Weisfeiler & Lehman, [1968](https://arxiv.org/html/2510.09407v1#bib.bib62)), a classical algorithm used for network comparison. In GIN, each node aggregates information from its neighbours to update its own features. The update mechanism is designed to be as powerful as the WL test in terms of distinguishing different network structures. The hidden representation of each node is updated based on both its own embedding and the aggregated embeddings of its neighbours. The update rule is formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi=MLP​((1+ε)​hi+∑j∈N​(vi)hj).\displaystyle Z\_{i}=\text{MLP}\left((1+\varepsilon)h\_{i}+\sum\_{j\in N(v\_{i})}h\_{j}\right). |  | (3) |

Here, ε\varepsilon is a learnable parameter or a fixed scalar, and MLP represents a multilayer perceptron. As before, the embeddings hih\_{i} and hjh\_{j} are iteratively updated in each layer, with hi=Xih\_{i}=X\_{i} as the initial node representation in the first layer. The update rule ensures that a node’s own embedding is considered in addition to the aggregated embeddings of its neighbours. The inclusion of ε\varepsilon allows the model to learn the importance of a node’s own embedding relative to its neighbours.

The strength of GIN lies in its ability to effectively capture the structural information of networks. It can distinguish between different network structures that other GNN models might fail to differentiate. This makes GIN particularly useful in tasks that require a detailed understanding of network topology, such as social network analysis, where embedding the precise structure of the network is crucial.

### 3.3 Information fusion

To enable deep learning from both structured and semi-structured data, we will examine the effectiveness of different information fusion approaches.

#### 3.3.1 Fusion levels

Information fusion refers to the association, correlation, and combination of data from single or multiple sources (Zhang et al., [2018](https://arxiv.org/html/2510.09407v1#bib.bib68)). The concept of fusion level refers to the specific point in the processing pipeline where this merging occurs. Fig. [2](https://arxiv.org/html/2510.09407v1#S3.F2 "Figure 2 ‣ 3.3.1 Fusion levels ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") shows the three primary fusion levels: early, intermediate, and late fusion. Early fusion, also known as signal fusion, merges raw data directly with the aim of retaining maximal information and leaving filtering to the model. By avoiding manual feature selection or aggregation, it minimises bias by not imposing prior assumptions about feature relevance. However, the resulting high-dimensional feature space can increase variance if not properly regularised (Luo & Kay, [1988](https://arxiv.org/html/2510.09407v1#bib.bib42)). Intermediate fusion is a higher-level fusion in which data merging does not occur until after initial processing by earlier layers of the deep learning model (Boulahia et al., [2021](https://arxiv.org/html/2510.09407v1#bib.bib13)). Late fusion, the highest level, involves the integration of information that has already been extracted as abstract features or that can even assume the form of predictions generated by previous models (Luo & Kay, [1988](https://arxiv.org/html/2510.09407v1#bib.bib42)). Additionally, hybrid fusion combines different fusion levels, such as early and late fusion, when integrating information from different modalities (Chango et al., [2022](https://arxiv.org/html/2510.09407v1#bib.bib18)). In this study, we consider both simple and hybrid fusion, employing early and intermediate fusion levels. By combining both levels, we seek to leverage their respective benefits, as early fusion can capture a broad range of unprocessed information, whilst intermediate fusion handles more refined features.

![Refer to caption](x2.png)


Figure 2: The three primary fusion levels: early, intermediate, and late.

#### 3.3.2 Fusion techniques

This study explores two fusion techniques: concatenation and cross-attention. The former is a simple operation-based method, while the latter is an attention-driven approach (Zhang et al., [2020a](https://arxiv.org/html/2510.09407v1#bib.bib66)). Concatenation as a data fusion strategy involves combining feature vectors from multiple modalities into one extended feature vector. This new vector then serves as an input for machine learning tasks. The simplicity of concatenation makes it widely applicable, although it does not account for complex interactions between features from different modalities.

The second method, that is, cross attention, is a more intricate fusion technique that is especially relevant in deep learning settings where understanding the interplay between different types of data is crucial (Lee et al., [2018](https://arxiv.org/html/2510.09407v1#bib.bib34)). For two different modalities, the model generates queries (Q)(Q) from one modality and keys (K)(K) and values (V)(V) from the other modality. Attention scores are calculated by taking the dot product of queries with keys. This is often scaled down by the square root of the dimensionality of the keys to avoid overly large dot product values, which can lead to gradient vanishing problems during training. The raw scores are then normalised across all keys using the softmax function, which turns them into a distribution of weights that sum to one. These attention weights are subsequently used to create a weighted sum of the values, which gives us the final output of the cross-attention mechanism, emphasising the parts of one modality that are most relevant to each element of the other modality. The formula for this calculation is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Output=softmax​(Q​KTdk)​V.\displaystyle\text{Output}=\text{softmax}(\frac{QK^{T}}{\sqrt{d\_{k}}})V. |  | (4) |

Here, dkd\_{k} is the dimensionality of the keys and KTK^{T} represents the transpose of the key matrix. The output of the cross-attention mechanism can then be used as a fused representation of the two modalities, combining the information in a way that is contextually enriched by the intermodal relationships. Cross-attention thus allows the model to adaptively focus on the most pertinent information from one modality informed by another.

#### 3.3.3 Fusion strategies

Our empirical analysis hence aims to identify, for our specific application, the most effective combination of: 1) GNN type, 2) fusion
techniques, and 3) fusion levels. In our experiments, we test both GAT and GIN (applied to a sequence of τ\tau graph snapshots, as Section [4.2](https://arxiv.org/html/2510.09407v1#S4.SS2 "4.2 Network construction ‣ 4 Experimental setup ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") will later explain), each of which we combine with four different fusion strategies (as illustrated in Fig. [3](https://arxiv.org/html/2510.09407v1#S3.F3 "Figure 3 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") adapted from Tavakoli et al., [2025](https://arxiv.org/html/2510.09407v1#bib.bib57)). This creates a total of eight multimodal model variations, designed to deal with two types of input channels: the semi-structured (network) data and the structured (tabular) data (hence, the resulting models will be referred to as bimodal models). The respective fusion strategies are classified as follows.

* •

  Strategy 1 – Simple Concatenation: As shown in Fig. [3(a)](https://arxiv.org/html/2510.09407v1#S3.F3.sf1 "In Figure 3 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ"), the semi-structured and structured channels are processed through the (neural) networks A and B, respectively. Their penultimate layers are concatenated employing a simple form of intermediate fusion.
* •

  Strategy 2 – Simple Concatenation-Attention: Fig. [3(b)](https://arxiv.org/html/2510.09407v1#S3.F3.sf2 "In Figure 3 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") shows a setup in which the penultimate layers of the semi-structured modality are concatenated and then fused using cross-attention with the neural network layer for the structured data.
* •

  Strategy 3 – Hybrid Concatenation (see Fig. [3(c)](https://arxiv.org/html/2510.09407v1#S3.F3.sf3 "In Figure 3 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ")): This setup uses a hybrid fusion approach, in which all semi-structured data undergo early fusion and are fed into neural network A. The structured data is processed through network B. The penultimate layers of the different modalities are then merged by concatenation.
* •

  Strategy 4 – Hybrid Concatenation-Attention (Fig. [3(d)](https://arxiv.org/html/2510.09407v1#S3.F3.sf4 "In Figure 3 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ")): This strategy is similar to the previous strategy, except that it uses cross-attention to fuse the penultimate layers of the two modalities.

![Refer to caption](x3.png)


(a) Strategy 1 - Simple Concatenation

![Refer to caption](x4.png)


(b) Strategy 2 - Simple Concatenation-Attention

![Refer to caption](x5.png)


(c) Strategy 3 - Hybrid Concatenation

![Refer to caption](x6.png)


(d) Strategy 4 - Hybrid Concatenation-Attention

Figure 3: The proposed fusion strategies for the multimodal models. Adapted from Tavakoli et al. ([2025](https://arxiv.org/html/2510.09407v1#bib.bib57)).

In Fig. [3](https://arxiv.org/html/2510.09407v1#S3.F3 "Figure 3 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ"), networks A and B consist of a set of densely connected neurons followed by a series of layers that either apply a chosen activation function to introduce non-linearity or use a dropout function for regularisation. The parameters for each of these networks, such as neuron count and dropout rate, are optimised for the best performance on the validation set. Fig. [4](https://arxiv.org/html/2510.09407v1#S3.F4 "Figure 4 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") provides an overview of the architectures of these networks.

![Refer to caption](x7.png)


Figure 4: An overview of the architectures of networks A and B.

### 3.4 Unimodal and bimodal models

In addition to our proposed bimodal model variations, we also tested some simpler unimodal alternatives. Referred to as Unimod-GNN, these are single-channel (unimodal) models, built using either GAT or GIN, that exclusively employ the network data and within which each network node contains a self-loop. By connecting each node back to itself, we aim to preserve the node’s own features during the learning process. Fig. [5(a)](https://arxiv.org/html/2510.09407v1#S3.F5.sf1 "In Figure 5 ‣ 3.4 Unimodal and bimodal models ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") presents a schematic representation of this model, comprising a sequence of processes that begin with multiple GNN instances being used to process the different network snapshots. Next, the outputs of these GNNs are concatenated into a single representation. The combined data is then fed into a feedforward neural network (FNN), which further processes the information to produce a final prediction output.

The second series of models, i.e. Bimod-GNN, are two-channel (bimodal) models that process the network and the tabular data, alongside each other. Fig. [5(b)](https://arxiv.org/html/2510.09407v1#S3.F5.sf2 "In Figure 5 ‣ 3.4 Unimodal and bimodal models ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") shows their structure. As before, a series of GNNs are used to process the network data, but now their output is fused with the tabular data using one of the strategies described in the previous subsection. The outputs from the fusion process then again go through an FNN which allows for further processing before arriving at the final output.

![Refer to caption](x8.png)


(a) Unimod-GNN

![Refer to caption](x9.png)


(b) Bimod-GNN

Figure 5: The unimodal and bimodal model structures.

### 3.5 FNN and loss function

Although the architecture of the FNN in Fig. [5](https://arxiv.org/html/2510.09407v1#S3.F5 "Figure 5 ‣ 3.4 Unimodal and bimodal models ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") exhibits similarities in terms of layout and design with the structure of networks A and B in Fig. [4](https://arxiv.org/html/2510.09407v1#S3.F4 "Figure 4 ‣ 3.3.3 Fusion strategies ‣ 3.3 Information fusion ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ"), a notable difference in the FNN architecture is the incorporation of an additional layer toward the end, which employs a sigmoid activation function. The purpose of this final layer is to refine the model output to make binary decisions, in this case determining whether a specific node (loan) viv\_{i} should be classified into class 11 (Yi=1Y\_{i}=1) or class 0 (Yi=0Y\_{i}=0). We let Y^i\hat{Y}\_{i} denote the probability that node viv\_{i} belongs to class ii produced by the model.

A critical element in training and evaluating the performance of a deep learning model is the choice of loss function. In the context of this study, we employ the well-known binary cross-entropy loss function (Gneiting & Raftery, [2007](https://arxiv.org/html/2510.09407v1#bib.bib25)), which can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Loss=−1n​∑i=1n[Yi​l​o​g​(Y^i)+(1−Yi)​l​o​g​(1−Y^i)].\textrm{Loss}=-\frac{1}{n}\sum\_{i=1}^{n}\left[Y\_{i}log(\hat{Y}\_{i})+(1-Y\_{i})log(1-\hat{Y}\_{i})\right]. |  | (5) |

## 4 Experimental setup

### 4.1 Dataset

In this paper, we use a comprehensive loan-level dataset provided by a prominent financial institution, containing information on loans issued to SMEs. The dataset includes data on both the loan and the borrower, covering approximately 218,000 companies and 1.2 million loan instances. Within the data, a single company may have been granted multiple loans. The features are available at the time of loan application and do not change from one month to the next. Numerical features are normalised with min-max scaling. We clean the data by treating outliers and handling null values. Specifically, outliers are capped at the 99th percentile and 1st percentile points. To handle null values in categorical and numerical features, we implement a strategy comparable to [Bravo et al.](https://arxiv.org/html/2510.09407v1#bib.bib14)’s ([2013](https://arxiv.org/html/2510.09407v1#bib.bib14)) (summarised in Appendix [A](https://arxiv.org/html/2510.09407v1#A1 "Appendix A Strategy for handling null values ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ")). In addition, to reduce redundancy and improve model performance, we remove features with high correlation, using a correlation threshold of 70%. When deciding between correlated features, we retain the one that is most strongly correlated with the target. After completing the data preparation process, we are thus left with 65 distinct features per loan that will be used to predict one-year-ahead loan default. The descriptions of the most informative features are shown in Table [1](https://arxiv.org/html/2510.09407v1#S4.T1 "Table 1 ‣ 4.1 Dataset ‣ 4 Experimental setup ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ").

Table 1: Description of most informative node features.

|  |  |
| --- | --- |
| Feature | Description |
| avg\_bal\_lia | Average balance of liabilities over the past 12 months |
| mon\_install\_amt | Monthly instalment amount for existing mortgage loans |
| tot\_rev\_gen | Total revenue generated from operations of active assets |
| if\_act\_flag\_na | Is the active flag indicator for the entity set to ‘N/A’? |
| end\_cur\_year | Endowment of the entity for the current year |
| avg\_bal\_act | Average balance of active assets |
| if\_pre\_app | Does the entity have pre-approved status? |
| ent\_own\_equ | Entity’s own equity |
| cov\_rat\_tax | Coverage ratio before taxes |
| if\_desc\_gsi | Is the description of the current worst GSI situation available? |
| adj\_tot\_rev\_gen | Adjusted total revenue generated from operations associated with liabilities |
| if\_wel\_dep\_acc | Does the offer involve a welcome deposit account with the bank? |
| if\_restruct | Has the entity undergone any restructuring? |
| if\_bur\_ind | Is there any bureau indicator assigned to the entity? |
| if\_trans\_ind | Is there any transaction indicator assigned to the entity? |
| default | Being 90 days or more in payment arrears over next 12 months (*target*) |

Loans originated from July 2019 to December 2020 are used for training. For this cohort, we observe a default rate of 3.63%, providing a suitable environment to train our models. The subsequent test phase is conducted with loans originating from January 2021 to October 2021. A key step in our experimental setup is the exclusion of any companies from the test set whose loans were included in the training dataset. This deliberate exclusion is crucial for maintaining the integrity of our test results, ensuring that there is no data overlap that could artificially inflate the performance of our predictive models.

Fig. [6](https://arxiv.org/html/2510.09407v1#S4.F6 "Figure 6 ‣ 4.1 Dataset ‣ 4 Experimental setup ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") presents the loan default rates categorised by company size (small or medium) and loan origination month. It reveals a clear trend whereby small companies exhibit higher default rates compared to medium-sized ones. This pattern highlights that smaller companies tend to be more financially vulnerable, possibly due to limited access to resources or higher sensitivity to economic fluctuations.

![Refer to caption](fig6.png)


Figure 6: Loan default rates by company size and loan origination month.

### 4.2 Network construction

As the original dataset also contains company ownership data and any financial transactions between companies that were made through the lender, we are able to construct single- and double-layer networks (see Subsection [3.1](https://arxiv.org/html/2510.09407v1#S3.SS1 "3.1 Multilayer networks ‣ 3 Methodology ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ")), using financial transactions (FT) and common ownership (CO) as the primary sources of connections. This allows us to map and analyse the complex interplay between different companies. In these networks, the nodes represent loans associated with the companies.

For each origination month, we adopt a six-month look-back period, which is similar to the approach by Zandi et al. ([2025](https://arxiv.org/html/2510.09407v1#bib.bib65)) but applied in a different context. Specifically, each origination month is assigned six snapshots, each of which represents the connections observed between the loans of that origination month and other loans originating in one of the six preceding months. To illustrate, consider loans that originated in July 2019 (see Fig. [7](https://arxiv.org/html/2510.09407v1#S4.F7 "Figure 7 ‣ 4.2 Network construction ‣ 4 Experimental setup ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ")). We begin by identifying the companies to which these loans were issued. Next, we observe what other companies exhibited a relationship with those companies at any time from January to June 2019, referring to the former as our pool of ‘neighbouring’ companies. We then establish edges between each of the loans originating in July 2019, and any loans issued to its neighbouring companies, provided that they originated in January 2019. This produces a first snapshot, G(1)G^{(1)}. To form G(2)G^{(2)}, we connect loans originating in July 2019 with loans from neighbouring companies originating in February 2019. We continue this process until we connect loans originating in July 2019 with loans from neighbouring companies originating in June 2019, thus forming our sixth snapshot, G(6)G^{(6)}. This procedure is repeated by moving the origination month by one month each time, ensuring that the entire period is covered.

![Refer to caption](x10.png)


Figure 7: Snapshots corresponding to the July 2019 origination month.

The rationale for this design is that the effects of inter-firm relationships on credit risk are rarely immediate, but instead materialise over several months through mechanisms such as delayed payments, supply chain disruptions, or gradual transmission of financial distress (Berloco et al., [2021](https://arxiv.org/html/2510.09407v1#bib.bib9)). Restricting the look-back period to six months ensures that the connected firms also have relatively recent loan applications in the dataset. This window allows us to capture both short-term and lagged dependencies while avoiding the noise and dilution associated with excessively long windows, thereby striking a balance between economic intuition and predictive tractability in modelling SME credit risk (Huang & Yang, [2024](https://arxiv.org/html/2510.09407v1#bib.bib28)).

During the training phase for each origination month, our objective is to predict defaults within the 12 months following that month. A one-year horizon is practical for credit management and decision making, offering a balance between providing enough time to accurately assess risk and avoiding the uncertainty associated with longer-term predictions (Lopez & Saidenberg, [2000](https://arxiv.org/html/2510.09407v1#bib.bib39)).

### 4.3 Model evaluation

Our research involves evaluating the predictive performance of several unimodal and bimodal models and comparing them with that of established baseline methods. Given the class imbalance within this binary classification problem, we employ the Area Under the Receiver Operating Characteristic Curve (AUC), which reflects a model’s ability to distinguish between default and non-default cases across the range of thresholds, and the Area Under the Precision–Recall Curve (AUCPR), which emphasises performance on the minority (default) class, as the two primary means of measuring each model’s performance. The results of these evaluations are reported, accompanied by 95% confidence intervals obtained by bootstrapping applied to the test dataset.

We perform a modality contribution analysis to infer the relative importance of each input modality in shaping the fused representation learnt by the model. We also investigate how accounting for the directionality and weight of connections affects the performance of the best-performing model and enhances the analysis of risk propagation. Since, similarly to other operational research problems, explainability is a key consideration (De Bock et al., [2024](https://arxiv.org/html/2510.09407v1#bib.bib20)), we complete the analysis by employing the Shapley approach (Lundberg & Lee, [2017](https://arxiv.org/html/2510.09407v1#bib.bib41)) to gain additional information on the contributions of individual features.

## 5 Results

### 5.1 Performance of the baseline methods

To compare our proposed network models, we have trained several baseline models that use only tabular data. Table [2](https://arxiv.org/html/2510.09407v1#S5.T2 "Table 2 ‣ 5.1 Performance of the baseline methods ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") displays the performance results for four baseline methods: Logistic Regression (LR) (Hosmer Jr. et al., [2013](https://arxiv.org/html/2510.09407v1#bib.bib27)), Random Forest (RF) (Breiman, [2001](https://arxiv.org/html/2510.09407v1#bib.bib16)), XGBoost (XGB) (Chen & Guestrin, [2016](https://arxiv.org/html/2510.09407v1#bib.bib19)), and a Deep Neural Network (DNN) (LeCun et al., [2015](https://arxiv.org/html/2510.09407v1#bib.bib33)). Among these, LR is preferred in some settings for its simplicity and ease of interpretation. RF, on the other hand, is known for its robustness and ability to handle large and complex datasets with high accuracy. XGB is recognised as a powerful technique for classification and regression tasks involving structured datasets. In recent years, DNN has gained popularity for a variety of predictive tasks. We perform a grid search to tune the hyperparameters for each model, using a validation set that covers 20% of the data. Details of tuning and DNN architecture are provided in Appendix [B](https://arxiv.org/html/2510.09407v1#A2 "Appendix B Hyperparameter tuning for baseline models ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") and Appendix [C](https://arxiv.org/html/2510.09407v1#A3 "Appendix C Architecture of the DNN baseline model ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ"), respectively.

Table 2: Performance of the baseline models.

| Model | AUC | AUCPR |
| --- | --- | --- |
| LR | 0.821±0.0160.821\pm 0.016 | 0.322±0.0140.322\pm 0.014 |
| RF | 0.853±0.0150.853\pm 0.015 | 0.382±0.0120.382\pm 0.012 |
| XGB | 0.863±0.014\mathbf{0.863\pm 0.014} | 0.398±0.012\mathbf{0.398\pm 0.012} |
| DNN | 0.839±0.0140.839\pm 0.014 | 0.345±0.0100.345\pm 0.010 |

Table [2](https://arxiv.org/html/2510.09407v1#S5.T2 "Table 2 ‣ 5.1 Performance of the baseline methods ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") reports the out-of-time performance of these baseline models, showing that XGB performs the best among them (indicated in bold), closely followed by RF. Of the four, LR is the weakest performer, which was expected given its linear nature. The DNN’s performance sits in between, indicating that while deep learning techniques have potential, their performance can be hindered by the need for extensive tuning and large amounts of data. In general, the baseline results set a high bar against which the proposed models will be compared.

### 5.2 Performance of the proposed models

We apply the unimodal and bimodal models proposed earlier to each type of single network layer, i.e. derived either from the financial transaction (FT) or common ownership (CO) data, and to the double-layer networks. To facilitate comparison, the training, validation, and test sets are kept consistent with those used in the baseline model experiments. Details regarding the hyperparameter tuning for GAT and GIN are provided in Appendix [D](https://arxiv.org/html/2510.09407v1#A4 "Appendix D Hyperparameter tuning for GAT and GIN models ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ"). Next, Table [3](https://arxiv.org/html/2510.09407v1#S5.T3 "Table 3 ‣ 5.2 Performance of the proposed models ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") presents the performance of the unimodal models, while Table [4](https://arxiv.org/html/2510.09407v1#S5.T4 "Table 4 ‣ 5.2 Performance of the proposed models ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") shows the performance of the bimodal models. The best-performing model in each table is again highlighted in bold.

Table 3: Performance of the unimodal models.

| Model | | Single Layer: FT | | Single Layer: CO | | Double Layer: FT-CO | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy | GNN | AUC | AUCPR | AUC | AUCPR | AUC | AUCPR |
| Unimod | GAT | 0.820±0.0140.820\pm 0.014 | 0.310±0.0110.310\pm 0.011 | 0.813±0.0120.813\pm 0.012 | 0.306±0.0130.306\pm 0.013 | 0.828±0.015\mathbf{0.828\pm 0.015} | 0.323±0.010\mathbf{0.323\pm 0.010} |
| GIN | 0.814±0.0140.814\pm 0.014 | 0.308±0.0100.308\pm 0.010 | 0.802±0.0130.802\pm 0.013 | 0.282±0.0120.282\pm 0.012 | 0.822±0.0120.822\pm 0.012 | 0.314±0.0100.314\pm 0.010 |

For the unimodal models, it can be seen from Table [3](https://arxiv.org/html/2510.09407v1#S5.T3 "Table 3 ‣ 5.2 Performance of the proposed models ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") that GAT yields better results than GIN, across all network configurations. The observed performance differential is likely attributable to practical factors such as sensitivity to hyperparameter tuning, training stability, and the risk of overfitting. Moreover, GAT’s attention mechanism provides a useful means of encoding how different neighbours contribute to prediction, which may explain why its representations appear better aligned with the structure of SME networks in our experiments. The best-performing unimodal model, i.e. Unimod-GAT, is still outperformed, though, by the best-performing baseline model, XGB. This outcome is consistent with the known robustness of tree-based ensemble methods for structured tabular data, and underscores that deep learning models are not necessarily superior in any context (Borisov et al., [2022](https://arxiv.org/html/2510.09407v1#bib.bib12); Gunnarsson et al., [2021](https://arxiv.org/html/2510.09407v1#bib.bib26)).

Table 4: Performance of the bimodal models.

| Model | | Single Layer: FT | | Single Layer: CO | | Double Layer: FT-CO | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy | GNN | AUC | AUCPR | AUC | AUCPR | AUC | AUCPR |
| Simple Concat | GAT | 0.845±0.0100.845\pm 0.010 | 0.350±0.0080.350\pm 0.008 | 0.841±0.0120.841\pm 0.012 | 0.349±0.0090.349\pm 0.009 | 0.849±0.0120.849\pm 0.012 | 0.361±0.0070.361\pm 0.007 |
| GIN | 0.841±0.0110.841\pm 0.011 | 0.348±0.0090.348\pm 0.009 | 0.840±0.0110.840\pm 0.011 | 0.347±0.0100.347\pm 0.010 | 0.844±0.0090.844\pm 0.009 | 0.358±0.0080.358\pm 0.008 |
| Simple Concat-Att | GAT | 0.852±0.0120.852\pm 0.012 | 0.359±0.0080.359\pm 0.008 | 0.844±0.0110.844\pm 0.011 | 0.357±0.0100.357\pm 0.010 | 0.855±0.0110.855\pm 0.011 | 0.366±0.0090.366\pm 0.009 |
| GIN | 0.840±0.0090.840\pm 0.009 | 0.345±0.0090.345\pm 0.009 | 0.839±0.0120.839\pm 0.012 | 0.341±0.0080.341\pm 0.008 | 0.842±0.0080.842\pm 0.008 | 0.355±0.0080.355\pm 0.008 |
| Hybrid Concat | GAT | 0.857±0.0120.857\pm 0.012 | 0.372±0.0090.372\pm 0.009 | 0.852±0.0100.852\pm 0.010 | 0.365±0.0080.365\pm 0.008 | 0.863±0.0120.863\pm 0.012 | 0.392±0.0100.392\pm 0.010 |
| GIN | 0.853±0.0100.853\pm 0.010 | 0.369±0.0100.369\pm 0.010 | 0.847±0.0080.847\pm 0.008 | 0.357±0.0080.357\pm 0.008 | 0.859±0.0110.859\pm 0.011 | 0.373±0.0070.373\pm 0.007 |
| Hybrid Concat-Att | GAT | 0.866±0.0120.866\pm 0.012 | 0.397±0.0110.397\pm 0.011 | 0.861±0.0090.861\pm 0.009 | 0.375±0.0070.375\pm 0.007 | 0.872±0.008\mathbf{0.872\pm 0.008} | 0.406±0.008\mathbf{0.406\pm 0.008} |
| GIN | 0.849±0.0110.849\pm 0.011 | 0.359±0.0090.359\pm 0.009 | 0.845±0.0090.845\pm 0.009 | 0.356±0.0080.356\pm 0.008 | 0.856±0.0120.856\pm 0.012 | 0.371±0.0100.371\pm 0.010 |

However, the results shown in Table [4](https://arxiv.org/html/2510.09407v1#S5.T4 "Table 4 ‣ 5.2 Performance of the proposed models ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") demonstrate that bimodal models generally produce better results compared to unimodal models, while the reported metrics also have narrower confidence intervals, suggesting greater robustness. This improved performance can possibly be attributed to the ability of bimodal models to integrate and leverage information from both the network and traditional structured data simultaneously. We also find that hybrid fusion strategies outperform simple concatenation ones. The latter is likely due to hybrid approaches being capable of preserving detailed signals while also modelling more abstract cross-modal dependencies, which may be useful when combining heterogeneous data such as tabular data and network embeddings. Specifically, the hybrid concatenation-attention strategy using GAT, applied to double-layer networks, achieves the highest AUC of 0.872 and an AUCPR of 0.406, thus outperforming the best baseline model. This underscores the effectiveness of advanced fusion techniques, such as cross-attention, in capturing complex interactions between different modalities. However, it should be noted that there is a slight overlap between the confidence interval of the best-performing model and those of its closest competitors.

Another notable aspect is that the financial transaction network data appears more informative than the common ownership network. Direct financial transactions between firms can point to inter-firm dependencies, providing insight into financial health and stability that prove important for assessing creditworthiness. In contrast, the common ownership network, while valuable, captures more static structural relationships and may not reflect current financial realities as effectively. Ownership links can signal financial support or risk contagion, but lack the detailed transactional information provided by financial transfers.

The results also highlight the predictive performance gains of using double-layer networks over single-layer ones, suggesting that incorporating multiple types of connections allows the models to capture more nuanced patterns of credit risk contagion.

### 5.3 Modality contribution analysis

To better understand the relative importance of each modality in the best performing proposed model, that is, the hybrid Concat-Att-GAT, we perform a modality contribution analysis. We compute two separate cross-attention outputs: one where the tabular representation attends to the network representation and another where the network representation attends to the tabular representation.

Formally, let QTQ\_{T} and QNQ\_{N} be the queries derived from the tabular and network modalities, respectively. Let KT,VTK\_{T},V\_{T} denote the keys and values of the tabular modality and KN,VNK\_{N},V\_{N} those of the network modality. We compute two attended representations as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RN=Attn​(QT,KN,VN),\displaystyle R\_{N}=\textrm{Attn}(Q\_{T},K\_{N},V\_{N}), |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | RT=Attn​(QN,KT,VT).\displaystyle R\_{T}=\textrm{Attn}(Q\_{N},K\_{T},V\_{T}). |  | (7) |

Here, RNR\_{N} captures how much the network contributes to the refinement of the tabular query, while RTR\_{T} captures how much the tabular modality contributes to the representation of the network. We quantify the contribution of each modality using the relative ℓ2\ell\_{2} norm of the attended outputs as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CN=‖RN‖2‖RT‖2+‖RN‖2+ϵ,\displaystyle C\_{N}=\frac{\|R\_{N}\|\_{2}}{\|R\_{T}\|\_{2}+\|R\_{N}\|\_{2}+\epsilon}, |  | (8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CT=‖RT‖2‖RT‖2+‖RN‖2+ϵ.\displaystyle C\_{T}=\frac{\|R\_{T}\|\_{2}}{\|R\_{T}\|\_{2}+\|R\_{N}\|\_{2}+\epsilon}. |  | (9) |

Above, CNC\_{N} and CTC\_{T} represent the contributions of the network and tabular modalities, respectively, and ϵ\epsilon is a small constant for numerical stability. Fig. [8](https://arxiv.org/html/2510.09407v1#S5.F8 "Figure 8 ‣ 5.3 Modality contribution analysis ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") shows the distributions of the normalised contributions by the tabular and network data.

![Refer to caption](fig8.png)


Figure 8: Distributions of normalised modality contributions to the final fused representation. The dashed lines indicate mean contributions from each modality.

It can be observed that both modalities contribute meaningfully to the final fused representation with the distributions centred around the midpoint of the normalised scale. The mean contribution from the network modality is slightly higher than that of the tabular modality, suggesting that, in the current task, the GNN embeddings exert a stronger effect in shaping the final representation. This outcome aligns with the intuition that structural information encoded in the network topology can enhance learning, especially when node interactions are important for prediction. However, the overlap between the two distributions indicates that the model benefits from both sources of data and does not ignore either modality, highlighting the advantage of modelling interactions between the two modalities rather than relying on either in isolation.

### 5.4 Effects of edge direction and weights

Table [5](https://arxiv.org/html/2510.09407v1#S5.T5 "Table 5 ‣ 5.4 Effects of edge direction and weights ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") explores the impact of including edge directionality and weights on the performance of the hybrid Concat-Att-GAT model for double-layer networks. In the financial transaction layer, the edge direction represents the flow of transactions between two firms, and the weight is determined by dividing the total sum of the transaction values by the number of transactions over a period of six months, following the approaches commonly used in transaction network studies (Saxena et al., [2021](https://arxiv.org/html/2510.09407v1#bib.bib52); Elliott et al., [2019](https://arxiv.org/html/2510.09407v1#bib.bib22)). A logarithmic transformation is applied to the edge weights to enhance training stability and mitigate the risk of gradient explosion that can arise from excessively large weight values (Li et al., [2024](https://arxiv.org/html/2510.09407v1#bib.bib37)). For the common ownership layer, the edges are bidirectional, and their weights are uniformly set at 1.

Table 5: Performance of the best-performing proposed model on directed and/or weighted networks.

| Model | | Edges | | Double Layer: FT-CO | |
| --- | --- | --- | --- | --- | --- |
| Strategy | GNN | Directed | Weighted | AUC | AUCPR |
| Hybrid Concat-Att |  | ✓\checkmark | ×\times | 0.872±0.0100.872\pm 0.010 | 0.407±0.0090.407\pm 0.009 |
| GAT | ×\times | ✓\checkmark | 0.878±0.0120.878\pm 0.012 | 0.412±0.0100.412\pm 0.010 |
|  | ✓\checkmark | ✓\checkmark | 0.879±0.011\mathbf{0.879\pm 0.011} | 0.414±0.010\mathbf{0.414\pm 0.010} |

The results suggest that incorporating edge direction and weights improves the performance somewhat, increasing AUC to 0.879 and AUCPR to 0.414, although the confidence intervals of the three model variations overlap. This modest improvement may be attributed to the added granularity and realism provided by these characteristics. The directed edges capture the asymmetry in financial relationships, which can affect the flow of credit risk contagion. Edge weighting, which appears to provide richer information than edge orientation, reflects the varying intensities of the connections between SMEs, allowing the model to differentiate between stronger and weaker financial ties. These enhancements provide deeper insight into the mechanisms of credit risk propagation, leading to more accurate predictions.

An interesting question about directional network models is whether they find that the default risk of a firm is more adversely affected by default events experienced by its payees (which may, in the context of a supply chain, be some of the firm’s direct suppliers) or its payers (i.e. by the customers of the firm). In the transaction graph layer, this corresponds to a node being connected to other defaulted nodes via outgoing or incoming edges, respectively. To shed light on this, Fig. [9](https://arxiv.org/html/2510.09407v1#S5.F9 "Figure 9 ‣ 5.4 Effects of edge direction and weights ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") contains kernel density estimates of the estimated probabilities of default for SMEs that are linked to defaulters via outgoing or incoming transactions. Separate distributions are included for the weighted and unweighted networks.

![Refer to caption](x11.png)


Figure 9: Kernel density estimates of the estimated probabilities of default for SMEs exposed to defaulters via incoming or outgoing financial transactions, in the weighted and unweighted networks.

The four density distributions shown in Fig. [9](https://arxiv.org/html/2510.09407v1#S5.F9 "Figure 9 ‣ 5.4 Effects of edge direction and weights ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") appear to be different. Notably, SMEs that have been at the receiving end of transactions from a defaulted firm tend to be assigned a higher probability of default than those that have initiated transactions towards defaulted firms. This pattern is observed in both the weighted and unweighted networks, although the effect is more pronounced in the weighted case, where stronger financial ties can amplify risk transmission.

### 5.5 Interpretability of the architecture

Since the hybrid Concat-Att-GAT model applied to directed double-layer networks yielded the best predictive performance in the previous subsection, we now employ the Shapley approach (Lundberg & Lee, [2017](https://arxiv.org/html/2510.09407v1#bib.bib41)) to further analyse this model. This method allows us to assess the relative importance of each node feature and quantify its contribution to the model outputs. Fig [10(a)](https://arxiv.org/html/2510.09407v1#S5.F10.sf1 "In Figure 10 ‣ 5.5 Interpretability of the architecture ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") provides a ranking of the most important node features in the aforementioned model, along with their importance in the best baseline model, i.e. XGB. In addition to this, Fig.[10(b)](https://arxiv.org/html/2510.09407v1#S5.F10.sf2 "In Figure 10 ‣ 5.5 Interpretability of the architecture ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") depicts how these features affect the predictions of the proposed model. Here, higher SHAP values for a (colour-coded) feature value push the model towards predicting 11 (default); lower SHAP values drive it towards 0 (non-default).

![Refer to caption](x12.png)


(a) Relative importance for Hybrid Concat-Att-GAT and XGB.

![Refer to caption](x13.png)


(b) Shapley values for Hybrid Concat-Att-GAT.

Figure 10: Summary of feature importance.

As seen from Fig. [10(a)](https://arxiv.org/html/2510.09407v1#S5.F10.sf1 "In Figure 10 ‣ 5.5 Interpretability of the architecture ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ"), the most important features in the hybrid Concat-Att-GAT model include several internal or external status indicators, such as ‘if\_pre\_app’ (pre-approval status), ‘if\_act\_flag\_na’ (missing active flag indicator), ‘if\_trans\_ind’ (transaction indicator assigned), ‘if\_restruct’ (restructuring indicator), and ‘if\_bur\_ind’ (bureau indicator assigned). In contrast, XGB places greater importance on financial metrics, including income statement items such as ‘tot\_rev\_gen’ (total revenue generated) and balance sheet measures such as ‘avg\_bal\_act’ (average active assets) and ‘avg\_bal\_lia’ (average liabilities), suggesting a preference for numerical features.

Fig. [10(b)](https://arxiv.org/html/2510.09407v1#S5.F10.sf2 "In Figure 10 ‣ 5.5 Interpretability of the architecture ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ") shows that the effects of these features generally align with expectations. For example, for the top variable, ‘if\_pre\_app’, a positive pre-approval status (coded in red) tends to reduce the predicted default risk for the company, whereas negative values (coded in blue) increase it. Missing information (e.g. positive values for ‘if\_act\_flag\_na’) tends to increase risk. So does, for example, any indication that the firm has undergone restructuring (see ‘if\_restruct’), which is again an intuitive finding.
Low values (depicted as blue dots) for ‘tot\_rev\_gen’ are strongly associated with elevated default risk (in other words, firms that generate little revenue are deemed higher risk). Having greater liabilities is also seen to add to the risk, albeit more modestly (see, for example, ‘avg\_bal\_lia’). Being deemed lower risk, higher monthly instalments might be linked to larger firms that are capable of handling larger loans or credit obligations. Some of the other financial metrics, as was also apparent from Fig. [10(a)](https://arxiv.org/html/2510.09407v1#S5.F10.sf1 "In Figure 10 ‣ 5.5 Interpretability of the architecture ‣ 5 Results ‣ A multimodal approach to SME credit scoring integrating transaction and ownership networks 1footnote 11footnote 1NOTICE: This is the author’s version of a work which will be submitted for publication. Changes resulting from the publishing process, such as editing, corrections, structural formatting, and other quality control mechanisms may not be reflected in this document. This work is made available under a Creative Commons BY-NC-ND license. ΓΔΞΛ"), appear to be less influential in the model.

## 6 Discussion

This study sought to address three key research questions: 1) whether incorporating explicit network data into predictive models improves their accuracy or provides a deeper understanding of how credit risk spreads among interconnected SMEs; and if this is the case, determine the optimal method for integrating network data with structured data; 2) whether multilayer networks offer advantages over single-layer networks; and if so, identify the type of connection that is more informative; and 3) whether additional insights can be gained by considering the directionality and intensity of these connections.

Our findings indeed indicate that the integration of network data with traditional structured data improves the performance of the model. The results suggest that the bimodal model employing a hybrid fusion strategy with a cross-attention approach is the most effective. The use of multilayer networks instead of single-layer networks is shown to be more informative and effective in capturing the complexities of borrower interactions and credit risk contagion, which is consistent with other recent studies in the credit risk area (Óskarsdóttir & Bravo, [2021](https://arxiv.org/html/2510.09407v1#bib.bib46); Zandi et al., [2025](https://arxiv.org/html/2510.09407v1#bib.bib65)). Furthermore, considering the directionality and intensity of these connections provides added insight into the propagation of risk, leading to more accurate predictions. This could be due to supply chain dependencies and financial contagion. In supply chains, upstream supplier distress can disrupt production and increase costs for downstream firms (Agca et al., [2022](https://arxiv.org/html/2510.09407v1#bib.bib1); Tabachová et al., [2024](https://arxiv.org/html/2510.09407v1#bib.bib56)). However, our results indicate that buyer-side defaults have an even greater impact on SMEs, as lost revenues and unpaid receivables may directly strain a firm’s liquidity. This aligns with evidence that firms with concentrated client bases (as is common for many SMEs) face higher debt costs and risk exposure (Dhaliwal et al., [2016](https://arxiv.org/html/2510.09407v1#bib.bib21)), and that their use of trade credit can amplify the transmission of financial shocks through supply chains (Agca et al., [2022](https://arxiv.org/html/2510.09407v1#bib.bib1)).

The findings of this research have significant societal implications, as improving financial inclusion can support the growth of SMEs and broader economic development (Boachie & Adu-Darko, [2024](https://arxiv.org/html/2510.09407v1#bib.bib10)). Even in advanced economies, obtaining credit remains a challenging task for many SMEs, especially for recently established firms without extensive financial histories (Lee et al., [2015](https://arxiv.org/html/2510.09407v1#bib.bib35)). Our approach allows financial institutions to assess credit risk more accurately, thus lowering lending costs and, in turn, enabling greater credit availability for SMEs. In emerging economies, where traditional financial records are often sparse, there are distinct opportunities to apply similar techniques. Many SMEs in these regions operate in environments where formal banking infrastructure is limited, yet engage in extensive interactions and are highly interdependent (Wang, [2016](https://arxiv.org/html/2510.09407v1#bib.bib61)). These interdependencies can be derived from various sources such as call detail records, mobile money services, social media activities, community contributions, or geolocation data, among others. Our approach would enable the use of such interaction data to provide an alternative means of credit assessment, thus facilitating access to finance for a broader range of businesses. As for the lender, the ability to model credit risk contagion within SME networks can improve the resilience of a lender’s portfolio (Anagnostou et al., [2018](https://arxiv.org/html/2510.09407v1#bib.bib4)). By identifying how financial distress propagates through observed inter-firm connections, financial institutions can better anticipate correlated defaults within their client base and adjust risk management strategies accordingly. While our dataset only captures the slice of the market observed by one lender, these insights can nonetheless inform portfolio-level decision making and contribute to more prudent credit allocation.

## 7 Conclusions

This study demonstrated the value of incorporating multilayer network data and advanced deep learning techniques in predicting SME default risk. By integrating network-based information with traditional structured data, we showed that predictive models can more effectively assess the default risk of SMEs. To evaluate our approach, we used a large dataset from a major financial institution, deriving both single- and double-layer networks from company ownership structures and individual inter-firm financial transactions observed by the lender. In so doing, we were able to capture explicit supply chain relations between firms. We experimented with unimodal and bimodal architectures, employing two types of GNN, and testing various fusion strategies for bimodal models. Our results showed that bimodal learning, particularly when applying a hybrid fusion strategy and cross-attention, enhances predictive accuracy and provides deeper insight into risk propagation. We observed that the network modality has a slightly greater influence on the fused representation than the tabular modality. The results also showed that multilayer networks are able to extract more information from the data, leading to more accurate risk assessments. We found that employing networks with directed and weighted edges further boosts predictive performance, confirming that the strength and intensity of inter-firm links affects credit risk propagation. Lastly, we showed how Shapley analysis can shed light on the relative importance of different features and how this ranking may change as a result of adding the network modality.

Future research could explore several avenues to build on these findings. First, expanding the scope of network data to include additional types of interactions such as social media connections or geographic proximity could provide a more holistic view of SME networks. Social media data, for example, could offer insights into potential inter-firm linkages — such as business partnerships, customer-supplier mentions, or co-membership in professional networks. Geographic proximity data could help model localised economic conditions and their impact on SMEs (Calabrese et al., [2019](https://arxiv.org/html/2510.09407v1#bib.bib17)). Second, advances in fusion techniques may further improve predictive performance, revealing more effective ways to integrate multimodal data. Lastly, applying the proposed methods in different contexts would test their robustness and adaptability. Lenders can use the framework to build models tailored to their own data, and testing across diverse scenarios would help ensure the methods’ reliability.

## Acknowledgements

The first author acknowledges the support of the Natural Sciences and Engineering Research Council (NSERC) of Canada through the Canada Graduate Scholarships – Doctoral (CGS D) program. The second and fifth authors acknowledge the support of the Economic and Social Research Council (ESRC) [grant number ES/P000673/1]. The fourth author acknowledges the support of the Icelandic Research Fund (IRF) [grant number 228511-051]. The last author acknowledges the support of the NSERC [discovery grant RGPIN-2020-07114]. This research was undertaken, in part, thanks to funding from the Canada Research Chairs program [CRC-2018-00082]. The authors acknowledge the use of the IRIDIS High Performance Computing Facility and associated support services at the University of Southampton in the completion of this work.

## References

* Agca et al. (2022)

  Agca, S., Babich, V., Birge, J. R., & Wu, J. (2022).
  Credit shock propagation along supply chains: Evidence from the CDS market.
  Management Science, 68, 6506–6538.
* Allen & Gale (2000)

  Allen, F., & Gale, D. (2000).
  Financial contagion.
  Journal of Political Economy, 108, 1–33.
* Altman (1968)

  Altman, E. I. (1968).
  Financial ratios, discriminant analysis and the prediction of corporate bankruptcy.
  The Journal of Finance, 23, 589–609.
* Anagnostou et al. (2018)

  Anagnostou, I., Sourabh, S., & Kandhai, D. (2018).
  Incorporating contagion in portfolio credit risk models using network theory.
  Complexity, 2018, 6076173.
* Bakhtiari et al. (2020)

  Bakhtiari, S., Breunig, R., Magnani, L., & Zhang, J. (2020).
  Financial constraints and small and medium enterprises: A review.
  Economic Record, 96, 506–523.
* Baltrušaitis et al. (2018)

  Baltrušaitis, T., Ahuja, C., & Morency, L.-P. (2018).
  Multimodal machine learning: A survey and taxonomy.
  IEEE Transactions on Pattern Analysis and Machine Intelligence, 41, 423–443.
* Barabási & Pósfai (2016)

  Barabási, A.-L., & Pósfai, M. (2016).
  Network science.
  Cambridge University Press.
* Beaver et al. (2019)

  Beaver, W. H., Cascino, S., Correia, M., & McNichols, M. F. (2019).
  Group affiliation and default prediction.
  Management Science, 65, 3559–3584.
* Berloco et al. (2021)

  Berloco, C., De Francisci Morales, G., Frassineti, D., Greco, G., Kumarasinghe, H., Lamieri, M., Massaro, E., Miola, A., & Yang, S. (2021).
  Predicting corporate credit risk: Network contagion via trade credit.
  PLoS One, 16, e0250115.
* Boachie & Adu-Darko (2024)

  Boachie, C., & Adu-Darko, E. (2024).
  The effect of financial inclusion on economic growth: The role of human capital development.
  Cogent Social Sciences, 10, 2346118.
* Borgatti & Halgin (2011)

  Borgatti, S. P., & Halgin, D. S. (2011).
  On network theory.
  Organization Science, 22, 1168–1181.
* Borisov et al. (2022)

  Borisov, V., Leemann, T., Seßler, K., Haug, J., Pawelczyk, M., & Kasneci, G. (2022).
  Deep neural networks and tabular data: A survey.
  IEEE Transactions on Neural Networks and Learning Systems, 35, 7499–7519.
* Boulahia et al. (2021)

  Boulahia, S. Y., Amamra, A., Madi, M. R., & Daikh, S. (2021).
  Early, intermediate and late fusion strategies for robust deep learning-based multimodal action recognition.
  Machine Vision and Applications, 32, 121.
* Bravo et al. (2013)

  Bravo, C., Maldonado, S., & Weber, R. (2013).
  Granting and managing loans for micro-entrepreneurs: New developments and practical experiences.
  European Journal of Operational Research, 227, 358–366.
* Bravo & Óskarsdóttir (2020)

  Bravo, C., & Óskarsdóttir, M. (2020).
  Evolution of credit risk using a personalized pagerank algorithm for multilayer networks.
  In KDD MLF 2020: KDD Workshop on Machine Learning in Finance.
* Breiman (2001)

  Breiman, L. (2001).
  Random forests.
  Machine Learning, 45, 5–32.
* Calabrese et al. (2019)

  Calabrese, R., Andreeva, G., & Ansell, J. (2019).
  “Birds of a feather” fail together: Exploring the nature of dependency in SME defaults.
  Risk Analysis, 39, 71–84.
* Chango et al. (2022)

  Chango, W., Lara, J. A., Cerezo, R., & Romero, C. (2022).
  A review on data fusion in multimodal learning analytics and educational data mining.
  Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 12, e1458.
* Chen & Guestrin (2016)

  Chen, T., & Guestrin, C. (2016).
  XGBoost: A scalable tree boosting system.
  In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785–794).
* De Bock et al. (2024)

  De Bock, K. W., Coussement, K., De Caigny, A., Slowiński, R., Baesens, B., Boute, R. N., Choi, T.-M., Delen, D., Kraus, M., Lessmann, S. et al. (2024).
  Explainable AI for operational research: A defining framework, methods, applications, and a research agenda.
  European Journal of Operational Research, 317, 249–272.
* Dhaliwal et al. (2016)

  Dhaliwal, D., Judd, J. S., Serfling, M., & Shaikh, S. (2016).
  Customer concentration risk and the cost of equity capital.
  Journal of Accounting and Economics, 61, 23–48.
* Elliott et al. (2019)

  Elliott, A., Cucuringu, M., Luaces, M. M., Reidy, P., & Reinert, G. (2019).
  Anomaly detection in networks with application to financial transaction networks.
  arXiv preprint arXiv:1901.00402, .
* Fenech et al. (2015)

  Fenech, J. P., Vosgha, H., & Shafik, S. (2015).
  Loan default correlation using an Archimedean copula approach: A case for recalibration.
  Economic Modelling, 47, 340–354.
* Giesecke & Weber (2004)

  Giesecke, K., & Weber, S. (2004).
  Cyclical correlations, credit contagion, and portfolio losses.
  Journal of Banking & Finance, 28, 3009–3036.
* Gneiting & Raftery (2007)

  Gneiting, T., & Raftery, A. E. (2007).
  Strictly proper scoring rules, prediction, and estimation.
  Journal of the American Statistical Association, 102, 359–378.
* Gunnarsson et al. (2021)

  Gunnarsson, B. R., Vanden Broucke, S., Baesens, B., Óskarsdóttir, M., & Lemahieu, W. (2021).
  Deep learning for credit scoring: Do or don’t?
  European Journal of Operational Research, 295, 292–305.
* Hosmer Jr. et al. (2013)

  Hosmer Jr., D. W., Lemeshow, S., & Sturdivant, R. X. (2013).
  Applied logistic regression.
  John Wiley & Sons.
* Huang & Yang (2024)

  Huang, C., & Yang, Y. (2024).
  Time series feature redundancy paradox: An empirical study based on mortgage default prediction.
  arXiv preprint arXiv:2501.00034, .
* Iori et al. (2008)

  Iori, G., De Masi, G., Precup, O. V., Gabbi, G., & Caldarelli, G. (2008).
  A network analysis of the Italian overnight money market.
  Journal of Economic Dynamics and Control, 32, 259–278.
* Jackson & Pernoud (2021)

  Jackson, M. O., & Pernoud, A. (2021).
  Systemic risk in financial networks: A survey.
  Annual Review of Economics, 13, 171–202.
* Kivelä et al. (2014)

  Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014).
  Multilayer networks.
  Journal of Complex Networks, 2, 203–271.
* Korangi et al. (2023)

  Korangi, K., Mues, C., & Bravo, C. (2023).
  A transformer-based model for default prediction in mid-cap corporate markets.
  European Journal of Operational Research, 308, 306–320.
* LeCun et al. (2015)

  LeCun, Y., Bengio, Y., & Hinton, G. (2015).
  Deep learning.
  Nature, 521, 436–444.
* Lee et al. (2018)

  Lee, K.-H., Chen, X., Hua, G., Hu, H., & He, X. (2018).
  Stacked cross attention for image-text matching.
  In Proceedings of the European Conference on Computer Vision (ECCV) (pp. 201–216).
* Lee et al. (2015)

  Lee, N., Sameen, H., & Cowling, M. (2015).
  Access to finance for innovative SMEs since the financial crisis.
  Research Policy, 44, 370–380.
* Letizia & Lillo (2019)

  Letizia, E., & Lillo, F. (2019).
  Corporate payments networks and credit risk rating.
  EPJ Data Science, 8, 21.
* Li et al. (2024)

  Li, Z., Shi, J., & van Leeuwen, M. (2024).
  Graph neural networks based log anomaly detection and explanation.
  arXiv preprint arXiv:2307.00527v3, .
* Long et al. (2022)

  Long, J., Jiang, C., Dimitrov, S., & Wang, Z. (2022).
  Clues from networks: Quantifying relational risk for credit risk evaluation of SMEs.
  Financial Innovation, 8, 91.
* Lopez & Saidenberg (2000)

  Lopez, J. A., & Saidenberg, M. R. (2000).
  Evaluating credit risk models.
  Journal of Banking & Finance, 24, 151–165.
* Lu et al. (2025)

  Lu, S., Zhang, X., Su, Y., Liu, X., & Yu, L. (2025).
  Efficient multimodal learning for corporate credit risk prediction with an extended deep belief network.
  Annals of Operations Research, (pp. 1–38).
* Lundberg & Lee (2017)

  Lundberg, S. M., & Lee, S.-I. (2017).
  A unified approach to interpreting model predictions.
  In Proceedings of the 31st International Conference on Neural Information Processing Systems (NIPS’17) (pp. 4768––4777).
* Luo & Kay (1988)

  Luo, R. C., & Kay, M. G. (1988).
  Multisensor integration and fusion: Issues and approaches.
  In Sensor Fusion (pp. 42–49).
  volume 931.
* Mai et al. (2019)

  Mai, F., Tian, S., Lee, C., & Ma, L. (2019).
  Deep learning models for bankruptcy prediction using textual disclosures.
  European Journal of Operational Research, 274, 743–758.
* Massa & Žaldokas (2017)

  Massa, M., & Žaldokas, A. (2017).
  Information transfers among co-owned firms.
  Journal of Financial Intermediation, 31, 77–92.
* Nagpal & Bahar (2001)

  Nagpal, K., & Bahar, R. (2001).
  Measuring default correlation.
  Risk, 14, 129–132.
* Óskarsdóttir & Bravo (2021)

  Óskarsdóttir, M., & Bravo, C. (2021).
  Multilayer network analysis for improved credit risk prediction.
  Omega, 105, 102520.
* Óskarsdóttir et al. (2019)

  Óskarsdóttir, M., Bravo, C., Sarraute, C., Vanthienen, J., & Baesens, B. (2019).
  The value of big data for credit scoring: Enhancing financial inclusion using mobile phone data and social network analytics.
  Applied Soft Computing, 74, 26–39.
* Poria et al. (2017)

  Poria, S., Cambria, E., Bajpai, R., & Hussain, A. (2017).
  A review of affective computing: From unimodal analysis to multimodal fusion.
  Information Fusion, 37, 98–125.
* Ramachandram & Taylor (2017)

  Ramachandram, D., & Taylor, G. W. (2017).
  Deep multimodal learning: A survey on recent advances and trends.
  IEEE Signal Processing Magazine, 34, 96–108.
* Rao et al. (2023)

  Rao, P. K., Chatterjee, S., Nagaraju, K., Khan, S. B., Almusharraf, A., & Alharbi, A. I. (2023).
  Fusion of graph and tabular deep learning models for predicting chronic kidney disease.
  Diagnostics, 13, 1981.
* Rishehchi Fayyaz et al. (2021)

  Rishehchi Fayyaz, M., Rasouli, M. R., & Amiri, B. (2021).
  A data-driven and network-aware approach for credit risk prediction in supply chain finance.
  Industrial Management & Data Systems, 121, 785–808.
* Saxena et al. (2021)

  Saxena, A., Pei, Y., Veldsink, J., van Ipenburg, W., Fletcher, G., & Pechenizkiy, M. (2021).
  The banking transactions dataset and its comparative analysis with scale-free networks.
  In Proceedings of the 2021 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (pp. 283–296).
* Smit & Watkins (2012)

  Smit, Y., & Watkins, J. A. (2012).
  A literature review of small and medium enterprises (SME) risk management practices in South Africa.
  African Journal of Business Management, 6, 6324–6330.
* Spatareanu et al. (2023)

  Spatareanu, M., Manole, V., Kabiri, A., & Roland, I. (2023).
  Bank default risk propagation along supply chains: Evidence from the UK.
  International Review of Economics & Finance, 84, 813–831.
* Stevenson et al. (2021)

  Stevenson, M., Mues, C., & Bravo, C. (2021).
  The value of text for small business default prediction: A deep learning approach.
  European Journal of Operational Research, 295, 758–771.
* Tabachová et al. (2024)

  Tabachová, Z., Diem, C., Borsos, A., Burger, C., & Thurner, S. (2024).
  Estimating the impact of supply chain network contagion on financial stability.
  Journal of Financial Stability, 75, 101336.
* Tavakoli et al. (2025)

  Tavakoli, M., Chandra, R., Tian, F., & Bravo, C. (2025).
  Multi-modal deep learning for credit rating prediction using text and numerical data streams.
  Applied Soft Computing, 171, 112771.
* Thomas et al. (2017)

  Thomas, L., Crook, J., & Edelman, D. (2017).
  Credit scoring and its applications.
  SIAM-Society for Industrial and Applied Mathematics.
* Veličković et al. (2018)

  Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., & Bengio, Y. (2018).
  Graph attention networks.
  In 6th International Conference on Learning Representations (ICLR).
* Vinciotti et al. (2019)

  Vinciotti, V., Tosetti, E., Moscone, F., & Lycett, M. (2019).
  The effect of interfirm financial transactions on the credit risk of small and medium-sized enterprises.
  Journal of the Royal Statistical Society Series A: Statistics in Society, 182, 1205–1226.
* Wang (2016)

  Wang, Y. (2016).
  What are the biggest obstacles to growth of SMEs in developing countries? – An empirical evidence from an enterprise survey.
  Borsa Istanbul Review, 16, 167–176.
* Weisfeiler & Lehman (1968)

  Weisfeiler, B., & Lehman, A. A. (1968).
  A reduction of a graph to a canonical form and an algebra arising during this reduction.
  Nauchno-Technicheskaya Informatsia, 2, 12–16.
  English translation by G. Ryabov available at <https://www.iti.zcu.cz/wl2018/pdf/wl_paper_translation.pdf>.
* Xu et al. (2019)

  Xu, K., Hu, W., Leskovec, J., & Jegelka, S. (2019).
  How powerful are graph neural networks?
  In 7th International Conference on Learning Representations (ICLR).
* Yin et al. (2020)

  Yin, C., Jiang, C., Jain, H. K., & Wang, Z. (2020).
  Evaluating the credit risk of SMEs using legal judgments.
  Decision Support Systems, 136, 113364.
* Zandi et al. (2025)

  Zandi, S., Korangi, K., Óskarsdóttir, M., Mues, C., & Bravo, C. (2025).
  Attention-based dynamic multilayer graph neural networks for loan default prediction.
  European Journal of Operational Research, 321, 586–599.
* Zhang et al. (2020a)

  Zhang, C., Yang, Z., He, X., & Deng, L. (2020a).
  Multimodal intelligence: Representation learning, information fusion, and applications.
  IEEE Journal of Selected Topics in Signal Processing, 14, 478–493.
* Zhang et al. (2020b)

  Zhang, D., Yin, C., Zeng, J., Yuan, X., & Zhang, P. (2020b).
  Combining structured and unstructured data for predictive models: A deep learning approach.
  BMC Medical Informatics and Decision Making, 20, 1–11.
* Zhang et al. (2018)

  Zhang, L., Xie, Y., Xidao, L., & Zhang, X. (2018).
  Multi-source heterogeneous data fusion.
  In 2018 International Conference on Artificial Intelligence and Big Data (ICAIBD) (pp. 47–51).
* Zhang et al. (2022)

  Zhang, W., Yan, S., Li, J., Tian, X., & Yoshida, T. (2022).
  Credit risk prediction of SMEs in supply chain finance by fusing demographic and behavioral data.
  Transportation Research Part E: Logistics and Transportation Review, 158, 102611.
* Zhao et al. (2024)

  Zhao, F., Zhang, C., & Geng, B. (2024).
  Deep multimodal data fusion.
  ACM Computing Surveys, 56.
* Zhou et al. (2022)

  Zhou, T., Lee, Y.-L., Li, Q., Chen, D., Xie, W., Wu, T., & Zeng, T. (2022).
  Identifying discreditable firms in a large-scale ownership network.
  arXiv preprint arXiv:2211.14316, .

## Appendix A Strategy for handling null values

Table A.1: Strategy for handling null values.

| Null value percentage | Feature type | Action |
| --- | --- | --- |
| 0% to <5%<5\% | Categorical | Replace with mode |
| Numerical | Replace with median |
| 5% to <40%<40\% | Categorical | Replace with ‘N/A’ |
| Numerical | Replace with median and add dummy variable indicating presence or absence |
| 40% to <95%<95\% | Categorical | Drop feature and add dummy variable indicating presence or absence |
| Numerical | Drop feature and add dummy variable indicating presence or absence |
| 95% to 100% | Categorical | Drop feature |
| Numerical | Drop feature |

## Appendix B Hyperparameter tuning for baseline models

Table B.1: Hyperparameter tuning for baseline models.

|  |  |  |
| --- | --- | --- |
| Model | Hyper-parameters | Grid search values |
| LR | Penalty | {L1, L2} |
| RF | Number of trees | {100, 200, 500} |
| Minimum samples leaf | {2, 5, 10} |
| Minimum samples split | {2, 5, 10} |
| XGB | Learning rate | {0.001, 0.01, 0.1} |
| Maximum depth | {2, 3, 4} |
| Number of estimators | {50, 100, 250, 500} |
| Alpha | {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9} |

## Appendix C Architecture of the DNN baseline model

![Refer to caption](x14.png)


Figure C.1: Architecture of the DNN baseline model.

## Appendix D Hyperparameter tuning for GAT and GIN models

Table D.1: Hyperparameter tuning for GAT and GIN models.

| Model | Hyper-parameters | Grid search values |
| --- | --- | --- |
| GAT | Number of layers | {1, 2} |
| Number of attention heads | {1, 2, 4} |
| Hidden units per head | {16, 32, 64} |
| Learning rate | {0.001, 0.005, 0.01} |
| Dropout rate | {0.0, 0.25, 0.5} |
| GIN | Number of layers | {1, 2} |
| Hidden units | {16, 32, 64} |
| Epsilon (ε\varepsilon) | {0, 0.2, 0.4} |
| Learning rate | {0.001, 0.005, 0.01} |
| Dropout rate | {0.0, 0.25, 0.5} |