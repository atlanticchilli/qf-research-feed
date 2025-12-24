---
authors:
- Anastasiia Zbandut
doc_id: arxiv:2512.20190v1
family_id: arxiv:2512.20190
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Pricing of wrapped Bitcoin and Ethereum on-chain options
url_abs: http://arxiv.org/abs/2512.20190v1
url_html: https://arxiv.org/html/2512.20190v1
venue: arXiv q-fin
version: 1
year: 2025
---


\fnmAnastasiia \surZbandut

###### Abstract

This paper measures price differences between Hegic option quotes on Arbitrum and a model-based benchmark built on Black–Scholes model with regime-sensitive volatility estimated via a two-regime MS-AR-(GJR)-GARCH model. Using option-level feasible GLS, we find benchmark prices exceed Hegic quotes on average, especially for call options. The price spread rises with order size, strike, maturity, and estimated volatility, and falls with trading volume. By underlying, wrapped Bitcoin options show larger and more persistent spreads, while Ethereum options are closer to the benchmark. The framework offers a data-driven analysis for monitoring and calibrating on-chain option pricing logic.

###### keywords:

decentralized finance, on-chain protocols, automated market maker, options

###### pacs:

[

JEL Classification]G12, G13, G15, G17

## 1 Introduction

Over the past few years, automated market makers (AMMs) have expanded from spot trading to perpetuals and, most recently, to options. They are core of decentralized finance (DeFi) because they replace the traditional order‐book with a programmatic pricing rule backed by pooled liquidity.
In centralized finance (CeFi), a centralized exchange discovers prices via a limit order book, holds client assets in custody, and relies on off-chain clearing and risk management [[38](https://arxiv.org/html/2512.20190v1#bib.bib38)]. In DeFi, these functions are implemented in code where smart contracts hold collateral, compute quotes according to an AMM formula, manage oracles and validators sustain liveness on the blockchain [[22](https://arxiv.org/html/2512.20190v1#bib.bib22), [46](https://arxiv.org/html/2512.20190v1#bib.bib46), [39](https://arxiv.org/html/2512.20190v1#bib.bib39), [20](https://arxiv.org/html/2512.20190v1#bib.bib20)].
Consequently, on-chain option prices are determined algorithmically by four components: (i) the AMM pricing rule and its parameters, (ii) the liquidity pool’s inventory and utilization, (iii) the oracle’s reference index and update frequency, and (iv) protocol fees together with throughput constraints [[44](https://arxiv.org/html/2512.20190v1#bib.bib44), [37](https://arxiv.org/html/2512.20190v1#bib.bib37)].

The four components above map directly to the main frictions of on-chain pricing. First, the AMM pricing rule and its parameters include denomination and settlement choices, which change payoff curvature and can introduce basis risk even when the spot market is liquid [[4](https://arxiv.org/html/2512.20190v1#bib.bib4)]. Second, the liquidity pool’s inventory and utilization matter because pooled capital must warehouse option convexity under full collateralization. Moreover, near-instant settlement at block finality reduces netting benefits and can raise funding needs relative to traditional clearing [[37](https://arxiv.org/html/2512.20190v1#bib.bib37)]. Third, the oracle’s reference index and update frequency create timing risk. Threshold updates and latency can open short-term spreads to reference prices. Prior feasibility studies and live oracle analyses show that liveness and data delivery are first-order concerns [[44](https://arxiv.org/html/2512.20190v1#bib.bib44), [20](https://arxiv.org/html/2512.20190v1#bib.bib20)].
Fourth, protocol fees and throughput constraints (block capacity) limit how quickly the protocol can update quotes or adjust hedges [[20](https://arxiv.org/html/2512.20190v1#bib.bib20)]. This speed limit matters more for options as their convex payoffs make values very sensitive to volatility. In cryptocurrency markets, the effect is amplified because Bitcoin (BTC) and Ethereum (ETH) returns feature jumps, regime shifts, heavy tails, and persistence. A pricing rule that omits these features can misstate volatility and distort option values [[16](https://arxiv.org/html/2512.20190v1#bib.bib16), [12](https://arxiv.org/html/2512.20190v1#bib.bib12), [50](https://arxiv.org/html/2512.20190v1#bib.bib50), [32](https://arxiv.org/html/2512.20190v1#bib.bib32), [36](https://arxiv.org/html/2512.20190v1#bib.bib36)].

Together, these four components describe how the smart contract sets the quote. We compare those quotes with a benchmark price, i.e., the Black–Scholes (BS) price computed with a regime-sensitive volatility estimate. This benchmark is a model-based reference, not the unobservable “true” price. Deviations from it can arise for two reasons. First, residual benchmark model risk, e.g., jump risk a volatility proxy does not fully capture. Second, economically justified AMM compensation for design and operating constraints, e.g., denomination/settlement basis or oracle timing risk. We mitigate the first source by focusing on short maturities and by using regime-sensitive volatility, therefore, the remaining patterns are informative about the second source.
This interpretation has two practical implications. If deviations are systematic along order size, moneyness, maturity, volatility, and liquidity depth (and economically large) they point to concrete calibration targets for the AMM. If deviations are persistent and hedgeable after costs with feasible instruments, they may also indicate potential arbitrage in principle. Our goal, however, is diagnosis and guidance for protocol tuning rather than proposing a trading strategy. In this way, the study informs both the empirical assessment of on-chain option pricing and the design of option-AMM pricing rules.

This paper studies Hegic protocol on Arbitrum chain by using data for wrapped Bitcoin (wBTC) and ETH options from October 24, 2022 to May 21, 2024. Purely on-chain, AMM-based option protocols remain rare and the segment is still small. At the moment of writing, according to [[19](https://arxiv.org/html/2512.20190v1#bib.bib19)], total value locked (TVL) in DeFi option protocols is about $100 million where Hegic accounts for $28.5 million and is the largest options protocol. Hegic is launched on both ETH and Arbitrum blockchains and with respect of it’s TVL, about $1.7 million is on ETH and $25.3 million on Arbitrum, which indicates that most activity occurs on Arbitrum. This concentration motivates the focus on the Arbitrum chain. Hegic is a long-only, pooled-liquidity protocol that offers American-style call and put options on a discrete strike–maturity grid and prices via a rate-based rule. On the contrary, other on-chain option protocols, Lyra/Derive and Deri implement BS–style AMM logic driven by oracle inputs and, for Lyra/Derive, an implied volatility (IV) surface. This design difference makes Hegic an informative case for evaluating how an AMM’s pricing rule maps into observed quotes relative to a benchmark BS valuation, and along which variables, i.e., order size, moneyness, maturity, volatility, liquidity depth, the mispricing is most pronounced.

We construct a model-based benchmark valuation by applying the BS model with a regime-sensitive estimate of the underlying volatility, consistent with the nature of cryptocurrency returns (heavy tails, volatility clustering, and regime shifts).
Specifically, we estimate a two–regime MS–AR–(GJR)–GARCH model for the underlying asset. The Markov component accommodates structural breaks and persistence documented for BTC and ETH, while the GJR term captures asymmetric volatility responses within regimes [[16](https://arxiv.org/html/2512.20190v1#bib.bib16), [12](https://arxiv.org/html/2512.20190v1#bib.bib12), [50](https://arxiv.org/html/2512.20190v1#bib.bib50)].
When the option market offers only a sparse set of quotes across strikes and maturities, i.e., low liquidity depth or intermittent trading,111Typical for on-chain protocols that list only a few ATM/OTM strikes on discrete maturities. GARCH-based measures provide a practical proxy for expected volatility and capture large moves in cryptocurrency markets [[45](https://arxiv.org/html/2512.20190v1#bib.bib45)]. Forecast studies also show that cryptocurrency volatility is better explained by crypto–specific factors, than by equity–based benchmarks [[30](https://arxiv.org/html/2512.20190v1#bib.bib30)]. For these reasons, the BS model with a regime-sensitive volatility serves as a coherent reference price for cross-sectional comparisons [[36](https://arxiv.org/html/2512.20190v1#bib.bib36), [32](https://arxiv.org/html/2512.20190v1#bib.bib32), [15](https://arxiv.org/html/2512.20190v1#bib.bib15), [14](https://arxiv.org/html/2512.20190v1#bib.bib14)]. We then define mispricing as the relative difference between the benchmark and the Hegic price and explain it with feasible GLS, accounting for heteroskedasticity, same–day dependence across contracts written on the same underlying.
The paper reports both statistical significance and economic magnitude.

The main findings are threefold. First, the benchmark price is higher than the Hegic quote on average, except for ETH put options, and the deviation is larger for call options. For wBTC mispricing increases with volatility, while this effect is not statistically distinguishable from zero for ETH. Second, the price deviation increases when the order is larger, the strike is further from the money, the maturity is longer, and the underlying is more volatile. On the contrary, it decreases when underlying trading volume is higher. Third, ETH options are generally closer to the benchmark than wBTC options.
These patterns admit a clear economic interpretation. In a pooled-liquidity AMM, larger orders impose higher marginal inventory and convexity risk on the pool. Far OTM and short-maturity options concentrate that convexity where hedging is most fragile, so quotes tend to move further from the benchmark. On the contrary, deeper markets improve the ability to hedge and bring quotes closer to the benchmark price.
The price deviation varies with market conditions. In high-volatility periods, cross-exchange price differences increase, however, when centralized exchange depth and on-chain transfer activity are higher, these differences decrease [[27](https://arxiv.org/html/2512.20190v1#bib.bib27), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)].
Common long-run factors and time-varying error correction imply that wBTC and ETH deviations can co-move in some periods [[26](https://arxiv.org/html/2512.20190v1#bib.bib26), [29](https://arxiv.org/html/2512.20190v1#bib.bib29)].
During large market moves or liquidity squeezes, prices tend to adjust first in the futures market while spot follows. The delayed price discovery or contract design can cause temporary differences between futures and spot prices during big market moves [[3](https://arxiv.org/html/2512.20190v1#bib.bib3)].
Additionally, market-wide efficiency in major cryptocurrencies has improved over time and is strongest when liquidity and money flows are high [[31](https://arxiv.org/html/2512.20190v1#bib.bib31), [43](https://arxiv.org/html/2512.20190v1#bib.bib43), [21](https://arxiv.org/html/2512.20190v1#bib.bib21), [34](https://arxiv.org/html/2512.20190v1#bib.bib34), [8](https://arxiv.org/html/2512.20190v1#bib.bib8)]. The results of the paper point to protocol design and market plumbing as the primary drivers of systematic deviations from the benchmark.

This paper complements the study of Andolfatto et al. [[5](https://arxiv.org/html/2512.20190v1#bib.bib5)]. Their focus is the implied–volatility (IV) difference between Lyra (on-chain) and Deribit (off-chain) options. They document the an on–chain IV premium is related to retail net buying of call options and to trading–volume shocks. The authors also examine the performance of a volatility–premium trading strategy. The focus of this paper is different, it analyses the on-chain pricing rule at the transaction level.
This trade-by-trade comparison isolates how the AMM prices options and where the price deviates from a model-based reference. Therefore, the paper investigates whether the deviation co–moves with the specific rules that an option AMM follows.
The two paper are, therefore, complementary. Cross–exchange IV comparisons show how on-chain markets as a whole differ from centralized order books.
Protocol-specific price diagnostics show how the AMM’s design maps market conditions into prices.

The contribution of this paper is both empirical and practical. First, with respect to volatility modelling/forecasting, we show that a two–regime MS–AR–(GJR)–GARCH model delivers a credible short-term volatility estimate for on-chain option valuation and we document asset-specific regime features (BTC vs. ETH) that are informative for forecasting and risk control. Second, with respect to protocol design, we map the documented price deviations into actionable calibration levers for Hegic-type AMMs. Third, with respect to the literature on on-chain option AMMs, we provide the first transaction-level evaluation of a rate-based option AMM and, thereby, advancing the empirical basis for AMM design in on-chain options.

The rest of the paper is organized as follows: Section [2](https://arxiv.org/html/2512.20190v1#S2 "2 Related literature ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reviews related work on cryptocurrency market efficiency, volatility regimes and breaks, and DeFi microstructure. Section [3](https://arxiv.org/html/2512.20190v1#S3 "3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") outlines the methodology design in Subsection [3.1](https://arxiv.org/html/2512.20190v1#S3.SS1 "3.1 Methodology ‣ 3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options"), presents the design of the Hegic protocol and data in Subsection [3.2](https://arxiv.org/html/2512.20190v1#S3.SS2 "3.2 Data ‣ 3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options"). Section [4](https://arxiv.org/html/2512.20190v1#S4 "4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reports the results and offers discussion. Section [5](https://arxiv.org/html/2512.20190v1#S5 "5 Conclusion ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") concludes the paper with implications and limitations.

## 2 Related literature

We group the literature into four strands that motivate the methodology choices of this paper: ([2.1](https://arxiv.org/html/2512.20190v1#S2.SS1 "2.1 Market efficiency ‣ 2 Related literature ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")) market efficiency; ([2.2](https://arxiv.org/html/2512.20190v1#S2.SS2 "2.2 Volatility regimes, jumps, and structural breaks ‣ 2 Related literature ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")) volatility regimes, jumps, and structural breaks; ([2.3](https://arxiv.org/html/2512.20190v1#S2.SS3 "2.3 Option microstructure, denomination, and hedging ‣ 2 Related literature ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")) option microstructure, denomination, and hedging; and ([2.4](https://arxiv.org/html/2512.20190v1#S2.SS4 "2.4 DeFi plumbing: AMMs, oracles, and protocol design ‣ 2 Related literature ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")) DeFi plumbing, i.e., AMMs, oracles, bridges, and protocol design.

### 2.1 Market efficiency

Tran and Leirvik [[43](https://arxiv.org/html/2512.20190v1#bib.bib43)] examine weak–form efficiency for BTC, ETH, XRP, LTC, and EOS during 2013–2019 using the Adjusted Market Inefficiency Magnitude and find that efficiency improves during 2017–2018, with event–driven setbacks. The authors find that LTC is most and XRP least efficient on average. López-Martín et al. [[31](https://arxiv.org/html/2512.20190v1#bib.bib31)] apply linear and nonlinear tests to BTC, LTC, ETH, XRP, XLM, and XMR and report that BTC, LTC and ETH become more efficient in later subsamples, consistent with the Adaptive Market Hypothesis.
Earlier work also documents time variation in efficiency and the return–risk trade-off. Bariviera [[9](https://arxiv.org/html/2512.20190v1#bib.bib9)] compute rolling Hurst exponents for BTC returns and volatility during 2011–2017 and show that return efficiency improves over time while volatility retains long memory and clustering. Focusing on the 2013 crash, Bouri et al. [[11](https://arxiv.org/html/2512.20190v1#bib.bib11)] estimate asymmetric GARCH models on daily BTC data and document an inverse leverage effect, i.e., volatility reacts more to positive than to negative return shocks, with dynamics that differ across the pre- and post-crash windows.
Using entropy–information methods for BTC, ETH, ADA, BNB, and XRP prices during 2018–2021, Fernandes et al. [[21](https://arxiv.org/html/2512.20190v1#bib.bib21)] find high and stable efficiency before and during COVID–19, with ETH exhibiting the least variation.
Multifractal evidence further clarifies the state dependence of efficiency. Aslam et al. [[8](https://arxiv.org/html/2512.20190v1#bib.bib8)] apply multifractal detrended fluctuation analysis to daily prices of ADA, BNB, BTC, ETH, LTC, and XRP up to early 2023 and rank assets by the width of the multifractal spectrum and a long-memory index. They find a lower weak-form efficiency, for BTC and LTC when multifractality is high. On the contrary, a stronger herding during crisis windows for ADA and BNB when multifractality is low. Therefre, they argue that efficiency varies with market conditions and across assets. Complementing this finding, Mokni et al. [[34](https://arxiv.org/html/2512.20190v1#bib.bib34)] measure efficiency using the Adjusted Market Inefficiency Magnitude (AMIM) for 2016–2023 and explain it with quintile regressions on global factors, e.g., financial stress, equity benchmarks, substitutes, e.g., commodities, and internal crypto variables, e.g., liquidity, volatility, money flows. They report that greater liquidity and stronger money flows are associated with lower AMIM, i.e., higher efficiency, whereas financial stress raises AMIM with effects that vary across quintiles. These studies imply that efficiency is time-varying and improves with depth and activity. Therefore, this paper treat persistent on-chain price deviations as design- and state-driven and investigates whether they decrease when underlying volume and market liquidity increase.

### 2.2 Volatility regimes, jumps, and structural breaks

A large strand of literature shows that cryptocurrency volatility is clustered, asymmetric, and state dependent, with jumps and structural breaks. Using daily date for BTC prices over the early market years up to 2016, Katsiampa [[25](https://arxiv.org/html/2512.20190v1#bib.bib25)] compare GARCH variants and show that GARCH–type specifications fit volatility better than simple historical measures. For BTC risk measurement, Stavroyiannis [[41](https://arxiv.org/html/2512.20190v1#bib.bib41)] estimate VaR and related metrics on daily data and document heavy tails, underscoring the relevance of fat–tailed errors for the option risk estimation. Focusing on regime changes, Thies and Molnár [[42](https://arxiv.org/html/2512.20190v1#bib.bib42)] apply Bayesian change–point methods to BTC daily returns during 2012–2018 and identify multiple volatility regimes. Over an earlier sample,, during 2011–2013, Ardia et al. [[7](https://arxiv.org/html/2512.20190v1#bib.bib7)] compare Markov–switching AR–GARCH models and find that a two–state MS–AR–GJR–GARCH with skewed–tt innovations performs best, confirming both regime switching and asymmetric responses.
The literature on the cross–asset evidence is consistent with this view. Using daily data for BTC, DASH, LTC, and XRP over 2014–2018, Charles and Darné [[16](https://arxiv.org/html/2512.20190v1#bib.bib16)] first detect and filter jumps and control for variance breaks. Once these are accounted for, GARCH inference changes significantly, IGARCH(tt) best fits BTC, DASH, and LTC, FIGARCH(tt) fits XRP, and leverage effects disappear. For BTC over 2010–2016, Bouri et al. [[12](https://arxiv.org/html/2512.20190v1#bib.bib12)] document highly persistent shocks at the full–sample level, mean reversion within break–defined subsamples, and long memory in volatility, highlighting the role of structural breaks for persistence measurement.

A part of stand argues that the window length matters as well. Across BTC, ETH, and XRP over 2011–2020, Wu [[50](https://arxiv.org/html/2512.20190v1#bib.bib50)] show that out–of–sample VaR from MS–GARCH is sensitive to the estimation window even when within–regime parameters are stable. They find BTC performing best around a 400–day window and ETH closer to 600 days. When listed option quotes are rare, Venter and Maré [[45](https://arxiv.org/html/2512.20190v1#bib.bib45)] construct GARCH–generated 30/60/90–day volatility indices for BTC and CRIX and validate them by pricing BTC options. The authors find that the indices track jumps and can invert at large shocks, supporting GARCH–type estimates as forward–looking proxies. The literature on forecasting points to crypto–specific drivers. Using the data over 2013–2019, Liang et al. [[30](https://arxiv.org/html/2512.20190v1#bib.bib30)] find that commodity volatility and investor attention (Google Trends) improve BTC volatility forecasts, while VIX adds little. Complementing these results, Chen et al. [[17](https://arxiv.org/html/2512.20190v1#bib.bib17)] estimate stochastic–volatility–with–jumps models on high–frequency intraday and daily BTC and show pervasive return and variance jumps and co–jumps that steepen short–maturity smiles. They find that diffusion–only benchmarks understate tail risk.
These studies show that ignoring jumps and breaks biases volatility estimates, and stable regime identification benefits from long samples that include multiple market conditions (booms, busts, stress events). Accordingly, we estimate a two–state MS–AR–(GJR)–GARCH on a long daily window for each underlying. This choice follows the window–sensitivity evidence in Wu [[50](https://arxiv.org/html/2512.20190v1#bib.bib50)], the option–pricing validation of GARCH indices in Venter and Maré [[45](https://arxiv.org/html/2512.20190v1#bib.bib45)], and the crypto–specific forecasting drivers in Liang et al. [[30](https://arxiv.org/html/2512.20190v1#bib.bib30)].

### 2.3 Option microstructure, denomination, and hedging

Empirically studies argue that simple diffusion models, e.g., the BS model with constant volatility, do not fit observed BTC option surfaces. Particularly, the pronounced smiles and short–maturity curvature.
Using ten BTC option surfaces222The BTC option surface is built on an index aggregating quotes from six BTC–USD spot exchanges, i.e., Bitfinex, Bitstamp, GDAX (Coinbase Pro), Gemini, Itbit, and Kraken. The options are European, cash–settled in BTC, with USD as the numéraire. collected weekly from June 29 to August 31, 2018, Madan et al. [[32](https://arxiv.org/html/2512.20190v1#bib.bib32)] show that stochastic–volatility and time–changed Lévy models outperform diffusion-only benchmarks. They report that the conic-finance implied liquidity metric rises with maturity and falls as options move further out of the money. Thus, liquidity is thinnest for short-maturity, far OTM options.
Complementing this funding, Olivares [[36](https://arxiv.org/html/2512.20190v1#bib.bib36)] calibrate a mean-reverting jump–diffusion under an Esscher-selected risk-neutral measure on daily BTC–USD data from January 2011 to June 2018 and reject diffusion-only specifications. The author finds that return and variance tails require jumps, which is most consequential for short maturities.
Alexander et al. [[4](https://arxiv.org/html/2512.20190v1#bib.bib4)] develop pricing for direct, inverse, and quanto–inverse cryptocurrency options and show that denomination and index–based settlement change payoff curvature and greeks. These design choices create a systematic deviation between what the option pays and what can be replicated with traded hedges, indicating that replication is only approximate. [[15](https://arxiv.org/html/2512.20190v1#bib.bib15)] do not specify the options’ nature, however contributes to the field by deriving the analytical formula for pricing BTC options. It is based on the equilibrium model of [[14](https://arxiv.org/html/2512.20190v1#bib.bib14)] where money supply and aggregated dividend follow jump-diffusion processes. The authors assume BTC as foreign currency in a small open economy and empirically find that the BS model underprices BTC options compared to their model. Although the authors do not differentiate between off-chain and on-chain options, they find that IV is sensitive to jumps in money supply and suggest that additional pricing risk should be considered when valuing cryptocurrency options.

Using one–minute data around the launch of U.S. BTC futures (December 2017–February 2018), Akyildirim et al. [[3](https://arxiv.org/html/2512.20190v1#bib.bib3)] show that price discovery often originates in the futures market and that structural breaks coincide with major news and regulatory events. Short–term spreads between futures and spot may be reflected in oracle-reported prices and, in turn, into on–chain quotes. Sebastião and Godinho [[40](https://arxiv.org/html/2512.20190v1#bib.bib40)] uses daily data and find that hedging BTC with BTC futures delivers large reductions in variance and semivariance, whereas cross–hedging ETH,LTC, or XRP with BTC futures is weak and can even increase expected shortfall.
Using a large cross–section of major cryptocurrencies with daily data up to 2019, Keilbar and Zhang [[26](https://arxiv.org/html/2512.20190v1#bib.bib26)] report four long–run cointegrating relations and introduce a COINtensity–VECM in which the strength of error correction varies over time. The error–correction loadings are the largest during the 2017–2018 bubble, so deviations from the long–run cointegrating relations close more quickly.
Leung and Nguyen [[29](https://arxiv.org/html/2512.20190v1#bib.bib29)] construct cointegrated spreads, using Coinbase daily prices for BTC, ETH, LTC, and BCH from December 20, 2017 to June 20, 2018, and show that they are tradable in–sample without costs, However, the performance of this strategy is sensitive to realistic transaction frictions. From the bear-market evidence, Kyriazis et al. [[28](https://arxiv.org/html/2512.20190v1#bib.bib28)] show that most major cryptocurrencies are complementary to BTC/ETH/XRP and that principal coins offer no hedging benefits in distressed times. The authors argue that information-criterion selection favors asymmetric and nonlinear GARCH variants for many assets, indicating time-varying co-movement. This findings explains why on-chain AMM deviations can become systemic during stress.

This literature strand implies larger price deviations for bigger orders and for options further out of the money or nearer to maturity. On the contrary, it suggests decreasing price deviations with greater liquidity depth, market activity, and the possibility of cross-asset co-movement of deviations in particular market states.

### 2.4 DeFi plumbing: AMMs, oracles, and protocol design

On-chain pricing is constrained by how protocols encode trading, data, and settlement. In an early feasibility study on ETH, Eskandari et al. [[20](https://arxiv.org/html/2512.20190v1#bib.bib20)] implement a fully collateralized option and two oracle designs: (i) callback oracles that trigger contract updates on events, and (ii) per–block oracle that write prices each block. Their experiments show that while the option logic is straightforward to encode, oracle delivery, gas costs, and liveness are binding: callbacks can miss or delay updates, whereas per–block posting improves liveness at the cost of trusting an oracle. Vakhmyanin and Volkovich [[44](https://arxiv.org/html/2512.20190v1#bib.bib44)] compare Mycelium, a centralized exchange oracle on Arbitrum, with Chainlink, a cross-chain decentralized oracle network, around two high–volatility windows in around FTX collapse (November 2022).
They measure the percentage deviation between each oracle and a three-exchange median (Binance, FTX, Bitfinex). In calm periods, the Mycelium oracle updates quickly with average latency ≈0.3\approx 0.3 seconds and stays close to the median and, on high-volatility days, the deviation widens. On the contrary, Chainlink’s 2.5% deviation threshold can delay updates. Consequently, those deviations across centralized exchanges can incfluence the oracle feed and, in turn, into on-chain quotes.

Rahman et al. [[39](https://arxiv.org/html/2512.20190v1#bib.bib39)] survey option protocols such as Lyra, Deri, Vega, and Thales (primarily on ETH/L2s) and document the key design choices that differentiate them from centralized venues are: AMM pricing rules, oracle providers, liquidity architecture e.g., peer–to–pool vs. peer–to–peer, and governance/incentive tokens. These choices impact inventory, funding, and data–quality risks that affect quoted premiums.
Priem [[37](https://arxiv.org/html/2512.20190v1#bib.bib37)] examine the OTC derivatives life cycle on distributed ledgers and show that near-instant settlement reduces multilateral netting, thereby increasing gross funding needs for long-term positions. They also argue that smart contracts do not, by themselves, resolve issues of legal enforceability, privacy, or cross-platform interoperability. These frictions provide a reason why on-chain quotes can persistently differ from the benchmark.
McCorry et al. [[33](https://arxiv.org/html/2512.20190v1#bib.bib33)] classify bridge validation designs and highlight core trade-offs among security assumptions, latency, and interoperability. Bridge choices determine how quickly and safely assets and price information can move across domains. They interact with oracle update cadence, influencing the timing of settlement and hedging on-chain.
Reviewing empirical work on stablecoins, Ante et al. [[6](https://arxiv.org/html/2512.20190v1#bib.bib6)] summarize evidence on adoption, liquidity, and peg stability. The authors emphasize that market distress can lead to temporary depegs and liquidity strains. When option protocols settle in stablecoins, these dynamics can influence realized payoffs, liquidity provision, and risk management.

The above mentioned evidence implies that differences between an AMM quote and the benchmark price can arise from protocol setting. Accordingly, we include explanatory variables that map directly to those mechanisms: order size (inventory and funding pressure in a pooled pool), moneyness and maturity (option convexity and hedgeability), underlying volatility (data/throughput stress and hedging difficulty), and liquidity depth (external hedging capacity).

The combined findings of the literature strands indicate that since major cryptocurrency markets are often informationally efficient for long periods, persistent on–chain deviations should be traced to protocol setting and market conditions rather than to a failure of price discovery. Because volatility is jumpy and regime dependent, the volatility estimation should cover heavy tails and short–term convexity. Since denomination/settlement, hedging capacity, and oracle design affect replication and inventory risk, deviations should be larger when orders are bigger, strikes are further from the money, maturities are short, or volatility is elevated, and should shrink when underlying volume and on–chain activity increase in the market. These predictions map directly into our empirical specification and the interpretation of economic magnitudes.

## 3 Empirical analysis

This section outlines how we construct a regime–sensitive volatility input and a benchmark price to evaluate Hegic quotes, and how we then measure and explain mispricing.

### 3.1 Methodology

The methodology starts with constructing a regime–switching volatility input using BTC and ETH time series and only then prices options with the Black and Scholes [[10](https://arxiv.org/html/2512.20190v1#bib.bib10)] model. The resulting benchmark prices are compared to Hegic quotes at the transaction timestamp, and the cross–section of price deviations is explained with a feasible GLS (FGLS) regression. Each step is motivated by the empirical finding on of cryptocurrency returns properties and by the protocol’s microstructure.

#### Step 1: Regime identification

We model daily rates of return rtr\_{t} with a two–regime Markov–Switching autoregression (MS-AR) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=μρt+∑i=1aϕρt,i​rt−i+ερt,t,ερt,t∼𝒩​(0,σρt2)\displaystyle r\_{t}=\mu\_{\rho\_{t}}+\sum\_{i=1}^{a}\phi\_{\rho\_{t},i}\,r\_{t-i}+\varepsilon\_{\rho\_{t},t},\qquad\varepsilon\_{\rho\_{t},t}\sim\mathcal{N}\!\bigl(0,\sigma^{2}\_{\rho\_{t}}\bigr) |  | (1) |

where ρt∈{0,1}\rho\_{t}\in\{0,1\} denotes the regime at time tt and follows a first-order Markov chain with transition probabilities
ps​s′=Pr⁡(ρt=s′∣ρt−1=s)p\_{ss^{\prime}}=\Pr(\rho\_{t}=s^{\prime}\mid\rho\_{t-1}=s) for s,s′∈{0,1}s,s^{\prime}\in\{0,1\}.
We estimate the model by maximum likelihood and get, for each day tt,
smoothed state probabilities as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p~t​(s)=Pr⁡(ρt=s∣ℱT),s∈{0,1}\displaystyle\tilde{p}\_{t}(s)=\Pr(\rho\_{t}=s\mid\mathcal{F}\_{T}),\qquad s\in\{0,1\} |  | (2) |

where ℱT\mathcal{F}\_{T} is all information up to the end of the sample. We then sort days into regimes where we assign day tt to the state with the higher smoothed probability as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^t=arg⁡maxs∈{0,1}⁡p~t​(s)\displaystyle\hat{\rho}\_{t}=\arg\max\_{s\in\{0,1\}}\tilde{p}\_{t}(s) |  | (3) |

If maxs⁡p~t​(s)≤0.5\max\_{s}\tilde{p}\_{t}(s)\leq 0.5, we treat tt as uncertain, this avoids noisy classifications. The MS-AR is label-invariant, so after estimation we name the regimes by their level of variances. The regime with the larger variance is labeled high-volatility, the other low-volatility.
We report the transition matrix, expected durations, and the smoothed probability plots which provides the probability of being in the certain regime and how persistent the regimes are.

#### Step 2: Regime–conditional volatility estimation

Within each regime identified by the MS–AR model, we fit a regime–conditional GJR–GARCH process with skewed–tt distribution to capture volatility clustering and asymmetry [[23](https://arxiv.org/html/2512.20190v1#bib.bib23), [7](https://arxiv.org/html/2512.20190v1#bib.bib7)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϵρt,t\displaystyle\epsilon\_{\rho\_{t},t} | ∼skewed-​t​(0,σρt,t2,η,λ),\displaystyle\sim\text{skewed-}t\!\left(0,\ \sigma^{2}\_{\rho\_{t},t},\,\eta,\lambda\right), |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σρt,t2\displaystyle\sigma^{2}\_{\rho\_{t},t} | =ωρt+∑i=1pαρt,i⋅ϵρt,t−i2+∑i=1oγρt,i⋅ϵρt,t−i2⋅I​(ϵρt,t−i<0)+∑j=1qβρt,j⋅σρt,t−j2\displaystyle=\omega\_{\rho\_{t}}\;+\;\sum\_{i=1}^{p}\alpha\_{\rho\_{t},i}\,\cdot\epsilon^{2}\_{\rho\_{t},t-i}\;+\;\sum\_{i=1}^{o}\gamma\_{\rho\_{t},i}\,\cdot\epsilon^{2}\_{\rho\_{t},t-i}\,\cdot I(\epsilon\_{\rho\_{t},t-i}<0)\;+\;\sum\_{j=1}^{q}\beta\_{\rho\_{t},j}\,\cdot\sigma^{2}\_{\rho\_{t},t-j} |  | (5) |

For each cryptocurrency and regime we select (p,o,q)(p,o,q) by the Bayesian Information Criterion (BIC) over p,q∈{1,…,10}p,q\in\{1,\dots,10\} and o∈{0,…,5}o\in\{0,\dots,5\}. If o=0o=0, the specification reduces to standard GARCH. We report AIC/BIC, Ljung–Box and Engle’s ARCH statistics on standardized residuals, as well as the estimated degrees of freedom and skewness, to document fit and remaining dynamics. The conditional variance path σρt,t2\sigma^{2}\_{\rho\_{t},t} provides a time–varying volatility input aligned to each options’ purchase date. We convert the daily conditional variance to annualized volatility.

#### Step 3: Benchmark price estimation

Given σt\sigma\_{t} from step 2, we compute the BS benchmark price for call CC and put PP options as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C\displaystyle C | =S⋅N​(d1)−K⋅e−rf⋅T⋅N​(d2)\displaystyle=S\cdot N(d\_{1})-K\cdot e^{-r\_{f}\cdot T}\cdot N(d\_{2}) |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P\displaystyle P | =K⋅e−rf⋅T⋅N​(−d2)−S⋅N​(−d1)\displaystyle=K\cdot e^{-r\_{f}\cdot T}\cdot N(-d\_{2})-S\cdot N(-d\_{1}) |  | (7) |

where SS denotes the price of the underlying, KK denotes the strike price, rfr\_{f} denotes the risk free rate, TT denotes maturity, d1=ln⁡(SK)+(r+σ22)⋅Tσ⋅Td\_{1}=\frac{\ln\left(\frac{S}{K}\right)+\left(r+\frac{\sigma^{2}}{2}\right)\cdot T}{\sigma\cdot\sqrt{T}} and d2=d1−σ⋅Td\_{2}=d\_{1}-\sigma\cdot\sqrt{T}. We treat BS with a regime–switching volatility as a reference price suitable for short maturities, not as a full structural model of the risk–neutral measure [[32](https://arxiv.org/html/2512.20190v1#bib.bib32), [36](https://arxiv.org/html/2512.20190v1#bib.bib36), [45](https://arxiv.org/html/2512.20190v1#bib.bib45), [30](https://arxiv.org/html/2512.20190v1#bib.bib30)]. This design matches the single–purchase nature of Hegic contracts.

#### Step 4: Mispricing measurement

For each option jj, we define the relative price deviation, i.e., mispricing, as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​pricej=C​(P)j−OjOj\displaystyle\Delta\text{price}\_{j}\;=\;\frac{C(P)\_{j}-O\_{j}}{O\_{j}} |  | (8) |

where OjO\_{j} is the Hegic quote and C​(P)jC(P)\_{j} is the benchmark price for call and put, respectively. A positive value indicates that the benchmark exceeds the Hegic quote, whereas a negative value indicates the reverse. All inputs are aligned at the exact trade timestamp.

#### Step 5: Cross-sectional analysis

We explain cross-sectional variation in Δ​pricej\Delta\text{price}\_{j} with trade-time variables that mirror the AMM pricing rule and market condition. Order size (*Amount*) captures inventory and funding pressure in a pooled AMM. Larger trades generate convexity risk in the pool and are costlier to absorb, especially with near-instant settlement [[37](https://arxiv.org/html/2512.20190v1#bib.bib37), [39](https://arxiv.org/html/2512.20190v1#bib.bib39)]. Moneyness (*Strike*) captures how far the option is from the money. Far OTM options are harder to replicate and trade in illiquid markets.
Maturity (*Maturity*) matters for two opposing reasons. Options near maturity exhibit high gamma, which makes hedging more complex, whereas options far from maturity lock collateral for longer and increase funding needs [[37](https://arxiv.org/html/2512.20190v1#bib.bib37)].
The underlying rate of return (*Return*) and trading volume (*Volume*) are proxies for liquidity depth and trading activity. The greater the liquidity depth and on-chain activity the smaller are cross-exchange price deviations [[27](https://arxiv.org/html/2512.20190v1#bib.bib27)]. We also include the underlying volatility σt\sigma\_{t}, since it tracks jumps and provide forward-uncertainty proxies [[45](https://arxiv.org/html/2512.20190v1#bib.bib45)]. Finally, dummies for option kind (call=1) and type (ATM=1) allow for side-specific pressure, e.g., retail net call buying on-chain [[5](https://arxiv.org/html/2512.20190v1#bib.bib5)].

Since many options are bought on the same day on the same underlying, the regression errors can be heteroskedastic (their variance changes with trade characteristics such as order size or moneyness) and within–day correlated (trades share the same market conditions). OLS coefficients remain unbiased but are inefficient, and their standard errors can be misleading. We therefore use two–step feasible GLS (FGLS) [[13](https://arxiv.org/html/2512.20190v1#bib.bib13), pp. 204–210] to model the error variance, reweight observations, and report standard errors that remain valid even when residual variances differ across trades. The first step is a baseline fit where we estimate the cross–sectional model with standard OLS as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​pricej\displaystyle\Delta\text{price}\_{j} | =β0+βamount⋅Amountj+βstrike⋅Strikej+βmaturity⋅Maturityj\displaystyle=\beta\_{0}+\beta\_{\text{amount}}\cdot\text{Amount}\_{j}+\beta\_{\text{strike}}\cdot\text{Strike}\_{j}+\beta\_{\text{maturity}}\cdot\text{Maturity}\_{j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +βreturn⋅Returnt,j+βvolume⋅Volumet,j+βvol⋅Volatilityt,j\displaystyle\quad+\beta\_{\text{return}}\cdot\text{Return}\_{t,j}+\beta\_{\text{volume}}\cdot\text{Volume}\_{t,j}+\beta\_{\text{vol}}\cdot\text{Volatility}\_{t,j} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +βkind⋅Kindj+βtype⋅Typej+ξj\displaystyle\quad+\beta\_{\text{kind}}\cdot\text{Kind}\_{j}+\beta\_{\text{type}}\cdot\text{Type}\_{j}+\xi\_{j} |  | (9) |

From this step, we collect residuals ξ^j\hat{\xi}\_{j} which contain the behavior of how error variance varies across trades. The next step in the cross-sectional analysis is to estimate the variance model and weights. For this, we square the collected residuals and explain their dispersion with the same regressors via auxiliary regression as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ^j 2\displaystyle\hat{\xi}\_{j}^{\,2} | =γ0+γamount⋅Amountj+γstrike⋅Strikej+γmaturity⋅Maturityj\displaystyle=\gamma\_{0}+\gamma\_{\text{amount}}\cdot\text{Amount}\_{j}+\gamma\_{\text{strike}}\cdot\text{Strike}\_{j}+\gamma\_{\text{maturity}}\cdot\text{Maturity}\_{j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +γreturn⋅Returnt,j+γvolume⋅Volumet,j+γvol⋅Volatilityt,j\displaystyle\quad+\gamma\_{\text{return}}\cdot\text{Return}\_{t,j}+\gamma\_{\text{volume}}\cdot\text{Volume}\_{t,j}+\gamma\_{\text{vol}}\cdot\text{Volatility}\_{t,j} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +γkind⋅Kindj+γtype⋅Typej+νj\displaystyle\quad+\gamma\_{\text{kind}}\cdot\text{Kind}\_{j}+\gamma\_{\text{type}}\cdot\text{Type}\_{j}+\nu\_{j} |  | (10) |

The fitted values form the diagonal elements of the omega matrix Ω\Omega. This variance-covariance matrix, which incorporates the heteroskedasticity pattern. This variance-covariance matrix incorporates the heteroskedasticity pattern of the data. Observations predicted to have large residual variance, e.g., big orders or far–OTM strikes, receive less weight in FGLS regression (the final step); low–variance observations receive more weight. This directly addresses heteroskedasticity and improves estimates efficiency.
The final step is the GLS regression, estimated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^GLS=(X⊤⋅Ω−1⋅X)−1⋅X⊤⋅Ω−1⋅Δ​price\displaystyle\hat{\beta}\_{\text{GLS}}=(X^{\top}\cdot\Omega^{-1}\cdot X)^{-1}\cdot X^{\top}\cdot\Omega^{-1}\,\cdot\Delta\text{price} |  | (11) |

where XX contains the same regressors as in equation ([9](https://arxiv.org/html/2512.20190v1#S3.E9 "In Step 5: Cross-sectional analysis ‣ 3.1 Methodology ‣ 3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")). This step is equivalent to weighted least squares where each trade is weighted by the inverse of its predicted error variance. When error variance differs across trades, these GLS estimates use the information more efficiently than OLS and typically yield more reliable standard errors. We report heteroskedasticity– and autocorrelation–consistent (HAC) standard errors [[35](https://arxiv.org/html/2512.20190v1#bib.bib35)], which are robust to unequal variances and short–term correlation. We also report Wald tests for joint significance, the adjusted R2R^{2}, the condition number, and variance–inflation factors (VIFs) to document multicollinearity.

### 3.2 Data

Hegic is a peer-to-pool option AMM deployed on ETH and Arbitrum blockchains. It lists American-style options (called hedge contracts) on wrapped wBTC and ETH, and allows only long positions. The options’ counterparty is a pooled liquidity vault funded in stablecoins (DAI, USDC, USDT).Premiums paid by buyers accrue to the pool, and losses are allocated to liquidity providers in proportion to each provider’s share of the pool. The protocol relies on an external price oracle (Chainlink) for the underlying, settles in DAI, and routes swaps through a decentralized exchange (Uniswap). When adding liquidity to the poool, liquidity providers receive ERC-20 token, e.g., writeDAI, and a portion of the pool is locked until option expiry. Withdrawals are otherwise subject to available unlocked liquidity and a queueing mechanism. A portion of idle DAI can be wrapped into CHAI to earn interest via MakerDAO, i.e., additional incentive for the liquidity provision [[48](https://arxiv.org/html/2512.20190v1#bib.bib48)].

The AMM pricing rule on Hegic is unique and rate-based. For a given strike KK and maturity TT from the protocol’s discrete grid, the quoted option premium is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | O=v​(K,T)⋅S\displaystyle O=v(K,T)\cdot S |  | (12) |

where v​(⋅)v(\cdot) is a predefined rate. Buyers pay an additional settlement fee is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s=Amount×O×rs\displaystyle s=\text{Amount}\times O\times r\_{s} |  | (13) |

where ATM options carry a 1%1\% settlement rate and OTM options 0.5%0.5\%. The rate of strike grid is discrete and symmetric around the spot. For calls, available strikes are at 100%,110%,120%,130%100\%,110\%,120\%,130\% of the oracle price and, for puts, at 100%,90%,80%,70%100\%,90\%,80\%,70\% with maturities spanning from 7 to 90 days. Hegic does not offer in-the-money options.

This design contrasts with other on-chain option protocols. Lyra uses a BS–style surface from an external oracle (Block Scholes) and splits risk across a collateral pool and a delta-hedging pool. The protocol offers maturity in four fixed expires, i.e., 7/14/21/28 days. [[18](https://arxiv.org/html/2512.20190v1#bib.bib18), [39](https://arxiv.org/html/2512.20190v1#bib.bib39)] Deri offers everlasting options (BS model with the T→∞T\!\to\!\infty) where positions are balanced through continuous funding payments and a proactive market–making algorithm that adjusts to oracle quotes. [[2](https://arxiv.org/html/2512.20190v1#bib.bib2), [1](https://arxiv.org/html/2512.20190v1#bib.bib1)]. Additionally, the protocol is deployed across multiple chains which broadens access and can lower user costs on L2s. However, it can also fragment liquidity across exchanges and introduce bridge-related security risk. Moreover, oracle parameters are chain specific, so update timing can also differ. The net effect on depth and price quality is, therefore, ambiguous and state dependent [[39](https://arxiv.org/html/2512.20190v1#bib.bib39), [33](https://arxiv.org/html/2512.20190v1#bib.bib33), [37](https://arxiv.org/html/2512.20190v1#bib.bib37), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)].

Unlike BS–style AMMs, Hegic calculates quotes from a static rate table on a discrete strike–maturity grid, where users restricted to buying options, i.e., only long positions.
The level of the quote depends primarily on the rate schedule and the execution depends on available pool liquidity.
In Hegic, the liquidity pool is the sole writer of all options, and both premia and payouts are shared across liquidity providers in proportion to their pool share. When a liquidity provider also buys an option from the same pool, part of the premium they pay flows back to them through their liquidity provider entitlement, and part of any eventual payout is borne by them for the same reason. Economically, this is equivalent to buying a smaller position from an external counterparty. The liquidity provider’s effective premium paid and effective payoff are both reduced by the fraction of the pool they own. Two practical implications follow. First, liquidity provider purchases partially offset the pool’s natural short-convexity exposure without withdrawing liquidity, because the buyer and the holder of the option are partly the same economic agent. Second, a liquidity provider who buys an option from the pool does not create a free gain. Because the pool is the counterparty, part of the premium the liquidity provider pays is redistributed back to them through their pool share, but the same share also funds a proportion of any future payout if the option finishes in the money. After protocol fees and the fact that premia are shared with all liquidity providers, the pay back is incomplete. Economically, such a trade simply rebalances the liquidity provider’s net short-gamma exposure, i.e., reducing risk taken via the pool rather than generating arbitrage profits.

If the Hegic rate vv is not adjusted when market volatility or order pressure changes, the quoted premium OO can drift from a benchmark price PBSP^{\text{BS}}. When vv is set too low for current risk, quotes fall below the benchmark and the pool is under-compensated for the convexity it sells (options are “too cheap” for buyers). When vv is set too high, quotes exceed the benchmark and order flow usually declines, but filled trades pay higher premia to the pool. In practice, if O<PBSO<P^{\text{BS}} a trader can buy on Hegic and hedge delta in spot or futures off-protocol; if O>PBSO>P^{\text{BS}}, the short position must be taken on another exchange because Hegic does not allow users to write options. Execution costs, hedge basis, oracle timing, and available depth limit any cross-exchange strategy and help explain why price deviations can persist [[4](https://arxiv.org/html/2512.20190v1#bib.bib4), [37](https://arxiv.org/html/2512.20190v1#bib.bib37), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)]. These motivate our explanatory variables and point to calibration possibilities for a rate-based AMM.

Fully on–chain option AMMs are still a small segment of DeFi. At the time of writing, TVL in DeFi option protocols is about $100 million where Hegic accounts for $28.5 million and is the largest option AMM by TVL. Within Hegic, $25.3 million is locked on Arbitrum and $1.7 million on ETH, so most activity occurs on Arbitrum. Therefore, we analyze all Hegic option trades on Arbitrum between October 24, 2022 and May 21, 2024, which is the full history available on that chain at the time of writing.

Unlike centralized exchanges, decentralized exchange trades are recorded on–chain with public excess. Each observation includes the option type, strike, maturity, amount (fractional units allowed), the paid premium (in stablecoin), and the exact block timestamp, as well as the buyer address and transaction hash.
Figures [1](https://arxiv.org/html/2512.20190v1#S3.F1 "Figure 1 ‣ 3.2 Data ‣ 3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")–[2](https://arxiv.org/html/2512.20190v1#S3.F2 "Figure 2 ‣ 3.2 Data ‣ 3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") show Sankey charts of purchased options by unique address and summarize protocol participation. For wBTC, 1,315 options were bought by 275 addresses, with roughly 40% of all contracts purchased by two addresses.3330x7…d3d address bought 346 options and 0x7…74c address bought 150 options. The split is 723 call options (377 ATM options) and 592 put options (400 ATM options). For ETH, 2,775 options were bought by 728 addresses, with about 40% purchased by 18 addresses. ETH order flow is more dispersed than wBTC. ETH totals are 1,664 calls (1,137 ATM) and 1,111 puts (621 ATM). The prevalence of ATM options is consistent with leveraged directional views which align with on–chain evidence in Andolfatto et al. [[5](https://arxiv.org/html/2512.20190v1#bib.bib5)].

Figure 1: Sankey chart — wBTC option holders

![Refer to caption](figures/sankey_BTC.png)

Figure 2: Sankey chart — ETH option holders

![Refer to caption](figures/sankey_ETH.png)

Table [5](https://arxiv.org/html/2512.20190v1#A1.T5 "Table 5 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reports summary statistics by the underlying and kind. Fractional order sizes exhibit very small minimum and mean premiums are of similar level across buckets, with higher dispersion for wBTC reflecting its higher price level. By design, strikes reflect a discrete grid (ATM and fixed OTM steps), and maturities cluster at 7–90 days with similar medians across buckets. ETH options show larger Amount quartiles than wBTC, consistent with deeper trading activity shown in the figure [2](https://arxiv.org/html/2512.20190v1#S3.F2 "Figure 2 ‣ 3.2 Data ‣ 3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options"). Across both underlying, call options show higher mean volumes than puts, in line with speculative demand found in Andolfatto et al. [[5](https://arxiv.org/html/2512.20190v1#bib.bib5)].

## 4 Results

We begin by constructing the volatility input for wBTC and ETH options. For this, the time-series history of daily prices for BTC and ETH prices from December 7, 2018, until May 25, 2024, are retrieved from CryptoCompare via API. This time horizon includes distinct market conditions that are important for identifying regimes, i.e., the COVID-19 shock in March 2020, the 2020–2021 bull run associated with “DeFi Summer,” and major policy episodes, e.g., EU MiCA negotiations. A long history that covers both calm and stressed periods is necessary for reliable regime detection. Otherwise, regime probabilities and state-conditional dynamics are weakly identified. Prior research documents structural breaks, long memory, and regime changes in cryptocurrency volatility, and shows that inference and tail-risk forecasts are sensitive to the estimation window [[42](https://arxiv.org/html/2512.20190v1#bib.bib42), [7](https://arxiv.org/html/2512.20190v1#bib.bib7), [16](https://arxiv.org/html/2512.20190v1#bib.bib16), [12](https://arxiv.org/html/2512.20190v1#bib.bib12), [50](https://arxiv.org/html/2512.20190v1#bib.bib50)]. Consistent with this evidence, we use roughly ∼\sim2,000 daily observations to estimate a two-regime MS–AR–(GJR)–GARCH: the Markov-switching autoregression assigns each day to a low- or high-volatility regime, and, within each regime, a GJR–GARCH with skewed-tt innovations captures volatility clustering and asymmetry. This provides the rationale for the regime–sensitive volatility input and a longer time horizon than the option sample.

Table [4](https://arxiv.org/html/2512.20190v1#A1.T4 "Table 4 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") summarizes the statistics of BTC and ETH rates of return. Mean rates of return for both samples are positive, with around four percentage points higher for ETH. This is likely due to the continuously growing DeFi ecosystem, where ETH is the preferable blockchain and plays a vital role in various on-chain applications. ETH rates of return also exhibit higher standard deviation and minimum and maximum values, suggesting significant price variations. This, in turn, again highlights the dominant role of ETH in the ecosystem, where an increased amount of projects deployed on its chain and a high transaction flow lead to more frequent price changes. Both BTC and ETH time series are left-skewed, suggesting events with a more pronounced price decline. Similarly, high kurtosis values indicate fat tails, which emphasize extreme values in rates of return.

Table [1](https://arxiv.org/html/2512.20190v1#S4.T1 "Table 1 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reports estimates from two–regime MS–AR models in which the intercept, autoregressive coefficients, and innovation variance may differ by regime. Robust standard errors (HAC) are in parentheses and statistical significance is based on tt–statistics: ∗∗∗, ∗∗, and ∗ denote the 1%, 5%, and 10% levels, respectively. Parameters are obtained by maximum likelihood using the limited-memory BFGS (L-BFGS) algorithm, which approximates the inverse Hessian without storing the full matrix. The table also reports heteroskedasticity-robust standard errors in parentheses [[47](https://arxiv.org/html/2512.20190v1#bib.bib47)]. The autoregressive order is eight for BTC and ten for ETH (selected from PACF figures [15(a)](https://arxiv.org/html/2512.20190v1#A1.F15.sf1 "In Figure 15 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") and [15(b)](https://arxiv.org/html/2512.20190v1#A1.F15.sf2 "In Figure 15 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")). Regime labels are assigned by variance levels. For BTC, Regime 0 is the low-volatility regime (σ2^=2.46\widehat{\sigma^{2}}=2.46) and Regime 1 the high-volatility regime (σ2^=28.61\widehat{\sigma^{2}}=28.61). For ETH, Regime 0 is high volatility (σ2^=51.83\widehat{\sigma^{2}}=51.83) and Regime 1 low volatility (σ2^=6.06\widehat{\sigma^{2}}=6.06).
The autoregressive terms for both BTC and ETH show several significant coefficients, with ETH’s rates of return showing more significant coefficients for high volatility regime, indicating stronger autoregressive behavior. With respect to persistency, for BTC the probability of remaining in the low-volatility regime is p^​(0→0)=0.771\widehat{p}(0\!\to\!0)=0.771, while for ETH the probability of remaining in the high-volatility state is p^​(0→0)=0.750\widehat{p}(0\!\to\!0)=0.750. The corresponding switch probabilities are moderate, for BTC, p^​(1→0)=0.366\widehat{p}(1\!\to\!0)=0.366 (and p^​(0→1)=0.229\widehat{p}(0\!\to\!1)=0.229) and, for ETH, p^​(1→0)=0.113\widehat{p}(1\!\to\!0)=0.113 (and p^​(0→1)=0.250\widehat{p}(0\!\to\!1)=0.250). These magnitudes are consistent with prior evidence of regime persistence in BTC volatility [[7](https://arxiv.org/html/2512.20190v1#bib.bib7)].
For ETH, several autoregressive coefficients are significant in the high-volatility regime, and the model implies a high day-to-day probability of remaining in that regime, indicating strong persistence. The estimated probability of leaving the high-volatility regime is low for ETH, suggesting high-volatility episodes are more persistent for ETH than for BTC. Overall, once a regime is entered, returns tend to remain in that regime over short horizons.

Table 1: Markov switching model results

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | BTC | | ETH | |
| AIC | 10199.1912 | | 11206.6259 | |
| BIC | 10322.3224 | | 11352.1183 | |
|  | Regime 0 | Regime 1 | Regime 0 | Regime 1 |
| Constant | 0.1208 | 0.0712 | 0.5293∗ | 0.0924 |
|  | (0.0823) | (0.1870) | (0.3153) | (0.1378) |
| σ2\sigma^{2} | 2.4550∗∗∗ | 28.6134∗∗∗ | 51.8320∗∗∗ | 6.0647∗∗∗ |
|  | (0.7101) | (7.7156) | (12.8606) | (1.4789) |
| ar.L1 | -0.1311∗∗∗ | -0.0562 | -0.1359∗∗ | -0.1114∗∗∗ |
|  | (0.0374) | (0.0742) | (0.0543) | (0.0397) |
| ar.L2 | 0.0421 | 0.0072 | 0.1297∗∗ | -0.0398 |
|  | (0.0468) | (0.0728) | (0.0659) | (0.0423) |
| ar.L3 | 0.0539 | -0.0301 | 0.0821 | -0.0209 |
|  | (0.0459) | (0.0940) | (0.1115) | (0.0402) |
| ar.L4 | -0.0794∗∗ | 0.1206∗∗∗ | 0.0325 | -0.0142 |
|  | (0.0368) | (0.0381) | (0.2085) | (0.0759) |
| ar.L5 | 0.0203 | -0.0581∗∗ | -0.0770 | 0.0028 |
|  | (0.0325) | (0.0294) | (0.0959) | (0.0566) |
| ar.L6 | -0.0044 | -0.0515 | 0.0807 | -0.0381 |
|  | (0.0389) | (0.0826) | (0.0717) | (0.0363) |
| ar.L7 | -0.0509 | 0.0873 | 0.0213 | -0.0071 |
|  | (0.0433) | (0.1027) | (0.1005) | (0.0442) |
| ar.L8 | -0.0065 | -0.0169 | -0.1571∗ | 0.0199 |
|  | (0.0318) | (0.0278) | (0.0917) | (0.0304) |
| ar.L9 |  |  | -0.0145 | -0.0203 |
|  |  |  | (0.0385) | (0.0344) |
| ar.L10 |  |  | 0.1617∗ | -0.0151 |
|  |  |  | (0.0855) | (0.0601) |
| Regime transition parameters | | | | |
| p​(0→0)p(0\to 0) | 0.7710∗∗∗ | | 0.7502∗∗∗ | |
|  | (0.0556) | | (0.0960) | |
| p​(1→0)p(1\to 0) | 0.3659∗∗∗ | | 0.1127∗ | |
|  | (0.1052) | | (0.0595) | |

Figures [3](https://arxiv.org/html/2512.20190v1#S4.F3 "Figure 3 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") and [4](https://arxiv.org/html/2512.20190v1#S4.F4 "Figure 4 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") depict smoothed probabilities of regime 0 (low volatility for BTC and high volatility for ETH) in green and regime 1 (high volatility for BTC and low volatility for ETH) in purple from the MS-AR model. For BTC, the low volatility regime shows more frequent transitions between low and high volatility states. The interruption in persistence staying in a low volatility regime is observable around early 2020, i.e., the bear market, and late 2020 to early 2021, i.e., the bull market. The high volatility regime shows significant periods around these dates as well, highlighting market reactions. For ETH, both regimes show less frequent transitions and show more pronounced peaks, indicating increased market activity. On the contrary, the low volatility regime shows persistence after late 2021, which mirrors the growing adoption and the establishment of the ETH chain in the decentralized finance ecosystem.
Both BTC and ETH show significant reactions to global market events, pinned down by frequent regime changes and definite peaks, correspondingly.

Figure 3: Volatility regimes - BTC

![Refer to caption](figures/regimes_n_BTC.png)



Figure 4: Volatility regimes - ETH

![Refer to caption](figures/regimes_n_ETH.png)

Table [2](https://arxiv.org/html/2512.20190v1#S4.T2 "Table 2 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reports the regime–specific volatility models selected after the MS–AR classification, where the model choice is based on the BIC.
Standard errors (in parentheses) of estimated coefficients for the mean (top) and variance (middle) equations and the error distribution (bottom) are robust to heteroskedasticity and autocorrelation. The significance is based on tt-statistics: ∗∗∗, ∗∗, ∗ denote the 1%, 5%, and 10% levels. The GJR term γ1\gamma\_{1} appears only in the GJR–GARCH specification. Goodness-of-fit is assessed with Ljung–Box and Engle’s ARCH diagnostics. Only for BTC’s low–volatility regime the optimal process is a GJR–GARCH(1,1,1). The estimated leverage parameter is negative and highly significant, indicating an inverse leverage effect (positive shocks raise volatility more than negative shocks). This pattern, unusual for equities but repeatedly documented for BTC, aligns with findings in Bouri et al. [[11](https://arxiv.org/html/2512.20190v1#bib.bib11)], Katsiampa [[25](https://arxiv.org/html/2512.20190v1#bib.bib25)], Stavroyiannis [[41](https://arxiv.org/html/2512.20190v1#bib.bib41)], and Ardia et al. [[7](https://arxiv.org/html/2512.20190v1#bib.bib7)]. On the contrary, the remaining regimes (BTC high–volatility, ETH high– and low–volatility) are best described by standard GARCH(1,1), which is the GJR model with a zero leverage term γ\gamma. Across regimes, the β\beta coefficients are large and significant, confirming strong volatility persistence. They are somewhat lower in high–volatility states, implying faster mean reversion when markets are stressed. For ETH, persistence in the low–volatility state is very high (large β\beta), while the high–volatility state shows persistence that is lower than BTC’s, suggesting milder clustering in ETH during turbulent periods. Diagnostic checks support the adequacy of the fitted models: across all regimes, the Ljung–Box test on standardized residuals yields p-values above 0.10 (0.1608, 0.9965, 0.9999, 0.7628; Table [2](https://arxiv.org/html/2512.20190v1#S4.T2 "Table 2 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")), so we fail to reject the null of no residual autocorrelation and Engle’s ARCH tests likewise have p-values above 0.10, indicating no remaining ARCH effects. These results are consistent with a broader literature showing that cryptocurrency volatility is regime dependent, heavy–tailed, and sensitive to breaks and jumps found in Charles and Darné [[16](https://arxiv.org/html/2512.20190v1#bib.bib16)], Bouri et al. [[12](https://arxiv.org/html/2512.20190v1#bib.bib12)], Wu [[50](https://arxiv.org/html/2512.20190v1#bib.bib50)], Venter and Maré [[45](https://arxiv.org/html/2512.20190v1#bib.bib45)], Liang et al. [[30](https://arxiv.org/html/2512.20190v1#bib.bib30)]. Taken together, the evidence justifies our regime–specific, skewed–GARCH specification and supports using these regime–conditioned volatilities as inputs to the benchmark pricing step.

Table 2: GARCH results

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | BTC | | ETH | |
| Regime | Regime 0 | Regime 1 | Regime 0 | Regime 1 |
| Interpretation | Low volatility | High volatility | High volatility | Low volatility |
| Specification | GJR–GARCH(1,1,1) | GARCH(1,1) | GARCH(1,1) | GARCH(1,1) |
| AIC | 6785.3842 | 3294.1601 | 3025.3312 | 8079.4733 |
| BIC | 6822.0511 | 3320.5530 | 3050.7008 | 8111.2821 |
| Mean model | | | | |
| μ\mu | 0.2107∗∗ | 0.1197 | 0.3629 | 0.1315 |
|  | (0.0993) | (0.1652) | (0.2269) | (0.0945) |
| Volatility model | | | | |
| ω\omega | 0.1620 | 3.5636∗ | 8.1344∗ | 0.1500 |
|  | (0.5642) | (2.0924) | (4.2226) | (0.2621) |
| α1\alpha\_{1} | 0.1141 | 0.1336∗ | 0.1325∗ | 0.0674∗ |
|  | (0.0714) | (0.0591) | (0.0736) | (0.0397) |
| γ1\gamma\_{1} | -0.0895∗∗∗ |  |  |  |
|  | (0.0255) |  |  |  |
| β1\beta\_{1} | 0.9306∗∗∗ | 0.7304∗∗∗ | 0.6330∗∗∗ | 0.9325∗∗∗ |
|  | (0.1161) | (0.1029) | (0.1429) | (0.0485) |
| Distribution | | | | |
| η\eta | 2.9555∗∗∗ | 2.9625∗∗∗ | 3.2018∗∗∗ | 3.5463∗∗∗ |
|  | (0.4766) | (0.3934) | (0.5555) | (0.3412) |
| λ\lambda | 0.0602 | 0.0054 | 0.0044 | 0.0277 |
|  | (0.0467) | (0.0496) | (0.0539) | (0.0333) |
| Diagnostics | | | | |
| Ljung–Box | 14.2746 | 1.9784 | 0.4306 | 6.5972 |
| pp-value | 0.1608 | 0.9965 | 0.9999 | 0.7628 |
| Engle’s ARCH | 0.8115 | 0.0317 | 0.0287 | 1.3423 |
| pp-value | 0.9999 | 0.9999 | 0.9999 | 0.9993 |

Figures [5](https://arxiv.org/html/2512.20190v1#S4.F5 "Figure 5 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") and [6](https://arxiv.org/html/2512.20190v1#S4.F6 "Figure 6 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") compare two volatility measures for BTC and ETH: the model–implied conditional volatility from the MS–AR–(GJR)–GARCH specification (blue) and a 7-day rolling realized volatility (orange). The rolling series is intentionally very reactive and, therefore, noisy from day to day. On the contrary, the regime–sensitive GARCH path is smoother in normal periods but shows sharper spikes around major market moves. This pattern is expected when volatility is clustered, exhibits regime shifts, and contains jump components. Short windows pick up the transient noise, while regime–dependent models filter that noise yet still respond strongly when the regime changes [[42](https://arxiv.org/html/2512.20190v1#bib.bib42), [7](https://arxiv.org/html/2512.20190v1#bib.bib7), [16](https://arxiv.org/html/2512.20190v1#bib.bib16), [12](https://arxiv.org/html/2512.20190v1#bib.bib12), [50](https://arxiv.org/html/2512.20190v1#bib.bib50)].
In our sample, the ETH path shows taller peaks than BTC, indicating stronger short–run reactions during turbulent intervals. While our setting differs, Andolfatto et al. [[5](https://arxiv.org/html/2512.20190v1#bib.bib5)] likewise document rapid movements in on–chain IV and link them to order–flow pressures on ETH. Overall, the two volatility measures co–move closely and agree on the timing of volatility bursts, but the regime–switching model reduces high–frequency noise and highlights the major episodes, providing a cleaner volatility estimate for benchmark pricing.

Figure 5: Volatility dynamics - BTC

![Refer to caption](figures/vol_comparison_BTC.png)

Figure 6: Volatility dynamics - ETH

![Refer to caption](figures/vol_comparison_ETH.png)

Table [6](https://arxiv.org/html/2512.20190v1#A1.T6 "Table 6 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reports summary statistics for mispricing Δ​pricej\Delta\text{price}\_{j}, defined in equation [3.1](https://arxiv.org/html/2512.20190v1#S1.EGx6 "Step 4: Mispricing measurement ‣ 3.1 Methodology ‣ 3 Empirical analysis ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options"). Because Hegic allows fractional purchases, premiums are first expressed on a per-contract basis so that the ratio is scale-free. Mean mispricing is positive in all samples except for ETH put options, implying that, on average, the BS reference exceeds the Hegic quote (it is lower for ETH put options). Mean levels are smaller for ETH than for wBTC, indicating closer alignment of ETH quotes with the benchmark price. Dispersion is higher for wBTC, especially for call options, as shown by the larger standard deviations. The minima and maxima document occasional large deviations in both directions for both underlyings. Quartiles suggest slightly wider spread for wBTC than for ETH. Distributions are right-skewed, consistent with more observations where the benchmark price is above the Hegic quote. This asymmetry is more pronounced for call options. High kurtosis further indicates fat tails, i.e., infrequent but sizable dislocations, again most evident for call options.

Figure 7: Mispricing - wBTC call options

![Refer to caption](figures/mispricing_BTC_CALL.png)

Figure 8: Mispricing - wBTC put options

![Refer to caption](figures/mispricing_BTC_PUT.png)

Figure 9: Mispricing - ETH call options

![Refer to caption](figures/mispricing_ETH_CALL.png)

Figure 10: Mispricing - ETH put options

![Refer to caption](figures/mispricing_ETH_PUT.png)

Before estimating the FGLS model, we diagnose and preprocess the regressors to avoid spurious conclusion and to make effect sizes comparable across variables. First, we compute a pairwise correlation matrix (figure [16(b)](https://arxiv.org/html/2512.20190v1#A1.F16.sf2 "In Figure 16 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")) and find no severe correlations. For wBTC, most pairs are low with a few moderate entries, e.g., Strike with Type) and, for ETH, moderate correlations appear for Volume with Volatility, which is consistent with higher activity during volatile periods. Second, we assess multicollinearity using variance inflation factors (table [7](https://arxiv.org/html/2512.20190v1#A1.T7 "Table 7 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")), where all VIFs lie below 5, indicating that collinearity is not a concern. Third, to reduce right-skewness and stabilize scale, we take natural logs of strictly non-negative variables, i.e., Amount, Strike, Maturity, and Volume. Finally, to place coefficients on a comparable footing, we standardize all continuous regressors (except dummy variables) to zero mean and unit variance. These transformations are standard in empirical asset-pricing and market-microstructure applications, improving efficiency and interpretability in heteroskedastic cross-sections.444See Campbell et al. [[13](https://arxiv.org/html/2512.20190v1#bib.bib13), pp. 204–210], Wooldridge [[49](https://arxiv.org/html/2512.20190v1#bib.bib49), Ch. 6].

Table [3](https://arxiv.org/html/2512.20190v1#S4.T3 "Table 3 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reports the FGLS estimates for wBTC and ETH options with Newey–West (HAC) standard errors in parentheses and statistical significance with ∗∗∗, ∗∗, ∗, denoting the 1 %1\text{\,}\%, 5 %5\text{\,}\%, and 10 %10\text{\,}\% levels, respectively. Adjusted R2R^{2}, the model FF-statistic, and the Wald statistic are reported as goodness-of-fit measures.
Recall that continuous regressors (Amount, Strike, Maturity, Return, Volume, Volatility) are logs and standardized to zero mean and unit variance, so each slope can be read as the change in mispricing (in %age points) for a one–standard–deviation move in the regressor. Model fit is at the comparable level across underlyings with Adj. R2=0.56R^{2}{=}0.56 for wBTC and 0.500.50 for ETH. Intercepts are negative but statistically insignificant in both markets, indicating no detectable average bias.

For wBTC, Amount, Strike, Maturity, Volume, Volatility, and the Kind dummy are statistically significant. Translating coefficients into US dollars using the mean wBTC call premium (≈$​700\approx\mathdollar 700 according to table [5](https://arxiv.org/html/2512.20190v1#A1.T5 "Table 5 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options")) yields:
(i) Order size coefficient of 0.0228∗⁣∗∗0.0228^{\*\*\*} implies that a 11 s.d. increase in Amount raises the mispricing by about 2.28%2.28\%, i.e., roughly $​16\mathdollar 16 on a $700 option.
(ii) Strike coefficient of 0.0559∗⁣∗∗0.0559^{\*\*\*} adds 5.59%5.59\%, or about $​39\mathdollar 39, consistent with wider prices deviation for further OTM options.
(iii) Maturity coefficient of 0.0166∗0.0166^{\*} adds 1.66%1.66\%, or about $​12\mathdollar 12, indicating slightly larger price spreads for longer maturities.
(iv) Underlying depth (Volume) coefficient of −0.0743∗⁣∗∗-0.0743^{\*\*\*} reduces the price difference by 7.43%7.43\%, or about −$​52-\mathdollar 52, consistent with tighter alignment when market activity is higher.
(v) Volatility coefficient of 0.0789∗⁣∗∗0.0789^{\*\*\*} increases the price deviation by 7.89%7.89\%, or about $​55\mathdollar 55, in line with greater pressure on inventory/oracle channels in turbulent periods.
(vi) Option side (kind) coefficient of −0.0896∗⁣∗∗-0.0896^{\*\*\*} indicates call options are, on average, 8.96%8.96\% closer to the benchmark price than put options (about −$​63-\mathdollar 63 on a $700 premium).

For ETH, only Amount, Volume, and Kind are significant, with signs matching wBTC results where comparable. Using the mean ETH call premium (≈$​673\approx\mathdollar 673) yields:
(i) Order size coefficient of 0.0334∗⁣∗∗0.0334^{\*\*\*} implies an increase in mispricing by +3.34%+3.34\%, or about $​22\mathdollar 22.
(ii) Underlying depth (Volume) coefficient of −0.1353∗⁣∗∗-0.1353^{\*\*\*} implies decrease of−13.53%-13.53\% in the price deviation, or about −$​92-\mathdollar 92, underscoring the role of liquidity.
(iii) Option side (Kind) coefficient of 0.0869∗∗0.0869^{\*\*} indicates call options show about +8.69%+8.69\% larger price difference than put options, i.e., roughly +$​59+\mathdollar 59 on a $673 premium. Coefficients on strike, maturity, return, and volatility are not statistically different from zero in the ETH sample, therefore, and we do not ascribe economic content to them.

The pattern of larger price deviations for bigger orders, further OTM strikes, longer maturities (wBTC), and higher volatility, and smaller deviations when underlying volume is high, is consistent with pooled–liquidity AMM mechanics and oracle frictions documented in prior work [[4](https://arxiv.org/html/2512.20190v1#bib.bib4), [20](https://arxiv.org/html/2512.20190v1#bib.bib20), [37](https://arxiv.org/html/2512.20190v1#bib.bib37), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)].
In practical terms, the estimated effects suggest following calibration opportunities for the protocol. First, introduce an amount slope in the rate schedule so that larger orders pay more, compensating the pool for convexity and inventory pressure. Second, raise OTM rates relative to ATM to reflect greater replication difficulty [[32](https://arxiv.org/html/2512.20190v1#bib.bib32), [36](https://arxiv.org/html/2512.20190v1#bib.bib36)]. Third, allow systemic adjustments to the base rate across maturities, if longer maturities increase collateral and, thus, increase funding needs under full collateralization [[37](https://arxiv.org/html/2512.20190v1#bib.bib37)].
Fourth, link fees (or small rate adjustments) to observed market depth. When liquidity depth is high, reduce fees to bring quotes closer to the benchmark and, when liquidity depth is low, keep fees higher to protect the pool from inventory risk. This aligns with evidence that liquidity conditions shape cross‐exchange price spreads [[27](https://arxiv.org/html/2512.20190v1#bib.bib27), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)].

Table 3: FGLS results

|  |  |  |
| --- | --- | --- |
|  | wBTC options | ETH options |
| Intercept | -0.0213 | -0.2700 |
|  | (0.0512) | (0.1775) |
| Amount | 0.0228∗∗∗ | 0.0334∗∗∗ |
|  | (0.0086) | (0.0107) |
| Strike | 0.0559∗∗∗ | -0.0160 |
|  | (0.0204) | (0.0267) |
| Maturity | 0.0166∗ | -0.0087 |
|  | (0.0094) | (0.0118) |
| Return (underlying) | 0.0005 | -0.0167 |
|  | (0.0082) | (0.0145) |
| Volume (underlying) | -0.0743∗∗∗ | -0.1353∗∗∗ |
|  | (0.0140) | (0.0207) |
| Volatility (underlying) | 0.0789∗∗∗ | -0.0662 |
|  | (0.0230) | (0.0554) |
| Kind | -0.0896∗∗∗ | 0.0869∗∗ |
|  | (0.0337) | (0.0362) |
| Type | 0.0280 | 0.1827 |
|  | (0.0424) | (0.1681) |
| Diagnostics | | |
| Adj. R2R^{2} | 0.5617 | 0.4961 |
| Cond. number | 46.5044 | 38.8960 |
| F-statistic | 39.1036 | 28.5514 |
| pp-value | 0.0000 | 0.0000 |
| Wald-statistic | 312.8189 | 228.3650 |
| pp-value | 0.0000 | 0.0000 |

A key driver of differences between our benchmark price and Hegic quotes is the volatility input used in the pricing. In practice, IV is the standard diagnostic in risk management, forecasting, and option valuation. Accordingly, for each Hegic trade we invert the Black and Scholes [[10](https://arxiv.org/html/2512.20190v1#bib.bib10)] formula with a Brent root–finding to estimate the option’s IV and compare it to the volatility σt\sigma\_{t} from our MS–AR–(GJR)–GARCH model. If IV>σt\text{IV}>\sigma\_{t}, the Hegic quote embeds a volatility premium and, if IV<σt\text{IV}<\sigma\_{t}, it embeds a discount. However, this comparison is not proof of arbitrage, because execution costs, limited depth, and oracle timing can block riskless trades. The possible trading strategies could follow as: when IV<σt\text{IV}<\sigma\_{t} (the option is underpriced relative to our reference), a trader can buy the option on Hegic and form a delta–neutral hedge by shorting Δ\Delta units of the underlying (at spot or futures markets). This isolates the volatility exposure. When IV>σt\text{IV}>\sigma\_{t} (the option is overpriced), the mirror trade is to sell the option and hedge delta. Because Hegic does not allow users to write options, that short leg must be executed off-protocol, or indirectly via liquidity provision into the pool. Related work demonstrates the feasibility of volatility-premium strategies on protocols with two-sided markets [[5](https://arxiv.org/html/2512.20190v1#bib.bib5)]. Frictions in DeFi, e.g., fees, slippage, depth, and oracle update cadence, constrain realized profits in both directions. The IV–σt\sigma\_{t} signal also has clear implications for liquidity providers. If quotes carry a sustained premium (IV>σt\text{IV}>\sigma\_{t}) and realized volatility remains moderate, filled trades tend to deliver higher premia with fewer exercises, benefiting the pool. If quotes carry a discount (IV<σt\text{IV}<\sigma\_{t}), the pool collects too little premium for the convexity it sells and is more exposed when volatility rises.

Figure 11: Volatility difference - wBTC call options

![Refer to caption](figures/vol_difference_BTC_CALL.png)

Figure 12: Volatility difference - wBTC put options

![Refer to caption](figures/vol_difference_BTC_PUT.png)

Figure 13: Volatility difference - ETH call options

![Refer to caption](figures/vol_difference_ETH_CALL.png)

Figure 14: Volatility difference - ETH put options

![Refer to caption](figures/vol_difference_ETH_PUT.png)

In the BS benchmark, we treat volatility estimate as fixed over the life of the option. For Hegic’s short maturities (7–90 days), this is a practical approximation. However, for longer maturities, the volatility estimate can drift if the market switches regimes after trade time. To keep track of this risk, the smoothed probabilities of being in (or moving into) the high–volatility regime can help to identify when a fixed–volatility assumption is more likely to understate future volatiltiy [[42](https://arxiv.org/html/2512.20190v1#bib.bib42), [7](https://arxiv.org/html/2512.20190v1#bib.bib7), [16](https://arxiv.org/html/2512.20190v1#bib.bib16), [12](https://arxiv.org/html/2512.20190v1#bib.bib12), [50](https://arxiv.org/html/2512.20190v1#bib.bib50)]. For each Hegic quote, we invert BS to estimate its IV. Figures [11](https://arxiv.org/html/2512.20190v1#S4.F11 "Figure 11 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options"), [8](https://arxiv.org/html/2512.20190v1#S4.F8 "Figure 8 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options"), [9](https://arxiv.org/html/2512.20190v1#S4.F9 "Figure 9 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") and [10](https://arxiv.org/html/2512.20190v1#S4.F10 "Figure 10 ‣ 4 Results ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") plot IV−σt\text{IV}-\sigma\_{t} by strike, and table [8](https://arxiv.org/html/2512.20190v1#A1.T8 "Table 8 ‣ Appendix A Appendix ‣ Pricing of wrapped Bitcoin and Ethereum on-chain options") reports its summary statistics. For wBTC, call option differences have a slightly negative mean (about −0.02-0.02), so IV is, on average, a bit below σt\sigma\_{t}; put options are also slightly negative and very close to zero (tighter alignment). For ETH, call option differences are near zero on average (slightly negative), while put option differences are positive on average (about +0.05+0.05) with occasional large positive outliers (maximum around 0.910.91). Dispersion and tails are larger for ETH (especially on puts) consistent with stronger sensitivity to market spikes and with evidence that on–chain ETH option metrics respond more to changing conditions [[5](https://arxiv.org/html/2512.20190v1#bib.bib5)].

These IV−σt\text{IV}-\sigma\_{t} diagnostics indicate where a delta–neutral long– (if IV<σt\text{IV}<\sigma\_{t}) or short–volatility strategy (if IV>σt\text{IV}>\sigma\_{t}) would be possible, subject to the practical limits noted above.
A delta–neutral position removes first–order exposure to the underlying and turns the trade into a bet on the spread between the volatility embedded in the option’s price (IV) and the volatility the market will actually realize over the life of the contract. In continuous time, the P&L of a delta–hedged option decomposes into gains from gamma (which scale with realized variance) minus theta (time decay), plus trading frictions. Therefore, a long option with frequent hedging earns on average if realized volatility exceeds the level implied by IV, and loses if realized variance is lower [[24](https://arxiv.org/html/2512.20190v1#bib.bib24), chap. 20]. In our setting, when IV<σt\text{IV}<\sigma\_{t}, buying the option on Hegic and delta–hedging in spot/futures is expected to have positive gain. When IV>σt\text{IV}>\sigma\_{t}, the opposite trade would have positive gain, though that short leg must be placed off–protocol or approximated via liquidity provision. The size of any premium is bounded by discrete hedging error, funding costs for the hedge, exchange fees, slippage, and oracle/update latency. These frictions rise in stressed markets and can overturn profits even when the IV–σt\sigma\_{t} signal is favorable [[3](https://arxiv.org/html/2512.20190v1#bib.bib3), [40](https://arxiv.org/html/2512.20190v1#bib.bib40), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)].

## 5 Conclusion

This paper studies on–chain option pricing on Hegic using transaction–level data for wBTC and ETH on Arbitrum chain (October 24, 2022 to May 21, 2024) and a BS reference price with a regime–sensitive volatility. Three results are robust across specifications. First, mispricing co–moves positively with order size and negatively with underlying trading volume in both markets. For wBTC it also increases with strike, maturity, and volatility, while the corresponding ETH coefficients are statistically indistinguishable from zero. Second, the kind (call vs. put) effect is significant with opposite signs across underlyings, indicating side–specific pressure that is protocol– and state–dependent.
The cross–section analysis offers calibration levers that preserve Hegic’s rate–based quoting while improving price quality. (i) Introduce a size–dependent increase so that larger trades pay a higher effective rate, compensating pooled writers for inventory and convexity pressure. (ii) Raise rates for OTM strikes relative to ATM to reflect tougher replication and thinner markets[[32](https://arxiv.org/html/2512.20190v1#bib.bib32), [36](https://arxiv.org/html/2512.20190v1#bib.bib36)]. (iii) Apply rate adjustment for longer maturities to acknowledge capital being locked up longer under full collateralization [[37](https://arxiv.org/html/2512.20190v1#bib.bib37)]. (iv) Condition fees on observed market liquidity depth so that deviations narrow when liquidity is high [[27](https://arxiv.org/html/2512.20190v1#bib.bib27), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)]. These rules can be made explicit, monitored on–chain, and governed transparently.

For traders, the comparison of IV with the MS–GARCH volatility σt\sigma\_{t} serves as a standard level diagnostic rather than an arbitrage proof. When IV<σt\text{IV}<\sigma\_{t}, a delta–hedged long isolates volatility exposure and, when IV>σt\text{IV}>\sigma\_{t}, the natural short–vol leg must be implemented off–protocol or approximated via liquidity provision, since end–users cannot write on Hegic [[48](https://arxiv.org/html/2512.20190v1#bib.bib48), [39](https://arxiv.org/html/2512.20190v1#bib.bib39), [5](https://arxiv.org/html/2512.20190v1#bib.bib5)]. Realized outcomes depend on fees, slippage, liquidity depth, and jump risk during rebalancing [[3](https://arxiv.org/html/2512.20190v1#bib.bib3), [40](https://arxiv.org/html/2512.20190v1#bib.bib40), [44](https://arxiv.org/html/2512.20190v1#bib.bib44)]. For liquidity providers, sustained IV premia (IV>σt>\sigma\_{t}) with moderate realized variance raise expected premia retention and sustained discounts (IV<σt<\sigma\_{t}) do the opposite. Because the pool is the sole writer, buying options from the pool mainly internalizes part of one’s own short–gamma risk and is not a free gain. Practical risk management as monitoring IV–σt\sigma\_{t} spreads, utilization, oracle latency, and depth, helps to adjust utilization caps and inventory tolerances when spreads increases and liquidity depth decreases.

Policymakers and standard setters should adopt a disclosure standard for DeFi option AMMs that mandates oracle transparency to publicly report update thresholds, expected latencies, and fallback logic. There should be a requirement of routine reporting of liquidity and utilization, queuing dynamics, and any withdrawal gates. Additionally, the disclosure standard should provide user-facing risk notices on short-maturity convexity and the transaction costs of delta-hedged strategies. Event-triggered updates, e.g., during volatility spikes or oracle incidents, should be required to keep these disclosures relevant. This technology standard can improve price formation, reduce timing and funding uncertainty, and lower the risk that observed price differences are misread as informational inefficiency when they primarily reflect market structure.

It is important to clarify that our price estimates serve as a model-based benchmark rather than a definitive true price. Our valuation method uses the BS model with a regime-sensitive volatility, a practical approach for short-maturity options in emerging environments [[45](https://arxiv.org/html/2512.20190v1#bib.bib45)]. However, this model has several limitations. It intentionally omits complex features like jump–diffusion and stochastic volatility over the live time of options. Consequently, in market states where these factors are significant, our calculated option values may be systematically biased.
The identification of this study is cross-sectional and conditional. Therefore, the reported results should be interpreted as local associations. Furthermore, the model abstracts from critical market design features and frictions. We do not account for AMM inventory and fee mechanics, execution costs, collateral and stablecoin risks, or cross-chain bridge delays. As a result, what may appear as mispricings could reflect these microstructure frictions rather than pure risk premia.
The external validity of our findings is also limited. Significant differences in fees, margin requirements, and settlement conventions between centralized and decentralized exchanges make cross-market comparisons difficult without controlling for microstructure effects.
The limitations of this study suggest several avenues for future research. Subsequent work could extend the analysis to protocols that permit end-user shorting to test the role of inventory constraints. To better separate risk premia from execution costs, future studies could incorporate real-time, cross-exchange hedging frictions. To assess the stability of the results, it could be of advantage to test alternative regime specifications and look-back windows for the volatility estimation [[50](https://arxiv.org/html/2512.20190v1#bib.bib50), [30](https://arxiv.org/html/2512.20190v1#bib.bib30)].
To sum up, while our evidence provides a coherent benchmark under its stated assumptions, it should not be interpreted as establishing causal effects or unique market prices.

For Hegic protocol, economically meaningful and directionally coherent links between mispricing and order size, moneyness, maturity (for wBTC), volatility (for wBTC), and liquidity, point to design and state variable as first–order drivers of on–chain option pricing. The design recommendations above provide immediately actionable calibration targets for developers, the IV–σt\sigma\_{t} diagnostic and delta–neutral hedge opportunities provide practical decision rules for traders and liquidity providers. Together, these steps can narrow systematic price deviations while retaining the simplicity and composability that make on–chain option AMMs attractive.

## References

* \bibcommenthead
* 0xAlpha et al. [2021]

  0xAlpha, Fang D, Chen R (2021) The exchange protocol of everlasting options. Working paper
* 0xAlpha et al. [2023]

  0xAlpha, Fang D, Chen R (2023) Deri v4: A cross-chain decentralized protocol of derivatives. Working paper
* Akyildirim et al. [2020]

  Akyildirim E, Corbet S, Katsiampa P, et al (2020) The development of bitcoin futures: Exploring the interactions between cryptocurrency derivatives. Finance Research Letters 34. [10.1016/j.frl.2019.07.007](https:/doi.org/10.1016/j.frl.2019.07.007)
* Alexander et al. [2023]

  Alexander C, Chen D, Imeraj A (2023) Crypto quanto and inverse options. Mathematical Finance 33(4):1005–1043. [10.1111/mafi.12410](https:/doi.org/10.1111/mafi.12410)
* Andolfatto et al. [2024]

  Andolfatto A, Naik S, Schoenleber L (2024) Decentralized and centralized options trading: A risk premia perspective. Working paper
* Ante et al. [2023]

  Ante L, Fiedler I, Willruth JM, et al (2023) A systematic literature review of empirical research on stablecoins. FinTec 2:34–47. [10.3390/fintech2010003](https:/doi.org/10.3390/fintech2010003)
* Ardia et al. [2019]

  Ardia D, Bluteau K, Rüede M (2019) Regime changes in bitcoin garch volatility dynamics. Finance Research Letters 29:266–271. [10.1016/j.frl.2018.08.009](https:/doi.org/10.1016/j.frl.2018.08.009)
* Aslam et al. [2023]

  Aslam F, Memon BA, Hunjra AI, et al (2023) The dynamics of market efficiency of major cryptocurrencies. Global Finance Journal 58. [10.1016/j.gfj.2023.100899](https:/doi.org/10.1016/j.gfj.2023.100899)
* Bariviera [2017]

  Bariviera AF (2017) The inefficiency of bitcoin revisited: A dynamic approach. Economic Letters 161:1–4. [10.1016/j.econlet.2017.09.013](https:/doi.org/10.1016/j.econlet.2017.09.013)
* Black and Scholes [1973]

  Black F, Scholes M (1973) The pricing of options and corporate liabilities. Journal of Political Economy 81(3):637–654. [10.1086/260062](https:/doi.org/10.1086/260062)
* Bouri et al. [2017]

  Bouri E, Azzi G, Dyhrberg AH (2017) On the return-volatility relationship in the bitcoin market around the price crash of 2013. Economics 11(1). [10.5018/economics-ejournal.ja.2017-2](https:/doi.org/10.5018/economics-ejournal.ja.2017-2)
* Bouri et al. [2019]

  Bouri E, Gil‐Alana LA, Gupta R, et al (2019) Modelling long memory volatility in the bitcoin market: Evidence of persistence and structural breaks. International Journal of Finance and Economics 24(1):412–426
* Campbell et al. [1997]

  Campbell JY, Lo AW, MacKinlay AC (1997) The Econometrics of Financial Markets. Princeton University Press
* Cao [2001]

  Cao M (2001) Systematic jump risks in a small open economy: simultaneous equilibrium valuation of options on the market portfolio and the exchange rate. Journal of International Money and Finance 2:191–218. [10.1016/S0261-5606(00)00053-X](https:/doi.org/10.1016/S0261-5606(00)00053-X)
* Cao and Celik [2021]

  Cao M, Celik B (2021) Valuation of bitcoin options. Journal of Futures Markets 41(7):1007–1026. [10.1002/fut.22214](https:/doi.org/10.1002/fut.22214)
* Charles and Darné [2019]

  Charles A, Darné O (2019) Volatility estimation for cryptocurrencies: Further evidence with jumps and structural breaks. Economics Bulletin 39(2):954–968
* Chen et al. [2020]

  Chen CYH, Härdle WK, Hou AJ, et al (2020) Pricing cryptocurrency options. Journal of Financial Econometrics 18(2):250–279. [10.1093/jjfinec/nbaa006](https:/doi.org/10.1093/jjfinec/nbaa006)
* Dawson et al. [2023]

  Dawson S, Romanowski D, Cheng A, et al (2023) Lyra v2. Working paper
* DeFiLlama [2025]

  DeFiLlama (2025) Defillama option protocols. <https://defillama.com/protocols/Options>, accessed during the sample window; TVL fluctuates over time.
* Eskandari et al. [2017]

  Eskandari S, Clark J, Sundaresan V, et al (2017) On the feasibility of decentralized derivatives markets. In International Conference on Financial Cryptography and Data Security pp 553–567. [10.1007/978-3-319-70278-0\_35](https:/doi.org/10.1007/978-3-319-70278-0_35)
* Fernandes et al. [2022]

  Fernandes LH, Bouri E, Silva JW, et al (2022) The resilience of cryptocurrency market efficiency to covid-19 shock. Physica A: Statistical Mechanics and its Applications 607. [10.1016/j.physa.2022.128218](https:/doi.org/10.1016/j.physa.2022.128218)
* Fu [2023]

  Fu F (2023) Sok: Decentralized exchanges (dex) with automated market maker (amm) protocols. ACM Computing Surveys 55(11):1–50. [10.1145/3570639](https:/doi.org/10.1145/3570639)
* Glosten and R. Jagannathan [1993]

  Glosten LR, R. Jagannathan DER (1993) On the relation between the expected value and the volatility of the nominal excess return on stocks. Journal of Finance 48(5):1779–1801. [10.1111/j.1540-6261.1993.tb05128.x](https:/doi.org/10.1111/j.1540-6261.1993.tb05128.x)
* Hull [2012]

  Hull JC (2012) Options, Futures, and Other Derivatives, 8th edn. Prentice Hall
* Katsiampa [2017]

  Katsiampa P (2017) Volatility estimation for bitcoin: A comparison of garch models. Economics Letters 158:3–6. [10.1016/j.econlet.2017.06.023](https:/doi.org/10.1016/j.econlet.2017.06.023)
* Keilbar and Zhang [2021]

  Keilbar G, Zhang Y (2021) On cointegration and cryptocurrency dynamics. Digital Finance 3(1):1–23. [10.1007/s42521-021-00027-5](https:/doi.org/10.1007/s42521-021-00027-5)
* Kristoufek and Bouri [2023]

  Kristoufek L, Bouri E (2023) Exploring sources of statistical arbitrage opportunities among bitcoin exchanges. Finance Research Letters 51. [10.1016/j.frl.2022.103332](https:/doi.org/10.1016/j.frl.2022.103332)
* Kyriazis et al. [2019]

  Kyriazis NA, Daskalou K, Arampatzis M, et al (2019) Estimating the volatility of cryptocurrencies during bearish markets by employing garch models. Heliyon 5(8). URL <https://www.cell.com/heliyon/fulltext/S2405-8440(19)35899-2>
* Leung and Nguyen [2019]

  Leung T, Nguyen H (2019) Constructing cointegrated cryptocurrency portfolios for statistical arbitrage. Studies in Economics and Finance 36(4):581–599. [10.1108/SEF-08-2018-0264](https:/doi.org/10.1108/SEF-08-2018-0264)
* Liang et al. [2022]

  Liang C, Zhang Y, Li X, et al (2022) Which predictor is more predictive for bitcoin volatility? and why? International Journal of Finance and Economics 27(2):1947–1961. [10.1002/ijfe.2252](https:/doi.org/10.1002/ijfe.2252)
* López-Martín et al. [2021]

  López-Martín C, Muela SB, Arguedas R (2021) Efficiency in cryptocurrency markets: New evidence. Eurasian Economic Review 11(3). [10.1007/s40822-021-00182-5](https:/doi.org/10.1007/s40822-021-00182-5)
* Madan et al. [2019]

  Madan DB, Reyners S, Schoutens W (2019) Advanced model calibration on bitcoin options. Digital Finance 1(1):117–137. [10.1007/s42521-019-00002-1](https:/doi.org/10.1007/s42521-019-00002-1)
* McCorry et al. [2021]

  McCorry P, Buckland C, Yee B, et al (2021) Sok: Validating bridges as a scaling solution for blockchains. Cryptology ePrint Archive pp 1–46. URL <https://eprint.iacr.org/2021/1589>
* Mokni et al. [2025]

  Mokni K, Montasser GE, Ajmi AN, et al (2025) On the efficiency and its drivers in the cryptocurrency market: the case of bitcoin and ethereum. In Blockchain, Crypto Assets, and Financial Innovation: A Decade of Insights and Advances 162-191. [10.1007/978-981-96-6839-7\_6](https:/doi.org/10.1007/978-981-96-6839-7_6)
* Newey and West [1987]

  Newey W, West K (1987) A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica 55(3):703–708. URL <https://core.ac.uk/download/pdf/6894872.pdf>
* Olivares [2020]

  Olivares P (2020) Pricing bitcoin derivatives under jump-diffusion models. arXiv preprint [10.48550/arXiv.2002.07117](https:/doi.org/10.48550/arXiv.2002.07117)
* Priem [2022]

  Priem R (2022) Blockchains and otc derivatives markets: A possible combination? Working paper [10.2139/ssrn.4286043](https:/doi.org/10.2139/ssrn.4286043)
* Qin et al. [2021]

  Qin K, Zhou L, Afonin Y, et al (2021) Cefi vs. defi – comparing centralized to decentralized finance. arXiv: Quantitative Finance [10.48550/arXiv.2106.08157](https:/doi.org/10.48550/arXiv.2106.08157)
* Rahman et al. [2022]

  Rahman A, Shi V, Ding M, et al (2022) Sok: Synthetic assests, derivatives, and on-chain portfolio management. arXiv: Quantitative Finance 55(3):1–1. [10.48550/arXiv.2209.09958](https:/doi.org/10.48550/arXiv.2209.09958)
* Sebastião and Godinho [2020]

  Sebastião H, Godinho P (2020) Bitcoin futures: An effective tool for hedging cryptocurrencies. Finance Research Letters 33. [10.1016/j.frl.2019.07.003](https:/doi.org/10.1016/j.frl.2019.07.003)
* Stavroyiannis [2018]

  Stavroyiannis S (2018) Value-at-risk and related measures for the bitcoin. Journal of Risk Finance 19:127–136. [10.1016/j.econlet.2017.06.023](https:/doi.org/10.1016/j.econlet.2017.06.023)
* Thies and Molnár [2018]

  Thies S, Molnár P (2018) Bayesian change point analysis of bitcoin returns. Finance Research Letters 27:223–227. [10.1016/j.frl.2018.03.018](https:/doi.org/10.1016/j.frl.2018.03.018)
* Tran and Leirvik [2020]

  Tran VL, Leirvik T (2020) Efficiency in the markets of crypto-currencies. Finance Research Letters 55. [10.1016/j.frl.2019.101382](https:/doi.org/10.1016/j.frl.2019.101382)
* Vakhmyanin and Volkovich [2023]

  Vakhmyanin I, Volkovich Y (2023) Price arbitrage for defi derivatives. In 2023 IEEE International Conference on Blockchain and Cryptocurrency pp 1–4. [10.1109/ICBC56567.2023.10174884](https:/doi.org/10.1109/ICBC56567.2023.10174884)
* Venter and Maré [2020]

  Venter PJ, Maré E (2020) Garch generated volatility indices of bitcoin and crix. Journal of Risk and Financial Management 13(6). [10.3390/jrfm13060121](https:/doi.org/10.3390/jrfm13060121)
* Werner et al. [2022]

  Werner S, Perez D, Gudgeona L, et al (2022) Sok: Decentralized finance (defi). In Proceedings of the 4th ACM Conference on Advances in Financial Technologies 127:30–46. [10.1145/3558535.3559780](https:/doi.org/10.1145/3558535.3559780)
* White [1980]

  White H (1980) A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity. Econometrica 48(4):817–838. [10.2307/1912934](https:/doi.org/10.2307/1912934)
* Wintermute [2020]

  Wintermute M (2020) Hegic: On-chain options trading protocol on ethereum powered by hedge contracts and liquidity pools. Working paper
* Wooldridge [2010]

  Wooldridge JY (2010) Econometric Analysis of Cross Section and Panel Data. The MIT Press
* Wu [2021]

  Wu C (2021) Window effect with markov-switching garch model in cryptocurrency market. Chaos, Solitons & Fractals 146. [10.1016/j.chaos.2021.110902](https:/doi.org/10.1016/j.chaos.2021.110902)

## Appendix A Appendix

An appendix contains supplementary information that is not an essential part of the text itself but which may be helpful in providing a more comprehensive understanding of the research problem or it is information that is too cumbersome to be included in the body of the paper.

Table 4: Descriptive statistics of underlyings

|  | BTC | ETH |
| --- | --- | --- |
| Mean | 0.14910.1491 | 0.18490.1849 |
| Std Deviation | 3.58753.5875 | 4.60914.6091 |
| Min | −47.9934-47.9934 | −56.9506-56.9506 |
| 25 %25\text{\,}\%-Quartile | −1.3578-1.3578 | −1.8478-1.8478 |
| 50 %50\text{\,}\%-Quartile | 0.07780.0778 | 0.12040.1204 |
| 75 %75\text{\,}\%-Quartile | 1.72331.7233 | 2.34792.3479 |
| Max | 17.791317.7913 | 23.348023.3480 |
| Skewness | −1.1730-1.1730 | −1.1068-1.1068 |
| Kurtosis | 21.485721.4857 | 18.179218.1792 |




Table 5: Descriptive statistics of options

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Amount | Premium Paid | Strike | Maturity | Moneyness |
| Call options — wBTC (nn = 723723) | | | | | |
| Mean | 1.38061.3806 | 699.5291699.5291 | 29 064.775629\,064.7756 | 1717 | 0.94950.9495 |
| Std Deviation | 4.57864.5786 | 2253.80082253.8008 | 13 989.111713\,989.1117 | 2121 | 0.05770.0577 |
| Min | 0.00000.0000 | 0.01860.0186 | 15 574.247015\,574.2470 | 77 | 0.76920.7692 |
| 25 %25\text{\,}\%-Quartile | 0.03500.0350 | 15.899915.8999 | 19 952.660819\,952.6608 | 77 | 0.90910.9091 |
| 50 %50\text{\,}\%-Quartile | 0.15000.1500 | 47.000047.0000 | 24 312.810024\,312.8100 | 77 | 1.00001.0000 |
| 75 %75\text{\,}\%-Quartile | 0.50000.5000 | 366.7770366.7770 | 29 814.156129\,814.1561 | 1515 | 1.00001.0000 |
| Max | 53.500053.5000 | 28 075.924228\,075.9242 | 78 565.229978\,565.2299 | 9090 | 1.00001.0000 |
| Put options — wBTC (nn = 592592) | | | | | |
| Mean | 0.62320.6232 | 559.0408559.0408 | 28 933.044728\,933.0447 | 1919 | 1.04261.0426 |
| Std Deviation | 1.52821.5282 | 2236.63102236.6310 | 13 319.597513\,319.5975 | 2020 | 0.06960.0696 |
| Min | 0.00010.0001 | 0.10850.1085 | 11 362.704511\,362.7045 | 77 | 1.00001.0000 |
| 25 %25\text{\,}\%-Quartile | 0.02500.0250 | 22.797322.7973 | 20 540.606820\,540.6068 | 77 | 1.00001.0000 |
| 50 %50\text{\,}\%-Quartile | 0.10000.1000 | 70.312570.3125 | 25 603.150025\,603.1500 | 1010 | 1.00001.0000 |
| 75 %75\text{\,}\%-Quartile | 0.50000.5000 | 268.8343268.8343 | 30 303.977530\,303.9775 | 2626 | 1.11111.1111 |
| Max | 15.000015.0000 | 39 551.547139\,551.5471 | 72 142.147072\,142.1470 | 9090 | 1.42861.4286 |
| Call options — ETH (nn = 16641664) | | | | | |
| Mean | 9.36639.3663 | 673.4381673.4381 | 1943.76151943.7615 | 2222 | 0.96510.9651 |
| Std Deviation | 22.231922.2319 | 1894.17411894.1741 | 617.8966617.8966 | 2424 | 0.05670.0567 |
| Min | 0.00000.0000 | 0.00000.0000 | 1089.41591089.4159 | 77 | 0.76920.7692 |
| 25 %25\text{\,}\%-Quartile | 0.25000.2500 | 11.765311.7653 | 1572.74111572.7411 | 77 | 0.90910.9091 |
| 50 %50\text{\,}\%-Quartile | 1.13951.1395 | 83.715983.7159 | 1790.06981790.0698 | 1414 | 1.00001.0000 |
| 75 %75\text{\,}\%-Quartile | 8.00008.0000 | 494.0209494.0209 | 2091.92562091.9256 | 2626 | 1.00001.0000 |
| Max | 264.0000264.0000 | 24 372.627024\,372.6270 | 4457.61314457.6131 | 9090 | 1.00001.0000 |
| Put options — ETH (nn = 11111111) | | | | | |
| Mean | 12.400212.4002 | 626.3159626.3159 | 1636.46351636.4635 | 1919 | 1.06721.0672 |
| Std Deviation | 33.419533.4195 | 1963.53211963.5321 | 458.8686458.8686 | 2020 | 0.09690.0969 |
| Min | 0.00010.0001 | 0.00200.0020 | 811.7060811.7060 | 77 | 1.00001.0000 |
| 25 %25\text{\,}\%-Quartile | 1.00001.0000 | 19.941219.9412 | 1398.36431398.3643 | 77 | 1.00001.0000 |
| 50 %50\text{\,}\%-Quartile | 2.00002.0000 | 99.466799.4667 | 1590.49261590.4926 | 1010 | 1.00001.0000 |
| 75 %75\text{\,}\%-Quartile | 10.000010.0000 | 474.4329474.4329 | 1801.49491801.4949 | 2121 | 1.11111.1111 |
| Max | 516.0000516.0000 | 34 994.259834\,994.2598 | 4043.22004043.2200 | 9090 | 1.42861.4286 |




Table 6: Descriptive statistics of mispricing

|  | wBTC | | ETH | |
| --- | --- | --- | --- | --- |
|  | Call options | Put options | Call options | Put options |
| Mean | 0.17505 | 0.02490 | 0.09730 | -0.06450 |
| Std Deviation | 0.67728 | 0.39620 | 0.42850 | 0.35810 |
| Min | -0.99617 | -0.99410 | -0.98750 | -0.99990 |
| 25 %25\text{\,}\%-Quartile | -0.17070 | -0.20700 | -0.12600 | -0.27320 |
| 50 %50\text{\,}\%-Quartile | 0.05200 | 0.01050 | 0.06310 | -0.02430 |
| 75 %75\text{\,}\%-Quartile | 0.31120 | 0.27020 | 0.24370 | 0.13890 |
| Max | 4.58930 | 1.41200 | 4.29980 | 2.05460 |
| Skewness | 2.77620 | 0.33981 | 2.23161 | 0.14577 |
| Kurtosis | 13.82080 | 4.00729 | 14.96550 | 5.24340 |




Table 7: Variance inflation factor

|  | wBTC | ETH |
| --- | --- | --- |
| Intercept | 4.6253 | 4.4292 |
| Amount | 1.1222 | 1.0892 |
| Strike | 1.4042 | 1.2357 |
| Maturity | 1.1429 | 1.1200 |
| Return | 1.0434 | 1.0505 |
| Volume | 1.2593 | 1.4251 |
| Volatility | 1.1175 | 1.3186 |
| Kind | 1.0420 | 1.1032 |
| Type | 1.2932 | 1.1450 |




Table 8: Descriptive statistics of volatility differences

|  | BTC | | ETH | |
| --- | --- | --- | --- | --- |
|  | Call options | Put options | Call options | Put options |
| Mean | -0.0194 | -0.0055 | -0.0074 | 0.0484 |
| Std Deviation | 0.1432 | 0.1542 | 0.1643 | 0.1849 |
| Min | -0.5074 | -0.4451 | -0.6082 | -0.5378 |
| 25 %25\text{\,}\%-Quartile | -0.1036 | -0.1145 | -0.0920 | -0.0598 |
| 50 %50\text{\,}\%-Quartile | -0.0171 | -0.0047 | -0.0276 | 0.0084 |
| 75 %75\text{\,}\%-Quartile | 0.0627 | 0.0936 | 0.0604 | 0.1269 |
| Max | 0.4749 | 0.7154 | 0.8252 | 0.9127 |
| Skewness | 0.1700 | 0.3819 | 0.4054 | 1.2628 |
| Kurtosis | 3.7762 | 4.4548 | 5.8807 | 6.4725 |




Figure 15: PACF

![Refer to caption](figures/pacf_Bitcoin_Price.png)


(a) BTC

![Refer to caption](figures/pacf_Ethereum_Price.png)


(b) ETH




Figure 16: Correlation matrices.

![Refer to caption](figures/correlation_BTC.png)


(a) wBTC

![Refer to caption](figures/correlation_ETH.png)


(b) ETH