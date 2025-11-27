---
authors:
- Hui Gong
- Akash Sharma
- Francesca Medda
doc_id: arxiv:2511.21515v1
family_id: arxiv:2511.21515
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Quantum Network of Assets: A Non-Classical Framework for Market Correlation
  and Structural Risk'
url_abs: http://arxiv.org/abs/2511.21515v1
url_html: https://arxiv.org/html/2511.21515v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hui Gong
Institute of Finance and Technology, University College London

Akash Sharma
Institute of Finance and Technology, University College London

Francesca Medda
Institute of Finance and Technology, University College London

(November 26, 2025)

###### Abstract

Classical correlation matrices capture only linear and pairwise co-movements, leaving the higher-order, non-linear, and state-dependent interactions of financial markets fundamentally unrepresented. This paper introduces the *Quantum Network of Assets* (QNA), a density-matrix based framework that generalises classical correlation by embedding cross-asset dependencies into a quantum-information representation. The construction does not invoke physical quantum effects; instead, it exploits the mathematical structure of density operators, von Neumann entropy, and quantum mutual information to characterise market organisation at a structural level.

Within this framework, we propose two structural observables: the *Entanglement Risk Index* (ERI), which measures global non-separability and the compression of effective market degrees of freedom, and the *Quantum Early-Warning Signal* (QEWS), which tracks temporal changes in entropy to detect latent information build-up. Both measures reveal dependency geometry inaccessible to covariance-based approaches.

Using NASDAQ–100 data from 2024–2025, we show that quantum entropy exhibits smoother dynamics and sharper regime distinctions than classical entropy, and that ERI rises during periods of structural tightening even when volatility remains subdued. Around the 2025 U.S. tariff announcement, QEWS highlights a pronounced pre-event increase in structural tension followed by an abrupt post-announcement collapse—demonstrating that structural transitions can lead observable price changes without implying predictive modelling.

QNA therefore offers a principled and interpretable extension of correlation analysis, providing structural diagnostics of market fragility, regime shifts, and latent information flow. The framework opens new avenues for systemic risk research by linking empirical asset networks with tools from quantum information theory.

Keywords: quantum finance, entropy, entanglement, systemic risk, early-warning signals.

## 1 Introduction

