---
authors:
- Soumen Majhi
- Anna Mancini
- Giulio Cimini
doc_id: arxiv:2603.09854v1
family_id: arxiv:2603.09854
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Modeling structure and credit risk of the economy: a multilayer bank-firm
  network approach'
url_abs: http://arxiv.org/abs/2603.09854v1
url_html: https://arxiv.org/html/2603.09854v1
venue: arXiv q-fin
version: 1
year: 2026
---


Soumen Majhi


 Anna Mancini


 and Giulio Cimini
  
Physics Department and INFN



  
University of Rome Tor Vergata


 00133 Rome (Italy)

###### Abstract

Assessing the resilience of the economy requires accounting for its intrinsic multi-layer nature, by assessing for instance how disruptions at the firm level spread through the production network and propagate to the banking sector. Methods exist to measure the reverberation of shocks over the multilayer network of supply-customer relations among firms, corporate loans of banks and their interbank market exposures.
However, empirical network data are often privacy protected and thus inaccessible to researchers and regulators.
In this work we develop an unified framework, combining state-of-the art techniques to reconstruct the whole multilayer structure of the economy
from balance sheet information of banks and firms, as well as dynamics of shock propagation from the interfirm to the interbank layers.
We showcase application of our methodology using data of the Italian economy. We identify the most systemically important firms and industries, as well as the most vulnerable banks, further assessing the determinants of systemic risk – obtaining results coherent with the empirical literature on network contagion.
Overall, our framework allows performing detailed network-based stress tests on a digital twin of the economy, without requiring detailed network information that is difficult to acquire.

## 1 Introduction

