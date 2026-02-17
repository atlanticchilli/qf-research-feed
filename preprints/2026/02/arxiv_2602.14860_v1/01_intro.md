---
authors:
- Giulio Marino
- Manuel Naviglio
- Francesco Tarantelli
- Fabrizio Lillo
doc_id: arxiv:2602.14860v1
family_id: arxiv:2602.14860
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Predicting the success of new crypto-tokens: the Pump.fun case'
url_abs: http://arxiv.org/abs/2602.14860v1
url_html: https://arxiv.org/html/2602.14860v1
venue: arXiv q-fin
version: 1
year: 2026
---


Giulio Marino
Dipartimento di Fisica “E. Fermi”, Università di Pisa, Largo Pontecorvo 3, 56127 Pisa, Italy
INFN Sezione di Pisa, Polo Fibonacci, Largo B. Pontecorvo 3, 56127 Pisa, Italy
  
Manuel Naviglio
Scuola Normale Superiore, Pisa, Italy
  
Francesco Tarantelli
Dipartimento di Matematica, Università di Bologna, Bologna, Italy.
  
Fabrizio Lillo
Scuola Normale Superiore, Pisa, Italy

###### Abstract

We study the dynamics of token launched on Pump.fun, a Solana-based launchpad platform, to identify the determinants of the token success. Pump.fun employs a bonding curve mechanism to bootstrap initial liquidity possibly leading to graduation to the on-chain market, which can be seen as a token success. We build predictive models of the probability of graduation conditional on the current amount of Solana locked in the bonding curve and a set of explanatory variables that capture structural and behavioral aspects of the launch process. Conditioning the graduation probability on these variables significantly improves its predictive power, providing insights into early-stage market behavior, speculative and manipulative dynamics, and the informational efficiency of bonding-curve-based token launches.

## I Introduction

The advent of blockchain technology has dramatically lowered the barriers to issuing new crypto-assets.
Today, tokens can be minted cheaply and almost instantaneously through web interfaces or applications, requiring only a small amount of capital to cover transaction and deployment fees.
In many cases, tokens are introduced by protocol teams as a mechanism to bootstrap ecosystems, incentivize users, or raise resources for further development.
Prominent examples include governance tokens such as JTO (Jito), MORPHO (Morpho), AAVE (Aave), COMP (Compound), as well as the native PUMP token of the Pump.fun launchpad on Solana.

