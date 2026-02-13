---
authors:
- Agathe Sadeghi
- Zachary Feinstein
doc_id: arxiv:2602.12104v1
family_id: arxiv:2602.12104
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Liquidation Dynamics in DeFi and the Role of Transaction Fees
url_abs: http://arxiv.org/abs/2602.12104v1
url_html: https://arxiv.org/html/2602.12104v1
venue: arXiv q-fin
version: 1
year: 2026
---


Agathe Sadeghi
Stevens Institute of Technology, School of Business, Hoboken, NJ 07030. asadeghi@stevens.edu Corresponding author.
  
Zachary Feinstein
Stevens Institute of Technology, School of Business, Hoboken, NJ 07030.

###### Abstract

Liquidation of collateral are the primary safeguard for solvency of lending protocols in decentralized finance. However, the mechanics of liquidations expose these protocols to predatory price manipulations and other forms of Maximal Extractable Value (MEV). In this paper, we characterize the optimal liquidation strategy, via a dynamic program, from the perspective of a profit-maximizing liquidator when the spot oracle is given by a Constant Product Market Maker (CPMM). We explicitly model Oracle Extractable Value (OEV) where liquidators manipulate the CPMM with sandwich attacks to trigger profitable liquidation events. We derive closed-form liquidation bounds and prove that CPMM transaction fees act as a critical security parameter. Crucially, we demonstrate that fees do not merely reduce attacker profits, but can make such manipulations unprofitable for an attacker. Our findings suggest that CPMM transaction fees serve a dual purpose: compensating liquidity providers and endogenously hardening CPMM oracles against manipulation without the latency of time-weighted averages or medianization.

Keywords: Lending Protocols, Automated Market Makers, Oracle Extractable Value, Liquidation events

## 1 Introduction

Decentralized Finance (DeFi) has grown exponentially since 2018, transforming the traditional financial landscape by offering blockchain-based financial services within the crypto ecosystem. One of the most significant developments in DeFi is the rise of borrowing and lending platforms (LPs), which allow crypto asset holders to earn interest or access additional funds by utilizing their existing assets. Since 2020, the outstanding debt in DeFi lending has increased dramatically, driven by the wider adoption of stablecoins and their role in providing stability to the volatile cryptocurrency market. As of this writing LPs hold around $80 billion in total value locked (TVL).111<https://defillama.com/protocols/lending>, accessed October 2025

The standard operational process within these platforms includes lenders, who have surplus funds, supplying assets which are often stablecoins, to a specific lending smart contract. The utilization ratio which is the proportion of supplied liquidity currently borrowed in relation to the total amount of funds available, determines the interest rate on lending platforms. Each lender receives a platform-specific utility token representing their deposit, often functioning as a certificate of deposit. These tokens accrue interest and have a value equivalent to the underlying asset. Depositors can withdraw their funds at any time, typically by redeeming their utility tokens back to the platform.

In exchange, borrowers provide risky crypto assets, like Bitcoin or Ether, as collateral to back loans, which are frequently denominated in stablecoins. Smart contracts act as the direct interface connecting depositors and borrowers, streamlining the entire loan lifecycle, which includes loan issuance, repayment tracking, and collateral liquidation. Furthermore, smart contracts are responsible for managing collateral by assigning a specific margin to each collateral type and rigorously enforcing overcollateralization requirements (capponi23).

### 1.1 Motivation

Despite its innovations, DeFi lending is not immune to risks associated with market volatility, liquidity mismatches, and operational inefficiencies (gudgeon20\_1). Additionally, the trade-off between risk and reward in DeFi lending can be analyzed empirically (lehar22). Volatile crypto prices frequently trigger loan liquidations when borrowers fail to maintain their Loan-to-Value (LTV) ratios.
LTV ratios quickly deteriorate in response to a drop in collateral prices, which leads to automated liquidations. Lending platforms run the risk of bad debt in the absence of prompt liquidation since declining collateral values might not be sufficient to cover the outstanding debt. These forced sales have the potential to further depress collateral prices, which could trigger a chain reaction of liquidations throughout the ecosystem.
For example, during the January 2022 crypto sell-off, liquidations surged to their highest level since May 2021, erasing $50 billion in borrowed asset value.222International Monetary Fund (2022). Global Financial Stability Report: Shock waves from the War in Ukraine Test the Financial System’s Resilience, Chapter 3. Available at: <https://www.imf.org/-/media/Files/Publications/GFSR/2022/April/English/ch3.ashx> DeFi platforms set their own maximum LTVs based on factors such as collateral type and market volatility.

Liquidation events are essential automated mechanisms in DeFi lending protocols that are intended to safeguard the system’s solvency. The main cause of these occurrences is when a borrower’s Health Factor (HF), calculated as the ratio of value of collateral to debt, drops bellow a specified liquidation threshold. While the LTV ratio calculates the borrowed value relative to the collateral, HF is the inverse relationship (adjusted for the liquidation threshold) indicating a position’s proximity to liquidation. The protocols’ solvency is undermined when the value of the collateral assets, which are usually risky cryptocurrencies falls drastically. The loan is now automatically considered eligible for liquidation since it is undercollateralized. This liquidation necessity demonstrates the importance of having a reliable price for the collateral asset available for the lending protocol contract.

These prices can be obtained from off-chain suppliers like Chainlink or from decentralized exchanges’ on-chain oracles such as Uniswap. However, top platforms, like Aave and Compound rely on further robustness mechanisms like time-weighted average price (TWAP) feeds that update once per block, in order to reduce the risk of short-term manipulation of spot markets. Although these defenses increase the oracle’s resistance to manipulation, they also create weaknesses in times of rapid crisis (like during the collapse of Terra/Luna) when off-chain oracles might malfunction or TWAPs might react too slowly to reflect sharp price drops. Using off-chain or time-averaged oracle mechanisms usually requires more conservative LTV thresholds to account for update latency, which ultimately lowers capital efficiency and raises the collateral requirements for borrowers.

Although it is theoretically possible for borrowers to avoid liquidation by adding more collateral or manually repaying their loans, this is frequently not feasible for regular users. Timely manual intervention is difficult due to the need for continuous monitoring of fluctuating collateral prices and transaction fee variability. Theoretically, any blockchain user in the DeFi ecosystem can keep an eye on HFs and start the liquidation process on these undercollateralized positions. But in reality, liquidation in DeFi has become a very specialized task that is primarily carried out by advanced bots. With the help of flash loans (qin21) and other algorithms, these bots can quickly liquidate large amounts of undercollateralized positions, removing the need for capital. Over 70% of liquidable positions are now instantly liquidated by these automated agents, according to empirical data, demonstrating the significant improvement in these liquidators’ efficiency over time (perez21). The substantial potential profits, which can occasionally amount to hundreds of thousands of dollars from a single transaction, are what propel this high speed and scale and encourage ongoing advancements in liquidation methods.

We investigate the use of constant product market makers (CPMMs) as an on-chain, trustless and without a lag spot oracles. To assess their robustness, we explicitly model the Oracle Extractable Value (OEV) and Maximal Extractable Value (MEV) accessible to sophisticated liquidators who can manipulate prices within a single block. We then study how transaction fees imposed by AMMs can act as an inherent safeguard, enhancing intra-block spot oracles’ robustness to transient attacks: by decreasing the marginal profitability of price manipulation, AMM trading fees alter the incentives of liquidators and potential attackers. More precisely, when transaction fees are incorporated into liquidation and MEV-driven tactics such as sandwiching liquidation events, profitability declines and eventually becomes negative beyond a critical threshold fee. This highlights the dual function of transaction fees, often neglected in prior research, in compensating liquidity providers while strengthening oracle resilience by deterring intra-block price manipulation that might otherwise trigger unnecessary liquidations.

### 1.2 Literature Review

DeFi lending platforms operate by receiving crypto assets as deposits and lending them out to borrowers who meet specific collateral requirements. These platforms rely on liquidity pools, which are pools of deposited assets made available for lending. Users who deposit their crypto assets into these pools earn interest in return. Aave, MakerDAO and Compound are notable instances of decentralized lending protocols that have become very popular. Among DeFi lenders, Aave stands out for having the highest total value locked (iftikhar25).

For borrowers, DeFi platforms offer the ability to borrow crypto assets from these liquidity pools by posting their deposited assets as collateral. The interest rate on borrowing, denominated in the borrowed asset (john23), varies based on the utilization rate333The utilization rate of a crypto asset represents the proportion of total loans to total deposits for that asset on the platform. When the deposit pool has greater available liquidity, the lending rate tends to be lower. of the lending pool, meaning higher demand for an asset can drive up borrowing costs. This mechanism helps balance supply and demand within the system. Collateral is central to managing risks in DeFi lending, as it safeguards the platform against market volatility. Borrowers are often required to overcollateralize their loans (wang22), meaning they must provide collateral worth more than the loan itself. This is achieved by applying a collateral factor which is a discount rate assigned to each asset type. For example, if an asset has a collateral factor of 0.8, a borrower can only borrow up to 80% of the posted collateral’s value. Some assets, like Tether (USDT) on certain platforms, have a collateral factor of zero, meaning they cannot be used as collateral. As noted by cornelli24, the anonymity and volatility of crypto assets necessitate overcollateralization as the primary risk management tool, unlike traditional banking, which uses undercollateralized loans backed by diverse assets like real estate. This reliance on crypto assets as collateral also makes DeFi inherently self-referential.

Borrowers on DeFi platforms can repay their loans at any time, but they must continuously meet collateral requirements. If the value of their collateral falls below the required threshold due to adverse price movements, liquidators are incentivized to step in. Liquidators repay the borrower’s debt and acquire the collateral in exchange for a reward, known as the liquidation bonus. This mechanism ensures that the platform remains solvent even during market volatility. However, the liquidation process can be costly, particularly when collateral shortfalls arise during periods of high volatility, leaving the platform vulnerable to further destabilization if liquidations are delayed.

DeFi lending also facilitates leveraged trading strategies, such as leveraged longs and short selling, which are widely used by investors. For instance, borrowers may post volatile crypto assets, such as Ethereum or Wrapped Bitcoin, as collateral to borrow stablecoins. Stablecoins are a type of cryptocurrency specifically created to maintain price stability (clark20). Their value is usually tied to a reference asset, such as the US dollar, to minimize fluctuations. For a thorough understanding of these coins we refer the reader to klages20.

Many studies explore lending and borrowing in the context of DeFi. bartoletti21; bartoletti22 demonstrate essential behavioral characteristics of decentralized lending and borrowing protocols. perez21 presents an abstract framework to analyze the state of decentralized lending and borrowing protocols. szpruch24 explores loan contracts as American perpetual barrier options. mueller24 observes that the liquidation mechanism in DeFi lending protocols amplifies both the costs and risks associated with leveraged investments.

