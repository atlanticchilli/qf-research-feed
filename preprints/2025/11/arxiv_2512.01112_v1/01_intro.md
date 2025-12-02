---
authors:
- Tarun Chitra
doc_id: arxiv:2512.01112v1
family_id: arxiv:2512.01112
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Autodeleveraging: Impossibilities and Optimization'
url_abs: http://arxiv.org/abs/2512.01112v1
url_html: https://arxiv.org/html/2512.01112v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tarun Chitra
  
Gauntlet
  
tarun@gauntlet.xyz

(November 30, 2025)

###### Abstract

Autodeleveraging (ADL) is a last-resort loss socialization mechanism for perpetual futures venues.
It is triggered when solvency-preserving liquidations fail.
Despite the dominance of perpetual futures in the crypto derivatives market, with over $60 trillion of volume in 2024, there has been no formal study of ADL.
In this paper, we provide the first rigorous model of ADL.
We prove that ADL mechanisms face a fundamental *trilemma*: no policy can simultaneously satisfy exchange *solvency*, *revenue*, and *fairness* to traders.
This impossibility theorem implies that as participation scales, a novel form of *moral hazard* grows asymptotically, rendering ‘zero-loss’ socialization impossible.
On the positive side, we show that three classes of ADL mechanisms can optimally navigate this trilemma to provide fairness, robustness to price shocks, and maximal exchange revenue.
We analyze these mechanisms on the Hyperliquid dataset from October 10, 2025, when ADL was used repeatedly to close $2.1 billion of positions in 12 minutes.
By comparing our ADL mechanisms to the one used in practice on Hyperliquid and Binance, we demonstrate empirically that Hyperliquid’s production queue overutilized ADL by ≈8×\approx 8\times relative to our optimal policy, imposing roughly $630 million of unnecessary haircuts on winning traders.
This comparison also suggests that Binance overutilized ADL far more than Hyperliquid.
Our results both theoretically and empirically demonstrate that optimized ADL mechanisms can dramatically reduce losses of trader profitability while maintaining exchange solvency.

## 1 Introduction

Perpetual futures (or simply, perpetuals) are by far the most popular crypto derivatives contract.
These contracts allow for duration-independent hedging of cryptocurrencies, such as Bitcoin, Ethereum or Solana.
That is, unlike traditional future contracts, perpetuals are not subject to a fixed expiration date.
Instead, perpetuals are similar to *contracts for difference*, where market participants repeatedly send each other payments depending on how the spot price trades relative to the futures price.
For instance, if the spot price is higher than the futures price, then traders with short futures positions pay the traders with long futures until the prices are equalized.
We note that while Robert Shiller’s 1993 proposal for perpetual futures provides the genesis of this idea, the BitMEX exchange’s 2016 launch of the XBTUSD perpetual swap became the first live implementation [shiller1993measuring, Soska2021BitMEX, Hayes2025AdaptOrDie].

Perpetual futures have a higher notional trading volume than spot cryptocurrency volume.
This is akin to index futures for US stocks, where there is far more volume traded in the futures contracts than the underlying spot assets, with the S&P 500 futures index future trading roughly ten times more volume than the spot asset [CMEGroup2024EqualWeight].
In 2024, centralized crypto exchanges such as Binance and Bybit processed nearly $58.5 trillion (notional) in perpetuals trades [CoinGecko2025Perps].
On the other hand, centralized exchanges processed nearly $17.4 trillion of spot cryptocurrency trades [CoinGecko2025Q1], which is a 3.3x ratio of perpetuals to spot volume.

The main reason for the elevated usage of perpetual futures, much like their index futures cousins, is due to the high level of leverage they offer.
In particular, the capital requirements for trading perpetual futures are much lower than spot trading.
Moreover, the continuous nature of perpetual futures allows for easier margin management than duration-based futures.
This is illustrated via the large gap between the maximum leverage offered by perpetuals exchanges (up to 125x [Binance2025CollateralLeverageUpdate]) versus the index futures on the Chicago Mercantile Exchange (around 10-15x leverage for index futures [CMEGroup2025SP500Margins]).

##### Centralized vs. Decentralized Exchanges.

Historically, the majority of perpetuals trading volume has been concentrated on centralized exchanges (CEXes).
These venues, which include Binance, Bybit, and Coinbase, require users to deposit collateral that is custodied by the exchange.
The exchange is responsible for ensuring that users’ positions are solvent and that their collateral is not used to cover losses from other traders.
In practice, this involves traders having to trust the exchange to not use their collateral for other purposes.
In 2022, centralized exchange FTX was found to have utilized customer collateral for other purposes, leading to multi-billion-dollar losses [FTXDebtors2023Report].

In response, there has been an increasing trend in the usage of decentralized exchanges (DEXes) for trading perpetual futures.
These exchanges provide far more transparency and auditability into the mechanics of the exchange.
In particular, user’s can always verify what their collateral is being used for and what positions it is collateralizing.
Moreover, these exchanges are permissionless and pseudonymous, meaning anyone can trade on these exchanges without explicitly revealing their identity.

The transparent nature of decentralized exchanges does have, however, a downside.
Most positions in decentralized exchanges need to be fully overcollateralized, which generally means traders can take less leverage than they would on a centralized exchange.
Generally speaking, this is because the exchange doesn’t know the identity of a trader and can only enforce global collateral invariants (e.g. assets > liabilities) by forcing users to post more collateral than if the exchange knew their identity.
Early decentralized perpetuals exchanges, such as perpetual protocol, were unable to offer much more than 5x leverage.

However, in recent years, hybrid models of decentralized exchanges where withdrawals and deposits are permissionless, but certain exchange operations are centralized, have become popular.
The most popular exchange of this form is Hyperliquid, which has helped increase the market share of perpetuals volume on DEXs from roughly 1% in 2024 to over 8% in 2025.
These hybrid models allow for the exchange to use cryptographic commitments to enforce collateral rights while also allowing for oracles, markets, and solvency to be controlled by a smaller set of participants.
This allows the exchange to avoid issues that fully open decentralized exchanges have, where weak collateral can be added to an exchange that cannot be sold or liquidated successfully during a market crash to ensure solvency.

More concretely, there have been recent incidents on perpetual DEXs that highlight how novel market structures can be exploited or stressed in practice.
These include but are not limited to: Hyperliquid’s XPL pre-market price spike and the JellyJelly attack [CryptoTimesXPL2025, ODailyXPL2025, OakResearchJELLY].
These episodes led to emergency safeguards and community post-mortems, underscoring the need for robust oracle design, listing policies, and circuit breakers to mitigate manipulation.
Such emergency responses would have been nearly impossible in the fully decentralized setting, demonstrating the value of hybrid models of decentralization in perpetual futures.

##### Liquidations.

Despite the empirical prominence of perpetuals markets, there has been little formal study of the stability and robustness of these markets relative to the large body of research into spot cryptocurrency trading.
For instance, the main price stability mechanism used for perpetuals is the *funding rate*, a continuous payment stream between the long and short positions.
There has been some study of how to replicate funding rates via other financial instruments [AngerisChitra2023PerpsSIAM, he2022fundamentals, ackerer2024perpetual], but little to no empirical study of how well such approximations work.
Even more surprising is the lack of formal study of how robust perpetual exchanges are under high leverage conditions, despite their usage being driven by high leverage traders.

A crucial component to ensuring the stability of perpetual futures markets with high leverage is *liquidation*.
This is the process of closing a user’s position that is worth less than the cash collateral they have posted to the exchange.
Perpetuals exchanges rely on liquidation mechanisms to ensure that they stay solvent — that is, the assets they hold are greater than the liabilities they owe to traders.
To the author’s knowledge, there has been no formal study of liquidations in perpetuals exchanges, despite there being a large body of work studying liquidations in overcollateralized cryptocurrency lending (e.g. [perez2021liquidations, kao2020analysis, sun2022liquidity, qin2021empirical]).

Liquidations are executed by taking the collateral of a trader and selling it in a manner that minimizes losses that the exchange realizes.
In centralized exchanges, liquidations are usually executed by the exchange itself in its own spot markets.
For instance, suppose that a user uses $1,000 worth of collateral to open a long position with 10x leverage.
This implies that if the price falls from the initial price when the contract was opened, p0p\_{0}, by roughly 10%, then the user’s position will have a value of -$1,000, so that user’s net position is $0.
If the price decreases beyond this point, then the user’s position will have a negative value, implying that the user owes the exchange (and hence, other traders) capital.
We say that a trader’s position is *insolvent* if such a negative net position is realized.

Exchanges utilize liquidations to remove trader positions before they are insolvent.
For instance, in our example, an exchange might deem a trader’s position to be liquidatable if the price falls by 9%, such that the trader’s position is closed before insolvency.
Provided that the exchange can execute this position (inclusive of transaction fees and market impact costs) at a price in between 0.91​p00.91p\_{0} and 0.9​p00.9p\_{0}, the position can be closed profitably.
This profit is usually distributed to other traders in the exchange, added to an insurance fund for future losses, or realized as a profit for the exchange.

Centralized exchanges usually execute liquidations in their own spot markets.
This is because they can effectively guarantee atomicity of liquidations, ensuring that the liquidation transaction does not get front run and have a worse execution price than expected.
In decentralized exchanges, liquidiations are usually executed by third-party actors known as liquidators.
Liquidators can be viewed as traders who have the ability to warehouse the inventory of a collateral position and exit profitably.
From an economic perspective, liquidations need to be profitable for either the exchange or the liquidator in order to help with exchange solvency.

##### Autodeleveraging.

In severe market dislocations, it is sometimes possible for liquidations to be so deeply unprofitable that they are unable to be executed by any party.
When this happens, the exchange can reach a state of insolvency, where the assets held are less than the liabilities owed to its traders.
This excess in liabilities is known as the *shortfall*.
In such scenarios, a natural strategy to reduce the risk of total insolvency is to socialize losses by haircutting profitable (or *winning*) traders.
In the worst case, a winning user’s position is completely closed to zero, leaving them with a potentially large opportunity cost.
This process is known as *autodeleveraging* (ADL) and is a last-resort measure used by exchanges.

Autodeleveraging is unique in that it algorithmically socializes losses on winners based on a public rule or mechanism that an exchange posts.
This means that all of the position closures and implicit liquidations of insolvent positions are performed in an irreversible and atomic manner.
The closest analogue to autodeleveraging in traditional finance is a central counterparty (CCP) such as a derivatives clearing house.
In traditional finance, CCPs employ default waterfalls and loss mutualization (including variation-margin gains haircutting (VMGH)) that share the same core idea of allocating residual losses across non-defaulting members [DuffieZhu2011, Pirrong2011, CPMI\_IOSCO\_2014, ContGhamamiSITG, KubitzaWinnersLosers, Turing2019MagicRelighting].
CCPs generally have manual, non-algorithmic socialization and disbursement of insurance funds during such events with disputes reconciled via the legal system.
We note, furthermore, that only clearing members bare the losses in CCPs, which leads to a different principal-agent dynamic than perpetuals markets as smaller traders need not bare the final losses.

Autodeleveraging, to the best of the author’s knowledge, was first introduced by the crypto exchange Huobi in 2015 [HuobiADL].
Prior to the implementation of ADL, exchanges would manually socialize losses, with the exchange serving as the sole CCP.
By 2016, the BitMEX exchange implemented ADL via a formula that ranked trader positions for ADL by their profit times their leverage [BitMEXADL].
This formula persists to today on virtually every centralized exchange (including Binance, who implemented the formula in 2019 [BinanceADL]) and on the decentralized exchange Hyperliquid [HyperliquidDocsLiquidations].
We note that there are some decentralized exchanges such as Drift [DriftADLCode] and Paradex [ParadexADLBlog] that use a different ADL mechanism (the *pro-rata* mechanism defined in §[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
However, well over 95% of perpetuals trading volume is on exchanges that utilize the BitMEX ranking model.

In practice, ADL is reserved for extreme tail events where routine liquidation mechanisms are insufficient to maintain venue solvency.
There are two primary scenarios that can trigger ADL activation.
First, a sudden and large price movement can push positions far beyond their liquidation thresholds before the exchange’s liquidation system can execute the necessary trades.
Second, a temporary but severe loss of executable liquidity in the order book can prevent the exchange from closing positions at prices near their liquidation triggers, even when the price movement itself is not extreme.

To illustrate how such scenarios can lead to insolvency, consider a concrete example.
Suppose that a trader posts $1,000 of collateral to take a 10x leveraged long position with a notional value of $10,000, where the position becomes liquidatable when the price declines by 9% from its initial value p0p\_{0}.
Under normal market conditions, the exchange would execute a liquidation when the price reaches 0.91​p00.91\,p\_{0}, closing the position and recovering the collateral.
However, if an abrupt 12% price drop occurs between price updates or during a period of low liquidity, the position may be closed at a significantly worse execution price, such as 0.88​p00.88\,p\_{0} rather than the intended 0.91​p00.91\,p\_{0}.
In this scenario, the account’s equity becomes negative, representing approximately 2% of its initial collateral value.
When many traders simultaneously experience such execution slippage and the exchange’s insurance fund reserves cannot absorb the aggregate resulting losses, the venue triggers ADL.
Under the exchange’s predefined ADL rules, the system algorithmically reduces or closes profitable opposing positions until the shortfall is covered and solvency is restored.

Inherently, ADL creates *moral hazard* — that is, losing traders have an incentive to take on more risk in anticipation of being socialized by winning traders.
The goal of an exchange is to balance the risk of insolvency against haircutting winning trader profits.
Moral hazard is measured by this trade-off — if it is possible to reduce the risk of insolvency to zero without haircutting winning traders, then the system has no moral hazard.
On the other hand, if it is not possible to reduce the risk of insolvency by any appreciable amount without severely haircutting winning trades, the system has excessive moral hazard.
The job of an exchange operator is to choose an ADL mechanism that tries to induce a low level of moral hazard under most tail event scenarios.
This connects to principal–agent models of moral hazard and linear/robust contracting [Holmstrom1982, Carroll2015RobustLinearContracts, DuttingEtAl2023MultiAgentContracts], with key differences: many agents act simultaneously, externalities operate through a common solvency constraint, and tail-risk mitigation substitutes for standard effort observability.

Despite the rarity of ADL, it is certainly not hypothetical: there have been dozens of instances of ADL activations on major venues since 2018 [BinanceADL, BitMEXADL, AevoADL, CoinglassADL].
The largest episode of ADL usage was on October 10-11, 2025 (UTC), when outsized liquidations exhausted insurance funds and multiple venues simultaneously invoked ADL [CoinDesk2025LargestLiquidations].
However, other famous incidents such as the March 2020 “Black Thursday” and May 19, 2021 deleveraging event were other prominent days involving ADL usage.
Most of these usages of ADL often involved controversies, in that highly profitable but lower risk (e.g. lower leverage) traders found their positions closed out by ADL mechanisms.
These traders have often threatened to sue exchanges for unfair treatment, with rumors and public speculation surfacing during Oct. 10–11, 2025 (subsequently denied by Wintermute) [CointelegraphWintermute2025, TheBlockWintermute2025]111See also prior complaints during May 2020 on Binance futures when profitable shorts were closed via ADL [CointelegraphBinanceADL2020].

This incidents demonstrate a natural trade-off that perpetuals exchanges have to make: they can either aggressively socialize losses to their winners and (potentially) lose the future revenue of these users while preserving solvency or hold the losses due to the insolvency on their balance sheet.
In the former case, the exchange effectively chooses to prioritize short term solvency and potential liquidation profits over long term value and fees generated by users.
The latter case, effectively creates a long term risk for the exchange’s balance sheet, especially if it does not have sufficient funds to cover insolvencies.
This strongly suggests that one can view the choice of how an exchange implements ADL as a trade-off between solvency, moral hazard, and long term revenue for an exchange.

We note that open interest post October 10, 2025 that suggests that Hyperliquid has nearly 50% of open interest, whereas competitors such as Lighter and even Binance have recovered to pre-event levels.222Source: DeFiLlama perpetuals dashboard, <https://defillama.com/perps>, accessed Nov. 30, 2025.
Open interest is generally more expensive to manipulate than trading volume and can serve as a coarse measurement of expected future revenue for an exchange.
Numerous parties have argued that this open interest loss for Hyperliquid is due to their overly aggressive ADL policy.333See, e.g. , public commentary from @fiddybps1, @0xReaz, @Eugene\_Bulltime, and @0xLouisT on X (Nov. 2025): <https://x.com/fiddybps1/status/1978750722901762321>, <https://x.com/0xReaz/status/1986486213101166599>, <https://x.com/Eugene_Bulltime/status/1994380900067582182>, <https://x.com/0xLouisT/status/1990815109787058654>.

##### This Paper.

In this paper, we provide (to the author’s best knowledge) the first formal mathematical model of autodeleveraging.
The main model of the paper is venue-agnostic: it abstracts away pricing (e.g. order book versus automated market maker microstructure) and focuses on how positions are opened and closed.
As a warning to the reader: this paper is more verbose than necessary.
The author aims to provide a self-contained, pedagogical introduction to perpetual futures and liquidations, as the current literature and open source documentary does not cover liquidations and ADL in any manner comprehensive enough for formal study.
Throughout the paper, there will be numerous simple numerical examples to illustrate the basic concepts and mechanics of perpetual futures.

The first section of the paper (§[2](https://arxiv.org/html/2512.01112v1#S2 "2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) provides definitions and examples of the basic objects — *positions* — and basic operations that one can perform on them.
In the process of defining the set of operations on positions, we will naturally need to define the economics of positions using funding rates and arbitrage.
These definitions will hopefully provide answers to the questions of why one opens a position, how much one has to spend on keeping a position open, and how positions on different exchanges achieve price synchronization.
From these economic properties, we will naturally define solvency for both individual traders and of the exchange itself.

Liquidations and ADL then naturally follow as operations that exist to try to use economic means to enforce solvency constraints with high probability.
We will define the set of ADL mechanisms in a sufficiently broad manner to allow for venue-specific ADL, this allowing us to compare Binance, Hyperliquid, Drift, and other exchanges.
Our decomposition of the ADL strategy space into *severity* (i.e., dollar amount impacted by ADL) and *haircuts* (i.e., per-trader percentage liquidated) allows us to separate exchange solvency and trader profitability into two separate optimization problems.
This will be key to simplifying our results and constructing practical algorithms.

Given a perpetuals exchange, defined in the combinatorial manner of §[2](https://arxiv.org/html/2512.01112v1#S2 "2 Background ‣ Autodeleveraging: Impossibilities and Optimization"), we next focus on notions of risk that are endemic to perpetuals exchanges in §[3](https://arxiv.org/html/2512.01112v1#S3 "3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization").
We construct a set of risk measurements that, while specific to perpetuals exchanges, are connected to classical risk metrics such as Value-at-Risk.
Subsequently, we describe four facets of perpetuals exchange risk that we will analyze: extreme value analysis, Schur ordering, fairness, and moral hazard.

Extreme value analysis is the classical actuarial estimation of tail probabilities and rare events.
We provide a simple primer to make the text self-contained and our notation consistent.
The Schur ordering provides a way of partially ordering risk measurements, even if they are not fully comparable.
This allows us to compare ADL mechanisms across venues, despite the fact that the outcomes might not have explicitly comparable risks in every situation.
Algorithmic fairness measures (axiomatic and optimization-based) are subsequently introduced to concretely answer the question of whether ADL is more fair to certain traders than others.
Finally, we describe the general moral hazard problem and specialize it to the perpetuals exchange setting.
In this setting, it corresponds to whether the exchange operator has an incentive to take on more risk than necessary because they can socialize worst-case losses on their best traders.

With these risk tools in tow, we are now prepared to describe the main results of the paper.
We have five classes of results in this paper:

1. 1.

   *Negative*: Moral hazard is strictly increasing in the size of the exchange.
2. 2.

   *Fairness*: The Pro-Rata ADL mechanism is the most fair mechanism
3. 3.

   *Robustness*: Given a risk model gg for historical user behavior, there is a unique ADL mechanism maximally robust to price shocks
4. 4.

   *ADL as Stackelberg Game*: Multiple price shocks causing ADL to be used repeatedly are a Stackelberg game that can be studied rigorously.
5. 5.

   *Empirical*: Using Hyperliquid’s data from October 10, 2025, where ADL was used over 40 times in a 10 minute period, we evaluate the performance of difference ADL mechanisms

##### Negative Results.

Our negative results focus on quantifying limits to how much ADL can actually reduce insolvency without inuring traders with disproportionate losses.
We explicitly ask the question of how the loss of profit due to ADL to the trader with the highest PNL scales as the number of positions nn grows.
We quantify this by looking at ratios of the maximum winner’s profit to the total shortfall (over all traders) and to the worst trader’s shortfall.
These ratios can be viewed as analogues of the Value-at-Risk and Expected Shortfall metrics in traditional risk modeling, as we show in Appendix [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").
The main difference is that while Value-at-Risk and Expected Shortfall measure the total expected loss (over all traders) in tail events, our metrics only measure the expected loss to the most winning trader.
Moreover, Appendix [B.5](https://arxiv.org/html/2512.01112v1#A2.SS5 "B.5 Relationship to Classical Risk Measures ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") shows that classical VaR/ES rankings echo the same conclusion: queue-based ADL always delivers the lowest top-winner survival even under these traditional risk lenses.

When these ratios, as constructed, are bounded below by a constant, then the winner can expect to always retain at least a constant fraction of their earnings after an ADL event.
However, if these ratios decay to zero, then the winner has no guarantee of retaining any of their profits after an ADL event.
We show that under some mild technical assumptions, these ratios decay as O​(bnn)O(\frac{b\_{n}}{n}), where bnb\_{n} is the *extreme value scale* (EV scale) of profits (see §[3](https://arxiv.org/html/2512.01112v1#S3 "3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization")).
For most well-behaved probability distributions over the set of profits, bn=o​(n)b\_{n}=o(n), so the ratios decay to zero.
This result establishes a fundamental limit of these markets: moral hazard scales with participation.
It suggests that as crypto exchanges grow, ADL must become either more frequent or more severe for top traders; they cannot “grow out” of the problem.

##### Fairness Results.

As the negative results show that no ADL mechanism can scale to preserve winner’s profit, a natural follow-up question is, what is the most fair way of socializing profitable users?
We consider two notions of fairness in §[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization"): axiomatic and optimization-based.
They are both common in the algorithmic fairness literature within machine learning [KleinbergEtAl2018FairnessImpossibility, BarocasHardtNarayanan2019FairnessBook, Mehrabi2021SurveyFairness, DworkEtAl2012FairnessAwareness, Agarwal2018ReductionsFairness, HardtPriceSrebro2016EqualityOfOpportunity].
We demonstrate that the pro-rata ADL rule (used by Drift [DriftADLCode] and Paradex [ParadexADLBlog]) is the unique fair ADL rule in *both* the axiomatic and optimization senses [johnson2023concave].

Axiomatic fairness involves defining rules or invariants that a particular ADL mechanism must satisfy to be deemed fair.
The rules we analyze for fairness are monotonicity, scale invariance and Sybil resistance.
Roughly speaking, monotonicity says that if you were the kkth highest winner (ranked by PNL) before ADL, then you will be the kkth highest winner after ADL.
Scale invariance states that if everyone scaled up their positions by an equal factor, their loss due to ADL does not change.
And finally, Sybil resistance states that splitting a position into multiple positions does not change the loss due to ADL.
We show that under mild smoothness conditions, the pro-rata ADL rule is the unique rule to satisfy these axioms.
In stark contrast, we show that the queue-based mechanisms used by Binance and Hyperliquid are effectively “anti-fair”: in our model and data they produce extremely low Profit-to-Solvency Ratios (PTSR), imposing disproportionately large losses on the top winner.
This finding contradicts the common intuition that queues are orderly; instead, they concentrate losses on the most successful traders.

Optimization-based fairness involves showing that for a large class of individual trader utility functions, a particular mechanism maximizes social welfare (i.e., the total profit).
This is more of a system-wide fairness notion, as it shows that the system as a whole is fair, even though there might be individuals who were punished more by an ADL mechanism.
Unlike the axiomatic rules, which have to hold for every trader exactly, the optimization-based fairness rules can be thought of as ‘fuzzier’ and allowing for more slack.
Despite this, we still show that the pro-rata ADL rule is the unique rule to maximize social welfare for a large class of concave utility functions.

##### Robustness Results.

A natural question, beyond fairness, is whether an ADL rule is *robust* to subsequent price shocks.
The main question here is whether the choices of severities (e.g. total amount to socialize) and haircuts (e.g. per-account socialization) increases the chance of insolvency should another price shock occur.
In §[7](https://arxiv.org/html/2512.01112v1#S7 "7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization"), we consider a new threat model where an ADL mechanism is graded based on how well it reduces to total shortfall from two price shocks.
The model involves a price shock occurring that triggers ADL, an ADL policy being executed, and then another price shock occurring.

We show that a natural way to model total shortfall is via a *risk model* gg that maps a user’s amount of leverage used to a risk score.
A higher risk score implies that a trader’s leverage level places a higher burden on the rest of the exchange’s solvency, especially in the repeated price shock scenario.
We first show that the risk model is effectively a way to quantify the total shortfall.
Given a stochastic process for price shocks, one can construct an optimal risk model (using convex duality) g∗g^{\*} that maximizes the total solvency gained per dollar of winner position that is haircut by an ADL policy.
With the optimal risk model in hand, we construct a linear-time algorithm to choose haircuts for each trader that are weighted by this model.
We then show that the resulting ADL policy derived from these weights has lowest expected total shortfall and is the optimal ADL policy (in the Schur ordering sense).

##### ADL as a Stackelberg Game.

A direct extension of the robustness threat model is to consider a sequential ADL problem, where for multiple rounds, a price shock is received, the exchange chooses an ADL policy, and then losses are realized.
This model might at first glance seem to only have theoretical value since ADL is itself a rare event.
However, on October 10, 2025 there were multiple ADL events that occurred over a short time window on both Hyperliquid and Binance.
While the account-level data for Binance’s usage of ADL is not public, we do have this data for Hyperliquid.
Starting at 10:21:00 UTC, there were at least 40 recorded ADL events on Hyperliquid in a 10 minute period.
This strongly suggests that there is clustering or cascading of ADL events, making the multiple round model necessary to study.

Unlike in the single round models (used for fairness and robustness), the exchange is allowed to adjust their ADL policy after each ADL shock.
One can view this as a sequential game and we argue that it is a *Stackelberg game*.
Stackelberg games have a well-known follower-leader decompsoition, where one user (the leader) plays a strategy first.
Then the follower conditions their strategy on the leader’s action, before playing their own move.
In the ADL setting, the exchange is the leader and the traders are the followers.

We first show that viewing ADL as a dynamic, multiple round Stackelberg game leads to sharply different equilibria.
We prove a crucial “principal-agent” tension: any strategy an exchange executes that minimizes the time to recover solvency (i.e., number of rounds) necessarily maximizes the loss of exchange long-term revenue.
This trade-off is the economic heart of the paper: the exchange wants to be solvent in few rounds, but doing so destroys the best customers (e.g. the whales).
Intuitively, this occurs because any strategy that quickly recovers solvency autodeleverages the largest winners more aggressively.
These winners, however, are also often the most profitable users and generate high long-term fees for the exchange.
By liquidating them aggressively, you’re removing the capital that they would use to later create positions and generate fees.
We note that threats to sue exchanges for ADL losses in profit after October 10, 2025 provide indirect empirical evidence to support this theoretical result [CointelegraphWintermute2025, TheBlockWintermute2025].

This implies that any optimal ADL policy over multiple ronds also has to include incentive compatibility constraints that balance future exchange revenue, current exchange solvency, and current trader profits.
We construct an explicit algorithm for optimizing a revenue and solvency based objective and show that a simple mirror descent algorithm achieves vanishing regret for this objective.
We conclude with a simple example demonstrating that no static policy that dominate the dynamic policy, especially when exchange long-term revenue is a consideration.

##### Empirical Results: The $630 Million Inefficiency.

We conclude by analyzing the October 10, 2025 ADL events on Hyperliquid.
Unlike centralized exchanges like Binance and Bybit, Hyperliquid publicly shares all position data, including position leverage, collateral, PNL, and ADL status.
Using this data, we evaluate the efficiency of Hyperliquid’s ADL mechanism (which is a slight modification of the original 2015 Huobi queueing mechanism).
We show that Hyperliquid autodeleveraged roughly  $705m of winning trader PNL during the 12 minute cascade on October 10, 2025.
Over the same period, there were at least 40 ADL events which accumulated a total of  $304m of negative equity positions.444Hyperliquid’s on-chain fill log for 10 Oct. 2025 records 34,983 individual ADL executions across 19,337 distinct wallets and 162 tickers. We analyze the per-fill data but aggregate those executions into the 40 queue waves discussed in the text.
Measured shock-by-shock, this implies the production queue generated about  $630m of overshoot—haircuts beyond the deficits that actually materialized.
This result highlights a massive capital inefficiency in current queue-based mechanisms: they are not just unfair; they destroy hundreds of millions of dollars of trader value unnecessarily.

We then compare the pro-rata, risk-weighted pro-rata, and dynamic mechanisms to the live queueing mechanism used.
We utilize these methods with different severity optimization algorithms and show that all of these algorithms were able to learn to autodeleverage substantially less than what Hyperliquid did in practice.
Utilizing these algorithms on the historical data, we find that nearly 98% of the over autodeleveraging used by Hyperliquid could have been removed by a smarter ADL policy.

##### Notation.

* •

  For a vector x∈Rnx\in{\mbox{\bf R}}^{n}, we define (x)+=max⁡(x,0)(x)\_{+}=\max(x,0), where this is done coordinate-wise and (x)−=min⁡(x,0)(x)\_{-}=\min(x,0) (also coordinate-wise).
  Using our convention, we have (x)+=−(−x)−(x)\_{+}=-(-x)\_{-}
* •

  We denote the set of integers {1,…,n}\{1,\ldots,n\} by [n][n].
* •

  For a sequence x1,x2,…x\_{1},x\_{2},\ldots, we denote the subsequence from ss to tt as xs:t=(xs,xs+1,…,xt)x\_{s:t}=(x\_{s},x\_{s+1},\ldots,x\_{t}).
* •

  We use 𝟏E\mathbf{1}\_{E} or 𝟏​{E}\mathbf{1}\{E\} to denote the indicator function of an event EE, which is 11 if EE is true and 0 otherwise.
* •

  We use the notation f​(n)≍g​(n)f(n)\asymp g(n) to denote that f​(n)=Θ​(g​(n))f(n)=\Theta(g(n)), i.e., there exist constants c,C>0c,C>0 such that c​|g​(n)|≤|f​(n)|≤C​|g​(n)|c|g(n)|\leq|f(n)|\leq C|g(n)| for sufficiently large nn.
* •

  We write Xn≍pYnX\_{n}\asymp\_{p}Y\_{n} for random variables Xn,YnX\_{n},Y\_{n} if there exist constants c,C>0c,C>0 such that c​|Yn|≤|Xn|≤C​|Yn|c|Y\_{n}|\leq|X\_{n}|\leq C|Y\_{n}| with high probability as n→∞n\to\infty.
* •

  For vectors x,y∈Rnx,y\in{\mbox{\bf R}}^{n}, we write x≺yx\prec y if xx is majorized by yy (see §[3.2](https://arxiv.org/html/2512.01112v1#S3.SS2.SSS0.Px1 "Schur-Convexity and Submajorization. ‣ 3.2 Fairness and Distributional Comparisons ‣ 3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization") for details).

## 2 Background

We will first introduce a mathematical model for solvency risks in a perpetuals exchange.
Using this model, we define the key components for measuring the solvency of perpetuals exchanges: trader equity, exchange deficits, and autodeleveraging (ADL) policies.
These components will allow us to formalize the notion of moral hazard in perpetuals exchanges and sets the notation up for our main results in §[5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization"), §[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization"), §[7](https://arxiv.org/html/2512.01112v1#S7 "7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization"), and §[8](https://arxiv.org/html/2512.01112v1#S8 "8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization").

### 2.1 Perpetuals Exchanges.

A *perpetuals futures exchange* (or perpetuals exchange) is a derivatives trading venue that allows traders to use leverage to speculate on the prices of cryptocurrency assets.
The main asset traded is a perpetual future, which is a continuous, expiryless futures contract.
Traders speculate on the contract in either the long (buy) or short (sell) direction.
Traders are allowed to make leveraged bets up to a maximum leverage cap ℓmax\ell^{\max}.
As is often common with levered positions, the trader has to post collateral, known as *margin*, to keep their positions *solvent*.
We define a precise notion of solvency in this section, but for now think of solvency conditions as meaning that a trader’s assets are greater than their liabilities.

The exchange incentivizes futures prices to approximately match spot prices by having long and short traders pay each other a continuous rate, known as the *funding rate*.
The funding rate is determined by the spot price of the asset and the relative imbalance of long and short futures positions.
Arbitrageurs keep the price of the futures contract in line with the spot price by opening futures positions that push the contract price towards the spot price.
For simplicity, we assume that trades occur in discrete time t∈Nt\in{\mbox{\bf N}}, but note that our results can easily be extended to continuous time t∈R+t\in{\mbox{\bf R}}\_{+}.

##### Spot Price Oracle.

Perpetual futures exchanges require a spot price oracle that provides a spot price of the asset from a spot trading venue.
Price oracles are assumed to be expensive or difficult to manipulate, which is dependent on the liquidity of the spot market.
Most perpetuals exchanges utilize oracles that aggregate price reporting over multiple venues to increase the overall liquidity represented in the price and hence, the manipulation cost.
We assume that there is a non-manipulable spot price p^t\hat{p}\_{t} for an asset at all times t∈R+t\in{\mbox{\bf R}}\_{+}.
Furthermore, we denote the futures price quoted by the exchange as ptp\_{t} and similarly assume that it exists for all t∈R+t\in{\mbox{\bf R}}\_{+}.

##### Positions.

Given a spot price oracle and futures price, a perpetuals exchange is able to open and close *positions* created by its traders.
A position consists of collateral deposited by the trader, a leverage amount, and a direction (e.g. buy or sell).
A trader’s position is updated as the spot price changes, realizing a gain or a loss for the trader.
The accumulation of gains and losses over the lifetime of the position is the trader’s PNL (profit-and-loss).
We define a perpetuals exchange with nn traders as the set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫n={(qi,ci,ti,bi)∈R+3×{−1,1}:i∈[n]}\mathcal{P}\_{n}=\{(q\_{i},c\_{i},t\_{i},b\_{i})\in{\mbox{\bf R}}\_{+}^{3}\times\{-1,1\}:i\in[n]\} |  | (1) |

where qi≥0q\_{i}\geq 0 is the notional quantity of futures held by the trader, ci≥0c\_{i}\geq 0 is the trader’s collateral (cash) position (also known as the *initial margin*), ti∈Nt\_{i}\in{\mbox{\bf N}} is the timestamp that the position was created, and bib\_{i} is their side (−1-1 is sell, 11 is buy).
We denote each position 𝔭i=(qi,ci,ti,bi)\mathfrak{p}\_{i}=(q\_{i},c\_{i},t\_{i},b\_{i}) and assume that without the loss of generality that there is a fixed, strictly increasing ordering of these orders such that we can refer to 𝔭i\mathfrak{p}\_{i} unambiguously.

For each position 𝔭\mathfrak{p}, we define the *notional exposure* at time tt is the gross dollar size

|  |  |  |
| --- | --- | --- |
|  | ni,t=pt​qi.n\_{i,t}\ =\ p\_{t}\,q\_{i}\,. |  |

The notional exposure is the gross dollar size of the trader’s position and is used to define leverage.

##### Example.

In this section, we fix a canonical running example that we will reuse across definitions to illustrate each exchange function.
Our simple test perpetuals exchange will have five positions, 𝒫5\mathcal{P}\_{5}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫5={\displaystyle\mathcal{P}\_{5}=\Big\{ | 𝔭A=(qA,cA,tA,bA)=(1, 2, 0,+1),\displaystyle\mathfrak{p}\_{A}=(q\_{A},c\_{A},t\_{A},b\_{A})=\big(1,\,2,\,0,\,+1\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔭B=(qB,cB,tB,bB)=(1,23, 0,+1),\displaystyle\mathfrak{p}\_{B}=(q\_{B},c\_{B},t\_{B},b\_{B})=\big(1,\,\tfrac{2}{3},\,0,\,+1\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔭C=(qC,cC,tC,bC)=(4,83, 0,−1),\displaystyle\mathfrak{p}\_{C}=(q\_{C},c\_{C},t\_{C},b\_{C})=\big(4,\,\tfrac{8}{3},\,0,\,-1\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔭D=(qD,cD,tD,bD)=(1,219, 0,+1),\displaystyle\mathfrak{p}\_{D}=(q\_{D},c\_{D},t\_{D},b\_{D})=\big(1,\,\tfrac{2}{19},\,0,\,+1\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔭E=(qE,cE,tE,bE)=(1,1099, 0,−1)}.\displaystyle\mathfrak{p}\_{E}=(q\_{E},c\_{E},t\_{E},b\_{E})=\big(1,\,\tfrac{10}{99},\,0,\,-1\big)\Big\}. |  |

Moreover, if at t=0t=0 we have p0=1p\_{0}=1 for 𝒫5\mathcal{P}\_{5}, then the notional exposure are:

|  |  |  |
| --- | --- | --- |
|  | nA,0=1⋅1=1,nB,0=1⋅1=1,nC,0=1⋅4=4,nD,0=1⋅1=1,nE,0=1⋅1=1.n\_{A,0}=1\cdot 1=1,\quad n\_{B,0}=1\cdot 1=1,\quad n\_{C,0}=1\cdot 4=4,\quad n\_{D,0}=1\cdot 1=1,\quad n\_{E,0}=1\cdot 1=1. |  |

Note this toy example is net short by 2 contracts: ∑ibi​qi=−2\sum\_{i}b\_{i}q\_{i}=-2.
For AMM-style venues, the pool holds the offsetting inventory qV=2q\_{V}=2 with bV=+1b\_{V}=+1, so across traders plus venue ∑ibi​qi+bV​qV=0\sum\_{i}b\_{i}q\_{i}+b\_{V}q\_{V}=0.
For order-book venues, interpret 𝒫5\mathcal{P}\_{5} as a subset of accounts.
The complementary matched positions are omitted but implied.555We note that in centralized exchanges, the exchange itself creates the complementary positions whereas in decentralized exchanges with order books (like Hyperliquid and Lighter), a liquidity provider like HLP or LLP owns the position; see Hyperliquid’s HLP documentation [HyperliquidHLPVaults] and the Lighter whitepaper [LighterWhitepaper].
All zero-sum statements (e.g., funding rates, which will be defined shortly) are taken over traders plus the venue inventory.

##### Position Creation.

When an exchange opens a new position, it performs two tasks:

1. 1.

   Selecting a price ptp\_{t} for the position and constructing 𝔭=(q,c,t,b)\mathfrak{p}=(q,c,t,b).
2. 2.

   Construction of an equal but opposite position, 𝔭¯=(q,c,t,−b)\overline{\mathfrak{p}}=(q,c,t,-b) is created

The latter condition is needed because the perpetuals exchange is meant to be a neutral matching layer for traders.
This means that the exchange should not have a net exposure to the spot asset, as it increases the risk of default for traders.
Specifically, the position 𝔭¯\overline{\mathfrak{p}} is created to ensure that the total notional exposure of the exchange to the spot asset is zero.666In centralized venues such as Binance Futures, the matching engine and clearing layer are designed to operate a matched book over user positions, as reflected in their open interest endpoints for USD$- and COIN-margined futures [BinanceFuturesOpenInterest]. In decentralized order-book venues like Hyperliquid, the protocol core similarly avoids taking directional exposure. Offsetting inventory is held in separate HLP vaults on behalf of liquidity providers [HyperliquidHLPVaults].
We define

|  |  |  |
| --- | --- | --- |
|  | 𝒫¯n=𝒫n∪{𝔭¯:𝔭∈𝒫n}\overline{\mathcal{P}}\_{n}=\mathcal{P}\_{n}\cup\{\overline{\mathfrak{p}}:\mathfrak{p}\in\mathcal{P}\_{n}\} |  |

as the full set of positions held by the exchange (including matching, complementary positions).

While all venues construct 𝔭¯\overline{\mathfrak{p}} in the same manner, the price ptp\_{t} is chosen in a venue-specific manner.
Each venue has a *liquidity model* for determining how prices ptp\_{t} are chosen.
The two most popular liquidity models are order books and automated market makers (AMMs).

Order book venues maintain a limit order book of bids and asks for perpetual futures contracts at discrete price levels, and have been extensively studied in the market microstructure literature [Kyle1985, AlmgrenChriss2001, Gatheral2010, BouchaudImpact2010].
Traders may submit limit orders, which rest in the book until they are matched, or market orders, which execute immediately against resting liquidity.
When a trader opens a new position as a taker, the execution price ptp\_{t} is the volume-weighted average of the resting orders they consume, i.e., the price they would obtain by submitting a market order of size qq into the book at time tt.
The largest order book venues in the perpetual futures market include centralized exchanges such as Binance and Bybit and decentralized exchanges such as Hyperliquid and Lighter.777From a risk-warehousing perspective, Hyperliquid’s HLP vaults cause the protocol to function as a hybrid between a pure order-book venue and an inventory-taking pool: user orders are matched via an order book, but directional exposure is warehoused collectively in HLP vaults on behalf of liquidity providers [HyperliquidHLPVaults, OakResearchJELLY, CoinDesk2025LargestLiquidations].

Automated market maker (AMM) venues maintain a pool of collateral and inventory for the perpetual, and quote prices according to a deterministic pricing rule or bonding curve that depends on the pool state, typically implemented via constant-function market makers [AngerisChitra2020ImprovedOracles, Angeris2023GeometryCFMM].
Traders interact with the pool via swap-like trades: submitting an order of size qq moves the pool along its pricing curve, and the execution price ptp\_{t} is the average price paid over this path.
When a trader opens a new position against the AMM, the pool itself holds the offsetting inventory 𝔭¯\overline{\mathfrak{p}}, so that the trader’s exposure is matched by an equal and opposite position in the pool, as in inventory-taking perpetual venues such as GMX, Drift, and Perpetual Protocol v2 [GMXDocs, DriftADLCode, PerpV2Docs].

In the remainder of this paper, we will ignore the liquidity model of a perpetuals exchange.
This is because the default conditions that we will study for autodeleveraging only depend on the positions 𝒫n\mathcal{P}\_{n} and not the process by which they were created.

##### Example.

Consider an order-book venue at time tt with three resting sell (ask) limit orders

|  |  |  |
| --- | --- | --- |
|  | (p1,q1)=(1.0,1),(p2,q2)=(1.1,3),(p3,q3)=(1.2,10).(p^{1},q^{1})=(1.0,1),\quad(p^{2},q^{2})=(1.1,3),\quad(p^{3},q^{3})=(1.2,10). |  |

A trader submits a market buy order for quantity q=5q=5. The exchange matches this order against the resting asks in price–time priority: it first consumes q1=1q\_{1}=1 at p1=1.0p\_{1}=1.0, then q2=3q\_{2}=3 at p2=1.1p\_{2}=1.1, and finally 11 unit from the third order at p3=1.2p\_{3}=1.2.
The total notional paid is 1⋅1.0+3⋅1.1+1⋅1.2=5.51\cdot 1.0+3\cdot 1.1+1\cdot 1.2=5.5, so the execution price is the volume-weighted average pt=5.55=1.1p\_{t}=\frac{5.5}{5}=1.1.
Ignoring fees, the taker acquires a new long position 𝔭=(q,c,t,b)=(5,c,t,+1)\mathfrak{p}=(q,c,t,b)=(5,c,t,+1) with notional exposure q​pt=5.5q\,p\_{t}=5.5.
Aggregating across the three maker accounts, the exchange simultaneously creates an equal and opposite short position 𝔭¯\overline{\mathfrak{p}} of size 55, so that total long and short contract quantities (over all accounts) remain matched.

##### Open Interest.

Note that the notion of leverage is encoded into the quantity qiq\_{i} of a position, as a user who can buy pti​qp\_{t\_{i}}q units of spot assets with cic\_{i} units of collteral can open a position with qi≤ℓmax​qq\_{i}\leq\ell\_{\max}q.
This implies that the correct notion of the notional trades outstanding, known as *interest*, on a pereptuals exchange is simply the sum of price-weighted quantities.
We divide the exchange 𝒫n\mathcal{P}\_{n} into long and short positions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(𝒫n)\displaystyle\mathcal{L}(\mathcal{P}\_{n}) | ={(qi,ci,ti,bi)∈𝒫n:bi=1}\displaystyle=\{(q\_{i},c\_{i},t\_{i},b\_{i})\in\mathcal{P}\_{n}:b\_{i}=1\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮​(𝒫n)\displaystyle\mathcal{S}(\mathcal{P}\_{n}) | ={(qi,ci,ti,bi)∈𝒫n:bi=−1}\displaystyle=\{(q\_{i},c\_{i},t\_{i},b\_{i})\in\mathcal{P}\_{n}:b\_{i}=-1\} |  |

We define the total set of long and short positions as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ¯​(𝒫n)\displaystyle\overline{\mathcal{L}}(\mathcal{P}\_{n}) | =ℒ​(𝒫n)∪{𝔭¯:𝔭∈ℒ​(𝒫n)}\displaystyle=\mathcal{L}(\mathcal{P}\_{n})\cup\{\overline{\mathfrak{p}}:\mathfrak{p}\in\mathcal{L}(\mathcal{P}\_{n})\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮¯​(𝒫n)\displaystyle\overline{\mathcal{S}}(\mathcal{P}\_{n}) | =𝒮​(𝒫n)∪{𝔭¯:𝔭∈𝒮​(𝒫n)}\displaystyle=\mathcal{S}(\mathcal{P}\_{n})\cup\{\overline{\mathfrak{p}}:\mathfrak{p}\in\mathcal{S}(\mathcal{P}\_{n})\} |  |

This is the set of all long and short positions, including matching positions.

Futures exchanges define the *open interest* of the exchange as the total outstanding notional value of the positions held by the exchange.
Given the futures price ptp\_{t}, the long open interest L​(𝒫n,pt)L(\mathcal{P}\_{n},p\_{t}) and short open interest S​(𝒫n,pt)S(\mathcal{P}\_{n},p\_{t}) are defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(𝒫n,pt)\displaystyle L(\mathcal{P}\_{n},p\_{t}) | =∑(qi,ci,ti,bi)∈ℒ​(𝒫n)qi​pt\displaystyle=\sum\_{(q\_{i},c\_{i},t\_{i},b\_{i})\in\mathcal{L}(\mathcal{P}\_{n})}q\_{i}p\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(𝒫n,pt)\displaystyle S(\mathcal{P}\_{n},p\_{t}) | =∑(qi,ci,ti,bi)∈𝒮​(𝒫n)qi​pt\displaystyle=\sum\_{(q\_{i},c\_{i},t\_{i},b\_{i})\in\mathcal{S}(\mathcal{P}\_{n})}q\_{i}p\_{t} |  |

Given the long and short open interest, we define the exchange’s open interest simply as the sum, O​I​(𝒫n,pt)=L​(𝒫n,pt)+S​(𝒫n,pt)OI(\mathcal{P}\_{n},p\_{t})=L(\mathcal{P}\_{n},p\_{t})+S(\mathcal{P}\_{n},p\_{t})
888We note that exchange’s will report open interest over 𝒫¯n\overline{\mathcal{P}}\_{n}, which would be twice the open interest reported here. Since we assume that 𝒫n\mathcal{P}\_{n} is the set of unmatched trader positions, one can view our definition of open interest (which differs from Binance’s definition by a factor of two) as ‘trader open interest’ vs. ‘exchange open interest’.
To lighten notation, we will write Lt=L​(𝒫n,pt),St=S​(𝒫n,pt),O​It=O​I​(𝒫n,pt)L\_{t}=L(\mathcal{P}\_{n},p\_{t}),S\_{t}=S(\mathcal{P}\_{n},p\_{t}),OI\_{t}=OI(\mathcal{P}\_{n},p\_{t}) when the exchange 𝒫n\mathcal{P}\_{n} is already defined.

##### Example.

For 𝒫5\mathcal{P}\_{5} at t=0t=0 with p0=1p\_{0}=1, longs are {A,B,D}\{A,B,D\} and shorts are {C,E}\{C,E\}, so

|  |  |  |
| --- | --- | --- |
|  | L0=∑bi=+1qi​p0=(1+1+1)⋅1=3,S0=∑bi=−1qi​p0=(4+1)⋅1=5,O​I0=8.L\_{0}=\sum\_{b\_{i}=+1}q\_{i}p\_{0}=(1+1+1)\cdot 1=3,\quad S\_{0}=\sum\_{b\_{i}=-1}q\_{i}p\_{0}=(4+1)\cdot 1=5,\quad OI\_{0}=8. |  |

At t=1t=1 with p1=1.4p\_{1}=1.4 (same quantities), L1=3⋅1.4=4.2L\_{1}=3\cdot 1.4=4.2, S1=5⋅1.4=7.0S\_{1}=5\cdot 1.4=7.0, O​I1=11.2OI\_{1}=11.2 .

##### Leverage and Margin.

The *leverage* of a position is the ratio of the notional exposure to the collateral value.
If the leverage is greater than 1, it means that the user has effectively borrowed money from the exchange to have an exposure higher than their cash balance.
When the leverage is less than 1, the user’s position is *overcollateralized*.

As the price of the asset changes, the leverage of the position naturally changes due to its dependence on notional exposure.
When a position is opened, there is an *initial leverage* ratio that the position is created with.
We define the initial leverage of a position as

|  |  |  |
| --- | --- | --- |
|  | ℓi=ℓ​(𝔭i)=ni,tic=pti​qici\ell\_{i}=\ell(\mathfrak{p}\_{i})=\frac{n\_{i,t\_{i}}}{c}=\frac{p\_{t\_{i}}q\_{i}}{c\_{i}} |  |

The larger the initial leverage, the most exposure the trader has to the asset and implicitly, the more risk the exchange is taking on lending to the user.

For risk management purposes, exchanges define leverage limits in terms of initial and maintenance *margins*.
Margins are bounds on the ratio of notional exposure to collateral that the exchange enforces as an invariant.
The *initial margin ratio*, mI∈(0,1)m\_{I}\in(0,1) is defined such that for any valid position, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | mI​pti​qi≤cim\_{I}p\_{t\_{i}}q\_{i}\leq c\_{i} |  | (2) |

This invariant implies that the maximum leverage that a position can have, ℓmax\ell^{\max} is ℓmax=1mI\ell^{\max}=\frac{1}{m\_{I}}.

In order to continually satisfy ([2](https://arxiv.org/html/2512.01112v1#S2.E2 "Equation 2 ‣ Leverage and Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) as spot and future prices change, a trader often needs to ‘top up’ or add more collateral their position.
The amount of collateral needed is related to the exchange’s *maintenance margin ratio* mμm\_{\mu}, which will be defined in the sequel.
As the user adjusts their collateral position dynamically, we let ci,tc\_{i,t} be the total quantity of collateral (margin) placed by the user at time tt.
This also means that the state of position is dynamic, 𝔭i,t=(qi,ci,t,ti,bi)\mathfrak{p}\_{i,t}=(q\_{i},c\_{i,t},t\_{i},b\_{i}).
We define the *leverage at time tt* as ℓi,t=𝟏t≥ti​pt​qici,t\ell\_{i,t}=\mathbf{1}\_{t\geq t\_{i}}\frac{p\_{t}q\_{i}}{c\_{i,t}}

##### Example.

These five examples of 𝒫5\mathcal{P}\_{5} represent one highly overcollateralized and under leveraged position (𝔭A\mathfrak{p}\_{A}), two somewhat leveraged positions with medium leverage (𝔭B,𝔭C\mathfrak{p}\_{B},\mathfrak{p}\_{C}) and two highly leveraged positions (𝔭D,𝔭E\mathfrak{p}\_{D},\mathfrak{p}\_{E}).
We will initialize the example with p0=1p\_{0}=1 and take a maximum leverage ℓmax=10\ell^{\max}=10 (e.g., mI=0.10m\_{I}=0.10).
This gives the following opening leverages:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | ℓA,0\displaystyle\ell\_{A,0} | =1⋅12=0.5,\displaystyle=\tfrac{1\cdot 1}{2}=0.5, | ℓB,0\displaystyle\ell\_{B,0} | =1⋅12/3=1.5,\displaystyle=\tfrac{1\cdot 1}{2/3}=1.5, | ℓC,0\displaystyle\ell\_{C,0} | =1⋅48/3=1.5,\displaystyle=\tfrac{1\cdot 4}{8/3}=1.5, |  |
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | ℓD,0\displaystyle\ell\_{D,0} | =1⋅12/19=9.5,\displaystyle=\tfrac{1\cdot 1}{2/19}=9.5, | ℓE,0\displaystyle\ell\_{E,0} | =1⋅110/99=9.9.\displaystyle=\tfrac{1\cdot 1}{10/99}=9.9. |  | | |

If the mark moves to p1=1.4p\_{1}=1.4 and cash is unchanged (ci,1=cic\_{i,1}=c\_{i}), then time-11 leverages are

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | ℓA,1\displaystyle\ell\_{A,1} | =1.4⋅12=0.7,\displaystyle=\tfrac{1.4\cdot 1}{2}=0.7, | ℓB,1\displaystyle\ell\_{B,1} | =1.4⋅12/3=2.1,\displaystyle=\tfrac{1.4\cdot 1}{2/3}=2.1, | ℓC,1\displaystyle\ell\_{C,1} | =1.4⋅48/3=2.1,\displaystyle=\tfrac{1.4\cdot 4}{8/3}=2.1, |  |
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | ℓD,1\displaystyle\ell\_{D,1} | =1.4⋅12/19=13.3,\displaystyle=\tfrac{1.4\cdot 1}{2/19}=13.3, | ℓE,1\displaystyle\ell\_{E,1} | =1.4⋅110/99=13.86.\displaystyle=\tfrac{1.4\cdot 1}{10/99}=13.86. |  | | |

In practice, if ℓi,1>ℓmax\ell\_{i,1}>\ell^{\max} (e.g., 𝔭D\mathfrak{p}\_{D} and 𝔭E\mathfrak{p}\_{E}), then the venue requires collateral additions from the trader to restore the constraint ℓi,1≤ℓm​a​x\ell\_{i,1}\leq\ell^{max}.

##### Funding Rate.

A perpetual future is only useful as a hedging instrument if the futures price ptp\_{t} and spot price p^t\hat{p}\_{t} are sufficiently “close.”
To incentivize this, the majority of perpetuals futures markets use a continuous payment stream between the long and short positions called a *funding rate*.
If the price of the future is lower than spot, pt<p^tp\_{t}<\hat{p}\_{t}, traders holding short futures positions pay a payment to traders holding long futures positions.
This encourages traders who want to earn these payments to open long positions, which will decrease the over all rate.
Conversely, if pt>p^tp\_{t}>\hat{p}\_{t}, traders holding long positions pay those holding short positions.

Most funding rates are simple linear functions of the relative imbalance between the long and short positions.
A common funding rate [Chitra2025PDLP] formula takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(𝒫n,pt,p^t)=κ​(L​(𝒫n,pt)S​(𝒫n,pt)−ptp^t)\gamma(\mathcal{P}\_{n},p\_{t},\hat{p}\_{t})=\kappa\left(\frac{L(\mathcal{P}\_{n},p\_{t})}{S(\mathcal{P}\_{n},p\_{t})}-\frac{p\_{t}}{\hat{p}\_{t}}\right) |  | (3) |

for a constant κ>0\kappa>0.
For brevity, write γt=γ​(𝒫n,pt,p^t)\gamma\_{t}=\gamma(\mathcal{P}\_{n},p\_{t},\hat{p}\_{t}).
Note that we have defined γt\gamma\_{t} such that if γt>0\gamma\_{t}>0, then short traders pay long traders γt\gamma\_{t}% of their holdings.
This convention is opposite to what many exchanges use (i.e., γt<0\gamma\_{t}<0 represents a payment from the short side to the long side).
However, our convention leads to needing to check fewer negative signs in our formulas, as we will illustrate with our examples.

Given funding rates γt\gamma\_{t} for t≥0t\geq 0, a position 𝔭=(q,c,t,b)\mathfrak{p}=(q,c,t,b) linearly accumulates funding positions between time tt and the current time TT, if the position is solvent.
That is, if the position is solvent at time TT, the user receives a payments of the form

|  |  |  |
| --- | --- | --- |
|  | Γ​((q,c,t,b),t,T)=∑s=t+1T(b​q)​γs​ps\Gamma((q,c,t,b),t,T)=\sum\_{s=t+1}^{T}(bq)\gamma\_{s}p\_{s} |  |

If Γ>0\Gamma>0, then over the interval [t,T][t,T], the user receives a payment from the exchange whereas if Γ<0\Gamma<0, the user pays the exchange.
When the user pays the exchange, their profits are distributed by the exchange to the other side of the market.
For brevity, we use the notation Γi,t,T=Γ​(𝔭i,t,T)\Gamma\_{i,t,T}=\Gamma(\mathfrak{p}\_{i},t,T).

We also note that the funding rate, by construction, is zero-sum when one considers entire set of exchange positions 𝒫¯n\overline{\mathcal{P}}\_{n}.
To see, this note the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑𝔭∈𝒫¯nγt​pt​(b​q)=∑𝔭∈ℒ¯​(𝒫n)γt​pt​(q)−∑𝔭∈𝒮¯​(𝒫n)γt​pt​(q)=0\sum\_{\mathfrak{p}\in\overline{\mathcal{P}}\_{n}}\gamma\_{t}p\_{t}\,(bq)=\sum\_{\mathfrak{p}\in\overline{\mathcal{L}}(\mathcal{P}\_{n})}\gamma\_{t}p\_{t}\,(q)-\sum\_{\mathfrak{p}\in\overline{\mathcal{S}}(\mathcal{P}\_{n})}\gamma\_{t}p\_{t}\,(q)=0 |  | (4) |

where the last equality follows from the fact that 𝔭∈ℒ¯​(𝒫n)⇔𝔭¯∈𝒮¯​(𝒫n)\mathfrak{p}\in\overline{\mathcal{L}}(\mathcal{P}\_{n})\iff\overline{\mathfrak{p}}\in\overline{\mathcal{S}}(\mathcal{P}\_{n}).

##### Example.

To make the linear funding rule concrete, take κ=1\kappa=1 and suppose the oracle and mark follow
(p^0,p0)=(1,1)(\hat{p}\_{0},p\_{0})=(1,1), (p^1,p1)=(1.5,1.4)(\hat{p}\_{1},p\_{1})=(1.5,1.4), (p^2,p2)=(1.25,1.3)(\hat{p}\_{2},p\_{2})=(1.25,1.3), with quantities unchanged (so LS=35\tfrac{L}{S}=\tfrac{3}{5}).
Then with κ=1\kappa=1, γ1=LS−p1p^1=0.6−1.41.5≈−0.3333\gamma\_{1}=\tfrac{L}{S}-\tfrac{p\_{1}}{\hat{p}\_{1}}=0.6-\tfrac{1.4}{1.5}\approx-0.3333 and γ2=0.6−1.31.25=−0.44\gamma\_{2}=0.6-\tfrac{1.3}{1.25}=-0.44 (longs pay shorts at both steps).
Per-step funding cash to each position is γt​pt​(bi​qi)\gamma\_{t}p\_{t}\,(b\_{i}q\_{i}) (positive means received, negative means paid):

|  |  |  |
| --- | --- | --- |
|  | t𝔭A𝔭B𝔭C𝔭D𝔭E00.00000.00000.00000.00000.00001−0.4667−0.4667+1.8667−0.4667+0.46672−0.5720−0.5720+2.2880−0.5720+0.5720\begin{array}[]{c|ccccc}t&\mathfrak{p}\_{A}&\mathfrak{p}\_{B}&\mathfrak{p}\_{C}&\mathfrak{p}\_{D}&\mathfrak{p}\_{E}\\ \hline\cr 0&0.0000&0.0000&0.0000&0.0000&0.0000\\ 1&-0.4667&-0.4667&+1.8667&-0.4667&+0.4667\\ 2&-0.5720&-0.5720&+2.2880&-0.5720&+0.5720\\ \end{array} |  |

Values follow Eq. ([3](https://arxiv.org/html/2512.01112v1#S2.E3 "Equation 3 ‣ Funding Rate. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) using (p^t,pt)(\hat{p}\_{t},p\_{t}) above.

##### Profit and Loss.

Given funding rates, one can write the explicit profit and/or loss that a trader faces during the lifetime of their position.
We define the profit-and-loss (PNL) of duration T>0T>0, 𝖯𝖭𝖫s:T:(R+4×{−1,1})×R+T×R+T→R\mathsf{PNL}\_{s:T}:({\mbox{\bf R}}\_{+}^{4}\times\{-1,1\})\times{\mbox{\bf R}}\_{+}^{T}\times{\mbox{\bf R}}\_{+}^{T}\rightarrow{\mbox{\bf R}} as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖯𝖭𝖫s:T​((q,c,ℓ,t,b),p1:T,p^1:T)=𝟏s≤t<T​(b​q​(pT^−pt)+Γ​((q,c,t,b),t,T^))\mathsf{PNL}\_{s:T}((q,c,\ell,t,b),p\_{1:T},\hat{p}\_{1:T})=\mathbf{1}\_{s\leq t<T}\left(bq(p\_{\hat{T}}-p\_{t})+\Gamma((q,c,t,b),t,\hat{T})\right) |  | (5) |

where T^=min⁡(T,τ)\hat{T}=\min(T,\tau) is the last time the position is solvent.
We will use the shorthand 𝖯𝖭𝖫T=𝖯𝖭𝖫0:T\mathsf{PNL}\_{T}=\mathsf{PNL}\_{0:T}.
We will formally define the quantity τ\tau shortly when we discuss liquidations, but for now think of it as a martingale stopping time for position solvency.
This condition states that the total position of the user is their collateral plus the net change from funding costs.
A natural consequence of the zero-sum nature of funding is that the total PNL is also zero-sum:

|  |  |  |
| --- | --- | --- |
|  | ∑𝔭∈𝒫¯n𝖯𝖭𝖫T​(𝔭,p1:T,p^1:T)=∑𝔭∈𝒫¯nb​q​(pT^−p0)+Γ​(𝔭,t,T^)=0\sum\_{\mathfrak{p}\in\overline{\mathcal{P}}\_{n}}\mathsf{PNL}\_{T}(\mathfrak{p},p\_{1:T},\hat{p}\_{1:T})=\sum\_{\mathfrak{p}\in\overline{\mathcal{P}}\_{n}}bq(p\_{\hat{T}}-p\_{0})+\Gamma(\mathfrak{p},t,\hat{T})=0 |  |

The first term sums to zero, because there will be offsetting positions with b=−1,b=1b=-1,b=1 and the second term is zero via ([4](https://arxiv.org/html/2512.01112v1#S2.E4 "Equation 4 ‣ Funding Rate. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).

##### Example.

Under the additive funding convention in Eq. ([5](https://arxiv.org/html/2512.01112v1#S2.E5 "Equation 5 ‣ Profit and Loss. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) with the prices, open interest, and funding above, PNL over [0,1][0,1] and [0,2][0,2] is:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝖯𝖭𝖫0:1​(𝔭A)\displaystyle\mathsf{PNL}\_{0:1}(\mathfrak{p}\_{A}) | =−0.0667,\displaystyle=-0.0667, | 𝖯𝖭𝖫0:2​(𝔭A)\displaystyle\quad\mathsf{PNL}\_{0:2}(\mathfrak{p}\_{A}) | =−0.7387,\displaystyle=-0.7387, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝖯𝖭𝖫0:1​(𝔭B)\displaystyle\mathsf{PNL}\_{0:1}(\mathfrak{p}\_{B}) | =−0.0667,\displaystyle=-0.0667, | 𝖯𝖭𝖫0:2​(𝔭B)\displaystyle\quad\mathsf{PNL}\_{0:2}(\mathfrak{p}\_{B}) | =−0.7387,\displaystyle=-0.7387, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝖯𝖭𝖫0:1​(𝔭C)\displaystyle\mathsf{PNL}\_{0:1}(\mathfrak{p}\_{C}) | =+0.2667,\displaystyle=+0.2667, | 𝖯𝖭𝖫0:2​(𝔭C)\displaystyle\quad\mathsf{PNL}\_{0:2}(\mathfrak{p}\_{C}) | =+2.9547,\displaystyle=+2.9547, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝖯𝖭𝖫0:1​(𝔭D)\displaystyle\mathsf{PNL}\_{0:1}(\mathfrak{p}\_{D}) | =−0.0667,\displaystyle=-0.0667, | 𝖯𝖭𝖫0:2​(𝔭D)\displaystyle\quad\mathsf{PNL}\_{0:2}(\mathfrak{p}\_{D}) | =−0.7387,\displaystyle=-0.7387, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝖯𝖭𝖫0:1​(𝔭E)\displaystyle\mathsf{PNL}\_{0:1}(\mathfrak{p}\_{E}) | =+0.0667,\displaystyle=+0.0667, | 𝖯𝖭𝖫0:2​(𝔭E)\displaystyle\quad\mathsf{PNL}\_{0:2}(\mathfrak{p}\_{E}) | =+0.7387.\displaystyle=+0.7387. |  |

##### Equity.

For each position 𝔭i,t\mathfrak{p}\_{i,t}, one can view the assets of the position as ci,tc\_{i,t} (e.g. the margin posted by the user) and the liabilities of the users as −𝖯𝖭𝖫T​(𝔭i,t,p1:T,p^1:T)-\mathsf{PNL}\_{T}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T}).
The liabilities are the negative of PNL because if the user has a loss, then they have positive liabilities to the exchange (e.g. they owe the exchange money).
On the other hand, if the user has a gain, then the exchange owes the user money (and is a negative liability).
The *equity* of a position 𝔭i,t\mathfrak{p}\_{i,t}, e​(𝔭i,t)e(\mathfrak{p}\_{i,t}) is simply the assets of the position minus the liabilities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | e​(𝔭i,t,p1,T,p^1,T)=ci,t+𝖯𝖭𝖫T​(𝔭i,t,p1:T,p^1:T)e(\mathfrak{p}\_{i,t},p\_{1,T},\hat{p}\_{1,T})=c\_{i,t}+\mathsf{PNL}\_{T}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T}) |  | (6) |

For notational convenience, we will write the terminal equity shorthand

|  |  |  |
| --- | --- | --- |
|  | eT​(𝔭i,t)=e​(𝔭i,t,p1:T,p^1:T).e\_{T}(\mathfrak{p}\_{i,t})=e(\mathfrak{p}\_{i,t},\ p\_{1:T},\ \hat{p}\_{1:T}). |  |

A position is said to be *totally insolvent* if eT​(𝔭i,t)<0e\_{T}(\mathfrak{p}\_{i,t})<0.
Traders can update their collateral ci,tc\_{i,t} or close positions to avoid fully insolvency.
We define the random variable τ​(𝔭i,t,p1:t)\tau(\mathfrak{p}\_{i,t},p\_{1:t}) as the first time that a position is insolvent, i.e.,

|  |  |  |
| --- | --- | --- |
|  | τ​(𝔭i,t,p1:t)=min⁡{s≤t:e​(𝔭i,s,p1:s)≤μ​ps​qi}\tau(\mathfrak{p}\_{i,t},p\_{1:t})=\min\{s\leq t:e(\mathfrak{p}\_{i,s},p\_{1:s})\leq\mu p\_{s}q\_{i}\} |  |

For any time index tt, we will refer to the *winner* and *loser* index sets as

|  |  |  |
| --- | --- | --- |
|  | 𝒲t={i:e​(𝔭i,t)>0},ℒt={i:e​(𝔭i,t)<0}.\mathcal{W}\_{t}\ =\ \{\,i:\ e(\mathfrak{p}\_{i,t})>0\,\},\qquad\mathcal{L}\_{t}\ =\ \{\,i:\ e(\mathfrak{p}\_{i,t})<0\,\}. |  |

Write their sizes as kt=|𝒲t|k\_{t}=|\mathcal{W}\_{t}| and mt=|ℒt|m\_{t}=|\mathcal{L}\_{t}|. We will use 𝒲T,ℒT\mathcal{W}\_{T},\mathcal{L}\_{T} for the terminal sets at horizon TT.

##### Example.

To illustrate the maintenance test, let μ=0.10\mu=0.10 and reuse the [0,1][0,1] price and funding path above. Equities at t=1t=1 (using ci,1=cic\_{i,1}=c\_{i}) are

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | e​(𝔭A)\displaystyle e(\mathfrak{p}\_{A}) | =2−0.0667≈1.9333,\displaystyle=2-0.0667\approx 1.9333, | e​(𝔭B)\displaystyle e(\mathfrak{p}\_{B}) | =23−0.0667≈0.6000,\displaystyle=\tfrac{2}{3}-0.0667\approx 0.6000, | e​(𝔭C)\displaystyle e(\mathfrak{p}\_{C}) | =83+0.2667≈2.9334,\displaystyle=\tfrac{8}{3}+0.2667\approx 2.9334, |  |
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | e​(𝔭D)\displaystyle e(\mathfrak{p}\_{D}) | =219−0.0667≈0.0386,\displaystyle=\tfrac{2}{19}-0.0667\approx 0.0386, | e​(𝔭E)\displaystyle e(\mathfrak{p}\_{E}) | =1099+0.0667≈0.1677.\displaystyle=\tfrac{10}{99}+0.0667\approx 0.1677. |  | | |

At t=2t=2 (using the same path and ci,2=cic\_{i,2}=c\_{i}), equities are

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | e​(𝔭A)\displaystyle e(\mathfrak{p}\_{A}) | ≈1.2613,\displaystyle\approx 1.2613, | e​(𝔭B)\displaystyle e(\mathfrak{p}\_{B}) | ≈−0.0720,\displaystyle\approx-0.0720, | e​(𝔭C)\displaystyle e(\mathfrak{p}\_{C}) | ≈5.6214,\displaystyle\approx 5.6214, |  |
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | e​(𝔭D)\displaystyle e(\mathfrak{p}\_{D}) | ≈−0.6334,\displaystyle\approx-0.6334, | e​(𝔭E)\displaystyle e(\mathfrak{p}\_{E}) | ≈0.8397.\displaystyle\approx 0.8397. |  | | |

Note that under this price move, there are now negative equity positions that are liquidatable.

##### Maintenance Margin.

As spot and future prices change, an exchange needs to enforce dynamic collateral requirements to avoid insolvencies.
The *maintenance margin ratio*, mμm\_{\mu}, represents the ratio of collateral to notional exposure that a trader must maintain under adverse price moves.
With mμ∈(0,1)m\_{\mu}\in(0,1) and equity from eq. ([6](https://arxiv.org/html/2512.01112v1#S2.E6 "Equation 6 ‣ Equity. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")), a position is maintenance-insolvent (and liquidatable) when

|  |  |  |  |
| --- | --- | --- | --- |
|  | e​(𝔭i,t)≤mμ​pt​|qi|.e(\mathfrak{p}\_{i,t})\ \leq\ m\_{\mu}\,p\_{t}\,|q\_{i}|. |  | (7) |

Note that maintenance margin depends on the equity of a position (e.g. includes the position’s PNL) whereas initial margin only depends on the initial cash position.
If a user violates ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) due to a price move, they can add collateral within a specified time interval to keep their position open.
Otherwise, the venue liquidates the position.

##### Example.

Take mμ=0.10m\_{\mu}=0.10 and reuse the [0,1][0,1] path above with p1=1.4p\_{1}=1.4 and the computed equities

|  |  |  |
| --- | --- | --- |
|  | e​(𝔭A)≈1.9333,e​(𝔭B)≈0.6000,e​(𝔭C)≈2.9334,e​(𝔭D)≈0.0386,e​(𝔭E)≈0.1677.e(\mathfrak{p}\_{A})\approx 1.9333,\quad e(\mathfrak{p}\_{B})\approx 0.6000,\quad e(\mathfrak{p}\_{C})\approx 2.9334,\quad e(\mathfrak{p}\_{D})\approx 0.0386,\quad e(\mathfrak{p}\_{E})\approx 0.1677. |  |

The maintenance thresholds are mμ​p1​|q|=(0.14, 0.14, 0.56, 0.14, 0.14)m\_{\mu}p\_{1}|q|=(0.14,\ 0.14,\ 0.56,\ 0.14,\ 0.14) for (A,B,C,D,E)(A,B,C,D,E). Here e​(𝔭D)≤mμ​p1​|q|e(\mathfrak{p}\_{D})\leq m\_{\mu}p\_{1}|q| while others remain above the threshold.
Position DD is maintenance-insolvent and would need to add collateral or be liquidated.

##### Leverage Mass.

The final quantity we will define aims to measure how much leverage the winning (positive equity) and losing (negative equity) sides have on the exchange.
This will serve as a coarse measure of an exchange’s risk exposure and will be used in §[5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization").
We define a natural aggregate leverage quantity for both the winning and losing sides that normalizes leverage by equity, allowing us to compare traders with very different margin ratios on a common “true asset composition” scale.
For i∈𝒲ti\in\mathcal{W}\_{t} define the *winner effective leverage* λi,t+=ni,te​(𝔭i,t)\lambda^{+}\_{i,t}=\frac{n\_{i,t}}{e(\mathfrak{p}\_{i,t})}, and for i∈ℒti\in\mathcal{L}\_{t} the *loser effective leverage* λi,t−=ni,t|e​(𝔭i,t)|\lambda^{-}\_{i,t}=\frac{n\_{i,t}}{|e(\mathfrak{p}\_{i,t})|}. The *winner* and *loser leverage masses* are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt+=∑i∈𝒲tλi,t+,ℓt−=∑i∈ℒtλi,t−,ℓ¯t±=ℓt±n​(per–trader).\ell^{+}\_{t}\ =\ \sum\_{i\in\mathcal{W}\_{t}}\lambda^{+}\_{i,t},\qquad\ell^{-}\_{t}\ =\ \sum\_{i\in\mathcal{L}\_{t}}\lambda^{-}\_{i,t},\qquad\bar{\ell}^{\pm}\_{t}\ =\ \frac{\ell^{\pm}\_{t}}{n}\ (\text{per--trader}). |  | (8) |

Note that unlike the leverage ℓi,t\ell\_{i,t}, we divide by the equity (which can be larger or smaller than leverage, depending on the trader’s PNL).

##### Example.

Consider t=1t=1 with p1=1.40p\_{1}=1.40. Then ni,1=p1​qi=1.4n\_{i,1}=p\_{1}q\_{i}=1.4 for i∈{A,B,D,E}i\in\{A,B,D,E\} and 5.65.6 for CC.
Using the equities at t=1t=1 above, all five are winners and

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | λA,1+\displaystyle\lambda^{+}\_{A,1} | =1.41.9333≈0.7246,\displaystyle=\tfrac{1.4}{1.9333}\approx 0.7246, | λB,1+\displaystyle\lambda^{+}\_{B,1} | =1.40.6000=2.3333,\displaystyle=\tfrac{1.4}{0.6000}=2.3333, | λC,1+\displaystyle\lambda^{+}\_{C,1} | =5.62.9334≈1.9090,\displaystyle=\tfrac{5.6}{2.9334}\approx 1.9090, |  |
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | λD,1+\displaystyle\lambda^{+}\_{D,1} | =1.40.0386≈36.269,\displaystyle=\tfrac{1.4}{0.0386}\approx 36.269, | λE,1+\displaystyle\lambda^{+}\_{E,1} | =1.40.1677≈8.353.\displaystyle=\tfrac{1.4}{0.1677}\approx 8.353. |  | | |

Hence ℓ1+≈49.59\ell^{+}\_{1}\approx 49.59; the large λD,1+\lambda^{+}\_{D,1} reflects DD’s very small equity at t=1t=1.
Recall DD’s opening leverage was only ℓD,0≈9.5\ell\_{D,0}\approx 9.5, so effective leverage can greatly exceed raw leverage when equity has been eroded by losses.
At t=2t=2 with p2=1.30p\_{2}=1.30, ni,2=p2​|qi|n\_{i,2}=p\_{2}|q\_{i}| equals 1.31.3 for i∈{A,B,D,E}i\in\{A,B,D,E\} and 5.25.2 for CC.
From the equity example above, the winner/loser sets are 𝒲2={A,C,E}\mathcal{W}\_{2}=\{A,C,E\} with eA≈1.2613e\_{A}\approx 1.2613, eC≈5.6214e\_{C}\approx 5.6214, eE≈0.8397e\_{E}\approx 0.8397 and ℒ2={B,D}\mathcal{L}\_{2}=\{B,D\} with eB≈−0.0720e\_{B}\approx-0.0720, eD≈−0.6334e\_{D}\approx-0.6334.
Winner effective leverages are

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | λA,2+\displaystyle\lambda^{+}\_{A,2} | =1.31.2613≈1.031,\displaystyle=\tfrac{1.3}{1.2613}\approx 1.031, | λC,2+\displaystyle\lambda^{+}\_{C,2} | =5.25.6214≈0.925,\displaystyle=\tfrac{5.2}{5.6214}\approx 0.925, | λE,2+\displaystyle\lambda^{+}\_{E,2} | =1.30.8397≈1.548,\displaystyle=\tfrac{1.3}{0.8397}\approx 1.548, |  |

so ℓ2+≈3.504\ell^{+}\_{2}\approx 3.504.
Loser effective leverages are

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | λB,2−\displaystyle\lambda^{-}\_{B,2} | =1.3|−0.0720|≈18.05,\displaystyle=\tfrac{1.3}{|{-}0.0720|}\approx 18.05, | λD,2−\displaystyle\lambda^{-}\_{D,2} | =1.3|−0.6334|≈2.052,\displaystyle=\tfrac{1.3}{|{-}0.6334|}\approx 2.052, |  |

so ℓ2−≈20.102\ell^{-}\_{2}\approx 20.102.
The ratio of leverage masses ℓ2−/ℓ2+≈5.7\ell^{-}\_{2}/\ell^{+}\_{2}\approx 5.7 shows that, at this horizon, most effective leverage sits on the losing side of the book.
Here BB and DD have the same notional ni,2n\_{i,2} but very different effective leverages, illustrating how λi,t±\lambda^{\pm}\_{i,t} can diverge from the raw leverage ℓi,t\ell\_{i,t} when equities differ.

### 2.2 Liquidations

When a user’s position is insolvent, i.e., ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) holds, the exchange must *liquidate* the position — that is, remove some or all of the position from 𝒫n\mathcal{P}\_{n}.
Liquidations are used to ensure that the exchange itself remains solvent, which ensures that traders can withdraw their funds and profits as expected.
The process of liquidating a position is probabilistic, however, and can fail in a number of ways.
We will illustrate the high-level process of liquidation using bankruptcy and liquidation prices.
Then we will describe how exchanges can lose solvency when liquidations fail, leading to the usage of autodeleveraging mechanisms.
Our description of liquidations is minimal, avoiding formal mathematical description unless needed, as we are concerned with liquidations failure versus liquidation mechanics.
We refer the interested reader to [Soska2021BitMEX, perez2021liquidations, qin2021empirical, AngerisChitra2023PerpsSIAM] for detailed accounts of liquidation mechanisms and modeling on centralized and decentralized venues.

#### 2.2.1 Liquidation Prices

Before defining how liquidations work, we need to define the criteria for when a position is eligible for liquidation.
These criteria depend on when certain prices are reached where a trader position has low or negative equity.
We focus on defining three prices: bankruptcy price (zero equity), liquidation price (low equity), and execution price (actual realized price of a liquidation).
In practice, liquidation mechanisms often use more price-based variables to decide on execution.
However, all mechanisms define these three prices, allowing us to abstract liquidations to mechanisms involving these prices.

##### Bankruptcy Price.

The *bankruptcy price* of a position 𝔭i,t\mathfrak{p}\_{i,t}, pb​k​(𝔭i,t)p^{bk}(\mathfrak{p}\_{i,t}), is the highest price at which the position is totally insolvent.
The threshold condition for a position to be totally insolvent is eT​(𝔭i,t)=0e\_{T}(\mathfrak{p}\_{i,t})=0:

|  |  |  |
| --- | --- | --- |
|  | 0=eT​(𝔭i,t)=ci,t+𝖯𝖭𝖫T​(𝔭i,t,p1:T,p^1:T)=ci,t+bi​qi​(pb​k​(𝔭i,t)−pt)+Γ​(𝔭i,t,t,T^)0=e\_{T}(\mathfrak{p}\_{i,t})=c\_{i,t}+\mathsf{PNL}\_{T}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T})=c\_{i,t}+b\_{i}q\_{i}(p^{bk}(\mathfrak{p}\_{i,t})-p\_{t})+\Gamma(\mathfrak{p}\_{i,t},t,\hat{T}) |  |

Rearranging this gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​k​(𝔭i,t)=max⁡(pt−ci,t+Γ​(𝔭i,t,t,T^)bi​qi,0)p^{bk}(\mathfrak{p}\_{i,t})=\max\left(p\_{t}-\frac{c\_{i,t}+\Gamma(\mathfrak{p}\_{i,t},t,\hat{T})}{b\_{i}q\_{i}},0\right) |  | (9) |

One can view the bankruptcy price as the worst-case liquidation price, in the sense that if the position is liquidated at any p<pb​k​(𝔭i,t)p<p^{bk}(\mathfrak{p}\_{i,t}), then other traders of the exchange will realize a loss.
Such a loss, which is either bourne by the exchange or by other traders, is known as *bad debt* (see §[2.3](https://arxiv.org/html/2512.01112v1#S2.SS3 "2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).

The bankruptcy price also constrains the maximum leverage that a position can have.
Suppose that the funding is zero, e.g. Γ​(𝔭i,t,t,T^)=0\Gamma(\mathfrak{p}\_{i,t},t,\hat{T})=0.
The bankruptcy price then simplifies to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​k​(𝔭i,t)=max⁡(pt−ci,tbi​qi,0)=max⁡(pt−biℓi,t​pt,0)=pt​max⁡(1−biℓi,t,0)p^{bk}(\mathfrak{p}\_{i,t})=\max\left(p\_{t}-\frac{c\_{i,t}}{b\_{i}q\_{i}},0\right)=\max\left(p\_{t}-\frac{b\_{i}}{\ell\_{i,t}}\,p\_{t},0\right)=p\_{t}\max\left(1-\frac{b\_{i}}{\ell\_{i,t}},0\right) |  | (10) |

This formula represents the common maxim that a perpetuals position with ℓi≥1\ell\_{i}\geq 1 times leverage will be liquidated when the price moves by 1ℓi\frac{1}{\ell\_{i}}% in the direction opposite to bib\_{i}; see, for example, [Binance2025CollateralLeverageUpdate, he2022fundamentals].
For instance, a maximal 10x leveraged position will be liquidated when the price moves by 10% from the initial price.
Detailed numerical examples of bankruptcy prices are provided in Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization").

##### Liquidation Price.

To avoid bad debt, an exchange defines a *liquidation price* p^l​i​q​(𝔭i,t)≥pb​k​(𝔭i,t)\hat{p}^{liq}(\mathfrak{p}\_{i,t})\geq p^{bk}(\mathfrak{p}\_{i,t}), when the position is liquidatable at time tt.
Generally, the liquidation price is a spot price derived from the oracle versus a futures price quoted by the exchange.
This makes market manipulation — creating and executing non-economically rational orders to force a liquidation — costly to perform.
When the maintenance margin condition ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) is satisfied, the exchange attempts to partially liquidate the position.
The μ\mu-liquidation price, pl​i​q​(𝔭i,t,μ)p^{liq}(\mathfrak{p}\_{i,t},\mu) is defined as the maximal price where ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) holds. To avoid ambiguity about the base price used in pb​kp^{bk}, we write p^l​i​q\hat{p}^{liq} directly in terms of the entry price ptip\_{t\_{i}} (independent of bankruptcy):

|  |  |  |
| --- | --- | --- |
|  | p^l​i​q​(𝔭i,t,μ)={max⁡(pti−(ci,t+Γ​(𝔭i,t,t,T^))/qi1−μ, 0),bi=+1,pti+(ci,t+Γ​(𝔭i,t,t,T^))/|qi|1+μ,bi=−1.\hat{p}^{liq}(\mathfrak{p}\_{i,t},\mu)=\begin{cases}\displaystyle\max\!\left(\frac{\,p\_{t\_{i}}-(c\_{i,t}+\Gamma(\mathfrak{p}\_{i,t},t,\hat{T}))/q\_{i}\,}{1-\mu},\ 0\right),&b\_{i}=+1,\\[10.0pt] \displaystyle\frac{\,p\_{t\_{i}}+(c\_{i,t}+\Gamma(\mathfrak{p}\_{i,t},t,\hat{T}))/|q\_{i}|\,}{1+\mu},&b\_{i}=-1.\end{cases} |  |

Detailed numerical examples of liquidation prices are provided in Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization").

##### Execution Price.

When p^t<pl​i​q​(𝔭i,t,μ)\hat{p}\_{t}<p^{liq}(\mathfrak{p}\_{i,t},\mu) a position is liquidatable. The venue then sells (if bi=+1b\_{i}=+1) or buys (if bi=−1b\_{i}=-1) a slice of size Δ​q\Delta q, realizing an execution price pe​x​e​c​(𝔭i,t,μ,Δ​q)p^{exec}(\mathfrak{p}\_{i,t},\mu,\Delta q).
Whether a liquidation creates bad debt depends on the location of pe​x​e​cp^{exec} relative to the bankruptcy price pb​kp^{bk}:

* •

  *Long* (bi=+1b\_{i}=+1): no shortfall if pe​x​e​c≥pb​kp^{exec}\geq p^{bk}; otherwise the realized shortfall is Dt=(pb​k−pe​x​e​c)​Δ​qD\_{t}=(p^{bk}-p^{exec})\,\Delta q.
* •

  *Short* (bi=−1b\_{i}=-1): no shortfall if pe​x​e​c≤pb​kp^{exec}\leq p^{bk}; otherwise the realized shortfall is Dt=(pe​x​e​c−pb​k)​Δ​qD\_{t}=(p^{exec}-p^{bk})\,\Delta q.

Shortfalls are first absorbed by the insurance fund (§[2.3](https://arxiv.org/html/2512.01112v1#S2.SS3 "2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) up to its balance.
Any residual shortfall not covered by the insurance fund is socialized via ADL (§[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
The choice of liquidation size Δ​q\Delta q and impact parameter α\alpha together determines whether thin-equity positions can typically be closed without realizing bad debt.
Detailed numerical examples of execution prices and shortfalls are provided in Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization").

#### 2.2.2 Liquidation Mechanics

Given liquidation prices, a natural question is how liquidations are mechanically executed.
At a high level, the exchange seizes a low equity position’s cash and collateral and sells it to the market.
Such a sale can realize a profit or a loss for the exchange and is best thought of as a trading strategy itself.
We will provide a high-level description of liquidation mechanisms as trading strategies, with the caveat that there are many idiosyncrasies in practical implementations (see, e.g., [BinanceADL, HyperliquidDocsLiquidations, BitMEXADL] for venue documentation and differences between auctions, order-book liquidations, and RFQ-style closures).

##### Liquidation Costs.

Most exchanges charge penalties to users who are liquidated as a means of disincentivizing liquidations and moral hazard.
These fees come in three flavors: fixed charges, insurance fund fees, and liquidation incentives.
The fixed fees correspond to reimbursement for gas and/or operational costs that an exchange realizes for performing a liquidation.
The insurance fund fees are proportional to the liquidation price and allow for the exchange to cover bad debt.
Finally, the liquidation incentives are used to encourage third-party actors known as liquidators to hold the risk of buying the position of size Δ​q\Delta q from the exchange and exiting it profitably.

In decentralized exchanges, liquidators are usually any market participant with enough capital who can connect to the exchange.
On the other hand, in centralized exchanges, liquidators are usually whitelisted parties approved by the exchange to perform liquidations
We denote the set of liquidation costs for a liquidation of size Δ​q\Delta q at time tt as τt​(Δ​q)∈R+\tau\_{t}(\Delta q)\in{\mbox{\bf R}}\_{+}, which represents the cash cost paid by the user upon liquidation.
Detailed numerical examples of liquidation costs are provided in Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization").

##### Liquidation Strategies.

The policy by which an exchange chooses the liquidation quantity Δ​q\Delta q is known as the *liquidation strategy*, L:𝒫n×R+T×R+T→RL:\mathcal{P}\_{n}\times{\mbox{\bf R}}^{T}\_{+}\times{\mbox{\bf R}}^{T}\_{+}\rightarrow{\mbox{\bf R}}.
The strategy L​(𝔭i,t,p1:T,p^1:T)L(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T}) outputs a quantity Δ​q\Delta q to liquidate.
Generally speaking, the strategy has some model of the environment (e.g. the price impact function of the spot and futures exchanges) and utilizes that to pick the quantity.
Most exchanges utilize a simple a greedy liquidation strategy that chooses the minimal Δ​q\Delta q to ensure that the equity does not satisfy ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
Such strategies choose Δ​q\Delta q such that an equality of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | eT​(𝔭i,t)+b​Δ​q​(pte​x​e​c−pt)−τt​(Δ​q)=μ​pt​(q−Δ​q)e\_{T}(\mathfrak{p}\_{i,t})+b\,\Delta q\,(p^{exec}\_{t}-p\_{t})-\tau\_{t}(\Delta q)=\mu p\_{t}(q-\Delta q) |  | (11) |

approximately holds.
For notational simplicity, we assume that L​(𝔭i,t,p1:T,p^1:T)=0L(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T})=0 if the position 𝔭i,t\mathfrak{p}\_{i,t} is not liquidatable.

As an explicit example, suppose that we have linear price impact, i.e., pe​x​e​c=pt∓α2​Δ​qp^{exec}=p\_{t}\mp\tfrac{\alpha}{2}\,\Delta q.
We receive a quadratic equation in Δ​q\Delta q:

|  |  |  |
| --- | --- | --- |
|  | α2​Δ​q2−μ​pt​Δ​q+(μ​pt​q−eT+τ)= 0,\tfrac{\alpha}{2}\,\Delta q^{2}\;-\;\mu p\_{t}\,\Delta q\;+\;(\mu p\_{t}q-e\_{T}+\tau)\;=\;0, |  |

The greedy liquidation strategy simply takes the smallest feasible root of this quadratic and uses it as the liquidation quantity Δ​q\Delta q.
We refer the reader to Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization") for detailed numerical examples of this strategy and related liquidation procedures.

##### Bad Debt.

A liquidation for position 𝔭i,t\mathfrak{p}\_{i,t} generates *bad debt* if the post-liquidation equity (including execution price and fees) is non-positive.
Formally, we define an adjusted terminal equity e~T​(𝔭i,t,p1:T,p^1:T,Δ​q)\tilde{e}\_{T}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T},\Delta q) that incorporates liquidation costs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | e~T=eT+b​Δ​q​(pe​x​e​c−pt)−τt​(Δ​q)\tilde{e}\_{T}\;=\;e\_{T}\;+\;b\,\Delta q\,\big(p^{exec}-p\_{t}\big)\;-\;\tau\_{t}(\Delta q) |  | (12) |

Intuitively, relative to marking the entire position at ptp\_{t}, realizing a slice Δ​q\Delta q at pe​x​e​cp^{exec} changes equity by the slippage term b​Δ​q​(pe​x​e​c−pt)b\,\Delta q\,(p^{exec}-p\_{t}), and fees reduce equity via τt​(Δ​q)\tau\_{t}(\Delta q).
We say that a liquidation creates bad debt if e~T​(𝔭i,t,p1:T,p^1:T,Δ​q)<0\tilde{e}\_{T}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T},\Delta q)<0, i.e., the liquidation leaves a residual liability for the venue.

Note that in practice, a liquidation strategy might retry or reattempt to liquidate the position repeatedly.
We elide formulating the details of such a liquidation strategy here for simplicity, but note that our model can be easily extended to account for this.
We define the *total bad debt* or *shortfall* of an exchange, DtD\_{t} given a liquidation strategy LL is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(L)=∑𝔭∈𝒫nmax⁡(0,−e~​(𝔭i,t,p1:T,p^1:T,Δ​qi))=∑𝔭∈𝒫n−e~​(𝔭i,t,p1:T,p^1:T,Δ​qi)−D\_{t}(L)=\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}\max(0,-\tilde{e}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T},\Delta q\_{i}))=\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}-\tilde{e}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T},\Delta q\_{i})\_{-} |  | (13) |

where Δ​qi=L​(𝔭i,t,p1:T,p^1:T)\Delta q\_{i}=L(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T}).
This represents the shortfall that the exchange must cover to be solvent (§[2.3](https://arxiv.org/html/2512.01112v1#S2.SS3 "2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
Detailed numerical examples of bad debt are provided in Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization").

eT,ie\_{T,i}equity ranking (k→1k\rightarrow 1)10%10\% liquidation thresholdbankruptcykkk−1k-1k−2k-2⋯\cdots2211liquidatablept=0.88​p0p\_{t}=0.88\,p\_{0}p^t=0.80​p0\hat{p}\_{t}=0.80\,p\_{0}eT,k<0e\_{T,k}<0


(a) Baseline 10% liquidation buffer: mark price pt=0.88​p0p\_{t}=0.88p\_{0} is 10% above bankruptcy p^t=0.80​p0\hat{p}\_{t}=0.80p\_{0}.

eT,ie\_{T,i}equity ranking (k→1k\rightarrow 1)10%10\% liquidation thresholdbankruptcykkk−1k-1k−2k-2⋯\cdots2211pt+Δ=0.94​p0p\_{t+\Delta}=0.94\,p\_{0}p^t+Δ=0.93​p0\hat{p}\_{t+\Delta}=0.93\,p\_{0}all positions solvent


(b) Price recovery: increasing the mark price by Δ​pt=+0.06​p0\Delta p\_{t}=+0.06p\_{0} and the bankruptcy level by Δ​p^t=+0.13​p0\Delta\hat{p}\_{t}=+0.13p\_{0} moves them to pt+Δ=0.94​p0p\_{t+\Delta}=0.94p\_{0} and p^t+Δ=0.93​p0\hat{p}\_{t+\Delta}=0.93p\_{0}, leaving every account with positive equity and a residual mark–bankruptcy buffer of about 1%1\%.

eT,ie\_{T,i}ranking (k→1k\rightarrow 1)bankruptcykkk−1k-1k−2k-2⋯\cdots2211pt=0.88​p0p\_{t}=0.88\,p\_{0}p^t=0.80​p0\hat{p}\_{t}=0.80\,p\_{0}negative equity (insolvent)


(c) Example of a negative-equity account inside the sorted stack.

Figure 1: Sorted equity profiles for stylized liquidation examples. Negative positions (red) appear on the left, positive positions (green) on the right. Dashed lines highlight the bankruptcy level and liquidation triggers.

##### Anatomy of a Liquidation.

Given the bankruptcy, liquidation, and execution prices, we can now describe the high-level algorithm that liquidations follow (see Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization")).
We note that many live liquidation systems will have much more complex liquidation algorithms.
These complexities deal with the coordination costs of coordinating many parties (e.g. oracle provider, liquidators, spot order book liquidity) and precise models that exchanges use for their liquidation strategy.
However, we effectively lump all of these complexities into the definition of the liquidation strategy.
A detailed algorithmic description of the liquidation loop and a step-by-step example are provided in Appendix [A](https://arxiv.org/html/2512.01112v1#A1 "Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization").

### 2.3 Exchange Solvency

In the previous section, we focused on liquidations as a means to remove individual trader solvencies.
However, there is also a ‘macroscopic’ notion of solvency at the exchange level.
The goal of the exchange is to make sure that traders can realize their full profits and losses given the cash collateral held at the exchange.
In rare cases, an exchange might not be able to successfully execute a liquidation strategy, leading to the exchange being unable to pay unrealized but earned profits to some users.

In this section, we define solvency for exchanges and how exchanges use *insurance funds* to try to ensure solvency.
An exchange’s insurance fund is the first line of defense against insolvency.
However, if the insurance fund has insufficient balance, the exchange will need to utilize a autodeleveraging mechanism to socialize losses.
In this section, we will define solvency for exchanges and how insurance funds are constructed.

##### Exchange Solvency.

The *solvency* of an exchange is simply the total equity of all positions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖲𝗈𝗅𝗏T​(𝒫n)=∑𝔭∈𝒫neT​(𝔭)=∑𝔭∈𝒫nc𝔭+𝖯𝖭𝖫T​(𝔭,p1:T,p^1:T)\mathsf{Solv}\_{T}(\mathcal{P}\_{n})=\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}e\_{T}(\mathfrak{p})=\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}c\_{\mathfrak{p}}+\mathsf{PNL}\_{T}(\mathfrak{p},p\_{1:T},\hat{p}\_{1:T}) |  | (14) |

An exchange is said to be *insolvent* if the following condition holds 𝖲𝗈𝗅𝗏T​(𝒫n)≤0\mathsf{Solv}\_{T}(\mathcal{P}\_{n})\leq 0.
The insolvency condition corresponds to when the total cash held by the exchange on behalf of users is less than the total accrued profits.
This mean that if this insolvency condition is hit, the exchange will not be about to payout all profitable traders when they withdraw from the exchange.
Note that this is a global condition on 𝒫n\mathcal{P}\_{n} as opposed to a per user constraint.

Most exchanges have a solvency threshold, δ>0\delta>0, such that if it takes a global loss of δ\delta units of equity to become truly insolvent, then the exchange is deemed approximately insolvent.
This notion of approximate insolvency is useful in practice, as it allows an exchange to have a risk parameter for tuning how aggressively it enters the ADL regime.
Formally, we define an exchange to be δ\delta-insolvent if the following condition holds 𝖲𝗈𝗅𝗏T​(𝒫n)≤δ\mathsf{Solv}\_{T}(\mathcal{P}\_{n})\leq\delta.

##### Comparison to overcollateralized lending.

In overcollateralized lending, where a user uses one crypto asset as collateral to borrow another crypto asset, there is a similar notion of a user’s equity position.
However, in overcollateralized lending, the user’s equity position is not global, but rather is local to the user.
The goal of a lending protocol is to ensure that the equity el​e​n​d​(p)≥0e\_{lend}(p)\geq 0 for *every* user’s position pp.
Ensuring per account solvency condition inherently forces overcollateralized lending protocols to offer far lower leverage than perpetuals exchanges.
From a mathematical standpoint, perpetual solvency is easier to satisfy, allowing for higher leverage — there is only one global constraint that has to hold versus O​(n)O(n) local constraints for nn users.
However, in perpetuals exchanges, users who are solvent can face losses from users who are insolvent which cannot happen in isolated overcollateralized lending markets like Morpho.

##### Insurance Funds.

Many exchanges maintain an insurance fund to cover bad debt that arises from failed liquidations.
When a positive shortfall Dt>0D\_{t}>0 is realized, the insurance fund is used to reduce DtD\_{t} to as close to zero as possible.
The insurance fund is typically funded using a portion of the exchange’s revenue from transaction, liquidation, and funding fees.

Insurance reserves in crypto funds were first popularized alongside perpetual futures in the mid-2010s (notably on BitMEX) [Soska2021BitMEX].
A majority of perpetuals venues (centralized and on-chain) maintain such reserves (e.g. BitMEX [BitMEXADL], Binance [BinanceFuturesInsuranceFund], Drift [DriftADLCode], Bybit [BybitInsuranceFund]).
To illustrate the size of these funds, we note that mid-2025 estimates place OKX and Bybit insurance funds at roughly $300M and $150M, respectively [OKXBybitInsuranceComparison].

We will first provide a simple model for how the insurance fund evolves over time.
Let 𝖨𝖥t≥0\mathsf{IF}\_{t}\geq 0 denote the insurancefund balance at time tt.
Furthermore, let 𝒯t\mathcal{T}\_{t} be the multiset of liquidations at time tt with sizes {Δ​qj}j∈𝒯t\{\Delta q\_{j}\}\_{j\in\mathcal{T}\_{t}} and execution costs τt​(Δ​qj)∈R+\tau\_{t}(\Delta q\_{j})\in{\mbox{\bf R}}\_{+} (cf. eq. ([12](https://arxiv.org/html/2512.01112v1#S2.E12 "Equation 12 ‣ Bad Debt. ‣ 2.2.2 Liquidation Mechanics ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"))).
Let Vt≥0V\_{t}\geq 0 denote the gross traded volume (absolute quantity) in the contract at time tt.
We introduce three parameters to model insurance fund growth: α,β,η∈[0,1]\alpha,\beta,\eta\in[0,1].
The α,β,η\alpha,\beta,\eta parameters controls how much of liquidation, funding, and trading fee revenue is added 𝖨𝖥t\mathsf{IF}\_{t}, respectively.

Given these parameters, the time evolution of the insurance fund is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖨𝖥t+1=𝖨𝖥t+α​∑j∈𝒯tτt​(Δ​qj)+η​pt​Vt+β​∑i=1n|γt|​pt​qi−min⁡{𝖨𝖥t,Dt}\mathsf{IF}\_{t+1}=\mathsf{IF}\_{t}+\alpha\sum\_{j\in\mathcal{T}\_{t}}\tau\_{t}(\Delta q\_{j})+\eta\,p\_{t}V\_{t}+\beta\sum\_{i=1}^{n}|\gamma\_{t}|\,p\_{t}\,q\_{i}-\min\{\mathsf{IF}\_{t},\,D\_{t}\} |  | (15) |

Note that the positive contributions represent the revenue sharing terms whereas the negative contribution represents the cover of a shortfall using the insurance fund.

The main quantity of interest, given 𝖨𝖥t\mathsf{IF}\_{t}, is the *residual shortfall*.
This represents the amount of bad debt that cannot be covered by the insurance fund and needs to be socialized via ADL (§[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
Formally, we define the residual shortfall as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=Dt−min⁡{𝖨𝖥t,Dt}=(Dt−𝖨𝖥t)+R\_{t}=D\_{t}-\min\{\mathsf{IF}\_{t},\,D\_{t}\}=(D\_{t}-\mathsf{IF}\_{t})\_{+} |  | (16) |

We note that when Rt>0R\_{t}>0, an ADL mechanism is triggered.

##### Example.

Continuing from the previous liquidation example, the bad debt realized at t=4t=4 by 𝔭E\mathfrak{p}\_{E} is

|  |  |  |
| --- | --- | --- |
|  | D4=(pEe​x​e​c−pb​k​(𝔭E,4))​Δ​qE≈ 0.399.D\_{4}\;=\;(p^{exec}\_{E}-p^{bk}(\mathfrak{p}\_{E,4}))\,\Delta q\_{E}\;\approx\;0.399. |  |

Let 𝖨𝖥4\mathsf{IF}\_{4} denote the pre-coverage fund balance. The coverage is min⁡{𝖨𝖥4,D4}\min\{\mathsf{IF}\_{4},D\_{4}\} and the ADL residual is R4=(D4−𝖨𝖥4)+R\_{4}=(D\_{4}-\mathsf{IF}\_{4})\_{+}.
We assume that the fund evolves via eq. ([15](https://arxiv.org/html/2512.01112v1#S2.E15 "Equation 15 ‣ Insurance Funds. ‣ 2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) and model liquidation fees as affine in notional size:

|  |  |  |
| --- | --- | --- |
|  | τt​(Δ​q)=τf​i​x+ϕm​a​r​k​pt​Δ​q+ϕe​x​e​c​pte​x​e​c​Δ​q,\tau\_{t}(\Delta q)=\tau^{fix}+\phi^{mark}\,p\_{t}\,\Delta q+\phi^{exec}\,p^{exec}\_{t}\,\Delta q, |  |

where τf​i​x\tau^{fix} is a fixed fee and ϕm​a​r​k,ϕe​x​e​c\phi^{mark},\phi^{exec} are proportional rates on mark and execution price, respectively.
Using the Hyperliquid fee schedule (τf​i​x,ϕm​a​r​k,ϕe​x​e​c)=(0,20​bps,10​bps)(\tau^{fix},\phi^{mark},\phi^{exec})=(0,20\,\mathrm{bps},10\,\mathrm{bps}) (see §[2.2.2](https://arxiv.org/html/2512.01112v1#S2.SS2.SSS2 "2.2.2 Liquidation Mechanics ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")), the fees are

|  |  |  |
| --- | --- | --- |
|  | τ4​(Δ​qE)=0+20⋅10−4⋅p4​Δ​qE+10⋅10−4⋅pEe​x​e​c​Δ​qE≈0.00365.\tau\_{4}(\Delta q\_{E})=0+20\cdot 10^{-4}\cdot p\_{4}\,\Delta q\_{E}+10\cdot 10^{-4}\cdot p^{exec}\_{E}\,\Delta q\_{E}\approx 0.00365. |  |

Assuming γ4=0\gamma\_{4}=0 and neglecting trading volume V4V\_{4} for simplicity:

* •

  *Sufficiently sized fund (R4=0R\_{4}=0).* If 𝖨𝖥4≥D4\mathsf{IF}\_{4}\geq D\_{4}, the debt is fully covered. No ADL occurs. The balance updates to

  |  |  |  |
  | --- | --- | --- |
  |  | 𝖨𝖥5=𝖨𝖥4+α​τ4​(Δ​qE)−D4.\mathsf{IF}\_{5}=\mathsf{IF}\_{4}+\alpha\,\tau\_{4}(\Delta q\_{E})-D\_{4}. |  |
* •

  *Insufficiently sized fund (R4>0R\_{4}>0).* If 𝖨𝖥4<D4\mathsf{IF}\_{4}<D\_{4}, the fund is depleted to zero and pays 𝖨𝖥4\mathsf{IF}\_{4}. The residual R4=D4−𝖨𝖥4R\_{4}=D\_{4}-\mathsf{IF}\_{4} is socialized via ADL (§[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")). The new balance is simply the inflows:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝖨𝖥5=α​τ4​(Δ​qE).\mathsf{IF}\_{5}=\alpha\,\tau\_{4}(\Delta q\_{E}). |  |

Increasing α\alpha, β\beta, or η\eta builds 𝖨𝖥t\mathsf{IF}\_{t} faster, reducing the probability of Rt>0R\_{t}>0.

##### Optimal Insurance Fund Size.

A natural question to ask is, what is the optimal size for an insurance fund?
While this question is nuanced in practice, we provide a simple mean-field model that provide some intuition.
In particular, we determine the optimal fund size K∗K^{\*} by minimizing a total cost function that balances the opportunity cost of capital against the expected franchise damage from ADL events.
Let r>0r>0 denote the opportunity cost of holding capital (e.g., the risk-free rate) and κ>0\kappa>0 denote the reputation cost per unit of socialized loss (reflecting lost future volume).
The exchange minimizes

|  |  |  |
| --- | --- | --- |
|  | minK≥0⁡r​K+κ​𝐄[(DT−K)+].\min\_{K\geq 0}\;rK+\kappa\,\mathop{\bf E{}}[(D\_{T}-K)\_{+}]. |  |

This is a classic newsvendor-type problem [ArrowHarrisMarschak1951].
Classical result show that the optimal size is the Value-at-Risk of the deficit distribution at quantile 1−r/κ1-r/\kappa:

|  |  |  |
| --- | --- | --- |
|  | K∗=VaR1−r/κ​(DT)=inf{x:𝐏𝐫𝐨𝐛(DT≤x)≥1−r/κ}.K^{\*}\;=\;\text{VaR}\_{1-r/\kappa}(D\_{T})\;=\;\inf\{x:\mathop{\bf Prob}(D\_{T}\leq x)\geq 1-r/\kappa\}. |  |

For completeness, we provide a derivation in Appendix [A.8](https://arxiv.org/html/2512.01112v1#A1.SS8 "A.8 Optimal Capital Structure Derivation ‣ Appendix A Liquidations, Autodeleveraging, and Insurance Funds ‣ Autodeleveraging: Impossibilities and Optimization").
Intuitively, as the reputation cost κ\kappa increases relative to the cost of capital rr, the exchange holds a larger buffer to push ADL events further into the tail.

### 2.4 Autodeleveraging

Any mechanism for reducing or closing profitable user positions to reduce an exchange’s insolvency is termed *autodeleveraging* (ADL).
Mathematically, ADL mechanisms attempt to liquidating positions in order to reduce the residual RtR\_{t}.
This inherently means that users with positive equity (e.g. are profitable) will be forced to close their positions and not realize their full profit.

We first note that ADL mechanisms are not deterministic and foolproof.
For example, if an exchange is already insolvent, 𝖲𝗈𝗅𝗏T​(𝒫n)≤0\mathsf{Solv}\_{T}(\mathcal{P}\_{n})\leq 0, then no deterministic ADL mechanism can return solvency.
To see this, we define four key quantifies, the total shortfall DT​(𝒫n)D\_{T}(\mathcal{P}\_{n}), the maximum shortfall ΔT​(𝒫n)\Delta\_{T}(\mathcal{P}\_{n}), the total winner’s equity WT​(𝒫n)W\_{T}(\mathcal{P}\_{n}), and the max-winner ωT​(𝒫n)\omega\_{T}(\mathcal{P}\_{n}):

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | DT​(𝒫n)\displaystyle D\_{T}(\mathcal{P}\_{n}) | =∑𝔭∈𝒫n(−eT​(𝔭))+≥0\displaystyle=\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}\big(-e\_{T}(\mathfrak{p})\big)\_{+}\geq 0 | ΔT​(𝒫n)\displaystyle\Delta\_{T}(\mathcal{P}\_{n}) | =max𝔭∈𝒫n⁡(−eT​(𝔭)−)≥0\displaystyle=\max\_{\mathfrak{p}\in\mathcal{P}\_{n}}\big(-e\_{T}(\mathfrak{p})\_{-}\big)\geq 0 |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | WT​(𝒫n)\displaystyle W\_{T}(\mathcal{P}\_{n}) | =∑𝔭∈𝒫neT​(𝔭)+≥0\displaystyle=\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}e\_{T}(\mathfrak{p})\_{+}\geq 0 | ωT​(𝒫n)\displaystyle\omega\_{T}(\mathcal{P}\_{n}) | =max𝔭∈𝒫n⁡eT​(𝔭)+≥0\displaystyle=\max\_{\mathfrak{p}\in\mathcal{P}\_{n}}e\_{T}(\mathfrak{p})\_{+}\geq 0 |  |

For notational simplicity, we will use Roman letters for total quantities and Greek letters for maximum or extreme value quantities.
The shortfall represents the total amount of negative equity whereas the winners’ equity represents the total amount of positive equity.
By definition, 𝖲𝗈𝗅𝗏T​(𝒫n)=WT​(𝒫n)−DT​(𝒫n)\mathsf{Solv}\_{T}(\mathcal{P}\_{n})=W\_{T}(\mathcal{P}\_{n})-D\_{T}(\mathcal{P}\_{n}), so if 𝖲𝗈𝗅𝗏T​(𝒫n)≤0\mathsf{Solv}\_{T}(\mathcal{P}\_{n})\leq 0, then DT​(𝒫n)≥WT​(𝒫n)D\_{T}(\mathcal{P}\_{n})\geq W\_{T}(\mathcal{P}\_{n}), i.e., no amount of forced liquidations of positive equity can cover the shortfall.

Instead, ADL mechanisms attempt to liquidate a fraction of the shortfall, then allow the market to react for some time (e.g. for users to close positions or post more margin and spot prices to update), before attempting a future deleveraging (if needed).
This means that the ADL process should be viewed probabilistically, as a sequence of decisions that are dynamically adjusted based on market conditions.
We will demonstrate that from this perspective, ADL can be formulated as a standard reinforcement learning problem.

##### ADL Policies.

The fundamental object of reinforcement learning is the policy, which maps states of the world to actions.
For ADL, the positions 𝒫n\mathcal{P}\_{n} serve as the state space, whereas the actions are the fraction of shortfall to socialize and which positions are socialized.
While the majority of exchanges (e.g. Binance and Hyperliquid) use queue-based policies that greedily rank positions by PNL and leverage, we will define a formalism over a larger class of potential ADL policies.
This larger class will enable us to find more efficient and fair ADL policies than queue-based models and includes pro-rata ADL policies used by smaller exchanges such as Drift and Paradex.

An *ADL policy* π​(𝒫n)\pi(\mathcal{P}\_{n}) maps a perpetuals exchange to a fraction of shortfall to socialize, θ∈[0,1]\theta\in[0,1], and a set of haircuts to apply to positions, h∈[0,1]nh\in[0,1]^{n}.
We term the fraction θ\theta the *severity* of the ADL policy.
For notational convenience we define θπ,hπ\theta\_{\pi},h\_{\pi} as the severity and haircuts induced by an ADL policy π\pi.
We say an ADL policy π\pi if *valid* if the following three constraints always hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑𝔭∈𝒫nhπ,i​eT​(𝔭)+=θπ​DT​(𝒫n)=−∑𝔭∈𝒫nhπ,i​eT​(𝔭)−.\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}h\_{\pi,i}e\_{T}(\mathfrak{p})\_{+}=\theta\_{\pi}D\_{T}(\mathcal{P}\_{n})=-\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}h\_{\pi,i}e\_{T}(\mathfrak{p})\_{-}. |  | (17) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | θπ​DT​(𝒫n)≤WT​(𝒫n).\theta\_{\pi}D\_{T}(\mathcal{P}\_{n})\leq W\_{T}(\mathcal{P}\_{n}). |  | (18) |

where pip\_{i} is the iith trader’s position.
The first two conditions ([17](https://arxiv.org/html/2512.01112v1#S2.E17 "Equation 17 ‣ ADL Policies. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) ensure that when an ADL policy is executed, only a θ\theta% of the deficit is socialized from the winners to the losers (i.e., a budget balance constraint).
The third condition ([18](https://arxiv.org/html/2512.01112v1#S2.E18 "Equation 18 ‣ ADL Policies. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) ensures that θπ\theta\_{\pi} is chosen such that one does not need to haircut more equity than what the winners have (i.e., a feasibility constraint).
We define the post-policy deficit DTπD^{\pi}\_{T}, winners WTπW^{\pi}\_{T}, and max-winner MTπM^{\pi}\_{T} as

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | DTπ\displaystyle D^{\pi}\_{T} | =θπ​DT​(𝒫n)\displaystyle=\theta\_{\pi}D\_{T}(\mathcal{P}\_{n}) | ΔTπ\displaystyle\Delta^{\pi}\_{T} | =θπ​ΔT​(𝒫n)\displaystyle=\theta\_{\pi}\Delta\_{T}(\mathcal{P}\_{n}) |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | WTπ\displaystyle W^{\pi}\_{T} | =∑𝔭∈𝒫n(1−hπ,i)​(eT​(𝔭))+\displaystyle=\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}(1-h\_{\pi,i})(e\_{T}(\mathfrak{p}))\_{+} | ωTπ\displaystyle\omega^{\pi}\_{T} | =max𝔭∈𝒫n⁡(1−hπ,i)​(eT​(𝔭))+\displaystyle=\max\_{\mathfrak{p}\in\mathcal{P}\_{n}}(1-h\_{\pi,i})(e\_{T}(\mathfrak{p}))\_{+} |  |

Our goal is to construct policies that minimize an objective function that balances individual user profits with global exchange solvency.

Given an ADL policy outputting (θπ,hπ)(\theta\_{\pi},h\_{\pi}), the positive equity positions 𝒲T={i:eT​(𝔭i)>0}\mathcal{W}\_{T}=\{i:e\_{T}(\mathfrak{p}\_{i})>0\} are haircut by hπ,ih\_{\pi,i}, leading to equities eT​(𝔭i)←(1−hπ,i)​eT​(𝔭i)e\_{T}(\mathfrak{p}\_{i})\leftarrow(1-h\_{\pi,i})e\_{T}(\mathfrak{p}\_{i}) for i∈𝒲Ti\in\mathcal{W}\_{T}.
For instance, if we have equities eT=(10,5,−5)e\_{T}=(10,5,-5) and the ADL policy outputs haircuts (0.5,0,−1)(0.5,0,-1), then the post-ADL equities are eT=(5,5,0)e\_{T}=(5,5,0).
On the other hand, if the ADL policy outputs haircuts h=(0.25,0.5,−1)h=(0.25,0.5,-1), then the final equities after execution of the policy are eT=(7.5,2.5,0)e\_{T}=(7.5,2.5,0).

##### Examples of ADL Policies.

We will first provide two canonical examples: queueing (or *leverage ranking*) and pro-rata.
These examples represent the solvency policies of virtually all live perpetuals exchanges as of November 2025.
For both of these policies, the choice of θπ\theta\_{\pi} is independent of the choice of hπh\_{\pi}.

##### PNL and Leverage Ranking.

The policy that the largest centralized exchange, Binance, and the largest decentralized exchange, Hyperliquid, use is the PNL-leverage ranking (which we also refer to as a *queueing* method).
We will denote this strategy as πP​L\pi\_{PL} and define it via the algorithm that implements it.
Given a haircut budget B=θπP​L​DT​(𝒫n)B=\theta\_{\pi\_{PL}}D\_{T}(\mathcal{P}\_{n}), the algorithm to choose hih\_{i} works as follows:

1. 1.

   For each position 𝔭=(q,c,ℓ,t,b)∈𝒫n\mathfrak{p}=(q,c,\ell,t,b)\in\mathcal{P}\_{n}, define the score999We note that technically, many exchanges define the leverage used in the score differently (i.e., instead of the score being linear in ℓ\ell, some exchanges multiply by ℓ​p​qp​q+c)\frac{\ell pq}{pq+c}). This does not change our main results and mainly adds technical complications to the example. sT​(𝔭,pr​e​f)=ℓ​p^Tpr​e​fs\_{T}(\mathfrak{p},p^{ref})=\ell\,\frac{\hat{p}\_{T}}{p^{ref}}.
2. 2.

   Let σ∈𝖯𝖾𝗋𝗆​(𝒫n)\sigma\in\mathsf{Perm}(\mathcal{P}\_{n}) be any permutation of the positions ranked by decreasing score sT​(𝔭,pr​e​f)s\_{T}(\mathfrak{p},p^{ref})
3. 3.

   For i∈[n]i\in[n], define Ai=(B−∑j=1ieT​(𝔭σ​(j))+)+A\_{i}=(B-\sum\_{j=1}^{i}e\_{T}(\mathfrak{p}\_{\sigma(j)})\_{+})\_{+}, where eT​(𝔭σ​(j))e\_{T}(\mathfrak{p}\_{\sigma(j)}) is the equity of the jjth largest position under the ranking σ\sigma
4. 4.

   Define h∈[0,1]nh\in[0,1]^{n} as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | hπP​L,σ​(i)={1if ​Ai−1−Ai=eT​(𝔭σ​(i))+,Ai>0Ai−1eT​(𝔭σ​(i))if ​Ai=0,Ai−1>00otherwiseh\_{\pi\_{PL},\sigma(i)}=\begin{cases}1&\text{if }A\_{i-1}-A\_{i}=e\_{T}(\mathfrak{p}\_{\sigma(i)})\_{+},\;A\_{i}>0\\ \frac{A\_{i-1}}{e\_{T}(\mathfrak{p}\_{\sigma}(i))}&\text{if }A\_{i}=0,A\_{i-1}>0\\ 0&\text{otherwise}\end{cases} |  | (19) |

Note this definition of hπP​Lh\_{\pi\_{PL}} ensures that ∑i=1nhπP​L,i​eT​(𝔭i)=B\sum\_{i=1}^{n}h\_{\pi\_{PL},i}e\_{T}(\mathfrak{p}\_{i})=B, satisfying ([17](https://arxiv.org/html/2512.01112v1#S2.E17 "Equation 17 ‣ ADL Policies. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
On the other hand, since we only subtract positive equity positions (e.g. jj such that eT​(𝔭σ​(j))+>0e\_{T}(\mathfrak{p}\_{\sigma(j)})\_{+}>0), we satisfy ([18](https://arxiv.org/html/2512.01112v1#S2.E18 "Equation 18 ‣ ADL Policies. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) by construction.

There is one remaining question to address: how should we interpret the score sT​(𝔭,pr​e​f)s\_{T}(\mathfrak{p},p^{ref})?
Most exchanges justify this form for the score by arguing that it can represent the risk a single position holds, so that the exchange ranks positions to ADL by risk-level.
Winning, positive equity positions that are autodeleveraged first will tend to be higher risk positions (i.e., used more leverage for their winnings).
The price terms in the numerator, pT^p\_{\hat{T}}, represents the last mark price of the position whereas the parameter pr​e​fp^{ref} represents the initial or opening price of the user.

Binance chooses the scoring parameter pr​e​f=pb​kp^{ref}=p^{bk} of the position, i.e.,sTBinance​(𝔭)=ℓ​pT^​(𝔭)pb​k​(𝔭)s^{\text{Binance}}\_{T}(\mathfrak{p})=\ell\frac{p\_{\hat{T}}(\mathfrak{p})}{p^{bk}(\mathfrak{p})}.
Hyperliquid, on the other hand, chooses the parameter pr​e​fp^{ref} to simply be the last mark price, pr​e​f=p^tp^{ref}=\hat{p}\_{t}.
In other words, Binance’s choice effectively ranks a position based on the maximum possible PNL that a user could realize whereas Hyperliquid simply chooses the current PNL.

##### Pro-Rata Rules.

This haircut strategy is even simpler than the PNL-Leverage ranking and has some benefits in terms of fairness, as we will show in §[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization").
Given a valid feasible shortfall θπ​DT​(𝒫n≤WT​(𝒫n))\theta\_{\pi}D\_{T}(\mathcal{P}\_{n}\leq W\_{T}(\mathcal{P}\_{n})), the pro-rata haircut policy is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hπP​R​(𝔭)=θπ​DT​(𝒫n)WT​(𝒫n)​(eT​(𝔭))+h\_{\pi\_{PR}}(\mathfrak{p})=\frac{\theta\_{\pi}D\_{T}(\mathcal{P}\_{n})}{W\_{T}(\mathcal{P}\_{n})}(e\_{T}(\mathfrak{p}))\_{+} |  | (20) |

This ranking simply says that the positive equity positions are socialized proportional to their size.
Some exchanges slightly modify this formula to include leverage (e.g., Binance’s ADL Priority Index includes leverage and unrealized PNL [BinanceADL]; Aevo documentation discusses leverage-weighted priority [AevoADL]), which penalizes higher leverage positions much like the PNL-leverage ranking:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hπL​P​R​(𝔭)=(ℓ​eT​(𝔭)+∑𝔭∈𝒫nℓ​eT​(𝔭)+)​hπP​R​(𝒫n)h\_{\pi\_{LPR}}(\mathfrak{p})=\left(\frac{\ell e\_{T}(\mathfrak{p})\_{+}}{\sum\_{\mathfrak{p}\in\mathcal{P}\_{n}}\ell e\_{T}(\mathfrak{p})\_{+}}\right)h\_{\pi\_{PR}}(\mathcal{P}\_{n}) |  | (21) |

eT,ie\_{T,i}ranking (k→1k\rightarrow 1)kkk−1k-1k−2k-2⋯\cdots2211deficithaircutqueuehaircutseverity θ=0.50\theta=0.50

(a) Queue ADL:
  
all haircuts fall on the highest-ranked winner.

eT,ie\_{T,i}ranking (k→1k\rightarrow 1)kkk−1k-1k−2k-2⋯\cdots2211deficithaircutpro-rata haircutsseverity θ=0.50\theta=0.50

(b) Pro-rata ADL:
  
haircuts are shared across the surviving winners.

Figure 2: ADL severity example comparing queue and pro-rata coloring. Purple shading equals the negative equity mass (deficit) while blue shading shows the haircut mass allocated to winning traders. The queue panel’s dashed blue block at rank 2 highlights residual equity when the queue method allows partial closures; exchanges that close winners fully (e.g., Hyperliquid) would shave this bar completely. Haircut mass matches deficit mass in each panel, illustrating severity θ=0.50\theta=0.50.

##### Per-account constraints.

Suppose that one wants to enforce some per-account constraints on the amount haircut.
For instance, suppose that we guarantee that for user ii, their haircut hih\_{i} always satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi≤h¯ih\_{i}\leq\overline{h}\_{i} |  | (22) |

This corresponds to an exchange guaranteeing that a user will never lose more than h¯i\overline{h}\_{i}% of their position in a single ADL round.
Moreover, an exchange might also offer an absolute guarantee to users: if your equity is positive and sufficiently large, you will never be have your equity cut to below some threshold e¯i\underline{e}\_{i}.
This can be represented by the constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−hπ,i)​eT​(𝔭i)≥e¯i(1-h\_{\pi,i})e\_{T}(\mathfrak{p}\_{i})\geq\underline{e}\_{i} |  | (23) |

Numerous exchanges offer one or both of these guarantees on a per-ADL-round basis, including Hyperliquid, BitMEX, and Aevo [HyperliquidDocsLiquidations, BitMEXADL, AevoADL].

##### Numerical example.

Consider five accounts with equities eT=(10,5,1,−3,−12)e\_{T}=(10,5,1,-3,-12) and queue order σ=(2,1,3,5,4)\sigma=(2,1,3,5,4) induced by the PNL-leverage scores.
Let the queue policy choose severity θπP​L=12\theta\_{\pi\_{PL}}=\tfrac{1}{2}, so the haircut budget is B=θπP​L​DT​(𝒫n)=7.5B=\theta\_{\pi\_{PL}}D\_{T}(\mathcal{P}\_{n})=7.5.
The construction in ([19](https://arxiv.org/html/2512.01112v1#S2.E19 "Equation 19 ‣ Item 4 ‣ PNL and Leverage Ranking. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) yields A=(2.5,0,0,0,0)A=(2.5,0,0,0,0) and haircuts h=(0.25,1,0,0,0)h=(0.25,1,0,0,0): the top winner is cut from 1010 to 7.57.5, the second winner is fully wiped out, and the remaining accounts are unchanged, giving eT=(7.5,0,1,−3,−4.5)e\_{T}=(7.5,0,1,-3,-4.5).
If, before the next ADL decision, only the losing accounts partially recover to eT=(7.5,0,1,−1.5,−2.25)e\_{T}=(7.5,0,1,-1.5,-2.25), then a second round at the same severity θπP​L=12\theta\_{\pi\_{PL}}=\tfrac{1}{2} autodeleverages all negative-equity accounts against the largest winner, yielding final equities eT=(3.75,0,1,0,0)e\_{T}=(3.75,0,1,0,0).
Under the pro-rata rule ([20](https://arxiv.org/html/2512.01112v1#S2.E20 "Equation 20 ‣ Pro-Rata Rules. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) with the same severity θπP​R=12\theta\_{\pi\_{PR}}=\tfrac{1}{2}, we have DT=15D\_{T}=15 and WT=16W\_{T}=16, so the uniform haircut factor is α=θπP​R​DT/WT=15/32\alpha=\theta\_{\pi\_{PR}}D\_{T}/W\_{T}=15/32 and each winning account’s equity is scaled by (1−α)=17/32(1-\alpha)=17/32, giving eT=(170/32,85/32,17/32,−3,−12)e\_{T}=(170/32,85/32,17/32,-3,-12).
In particular, the ranking of positive-equity accounts is preserved under pro-rata, since all winners are multiplied by the same constant factor, illustrating its rank-preservation property.

### 2.5 ADL Trilemma

The preceding subsections defined trader equity, exchange solvency, insurance funds, and autodeleveraging (ADL) policies.
In this subsection we introduce a high–level design principle that organizes the rest of the paper: an *ADL trilemma*.
Informally, a perpetuals venue cannot simultaneously (i) keep insolvency and ADL breach events rare, (ii) protect solvent winners from large socialized losses, and (iii) extract maximal long–run exchange revenue from trading and funding activity.
Any ADL design must pick (at most) two of these three goals.

##### Exchange revenue.

To define the trilemma, we have to first formally describe what constitutes exchange revenue.
Recall from §[2.3](https://arxiv.org/html/2512.01112v1#S2.SS3 "2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization") that, given parameters α,β,η∈[0,1]\alpha,\beta,\eta\in[0,1], the insurance fund I​FtIF\_{t}
evolves by

|  |  |  |
| --- | --- | --- |
|  | I​Ft+1=I​Ft+α​∑j∈Ttτt​(Δ​qj)+η​pt​Vt+β​∑i=1n|γt|​pt​|qi|−min⁡{I​Ft,Dt},IF\_{t+1}=IF\_{t}+\alpha\sum\_{j\in T\_{t}}\tau\_{t}(\Delta q\_{j})+\eta\,p\_{t}V\_{t}+\beta\sum\_{i=1}^{n}|\gamma\_{t}|\,p\_{t}|q\_{i}|-\min\{IF\_{t},D\_{t}\}, |  |

where TtT\_{t} is the multiset of liquidations at tt, VtV\_{t} is traded volume, γt\gamma\_{t} is the funding rate, and DtD\_{t} is the period bad debt.
For notational convenience, define the per–period gross fee flows

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝖥𝖾𝖾tliq\displaystyle\mathsf{Fee}^{\text{liq}}\_{t} | =∑j∈Ttτt​(Δ​qj)\displaystyle=\sum\_{j\in T\_{t}}\tau\_{t}(\Delta q\_{j}) | 𝖥𝖾𝖾ttrade=pt​Vt\displaystyle\mathsf{Fee}^{\text{trade}}\_{t}=p\_{t}V\_{t} | 𝖥𝖾𝖾tfund=∑i=1n|γt|​pt​|qi|.\displaystyle\mathsf{Fee}^{\text{fund}}\_{t}=\sum\_{i=1}^{n}|\gamma\_{t}|\,p\_{t}|q\_{i}|. |  |

Most exchanges fully collect liquidation and trading fees and potentially collect fees on funding rates.101010In particular, we note that HLP-like systems where fees are charged on quoting offsetting positions can be viewed as a form of exchange revenue [HyperliquidHLPVaults]. Moreover, a number of perpetuals AMM DEXs collect protocol revenue from funding flows [GMXDocs, PerpV2Docs].

Let ζ≤(1−β)\zeta\leq(1-\beta) be the expected fraction of funding rates that the exchange keeps as revenue.
Then the exchange’s *gross revenue* at time tt is

|  |  |  |
| --- | --- | --- |
|  | 𝖱𝖾𝗏𝖾𝗇𝗎𝖾tgross=𝖥𝖾𝖾tliq+𝖥𝖾𝖾ttrade+ζ​𝖥𝖾𝖾tfund.\mathsf{Revenue}^{\text{gross}}\_{t}=\mathsf{Fee}^{\text{liq}}\_{t}+\mathsf{Fee}^{\text{trade}}\_{t}+\zeta\mathsf{Fee}^{\text{fund}}\_{t}. |  |

By construction, the fractions α,η,β\alpha,\eta,\beta of these fee flows are diverted into the
insurance fund. The remaining share accrues as *net exchange revenue*

|  |  |  |
| --- | --- | --- |
|  | 𝖱𝖾𝗏𝖾𝗇𝗎𝖾t:=(1−α)𝖥𝖾𝖾tliq+(1−η)𝖥𝖾𝖾ttrade+(1−β−ζ)𝖥𝖾𝖾tfund.\mathsf{Revenue}\_{t}:=(1-\alpha)\,\mathsf{Fee}^{\text{liq}}\_{t}+(1-\eta)\,\mathsf{Fee}^{\text{trade}}\_{t}+(1-\beta-\zeta)\,\mathsf{Fee}^{\text{fund}}\_{t}. |  |

We note that in §[8](https://arxiv.org/html/2512.01112v1#S8 "8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization") that we refine this notion of revenue to a discounted *exchange long–term value* (LTV).
The LTV accounts for future expected fee flows and traders leaving the exchange as a function of the realized ADL haircuts.

##### Three competing desiderata.

There are three main goals that an ADL policy aims to enforce for traders and exchanges: revenue, solvency, and fairness.
We formalize these notions in the sequel:

* •

  *Solvency.* (§[4](https://arxiv.org/html/2512.01112v1#S4 "4 Severity Optimization ‣ Autodeleveraging: Impossibilities and Optimization"), §[5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization")) The exchange aims to ensure that Rt=0R\_{t}=0 for most times tt and that the total shortfall ∑tRt\sum\_{t}R\_{t} is small relative to the expected insurance fund size.
  This desideratum is beneficial to both the exchange and traders.
* •

  *Fairness and moral hazard.* (§[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization"), §[7](https://arxiv.org/html/2512.01112v1#S7 "7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization"))
  Traders want to know that if they face socialization, they will not be asked to absorb a portion of RtR\_{t} that is too large relative to their notional exposure on the exchange.
  This desideratum is mainly beneficial to traders.
* •

  *Exchange revenue and participation.* (§[8](https://arxiv.org/html/2512.01112v1#S8 "8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization"))
  Heavy ADL on high–value winners can trigger traders exiting the exchange permanently, shrinking future fee flows.
  This desideratum is mainly beneficial to the exchange.

It is clear that α,β,η\alpha,\beta,\eta and the ADL policy π\pi jointly control these three dimensions.
But a natural question is what the trade-offs are between these three desiderata at different values of α,β,η\alpha,\beta,\eta and parametrizations of π\pi.
Raising α,β,η\alpha,\beta,\eta builds the reserve faster and decreases breaches (i.e., times with Rt>0R\_{t}>0), but diverts exchange revenue into the fund.
Increasing ADL severity (or concentrating haircuts) makes breaches rarer and accelerates solvency, but worsens fairness and drives away the highest–value winning traders.
Keeping severities (i.e., total solvency resolved by ADL) small preserves fairness and participation, but leaves the exchange exposed to repeated shortfalls.
The goal of this paper is to formalize these three statements via a trilemma:

###### Proposition 2.1 (Trilemma, Informal).

Fix a sequence of perpetuals exchanges 𝒫n\mathcal{P}\_{n} and static ADL policies πn\pi\_{n} with insurance parameters (α,β,η)(\alpha,\beta,\eta).
Under the heavy-tailed shortfall assumptions of §[5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization"), no policy family (πn)(\pi\_{n}) can simultaneously satisfy the following uniformly in nn:

1. (S)

   Solvency: Residual risk is controlled, i.e.,, ∑tRt​(πn)=Op​(1)\sum\_{t}R\_{t}(\pi\_{n})=O\_{p}(1) and ℙ​[Rt​(πn)>0]=O​(1)\mathbb{P}[R\_{t}(\pi\_{n})>0]=O(1).
2. (F)

   Fairness: Moral hazard is bounded, i.e.,, ωTπ/DTπ=Θ​(1)\omega^{\pi}\_{T}/D^{\pi}\_{T}=\Theta(1) and ωTπ/ΔTπ=Θ​(1)\omega^{\pi}\_{T}/\Delta^{\pi}\_{T}=\Theta(1).
3. (R)

   Revenue: Exchange revenue is preserved relative to a benchmark, i.e.,, LTV​(πn)≍LTVbenchmark\text{LTV}(\pi\_{n})\asymp\text{LTV}\_{\text{benchmark}}.

Enforcing (S) requires sacrificing (F) (via concentrated haircuts) or (R) (via excessive insurance diversion). Conversely, preserving (F) and (R) necessitates frequent solvency breaches.

A formal statement with precise definitions and a complete proof of the proposition appears in Appendix [I](https://arxiv.org/html/2512.01112v1#A9 "Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization").

##### Proof sketch and roadmap.

The remainder of the paper establishes the Trilemma by analyzing each desideratum in turn:

* •

  *Solvency Ratios (§[5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization"), Appendix [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization")).*
  We analyze the ratio ωTπ/DTπ\omega^{\pi}\_{T}/D^{\pi}\_{T} under heavy-tailed assumptions.
  Theorem [B.3](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem3 "Theorem B.3 (PTSR scaling). ‣ B.4 Asymptotic Scaling Results ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") proves that for any budget-balanced static ADL with severity θn\theta\_{n}, the ratio scales as bn/(θn​n)b\_{n}/(\theta\_{n}n).
  Consequently, enforcing rare breaches (large θn\theta\_{n}) drives the ratio to zero, violating (F).
* •

  *Fairness Models (§[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")–§[7](https://arxiv.org/html/2512.01112v1#S7 "7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization"), Appendices [C](https://arxiv.org/html/2512.01112v1#A3 "Appendix C Theoretical Properties of Capped Pro-Rata ‣ Autodeleveraging: Impossibilities and Optimization")–[E.2](https://arxiv.org/html/2512.01112v1#A5.SS2 "E.2 RAP Optimality and Convex Dominance ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization")).*
  We formalize fairness in two regimes.
  First, for a single round (§[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")), we show that capped pro-rata is the unique policy satisfying Sybil resistance and monotonicity.
  Second, under external shocks (§[7](https://arxiv.org/html/2512.01112v1#S7 "7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization")), we prove that leverage-weighted rules (RAP) minimize future shortfall but sacrifice the most systemically important winners, highlighting the tension between short-term robustness and long-term participation.
* •

  *Revenue and Price of Anarchy (§[8](https://arxiv.org/html/2512.01112v1#S8 "8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization"), Appendix [F.3](https://arxiv.org/html/2512.01112v1#A6.SS3 "F.3 Stackelberg vs. Nash in a Two-Round ADL Game ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization")).*
  We model the revenue-solvency tradeoff as a Stackelberg game between the exchange and traders.
  We show that static severities yield an unbounded Price of Anarchy (Jn​(π)∼θn​n/bnJ\_{n}(\pi)\sim\theta\_{n}n/b\_{n}) compared to dynamic policies.
  This confirms that achieving (R) and (S) simultaneously requires dynamic intervention, as static rules cannot balance the trilemma asymptotically.

## 3 Risk and Fairness Preliminaries

To analyze how different ADL policies balance solvency and winner survival, we require metrics that capture both the *magnitude* of losses (risk) and their *distribution* across traders (fairness).
Classical risk measures like Value-at-Risk (VaR) and Expected Shortfall (ES) quantify aggregate solvency but ignore how the burden is shared.
To address this, we introduce fairness-aware metrics and distributional orderings that allow us to rank policies based on how they concentrate or spread losses among winners.
We then provide with an brief presentation of extreme-value scaling that we use in the sequel, before concluding with a brief introduction to algorithmic fairness.
The preliminaries in this section are meant to be incomplete and we refer the reader to the literature cited for more details.

### 3.1 Risk Metrics

#### 3.1.1 Traditional Risk Metrics

We briefly review standard metrics used in finance and regulation [Boyd2017MultiPeriodTrading, BCBS2019FRTB].
For a loss X≥0X\geq 0 and confidence level α∈(0,1)\alpha\in(0,1):

* •

  *Value-at-Risk (VaR):* The quantile VaRα​(X)=inf{x:𝐏𝐫𝐨𝐛(X>x)≤α}\mathrm{VaR}\_{\alpha}(X)=\inf\{x:\mathop{\bf Prob}(X>x)\leq\alpha\}.
* •

  *Expected Shortfall (ES):* The average loss in the worst α\alpha-fraction of cases, ESα​(X)=𝐄[X∣X≥VaRα​(X)]\mathrm{ES}\_{\alpha}(X)=\mathop{\bf E{}}[X\mid X\geq\mathrm{VaR}\_{\alpha}(X)].

In ADL, we apply these to the residual shortfall RtR\_{t} to measure solvency risk.

#### 3.1.2 ADL-Specific Efficiency Metrics

To capture the trade-off between solvency and trader welfare, we define two ratios that normalize winner survival by the scale of the default:

* •

  *Profitability-to-Total-Solvency Ratio (PTSR):*

  |  |  |  |
  | --- | --- | --- |
  |  | 𝖯𝖳𝖲𝖱T​(π)=𝐄[ωTπDTπ].\mathsf{PTSR}\_{T}(\pi)=\mathop{\bf E{}}\left[\frac{\omega^{\pi}\_{T}}{D^{\pi}\_{T}}\right]. |  |

  This measures the survival of the top winner relative to the total socialized loss. A low PTSR indicates that the most profitable trader is being disproportionately cannibalized to cover deficits.
* •

  *Profitability-to-Maximum Solvency Ratio (PMR):*

  |  |  |  |
  | --- | --- | --- |
  |  | 𝖯𝖬𝖱T​(π)=𝐄[ωTπΔTπ].\mathsf{PMR}\_{T}(\pi)=\mathop{\bf E{}}\left[\frac{\omega^{\pi}\_{T}}{\Delta^{\pi}\_{T}}\right]. |  |

  This compares the top winner’s equity to the largest single loser’s shortfall, capturing the concentration of risk on both sides of the trade.

These ratios mirror the VaR/ES distinction: PTSR captures aggregate efficiency, while PMR captures tail concentration.
We formalize this connection and derive exact relationships in Appendix [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").

### 3.2 Fairness and Distributional Comparisons

While scalar metrics like PTSR provide summary statistics, they cannot fully capture the fairness of a policy across the entire population of winners.
Two policies might achieve similar solvency but distribute the pain very differently—one by wiping out a few large winners (Queue), another by shaving everyone slightly (Pro-Rata).
To rank policies robustly, we use tools from majorization theory [MarshallOlkinArnold2011].

##### Schur-Convexity and Submajorization.

We compare haircut vectors h∈Rnh\in{\mbox{\bf R}}^{n} using *submajorization* (≺w\prec\_{w}).
We say a policy πA\pi\_{A} is *more fair* (or less concentrated) than πB\pi\_{B} if its haircut vector is submajorized by πB\pi\_{B}’s, i.e., h​(πA)≺wh​(πB)h(\pi\_{A})\prec\_{w}h(\pi\_{B}).
This implies that for *any* convex cost function ϕ\phi (representing trader disutility), the aggregate distress is lower under πA\pi\_{A}:

|  |  |  |
| --- | --- | --- |
|  | h​(πA)≺wh​(πB)⟹∑ϕ​(hi​(πA))≤∑ϕ​(hi​(πB)).h(\pi\_{A})\prec\_{w}h(\pi\_{B})\implies\sum\phi(h\_{i}(\pi\_{A}))\leq\sum\phi(h\_{i}(\pi\_{B})). |  |

This gives us a powerful, parameter-free way to claim that Pro-Rata is “fairer” than Queue: it minimizes the collective pain for all convex risk attitudes.
We provide a detailed treatment of these orderings and their application to ADL in Appendix [E.2](https://arxiv.org/html/2512.01112v1#A5.SS2.SSS0.Px2 "RAP realizes Schur-convex dominance. ‣ E.2 RAP Optimality and Convex Dominance ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization").

##### Comonotonicity.

In our worst-case analysis, we often consider *comonotonic* couplings, where winners’ profits and losers’ deficits are perfectly correlated (move in lockstep).
This represents the most dangerous regime for ADL, as large deficits coincide with large winner profits, testing the policy’s ability to extract liquidity without destroying the best traders.
Our negative results in §[5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization") exploit this structure to derive tight bounds on the Trilemma.
See Appendix [E.2](https://arxiv.org/html/2512.01112v1#A5.SS2.SSS0.Px2 "RAP realizes Schur-convex dominance. ‣ E.2 RAP Optimality and Convex Dominance ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization") for further details on comonotonic risk bounds.

### 3.3 Extreme–value scaling

Our asymptotic analysis relies on *extreme–value scales*: deterministic sequences that characterize the typical magnitude of the largest winner equity and the largest loser shortfall in the limit of a large market.
Recall the winner and loser index sets 𝒲T\mathcal{W}\_{T} and ℒT\mathcal{L}\_{T} with cardinalities knk\_{n} and mnm\_{n}, respectively.
Under mild mixing we assume the aggregate winner and loser masses concentrate at linear scales:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (WT​(𝒫n)n,DT​(𝒫n)n)→𝑝(μ+,μ−).\left(\frac{W\_{T}(\mathcal{P}\_{n})}{n},\,\frac{D\_{T}(\mathcal{P}\_{n})}{n}\right)\xrightarrow{p}(\mu\_{+},\mu\_{-}). |  | (24) |

Here μ+,μ−>0\mu\_{+},\mu\_{-}>0 summarize the average winner and loser magnitudes.
We define the respective maxima as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ωT,ΔT)=(maxi∈𝒲T(eT(𝔭i,T))+,maxi∈ℒT(−eT(𝔭i,T))+).\big(\omega\_{T},\,\Delta\_{T}\big)=\left(\max\_{i\in\mathcal{W}\_{T}}\big(e\_{T}(\mathfrak{p}\_{i,T})\big)\_{+},\,\max\_{i\in\mathcal{L}\_{T}}\big(-e\_{T}(\mathfrak{p}\_{i,T})\big)\_{+}\right). |  | (25) |

A pair of deterministic, increasing sequences {bk+}k≥1\{b^{+}\_{k}\}\_{k\geq 1} and {bm−}m≥1\{b^{-}\_{m}\}\_{m\geq 1} constitute *extreme–value scales* if there exist constants c+,c−∈(0,∞)c\_{+},c\_{-}\in(0,\infty) such that, as n→∞n\to\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ωTbkn+,ΔTbmn−)→𝑝(c+,c−).\left(\frac{\omega\_{T}}{b^{+}\_{k\_{n}}},\,\frac{\Delta\_{T}}{b^{-}\_{m\_{n}}}\right)\xrightarrow{p}(c\_{+},c\_{-}). |  | (26) |

We abbreviate bn=bkn+b\_{n}=b^{+}\_{k\_{n}} when the context (winner side) is unambiguous.
A canonical choice, consistent with classical extreme–value theory, is the set of *upper–quantile normalizers*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (bk+,bm−)=(F+−1​(1−1k),F−−1​(1−1m)).\big(b^{+}\_{k},\,b^{-}\_{m}\big)=\left(F\_{+}^{-1}\!\left(1-\frac{1}{k}\right),\,F\_{-}^{-1}\!\left(1-\frac{1}{m}\right)\right). |  | (27) |

where F+F\_{+} and F−F\_{-} denote the distribution functions of winner-side positive equities and loser-side shortfalls, respectively.

##### Examples.

Two prototypical cases appear throughout our analysis:

* •

  *Light tails (sub–Gaussian).* For distributions with sub–Gaussian scales σ+,σ−\sigma\_{+},\sigma\_{-},

  |  |  |  |
  | --- | --- | --- |
  |  | bk+≍σ+​2​log⁡k,bm−≍σ−​2​log⁡m.b^{+}\_{k}\ \asymp\ \sigma\_{+}\sqrt{2\log k},\qquad b^{-}\_{m}\ \asymp\ \sigma\_{-}\sqrt{2\log m}. |  |
* •

  *Power–law tails (Pareto/Fréchet).* For distributions satisfying 𝐏𝐫𝐨𝐛{(eT)+>x}∼C+​x−α+\mathop{\bf Prob}\{(e\_{T})\_{+}>x\}\sim C\_{+}x^{-\alpha\_{+}} and 𝐏𝐫𝐨𝐛{(−(eT))+>x}∼C−​x−α−\mathop{\bf Prob}\{(-(e\_{T}))\_{+}>x\}\sim C\_{-}x^{-\alpha\_{-}} with α±>0\alpha\_{\pm}>0,

  |  |  |  |
  | --- | --- | --- |
  |  | bk+≍(C+​k)1/α+,bm−≍(C−​m)1/α−.b^{+}\_{k}\ \asymp\ (C\_{+}k)^{1/\alpha\_{+}},\qquad b^{-}\_{m}\ \asymp\ (C\_{-}m)^{1/\alpha\_{-}}. |  |

##### Extreme–value severity scales.

We refer to θn=Θ​(bn/n)\theta\_{n}=\Theta(b\_{n}/n) as the *extreme–value severity scale*.
This choice aligns the haircut magnitude with the typical largest winner equity bn=bkn+b\_{n}=b^{+}\_{k\_{n}} in a large market where kn=Θ​(n)k\_{n}=\Theta(n).
Theorem [B.3](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem3 "Theorem B.3 (PTSR scaling). ‣ B.4 Asymptotic Scaling Results ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") (Appendix [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization")) demonstrates that this scale is canonical: for any budget-balanced ADL with total severity H=θn​DTH=\theta\_{n}D\_{T}, the PTSR scales asymptotically as bkn+/(θn​n)b^{+}\_{k\_{n}}/(\theta\_{n}n).
Consequently, parameter choices on the extreme–value scale preserve non-degenerate efficiency limits, whereas aggressive severities θn≫bkn+/n\theta\_{n}\gg b^{+}\_{k\_{n}}/n drive the PTSR to zero.

### 3.4 Fairness

##### Algorithmic Fairness in ADL.

Algorithmic fairness literature distinguishes between *axiomatic* approaches, which posit structural invariants (often yielding impossibility results [Arrow1951, KleinbergEtAl2018FairnessImpossibility]), and *optimization* approaches, which minimize disparate impact via convex programs [DworkEtAl2012FairnessAwareness].
ADL spans both: queue-based policies resemble discrete ranking mechanisms subject to Arrow-style impossibilities, while pro-rata policies admit continuous convex formulations.
We adopt an axiomatic perspective to characterize “ideal” fairness, then relax it to optimize for robustness.

##### Axiomatic Properties.

We formalize three operational desiderata for fair ADL policies:

* •

  *Sybil Resistance:* Splitting an account into multiple smaller positions (or merging them) should not alter the aggregate haircut. This ensures outcomes depend on total exposure, not identity or fragmentation. Queue-based rules violate this, as splitting a large winner can push parts of its equity lower in the priority stack.
* •

  *Monotonicity (Stable Ordering):* The policy should preserve the relative ordering of winners. If trader AA has more equity than trader BB pre-ADL, AA should also have more equity post-ADL. This prevents arbitrary re-ranking of survivors.
* •

  *Scale Invariance:* If all deficits and equities scale by λ>0\lambda>0, the relative haircuts should remain unchanged. This ensures the mechanism responds to *leverage* and *risk distribution*, not nominal sizes.

In §[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization"), we prove that *capped pro-rata* is the unique policy satisfying all three properties, whereas standard queueing fails Sybil resistance and monotonicity.

### 3.5 Moral hazard

Moral hazard is a generic incentive problem that arises when one party (the *agent*) can take actions that affect risk or payoffs, but those actions are not perfectly observable, verifiable, or contractible by the party bearing some of the downside (the *principal*); see, e.g. Holmstrom1982, LaffontMartimort2002.
Classic examples include workers choosing effort under wage contracts, managers taking portfolio risk on behalf of investors, or insurers providing coverage to policyholders whose behavior may change once insured.
Because the agent’s action is hidden, the principal cannot simultaneously provide full insurance (so that the agent’s payoff is insulated from shocks) and preserve strong incentives for the agent to take socially desirable actions: risk sharing necessarily distorts effort incentives.
The central goal of the moral-hazard literature is therefore to characterize *second-best* contracts (typically linear or otherwise simple sharing rules) that optimally trade off incentive provision against insurance under information constraints [DuttingEtAl2023MultiAgentContracts, Carroll2015RobustLinearContracts].

In modern treatments, moral hazard also interacts with robustness and model uncertainty: the principal designs contracts that must perform well across a range of environments, counterparty types, or effort technologies, which further limits how close one can get to the idealized first-best benchmark [DuttingEtAl2023MultiAgentContracts].
In financial systems, these issues appear whenever risk is mutualized or losses are socialized across participants: for example, in insurance pools and in centrally cleared derivatives, where default funds and loss-sharing rules can weaken incentives for individual risk management.
Our ADL setting can be viewed as an instance of this general template, with winners and losers in the market acting as principals who provide mutual insurance and the exchange acting as an agent choosing risk and loss-sharing policies; the negative results in Section [5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization") make this second-best trade-off precise in our model.

## 4 Severity Optimization

We decompose the ADL problem into two orthogonal components: *severity* (how much to socialize) and *haircuts* (who pays).
Solvency is driven almost entirely by the scalar severity sequence (θt)(\theta\_{t}), while fairness and revenue depend on the haircut distribution hth\_{t}.
Since §[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")–§[7](https://arxiv.org/html/2512.01112v1#S7 "7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization") cover haircut design, here we focus on optimizing θt\theta\_{t} to balance solvency against the risk of driving away traders.

##### Severity Policies.

A *causal severity policy* maps available information ℱt\mathcal{F}\_{t} (deficits, funding rates, risk limits) to a severity fraction θt∈[0,1]\theta\_{t}\in[0,1].
We contrast three approaches:

1. 1.

   *Static Interpolation:* θt\theta\_{t} is fixed or linearly interpolates between deficit-matching and full queue liquidation. This is simple but rigid.
2. 2.

   *Exponential Backoff:* θt=θ0​αkt\theta\_{t}=\theta\_{0}\alpha^{k\_{t}} decays as the number of recent shocks ktk\_{t} increases. This prevents cascading failures from wiping out the entire book during prolonged stress.
3. 3.

   *Online Control (Mirror Descent):* We treat severity selection as an online convex optimization problem. The controller adjusts θt\theta\_{t} to minimize a regret bound combining solvency costs (RtR\_{t}) and revenue loss (excessive haircuts). This approach adapts to non-stationary market conditions and respects caps Θt\Theta\_{t} derived from the Price of Anarchy analysis in §[8](https://arxiv.org/html/2512.01112v1#S8 "8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization").

##### Separation Principle.

Under the budget-balance constraint ([17](https://arxiv.org/html/2512.01112v1#S2.E17 "Equation 17 ‣ ADL Policies. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")), any one-round ADL policy π\pi with severity θπ\theta\_{\pi} and haircuts hπh\_{\pi} satisfies

|  |  |  |
| --- | --- | --- |
|  | H​(π)=∑ihπ,i​eT​(𝔭i)+=θπ​DT​(𝒫n),H(\pi)\;=\;\sum\_{i}h\_{\pi,i}\,e\_{T}(\mathfrak{p}\_{i})\_{+}\;=\;\theta\_{\pi}D\_{T}(\mathcal{P}\_{n}), |  |

so the post-ADL deficit is

|  |  |  |
| --- | --- | --- |
|  | RT​(π)=(DT​(𝒫n)−H​(π))+=(1−θπ)+​DT​(𝒫n),R\_{T}(\pi)\;=\;(D\_{T}(\mathcal{P}\_{n})-H(\pi))\_{+}\;=\;(1-\theta\_{\pi})\_{+}D\_{T}(\mathcal{P}\_{n}), |  |

which depends only on θπ\theta\_{\pi} and DT​(𝒫n)D\_{T}(\mathcal{P}\_{n}), not on how H​(π)H(\pi) is distributed across winners.
Thus, any solvency functional that depends on π\pi only via {Rt​(π)}t\{R\_{t}(\pi)\}\_{t} (e.g., breach frequencies, VaR/ES of ∑tRt\sum\_{t}R\_{t}) can be optimized over the scalar sequence (θt)(\theta\_{t}), holding the haircut rule fixed.
Conversely, fairness and revenue functionals depend on the winner-side post-ADL equities {(1−hπ,i)​eT​(𝔭i)+}i\{(1-h\_{\pi,i})e\_{T}(\mathfrak{p}\_{i})\_{+}\}\_{i} and are invariant to the choice of θt\theta\_{t} once the total budget HtH\_{t} is fixed.
We exploit this separability in our numerics (§[9](https://arxiv.org/html/2512.01112v1#S9 "9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization")) by tuning θt\theta\_{t} (severity control) and hth\_{t} independently.

## 5 Negative Results

We begin with two structural limits for ADL.
They formalize a moral-hazard trade-off between solvency and winner payoffs that cannot be removed by better policy design.
The tension is instantaneous and zero-sum at the shock: covering aggregate deficit DTD\_{T} eventually requires shaving the profits of the best winner.
We first argue that this tension can be viewed as a form of moral hazard, in the sense used in principal-agent contracts.

An exchange that earns fees from trading volume has an incentive to let very risky, highly leveraged users accumulate large positions.
When these users default, their negative equity shows up as a large deficit DTD\_{T}, which is then socialized onto the winners via ADL haircuts.
In our model this is the basic moral-hazard question: the exchange enjoys fee revenue from risky losers, while the cost of their tail losses is borne by solvent winners.
The results below quantify how this wedge scales as the market thickens, showing that the severity needed for solvency grows with the number of positions and with the leverage imbalance between losers and winners.

### 5.1 Impossibility of Avoiding Moral Hazard as n→∞n\to\infty

We first show that the tension between solvency and winner survival scales unfavorably with market size, creating an unavoidable moral hazard wedge.
Viewing traders as principals and the exchange as an agent, preserving the agent’s utility (solvency) asymptotically destroys the principals’ utility (winner profits) unless severity vanishes.

##### Example.

Consider a book of size nn where loser positions are i.i.d. with mean loss μ>0\mu>0, so aggregate deficit scales as DT≈μ​nD\_{T}\approx\mu n.
Suppose the top winner’s equity scales sub-linearly, e.g., bn∼c​log⁡nb\_{n}\sim c\log n (light tails).
If the exchange commits to a fixed severity θ¯>0\bar{\theta}>0 to maintain solvency, the total haircut budget is Hn≈θ¯​μ​nH\_{n}\approx\bar{\theta}\mu n.
As n→∞n\to\infty, this linear haircut cost overwhelms the logarithmic winner equity:

|  |  |  |
| --- | --- | --- |
|  | enpost≈(c​log⁡n−θ¯​μ​n)+→0.e\_{n}^{\text{post}}\approx(c\log n-\bar{\theta}\mu n)\_{+}\to 0. |  |

Thus, to preserve any winner profit, severity must vanish at the rate θn=O​(bn/n)\theta\_{n}=O(b\_{n}/n).
Constant severity policies therefore represent a form of growing moral hazard: they transfer an increasingly large share of tail risk from the exchange to the most profitable traders.
We formalize this scaling in Appendix [B.6](https://arxiv.org/html/2512.01112v1#A2.SS6 "B.6 Randomized constructions for moral-hazard examples ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").

##### Main Result.

In our model, socialization is instantaneously zero-sum: every dollar of deficit DTD\_{T} covered by ADL must come from the winners’ equity.
If ADL usage does not vanish as the market grows larger (n→∞n\rightarrow\infty), then one cannot simultaneously keep deficits small (solvency, low DTD\_{T}) and preserve winner payoffs (high ωT\omega\_{T}).
The proposition below quantifies this tradeoff in terms of extreme-value scales and can be read as a moral-hazard impossibility result in the principal–agent sense.

###### Proposition 5.1 (Informal).

Suppose that the extreme value scale of the winning trader’s equity, ωTπ​(𝒫n)\omega\_{T}^{\pi}(\mathcal{P}\_{n}), is bnb\_{n}.
Then,

|  |  |  |
| --- | --- | --- |
|  | 𝖯𝖳𝖲𝖱T​(𝒫n,π)=𝐄π[ωTπ​(𝒫n)DTπ​(𝒫n)]≍bnθn​n\mathsf{PTSR}\_{T}(\mathcal{P}\_{n},\pi)=\mathop{\bf E{}}\_{\pi}\left[\frac{\omega^{\pi}\_{T}(\mathcal{P}\_{n})}{D^{\pi}\_{T}(\mathcal{P}\_{n})}\right]\asymp\frac{b\_{n}}{\theta\_{n}\,n} |  |

In particular, the example above shows the order bn/nb\_{n}/n is tight: unless the severity vanishes at the extreme–value scale, θn=Θ​(bn/n)\theta\_{n}=\Theta(b\_{n}/n), one cannot preserve the best trader’s profits as n→∞n\to\infty.
See §[3](https://arxiv.org/html/2512.01112v1#S3 "3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization") for the formal definition of extreme-value scales.

##### Example.

The bound bn/nb\_{n}/n dictates the maximal safe severity for different distributions:

* •

  *Gaussian Winners (Light Tails):* For ei∼𝒩​(0,1)e\_{i}\sim\mathcal{N}(0,1), the maximum scales as bn∼2​log⁡nb\_{n}\sim\sqrt{2\log n}.
  Thus, severity must vanish rapidly, θn≲2​log⁡n/n\theta\_{n}\lesssim\sqrt{2\log n}/n, to avoid autodeleveraging the top winner.
  This implies that the shortfall that can be covered goes to zero as n→∞n\rightarrow\infty.
* •

  *Pareto Winners (Heavy Tails):* For ei∼Pareto​(α)e\_{i}\sim\text{Pareto}(\alpha) with α>1\alpha>1, the maximum scales as bn∼n1/αb\_{n}\sim n^{1/\alpha}.
  Here, the constraint is looser but still vanishing as n→∞n\rightarrow\infty: θn≲n−(1−1/α)\theta\_{n}\lesssim n^{-(1-1/\alpha)}.

Even in the heavy-tailed case (infinite variance, α<2\alpha<2), budget balance implies that a constant fraction severity θ\theta wipes out the top winner almost surely as n→∞n\to\infty.

### 5.2 Excessive leverage guarantees large maximal trader loss

Another natural form of moral hazard, one that quantifies the role of the exchange as an agent, is the ratio of leverage held by the winning and losing sides.
If losers generally have much more leverage than winners, then the exchange is giving winning traders a higher likelihood of paying socialized losses.
We quantify this deficiency in risk management by the exchange by providing a more quantitative extreme value result: we show that the ratio of winner to loser leverages is a multiplicative term in how fast the winning trader’s position is likely to be autodeleveraged.

##### Example.

Consider a regime where loser leverage mass ℓ−\ell^{-} dominates winner leverage mass ℓ+\ell^{+}.
Aggregate shortfall scales with loser liability, DT≈ℓ−​bn−D\_{T}\approx\ell^{-}b\_{n}^{-}, while the top winner’s equity scales as ωT≈ℓ+​bn+\omega\_{T}\approx\ell^{+}b\_{n}^{+}.
If severity θn\theta\_{n} is fixed, the haircut budget Hn=θn​DT≈θn​ℓ−​bn−H\_{n}=\theta\_{n}D\_{T}\approx\theta\_{n}\ell^{-}b\_{n}^{-} is large.
Comparing budget to winner equity:

|  |  |  |
| --- | --- | --- |
|  | HnωT≈θn​ℓ−ℓ+​bn−bn+.\frac{H\_{n}}{\omega\_{T}}\approx\theta\_{n}\frac{\ell^{-}}{\ell^{+}}\frac{b\_{n}^{-}}{b\_{n}^{+}}. |  |

If ℓ−≫ℓ+\ell^{-}\gg\ell^{+}, even a small severity θn\theta\_{n} creates a haircut larger than the top winner’s entire position.
Thus, safe severity is throttled not just by market size but by the *leverage imbalance* ℓ+/ℓ−\ell^{+}/\ell^{-}.
See Appendix [B.6](https://arxiv.org/html/2512.01112v1#A2.SS6.SSS0.Px2 "Leverage-imbalance construction. ‣ B.6 Randomized constructions for moral-hazard examples ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") for the rigorous construction.

##### Main Result.

The next result makes the leverage–imbalance effect precise.
When loser positions carry much more leverage than winners, the ratio of winner to loser leverage masses ℓn+/ℓn−\ell\_{n}^{+}/\ell\_{n}^{-} enters multiplicatively in the EV-scale bound for the top winner’s survival.
In moral-hazard terms, an exchange that tolerates very high loser leverage effectively exposes its best winners to autodeleveraging: even with small severities θn\theta\_{n}, a large imbalance ℓn−/ℓn+\ell\_{n}^{-}/\ell\_{n}^{+} can still force substantial haircuts on the most profitable traders.

###### Proposition 5.2 (Informal).

Let bn+,bn−b\_{n}^{+},b\_{n}^{-} be the extreme value scales of the winning and losing traders, respectively.
Furthermore, let the winner and loser side leverage masses be ℓn+,ℓn−\ell\_{n}^{+},\ell\_{n}^{-}, respectively.
Then we have the general EVT scaling:

|  |  |  |
| --- | --- | --- |
|  | 𝐄π[ωTπ​(𝒫n)DTπ​(𝒫n)]≍ℓn+ℓn−⋅bn+bn−⋅1θn.\mathop{\bf E{}}\_{\pi}\!\left[\frac{\omega^{\pi}\_{T}(\mathcal{P}\_{n})}{D^{\pi}\_{T}(\mathcal{P}\_{n})}\right]\ \asymp\ \frac{\ell\_{n}^{+}}{\ell\_{n}^{-}}\cdot\frac{b\_{n}^{+}}{b\_{n}^{-}}\cdot\frac{1}{\theta\_{n}}. |  |

The full proof is in Appendix [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").

##### Example.

The scaling is now modulated by the *leverage imbalance* Λn=ℓn+/ℓn−\Lambda\_{n}=\ell\_{n}^{+}/\ell\_{n}^{-}.

* •

  *Symmetric Leverage (Λn≍1\Lambda\_{n}\asymp 1):* If winner and loser leverages are comparable, the bound reverts to the previous case (bn+/bn−b\_{n}^{+}/b\_{n}^{-}).
* •

  *High Loser Leverage (Λn≪1\Lambda\_{n}\ll 1):* If losers are 10×10\times more leveraged, the safe severity drops by 10×10\times. In the extreme, if ℓn−∼n\ell\_{n}^{-}\sim n (e.g., a few massive whales) while ℓn+∼1\ell\_{n}^{+}\sim 1 (retail winners), the required severity θn\theta\_{n} becomes vanishingly small even faster than the EV scale suggests.
* •

  *High Winner Leverage (Λn≫1\Lambda\_{n}\gg 1):* Conversely, if winners are highly leveraged (so their equity is sensitive to small price moves, but large in notional), the ratio Λn\Lambda\_{n} buffers the impact, allowing for larger severities without autodeleveraging the top winner.

##### Moral Hazard Interpretation.

These results formalize the “second-best” nature of ADL: perfect insurance without incentive distortion is impossible.
Proposition [5.1](https://arxiv.org/html/2512.01112v1#S5.Thmtheorem1 "Proposition 5.1 (Informal). ‣ Main Result. ‣ 5.1 Impossibility of Avoiding Moral Hazard as 𝑛→∞ ‣ 5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization") implies that tail events necessarily penalize the best traders disproportionately, while Proposition [5.2](https://arxiv.org/html/2512.01112v1#S5.Thmtheorem2 "Proposition 5.2 (Informal). ‣ Main Result. ‣ 5.2 Excessive leverage guarantees large maximal trader loss ‣ 5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization") shows that unconstrained loser leverage amplifies this burden.
This mirrors the tension in Central Counterparty (CCP) recovery in traditional clearing, where Variation Gains Haircutting (VGH) socializes losses among winners to avoid insolvency [CPMI\_IOSCO\_2014, Gregory2015].
Like VGH (and unlike assessment powers that call external capital), ADL is an ex-post haircut on unrealized profits, creating similar moral hazard channels [DuffieZhu2011, Pirrong2011].
Practitioners should therefore treat PTSR/PMR as key risk indicators, tuning dynamic severity caps to keep these ratios bounded.

### 5.3 Queue-based Methods are the worst ADL policies for the top winning trade

One result that we see empirically in §[9](https://arxiv.org/html/2512.01112v1#S9 "9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") is that the Queue mechanism is by far the worst ADL policy for the top winning trade.
We briefly formalize this with an informal proposition that we prove in Appendix [B.3](https://arxiv.org/html/2512.01112v1#A2.SS3 "B.3 Queue maximizes top-winner damage ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").

###### Proposition 5.3 (Queue Maximizes Damage to Top Winner).

Among all budget-balanced ADL policies with fixed severity θ\theta, the *Queue* policy (haircut largest winners first) uniquely minimizes the survival of the top winner.
Let ωTQueue\omega\_{T}^{\text{Queue}} and ωTPR\omega\_{T}^{\text{PR}} be the top winner’s post-ADL equity under Queue and Pro-Rata, respectively.
Whenever the haircut budget H=θ​DTH=\theta D\_{T} satisfies H≤e(1)H\leq e\_{(1)}, we have the strict gap

|  |  |  |
| --- | --- | --- |
|  | ωTPR−ωTQueue=H​(1−e(1)WT)> 0.\omega\_{T}^{\text{PR}}-\omega\_{T}^{\text{Queue}}\;=\;H\left(1-\frac{e\_{(1)}}{W\_{T}}\right)\;>\;0. |  |

Consequently, Pro-Rata strictly dominates Queue in terms of fairness metrics:

|  |  |  |
| --- | --- | --- |
|  | 𝖯𝖳𝖲𝖱T​(PR)−𝖯𝖳𝖲𝖱T​(Queue)=θ​(1−e(1)WT).\mathsf{PTSR}\_{T}(\text{PR})-\mathsf{PTSR}\_{T}(\text{Queue})\;=\;\theta\left(1-\frac{e\_{(1)}}{W\_{T}}\right). |  |

Thus, Queue maximizes the concentration of haircuts on the most profitable trader, leading to the worst possible PTSR/PMR scores.

The full proof is in Appendix [B.3](https://arxiv.org/html/2512.01112v1#A2.SS3 "B.3 Queue maximizes top-winner damage ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").
Appendix [B.5](https://arxiv.org/html/2512.01112v1#A2.SS5 "B.5 Relationship to Classical Risk Measures ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") further strengthens this statement by proving that Queue also minimizes the VaR and ES of the top survivor at every confidence level, so even classical risk metrics rank Queue as the worst policy for the top winner.

## 6 Fairness

A natural question is whether a particular ADL policy is optimal or fair.
We demonstrate that a modified pro-rata rule respecting per-account constraints, the *capped pro-rata rule*, is the most fair policy in two senses: it minimizes total convex disutility and is the unique rule satisfying key axiomatic properties.

##### Definition of the Capped Pro-Rata Rule.

The capped pro-rata rule is a water-filling algorithm that enforces per-account constraints before applying a pro-rata haircut.
Combining haircut constraints ([22](https://arxiv.org/html/2512.01112v1#S2.E22 "Equation 22 ‣ Per-account constraints. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) and equity constraints ([23](https://arxiv.org/html/2512.01112v1#S2.E23 "Equation 23 ‣ Per-account constraints. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")), we define an effective cap βi=min⁡{h¯i,1−e¯i/eT​(𝔭i)}\beta\_{i}=\min\{\overline{h}\_{i},1-\underline{e}\_{i}/e\_{T}(\mathfrak{p}\_{i})\}.
The maximum haircut capacity is

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(β)=∑i=1neT​(𝔭i)​βi.C(\beta)=\sum\_{i=1}^{n}e\_{T}(\mathfrak{p}\_{i})\beta\_{i}. |  | (28) |

If the deficit exceeds this capacity, no feasible haircut exists.
Otherwise, we aim to equalize haircuts subject to these caps.
The capped pro-rata rule πC​P\pi\_{CP} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hπC​P,i=min⁡{η,βi}h\_{\pi\_{CP},i}=\min\{\eta,\beta\_{i}\} |  | (29) |

where η∈[0,1]\eta\in[0,1] is chosen to satisfy the budget constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nhπC​P,i​eT​(𝔭i)+=θπ​DT​(𝒫n).\sum\_{i=1}^{n}h\_{\pi\_{CP},i}e\_{T}(\mathfrak{p}\_{i})\_{+}=\theta\_{\pi}D\_{T}(\mathcal{P}\_{n}). |  | (30) |

This can be computed efficiently by sorting the caps βi\beta\_{i} and finding the threshold η\eta (see eq. ([30](https://arxiv.org/html/2512.01112v1#S6.E30 "Equation 30 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")) and the algorithm in Appendix [D](https://arxiv.org/html/2512.01112v1#A4 "Appendix D Algorithms for Pro-Rata Haircut Rules ‣ Autodeleveraging: Impossibilities and Optimization")).

##### Convex Optimality.

Let ϕ:[0,1]→R\phi:[0,1]\rightarrow{\mbox{\bf R}} be an increasing convex function representing the disutility of a haircut.
We formulate the problem of minimizing total disutility subject to per-account constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minh∈[0,1]n∑i=1nϕ​(hi)subject to∀i∈[n]​hi≤βi(effective cap)\begin{array}[]{ll}\displaystyle{\min\_{h\in[0,1]^{n}}}&\displaystyle{\sum\_{i=1}^{n}\phi(h\_{i})}\\[6.0pt] \text{subject to}&\forall i\in[n]\;\;h\_{i}\leq\beta\_{i}\quad\text{(effective cap)}\end{array} |  | (31) |

In Appendix [C](https://arxiv.org/html/2512.01112v1#A3.SS0.SSS0.Px2 "Convex Optimality ‣ Appendix C Theoretical Properties of Capped Pro-Rata ‣ Autodeleveraging: Impossibilities and Optimization"), we show:

###### Proposition 6.1.

The unique solution to ([31](https://arxiv.org/html/2512.01112v1#S6.E31 "Equation 31 ‣ Convex Optimality. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")) is the capped pro-rata rule ([29](https://arxiv.org/html/2512.01112v1#S6.E29 "Equation 29 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")).

This implies that for any reasonable model of financial disutility, capped pro-rata maximizes social welfare.

##### Axiomatic Fairness.

We define three natural fairness properties:

* •

  *Sybil resistance:* Outcomes are identity-agnostic and invariant to splitting or merging accounts.
* •

  *Scale invariance:* Haircuts are unchanged if both shortfall and equities are scaled by a common factor.
* •

  *Monotonicity (Stability):* The policy preserves the relative ordering of post-haircut equity. If ei≥eje\_{i}\geq e\_{j}, then (1−hi)​ei≥(1−hj)​ej(1-h\_{i})e\_{i}\geq(1-h\_{j})e\_{j}.

In Appendix [C](https://arxiv.org/html/2512.01112v1#A3 "Appendix C Theoretical Properties of Capped Pro-Rata ‣ Autodeleveraging: Impossibilities and Optimization"), we formalize the following result:

###### Proposition 6.2 (Informal).

Under mild smoothness conditions, the unique sybil-resistant, scale-invariant, and monotone ADL policy satisfying per-account constraints is capped pro-rata.

This establishes capped pro-rata as the unique fair ordering rule.
In contrast, queue-based rules (ranking by leverage or PNL) are generally not stable or sybil-resistant.
RAP introduces a risk tilt, deviating from strict equity stability to reduce risk, but remains “as stable as possible” within its risk-weighted framework.
In the numerical examples we present in the next section, we will see explicit examples where capped-pro rata is better for both exchange solvency and trader profitability than the PNL-leverage ranking and pure pro-rata.

## 7 Risk-aware Policies (RAP)

Fairness-focused rules like capped pro-rata treat all winning dollars equally, ignoring the heterogeneous risks imposed by different winners.
Higher effective leverage implies thinner liquidation windows and greater sensitivity to execution costs [AlmgrenChriss2001, Gatheral2010].
We introduce *Risk-Aware Pro-Rata* (RAP), a family of rules that preserves the fairness structure of capped pro-rata while tilting haircuts toward higher-risk positions.
This family includes Levered Pro-Rata (LPR) when the risk weighting is linear in leverage.
We derive RAP from a robustness criterion that minimizes a one-step excess-deficit proxy.

##### One-step Next Deficit.

To formalize robustness, we consider the *next-step deficit* DT+1nextD^{\text{next}}\_{T+1} resulting from a price shock ZTZ\_{T} occurring immediately after the ADL procedure.
Let π\pi be an ADL policy yielding post-haircut notional n~T,i\tilde{n}\_{T,i} and equity eT,ie\_{T,i}.
We model the shock ZTZ\_{T} using a Markov kernel sensitive to the state.
The next-step deficit is the negative equity after the shock:

|  |  |  |
| --- | --- | --- |
|  | DT+1next=∑i∈𝒲T(−eT,i−n~T,i​ZT,i)+=∑i∈𝒲Tn~T,i​(1λT,i+ZT,i)−.D^{\text{next}}\_{T+1}=\sum\_{i\in\mathcal{W}\_{T}}(-e\_{T,i}-\tilde{n}\_{T,i}Z\_{T,i})\_{+}=\sum\_{i\in\mathcal{W}\_{T}}\tilde{n}\_{T,i}\left(\frac{1}{\lambda\_{T,i}}+Z\_{T,i}\right)\_{-}. |  |

Our objective is to minimize the conditional expected deficit δT=𝐄[DT+1next∣ℱT]\delta\_{T}=\mathop{\bf E{}}[D^{\text{next}}\_{T+1}\mid\mathcal{F}\_{T}].
Defining ψi​(u)=𝐄[(u+ZT,i)−]\psi\_{i}(u)=\mathop{\bf E{}}[(u+Z\_{T,i})\_{-}], we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δT=∑i∈𝒲Tn~T,i​ψi​(1λT,i).\delta\_{T}=\sum\_{i\in\mathcal{W}\_{T}}\tilde{n}\_{T,i}\psi\_{i}\left(\frac{1}{\lambda\_{T,i}}\right). |  | (32) |

Appendix [E.1](https://arxiv.org/html/2512.01112v1#A5.SS1 "E.1 Examples of Risk-Aware Pro-Rata (RAP) and Next Deficit ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization") illustrates how pro-rata fails to control this deficit when shocks scale with leverage.

##### Risk Models.

We assume the exchange employs a convex risk model g​(λ)g(\lambda) characterizing the risk contribution of leverage λ\lambda.
Common choices include:

1. 1.

   *Linear*: g​(λ)=λg(\lambda)=\lambda, corresponding to LPR. Matches VaR/CVaR scaling under linear shocks.
2. 2.

   *Power*: g​(λ)=λcg(\lambda)=\lambda^{c} (c>1c>1), penalizing high leverage super-linearly.
3. 3.

   *CVaR*: g​(λ)=(λ−τ)+g(\lambda)=(\lambda-\tau)\_{+}, a surrogate for Conditional Value-at-Risk.

Appendix [E.1](https://arxiv.org/html/2512.01112v1#A5.SS1 "E.1 Examples of Risk-Aware Pro-Rata (RAP) and Next Deficit ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization") provides numerical examples of these weightings.

### 7.1 Risk-Aware Pro-Rata (RAP) Rule

The RAP rule allocates haircuts using weights wi=λT,i​g​(λT,i)w\_{i}=\lambda\_{T,i}g(\lambda\_{T,i}).
With per-account caps βi\beta\_{i}, the haircuts are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hRAP​(g),i=min⁡{βi,τ​wi},h\_{\mathrm{RAP}(g),i}=\min\{\beta\_{i},\tau w\_{i}\}, |  | (33) |

where τ\tau is calibrated to meet the target budget.
This concentrates haircuts on high-risk positions.
See Appendix [D](https://arxiv.org/html/2512.01112v1#A4 "Appendix D Algorithms for Pro-Rata Haircut Rules ‣ Autodeleveraging: Impossibilities and Optimization") for precise implementation of the algorithm.

### 7.2 Convex Dominance of RAP

We can construct an optimal risk model g∗g^{\*} that minimizes δT\delta\_{T}.
Intuitively, an optimal risk model should maximize the marginal reduction of δT\delta\_{T} per unit of equity eT,ie\_{T,i}.
Differentiating δT\delta\_{T} with respect to the haircut hT,ih\_{T,i} reveals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂δT​(h)∂hT,i=nT,i​ψi​(1λT,i)=eT,i​λT,i​ψi​(1λT,i)=eT,i​ρi​(λT,i),-\frac{\partial\,\delta\_{T}(h)}{\partial h\_{T,i}}\ =\ n\_{T,i}\,\psi\_{i}\!\left(\tfrac{1}{\lambda\_{T,i}}\right)\ =\ e\_{T,i}\,\lambda\_{T,i}\,\psi\_{i}\!\left(\tfrac{1}{\lambda\_{T,i}}\right)\ =\ e\_{T,i}\,\rho\_{i}(\lambda\_{T,i}), |  | (34) |

where we define the *perspective transform* ρi​(λ)=λ​ψi​(1/λ)\rho\_{i}(\lambda)=\lambda\,\psi\_{i}(1/\lambda).
The greedy rule that maximizes the marginal reduction per equity-dollar is exactly the rule that prioritizes winners with the largest ρi​(λT,i)\rho\_{i}(\lambda\_{T,i}).

##### Perspective Transform and Economic Intuition.

The function ρi\rho\_{i} is the perspective transform of the convex function ψi\psi\_{i} [BoydVandenberghe2004, §2.3.3], widely used to induce 1-homogeneity.
Economically, u=1/λu=1/\lambda is the bankruptcy buffer, which is the percentage price shock required to wipe out the position’s equity (since loss equals equity when shock magnitude Z=e/n~=1/λZ=e/\tilde{n}=1/\lambda).
Using convex duality, we can write ρi​(λ)=supy≥0{y−λ​ψi∗​(y)}\rho\_{i}(\lambda)=\sup\_{y\geq 0}\{y-\lambda\,\psi\_{i}^{\*}(y)\}, where yy is a ‘yield’ (equity change per unit buffer change) and ψi∗​(y)\psi\_{i}^{\*}(y) is the cost to insure a position with yield yy.
Thus, maximizing ρi\rho\_{i} is equivalent to maximizing the net solvency gain per unit of equity.
For example, if a trader with leverage λ=10\lambda=10 faces an insurance cost of 0.5% for a yield of 8%, the net solvency gain is 0.08−10​(0.005)=0.030.08-10(0.005)=0.03 per unit equity.

##### Constructing the optimal risk model.

This suggests the optimal weights wi⋆=ρi​(λT,i)w^{\star}\_{i}=\rho\_{i}(\lambda\_{T,i}) and risk model g⋆​(λ)=ρ​(λ)/λg^{\star}(\lambda)=\rho(\lambda)/\lambda.

###### Proposition 7.1 (Informal).

For any weighted pro-rata rule comonotone with w⋆w^{\star}, the residual risk vector is weakly submajorized by that of RAP​(g⋆)\mathrm{RAP}(g^{\star}).
This implies that RAP​(g⋆)\mathrm{RAP}(g^{\star}) minimizes the total risk for any convex risk measure, assuming the shock process follows the kernel KK.

The proof is in Appendix [E.2](https://arxiv.org/html/2512.01112v1#A5.SS2 "E.2 RAP Optimality and Convex Dominance ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization").
This result implies that if we have prior knowledge about the kernel KK (e.g., from historical data or backtesting), then constructing g∗g^{\*} via the perspective transform yields the optimally robust and fair haircut model.

### 7.3 Limitations of One-Step Optimality

While RAP minimizes the one-step next deficit, it may not be optimal under multiple correlated shocks or broader exchange objectives.

##### Correlated Shocks.

Consider sequential shocks Zt+1,Zt+2Z\_{t+1},Z\_{t+2} with positive correlation.
High-leverage positions might act as a hedge against future shocks.
In such cases, aggressively liquidating high-leverage winners (as in RAP) can increase the two-step deficit compared to pro-rata.
Appendix [E.1](https://arxiv.org/html/2512.01112v1#A5.SS1 "E.1 Examples of Risk-Aware Pro-Rata (RAP) and Next Deficit ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization") details an AR(1) shock example where the sum of deficits is lower for pro-rata.

##### Exchange Incentive Compatibility.

Exchanges must also consider *exchange long–term value (LTV)*—the future fees and liquidity provided by traders.
RAP targets high-leverage, often high-volume, traders.
Fully liquidating these accounts to minimize immediate risk can reduce the exchange’s long-term utility.
Appendix [E.3](https://arxiv.org/html/2512.01112v1#A5.SS3 "E.3 Example of the Solvency vs. Long-Term Revenue Trade-Off ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization") provides an example where preserving a high-value trader (via pro-rata) yields higher total utility than the risk-minimizing RAP.

## 8 Multiple–Round ADL as a Stackelberg Control Problem

As the previous section illustrates, risk-aware pro-rata mechanisms work well as robust, static strategies but not in a dynamic setting.
Both exchange future revenue and correlated shocks require including a model of the dynamics of ADL over multiple rounds.
We use the intuition gained from RAP mechanisms for a single round to help extend the model to the multiple round setting.
A common place where there is a difference between one-shot equilibria and multi-round equilibria is in the difference between Nash and Stackelberg games.
We will illustrate how the multi-round ADL problem is naturally a Stackelberg game whereas the ADL policies that we have studied so far are more like Nash optimal strategies.
To do this, we will first briefly describe Stackelberg games and then provide examples demonstrating that it is the right formalism for this extension.

### 8.1 ADL is a Stackelberg Game

##### Definition.

A Stackelberg (leader–follower) game is a sequential game where the leader first *commits* to a strategy or policy, the follower observes this commitment, and then best–responds; the leader chooses its commitment anticipating this response [Stackelberg1934, FudenbergTirole1991, BasarOlsder1999].111111In the finance and control literature, this setup is often framed as “Dynamic Optimal Control with Rational Expectations” or a principal-agent problem with commitment [Puterman1994, Bertsekas2017, LaffontMartimort2002].
The defining features are (i) observable commitment, (ii) sequential move order, and (iii) the leader’s optimization against the follower’s best–response correspondence.
In repeated or multi–round settings, the leader can *learn* a near–optimal commitment by updating its policy from round to round using feedback from realized follower responses and shocks; this supports standard online learning guarantees when losses are convex (or admit convex surrogates) [Zinkevich2003, ShalevShwartz2012, Hazan2019], and, under additional regularity, learnability results specific to Stackelberg games [conitzer2006].

##### ADL and Stackelberg games.

ADL naturally fits the setup of a Stackelberg game: the exchange (leader) *publishes* its ADL policy each round by choosing a severity budget θt∈[0,1]\theta\_{t}\in[0,1] and a haircut rule.
As we saw in §[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"), the queueing rules used by Binance and Hyperliquid imply both a static severity and haircut rule and are published on their websites (which is their form of commitment).
Market participants (e.g. traders, LPs) and the stochastic environment (order flow, depth, liquidation behavior, oracle and price shocks) then respond as followers given the announced policy.
After market participants (followers) respond, the residual exposure (i.e., the remaining negative equity) is measured and the leader decides on a next action (which could include to stop the game and not perform an ADL policy).
The commitment of the exchange allows followers to construct a *local* best response that can adapt as the number of rounds of the game increases.

##### Credibility and Time Inconsistency.

Crucially, the Stackelberg formulation assumes the leader can credibly commit to a policy path.
In decentralized venues (e.g., Hyperliquid), this is enforced via on-chain code or DAO governance, making the commitment verifiable.
In centralized venues (e.g., Binance), the commitment is reputational.
Without commitment, the game reverts to a Nash setting where the exchange suffers from *time inconsistency*: ex-ante, it prefers a “gentle” policy to attract liquidity, but ex-post (once a deficit DtD\_{t} materializes), it has a dominant incentive to defect to maximal severity (Queue ADL) to minimize immediate insolvency risk.
This temptation to defect undermines liquidity provision unless the commitment is binding, further justifying the Stackelberg framework over pure control theory.

##### Stackelberg vs. Nash.

Nash equilibria are one–shot, *simultaneous–move* fixed points where each player best–responds to the other’s action but no one commits *ex ante* [FudenbergTirole1991].
By contrast, Stackelberg equilibria embed the leader’s commitment advantage, often producing different (and more robust or revenue–enhancing) outcomes [Stackelberg1934, BasarOlsder1999].
Static ADL strategies such as venue queues (Binance/Hyperliquid) or single–round RAP can be analyzed under a Nash lens, as we assume there is no further response by a leader after a single execution of an ADL policy.
In practice, ADL controllers are used repeatedly (such as on October 10, 2025; see §[9](https://arxiv.org/html/2512.01112v1#S9 "9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization")) which more resembles a Stackelberg game.
In Appendix [F.3](https://arxiv.org/html/2512.01112v1#A6.SS3 "F.3 Stackelberg vs. Nash in a Two-Round ADL Game ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") we give an explicit example for ADL where a Stackelberg equilibrium differs from a Nash outcome and in which the Stackelberg equilibrium strictly improves exchange revenue and robustness.

##### Robustness and Learnability of Stackelberg games.

Robust Stackelberg models capture the leader’s desire to hedge against uncertainty hidden in the follower’s strategy by optimizing for *worst–case* responses [aghassi2006].
In ADL, robustness corresponds to resilience against adverse price/oracle shocks, liquidity droughts, and funding–rate shocks.
Specifically, the exchange chooses a policy that anticipates such perturbations and steers the system toward states with smaller tail externalities (analogous to Stackelberg Security Games [Tambe2011, conitzer2006]).

When the leader’s per round objective function is convex in its policy (or admits convex surrogates) and constraints are convex, standard online methods (mirror descent, FTRL) achieve sublinear regret and convergence to near–optimal commitments [Zinkevich2003, ShalevShwartz2012, Hazan2019].
Recent work studies gradient–based learning in Stackelberg games directly, providing conditions under which leader updates converge to Stackelberg equilibria, including bandit/noisy feedback regimes.
These tools align well with ADL’s multi–round nature and with the RAP geometry used for choosing haircuts.

### 8.2 Why do we need a dynamic model?

Stackelberg games are inherently dynamic due to the alternating move order between the leader and follower.
A natural question is whether we really need to use a dynamic method or if a static method is ‘good enough.’
In this section, we will provide our first formal results showing that dynamic ADL rules are necessary if you want to optimize both time to recover solvency and exchange revenue after repeated shocks.
This will motivate the construction of the dynamic ADL policy in the sequel.

##### Exchange Long-Term Value (LTV) and the Trilemma.

Recall the ADL Trilemma from §[2.5](https://arxiv.org/html/2512.01112v1#S2.SS5 "2.5 ADL Trilemma ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"), which posits a conflict between Solvency (S), Fairness (F), and Revenue (R).
To quantify the *Revenue* objective, we define the *Exchange Long-Term Value* (LTV).
Unlike immediate fee capture, LTV accounts for the long-run impact of ADL on trader participation: heavy haircuts on winners cause them to exit or reduce activity (“churn”), eroding future fees.

For a policy π\pi, let ht,i∈[0,1]h\_{t,i}\in[0,1] be the haircut fraction on winner ii at time tt.
We model trader retention via a revenue retention curve rt,i​(ht,i)r\_{t,i}(h\_{t,i}) which is decreasing in the haircut size (larger haircuts drive away more volume).
The per-period expected revenue from trader ii is then Rt,i=et,i​rt,i​(ht,i)R\_{t,i}=e\_{t,i}r\_{t,i}(h\_{t,i}), where et,ie\_{t,i} is their equity.
The LTV is the discounted sum of these revenues:

|  |  |  |
| --- | --- | --- |
|  | LTVT​(π)=∑t=0Tβt​∑i∈Wtet,i​rt,i​(ht,i).\mathrm{LTV}\_{T}(\pi)=\sum\_{t=0}^{T}\beta^{t}\sum\_{i\in W\_{t}}e\_{t,i}\,r\_{t,i}(h\_{t,i}). |  |

Maximizing LTV corresponds directly to the *(R)* vertex of the trilemma.

##### Competing Time Scales.

To compare policies dynamically, we track two opposing clocks starting from a default event at τdef\tau\_{\mathrm{def}}:

* •

  *Solvency Recovery Time* (τsolv\tau\_{\mathrm{solv}}): The time required for the insurance fund (or deficit) to fully recover to a safe level δ\delta.
* •

  *Revenue Recovery Time* (τrev\tau\_{\mathrm{rev}}): The time required for the exchange’s expected LTV to return to pre-shock levels (1−ϵ)​LTVpre(1-\epsilon)\mathrm{LTV}\_{\text{pre}}.

Intuitively, τsolv\tau\_{\mathrm{solv}} measures how fast the “hole is plugged,” while τrev\tau\_{\mathrm{rev}} measures how fast the “business recovers.”
Static policies face a fundamental trade-off between these times, governed by the concentration of haircuts.

##### Example.

We can rigorously rank policies using the Schur-convex (majorization) order from §[3](https://arxiv.org/html/2512.01112v1#S3 "3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization").
Consider two canonical policies:

* •

  *Queue ADL (Concentrated):* This policy fully haircuts the largest winner until the deficit is covered. It is extremely Schur-convex (unequal).
  By targeting the deepest pocket, it clears the deficit with the minimal total haircut volume, minimizing τsolv\tau\_{\mathrm{solv}}.
  However, it destroys the highest-value traders (the “whales”), causing a massive drop in LTV and maximizing τrev\tau\_{\mathrm{rev}}.
* •

  *Pro-Rata ADL (Diffused):* This policy spreads the haircut proportionally across all winners. It is Schur-concave (equal).
  It preserves the whales but requires a larger total haircut volume to clear the same deficit (due to many small accounts having insufficient equity), effectively delaying τsolv\tau\_{\mathrm{solv}}.
  However, because the per-trader impact is small, churn is low, and τrev\tau\_{\mathrm{rev}} is minimized.

This intuition is formalized in the following proposition, which states that any policy that concentrates haircuts (like Queue) will recover solvency faster but revenue slower than a diffuse policy (like Pro-Rata).

##### Opposing Schur orderings.

Let zt​(π)z\_{t}(\pi) be the vector of post-haircut residual equities.
If policy AA is more concentrated than policy BB (i.e., zt​(A)≻Schurzt​(B)z\_{t}(A)\succ\_{\text{Schur}}z\_{t}(B)), then AA recovers solvency faster but revenue slower.

###### Proposition 8.1 (Informal).

Under separable convex stage losses and monotone shock dynamics, if the residual exposure of policy AA majorizes policy BB (e.g., Queue vs. Pro-Rata), then:

|  |  |  |
| --- | --- | --- |
|  | τsolv​(A)≤τsolv​(B)butLTVt​(A)≤LTVt​(B)for all ​t.\tau\_{\mathrm{solv}}(A)\leq\tau\_{\mathrm{solv}}(B)\quad\text{but}\quad\mathrm{LTV}\_{t}(A)\leq\mathrm{LTV}\_{t}(B)\quad\text{for all }t. |  |

This implies no static policy can simultaneously minimize both recovery times.

##### Endogenous Price Feedback.

Static models typically treat the deficit DtD\_{t} as exogenous.
In reality, large ADL events create *endogenous* feedback: the act of closing positions (even if socialized among winners) reduces open interest and can signal distress, causing market makers to widen spreads or withdraw bids.
This secondary liquidity shock can drive mark prices further against the exchange, increasing Dt+1D\_{t+1}.
Dynamic policies like πmd\pi\_{\text{md}} (§[8.5](https://arxiv.org/html/2512.01112v1#S8.SS5 "8.5 Learning the Optimal ADL Policy ‣ 8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization")) naturally handle this by treating the environment as adversarial (or responsive), whereas static policies risk under-estimating the “death spiral” effect of the ADL action itself.

### 8.3 Incentive Compatibility and Constraints

We frame the problem as a Stackelberg game: the exchange (leader) commits to a policy, and traders (followers) best-respond.
*Follower Incentive Compatibility* requires traders’ actions—liquidity provision and liquidations—to satisfy feasibility and non-bankruptcy conditions given this commitment.
The exchange’s policy is subject to *Revenue Constraints* (ensuring profitability via fees and net liquidation revenues) and *Solvency Constraints* (bounding tail risk via coherent measures like ES or CVaR [RockafellarUryasev2002, BCBS2019FRTB]).
These constraints define the feasible region for the loss minimization problem.

### 8.4 ADL Constraints and Objective

##### Composite Loss Function.

We formulate the ADL control problem as minimizing a composite loss function that explicitly balances exchange revenue, solvency, and fairness.
Let πt=(θt,ht)\pi\_{t}=(\theta\_{t},h\_{t}) denote the ADL policy at round tt, where θt∈[0,1]\theta\_{t}\in[0,1] is the severity (fraction of deficit socialized) and ht∈[0,1]nh\_{t}\in[0,1]^{n} parameterizes the inner allocation rule (e.g., weights for RAP or Pro-Rata).
Based on our empirical framework, the per-round loss ℓt​(πt)\ell\_{t}(\pi\_{t}) is defined as:

|  |  |  |
| --- | --- | --- |
|  | ℓt​(πt)=λrev⋅ℒtrev​(πt)+λsolv⋅ℒtsolv​(πt)+λfair⋅ℒtfair​(πt),\ell\_{t}(\pi\_{t})\;=\;\lambda\_{\text{rev}}\cdot\mathcal{L}^{\text{rev}}\_{t}(\pi\_{t})\;+\;\lambda\_{\text{solv}}\cdot\mathcal{L}^{\text{solv}}\_{t}(\pi\_{t})\;+\;\lambda\_{\text{fair}}\cdot\mathcal{L}^{\text{fair}}\_{t}(\pi\_{t}), |  |

where the components are:

* •

  *Revenue Loss (ℒ*rev*\mathcal{L}^{\text{rev}}):* The discounted stream of future fees lost due to liquidating positions. This incentivizes the exchange to preserve valuable, high-volume users when possible.
* •

  *Solvency Cost (ℒ*solv*\mathcal{L}^{\text{solv}}):* A penalty on the *residual deficit* (the portion of the loss DtD\_{t} not covered by the ADL recovery) and *overshoot* (excessive liquidation beyond what is needed). This ensures the mechanism actually restores system health without unnecessary destruction.
* •

  *Fairness Cost (ℒ*fair*\mathcal{L}^{\text{fair}}):* Penalties based on the Profit-to-Solvency Ratio (PTSR) and Profit-Margin Ratio (PMR). These terms enforce that the burden of ADL is distributed equitably relative to traders’ profitability and risk contribution, preventing the “death spiral” of adverse selection.

##### Stackelberg vs. Nash Equilibria.

We model the interaction between the exchange and traders as a Stackelberg game where the exchange (leader) commits to a policy πt\pi\_{t}, and traders (followers) subsequently respond (e.g., by adjusting liquidity or closing positions).
This commitment power is crucial.
As we show in Appendix [F.3](https://arxiv.org/html/2512.01112v1#A6.SS3 "F.3 Stackelberg vs. Nash in a Two-Round ADL Game ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") (Proposition [F.6](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem6 "Proposition F.6 (Stackelberg Dominance). ‣ Simultaneous play (Nash). ‣ F.3 Stackelberg vs. Nash in a Two-Round ADL Game ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization")), a simultaneous-move (Nash) game admits a “bad” equilibrium where traders withdraw liquidity anticipating high severity, which in turn forces the exchange to set high severity to cover the deficit.
In the Stackelberg model, the exchange can commit to a policy that eliminates this inefficient equilibrium, coordinating the market towards a high-liquidity, lower-severity outcome that improves welfare for all participants.

### 8.5 Learning the Optimal ADL Policy

##### Mirror Descent with IC constraints (MDIC).

We adopt a primal–dual mirror–descent scheme tailored to the RAP geometry and non–smooth constraints:

1. 1.

   Choose a mirror map ψ\psi on the policy domain Π\Pi (e.g., a separable entropy or a Bregman geometry aligned with capped pro–rata).
2. 2.

   Initialize π1∈Π\pi\_{1}\in\Pi and dual multipliers λ1≥0\lambda\_{1}\!\geq 0 for constraints c​(⋅;⋅)≤0c(\cdot;\cdot)\leq 0.
3. 3.

   For rounds t=1,2,…t=1,2,\dots:

   1. (a)

      Observe state sts\_{t}; publish πt\pi\_{t} (commitment). The follower/environment best–responds; incur loss ℓt​(πt)\ell\_{t}(\pi\_{t}) and observe a subgradient gt∈∂ℓt​(πt)g\_{t}\in\partial\ell\_{t}(\pi\_{t}) and constraint feedback ct=c​(πt;st)c\_{t}=c(\pi\_{t};s\_{t}).
   2. (b)

      Primal update (mirror step with penalties):

      |  |  |  |
      | --- | --- | --- |
      |  | πt+1=argminπ∈Π{⟨gt+∇π⟨λt,c​(π;st)⟩,π⟩+1ηt​Dψ​(π∥πt)}.\pi\_{t+1}\;=\;\mathop{\rm argmin}\_{\pi\in\Pi}\;\Big\{\langle g\_{t}+\nabla\_{\pi}\langle\lambda\_{t},c(\pi;s\_{t})\rangle,\,\pi\rangle\;+\;\tfrac{1}{\eta\_{t}}D\_{\psi}(\pi\,\|\,\pi\_{t})\Big\}. |  |
   3. (c)

      Dual update (projected subgradient ascent on violations):

      |  |  |  |
      | --- | --- | --- |
      |  | λt+1=[λt+γt​ct]+.\lambda\_{t+1}\;=\;\big[\lambda\_{t}+\gamma\_{t}\,c\_{t}\big]\_{+}. |  |
4. 4.

   Tune (ηt,γt)(\eta\_{t},\gamma\_{t}) as O​(t−1/2)O(t^{-1/2}) to balance regret and constraint violations.

This controller reduces to standard OCO when constraints are absent, while handling non–smooth IC/solvency constraints via the dual iterates.

##### Why MDIC vs. Online Convex Optimization.

All constraints in 𝒞tIC\mathcal{C}\_{t}^{\mathrm{IC}} are convex but can be non-smooth (e.g. hinge losses, maximizing over scenarios).
Mirror descent handles this composite structure while matching the geometry: KL geometry on the simplex reduces diameter to O​(log⁡|Wt|)O(\log|W\_{t}|); the log-barrier keeps θ\theta interior and gives stable 1-D projections.
This improves constants relative to Euclidean OGD while preserving the same rate.

##### Algorithmic Guarantees.

Assume ftf\_{t} is ℓ\ell-Lipschitz in the dual norms of (ϕ,Φ)(\phi,\Phi), the follower is an
ε\varepsilon-best responder, and 𝒞tIC\mathcal{C}\_{t}^{\mathrm{IC}} is nonempty with bounded diameter in the same
norms. Then MDIC with ηt∝1/T\eta\_{t}\propto 1/\sqrt{T} achieves

|  |  |  |
| --- | --- | --- |
|  | RegretT=O​(T​Dϕ​(θ⋆∥θ1)+T​DΦ​(h⋆∥h1))+ε​T,\mathrm{Regret}\_{T}\;=\;O\!\Big(\sqrt{T\,D\_{\phi}(\theta^{\star}\|\theta\_{1})}+\sqrt{T\,D\_{\Phi}(h^{\star}\|h\_{1})}\Big)\;+\;\varepsilon T, |  |

and enforces the IC rows per round (or, in a primal–dual variant with long-term ES, sublinear average
violation). A full theorem and proof (via the standard MD telescoping bound plus feasibility of the
Bregman projection) appear in Appendix [F.2](https://arxiv.org/html/2512.01112v1#A6.SS2 "F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization"); see also Theorem [F.2](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem2 "Theorem F.2 (OMD Regret). ‣ Master Mirror Descent Bound. ‣ F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") for the unconstrained MD bound.
Under these convexity, Lipschitz, and feasibility assumptions, MDIC attains O​(T)O(\sqrt{T}) regret and sublinear average IC/solvency violations, whereas any static policy incurs Ω​(T)\Omega(T) regret on an alternating environment (see Appendix [F.2](https://arxiv.org/html/2512.01112v1#A6.SS2 "F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") for details).

##### Linear Regret for Static Strategies.

Consider a simplified environment that alternates between two regimes: AA (liquidity) and BB (stress). We fix a maximum severity cap θ¯\bar{\theta} (e.g., θ¯=0.30\bar{\theta}=0.30).
The per-round loss function ft​(θ)f\_{t}(\theta) captures the trade-off between revenue and solvency:

|  |  |  |
| --- | --- | --- |
|  | ft​(θ)={θif ​t∈A​ (minimize severity to protect revenue),θ¯−θif ​t∈B​ (maximize severity to ensure solvency).f\_{t}(\theta)=\begin{cases}\theta&\text{if }t\in A\text{ (minimize severity to protect revenue)},\\ \bar{\theta}-\theta&\text{if }t\in B\text{ (maximize severity to ensure solvency)}.\end{cases} |  |

The optimal static policy must choose a fixed θ∈[0,θ¯]\theta\in[0,\bar{\theta}]. However, any fixed θ\theta incurs linear regret:

|  |  |  |
| --- | --- | --- |
|  | ∑t=1T(ft​(θ)−ft​(θt⋆))=T2​θ+T2​(θ¯−θ)=T2​θ¯=Ω​(T).\sum\_{t=1}^{T}(f\_{t}(\theta)-f\_{t}(\theta^{\star}\_{t}))=\frac{T}{2}\theta+\frac{T}{2}(\bar{\theta}-\theta)=\frac{T}{2}\bar{\theta}=\Omega(T). |  |

In contrast, MDIC adapts θt\theta\_{t} online. Using a standard mirror descent bound (Theorem [F.2](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem2 "Theorem F.2 (OMD Regret). ‣ Master Mirror Descent Bound. ‣ F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization")), MDIC achieves

|  |  |  |
| --- | --- | --- |
|  | 𝖱𝖾𝗀𝗋𝖾𝗍T=O​(θ¯​T).\mathsf{Regret}\_{T}=O(\bar{\theta}\sqrt{T}). |  |

Numerically, for T=104T=10^{4} and θ¯=0.30\bar{\theta}=0.30, a static policy suffers regret ≈1500\approx 1500, while MDIC suffers ≈30\approx 30.

### 8.6 Follower Robustness

So far, we have focused on the leader (e.g. the exchange), as they have to commit to a policy.
However, it is possible that if the follower (i.e., a trader who reduces the deficit) knows enough about the leader’s strategy to adversely select against other traders.
We address the strategic behavior of traders (“followers”) in response to ADL policies, focusing on adverse selection and timing games that naturally occur.
Our coverage of this will be minimal with most details in Appendix [F.4](https://arxiv.org/html/2512.01112v1#A6.SS4 "F.4 Follower Strategic Responses ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization").

##### Adverse Selection and the Pro-Rata Death Spiral.

If an ADL policy socializes losses uniformly (like Pro-Rata), low-risk traders subsidize high-risk traders.
If this subsidy exceeds the utility of trading, low-risk traders exit, increasing both the exchange’s average risk and probability of future deficits.
This is a direct consequence of the follower’s strategic response: low-risk traders, observing a policy that penalizes them disproportionately, rationally choose to exit (or not participate), leaving the exchange with a riskier pool of traders.

Formally, a participation constraint μi−𝐄[Hπ​(λi,𝒫n)]≥u0\mu\_{i}-\mathop{\bf E{}}[H\_{\pi}(\lambda\_{i},\mathcal{P}\_{n})]\geq u\_{0} must hold.
Here μi\mu\_{i} denotes trader ii’s baseline per-round utility in the absence of ADL haircuts, Hπ​(λi,𝒫n)H\_{\pi}(\lambda\_{i},\mathcal{P}\_{n}) is the random haircut mass assigned to a type-ii winner with leverage λi\lambda\_{i} under policy π\pi when the market state is 𝒫n\mathcal{P}\_{n}, and u0u\_{0} is the reservation utility defined in Appendix [F.4.1](https://arxiv.org/html/2512.01112v1#A6.SS4.SSS1 "F.4.1 Adverse Selection Under Pro-Rata ‣ F.4 Follower Strategic Responses ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization").
Under Pro-Rata, 𝐄[HπP​R]\mathop{\bf E{}}[H\_{\pi\_{PR}}] depends on average leverage, which penalizes low-risk traders and potentially causes a “death spiral” of exits.
This “death spiral” refers to the adverse selection that the exchange faces as the pool of traders becomes increasingly risky from a leverage standpoint.

In contrast, RAP’s haircut is proportional to risk weight λi​g​(λi)\lambda\_{i}g(\lambda\_{i}), minimizing the burden on low-risk traders and stabilizing the pool.
Appendix [F.4.1](https://arxiv.org/html/2512.01112v1#A6.SS4.SSS1 "F.4.1 Adverse Selection Under Pro-Rata ‣ F.4 Follower Strategic Responses ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") formalizes this participation test and provides explicit death-spiral examples.

##### The Waiting Game.

Traders may act as “Backstop Liquidity Providers” (BLP) by voluntarily filling liquidation orders to reduce the deficit DtD\_{t}.
For instance, traders who deposit to Hyperliquid’s HLP pool around the time of an ADL event do this.
This presents an optimal stopping problem: a BLP can absorb the deficit immediately (incurring market risk and execution costs) or wait, hoping that the exchange reduces ADL severity θt\theta\_{t} (and thus the potential haircut) in subsequent rounds.
If the exchange employs a policy like exponential backoff that lowers severity over time, it incentivizes traders to wait, potentially exacerbating the deficit.

To prevent such strategic delays, the exchange must satisfy a “No-Wait” constraint: θt​Dt≥Γt\theta\_{t}D\_{t}\geq\Gamma\_{t}, where Γt\Gamma\_{t} is the liquidity premium.
Intuitively, Γt\Gamma\_{t} quantifies the cost of immediate intervention, capturing the execution slippage and inventory risk premium required for a BLP to step in.
By adjusting incentives that are paid to BLPs, an exchange can incentivize “no-wait” conditions and lower the overall time to recover solvency.
We formalize this with the following proposition:

###### Proposition 8.2 (No-Wait Condition).

Let Γt\Gamma\_{t} be the liquidity premium required for a Backstop Liquidity Provider (BLP) to absorb deficit DtD\_{t} immediately rather than waiting for Δ​t\Delta t.
If the severity policy θt\theta\_{t} is a decreasing function of time (e.g., exponential backoff), a BLP will withhold liquidity unless the immediate haircut cost is cheaper than the discounted future cost:

|  |  |  |
| --- | --- | --- |
|  | θt​Dt≤𝐄t[θt+Δ​t​Dt+Δ​t]−Γt.\theta\_{t}D\_{t}\;\leq\;\mathop{\bf E{}}\_{t}[\theta\_{t+\Delta t}D\_{t+\Delta t}]-\Gamma\_{t}. |  |

Violating this condition induces a “Waiting Game” where solvency recovery is delayed purely by the follower’s strategy.

Appendix [F.4.2](https://arxiv.org/html/2512.01112v1#A6.SS4.SSS2 "F.4.2 Waiting Game and MDIC-NW ‣ F.4 Follower Strategic Responses ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") details the construction of Γt\Gamma\_{t} and proves this proposition.

### 8.7 Dynamic Phase Transition in ADL

In Section [5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization"), we established that static ADL rules face fundamental scaling limits.
To quantify the efficiency gap between static (Nash) and dynamic (Stackelberg) control, we evaluate the system using welfare functionals W​(π)W(\pi) corresponding to the trilemma (Proposition [I.7](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem7 "Theorem I.7 (ADL Trilemma). ‣ Formal Statement of the Trilemma. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization")) objectives.
We consider both a fairness welfare WFair​(π)=𝖯𝖳𝖲𝖱T​(π)W\_{\text{Fair}}(\pi)=\mathsf{PTSR}\_{T}(\pi) and a revenue welfare WLTV​(π)=LTVT​(π)W\_{\text{LTV}}(\pi)=\text{LTV}\_{T}(\pi).
The severity load κn=θn​n/bn\kappa\_{n}=\theta\_{n}n/b\_{n} serves as the order parameter for the fairness transition, while the heavy-tail index α\alpha (see §[3.1.2](https://arxiv.org/html/2512.01112v1#S3.SS1.SSS2 "3.1.2 ADL-Specific Efficiency Metrics ‣ 3.1 Risk Metrics ‣ 3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization")) governs the revenue transition.
Together, they drive a *phase transition* in the efficiency of static policies relative to dynamic ones.

##### Why PoA for Nash vs. Stackelberg?

PoA is the standard metric for quantifying efficiency loss from strategic behavior across equilibrium concepts [Roughgarden2005SelfishRouting, roughgarden15intrinsic].
In Stackelberg settings, a leader’s commitment reshapes follower best responses and can systematically lower inefficiency relative to simultaneous-move (Nash) play.
This is well documented in dynamic game models [BasarOlsder1999] and in smoothness-based PoA analyses that extend uniformly across equilibrium notions, including sequential and composed mechanisms [SyrgkanisTardos2013, roughgarden15intrinsic].
In our ADL context, the venue is a natural leader that can commit to a severity path, while traders react myopically to current and anticipated haircuts.
This makes a PoA comparison between one-shot (Nash-like) and multi-round (Stackelberg) control both natural and informative.

We define the Price of Anarchy (PoA) as the ratio of the optimal dynamic Stackelberg welfare to the welfare of a static, one-shot policy πnstat\pi^{\mathrm{stat}}\_{n}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PoAn​(W)=W​(πndyn)W​(πnstat)\mathrm{PoA}\_{n}(W)=\frac{W(\pi^{\mathrm{dyn}}\_{n})}{W(\pi^{\mathrm{stat}}\_{n})} |  | (35) |

Using smoothness arguments [roughgarden15intrinsic] and extreme-value analysis, we obtain PoA bounds that are robust to the precise equilibrium concept. Appendix [G](https://arxiv.org/html/2512.01112v1#A7 "Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization") formalizes our mean-field scaling assumptions and presents the theorem. Informally:

###### Proposition 8.3 (Informal).

Let κn=θ​n/bn\kappa\_{n}=\theta n/b\_{n} be the normalized severity relative to the winner equity scale bnb\_{n}.

* •

  *Bounded PoA (Static Sufficient):* If severity is EV-scaled (supκn<∞\sup\kappa\_{n}<\infty), leverage is balanced (ℓn+≍ℓn−\ell\_{n}^{+}\asymp\ell\_{n}^{-}), and impact is smooth (μOB<1\mu\_{\mathrm{OB}}<1), then static ADL is constant-factor optimal for both Fairness and Revenue: supnPoAnFair<∞\sup\_{n}\mathrm{PoA}^{\text{Fair}}\_{n}<\infty and supnPoAnLTV<∞\sup\_{n}\mathrm{PoA}^{\text{LTV}}\_{n}<\infty.
* •

  *Unbounded PoA (Dynamic Necessary):* If severity is excessive (κn→∞\kappa\_{n}\to\infty) or leverage is concentrated (ℓn+/ℓn−→0\ell\_{n}^{+}/\ell\_{n}^{-}\to 0), then static policies fail on at least one objective: max⁡(PoAnFair,PoAnLTV)→∞\max(\mathrm{PoA}^{\text{Fair}}\_{n},\mathrm{PoA}^{\text{LTV}}\_{n})\to\infty. Specifically, heavy tails force static policies to choose between fairness collapse (θ≈1\theta\approx 1) or revenue collapse (δ≈1\delta\approx 1).

This implies a screening rule: if estimates satisfy κ^n≤K\widehat{\kappa}\_{n}\leq K and Λ^n∈[c,C]\widehat{\Lambda}\_{n}\in[c,C], static ADL suffices; otherwise, dynamic control is required to navigate the Trilemma.

Practically, this result suggests that exchanges can screen assets using historical data to determine whether a simple static rule suffices or if a dynamic policy is required.
Formal statements and proofs are given by Theorem [G.3](https://arxiv.org/html/2512.01112v1#A7.Thmtheorem3 "Theorem G.3 (Fairness PoA Phase Transition). ‣ G.1.2 Phase Transition ‣ G.1 Fairness Phase Transition ‣ Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization")
and Proposition [G.5](https://arxiv.org/html/2512.01112v1#A7.Thmtheorem5 "Proposition G.5 (Revenue PoA Phase Transition). ‣ G.2.2 Phase Transition ‣ G.2 Revenue Phase Transition ‣ Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization")
in Appendix [G](https://arxiv.org/html/2512.01112v1#A7 "Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization"), and by
Example [G.4](https://arxiv.org/html/2512.01112v1#A7.Thmtheorem4 "Example G.4 (Light-tailed Failure). ‣ G.1.2 Phase Transition ‣ G.1 Fairness Phase Transition ‣ Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization").

## 9 Empirical Analysis: The October 10 Event

We evaluate the proposed ADL mechanisms using a high-fidelity replay of the October 10, 2025 liquidation cascade on Hyperliquid [CoinDesk2025LargestLiquidations].
This event serves as a practical testbed for the theoretical phase transitions identified in Section [8.7](https://arxiv.org/html/2512.01112v1#S8.SS7 "8.7 Dynamic Phase Transition in ADL ‣ 8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization"), characterizing the performance gap between static and dynamic policies in a high-stress regime (Dt≫0D\_{t}\gg 0).

### 9.1 Experimental Setup

##### Dataset.

We utilize the canonical reconstruction of the event [HyperMultiAssetedADL], covering a 12-minute window (21:16–21:27 UTC) with $2.1B in liquidations across 161 assets.
The replay comprises T=1108T=1108 ADL shocks (998 with Dt>0D\_{t}>0).
Each shock records the realized deficit DtD\_{t} (total negative equity of the losers) and the account-level winner capacities wtw\_{t}.
Summing DtD\_{t} across the positive-deficit shocks yields $304.5M of shortfall that must be socialized, whereas the feasible haircut mass ∑iwt,i\sum\_{i}w\_{t,i} totals only $95.8M, so at least $208.6M of losses remain uncovered irrespective of policy.
These pathwise statistics match the appendix methodology and provide the baseline against which we evaluate each controller.
The dataset provides the exact sequence of exogenous price shocks and trader positions, allowing for a counterfactual analysis of ADL responses holding market conditions fixed.

##### Policies.

We compare the static benchmark πqueue\pi\_{\text{queue}} against the dynamic controllers defined in Appendix [H.3](https://arxiv.org/html/2512.01112v1#A8.SS3 "H.3 Policies ‣ Appendix H Empirical Methodology ‣ Autodeleveraging: Impossibilities and Optimization"):

* •

  *Static Priority (π*queue*,π*smart*\pi\_{\text{queue}},\pi\_{\text{smart}}):* The standard greedy mechanism (Queue) and its deficit-capped variant (Smart Queue). πsmart\pi\_{\text{smart}} enforces Ht≤DtH\_{t}\leq D\_{t} but retains the greedy priority ranking.
* •

  *Dynamic Severity (π*exp*,π*md*\pi\_{\text{exp}},\pi\_{\text{md}}):* The Exponential Backoff and Mirror Descent controllers that optimize the scalar severity θt\theta\_{t} while allocating haircuts pro-rata.
* •

  *Vector Optimization (π*vec*\pi\_{\text{vec}}):* The full allocation policy minimizing the composite loss LtL\_{t} via high-dimensional mirror descent.

##### Revenue proxy.

We construct a *revenue proxy* that estimates the expected fee and revenue loss for the exchange given a set of ADL haircuts.
At a high level, we model how much churn traders experience post haircut, akin to other customer retention models [Acerbi2002, Bolton1998Duration, Schmittlein1987Customers].
Given the churn, we model a fee proxy that estimate the loss in fees per unit of notional size that churns.
Formally, define the *churn probability* of winner ii as the probability that the account exits the venue after receiving a haircut in round tt.
Empirically, this quantity controls how much future revenue the exchange forfeits.
We model churn with the exponential hazard pt,i=1−exp⁡(−β​ht,i/wt,i)p\_{t,i}=1-\exp(-\beta h\_{t,i}/w\_{t,i}), which keeps responses linear for small haircuts yet saturates toward one for severe cuts, matching the account-level attrition we measure in the Hyperliquid replay.
This mirrors the survival-style retention curves widely used in both classic and modern marketing-science churn models [Bolton1998Duration, Schmittlein1987Customers, AscarzaHardie2013UsageChurn, LemmensGupta2020Churn, Ascarza2018RetentionFutility].
Full details of the calculation and the fee proxy are in Appendix [H.2](https://arxiv.org/html/2512.01112v1#A8.SS2.SSS0.Px3 "Revenue loss proxy. ‣ H.2 Losses and objectives ‣ Appendix H Empirical Methodology ‣ Autodeleveraging: Impossibilities and Optimization").

### 9.2 Results

##### Overshoot and Efficiency.

Consistent with the theoretical prediction of excessive severity in static regimes (Section [5](https://arxiv.org/html/2512.01112v1#S5 "5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization")), πqueue\pi\_{\text{queue}} amassed a cumulative overshoot of $630M (Figure [3](https://arxiv.org/html/2512.01112v1#S9.F3 "Figure 3 ‣ Overshoot and Efficiency. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization")).
While πsmart\pi\_{\text{smart}} eliminates this technical inefficiency by capping haircuts at the deficit, it does so by concentrating losses on the largest winners.
This triggers the adverse selection feedback loop: πsmart\pi\_{\text{smart}} induces high churn among liquidity providers, paradoxically resulting in a larger residual deficit than the dynamic policies (Figure [4](https://arxiv.org/html/2512.01112v1#S9.F4 "Figure 4 ‣ The ADL Trilemma. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization")).

![Refer to caption](adl-simulation-retry/results/overshoot_time_series_with_cumulative.png)


Figure 3: ADL overshoot (Ht−DtH\_{t}-D\_{t}). Dashed: per-shock overshoot. Solid: cumulative overshoot. The static policy πqueue\pi\_{\text{queue}} accumulates ≈$​630\approx\mathdollar 630M of excess haircutting. Dynamic policies (πmd,πvec\pi\_{\text{md}},\pi\_{\text{vec}}) keep overshoot negligible by construction, while πexp\pi\_{\text{exp}} maintains it within a bounded constant factor.

##### The ADL Trilemma.

We analyze the ADL trilemma (Proposition [2.1](https://arxiv.org/html/2512.01112v1#S2.Thmtheorem1 "Proposition 2.1 (Trilemma, Informal). ‣ Three competing desiderata. ‣ 2.5 ADL Trilemma ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization") empirically by looking at the components of regret for each policy.
These components represent the shortfall, fairness, and revenue loss realized by using each ADL policy.
Figure [7](https://arxiv.org/html/2512.01112v1#S9.F7 "Figure 7 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") anchors the “solvency-at-any-cost” corner of the trilemma: πqueue\pi\_{\text{queue}} slashes residual deficits (i.e., higher solvency) yet incurs runaway overshoot and fairness penalties (i.e., lower fairness and revenue).
Figure [8](https://arxiv.org/html/2512.01112v1#S9.F8 "Figure 8 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") shows that capping overshoot via πsmart\pi\_{\text{smart}} still leaves concentrated losses (i.e., low fairness) and elevated residual deficits once churn feedback kicks in (i.e., lower long term revenue).
Figures [9](https://arxiv.org/html/2512.01112v1#S9.F9 "Figure 9 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") and [10](https://arxiv.org/html/2512.01112v1#S9.F10 "Figure 10 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") illustrate how dynamic mirror-descent controllers match the queue’s residual deficits without its welfare cost, i.e., they have better revenue preserving properties than Queue while preserving approximately the same amount of solvency.
On the other hand, Figure [11](https://arxiv.org/html/2512.01112v1#S9.F11 "Figure 11 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") demonstrates that (static) exponential backoff strategies can be competitive with dynamic policies if the deficit is sufficiently bounded.
By jointly optimizing allocation and severity, Figure [12](https://arxiv.org/html/2512.01112v1#S9.F12 "Figure 12 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") shows πvec\pi\_{\text{vec}} delivering the fairest loss sharing and the steepest long term revenue recovery.

![Refer to caption](adl-simulation-retry/results/deficit_flow/outstanding_overlay.png)


Figure 4: Outstanding negative equity (cumulative residual deficits). Lower is better. Despite its aggression, πqueue\pi\_{\text{queue}} fails to clear the deficit effectively due to feedback loops. πexp\pi\_{\text{exp}} achieves competitive solvency without the welfare cost.

![Refer to caption](adl-simulation-retry/results/top_winner_haircut_time_series.png)


Figure 5: Largest winner haircut (USD). πqueue\pi\_{\text{queue}} places a massive, spikey burden on single participants. Dynamic policies (πmd,πexp\pi\_{\text{md}},\pi\_{\text{exp}}) distribute the load, respecting fairness constraints.

![Refer to caption](adl-simulation-retry/results/ptsr_pmr_time_series.png)


Figure 6: PTSR (top) and PMR (bottom) on log scale. πqueue\pi\_{\text{queue}} exhibits ratios >106>10^{6}, indicating extreme moral hazard. Adaptive policies remain within the theoretical corridor (≈1\approx 1–1010).

##### Regret Decomposition.

Figure [7](https://arxiv.org/html/2512.01112v1#S9.F7 "Figure 7 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") makes clear that overshoot (orange) and fairness (red) dominate the queue baseline.
Figure [8](https://arxiv.org/html/2512.01112v1#S9.F8 "Figure 8 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") cuts the overshoot bar almost entirely but replaces it with a larger residual (blue) mass as liquidity flees.
Mirror-descent controllers in Figures [9](https://arxiv.org/html/2512.01112v1#S9.F9 "Figure 9 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") and [10](https://arxiv.org/html/2512.01112v1#S9.F10 "Figure 10 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") shrink every component simultaneously by aligning severity with observed deficits, with the warm-started variant tightening the residual tail.
Figure [11](https://arxiv.org/html/2512.01112v1#S9.F11 "Figure 11 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") trades a small overshoot allowance for even lower fairness cost, while Figure [12](https://arxiv.org/html/2512.01112v1#S9.F12 "Figure 12 ‣ Regret Decomposition. ‣ 9.2 Results ‣ 9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") compresses all three components and traces the Pareto frontier across solvency, fairness, and revenue.

![Refer to caption](adl-simulation-retry/results/regret_components_queue.png)


Figure 7: Regret decomposition for the production Queue baseline πqueue\pi\_{\text{queue}}. Overshoot (orange) and fairness (red) penalties dominate, illustrating static inefficiency.

![Refer to caption](adl-simulation-retry/results/regret_components_smart_queue.png)


Figure 8: Regret decomposition for the Smart Queue πsmart\pi\_{\text{smart}}. Capping overshoot helps, but churn-driven residual deficits and fairness costs still dominate regret.

![Refer to caption](adl-simulation-retry/results/regret_components_mirror.png)


Figure 9: Regret decomposition for Mirror Descent πmd\pi\_{\text{md}}. Adaptive severity minimizes overshoot while balancing fairness and residual losses.

![Refer to caption](adl-simulation-retry/results/regret_components_dyn2.png)


Figure 10: Regret decomposition for the Dynamic2 controller πdyn2\pi\_{\text{dyn2}}. Warm-started mirror descent keeps overshoot tame while moderating fairness penalties.

![Refer to caption](adl-simulation-retry/results/regret_components_backoff.png)


Figure 11: Regret decomposition for Exponential Backoff πexp\pi\_{\text{exp}}. Feedback-tuned severity contains overshoot without sacrificing solvency or fairness.

![Refer to caption](adl-simulation-retry/results/regret_components_vector.png)


Figure 12: Regret decomposition for Vector Mirror πvec\pi\_{\text{vec}}. Joint severity and allocation updates compress every component, tracing the Pareto frontier.

### 9.3 Interpretation

In aggregate, the empirical evidence of this section strongly suggests that the standard Queue mechanism operates in the unbounded PoA regime defined in Proposition [8.3](https://arxiv.org/html/2512.01112v1#S8.Thmtheorem3 "Proposition 8.3 (Informal). ‣ Why PoA for Nash vs. Stackelberg? ‣ 8.7 Dynamic Phase Transition in ADL ‣ 8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization").
It fails to balance the competing objectives of a perpetuals exchange, sacrificing trader welfare and future revenue for marginal (and often negative) gains in immediate solvency.
The decoupling of severity (θt\theta\_{t}) from allocation (hth\_{t}) via policies like Exponential Backoff (πexp\pi\_{\text{exp}}) offers a strictly dominant strategy, improving fairness and revenue retention without compromising system stability.

Based on these results, we offer three concrete prescriptions for Hyperliquid and similar venues:

1. 1.

   *Decouple Severity from Allocation.* Current mechanisms conflate the decision of *how much* to haircut with *who* to haircut. We recommend adopting a scalar feedback controller (e.g., πexp\pi\_{\text{exp}} or πmd\pi\_{\text{md}}) to determine the aggregate severity θt\theta\_{t} dynamically based on the observed deficit DtD\_{t}.
2. 2.

   *Adopt Fairer Allocations.* The greedy ranking used by πqueue\pi\_{\text{queue}} maximizes the fairness penalty and adverse selection. Shifting to a *Levered Pro-Rata* (LPR) rule (or the optimized vector hth\_{t} from πvec\pi\_{\text{vec}}) ensures that loss socialization is proportional to risk and capacity, maintaining PTSR≈1\text{PTSR}\approx 1.
3. 3.

   *Implement a Hybrid Controller.* We recommend a hybrid approach: use LPR (Eq. [21](https://arxiv.org/html/2512.01112v1#S2.E21 "Equation 21 ‣ Pro-Rata Rules. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) for allocation to satisfy fairness constraints, paired with the πexp\pi\_{\text{exp}} controller for severity to manage the deficit. This combination provides the robustness of dynamic severity with the transparency and fairness of pro-rata allocation, minimizing the long-term revenue impact of ADL events.

## 10 Conclusion and Future Work

In this paper, we provide the first formalism for ADL mechanisms that allows us to compare the performance of different policies.
We first that a negative result: it is impossible for a perpetuals to optimize for exchange solvency, long term revenue, and fairness to traders.
We then try to get around the negative result by analyzing strategies that optimize each of these components individually.
Our results demonstrate that the heuristic strategy employed by Hyperliquid, Binance, and others that stems from 2015 is actually suboptimal in all dimensions.
We empirically validate our results on Hyperliquid data from October 10, 2025 and demonstrate the superiority of dynamic and even other static algorithms to the live policy.

Our results suggest a few directions for future inquiry.
Implementing these policies in production has a number of challenges that we don’t consider in the paper.
For instance, as exchanges grow and have many accounts with very smaller notation sizes, it makes more sense to choose a subset of users who are “eligible for ADL”.
This lowers the computational burden of executing ADL during times of duress (when execution latency is high) while also ensuring that smaller users are not subsidizing larger users.
Practical limits on ADL applicability likely change the results we have here and need to be studied further.

ADL policies also likely change in their efficacy if they were able to be executed in a fully privately manner.
In this paper, we ignored modeling execution costs for exchanges upon liquidation and position closure.
The modeling of such execution costs is nuanced and likely leads to incorrect conclusions about ADL if not carefully handled121212See, e.g. Storm2025ADLThread1, Storm2025ADLThread2 for examples of overly naive analyses that conflate execution costs with ADL mechanism design..
When private execution is possible, the impact of these costs is muted as follower strategies are not able to react to ADL shocks.

While centralized exchanges effectively offer ADL privacy (i.e., other users do not know who else was autodeleveraged besides themselves), they still leak information to the market via public changes to the order book.
With superior privacy guarantess (likely provided by fully homomorphic encryption, zero knowledge proofs, and secure multi-party computation), one could imagine ADL policies being able to avoid the adverse selection effects we describe in the follower strategies section.
As ADL mechanisms rely increasingly on backstop liquidity vaults (such as Hyperliquid’s HLP and Lighter’s LLP), privacy of ADL execution becomes increasingly important to reduce costs for the exchange and traders.

Finally, we note that the results in this paper focused on a single margin model, where the posted collateral was the numéraire.
Many exchanges, including Hyperliquid, have cross-margin ADL support.
This changes the modeling of execution costs and forces us to explicitly model market impact on cash / collateral balances.

## 11 Acknowledgments

The author would like to thank Udai Parvathaneni, Nathan Sheng, JD Maturen, Kamil Yusubov, and Luke Sterle from Gauntlet for helpful dicussions around how to quantify realistic ADL scenarios (such as October 10, 2025).
The author would also like to thank Matheus V. X. Ferreira, Guillermo Angeris, Victor Xu, and Vinayak Kurup for helpful discussions.
Finally, the author really appreciates the data provided by SonarX, Hydromancer, and Mauricio Trujillo.

## Notation and conventions

Throughout the appendix we use consistent notation:

* •

  Shocks are indexed by t=1,2,…,Tt=1,2,\dots,T; winners WtW\_{t} with equities et,i>0e\_{t,i}>0 and losers LtL\_{t}.
* •

  Deficit Dt≥0D\_{t}\geq 0; severity θt≥0\theta\_{t}\geq 0; haircut vector ht∈[0,1]|Wt|h\_{t}\in[0,1]^{|W\_{t}|} with survivors st,i=(1−ht,i)​et,is\_{t,i}=(1-h\_{t,i})e\_{t,i}.
* •

  Per–round budget Bt=min⁡{θt​Dt,∑iwt,i}B\_{t}=\min\{\theta\_{t}D\_{t},\ \sum\_{i}w\_{t,i}\} for severity policies and Bt=wt⊤​htB\_{t}=w\_{t}^{\top}h\_{t} for vector policies; Bt⋆=min⁡{Dt,∑iwt,i}B\_{t}^{\star}=\min\{D\_{t},\sum\_{i}w\_{t,i}\}.
* •

  Per–account caps are βt,i∈[0,1]\beta\_{t,i}\in[0,1] so that 0≤ht,i≤βt,i0\leq h\_{t,i}\leq\beta\_{t,i}.
* •

  Risk weights: ρ​(λ)=λ​ψ​(1/λ)\rho(\lambda)=\lambda\,\psi(1/\lambda) and g​(λ)=ρ​(λ)/λg(\lambda)=\rho(\lambda)/\lambda; when ordering by risk we use ρ\rho.
* •

  Orders: x≺wyx\prec\_{w}y denotes weak submajorization (on decreasing rearrangements).
* •

  Asymptotics: Xn≍pYnX\_{n}\asymp\_{p}Y\_{n} means there exist constants c,C>0c,C>0 such that c​|Yn|≤|Xn|≤C​|Yn|c|Y\_{n}|\leq|X\_{n}|\leq C|Y\_{n}| with high probability.

## Appendix A Liquidations, Autodeleveraging, and Insurance Funds

### A.1 Bankruptcy Price Example

We illustrate the bankruptcy price calculation with an example.
Fix ℓmax=10\ell^{\max}=10 (so mI=0.10m\_{I}=0.10) and p0=1p\_{0}=1.
Consider the five running positions from 𝒫5\mathcal{P}\_{5}:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 𝔭A\displaystyle\mathfrak{p}\_{A} | =(q,c,b)=(1, 2,+1),\displaystyle=(q,c,b)=(1,\,2,\,+1), | 𝔭B\displaystyle\mathfrak{p}\_{B} | =(1, 2/3,+1),\displaystyle=(1,\,2/3,\,+1), | 𝔭C\displaystyle\mathfrak{p}\_{C} | =(4, 8/3,−1),\displaystyle=(4,\,8/3,\,-1), |  |
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 𝔭D\displaystyle\mathfrak{p}\_{D} | =(1, 2/19,+1),\displaystyle=(1,\,2/19,\,+1), | 𝔭E\displaystyle\mathfrak{p}\_{E} | =(1, 10/99,−1).\displaystyle=(1,\,10/99,\,-1). |  | | |

Applying Eq. ([10](https://arxiv.org/html/2512.01112v1#S2.E10 "Equation 10 ‣ Bankruptcy Price. ‣ 2.2.1 Liquidation Prices ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) with Γ=0\Gamma=0 and pt=p0=1p\_{t}=p\_{0}=1 gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​k​(𝔭A)\displaystyle p^{bk}(\mathfrak{p}\_{A}) | =max⁡{0, 1−2}=0,\displaystyle=\max\{0,\,1-2\}=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​k​(𝔭B)\displaystyle p^{bk}(\mathfrak{p}\_{B}) | =1−23=13,\displaystyle=1-\tfrac{2}{3}=\tfrac{1}{3}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​k​(𝔭C)\displaystyle p^{bk}(\mathfrak{p}\_{C}) | =1− 8/3−4=1+23=53​(1.6667),\displaystyle=1-\tfrac{\,8/3\,}{-4}=1+\tfrac{2}{3}=\tfrac{5}{3}\ (1.6667), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​k​(𝔭D)\displaystyle p^{bk}(\mathfrak{p}\_{D}) | =1−219≈0.8947,\displaystyle=1-\tfrac{2}{19}\approx 0.8947, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​k​(𝔭E)\displaystyle p^{bk}(\mathfrak{p}\_{E}) | =1+1099≈1.1010.\displaystyle=1+\tfrac{10}{99}\approx 1.1010. |  |

Thus A is robust to a full drop to zero; B (long 1.5x) has a low bankruptcy price; C (short 1.5x) bankrupts only if the mark rises above 53\tfrac{5}{3}; D/E (long  9.5x/9.9x) have high bankruptcy prices close to 11, making negative equity likely if liquidations lag.

### A.2 Liquidation Price Example

For μ=0.10\mu=0.10 the liquidation prices evaluate to factors 11−μ\tfrac{1}{1-\mu} for longs and 11+μ\tfrac{1}{1+\mu} for shorts. Using the same five positions with pti=1p\_{t\_{i}}=1 and Γ=0\Gamma=0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^l​i​q​(𝔭A,0.10)\displaystyle\hat{p}^{liq}(\mathfrak{p}\_{A},0.10) | =10.9⋅0=0,\displaystyle=\tfrac{1}{0.9}\cdot 0=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p^l​i​q​(𝔭B,0.10)\displaystyle\hat{p}^{liq}(\mathfrak{p}\_{B},0.10) | =10.9⋅13≈0.3704,\displaystyle=\tfrac{1}{0.9}\cdot\tfrac{1}{3}\approx 0.3704, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p^l​i​q​(𝔭C,0.10)\displaystyle\hat{p}^{liq}(\mathfrak{p}\_{C},0.10) | =11.1⋅53≈1.5152,\displaystyle=\tfrac{1}{1.1}\cdot\tfrac{5}{3}\approx 1.5152, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p^l​i​q​(𝔭D,0.10)\displaystyle\hat{p}^{liq}(\mathfrak{p}\_{D},0.10) | =10.9⋅1719≈0.9942,\displaystyle=\tfrac{1}{0.9}\cdot\tfrac{17}{19}\approx 0.9942, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p^l​i​q​(𝔭E,0.10)\displaystyle\hat{p}^{liq}(\mathfrak{p}\_{E},0.10) | =11.1⋅10999≈1.0010.\displaystyle=\tfrac{1}{1.1}\cdot\tfrac{109}{99}\approx 1.0010. |  |

Long A would liquidate only if the oracle fell to 0 (i.e., never occurs in practice). The short CC becomes liquidatable only when the oracle exceeds its threshold; the high-leverage long DD and short EE become liquidatable close to 11 if collateral is not topped up.

### A.3 Execution Price Example

We summarize execution with a directional linear impact rule consistent with our notation: selling to close a long uses Ps​e​l​l​(x)=pt−α​xP^{sell}(x)=p\_{t}-\alpha x and buying to close a short uses Pb​u​y​(x)=pt+α​xP^{buy}(x)=p\_{t}+\alpha x with α>0\alpha>0; the volume–weighted execution for a slice is
pe​x​e​c=pt−α2​Δ​q\;p^{exec}=p\_{t}-\tfrac{\alpha}{2}\Delta q if bi=+1b\_{i}=+1 (sell) and pe​x​e​c=pt+α2​Δ​qp^{exec}=p\_{t}+\tfrac{\alpha}{2}\Delta q if bi=−1b\_{i}=-1 (buy).
Directional linear impact with a single α\alpha: selling (closing a long) uses Ps​e​l​l​(x)=pt−α​xP^{sell}(x)=p\_{t}-\alpha x, buying (closing a short) uses Pb​u​y​(x)=pt+α​xP^{buy}(x)=p\_{t}+\alpha x. The slice VWAP over [0,Δ​q][0,\Delta q] is pe​x​e​c=pt∓α2​Δ​qp^{exec}=p\_{t}\mp\tfrac{\alpha}{2}\Delta q (minus for sells, plus for buys). Fix α=1.0\alpha=1.0 and choose Δ​q\Delta q per case:

* •

  𝔭A\mathfrak{p}\_{A} (Long): pt=1.30p\_{t}=1.30, Δ​q=0.5\Delta q=0.5 gives pe​x​e​c=1.30−0.5⋅0.5=1.05p^{exec}=1.30-0.5\cdot 0.5=1.05. Here pb​k​(𝔭A)=max⁡{pt−2,0}=0p^{bk}(\mathfrak{p}\_{A})=\max\{p\_{t}-2,0\}=0, so pe​x​e​c>pb​kp^{exec}>p^{bk}.
* •

  𝔭B\mathfrak{p}\_{B} (Long): pt=0.95p\_{t}=0.95, Δ​q=0.2\Delta q=0.2 gives pe​x​e​c=0.95−0.5⋅0.2=0.85p^{exec}=0.95-0.5\cdot 0.2=0.85. With pb​k​(𝔭B)=max⁡{0.95−23,0}≈0.2833p^{bk}(\mathfrak{p}\_{B})=\max\{0.95-\tfrac{2}{3},0\}\approx 0.2833, we have pe​x​e​c>pb​kp^{exec}>p^{bk}.
* •

  𝔭C\mathfrak{p}\_{C} (Short): pt=1.60p\_{t}=1.60, Δ​q=2.0\Delta q=2.0 gives pe​x​e​c=1.60+0.5⋅2.0=2.60p^{exec}=1.60+0.5\cdot 2.0=2.60. Since pb​k​(𝔭C)=pt+8/34=pt+23=2.2667p^{bk}(\mathfrak{p}\_{C})=p\_{t}+\tfrac{8/3}{4}=p\_{t}+\tfrac{2}{3}=2.2667, pe​x​e​c>pb​kp^{exec}>p^{bk} (adverse for a short).
* •

  𝔭D\mathfrak{p}\_{D} (Long; targeted): pt=0.98p\_{t}=0.98, Δ​q=0.4\Delta q=0.4 gives pe​x​e​c=0.98−0.5⋅0.4=0.78p^{exec}=0.98-0.5\cdot 0.4=0.78. With pb​k​(𝔭D)=pt−219≈0.8747p^{bk}(\mathfrak{p}\_{D})=p\_{t}-\tfrac{2}{19}\approx 0.8747, we achieve pe​x​e​c<pb​kp^{exec}<p^{bk}.
* •

  𝔭E\mathfrak{p}\_{E} (Short): pt=1.05p\_{t}=1.05, Δ​q=0.4\Delta q=0.4 gives pe​x​e​c=1.05+0.5⋅0.4=1.25p^{exec}=1.05+0.5\cdot 0.4=1.25. With pb​k​(𝔭E)=pt+1099≈1.151p^{bk}(\mathfrak{p}\_{E})=p\_{t}+\tfrac{10}{99}\approx 1.151, we have pe​x​e​c>pb​kp^{exec}>p^{bk}.

### A.4 Liquidation Costs Example

To ground the fee model, let τ​(Δ​q)=τf​i​x+ϕm​a​r​k​pt​Δ​q+ϕe​x​e​c​pe​x​e​c​Δ​q\tau(\Delta q)=\tau^{fix}+\phi^{mark}p\_{t}\,\Delta q+\phi^{exec}p^{exec}\,\Delta q as in practice.
Consider pt=1.30p\_{t}=1.30, a slice Δ​q=0.50\Delta q=0.50, and a realized pe​x​e​c=1.32p^{exec}=1.32.
Two parameterizations:

* •

  Binance: (τf​i​x,ϕm​a​r​k,ϕe​x​e​c)=(0, 40​bps, 0)(\tau^{fix},\phi^{mark},\phi^{exec})=(0,\,40\,\mathrm{bps},\,0) [BinanceFuturesInsuranceFund]. Then τ=0.0040⋅1.30⋅0.50=0.0026\tau=0.0040\cdot 1.30\cdot 0.50=0.0026.
* •

  Hyperliquid: (τf​i​x,ϕm​a​r​k,ϕe​x​e​c)=(0, 20​bps, 10​bps)(\tau^{fix},\phi^{mark},\phi^{exec})=(0,\,20\,\mathrm{bps},\,10\,\mathrm{bps}) [HyperliquidDocsLiquidations]. Then τ=0.0020⋅1.30⋅0.50+0.0010⋅1.32⋅0.50≈0.00130+0.00066=0.00196\tau=0.0020\cdot 1.30\cdot 0.50+0.0010\cdot 1.32\cdot 0.50\approx 0.00130+0.00066=0.00196.

Rates and formulas vary by venue and contract; the above are illustrative parameterizations consistent with public documentation that liquidation fees are charged and, on centralized venues like Binance, credited to the insurance fund.

### A.5 Liquidation Strategy Example

Consider short 𝔭E\mathfrak{p}\_{E} when the mark jumps to pt=5.5p\_{t}=5.5 (ignore funding for this step).
Equity before liquidation is e≈cE−qE​(pt−p0)=1099−1⋅4.5≈−4.399e\approx c\_{E}-q\_{E}(p\_{t}-p\_{0})=\tfrac{10}{99}-1\cdot 4.5\approx-4.399.
Let μ=0.10\mu=0.10 and a linear fee τ​(Δ​q)=ϕ​pt​Δ​q\tau(\Delta q)=\phi\,p\_{t}\,\Delta q with ϕ=30\phi=30bps. Suppose execution is pe​x​e​c=5.55p^{exec}=5.55.
Using ([11](https://arxiv.org/html/2512.01112v1#S2.E11 "Equation 11 ‣ Liquidation Strategies. ‣ 2.2.2 Liquidation Mechanics ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) and b=−1b=-1, the minimal slice that restores maintenance solves

|  |  |  |
| --- | --- | --- |
|  | Δ​q=μ​pt​q−eb​(pe​x​e​c−pt)−ϕ​pt+μ​pt=0.1⋅5.5⋅1−(−4.399)−0.05−0.003⋅5.5+0.1⋅5.5≈4.9490.4835≈ 10.24.\Delta q\;=\;\frac{\mu p\_{t}q-e}{\,b(p^{exec}-p\_{t})-\phi p\_{t}+\mu p\_{t}\,}\;=\;\frac{0.1\cdot 5.5\cdot 1-(-4.399)}{-0.05-0.003\cdot 5.5+0.1\cdot 5.5}\ \approx\ \frac{4.949}{0.4835}\ \approx\ 10.24. |  |

Since Δ​q>qE\Delta q>q\_{E}, a greedy policy would fully close E (cap at Δ​q=qE=1\Delta q=q\_{E}=1).

### A.6 Bad Debt Example

Consider the high-leverage long 𝔭D\mathfrak{p}\_{D} and a slice of size Δ​q=0.4\Delta q=0.4 at pt=0.98p\_{t}=0.98.
Suppose the realized execution is pDe​x​e​c=0.78p^{exec}\_{D}=0.78 while the bankruptcy level is pDb​k≈0.8747p^{bk}\_{D}\approx 0.8747.
Since pDe​x​e​c<pDb​kp^{exec}\_{D}<p^{bk}\_{D}, the realized shortfall from this slice is

|  |  |  |
| --- | --- | --- |
|  | (pDb​k−pDe​x​e​c)​Δ​q≈(0.8747−0.78)⋅0.4≈ 0.0379,(p^{bk}\_{D}-p^{exec}\_{D})\,\Delta q\ \approx\ (0.8747-0.78)\cdot 0.4\ \approx\ 0.0379, |  |

which contributes this amount to the period bad debt DtD\_{t} (cf. Eq. ([13](https://arxiv.org/html/2512.01112v1#S2.E13 "Equation 13 ‣ Bad Debt. ‣ 2.2.2 Liquidation Mechanics ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"))).
Coverage follows the solvency waterfall: the insurance fund pays min⁡{𝖨𝖥t,Dt}\min\{\mathsf{IF}\_{t},D\_{t}\} and any residual shortfall is socialized via ADL (see §[2.3](https://arxiv.org/html/2512.01112v1#S2.SS3 "2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"), §[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
The short case is symmetric: buying to close above bankruptcy (pe​x​e​c>pb​kp^{exec}>p^{bk}) realizes a positive contribution to DtD\_{t}.

### A.7 Anatomy of a Liquidation

Given the bankruptcy, liquidation, and execution prices, we can now describe the high-level algorithm that liquidations follow.
We note that many live liquidation systems will have much more complex liquidation algorithms.
These complexities deal with the coordination costs of coordinating many parties (e.g. oracle provider, liquidators, spot order book liquidity) and precise models that exchanges use for their liquidation strategy.
However, we effectively lump all of these complexities into the definition of the liquidation strategy.
The following liquidation loop is run on every oracle update received by a perpetuals exchange:

* •

  For 𝔭i,t∈𝒫n\mathfrak{p}\_{i,t}\in\mathcal{P}\_{n}

  + –

    If the maintenance margin condition ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) is violated for 𝔭i,t\mathfrak{p}\_{i,t}

    1. 1.

       Remove the position 𝒫n←𝒫n−{𝔭i,t}\mathcal{P}\_{n}\leftarrow\mathcal{P}\_{n}-\{\mathfrak{p}\_{i,t}\}
    2. 2.

       Estimate quantity to liquidate Δ​qi←L​(𝔭i,t,p1:T,p^1:T)\Delta q\_{i}\leftarrow L(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T})
    3. 3.

       Liquidator executes Δ​qi\Delta q\_{i}-sized liquidation and returns their execution price pe​x​e​c​(Δ​qi)p^{exec}(\Delta q\_{i})
    4. 4.

       Update position: 𝔭i,t′=(qi−Δ​qi,ci+pe​x​e​c​Δ​qi−τt​(Δ​qi),ti,bi)\mathfrak{p}^{\prime}\_{i,t}=(q\_{i}-\Delta q\_{i},c\_{i}+p^{exec}\Delta q\_{i}-\tau\_{t}(\Delta q\_{i}),t\_{i},b\_{i})
    5. 5.

       Re-add the position position: 𝒫n←𝒫n∪{𝔭i,t′}\mathcal{P}\_{n}\leftarrow\mathcal{P}\_{n}\cup\{\mathfrak{p}^{\prime}\_{i,t}\}
    6. 6.

       Update equity using ([12](https://arxiv.org/html/2512.01112v1#S2.E12 "Equation 12 ‣ Bad Debt. ‣ 2.2.2 Liquidation Mechanics ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"))
* •

  If 𝔭i,t\mathfrak{p}\_{i,t} has bad debt, e~​(𝔭i,t,p1:T,p^1:T,Δ​qi)<0\tilde{e}(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T},\Delta q\_{i})<0, then

  + –

    Attempt to use the insurance fund, if it exists, to cover the bad debt (§[2.3](https://arxiv.org/html/2512.01112v1#S2.SS3 "2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"))
  + –

    If the insurance fund is insufficiently sized, utilize an ADL mechanism (§[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"))

##### Example.

We illustrate a five–step path using the running set 𝒫5\mathcal{P}\_{5} from above. Take T=5T=5, p0=1p\_{0}=1 and

|  |  |  |
| --- | --- | --- |
|  | p0:5=(1.00, 0.96, 0.94, 0.97, 1.05, 1.12),p^t=pt(t=0,…,5),μ=mI=0.10.p\_{0:5}=(1.00,\ 0.96,\ 0.94,\ 0.97,\ 1.05,\ 1.12),\qquad\hat{p}\_{t}=p\_{t}\ \ (t=0,\dots,5),\qquad\mu=m\_{I}=0.10. |  |

Executions follow the directional linear impact rule introduced in the execution example: for a slice of size Δ​q\Delta q at time tt, the volume-weighted execution is

|  |  |  |  |
| --- | --- | --- | --- |
|  | pe​x​e​c=pt−α2​Δ​q\displaystyle p^{exec}\;=\;p\_{t}-\tfrac{\alpha}{2}\,\Delta q | (sell to close a long, b=+1),\displaystyle\quad\text{(sell to close a long, $b=+1$)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pe​x​e​c=pt+α2​Δ​q\displaystyle p^{exec}\;=\;p\_{t}+\tfrac{\alpha}{2}\,\Delta q | (buy to close a short, b=−1).\displaystyle\quad\text{(buy to close a short, $b=-1$)}. |  |

with α>0\alpha>0. We take α=1.0\alpha=1.0 and choose Δ​q\Delta q via the loop’s liquidation size Δ​qi=L​(𝔭i,t,p1:T,p^1:T)\Delta q\_{i}=L(\mathfrak{p}\_{i,t},p\_{1:T},\hat{p}\_{1:T}).

##### D liquidates at t=2t=2 (no bad debt).

At t=2t=2 we have p2=0.94p\_{2}=0.94 and the maintenance condition ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) is violated for 𝔭D,2\mathfrak{p}\_{D,2}, so the loop attempts a partial liquidation. Take Δ​qD=L​(𝔭D,2,⋅)=0.20\Delta q\_{D}=L(\mathfrak{p}\_{D,2},\cdot)=0.20 for illustration. By ([10](https://arxiv.org/html/2512.01112v1#S2.E10 "Equation 10 ‣ Bankruptcy Price. ‣ 2.2.1 Liquidation Prices ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")),

|  |  |  |
| --- | --- | --- |
|  | pb​k​(𝔭D,2)=p2−219≈ 0.8347,pDe​x​e​c=p2−α2​Δ​qD= 0.94−0.10= 0.84.p^{bk}(\mathfrak{p}\_{D,2})\;=\;p\_{2}-\tfrac{2}{19}\;\approx\;0.8347,\qquad p^{exec}\_{D}\;=\;p\_{2}-\tfrac{\alpha}{2}\Delta q\_{D}\;=\;0.94-0.10\;=\;0.84. |  |

Since pDe​x​e​c>pb​k​(𝔭D,2)p^{exec}\_{D}>p^{bk}(\mathfrak{p}\_{D,2}), this slice executes without bad debt; the position is updated to 𝔭D,2′=(qD−Δ​qD,cD+pDe​x​e​c​Δ​qD−τ2​(Δ​qD),tD,bD)\mathfrak{p}^{\prime}\_{D,2}=(q\_{D}-\Delta q\_{D},\ c\_{D}+p^{exec}\_{D}\Delta q\_{D}-\tau\_{2}(\Delta q\_{D}),\ t\_{D},\ b\_{D}) and equity is updated per ([12](https://arxiv.org/html/2512.01112v1#S2.E12 "Equation 12 ‣ Bad Debt. ‣ 2.2.2 Liquidation Mechanics ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) before reinserting 𝔭D,2′\mathfrak{p}^{\prime}\_{D,2} into 𝒫n\mathcal{P}\_{n}.

##### E becomes bad debt at t=4t=4 (short; liquidation fails).

At t=4t=4 we have p4=1.05p\_{4}=1.05 and ([7](https://arxiv.org/html/2512.01112v1#S2.E7 "Equation 7 ‣ Maintenance Margin. ‣ 2.1 Perpetuals Exchanges. ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) is violated for 𝔭E,4\mathfrak{p}\_{E,4} with bE=−1b\_{E}=-1. The loop selects a liquidation size; take a full close Δ​qE=L​(𝔭E,4,⋅)=1\Delta q\_{E}=L(\mathfrak{p}\_{E,4},\cdot)=1. By ([10](https://arxiv.org/html/2512.01112v1#S2.E10 "Equation 10 ‣ Bankruptcy Price. ‣ 2.2.1 Liquidation Prices ‣ 2.2 Liquidations ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")),

|  |  |  |
| --- | --- | --- |
|  | pb​k​(𝔭E,4)=p4+1099≈ 1.1510,pEe​x​e​c=p4+α2​Δ​qE= 1.05+0.50= 1.55.p^{bk}(\mathfrak{p}\_{E,4})\;=\;p\_{4}+\tfrac{10}{99}\;\approx\;1.1510,\qquad p^{exec}\_{E}\;=\;p\_{4}+\tfrac{\alpha}{2}\Delta q\_{E}\;=\;1.05+0.50\;=\;1.55. |  |

For a short, pe​x​e​c>pb​kp^{exec}>p^{bk} realizes bad debt. The loop records the shortfall

|  |  |  |
| --- | --- | --- |
|  | D4=(pEe​x​e​c−pb​k​(𝔭E,4))​Δ​qE≈ 0.399,e~​(𝔭E,4,p1:5,p^1:5,Δ​qE)=−D4<0,D\_{4}\;=\;\big(p^{exec}\_{E}-p^{bk}(\mathfrak{p}\_{E,4})\big)\,\Delta q\_{E}\;\approx\;0.399,\qquad\tilde{e}\big(\mathfrak{p}\_{E,4},p\_{1:5},\hat{p}\_{1:5},\Delta q\_{E}\big)\;=\;-D\_{4}<0, |  |

and then attempts coverage via the insurance fund (up to min⁡{𝖨𝖥4,D4}\min\{\mathsf{IF}\_{4},D\_{4}\}); any residual shortfall R4R\_{4} defined by Eq. ([16](https://arxiv.org/html/2512.01112v1#S2.E16 "Equation 16 ‣ Insurance Funds. ‣ 2.3 Exchange Solvency ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) is socialized by ADL (see §[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).

### A.8 Optimal Capital Structure Derivation

In this section, we compute the optimal static insurance fund size I​F⋆IF^{\star} that trades off the opportunity cost of capital and expected uncovered losses beyond I​FIF.

##### Setup.

Let DTD\_{T} denote the round deficit with pdf fDf\_{D} and tail F¯D​(x)=Pr⁡[DT>x]\bar{F}\_{D}(x)=\Pr[D\_{T}>x]. Let r>0r>0 be the per-unit capital cost and κ>0\kappa>0 the per-unit social loss weight of uncovered deficits.
The objective is

|  |  |  |
| --- | --- | --- |
|  | minI​F≥0⁡𝒥​(I​F)=r​I​F+κ​𝔼​[(DT−I​F)+]\min\_{IF\geq 0}\ \mathcal{J}(IF)\;=\;r\,IF\;+\;\kappa\,\mathbb{E}\big[(D\_{T}-IF)\_{+}\big] |  |

which equals r​I​F+κ​∫I​F∞(x−I​F)​fD​(x)​𝑑xr\,IF+\kappa\int\_{IF}^{\infty}(x-IF)f\_{D}(x)\,dx when DTD\_{T} is continuous.

##### Optimality condition.

Differentiating yields,

|  |  |  |
| --- | --- | --- |
|  | 𝒥′​(I​F)=r−κ​F¯D​(I​F).\mathcal{J}^{\prime}(IF)=r-\kappa\,\bar{F}\_{D}(IF). |  |

Hence any interior minimizer satisfies F¯D​(I​F⋆)=r/κ\bar{F}\_{D}(IF^{\star})=r/\kappa, i.e.,

|  |  |  |
| --- | --- | --- |
|  | I​F⋆=F¯D−1​(rκ)=VaR 1−r/κ​(DT).IF^{\star}\;=\;\bar{F}\_{D}^{-1}\!\Big(\tfrac{r}{\kappa}\Big)\;=\;\mathrm{VaR}\_{\,1-r/\kappa}(D\_{T}). |  |

##### Assumptions.

In order for this argument to hold, we assume that 𝒥\mathcal{J} is convex and differentiable.
Moreover, if r≥κr\geq\kappa then we define I​F⋆=0IF^{\star}=0, whereas if r→0r\to 0, then I​F⋆→supDTIF^{\star}\rightarrow\sup D\_{T}.

## Appendix B Moral Hazard and Extreme Value Analysis

In this appendix, we formalize the moral hazard properties of ADL mechanisms.
We analyze the optimal control of the Profitability-to-Total-Solvency Ratio (PTSR) and the Profitability-to-Maximum Solvency Ratio (PMR) defined in §[3.1.2](https://arxiv.org/html/2512.01112v1#S3.SS1.SSS2 "3.1.2 ADL-Specific Efficiency Metrics ‣ 3.1 Risk Metrics ‣ 3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization"), and derive their asymptotic behavior under distributional assumptions.

### B.1 Setup and Assumptions

We work in the *large-market limit* (n→∞n\to\infty) under the heavy-tailed assumptions characteristic of crypto markets.
Recall that DTπ=θπ​DTD^{\pi}\_{T}=\theta\_{\pi}D\_{T} is the total socialized loss and ΔTπ=θπ​ΔT\Delta^{\pi}\_{T}=\theta\_{\pi}\Delta\_{T} is the maximum socialized shortfall under policy π\pi.
The survivor of the top winner is denoted ωTπ\omega^{\pi}\_{T}.

##### Assumption A (Regular Variation).

The right tail of the winner equity distribution F¯+​(x)\bar{F}\_{+}(x) and the right tail of the loser shortfall distribution F¯−​(x)\bar{F}\_{-}(x) are regularly varying with indices α+>0\alpha\_{+}>0 and α−>0\alpha\_{-}>0, respectively.
That is, F¯±​(x)=L±​(x)​x−α±\bar{F}\_{\pm}(x)=L\_{\pm}(x)x^{-\alpha\_{\pm}} where L±L\_{\pm} are slowly varying functions.

##### Assumption B (LLN and EVT).

We assume the standard Law of Large Numbers (LLN) and Extreme Value Theory (EVT) scaling limits apply:

* •

  *Aggregates:* WT/n→𝑝μ+W\_{T}/n\xrightarrow{p}\mu\_{+} and DT/n→𝑝μ−D\_{T}/n\xrightarrow{p}\mu\_{-}, for constants μ±∈(0,∞)\mu\_{\pm}\in(0,\infty).
* •

  *Extremes:* The maximum winner ωT\omega\_{T} scales as bkn+=F+←​(1−1/n)b\_{k\_{n}}^{+}=F\_{+}^{\leftarrow}(1-1/n), and the maximum loser shortfall ΔT\Delta\_{T} scales as bmn−=F−←​(1−1/n)b\_{m\_{n}}^{-}=F\_{-}^{\leftarrow}(1-1/n).

### B.2 Optimal Control of Moral Hazard

### B.3 Queue maximizes top-winner damage

We first establish that the *Queue* (or Top-First) rule minimizes the moral hazard metrics defined in the main text for any fixed budget.

###### Proposition B.1 (Queue Minimizes Top Survivor).

Fix a budget H=DTπH=D^{\pi}\_{T}. Let ωT\omega\_{T} be the equity of the largest winner.
For any feasible haircut vector hh satisfying ∑hi​ei=H\sum h\_{i}e\_{i}=H, the top-winner survivor ωTπ\omega^{\pi}\_{T} satisfies

|  |  |  |
| --- | --- | --- |
|  | ωTπ≥max⁡{ωT−H,0}.\omega^{\pi}\_{T}\;\geq\;\max\{\omega\_{T}-H,0\}. |  |

Equality is attained by the Queue rule, which sets the haircut on the top winner to h(1)=min⁡(H/ωT,1)h\_{(1)}=\min(H/\omega\_{T},1) and others to 0 (until h(1)h\_{(1)} saturates).

###### Proof.

Let h(1)h\_{(1)} be the haircut applied to the top winner.
Since hi​ei≥0h\_{i}e\_{i}\geq 0 for all ii, we have h(1)​ωT≤∑ihi​ei=Hh\_{(1)}\omega\_{T}\leq\sum\_{i}h\_{i}e\_{i}=H.
The survivor is ωTπ=ωT−h(1)​ωT≥ωT−H\omega^{\pi}\_{T}=\omega\_{T}-h\_{(1)}\omega\_{T}\geq\omega\_{T}-H.
Since equity cannot be negative, ωTπ≥max⁡{ωT−H,0}\omega^{\pi}\_{T}\geq\max\{\omega\_{T}-H,0\}.
The Queue rule greedily allocates the budget to the largest position, achieving h(1)​ωT=min⁡(H,ωT)h\_{(1)}\omega\_{T}=\min(H,\omega\_{T}), thus attaining the lower bound.
∎

###### Corollary B.2 (Minimality of PTSR/PMR).

Since DTπD^{\pi}\_{T} and ΔTπ\Delta^{\pi}\_{T} are fixed for a given policy severity, the Queue rule minimizes both 𝖯𝖳𝖲𝖱T\mathsf{PTSR}\_{T} and 𝖯𝖬𝖱T\mathsf{PMR}\_{T} among all budget-balanced policies.

##### Gap versus Pro-Rata.

The Queue rule minimizes moral hazard but concentrates the entire loss on the top winner (extreme inequality).
In contrast, the Pro-Rata rule spreads the loss proportionally across all winners, prioritizing *smoothness* (treating similar positions similarly) over minimizing the top survivor’s burden.
For H≤ωTH\leq\omega\_{T}, the survivor gap is

|  |  |  |
| --- | --- | --- |
|  | ωTPR−ωTQueue=H​(1−ωTWT).\omega^{\mathrm{PR}}\_{T}-\omega^{\mathrm{Queue}}\_{T}\;=\;H\left(1-\frac{\omega\_{T}}{W\_{T}}\right). |  |

This gap scales linearly with the budget HH, quantifying the “cost of fairness”: by choosing the smoother Pro-Rata allocation, the system allows the top winner to retain more profit than is strictly necessary to cover the deficit.

### B.4 Asymptotic Scaling Results

We now characterize the asymptotic behavior of PTSR and PMR under “gentle” policies (like Pro-Rata) where the top winner is not specifically targeted.

###### Theorem B.3 (PTSR scaling).

Under Assumptions A and B, for any policy π\pi with severity θn\theta\_{n} where ωTπ∼ωT\omega^{\pi}\_{T}\sim\omega\_{T} (e.g., Pro-Rata with H≪WTH\ll W\_{T}), the PTSR scales as

|  |  |  |
| --- | --- | --- |
|  | 𝖯𝖳𝖲𝖱T​(π)≍pbkn+θn​n.\mathsf{PTSR}\_{T}(\pi)\;\asymp\_{p}\;\frac{b\_{k\_{n}}^{+}}{\theta\_{n}n}. |  |

###### Proof.

By definition, 𝖯𝖳𝖲𝖱T​(π)=𝐄[ωTπ/DTπ]\mathsf{PTSR}\_{T}(\pi)=\mathop{\bf E{}}[\omega^{\pi}\_{T}/D^{\pi}\_{T}].
Under the hypothesis, the numerator scales as ωT∼bkn+\omega\_{T}\sim b\_{k\_{n}}^{+}.
The denominator is DTπ=θn​DTD^{\pi}\_{T}=\theta\_{n}D\_{T}. By the LLN, DT∼μ−​nD\_{T}\sim\mu\_{-}n, so DTπ∼θn​μ−​nD^{\pi}\_{T}\sim\theta\_{n}\mu\_{-}n.
Thus, the ratio scales as bkn+/(θn​n)b\_{k\_{n}}^{+}/(\theta\_{n}n).
Using bounded convergence for the expectation yields the result.
∎

##### Implication.

The behavior of PTSR depends critically on the tail class of winner equities:

* •

  *Pareto (Heavy) Tails:* bkn+≍n1/α+b\_{k\_{n}}^{+}\asymp n^{1/\alpha\_{+}}. Here 𝖯𝖳𝖲𝖱T≍n1/α+−1/θn\mathsf{PTSR}\_{T}\asymp n^{1/\alpha\_{+}-1}/\theta\_{n}. Moral hazard vanishes (𝖯𝖳𝖲𝖱→0\mathsf{PTSR}\to 0) if and only if winners have finite mean (α+>1\alpha\_{+}>1). If α+<1\alpha\_{+}<1, the top survivor grows faster than the aggregate deficit, making the moral hazard wedge permanent.
* •

  *Exponential/Gaussian (Light) Tails:* bkn+≍(log⁡n)γb\_{k\_{n}}^{+}\asymp(\log n)^{\gamma}. Here 𝖯𝖳𝖲𝖱T≍(log⁡n)γ/(n​θn)\mathsf{PTSR}\_{T}\asymp(\log n)^{\gamma}/(n\theta\_{n}). Since polylog growth is slower than linear, moral hazard vanishes rapidly for any non-vanishing severity θn\theta\_{n}, as the aggregate deficit overwhelms the largest individual winner.

###### Theorem B.4 (PMR Scaling).

Assume winner equities have mass ℓn+\ell\_{n}^{+} and loser deficits have mass ℓn−\ell\_{n}^{-} (representing total leverage), and that the underlying normalized distributions satisfy Assumption A.
The PMR scales as:

|  |  |  |
| --- | --- | --- |
|  | 𝖯𝖬𝖱T​(π)≍p1θn⋅ℓn+ℓn−⋅bkn+bmn−≍1θn⋅ℓn+ℓn−⋅n1α+−1α−.\mathsf{PMR}\_{T}(\pi)\;\asymp\_{p}\;\frac{1}{\theta\_{n}}\cdot\frac{\ell\_{n}^{+}}{\ell\_{n}^{-}}\cdot\frac{b\_{k\_{n}}^{+}}{b\_{m\_{n}}^{-}}\;\asymp\;\frac{1}{\theta\_{n}}\cdot\frac{\ell\_{n}^{+}}{\ell\_{n}^{-}}\cdot n^{\frac{1}{\alpha\_{+}}-\frac{1}{\alpha\_{-}}}. |  |

###### Proof.

We have 𝖯𝖬𝖱T​(π)=𝐄[ωTπ/ΔTπ]\mathsf{PMR}\_{T}(\pi)=\mathop{\bf E{}}[\omega^{\pi}\_{T}/\Delta^{\pi}\_{T}].
The top winner scales with total winner leverage mass: ωT∼ℓn+​bkn+\omega\_{T}\sim\ell\_{n}^{+}b\_{k\_{n}}^{+}.
The maximum loser shortfall scales with total loser leverage mass: ΔT∼ℓn−​bmn−\Delta\_{T}\sim\ell\_{n}^{-}b\_{m\_{n}}^{-}.
The budget balance condition implies ΔTπ=θn​ΔT\Delta^{\pi}\_{T}=\theta\_{n}\Delta\_{T}.
Thus, the ratio scales as

|  |  |  |
| --- | --- | --- |
|  | ℓn+​bkn+θn​ℓn−​bmn−=1θn​ℓn+ℓn−​bkn+bmn−.\frac{\ell\_{n}^{+}b\_{k\_{n}}^{+}}{\theta\_{n}\ell\_{n}^{-}b\_{m\_{n}}^{-}}\;=\;\frac{1}{\theta\_{n}}\frac{\ell\_{n}^{+}}{\ell\_{n}^{-}}\frac{b\_{k\_{n}}^{+}}{b\_{m\_{n}}^{-}}. |  |

Substituting the regular variation scalings bkn+∼n1/α+b\_{k\_{n}}^{+}\sim n^{1/\alpha\_{+}} and bmn−∼n1/α−b\_{m\_{n}}^{-}\sim n^{1/\alpha\_{-}} yields the result.
∎

Theorem [B.4](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem4 "Theorem B.4 (PMR Scaling). ‣ Implication. ‣ B.4 Asymptotic Scaling Results ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") decomposes moral hazard into three components:
(1) *Policy Severity* (1/θn1/\theta\_{n}): Lower severity amplifies PMR.
(2) *Leverage Imbalance* (ℓn+/ℓn−\ell\_{n}^{+}/\ell\_{n}^{-}): If the winning side holds more leverage mass, PMR increases.
(3) *Tail Risk* (n1/α+−1/α−n^{1/\alpha\_{+}-1/\alpha\_{-}}): Heavier winner tails relative to losers drive PMR divergence.
This decomposition highlights that even with fair tails (α+=α−\alpha\_{+}=\alpha\_{-}), a systemic leverage imbalance (ℓn+≫ℓn−\ell\_{n}^{+}\gg\ell\_{n}^{-}) can sustain a high PMR.
Specifically, if the exchange allows winners to be significantly more leveraged than losers (a "risk-on" imbalance), the top winner’s survival will systematically outstrip the worst-case socialized loss, creating a persistent moral hazard where maximal profits are privatized while maximal losses are capped.

### B.5 Relationship to Classical Risk Measures

These two metrics have natural interpretations in terms of financial risk measures.
The deficit DTD\_{T} corresponds to the aggregate *Expected Shortfall* (ES) of the losing tail, while ΔT\Delta\_{T} corresponds to the *Value-at-Risk* (VaR) at the extreme quantile (1/n1/n).
Specifically, PTSR compares the *Maximum Profit* to the *Aggregate Socialized Loss* (ES-like), measuring efficiency in bulk.
PMR compares the *Maximum Profit* to the *Maximum Socialized Loss* (VaR-like), measuring efficiency in the extreme tail.
A high PMR implies that the system permits “unicorn” wins that vastly exceed the worst-case individual losses, potentially incentivizing excessive risk-taking if traders perceive a capped downside but unbounded upside.

We further strengthen the connection to classical risk measures by showing that Queue not only minimizes the top survivor in expectation, but also minimizes it in the sense of VaR and ES at *every* tail level.

###### Proposition B.5 (Queue minimizes VaR/ES of the top survivor).

Fix any budget h≥0h\geq 0 and α∈(0,1)\alpha\in(0,1).
For any feasible haircut vector hh with ∑ihi​ei=h\sum\_{i}h\_{i}e\_{i}=h,

|  |  |  |
| --- | --- | --- |
|  | ωTπ≥(ωT−h)+a.s.\omega^{\pi}\_{T}\;\geq\;(\omega\_{T}-h)\_{+}\quad\text{a.s.} |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | VaRα​(ωTπ)≥VaRα​((ωT−h)+),ESα​(ωTπ)≥ESα​((ωT−h)+).\mathrm{VaR}\_{\alpha}(\omega^{\pi}\_{T})\;\geq\;\mathrm{VaR}\_{\alpha}\big((\omega\_{T}-h)\_{+}\big),\qquad\mathrm{ES}\_{\alpha}(\omega^{\pi}\_{T})\;\geq\;\mathrm{ES}\_{\alpha}\big((\omega\_{T}-h)\_{+}\big). |  |

The Queue rule attains equality. Moreover, the following identities hold:

|  |  |  |
| --- | --- | --- |
|  | VaRα​((ωT−h)+)=max⁡{VaRα​(ωT)−h, 0},\mathrm{VaR}\_{\alpha}\big((\omega\_{T}-h)\_{+}\big)\;=\;\max\{\mathrm{VaR}\_{\alpha}(\omega\_{T})-h,\,0\}, |  |

|  |  |  |
| --- | --- | --- |
|  | ESα​((ωT−h)+)=11−α​∫α1max⁡{VaRu​(ωT)−h, 0}​𝑑u.\mathrm{ES}\_{\alpha}\big((\omega\_{T}-h)\_{+}\big)\;=\;\frac{1}{1-\alpha}\int\_{\alpha}^{1}\max\{\mathrm{VaR}\_{u}(\omega\_{T})-h,\,0\}\,du. |  |

###### Proof.

The pointwise lower bound ωTπ≥(ωT−h)+\omega^{\pi}\_{T}\geq(\omega\_{T}-h)\_{+} follows from the budget constraint and nonnegativity of haircuts, as in Proposition [B.1](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem1 "Proposition B.1 (Queue Minimizes Top Survivor). ‣ B.3 Queue maximizes top-winner damage ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").
Monotonicity of risk measures implies that if X≥YX\geq Y almost surely, then VaRα​(X)≥VaRα​(Y)\mathrm{VaR}\_{\alpha}(X)\geq\mathrm{VaR}\_{\alpha}(Y) and ESα​(X)≥ESα​(Y)\mathrm{ES}\_{\alpha}(X)\geq\mathrm{ES}\_{\alpha}(Y).
For the identities, observe that x↦(x−h)+x\mapsto(x-h)\_{+} is nondecreasing; hence quantiles shift: VaRα​((X−h)+)=max⁡{VaRα​(X)−h,0}\mathrm{VaR}\_{\alpha}((X-h)\_{+})=\max\{\mathrm{VaR}\_{\alpha}(X)-h,0\}.
The ES identity follows from the Kusuoka representation [Kusuoka2001] ESα​(Z)=11−α​∫α1VaRu​(Z)​𝑑u\mathrm{ES}\_{\alpha}(Z)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\mathrm{VaR}\_{u}(Z)\,du applied to Z=(X−h)+Z=(X-h)\_{+}.
∎

##### Implication for severity design.

For a random budget H=θn​DTH=\theta\_{n}D\_{T}, apply Theorem [B.5](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem5 "Proposition B.5 (Queue minimizes VaR/ES of the top survivor). ‣ B.5 Relationship to Classical Risk Measures ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") conditionally on HH to conclude that Queue minimizes the conditional VaR/ES of the top survivor at every tail level.
When α+>1\alpha\_{+}>1 (finite mean winners), the tail-equivalence property of regularly varying distributions yields

|  |  |  |
| --- | --- | --- |
|  | ESu​(ωT)VaRu​(ωT)→α+α+−1as ​u↑1,\frac{\mathrm{ES}\_{u}(\omega\_{T})}{\mathrm{VaR}\_{u}(\omega\_{T})}\;\to\;\frac{\alpha\_{+}}{\alpha\_{+}-1}\qquad\text{as }u\uparrow 1, |  |

so VaR- and ES-based moral hazard conclusions coincide asymptotically with those of PTSR and PMR.

### B.6 Randomized constructions for moral-hazard examples

##### Extreme-value moral-hazard (principal–agent).

Fix ρ∈(0,1)\rho\in(0,1) and kn=⌊ρ​n⌋k\_{n}=\lfloor\rho n\rfloor. Draw winner equities Yi(n)Y\_{i}^{(n)} i.i.d. Pareto(α+)(\alpha\_{+}) and loser equities Xi(n)X\_{i}^{(n)} with mean μ\mu.
Then Mn+=max⁡Yi(n)≍n1/α+M\_{n}^{+}=\max Y\_{i}^{(n)}\asymp n^{1/\alpha\_{+}} while non-max winners sum to o​(Mn+)o(M\_{n}^{+}).
Losers sum to DT≈μ​nD\_{T}\approx\mu n.
For fixed severity θn≡θ¯\theta\_{n}\equiv\bar{\theta}, the haircut Hn≈θ¯​μ​nH\_{n}\approx\bar{\theta}\mu n exceeds the capacity of non-max winners, forcing the top winner to cover the bulk.
Post-ADL equity is (Mn+−θ¯​μ​n)+→0(M\_{n}^{+}-\bar{\theta}\mu n)\_{+}\to 0 since n1/α+≪nn^{1/\alpha\_{+}}\ll n for α+<1\alpha\_{+}<1.

##### Leverage-imbalance construction.

Fix leverage masses ℓn−≫ℓn+\ell\_{n}^{-}\gg\ell\_{n}^{+}. Draw loser equities Xi(n)X\_{i}^{(n)} i.i.d. Pareto(α−)(\alpha\_{-}), so DT≈Mn−≍n1/α−D\_{T}\approx M\_{n}^{-}\asymp n^{1/\alpha\_{-}}.
Assign winner leverage c​ℓn+c\,\ell\_{n}^{+} to a random index InI\_{n} and distribute the rest evenly.
Then ωn≍(ℓn+/ℓn−)​n\omega\_{n}\asymp(\ell\_{n}^{+}/\ell\_{n}^{-})n.
This satisfies Proposition [5.2](https://arxiv.org/html/2512.01112v1#S5.Thmtheorem2 "Proposition 5.2 (Informal). ‣ Main Result. ‣ 5.2 Excessive leverage guarantees large maximal trader loss ‣ 5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization") assumptions, yielding the claimed threshold.

## Appendix C Theoretical Properties of Capped Pro-Rata

We formalize the theoretical properties of the capped pro-rata rule.
We note that the capped pro-rata algorithm in Algorithm [1](https://arxiv.org/html/2512.01112v1#alg1 "Algorithm 1 ‣ D.1 Capped Pro-Rata Water-Filling ‣ Appendix D Algorithms for Pro-Rata Haircut Rules ‣ Autodeleveraging: Impossibilities and Optimization") is a standard water-filling algorithm [BoydVandenberghe2004].
The most similar known prior work to this appendix is the study of how such algorithms provide sybil resistance in concave games in decentralized systems [johnson2023concave].
One can view our result as a generalization of this result.

##### Properties of ADL rules.

Fix time TT, state 𝒫n\mathcal{P}\_{n}, winners 𝒲T\mathcal{W}\_{T}, and equities ei=(eT​(𝔭i))+e\_{i}=(e\_{T}(\mathfrak{p}\_{i}))\_{+}.
Let sπ,i=(1−hπ,i)​eis\_{\pi,i}=(1-h\_{\pi,i})e\_{i} be the surviving equity of position ii under ADL policy π\pi.
We say that a feasible ADL rule π\pi (§[2.4](https://arxiv.org/html/2512.01112v1#S2.SS4 "2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")) satisfies:

1. 1.

   *Sybil resistance:* Outcomes are invariant to splitting/merging accounts. For any split ei=∑a=1rzae\_{i}=\sum\_{a=1}^{r}z\_{a}, the sum of survivors equals the original survivor: ∑asπ,a(i→z)=sπ,i\sum\_{a}s^{(i\to z)}\_{\pi,a}=s\_{\pi,i}.
2. 2.

   *Scale invariance:* sπ​(c​e;θπ)=c​sπ​(e;θπ)s\_{\pi}(ce;\theta\_{\pi})=c\,s\_{\pi}(e;\theta\_{\pi}) for c>0c>0.
3. 3.

   *Monotonicity:* If e1≥⋯≥eke\_{1}\geq\dots\geq e\_{k}, then sπ,1≥⋯≥sπ,ks\_{\pi,1}\geq\dots\geq s\_{\pi,k}.
4. 4.

   *Interior regularity:* The map (e,H)↦sπ​(e;H)(e,H)\mapsto s\_{\pi}(e;H) is C1C^{1} on the interior, i.e., for ei>0e\_{i}>0 for all ii and 0<H<∑iei0<H<\sum\_{i}e\_{i}.

Collectively, we refer to these as the *fairness properties* for an ADL rule.

###### Proposition C.1 (Uniqueness of the Pro-Rata Rule).

If a feasible ADL policy π\pi satisfies the fairness properties, then sπ​(e;H)=sPR​(e;H)s\_{\pi}(e;H)=s^{\mathrm{PR}}(e;H) for all feasible inputs.

###### Proof.

Fix a feasible budget HH (e.g. maximum value of θn​DT\theta\_{n}D\_{T}) and write βi∈(0,1]\beta\_{i}\in(0,1] for the haircut cap on winner ii (as in the capped pro-rata rule ([29](https://arxiv.org/html/2512.01112v1#S6.E29 "Equation 29 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization"))), and sort so that e1≥⋯≥eke\_{1}\geq\cdots\geq e\_{k}.
View the haircuts as a function of the realized budget b∈[0,H]b\in[0,H] and write hi​(b)h\_{i}(b) for the haircut on winner ii when total budget bb has been allocated.
For each bb, define the *active set*

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(b)={i:hi​(b)<βi}A(b)=\{i:\ h\_{i}(b)<\beta\_{i}\} |  | (36) |

of winners whose caps are not yet binding.
Since there are only finitely many caps βi\beta\_{i}, there exists a partition 0=b0<b1<⋯<bL=H0=b\_{0}<b\_{1}<\cdots<b\_{L}=H such that on each open interval Iℓ:=(bℓ−1,bℓ)I\_{\ell}:=(b\_{\ell-1},b\_{\ell}) the active set is constant.
Fix one such interval I=(b−,b+)I=(b\_{-},b\_{+}) and write A=A​(b)A=A(b) for any b∈Ib\in I.
On this interval, by scale invariance on AA (per–unit budget increases all active haircuts at the same rate) and feasibility,

|  |  |  |
| --- | --- | --- |
|  | d​hid​b=1∑j∈Aej(i∈A),d​hid​b=0(i∉A).\frac{dh\_{i}}{db}\;=\;\frac{1}{\sum\_{j\in A}e\_{j}}\quad(i\in A),\qquad\frac{dh\_{i}}{db}=0\quad(i\notin A). |  |

Using the interior regularity property, we can integrate these terms on II.
Integrating from b−b\_{-} to any b∈Ib\in I gives the *unconstrained* evolution

|  |  |  |
| --- | --- | --- |
|  | h~i​(b)={hi​(b−)+b−b−∑j∈Aej(i∈A),hi​(b−)(i∉A).\tilde{h}\_{i}(b)\;=\;\begin{cases}h\_{i}(b\_{-})\;+\;\dfrac{b-b\_{-}}{\sum\_{j\in A}e\_{j}}&(i\in A),\\[4.0pt] h\_{i}(b\_{-})&(i\notin A).\end{cases} |  |

All active coordinates in AA move in lockstep, so on II there exists a scalar function ηI​(b)\eta\_{I}(b) such that

|  |  |  |
| --- | --- | --- |
|  | hi​(b)=min⁡{ηI​(b),βi}(i∈A),hi​(b)=hi​(b−)(i∉A).h\_{i}(b)\;=\;\min\{\eta\_{I}(b),\beta\_{i}\}\quad(i\in A),\qquad h\_{i}(b)=h\_{i}(b\_{-})\quad(i\notin A). |  |

The budget identity can then be written on II as

|  |  |  |
| --- | --- | --- |
|  | b=∑i∉Aei​hi​(b−)+∑i∈Aei​min⁡{ηI​(b),βi},b\;=\;\sum\_{i\notin A}e\_{i}h\_{i}(b\_{-})\;+\;\sum\_{i\in A}e\_{i}\min\{\eta\_{I}(b),\beta\_{i}\}, |  |

which, for fixed b∈Ib\in I, is a continuous strictly increasing function of ηI​(b)\eta\_{I}(b) as long as A≠∅A\neq\emptyset.
Thus for each b∈Ib\in I there is a unique ηI​(b)\eta\_{I}(b) solving the budget identity.
In particular, on the *interior* interval where no caps bind (A={1,…,k}A=\{1,\dots,k\} and b∈(0,WT)b\in(0,W\_{T})), we have hi​(b)=ηI​(b)h\_{i}(b)=\eta\_{I}(b) for all ii so the budget identity reduces to

|  |  |  |
| --- | --- | --- |
|  | b=∑i=1kei​hi​(b)=ηI​(b)​∑i=1kei=ηI​(b)​WT,b\;=\;\sum\_{i=1}^{k}e\_{i}h\_{i}(b)\;=\;\eta\_{I}(b)\sum\_{i=1}^{k}e\_{i}\;=\;\eta\_{I}(b)\,W\_{T}, |  |

which implies ηI​(b)=b/WT\eta\_{I}(b)=b/W\_{T}.
Thus on this interval
sπ,i=(1−ηI​(b))​ei=(1−b/WT)​eis\_{\pi,i}=(1-\eta\_{I}(b))e\_{i}=(1-b/W\_{T})e\_{i}, i.e., proportional to equity.

Sybil resistance implies allocations depend only on total equity: splitting ei=∑azae\_{i}=\sum\_{a}z\_{a} leaves
∑aza​ha​(b)\sum\_{a}z\_{a}h\_{a}(b) and hence the survivor ∑a(1−ha​(b))​za\sum\_{a}(1-h\_{a}(b))z\_{a} unchanged for each bb, so the proportional form on interior intervals is preserved under arbitrary splits.
Monotonicity further restricts how indices can exit the active set as bb increases.
At an endpoint bℓb\_{\ell} where ηI​(bℓ)\eta\_{I}(b\_{\ell}) first hits some cap βm\beta\_{m}, all indices j≥mj\geq m with βj≤βm\beta\_{j}\leq\beta\_{m} must saturate together; otherwise we would have em≥eje\_{m}\geq e\_{j} but (1−hm​(bℓ))​em<(1−hj​(bℓ))​ej(1-h\_{m}(b\_{\ell}))e\_{m}<(1-h\_{j}(b\_{\ell}))e\_{j}, violating monotonicity.
Thus, as we pass from IℓI\_{\ell} to Iℓ+1I\_{\ell+1}, a (possibly empty) tail {j>m}\{j>m\} leaves AA, contributing a fixed amount ∑j>mej​βj\sum\_{j>m}e\_{j}\beta\_{j} to the budget, and the same water-filling argument applies on the remaining head with reduced budget.

Concatenating the solution across all intervals IℓI\_{\ell} yields the reverse–waterfilling form
hi=min⁡{η⋆,βi}h\_{i}=\min\{\eta^{\star},\beta\_{i}\} with η⋆\eta^{\star} chosen so that ∑iei​hi=H\sum\_{i}e\_{i}h\_{i}=H, which is exactly capped pro–rata.
Uniqueness follows either from the strict convexity of the Euclidean projection onto
{h∈[0,1]k:∑iei​hi=H}\{h\in[0,1]^{k}:\ \sum\_{i}e\_{i}h\_{i}=H\} or from the monotone one–dimensional search that defines η⋆\eta^{\star}.
∎

##### Convex Optimality

We now formalize the convex-welfare interpretation of capped pro-rata from §[6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization").
Fix time TT, winners 𝒲T\mathcal{W}\_{T} with equities ei=eT​(𝔭i)+e\_{i}=e\_{T}(\mathfrak{p}\_{i})\_{+}, and effective caps βi=min⁡{h¯i,1−e¯i/eT​(𝔭i)}\beta\_{i}=\min\{\overline{h}\_{i},1-\underline{e}\_{i}/e\_{T}(\mathfrak{p}\_{i})\} defined by the haircut and equity constraints ([22](https://arxiv.org/html/2512.01112v1#S2.E22 "Equation 22 ‣ Per-account constraints. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization"))–([23](https://arxiv.org/html/2512.01112v1#S2.E23 "Equation 23 ‣ Per-account constraints. ‣ 2.4 Autodeleveraging ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
Let BT=θπ​DT​(𝒫n)B\_{T}=\theta\_{\pi}D\_{T}(\mathcal{P}\_{n}) denote the haircut budget from ([30](https://arxiv.org/html/2512.01112v1#S6.E30 "Equation 30 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")), and let ϕ:[0,1]→R\phi:[0,1]\to{\mbox{\bf R}} be a strictly convex increasing function representing per-unit haircut disutility as in ([31](https://arxiv.org/html/2512.01112v1#S6.E31 "Equation 31 ‣ Convex Optimality. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")).
We consider choosing haircuts h=(hi)i∈𝒲Th=(h\_{i})\_{i\in\mathcal{W}\_{T}} to minimize the equity-weighted total disutility ∑i∈𝒲Tei​ϕ​(hi)\sum\_{i\in\mathcal{W}\_{T}}e\_{i}\phi(h\_{i}) subject to the per-account bounds 0≤hi≤βi0\leq h\_{i}\leq\beta\_{i} and the aggregate budget constraint ∑i∈𝒲Tei​hi=BT\sum\_{i\in\mathcal{W}\_{T}}e\_{i}h\_{i}=B\_{T}.

###### Proposition C.2 (Convex optimality).

For any strictly convex increasing ϕ\phi, the unique solution to

|  |  |  |
| --- | --- | --- |
|  | minh​∑i∈𝒲Tei​ϕ​(hi)s.t.∑i∈𝒲Tei​hi=BT,0≤hi≤βi\min\_{h}\ \sum\_{i\in\mathcal{W}\_{T}}e\_{i}\,\phi(h\_{i})\quad\text{s.t.}\quad\sum\_{i\in\mathcal{W}\_{T}}e\_{i}h\_{i}=B\_{T},\quad 0\leq h\_{i}\leq\beta\_{i} |  |

is the capped pro-rata rule ([29](https://arxiv.org/html/2512.01112v1#S6.E29 "Equation 29 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")), i.e., hπC​P,i⋆=min⁡{η⋆,βi}h\_{\pi\_{CP},i}^{\star}=\min\{\eta^{\star},\beta\_{i}\}, where η⋆\eta^{\star} is chosen so that ∑i∈𝒲Tei​hπC​P,i⋆=BT\sum\_{i\in\mathcal{W}\_{T}}e\_{i}h\_{\pi\_{CP},i}^{\star}=B\_{T}.

###### Proof.

The optimization problem is convex with a strictly convex objective and linear constraints, so any point satisfying the Karush–Kuhn–Tucker (KKT) conditions is the unique global minimizer [BoydVandenberghe2004, Ch. 5].
For BTB\_{T} in the interior of the feasible region (0<BT<C​(β)0<B\_{T}<C(\beta), where C​(β)C(\beta) is defined in ([28](https://arxiv.org/html/2512.01112v1#S6.E28 "Equation 28 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization"))), Slater’s condition holds, so KKT conditions are necessary and sufficient.
The Lagrangian is

|  |  |  |
| --- | --- | --- |
|  | ℒ​(h,λ,μ,ν)=∑i∈𝒲Tei​ϕ​(hi)+λ​(∑i∈𝒲Tei​hi−BT)+∑i∈𝒲Tμi​(hi−βi)−∑i∈𝒲Tνi​hi,\mathcal{L}(h,\lambda,\mu,\nu)\;=\;\sum\_{i\in\mathcal{W}\_{T}}e\_{i}\phi(h\_{i})+\lambda\!\left(\sum\_{i\in\mathcal{W}\_{T}}e\_{i}h\_{i}-B\_{T}\right)+\sum\_{i\in\mathcal{W}\_{T}}\mu\_{i}(h\_{i}-\beta\_{i})-\sum\_{i\in\mathcal{W}\_{T}}\nu\_{i}h\_{i}, |  |

with multipliers λ∈R\lambda\in{\mbox{\bf R}} and μi,νi≥0\mu\_{i},\nu\_{i}\geq 0.
Stationarity with respect to hih\_{i} gives

|  |  |  |
| --- | --- | --- |
|  | ei​ϕ′​(hi)+λ​ei+μi−νi=0(i∈𝒲T),e\_{i}\phi^{\prime}(h\_{i})+\lambda e\_{i}+\mu\_{i}-\nu\_{i}=0\quad(i\in\mathcal{W}\_{T}), |  |

together with complementary slackness μi​(hi−βi)=0\mu\_{i}(h\_{i}-\beta\_{i})=0 and νi​hi=0\nu\_{i}h\_{i}=0.
For any index ii with 0<hi<βi0<h\_{i}<\beta\_{i}, we must have μi=νi=0\mu\_{i}=\nu\_{i}=0, so ϕ′​(hi)=−λ\phi^{\prime}(h\_{i})=-\lambda.
Because ϕ′\phi^{\prime} is strictly increasing, this implies hi=ch\_{i}=c for some common scalar cc independent of ii.
If hi=βih\_{i}=\beta\_{i} then μi≥0\mu\_{i}\geq 0 and νi=0\nu\_{i}=0, and if hi=0h\_{i}=0 then νi≥0\nu\_{i}\geq 0 and μi=0\mu\_{i}=0, so in all cases the KKT conditions imply the water-filling form

|  |  |  |
| --- | --- | --- |
|  | hi=min⁡{c,βi}(i∈𝒲T).h\_{i}=\min\{c,\beta\_{i}\}\quad(i\in\mathcal{W}\_{T}). |  |

The budget constraint ∑i∈𝒲Tei​hi=BT\sum\_{i\in\mathcal{W}\_{T}}e\_{i}h\_{i}=B\_{T} then reduces to finding cc such that

|  |  |  |
| --- | --- | --- |
|  | ∑i∈𝒲Tei​min⁡{c,βi}=BT.\sum\_{i\in\mathcal{W}\_{T}}e\_{i}\min\{c,\beta\_{i}\}=B\_{T}. |  |

The left-hand side is continuous and strictly increasing in cc on [0,1][0,1] as long as some βi>0\beta\_{i}>0, so there is a unique c=η⋆c=\eta^{\star} solving this equation.
Thus every KKT point has the capped pro-rata form hi=min⁡{η⋆,βi}h\_{i}=\min\{\eta^{\star},\beta\_{i}\} with η⋆\eta^{\star} determined by the budget, which is exactly the rule in ([29](https://arxiv.org/html/2512.01112v1#S6.E29 "Equation 29 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization")).
Strict convexity of the objective implies this KKT point is the unique global minimizer, proving the claim (see also the standard water-filling derivations in [BoydVandenberghe2004, Ch. 5]).
∎

## Appendix D Algorithms for Pro-Rata Haircut Rules

This appendix collects the explicit water-filling procedures for both the capped pro-rata rule from [Section˜6](https://arxiv.org/html/2512.01112v1#S6 "6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization") and the Risk-Aware Pro-Rata (RAP) rule from [Section˜7](https://arxiv.org/html/2512.01112v1#S7 "7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization").
Each algorithm takes the winner equities {ei}\{e\_{i}\}, effective caps {βi}\{\beta\_{i}\}, and the target budget BT=θπ​DT​(𝒫n)B\_{T}=\theta\_{\pi}D\_{T}(\mathcal{P}\_{n}), returning the optimal haircut vector hh or declaring infeasibility if the aggregate capacity ∑iei​βi\sum\_{i}e\_{i}\beta\_{i} is insufficient.

### D.1 Capped Pro-Rata Water-Filling

The procedure below enforces the constraints in [Equations˜29](https://arxiv.org/html/2512.01112v1#S6.E29 "In Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization") and [30](https://arxiv.org/html/2512.01112v1#S6.E30 "Equation 30 ‣ Definition of the Capped Pro-Rata Rule. ‣ 6 Fairness ‣ Autodeleveraging: Impossibilities and Optimization") by leveling caps until the target budget is met.

Algorithm 1  Capped Pro-Rata Haircut Allocation (Water-Filling)

1:Winner equities e={e1,…,en}e=\{e\_{1},\dots,e\_{n}\}, Effective caps β={β1,…,βn}\beta=\{\beta\_{1},\dots,\beta\_{n}\}, Target budget BTB\_{T}

2:Haircut vector h={h1,…,hn}h=\{h\_{1},\dots,h\_{n}\} or Infeasible

3:C←∑i=1nei​βiC\leftarrow\sum\_{i=1}^{n}e\_{i}\beta\_{i} ⊳\triangleright Compute total maximum capacity

4:if BT>CB\_{T}>C then

5:  return Infeasible

6:end if

7:Sort indices pp such that βp1≤βp2≤⋯≤βpn\beta\_{p\_{1}}\leq\beta\_{p\_{2}}\leq\dots\leq\beta\_{p\_{n}}

8:βp0←0\beta\_{p\_{0}}\leftarrow 0

9:V←0V\leftarrow 0 ⊳\triangleright Cumulative value covered

10:R←∑i=1neiR\leftarrow\sum\_{i=1}^{n}e\_{i} ⊳\triangleright Remaining uncapped equity mass

11:for k=1k=1 to nn do

12:  Δ​β←βpk−βpk−1\Delta\beta\leftarrow\beta\_{p\_{k}}-\beta\_{p\_{k-1}}

13:  Vstep←Δ​β⋅RV\_{\mathrm{step}}\leftarrow\Delta\beta\cdot R

14:  if V+Vstep≥BTV+V\_{\mathrm{step}}\geq B\_{T} then

15:   η←βpk−1+(BT−V)/R\eta\leftarrow\beta\_{p\_{k-1}}+(B\_{T}-V)/R ⊳\triangleright Found the water level η\eta

16:   break

17:  end if

18:  V←V+VstepV\leftarrow V+V\_{\mathrm{step}}

19:  R←R−epkR\leftarrow R-e\_{p\_{k}} ⊳\triangleright User pkp\_{k} becomes fully capped

20:end for

21:if V<BTV<B\_{T} then ⊳\triangleright Handling numerical edge cases

22:  η←βpn\eta\leftarrow\beta\_{p\_{n}}

23:end if

24:for i=1i=1 to nn do

25:  hi←min⁡{η,βi}h\_{i}\leftarrow\min\{\eta,\beta\_{i}\}

26:end for

27:return hh

### D.2 Risk-Aware Pro-Rata Water-Filling

The RAP algorithm augments the capped procedure by prioritizing accounts according to their “cap-to-weight” ratios βi/wi\beta\_{i}/w\_{i}.

Algorithm 2  Risk-Aware Pro-Rata Haircut Allocation (Weighted Water-Filling)

1:Winner equities e={e1,…,en}e=\{e\_{1},\dots,e\_{n}\}, Effective caps β={β1,…,βn}\beta=\{\beta\_{1},\dots,\beta\_{n}\}, Risk weights w={w1,…,wn}w=\{w\_{1},\dots,w\_{n}\}, Target budget BTB\_{T}

2:Haircut vector h={h1,…,hn}h=\{h\_{1},\dots,h\_{n}\} or Infeasible

3:C←∑i=1nei​βiC\leftarrow\sum\_{i=1}^{n}e\_{i}\beta\_{i} ⊳\triangleright Total capacity

4:if BT>CB\_{T}>C then

5:  return Infeasible

6:end if

7:Compute ratios ri←βi/wir\_{i}\leftarrow\beta\_{i}/w\_{i} for all ii (treat wi=0w\_{i}=0 as ri=∞r\_{i}=\infty)

8:Sort indices pp such that rp1≤rp2≤⋯≤rpnr\_{p\_{1}}\leq r\_{p\_{2}}\leq\dots\leq r\_{p\_{n}}

9:rp0←0r\_{p\_{0}}\leftarrow 0

10:V←0V\leftarrow 0 ⊳\triangleright Cumulative value covered

11:Wrem←∑i=1nei​wiW\_{\mathrm{rem}}\leftarrow\sum\_{i=1}^{n}e\_{i}w\_{i} ⊳\triangleright Remaining weighted equity mass

12:for k=1k=1 to nn do

13:  Δ​τ←rpk−rpk−1\Delta\tau\leftarrow r\_{p\_{k}}-r\_{p\_{k-1}}

14:  Vstep←Δ​τ⋅WremV\_{\mathrm{step}}\leftarrow\Delta\tau\cdot W\_{\mathrm{rem}}

15:  if V+Vstep≥BTV+V\_{\mathrm{step}}\geq B\_{T} then

16:   τ←rpk−1+(BT−V)/Wrem\tau\leftarrow r\_{p\_{k-1}}+(B\_{T}-V)/W\_{\mathrm{rem}} ⊳\triangleright Found the scaling factor τ\tau

17:   break

18:  end if

19:  V←V+VstepV\leftarrow V+V\_{\mathrm{step}}

20:  Wrem←Wrem−epk​wpkW\_{\mathrm{rem}}\leftarrow W\_{\mathrm{rem}}-e\_{p\_{k}}w\_{p\_{k}} ⊳\triangleright User pkp\_{k} becomes fully capped

21:end for

22:if V<BTV<B\_{T} then ⊳\triangleright Numerical edge case

23:  τ←rpn\tau\leftarrow r\_{p\_{n}}

24:end if

25:for i=1i=1 to nn do

26:  hi←min⁡{βi,τ​wi}h\_{i}\leftarrow\min\{\beta\_{i},\tau w\_{i}\}

27:end for

28:return hh

## Appendix E Risk-Aware Pro-Rata (RAP)

### E.1 Examples of Risk-Aware Pro-Rata (RAP) and Next Deficit

In this section, we provide detailed numerical examples illustrating the properties of the RAP rule and the impact of post-haircut shocks.

##### RAP Weighting Example.

We illustrate the three choices of risk models on an example at T=2T=2 where the winners are 𝒲2={A,C,E}\mathcal{W}\_{2}=\{A,C,E\} with effective leverages λA,2+≈1.031\lambda^{+}\_{A,2}\approx 1.031, λC,2+≈0.925\lambda^{+}\_{C,2}\approx 0.925, and λE,2+≈1.548\lambda^{+}\_{E,2}\approx 1.548.
Recall that under pro-rata, the normalized shares are siPR∝eT,is^{\mathrm{PR}}\_{i}\propto e\_{T,i}, yielding (sAPR,sCPR,sEPR)≈(0.163,0.728,0.109)(s^{\mathrm{PR}}\_{A},s^{\mathrm{PR}}\_{C},s^{\mathrm{PR}}\_{E})\approx(0.163,0.728,0.109).
For RAP with wi=λi​g​(λi)w\_{i}=\lambda\_{i}g(\lambda\_{i}), the shares allocate proportional to eT,i​wie\_{T,i}w\_{i}.
The resulting shares (order A,C,EA,C,E) are:

* •

  Linear g​(λ)=λg(\lambda)=\lambda: ≈(0.164,0.589,0.246)\approx(0.164,0.589,0.246).
* •

  Power g​(λ)=λ2g(\lambda)=\lambda^{2}: ≈(0.155,0.498,0.348)\approx(0.155,0.498,0.348).
* •

  CVaR g​(λ)=(λ−0.9)+g(\lambda)=(\lambda-0.9)\_{+}: ≈(0.149,0.114,0.737)\approx(0.149,0.114,0.737).

RAP shifts haircut mass toward high-leverage winners; the tilt is mild for linear gg, stronger for λ2\lambda^{2}, and concentrates almost entirely on the over-threshold tail for the CVaR model.

##### Next Deficit and Leverage Sensitivity.

Consider the setup where T=2T=2 with DT≈0.705D\_{T}\approx 0.705 and WT≈7.72W\_{T}\approx 7.72.
Under the normal pro-rata rule, the haircut rate is hTPR≈0.0913h^{\mathrm{PR}}\_{T}\approx 0.0913.
We consider a simple Markovian shock whose direction is uniformly random and whose magnitude grows with the winner leverage mass:

|  |  |  |
| --- | --- | --- |
|  | ZT,i=ξT​ζT,ξT∈{−1,+1}​ equiprobable,ζT=α​ℓT+kT.Z\_{T,i}=\xi\_{T}\zeta\_{T},\quad\xi\_{T}\in\{-1,+1\}\text{ equiprobable},\quad\zeta\_{T}=\alpha\frac{\ell^{+}\_{T}}{k\_{T}}. |  |

With α=1.2\alpha=1.2, the expected next deficit is:

|  |  |  |
| --- | --- | --- |
|  | 𝐄[DT+1next∣ℱT]≈1.46>DT.\mathop{\bf E{}}[D^{\mathrm{next}}\_{T+1}\mid\mathcal{F}\_{T}]\approx 1.46>D\_{T}. |  |

This illustrates a failure mode for pro-rata when the shock kernel scales strongly with leverage: pro-rata shrinks all winners uniformly and leaves effective leverages λT,i\lambda\_{T,i} unchanged, so the shock magnitude ζT\zeta\_{T} is unaffected while residual exposure remains large on high-leverage winners.

##### Correlated Shocks Example.

Consider two winners with equal equity ee and leverage levels λt,1>λt,2≥1\lambda\_{t,1}>\lambda\_{t,2}\geq 1, and budget bt=2​ε​eb\_{t}=2\varepsilon e.
Assume price shocks are AR(1): Zt+2=ρ​Zt+1+εt+2Z\_{t+2}=\rho Z\_{t+1}+\varepsilon\_{t+2}, ρ∈(0,1)\rho\in(0,1).
RAP with wt,i∝λt,i​ψ​(1/λt,i)w\_{t,i}\propto\lambda\_{t,i}\psi(1/\lambda\_{t,i}) puts more haircut mass on account 1 (the higher leverage account).
Assume account 1’s exposure to Zt+1Z\_{t+1} offsets the loss term (a "hedge") in the next step deficit: Dt+1next=(α−β​st,1)​Zt+1D^{\text{next}}\_{t+1}=(\alpha-\beta s\_{t,1})Z\_{t+1}.
Shrinking st,1s\_{t,1} (winner 1’s residual equity) weakens the hedge into t+2t+2.
Since st,1RAP<st,1PRs^{\mathrm{RAP}}\_{t,1}<s^{\mathrm{PR}}\_{t,1}, the two-step sum of deficits StS\_{t} can satisfy St​(htPR)<St​(htRAP)S\_{t}(h^{\mathrm{PR}}\_{t})<S\_{t}(h^{\mathrm{RAP}}\_{t}), even if RAP minimizes the one-step deficit.

##### Exchange Incentive Compatibility Example.

Consider two positions 𝔭A\mathfrak{p}\_{A} (high value, θA=100\theta\_{A}=100) and 𝔭B\mathfrak{p}\_{B} (low value, θB=5\theta\_{B}=5) with equal initial leverage ℓ=1\ell=1.
Suppose the exchange must reduce total leverage by 1 unit.

* •

  RAP (Targeted): Fully liquidates 𝔭A\mathfrak{p}\_{A}. Continuation value: 5​β5\beta.
* •

  Pro-Rata: Reduces both by 50%. Continuation value: 52.5​β52.5\beta.

Pro-rata yields significantly higher utility by preserving the high-value trader, demonstrating that RAP need not be incentive compatible for the exchange.

### E.2 RAP Optimality and Convex Dominance

In this appendix, we prove two statements: 1) RAP optimizes the one-step next deficit ([32](https://arxiv.org/html/2512.01112v1#S7.E32 "Equation 32 ‣ One-step Next Deficit. ‣ 7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization")) and 2) RAP has a smaller residual than any other comonotone haircut rule.

##### RAP optimizes δT\delta\_{T}.

In this section, we briefly show that RAP optimizes the one-step deficit proxy δT\delta\_{T}.
We do this by showing that the weights determined by the perspective transformr ρ​(λ)\rho(\lambda), which define g⋆g^{\star}, optimize δT\delta\_{T}.

###### Proposition E.1.

Fix a round tt with budget bt=θt​|Dt|b\_{t}=\theta\_{t}|D\_{t}| and per-account caps 0≤Ht,i≤10\leq H\_{t,i}\leq 1. For

|  |  |  |
| --- | --- | --- |
|  | δt​(h)=∑i∈Wt(1−ht,i)​λt,i​et,i​ψi​(1λt,i)\delta\_{t}(h)=\sum\_{i\in W\_{t}}(1-h\_{t,i})\,\lambda\_{t,i}e\_{t,i}\,\psi\_{i}\!\Big(\tfrac{1}{\lambda\_{t,i}}\Big) |  |

the capped reverse-waterfilling with weights wt,i=ρ​(λt,i)=λt,i​ψi​(1/λt,i)w\_{t,i}=\rho(\lambda\_{t,i})=\lambda\_{t,i}\psi\_{i}(1/\lambda\_{t,i}) minimizes δt​(h)\delta\_{t}(h) among all hh with ∑iet,i​ht,i=bt\sum\_{i}e\_{t,i}h\_{t,i}=b\_{t} and 0≤ht,i≤Ht,i0\leq h\_{t,i}\leq H\_{t,i}.

###### Proof.

Using ρ​(λ)=λ​ψ​(1/λ)\rho(\lambda)=\lambda\psi(1/\lambda),

|  |  |  |
| --- | --- | --- |
|  | δt​(h)=∑i(1−ht,i)​λt,i​et,i​ψ​(1/λt,i)≡Ch−∑iρ​(λt,i)​et,i​ht,i\delta\_{t}(h)=\sum\_{i}(1-h\_{t,i})\,\lambda\_{t,i}e\_{t,i}\,\psi(1/\lambda\_{t,i})\equiv C\_{h}-\sum\_{i}\rho(\lambda\_{t,i})e\_{t,i}h\_{t,i} |  |

where ChC\_{h} is a constant independent of hh (can depend on λt,i\lambda\_{t,i}).
Maximizing ∑iρ​(λt,i)​et,i​ht,i\sum\_{i}\rho(\lambda\_{t,i})\,e\_{t,i}h\_{t,i} under ∑ist,i=bt\sum\_{i}s\_{t,i}=b\_{t} and 0≤st,i≤et,i​Ht,i0\leq s\_{t,i}\leq e\_{t,i}H\_{t,i} is a fractional knapsack problem solved by sorting the values ρ​(λt,i)\rho(\lambda\_{t,i}).
The optimizer for this problem is reverse-waterfilling [BoydVandenberghe2004]:

|  |  |  |
| --- | --- | --- |
|  | ht,i=min⁡{Ht,i,τt⋆​wt,i},wt,i=ρ​(λt,i),h\_{t,i}=\min\{H\_{t,i},\ \tau^{\star}\_{t}\,w\_{t,i}\},\qquad w\_{t,i}=\rho(\lambda\_{t,i}), |  |

with τt⋆\tau^{\star}\_{t} set by ∑iet,i​ht,i=bt\sum\_{i}e\_{t,i}h\_{t,i}=b\_{t}.
This choice of ww minimizes δt\delta\_{t} among all weighted reverse-waterfilling rules.
∎

##### RAP realizes Schur-convex dominance.

We first note that theoretical results from the measure theoretic literature imply than RAP should provide Schur-convex dominance.
RAP weights wi=λT,i​g​(λT,i)w\_{i}=\lambda\_{T,i}g(\lambda\_{T,i}) can be interpreted as allocating budget proportional to a coherent, law-invariant risk measure.
Specifically, let ρ​(λ)=λ​ψ​(1/λ)\rho(\lambda)=\lambda\,\psi(1/\lambda) be a risk density with ψ\psi convex and nonincreasing.
This corresponds to a spectral risk measure ρ​(X)=∫01ESα​(X)​𝑑μ​(α)\rho(X)=\int\_{0}^{1}\mathrm{ES}\_{\alpha}(X)\,d\mu(\alpha) via the Kusuoka representation [Kusuoka2001, Acerbi2002].
Choosing g​(λ)=ρ​(λ)/λg(\lambda)=\rho(\lambda)/\lambda aligns the RAP allocation with this spectral density.
Known results from [Kusuoka2001] then imply RAP with a “more convex” risk density (in the Schur sense) will weakly Schur-dominate any other weighted pro-rata rule with a less concentrated density.
Instead of utilizing such strong measure theoretic tools, we instead prove this directly below in an elementary manner.

###### Theorem E.2 (Constructive Schur–convex dominance).

Fix TT, budget bTb\_{T}, and caps (βi)(\beta\_{i}). Let ρ\rho be nondecreasing and g⋆​(λ)=ρ​(λ)/λg^{\star}(\lambda)=\rho(\lambda)/\lambda.
Consider any weighted pro-rata rule h(w)h^{(w)} with weights ww.
If the haircut share vector of h(w)h^{(w)} is no more concentrated on high-ρ\rho indices than that of RAP​(g⋆)\mathrm{RAP}(g^{\star}) on any fixed active set, then the residual vector of RAP​(g⋆)\mathrm{RAP}(g^{\star}) weakly submajorizes that of h(w)h^{(w)}:

|  |  |  |
| --- | --- | --- |
|  | zT​(RAP​(g⋆))⪯wzT​(h(w)).z\_{T}(\mathrm{RAP}(g^{\star}))\preceq\_{w}z\_{T}(h^{(w)}). |  |

Thus, for any convex increasing ϕ\phi, ∑ϕ​(zT,i​(RAP))≤∑ϕ​(zT,i​(h(w)))\sum\phi(z\_{T,i}(\mathrm{RAP}))\leq\sum\phi(z\_{T,i}(h^{(w)})).

###### Proof.

We split this proof into three steps.
The first step is analogous to the proof of Proposition [C.1](https://arxiv.org/html/2512.01112v1#A3.Thmtheorem1 "Proposition C.1 (Uniqueness of the Pro-Rata Rule). ‣ Properties of ADL rules. ‣ Appendix C Theoretical Properties of Capped Pro-Rata ‣ Autodeleveraging: Impossibilities and Optimization"), where we analyze the change to the weights on a piecewise constant set of intervals.
The second step is to analyze how the residuals change with budget using the piecewise-constant representation.
Given the change in residual, the final step uses the majorization inequality to show that the residual vector of RAP weakly submajorizes that of any other weighted pro-rata rule.

*Step 1: Active set and parameterization.*
We first define the active set A​(b)A(b) as in ([36](https://arxiv.org/html/2512.01112v1#A3.E36 "Equation 36 ‣ Properties of ADL rules. ‣ Appendix C Theoretical Properties of Capped Pro-Rata ‣ Autodeleveraging: Impossibilities and Optimization")).
Any weighted reverse-waterfilling with weights ww admits the water-level form

|  |  |  |
| --- | --- | --- |
|  | hT,i(w)​(b)=min⁡{βi,τ(w)​(b)​wi},h^{(w)}\_{T,i}(b)\;=\;\min\{\beta\_{i},\ \tau^{(w)}(b)\,w\_{i}\}, |  |

where τ(w)​(b)\tau^{(w)}(b) is chosen so that ∑ieT,i​hT,i(w)​(b)=b\sum\_{i}e\_{T,i}\,h^{(w)}\_{T,i}(b)=b.
On an interval [b0,b1][b\_{0},b\_{1}] with fixed A​(b)A(b) we have

|  |  |  |
| --- | --- | --- |
|  | d​bd​τ(w)=∑j∈A​(b)eT,j​wj,d​hT,i(w)d​b={wi∑j∈A​(b)eT,j​wj,i∈A​(b),0,i∉A​(b).\frac{db}{d\tau^{(w)}}=\sum\_{j\in A(b)}e\_{T,j}w\_{j},\qquad\frac{dh^{(w)}\_{T,i}}{db}\;=\;\begin{cases}\displaystyle\frac{w\_{i}}{\sum\_{j\in A(b)}e\_{T,j}w\_{j}},&i\in A(b),\\[4.30554pt] 0,&i\notin A(b).\end{cases} |  |

*Step 2: Residual dynamics.*
Next we look at how the residuals (e.g. post haircut equity) change with budget.
Write the reweighted residuals as

|  |  |  |
| --- | --- | --- |
|  | zT,i​(b)=ρ​(λT,i)​eT,i​(1−hT,i​(b)).z\_{T,i}(b)\;=\;\rho(\lambda\_{T,i})\,e\_{T,i}\,\bigl(1-h\_{T,i}(b)\bigr). |  |

Then on [b0,b1][b\_{0},b\_{1}],

|  |  |  |
| --- | --- | --- |
|  | d​zT,i(w)d​b={−ρ​(λT,i)​eT,i​wi∑j∈A​(b)eT,j​wj,i∈A​(b),0,i∉A​(b).\frac{dz^{(w)}\_{T,i}}{db}\;=\;\begin{cases}\displaystyle-\frac{\rho(\lambda\_{T,i})\,e\_{T,i}\,w\_{i}}{\sum\_{j\in A(b)}e\_{T,j}w\_{j}},&i\in A(b),\\[4.30554pt] 0,&i\notin A(b).\end{cases} |  |

For RAP​(g⋆)\mathrm{RAP}(g^{\star}) we take wi=ρ​(λT,i)w\_{i}=\rho(\lambda\_{T,i}), giving

|  |  |  |
| --- | --- | --- |
|  | d​zT,i(RAP)d​b={−ρ​(λT,i)2​eT,i∑j∈A​(b)eT,j​ρ​(λT,j),i∈A​(b),0,i∉A​(b).\frac{dz^{(\mathrm{RAP})}\_{T,i}}{db}\;=\;\begin{cases}\displaystyle-\frac{\rho(\lambda\_{T,i})^{2}\,e\_{T,i}}{\sum\_{j\in A(b)}e\_{T,j}\rho(\lambda\_{T,j})},&i\in A(b),\\[4.30554pt] 0,&i\notin A(b).\end{cases} |  |

*Step 3: Majorization at each budget.* On a fixed A​(b)A(b), sort indices by decreasing ρ​(λT,i)\rho(\lambda\_{T,i}).
By the hypothesis that the haircut share vector of h(w)h^{(w)} on A​(b)A(b),

|  |  |  |
| --- | --- | --- |
|  | σi(w)​(b):=eT,i​wi∑j∈A​(b)eT,j​wj,\sigma^{(w)}\_{i}(b)\ :=\ \frac{e\_{T,i}w\_{i}}{\sum\_{j\in A(b)}e\_{T,j}w\_{j}}, |  |

is no more concentrated on high-ρ\rho indices than the RAP share
σi(RAP)​(b)=eT,i​ρ​(λT,i)∑j∈A​(b)eT,j​ρ​(λT,j)\sigma^{(\mathrm{RAP})}\_{i}(b)=\frac{e\_{T,i}\rho(\lambda\_{T,i})}{\sum\_{j\in A(b)}e\_{T,j}\rho(\lambda\_{T,j})}, the rearrangement/majorization inequality implies that for every kk,

|  |  |  |
| --- | --- | --- |
|  | ∑i≤kd​zT,(i)(RAP)d​b≤∑i≤kd​zT,(i)(w)d​b\sum\_{i\leq k}\!\frac{dz^{(\mathrm{RAP})}\_{T,(i)}}{db}\;\leq\;\sum\_{i\leq k}\!\frac{dz^{(w)}\_{T,(i)}}{db} |  |

where (i)(i) denotes the order by decreasing ρ\rho.
Hence the instantaneous decrease vector under RAP weakly submajorizes that under h(w)h^{(w)} on [b0,b1][b\_{0},b\_{1}].
Integrating over bb preserves ≺w\prec\_{w} on the interval, and concatenating the finitely many intervals where A​(b)A(b) changes preserves the order overall:
zT​(RAP​(g⋆))⪯wzT​(h(w))z\_{T}(\mathrm{RAP}(g^{\star}))\preceq\_{w}z\_{T}(h^{(w)}).
Schur–convexity then yields the separable convex loss comparison.
∎

### E.3 Example of the Solvency vs. Long-Term Revenue Trade-Off

This example illustrates a fundamental tension: the risk-minimizing policy (RAP) may be suboptimal for the exchange’s long-term value (LTV) because it disproportionately liquidates high-leverage users who generate the most fees. Under certain conditions, a “fairer” policy like Pro-Rata (PR), which preserves these high-value users, yields higher total utility for the exchange.

##### Setup.

Consider an exchange with two profitable users i∈{H,L}i\in\{H,L\}. User HH is high-leverage (λH>λL\lambda\_{H}>\lambda\_{L}) and high-revenue; user LL is safer but generates less fee volume.
The exchange must raise a budget bb via haircuts h=(hH,hL)h=(h\_{H},h\_{L}) to cover a deficit.
Its objective combines immediate safety (minimizing insolvency risk) and future revenue (LTV):

|  |  |  |
| --- | --- | --- |
|  | Uexch​(h)=−Loss​(h)⏟Immediate Safety+β​∑i∈{H,L}θi​(1−hi)​λi⏟Future Revenue (LTV),U^{\mathrm{exch}}(h)\;=\;\underbrace{-\mathrm{Loss}(h)}\_{\text{Immediate Safety}}\;+\;\underbrace{\beta\sum\_{i\in\{H,L\}}\theta\_{i}(1-h\_{i})\lambda\_{i}}\_{\text{Future Revenue (LTV)}}, |  |

where Loss​(h)=L0−αH​hH−αL​hL\mathrm{Loss}(h)=L\_{0}-\alpha\_{H}h\_{H}-\alpha\_{L}h\_{L} is the expected insurance fund draw, and θi​λi\theta\_{i}\lambda\_{i} is the expected future fee revenue per unit of equity from user ii.
We assume αH/eH>αL/eL\alpha\_{H}/e\_{H}>\alpha\_{L}/e\_{L}, meaning user HH provides the cheapest risk reduction per dollar of haircut.

##### Policy Comparison.

We compare two policies:

* •

  *RAP (Risk-Minimizing):* Prioritizes risk reduction above all.
  Since HH offers the best “bang for the buck” in safety (αH/eH>αL/eL\alpha\_{H}/e\_{H}>\alpha\_{L}/e\_{L}),131313The marginal reduction in loss per unit of budget is ∂Loss∂hi​d​hid​(budget)=αiei\frac{\partial\mathrm{Loss}}{\partial h\_{i}}\frac{dh\_{i}}{d(\text{budget})}=\frac{\alpha\_{i}}{e\_{i}}. Since user HH has higher leverage, they have a higher risk coefficient αH\alpha\_{H}, making αH/eH\alpha\_{H}/e\_{H} the steepest descent direction for the loss function. RAP fully targets HH first: hRAP=(b/eH,0)h^{\mathrm{RAP}}=(b/e\_{H},0) (assuming b<eHb<e\_{H}).
* •

  *Pro-Rata (Revenue-Preserving):* Spreads the pain evenly, setting hiPR=beH+eLh^{\mathrm{PR}}\_{i}=\frac{b}{e\_{H}+e\_{L}} for both users. This is less efficient for immediate safety but preserves more of user HH’s position.

##### When an exchange prefers Pro-Rata to maximize long-term revenue.

The exchange prefers PR over RAP when the LTV gain from saving user HH outweighs the increased immediate risk.
The utility difference is:

|  |  |  |
| --- | --- | --- |
|  | Δ​U=Uexch​(hPR)−Uexch​(hRAP)=Δ​hH​(β​θH​λH−αH)⏟Gain from saving ​H−hLPR​(αL−β​θL​λL)⏟Cost of cutting ​L.\Delta U=U^{\mathrm{exch}}(h^{\mathrm{PR}})-U^{\mathrm{exch}}(h^{\mathrm{RAP}})\;=\;\underbrace{\Delta h\_{H}(\beta\theta\_{H}\lambda\_{H}-\alpha\_{H})}\_{\text{Gain from saving }H}\;-\;\underbrace{h^{\mathrm{PR}}\_{L}(\alpha\_{L}-\beta\theta\_{L}\lambda\_{L})}\_{\text{Cost of cutting }L}. |  |

If user HH is sufficiently profitable (θH\theta\_{H} is large), then Δ​U>0\Delta U>0.
Specifically, PR dominates RAP if the relative revenue of the high-leverage user exceeds a threshold:

|  |  |  |
| --- | --- | --- |
|  | θHθL≥Θ⋆=hLPRΔ​hH⋅λLλH+αH−hLPRΔ​hH​αLβ​λH​θL.\frac{\theta\_{H}}{\theta\_{L}}\;\geq\;\Theta^{\star}\;=\;\frac{h^{\mathrm{PR}}\_{L}}{\Delta h\_{H}}\cdot\frac{\lambda\_{L}}{\lambda\_{H}}\;+\;\frac{\alpha\_{H}-\frac{h^{\mathrm{PR}}\_{L}}{\Delta h\_{H}}\alpha\_{L}}{\beta\,\lambda\_{H}\,\theta\_{L}}. |  |

While RAP is “optimal” for preventing immediate insolvency, it can be myopic. If high-leverage traders are the exchange’s cash cows, the exchange has a rational incentive to use Pro-Rata to keep them active, even at the cost of slightly higher short-term risk.

## Appendix F Stackelberg Control

In this appendix, we formalize the results of §[8](https://arxiv.org/html/2512.01112v1#S8 "8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization"), where we model ADL as a Stackelberg game.

### F.1 Opposing Schur orderings for time to solvency and LTV

We formalize the fundamental trade-off between aggressive debt reduction (safety) and trader fee retention (value), formalizing the example in Appendix [E.3](https://arxiv.org/html/2512.01112v1#A5.SS3 "E.3 Example of the Solvency vs. Long-Term Revenue Trade-Off ‣ Appendix E Risk-Aware Pro-Rata (RAP) ‣ Autodeleveraging: Impossibilities and Optimization").
Let nt=|𝒲t|n\_{t}=|\mathcal{W}\_{t}|.
Given any feasible strategy π\pi, write zt​(π)∈R+ntz\_{t}(\pi)\in{\mbox{\bf R}}\_{+}^{n\_{t}} for the vector of residual debts at time tt (sorted in decreasing order).
Let ht,iπ∈[0,1]h\_{t,i}^{\pi}\in[0,1] be the haircut fraction for agent ii with equity et,ie\_{t,i}, so that the haircut mass is mt,i​(π)=ht,iπ​et,im\_{t,i}(\pi)=h\_{t,i}^{\pi}e\_{t,i}.
We write mt​(π)∈R+ntm\_{t}(\pi)\in{\mbox{\bf R}}\_{+}^{n\_{t}} for the corresponding vector of haircut masses.
Let Zt∈R+ntZ\_{t}\in{\mbox{\bf R}}\_{+}^{n\_{t}} denote the equity shock at time tt, following the notation of Section [7](https://arxiv.org/html/2512.01112v1#S7.SS0.SSS0.Px1 "One-step Next Deficit. ‣ 7 Risk-aware Policies (RAP) ‣ Autodeleveraging: Impossibilities and Optimization").
These evolve componentwise as

|  |  |  |
| --- | --- | --- |
|  | zt+1,i​(π)=zt,i​(π)+Zt+1,i−mt,i​(π),z\_{t+1,i}(\pi)=z\_{t,i}(\pi)+Z\_{t+1,i}-m\_{t,i}(\pi), |  |

so summing from τ=0\tau=0 to t−1t-1 yields the conservation–of–mass identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | zt​(π)=z0+∑τ=1tZτ−∑τ=0t−1mτ​(π).z\_{t}(\pi)=z\_{0}+\sum\_{\tau=1}^{t}Z\_{\tau}-\sum\_{\tau=0}^{t-1}m\_{\tau}(\pi). |  | (37) |

This ensures that the equity at time tt is either initial equity, was gained or lost in a price shock, or haircut.

###### Proposition F.1 (Solvency-Revenue Trade-off).

Let AA and BB be two strategies facing the same shock sequence (Zt)t(Z\_{t})\_{t}. Assume:

1. (i)

   *Safety Dominance:* For all t<τsolv​(A)t<\tau\_{\mathrm{solv}}(A), strategy AA maintains weakly smaller residuals than BB in the weak submajorization order: zt​(A)⪯wzt​(B)z\_{t}(A)\preceq\_{w}z\_{t}(B).
2. (ii)

   *Retention Value:* Let Mt​(π):=∑τ=0t−1mτ​(π)M\_{t}(\pi):=\sum\_{\tau=0}^{t-1}m\_{\tau}(\pi) be the cumulative haircut vector and suppose the lifetime value takes the form

   |  |  |  |
   | --- | --- | --- |
   |  | LTV​(π)=∑tβt​Gt​(Mt​(π)),\mathrm{LTV}(\pi)=\sum\_{t}\beta^{t}G\_{t}(M\_{t}(\pi)), |  |

   where each stage value Gt:R+nt→RG\_{t}:{\mbox{\bf R}}\_{+}^{n\_{t}}\to{\mbox{\bf R}} is Schur–concave and coordinate-wise nonincreasing in MtM\_{t} (more cumulative liquidations in the weak submajorization order reduce exchange LTV).

Then:

1. (a)

   τsolv​(A)≤τsolv​(B)\tau\_{\mathrm{solv}}(A)\leq\tau\_{\mathrm{solv}}(B) (Strategy AA is safer).
2. (b)

   LTV​(A)≤LTV​(B)\mathrm{LTV}(A)\leq\mathrm{LTV}(B) (Strategy BB generates more value).

###### Proof.

We prove this in two steps.

*Step 1: Solvency time.*
For any t<τsolv​(A)t<\tau\_{\mathrm{solv}}(A) we have zt​(A)⪯wzt​(B)z\_{t}(A)\preceq\_{w}z\_{t}(B) by (i).
If BB is solvent at some such time tt so that zt​(B)=0z\_{t}(B)=0, then weak submajorization on R+nt{\mbox{\bf R}}\_{+}^{n\_{t}} forces zt​(A)=0z\_{t}(A)=0 as well, since the zero vector is minimal in this order.
Hence BB cannot become solvent strictly before AA, and τsolv​(A)≤τsolv​(B)\tau\_{\mathrm{solv}}(A)\leq\tau\_{\mathrm{solv}}(B) almost surely.

*Step 2: LTV.*
From the conservation–of–mass identity ([37](https://arxiv.org/html/2512.01112v1#A6.E37 "Equation 37 ‣ F.1 Opposing Schur orderings for time to solvency and LTV ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization")) and the fact that z0z\_{0} and (Zτ)τ(Z\_{\tau})\_{\tau} are common across strategies, the cumulative haircuts Mt​(π):=∑τ=0t−1mτ​(π)M\_{t}(\pi):=\sum\_{\tau=0}^{t-1}m\_{\tau}(\pi) satisfy

|  |  |  |
| --- | --- | --- |
|  | Mt​(π)=z0+∑τ=1tZτ−zt​(π),M\_{t}(\pi)=z\_{0}+\sum\_{\tau=1}^{t}Z\_{\tau}-z\_{t}(\pi), |  |

so that

|  |  |  |
| --- | --- | --- |
|  | Mt​(A)−Mt​(B)=zt​(B)−zt​(A).M\_{t}(A)-M\_{t}(B)=z\_{t}(B)-z\_{t}(A). |  |

For each t<τsolv​(A)t<\tau\_{\mathrm{solv}}(A), assumption (i) gives zt​(A)⪯wzt​(B)z\_{t}(A)\preceq\_{w}z\_{t}(B), and subtracting from the common vector z0+∑τ=1tξτz\_{0}+\sum\_{\tau=1}^{t}\xi\_{\tau} reverses the weak submajorization order, yielding Mt​(A)⪰wMt​(B)M\_{t}(A)\succeq\_{w}M\_{t}(B).
By Schur–concavity and coordinate-wise monotonicity of each GtG\_{t} in (ii), this implies Gt​(Mt​(A))≤Gt​(Mt​(B))G\_{t}(M\_{t}(A))\leq G\_{t}(M\_{t}(B)) for all tt, so

|  |  |  |
| --- | --- | --- |
|  | LTV​(A)=∑tβt​Gt​(Mt​(A))≤∑tβt​Gt​(Mt​(B))=LTV​(B).\mathrm{LTV}(A)\;=\;\sum\_{t}\beta^{t}G\_{t}(M\_{t}(A))\;\leq\;\sum\_{t}\beta^{t}G\_{t}(M\_{t}(B))\;=\;\mathrm{LTV}(B). |  |

∎

##### Examples.

We first give a one–step illustration of Proposition [F.1](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem1 "Proposition F.1 (Solvency-Revenue Trade-off). ‣ F.1 Opposing Schur orderings for time to solvency and LTV ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") and then show how its hypotheses can fail for the literal queue versus capped pro–rata policies.

##### Single–period trade-off.

Consider a single round with two winners and common initial residuals z0=(1,1)z\_{0}=(1,1).
Let strategy AA use aggressive haircuts M1​(A)=(1,1)M\_{1}(A)=(1,1), fully clearing both accounts so that z1​(A)=(0,0)z\_{1}(A)=(0,0).
Let strategy BB use milder haircuts M1​(B)=(1,0)M\_{1}(B)=(1,0), clearing only the first account and leaving z1​(B)=(0,1)z\_{1}(B)=(0,1).
Then z1​(A)⪯wz1​(B)z\_{1}(A)\preceq\_{w}z\_{1}(B) and M1​(A)⪰wM1​(B)M\_{1}(A)\succeq\_{w}M\_{1}(B), so the hypotheses of Proposition [F.1](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem1 "Proposition F.1 (Solvency-Revenue Trade-off). ‣ F.1 Opposing Schur orderings for time to solvency and LTV ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") hold with T=1T=1.
For a Schur–concave, coordinate-wise nonincreasing stage value such as

|  |  |  |
| --- | --- | --- |
|  | G1​(M):=−‖M‖22,G\_{1}(M)\;:=\;-\|M\|\_{2}^{2}, |  |

we obtain G1​(M1​(A))=−2G\_{1}(M\_{1}(A))=-2 and G1​(M1​(B))=−1G\_{1}(M\_{1}(B))=-1, so LTV​(A)≤LTV​(B)\mathrm{LTV}(A)\leq\mathrm{LTV}(B), exactly exhibiting the safety–versus–value trade-off.

##### Queue versus capped pro–rata.

Now consider the familiar one–round example with two winners, equities e=(1,1)e=(1,1), and budget b=1b=1.
Under capped pro–rata we have haircuts hPR=(12,12)h^{\mathrm{PR}}=(\tfrac{1}{2},\tfrac{1}{2}), masses mPR=(12,12)m^{\mathrm{PR}}=(\tfrac{1}{2},\tfrac{1}{2}), and residuals zPR=(12,12)z^{\mathrm{PR}}=(\tfrac{1}{2},\tfrac{1}{2}).
Under a queue policy we instead have hQ=(1,0)h^{\mathrm{Q}}=(1,0), so mQ=(1,0)m^{\mathrm{Q}}=(1,0) and zQ=(0,1)z^{\mathrm{Q}}=(0,1).
In weak submajorization order, zPR≺wzQz^{\mathrm{PR}}\prec\_{w}z^{\mathrm{Q}} and likewise mPR≺wmQm^{\mathrm{PR}}\prec\_{w}m^{\mathrm{Q}}.
Thus no choice of labels A,BA,B can make pro–rata simultaneously satisfy the safety-dominance condition zt​(A)⪯wzt​(B)z\_{t}(A)\preceq\_{w}z\_{t}(B) and the “more cumulative haircuts” condition Mt​(A)⪰wMt​(B)M\_{t}(A)\succeq\_{w}M\_{t}(B) in Proposition [F.1](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem1 "Proposition F.1 (Solvency-Revenue Trade-off). ‣ F.1 Opposing Schur orderings for time to solvency and LTV ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization").
Moreover, for any Schur–concave, coordinate-wise nonincreasing GG (for instance G​(M)=−‖M‖22G(M)=-\|M\|\_{2}^{2}), we have G​(mQ)≤G​(mPR)G(m^{\mathrm{Q}})\leq G(m^{\mathrm{PR}}), so in this toy case the safer policy (pro–rata) also delivers *higher* user value.
This shows that while Proposition [F.1](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem1 "Proposition F.1 (Solvency-Revenue Trade-off). ‣ F.1 Opposing Schur orderings for time to solvency and LTV ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") captures a structural opposing–orders phenomenon, its hypotheses do not hold mechanically for every queue versus capped pro–rata comparison.

### F.2 Regret Analysis

In this appendix, we unify the regret analysis for the severity (scalar) and MDIC (vector) controllers. We present a master theorem for Online Mirror Descent (OMD) with constraints and then specialize it to our specific settings.

##### Master Mirror Descent Bound.

Consider a sequence of convex loss functions ft:𝒳→ℝf\_{t}:\mathcal{X}\to\mathbb{R} on a convex set 𝒳\mathcal{X}. A learner chooses xt∈𝒳x\_{t}\in\mathcal{X} and updates using Online Mirror Descent (OMD) with a proximal function (Bregman divergence) D(⋅∥⋅)D(\cdot\|\cdot).

###### Theorem F.2 (OMD Regret).

Let subgradients be bounded by ‖gt‖∗≤G\|g\_{t}\|\_{\*}\leq G in the dual norm, and let the domain diameter be bounded by Dmax2≥maxx⁡D​(x∥x1)D\_{\max}^{2}\geq\max\_{x}D(x\|x\_{1}). With step size ηt=DmaxG​t\eta\_{t}=\frac{D\_{\max}}{G\sqrt{t}}, the regret satisfies:

|  |  |  |
| --- | --- | --- |
|  | ∑t=1Tft​(xt)−minx∈𝒳​∑t=1Tft​(x)≤ 2​Dmax​G​T.\sum\_{t=1}^{T}f\_{t}(x\_{t})-\min\_{x\in\mathcal{X}}\sum\_{t=1}^{T}f\_{t}(x)\;\leq\;2D\_{\max}G\sqrt{T}. |  |

When convex constraints ct​(x)≤0c\_{t}(x)\leq 0 are imposed, applying OMD to the Lagrangian guarantees the same O​(T)O(\sqrt{T}) regret and O​(T−1/2)O(T^{-1/2}) average constraint violation [Hazan2019].

We refer the interested reader to the standard reference [Hazan2019] for a detailed proof.

##### Residual Value Function and Subgradients.

We now describe the residual value function, which is the main subject of mirror descent analysis.
For each round tt, let 𝒲t\mathcal{W}\_{t} be the set of winners with equities et,i>0e\_{t,i}>0, haircut caps βt,i∈[0,1]\beta\_{t,i}\in[0,1], and weights wt,i≥0w\_{t,i}\geq 0.
The residual value function parametrized by a haircut budget bb is

|  |  |  |
| --- | --- | --- |
|  | L~t​(b)=minh∈[0,1]|Wt|​∑i∈Wt(1−hi)​λt,i​et,is.t.∑i∈Wtet,i​hi=b,  0≤hi≤βt,i.\tilde{L}\_{t}(b)\;=\;\min\_{h\in[0,1]^{|W\_{t}|}}\;\sum\_{i\in W\_{t}}(1-h\_{i})\,\lambda\_{t,i}e\_{t,i}\quad\text{s.t.}\quad\sum\_{i\in W\_{t}}e\_{t,i}h\_{i}=b,\;\;0\leq h\_{i}\leq\beta\_{t,i}. |  |

Let τt​(b)\tau\_{t}(b) be the KKT multiplier of the budget constraint at bb.

###### Lemma F.3 (Convexity and subgradient).

For each tt, b↦L~t​(b)b\mapsto\tilde{L}\_{t}(b) is convex, nonincreasing, and piecewise-linear on [0,b¯t][0,\bar{b}\_{t}]; any KKT multiplier −τt​(b)∈∂L~t​(b)-\tau\_{t}(b)\in\partial\tilde{L}\_{t}(b) is a valid subgradient.
Moreover |τt​(b)|≤maxi∈Wt⁡wt,i|\tau\_{t}(b)|\leq\max\_{i\in W\_{t}}w\_{t,i}.

###### Proof.

The program is a linear minimization with a right-hand-side parameter bb.
Sensitivity analysis implies that the optimal value is convex and piecewise-linear in bb, and that the negative of the budget multiplier is a subgradient.
Complementary slackness yields hi=min⁡{βt,i,τt​(b)​wt,i}h\_{i}=\min\{\beta\_{t,i},\tau\_{t}(b)w\_{t,i}\} on active coordinates, which bounds |τt​(b)||\tau\_{t}(b)| by the maximum weight.
∎

Lemma [F.3](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem3 "Lemma F.3 (Convexity and subgradient). ‣ Residual Value Function and Subgradients. ‣ F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") verifies the curvature and bounded-subgradient assumptions required by the master OMD regret theorem (Theorem [F.2](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem2 "Theorem F.2 (OMD Regret). ‣ Master Mirror Descent Bound. ‣ F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization")) hold, so we can directly plug L~t\tilde{L}\_{t} into that framework.

##### Severity Optimization.

In the main text, the severity controller selects a scalar severity θt∈[0,Θt]\theta\_{t}\in[0,\Theta\_{t}] that determines the haircut budget via bt=θt​Dtb\_{t}=\theta\_{t}D\_{t}.
Optimizing over btb\_{t} or θt\theta\_{t} is equivalent; we keep btb\_{t} as the decision variable in the appendix for notational convenience.
The loss is ft​(b)=L~t​(b)f\_{t}(b)=\tilde{L}\_{t}(b), which is convex by Lemma [F.3](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem3 "Lemma F.3 (Convexity and subgradient). ‣ Residual Value Function and Subgradients. ‣ F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization").
We use the Euclidean divergence D​(x∥y)=12​(x−y)2D(x\|y)=\tfrac{1}{2}(x-y)^{2}, reducing OMD to projected gradient descent.

###### Corollary F.4 (Severity Regret).

Let G=maxt,i⁡wt,iG=\max\_{t,i}w\_{t,i} be the bound on subgradients (marginal haircut savings). The severity controller achieves:

|  |  |  |
| --- | --- | --- |
|  | RegretT(sev)≤ 2​b¯​G​T.\mathrm{Regret}\_{T}^{(\mathrm{sev})}\;\leq\;2\bar{b}G\sqrt{T}. |  |

###### Proof.

The domain diameter is b¯\bar{b}. By Lemma [F.3](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem3 "Lemma F.3 (Convexity and subgradient). ‣ Residual Value Function and Subgradients. ‣ F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization"), subgradients correspond to dual variables bounded by the maximum weight GG. The result follows directly from Theorem [F.2](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem2 "Theorem F.2 (OMD Regret). ‣ Master Mirror Descent Bound. ‣ F.2 Regret Analysis ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization").
∎

##### Haircut Optimization (MDIC).

The MDIC controller optimizes ut=(θt,vt)u\_{t}=(\theta\_{t},v\_{t}), where θt\theta\_{t} is severity and vtv\_{t} are ranking weights. We use a block-separable divergence D=Dϕ⊕DΦD=D\_{\phi}\oplus D\_{\Phi}, where DΦD\_{\Phi} is the KL-divergence for the weights.

###### Corollary F.5 (MDIC Regret).

The MDIC controller achieves regret bounded by:

|  |  |  |
| --- | --- | --- |
|  | O​(T​Dϕ​(θ⋆∥θ1)+T​DΦ​(v⋆∥v1)).O\left(\sqrt{TD\_{\phi}(\theta^{\star}\|\theta\_{1})}\;+\;\sqrt{TD\_{\Phi}(v^{\star}\|v\_{1})}\right). |  |

Initializing v1v\_{1} as the uniform distribution over the active winners (so every coordinate is strictly positive) minimizes DΦ​(v⋆∥v1)D\_{\Phi}(v^{\star}\|v\_{1}) to O​(log⁡|𝒲t|)O(\log|\mathcal{W}\_{t}|), yielding better scaling than Euclidean approaches for high-dimensional weight vectors.

###### Proof of the 𝒪​(log⁡|𝒲t|)\mathcal{O}(\log|\mathcal{W}\_{t}|) claim.

The divergence DΦD\_{\Phi} induced by the entropy mirror map equals the Kullback–Leibler divergence:

|  |  |  |
| --- | --- | --- |
|  | DΦ​(v⋆∥v1)=∑i∈Wtvi⋆​log⁡vi⋆v1,i.D\_{\Phi}(v^{\star}\|v\_{1})=\sum\_{i\in W\_{t}}v^{\star}\_{i}\log\frac{v^{\star}\_{i}}{v\_{1,i}}. |  |

Uniform initialization over active winners sets v1,i=1/|𝒲t|v\_{1,i}=1/|\mathcal{W}\_{t}|.
Hence

|  |  |  |
| --- | --- | --- |
|  | DΦ​(v⋆∥v1)=∑ivi⋆​log⁡vi⋆+log⁡|𝒲t|.D\_{\Phi}(v^{\star}\|v\_{1})=\sum\_{i}v^{\star}\_{i}\log v^{\star}\_{i}+\log|\mathcal{W}\_{t}|. |  |

The first term is the negative Shannon entropy of v⋆v^{\star} and is therefore non-positive, implying DΦ​(v⋆∥v1)≤log⁡|Wt|D\_{\Phi}(v^{\star}\|v\_{1})\leq\log|W\_{t}|.
Thus the initialization costs at most O​(log⁡|𝒲t|)O(\log|\mathcal{W}\_{t}|).
∎

### F.3 Stackelberg vs. Nash in a Two-Round ADL Game

This appendix illustrates how the timing of moves affects equilibrium selection in ADL scenarios. We show that while simultaneous moves (Nash) can result in a coordination failure where no one unwinds, sequential moves (Stackelberg) allow a leader to induce the efficient high-unwind outcome.

##### Setup.

Consider two agents i∈{1,2}i\in\{1,2\}, each holding one unit of position.
At t=1t=1, each agent chooses whether to *unwind* (voluntarily close) their position (xi=1x\_{i}=1) or maintain it (xi=0x\_{i}=0).
Let X=x1+x2X=x\_{1}+x\_{2} be the total volume of voluntary unwinds.
We assume that forced ADL occurs at t=2t=2 if this volume is insufficient, i.e., if X<TX<T for some safety threshold T∈(1,2]T\in(1,2].
Voluntary unwinding incurs a transaction cost f>0f>0.
However, if ADL is triggered (because X<TX<T), *every* agent suffers an additional penalty cost c>fc>f, regardless of their individual choice.

##### Simultaneous play (Nash).

In simultaneous play, there are two pure Nash equilibria and we effectively have a Coordination Game [FudenbergTirole1991]:

* •

  *Coordination failure (0,0)(0,0):* If the opponent plays 0, playing 11 results in volume 1<T1<T. ADL still triggers, yielding a total cost f+c>cf+c>c. Thus, the best response is 0, making (0,0)(0,0) stable.
* •

  *Coordination success (1,1)(1,1):* If the opponent plays 11, playing 11 achieves volume 2≥T2\geq T at cost ff. Since f<cf<c, this is preferred to playing 0 (which yields volume 1<T1<T and cost cc), making (1,1)(1,1) stable.

This creates a coordination problem: agents may get stuck in the inefficient (0,0)(0,0) equilibrium where ADL triggers.

###### Proposition F.6 (Stackelberg Dominance).

In sequential play where Agent 1 moves first, the unique subgame-perfect equilibrium is (1,1)(1,1). Agent 2 observes Agent 1 and will match their action (per the logic above). Agent 1 anticipates this: playing 0 leads to (0,0)(0,0) with cost cc, while playing 11 induces (1,1)(1,1) with cost ff. Since f<cf<c, Agent 1 chooses 11, eliminating the bad equilibrium.

##### Numerical Example.

Let f=1f=1, c=5c=5, and T=1.5T=1.5.
In simultaneous play, (0,0)(0,0) is stable because deviating costs 1+5=6>51+5=6>5. In Stackelberg play, the leader plays 11, knowing the follower will respond with 11 (cost 11) rather than triggering ADL (cost 55). From the exchange’s perspective, if ADL losses exceed 2​f2f, the sequential outcome (1,1)(1,1) is strictly preferred as it collects fees and preserves solvency.

### F.4 Follower Strategic Responses

We study two types of follower strategic responses.
First, we show that pro-rata haircuts can lead to low leverage users responding by leaving an exchange earlier than higher leverage users.
This imposes a negative feedback loop as the exchange’s remaining users are higher risk.
Secondly, we study traders who aim to add liquidity to the exchange to cover a deficit.
These traders are speculating on profits that can be made after an ADL event.
We show that such users are incentivized to wait long than the exchange solvency time.

#### F.4.1 Adverse Selection Under Pro-Rata

We model the ADL interaction as a repeated Stackelberg game: in every round tt the exchange (leader) moves first and the surviving winners (followers) best respond.
Each stage looks like a one-round Stackelberg problem, but the outcomes feed into subsequent rounds through the evolving of winner equities eT,ie\_{T,i} and the winning set 𝒲t\mathcal{W}\_{t}.
At the start of round tt the exchange publicly commits to a severity/haircut rule (e.g. queue, pro-rata, RAP) that maps the realized deficit DtD\_{t} and winner book 𝒲t\mathcal{W}\_{t} to haircut shares.
After observing θt\theta\_{t} and anticipating DtD\_{t}, each winner chooses whether to keep its position active (accepting the induced haircut) or to exit/migrate, receiving outside option u0u\_{0}.
Payoffs are Ui(π)=μi−𝐄[Ht,i(π)]U\_{i}^{(\pi)}=\mu\_{i}-\mathop{\bf E{}}[H\_{t,i}^{(\pi)}]; type ii exits whenever this falls below u0u\_{0}.

A *death spiral* occurs when pro-rata haircuts force the safest (low-leverage) winners to churn first, shrinking WtW\_{t}, which in turn raises the future haircut share for the remaining winners, triggering additional exits and further eroding liquidity.
We show that RAP breaks this feedback loop by tilting the follower game against high-leverage accounts.

##### Setup.

Let ii index a profitable trader with effective equity et,ie\_{t,i}, leverage λt,i\lambda\_{t,i}, and expected per-round utility μi\mu\_{i}.
Normalize severity and deficits by θ¯=𝐄[θt]\bar{\theta}=\mathop{\bf E{}}[\theta\_{t}], D¯=𝐄[Dt]\bar{D}=\mathop{\bf E{}}[D\_{t}], and write W¯=𝐄[Wt]\bar{W}=\mathop{\bf E{}}[W\_{t}] for the expected equity mass of winners.
Under pro-rata, the haircut share of ii is st,iPR=et,i/Wts^{\mathrm{PR}}\_{t,i}=e\_{t,i}/W\_{t}, so the realized haircut mass is

|  |  |  |
| --- | --- | --- |
|  | Ht,iPR=θt​Dt​st,iPR.H^{\mathrm{PR}}\_{t,i}=\theta\_{t}D\_{t}\,s^{\mathrm{PR}}\_{t,i}. |  |

For RAP with a nondecreasing weight gg, the share becomes

|  |  |  |
| --- | --- | --- |
|  | st,iRAP=et,i​λt,i​g​(λt,i)∑j∈Wtet,j​λt,j​g​(λt,j),Ht,iRAP=θt​Dt​st,iRAP.s^{\mathrm{RAP}}\_{t,i}=\frac{e\_{t,i}\,\lambda\_{t,i}g(\lambda\_{t,i})}{\sum\_{j\in W\_{t}}e\_{t,j}\,\lambda\_{t,j}g(\lambda\_{t,j})},\qquad H^{\mathrm{RAP}}\_{t,i}=\theta\_{t}D\_{t}\,s^{\mathrm{RAP}}\_{t,i}. |  |

##### Risk-intensity comparator.

Define the equity-weighted market risk intensity at round tt by

|  |  |  |
| --- | --- | --- |
|  | μt(g):=∑j∈Wtet,j​λt,j​g​(λt,j)∑j∈Wtet,j.\mu^{(g)}\_{t}\ :=\ \frac{\sum\_{j\in W\_{t}}e\_{t,j}\,\lambda\_{t,j}g(\lambda\_{t,j})}{\sum\_{j\in W\_{t}}e\_{t,j}}. |  |

###### Lemma F.7 (When RAP burdens a trader less than Pro-Rata).

For any winner ii,

|  |  |  |
| --- | --- | --- |
|  | st,iRAP≤st,iPR⟺λt,i​g​(λt,i)≤μt(g).s^{\mathrm{RAP}}\_{t,i}\ \leq\ s^{\mathrm{PR}}\_{t,i}\quad\Longleftrightarrow\quad\lambda\_{t,i}\,g(\lambda\_{t,i})\ \leq\ \mu^{(g)}\_{t}. |  |

If gg is strictly increasing and λt,i\lambda\_{t,i} is strictly below the equity-weighted market average in the gg-scale, the inequality is strict.

###### Proof.

Compute

|  |  |  |
| --- | --- | --- |
|  | st,iRAPst,iPR=et,i​λt,i​g​(λt,i)/∑jet,j​λt,j​g​(λt,j)et,i/∑jet,j=λt,i​g​(λt,i)μt(g).\frac{s^{\mathrm{RAP}}\_{t,i}}{s^{\mathrm{PR}}\_{t,i}}\ =\ \frac{e\_{t,i}\lambda\_{t,i}g(\lambda\_{t,i})/\sum\_{j}e\_{t,j}\lambda\_{t,j}g(\lambda\_{t,j})}{e\_{t,i}/\sum\_{j}e\_{t,j}}\ =\ \frac{\lambda\_{t,i}g(\lambda\_{t,i})}{\mu^{(g)}\_{t}}. |  |

The claim follows immediately.
∎

##### Participation thresholds.

Each trader type ii has a reservation utility u0u\_{0}: the expected per-round payoff it can secure outside the ADL venue (e.g. by migrating flow to another exchange, posting liquidity in a different product, or simply investing idle cash in a risk-free instrument).
We treat u0>0u\_{0}>0 as exogenous and, unless stated otherwise, common across trader types.
We note that heterogeneity in reservation utility can be captured by indexing it as u0,iu\_{0,i} without changing the argument.

A trader remains active only if the ADL-adjusted payoff exceeds this fallback value.
We formalize this by defining the net utility under policy π\pi as

|  |  |  |
| --- | --- | --- |
|  | Ui(π):=μi−𝐄[Ht,i(π)],U\_{i}^{(\pi)}:=\mu\_{i}-\mathop{\bf E{}}[H\_{t,i}^{(\pi)}], |  |

and saying that ii participates in a given regime iff Ui(π)≥u0U\_{i}^{(\pi)}\geq u\_{0}.
Equivalently, the *participation threshold* is the maximum haircut burden 𝐄[Ht,i(π)]\mathop{\bf E{}}[H\_{t,i}^{(\pi)}] that keeps ii indifferent, namely μi−u0\mu\_{i}-u\_{0}.

###### Corollary F.8 (Pro-Rata death spiral vs. RAP retention).

Fix a type ii and suppose there is a set of rounds of positive probability on which λt,i​g​(λt,i)≤μt(g)\lambda\_{t,i}g(\lambda\_{t,i})\leq\mu^{(g)}\_{t} (so st,iRAP≤st,iPRs^{\mathrm{RAP}}\_{t,i}\leq s^{\mathrm{PR}}\_{t,i} by Lemma [F.7](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem7 "Lemma F.7 (When RAP burdens a trader less than Pro-Rata). ‣ Risk-intensity comparator. ‣ F.4.1 Adverse Selection Under Pro-Rata ‣ F.4 Follower Strategic Responses ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization")).
If, over the same distribution of rounds,

|  |  |  |
| --- | --- | --- |
|  | μi−𝐄[θt​Dt​st,iPR]<u0≤μi−𝐄[θt​Dt​st,iRAP],\mu\_{i}-\mathop{\bf E{}}\big[\theta\_{t}D\_{t}\,s^{\mathrm{PR}}\_{t,i}\big]\ <\ u\_{0}\ \ \leq\ \ \mu\_{i}-\mathop{\bf E{}}\big[\theta\_{t}D\_{t}\,s^{\mathrm{RAP}}\_{t,i}\big], |  |

then the participation constraint fails under pro-rata but holds under RAP: type ii exits in the pro-rata regime while remaining under RAP.

##### Examples and calibration.

Consider two winners, LL (low leverage) and HH (high leverage), who trade for two rounds.
Equities are (eL,eH)=(60,40)(e\_{L},e\_{H})=(60,40), leverage levels are (λL,λH)=(2,6)(\lambda\_{L},\lambda\_{H})=(2,6), expected per-round utilities are (μL,μH)=(12,40)(\mu\_{L},\mu\_{H})=(12,40), and the outside option is u0=2u\_{0}=2.
Each round the deficit equals the total haircut budget (θt=1\theta\_{t}=1) with D1=40D\_{1}=40 and D2=30D\_{2}=30.

*Pro-rata.*
Shares equal equity weights: siPR=ei/(eL+eH)s\_{i}^{\mathrm{PR}}=e\_{i}/(e\_{L}+e\_{H}), so sPR=(0.6,0.4)s^{\mathrm{PR}}=(0.6,0.4) even though both traders lose the *same haircut factor* hPR=HiPR/ei=θt​Dt/Wt=0.4h^{\mathrm{PR}}=H\_{i}^{\mathrm{PR}}/e\_{i}=\theta\_{t}D\_{t}/W\_{t}=0.4.
Round 1 haircut masses are HPR=(24,16)H^{\mathrm{PR}}=(24,16) and utilities are UPR=(−12,24)U^{\mathrm{PR}}=(\!-12,24).
Trader LL churns because ULPR<u0U\_{L}^{\mathrm{PR}}<u\_{0}, leaving only HH for round 2.
With W2=40W\_{2}=40 the next deficit D2=30D\_{2}=30 forces H2,HPR=30H\_{2,H}^{\mathrm{PR}}=30 (i.e., haircut factor 0.750.75), giving U2,HPR=10U\_{2,H}^{\mathrm{PR}}=10; solvency is preserved but the equity base has already halved, so any larger D2D\_{2} would wipe out the last winner, illustrating the death spiral.

*RAP with g​(λ)=λg(\lambda)=\lambda.*
Weights scale as ei​λi2e\_{i}\lambda\_{i}^{2}, so LL’s share collapses to sLRAP=240/(240+1440)≈0.14s\_{L}^{\mathrm{RAP}}=240/(240+1440)\approx 0.14 and HH’s share rises to 0.860.86.
The round 1 haircut factors become hLRAP≈0.095h\_{L}^{\mathrm{RAP}}\approx 0.095 and hHRAP≈0.86h\_{H}^{\mathrm{RAP}}\approx 0.86 (masses HRAP=(5.7,34.3)H^{\mathrm{RAP}}=(5.7,34.3)), yielding URAP=(6.3,5.7)>u0U^{\mathrm{RAP}}=(6.3,5.7)>u\_{0}, so both types remain for round 2.
With both accounts active in round 2, shares remain tilted toward HH and haircuts (4.3,25.7)(4.3,25.7) keep both traders above u0u\_{0}, preventing churn and stabilizing WtW\_{t}.
This concrete two-player, two-round example mirrors the equilibria predicted by Appendix [B.6](https://arxiv.org/html/2512.01112v1#A2.SS6 "B.6 Randomized constructions for moral-hazard examples ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization") and the empirical replay in §[9](https://arxiv.org/html/2512.01112v1#S9 "9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization"): pro-rata drives the safest capital away first, whereas RAP reallocates the burden toward high-leverage accounts and keeps the equity base intact.

#### F.4.2 Waiting Game and MDIC-NW

##### Game.

When an ADL event creates a deficit DtD\_{t}, the exchange moves first: it announces the contemporaneous severity θt\theta\_{t} (hence the haircut budget θt​Dt\theta\_{t}D\_{t}) together with the liquidity premium κt\kappa\_{t} it is willing to pay per unit of external capital.141414In practice, this occurs via either an increase in the expected payment for users who stake to an insurance fund (e.g. [DriftInsuranceFund]) or add assets to an HLP/LLP style vault [HyperliquidHLPVaults, LighterWhitepaper]
A Backstop Liquidity Provider (BLP) then decides whether to intervene immediately by injecting any qt∈[0,Dt]q\_{t}\in[0,D\_{t}] units, or to wait u≥1u\geq 1 additional rounds before posting the same quantity.
Waiting exposes the BLP to time discounting (with a factor βu\beta^{u}) and to the future premium schedule (θt+u,κt+u)(\theta\_{t+u},\kappa\_{t+u}).
The BLP’s payoff from intervening in round t+ut+u with size qq is βu​q​(θt+u−κt+u)\beta^{u}q(\theta\_{t+u}-\kappa\_{t+u}), while the exchange’s objective is to restore solvency before a deadline by ensuring that the entire deficit is filled (so delay harms solvency).

This Stackelberg game involves the exchange posting incentives as leader and BLPs optimally choose a stopping time and quantity as a follower.
The setup captures the “waiting game” intuition: unless the contract guarantees non-negative per-unit surplus right now, rational liquidity providers will defer, pushing resolution beyond the solvency window.
We note that this resembles other waiting games in Maximal Extractable Value (MEV) auctions that have been studied empirically on live systems [messias2025express, mamageishvili2025timeboost].

##### Per-unit surplus and waiting.

Let a Backstop Liquidity Provider (BLP) be able to absorb up to DtD\_{t} units at time tt.
Write the per-unit liquidity premium as κt≥0\kappa\_{t}\geq 0 (execution cost plus risk per unit, e.g., κt=Γt/Dt\kappa\_{t}=\Gamma\_{t}/D\_{t} when the premium is linear in size) and define the per-unit net surplus

|  |  |  |
| --- | --- | --- |
|  | δt:=θt−κt.\delta\_{t}\ :=\ \theta\_{t}-\kappa\_{t}. |  |

If the BLP executes q∈[0,Dt]q\in[0,D\_{t}] units at time tt, the immediate surplus is q​δtq\,\delta\_{t}; deferring the same qq to a later time t+ut+u yields discounted surplus βu​q​δt+u\beta^{u}q\,\delta\_{t+u}.

##### No-wait condition.

We say the exchange enforces a per-unit “No-Wait” constraint when δt≥0\delta\_{t}\geq 0 (equivalently, θt​Dt≥Γt\theta\_{t}D\_{t}\geq\Gamma\_{t} in the linear-premium case).

###### Lemma F.9 (Per-unit No-Wait implies immediate action).

Suppose β∈(0,1]\beta\in(0,1], the exchange enforces δt≥0\delta\_{t}\geq 0, and the net per-unit surplus is nonincreasing over time: δt+u≤δt\delta\_{t+u}\leq\delta\_{t} for all u≥0u\geq 0 (e.g., when θt+u≤θt\theta\_{t+u}\leq\theta\_{t} and κt+u≥κt\kappa\_{t+u}\geq\kappa\_{t}).
Then for any q∈[0,Dt]q\in[0,D\_{t}], executing qq immediately at tt weakly dominates waiting:

|  |  |  |
| --- | --- | --- |
|  | q​δt≥βu​q​δt+u∀u≥0.q\,\delta\_{t}\ \geq\ \beta^{u}\,q\,\delta\_{t+u}\qquad\forall\,u\geq 0. |  |

In particular, the BLP’s optimal stopping time is τ⋆=t\tau^{\star}=t and, if capacity allows, qt⋆=Dtq\_{t}^{\star}=D\_{t}.

###### Proof.

By assumption, δt+u≤δt\delta\_{t+u}\leq\delta\_{t} and βu≤1\beta^{u}\leq 1 for all u≥0u\geq 0, hence βu​q​δt+u≤q​δt\beta^{u}q\,\delta\_{t+u}\leq q\,\delta\_{t} for any fixed q∈[0,Dt]q\in[0,D\_{t}].
Summing over an optimal decomposition of DtD\_{t} into infinitesimal units yields the stated dominance and the immediate-execution optimality.
∎

###### Corollary F.10 (No-Wait bounds solvency recovery).

Let τdef\tau\_{\mathrm{def}} denote the default time and recall the solvency recovery clock τsolv\tau\_{\mathrm{solv}} from §[8.2](https://arxiv.org/html/2512.01112v1#S8.SS2.SSS0.Px4 "Opposing Schur orderings. ‣ 8.2 Why do we need a dynamic model? ‣ 8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization").
If the exchange enforces δt≥0\delta\_{t}\geq 0 for all rounds between τdef\tau\_{\mathrm{def}} and the first round in which the deficit is zero, then τsolv=τdef+1\tau\_{\mathrm{solv}}=\tau\_{\mathrm{def}}+1.
Hence solvency is restored within a single round of the default event.

###### Proof.

Lemma [F.9](https://arxiv.org/html/2512.01112v1#A6.Thmtheorem9 "Lemma F.9 (Per-unit No-Wait implies immediate action). ‣ No-wait condition. ‣ F.4.2 Waiting Game and MDIC-NW ‣ F.4 Follower Strategic Responses ‣ Appendix F Stackelberg Control ‣ Autodeleveraging: Impossibilities and Optimization") implies that at τdef\tau\_{\mathrm{def}} the BLP injects qτdef⋆=Dτdefq\_{\tau\_{\mathrm{def}}}^{\star}=D\_{\tau\_{\mathrm{def}}}, so the entire deficit is covered immediately.
Therefore the insurance fund (or deficit buffer) reaches the safety level δ\delta after the same round, yielding τsolv=τdef+1\tau\_{\mathrm{solv}}=\tau\_{\mathrm{def}}+1.
∎

This result states that if the no-wait condition is enforced, BLPs will inject liquidity such that the solvency time is minimized.
In theory, an exchange can use some of its future revenue or profits (e.g. via token issuance) to enforce the no-wait constraint.

##### Proof of Proposition [8.2](https://arxiv.org/html/2512.01112v1#S8.Thmtheorem2 "Proposition 8.2 (No-Wait Condition). ‣ The Waiting Game. ‣ 8.6 Follower Robustness ‣ 8 Multiple–Round ADL as a Stackelberg Control Problem ‣ Autodeleveraging: Impossibilities and Optimization")

###### Proof.

Let U​(τ,q)=βτ−t​q​(θτ−κτ)U(\tau,q)=\beta^{\tau-t}q(\theta\_{\tau}-\kappa\_{\tau}) be the discounted utility of a BLP who provides liquidity qq at time τ≥t\tau\geq t.
Here, θτ\theta\_{\tau} represents the payment per unit of liquidity (derived from the ADL severity) and κτ\kappa\_{\tau} represents the cost per unit (liquidity premium).
The BLP solves the optimal stopping problem (see, e.g. [Peskir2006]):

|  |  |  |
| --- | --- | --- |
|  | maxτ≥t,q∈[0,Dt]​𝐄t[U​(τ,q)].\max\_{\tau\geq t,q\in[0,D\_{t}]}\mathop{\bf E{}}\_{t}\left[U(\tau,q)\right]. |  |

This objective captures the trade-off between acting immediately to capture the current spread versus waiting for potentially higher future premiums, discounted by the time cost of delay.
Assuming the BLP is risk-neutral and has capacity q=Dtq=D\_{t}, the condition for immediate stopping at τ=t\tau=t is that the immediate payoff exceeds the expected discounted future value:

|  |  |  |
| --- | --- | --- |
|  | Dt​(θt−κt)≥β​𝐄t[Vt+1​(Dt+1)],D\_{t}(\theta\_{t}-\kappa\_{t})\;\geq\;\beta\mathop{\bf E{}}\_{t}[V\_{t+1}(D\_{t+1})], |  |

where Vt+1​(Dt+1)=maxτ≥t+1,q∈[0,Dt+1]​𝐄t+1[U​(τ,q)]V\_{t+1}(D\_{t+1})=\max\_{\tau\geq t+1,q\in[0,D\_{t+1}]}\mathop{\bf E{}}\_{t+1}[U(\tau,q)] is the value function from t+1t+1 onwards.
Substituting the per-unit surplus δt=θt−κt\delta\_{t}=\theta\_{t}-\kappa\_{t} and rearranging gives the condition:

|  |  |  |
| --- | --- | --- |
|  | θt​Dt≥Γt+β​𝐄t[Vt+1​(Dt+1)].\theta\_{t}D\_{t}\;\geq\;\Gamma\_{t}+\beta\mathop{\bf E{}}\_{t}[V\_{t+1}(D\_{t+1})]. |  |

In the simplified case where the BLP compares acting now vs. acting at t+Δ​tt+\Delta t, and assuming capacity constraints are non-binding, the condition reduces to comparing marginal costs.
Specifically, if the cost of waiting is strictly positive (due to discounting β<1\beta<1 or decreasing surplus δt+Δ​t<δt\delta\_{t+\Delta t}<\delta\_{t}), then the optimal strategy is to act immediately.
If, however, θt\theta\_{t} decays rapidly such that θt​Dt>𝐄[θt+Δ​t​Dt+Δ​t]\theta\_{t}D\_{t}>\mathop{\bf E{}}[\theta\_{t+\Delta t}D\_{t+\Delta t}], but the premium Γt\Gamma\_{t} makes immediate action costly, the inequality flips.
Rearranging the condition in the proposition statement:

|  |  |  |
| --- | --- | --- |
|  | θt​Dt+Γt≤𝐄t[θt+Δ​t​Dt+Δ​t]\theta\_{t}D\_{t}+\Gamma\_{t}\leq\mathop{\bf E{}}\_{t}[\theta\_{t+\Delta t}D\_{t+\Delta t}] |  |

implies that the future expected payout (even after discounting) is higher than the current payout net of costs, incentivizing delay.
Thus, to enforce no-wait, the exchange must ensure the reverse inequality holds.
∎

## Appendix G Price of Anarchy Phase Transitions

We characterize the efficiency gap between static (Nash) and dynamic (Stackelberg) ADL policies via Price of Anarchy (PoA) phase transitions.
We analyze two distinct welfare objectives: *Fairness* (minimizing haircuts to winners) and *Revenue* (maximizing exchange value).
In both cases, we find a sharp transition from a bounded regime, where static policies are constant-factor optimal, to an unbounded regime, where dynamic control is strictly necessary.
Throughout, we work with the terminal book 𝒫n\mathcal{P}\_{n} of size nn as n→∞n\to\infty.

### G.1 Fairness Phase Transition

We first analyze fairness using the Profitability-to-Total-Solvency Ratio (PTSR), which measures the survival rate of winner equity relative to the total deficit covered.

#### G.1.1 Welfare and Assumptions

##### Fairness Welfare.

We define the fairness welfare of a policy π\pi as its expected PTSR:

|  |  |  |
| --- | --- | --- |
|  | WFair​(π):=𝐄[ωTπDTπ].W\_{\mathrm{Fair}}(\pi)\;:=\;\mathop{\bf E{}}\left[\frac{\omega\_{T}^{\pi}}{D\_{T}^{\pi}}\right]. |  |

This metric captures the efficiency of haircuts: higher values imply that the policy covers deficits DTπD\_{T}^{\pi} while preserving maximal winner equity ωTπ\omega\_{T}^{\pi}.
Extreme-value scaling implies WFairW\_{\mathrm{Fair}} scales inversely with the severity load.

##### Price of Anarchy.

We compare the welfare of a static policy πstat\pi^{\mathrm{stat}} (simultaneous move) against the optimal dynamic Stackelberg policy π⋆\pi^{\star}. The Price of Anarchy is defined as the ratio:

|  |  |  |
| --- | --- | --- |
|  | PoAFair:=WFair​(π⋆)WFair​(πstat).\mathrm{PoA}\_{\mathrm{Fair}}\;:=\;\frac{W\_{\mathrm{Fair}}(\pi^{\star})}{W\_{\mathrm{Fair}}(\pi^{\mathrm{stat}})}. |  |

We require the following regularity assumptions.
*LLN and EV Scaling (Prop. [G.1](https://arxiv.org/html/2512.01112v1#A7.Thmtheorem1 "Proposition G.1 (LLN and EV scaling). ‣ Price of Anarchy. ‣ G.1.1 Welfare and Assumptions ‣ G.1 Fairness Phase Transition ‣ Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization"))* establish the baseline scales for deficits (O​(n)O(n)) and equity (O​(bn)O(b\_{n})).
*Anti-concentration (Prop. [G.2](https://arxiv.org/html/2512.01112v1#A7.Thmtheorem2 "Proposition G.2 (Anti-concentration). ‣ Price of Anarchy. ‣ G.1.1 Welfare and Assumptions ‣ G.1 Fairness Phase Transition ‣ Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization"))* ensures that bn≪nb\_{n}\ll n, creating the scarcity of winner equity that drives the phase transition.

###### Proposition G.1 (LLN and EV scaling).

The number of winners knk\_{n} and losers mnm\_{n} satisfy kn,mn≍nk\_{n},m\_{n}\asymp n.
Winner equity and loser deficits satisfy extreme-value limits with scales bn:=bkn+b\_{n}:=b^{+}\_{k\_{n}} and bmn−b^{-}\_{m\_{n}}.

###### Proposition G.2 (Anti-concentration).

(i) *Equity:* The top winner is not dominant: bn=o​(n)b\_{n}=o(n).
(ii) *Leverage:* Max leverage scales with average leverage: maxi⁡λi,T±≤C​ℓn±/n\max\_{i}\lambda\_{i,T}^{\pm}\leq C\ell^{\pm}\_{n}/n.
(iii) *Balance:* Winner and loser leverage masses are comparable: ℓn+≍ℓn−\ell^{+}\_{n}\asymp\ell^{-}\_{n}.

#### G.1.2 Phase Transition

The efficiency of static ADL depends on the *load* κn=θn​n/bn\kappa\_{n}=\theta\_{n}n/b\_{n}, which measures the severity intensity relative to the tail of the winner distribution.

###### Theorem G.3 (Fairness PoA Phase Transition).

Suppose Assumptions [G.1](https://arxiv.org/html/2512.01112v1#A7.Thmtheorem1 "Proposition G.1 (LLN and EV scaling). ‣ Price of Anarchy. ‣ G.1.1 Welfare and Assumptions ‣ G.1 Fairness Phase Transition ‣ Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization")–[G.2](https://arxiv.org/html/2512.01112v1#A7.Thmtheorem2 "Proposition G.2 (Anti-concentration). ‣ Price of Anarchy. ‣ G.1.1 Welfare and Assumptions ‣ G.1 Fairness Phase Transition ‣ Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization") hold.
Let π⋆\pi^{\star} be the optimal dynamic policy and πstat\pi^{\mathrm{stat}} be any static policy with load κnstat\kappa\_{n}^{\mathrm{stat}}.

1. 1.

   *Bounded Regime (Low Load):*
   If supnκnstat<∞\sup\_{n}\kappa\_{n}^{\mathrm{stat}}<\infty, then static ADL is constant-factor optimal:

   |  |  |  |
   | --- | --- | --- |
   |  | lim supn→∞PoAFair≤C<∞.\limsup\_{n\to\infty}\mathrm{PoA}\_{\mathrm{Fair}}\;\leq\;C<\infty. |  |
2. 2.

   *Unbounded Regime (High Load):*
   If κnstat→∞\kappa\_{n}^{\mathrm{stat}}\to\infty (e.g., due to heavy tails or fixed severity with bn=o​(n)b\_{n}=o(n)), then the Price of Anarchy diverges:

   |  |  |  |
   | --- | --- | --- |
   |  | PoAFair≍κnstat→∞.\mathrm{PoA}\_{\mathrm{Fair}}\;\asymp\;\kappa\_{n}^{\mathrm{stat}}\;\to\;\infty. |  |

###### Proof.

We prove the result by establishing the scaling limits of the dynamic benchmark, the static cost, and their asymptotic ratio.

First, for the dynamic benchmark, the optimal Stackelberg policy π⋆\pi^{\star} minimizes haircuts ex-post to cover the realized deficit DT≍nD\_{T}\asymp n.
By targeting the haircut to preserve the top winner’s equity ωT≍bn\omega\_{T}\asymp b\_{n}, the dynamic policy achieves a Profitability-to-Total-Solvency Ratio (PTSR) that concentrates around a constant, WFair​(π⋆)≍1W\_{\mathrm{Fair}}(\pi^{\star})\asymp 1 (Theorem [B.3](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem3 "Theorem B.3 (PTSR scaling). ‣ B.4 Asymptotic Scaling Results ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization")).
This is possible because the controller can observe the realization of heavy-tailed variates and adjust the severity θ\theta precisely to the minimal necessary level.

Second, for the static policy, the severity θn\theta\_{n} is fixed ex-ante and applies a uniform pressure θn​n\theta\_{n}n on the book, which must be absorbed by individual winners with capacity scaling as bnb\_{n}.
Under heavy-tailed scaling, Proposition [5.1](https://arxiv.org/html/2512.01112v1#S5.Thmtheorem1 "Proposition 5.1 (Informal). ‣ Main Result. ‣ 5.1 Impossibility of Avoiding Moral Hazard as 𝑛→∞ ‣ 5 Negative Results ‣ Autodeleveraging: Impossibilities and Optimization") shows that this mismatch leads to a welfare decay WFair​(π)≍bn/(θn​n)=1/κnW\_{\mathrm{Fair}}(\pi)\asymp b\_{n}/(\theta\_{n}n)=1/\kappa\_{n}, as the policy blindly destroys small winners or fails to extract sufficient capital from the tail without excessive rates.
Crucially, as n→∞n\to\infty, the gap between the aggregate load O​(n)O(n) and individual capacity O​(bn)O(b\_{n}) widens (since bn=o​(n)b\_{n}=o(n)), forcing κn\kappa\_{n} to grow if θn\theta\_{n} does not vanish rapidly enough.

Finally, combining these estimates yields the Price of Anarchy PoAFair≍1/(1/κnstat)=κnstat\mathrm{PoA}\_{\mathrm{Fair}}\asymp 1/(1/\kappa\_{n}^{\mathrm{stat}})=\kappa\_{n}^{\mathrm{stat}}.
In the bounded regime (κnstat=O​(1)\kappa\_{n}^{\mathrm{stat}}=O(1)), the ratio is constant, but in the unbounded regime (κnstat→∞\kappa\_{n}^{\mathrm{stat}}\to\infty), the efficiency of the static policy collapses relative to the dynamic optimum, proving the divergence.
∎

###### Example G.4 (Light-tailed Failure).

If winner equities are sub-Gaussian (bn≍log⁡nb\_{n}\asymp\sqrt{\log n}) but the exchange uses fixed severity θ>0\theta>0, then κnstat≍n/log⁡n→∞\kappa\_{n}^{\mathrm{stat}}\asymp n/\sqrt{\log n}\to\infty.
Static ADL unnecessarily destroys winner equity compared to a dynamic policy that scales θ∼1/n\theta\sim 1/n, leading to infinite PoA.

### G.2 Revenue Phase Transition

We now extend the analysis to the *Revenue* objective, formalizing the trade-off between solvency and capital efficiency (LTV).

#### G.2.1 Joint Welfare

##### Solvency-Revenue Welfare.

We define the joint welfare WRev​(π)W\_{\mathrm{Rev}}(\pi) as the risk-adjusted LTV, penalizing insolvency RTR\_{T} with weight λ>1\lambda>1:

|  |  |  |
| --- | --- | --- |
|  | WRev​(π):=𝐄[LTVT​(π)−λ⋅RT​(π)].W\_{\mathrm{Rev}}(\pi)\;:=\;\mathop{\bf E{}}\left[\mathrm{LTV}\_{T}(\pi)-\lambda\cdot R\_{T}(\pi)\right]. |  |

The tension arises from provisioning: Dynamic policies provision for the *average* deficit, while static policies must provision for the *tail* to ensure solvency.

#### G.2.2 Phase Transition

###### Proposition G.5 (Revenue PoA Phase Transition).

Suppose deficits have heavy tails with index α∈(1,2)\alpha\in(1,2) (infinite variance) and the exchange operates in the structural deficit regime (μ−>μΦ\mu\_{-}>\mu\_{\Phi}).
Let WRev⋆=supπWRev​(π)W\_{\mathrm{Rev}}^{\star}=\sup\_{\pi}W\_{\mathrm{Rev}}(\pi).

1. 1.

   *Bounded Regime (Light Tails):*
   If deficits are light-tailed, static policies that provision for the mean are efficient:

   |  |  |  |
   | --- | --- | --- |
   |  | PoARev:=WRev⋆WRev​(πstat)≤C<∞.\mathrm{PoA}\_{\mathrm{Rev}}\;:=\;\frac{W\_{\mathrm{Rev}}^{\star}}{W\_{\mathrm{Rev}}(\pi^{\mathrm{stat}})}\;\leq\;C<\infty. |  |
2. 2.

   *Unbounded Regime (Heavy Tails):*
   If deficits are heavy-tailed (α<2\alpha<2), any static policy πstat\pi^{\mathrm{stat}} satisfying solvency condition (S) diverges:

   |  |  |  |
   | --- | --- | --- |
   |  | PoARev→∞.\mathrm{PoA}\_{\mathrm{Rev}}\;\to\;\infty. |  |

###### Proof.

We establish the result by comparing the linear scaling of dynamic welfare with the sub-linear or negative welfare of static policies under heavy tails.

First, the optimal dynamic policy π⋆\pi^{\star} operates as a regulator that clears the market based on realized deficits, diverting fees ΦT\Phi\_{T} only as strictly needed to cover DTD\_{T}.
By the Law of Large Numbers, both ΦT\Phi\_{T} and DTD\_{T} scale linearly with nn, yielding an expected welfare WRev⋆≍n​(μΦ−μ−)W\_{\mathrm{Rev}}^{\star}\asymp n(\mu\_{\Phi}-\mu\_{-}) that is positive and proportional to market size.

Second, a static policy is parameterized by a fixed fee diversion rate δ∈[0,1]\delta\in[0,1] chosen ex-ante, meaning it diverts a constant fraction of fees 𝒟t=δ​ϕt\mathcal{D}\_{t}=\delta\phi\_{t} (where ΦT=∑ϕt\Phi\_{T}=\sum\phi\_{t} follows the scaling in Assumption [I.2](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem2 "Assumption I.2 (LLN and EVT Scaling). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization")) to the insurance fund.
To build a fund KtK\_{t} capable of absorbing heavy-tailed shocks with infinite variance (α<2\alpha<2),
Standard ruin theory [AsmussenAlbrecher2010, Embrechts1997] implies that to ensure Solvency Condition (S) (Definition [I.4](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem4 "Definition I.4 (Solvency). ‣ Formal Desiderata. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization")) against the maximum jump ΔT∼n1/α\Delta\_{T}\sim n^{1/\alpha}, the policy must essentially set δ→1\delta\to 1 to handle the timing mismatch where large shocks occur before the fund accumulates.
Any policy that attempts to maintain δ<1\delta<1 will fail solvency with probability approaching 1, while a policy with δ≈1\delta\approx 1 consumes the entire revenue stream, driving WRev​(πstat)→0W\_{\mathrm{Rev}}(\pi^{\mathrm{stat}})\to 0 or into negative territory due to insolvency penalties.

Finally, the Price of Anarchy is the ratio of the linear dynamic payoff to the vanishing static payoff: PoARev≍n/o​(n)→∞\mathrm{PoA}\_{\mathrm{Rev}}\asymp n/o(n)\to\infty.
This divergence confirms that in the heavy-tailed regime, the information advantage of the dynamic controller (i.e., knowing exactly when to divert funds) is infinitely valuable compared to a static rule.
∎

### G.3 The Aggregation Paradox

We conclude by observing that the divergence of PoA depends on how objectives are aggregated.

###### Proposition G.6 (Sum vs. Min Aggregation).

Let WΣ=WFair+WRevW\_{\Sigma}=W\_{\mathrm{Fair}}+W\_{\mathrm{Rev}} and Wmin=min⁡(WFair,WRev)W\_{\min}=\min(W\_{\mathrm{Fair}},W\_{\mathrm{Rev}}) be normalized combined objectives.

1. 1.

   *Sum-Welfare is Bounded:* PoAΣ≤2\mathrm{PoA}\_{\Sigma}\leq 2. A static policy can always choose to satisfy one objective fully, achieving at least half the optimal total score.
2. 2.

   *Min-Welfare is Unbounded:* PoAmin→∞\mathrm{PoA}\_{\min}\to\infty. In the heavy-tailed regime, static policies face the ADL Trilemma and must drive at least one objective to zero, while dynamic policies maintain both.

This implies that static ADL is sufficient if objectives are substitutes, but catastrophically inefficient if they are complements (i.e., if the exchange requires *both* fairness and revenue to survive).

## Appendix H Empirical Methodology

We backtest the mechanisms of §[9](https://arxiv.org/html/2512.01112v1#S9 "9 Empirical Analysis: The October 10 Event ‣ Autodeleveraging: Impossibilities and Optimization") on Hyperliquid’s October 10, 2025 autodeleveraging episode.
Price shocks are represented by timestamps where the chain records an ADL tranche and are indexed by discrete times t=1,…,Tt=1,\dots,T and grouped by coin cc.
Each shock carries a realized deficit Dt≥0D\_{t}\geq 0, the total negative equity of the losers in that liquidation cluster, and an account-level winner capacity vector wt=(wt,1,…,wt,Wt)∈R+Wtw\_{t}=(w\_{t,1},\dots,w\_{t,W\_{t}})\in{\mbox{\bf R}}\_{+}^{W\_{t}} measured in USD of available positive PNL.
Summing DtD\_{t} across shocks therefore reports the aggregate shortfall that must be socialized during the event.

Controllers either select a scalar severity θt≥0\theta\_{t}\geq 0 or a haircut vector ht∈[0,1]𝒲th\_{t}\in[0,1]^{\mathcal{W}\_{t}}, generating a per-round budget Bt=θt​DtB\_{t}=\theta\_{t}D\_{t} or Bt=wt⊤​htB\_{t}=w\_{t}^{\top}h\_{t}, respectively.
Budgets are always truncated to the realized winner capacity ∑iwt,i\sum\_{i}w\_{t,i}.
The release contains T=1108T=1108 shocks across 161 coins.
Across the positive-deficit shocks this reconstruction captures 304.5304.5M USD of loser shortfall, while the corresponding winner capacity only supports 95.895.8M USD of feasible haircuts, leaving at least 208.6208.6M USD structurally uncovered irrespective of policy.

### H.1 Data construction

##### Event sample.

The data (provided by Hydromancer and SonarX) captured Hyperliquid’s core exchange logs covering 21:15–21:30 UTC and retain every coin with at least one liquidation cluster.
There are 998 positive-deficit shocks and 110 shocks with zero deficit (for which policies trivially abstain).

##### Clustering.

Within each coin, fills are sorted by timestamp and grouped into shocks via a fixed inter-arrival rule: a new cluster begins whenever the gap since the previous fill exceeds Δ=5\Delta=5s.
If tkt\_{k} denotes the time of fill kk, the cluster index obeys κ1=0\kappa\_{1}=0 and κk=κk−1+𝟏​{tk−tk−1>Δ}\kappa\_{k}=\kappa\_{k-1}+\mathbf{1}\{t\_{k}-t\_{k-1}>\Delta\}.
All statistics below are computed at the cluster level.

##### Account aggregates and capacities.

We aggregate filled trades (‘fills’) by account within a cluster.
Positive realized PNL marks winners and contributes to capacity, whereas negative PNL marks losers and contributes to the deficit Dt=∑i∈ℒt(−PNLt,i)D\_{t}=\sum\_{i\in\mathcal{L}\_{t}}(-\mathrm{PNL}\_{t,i}).
Capacities are inferred in the order notional →\rightarrow |start\_position×price||\texttt{start\\_position}\times\texttt{price}| →\rightarrow |closed\_pnl||\texttt{closed\\_pnl}|, providing a conservative haircut limit when full notional quotes are unavailable.
Queue priority scores replicate the production ranking by summing realized PNL per account within the cluster.

##### Production queue replay.

We reconstruct the realized queue budgets BtQB\_{t}^{\mathrm{Q}} and haircuts by replaying the published priority order and shaving capacity greedily until the recorded budget is exhausted.
This reproduces the overshoot and participation statistics observed on chain and serves as our baseline.

### H.2 Losses and objectives

##### Scalar severity surrogate.

Controllers that only choose θt\theta\_{t} minimize the convex surrogate

|  |  |  |
| --- | --- | --- |
|  | ft​(θ)=−λ​θ​Dt+μ​(Mt−θ​Dt)++ν​(θ​Dt−Dt)+2,f\_{t}(\theta)=-\lambda\,\theta D\_{t}+\mu\,(M\_{t}-\theta D\_{t})\_{+}+\nu\,(\theta D\_{t}-D\_{t})\_{+}^{2}, |  |

where Mt=maxi⁡wt,iM\_{t}=\max\_{i}w\_{t,i} is the largest winner, and λ,μ,ν≥0\lambda,\mu,\nu\geq 0 trade off solvency, shortfall, and overshoot.
The subgradient satisfies

|  |  |  |
| --- | --- | --- |
|  | ∂ft​(θ)=−λ​Dt−μ​Dt​ 1​{Mt>θ​Dt}+2​ν​(θ​Dt−Dt)+​Dt.\partial f\_{t}(\theta)=-\lambda D\_{t}-\mu D\_{t}\,\mathbb{1}\{M\_{t}>\theta D\_{t}\}+2\nu(\theta D\_{t}-D\_{t})\_{+}\,D\_{t}. |  |

We tune (λ,μ,ν)(\lambda,\mu,\nu) and the initialization/step-size grid (θinit,η0)(\theta\_{\text{init}},\eta\_{0}) by coarse search and fix the best setting for all severity controllers.

##### Vector objective.

When actions are full haircut vectors, we minimize

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒt​(h)=\displaystyle\mathcal{L}\_{t}(h)={} | −λvec​∑i=1Wtwt,i​(1−e−β​hi)+μspr​‖h‖22+ϕ​‖h−θ¯t​𝟏‖22\displaystyle-\lambda\_{\mathrm{vec}}\sum\_{i=1}^{W\_{t}}w\_{t,i}(1-e^{-\beta h\_{i}})+\mu\_{\mathrm{spr}}\|h\|\_{2}^{2}+\phi\,\|h-\bar{\theta}\_{t}\mathbf{1}\|\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +νvec​(wt⊤​h−Dt)+2+γvec​(Dt−wt⊤​h)+2+ρvec​(Dt−wt⊤​h)+,\displaystyle+\nu\_{\mathrm{vec}}\,(w\_{t}^{\top}h-D\_{t})\_{+}^{2}+\gamma\_{\mathrm{vec}}\,(D\_{t}-w\_{t}^{\top}h)\_{+}^{2}+\rho\_{\mathrm{vec}}\,(D\_{t}-w\_{t}^{\top}h)\_{+}, |  |

with θ¯t=min⁡{Dt,∑iwt,i}/Dt\bar{\theta}\_{t}=\min\{D\_{t},\sum\_{i}w\_{t,i}\}/D\_{t} when Dt>0D\_{t}>0.
The weights (λvec,β,μspr,ϕ,νvec,γvec,ρvec)(\lambda\_{\mathrm{vec}},\beta,\mu\_{\mathrm{spr}},\phi,\nu\_{\mathrm{vec}},\gamma\_{\mathrm{vec}},\rho\_{\mathrm{vec}}) are fixed to the calibrated values shipped with the release.
We enforce the budget equality constraint wt⊤​h=Bt⋆w\_{t}^{\top}h=B\_{t}^{\star} with Bt⋆=min⁡{Dt,∑iwt,i}B\_{t}^{\star}=\min\{D\_{t},\sum\_{i}w\_{t,i}\} via the projection described below.

##### Revenue loss proxy.

To translate haircut allocations into an expected loss of future fees we use a funding-rate-based proxy.
For each winner ii in shock tt we observe the realized haircut ratio ft,i=ht,i/wt,if\_{t,i}=h\_{t,i}/w\_{t,i} and treat it as a churn shock with probability pt,i=1−exp⁡(−β​ft,i)p\_{t,i}=1-\exp(-\beta f\_{t,i}), where β=5\beta=5 controls sensitivity.
The remaining positive PNL wt,iw\_{t,i} serves as a conservative proxy for the trader’s deployable notional.
We combine this with an estimate of per-dollar daily revenue,

|  |  |  |
| --- | --- | --- |
|  | rtdaily=24​|ftfund|+τturn⋅feetaker,r^{\text{daily}}\_{t}=24\,|f^{\text{fund}}\_{t}|+\tau\_{\text{turn}}\cdot\text{fee}\_{\text{taker}}, |  |

where |ftfund||f^{\text{fund}}\_{t}| is the absolute funding rate observed for the coin (defaulting to 1.5×10−51.5\times 10^{-5} when data are sparse), τturn=1\tau\_{\text{turn}}=1 assumes one notional turnover per day, and feetaker=4\text{fee}\_{\text{taker}}=4 bps.
Multiplying rtdailyr^{\text{daily}}\_{t} by a two-year horizon H=730H=730 days yields the per-dollar lifetime value estimate.
The per-shock revenue loss is then

|  |  |  |
| --- | --- | --- |
|  | RevLosst=H​rtdaily​∑iwt,i​pt,i,\text{RevLoss}\_{t}=H\,r^{\text{daily}}\_{t}\sum\_{i}w\_{t,i}\,p\_{t,i}, |  |

which we aggregate across shocks for each controller.

The exponential hazard ensures that zero haircuts map to zero churn, while large cuts asymptotically drive pt,i→1p\_{t,i}\rightarrow 1, mirroring the threshold-like exits we observe in the account-level replay data.
We set β=5\beta=5 so that a 10% haircut implies ≈39%\approx 39\% churn and a 20% haircut implies ≈63%\approx 63\% churn, matching the attrition rate measured by comparing pre/post-shock winner mass in the Hyperliquid October 10 dataset [HyperMultiAssetedADL].
Funding rates ftfundf^{\text{fund}}\_{t} come directly from the “misc events” stream bundled with the same dataset: we aggregate the absolute funding paid per coin over the preceding hour and divide by the coin’s outstanding notional to obtain an hourly rate.
When the logs lack funding entries for a coin during the 12-minute window we substitute the cross-sectional median absolute rate of 1.5×10−51.5\times 10^{-5} (the BTC/ETH average).
This proxy ignores second-order follower dynamics (e.g., strategic re-entry) but provides a consistent way to compare policies on a common revenue scale using only observable quantities.

### H.3 Policies

##### Queue (production).

The production policy orders winners by the realized priority score qt,iq\_{t,i} and applies the greedy queue allocator with the recorded budget BtQB\_{t}^{\mathrm{Q}}.
Haircuts therefore match the on-chain execution and may overshoot DtD\_{t}.

##### Smart queue.

We retain the same ordering but cap the budget at the feasible mass: BtSQ=min⁡{Dt,∑iwt,i}B\_{t}^{\mathrm{SQ}}=\min\{D\_{t},\sum\_{i}w\_{t,i}\}.
The greedy queue allocator is applied under this cap, eliminating overshoot while keeping the queue’s concentration.

##### Exponential backoff.

We impose the per-round PoA cap Θt=R1+R​MtDt\Theta\_{t}=\frac{R}{1+R}\,\frac{M\_{t}}{D\_{t}} (uncapped if R=∞R=\infty) and update

|  |  |  |
| --- | --- | --- |
|  | θt=min⁡{θtcand,Θt},θtcand={θ0,t=1,max⁡{α​θt−1,θ0},t≥2,\theta\_{t}=\min\{\theta^{\mathrm{cand}}\_{t},\Theta\_{t}\},\qquad\theta^{\mathrm{cand}}\_{t}=\begin{cases}\theta\_{0},&t=1,\\ \max\{\alpha\theta\_{t-1},\theta\_{0}\},&t\geq 2,\end{cases} |  |

with α∈(0,1)\alpha\in(0,1).
The resulting budget Bt=min⁡{θt​Dt,∑iwt,i}B\_{t}=\min\{\theta\_{t}D\_{t},\sum\_{i}w\_{t,i}\} is distributed pro-rata across capacities.

##### Mirror descent.

We initialize at θ1=θinit\theta\_{1}=\theta\_{\mathrm{init}}, compute gt∈∂ft​(θt)g\_{t}\in\partial f\_{t}(\theta\_{t}), take θ~t+1=θt−ηt​gt\tilde{\theta}\_{t+1}=\theta\_{t}-\eta\_{t}g\_{t} with ηt=η0/t\eta\_{t}=\eta\_{0}/\sqrt{t}, perform a short backtracking line-search, and project onto [0,Θt][0,\Theta\_{t}].
Budgets and allocations mirror the backoff policy and differ only through the learning dynamics.

##### Dynamic2 warm start.

Dynamic2 matches mirror descent but sets θ1\theta\_{1} to the levered pro-rata fixed point θLPR\theta\_{\mathrm{LPR}} computed from the first shock before continuing with the same updates.

##### Vector mirror descent.

We initialize ht≡0h\_{t}\equiv 0 and iterate for s=1,…,Ss=1,\dots,S

|  |  |  |
| --- | --- | --- |
|  | h~←h−ηs​∇ℒt​(h),h←Π𝒞t​(h~),\tilde{h}\leftarrow h-\eta\_{s}\nabla\mathcal{L}\_{t}(h),\qquad h\leftarrow\Pi\_{\mathcal{C}\_{t}}(\tilde{h}), |  |

where 𝒞t={h∈[0,1]Wt:wt⊤​h=Bt⋆}\mathcal{C}\_{t}=\{h\in[0,1]^{W\_{t}}:w\_{t}^{\top}h=B\_{t}^{\star}\}.
The projection solves

|  |  |  |
| --- | --- | --- |
|  | minh∈[0,1]Wt⁡12​‖h−h~‖22​s.t.​wt⊤​h=Bt⋆,\min\_{h\in[0,1]^{W\_{t}}}\tfrac{1}{2}\|h-\tilde{h}\|\_{2}^{2}\ \text{s.t.}\ w\_{t}^{\top}h=B\_{t}^{\star}, |  |

and admits the closed form hi​(τ)=[h~i−τ​wt,i]01h\_{i}(\tau)=\big[\tilde{h}\_{i}-\tau w\_{t,i}\big]\_{0}^{1} with τ\tau found by bisection so that ∑iwt,i​hi​(τ)=Bt⋆\sum\_{i}w\_{t,i}h\_{i}(\tau)=B\_{t}^{\star}.

### H.4 Backtest summary

##### Coverage.

Aggregate deficits over the event sum to $304.5304.5M USD.
Because winner capacity within most clusters is thin, the feasible budget Bt⋆B\_{t}^{\star} totals only 95.895.8M USD, leaving a structural residual of 208.6208.6M USD that no policy can eliminate.

##### Production queue.

The replayed Hyperliquid queue expends $704.6704.6M USD of budgets while overshooting deficits by $630.5630.5M USD and still leaves $230.3230.3M USD of residual loss.
Average winner participation is 31.7%31.7\%, but the queue routinely concentrates haircuts: the mean budget-to-deficit ratio is 9.4×1039.4\times 10^{3} and the largest single haircut reaches $47.247.2M USD.
This misallocation also destroys $602.8602.8M USD of positive PNL.

##### Queue variants.

Capping the queue’s budget at feasibility removes the $630.5630.5M USD overshoot and improves average participation to 60.9%60.9\%, yet it still leaves $222.1222.1M USD of residual losses and $113.8113.8M USD of revenue destruction.

##### Adaptive severity controllers.

The exponential backoff, mirror-descent, and Dynamic2 controllers each use between $8787M and $146146M USD of budgets, moving residual losses into the $217217M USD range while avoiding overshoot (mirror) or limiting it (Dynamic2 and backoff).
Relative to production, these policies reduce winner haircuts by $365365–$461461M USD and modestly raise participation to 3535–38%38\% despite operating with the same per-round PoA cap.

##### Vector mirror descent.

Optimizing the full haircut vector supplies $87.587.5M USD of budgets, drives overshoot below 10−410^{-4} USD, and achieves the lowest residual ($217.0217.0M USD) and second-lowest revenue loss ($136.9136.9M USD).
Winner participation averages 45.2%45.2\%, reflecting the model’s explicit spreading and budget-equality constraint.

## Appendix I Formal Proof of the ADL Trilemma

In this appendix, we provide a complete formal statement and proof of the ADL Trilemma (Proposition [2.1](https://arxiv.org/html/2512.01112v1#S2.Thmtheorem1 "Proposition 2.1 (Trilemma, Informal). ‣ Three competing desiderata. ‣ 2.5 ADL Trilemma ‣ 2 Background ‣ Autodeleveraging: Impossibilities and Optimization")).
The proof assembles results from Appendices [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization")–[G](https://arxiv.org/html/2512.01112v1#A7 "Appendix G Price of Anarchy Phase Transitions ‣ Autodeleveraging: Impossibilities and Optimization"), demonstrating that the three-way tension between solvency, fairness, and revenue is a fundamental structural constraint under heavy-tailed shortfalls.

##### Formal Setup and Definitions.

We work in the large-market limit n→∞n\to\infty under the standard assumptions established in §[3](https://arxiv.org/html/2512.01112v1#S3 "3 Risk and Fairness Preliminaries ‣ Autodeleveraging: Impossibilities and Optimization") and Appendix [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization").

##### Book and Policy Sequences.

Consider a sequence of perpetuals exchanges (𝒫n)n≥1(\mathcal{P}\_{n})\_{n\geq 1} with nn positions at terminal time TT.
Let 𝒲T\mathcal{W}\_{T} and ℒT\mathcal{L}\_{T} denote the winner and loser index sets with cardinalities kn=|𝒲T|k\_{n}=|\mathcal{W}\_{T}| and mn=|ℒT|m\_{n}=|\mathcal{L}\_{T}|.
We assume throughout that kn,mn=Θ​(n)k\_{n},m\_{n}=\Theta(n).
We further assume the initial insurance fund capital K0K\_{0} satisfies K0=o​(n)K\_{0}=o(n), ensuring that solvency depends on flow mechanics rather than initial endowment.
A static ADL policy πn\pi\_{n} is characterized by:

* •

  A severity parameter θn∈[0,1]\theta\_{n}\in[0,1] determining the fraction of deficit socialized;
* •

  An allocation rule hn:R+kn→[0,1]knh\_{n}:{\mbox{\bf R}}^{k\_{n}}\_{+}\to[0,1]^{k\_{n}} distributing haircuts across winners;
* •

  Insurance parameters determining the diversion of fees into the insurance fund.

##### Distributional Assumptions.

We impose the following standard assumptions from Appendix [B](https://arxiv.org/html/2512.01112v1#A2 "Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization"):

###### Assumption I.1 (Regular Variation).

The right tails of the winner equity distribution F¯+​(x)\bar{F}\_{+}(x) and loser shortfall distribution F¯−​(x)\bar{F}\_{-}(x) are regularly varying with indices α+>0\alpha\_{+}>0 and α−>0\alpha\_{-}>0, respectively:

|  |  |  |
| --- | --- | --- |
|  | F¯±​(x)=L±​(x)​x−α±,\bar{F}\_{\pm}(x)=L\_{\pm}(x)x^{-\alpha\_{\pm}}, |  |

where L±L\_{\pm} are slowly varying functions.

###### Assumption I.2 (LLN and EVT Scaling).

The following scaling limits hold:

1. 1.

   *Aggregates:* WT/n→𝑝μ+W\_{T}/n\xrightarrow{p}\mu\_{+}, DT/n→𝑝μ−D\_{T}/n\xrightarrow{p}\mu\_{-}, and total fees ΦT/n→𝑝μΦ\Phi\_{T}/n\xrightarrow{p}\mu\_{\Phi} for constants μ±,μΦ∈(0,∞)\mu\_{\pm},\mu\_{\Phi}\in(0,\infty).
2. 2.

   *Extremes:* The maximum winner equity ωT\omega\_{T} and maximum loser shortfall ΔT\Delta\_{T} satisfy

   |  |  |  |
   | --- | --- | --- |
   |  | ωTbkn+→𝑝c+,ΔTbmn−→𝑝c−,\frac{\omega\_{T}}{b\_{k\_{n}}^{+}}\xrightarrow{p}c\_{+},\qquad\frac{\Delta\_{T}}{b\_{m\_{n}}^{-}}\xrightarrow{p}c\_{-}, |  |

   where bk±=F±−1​(1−1/k)b\_{k}^{\pm}=F\_{\pm}^{-1}(1-1/k) are the extreme-value scales.

We abbreviate bn:=bkn+b\_{n}:=b\_{k\_{n}}^{+}.

###### Assumption I.3 (Structural Deficit Regime).

We assume the exchange operates in a regime where insurance alone is insufficient to cover tail risks. Specifically, the expected deficit rate exceeds the maximum sustainable fee diversion rate: μ−>μΦ\mu\_{-}>\mu\_{\Phi}.
This ensures that the Solvency constraint cannot be trivially satisfied by insurance without impacting LTV or requiring haircuts.

##### Formal Desiderata.

We now define the three desiderata precisely:

###### Definition I.4 (Solvency).

A policy family (πn)(\pi\_{n}) satisfies the *solvency* condition (S) if:

1. (S1)

   *Bounded cumulative residual:* ∑t=1TRt​(πn)=Op​(1)\sum\_{t=1}^{T}R\_{t}(\pi\_{n})=O\_{p}(1) as n→∞n\to\infty;
2. (S2)

   *Controlled breach probability:* supn,t𝐏𝐫𝐨𝐛[Rt​(πn)>0]<1\sup\_{n,t}\mathop{\bf Prob}\!\left[R\_{t}(\pi\_{n})>0\right]<1.

###### Definition I.5 (Fairness / Bounded Moral Hazard).

A policy family (πn)(\pi\_{n}) satisfies the *fairness* condition (F) if:

1. (F1)

   *PTSR stability:* There exist constants 0<clo≤chi<∞0<c\_{\text{lo}}\leq c\_{\text{hi}}<\infty such that

   |  |  |  |
   | --- | --- | --- |
   |  | clo≤𝖯𝖳𝖲𝖱T​(𝒫n,πn):=𝐄[ωTπnDTπn]≤chi;c\_{\text{lo}}\;\leq\;\mathsf{PTSR}\_{T}(\mathcal{P}\_{n},\pi\_{n}):=\mathop{\bf E{}}\left[\frac{\omega\_{T}^{\pi\_{n}}}{D\_{T}^{\pi\_{n}}}\right]\;\leq\;c\_{\text{hi}}; |  |
2. (F2)

   *PMR stability:* There exist constants 0<clo′≤chi′<∞0<c^{\prime}\_{\text{lo}}\leq c^{\prime}\_{\text{hi}}<\infty such that

   |  |  |  |
   | --- | --- | --- |
   |  | clo′≤𝖯𝖬𝖱T​(𝒫n,πn):=𝐄[ωTπnΔTπn]≤chi′.c^{\prime}\_{\text{lo}}\;\leq\;\mathsf{PMR}\_{T}(\mathcal{P}\_{n},\pi\_{n}):=\mathop{\bf E{}}\left[\frac{\omega\_{T}^{\pi\_{n}}}{\Delta\_{T}^{\pi\_{n}}}\right]\;\leq\;c^{\prime}\_{\text{hi}}. |  |

These bounds ensure the top winner’s residual equity remains proportional to the deficit scale.
For brevity we write 𝖯𝖳𝖲𝖱T​(πn)\mathsf{PTSR}\_{T}(\pi\_{n}) (and 𝖯𝖬𝖱T​(πn)\mathsf{PMR}\_{T}(\pi\_{n})) whenever the dependence on 𝒫n\mathcal{P}\_{n} is clear from context.

###### Definition I.6 (Revenue Preservation).

Let ΦT​(π)\Phi\_{T}(\pi) be the cumulative trading fees generated under policy π\pi, and let 𝒟T​(π)\mathcal{D}\_{T}(\pi) be the cumulative diversion of fees into the insurance fund. The *Exchange Long-Term Value* is defined as the net retained revenue:

|  |  |  |
| --- | --- | --- |
|  | LTVT​(π):=ΦT​(π)−𝒟T​(π).\mathrm{LTV}\_{T}(\pi)\;:=\;\Phi\_{T}(\pi)-\mathcal{D}\_{T}(\pi). |  |

A policy family (πn)(\pi\_{n}) satisfies the *revenue* condition (R) if there exists a constant cR∈(0,1]c\_{R}\in(0,1] such that:

|  |  |  |
| --- | --- | --- |
|  | LTVT​(πn)≥cR⋅supπ′ΦT​(π′).\mathrm{LTV}\_{T}(\pi\_{n})\;\geq\;c\_{R}\cdot\sup\_{\pi^{\prime}}\Phi\_{T}(\pi^{\prime}). |  |

This definition implies that (1) the policy does not cause excessive churn (reducing ΦT\Phi\_{T}) and (2) the policy does not divert substantially all revenue to insurance (increasing 𝒟T\mathcal{D}\_{T} to ≈ΦT\approx\Phi\_{T}).

##### Formal Statement of the Trilemma.

###### Theorem I.7 (ADL Trilemma).

Let (𝒫n)n≥1(\mathcal{P}\_{n})\_{n\geq 1} be a sequence of perpetuals exchanges satisfying Assumptions [I.1](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem1 "Assumption I.1 (Regular Variation). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization")–[I.3](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem3 "Assumption I.3 (Structural Deficit Regime). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization").
For any static ADL policy family (πn)(\pi\_{n}) with severity sequence (θn)(\theta\_{n}), at most two of the three conditions (S), (F), and (R) can hold simultaneously.

More precisely:

1. (I)

   (S) ∧\wedge (F) ⇒\Rightarrow ¬\neg(R):
   If both solvency and fairness hold, then LTV must be sacrificed via full fee diversion, violating (R).
2. (II)

   (S) ∧\wedge (R) ⇒\Rightarrow ¬\neg(F):
   If both solvency and revenue hold, then fairness is sacrificed (𝖯𝖳𝖲𝖱T→0\mathsf{PTSR}\_{T}\to 0).
3. (III)

   (F) ∧\wedge (R) ⇒\Rightarrow ¬\neg(S):
   If both fairness and revenue hold, then solvency is sacrificed (𝐏𝐫𝐨𝐛[Rt>0]→1\mathop{\bf Prob}[R\_{t}>0]\to 1).

### I.1 Proof of the Trilemma

We first establish a fundamental identity linking the three quantities.

###### Lemma I.8 (Solvency-Revenue Identity).

For any policy π\pi, the cumulative deficit DTD\_{T} must be covered by the haircut budget BTB\_{T}, insurance fund diversions 𝒟T\mathcal{D}\_{T}, initial capital K0K\_{0}, and residual insolvency RTR\_{T}:

|  |  |  |
| --- | --- | --- |
|  | DT≤BT+𝒟T+K0+RT.D\_{T}\;\leq\;B\_{T}+\mathcal{D}\_{T}+K\_{0}+R\_{T}. |  |

Substituting the LTV definition 𝒟T=ΦT−LTVT\mathcal{D}\_{T}=\Phi\_{T}-\mathrm{LTV}\_{T} and using K0=o​(n)K\_{0}=o(n), we obtain the asymptotic inequality:

|  |  |  |
| --- | --- | --- |
|  | LTVT​(π)≤ΦT​(π)+BT​(π)+RT​(π)−DT​(π)+o​(n).\mathrm{LTV}\_{T}(\pi)\;\leq\;\Phi\_{T}(\pi)+B\_{T}(\pi)+R\_{T}(\pi)-D\_{T}(\pi)+o(n). |  |

The proof then proceeds by analyzing this identity under different constraint combinations.

##### Proof of Implication (I): (S) ∧\wedge (F) ⇒\Rightarrow ¬\neg(R).

###### Proof.

Suppose both (S) and (F) hold.

1. *Fairness Implication:* By (F), θn=O​(bn/n)\theta\_{n}=O(b\_{n}/n) (Theorem [B.3](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem3 "Theorem B.3 (PTSR scaling). ‣ B.4 Asymptotic Scaling Results ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization")). Since bn=o​(n)b\_{n}=o(n), the haircut budget scales as:

|  |  |  |
| --- | --- | --- |
|  | BT=θn​DT≍bnn⋅n=bn=o​(n).B\_{T}=\theta\_{n}D\_{T}\asymp\frac{b\_{n}}{n}\cdot n=b\_{n}=o(n). |  |

Thus, BT/n→𝑝0B\_{T}/n\xrightarrow{p}0.

2. *Solvency Implication:* By (S), residual risk is negligible, so RT/n→𝑝0R\_{T}/n\xrightarrow{p}0.

3. *Identity Analysis:* Using the Solvency-Revenue Identity (divided by nn):

|  |  |  |
| --- | --- | --- |
|  | LTVTn≤ΦTn+BTn+RTn−DTn+o​(n)n.\frac{\mathrm{LTV}\_{T}}{n}\;\leq\;\frac{\Phi\_{T}}{n}+\frac{B\_{T}}{n}+\frac{R\_{T}}{n}-\frac{D\_{T}}{n}+\frac{o(n)}{n}. |  |

Taking limits n→∞n\to\infty:

|  |  |  |
| --- | --- | --- |
|  | limn→∞LTVTn≤μΦ+0+0−μ−+0.\lim\_{n\rightarrow\infty}\frac{\mathrm{LTV}\_{T}}{n}\;\leq\;\mu\_{\Phi}+0+0-\mu\_{-}+0. |  |

By Assumption [I.3](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem3 "Assumption I.3 (Structural Deficit Regime). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization"), μ−>μΦ\mu\_{-}>\mu\_{\Phi}.
Thus:

|  |  |  |
| --- | --- | --- |
|  | limn→∞LTVTn≤μΦ−μ−< 0.\lim\_{n\rightarrow\infty}\frac{\mathrm{LTV}\_{T}}{n}\;\leq\;\mu\_{\Phi}-\mu\_{-}\;<\;0. |  |

This inequality implies a contradiction for any solvent, self-sustaining exchange.
Since LTVT\mathrm{LTV}\_{T} represents retained earnings, a strictly negative limit implies the exchange requires external subsidies to cover the structural deficit.
In the absence of external capital, the exchange must either halt or become insolvent.
Consequently, LTVT​(πn)\mathrm{LTV}\_{T}(\pi\_{n}) cannot satisfy the revenue condition (R), which requires LTVT\mathrm{LTV}\_{T} to be a positive fraction of ΦT\Phi\_{T}.
∎

##### Proof of Implication (II): (S) ∧\wedge (R) ⇒\Rightarrow ¬\neg(F).

###### Proof.

Suppose both (S) and (R) hold.

1. *Revenue Implication:* By (R), LTVT≥cR​ΦT\mathrm{LTV}\_{T}\geq c\_{R}\Phi\_{T}.
This implies diversions are limited: 𝒟T=ΦT−LTVT≤(1−cR)​ΦT\mathcal{D}\_{T}=\Phi\_{T}-\mathrm{LTV}\_{T}\leq(1-c\_{R})\Phi\_{T}.

2. *Solvency Implication:* By (S), RT≈0R\_{T}\approx 0.
From DT≤BT+𝒟T+RTD\_{T}\leq B\_{T}+\mathcal{D}\_{T}+R\_{T}, we have:

|  |  |  |
| --- | --- | --- |
|  | BT≥DT−𝒟T≥DT−(1−cR)​ΦT.B\_{T}\;\geq\;D\_{T}-\mathcal{D}\_{T}\;\geq\;D\_{T}-(1-c\_{R})\Phi\_{T}. |  |

3. *Fairness Violation:*
Dividing by nn and taking limits:

|  |  |  |
| --- | --- | --- |
|  | limn→∞BTn≥μ−−(1−cR)​μΦ.\lim\_{n\rightarrow\infty}\frac{B\_{T}}{n}\;\geq\;\mu\_{-}-(1-c\_{R})\mu\_{\Phi}. |  |

Since μ−>μΦ\mu\_{-}>\mu\_{\Phi} (Assumption [I.3](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem3 "Assumption I.3 (Structural Deficit Regime). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization")) and cR∈(0,1]c\_{R}\in(0,1], the RHS is strictly positive:

|  |  |  |
| --- | --- | --- |
|  | μ−−(1−cR)​μΦ>μΦ−(1−cR)​μΦ=cR​μΦ> 0.\mu\_{-}-(1-c\_{R})\mu\_{\Phi}\;>\;\mu\_{\Phi}-(1-c\_{R})\mu\_{\Phi}\;=\;c\_{R}\mu\_{\Phi}\;>\;0. |  |

Thus, BT=Θ​(n)B\_{T}=\Theta(n).
Since BT=θn​DTB\_{T}=\theta\_{n}D\_{T} and DT=Θ​(n)D\_{T}=\Theta(n), this implies θn=Θ​(1)\theta\_{n}=\Theta(1).

With θn=Θ​(1)\theta\_{n}=\Theta(1), the load κn=θn​n/bn→∞\kappa\_{n}=\theta\_{n}n/b\_{n}\to\infty (since bn=o​(n)b\_{n}=o(n)).
By Theorem [B.3](https://arxiv.org/html/2512.01112v1#A2.Thmtheorem3 "Theorem B.3 (PTSR scaling). ‣ B.4 Asymptotic Scaling Results ‣ Appendix B Moral Hazard and Extreme Value Analysis ‣ Autodeleveraging: Impossibilities and Optimization"), 𝖯𝖳𝖲𝖱T≍1/κn→0\mathsf{PTSR}\_{T}\asymp 1/\kappa\_{n}\to 0.
This violates (F), which requires 𝖯𝖳𝖲𝖱T=Θ​(1)\mathsf{PTSR}\_{T}=\Theta(1).
∎

##### Proof of Implication (III): (F) ∧\wedge (R) ⇒\Rightarrow ¬\neg(S).

###### Proof.

Suppose both (F) and (R) hold.

1. *Fairness Implication:* As shown in (I), (F) implies BT=o​(n)B\_{T}=o(n).

2. *Revenue Implication:* As shown in (II), (R) implies 𝒟T≤(1−cR)​ΦT\mathcal{D}\_{T}\leq(1-c\_{R})\Phi\_{T}.

3. *Solvency Violation:*
From the Solvency-Revenue Identity: RT≥DT−BT−𝒟TR\_{T}\geq D\_{T}-B\_{T}-\mathcal{D}\_{T}.
Dividing by nn and taking limits:

|  |  |  |
| --- | --- | --- |
|  | limn→∞RTn≥μ−−0−(1−cR)​μΦ.\lim\_{n\rightarrow\infty}\frac{R\_{T}}{n}\;\geq\;\mu\_{-}-0-(1-c\_{R})\mu\_{\Phi}. |  |

By Assumption [I.3](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem3 "Assumption I.3 (Structural Deficit Regime). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization") (μ−>μΦ\mu\_{-}>\mu\_{\Phi}), we have:

|  |  |  |
| --- | --- | --- |
|  | μ−−(1−cR)​μΦ>μΦ−(1−cR)​μΦ=cR​μΦ> 0.\mu\_{-}-(1-c\_{R})\mu\_{\Phi}\;>\;\mu\_{\Phi}-(1-c\_{R})\mu\_{\Phi}\;=\;c\_{R}\mu\_{\Phi}\;>\;0. |  |

Thus, RTR\_{T} scales as Θ​(n)\Theta(n).
This implies 𝐏𝐫𝐨𝐛[RT>0]→1\mathop{\bf Prob}[R\_{T}>0]\to 1 and ∑Rt→∞\sum R\_{t}\to\infty, violating (S).
∎

##### Sharpness and Attainability.

The trilemma bound is tight in the sense that each pair of desiderata *can* be achieved by an appropriately designed policy:

###### Proposition I.9 (Attainability of Two Desiderata).

Under Assumptions [I.1](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem1 "Assumption I.1 (Regular Variation). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization")–[I.3](https://arxiv.org/html/2512.01112v1#A9.Thmtheorem3 "Assumption I.3 (Structural Deficit Regime). ‣ Distributional Assumptions. ‣ Appendix I Formal Proof of the ADL Trilemma ‣ Autodeleveraging: Impossibilities and Optimization"):

1. 1.

   (S) ∧\wedge (F) is achieved by a *high-diversion* policy: set diversions 𝒟T≈ΦT\mathcal{D}\_{T}\approx\Phi\_{T} (taking all revenue) plus potentially external capital if μ−>μΦ\mu\_{-}>\mu\_{\Phi} is very large. This covers deficits (DT≈𝒟TD\_{T}\approx\mathcal{D}\_{T}) with minimal haircuts (BT≈0B\_{T}\approx 0), satisfying (S) and (F), but reducing LTVT→0\mathrm{LTV}\_{T}\to 0, violating (R).
2. 2.

   (S) ∧\wedge (R) is achieved by a *Queue* (concentrated haircut) policy: use high severity θn=Θ​(1)\theta\_{n}=\Theta(1) to generate BT≈DTB\_{T}\approx D\_{T}. This ensures solvency and preserves fee revenue (since 𝒟T≈0\mathcal{D}\_{T}\approx 0), but destroys the top winners (𝖯𝖳𝖲𝖱T→0\mathsf{PTSR}\_{T}\to 0), violating (F).
3. 3.

   (F) ∧\wedge (R) is achieved by a *Pro-Rata with low severity* policy: use EV-scaled severity θn=O​(bn/n)\theta\_{n}=O(b\_{n}/n) and low diversion. This keeps LTVT≈ΦT\mathrm{LTV}\_{T}\approx\Phi\_{T} and 𝖯𝖳𝖲𝖱T=Θ​(1)\mathsf{PTSR}\_{T}=\Theta(1), but leaves an unhedged deficit RT≈DT>0R\_{T}\approx D\_{T}>0, violating (S).

### I.2 Connection to Classical Impossibility Results

The ADL trilemma echoes classical impossibility results in mechanism design and finance:

* •

  *Arrow’s Impossibility Theorem:* No voting rule satisfies Pareto efficiency, independence of irrelevant alternatives, and non-dictatorship simultaneously [Arrow1951].
* •

  *Mundell-Fleming Trilemma:* In international finance, a country cannot simultaneously maintain a fixed exchange rate, free capital movement, and independent monetary policy [Mundell1963, Fleming1962].
* •

  *CAP Theorem:* In distributed systems, a database cannot provide consistency, availability, and partition tolerance simultaneously [Brewer2000, GilbertLynch2002].
* •

  *Credibility Trilemma:* Single-item auctions cannot be simultaneously optimal, strategy-proof, and credible, forcing designers to sacrifice at least one desideratum [AkbarpourLi2020].

These connections suggest the trilemma is a fundamental constraint arising from the heavy-tailed nature of crypto markets, not an artifact of specific mechanism choices.

##### Circumventing Impossibility via Relaxations.

While the impossibility results are strict in worst-case settings, recent literature demonstrates that they can be circumvented under probabilistic assumptions or cryptographic commitments:

1. 1.

   *Quantitative Arrow’s Theorem:*
   Recent results in quantitative social choice show that while Arrow’s impossibility holds in the worst case, the probability of paradoxical outcomes (like intransitivity) can be small for many natural distributions of preferences [MosselNeemanTamuz2014].
   Analogously, our ADL trilemma bounds hold with high probability under heavy-tailed distributions, but dynamic policies (like Stackelberg controllers) can minimize the frequency of trilemma-binding events, achieving a “quantitative” relaxation.
2. 2.

   *Probabilistic CAP Theorem:*
   Blockchains circumvent the strict CAP theorem by weakening consistency to probabilistic finality (e.g., Nakamoto consensus) or availability to liveness under synchronous periods [PassShi2017, Shi2020, ShiConsensusBook].
   This parallels the (S) vs. (R) trade-off: exchanges effectively accept probabilistic solvency (via insurance funds) to maintain liveness (continuous trading/revenue).
3. 3.

   *Cryptographic Commitments for Credibility:*
   The credibility trilemma of Akbarpour and Li motivates cryptographic mechanisms that make optimal auctions simultaneously credible and strategy-proof by enforcing operator commitments [AkbarpourLi2020, FerreiraWeinberg2020, EssaidiFerreiraWeinberg2022, ChitraFerreiraKulkarni2024].
   For ADL, this suggests that verifiable execution (e.g. via zero-knowledge proofs or on-chain logic) could allow an exchange to commit to a dynamic policy that balances the trilemma better than any opaque static policy could, by removing the operator’s incentive to deviate during crises.