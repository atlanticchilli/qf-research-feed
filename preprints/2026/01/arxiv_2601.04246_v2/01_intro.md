---
authors:
- Tatsuru Kikuchi
doc_id: arxiv:2601.04246v2
family_id: arxiv:2601.04246
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network
  Approach'
url_abs: http://arxiv.org/abs/2601.04246v2
url_html: https://arxiv.org/html/2601.04246v2
venue: arXiv q-fin
version: 2
year: 2026
---


Tatsuru Kikuchi111e-mail: tatsuru.kikuchi@e.u-tokyo.ac.jp

((January 9, 2026))

###### Abstract

This paper develops a unified framework for analyzing technology adoption in financial networks that incorporates spatial spillovers, network externalities, and their interaction. The framework characterizes adoption dynamics through a master equation whose solution admits a Feynman-Kac representation as expected cumulative adoption pressure along stochastic paths through spatial-network space. From this representation, I derive the Adoption Amplification Factor—a structural measure of technology leadership that captures the ratio of total system-wide adoption to initial adoption following a localized shock. A Lévy jump-diffusion extension with state-dependent jump intensity captures critical mass dynamics: below threshold, adoption evolves through gradual diffusion; above threshold, cascade dynamics accelerate adoption through discrete jumps. Applying the framework to SWIFT gpi adoption among 17 Global Systemically Important Banks, I find strong support for the two-regime characterization. Network-central banks adopt significantly earlier (ρ=−0.69\rho=-0.69, p=0.002p=0.002), and pre-threshold adopters have significantly higher amplification factors than post-threshold adopters (11.81 versus 7.83, p=0.010p=0.010). Founding members, representing 29 percent of banks, account for 39 percent of total system amplification—sufficient to trigger cascade dynamics. Controlling for firm size and network position, CEO age delays adoption by 11–15 days per year.

JEL Classification: O33, D85, L14, G21

Keywords: Technology adoption; Network externalities; Coordination failures; Levy processes; Critical mass dynamics; Financial technology

## 1 Introduction

Technology adoption in networked markets exhibits distinctive dynamics that standard models struggle to capture. When the value of a technology depends on how many others have adopted—the defining feature of network externalities—coordination failures can trap markets in inefficient equilibria even when superior technologies are available. The transition from legacy payment systems to modern financial technology illustrates these dynamics vividly: banks benefit from new payment platforms only if their counterparties also adopt, and counterparties invest in integration only if enough banks participate. This coordination problem can sustain a low-adoption equilibrium indefinitely, even when all parties would prefer universal adoption.