The liquidation mechanism should aim to minimize both the frequency of liquidation events and the total number of transactions, given the constrained nature of blockchains (qin21\_1). qin23 proposes reversible call options, which allows the seller of a call option to cancel the contract before its maturity date. iragorri21 finds that if liquidators are incentivized sufficiently, the risk of undercollateralization will be kept low.

Bad debt can happen as well. This occurs when the value of the borrower’s collateral is insufficient to cover their outstanding debt (under-collateralizitation) after liquidation, exposing the protocol to financial losses (gudgeon20). The accumulation of bad debt diminishes the total liquidity available in a lending protocol, resulting in higher interest rates for borrowers. If the lending pool becomes entirely comprised of bad debt, lenders will be unable to withdraw their funds. Another risk to consider is that the liquidator’s transaction fee may exceed the value of the discounted collateral obtained, failing to provide an incentive for them to assist in closing the position.

Peer-to-peer and peer-to-pool marketplaces known as Decentralized Exchanges (DEXs) facilitate direct transactions between cryptocurrency traders. A key potential of decentralized finance is embodied by this architecture: enabling financial transactions without the need for conventional middlemen like banks, brokers, or payment processors.

There have been two main developments in DEX architectures. Launched in 2016, Order-Book-Based DEXs are the first version of these exchanges (daian20). By using a central limit order book where buyers and sellers place bid and ask orders, which are subsequently matched to execute trades, these platforms function similarly to traditional stock exchanges. With the advent of AMMs in 2018, a major architectural breakthrough was made possible by protocols such as Uniswap (angeris20). The AMM model uses liquidity pools, which usually consist of two separate asset reserves, to facilitate trading rather than an order book. An AMM’s core implementation is made possible by a number of smart contracts that run on a blockchain. In order to determine prices algorithmically, pioneering AMMs like Uniswap v2 use a constant product function, which can be mathematically expressed as x×y=kx\times y=k, where xx and yy are the quantities of two tokens in the pool and kk is their constant product (angeris21). This mathematical connection guarantees that the current supply and demand dynamics within that particular pool will determine the token price.

Transaction and gas fees are important aspects of user behavior and market dynamics in DEXs as well. On blockchain platforms like Ethereum, gas fees, which are based on network congestion and the computational complexity of transactions, act as incentives for validators to add transactions to blocks (cong21). DEX protocols may impose transaction fees in addition to gas in order to fund liquidity providers or platform upkeep (capponi21). These expenses can have a big influence on trading tactics, especially in situations with high frequency or low margins where fee optimization is crucial. The efficiency and accessibility of decentralized trading are shaped by the interaction of gas prices, transaction throughput, and user incentives. This interaction affects market participation as well as the general scalability of DEX ecosystems.

Volatility in collateral prices due to liquidations can exacerbate price impact in the DEX, creating feedback loops. That is why price impact matters. Price impact refers to the effect of asset liquidation on the market price of those assets, particularly in times of financial distress. zach17 introduces a framework that models the dynamics of financial contagion caused by price impact and fire sales in systems with multiple illiquid assets in traditional financial markets.

Maximal Extractable Value (MEV) is the extra profit that block producers, like miners, can make by choosing the order in which transactions go into a block. This matters a lot in areas like DeFi, where the order of transactions can affect the outcome (daian20). This ability to reorder transactions allows for practices akin to frontrunning (eskandari19) and sandwich trading (zhou21), which would be considered illegal in traditional financial markets (auer22). Specialized actors known as searchers track pending transactions to spot profit-making opportunities, like arbitrage between exchanges, atomic arbitrage or liquidations on lending platforms. They then submit their own carefully crafted transactions or bundles to capture that value. Block producers can include these transactions in the blocks they create, often giving priority to those offering the highest fees or direct payments. By controlling the order and composition of transactions, they can extract additional value from the block (qin22; li23). MEV also leads to inefficiencies by filling blocks with profit-seeking transactions and pushing out valuable user activity (capponi25). Some work has been published on how to mitigate the MEV effect (zhou21-1; heimach22; yang23). There are also other kind of attacks that can be done in DeFi, see e.g., lee23.

One specific kind of attack involves deliberately pushing the price of the risky asset down by selling large amount of it first. This is putting a sell order at the beginning of the block, i.e., frontrunning. Followed with other orders, the attacker puts a buy order at the end of the same block, allowing them to repurchase the asset with the lowered price, i.e., backrunning. They can potentially profit from the classic selling high, buying low strategy, known as sandwiching in the DeFi space. When the initial frontrunning is used to manipulate the price of an asset for use in another smart contract, the profits from this attack can be characterized as OEV. We will explicitly consider attacks of this type within this work.

### 1.3 Primary Contributions

#### Optimal Liquidations

