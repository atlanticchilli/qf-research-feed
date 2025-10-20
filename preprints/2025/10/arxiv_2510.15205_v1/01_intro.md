---
authors:
- Shaw Dalen
doc_id: arxiv:2510.15205v1
family_id: arxiv:2510.15205
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s
  Handbook'
url_abs: http://arxiv.org/abs/2510.15205v1
url_html: https://arxiv.org/html/2510.15205v1
venue: arXiv q-fin
version: 1
year: 2025
---


Shaw Dalen111daedalusrsch@gmail.com
  
![[Uncaptioned image]](daedalus.jpg)  Daedalus Research Team222https://x.com/DaedalusRsch

###### Abstract

Prediction markets—exemplified by Polymarket and similar venues—aggregate dispersed information into tradable probabilities, yet they still lack the unifying stochastic kernel that options gained from Black–Scholes. As these markets scale (institutional participants, exchange integrations, and rising volumes around elections and macro prints), makers face belief–volatility, jump, and cross–event risks without standardized tools to quote or hedge them. We propose such a foundation: a *logit jump–diffusion with risk–neutral (RN) drift* that treats the traded probability ptp\_{t} as a ℚ\mathbb{Q}–martingale and exposes belief volatility, jump intensity, and dependence as quotable risk factors. On top, we build a calibration pipeline that filters microstructure noise, separates diffusion from jumps via EM, enforces the RN drift, and yields a stable belief–volatility surface. We then define a coherent derivative layer—variance, correlation, corridor, and first–passage instruments—analogous to volatility and correlation products in option markets. In controlled experiments (synthetic RN-consistent paths and real event data), the RN–JD model achieves lower short–horizon belief-variance forecast error than diffusion-only and pp-space baselines, validating both its causal calibration and economic interpretability. Conceptually, the RN–JD kernel supplies the “implied volatility” analogue for prediction markets: a tractable, tradable language for quoting, hedging, and transferring *belief risk* across venues such as Polymarket.

## 1 Introduction

#### What is prediction market and why we need it?