Recent empirical work has documented both the importance of coordination frictions and the potential for policy to overcome them. Crouzet et al. ([2023](https://arxiv.org/html/2601.04246v2#bib.bib8)) show that India’s demonetization—a large but temporary shock to cash availability—produced persistent increases in digital wallet adoption, with complementarities accounting for 45 percent of the adoption response. Higgins ([2024](https://arxiv.org/html/2601.04246v2#bib.bib17)) demonstrates that government distribution of debit cards to poor households in Mexico triggered supply-side adoption of point-of-sale terminals, which then spilled over to increase other consumers’ card adoption by 21 percent. These findings confirm that coordination failures constrain technology diffusion and that coordinated shocks can shift economies to superior equilibria.

This paper develops a unified framework that captures three distinct channels of technology spillovers in financial networks: spatial spillovers reflecting geographic clustering of adopters, network spillovers reflecting adoption by business partners and counterparties, and the interaction between these channels that arises when geographic neighbors are also network-connected. Existing studies of network externalities focus exclusively on network linkages, neglecting spatial spillovers that arise from geographic proximity. However, financial institutions form business relationships disproportionately with geographic neighbors due to information advantages, regulatory similarities, and historical ties. The spatial-network interaction—absent from existing models—captures amplification when both channels operate simultaneously, which is empirically important in financial technology settings. The framework contributes to understanding the externality structure of financial networks in three ways. First, the Adoption Amplification Factor quantifies externalities by measuring how much a shock at one institution affects the entire system beyond the direct effect. Second, the channel decomposition reveals whether externalities flow primarily through network linkages, geographic proximity, or their interaction. Third, the Feynman-Kac representation provides a path-based interpretation: externalities propagate along all possible paths of economic linkage, weighted by probability and discounted by adjustment frictions.

A central methodological contribution is extending the baseline diffusion framework to incorporate Lévy jump-diffusion dynamics with state-dependent intensity. The baseline continuous model describes gradual adoption transmission appropriate for the pre-critical-mass regime, where institutions learn from neighbors and incrementally adjust adoption decisions. However, technology adoption often exhibits sudden cascades once critical mass is reached—adoption spreads rapidly through positive feedback as network effects dominate individual cost-benefit calculations. The Lévy extension captures these dynamics by adding a jump operator 𝒥​[τ]\mathcal{J}[\tau] whose intensity depends on the current adoption level: λJ​(τ)=λ0+(λ1−λ0)⋅H​(τ−τ¯∗)\lambda\_{J}(\tau)=\lambda\_{0}+(\lambda\_{1}-\lambda\_{0})\cdot H(\tau-\bar{\tau}^{\*}), where H​(⋅)H(\cdot) is the Heaviside function and τ¯∗\bar{\tau}^{\*} is the critical mass threshold. Below threshold, jumps are rare (λJ≈λ0\lambda\_{J}\approx\lambda\_{0}) and diffusion dominates; above threshold, jump intensity increases to λ1≫λ0\lambda\_{1}\gg\lambda\_{0}, generating rapid cascades. In the limit λ0→0\lambda\_{0}\to 0 and λ1→∞\lambda\_{1}\to\infty, the framework converges to deterministic cascade models, clarifying that continuous and discrete approaches describe different regimes of the same phenomenon. This nesting relationship unifies the gradual diffusion models of Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)) with the tipping point dynamics emphasized in Katz and Shapiro ([1985](https://arxiv.org/html/2601.04246v2#bib.bib19)) and Arthur ([1989](https://arxiv.org/html/2601.04246v2#bib.bib4)).

The theoretical contribution centers on demonstrating that the continuous spatial-network framework nests several canonical models from the technology adoption and dynamic coordination literatures as special cases through explicit discretization. The Katz-Shapiro model of network externalities and compatibility corresponds to the discrete network steady state, with the externality function identified as v​(ni)=νn​∑jGi​j​τj/κv(n\_{i})=\nu\_{n}\sum\_{j}G\_{ij}\tau\_{j}/\kappa. The Frankel-Pauzner model of dynamic coordination, which shows how aggregate shocks can resolve multiple equilibria, emerges when spatial and network dimensions collapse to a single aggregate state, with strategic complementarity parameter (νs+νn)/κ(\nu\_{s}+\nu\_{n})/\kappa. The Guimaraes-Machado-Pereira framework of dynamic coordination with timing frictions maps directly to the decay parameter: their Poisson arrival rate of revision opportunities λ\lambda equals the adjustment rate κ\kappa in the master equation. Standard technology adoption hazard models correspond to the case where diffusion coefficients are zero (νs=νn=0\nu\_{s}=\nu\_{n}=0). These nesting relationships, established through the discrete Feynman-Kac formula, demonstrate that the framework is not an exotic alternative but a unification that reveals the common structure underlying conventional methods.

The framework yields several insights for technology policy in financial systems. The Adoption Amplification Factor identifies technology leaders whose adoption decisions have outsized influence on system-wide outcomes. Targeting subsidies or pilot programs at high-amplification institutions maximizes spillovers per dollar spent. The channel decomposition reveals whether adoption spreads primarily through geographic proximity, business relationships, or their interaction, informing whether policy should target geographic clusters, network hubs, or institutions that are central on both dimensions. The critical mass analysis provides guidance on intervention size: temporary interventions must push adoption above threshold to produce permanent effects, and the Lévy extension characterizes the threshold condition as ∫0TI​(s)⋅𝒜​(s)​𝑑s>τ¯∗−τ¯0\int\_{0}^{T}I(s)\cdot\mathcal{A}(s)\,ds>\bar{\tau}^{\*}-\bar{\tau}\_{0}, where cumulative amplified intervention effects must exceed the gap between initial adoption and critical mass.

I apply the framework to study SWIFT gpi adoption among Global Systemically Important Banks in 2017. SWIFT gpi represents a major technological upgrade to interbank payment messaging, offering same-day settlement, end-to-end tracking, and confirmation of credit to beneficiary accounts. The adoption pattern provides a natural test of the framework’s predictions: banks with higher amplification factors—those more central in the combined spatial-network structure—should be earlier adopters. The empirical analysis confirms this prediction strongly (ρ=−0.69\rho=-0.69, p=0.002p=0.002), with network-central banks adopting significantly earlier than peripheral banks. Founding members, representing 29 percent of banks in the sample, account for 39 percent of total system amplification, confirming that high-amplification institutions lead adoption. The two-regime dynamics predicted by the Lévy extension are evident in the data: pre-threshold adopters have significantly higher amplification factors than post-threshold adopters (11.81 versus 7.83, p=0.010p=0.010), and the cumulative adoption curve exhibits classic S-curve dynamics. Controlling for network position reveals the role of firm-level characteristics: CEO age delays adoption by 11–15 days per year conditional on firm size and network centrality.

The paper proceeds as follows. Section 2 develops the theoretical framework, beginning with the coordinate system and adoption representation, deriving the master equation from three independent economic foundations (heterogeneous agent aggregation, market equilibrium, and cost minimization), presenting the complete master equation with spatial-network interaction, establishing the Feynman-Kac representation and its discrete analog, deriving the Adoption Amplification Factor, demonstrating connections to conventional models through explicit mathematical identification, and extending to Lévy jump-diffusion with state-dependent intensity to capture critical mass dynamics. Section 3 presents Monte Carlo evidence validating the amplification factor as a predictor of technology leadership and demonstrating threshold dynamics. Section 4 applies the framework to SWIFT gpi adoption among Global Systemically Important Banks, presenting the empirical specification, regression results, and evidence for two-regime dynamics. Section 5 concludes.

### 1.1 Related Literature

This paper connects to several strands of literature on technology adoption, network externalities, and dynamic coordination.

The foundational analysis of network externalities begins with Katz and Shapiro ([1985](https://arxiv.org/html/2601.04246v2#bib.bib19)), who distinguish direct network effects from indirect network effects arising in two-sided markets. Katz and Shapiro ([1986](https://arxiv.org/html/2601.04246v2#bib.bib20)) analyze technology adoption in the presence of network externalities, showing that the market may fail to adopt a superior technology due to coordination failure. Farrell and Saloner ([1985](https://arxiv.org/html/2601.04246v2#bib.bib10)) study standardization when firms have private information about technology value. The subsequent literature has explored path dependence and lock-in (Arthur, [1989](https://arxiv.org/html/2601.04246v2#bib.bib4); David, [1985](https://arxiv.org/html/2601.04246v2#bib.bib9)), with Liebowitz and Margolis ([1994](https://arxiv.org/html/2601.04246v2#bib.bib22)) and Guimaraes and Pereira ([2016](https://arxiv.org/html/2601.04246v2#bib.bib15)) providing important qualifications about when lock-in to inferior technologies actually occurs.

The theoretical foundations for equilibrium selection in coordination games develop in two related traditions. The global games approach, pioneered by Carlsson and Van Damme ([1993](https://arxiv.org/html/2601.04246v2#bib.bib7)) and extended by Morris and Shin ([1998](https://arxiv.org/html/2601.04246v2#bib.bib23), [2003](https://arxiv.org/html/2601.04246v2#bib.bib24)) and Frankel et al. ([2003](https://arxiv.org/html/2601.04246v2#bib.bib12)), uses private information to select among equilibria. The dynamic approach, developed by Frankel and Pauzner ([2000](https://arxiv.org/html/2601.04246v2#bib.bib11)) and Burdzy et al. ([2001](https://arxiv.org/html/2601.04246v2#bib.bib6)), introduces aggregate shocks that move the game through dominance regions. Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)) develop a general framework for dynamic coordination with timing frictions: agents receive Poisson opportunities to revise their actions, with the revision rate determining how quickly the economy adjusts to changing fundamentals. This paper shows that the timing friction in Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)) corresponds precisely to the decay parameter κ\kappa in the master equation, with the discrete Feynman-Kac formula providing the explicit mathematical bridge.

The application to financial technology connects to a growing literature on fintech adoption and banking networks. Buchak et al. ([2018](https://arxiv.org/html/2601.04246v2#bib.bib5)) document the growth of fintech lending, while Fuster et al. ([2019](https://arxiv.org/html/2601.04246v2#bib.bib14)) study technology’s effect on mortgage lending. The network dimension links to the financial contagion literature: Allen and Gale ([2000](https://arxiv.org/html/2601.04246v2#bib.bib3)) and Freixas et al. ([2000](https://arxiv.org/html/2601.04246v2#bib.bib13)) develop foundational contagion models, while Acemoglu et al. ([2015](https://arxiv.org/html/2601.04246v2#bib.bib1)) characterize how network structure determines whether connections facilitate risk sharing or amplify shocks. The framework developed here shares the Feynman-Kac foundation and Lévy extension structure with recent work on financial contagion (Kikuchi , [2025](https://arxiv.org/html/2601.04246v2#bib.bib21)), but analyzes positive externalities—technology adoption that benefits counterparties—rather than negative externalities arising from stress transmission. This parallel structure suggests that the same network positions that make institutions systemically important for crisis propagation also make them technology leaders whose adoption decisions cascade broadly through the financial system.

## 2 Theoretical Framework

This section develops the theoretical framework in five stages. I first present the coordinate system and adoption representation. I then derive the master equation from three independent economic foundations—heterogeneous agent aggregation, market equilibrium, and cost minimization—establishing that the framework rests on fundamental principles rather than ad hoc specifications. Third, I present the Feynman-Kac representation and its discrete analog. Fourth, I develop the Adoption Amplification Factor. Finally, I demonstrate through explicit mathematical identification how canonical models emerge as special cases.

### 2.1 Coordinate System and Adoption Representation

We represent financial institutions by coordinates (𝐱,α)(\mathbf{x},\alpha) where 𝐱∈Ω⊆ℝd\mathbf{x}\in\Omega\subseteq\mathbb{R}^{d} denotes spatial location and α∈𝒩⊆ℝ\alpha\in\mathcal{N}\subseteq\mathbb{R} denotes position in the network of business relationships. The adoption functional τ​(𝐱,α,t):Ω×𝒩×[0,T]→ℝ\tau(\mathbf{x},\alpha,t):\Omega\times\mathcal{N}\times[0,T]\to\mathbb{R} represents adoption intensity at each point in this coordinate space.

###### Definition 2.1 (Spatial and Network Coordinates).

The spatial coordinate 𝐱\mathbf{x} represents geographic location—latitude, longitude, and potentially economic distance metrics reflecting transportation costs or communication frictions.

The network position coordinate α\alpha represents position in economic networks—centrality in correspondent banking relationships, position in payment flows, or role in interbank lending markets.

The continuous representation avoids three limitations of discrete methods. First, it avoids arbitrary discretization of adoption intensity into binary indicators, preserving the dose-response relationship central to technology diffusion. Second, it avoids arbitrary spatial boundaries between regions, allowing smooth geographic variation in adoption patterns. Third, it avoids discrete network categories, enabling continuous market position that captures fine gradations in institutional relationships.

###### Definition 2.2 (Source Term).

The source term S​(𝐱,α,t)S(\mathbf{x},\alpha,t) represents exogenous adoption shocks entering the system. In technology adoption contexts, SS measures the intensity of direct adoption incentives at each location-network-time cell, arising from regulatory mandates, technological breakthroughs, or coordinated industry initiatives.

The distinction between source SS and adoption functional τ\tau is fundamental. The source represents direct, exogenous adoption pressure; the adoption functional represents the equilibrium response incorporating both direct effects and all spillovers through spatial and network channels.

### 2.2 Derivation from Heterogeneous Agent Aggregation

The first derivation proceeds from aggregating heterogeneous agent behavior, following the tradition of Aiyagari ([1994](https://arxiv.org/html/2601.04246v2#bib.bib2)) and Huggett ([1993](https://arxiv.org/html/2601.04246v2#bib.bib18)) in macroeconomics.

Consider a continuum of heterogeneous institutions indexed by type θ∈Θ\theta\in\Theta distributed over space and network positions. Each institution has idiosyncratic characteristics—size, risk appetite, technological capacity—captured by θ\theta. Institution ii of type θ\theta at location 𝐱\mathbf{x} with network position α\alpha experiences adoption intensity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τi​(𝐱,α,t,θ)=τ0​(𝐱,α)+τ​(𝐱,α,t)+εi​(θ)\tau\_{i}(\mathbf{x},\alpha,t,\theta)=\tau\_{0}(\mathbf{x},\alpha)+\tau(\mathbf{x},\alpha,t)+\varepsilon\_{i}(\theta) |  | (1) |

where τ0\tau\_{0} is baseline adoption, τ\tau is the aggregate adoption effect to be determined, and εi​(θ)\varepsilon\_{i}(\theta) captures idiosyncratic variation.

Institutions optimize location and network position subject to adjustment costs. The state of institution ii evolves according to the stochastic differential equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xti\displaystyle dX\_{t}^{i} | =μs​(Xti,Ati,θi)​d​t+σs​(Xti,Ati,θi)​d​Bts\displaystyle=\mu\_{s}(X\_{t}^{i},A\_{t}^{i},\theta\_{i})\,dt+\sigma\_{s}(X\_{t}^{i},A\_{t}^{i},\theta\_{i})\,dB\_{t}^{s} |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ati\displaystyle dA\_{t}^{i} | =μn​(Xti,Ati,θi)​d​t+σn​(Xti,Ati,θi)​d​Btn\displaystyle=\mu\_{n}(X\_{t}^{i},A\_{t}^{i},\theta\_{i})\,dt+\sigma\_{n}(X\_{t}^{i},A\_{t}^{i},\theta\_{i})\,dB\_{t}^{n} |  | (3) |

where (Bts,Btn)(B\_{t}^{s},B\_{t}^{n}) are independent Brownian motions representing location and network uncertainty. The drift terms μs,μn\mu\_{s},\mu\_{n} capture directed adjustments—institutions moving toward more favorable positions. The diffusion terms σs,σn\sigma\_{s},\sigma\_{n} capture randomness in adjustment outcomes—search frictions, information imperfections, and relationship formation uncertainty.

The joint density f​(𝐱,α,t)f(\mathbf{x},\alpha,t) of institutions over spatial and network coordinates evolves according to the Kolmogorov forward equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂f∂t=−∇⋅(𝝁s​f)−∂∂α​(μn​f)+12​∇⋅(𝚺s​∇f)+12​∂2∂α2​(σn2​f)\frac{\partial f}{\partial t}=-\nabla\cdot(\boldsymbol{\mu}\_{s}f)-\frac{\partial}{\partial\alpha}(\mu\_{n}f)+\frac{1}{2}\nabla\cdot(\boldsymbol{\Sigma}\_{s}\nabla f)+\frac{1}{2}\frac{\partial^{2}}{\partial\alpha^{2}}(\sigma\_{n}^{2}f) |  | (4) |

This equation describes how the population distribution shifts as institutions relocate and adjust network positions.

###### Proposition 2.1 (Aggregation Result).

Under the following regularity conditions: (i) bounded heterogeneity: supθ‖σ​(⋅,θ)‖<∞\sup\_{\theta}\|\sigma(\cdot,\theta)\|<\infty; (ii) ergodic dynamics: the process (Xt,At)(X\_{t},A\_{t}) has a unique stationary distribution for each θ\theta; (iii) smooth aggregation: the mapping θ↦τ​(⋅,θ)\theta\mapsto\tau(\cdot,\theta) is measurable; the aggregate adoption functional satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂τ∂t=νs​∇2τ+νn​∂2τ∂α2−κ​τ+S​(𝐱,α,t)\frac{\partial\tau}{\partial t}=\nu\_{s}\nabla^{2}\tau+\nu\_{n}\frac{\partial^{2}\tau}{\partial\alpha^{2}}-\kappa\tau+S(\mathbf{x},\alpha,t) |  | (5) |

where νs=12​𝔼θ​[σs2​(θ)]\nu\_{s}=\frac{1}{2}\mathbb{E}\_{\theta}[\sigma\_{s}^{2}(\theta)] is mean spatial diffusivity, νn=12​𝔼θ​[σn2​(θ)]\nu\_{n}=\frac{1}{2}\mathbb{E}\_{\theta}[\sigma\_{n}^{2}(\theta)] is mean network diffusivity, and κ\kappa reflects mean reversion from competitive pressure.

The aggregation result shows that heterogeneous institution behavior generates aggregate dynamics governed by a partial differential equation. The diffusion coefficients (νs,νn)(\nu\_{s},\nu\_{n}) emerge from averaging individual mobility variances across types; they measure how quickly adoption spreads through the population as institutions adjust positions and form new relationships.

### 2.3 Derivation from Market Equilibrium

An independent derivation proceeds from market equilibrium conditions, connecting observed adoption volatility to underlying market structure.

In markets with search frictions, matching delays, or information asymmetries, adoption rates fluctuate around equilibrium values. The observed volatility σ2\sigma^{2} of adoption processes relates to underlying market adjustment through the equilibrium volatility relation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2=2​D​κ\sigma^{2}=2D\kappa |  | (6) |

where DD is a diffusion coefficient measuring the amplitude of fluctuations and κ\kappa is the adjustment rate toward equilibrium.

This relation emerges from the stochastic process governing adoption dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​τ=−κ​(τ−τ∗)​d​t+σ​d​Bd\tau=-\kappa(\tau-\tau^{\*})\,dt+\sigma\,dB |  | (7) |

where τ∗\tau^{\*} is equilibrium adoption and κ\kappa governs mean reversion speed. At stationarity, variance satisfies Var​(τ)=σ2/(2​κ)\text{Var}(\tau)=\sigma^{2}/(2\kappa), which rearranges to ([6](https://arxiv.org/html/2601.04246v2#S2.E6 "In 2.3 Derivation from Market Equilibrium ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")).

Connecting observed dynamics to adoption propagation: spatial adoption volatility σs2\sigma\_{s}^{2} implies spatial diffusion νs=σs2/(2​κ)\nu\_{s}=\sigma\_{s}^{2}/(2\kappa); network adoption volatility σn2\sigma\_{n}^{2} implies network diffusion νn=σn2/(2​κ)\nu\_{n}=\sigma\_{n}^{2}/(2\kappa). Markets with high adoption volatility—active experimentation, frequent technology updates—exhibit rapid spatial diffusion; markets with stable adoption patterns exhibit slow diffusion.

### 2.4 Derivation from Cost Minimization

A third derivation proceeds from cost minimization, following variational principles underlying market equilibrium.

###### Definition 2.3 (Adjustment Cost Functional).

The total adjustment cost functional is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​[τ]=∫0T∫Ω∫𝒩[12​(∂τ∂t)2+νs2​|∇τ|2+νn2​(∂τ∂α)2+κ2​τ2−S​τ]​𝑑α​𝑑𝐱​𝑑t\mathcal{C}[\tau]=\int\_{0}^{T}\int\_{\Omega}\int\_{\mathcal{N}}\left[\frac{1}{2}\left(\frac{\partial\tau}{\partial t}\right)^{2}+\frac{\nu\_{s}}{2}|\nabla\tau|^{2}+\frac{\nu\_{n}}{2}\left(\frac{\partial\tau}{\partial\alpha}\right)^{2}+\frac{\kappa}{2}\tau^{2}-S\tau\right]d\alpha\,d\mathbf{x}\,dt |  | (8) |

The terms have economic interpretations in the technology adoption context. The term 12​(∂τ/∂t)2\frac{1}{2}(\partial\tau/\partial t)^{2} captures temporal adjustment costs: rapidly changing adoption is costly due to integration frictions, training requirements, and coordination failures. The term νs2​|∇τ|2\frac{\nu\_{s}}{2}|\nabla\tau|^{2} captures spatial gradient costs: maintaining adoption differentials across space is costly due to competitive pressure from neighboring institutions. The term νn2​(∂τ/∂α)2\frac{\nu\_{n}}{2}(\partial\tau/\partial\alpha)^{2} captures network gradient costs: maintaining adoption differentials across network positions is costly due to interoperability pressure from counterparties. The term κ2​τ2\frac{\kappa}{2}\tau^{2} captures level costs: deviating from baseline technology is costly due to switching costs and legacy system maintenance. The term −S​τ-S\tau captures policy benefits: the intervention SS shifts optimal adoption.

###### Proposition 2.2 (Euler-Lagrange Equation).

The adoption functional τ∗\tau^{\*} minimizing 𝒞​[τ]\mathcal{C}[\tau] satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂τ∂t=νs​∇2τ+νn​∂2τ∂α2−κ​τ+S\frac{\partial\tau}{\partial t}=\nu\_{s}\nabla^{2}\tau+\nu\_{n}\frac{\partial^{2}\tau}{\partial\alpha^{2}}-\kappa\tau+S |  | (9) |

###### Proof.

The first variation of 𝒞\mathcal{C} with respect to τ\tau must vanish for all admissible variations η\eta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​𝒞=∫0T∫Ω∫𝒩[∂τ∂t​∂η∂t+νs​∇τ⋅∇η+νn​∂τ∂α​∂η∂α+κ​τ​η−S​η]​𝑑α​𝑑𝐱​𝑑t=0\delta\mathcal{C}=\int\_{0}^{T}\int\_{\Omega}\int\_{\mathcal{N}}\left[\frac{\partial\tau}{\partial t}\frac{\partial\eta}{\partial t}+\nu\_{s}\nabla\tau\cdot\nabla\eta+\nu\_{n}\frac{\partial\tau}{\partial\alpha}\frac{\partial\eta}{\partial\alpha}+\kappa\tau\eta-S\eta\right]d\alpha\,d\mathbf{x}\,dt=0 |  | (10) |

Integrating by parts and assuming boundary terms vanish yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T∫Ω∫𝒩[−∂2τ∂t2−νs​∇2τ−νn​∂2τ∂α2+κ​τ−S]​η​𝑑α​𝑑𝐱​𝑑t=0\int\_{0}^{T}\int\_{\Omega}\int\_{\mathcal{N}}\left[-\frac{\partial^{2}\tau}{\partial t^{2}}-\nu\_{s}\nabla^{2}\tau-\nu\_{n}\frac{\partial^{2}\tau}{\partial\alpha^{2}}+\kappa\tau-S\right]\eta\,d\alpha\,d\mathbf{x}\,dt=0 |  | (11) |

For quasi-static evolution where ∂2τ/∂t2≈0\partial^{2}\tau/\partial t^{2}\approx 0, this yields the master equation.
∎

The cost minimization derivation connects the master equation to optimization principles. The parameters (νs,νn,κ)(\nu\_{s},\nu\_{n},\kappa) have natural interpretations as relative costs: high νs\nu\_{s} means spatial arbitrage is rapid (low cost of spatial gradients); high κ\kappa means competitive pressure is strong (high cost of deviating from baseline technology).

### 2.5 The Complete Master Equation with Interaction

The three derivations above establish the basic master equation without spatial-network interaction. The complete specification adds the interaction term capturing amplification when geographic and network proximity coincide.

###### Definition 2.4 (Master Equation).

The adoption field τ​(𝐱,α,t)\tau(\mathbf{x},\alpha,t) evolves according to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂τ∂t=νs​∇2τ+νn​∂2τ∂α2+λ​∂2τ∂𝐱​∂α−κ​τ+S​(𝐱,α,t)\frac{\partial\tau}{\partial t}=\nu\_{s}\nabla^{2}\tau+\nu\_{n}\frac{\partial^{2}\tau}{\partial\alpha^{2}}+\lambda\frac{\partial^{2}\tau}{\partial\mathbf{x}\partial\alpha}-\kappa\tau+S(\mathbf{x},\alpha,t) |  | (12) |

where νs≥0\nu\_{s}\geq 0 is spatial diffusion, νn≥0\nu\_{n}\geq 0 is network diffusion, λ\lambda is spatial-network interaction, κ>0\kappa>0 is adjustment speed, and SS is the exogenous adoption shock.

The interaction term λ​∂2τ/∂𝐱​∂α\lambda\partial^{2}\tau/\partial\mathbf{x}\partial\alpha captures amplification when institutions are proximate on both dimensions. In financial networks, institutions form business relationships disproportionately with geographic neighbors due to information advantages, regulatory similarities, and historical ties. When a geographic neighbor is also a network partner, adoption influence compounds: the neighbor’s adoption affects the focal institution through both demonstration effects (spatial channel) and interoperability benefits (network channel), with the interaction term capturing reinforcement beyond the sum of separate effects.

###### Remark 2.1 (Parameter Interpretation for Technology Adoption).

The parameters have structural interpretations in the adoption context:

The spatial diffusion coefficient νs\nu\_{s} measures geographic adoption spillovers reflecting local demonstration effects, labor mobility spreading technological knowledge, and regional market integration creating competitive pressure to adopt.

The network diffusion coefficient νn\nu\_{n} measures adoption spillovers through business relationships reflecting interoperability benefits when counterparties adopt, learning from network partners’ experiences, and coordination incentives in bilateral transactions.

The interaction coefficient λ\lambda captures amplification when both channels coincide, common in financial markets where correspondent banks, payment network partners, and syndicate members are often geographic neighbors.

The adjustment parameter κ\kappa measures how rapidly institutions respond to adoption incentives, corresponding to the timing friction in Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)): higher κ\kappa implies faster adjustment and shorter waiting times until adoption decisions are revised.

### 2.6 Feynman-Kac Representation and Discrete Analog

The master equation admits a probabilistic solution that provides both computational methods and economic intuition.

###### Theorem 2.1 (Feynman-Kac Representation).

The solution to the master equation ([12](https://arxiv.org/html/2601.04246v2#S2.E12 "In Definition 2.4 (Master Equation). ‣ 2.5 The Complete Master Equation with Interaction ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")) admits the representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ​(𝐱,α,t)=𝔼(𝐱,α)​[e−κ​t​τ0​(Xt,At)+∫0te−κ​(t−s)​S​(Xs,As,s)​𝑑s]\tau(\mathbf{x},\alpha,t)=\mathbb{E}\_{(\mathbf{x},\alpha)}\left[e^{-\kappa t}\tau\_{0}(X\_{t},A\_{t})+\int\_{0}^{t}e^{-\kappa(t-s)}S(X\_{s},A\_{s},s)\,ds\right] |  | (13) |

where (Xs,As)s≥0(X\_{s},A\_{s})\_{s\geq 0} is the diffusion process with generator ℒ=νs​∇2+νn​∂2/∂α2+λ​∂2/∂𝐱​∂α\mathcal{L}=\nu\_{s}\nabla^{2}+\nu\_{n}\partial^{2}/\partial\alpha^{2}+\lambda\partial^{2}/\partial\mathbf{x}\partial\alpha started at (X0,A0)=(𝐱,α)(X\_{0},A\_{0})=(\mathbf{x},\alpha).

###### Proof.

Define the transformed function u​(𝐱,α,t)=eκ​t​τ​(𝐱,α,t)u(\mathbf{x},\alpha,t)=e^{\kappa t}\tau(\mathbf{x},\alpha,t). Substituting into the master equation yields ∂u/∂t=ℒ​u+eκ​t​S\partial u/\partial t=\mathcal{L}u+e^{\kappa t}S. By the standard Feynman-Kac formula for parabolic PDEs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(𝐱,α,t)=𝔼(𝐱,α)​[u0​(Xt,At)+∫0teκ​s​S​(Xs,As,s)​𝑑s]u(\mathbf{x},\alpha,t)=\mathbb{E}\_{(\mathbf{x},\alpha)}\left[u\_{0}(X\_{t},A\_{t})+\int\_{0}^{t}e^{\kappa s}S(X\_{s},A\_{s},s)\,ds\right] |  | (14) |

Substituting u=eκ​t​τu=e^{\kappa t}\tau and rearranging yields ([13](https://arxiv.org/html/2601.04246v2#S2.E13 "In Theorem 2.1 (Feynman-Kac Representation). ‣ 2.6 Feynman-Kac Representation and Discrete Analog ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")).
∎

The representation has direct economic content: adoption intensity equals the expected cumulative exposure to adoption shocks along all paths of economic linkage, discounted at rate κ\kappa. Institutions in densely connected network regions or geographically central locations receive contributions from more paths, elevating their adoption intensity even without direct shocks.

###### Proposition 2.3 (Discrete Feynman-Kac Formula).

For discrete time periods t=0,1,…,Tt=0,1,\ldots,T and discrete units i=1,…,Ni=1,\ldots,N, the Feynman-Kac representation admits the discrete analog:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τi,t=∑s=0t−1(1−κ​Δ​t)t−s⋅𝔼​[Si​(s),s|i​(t)=i]⋅Δ​t\tau\_{i,t}=\sum\_{s=0}^{t-1}(1-\kappa\Delta t)^{t-s}\cdot\mathbb{E}[S\_{i(s),s}|i(t)=i]\cdot\Delta t |  | (15) |

where i​(s)i(s) traces a stochastic path backward through the network from unit ii at time tt to earlier times, and (1−κ​Δ​t)t−s(1-\kappa\Delta t)^{t-s} are exponentially decaying weights.

This discrete formula provides the bridge to conventional econometric methods and enables the nesting relationships developed below.

### 2.7 Adoption Amplification Factor

The Feynman-Kac representation motivates a natural measure of technology leadership.

###### Definition 2.5 (Adoption Amplification Factor).

For an institution at location (𝐱i,αi)(\mathbf{x}\_{i},\alpha\_{i}), the Adoption Amplification Factor is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜i=∫0∞∫𝒳∫𝒩τ​(𝐱,α,t)​𝑑α​𝑑𝐱​𝑑t∫0∞τ​(𝐱i,αi,t)​𝑑t\mathcal{A}\_{i}=\frac{\int\_{0}^{\infty}\int\_{\mathcal{X}}\int\_{\mathcal{N}}\tau(\mathbf{x},\alpha,t)\,d\alpha\,d\mathbf{x}\,dt}{\int\_{0}^{\infty}\tau(\mathbf{x}\_{i},\alpha\_{i},t)\,dt} |  | (16) |

measuring the ratio of total system-wide adoption to direct adoption at institution ii following a localized shock at ii.

An amplification factor of 𝒜i=10\mathcal{A}\_{i}=10 means that total system-wide adoption following a shock at institution ii is ten times larger than direct adoption at ii alone—the remaining nine-tenths represent spillovers along paths of economic linkage through space and network.

###### Proposition 2.4 (Channel Decomposition).

The Adoption Amplification Factor decomposes as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜i=1+𝒜ispatial+𝒜inetwork+𝒜iinteraction\mathcal{A}\_{i}=1+\mathcal{A}\_{i}^{\text{spatial}}+\mathcal{A}\_{i}^{\text{network}}+\mathcal{A}\_{i}^{\text{interaction}} |  | (17) |

where 𝒜ispatial\mathcal{A}\_{i}^{\text{spatial}} captures spillovers through geographic proximity, 𝒜inetwork\mathcal{A}\_{i}^{\text{network}} captures spillovers through business relationships, and 𝒜iinteraction\mathcal{A}\_{i}^{\text{interaction}} captures amplification from coincident proximity.

This decomposition reveals which transmission channel contributes most to each institution’s role as a technology leader, informing targeted policy interventions.

### 2.8 Connection to Conventional Models

The master equation framework nests several canonical models as special cases. This section establishes these connections through explicit mathematical identification.

#### Katz-Shapiro Network Externalities.

Katz and Shapiro ([1985](https://arxiv.org/html/2601.04246v2#bib.bib19)) model network externalities through the utility function ui=v​(n)−pu\_{i}=v(n)-p where v​(n)v(n) is the value of adoption when nn others have adopted, with v′​(n)>0v^{\prime}(n)>0 capturing the positive externality.

###### Proposition 2.5 (Katz-Shapiro as Discrete Network Steady State).

At steady state (∂τ/∂t=0\partial\tau/\partial t=0) with discrete network structure and no spatial diffusion (νs=0\nu\_{s}=0), the master equation yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ​τi=νn​∑jGi​j​(τj−τi)+Si\kappa\tau\_{i}=\nu\_{n}\sum\_{j}G\_{ij}(\tau\_{j}-\tau\_{i})+S\_{i} |  | (18) |

Rearranging gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τi=1κ+νn​di​(Si+νn​∑jGi​j​τj)\tau\_{i}=\frac{1}{\kappa+\nu\_{n}d\_{i}}\left(S\_{i}+\nu\_{n}\sum\_{j}G\_{ij}\tau\_{j}\right) |  | (19) |

where di=∑jGi​jd\_{i}=\sum\_{j}G\_{ij} is node degree. This corresponds to the Katz-Shapiro equilibrium with network externality v​(ni)=νn​∑jGi​j​τj/κv(n\_{i})=\nu\_{n}\sum\_{j}G\_{ij}\tau\_{j}/\kappa.

#### Frankel-Pauzner Dynamic Coordination.

Frankel and Pauzner ([2000](https://arxiv.org/html/2601.04246v2#bib.bib11)) show that when agents choose between two actions with payoffs depending on the fraction choosing each action, and the payoff-relevant parameter follows Brownian motion, a unique equilibrium emerges.

###### Proposition 2.6 (Frankel-Pauzner as Aggregate Limit).

When spatial and network coordinates collapse to a single dimension, the master equation reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​τ¯d​t=−κ​τ¯+S¯​(t)+ν⋅τ¯\frac{d\bar{\tau}}{dt}=-\kappa\bar{\tau}+\bar{S}(t)+\nu\cdot\bar{\tau} |  | (20) |

where τ¯\bar{\tau} is aggregate adoption, S¯\bar{S} is aggregate shock, and ν=νs+νn\nu=\nu\_{s}+\nu\_{n}. This corresponds to the Frankel-Pauzner dynamics with strategic complementarity parameter ν/κ\nu/\kappa.

#### Guimaraes-Machado-Pereira Timing Frictions.

Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)) develop a framework where agents receive Poisson opportunities to revise actions at rate λ\lambda. The state evolution satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​nd​t=λ⋅[F​(θ,n)−n]\frac{dn}{dt}=\lambda\cdot[F(\theta,n)-n] |  | (21) |

###### Proposition 2.7 (Timing Friction Correspondence).

The decay parameter κ\kappa in the master equation corresponds exactly to the Poisson revision rate λ\lambda in Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ=λ\kappa=\lambda |  | (22) |

The discrete Feynman-Kac formula ([15](https://arxiv.org/html/2601.04246v2#S2.E15 "In Proposition 2.3 (Discrete Feynman-Kac Formula). ‣ 2.6 Feynman-Kac Representation and Discrete Analog ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")) with time step Δ​t\Delta t yields dynamics matching Guimaraes-Machado-Pereira with λ=κ\lambda=\kappa.

This identification has important implications. The timing friction λ−1\lambda^{-1}—the expected waiting time until revision—equals κ−1\kappa^{-1} in the master equation. The half-life of adoption effects is t1/2=ln⁡(2)/κt\_{1/2}=\ln(2)/\kappa, independent of observation frequency.

#### Adoption Hazard Models.

Standard duration models specify hazard rate h​(t|Xi)=h0​(t)​exp⁡(Xi′​β)h(t|X\_{i})=h\_{0}(t)\exp(X\_{i}^{\prime}\beta).

###### Proposition 2.8 (Hazard Models as No-Spillover Limit).

When νs=νn=0\nu\_{s}=\nu\_{n}=0, the master equation implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​τid​t=−κ​τi+Si​(t)\frac{d\tau\_{i}}{dt}=-\kappa\tau\_{i}+S\_{i}(t) |  | (23) |

corresponding to independent adoption with hazard hi=κ+Sih\_{i}=\kappa+S\_{i}. The no-spillover case is a testable restriction.

Table [1](https://arxiv.org/html/2601.04246v2#S2.T1 "Table 1 ‣ Adoption Hazard Models. ‣ 2.8 Connection to Conventional Models ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") summarizes these relationships.

Table 1: Conventional Models as Special Cases of the Master Equation

| Model | νs\nu\_{s} | νn\nu\_{n} | Mathematical Identification |
| --- | --- | --- | --- |
| Adoption hazard models | 0 | 0 | hi=κ+Sih\_{i}=\kappa+S\_{i} |
| Katz-Shapiro (1985) | 0 | >0>0 | v​(ni)=νn​∑jGi​j​τj/κv(n\_{i})=\nu\_{n}\sum\_{j}G\_{ij}\tau\_{j}/\kappa |
| Frankel-Pauzner (2000) | νs+νn>0\nu\_{s}+\nu\_{n}>0 | | Complementarity =(νs+νn)/κ=(\nu\_{s}+\nu\_{n})/\kappa |
| Guimaraes et al. (2020) | ≥0\geq 0 | ≥0\geq 0 | Timing friction λ=κ\lambda=\kappa |
| Spatial-network (full) | >0>0 | >0>0 | All parameters free |

* •

  Notes: Each conventional model emerges through parameter restrictions and discretization. The full model generalizes all approaches.

### 2.9 Lévy Extension: Critical Mass and Cascade Dynamics

The baseline framework describes continuous adoption transmission appropriate for gradual diffusion regimes. To capture the sudden adoption cascades that occur when critical mass is reached—where adoption spreads rapidly through positive feedback rather than gradual diffusion—I extend the framework to incorporate jumps through Lévy processes.

#### Jump-Diffusion Dynamics.

The extended dynamics replace pure diffusion with a jump-diffusion process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂τ∂t=νs​∇2τ+νn​∂2τ∂α2+λ​∂2τ∂𝐱​∂α−κ​τ+S+𝒥​[τ]\frac{\partial\tau}{\partial t}=\nu\_{s}\nabla^{2}\tau+\nu\_{n}\frac{\partial^{2}\tau}{\partial\alpha^{2}}+\lambda\frac{\partial^{2}\tau}{\partial\mathbf{x}\partial\alpha}-\kappa\tau+S+\mathcal{J}[\tau] |  | (24) |

where the jump operator 𝒥​[τ]\mathcal{J}[\tau] captures sudden adoption events distinct from gradual diffusion, defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​[τ]=∫ℝ[τ​(𝐱,α+z,t)−τ​(𝐱,α,t)−z​∂τ∂α​𝟏|z|<1]​ν​(d​z)\mathcal{J}[\tau]=\int\_{\mathbb{R}}\left[\tau(\mathbf{x},\alpha+z,t)-\tau(\mathbf{x},\alpha,t)-z\frac{\partial\tau}{\partial\alpha}\mathbf{1}\_{|z|<1}\right]\nu(dz) |  | (25) |

Here ν​(d​z)\nu(dz) is the Lévy measure characterizing jump intensity and size distribution. The compensator term z​∂τ/∂α⋅𝟏|z|<1z\partial\tau/\partial\alpha\cdot\mathbf{1}\_{|z|<1} ensures the integral is well-defined for Lévy measures with infinite activity near zero.

In the technology adoption context, jumps represent sudden adoption events distinct from gradual diffusion. When adoption reaches critical mass, network effects trigger rapid cascades—institutions observe successful adoption by counterparties and revise their own adoption decisions discretely rather than incrementally. The Lévy measure ν​(d​z)\nu(dz) captures both how frequently such cascade events occur (total mass of ν\nu) and the distribution of adoption spillover magnitudes when they occur (shape of ν\nu).

For a compound Poisson process with intensity λJ\lambda\_{J} and jump size distribution FF, the Lévy measure is ν​(d​z)=λJ​d​F​(z)\nu(dz)=\lambda\_{J}dF(z), and the jump operator simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​[τ]=λJ​∫ℝ[τ​(𝐱,α+z,t)−τ​(𝐱,α,t)]​𝑑F​(z)=λJ​(𝔼​[τ​(𝐱,α+Z,t)]−τ​(𝐱,α,t))\mathcal{J}[\tau]=\lambda\_{J}\int\_{\mathbb{R}}\left[\tau(\mathbf{x},\alpha+z,t)-\tau(\mathbf{x},\alpha,t)\right]dF(z)=\lambda\_{J}\left(\mathbb{E}[\tau(\mathbf{x},\alpha+Z,t)]-\tau(\mathbf{x},\alpha,t)\right) |  | (26) |

where Z∼FZ\sim F represents the random jump size. This has intuitive interpretation: at rate λJ\lambda\_{J}, an institution’s adoption intensity jumps by an amount determined by the cascade spillover from adopting counterparties at network distance ZZ.

#### State-Dependent Jump Intensity.

The key innovation capturing critical mass dynamics makes jump intensity depend on the current adoption level:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λJ​(τ)=λ0+(λ1−λ0)⋅H​(τ−τ¯∗)\lambda\_{J}(\tau)=\lambda\_{0}+(\lambda\_{1}-\lambda\_{0})\cdot H(\tau-\bar{\tau}^{\*}) |  | (27) |

where H​(⋅)H(\cdot) is the Heaviside function, τ¯∗\bar{\tau}^{\*} is the critical mass threshold, λ0\lambda\_{0} is baseline jump intensity (gradual adoption regime), and λ1≫λ0\lambda\_{1}\gg\lambda\_{0} is elevated intensity above threshold (cascade regime).

The state-dependent specification captures the central insight of the coordination literature: below critical mass, adoption proceeds gradually as institutions weigh costs and benefits individually; above critical mass, positive feedback accelerates adoption as network effects dominate. The threshold τ¯∗\bar{\tau}^{\*} corresponds to the tipping point in Arthur ([1989](https://arxiv.org/html/2601.04246v2#bib.bib4)) and the critical mass in Katz and Shapiro ([1985](https://arxiv.org/html/2601.04246v2#bib.bib19)).

###### Proposition 2.9 (Cascade Limit).

In the limit λ0→0\lambda\_{0}\to 0 and λ1→∞\lambda\_{1}\to\infty, the dynamics converge to deterministic cascade dynamics: below threshold, only diffusive transmission occurs; above threshold, immediate cascade with adoption spreading instantaneously to all connected institutions.

###### Proof.

Consider the jump-diffusion dynamics with state-dependent intensity. For τ¯<τ¯∗\bar{\tau}<\bar{\tau}^{\*}, λJ​(τ)=λ0→0\lambda\_{J}(\tau)=\lambda\_{0}\to 0, so the jump term vanishes and dynamics reduce to pure diffusion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂τ∂t=νs​∇2τ+νn​∂2τ∂α2+λ​∂2τ∂𝐱​∂α−κ​τ+S\frac{\partial\tau}{\partial t}=\nu\_{s}\nabla^{2}\tau+\nu\_{n}\frac{\partial^{2}\tau}{\partial\alpha^{2}}+\lambda\frac{\partial^{2}\tau}{\partial\mathbf{x}\partial\alpha}-\kappa\tau+S |  | (28) |

For τ¯≥τ¯∗\bar{\tau}\geq\bar{\tau}^{\*}, λJ​(τ)=λ1→∞\lambda\_{J}(\tau)=\lambda\_{1}\to\infty. In this limit, the jump term dominates and forces instantaneous equilibration: τ​(𝐱,α+z,t)=τ​(𝐱,α,t)\tau(\mathbf{x},\alpha+z,t)=\tau(\mathbf{x},\alpha,t) for all zz in the support of FF, implying uniform adoption across network-connected institutions. This is precisely the cascade outcome where adoption spreads immediately upon crossing threshold.
∎

This nesting relationship clarifies that continuous diffusion and discrete cascades describe different regimes of the same phenomenon. Diffusion captures pre-critical-mass dynamics (gradual demonstration effects, incremental learning), while jumps capture discrete adoption cascades when critical mass materializes. The framework thus unifies the gradual diffusion models of Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)) with the tipping point dynamics emphasized in Katz and Shapiro ([1985](https://arxiv.org/html/2601.04246v2#bib.bib19)) and Arthur ([1989](https://arxiv.org/html/2601.04246v2#bib.bib4)).

#### Feynman-Kac Representation with Jumps.

The Feynman-Kac representation extends to the Lévy case by replacing the diffusion process with a jump-diffusion:

###### Theorem 2.2 (Lévy-Feynman-Kac Representation).

The solution to the Lévy-extended master equation ([24](https://arxiv.org/html/2601.04246v2#S2.E24 "In Jump-Diffusion Dynamics. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")) admits the representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ​(𝐱,α,t)=𝔼(𝐱,α)​[e−κ​t​τ0​(Xt,At)+∫0te−κ​(t−s)​S​(Xs,As,s)​𝑑s]\tau(\mathbf{x},\alpha,t)=\mathbb{E}\_{(\mathbf{x},\alpha)}\left[e^{-\kappa t}\tau\_{0}(X\_{t},A\_{t})+\int\_{0}^{t}e^{-\kappa(t-s)}S(X\_{s},A\_{s},s)\,ds\right] |  | (29) |

where (Xs,As)s≥0(X\_{s},A\_{s})\_{s\geq 0} is now a Lévy process combining diffusion with jumps governed by measure ν​(d​z)\nu(dz).

The economic interpretation remains: adoption intensity equals expected cumulative exposure to adoption shocks along all paths through spatial-network space, but paths now include both continuous diffusion and discrete jumps. The jump component captures cascade pathways where adoption spreads instantaneously through network links when critical mass is reached.

#### Temporary Interventions and Critical Mass.

The Lévy extension provides rigorous foundations for analyzing when temporary interventions produce permanent adoption shifts.

###### Definition 2.6 (Intervention Intensity).

The intervention intensity function I:[0,T]→ℝ+I:[0,T]\to\mathbb{R}\_{+} measures the rate at which the policy shock affects adoption at each instant s∈[0,T]s\in[0,T]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(s)=∫𝒳∫𝒩S​(𝐱,α,s)​𝑑α​𝑑𝐱I(s)=\int\_{\mathcal{X}}\int\_{\mathcal{N}}S(\mathbf{x},\alpha,s)\,d\alpha\,d\mathbf{x} |  | (30) |

representing spatially and network-integrated shock intensity at time ss.

###### Corollary 2.1 (Temporary Intervention Threshold).

Consider a temporary intervention of duration TT with time-varying intensity I​(s)I(s) as defined in Definition [2.6](https://arxiv.org/html/2601.04246v2#S2.Thmdefinition6 "Definition 2.6 (Intervention Intensity). ‣ Temporary Interventions and Critical Mass. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach"). Let 𝒜​(s)\mathcal{A}(s) denote the time-varying system-wide amplification factor at time ss. The intervention produces permanent adoption gains if and only if cumulative amplified effects exceed the critical mass gap:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0TI​(s)⋅𝒜​(s)​𝑑s>τ¯∗−τ¯0\int\_{0}^{T}I(s)\cdot\mathcal{A}(s)\,ds>\bar{\tau}^{\*}-\bar{\tau}\_{0} |  | (31) |

where τ¯0\bar{\tau}\_{0} is initial average adoption and the left-hand side represents cumulative amplified intervention effects.

###### Proof.

Under the Lévy dynamics with state-dependent jump intensity ([27](https://arxiv.org/html/2601.04246v2#S2.E27 "In State-Dependent Jump Intensity. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")), the system exhibits two stable regimes: a low-adoption equilibrium with τ¯<τ¯∗\bar{\tau}<\bar{\tau}^{\*} and a high-adoption equilibrium with τ¯>τ¯∗\bar{\tau}>\bar{\tau}^{\*}. The intervention shifts average adoption by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​τ¯​(T)=∫0Te−κ​(T−s)​I​(s)⋅𝒜​(s)​𝑑s\Delta\bar{\tau}(T)=\int\_{0}^{T}e^{-\kappa(T-s)}I(s)\cdot\mathcal{A}(s)\,ds |  | (32) |

following from the Feynman-Kac representation integrated over space and network. For permanent effects, the intervention must push adoption above threshold before time TT: τ¯0+Δ​τ¯​(T)>τ¯∗\bar{\tau}\_{0}+\Delta\bar{\tau}(T)>\bar{\tau}^{\*}. Rearranging and noting that e−κ​(T−s)≤1e^{-\kappa(T-s)}\leq 1 gives the sufficient condition ([31](https://arxiv.org/html/2601.04246v2#S2.E31 "In Corollary 2.1 (Temporary Intervention Threshold). ‣ Temporary Interventions and Critical Mass. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")).
∎

The condition has intuitive content: the cumulative intervention, weighted by the amplification factor at each instant, must exceed the gap between initial adoption and critical mass. Larger, more concentrated interventions are more likely to cross the threshold than equivalent total resources spread thinly over time. This rationalizes the findings in Crouzet et al. ([2023](https://arxiv.org/html/2601.04246v2#bib.bib8)) regarding India’s demonetization: the large but temporary shock pushed digital wallet adoption above critical mass in high-exposure regions, producing persistent increases even after cash availability normalized. In low-exposure regions, the shock fell short of the threshold, and adoption gains dissipated.

#### Two-Regime Dynamics.

The Lévy extension generates qualitatively different dynamics in the two regimes:

###### Proposition 2.10 (Two-Regime Characterization).

Under the state-dependent Lévy dynamics:

1. (i)

   Below threshold (τ¯<τ¯∗\bar{\tau}<\bar{\tau}^{\*}): Adoption evolves through gradual diffusion with characteristic time scale κ−1\kappa^{-1}. The half-life of adoption responses is t1/2=ln⁡(2)/κt\_{1/2}=\ln(2)/\kappa, and spatial-network spillovers spread at rates governed by νs\nu\_{s} and νn\nu\_{n}.
2. (ii)

   Above threshold (τ¯≥τ¯∗\bar{\tau}\geq\bar{\tau}^{\*}): Jump intensity increases to λ1\lambda\_{1}, generating rapid cascade dynamics. The characteristic time scale becomes λ1−1≪κ−1\lambda\_{1}^{-1}\ll\kappa^{-1}, and adoption spreads through discrete jumps rather than continuous diffusion.
3. (iii)

   Transition dynamics: Near threshold, the system exhibits critical slowing—small perturbations produce large, long-lasting responses as the system approaches the bifurcation point.

This two-regime structure explains why technology adoption often exhibits S-curve dynamics: slow initial growth (below-threshold diffusion), rapid acceleration (above-threshold cascade), and eventual saturation. The framework provides microfoundations for this pattern through the state-dependent jump intensity mechanism.

###### Remark 2.2 (Connection to Empirical Patterns).

The Lévy extension rationalizes several empirical patterns documented in the technology adoption literature. The sharp contrast between gradual pre-threshold dynamics and rapid post-threshold cascades matches the “hockey stick” adoption curves observed for successful technologies. The critical slowing near threshold explains why adoption often appears to stall before suddenly accelerating. The permanent effects of sufficiently large temporary interventions rationalize how coordinated industry initiatives or regulatory mandates can overcome coordination failures that market forces alone cannot resolve.

## 3 Monte Carlo Evidence

This section presents Monte Carlo simulations validating the theoretical predictions.

### 3.1 Simulation Design

The simulations implement the discrete network formulation for networks of N=30N=30 to 4040 agents. I consider three network structures: random networks, scale-free networks, and clustered networks where agents connect preferentially to geographic neighbors. The baseline parameters are νs=0.5\nu\_{s}=0.5, νn=0.8\nu\_{n}=0.8, λ=0.3\lambda=0.3, κ=0.15\kappa=0.15, and critical mass threshold τ¯∗=0.35\bar{\tau}^{\*}=0.35.

### 3.2 Results

Figure [1](https://arxiv.org/html/2601.04246v2#S3.F1 "Figure 1 ‣ 3.2 Results ‣ 3 Monte Carlo Evidence ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") illustrates the two-regime dynamics predicted by Proposition LABEL:prop:critical\_mass. Panel (a) compares adoption trajectories following small and large shocks. The small shock targets 5 nodes (17 percent) while the large shock targets 18 nodes (60 percent). Under the small shock, adoption rises during intervention but decays to 4.6 percent at terminal date—the shock fails to cross critical mass. Under the large shock, adoption crosses threshold and terminal adoption reaches 67.3 percent, nearly fifteen times higher. Panel (b) shows the cross-sectional distribution: the large shock produces bimodal adoption with mass near full adoption, while the small shock concentrates near zero.

![Refer to caption](figures/fig_critical_mass.png)

Figure 1: Critical Mass Dynamics

Notes: Panel (a) shows average adoption over time following small and large shocks. The small shock fails to reach critical mass. The large shock crosses threshold and triggers self-sustaining cascade. Panel (b) shows final adoption distribution. Parameters: N=30N=30, νs=0.8\nu\_{s}=0.8, νn=1.2\nu\_{n}=1.2, λ=0.4\lambda=0.4, κ=0.1\kappa=0.1, τ¯∗=0.35\bar{\tau}^{\*}=0.35.

Figure [2](https://arxiv.org/html/2601.04246v2#S3.F2 "Figure 2 ‣ 3.2 Results ‣ 3 Monte Carlo Evidence ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") examines intervention duration effects as characterized in Corollary [2.1](https://arxiv.org/html/2601.04246v2#S2.Thmcorollary1 "Corollary 2.1 (Temporary Intervention Threshold). ‣ Temporary Interventions and Critical Mass. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach"). Short interventions (T=1,2T=1,2) fail to cross threshold and produce terminal adoption of only 1.6–1.8 percent. Longer interventions (T=4,7T=4,7) succeed, with terminal adoption of 37–45 percent. The sharp contrast illustrates threshold nonlinearity: resources concentrated into interventions exceeding critical duration produce permanent shifts, while equivalent resources spread below threshold have negligible permanent effects.

![Refer to caption](figures/fig_temporary_intervention.png)

Figure 2: Effect of Intervention Duration on Adoption Dynamics

Notes: Short interventions (T=1,2T=1,2) produce only temporary effects. Longer interventions (T=4,7T=4,7) cross critical mass and produce permanent shifts. Parameters: N=30N=30, νs=0.5\nu\_{s}=0.5, νn=0.8\nu\_{n}=0.8, λ=0.3\lambda=0.3, κ=0.15\kappa=0.15, τ¯∗=0.35\bar{\tau}^{\*}=0.35.

Figure [3](https://arxiv.org/html/2601.04246v2#S3.F3 "Figure 3 ‣ 3.2 Results ‣ 3 Monte Carlo Evidence ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") validates the Adoption Amplification Factor. Unit shocks are applied to each node separately, and total adoption is measured at terminal date. The correlation between simulated effects and theoretical amplification factors is 0.996 (p<0.001p<0.001), confirming that the amplification factor accurately identifies technology leaders.

![Refer to caption](figures/fig_amplification_validation.png)

Figure 3: Validation of the Adoption Amplification Factor

Notes: Simulated total adoption effects plotted against theoretical amplification factors. Correlation of 0.996 (p<0.001p<0.001) confirms that the amplification factor accurately predicts technology leadership. Parameters: N=40N=40, νs=0.8\nu\_{s}=0.8, νn=1.2\nu\_{n}=1.2, λ=0.4\lambda=0.4, κ=0.1\kappa=0.1.

Table [2](https://arxiv.org/html/2601.04246v2#S3.T2 "Table 2 ‣ 3.2 Results ‣ 3 Monte Carlo Evidence ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") presents channel decomposition for the 15 highest-amplification nodes. Network components dominate (reflecting νn=1.2>νs=0.8\nu\_{n}=1.2>\nu\_{s}=0.8), and interaction terms are negative, indicating overlap between spatial and network centrality.

Table 2: Channel Decomposition of Adoption Amplification Factor (Top 15 Nodes)

| Rank | Node | Total 𝒜\mathcal{A} | Spatial | Network | Interaction |
| --- | --- | --- | --- | --- | --- |
| 1 | 3 | 20.70 | 6.63 | 16.81 | −3.74-3.74 |
| 2 | 0 | 18.95 | 6.49 | 14.37 | −2.91-2.91 |
| 3 | 2 | 18.94 | 6.32 | 15.33 | −3.71-3.71 |
| 4 | 5 | 18.81 | 6.84 | 14.18 | −3.20-3.20 |
| 5 | 6 | 18.43 | 6.73 | 13.55 | −2.85-2.85 |
| 6 | 1 | 17.51 | 6.08 | 13.67 | −3.24-3.24 |
| 7 | 10 | 16.69 | 6.39 | 11.47 | −2.18-2.18 |
| 8 | 21 | 16.45 | 6.39 | 10.52 | −1.46-1.46 |
| 9 | 4 | 16.40 | 6.60 | 11.76 | −2.96-2.96 |
| 10 | 8 | 16.11 | 6.27 | 11.79 | −2.95-2.95 |
| 11 | 12 | 14.46 | 6.98 | 8.38 | −1.89-1.89 |
| 12 | 15 | 14.30 | 6.87 | 8.56 | −2.12-2.12 |
| 13 | 9 | 14.07 | 6.96 | 8.36 | −2.25-2.25 |
| 14 | 20 | 13.47 | 6.93 | 7.27 | −1.73-1.73 |
| 15 | 23 | 13.37 | 6.73 | 7.16 | −1.52-1.52 |

* •

  Notes: Network component dominates. Negative interaction indicates spatial-network centrality overlap.

## 4 Empirical Application: SWIFT gpi Adoption

### 4.1 Institutional Setting and Data

SWIFT gpi (Global Payments Innovation) represents a major technological upgrade to the interbank payment messaging system. Launched on February 1, 2017, gpi offers same-day settlement, end-to-end tracking, and confirmation of credit to beneficiary accounts. The technology exhibits strong network externalities: banks benefit only if correspondent banks also adopt.

The sample consists of 17 Global Systemically Important Banks with complete data on adoption timing, CEO characteristics, and network position. The dependent variable is days from launch to adoption, ranging from 0 (founding members) to 305 days. The Amplification Factor is computed from the spatial-network framework using BIS bilateral exposure data and geographic coordinates.

### 4.2 Empirical Specification

The theoretical framework generates predictions about the relationship between network position, firm characteristics, and adoption timing. I estimate the following specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Daysi=β0+β1⋅CEO Agei+β2⋅𝒜i+β3⋅log⁡(Assetsi)+γ′​𝐑i+εi\text{Days}\_{i}=\beta\_{0}+\beta\_{1}\cdot\text{CEO Age}\_{i}+\beta\_{2}\cdot\mathcal{A}\_{i}+\beta\_{3}\cdot\log(\text{Assets}\_{i})+\gamma^{\prime}\mathbf{R}\_{i}+\varepsilon\_{i} |  | (33) |

where Daysi\text{Days}\_{i} is the number of days from SWIFT gpi launch (February 1, 2017) to bank ii’s adoption date; CEO Agei\text{CEO Age}\_{i} is the age of bank ii’s CEO at the time of the adoption decision; 𝒜i\mathcal{A}\_{i} is the Adoption Amplification Factor measuring network centrality; log⁡(Assetsi)\log(\text{Assets}\_{i}) is log total assets controlling for firm size; and 𝐑i\mathbf{R}\_{i} is a vector of regional indicators (Europe, Asia-Pacific, with North America as baseline).

The theoretical predictions are: β2<0\beta\_{2}<0 (network-central banks adopt earlier, reflecting their higher returns from adoption due to larger spillovers); β3<0\beta\_{3}<0 (larger banks adopt earlier, reflecting greater resources and network effects); and β1>0\beta\_{1}>0 (older CEOs adopt later, conditional on network position and size, reflecting technology hesitancy).

### 4.3 Results

Figure [4](https://arxiv.org/html/2601.04246v2#S4.F4 "Figure 4 ‣ 4.3 Results ‣ 4 Empirical Application: SWIFT gpi Adoption ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") displays the relationship between Amplification Factor and adoption timing. The correlation is strongly negative (ρ=−0.69\rho=-0.69, p=0.002p=0.002): network-central banks adopt significantly earlier. This pattern confirms the framework’s central prediction that institutions with higher amplification factors—those whose adoption decisions cascade most strongly through the system—are technology leaders who adopt first.

![Refer to caption](figures/fig_amplification_adoption.png)

Figure 4: Amplification Factor and Adoption Timing

Notes: Scatter plot of Adoption Amplification Factor against days from SWIFT gpi launch to adoption. The strong negative correlation (ρ=−0.69\rho=-0.69, p=0.002p=0.002) confirms that network-central banks adopt earlier. Colors indicate regions: blue = North America, green = Europe, red = Asia-Pacific.

Table [3](https://arxiv.org/html/2601.04246v2#S4.T3 "Table 3 ‣ 4.3 Results ‣ 4 Empirical Application: SWIFT gpi Adoption ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") presents regression results. Column (1) shows the baseline specification without size controls: the amplification factor is negative and marginally significant (−15.6-15.6 days per unit, p=0.07p=0.07). Column (2) adds log assets, which is strongly significant (−195-195 days per log unit, p<0.01p<0.01) and absorbs much of the amplification effect. Crucially, the CEO age coefficient increases from 6.0 to 15.2 days per year and becomes highly significant (p=0.01p=0.01) once size is controlled—firm size was a confounding variable. Columns (3)–(4) add regional controls and CEO tenure; the CEO age effect remains robust at 11–12 days per year.

Table 3: Determinants of SWIFT gpi Adoption Timing

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) |
| CEO Age | 6.015 | 15.150∗∗∗ | 12.390∗∗ | 11.530∗∗ |
|  | (6.835) | (5.006) | (4.700) | (4.490) |
| Amplification Factor | −-15.633∗ | −-7.564 | −-5.090 | −-11.920 |
|  | (8.079) | (5.694) | (5.830) | (7.180) |
| Log(Total Assets) |  | −-194.22∗∗∗ | −-195.61∗∗∗ | −-172.01∗∗∗ |
|  |  | (44.950) | (40.200) | (41.280) |
| CEO Tenure |  |  |  | 8.830 |
|  |  |  |  | (5.920) |
| Europe |  |  | −-79.43∗∗ | −-60.640 |
|  |  |  | (34.380) | (34.950) |
| Asia-Pacific |  |  | −-2.42 | −-5.450 |
|  |  |  | (44.310) | (42.080) |
| Region FE | No | No | Yes | Yes |
| Observations | 17 | 17 | 17 | 17 |
| R2R^{2} | 0.217 | 0.679 | 0.790 | 0.828 |

* •

  Notes: Standard errors in parentheses. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01. Dependent variable is days from SWIFT gpi launch to adoption. Baseline region is North America.

Figure [5](https://arxiv.org/html/2601.04246v2#S4.F5 "Figure 5 ‣ 4.3 Results ‣ 4 Empirical Application: SWIFT gpi Adoption ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") presents the partial regression plot for CEO age, residualizing both the dependent variable and CEO age on firm size and amplification factor. The positive slope confirms that older CEOs adopt later conditional on network position and size.

![Refer to caption](figures/fig_partial_ceo_age.png)

Figure 5: Partial Regression: CEO Age Effect

Notes: Partial regression plot showing the relationship between CEO age and adoption timing after controlling for log total assets and amplification factor. Both variables are residualized on the controls. The positive slope indicates that older CEOs adopt later, conditional on firm size and network centrality.

Figure [6](https://arxiv.org/html/2601.04246v2#S4.F6 "Figure 6 ‣ 4.3 Results ‣ 4 Empirical Application: SWIFT gpi Adoption ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") shows cumulative adoption over time. Five banks (29%) adopted at launch as founding members, but these banks account for 42% of total system amplification, confirming that the highest-amplification institutions led adoption. The adoption curve for amplification-weighted adoption rises faster than the count-based curve, indicating that network-central banks adopted disproportionately early.

![Refer to caption](figures/fig_cumulative_adoption.png)

Figure 6: Cumulative Adoption and Amplification

Notes: Cumulative adoption over time since SWIFT gpi launch. Solid line: percentage of banks adopted. Dashed line: percentage of total system amplification represented by adopters. The amplification curve rises faster, indicating network-central banks adopted earlier.

### 4.4 Two-Regime Dynamics: Empirical Evidence

The Lévy extension with state-dependent jump intensity (Proposition [2.10](https://arxiv.org/html/2601.04246v2#S2.Thmproposition10 "Proposition 2.10 (Two-Regime Characterization). ‣ Two-Regime Dynamics. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")) predicts qualitatively different adoption dynamics before and after critical mass is reached. This subsection tests whether SWIFT gpi adoption exhibits the two-regime pattern: gradual diffusion below threshold followed by accelerated cascade dynamics above threshold.

I identify the critical mass threshold using the amplification-weighted adoption measure. The founding members—Citigroup, JPMorgan Chase, HSBC, Mitsubishi UFJ, and BNP Paribas—adopted at launch (day 0). While these five banks represent only 29 percent of the sample by count, they account for 39 percent of total system amplification. Their simultaneous adoption created sufficient network externalities to trigger cascade dynamics: subsequent banks could observe successful implementation by major counterparties, reducing uncertainty and coordination costs.

Table [4](https://arxiv.org/html/2601.04246v2#S4.T4 "Table 4 ‣ 4.4 Two-Regime Dynamics: Empirical Evidence ‣ 4 Empirical Application: SWIFT gpi Adoption ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") compares adoption patterns across three periods: pre-threshold (founding members), early post-threshold (days 1–100), and late post-threshold (days 101+). The results strongly support the two-regime characterization. Pre-threshold adopters have significantly higher mean amplification factors (11.81) compared to post-threshold adopters (7.82), with the difference statistically significant (t=2.96t=2.96, p=0.010p=0.010). This confirms the framework’s prediction that high-amplification institutions—those whose adoption decisions cascade most strongly—adopt first, pushing the system above critical mass.

Table 4: Two-Regime Characterization: Pre- and Post-Threshold Adoption

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pre-Threshold | Post-Threshold | Post-Threshold |
|  | (Day 0) | (Days 1–100) | (Days 101+) |
| Number of banks | 5 | 6 | 6 |
| Percentage of sample | 29.4% | 35.3% | 35.3% |
| Mean days to adoption | 0.0 | 68.8 | 182.3 |
| Mean amplification factor 𝒜\mathcal{A} | 11.81 | 8.99 | 6.66 |
| Amplification contribution | 38.6% | 35.2% | 26.1% |
| Adoption velocity (banks per 30 days) | | | |
| Days 0–30 | 5 banks (29.4%) | | |
| Days 31–100 | 6 banks (35.3%) | | |
| Days 101+ | 6 banks (35.3%) | | |

* •

  Notes: Pre-threshold adopters (founding members) have significantly higher amplification factors than post-threshold adopters (t=2.96t=2.96, p=0.010p=0.010). Within the post-threshold period, amplification and adoption timing remain negatively correlated (ρ=−0.60\rho=-0.60, p=0.039p=0.039).

Within the post-threshold period, the framework predicts continued negative correlation between amplification and adoption timing, as higher-amplification banks benefit more from network externalities and thus adopt earlier even after critical mass is reached. The data confirm this prediction: among post-threshold adopters, amplification and days to adoption are significantly negatively correlated (ρ=−0.60\rho=-0.60, p=0.039p=0.039). Banks in the early post-threshold period (days 1–100) have mean amplification of 8.99, while late adopters (days 101+) have mean amplification of only 6.66.

Figure [7](https://arxiv.org/html/2601.04246v2#S4.F7 "Figure 7 ‣ 4.4 Two-Regime Dynamics: Empirical Evidence ‣ 4 Empirical Application: SWIFT gpi Adoption ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") displays the two-regime dynamics graphically. Panel (A) shows cumulative adoption over time, with the pre-threshold regime (blue shading) and post-threshold regime (red shading) clearly demarcated. The founding members’ adoption at day 0 represents crossing the critical mass threshold, after which adoption proceeds through cascade dynamics. The cumulative amplification curve (dashed) rises faster than the bank count curve (solid), confirming that high-amplification institutions adopted disproportionately early.

Panel (B) shows adoption velocity over time. The spike at day 0 reflects the coordinated adoption by founding members—precisely the “large shock” that Corollary [2.1](https://arxiv.org/html/2601.04246v2#S2.Thmcorollary1 "Corollary 2.1 (Temporary Intervention Threshold). ‣ Temporary Interventions and Critical Mass. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") identifies as necessary to cross the critical mass threshold. Subsequent adoption proceeds at a more gradual pace, with velocity declining over time as the remaining low-amplification banks adopt.

![Refer to caption](figures/fig_two_regime_dynamics_v2.png)

Figure 7: Two-Regime Adoption Dynamics

Notes: Panel (A) shows cumulative adoption (solid) and cumulative amplification (dashed) over time. Blue shading indicates the pre-threshold regime; red shading indicates the post-threshold regime. The founding members’ adoption at day 0 crosses the critical mass threshold (42% of total amplification). Panel (B) shows adoption velocity (banks per month) by time period. The spike at day 0 reflects coordinated founding member adoption.

Figure [8](https://arxiv.org/html/2601.04246v2#S4.F8 "Figure 8 ‣ 4.4 Two-Regime Dynamics: Empirical Evidence ‣ 4 Empirical Application: SWIFT gpi Adoption ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach") provides additional evidence for the two-regime characterization. Panel (A) fits a logistic S-curve to the cumulative adoption data. The estimated inflection point t0=89t\_{0}=89 days corresponds to the transition from accelerating to decelerating adoption—the point at which half of eventual adopters have joined. This S-curve pattern is precisely what the Lévy extension predicts: slow initial growth (pre-threshold diffusion), rapid acceleration (post-threshold cascade), and eventual saturation.

Panel (B) compares pre-threshold and post-threshold adopters directly. Founding members have both higher count-weighted importance (5 banks) and dramatically higher amplification-weighted importance (mean 𝒜=11.81\mathcal{A}=11.81 versus 7.82 for post-threshold adopters). This pattern confirms that critical mass was reached through adoption by the highest-amplification institutions, consistent with the framework’s prediction that technology leaders with outsized network influence adopt first.

![Refer to caption](figures/fig_scurve_comparison_v2.png)

Figure 8: S-Curve Dynamics and Pre- versus Post-Threshold Comparison

Notes: Panel (A) shows cumulative adoption with logistic S-curve fit. The inflection point t0=89t\_{0}=89 days marks the transition from accelerating to decelerating adoption. Panel (B) compares pre-threshold (founding members) and post-threshold adopters. Pre-threshold adopters have significantly higher mean amplification factors (t=2.96t=2.96, p=0.010p=0.010).

These empirical patterns provide strong support for the Two-Regime Characterization (Proposition [2.10](https://arxiv.org/html/2601.04246v2#S2.Thmproposition10 "Proposition 2.10 (Two-Regime Characterization). ‣ Two-Regime Dynamics. ‣ 2.9 Lévy Extension: Critical Mass and Cascade Dynamics ‣ 2 Theoretical Framework ‣ Technology Adoption and Network Externalities in Financial Systems: A Spatial-Network Approach")). The founding members’ coordinated adoption at launch created sufficient network externalities to trigger cascade dynamics, with subsequent adoption proceeding through the post-threshold regime where positive feedback accelerates diffusion. The declining amplification profile of successive adopters—from 11.81 (founding members) to 8.99 (early post-threshold) to 6.66 (late post-threshold)—confirms that technology leaders adopt first, followed by progressively more peripheral institutions as network externalities make adoption increasingly attractive.

## 5 Conclusion

This paper develops a unified framework for analyzing technology adoption in financial networks that incorporates spatial spillovers, network externalities, and their interaction. The framework is grounded in a master equation whose solution admits a Feynman-Kac representation as expected cumulative adoption pressure along stochastic paths through spatial-network space. From this representation, I derive the Adoption Amplification Factor—a structural measure of technology leadership that captures the ratio of total system-wide adoption to initial adoption following a localized shock.

The framework makes three contributions to the literature on technology adoption and dynamic coordination. First, it provides a unified treatment that nests canonical models as special cases through explicit mathematical identification. The network externality model of Katz and Shapiro ([1985](https://arxiv.org/html/2601.04246v2#bib.bib19)) emerges at discrete network steady state with the externality function v​(ni)=νn​∑jGi​j​τj/κv(n\_{i})=\nu\_{n}\sum\_{j}G\_{ij}\tau\_{j}/\kappa. The dynamic coordination model of Frankel and Pauzner ([2000](https://arxiv.org/html/2601.04246v2#bib.bib11)) emerges when spatial and network dimensions collapse to a single aggregate state, with strategic complementarity parameter (νs+νn)/κ(\nu\_{s}+\nu\_{n})/\kappa. The timing friction framework of Guimaraes et al. ([2020](https://arxiv.org/html/2601.04246v2#bib.bib16)) corresponds directly to the decay parameter: their Poisson revision rate λ\lambda equals the adjustment rate κ\kappa in the master equation. These nesting relationships, established through the discrete Feynman-Kac formula, clarify how existing insights generalize to richer spatial-network settings while demonstrating that the framework unifies rather than replaces conventional methods.

Second, the framework introduces the spatial-network interaction as a distinct channel of technology spillovers. Existing models consider either spatial diffusion or network effects in isolation. The interaction term captures amplification when both channels operate simultaneously—when geographic neighbors are also network partners, as is common in financial markets where institutions form business relationships disproportionately with geographic neighbors. The channel decomposition of the amplification factor reveals the relative importance of spatial, network, and interaction channels for each institution’s role as a technology leader. Monte Carlo simulations confirm that the amplification factor accurately predicts technology leadership, with correlation of 0.996 between theoretical amplification and simulated cascade effects.

Third, the Lévy extension with state-dependent jump intensity provides a rigorous treatment of critical mass dynamics that generates testable predictions about two-regime adoption patterns. The jump-diffusion framework predicts that below critical mass, adoption evolves through gradual diffusion; above critical mass, cascade dynamics accelerate adoption through discrete jumps. In the limit where jump intensity becomes infinite above threshold, the framework converges to deterministic cascade models, clarifying that continuous diffusion and discrete cascades describe different regimes of the same phenomenon rather than competing approaches.

The empirical application to SWIFT gpi adoption among Global Systemically Important Banks provides strong validation of the framework’s predictions, including the two-regime characterization. Network-central banks adopt significantly earlier (ρ=−0.69\rho=-0.69, p=0.002p=0.002), with founding members representing 29 percent of banks but 39 percent of total system amplification. This concentration of amplification among early adopters is precisely what the framework predicts: high-amplification institutions—those whose adoption decisions cascade most strongly through the system—adopt first, pushing the market above critical mass.

The two-regime dynamics are strikingly evident in the data. Pre-threshold adopters (founding members) have significantly higher mean amplification factors than post-threshold adopters (11.81 versus 7.83, t=2.96t=2.96, p=0.010p=0.010). Within the post-threshold period, amplification and adoption timing remain negatively correlated (ρ=−0.60\rho=-0.60, p=0.039p=0.039), with mean amplification declining from 8.99 for early post-threshold adopters to 6.66 for late adopters. This declining amplification profile—from technology leaders to progressively more peripheral institutions—matches the theoretical prediction that network externalities make adoption increasingly attractive as critical mass is reached, drawing in lower-amplification institutions who benefit from the network effects created by earlier adopters. The cumulative adoption curve exhibits classic S-curve dynamics with inflection point at approximately 89 days, consistent with the transition from accelerating to decelerating growth predicted by the Lévy extension.

Controlling for network position and firm size reveals that CEO age delays adoption by 11–15 days per year, consistent with the management literature on technology hesitancy among older executives. This finding demonstrates that both network structure and individual characteristics matter for technology diffusion in financial systems, and that the framework can identify firm-level determinants of adoption timing after accounting for network effects.

The framework has implications for technology policy in financial infrastructure. The Adoption Amplification Factor identifies technology leaders whose adoption decisions have outsized influence on system-wide outcomes. Policy interventions—subsidies, mandates, pilot programs—should target high-amplification institutions to maximize spillovers per dollar spent. The two-regime dynamics suggest that intervention timing matters: resources should be concentrated to push adoption above critical mass rather than spread thinly over time. The empirical finding that five founding members (29% of banks) were sufficient to trigger cascade dynamics by contributing 39% of system amplification provides concrete guidance on the scale of coordinated action required to overcome coordination failures.

Several directions for future research emerge from this analysis. Extensions to competing technologies can characterize the dynamics of standards competition and the conditions for tipping to dominant standards. The dual externality extension balancing adoption benefits against systemic risk from technology concentration can inform optimal standardization policy—universal adoption creates interoperability benefits but also systemic vulnerability if the common platform fails. Applying the framework to other financial technologies, including distributed ledger systems, real-time payment networks, and regulatory technology platforms, can test the generality of the two-regime adoption patterns documented here. Finally, structural estimation of the diffusion parameters (νs,νn,κ)(\nu\_{s},\nu\_{n},\kappa) and critical mass threshold τ¯∗\bar{\tau}^{\*} using adoption timing data would enable quantitative policy analysis and counterfactual simulations.

## References

* Acemoglu et al. (2015)

  Acemoglu, Daron, Asuman Ozdaglar, and Alireza Tahbaz-Salehi. 2015. “Systemic Risk and Stability in Financial Networks.” American Economic Review 105(2): 564–608.
* Aiyagari (1994)

  Aiyagari, S. R. 1994. “Uninsured idiosyncratic risk and aggregate saving.” Quarterly Journal of Economics 109(3), 659–684.
* Allen and Gale (2000)

  Allen, Franklin, and Douglas Gale. 2000. “Financial Contagion.” Journal of Political Economy 108(1): 1–33.
* Arthur (1989)

  Arthur, W. Brian. 1989. “Competing Technologies, Increasing Returns, and Lock-In by Historical Events.” Economic Journal 99(394): 116–131.
* Buchak et al. (2018)

  Buchak, Greg, Gregor Matvos, Tomasz Piskorski, and Amit Seru. 2018. “Fintech, Regulatory Arbitrage, and the Rise of Shadow Banks.” Journal of Financial Economics 130(3): 453–483.
* Burdzy et al. (2001)

  Burdzy, Krzysztof, David M. Frankel, and Ady Pauzner. 2001. “Fast Equilibrium Selection by Rational Players Living in a Changing World.” Econometrica 69(1): 163–189.
* Carlsson and Van Damme (1993)

  Carlsson, Hans, and Eric Van Damme. 1993. “Global Games and Equilibrium Selection.” Econometrica 61(5): 989–1018.
* Crouzet et al. (2023)

  Crouzet, Nicolas, Apoorv Gupta, and Filippo Mezzanotti. 2023. “Shocks and Technology Adoption: Evidence from Electronic Payment Systems.” Journal of Political Economy 131(11): 3003–3065.
* David (1985)

  David, Paul A. 1985. “Clio and the Economics of QWERTY.” American Economic Review 75(2): 332–337.
* Farrell and Saloner (1985)

  Farrell, Joseph, and Garth Saloner. 1985. “Standardization, Compatibility, and Innovation.” RAND Journal of Economics 16(1): 70–83.
* Frankel and Pauzner (2000)

  Frankel, David, and Ady Pauzner. 2000. “Resolving Indeterminacy in Dynamic Settings: The Role of Shocks.” Quarterly Journal of Economics 115(1): 285–304.
* Frankel et al. (2003)

  Frankel, David M., Stephen Morris, and Ady Pauzner. 2003. “Equilibrium Selection in Global Games with Strategic Complementarities.” Journal of Economic Theory 108(1): 1–44.
* Freixas et al. (2000)

  Freixas, Xavier, Bruno M. Parigi, and Jean-Charles Rochet. 2000. “Systemic Risk, Interbank Relations, and Liquidity Provision by the Central Bank.” Journal of Money, Credit and Banking 32(3): 611–638.
* Fuster et al. (2019)

  Fuster, Andreas, Matthew Plosser, Philipp Schnabl, and James Vickery. 2019. “The Role of Technology in Mortgage Lending.” Review of Financial Studies 32(5): 1854–1899.
* Guimaraes and Pereira (2016)

  Guimaraes, Bernardo, and Ana Elisa Pereira. 2016. “QWERTY is Efficient.” Journal of Economic Theory 163: 819–825.
* Guimaraes et al. (2020)

  Guimaraes, Bernardo, Caio Machado, and Ana E. Pereira. 2020. “Dynamic Coordination with Timing Frictions: Theory and Applications.” Journal of Public Economic Theory 22(3): 656–697.
* Higgins (2024)

  Higgins, Sean. 2024. “Financial Technology Adoption: Network Externalities of Cashless Payments in Mexico.” American Economic Review 114(11): 3469–3512.
* Huggett (1993)

  Huggett, M. 1993. “The risk-free rate in heterogeneous-agent incomplete-insurance economies.” Journal of Economic Dynamics and Control 17(5–6), 953–969.
* Katz and Shapiro (1985)

  Katz, Michael L., and Carl Shapiro. 1985. “Network Externalities, Competition, and Compatibility.” American Economic Review 75(3): 424–440.
* Katz and Shapiro (1986)

  Katz, Michael L., and Carl Shapiro. 1986. “Technology Adoption in the Presence of Network Externalities.” Journal of Political Economy 94(4): 822–841.
* Kikuchi (2025)

  Tatsuru Kikuchi. 2025. “General Equilibrium Amplification and Crisis Vulnerability: Cross-Crisis Evidence from Global Banks.” arXiv preprint arXiv:2510.24775.
* Liebowitz and Margolis (1994)

  Liebowitz, Stan J., and Stephen E. Margolis. 1994. “The Fable of the Keys.” Journal of Law and Economics 37(1): 1–22.
* Morris and Shin (1998)

  Morris, Stephen, and Hyun Song Shin. 1998. “Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks.” American Economic Review 88(3): 587–597.
* Morris and Shin (2003)

  Morris, Stephen, and Hyun Song Shin. 2003. “Global Games: Theory and Applications.” In Advances in Economics and Econometrics, ed. M. Dewatripont, L.P. Hansen, and S.J. Turnovsky, 56–114. Cambridge University Press.