In contrast to models focused on the lending platform’s perspective and the mitigation of bad debt (see, e.g., qin21\_1), we examine liquidation spirals from the liquidator’s point of view in Section [3.1](https://arxiv.org/html/2602.12104v1#S3.SS1 "3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"). In order to isolate how real-time price impact shapes liquidation incentives, particularly during fast-moving crises, we assume that the lending platform quotes the intra-block spot price to measure the health of the loan’s collateral. A dynamic program for the liquidator’s profit maximization within a single block along with a semi-analytic characterization of the value function and an implementable algorithm are presented.

#### Switching Condition

We monitor three practical limits on how far a troubled position can be pushed by a liquidator. First, the maximum amount of collateral that the liquidator can confiscate (after deducting the discount and fees) is known as the collateral cap. Second, the debt cap, is the amount of liquidation that completely settles the borrower’s outstanding debt. If the liquidator reaches the debt cap, even if most or all of the collateral was taken, the loan is closed and there is no bad debt. Third, the closing-factor cap, is not a hard policy limit; it’s the HF checkpoint. It is the liquidation amount at which the position’s health factor reaches the pertinent threshold. These three make it simple to interpret the results: if we can either (a) reach the debt cap and retire the loan, or (b) reach the closing-factor cap and return the position’s health to 1 before depleting collateral, the liquidation is successful. Bad debt only appears when we run out of collateral or the HF is restored to 1 before the debt is paid off in full. That is, as much collateral has been liquidated as possible but there is still a loan balance remaining to be paid.

#### Impact of Fees on MEV Profitability

We show how incorporating AMM trading fees into the liquidation and any MEV triggered (sandwich) attacks, compress the profitable region and can even cause reversion for bundles backed by flash loans in Section [4](https://arxiv.org/html/2602.12104v1#S4 "4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"). We show that smaller, staged liquidations outperform lump-sum ones when fees are present. We numerically determine the fee levels at which all viable attacks lose their profitability in Section [4.1](https://arxiv.org/html/2602.12104v1#S4.SS1 "4.1 Limiting Behavior ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), emphasizing fees as a design lever for strengthening AMM-based oracles in Section [4.2](https://arxiv.org/html/2602.12104v1#S4.SS2 "4.2 Fees as Oracle Protection ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees").

## 2 Background

In this section, we discuss the stylized modeling framework for the lending and exchange protocols which we focus on within this work. In order to maintain consistency and clarity, we also introduce the notation that will be used throughout the paper.

### 2.1 Lending Protocols

The health factor is a key statistic in DeFi lending platforms, measuring the stability of a borrower’s position relative to the risk of liquidation. It represents the ratio of the liquidation-threshold-weighted collateral value to the total debt value, both denominated in a constant numéraire (such as ETH or USDC). The weights are determined by the collateral-specific liquidation thresholds (also known as the haircut rate), which reflect the maximum borrowing capacity of each asset before liquidation is triggered. The general formula for the health factor is given by

|  |  |  |
| --- | --- | --- |
|  | H​F=liquidation threshold×amount of collateral×price of collateralvalue of borrowed assets.HF=\frac{\text{liquidation threshold}\times\text{amount of collateral}\times\text{price of collateral}}{\text{value of borrowed assets}}. |  |

The numerator sums the weighted values of all collateral tokens deposited by the user, adjusted by their respective liquidation thresholds. The denominator accounts for the user’s total debt. All values are denominated in, e.g., USDC to maintain consistency across assets. A higher HF reflects a more secure position, whereas a value below 1 indicates that the user’s position is undercollateralized and at risk of liquidation. Platforms, in practice, enforce two thresholds: if the HF falls below the Closing Factor (CF), then up to 100% of the debt can be liquidated to fully resolve the position; if the HF falls below 1 but still higher than CF, only a portion (κ\kappa) of the borrower’s debt becomes liquidatable.

Figure [1](https://arxiv.org/html/2602.12104v1#S2.F1 "Figure 1 ‣ 2.1 Lending Protocols ‣ 2 Background ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") depicts the platform’s balance sheet before and after a liquidation. The platform holds cc units of collateral priced at p0p\_{0} against debt bb prior to liquidation; only a portion θ\theta of the collateral’s market value counts toward safety, so HF compares θ​p0​c\theta\,p\_{0}\,c to bb. A liquidation is allowed when HF is less than 11 or the closing-factor threshold C​FCF. In that step, a liquidator receives x​(1+ℓ)x\,(1+\ell) units of collateral and repays β​(x)\beta(x) of the debt, where xx is the liquidation size and ℓ\ell is the liquidation bonus. After liquidation, the remaining debt is b−β​(x)b-\beta(x), and the platform’s held collateral becomes c−x​(1+ℓ)c-x\,(1+\ell), marked at the updated price p1p\_{1}. The collateral transferred out, x​(1+ℓ)x\,(1+\ell), and the reduced debt, β​(x)\beta(x), are represented by the greyed out box at the top of the figure. After the liquidation, HF is defined as the same ratio, eligible collateral value over debt value, but calculated using the updated parameters. The position is healthy if the post-liquidation HF goes back to at least 11. Otherwise, further liquidations might be necessary, and in the worst case, bad debt might remain. The formula for HF after the first liquidation is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​F\displaystyle HF | =θ​(c−x​(1+ℓ))​p1b−β​(x)\displaystyle=\frac{\theta\,(c-x\,(1+\ell))\,p\_{1}}{b-\beta(x)} |  | (1) |

p0​cp\_{0}cE​q​u​i​t​y{\displaystyle Equity}E​q​u​i​t​y{\displaystyle Equity}bbb−β​(x)b-\beta(x)p1(c−x(1+ℓ))\begin{array}[]{l}p\_{1}(c-\\
\ \ x(1+\ell))\end{array}


Figure 1: Lending platform reserves Left initial state Right after liquidation state

Without timely liquidation, collateral shortfalls can undermine platform solvency. Overcollateralization mitigates some risks, but expected losses still average around 0.9%, with riskier borrowers incurring larger losses as noted in imf22. These dynamics underscore the importance of managing collateral and liquidation risks to ensure the resilience of DeFi platforms in volatile market conditions.

### 2.2 Decentralized Exchanges

Let A0A\_{0} and B0B\_{0} denote the initial AMM reserves of a risky asset (e.g., collateral) and a stablecoin (e.g., USDC), respectively. The AMM charges a transaction fee γ\gamma (e.g., 30 basis points in Uniswap v2) on the incoming asset. In practice, this means only 1−γ1-\gamma of the asset is being deposited in the pool, while liquidity providers receive the remaining amount as payment for their capital contributions. The constant product market maker (CPMM) rule in Uniswap v2 incorporates this fee structure directly, thereby modifying the reserves after each swap. Given this rule, the initial spot price at the CPMM is p0=B0A0p\_{0}=\frac{B\_{0}}{A\_{0}}.
Under the scenario where we swap aa units of asset AA for bb units of asset BB, the invariant must hold:

|  |  |  |
| --- | --- | --- |
|  | (A0+a​(1−γ))​(B0−b)=A0​B0⇒b=B0​a​(1−γ)A0+a​(1−γ)\displaystyle(A\_{0}+a(1-\gamma))(B\_{0}-b)=A\_{0}B\_{0}\,\quad\Rightarrow\quad b=\frac{B\_{0}a(1-\gamma)}{A\_{0}+a(1-\gamma)} |  |

Hence, after the swap, the updated reserves of the assets held by the CPMM will be A1=A0+a​(1−γ)A\_{1}=A\_{0}+a(1-\gamma) and B1=B0−b=A0​B0A0+a​(1−γ)B\_{1}=B\_{0}-b=\frac{A\_{0}B\_{0}}{A\_{0}+a(1-\gamma)} while the updated price becomes p1=B1A1p\_{1}=\frac{B\_{1}}{A\_{1}}. Figure [2](https://arxiv.org/html/2602.12104v1#S2.F2 "Figure 2 ‣ 2.2 Decentralized Exchanges ‣ 2 Background ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") visualizes the reserve update along the constant product hyperbola when neglecting the fees (γ=0\gamma=0).

Token B reserveToken A reserve(A0,B0A\_{0},B\_{0})(A1,B1A\_{1},B\_{1})A​B=kAB=k 


Figure 2: Constant product hyperbola. kk is a constant.

## 3 Optimal Liquidation at Lending Protocols

The liquidation process in the lending platform creates an optimization problem: the searcher (same as liquidator in our case) aims to maximize liquidation profit under conditions such as (i) the HF must fall to or below 1 for liquidation to be valid, (ii) there must be sufficient available collateral and outstanding loan balance, and (iii) the prevailing market price updates based on the holdings of a CPMM. We interpret the resulting profits as an upper bound, as we ignore gas costs.

We specifically model this problem from the viewpoint of the liquidator, not the lending protocol, emphasizing the motivations and tactics of the liquidator. Two main strategies emerge for the searcher: Full liquidation in a single block to realize a one-time profit or a gradual liquidation, keeping HF just below 1 (or the closing factor) to repeatedly liquidate over multiple steps, potentially extracting more value.444Later, in Lemma [1](https://arxiv.org/html/2602.12104v1#Thmtheorem1 "Lemma 1. ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), we show that small liquidations are more profitable than a lump sum liquidation. We use dynamic programming to model the strategic behavior of the liquidator, since the optimal action depends on expected future profits which in turn depend on future asset prices.

Additionally, we assume that the spot price from the CPMM is used by the lending protocol to calculate the HF. While most production platforms use TWAPs to reduce short-term volatility, using the instantaneous spot price gives a clearer picture of how intra-block price fluctuations directly affect liquidation incentives. Since the spot price is the primary driver from which TWAPs are ultimately derived, this modeling decision enables us to isolate and analyze the dynamic interaction between price impact and liquidation behavior without loss of generality which is the paper’s main focus.

We also recall that the amount of a borrower’s debt that can be liquidated is determined by two parameters; the health factor threshold CF, which determines when a position becomes eligible for liquidation and liquidation fraction κ\kappa, which specifies the fixed portion of the outstanding debt that can be repaid in a single liquidation transaction. We first analyze the case under fixed parameters, i.e., (C​F,κ)(CF,\kappa) and afterwards generalize it to more flexible cases where several threshold pairs, i.e. (C​Fi,κi)(CF\_{i},\kappa\_{i}), are taken into account in order to identify the combination that maximizes profits and capture various liquidation regimes.

In this work, we extend the approach of, e.g., cohen23, to incorporate transaction fees and examine scenarios where a liquidator can initiate liquidation by crashing the collateral price on DEXs (Section [4](https://arxiv.org/html/2602.12104v1#S4 "4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")). We formalize this setup below, focusing on the mechanics of Aave555Aave is a DeFi lending platform built on the Ethereum blockchain, designed to facilitate borrowing and lending of cryptocurrency assets. as the lending platform and Uniswap v2 as the DEX where the liquidity is distributed evenly across ticks.

It is helpful to introduce the shorthand H​F​(c,b,A,B):=θ​B​cA​bHF(c,b,A,B):=\frac{\theta B\,c}{A\,b} which represents the borrower’s health factor in any given state. In this case, the *updated* quantities corresponding to that state are (c,b,A,B)(c,b,A,B). In other words, following a liquidation trade of size xx, the updated collateral becomes c−x​(1+ℓ)c-x(1+\ell), the updated debt becomes b−β​(x)b-\beta(x) and the updated AMM reserves produce the updated price p1p\_{1}. While the schematic expression in ([1](https://arxiv.org/html/2602.12104v1#S2.E1 "Equation 1 ‣ 2.1 Lending Protocols ‣ 2 Background ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) showed how these variables change, the compact form above assesses the health factor following the updates. The corresponding health factor can therefore be obtained by directly substituting the current values of (c,b,A,B)(c,b,A,B) at each stage of the process.

### 3.1 Single Threshold Health Factor

Following the notation introduced in Section [2](https://arxiv.org/html/2602.12104v1#S2 "2 Background ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), we now consider objective of a liquidator at the lending protocol.
That is, finding the ideal liquidation size xx in a sequenced transaction in order to maximize the overall anticipated profit. Every liquidation generates an instant profit and, if the resulting health factor stays below the closing threshold C​FCF, the liquidator can continue to make money from subsequent liquidations. In this way, given the current collateral cc, outstanding debt bb, and DEX reserves (A,B)(A,B), the ideal liquidation strategy is captured by the value function V​(⋅)V(\cdot) of the dynamic program:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(c,b,A,B)\displaystyle V(c,b,A,B) | ={supx≥0x≤xcx≤xκ​bx≤xc​f​[B​x​(1+ℓ)​(1−γ)A+x​(1+ℓ)​(1−γ)−B​xA+V​(c−x​(1+ℓ),b−B​x/A,A¯,B¯)]if ​H​F​(c,b,A,B)≤C​F0if ​H​F​(c,b,A,B)>C​F\displaystyle=\begin{cases}\underset{\begin{subarray}{c}x\geq 0\\ x\leq x\_{c}\\ x\leq x\_{\kappa b}\\ x\leq x\_{cf}\end{subarray}}{\sup}\Bigg[\begin{array}[]{l}\frac{Bx(1+\ell)(1-\gamma)}{A+x(1+\ell)(1-\gamma)}-\frac{Bx}{A}\\ +V(c-x(1+\ell),b-Bx/A,\bar{A},\bar{B})\end{array}\Bigg]&\text{if }HF(c,b,A,B)\leq CF\\ 0&\text{if }HF(c,b,A,B)>CF\end{cases} |  | (2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A¯\displaystyle\bar{A} | =A+x​(1+ℓ)​(1−γ),\displaystyle=A+x(1+\ell)(1-\gamma), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B¯\displaystyle\bar{B} | =A​BA+x​(1+ℓ)​(1−γ).\displaystyle=\frac{AB}{A+x(1+\ell)(1-\gamma)}. |  |

The liquidator selects the liquidation size xx at each stage within the feasible range of 0 to min⁡{xc,xκ​b,xc​f}\min\{x\_{c},x\_{\kappa b},x\_{cf}\}, where xc=c1+ℓx\_{c}=\frac{c}{1+\ell} and xκ​b=κ​b​AB−κ​b​(1−γ)​(1+ℓ)x\_{\kappa b}=\frac{\kappa bA}{B-\kappa b(1-\gamma)(1+\ell)} represent the amount to be liquidated to clear all collateral and debt (subject to the κ\kappa constraint), respectively and xc​fx\_{cf} is the amount to be liquidated to revive the H​F=C​FHF=CF. The liquidation profit B​x​(1+ℓ)​(1−γ)A+x​(1+ℓ)​(1−γ)−B​xA\frac{Bx(1+\ell)(1-\gamma)}{A+x(1+\ell)(1-\gamma)}-\frac{Bx}{A} is the immediate payout from performing the liquidation at the DEX where B​xA\frac{Bx}{A} is paid to the lending protocol to claim the collateral. The process proceeds recursively, updating the state variables in accordance with the constant product pricing rule and accounting for transaction fees γ\gamma and discount rate ℓ\ell, if the health factor following liquidation, H​FHF, stays below the closing factor C​FCF.

###### Remark 1.

During liquidation, the health factor in ([1](https://arxiv.org/html/2602.12104v1#S2.E1 "Equation 1 ‣ 2.1 Lending Protocols ‣ 2 Background ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) updates to reflect changes in collateral, debt, and price. After swapping collateral into the debt asset against a CPMM with reserves (A,B)(A,B), the post swap price is

|  |  |  |
| --- | --- | --- |
|  | p1=B−yA+x​(1−γ)​(1+ℓ)=B​A(A+x​(1−γ)​(1+ℓ))2,p\_{1}=\frac{B-y}{A+x(1-\gamma)(1+\ell)}=\frac{BA}{\bigl(A+x(1-\gamma)(1+\ell)\bigr)^{2}}\,, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=B​x​(1+ℓ)​(1−γ)A+x​(1+ℓ)​(1−γ)\displaystyle y=\frac{B\,x(1+\ell)(1-\gamma)}{A+x(1+\ell)(1-\gamma)} |  | (3) |

is the amount of debt asset received through the swap.
Substituting into the updated health factor yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​F=θ​(c−x​(1+ℓ))​B​Aκ​b​(A+x​(1−γ)​(1+ℓ))2−B​x​(A+x​(1−γ)​(1+ℓ)).HF=\frac{\theta(c-x(1+\ell))BA}{\kappa b\bigl(A+x(1-\gamma)(1+\ell)\bigr)^{2}-Bx\bigl(A+x(1-\gamma)(1+\ell)\bigr)}. |  | (4) |

Since H​F>0HF>0, the liquidator’s trade size xx must satisfy two feasibility constraints:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | c−x​(1+ℓ)≥0\displaystyle c-x(1+\ell)\geq 0\quad | ↔x≤xc:=c1+ℓ\displaystyle\leftrightarrow\quad x\leq x\_{c}:=\frac{c}{1+\ell} |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | κ​b−B​xA+x​(1−γ)​(1+ℓ)≥0\displaystyle\kappa b-\frac{Bx}{A+x(1-\gamma)(1+\ell)}\geq 0\quad | ↔x≤xκ​b:=κ​b​AB−κ​b​(1−γ)​(1+ℓ)\displaystyle\leftrightarrow\quad x\leq x\_{\kappa b}:=\frac{\kappa bA}{B-\kappa b(1-\gamma)(1+\ell)} |  | (6) |

The bound xcx\_{c} prevents the liquidator from withdrawing more collateral than the borrower holds, while xκ​bx\_{\kappa b} prevents repaying more than the outstanding debt (subject to the maximum liquidation size κ\kappa). Throughout this work, in addition, we often consider the bound xbx\_{b} for repaying the full debt; this value results from taking κ=1\kappa=1 in the above equation for xκ​bx\_{\kappa b}.
Often, for tractability, we impose the additional condition

|  |  |  |
| --- | --- | --- |
|  | b≤B(1−γ)​(1+ℓ),b\leq\frac{B}{(1-\gamma)(1+\ell)}\,, |  |

in order to ensure the AMM has sufficient debt-asset liquidity relative to the position being unwound.
Finally, the trade size at which the liquidation threshold is met, H​F=C​FHF=CF, is obtained by solving

|  |  |  |
| --- | --- | --- |
|  | θ​(c−x​(1+ℓ))​B​Ab(A+x(1−γ)(1+ℓ))2−Bx(A+x(1−γ(1+ℓ))=C​F,\frac{\theta(c-x(1+\ell))BA}{b\bigl(A+x(1-\gamma)(1+\ell)\bigr)^{2}-Bx\bigl(A+x(1-\gamma(1+\ell)\bigr)}=CF\,, |  |

which gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | xc​f=Λ+D2​C​F⋅Γ,x\_{cf}=\frac{\Lambda+\sqrt{D}}{2CF\cdot\Gamma}\,, |  | (7) |

where Λ=C​F⋅(2​A​b​(1−γ)​(1+ℓ)−B​A)+θ​B​A​(1+ℓ)\Lambda=CF\cdot\bigl(2Ab(1-\gamma)(1+\ell)-BA\bigr)+\theta BA(1+\ell), Γ=B​(1−γ)​(1+ℓ)−b​(1−γ)2​(1+ℓ)2\Gamma=B(1-\gamma)(1+\ell)-b\,(1-\gamma)^{2}(1+\ell)^{2}
and D=Λ2+4​C​F⋅Γ​(C​F⋅b​A2−θ​B​A​c)D=\Lambda^{2}+4CF\cdot\Gamma\bigl(CF\cdot bA^{2}-\theta BAc\bigr).
  
In the optimization problem ([2](https://arxiv.org/html/2602.12104v1#S3.E2 "Equation 2 ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")), subject to C​F≥H​F​(c,b,A,B)CF\geq HF(c,b,A,B), the admissible search domain for xx is therefore

|  |  |  |
| --- | --- | --- |
|  | 0≤x≤min⁡{xc,xκ​b,xc​f},0\leq x\leq\min\{x\_{c},\;x\_{\kappa b},\;x\_{cf}\}\,, |  |

where the liquidation thresholds are taken as infinity if they involve division by 0.

###### Lemma 1.

Consider a lending protocol holding collateral cc and debt bb with closing factor C​FCF and liquidation threshold κ\kappa.
Consider, also, a CPMM with initial reserves (A,B)(A,B) in the collateral and debt assets, respectively.
The optimal profit ([2](https://arxiv.org/html/2602.12104v1#S3.E2 "Equation 2 ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) obtained by the liquidator is given as the output of Algorithm [1](https://arxiv.org/html/2602.12104v1#alg1 "Algorithm 1 ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees").
This profit is obtained by incrementally claiming and selling marginal d​xdx units of the collateral until the health factor equals C​FCF and then completing a final, finite sized, liquidation.

###### Proof.

Herein we provide a sketch of the logic. For the complete proof refer to Appendix [A.1](https://arxiv.org/html/2602.12104v1#A1.SS1 "A.1 Lemma 1 Proof ‣ Appendix A Proofs ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees").
First, we find that it is optimal for the liquidator to make sequential small liquidations over a single large liquidation. In this way the optimal strategy is to liquidate marginal d​xdx units of the collateral for as long as possible. Notably, this occurs up to whichever of the following conditions is met first: the collateral has been fully used (xcx\_{c}), the loan is fully repaid (xbx\_{b}), or the health factor has recovered up to C​FCF (xc​fx\_{cf}).
Because such liquidations occur at marginal size, we are able to find the total profits from this stage via the integral

|  |  |  |  |
| --- | --- | --- | --- |
|  | πl​i​q=∫0xl​i​q(B−y)​((1−γ)​(1+ℓ)−1)A+x​(1−γ)​(1+ℓ)​𝑑x=B​((1−γ)​(1+ℓ)−1)​xl​i​qA+xl​i​q​(1−γ)​(1+ℓ)\pi\_{liq}=\int\_{0}^{x\_{liq}}\frac{(B-y)((1-\gamma)(1+\ell)-1)}{A+x(1-\gamma)(1+\ell)}dx=\frac{B((1-\gamma)(1+\ell)-1)x\_{liq}}{A+\,x\_{liq}(1-\gamma)(1+\ell)} |  | (8) |

At this time, if further liquidations can be accomplished (i.e., xl​i​q=xc​fx\_{liq}=x\_{cf}), the liquidator makes one final large transaction chosen to either exhaust the remaining collateral (xc−xc​fx\_{c}-x\_{cf}), repay the maximum allowable fraction of the loan (xκ​bx\_{\kappa b}), or maximize total profitability (x∗x^{\*}).
∎

Algorithm 1  Liquidation Profit Dynamics L​(C​F,κ)L(CF,\kappa)

Input: AA (collateral amount in DEX), BB (debt amount in DEX), γ\gamma (transaction fee), bb (debt in LP), cc (collateral in LP), θ\theta (haircut rate), ℓ\ell (discount rate), C​FCF (closing factor), κ\kappa (max liquidation rate)
  
0. Compute: H​F​(c,b,A,B)=θ​B​cA​bHF(c,b,A,B)=\frac{\theta Bc}{Ab}, If H​F>C​FHF>CF or γ≤ℓ1+ℓ\gamma\leq\frac{\ell}{1+\ell} then Return: πtot=0\pi\_{\text{tot}}=0
  
1. Compute: xc=c1+ℓ,xb=b​AB−b​(1−γ)​(1+ℓ)x\_{c}=\frac{c}{1+\ell},\quad x\_{b}=\frac{bA}{B-b(1-\gamma)(1+\ell)}
  
2. Compute: xc​f=Λ+D2​C​F⋅Γ,x\_{cf}=\frac{\Lambda\,+\,\sqrt{D}}{2CF\cdot\,\Gamma},

|Λ=−C​F⋅(2​A​b​(1−γ)​(1+ℓ)−B​A)+θ​B​A​(1+ℓ)Γ=B​(1−γ)​(1+ℓ)−b​(1−γ)2​(1+ℓ)2D=Λ2+4​C​F⋅Γ​(C​F⋅b​A2−θ​B​A​c)\left|\begin{array}[]{l}\Lambda=-CF\cdot\bigl(2Ab\,(1-\gamma)(1+\ell)-BA\bigr)+\theta BA(1+\ell)\\
\Gamma=B\,(1-\gamma)(1+\ell)-b\,(1-\gamma)^{2}(1+\ell)^{2}\\
D=\Lambda^{2}+4CF\cdot\,\Gamma\bigl(CF\cdot\,bA^{2}-\theta BAc\bigr)\\
\end{array}\right.

3. Set: xliq=min⁡{xc,xb,xc​f}x\_{\text{liq}}=\min\{x\_{c},x\_{b},x\_{cf}\}
  
4. Compute: πliq=B​((1−γ)​(1+ℓ)−1)​xl​i​qA+xl​i​q​(1−γ)​(1+ℓ)\pi\_{\text{liq}}=\frac{B((1-\gamma)(1+\ell)-1)x\_{liq}}{A+x\_{liq}(1-\gamma)(1+\ell)}
  
5. If xc​f<min⁡{xc,xb}x\_{cf}<\min\{x\_{c},x\_{b}\}:

|yc​f=B​xc​f​(1−γ)​(1+ℓ)A+xc​f​(1−γ)​(1+ℓ)b¯=b−11+l​yc​fA¯=A+xc​f​(1−γ)​(1+ℓ),B¯=B−yc​fxκ​b=κ​b¯​A¯B¯−κ​b¯​(1−γ)​(1+ℓ)x∗=A¯​((1−γ)​(1+ℓ)−1)(1−γ)​(1+ℓ)xlast=min⁡{xc−xc​f,xκ​b,x∗}πlast=B¯​xl​a​s​t​(1+ℓ)​(1−γ)A¯+xl​a​s​t​(1−γ)​(1+ℓ)−B¯​xl​a​s​tA¯\left|\begin{array}[]{l}y\_{cf}=\frac{Bx\_{cf}(1-\gamma)(1+\ell)}{A+x\_{cf}(1-\gamma)(1+\ell)}\\
\bar{b}=b-\frac{1}{1+l}y\_{cf}\\
\bar{A}=A+x\_{cf}(1-\gamma)(1+\ell),\quad\bar{B}=B-y\_{cf}\\
x\_{\kappa b}=\frac{\kappa\bar{b}\bar{A}}{\bar{B}-\kappa\bar{b}(1-\gamma)(1+\ell)}\\
x^{\*}=\frac{\bar{A}(\sqrt{(1-\gamma)(1+\ell)}-1)}{(1-\gamma)(1+\ell)}\\
x\_{\text{last}}=\min\{x\_{c}-x\_{cf},x\_{\kappa b},x^{\*}\}\\
\pi\_{\text{last}}=\frac{\bar{B}x\_{last}(1+\ell)(1-\gamma)}{\bar{A}+x\_{last}(1-\gamma)(1+\ell)}-\frac{\bar{B}x\_{last}}{\bar{A}}\end{array}\right.

6. Else: πlast=0\pi\_{\text{last}}=0
  
7. Return: πtot=πliq+πlast\pi\_{\text{tot}}=\pi\_{\text{liq}}+\pi\_{\text{last}}

###### Remark 2.

When calculating the profit with transaction fees at the CPMM, it is possible that the liquidator is taking a loss due to the assessed fees. Notably, the only condition for the derivative of πl​i​q\pi\_{liq} to be zero is: (1−γ)​(1+ℓ)−1=0(1-\gamma)(1+\ell)-1=0. This means that if γ\gamma is too high compared to ℓ\ell, liquidators will never choose to enter the system and bad debt will proliferate.

### 3.2 Full Liquidation Event

The closing factor and maximum liquidation rate are parameters set by the lending platform. In order to determine the ultimate optimal profit, the optimal profit L​(C​Fi,κi)L(CF\_{i},\kappa\_{i}) across all potential threshold pairs (C​Fi,κi)(CF\_{i},\kappa\_{i}) should be evaluated, where i∈Ni\in N indexes the chosen discretizations of thresholds. That is, the maximum would be taken as maxi∈N⁡{L​(C​Fi,κi)}\max\_{i\in N}\{L(CF\_{i},\kappa\_{i})\}.
In fact, Aave (and major other LPs) use only two threshold pairs: (C​F,1)(CF,1) and (1,κ)(1,\kappa) for C​F,κ∈(0,1)CF,\kappa\in(0,1). Thus, for simplicity, herein we consider the maximum of the two outcomes, i.e., max⁡{L​(C​F,1),L​(1,κ)}\max\{L(CF,1),\,L(1,\kappa)\} as the realized profit.

Notably, there is a key trade-off between the two strategies. If the integral is stopped at a lower health factor, e.g., when the position crosses C​FCF, the liquidator is permitted to carry out a larger, final liquidation event in a single shot. In contrast, extending the liquidation sequence by continuing the integral under the κ\kappa constraint results in a longer stream of smaller profits. The final liquidation’s size is usually capped by κ\kappa, which determines the forced cutoff of the permitted liquidation amount. In other words, the liquidator must decide between a shorter horizon with a larger terminal gain or longer horizon with a capped end-payoff. Throughout the remainder of this section, we will explore these tradeoffs via numerical examples.

First, in Example [1](https://arxiv.org/html/2602.12104v1#Thmexample1 "Example 1. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), we study how price impact and market depth affect liquidation outcomes, demonstrating that deeper pools favor the L​(C​F,1)L(CF,1) liquidation strategy.
Second, we examine a fee-free setting in Example [2](https://arxiv.org/html/2602.12104v1#Thmexample2 "Example 2. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), to isolate the role of price dynamics, demonstrating how changes in the DEX price cause regime shifts in the binding liquidation constraint and produce nonlinear profit behavior as the dominant liquidation mechanism shifts. Third, in Example [3](https://arxiv.org/html/2602.12104v1#Thmexample3 "Example 3. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), we analyze how liquidation profitability changes across health factor regimes by looking at a fixed debt and collateral configuration and changing the underlying asset price.

###### Example 1.

Consider a CPMM with initial reserves of risky assets A′=1,000​sA^{\prime}=1{,}000s and stablecoins B′=2,000,000​sB^{\prime}=2{,}000{,}000s for s>0s>0 which charges a fee of γ=0.3%\gamma=0.3\%. For simplicity of notation, we take A0=1,000A\_{0}=1{,}000 and B0=2,000,000B\_{0}=2{,}000{,}000 for the remainder of this example; the factor s>0s>0 allows us to scale the DEX depth while maintaining the spot price at B0/A0=2,000B\_{0}/A\_{0}=2{,}000. Fix the lending position at b=10,000b=10{,}000 and the liquidation parameters to θ=85%\theta=85\%, ℓ=5%\ell=5\%, C​F=95%CF=95\%, and κ=50%\kappa=50\%. In order to ensure that liquidations can be triggered, the initial collateral level is selected as c=b​A0θ​B0−0.35c=\frac{bA\_{0}}{\theta B\_{0}}-0.35.

Under such a setting, we calculate the liquidation profits under two strategies for each value of ss: L​(C​F,1)L(CF,1), which represents liquidation that is terminated when the health factor recovers to the closing factor and then completed with a final liquidation, and L​(1,κ)L(1,\kappa), which permits liquidation to proceed up to the protocol-imposed fraction.

The L​(C​F,1)L(CF,1) strategy produces higher profit for the majority of pool depths, as shown in Figure [3](https://arxiv.org/html/2602.12104v1#S3.F3 "Figure 3 ‣ Example 1. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), and its advantage grows as the pool gets deeper.
Shallow pools, causing high slippage, result in liquidations that rapidly hit one of the binding constraints (xcx\_{c}, xκ​bx\_{\kappa b}, or xc​fx\_{cf}); because of this, the two strategies—L​(C​F,1)L(CF,1) and L​(1,κ)L(1,\kappa)—behave similarly and sometimes reverse their ordering.
We highlight that L​(C​F,1)L(CF,1) is non-monotonic in pool depth; this occurs as deeper pools reduce πl​i​q\pi\_{liq} as xc​fx\_{cf} is decreasing in pool depth (the decreasing price impacts reduce the length during which the infinitesimal liquidations can occur) while πl​a​s​t\pi\_{last} is increasing.
This explains the divergence seen in the figure and shows how market depth controls the relative optimality of liquidation strategies.

![Refer to caption](image/l_compare.png)


Figure 3: Example [1](https://arxiv.org/html/2602.12104v1#Thmexample1 "Example 1. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"): Comparison of liquidation profit under two liquidation strategies. The x-axis shows the depth of the pool and the y-axis indicates the total profit of the strategy.

###### Example 2.

To focus solely on the liquidation problem without considering details of the DEX, we consider the CPMM without any transaction fees, i.e., γ=0\gamma=0. In doing this, our goal is to example the relationship between liquidation profits and the asset prices as the initial health factor is varied.

Consider the CPMM with spot price p>0p>0 and liquidity A0​B0=K=2×109A\_{0}B\_{0}=K=2\times 10^{9}, i.e., A0=K/pA\_{0}=\sqrt{K/p} and B0=K​pB\_{0}=\sqrt{Kp}. Consider, the lending pool with fixed parameters θ=85%\theta=85\%, ℓ=5%\ell=5\%, C​F=80%CF=80\% and κ=50%\kappa=50\%. For an initial health factor ranging from H​F∈{50%,90%,92%,94%,99%}HF\in\{50\%,90\%,92\%,94\%,99\%\}, we consider b=10,000b=10,000 and c=H​F⋅b​A0θ​B0c=HF\cdot\frac{bA\_{0}}{\theta B\_{0}}. Herein we have found that the system behavior is qualitatively comparable for all health factors below 90%90\%, as such we consider H​F=50%HF=50\% as a representative setting.

![Refer to caption](image/k_mults_12.png)


Figure 4: Example [2](https://arxiv.org/html/2602.12104v1#Thmexample2 "Example 2. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"): Liquidation profit for different health factor levels

As seen in Figure [4](https://arxiv.org/html/2602.12104v1#S3.F4 "Figure 4 ‣ Example 2. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), the profit curves exhibit distinct breakpoints when the variable limiting the amount of liquidations changes. Recall that the available collateral in the lending platform, represented by xcx\_{c}, limits the amount that can be liquidated when the DEX price is low. As the price grows, the requirement to return the health factor to 1 (or to the closing factor C​FCF when H​F<C​FHF<CF) becomes binding for xliqx\_{\text{liq}}; that is, the collateral becomes adequate to support deeper liquidations. As a result, the profit function’s slope changes as it enters this new regime. At even higher prices, there is a second, more subtle transition; this is particularly noticeable in the H​F=99%HF=99\% case.
The πlast\pi\_{\text{last}} term captures this second transition, as, again, the liquidator moves from running through all available collateral leaving bad debt for the lending pool to closing out the maximum allowable debt. The decreasing profitability as prices increase results from the decreasing first-stage profits (πliq\pi\_{\text{liq}}). In fact, even though the final liquidation amount xlastx\_{\text{last}} is declining, πlast\pi\_{\text{last}} can actually start to rise with the larger initial price. The nonlinearity of πlast\pi\_{\text{last}} is the cause of this counterintuitive behavior: each unit becomes more profitable as less is being liquidated meaning the increase in per unit profit exceeds the decreasing liquidation size. Also, eventually, πlast\pi\_{\text{last}} starts to grow more quickly than πliq\pi\_{\text{liq}} decrease. Consequently, the total profit πtot\pi\_{\text{tot}} starts to increase once more for high enough prices.

###### Example 3.

In contrast to Example [2](https://arxiv.org/html/2602.12104v1#Thmexample2 "Example 2. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), we now explore what happens when the health factor is driven by the initial price at the CPMM. Consider the lending pool with debt b=10,000b=10,000 and collateral c=6c=6. The liquidations are driven by parameters θ=85%\theta=85\%, ℓ=5%\ell=5\%, C​F=80%CF=80\%, and κ=50%\kappa=50\%. Herein, we consider the CPMM with a fixed liquidity K=2×109K=2\times 10^{9} with A0=K/pA\_{0}=\sqrt{K/p} and B0=K​pB\_{0}=\sqrt{Kp} for p=H​F⋅bθ​cp=HF\cdot\frac{b}{\theta c}.
As can be seen in Figure [5](https://arxiv.org/html/2602.12104v1#S3.F5 "Figure 5 ‣ Example 3. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), the liquidation profit rises as prices do. The health factor declines when prices fall too low, leaving the lending platform with bad debt that is unrecoverable. Until the price hits 1756.76, the binding constraint on liquidation stays at xcx\_{c}. After that, it changes to xc​fx\_{cf}. The reason for the steep decline in profit around H​F=1HF=1 is that liquidation is prohibited once the health factor hits 1, which results in a zero profit.

![Refer to caption](image/nofee_nodelta.png)


Figure 5: Example [3](https://arxiv.org/html/2602.12104v1#Thmexample3 "Example 3. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"): Liquidation profit without sandwiching and transaction fees

## 4 Sandwich Attack of a Liquidation Event

Following the common practice in which liquidations are often executed through MEV relays and private transaction bundles, within this section we assume that the liquidator can influence transaction ordering within a block, i.e., get their transaction posted before anyone else tries. This liquidator’s goal is to push the collateral price downward to reduce the health factor in order to trigger liquidations, thus, increase profitability. Specifically, within a single block, the liquidator can insert a sequence of trades that: (1) drop the price of the collateral at the DEX; (2) complete the liquidations; and (3) reverse the initial selling pressure at this further depressed price to recover the initial holdings. Notably, such a MEV attack is possible because the liquidator can control their transaction orders and the DEX price can be deterministically predicted within the block.

Even if the initial health factor is above 1, the liquidator can strategically manipulate the price by selling collateral units into the DEX.
This sale depresses the collateral price and, if sufficiently large, can lower the health factor below the critical threshold to trigger liquidations on the lending platform.
Mathematically, and as highlighted in the simplified timeline in Figure [6](https://arxiv.org/html/2602.12104v1#S4.F6 "Figure 6 ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), assuming the initial DEX liquidity is (A0,B0)(A\_{0},B\_{0}), the attacker can sell Δ\Delta units of collateral to the DEX to update the DEX reserves (A1>A0A\_{1}>A\_{0} and B1<B0B\_{1}<B\_{0} in the collateral and debt assets, respectively).
Once the liquidation spiral unfolds (which causes the DEX to have updated collateral and debt asset reserves A2>A1A\_{2}>A\_{1} and B2<B1B\_{2}<B\_{1}), the liquidator can repurchase the previously sold collateral amount Δ\Delta at the new, lower price. This sandwich attack on the liquidation event results in profits in excess of the liquidation event itself as it effectively allows the liquidator to sell Δ\Delta high and buy it back low.

t = 0t = 1t = 2(A0A\_{0}, B0B\_{0})Sell Δ\Delta(A1A\_{1}, B1B\_{1})Liquidate(A2A\_{2}, B2B\_{2})Buy Δ\Delta


Figure 6: Sell, liquidate and buy back events

###### Remark 3.

Within the discussion herein, we ignore where the liquidator obtains the initial Δ\Delta collateral to be sold at the DEX to initiate the sandwich attack. Due to the requirement to close out the sandwich attack after the liquidation event is completed, this initial liquidity could be obtained from, e.g., a flash loan rather than requiring the attacker to have the necessary liquidity on their own.

Before considering the profits that can be obtained from this sandwich attack, we wish to consider the exact reserves of the CPMM at each stage of the attack. Recall, we assume that the initial CPMM reserves are (A0,B0)(A\_{0},B\_{0}) and the attack is of size Δ≥0\Delta\geq 0.
Following the constant product rule, after the initiation of the attack, the DEX reserves update to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A1​(Δ)\displaystyle A\_{1}(\Delta) | =A0+Δ​(1−γ)\displaystyle=A\_{0}+\Delta(1-\gamma) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B1​(Δ)\displaystyle B\_{1}(\Delta) | =A0​B0A0+Δ​(1−γ)\displaystyle=\frac{A\_{0}B\_{0}}{A\_{0}+\Delta(1-\gamma)} |  |

so that A1​(Δ)​B1​(Δ)=A0​B0A\_{1}(\Delta)B\_{1}(\Delta)=A\_{0}B\_{0}.
With these updated reserves, the liquidation process, following the optimal structure discussed in Section [3](https://arxiv.org/html/2602.12104v1#S3 "3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), will commence. Herein, we will simplify the discussion to assume that this process results in x≥0x\geq 0 of collateral being claimed by the attacking liquidator (not including the ℓ\ell bonus paid for completing the liquidation). This liquidation leads to the further, updated, DEX reserves:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A2​(Δ,x)\displaystyle A\_{2}(\Delta,x) | =A1​(Δ)+x​(1+ℓ)​(1−γ)=A0+Δ​(1−γ)+x​(1+ℓ)​(1−γ)\displaystyle=A\_{1}(\Delta)+x(1+\ell)(1-\gamma)=A\_{0}+\Delta(1-\gamma)+x(1+\ell)(1-\gamma) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B2​(Δ,x)\displaystyle B\_{2}(\Delta,x) | =A1​(Δ)​B1​(Δ)A1​(Δ)+x​(1+ℓ)​(1−γ)=A0​B0A0+Δ​(1−γ)+x​(1+ℓ)​(1−γ)\displaystyle=\frac{A\_{1}(\Delta)B\_{1}(\Delta)}{A\_{1}(\Delta)+x(1+\ell)(1-\gamma)}=\frac{A\_{0}B\_{0}}{A\_{0}+\Delta(1-\gamma)+x(1+\ell)(1-\gamma)} |  |

so that A2​(Δ,x)​B2​(Δ,x)=A1​(Δ)​B1​(Δ)=A0​B0A\_{2}(\Delta,x)B\_{2}(\Delta,x)=A\_{1}(\Delta)B\_{1}(\Delta)=A\_{0}B\_{0}.

In order to determine the true profitability of this full sandwich attack, we need to determine the cost of repurchasing Δ\Delta after the liquidation event has concluded. To ensure that the attacker is repurchasing exactly Δ\Delta, and following the CPMM construction, they must pay B2​(Δ,x)​Δ(1−γ)​(A2​(Δ,x)−Δ)\frac{B\_{2}(\Delta,x)\Delta}{(1-\gamma)(A\_{2}(\Delta,x)-\Delta)}.
In this way, we can write the MEV-based optimization problem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | maxΔ≥0⁡[B0​Δ​(1−γ)A0+Δ​(1−γ)+V​(c,b,A1​(Δ),B1​(Δ))−B2​(Δ,x)​Δ(1−γ)​(A2​(Δ,x)−Δ)]\displaystyle\max\_{\Delta\geq 0}\bigg[\frac{B\_{0}\Delta(1-\gamma)}{A\_{0}+\Delta(1-\gamma)}+V(c,b,A\_{1}(\Delta),B\_{1}(\Delta))-\frac{B\_{2}(\Delta,x)\Delta}{(1-\gamma)(A\_{2}(\Delta,x)-\Delta)}\bigg] |  | (9) |

where VV is as in ([2](https://arxiv.org/html/2602.12104v1#S3.E2 "Equation 2 ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) while the difference between the first and last terms correspond to the profits purely from the sandwich attack on the liquidation event. Recall that xx denotes the optimal amount of collateral claimed (not including the ℓ\ell bonus) as part of the liquidation procedure; in this way, implicitly, xx is also a function of Δ\Delta within this optimal MEV attack problem.
Notably, this maximization takes into consideration the effect on future liquidation opportunities when determining the ideal amount Δ\Delta to trade in the DEX for MEV profits.

###### Remark 4.

While ([9](https://arxiv.org/html/2602.12104v1#S4.E9 "Equation 9 ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) is written to optimize over Δ≥0\Delta\geq 0, we may wish to consider upper and lower bounds on Δ\Delta.
First, the MEV attacker implicitly needs to make the initial liquidation large enough to push the health factor of the loan below 1 to trigger any possibility of profits, i.e.,

|  |  |  |
| --- | --- | --- |
|  | Δ≥max⁡{0,θ​c​A0​B0b−A01−γ}.\Delta\geq\max\left\{0\;,\;\frac{\sqrt{\frac{\theta cA\_{0}B\_{0}}{b}}-A\_{0}}{1-\gamma}\right\}. |  |

Second, for system robustness, we may impose a constraint so that the DEX holds enough reserves B1​(Δ)B\_{1}(\Delta) to cover the debt bb at the LP, i.e.,

|  |  |  |
| --- | --- | --- |
|  | Δ≤A0​B0b​(1−γ)2​(1+ℓ)−A01−γ.\Delta\leq\frac{A\_{0}B\_{0}}{b(1-\gamma)^{2}(1+\ell)}-\frac{A\_{0}}{1-\gamma}. |  |

If Δ\Delta exceeds this cap, then any debt that cannot be liquidated would count as *bad debt* which results in losses for the lenders.666Implicitly, we are assuming the CPMM is the only market at which the collateral can be sold.

###### Example 4.

Herein we wish to explore a simple example in which the LP has an initial health factor greater than 1. In this way, without the MEV attack, no liquidation event would be triggered. Thus, to make a profit, the liquidator will need to lower the market price of the collateral by selling some of it into the CPMM in order to start the liquidation spiral. All system parameters are as in Example [3](https://arxiv.org/html/2602.12104v1#Thmexample3 "Example 3. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees").

Rather than directly solving ([9](https://arxiv.org/html/2602.12104v1#S4.E9 "Equation 9 ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")), in Figure [7](https://arxiv.org/html/2602.12104v1#S4.F7 "Figure 7 ‣ Example 4. ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), we plot the profits earned by the liquidators as a function of the attack size Δ\Delta.
Notably, the profits are initially zero when Δ\Delta is low because the health factor remains above 1 and no liquidations are triggered. However, as the attack size grows, profits jump up at the moment that the attack drives the health factor to 1 as seen at the dashed red line in the plot. From this point, the total profits earned by the attacker are monotonically increasing as a function of the attack size Δ\Delta. Though the total profits continue to grow, the profitability of the liquidation itself begins to drop as a function of the attack size as the liquidation amounts moves from xc​fx\_{cf} and xlastx\_{\text{last}} to xcx\_{c}, i.e., where all collateral is liquidated so the lower prices merely decrease the profits earned from selling that collateral.

We wish to note that the non-monotonicity of the liquidation profits correspond to what was observed in Figure [5](https://arxiv.org/html/2602.12104v1#S3.F5 "Figure 5 ‣ Example 3. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") (Example [3](https://arxiv.org/html/2602.12104v1#Thmexample3 "Example 3. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")). In that example, we considered how liquidation profits were a function of the initial price; herein, that initial price is a decreasing function of Δ\Delta. Therefore, the same profit dynamics as in Figure [5](https://arxiv.org/html/2602.12104v1#S3.F5 "Figure 5 ‣ Example 3. ‣ 3.2 Full Liquidation Event ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") can be seen if we read Figure [7](https://arxiv.org/html/2602.12104v1#S4.F7 "Figure 7 ‣ Example 4. ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") from right to left.

![Refer to caption](image/front_nofee.png)


Figure 7: Example [4](https://arxiv.org/html/2602.12104v1#Thmexample4 "Example 4. ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"): Profit with sandwiching and no transaction fees

### 4.1 Limiting Behavior

As seen in Example [4](https://arxiv.org/html/2602.12104v1#Thmexample4 "Example 4. ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), the liquidator’s profits are strictly increasing in the size of the attack. With this intuition, it is tempting to think that the optimal behavior ([9](https://arxiv.org/html/2602.12104v1#S4.E9 "Equation 9 ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) is always to liquidate as much as possible.
Within this section, we will investigate the result of that maximally sized attack Δm​a​x\Delta\_{max} to demonstrate that this is not only wrong, but the worst possible situation when the DEX has a non-zero fee rate γ>0\gamma>0.

First, in order to determine the profitability under the maximally sized attack Δm​a​x\Delta\_{max} we need to determine its size. Specifically, when attempting to close the attack (e.g., to repay the flash loan used to initiate the sandwich attack so as to not revert the transaction), the DEX needs to have sufficient liquidity in order to allow for this purchase, i.e., A2​(Δ,x)≥ΔA\_{2}(\Delta,x)\geq\Delta. Because of the fees γ\gamma charged at the DEX, in Proposition [2](https://arxiv.org/html/2602.12104v1#Thmtheorem2 "Proposition 2. ‣ 4.1 Limiting Behavior ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") below, we find the maximal feasible attack size. Note that the attack size Δ=A2​(Δ,x)\Delta=A\_{2}(\Delta,x) depends on the realized liquidation event xx; because we are following the situation in which the sandwich attack is of significant size, we simplify to consider x=xcx=x\_{c}, i.e., all collateral is liquidated in the event.

###### Proposition 2.

An attack Δ≥0\Delta\geq 0 is feasible without reversion (i.e., A2​(Δ,xc)≥ΔA\_{2}(\Delta,x\_{c})\geq\Delta) if and only if Δ≤Δm​a​x\Delta\leq\Delta\_{max} where

|  |  |  |
| --- | --- | --- |
|  | Δm​a​x={+∞if ​γ=0A0+(1−γ)​cγ,if ​γ>0.\Delta\_{max}=\begin{cases}+\infty&\text{if }\gamma=0\\ \frac{A\_{0}+(1-\gamma)c}{\gamma},&\text{if }\gamma>0.\end{cases} |  |

###### Proof.

The first swap in the attack increases the DEX’s collateral by (1−γ)​Δ(1-\gamma)\Delta units. In the large attack regime under consideration, the liquidation contributes an extra (1−γ)​xc​(1+ℓ)=(1−γ)​c(1-\gamma)x\_{c}(1+\ell)=(1-\gamma)c units of collateral to the DEX after exhausting the borrower’s collateral constraint, i.e., x=xc=c1+ℓx=x\_{c}=\frac{c}{1+\ell}. Hence the post-liquidation collateral reserve is

|  |  |  |
| --- | --- | --- |
|  | A2​(Δ,xc)=A0+(1−γ)​Δ+(1−γ)​c.A\_{2}(\Delta,x\_{c})=A\_{0}+(1-\gamma)\Delta+(1-\gamma)c\,. |  |

The ability of the attacker to repurchase Δ\Delta units of collateral, i.e., A2​(Δ,xc)≥ΔA\_{2}(\Delta,x\_{c})\geq\Delta or equivalently

|  |  |  |
| --- | --- | --- |
|  | A0+(1−γ)​Δ+(1−γ)​c≥Δ↔A0+(1−γ)​c≥γ​ΔA\_{0}+(1-\gamma)\Delta+(1-\gamma)c\;\geq\;\Delta\quad\leftrightarrow\quad A\_{0}+(1-\gamma)c\;\geq\;\gamma\Delta |  |

is necessary for the attack to be feasible.
This results in Δ≤A0+(1−γ)​cγ\Delta\leq\frac{A\_{0}+(1-\gamma)c}{\gamma} if γ>0\gamma>0. The inequality reduces to A0+c≥0A\_{0}+c\geq 0 if γ=0\gamma=0, which holds trivially for A0,c≥0A\_{0},c\geq 0, i.e., Δ\Delta is unbounded.
∎

###### Remark 5.

In Proposition [2](https://arxiv.org/html/2602.12104v1#Thmtheorem2 "Proposition 2. ‣ 4.1 Limiting Behavior ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), we implicitly assume x=xc=c/(1+ℓ)x=x\_{c}=c/(1+\ell) from the optimal liquidation after the attack Δ\Delta has commenced. Intuitively, in the large-attack regime in which the price is sufficiently low, the health factor constraint (xc​fx\_{cf}) becomes exceedingly large as recovering the health factor of 1 becomes a near impossibility. Similarly, when the collateral price is low, even ignoring price impacts, the ability to repay the loan bb requires a large amount of collateral (xbx\_{b}). This leaves the only remaining constraint to be that based on the total amount of collateral in the LP (xcx\_{c}).

With this maximal attack size, the goal is to determine the profits that result from such an attack. This profit *and loss* is provided in Proposition [3](https://arxiv.org/html/2602.12104v1#Thmtheorem3 "Proposition 3. ‣ 4.1 Limiting Behavior ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"). Notably, while the case in which the DEX charges no fees (γ=0\gamma=0) behaves as seen in Example [4](https://arxiv.org/html/2602.12104v1#Thmexample4 "Example 4. ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") (i.e., larger attacks lead to larger profits), a large attack can generate infinite losses for the attacker when DEX fees are introduced (γ>0\gamma>0).

###### Proposition 3.

The limiting profitability when Δ↗Δm​a​x\Delta\nearrow\Delta\_{max} is provided by:

* •

  If γ=0\gamma=0: The liquidation value of the collateral cc, i.e., B0​cA0+c\frac{B\_{0}c}{A\_{0}+c}.
* •

  If γ>0\gamma>0: Infinite losses, i.e., −∞-\infty.

###### Proof.

In ([9](https://arxiv.org/html/2602.12104v1#S4.E9 "Equation 9 ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")), we examine the limiting profit as Δ↗Δmax\Delta\nearrow\Delta\_{\max}, differentiating between γ=0\gamma=0 and γ>0\gamma>0.

Case γ=0\gamma=0.
When γ=0\gamma=0, we have Δmax=+∞\Delta\_{\max}=+\infty per Proposition [2](https://arxiv.org/html/2602.12104v1#Thmtheorem2 "Proposition 2. ‣ 4.1 Limiting Behavior ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"). The first term in ([9](https://arxiv.org/html/2602.12104v1#S4.E9 "Equation 9 ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) satisfies

|  |  |  |
| --- | --- | --- |
|  | limΔ→∞B0​ΔA0+Δ=B0.\lim\_{\Delta\to\infty}\frac{B\_{0}\Delta}{A\_{0}+\Delta}=B\_{0}. |  |

The continuation value fades since B1​(Δ)=A0​B0A0+Δ→0B\_{1}(\Delta)=\frac{A\_{0}B\_{0}}{A\_{0}+\Delta}\to 0, implying
limΔ→∞V​(c,b,A1​(Δ),B1​(Δ))=0.\lim\_{\Delta\to\infty}V(c,b,A\_{1}(\Delta),B\_{1}(\Delta))=0.
The final term converges to

|  |  |  |
| --- | --- | --- |
|  | limΔ→∞(A0​B0A0+Δ+x​(1+ℓ))​ΔA0+x​(1+ℓ)=A0​B0A0+c,\lim\_{\Delta\to\infty}\frac{\left(\frac{A\_{0}B\_{0}}{A\_{0}+\Delta+x(1+\ell)}\right)\Delta}{A\_{0}+x(1+\ell)}=\frac{A\_{0}B\_{0}}{A\_{0}+c}, |  |

where we use x=xc=c1+ℓx=x\_{c}=\frac{c}{1+\ell}. Thus, limΔ→∞π​(Δ)=B0​cA0+c.\lim\_{\Delta\to\infty}\pi(\Delta)=\frac{B\_{0}c}{A\_{0}+c}.

Case γ>0\gamma>0.
When γ>0\gamma>0, Proposition [2](https://arxiv.org/html/2602.12104v1#Thmtheorem2 "Proposition 2. ‣ 4.1 Limiting Behavior ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") implies

|  |  |  |
| --- | --- | --- |
|  | Δmax=A0+(1−γ)​cγ.\Delta\_{\max}=\frac{A\_{0}+(1-\gamma)c}{\gamma}. |  |

As Δ↗Δmax\Delta\nearrow\Delta\_{\max}, we have A2​(Δ,xc)−Δ→0A\_{2}(\Delta,x\_{c})-\Delta\to 0, and therefore

|  |  |  |
| --- | --- | --- |
|  | B2​(Δ,x)​Δ(1−γ)​(A2​(Δ,x)−Δ)→+∞.\frac{B\_{2}(\Delta,x)\Delta}{(1-\gamma)(A\_{2}(\Delta,x)-\Delta)}\to+\infty. |  |

Since this term enters the objective with a negative sign (while all other terms are bounded), the total profit diverges to −∞-\infty.
∎

### 4.2 Fees as Oracle Protection

It follows from Proposition [3](https://arxiv.org/html/2602.12104v1#Thmtheorem3 "Proposition 3. ‣ 4.1 Limiting Behavior ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") that the attacker may need to restrict the attack’s scope rather than always carrying out a naive, large attack. Within this section, we consider a numerical example to demonstrate how fees of the DEX oracle, can prevent profitable manipulations to the spot price.

###### Example 5.

Consider a joint CPMM and LP system. Herein, we take the CPMM with initial reserves A0=10,000A\_{0}=10{,}000 and B0=28,000,000B\_{0}=28{,}000{,}000 in the collateral asset and stablecoin, respectively. In addition, to match the fees charged at Uniswap v2, we consider γ=0.3%\gamma=0.3\%. Consider the LP with θ=85%\theta=85\%, ℓ=5%\ell=5\%, C​F=80%CF=80\% and κ=50%\kappa=50\%. Finally, consider the situation in which b=32,000b=32{,}000 stablecoins were borrowed with c=20.12c=20.12 of collateral. These values were selected to reflect realistic pool depths and borrower positions.

The profitability of an attack, as a function of the attack size Δ\Delta, is provided in Figure [8](https://arxiv.org/html/2602.12104v1#S4.F8 "Figure 8 ‣ Example 5. ‣ 4.2 Fees as Oracle Protection ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"). Similar to the earlier examples, we consider both the total profits and loss as well as the profits that are derived directly from the liquidation event. Notably, these transaction fees clearly change the strategy’s profitability; for instance, without fees (γ=0\gamma=0), the total profits would be non-negative and non-decreasing as in, e.g., Figure [7](https://arxiv.org/html/2602.12104v1#S4.F7 "Figure 7 ‣ Example 4. ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"). Importantly, the overall profit is negative for all positive values of Δ>0\Delta>0 even though the liquidation profits still reflect the same regime changes discussed in Example [4](https://arxiv.org/html/2602.12104v1#Thmexample4 "Example 4. ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"); that is, once the health factor falls below 1, the liquidation component jumps to a positive value. This effect, in which the attacker takes losses even with the jump in profits at the health factor of 1, deters any such attack.

![Refer to caption](image/fee30_delta.png)


Figure 8: Example [5](https://arxiv.org/html/2602.12104v1#Thmexample5 "Example 5. ‣ 4.2 Fees as Oracle Protection ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"): Profit with 30 bps transaction fees and sandwiching

Consider the case in which we vary the CPMM fees γ\gamma. As expected, and shown in Figure [9](https://arxiv.org/html/2602.12104v1#S4.F9 "Figure 9 ‣ Example 5. ‣ 4.2 Fees as Oracle Protection ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"), the total profits extracted by the attack are decreasing in the fees charged. Though a small fee (e.g., γ=0.1%\gamma=0.1\%) may still present a profitable sandwiching opportunity for Δ\Delta within a bounded range, raising this fee to γ>γ∗:=0.17%\gamma>\gamma^{\*}:=0.17\% completely eliminates the profitability. This demonstrates how transaction fees work as a deterrent to sandwiching because those costs eliminate the economic incentives of the DEX oracle manipulation. That is, the DEX fees serve as a mechanism which promote market stability.

![Refer to caption](image/fee_star.png)


Figure 9: Example [5](https://arxiv.org/html/2602.12104v1#Thmexample5 "Example 5. ‣ 4.2 Fees as Oracle Protection ‣ 4 Sandwich Attack of a Liquidation Event ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees"): Total profit as a function of liquidation size Δ\Delta for different fee levels γ\gamma. The black curve corresponds to the critical threshold γ∗=17\gamma^{\*}=17 bps.

## 5 Discussion

In order to prevent short-term price manipulation, lending protocols frequently use hardened oracle mechanisms, such as time-weighted averages (TWAPs), medianized prices, or off-chain price feeds. These methods add latency even though they strengthen resistance against transient attacks. Oracle updates that are delayed during sharp market declines may underestimate risk and delay required liquidations, which raises the possibility of bad debt accumulation. In these systems, responsiveness is sacrificed for robustness.

Our findings show that this trade-off is not inevitable. By removing the latency that comes with averaging or off-chain methods, we demonstrate that AMM spot prices can function as practical, fully on-chain oracles. Lending protocols can achieve immediate responsiveness to market movements while preserving solvency during steep price declines by exclusively depending on intra-block DEX prices. This method maintains the blockchain environment’s transparency while eliminating reliance on outside data sources.

Importantly, we prove that transaction fees enable this design in two ways. Fees essentially change the incentives for manipulation in addition to rewarding liquidity providers and increasing market liquidity. Unlike previous works (e.g., cohen23) that assume frictionless AMMs, we demonstrate that the profitability of oracle manipulation attacks can be completely eliminated by setting DEX fees high enough. Fees act as a “win-win” design lever in this way, rewarding liquidity provision while fortifying the oracle against predatory MEV tactics. Robustness arises naturally from appropriately aligned market incentives rather than needing external protections.

Crucially, our results serve as a cautious standard for oracle security. The model assumes access to free flash loans and abstracts away operational frictions like gas prices. We give an upper bound on the profitability of a manipulative attacker by disregarding these costs. The robustness of fully on-chain AMM oracles is probably stronger than our theoretical estimates indicate, as the inclusion of gas fees and execution frictions would further compress manipulation incentives in practice.

## References

## Appendix A Proofs

### A.1 Lemma [1](https://arxiv.org/html/2602.12104v1#Thmtheorem1 "Lemma 1. ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees") Proof

There are two conditions that should be checked in order for the value function in ([2](https://arxiv.org/html/2602.12104v1#S3.E2 "Equation 2 ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) to be the sum of the two profit functions, i.e., step (7) in Algorithm [1](https://arxiv.org/html/2602.12104v1#alg1 "Algorithm 1 ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees").

* •

  Profit subadditivity:

  |  |  |  |
  | --- | --- | --- |
  |  | πl​i​q​(x1+x2)≤πl​i​q​(x1)+πl​i​q​(x2;x1)\displaystyle\pi\_{liq}(x\_{1}+x\_{2})\leq\pi\_{liq}(x\_{1})+\pi\_{liq}(x\_{2};x\_{1}) |  |

  where the notation x2;x1x\_{2};x\_{1} means using the value x2x\_{2} starting from x1x\_{1}.
* •

  Health factor constraint:

  |  |  |  |
  | --- | --- | --- |
  |  | H​F​(x1+x2)≥H​F​(x2;x1)\displaystyle HF(x\_{1}+x\_{2})\geq HF(x\_{2};x\_{1}) |  |
  |  |  |  |
  | --- | --- | --- |
  |  | s.t.H​F​(x1)≤C​F\displaystyle\text{s.t.}\quad HF(x\_{1})\leq CF |  |

  As based on the profit subadditivity condition we realized that smaller transactions are better, they also should be able to increase the HF at a slower rate (up to C​FCF), so that we will have more opportunities to liquidate. Hence, based on ([1](https://arxiv.org/html/2602.12104v1#S2.E1 "Equation 1 ‣ 2.1 Lending Protocols ‣ 2 Background ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | H​F​(x1+x2)\displaystyle HF(x\_{1}+x\_{2}) | =θ​(c−(x1+x2)​(1+ℓ))​B1A1b−(x1+x2)​B0A0\displaystyle=\frac{\theta(c-(x\_{1}+x\_{2})(1+\ell))\frac{B\_{1}}{A\_{1}}}{b-(x\_{1}+x\_{2})\frac{B\_{0}}{A\_{0}}} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | H​F​(x2;x1)\displaystyle HF(x\_{2};x\_{1}) | =θ​(c−x1​(1+ℓ)−x2​(1+ℓ))​B2A2b−x1​B0A0−x2​B1A1\displaystyle=\frac{\theta(c-x\_{1}(1+\ell)-x\_{2}(1+\ell))\frac{B\_{2}}{A\_{2}}}{b-x\_{1}\frac{B\_{0}}{A\_{0}}-x\_{2}\frac{B\_{1}}{A\_{1}}} |  |

  As B0A0≥B1A1≥B2A2\frac{B\_{0}}{A\_{0}}\geq\frac{B\_{1}}{A\_{1}}\geq\frac{B\_{2}}{A\_{2}}, the denominator of H​F​(x2;x1)HF(x\_{2};x\_{1}) is larger than H​F​(x1+x2)HF(x\_{1}+x\_{2}) and the numerator smaller, making the inequality to hold.

As highlighted above, the optimal liquidation strategy is to incrementally claim and sell marginal d​xdx units of the collateral. A question that might rise is if liquidating all at once would yield a higher profit. If we liquidate all in one transaction, the profit is as:

|  |  |  |
| --- | --- | --- |
|  | πo​n​e=B​x​(1+ℓ)​(1−γ)A+x​(1+ℓ)​(1−γ)−B​xA\displaystyle\pi\_{one}=\frac{Bx(1+\ell)(1-\gamma)}{A+x(1+\ell)(1-\gamma)}-\frac{Bx}{A} |  |

If we liquidate by incrementally small amounts, each transaction’s value is calculated by multiplying the quantity sold by the execution price. The relevant value for the transaction is based on the updated price after selling up to xx, or at the price using B−yB-y, where yy is obtained from ([3](https://arxiv.org/html/2602.12104v1#S3.E3 "Equation 3 ‣ Remark 1. ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")), rather than the initial price BB because every sale lowers the price. Consequently, B−yA+x​(1−γ)​(1+ℓ)\frac{B-y}{A+x(1-\gamma)(1+\ell)} is used as the price per unit at that point in time to determine the value of the subsequent small transaction d​xdx:

|  |  |  |
| --- | --- | --- |
|  | (B−y)​d​x​(1+ℓ)​(1−γ)A+x​(1+ℓ)​(1−γ)+d​x​(1+ℓ)​(1−γ)−(B−y)​d​xA+x​(1+ℓ)​(1−γ)\displaystyle\frac{(B-y)dx(1+\ell)(1-\gamma)}{A+x(1+\ell)(1-\gamma)+dx(1+\ell)(1-\gamma)}-\frac{(B-y)dx}{A+x(1+\ell)(1-\gamma)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =(B−y)​d​x​((1+ℓ)​(1−γ)−1)A+x​(1+ℓ)​(1−γ)\displaystyle=\frac{(B-y)dx((1+\ell)(1-\gamma)-1)}{A+x(1+\ell)(1-\gamma)} |  | (10) |

The total profit from these liquidations then would be the integral up to xl​i​qx\_{liq}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πl​i​q=∫0xl​i​q\displaystyle\pi\_{liq}=\int\_{0}^{x\_{liq}} | (B−y)​((1−γ)​(1+ℓ)−1)A+x​(1−γ)​(1+ℓ)​d​x\displaystyle\frac{(B-y)((1-\gamma)(1+\ell)-1)}{A+x(1-\gamma)(1+\ell)}dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =B​((1−γ)​(1+ℓ)−1)​xl​i​qA+xl​i​q​(1−γ)​(1+ℓ)\displaystyle=\frac{B((1-\gamma)(1+\ell)-1)x\_{liq}}{A+x\_{liq}(1-\gamma)(1+\ell)} |  | (11) |

where xl​i​q=min⁡{xc,xb,xc​f}x\_{liq}=\min\{x\_{c},x\_{b},x\_{cf}\} and xcx\_{c} and xbx\_{b} can be obtained from ([5](https://arxiv.org/html/2602.12104v1#S3.E5 "Equation 5 ‣ Remark 1. ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) and ([6](https://arxiv.org/html/2602.12104v1#S3.E6 "Equation 6 ‣ Remark 1. ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")) with κ=1\kappa=1 respectively and xc​fx\_{cf} is detailed in ([7](https://arxiv.org/html/2602.12104v1#S3.E7 "Equation 7 ‣ Remark 1. ‣ 3.1 Single Threshold Health Factor ‣ 3 Optimal Liquidation at Lending Protocols ‣ Liquidation Dynamics in DeFi and the Role of Transaction Fees")).

To test which one has a higher profit, we compare the profit from the liquidation types (πl​i​q,vs.​πo​n​e\pi\_{liq},\text{vs.}\,\pi\_{one}). Note that, for any x≥0x\geq 0:

|  |  |  |
| --- | --- | --- |
|  | B​((1−γ)​(1+ℓ)−1)​xA+x​(1−γ)​(1+ℓ)=B​x​(1+ℓ)​(1−γ)A+x​(1+ℓ)​(1−γ)−B​xA+x​(1+ℓ)​(1−γ)≥B​x​(1+ℓ)​(1−γ)A+x​(1+ℓ)​(1−γ)−B​xA\frac{B((1-\gamma)(1+\ell)-1)x}{A+x(1-\gamma)(1+\ell)}=\frac{Bx(1+\ell)(1-\gamma)}{A+x(1+\ell)(1-\gamma)}-\frac{Bx}{A+x(1+\ell)(1-\gamma)}\geq\frac{Bx(1+\ell)(1-\gamma)}{A+x(1+\ell)(1-\gamma)}-\frac{Bx}{A} |  |

This means liquidating by smaller transactions is more profitable.