---
authors:
- Sunghun Ko
- Jinsuk Park
doc_id: arxiv:2512.23386v1
family_id: arxiv:2512.23386
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Impact of Volatility on Time-Based Transaction Ordering Policies
url_abs: http://arxiv.org/abs/2512.23386v1
url_html: https://arxiv.org/html/2512.23386v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ko Sunghun
  
Jinsuk Park

###### Abstract

We study Arbitrum’s *Express Lane Auction* (ELA), an ahead-of-time second-price auction that grants the winner an exclusive latency advantage for one minute. Building on a single-round model with risk-averse bidders, we propose a hypothesis that the value of priority access is discounted relative to risk-neutral valuation due to the difficulty of forecasting short-horizon volatility and bidders’ risk aversion. We test these predictions using ELA bid records matched to high-frequency ETH prices and find that the result is consistent with the model.

## 1 Introduction

### 1.1 Background

Timeboost, a novel transaction ordering policy introduced in [mamageishvili2023buying] and subsequently implemented by Offchain Labs, has recently been deployed on the Arbitrum mainnet [offchainlabs2025timeboost]. Under the Timeboost policy, transactions are delivered to the sequencer through two distinct channels: the normal lane and the Express Lane (EL). While the sequencer processes transactions in a First-In, First-Out (FIFO) manner, transactions submitted via the normal lane incur a 200200-millisecond delay before being forwarded to the sequencer. Conversely, the EL immediately forwards received transactions, thereby offering its users a 200200-millisecond latency advantage.

The temporary right to utilize the EL is periodically allocated for each round—which lasts for one minute—via a second-price sealed-bid auction termed the *Express Lane Auction (ELA)*111The winner may elect to either exclusively utilize this access or to share and resell it to other parties. For instance, [kairossubauction] is currently running a secondary market that resells the EL access.. This auction operates on an ahead-of-time basis; participants in the ELA are required to estimate the value of the good (the right to use the EL in the forthcoming round), submit their bids, and pay if they win, prior to exercising their EL access. Given that the latency differential is barely noticeable to typical users, participation and bidding in the ELA are primarily confined to latency-sensitive players, such as High-Frequency Traders (HFTs). The primary objective of this mechanism is to capture a portion of the Maximal Extractable Value (MEV) generated, without compromising the experience of the typical user, by imposing charges solely on strategic players, frequently referred to as *searchers*.

Searchers value access to EL due to the 200-millisecond latency advantage, which is typically sufficient to secure the majority of CEX-DEX arbitrage opportunities for each arbitrage oppportunities222This does not universally hold true. For instance, if the latency advantage is insufficiently large, a probabilistic strategy involving transaction spamming can still capture a non-negligible portion of opportunities. For further details, refer to [akaki2025blind]. Generally, a 200200-millisecond gap is considered big enough to mitigate such possibilities.. Given that CEX-DEX arbitrage profit is directly proportional to the integrated variance I​V(≡∫0Tσt2​𝑑t)IV(\equiv\int^{T}\_{0}\sigma^{2}\_{t}dt) of risky assets, bidding in ELA yields a payoff analogous to a long position in a variance swap. Previous research has identified a discount in variance swap markets, termed the *Variance Risk Premium (VRP)*, which represents the discrepancy between the theoretical fair price (derived from a replicating portfolio) and the observed market price. Studies such as [bollerslev2009expected] and [carr2009variance] attribute the existence of VRP to the stochastic nature of volatility and traders’ risk aversion. Consequently, a similar question arises for ELA: do bidders submit bids below the expected CEX-DEX arbitrage profit for an upcoming round? This study addresses questions concerning the factors influencing Timeboost’s performance and their impact, including the aforementioned phenomenon.

More specifically, we endeavor to answer the following research questions: *(i)* Does a discount analogous to VRP exist in ELA? *(ii)* If such a discount exists, what is its primary causal mechanism? and *(iii)* What is the intensity of this discount effect?

Our findings indicate that *(i)* a comparable discount does exist, and *(ii)* it is consistent with the inherent difficulty in forecasting the future volatility of risky assets within a short time horizon. We also provide an estimation of the intensity of this effect.

This study is one of the first empirical investigations into the performance of Timeboost, examining the determinants of bidder valuations and the efficacy of express lane auctions. As such, it establishes a foundational reference for subsequent research that employs more sophisticated methodologies and realistic assumptions. Ultimately, this investigation seeks to enhance the understanding of time-based sequencing mechanisms, including Timeboost, within auction frameworks.

![Refer to caption](x1.png)


Figure 1: Cumulative revenue of Timeboost through express lane auction from May to October.

### 1.2 Related Literature

#### Loss-versus-rebalancing and CEX-DEX Arbitrage.

Following the foundational work of [daian2019flash], which introduced the term Maximal Extractable Value (MEV), a substantial body of literature has emerged exploring both its theoretical and empirical aspects. Early on, both academia and practitioners recognized CEX-DEX arbitrage as the primary source of MEV, commonly measured using short-term (≤5\leq 5 minutes) markouts [wu2025measuring, gogol2024cross, heimbach2024non, oz2025pandora, followupuniv3, usageofmarkout]. Subsequently, [milionis2022automated] provided a theoretical justification for such a metric and introduced Loss-Versus-Rebalancing (LVR), which has been generalized to more realistic settings in later works, including [milionis2024automated] and [nezlobin2025loss]. These studies, while differing in their specific details, consistently demonstrate a close relationship between CEX-DEX arbitrage and LVR, which represents the adverse selection cost borne by Automated Market Makers (AMMs). After abstracting away fees, gas costs, and inventory risk, the leading term of this relationship is shown to be 𝒪​(σ2)\mathcal{O}(\sigma^{2}), where σ\sigma denotes the instantaneous volatility of the asset price.

#### Time-based Transaction Ordering Policies and Timeboost.

Even before the advent of blockchain technology, time-based transaction ordering policies and associated products were well established and widely adopted. For instance, since the late 20002000s, traditional finance (TradFi) exchanges have commercialized latency, offering “speed technology” to high-frequency trading (HFT) firms, generating revenues exceeding $ 700700 million in 20172017 [budish2024theory]. The impact of asymmetric speed bumps and micro-burst fees, exemplifying such exotic transaction ordering policies (priority rules), has been investigated by [Aoyagi\_2025] and [brolley2023liquid]. Timeboost, as introduced in [mamageishvili2023buying], aligns with these policies, and [akaki2025blind] and [fritsch2024mev] provide a comprehensive theoretical understanding of its mechanisms. While Timeboost generated over 14001400 ETH in revenue from May to October, demonstrating its effectiveness, empirical research in this area remains nascent, with [messias2025express] and [mamageishvili2025timeboostaheadoftimeauctionswork] among the pioneering works that explore bidder behavior in ELA and the performance of Timeboost. In particular, the latter work claimed that the bidders’ bids can be used as a noisy proxy for the markout of arbitrageurs’ trades in the subsequent round.

#### Variance Risk Premia and Risk Aversion.

