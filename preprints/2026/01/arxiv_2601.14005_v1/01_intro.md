---
authors:
- Bastien Baude
- Vincent Danos
- Hamza El Khalloufi
doc_id: arxiv:2601.14005v1
family_id: arxiv:2601.14005
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Leveraged positions on decentralized lending platforms
url_abs: http://arxiv.org/abs/2601.14005v1
url_html: https://arxiv.org/html/2601.14005v1
venue: arXiv q-fin
version: 1
year: 2026
---


Bastien Baude
[bastien.baude@centralesupelec.fr](mailto:bastien.baude@centralesupelec.fr)
Université Paris-Saclay, CentraleSupélec, 91192 Gif-sur-Yvette, France

Vincent Danos
[vincent.danos@ens.fr](mailto:vincent.danos@ens.fr)
CNRS, École Normale Supérieure, 45 rue d’Ulm, 75005 Paris, France
School of Informatics, University of Edinburgh, Edinburgh EH8 9AB, UK

Hamza El Khalloufi
[hamza.el-khalloufi@univ-paris1.fr](mailto:hamza.el-khalloufi@univ-paris1.fr)
Université Paris 1 Panthéon-Sorbonne, 12 place du Panthéon, 75005 Paris, France

###### Abstract

We develop a mathematical framework to optimize leveraged staking (“loopy”) strategies in Decentralized Finance (DeFi), in which a staked asset is supplied as collateral, the underlying is borrowed and re-staked, and the loop can be repeated across multiple lending markets. Exploiting the fact that DeFi borrow rates are deterministic functions of pool utilization, we reduce the multi-market problem to a convex allocation over market exposures and obtain closed-form solutions under three interest-rate models: linear, kinked, and adaptive (Morpho’s AdaptiveCurveIRM). The framework incorporates market-specific leverage limits, utilization-dependent borrowing costs, and transaction fees. Backtests on the Ethereum and Base blockchains using the largest Morpho wstETH/WETH markets (Jan. 1–Apr. 1, 2025) show that rebalanced leveraged positions can reach up to 6.2% APY versus 3.1% for unleveraged staking, with strong dependence on position size and rebalancing frequency. Our results provide a mathematical basis for transparent, automated DeFi portfolio optimization.

Keywords – Decentralized finance; leveraged staking; lending protocols; interest rate models; portfolio optimization.

## 1 Introduction

Decentralized finance (DeFi) has emerged as a transformative paradigm in financial markets, offering unprecedented transparency and programmability. Among the various DeFi strategies, leveraged staking, colloquially known as “loopy” staking, has gained significant traction. This strategy involves depositing staked assets (such as wstETH) as collateral in lending protocols, borrowing the underlying asset (such as WETH), re-staking it, and repeating the process to amplify exposure to staking yields. While conceptually straightforward, optimizing such strategies across multiple markets with varying interest rate models, liquidity constraints, and transaction costs presents a complex mathematical challenge.

Unlike traditional finance, DeFi protocols operate with complete transparency: all market states, interest rate models, and transaction histories are publicly available on-chain. This transparency enables rigorous mathematical modeling and optimization that would be impossible in opaque traditional markets. Moreover, DeFi interest rate models are deterministic functions of market utilization, what we term “white-box” models, allowing us to compute the precise relationship between position size and borrowing costs. This stands in contrast to traditional finance where interest rates are often negotiated or determined by opaque internal models.