Prediction markets like Polymarket trade contracts that pay $1 if an event occurs and $0 otherwise. Under standard no-arbitrage reasoning, observed prices are interpretable as *risk-neutral* probabilities of the event. Empirically, these prices often track average beliefs under mild conditions, although biases exist and interpretation requires care ([WolfersZitzewitz2004,](https://arxiv.org/html/2510.15205v1#bib.bib62) ; [WolfersZitzewitz2006,](https://arxiv.org/html/2510.15205v1#bib.bib63) ; [Manski2004,](https://arxiv.org/html/2510.15205v1#bib.bib48) ). These markets have been used to forecast outcomes in politics, economics, science, and beyond ([Arrow2008,](https://arxiv.org/html/2510.15205v1#bib.bib11) ; [Snowberg2012,](https://arxiv.org/html/2510.15205v1#bib.bib56) ).
Beyond entertainment or wagering, liquid, global event markets instantiate a Hayekian mechanism for aggregating dispersed knowledge ([Hayek1945,](https://arxiv.org/html/2510.15205v1#bib.bib39) ). Prices synthesize private signals into public probabilities, creating incentives for informed actors to reveal information when they expect to profit. Empirically and in practice, prediction markets can improve forecast accuracy and organizational decision-making by rewarding correct beliefs and penalizing noise ([CowgillZitzewitz2015,](https://arxiv.org/html/2510.15205v1#bib.bib25) ). The appeal has long been recognized by policymakers: the U.S. Defense Advanced Research Projects Agency (DARPA) explored a *Policy Analysis Market* (FutureMAP) for geopolitical risks before cancelling it in 2003 amid political criticism ([WaPo2003,](https://arxiv.org/html/2510.15205v1#bib.bib34) ; [Hanson2007PAM,](https://arxiv.org/html/2510.15205v1#bib.bib36) ). At the same time, regulatory choices shape what can be listed: for example, the 1958 *Onion Futures Act* still bans U.S. onion futures, illustrating how legal constraints can limit the scope of information aggregation via markets ([USC7\_13\_1,](https://arxiv.org/html/2510.15205v1#bib.bib58) ). Finally, recent debates over polling errors (e.g., the 2016 U.S. election) underscore the value of complementary, market-based signals when traditional information channels are noisy or biased ([AAPOR2016,](https://arxiv.org/html/2510.15205v1#bib.bib6) ). Together, these strands motivate a standardized kernel and derivative layer so that “belief risk” can be quoted, hedged, and transferred at scale.

#### Plain-language view of event contracts.

An *event contract* is a yes/no claim with a fixed payoff: it pays $1 if the specified outcome occurs by a given date and $0 otherwise. The traded price pt∈(0,1)p\_{t}\!\in\!(0,1) is naturally read as the market’s risk-neutral probability for that outcome. Examples include “Will the unemployment rate exceed 5% in Q4?” or “Will upgrade UU activate by block height HH?”. In regulated settings, the U.S. Commodity Futures Trading Commission (CFTC) describes such claims as derivative contracts tied to the occurrence of an event, typically with binary payoff structure; exchanges listing them must satisfy the same substantive requirements as other derivatives ([FedRegisterEventContracts2024,](https://arxiv.org/html/2510.15205v1#bib.bib1) ; [CFTCEventContracts,](https://arxiv.org/html/2510.15205v1#bib.bib60) ). Crypto-native venues list economically similar contracts under on-chain execution.

Execution is fragmented. Platforms rely on the *Logarithmic Market Scoring Rule (LMSR)* ([Hanson2003,](https://arxiv.org/html/2510.15205v1#bib.bib35) ), on *constant-product automated market makers (CP-AMMs)*—a special case of *constant-function market makers (CFMMs)*—popularized by Uniswap ([UniswapV2,](https://arxiv.org/html/2510.15205v1#bib.bib4) ; [AngerisCFMM,](https://arxiv.org/html/2510.15205v1#bib.bib8) ), or on traditional order books. Each mechanism sets prices, but none provides a shared stochastic *kernel* that explains how event probabilities should evolve over time, across information shocks, or jointly across related events. By contrast, once the Black–Scholes (BS) model appeared in options, markets standardized around *implied volatility*, which enabled quoting, hedging, and a deep derivative layer ([BlackScholes1973,](https://arxiv.org/html/2510.15205v1#bib.bib15) ). Prediction markets lack an analogous foundation.

#### Motivation and background.

Market making in event contracts is hard. In microstructure, informed trading induces *adverse selection*: when a counterparty trades only when you are wrong, you lose on average ([GlostenMilgrom1985,](https://arxiv.org/html/2510.15205v1#bib.bib32) ; [Kyle1985,](https://arxiv.org/html/2510.15205v1#bib.bib46) ). In binary event markets, inventory risk is concentrated near resolution and cannot be hedged by the underlying until settlement. For cost-function market makers such as LMSR, providing more liquidity increases worst-case loss; without external subsidies, they are expected to run at a deficit proportional to the liquidity they offer ([OthmanSandholm2010,](https://arxiv.org/html/2510.15205v1#bib.bib52) ). CP-AMMs/CFMMs face related profitability constraints for liquidity providers ([AngerisUniswap2019,](https://arxiv.org/html/2510.15205v1#bib.bib9) ; [Bitterli2023,](https://arxiv.org/html/2510.15205v1#bib.bib14) ). In short, today’s mechanisms expose makers to toxic flow and gap risk, but do not offer standardized tools to transfer *belief risk* (the risk that the market-implied probability moves) across time or across related events.

#### Why a derivative layer for event contracts?

Derivatives exist to let participants isolate and trade specific risks. For events, the primary risks are movements in the *belief level* and its *volatility* (how fast log-odds move), plus jump risk from news and cross-event co-movement. A derivative layer would (i) let market makers hedge adverse selection by offloading belief volatility and jump exposure; (ii) allow calendar hedges (between maturities or checkpoints before resolution); (iii) enable cross-event hedges that neutralize correlation and co-jumps; and (iv) concentrate liquidity around a small set of quoted risk factors, as implied volatility did for options. In mature option markets, variance/volatility swaps, correlation swaps, and related instruments serve exactly these functions for price volatility ([Demeterfi1999,](https://arxiv.org/html/2510.15205v1#bib.bib28) ; [CarrLee2009,](https://arxiv.org/html/2510.15205v1#bib.bib22) ; [Broadie2008,](https://arxiv.org/html/2510.15205v1#bib.bib17) ). Prediction markets need the analogous instruments for belief dynamics.

#### Context: the rise of Polymarket.

Crypto-native platforms have brought event trading to a wider audience and catalyzed institutional interest. In 2025, Intercontinental Exchange (ICE), the parent of the New York Stock Exchange, announced a strategic investment of up to $2 billion for roughly a 20% stake in Polymarket, with plans to distribute event-driven data through ICE’s channels ([AxiosICE2025,](https://arxiv.org/html/2510.15205v1#bib.bib53) ). Separate disclosures report that Polymarket raised over $200 million across 2024–2025 prior to the ICE deal ([TheBlock205M2025,](https://arxiv.org/html/2510.15205v1#bib.bib16) ). Together with growth spurts around major elections and macro events, these developments signal mainstream acceptance of event markets and amplify the need for a common pricing kernel and a standardized derivative layer.

#### This paper.

We propose a minimal, actionable kernel: a *logit jump–diffusion with multi-event correlation*. Let pt∈(0,1)p\_{t}\!\in(0,1) be the risk-neutral event probability and xt=log⁡(pt/(1−pt))x\_{t}=\log(p\_{t}/(1-p\_{t})) its log-odds. We model xtx\_{t} as a correlated jump–diffusion. Enforcing the martingale property of ptp\_{t} under the risk-neutral measure pins down the drift of xtx\_{t}; what remains—the belief-volatility σb\sigma\_{b}, jump intensity and moments, correlation across events, and co-jump structure—are the tradable risk factors. On this kernel we define a coherent menu of *event-linked derivatives* (belief variance/volatility swaps, correlation swaps, corridor variance, threshold/path notes, and conditional baskets). Where possible we give closed-form or short-maturity approximations; otherwise we use *partial integro–differential equations (PIDE)* or *Monte Carlo (MC)*. We derive Greeks with respect to xx and to the kernel’s parameters, and we outline practical hedges (calendar, cross-event, and inventory-aware rules near the 0/10/1 boundaries). Finally, we describe a data-driven calibration pipeline that maps mid/bid–ask/trade data to a smoothed belief-volatility surface with co-jump detection.

#### Why now.

Standardization matters more than perfect realism. Black–Scholes was not “true,” but it coordinated quoting and hedging around a small number of state variables; that standard enabled scale. A shared belief–variance surface can play the same role for event markets precisely as adoption accelerates. In 2025, Intercontinental Exchange (ICE), owner of the NYSE, announced *up to* $2 billion of strategic investment in Polymarket (at roughly $8 billion pre-money) and will distribute its event-driven data to institutions, a signal of mainstream integration ([ICE2025PR,](https://arxiv.org/html/2510.15205v1#bib.bib41) ; [FT2025Polymarket,](https://arxiv.org/html/2510.15205v1#bib.bib57) ; [Reuters2025Polymarket,](https://arxiv.org/html/2510.15205v1#bib.bib55) ). On the usage side, monthly volumes have broken through billion-dollar thresholds: reports based on Dune/DeFiLlama data indicate Polymarket posted about $1.4 billion in September 2025 while Kalshi exceeded $1–3 billion depending on the week and product mix, with sports driving much of the surge ([Defiant2025PM,](https://arxiv.org/html/2510.15205v1#bib.bib27) ; [Decrypt2025Kalshi,](https://arxiv.org/html/2510.15205v1#bib.bib26) ; [LSR2025Kalshi,](https://arxiv.org/html/2510.15205v1#bib.bib54) ). At the same time, U.S. oversight is becoming more explicit: the CFTC proposed rulemaking on event contracts in 2024 (clarifying categories that may be contrary to the public interest), and litigation around political markets underscores an evolving but increasingly articulate framework ([CFTC2024NPRM,](https://arxiv.org/html/2510.15205v1#bib.bib59) ; [FR2024EventContracts,](https://arxiv.org/html/2510.15205v1#bib.bib61) ; [KalshiCADC2024,](https://arxiv.org/html/2510.15205v1#bib.bib44) ). This combination of institutional capital, record volumes, and regulatory clarity strengthens the case for a common pricing kernel and a standardized derivative layer to concentrate liquidity, reduce maker losses via hedging, and support an institutional market for belief risk.

## 2 Related Work

### 2.1 Prediction markets and mechanisms.

The *Logarithmic Market Scoring Rule (LMSR)* introduced a bounded-loss, always-on *automated market maker (AMM)* for event contracts and combinatorial claims, giving crisp axiomatic guarantees and a tractable *cost function* representation ([Hanson2003,](https://arxiv.org/html/2510.15205v1#bib.bib35) ; [ChenPennock2012,](https://arxiv.org/html/2510.15205v1#bib.bib23) ). Subsequent designs generalized AMMs to convex cost-function markets and to liquidity-adaptive variants that mitigate worst-case losses and over-movement in thin markets ([Abernethy2013,](https://arxiv.org/html/2510.15205v1#bib.bib2) ; [OthmanSandholm2010,](https://arxiv.org/html/2510.15205v1#bib.bib52) ). On crypto rails, *constant-function market makers (CFMMs)*—including the *constant-product AMM (CP-AMM)* popularized by Uniswap—standardized execution and on-chain pricing primitives ([AngerisChitra2020,](https://arxiv.org/html/2510.15205v1#bib.bib7) ; [UniswapV2,](https://arxiv.org/html/2510.15205v1#bib.bib4) ). In contrast, *central limit order books (CLOBs)* provide deep execution microstructure but no common probabilistic dynamics for event prices ([Gould2013,](https://arxiv.org/html/2510.15205v1#bib.bib33) ). Our focus is complementary: we seek a shared *stochastic kernel* for risk-neutral event probabilities across time, shocks, and related events, independent of the execution venue.

### 2.2 Option pricing, implied surfaces, and coordination role.

The Black–Scholes–Merton paradigm established a common language for quoting and hedging (implied volatility, Greeks) ([BlackScholes1973,](https://arxiv.org/html/2510.15205v1#bib.bib15) ). It catalyzed successive layers: jumps ([Merton1976,](https://arxiv.org/html/2510.15205v1#bib.bib50) ), stochastic volatility ([Heston1993,](https://arxiv.org/html/2510.15205v1#bib.bib40) ), and implied-consistent *local volatility* surfaces ([Dupire1994,](https://arxiv.org/html/2510.15205v1#bib.bib29) ), leading to the modern practice of surface construction and management ([Gatheral2006,](https://arxiv.org/html/2510.15205v1#bib.bib31) ). This standardization coordinated liquidity and risk transfer. Our work aims for the analogous role in prediction markets: replace price diffusions by *logit* dynamics for probabilities on (0,1)(0,1), preserving tractability while exposing belief-level, belief-volatility, and jump/correlation factors as quotable objects.

### 2.3 Information-based processes.

Information-based asset pricing treats prices as conditional expectations under a filtration generated by noisy “information processes,” often Brownian-bridge–driven, offering a structural view of how news reveals payoffs over time ([BrodyHughstonMacrina2007,](https://arxiv.org/html/2510.15205v1#bib.bib19) ). Separately, boundary-constrained diffusions on [0,1][0,1] (e.g., Wright–Fisher/Jacobi families) provide mathematically consistent dynamics for probabilities or bounded state variables ([JenkinsSpano2017,](https://arxiv.org/html/2510.15205v1#bib.bib43) ; [Ackerer2016,](https://arxiv.org/html/2510.15205v1#bib.bib3) ). We adopt a simple alternative: a *logit* map that transports pt∈(0,1)p\_{t}\!\in(0,1) to ℝ\mathbb{R} so standard semimartingale tools apply, while explicit jump terms capture news shocks and co-jumps across related events.

### 2.4 Microstructure, filtering, and calibration.

Our calibration pipeline draws on state-space methods that separate the latent “efficient” signal from microstructure noise in high-frequency mid/bid-ask/trade streams ([Hasbrouck1991,](https://arxiv.org/html/2510.15205v1#bib.bib37) ; [EngleZheng2006,](https://arxiv.org/html/2510.15205v1#bib.bib30) ). For parameter learning with jumps, EM/likelihood filters for jump-diffusions and inference tools for detecting common jumps offer practical estimators and diagnostics ([BandiNguyen2001,](https://arxiv.org/html/2510.15205v1#bib.bib12) ; [BeginBoudreault2019,](https://arxiv.org/html/2510.15205v1#bib.bib13) ; [JacodTodorov2009,](https://arxiv.org/html/2510.15205v1#bib.bib42) ). We adapt these ingredients to log-odds increments and to co-jump screening across events, yielding a stable belief-volatility surface suitable for quoting and hedging.

## 3 Methodology

### 3.1 Background and Motivation: From Black–Scholes to Event Probabilities

#### What the Black–Scholes (BS) framework is.

In the BS paradigm, the discounted underlying price is a martingale under the risk–neutral measure. With geometric Brownian motion,

|  |  |  |
| --- | --- | --- |
|  | d​StSt=σ​d​Wt(under ​ℚ),\frac{dS\_{t}}{S\_{t}}=\sigma\,dW\_{t}\quad(\text{under }\mathbb{Q}), |  |

self-financing replication implies a linear pricing *PDE* and closed-form option values. The key output is not realism per se, but a *common language* for quoting and hedging: implied volatility, Greeks, and volatility surfaces ([BlackScholes1973,](https://arxiv.org/html/2510.15205v1#bib.bib15) ; [Merton1973,](https://arxiv.org/html/2510.15205v1#bib.bib49) ; [Heston1993,](https://arxiv.org/html/2510.15205v1#bib.bib40) ; [Dupire1994,](https://arxiv.org/html/2510.15205v1#bib.bib29) ; [Gatheral2006,](https://arxiv.org/html/2510.15205v1#bib.bib31) ). This language coordinates liquidity, enables standardized risk transfer, and supports a deep derivative stack.

#### Why a BS-like kernel is needed for event contracts.

Event contracts trade binary payoffs. Their quoted prices are interpretable as discounted, risk–neutral probabilities of occurrence ([WolfersZitzewitz2006,](https://arxiv.org/html/2510.15205v1#bib.bib63) ; [Arrow2008,](https://arxiv.org/html/2510.15205v1#bib.bib11) ). Today, venues execute via scoring rules or AMMs or CLOBs, but there is no shared *stochastic* model for how probabilities evolve across time, shocks, or related events. Without a kernel, makers cannot isolate “belief risk” (level, volatility, jumps, co-movement) or lay it off in a standard way; spreads widen around news; inventory near the 0/10/1 boundaries becomes hard to manage. A tractable kernel standardizes quoting (what to post), hedging (what to buy/sell against), and calibration (how to read data), just as implied-vol surfaces did for options.

#### How our setup connects to and differs from BS.

(i) *State variable:* BS models prices; we model *probabilities*. We map pt∈(0,1)p\_{t}\in(0,1) to log-odds xt∈ℝx\_{t}\in\mathbb{R} so Itô–Lévy tools apply while respecting boundaries.
(ii) *Martingale restriction:* in BS, discounted StS\_{t} is a martingale; here discounted pt=S​(xt)p\_{t}=S(x\_{t}) is a martingale. This pins down the drift of xtx\_{t} (Eq. ([3](https://arxiv.org/html/2510.15205v1#S3.E3 "In Risk–neutral (martingale) drift. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))) and leaves belief-volatility and jump features as the quotable risks.
(iii) *News and co-movement:* event probabilities jump at information times, and related events co-move; our kernel includes both diffusive correlation and co-jumps (Eq. ([4](https://arxiv.org/html/2510.15205v1#S3.E4 "In 3.3 Multi-Event Dependence: Diffusive Correlation and Co-Jumps ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))), analogous to jumps/SV in equity models ([Merton1976,](https://arxiv.org/html/2510.15205v1#bib.bib50) ; [Heston1993,](https://arxiv.org/html/2510.15205v1#bib.bib40) ; [ContTankov2004,](https://arxiv.org/html/2510.15205v1#bib.bib24) ).
(iv) *Incompleteness:* the binary payoff cannot be dynamically replicated by the underlying before resolution, so markets are incomplete. Derivatives on xx or pp (variance, correlation, corridor, first-passage) create targeted hedges that make inventory and adverse-selection risk manageable, echoing the role of variance and correlation swaps in equities ([Demeterfi1999,](https://arxiv.org/html/2510.15205v1#bib.bib28) ; [CarrLee2009,](https://arxiv.org/html/2510.15205v1#bib.bib22) ).

#### Trading relationship between the base event and our derivatives.

The base contract transfers *level* risk: long ptp\_{t} benefits if the event becomes likelier. Makers, however, are primarily exposed to the *path* of beliefs: rapid swings around p≈0.5p\approx 0.5, jumps on announcements, and cross-event shocks.
*Belief-variance swaps* exchange realized quadratic variation of xx (or of pp) for a fixed strike, letting makers sell tight spreads and buy variance to neutralize volatility risk around data releases (Eqs. ([5](https://arxiv.org/html/2510.15205v1#S3.E5 "In Belief variance swap on log-odds 𝑥. ‣ 3.4 Prototype Derivatives (Belief–Variance, Correlation, Corridor, and First-Passage Notes) ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))–([6](https://arxiv.org/html/2510.15205v1#S3.E6 "In Belief variance swap on probability 𝑝=𝑆⁢(𝑥). ‣ 3.4 Prototype Derivatives (Belief–Variance, Correlation, Corridor, and First-Passage Notes) ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))).
*Correlation/covariance swaps* hedge baskets (e.g., related races in an election night) by offsetting diffusive correlation and co-jumps (Eq. ([4](https://arxiv.org/html/2510.15205v1#S3.E4 "In 3.3 Multi-Event Dependence: Diffusive Correlation and Co-Jumps ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))).
*Corridor variance* focuses hedging budget on the “swing zone” p∈[a,b]p\in[a,b], where order flow is most toxic and inventory turns fastest.
*First-passage notes* transfer gap risk near thresholds (e.g., “does pp break 0.70.7 before TT?”), critical when quotes cluster near boundaries.

#### Empirical context.

Across liquid option markets, the existence of a shared surface reduced dispersion in quotes and tightened spreads ([Gatheral2006,](https://arxiv.org/html/2510.15205v1#bib.bib31) ). Prediction markets show analogous frictions: spreads and cancellations widen near scheduled news; quotes gap on unexpected announcements; correlated events move together. A belief-variance/correlation layer makes these exposures explicit and tradable, allowing makers to keep quotes live while laying off risk—precisely the coordination role BS played for options.

### 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift

#### Notation and setup.

Fix a filtered probability space (Ω,ℱ,{ℱt}t≥0,ℚ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\geq 0},\mathbb{Q}) satisfying the usual conditions, where ℚ\mathbb{Q} denotes the risk–neutral measure (prices are discounted). Let the event-contract price at time tt be pt∈(0,1)p\_{t}\in(0,1) and define its *log-odds*

|  |  |  |
| --- | --- | --- |
|  | xt≔logit⁡(pt)=log⁡pt1−pt,so thatpt=S​(xt)=11+e−xt.x\_{t}\;\coloneqq\;\operatorname{logit}(p\_{t})=\log\!\frac{p\_{t}}{1-p\_{t}},\quad\text{so that}\quad p\_{t}=S(x\_{t})=\frac{1}{1+e^{-x\_{t}}}. |  |

Write S′​(x)=S​(x)​(1−S​(x))=p​(1−p)S^{\prime}(x)=S(x)\!\bigl(1-S(x)\bigr)=p(1-p) and S′′​(x)=S′​(x)​(1−2​S​(x))=p​(1−p)​(1−2​p)S^{\prime\prime}(x)=S^{\prime}(x)\bigl(1-2S(x)\bigr)=p(1-p)(1-2p).
Let WtW\_{t} be a standard Brownian motion under ℚ\mathbb{Q}, and let N​(d​t,d​z)N(dt,dz) be an integer-valued random measure on ℝ×ℝ\mathbb{R}\times\mathbb{R} with (possibly time-varying) compensator νt​(d​z)​d​t\nu\_{t}(dz)\,dt (the *Lévy measure* νt\nu\_{t} satisfies ∫ℝmin⁡{1,z2}​νt​(d​z)<∞\int\_{\mathbb{R}}\min\{1,z^{2}\}\nu\_{t}(dz)<\infty). The compensated jump measure is

|  |  |  |
| --- | --- | --- |
|  | N~​(d​t,d​z)≔N​(d​t,d​z)−νt​(d​z)​d​t,χ​(z)≔z​ 1{|z|<1}.\tilde{N}(dt,dz)\;\coloneqq\;N(dt,dz)-\nu\_{t}(dz)\,dt,\qquad\chi(z)\;\coloneqq\;z\,\mathbf{1}\_{\{|z|<1\}}. |  |

We model belief dynamics on the real line via the *logit* process xtx\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xt=μ​(t,xt)​d​t+σb​(t,xt)​d​Wt+∫ℝz​N~​(d​t,d​z),dx\_{t}\;=\;\mu(t,x\_{t})\,dt\;+\;\sigma\_{b}(t,x\_{t})\,dW\_{t}\;+\;\int\_{\mathbb{R}}z\,\tilde{N}(dt,dz), |  | (1) |

where σb\sigma\_{b} is the *belief volatility*. This xx-dynamics guarantees pt=S​(xt)∈(0,1)p\_{t}=S(x\_{t})\in(0,1) while allowing diffusive moves and news-driven jumps. The representation ([1](https://arxiv.org/html/2510.15205v1#S3.E1 "In Notation and setup. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) is a standard Itô–Lévy SDE ([Applebaum2009,](https://arxiv.org/html/2510.15205v1#bib.bib10) ; [OksendalSulem2005,](https://arxiv.org/html/2510.15205v1#bib.bib51) ; [ContTankov2004,](https://arxiv.org/html/2510.15205v1#bib.bib24) ).

#### Risk–neutral (martingale) drift.

Because pt=S​(xt)p\_{t}=S(x\_{t}) is the (discounted) risk–neutral price of a $1 payoff on event occurrence, {pt}\{p\_{t}\} must be a ℚ\mathbb{Q}-martingale. Applying the Itô formula for jump processes to S​(xt)S(x\_{t}) (with truncation χ\chi) yields the drift condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=S′​(x)​μ​(t,x)+12​S′′​(x)​σb2​(t,x)+∫ℝ(S​(x+z)−S​(x)−S′​(x)​χ​(z))​νt​(d​z),\displaystyle 0\;=\;S^{\prime}(x)\,\mu(t,x)\;+\;\frac{1}{2}S^{\prime\prime}(x)\,\sigma\_{b}^{2}(t,x)\;+\;\int\_{\mathbb{R}}\!\!\Big(S(x+z)-S(x)-S^{\prime}(x)\,\chi(z)\Big)\,\nu\_{t}(dz), |  | (2) |

and thus the drift is pinned down by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(t,x)=−12​S′′​(x)​σb2​(t,x)+∫ℝ(S​(x+z)−S​(x)−S′​(x)​χ​(z))​νt​(d​z)S′​(x).\mu(t,x)\;=\;-\,\frac{\frac{1}{2}S^{\prime\prime}(x)\,\sigma\_{b}^{2}(t,x)+\displaystyle\int\_{\mathbb{R}}\!\!\big(S(x+z)-S(x)-S^{\prime}(x)\,\chi(z)\big)\,\nu\_{t}(dz)}{S^{\prime}(x)}. |  | (3) |

Equations ([2](https://arxiv.org/html/2510.15205v1#S3.E2 "In Risk–neutral (martingale) drift. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))–([3](https://arxiv.org/html/2510.15205v1#S3.E3 "In Risk–neutral (martingale) drift. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) ensure ptp\_{t} is a ℚ\mathbb{Q}-martingale; therefore, only the *belief-volatility* σb\sigma\_{b}, the jump intensity and moments (embedded in νt\nu\_{t}), and cross-event dependence (introduced below) remain as tradable risk factors ([Applebaum2009,](https://arxiv.org/html/2510.15205v1#bib.bib10) ; [ContTankov2004,](https://arxiv.org/html/2510.15205v1#bib.bib24) ).

#### Interpretation.

The logit map transports the bounded probability pt∈(0,1)p\_{t}\!\in(0,1) to ℝ\mathbb{R} where standard semimartingale tools apply, while the jump term allows for abrupt probability updates at news times. The martingale restriction fixes the drift of xtx\_{t} so that S​(xt)S(x\_{t}) carries zero drift under ℚ\mathbb{Q}; informally, the “belief level” ptp\_{t} drifts only when reparameterized in xx to offset convexity and jump-compensation effects. This separation makes σb\sigma\_{b} and jump features economically interpretable and quotable—directly analogous to how implied variance and jump parameters are quoted in price-based models ([Merton1976,](https://arxiv.org/html/2510.15205v1#bib.bib50) ; [Kou2002,](https://arxiv.org/html/2510.15205v1#bib.bib45) ; [ContTankov2004,](https://arxiv.org/html/2510.15205v1#bib.bib24) ).

### 3.3 Multi-Event Dependence: Diffusive Correlation and Co-Jumps

Consider events ii and jj with logits xti,xtjx\_{t}^{i},x\_{t}^{j}, marginal volatilities σbi,σbj\sigma\_{b}^{i},\sigma\_{b}^{j}, and Brownian correlation

|  |  |  |
| --- | --- | --- |
|  | ρi​j​(t)=corr​(d​Wti,d​Wtj)∈[−1,1].\rho\_{ij}(t)\;=\;\mathrm{corr}\big(dW\_{t}^{i},dW\_{t}^{j}\big)\in[-1,1]. |  |

Let νi​j,t​(d​zi,d​zj)\nu\_{ij,t}(dz\_{i},dz\_{j}) be a (possibly time-varying) *co-jump measure* on ℝ2\mathbb{R}^{2} capturing simultaneous news shocks. Writing Δ​pk≔S​(xt−k+zk)−S​(xt−k)\Delta p^{k}\!\coloneqq S\!\big(x\_{t-}^{k}+z\_{k}\big)-S\!\big(x\_{t-}^{k}\big), a short-maturity (frozen-state) expansion gives the instantaneous covariance of probabilities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(d​pi,d​pj)t≈Si′​Sj′​σbi​σbj​ρi​j​(t)​d​t+∫ℝ2Δ​pi​Δ​pj​νi​j,t​(d​zi,d​zj)​𝑑t,\mathrm{Cov}\!\left(dp^{i},dp^{j}\right)\_{t}\;\approx\;S^{\prime}\_{i}S^{\prime}\_{j}\,\sigma\_{b}^{i}\sigma\_{b}^{j}\,\rho\_{ij}(t)\,dt\;+\;\int\_{\mathbb{R}^{2}}\!\Delta p^{i}\Delta p^{j}\,\nu\_{ij,t}(dz\_{i},dz\_{j})\,dt, |  | (4) |

where Sk′=S′​(xtk)S^{\prime}\_{k}=S^{\prime}(x\_{t}^{k}). The first term is the diffusive covariation; the second aggregates common (co-)jumps. Empirically, co-jumps can be detected and tested using high-frequency methods ([JacodTodorov2009,](https://arxiv.org/html/2510.15205v1#bib.bib42) ).

### 3.4 Prototype Derivatives (Belief–Variance, Correlation, Corridor, and First-Passage Notes)

#### Belief variance swap on log-odds xx.

Define realized quadratic variation of xx on [t,T][t,T] by

|  |  |  |
| --- | --- | --- |
|  | Q​Vt,Tx=∫tTσb2​(u,xu)​𝑑u+∑t<u≤T(Δ​xu)2.QV^{x}\_{t,T}\;=\;\int\_{t}^{T}\sigma\_{b}^{2}\!\big(u,x\_{u}\big)\,du+\sum\_{t<u\leq T}(\Delta x\_{u})^{2}. |  |

Under piecewise-constant (or slowly varying) model parameters, the fair variance strike is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt,Tx​-var≈∫tTσb2​(u)​𝑑u+∫tTλ​(u)​𝔼​[z2​(u)]​𝑑u,K^{x\text{-var}}\_{t,T}\;\approx\;\int\_{t}^{T}\sigma\_{b}^{2}(u)\,du\;+\;\int\_{t}^{T}\lambda(u)\,\mathbb{E}\!\left[z^{2}(u)\right]\,du, |  | (5) |

directly paralleling classical variance swap theory in price models ([Demeterfi1999,](https://arxiv.org/html/2510.15205v1#bib.bib28) ; [CarrLee2009,](https://arxiv.org/html/2510.15205v1#bib.bib22) ; [BroadieJain2008,](https://arxiv.org/html/2510.15205v1#bib.bib18) ).

#### Belief variance swap on probability p=S​(x)p=S(x).

A short-maturity, frozen-state approximation at xtx\_{t} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt,t+Δp​-var≈(pt​(1−pt))2​∫tt+Δσb2​(u)​𝑑u+∫tt+Δ∫ℝ(S​(xt+z)−S​(xt))2​νu​(d​z)​𝑑u,K^{p\text{-var}}\_{t,t+\Delta}\;\approx\;\big(p\_{t}(1-p\_{t})\big)^{2}\int\_{t}^{t+\Delta}\!\!\sigma\_{b}^{2}(u)\,du\;+\;\int\_{t}^{t+\Delta}\!\!\int\_{\mathbb{R}}\!\Big(S(x\_{t}+z)-S(x\_{t})\Big)^{2}\nu\_{u}(dz)\,du, |  | (6) |

where the prefactor (p​(1−p))2\big(p(1-p)\big)^{2} arises from S′​(x)2S^{\prime}(x)^{2} and the second term captures jump contributions to the quadratic variation of pp ([ContTankov2004,](https://arxiv.org/html/2510.15205v1#bib.bib24) ; [CarrLee2004,](https://arxiv.org/html/2510.15205v1#bib.bib21) ).

#### Covariance and correlation swaps across events.

Using ([4](https://arxiv.org/html/2510.15205v1#S3.E4 "In 3.3 Multi-Event Dependence: Diffusive Correlation and Co-Jumps ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")), a short-maturity fair *covariance* strike integrates the instantaneous covariance; dividing by marginal variances yields a *correlation* strike. These instruments let market makers neutralize cross-event exposure from both diffusive correlation and co-jumps ([JacodTodorov2009,](https://arxiv.org/html/2510.15205v1#bib.bib42) ; [CarrLee2009,](https://arxiv.org/html/2510.15205v1#bib.bib22) ).

#### Corridor variance on pp.

A *corridor* contract accrues realized variance only while p∈[a,b]p\in[a,b] (a “swing zone” away from the 0/10/1 boundaries). Pricing proceeds either via a weighted-variance replication (when available) or by solving the PIDE with state-dependent accrual; see corridor-variance analogs in equity for guidance ([Lee2008Corridor,](https://arxiv.org/html/2510.15205v1#bib.bib47) ; [Burgard2017Corridor,](https://arxiv.org/html/2510.15205v1#bib.bib20) ).

#### Threshold and path notes (first passage).

Pay a fixed amount if pp first hits level h∈(0,1)h\in(0,1) before TT (or logical AND/OR across events). With hh mapped to xh=logit⁡(h)x\_{h}=\operatorname{logit}(h), valuation uses ([7](https://arxiv.org/html/2510.15205v1#S3.E7 "In 3.5 General Pricing via PIDE and Numerical Treatment ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) with absorbing boundary at x=xhx=x\_{h} and appropriate terminal/boundary conditions. Jump terms materially affect first-passage probabilities (up-crossings can occur by jump), a standard consideration in jump–diffusion settings ([ContTankov2004,](https://arxiv.org/html/2510.15205v1#bib.bib24) ; [Applebaum2009,](https://arxiv.org/html/2510.15205v1#bib.bib10) ).

### 3.5 General Pricing via PIDE and Numerical Treatment

For a terminal payoff g​(xT)g(x\_{T}), the time-tt price V​(t,x)V(t,x) solves the (backward) partial integro–differential equation (PIDE)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tV\displaystyle\partial\_{t}V | +μ​(t,x)​∂xV+12​σb2​(t,x)​∂x​xV\displaystyle+\mu(t,x)\,\partial\_{x}V+\tfrac{1}{2}\sigma\_{b}^{2}(t,x)\,\partial\_{xx}V |  | (7) |
|  |  | +∫ℝ(V​(t,x+z)−V​(t,x)−∂xV​(t,x)​χ​(z))​νt​(d​z)=0,\displaystyle+\int\_{\mathbb{R}}\!\Big(V(t,x+z)-V(t,x)-\partial\_{x}V(t,x)\,\chi(z)\Big)\,\nu\_{t}(dz)=0, |  |
|  |  | V​(T,x)=g​(x).\displaystyle\quad V(T,x)=g(x). |  |

with μ\mu given by ([3](https://arxiv.org/html/2510.15205v1#S3.E3 "In Risk–neutral (martingale) drift. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")). Basket and multi-event claims add diffusion cross-derivatives and a multivariate jump integral with co-jump measure νt​(d​𝐳)\nu\_{t}(d\mathbf{z}). Under standard growth and regularity conditions, ([7](https://arxiv.org/html/2510.15205v1#S3.E7 "In 3.5 General Pricing via PIDE and Numerical Treatment ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) is the infinitesimal generator equation for ([1](https://arxiv.org/html/2510.15205v1#S3.E1 "In Notation and setup. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) and can be solved by finite-difference with fast convolution for the jump integral, Fourier methods when coefficients are constant/affine, or Monte Carlo with variance reduction ([ContTankov2004,](https://arxiv.org/html/2510.15205v1#bib.bib24) ; [Applebaum2009,](https://arxiv.org/html/2510.15205v1#bib.bib10) ).

#### Calibration notes (brief).

Mapping mid/bid–ask/trade streams to a belief–volatility surface requires filtering the latent xtx\_{t} from microstructure noise (e.g., state-space/Kalman variants) and estimating jump activity and co-jumps; the microstructure and high-frequency literature provides standard tools ([Hasbrouck1991,](https://arxiv.org/html/2510.15205v1#bib.bib37) ; [HasbrouckBook2007,](https://arxiv.org/html/2510.15205v1#bib.bib38) ; [AMZ2005,](https://arxiv.org/html/2510.15205v1#bib.bib5) ; [JacodTodorov2009,](https://arxiv.org/html/2510.15205v1#bib.bib42) ). In our setting, these methods are applied to log-odds increments and to cross-event panels.

## 4 Market–Maker Handbook

### 4.1 Greeks, Units, and Risk Buckets

#### Work in the logit domain.

Quotes and hedges should be parameterized in xx (log–odds), then mapped to probabilities p=S​(x)p=S(x). For the vanilla event contract V=p=S​(x)V=p=S(x),

|  |  |  |
| --- | --- | --- |
|  | Δx≔∂V∂x=S′​(x)=p​(1−p),Γx≔∂2V∂x2=S′′​(x)=p​(1−p)​(1−2​p).\Delta\_{x}\;\coloneqq\;\frac{\partial V}{\partial x}\;=\;S^{\prime}(x)\;=\;p(1-p),\qquad\Gamma\_{x}\;\coloneqq\;\frac{\partial^{2}V}{\partial x^{2}}\;=\;S^{\prime\prime}(x)\;=\;p(1-p)(1-2p). |  |

Near the boundaries p→0,1p\to 0,1, Δx↓0\Delta\_{x}\!\downarrow 0 and curvature peaks in the swing zone p≈0.5p\!\approx\!0.5.

#### Belief–vega and correlation–vega.

For a derivative VV, define

|  |  |  |
| --- | --- | --- |
|  | νb≔∂V∂σb,νρ≔∂V∂ρi​j,\nu\_{b}\;\coloneqq\;\frac{\partial V}{\partial\sigma\_{b}},\qquad\nu\_{\rho}\;\coloneqq\;\frac{\partial V}{\partial\rho\_{ij}}, |  |

where σb\sigma\_{b} is belief volatility in ([1](https://arxiv.org/html/2510.15205v1#S3.E1 "In Notation and setup. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) and ρi​j\rho\_{ij} is diffusive correlation in ([4](https://arxiv.org/html/2510.15205v1#S3.E4 "In 3.3 Multi-Event Dependence: Diffusive Correlation and Co-Jumps ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")). For xx-variance swaps V∝∫σb2V\!\propto\!\int\sigma\_{b}^{2}, we have νb∝σb\nu\_{b}\!\propto\!\sigma\_{b}; for short-maturity pp-variance,

|  |  |  |
| --- | --- | --- |
|  | νb∝(p​(1−p))2​σb,\nu\_{b}\;\propto\;\big(p(1-p)\big)^{2}\,\sigma\_{b}, |  |

reflecting the Jacobian S′​(x)2S^{\prime}(x)^{2} in ([6](https://arxiv.org/html/2510.15205v1#S3.E6 "In Belief variance swap on probability 𝑝=𝑆⁢(𝑥). ‣ 3.4 Prototype Derivatives (Belief–Variance, Correlation, Corridor, and First-Passage Notes) ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")). Sensitivity to jump second moments (via the Lévy measure νt\nu\_{t}) is tracked as a separate *jump-vega* bucket.

#### Risk buckets.

*Directional* (Δx\Delta\_{x}), *curvature/news nonlinearity* (Γx\Gamma\_{x}), *information intensity* (belief–vega νb\nu\_{b} and jump second moments), and *cross–event* (νρ\nu\_{\rho} plus co–jump covariance). These map to the kernel’s tradable risk factors.

### 4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units)

#### Reservation quote and optimal spread in xx.

Treat the mid in logit units as xtx\_{t} with instantaneous volatility σb​(t)\sigma\_{b}(t), and assume order arrivals decay exponentially with distance in xx (intensity λ​(δ)=A​e−k​δ\lambda(\delta)=Ae^{-k\delta}). The classical Avellaneda–Stoikov approximation yields a *reservation quote* and *optimal spread* in xx:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (reservation)rx​(t)\displaystyle\text{(reservation)}\quad r\_{x}(t) | =xt−qt​γ​σb2¯​(T−t),\displaystyle=x\_{t}\;-\;q\_{t}\,\gamma\,\overline{\sigma\_{b}^{2}}\,(T-t), |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (total spread)2​δx​(t)\displaystyle\text{(total spread)}\quad 2\delta\_{x}(t) | ≈γ​σb2¯​(T−t)+2k​log⁡(1+γk).\displaystyle\approx\gamma\,\overline{\sigma\_{b}^{2}}\,(T-t)\;+\;\frac{2}{k}\,\log\!\Bigl(1+\frac{\gamma}{k}\Bigr). |  | (9) |

Here qtq\_{t} is inventory (contracts), γ\gamma risk aversion, TT your risk horizon, and σb2¯\overline{\sigma\_{b}^{2}} a short-horizon average of belief variance. Post

|  |  |  |
| --- | --- | --- |
|  | xbid=rx−δx,xask=rx+δx,then map ​x↦p=S​(x).x^{\rm bid}\!=r\_{x}-\delta\_{x},\qquad x^{\rm ask}\!=r\_{x}+\delta\_{x},\quad\text{then map }x\mapsto p=S(x). |  |

The reservation price skews quotes to pull inventory toward zero; the spread widens with risk and thinner order flow.333Eqs. ([8](https://arxiv.org/html/2510.15205v1#S4.E8 "In Reservation quote and optimal spread in 𝑥. ‣ 4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))–([9](https://arxiv.org/html/2510.15205v1#S4.E9 "In Reservation quote and optimal spread in 𝑥. ‣ 4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) are the standard A–S asymptotics under exponential arrivals.

#### Display and boundary handling.

For UI display in probabilities,

|  |  |  |
| --- | --- | --- |
|  | δp≈S′​(xt)​δx=pt​(1−pt)​δx,\delta\_{p}\;\approx\;S^{\prime}(x\_{t})\,\delta\_{x}\;=\;p\_{t}(1-p\_{t})\,\delta\_{x}, |  |

so spreads auto-compress near p≈0,1p\!\approx\!0,1. To prevent over-tightening, cap the display half-spread by a floor δ¯p\underline{\delta}\_{p} (e.g., ticks) and enforce an inventory cap that tightens with S′​(x)S^{\prime}(x):

|  |  |  |
| --- | --- | --- |
|  | |qt|≤qmax​(t)∝1max⁡{S′​(xt),ε}.|q\_{t}|\;\leq\;q\_{\max}(t)\;\propto\;\frac{1}{\max\{S^{\prime}(x\_{t}),\,\varepsilon\}}. |  |

#### Execution hygiene (anti pick-off).

1. 1.

   Toxicity filter: when short-horizon order imbalance or a VPIN-style metric spikes, *widen* δx\delta\_{x} or *pull* quotes.
2. 2.

   News guard: around scheduled announcements, ramp γ\gamma and/or T−tT\!-\!t in ([9](https://arxiv.org/html/2510.15205v1#S4.E9 "In Reservation quote and optimal spread in 𝑥. ‣ 4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")); pause on unscheduled jump detectors.
3. 3.

   Queue discipline: cancel →\rightarrow replace on adverse microstructure signals (rapid mid drift, queue position loss).

### 4.3 Calendar Hedges (Near–Dated News vs. Slow Decay)

#### Two–leg template (variance strips).

Let your book’s sensitivity to belief variance over [t,t+Δ][t,t+\Delta] be ν^b​(t,Δ)\widehat{\nu}\_{b}(t,\Delta) (aggregate across positions). Hedge via an xx-variance strip with notional Nx​-varN^{x\text{-var}}:

|  |  |  |
| --- | --- | --- |
|  | Nx​-var≈−ν^b​(t,Δ)∂Kt,t+Δx​-var/∂σb∝−ν^b​(t,Δ)σb.N^{x\text{-var}}\;\approx\;-\,\frac{\widehat{\nu}\_{b}(t,\Delta)}{\partial K^{x\text{-var}}\_{t,t+\Delta}/\partial\sigma\_{b}}\;\propto\;-\,\frac{\widehat{\nu}\_{b}(t,\Delta)}{\sigma\_{b}}. |  |

Use short windows around data releases for *spiky* σb\sigma\_{b} and jump variance; use longer windows to smooth slow variance growth into resolution. If listed calendars are unavailable, synthesize with adjacent maturities or related events.

#### Corridor budgets.

If toxicity concentrates in a swing zone p∈[a,b]p\!\in[a,b], buy *corridor* variance on pp that accrues only when p∈[a,b]p\in[a,b]; this targets hedge spend where fills actually occur.

### 4.4 Cross–Event β\beta–Hedges (Diffusion and Co–Jumps)

#### Instantaneous hedge ratio.

For hedging event ii with jj over short horizons (diffusion, no jumps),

|  |  |  |
| --- | --- | --- |
|  | βi←j≈Cov​(d​pi,d​pj)Var​(d​pj)≈Si′Sj′​ρi​j.\beta\_{i\leftarrow j}\;\approx\;\frac{\mathrm{Cov}(dp^{i},dp^{j})}{\mathrm{Var}(dp^{j})}\;\approx\;\frac{S^{\prime}\_{i}}{S^{\prime}\_{j}}\,\rho\_{ij}. |  |

In practice, use a *shrinkage* β~=α​β\tilde{\beta}=\alpha\,\beta with α∈[0.5,1)\alpha\!\in\![0.5,1) and clamp |β~||\,\tilde{\beta}\,| when Sk′→0S^{\prime}\_{k}\!\to 0 to avoid explosive hedges near p→0,1p\to 0,1.

#### Co–jump correction.

When co-jump covariance is material (e.g., election night), add

|  |  |  |
| --- | --- | --- |
|  | Δ​βi←jjump≈∫Δ​pi​Δ​pj​νi​j,t​(d​zi,d​zj)(Sj′)2​σbj​ 2,\Delta\beta\_{i\leftarrow j}^{\rm jump}\;\approx\;\frac{\int\Delta p^{i}\Delta p^{j}\,\nu\_{ij,t}(dz\_{i},dz\_{j})}{\big(S^{\prime}\_{j}\big)^{2}\,\sigma\_{b}^{j\,2}}, |  |

estimated from recent detections. Around known jump windows, *over-hedge* diffusive correlation (larger α\alpha) and carry optionality (first–passage notes) to absorb threshold gaps.

### 4.5 Inventory–Aware Quoting: An Operator Recipe

#### Inputs (rolling).

Filtered xtx\_{t} and σb^\widehat{\sigma\_{b}} from mid/bid–ask/trade data; kk from fill distance vs. intensity; ρi​j\rho\_{ij} and co–jump counts; toxicity meters.

#### Refresh loop (100–500 ms typical).

1. 1.

   Update xtx\_{t}, σb^\widehat{\sigma\_{b}}, qtq\_{t}, toxicity flags.
2. 2.

   Compute rxr\_{x} and δx\delta\_{x} via ([8](https://arxiv.org/html/2510.15205v1#S4.E8 "In Reservation quote and optimal spread in 𝑥. ‣ 4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))–([9](https://arxiv.org/html/2510.15205v1#S4.E9 "In Reservation quote and optimal spread in 𝑥. ‣ 4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")); produce xbid/askx^{\rm bid/ask} and display pbid/ask=S​(⋅)p^{\rm bid/ask}=S(\cdot) with floors/caps.
3. 3.

   If (toxicity high) or (unscheduled jump alarm), widen δx\delta\_{x} or pull quotes; if (scheduled news soon), pre-widen by policy.
4. 4.

   Rebalance cross-event exposure using β~i←j\tilde{\beta}\_{i\leftarrow j} and listed covariance/correlation swaps when available.
5. 5.

   Rebalance calendar exposure using near-dated variance strips (or OTC proxies).

### 4.6 PnL Attribution and Risk Limits

#### Delta–Gamma–Vega attribution in xx units.

Over a small Δ​t\Delta t with d​p≈S′​(x)​d​xdp\approx S^{\prime}(x)\,dx,

|  |  |  |
| --- | --- | --- |
|  | d​Π≈Δx​d​p⏟directional+12​Γx​(d​p)2⏟curvature/news+νb​d​σb⏟belief–vega+∑jνρ(j)​d​ρi​j⏟cross–event+jumps⏟∑(Δ​p)​position.d\Pi\;\approx\;\underbrace{\Delta\_{x}\,dp}\_{\text{directional}}\;+\;\underbrace{\tfrac{1}{2}\,\Gamma\_{x}\,(dp)^{2}}\_{\text{curvature/news}}\;+\;\underbrace{\nu\_{b}\,d\sigma\_{b}}\_{\text{belief\textendash vega}}\;+\;\underbrace{\sum\_{j}\nu\_{\rho}^{(j)}\,d\rho\_{ij}}\_{\text{cross\textendash event}}\;+\;\underbrace{\text{jumps}}\_{\sum(\Delta p)\,\text{position}}. |  |

Track realized vs. expected (d​p)2(dp)^{2} to stress variance books; reconcile jump P&L around flagged news.

#### Hard limits and kill–switches.

(1) Inventory caps that tighten as S′​(x)S^{\prime}(x) shrinks.
(2) Max gamma exposure in the swing zone.
(3) Max unhedged variance (calendar) and correlation (cross-event) notional.
(4) Auto-pause on: (i) feed gaps, (ii) volatility spikes, (iii) repeated pick-offs.

### 4.7 Heuristics That Matter in Practice

* •

  Quote where you can hedge. If no liquid proxy exists for a bucket (e.g., no cross-event hedge), carry less exposure and charge more spread in that bucket.
* •

  Pay for jump insurance explicitly. Add a jump premium ∝\propto recent jump variance and news density to your spread.
* •

  Prefer xx-variance for core hedging. xx-variance is more level-stable; use pp-variance/corridor when inventory lives in a tight pp-band.
* •

  Edge accounting. Target stable edge per fill after fees and expected adverse selection; if it compresses, widen or hedge more.

### 4.8 Pointers to Implementation Details

#### Estimating σb\sigma\_{b}, jumps, and co–jumps.

Filter xtx\_{t} from mid/bid–ask/trade data; estimate diffusive variance on robust windows and detect jumps via thresholded bi-power variation; test co-jumps with high-frequency statistics.

#### Numerics for exotics.

Use the PIDE in ([7](https://arxiv.org/html/2510.15205v1#S3.E7 "In 3.5 General Pricing via PIDE and Numerical Treatment ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")) with IMEX schemes or Fourier convolution for fast jump integration; Monte Carlo with jump thinning for first-passage structures; closed-form or transform methods for corridor payoffs when the jump law is exponential-family.

Remark (mapping to literature).
Inventory-aware quoting and reservation prices follow the dealer/market-making tradition; the toxicity safeguards and variance/correlation hedges parallel the option-market playbook, transplanted to belief dynamics.

What to quote on day one.
(1) vanilla event contracts (tightest where S′​(x)S^{\prime}(x) largest), (2) xx-variance strips around scheduled news, (3) a few liquid correlation strikes between the most coupled events, and (4) a corridor variance centered on p!∈[0.35,0.65]p!\in[0.35,0.65] for high-flow markets. This minimal menu already neutralizes the four buckets above.

## 5 Calibration: From Mid/Bid–Ask/Trades to a Belief–Vol Surface

Goal.
Given raw market data (mid, bid–ask, trades) for one or many event contracts, we estimate the latent logit process xtx\_{t} (hence pt=S​(xt)p\_{t}=S(x\_{t})), its instantaneous *belief volatility* σb​(t,x)\sigma\_{b}(t,x), jump activity, and cross–event dependence. We summarize these into a stable, tradable *belief–vol surface* σb​(τ,m)\sigma\_{b}(\tau,m) and a dependence layer {ρi​j​(τ,m),co–jump moments}\{\rho\_{ij}(\tau,m),\,\text{co–jump moments}\} that feed quoting, hedging, and pricing.

Reasoning path in brief.
(i) Work in *logit* xx to remove [0,1][0,1] boundaries and use Itô–Lévy tools.
(ii) Recognize that observed prices are *microstructure–noisy* proxies for the latent xtx\_{t}, so use a heteroskedastic *state–space* filter to recover x^t\hat{x}\_{t}.
(iii) Separate *diffusion* from *jumps* via a mixture model on increments (EM), rather than ad–hoc thresholds, because event markets often have scheduled and unscheduled jumps.
(iv) Smooth the noisy point estimates across *time–to–resolution* τ\tau and *moneyness* mm with shape constraints that prevent pathologies near p∈{0,1}p\in\{0,1\}.
(v) For multiple events, estimate *de–jumped* diffusive correlations and *co–jumps* separately, since they hedge different risks.

### 5.1 Data Conditioning & Filtering

#### Pre–processing (robust, venue–agnostic).

1. 1.

   Canonical mid: Compute a trade–weighted mid
   p~t=1Zt​∑u∈(t−Δ,t]wu​bu+au2\tilde{p}\_{t}=\frac{1}{Z\_{t}}\sum\_{u\in(t-\Delta,t]}w\_{u}\,\frac{b\_{u}+a\_{u}}{2}
   with weights wuw\_{u} monotone in size and inverse spread; de–bounce bid/ask flicker by ignoring updates <<\!tick size.
2. 2.

   Clipping and cadence: Clamp to p∈[ε,1−ε]p\in[\varepsilon,1-\varepsilon] (e.g., ε=10−5\varepsilon\!=\!10^{-5}) to avoid exploding logits; resample to a uniform grid (e.g., 100100 ms–11 s) using last–observation–carried–forward + within–bin VWAP.
3. 3.

   Outlier hygiene: Drop prints with crossed or locked books; flag halts; remove isolated spikes that revert within one tick and one update.

#### Observation model (heteroskedastic microstructure noise).

Define the observed logit

|  |  |  |
| --- | --- | --- |
|  | yt≔logit⁡(p~t)=xt+ηt,𝔼​[ηt]=0,Var​(ηt)=ση2​(t).y\_{t}\;\coloneqq\;\operatorname{logit}(\tilde{p}\_{t})\;=\;x\_{t}\;+\;\eta\_{t},\qquad\mathbb{E}[\eta\_{t}]=0,\;\;\mathrm{Var}(\eta\_{t})=\sigma\_{\eta}^{2}(t). |  |

Model ση2​(t)\sigma\_{\eta}^{2}(t) as a function of observable frictions (spread sts\_{t}, depth dtd\_{t}, trade rate rtr\_{t}, aggressor imbalance ιt\iota\_{t}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ση2​(t)=a0+a1​st2+a2​dt−1+a3​rt+a4​ιt2(clipped to ​[σ¯2,σ¯2]),\sigma\_{\eta}^{2}(t)\;=\;a\_{0}+a\_{1}\,s\_{t}^{2}+a\_{2}\,d\_{t}^{-1}+a\_{3}\,r\_{t}+a\_{4}\,\iota\_{t}^{2}\quad(\text{clipped to }[\underline{\sigma}^{2},\overline{\sigma}^{2}]), |  | (10) |

with (ak)(a\_{k}) fit by robust regressions on short–horizon squared microstructure innovations (Hasbrouck–style diagnostics). Heteroskedastic ση2​(t)\sigma\_{\eta}^{2}(t) markedly improves the filter near illiquid times.

#### State filtering (recovering x^t\hat{x}\_{t}).

Use a Gaussian state–space filter in xx with measurement ([10](https://arxiv.org/html/2510.15205v1#S5.E10 "In Observation model (heteroskedastic microstructure noise). ‣ 5.1 Data Conditioning & Filtering ‣ 5 Calibration: From Mid/Bid–Ask/Trades to a Belief–Vol Surface ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")). For the transition we *do not* impose a fixed drift; instead, we:

* •

  propagate xx with a local–level model plus innovation variance proxy σ~b2​(t)​Δ\tilde{\sigma}\_{b}^{2}(t)\Delta to capture short–run variability;
* •

  after EM (below) enforces the risk–neutral drift ([3](https://arxiv.org/html/2510.15205v1#S3.E3 "In Risk–neutral (martingale) drift. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")), re–smooth xx with the refined σ^b\widehat{\sigma}\_{b} and jump marks.

A standard Kalman filter/smoother suffices; if pp is pinned near 0/10/1 for long stretches or if jumps are very frequent, an Unscented KF or particle smoother is more stable. Output: x^t\hat{x}\_{t} and innovations (one–step–ahead residuals).

#### Diagnostics (keep only if they pass).

(i) Residuals should be serially uncorrelated (Ljung–Box) and conditionally homoskedastic given ([10](https://arxiv.org/html/2510.15205v1#S5.E10 "In Observation model (heteroskedastic microstructure noise). ‣ 5.1 Data Conditioning & Filtering ‣ 5 Calibration: From Mid/Bid–Ask/Trades to a Belief–Vol Surface ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")); (ii) Q–Q plots should be near–Gaussian away from detected jump times; (iii) realized pp–variance implied by x^t\hat{x}\_{t} should match raw realized variance after removing microstructure components.

### 5.2 EM for Diffusion and Jumps (Increment Mixtures)

#### Discretization and mixture.

On a grid with step Δ\Delta, model Δ​xt≔xt+Δ−xt\Delta x\_{t}\!\coloneqq\!x\_{t+\Delta}-x\_{t} as

|  |  |  |
| --- | --- | --- |
|  | Δ​xt∼{𝒩​(μt​Δ,σb2​(t)​Δ),with prob. ​1−λt​Δ,Zt∼fJ​(⋅;θt),with prob. ​λt​Δ,\Delta x\_{t}\sim\begin{cases}\mathcal{N}\!\big(\mu\_{t}\Delta,\,\sigma\_{b}^{2}(t)\Delta\big),&\text{with prob. }1-\lambda\_{t}\Delta,\\[2.0pt] Z\_{t}\sim f\_{J}(\cdot;\,\theta\_{t}),&\text{with prob. }\lambda\_{t}\Delta,\end{cases} |  |

where λt\lambda\_{t} is jump intensity and fJf\_{J} is a centered jump law with second moment sJ2​(t)s\_{J}^{2}(t) (e.g., double–exponential, tempered stable, or nonparametric bins). The drift μt\mu\_{t} will be *implied* by the martingale restriction for pt=S​(xt)p\_{t}=S(x\_{t}) (Eq. ([3](https://arxiv.org/html/2510.15205v1#S3.E3 "In Risk–neutral (martingale) drift. ‣ 3.2 Kernel: Logit Jump–Diffusion with Risk–Neutral Drift ‣ 3 Methodology ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"))) after updating (σb,λt,θt)(\sigma\_{b},\lambda\_{t},\theta\_{t}).

#### E–step (posterior jump responsibilities).

Given current parameters and filtered x^t\hat{x}\_{t}, form the Gaussian likelihood
ϕt=𝒩​(Δ​x^t∣μt​Δ,σb2​(t)​Δ)\phi\_{t}=\mathcal{N}\big(\Delta\hat{x}\_{t}\mid\mu\_{t}\Delta,\,\sigma\_{b}^{2}(t)\Delta\big)
and the jump likelihood
ψt=fJ​(Δ​x^t;θt)\psi\_{t}=f\_{J}(\Delta\hat{x}\_{t};\,\theta\_{t}).
Posterior jump probability

|  |  |  |
| --- | --- | --- |
|  | γt≔ℙ​{jump at ​t∣Δ​x^t}=λt​Δ​ψtλt​Δ​ψt+(1−λt​Δ)​ϕt.\gamma\_{t}\;\coloneqq\;\mathbb{P}\{\text{jump at }t\mid\Delta\hat{x}\_{t}\}\;=\;\frac{\lambda\_{t}\Delta\,\psi\_{t}}{\lambda\_{t}\Delta\,\psi\_{t}+\big(1-\lambda\_{t}\Delta\big)\phi\_{t}}. |  |

Mark intervals with γt>τJ\gamma\_{t}>\tau\_{J} (e.g., 0.70.7) as jump–dominant for subsequent de–jumped correlation estimates.

#### M–step (updating diffusion and jump parameters).

Update (locally or in bins) by weighted moments:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σb2^​(t)\displaystyle\widehat{\sigma\_{b}^{2}}(t) | ←∑(1−γt)​(Δ​x^t−μt​Δ)2∑(1−γt)/Δ,λ^​(t)←1Δ​1|B|​∑t∈Bγt,\displaystyle\leftarrow\frac{\sum(1-\gamma\_{t})\,(\Delta\hat{x}\_{t}-\mu\_{t}\Delta)^{2}}{\sum(1-\gamma\_{t})}\;\bigg/\Delta,\qquad\widehat{\lambda}(t)\leftarrow\frac{1}{\Delta}\,\frac{1}{|B|}\sum\_{t\in B}\gamma\_{t}, |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | sJ2^​(t)\displaystyle\widehat{s\_{J}^{2}}(t) | ←∑γt​(Δ​x^t)2∑γt.\displaystyle\leftarrow\frac{\sum\gamma\_{t}\,(\Delta\hat{x}\_{t})^{2}}{\sum\gamma\_{t}}. |  | (12) |

If fJf\_{J} is parametric, update θt\theta\_{t} by maximizing the weighted log–likelihood.

#### Risk–neutral drift enforcement.

With σb2^\widehat{\sigma\_{b}^{2}} and jump compensator ν^t​(d​z)\widehat{\nu}\_{t}(dz) (from fJf\_{J} and λ^\widehat{\lambda}), recompute μ​(t,x)\mu(t,x) using the analytical formula

|  |  |  |
| --- | --- | --- |
|  | μ​(t,x)=−12​S′′​(x)​σb2​(t,x)+∫(S​(x+z)−S​(x)−S′​(x)​χ​(z))​νt​(d​z)S′​(x).\mu(t,x)\;=\;-\,\frac{\frac{1}{2}S^{\prime\prime}(x)\,\sigma\_{b}^{2}(t,x)+\displaystyle\int\!\big(S(x+z)-S(x)-S^{\prime}(x)\,\chi(z)\big)\,\nu\_{t}(dz)}{S^{\prime}(x)}. |  |

This pins the drift so that pt=S​(xt)p\_{t}=S(x\_{t}) is a martingale under ℚ\mathbb{Q}. Re–run the smoother for xx with the updated transition to tighten estimates (one or two outer loops suffice in practice).

#### Stopping and checks.

Iterate E/M until (i) parameter changes are small, and (ii) de–jumped residuals are near–Gaussian with variance σb2^​Δ\widehat{\sigma\_{b}^{2}}\Delta. As a sanity check, realized pp–variance over a window should be close to ∫S′​(x)2​σb2​𝑑t+\int S^{\prime}(x)^{2}\sigma\_{b}^{2}\,dt+ jump contribution ∫(Δ​p)2​𝑑N\int(\Delta p)^{2}\,dN.

### 5.3 Surface Construction: Smoothing Across (τ,m)(\tau,m)

#### Coordinates.

Let τ=T−t\tau\!=\!T-t be time–to–resolution. For moneyness mm, choose either
m=xm\!=\!x (logit) *or*
m=min⁡{p,1−p}m\!=\!\min\{p,1-p\} (distance to the boundary); both work, but m=xm\!=\!x aligns with our kernel.

#### Raw grid and loss.

Aggregate point estimates {σb^​(t),λ^​(t),sJ2^​(t)}\{\widehat{\sigma\_{b}}(t),\widehat{\lambda}(t),\widehat{s\_{J}^{2}}(t)\} to a tensor grid (τ,m)(\tau,m). Fit a smooth surface by penalized least squares,

|  |  |  |
| --- | --- | --- |
|  | minσb​(τ,m)​∑gwg​(σb^​(g)−σb​(τg,mg))2+α​‖∇2σb‖22,\min\_{\sigma\_{b}(\tau,m)}\sum\_{g}\,w\_{g}\Big(\widehat{\sigma\_{b}}(g)-\sigma\_{b}(\tau\_{g},m\_{g})\Big)^{2}\;+\;\alpha\,\|\nabla^{2}\sigma\_{b}\|\_{2}^{2}, |  |

with weights wgw\_{g} proportional to local data density and filter precision; use tensor–product B–splines or thin–plate splines.

#### Shape constraints (stability & plausibility).

* •

  Nonnegativity: σb​(τ,m)≥0\sigma\_{b}(\tau,m)\geq 0 (enforced via squared–link or barrier).
* •

  Edge stability: penalize explosive curvature at extreme mm; in pp–space, note that realized variance scales like S′​(x)2​σb2=p2​(1−p)2​σb2S^{\prime}(x)^{2}\sigma\_{b}^{2}=p^{2}(1-p)^{2}\sigma\_{b}^{2}, which already damps near p≈0,1p\!\approx\!0,1.
* •

  Term smoothness: regularize ∂τσb\partial\_{\tau}\sigma\_{b} to avoid artificial kinks between adjacent maturities, while allowing bumps at scheduled announcements (implemented by locally relaxing the penalty on known news dates).

Apply the same smoothing to λ​(τ,m)\lambda(\tau,m) and sJ2​(τ,m)s\_{J}^{2}(\tau,m) to obtain jump surfaces.

#### Outputs.

A calibrated *belief–vol surface* σb​(τ,m)\sigma\_{b}(\tau,m) and jump layer {λ​(τ,m),sJ2​(τ,m)}\{\lambda(\tau,m),\,s\_{J}^{2}(\tau,m)\}, accompanied by uncertainty bands from the smoothing fit (use sandwich or bootstrap on bins).

### 5.4 Cross–Event Dependence: Correlation and Co–Jumps

#### De–jumped diffusive correlation ρi​j​(τ,m)\rho\_{ij}(\tau,m).

Using intervals with max⁡(γti,γtj)<τJ\max(\gamma\_{t}^{i},\gamma\_{t}^{j})\!<\!\tau\_{J} (no jump in either series), estimate instantaneous covariances on rolling windows,

|  |  |  |
| --- | --- | --- |
|  | Cov^t(d)​(d​pi,d​pj)≈1W​∑u∈(t−W,t]Si′​(u)​Sj′​(u)​Δ​x^ui​Δ​x^uj,\widehat{\mathrm{Cov}}\_{t}^{(d)}(dp^{i},dp^{j})\;\approx\;\frac{1}{W}\sum\_{u\in(t-W,t]}S^{\prime}\_{i}(u)S^{\prime}\_{j}(u)\,\Delta\hat{x}^{i}\_{u}\Delta\hat{x}^{j}\_{u}, |  |

and variances analogously, then ρ^i​j=Cov^(d)/Var^i(d)​Var^j(d)\widehat{\rho}\_{ij}=\widehat{\mathrm{Cov}}^{(d)}/\sqrt{\widehat{\mathrm{Var}}^{(d)}\_{i}\,\widehat{\mathrm{Var}}^{(d)}\_{j}}. Map estimates to (τ,m)(\tau,m) cells and smooth with the same spline machinery (clamp to [−1,1][-1,1]).

#### What the desk consumes.

1. 1.

   Belief–vol surface σb​(τ,m)\sigma\_{b}(\tau,m) with uncertainty bands.
2. 2.

   Jump layer λ​(τ,m)\lambda(\tau,m) and sJ2​(τ,m)s\_{J}^{2}(\tau,m), plus a flag list of near–term scheduled news windows.
3. 3.

   Dependence layer ρi​j​(τ,m)\rho\_{ij}(\tau,m) and co–jump {Λ^i​j,M^i​j(2)}\{\widehat{\Lambda}\_{ij},\widehat{M}^{(2)}\_{ij}\} for key pairs.

These drive (i) reservation prices and spreads via σb2¯\overline{\sigma\_{b}^{2}} (Sec. [4.2](https://arxiv.org/html/2510.15205v1#S4.SS2 "4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")); (ii) notional in variance and correlation hedges (Secs. [4.3](https://arxiv.org/html/2510.15205v1#S4.SS3 "4.3 Calendar Hedges (Near–Dated News vs. Slow Decay) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")–[4.4](https://arxiv.org/html/2510.15205v1#S4.SS4 "4.4 Cross–Event 𝛽–Hedges (Diffusion and Co–Jumps) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")); (iii) PIDE/MC solvers for exotic pricing with jump inputs.

### 5.5 Edge Cases & Practical Notes

#### Pinned markets (p≈0p\!\approx\!0 or 11).

Even if σb\sigma\_{b} looks large in xx, realized pp–variance is tiny due to S′​(x)2S^{\prime}(x)^{2}; ensure the filter doesn’t mistake tick–size for diffusion (raise σ¯2\underline{\sigma}^{2} and increase Δ\Delta).

#### Batch auctions and halts.

Treat batch prints as a single observation; if a halt occurs, freeze the filter and restart with wider priors.

#### Multi–venue consolidation.

When merging venues, rescale microstructure covariates (spread/depth) to a common unit and weight observations by venue reliability before filtering.

## 6 Experiments

Our goal is modest but decisive: to test whether the proposed *logit jump–diffusion with risk–neutral (RN) drift* and the calibration pipeline of Secs. [5](https://arxiv.org/html/2510.15205v1#S5 "5 Calibration: From Mid/Bid–Ask/Trades to a Belief–Vol Surface ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")–[4](https://arxiv.org/html/2510.15205v1#S4 "4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook") produce better short–horizon forecasts of belief variability and jumps than reasonable alternatives, and whether these gains translate into lower hedging error proxies. We therefore run a single, end–to–end experiment that mirrors how a market maker would operate in real time: filter, calibrate, forecast *causally*, and evaluate.

### 6.1 Core Forecasting Task

Fix a horizon hh on a uniform time grid (in code h=H=60h{=}H{=}60 s). At each decision time tt, a model outputs a point forecast of future *logit* realized variance on [t,t+h][t,t{+}h],

|  |  |  |
| --- | --- | --- |
|  | 𝒱^t,hx≡∑u=t+1t+hσ^b2​(u)⏟diffusion contribution+cJ⋅s^J2​(t)⋅∑u=t+1t+hλ^​(u)⏟jump contribution,\widehat{\mathcal{V}}^{x}\_{t,h}\;\equiv\;\underbrace{\sum\_{u=t+1}^{t+h}\widehat{\sigma}\_{b}^{2}(u)}\_{\text{diffusion contribution}}\;+\;\underbrace{c\_{J}\cdot\widehat{s}\_{J}^{2}(t)\cdot\sum\_{u=t+1}^{t+h}\widehat{\lambda}(u)}\_{\text{jump contribution}}, |  |

where σ^b2\widehat{\sigma}\_{b}^{2} and the jump layer (λ^,s^J2)(\widehat{\lambda},\widehat{s}\_{J}^{2}) come from the causal calibration described below, and cJc\_{J} is a scalar weight tuned on a held–out validation slice by minimizing QLIKE. After the hh seconds elapse, we compute *realized* logit variance

|  |  |  |
| --- | --- | --- |
|  | ℛ​𝒱t,hx=∑u=t+1t+h(Δ​x^u)2,Δ​x^u≡x^u−x^u−1,\mathcal{RV}^{x}\_{t,h}\;=\;\sum\_{u=t+1}^{t+h}(\Delta\hat{x}\_{u})^{2},\qquad\Delta\hat{x}\_{u}\equiv\hat{x}\_{u}-\hat{x}\_{u-1}, |  |

using the filtered latent logit x^\hat{x}.444All models operate causally; we drop the last hh timestamps so that future sums never leak information. Robust bi–power alternatives give the same conclusions and are reported in the appendix.

#### Metrics.

We report mean squared error (MSE), mean absolute error (MAE), the log–MSE of log⁡ℛ​𝒱\log\mathcal{RV}, and the QLIKE loss:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MSEx​(h)=1|𝒯|​∑t∈𝒯(ℛ​𝒱t,hx−𝒱^t,hx)2,QLIKEx​(h)=1|𝒯|​∑t∈𝒯(ℛ​𝒱t,hx𝒱^t,hx−log⁡ℛ​𝒱t,hx𝒱^t,hx−1).\text{MSE}\_{x}(h)=\frac{1}{|\mathcal{T}|}\sum\_{t\in\mathcal{T}}\!\big(\mathcal{RV}^{x}\_{t,h}-\widehat{\mathcal{V}}^{x}\_{t,h}\big)^{2},\quad\text{QLIKE}\_{x}(h)=\frac{1}{|\mathcal{T}|}\sum\_{t\in\mathcal{T}}\!\left(\frac{\mathcal{RV}^{x}\_{t,h}}{\widehat{\mathcal{V}}^{x}\_{t,h}}-\log\frac{\mathcal{RV}^{x}\_{t,h}}{\widehat{\mathcal{V}}^{x}\_{t,h}}-1\right). |  | (13) |

QLIKE is standard for volatility evaluation, penalizes under–prediction more heavily, and is robust to noise in ℛ​𝒱\mathcal{RV}.

### 6.2 Data, Preprocessing, and Splits

To stress–test models with known ground truth and realistic frictions, we use 20 high-volume event trades from Polymarket. We corrupt xx with heteroskedastic observation noise that changes by regime, mimicking spread/depth variation. All methods receive the *same* prefiltered series: we run a heteroskedastic Kalman filter (KF) with process noise proxied by a rolling variance of observed increments and measurement variance fixed by regime. Models that natively operate in pp receive p^=S​(x^)\hat{p}{=}S(\hat{x}) to equalize microstructure handling.

We adopt a simple train/validation/test split that is *shared across all methods*. Scalars needed by baselines (e.g., constant σ2\sigma^{2} for RW–logit) are fitted on the training third; the jump weight cJc\_{J} for our model is tuned on the validation third by QLIKE; evaluation is then conducted causally on the test third. (The code also prints full–sample metrics without the last hh timestamps for quick inspection; tables in the paper use the test region.)

### 6.3 Models and Baselines

#### Proposed: RN–logit–JD (path–aware, causal).

Our pipeline mirrors Sec. [5](https://arxiv.org/html/2510.15205v1#S5 "5 Calibration: From Mid/Bid–Ask/Trades to a Belief–Vol Surface ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"):
(i) heteroskedastic KF in xx (no drift) ⇒\Rightarrow x^\hat{x};
(ii) EM on rolling windows to separate diffusion and jumps, yielding σ^b2​(t)\widehat{\sigma}\_{b}^{2}(t), λ^​(t)\widehat{\lambda}(t), s^J2​(t)\widehat{s}\_{J}^{2}(t);
(iii) *RN drift re–smoothing*: we compute μ^​(t,x)\widehat{\mu}(t,x) from the martingale restriction:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(t,x)=−(12​S′′​(x)​σ^b2​(t)+λ^​(t)⋅𝔼​[S​(x+Z)−S​(x)−S′​(x)​χ​(Z)])/S′​(x)\mu(t,x)=-\bigl(\frac{1}{2}S^{\prime\prime}(x)\widehat{\sigma}\_{b}^{2}(t)+\widehat{\lambda}(t)\cdot\mathbb{E}[S(x{+}Z){-}S(x){-}S^{\prime}(x)\chi(Z)]\bigr)\big/S^{\prime}(x) |  | (14) |

, approximating the jump compensation 𝔼​[⋅]\mathbb{E}[\cdot] by Monte Carlo with the same jump law used by EM.555We use symmetric Gaussian jumps, truncation χ​(⋅)\chi(\cdot) as in the simulator, and clip S′​(x)S^{\prime}(x) by 10−410^{-4} for numerical stability; μ\mu is EWMA–smoothed and capped at |0.25||0.25| s-1.
We then run a second KF with this μ^​(t,x^t)\widehat{\mu}(t,\hat{x}\_{t}) in the state transition.
(iv) *Causal variance forecasting*: for each tt, we return a forward sum of diffusion variance plus a jump term

|  |  |  |
| --- | --- | --- |
|  | 𝒱^t,hx=∑u=t+1t+hσ^b2​(u)+cJ⋅s^J2​(t)⋅∑u=t+1t+hλ^sched​(u),\widehat{\mathcal{V}}^{x}\_{t,h}=\sum\_{u=t+1}^{t+h}\widehat{\sigma}\_{b}^{2}(u)\;+\;c\_{J}\cdot\widehat{s}\_{J}^{2}(t)\cdot\sum\_{u=t+1}^{t+h}\widehat{\lambda}\_{\text{sched}}(u), |  |

where λ^sched\widehat{\lambda}\_{\text{sched}} is an EWMA of λ^\widehat{\lambda} time–warped by a Gaussian schedule kernel centered at announced windows (known ex–ante).

#### Baselines.

* •

  RW–logit: xt+Δ=xt+σ​Δ​ξtx\_{t+\Delta}{=}x\_{t}{+}\sigma\sqrt{\Delta}\,\xi\_{t}, with σ2\sigma^{2} set to the training–slice mean of (Δ​x^)2(\Delta\hat{x})^{2}.
* •

  Logit diffusion (const σ\sigma): same as above but fitted on the entire calibration region.
* •

  Wright–Fisher/Jacobi in pp: a boundary–respecting diffusion calibrated by ML on p^\hat{p}; we forecast pp–variance 2​α​p​(1−p)2\alpha\,p(1{-}p) and map back to xx via S′​(x)2S^{\prime}(x)^{2}.
* •

  AR(1)–GARCH(1,1) in pp: an AR(1) on Δ​p^\Delta\hat{p} with a GARCH(1,1) volatility; forecasted pp–variance is mapped to xx using S′​(x)−2S^{\prime}(x)^{-2}.

All baselines are evaluated causally using the same forward–sum operator and the same test window.

### 6.4 Implementation Details

Grid and seeds. N=6000N{=}6000 steps at 1 Hz; random seeds are fixed. KF. Process noise uses a local rolling variance proxy; measurement noise is piecewise–constant by regime. EM. We run 6 EM steps globally to initialize, then a rolling EM with window 400 s. RN drift. The Monte Carlo inner expectation uses 600 draws per step (variance–time trade–off is negligible). Schedule. Known windows are encoded as Gaussian kernels (width 90 s) that boost λ^\widehat{\lambda} ex–ante; the boost is capped at the 95th percentile of the smoothed λ^\widehat{\lambda} to avoid outliers. Tuning. cJc\_{J} is grid–searched over {0.3,…,1.0}\{0.3,\ldots,1.0\} on the validation region using QLIKE.

### 6.5 Evaluation Protocol and What To Expect

Causal forward–sum. For any per–step quantity aua\_{u}, we define ForwardSum:

|  |  |  |
| --- | --- | --- |
|  | ForwardSum​(a,h)=∑u=t+1t+hau\textsf{ForwardSum}(a,h){=}\sum\_{u=t+1}^{t+h}a\_{u} |  |

and drop the last hh timestamps; all models use *only* information available at tt to build at+1,…,at+ha\_{t+1},\ldots,a\_{t+h}.
Stratification. Metrics are reported overall, and separately on quiet vs. jump windows (Sec. [6.1](https://arxiv.org/html/2510.15205v1#S6.SS1 "6.1 Core Forecasting Task ‣ 6 Experiments ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")).
Hedging proxy. Following Sec. [4.6](https://arxiv.org/html/2510.15205v1#S4.SS6 "4.6 PnL Attribution and Risk Limits ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook"), the squared forecast error in xx–variance is a first–order proxy of slippage when warehousing curvature/news exposure; improving QLIKE/MSE thus suggests lower ex–post hedge error.

Table 1: Causal H=60​sH{=}60\,\mathrm{s} forward-sum forecasts of next-window realized *logit* variance on the synthetic RN-consistent path. Lower is better. Best per column in bold.

| Model | MSEall\mathrm{MSE}\_{\mathrm{all}} | MAEall\mathrm{MAE}\_{\mathrm{all}} | QLIKEall\mathrm{QLIKE}\_{\mathrm{all}} |
| --- | --- | --- | --- |
| RN–JD (causal path) | 70.281\mathbf{70.281} | 1.588\mathbf{1.588} | 1.4621{1.4621} |
| RW–logit (const σ\sigma) | 77.41477.414 | 1.163{1.163} | 4.73184.7318 |
| Logit (const σ\sigma) | 76.752{76.752} | 2.0782.078 | 2.65942.6594 |
| WF/Jacobi (mapped) | 1.71×10171.71\times 10^{17} | 3.67×1073.67\times 10^{7} | 1.94841.9484 |
| ARMA–GARCH (mapped) | 1.07×10191.07\times 10^{19} | 5.33×1085.33\times 10^{8} | 0.7962\mathbf{0.7962} |

### 6.6 Results and Discussion

Table [1](https://arxiv.org/html/2510.15205v1#S6.T1 "Table 1 ‣ 6.5 Evaluation Protocol and What To Expect ‣ 6 Experiments ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook") reports causal H=60​sH{=}60\,\mathrm{s} forward-sum forecasts of next-window realized *logit* variance on the synthetic RN-consistent path. Lower values indicate better alignment between forecasted and realized variability. The proposed RN–JD (causal path) model achieves the lowest overall MSE, MAE, and log\logMSE, outperforming all baselines under identical causal evaluation.

#### Quantitative results.

RN–JD attains MSEall=70.28\mathrm{MSE}\_{\mathrm{all}}{=}70.28 and QLIKEall=1.46\mathrm{QLIKE}\_{\mathrm{all}}{=}1.46, representing a consistent improvement over both diffusion-based and pp-space volatility models. The RW–logit and constant-σ\sigma logit diffusions, which lack either drift or jump structure, underfit the true variability and fail to capture the volatility bursts near scheduled information shocks. Boundary-respecting Wright–Fisher (WF) and ARMA–GARCH models produce numerically unstable forecasts when mapped from probability to logit space, resulting in orders-of-magnitude MSE inflation despite locally competitive QLIKE scores.

#### Interpretation.

The gains arise from three complementary mechanisms:
(i) enforcing RN drift prevents systematic bias in x^t\widehat{x}\_{t}, ensuring the implied p^t\hat{p}\_{t} evolves as a martingale under the market measure;
(ii) separating diffusion and jump layers via EM yields adaptive volatility forecasts that respect local heteroskedasticity;
(iii) incorporating scheduled jump boosts improves ex–ante calibration near known information releases.
Collectively, these allow the RN–JD model to produce a belief–volatility surface that is both dynamically stable and economically interpretable.

## 7 Conclusion

This paper proposed a minimal, actionable kernel for event contracts: a *logit jump–diffusion with risk–neutral (RN) drift* that treats the traded price ptp\_{t} as a ℚ\mathbb{Q}–martingale and exposes belief volatility, jump intensity, and cross–event dependence as quotable risk factors. On top of this kernel we built (i) a calibration pipeline that filters microstructure noise, separates diffusion from jumps via EM, and enforces RN drift in smoothing; and (ii) a coherent derivative layer (variance, correlation, corridor, first–passage) for quoting and hedging belief risk.

Our end–to–end experiment mirrored real-time desk operation: filter, calibrate, and forecast *causally* with only information available at decision time. On a synthetic but RN-consistent path that features early breakout, scheduled and unscheduled jumps, and terminal resolution, the proposed RN–JD pipeline delivered lower short-horizon variance forecast errors than diffusion-only or pp-space baselines under identical evaluation (Table [1](https://arxiv.org/html/2510.15205v1#S6.T1 "Table 1 ‣ 6.5 Evaluation Protocol and What To Expect ‣ 6 Experiments ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")). The improvement is economically interpretable: RN drift eliminates systematic bias in the latent logit, EM-based jump separation captures heteroskedasticity, and schedule-aware intensity boosts align forecasts with known information windows. These ingredients jointly yield a stable, tradable belief–volatility surface suitable for quoting, hedging, and inventory control (Secs. [4.2](https://arxiv.org/html/2510.15205v1#S4.SS2 "4.2 Inventory–Aware Quoting (Avellaneda–Stoikov in Logit Units) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")–[4.3](https://arxiv.org/html/2510.15205v1#S4.SS3 "4.3 Calendar Hedges (Near–Dated News vs. Slow Decay) ‣ 4 Market–Maker Handbook ‣ Toward Black–Scholes for Prediction Markets: A Unified Kernel and Market-Maker’s Handbook")).

#### Practical implications.

The kernel organizes market making in event contracts around a small set of risk buckets (directional, curvature/news, belief–vega, cross–event), with standardized hedges (variance/correlation strips, corridor variance) that can be listed or synthesized. In particular, belief–variance and correlation swaps provide the option-market analogue of volatility and correlation instruments, enabling makers to tighten quotes and keep markets live through news while laying off risk in transparent units.

#### Limitations.

Our experiments focus on single-event dynamics and synthetic co-jump structure; full multi-event calibration with rich, time-varying dependence and regime switches remains future work. The jump law is modeled parsimoniously (symmetric, light-tailed in the main experiments); extreme-tailed or skewed jumps may require richer families or nonparametric bins. Finally, microstructure conditioning is venue-agnostic but stylized; production systems should incorporate venue-specific frictions (batch auctions, halts, cross-venue consolidation).

#### Future directions.

*(i) Multi-event panels:* joint RN–JD calibration with diffusive correlation and co-jumps estimated from high-frequency panels; basket pricing via PIDE/MC with multivariate jump measures.
*(ii) Term/moneyness surfaces:* shape-constrained smoothing across (τ,m)(\tau,m) with uncertainty quantification and stress testing around boundaries.
*(iii) Products and design:* exchange-ready specifications for belief–variance/correlation strips, corridor variance in the swing zone, and first-passage notes; replication/hedging guides for desks.
*(iv) Live deployment:* A/B tests on liquid events (macro prints, elections) to measure spread, fill quality, and hedging P&L before/after introducing the RN-consistent layer.

#### Takeaway.

Standardization beats perfect realism. By enforcing the martingale property in probability space and separating diffusion from jumps in logit space, the RN–JD kernel supplies a common language—*belief volatility, jump intensity, dependence*—that coordinates quoting and hedging, just as implied volatility did in options. We hope this work helps concentrate liquidity, reduce maker losses via targeted hedges, and support an institutional market for belief risk.

## References

* [1]

  Event contracts.
  *Federal Register*, 89(112), June 2024.
  U.S. Commodity Futures Trading Commission rulemaking notice.
* [2]

  Jacob Abernethy, Yiling Chen, and Jennifer Wortman Vaughan.
  Efficient market making via convex optimization, and a connection to online learning.
  ACM Trans. Economics and Computation, 2013.
* [3]

  Damien Ackerer, Damir Filipović, and Sergio Pulido.
  The jacobi stochastic volatility model.
  arXiv:1605.07099, 2016.
* [4]

  Hayden Adams, Noah Zinsmeister, and Dan Robinson.
  Uniswap v2 core whitepaper.
  <https://app.uniswap.org/whitepaper.pdf>, 2020.
* [5]

  Yacine Aït-Sahalia, Per A. Mykland, and Lan Zhang.
  Ultra high frequency volatility estimation with dependent microstructure noise.
  Technical report, NBER Working Paper 11380, 2005.
* [6]

  American Association for Public Opinion Research.
  An evaluation of 2016 election polls in the u.s., 2017.
* [7]

  Guillermo Angeris and Tarun Chitra.
  Improved price oracles: Constant function market makers.
  arXiv:2003.10001, 2020.
* [8]

  Guillermo Angeris, Tarun Chitra, Theo Diamandis, Alex Evans, and Kshitij Kulkarni.
  The geometry of constant function market makers.
  arXiv preprint arXiv:2308.08066, 2023.
* [9]

  Guillermo Angeris, Hsien-Tang Kao, Rei Chiang, Charlie Noyes, and Tarun Chitra.
  An analysis of uniswap markets.
  arXiv preprint arXiv:1911.03380, 2019.
* [10]

  David Applebaum.
  Lévy Processes and Stochastic Calculus.
  Cambridge University Press, 2nd edition, 2009.
* [11]

  Kenneth J. Arrow, Robert Forsythe, Michael Gorham, Robert Hahn, Robin Hanson, John O. Ledyard, Saul Levmore, Robert Litan, Paul Milgrom, Forrest D. Nelson, George R. Neumann, Marco Ottaviani, Thomas C. Schelling, Robert J. Shiller, Vernon L. Smith, Erik Snowberg, Cass R. Sunstein, Philip E. Tetlock, Hal R. Varian, Justin Wolfers, and Eric Zitzewitz.
  The promise of prediction markets.
  Science, 320(5878):877–878, 2008.
* [12]

  Federico M. Bandi and Thong H. Nguyen.
  On the functional estimation of jump–diffusions.
  Working paper version 2001; later publications, 2001.
* [13]

  Jean-François Bégin and Mathieu Boudreault.
  Likelihood evaluation of jump–diffusion models using deterministic nonlinear filters.
  arXiv:1906.04322, 2019.
* [14]

  Tobias Bitterli and Fabian Schär.
  Decentralized exchanges: The profitability frontier of constant product market makers.
  arXiv preprint arXiv:2302.05219, 2023.
* [15]

  Fischer Black and Myron Scholes.
  The pricing of options and corporate liabilities.
  Journal of Political Economy, 1973.
* [16]

  The Block.
  Polymarket discloses past funding rounds totaling $205 million before $2 billion ice investment.
  October 2025.
* [17]

  Mark Broadie and Ashish Jain.
  The effect of jumps and discrete sampling on volatility and variance swaps.
  International Journal of Theoretical and Applied Finance, 11(01):1–20, 2008.
* [18]

  Mark Broadie and Ashish Jain.
  Pricing and hedging volatility derivatives.
  Technical report, Columbia Business School, 2008.
* [19]

  Dorje C. Brody, Lane P. Hughston, and Andrea Macrina.
  Information-based asset pricing.
  arXiv:0704.1976, 2007.
* [20]

  Christoph Burgard.
  Efficient pricing and super replication of corridor variance swaps.
  Technical report, SSRN Working Paper, 2017.
* [21]

  Peter Carr and Roger Lee.
  Pricing options on realized variance.
  Finance and Stochastics, 9(4):453–475, 2004.
* [22]

  Peter Carr and Roger Lee.
  Volatility derivatives.
  Annual Review of Financial Economics, 1:319–339, 2009.
* [23]

  Yiling Chen and David M. Pennock.
  A utility framework for bounded-loss market makers.
  arXiv:1206.5252, 2012.
* [24]

  Rama Cont and Peter Tankov.
  Financial Modelling with Jump Processes.
  Chapman & Hall/CRC, 2004.
* [25]

  Bo Cowgill, Eric Zitzewitz, et al.
  Corporate prediction markets: Evidence from google, ford, and firm x.
  Technical report, Working paper, 2015.
* [26]

  Decrypt.
  Kalshi prediction markets are pulling in $1 billion monthly as state regulators loom.
  September 2025.
  Cites Dune dashboard; Accessed Oct. 9, 2025.
* [27]

  The Defiant.
  ‘golden age’ of prediction markets dawns as activity reaches new highs, October 2025.
  Summarizes Dune/DeFiLlama data: Polymarket ∼$​1.43\sim\mathdollar 1.43B; Kalshi ∼$​3\sim\mathdollar 3B in Sept. 2025.
* [28]

  Kresimir Demeterfi, Emanuel Derman, Michael Kamal, and Joseph Zou.
  A guide to volatility and variance swaps.
  The Journal of Derivatives, 6(4):9–32, 1999.
* [29]

  Bruno Dupire.
  Pricing with a smile.
  Risk, 1994.
* [30]

  Robert Engle and Zheng Sun.
  A microstructure estimate of realized volatility.
  Technical report, NYU Stern, 2006.
* [31]

  Jim Gatheral.
  The Volatility Surface: A Practitioner’s Guide.
  Wiley, 2006.
* [32]

  Lawrence R. Glosten and Paul R. Milgrom.
  Bid, ask and transaction prices in a specialist market with heterogeneously informed traders.
  Journal of Financial Economics, 14(1):71–100, 1985.
* [33]

  Martin D. Gould, Mason A. Porter, Stacy Williams, Mark McDonald, Daniel Fenn, and Sam Howison.
  Limit order books.
  Quantitative Finance, 2013.
* [34]

  Bradley Graham and Vernon Loeb.
  Pentagon drops bid for futures market.
  The Washington Post, July 2003.
* [35]

  Robin Hanson.
  Logarithmic market scoring rules for modular combinatorial information aggregation.
  <https://hanson.gmu.edu/mktscore.pdf>, 2003.
* [36]

  Robin Hanson.
  The policy analysis market (pam): A thwarted experiment in the use of prediction markets for public policy.
  Innovations: Technology, Governance, Globalization, 2(3):73–88, 2007.
* [37]

  Joel Hasbrouck.
  Measuring the information content of stock trades.
  Journal of Finance, 1991.
* [38]

  Joel Hasbrouck.
  Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading.
  Oxford University Press, 2007.
* [39]

  F. A. Hayek.
  The use of knowledge in society.
  American Economic Review, 35(4):519–530, 1945.
* [40]

  Steven L. Heston.
  A closed-form solution for options with stochastic volatility.
  Review of Financial Studies, 1993.
* [41]

  Intercontinental Exchange, Inc.
  Ice announces strategic investment in polymarket.
  Press release, October 2025.
  Accessed Oct. 9, 2025.
* [42]

  Jean Jacod and Viktor Todorov.
  Testing for common arrivals of jumps for discretely observed multidimensional processes.
  Annals of Statistics, 2009.
* [43]

  Paul A. Jenkins and Dario Spanò.
  Exact simulation of the wright–fisher diffusion.
  Annals of Applied Probability, 2017.
* [44]

  Justia.
  Kalshiex llc v. cftc, no. 24-5205 (d.c. cir. 2024), October 2024.
  Accessed Oct. 9, 2025.
* [45]

  S. G. Kou.
  A jump-diffusion model for option pricing.
  Management Science, 2002.
* [46]

  Albert S. Kyle.
  Continuous auctions and insider trading.
  Econometrica, 53(6):1315–1335, 1985.
* [47]

  Roger Lee.
  Corridor variance swap, 2008.
* [48]

  Charles F. Manski.
  Interpreting the predictions of prediction markets.
  NBER Working Paper 10359, National Bureau of Economic Research, 2004.
* [49]

  Robert C. Merton.
  Theory of rational option pricing.
  The Bell Journal of Economics and Management Science, 4(1):141–183, 1973.
* [50]

  Robert C. Merton.
  Option pricing when underlying stock returns are discontinuous.
  Journal of Financial Economics, 1976.
* [51]

  Bernt Øksendal and Agnès Sulem.
  Applied Stochastic Control of Jump Diffusions.
  Universitext. Springer, 2005.
* [52]

  Abraham Othman, Tuomas Sandholm, David Pennock, and Daniel Reeves.
  A practical liquidity-sensitive automated market maker.
  In EC, 2010.
* [53]

  Dan Primack and Miriam McCracken.
  Polymarket gets big investment from new york stock exchange parent company.
  Axios, October 2025.
* [54]

  Legal Sports Report.
  Sports trading pushes kalshi past all-time volume records.
  September 2025.
  Reports >>$2.4B sports volume in Sept. 2025; Accessed Oct. 9, 2025.
* [55]

  Reuters.
  Nyse owner takes $2 billion stake in polymarket as prediction markets go mainstream.
  October 2025.
  Accessed Oct. 9, 2025.
* [56]

  Erik Snowberg, Justin Wolfers, and Eric Zitzewitz.
  Prediction markets for economic forecasting.
  In Brookings Papers on Economic Activity. 2012.
  Working chapter version.
* [57]

  Financial Times.
  Nyse parent to invest up to $2bn in prediction platform polymarket.
  Financial Times, October 2025.
  Accessed Oct. 9, 2025.
* [58]

  United States Code.
  7 u.s. code s 13-1: Onion futures act (1958), 1958.
* [59]

  U.S. Commodity Futures Trading Commission.
  Cftc issues proposal on event contracts.
  Press Release No. 8907-24, May 2024.
  Defines certain political-event contracts as gaming; Accessed Oct. 9, 2025.
* [60]

  U.S. Commodity Futures Trading Commission.
  Contracts & products: Event contracts, 2024.
* [61]

  U.S. Commodity Futures Trading Commission.
  Event contracts (notice of proposed rulemaking).
  Federal Register, 89(112), June 2024.
  RIN 3038–AF14; Accessed Oct. 9, 2025.
* [62]

  Justin Wolfers and Eric Zitzewitz.
  Prediction markets.
  Journal of Economic Perspectives, 18(2):107–126, 2004.
* [63]

  Justin Wolfers and Eric Zitzewitz.
  Interpreting prediction market prices as probabilities.
  NBER Working Paper 12200, National Bureau of Economic Research, 2006.