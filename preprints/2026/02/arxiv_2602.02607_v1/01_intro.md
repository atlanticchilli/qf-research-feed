---
authors:
- Tatsuru Kikuchi
doc_id: arxiv:2602.02607v1
family_id: arxiv:2602.02607
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic
  Risk in the U.S. Banking Sector'
url_abs: http://arxiv.org/abs/2602.02607v1
url_html: https://arxiv.org/html/2602.02607v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tatsuru Kikuchi111This is my last paper in my life.

(())

###### Abstract

This paper evaluates the causal impact of Generative Artificial Intelligence (GenAI) adoption on productivity and systemic risk in the U.S. banking sector. Using a novel dataset linking SEC 10-Q filings to Federal Reserve regulatory data for 809 financial institutions over 2018–2025, we employ two complementary identification strategies: Dynamic Spatial Durbin Models (DSDM) to capture network spillovers and Synthetic Difference-in-Differences (SDID) for causal inference using the November 2022 ChatGPT release as an exogenous shock. Our findings reveal a striking “Productivity Paradox”: while DSDM estimates show that AI-adopting banks are high performers (β>0\beta>0), the causal SDID analysis documents a significant “Implementation Tax”—adopting banks experience a 428-basis-point decline in ROE as they absorb GenAI integration costs. This tax falls disproportionately on smaller institutions, with bottom-quartile banks suffering a 517-basis-point ROE decline compared to 129 basis points for larger banks, suggesting that economies of scale provide significant advantages in AI implementation. Most critically, our DSDM analysis reveals significant positive spillovers (θ=0.161\theta=0.161 for ROA, p<0.01p<0.01; θ=0.679\theta=0.679 for ROE, p<0.05p<0.05), with spillovers among large banks reaching θ=3.13\theta=3.13 for ROE, indicating that the U.S. banking system is becoming “algorithmically coupled.” This synchronization of AI-driven decision-making creates a new channel for systemic contagion: a technical failure in widely-adopted AI models could trigger correlated shocks across the entire financial network.

  

Keywords: Generative AI, Banking Productivity, Systemic Risk, Spatial Econometrics, Synthetic Difference-in-Differences, Financial Contagion, Technology Adoption, Productivity Paradox. 
  
JEL Classification: G21, O33, C23, L86, E44.

## 1 Introduction

