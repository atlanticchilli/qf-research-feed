---
authors:
- Ilias Aarab
- Thomas Gottron
- Andrea Colombo
- Jörg Reddig
- Annalauro Ianiro
doc_id: arxiv:2602.10960v1
family_id: arxiv:2602.10960
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Integrating granular data into a multilayer network: an interbank model of
  the euro area for systemic risk assessment'
url_abs: http://arxiv.org/abs/2602.10960v1
url_html: https://arxiv.org/html/2602.10960v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ilias Aarab
Corresponding author: .
  
Thomas Gottron
  
Andrea Colombo
  
Jörg Reddig
  
Annalaura Ianiro

(24 September 2023)

###### Abstract

Micro-structural models of contagion and systemic risk emphasize that shock propagation is inherently multi-channel, spanning counterparty exposures, short-term funding and roll-over risk, securities cross-holdings, and common-asset (fire-sale) spillovers. Empirical implementations, however, often rely on stylized or simulated networks, or focus on a single exposure dimension, reflecting the practical difficulty of reconciling heterogeneous granular collections into a coherent representation with consistent identifiers and consolidation rules. We close part of this gap by constructing an empirically grounded multilayer network for euro area significant banking groups that integrates several supervisory and statistical datasets into layer-consistent exposure matrices defined on a common node set. Each layer corresponds to a distinct transmission channel, long- and short-term credit, securities cross-holdings, short-term secured funding, and overlapping external portfolios, and nodes are enriched with balance-sheet information to support model calibration. We document pronounced cross-layer heterogeneity in connectivity and centrality, and show that an aggregated (flattened) representation can mask economically relevant structure and misidentify the institutions that are systemically important in specific markets. We then illustrate how the resulting network disciplines standard systemic-risk analytics by implementing a centrality-based propagation measure and a micro-structural agent-based framework on real exposures. The approach provides a data-grounded basis for layer-aware systemic-risk assessment and stress testing across multiple dimensions of the banking network.

JEL: D8, H51

MSC: 05C90, 68T30

###### keywords:

granular data collections, multi-layer network, financial contagion, systemic risk, micro-structural models

## 1 Introduction

A large literature studies how shocks propagate through financial networks and how amplification mechanisms can turn idiosyncratic stress into systemic events [eisenberg2001systemic, boss2004network, montagna2016multi]. Micro-structural models emphasize that transmission is multi-channel: losses can spread through long-term counterparty exposures, roll-over risk in short-term funding markets, securities cross-holdings, and common-asset fire-sale spillovers [allen2000financial, elliott2014financial, cifuentes2005liquidity]. Yet empirical implementations frequently operate on a single exposure dimension or on stylized network structures, largely because real-world bilateral exposures are fragmented across data collections, reported under different definitions and frequencies, and difficult to reconcile across entity identifiers and consolidation regimes.

In the last decade, policy makers and supervisors have gained access to an expanding set of granular statistical and supervisory collections that, in principle, enable a more realistic measurement of interconnectedness and risk transmission. Prominent examples include AnaCredit, EMIR, SFTDS, MMSR, SHS, FINREP and COREP222AnaCredit (analytical credit datasets) contains detailed information on individual bank loans above €25,000 to legal entities in the euro area, harmonised across all Member States. EMIR data underlies derivatives contract data collected under the European Market Infrastructure Regulation (EMIR). SFTDS is based on the EU SFTR (Regulation (EU) 2015/2365) to collect securities financing transaction data. The money market statistical reporting (MMSR) dataset provides information on the (un)secured, foreign exchange swap and overnight index swap euro money market segments. FINREP and COREP are European projects of the Committee of European Banking Supervisors (CEBS): FINREP stands for Financial Reporting and is based on the International Financial Reporting Standards (IFRS); COREP stands for Common Reporting of the solvency ratio and is based on the Capital Requirements Directive (CRD).. A key challenge is to integrate these sources in a semantically consistent manner, including the alignment of identifiers, consolidation boundaries, instrument definitions, and reporting structures, and to map them into representations suitable for core analytical questions in macro- and micro-prudential surveillance.

A natural representation for such questions is a network (graph) in which nodes represent institutions (or groups under a given consolidation regime) and weighted directed edges represent exposures or claims. For many mechanisms, however, a single network is insufficient: different types of interactions (e.g., short- versus long-term credit, secured funding, or cross-holdings) encode distinct transmission channels and can exhibit markedly different topology [bargigli2015multiplex, battiston2014structural]. Aggregating these channels into a single layer can therefore mask economically relevant structure and potentially misidentify the institutions that are systemically important in a particular market. Conversely, populating a multilayer model with real exposures is demanding: it requires both substantive knowledge of the reporting frameworks to resolve inconsistencies and scalable tooling to process large volumes of granular records.

This paper contributes to closing the gap between the multi-channel contagion mechanisms emphasized in the theoretical literature and what can be evaluated empirically on real systems. We construct an empirically grounded multilayer network for euro area significant banking groups by integrating several granular supervisory and statistical collections into layer-consistent exposure matrices defined on a common node set. The resulting network supports layer-aware stress-testing and provides a realistic empirical basis for systemic-risk analytics that are often studied on simulated networks. We then illustrate the implications of this measurement approach by implementing leading propagation-based and micro-structural agent-based frameworks on the constructed layers.

In particular we make the following contributions:

* •

  Measurement: We construct a multilayer exposure network for euro area significant banking groups by integrating multiple granular supervisory and statistical collections into a harmonized, consolidation-consistent representation with a common node set. We document the mapping, preprocessing, and aggregation steps that reconcile heterogeneous reporting schemes and identifiers.
* •

  Structure: We provide evidence of pronounced cross-layer heterogeneity in connectivity and centrality and show that a flattened (aggregated) representation can conceal channel-specific structure that is relevant for propagation and systemic importance.
* •

  Implications for systemic-risk analytics: Using real exposures, we implement two widely used frameworks, a centrality-based propagation measure and a micro-structural agent-based model, to illustrate how layer-aware measurement changes the identification and magnitude of systemic impact across channels, and to compare empirical outcomes to theoretical mechanisms.