Once issued, tokens, regardless of whether they are backed by a substantive underlying project, become tradable on centralized and decentralized exchanges, where liquidity and price formation are endogenously determined by investor demand.
Projects that manage to construct credible narratives or perceived utility often attract larger communities of traders, a process typically reflected in higher trading volumes and prices.
However, in the absence of verifiable fundamentals, early token adoption is rarely driven by intrinsic value in the traditional sense.
Instead, it is largely shaped by coordination dynamics among traders, in a mechanism reminiscent of Keynes’ “beauty contest” Keynes ([1936](https://arxiv.org/html/2602.14860v1#bib.bib24 "The general theory of employment, interest and money")); Allen et al. ([2006](https://arxiv.org/html/2602.14860v1#bib.bib23 "Beauty contests and iterated expectations in asset markets")); Morris and Shin ([2002](https://arxiv.org/html/2602.14860v1#bib.bib25 "Social value of public information")), where agents attempt to anticipate others’ demand rather than to assess long-run economic worth.

This technological ease of token creation has a direct statistical consequence: crypto markets are characterized by an extreme proliferation of new assets and by a vanishingly small fraction of “successful” launches.
On most platforms, the overwhelming majority of newly issued tokens exhibit short lifetimes, low liquidity, or outright malicious behavior.
Empirical evidence from Uniswap-style listings shows that most tokens fail to sustain meaningful trading activity, often due to rug-pulls or contract-level manipulation.
For instance, in Naviglio et al. ([2025](https://arxiv.org/html/2602.14860v1#bib.bib4 "Price manipulation schemes of new crypto-tokens in decentralized exchanges")) we document that approximately 88%88\% of tokens launched on Uniswap v2 in late 2024 can be classified as manipulation schemes.

A crucial source of heterogeneity in these markets arises from the *design of smart contracts*.
The contractual rules governing token creation, transfers, minting, burning, and trading permissions can profoundly affect a token lifecycle independently of market demand.
In particular, certain design choices embed manipulation mechanisms directly into the contract logic, for instance by restricting sell permissions or introducing asymmetric transfer rules.
Such designs, commonly referred to as *honeypots*, mechanically trap liquidity and make apparent early success misleading, as the eventual collapse of the token may be encoded in the contract itself rather than driven by endogenous market forces Qin et al. ([2021](https://arxiv.org/html/2602.14860v1#bib.bib5 "Quantifying blockchain extractable value: how dark is the forest?")); Torres et al. ([2019](https://arxiv.org/html/2602.14860v1#bib.bib6 "The art of the scam: demystifying honeypots in ethereum smart contracts")); Sun et al. ([2024](https://arxiv.org/html/2602.14860v1#bib.bib7 "SoK: comprehensive analysis of rug pull causes, datasets, and detection tools in defi")).

This intertwining of economic behavior and contract design complicates the identification of meaningful predictors of success in decentralized token markets.
A central empirical challenge is therefore to determine which information, observable *in real time* during a token’s early life, is predictive of its future outcome.
This task is difficult for two fundamental reasons.
First, the base rate of success is extremely low, making ex-ante discrimination statistically challenging.
Second, even when manipulation is not the focus, the very definition of “success” is often ambiguous, as it typically requires fixing arbitrary time horizons or price thresholds.

A robust empirical analysis thus requires both (i) a controlled environment that limits heterogeneity unrelated to market dynamics and (ii) a non-arbitrary success criterion that is endogenous to the platform mechanism.

Pump.fun as a natural laboratory.
In this work we exploit Pump.fun Pump.fun ([2024](https://arxiv.org/html/2602.14860v1#bib.bib3 "Pump.fun: solana token launchpad")), a Solana-based launchpad whose design satisfies both requirements and provides an unusually clean stage to study the lifecycle of speculative crypto-assets.
Pump.fun enables the creation of a very large number of tokens every day, generating a high-throughput environment well suited for statistical analysis.
More importantly, the launch mechanism is fully standardized: all tokens are created under the same smart contract, share identical initial conditions, and trade along the same bonding-curve design.
This avoids weird contract-specific behavior, like honeypots or transfer limits, that can skew results on DEXs.

Beyond contract-level homogeneity, Pump.fun also embeds an endogenous and protocol-level notion of early success.
Each token begins trading on a virtual constant-product bonding curve that governs price formation and liquidity accumulation.
Graduation occurs deterministically once cumulative buy pressure pushes the bonding curve beyond a fixed threshold of bonded Solana, triggering migration to a real on-chain AMM pool.
During our sample period, this threshold corresponds to approximately 8585 SOL raised and a market capitalization of about $69,000.
Reaching this threshold does not guarantee long-run viability or economic value, but it certifies that the token has attracted sufficient coordinated demand to complete the launchpad phase.
Importantly, only a very small fraction of tokens reach graduation (about 0.63%0.63\% in our dataset), producing a sharp empirical separation between failures and successes.

From a methodological perspective, Pump.fun therefore functions as a large-scale experimental platform for observing the birth, evolution, and early termination of speculative assets.
Because most launches are not tied to informative fundamentals, outcomes are primarily driven by trader behavior, coordination, and attention dynamics, all of which are fully observable on-chain. On top of that, this ecosystem is mostly driven by meme tokens that are not backed by solid projects, where the creator main goal is often to make a quick return from the token they launched. That said, some tokens do try to raise funds to build something real, as shown by initiatives like Pump.fun new investment arm, Pump Fund, which aims to support projects. Dubey ([2026](https://arxiv.org/html/2602.14860v1#bib.bib27 "Pump.fun debuts new investment arm pump fund")).
The transparency of blockchain data further allows us to track individual trader addresses and to construct predictive signals based on trader composition and behavior, an approach that is rarely feasible in traditional financial markets.

These features make Pump.fun an ideal setting to investigate a central question in high-churn token markets: given the observable state of early trading activity, which signals are informative about a token likelihood of success?

The contribution of this work.
This paper provides a systematic and fully on-chain empirical analysis of early-stage token launches on bonding-curve-based platforms, using Pump.fun as a canonical and controlled case study.
Our main contribution is to frame the notion of early success in launchpad environments as a probabilistic object that can be monitored and updated in real time, based exclusively on information observable during a token launch phase.

Methodologically, we depart from project-specific or fundamental evaluations and instead treat graduation as a binary, protocol-defined outcome.
This allows us to construct a scalable framework in which the probability of success is estimated conditionally on the evolving state of the bonding curve and on a set of behavioral and microstructural variables.
The resulting graduation-probability curves provide an interpretable, time-consistent summary of how early trading dynamics shape outcomes in an environment characterized by extreme churn and very low base rates of success.

A first contribution is the identification of the amount of Solana accumulated in the bonding curve as a natural state variable summarizing collective demand.
We show that the conditional probability of graduation given the current bonding-curve state is monotone and converges smoothly to unity near the deterministic threshold.
This baseline curve serves as a real-time gauge of launch progress and establishes a natural breakeven against which additional information can be evaluated.

Second, exploiting the transparency of blockchain data, we go beyond aggregate liquidity measures and study how the *composition* of market participants affects graduation likelihood.
We introduce conditioning variables that capture (i) the intensity of bot-like or algorithmic trading activity, (ii) the speed at which liquidity is accumulated, measured by the number of trades required to reach a given bonding-curve level, (iii) the early participation of historically successful traders, and (iv) the identity and behavior of prolific token creators.
All conditioning variables are constructed in a strictly time-consistent manner, using only information available up to the current point on the bonding curve, ensuring a genuinely predictive interpretation.

Our empirical results highlight that not all paths to the same bonding-curve state are equivalent.
Fast accumulation of liquidity through a small number of trades is the strongest predictor of graduation, dominating other variables across the entire range of vSol.
In contrast, markets dominated by bot-like activity exhibit systematically lower graduation probabilities beyond intermediate stages, suggesting that high turnover and algorithmic trading do not translate into sustained capital commitment.
The presence of historically successful traders provides at most a modest and non-monotonic effect, reflecting the dual role of such agents in accelerating early discovery while often engaging in rapid exit strategies.

Third, we introduce an explicit economic breakeven that maps graduation probabilities into a minimal profitability condition under a deliberately naive buy-and-hold strategy.
Although not intended as a realistic trading rule, this breakeven provides an interpretable scale to assess whether the estimated probabilities are economically meaningful given the mechanical price dynamics imposed by the bonding curve.
By comparing conditional probability curves to this breakeven, we clarify which features of early trading behavior are not only statistically predictive, but also relevant from an economic perspective.

Finally, we document and rationalize systematic pump-and-dump behavior by token creators, showing how the transition from virtual to real liquidity at graduation induces incentives for pre-graduation liquidation.
This mechanism-level analysis highlights how design choices embedded in bonding-curve launchpads can shape strategic behavior and redistribute value, independently of project quality.

## II The Solana blockchain

Solana is a high-performance public blockchain designed to support fast and cheap transactions at large scale.
Although conceptually similar to Ethereum in that it enables programmable smart contracts and decentralized applications, its underlying architecture differs substantially in both consensus design and system optimization.

The key innovation of Solana lies in its consensus mechanism, known as Proof of History (PoH).
Unlike traditional blockchains such as Ethereum, which rely purely on Proof of Stake (PoS) or Proof of Work (PoW) to agree on the ordering of transactions, Solana introduces a verifiable cryptographic clock that provides a built-in notion of time.
Each validator maintains a continuous sequence of hash computations, where every hash depends on the previous one, forming a chain that proves the passage of time between events.
This allows the network to pre-order transactions before they are broadcast and validated, dramatically reducing coordination overhead among validators.

In practice, Proof of History operates in conjunction with a delegated Proof of Stake (dPoS) consensus layer.
Validators periodically produce blocks based on the PoH sequence, and their ordering can be verified without waiting for network-wide communication.
This hybrid design enables extremely high throughput (up to several tens of thousands of transactions per second) and sub-second block times, while maintaining decentralized validation and security guarantees.

In contrast, Ethereum, despite its transition to PoS in 2022, relies on a global consensus round for every block, requiring validators to agree on both block contents and ordering.
This process ensures strong consistency but limits scalability, with average block times of around 12 seconds and significantly lower throughput.

The architectural differences between Solana and Ethereum have major implications for application design.
Solana’s high-frequency block production and low latency make it particularly suitable for use cases involving rapid transaction sequences, micro-trades, and real-time state updates.
These features enable the emergence of platforms such as Pump.fun, where token creation, bonding curve evolution, and trading occur in seconds, driven by a continuous stream of on-chain interactions.

In the following section, we introduce the Pump.fun platform and describe how it leverages Solana’s unique performance characteristics to implement a fully on-chain launchpad mechanism based on bonding curves.

## III The Pump.fun platform

Pump.fun111See the official documentation at <https://pump.fun>. is a fully on-chain token launchpad built on the Solana blockchain, designed to automate the process of token creation, price discovery, and early trading through bonding-curve dynamics.
It provides a standardized framework in which any user can deploy a new token at minimal cost (of the order of a few dollars), while initial price formation and liquidity provisioning are entirely managed by smart contracts.
The platform design supports the simultaneous creation and trading of thousands of independent tokens, leveraging Solana’s high throughput and low latency for fast execution.

At its core, Pump.fun consists of two distinct and sequential automated market maker (AMM) environments, both based on a constant-product pricing rule in the spirit of Uniswap-like designs Adams et al. ([2020](https://arxiv.org/html/2602.14860v1#bib.bib1 "Uniswap v2 core")); Angeris and Chitra ([2020](https://arxiv.org/html/2602.14860v1#bib.bib10 "An analysis of constant function market makers")).
These environments differ in their economic interpretation and reserve structure, corresponding to a *virtual* and a *real* bonding-curve phase.
In both cases, prices are determined by a deterministic mapping between the reserves of the token and Solana, defined by the constant-product invariant governing market dynamics.

The first environment is a virtual AMM, which governs the early phase of each token lifecycle and implements the launchpad mechanism.
During this phase, trading takes place along a virtual bonding curve, described in detail below, which determines token prices algorithmically as a function of the cumulative amount of Solana committed by traders.
The bonding curve is initialized with protocol-defined virtual liquidity parameters and starts with zero real SOL reserves.
Once the total amount of Solana accumulated along the curve reaches a fixed threshold—known as the graduation point—the token exits the launchpad phase and migrates to the second environment.

The post-graduation phase takes place on a constant-product AMM with real reserves, PumpSwap.
Upon graduation, the protocol creates a canonical on-chain liquidity pool in which the graduated token acts as the base asset and the quote asset is Wrapped SOL (WSOL).
The migration procedure transfers the real SOL accumulated during the launchpad phase to the quote-token account of the PumpSwap pool, where it is wrapped into WSOL.
Importantly, only *real* reserves are migrated: the *virtual* reserves used during the bonding-curve phase are synthetic state variables employed solely for pricing and are not transferred on-chain.
As a result, the WSOL liquidity that seeds the PumpSwap pool is generated endogenously by traders’ purchases rather than by an upfront SOL deposit from the token creator.

This transition effectively converts a speculative, launchpad-based virtual market into a standard decentralized exchange environment based on a constant-product AMM with only real existing tokens.
After graduation, trading follows the same economic and microstructural principles as established DEXs such as Uniswap and Raydium, where liquidity provision, arbitrage, and price discovery emerge from interactions among heterogeneous market participants Adams et al. ([2020](https://arxiv.org/html/2602.14860v1#bib.bib1 "Uniswap v2 core")); Angeris and Chitra ([2020](https://arxiv.org/html/2602.14860v1#bib.bib10 "An analysis of constant function market makers")); Zhang et al. ([2020](https://arxiv.org/html/2602.14860v1#bib.bib11 "Formal foundations of automated market makers")); Capponi and Jia ([2022](https://arxiv.org/html/2602.14860v1#bib.bib13 "The adoption of decentralized exchanges")); Milionis et al. ([2022](https://arxiv.org/html/2602.14860v1#bib.bib14 "Automated market making and arbitrage")).

The following subsections describe in more detail the mechanisms underlying these two stages:
first, the Virtual AMM implemented by the Pump.fun launchpad, and second, the Real AMM called PumpSwap, where trading continues after graduation.

### Virtual AMM: Pump.fun Launchpad

The operational mechanism of the Pump.fun launchpad unfolds in the following stages. First, an initial supply of y0mint=109y^{\rm mint}\_{0}=10^{9} tokens is minted. This total supply is then divided into two parts:
y0virt,mint=0.7931×109y^{\rm virt,mint}\_{0}=0.7931\times 10^{9} tokens are allocated to the *virtual bonding curve*, while the remaining fraction y0pswap,mint=0.2069×109y^{\rm pswap,mint}\_{0}=0.2069\times 10^{9} is
reserved for a potential *graduation* into a Real PumpSwap AMM bonding curve. Note that the creator does not incur in any cost for the new token.

Subsequently, a *virtual AMM* is created, so named because its initial liquidity consists of both
virtual synthetic and real tokens. Specifically, the bonding curve is initialized with
x0synt=30x^{\rm synt}\_{0}=30 virtual synthetic tokens SOL, y0virt,mint=0.7931×109y^{\rm virt,mint}\_{0}=0.7931\times 10^{9} real tokens, and
y0synt=0.2799×109y^{\rm synt}\_{0}=0.2799\times 10^{9} virtual synthetic tokens.
Hence, the total initial liquidity state can be expressed as

|  |  |  |
| --- | --- | --- |
|  | x0tot,virt=x0synt=30​SOL,y0tot,virt=y0virt,mint+y0synt=1.073×109​tokens.x^{\text{tot,virt}}\_{0}=x^{\rm synt}\_{0}=30\ \text{SOL},\qquad y^{\text{tot,virt}}\_{0}=y^{\rm virt,mint}\_{0}+y^{\rm synt}\_{0}=1.073\times 10^{9}\ \text{tokens}. |  |

As other decentralized exchanges, this AMM works with a constant-product rule i.e. indicating the pool reserves at a generic time as (x,y)(x,y) it is always satisfied

|  |  |  |
| --- | --- | --- |
|  | x​y=k=x0tot,virt​y0tot,virt,x\,y=k=x\_{0}^{\rm tot,virt}y\_{0}^{\rm tot,virt}, |  |

so that the bonding curve is simply the set of points (x,y)(x,y) with the same invariant kk and the marginal price is P=x/yP=x/y. However, differently from other AMMs, during the virtual bonding curve phase liquidity cannot be added or removed with mint and burn actions and it is therefore always equal to kk.

The transaction fee is applied externally to the pool and is charged on each buy or sell swap.
Specifically, a fee equal to 1−r=f=1.25%1-r=f=1.25\% of the amount of exchanged SOL is collected.
In particular, the 0.3%0.3\% of the total amount is distributed to the token creator, while the remaining portion 0.95%0.95\% is collected by the Pump.fun protocol as a platform fee.
When a trader sends an amount Δ​x\Delta x of real SOL to the pool, only a fraction r​Δ​xr\Delta x effectively enters the bonding curve, after fees.
Given the invariant k=x0tot,virt​y0tot,virtk=x^{\rm tot,virt}\_{0}y^{\rm tot,virt}\_{0}, the new total SOL reserve is

|  |  |  |
| --- | --- | --- |
|  | xtot,virt=x0tot,virt+r​Δ​x,x^{\rm tot,virt}=x^{\rm tot,virt}\_{0}+r\Delta x, |  |

and the corresponding token reserve on the bonding curve is

|  |  |  |
| --- | --- | --- |
|  | ytot,virt=kxtot,virt.y^{\rm tot,virt}=\frac{k}{x^{\rm tot,virt}}. |  |

Hence, the number of tokens purchased and thus withdrawn from the pool is

|  |  |  |
| --- | --- | --- |
|  | Δ​y​(Δ​x)=y0tot,virt−ytot,virt=y0tot,virt−kx0tot,virt+r​Δ​x.\Delta y(\Delta x)=y^{\rm tot,virt}\_{0}-y^{\rm tot,virt}=y^{\rm tot,virt}\_{0}-\frac{k}{x^{\rm tot,virt}\_{0}+r\Delta x}. |  |

This relation defines the cumulative quantity of tokens issued as a function of the Solana deposited.

By definition, graduation occurs when the total reserve xtot,virtx^{\mathrm{tot,virt}} reaches 115115 SOL.
At that point, the transition to the real PumpSwap AMM takes place by creating a new, real bonding curve using the remaining
token supply y0pswap,minty^{\mathrm{pswap,mint}}\_{0} and the portion of real SOL x0pswapx\_{0}^{\rm pswap} from the virtual bonding curve, equal to 8585 SOL.
At the graduation point, the price remains continuous by construction, i.e.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 115​SOLy0synt≃85​SOLy0pswap,mint,\displaystyle\frac{115\,{\rm SOL}}{y^{\rm synt}\_{0}}\simeq\frac{85\,{\rm SOL}}{y^{\rm pswap,mint}\_{0}}\,\,, |  | (1) |

Up to minor transaction costs, the migration process also consumes a small portion of the real SOL reserves to cover
the *gas fee* required for the creation of the new AMM pool. This fee is deducted directly from the real SOL
balance accumulated within the virtual bonding curve.
Even though, the effective liquidity x​y\sqrt{x\,y} undergoes a discrete drop due to the
transition from virtual to real reserves.

### Real AMM: PumpSwap

Upon graduation, the token transitions to the real AMM, known as PumpSwap.
At this point, the system reclaims the 30 SOL virtual advance used to initialize the curve, effectively reducing the total SOL reserve from 115 SOL to 85 SOL.
Simultaneously, the token reserve decreases from its virtual synthetic total ysynty^{\rm synt} to ypswap,minty^{\rm pswap,mint} tokens, corresponding to the amount that would remain in the pool according to the bonding curve mechanics.
Importantly, the token price at the moment of transition, pgradp\_{\text{grad}}, remains constant by design to ensure a smooth migration between the virtual and real environments.

In the real phase, a liquidity pool is created in the PumpSwap AMM with the pair (85 SOL, 2.069×1082.069\times 10^{8} tokens), defining the initial market price:

|  |  |  |
| --- | --- | --- |
|  | pgrad=852.069×108.p\_{\text{grad}}=\frac{85}{2.069\times 10^{8}}. |  |

From this point onward, the token becomes fully tradable on-chain, and its price evolves freely according to the dynamics of the real PumpSwap AMM.
This second phase resembles a standard decentralized exchange, where liquidity providers and traders interact continuously, and price movements are determined by actual supply and demand.

The two-phase architecture of Pump.fun thus serves a dual purpose: the virtual AMM efficiently bootstraps liquidity and price discovery in a deterministic way, while the real PumpSwap AMM enables open trading under true market conditions.
This structure explains why Pump.fun can sustain a very high volume of token launches and rapid trading activity, a feature made possible by Solana low latency and high transaction throughput.

## IV The Dataset

The investigated dataset covers a one-month period, from September 1 to October 1, 2025, and includes only newly created tokens. During this time, a total of 655,770 tokens were created by 243,123 distinct token creator addresses. Among these, only 4,338 coins reached the graduation point, corresponding to a graduation frequency of approximately 0.63%. In total, 2,600,790 distinct trader addresses were recorded, although the effective number of unique users interacting with the platform is likely lower due to the use of multiple wallets per trader.

Data were collected directly from the Solana blockchain by parsing on-chain data from the Pump.fun and PumpSwap programs. This allowed us to track all newly created tokens across both the virtual and the real bonding curves. We retrieved and decoded all transaction events associated with token creation, bonding-curve interactions, and swap operations. On this launchpad system, i.e. on the virtual bonding-curve, adding and removing liquidity is not allowed by the protocol. Each transaction was mapped to its corresponding token launch, enabling the reconstruction of time-resolved bonding-curve states and the cumulative amount of SOL committed to each project. This approach ensures full transparency and reproducibility of the dataset, while accurately capturing the early trading and funding dynamics of the launchpad.

Each record in the dataset corresponds to a single on-chain transaction and includes the following core variables:

* •

  timestamp and local\_time: blockchain and local time of the transaction, used for temporal alignment and intra-block sequencing;
* •

  signature: unique transaction hash identifying each operation;
* •

  mint: token address associated with the launched token;
* •

  coin\_creator: address of the token creator;
* •

  trader: wallet address of the trader executing the transaction;
* •

  txType: categorical variable describing the transaction type (create, buy, sell);
* •

  inBondingCurve: boolean flag indicating whether the transaction occurred during the bonding curve phase;
* •

  vSolInBondingCurve and vTokInBondingCurve: current amounts of SOL and tokens locked in the virtual bonding curve just after the transaction;
* •

  solAmount and tokenAmount: quantities of SOL and tokens involved in the specific trade;
* •

  isBot: binary indicator (0/1) identifying bot-like activity, derived from log-level inspection of transaction sources.

Regarding the variable isBot, we extracted this information by looking at the logs of the transactions on the blockchain. Specifically, each transaction recorded on the Solana blockchain contains metadata about the calling program and the origin of the request.
By analyzing these logs, we distinguished between two cases: (i) transactions routed through the official Pump.fun graphical interface (a website), and (ii) transactions directly invoking the smart contract without passing through the platform’s frontend.
The former are typically associated with automated or scripted interactions, while the latter correspond to manual trades executed via the public user interface.
Accordingly, we assign isBot = 1 to transactions that directly interact with the contract (bypassing the interface) and isBot = 0 to those executed through dApp interfaces.
This classification allows us to isolate algorithmic or non-standard trading behaviors and assess their impact on the probability of graduation.

This structure provides both micro-level transactional granularity and macro-level aggregation possibilities, enabling the estimation of conditional graduation probabilities as a function of bonding curve dynamics and trader composition.

## V Descriptive statistics of the investigated dataset

![Refer to caption](x1.png)


Figure 1: On-chain trading activity in the PumpFun ecosystem during September 2025.
The top panel reports the daily number of newly created tokens.
The second panel shows the daily number of trades.
The third panel displays the average daily price of Solana (SOL) in USD.
The bottom panel reports the daily trading volume, expressed in million USD, computed from SOL-denominated volumes rescaled by the corresponding daily average SOL price.

This section provides an overview of the main aggregate properties of the market captured in our dataset, in order to illustrate its scale and overall activity.
Figure [1](https://arxiv.org/html/2602.14860v1#S5.F1 "Figure 1 ‣ V Descriptive statistics of the investigated dataset ‣ Predicting the success of new crypto-tokens: the Pump.fun case") provides an initial macroscopic view of the ecosystem during the observation month, summarising four dimensions of activity. From the top: daily tokens created, daily number of trades, average USD price of Solana, and daily USD-denominated trading volume.
The daily number of trades shows pronounced fluctuations, with activity ranging from roughly 2 to 5 million trades per day. From the figures, we observe an obvious positive correlations between the trade activity and the number of new tokens created.
The third panel indicates that the price of Solana remained comparatively stable throughout the period. The relative smoothness of the price trajectory suggests that variations in market activity are not primarily driven by exogenous price shocks.
The bottom panel shows that the daily volume dynamics broadly mirror those of the trade count, with particularly intense activity during the central part of the month, where several days exceed 600–700 million USD in exchanged value. After mid-month, the USD volume progressively decreased, stabilizing at significantly lower levels in the last week. The combination of somewhat stable SOL prices and sharply varying USD volume underscores that fluctuations in the Pump.fun ecosystem activity are predominantly driven by changes in trading intensity rather than price movements of Solana.
As explained above, a graduated token must reach a threshold of approximately 85​SOL85\,\mathrm{SOL} on its bonding curve. Considering the 4,3384{,}338 tokens that successfully graduated, this corresponds to a total net exchanged volume of

|  |  |  |
| --- | --- | --- |
|  | 85​SOL×4,338≃3.7×105​SOL≃7.4×107​USD,85\,\mathrm{SOL}\times 4{,}338\simeq 3.7\times 10^{5}\,\mathrm{SOL}\simeq 7.4\times 10^{7}\,\mathrm{USD}, |  |

where we consider only graduated tokens. To provide an aggregate, directly observable measure of the economic relevance of this ecosystem, we construct a market-level flow metric. Specifically, in Fig. [2](https://arxiv.org/html/2602.14860v1#S5.F2 "Figure 2 ‣ V Descriptive statistics of the investigated dataset ‣ Predicting the success of new crypto-tokens: the Pump.fun case") we compute the total net SOL cash flow generated by all newly created tokens over the month, accounting both for the bonding-curve phase on Pump.fun and for the post-graduation trading on AMMs. This quantity captures how much SOL is, on net, absorbed and retained by the Pump.fun token market over the sample period, and thus offers a simple proxy for the scale and importance of this segment of on-chain activity.

![Refer to caption](x2.png)


Figure 2: Cumulative signed amount value of Solana (vSol) circulating through all newly created tokens during September 2025, including both bonding curve and post-graduation AMM activity.

At the end of September, this cumulative value reached approximately 1.6×1051.6\times 10^{5} SOL ≃3.2×107\simeq 3.2\times 10^{7} $, which can be interpreted as the residual amount of Solana effectively created and remaining within the system at the end of the observation period.
This measure therefore captures the aggregate liquidity that continues to exist within the system, integrating both pre- and post-graduation dynamics. We also note that this aggregate net flow is of the same order of magnitude as the SOL that can be transferred into canonical AMM liquidity at graduation. This pattern may be related to post-graduation persistence: a subset of graduated tokens remains actively traded over time and, since liquidity-pool creation on Solana AMMs is permissionless, additional pools may be created on other DEX venues beyond the canonical post-graduation market. In the most extreme cases, sufficiently popular tokens are also listed on centralized exchanges (e.g., from Pump.Fun all data history: POPCAT on Binance.US; GOAT via Binance futures; PNUT on major CEXs such as Gate and OKX).

![Refer to caption](x3.png)


Figure 3: Empirical survival curve of bonding-curve progress.
For each threshold of SOL in bonding curve, we report the number of newly created tokens reaching that amount.
The ordinate is shown on a logarithmic scale, highlighting the rapid drop-off in the fraction of tokens that accumulate large amounts of SOL along the bonding curve.

Beyond aggregate liquidity, it is also interesting to quantify how stalling tokens progress along the bonding curve before graduation (see Figure [3](https://arxiv.org/html/2602.14860v1#S5.F3 "Figure 3 ‣ V Descriptive statistics of the investigated dataset ‣ Predicting the success of new crypto-tokens: the Pump.fun case"))
For each level of vSol in the bonding curve, we count how many tokens ever reach at least that value during their lifetime.
The resulting curve is monotonically decreasing by construction and displays a steep decay: while a large mass of tokens reaches only low vSol levels, only a tiny fraction approaches the upper part of the curve near the graduation region.
On the logarithmic scale, the approximately linear behavior over an intermediate range suggests a fast, nearly exponential drop in the probability of reaching higher capital thresholds, consistent with a strong selection effect in early trading and funding dynamics.

The two upper panels in Figure [4](https://arxiv.org/html/2602.14860v1#S5.F4 "Figure 4 ‣ V Descriptive statistics of the investigated dataset ‣ Predicting the success of new crypto-tokens: the Pump.fun case") report information on the steps and the time tokens that are usually required to graduate. The top left panel reports the empirical distribution of graduation steps, i.e. the number of on-chain bonding-curve updates (swaps/events) required for a token to reach the graduation threshold. In fact, on the Pump.fun launchpad, the only event , which drives measurable market changes, is the swap event.
The distribution is strongly right-skewed: most tokens graduate after a relatively small number of steps, while a long tail extends to several thousand steps.
The vertical dashed line marks the median, ≃457\simeq 457 steps, indicating that half of the graduated tokens reach migration within a few hundred bonding-curve events.

The top right panel shows the corresponding distribution of time-to-graduation, measured in minutes from token creation to the graduation transaction.
Also in this case the distribution exhibits a pronounced heavy tail: the bulk of graduations occurs very rapidly, whereas a minority of tokens requires tens of minutes to migrate.
The median time to graduation is ≃4.4\simeq 4.4 minutes (dashed line), highlighting the high-frequency and strongly momentum-driven nature of successful launches on Pump.fun.

The bottom-left panel shows that only a small fraction of the total number of tokens actually reaches the graduation threshold and migrates to the real PumpSwap AMM pool.
Specifically, the curve reports the normalized fraction of tokens whose bonding-curve trajectory exceeds a given value of vSol.
The sharp decay highlights that the vast majority of tokens stalls at relatively low levels of accumulated Solana, while only about 0.6%0.6\% of all launched tokens manage to graduate.

The bottom-right panel provides a joint view of the graduation process by displaying the empirical density of tokens in the plane defined by time to graduation and number of graduation steps.
Color intensity encodes the number of tokens in each bin on a logarithmic scale.
The plot reveals a strong concentration of mass at short times and low step counts, indicating that most successful tokens graduate very quickly and with relatively few bonding-curve interactions.
At the same time, a broad and sparse tail extends toward longer times and larger numbers of steps, reflecting heterogeneous and less efficient paths to graduation for a minority of tokens.

![Refer to caption](x4.png)


Figure 4: 
Graduation dynamics of Pump.fun tokens across multiple dimensions.
Top left: Empirical distribution of the number of bonding-curve steps required to reach graduation.
Top right: Empirical distribution of time to graduation (in minutes) from token creation.
Both distributions are strongly right-skewed, with medians of approximately 457457 steps and 4.44.4 minutes, respectively (dashed lines).
Bottom left: Normalized fraction of tokens whose maximum bonding-curve state exceeds a given value of vSol, showing that only a small fraction of launched tokens reaches the graduation region and migrates to the real PumpSwap AMM pool.
Bottom right: Joint distribution of graduation steps and time to graduation, with color intensity indicating the number of tokens on a logarithmic scale.
The concentration of mass at short times and low step counts highlights the fast and momentum-driven nature of successful launches, while the sparse tail reflects heterogeneous and less efficient paths to graduation.

## VI Conditional graduation probability

![Refer to caption](x5.png)


Figure 5: Empirical probability of graduation as a function of the virtual Solana threshold (vSol).
The solid line (pstdp\_{\mathrm{std}}) reports the baseline estimator P​(grad​∣∃x:x>​v​S​o​l)P(\mathrm{grad}\mid\exists\,x:x>vSol).
The dashed line (pstdt>2p\_{\mathrm{std}}^{t>2}) shows the same probability after excluding ultra-fast graduations with time to graduation shorter than two seconds.
Light-blue bars (pbin,jp\_{\mathrm{bin},j}) display a non-parametric binned estimate over intervals of width 55 SOL.
The close agreement between the curves indicates that extremely rapid, likely bot-driven events do not materially affect the graduation-probability profile, while the monotonic increase reflects the deterministic progression of tokens along the bonding curve toward the graduation threshold.

In the following, we exploit this structure to study how the probability of graduation evolves as a function of information that is observable in real time during a token’s launch phase.

As a first step, we focus on the most natural state variable of the launch mechanism itself: the amount of Solana currently locked in the bonding curve.
We therefore begin by estimating the probability of graduation conditional on the current level of virtual Solana (vSol), before moving on to richer conditioning sets that capture additional dimensions of trading behavior and agent composition.

We estimate this probability empirically by computing, for each level of vSol observed across all tokens, the fraction of coins that ultimately graduate.
More precisely, for any threshold on the bonding curve, we consider the set of tokens that have reached at least vSol at some point in their life cycle and measure the proportion of those that eventually graduate.
The resulting conditional probabilities are reported in Fig. [5](https://arxiv.org/html/2602.14860v1#S6.F5 "Figure 5 ‣ VI Conditional graduation probability ‣ Predicting the success of new crypto-tokens: the Pump.fun case").

The solid blue curve represents our baseline estimator,

|  |  |  |
| --- | --- | --- |
|  | pstd​(v​S​o​l)=P​(grad​∣∃x:x>​v​S​o​l),p\_{\mathrm{std}}(vSol)=P\bigl(\mathrm{grad}\mid\exists\,x:x>vSol\bigr), |  |

namely the probability that a token eventually graduates conditional on having crossed a given vSol level.
This quantity provides a smooth, global characterization of how the likelihood of graduation increases as more Solana is accumulated along the bonding curve, and it will serve as the reference object throughout the remainder of the paper.

The dashed orange curve reports the same conditional probability after excluding extremely fast graduations, defined as events with a total time to graduation shorter than two seconds:

|  |  |  |
| --- | --- | --- |
|  | pstdt>2​(v​S​o​l)=P​(grad​∣∃x:x>​v​S​o​l,tgrad>2​s).p\_{\mathrm{std}}^{t>2}(vSol)=P\bigl(\mathrm{grad}\mid\exists\,x:x>vSol,\;t\_{\mathrm{grad}}>2~\mathrm{s}\bigr). |  |

This filter removes ultra-fast events that are likely driven by automated bots or anomalous bursts of activity.
The close alignment between pstdt>2p\_{\mathrm{std}}^{t>2} and pstdp\_{\mathrm{std}} indicates that such events do not materially affect the shape of the graduation-probability curve, supporting the robustness of the baseline estimator.

For completeness, the light-blue bars report a non-parametric binned estimate of the same probability.
For each interval [v​S​o​l,v​S​o​l+5)[vSol,vSol+5) of width 5 SOL, we compute the fraction of tokens that graduate among those whose bonding-curve trajectory enters that bin.
This discretized representation provides a direct view of the underlying empirical frequencies and visually encodes the local statistical support, complementing the smoother baseline curve.

As expected, all estimators display a monotonically increasing probability of graduation as vSol grows, with values approaching one near 115115 SOL.
This level corresponds to the effective graduation threshold, consisting of 3030 virtual SOL (initialized at creation) and 8585 real SOL deposited by traders.
Once the bonding curve accumulates this total amount, graduation becomes virtually guaranteed and the empirical probabilities converge to unity.

In the remainder of the paper, we use pstd​(v​S​o​l)p\_{\mathrm{std}}(vSol) as the breakeven graduation-probability curve and study how it shifts when conditioning on additional variables capturing trading intensity, agent composition, and behavioral heterogeneity.

However, the predictive information contained in vSol alone is limited: tokens with similar vSol values may exhibit very different outcomes depending on behavioral and structural factors that are not captured by aggregate capital accumulation.
This motivates the introduction of additional conditioning variables, aimed at disentangling how trading intensity, agent composition, and participation patterns affect the likelihood of graduation.

Before turning to these richer conditioning sets, it is useful to place the graduation-probability curves in an explicitly economic perspective.
In particular, one may ask whether the empirical probabilities we estimate are large enough to be economically meaningful for a trader facing the mechanical price dynamics implied by the bonding-curve design.
To this end, we first introduce a simple breakeven that maps graduation probabilities into a minimal profitability condition under a naive buy-and-hold strategy.
This breakeven provides a transparent reference scale against which the magnitude and relevance of the estimated probabilities can be assessed.

### An economic breakeven curve

The conditional graduation-probability curves introduced above naturally raise the question of whether such information can be exploited in an economically meaningful way.
Rather than proposing a realistic or optimized trading strategy, we use a deliberately simple breakeven to translate graduation probabilities into a minimal profitability condition.
This exercise serves as a sanity check: it allows us to assess whether the empirical likelihood of graduation is, in principle, strong enough to compensate for the mechanical price dynamics implied by the bonding-curve design.

Specifically, imagine that by considering additional features θ\theta, we estimate the graduation probability p​(v​S​o​l;θ)p(vSol;\theta) which depends also on the current v​S​o​lvSol and hence on the price v​S​o​l2/kvSol^{2}/k. We consider a simple buy-and-hold trading strategy where we buy a given token when v​S​o​lvSol first reaches a chosen threshold (corresponding to the candidate xx-axis entry points in the figures), and we sell only at graduation, i.e., when v​S​o​l=115vSol=115 and the price is 1152/k115^{2}/k.
If the token never reaches graduation, we never sell (the position remains open) and we lose our investment222Throughout, we ignore gas costs as well as protocol and creator fees, which are negligible under the small-fee approximation f=0.0125≪1f=0.0125\ll 1. . The expected simple return rr of the strategy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[r|vSol;θ]=(1152kkv​S​o​l2−1)p(vSol;θ)+(0−1)(1−p(vSol;θ)).\displaystyle{\mathbb{E}}[r|vSol;\theta]=\Biggl(\frac{115^{2}}{k}\frac{k}{vSol^{2}}-1\Biggl)p(vSol;\theta)+(0-1)\Bigl(1-p(vSol;\theta)\Bigl)\,\,. |  | (2) |

The strategy is economically profitable if 𝔼​[r|v​S​o​l;θ]>0{\mathbb{E}}[r|vSol;\theta]>0 hence if

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(v​S​o​l;θ)>v​S​o​l21152.\displaystyle p(vSol;\theta)>\frac{vSol^{2}}{115^{2}}\,\,. |  | (3) |

Thus, if the conditional graduation probability curve p​(v​S​o​l;θ)p(vSol;\theta) lies above the parabolic boundary v​S​o​l2/1152{vSol^{2}}/{115^{2}}, the naive buy-and-hold strategy based on it delivers a positive expected profit (under the same cost assumptions). We call the curve p=v​S​o​l2/1152p={vSol^{2}}/{115^{2}} as the breakeven curve. It is important to stress that this is the breakeven curve only for buy-and-hold strategies. In other words, it might be possible to devise dynamic strategies delivering positive expected profits also when the conditional probability lies below the breakeven curve. When there are no additional features p​(v​S​o​l;θ)=ps​t​d​(v​S​o​l)p(vSol;\theta)=p\_{std}(vSol). As shown below (see for example Fig. [6](https://arxiv.org/html/2602.14860v1#S7.F6 "Figure 6 ‣ Conditioning on the share of bot-like activity ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case")) ps​t​d​(v​S​o​l)p\_{std}(vSol) lies below the breakeven curve, hence it is not possible to make profits with a buy-and-hold strategy based only on v​S​o​lvSol (or the price).

In the next section, we will systematically compare the empirically estimated graduation-probability curves with this breakeven boundary in order to quantify how different conditioning variables θ\theta shift the probability mass relative to the profitability threshold.

## VII Prediction variables

We consider four main variables that capture distinct aspects of market behavior and participant profiles and might be useful in improving success prediction:

* •

  Bot activity (isBot): a binary indicator identifying transactions associated with algorithmic trading accounts.
  Conditioning on this variable reveals whether coins traded primarily by bots are more or less likely to graduate for a given vSol.
* •

  Number of trades: the cumulative number of transactions recorded for a token up to a given vSol.
  This variable proxies market activity and engagement, allowing us to evaluate whether a higher trading frequency increases the probability of graduation.
* •

  Presence of successful traders: a categorical variable marking whether at least one wallet that achieved high profits during the month has traded the token.
  Conditioning on this variable helps assessing whether the involvement of successful or possibly informed traders correlates with higher graduation chances.
* •

  Top token creators: an indicator for whether the token was issued by one of the most prolific creators, defined as those who launched the largest number of tokens in the observation period.
  This conditioning captures potential experience or network effects among frequent creators.

Each of these variables is used to compute a new conditional graduation probability curve, estimated in the same way as the baseline in Figure [5](https://arxiv.org/html/2602.14860v1#S6.F5 "Figure 5 ‣ VI Conditional graduation probability ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
In the following subsections, we compare these curves to the baseline case and discuss how the inclusion of each conditioning variable modifies the probability landscape, thereby improving the predictive understanding of graduation events.

### Conditioning on the share of bot-like activity

A key dimension of heterogeneity in the Pump.fun market concerns the distinction between algorithmic and manual trading behavior.
To capture this aspect, we define the variable isBot as a binary indicator (0/1) identifying bot-like activity, derived from log-level inspection of transaction sources.
Specifically, each transaction on the Solana blockchain contains metadata about the calling program and the origin of the request.
By analyzing these logs, we distinguished between transactions routed through the official Pump.fun frontend (the website) and those directly invoking the smart contract on-chain.
The latter interactions, which bypass the graphical interface, are typically associated with automated or scripted trading behavior.
Accordingly, we assign isBot = 1 to direct on-chain calls and isBot = 0 to transactions executed via the Pump.fun website.

In this analysis, rather than conditioning on individual transactions, we aggregate information at the token level.
For each token, we compute the fraction of trades executed by addresses flagged as isBot = 1 and use this quantity as a proxy for the presence of automated or sophisticated trading activity.
We then partition tokens into two groups depending on whether their bot share exceeds a given threshold, distinguishing markets with a high prevalence of bot-like activity from those dominated by non-automated, retail-like traders.

Formally, let τ\tau denote the fraction of non bot-initiated trades for a given token, and let θ\theta be a chosen threshold.
We define the conditional graduation probability

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ​(vSol)=P​(grad​∣τ>​θ),p\_{\theta}(\mathrm{vSol})=P\bigl(\mathrm{grad}\mid\tau>\theta\bigr), |  | (4) |

that is, the probability of graduation conditional on the token exhibiting a non bot share above θ\theta. In other words, the threshold θ\theta represents a lower bound on the fraction of non sophisticated traders acting on the considered tokens.

Crucially, in order to preserve a causal and predictive interpretation, the non bot-share τ\tau is computed using only trades that occurred up to the current level of vSol on the bonding curve.

In other words, at each value of accumulated Solana, the conditioning variable is constructed exclusively from information that would have been observable to an external agent at that point in time.
This ensures that the resulting conditional probability curves capture genuine predictive content rather than ex-post correlations driven by future trading activity.

![Refer to caption](x6.png)

![Refer to caption](x7.png)

Figure 6: The top panel shows the graduation probability as a function of the bonding-curve state variable vSol, conditional on the intensity of non bot-like trading activity.
The solid blue line (pstdp\_{\mathrm{std}}) reports the baseline graduation probability.
The solid and dashed brown lines show the conditional probabilities for tokens with a share of non-bot-attributed trades above 0.30.3 and 0.70.7, respectively.
The black dashed line represents the breakeven profitability boundary derived from the naive entry-and-hold strategy.
Curves lying above the breakeven indicate regions in which the implied graduation probability is sufficient to offset the mechanical price increase along the bonding curve, yielding non-negative expected returns under the breakeven assumptions.
The bottom panel shows the mean bot rate as a a function of the price level. This serves as a motivation for choosing the extreme bot-probability values of 0.3 and 0.7.

Figure [6](https://arxiv.org/html/2602.14860v1#S7.F6 "Figure 6 ‣ Conditioning on the share of bot-like activity ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case") compares the baseline graduation-probability curve pstdp\_{\mathrm{std}} with conditional curves obtained by partitioning tokens according to the share of bot-initiated trades.
Specifically, we consider two thresholds for the minimum presence of non-sophisticated traders, namely θ=0.3\theta=0.3 and θ=0.7\theta=0.7. We choose these extreme values because the average non-bot rate in our data lies between them; moving further away would not materially affect the implied probabilities, since only a small fraction of coins fall more than one standard deviation from the mean (see bottom plot in Fig. [6](https://arxiv.org/html/2602.14860v1#S7.F6 "Figure 6 ‣ Conditioning on the share of bot-like activity ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case")).
This means that we condition the graduation probability on tokens that, upon reaching a given SOL threshold on the bonding curve, exhibit at least 30%30\% of non-sophisticated traders (i.e. at most 70%70\% bot activity) and, respectively, at least 70%70\% of non-sophisticated traders (i.e. at most 30%30\% bot activity).
For reference, the dashed line reports the economic breakeven curve derived from the naive buy-and-hold strategy.

What emerges from the analysis is that both conditional curves lie systematically above the pstdp\_{\rm std} curve. This indicates that incorporating information on the composition of traders participating in the price-formation process is highly informative.
In particular, the results suggest that a large participation of non-sophisticated traders is associated with an increased likelihood of reaching graduation.
A plausible interpretation is that sophisticated traders, including token creators, often engage in short-horizon strategies such as pump-and-dump schemes—which we analyze in detail in a later section—that tend to accelerate the depletion of liquidity and contribute to an early termination of the token lifecycle. We also stress that the two conditional graduation-probability curves, associated with the two different values of θ\theta, become statistically similar. Beyond that range, increasing the share of non-bot traders does not materially change the predicted probability: the signal carried by the non-bot percentage is essentially exhausted at high non-bot presence.
Finally, we observe that all conditional graduation-probability curves remain below the economic breakeven over most of the vSol range, with the notable exception of the p0.3p\_{0.3} curve, which approaches the breakeven in the vicinity of the graduation threshold.
It should be emphasized that this comparison is purely qualitative.
The breakeven curve is derived from a deliberately naive buy-and-hold strategy and relies on strong simplifying assumptions, in particular the neglect of protocol, creator, and gas fees, which are assumed to be negligible.
As a result, the purpose of this exercise is not to assess realistic profitability, but rather to provide an interpretable reference scale against which the magnitude of the estimated graduation probabilities can be evaluated.

### Conditioning on trading intensity

Another relevant dimension affecting the likelihood of graduation is the intensity of trading activity prior to reaching a given level of Solana on the bonding curve.
The same value of vSol can be attained either through a single large transaction or via many small, possibly alternating trades.
To disentangle these effects, we condition the graduation probability on the cumulative number of swaps observed *up to the moment a given vSol threshold is first reached*.
This construction is strictly causal: at each point along the bonding curve, the conditioning variable depends only on past information and therefore preserves a genuinely predictive interpretation.
We consider five increasing thresholds for trading activity (10, 50, 100, 500, and 1000 swaps).
For each threshold NN, we estimate the probability of graduation conditional on having reached a given vSol level with at most NN trades.
The left panel of Fig. [7](https://arxiv.org/html/2602.14860v1#S7.F7 "Figure 7 ‣ Conditioning on trading intensity ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case") displays the resulting conditional probability curves.
A clear monotonic pattern emerges: for any fixed vSol, tokens that reach that level with fewer trades exhibit substantially higher graduation probabilities.
In particular, rapid accumulation of liquidity within the first few tens of transactions produces graduation probabilities that lie well above the baseline curve conditioned only on vSol.
Conversely, when hundreds or thousands of trades are required to reach the same amount of Solana, the graduation probability flattens and converges toward the baseline, indicating that slow and fragmented trading activity is markedly less conducive to success.

![Refer to caption](x8.png)

![Refer to caption](x9.png)

Figure 7: 
Graduation probability conditional on the bonding-curve state variable vSol and on the cumulative number of swaps required to reach that level.
Curves correspond to upper bounds of 10, 50, 100, 500, and 1000 trades.
Left panel: full sample.
Right panel: same analysis after imposing a minimum of 10 trades, excluding near-instant graduation events.

A potential concern is that the strong uplift observed at low vSol might be mechanically driven by tokens that graduate almost instantaneously, following only a handful of very large early trades.
Such ultra-fast events, while statistically influential, are economically uninformative and generally not exploitable in practice.

To address this issue, the right panel of Fig. [7](https://arxiv.org/html/2602.14860v1#S7.F7 "Figure 7 ‣ Conditioning on trading intensity ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case") repeats the same analysis after imposing a lower bound of 10 trades, thereby excluding tokens that graduate immediately.
While this filtering naturally raises the estimated probabilities, the qualitative ordering of the curves is preserved across the entire bonding-curve range.
Crucially, even after removing these near-instant graduations, tokens characterized by fast liquidity accumulation continue to dominate in terms of graduation likelihood.

Taken together, these results indicate that not only the amount of capital committed matters, but also the *speed* at which it is deployed.
Successful tokens are characterized by strong early momentum, where liquidity concentrates rapidly in a small number of trades.
In contrast, prolonged accumulation through many small transactions typically signals weak collective engagement and frequently precedes stagnation.
In this sense, liquidity velocity emerges as the single most informative predictor of graduation among all variables considered in this study.

### Conditioning on successful traders

One of the key peculiarities of blockchain-based markets is their inherent transparency.
Because all transactions are publicly observable, it is possible to track which wallets have achieved higher profitability over time and to analyze the trading strategies associated with those addresses.
This feature enables an entire class of trading strategies based on imitation, whereby agents condition their actions on the observed behavior and past performance of other traders.
In this setting, wallet-level performance becomes an informative signal, allowing market participants to infer and potentially replicate the strategies of more successful traders.

To exploit this feature in a predictive and causally interpretable way, we split our observation window into two consecutive subperiods of two weeks each.
We use the first subperiod to identify a set of top-performing traders based exclusively on their realized profits, measured in Solana, from closing positions during that period.
Specifically, we track wallets that have accumulated the largest net amounts of SOL from selling their positions, thereby constructing an ex-ante list of traders that can be classified as “successful” according to past performance.
The second subperiod is then used to study whether the participation of these ex-ante identified top traders provides predictive information about the probability of graduation for newly launched tokens.
Crucially, the set of top traders is fixed before the beginning of the second subperiod and does not depend on any trading activity occurring thereafter.
This temporal separation ensures that the conditioning variable is constructed independently of future outcomes and allows for a genuinely causal interpretation in the sense of out-of-sample prediction.
Table [1](https://arxiv.org/html/2602.14860v1#S7.T1 "Table 1 ‣ Conditioning on successful traders ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case") reports the list of top traders identified in the first subperiod, together with the total amount of Solana received after closing their positions, the number of trades, and the breakdown between buy and sell transactions.
Interestingly, several of these wallets exhibit an extreme asymmetry in their trading behavior, having executed only sell transactions.
This pattern suggests that such wallets may act as liquidity exit points, receiving funds that were originally accumulated across multiple addresses through intermediate transfers, possibly as part of coordinated profit-taking or aggregation strategies.

Table 1: Top trader wallets ranked by PnL (SOL): comparison between the full monthly dataset and the first two weeks.

(a) Full dataset

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rank | Wallet | PnL (SOL) | #Trades | #Buy | #Sell |
| 1 | 5JewENBbfKu23TLEhfXxzL4VRHwJvcLf9BCPHAuB5Rmh | 9373.141 | 1793 | 0 | 1793 |
| 2 | niggerd597QYedtvjQDVHZTCCGyJrwHNm2i49dkm5zS | 3681.430 | 4028 | 596 | 3432 |
| 3 | GsbjKVpmusptbt5RwwQ6z7P4cEVhqXbhRMHPwQ4hfRp4 | 3622.959 | 905 | 754 | 151 |
| 4 | suqh5sHtr8HyJ7q8scBimULPkPpA557prMG47xCHQfK | 3208.460 | 19103 | 13486 | 5617 |
| 5 | CeAjiFBzgNb2oBM2v3nG8u8QnmLhtS1SiRJwqVPaSwqK | 3194.397 | 632 | 0 | 632 |
| 6 | 24oimYpYTiChCRHXRkNZNqw5mEE6X8RWFEWXrsVLM8PP | 2856.466 | 48 | 25 | 23 |
| 7 | Dsi8ntQziuCPt16TStjG4tgviracSryHsRcH72zbwRgu | 2687.453 | 116503 | 57849 | 58654 |
| 8 | 5sNnKuWKUtZkdC1eFNyqz3XHpNoCRQ1D1DfHcNHMV7gn | 2515.810 | 4723 | 1744 | 2979 |
| 9 | 2ErKM3aVUjuvGhRVvYzeq6VHxqjyT9Q4P4D6xioCRZxU | 2499.163 | 520 | 0 | 520 |
| 10 | 2ezv4U5HmPpkt2xLsKnw1FyyGmjFBeW7c166p99Hw2xB | 2493.568 | 66109 | 30259 | 35850 |
| Best wallet: 5JewENBbfKu23TLEhfXxzL4VRHwJvcLf9BCPHAuB5Rmh | | | | | |
| --- | --- | --- | --- | --- | --- |
| Expected profit: $1,874,628.30  (200 $/SOL) | | | | | |

(b) First two weeks of the dataset

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rank | Wallet | PnL (SOL) | #Trades | #Buy | #Sell |
| 1 | GsbjKVpmusptbt5RwwQ6z7P4cEVhqXbhRMHPwQ4hfRp4 | 3017.655 | 476 | 415 | 61 |
| 2 | 24oimYpYTiChCRHXRkNZNqw5mEE6X8RWFEWXrsVLM8PP | 2845.029 | 45 | 24 | 21 |
| 3 | suqh5sHtr8HyJ7q8scBimULPkPpA557prMG47xCHQfK | 2634.320 | 15220 | 10782 | 4438 |
| 4 | CeAjiFBzgNb2oBM2v3nG8u8QnmLhtS1SiRJwqVPaSwqK | 2512.679 | 493 | 0 | 493 |
| 5 | niggerd597QYedtvjQDVHZTCCGyJrwHNm2i49dkm5zS | 2492.898 | 1948 | 364 | 1584 |
| 6 | jECNQy2tSeA9pZpq54eVE7WWEGSeZHpeJ1sj2RsxoR1 | 2441.683 | 101 | 1 | 100 |
| 7 | 5JewENBbfKu23TLEhfXxzL4VRHwJvcLf9BCPHAuB5Rmh | 2247.917 | 568 | 0 | 568 |
| 8 | Ho7pNj4ABqrVzdsN34aVPyHQ27eGbWMQHhnDp6QTFHW5 | 2002.581 | 61 | 35 | 26 |
| 9 | j1oAbxxiDUWvoHxEDhWE7THLjEkDQW2cSHYn2vttxTF | 1875.038 | 5111 | 1733 | 3378 |
| 10 | Dsi8ntQziuCPt16TStjG4tgviracSryHsRcH72zbwRgu | 1835.249 | 70672 | 35030 | 35642 |
| Best wallet: GsbjKVpmusptbt5RwwQ6z7P4cEVhqXbhRMHPwQ4hfRp4 | | | | | |
| --- | --- | --- | --- | --- | --- |
| Expected profit: $603,531.00  (200 $/SOL) | | | | | |

![Refer to caption](x10.png)


Figure 8: Graduation probability conditional on vSol and on the presence of at least one trade by a top successful trader before the corresponding Solana threshold in the bonding curve.

In Figure [8](https://arxiv.org/html/2602.14860v1#S7.F8 "Figure 8 ‣ Conditioning on successful traders ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case"), we condition the graduation probability on the occurrence of at least one trade executed by a trader belonging to this ex-ante defined set of top-performing wallets before a given level of vSol is reached.
The conditioning variable is constructed in a time-consistent manner: for each value of vSol, we only consider trades that occurred up to that point along the bonding curve and only within the second subperiod.
As a result, both the identification of top traders and the conditioning itself rely solely on information that would have been available to an observer in real time. Under this construction, the analysis admits a genuinely predictive interpretation.
The presence of a top trader should therefore be understood not as an ex-post correlate of success, but as an ex-ante signal reflecting the early involvement of agents who have demonstrated superior performance in the recent past.

The resulting conditional graduation-probability curve lies above the baseline probability conditioned only on vSol, indicating that the early participation of ex-ante identified top traders is associated with a higher likelihood of graduation. This indicates that some traders are able to take advantage of the this graduation mechanism and, therefore, they insert information in the market.

Note that, however, the two curves still are below the breakeven curve. Meaning that using a simple buy and hold strategy gaining would be unlikely. This is surely due, in part, to the simplicity of the strategy. However, it is also important to consider that the effect of top traders usually reflects two opposing mechanisms.
On the one hand, early entry by experienced traders may accelerate initial liquidity accumulation and help coordinate early demand.
On the other hand, these same traders tend to exit positions rapidly, often around salient events such as graduation, thereby limiting the sustained buying pressure required to complete the launchpad phase.
Overall, the presence of top traders emerges as a double-edged signal: it conveys information about informed participation, yet it may also coincide with opportunistic behavior that constrains the long-run stability of the bonding curve.

### Conditioning with respect top token creators

Another important dimension for understanding the lifecycle of newly issued tokens concerns the identity and behavior of their creators.
Token creators represent a relatively new class of market participants that has emerged with the advent of low-cost, high-throughput launchpad platforms such as Pump.fun.
These platforms drastically reduce the cost of token creation, enabling a single address to deploy a very large number of tokens within a short time span.
Creators do not merely influence the market by increasing the supply of new assets.
They can also actively shape the subsequent evolution of the tokens they issue by participating directly in trading activity after creation.
In particular, creators enjoy a structural advantage in timing, as they are able to interact with the token immediately upon deployment and can therefore be among the earliest buyers.
This early access potentially allows creators to influence price dynamics during the most fragile phase of the token’s lifecycle, when liquidity is still thin and coordination effects are strongest.

At the same time, the design of Pump.fun imposes important constraints on creator behavior.
Unlike many decentralized exchange environments, creators cannot directly extract value through liquidity-removal mechanisms such as rug pulls.
All liquidity is managed by the protocol, and creators have no privileged control over the pool.
As a result, creators can affect the market only through standard trading actions, such as buying and selling the token along the bonding curve.
This restriction isolates a well-defined class of strategic behaviors, most notably pump-and-dump strategies, that operate purely through trading rather than through contract-level manipulation. These features make creator activity particularly informative for studying early token dynamics.

![Refer to caption](x11.png)


Figure 9:

As we did in the last section with successful traders, we investigate the predictive information contained in successful token creators. Table [2](https://arxiv.org/html/2602.14860v1#S7.T2 "Table 2 ‣ Conditioning with respect top token creators ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case") reports the top 10 token creators in the month of September, some of whom issued more than 2,000 tokens within a single month. This role is further incentivized by the platform, contributing to its dominance among existing launchpads, as it grants token creators a share of the fees generated by swaps involving their own tokens. Specifically, creators receive a 0.3% fee during the virtual AMM phase, and a dynamic fee in the real PumpSwap AMM phase that ranges from 0.950% down to 0.050% as the amount of SOL locked in the bonding curve continues to increase.

| Rank | Creator | Ratio | NgradN\_{\rm grad} | NtotN\_{\rm tot} |
| --- | --- | --- | --- | --- |
| 1 | CeZbzsqje88U7GCCrAiGUr5BrZrBJ3AkQMyG9aggDiqQ | 0.084 | 9 | 107 |
| 2 | HyRzY2SNzGSFvhJkCepj6DRtR3LaHCSyNKJ4HMYktbU4 | 0.058 | 3 | 52 |
| 3 | ESBjYRXRkYUCqoY54V6AB3BXvNW4P37bBhgutfPejJ2X | 0.050 | 3 | 60 |
| 4 | Hh3zeEWtMLM24mQBnomf7Fviem5xEMwJGMxWchhX4gwK | 0.041 | 3 | 73 |
| 5 | GH9yk8vgFvHnAD8JZqXxr3hBN1Lr1mJ9NPzrP5mVqiJe | 0.041 | 11 | 268 |
| 6 | Gak3gXmn3N6JUTggPanQA52yhwzLJ9fdM3SamZ42N5HD | 0.039 | 2 | 51 |
| 7 | 8deJ9xeUvXSJwicYptA9mHsU2rN2pDx37KWzkDkEXhU6 | 0.036 | 2 | 56 |
| 8 | GFA2t9fZVY3jC7wDBPDB8FdsVNzLWgK44J4q7XpP476a | 0.031 | 3 | 97 |
| 9 | 5nNvKhVy27NLYq4xVcCV84QY7v19RQQxYQEfHz7oP1QZ | 0.027 | 7 | 263 |
| 10 | C9TGKPhBf3ovo4RrjeP2bThyhP37DHLgkTqkkvFE4mMs | 0.023 | 2 | 88 |

Table 2: Top creator ranking under filters: total tokens ≥50\geq 50, graduation step ≥10\geq 10, and ratio >0.001>0.001.



| vSolmin>τ{\rm vSol\_{min}}>\tau | Std | | isBot>0.3>0.3 | | Trades≥10\geq 10 | | Top100 wallets | | Top100 creators | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| τ\tau | NeligN\_{\text{elig}} | pp | NeligN\_{\text{elig}} | pp | NeligN\_{\text{elig}} | pp | NeligN\_{\text{elig}} | pp | NeligN\_{\text{elig}} | pp |
| 30 | 652768 | 0.006 | 372960 | 0.010 | 0 | 0.000 | 3885 | 0.004 | 7183 | 0.005 |
| 50 | 40817 | 0.100 | 32794 | 0.112 | 36999 | 0.085 | 8968 | 0.104 | 523 | 0.073 |
| 80 | 11557 | 0.354 | 8181 | 0.436 | 11163 | 0.326 | 2679 | 0.427 | 93 | 0.409 |
| 100 | 6417 | 0.638 | 4611 | 0.748 | 6355 | 0.616 | 1649 | 0.741 | 51 | 0.745 |

Note: Top100 wallets/creators are computed on the last two weeks with the top wallets/creators defined on the first two weeks of the month.

Table [2](https://arxiv.org/html/2602.14860v1#S7.T2 "Table 2 ‣ Conditioning with respect top token creators ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case") reports the top token creators identified during the first two weeks of September.
We define a creator as *successful* if the fraction of their tokens that reach graduation is at least 0.0010.001, subject to two additional constraints.
First, each token must have recorded at least 10 trades during its lifetime, in order to exclude cases in which a creator forces an almost immediate graduation through isolated transactions.
Second, the creator must have issued at least 50 tokens in total.
These thresholds are chosen to ensure a sufficiently large and statistically meaningful sample of tokens per creator.

Successful token creators are identified using data from the *first half* of the month only.
Following the same logic adopted for top traders, we then perform an out-of-sample analysis by computing, over the subsequent two weeks, the probability of graduation conditional on the token being created by one of these selected creators.
This procedure ensures that the conditioning does not exploit future information and preserves a predictive interpretation.

We repeat the analysis by considering different sets of creators, namely the top 10, top 100, and top 1000 successful creators.
The resulting conditional graduation probabilities are shown in Figure [9](https://arxiv.org/html/2602.14860v1#S7.F9 "Figure 9 ‣ Conditioning with respect top token creators ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
We observe that, as the bonding-curve threshold vSol increases, the probability of graduation rises sharply.
In the case of the top 10 creators, the conditional probability even exceeds the economic breakeven curve introduced earlier, indicating that creator identity can carry economically relevant predictive information at sufficiently advanced stages of the bonding curve.

It is important to stress, however, that the statistical support in this conditioning is limited.
As reported in Table [2](https://arxiv.org/html/2602.14860v1#S7.T2 "Table 2 ‣ Conditioning with respect top token creators ‣ VII Prediction variables ‣ Predicting the success of new crypto-tokens: the Pump.fun case"), the number of eligible tokens created by these highly selective groups of creators is relatively small, especially for the top 10 case.
As a result, while the effect is suggestive and consistent with a role of experienced creators in sustaining tokens that have already accumulated liquidity, the corresponding estimates should be interpreted with appropriate caution.

## VIII Pump & Dump of the tokens

Pump-and-dump behavior is a well-known feature of low-friction, low-screening token issuance environments: early participants can accumulate inventory during the initial trading phase and subsequently sell it in a concentrated manner once sufficient liquidity has formed Bello et al. ([2023](https://arxiv.org/html/2602.14860v1#bib.bib15 "LLD: a low latency detection solution to thwart cryptocurrency pump & dumps")); Golmohammadi et al. ([2014](https://arxiv.org/html/2602.14860v1#bib.bib16 "Detecting stock market manipulation using supervised learning algorithms")). In our setting, we deliberately concentrate on *dumps* rather than *pumps* Hamrick et al. ([2021](https://arxiv.org/html/2602.14860v1#bib.bib17 "An examination of the cryptocurrency pump-and-dump ecosystem")); Kamps and Kleinberg ([2018](https://arxiv.org/html/2602.14860v1#bib.bib19 "To the moon: defining and detecting cryptocurrency pump-and-dumps")). In practice, the buy-side leg is intrinsically hard to detect comprehensively: accumulation can be spread over time and fragmented across multiple addresses that are ultimately controlled by the same trader, making coordinated buying largely indistinguishable from ordinary, dispersed demand in on-chain data. By contrast, the exit leg is constrained by execution incentives. To maximize monetization before liquidity conditions deteriorate, a trader typically needs to unwind inventory rapidly and in a highly concentrated manner, using one or a small set of wallets. This concentration makes dump episodes both economically more relevant and empirically more identifiable.

### Shewhart-type rule for dump detection

In our setting, we operationalize a *dump* as a statistically significant negative price shock detected via the rule introduced in this subsection. Motivated by the abrupt drawdowns in Figs. [12](https://arxiv.org/html/2602.14860v1#S8.F12 "Figure 12 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case")–[13](https://arxiv.org/html/2602.14860v1#S8.F13 "Figure 13 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case"), we implement a transparent control-chart procedure to flag dump events during the bonding-curve phase Fantazzini and Xiao ([2023](https://arxiv.org/html/2602.14860v1#bib.bib22 "Detecting pump-and-dumps with crypto-assets: dealing with imbalanced datasets and insiders’ anticipated purchases")). For each token ii, let pi,tp\_{i,t} denote the marginal price implied by the curve at observation time tt (equivalently, the on-curve spot price). We work with log-returns

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t≡log⁡pi,tpi,t−1.\displaystyle r\_{i,t}\equiv\log\frac{p\_{i,t}}{p\_{i,t-1}}\,\,. |  | (5) |

A Shewhart chart requires an “in-control” baseline Champ and Woodall ([1987](https://arxiv.org/html/2602.14860v1#bib.bib18 "Exact results for shewhart control charts with supplementary runs rules")). For each token we estimate a reference location and dispersion using an initial window that precedes the first major run-up. To ensure that the robust scale estimator is well-defined and statistically stable, we restrict attention to tokens for which the baseline window contains at least 3030 to a maximum look-back of 200200 trades (i.e., at least 3030 observations of ri,tr\_{i,t}). This minimum-sample requirement provides a meaningful empirical distribution from which to estimate dispersion and avoids spurious “extreme” events driven by very short or illiquid histories.

To mitigate the impact of heavy tails and microstructure noise, we replace the mean–standard-deviation pair with a median–MAD specification. Specifically, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | mi≡median​(ri,t),MADi≡median​(|ri,t−mi|),\displaystyle m\_{i}\equiv\mathrm{median}\!\left(r\_{i,t}\right),\qquad\mathrm{MAD}\_{i}\equiv\mathrm{median}\!\left(\left|r\_{i,t}-m\_{i}\right|\right), |  | (6) |

computed over the baseline observations. We then define the Gaussian-consistent MAD scale as

|  |  |  |  |
| --- | --- | --- | --- |
|  | σMAD,i≡10.67449​MADi,\displaystyle\sigma\_{\mathrm{MAD},i}\equiv\frac{1}{0.67449}\,\mathrm{MAD}\_{i}, |  | (7) |

where the factor 1/0.67449=2​erf−1​121/0.67449=\sqrt{2}~{\rm erf}^{-1}\frac{1}{2} ensures consistency with the standard deviation under a gaussian reference model Rousseeuw and Croux ([1993](https://arxiv.org/html/2602.14860v1#bib.bib26 "Alternatives to the median absolute deviation")).

We declare a dump signal at the first time tt such that the log-return violates a robust kk-sigma lower control limit,

|  |  |  |  |
| --- | --- | --- | --- |
|  | τiD≡inf{t:ri,t<−k​σMAD,i},k=4.\displaystyle\tau\_{i}^{D}\equiv\inf\left\{t:\ r\_{i,t}<-k\,\sigma\_{\mathrm{MAD},i}\right\},\qquad k=4. |  | (8) |

### Prevalence and stylized facts

Under the definition above, dumps are not a marginal phenomenon: out of 184,282184{,}282 tokens in our sample that had at least 3030 swaps, 169,938169{,}938 (92.22%) exhibit at least one dump event.
Among the 184,282184{,}282, only 2.55%2.55\% graduate. Figure [10](https://arxiv.org/html/2602.14860v1#S8.F10 "Figure 10 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case") reports the distribution of tokens by the number of detected dumps, highlighting a strongly right-skewed structure: most tokens experience no dump or only a small number of events, while a minority displays repeated episodes.

![Refer to caption](x12.png)


Figure 10: Coverage curve. For each dump threshold kk, the curve reports the fraction of coins such that dumps≥k\texttt{dumps}\geq k. The tail of the distribution is preserved by appending a final point at k=maxkk=\max\_{k}, which aggregates all observations with dumps≥maxk\texttt{dumps}\geq\max\_{k}.

From Figs. [11](https://arxiv.org/html/2602.14860v1#S8.F11 "Figure 11 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case")–[13](https://arxiv.org/html/2602.14860v1#S8.F13 "Figure 13 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case") we observe a recurring pattern that is consistent with profit extraction by token creators and, more generally, with pump-and-dump Balcilar and Ozdemir ([2023](https://arxiv.org/html/2602.14860v1#bib.bib21 "On the risk spillover from bitcoin to altcoins: the fear of missing out and pump-and-dump scheme effects")); Yu et al. ([2025](https://arxiv.org/html/2602.14860v1#bib.bib20 "Improving cryptocurrency pump-and-dump detection through ensemble-based models and synthetic oversampling techniques")). In particular, Fig. [11](https://arxiv.org/html/2602.14860v1#S8.F11 "Figure 11 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case") shows that large drops tend to cluster at specific levels of v​S​o​lvSol, i.e., when a non-negligible amount of SOL has already accumulated along the curve, while Figs. [12](https://arxiv.org/html/2602.14860v1#S8.F12 "Figure 12 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case") and [13](https://arxiv.org/html/2602.14860v1#S8.F13 "Figure 13 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case") jointly characterize the severity of such events (drop magnitudes) and the associated concentration of selling activity across wallets (single- vs. multi-wallet episodes). A natural interpretation is that, once the pool has accumulated enough SOL to make the liquidation economically profitable (often prior to graduation), the creator (or a tightly connected set of early wallets) offloads a substantial inventory of tokens acquired since launch and cashes out in SOL. The timing is not accidental: in the late stages of the bonding curve, the price becomes mechanically more sensitive to net order flow, so a concentrated sell wave can trigger an abrupt drawdown.

![Refer to caption](x13.png)


Figure 11: Distribution of the value of SOL in the bonding curve when the dump occurs, shown separately for (i) one-wallet dump episodes and (ii) for multi-wallet dump episodes.

![Refer to caption](x14.png)


Figure 12: Distribution of drop percentage in a dump event, shown separately (i) in one-wallet dump episodes and (ii) in multi-wallet dump episodes.

![Refer to caption](x15.png)


Figure 13: Distribution of the number of dump events executed by each wallet, shown separately for (i) wallets involved in one-wallet dump episodes and (ii) wallets participating in multi-wallet dump episodes. For each Events per wallet, the histogram reports the frequency of wallets that performed exactly Events per wallet dumps.

The incentive to exit before graduation is further strengthened by a liquidity discontinuity at the transition. During the launchpad phase, pricing is produced by a bonding-curve state that includes virtual reserves. At graduation the market moves to a post-migration AMM supported only by real reserves. Even if the marginal price is approximately continuous at the boundary by construction, the depth is not: the disappearance of virtual liquidity reduces the effective inventory against which sells are absorbed. This effect is visible in the expected proceeds of a sale executed just before versus just after graduation.

Fix a token inventory Δ​y\Delta y held by a trader. Consider first a sale *before* graduation, when the bonding-curve state is approximately x=115x=115 SOL and y=0.2799⋅109y=0.2799\cdot 10^{9} tokens. Neglecting fees, the constant-product swap gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​x=x−x​yy+Δ​y=x​Δ​yy+Δ​y=P​Δ​y1+Δ​yy,\displaystyle\Delta x=x-\frac{xy}{y+\Delta y}=\frac{x\Delta y}{y+\Delta y}=P\,\frac{\Delta y}{1+\frac{\Delta y}{y}}, |  | (9) |

where P≡xyP\equiv\frac{x}{y} denotes the marginal price before the swap.

Consider next the same trade executed *after* graduation, when the corresponding post-migration AMM state is approximately x′=85x^{\prime}=85 SOL and y′=0.2069⋅109y^{\prime}=0.2069\cdot 10^{9} tokens. The SOL received is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​x′=x′​Δ​yy′+Δ​y=P​Δ​y1+Δ​yy′,\displaystyle\Delta x^{\prime}=\frac{x^{\prime}\Delta y}{y^{\prime}+\Delta y}=P\,\frac{\Delta y}{1+\frac{\Delta y}{y^{\prime}}}, |  | (10) |

where the equality uses the fact that the boundary is calibrated so that333Remember that continuity of the marginal price does not imply continuity of depth. x′y′≃xy=P\frac{x^{\prime}}{y^{\prime}}\simeq\frac{x}{y}=P. Since y>y′y>y^{\prime}, it follows that Δ​yy<Δ​yy′\frac{\Delta y}{y}<\frac{\Delta y}{y^{\prime}} and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​xΔ​x′=1+Δ​yy′1+Δ​yy>1⇒Δ​x>Δ​x′∀Δ​y>0.\displaystyle\frac{\Delta x}{\Delta x^{\prime}}=\frac{1+\frac{\Delta y}{y^{\prime}}}{1+\frac{\Delta y}{y}}>1\qquad\Rightarrow\qquad\Delta x>\Delta x^{\prime}\ \ \ \forall\,\Delta y>0. |  | (11) |

Hence, holding the same token inventory, selling strictly before graduation is more profitable than selling immediately after graduation, providing a simple mechanical rationale for the pre-graduation sell pressure documented in Figs. [12](https://arxiv.org/html/2602.14860v1#S8.F12 "Figure 12 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case") and [13](https://arxiv.org/html/2602.14860v1#S8.F13 "Figure 13 ‣ Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").

These results link directly to graduation prediction. Because selling strictly before graduation yields higher proceeds, early actors have a clear incentive to dump while the token is still on the bonding curve. The high incidence of pre-graduation dumps therefore acts as a frequent mechanism that cuts the trajectory short: once a dump occurs, the token is far less likely to keep attracting the net inflows required to reach the graduation threshold. In this sense, repeated dump activity makes the virtual bonding-curve market highly manipulable, since coordinated exit behavior can deterministically depress (or terminate) the graduation path.

Predicting the pump leg is considerably harder. As discussed above, accumulation is often executed through multiple wallets, and it is common for the subsequent dump to be carried out by a single wallet after the pump has been distributed across several addresses, with tokens consolidated into the selling wallet at a later time. Identifying such patterns reliably requires deeper wallet-linkage and transfer-graph analysis. For this reason, we leave a systematic study of pump-prediction mechanisms to future work.

## IX Conclusions

This study provides an empirical characterization of token launches on Pump.fun and of the conditions under which newly created tokens reach the protocol-defined *graduation* threshold. The economic motivation for this setting is that tokens are often launched as a financing and coordination primitive for projects with substantive underlying development goals: they are used to bootstrap ecosystems, attract early communities, and establish an initial market valuation under transparent, on-chain rules. Using a fully on-chain dataset reconstructed from Solana transaction logs over a one-month window (September 2025), we document an ecosystem operating at very large scale, with hundreds of thousands of new tokens and a graduation rate well below one percent. This extreme class imbalance motivates a probabilistic framing: rather than attempting to assess project fundamentals directly, we treat graduation as a binary, protocol-level outcome and quantify how its likelihood evolves as a function of the bonding-curve state, thereby offering a scalable screening signal for early traction among project-backed launches.

Our baseline quantity is the empirical probability of graduation conditional on the amount of SOL accumulated in the bonding curve. As expected, this probability increases monotonically with vSol and approaches one near the deterministic threshold. However, conditioning on vSol alone leaves unexplained substantial heterogeneity. We therefore augment the conditioning set with variables that proxy market microstructure and participant composition, constructed in a way that is observable up to the current point on the curve. The resulting conditional curves reveal that not all paths to the same vSol are equivalent: rapid accumulation of liquidity, achieved in a small number of trades, is systematically associated with higher graduation likelihood. For tokens associated with substantive projects, this pattern is consistent with the interpretation that early, coordinated demand reflects stronger initial conviction and faster community formation, which in turn sustains the net inflow required to reach migration.

A second set of results concerns the role of agent types. Tokens whose early activity is dominated by transactions classified as bot-like exhibit a lower probability of graduation beyond intermediate vSol levels, suggesting that algorithmic participation is often correlated with short-horizon trading that does not support sustained capital formation. The presence of historically profitable (“successful”) traders provides at most a modest uplift in graduation probability and should be interpreted with caution, since the identification of such traders can embed ex-post information. In contrast, conditioning on prolific token creators does not improve predictive performance relative to the baseline and is associated with patterns consistent with creator-specific incentives that may not align with long-horizon project value creation.

Several extensions follow naturally. First, the predictive framework could be cast as a hazard-rate (survival) model, so graduation likelihood can be updated continuously over time and along the curve, while properly handling right-censoring. Second, bot detection and the definition of “successful traders” could be made more robust by using out-of-sample evaluation windows and richer behavioral features, reducing look-ahead bias. Third, the profit-extraction channel deserves dedicated accounting of creator-level PnL, including cross-wallet transfers and coordinated selling, to measure how value is redistributed and how these flows interact with project-funding objectives. More broadly, our results suggest that, in bonding-curve launchpads, the composition and pace of early trading carry material predictive signal for protocol-level success and early project traction, while also highlighting structural incentives that can degrade post-graduation market quality if not carefully managed. Finally, future work could expand the feature set with token metadata and platform-level signals, e.g. token name and image, or web-scraped indicators from Pump.fun top-token lists and other on-site rankings.

### Acknowledgements

FL and FT acknowledge support from the grant PRIN2022 DD N. 104 of February 2, 2022 ”Liquidity and systemic risks in centralized and decentralized markets”, codice proposta 20227TCX5W - CUP J53D23004130006 funded by the European Union NextGenerationEU through the Piano Nazionale di Ripresa e Resilienza (PNRR).

## References

* H. Adams, N. Robinson, D. Zinsmeister, M. Keefer, and M. Reed (2020)
  Uniswap v2 core.
  Note: <https://uniswap.org/whitepaper.pdf>
  Cited by: [§III](https://arxiv.org/html/2602.14860v1#S3.p2.1 "III The Pump.fun platform ‣ Predicting the success of new crypto-tokens: the Pump.fun case"),
  [§III](https://arxiv.org/html/2602.14860v1#S3.p5.1 "III The Pump.fun platform ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* F. Allen, S. Morris, and H. S. Shin (2006)
  Beauty contests and iterated expectations in asset markets.
  The Review of Financial Studies 19 (3),  pp. 719–752.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhj036)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p2.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* G. Angeris and T. Chitra (2020)
  An analysis of constant function market makers.
  Mathematics of Financial Markets Conference.
  External Links: 2005.09743
  Cited by: [§III](https://arxiv.org/html/2602.14860v1#S3.p2.1 "III The Pump.fun platform ‣ Predicting the success of new crypto-tokens: the Pump.fun case"),
  [§III](https://arxiv.org/html/2602.14860v1#S3.p5.1 "III The Pump.fun platform ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* M. Balcilar and H. Ozdemir (2023)
  On the risk spillover from bitcoin to altcoins: the fear of missing out and pump-and-dump scheme effects.
  Journal of Risk and Financial Management 16 (1),  pp. 41.
  External Links: [Document](https://dx.doi.org/10.3390/jrfm16010041)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.SSx2.p2.1 "Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* A. S. Bello, J. Schneider, and R. Di Pietro (2023)
  LLD: a low latency detection solution to thwart cryptocurrency pump & dumps.
  2023 IEEE International Conference on Blockchain and Cryptocurrency (ICBC),  pp. 1–9.
  External Links: [Document](https://dx.doi.org/10.1109/ICBC56567.2023.10174922)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.p1.1 "VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* A. Capponi and R. Jia (2022)
  The adoption of decentralized exchanges.
  Management Science.
  Cited by: [§III](https://arxiv.org/html/2602.14860v1#S3.p5.1 "III The Pump.fun platform ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* C. W. Champ and W. H. Woodall (1987)
  Exact results for shewhart control charts with supplementary runs rules.
  Technometrics 29 (4),  pp. 393–399.
  External Links: [Document](https://dx.doi.org/10.1080/00401706.1987.10488234)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.SSx1.p2.4 "Shewhart-type rule for dump detection ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* P. Dubey (2026)
   Yahoo Finance.
  Note: Syndicated on Yahoo Finance (original story credited to Coinspeaker).
  External Links: [Link](https://finance.yahoo.com/news/pump-fun-debuts-investment-arm-094156307.html)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p9.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* D. Fantazzini and Y. Xiao (2023)
  Detecting pump-and-dumps with crypto-assets: dealing with imbalanced datasets and insiders’ anticipated purchases.
  Econometrics 11 (3),  pp. 22.
  External Links: [Document](https://dx.doi.org/10.3390/econometrics11030022)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.SSx1.p1.3 "Shewhart-type rule for dump detection ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* K. Golmohammadi, O. R. Zaiane, and D. Diaz (2014)
  Detecting stock market manipulation using supervised learning algorithms.
  In 2014 IEEE International Conference on Data Science and Advanced Analytics (DSAA),
   pp. 435–441.
  External Links: [Document](https://dx.doi.org/10.1109/DSAA.2014.7058109)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.p1.1 "VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* J. T. Hamrick, F. Rouhi, A. Mukherjee, A. Feder, N. Gandal, T. Moore, and M. Vasek (2021)
  An examination of the cryptocurrency pump-and-dump ecosystem.
  Information Processing & Management 58 (4),  pp. 102506.
  External Links: [Document](https://dx.doi.org/10.1016/j.ipm.2021.102506)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.p1.1 "VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* J. Kamps and B. Kleinberg (2018)
  To the moon: defining and detecting cryptocurrency pump-and-dumps.
  Crime Science 7 (1),  pp. 18.
  External Links: [Document](https://dx.doi.org/10.1186/s40163-018-0093-5)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.p1.1 "VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* J. M. Keynes (1936)
  The general theory of employment, interest and money.
   Macmillan, London.
  Note: Chapter 12 (“The State of Long-Term Expectation”)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p2.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* J. Milionis, A. Lehar, and C. Parlour (2022)
  Automated market making and arbitrage.
  Note: SSRN Working Paper
  Cited by: [§III](https://arxiv.org/html/2602.14860v1#S3.p5.1 "III The Pump.fun platform ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* S. Morris and H. S. Shin (2002)
  Social value of public information.
  American Economic Review 92 (5),  pp. 1521–1534.
  External Links: [Document](https://dx.doi.org/10.1257/000282802762024610)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p2.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* M. Naviglio, F. Tarantelli, and F. Lillo (2025)
  Price manipulation schemes of new crypto-tokens in decentralized exchanges.
  EPJ Data Science.
  Note: In press
  External Links: 2502.10512,
  [Link](https://arxiv.org/abs/2502.10512)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p3.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* Pump.fun (2024)
  Pump.fun: solana token launchpad.
  Note: <https://pump.fun>
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p7.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* K. Qin, L. Zhou, and A. Gervais (2021)
  Quantifying blockchain extractable value: how dark is the forest?.
  2022 IEEE Symposium on Security and Privacy (SP),  pp. 198–214.
  External Links: [Link](https://api.semanticscholar.org/CorpusID:231603355)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p4.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* P. J. Rousseeuw and C. Croux (1993)
  Alternatives to the median absolute deviation.
  Journal of the American Statistical Association 88 (424),  pp. 1273–1283.
  External Links: [Document](https://dx.doi.org/10.1080/01621459.1993.10476408),
  [Link](https://wis.kuleuven.be/stat/robust/papers/publications-1993/rousseeuwcroux-alternativestomedianad-jasa-1993.pdf)
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.SSx1.p3.1 "Shewhart-type rule for dump detection ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* D. Sun, W. Ma, L. Nie, and Y. Liu (2024)
  SoK: comprehensive analysis of rug pull causes, datasets, and detection tools in defi.
  ArXiv abs/2403.16082.
  External Links: [Link](https://api.semanticscholar.org/CorpusID:268680695)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p4.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* C. F. Torres, M. Steichen, and R. State (2019)
  The art of the scam: demystifying honeypots in ethereum smart contracts.
  Santa Clara, CA,  pp. 1591–1607.
  External Links: ISBN 978-1-939133-06-9,
  [Link](https://www.usenix.org/conference/usenixsecurity19/presentation/ferreira)
  Cited by: [§I](https://arxiv.org/html/2602.14860v1#S1.p4.1 "I Introduction ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* J. Yu, M. Park, and S. Chai (2025)
  Improving cryptocurrency pump-and-dump detection through ensemble-based models and synthetic oversampling techniques.
  arXiv preprint arXiv:2510.00836.
  Note: <https://arxiv.org/abs/2510.00836>
  Cited by: [§VIII](https://arxiv.org/html/2602.14860v1#S8.SSx2.p2.1 "Prevalence and stylized facts ‣ VIII Pump & Dump of the tokens ‣ Predicting the success of new crypto-tokens: the Pump.fun case").
* R. Zhang, X. Chen, and D. C. Parkes (2020)
  Formal foundations of automated market makers.
  Proceedings of the 21st ACM Conference on Economics and Computation,  pp. 25–26.
  Cited by: [§III](https://arxiv.org/html/2602.14860v1#S3.p5.1 "III The Pump.fun platform ‣ Predicting the success of new crypto-tokens: the Pump.fun case").