The primary contribution of this work is to propose a solution to the optimal capital allocation problem across multiple leveraged staking markets. We derive closed-form solutions for three widely-used interest rate models: linear rates, kinked rates (as used by Aave (AAVE, [2020](https://arxiv.org/html/2601.14005v1#bib.bib3 "Aave v1"))), and adaptive rates (Morpho’s AdaptiveCurveIRM (Morpho, [2023](https://arxiv.org/html/2601.14005v1#bib.bib8 "AdaptiveCurveIRM"))). A key methodological insight is that any leveraged position can be decomposed into a maximally-leveraged component and an unleveraged (pure staking) component. This decomposition, combined with the aggregation of unleveraged positions across markets, transforms the original a priori non-convex optimization problem over exposures and leverage ratios into a simpler convex problem over exposures alone, enabling closed-form solutions. Our framework accounts for market-specific constraints including maximum loan-to-value ratios, variable borrowing rates that depend on pool utilization, and transaction costs. We provide efficient algorithms for computing optimal allocations and validate our theoretical results through backtesting on real market data from the Ethereum and Base blockchains.

Our work builds upon recent advances in DeFi. AAVE ([2020](https://arxiv.org/html/2601.14005v1#bib.bib3 "Aave v1")) introduced the kinked interest rate model for decentralized lending, while Morpho ([2023](https://arxiv.org/html/2601.14005v1#bib.bib8 "AdaptiveCurveIRM")) developed adaptive rate mechanisms that respond dynamically to market conditions. Related work on DeFi optimization includes portfolio optimization under automated market makers and optimal liquidity provision strategies. However, to our knowledge, this is the first work to provide closed-form solutions for multi-market leveraged staking optimization with rigorous treatment of transaction costs and complete liquidity assumptions.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2601.14005v1#S2 "2 Related work ‣ Leveraged positions on decentralized lending platforms") reviews related work. Section [3](https://arxiv.org/html/2601.14005v1#S3 "3 Lending positions ‣ Leveraged positions on decentralized lending platforms") introduces some preliminary definitions and notations. Section [4](https://arxiv.org/html/2601.14005v1#S4 "4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms") formulates the optimization problem and derives closed-form solutions for linear, kinked, and adaptive rate models. Section [5](https://arxiv.org/html/2601.14005v1#S5 "5 Dealing with transaction fees ‣ Leveraged positions on decentralized lending platforms") extends the framework to account for transaction costs. Section [6](https://arxiv.org/html/2601.14005v1#S6 "6 Numerical results ‣ Leveraged positions on decentralized lending platforms") presents numerical results from backtesting on the Ethereum and Base blockchains. Section [7](https://arxiv.org/html/2601.14005v1#S7 "7 Discussion and conclusion ‣ Leveraged positions on decentralized lending platforms") concludes with a discussion of limitations and future directions, including game-theoretic considerations when multiple agents employ similar strategies.

## 2 Related work

The mathematical analysis of DeFi lending protocols has attracted growing attention from both the computer science and finance communities. Bartoletti et al. ([2021](https://arxiv.org/html/2601.14005v1#bib.bib12 "SoK: Lending pools in decentralized finance")) provide a systematic overview of lending pools in decentralized finance, introducing a formal model to characterize user interactions, identify vulnerabilities, and analyze potential attacks. Their work establishes foundational abstractions for understanding how lending protocols operate and interact with users.

From an economic perspective, Tovanich et al. ([2023](https://arxiv.org/html/2601.14005v1#bib.bib11 "Contagion in decentralized lending protocols: A case study of Compound")) study the propagation of financial shocks in DeFi lending networks using data from the Compound protocol. By constructing balance sheets of liquidity pools and applying contagion models, they characterize how distress cascades through the interconnected positions of borrowers and lenders. Their findings highlight the systemic risks inherent in highly leveraged DeFi positions.

The design of interest rate models for DeFi lending has been studied by Bertucci et al. ([2025](https://arxiv.org/html/2601.14005v1#bib.bib10 "Agents’ behavior and interest rate model optimization in DeFi lending")), who analyze agents’ behavior on lending platforms and propose a theoretical framework for developing optimal interest rate models. Their work demonstrates that optimal control models with state constraints can generate interest rate policies similar to those used in popular markets, and they show that Morpho’s AdaptiveCurveIRM can be interpreted as a nonlinear PD controller. Our work is complementary: while they focus on the protocol’s perspective of designing interest rate curves, we focus on the user’s perspective of optimizing allocations given existing rate models.

Most closely related to our work, Alexander ([2024](https://arxiv.org/html/2601.14005v1#bib.bib9 "Leveraged restaking of leveraged staking: What are the risks?")) analyze the risks of leveraged staking and restaking strategies. Their empirical analysis documents the prevalence of looping strategies and identifies key risk factors including liquidation cascades and rate volatility. Our work complements their risk analysis by providing an optimization framework that accounts for these factors through the size effect and transaction cost mechanisms.

## 3 Lending positions

In this preliminary section we fix a few notations pertaining to positions on a single lending market ii.
In the next one, we deal with lending positions that span several lending markets.

From the point of view of a borrower, a lending market can be characterized by:

* •

  a maximum loan-to-value, denoted by maxLTVi<1\mathrm{maxLTV}\_{i}<1;
* •

  a liquidity state, with S¯i\bar{S}\_{i} and B¯i\bar{B}\_{i} denoting the total value (using USD as numeraire) supplied to and borrowed from the market (with S¯i≥B¯i\bar{S}\_{i}\geq\bar{B}\_{i});
* •

  an interest rate model mapping the market’s utilization rate U¯i=B¯i/S¯i≤1\bar{U}\_{i}=\bar{B}\_{i}/\bar{S}\_{i}\leq 1 to the instantaneous borrow interest rate bi​(U¯i)b\_{i}(\bar{U}\_{i}).

![Refer to caption](x1.png)


Figure 1: Borrow rate as a function of utilization under the kinked model (illustrative example).

We assume bib\_{i} is continuous, monotonically increasing (higher utilization implies higher borrow rates) and convex. This holds for the interest-rate models considered in this paper: linear and kinked/adaptive models with an increasing slope. Convexity ensures that the (separable) objectives considered below are concave, so Karush-Kuhn-Tucker (KKT) conditions characterize the global optimum and standard one-dimensional root-finders (e.g., Brent’s method) behave well. We do not assume differentiability everywhere: kinked/adaptive models are not differentiable at the kink, and first-order conditions there translate into subgradient inequalities. Figure [1](https://arxiv.org/html/2601.14005v1#S3.F1 "Figure 1 ‣ 3 Lending positions ‣ Leveraged positions on decentralized lending platforms") shows an illustrative example of the kinked interest rate model, emphasizing the non-differentiability at the kink.

Suppose we have taken a position (Ci,Bi)(C\_{i},B\_{i}) on market ii, that is to say we have deposited a value Ci>0C\_{i}>0 of collateral (in USD), and borrowed a value BiB\_{i} (in USD) of the loanable. Our exposure in market ii, or the value of our position, denoted by xix\_{i} (in USD), is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi=Ci−Bi>0x\_{i}=C\_{i}-B\_{i}>0 |  | (1) |

The position is subject to the collateralization constraint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bi/Ci<maxLTViB\_{i}/C\_{i}<\mathrm{maxLTV}\_{i} |  | (2) |

If the price of CiC\_{i} relative to BiB\_{i} decreases, and this condition is violated,
the position is liquidated. Because we work with instantaneous USD values (i.e., everything is marked to market at the time of optimization), liquidation dynamics are outside the scope of this static problem; in practice, maintaining a safety buffer is crucial.

It will be convenient to describe such a position by introducing explicitly its leverage ℓi\ell\_{i} defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓi=Ci/(Ci−Bi)\ell\_{i}=C\_{i}/(C\_{i}-B\_{i}) |  | (3) |

Note that by construction ℓi≥1\ell\_{i}\geq 1. The position (Ci,Bi)(C\_{i},B\_{i}) can now be described as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci=xi​ℓi,Bi=xi​(ℓi−1)C\_{i}=x\_{i}\ell\_{i},\quad B\_{i}=x\_{i}(\ell\_{i}-1) |  | (4) |

If ℓi=1\ell\_{i}=1, we have borrowed nothing and the entire value of the position is the amount deposited as collateral.

The collateralization constraint above fixes the maximum allowed leverage in market ii:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓi≤11−maxLTVi\ell\_{i}\leq\frac{1}{1-\mathrm{maxLTV}\_{i}} |  | (5) |

The position can be decomposed into:

* •

  an unleveraged (staked) sub-position;
* •

  a leveraged sub-position with the maximum leverage ℓimax≤11−maxLTVi\ell^{\text{max}}\_{i}\leq\frac{1}{1-\mathrm{maxLTV}\_{i}} which we allow internally for a position.

Let xi1x^{1}\_{i} be the exposure to the leveraged sub-position with maximum leverage and xi0x^{0}\_{i} the exposure to the unleveraged (staked) sub-position in market ii. Since the overall position is the sum of the two sub-positions, we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci=xi0+xi1​ℓimax,Bi=xi1​(ℓimax−1)C\_{i}=x^{0}\_{i}+x^{1}\_{i}\ell^{\text{max}}\_{i},\quad B\_{i}=x^{1}\_{i}(\ell^{\text{max}}\_{i}-1) |  | (6) |

Solving for xi1x^{1}\_{i} and xi0x^{0}\_{i} in terms of xix\_{i} and ℓi\ell\_{i} yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi1=xi​ℓi−1ℓimax−1,xi0=xi​ℓimax−ℓiℓimax−1x^{1}\_{i}=x\_{i}\frac{\ell\_{i}-1}{\ell^{\text{max}}\_{i}-1},\quad x^{0}\_{i}=x\_{i}\frac{\ell^{\text{max}}\_{i}-\ell\_{i}}{\ell^{\text{max}}\_{i}-1} |  | (7) |

As discussed above, we may choose any internal leverage cap ℓimax≤11−maxLTVi\ell^{\text{max}}\_{i}\leq\frac{1}{1-\mathrm{maxLTV}\_{i}}. In practice we pick ℓimax\ell^{\text{max}}\_{i} with a safety margin below the theoretical maximum to reduce liquidation risk under adverse price moves of the collateral relative to the loan asset. In the numerical examples, we use Lido’s wstETH as collateral. Since wstETH has historically appreciated (almost monotonically) relative to WETH, we set a conservative cap ℓmax=5\ell^{\text{max}}=5, far below the theoretical maximum (typical maxLTV\mathrm{maxLTV} values for these markets are at least 0.9450.945, corresponding to a maximum leverage above 1818). With ℓmax=5\ell^{\text{max}}=5 the collateral-to-debt ratio is C/B=5/4C/B=5/4 in value, which has historically been ample protection against wstETH depegs.

## 4 Optimal capital allocation

Let ξ\xi denote our total budget (in USD). Our objective is to allocate ξ\xi across nn distinct markets to maximize overall cash flow. We assume that the collateral asset is the same across markets, so all collateral earns the same instantaneous staking rate ss (treated as exogenous). The canonical example is wstETH, which accrues a staking yield of approximately 3%3\% for holders.

For each market ii, we set an ℓimax\ell^{\text{max}}\_{i} as explained above. Our decision variables are then the exposure xix\_{i} (in USD) and the leverage multiplier ℓi\ell\_{i}. We seek to determine the optimal pair (xi,ℓi)(x\_{i},\ell\_{i}) for each market ii such that the cash flow is maximized, subject to the total budget constraint and any market-specific restrictions (e.g., maximum leverage constraints). The basic optimization problem is as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (x,ℓ)∗=argmax(x,ℓ)\displaystyle(x,\ell)^{\ast}=\underset{(x,\ell)}{\mathrm{argmax}} | ∑i=1nxi​ℓi​s−∑i=1nxi​(ℓi−1)​b^i​(xi​(ℓi−1))\displaystyle\sum^{n}\_{i=1}x\_{i}\ell\_{i}s-\sum^{n}\_{i=1}x\_{i}(\ell\_{i}-1)\hat{b}\_{i}\big(x\_{i}(\ell\_{i}-1)\big) |  | (8) |
|  | s.t. | ∑i=1nxi=ξ\displaystyle\sum^{n}\_{i=1}x\_{i}=\xi |  |
|  |  | xi≥0,i=1,…,n\displaystyle x\_{i}\geq 0,\quad i=1,\ldots,n |  |
|  |  | xi​(ℓi−1)≤S¯i−B¯i,i=1,…,n\displaystyle x\_{i}(\ell\_{i}-1)\leq\bar{S}\_{i}-\bar{B}\_{i},\quad i=1,\ldots,n |  |
|  |  | 1≤ℓi≤ℓimax,i=1,…,n\displaystyle 1\leq\ell\_{i}\leq\ell^{\text{max}}\_{i},\quad i=1,\ldots,n |  |

with:

|  |  |  |
| --- | --- | --- |
|  | b^i​(x)=bi​((B¯i+x)/S¯i)\hat{b}\_{i}(x)=b\_{i}\big((\bar{B}\_{i}+x)/\bar{S}\_{i}\big) |  |

that is to say b^i​(x)\hat{b}\_{i}(x) is the new borrow rate induced by borrowing xx on top of the amount B¯i\bar{B}\_{i} already borrowed. Henceforth, we will write simply bib\_{i} for b^i\hat{b}\_{i} to keep notations simple.

For completeness, we include the feasibility constraint xi​(ℓi−1)≤S¯i−B¯ix\_{i}(\ell\_{i}-1)\leq\bar{S}\_{i}-\bar{B}\_{i}, which ensures that additional borrowing does not exceed available liquidity. In practice, borrow rates typically explode as utilization approaches full capacity (see Figure [1](https://arxiv.org/html/2601.14005v1#S3.F1 "Figure 1 ‣ 3 Lending positions ‣ Leveraged positions on decentralized lending platforms")), so this constraint rarely binds; henceforth we will often leave it implicit.

In the objective, the first term represents the staking yield accrued on the collateral, while the second term represents the interest paid on the borrowed amount. The optimization problem is non-trivial because borrowing more increases utilization and therefore increases the marginal borrowing rate bib\_{i}.

If we set mi=ℓi−1m\_{i}=\ell\_{i}-1, we see that the objective function can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ​s+∑i=1nmi​xi×(s−bi​(mi​xi)⏟carry)\xi s+\sum^{n}\_{i=1}m\_{i}x\_{i}\times(\underbrace{s-b\_{i}(m\_{i}x\_{i})}\_{\text{carry}}) |  | (9) |

The term ξ​s\xi s corresponds to the yield of the position where we borrow nothing (ℓi=1\ell\_{i}=1, or mi=0m\_{i}=0). The expression s−bi​(mi​xi)s-b\_{i}(m\_{i}x\_{i}) is sometimes called the *carry*. We see that building a looped position on a market is only profitable if the collateral’s staking rate exceeds the rate at which one borrows the loanable, that is if the carry is positive.

Problem ([8](https://arxiv.org/html/2601.14005v1#S4.E8 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) does not seem convex in the first instance. However, using ([7](https://arxiv.org/html/2601.14005v1#S3.E7 "In 3 Lending positions ‣ Leveraged positions on decentralized lending platforms")), we can replace (xi,ℓi)(x\_{i},\ell\_{i}) with (xi0,xi1)(x^{0}\_{i},x^{1}\_{i}) and obtain an equivalent and clearly convex problem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (x1,x0)∗=argmax(x1,x0)\displaystyle(x^{1},x^{0})^{\ast}=\underset{(x^{1},x^{0})}{\mathrm{argmax}} | ∑i=1nxi0​s+∑i=1nxi1​ℓimax​s−∑i=1nxi1​(ℓimax−1)​bi​(xi1​(ℓimax−1))\displaystyle\sum^{n}\_{i=1}x^{0}\_{i}s+\sum^{n}\_{i=1}x^{1}\_{i}\ell^{\text{max}}\_{i}s-\sum^{n}\_{i=1}x^{1}\_{i}(\ell^{\text{max}}\_{i}-1)b\_{i}\big(x^{1}\_{i}(\ell^{\text{max}}\_{i}-1)\big) |  | (10) |
|  | s.t. | ∑i=1nxi1+∑i=1nxi0=ξ\displaystyle\sum^{n}\_{i=1}x^{1}\_{i}+\sum^{n}\_{i=1}x^{0}\_{i}=\xi |  |
|  |  | xi1≥0,i=1,…,n\displaystyle x^{1}\_{i}\geq 0,\quad i=1,\ldots,n |  |
|  |  | xi0≥0,i=1,…,n\displaystyle x^{0}\_{i}\geq 0,\quad i=1,\ldots,n |  |

(See Appendix [A](https://arxiv.org/html/2601.14005v1#A0.SS1 "A Proof of equivalence between (8) and (10) ‣ Appendix ‣ Leveraged positions on decentralized lending platforms") for details about the equivalence between the two problems.)

The reformulated problem ([10](https://arxiv.org/html/2601.14005v1#S4.E10 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) is a convex optimization problem: the constraints are linear, and the nonlinear objective terms are separable and of the form −x​h​(x)-x\,h(x) with hh increasing and convex, hence concave in xx.

Since the problem ([10](https://arxiv.org/html/2601.14005v1#S4.E10 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) depends on the sum of the unleveraged exposures, we define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x0=∑i=1nxi0x\_{0}=\sum^{n}\_{i=1}x^{0}\_{i} |  | (11) |

The aggregation of unleveraged allocations allows us to consider the overall unleveraged exposure as a single decision variable. Consequently, our allocation problem involves distributing the total budget across nn markets at (a conventional) maximum leverage and one aggregated unleveraged position x0x\_{0}. Therefore, the total budget is allocated over n+1n+1 positions with the objective of maximizing cash flow. For notational simplicity, we omit the superscript notation and write xix\_{i} instead of xi1x^{1}\_{i} for i=1,…,ni=1,\ldots,n. The optimization problem ([10](https://arxiv.org/html/2601.14005v1#S4.E10 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) becomes:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x∗=argmax𝑥\displaystyle x^{\ast}=\underset{x}{\mathrm{argmax}} | x0​s+∑i=1nxi​ℓimax​s−∑i=1nxi​(ℓimax−1)​bi​(xi​(ℓimax−1))\displaystyle x\_{0}s+\sum^{n}\_{i=1}x\_{i}\ell^{\text{max}}\_{i}s-\sum^{n}\_{i=1}x\_{i}(\ell^{\text{max}}\_{i}-1)b\_{i}\big(x\_{i}(\ell^{\text{max}}\_{i}-1)\big) |  | (12) |
|  | s.t. | x0+∑i=1nxi=ξ\displaystyle x\_{0}+\sum^{n}\_{i=1}x\_{i}=\xi |  |
|  |  | xi≥0,i=0,…,n\displaystyle x\_{i}\geq 0,\quad i=0,\ldots,n |  |

Thus reformulated, the problem is in the class of convex allocation problems (Patriksson, [2008](https://arxiv.org/html/2601.14005v1#bib.bib2 "A survey on the continuous nonlinear resource allocation problem")). We can solve it using a Lagrange multiplier λ\lambda for the equality constraint x0+∑i=1nxi=ξx\_{0}+\sum^{n}\_{i=1}x\_{i}=\xi:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x∗​(λ)=argmax𝑥\displaystyle x^{\ast}(\lambda)=\underset{x}{\mathrm{argmax}} | x0​(s−λ)+∑i=1nxi​ℓimax​s−∑i=1nxi​(ℓimax−1)​bi​(xi​(ℓimax−1))+λ​(ξ−∑i=1nxi)\displaystyle x\_{0}(s-\lambda)+\sum^{n}\_{i=1}x\_{i}\ell^{\text{max}}\_{i}s-\sum^{n}\_{i=1}x\_{i}(\ell^{\text{max}}\_{i}-1)b\_{i}\big(x\_{i}(\ell^{\text{max}}\_{i}-1)\big)+\lambda\big(\xi-\sum^{n}\_{i=1}x\_{i}\big) |  | (13) |
|  | s.t. | xi≥0,i=0,…,n\displaystyle x\_{i}\geq 0,\quad i=0,\ldots,n |  |

The partial derivative with respect to x0x\_{0} is equal to s−λs-\lambda. Consequently, λ∗=s\lambda^{\ast}=s if x0>0x\_{0}>0. Otherwise, we should have λ∗>s\lambda^{\ast}>s. We now examine these two cases separately.

#### Unsaturated markets with fully leveraged positions (λ∗>s\lambda^{\ast}>s)

In this regime, the total budget is not sufficient to saturate111meaning, had we more budget it would be advantageous to borrow more all markets, so the unleveraged allocation vanishes (x0∗=0x^{\ast}\_{0}=0). Moreover, for each market ii, the optimal allocation xi∗x^{\ast}\_{i} is given by the First Order Condition (FOC) obtained from differentiating the objective function in ([13](https://arxiv.org/html/2601.14005v1#S4.E13 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) with respect to xix\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓimax​s−(ℓimax−1)​(bi​(xi∗​(ℓimax−1))+xi∗​(ℓimax−1)​bi′​(xi∗​(ℓimax−1)))=λ\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\big(b\_{i}\big(x^{\ast}\_{i}(\ell^{\text{max}}\_{i}-1)\big)+x^{\ast}\_{i}(\ell^{\text{max}}\_{i}-1)b^{\prime}\_{i}(x^{\ast}\_{i}(\ell^{\text{max}}\_{i}-1))\big)=\lambda |  | (14) |

And the optimal Lagrange multiplier λ∗\lambda^{\ast} is the unique solution to the budget constraint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nxi∗​(λ∗)=ξ\sum^{n}\_{i=1}x^{\ast}\_{i}(\lambda^{\ast})=\xi |  | (15) |

#### Saturated markets with strictly positive unleveraged position (λ∗=s\lambda^{\ast}=s)

For each market ii, we determine the optimal allocation xi∗x^{\ast}\_{i} by differentiating the objective function in ([13](https://arxiv.org/html/2601.14005v1#S4.E13 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) with respect to xix\_{i} and imposing the FOC:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​(xi∗​(ℓimax−1))+xi∗​(ℓimax−1)​bi′​(xi∗​(ℓimax−1))=sb\_{i}\big(x^{\ast}\_{i}(\ell^{\text{max}}\_{i}-1)\big)+x^{\ast}\_{i}(\ell^{\text{max}}\_{i}-1)b^{\prime}\_{i}\big(x^{\ast}\_{i}(\ell^{\text{max}}\_{i}-1)\big)=s |  | (16) |

The unleveraged exposure x0∗x^{\ast}\_{0} follows from the budget constraint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x0∗=ξ−∑i=1nxi∗x^{\ast}\_{0}=\xi-\sum^{n}\_{i=1}x^{\ast}\_{i} |  | (17) |

In this regime, all markets are saturated, and the residual budget is allocated to the unleveraged position.

Since ([16](https://arxiv.org/html/2601.14005v1#S4.E16 "In Saturated markets with strictly positive unleveraged position (𝜆^∗=𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) is recovered from ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) with λ=s\lambda=s, henceforth we focus exclusively on ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")).

Above we have used bi′b^{\prime}\_{i} as if the rate function was everywhere differentiable. Let Bi=(ℓimax−1)​xiB\_{i}=(\ell^{\text{max}}\_{i}-1)x\_{i} (the amount we borrow) and define gi​(Bi)=Bi​bi​(Bi)g\_{i}(B\_{i})=B\_{i}\,b\_{i}(B\_{i}). When bib\_{i} is kinked, gig\_{i} may not be differentiable at Bikink=S¯i​u∗−B¯iB\_{i}^{\mathrm{kink}}=\bar{S}\_{i}u^{\ast}-\bar{B}\_{i}.
The KKT condition is now a subgradient one:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∈ℓimax​s−(ℓimax−1)​∂gi​(Bi)\lambda\in\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\,\partial g\_{i}(B\_{i}) |  | (18) |

so if λ\lambda lies between the left and right marginal costs at BikinkB\_{i}^{\mathrm{kink}}, the maximizer is attained at the kink boundary Bi=BikinkB\_{i}=B\_{i}^{\mathrm{kink}}, i.e. xi=Bikink/(ℓimax−1)x\_{i}=B\_{i}^{\mathrm{kink}}/(\ell^{\text{max}}\_{i}-1). This will show clearly in our solution of the kinked rate model below (see Section [4.4](https://arxiv.org/html/2601.14005v1#S4.SS4 "4.4 Kinked rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")).

### 4.1 Algorithm

First, we compute the optimal allocations from ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) with λ=s\lambda=s, denoted by x∗,(0)x^{\ast,(0)}. If the budget constraint holds, that is to say if ∑i=1nxi∗,(0)≤ξ\sum^{n}\_{i=1}x^{\ast,(0)}\_{i}\leq\xi, the solution is valid, and the unleveraged allocation follows from: x0∗,(0)=ξ−∑i=1nxi∗,(0)x^{\ast,(0)}\_{0}=\xi-\sum^{n}\_{i=1}x^{\ast,(0)}\_{i}.

Else, we compute the optimal allocations from ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")), denoted by x∗,(1)​(λ)x^{\ast,(1)}(\lambda) given λ\lambda, for which x0∗,(1)=0x^{\ast,(1)}\_{0}=0. The optimal Lagrange multiplier λ∗\lambda^{\ast} is determined from the budget constraint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nxi∗,(1)​(λ∗)=ξ\sum^{n}\_{i=1}x^{\ast,(1)}\_{i}(\lambda^{\ast})=\xi |  | (19) |

Closed-form solutions may exist depending on the interest rate model; otherwise, λ∗\lambda^{\ast} is determined numerically, e.g., using Brent’s algorithm.

### 4.2 Interpreting λ∗\lambda^{\ast}

One can think of λ∗\lambda^{\ast}, the optimal Lagrange multiplier, as a way to make the leveraged strategy artificially and gradually less profitable, up until the point where all markets become saturated under the budget constraint. Suppose that the same maximum allowed leverage ℓmax\ell^{\text{max}} is applied to all markets. Then, ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) becomes equivalent to ([16](https://arxiv.org/html/2601.14005v1#S4.E16 "In Saturated markets with strictly positive unleveraged position (𝜆^∗=𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) using a modified staking rate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sa​(λ)=s+s−λℓmax−1s^{a}(\lambda)=s+\frac{s-\lambda}{\ell^{\text{max}}-1} |  | (20) |

Since λ∗≥s\lambda^{\ast}\geq s, it follows that sa​(λ∗)≤ss^{a}(\lambda^{\ast})\leq s. To find λ∗\lambda^{\ast}, the algorithm starts from λ=s\lambda=s and increases it, which is equivalent to decreasing sas^{a}, until the budget constraint is satisfied. Once it is found, the optimal strategy derived from ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) (unsaturated markets) is equivalent to the one obtained from ([16](https://arxiv.org/html/2601.14005v1#S4.E16 "In Saturated markets with strictly positive unleveraged position (𝜆^∗=𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) (all markets saturated) under the artificial staking rate sa​(λ∗)s^{a}(\lambda^{\ast}) instead of the original ss.

A similar interpretation applies on the borrow side. Increasing the Lagrange multiplier can be seen as introducing artificial (and higher) borrowing rates, which are gradually raised until all markets are saturated. This interpretation, unlike its counterpart on the staking side, holds even when markets have different leverage limits.

### 4.3 Linear rate

Using the notations introduced in AAVE ([2020](https://arxiv.org/html/2601.14005v1#bib.bib3 "Aave v1")), the linear model reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​(Bi)=rb​a​s​e+B¯i+BiS¯i​u∗​rs​l​o​p​e​1b\_{i}(B\_{i})=r\_{base}+\frac{\bar{B}\_{i}+B\_{i}}{\bar{S}\_{i}u^{\*}}r\_{slope1} |  | (21) |

where u∗∈(0,1)u^{\*}\in(0,1) is called the target utilization,
rb​a​s​e≥0r\_{base}\geq 0 and rs​l​o​p​e​1≥0r\_{slope1}\geq 0. At target utilization, the borrow rate is rb​a​s​e+rs​l​o​p​e​1r\_{base}+r\_{slope1}.

With a linear rate model, our problem becomes a so-called “water-filling” problem (Boyd and Vandenberghe, [2004](https://arxiv.org/html/2601.14005v1#bib.bib1 "Convex optimization"), Example 5.2). We now state its general closed-form solution.

###### Proposition 1 (Linear rate)

Under the linear rate model ([21](https://arxiv.org/html/2601.14005v1#S4.E21 "In 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")), the optimal solution to ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi∗​(λ)=αi​[βi−λ]+x^{\*}\_{i}(\lambda)=\alpha\_{i}\big[\beta\_{i}-\lambda\big]^{+} |  | (22) |

where,

|  |  |  |  |
| --- | --- | --- | --- |
|  | αi=S¯i​u∗2​rs​l​o​p​e​1​(ℓimax−1)2,βi=ℓimax​s−(ℓimax−1)​(rb​a​s​e+B¯iS¯i​u∗​rs​l​o​p​e​1)\alpha\_{i}=\frac{\bar{S}\_{i}u^{\*}}{2r\_{slope1}(\ell^{\text{max}}\_{i}-1)^{2}},\quad\beta\_{i}=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\big(r\_{base}+\frac{\bar{B}\_{i}}{\bar{S}\_{i}u^{\*}}r\_{slope1}\big) |  | (23) |

for i=1,…,ni=1,\ldots,n and the optimal Lagrange multiplier reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗=∑j=1kαj​βj−ξ∑j=1kαj\lambda^{\*}=\frac{\sum^{k}\_{j=1}\alpha\_{j}\beta\_{j}-\xi}{\sum^{k}\_{j=1}\alpha\_{j}} |  | (24) |

Without loss of generality, we assume that the markets are ordered such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β1≥β2≥⋯≥βn\beta\_{1}\geq\beta\_{2}\geq\cdots\geq\beta\_{n} |  | (25) |

and the index k∈{1,…,n}k\in\{1,\ldots,n\} is determined by the conditions (with by convention φn+1=+∞\varphi\_{n+1}=+\infty):

|  |  |  |  |
| --- | --- | --- | --- |
|  | φk<ξ≤φk+1\varphi\_{k}<\xi\leq\varphi\_{k+1} |  | (26) |

where,

|  |  |  |  |
| --- | --- | --- | --- |
|  | φk=∑j=1kαj​[βj−βk]\varphi\_{k}=\sum^{k}\_{j=1}\alpha\_{j}\big[\beta\_{j}-\beta\_{k}\big] |  | (27) |

The proof is provided in Appendix [B](https://arxiv.org/html/2601.14005v1#A0.SS2 "B Proof of Proposition 1 ‣ Appendix ‣ Leveraged positions on decentralized lending platforms").

### 4.4 Kinked rate

The kinked model reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​(Bi)={rb​a​s​e+B¯i+BiS¯i​u∗​rs​l​o​p​e​1if ​B¯i+Bi<S¯i​u∗rb​a​s​e+rs​l​o​p​e​1+B¯i+Bi−S¯i​u∗S¯i​(1−u∗)​rs​l​o​p​e​2if ​B¯i+Bi≥S¯i​u∗b\_{i}(B\_{i})=\left\{\begin{array}[]{ll}\displaystyle r\_{base}+\frac{\bar{B}\_{i}+B\_{i}}{\bar{S}\_{i}u^{\*}}r\_{slope1}&\mbox{if }\bar{B}\_{i}+B\_{i}<\bar{S}\_{i}u^{\*}\\ \displaystyle r\_{base}+r\_{slope1}+\frac{\bar{B}\_{i}+B\_{i}-\bar{S}\_{i}u^{\*}}{\bar{S}\_{i}(1-u^{\*})}r\_{slope2}&\mbox{if }\bar{B}\_{i}+B\_{i}\geq\bar{S}\_{i}u^{\*}\end{array}\right. |  | (28) |

where u∗∈(0,1)u^{\*}\in(0,1), rb​a​s​e≥0r\_{base}\geq 0, rs​l​o​p​e​1≥0r\_{slope1}\geq 0 and rs​l​o​p​e​2≥0r\_{slope2}\geq 0. Again, we use the notation of AAVE ([2020](https://arxiv.org/html/2601.14005v1#bib.bib3 "Aave v1")). The parameter rs​l​o​p​e​1r\_{slope1} is normalized such that the rate at target utilization u∗u^{\*} equals rb​a​s​e+rs​l​o​p​e​1r\_{base}+r\_{slope1}, while rs​l​o​p​e​2r\_{slope2} is normalized so that the rate at full utilization equals rb​a​s​e+rs​l​o​p​e​1+rs​l​o​p​e​2r\_{base}+r\_{slope1}+r\_{slope2}.

We now state the general closed-form solution under kinked interest rate models.

###### Proposition 2 (Kinked rate)

Under the kinked rate model ([28](https://arxiv.org/html/2601.14005v1#S4.E28 "In 4.4 Kinked rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) and assuming rs​l​o​p​e​1<u∗1−u∗​rs​l​o​p​e​2r\_{slope1}<\frac{u^{\*}}{1-u^{\*}}r\_{slope2}, if S¯i​u∗−B¯i>0\bar{S}\_{i}u^{\*}-\bar{B}\_{i}>0, i.e., when the current utilization is below the target rate, the optimal solution to ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi∗​(λ)={αi2​[βi2−λ]+if ​λ<λi2S¯i​u∗−B¯iℓimax−1if ​λi2≤λ≤λi1αi1​[βi1−λ]+if ​λi1<λx^{\*}\_{i}(\lambda)=\left\{\begin{array}[]{ll}\displaystyle\alpha^{2}\_{i}\big[\beta^{2}\_{i}-\lambda\big]^{+}&\mbox{if }\lambda<\lambda^{2}\_{i}\\ \displaystyle\frac{\bar{S}\_{i}u^{\*}-\bar{B}\_{i}}{\ell^{\text{max}}\_{i}-1}&\mbox{if }\lambda^{2}\_{i}\leq\lambda\leq\lambda^{1}\_{i}\\ \displaystyle\alpha^{1}\_{i}\big[\beta^{1}\_{i}-\lambda\big]^{+}&\mbox{if }\lambda^{1}\_{i}<\lambda\end{array}\right. |  | (29) |

where,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | αi1\displaystyle\alpha^{1}\_{i} | =S¯i​u∗2​rs​l​o​p​e​1​(ℓimax−1)2,βi1=ℓimax​s−(ℓimax−1)​(rb​a​s​e+B¯iS¯i​u∗​rs​l​o​p​e​1)\displaystyle=\frac{\bar{S}\_{i}u^{\*}}{2r\_{slope1}(\ell^{\text{max}}\_{i}-1)^{2}},\quad\beta^{1}\_{i}=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\big(r\_{base}+\frac{\bar{B}\_{i}}{\bar{S}\_{i}u^{\*}}r\_{slope1}\big) |  | (30) |
|  | αi2\displaystyle\alpha^{2}\_{i} | =S¯i​(1−u∗)2​rs​l​o​p​e​2​(ℓimax−1)2,βi2=ℓimax​s−(ℓimax−1)​(rb​a​s​e+rs​l​o​p​e​1+B¯i−S¯i​u∗S¯i​(1−u∗)​rs​l​o​p​e​2)\displaystyle=\frac{\bar{S}\_{i}(1-u^{\*})}{2r\_{slope2}(\ell^{\text{max}}\_{i}-1)^{2}},\quad\beta^{2}\_{i}=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\big(r\_{base}+r\_{slope1}+\frac{\bar{B}\_{i}-\bar{S}\_{i}u^{\*}}{\bar{S}\_{i}(1-u^{\*})}r\_{slope2}\big) |  |

and,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λi1\displaystyle\lambda^{1}\_{i} | =ℓimax​s−(ℓimax−1)​(rb​a​s​e+rs​l​o​p​e​1+(S¯i​u∗−B¯i)​rs​l​o​p​e​1S¯i​u∗)\displaystyle=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\big(r\_{base}+r\_{slope1}+(\bar{S}\_{i}u^{\*}-\bar{B}\_{i})\frac{r\_{slope1}}{\bar{S}\_{i}u^{\*}}\big) |  | (31) |
|  | λi2\displaystyle\lambda^{2}\_{i} | =ℓimax​s−(ℓimax−1)​(rb​a​s​e+rs​l​o​p​e​1+(S¯i​u∗−B¯i)​rs​l​o​p​e​2S¯i​(1−u∗))\displaystyle=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\big(r\_{base}+r\_{slope1}+(\bar{S}\_{i}u^{\*}-\bar{B}\_{i})\frac{r\_{slope2}}{\bar{S}\_{i}(1-u^{\*})}\big) |  |

Otherwise, if S¯i​u∗−B¯i<0\bar{S}\_{i}u^{\*}-\bar{B}\_{i}<0, i.e., when the current utilization exceeds the target rate, the optimal solution reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi∗​(λ)=αi2​[βi2−λ]+x^{\*}\_{i}(\lambda)=\alpha^{2}\_{i}\big[\beta^{2}\_{i}-\lambda\big]^{+} |  | (32) |

The proof is provided in Appendix [C](https://arxiv.org/html/2601.14005v1#A0.SS3 "C Proof of Proposition 2 ‣ Appendix ‣ Leveraged positions on decentralized lending platforms").

### 4.5 Adaptive rate

In contrast to the linear and kinked rate models, which depend solely on the current utilization rate, the Morpho interest rate model (Morpho, [2023](https://arxiv.org/html/2601.14005v1#bib.bib8 "AdaptiveCurveIRM")), called AdaptiveCurveIRM (abbreviated as adaptive rate) also depends on the previous state of the liquidity pool. Specifically, the model is given by r​(u,t)=rttarget​curve​(u)r(u,t)=r^{\text{target}}\_{t}\text{curve}(u) where,

|  |  |  |  |
| --- | --- | --- | --- |
|  | rttarget=rtl​a​s​ttarget​speed​(t),speed​(t)=ekp​error​(utl​a​s​t)​(t−tl​a​s​t),error​(u)={u−u∗u∗if ​u<u∗u−u∗1−u∗if ​u≥u∗r^{\text{target}}\_{t}=r^{\text{target}}\_{t\_{last}}\text{speed}(t),\quad\text{speed}(t)=e^{k\_{p}\text{error}(u\_{t\_{last}})(t-t\_{last})},\quad\text{error}(u)=\left\{\begin{array}[]{ll}\frac{u-u^{\*}}{u^{\*}}&\mbox{if }u<u^{\*}\\ \frac{u-u^{\*}}{1-u^{\*}}&\mbox{if }u\geq u^{\*}\end{array}\right. |  | (33) |

where kp>0k\_{p}>0. The time tl​a​s​tt\_{last} corresponds to the last interaction with the pool (deposit, withdrawal, borrow, or repay) and utl​a​s​tu\_{t\_{last}} denotes the associated utilization rate. In addition, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | curve​(u)={(1−1kd)​error​(u)+1if ​u<u∗(kd−1)​error​(u)+1if ​u≥u∗\text{curve}(u)=\left\{\begin{array}[]{ll}\big(1-\frac{1}{k\_{d}}\big)\text{error}(u)+1&\mbox{if }u<u^{\*}\\ \big(k\_{d}-1\big)\text{error}(u)+1&\mbox{if }u\geq u^{\*}\end{array}\right. |  | (34) |

where u∗∈(0,1)u^{\*}\in(0,1) and kd>1k\_{d}>1.

The adaptive rate model can be reformulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​(Bi)={rttarget​[1+(1−1kd)​B¯i+Bi−S¯i​u∗S¯i​u∗]if ​B¯i+Bi<S¯i​u∗rttarget​[1+(kd−1)​B¯i+Bi−S¯i​u∗S¯i​(1−u∗)]if ​B¯i+Bi≥S¯i​u∗b\_{i}(B\_{i})=\left\{\begin{array}[]{ll}\displaystyle r^{\text{target}}\_{t}\big[1+\big(1-\frac{1}{k\_{d}}\big)\frac{\bar{B}\_{i}+B\_{i}-\bar{S}\_{i}u^{\*}}{\bar{S}\_{i}u^{\*}}\big]&\mbox{if }\bar{B}\_{i}+B\_{i}<\bar{S}\_{i}u^{\*}\\ \displaystyle r^{\text{target}}\_{t}\big[1+\big(k\_{d}-1\big)\frac{\bar{B}\_{i}+B\_{i}-\bar{S}\_{i}u^{\*}}{\bar{S}\_{i}(1-u^{\*})}\big]&\mbox{if }\bar{B}\_{i}+B\_{i}\geq\bar{S}\_{i}u^{\*}\end{array}\right. |  | (35) |

By omitting the dynamic feature of the adaptive rate—which is justified in our case since the optimization problem is static in time—the adaptive model is a reparametrization of the kinked model. Nonetheless, we still provide the general closed-form solution under adaptive interest rate models, as we believe it may be useful for practitioners.

###### Corollary 1 (Adaptive rate)

Under the adaptive rate model ([35](https://arxiv.org/html/2601.14005v1#S4.E35 "In 4.5 Adaptive rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) and assuming 1−u∗u∗<kd\frac{1-u^{\*}}{u^{\*}}<k\_{d}, if S¯i​u∗−B¯i>0\bar{S}\_{i}u^{\*}-\bar{B}\_{i}>0, i.e., when the current utilization is below the target rate, the optimal solution to ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi∗​(λ)={αi2​[βi2−λ]+if ​λ<λi2S¯i​u∗−B¯iℓimax−1if ​λi2≤λ≤λi1αi1​[βi1−λ]+if ​λi1<λx^{\*}\_{i}(\lambda)=\left\{\begin{array}[]{ll}\displaystyle\alpha^{2}\_{i}\big[\beta^{2}\_{i}-\lambda\big]^{+}&\mbox{if }\lambda<\lambda^{2}\_{i}\\ \displaystyle\frac{\bar{S}\_{i}u^{\*}-\bar{B}\_{i}}{\ell^{\text{max}}\_{i}-1}&\mbox{if }\lambda^{2}\_{i}\leq\lambda\leq\lambda^{1}\_{i}\\ \displaystyle\alpha^{1}\_{i}\big[\beta^{1}\_{i}-\lambda\big]^{+}&\mbox{if }\lambda^{1}\_{i}<\lambda\end{array}\right. |  | (36) |

where,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | αi1\displaystyle\alpha^{1}\_{i} | =S¯i​u∗2​rttarget​(1−1kd)​(ℓimax−1)2,βi1=ℓimax​s−(ℓimax−1)​rttarget​(1kd+B¯iS¯i​u∗​(1−1kd))\displaystyle=\frac{\bar{S}\_{i}u^{\*}}{2r^{\text{target}}\_{t}(1-\frac{1}{k\_{d}})(\ell^{\text{max}}\_{i}-1)^{2}},\quad\beta^{1}\_{i}=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)r^{\text{target}}\_{t}\big(\frac{1}{k\_{d}}+\frac{\bar{B}\_{i}}{\bar{S}\_{i}u^{\*}}(1-\frac{1}{k\_{d}})\big) |  | (37) |
|  | αi2\displaystyle\alpha^{2}\_{i} | =S¯i​(1−u∗)2​rttarget​(kd−1)​(ℓimax−1)2,βi2=ℓimax​s−(ℓimax−1)​rttarget​(1+B¯i−S¯i​u∗S¯i​(1−u∗)​(kd−1))\displaystyle=\frac{\bar{S}\_{i}(1-u^{\*})}{2r^{\text{target}}\_{t}(k\_{d}-1)(\ell^{\text{max}}\_{i}-1)^{2}},\quad\beta^{2}\_{i}=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)r^{\text{target}}\_{t}\big(1+\frac{\bar{B}\_{i}-\bar{S}\_{i}u^{\*}}{\bar{S}\_{i}(1-u^{\*})}(k\_{d}-1)\big) |  |

and,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λi1\displaystyle\lambda^{1}\_{i} | =ℓimax​s−(ℓimax−1)​rttarget​(1+(S¯i​u∗−B¯i)​(1−1kd)S¯i​u∗)\displaystyle=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)r^{\text{target}}\_{t}\big(1+(\bar{S}\_{i}u^{\*}-\bar{B}\_{i})\frac{(1-\frac{1}{k\_{d}})}{\bar{S}\_{i}u^{\*}}\big) |  | (38) |
|  | λi2\displaystyle\lambda^{2}\_{i} | =ℓimax​s−(ℓimax−1)​rttarget​(1+(S¯i​u∗−B¯i)​(kd−1)S¯i​(1−u∗))\displaystyle=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)r^{\text{target}}\_{t}\big(1+(\bar{S}\_{i}u^{\*}-\bar{B}\_{i})\frac{(k\_{d}-1)}{\bar{S}\_{i}(1-u^{\*})}\big) |  |

Otherwise, if S¯i​u∗−B¯i<0\bar{S}\_{i}u^{\*}-\bar{B}\_{i}<0, i.e., when the current utilization exceeds the target rate, the optimal solution reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi∗​(λ)=αi2​[βi2−λ]+x^{\*}\_{i}(\lambda)=\alpha^{2}\_{i}\big[\beta^{2}\_{i}-\lambda\big]^{+} |  | (39) |

The proof is provided in Appendix [D](https://arxiv.org/html/2601.14005v1#A0.SS4 "D Proof of Corollary 1 ‣ Appendix ‣ Leveraged positions on decentralized lending platforms"). In practice, the values u∗=0.9u^{\*}=0.9 and kd=4k\_{d}=4 are hardcoded into the smart contract, and they satisfy the condition 1−u∗u∗<kd\frac{1-u^{\*}}{u^{\*}}<k\_{d}.

## 5 Dealing with transaction fees

### 5.1 General approach

Suppose we already hold a position x¯\bar{x}, and we wish to move to a new position xx. Because of the cost of moving capital around, it may not be profitable to move even if xx has a higher yield. Let us write c​(x,x¯)c(x,\bar{x}) for the cost of rebalancing the portfolio from the current one to xx. Let TT be our investment horizon, that is to say the typical duration we expect to hold a position.

Our basic optimization problem ([12](https://arxiv.org/html/2601.14005v1#S4.E12 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) can be modified to account for transaction fees:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x∗=argmax𝑥\displaystyle x^{\ast}=\underset{x}{\mathrm{argmax}} | {−1Tc(x,x¯)+(x0−x¯0+∑i=1n(xi−x¯i)ℓimax)s\displaystyle\left\{-\frac{1}{T}c(x,\bar{x})+\left(x\_{0}-\bar{x}\_{0}+\sum^{n}\_{i=1}(x\_{i}-\bar{x}\_{i})\ell^{\text{max}}\_{i}\right)s\right. |  | (40) |
|  |  | −∑i=1n(ℓimax−1)[xibi(xi(ℓimax−1))−x¯ibi(x¯i(ℓimax−1))]}\displaystyle\left.-\sum^{n}\_{i=1}(\ell^{\text{max}}\_{i}-1)\Big[x\_{i}b\_{i}\big(x\_{i}(\ell^{\text{max}}\_{i}-1)\big)-\bar{x}\_{i}b\_{i}\big(\bar{x}\_{i}(\ell^{\text{max}}\_{i}-1)\big)\Big]\right\} |  |
|  | s.t. | x0+∑i=1nxi=ξ\displaystyle x\_{0}+\sum^{n}\_{i=1}x\_{i}=\xi |  |
|  |  | xi≥0,i=0,…,n\displaystyle x\_{i}\geq 0,\quad i=0,\ldots,n |  |

In words, we seek the position xx that best trades-off expected yield improvements against rebalancing costs. This trade-off depends on the choice of TT. The shorter TT is, the smaller the optimal rebalancing will be. In addition, TT should be small, as compounding effects are neglected in ([40](https://arxiv.org/html/2601.14005v1#S5.E40 "In 5.1 General approach ‣ 5 Dealing with transaction fees ‣ Leveraged positions on decentralized lending platforms")). (In practice, a natural choice for TT is the time it takes for the disparity of borrow rates to dissipate.)

We choose to model transaction fees as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(x,x¯)=γ​(x,x¯)​|x0−x¯0+∑i=1n(xi−x¯i)​ℓimax|c(x,\bar{x})=\gamma(x,\bar{x})\,\Big|x\_{0}-\bar{x}\_{0}+\sum^{n}\_{i=1}(x\_{i}-\bar{x}\_{i})\ell^{\text{max}}\_{i}\Big| |  | (41) |

and,

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(x,x¯)={γ+if ​x¯0+∑i=1nx¯i​ℓimax<x0+∑i=1nxi​ℓimaxγ−if ​x¯0+∑i=1nx¯i​ℓimax≥x0+∑i=1nxi​ℓimax\gamma(x,\bar{x})=\left\{\begin{array}[]{ll}\displaystyle\gamma^{+}&\mbox{if }\bar{x}\_{0}+\sum^{n}\_{i=1}\bar{x}\_{i}\ell^{\text{max}}\_{i}<x\_{0}+\sum^{n}\_{i=1}x\_{i}\ell^{\text{max}}\_{i}\\ \displaystyle\gamma^{-}&\mbox{if }\bar{x}\_{0}+\sum^{n}\_{i=1}\bar{x}\_{i}\ell^{\text{max}}\_{i}\geq x\_{0}+\sum^{n}\_{i=1}x\_{i}\ell^{\text{max}}\_{i}\end{array}\right. |  | (42) |

Note that our simple notion of cost only depends on the change in total collateral amount; moving collateral across markets is assumed to be free, which isn’t true operationally, because of so-called (zero-order) “gas costs”. We distinguish between the cases where the total collateral increases or decreases. In the former case we use γ+\gamma^{+}; in the latter we use γ−\gamma^{-}.

To see why the distinction is worth making in practice we can take the example of Lido’s wstETH as collateral. To acquire it starting from WETH, one can convert WETH directly without fees. Not so in the other direction where Lido redemption protocol forces a variable delay and selling wstETH for WETH can be done at a small discount on exit markets. Thus in this case there is a strong asymmetry between the two directions as γ+=0\gamma^{+}=0, while γ−>0\gamma^{-}>0 is typically of the order of a couple of basis points (bps).

Our transaction fee model is proportional to the change in total collateral, with constant rates γ+\gamma^{+} and γ−\gamma^{-}. This formulation implicitly neglects slippage on exit markets. To account for linear slippage—the simplest extension—rates γ+\gamma^{+} and γ−\gamma^{-} should be linear in the change in total collateral. However, this leads to a non-separable objective function, which precludes closed-form solutions.

### 5.2 Algorithm

To solve the problem, we first assume that the total amount of collateral increases. That is to say: x¯0+∑i=1nx¯i​ℓimax<x0+∑i=1nxi​ℓimax\bar{x}\_{0}+\sum^{n}\_{i=1}\bar{x}\_{i}\ell^{\text{max}}\_{i}<x\_{0}+\sum^{n}\_{i=1}x\_{i}\ell^{\text{max}}\_{i}. This means that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​c​(x,x¯)=γ+T​(x0−x¯0+∑i=1n(xi−x¯i)​ℓimax)\frac{1}{T}\,c(x,\bar{x})=\frac{\gamma^{+}}{T}\left(x\_{0}-\bar{x}\_{0}+\sum^{n}\_{i=1}(x\_{i}-\bar{x}\_{i})\ell^{\text{max}}\_{i}\right) |  | (43) |

Hence, we are back in the case of Section [4](https://arxiv.org/html/2601.14005v1#S4 "4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms"), except that we use an effective staking rate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s+=s−γ+Ts^{+}=s-\frac{\gamma^{+}}{T} |  | (44) |

If the resulting allocation satisfies the initial inequality, the solution is valid. Else, we compute the optimal allocation with s−=s+γ−Ts^{-}=s+\frac{\gamma^{-}}{T}. If neither solution is valid, then the optimal allocation is x¯\bar{x}, i.e., we should not change our position.

## 6 Numerical results

### 6.1 Data processing

| market | ID | creation date | LLTV (%\%) |
| --- | --- | --- | --- |
| 1 | 6becf9b4-3c85-40bf-9938-196812e034a3 | March 14, 2024 | 96.596.5 |
| 2 | 928c009a-d217-42f7-9d3a-45bb6c8d71f9 | March 25, 2024 | 94.594.5 |

Table 1: IDs, creation dates and LLTVs of the two largest wstETH/WETH markets on Morpho on the Ethereum blockchain.

We backtest the “loopy” strategy on real market data from the Ethereum blockchain. We first describe the dataset and preprocessing steps before turning to the results. We focus on the largest Morpho markets for the wstETH/WETH pair over the period from January 1, 2025, to April 1, 2025. The data is retrieved from Morpho’s GraphQL service.222<https://api.morpho.org/graphql> We select the two largest markets in terms of supplied assets; their characteristics are summarized in Table [1](https://arxiv.org/html/2601.14005v1#S6.T1 "Table 1 ‣ 6.1 Data processing ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms"). The third-largest market is negligible in comparison and therefore excluded from the analysis. Figure [2](https://arxiv.org/html/2601.14005v1#S6.F2 "Figure 2 ‣ 6.1 Data processing ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") shows the evolution of supplied and borrowed WETH in the selected markets. At the beginning of the period, both markets had comparable levels of supplied assets. However, the second market declined substantially over time, and by April 1, 2025, the first market had become nearly 2020 times larger. This difference is likely due to the higher maximum LTV in the first market, which allows for greater leverage capacity (see Table [1](https://arxiv.org/html/2601.14005v1#S6.T1 "Table 1 ‣ 6.1 Data processing ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms")).

![Refer to caption](x2.png)


Figure 2: Evolution of WETH reserves (solid line: supplied funds; dashed line: borrowed fund) for the two largest wstETH/WETH markets on Morpho on the Ethereum blockchain from January 1, 2025 to April 1, 2025.

Figure [3](https://arxiv.org/html/2601.14005v1#S6.F3 "Figure 3 ‣ 6.1 Data processing ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") shows the evolution of the borrowing rate and the rate at target for both markets on an hourly basis, compared to the Lido staking rate over the same period. The staking rate data is retrieved via Lido’s The Graph service333<https://github.com/lidofinance/lido-subgraph> on a daily basis. We can identify periods where the borrowing rate is lower than the staking rate, suggesting that a “loopy” strategy would have been profitable, as well as highly volatile periods where this is no longer the case. To reduce noise in the backtest, we apply a one-day moving average to the borrowing rate. In contrast, the staking rate, which is less volatile, is used as-is.

![Refer to caption](x3.png)


(a) market 11

![Refer to caption](x4.png)


(b) market 22

Figure 3: Evolution of the interest rate (solid line: effective rate; dashed line: rate at target) for the two largest wstETH/WETH markets on Morpho on the Ethereum blockchain, compared to the staking rate from January 1, 2025 to April 1, 2025.

### 6.2 Backtesting

We perform a backtest of the “loopy” strategy using the dataset described above. Two budget configurations are considered: a low budget of $10k, which has a moderate impact on the liquidity pools, and a high budget of $10m, whose impact is significant. In addition, the backtest is also conducted with both hourly and daily rebalancing to evaluate the effect of the rebalancing frequency on the strategy’s performance. Table [2](https://arxiv.org/html/2601.14005v1#S6.T2 "Table 2 ‣ 6.2 Backtesting ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") reports the resulting APYs across the different configurations over the backtesting period.

| strategy | initial investment ($\mathdollar) | rebalancing frequency | ℓmax\ell^{\text{max}} | APY (%\%) |
| --- | --- | --- | --- | --- |
| loopy (low cap, 1h-freq) | 10​k10\text{k} | 1​h1\text{h} | 55 | 6.26.2 |
| loopy (low cap, 1d-freq) | 10​k10\text{k} | 1​d1\text{d} | 55 | 5.85.8 |
| loopy (high cap, 1h-freq) | 10​m10\text{m} | 1​h1\text{h} | 55 | 3.73.7 |
| loopy (high cap, 1d-freq) | 10​m10\text{m} | 1​d1\text{d} | 55 | 3.73.7 |
| staking | ⋅\cdot | ⋅\cdot | 11 | 3.13.1 |

Table 2: Characteristics and performance of the leveraged strategy compared to staking on the Ethereum blockchain from January 1, 2025 to April 1, 2025.

First, we assume a zero-fee setting in the backtest. While this assumption is not realistic in practice, it provides a benchmark for evaluating the ideal performance of the strategy in the absence of transaction costs.

![Refer to caption](x5.png)


(a) 1h-freq rebalancing

![Refer to caption](x6.png)


(b) 1d-freq rebalancing

Figure 4: Evolution of the WETH positions of the “loopy” (low cap) strategy on the Ethereum blockchain from January 1, 2025 to April 1, 2025.

Table [2](https://arxiv.org/html/2601.14005v1#S6.T2 "Table 2 ‣ 6.2 Backtesting ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") reveals several key insights. First, the leveraged strategy significantly outperforms simple staking across all configurations, with APYs ranging from 3.7%3.7\% to 6.2%6.2\% compared to 3.1%3.1\% for staking alone, representing up to a twofold improvement. Second, capital size has a substantial impact on achievable returns: the low-cap strategy ($10k) achieves nearly double the APY of the high-cap strategy ($10m). This *size effect* is a direct consequence of our theoretical framework: larger positions drive up pool utilization rates, which increases borrowing costs and reduces the spread between staking yield and borrowing rate. Third, rebalancing frequency matters more for smaller positions: hourly rebalancing improves APY by approximately 0.40.4 percentage points for low-cap strategies (6.2%6.2\% vs. 5.8%5.8\%), while making virtually no difference for high-cap strategies (3.7%3.7\% in both cases). This suggests that for large positions, the market impact of rebalancing dominates any benefits from faster rate arbitrage.

![Refer to caption](x7.png)


(a) 1h-freq rebalancing

![Refer to caption](x8.png)


(b) 1d-freq rebalancing

Figure 5: Evolution of the WETH positions of the “loopy” (high cap) strategy on the Ethereum blockchain from January 1, 2025 to April 1, 2025.

Figures [4](https://arxiv.org/html/2601.14005v1#S6.F4 "Figure 4 ‣ 6.2 Backtesting ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms")–[5](https://arxiv.org/html/2601.14005v1#S6.F5 "Figure 5 ‣ 6.2 Backtesting ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") illustrate the evolution of position allocations over the backtesting period, where negative positions correspond to the debt contracted on the markets. For low-cap strategies, the optimizer frequently reallocates between markets based on relative rate conditions, demonstrating active exploitation of rate differentials. In contrast, high-cap strategies show more stable allocations, as the size effect limits the profitability of aggressive rebalancing.

![Refer to caption](x9.png)


Figure 6: APY of the “loopy” strategy with respect to initial investment on the Ethereum blockchain from January 1, 2025 to April 1, 2025.

Figure [6](https://arxiv.org/html/2601.14005v1#S6.F6 "Figure 6 ‣ 6.2 Backtesting ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") presents the APY as a function of initial investment, clearly illustrating the monotonically decreasing relationship predicted by our theoretical analysis. The curve exhibits a steep decline for investments below $1m, after which returns asymptotically approach the simple staking rate as position size dominates pool utilization.

![Refer to caption](x10.png)


Figure 7: APY of the “loopy” (1d-freq) strategy with respect to initial investment on the Ethereum blockchain for different values of ℓmax\ell^{\text{max}} from January 1, 2025 to April 1, 2025.

Figure [7](https://arxiv.org/html/2601.14005v1#S6.F7 "Figure 7 ‣ 6.2 Backtesting ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") presents the APY as a function of initial investment for different values of ℓmax\ell^{\text{max}} (1d-freq). While the differences across configurations are significant for small-cap investments, they become negligible for large-cap allocations, as market saturation prevents the strategy from exploiting the full investment capacity.

![Refer to caption](x11.png)


Figure 8: APY of the “loopy” strategy with respect to initial investment including fees on the Ethereum blockchain from January 1, 2025 to April 1, 2025.

Second, we introduce a 11bp fee for selling wstETH for WETH. Both strategies—whether rebalanced daily or hourly—are significantly affected by the fee. Indeed, the high volatility of the borrowing rate can generate false signals, leading the strategy to rebalance, only to rebalance again shortly after. To address this issue, we introduce a third strategy, denoted “loopy” (dynamic), in which rebalancing occurs only if the expected yield after rebalancing exceeds the current yield by more than 2020bps. Figure [8](https://arxiv.org/html/2601.14005v1#S6.F8 "Figure 8 ‣ 6.2 Backtesting ‣ 6 Numerical results ‣ Leveraged positions on decentralized lending platforms") presents the APY as a function of initial investment. While loopy strategies—whether rebalanced daily or hourly—underperform beyond $3m and $1m invested, respectively, the dynamic strategy still outperforms native staking even with $10m.

(See Appendix [E](https://arxiv.org/html/2601.14005v1#A0.SS5 "E Backtest on the Base blockchain ‣ Appendix ‣ Leveraged positions on decentralized lending platforms") for the backtest on the Base blockchain.)

## 7 Discussion and conclusion

This paper presents a comprehensive mathematical framework for optimizing leveraged staking strategies across multiple DeFi lending markets. We derived closed-form solutions for optimal capital allocation under three interest rate models (linear, kinked, and adaptive) and validated our theoretical results through backtesting on the Ethereum and Base blockchains. Our results demonstrate that optimal rebalancing can significantly enhance returns, with APYs reaching 6.2%6.2\% for small capital positions compared to 3.1%3.1\% for simple staking.

#### Key findings

Our backtesting results reveal several important insights. First, capital size has a substantial impact on achievable returns: smaller positions ($10k) achieve significantly higher APYs than larger positions ($10m) due to their reduced impact on pool utilization rates. Second, rebalancing frequency matters, though the marginal benefit diminishes beyond hourly rebalancing.

#### Limitations and assumptions

Our framework relies on several simplifying assumptions that warrant discussion. First, we assume complete liquidity; i.e., that positions can be opened, closed, and rebalanced instantaneously without slippage. While this is approximately true for small positions, large capital movements may face liquidity constraints in practice. Second, we treat the staking rate as exogenous and constant, whereas in reality it varies based on validator performance and network conditions. Third, and most importantly, our analysis assumes a single agent optimizing in isolation. When multiple sophisticated agents employ similar strategies, game-theoretic considerations become crucial.

#### Game-theoretic considerations

If many agents simultaneously pursue optimal leveraged strategies, a feedback loop emerges: increased borrowing demand raises utilization rates, which increases borrowing costs, which in turn reduces the profitability of leveraged positions. This creates a Nash equilibrium where individual optimization may lead to collectively suboptimal outcomes. Analyzing this multi-agent scenario requires extending our framework to incorporate strategic interactions, potentially using mean-field game theory or evolutionary game dynamics. This represents an important direction for future research.

#### Future directions

Several extensions of this work merit investigation. First, incorporating stochastic interest rate dynamics and staking rate volatility would enable risk-adjusted optimization and Value-at-Risk constraints. Second, analyzing the impact of liquidation risk under volatile collateral prices would provide more robust strategies for real-world deployment. Third, extending the framework to include multiple collateral types and cross-chain opportunities would capture the full complexity of modern DeFi ecosystems. Finally, empirical analysis of how quickly capital actually moves in response to rate differentials would validate our complete liquidity assumption and inform practical rebalancing policies.

In conclusion, this work demonstrates that rigorous mathematical optimization can substantially improve DeFi investment strategies. The transparency and programmability of DeFi protocols enable a level of analytical precision impossible in traditional finance. As the DeFi ecosystem matures, we anticipate that such optimization frameworks will become standard tools for both individual investors and institutional participants.

## References

* AAVE (2020)
  Aave v1.
  Note: Available at <https://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf>
  Cited by: [§1](https://arxiv.org/html/2601.14005v1#S1.p3.1 "1 Introduction ‣ Leveraged positions on decentralized lending platforms"),
  [§1](https://arxiv.org/html/2601.14005v1#S1.p4.1 "1 Introduction ‣ Leveraged positions on decentralized lending platforms"),
  [§4.3](https://arxiv.org/html/2601.14005v1#S4.SS3.p1.5 "4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms"),
  [§4.4](https://arxiv.org/html/2601.14005v1#S4.SS4.p1.9 "4.4 Kinked rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms").
* C. Alexander (2024)
  Leveraged restaking of leveraged staking: What are the risks?.
  Cited by: [§2](https://arxiv.org/html/2601.14005v1#S2.p4.1 "2 Related work ‣ Leveraged positions on decentralized lending platforms").
* M. Bartoletti, J. H. Chiang, and A. L. Lafuente (2021)
  SoK: Lending pools in decentralized finance.
  In International Conference on Financial Cryptography and Data Security,
   pp. 553–578.
  Cited by: [§2](https://arxiv.org/html/2601.14005v1#S2.p1.1 "2 Related work ‣ Leveraged positions on decentralized lending platforms").
* C. Bertucci, L. Bertucci, M. G. Delaunay, O. Gueant, and M. Lesbre (2025)
  Agents’ behavior and interest rate model optimization in DeFi lending.
  Mathematical Finance.
  Cited by: [§2](https://arxiv.org/html/2601.14005v1#S2.p3.1 "2 Related work ‣ Leveraged positions on decentralized lending platforms").
* S. P. Boyd and L. Vandenberghe (2004)
  Convex optimization.
   Cambridge University Press.
  Cited by: [§4.3](https://arxiv.org/html/2601.14005v1#S4.SS3.p2.1 "4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms").
* Morpho (2023)
  AdaptiveCurveIRM.
  Note: Available at <https://docs.morpho.org/morpho/contracts/irm/adaptive-curve-irm/>
  Cited by: [§1](https://arxiv.org/html/2601.14005v1#S1.p3.1 "1 Introduction ‣ Leveraged positions on decentralized lending platforms"),
  [§1](https://arxiv.org/html/2601.14005v1#S1.p4.1 "1 Introduction ‣ Leveraged positions on decentralized lending platforms"),
  [§4.5](https://arxiv.org/html/2601.14005v1#S4.SS5.p1.1 "4.5 Adaptive rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms").
* M. Patriksson (2008)
  A survey on the continuous nonlinear resource allocation problem.
  European Journal of Operational Research 185 (1),  pp. 1–46.
  Cited by: [§4](https://arxiv.org/html/2601.14005v1#S4.p10.2 "4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms").
* N. Tovanich, M. Kassoul, S. Weidenholzer, and J. Prat (2023)
  Contagion in decentralized lending protocols: A case study of Compound.
  In Proceedings of the 2023 Workshop on Decentralized Finance and Security,
   pp. 55–63.
  Cited by: [§2](https://arxiv.org/html/2601.14005v1#S2.p2.1 "2 Related work ‣ Leveraged positions on decentralized lending platforms").

## Appendix

### A Proof of equivalence between ([8](https://arxiv.org/html/2601.14005v1#S4.E8 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) and ([10](https://arxiv.org/html/2601.14005v1#S4.E10 "In 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms"))

The action takes place in ℝ2​n\mathbb{R}^{2n} where nn is the number of markets at play. We pick a maximum leverage ℓimax>1\ell^{\text{max}}\_{i}>1 for i=1,…,ni=1,\ldots,n, and a budget size ξ>0\xi>0. The respective domains (thus parameterized) of the two problems are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D1​(ξ,ℓmax)={(x,ℓ)∣xi≥0,∑i=1nxi=ξ,ℓi≥1,ℓi≤ℓimax}D\_{1}(\xi,\ell^{\text{max}})=\{(x,\ell)\mid x\_{i}\geq 0,\,\sum\_{i=1}^{n}x\_{i}=\xi,\,\ell\_{i}\geq 1,\,\ell\_{i}\leq\ell^{\text{max}}\_{i}\} |  | (45) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | D2​(ξ)={(x0,x1)∣xi0≥0,xi1≥0,∑i=1nxi0+∑inxi1=ξ}D\_{2}(\xi)=\{(x^{0},x^{1})\mid x^{0}\_{i}\geq 0,\,x^{1}\_{i}\geq 0,\,\sum\_{i=1}^{n}x^{0}\_{i}+\sum\_{i}^{n}x^{1}\_{i}=\xi\} |  | (46) |

We wish to show that the following map is a bijection between D1​(ξ,ℓmax)D\_{1}(\xi,\ell^{\text{max}}) and D2​(ξ)D\_{2}(\xi):

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​(ℓmax):(xi,ℓi)↦(xi​ℓimax−ℓiℓimax−1,xi​ℓi−1ℓimax−1)\theta(\ell^{\text{max}}):(x\_{i},\ell\_{i})\mapsto(x\_{i}\,\frac{\ell^{\text{max}}\_{i}-\ell\_{i}}{\ell^{\text{max}}\_{i}-1},x\_{i}\,\frac{\ell\_{i}-1}{\ell^{\text{max}}\_{i}-1}) |  | (47) |

Since ℓimax>1\ell^{\text{max}}\_{i}>1 this map is well-defined on ℝ2​n\mathbb{R}^{2n}.

Let’s first show that θ​(D1)⊆D2\theta(D\_{1})\subseteq D\_{2}. Clearly, xi0x^{0}\_{i}, xi1≥0x^{1}\_{i}\geq 0. Also xi0+xi1=xix^{0}\_{i}+x^{1}\_{i}=x\_{i}, therefore the budget constraint is also satisfied.

We can invert θ\theta on ℝ2​n\mathbb{R}^{2n}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ−1:(xi0,xi1)↦(xi0+xi1,xi0+ℓimax​xi1xi0+xi1)\theta^{-1}:(x^{0}\_{i},x^{1}\_{i})\mapsto(x^{0}\_{i}+x^{1}\_{i},\frac{x^{0}\_{i}+\ell^{\text{max}}\_{i}x^{1}\_{i}}{x^{0}\_{i}+x^{1}\_{i}}) |  | (48) |

and θ−1\theta^{-1} is easily seen to restrict from D2D\_{2} to D1D\_{1}.

To maximize the first objective F1F\_{1} on D1​(ξ,ℓmax)D\_{1}(\xi,\ell^{\text{max}}) is therefore equivalent to maximizing the second objective F2​(ℓmax)F\_{2}(\ell^{\text{max}}) on D2​(ξ)D\_{2}(\xi). Let hi​(x)=x​bi​(x)h\_{i}(x)=xb\_{i}(x), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F1​(x,ℓ)=(∑i=1nxi​ℓi)​s−∑i=1nhi​(xi​(ℓi−1))F\_{1}(x,\ell)=(\sum\_{i=1}^{n}x\_{i}\ell\_{i})s-\sum\_{i=1}^{n}h\_{i}(x\_{i}(\ell\_{i}-1)) |  | (49) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | F2​(ℓmax)​(x0,x1)=(∑i=1nxi0)​s+(∑i=1nxi1​ℓimax)​s−∑i=1nhi​(xi1​(ℓimax−1))F\_{2}(\ell^{\text{max}})(x^{0},x^{1})=(\sum\_{i=1}^{n}x^{0}\_{i})s+(\sum\_{i=1}^{n}x^{1}\_{i}\ell^{\text{max}}\_{i})s-\sum\_{i=1}^{n}h\_{i}(x^{1}\_{i}(\ell^{\text{max}}\_{i}-1)) |  | (50) |

The claim above is true because F2​(ℓmax)∘θ=F1F\_{2}(\ell^{\text{max}})\circ\theta=F\_{1} as can be readily verified:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F2​(ℓmax)​(θ​(x,ℓ))=s​∑i=1nxi​ℓi−∑i=1nhi​(xi​(ℓi−1))=F1​(x,ℓ)F\_{2}(\ell^{\text{max}})(\theta(x,\ell))=s\sum\_{i=1}^{n}x\_{i}\ell\_{i}-\sum\_{i=1}^{n}h\_{i}(x\_{i}(\ell\_{i}-1))=F\_{1}(x,\ell) |  | (51) |

Not only those problems have the same maximiser, but the max values are the same (they are the optimal cash flow).

### B Proof of Proposition [1](https://arxiv.org/html/2601.14005v1#Thmproposition1 "Proposition 1 (Linear rate) ‣ 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")

Substituting the linear rate model ([21](https://arxiv.org/html/2601.14005v1#S4.E21 "In 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) into the first-order condition ([14](https://arxiv.org/html/2601.14005v1#S4.E14 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) yields: xi∗​(λ)=αi​[βi−λ]+x^{\*}\_{i}(\lambda)=\alpha\_{i}\big[\beta\_{i}-\lambda\big]^{+} for i=1,…,ni=1,\ldots,n, where the parameters are defined in ([23](https://arxiv.org/html/2601.14005v1#S4.E23 "In Proposition 1 (Linear rate) ‣ 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")).

Let the markets be ordered according to ([25](https://arxiv.org/html/2601.14005v1#S4.E25 "In Proposition 1 (Linear rate) ‣ 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")), and let k∈{1,…,n}k\in\{1,\ldots,n\} be such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βk≥λ∗>βk+1\beta\_{k}\geq\lambda^{\*}>\beta\_{k+1} |  | (52) |

The optimal allocation then takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi∗​(λ∗)={αi​[βi−λ∗]if ​i≤k0if ​i>kx^{\*}\_{i}(\lambda^{\*})=\left\{\begin{array}[]{ll}\alpha\_{i}\big[\beta\_{i}-\lambda^{\*}\big]&\mbox{if }i\leq k\\ 0&\mbox{if }i>k\end{array}\right. |  | (53) |

The budget constraint ([15](https://arxiv.org/html/2601.14005v1#S4.E15 "In Unsaturated markets with fully leveraged positions (𝜆^∗>𝑠) ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1nxj∗​(λ∗)=∑j=1kαj​[βj−λ∗]=ξ\sum^{n}\_{j=1}x^{\*}\_{j}(\lambda^{\*})=\sum^{k}\_{j=1}\alpha\_{j}\big[\beta\_{j}-\lambda^{\*}\big]=\xi |  | (54) |

from which we deduce ([24](https://arxiv.org/html/2601.14005v1#S4.E24 "In Proposition 1 (Linear rate) ‣ 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")). Substituting ([24](https://arxiv.org/html/2601.14005v1#S4.E24 "In Proposition 1 (Linear rate) ‣ 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) into ([53](https://arxiv.org/html/2601.14005v1#A0.E53 "In B Proof of Proposition 1 ‣ Appendix ‣ Leveraged positions on decentralized lending platforms")) yields the optimal allocation ([22](https://arxiv.org/html/2601.14005v1#S4.E22 "In Proposition 1 (Linear rate) ‣ 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")). Finally, condition ([52](https://arxiv.org/html/2601.14005v1#A0.E52 "In B Proof of Proposition 1 ‣ Appendix ‣ Leveraged positions on decentralized lending platforms")) implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1kαj​[βj−βk]<ξ≤∑j=1k+1αj​[βj−βk+1]\sum^{k}\_{j=1}\alpha\_{j}\big[\beta\_{j}-\beta\_{k}\big]<\xi\leq\sum^{k+1}\_{j=1}\alpha\_{j}\big[\beta\_{j}-\beta\_{k+1}\big] |  | (55) |

which is the condition ([26](https://arxiv.org/html/2601.14005v1#S4.E26 "In Proposition 1 (Linear rate) ‣ 4.3 Linear rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")).

### C Proof of Proposition [2](https://arxiv.org/html/2601.14005v1#Thmproposition2 "Proposition 2 (Kinked rate) ‣ 4.4 Kinked rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")

We consider the maximization problem for a given market ii under the kinked rate model. The first-order optimality condition is derived from the KKT conditions, accounting for the non-differentiability of the objective function at the kink point. We examine the cases where the utilization rate is below and above the target rate separately.

#### Current utilization is below the target rate (S¯i​u∗−B¯i>0\bar{S}\_{i}u^{\*}-\bar{B}\_{i}>0)

The kinked rate function ([28](https://arxiv.org/html/2601.14005v1#S4.E28 "In 4.4 Kinked rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")) is piecewise linear with a discontinuity in its derivative at xi(kink)=S¯i​u∗−B¯iℓimax−1x^{(\text{kink})}\_{i}=\frac{\bar{S}\_{i}u^{\*}-\bar{B}\_{i}}{\ell^{\text{max}}\_{i}-1}. At this point, we must use the subdifferential of bib\_{i} denoted ∂bi\partial b\_{i}. The subdifferential at xi(kink)x^{(\text{kink})}\_{i} is the interval between the left and right derivatives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂bi​(xi(kink))=[rs​l​o​p​e​1S¯i​u∗,rs​l​o​p​e​2S¯i​(1−u∗)]\partial b\_{i}(x^{(\text{kink})}\_{i})=\Big[\frac{r\_{slope1}}{\bar{S}\_{i}u^{\*}},\frac{r\_{slope2}}{\bar{S}\_{i}(1-u^{\*})}\Big] |  | (56) |

The subdifferential optimality condition requires that there exists some g∈∂bi​(xi(kink))g\in\partial b\_{i}(x^{(\text{kink})}\_{i}) such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ=ℓimax​s−(ℓimax−1)​(bi​(xi(kink)​(ℓimax−1))+xi(kink)​(ℓimax−1)​g)\lambda=\ell^{\text{max}}\_{i}s-(\ell^{\text{max}}\_{i}-1)\big(b\_{i}(x^{(\text{kink})}\_{i}(\ell^{\text{max}}\_{i}-1))+x^{(\text{kink})}\_{i}(\ell^{\text{max}}\_{i}-1)g\big) |  | (57) |

Substituting bi​(xi(kink))=rb​a​s​e+rs​l​o​p​e​1b\_{i}(x^{(\text{kink})}\_{i})=r\_{base}+r\_{slope1} and xi(kink)=S¯i​u∗−B¯iℓimax−1x^{(\text{kink})}\_{i}=\frac{\bar{S}\_{i}u^{\*}-\bar{B}\_{i}}{\ell^{\text{max}}\_{i}-1} yields the condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∈[λi2,λi1]\lambda\in\big[\lambda^{2}\_{i},\lambda^{1}\_{i}\big] |  | (58) |

where λi1\lambda^{1}\_{i} and λi2\lambda^{2}\_{i} are defined in ([31](https://arxiv.org/html/2601.14005v1#S4.E31 "In Proposition 2 (Kinked rate) ‣ 4.4 Kinked rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")).
Thus, when λ∈[λi2,λi1]\lambda\in\big[\lambda^{2}\_{i},\lambda^{1}\_{i}\big], the optimal solution is xi(kink)x^{(\text{kink})}\_{i}. For λ\lambda outside this interval, the solution lies in the associated linear regime. The assumption rs​l​o​p​e​1<u∗1−u∗​rs​l​o​p​e​2r\_{slope1}<\frac{u^{\*}}{1-u^{\*}}r\_{slope2} ensures λi2<λi1\lambda^{2}\_{i}<\lambda^{1}\_{i}, validating the ordering of the regimes.

#### Current utilization is above the target rate (S¯i​u∗−B¯i<0\bar{S}\_{i}u^{\*}-\bar{B}\_{i}<0)

When current utilization exceeds the target, xi(kink)<0x^{(\text{kink})}\_{i}<0 is infeasible. Only the second linear region is relevant, reducing to a linear rate model framework.

### D Proof of Corollary [1](https://arxiv.org/html/2601.14005v1#Thmcorollary1 "Corollary 1 (Adaptive rate) ‣ 4.5 Adaptive rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms")

The adaptive rate model can be reformulated as the kinked rate model by assigning the parameters:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rb​a​s​e=rttargetkd,rs​l​o​p​e​1=rttarget​(1−1kd),rs​l​o​p​e​2=rttarget​(kd−1)r\_{base}=\frac{r^{\text{target}}\_{t}}{k\_{d}},\quad r\_{slope1}=r^{\text{target}}\_{t}\big(1-\frac{1}{k\_{d}}\big),\quad r\_{slope2}=r^{\text{target}}\_{t}\big(k\_{d}-1\big) |  | (59) |

Substituting ([59](https://arxiv.org/html/2601.14005v1#A0.E59 "In D Proof of Corollary 1 ‣ Appendix ‣ Leveraged positions on decentralized lending platforms")) into Proposition [2](https://arxiv.org/html/2601.14005v1#Thmproposition2 "Proposition 2 (Kinked rate) ‣ 4.4 Kinked rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms") yields Corollary [1](https://arxiv.org/html/2601.14005v1#Thmcorollary1 "Corollary 1 (Adaptive rate) ‣ 4.5 Adaptive rate ‣ 4 Optimal capital allocation ‣ Leveraged positions on decentralized lending platforms").

### E Backtest on the Base blockchain

| market | ID | creation date | LLTV (%\%) |
| --- | --- | --- | --- |
| 1 | b991f6fd-568b-4332-998e-3fedf6afae20 | June 11, 2024 | 94.594.5 |
| 2 | 130cec4d-4fe4-4fbb-9d85-5e2c279eb854 | May 30, 2024 | 96.596.5 |
| 3 | 13aac762-a267-4d6e-8904-9f886babec7f | July 22, 2024 | 94.594.5 |
| 4 | 58e6612e-a221-4b64-b53c-6b69c3a3836e | May 30, 2024 | 94.594.5 |

Table 3: IDs, creation dates and LLTVs of the four largest wstETH/WETH markets on Morpho on the Base blockchain.

On Base, we select the four largest Morpho markets for the wstETH/WETH pair over the period from January 1, 2025, to April 1, 2025. Although the last two are negligible compared to the top two (see Figure [9](https://arxiv.org/html/2601.14005v1#A0.F9 "Figure 9 ‣ E Backtest on the Base blockchain ‣ Appendix ‣ Leveraged positions on decentralized lending platforms")), we retain them to illustrate a backtest involving more markets than in the Ethereum case. The characteristics of each market are summarized in Table [3](https://arxiv.org/html/2601.14005v1#A0.T3 "Table 3 ‣ E Backtest on the Base blockchain ‣ Appendix ‣ Leveraged positions on decentralized lending platforms").

![Refer to caption](x12.png)


Figure 9: Evolution of WETH reserves (solid line: supplied funds; dashed line: borrowed fund) for the four largest wstETH/WETH markets on Morpho on the Base blockchain from January 1, 2025 to April 1, 2025.



![Refer to caption](x13.png)


(a) Low cap

![Refer to caption](x14.png)


(b) High cap

Figure 10: Evolution of the WETH positions of the “loopy” (1d-freq) strategy on the Base blockchain from January 1, 2025 to April 1, 2025.

Figure [10](https://arxiv.org/html/2601.14005v1#A0.F10 "Figure 10 ‣ E Backtest on the Base blockchain ‣ Appendix ‣ Leveraged positions on decentralized lending platforms") illustrates the evolution of position allocations over the backtesting period for the low- and high-cap 1d-frequency strategies. The low-cap strategy loops through all four markets, whereas the high-cap one almost exclusively loops through the first market, as the others quickly become saturated.

![Refer to caption](x15.png)


Figure 11: APY of the “loopy” strategy with respect to initial investment including fees on the Base blockchain from January 1, 2025 to April 1, 2025.

Figure [11](https://arxiv.org/html/2601.14005v1#A0.F11 "Figure 11 ‣ E Backtest on the Base blockchain ‣ Appendix ‣ Leveraged positions on decentralized lending platforms") presents the APY as a function of the initial investment including a 11bp fee for selling wstETH for WETH in the backtest. As in the Ethereum case, the dynamic strategy outperforms both daily and hourly rebalancing strategies.