The rest of the paper is structured as follows: We review related work in Section [2](https://arxiv.org/html/2602.10960v1#S2 "2 Related work ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment").
In Section [3](https://arxiv.org/html/2602.10960v1#S3 "3 Data ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") we describe the data used and our data preparation and integration techniques.
Section [4](https://arxiv.org/html/2602.10960v1#S4 "4 Network modelling ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") details the construction of the multi-layer network, and
Section [5](https://arxiv.org/html/2602.10960v1#S5 "5 Topological diagnostics ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") provides compact topological diagnostics, with a more comprehensive treatment provided in [aarab2025topology].
The analytical methods we apply on the network are presented in Section [6](https://arxiv.org/html/2602.10960v1#S6 "6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment").
We conclude in Section [7](https://arxiv.org/html/2602.10960v1#S7 "7 Summary and conclusions ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment").

## 2 Related work

The banking-network perspective has become a central empirical and theoretical tool for studying systemic risk, particularly in the wake of the 2008 financial crisis, which highlighted the difficulty of understanding and predicting propagation mechanisms in an interwoven financial system [huser2015too]. A parallel development has been the gradual expansion of granular supervisory and statistical reporting, enabling more detailed measurement of interdependencies but also raising non-trivial integration challenges across heterogeneous data sources.

Related literature can be divided into three categories: (1) motivating work, arguing for the advantages of modelling financial markets as networks, (2) theoretical work, developing network models and dynamics to represent market behaviour and (3) empirical work, using different types of data to describe certain aspects of the network structures in the banking sector.

[allen2009networks] argue that network theory can help in understanding financial systems, interactions among agents, and associated economic phenomena.
[bandt2012systemic] consider the complex network of exposures among banks as one of the key features for determining systemic risk while [di2018survey] review network-based approaches as an analytical basis for systemic risk indicators.
Recent work focuses in particular on multi-layer networks [bargigli2015multiplex]. Multi-layer networks cater for different types of interrelation among banks and model them separately in distinct layers of the network, where each layer may exhibit a different topology [battiston2014structural].

Theoretical foundations of financial market network analytics address contagion chains caused by liquidity preference shocks [allen2000financial], cross-holdings [elliott2014financial], default cascades based on capitalisation and exposures in the network [nier2007network] or contagion effects based on shocks to asset values [glasserman2015likely]. Insights vary across models and assumptions.
A frequent conclusion is that highly connected nodes are often most exposed to spillover effects [glasserman2015likely].
[nier2007network] observe that the effect of connectivity on contagion can be non-linear: initial increases in connectivity foster contagion, but beyond a threshold additional connectivity may dampen cascades by improving risk sharing. [battiston2012liaisons] report similar non-linear behavior in networks of risk diversification.
[elliott2014financial] model cross-holdings and investigate how defaults can trigger further failures.
[glasserman2015likely] study contagion effects due to shocks to asset values, linking interconnectedness to expectations of losses and defaults.
[cifuentes2005liquidity] provide a model of fire sales using a network based on overlapping portfolios: distressed entities liquidate assets, depressing prices and transmitting valuation losses to other holders.
DebtRank [battiston2012debtrank] estimates the systemic importance of institutions based on balance-sheet buffers and network exposures, introducing domain-specific modifications of feedback centrality metrics to quantify distress propagation following exogenous shocks. The DebtRank value of a node corresponds to the additional distress in the system that is attributable to that node’s initial default or distress.

Empirical work on interbank networks is largely data-driven, ranging from descriptive characterizations of topology to applications of contagion models.
[boss2004network] analyze Austrian banks and document fat-tailed degree distributions, low clustering, and short average path lengths.
A recurring finding is a core–periphery structure, which often fits interbank data better than alternative generative mechanisms [van2014finding] such as preferential attachment [barabasi1999emergence].
Similar observations are reported for German banks using bilateral exposure data [craig2014interbank], with interpretations linked to specialization and non-random formation of relationships.
An analysis of large EU banks [alves2013structure] distinguishes between direct and indirect interconnections and studies temporal dynamics.

Empirical investigations of multi-layer networks capture different types of connections between banks. [bargigli2015multiplex] distinguish contracts by maturity and secured/unsecured nature in the Italian market and show that layers can have sharply different topology; moreover, a flattened representation may fail to capture key aspects of complexity.
[montagna2016multi] develop a micro-structural systemic-risk model on a multi-layer network combining short- and long-term loans with common exposures to financial assets, partially leveraging real-world data and filling gaps with simulated estimates.
[aldasoro2018multiplex] use anonymized exposures among 53 large European banks, broken down by maturity and instrument type, to characterize multi-layer network features using data collected by the European Systemic Risk Board, the European Banking Authority, and national supervisory authorities.

Our contribution is complementary to these strands: Much of the systemic-risk literature develops micro-structural contagion models on stylized balance sheets and simulated networks, or studies a single channel of interdependence in isolation. We contribute an empirically grounded alternative that integrates multiple granular collections into a semantically consistent, multi-layer interbank network capturing distinct market segments and exposure types. On this integrated network, we extend widely used systemic-risk and contagion frameworks to operate directly on observed exposures and balance-sheet information, providing a unified basis to study how propagation patterns differ by market segment and how they interact across layers.

## 3 Data

Granular datasets provide the foundation for creating our multi-layer networks. While Table [1](https://arxiv.org/html/2602.10960v1#S3.T1 "Table 1 ‣ 3 Data ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") gives an overview of the various datasets we explain in the following their specificities and the rational for using them in our analysis.

Table 1: Overview of granular datasets

|  |  |  |  |
| --- | --- | --- | --- |
| Dataset | Available from | Frequency | Coverage / instrument |
| AnaCredit | 2018–09 | Monthly | Loan-by-loan information |
| CSDB | 2009–04 | Monthly | Security-by-security information |
| SHSG | 2018–09 | Monthly | Security-by-security holdings |
| SFTDS | 2020–06 | Daily | Repurchase and buy-sell back transactions |
| RIAD | 1998–01 | Daily | Banking group structures and identifiers |
| ROSSI | 2019–01 | Monthly | List of significant institutions |
| COREP | 2017–06 | Semiannual | Capital information |
| FINREP | 2016–09 | Quarterly | Financial information |

Register of Institutions and Affiliates Data (RIAD): RIAD is the shared master dataset serving several European System of Central Banks (ESCB) and Single Supervisory Mechanism (SSM) business processes and statistical data collections. The RIAD data model includes more than 100 properties for legal entities, including a wide range of entity identifiers and relationships (e.g. foreign branches and subsidiaries).
In our application, RIAD serves to identify entities across different datasets and as a source for constructing banking groups.

List of significant banking groups (ROSSI list):
Almost all available granular datasets comprise information on the largest banking groups in the EA and participating member states which are directly supervised by the SSM.
Hence, we use ROSSI to determine the sample of banking groups to be included in our multi-layer network.
As of 1st of June 2021, this list of significant institutions comprised a total of 114 banking groups.
From ROSSI, we extract the RIAD codes of significant institutions, considering the prudential consolidation regime. This regime widens the group structure view as it also considers cases where the consolidating entity might be different than a bank (e.g. a financial holding) and improves consistency in the aggregation of granular datasets.

CSDB and SHSG data: The Centralised Securities Database (CSDB) is a reference database for all securities relevant for statistical purposes of the ESCB. It comprises information on debt securities, equity instruments and investment fund shares stored on a security-by-security basis. Each instrument is identifiable by its International Securities Identification Number. For each security, a large set of attributes is available.
While CSDB covers the issuance of securities by banking groups, the Securities Holdings Statistics Database by Group (SHSG) dataset contains the holdings of securities by banks. Thus, we also observe which banking groups hold issued securities, inside and outside the euro area.

AnaCredit data: The AnaCredit dataset [israel2017analytical]
contains loan-by-loan information collected from euro area banks extended to corporations. These data are reported at monthly frequency and are available as of September 2018. Among others, information on the outstanding amount, maturity, interest rate, collateral/guarantee, and on involved counterparties are collected for each individual loan. This makes AnaCredit a rich dataset for a wide range of analytical purposes.

SFT – Securities Financing Transactions data: The Securities Financing Transactions Data Store (SFTDS) collects and processes data reported under the Securities Financing Transactions Regulation (EU) 2015/2365333Regulation (EU) No. 2015/2365 on transparency of securities financing transactions and of reuse and amending Regulation (EU) No. 648/2012 Securities Financing Transactions Regulation – SFTR)..
SFTs and the scope of the SFTR include444Article 3 (11) SFTR:
(a) repurchase/ reverse repurchase transactions, (b) buy-sell back or sell-buy back transactions, (c) securities or commodities lending and securities or commodities borrowing and (d) margin lending transactions.

FINREP/COREP: FINREP (Financial Reporting Standards) and COREP (Common Reporting Standards) are the two reporting frameworks developed as part of the implementation of Basel III in Europe555EBA’s Implementing Technical Standards (ITS) amending the European Commission’s Implementing Regulation (EU) No 680/2014 on supervisory reporting of institutions under Regulation (EU) No 575/2013. which gives the European Banking Authority a mandate to request both capital and financial information.
COREP specifies the framework related to capital information, while FINREP specifies the financial information.
Banks subject to International Financial Reporting Standards (IFRS) already use FINREP templates to submit financial information in a harmonised format at consolidated level. This requirement has also been extended to SSM banks reporting at sub-consolidated or solo level under IFRS and national Generally Accepted Accounting Principles (GAAPs)666Regulation (EU) 2015/534 of the ECB of 17 March 2015. FINREP templates are subject to quarterly mandatory reporting.
COREP is used to collect Pillar 1 data and information on liquidity, leverage and large exposures from banks in a harmonised format.

## 4 Network modelling

This section provides details on how we construct our multi-layer network based on the various datasets. Figure [1](https://arxiv.org/html/2602.10960v1#S4.F1 "Figure 1 ‣ 4 Network modelling ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") provides a bird eye view of the modelling process.777Note that the analysis we conduct focuses on a static snapshot of the multi-layer network. The considered snapshot is the end-of-month observation of the network as of June 2021. This is a date in which all datasets, considering their respective frequencies, are available.

![Refer to caption](x1.png)


Figure 1: 1. Using ROSSI, RIAD and COREP data a list of banking groups, including their group structure is constructed. 2. A multitude of granular datasets are integrated with banking groups. 3. A multi-layer network is constructed, with nodes depicting banking groups, layers depicting financial markets and edges representing financial relationships between nodes. 4. Further enrichment of the nodes is carried out to represent nodes by their balance sheet.

### 4.1 Identification and modelling of banking groups

The first step in modelling a multi-layer network is to define the nodes nin\_{i} of the network. As our focus is to measure exposures between banking groups across different markets, we model banking groups as nodes. The construction of banking groups is initiated from the head of a banking group. The list of group heads of significant888The definition of Significant Institutions can be found in Regulation (EU) No 468/2014 of the European Central Bank of 16 April 2014. banks in the EA is retrieved from ROSSI.
Once the group head has been identified, all entities belonging to that group need to be identified.
We consider all subsidiaries as being part of the group over which the group head exercises direct or indirect control, based on equity share999In addition, supervised entities according to Guideline (EU) 2020/497 of the ECB are also included in the group, if not already included following the control relationship criteria..
To obtain a complete group structure, including subsidiaries that are not credit or financial institutions, we leverage and integrate different group information available in ROSSI, COREP and RIAD.

### 4.2 Granular data integration

After the identification of banking groups and their subsidiaries, we integrate the different granular datasets to form layer-specific exposures. Consistent identification of group entities is realized using entity identifiers available in RIAD. During the integration process we harmonize and align different structures and semantics of the datasets (e.g., stock-based versus transactional reporting).
Having information on the banking group structure allows us to aggregate subsidiary-level records to the group-head level and to identify interrelations across all granular datasets101010To efficiently process the large amount of data we make use of a Hadoop based data lake to store the data and utilize Spark for distributed processing [aarab2022analysis]..

### 4.3 Construction of a multi-layer network

We follow [battiston2014structural] and define a multi-layer network as *a network where each node appears in a set of different layers ll, and each layer describes all the edges of a given type*. This entails that the layers share the same node set. In our case, edges ei​jle\_{ij}^{l} from node nin\_{i} to node njn\_{j} are directed and their weight indicates the aggregated exposure of banking group ii towards jj within layer ll111111Note that intra-group exposures of banking groups are removed to avoid self-loops within the network.. The edge values differ across layers ll based on the type of exposure they represent:

Long-term credit layer: This layer contains loan exposures between banking groups having an initial maturity of at least three months, in line with [montagna2016multi]. Exposures are aggregated over different types of loan instruments (e.g., deposits, credit lines, convenience credit, etc.), with the bulk (more than 90%) of exposures coming from deposits, credit lines other than revolving credit and unspecified loans. Edge weights wi​jltcw\_{ij}^{\textit{ltc}} indicate the outstanding nominal values.

Short-term credit layer: This layer contains loan exposures with an initial maturity shorter than three months. Exposures are processed in the same way as for the long-term credit layer, with the additional constraint of ensuring strictly positive maturities of the loans. We observe that a large part of instruments (more than 45%) are reverse repurchase agreements, confirming the short-term nature of the layer. Edge weights wi​jstcw\_{ij}^{\textit{stc}} indicate the outstanding nominal values.

Cross-securities layer: This layer contains equity and debt holdings between banking groups. An edge from node nin\_{i} to node njn\_{j} represents the market value of the securities issued by njn\_{j} and held by nin\_{i}. We do not distinguish between equity and debt securities and aggregate them into the same edge. The edge weight wi​jcsw\_{ij}^{\textit{cs}} represents the market value of investments made by nin\_{i} into njn\_{j}’s issued securities.

Short-term funding layer: The short-term funding layer contains repurchase agreements and buy-sell back transactions obtained from the SFT dataset. Within this layer the edge weight wi​jstfw\_{ij}^{\textit{stf}} from node nin\_{i} to njn\_{j} represents the aggregated open funding transactions between banking group nin\_{i} and njn\_{j}. The edge ei​jstfe\_{ij}^{\textit{stf}} is directed from the collateral taker nin\_{i} to the collateral giver njn\_{j}. To align with the end-of-month snapshot used across layers, we extract transactions that are indicated as active at the end of the month.

External securities layer:
The external securities layer models investments by banking groups in securities issued by entities outside the interbank market. A natural representation is a bipartite network with two disjoint node sets: banking groups and external securities. Directed edges from a banking group to a security encode the market value of the corresponding holding. In our application, however, the primary interest is in the extent to which this layer can generate fire-sale spillovers. Specifically, when a banking group ii liquidates a substantial fraction of its securities portfolio, we ask how this may affect the balance sheets of other banking groups through common-asset holdings. To capture this mechanism parsimoniously while preserving a common vertex set across layers, we use the projected representation on the banking-group node set NN: we construct an undirected graph in which an edge between banking groups ii and jj represents the market value of overlap in their portfolios.

For example, suppose banking group ii holds 55 shares of security s1s\_{1} and banking group jj holds 33 shares of s1s\_{1}, where the market price of s1s\_{1} is € 100, and the two groups hold no other common securities. Then the edge weight between ii and jj equals the market value of the overlapping position, i.e.,

|  |  |  |
| --- | --- | --- |
|  | wi​j=min⁡(5,3)×100= 300.w\_{ij}\;=\;\min(5,3)\times 100\;=\;300\,. |  |

Under this construction, the impact of a sell-off by ii can be traced by following edges that are directly or indirectly connected to ii: banking groups linked to ii are more likely to experience balance-sheet deterioration when ii liquidates large positions in overlapping securities. To limit the universe of securities, we aggregate holdings at the issuer level, which also has the advantage of implicitly accounting for positive correlations among securities issued by the same issuer. Data are derived mainly from SHSG and mapped to banking groups through RIAD and ROSSI.

Flattened network layer:
The flattened network layer is an artificially constructed layer, in the sense that it does not correspond to a specific real-world market. Instead, it is defined as the sum of all layers in the multi-layer network, where summation corresponds to edge-wise aggregation. If an edge from banking group ii to jj appears in multiple layers, its weights are added; if an edge appears in one layer but not another, it is carried over unchanged. The same logic extends to the aggregation of more than two layers. Care is required when adding undirected layers (in our case, the external securities layer). To obtain a meaningful aggregated *directed* layer, we first convert each undirected edge into a pair of symmetric directed edges (i.e., we construct a directed graph in which, for every edge, the reverse edge is also present) before summing it with the other layers. This ensures that the network effects induced by this layer are represented in the flattened network (i.e., price deterioration can propagate in either direction between two connected banking groups). At the same time, edge weights in the flattened network lose a direct economic interpretation because aggregation can introduce double counting (e.g., the total weight in the flattened network double counts the market value of overlapping portfolios). The flattened network provides a useful benchmark to compare layer-specific structures with the system as a whole and to assess the contribution of each layer to aggregate network connectivity. By construction, it draws on all datasets described above.

### 4.4 Enrichment of the nodes

After constructing the multi-layer network, we enrich nodes with key balance-sheet items (e.g., Tier 1 capital and total assets) to support calibration and interpretation of systemic-risk measures. Total assets are retrieved from FINREP121212Total assets are available in FINREP template: F 01.01 - Balance Sheet Statement. and Tier 1 capital from COREP131313Tier 1 Capital is available in the COREP template: C47.00 – Leverage ratio calculation. The amount of Tier 1 capital is calculated according to article 25 of the CRR, without taking into account the derogation laid down in Chapters 1 and 2 of Title I of Part Ten of the CRR.. These values are available at consolidated level, enabling a straightforward mapping to banking groups via RIAD identifiers. The enriched nodes allow a more economically interpretable analysis of propagation and systemic impact across layers.

## 5 Topological diagnostics

A comprehensive topological characterization of the constructed multi-layer interbank network
(e.g., layer-specific global metrics, tail behavior, and cross-layer comparisons) is provided in
[aarab2025topology]. In this paper, we report two compact diagnostics that (i) validate that
the constructed layers exhibit the pronounced heterogeneity commonly documented for interbank networks,
and (ii) motivate conducting the financial applications in Section [6](https://arxiv.org/html/2602.10960v1#S6 "6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") in a layer-aware
manner rather than relying solely on an aggregated representation.

### 5.1 Degree heterogeneity across layers

Figure [2](https://arxiv.org/html/2602.10960v1#S5.F2 "Figure 2 ‣ 5.1 Degree heterogeneity across layers ‣ 5 Topological diagnostics ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") compares empirical in- and out-degree distributions across layers.
Two patterns are particularly relevant for the subsequent systemic-risk analytics.
First, within each layer, the in- and out-degree distributions are closely aligned, indicating a broadly balanced system
with both active creditors and debtors.
Second, the degree distributions differ markedly across layers, indicating that the same set of banking groups
is embedded in market segments with substantially different connectivity profiles.
In line with prior empirical evidence on interbank networks, the credit and funding layers display pronounced right-skewness
and fat tails that are visually compatible with scale-free-type heterogeneity [boss2004network, craig2014interbank, van2014finding], whereas the cross-securities layer appears
substantially flatter (closer to a uniform shape), and the external-securities layer exhibits a distinct left-skewed fat-tailed
structure (with a median centred around roughly 76 edges, consistent with its largest connected subcomponent).
Third, the aggregated (flattened) representation can mask this layer-specific heterogeneity: depending on how
layers are combined, the resulting degree shape may be dominated by the most populated layer.
In our data, the flattened layer aligns most closely with the degree distribution of the cross-securities layer,
despite being a composite of credit and funding markets as well.
This observation supports a key modelling choice of our application section: contagion and systemic impact are evaluated
on the relevant layers (or controlled combinations of layers), rather than relying on a single aggregate network as a proxy
for all market mechanisms.

![Refer to caption](x2.png)


Figure 2: Empirical degree distributions across layers (June 2021 snapshot).
Left panel: in-degree distributions; right panel: out-degree distributions (x-axes depict the number of edges).
Layers are color-coded: short-term credit (dark blue), long-term credit (yellow), cross-securities (red),
short-term funding / repo market (light green), external securities (light blue, dubbed overlapping portfolio), and the flattened (aggregated) layer (dark green).
Density estimates are obtained via a Gaussian kernel density estimator with bandwidth selected according to Scott’s rule [scott1992multivariate].

### 5.2 Centrality and core–periphery structure

Figure [3](https://arxiv.org/html/2602.10960v1#S5.F3 "Figure 3 ‣ 5.2 Centrality and core–periphery structure ‣ 5 Topological diagnostics ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") reports distributions of standard centrality measures across layers.
While most institutions concentrate at low centrality values, the distributions also indicate that a comparatively small subset
of nodes occupies structurally important positions (e.g., short-path accessibility and intermediation roles).
Across layers, PageRank [page1999pagerank] and betweenness centralities concentrate near small values (with most mass between 0–5% and maxima barely exceeding
the 10% mark), suggesting that only a limited subset of institutions can strongly intermediate or steer propagation paths.
In contrast, closeness centrality exhibits a bimodal structure for most layers, with one mode near zero and a second mode typically between
25–75% depending on the layer.
This pattern is consistent with a core–periphery organization: a relatively small and well-connected core coexists with a large periphery that is weakly embedded.
For the financial applications in Section [6](https://arxiv.org/html/2602.10960v1#S6 "6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment"), this provides a structural rationale for two recurring themes:
(i) systemic impact is driven not only by balance-sheet size but also by network position, and (ii) propagation dynamics can be
sensitive to shocks affecting core institutions even when average connectivity appears moderate.141414In- and out-degree centralities are not shown, as their distributions closely mirror the in- and out-degree patterns in Figure [2](https://arxiv.org/html/2602.10960v1#S5.F2 "Figure 2 ‣ 5.1 Degree heterogeneity across layers ‣ 5 Topological diagnostics ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment").

![Refer to caption](x3.png)


Figure 3: Centrality distributions across layers (June 2021 snapshot).
Rows depict (normalized) centrality measures: PageRank CP​R​(i)C^{PR}(i), betweenness Cb​(i)C^{b}(i), and closeness Cc​(i)C^{c}(i).
Columns represent layers; x-axes depict centrality values normalized to [0,1][0,1].
Layers are color-coded: short-term credit (dark blue), long-term credit (yellow), cross-securities (red),
short-term funding / repo market (light green), external securities (light blue), and the flattened (aggregated) layer (dark green).
The black vertical dashed line in each subplot denotes the median for the corresponding layer–measure pair.
Density estimates are obtained via a Gaussian kernel density estimator with bandwidth selected according to Scott’s rule [scott1992multivariate].

## 6 Layer-aware systemic-risk assessment

We use the constructed multilayer network to address financial-stability questions for euro area banks. Our aim is not to propose a new contagion channel, but to move beyond single-layer or stylised calibrations by extending leading network-based frameworks to a setting in which exposures are empirically observed across multiple market dimensions and can be analysed in a layer-consistent way. This provides an empirical basis to evaluate how systemic impact and propagation patterns depend on the market segment through which stress travels, and how conclusions can change when the same institutions are embedded in different layers. Building on the literature’s shock-based analytics for systemic risk, we focus on two widely used but complementary approaches: a propagation-based systemic-importance measure and a micro-structural agent-based framework.

### 6.1 Notational preliminaries

Throughout this section we utilize a number of definitions and notational
conventions derived from Linear Algebra and Graph Theory. The
conventions are standard and utilized commonly in financial literature
as well. However, as we deal with multiple graphs, multiple variables,
and different dimensions, we collect these definitions together in this
section to make referencing throughout the paper easy.

Let Ω:=(N,G)\Omega:=(N,\ G) denote a multi-layer network where NN is a
set of nodes with cardinality |N|:=n=114\lvert N\rvert:=n=114, equal
to the number of Significant Institutions in our network. GG denotes
a set of graphs making up the different layers of the network. The
cardinality of |G|:=L\lvert G\rvert:=L, represents the number of
layers in the network. A graph, glg\_{l}, related to a layer
l∈Gl\in G can typically be represented by the tuple (N,Wl)(N,\ W\_{l}),
with Wl∈ℝN×NW\_{l}\in\mathbb{R}^{N\times N} an adjacency matrix
representing the directed and weighted edges in the layer. Elements of
WlW\_{l}, wijlw\_{\text{ij}}^{l} with i,j∈1,…,ni,j\in 1,\ \ldots,\ n,
represent the weight of the edge coming from node nin\_{i} towards node
njn\_{j}. wijlw\_{\text{ij}}^{l}= 0 signifies that no edge is present that
goes from nin\_{i} to njn\_{j} within layer ll. If not explicitly mentioned
otherwise, the direction of an edge in a graph follows the flow
of funds. That is wijlw\_{\text{ij}}^{l} represents a notion of the
exposure of nin\_{i} towards njn\_{j}, with the exact definition depending on
the layer we are considering.

For the external securities channel, we distinguish between (i) the security-level representation used to model fire-sale price dynamics and (ii) the projected network-layer representation used in the multi-layer graph Ω\Omega. In the security-level representation, we work with a securities universe MM of cardinality mm and a holding matrix S∈ℝn×mS\in\mathbb{R}^{n\times m}, where si​μs\_{i\mu} denotes the amount of security μ∈M\mu\in M held by banking group ni∈Nn\_{i}\in N. In the multi-layer network Ω\Omega, the external securities layer itself is represented on the common node set NN via the projected overlap graph (an undirected layer), where edge weights capture the market value of overlap in portfolio holdings. Note that for all graphs in GG we have
that the set of nodes is defined by the same set NN, underlying one
of the key features of a multi-layered network. The multi-layer network
is thus composed of a set of layers representing financial markets which
in turn are mathematically represented as graphs.

Every node in the network is characterised by an internal structure
given by its (consolidated) balance sheet. Balance sheet items of the
nodes are typically represented within an nn-dimensional Euclidean
vector space ℝn\mathbb{R}^{n} with elements of the vector depicting
the balance sheet item value for the different nodes in the system
(e.g., for equity we have the vector E​q∈ℝnEq\in\mathbb{R}^{n} with
e​qieq\_{i} the equity value of node nin\_{i}). Similarly
state vectors representing the state of a node within the network at any
given time are represented as [a,b]n\left[a,\ b\right]^{n}
with aa and bb respectively the lower- and upper bound levels that
the vector contains. Binary state vectors are depicted as
{0,1}n\left\{0,1\right\}^{n}. A vector of ones is depicted as
𝟏𝐧∈ℝn\mathbf{1}\_{\mathbf{n}}\in\mathbb{R}^{n}. The transpose of a
matrix or vector VV is given by VTV^{T}, with the transpose of a
vector indicating a column vector.

The matrix multiplication is not defined by an explicit operator but can
be inferred by the juxtaposition position of two matrices/vectors
without any intermediary operation symbol, e.g., the matrix
multiplication between AA and BB is represented by AB.
The elementwise Hadamard product is defined as A⋅BA\cdot B, with
broadcasting of vectors inferred from the dimensions of matrices being
multiplied with the vector. The Hadamard product between a matrix and a
row vector will be broadcasted row-wise, whereas for a column vector
broadcasting is done column-wise. The min​{}/m​a​x​{}\min{\{\}}/max\{\} operators
are always defined element wise,

|  |  |  |
| --- | --- | --- |
|  | min⁡{A∈ℝn,B∈ℝn}:=(min⁡{a1,b1},…,min⁡{an,bn})∈ℝn\displaystyle\min\left\{A\in\mathbb{R}^{n},\ B\in\mathbb{R}^{n}\right\}:=\left(\min\left\{a\_{1},\ b\_{1}\right\},\ \ldots,\min\left\{a\_{n},\ b\_{n}\right\}\right)\in\mathbb{R}^{n} |  |
|  |  |  |
| --- | --- | --- |
|  | max⁡{A∈ℝn,B∈ℝn}:=(max⁡{a1,b1},…,max⁡{an,bn})∈ℝn\displaystyle\max\left\{A\in\mathbb{R}^{n},\ B\in\mathbb{R}^{n}\right\}:=\left(\max\left\{a\_{1},\ b\_{1}\right\},\ \ldots,\max\left\{a\_{n},\ b\_{n}\right\}\right)\in\mathbb{R}^{n} |  |

### 6.2 Propagation-based systemic importance

We apply the original DebtRank [battiston2012debtrank] algorithm to the multilayer network in two distinct calibrations: (a) a counterparty-loss channel, capturing credit risk, and (b) a liquidity-shortfall channel, capturing roll-over and funding risk. The objective is to quantify how a bank’s distress can propagate through a given layer and to compare systemic impact across channels.

The credit-risk calibration is based on a vector E​q∈ℝnEq\in\mathbb{R}^{n} of banks’ capital buffers to absorb shocks151515To construct E​qEq we make use of the Tier 1 capital information of banks, as proposed by [battiston2012debtrank]..
The exposures of banking group nin\_{i} towards its interbank debtors relative to its capital buffer e​qieq\_{i} is described by wi​jeq,l1=min⁡(1,wi​jl1eqi)w\_{ij}^{\textit{eq},l\_{1}}=\min\left(1,\frac{w\_{ij}^{l\_{1}}}{\textit{eq}\_{i}}\right) for l1∈{ltc,cs}l\_{1}\in\{\textit{ltc},\textit{cs}\}, i.e., the long-term credit market and the cross-securities market.
The edge weight wi​jeq,l1w\_{ij}^{\textit{eq},l\_{1}} represents the potential loss that banking group nin\_{i} can suffer when banking group njn\_{j} defaults (assuming no recovery of debt is possible in the short run) as a fraction of its capital buffer. Note that if a potential loss from the exposures of banking group nin\_{i} exceeds its capital buffer, then wi​jeq,l1=1w\_{ij}^{\textit{eq},l\_{1}}=1, representing the maximum loss that nin\_{i} can experience.
We simulate distress propagation within the long-term credit and cross-securities layers by applying the DebtRank recursion.

Similarly, the liquidity-shortfall calibration uses a vector L​i​q∈ℝnLiq\in\mathbb{R}^{n} of banks’ liquidity buffers to absorb shocks.
For the liquidity buffers we use the cash (asset) and deposits (liabilities) positions of a banking group nin\_{i} to define its buffer liqi=Cashi−β⋅Depositsi\textit{liq}\_{i}=\textit{Cash}\_{i}-\beta\cdot\textit{Deposits}\_{i}, where the parameter β∈[0,1]\beta\in[0,1] is a liquidity buffer scaler.
In our experiments we set β\beta to 0.05, 0.1 and 0.2 to examine different possible scenarios [montagna2016multi, brandi2018epidemics].
In this way we investigate the Liquidity Coverage Ratio of a banking group under different stressed circumstances, with higher β\beta values indicating a higher net cash outflow. The exposure is defined by wi​jliq,l2=min⁡(1,wj​il2liqi)w\_{ij}^{\textit{liq},l\_{2}}=\min\left(1,\frac{w\_{ji}^{l\_{2}}}{\textit{liq}\_{i}}\right) for l2∈{stc,stf}l\_{2}\in\{\textit{stc},\textit{stf}\}, i.e., the short-term credit and the short-term funding market.
wi​jliq,l2w\_{ij}^{\textit{liq},l\_{2}} represents the potential liquidity shortfall that banking group nin\_{i} can suffer when banking group njn\_{j} defaults as a fraction of its liquidity buffer. Again, if a potential liquidity shortfall exceeds the liquidity buffer, then wi​jliq,l2=1w\_{ij}^{\textit{liq},l\_{2}}=1, representing maximum depletion.

Next, we have a state vector
H∈[0,1]nH\in\left[0,1\right]^{n} representing the distress
level of the banking groups, with a level of hi=1h\_{i}=1 indicating the default
of banking group nin\_{i}. We also denote with D∈{0,1}nD\in\left\{0,1\right\}^{n} a
binary state vector which represents whether a banking group nin\_{i} is in distress
(di=1⇔hi>0d\_{i}=1\Leftrightarrow h\_{i}>0) or not
(di=0⇔hi=0d\_{i}=0\Leftrightarrow h\_{i}=0). Lastly, we have the binary
state vector I∈{0,1}nI\in\left\{0,1\right\}^{n} indicating the set of
inactive nodes. Nodes in a distressed state become inactive nodes in the
next period, to ensure no infinite reverberations are introduced into
the system. With this in mind we can simulate the dynamics of a shock
propagation within the long-term credit market or cross-securities
market as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(t)\displaystyle H\left(t\right) | =min⁡{H​(t−1)+Wl1,eq​[H​(t−1)⋅D​(t−1)], 1𝐧},\displaystyle=\min\left\{H\left(t-1\right)+W^{l\_{1},\textit{eq}}\left[\,H(t-1)\cdot D(t-1)\,\right],\ \mathbf{1}\_{\mathbf{n}}\right\}, |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(t)\displaystyle I\left(t\right) | =min⁡{I​(t−1)+D​(t−1), 1𝐧},\displaystyle=\min\left\{I\left(t-1\right)+D\left(t-1\right),\ \mathbf{1}\_{\mathbf{n}}\right\}, |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | di​(t)\displaystyle d\_{i}\left(t\right) | ={1,if ​hi​(t)=1​ and ​Ii​(t−1)=0,0,otherwise.\displaystyle=\begin{cases}1,&\text{if }h\_{i}\left(t\right)=1\text{ and }I\_{i}\left(t-1\right)=0,\\ 0,&\text{otherwise.}\end{cases} |  | (3) |

For the
liquidity shortfall propagation, we have a very similar dynamic with the
exception that the matrices Wl1,eqW^{l\_{1},\textit{eq}} are now replaced
by Wl2,liqW^{l\_{2},\textit{liq}}.

The above equations define a recursive propagation mechanism. Distress at time t−1t-1 is transmitted through the
weight matrix Wl1,eqW^{l\_{1},\textit{eq}} (or Wl2,liqW^{l\_{2},\textit{liq}} for the liquidity layers), updating the distress levels H​(t)H(t).
The binary vector D​(t)D(t) flags distressed nodes, while I​(t)I(t) marks nodes that become inactive after being distressed,
preventing repeated reverberations. The process converges once no additional nodes enter distress.

To trigger the dynamics, we have the following set of initial
conditions:

* •

  hi∈Sf​(t=1)=1h\_{i\in S\_{f}\ }\left(t=1\right)=1 and
  hi∉Sf​(t=1)=0h\_{i\notin S\_{f}\ }\left(t=1\right)=0
* •

  di∈Sf​(t=1)=1d\_{i\in S\_{f}\ }\left(t=1\right)=1 and
  di∉Sf​(t=1)=0d\_{i\notin S\_{f}\ }\left(t=1\right)=0

with SfS\_{f} the singleton set containing the node that is going
initially in default due to an exogenous shock introduced to the system.

After the dynamics converges at time TT, we can compute the DebtRank
value of node ni∈Sfn\_{i}\in S\_{f} as:

|  |  |  |
| --- | --- | --- |
|  | D​Ri=∑j[hj​(t=T)−hj​(t=1)]​vjDR\_{i}=\ \sum\_{j}{\left[h\_{j}\left(t=T\right)-h\_{j}\left(t=1\right)\right]v\_{j}} |  |

With
vi=∑jWijl∑i∑jWi,jlv\_{i}=\frac{\sum\_{j}W\_{\text{ij}}^{l}}{\sum\_{i}{\sum\_{j}{W\_{i,j}^{l}\ }}}
a proxy for the relative economic value of a node defined as the
proportion of total investments (funding for the liquidity layers)
contributed by the node nin\_{i}. D​RiDR\_{i} thus measures the additional
distress propagated into the system, excluding the initial distress
caused by the exogenous shock. This additional distress can be used as a
proxy for the systemic impact of nin\_{i} on a specific layer within
the multi-layer network. For l1∈l\_{1}\in {long-term credit
market, cross-securities market}, systemic impact reflects potential default cascades due to counterparty risk.
For l2∈l\_{2}\in {short-term credit market,
short-term funding market}, systemic impact reflects potential liquidity crunches due to roll-over and funding risk.161616The DebtRank modifications to capture liquidity shortfalls are partly based on the Exposed–Distressed–Bankrupted (EDB) model of [brandi2018epidemics], with the main difference that we incorporate information on banks’ balance-sheet composition, as suggested as an extension by the authors.

For each node nin\_{i} of the network, we initiate both models to compute its DebtRank. Comparing across layers directly addresses the multi-channel nature of contagion: institutions that appear marginal in one market can be central in another, and the ranking of systemic importance can shift with the transmission mechanism [bargigli2015multiplex].

Figure [4](https://arxiv.org/html/2602.10960v1#S6.F4 "Figure 4 ‣ 6.2 Propagation-based systemic importance ‣ 6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") shows the results for the credit risk simulation.
For both the long-term credit market and the cross-securities market we observe relatively small DebtRank values with the bulk below 2%. This implies that most banks would account for less than 2% of the system’s economic value in the event of their default. In the long-term credit layer, the most systemic bank accounts for roughly 5% of the market, whereas in the cross-securities layer the maximum is around 3%. Importantly, the identity of the most systemic bank differs across these two layers, consistent with the notion that systemic importance is channel-specific in multilayer financial networks [bargigli2015multiplex].

![Refer to caption](x4.png)


Figure 4: Top panel: densities of DebtRank values for the long-term credit
layer (left in yellow) and cross-securities layer (right in red); x-axes
depict DebtRank values in (%).
Bottom panel: cumulative counts of the same DebtRank values for the two layers

Likewise, Figure [5](https://arxiv.org/html/2602.10960v1#S6.F5 "Figure 5 ‣ 6.2 Propagation-based systemic importance ‣ 6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") reports DebtRank values for the liquidity-shortfall calibration across different values of the liquidity buffer scaler β\beta.
A first pattern is the substantial difference between the two short-term layers: the repo market exhibits materially larger propagation than the short-term credit market. In the base scenario β=0.05\beta=0.05, the repo layer features systemic impacts up to an order of magnitude larger, with some nodes accounting for up to 10% of the repo market in the event of default. This gap narrows as β\beta increases, with β=0.2\beta=0.2 yielding more similar DebtRank values across the two layers.

The non-linear sensitivity to liquidity buffers is highlighted in the last column of Figure [5](https://arxiv.org/html/2602.10960v1#S6.F5 "Figure 5 ‣ 6.2 Propagation-based systemic importance ‣ 6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment"). The increase in DebtRank from β=0.1\beta=0.1 to 0.20.2 is substantially larger than the increase from β=0.05\beta=0.05 to 0.10.1, for both layers. This illustrates how tighter liquidity conditions can amplify roll-over risk and contagion potential. Finally, while the repo market exhibits high systemic impact under this calibration, it is also highly collateralized; in practice, collateral liquidation can mitigate liquidity shortfalls and reduce propagation.171717An extension of the current framework would be to include collateral information in future work.

![Refer to caption](x5.png)


Figure 5: 
DebtRank values for the two layers that are concerned with
funding risk, the short-term credit market (top panel, color-coded in
blue shades) and the short-term funding market (bottom-panel,
color-coded in green shades). First three columns represent DebtRank
values for respectively β=0.05\beta=0.05, β=0.1\beta=0.1 and
β=0.2\beta=0.2, with β∈[0,1]\beta\in[0,1] a liquidity buffer scaler with
higher β\beta values aligned with a higher net cash outflow. The last column
shows the cumulative counts of DebtRank (darker shades indicate higher
β\beta values). x-axes depict DebtRank values in (%) .

We can also examine whether non-linearities exist across layers: when propagating an exogenous shock through multiple layers simultaneously, does systemic impact exceed what would be implied by treating layers independently?

Figure [6](https://arxiv.org/html/2602.10960v1#S6.F6 "Figure 6 ‣ 6.2 Propagation-based systemic importance ‣ 6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") reports this thought experiment. The left panel considers shocks propagated jointly through the long-term credit and cross-securities layers, whereas the right panel focuses on the short-term credit and repo layers.181818The figure shows results for β=0.1\beta=0.1, although different values yield the same qualitative results. The x-axis depicts DebtRank, and the y-axis lists the top 10 banks by systemic impact. Blue markers correspond to DebtRank computed on the aggregated (combined) layer, while yellow markers represent a linear superposition of layer-by-layer DebtRank values.191919The top 10 banks with highest DebtRank values are determined by taking the average results of the two computation methods. Differences between blue and yellow markers capture interaction effects induced by aggregation. In the left panel, linear superposition tends to overstate systemic impact relative to the direct aggregated computation. In the right panel, differences are smaller and less systematic. Overall, with the exception of a few highly systemic nodes for which aggregation induces more noticeable deviations, the proximity of the two computations suggests limited additional non-linearities from simple layer aggregation in this setting.

![Refer to caption](x6.png)


(a) Long-term credit market and cross-securities market.

![Refer to caption](x7.png)


(b) Short-term credit market and funding market.

Figure 6: 
Left panel depicts DebtRank values when shocking simultaneously the long-term credit market and the cross-securities market; right panel focuses on the short-term credit market and funding market. The x-axis depicts DebtRank, whereas the y-axis depicts the top 10 banks with the largest systemic impact. The blue markers are DebtRank values when computed on the aggregated layers, whereas yellow markers are based on a linear superposition of the DebtRank values computed for the layers separately. The figure shows results for β=0.1\beta=0.1, although different values yield the same qualitative results. The top 10 banks with highest DebtRank values are determined by taking the average results of the two computation methods.

### 6.3 Micro-structural agent-based contagion framework

Our second analytical use case leverages an agent-based modelling framework based on the micro-structural multi-layer approach of [montagna2016multi], extended in [montagna2020origin]. In contrast to the original paper, we use real-world exposures from our multilayer network rather than simulated edges between nodes. This allows us to evaluate a standard micro-structural propagation mechanism in a setting where network topology and exposure magnitudes are disciplined by granular data.

We assume that a shock first passes through the long-term interbank market, where banking groups borrow and lend to each other on a long-term basis and issue and invest in shares and obligations to each other. This market is primarily embedded with counterparty risk, i.e., the risk that a debtor cannot meet its obligations, forcing creditors to book losses. Similarly, if an investee goes into default, its investors book corresponding losses.
Outcomes from the long-term market may induce a chain reaction in the short-term liquidity market where banking groups use short-term debt to finance balance-sheet activities; this market is embedded with funding and roll-over risk.
When a creditor hoards liquidity, its debtors may struggle to refinance and meet repayments. Lastly, contagion can propagate through the external securities market where securities are marked-to-market and banking groups hold potentially overlapping portfolios. This market is embedded with market risk: liquidation by one node can depress prices and deteriorate the balance sheets of other holders, potentially generating a fire-sale spiral.

The agent-based framework allows us to assess systemic importance in terms of how the default of a banking group influences the system through these channels. We take a similar approach as for the DebtRank analysis and, for each node nin\_{i}, initiate a simulation in which nin\_{i} goes into default due to an exogenous shock.
The default corresponds to a full depletion of nin\_{i}’s cash and equity balances, leading to the violation of regulatory requirements and the freezing of its securities portfolio. Creditors and investors of nin\_{i} on the long-term market book losses accordingly; if this reduces their capital ratios below a threshold they begin hoarding liquidity on the short-term market, propagating the initial shock further. We track (i) the number of additional defaults induced by nin\_{i} and (ii) the cumulative capital base of defaulting banks until convergence (i.e., when no additional defaults occur). We repeat this exercise with each node as the initially defaulting entity.
We refer to Appendix [A](https://arxiv.org/html/2602.10960v1#A1 "Appendix A Agent-based modelling framework ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") for a more detailed exposition of the model and its dynamics.

In Figure [7](https://arxiv.org/html/2602.10960v1#S6.F7 "Figure 7 ‣ 6.3 Micro-structural agent-based contagion framework ‣ 6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment"), the left panel reports the number of additional defaults, while the right panel reports the cumulated capital base of defaulting entities as a fraction of total capital in the system. Most institutions do not generate contagion (zero additional defaults). For a small subset, however, initial defaults trigger cascades: some nodes induce up to two additional defaults, while a smaller set generates cascades of 10 to 15 additional defaults. For one entity, default triggers a long chain across multiple cycles, leading to 43 additional defaults, indicating far-reaching propagation that reaches seemingly distant nodes.

All entities that generate contagion effects originate from only five countries, suggesting national clustering effects. While several contagion-inducing institutions are large, we also observe smaller institutions that induce propagation, and conversely large institutions that do not. This underscores that size alone has limited explanatory power for systemic impact, consistent with theoretical results obtained on artificial networks [glasserman2015likely].
The bottom panel shows that the cumulated capital base remains below 10% for most cascades, but four nodes induce spirals exceeding 10%, reaching more than 50% for the most impactful entity.

![Refer to caption](x8.png)


(a) Additional number of defaults triggered by an initial default.

![Refer to caption](x9.png)


(b) Cumulative capital base of defaulting institutions.

Figure 7: 
Panel (a) reports the additional number of defaults induced by an initially defaulting institution nin\_{i}.
Panel (b) reports the cumulative capital base of defaulting institutions, including nin\_{i}.
Marker size is proportional to total assets. Institutions that induce contagion effects are shown in red; institutions with no contagion effects are shown in black.
The x-axis reports anonymized bank identifiers.
Risk weights are set to wib=0.2w^{\mathrm{ib}}=0.2 for interbank exposures and wes=0.1w^{\mathrm{es}}=0.1 for external securities.
Price-impact weights are set to α=0.2\alpha=0.2.
The liquidity-buffer scaler is β=0.05\beta=0.05, and the minimum capital ratio is γ¯=0.10\overline{\gamma}=0.10.

Figure [8](https://arxiv.org/html/2602.10960v1#S6.F8 "Figure 8 ‣ 6.3 Micro-structural agent-based contagion framework ‣ 6 Layer-aware systemic-risk assessment ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") zooms into the 10 most systemically important institutions and studies sensitivity to the liquidity buffer scaler β\beta. A higher β\beta corresponds to greater net outflows of short-term funds and thus higher liquidity risk. Increasing β\beta from 0.05 to 0.1 produces stronger contagion: the number of additional defaults rises on average by 8 and the cumulative defaulted capital base by 3.2% (a relative increase of 27%). Increasing β\beta further to 0.2 yields an extreme increase, with all 10 institutions producing large cascades (around 75 additional defaults). The uniformity at β=0.2\beta=0.2 suggests an upper bound on default counts that is largely determined by network topology. A similar non-linear pattern emerges for the cumulative capital base, reaching around 80% (an average relative increase of roughly 500%).
These findings align with the DebtRank sensitivity analysis and highlight the importance of maintaining adequate liquidity buffers to mitigate contagion when liquidity hoarding is present.

![Refer to caption](x10.png)


(a) Additional defaults induced by the initial default.

![Refer to caption](x11.png)


(b) Cumulative capital base of defaulting institutions.

Figure 8: 
Panel (a) reports the additional number of defaults induced by an initially defaulting institution nin\_{i}.
Panel (b) reports the cumulative capital base of defaulting institutions, including nin\_{i}.
Each initially defaulting institution is selected among the most systemic nodes in the network.
The x-axis reports anonymized bank identifiers; the first two characters indicate the country of headquarters.
Risk weights are set to wib=0.2w^{\mathrm{ib}}=0.2 for interbank exposures and wes=0.1w^{\mathrm{es}}=0.1 for external securities.
Price-impact weights are set to α=0.2\alpha=0.2.
The liquidity-buffer scaler varies over β∈{0.05,0.10,0.20}\beta\in\{0.05,0.10,0.20\}, and the minimum capital ratio is γ¯=0.10\overline{\gamma}=0.10.

## 7 Summary and conclusions

The Great Financial Crisis brought to the fore the relevance of interconnectedness in interbank markets and the need for detailed data to understand the relationships that link credit institutions. Subsequent episodes, including the Great Recession and the Covid-19 shock, further underscored that macro-financial outcomes can be shaped by propagation mechanisms operating through multi-faceted and far-reaching linkages among financial entities.

This paper advances an empirically grounded, system-level representation of euro area banking interconnectedness. We integrate multiple granular supervisory and statistical collections into a multilayer network of significant banking groups, enabling a layer-consistent view of exposures across distinct transmission channels. The multilayer perspective reveals pronounced heterogeneity in both topology and institutional roles across markets; heterogeneity that can be muted or misrepresented when exposures are collapsed into a single aggregate network.

Building on this integrated measurement framework, we extend leading network-based systemic-risk approaches to a setting in which exposures are observed jointly across markets and can be analysed coherently at the layer level. In particular, we adapt a propagation-based systemic-importance measure and a micro-structural agent-based model to operate on the empirically constructed multilayer network. The propagation analysis identifies channel-specific systemic importance and documents a strong sensitivity of short-term market contagion to liquidity buffers, with the ranking of influential institutions varying across layers. The agent-based framework, by explicitly coupling balance-sheet adjustments, roll-over decisions, and fire-sale spillovers across market segments, generates sizeable default cascades for a small subset of institutions and reinforces that systemic impact is shaped not only by size, but also by network position and market-specific connectivity.

These results underscore the value of assessing resilience in a layer-aware manner when the same institutions participate in multiple market segments with different micro-structural features. A multilayer, empirically calibrated view of exposures can inform policy discussions on the design of flexible and targeted macro- and micro-prudential instruments, and provides a concrete empirical basis for evaluating multi-channel contagion mechanisms in stress-testing exercises.

## Appendix A Agent-based modelling framework

The main model deployed in this paper is heavily based on the microstructural multi-layered approach introduced in [montagna2016multi]. In contrast to the original paper, we do not rely on simulated edges between nodes, but utilize our multi-layer network constructed of real-world granular data. The agent-based model allows one to traverse an initial exogenous default shock throughout the different layers of the multi-layer network, considering the distinct characteristics and embedded risks within the layers.

Each node nin\_{i} is characterized by a simplified balance sheet (Table [2](https://arxiv.org/html/2602.10960v1#A1.T2 "Table 2 ‣ Appendix A Agent-based modelling framework ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment")).

Table 2: Simplified balance sheet of banking groups

|  |  |
| --- | --- |
| Assets | Liabilities |
| cic\_{i}: cash | did\_{i}: deposits |
| eie\_{i}: external securities | e​qieq\_{i}: equity |
| uiau\_{i}^{a}: cross-securities holdings | uilu\_{i}^{l}: cross-securities issuance |
| lill\_{i}^{l}: long-term loans | bilb\_{i}^{l}: long-term borrowings |
| lisl\_{i}^{s}: short-term loans | bisb\_{i}^{s}: short-term borrowings |
| hiah\_{i}^{a}: repurchase agreements | hilh\_{i}^{l}: short-term funding |
| oiao\_{i}^{a}: other assets | oilo\_{i}^{l}: other liabilities |

Next, we define the propagation logic of the model. We assume that nodes
can be characterized by a state variable
ϕ∈{0,1,2}n\mathbf{\phi}\in\left\{0,1,2\right\}^{n}:

|  |  |  |
| --- | --- | --- |
|  | ϕi={2, if ni in default1, if ni in distress0, otherwise\phi\_{i}=\begin{cases}2,&\textit{ if $n\_{i}$ in default}\\ 1,&\textit{ if $n\_{i}$ in distress}\\ 0,&\textit{ otherwise}\end{cases} |  |

We further assume that nodes will take the necessary measures possible
to avoid going into distress or default.

There are two main channels that impact the state of a node. The first
channel is determined by the capital of the nodes. Nodes go into a
distressed state if at any point in time we observe:

|  |  |  |
| --- | --- | --- |
|  | γ=Eqwb⋅(ll+ls+ua)+S​(ws⋅P)+Cte<γ¯\gamma=\frac{\text{Eq}}{w^{b}\cdot\left(l^{l}+l^{s}+u^{a}\right)+S\left(w^{s}\cdot P\right)+C^{\text{te}}}<\ \overline{\gamma} |  |

With wb∈ℝn,ws∈ℝmw^{b}\in\mathbb{R}^{n},\ w^{s}\in\mathbb{R}^{m}
respectively the risk-weights for interbank assets and external
securities. S∈ℝn×mS\in\mathbb{R}^{n\times m}\  is the holding matrix of securities
with si​μs\_{i\mu} the amount that node nin\_{i} is holding of
security μ\mu. P∈ℝmP\in\mathbb{R}^{m} is the price vector of securities with pμp\_{\mu} the price of security μ∈M\mu\in M and CteC^{\text{te}} a constant representing risk-weighted
assets that are not explicitly modelled. γ∈ℝn\gamma\in\mathbb{R}^{n}
is thus a proxy for the risk-weighted capital ratio of banks and needs
to be above a minimum regulatory lower bound γ¯\overline{\gamma}.

The second channel that might impact the state of a node is determined
by the liquidity position of the node. Nodes go into a distressed state
if we observe at any point in time:

|  |  |  |
| --- | --- | --- |
|  | c<β​(d+bs+hl)c<\beta\left(d+b^{s}+h^{l}\right) |  |

With β\beta a liquidity buffer scaler.

We further assume that a propagation cycle coincides with the longest
maturity of short-term debt, that is during the shock propagation nodes
need to decide how much of their short-term debt to roll-over to their
current debtors. In case a node decides to withdraw its short-term funds
from the market, its debtors might be facing difficulties in actually
repaying the debt. This gives rise to an additional liquidity channel
that impacts the state of a bank by the end of a cycle. This is encoded
as:

|  |  |  |
| --- | --- | --- |
|  | p<p¯p<\overline{p} |  |

With p¯∈ℝn\overline{p}\in\mathbb{R}^{n} the proportion of short-term
debt that banks need to repay from their total short-term borrowings,
and p∈ℝnp\in\mathbb{R}^{n} the clearing vector that clears the
short-term interbank market during a certain propagation cycle. Note the
correspondence with an [eisenberg2001systemic] system.

If a node nin\_{i} admits to any one of the three above violations it is
put in a distressed state. Node nin\_{i} will then try to rectify its
position by (i) withdrawing liquidity from the short-term interbank
market and, if further needed, by (ii) selling off (a portion) of its
external securities. If after trying to do so, nin\_{i} is still in a
distressed state it will be put in a default state. When a node nin\_{i}
goes into default its securities portfolio gets frozen by external
authorities until the markets are stable again. This to avoid inducing
further fire sales into the system. Next, the remaining nodes will have
to book their losses on the long-term interbank market in case they had
exposures against the defaulted nodes. This will induce a second cycle
in the shock propagation mechanism and will continue to do so until the
system converges, i.e. when no additional defaults are observed at the
end of a propagation cycle.

### A.1 The long-term interbank market

The long-term interbank market is constructed based on two layers of the multi-layer network, the long-term credit, and the cross-securities layers. At the beginning of each propagation cycle, nodes book losses from the long-term interbank market, if any, due to the bankruptcy of their debtors/investee’s in the previous period. These losses affect the capital of the node and therefore can lead to the violation of their capital ratio constraint. To be more precise, and in line with [ContMoussaSantos], when a node nin\_{i} defaults, it leads to the immediate write-down in value of all its liabilities to its creditors/investors. These losses are then imputed to the Tier 1 capital base (represented by the E​q∈ℝnEq\in\mathbb{R}^{n} vector) of the creditors, leading to a deterioration of the risk-weighted capital ratio of these creditors/investors. In case the updated capital ratio is lower than the regulatory required lower bound γ¯\bar{\gamma}, the creditors and investors become distressed and will try to gain liquidity from the short-term interbank market to rebalance their capital ratio.

### A.2 The short-term interbank market

If one of the nodes constraints is violated, it will need to react
adequately to avoid going into default. The first step to undertake is
to reduce its short-term interbank market exposures. We assume that each
cycle in the model coincides with the longest maturity level of
short-term debt, that is at the end of each cycle nodes need to decide
on the amount of their short-term debt they want to roll-over to their
debtors for next period.

This endogenous decision is based on two factors: (i) the need to make sure a node’s constraints are satisfied and (ii) the fact that a nodes own funding from other creditors is being reduced, forcing it to withdraw more money from its debtors.

This endogenous decision making can be formulated by the following
mapping:

|  |  |  |
| --- | --- | --- |
|  | f⋅l=m​i​n​{r+max⁡{(WstT​f−cbuf), 0},l}f\cdot l=min\{r+\max\left\{\left(W\_{\text{st}}^{T}f-c\_{\text{buf}}\right),\ 0\right\},\ l\} |  |

With,

* •

  f∈[0,1]nf\in\left[0,1\right]^{n} the fraction of
  short-term debt that will not be rolled-over
* •

  l=ls+ual=l^{s}+u^{a}, the total short-term assets available to
  roll-over,
* •

  WstT=Ws​h​o​r​t​\_​t​e​r​m​\_​c​r​e​d​i​tT+Ws​h​o​r​t​\_​t​e​r​m​\_​f​u​n​d​i​n​gTW\_{\text{st}}^{T}=W\_{short\\_term\\_credit}^{T}+W\_{short\\_term\\_funding}^{T},
  the sum of the adjacency matrices derived from the short-term credit
  and funding layers. (wstT)ij\left(w\_{\text{st}}^{T}\right)\_{\text{ij}}
  thus represents the total short-term debt that nin\_{i} has received from
  jj, and WstT​fW\_{\text{st}}^{T}f depicts then the amount of debt that
  needs to be repaid to nodes
* •

  cbuf=c−β​(d+bs+hl−WstT​f)c\_{\text{buf}}=c-\beta(d+b^{s}+h^{l}-W\_{\text{st}}^{T}f)
  represents the cash level above the liquidity requirement that can
  readily be used to pay back nodes
* •

  r∈ℝnr\in\mathbb{R}^{n} a vector denoting the amount of funds each
  bank wants to withdraw to satisfy their constraints. We can decompose
  rr in two additive components being:

  + –

    rliq=min⁡{max⁡{β​(d+bs+hl−WstT⋅f)−c, 0},l}r\_{\text{liq}}=\min\left\{\max\left\{\beta\left(d+b^{s}+h^{l}-W\_{\text{st}}^{T}\cdot f\right)-c,\ 0\right\},\ \ l\right\}
  + –

    rcap=m​i​n​{m​a​x​{γ¯(Cte+S(ws⋅P)+γ¯wb(ll+l−rliq)−Eqγ¯​wb, 0},l−rliq}r\_{\text{cap}}=min\{max\{\frac{\overline{\gamma}(C^{\text{te}}+S\left(w^{s}\cdot P\right)+\ \overline{\gamma}w^{b}\left(l^{l}+l-r\_{\text{liq}}\right)-Eq}{\overline{\gamma}w^{b}},\ 0\},\ l-r\_{\text{liq}}\}

with rliqr\_{\text{liq}} taking care of liquidity requirements and
rcapr\_{\text{cap}} taking care of capital requirements. The above loop
describes how a node withdraws funds from the short-term market only if
it has problems fulfilling its constraints and in case other nodes
decide to withdraw their funds that are deposited with the node.

Note the similarities between the above mapping and the mapping
introduced by  [eisenberg2001systemic]. We can leverage the same
mathematical tools as used in  [eisenberg2001systemic] to solve the
above decision-making process. To do so we need to rewrite the above,
noting that the mapping is homogenous of degree one, that is:

|  |  |  |
| --- | --- | --- |
|  | f=m​i​n​{r+max⁡{(WstT​f−cbuf), 0}l, 1}f=min\{\frac{r+\max\left\{\left(W\_{\text{st}}^{T}f-c\_{\text{buf}}\right),\ 0\right\}}{l},\ 1\} |  |

Allowing us to reformulate the problem as a fixed-point problem of the
mapping:

|  |  |  |
| --- | --- | --- |
|  | Φ​(f):[0,1]n→[0,1]n=m​i​n​{r+max⁡{(WstT​f−cbuf),0}l,1}\Phi(f):\left[0,1\right]^{n}\rightarrow\left[0,1\right]^{n}=\ min\{\frac{r+\max\left\{\left(W\_{\text{st}}^{T}f-c\_{\text{buf}}\right),0\right\}}{l},1\}\ |  |

Solving the fixed-point problem yields then the short-term equilibrium
state of the short-term interbank market during a propagation cycle.

### A.3 The (external) securities market

Once banks decide about how much to withdraw from the interbank market,
their counterparts might need to sell-off portions of their securities
portfolio, above their cash and short-term funds, in order to
successfully repay their creditors. The securities market is constructed
based on the external-securities layer of the multi-layer network.

To properly model the securities market, we need to know (i)
the prices of the securities in our universe, (ii) the amount that each
node nin\_{i} is holding of security μ\mu and (iii) the way that prices
change through time (which will be endogenously determined). We
therefore use:

* •

  The price vector of securities P∈ℝmP\in\mathbb{R}^{m} with
  pμp\_{\mu} the initial price of security μ∈M\mu\in M. MM represents the set of all securities in our universe, with mm the total number of securities as noted before.
* •

  The holding matrix of securities S∈ℝn×mS\in\mathbb{R}^{n\times m}\ 
  with si​μs\_{i\mu} the amount that node nin\_{i} is holding of
  security μ\mu with ni∈Nn\_{i}\in N and
  μ∈M\mu\in M.
* •

  The total market value of nin\_{i}’s external securities portfolio can
  then be simply represented by:

|  |  |  |
| --- | --- | --- |
|  | E=S​P\ E=SP |  |

With eie\_{i}\  the market value of nin\_{i}’s portfolio.

* •

  Lastly, the sell-off matrix Z∈ℝn×mZ\in\mathbb{R}^{n\times m} with
  zi​μz\_{i\mu} the amount that node nin\_{i} is selling of security
  μ\mu at any given moment in time. Note that
  Z∈[0,S]Z\in[0,\ S].

We furthermore assume that the price dynamics of the securities are
governed by the following process:

|  |  |  |
| --- | --- | --- |
|  | Pt+1=Pt​e−α⋅δP^{t+1}=P^{t}e^{-\alpha\cdot\delta} |  |

With

* •

  α∈[0,1]m\alpha\in\left[0,1\right]^{m} a vector of constants
  representing the narrowness of the market for the securities,
* •

  δ=\delta=
  𝟏𝐧​Z𝟏𝐧​S∈ℝm\frac{\mathbf{1}\_{\mathbf{n}}Z}{\mathbf{1}\_{\mathbf{n}}S}\in\mathbb{R}^{m},
  with δμ\delta\_{\mu} the proportion of security μ\mu that has been
  sold off by the nodes in the network relative to the total available
  amount of that security in the network

Note how the price dynamics assumes that prices cannot increase from one
period to the other, as we model an extreme tail scenario over a short
total timeframe.

We can look at the proportion being sold from two perspectives, (i) the
proportion being sold relative to the initial total holding amount
within the interbank network or (ii) the proportion being sold relative
to the total holding amount available within the interbank as of last
period. (ii) is a more sophisticated approach that induces a memory
effect in the price dynamics: The more of a security has been sold
during a fire sale spiral the harder the price will decrease for each
additional sell that happens.

Fig [9](https://arxiv.org/html/2602.10960v1#A1.F9 "Figure 9 ‣ A.3 The (external) securities market ‣ Appendix A Agent-based modelling framework ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment") illustrates the two different perspectives. The
exponential decrease of (ii) (depicted as the yellow graph in the left
figure) shows the memory effect. When αμ\alpha\_{\mu} is high we see
that the price of a security μ\mu goes down to a lower bound that is
greater than 0 for (i) whereas the price goes to 0 for (ii) (see upper
and bottom panel of the right side of the figure). This edge case can
for example represent a highly illiquid security such as an RMBS product
during the Great Financial Crisis. To adequately model such an
environment we take perspective (ii) moving forward.

![Refer to caption](x12.png)


Figure 9: 
Left panel: price dynamics with impact parameter αμ=0.2\alpha\_{\mu}=0.2,
for both static proportion computation (blue) and dynamic proportion
computation (yellow). Right upper panel: price dynamics of static
proportion-based computation for various αμ\alpha\_{\mu} values. Right
bottom panel: price dynamics of dynamic proportion-based computation for
various αμ\alpha\_{\mu} values. X-axis depict the quantity of μ\mu
sold, y-axis shows the resulting price of μ\mu.
Left panel shows a comparison of the endogenous price mechanism
Pt+1=Pt​e−α⋅δP^{t+1}=P^{t}e^{-\alpha\cdot\delta}when using a static vs.
dynamic proportion-based computation of the amount of securities sold.
The dynamic based computation shows a sharper decrease of the price of a
security due to memory effects. The right panels show price
depreciations for different values of α\alpha for the static based
method (upper) and dynamic based method (lower). The dynamic proportion
can lead to extreme price depreciation when the market is very narrow.

Again, we rely on  [eisenberg2001systemic] to find the optimal ZZ
that helps clear the system:

|  |  |  |
| --- | --- | --- |
|  | p=m​i​n​{c+ΠT​p+Z​P,p¯}p=min\{{c+\ \Pi}^{T}p+ZP,\ \overline{p}\} |  |

With,

* •

  p¯=WstT​f∈ℝn\overline{p}=W\_{\text{st}}^{T}f\in\mathbb{R}^{n} the
  proportion of short-term debt that nodes need to repay from their
  total short-term borrowings based on the roll-over decisions made in
  the short-term interbank market.
* •

  p∈ℝnp\in\mathbb{R}^{n} the clearing vector that clears the
  short-term interbank market within a propagation cycle
* •

  Π∈[0,1]n×n\Pi\in{[0,1]}^{n\times n} the relative liabilities
  matrix with

  |  |  |  |
  | --- | --- | --- |
  |  | πij={(wstT)ij⋅fip¯, if p¯>00,otherwise\pi\_{\text{ij}}=\begin{cases}\frac{\left(w\_{\text{st}}^{T}\right)\_{\text{ij}}\cdot f\_{i}}{\overline{p}},&\textit{ if $\overline{p}>0$}\\ 0,&\textit{otherwise}\end{cases} |  |

  the liability that node nin\_{i} has against
  jj relative to nin\_{i}’s total obligations.
* •

  Z​P∈ℝn×mZP\in\mathbb{R}^{n\times m} gives the liquidity gained from
  selling securities, with the price vector PP in turn dependent on
  how much securities actually being sold, as driven by the endogenous
  price dynamics of the system.

We further assume that a node nin\_{i} in liquidity need sells securities
in its portfolio proportional to the market value of its holdings while taking into account the risk-weights of the securities. That is,
ceteris paribus, securities with higher risk weights are sold in
larger quantities than securities with lower risk weights. The
underlying logic is that banks attempt to be efficient in restoring their
risk-weighted capital ratios. We obtain the proportional weight matrix of portfolios as,

|  |  |  |
| --- | --- | --- |
|  | η=S⋅(ws⋅P)(S⋅[ws⋅P])​1n∈ℝn×m\eta=\frac{S\cdot(w^{s}\cdot P)}{(S\cdot[w^{s}\cdot P])1\_{n}}\in\mathbb{R}^{n\times m} |  |

We can then decompose the sell-off matrix ZZ into three additive
components, one for each of the requirements banks must satisfy:

1. 1.

   Banks must ensure sufficient liquidity to repay creditors in the short-term interbank market, based on roll-over decisions:

   |  |  |  |
   | --- | --- | --- |
   |  | Li​qneedinterbank=max⁡{p¯−(cbuf+ΠT​p), 0}∈ℝn\text{Li}q\_{\text{need}}^{\text{interbank}}=\max\left\{\overline{p}-\left(c\_{\text{buf}}+\Pi^{T}p\right),\ 0\right\}\in\mathbb{R}^{n} |  |

   The amount to be sold of each security is then,

   |  |  |  |
   | --- | --- | --- |
   |  | Zinterbank=m​i​n​{(Li​qneedinterbank)T⋅ηP,S}Z^{\text{interbank}}=min\{\frac{\left(\text{Li}q\_{\text{need}}^{\text{interbank}}\right)^{T}\cdot\eta}{P},\ S\} |  |
2. 2.

   Banks must also satisfy the liquidity requirement,

   |  |  |  |
   | --- | --- | --- |
   |  | Li​qneedliquidity=m​a​x​{β​(d+bs+hl−WstT​f)−c,0}\text{Li}q\_{\text{need}}^{\text{liquidity}}=max\{\beta\left(d+b^{s}+h^{l}-W\_{\text{st}}^{T}f\right)-c,0\} |  |

   The amount to be sold of each security is then,

   |  |  |  |
   | --- | --- | --- |
   |  | Zliquidity=min⁡{(Li​qneedliquidity)T⋅ηP,S−Zinterbank}Z^{\text{liquidity}}=\min\left\{\frac{\left(\text{Li}q\_{\text{need}}^{\text{liquidity}}\right)^{T}\cdot\eta}{P},\ S-Z^{\text{interbank}}\right\} |  |
3. 3.

   Lastly, banks must maintain their capital requirement, recognizing that fire-sale price effects can deteriorate balance sheets:

|  |  |  |
| --- | --- | --- |
|  | Li​qn​e​e​d​\_​r​wcapital=max⁡{wb⋅A+B​(ws⋅P)+Cte−Eqγ¯,0}\text{Li}q\_{need\\_rw}^{\text{capital}}=\max\left\{w^{b}\cdot A+B\left(w^{s}\cdot P\right)+C^{\text{te}}-\frac{\text{Eq}}{\overline{\gamma}}\ ,0\right\} |  |

With,

* •

  A=ll+ls+ha−(rliq+rcap)A=\ l^{l}+l^{s}+h^{a}-\left(r\_{\text{liq}}+r\_{\text{cap}}\right)
* •

  B=S−(Zinterbank+Zliquidity)B=\ S-(Z^{\text{interbank}}+Z^{\text{liquidity}})

Cancelling out the risk-adjusted measure yields liquidity needs in euros:

|  |  |  |
| --- | --- | --- |
|  | Li​qneedcapital=(Li​qn​e​e​d​\_​r​wcapital⋅ηws)​1m∈ℝn\text{Li}q\_{\text{need}}^{\text{capital}}=\left(\frac{\text{Li}q\_{need\\_rw}^{\text{capital}}\cdot\eta}{w^{s}}\right)1\_{m}\in\mathbb{R}^{n} |  |

Raising Li​qneedcapital\text{Li}q\_{\text{need}}^{\text{capital}} ensures that the
capital ratio is at least γ¯\overline{\gamma}.

The amount to be sold of each security is then,

|  |  |  |
| --- | --- | --- |
|  | Zcapital=min⁡{(Li​qneedcapital)T⋅ηP,S−(Zinterbank+Zliquidity)}Z^{\text{capital}}=\min\left\{\frac{\left(\text{Li}q\_{\text{need}}^{\text{capital}}\right)^{T}\cdot\eta}{P},\ S-(Z^{\text{interbank}}+Z^{\text{liquidity}})\right\} |  |

These intermediary results yield
Z=Zinterbank+Zliquidity+Zcapital∈[0,S]n×mZ=Z^{\text{interbank}}+Z^{\text{liquidity}}+Z^{\text{capital}}\in\left[0,\ S\right]^{n\times m},
the sell-off matrix of the system. Solving the fixed-point
problem of the mapping

|  |  |  |
| --- | --- | --- |
|  | ξ​(p):[0,p¯]n→[0,p¯]n:m​i​n​{c+ΠT​p+Z​P,p¯}\xi\left(p\right):\left[0,\ \overline{p}\right]^{n}\rightarrow\left[0,\ \overline{p}\right]^{n}:\ min\{{c+\ \Pi}^{T}p+ZP,\ \overline{p}\}\ |  |

produces the clearing vector pp and, as a byproduct, the sell-off matrix ZZ and updated price vector PP. The mechanism can be interpreted as follows: liquidity needs in the interbank market induce security sales, which depress prices; price declines erode capital ratios, which in turn can raise liquidity needs and further sales. Once pp is sufficient to clear obligations, ZZ and PP stabilize and the system reaches an equilibrium for the propagation cycle.

### A.4 Data considerations

In the context of data considerations for a well-functioning agent-based model, it’s essential to have detailed data encompassing a wide range of financial aspects. Much of this data can be derived from the multi-layer network:

* •

  Agents within the framework are characterized by their balance sheets, which are readily available and accessible in the multi-layered network, thanks to the enrichment process outlined in section [4.4](https://arxiv.org/html/2602.10960v1#S4.SS4 "4.4 Enrichment of the nodes ‣ 4 Network modelling ‣ Integrating granular data into a multilayer network: an interbank model of the euro area for systemic risk assessment"). This includes information about the risk-weighted assets of the agents, allowing for the computation of their capital ratios.
* •

  The model’s long-term interbank market and short-term funding market can be effectively modeled using adjacency matrices Wl,l∈GW^{l},\ \ l\in G within the network. These matrices establish the connections between agents participating in these markets.
* •

  For modeling fire sales in the securities market, we can start by examining the external securities layer, of which the security-
  level representation aligns with the holding matrix S∈ℝn×mS\in\mathbb{R}^{n\times m} of the model.
* •

  The price vector PP is implicitly embedded within the multi-layer network, as the external securities layer includes prices for the securities, necessary for calculating the market value of portfolio investments.

However, it’s worth noting that certain information isn’t naturally present in the network:

* •

  The agent-based model relies on risk weights for both interbank assets and external securities, which are not directly available in the network. A workaround involves using ratings data to attribute risk weights based on the security’s rating. Alternatively, constant values for the weights can be assigned.
* •

  To model price depreciations of securities, it’s essential to quantify the liquidity or narrowness of the market for various securities, denoted as α∈ℝm\alpha\in\mathbb{R}^{m}. This calibration process typically relies on publicly available market data, including price returns and traded volumes, such as the approach described in [Busseti\_2012]. This information is currently not captured by the multi-layer network and needs to be simulated to explore different market scenarios and their potential impact on the interbank system.