A large body of literature documents a systematic wedge between the replication-based (risk-neutral) fair value of a variance swap and its traded price, commonly referred to as the variance (or volatility) risk premium (VRP). The “fair” strike for variance swap can be synthesized from an option strip [demeterfi1999guide] or via model‐free implied variance [jiang2005modelfree], and the VRP is typically measured as implied minus subsequently realized variance (RV\mathrm{RV}) [carr2009variance]. Empirically, this wedge is time-varying and (on average) negative, consistent with investors’ risk aversion and a stochastic nature of volatility that loads on variance and tail risks [bakshi2003delta, bollerslev2009expected, broadie2007model, bollerslev2011tails]. Beyond level effects, the term structure and composition of premia matter as well: short-horizon variance premia are especially volatile and command higher compensation, and downside (“bad”) variance carries a larger premium than upside variance [dewbecker2017price, aitsahalia2020term, feunou2018downside]. The phenomenon is not equity‐specific: analogous variance premia appear in foreign exchange (FX) and commodity markets, indicating a broad, asset-agnostic compensation for variance and jump risks [londono2017fxvrp, prokopczuk2017commodityvrp, vantassel2018equityvrp]. Collectively, these results suggest that forward-looking prices for variance-linked payoffs can be persistently discounted relative to their “fair” values when risk is borne by risk-averse traders.

### 1.3 Roadmap

The subsequent sections of this paper are structured as follows: Section 2 provides a theoretical foundation for the proposed model and hypothesis. Section 3 outlines the data sources and the analytical methodologies employed, presents results, and discusses the findings and their implications. The paper concludes with Section 4, which summarizes the key findings and potential future research topics.

## 2 Theory

In this section, we provide a theoretical derivation of how bidders value the express lane (EL). We model each round of the express lane auction (ELA) as a second-price sealed-bid auction for a single, exclusive right to use the EL for a one-minute period, within a conditionally independent private value (CIPV) framework. We assume the winner captures the arbitrage opportunity solely during this period.

We first review how CEX-DEX arbitrage profit is related to the volatility of risky assets. We then specify the auction environment and timing and derive the bidders’ payoffs. From the payoff, we infer bidders’ valuations and their bids, and finally present a reduced-form model and hypotheses for empirical testing.

### 2.1 Arbitrageurs’ Profit

Since the value of the express lane is closely related to MEV, and most of that MEV comes from CEX-DEX arbitrage, it is important to understand arbitrageurs’ profits to correctly value the express lane. In this section, as mentioned earlier, we review the theory of CEX-DEX arbitrage. For simplicity, consider a single constant product market maker (CPMM) pool with an invariant L2L^{2} that consists of a risky asset and a stablecoin. We assume the log price of the risky asset at CEX, which is a *true* price, follows a semi-martingale process with stochastic volatility,

|  |  |  |
| --- | --- | --- |
|  | d​(log⁡Pt)=μt​d​t+σt​d​Wt.d\left(\log P\_{t}\right)=\mu\_{t}dt+\sigma\_{t}dW\_{t}\,. |  |

[milionis2022automated] then showed that loss-versus-rebalancing, which is the arbitrageur’s revenue under ideal settings (i.e., no gas fee and no friction in trading), is proportional to the pool value and volatility of the risky asset.

###### Proposition 1([milionis2022automated])

The instantaneous rate of loss-versus-rebalancing LVR¯\overline{\mathrm{LVR}} is

|  |  |  |
| --- | --- | --- |
|  | LVR¯=L​Pt4​σt2,\overline{\mathrm{LVR}}=\frac{L\sqrt{P\_{t}}}{4}\sigma^{2}\_{t}, |  |

where PtP\_{t} and σt\sigma\_{t} are price and volatility of risky asset at time tt, respectively.

Thus, for interval [0,T][0,T], the arbitrageur’s revenue ARB\mathrm{ARB}is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ARB\displaystyle\mathrm{ARB} | =∫0TLVR¯​𝑑t\displaystyle=\int^{T}\_{0}\overline{\mathrm{LVR}}\,dt |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0TL​Pt4​σt2​𝑑t\displaystyle=\int^{T}\_{0}\frac{L\sqrt{P\_{t}}}{4}\sigma^{2}\_{t}\,dt |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈L​P04​∫0Tσt2​𝑑t\displaystyle\approx\frac{L\sqrt{P\_{0}}}{4}\int^{T}\_{0}\sigma^{2}\_{t}\,dt |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =L​P04​IV,\displaystyle=\frac{L\sqrt{P\_{0}}}{4}\mathrm{IV}, |  | (4) |

where integrated variance IV≡∫0Tσt2​𝑑t\mathrm{IV}\equiv\int^{T}\_{0}\sigma^{2}\_{t}\,dt, with assumption that TT is small enough so that P0≈PtP\_{0}\approx P\_{t} for all t∈[0,T]t\in[0,T]. In practice, a block is not generated continuously, and the arbitrageur has to bear the gas fees and trading costs. However, as shown in works including [milionis2024automated] and [nezlobin2025loss], it remains true that an arbitrageur’s revenue is proportional to the pool’s value and the square of the asset’s volatility.

### 2.2 Express Lane Auction

Here, we clarify the mechanism of the express lane auction (ELA) and its timing. Participants in ELA compete in each round, lasting a minute, for the exclusive right to use the express lane. They want such a right because those with access to the express lane can win all the CEX-DEX arbitrage opportunities. The auction is conducted as a sealed-bid second-price auction, with the bidding deadline strictly before the start of each round. Therefore, the bidders should calculate the value of the express lane based on both public and private information provided to each bidder, and submit a bid before the value is realized. We begin with the following definitions.

###### Definition 1(Rounds, Periods, Bidders, Information, and Reward)

Let:

* •

  r∈ℕr\in\mathbb{N} be each round of ELA,
* •

  [Tr,Tr+1)[T\_{r},T\_{r+1}) be period of each round,
* •

  Dr<TrD\_{r}<T\_{r} be the deadline of bid submission for each round,
* •

  S≡{1,2,⋯,N}S\equiv\{1,2,\cdots,N\} be set of bidders,
* •

  ℱr\mathcal{F}\_{r} and 𝒮i​r\mathcal{S}\_{ir} be public and private information for bidder ii available at DrD\_{r}, respectively,
* •

  vi​rv\_{ir} be bidder ii’s valuation at round rr, and
* •

  bi​rb\_{ir} be bidder ii’s bid at round rr.

### 2.3 Bidders’ Payoff and Valuation

We now derive how bidders value the right to use the express lane in a given
round. For notational convenience, write

|  |  |  |
| --- | --- | --- |
|  | IVr≡IV[Tr,Tr+1)=∫TrTr+1σt2​𝑑t\mathrm{IV}\_{r}\equiv\mathrm{IV}\_{[T\_{r},T\_{r+1})}=\int\_{T\_{r}}^{T\_{r+1}}\sigma\_{t}^{2}\,dt |  |

for the integrated variance over round rr. The winner at round rr will earn profit from arbitrage opportunities within that round. Thus the reward RrR\_{r} is

|  |  |  |
| --- | --- | --- |
|  | Rr=∫TrTr+1LVR¯​𝑑t≈L​PTr4​IVr,R\_{r}=\int^{T\_{r+1}}\_{T\_{r}}\overline{\mathrm{LVR}}\,dt\approx\frac{L\sqrt{P\_{T\_{r}}}}{4}\mathrm{IV}\_{r}, |  |

where LL is liquidity available and IV[Tr,Tr+1)\mathrm{IV}\_{[T\_{r},T\_{r+1})} is integrated variance of risky asset from TrT\_{r} to Tr+1T\_{r+1}.333While traders use the entire liquidity available, beyond a single CPMM pool, if the price does not move much within a round, we can still locally approximate it as a single big CPMM pool; see [Dan2021UniswapV3Universal]. Through the paper, we assume that LL is constant. It is roughly true, since the majority of liquidity is provided by professional LPs who concentrate liquidity near the current price most of the time. Note that RrR\_{r} is random variable and only fully realized after time Tr+1T\_{r+1}. In practice, even with express lane access, a bidder may only capture a fraction of the available arbitrage, and may face idiosyncratic costs or benefits (e.g., private order flow, infrastructure frictions).444Note that this does not necessarily imply that others can take advantage of it and earn profit. If such friction exists, it is very likely that others will have to bear that friction as well, which makes trade unprofitable. We model the *net* profit of bidder ii from winning round rr as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πi​r=αi​r+βi​r​IVr​PTr,\Pi\_{ir}=\alpha\_{ir}+\beta\_{ir}\mathrm{IV}\_{r}\sqrt{P\_{T\_{r}}}, |  | (5) |