Modern economies are characterized by complex multi-layered interdependencies linking corporate entities with financial institutions. Production networks describe the web of supply relationships through which firms exchange intermediate goods and services [[1](#bib.bib1)], while financial networks capture credit exposures among banks and between banks and firms [[2](#bib.bib2)]. The structural coupling between these two domains is fundamental for the functioning of modern economies, but also plays a crucial role in determining how localized disruptions evolve into systemic crises. Assessing economic resilience therefore requires understanding not only contagion within each network layer, but also the feedback mechanisms that connect the economic and financial sectors.

Recent global events have highlighted the importance of such cross-layer interactions. Climate-related disasters [[3](#bib.bib3), [4](#bib.bib4), [5](#bib.bib5)], geopolitical conflicts [[6](#bib.bib6)], and the COVID-19 pandemic [[7](#bib.bib7)] have revealed how disruptions in production networks can rapidly propagate across supply chains, generating firm-level losses that spill over to creditor banks. When suppliers halt production, downstream firms experience revenue declines that may translate into liquidity shortages and loan defaults, thereby impairing bank balance sheets. Financial distress can in turn feed back into the real economy through credit contraction. These reinforcing loops lie at the core of systemic risk [[8](#bib.bib8), [9](#bib.bib9)] and economic resilience [[10](#bib.bib10), [11](#bib.bib11)]. Developing tools capable of quantifying such multilayer contagion dynamics has thus become a priority for regulators and policymakers.

A fundamental obstacle to this endeavor is data availability. Detailed information on interfirm transactions, bank-firm credit exposures, and interbank lending relationships is typically confidential and inaccessible to researchers and stakeholders. Yet systemic risk is inherently shaped by network topology. Being able to reconstruct hidden economic and financial networks from partial balance-sheet information has therefore become a prerequisite for realistic stress testing and policy analysis [[12](#bib.bib12)].

In the aftermath of the global financial crisis of 2007/2008, research efforts concentrated primarily on the interbank market. The reconstruction problem in this context consisted in inferring bilateral exposures from aggregate balance-sheet figures. This challenge was addressed using methods rooted in statistical physics: when only aggregate information is available, the principle of maximum entropy prescribes selecting the least biased probabilistic network consistent with the available information (acting as constraint). Applied to networks, this approach leads to Exponential Random Graph (ERG) models [[13](#bib.bib13), [14](#bib.bib14)]. Fitness-based ERG specifications have proven highly effective in reconstructing interbank networks without topological information, consistently outperforming alternative probabilistic approaches in validation exercises [[15](#bib.bib15)].
More recently, attention has shifted towards production networks. Unlike interbank markets, supply chains are shaped by technological and sectoral compatibility constraints: not all pairs of firms can realistically trade, and connections depend on input-output requirements. Standard ERG formulations, which treat all node pairs as potentially connected, are therefore insufficient to capture the functional structure of production systems. Models incorporating sectoral information and input-output constraints have therefore begun to address this limitation [[16](#bib.bib16), [17](#bib.bib17)].

Beyond reconstruction, another key limitation of the literature lies in the fragmentation of contagion modeling. A substantial body of work has examined shock propagation within financial networks [[18](#bib.bib18), [19](#bib.bib19), [20](#bib.bib20), [21](#bib.bib21)] or within production networks [[22](#bib.bib22), [23](#bib.bib23)]. However, most approaches treat the real economy and the financial system as largely separate domains. Only a few recent studies have attempted to link firm-level supply chains with bank exposures. For instance, Guth et al. [[24](#bib.bib24)] investigates the impact of COVID-19 supply-chain disruptions on Austria’s banking sector using aggregated input-output data. Borsos et al. [[25](#bib.bib25)] analyze bidirectional amplification between firms and banks. Tabachová et al. [[26](#bib.bib26)] develop a multilayer contagion model integrating firm-level supply chains and bank-firm credit relationships, but without incorporating the interbank market. Fialkowski et al. [[27](#bib.bib27)] studies how production shocks generate correlated defaults and spillover into interbank solvency contagion. Despite these advances, a unified data-driven framework that simultaneously reconstructs all relevant layers and models their ordered interaction remains absent.

In this work, we address this gap by developing a comprehensive computational framework that reconstructs and integrates the interbank, bank-firm, and firm-firm networks into a single multilayer economic-financial structure. Importantly, our approach relies exclusively on balance-sheet information, enabling the construction of a “digital twin” of the economy without requiring access to confidential micro-level transaction data.
Each layer is reconstructed using state-of-the-art techniques tailored to its structural properties. The interbank network is inferred using the Density-Corrected Gravity Model (DCGM) [[21](#bib.bib21)], the bank-firm credit layer via the Enhanced Capital Asset Pricing Model (ECAPM) [[28](#bib.bib28)], and the firm-firm production network through the Stripe-Corrected Gravity Model (SCGM), using the Input-Output Gravity Model (IOGM) [[16](#bib.bib16), [17](#bib.bib17)] specification. These reconstructed layers are then combined into a coherent multilayer network.

On top of this structure, we design an ordered contagion pipeline linking production and financial distress. Shocks originate in the production layer, where disruptions propagate across supply chains and generate output losses measured by the Economic Systemic Risk Index (ESRI) [[22](#bib.bib22)], accounting for essential and non-essential input constraints [[23](#bib.bib23)]. The resulting erosion of firm profit margin translates into credit losses for banks, quantified through the Financial Systemic Risk Index (FSRI) [[26](#bib.bib26)] – which we extend to take into account non-performing loans (NPL). Residual bank-level equity losses then propagate within the interbank market via DebtRank dynamics [[29](#bib.bib29)], capturing financial amplification effects.
Together, these coupled processes link the economic and financial sectors into a single cascade framework, allowing us to track how local failures evolve into systemic events.

We apply this unified framework to balance-sheet data for Italian firms and banks. Our analysis identifies the most systemically important firms and industries, as well as the most vulnerable banks, and provides empirical evidence on the determinants of systemic risk. Overall, our results demonstrate that integrating reconstructed production and financial networks within a single cascade framework enables faithful, detailed network-based stress testing of the economy, even in the absence of granular transaction data.

Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") provides a conceptual representation of the full modeling pipeline underlying our firm-bank contagion analysis. Panel A illustrates the reconstruction stage, where interfirm, firm-bank, and interbank layers are inferred separately and combined into a multilayer bank-firm network. Panel B depicts the ordered propagation mechanism,where shocks originate at the firm level, spread across production relationships, induce bank distress through credit exposures, and are subsequently transmitted within the interbank market. Panel C summarizes the resulting systemic-risk measures, emphasizing how risk rankings progressively change as additional layers of contagion are incorporated.

![Refer to caption](2603.09854v1/x1.png)


Figure 1: Schematic overview of the multilayer bank-firm systemic-risk framework. (A) Network reconstruction: starting from balance-sheet information for banks and firms in our sample, three interconnected networks are reconstructed independently: the interbank market layer (top, blue links), the bank-firm credit network (middle, green links), and the interfirm production network layer (bottom, red links).
(B) Shock propagation: Once the multilayer network is reconstructed, we simulate the spreading of a shock originating in the interfirm layer. The shock first diffuses through interfirm production links, according to ESRI dynamics (left), then is transmitted to the bank layer via firm exposures to banks, according to FSRI (center), and finally amplified through interbank contagion following DR dynamics (right). (C) Systemic-risk analysis: the cumulative effects of the shock propagation are summarized through ranked risk profiles, showing how successive layers contribute to economic losses: reduction of production (ESRI, left), additional bank credit losses (ESRI+FSRI, middle), and interbank amplification (ESRI+FSRI+DR, right).

## 2 Materials and Methods

### 2.1 Variables Definitions

We model a multi-layer weighted directed network composed of NBN\_{B} banks and NFN\_{F} firms. Banks are labeled with Greek letters (α=1,…,NB\alpha=1,\dots,N\_{B}) while firms are labeled with Latin letters (i=1,…,NFi=1,\dots,N\_{F}).
Table [1](#S2.T1 "Table 1 ‣ 2.1 Variables Definitions ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") reports the value we extract from balance sheets of banks and firms, which we use to reconstruct the multilayer network (see below).
Bank-level attributes for each bank α\alpha include interbank assets AαA\_{\alpha}, interbank liabilities LαL\_{\alpha}, corporate loans CαC\_{\alpha} and equity EαE\_{\alpha}. Firm-level attributes for each firm ii are production RiR\_{i}, supply SiS\_{i}, bank loans BiB\_{i}, shareholder funds EiE\_{i} and sector of production pip\_{i}.
Finally, we consider industrial sector attributes (Input–Output table entries {sp→p′}\{s\_{p\to p^{\prime}}\} and essentiality relations {ep→p′}\{e\_{p\to p^{\prime}}\}) to inform the interfirm layer through input-output flows and critical supplier dependencies (see below).
We exploit this balance-sheet level information as constraint to reconstruct a statistically principled ensemble of multilayer networks, which then we use as substrate for the shock propagation dynamics.

| Variable | Description |
| --- | --- |
| AαA\_{\alpha} | Total interbank assets of bank α\alpha (claims on other banks) |
| LαL\_{\alpha} | Total interbank liabilities of bank α\alpha (obligations to other banks) |
| CαC\_{\alpha} | Total corporate loans of bank α\alpha (credit granted to firms) |
| EαE\_{\alpha} | Total equity of bank α\alpha (net worth) |
| RiR\_{i} | Total production/output of firm ii (proxied by revenues) |
| SiS\_{i} | Total supply/input of firm ii (proxied by cost of materials and services) |
| BiB\_{i} | Total bank loans of firm ii (borrowing from banks) |
| EiE\_{i} | Total equity of firm ii (shareholders’ funds) |
| pip\_{i} | Sector of production of firm ii (NACE2 classification) |
| sp→p′s\_{p\to p^{\prime}} | Input–Output table entry: flow from sector pp to sector p′p^{\prime} (NACE2) |
| ep→p′e\_{p\to p^{\prime}} | Essentiality relation: whether sector pp is an essential input for sector p′p^{\prime} (NACE2) |

Table 1: Variables used in our framework and their economic meaning, at the bank, firm, and industrial sector levels.

### 2.2 Network Reconstruction

The following procedure, derived from constrained maximum entropy arguments augmented by a fitness ansatz [[12](#bib.bib12)], allows defining connection probabilities and weights describing the multilayer bank-firm network.
Such probabilities can be used to generate individual realizations of the multilayer network, i.e., they describe an ensemble of multilayer networks.
The only required input is the balance sheet information described above, which is also preserved on average over the ensemble.

#### 2.2.1 Interbank layer ℬ\cal B

Bank-bank links define the interbank market ℬ\cal B. We denote the amount of the interbank loan from lender bank α\alpha to borrower bank β\beta as wα→βℬw\_{\alpha\to\beta}^{\cal B}.
This is reconstructed through the Density-Corrected Gravity Model (DCGM) [[21](#bib.bib21)] as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wα→βℬ=Aα​LβWℬ​pα→βℬwith probability ​pα→βℬ=zℬ​Aα​Lβ1+zℬ​Aα​Lβw\_{\alpha\to\beta}^{\cal B}=\frac{A\_{\alpha}L\_{\beta}}{W^{\cal B}\>p\_{\alpha\to\beta}^{\cal B}}\qquad\text{with probability\>\>}p\_{\alpha\to\beta}^{\cal B}=\frac{z^{\cal B}A\_{\alpha}L\_{\beta}}{1+z^{\cal B}A\_{\alpha}L\_{\beta}} |  | (1) |

and wα→βℬ=0w\_{\alpha\to\beta}^{\cal B}=0 otherwise.
That is, the loan amount is given by the product of the interbank assets of α\alpha, AαA\_{\alpha}, and interbank liabilities of β\beta, LβL\_{\beta}, normalized by the total weight of layer ℬ\cal B, WℬW^{\cal B}, and the connection probability pα→βℬp\_{\alpha\to\beta}^{\cal B} of the two banks, given by a Logistic function of the same quantities (known as fitness model in network science).
The parameter zℬz^{\cal B} sets the network density (see below), while Wℬ=A​LW^{\cal B}=\sqrt{AL} is the total weight of layer ℬ\cal B, given by the geometric mean of the two total masses A=∑αAαA=\sum\_{\alpha}A\_{\alpha} and L=∑αLαL=\sum\_{\alpha}L\_{\alpha}.
When the system is closed (meaning that the total masses are equal, A≡LA\equiv L),
by construction the model preserves the total interbank assets and liabilities of each bank, as ensemble averages.
For instance, ⟨Aα⟩=∑β⟨wα→βℬ⟩=∑βwα→βℬ​pα→βℬ=Aα​(L/Wℬ)=Aα\langle A\_{\alpha}\rangle=\sum\_{\beta}\langle w\_{\alpha\to\beta}^{\cal B}\rangle=\sum\_{\beta}w\_{\alpha\to\beta}^{\cal B}p\_{\alpha\to\beta}^{\cal B}=A\_{\alpha}(L/W^{\cal B})=A\_{\alpha}. Deviations appear if the system is not closed: ⟨Aα⟩=Aα​L/A\langle A\_{\alpha}\rangle=A\_{\alpha}\sqrt{L/A}.

#### 2.2.2 Bank-firm layer ℐ\cal I

Bank-firm links define the bipartite (inter-layer) corporate relationships ℐ\cal I. The amount of the loan from bank α\alpha to firm ii, denoted as wα→iℐw\_{\alpha\to i}^{\cal I}, is reconstructed through the bipartite version of the DCGM, also known as Enhanced Capital Asset Pricing Model (ECAPM) [[28](#bib.bib28)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wα→iℐ=Cα​BiWℐ​pα→iℐwith probability ​pα→iℐ=zℐ​Cα​Bi1+zℐ​Cα​Biw\_{\alpha\to i}^{\cal I}=\frac{C\_{\alpha}B\_{i}}{W^{\cal I}\>p\_{\alpha\to i}^{\cal I}}\qquad\text{with probability\>\>}p\_{\alpha\to i}^{\cal I}=\frac{z^{\cal I}C\_{\alpha}B\_{i}}{1+z^{\cal I}C\_{\alpha}B\_{i}} |  | (2) |

and wα→iℐ=0w\_{\alpha\to i}^{\cal I}=0 otherwise. As for the DCGM, the loan amount is given by the normalized product of the corporate loans of α\alpha, CαC\_{\alpha}, and bank loans of ii, BiB\_{i}, while the connection probability pα→iℐp\_{\alpha\to i}^{\cal I} is a Logistic function of the same quantities.
As before, the parameter zℐz^{\cal I} sets the network density, while Wℐ=C​BW^{\cal I}=\sqrt{CB} is the total weight of layer ℐ\cal I, given by the geometric mean of the total corporate loans C=∑αCαC=\sum\_{\alpha}C\_{\alpha} and total bank debt B=∑iBi)B=\sum\_{i}B\_{i}).
Again when the system is closed (C≡BC\equiv B),
by construction the model preserves the total corporate loans of each bank and total bank debt of each firm, as ensemble averages.
For instance, ⟨Cα⟩=∑i⟨wα→iℐ⟩=Cα​(B/Wℐ)=Cα\langle C\_{\alpha}\rangle=\sum\_{i}\langle w\_{\alpha\to i}^{\cal I}\rangle=C\_{\alpha}(B/W^{\cal I})=C\_{\alpha}, with deviations occurring if the system is not closed, ⟨Cα⟩=Cα​B/C\langle C\_{\alpha}\rangle=C\_{\alpha}\sqrt{B/C}.

#### 2.2.3 Firm-firm layer ℱ\cal F

Firm-firm links define the production network ℱ\cal F. Reconstructing this layer is more involving than the previous cases, since links are not monetary loans anymore but correspond to purchases of goods and services according to firms’ production processes.
As customarily done in the literature [[16](#bib.bib16), [22](#bib.bib22)], we assume that firms produce outputs only in their own industrial sector. Therefore a link wi→jℱw\_{i\to j}^{\cal F} corresponds to the (monetary) amount of product type pip\_{i} supplied by firm ii to customer firm jj.
The Stripe-Corrected Gravity Model (SCGM) [[16](#bib.bib16)] reconstructs these links as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi→jℱ=Ri​Spi→jWpiℱ​pi→jℱwith probability ​pi→jℱ=zℱ​Ri​Spi→j1+zℱ​Ri​Spi→jw\_{i\to j}^{\cal F}=\frac{R\_{i}S\_{p\_{i}\to j}}{W\_{p\_{i}}^{\cal F}\>p\_{i\to j}^{\cal F}}\qquad\text{with probability\>\>}p\_{i\to j}^{\cal F}=\frac{z^{\cal F}R\_{i}S\_{p\_{i}\to j}}{1+z^{\cal F}R\_{i}S\_{p\_{i}\to j}} |  | (3) |

and wi→jℱ=0w\_{i\to j}^{\cal F}=0 otherwise.
As before the parameter zℱz^{\cal F} sets the total network density, while now the model uses sector-specific normalization Wpiℱ=Rpi​SpiW\_{p\_{i}}^{\cal F}=\sqrt{R\_{p\_{i}}S\_{p\_{i}}},
where Rpi=∑i∈piRiR\_{p\_{i}}=\sum\_{i\in p\_{i}}R\_{i} is the total production of sector pip\_{i} while Spi=∑jSpi→jS\_{p\_{i}}=\sum\_{j}S\_{p\_{i}\to j} is the total supply of firms from sector pip\_{i}.
According to the SCGM formulation, outgoing connections (sales) of firm ii are ruled by its total production RiR\_{i} (all in sector pip\_{i}) while, differently from DCGM, incoming connections (purchases) of firm jj depend on how much input its production process requires from a given sector pp, indicated as Sp→jS\_{p\to j}.
Then when the system is closed for each sector (Rp≡SpR\_{p}\equiv S\_{p} ∀p\forall p), the model preserves the total production of each firm and its total input by sector, as ensemble averages:
⟨Ri⟩=∑j⟨wi→jℱ⟩=Ri\langle R\_{i}\rangle=\sum\_{j}\langle w\_{i\to j}^{\cal F}\rangle=R\_{i}
and ⟨Spi→j⟩=∑i∈pi⟨wi→jℱ⟩=Spi→j\langle S\_{p\_{i}\to j}\rangle=\sum\_{i\in p\_{i}}\langle w\_{i\to j}^{\cal F}\rangle=S\_{p\_{i}\to j}. Deviations in this case read, for instance, ⟨Spi→j⟩=Spi→j​Rpi/Spi\langle S\_{p\_{i}\to j}\rangle=S\_{p\_{i}\to j}\sqrt{R\_{p\_{i}}/S\_{p\_{i}}}.

However, values of the costs by sector Sp→jS\_{p\to j} (how much jj buys from suppliers belonging to sector pp) are not directly available from balance sheet information.
We therefore estimate them using the Input-Output Gravity Model (IOGM) approach [[17](#bib.bib17)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Spi→j=Sj​spi→pj∑psp→pjS\_{p\_{i}\to j}=S\_{j}\frac{s\_{p\_{i}\to p\_{j}}}{\sum\_{p}s\_{p\to p\_{j}}} |  | (4) |

where spi→pjs\_{p\_{i}\to p\_{j}} is the total flux from sector pip\_{i} to sector pjp\_{j} (how much pjp\_{j} requires from pip\_{i}) and ∑psp→pj\sum\_{p}s\_{p\to p\_{j}} is the total incoming flux of sector pjp\_{j} (how much pjp\_{j} requires from all other sectors). These quantities are obtained from Input-Output (IO) tables [[30](#bib.bib30), [31](#bib.bib31)]. In other words, we split the total costs of firm jj across industrial sectors proportionally to what IO tables prescribe.

### 2.3 Shock Propagation and Systemic Risk Metrics

Given a reconstructed network sampled according to the procedure described above, we simulate contagion spreading from the production network layer to the interbank network layer according to the three steps described in detail below:

1. 1.

   Quantify the amount of disruption in the production network after an initial shock, using ESRI dynamics [[22](#bib.bib22)];
2. 2.

   Update the banks’ equity buffers due to non-performing loans to disrupted firms, generalizing FSRI dynamics [[26](#bib.bib26)];
3. 3.

   Propagate credit shocks in the interbank market due to non-performing loans of affected banks, using DR dynamics [[20](#bib.bib20)].

#### 2.3.1 Shocks in the production network: the Economic Systemic Risk Index

The Economic Systemic Risk Index (ESRI) [[22](#bib.bib22)] quantifies the output reduction experienced by the whole production network after an initial production shock hitting one or more firms.
The initial shock is described by a vector ψ\psi, with generic component ψj\psi\_{j} representing the remaining production level of firm jj.
For instance, ψj=0\psi\_{j}=0 and ψi=1\psi\_{i}=1 ∀i≠j\forall i\neq j represents the initial default of firm jj, while other firms remain unaffected.
Shock propagation is then ruled by a generalized Leontief production function: inputs from essential sectors (p∈Essip\in\text{Ess}\_{i}) set a hard constraint on the output of firm ii, while the inputs from non-essential sectors (p∉Essip\notin\text{Ess}\_{i}) are treated in a linear way.
The distinction between essential and non-essential inputs is derived from [[23](#bib.bib23), [32](#bib.bib32)], hence for each pair of sectors pp and p′p^{\prime} we have the sector essentiality relation ep→p′=1e\_{p\to p^{\prime}}=1 if pp is an essential input for p′p^{\prime}, while ep→p′=0e\_{p\to p^{\prime}}=0 otherwise.
We thus have Essi={p:ep→pi=1}\text{Ess}\_{i}=\{p:e\_{p\to p\_{i}}=1\}.

ESRI dynamics is based on the downstream impact matrix, whose element Λj​id\Lambda\_{ji}^{\text{d}} determines the fraction of production firm ii loses if firm jj stops supplying to it:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λj​id={wj→iℱSpj→iif​pj∈Essiwj→iℱSiif​pj∉Essi\Lambda\_{ji}^{\text{d}}=\begin{cases}\frac{w\_{j\to i}^{\cal F}}{S\_{p\_{j}\to i}}\qquad\text{if}\;p\_{j}\in\text{Ess}\_{i}\\ \frac{w\_{j\to i}^{\cal F}}{S\_{i}}\qquad\text{if}\;p\_{j}\notin\text{Ess}\_{i}\end{cases} |  | (5) |

and the upstream impact matrix, whose element Λj​iu\Lambda^{\text{u}}\_{ji} determines the fraction of production firm ii loses if firm jj stops buying from it:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λj​iu=wi→jℱRi\displaystyle\Lambda^{\text{u}}\_{ji}=\frac{w\_{i\to j}^{\cal F}}{R\_{i}} |  | (6) |

After applying the initial shock, downstream and upstream shocks are propagated to any firm ii through two iterative equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hid​(t+1)=min⁡[minp∈Essi⁡(Π~i​p​(t)),Π~i​(t),ψi]h\_{i}^{\text{d}}(t+1)=\min\Big[\min\_{p\in\text{Ess}\_{i}}\Big(\tilde{\Pi}\_{ip}(t)\Big),\;\tilde{\Pi}\_{i}(t),\psi\_{i}\Big] |  | (7) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | hiu​(t+1)=min⁡[∑jΛj​iu​hju​(t),ψi]h^{u}\_{i}(t+1)=\min\Big[\sum\_{j}\Lambda^{\text{u}}\_{ji}h^{\text{u}}\_{j}(t),\psi\_{i}\Big] |  | (8) |

Here tt indicates the time step of the propagation, while hid​(t)h\_{i}^{d}(t) and hiu​(t)h\_{i}^{u}(t) are the residual fraction of production of firm ii at time tt following the propagation of the downstream and upstream shock, respectively, with initial values hid​(0)=hiu​(0)=ψih\_{i}^{d}(0)=h\_{i}^{u}(0)=\psi\_{i}.
The relative amount of essential inputs in sector p∈Essip\in\text{Ess}\_{i} available for firm ii is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π~i​p​(t)=1−∑j∈pσj​(t)​Λj​id​(1−hjd​(t))\tilde{\Pi}\_{ip}(t)=1-\sum\_{j\in p}\sigma\_{j}(t)\Lambda^{d}\_{ji}\big(1-h\_{j}^{\text{d}}(t)\big) |  | (9) |

while the relative share of all non-essential inputs is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π~i​(t)=1−∑p∉Essi∑j∈pnσj​(t)​Λj​id​(1−hjd​(t))\tilde{\Pi}\_{i}(t)=1-\sum\_{p\notin\text{Ess}\_{i}}\sum\_{j\in p}^{n}\sigma\_{j}(t)\Lambda^{d}\_{ji}\big(1-h\_{j}^{\text{d}}(t)\big) |  | (10) |

and firms’ market share, used as a proxy for how replaceable a firm is for its buyers, is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σj​(t)=min⁡(Rj∑l∈pjRl​hld​(t),1)\sigma\_{j}(t)=\min\left(\frac{R\_{j}}{\sum\_{l\in p\_{j}}R\_{l}\,h\_{l}^{d}(t)},1\right) |  | (11) |

After the two, independent shocks of eqs. ([7](#S2.E7 "In 2.3.1 Shocks in the production network: the Economic Systemic Risk Index ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) and ([8](#S2.E8 "In 2.3.1 Shocks in the production network: the Economic Systemic Risk Index ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) have converged at t=t∗t=t^{\*}, the residual fraction of output of firm ii is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(t∗)=min⁡{hid​(t∗),hiu​(t∗)}h\_{i}(t^{\*})=\min\{h\_{i}^{d}(t^{\*}),h\_{i}^{u}(t^{\*})\} |  | (12) |

The ESRI value is then given by the fraction of total production lost in the system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESRI​(ψ)=∑iRi∑jRj​[1−hi​(t∗)]\text{ESRI}(\psi)=\sum\_{i}\frac{R\_{i}}{\sum\_{j}R\_{j}}[1-h\_{i}(t^{\*})] |  | (13) |

#### 2.3.2 Credit shocks to the bank layer: the Financial Systemic Risk Index

The reduced production levels, h​(t∗)h(t^{\*}), correspond to a drop in firms’ revenues and material costs that affects their profits. Reduced profits in turn affect the equity of firms and, eventually, the ability to repay their bank loans – which become non-performing loans (NPL).
Indeed the production reduction of firm ii translates into a reduction of profit as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​πi=max⁡{0,[1−hiu​(t∗)]​Ri−[1−hid​(t∗)]​Si}\Delta\pi\_{i}=\max\left\{0,\Big[1-h\_{i}^{u}(t^{\*})\Big]R\_{i}-\left[1-h\_{i}^{d}(t^{\*})\right]S\_{i}\right\} |  | (14) |

where RiR\_{i} is the revenue and SiS\_{i} the material costs, which are reduced proportionally to the upstream and downstream shocks, respectively
111With this formula we link the reduction in production costs to the downstream shock, i.e. the supply shock, and the reduction in revenues to the upstream, or demand shock. We also take only positive values of Δ​π\Delta\pi. Overall, this is different from the formula Δ​πi=(1−hi​(t∗))​(Ri−Si)\Delta\pi\_{i}=\left(1-h\_{i}(t^{\*})\right)(R\_{i}-S\_{i}) used in [[26](#bib.bib26)]. Additionally, we do not consider the effect of reduced profit on liquidity buffers and potential insolvency of firms..
This causes a direct reduction of firm’s equity: Ei′=max⁡[0,Ei−Δ​πi]E\_{i}^{\prime}=\max[0,\,E\_{i}-\Delta\pi\_{i}].
We then assume that the value of the loan wα→iℐw\_{\alpha\to i}^{\cal I} that bank α\alpha has towards firm ii reduces proportionally to the equity loss of ii:
(wα→iℐ)′=wα→iℐ​(Ei′/Ei)\left(w\_{\alpha\to i}^{\cal I}\right)^{\prime}=w\_{\alpha\to i}^{\cal I}\left(E\_{i}^{\prime}/E\_{i}\right).
Hence when ii has no profit reduction (Δ​πi=0\Delta\pi\_{i}=0) then loans keep their original value, while when the equity of ii becomes 0 (meaning that the firm has defaulted), the entire exposure is written off.
Overall, considering losses from all firms, the reduced equity of bank α\alpha is calculated as Eα′=max⁡{0,Eα−∑i[wα→iℐ−(wα→iℐ)′]}E\_{\alpha}^{\prime}=\max\left\{0,E\_{\alpha}-\sum\_{i}[w\_{\alpha\to i}^{\cal I}-(w\_{\alpha\to i}^{\cal I})^{\prime}]\right\},
so the relative equity loss for bank α\alpha is

|  |  |  |  |
| --- | --- | --- | --- |
|  | hα​(1)=1−Eα′Eα=min⁡{1,1Eα​∑iwα→iℐ​(1−Ei′Ei)}=min⁡{1,∑iwα→iℐEα​min⁡(1,Δ​πiEi)}h\_{\alpha}(1)=1-\frac{E\_{\alpha}^{\prime}}{E\_{\alpha}}=\min\left\{1,\frac{1}{E\_{\alpha}}\sum\_{i}w\_{\alpha\to i}^{\cal I}\left(1-\frac{E\_{i}^{\prime}}{E\_{i}}\right)\right\}=\min\left\{1,\sum\_{i}\frac{w\_{\alpha\to i}^{\cal I}}{E\_{\alpha}}\min\left(1,\>\frac{\Delta\pi\_{i}}{E\_{i}}\right)\right\} |  | (15) |

Differently from [[26](#bib.bib26)], we do not only count banks that default, but quantify the reduction of banks equity due to production shocks of firms.
The overall loss for the banking system is the Financial Systemic Risk Index [[26](#bib.bib26)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | FSRI​(ψ)=∑αEα∑βEβ​hα​(1)\text{FSRI}(\psi)=\sum\_{\alpha}\frac{E\_{\alpha}}{\sum\_{\beta}E\_{\beta}}h\_{\alpha}(1) |  | (16) |

which is the equity-weighted sum of losses suffered by individual banks in the network, and represents the fraction of total bank equity that is lost after the initial shock propagates through the supply chain network, generating NPLs.

#### 2.3.3 Credit shocks in the interbank market: the DebtRank

Finally we use the Debt Rank algorithm (DR) [[29](#bib.bib29), [20](#bib.bib20)] to propagate credit shocks originating from bank losses {h​(1)}\{h(1)\} in the interbank layer. The idea at the basis of DR is that credit shocks propagate also in the absence of defaults, provided that balance sheets are deteriorated: potential losses in the equity of a borrower translate into the devaluation of interbank assets of the corresponding lender.
Losses are then obtained by iteratively spreading the individual banks distress levels weighted by the potential wealth affected.

The level of financial distress
of each bank α\alpha at each time step tt of the shock propagation dynamics is given by the relative change of equity with respect to the original value: hα​(t)=1−Eα​(t)/Eαh\_{\alpha}(t)=1-E\_{\alpha}(t)/E\_{\alpha}.
By definition, hα=0h\_{\alpha}=0 when no equity losses occurred for bank α\alpha, hα=1h\_{\alpha}=1 when that bank defaults, and 0<hα<10<h\_{\alpha}<1 for intermediate distress levels.
In our case the initial shock comes from NPL, thus
hα​(1)=1−Eα′/Eαh\_{\alpha}(1)=1-E\_{\alpha}^{\prime}/E\_{\alpha} as of eq. ([15](#S2.E15 "In 2.3.2 Credit shocks to the bank layer: the Financial Systemic Risk Index ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")).
Subsequent values of hh are obtained by spreading this shock on the interbank layer,
according to the equation describing the evolution of banks equity.
By defining 𝒜​(t)={β:hβ​(t−1)<1}\mathcal{A}(t)=\{\beta:h\_{\beta}(t-1)<1\} as the set of banks that have not defaulted up to time tt (and thus can still spread their financial distress),
we assume that a generic bank β\beta propagates shocks as long as it keeps receiving them, i.e., provided that hβ​(t)>hβ​(t−1)h\_{\beta}(t)>h\_{\beta}(t-1).
We have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hα​(t+1)=min⁡{1,hα​(t)+∑β∈𝒜​(t)wα→βℬEα​[Hβ​(t)−Hβ​(t−1)]}h\_{\alpha}(t+1)=\min\left\{1,\;h\_{\alpha}(t)+\sum\_{\beta\in\mathcal{A}(t)}\frac{w\_{\alpha\to\beta}^{\cal B}}{E\_{\alpha}}\,[H\_{\beta}(t)-H\_{\beta}(t-1)]\right\} |  | (17) |

where Hβ​(t)H\_{\beta}(t) is the probability of default of bank β\beta at time tt.
As in [[33](#bib.bib33)], we assume the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hβ​(t)=hβ​(t)​eη​[hβ​(t)−1]H\_{\beta}(t)=h\_{\beta}(t)e^{\eta[h\_{\beta}(t)-1]} |  | (18) |

where η≥0\eta\geq 0 is a free parameter representing the inverse of the typical relative equity loss after which banks start to propagate distress to their creditors. η\eta allows interpolating between two of the mostly widely used contagion models: η=0\eta=0 leads to the linear DebtRank (where the default probability is the relative equity loss), while η→∞\eta\to\infty recovers contagion-at-default (or Furfine algorithm, where the probability of default is one only if the equity is depleted, and zero otherwise).

The described dynamics stops at t∗t^{\*} when no more banks can propagate their distress, i.e., Hα​(t∗)=Hα​(t∗−1)H\_{\alpha}(t^{\*})=H\_{\alpha}(t^{\*}-1) ∀α\forall\alpha.
The overall DebtRank of the network is then obtained as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​R​(ψ)=∑αEα∑βEβ​hα​(t∗)DR(\psi)=\sum\_{\alpha}\frac{E\_{\alpha}}{\sum\_{\beta}E\_{\beta}}h\_{\alpha}(t^{\*}) |  | (19) |

D​RDR thus represents the amount of equity that is potentially at risk in the system, given an initial shock {hα​(1)}\{h\_{\alpha}(1)\}.
Note that while in our setup DebtRank is a function of the initial shock at the firm level, ψ\psi, we can compute a resilience indicator for individual banks by averaging over different realizations of the initial shock.
We thus define the vulnerability of bank α\alpha as [[34](#bib.bib34)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vα=⟨hα​(t∗|ψ)⟩ψV\_{\alpha}=\langle h\_{\alpha}(t^{\*}|\psi)\rangle\_{\psi} |  | (20) |

where hα​(t∗|ψ)h\_{\alpha}(t^{\*}|\psi) specifies the final value of hh obtained by using ψ\psi as initial condition of the dynamics, and the average is performed over all possible default configurations ψi\psi\_{i} of the chosen setup (see below).

## 3 Data Description

### 3.1 Dataset Construction

We inform the multilayer framework using a proprietary dataset covering Italian banks and firms for the year 2023, compiled from regulatory balance sheets.

Bank data is obtained from the BankFocus database by Bureau van Dijk. We applied 4 filtering steps to select the relevant banks for our analysis: 1) Status: active company; 2) World region: Italy; 3) Specialization: commercial bank, finance company, cooperative bank, savings bank, specialized governmental credit institution, private banking, investment bank; 4) Total assets in 2023 >2 000 000>2\,000\,000€, with the exclusion of companies with no recent financial data and Public authorities. The resulting bank dataset is composed of NB=109N\_{B}=109 Italian banks.

Firm data is obtained through AIDA, Bureau van Dijk’s database of Italian firms. We applied the following filters: 1) Companies who are ultimate owners of their groups; 2) Companies whose NACE2 code is not 64, 65, 66 (financial companies are removed); 3) Total assets for 2023 ≥10 000\geq 10\,000€ and total shareholder’s funds for 2023 ≥1 000\geq 1\,000€. The resulting firm data is composed of NF=7109N\_{F}=7109 Italian firms.

Input-output (IO) table entries {σp→p′}\{\sigma\_{p\to p^{\prime}}\} are obtained from ISTAT (Italian Institute of Statistics)222<https://www.istat.it/tavole-di-dati/il-sistema-di-tavole-input-output-anni-2020-2022/> for the last available year 2022.
Given that we only have a subsample of the Italian economy, we rescale IO entries such that the total output of a sector matches the total revenues of firms in that sector for our data. This means that the factors entering eq. ([4](#S2.E4 "In 2.2.3 Firm-firm layer ℱ ‣ 2.2 Network Reconstruction ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) are computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sp→p′=Rp​σp→p′∑p′′σp→p′′s\_{p\to p^{\prime}}=R\_{p}\frac{\sigma\_{p\to p^{\prime}}}{\sum\_{p^{\prime\prime}}\sigma\_{p\to p^{\prime\prime}}} |  | (21) |

### 3.2 Descriptive Statistics

Tables [A1](#Ax1.T1 "Table A1 ‣ Appendix ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") and [A2](#Ax1.T2 "Table A2 ‣ Appendix ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") in the Appendix report summary statistics (mean, standard deviation, minimum and maximum, skewness) for the balance-sheet variables of our sample that we use to build the multilayer framework, while Figure [2](#S3.F2 "Figure 2 ‣ 3.2 Descriptive Statistics ‣ 3 Data Description ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") reports the corresponding complementary cumulative distribution functions (CCDF).
For all quantities, the distribution shows a power law tail, highlighting the wide heterogeneity of banks and firms: most institutions have intermediate balance sheet figures while a few very large ones dominate the upper tail. This is confirmed by mean values being much higher than median ones, with maximum values being orders of magnitude larger than typical ones. These patterns may suggest that systemic importance is concentrated in a small subset of large banks and firms, with shocks to top-ranked firms potentially dominating aggregate outcomes.
Therefore in the following we will perform sensitivity analyses to examine tail dependence and robustness with respect to the upper end of the distributions.
Note that all CCDFs saturate at relatively high values, since our sample covers only the most capitalized banks and firms in Italy. The only exception is bank debt of firms, which is 0 for about 20% of firms in our sample.

![Refer to caption](2603.09854v1/x2.png)


Figure 2: CCDF of bank variables (A) and firm variables (B) extracted from the balance sheets of our 2023 sample of the Italian economy.

## 4 Results: Reconstructed networks

### 4.1 Density setting and reconstructed degrees

Before running the multilayer network reconstruction framework, we need to specify the three free parameters, zℬz^{\cal B}, zℐz^{\cal I} and zℱz^{\cal F}, which determine the link density of the interbank, bank-firm and interfirm layers, respectively.
As the level of connectivity strongly influences systemic risk properties of the network [[35](#bib.bib35)], we want to set these values properly using empirical measures provided by the literature.
However we must notice that, in real networks, the link density ρ\rho typically scales with the inverse of the number of nodes, ρ∼N−1\rho\sim N^{-1}. This means that we cannot directly use density values taken from empirical studies about networks of different sizes, especially because our network only represents a subset of the Italian economy.
A more reliable quantity is the average node degree ⟨k⟩∼ρ​N\langle k\rangle\sim\rho N, which in principle does not vary with the size of the network. Indeed, in our case it represents the intrinsic capacity of a bank or firm to connect with others, which should not depend on the size of the economy.
We thus proceed as follows.

In the interbank layer, according to eq. ([1](#S2.E1 "In 2.2.1 Interbank layer ℬ ‣ 2.2 Network Reconstruction ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) each bank α\alpha has an average out-degree (number of borrower banks) equal to ⟨kαo​u​t,ℬ⟩=∑βpα→βℬ\langle k\_{\alpha}^{out,\cal B}\rangle=\sum\_{\beta}p\_{\alpha\to\beta}^{\cal B} and and average in-degree (number of lending banks) equal to ⟨kαi​n,ℬ⟩=∑βpβ→αℬ\langle k\_{\alpha}^{in,\cal B}\rangle=\sum\_{\beta}p\_{\beta\to\alpha}^{\cal B}. We thus set zℬz^{\cal B} so that the mean values of these quantities over banks equals 20 [[36](#bib.bib36), [37](#bib.bib37)],
corresponding to a density value of ρB=0.17\rho\_{B}=0.17:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zℬ​ such that ​1NB​∑α⟨kαo​u​t,ℬ⟩≡1NB​∑α⟨kαi​n,ℬ⟩=1NB​∑α≠βpα→βℬ=20z^{\cal B}\mbox{ such that }\frac{1}{N\_{B}}\sum\_{\alpha}\langle k\_{\alpha}^{out,\cal B}\rangle\equiv\frac{1}{N\_{B}}\sum\_{\alpha}\langle k\_{\alpha}^{in,\cal B}\rangle=\frac{1}{N\_{B}}\sum\_{\alpha\neq\beta}p\_{\alpha\to\beta}^{\cal B}=20 |  | (22) |

Similarly in the interfirm layer,
according to eq. ([3](#S2.E3 "In 2.2.3 Firm-firm layer ℱ ‣ 2.2 Network Reconstruction ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) each firm ii has an average out-degree (number of customer firms) equal to ⟨kio​u​t,ℱ⟩=∑jpi→jℱ\langle k\_{i}^{out,\cal F}\rangle=\sum\_{j}p\_{i\to j}^{\cal F} and and average in-degree (number of supplier firms) equal to ⟨kii​n,ℱ⟩=∑jpj→iℱ\langle k\_{i}^{in,\cal F}\rangle=\sum\_{j}p\_{j\to i}^{\cal F}. We set zℱz^{\cal F} so that the mean values of these quantities over firms equals 40 [[38](#bib.bib38)], corresponding to a density value of ρF=0.0054\rho\_{F}=0.0054:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zℱ​ such that ​1NF​∑i⟨kio​u​t,ℱ⟩≡1NF​∑i⟨kii​n,ℱ⟩=1NF​∑i≠jpi→jℱ=40z^{\cal F}\mbox{ such that }\frac{1}{N\_{F}}\sum\_{i}\langle k\_{i}^{out,\cal F}\rangle\equiv\frac{1}{N\_{F}}\sum\_{i}\langle k\_{i}^{in,\cal F}\rangle=\frac{1}{N\_{F}}\sum\_{i\neq j}p\_{i\to j}^{\cal F}=40 |  | (23) |

For the bank-firm layer, according to eq. ([2](#S2.E2 "In 2.2.2 Bank-firm layer ℐ ‣ 2.2 Network Reconstruction ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) each bank α\alpha has an average out-degree (number of borrower firms) equal to ⟨kαo​u​t,ℐ⟩=∑ipα→iℐ\langle k\_{\alpha}^{out,\cal I}\rangle=\sum\_{i}p\_{\alpha\to i}^{\cal I} while each firm has an average in-degree (number of lending banks) equal to ⟨kii​n,ℐ⟩=∑αpα→iℐ\langle k\_{i}^{in,\cal I}\rangle=\sum\_{\alpha}p\_{\alpha\to i}^{\cal I}.
We set zℐz^{\cal I} so that the average firm degree equals 1.8 [[39](#bib.bib39)], corresponding to an average bank degree of 117.5 and a density value of ρF=0.0.016\rho\_{F}=0.0.016:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zℐ​ such that ​1NF​∑i⟨kii​n,ℐ⟩=1NF​∑i,αpi→jℐ=1.8⟹1NB​∑α⟨kαo​u​t,ℐ⟩=117.5z^{\cal I}\mbox{ such that }\frac{1}{N\_{F}}\sum\_{i}\langle k\_{i}^{in,\cal I}\rangle=\frac{1}{N\_{F}}\sum\_{i,\alpha}p\_{i\to j}^{\cal I}=1.8\Longrightarrow\frac{1}{N\_{B}}\sum\_{\alpha}\langle k\_{\alpha}^{out,\cal I}\rangle=117.5 |  | (24) |

Using these values, we can generate independent samples of the multilayer network.
Results presented below are computed as average values over an ensemble of 100 networks.
Figure [3](#S4.F3 "Figure 3 ‣ 4.1 Density setting and reconstructed degrees ‣ 4 Results: Reconstructed networks ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") shows how the reconstruction procedure determines node degrees. Each value is scattered versus the balance sheet quantity that mainly determines it. For instance, the average out-degree of a bank in the interbank layer reads ⟨kαo​u​t,ℬ⟩=∑βpα→βℬ∼Aα\langle k\_{\alpha}^{out,\cal B}\rangle=\sum\_{\beta}p\_{\alpha\to\beta}^{\cal B}\sim A\_{\alpha} at first approximation when AαA\_{\alpha} is small. Analogously, ⟨kαi​n,ℬ⟩∼Lα\langle k\_{\alpha}^{in,\cal B}\rangle\sim L\_{\alpha},
⟨kαo​u​t,ℐ⟩∼Cα\langle k\_{\alpha}^{out,\cal I}\rangle\sim C\_{\alpha}, ⟨kii​n,ℐ⟩∼Bi\langle k\_{i}^{in,\cal I}\rangle\sim B\_{i}, ⟨kio​u​t,ℱ⟩∼Ri\langle k\_{i}^{out,\cal F}\rangle\sim R\_{i}, ⟨kii​n,ℱ⟩∼Si\langle k\_{i}^{in,\cal F}\rangle\sim S\_{i}. Naturally, these linear relationships saturate for large balance sheet values, as connection probabilities cannot grow above one and so degrees are upper-bounded by the number of nodes in the network. Overall, this makes the degree distribution highly skewed with an upper cutoff. Note that for kio​u​t,ℱk\_{i}^{out,\cal F} and kii​n,ℱk\_{i}^{in,\cal F} we observe slightly different trends for the various industrial sectors, which depend on their level of balance (how much RpR\_{p} and SpS\_{p} differ) in a non-linear way.

![Refer to caption](2603.09854v1/x3.png)


Figure 3: Scatter plots of node degrees versus strength used in the reconstruction procedure. Each point represents an individual bank or firm, colored according to their specialization or NACE1 sector, respectively.

### 4.2 Strength conservation

Here, we check whether the reconstruction process is able (as intended) to reproduce balance sheet variables of banks and firms – which we generically refer to as strengths. This validation step is crucial, as it confirms that the reconstructed network retains the key balance-sheet figures necessary for subsequent contagion and systemic-risk dynamics.
Figure [4](#S4.F4 "Figure 4 ‣ 4.2 Strength conservation ‣ 4 Results: Reconstructed networks ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") shows scatter plots of empirical versus reconstructed strength values. Most points, representing individual banks or firms, lay along the identity line, indicating that the method reproduces empirical strengths with high accuracy. Offsets are due to the system not being closed (for instance, reconstructed interbank assets/liabilities are systematically higher/lower than their empirical counterparts), but such deviations are generally small.

![Refer to caption](2603.09854v1/x4.png)


Figure 4: Scatter plots of empirical versus reconstructed strength values, where each point represents an individual bank or firm, while the identity (solid line) serves as a reference for perfect reconstruction. Banks are colored according to their specialization while firms to their NACE1 sector.

## 5 Results: Systemic risk of individual firms

We now discuss simulation results of the shock propagation dynamics on the multilayer network, studying the impact of the failure of individual firms. We thus represent the default of firm jj with the initial condition ψj=0\psi\_{j}=0 and ψi=1\psi\_{i}=1 ∀i≠j\forall i\neq j (all other firms are unaffected).
Given such initial shock, we run ESRI dynamics of eqs. ([7](#S2.E7 "In 2.3.1 Shocks in the production network: the Economic Systemic Risk Index ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) and ([8](#S2.E8 "In 2.3.1 Shocks in the production network: the Economic Systemic Risk Index ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) up to convergence at t∗t^{\*}, then do FSRI dynamics of eq. ([15](#S2.E15 "In 2.3.2 Credit shocks to the bank layer: the Financial Systemic Risk Index ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) and finally run DR dynamics eq. ([17](#S2.E17 "In 2.3.3 Credit shocks in the interbank market: the DebtRank ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) up to convergence at t∗t^{\*}, using the nonlinear formulation with η=2\eta=2 (we avoid using linear propagation otherwise the banking layer suffers overwhelming unrealistic losses).
With this scenario, we measure the overall losses that the failure of a firm would cause to the whole economy, without any mitigation action taken on the system.

### 5.1 Ranking plots

![Refer to caption](2603.09854v1/x5.png)


Figure 5: Ranking plots in terms of systemic risk metrics, with nodes placed in descending order of the corresponding scores.
(A) Ranking based on ESRI scores of firms, where for each firm ii the initial condition is given by its complete production shutdown (ψi=0.0\psi\_{i}=0.0), while all other firms remain active. ESRI of ii thus measures the fraction of total production lost in the interfirm layer through supply-chain contagion, due to the default of ii.
(B) Ranking based on FSRI scores of firms: FSRI of ii measures the fraction of total bank equity lost in the bank-firm layer due to the results of the ESRI dynamics with the same initial condition as before.
(C) Ranking based on DR scores of firms: DR of ii measures the fraction of total bank equity lost in the interbank layer due to the results of the FSRI dynamics with the same initial condition as before.
(D) Ranking based on total systemic risk scores of firms (ESRI+FSRI+DR), highlighting the total impact of firms default on the overall economy.
Total impact of ii thus measures the fraction of total firm production and bank equity lost due to the default of ii, subsequent supply chain contagion, bank loans devaluation and re-evaluation of interbank claims.
(E) Ranking based on vulnerability scores of banks, obtained by averaging over shutdowns of all individual firms as initial conditions. Vulnerability of α\alpha thus measures how much the bank can be affected by economic losses, in terms of equity losses. Marker colors denote bank specialisation.

Figure [5](#S5.F5 "Figure 5 ‣ 5.1 Ranking plots ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")A shows the ranking of individual firms in terms of their ESRI values (the fraction of total production lost in the interfirm network after their initial default).
Similarly to what was found in related studies on empirical production networks [[22](#bib.bib22), [17](#bib.bib17), [40](#bib.bib40)], the ranking curve features an initial region of a handful high-impact firms, with ESRI values close to 1, meaning that their initial collapse can ultimately destroy the entire production of the economy (we recall that we are considering only the most capitalized firms in Italy). The top-5 firms belong to NACE4 sectors 7010 (Business management), 1920 (Manufacture of refined petroleum products), 0910 (Petroleum and natural gas extraction services), 5110 (Air passenger transport) and 3600 (Water production, treatment and supply).
The ranking curve then declines quickly: only about 0.3% of the firms have ESRI larger than 0.1, while the rest of firms have smaller or negligible impact, indicating a strong heterogeneity of the ESRI distribution.

Figure [5](#S5.F5 "Figure 5 ‣ 5.1 Ranking plots ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")B displays firms’ ranking in terms of their FSRI values (the fraction of total bank equity lost in the bank-firm network after their initial default). Again we observe an initial region of high-impact firms, with FSRI up to 0.8. The top-4 firms in this case belong to NACE4 sector 7010 (Business management), while the 5th to NACE4 2910 (Manufacture of motor vehicles). FSRI then quickly declines to negligible values: again only about 0.3% of firms have FSRI larger than 0.1.
Figure [5](#S5.F5 "Figure 5 ‣ 5.1 Ranking plots ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")C finally shows firms’ ranking in terms of their DR values (the fraction of total bank equity lost in the interbank network after their initial default). The initial region of high-impact firms, with DR around 0.8, basically overlaps with that of FSRI. However in this case we see a slower decline towards negligible values, characterized by an additional flat region of medium-impact firms (DR around 0.3).
Indeed, in this case more than 1% of firms have DR larger than 0.1. This signals the presence of many firms whose failure has little impact on the economy but a considerable one on the financial system.

As the three rankings just discussed mostly do not coincide (for instance a firm that ranks top according to ESRI may be in the DR rank tail), in order to assess the overall impact of firms on the multilayer system we rank them according to the sum of their ESRI, FSRI and DR scores. As Figure [5](#S5.F5 "Figure 5 ‣ 5.1 Ranking plots ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")D shows,
top-ranked ESRI firms can have very different impact on the banking sector. While FSRI is close to zero for firms with NACE4 category 3600 and 5110, the other systemically risky firms achieve top overall impact, along with those firms having intermediate ESRI values but large corporate loans, which allow their shock to travel and propagate within the banking sector.

At last, concerning banks’ vulnerability, the rank plot of Figure [5](#S5.F5 "Figure 5 ‣ 5.1 Ranking plots ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")E shows that banks are hardly immune to shocks originating in the interfirm layer. The distribution is not particularly heterogeneous, with most values laying in the range 0.1%-0.4%. Due to their specialization, finance companies typically have the largest values, while the most vulnerable one is a commercial bank (which was placed under extraordinary administration in 2023 after inspections by Bank of Italy).
Other commercial banks, as well as cooperative and savings banks tend to populate the middle of the ranking, while investment and specialized institutions are more prevalent in the lower tail.

### 5.2 Empirical analysis of determinants

After assessing the outcomes of systemic risk dynamics, we now aim at understanding the drivers of the various impact metrics.

#### 5.2.1 ESRI

Important quantities that enter in the computation of the ESRI of firm ii are its revenues RiR\_{i}, production costs SiS\_{i}, market share σi\sigma\_{i} of eq. ([11](#S2.E11 "In 2.3.1 Shocks in the production network: the Economic Systemic Risk Index ‣ 2.3 Shock Propagation and Systemic Risk Metrics ‣ 2 Materials and Methods ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")), industrial sector pip\_{i} and essentiality relations with other sectors {epi→p}\{e\_{p\_{i}\to p}\}, as well as the topology of the production network around it.
We thus estimate a minimal cross-sectional specification for ESRI:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(ESRIi)=γ+β1​log⁡(Θi)+β2​σi+β3​ℰi+εi\log(\mathrm{ESRI}\_{i})=\gamma+\beta\_{1}\log(\Theta\_{i})+\beta\_{2}\sigma\_{i}+\beta\_{3}\mathcal{E}\_{i}+\varepsilon\_{i} |  | (25) |

where Θi=max⁡[Ri,Si]\Theta\_{i}=\max[R\_{i},S\_{i}] measures firm size, while ℰi\mathcal{E}\_{i} is the “essentiality” score of the firm in the economy, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰi=∑jwi→jℱ​Rj​epi→pj∑jwi→jℱ​Rj\mathcal{E}\_{i}=\frac{\sum\_{j}w\_{i\to j}^{\cal F}\,R\_{j}\,e\_{p\_{i}\to p\_{j}}}{\sum\_{j}w\_{i\to j}^{\cal F}\,R\_{j}} |  | (26) |

This index measures the share of downstream economic activity supplied by firm ii that relies on the essential inputs the firm provides. Alternatively, it can be seen as a weighted average of essentiality indicators across customers, where weights reflect the economic importance of the relationship. Hence, the essentiality index is closely related to Bonacich centrality in production networks [[41](#bib.bib41)].

We estimate model ([25](#S5.E25 "In 5.2.1 ESRI ‣ 5.2 Empirical analysis of determinants ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) both by OLS with heteroskedasticity-robust (HC3) standard errors and by quantile regression to explore heterogeneity across the ESRI distribution.
Results, reported in Figure [6](#S5.F6 "Figure 6 ‣ 5.2.1 ESRI ‣ 5.2 Empirical analysis of determinants ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach"), indicate a significant association of ESRI with these variables – the OLS estimates show an extremely high explanatory power (R2=0.979R^{2}=0.979). Firm size has a strong and stable positive effect: the coefficient slightly above one implies that systemic risk increases more than proportionally with firm size. Essentiality and market share also have a positive and highly significant effect in the OLS specification, indicating that firms providing essential inputs and occupying a larger position in their market can affect a greater portion of economic activity.

Quantile regression reveals substantial heterogeneity across the ESRI distribution. While the effect of firm size remains positive and relatively stable across all quantiles, the impact of essentiality and market share increases markedly toward the upper tail. In particular, essentiality is negative or insignificant in the lower quantiles but becomes strongly positive from the median upward, reaching large and highly significant values in the top deciles. A similar pattern is observed for market share, whose effect grows dramatically at higher quantiles of ESRI. In other words, while size is a pervasive driver of systemic exposure, the combination of essential inputs and large market positions acts as a powerful nonlinear amplifier in the upper tail, shaping the concentration of extreme systemic risk.

![Refer to caption](2603.09854v1/x6.png)


Figure 6: Determinants of ESRI for firm-level shocks: Size effects and significance of firm size (A), market share (B) and essentiality score (C) in OLS and quantile regressions of ESRI values.

#### 5.2.2 FSRI

Relevant variables involved in the computation of the FSRI of firm ii are its size Θi\Theta\_{i}, bank loans BiB\_{i}, and the initial shock – proportional to ESRIi and depending also on profit margin μi=max⁡(Ri−Si,0)\mu\_{i}=\max(R\_{i}-S\_{i},0).
Again we expect firm size to be an important determinant of systemic risk. According to the previous analysis, we take ESRI as a proxy of size and observe a very high correlation between FSRI and ESRI values (Figure [7](#S5.F7 "Figure 7 ‣ 5.2.2 FSRI ‣ 5.2 Empirical analysis of determinants ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")A); however, firms with large ESRI can differ by orders of magnitude in FSRI, indicating that financial losses transmitted to banks do depend also on firms exposures.
We therefore estimate the following minimal cross-sectional specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(FSRIi)=γ+β1​log⁡(ESRIi)+β2​(Bi/Θi)+β3​(μi/Θi)+εi\log(\mathrm{FSRI}\_{i})=\gamma+\beta\_{1}\log(\mathrm{ESRI}\_{i})+\beta\_{2}(B\_{i}/\Theta\_{i})+\beta\_{3}(\mu\_{i}/\Theta\_{i})+\varepsilon\_{i} |  | (27) |

where we take ESRI as a proxy of both size and initial shock, while the other two variables are normalized to avoid collinearity with size.
Results, reported in Figure [7](#S5.F7 "Figure 7 ‣ 5.2.2 FSRI ‣ 5.2 Empirical analysis of determinants ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach"),
reveal a strong relationship between FSRI and ESRI. In the OLS specification, with R2=0.935R^{2}=0.935, log\log(ESRI) exhibits a coefficient close to one (1.048) and is highly statistically significant, indicating an almost proportional relationship between the two systemic risk measures: firms that are more systemically relevant in the production network also tend to be more relevant from a financial perspective. The coefficient of profit margin is positive and strongly significant: more profitable firms are more sensitive to the initial shock and tend to exhibit higher financial systemic relevance. By contrast, loans share is not statistically significant in the mean regression.

The quantile regression results provide a more nuanced picture by allowing the relationship to vary across the distribution of FSRI. The coefficients of log\log(ESRI) and profit margin remain remarkably stable while the effect of loans share increases sharply across quantiles: it is insignificant at the 10th percentile, modestly positive around the median, and becomes very large and highly significant in the upper tail of the FSRI distribution. Therefore, bank credit exposure becomes particularly relevant in determining the firms that are highly systemically important.

![Refer to caption](2603.09854v1/x7.png)


Figure 7: Determinants of FSRI for firm-level shocks. Correlation between ESRI and FSRI (A). Size effects and significance of ESRI (B), bank loans (C) and profit margin (D) in OLS and quantile regressions of FSRI values.

![Refer to caption](2603.09854v1/x8.png)


Figure 8: Determinants of DebtRank and bank vulnerability for firm-level shocks. Correlation between DR and FSRI (A) and between vulnerability and corporate loans share (B).

#### 5.2.3 DebtRank and Vulnerability

The situation for the DebtRank case is more involving, as the dynamics is tied to properties of the interbank layer, while here we are considering how firm characteristics trigger and drive DR.
However, as Figure [8](#S5.F8 "Figure 8 ‣ 5.2.2 FSRI ‣ 5.2 Empirical analysis of determinants ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") shows, DR is directly driven by FSRI, with saturation effects as DR approaches the value of one.
Results of the OLS regression of log⁡(DR)\log(\mathrm{DR}) versus log⁡(FSRI)\log(\mathrm{FSRI}) show an almost one-to-one relationship between FSRI and DebtRank (R2=0.997R^{2}=0.997): FSRI alone explains virtually all cross-sectional variation in DebtRank.

Vulnerability instead can be more easily mapped to bank variables. However, as Figure [8](#S5.F8 "Figure 8 ‣ 5.2.2 FSRI ‣ 5.2 Empirical analysis of determinants ‣ 5 Results: Systemic risk of individual firms ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") shows, there is almost perfect correlation between VαV\_{\alpha} and Cα/EαC\_{\alpha}/E\_{\alpha}, namely the proportion of corporate loans over the bank’s equity.
This confirms that corporate loan share alone almost entirely explains the cross-sectional variation in vulnerability (R2=0.986R^{2}=0.986).

## 6 Results: Systemic risk of industrial sectors

We now study the impact of losses stemming from all firms within an industrial sector. Therefore we use as initial condition a 10% production loss for each firm belonging to sector pp, identified at the NACE2 level:
ψj=0.9\psi\_{j}=0.9 if pj=pp\_{j}=p (firm jj belongs to sector pp) and ψi=1\psi\_{i}=1 otherwise (all other firms are unaffected).
Differently from the previous scenario, here we consider a one-step propagation dynamics: we run ESRI for one step (t=1t=1), then do FSRI contagion and finally run DR for one step (t=1t=1), using the linear formulation η=0\eta=0. Hence, in this scenario we study the short-term impact of the initial shock, i.e., the losses that occur before any mitigation action can possibly take place.

Figure [A1](#Ax1.F1 "Figure A1 ‣ Appendix ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") in the Appendix shows the basic balance sheet characteristics of each sector pp:
total size, defined by summing the sizes of firms belonging to it: Θp=∑i∈pΘi\Theta\_{p}=\sum\_{i\in p}\Theta\_{i};
essentiality score, defined by averaging the essentiality index of its firms:
ℰp=⟨ℰi⟩i∈p\mathcal{E}\_{p}=\langle\mathcal{E}\_{i}\rangle\_{i\in p};
total bank loans Bp=∑i∈pBiB\_{p}=\sum\_{i\in p}B\_{i} and
total margin μp=∑i∈pμi\mu\_{p}=\sum\_{i\in p}\mu\_{i}.

### 6.1 Ranking plots

Figure [9](#S6.F9 "Figure 9 ‣ 6.1 Ranking plots ‣ 6 Results: Systemic risk of industrial sectors ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") shows the sector rankings in terms of systemic risk scores, with sectors identified by their NACE Rev. 2 two-digit codes.
Since in each sector we now aggregate firms of different sizes, rankings show less heterogeneity than in the case of individual firms.
The top ESRI value of 0.04 belongs to sectors
69–70 (Legal, accounting, management consultancy and head offices), which is the biggest and most essential overall. Other top sectors, whose decrease of 10% productivity would cause at least a 1% contraction of the whole economy, are:
61 (Telecommunications),
19 (Manufacture of coke and refined petroleum products),
46 (Wholesale trade, except of motor vehicles and motorcycles),
36 (Water collection, treatment and supply),
05–09 (Mining and quarrying support and extraction activities),
35
(Electricity, gas, steam and air conditioning supply).
At the lower tail of the ranking we find sectors
94 (Activities of membership organisations), 03 (Fishing and aquaculture) and 53 (Postal and courier activities – we only have one firm belonging to this sector in our data).

The FSRI and DR rankings reveal that sector 69–70 has an even larger impact on the financial system, due to its high bank loans and profit margin. Indeed, a 10% production contraction in this sector would cause a loss of 25% of the total bank equity.
Other high-impact sectors are
46 (Wholesale trade, except of motor vehicles and motorcycles),
19 (Manufacture of coke and refined petroleum products),
68 (Real estate activities) and
41 (Construction of buildings), but roughly 25% of sectors have DR larger than 0.02.

The stacked ranking plot shows the relative contribution of ESRI, FSRI and DR for each sector (we use logarithmic scale here to highlight the contribution of the different metrics also for all sectors and not just the top-impact ones). With respect to the previous scenario of individual firm defaults, now the initial shock is more broadly distributed, causing network amplification effects especially in the interbank layer (where propagation is now linear).
As a result, bank vulnerability values are about 10 times higher, with most banks above 0.01 and the most vulnerable ones around 0.1 (they lose on average 10% of equity for a 10% production reduction in any NACE2 sector).

![Refer to caption](2603.09854v1/x9.png)


Figure 9: Ranking plots in terms of systemic risk metrics, with nodes placed in descending order of the corresponding scores.
(A) Ranking based on ESRI scores of sectors, where for each sector the initial condition is given by a 10% reduction of production, while all other sectors remain fully active.
(B) Ranking based on FSRI scores of sectors.
(C) Ranking based on DR scores of sectors.
(D) Ranking based on total systemic risk scores of sectors (ESRI+FSRI+DR), quantifying the total impact of 10% production reduction of the sector on the overall economy.
Each bar is decomposed into its economic (ESRI), bank-level (FSRI), and interbank (DebtRank) components, highlighting the relative contribution of each layer to aggregate systemic importance.
(E) Ranking based on vulnerability scores of banks, obtained by averaging over 10% shocks of each sectors firms as initial conditions. Marker colors denote bank specialisation.

### 6.2 Empirical analysis of determinants

#### 6.2.1 ESRI

Repeating the same exercise as above, we estimate a minimal cross-sectional specification for ESRI of sectors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(ESRIp)=γ+β1​log⁡(Θp)+β2​ℰp+εp\log(\mathrm{ESRI}\_{p})=\gamma+\beta\_{1}\log(\Theta\_{p})+\beta\_{2}\mathcal{E}\_{p}+\varepsilon\_{p} |  | (28) |

(now we cannot consider the market share of a sector, which is one by definition).
Regression results (shown in Figure [10](#S6.F10 "Figure 10 ‣ 6.2.1 ESRI ‣ 6.2 Empirical analysis of determinants ‣ 6 Results: Systemic risk of industrial sectors ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) indicate that sector size is again the primary determinant of ESRI, while the role of sector essentiality appears heterogeneous across the distribution of systemic risk. In the OLS specification, the model explains a large share of the variation in ESRI (R2=0.87R^{2}=0.87); the coefficient of log⁡(Θ)\log(\Theta) is close to one and highly significant, while the essentiality index is not: being an essential sector does not systematically increase ESRI once size is controlled for. In the quantile regressions, the elasticity of ESRI with respect to size remains remarkably stable and strongly significant, while the coefficient of essentiality becomes positive and statistically significant in the upper quantiles (0.6 and especially 0.8). Therefore, essential sectors do not necessarily have high impact, except when they are very large.

![Refer to caption](2603.09854v1/x10.png)


Figure 10: Determinants of ESRI for sector-level shocks. Correlation between ESRI and sector size (A). Size effects and significance of sector size (B) and sector essentiality (C) in OLS and quantile regressions of ESRI values.

#### 6.2.2 FSRI

Considering FSRI, Figure [11](#S6.F11 "Figure 11 ‣ 6.2.2 FSRI ‣ 6.2 Empirical analysis of determinants ‣ 6 Results: Systemic risk of industrial sectors ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")A shows the positive correlation with ESRI: sectors that generate large economic losses tend to be more financially damaging, but the mapping is far from one-to-one – due to differences in bank credit exposures.
We therefore estimate the following minimal cross-sectional specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(FSRIp)=γ+β1​log⁡(ESRIp)+β2​(Bp/Θp)+β3​(μp/Θp)+εi\log(\mathrm{FSRI}\_{p})=\gamma+\beta\_{1}\log(\mathrm{ESRI}\_{p})+\beta\_{2}(B\_{p}/\Theta\_{p})+\beta\_{3}(\mu\_{p}/\Theta\_{p})+\varepsilon\_{i} |  | (29) |

Regression results, reported in Figure [11](#S6.F11 "Figure 11 ‣ 6.2.2 FSRI ‣ 6.2 Empirical analysis of determinants ‣ 6 Results: Systemic risk of industrial sectors ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach"), indicate that financial systemic risk is strongly driven by economic systemic relevance, with balance sheet characteristics playing a more limited, heterogeneous role. In the OLS specification, the model explains a substantial fraction of the variation in FSRI (R2=0.73R^{2}=0.73). The coefficient of ESRI is large, positive, and highly significant, with an elasticity close to unity. By contrast, loans share (B/Θ)(B/\Theta) and profit margin (μ/Θ)(\mu/\Theta) are not statistically significant, meaning that, on average, financial exposure and profitability do not systematically affect FSRI once real systemic importance is accounted for.

In the quantile regressions, the coefficient of ESRI remains highly significant and remarkably stable across all quantiles. In contrast, loans share becomes positive and statistically significant from the median quantile onward (0.4, 0.6, and 0.8), indicating that leverage through bank financing contributes to systemic exposure mainly for firms that are already structurally relevant in the economy. Finally, profit margin is never statistically significant and its coefficients fluctuate in sign across quantiles, providing little evidence that firm profitability systematically affects financial systemic importance. Overall, these findings suggest that financial systemic risk largely reflects the economic counterpart, with credit exposures acting as a reinforcing mechanism for firms that are already systemically important.

![Refer to caption](2603.09854v1/x11.png)
  


Figure 11: Determinants of FSRI for sector-level shocks. Correlation between FSRI and ESRI (A). Size effects and significance of ESRI (B), bank loans share (C) and profit margin (D) in OLS and quantile regressions of FSRI values.

#### 6.2.3 DebtRank and Vulnerability

Figure [12](#S6.F12 "Figure 12 ‣ 6.2.3 DebtRank and Vulnerability ‣ 6.2 Empirical analysis of determinants ‣ 6 Results: Systemic risk of industrial sectors ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")A
shows that DR is directly driven by FSRI (R2=1.000R^{2}=1.000),
implying that sectoral DebtRank is nearly a deterministic, proportional amplification of the initial bank-equity losses captured by FSRI. Indeed, FSRI represents the initial condition of the DR dynamics, which in the considered scenario propagates for just one step.

A more interesting picture is provided by bank vulnerability values VαV\_{\alpha}. As Figure [12](#S6.F12 "Figure 12 ‣ 6.2.3 DebtRank and Vulnerability ‣ 6.2 Empirical analysis of determinants ‣ 6 Results: Systemic risk of industrial sectors ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach") shows, vulnerability now is not much driven by corporate loans shares (Cα/EαC\_{\alpha}/E\_{\alpha}), but correlates more with interbank loans shares (Aα/EαA\_{\alpha}/E\_{\alpha}). Indeed, the one-step shock propagation in the interbank layer, driven by AαA\_{\alpha}, is much larger than the initial shock, determined (among other things) by CαC\_{\alpha}.
We therefore estimate the following minimal cross-sectional specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(Vα)=γ+β1​log⁡(Eα)+β2​(Aα/Eα)+β3​(Cα/Eα)+εi\log(V\_{\alpha})=\gamma+\beta\_{1}\log(E\_{\alpha})+\beta\_{2}(A\_{\alpha}/E\_{\alpha})+\beta\_{3}(C\_{\alpha}/E\_{\alpha})+\varepsilon\_{i} |  | (30) |

where we used bank equity EαE\_{\alpha} as a proxy of size, while interbank assets AαA\_{\alpha} and corporate loans CαC\_{\alpha} are normalized to avoid collinearity and to represent leverage values.
Regression results (Figure [12](#S6.F12 "Figure 12 ‣ 6.2.3 DebtRank and Vulnerability ‣ 6.2 Empirical analysis of determinants ‣ 6 Results: Systemic risk of industrial sectors ‣ Modeling structure and credit risk of the economy: a multilayer bank-firm network approach")) suggest that bank vulnerability is primarily driven by leverage rather than size. In the OLS specification, the model explains a substantial share of the variation in vulnerability (R2=0.63R^{2}=0.63), with both interbank exposure and corporate loan exposure being positive and statistically significant. By contrast, bank size, proxied by equity, is not statistically significant: balance sheet scale alone does not systematically determine vulnerability, once leverage ratios are accounted for.

The quantile regressions reveal important heterogeneity across the distribution of vulnerability. The coefficient of interbank share rises steadily from about 0.22 at the 10th percentile to more than 0.41 at the 90th percentile, indicating that interbank exposures play an increasingly dominant role among the most vulnerable banks. Corporate loan exposure also contributes positively across quantiles, though with a smaller and slightly declining effect at higher percentiles. In contrast, equity size shows significance only in the lowest quantile, where it enters with a negative coefficient, indicating that larger capital buffers may reduce vulnerability among the least fragile institutions, but this effect disappears for more vulnerable banks.

![Refer to caption](2603.09854v1/x12.png)


Figure 12: Determinants of DebtRank and bank vulnerability for sector-level shocks. Correlation between DR and FSRI (A), between vulnerability and interbank share (B), between vulnerability and corporate loans share (C).
Size effects and significance of equity (D), interbank loans share (E) and corporate loans share (F) in OLS and quantile regressions of vulnerability values.

## 7 Conclusions

Understanding how shocks propagate between the real economy and the financial system is crucial for assessing systemic risk. Production networks and financial networks are deeply intertwined: disruptions affecting firms propagate through supply chains, reduce revenues, impair loan repayments, and ultimately transmit distress to banks – which are amplified within the interbank market. However, empirical analyses of these mechanisms are typically constrained by the scarcity of detailed network data, since firm-to-firm transactions, credit exposures, and interbank relationships are largely confidential.

This work addresses this limitation by proposing a framework to reconstruct the multilayer structure linking firms and banks using only balance-sheet information. The approach combines reconstruction methods for production, bank–firm credit, and interbank networks into a unified multilayer representation of the economy. On this reconstructed structure, we simulate an ordered contagion mechanism in which shocks propagate from firms through supply chains, generate output losses measured by the Economic Systemic Risk Index (ESRI), translate into credit losses for banks captured by the Financial Systemic Risk Index (FSRI), and subsequently spread within the interbank market through equity deterioration computed by DebtRank (DR).

The illustrative application to the Italian economy highlights several important insights, which are in line with the empirical findings of the literature on network-based contagion. First, systemic importance is highly heterogeneous: only a very small fraction of firms generate large economic losses when they fail, while the vast majority have negligible systemic impact. Second, the firms that are most critical for production are not necessarily the same as those posing the greatest risk to the banking system, indicating that economic and financial systemic importance overlap only partially.
This highlights the importance of considering the full multilayer structure of the economy rather than focusing on a single network layer.
Finally, the empirical analysis of determinants of systemic impact suggests that financial contagion is strongly shaped by network exposures. Firms that are systemically important in the production network tend to generate larger losses for the banking sector, while banks’ vulnerability is largely determined by the composition of their assets, particularly their exposure to interbank lending and corporate loans. These results emphasize the role of network topology and cross-layer linkages in shaping systemic risk.
Furthermore, our framework can be used to simulate different scenarios of initial shocks, as well as to quantify their shot- and long-term impact.
For instance, we showcase a scenario in which all firms within an industrial sector suffer small production losses, and study their immediate effects to the production and financial layers.
In this way, we quantify the losses that occur before any mitigation action can possibly take place on the system.

Overall, our framework demonstrates how multilayer reconstruction can enable network-based stress testing even in the absence of detailed microdata.
From a policy perspective, the framework opens the possibility of constructing data-driven “digital twins” of economic systems that allow regulators to perform integrated stress tests across production and financial networks. Such tools could help identify firms whose disruption would generate disproportionate economic losses, detect banks whose balance-sheet composition makes them particularly exposed to real-economy shocks, and evaluate the systemic consequences of sectoral disruptions. At the same time, there are several directions for future research. Improving network reconstruction techniques, incorporating dynamic firm behavior and adaptive financial responses, and extending the framework to cross-border production and financial networks would allow a more realistic representation of shock propagation.
Ultimately, by bridging production and financial networks within a unified multilayer representation, this work highlights how systemic risk emerges not only from individual institutions but from the architecture of the economic network itself, emphasizing the need for analytical tools capable of capturing the interconnected nature of modern economies.

## Data and Code availability

Codes to reconstruct the multilayer network and run the shock propagation dynamics using sample data are available at
<https://github.com/mnlknt/bank-firm_multilayer_shocks>

## Acknowledgements

We acknowledge financial support from the National Recovery and Resilience Plan (NRRP), Mission 4 Component 2 Investment 1.1, funded by the European Union - NextGenerationEU:
Call for tender No. 1409 of 14/09/2022 by the Italian Ministry of University and Research (MUR), Project Title: *C2T - From Crises to Theory: towards a science of resilience and recovery for economic and financial systems*, Concession Decree No. 1381 of 01/09/2023, Project code P2022E93B8 - CUP E53D23018320001.
Call for tender No. 104 of 02/02/2022 by the Italian Ministry of University and Research (MUR), Project Title: *RENet - Reconstructing economic networks: from physics to machine learning and back*, Concession Decree No. 957 of 30/06/2023, Project code 2022MTBB22 - CUP E53D23001770006;

## References

* Schweitzer *et al.* [2009]
  F. Schweitzer, G. Fagiolo,
  D. Sornette, F. Vega-Redondo, A. Vespignani, and D. R. White, Science 325, 422 (2009).
* Bardoscia *et al.* [2021]
  M. Bardoscia, P. Barucca,
  S. Battiston, F. Caccioli, G. Cimini, D. Garlaschelli, F. Saracco, T. Squartini, and G. Caldarelli, [Nature Reviews Physics 3, 490 (2021)](https://doi.org/10.1038/s42254-021-00322-5).
* Carleton and Hsiang [2016]
  T. A. Carleton and S. M. Hsiang, Science 353, aad9837
  (2016).
* Carvalho *et al.* [2021]
  V. M. Carvalho, M. Nirei,
  Y. U. Saito, and A. Tahbaz-Salehi, The Quarterly
  Journal of Economics 136, 1255 (2021).
* Battiston *et al.* [2017]
  S. Battiston, A. Mandel,
  I. Monasterolo, F. Schütze, and G. Visentin, Nature Climate Change 7, 283 (2017).
* Góes and Bekkers [2022]
  C. Góes and E. Bekkers, arXiv
  preprint arXiv:2203.12173 (2022).
* Pichler *et al.* [2022]
  A. Pichler, M. Pangallo,
  R. M. del Rio-Chanona,
  F. Lafond, and J. D. Farmer, Journal of Economic Dynamics and
  Control 144, 104527
  (2022).
* Acemoglu *et al.* [2015]
  D. Acemoglu, A. Ozdaglar, and A. Tahbaz-Salehi, American Economic
  Review 105, 564
  (2015).
* Fouque and Langsam [2013]
  J.-P. Fouque and J. A. Langsam, *Handbook on systemic
  risk* (Cambridge University Press, 2013).
* Amini *et al.* [2016]
  H. Amini, R. Cont, and A. Minca, Mathematical Finance 26, 329 (2016).
* Hallegatte [2014]
  S. Hallegatte, World bank policy research working paper (2014).
* Cimini *et al.* [2019]
  G. Cimini, T. Squartini,
  F. Saracco, D. Garlaschelli, A. Gabrielli, and G. Caldarelli, [Nature Reviews Physics 1, 58 (2019)](https://doi.org/https://doi.org/10.1038/s42254-018-0002-6).
* Park and Newman [2004]
  J. Park and M. E. Newman, [Physical Review E 70, 066117 (2004)](https://doi.org/https://doi.org/10.1103/PhysRevE.70.066117).
* Squartini and Garlaschelli [2011]
  T. Squartini and D. Garlaschelli, [New Journal of Physics 13, 083001 (2011)](https://doi.org/https//doi.org/10.1088/1367-2630/13/8/083001).
* Anand *et al.* [2018]
  K. Anand, I. Van Lelyveld,
  Á. Banai, S. Friedrich, R. Garratt, G. Hałaj, J. Fique, I. Hansen, S. M. Jaramillo, H. Lee, *et al.*, [Journal of Financial Stability 35, 107 (2018)](https://doi.org/https://doi.org/10.1016/j.jfs.2017.05.012).
* Ialongo *et al.* [2022]
  L. N. Ialongo, C. de Valk,
  E. Marchese, F. Jansen, H. Zmarrou, T. Squartini, and D. Garlaschelli, [Scientific Reports 12, 1 (2022)](https://doi.org/https://doi.org/10.1038/s41598-022-13996-3).
* Fessina *et al.* [2024]
  M. Fessina, G. Cimini,
  T. Squartini, P. Astudillo-Estévez, S. Thurner, and D. Garlaschelli, [Inferring firm-level
  supply chain networks with realistic systemic risk from industry sector-level
  data](https://arxiv.org/abs/2408.02467) (2024), [arXiv:2408.02467 [physics.soc-ph]](https://arxiv.org/abs/2408.02467) .
* Elliott *et al.* [2014]
  M. Elliott, B. Golub, and M. O. Jackson, American Economic
  Review 104, 3115
  (2014).
* Haldane and May [2011]
  A. G. Haldane and R. M. May, Nature 469, 351 (2011).
* Bardoscia *et al.* [2015]
  M. Bardoscia, S. Battiston, F. Caccioli, and G. Caldarelli, PLoS ONE 10, e0130406
  (2015).
* Cimini *et al.* [2015]
  G. Cimini, T. Squartini,
  D. Garlaschelli, and A. Gabrielli, Scientific Reports 5, [https://doi.org/10.1038/srep15758](https://doi.org/https://doi.org/10.1038/srep15758) (2015).
* Diem *et al.* [2022]
  C. Diem, A. Borsos,
  T. Reisch, J. Kertész, and S. Thurner, [Scientific Reports 12, 1 (2022)](https://doi.org/https://doi.org/10.1038/s41598-022-11522-z).
* Pichler *et al.* [2021]
  A. Pichler, M. Pangallo,
  R. M. del Rio-Chanona,
  F. Lafond, and J. D. Farmer, arXiv preprint arXiv:2102.09608 [https://doi.org/10.48550/arXiv.2102.09608](https://doi.org/https://doi.org/10.48550/arXiv.2102.09608) (2021).
* Guth *et al.* [2020]
  M. Guth, C. Lipp, C. Puhr, M. Schneider, *et al.*, Financial Stability Report 40, 63 (2020).
* Borsos and Mero [2020]
  A. Borsos and B. Mero, *Shock propagation in the banking
  system with real economy feedback*, Tech. Rep. (MNB Working Papers, 2020).
* Tabachová *et al.* [2024]
  Z. Tabachová, C. Diem,
  A. Borsos, C. Burger, and S. Thurner, [Journal of Financial Stability 75, 101336 (2024)](https://doi.org/https://doi.org/10.1016/j.jfs.2024.101336).
* Fialkowski *et al.* [2025]
  J. Fialkowski, C. Diem,
  A. Borsos, and S. Thurner, arXiv preprint arXiv:2502.17044 (2025).
* Squartini *et al.* [2017]
  T. Squartini, A. Almog,
  G. Caldarelli, I. van Lelyveld, D. Garlaschelli, and G. Cimini, [Physical Review E 96, 032315 (2017)](https://doi.org/10.1103/PhysRevE.96.032315).
* Battiston *et al.* [2012]
  S. Battiston, M. Puliga,
  R. Kaushik, P. Tasca, and G. Caldarelli, [Scientific Reports 2, 541 (2012)](https://doi.org/10.1038/srep00541).
* Miller and Blair [2009]
  R. E. Miller and P. D. Blair, [*Input-output analysis: foundations and
  extensions*](https://doi.org/https://doi.org/10.1017/CBO9780511626982) (Cambridge university press, 2009).
* Leontief [1986]
  W. Leontief, *Input-output
  economics* (Oxford University Press, 1986).
* Pichler *et al.* [2020]
  A. Pichler, M. Pangallo,
  R. M. del Rio-Chanona,
  F. Lafond, and J. D. Farmer, arXiv preprint arXiv:2005.10585 [https://doi.org/10.48550/arXiv.2005.10585](https://doi.org/https://doi.org/10.48550/arXiv.2005.10585) (2020).
* Bardoscia *et al.* [2016]
  M. Bardoscia, F. Caccioli,
  J. I. Perotti, G. Vivaldo, and G. Caldarelli, [PLoS ONE 11, 1 (2016)](https://doi.org/10.1371/journal.pone.0163825).
* Cimini and Serri [2016]
  G. Cimini and M. Serri, [PLoS ONE 11, e0161642 (2016)](https://doi.org/10.1371/journal.pone.0161642).
* Ramadiah *et al.* [2020]
  A. Ramadiah, D. D. Gangi,
  D. R. L. Sardo, V. Macchiati, T. P. Minh, F. Pinotti, M. Wilinski, P. Barucca, and G. Cimini, [Journal of Network Theory in
  Finance 5, 53 (2020)](https://doi.org/10.21314/JNTF.2019.056).
* Manna and Iazzetta [2009]
  M. Manna and C. Iazzetta, [*The
  topology of the interbank market: developments in Italy since 1990*](https://doi.org/None), Temi di discussione (Economic working papers) 711 (Bank of Italy, Economic Research
  and International Relations Area, 2009).
* Finger *et al.* [2013]
  K. Finger, D. Fricke, and T. Lux, [Computational Management Science 10, 187 (2013)](https://doi.org/10.1007/s10287-013-0171-9).
* Bacilieri *et al.* [2023]
  A. Bacilieri, A. Borsos,
  P. Astudillo-Estevez, and F. Lafond, [*Firm-level production networks: what do we (really) know?*](https://ideas.repec.org/p/amz/wpaper/2023-08.html), Tech. Rep. 2023-08 (INET Oxford Working Paper, 2023).
* De Masi and Gallegati [2012]
  G. De Masi and M. Gallegati, [Empirical Economics 43, 851 (2012)](https://doi.org/10.1007/s00181-011-0512-x).
* Mancini *et al.* [2025]
  A. Mancini, B. Lengyel,
  R. Di Clemente, and G. Cimini, arXiv preprint arXiv:2506.21426 (2025).
* Bonacich [1987]
  P. Bonacich, [American Journal of Sociology 92, 1170 (1987)](https://doi.org/10.1086/228631).

## Appendix

|  | count | mean | median | std | min | max | skew |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Equity | 7109 | 77071 | 12761 | 923788 | 7 | 53644000 | 46 |
| Revenues | 7109 | 147411 | 17745 | 1721131 | 0 | 93717000 | 46 |
| Costs | 7109 | 109876 | 11801 | 1260132 | 0 | 69682000 | 44 |
| Bank debt | 7109 | 23644 | 2528 | 311761 | 0 | 21261000 | 50 |

Table A1: Descriptive statistics for Italian firms dataset (2023). Monetary values in th EUR.



|  | count | mean | median | std | min | max | skew |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total equity | 109 | 2418776 | 428691 | 8334136 | 110087 | 60303223 | 6 |
| Interbank assets | 109 | 3029873 | 196369 | 8503854 | 2 | 51380206 | 4 |
| Interbank liabilities | 109 | 5969979 | 816490 | 15413125 | 5 | 128435415 | 5 |
| Corporate loans | 109 | 6721815 | 1026702 | 23090709 | 2176 | 206761000 | 7 |

Table A2: Descriptive statistics for Italian banks dataset (2023). Monetary values in th EUR.

![Refer to caption](2603.09854v1/Plots_new/sector_plot.png)


Figure A1: Balance sheet properties of the various NACE2 sectors.

BETA