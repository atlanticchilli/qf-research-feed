---
authors:
- Joel Hasbrouck
- Julian Ma
- Fahad Saleh
- Caspar Schwarz-Schilling
doc_id: arxiv:2602.20771v1
family_id: arxiv:2602.20771
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Market Inefficiency in Cryptoasset Markets
url_abs: http://arxiv.org/abs/2602.20771v1
url_html: https://arxiv.org/html/2602.20771v1
venue: arXiv q-fin
version: 1
year: 2026
---


Joel Hasbrouck
Julian Ma
Fahad Saleh
Caspar Schwarz-Schilling


*NYU Stern*
*Ethereum Foundation*
*University of Florida*
*Ethereum Foundation*
email: jh4@stern.nyu.eduemail: julian.ma@ethereum.orgemail: fahad.saleh@ufl.eduemail: caspar.schwarz-schilling@ethereum.org

###### Abstract

We demonstrate market inefficiency in cryptoasset markets. Our approach examines investments that share a dominant risk factor but differ in their exposure to a secondary risk. We derive equilibrium restrictions that must hold regardless of how investors price either risk. Our empirical results strongly reject these necessary equilibrium restrictions. The rejection implies market inefficiency that cannot be attributed to mispriced risk, suggesting the presence of frictions that impede capital reallocation.

## 1 Introduction

We demonstrate market inefficiency in cryptoasset markets while allowing for arbitrary risk pricing. Our approach compares investments with similar risk and derives equilibrium restrictions that must hold regardless of how investors price risk. We then test these restrictions empirically. We show that necessary equilibrium restrictions are strongly rejected, thereby demonstrating market inefficiency.

To add more detail, we examine three investments involving ether (ETH), the native asset of the Ethereum blockchain. The first investment is direct staking: investors stake ETH on the Ethereum blockchain and earn staking yields. The second investment is lending ETH through a Decentralized Lending Protocol (DLP) which pays interest to lenders. The third investment is liquid staking: investors deposit ETH with a Staking Service Provider (SSP), receive an asset backed by the deposited ETH known as staked ether (stETH), and lend this stETH on a DLP for interest. This third investment earns both the staking yield (passed through by the SSP) and the stETH lending yield. Because stETH is redeemable for ETH, it trades near parity with ETH, and thus all three investments are primarily exposed to ETH price risk. Nonetheless, liquid staking carries an additional risk: the stETH-ETH exchange rate can deviate from unity, a phenomenon known as de-pegging. This de-peg risk is small in magnitude but nonzero and we account for it within our framework by allowing that investors price de-pegging risk.

Given the similar risk profiles of the three referenced investments, we derive tight equilibrium relationships relating their yields. To add some intuition, if capital can flow freely among the three investments, then an investor lending ETH at a DLP can withdraw that capital and pursue liquid staking or direct staking. In turn, if one investment becomes more attractive, capital will flow toward it until yields adjust to restore indifference across investments. This implies that changes in one yield must be accompanied by corresponding changes in the others, giving us testable equilibrium restrictions on relative yields. All three investments share the dominant risk factor (ETH price), and while liquid staking adds de-peg risk, we allow investors to price this additional risk arbitrarily. Because the equilibrium restrictions we derive hold for any price of de-peg risk, a rejection of these restrictions cannot be explained by investor de-peg risk pricing.

Our empirical tests examine whether yields co-move as necessary for equilibrium. We find that yields do not move in a manner consistent with equilibrium. The stETH lending yield shows almost no response to changes in the ETH lending yield or the staking yield differential. Both equilibrium restrictions are strongly rejected. The failure of yields to co-move as implied by equilibrium indicates that capital is not flowing among these investments freely, implying market inefficiency.