where:

* •

  αi​r\alpha\_{ir} collects components of profit and cost that do not scale with volatility (e.g., fixed costs, long-tail MEV),
* •

  βi​r\beta\_{ir} is bidder ii’s *extraction efficiency* in round rr, summarizing how effectively the bidder converts volatility into arbitrage revenue. In particular, βi​r\beta\_{ir} subsumes both the liquidity factor L/4L/4 and the bidder’s share of the total arbitrage RrR\_{r}.

Both αi​r\alpha\_{ir} and βi​r\beta\_{ir} are measurable with respect to bidder ii’s private information 𝒮i​r\mathcal{S}\_{ir} and the public information ℱr\mathcal{F}\_{r} available at the bidding deadline DrD\_{r}.

Conditional on (ℱr,𝒮i​r)(\mathcal{F}\_{r},\mathcal{S}\_{ir}), bidder ii forms a belief on the distribution over IVr\mathrm{IV}\_{r} and thus over Πi​r\Pi\_{ir}. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | mi​rIV≡𝔼​[IVr∣ℱr,𝒮i​r]andvi​rIV≡Var​(IVr∣ℱr,𝒮i​r)m^{\mathrm{IV}}\_{ir}\equiv\mathbb{E}\left[\mathrm{IV}\_{r}\mid\mathcal{F}\_{r},\mathcal{S}\_{ir}\right]\quad\text{and}\quad v^{\mathrm{IV}}\_{ir}\equiv\mathrm{Var}\left(\mathrm{IV}\_{r}\mid\mathcal{F}\_{r},\mathcal{S}\_{ir}\right) |  | (6) |

denote bidder ii’s forecast mean and variance of integrated variance for round rr. Since PTrP\_{T\_{r}} is (approximately) known at DrD\_{r}, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Πi​r∣ℱr,𝒮i​r]\displaystyle\mathbb{E}\!\left[\Pi\_{ir}\mid\mathcal{F}\_{r},\mathcal{S}\_{ir}\right] | =αi​r+βi​r​mi​rIV​PTr,\displaystyle=\alpha\_{ir}+\beta\_{ir}m^{\mathrm{IV}}\_{ir}\sqrt{P\_{T\_{r}}}\,, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​(Πi​r∣ℱr,𝒮i​r)\displaystyle\mathrm{Var}\!\left(\Pi\_{ir}\mid\mathcal{F}\_{r},\mathcal{S}\_{ir}\right) | =βi​r2​vi​rIV​PTr.\displaystyle=\beta\_{ir}^{2}v^{\mathrm{IV}}\_{ir}P\_{T\_{r}}\,. |  | (8) |

We now introduce a key assumption: the conditional independence of bidders’ valuation and risk aversion.

###### Assumption 1(CIPV)

Conditional on the public information ℱr\mathcal{F}\_{r}, bidders’ valuations parameters

|  |  |  |
| --- | --- | --- |
|  | {(αi​r,βi​r,γi​r,mi​rIV,vi​rIV)}i=1N\{(\alpha\_{ir},\beta\_{ir},\gamma\_{ir},m^{\mathrm{IV}}\_{ir},v^{\mathrm{IV}}\_{ir})\}\_{i=1}^{N} |  |

are independently drawn.