The covariance matrix and its derived correlation coefficients form the backbone of modern portfolio theory, risk management, and network-based market analysis.
Yet it is increasingly recognised that classical correlation captures only linear and pairwise co-movements, leaving a significant portion of market structure unexplained.
Empirical evidence shows that financial systems exhibit non-linear amplification, clustering of volatility, and rapid regime transitions - behaviours reminiscent of complex, interacting systems rather than collections of independent assets [[9](https://arxiv.org/html/2511.21515v1#bib.bib9)].
During periods of uncertainty or stress, asset interactions become highly concentrated and non-separable in ways that classical statistics cannot fully characterise.

These observations motivate the search for alternative representations of dependency.
Rather than adding incremental sophistication to traditional correlation, this paper adopts a fundamentally different perspective: we embed the market in a quantum-information-inspired framework.
Our aim is *not* to assert that financial markets obey the laws of quantum physics.
Instead, we leverage the mathematical structure of quantum theory-density matrices, entropies, and entanglement measures-to generalise correlation and capture higher-order, multi-scale interactions that become salient under structural stress.

We propose the Quantum Network of Assets (QNA), a representation in which returns are mapped to a quantum density operator and cross-asset dependencies are represented through quantum entropy and quantum mutual information.
By construction, QNA naturally accommodates non-linear coupling, asymmetric dependency, and contextual “state-dependent” interactions, features that classical correlation either suppresses or cannot represent.
This framework further provides a natural language for interpreting market behaviour in terms of superposition-like diversification states, decoherence-like loss of independence, and entanglement-like structural tightness.

Within the QNA framework, we extract two key observables:

* •

  Entanglement Risk Index (ERI) - a measure of cross-asset structural connectivity derived from quantum mutual information.
  High ERI reflects the compression of effective market degrees of freedom, a signature of tightening systemic coupling.
* •

  Quantum Early-Warning Signal (QEWS) - the temporal dynamics of quantum entropy, which highlight transitions between network regimes.
  QEWS is not proposed as a predictive trading indicator, but as a structural lens for detecting periods of rising interdependence.

Our emphasis is therefore structural rather than predictive.
While QNA may exhibit early signals before major market drawdowns, the primary contribution of this work is to show that quantum-information tools reveal aspects of market organisation that classical statistics systematically overlook.
In particular, the presence of non-Markovian coupling, compression of network dimensionality, and rapid entropy shifts suggest an analogy to decohering quantum systems, where measurement or external shocks trigger the collapse of a previously diffuse state into a more rigid structure.

The remainder of this paper demonstrates how QNA is constructed, how ERI and QEWS emerge naturally from the quantum representation, and how these quantities behave in comparison with classical correlation across major market episodes.
We highlight that the quantum view does not replace classical correlation; instead, it generalises it, offering a complementary and often more expressive measure of complexity and dependency in financial networks.

## 2 Theoretical Foundations

### 2.1 From Classical Correlation to Quantum States

Classical correlation matrices capture only the linear co-movement between pairs of assets.
Formally, given demeaned returns ri​(t)r\_{i}(t), the classical correlation between assets ii and jj is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρi​j=𝔼​[ri​rj]𝔼​[ri2]​𝔼​[rj2].\rho\_{ij}=\frac{\mathbb{E}[r\_{i}r\_{j}]}{\sqrt{\mathbb{E}[r\_{i}^{2}]\;\mathbb{E}[r\_{j}^{2}]}}. |  | (1) |

This formulation implicitly makes three assumptions:

1. 1.

   linearity of dependence,
2. 2.

   pairwise separability of interactions,
3. 3.

   time-invariant structure or slow variation.

Financial markets routinely violate all three, particularly during stress, when dependencies become non-linear, clustered, and state-dependent.

Embedding financial returns into a quantum-information representation.

To generalise beyond pairwise correlation, the QNA framework constructs a quantum state from the return vector.
Given a normalised return vector ψ​(t)\psi(t) with components

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψi​(t)=ri​(t)∑j=1Nrj2​(t),\psi\_{i}(t)=\frac{r\_{i}(t)}{\sqrt{\sum\_{j=1}^{N}r\_{j}^{2}(t)}}, |  | (2) |

we define a (pure) quantum state

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ψ​(t)⟩=∑i=1Nψi​(t)​|i⟩.\ket{\psi(t)}=\sum\_{i=1}^{N}\psi\_{i}(t)\ket{i}. |  | (3) |

The associated density matrix is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(t)=|ψ​(t)⟩​⟨ψ​(t)|,\rho(t)=\ket{\psi(t)}\bra{\psi(t)}, |  | (4) |

whose elements are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρi​j​(t)=ψi​(t)​ψj∗​(t).\rho\_{ij}(t)=\psi\_{i}(t)\psi\_{j}^{\*}(t). |  | (5) |

The diagonal terms ρi​i\rho\_{ii} encode marginal risk concentrations, while the off-diagonal terms ρi​j\rho\_{ij} capture structural coherence between assets—an analogue of phase correlations in quantum systems.
These coherence terms do not exist in classical covariance or correlation matrices.

Why density matrices are strictly richer than covariance matrices.

A classical covariance matrix is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σi​j=𝔼​[ri​rj].\Sigma\_{ij}=\mathbb{E}[r\_{i}r\_{j}]. |  | (6) |

It describes only second-moment dispersion.

In contrast, the density matrix ρ\rho contains:

* •

  full amplitude information,
* •

  non-classical coherence terms,
* •

  entropy-based structural complexity.

Following [[10](https://arxiv.org/html/2511.21515v1#bib.bib10)], the density matrix representation gives access to:

* •

  Von Neumann entropy S​(ρ)S(\rho),
* •

  Quantum mutual information I(A:B)I(A\!:\!B),
* •

  Entanglement structure of partitions.

These quantities reveal collective behaviour—compression of degrees of freedom, information synchronisation, and clustering—hidden from classical correlation.

Relation to superposition and entanglement.

The market state ([3](https://arxiv.org/html/2511.21515v1#S2.E3 "In 2.1 From Classical Correlation to Quantum States ‣ 2 Theoretical Foundations ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk")) is a quantum-like superposition:

|  |  |  |
| --- | --- | --- |
|  | |ψ⟩=∑iψi​|i⟩,\ket{\psi}=\sum\_{i}\psi\_{i}\ket{i}, |  |

representing simultaneous participation in multiple “risk states.”
As uncertainty rises, amplitude mass concentrates and off-diagonal coherence increases, producing entanglement-like coupling across subsets of assets.

Quantum mutual information computed on ρ\rho captures this concentration of structure far more sharply than classical correlation, forming the basis for the Entanglement Risk Index (ERI).

### 2.2 Quantum Entanglement in Financial Networks

While QNA does not claim the presence of *physical* quantum entanglement in markets,
the mathematical notion of non-separability provides a powerful analogue.
This follows naturally from the density-matrix formulation developed in Section 2.1.
Once returns are embedded into a quantum state
ρ=|ψ⟩​⟨ψ|\rho=\ket{\psi}\bra{\psi}, the market can be analysed through the structure of its subsystems.

Subsystems and financial partitions.

Let the full market be decomposed into two subsets of assets, AA and BB
(e.g., technology vs. energy; large-cap vs. mid-cap; U.S. vs. global).
From the global density matrix ρA​B\rho\_{AB}, we obtain the reduced states

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρA=TrB​(ρA​B),ρB=TrA​(ρA​B),\rho\_{A}=\mathrm{Tr}\_{B}(\rho\_{AB}),\qquad\rho\_{B}=\mathrm{Tr}\_{A}(\rho\_{AB}), |  | (7) |

using the standard partial-trace operation.

This reduction is well-defined regardless of whether the classical covariance between groups is linear or non-linear.
The key concept is that even if ρA​B\rho\_{AB} is a pure state, ρA\rho\_{A} and ρB\rho\_{B} are in general *mixed*, reflecting the statistical dependence between the two market partitions.

Von Neumann entropy and information concentration.

The von Neumann entropy of a subsystem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(ρ)=−Tr​(ρ​log⁡ρ),S(\rho)=-\mathrm{Tr}(\rho\log\rho), |  | (8) |

measures the degree of uncertainty or effective degrees of freedom.

In a financial setting:

* •

  Higher S​(ρ)S(\rho) implies a dispersed, multi-factor risk structure.
* •

  Lower S​(ρ)S(\rho) indicates concentration of information, often preceding market compression.

Thus, entropy responds to structural features that classical correlation matrices cannot detect—particularly the collapse of independent risk channels into a coherent market mode under stress.

Quantum mutual information and non-separability.

The total amount of information shared between AA and BB is given by the quantum mutual information:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I(A:B)=S(ρA)+S(ρB)−S(ρA​B).I(A:B)=S(\rho\_{A})+S(\rho\_{B})-S(\rho\_{AB}). |  | (9) |

Unlike classical correlation, which captures only linear pairwise co-movement,
the quantum mutual information I(A:B)I(A\!:\!B) responds to a strictly richer set of
dependencies, including:

* •

  non-linear interactions,
* •

  higher-order and collective coupling,
* •

  state-dependent structural changes,
* •

  multi-scale synchronisation across partitions.

When I(A:B)I(A\!:\!B) is large, the market exhibits strong non-separability-precisely the analogue of entanglement in quantum systems.
Following the interpretation of Nielsen and Chuang [[10](https://arxiv.org/html/2511.21515v1#bib.bib10)], I(A:B)I(A\!:\!B) measures the *incompressible information* linking two subsystems.
In finance, this corresponds to the degree to which risks, expectations, or signals propagate jointly across groups of assets.

Financial interpretation of entanglement-like behaviour.

The non-separability quantified by I(A:B)I(A\!:\!B) corresponds to observable financial phenomena:

1. 1.

   Risk-channel compression:
   When multiple sectors begin moving as one, ρ\rho becomes low-rank and entropy S​(ρ)S(\rho) falls.
2. 2.

   Information synchronisation:
   Collective trading behaviour, thematic rotations, or regime switches increase coherence terms and raise I(A:B)I(A\!:\!B).
3. 3.

   Market fragility and systemic coupling:
   Prior to stress events, entanglement-like structure develops as subsystems lose independence.

From this viewpoint, QNA allows us to study financial markets as complex, interacting systems where dependencies cannot be reduced to simple linear correlations.
The mathematical parallels with entanglement provide a rigorous vocabulary for this richer structure.

### 2.3 Bell-Type Correlations (Formal Analogy)

The non-separability exhibited by the QNA is
*formally analogous* to Bell-type correlations that arise in quantum systems.
This analogy is purely mathematical: QNA does not claim any physical
Bell inequality violation in financial markets, nor does it imply microscopic
quantum processes.
Instead, the connection lies in the structural properties of the density matrix,
which encode correlation patterns that cannot be factorized into independent
subsystem components.

Classical factorizability vs. non-separability.

In classical probability theory, a system composed of two parts AA and BB is
*separable* if the joint distribution can be factorized as

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(a,b)=P​(a)​P​(b),P(a,b)=P(a)P(b), |  | (10) |

or, more generally, as a convex mixture of such products.
The financial analogue would be two sets of assets whose risk dynamics remain
independent after conditioning on observable factors.

In contrast, the density matrix formalism allows for joint states ρA​B\rho\_{AB}
that cannot be decomposed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρA​B≠∑kpk​ρA(k)⊗ρB(k).\rho\_{AB}\neq\sum\_{k}p\_{k}\;\rho\_{A}^{(k)}\otimes\rho\_{B}^{(k)}. |  | (11) |

This *non-separability* is the defining feature of quantum entanglement
[[10](https://arxiv.org/html/2511.21515v1#bib.bib10), [8](https://arxiv.org/html/2511.21515v1#bib.bib8)].
In the QNA setting, non-separability signals that the risk structure of one
subset of assets cannot be described without reference to the other—even after
conditioning on classical factors such as volatility or sector exposures.

Formal analogy with Bell-type correlations.

Bell-type inequalities, such as the CHSH inequality, provide a criterion for
testing whether observed correlations can be reproduced by any classical,
local model. The CHSH expression is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ=E​(A1​B1)+E​(A1​B2)+E​(A2​B1)−E​(A2​B2),\mathcal{B}=E(A\_{1}B\_{1})+E(A\_{1}B\_{2})+E(A\_{2}B\_{1})-E(A\_{2}B\_{2}), |  | (12) |

with the classical bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℬ|≤2.|\mathcal{B}|\leq 2. |  | (13) |

Quantum systems can reach 2​22\sqrt{2} due to non-separable state structure.

While financial systems do *not* involve physical measurements,
the QNA density matrix shares a crucial structural feature with
Bell-correlated quantum states:

* •

  correlations arise from the global state ρA​B\rho\_{AB} rather than
  from factorizable local distributions,
* •

  subsystem reductions (ρA\rho\_{A}, ρB\rho\_{B}) become mixed even when
  the global state is pure,
* •

  cross-asset dependencies cannot be expressed through a classical
  covariance model.

These mathematical properties justify the analogy with Bell-type non-classicality,
without implying any violation of physical Bell inequalities.

Interpretation for financial markets.

In market dynamics, non-separability corresponds to situations where:

1. 1.

   Information propagates non-linearly across sectors,
   creating dependencies not reducible to pairwise correlations.
2. 2.

   Expectations synchronize across asset classes prior to
   policy announcements or macro events.
3. 3.

   Risk channels compress, causing previously independent
   components of the market to behave as a single effective mode.

A macroeconomic announcement (e.g., a trade tariff decision) plays the role of a
*measurement* in this analogy.
Prior to the announcement, information is latent and the market reflects a
superposed and non-separable state.
At the moment of disclosure, the system transitions sharply—similar to a
projection in quantum mechanics—revealing the structure encoded in the
pre-announcement density matrix.
The Quantum Early-Warning Signal (QEWS) captures precisely these transitions,
quantifying how the entanglement-like structure evolves prior to observable price
movements.

Summary of the analogy.

The relation between QNA and Bell-type correlations is *strictly formal*:

* •

  QNA does not claim physical entanglement,
* •

  QNA does not violate Bell inequalities,
* •

  The analogy refers to the mathematical structure of non-separability
  in ρ\rho.

This perspective motivates the use of quantum-information tools, such as
von Neumann entropy and quantum mutual information, as natural measures of
cross-asset structural coupling in financial networks.

##### Classical versus quantum structural metrics.

The formal distinction discussed above has direct implications for how market
dependencies are measured. Classical correlation captures only linear
co-movements and therefore represents the “local” limit of the quantum
framework, whereas quantum structural measures such as entropy, mutual
information, and ERI encode non-linear and non-separable dependencies.
Table [1](https://arxiv.org/html/2511.21515v1#S2.T1 "Table 1 ‣ Classical versus quantum structural metrics. ‣ 2.3 Bell-Type Correlations (Formal Analogy) ‣ 2 Theoretical Foundations ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk") summarises the contrast between
the two perspectives.

Table 1: Classical Correlation vs Quantum Structural Measures

| Feature | Classical Correlation | Quantum Entanglement Metrics |
| --- | --- | --- |
| Linear dependence only | Yes | No |
| Captures higher-order structure | No | Yes |
| Sensitivity to latent information | Weak | Strong |
| Response speed to regime shifts | Lagging | Leading / Structural |
| Noise sensitivity | High | Low (spectral smoothing) |
| Systemic-risk indication | Volatility clustering | Entropy / ERI / QEWS tightening |

### 2.4 Measurement, Collapse, and Market Information

Financial markets frequently operate under latent information: policy intentions,
regulatory drafts, macroeconomic assessments, or firm-specific events that are
known to some agents, partially leaked to others, or anticipated by the market as
a whole.
Prior to public disclosure, the market does not evolve toward a single outcome;
instead, it reflects a distribution of possible states, corresponding to
*informational superposition* in the quantum analogy.

Latent information as a mixed or superposed state.

Let the market encode several plausible scenarios
(e.g., tariff increase, policy pause, or stimulus).
Before the official announcement, the QNA density matrix represents a mixed state

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ=∑kpk​|ψk⟩​⟨ψk|,\rho=\sum\_{k}p\_{k}\ket{\psi\_{k}}\bra{\psi\_{k}}, |  | (14) |

where each |ψk⟩\ket{\psi\_{k}} reflects a distinct structural configuration of risk,
correlation, and cross-asset interaction consistent with scenario kk.

From this perspective:

* •

  the off-diagonal elements of ρ\rho encode the *coherence*
  between overlapping scenarios,
* •

  the von Neumann entropy S​(ρ)S(\rho) measures the dispersion of
  informational possibilities,
* •

  quantum mutual information I(A:B)I(A\!:\!B) detects non-separable
  dependencies emerging as agents partially incorporate the latent event.

Macroeconomic announcements as measurement operators.

A major disclosure-such as a central bank decision, fiscal announcement,
geopolitical statement, or trade tariff-acts analogously to a quantum
*measurement operator* MM.
The announcement sharply reduces the set of plausible states, producing

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ⟶M​ρ​M†Tr​(M​ρ​M†),\rho\;\longrightarrow\;\frac{M\rho M^{\dagger}}{\mathrm{Tr}(M\rho M^{\dagger})}, |  | (15) |

formally mirroring the projection postulate of quantum mechanics
(see [[10](https://arxiv.org/html/2511.21515v1#bib.bib10)]).

This transition represents the market’s sudden selection of a specific outcome
among previously latent possibilities.
The structural dependencies encoded in ρ\rho - such as coherence and
entanglement-like coupling across asset groups - are *resolved* or
*collapsed*, producing observable adjustments in prices and correlations.

Quantum-inspired interpretation of pre-event tightening.

In empirical settings, markets often exhibit:

* •

  rising cross-asset coherence,
* •

  narrowing effective degrees of freedom,
* •

  elevated structural coupling across sectors,
* •

  increasing sensitivity to new information.

These phenomena correspond to:

* •

  increasing von Neumann entropy S​(ρ)S(\rho)
  as independent risk channels compress,
* •

  rising quantum mutual information I(A:B)I(A\!:\!B)
  as expectations become synchronised,
* •

  entanglement-like tightening of subsystems
  as the market collectively anticipates an event.

This behaviour mirrors the build-up of coherence and non-separability in a
quantum state prior to measurement.

Collapse and the role of the Quantum Early-Warning Signal.

The Quantum Early-Warning Signal (QEWS) monitors the temporal dynamics of
entropy and mutual information.
When latent information accumulates, ρ\rho becomes increasingly structured, and
QEWS exhibits a *pre-event rise*.
After the announcement, the density matrix collapses to a lower-entropy state,
and QEWS correspondingly drops, reflecting the resolution of uncertainty.

Thus:

* •

  QEWS captures the pre-disclosure tightening of the market,
* •

  the announcement acts as an analogue of a measurement collapse,
* •

  the post-announcement adjustment reflects the projection of
  latent information into realized prices.

This framework offers an intuitive, quantum-inspired perspective on market
transitions, describing how information is gradually entangled across assets
and then suddenly resolved when new information becomes public.

##### Conceptual summary.

The preceding subsections outline the transition from classical correlation-based
representations to quantum-information formulations. To consolidate these ideas,
Table [2](https://arxiv.org/html/2511.21515v1#S2.T2 "Table 2 ‣ Conceptual summary. ‣ 2.4 Measurement, Collapse, and Market Information ‣ 2 Theoretical Foundations ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk") summarises the conceptual differences
between traditional financial network models and the QNA framework.

Table 2: Classical versus Quantum Representations of Financial Networks

| Level | Classical Finance | Quantum Network of Assets |
| --- | --- | --- |
| Basic Unit | Asset | Quantum Node |
| Dependency Type | Correlation ρi​j\rho\_{ij} | Coherence / Entangled Amplitudes |ψi​j⟩|\psi\_{ij}\rangle |
| Structure | Correlation Matrix | Density Matrix ρ\rho |
| Risk Transmission | Covariance Diffusion | Collapse-like Structural Response |
| System Mode | Multi-factor Exposure | Entanglement-driven Dimensionality Compression |

In the next section we formalise these ideas into a rigorous construct, the QNA, and show how density matrices, entropy and mutual information arise naturally once returns are embedded into amplitude states.

## 3 The Quantum Network of Assets (QNA)

### 3.1 Market State as a Density Matrix

In the QNA framework, each financial asset is associated with a normalized
return-amplitude vector, representing its probabilistic behaviour over a chosen
time window.
This mapping embeds the market into a Hilbert space, enabling the use of
quantum-information tools to study structural dependencies.

###### Definition 1 (Return Amplitude Vector).

Let ri​(t)r\_{i}(t) denote the (demeaned and standardized) return series of asset ii
over a rolling window of length TT.
Define the amplitude vector of asset ii as

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ψi⟩=1Zi​[ri​(t1)ri​(t2)⋮ri​(tT)],Zi=∑k=1Tri​(tk)2.\ket{\psi\_{i}}=\frac{1}{\sqrt{Z\_{i}}}\begin{bmatrix}r\_{i}(t\_{1})\\ r\_{i}(t\_{2})\\ \vdots\\ r\_{i}(t\_{T})\end{bmatrix},\qquad Z\_{i}=\sum\_{k=1}^{T}r\_{i}(t\_{k})^{2}. |  | (16) |

This ensures ⟨ψi|ψi⟩=1\braket{\psi\_{i}|\psi\_{i}}=1.

The amplitude construction follows the standard normalization used in quantum
state preparation (see [[10](https://arxiv.org/html/2511.21515v1#bib.bib10)]), and provides a unified
representation for heterogeneous assets.

###### Definition 2 (Market Density Matrix).

Given NN assets with amplitude states
{|ψi⟩}i=1N\{\ket{\psi\_{i}}\}\_{i=1}^{N},
the *market density matrix* is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ=1N​∑i=1N|ψi⟩​⟨ψi|.\rho=\frac{1}{N}\sum\_{i=1}^{N}\ket{\psi\_{i}}\bra{\psi\_{i}}. |  | (17) |

The matrix ρ\rho is Hermitian, positive semidefinite, and satisfies
Tr​(ρ)=1\mathrm{Tr}(\rho)=1, hence forming a valid density operator describing a
statistical ensemble of market states.

###### Lemma 1 (Cross-Asset Coherence).

Let ρ\rho be as in ([17](https://arxiv.org/html/2511.21515v1#S3.E17 "In Definition 2 (Market Density Matrix). ‣ 3.1 Market State as a Density Matrix ‣ 3 The Quantum Network of Assets (QNA) ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk")).
Then its off-diagonal elements satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρj​k=1N​∑i=1Nψi​(j)​ψi​(k),\rho\_{jk}=\frac{1}{N}\sum\_{i=1}^{N}\psi\_{i}(j)\,\psi\_{i}(k), |  | (18) |

which encode higher-order dependence beyond classical covariance.

###### Proof.

Directly expanding |ψi⟩​⟨ψi|\ket{\psi\_{i}}\bra{\psi\_{i}} yields
[|ψi⟩​⟨ψi|]j​k=ψi​(j)​ψi​(k)\left[\ket{\psi\_{i}}\bra{\psi\_{i}}\right]\_{jk}=\psi\_{i}(j)\,\psi\_{i}(k),
and averaging over ii proves ([18](https://arxiv.org/html/2511.21515v1#S3.E18 "In Lemma 1 (Cross-Asset Coherence). ‣ 3.1 Market State as a Density Matrix ‣ 3 The Quantum Network of Assets (QNA) ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk")).
∎

The coherence terms incorporate not only linear comovements, but all
state-dependent interactions arising from the joint behaviour of the amplitude
vectors.

###### Proposition 1 (Classical Correlation as a Special Case).

If all amplitude vectors |ψi⟩\ket{\psi\_{i}} are mutually orthogonal, the density
matrix ρ\rho becomes diagonal, and von Neumann entropy reduces to a classical
Shannon-type entropy.
Thus, classical correlation corresponds to a degenerate special case of QNA
where cross-asset coherence vanishes.

###### Proof.

Orthogonality implies ⟨ψi|ψj⟩=0\braket{\psi\_{i}|\psi\_{j}}=0 for i≠ji\neq j.
Then ([17](https://arxiv.org/html/2511.21515v1#S3.E17 "In Definition 2 (Market Density Matrix). ‣ 3.1 Market State as a Density Matrix ‣ 3 The Quantum Network of Assets (QNA) ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk")) becomes diagonal in the basis
{|ψi⟩}\{\ket{\psi\_{i}}\}, and
S​(ρ)S(\rho) collapses to the Shannon entropy of the eigenvalue distribution,
matching the classical regime.
∎

Interpretation.
The density matrix ρ\rho serves as the fundamental object of the Quantum
Network of Assets.
It captures the entire cross-sectional structure of the market within a single
operator, and its spectral properties describe:

* •

  the effective dimensionality of market behaviour,
* •

  structural concentration or dispersion of systemic risk,
* •

  non-separable, entanglement-like dependencies across assets.

These properties cannot be recovered from classical covariance matrices, making
ρ\rho a strictly richer representation of market structure.

### 3.2 Entropy and Quantum Mutual Information

Entropy and mutual information lie at the core of the QNA,
providing a concise description of the structure, concentration, and evolution of
cross-asset dependencies.
Unlike classical correlation, which only captures second-order comovement,
quantum entropy and quantum mutual information summarize all orders of dependence
encoded in the density matrix.

###### Definition 3 (Von Neumann Entropy).

For a market density matrix ρ\rho, the *quantum entropy* is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(ρ)=−Tr​(ρ​log⁡ρ)=−∑k=1Tλk​log⁡λk,S(\rho)=-\mathrm{Tr}\bigl(\rho\log\rho\bigr)=-\sum\_{k=1}^{T}\lambda\_{k}\log\lambda\_{k}, |  | (19) |

where {λk}\{\lambda\_{k}\} are the eigenvalues of ρ\rho.

Entropy measures the effective dimensionality of market behaviour.
High entropy indicates that several latent market modes are active simultaneously,
reflecting distributed and non-separable interactions.
Low entropy corresponds to more concentrated, synchronized behaviour.

###### Definition 4 (Quantum Mutual Information).

Let the market be partitioned into two subsystems AA and BB with reduced
density matrices ρA\rho\_{A} and ρB\rho\_{B}.
The *quantum mutual information* is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | I(A:B)=S(ρA)+S(ρB)−S(ρA​B).I(A\!:\!B)=S(\rho\_{A})+S(\rho\_{B})-S(\rho\_{AB}). |  | (20) |

Quantum mutual information is strictly non-negative and measures the total
amount of information—classical and quantum—shared between the two
subsystems.
In the financial context, I(A:B)I(A\!:\!B) quantifies the structural dependency between
groups of assets, without assuming linearity or Gaussianity.

Relation to Classical Measures.
If all cross-asset coherence terms vanish, the density matrix becomes diagonal,
and ([19](https://arxiv.org/html/2511.21515v1#S3.E19 "In Definition 3 (Von Neumann Entropy). ‣ 3.2 Entropy and Quantum Mutual Information ‣ 3 The Quantum Network of Assets (QNA) ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk")) reduces to Shannon entropy while
([20](https://arxiv.org/html/2511.21515v1#S3.E20 "In Definition 4 (Quantum Mutual Information). ‣ 3.2 Entropy and Quantum Mutual Information ‣ 3 The Quantum Network of Assets (QNA) ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk")) collapses to classical mutual information.
Thus, classical correlation emerges as a limiting case where market interactions
are fully separable.

Interpretation in QNA.
Within the Quantum Network of Assets:

* •

  S​(ρ)S(\rho) summarises the *overall structural complexity* of the market,
* •

  S​(ρ)S(\rho) dynamics identify periods of structural tightening or dispersion,
* •

  I(A:B)I(A\!:\!B) captures *cross-sector information flow* and
  multi-scale integration,
* •

  both metrics remain valid even when correlations are unstable or non-linear.

The joint use of S​(ρ)S(\rho) and I(A:B)I(A\!:\!B) provides a structural, model-free
characterization of market behaviour that cannot be replicated with
covariance-based tools.

### 3.3 Quantum Index and Entanglement Risk Index (ERI)

Beyond entropy and mutual information, the QNA produces a
scalar measure summarizing the overall strength of non-classical structural
dependencies.
This quantity, which we term the *Entanglement Risk Index (ERI)*, captures
the aggregate level of non-separability encoded in the market density matrix.

###### Definition 5 (Quantum Index).

Let ρ\rho be the market density matrix constructed from return amplitudes.
Define the *Quantum Index* as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(t)=Tr​(ρ​(t)2),Q(t)=\mathrm{Tr}\!\bigl(\rho(t)^{2}\bigr), |  | (21) |

which is the purity of the market state at time tt.

Purity ranges between:

|  |  |  |
| --- | --- | --- |
|  | 1T≤Q​(t)≤1,\frac{1}{T}\leq Q(t)\leq 1, |  |

where TT is the dimension of the market Hilbert space.
Smaller purity implies greater mixing and stronger structural integration across
assets.
Thus, 1−Q​(t)1-Q(t) naturally measures the *degree of structural entanglement*.

###### Definition 6 (Entanglement Risk Index (ERI)).

The *Entanglement Risk Index* is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ERI​(t)=1−Tr​(ρ​(t)2)=1−Q​(t),\mathrm{ERI}(t)=1-\mathrm{Tr}\!\bigl(\rho(t)^{2}\bigr)=1-Q(t), |  | (22) |

which is maximized when market structure is most non-separable.

ERI provides a model-free, scalar indicator of structural tightness in the
market network.
High ERI corresponds to:

* •

  strong non-linear cross-asset coupling,
* •

  dense information-sharing across sectors,
* •

  reduced effective dimensionality of market behaviour.

Relationship to von Neumann Entropy.
Entropy and ERI are closely related:

* •

  ERI captures *instantaneous* structural entanglement
  via quadratic mixing,
* •

  von Neumann entropy captures *global* structural complexity
  via spectral dispersion.

Both coincide for maximally mixed states:

|  |  |  |
| --- | --- | --- |
|  | ERI​(t)​ high ⟺S​(ρ​(t))​ high,\mathrm{ERI}(t)\text{ high }\quad\Longleftrightarrow\quad S(\rho(t))\text{ high}, |  |

but ERI reacts more sensitively to changes in the largest eigenvalues of ρ\rho,
making it a sharper proxy for systemic tightening.

Interpretation in Financial Networks.
In the QNA framework:

* •

  upward shifts in ERI indicate tightening systemic structure,
* •

  persistently high ERI reflects strong latent co-movement pressure,
* •

  turning points in ERI often precede shifts in volatility or drawdowns.

Thus, ERI plays a role analogous to “structural stress” in complex systems,
quantifying the build-up of market-wide integration beyond linear correlation.

### 3.4 Quantum Early-Warning Signal (QEWS)

While the Entanglement Risk Index (ERI) captures the instantaneous structural
tightness of the market network, it is the *temporal evolution* of
entanglement that reveals transitions in market configuration.
We therefore define the *Quantum Early-Warning Signal (QEWS)* as a
time-local measure of structural change in entropy or entanglement.

###### Definition 7 (Quantum Early-Warning Signal).

Let S​(t)S(t) be the von Neumann entropy of the market state at time tt, and let
ERI​(t)\mathrm{ERI}(t) be the entanglement risk index.
The *Quantum Early-Warning Signal (QEWS)* is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | QEWS​(t)=S​(t)−μS​(t)σS​(t),\mathrm{QEWS}(t)=\frac{S(t)-\mu\_{S}(t)}{\sigma\_{S}(t)}, |  | (23) |

or equivalently

|  |  |  |  |
| --- | --- | --- | --- |
|  | QEWSERI​(t)=ERI​(t)−μERI​(t)σERI​(t),\mathrm{QEWS}\_{\mathrm{ERI}}(t)=\frac{\mathrm{ERI}(t)-\mu\_{\mathrm{ERI}}(t)}{\sigma\_{\mathrm{ERI}}(t)}, |  | (24) |

where μS​(t)\mu\_{S}(t) and σS​(t)\sigma\_{S}(t) (respectively
μERI​(t)\mu\_{\mathrm{ERI}}(t), σERI​(t)\sigma\_{\mathrm{ERI}}(t)) denote the
local mean and local standard deviation computed over a rolling
window of length ww.

The standardized form ensures that QEWS reflects *structural deviations*
rather than absolute levels of entropy or ERI.
Large values of QEWS indicate unusual tightening of the market’s informational
state relative to recent history.

##### Interpretation.

QEWS is not a forecasting model; it does not aim to predict returns or
volatility.
Instead, it captures:

* •

  the accumulation of latent information in the market,
* •

  the tightening of structural dependencies prior to a disclosure event,
* •

  the non-linear co-movement pressure arising from hidden coupling.

In the quantum-information analogy, QEWS corresponds to the build-up of
non-separability in the market state prior to a “measurement”—such as a
policy announcement, earnings report, or macroeconomic shock.
Empirically, QEWS tends to rise during periods when:

* •

  uncertainty is high but unresolved,
* •

  cross-asset dependencies become more synchronized,
* •

  the market configuration approaches a structural transition.

After major announcements, entropy typically undergoes a sharp relaxation,
analogous to a post-measurement collapse of the informational state.
This produces a characteristic QEWS profile: a gradual rise preceding the event
and a sudden drop immediately afterward.

##### Relation to Classical Indicators.

Classical correlation matrices lack temporal sensitivity to structural
tightening—they change only when realized co-movements change.
In contrast:

* •

  QEWS responds to latent structural transitions,
* •

  QEWS can rise even while prices trend upward,
* •

  QEWS identifies hidden entanglement buildup invisible to correlation.

Thus, QEWS provides a complementary structural dimension to the analysis of
market stability.

## 4 Data and Implementation

This study employs all available NASDAQ–100 constituents, using daily prices and
volumes from January 2024 to November 2025.
The objective is not forecasting but the reconstruction of a quantum-inspired
market state and the extraction of structural indicators from it.

A rolling window of 60 trading days is used throughout the analysis, allowing
the density matrix and its associated quantities to evolve smoothly over time.
The implementation consists of a sequence of well-defined stages, each
corresponding directly to a conceptual layer of the QNA framework.

### 4.1 Pipeline Overview

The entire workflow may be summarized by the following dataflow structure:

|  |  |  |
| --- | --- | --- |
|  | Raw Market Data↓Feature Extraction↓Amplitude Construction↓Density Matrix Estimation↓{Entropy,Mutual Information,ERI,QEWS}\begin{array}[]{c}\text{Raw Market Data}\\ \downarrow\\ \text{Feature Extraction}\\ \downarrow\\ \text{Amplitude Construction}\\ \downarrow\\ \text{Density Matrix Estimation}\\ \downarrow\\ \{\text{Entropy},\ \text{Mutual Information},\ \text{ERI},\ \text{QEWS}\}\end{array} |  |

Figure 1: QNA Processing Pipeline: From raw data to quantum structural indicators

Each block corresponds to a specific computational stage, described below.

#### Step 1: Data Preprocessing

For each NASDAQ–100 constituent, we collect:

* •

  daily closing price,
* •

  daily trading volume,
* •

  derived log returns,
* •

  rolling volatility estimates.

All time series are aligned to a common business-day calendar.
Missing observations are forward-filled when appropriate and otherwise excluded
from the rolling window.

#### Step 2: Construction of Feature Vectors

Each asset ii at time tt is represented by a feature vector:

|  |  |  |
| --- | --- | --- |
|  | xi​(t)=(ri​(t),σi​(t),vi​(t),Δ​vi​(t)),x\_{i}(t)=\bigl(r\_{i}(t),\;\sigma\_{i}(t),\;v\_{i}(t),\;\Delta v\_{i}(t)\bigr), |  |

where ri​(t)r\_{i}(t) is the log return, σi​(t)\sigma\_{i}(t) the rolling volatility,
vi​(t)v\_{i}(t) the raw volume, and Δ​vi​(t)\Delta v\_{i}(t) a volume-acceleration proxy.
These features embed not only co-movement but also liquidity and activity
characteristics that influence the market’s structural state.

#### Step 3: Amplitude Vector Construction

To construct quantum-inspired state vectors, each feature vector is normalized:

|  |  |  |
| --- | --- | --- |
|  | |ψi​(t)⟩=xi​(t)‖xi​(t)‖,|\psi\_{i}(t)\rangle=\frac{x\_{i}(t)}{\|x\_{i}(t)\|}, |  |

which ensures that all assets lie on the unit hypersphere.
This step transforms heterogeneous financial features into comparable
probability-amplitude representations without imposing linearity assumptions.

#### Step 4: Density Matrix Estimation

Given the set of normalized amplitude vectors at time tt, the market state is
estimated as the empirical density matrix:

|  |  |  |
| --- | --- | --- |
|  | ρ​(t)=1N​∑i=1N|ψi​(t)⟩​⟨ψi​(t)|,\rho(t)=\frac{1}{N}\sum\_{i=1}^{N}|\psi\_{i}(t)\rangle\langle\psi\_{i}(t)|, |  |

where NN is the number of available assets on that date.
This matrix encodes cross-asset coherence through its off-diagonal elements and
serves as the central object from which all QNA observables are derived.

#### Step 5: Entropy and Mutual Information

The eigenvalue spectrum of the density matrix provides:

* •

  von Neumann entropy
  S​(t)=−Tr​(ρ​(t)​log⁡ρ​(t)),S(t)=-\mathrm{Tr}(\rho(t)\log\rho(t)),
* •

  quantum mutual information between asset subsets,
* •

  measures of spectral concentration and dispersion.

These quantities capture structural complexity and non-separability beyond what
classical correlation matrices can represent.

#### Step 6: Entanglement Risk Index (ERI)

The Entanglement Risk Index is computed from the purity:

|  |  |  |
| --- | --- | --- |
|  | ERI​(t)=1−Tr​(ρ​(t)2),\mathrm{ERI}(t)=1-\mathrm{Tr}\!\bigl(\rho(t)^{2}\bigr), |  |

summarizing the degree of structural entanglement in the market network.
Higher ERI indicates tighter systemic configuration and stronger cross-asset
integration.

#### Step 7: Quantum Early-Warning Signal (QEWS)

Finally, the temporal standardized deviation of entropy or ERI produces:

|  |  |  |
| --- | --- | --- |
|  | QEWS​(t)=ERI​(t)−μERI​(t)σERI​(t),\mathrm{QEWS}(t)=\frac{\mathrm{ERI}(t)-\mu\_{\mathrm{ERI}}(t)}{\sigma\_{\mathrm{ERI}}(t)}, |  |

which highlights latent structural transitions.
QEWS rises during periods of informational buildup and relaxes sharply
after major announcements or regime shifts.

### 4.2 Implementation Environment

All computations are carried out in Python using:

* •

  numpy for numerical operations,
* •

  pandas for time-series processing,
* •

  custom QNA functions for density matrices and entropy,
* •

  matplotlib for visualization.

The codebase is modular, with separate routines for data handling, amplitude
construction, density estimation, and structural metric computation.
This modular structure enables straightforward extension to other markets, higher
frequency data, or alternative feature sets.

## 5 Empirical Results

### 5.1 Network Summary Metrics (Quantum–Financial Interpretation)

To understand the structural differences between classical and quantum
representations, we compute a set of information, stability, and risk metrics
summarizing the behaviour of the market network.
What differentiates QNA from classical correlation is that each metric admits
both a *quantum-information interpretation* and a concrete *financial
market interpretation*.
Below we discuss these metrics jointly with their empirical values.

##### 1. Information Content (Entropy).

Quantum entropy is substantially higher than classical entropy
(Sclassical=2.81S\_{\text{classical}}=2.81, Squantum=3.33S\_{\text{quantum}}=3.33).

Quantum meaning.
Von Neumann entropy measures the “mixedness” of the density matrix, i.e., how
many distinguishable micro-configurations of the market state coexist.
A higher quantum entropy indicates richer latent structure and stronger
non-linear dependence, similar to a quantum system with more interfering
pathways.

Financial meaning.
The market contains multiple competing narratives and interacting risk channels.
Quantum entropy acts as a measure of *structural complexity*, capturing
dependencies missed by covariance-based correlation.
High entropy corresponds to markets where information is tightly interwoven—
typically ahead of major announcements or during stressed periods.

##### 2. Predictive Proxies (Associations with Realized Risk).

Structural indices correlate with realized volatility and future drawdown.
Classical correlations with volatility are stronger (0.59 vs. 0.52), while
quantum indices exhibit weaker association with short-term risk.

Quantum meaning.
The quantum index is a global observable derived from the spectrum of ρ\rho.
It integrates the entire cross-sectional configuration rather than local
pairwise variance.
This is analogous to a many-body observable that tracks system configuration
rather than local particle fluctuations.

Financial meaning.
Classical correlation reacts strongly to volatility spikes, but often mixes
signal and noise.
Quantum structure reflects *systemic reconfiguration*, which may not align
with 30-day realized volatility but captures deeper structural tightening—
consistent with pre-event information build-up.

##### 3. Stability of the Structural Index.

The quantum structural index exhibits markedly lower standard deviation
(σquantum=0.034\sigma\_{\text{quantum}}=0.034 vs. σclassical=0.107\sigma\_{\text{classical}}=0.107)
while retaining high persistence (ACF1: 0.987 vs. 0.994).

Quantum meaning.
The density matrix smooths out high-frequency noise because quantum amplitudes
encode normalized probability flow rather than raw fluctuations.
The resulting eigenvalues evolve gradually, much like low-energy modes in a
quantum Hamiltonian.

Financial meaning.
Markets contain microstructure noise and short-lived shocks that distort
classical correlation.
The QNA filters these transients automatically, isolating the
slow-moving structural backbone of market dependency—precisely the
part relevant for regime detection, diversification, and systemic risk.

##### 4. Risk Regimes and Structural Separation.

Entropy-based regime classification shows clearer structural contrast under the
quantum representation.
Classical indices drop from 0.320.32 (low entropy) to 0.220.22 (high entropy),
while quantum indices shift from 0.0390.039 to 0.0040.004 with far smaller noise.

Quantum meaning.
High quantum entropy corresponds to a more mixed density matrix, indicating
greater entanglement-like cross-asset dependence.
Such a state is harder to separate and signals reduced degrees of freedom—
analogous to constrained dynamics in a quantum network.

Financial meaning.
When entropy is high, the market behaves as a tightly coupled system with fewer
independent risk channels.
Diversification becomes less effective, correlations tighten, and systemic risk
rises.
Quantum metrics reveal this contraction more cleanly because they emphasize
global configuration instead of noisy pairwise movements.

##### Summary interpretation.

As shown in Table [3](https://arxiv.org/html/2511.21515v1#S5.T3 "Table 3 ‣ Summary interpretation. ‣ 5.1 Network Summary Metrics (Quantum–Financial Interpretation) ‣ 5 Empirical Results ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk"), the classical index is
closely tied to realised volatility and responds only after price-based
stress materialises, reflecting its reliance on linear co-movements.

Table 3: Summary of Empirical Differences Between Classical and Quantum Network Metrics

| Property | Classical Index | Quantum Index / QEWS | Interpretation |
| --- | --- | --- | --- |
| Structural sensitivity | Low | High | Quantum reacts to latent structural tension |
| Response speed | Lagging | Leading (structural) | Structure changes precede price changes |
| Higher-order dependence | No | Yes | Captures multi-scale coupling beyond correlation |
| Noise robustness | Low | High | Density matrix smooths microstructure noise |
| Regime separation | Weak | Strong | Clear entropy/ERI transitions across regimes |
| Relation to volatility | Strongly tied | Weakly tied | Quantum reacts to structure, not price dynamics |
| Systemic-risk signal | Volatility clustering | Entropy / ERI / QEWS tightening | Early tension buildup |

In contrast, the quantum index and QEWS respond to changes in the
*structural geometry* of the market—tightening of dependencies,
dimensionality compression, and coherence buildup. These quantum metrics
exhibit richer informational structure, smoother and less noisy evolution,
and clearer separation of systemic regimes. Their reduced sensitivity to
short-term price fluctuations allows structural shifts to appear earlier
in the quantum metrics than in classical ones.

Taken together, these properties make QNA a meaningful extension of
classical correlation, capable of capturing the latent, higher-order
informational geometry of financial markets and framing the empirical
analysis that follows.

### 5.2 Classical vs Quantum Entropy

##### Classical vs quantum structural properties.

Before examining Figure [2](https://arxiv.org/html/2511.21515v1#S5.F2 "Figure 2 ‣ Classical vs quantum structural properties. ‣ 5.2 Classical vs Quantum Entropy ‣ 5 Empirical Results ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk"), it is useful to summarise the
conceptual differences between classical correlation measures and the
quantum structural metrics used in QNA. Table [4](https://arxiv.org/html/2511.21515v1#S5.T4 "Table 4 ‣ Classical vs quantum structural properties. ‣ 5.2 Classical vs Quantum Entropy ‣ 5 Empirical Results ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk")
highlights these contrasts.

Table 4: Classical Correlation vs Quantum Structural Measures

| Feature | Classical Correlation | Quantum Entanglement Metrics |
| --- | --- | --- |
| Linear dependence only | Yes | No |
| Captures higher-order structure | No | Yes |
| Sensitivity to latent information | Weak | Strong |
| Response speed to regime shifts | Lagging | Leading / Structural |
| Noise sensitivity | High | Low (spectral smoothing) |
| Systemic-risk indication | Volatility clustering | Entropy / ERI / QEWS tightening |

This conceptual contrast frames the empirical behaviour observed in
Figure [2](https://arxiv.org/html/2511.21515v1#S5.F2 "Figure 2 ‣ Classical vs quantum structural properties. ‣ 5.2 Classical vs Quantum Entropy ‣ 5 Empirical Results ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk"): quantum entropy reacts not to price
co-movements but to deeper structural tension in the market network.

Figure [2](https://arxiv.org/html/2511.21515v1#S5.F2 "Figure 2 ‣ Classical vs quantum structural properties. ‣ 5.2 Classical vs Quantum Entropy ‣ 5 Empirical Results ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk") compares the evolution of classical entropy and quantum entropy
for the NASDAQ–100 network between 2024 and 2025. While both measures quantify
structural complexity, quantum entropy exhibits substantially higher sensitivity,
smoother dynamics, and clearer regime separation. These differences are essential
for understanding how market dependencies evolve under latent information flow.

![Refer to caption](x1.png)


Figure 2: Classical vs Quantum Entropy (NASDAQ 100 Network)

##### Quantum-information interpretation.

In the QNA framework, von Neumann entropy (Equation [19](https://arxiv.org/html/2511.21515v1#S3.E19 "In Definition 3 (Von Neumann Entropy). ‣ 3.2 Entropy and Quantum Mutual Information ‣ 3 The Quantum Network of Assets (QNA) ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk"))
measures the degree of *non-separability* of the market state. Higher quantum entropy
indicates that the joint density matrix ρ\rho contains stronger coherence terms,
representing richer higher-order interactions and multi-scale information sharing across assets.
This matches the intuition from quantum information theory: the more entangled and
non-separable the system, the higher its entropy.

Across the entire sample, quantum entropy (orange curve) consistently lies above
classical entropy (blue curve), revealing that:

* •

  market dependencies contain substantial non-linear and higher-order structure,
* •

  a significant component of cross-asset behaviour arises from shared latent information,
* •

  the effective dimensionality of the market contracts under stronger entanglement.

##### Financial-market interpretation.

In financial terms, rising quantum entropy reflects structural tightening—a state in
which assets increasingly respond to common information, sectoral dynamics become
synchronized, and diversification capacity weakens. This tightening implies:

* •

  increased systemic concentration risk,
* •

  fragility induced by alignment of investor expectations,
* •

  reduced independence among market components.

Two episodes in particular illustrate how quantum entropy captures structural stress before
it manifests in volatility or returns:

* •

  September–November 2024:
  Quantum entropy exhibits a pronounced upward spike while classical entropy remains flat.
  This period corresponds to heightened uncertainty surrounding trade policy discussions,
  shifting Fed expectations, and rotation across technology and AI-related sectors.
  The spike indicates that cross-asset dependencies tightened significantly even though
  realized volatility remained low.
* •

  Late 2024 to early 2025:
  Multiple “entropy spikes” occur during a period when the market index continued rising.
  These patterns signal latent build-up of systemic tension—a form of “entanglement
  compression”—that classical entropy does not detect.
  Such behaviour is consistent with speculative concentration and synchronous
  positioning across sectors.

In both episodes, classical entropy responds only after structural changes become visible in
realized volatility, whereas quantum entropy reacts to *pre-volatility structural drift*.
This demonstrates quantum entropy’s ability to detect shifts in dependency geometry that
precede price-based indicators.

##### Structural implication.

Quantum entropy is not intended as a forecasting tool for returns. Instead, it serves as a
quantum-information structural probe capable of revealing the latent geometry of
market dependencies. When quantum entropy rises, the network becomes increasingly
entangled and thus more sensitive to new information. Such tightening often marks the
run-up to market-wide regime shifts, explaining why entropy spikes tend to precede sharp
reconfigurations triggered by major announcements or policy disclosures.

### 5.3 QEWS and Structural Transitions

![Refer to caption](x2.png)


Figure 3: QEWS vs Market Index around the Trump Tariff Shock

Figure [3](https://arxiv.org/html/2511.21515v1#S5.F3 "Figure 3 ‣ 5.3 QEWS and Structural Transitions ‣ 5 Empirical Results ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk") illustrates how the Quantum Early-Warning Signal (QEWS) evolves
around the Trump tariff announcement on 18 February 2025.
QEWS is defined as the standardized temporal derivative of the Entanglement Risk Index (ERI),
capturing the *rate of change* of structural tightening or loosening in the market network.
In contrast with return-based indicators, QEWS describes the *dynamics of the
market’s internal dependency geometry*, not the dynamics of prices themselves.

##### Quantum-information interpretation.

Within the QNA framework, QEWS reflects changes in the non-separability of the market
density matrix ρt\rho\_{t}. A positive QEWS indicates that ρt\rho\_{t} is becoming increasingly
entangled—coherence terms intensify and a rising fraction of assets respond to a shared,
latent information set. In quantum-information terms, the system approaches a state in which
a subsequent “measurement” can trigger a discontinuous structural collapse.
Major announcements, such as the tariff decision, act as measurement operators that
resolve latent information and force the system into a more classical, decohered configuration.
The observed sharp fall in QEWS immediately following the announcement mirrors this
collapse from an entangled pre-event state into a post-event classical state.

##### Financial-market interpretation.

From a financial perspective, QEWS quantifies latent risk accumulation rather than
short-term return dynamics. In Figure [3](https://arxiv.org/html/2511.21515v1#S5.F3 "Figure 3 ‣ 5.3 QEWS and Structural Transitions ‣ 5 Empirical Results ‣ The Quantum Network of Assets: A Non-Classical Framework for Market Correlation and Structural Risk"), QEWS (red line) rises steadily throughout
January and early February 2025, even as the NASDAQ–100 index (blue line) continues
to trend upward. This divergence reveals that:

* •

  cross-asset dependencies were tightening well before the event,
* •

  diversification capacity was eroding despite rising prices,
* •

  the market was increasingly driven by a single latent information factor,
* •

  investor positioning was synchronizing around expectations not yet disclosed.

This pre-event rise in QEWS corresponds to a “structural loading” phase—the market
becomes more coherent, more one-dimensional, and therefore more fragile.
Classical correlation and realized volatility capture none of this behaviour; price-based
indicators show no sign of deterioration until after the announcement.

##### Structural transition at the event.

Immediately following the tariff announcement, QEWS collapses sharply and turns negative.
This behaviour indicates an abrupt decoherence-like transition:

* •

  the latent information set is resolved,
* •

  the previously tight dependency structure fragments,
* •

  assets revert to more idiosyncratic behaviour.

The NASDAQ–100 index begins to fall only *after* QEWS collapses, demonstrating
that structural deterioration precedes price deterioration.
This temporal ordering is consistent with network-based theories of systemic risk, where
dependency geometry typically destabilizes before returns reflect the new regime.

##### Interpretation.

QEWS should therefore be viewed not as a forecasting indicator but as a
quantum-inspired structural transition detector.
Its role is to identify when:

* •

  latent information begins affecting the joint market state,
* •

  the dependency network grows increasingly sensitive to shocks,
* •

  the system approaches a critical transition or regime shift.

The 2025 tariff shock provides a clear empirical demonstration:
QEWS detects structural tightening weeks before the event, collapses immediately upon
measurement, and stabilizes before prices recover.
This decoupling between structural and price dynamics highlights why quantum-information
metrics offer insights unavailable to classical correlation-based methods.

## 6 Discussion

A central conceptual feature of QNA is the explicit distinction between the
*structural layer* of financial markets—represented by the density matrix,
its entropy, and mutual-information characteristics—and the *price layer*,
represented by index levels or returns. These two layers evolve on different
timescales and respond to different components of the information set.
Consequently, structural signals such as QEWS may lead, lag, or diverge from
price movements. This behaviour is not a defect but a natural implication of
QNA’s purpose: it measures the geometry of dependencies, not price
expectations. The empirical results in Section 5 illustrate this clearly:
QEWS tightened before the tariff announcement because structural tension
accumulated before price deterioration—the hallmark of many systemic episodes.

##### Non-separability and market interconnectedness.

The density-matrix formalism enables QNA to encode *non-separability*:
a mathematical property reflecting the extent to which assets cannot be
decomposed into independent subsystems. In quantum theory, non-separability
is the defining feature of entanglement; in finance, it captures cross-asset
information sharing, factor co-movement, and the erosion of diversification
capacity. Classical correlation matrices implicitly assume linear,
pairwise separability, whereas QNA captures higher-order and global forms of
dependency that become particularly relevant in stressed markets. Rising
entropy or mutual information therefore reflects growing systemic
connectedness even when pairwise correlations remain muted.

##### Coherence, latent information, and structural tension.

The off-diagonal coherence terms of the density matrix encode latent
interactions among assets. In financial interpretation, these terms
represent information channels that influence joint behaviour before
being reflected in prices. Examples include anticipatory trading ahead of
policy decisions, slow-moving macroeconomic forces, or collective investor
behaviour leading to synchronised positioning. As structural dependencies
tighten, the density matrix becomes more mixed, and quantum entropy or ERI
increases. This mirrors physical systems approaching a measurement or phase
transition: sensitivity rises as the system becomes more coherent and more
susceptible to shocks.

##### Measurement, collapse, and market announcements.

Major announcements—such as earnings releases, policy statements, or
geopolitical events—can be viewed as measurement operations that “collapse”
the latent information state into a realised classical outcome. The structural
tension accumulated beforehand is captured by rising QEWS, while the sharp
post-announcement decline reflects a decoherence-like release of systemic
pressure. The tariff-shock experiment exemplifies this pattern: QEWS weakened
before prices fell, collapsed upon announcement, and stabilised before the
index recovered, demonstrating the structural–price lead–lag dynamic.

##### Interpretative, not predictive.

Although QEWS often moves ahead of prices, it is not intended as a forecasting
model. Its value lies in diagnosing the *state of the dependency network*:
how coherent, entangled, or one-dimensional the market has become. Structural
changes may precede price changes, but QNA does not attempt to map structure
into returns. Instead, it complements risk models by providing insights into
how fragile or tightly coupled the market is at any point in time. This
interpretative focus is essential for avoiding the common but misleading
equation of “early structural tightening” with “quantitative forecasting”.

##### Implications for systemic risk and financial stability.

Systemic crises frequently originate not from elevated volatility but from
hidden structural tightening that reduces effective dimensionality. QNA-based
metrics offer a direct lens for detecting such tightening by tracking entropy,
mutual information, and ERI. Potential applications include:

* •

  identifying market states characterised by reduced diversification capacity,
* •

  mapping regime boundaries and phase-transition-like behaviour,
* •

  analysing contagion channels through density-matrix partitions,
* •

  quantifying the structural impact of policy uncertainty or macro shocks.

Such tools may be particularly valuable for regulators or portfolio managers
seeking to understand systemic fragility beyond traditional correlation-based
stress tests.

##### Limitations.

One limitation of the present study is that QNA uses daily data and a
fixed rolling window. Higher-frequency data or adaptive windowing may
reveal finer structural transitions. Moreover, entropy-based indicators
depend on the stability of eigenvalue estimates, suggesting future work
on shrinkage-based or Bayesian density-matrix estimators.

##### Future research.

Several avenues extend naturally from the present framework. First,
Bell-type inequalities may offer a mathematical benchmark for
quantifying departures from classical factor models by testing
non-classical dependency structure, even though no physical entanglement
is claimed. Second, multipartite decompositions of the density matrix
could isolate sector-specific contributions to systemic coupling.
Third, integrating QNA with quantum-inspired optimisation and quantum
machine learning might enhance both structural modelling and
risk-sensitive portfolio design. These directions reinforce QNA’s
position as a bridge between quantum information theory and empirical
asset-network analysis.

Overall, QNA provides a novel structural lens through which to examine
financial markets. By integrating concepts from quantum information
with empirical measurements of network behaviour, the framework
highlights how complexity, dependency, and latent information jointly
shape market dynamics. As markets become increasingly interconnected
and information-driven, structural diagnostics such as QNA may play an
important role in understanding systemic vulnerability and regime change.

## 7 Conclusion

This paper introduces the Quantum Network of Assets (QNA), a
quantum-information-inspired framework that generalizes classical correlation by
representing financial markets through density matrices and entropy-based
structural metrics. Rather than invoking physical quantum effects, QNA adopts
the mathematical tools of quantum theory-non-separability, coherence, and
entropy-to capture forms of dependency that classical covariance matrices
cannot express.

The Entanglement Risk Index (ERI) provides a global measure of structural
tightness in the market network, reflecting how strongly assets respond to
shared latent information. The Quantum Early-Warning Signal (QEWS), derived as
a temporal gradient of structural entropy, highlights the buildup of systemic
tension prior to major regime transitions. Although not a forecasting tool,
QEWS reveals patterns of latent information accumulation, demonstrating how
dependency structures often adjust before observable price movements.

Through empirical analysis of the NASDAQ–100, we show that quantum entropy and
ERI evolve more smoothly and display clearer regime distinctions than their
classical counterparts. The framework captures structural tightening ahead of
the 2025 tariff announcement, illustrating how latent information can reshape
network geometry prior to market collapse. These results underscore the value
of quantum-inspired metrics as *diagnostic tools* for understanding
complexity, systemic fragility, and cross-asset interconnectedness.

QNA opens several promising directions for future research. Extensions may
include testing Bell-type inequalities for non-classical dependency,
decomposing multipartite density matrices to identify sectoral contributions to
systemic risk, or integrating QNA with quantum-inspired optimization and
machine learning methods. More broadly, the approach invites a re-examination
of market structure through the lens of quantum information theory, suggesting
that tools developed to characterize complex quantum systems may also illuminate
the hidden geometry of financial networks.

In summary, the QNA provides a coherent and interpretable
framework for structural analysis in finance, offering new perspectives on
market regimes, latent information dynamics, and the mechanisms through which
systemic risk emerges.

## References

* [1]

  Adesso, G., Ragy, S. and Lee, A. (2014).
  Continuous variable quantum information: Gaussian states and beyond.
  Open Systems & Information Dynamics, 21(1).
* [2]

  Bell, J. (1964).
  On the Einstein-Podolsky-Rosen paradox.
  Physics Physique Fizika, 1(3), 195–200.
* [3]

  Biamonte, J., Wittek, P., Pancotti, N., Rebentrost, P., Wiebe, N. and Lloyd, S. (2017).
  Quantum machine learning.
  Nature, 549, 195–202.
* [4]

  Bouchaud, J.-P. and Potters, M. (2003).
  Theory of Financial Risk and Derivative Pricing.
  Cambridge University Press.
* [5]

  Bužek, V. and Hillery, M. (1996).
  Quantum copying: Beyond the no-cloning theorem.
  Physical Review A, 54(3), 1844–1852.
* [6]

  Clauser, J., Horne, M., Shimony, A., and Holt, R. (1969).
  Proposed experiment to test local hidden-variable theories.
  Physical Review Letters, 23(15), 880–884.
* [7]

  Fuchs, C. (2002).
  Quantum mechanics as quantum information.
  arXiv:quant-ph/0205039.
* [8]

  Horodecki, R., Horodecki, P., Horodecki, M., and Horodecki, K. (2009).
  Quantum entanglement.
  Reviews of Modern Physics, 81(2), 865–942.
* [9]

  Mantegna, R. and Stanley, H. (2000).
  An Introduction to Econophysics: Correlations and Complexity in Finance.
  Cambridge University Press.
* [10]

  Nielsen, M. and Chuang, I. (2010).
  Quantum Computation and Quantum Information.
  Cambridge University Press.
* [11]

  Preskill, J. (2018).
  Quantum Computation Lecture Notes.
  California Institute of Technology.
* [12]

  Vedral, V. (2002).
  The role of relative entropy in quantum information theory.
  Reviews of Modern Physics, 74, 197–234.
* [13]

  Wehner, S. and Winter, A. (2010).
  Entropic uncertainty relations—a survey.
  New Journal of Physics, 12, 025009.
* [14]

  Zurek, W. (2003).
  Decoherence, einselection, and the quantum origins of the classical.
  Reviews of Modern Physics, 75(3), 715–775.