Our paper contributes to the literature on cryptoeconomics (John and Saleh, [2025](https://arxiv.org/html/2602.20771v1#bib.bib108 "Cryptoeconomics")), particularly the literature examining Ethereum’s Proof-of-Stake. This literature begins with Saleh ([2021](https://arxiv.org/html/2602.20771v1#bib.bib14 "Blockchain without waste: proof-of-stake")), which studies whether consensus arises in equilibrium. Several prominent works thereafter examine staking as an investment (Roşu and Saleh, [2021](https://arxiv.org/html/2602.20771v1#bib.bib16 "Evolution of shares in a proof-of-stake cryptocurrency"); Jermann, [2023](https://arxiv.org/html/2602.20771v1#bib.bib13 "A macro finance model for proof-of-stake ethereum"); Cong et al., [2025](https://arxiv.org/html/2602.20771v1#bib.bib112 "The tokenomics of staking"); John et al., [2025b](https://arxiv.org/html/2602.20771v1#bib.bib15 "Proof-of-work versus proof-of-stake: a comparative economic analysis"); Harvey et al., [2026](https://arxiv.org/html/2602.20771v1#bib.bib111 "Productivity enables security: the economics of blockchain settlement")). We extend that literature by abstracting from microeconomic details and developing general asset pricing restrictions. Using this framework, we are able to use the Ethereum ecosystem to test for market efficiency, highlighting that market efficiency fails.

## 2 Institutional Details

This section provides institutional background on Ethereum staking, liquid staking, and decentralized lending. We focus on the mechanisms relevant to our model, particularly those that determine yields and the relationship between ETH and stETH.

### 2.1 Ethereum Staking

The Ethereum blockchain uses a Proof-of-Stake consensus mechanism to secure its ledger (Saleh, [2021](https://arxiv.org/html/2602.20771v1#bib.bib14 "Blockchain without waste: proof-of-stake"); John et al., [2025b](https://arxiv.org/html/2602.20771v1#bib.bib15 "Proof-of-work versus proof-of-stake: a comparative economic analysis")). In Proof-of-Stake, a participant known as a *validator* locks capital in the form of ether (ETH) to participate in consensus. The Ethereum protocol requires a minimum of 32 ETH to become a validator. When selected by the protocol, validators propose blocks of transactions and attest to the validity of blocks proposed by others. In return for performing these duties, validators receive rewards from two sources (John et al., [2025a](https://arxiv.org/html/2602.20771v1#bib.bib10 "Economics of ethereum")). The first source is newly minted ETH, which corresponds to seigniorage. The protocol issues these rewards algorithmically, with the per-validator rate decreasing as more ETH is staked network-wide. The second source is transaction fees. Under Ethereum’s EIP-1559 fee mechanism (Roughgarden, [2021](https://arxiv.org/html/2602.20771v1#bib.bib104 "Transaction fee mechanism design")), users pay a base fee (which is burned) plus a priority fee (which goes to validators). Validators also capture *Maximal Extractable Value* (MEV), the profit available from reordering, inserting, or censoring transactions (Daian et al., [2020](https://arxiv.org/html/2602.20771v1#bib.bib105 "Flash boys 2.0: frontrunning in decentralized exchanges, miner extractable value, and consensus instability")).111Prominent examples of MEV include sandwich attacks (Park, [2023](https://arxiv.org/html/2602.20771v1#bib.bib94 "The conceptual flaws of decentralized automated market making")), stale price arbitrage (Capponi and Jia, [2025](https://arxiv.org/html/2602.20771v1#bib.bib87 "Liquidity provision on blockchain-based decentralized exchanges"); Lehar and Parlour, [2025](https://arxiv.org/html/2602.20771v1#bib.bib90 "Decentralized exchange: the uniswap automated market maker")), and JIT liquidity provision (Capponi et al., [2023](https://arxiv.org/html/2602.20771v1#bib.bib86 "The paradox of just-in-time liquidity in decentralized exchanges: more providers can sometimes mean less liquidity")). As an aside, in practice, specialized builders construct blocks to maximize MEV and bid for inclusion via proposer-builder separation mechanisms, transferring MEV to validators through priority fees (Schwarz-Schilling et al., [2023](https://arxiv.org/html/2602.20771v1#bib.bib106 "Time is money: strategic timing games in proof-of-stake protocols"); Capponi et al., [2024](https://arxiv.org/html/2602.20771v1#bib.bib107 "Proposer-builder separation, payment for order flows, and centralization in blockchain")).

The staking yield γtE​T​H\gamma^{ETH}\_{t} in our model corresponds to the rate at which validators accumulate rewards from both seigniorage and priority fees (including MEV). As of late 2025, approximately 34 million ETH is staked, corresponding to an annualized staking yield of approximately 3%. Importantly, the staking yield varies over time as the amount of staked ETH changes and as transaction fee revenue fluctuates with network activity. Our framework fully accommodates this time-variation, allowing that γtE​T​H\gamma^{ETH}\_{t} evolves stochastically.

### 2.2 Liquid Staking

The 32 ETH minimum and the technical requirements of running a validator node present barriers to direct staking. *Staking Service Providers* (SSPs) address these barriers by pooling capital from multiple users and operating validators on their behalf. Users deposit ETH with the SSP and receive a *Liquid Staking Token* (LST) in return. The LST represents a claim on the underlying staked ETH plus accumulated rewards.

Lido is the largest SSP, managing approximately 9.5 million ETH (around 28% of all staked ETH). Lido’s LST is called stETH. Lido’s operations are implemented via smart contracts, which are programs deployed on the Ethereum blockchain that execute automatically when called (John et al., [2023](https://arxiv.org/html/2602.20771v1#bib.bib24 "Smart contracts and decentralized finance")). When a user deposits ETH with Lido, the following occurs in a single atomic transaction: the user calls the submit() function on Lido’s deposit contract,222Lido stETH contract: <https://etherscan.io/address/0xae7ab96520de3a18e5e111b5eaab095312d7fe84> sending ETH to the contract; the contract mints stETH to the user’s address at a one-to-one ratio. The deposited ETH is then allocated to node operators who stake it with the Ethereum protocol.

Lido charges a 10% fee on all staking rewards, including both seigniorage and priority fees (and hence MEV). The remaining 90% accrues to stETH holders. In our model, γtE​T​H\gamma^{ETH}\_{t} denotes the full protocol staking yield (seigniorage plus priority fees), while γts​t​E​T​H\gamma^{stETH}\_{t} denotes the yield passed to stETH holders after Lido’s fee. Thus γts​t​E​T​H=0.9×γtE​T​H\gamma^{stETH}\_{t}=0.9\times\gamma^{ETH}\_{t}, and γts​t​E​T​H\gamma^{stETH}\_{t} inherits the time-variation of the underlying protocol yield.

Because stETH represents a claim on ETH held by Lido, it trades near parity with ETH. Holders can redeem stETH for ETH by calling the requestWithdrawals() function on Lido’s withdrawal contract.333Lido Withdrawal Queue contract: <https://etherscan.io/address/0x889edc2edab5f40e902b864ad4d7ade8e412f9b1> The redemption is subject to a delay due to Ethereum’s withdrawal queue, but once processed, holders receive ETH at the prevailing exchange rate within the protocol. This redeemability anchors the stETH price to ETH.

However, the stETH-ETH exchange rate can deviate from unity. We refer to such deviations as *de-pegging*. In our model, the variable χt\chi\_{t} captures the log stETH-ETH price ratio, with χt=0\chi\_{t}=0 corresponding to parity and χt<0\chi\_{t}<0 corresponding to stETH trading at a discount.

### 2.3 Decentralized Lending

Decentralized Lending Protocols (DLPs) enable users to lend and borrow cryptoassets via smart contracts (Gudgeon et al., [2020](https://arxiv.org/html/2602.20771v1#bib.bib103 "DeFi protocols for loanable funds: interest rates, liquidity and market efficiency")). Aave is the largest DLP on Ethereum, with over 40 billion USD in deposits. Users can supply assets to Aave’s liquidity pools and earn interest from borrowers.

To supply ETH to Aave, a user calls the supply() function on Aave’s pool contract,444Aave V3 Pool contract: <https://etherscan.io/address/0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2> specifying the amount and the asset. The contract transfers ETH from the user and mints *aTokens* (specifically, aWETH for ETH) to the user’s address. These aTokens represent the user’s claim on the supplied assets plus accrued interest. The interest rate paid to suppliers is determined algorithmically based on the utilization rate of the pool: when demand for borrowing is high relative to supply, the interest rate increases; when demand is low, the rate decreases (Rivera et al., [2023](https://arxiv.org/html/2602.20771v1#bib.bib102 "Equilibrium in a defi lending market")).

Aave also supports stETH as a supplied asset. Users holding stETH can supply it to Aave and earn the stETH lending yield ψts​t​E​T​H\psi^{stETH}\_{t} in addition to the staking yield γts​t​E​T​H\gamma^{stETH}\_{t} that accrues to stETH holders. Similarly, users can supply ETH to earn the ETH lending yield ψtE​T​H\psi^{ETH}\_{t}. The yields ψtE​T​H\psi^{ETH}\_{t} and ψts​t​E​T​H\psi^{stETH}\_{t} in our model correspond to the supply rates offered by Aave for ETH and stETH, respectively. Because utilization rates fluctuate with market conditions, these lending yields vary dynamically. Our framework fully accommodates this time-variation, allowing that ψtE​T​H\psi^{ETH}\_{t} and ψts​t​E​T​H\psi^{stETH}\_{t} may evolve stochastically.

All interactions with Aave occur through smart contracts, ensuring that the terms of lending are enforced programmatically. Borrowers must post collateral exceeding the value of their loans, and the protocol automatically adjusts interest rates based on market conditions. This transparency and automation allow us to observe lending yields directly from on-chain data.

## 3 Economic Model

We examine an infinite horizon setting where time is indexed by t∈{0,1,2,…}t\in\{0,1,2,\ldots\} and ℱt\mathcal{F}\_{t} denotes the information available at time tt. We examine three investment strategies available to ether (ETH) holders in each period: direct staking, lending via decentralized lending protocols, and liquid staking. We first describe the return structure of each strategy, then introduce the pricing framework, and finally derive equilibrium restrictions.

### 3.1 Investment Opportunities

#### 3.1.1 Direct Staking

Investors holding ETH can earn yield by staking, which involves locking ETH to participate in Ethereum’s proof-of-stake consensus protocol (John et al., [2025a](https://arxiv.org/html/2602.20771v1#bib.bib10 "Economics of ethereum")). The gross return from holding and staking ETH is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt,t+1E​T​H,s​t​a​k​e=exp⁡{γtE​T​H−κ+rt,t+1E​T​H}R^{ETH,stake}\_{t,t+1}=\exp\{\gamma^{ETH}\_{t}-\kappa+r^{ETH}\_{t,t+1}\} |  | (1) |

where rt,t+1E​T​Hr^{ETH}\_{t,t+1} denotes the period-tt to period-t+1t+1 log price return on ETH, γtE​T​H\gamma^{ETH}\_{t} denotes the log staking yield over the same period, and κ>0\kappa>0 denotes the cost of staking. The investor earns both the price appreciation and the staking yield, net of costs.

#### 3.1.2 Lending ETH

Alternatively, investors can deploy ETH in decentralized lending protocols such as Aave. The gross return from holding and lending ETH is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt,t+1E​T​H,l​e​n​d=exp⁡{ψtE​T​H+rt,t+1E​T​H}R^{ETH,lend}\_{t,t+1}=\exp\{\psi\_{t}^{ETH}+r^{ETH}\_{t,t+1}\} |  | (2) |

where ψtE​T​H\psi^{ETH}\_{t} denotes the period-tt to period-t+1t+1 log lending yield. The investor earns both the price appreciation and the lending yield.

#### 3.1.3 Liquid Staking

Investors can obtain exposure to staking yield through liquid staking tokens (LSTs). To acquire stETH, an investor deposits ETH with a staking service such as Lido and receives stETH one-for-one. The staking service stakes the deposited ETH and passes a fraction of the staking yield to stETH holders. Additionally, the investor can lend their stETH in protocols like Aave. The gross return from this combined strategy is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt,t+1s​t​E​T​H=exp⁡{γts​t​E​T​H+ψts​t​E​T​H+rt,t+1s​t​E​T​H}R^{stETH}\_{t,t+1}=\exp\{\gamma^{stETH}\_{t}+\psi^{stETH}\_{t}+r^{stETH}\_{t,t+1}\} |  | (3) |

where γts​t​E​T​H\gamma^{stETH}\_{t} denotes the log staking yield passed to stETH holders (net of the staking service’s fee), ψts​t​E​T​H\psi^{stETH}\_{t} denotes the log lending yield on stETH, and rt,t+1s​t​E​T​Hr^{stETH}\_{t,t+1} denotes the log price return on stETH.

The stETH price return is linked to the ETH price return through the stETH-ETH exchange rate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt,t+1s​t​E​T​H=rt,t+1E​T​H+χt+1−χtr^{stETH}\_{t,t+1}=r^{ETH}\_{t,t+1}+\chi\_{t+1}-\chi\_{t} |  | (4) |

where χt:=log⁡(Pts​t​E​T​H/PtE​T​H)\chi\_{t}:=\log(P^{stETH}\_{t}/P^{ETH}\_{t}) is the log stETH-ETH price ratio. Thus, stETH returns inherit ETH price risk plus any changes in the exchange rate.

#### 3.1.4 Peg Risk

The stETH-ETH exchange rate χt\chi\_{t} introduces additional risk. We model {χt}t=0∞\{\chi\_{t}\}\_{t=0}^{\infty} as a two-state Markov chain with states {0,−η}\{0,-\eta\} where η>0\eta>0. The state χt=0\chi\_{t}=0 corresponds to parity (stETH trades at par with ETH), while χt=−η\chi\_{t}=-\eta corresponds to a significant discount. We focus on two states because small deviations from parity are statistically indistinguishable from parity given market microstructure noise. The transition matrix under the physical measure is:

|  |  |  |
| --- | --- | --- |
|  | P=[p0,01−p0,01−pη,ηpη,η]P=\begin{bmatrix}p\_{0,0}&1-p\_{0,0}\\ 1-p\_{\eta,\eta}&p\_{\eta,\eta}\end{bmatrix} |  |

where p0,0p\_{0,0} is the probability of remaining at parity given the peg currently holds, and pη,ηp\_{\eta,\eta} is the probability of remaining at a discount given the peg is currently broken.

### 3.2 Asset Pricing Framework

We allow for arbitrary prices of risk and specify the pricing kernel as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λt,t+1=exp⁡(−rt,t+1−12​λE​T​H2−λE​T​H​εt+1E​T​H−λχ​ωt+1+ξt​(λχ))\Lambda\_{t,t+1}=\exp\left(-r\_{t,t+1}-\frac{1}{2}\lambda\_{ETH}^{2}-\lambda\_{ETH}\varepsilon^{ETH}\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\right) |  | (5) |

where rt,t+1r\_{t,t+1} denotes the risk-free rate, λE​T​H\lambda\_{ETH} is the market price of ETH risk, and λχ\lambda\_{\chi} is the market price of peg risk. The standardized ETH return innovation is εt+1E​T​H:=(rt,t+1E​T​H−μtE​T​H)/vtE​T​H\varepsilon^{ETH}\_{t+1}:=(r^{ETH}\_{t,t+1}-\mu\_{t}^{ETH})/\sqrt{v\_{t}^{ETH}}, where μtE​T​H:=𝔼​[rt,t+1E​T​H|ℱt]\mu\_{t}^{ETH}:=\mathbb{E}[r^{ETH}\_{t,t+1}|\mathcal{F}\_{t}] and vtE​T​H:=Var​[rt,t+1E​T​H|ℱt]v\_{t}^{ETH}:=\text{Var}[r^{ETH}\_{t,t+1}|\mathcal{F}\_{t}]. We assume εt+1E​T​H|ℱt∼N​(0,1)\varepsilon^{ETH}\_{t+1}|\mathcal{F}\_{t}\sim N(0,1) to ease exposition. The peg state indicator is ωt+1:=𝟏{χt+1=−η}\omega\_{t+1}:=\mathbf{1}\_{\{\chi\_{t+1}=-\eta\}}, and we assume εt+1E​T​H\varepsilon^{ETH}\_{t+1} and ωt+1\omega\_{t+1} are conditionally independent given ℱt\mathcal{F}\_{t}. The normalizing constant is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξt​(λχ):=−log⁡𝔼​[exp⁡{−λχ​ωt+1}|ℱt]\xi\_{t}(\lambda\_{\chi}):=-\log\mathbb{E}[\exp\{-\lambda\_{\chi}\omega\_{t+1}\}|\mathcal{F}\_{t}] |  | (6) |

We impose no arbitrage, implying:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Λt,t+1​Rt,t+1i|ℱt]=1\mathbb{E}[\Lambda\_{t,t+1}\,R^{i}\_{t,t+1}~|~\mathcal{F}\_{t}]=1 |  | (7) |

Equation ([7](https://arxiv.org/html/2602.20771v1#S3.E7 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) is the fundamental asset pricing equation (Harrison and Kreps, [1979](https://arxiv.org/html/2602.20771v1#bib.bib4 "Martingales and arbitrage in multiperiod securities markets"); Duffie, [2001](https://arxiv.org/html/2602.20771v1#bib.bib5 "Dynamic asset pricing theory")). The pricing kernel Λt,t+1\Lambda\_{t,t+1} reflects how investors value payoffs across different market outcomes: when Λt,t+1\Lambda\_{t,t+1} is high, a dollar is worth more to investors than when Λt,t+1\Lambda\_{t,t+1} is low. Our specification ([5](https://arxiv.org/html/2602.20771v1#S3.E5 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) incorporates two sources of risk: ETH price movements (through εt+1E​T​H\varepsilon^{ETH}\_{t+1}) and stETH de-pegging (through ωt+1\omega\_{t+1}). The parameters λE​T​H\lambda\_{ETH} and λχ\lambda\_{\chi} govern how these risks are priced. Mechanically, Λt,t+1\Lambda\_{t,t+1} decreases in λE​T​H​εt+1E​T​H\lambda\_{ETH}\varepsilon^{ETH}\_{t+1}: a larger λE​T​H\lambda\_{ETH} means the kernel assigns less weight to outcomes where εt+1E​T​H\varepsilon^{ETH}\_{t+1} is high. Consequently, an asset whose returns are positively correlated with εt+1E​T​H\varepsilon^{ETH}\_{t+1} receives a lower valuation, and must offer a higher expected return in compensation. The same concept applies to peg risk through λχ\lambda\_{\chi}. We leave both parameters unrestricted.

### 3.3 Equilibrium Restrictions

We now derive equilibrium restrictions by applying the pricing equation ([7](https://arxiv.org/html/2602.20771v1#S3.E7 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) to each investment opportunity.

###### Proposition 1 (ETH Staking).

The expected ETH return satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[rt,t+1E​T​H|ℱt]=rt,t+1+λE​T​H​vtE​T​H−γtE​T​H+κ−vtE​T​H2\mathbb{E}[r\_{t,t+1}^{ETH}~|~\mathcal{F}\_{t}]=r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}-\gamma^{ETH}\_{t}+\kappa-\frac{v\_{t}^{ETH}}{2} |  | (8) |

where vtE​T​H:=Var​[rt,t+1E​T​H|ℱt]v\_{t}^{ETH}:=\text{Var}[r\_{t,t+1}^{ETH}~|~\mathcal{F}\_{t}].

The term λE​T​H​vtE​T​H\lambda\_{ETH}\sqrt{v\_{t}^{ETH}} is the risk premium: investors require compensation for bearing ETH price risk. The staking yield γtE​T​H\gamma^{ETH}\_{t} reduces the required price return (staking provides additional compensation), while staking costs κ\kappa increase it. The term vtE​T​H/2v\_{t}^{ETH}/2 is a convexity adjustment.

###### Proposition 2 (ETH Lending).

The expected ETH return satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[rt,t+1E​T​H|ℱt]=rt,t+1+λE​T​H​vtE​T​H−ψtE​T​H−vtE​T​H2\mathbb{E}[r\_{t,t+1}^{ETH}~|~\mathcal{F}\_{t}]=r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}-\psi\_{t}^{ETH}-\frac{v\_{t}^{ETH}}{2} |  | (9) |

The interpretation parallels Proposition [1](https://arxiv.org/html/2602.20771v1#Thmproposition1 "Proposition 1 (ETH Staking). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets"): the lending yield ψtE​T​H\psi\_{t}^{ETH} substitutes for the staking yield as an additional source of return.

###### Proposition 3 (stETH Investment).

The expected ETH return satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[rt,t+1E​T​H|ℱt]=rt,t+1+λE​T​H​vtE​T​H+η~t−γts​t​E​T​H−ψts​t​E​T​H−vtE​T​H2\mathbb{E}[r\_{t,t+1}^{ETH}~|~\mathcal{F}\_{t}]=r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}+\tilde{\eta}\_{t}-\gamma^{stETH}\_{t}-\psi\_{t}^{stETH}-\frac{v\_{t}^{ETH}}{2} |  | (10) |

where η~t\tilde{\eta}\_{t} is the risk-adjusted peg premium:

|  |  |  |  |
| --- | --- | --- | --- |
|  | η~t={log⁡1e−η+p~0,0​(1−e−η)if ​χt=0log⁡1eη−p~η,η​(eη−1)if ​χt=−η\tilde{\eta}\_{t}=\begin{cases}\log{\frac{1}{e^{-\eta}+\tilde{p}\_{0,0}(1-e^{-\eta})}}&\text{if }\chi\_{t}=0\\[6.0pt] \log{\frac{1}{e^{\eta}-\tilde{p}\_{\eta,\eta}(e^{\eta}-1)}}&\text{if }\chi\_{t}=-\eta\end{cases} |  | (11) |

and the risk-adjusted transition probabilities, p~0,0\tilde{p}\_{0,0} and p~η,η\tilde{p}\_{\eta,\eta}, are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p~0,0=p0,0p0,0+(1−p0,0)​e−λχ\tilde{p}\_{0,0}=\frac{p\_{0,0}}{p\_{0,0}+(1-p\_{0,0})e^{-\lambda\_{\chi}}} |  | (12) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | p~η,η=pη,η​e−λχpη,η​e−λχ+(1−pη,η)\tilde{p}\_{\eta,\eta}=\frac{p\_{\eta,\eta}e^{-\lambda\_{\chi}}}{p\_{\eta,\eta}e^{-\lambda\_{\chi}}+(1-p\_{\eta,\eta})} |  | (13) |

The term η~t\tilde{\eta}\_{t} compensates investors for peg risk. When the peg holds (χt=0\chi\_{t}=0), investors face the risk of a future de-peg; when the peg is broken (χt=−η\chi\_{t}=-\eta), they face uncertainty about recovery. The risk-adjusted probabilities p~0,0\tilde{p}\_{0,0} and p~η,η\tilde{p}\_{\eta,\eta} incorporate the market price of peg risk λχ\lambda\_{\chi}.

### 3.4 Implied Equilibrium Relationships

Combining the restrictions from Propositions [1](https://arxiv.org/html/2602.20771v1#Thmproposition1 "Proposition 1 (ETH Staking). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")–[3](https://arxiv.org/html/2602.20771v1#Thmproposition3 "Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets") yields testable equilibrium relationships.

###### Proposition 4 (stETH Lending vs. ETH Staking).

In equilibrium:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψts​t​E​T​H=γtE​T​H−γts​t​E​T​H+η~t−κ\psi\_{t}^{stETH}=\gamma^{ETH}\_{t}-\gamma^{stETH}\_{t}+\tilde{\eta}\_{t}-\kappa |  | (14) |

This equation states that the stETH lending yield equals the ETH staking yield, minus the portion passed to stETH holders, plus compensation for peg risk, minus staking costs (which stETH holders avoid).

###### Proposition 5 (stETH Lending vs. ETH Lending).

In equilibrium:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψts​t​E​T​H=ψtE​T​H−γts​t​E​T​H+η~t\psi\_{t}^{stETH}=\psi^{ETH}\_{t}-\gamma^{stETH}\_{t}+\tilde{\eta}\_{t} |  | (15) |

This equation states that the stETH lending yield equals the ETH lending yield, minus the stETH staking yield (which stETH lenders also receive), plus compensation for peg risk. Crucially, staking costs κ\kappa do not appear because neither ETH lenders nor stETH lenders bear these costs directly.

## 4 Empirical Analysis

We test the equilibrium relationships derived in Propositions [4](https://arxiv.org/html/2602.20771v1#Thmproposition4 "Proposition 4 (stETH Lending vs. ETH Staking). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets") and [5](https://arxiv.org/html/2602.20771v1#Thmproposition5 "Proposition 5 (stETH Lending vs. ETH Lending). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets"). Both propositions imply exact relationships between observable yields. We find that the data strongly reject these relationships, indicating market inefficiency.

### 4.1 Data

We obtain daily data on lending yields from Aave and staking yields from Lido. Our sample spans January 30, 2023 to September 21, 2025, yielding 966 daily observations. Table [1](https://arxiv.org/html/2602.20771v1#S4.T1 "Table 1 ‣ 4.1 Data ‣ 4 Empirical Analysis ‣ Market Inefficiency in Cryptoasset Markets") presents summary statistics:

Table 1: Summary Statistics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Mean | Std. Dev. | Min | Max |
| ψE​T​H\psi^{ETH} (ETH lending yield) | 1.92% | 0.65% | 0.95% | 17.80% |
| ψs​t​E​T​H\psi^{stETH} (stETH lending yield) | 0.05% | 0.07% | 0.00% | 0.67% |
| γE​T​H\gamma^{ETH} (ETH staking yield) | 3.29% | 0.64% | 2.18% | 12.27% |
| γs​t​E​T​H\gamma^{stETH} (Lido staking yield) | 2.96% | 0.58% | 1.97% | 11.05% |
| stETH/ETH ratio | 0.999 | 0.001 | 0.990 | 1.015 |
| Observations | 966 | | | |
| Sample period | January 30, 2023 – September 21, 2025 | | | |

Notes: Yields are annualized. ψE​T​H\psi^{ETH} and ψs​t​E​T​H\psi^{stETH} are lending yields from Aave. γE​T​H\gamma^{ETH} is the Ethereum protocol staking yield. γs​t​E​T​H\gamma^{stETH} is the staking yield passed to Lido stETH holders (after Lido’s 10% fee). The stETH/ETH ratio is the daily average exchange rate.

### 4.2 Methodology

Given measurement error in the data, Proposition [4](https://arxiv.org/html/2602.20771v1#Thmproposition4 "Proposition 4 (stETH Lending vs. ETH Staking). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets") implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψts​t​E​T​H=α+β​(γtE​T​H−γts​t​E​T​H)+ϵt\psi\_{t}^{stETH}=\alpha+\beta\left(\gamma^{ETH}\_{t}-\gamma^{stETH}\_{t}\right)+\epsilon\_{t} |  | (16) |

where β=1\beta=1. Thus, to test market efficiency, we test:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0:β=1versusHA:β≠1H\_{0}:\beta=1\quad\text{versus}\quad H\_{A}:\beta\neq 1 |  | (17) |

Note that the regressor γE​T​H−γs​t​E​T​H\gamma^{ETH}-\gamma^{stETH} is the spread between the protocol staking yield and the yield that Lido passes through to stETH holders. Consider an investor deciding between two strategies: direct staking, which earns the full protocol yield γE​T​H\gamma^{ETH}, or liquid staking through Lido, which earns the Lido yield γs​t​E​T​H\gamma^{stETH} plus whatever can be earned by lending the stETH at Aave, ψs​t​E​T​H\psi^{stETH}. In equilibrium, these strategies must offer comparable returns. If the spread γE​T​H−γs​t​E​T​H\gamma^{ETH}-\gamma^{stETH} increases, then direct staking becomes more attractive. For liquid staking to remain competitive, the stETH lending yield ψs​t​E​T​H\psi^{stETH} must rise by the same amount. If it does not, capital will flow out of liquid staking and into direct staking until yields adjust. More formally, this one-for-one relationship is an implication from Proposition [4](https://arxiv.org/html/2602.20771v1#Thmproposition4 "Proposition 4 (stETH Lending vs. ETH Staking). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").

Similarly, Proposition [5](https://arxiv.org/html/2602.20771v1#Thmproposition5 "Proposition 5 (stETH Lending vs. ETH Lending). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets") implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψts​t​E​T​H=α+β​(ψtE​T​H−γts​t​E​T​H)+ϵt\psi\_{t}^{stETH}=\alpha+\beta\left(\psi^{ETH}\_{t}-\gamma^{stETH}\_{t}\right)+\epsilon\_{t} |  | (18) |

where β=1\beta=1. Thus, to test market efficiency, we test:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0:β=1versusHA:β≠1H\_{0}:\beta=1\quad\text{versus}\quad H\_{A}:\beta\neq 1 |  | (19) |

The regressor ψE​T​H−γs​t​E​T​H\psi^{ETH}-\gamma^{stETH} compares the ETH lending yield to the staking component of the liquid staking strategy. Consider an investor choosing between lending ETH at Aave, which earns ψE​T​H\psi^{ETH}, or pursuing the liquid staking strategy, which earns the Lido staking yield γs​t​E​T​H\gamma^{stETH} plus the stETH lending yield ψs​t​E​T​H\psi^{stETH}. If ψE​T​H−γs​t​E​T​H\psi^{ETH}-\gamma^{stETH} increases, then direct ETH lending becomes more attractive relative to the staking component of liquid staking. For the liquid staking strategy to remain competitive, the stETH lending yield must rise by the same amount. More formally, this one-for-one adjustment is an implication from Proposition [5](https://arxiv.org/html/2602.20771v1#Thmproposition5 "Proposition 5 (stETH Lending vs. ETH Lending). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").

Since our model allows for arbitrary risk pricing, a rejection of β=1\beta=1 cannot be attributed to mispriced risk. Rather, it implies a failure of market efficiency. We estimate both regressions with heteroskedasticity and autocorrelation consistent (HAC) standard errors using the Newey-West estimator with 10 lags.

### 4.3 Results

Table [2](https://arxiv.org/html/2602.20771v1#S4.T2 "Table 2 ‣ 4.3 Results ‣ 4 Empirical Analysis ‣ Market Inefficiency in Cryptoasset Markets") presents our results. Both tests strongly reject market efficiency. We discuss each result in turn.

Table 2: Tests of Market Efficiency

|  |  |  |
| --- | --- | --- |
|  | Proposition [4](https://arxiv.org/html/2602.20771v1#Thmproposition4 "Proposition 4 (stETH Lending vs. ETH Staking). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets") | Proposition [5](https://arxiv.org/html/2602.20771v1#Thmproposition5 "Proposition 5 (stETH Lending vs. ETH Lending). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets") |
|  | γE​T​H−γs​t​E​T​H\gamma^{ETH}-\gamma^{stETH} | ψE​T​H−γs​t​E​T​H\psi^{ETH}-\gamma^{stETH} |
| β^\hat{\beta} | −0.228-0.228 | 0.0170.017 |
|  | (0.043)(0.043) | (0.005)(0.005) |
| α^\hat{\alpha} (annualized) | 0.12%0.12\% | 0.06%0.06\% |
|  | (0.02%)(0.02\%) | (0.01%)(0.01\%) |
| tt-statistic (H0:β=1H\_{0}:\beta=1) | −28.33-28.33 | −179.22-179.22 |
| pp-value | <0.001<0.001 | <0.001<0.001 |
| R2R^{2} | 0.1430.143 | 0.1200.120 |
| Observations | 966 | 966 |

Notes: The dependent variable is the daily stETH lending yield ψs​t​E​T​H\psi^{stETH}. HAC standard errors (Newey-West, 10 lags) in parentheses. Under market efficiency, β=1\beta=1. Both tests reject this hypothesis at the 1% level.

For the test of Proposition [4](https://arxiv.org/html/2602.20771v1#Thmproposition4 "Proposition 4 (stETH Lending vs. ETH Staking). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets"), the estimated coefficient is β^=−0.228\hat{\beta}=-0.228, which is not only significantly different from unity but is negative. This implies that when the staking yield differential γE​T​H−γs​t​E​T​H\gamma^{ETH}-\gamma^{stETH} increases, the stETH lending yield ψs​t​E​T​H\psi^{stETH} actually decreases, contrary to the theoretical prediction.

For the test of Proposition [5](https://arxiv.org/html/2602.20771v1#Thmproposition5 "Proposition 5 (stETH Lending vs. ETH Lending). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets"), the estimated coefficient is β^=0.017\hat{\beta}=0.017. While positive, this is far below the predicted value of unity. A one percentage point increase in ψE​T​H−γs​t​E​T​H\psi^{ETH}-\gamma^{stETH} is associated with only a 0.017 percentage point increase in ψs​t​E​T​H\psi^{stETH}, rather than the one-for-one relationship implied by market efficiency.

## 5 Conclusion

This paper demonstrates market inefficiency in cryptoasset markets while allowing for arbitrary risk pricing. We examine three investments: direct staking, lending via decentralized protocols, and liquid staking. Allowing for arbitrary risk pricing, we derive equilibrium restrictions that must hold regardless of how investors price risk. Our empirical tests strongly reject these equilibrium restrictions, implying market inefficiency. Ultimately, our findings suggest the presence of market frictions that impede capital reallocation across investments. The nature of these frictions remains an open question for future research.

## References

* A. Capponi, R. Jia, and S. Olafsson (2024)
  Proposer-builder separation, payment for order flows, and centralization in blockchain.
  Note: Working paper, <https://ssrn.com/abstract=4723674>
  Cited by: [§2.1](https://arxiv.org/html/2602.20771v1#S2.SS1.p1.1 "2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* A. Capponi, R. Jia, and B. Zhu (2023)
  The paradox of just-in-time liquidity in decentralized exchanges: more providers can sometimes mean less liquidity.
  Available at SSRN.
  Cited by: [footnote 1](https://arxiv.org/html/2602.20771v1#footnote1 "In 2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* A. Capponi and R. Jia (2025)
  Liquidity provision on blockchain-based decentralized exchanges.
  Review of Financial Studies.
  Note: Forthcoming
  Cited by: [footnote 1](https://arxiv.org/html/2602.20771v1#footnote1 "In 2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* L. W. Cong, Z. He, and K. Tang (2025)
  The tokenomics of staking.
  NBER Working Paper (33640).
  Cited by: [§1](https://arxiv.org/html/2602.20771v1#S1.p5.1 "1 Introduction ‣ Market Inefficiency in Cryptoasset Markets").
* P. Daian, S. Goldfeder, T. Kell, Y. Li, X. Zhao, I. Bentov, L. Breidenbach, and A. Juels (2020)
  Flash boys 2.0: frontrunning in decentralized exchanges, miner extractable value, and consensus instability.
  In 2020 IEEE Symposium on Security and Privacy,
   pp. 910–927.
  Cited by: [§2.1](https://arxiv.org/html/2602.20771v1#S2.SS1.p1.1 "2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* D. Duffie (2001)
  Dynamic asset pricing theory.
  3rd edition, Princeton University Press.
  Cited by: [§3.2](https://arxiv.org/html/2602.20771v1#S3.SS2.p2.13 "3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").
* L. Gudgeon, S. M. Werner, D. Perez, and W. J. Knottenbelt (2020)
  DeFi protocols for loanable funds: interest rates, liquidity and market efficiency.
  In Proceedings of the 2nd ACM Conference on Advances in Financial Technologies,
   pp. 92–112.
  Cited by: [§2.3](https://arxiv.org/html/2602.20771v1#S2.SS3.p1.1 "2.3 Decentralized Lending ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* J. M. Harrison and D. M. Kreps (1979)
  Martingales and arbitrage in multiperiod securities markets.
  Journal of Economic theory 20 (3),  pp. 381–408.
  Cited by: [§3.2](https://arxiv.org/html/2602.20771v1#S3.SS2.p2.13 "3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").
* C. R. Harvey, K. John, and F. Saleh (2026)
  Productivity enables security: the economics of blockchain settlement.
  Note: Working paper
  Cited by: [§1](https://arxiv.org/html/2602.20771v1#S1.p5.1 "1 Introduction ‣ Market Inefficiency in Cryptoasset Markets").
* U. J. Jermann (2023)
  A macro finance model for proof-of-stake ethereum.
  Available at SSRN 4335835.
  Cited by: [§1](https://arxiv.org/html/2602.20771v1#S1.p5.1 "1 Introduction ‣ Market Inefficiency in Cryptoasset Markets").
* K. John, L. Kogan, and F. Saleh (2023)
  Smart contracts and decentralized finance.
  Annual Review of Financial Economics 15 (1),  pp. 523–542.
  Cited by: [§2.2](https://arxiv.org/html/2602.20771v1#S2.SS2.p2.1 "2.2 Liquid Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* K. John, B. Monnot, P. Mueller, F. Saleh, and C. Schwarz-Schilling (2025a)
  Economics of ethereum.
  Journal of Corporate Finance 91,  pp. 102718.
  Cited by: [§2.1](https://arxiv.org/html/2602.20771v1#S2.SS1.p1.1 "2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets"),
  [§3.1.1](https://arxiv.org/html/2602.20771v1#S3.SS1.SSS1.p1.6 "3.1.1 Direct Staking ‣ 3.1 Investment Opportunities ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").
* K. John, T. J. Rivera, and F. Saleh (2025b)
  Proof-of-work versus proof-of-stake: a comparative economic analysis.
  Review of Financial Studies.
  Note: Forthcoming
  Cited by: [§1](https://arxiv.org/html/2602.20771v1#S1.p5.1 "1 Introduction ‣ Market Inefficiency in Cryptoasset Markets"),
  [§2.1](https://arxiv.org/html/2602.20771v1#S2.SS1.p1.1 "2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* K. John and F. Saleh (2025)
  Cryptoeconomics.
  Oxford Research Encyclopedia of Economics and Finance.
  Cited by: [§1](https://arxiv.org/html/2602.20771v1#S1.p5.1 "1 Introduction ‣ Market Inefficiency in Cryptoasset Markets").
* A. Lehar and C. A. Parlour (2025)
  Decentralized exchange: the uniswap automated market maker.
  Journal of Finance 80 (1),  pp. 321–374.
  Cited by: [footnote 1](https://arxiv.org/html/2602.20771v1#footnote1 "In 2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* A. Park (2023)
  The conceptual flaws of decentralized automated market making.
  Management Science 69 (11),  pp. 6731–6751.
  Cited by: [footnote 1](https://arxiv.org/html/2602.20771v1#footnote1 "In 2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* T. J. Rivera, F. Saleh, and Q. Vandeweyer (2023)
  Equilibrium in a defi lending market.
  Note: <https://ssrn.com/abstract=4389890>
  Cited by: [§2.3](https://arxiv.org/html/2602.20771v1#S2.SS3.p2.1 "2.3 Decentralized Lending ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* I. Roşu and F. Saleh (2021)
  Evolution of shares in a proof-of-stake cryptocurrency.
  Management Science 67 (2),  pp. 661–672.
  Cited by: [§1](https://arxiv.org/html/2602.20771v1#S1.p5.1 "1 Introduction ‣ Market Inefficiency in Cryptoasset Markets").
* T. Roughgarden (2021)
  Transaction fee mechanism design.
  In Proceedings of the 22nd ACM Conference on Economics and Computation,
   pp. 792–812.
  Cited by: [§2.1](https://arxiv.org/html/2602.20771v1#S2.SS1.p1.1 "2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* F. Saleh (2021)
  Blockchain without waste: proof-of-stake.
  The Review of financial studies 34 (3),  pp. 1156–1190.
  Cited by: [§1](https://arxiv.org/html/2602.20771v1#S1.p5.1 "1 Introduction ‣ Market Inefficiency in Cryptoasset Markets"),
  [§2.1](https://arxiv.org/html/2602.20771v1#S2.SS1.p1.1 "2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").
* C. Schwarz-Schilling, F. Saleh, T. Thiery, J. Pan, N. Shah, and B. Monnot (2023)
  Time is money: strategic timing games in proof-of-stake protocols.
  In 5th Conference on Advances in Financial Technologies (AFT 2023),
   pp. 30:1–30:17.
  Cited by: [§2.1](https://arxiv.org/html/2602.20771v1#S2.SS1.p1.1 "2.1 Ethereum Staking ‣ 2 Institutional Details ‣ Market Inefficiency in Cryptoasset Markets").

## Appendix A Proofs

###### Lemma 1.

Let yty\_{t} be ℱt\mathcal{F}\_{t}-measurable. If the return Rt,t+1=exp⁡{yt+rt,t+1E​T​H}R\_{t,t+1}=\exp\{y\_{t}+r^{ETH}\_{t,t+1}\} satisfies the Euler equation ([7](https://arxiv.org/html/2602.20771v1#S3.E7 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")), then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[rt,t+1E​T​H|ℱt]=rt,t+1+λE​T​H​vtE​T​H−yt−vtE​T​H2.\mathbb{E}[r^{ETH}\_{t,t+1}|\mathcal{F}\_{t}]=r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}-y\_{t}-\frac{v\_{t}^{ETH}}{2}. |  | (20) |

###### Proof.

The Euler equation ([7](https://arxiv.org/html/2602.20771v1#S3.E7 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) requires:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Λt,t+1​exp⁡{yt+rt,t+1E​T​H}|ℱt]=1.\mathbb{E}\left[\Lambda\_{t,t+1}\exp\{y\_{t}+r^{ETH}\_{t,t+1}\}~\Big|~\mathcal{F}\_{t}\right]=1. |  | (21) |

Substituting the pricing kernel ([5](https://arxiv.org/html/2602.20771v1#S3.E5 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) and factoring out ℱt\mathcal{F}\_{t}-measurable terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡{−rt,t+1−12​λE​T​H2+yt}⋅𝔼​[exp⁡{rt,t+1E​T​H−λE​T​H​εt+1E​T​H−λχ​ωt+1+ξt​(λχ)}|ℱt]=1.\exp\left\{-r\_{t,t+1}-\tfrac{1}{2}\lambda\_{ETH}^{2}+y\_{t}\right\}\cdot\mathbb{E}\left[\exp\left\{r^{ETH}\_{t,t+1}-\lambda\_{ETH}\varepsilon^{ETH}\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\right\}~\Big|~\mathcal{F}\_{t}\right]=1. |  | (22) |

By the definition of εt+1E​T​H\varepsilon^{ETH}\_{t+1}, we have rt,t+1E​T​H=μtE​T​H+vtE​T​H​εt+1E​T​Hr^{ETH}\_{t,t+1}=\mu\_{t}^{ETH}+\sqrt{v\_{t}^{ETH}}\,\varepsilon^{ETH}\_{t+1}. Substituting:

|  |  |  |
| --- | --- | --- |
|  | rt,t+1E​T​H−λE​T​H​εt+1E​T​H=μtE​T​H+(vtE​T​H−λE​T​H)​εt+1E​T​H.r^{ETH}\_{t,t+1}-\lambda\_{ETH}\varepsilon^{ETH}\_{t+1}=\mu\_{t}^{ETH}+(\sqrt{v\_{t}^{ETH}}-\lambda\_{ETH})\varepsilon^{ETH}\_{t+1}. |  |

By independence of εt+1E​T​H\varepsilon^{ETH}\_{t+1} and ωt+1\omega\_{t+1}, the conditional expectation in ([22](https://arxiv.org/html/2602.20771v1#A1.E22 "In Proof. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")) factors:

|  |  |  |
| --- | --- | --- |
|  | exp⁡{μtE​T​H}⋅𝔼​[exp⁡{(vtE​T​H−λE​T​H)​εt+1E​T​H}|ℱt]⋅𝔼​[exp⁡{−λχ​ωt+1+ξt​(λχ)}|ℱt].\exp\{\mu\_{t}^{ETH}\}\cdot\mathbb{E}\left[\exp\{(\sqrt{v\_{t}^{ETH}}-\lambda\_{ETH})\varepsilon^{ETH}\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]\cdot\mathbb{E}\left[\exp\{-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}~\Big|~\mathcal{F}\_{t}\right]. |  |

Since εt+1E​T​H|ℱt∼N​(0,1)\varepsilon^{ETH}\_{t+1}|\mathcal{F}\_{t}\sim N(0,1), the moment generating function gives:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{(vtE​T​H−λE​T​H)​εt+1E​T​H}|ℱt]=exp⁡{12​(vtE​T​H−λE​T​H)2}.\mathbb{E}\left[\exp\{(\sqrt{v\_{t}^{ETH}}-\lambda\_{ETH})\varepsilon^{ETH}\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]=\exp\left\{\tfrac{1}{2}(\sqrt{v\_{t}^{ETH}}-\lambda\_{ETH})^{2}\right\}. |  |

The normalizing constant ξt​(λχ)\xi\_{t}(\lambda\_{\chi}) is defined such that 𝔼​[exp⁡{−λχ​ωt+1+ξt​(λχ)}|ℱt]=1\mathbb{E}[\exp\{-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}|\mathcal{F}\_{t}]=1. Substituting these results into ([22](https://arxiv.org/html/2602.20771v1#A1.E22 "In Proof. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")) and taking logarithms:

|  |  |  |
| --- | --- | --- |
|  | −rt,t+1−12​λE​T​H2+yt+μtE​T​H+12​(vtE​T​H−λE​T​H)2=0.-r\_{t,t+1}-\tfrac{1}{2}\lambda\_{ETH}^{2}+y\_{t}+\mu\_{t}^{ETH}+\tfrac{1}{2}(\sqrt{v\_{t}^{ETH}}-\lambda\_{ETH})^{2}=0. |  |

Solving for μtE​T​H=𝔼​[rt,t+1E​T​H|ℱt]\mu\_{t}^{ETH}=\mathbb{E}[r^{ETH}\_{t,t+1}|\mathcal{F}\_{t}] gives ([20](https://arxiv.org/html/2602.20771v1#A1.E20 "In Lemma 1. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")).
∎

###### Proof of Proposition [1](https://arxiv.org/html/2602.20771v1#Thmproposition1 "Proposition 1 (ETH Staking). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").

The staking return ([1](https://arxiv.org/html/2602.20771v1#S3.E1 "In 3.1.1 Direct Staking ‣ 3.1 Investment Opportunities ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) has the form Rt,t+1=exp⁡{yt+rt,t+1E​T​H}R\_{t,t+1}=\exp\{y\_{t}+r^{ETH}\_{t,t+1}\} with yt=γtE​T​H−κy\_{t}=\gamma^{ETH}\_{t}-\kappa. Since γtE​T​H\gamma^{ETH}\_{t} and κ\kappa are ℱt\mathcal{F}\_{t}-measurable, Lemma [1](https://arxiv.org/html/2602.20771v1#Thmlemma1 "Lemma 1. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets") applies. Substituting yt=γtE​T​H−κy\_{t}=\gamma^{ETH}\_{t}-\kappa into ([20](https://arxiv.org/html/2602.20771v1#A1.E20 "In Lemma 1. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")) gives ([8](https://arxiv.org/html/2602.20771v1#S3.E8 "In Proposition 1 (ETH Staking). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")).
∎

###### Proof of Proposition [2](https://arxiv.org/html/2602.20771v1#Thmproposition2 "Proposition 2 (ETH Lending). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").

The lending return ([2](https://arxiv.org/html/2602.20771v1#S3.E2 "In 3.1.2 Lending ETH ‣ 3.1 Investment Opportunities ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) has the form Rt,t+1=exp⁡{yt+rt,t+1E​T​H}R\_{t,t+1}=\exp\{y\_{t}+r^{ETH}\_{t,t+1}\} with yt=ψtE​T​Hy\_{t}=\psi\_{t}^{ETH}. Since ψtE​T​H\psi\_{t}^{ETH} is ℱt\mathcal{F}\_{t}-measurable, Lemma [1](https://arxiv.org/html/2602.20771v1#Thmlemma1 "Lemma 1. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets") applies. Substituting yt=ψtE​T​Hy\_{t}=\psi\_{t}^{ETH} into ([20](https://arxiv.org/html/2602.20771v1#A1.E20 "In Lemma 1. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")) gives ([9](https://arxiv.org/html/2602.20771v1#S3.E9 "In Proposition 2 (ETH Lending). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")).
∎

###### Lemma 2.

Let η~t\tilde{\eta}\_{t} be defined by ([11](https://arxiv.org/html/2602.20771v1#S3.E11 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")). Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[exp⁡{χt+1−λχ​ωt+1+ξt​(λχ)}|ℱt]=exp⁡{χt−η~t}.\mathbb{E}\left[\exp\{\chi\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}~\Big|~\mathcal{F}\_{t}\right]=\exp\{\chi\_{t}-\tilde{\eta}\_{t}\}. |  | (23) |

###### Proof.

We verify ([23](https://arxiv.org/html/2602.20771v1#A1.E23 "In Lemma 2. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")) for each state χt∈{0,−η}\chi\_{t}\in\{0,-\eta\}.

Case χt=0\chi\_{t}=0: The state χt+1∈{0,−η}\chi\_{t+1}\in\{0,-\eta\} with physical probabilities p0,0p\_{0,0} and 1−p0,01-p\_{0,0}. By definition, ωt+1=1\omega\_{t+1}=1 when χt+1=−η\chi\_{t+1}=-\eta. Evaluating the conditional expectation:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{χt+1−λχ​ωt+1+ξt​(λχ)}|χt=0]=eξt​(λχ)​[p0,0⋅1+(1−p0,0)⋅e−η−λχ].\mathbb{E}\left[\exp\{\chi\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}~\Big|~\chi\_{t}=0\right]=e^{\xi\_{t}(\lambda\_{\chi})}\left[p\_{0,0}\cdot 1+(1-p\_{0,0})\cdot e^{-\eta-\lambda\_{\chi}}\right]. |  |

The normalizing constant satisfies 𝔼​[exp⁡{−λχ​ωt+1+ξt​(λχ)}|χt=0]=1\mathbb{E}[\exp\{-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}|\chi\_{t}=0]=1, which gives eξt​(λχ)=[p0,0+(1−p0,0)​e−λχ]−1e^{\xi\_{t}(\lambda\_{\chi})}=[p\_{0,0}+(1-p\_{0,0})e^{-\lambda\_{\chi}}]^{-1}. Substituting:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{χt+1−λχ​ωt+1+ξt​(λχ)}|χt=0]=p0,0+(1−p0,0)​e−η−λχp0,0+(1−p0,0)​e−λχ.\mathbb{E}\left[\exp\{\chi\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}~\Big|~\chi\_{t}=0\right]=\frac{p\_{0,0}+(1-p\_{0,0})e^{-\eta-\lambda\_{\chi}}}{p\_{0,0}+(1-p\_{0,0})e^{-\lambda\_{\chi}}}. |  |

From ([12](https://arxiv.org/html/2602.20771v1#S3.E12 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")), define p~0,0=p0,0/[p0,0+(1−p0,0)​e−λχ]\tilde{p}\_{0,0}=p\_{0,0}/[p\_{0,0}+(1-p\_{0,0})e^{-\lambda\_{\chi}}]. The right-hand side simplifies to p~0,0+(1−p~0,0)​e−η=e−η+p~0,0​(1−e−η)\tilde{p}\_{0,0}+(1-\tilde{p}\_{0,0})e^{-\eta}=e^{-\eta}+\tilde{p}\_{0,0}(1-e^{-\eta}). From ([11](https://arxiv.org/html/2602.20771v1#S3.E11 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) with χt=0\chi\_{t}=0, this equals exp⁡{−η~t}=exp⁡{χt−η~t}\exp\{-\tilde{\eta}\_{t}\}=\exp\{\chi\_{t}-\tilde{\eta}\_{t}\}.

Case χt=−η\chi\_{t}=-\eta: The state χt+1∈{0,−η}\chi\_{t+1}\in\{0,-\eta\} with physical probabilities 1−pη,η1-p\_{\eta,\eta} and pη,ηp\_{\eta,\eta}. By definition, ωt+1=1\omega\_{t+1}=1 when χt+1=−η\chi\_{t+1}=-\eta. Evaluating the conditional expectation:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{χt+1−λχ​ωt+1+ξt​(λχ)}|χt=−η]=eξt​(λχ)​[(1−pη,η)⋅1+pη,η⋅e−η−λχ].\mathbb{E}\left[\exp\{\chi\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}~\Big|~\chi\_{t}=-\eta\right]=e^{\xi\_{t}(\lambda\_{\chi})}\left[(1-p\_{\eta,\eta})\cdot 1+p\_{\eta,\eta}\cdot e^{-\eta-\lambda\_{\chi}}\right]. |  |

The normalizing condition gives eξt​(λχ)=[(1−pη,η)+pη,η​e−λχ]−1e^{\xi\_{t}(\lambda\_{\chi})}=[(1-p\_{\eta,\eta})+p\_{\eta,\eta}e^{-\lambda\_{\chi}}]^{-1}. Substituting:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{χt+1−λχ​ωt+1+ξt​(λχ)}|χt=−η]=(1−pη,η)+pη,η​e−η−λχ(1−pη,η)+pη,η​e−λχ.\mathbb{E}\left[\exp\{\chi\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi})\}~\Big|~\chi\_{t}=-\eta\right]=\frac{(1-p\_{\eta,\eta})+p\_{\eta,\eta}e^{-\eta-\lambda\_{\chi}}}{(1-p\_{\eta,\eta})+p\_{\eta,\eta}e^{-\lambda\_{\chi}}}. |  |

From ([13](https://arxiv.org/html/2602.20771v1#S3.E13 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")), define p~η,η=pη,η​e−λχ/[(1−pη,η)+pη,η​e−λχ]\tilde{p}\_{\eta,\eta}=p\_{\eta,\eta}e^{-\lambda\_{\chi}}/[(1-p\_{\eta,\eta})+p\_{\eta,\eta}e^{-\lambda\_{\chi}}]. The right-hand side simplifies to (1−p~η,η)+p~η,η​e−η=1−p~η,η​(1−e−η)(1-\tilde{p}\_{\eta,\eta})+\tilde{p}\_{\eta,\eta}e^{-\eta}=1-\tilde{p}\_{\eta,\eta}(1-e^{-\eta}). From ([11](https://arxiv.org/html/2602.20771v1#S3.E11 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) with χt=−η\chi\_{t}=-\eta:

|  |  |  |
| --- | --- | --- |
|  | exp⁡{χt−η~t}=e−η⋅[eη−p~η,η​(eη−1)]=1−p~η,η​(1−e−η).\exp\{\chi\_{t}-\tilde{\eta}\_{t}\}=e^{-\eta}\cdot[e^{\eta}-\tilde{p}\_{\eta,\eta}(e^{\eta}-1)]=1-\tilde{p}\_{\eta,\eta}(1-e^{-\eta}). |  |

This confirms ([23](https://arxiv.org/html/2602.20771v1#A1.E23 "In Lemma 2. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")).
∎

###### Proof of Proposition [3](https://arxiv.org/html/2602.20771v1#Thmproposition3 "Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").

Apply the Euler equation ([7](https://arxiv.org/html/2602.20771v1#S3.E7 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) to the stETH return ([3](https://arxiv.org/html/2602.20771v1#S3.E3 "In 3.1.3 Liquid Staking ‣ 3.1 Investment Opportunities ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")):

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Λt,t+1​exp⁡{γts​t​E​T​H+ψts​t​E​T​H+rt,t+1s​t​E​T​H}|ℱt]=1.\mathbb{E}\left[\Lambda\_{t,t+1}\exp\{\gamma^{stETH}\_{t}+\psi^{stETH}\_{t}+r^{stETH}\_{t,t+1}\}~\Big|~\mathcal{F}\_{t}\right]=1. |  |

Substituting ([4](https://arxiv.org/html/2602.20771v1#S3.E4 "In 3.1.3 Liquid Staking ‣ 3.1 Investment Opportunities ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) for rt,t+1s​t​E​T​Hr^{stETH}\_{t,t+1}:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Λt,t+1​exp⁡{γts​t​E​T​H+ψts​t​E​T​H+rt,t+1E​T​H+χt+1−χt}|ℱt]=1.\mathbb{E}\left[\Lambda\_{t,t+1}\exp\{\gamma^{stETH}\_{t}+\psi^{stETH}\_{t}+r^{ETH}\_{t,t+1}+\chi\_{t+1}-\chi\_{t}\}~\Big|~\mathcal{F}\_{t}\right]=1. |  |

The quantities γts​t​E​T​H\gamma^{stETH}\_{t}, ψts​t​E​T​H\psi^{stETH}\_{t}, and χt\chi\_{t} are ℱt\mathcal{F}\_{t}-measurable. Substituting the pricing kernel ([5](https://arxiv.org/html/2602.20771v1#S3.E5 "In 3.2 Asset Pricing Framework ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) and factoring:

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡{−rt,t+1−12​λE​T​H2+γts​t​E​T​H+ψts​t​E​T​H−χt}⋅𝔼​[exp⁡{At+1+Bt+1}|ℱt]=1\exp\left\{-r\_{t,t+1}-\tfrac{1}{2}\lambda\_{ETH}^{2}+\gamma^{stETH}\_{t}+\psi^{stETH}\_{t}-\chi\_{t}\right\}\cdot\mathbb{E}\left[\exp\{A\_{t+1}+B\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]=1 |  | (24) |

where At+1:=rt,t+1E​T​H−λE​T​H​εt+1E​T​HA\_{t+1}:=r^{ETH}\_{t,t+1}-\lambda\_{ETH}\varepsilon^{ETH}\_{t+1} and Bt+1:=χt+1−λχ​ωt+1+ξt​(λχ)B\_{t+1}:=\chi\_{t+1}-\lambda\_{\chi}\omega\_{t+1}+\xi\_{t}(\lambda\_{\chi}).

By independence of εt+1E​T​H\varepsilon^{ETH}\_{t+1} and ωt+1\omega\_{t+1}, and since χt+1\chi\_{t+1} is determined by (χt,ωt+1)(\chi\_{t},\omega\_{t+1}):

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{At+1+Bt+1}|ℱt]=𝔼​[exp⁡{At+1}|ℱt]⋅𝔼​[exp⁡{Bt+1}|ℱt].\mathbb{E}\left[\exp\{A\_{t+1}+B\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]=\mathbb{E}\left[\exp\{A\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]\cdot\mathbb{E}\left[\exp\{B\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]. |  |

For the first factor, substituting rt,t+1E​T​H=μtE​T​H+vtE​T​H​εt+1E​T​Hr^{ETH}\_{t,t+1}=\mu\_{t}^{ETH}+\sqrt{v\_{t}^{ETH}}\,\varepsilon^{ETH}\_{t+1} and applying the moment generating function of εt+1E​T​H|ℱt∼N​(0,1)\varepsilon^{ETH}\_{t+1}|\mathcal{F}\_{t}\sim N(0,1):

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{At+1}|ℱt]=exp⁡{μtE​T​H+12​(vtE​T​H−λE​T​H)2}.\mathbb{E}\left[\exp\{A\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]=\exp\left\{\mu\_{t}^{ETH}+\tfrac{1}{2}(\sqrt{v\_{t}^{ETH}}-\lambda\_{ETH})^{2}\right\}. |  |

For the second factor, Lemma [2](https://arxiv.org/html/2602.20771v1#Thmlemma2 "Lemma 2. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets") gives:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡{Bt+1}|ℱt]=exp⁡{χt−η~t}.\mathbb{E}\left[\exp\{B\_{t+1}\}~\Big|~\mathcal{F}\_{t}\right]=\exp\{\chi\_{t}-\tilde{\eta}\_{t}\}. |  |

Substituting into ([24](https://arxiv.org/html/2602.20771v1#A1.E24 "In Proof of Proposition 3. ‣ Appendix A Proofs ‣ Market Inefficiency in Cryptoasset Markets")), the terms −χt-\chi\_{t} and +χt+\chi\_{t} cancel. Taking logarithms:

|  |  |  |
| --- | --- | --- |
|  | −rt,t+1−12​λE​T​H2+γts​t​E​T​H+ψts​t​E​T​H+μtE​T​H+12​(vtE​T​H−λE​T​H)2−η~t=0.-r\_{t,t+1}-\tfrac{1}{2}\lambda\_{ETH}^{2}+\gamma^{stETH}\_{t}+\psi^{stETH}\_{t}+\mu\_{t}^{ETH}+\tfrac{1}{2}(\sqrt{v\_{t}^{ETH}}-\lambda\_{ETH})^{2}-\tilde{\eta}\_{t}=0. |  |

Solving for μtE​T​H=𝔼​[rt,t+1E​T​H|ℱt]\mu\_{t}^{ETH}=\mathbb{E}[r^{ETH}\_{t,t+1}|\mathcal{F}\_{t}] gives ([10](https://arxiv.org/html/2602.20771v1#S3.E10 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")).
∎

###### Proof of Proposition [4](https://arxiv.org/html/2602.20771v1#Thmproposition4 "Proposition 4 (stETH Lending vs. ETH Staking). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").

Equations ([8](https://arxiv.org/html/2602.20771v1#S3.E8 "In Proposition 1 (ETH Staking). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) and ([10](https://arxiv.org/html/2602.20771v1#S3.E10 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) imply:

|  |  |  |
| --- | --- | --- |
|  | rt,t+1+λE​T​H​vtE​T​H−γtE​T​H+κ−vtE​T​H2=rt,t+1+λE​T​H​vtE​T​H+η~t−γts​t​E​T​H−ψts​t​E​T​H−vtE​T​H2.r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}-\gamma^{ETH}\_{t}+\kappa-\frac{v\_{t}^{ETH}}{2}=r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}+\tilde{\eta}\_{t}-\gamma^{stETH}\_{t}-\psi\_{t}^{stETH}-\frac{v\_{t}^{ETH}}{2}. |  |

which is equivalent to ([14](https://arxiv.org/html/2602.20771v1#S3.E14 "In Proposition 4 (stETH Lending vs. ETH Staking). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")).
∎

###### Proof of Proposition [5](https://arxiv.org/html/2602.20771v1#Thmproposition5 "Proposition 5 (stETH Lending vs. ETH Lending). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets").

Equations ([9](https://arxiv.org/html/2602.20771v1#S3.E9 "In Proposition 2 (ETH Lending). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) and ([10](https://arxiv.org/html/2602.20771v1#S3.E10 "In Proposition 3 (stETH Investment). ‣ 3.3 Equilibrium Restrictions ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")) imply:

|  |  |  |
| --- | --- | --- |
|  | rt,t+1+λE​T​H​vtE​T​H−ψtE​T​H−vtE​T​H2=rt,t+1+λE​T​H​vtE​T​H+η~t−γts​t​E​T​H−ψts​t​E​T​H−vtE​T​H2.r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}-\psi\_{t}^{ETH}-\frac{v\_{t}^{ETH}}{2}=r\_{t,t+1}+\lambda\_{ETH}\sqrt{v\_{t}^{ETH}}+\tilde{\eta}\_{t}-\gamma^{stETH}\_{t}-\psi\_{t}^{stETH}-\frac{v\_{t}^{ETH}}{2}. |  |

which is equivalent to ([15](https://arxiv.org/html/2602.20771v1#S3.E15 "In Proposition 5 (stETH Lending vs. ETH Lending). ‣ 3.4 Implied Equilibrium Relationships ‣ 3 Economic Model ‣ Market Inefficiency in Cryptoasset Markets")).
∎