Assumption [1](https://arxiv.org/html/2512.23386v1#Thmassump1 "Assumption 1(CIPV) ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") formalizes the “conditionally independent private values” (CIPV) environment: public information ℱr\mathcal{F}\_{r} is common to all bidders, while private signals 𝒮i​r\mathcal{S}\_{ir} generate heterogeneous valuations through the parameters

|  |  |  |
| --- | --- | --- |
|  | (αi​r,βi​r,γi​r,mi​rIV,vi​rIV),(\alpha\_{ir},\beta\_{ir},\gamma\_{ir},m^{\mathrm{IV}}\_{ir},v^{\mathrm{IV}}\_{ir}), |  |

which reflects the reality: while there are public signals observable to everyone, such as recent prices and order flow on exchanges, each firm relies on one’s proprietary models to forecast future volatility, and each firm’s edge or alpha of finding optimal route or executing trades remain private.

###### Assumption 2(Preferences)

Each bidder ii is risk-averse and evaluates random profits using a mean–variance functional. That is, there exists a risk-aversion parameter ρi​r>0\rho\_{ir}>0 such that the certainty equivalent (CE) of any profit random variable XX in round rr is

|  |  |  |
| --- | --- | --- |
|  | CEi​r​(X)=𝔼​[X]−ρi​r2​Var​(X).\mathrm{CE}\_{ir}(X)=\mathbb{E}[X]-\frac{\rho\_{ir}}{2}\mathrm{Var}(X). |  |

Under Assumption [2](https://arxiv.org/html/2512.23386v1#Thmassump2 "Assumption 2(Preferences) ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies"), bidder ii’s valuation of the express lane in round rr is the certainty equivalent of Πi​r\Pi\_{ir}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vi​r≡CEi​r​(Πi​r)=𝔼​[Πi​r∣ℱr,𝒮i​r]−ρi​r2​Var​(Πi​r∣ℱr,𝒮i​r).v\_{ir}\equiv\mathrm{CE}\_{ir}(\Pi\_{ir})=\mathbb{E}\!\left[\Pi\_{ir}\mid\mathcal{F}\_{r},\mathcal{S}\_{ir}\right]-\frac{\rho\_{ir}}{2}\mathrm{Var}\!\left(\Pi\_{ir}\mid\mathcal{F}\_{r},\mathcal{S}\_{ir}\right). |  | (9) |

Substituting ([7](https://arxiv.org/html/2512.23386v1#S2.E7 "Equation 7 ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")) and ([8](https://arxiv.org/html/2512.23386v1#S2.E8 "Equation 8 ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")) into
([9](https://arxiv.org/html/2512.23386v1#S2.E9 "Equation 9 ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | vi​r\displaystyle v\_{ir} | =αi​r+βi​r​mi​rIV​PTr−ρi​r2​βi​r2​vi​rIV​PTr\displaystyle=\alpha\_{ir}+\beta\_{ir}m^{\mathrm{IV}}\_{ir}\sqrt{P\_{T\_{r}}}-\frac{\rho\_{ir}}{2}\beta\_{ir}^{2}v^{\mathrm{IV}}\_{ir}P\_{T\_{r}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =αi​r+βi​r​mi​rIV​PTr−γi​r​vi​rIV​PTr,\displaystyle=\alpha\_{ir}+\beta\_{ir}m^{\mathrm{IV}}\_{ir}\sqrt{P\_{T\_{r}}}-\gamma\_{ir}v^{\mathrm{IV}}\_{ir}P\_{T\_{r}}, |  | (10) |

where we define

|  |  |  |
| --- | --- | --- |
|  | γi​r≡ρi​r2​βi​r2>0.\gamma\_{ir}\equiv\frac{\rho\_{ir}}{2}\beta\_{ir}^{2}>0. |  |

Equation ([10](https://arxiv.org/html/2512.23386v1#S2.E10 "Equation 10 ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")) makes explicit that higher expected volatility (integrated variance) increases valuations, while greater uncertainty about volatility lowers valuations through the risk-aversion term.

### 2.4 Auction Equilibrium and Empirical Implications

Given the valuation structure in ([10](https://arxiv.org/html/2512.23386v1#S2.E10 "Equation 10 ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")), we now describe bidding behavior in the express lane auction. In each round rr, bidders simultaneously submit sealed bids {bi​r}i=1N\{b\_{ir}\}\_{i=1}^{N}. The bidder with the highest bid wins the right to use the express lane during [Tr,Tr+1)[T\_{r},T\_{r+1}) and pays the second-highest bid, while all other bidders pay zero. The following proposition justifies the use of the submitted bid as the bidder’s valuation.

###### Proposition 2(Equilibrium Bidding)

Under Assumptions [2](https://arxiv.org/html/2512.23386v1#Thmassump2 "Assumption 2(Preferences) ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") and [1](https://arxiv.org/html/2512.23386v1#Thmassump1 "Assumption 1(CIPV) ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies"), in each round rr of the express lane auction, it is a (weakly) dominant strategy for each bidder to bid her valuation:

|  |  |  |
| --- | --- | --- |
|  | bi​r=vi​rfor all ​i∈{1,…,N}.b\_{ir}=v\_{ir}\quad\text{for all }i\in\{1,\dots,N\}. |  |

Proposition [2](https://arxiv.org/html/2512.23386v1#Thmprop2 "Proposition 2(Equilibrium Bidding) ‣ 2.4 Auction Equilibrium and Empirical Implications ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") is the standard truth-telling result for second-price auctions with private values; see, for example, [krishna2009auction]. Combining Proposition [2](https://arxiv.org/html/2512.23386v1#Thmprop2 "Proposition 2(Equilibrium Bidding) ‣ 2.4 Auction Equilibrium and Empirical Implications ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") with ([10](https://arxiv.org/html/2512.23386v1#S2.E10 "Equation 10 ‣ 2.3 Bidders’ Payoff and Valuation ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")), we obtain the structural relationship

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​r=αi​r+βi​r​mi​rIV​PTr−γi​r​vi​rIV​PTr.b\_{ir}=\alpha\_{ir}+\beta\_{ir}m^{\mathrm{IV}}\_{ir}\sqrt{P\_{T\_{r}}}-\gamma\_{ir}v^{\mathrm{IV}}\_{ir}P\_{T\_{r}}. |  | (11) |

Equation ([11](https://arxiv.org/html/2512.23386v1#S2.E11 "Equation 11 ‣ 2.4 Auction Equilibrium and Empirical Implications ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")) shows that, in our model, equilibrium bids are increasing in the bidder’s forecast of integrated variance and decreasing in the forecast uncertainty about integrated variance, with both effects scaled by the current asset price. This link motivates our empirical specification.

In the data, we do not observe the latent objects (αi​r,βi​r,γi​r,mi​rIV,vi​rIV)(\alpha\_{ir},\beta\_{ir},\gamma\_{ir},m^{\mathrm{IV}}\_{ir},v^{\mathrm{IV}}\_{ir}) directly. Instead, we approximate ([11](https://arxiv.org/html/2512.23386v1#S2.E11 "Equation 11 ‣ 2.4 Auction Equilibrium and Empirical Implications ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")) by a reduced-form model in which expected integrated variance and its uncertainty are replaced by observable proxies and bidder- or round-specific components are absorbed into fixed effects. Specifically, in the subsequent section we estimate regressions of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​r=θ0,i+θ1,i​𝔼​[IVr]^​PTr+θ2,i​Var​(IVr)^​PTr+εi​r,b\_{ir}=\theta\_{0,i}+\theta\_{1,i}\widehat{\mathbb{E}[\mathrm{IV}\_{r}]}\sqrt{P\_{T\_{r}}}+\theta\_{2,i}\widehat{\mathrm{Var}(\mathrm{IV}\_{r})}\,P\_{T\_{r}}+\varepsilon\_{ir}, |  | (12) |

where:

* •

  𝔼​[IVr]^\widehat{\mathbb{E}[\mathrm{IV}\_{r}]} is a proxy of forecast mean mi​rIVm^{\mathrm{IV}}\_{ir},
* •

  Var​(IVr)^\widehat{\mathrm{Var}(\mathrm{IV}\_{r})} is a proxy for the forecast variance
  vi​rIVv^{\mathrm{IV}}\_{ir}, and
* •

  εi​r\varepsilon\_{ir} is an error term.

Under ([11](https://arxiv.org/html/2512.23386v1#S2.E11 "Equation 11 ‣ 2.4 Auction Equilibrium and Empirical Implications ‣ 2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")), the theory predicts θ1,i>0\theta\_{1,i}>0 and θ2,i<0\theta\_{2,i}<0: bids should increase with expected volatility (more MEV to extract) and decrease with uncertainty about volatility (stronger risk discount). These sign restrictions form our main testable hypotheses.

## 3 Empirical Analysis

### 3.1 Data

#### Auction Records.

For the auction bids, we obtained the data directly from Arbitrum’s database [offchainlabs2025howtousetimeboost]. Our sample spans bids from May to October 2025. While multiple bidders participate, we focus on the two most dominant participants, 0x8c6f and 0x95c0, who together win over 90%90\% of rounds between May and October.

#### Measuring Volatility.

We proxy market-wide volatility using high-frequency ETH price data from Binance. As ETH is the most liquid crypto-asset on Arbitrum555We exclude stablecoins; see [l2beat]., focusing on ETH serves as a low-friction approximation of overall market conditions. While price follows a stochastic process and thus the integrated variance is also essentially random, all we have is historical data of a single *realized* path out of all possible outcomes. Therefore, we have to estimate 𝔼​[IV]\mathbb{E}[\mathrm{IV}] and Var​(IV)\mathrm{Var}(\mathrm{IV}) from the given path of price. We adopt a standard approach, treating the realized variance (RV), the sum of squares of log returns rtr\_{t}, as 𝔼​[IV]^\widehat{\mathbb{E}[\mathrm{IV}]}, while estimating Var​(IV)^\widehat{\mathrm{Var}(\mathrm{IV})} with the following Newey-West estimator:

|  |  |  |
| --- | --- | --- |
|  | Var​(IV)^=T​(γ0+2​∑k=1Lwk​γk),\widehat{\mathrm{Var}(\mathrm{IV})}=T(\gamma\_{0}+2\sum\_{k=1}^{L}w\_{k}\gamma\_{k}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | γk≡1T​∑t=1T−k(rt+k2−r2¯)​(rt2−r2¯)andr2¯≡1T​∑t=1Trt2,\gamma\_{k}\equiv\frac{1}{T}\sum\_{t=1}^{T-k}(r^{2}\_{t+k}-\overline{r^{2}})(r^{2}\_{t}-\overline{r^{2}})\quad\text{and}\quad\overline{r^{2}}\equiv\frac{1}{T}\sum\_{t=1}^{T}r\_{t}^{2}\,, |  |

for k=0,1,2,⋯k=0,1,2,\cdots, and wk≡1−kL+1w\_{k}\equiv 1-\frac{k}{L+1} is weight function. The standard practice of setting LL is of L=𝒪​(T1/3)L=\mathcal{O}(T^{1/3}). In our setting, we set T=60T=60 and L=5L=5.

#### Bidder Forecasts.

The theoretical model proposed in [Section˜2](https://arxiv.org/html/2512.23386v1#S2 "2 Theory ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") posits that bids depend on bidders’ private forecasts of realized variance, which are unobservable. We therefore adopt the following assumption to bridge the theory with our ex-post volatility measures:

###### Assumption 3(On-average Correct Forecast)

Bidders are capable of *on-average* correctly forecasting the mean and variance of forthcoming IVr\mathrm{IV}\_{r} based on public and private information available at time DrD\_{r}. That is, for

|  |  |  |
| --- | --- | --- |
|  | ϵi​r≡mi​rIV−𝔼​[IVr]a​n​dτi​r≡vi​rIV−Var​(IVr),\epsilon\_{ir}\equiv m^{\mathrm{IV}}\_{ir}-\mathbb{E}[\mathrm{IV}\_{r}]\quad and\quad\tau\_{ir}\equiv v^{\mathrm{IV}}\_{ir}-\mathrm{Var}(\mathrm{IV}\_{r}), |  |

𝔼​[ϵi​r|ℱr]=𝔼​[τi​r|ℱr]=0\mathbb{E}\left[\epsilon\_{ir}|\mathcal{F}\_{r}\right]=\mathbb{E}\left[\tau\_{ir}|\mathcal{F}\_{r}\right]=0.666Note that this does not necessarily violate the CIPV framework. One can interpret this assumption that, based on public information, it is possible to, on average, correctly forecast the mean and variance of IV\mathrm{IV}. Then ϵi​r\epsilon\_{ir} and τi​r\tau\_{ir} being independent and private is sufficient for the CIPV setting.

This errors-in-variables framework implies that our estimates of θ1\theta\_{1} and θ2\theta\_{2} will be subject to attenuation bias, which will bias them towards zero. Consequently, finding statistically significant coefficients despite this bias would provide a conservative and even stronger confirmation of our hypotheses.

### 3.2 Estimation

Our dependent variable, the observed bid bi​rb\_{ir}, is left-censored at the reserve price C=0.001C=0.001 ETH. To account for the fat tails often observed in financial data, we employ a heteroskedastic Tobit model, assuming that the normalized residuals follow a Student’s t distribution. Also, the bid unit is in ETH, while the bidder’s valuation is in USD. Thus, we divide the bidder’s valuation by the ETH price at each round.777The division on constant term is omitted, since the range of price (minimum 1.71.7k and maximum 4.94.9k USD) was negligible compared to that of the estimated mean and variance of IV\mathrm{IV}. Then, the model is defined as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | bi​r\displaystyle b\_{ir} | =max⁡(C,vi​r∗)\displaystyle=\max(C,v^{\*}\_{ir}) |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vi​r∗\displaystyle v^{\*}\_{ir} | =θ0+θ1​𝔼​[IV]^Pr+θ2​Var​(IV)^+εi​r\displaystyle=\theta\_{0}+\theta\_{1}\frac{\widehat{\mathbb{E}[\mathrm{IV}]}}{\sqrt{P\_{r}}}+\theta\_{2}\widehat{\mathrm{Var}(\mathrm{IV})}+\varepsilon\_{ir} |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡(σr)\displaystyle\log(\sigma\_{r}) | =γ0+γ1​log⁡(𝔼​[IV]^Pr)+γ2​log⁡(Var​(IV)^)\displaystyle=\gamma\_{0}+\gamma\_{1}\log\left(\frac{\widehat{\mathbb{E}[\mathrm{IV}]}}{\sqrt{P\_{r}}}\right)+\gamma\_{2}\log\left(\widehat{\mathrm{Var}(\mathrm{IV})}\right) |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | εi​rσr\displaystyle\frac{\varepsilon\_{ir}}{\sigma\_{r}} | ∼t​(ν)\displaystyle\sim t(\nu) |  | (16) |

where vi​r∗v^{\*}\_{ir} is the latent valuation of bidder ii for round rr, bi​rb\_{ir} is the observed bid, 𝔼​[IV]^\widehat{\mathbb{E}[\mathrm{IV}]} and Var​(IV)^\widehat{\mathrm{Var}(\mathrm{IV})} are estimated mean and variance of integrated variance of given round, σr\sigma\_{r} is the conditional scale (standard deviation) of the latent valuation, modeled in log-linear form to ensure positivity, and t​(ν)t(\nu) is the Student’s t-distribution with ν\nu degrees of freedom, which is also estimated. We also adjusted the scale of data (×10−15\times 10^{-15} for bids, ×109\times 10^{9} for 𝔼​[IV]^Pr\frac{\widehat{\mathbb{E}[\mathrm{IV}]}}{\sqrt{P\_{r}}} and ×1012\times 10^{12} for Var​(IV)^\widehat{\mathrm{Var}(\mathrm{IV})}) for numerical stability. Our hypotheses from the end of the previous section then translate to testing the coefficients in the mean model (Equation [14](https://arxiv.org/html/2512.23386v1#S3.E14 "Equation 14 ‣ 3.2 Estimation ‣ 3 Empirical Analysis ‣ Impact of Volatility on Time-Based Transaction Ordering Policies")):

* •

  𝐇𝟏:θ𝟏>𝟎\mathbf{H\_{1}:\theta\_{1}>0}. A positive θ1\theta\_{1} supports that higher expected volatility leads to higher valuations.
* •

  𝐇𝟐:θ𝟐<𝟎\mathbf{H\_{2}:\theta\_{2}<0}. A negative θ2\theta\_{2} supports the conclusion that higher uncertainty (forecast variance) leads to a larger risk-aversion discount and thus to lower valuations.

In addition to the linear specification derived from the mean-variance framework, we also estimate a log-log specification (where both bids and volatility measures are logged). While the linear model follows directly from our theoretical assumptions, the log-log specification offers strong empirical justifications. First, it systematically enforces nonnegative valuations, ruling out the theoretical possibility of negative bids implied by linear risk adjustments. Second, since the integrated variance and bids are numerically small values spanning multiple orders of magnitude, the log-log transformation mitigates the influence of extreme outliers and heteroskedasticity. Under these conditions, the log-log form can be interpreted as a first-order approximation of the equilibrium relationship, capturing potential nonlinearities in risk aversion (e.g., CRRA preferences) while serving as a strict robustness check for our main findings.

### 3.3 Results

![Refer to caption](x2.png)


Figure 2: Scatter plot of each bidder’s bids and price-adjusted integrated variance. Both are shown in log scale for visibility.

[Table˜1](https://arxiv.org/html/2512.23386v1#S3.T1 "In 3.3 Results ‣ 3 Empirical Analysis ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") shows the result of the estimates. For comparison, we also attach the result from the restricted model, which is identical to the original model except that the latent valuation depends only on 𝔼​[IV]^\widehat{\mathbb{E}[\mathrm{IV}]}. This corresponds to the risk-neutral bidder’s valuation. The first column corresponds to the restricted model, and the second to the previously introduced full model.

Across bidders, augmenting the specification with a variance term significantly improves the fit: LR tests are significant, and information criteria drop substantially. In the location equation, θ1>0\theta\_{1}>0 indicates that a higher expected IV is associated with higher bids, consistent with the view that the express-lane option is more valuable when arbitrage intensity rises. Conversely, θ2<0\theta\_{2}<0 on the standardized variance of the IV implies a risk discount: greater forecast uncertainty lowers valuations. Estimated tail parameters (ν≈1.2\nu\approx 1.2–1.71.7) confirm heavy-tailed residuals, justifying the Student-tt specification. [Figures˜2](https://arxiv.org/html/2512.23386v1#S3.F2 "In 3.3 Results ‣ 3 Empirical Analysis ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") and [3](https://arxiv.org/html/2512.23386v1#S3.F3 "Figure 3 ‣ 3.3 Results ‣ 3 Empirical Analysis ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") provide comprehensive visualization of our result.

Interestingly, the log-log variant of the reduced and full models yielded better results, although it lacks a theoretical justification. This may be due to the aforementioned scaling issues with the independent variables. The magnitude of the estimated mean and variance of IV spans across 10−610^{-6} to 10−310^{-3} and 10−2210^{-22} to 10−1210^{-12}, respectively, and residuals on the samples with large estimated IV moments dominate in the process of MLE. See [Table˜2](https://arxiv.org/html/2512.23386v1#Pt0.A1.T2 "In Appendix 0.A Tables ‣ Impact of Volatility on Time-Based Transaction Ordering Policies").

![Refer to caption](x3.png)


Figure 3: Scatter plots of each bidder’s bids grouped by percentile of 𝔼​[IV]/P\mathbb{E}[\mathrm{IV}]/\sqrt{P}. A heteroskedastic tobit regression was done for each subsample. For visibility, the figure is in log scale.



|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bidder 0x8c6f | | Bidder 0x95c0 | |
| Variable | Reduced | Full | Reduced | Full |
| Panel A: Location Coefficients | | | | |
| Intercept (θ0\theta\_{0}) | 0.9878∗∗∗ | 0.9836∗∗∗ | 1.3691∗∗∗ | 1.1393∗∗∗ |
|  | (0.0011) | (0.0021) | (0.0061) | (0.0060) |
| E[IV]/P\sqrt{P} (θ1\theta\_{1}) | 0.3404∗∗∗ | 0.3472∗∗∗ | 0.3828∗∗∗ | 0.4421∗∗∗ |
|  | (0.0012) | (0.0014) | (0.0015) | (0.0017) |
| Var(IV) (θ2\theta\_{2}) | – | -2.0792∗∗∗ | – | -3.1878∗∗∗ |
|  | – | (0.0340) | – | (0.0460) |
| Panel B: Scale Coefficients | | | | |
| Intercept (γ0\gamma\_{0}) | -0.1690∗∗∗ | -2.2705∗∗∗ | 0.2718∗∗∗ | -1.4502∗∗∗ |
|  | (0.0052) | (0.0286) | (0.0041) | (0.0252) |
| log\log(E[IV]/P\sqrt{P}) (γ1\gamma\_{1}) | 0.5933∗∗∗ | 1.0895∗∗∗ | 0.4310∗∗∗ | 0.8572∗∗∗ |
|  | (0.0022) | (0.0072) | (0.0018) | (0.0064) |
| log\log(Var(IV)) (γ2\gamma\_{2}) | – | -0.3005∗∗∗ | – | -0.2390∗∗∗ |
|  | – | (0.0039) | – | (0.0034) |
| Panel C: Model Fit Statistics | | | | |
| Observations | 264959 | 264959 | 264959 | 264959 |
| Censored | 264959 | 264959 | 264959 | 264959 |
| Student tt ν\nu | 1.23 | 1.30 | 1.55 | 1.70 |
| Log Likelihood | -729873.32 | -724012.17 | -724400.50 | -717011.02 |
| AIC | 1459756.64 | 1448038.34 | 1448810.99 | 1434036.03 |
| BIC | 1459809.08 | 1448111.75 | 1448863.43 | 1434109.44 |
| McFadden R2R^{2} | 0.071 | 0.079 | 0.078 | 0.087 |
| Panel D: Full vs Reduced Model Comparison | | | | |
| Δ\Delta AIC (Full - Reduced) | -11718.30 | | -14774.96 | |
| Δ\Delta BIC (Full - Reduced) | -11697.32 | | -14753.99 | |
| LR Test χ2\chi^{2} (p-val) | 11722.30∗⁣∗∗11722.30^{\*\*\*} | | 14778.96∗⁣∗∗14778.96^{\*\*\*} | |

Table 1: Heteroskedastic Tobit (Linear, t-dist Errors). p∗<0.05{}^{\*}p<0.05, p∗∗<0.01{}^{\*\*}p<0.01, p∗⁣∗∗<0.001{}^{\*\*\*}p<0.001.

#### Robustness.

We assess the robustness of the estimated relationships across different market conditions. To this end, we partition the dataset along both the temporal and regime dimensions. Specifically, the full sample is divided into (i) monthly subsamples from May through October and (ii) two volatility regimes (low and high, with median as threshold) delineated by the cross-sectional median of volatility. The regression model is then re-estimated separately for each subsample, and the corresponding estimates are reported in [Table˜3](https://arxiv.org/html/2512.23386v1#Pt0.A1.T3 "In Appendix 0.A Tables ‣ Impact of Volatility on Time-Based Transaction Ordering Policies").

Although the magnitude of the estimated coefficients varies across subsamples, the sign pattern is preserved: the coefficient on the variance of variance remains negative (interpreted as a discount) in all cases. A notable exception arises in the low-volatility regime, where the estimate of the coefficient on θ2\theta\_{2} is disproportionately large. While we do not have a definitive explanation for this outcome, we conjecture that it is attributable to a scaling issue. In particular, Var​(IV)^\widehat{\mathrm{Var}(\mathrm{IV})} is approximately of the same order of magnitude as 𝔼​[IV]^2\widehat{\mathbb{E}[\mathrm{IV}]}^{2}, with its minimum value on the order of 10−2210^{-22}, and such extreme scaling potentially lead to estimation bias and numerical instability in some cases.

To further verify our hypothesis without relying on the rational-expectations, i.e., the on-average correct forecasts assumption, we also ran a regression using lagged IV moment estimators, the estimated mean and variance of IV from the previous round, which are available to bidders at the time of bidding. For the result, see [Tables˜4](https://arxiv.org/html/2512.23386v1#Pt0.A1.T4 "In Appendix 0.A Tables ‣ Impact of Volatility on Time-Based Transaction Ordering Policies") and [5](https://arxiv.org/html/2512.23386v1#Pt0.A1.T5 "Table 5 ‣ Appendix 0.A Tables ‣ Impact of Volatility on Time-Based Transaction Ordering Policies"). We found that not only does the discount remain persistent, but the overall goodness of fit also improves significantly for both linear and log-transformed models, suggesting the possibility of bidders relying on a simple AR(1) model instead of trying to precisely forecast the volatility distribution.

### 3.4 Discussion

The empirical findings reveal a statistically significant discount attributed to the inherent uncertainty (i.e., risk) associated with forecasting future volatility and the generated arbitrage revenue.
This suggests that the efficiency of the ELA may diminish during periods of high market turbulence, not just because volatility is high, but because it becomes less predictable. This discount leads to lower bids relative to bidders’ expected value of CEX-DEX arbitrage profit and, consequently, to a lower MEV capture rate. Further refinement of the ELA mechanism is required to mitigate this observed inefficiency.

Given the challenges of accurately forecasting short-term volatility due to its low signal-to-noise ratio and non-stationarity, extending the round length to a longer duration, such as hourly or even daily, may be a more robust design. While longer horizons introduce other challenges, such as increased capital requirements, they may filter high-frequency noise and improve the signal-to-noise ratio of volatility forecasts. We also note that, instead of a seemingly arbitrary 0.0010.001 ETH, the reserve price should be set strategically to maximize expected revenue, balancing the guaranteed lower bound on payment with the probability of failing to attract any bidders.

Alternatively, a subscription-based model could be considered for simultaneously offering the express lane to multiple market participants. This approach has established precedents within traditional financial (TradFi) exchanges [budish2024theory], and recently launched perpetual exchanges such as Lighter and Paradex are adopting it as well888See <https://apidocs.lighter.xyz/docs/account-types> and <https://docs.paradex.trade/trading/trader-profiles#fee-structure>..

#### Limitations.

Although the data support our hypotheses, our model has several limitations. Firstly, our model presents an oversimplified representation. Factors such as Total Value Locked (TVL) and liquidity near the current price significantly influence bidders’ revenue; however, these elements are not incorporated into our model, which may introduce bias into our estimations. Secondly, data noise poses a challenge. Binance candles, generated from the last traded price, are susceptible to sudden price spikes from large market orders, thereby becoming decoupled from the true price. The use of future values as a proxy for the forecast also causes attenuation bias. We also remark that a significant portion of rounds being censored in samples and subsamples further weakens our claims, too.

## 4 Conclusion

In this study, we hypothesized that Timeboost exhibits a lower MEV capture rate under volatile market conditions and empirically tested this hypothesis. Our methodology uses realized values to construct a noisy proxy for an unobserved variable that captures bidders’ forecasts of future volatility. We developed a bidder valuation model and proposed using the coefficient on the variance of integrated variance (Var​(IV)\mathrm{Var}(\mathrm{IV})) as the risk premium for the uncertainty in the value of access to the express lane (EL).
Subsequently, we compared the regression results of our model with those of a baseline model that excluded a risk premium, demonstrating improvements in fit and a reduction in downward bias in the restricted model. We further tested our hypothesis under various conditions to check the robustness of the results.

This study shows that variance risk premiums are statistically significant and negative. Specifically, it demonstrates that the full model provides a better explanation of the findings compared to the restricted model. As expected, the restricted model yields a downward-biased slope relative to the full model, reinforcing the overall argument. We further tested our hypothesis under various conditions, checking the results with subsamples, using alternative measures of volatility, dropping the rational-expectations assumption, and using forecasted rather than realized values to assess robustness.

Based on the results, we provided an outline to improve the current Timeboost auction implementation and increase the sequencer’s revenue. Specifically, we offered two suggestions: a more advanced method for setting the reserve price and extending the round length, which helps bidders better estimate future (averaged) volatility, leading to less discounting. We also briefly mentioned the option of switching to a subscription model, which is already popular in traditional finance (TradFi).

Our methodology exhibits several notable limitations. Primarily, the model’s simplicity results in the omission of numerous real-world complexities. For example, the model assumes that the liquidity available around the CEX price remains constant throughout the analysis period and restricts its scope to ETH as the only volatile asset within AMMs. Furthermore, reliance on the CIPV framework may not fully capture the intricacies of actual market dynamics. The use of future realized variance and Newey-West estimators, which are inherently unknown at the time of bidding, as noisy proxies for bidders’ forecasts, introduces attenuation bias. Finally, the substantial rate of data censorship poses significant challenges to the robustness and validity of the inferences drawn, despite the use of tobit regression.

Despite of aforementioned limitations, this study is one of the first empirical investigations of Timeboost, examining the determinants of bidders’ valuations and the efficacy of the express lane auctions. As such, it provides a foundational reference for subsequent research that employs more advanced methodologies and incorporates realistic assumptions. Ultimately, this study aims to enhance the understanding of time-based sequencing mechanisms within auction frameworks.

## Appendix 0.A Tables

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bidder 0x8c6f | | Bidder 0x95c0 | |
| Variable | Reduced | Full | Reduced | Full |
| Panel A: Location Coefficients | | | | |
| Intercept (θ0\theta\_{0}) | 44.5019∗∗∗ | 44.7182∗∗∗ | 45.4140∗∗∗ | 45.7480∗∗∗ |
|  | (0.0313) | (0.0298) | (0.0283) | (0.0275) |
| log\log(E[IV]/P\sqrt{P}) (θ1\theta\_{1}) | 0.4541∗∗∗ | 1.2026∗∗∗ | 0.4962∗∗∗ | 1.3663∗∗∗ |
|  | (0.0016) | (0.0048) | (0.0015) | (0.0044) |
| log\log(Var(IV)) (θ2\theta\_{2}) | – | -0.4403∗∗∗ | – | -0.5092∗∗∗ |
|  | – | (0.0026) | – | (0.0024) |
| Panel B: Scale Coefficients | | | | |
| Intercept (γ0\gamma\_{0}) | -0.0320 | 0.5389∗∗∗ | -0.5813∗∗∗ | -0.2515∗∗∗ |
|  | (0.0169) | (0.0206) | (0.0162) | (0.0204) |
| log\log(E[IV]/P\sqrt{P}) (γ1\gamma\_{1}) | -0.0013 | 0.0384∗∗∗ | -0.0255∗∗∗ | -0.0842∗∗∗ |
|  | (0.0009) | (0.0038) | (0.0008) | (0.0039) |
| log\log(Var(IV)) (γ2\gamma\_{2}) | – | -0.0042∗ | – | 0.0478∗∗∗ |
|  | – | (0.0021) | – | (0.0021) |
| Panel C: Model Fit Statistics | | | | |
| Observations | 264959 | 264959 | 264959 | 264959 |
| Censored | 9151360 | 9151360 | 9151360 | 9151360 |
| Log Likelihood | -358833.46 | -345110.74 | -338519.76 | -317455.38 |
| AIC | 717674.91 | 690233.48 | 677047.52 | 634922.76 |
| BIC | 717716.86 | 690296.41 | 677089.47 | 634985.69 |
| McFadden R2R^{2} | 0.119 | 0.153 | 0.150 | 0.203 |
| Panel D: Full vs Reduced Model Comparison | | | | |
| Δ\Delta AIC (Full - Reduced) | -27441.43 | | -42124.76 | |
| Δ\Delta BIC (Full - Reduced) | -27420.45 | | -42103.78 | |
| LR Test χ2\chi^{2} (p-val) | 27445.43∗⁣∗∗27445.43^{\*\*\*} | | 42128.76∗⁣∗∗42128.76^{\*\*\*} | |

Table 2: Heteroskedastic Tobit (Log-Log, Gaussian Errors). p∗<0.05{}^{\*}p<0.05, p∗∗<0.01{}^{\*\*}p<0.01, p∗⁣∗∗<0.001{}^{\*\*\*}p<0.001.




Table 3: Heteroskedastic Tobit Regression by Subsample

| Bidder | Subsample | N | θ1R\theta\_{1}^{R} | θ1F\theta\_{1}^{F} | θ2F\theta\_{2}^{F} | LR | Δ\DeltaAIC | Δ\DeltaBIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0x8c6f | 2025-05 | 44640 | 0.070 | 0.071 | -0.080 | 571.3 | -567.3 | -549.9 |
|  | 2025-06 | 43200 | 0.425 | 0.485 | -2.713 | 1809.4 | -1805.4 | -1788.1 |
|  | 2025-07 | 44640 | 0.365 | 0.423 | -2.380 | 1929.8 | -1925.8 | -1908.4 |
|  | 2025-08 | 44640 | 0.179 | 0.182 | -1.103 | 1081.7 | -1077.7 | -1060.3 |
|  | 2025-09 | 43200 | 0.018 | 0.026 | -0.207 | 812.9 | -808.9 | -791.6 |
|  | 2025-10 | 44639 | 0.167 | 0.158 | -0.377 | 892.3 | -888.3 | -870.9 |
|  | High E[IV]/P\sqrt{P} | 132479 | 0.276 | 0.329 | -1.612 | 4196.5 | -4192.5 | -4172.9 |
|  | Low E[IV]/P\sqrt{P} | 132480 | 0.428 | 0.599 | -86.673 | 10163.1 | -10159.1 | -10139.6 |
| 0x95c0 | 2025-05 | 44640 | 0.461 | 0.483 | -2.385 | 1681.3 | -1677.3 | -1659.9 |
|  | 2025-06 | 43200 | 0.538 | 0.581 | -3.640 | 2561.0 | -2557.0 | -2539.7 |
|  | 2025-07 | 44640 | 0.450 | 0.481 | -3.101 | 2456.7 | -2452.7 | -2435.3 |
|  | 2025-08 | 44640 | 0.228 | 0.252 | -2.330 | 1564.9 | -1560.9 | -1543.5 |
|  | 2025-09 | 43200 | 0.259 | 0.285 | -2.372 | 1005.9 | -1001.9 | -984.6 |
|  | 2025-10 | 44639 | 0.304 | 0.338 | -2.166 | 1885.6 | -1881.6 | -1864.2 |
|  | High E[IV]/P\sqrt{P} | 132479 | 0.332 | 0.398 | -2.295 | 6232.3 | -6228.3 | -6208.7 |
|  | Low E[IV]/P\sqrt{P} | 132480 | 0.514 | 0.896 | -145.477 | 7800.4 | -7796.4 | -7776.8 |

* •

  Notes: θ1R\theta\_{1}^{R}: E[IV]/P\sqrt{P} coefficient (reduced model), θ1F\theta\_{1}^{F}: E[IV]/P\sqrt{P} coefficient (full model), θ2F\theta\_{2}^{F}: Var(IV) coefficient (full model). High/Low regimes split at the median of E[IV]/P\sqrt{P} across the entire dataset. All LR tests are significant at p<0.001p<0.001.



|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bidder 0x8c6f | | Bidder 0x95c0 | |
| Variable | Reduced | Full | Reduced | Full |
| Panel A: Location Coefficients | | | | |
| Intercept (θ0\theta\_{0}) | 0.9239∗∗∗ | 0.8976∗∗∗ | 0.9783∗∗∗ | 0.9646∗∗∗ |
|  | (0.0024) | (0.0025) | (0.0019) | (0.0027) |
| 𝔼​[I​V]/P\mathbb{E}[IV]/\sqrt{P} (θ1\theta\_{1}) | 0.4234∗∗∗ | 0.4306∗∗∗ | 0.5134∗∗∗ | 0.5318∗∗∗ |
|  | (0.0012) | (0.0013) | (0.0011) | (0.0013) |
| Var​(I​V)\text{Var}(IV) (θ2\theta\_{2}) | – | -0.9335∗∗∗ | – | -1.7999∗∗∗ |
|  | – | (0.0279) | – | (0.0364) |
| Panel B: Scale Coefficients | | | | |
| Intercept (γ0\gamma\_{0}) | -0.2747∗∗∗ | -1.6680∗∗∗ | 0.1052∗∗∗ | -0.8891∗∗∗ |
|  | (0.0048) | (0.0260) | (0.0042) | (0.0235) |
| log⁡(𝔼​[I​V]/P)\log(\mathbb{E}[IV]/\sqrt{P}) (γ1\gamma\_{1}) | 0.6417∗∗∗ | 0.9775∗∗∗ | 0.5029∗∗∗ | 0.7404∗∗∗ |
|  | (0.0020) | (0.0065) | (0.0017) | (0.0059) |
| log⁡(Var​(I​V))\log(\text{Var}(IV)) (γ2\gamma\_{2}) | – | -0.1976∗∗∗ | – | -0.1418∗∗∗ |
|  | – | (0.0036) | – | (0.0032) |
| Panel C: Model Fit Statistics | | | | |
| Observations | 264958 | 264958 | 264958 | 264958 |
| Censored | 264958 | 264958 | 264958 | 264958 |
| Student tt ν\nu | 1.54 | 1.61 | 2.09 | 2.22 |
| Log Likelihood | -685494.19 | -683003.61 | -676359.13 | -672856.17 |
| AIC | 1370998.37 | 1366021.22 | 1352728.26 | 1345726.35 |
| BIC | 1371050.81 | 1366094.63 | 1352780.70 | 1345799.76 |
| McFadden R2R^{2} | 0.128 | 0.131 | 0.139 | 0.144 |
| Panel D: Full vs Reduced Model Comparison | | | | |
| Δ\Delta AIC (Full - Reduced) | -4977.15 | | -7001.92 | |
| Δ\Delta BIC (Full - Reduced) | -4956.18 | | -6980.94 | |
| LR Test χ2\chi^{2} (p-val) | 4981.15∗⁣∗∗4981.15^{\*\*\*} | | 7005.92∗⁣∗∗7005.92^{\*\*\*} | |

Table 4: Regression with Lagged IV estimators (Linear, t-dist Errors). p∗<0.05{}^{\*}p<0.05, p∗∗<0.01{}^{\*\*}p<0.01, p∗⁣∗∗<0.001{}^{\*\*\*}p<0.001.



|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bidder 0x8c6f | | Bidder 0x95c0 | |
| Variable | Reduced | Full | Reduced | Full |
| Panel A: Location Coefficients | | | | |
| Intercept (θ0\theta\_{0}) | 47.1042∗∗∗ | 47.0202∗∗∗ | 47.7172∗∗∗ | 47.7364∗∗∗ |
|  | (0.0285) | (0.0301) | (0.0249) | (0.0268) |
| log⁡(𝔼​[I​V]/P)\log(\mathbb{E}[IV]/\sqrt{P}) (θ1\theta\_{1}) | 0.5892∗∗∗ | 1.0764∗∗∗ | 0.6160∗∗∗ | 1.1954∗∗∗ |
|  | (0.0015) | (0.0045) | (0.0013) | (0.0041) |
| log⁡(Var​(I​V))\log(\text{Var}(IV)) (θ2\theta\_{2}) | – | -0.2937∗∗∗ | – | -0.3455∗∗∗ |
|  | – | (0.0026) | – | (0.0023) |
| Panel B: Scale Coefficients | | | | |
| Intercept (γ0\gamma\_{0}) | -0.6782∗∗∗ | -0.1254∗∗∗ | -1.4440∗∗∗ | -1.1117∗∗∗ |
|  | (0.0157) | (0.0196) | (0.0146) | (0.0190) |
| log⁡(𝔼​[I​V]/P)\log(\mathbb{E}[IV]/\sqrt{P}) (γ1\gamma\_{1}) | -0.0287∗∗∗ | 0.0391∗∗∗ | -0.0637∗∗∗ | -0.1032∗∗∗ |
|  | (0.0008) | (0.0036) | (0.0008) | (0.0036) |
| log⁡(Var​(I​V))\log(\text{Var}(IV)) (γ2\gamma\_{2}) | – | -0.0224∗∗∗ | – | 0.0353∗∗∗ |
|  | – | (0.0019) | – | (0.0019) |
| Panel C: Model Fit Statistics | | | | |
| Observations | 264958 | 264958 | 264958 | 264958 |
| Censored | 9151325 | 9151325 | 9151325 | 9151325 |
| Log Likelihood | -327469.69 | -320362.18 | -305628.46 | -294324.82 |
| AIC | 654947.38 | 640736.36 | 611264.92 | 588661.64 |
| BIC | 654989.33 | 640799.28 | 611306.86 | 588724.57 |
| McFadden R2R^{2} | 0.196 | 0.214 | 0.233 | 0.261 |
| Panel D: Full vs Reduced Model Comparison | | | | |
| Δ\Delta AIC (Full - Reduced) | -14211.02 | | -22603.27 | |
| Δ\Delta BIC (Full- Reduced) | -14190.04 | | -22582.30 | |
| LR Test χ2\chi^{2} (p-val) | 14215.02∗⁣∗∗14215.02^{\*\*\*} | | 22607.27∗⁣∗∗22607.27^{\*\*\*} | |

Table 5: Regression with Lagged IV estimators (Log-Log, Gaussian Errors). p∗<0.05{}^{\*}p<0.05, p∗∗<0.01{}^{\*\*}p<0.01, p∗⁣∗∗<0.001{}^{\*\*\*}p<0.001.