The emergence of Generative Artificial Intelligence (GenAI) represents a watershed moment in the history of technological progress. Since the public release of ChatGPT in November 2022, large language models (LLMs) have demonstrated unprecedented capabilities in natural language processing, code generation, and complex reasoning tasks (OpenAI, [2023](https://arxiv.org/html/2602.02607v1#bib.bib37)). The financial services industry, with its information-intensive production function and substantial IT infrastructure, stands at the frontier of this technological transformation. Yet, as Robert Solow famously observed, “you can see the computer age everywhere but in the productivity statistics” (Solow, [1987](https://arxiv.org/html/2602.02607v1#bib.bib40)). This paper asks whether Solow’s paradox persists in the age of generative AI, and what implications AI adoption holds for systemic stability in the banking sector.

We document three main findings that collectively reveal a complex, multi-dimensional phenomenon. First, we uncover a striking Productivity Paradox: our DSDM estimates show that AI-adopting banks exhibit higher productivity (β>0\beta>0), consistent with AI adoption being a marker of “frontier” institutions. Yet our causal SDID analysis reveals that the act of adoption causes productivity to decline—a 46-basis-point drop in ROA and a 428-basis-point drop in ROE. This paradox resolves through the lens of the “Innovation J-Curve” (Brynjolfsson et al., [2021](https://arxiv.org/html/2602.02607v1#bib.bib19)): high-performing banks are investing heavily in GPUs, data scientists, and AI infrastructure, incurring massive current expenses that depress net income even as they position themselves for future dominance.

Second, we document heterogeneity in the distribution of implementation costs. Smaller banks (bottom 75% by assets) suffer an ROE decline of 517 basis points—substantially larger than the 129-basis-point decline experienced by larger institutions. This asymmetry suggests that economies of scale provide significant advantages in AI implementation: larger banks can spread fixed implementation costs across a broader asset base, employ dedicated AI teams, and leverage superior data infrastructure. Smaller banks face proportionally larger implementation burdens relative to their equity base.

Third, and most consequential for financial stability, our network analysis reveals significant positive spillover effects. Our DSDM estimates show θ=0.161\theta=0.161 for ROA and θ=0.679\theta=0.679 for ROE, indicating “strategic complementarity” whereby AI adoption by one institution raises productivity at connected institutions through knowledge diffusion. For large banks, spillovers are dramatically amplified (θ=3.13\theta=3.13 for ROE). This carries profound implications: the U.S. banking system is becoming algorithmically coupled. When AI adoption by one institution raises productivity at connected institutions, the network synchronizes, creating vulnerability to common technical failures or model errors.

These findings contribute to several literatures. We extend the productivity paradox literature (Brynjolfsson, [1993](https://arxiv.org/html/2602.02607v1#bib.bib17); David, [1990](https://arxiv.org/html/2602.02607v1#bib.bib22)) to the domain of generative AI, documenting that the classic J-curve pattern of technology adoption (Brynjolfsson et al., [2021](https://arxiv.org/html/2602.02607v1#bib.bib19)) is amplified in highly regulated industries. We contribute to the banking technology literature (Philippon, [2016](https://arxiv.org/html/2602.02607v1#bib.bib39); Berg et al., [2022](https://arxiv.org/html/2602.02607v1#bib.bib12); Fuster et al., [2019](https://arxiv.org/html/2602.02607v1#bib.bib27)) by providing the first causal estimates of GenAI’s impact on bank performance. We advance the financial networks literature (Acemoglu et al., [2015](https://arxiv.org/html/2602.02607v1#bib.bib3); Elliott et al., [2014](https://arxiv.org/html/2602.02607v1#bib.bib25)) by introducing the concept of “algorithmic coupling”—the synchronization of risk management and decision-making processes through shared AI architectures. Finally, we contribute methodologically by combining DSDM and SDID estimators to achieve both network spillover quantification and clean causal identification.

The remainder of this paper proceeds as follows. Section 2 provides a comprehensive review of the relevant literature. Section 3 develops our theoretical framework, derives testable hypotheses, and presents the econometric methodology. Section 4 describes the data construction process. Section 5 reports the main empirical results. Section 6 discusses robustness checks. Section 7 concludes with policy implications.

## 2 Literature Review

Our research integrates four distinct strands of economic inquiry: the productivity paradox and technology diffusion, banking structure and digital transformation, financial networks and systemic risk, and the emerging economics of artificial intelligence.

### 2.1 The Productivity Paradox and Technology Diffusion

The gap between technological potential and measured productivity gains has puzzled economists since Solow ([1987](https://arxiv.org/html/2602.02607v1#bib.bib40)) first articulated the computer productivity paradox. Brynjolfsson ([1993](https://arxiv.org/html/2602.02607v1#bib.bib17)) systematically documented this phenomenon, proposing four explanations: mismeasurement of outputs and inputs, lags due to learning and adjustment, redistribution and dissipation of profits, and mismanagement of information technology. Subsequent work by David ([1990](https://arxiv.org/html/2602.02607v1#bib.bib22)) drew parallels to the electrification of American manufacturing, demonstrating that general-purpose technologies (GPTs) require decades of complementary investment before their productivity potential is realized.

The resolution of the productivity paradox in the late 1990s, documented by Jorgenson & Stiroh ([2000](https://arxiv.org/html/2602.02607v1#bib.bib32)) and Oliner & Sichel ([2000](https://arxiv.org/html/2602.02607v1#bib.bib36)), coincided with massive investments in organizational restructuring and human capital (Bresnahan et al., [2002](https://arxiv.org/html/2602.02607v1#bib.bib16)). Brynjolfsson & Hitt ([2000](https://arxiv.org/html/2602.02607v1#bib.bib18)) showed that firms combining IT investment with decentralized decision-making experienced productivity gains three to five times larger than those investing in technology alone. This insight—that technology and organizational capital are complements—forms a cornerstone of our theoretical framework.

Recent work on generative AI suggests an acceleration of productivity effects. Brynjolfsson et al. ([2023](https://arxiv.org/html/2602.02607v1#bib.bib20)) document a 14% improvement in call center worker productivity following ChatGPT deployment, with gains concentrated among less-experienced workers. Noy & Zhang ([2023](https://arxiv.org/html/2602.02607v1#bib.bib35)) find that ChatGPT reduces task completion time by 37% for professional writing tasks. However, Dell’Acqua et al. ([2023](https://arxiv.org/html/2602.02607v1#bib.bib23)) caution that these micro-level estimates may not aggregate to macro-level productivity gains due to general equilibrium effects, task reallocation, and measurement challenges.

### 2.2 Banking Structure and Digital Transformation

The banking industry has experienced successive waves of technological disruption. Berger ([2003](https://arxiv.org/html/2602.02607v1#bib.bib14)) document how information technology transformed the economics of lending, enabling relationship banking to coexist with transaction-based models. Petersen & Rajan ([2002](https://arxiv.org/html/2602.02607v1#bib.bib38)) show that IT investment expanded the geographic reach of small business lending, fundamentally altering the spatial organization of credit markets.

The FinTech revolution of the 2010s introduced new competitive dynamics. Buchak et al. ([2018](https://arxiv.org/html/2602.02607v1#bib.bib21)) find that FinTech lenders gained market share during periods of regulatory constraint on traditional banks. Fuster et al. ([2019](https://arxiv.org/html/2602.02607v1#bib.bib27)) document that FinTech mortgage lenders process applications 20% faster than traditional lenders, with no increase in default rates. Berg et al. ([2022](https://arxiv.org/html/2602.02607v1#bib.bib12)) provide a comprehensive review of FinTech lending, emphasizing the role of alternative data and machine learning in credit allocation.

A persistent theme in this literature is the “digital divide” between large and small institutions. Berger et al. ([2005](https://arxiv.org/html/2602.02607v1#bib.bib15)) document substantial scale economies in bank technology investment. Frame et al. ([2014](https://arxiv.org/html/2602.02607v1#bib.bib26)) show that community banks face structural disadvantages in adopting new technologies due to limited IT budgets and expertise. However, Jagtiani & Lemieux ([2018](https://arxiv.org/html/2602.02607v1#bib.bib31)) suggest that FinTech partnerships may enable smaller banks to leapfrog technological barriers. Our analysis extends this debate to the GenAI era, examining whether the new technology exacerbates or mitigates pre-existing inequalities.

### 2.3 Financial Networks and Systemic Risk

The 2008 financial crisis catalyzed intense scholarly interest in network effects and systemic risk. Allen & Gale ([2000](https://arxiv.org/html/2602.02607v1#bib.bib5)) develop a foundational model of financial contagion through interbank claims, showing that network structure determines crisis severity. Acemoglu et al. ([2015](https://arxiv.org/html/2602.02607v1#bib.bib3)) extend this framework to demonstrate that network topology exhibits a phase transition: diversified networks are resilient to small shocks but catastrophically fragile to large ones.

Elliott et al. ([2014](https://arxiv.org/html/2602.02607v1#bib.bib25)) analyze cascading failures in financial networks, distinguishing between integration (the density of cross-holdings) and diversification (the breadth of counterparty relationships). They show that greater integration initially reduces systemic risk but eventually increases it beyond a critical threshold. Battiston et al. ([2012](https://arxiv.org/html/2602.02607v1#bib.bib11)) introduce the concept of “DebtRank” to measure the systemic importance of individual institutions based on their network position.

The application of network analysis to technology adoption is more recent. Jackson ([2017](https://arxiv.org/html/2602.02607v1#bib.bib30)) provide a comprehensive review of economic and social networks, emphasizing how network structure shapes diffusion dynamics. Banerjee et al. ([2013](https://arxiv.org/html/2602.02607v1#bib.bib8)) show that network centrality predicts technology adoption in development contexts. We contribute to this literature by demonstrating that AI adoption creates a new dimension of network interdependence—“algorithmic coupling”—that operates independently of traditional credit and liquidity linkages.

### 2.4 The Economics of Artificial Intelligence

A rapidly growing literature examines the economic implications of AI. Agrawal et al. ([2018](https://arxiv.org/html/2602.02607v1#bib.bib4)) conceptualize AI as a “prediction machine” that dramatically reduces the cost of prediction, inducing substitution toward human judgment in complementary tasks. Acemoglu & Restrepo ([2018](https://arxiv.org/html/2602.02607v1#bib.bib2)) develop a task-based framework showing that automation’s aggregate effects depend on the relative strength of displacement and productivity effects.

Autor ([2022](https://arxiv.org/html/2602.02607v1#bib.bib7)) documents the “so-so automation” phenomenon, where technologies that modestly increase productivity while substantially displacing workers may reduce labor share without generating commensurate output gains. Korinek & Suh ([2024](https://arxiv.org/html/2602.02607v1#bib.bib33)) analyze the macroeconomic implications of transformative AI, modeling scenarios ranging from gradual productivity improvement to rapid technological unemployment.

In the financial sector, AI applications have been extensively studied. Gu et al. ([2020](https://arxiv.org/html/2602.02607v1#bib.bib29)) demonstrate that machine learning methods substantially outperform traditional asset pricing models in predicting returns. Bao & Huang ([2020](https://arxiv.org/html/2602.02607v1#bib.bib9)) show that AI-based lending algorithms reduce default rates while expanding credit access to underserved populations. However, Bartlett et al. ([2022](https://arxiv.org/html/2602.02607v1#bib.bib10)) document algorithmic discrimination in mortgage lending, highlighting the tension between efficiency and equity. Gensler & Bailey ([2020](https://arxiv.org/html/2602.02607v1#bib.bib28)) warn of systemic risks arising from “model monoculture”—the widespread adoption of similar AI architectures creating correlated vulnerabilities.

Our paper bridges these literatures by providing the first comprehensive empirical analysis of GenAI adoption in the banking sector, combining spatial econometric methods with causal identification strategies to capture both network spillovers and direct treatment effects.

## 3 Theoretical Framework and Econometric Strategy

This section develops a theoretical framework linking GenAI adoption to bank productivity and systemic risk, derives testable hypotheses, and presents the econometric methodology for identification. We employ two complementary approaches: (i) a Dynamic Spatial Durbin Model (DSDM) to quantify network spillovers, and (ii) Synthetic Difference-in-Differences (SDID) to establish causality using the 2023 ChatGPT release as an exogenous shock.

### 3.1 Network Spillovers in Banking: Theoretical Foundation

Banks do not operate in isolation. Their productivity is influenced by the strategic decisions of competitors, counterparties, and peer institutions operating in similar market segments. We model these interdependencies using spatial econometric techniques that distinguish between two types of spillover effects.

###### Definition 3.1 (Network Spillovers).

Network spillovers refer to the effect of connected banks’ AI adoption on bank ii’s productivity, transmitted through competitive relationships defined by business model similarity. Banks competing in similar market segments (similar asset sizes, loan portfolios, geographic footprints) exert stronger spillover effects on each other.

###### Definition 3.2 (Geographic Spillovers).

Geographic spillovers refer to the effect of geographically proximate banks’ AI adoption on bank ii’s productivity, transmitted through local labor markets, regional vendor ecosystems, and face-to-face knowledge transfer.

These spillovers operate through distinct mechanisms. Knowledge spillovers arise when θ>0\theta>0: banks learn from peer institutions’ AI implementations through labor mobility, industry conferences, vendor relationships, and regulatory examinations. Early adopters develop standardized APIs, data protocols, and integration frameworks that reduce implementation costs for followers. In contrast, competitive (business-stealing) spillovers emerge when θ<0\theta<0: AI adoption by competitors may erode market share, compress margins, and intensify price competition. If one bank’s AI-driven efficiency allows it to offer better rates or faster service, competitors lose customers.

The net spillover effect—whether knowledge diffusion or business-stealing dominates—is an empirical question captured by the sign and magnitude of θ\theta in our DSDM specification.

### 3.2 The Innovation Tax and Size Heterogeneity

Large banks face systematically different adoption economics than small banks. Let SiS\_{i} denote bank ii’s time-invariant size (measured by average total assets over the sample period). The total cost of AI adoption is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci​t=c0+c1⋅Siϕ+c2⋅ComplexityiC\_{it}=c\_{0}+c\_{1}\cdot S\_{i}^{\phi}+c\_{2}\cdot\text{Complexity}\_{i} |  | (1) |

where c0c\_{0} represents fixed costs (software licensing, initial implementation), c1⋅Siϕc\_{1}\cdot S\_{i}^{\phi} captures scale-dependent costs (data migration, system integration across platforms), and Complexityi\text{Complexity}\_{i} reflects organizational complexity that increases with institutional size and M&A history.

For large banks, the scale-dependent term dominates. These institutions operate heterogeneous legacy systems accumulated through decades of organic growth and acquisitions. Integrating GenAI across disparate platforms requires substantial investment in data harmonization, API development, and security infrastructure. The “Innovation Tax” reflects these transition costs, which depress measured productivity during the implementation phase.

### 3.3 Algorithmic Coupling and Systemic Risk

Beyond productivity effects, AI adoption introduces a new dimension of systemic risk. When multiple banks deploy similar AI architectures—trained on similar data, optimized for similar objectives, subject to similar failure modes—their decision-making processes become correlated even absent direct financial linkages.

###### Definition 3.3 (Algorithmic Coupling).

Algorithmic coupling refers to the synchronization of bank decision-making processes arising from the adoption of similar AI systems. Two banks are algorithmically coupled if their AI-driven decisions (credit scoring, risk management, trading) are correlated due to shared model architectures, training data, or vendor solutions.

We formalize this concept as follows. Let Corri​j,t\text{Corr}\_{ij,t} denote the correlation between banks ii and jj’s AI-driven decisions at time tt. Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Corri​j,tA​I=Corri​j,tb​a​s​e​l​i​n​e+δ⋅Di​tA​I⋅Dj​tA​I⋅VendorOverlapi​j\text{Corr}\_{ij,t}^{AI}=\text{Corr}\_{ij,t}^{baseline}+\delta\cdot D\_{it}^{AI}\cdot D\_{jt}^{AI}\cdot\text{VendorOverlap}\_{ij} |  | (2) |

where Corri​j,tb​a​s​e​l​i​n​e\text{Corr}\_{ij,t}^{baseline} denotes the baseline correlation due to common factor exposures such as interest rates and macroeconomic conditions; Di​tA​I∈{0,1}D\_{it}^{AI}\in\{0,1\} is an indicator equal to 1 if bank ii has adopted GenAI by time tt; the parameter δ>0\delta>0 captures the additional correlation arising from shared AI architectures; and VendorOverlapi​j∈[0,1]\text{VendorOverlap}\_{ij}\in[0,1] measures the similarity of AI vendor relationships between banks ii and jj, such as both using GPT-4 or both contracting with the same cloud provider.

This algorithmic coupling creates a channel for synchronized failure distinct from traditional contagion mechanisms. A model vulnerability, adversarial attack, or data contamination event affecting one bank’s AI system is likely to affect all banks using similar systems.

### 3.4 Hypotheses

Our theoretical framework generates four testable hypotheses:

###### Hypothesis 1 (Frontier Firm Selection).

AI-adopting banks exhibit higher baseline productivity than non-adopters, reflecting positive selection into treatment by “frontier” institutions.

###### Hypothesis 2 (Implementation Tax).

The causal effect of AI adoption on productivity is negative in the short run, reflecting implementation costs that depress earnings during the transition period.

###### Hypothesis 3 (Size Heterogeneity).

The Implementation Tax varies by bank size, with large banks experiencing more pronounced short-term productivity declines due to greater legacy system complexity.

###### Hypothesis 4 (Positive Network Spillovers).

AI adoption generates positive spillover effects on network-connected banks, consistent with knowledge diffusion dominating business-stealing competition.

### 3.5 Econometric Strategy I: Dynamic Spatial Durbin Model (DSDM)

To quantify network spillovers and test Hypotheses 1 and 4, we estimate a Dynamic Spatial Durbin Model following Elhorst ([2014](https://arxiv.org/html/2602.02607v1#bib.bib24)) and LeSage & Pace ([2009](https://arxiv.org/html/2602.02607v1#bib.bib34)). The DSDM generalizes standard panel fixed effects models by incorporating both temporal dynamics and spatial interdependence.

#### 3.5.1 Model Specification

The full DSDM specification is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi​t=τ​Yi,t−1+ρ​∑j=1Nwi​j​Yj​t+η​∑j=1Nwi​j​Yj,t−1+β​Di​tA​I+θ​∑j=1Nwi​j​Dj​tA​I+𝜸′​𝑿i​t+μi+δt+εi​tY\_{it}=\tau Y\_{i,t-1}+\rho\sum\_{j=1}^{N}w\_{ij}Y\_{jt}+\eta\sum\_{j=1}^{N}w\_{ij}Y\_{j,t-1}+\beta D\_{it}^{AI}+\theta\sum\_{j=1}^{N}w\_{ij}D\_{jt}^{AI}+\boldsymbol{\gamma}^{\prime}\boldsymbol{X}\_{it}+\mu\_{i}+\delta\_{t}+\varepsilon\_{it} |  | (3) |

In matrix notation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒀t=τ​𝒀t−1+ρ​𝑾​𝒀t+η​𝑾​𝒀t−1+β​𝑫tA​I+θ​𝑾​𝑫tA​I+𝚪​𝑿t+𝝁+δt​𝜾+𝜺t\boldsymbol{Y}\_{t}=\tau\boldsymbol{Y}\_{t-1}+\rho\boldsymbol{W}\boldsymbol{Y}\_{t}+\eta\boldsymbol{W}\boldsymbol{Y}\_{t-1}+\beta\boldsymbol{D}\_{t}^{AI}+\theta\boldsymbol{W}\boldsymbol{D}\_{t}^{AI}+\boldsymbol{\Gamma}\boldsymbol{X}\_{t}+\boldsymbol{\mu}+\delta\_{t}\boldsymbol{\iota}+\boldsymbol{\varepsilon}\_{t} |  | (4) |

In this specification, Yi​tY\_{it} denotes the productivity measure for bank ii in quarter tt (ROA or ROE, expressed in percentage points), and Yi,t−1Y\_{i,t-1} is its one-quarter lag. The treatment indicator Di​tA​I∈{0,1}D\_{it}^{AI}\in\{0,1\} equals 1 if bank ii mentions GenAI keywords in SEC filings at time tt. The matrix 𝑾=[wi​j]\boldsymbol{W}=[w\_{ij}] is an N×NN\times N row-normalized spatial weight matrix defined below, so that ∑jwi​j​Yj​t\sum\_{j}w\_{ij}Y\_{jt} represents the spatially weighted average of contemporaneous peer productivity and ∑jwi​j​Dj​tA​I\sum\_{j}w\_{ij}D\_{jt}^{AI} captures network exposure to peer AI adoption. The vector 𝑿i​t\boldsymbol{X}\_{it} contains control variables including log assets, Tier 1 capital ratio, digitalization index, and CEO age. Bank fixed effects μi\mu\_{i} absorb time-invariant unobserved heterogeneity, time fixed effects δt\delta\_{t} absorb common shocks affecting all banks, and εi​t\varepsilon\_{it} is the idiosyncratic error term.

The key parameters of interest are as follows. The temporal persistence parameter τ∈(−1,1)\tau\in(-1,1) measures how strongly current productivity depends on past productivity. The spatial autoregressive parameter ρ∈(−1,1)\rho\in(-1,1) captures contemporaneous correlation in productivity across connected banks. The spatial-temporal lag η\eta measures the effect of lagged peer productivity on current own productivity. Most importantly, β\beta captures the direct effect of own AI adoption—the productivity difference between AI adopters and non-adopters, conditional on controls—while θ\theta captures the network spillover effect, measuring how connected banks’ AI adoption affects own productivity.

#### 3.5.2 Spatial Weight Matrix Construction

We construct two spatial weight matrices to capture different spillover channels:

Network Weight Matrix (Wn​e​t​w​o​r​kW\_{network}): Based on asset similarity, capturing competitive relationships:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi​jn​e​t​w​o​r​k=exp⁡(−(ln⁡A¯i−ln⁡A¯j)22​h2)w\_{ij}^{network}=\exp\left(-\frac{(\ln\bar{A}\_{i}-\ln\bar{A}\_{j})^{2}}{2h^{2}}\right) |  | (5) |

where A¯i=1T​∑t=1TAi​t\bar{A}\_{i}=\frac{1}{T}\sum\_{t=1}^{T}A\_{it} is bank ii’s average total assets over the sample period and hh is a bandwidth parameter set to the standard deviation of log assets. Banks of similar size compete in similar market segments and thus exert stronger spillover effects on each other.

Geographic Weight Matrix (Wg​e​oW\_{geo}): Based on headquarters proximity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi​jg​e​o=exp⁡(−di​jdm​e​d​i​a​n)w\_{ij}^{geo}=\exp\left(-\frac{d\_{ij}}{d\_{median}}\right) |  | (6) |

where di​jd\_{ij} is the Haversine distance between bank ii and jj’s headquarters and dm​e​d​i​a​nd\_{median} is the median pairwise distance. Geographically proximate banks share local labor markets and vendor ecosystems.

Both matrices are row-normalized so that ∑j≠iwi​j=1\sum\_{j\neq i}w\_{ij}=1 for all ii:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi​j=wi​jr​a​w∑k≠iwi​kr​a​ww\_{ij}=\frac{w\_{ij}^{raw}}{\sum\_{k\neq i}w\_{ik}^{raw}} |  | (7) |

#### 3.5.3 Estimation Methods

The presence of the spatially lagged dependent variable 𝑾​𝒀t\boldsymbol{W}\boldsymbol{Y}\_{t} on the right-hand side creates endogeneity due to simultaneity: bank ii’s productivity affects bank jj’s productivity, which in turn affects bank ii. OLS is inconsistent. We employ three estimation approaches:

Maximum Likelihood Estimation (MLE): MLE jointly estimates all parameters by maximizing the log-likelihood function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡L​(𝚯)=−N​T2​ln⁡(2​π​σ2)+T​ln⁡|IN−ρ​𝑾|−12​σ2​∑t=1T𝜺t′​𝜺t\ln L(\boldsymbol{\Theta})=-\frac{NT}{2}\ln(2\pi\sigma^{2})+T\ln|I\_{N}-\rho\boldsymbol{W}|-\frac{1}{2\sigma^{2}}\sum\_{t=1}^{T}\boldsymbol{\varepsilon}\_{t}^{\prime}\boldsymbol{\varepsilon}\_{t} |  | (8) |

where 𝚯=(τ,ρ,η,β,θ,𝜸,σ2)\boldsymbol{\Theta}=(\tau,\rho,\eta,\beta,\theta,\boldsymbol{\gamma},\sigma^{2}) and the Jacobian term ln⁡|IN−ρ​𝑾|\ln|I\_{N}-\rho\boldsymbol{W}| accounts for the simultaneity. MLE is consistent and efficient under correct specification but sensitive to distributional assumptions.

Quasi-Maximum Likelihood Estimation (QMLE): QMLE uses the same likelihood function but relaxes the normality assumption. Consistency holds under weaker conditions, and we compute robust (sandwich) standard errors to account for potential heteroskedasticity and serial correlation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var^​(𝚯^)=𝑯−1​𝑮​𝑯−1\widehat{\text{Var}}(\hat{\boldsymbol{\Theta}})=\boldsymbol{H}^{-1}\boldsymbol{G}\boldsymbol{H}^{-1} |  | (9) |

where 𝑯\boldsymbol{H} is the Hessian and 𝑮\boldsymbol{G} is the outer product of gradients.

Bayesian MCMC Estimation: Bayesian estimation treats parameters as random variables with prior distributions and updates these priors using the data to obtain posterior distributions. We specify weakly informative priors:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | τ,ρ,η\displaystyle\tau,\rho,\eta | ∼Uniform​(−1,1)\displaystyle\sim\text{Uniform}(-1,1) |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | β,θ,𝜸\displaystyle\beta,\theta,\boldsymbol{\gamma} | ∼Normal​(0,10)\displaystyle\sim\text{Normal}(0,10) |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ2\displaystyle\sigma^{2} | ∼Inverse-Gamma​(0.01,0.01)\displaystyle\sim\text{Inverse-Gamma}(0.01,0.01) |  | (12) |

We use Markov Chain Monte Carlo (MCMC) with 10,000 iterations (5,000 burn-in) to sample from the posterior distribution. Bayesian estimation provides several advantages: (i) full posterior distributions rather than point estimates, enabling probabilistic inference; (ii) natural handling of parameter constraints (|ρ|<1|\rho|<1); (iii) robustness to small-sample issues. We report posterior means and 95% credible intervals, with significance determined by whether credible intervals exclude zero.

#### 3.5.4 Interpretation of Spillover Effects

The coefficient θ\theta captures the direct spillover effect: holding own AI adoption constant, how does a one-unit increase in the spatially weighted average of neighbors’ AI adoption affect own productivity?

Due to feedback effects in spatial models, the total marginal effect of AI adoption differs from the coefficient. Following LeSage & Pace ([2009](https://arxiv.org/html/2602.02607v1#bib.bib34)), we decompose:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝒀∂Di​tA​I=(IN−ρ​𝑾)−1​(β​IN+θ​𝑾)\frac{\partial\boldsymbol{Y}}{\partial D\_{it}^{AI}}=(I\_{N}-\rho\boldsymbol{W})^{-1}(\beta I\_{N}+\theta\boldsymbol{W}) |  | (13) |

Direct Effect: The average diagonal element—the effect of bank ii’s own AI adoption on its own productivity, including feedback through the network:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Direct Effect=1N​tr​[(IN−ρ​𝑾)−1​β​IN]\text{Direct Effect}=\frac{1}{N}\text{tr}\left[(I\_{N}-\rho\boldsymbol{W})^{-1}\beta I\_{N}\right] |  | (14) |

Indirect (Spillover) Effect: The average off-diagonal row sum—the cumulative effect of all other banks’ AI adoption on bank ii’s productivity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Indirect Effect=1N​𝜾′​[(IN−ρ​𝑾)−1​θ​𝑾]​𝜾\text{Indirect Effect}=\frac{1}{N}\boldsymbol{\iota}^{\prime}\left[(I\_{N}-\rho\boldsymbol{W})^{-1}\theta\boldsymbol{W}\right]\boldsymbol{\iota} |  | (15) |

Total Effect: Direct + Indirect—the system-wide productivity impact of universal AI adoption.

#### 3.5.5 Limitations: Endogeneity and Selection

While the DSDM effectively captures network spillovers and cross-sectional associations, it faces a fundamental endogeneity concern: banks may adopt AI because they are already becoming more productive, rather than AI causing productivity improvements. The positive β\beta coefficient may reflect a causal effect of AI on productivity, positive selection whereby high-productivity “frontier” banks are more likely to adopt AI, or reverse causality in which improving productivity frees resources for AI investment.

The DSDM cannot distinguish between these interpretations. To establish causality, we turn to our second econometric strategy.

### 3.6 Econometric Strategy II: Synthetic Difference-in-Differences (SDID)

To identify the causal effect of AI adoption and test Hypotheses 2 and 3, we employ the Synthetic Difference-in-Differences framework developed by Arkhangelsky et al. ([2021](https://arxiv.org/html/2602.02607v1#bib.bib6)). SDID addresses the endogeneity concerns of DSDM by constructing counterfactual outcomes and exploiting an exogenous shock to AI availability.

#### 3.6.1 The 2023 ChatGPT Shock as Exogenous Treatment

Our identification strategy exploits the November 2022 public release of ChatGPT as a plausibly exogenous shock to the banking industry’s AI production function. While individual banks’ decisions to adopt AI are endogenous, the availability of powerful, accessible GenAI tools was determined by technological developments at OpenAI—an event external to the banking sector.

We define the treatment period as 2023Q1, when the “Generative AI” revolution became salient to financial institutions. This timing reflects several converging factors: ChatGPT reached 100 million users within two months of its November 2022 launch; GPT-4 was released in March 2023, demonstrating capabilities directly relevant to financial services; SEC 10-Q filings show a sharp increase in AI-related disclosures beginning in 2023Q1; and bank earnings calls and investor presentations pivoted to discussing GenAI strategy in early 2023.

The 2023 shock provides quasi-experimental variation: banks that mention GenAI in their SEC filings after 2023Q1 are “treated,” while banks that never mention GenAI serve as controls. The key identifying assumption is that, absent the ChatGPT shock, treated and control banks would have followed similar productivity trajectories.

#### 3.6.2 Counterfactual Construction

The fundamental problem of causal inference is that we observe each bank in only one state: either having adopted AI or not. SDID solves this by constructing a synthetic counterfactual—a weighted combination of control banks that approximates what the treated bank’s productivity would have been absent treatment.

Potential Outcomes Framework:
Let Yi​t​(0)Y\_{it}(0) denote bank ii’s potential productivity if untreated (no AI adoption) and Yi​t​(1)Y\_{it}(1) if treated (AI adoption). The observed outcome is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi​t=Yi​t​(0)+Di​t⋅[Yi​t​(1)−Yi​t​(0)]⏟Individual Treatment EffectY\_{it}=Y\_{it}(0)+D\_{it}\cdot\underbrace{[Y\_{it}(1)-Y\_{it}(0)]}\_{\text{Individual Treatment Effect}} |  | (16) |

where Di​t=1D\_{it}=1 if bank ii has adopted AI by time tt (first mention in SEC filings ≥\geq 2023Q1).

The Average Treatment Effect on the Treated (ATT) is our estimand:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τA​T​T=𝔼​[Yi​t​(1)−Yi​t​(0)∣Di​t=1]\tau^{ATT}=\mathbb{E}[Y\_{it}(1)-Y\_{it}(0)\mid D\_{it}=1] |  | (17) |

This answers the question: “What is the average productivity change caused by AI adoption among banks that chose to adopt?”

#### 3.6.3 The SDID Estimator

SDID improves on standard difference-in-differences by constructing both unit weights and time weights to achieve balance between treated and control groups.

Unit Weights (ω^j\hat{\omega}\_{j}): For each control bank jj, we assign a weight ω^j≥0\hat{\omega}\_{j}\geq 0 (with ∑jω^j=1\sum\_{j}\hat{\omega}\_{j}=1) such that the weighted average of control bank outcomes matches the pre-treatment trajectory of treated banks:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝎^=arg⁡minω​∑t<T0(Y¯1​t−∑j∈Controlωj​Yj​t)2+ζ​‖ω‖22\hat{\boldsymbol{\omega}}=\arg\min\_{\omega}\sum\_{t<T\_{0}}\left(\bar{Y}\_{1t}-\sum\_{j\in\text{Control}}\omega\_{j}Y\_{jt}\right)^{2}+\zeta\|\omega\|\_{2}^{2} |  | (18) |

where Y¯1​t\bar{Y}\_{1t} is the average outcome among treated banks in pre-treatment period tt, T0T\_{0} is the treatment date (2023Q1), and ζ\zeta is a regularization parameter preventing overfitting.

Time Weights (λ^t\hat{\lambda}\_{t}): For each post-treatment period tt, we assign a weight λ^t≥0\hat{\lambda}\_{t}\geq 0 that upweights periods most informative about treatment effects:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀^=arg⁡minλ​∑i∈Control(Y¯i,p​o​s​t−∑t<T0λt​Yi​t)2+ζ​‖λ‖22\hat{\boldsymbol{\lambda}}=\arg\min\_{\lambda}\sum\_{i\in\text{Control}}\left(\bar{Y}\_{i,post}-\sum\_{t<T\_{0}}\lambda\_{t}Y\_{it}\right)^{2}+\zeta\|\lambda\|\_{2}^{2} |  | (19) |

The SDID Estimator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ^S​D​I​D=(Y¯1,p​o​s​t−Y¯1,p​r​eλ)−(Y¯0,p​o​s​tω−Y¯0,p​r​eω,λ)\hat{\tau}^{SDID}=\left(\bar{Y}\_{1,post}-\bar{Y}\_{1,pre}^{\lambda}\right)-\left(\bar{Y}\_{0,post}^{\omega}-\bar{Y}\_{0,pre}^{\omega,\lambda}\right) |  | (20) |

where Y¯1,p​o​s​t\bar{Y}\_{1,post} denotes the average post-treatment outcome for treated banks, Y¯1,p​r​eλ\bar{Y}\_{1,pre}^{\lambda} is the time-weighted pre-treatment average for treated banks, Y¯0,p​o​s​tω\bar{Y}\_{0,post}^{\omega} represents the unit-weighted post-treatment average for control banks, and Y¯0,p​r​eω,λ\bar{Y}\_{0,pre}^{\omega,\lambda} is the doubly-weighted pre-treatment average for control banks.

#### 3.6.4 Advantages Over Standard Difference-in-Differences

Relaxing Parallel Trends: Standard DiD requires that treated and control groups would have followed parallel outcome trajectories absent treatment. This assumption is often violated: AI-adopting banks may have been on different trajectories before adoption due to superior management or earlier technology investments.

SDID does not require parallel trends. Instead, it re-weights the control group to match the treated group’s pre-treatment trajectory perfectly. The synthetic control for JPMorgan, for example, might place large weights on Bank of America and Wells Fargo (similar size and trajectory) and zero weight on community banks (different trajectory).

Doubly Robust Identification: SDID is consistent if either the parallel trends assumption holds (making standard DiD valid) or the synthetic control weights perfectly match pre-treatment outcomes (making synthetic control valid). This “doubly robust” property provides insurance against model misspecification.

Handling Staggered Adoption: Banks adopt AI at different times. SDID handles staggered adoption naturally by defining treatment relative to each bank’s first AI mention.

#### 3.6.5 Inference

We estimate standard errors using the placebo-based bootstrap procedure recommended by Arkhangelsky et al. ([2021](https://arxiv.org/html/2602.02607v1#bib.bib6)). For each bootstrap iteration b=1,…,Bb=1,\ldots,B, we resample banks with replacement while maintaining the treated/control structure, then re-estimate SDID weights and treatment effects. The standard error is computed as the standard deviation of bootstrap estimates: S​E^​(τ^)=1B−1​∑b=1B(τ^(b)−τ¯)2\widehat{SE}(\hat{\tau})=\sqrt{\frac{1}{B-1}\sum\_{b=1}^{B}(\hat{\tau}^{(b)}-\bar{\tau})^{2}}.

We report results based on B=200B=200 bootstrap replications. Confidence intervals are constructed as τ^±1.96×S​E^\hat{\tau}\pm 1.96\times\widehat{SE}.

#### 3.6.6 Event Study Extension

To examine dynamic treatment effects and test for pre-trends, we estimate period-specific ATTs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τk=𝔼​[Yi​t​(1)−Yi​t​(0)∣Di​t=1,t−ti∗=k]\tau\_{k}=\mathbb{E}[Y\_{it}(1)-Y\_{it}(0)\mid D\_{it}=1,t-t\_{i}^{\*}=k] |  | (21) |

where ti∗t\_{i}^{\*} is bank ii’s first treatment quarter and k∈{−4,−3,−2,−1,0,1,2,3,4}k\in\{-4,-3,-2,-1,0,1,2,3,4\} indexes quarters relative to treatment.

This produces the event study plots in Figure [1](https://arxiv.org/html/2602.02607v1#S5.F1 "Figure 1 ‣ 5.3 Event Study Evidence: J-Curve Dynamics ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector"). Pre-treatment coefficients (k<0k<0) serve as a placebo test: if SDID is valid, τ^k\hat{\tau}\_{k} should be statistically indistinguishable from zero for k<0k<0.

### 3.7 Identification Strategy: Complementary Approaches

The DSDM and SDID estimators answer different questions and face different threats to identification:

Table 1: Comparison of Identification Strategies

|  | DSDM | SDID |
| --- | --- | --- |
| Question Answered | Who adopts AI? | What happens after adoption? |
|  | What are network spillovers? | What is the causal effect? |
| Interpretation of β\beta | Selection + Treatment | Pure Treatment Effect (ATT) |
| Identifies Spillovers? | Yes (θ\theta) | No |
| Main Threat | Endogeneity | Violation of SUTVA |
|  | (reverse causality) | (spillovers to control group) |
| Key Assumption | Correct weight matrix | 2023 shock is exogenous |

Reconciling Positive β\beta (DSDM) and Negative ATT (SDID): The DSDM estimate of β>0\beta>0 indicates that AI-adopting banks are more productive than non-adopters on average. This reflects selection: “frontier” institutions with strong management, modern IT infrastructure, and strategic vision are more likely to adopt GenAI. In contrast, the SDID estimate of ATT <0<0 reveals that the act of adoption causes productivity to decline in the short run. This reflects treatment: massive implementation costs—GPUs, data scientists, cloud infrastructure, and “prompt engineering” consultants—immediately reduce net income.

Both findings are consistent with the “Innovation J-Curve” (Brynjolfsson et al., [2021](https://arxiv.org/html/2602.02607v1#bib.bib19)): frontier firms adopt transformative technologies early, accept short-term productivity losses during implementation, and position themselves for long-term competitive advantage.

## 4 Data and Variable Construction

### 4.1 Data Sources

We construct a quarterly panel dataset spanning 2018Q1 to 2025Q4 by integrating four primary data sources:

SEC EDGAR Filings: We extract the complete text of 10-Q quarterly reports and 10-K annual reports for all bank holding companies (SIC codes 6020, 6022, 6029, 6035, 6036, 6141, 6159, 6712). These filings provide the textual data for measuring AI adoption.

Federal Reserve FR Y-9C Reports: Quarterly Consolidated Financial Statements for Bank Holding Companies provide standardized balance sheet and income statement data. Key variables include total assets, total equity, net income, and tier 1 capital.

FFIEC Call Reports: Reports of Condition and Income (Forms 031/041/051) provide additional detail on loan portfolios, deposit composition, and operational metrics for commercial banks.

NY Fed CRSP-FRB Link: The Federal Reserve Bank of New York’s crosswalk file enables matching between SEC CIK identifiers and Federal Reserve RSSD identifiers, achieving a 95.4% match rate through a combination of exact matching and fuzzy name-matching algorithms.

### 4.2 Measuring AI Adoption

We identify GenAI adoption through systematic text analysis of SEC filings. Our keyword dictionary encompasses three categories. Core GenAI terms include “generative AI,” “generative artificial intelligence,” “large language model,” “LLM,” “ChatGPT,” “GPT-4,” “Claude,” “Gemini,” and “Copilot.” Application terms capture deployment contexts: “AI-powered,” “machine learning application,” “natural language processing,” “automated underwriting,” “algorithmic trading,” and “robo-advisor.” Strategic terms identify organizational commitment: “AI strategy,” “artificial intelligence initiative,” “digital transformation,” “AI investment,” and “AI implementation.”

For each filing, we count keyword occurrences and construct two measures:

|  |  |  |  |
| --- | --- | --- | --- |
|  | GenAI\_Mentionsi​t=∑k∈𝒦Count​(k,Filingi​t)\text{GenAI\\_Mentions}\_{it}=\sum\_{k\in\mathcal{K}}\text{Count}(k,\text{Filing}\_{it}) |  | (22) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di​tG​e​n​A​I=𝟏​[GenAI\_Mentionsi​t>0]D\_{it}^{GenAI}=\mathbf{1}[\text{GenAI\\_Mentions}\_{it}>0] |  | (23) |

The treatment indicator Di​tG​e​n​A​ID\_{it}^{GenAI} equals one if bank ii mentions any GenAI-related keyword in quarter tt’s filing.

### 4.3 Outcome Variables

Our primary productivity measures are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​O​Ai​t=Net Incomei​tTotal Assetsi​t×100ROA\_{it}=\frac{\text{Net Income}\_{it}}{\text{Total Assets}\_{it}}\times 100 |  | (24) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​O​Ei​t=Net Incomei​tTotal Equityi​t×100ROE\_{it}=\frac{\text{Net Income}\_{it}}{\text{Total Equity}\_{it}}\times 100 |  | (25) |

Both measures are winsorized at the 1st and 99th percentiles to mitigate the influence of outliers.

### 4.4 Control Variables

We include the following bank-level controls in our DSDM specifications: the natural logarithm of total assets (ln(Assets)i​t\ln(\text{Assets})\_{it}) to capture size effects; the Tier 1 capital ratio (Tier1i​t\text{Tier1}\_{it}) to measure capital adequacy; a technology keyword index from SEC filings (Digitali​t\text{Digital}\_{it}) to proxy for pre-existing digitalization; and the age of the chief executive officer (CEOAgei​t\text{CEOAge}\_{it}) to capture managerial characteristics that may affect technology adoption propensity.

Table [2](https://arxiv.org/html/2602.02607v1#S4.T2 "Table 2 ‣ 4.4 Control Variables ‣ 4 Data and Variable Construction ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") presents formal definitions of all variables used in the empirical analysis.

Table 2: Variable Definitions

| Variable | Definition |
| --- | --- |
| Panel A: Dependent Variables | |
| R​O​Ai​tROA\_{it} | Return on Assets: Net income divided by total assets for bank ii in quarter tt, expressed in percentage points. Winsorized at the 1st and 99th percentiles to mitigate outlier influence. |
| R​O​Ei​tROE\_{it} | Return on Equity: Net income divided by total equity for bank ii in quarter tt, expressed in percentage points. Winsorized at the 1st and 99th percentiles. |
| Panel B: Treatment Variable | |
| Di​tA​ID\_{it}^{AI} | Binary indicator equal to 1 if bank ii mentions GenAI-related keywords (“generative AI,” “large language model,” “ChatGPT,” “GPT-4,” “Claude,” “Gemini,” etc.) in SEC 10-Q filings during quarter tt, and 0 otherwise. |
| Panel C: Control Variables | |
| ln(Assets)i​t\ln(\text{Assets})\_{it} | Natural logarithm of total assets for bank ii in quarter tt. Captures bank size and scale effects on productivity. Larger banks may have different adoption patterns and productivity dynamics. |
| Tier1i​t\text{Tier1}\_{it} | Tier 1 capital ratio: Tier 1 capital divided by risk-weighted assets, expressed in percentage points. Measures capital adequacy and regulatory buffer. Well-capitalized banks may have more flexibility for technology investment. |
| Digitali​t\text{Digital}\_{it} | Digitalization index: Weighted count of technology-related keywords in SEC 10-K filings, normalized by document length. Captures pre-existing digital infrastructure and IT investment intensity. Constructed following established text-analysis methods. |
| CEOAgei​t\text{CEOAge}\_{it} | Age of the CEO in years as of quarter tt, extracted from SEC DEF 14A proxy statements. Captures managerial characteristics that may affect technology adoption propensity and organizational adaptability. |

* •

  Notes: All financial variables are sourced from Federal Reserve FR Y-9C reports. AI adoption is measured from SEC EDGAR 10-Q filings using keyword detection algorithms. CEO age is extracted from DEF 14A proxy statements using automated text parsing. The digitalization index is constructed from 10-K annual filings using a weighted keyword approach covering terms related to cloud computing, automation, data analytics, and digital banking.

### 4.5 Sample Construction

Our initial sample comprises 809 unique bank holding companies. After requiring non-missing values for key variables and a minimum of four quarterly observations, our estimation sample includes 126 banks with complete data, of which 41 are classified as AI adopters (having at least one quarter with positive GenAI mentions) and 85 serve as control banks (zero GenAI mentions throughout the sample period).

Table [3](https://arxiv.org/html/2602.02607v1#S4.T3 "Table 3 ‣ 4.5 Sample Construction ‣ 4 Data and Variable Construction ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") presents summary statistics for the full sample.

Table 3: Summary Statistics

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Variable | N | Mean | SD | P25 | Median | P75 |
| Panel A: Productivity Measures | | | | | | |
| ROA (%) | 13,777 | 1.204 | 1.022 | 0.783 | 1.098 | 1.410 |
| ROE (%) | 13,777 | 10.815 | 6.833 | 7.471 | 10.439 | 13.615 |
| Panel B: Bank Characteristics | | | | | | |
| Total Assets ($B) | 14,064 | 42.67 | 187.3 | 2.14 | 5.82 | 18.41 |
| Log Assets | 14,064 | 16.184 | 1.850 | 15.071 | 15.794 | 17.113 |
| Tier 1 Capital Ratio (%) | 10,910 | 14.881 | 5.618 | 11.364 | 12.741 | 14.869 |
| Digital Index | 12,456 | 0.342 | 0.287 | 0.124 | 0.278 | 0.489 |
| CEO Age (years) | 11,234 | 58.4 | 7.2 | 53 | 58 | 63 |
| Panel C: AI Adoption | | | | | | |
| GenAI Mentions | 66,894 | 0.121 | 2.185 | 0.000 | 0.000 | 0.000 |
| AI Adopter (D=1) | 66,894 | 0.048 | 0.214 | 0.000 | 0.000 | 0.000 |

* •

  Notes: This table reports summary statistics for the main variables in our analysis. The sample covers 809 unique bank holding companies observed quarterly from 2018Q1 to 2025Q4. ROA and ROE are winsorized at the 1st and 99th percentiles. Total Assets are reported in billions of dollars. Digital Index is a normalized weighted count of technology-related keywords in SEC filings. CEO Age is extracted from DEF 14A proxy statements.

## 5 Empirical Results

We present our empirical findings in the following order: first, DSDM estimates capturing network spillovers and the “frontier firm” effect (Section 5.1); second, SDID estimates identifying the causal “Implementation Tax” (Section 5.2); third, event study evidence on J-curve dynamics (Section 5.3); fourth, a unified interpretation reconciling the two approaches (Section 5.4); and finally, network analysis of systemic risk (Section 5.5).

### 5.1 DSDM Estimates: Efficiency Potential and Network Spillovers

Table [4](https://arxiv.org/html/2602.02607v1#S5.T4 "Table 4 ‣ 5.1 DSDM Estimates: Efficiency Potential and Network Spillovers ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") presents estimates from the Dynamic Spatial Durbin Model specified in Equation [3](https://arxiv.org/html/2602.02607v1#S3.E3 "In 3.5.1 Model Specification ‣ 3.5 Econometric Strategy I: Dynamic Spatial Durbin Model (DSDM) ‣ 3 Theoretical Framework and Econometric Strategy ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector"). We report results using both the network weight matrix (Wn​e​t​w​o​r​kW\_{network}) based on asset similarity and the geographic weight matrix (Wg​e​oW\_{geo}) based on headquarters proximity.

Table 4: Dynamic Spatial Durbin Model Estimates: Efficiency Potential and Network Spillovers

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ROA (%) | | ROE (%) | |
|  | Wn​e​t​w​o​r​kW\_{network} | Wg​e​oW\_{geo} | Wn​e​t​w​o​r​kW\_{network} | Wg​e​oW\_{geo} |
|  | (1) | (2) | (3) | (4) |
| Panel A: Direct Effects (Own AI Adoption) | | | | |
| AI Adoption (β\beta) | 0.0373\*\* | 0.0746\*\*\* | 0.4199\*\*\* | 0.6178\*\*\* |
|  | (0.0139) | (0.0212) | (0.0927) | (0.1432) |
| Panel B: Spillover Effects (Network AI Adoption) | | | | |
| W ×\times AI Adoption (θ\theta) | 0.1606\*\*\* | 0.1230\*\* | 0.6787\*\* | 0.6743\* |
|  | (0.0508) | (0.0855) | (0.3361) | (0.5809) |
| Panel C: Spatial Parameters | | | | |
| Temporal Lag (τ\tau) | 0.6363\*\*\* | 0.7127\*\*\* | 0.6967\*\*\* | 0.7816\*\*\* |
|  | (0.0047) | (0.0068) | (0.0044) | (0.0061) |
| Spatial Lag (ρ\rho) | 0.6166\*\*\* | 0.5123\*\*\* | 0.7453\*\*\* | 0.6607\*\*\* |
|  | (0.0170) | (0.0303) | (0.0132) | (0.0243) |
| Spatial-Temporal Lag (η\eta) | −-0.2898\*\*\* | −-0.2769\*\*\* | −-0.4653\*\*\* | −-0.4772\*\*\* |
|  | (0.0168) | (0.0295) | (0.0134) | (0.0238) |
| Panel D: Control Variables | | | | |
| Tier 1 Capital Ratio | 0.087\*\*\* | 0.127\*\*\* | 0.045 | 0.790\*\*\* |
|  | (0.023) | (0.013) | (0.160) | (0.186) |
| Log Assets | −-0.002 | −-0.084\*\*\* | 2.360\*\* | −-0.394\*\*\* |
|  | (0.021) | (0.003) | (1.151) | (0.132) |
| Digital Index | 0.099\*\*\* | −-0.129\*\*\* | −-1.709\*\*\* | −-1.569\*\*\* |
|  | (0.027) | (0.027) | (0.127) | (0.104) |
| CEO Age | 0.003 | 0.012\*\*\* | −-0.479\* | 0.059\*\*\* |
|  | (0.007) | (0.003) | (0.275) | (0.022) |
| Bank Fixed Effects | Yes | Yes | Yes | Yes |
| Time Fixed Effects | Yes | Yes | Yes | Yes |
| Observations | 24,270 | 24,270 | 24,270 | 24,270 |

* •

  Notes: This table reports Bayesian DSDM estimates from the Dynamic Spatial Durbin Model. Wn​e​t​w​o​r​kW\_{network} is constructed based on asset similarity; Wg​e​oW\_{geo} is based on geographic proximity. The positive β\beta indicates that AI-adopting banks exhibit higher productivity (“frontier firm” effect). The positive θ\theta indicates knowledge spillovers dominate business-stealing effects. Standard errors in parentheses from posterior distribution. \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

The DSDM estimates provide several critical insights. First, the direct effect of AI adoption (β\beta) is positive and statistically significant across specifications: 3.7 basis points for ROA and 42 basis points for ROE using the network weight matrix. This positive coefficient confirms Hypothesis 1: AI adoption is associated with higher productivity in the cross-section. AI adopters are “frontier” institutions that outperform non-adopters on average.

The Critical Finding: Positive Spillover Effects. The spillover coefficient θ\theta is positive and statistically significant in most specifications. Using the network weight matrix, θ=0.161\theta=0.161 (p<0.01p<0.01) for ROA and θ=0.679\theta=0.679 (p<0.05p<0.05) for ROE. These positive coefficients confirm Hypothesis 4: when one bank successfully implements AI, it raises productivity at connected institutions through knowledge diffusion rather than eroding it through business-stealing competition.

Control Variable Effects. Panel D reveals important heterogeneity in bank characteristics. Tier 1 capital ratios are positively associated with ROA (0.087, p<0.01p<0.01), suggesting well-capitalized banks maintain higher profitability. The digitalization index shows divergent effects: positive for ROA (0.099, p<0.01p<0.01) but negative for ROE (−1.71-1.71, p<0.01p<0.01), indicating that prior digital investments improve asset efficiency but may require equity-intensive implementation. CEO age exhibits a marginally negative effect on ROE (−0.48-0.48, p<0.10p<0.10), consistent with younger executives being more receptive to transformative technology adoption.

Three mechanisms explain the positive spillovers. First, infrastructure spillovers arise as early adopters develop standardized APIs, data protocols, and integration frameworks that reduce implementation costs for followers. Second, labor market development occurs as the AI talent pool deepens when more banks invest in training, reducing hiring costs and knowledge barriers for subsequent adopters. Third, vendor maturation benefits later adopters as the market for banking AI solutions expands, leading vendors to improve products and reduce prices.

The Systemic Synchronization Warning. The magnitude of θ=0.679\theta=0.679 for ROE is economically significant. A one-standard-deviation increase in network neighbors’ AI adoption is associated with a 68-basis-point improvement in own ROE. This sensitivity means that bank profitability is increasingly synchronized across the AI-adopting core—a pattern we examine further in Section 5.5.

Table [5](https://arxiv.org/html/2602.02607v1#S5.T5 "Table 5 ‣ 5.1 DSDM Estimates: Efficiency Potential and Network Spillovers ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") decomposes the total effect of AI adoption into direct and indirect (spillover) components, following the methodology of LeSage & Pace ([2009](https://arxiv.org/html/2602.02607v1#bib.bib34)).

Table 5: DSDM Marginal Effects Decomposition: The Dominance of Spillovers

|  | ROA (%) | ROE (%) |
| --- | --- | --- |
| Direct Effect | 0.0923\*\* | 0.7634\*\*\* |
|  | (0.0312) | (0.2267) |
| Indirect Effect (Spillovers) | 0.4289\*\*\* | 3.8941\*\*\* |
|  | (0.0934) | (0.8456) |
| Total Effect | 0.5212\*\*\* | 4.6575\*\*\* |
|  | (0.1078) | (0.9234) |
| Indirect/Total Ratio | 82.3% | 83.6% |

* •

  Notes: This table reports the decomposition of AI adoption effects from the DSDM into direct and indirect components following LeSage & Pace ([2009](https://arxiv.org/html/2602.02607v1#bib.bib34)). Direct effects measure the impact of own AI adoption; indirect effects measure the impact transmitted through network connections. The dominance of indirect effects (over 80%) indicates that the banking sector’s productivity response to AI is fundamentally a network phenomenon. Standard errors in parentheses computed via delta method. \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

The decomposition reveals that spillover effects account for over 80% of the total productivity impact of AI adoption. This finding has critical implications: the banking sector’s response to GenAI is fundamentally a network phenomenon rather than an aggregation of independent firm-level decisions. The social returns to AI adoption substantially exceed the private returns captured by individual institutions.

### 5.2 SDID Estimates: The Implementation Tax

While the DSDM reveals network spillover effects and direct associations between AI adoption and productivity, we use SDID to isolate the causal within-unit treatment effect. Table [6](https://arxiv.org/html/2602.02607v1#S5.T6 "Table 6 ‣ 5.2 SDID Estimates: The Implementation Tax ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") presents our SDID estimates using Bayesian inference.

Table 6: Synthetic Difference-in-Differences Estimates: The Implementation Tax

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | Full Sample | Large Banks | Small Banks |
|  |  | (Top 25%) | (Bottom 75%) |
| Panel A: Return on Assets (ROA, %) | | | |
| ATT | −-0.456\*\* | −-0.159\*\*\* | −-0.594\*\* |
|  | (0.177) | (0.053) | (0.282) |
| Panel B: Return on Equity (ROE, %) | | | |
| ATT | −-4.282\*\*\* | −-1.286\*\*\* | −-5.167\*\*\* |
|  | (0.887) | (0.527) | (1.741) |
| Treated Banks | 10 | 4 | 6 |
| Control Banks | 36 | 8 | 28 |

* •

  Notes: This table reports Synthetic Difference-in-Differences estimates of the causal effect of GenAI adoption on bank productivity using Bayesian inference. The treatment is defined as the first quarter in 2023 in which a bank mentions GenAI-related keywords in SEC filings, exploiting the November 2022 ChatGPT release as an exogenous shock. Negative ATT values indicate that AI adoption causes productivity to decline during the implementation phase—the “Implementation Tax.” Standard errors in parentheses from posterior distribution. Large banks are defined as those in the top quartile of average total assets; small banks are in the bottom three quartiles. \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

The aggregate estimates in Column (1) reveal the “Implementation Tax”: AI adoption causes ROA to decline by 46 basis points and ROE to decline by 428 basis points. These negative ATT values reveal that banks incur significant short-term costs when implementing GenAI technologies.

Heterogeneous Effects by Bank Size. The estimates in Columns (2)–(3) reveal a striking pattern that differs from expectations based on economies of scale. Smaller banks (bottom 75% by assets) experience a substantially larger Implementation Tax: an ROE decline of 517 basis points compared to only 129 basis points for larger banks. Similarly, smaller banks suffer a 59-basis-point ROA decline versus 16 basis points for larger institutions.

This asymmetry suggests that larger banks benefit from economies of scale in AI implementation, superior integration capabilities, and deeper capital reserves to absorb transition costs. Smaller banks face proportionally larger implementation burdens relative to their equity base, amplifying the ROE impact even though absolute dollar costs may be lower.

Implications for Competition. The differential Implementation Tax has important competitive implications. Capital constraints pose particular challenges for smaller banks: those with thinner capital buffers face proportionally larger equity impacts, potentially limiting their ability to sustain AI investments over multiple quarters. Scale advantages favor larger institutions, which can spread fixed implementation costs—including data infrastructure, talent acquisition, and vendor integration—across a broader asset base, thereby reducing per-unit costs. Network effects may also disadvantage smaller banks: as documented in our DSDM results, larger banks that adopt early generate positive spillovers benefiting later adopters, but smaller banks may lack the network centrality to fully capture these knowledge transfers.

### 5.3 Event Study Evidence: J-Curve Dynamics

Figure [1](https://arxiv.org/html/2602.02607v1#S5.F1 "Figure 1 ‣ 5.3 Event Study Evidence: J-Curve Dynamics ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") presents dynamic treatment effects from the SDID event study specification, providing evidence on Hypothesis 2.

![Refer to caption](figures/figure1_event_study_roa.png)


(a) ATT on ROA (%)

![Refer to caption](figures/figure1_event_study_roe.png)


(b) ATT on ROE (%)

Figure 1: Dynamic Treatment Effects of AI Adoption (SDID Event Study). The dashed vertical line indicates the quarter of first GenAI mention in SEC filings. Error bars represent 95% confidence intervals based on 200 bootstrap replications.

Several patterns emerge from Figure [1](https://arxiv.org/html/2602.02607v1#S5.F1 "Figure 1 ‣ 5.3 Event Study Evidence: J-Curve Dynamics ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector"). First, we observe a sharp structural break at t=0t=0. In Panel (a), the ATT on ROA improves from approximately −0.10%-0.10\% in the quarter immediately preceding adoption to +0.30%+0.30\% in the adoption quarter. This 40-basis-point improvement is economically substantial and statistically significant.

Second, the pre-treatment coefficients are uniformly negative and trending downward, consistent with a J-curve interpretation: banks experience declining relative performance in the quarters leading up to AI adoption as they invest in preparatory infrastructure. The sharp reversal at t=0t=0 suggests that adoption itself marks a turning point.

Third, Panel (b) reveals a more complex pattern for ROE. The pre-treatment decline is more pronounced (reaching −3.1%-3.1\% at t=−1t=-1), reflecting the leverage-amplified impact of transition costs on equity returns. Following adoption, ROE improves substantially, representing a 190-basis-point improvement relative to the pre-treatment trend.

These patterns are consistent with Hypothesis 2: the productivity impact of GenAI adoption follows a J-curve dynamic with initial decline followed by recovery.

### 5.4 Reconciling DSDM and SDID: Selection vs. Treatment

Table [7](https://arxiv.org/html/2602.02607v1#S5.T7 "Table 7 ‣ 5.4 Reconciling DSDM and SDID: Selection vs. Treatment ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") summarizes the apparent contradiction between our two estimation approaches and provides a unified interpretation.

Table 7: Reconciling DSDM and SDID: Efficiency Potential vs. Implementation Cost

|  |  |  |
| --- | --- | --- |
|  | DSDM | SDID |
|  | (Cross-Sectional) | (Causal/Within-Unit) |
| Panel A: Direct AI Effect (β\beta / ATT) | | |
| ROA Effect | ++0.037\*\* | −-0.456\*\* |
| ROE Effect | ++0.420\*\*\* | −-4.282\*\*\* |
| Panel B: Interpretation | | |
| What it measures | Selection effect | Treatment effect |
|  | (Who adopts?) | (What happens after?) |
| Economic meaning | “Frontier firms” adopt AI | Adoption causes |
|  | →\rightarrow positive association | implementation costs |
| Panel C: Spillover Effects (θ\theta) | | |
| ROA Spillover | ++0.161\*\*\* | — |
| ROE Spillover | ++0.679\*\* | — |
| Interpretation | Knowledge diffusion |  |
|  | dominates business-stealing |  |

* •

  Notes: This table reconciles the apparently contradictory findings from DSDM and SDID estimation. The positive DSDM coefficient (β>0\beta>0) reflects selection: high-performing “frontier” banks are more likely to adopt AI. The negative SDID estimate (ATT <0<0) reflects causation: the act of adoption imposes implementation costs that reduce productivity during the transition period. Both findings are consistent with the “Innovation J-Curve” hypothesis. \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05.

The reconciliation framework resolves the paradox through a distinction between selection and treatment effects:

Selection (DSDM, β>0\beta>0): High-performing banks—those with strong management, modern IT infrastructure, and strategic vision—are more likely to adopt GenAI. In the cross-section, AI adoption is positively correlated with productivity because frontier firms select into treatment.

Treatment (SDID, ATT <0<0): Conditional on the adoption decision, the act of implementing GenAI causes productivity to decline as banks absorb massive current expenses. The negative ATT reflects the implementation costs that even frontier firms must bear.

This pattern is the signature of a general-purpose technology in its early diffusion phase. The firms best positioned to benefit from AI are the first to adopt, but even they must traverse the valley of the J-Curve before realizing productivity gains.

### 5.5 Network Analysis and Systemic Synchronization Risk

Table [8](https://arxiv.org/html/2602.02607v1#S5.T8 "Table 8 ‣ 5.5 Network Analysis and Systemic Synchronization Risk ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") presents DSDM estimates separately for large (Top 25%) and small (Bottom 75%) banks, revealing a critical asymmetry in spillover dynamics.

Table 8: DSDM Heterogeneity: Large vs. Small Banks (Network Weight Matrix)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Large Banks (Top 25%) | | Small Banks (Bottom 75%) | |
|  | ROA | ROE | ROA | ROE |
| Panel A: Direct Effects | | | | |
| AI Adoption (β\beta) | 0.0441\*\*\* | 0.3622\*\*\* | 0.0381\*\* | 0.4730\*\*\* |
|  | (0.0096) | (0.0848) | (0.0152) | (0.0957) |
| Panel B: Spillover Effects | | | | |
| W ×\times AI Adoption (θ\theta) | 0.3466\*\*\* | 3.1272\*\*\* | 0.1055\*\* | 0.1502 |
|  | (0.0443) | (0.3934) | (0.0522) | (0.3243) |
| Spatial Lag (ρ\rho) | 0.6787\*\*\* | 0.7039\*\*\* | 0.5999\*\*\* | 0.7522\*\*\* |
|  | (0.0142) | (0.0140) | (0.0176) | (0.0130) |
| Temporal Lag (τ\tau) | 0.7313\*\*\* | 0.7150\*\*\* | 0.6178\*\*\* | 0.6918\*\*\* |
|  | (0.0046) | (0.0046) | (0.0048) | (0.0045) |
| Observations | 24,270 | 24,270 | 24,270 | 24,270 |

* •

  Notes: This table reports Bayesian DSDM estimates using the network weight matrix (Wn​e​t​w​o​r​kW\_{network}) separately for large and small banks. The dramatically larger spillover coefficient (θ=3.13\theta=3.13) for large bank ROE indicates that the systemic core of major institutions is highly synchronized—a one-standard-deviation increase in peer AI adoption raises own ROE by 313 basis points. Small banks exhibit much weaker and often insignificant spillover effects. \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

The Systemic Core: Large Bank Synchronization. Table [8](https://arxiv.org/html/2602.02607v1#S5.T8 "Table 8 ‣ 5.5 Network Analysis and Systemic Synchronization Risk ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") reveals a striking asymmetry. For large banks, the spillover coefficient θ\theta is massive: 0.35 for ROA and an extraordinary 3.13 for ROE. For small banks, spillovers are modest (0.11 for ROA) or statistically insignificant (0.15 for ROE). This pattern has profound implications for systemic risk.

The large positive θ\theta for major institutions indicates that AI-adopting banks are not merely co-located in network space—their profitability is causally linked through AI adoption dynamics. When JPMorgan successfully deploys a GenAI system, Bank of America and Citigroup experience measurable improvements in their own performance, likely through competitive imitation, talent acquisition, or vendor ecosystem development.

This synchronization is precisely what financial stability regulators should monitor. The positive spillovers that enhance productivity in normal times become transmission mechanisms for correlated failures during stress. If a vulnerability emerges in a widely-used LLM architecture, or if regulatory action restricts AI deployment, the synchronized response of the systemic core could amplify rather than dampen the shock.

Figure [2](https://arxiv.org/html/2602.02607v1#S5.F2 "Figure 2 ‣ 5.5 Network Analysis and Systemic Synchronization Risk ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") visualizes the interbank AI network, revealing the structural foundations of algorithmic coupling.

![Refer to caption](figures/figure2_network_twopanel.png)


Figure 2: Interbank AI Network Visualization. Left panel: Full network with nodes colored by AI adoption score (blue = low, red = high) and sized by total assets. Edges represent asset-similarity connections. Right panel: Systemic core of AI-adopting banks with red edges indicating AI-to-AI connections. The dense clustering illustrates the “algorithmic coupling” that creates new systemic risk channels.

The left panel of Figure [2](https://arxiv.org/html/2602.02607v1#S5.F2 "Figure 2 ‣ 5.5 Network Analysis and Systemic Synchronization Risk ‣ 5 Empirical Results ‣ The Innovation Tax: Generative AI Adoption, Productivity Paradox, and Systemic Risk in the U.S. Banking Sector") displays the full bank network, with nodes colored by AI adoption intensity and sized by total assets. The right panel isolates the “systemic core”—banks with positive GenAI mentions and their immediate network neighbors.

The Emergence of Algorithmic Coupling. Several features of this network topology are concerning from a financial stability perspective. Dense core clustering characterizes the AI-adopting banks (red nodes), which exhibit higher clustering coefficients than non-adopters; they are more densely connected to each other than to the network periphery, forming a tightly-coupled core. Short path lengths facilitate rapid contagion: the average path length between AI-adopting banks is substantially shorter than the network average, meaning shocks can propagate rapidly through the AI-adopting core. Hub vulnerability compounds these risks, as several large AI-adopting institutions serve as “hubs” with disproportionate connectivity; a disruption at these nodes would cascade through the network. Finally, model homogeneity creates correlated vulnerabilities: while not directly observable in our data, industry reports suggest that AI-adopting banks rely heavily on similar LLM architectures (GPT-4, Claude, Gemini) and vendor solutions, creating shared technical failure modes.

This “algorithmic contagion” operates through channels distinct from traditional financial contagion. Unlike credit and liquidity linkages that connect banks through balance sheet exposures, algorithmic coupling connects banks through shared decision-making processes. Two banks with no direct financial relationship can nonetheless be systemically linked if they rely on similar AI models for risk management, trading, and credit allocation.

## 6 Robustness Checks

We conduct several robustness checks to validate our main findings.

### 6.1 Alternative Treatment Definitions

Our baseline treatment is defined as the first quarter with any GenAI mention. We examine robustness to alternative definitions: an intensity treatment using continuous GenAI mention counts rather than binary adoption; a persistent treatment requiring mentions in two consecutive quarters; and a substantive treatment excluding mentions in boilerplate risk disclosures. Results (reported in the Online Appendix) are qualitatively similar across all definitions.

### 6.2 Alternative Weight Matrices

We examine sensitivity to spatial weight matrix specification, constructing alternatives based on geographic proximity using headquarters distance, business model similarity based on loan portfolio composition, and regulatory grouping based on Fed district membership. The spillover coefficient θ\theta remains positive and significant across all specifications, though magnitudes vary.

### 6.3 Placebo Tests

We implement two placebo tests: a pre-treatment placebo re-estimating with treatment date shifted to 2020Q1 (pre-ChatGPT), and a random assignment placebo randomly reassigning treatment status across banks. Neither placebo produces significant effects, supporting the validity of our identification strategy.

## 7 Conclusion

This paper provides the first comprehensive empirical analysis of Generative AI adoption in the U.S. banking sector, revealing a complex phenomenon that defies simple characterization. Using a novel dataset linking SEC filings to Federal Reserve regulatory data for 809 financial institutions, and employing both Dynamic Spatial Durbin Models and Synthetic Difference-in-Differences, we document a series of findings with significant implications for productivity, competition, and financial stability.

### 7.1 The Productivity Paradox Resolved

Our central finding is a striking Productivity Paradox. The DSDM results show that AI-adopting banks are high performers (β>0\beta>0)—AI adoption is a marker of “frontier” institutions with strong management and modern infrastructure. Yet our causal SDID analysis reveals that the act of adoption causes productivity to decline: the average adopting bank experiences a 428-basis-point drop in ROE as it absorbs the costs of GenAI integration.

This paradox resolves through the lens of the Innovation J-Curve. Banks are in the “Investment Phase” of a transformative technology, incurring massive current expenses—GPUs, data scientists, cloud infrastructure, prompt engineering consultants—that depress net income even as they position institutions for future competitive advantage. The negative ATT is not evidence that AI adoption is misguided; it is the classic signature of a general-purpose technology in its early diffusion stage.

### 7.2 The Digital Divide

We document substantial heterogeneity in the Implementation Tax. Smaller banks (bottom 75% by assets) experience an ROE decline of 517 basis points—substantially larger than the 129-basis-point impact on larger institutions. This asymmetry suggests that economies of scale provide significant advantages in AI implementation: larger banks can spread fixed implementation costs across a broader asset base, employ dedicated AI teams, and leverage superior data infrastructure.

Smaller banks face proportionally larger implementation burdens relative to their equity base. This dynamic suggests an emerging two-tier banking system: large institutions leveraging their scale advantages to absorb implementation costs more efficiently, while smaller banks face disproportionate transition challenges that may limit their ability to compete in an AI-driven financial services landscape.

### 7.3 Systemic Synchronization Risk

Perhaps our most consequential finding concerns network dynamics. The DSDM spillover parameter θ\theta is positive and significant (θ=0.161\theta=0.161 for ROA; θ=0.679\theta=0.679 for ROE), indicating that AI adoption generates knowledge spillovers rather than business-stealing competition. For large banks, these spillovers are dramatically amplified (θ=3.13\theta=3.13 for ROE), indicating that the U.S. banking system’s largest institutions have become algorithmically coupled.

The implications are profound. A high positive θ\theta means that bank profitability is increasingly synchronized across the AI-adopting core. The same knowledge spillovers that benefit banks in normal times become transmission channels for correlated failures under stress. If a widely-used LLM exhibits systematic errors, if a critical AI vendor experiences disruption, or if regulatory action restricts AI deployment, the synchronized nature of AI adoption ensures that all connected banks would be affected simultaneously.

### 7.4 Policy Implications

Our findings carry several policy implications:

Monetary Policy Transmission: The Implementation Tax may alter how banks respond to interest rate changes during the AI transition period. Depressed profitability could reduce lending capacity, potentially dampening policy transmission through the bank lending channel.

Financial Stability Regulation: The emergence of algorithmic coupling warrants new supervisory tools focused on AI model diversity, concentration risk in AI vendor relationships, and operational resilience of AI infrastructure. Stress tests should incorporate scenarios of coordinated AI system failures.

Competition Policy: The two-tier dynamic raises concerns about market concentration. If only the largest institutions can afford the Implementation Tax, the long-term competitive landscape may shift toward oligopoly. Policymakers should consider whether regulatory sandboxes or shared infrastructure initiatives could reduce barriers for smaller institutions.

Macroprudential Policy: The high θ\theta suggests that AI adoption has become a systemically important activity. Just as certain institutions are “too big to fail,” certain AI systems may be “too connected to fail.” Macroprudential frameworks should evolve to address this new dimension of systemic risk.

### 7.5 Limitations and Future Research

Several limitations suggest avenues for future work. Our treatment measure relies on disclosed AI adoption in SEC filings, which may understate actual implementation. Our sample period captures only the initial phase of GenAI diffusion; longer-term effects as the J-Curve completes may differ substantially. Our network analysis is based on asset similarity rather than actual AI vendor relationships; richer data on technology infrastructure would enable more precise spillover estimation.

Future research should examine the completion of the J-Curve as implementation costs decline and productivity benefits materialize. The evolution of θ\theta over time—whether strategic complementarity intensifies or competitive dynamics reassert—will determine the ultimate trajectory of systemic synchronization risk. The interaction between AI adoption and monetary policy transmission, credit allocation, and financial inclusion merit sustained scholarly attention.

Despite these limitations, this paper documents a technological transformation of historic significance. The U.S. banking system is undergoing fundamental restructuring as institutions invest billions in AI infrastructure, accept short-term productivity losses, and become increasingly interconnected through shared algorithmic decision-making. Understanding this transformation—its productivity effects, competitive dynamics, and systemic implications—is essential for policymakers, regulators, and market participants navigating the AI era in finance.

## References

* Abadie et al. (2010)

  Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies: Estimating the effect of California’s tobacco control program. Journal of the American Statistical Association, 105(490), 493–505.
* Acemoglu & Restrepo (2018)

  Acemoglu, D., & Restrepo, P. (2018). The race between man and machine: Implications of technology for growth, factor shares, and employment. American Economic Review, 108(6), 1488–1542.
* Acemoglu et al. (2015)

  Acemoglu, D., Ozdaglar, A., & Tahbaz-Salehi, A. (2015). Systemic risk and stability in financial networks. American Economic Review, 105(2), 564–608.
* Agrawal et al. (2018)

  Agrawal, A., Gans, J., & Goldfarb, A. (2018). Prediction Machines: The Simple Economics of Artificial Intelligence. Harvard Business Press.
* Allen & Gale (2000)

  Allen, F., & Gale, D. (2000). Financial contagion. Journal of Political Economy, 108(1), 1–33.
* Arkhangelsky et al. (2021)

  Arkhangelsky, D., Athey, S., Hirshberg, D. A., Imbens, G. W., & Wager, S. (2021). Synthetic difference-in-differences. American Economic Review, 111(12), 4088–4118.
* Autor (2022)

  Autor, D. (2022). The labor market impacts of technological change: From unbridled enthusiasm to qualified optimism to vast uncertainty. NBER Working Paper No. 30074.
* Banerjee et al. (2013)

  Banerjee, A., Chandrasekhar, A. G., Duflo, E., & Jackson, M. O. (2013). The diffusion of microfinance. Science, 341(6144), 1236498.
* Bao & Huang (2020)

  Bao, Z., & Huang, D. (2020). Shadow banking in a crisis: Evidence from FinTech during COVID-19. Journal of Financial and Quantitative Analysis, forthcoming.
* Bartlett et al. (2022)

  Bartlett, R., Morse, A., Stanton, R., & Wallace, N. (2022). Consumer-lending discrimination in the FinTech era. Journal of Financial Economics, 143(1), 30–56.
* Battiston et al. (2012)

  Battiston, S., Puliga, M., Kaushik, R., Tasca, P., & Caldarelli, G. (2012). DebtRank: Too central to fail? Financial networks, the FED and systemic risk. Scientific Reports, 2(1), 1–6.
* Berg et al. (2022)

  Berg, T., Burg, V., Gombović, A., & Puri, M. (2022). On the rise of FinTechs: Credit scoring using digital footprints. Review of Financial Studies, 33(7), 2845–2897.
* Berger (1999)

  Berger, A. N. (1999). The “Big Picture” about relationship-based finance. Federal Reserve Bank of Chicago Conference Proceedings, 390–429.
* Berger (2003)

  Berger, A. N. (2003). The economic effects of technological progress: Evidence from the banking industry. Journal of Money, Credit and Banking, 35(2), 141–176.
* Berger et al. (2005)

  Berger, A. N., Miller, N. H., Petersen, M. A., Rajan, R. G., & Stein, J. C. (2005). Does function follow organizational form? Evidence from the lending practices of large and small banks. Journal of Financial Economics, 76(2), 237–269.
* Bresnahan et al. (2002)

  Bresnahan, T. F., Brynjolfsson, E., & Hitt, L. M. (2002). Information technology, workplace organization, and the demand for skilled labor: Firm-level evidence. Quarterly Journal of Economics, 117(1), 339–376.
* Brynjolfsson (1993)

  Brynjolfsson, E. (1993). The productivity paradox of information technology. Communications of the ACM, 36(12), 66–77.
* Brynjolfsson & Hitt (2000)

  Brynjolfsson, E., & Hitt, L. M. (2000). Beyond computation: Information technology, organizational transformation and business performance. Journal of Economic Perspectives, 14(4), 23–48.
* Brynjolfsson et al. (2021)

  Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. American Economic Journal: Macroeconomics, 13(1), 333–372.
* Brynjolfsson et al. (2023)

  Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). Generative AI at work. NBER Working Paper No. 31161.
* Buchak et al. (2018)

  Buchak, G., Matvos, G., Piskorski, T., & Seru, A. (2018). Fintech, regulatory arbitrage, and the rise of shadow banks. Journal of Financial Economics, 130(3), 453–483.
* David (1990)

  David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. American Economic Review, 80(2), 355–361.
* Dell’Acqua et al. (2023)

  Dell’Acqua, F., McFowland, E., Mollick, E. R., et al. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. Harvard Business School Working Paper 24-013.
* Elhorst (2014)

  Elhorst, J. P. (2014). Spatial Econometrics: From Cross-Sectional Data to Spatial Panels. Springer.
* Elliott et al. (2014)

  Elliott, M., Golub, B., & Jackson, M. O. (2014). Financial networks and contagion. American Economic Review, 104(10), 3115–3153.
* Frame et al. (2014)

  Frame, W. S., Wall, L. D., & White, L. J. (2014). Technological change and financial innovation in banking: Some implications for FinTech. In Oxford Handbook of Banking (3rd ed.).
* Fuster et al. (2019)

  Fuster, A., Plosser, M., Schnabl, P., & Vickery, J. (2019). The role of technology in mortgage lending. Review of Financial Studies, 32(5), 1854–1899.
* Gensler & Bailey (2020)

  Gensler, G., & Bailey, L. (2020). Deep learning and financial stability. MIT Working Paper.
* Gu et al. (2020)

  Gu, S., Kelly, B., & Xiu, D. (2020). Empirical asset pricing via machine learning. Review of Financial Studies, 33(5), 2223–2273.
* Jackson (2017)

  Jackson, M. O. (2017). A typology of social capital and associated network measures. Social Choice and Welfare, 49(3), 573–586.
* Jagtiani & Lemieux (2018)

  Jagtiani, J., & Lemieux, C. (2018). Do fintech lenders penetrate areas that are underserved by traditional banks? Journal of Economics and Business, 100, 43–54.
* Jorgenson & Stiroh (2000)

  Jorgenson, D. W., & Stiroh, K. J. (2000). Raising the speed limit: US economic growth in the information age. Brookings Papers on Economic Activity, 2000(1), 125–211.
* Korinek & Suh (2024)

  Korinek, A., & Suh, J. (2024). Scenarios for the transition to AGI. NBER Working Paper No. 32255.
* LeSage & Pace (2009)

  LeSage, J., & Pace, R. K. (2009). Introduction to Spatial Econometrics. CRC Press.
* Noy & Zhang (2023)

  Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. Science, 381(6654), 187–192.
* Oliner & Sichel (2000)

  Oliner, S. D., & Sichel, D. E. (2000). The resurgence of growth in the late 1990s: Is information technology the story? Journal of Economic Perspectives, 14(4), 3–22.
* OpenAI (2023)

  OpenAI. (2023). GPT-4 technical report. arXiv preprint arXiv:2303.08774.
* Petersen & Rajan (2002)

  Petersen, M. A., & Rajan, R. G. (2002). Does distance still matter? The information revolution in small business lending. Journal of Finance, 57(6), 2533–2570.
* Philippon (2016)

  Philippon, T. (2016). The FinTech opportunity. NBER Working Paper No. 22476.
* Solow (1987)

  Solow, R. M. (1987). We’d better watch out. New York Times Book Review, July 12, 36.