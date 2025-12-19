---
authors:
- Tianyi Ma
doc_id: arxiv:2512.16080v1
family_id: arxiv:2512.16080
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol
  Supporting Arbitrary Maturities
url_abs: http://arxiv.org/abs/2512.16080v1
url_html: https://arxiv.org/html/2512.16080v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tianyi Ma

###### Abstract

In decentralized finance (DeFi), designing fixed-income lending automated market makers (AMMs) is extremely challenging due to time-related complexities. Moreover, existing protocols only support single-maturity lending. Building upon the BondMM protocol, this paper argues that its mathematical invariants are sufficiently elegant to be generalized to arbitrary maturities. This paper thus propose an improved design, BondMM-A, which supports lending activities of any maturity. By integrating fixed-income instruments of varying maturities into a single smart contract, BondMM-A offers users and liquidity providers (LPs) greater operational freedom and capital efficiency. Experimental results show that BondMM-A performs excellently in terms of interest rate stability and financial robustness.

## I Introduction

Following the 2008 financial crisis, the emergence and development of Bitcoin [[1](https://arxiv.org/html/2512.16080v1#bib.bib1)] and blockchain technology have introduced disruptive changes to the financial sector. Bitcoin pioneered decentralized digital money, and Ethereum [[2](https://arxiv.org/html/2512.16080v1#bib.bib2)], with its smart contract capabilities, further expanded blockchain applications in finance, catalyzing the rise of Decentralized Finance (DeFi) [[3](https://arxiv.org/html/2512.16080v1#bib.bib3)] and attracting massive participation.

In traditional finance, fixed-income instruments—commonly known as bonds—are financial assets that promise predetermined cash flows at specified future dates. They hold a dominant position in global financial markets: as of year-end 2023, global equity market capitalization stood at approximately $115 trillion, while the global bond market reached $141 trillion. Moreover, daily U.S. bond trading volume is roughly twice that of equities111Data Source: Huatai Xingzhi ([reprinted](https://stock.jrj.com.cn/2024/12/03080145936337.shtml)). Despite the DeFi lending market having grown to $54.6 billion222Data Source: [DefiLlama](https://defillama.com/protocols/Lending), truly fixed-income products remain rare [[4](https://arxiv.org/html/2512.16080v1#bib.bib4)]-[[8](https://arxiv.org/html/2512.16080v1#bib.bib8)].

Building on the BondMM protocol [[9](https://arxiv.org/html/2512.16080v1#bib.bib9)], this paper proposes BondMM-A, a novel AMM-based smart contract design supporting arbitrary maturities for decentralized fixed-income lending, aiming to meet this unmet market demand.

Related Work and Limitations: In DeFi, lacking traditional financial intermediaries, lending is typically facilitated through Automated Market Makers (AMMs). An AMM is a smart contract that enables users to lend, withdraw loans, borrow, and repay. Liquidity Providers (LPs) initially fund the AMM’s liquidity pool, and all user interactions occur directly with this pool. LPs earn fees or interest spreads as compensation.

Dominant DeFi lending protocols—such as AAVE [[4](https://arxiv.org/html/2512.16080v1#bib.bib4)], Compound [[5](https://arxiv.org/html/2512.16080v1#bib.bib5)], and MakerDAO [[6](https://arxiv.org/html/2512.16080v1#bib.bib6)]—primarily employ variable interest rates, treating fixed rates as supplementary features. Dedicated fixed-income protocols include Yield Protocol [[7](https://arxiv.org/html/2512.16080v1#bib.bib7)] and Notional Protocol [[8](https://arxiv.org/html/2512.16080v1#bib.bib8)].

Theoretically, these protocols set identical borrowing and lending rates, meaning LPs profit only from transaction fees. This requires sufficient secondary market trading (discussed below) rather than primary issuance. Speculators prefer longer-dated bonds due to higher leverage potential, yet current fixed-income AMMs offer only short maturities (maximum 1 year), limiting market depth. The Yield Protocol suffers from low capital efficiency and insufficient liquidity, often halting under stress. Notional Protocol attempts to resolve this but introduces new issues, such as excessively high pricing.

The BondMM protocol [[9](https://arxiv.org/html/2512.16080v1#bib.bib9)] uses a set of simple, closed-form mathematical invariants to achieve fair pricing, high capital efficiency, and stable LP equity, offering a promising path forward. However, like others, it supports only single-maturity products per contract. Since each AMM requires separate LP funding, multi-maturity support necessitates multiple disjoint liquidity pools, exposing LPs to fragmented capital risk.

Contributions: This paper enhances BondMM to propose BondMM-A, which supports arbitrary maturities within a single contract. Users can now choose from a continuous range of maturities in one interface, increasing flexibility. LPs provide liquidity to a unified pool, eliminating capital fragmentation. Overall, BondMM-A integrates user and LP needs, improving operational efficiency and capital utilization, and offering an innovative solution for decentralized fixed-income markets.

The remainder of this paper is structured as follows: Section II introduces foundational concepts; Section III details the BondMM-A design; Section IV presents experimental evaluation; Section V concludes with future outlook.

## II Preliminaries

### II-A Fixed-Income Instruments and Interest Rates

Mathematically, a fixed-income instrument can be represented as a pair of sequences: {ti}\{t\_{i}\} and {Cti}\{C\_{t\_{i}}\}, where tit\_{i} means cash flow times and CtiC\_{t\_{i}} means cash flow amounts. Typically, Ct1<0C\_{t\_{1}}<0, and Cti>0C\_{t\_{i}}>0 for i>1i>1. This means investors pay an initial outflow to purchase the bond, and receive subsequent inflows without further payment.

In the simplest case, {ti}={0,T}\{t\_{i}\}=\{0,T\}, {Cti}={−P,F}\{C\_{t\_{i}}\}=\{-P,F\}, where PP is the bond price and FF is the face value. Example: A 2-year bond with F=100F=100, P=95P=95 yields 55 in interest, giving a simple return of 5/95≈5.26%5/95\approx 5.26\%. To distinguish different maturities, practitioners use the annualized rate R=FP12−1≈2.60%R=\frac{F}{P}^{\frac{1}{2}}-1\approx 2.60\%. This interprets the 2-year bond as two consecutive 1-year bonds: investing PP at the start of year one returns P​(1+R)P(1+R) at year-end; reinvesting at the same rate returns P​(1+R)2P(1+R)^{2} at year two. If the annualized rate is constant over time, it satisfies ∑iCti​(1+R)−ti=0\sum\limits\_{i}C\_{t\_{i}}(1+R)^{-t\_{i}}=0. In continuous compounding, let r=ln⁡(1+R)r=\ln(1+R); then ∑iCti​e−ti​r=0\sum\limits\_{i}C\_{t\_{i}}e^{-t\_{i}r}=0. In the example, r=ln⁡(1+R)≈2.56%r=\ln(1+R)\approx 2.56\%. Unless noted, all rates below are continuously compounded annualized rates. Complex fixed-income products can be decomposed into simple ones via their cash-flow series, so this paper focus on the simplest case: {ti}={0,T}\{t\_{i}\}=\{0,T\}, {Cti}={−P,F}\{C\_{t\_{i}}\}=\{-P,F\}.

In reality, market mechanisms equalize rates for products with the same maturity—the market rate—but it fluctuates over time, so different maturities carry different rates. In the earlier example, if both 1-year and 2-year rates are 2.56%2.56\% initially but the 1-year rate rises after one year, the optimal choice is two consecutive 1-year bonds. Strictly, the instantaneous rate rr is a continuous function r​(t)r(t); a simple product satisfies F=P​e∫0Tr​d​tF=Pe^{\int\_{0}^{T}r\text{d}t}. Because r​(t)r(t) is uncertain, it is usually assumed constant over short horizons in practice.

Rate volatility makes bonds speculative assets. Traders can profit by buying and selling between issuance and maturity. Trades at issuance and maturity are primary trades that mint or burn bonds; trades in between are secondary trades that merely transfer bonds.

### II-B Fixed-Income AMM

Consider a bond maturing at time TT with face value 11 (in some digital currency such as DAI); it can be tokenized. A fixed-income AMM holds two tokens: bonds and currency. Currency is supplied by LPs; bonds are minted when the AMM is created. At any time, let tt be time to maturity; the AMM state is (x,y,r,p)(x,y,r,p), where x,yx,y are bond and currency balances, rr is the marginal rate, and pp is the marginal price. Assuming no spread, rr is the marginal rate for both lenders and borrowers. Theoretically p=e−t​r⇔r=1t​ln⁡1pp=e^{-tr}\Leftrightarrow r=\frac{1}{t}\ln\frac{1}{p}. In practice AMMs define r,pr,p as functions of (x,y)(x,y) so market forces adjust them; (x,y)(x,y) uniquely determines state, and different designs give different formulas for r,pr,p.

An AMM typically exposes four operations: lend (buy bonds), withdraw a loan (sell bonds), borrow, and repay. Each changes the two balances inversely. Lending injects cash and receives bonds; withdrawing injects bonds and receives cash. Borrowing requires collateral (often worth 150%150\% of the loan), receives cash, and the pool mints bonds; repaying injects cash, returns collateral, and the pool burns bonds. If a borrower fails to repay before maturity, the pool liquidates collateral. Any trade can be expressed as (Δ​x,Δ​y)(\Delta x,\Delta y): Δ​x>0\Delta x>0 (i.e., Δ​y<0\Delta y<0) for borrowing or withdrawing, and Δ​x<0\Delta x<0 (i.e., Δ​y>0\Delta y>0) for lending or repaying.

An ideal fixed-income AMM should satisfy:

Property 1 (Operability): After a trade (Δ​x,Δ​y)(\Delta x,\Delta y) on AMM (x,y)(x,y), balances remain nonnegative: x+Δ​x≥0,y+Δ​y≥0x+\Delta x\geq 0,\;y+\Delta y\geq 0.

Property 2 (Computability): Given Δ​x\Delta x, compute the unique Δ​y\Delta y (or prove it absent) in constant time, and vice versa.

Property 3 (Par Redemption): At t=0t=0, r=0,p=1r=0,p=1, independent of x,yx,y; one unit of bond equals one unit of currency.

Property 4 (Path Independence): For fixed tt, if (Δ​x1,Δ​y1)(\Delta x\_{1},\Delta y\_{1}) and (Δ​x2,Δ​y2)(\Delta x\_{2},\Delta y\_{2}) are two consecutive valid trades from state (x,y)(x,y), then (Δ​x1+Δ​x2,Δ​y1+Δ​y2)(\Delta x\_{1}+\Delta x\_{2},\Delta y\_{1}+\Delta y\_{2}) is also valid. Equivalently, buying Δ​x1\Delta x\_{1} then Δ​x2\Delta x\_{2} units of bonds at the same moment equals buying Δ​x1+Δ​x2\Delta x\_{1}+\Delta x\_{2} once.

Path independence typically comes from a conservation relation ft​(x,y)=0f\_{t}(x,y)=0 where, for fixed tt, xx and yy map one-to-one in the domain. Any valid trade satisfies ft​(x+Δ​x,y+Δ​y)=0f\_{t}(x+\Delta x,y+\Delta y)=0. Then r=−∂y∂xr=-\frac{\partial y}{\partial x} gives the marginal rate and p=e−t​rp=e^{-tr} the marginal price.

Property 5 (Economic Soundness): Convergence to market equilibrium should be stable with limited arbitrage. In particular, rates should be nonnegative, i.e., prices should not exceed 1.

### II-C Existing Protocols

This paper summarizes existing fixed-income AMMs: Yield, Notional, and BondMM.

#### II-C1 Yield Protocol

The Yield Protocol [[7](https://arxiv.org/html/2512.16080v1#bib.bib7)] constructs the invariant:

|  |  |  |
| --- | --- | --- |
|  | ft​(x,y)=x1−t/T+y1−t/T−C​(t)=0,f\_{t}(x,y)=x^{1-t/T}+y^{1-t/T}-C(t)=0, |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | p=−∂y∂x=(yx)t/T=ϕ−t/T,p=-\dfrac{\partial y}{\partial x}=\left(\dfrac{y}{x}\right)^{t/T}=\phi^{-t/T}, |  |

And thus

|  |  |  |
| --- | --- | --- |
|  | r=1t​ln⁡1p=1t​ln⁡ϕt/T=1T​ln⁡ϕ,r=\dfrac{1}{t}\ln\dfrac{1}{p}=\dfrac{1}{t}\ln\phi^{t/T}=\dfrac{1}{T}\ln\phi, |  |

Here ϕ=yx\phi=\frac{y}{x} is the bond-to-cash ratio. When ϕ<1\phi<1, r<0r<0 and negative rates appear, violating economic soundness; no one wants to lend, severely reducing liquidity.

#### II-C2 Notional Protocol

Unlike the general case, the Notional Protocol [[8](https://arxiv.org/html/2512.16080v1#bib.bib8)] prices with simple interest, p​(1+r​t)=1p(1+rt)=1, where tt is time to maturity. To avoid Yield’s negative-rate issue, Notional introduces two (possibly time-varying) parameters κ∈(0,1)\kappa\in(0,1) and r∗∈(0,1)r^{\*}\in(0,1), where r∗r^{\*} is the anchor rate and κ\kappa controls rate volatility. Under this protocol,

|  |  |  |
| --- | --- | --- |
|  | r=κ​ln⁡ϕ+r∗,r=\kappa\ln\phi+r^{\*}, |  |

So

|  |  |  |
| --- | --- | --- |
|  | p=11+r​t=(1+t​κ​ln⁡ϕ+t​r∗)−1.p=\dfrac{1}{1+rt}=(1+t\kappa\ln\phi+tr^{\*})^{-1}. |  |

Notional does not price via a conservation law but via a pricing formula. Given Δ​x\Delta x, define

|  |  |  |
| --- | --- | --- |
|  | ϕ¯=x+Δ​xy−Δ​x,\bar{\phi}=\dfrac{x+\Delta x}{y-\Delta x}, |  |

The average trade price is

|  |  |  |
| --- | --- | --- |
|  | p¯=(1+t​κ​ln⁡ϕ¯+t​r∗)−1,\bar{p}=(1+t\kappa\ln\bar{\phi}+tr^{\*})^{-1}, |  |

So Δ​y=−p¯​Δ​x\Delta y=-\bar{p}\Delta x.

If Δ​x<0\Delta x<0 (lend or repay), then p¯<1\bar{p}<1, so the post-trade ϕ′=x+Δ​xy−p¯​Δ​x<ϕ¯\phi^{\prime}=\frac{x+\Delta x}{y-\bar{p}\Delta x}<\bar{\phi}, giving p′>p¯p^{\prime}>\bar{p}. The user pays a price higher than both surrounding marginal prices—an extra interest cost to LPs—so Notional is less attractive to borrowers. It clearly lacks path independence. It is also hard to derive Δ​x\Delta x from Δ​y\Delta y, violating computability.

#### II-C3 BondMM Protocol

The BondMM protocol [[9](https://arxiv.org/html/2512.16080v1#bib.bib9)] introduces the bond present value (current-time price)

|  |  |  |  |
| --- | --- | --- | --- |
|  | X=x​p=x​e−r​t,X=xp=xe^{-rt}, |  | (1) |

And sets the rate as a function of X/yX/y:

|  |  |  |
| --- | --- | --- |
|  | r=R​(ψ),ψ=Xy,r=R(\psi),\psi=\dfrac{X}{y}, |  |

Unlike protocols that keep the bond amount fixed over time, BondMM seeks—by economic intuition—to keep the present value of bonds unchanged. With positive rates, present value decays, so BondMM gradually burns bonds in the pool.

Specifically, BondMM chooses RR similar to Notional:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=R​(ψ)=κ​ln⁡ψ+r∗=κ​ln⁡Xy+r∗.r=R(\psi)=\kappa\ln\psi+r^{\*}=\kappa\ln\dfrac{X}{y}+r^{\*}. |  | (2) |

It can be shown (Tran et al. [[9](https://arxiv.org/html/2512.16080v1#bib.bib9)], likewise below):

|  |  |  |
| --- | --- | --- |
|  | r=11+κ​t​(κ​ln⁡xy+r∗),r=\dfrac{1}{1+\kappa t}\left(\kappa\ln\dfrac{x}{y}+r^{\*}\right), |  |

|  |  |  |
| --- | --- | --- |
|  | p=[(xy)​er∗]−t/(1+κ​t).p=\left[\left(\dfrac{x}{y}\right)e^{r^{\*}}\right]^{-t/(1+\kappa t)}. |  |

Assume at pool creation LPs deposit y0y\_{0} cash and the initial rate is r0r\_{0}. To satisfy r0=r∗r\_{0}=r^{\*}, X0=y0X\_{0}=y\_{0} is needed, so mint x0=X0/p0=X0​eT​r0x\_{0}=X\_{0}/p\_{0}=X\_{0}e^{Tr\_{0}} units of bonds.

At any moment,

|  |  |  |
| --- | --- | --- |
|  | p=−∂y∂x=e−r​t,p=-\dfrac{\partial y}{\partial x}=e^{-rt}, |  |

And thus

|  |  |  |
| --- | --- | --- |
|  | r=R​(Xy)⇒y=XR−1​(r)=x​e−r​tR−1​(r),r=R\left(\dfrac{X}{y}\right)\Rightarrow y=\dfrac{X}{R}^{-1}(r)=\dfrac{xe^{-rt}}{R^{-1}(r)}, |  |

With initial values (x0,y0,r0)(x\_{0},y\_{0},r\_{0}), solving the differential equations yields:

|  |  |  |
| --- | --- | --- |
|  | x=X0​er0​[e(r−r0/κ)​e(r0−r∗)/κ+1e(r−r∗)/κ+1]1+κ​t,y=y0​[e(r0−r∗)/κ+1e(r−r∗)/κ+1]1+κ​t,\begin{array}[]{l}x=X\_{0}e^{r\_{0}}\left[e^{(r-r\_{0}/\kappa)}\dfrac{e^{(r\_{0}-r^{\*})/\kappa}+1}{e^{(r-r^{\*})/\kappa}+1}\right]^{1+\kappa t},\\ y=y\_{0}\left[\dfrac{e^{(r\_{0}-r^{\*})/\kappa}+1}{e^{(r-r^{\*})/\kappa}+1}\right]^{1+\kappa t}\end{array}, |  |

Hence BondMM satisfies the invariant

|  |  |  |  |
| --- | --- | --- | --- |
|  | K​xα+yα=C,Kx^{\alpha}+y^{\alpha}=C, |  | (3) |

Where

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=(1+κ​t)−1,K=e−t​r∗​α,C=y0α​[e(r0−r∗)/κ+1],\alpha=(1+\kappa t)^{-1},K=e^{-tr^{\*}\alpha},C=y\_{0}^{\alpha}[e^{(r\_{0}-r^{\*})/\kappa}+1], |  | (4) |

And XX and yy also satisfy an invariant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yα​(Xy+1)=C.y^{\alpha}(\dfrac{X}{y}+1)=C. |  | (5) |

For a new trade (Δ​x,Δ​y)(\Delta x,\Delta y), the AMM state before and after satisfies the invariant ([3](https://arxiv.org/html/2512.16080v1#S2.E3 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")):

|  |  |  |
| --- | --- | --- |
|  | K​(x+Δ​x)α+(y+Δ​y)α=C=K​xα+yα,K(x+\Delta x)^{\alpha}+(y+\Delta y)^{\alpha}=C=Kx^{\alpha}+y^{\alpha}, |  |

Thus, the following can be calculated from Δ​x\Delta x:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​y=[C−K​(x+Δ​x)α]1/α−y=y​[Xy+1−((Xy)1/α+e−r∗​t​Δ​xy)α]1/α−y,\begin{split}\Delta y&=\left[C-K(x+\Delta x)^{\alpha}\right]^{1/\alpha}-y\\ &=y\left[\dfrac{X}{y}+1-\left(\left(\dfrac{X}{y}\right)^{1/\alpha}+e^{-r^{\*}t}\dfrac{\Delta x}{y}\right)^{\alpha}\right]^{1/\alpha}-y,\end{split} |  | (6) |

Similarly, the following can be calculated from Δ​y\Delta y:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​x=er∗​t​y​[(Xy+1−(Δ​yy+1)a)1/α−(Xy)1/α].\Delta x=e^{r^{\*}t}y\left[\left(\dfrac{X}{y}+1-\left(\dfrac{\Delta y}{y}+1\right)^{a}\right)^{1/\alpha}-\left(\dfrac{X}{y}\right)^{1/\alpha}\right]. |  | (7) |

In Tran et al.’s experiments [[9](https://arxiv.org/html/2512.16080v1#bib.bib9)], r∗r^{\*} is set to r0r\_{0} and κ\kappa to 0.020.02, but both can vary over time so BondMM can adapt to market conditions. With suitable parameters, BondMM satisfies operability, computability, par redemption, path independence, and economic soundness.

BondMM also considers financial stability: the pool’s cash should cover all debt, so trades that could cause insolvency are rejected. Let bb and ll denote borrow and lend amounts; net equity is E=y+(b−l)​pE=y+(b-l)p. Ideally E=y0E=y\_{0}, meaning LPs neither lose nor gain beyond fees. BondMM rejects lending when EE trends substantially below y0y\_{0} [[9](https://arxiv.org/html/2512.16080v1#bib.bib9)].

## III BondMM-A: New Design

BondMM replaces face value with present value in the time conservation, inspiring a new design path. This will bring a question: Is tokenizing present value instead of the bond itself be a better way to further simplify fixed-income AMMs and support arbitrary maturities? Fortunately, BondMM’s elegant invariants enable this.

From ([1](https://arxiv.org/html/2512.16080v1#S2.E1 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")) and ([2](https://arxiv.org/html/2512.16080v1#S2.E2 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | x=X​er​t=X​er∗​t+κ​t​ln⁡(X/y),x=Xe^{rt}=Xe^{r^{\*}t+\kappa t\ln(X/y)}, |  | (8) |

Because the BondMM-A pool itself has no maturity, AMM state is no longer tied to clock time. Here tt denotes the maturity of the bond under consideration, and xx is the face value of a tt-maturity bond equivalent to the pool’s remaining present value. The parameters α,K,C\alpha,K,C in ([4](https://arxiv.org/html/2512.16080v1#S2.E4 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")) are functions of tt, so the invariants ([3](https://arxiv.org/html/2512.16080v1#S2.E3 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")) and ([5](https://arxiv.org/html/2512.16080v1#S2.E5 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")) still hold with the new meaning of tt, yielding infinitely many invariants at each moment. After a trade with maturity tt, only one invariant remains valid; others break. This does not affect operability, computability, par redemption, path independence, or economic soundness. Pricing still follows ([6](https://arxiv.org/html/2512.16080v1#S2.E6 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")) and ([7](https://arxiv.org/html/2512.16080v1#S2.E7 "In II-C3 BondMM Protocol ‣ II-C Existing Protocols ‣ II Preliminaries ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities")), with tt being the trade’s maturity. Pool initialization matches BondMM, with required face value X0=y0X\_{0}=y\_{0} minted.

For implementation, trades specify both amount and maturity, so transferring “present-value tokens” alone is insufficient. Alternatives include recording each user’s bond face value and maturity on-chain, or restricting maturities to a finite set and issuing one token per discrete tenor.

If r∗r^{\*} is fixed, BondMM-A would produce identical rates across maturities, contradicting reality. Since r∗r^{\*} can depend on maturity, the contract can set r∗r^{\*} as a function of tenor (e.g., a polynomial) and let the owner tune parameters to shape the curve and match market shifts.

Like BondMM, BondMM-A must ensure solvency. Because trades span different maturities, simply computing E=y+(b−l)​pE=y+(b-l)p is inefficient. Instead maintain LL, the present value of all outstanding borrows minus unrepaid loans, updating it over time via d​ln⁡L=r​d​t\text{d}\ln L=r\text{d}t. Then E=y+LE=y+L; if EE trends meaningfully below y0y\_{0}, BondMM-A rejects lending.

## IV Experimental Evaluation

This paper evaluates BondMM-A333Code: <https://github.com/HarryTMa/BondMMA> focusing on effectiveness (do rates match market rates?) and stability (is net equity stable?).

Parameter setup: The pool starts with cash y0=1000y\_{0}=1000, initial rate r0=5%r\_{0}=5\%, κ=0.02\kappa=0.02, and a common r∗r^{\*} across maturities. The market curve is generated by the Cox-Ingersoll-Ross (CIR) model [[10](https://arxiv.org/html/2512.16080v1#bib.bib10)] with k=0.4,θ=0.05,σ=0.2k=0.4,\theta=0.05,\sigma=0.2. The horizon is T=1T=1 year, divided into N=100000N=100000 steps; each step launches M=1000M=1000 active trades. At each step end, set r∗r^{\*} to the previous step’s market rate. Active trades follow speculation: if BondMM-A’s rate exceeds the market rate, users lend; otherwise they borrow. Each trade’s maturity (absolute value of N​(T−t,T−t)N(T-t,T-t) with current time tt) and size (absolute value of normal distribution N​(0.72,1)N(0.72,1), expected near 11) are random. Loans and borrows maturing within TT are settled as passive trades. If active and passive trades coexist, they interleave evenly (e.g., 10001000 active and 500500 passive imply 2 active then 1 passive). Lending stops if EE falls below 99%99\% of y0y\_{0} at any time.

![Refer to caption](img/r.png)


Figure 1: Comparison of BondMM-A average rate and market rate; they nearly overlap.

![Refer to caption](img/diff.png)


Figure 2: Difference between BondMM-A average rate and the market rate.

![Refer to caption](img/std.png)


Figure 3: Standard deviation of BondMM-A rates at each time step.

![Refer to caption](img/equity.png)


Figure 4: BondMM-A net equity minus initial capital.

As Figure [1](https://arxiv.org/html/2512.16080v1#S4.F1 "Figure 1 ‣ IV Experimental Evaluation ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities") shows, BondMM-A rates closely track market rates, demonstrating effectiveness. Figures [2](https://arxiv.org/html/2512.16080v1#S4.F2 "Figure 2 ‣ IV Experimental Evaluation ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities") and [3](https://arxiv.org/html/2512.16080v1#S4.F3 "Figure 3 ‣ IV Experimental Evaluation ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities") show the rate gap is around 10−510^{-5} and the standard deviation around 10−410^{-4}—both tiny; although they rise slightly later, magnitudes stay small. BondMM-A is effective.

Figure [4](https://arxiv.org/html/2512.16080v1#S4.F4 "Figure 4 ‣ IV Experimental Evaluation ‣ Design of a Decentralized Fixed-Income Lending Automated Market Maker Protocol Supporting Arbitrary Maturities") shows net equity: BondMM-A stays about 11 above the initial 10001000, indicating strong financial stability. Because equity never dropped below 99%99\% of initial capital, no loan refusals occurred.

## V Conclusion and Outlook

This paper proposed BondMM-A, a fixed-income AMM supporting arbitrary maturities. Its design proves effective: rates align with market levels, volatility is low, net equity is stable, users gain flexibility, and LPs avoid capital fragmentation—benefiting both sides.

BondMM-A still invites optimization. Future work includes more precise dynamic parameter tuning for fast markets, richer yield-curve models to match real-world diversity, and stronger resilience to extremes. Real deployments will test performance and security at DeFi scale. Overall, BondMM-A offers a new design path for decentralized fixed income and a reference for subsequent research.

## References

* [1]
   Nakamoto S. Bitcoin: A peer-to-peer electronic cash system[J]. Satoshi Nakamoto, 2008.
* [2]
   Buterin V. A next-generation smart contract and decentralized application platform[J]. Ethereum White Paper, 2014, 1(1): 1-32.
* [3]
   Schueffel P. Defi: Decentralized finance-an introduction and overview[J]. Journal of Innovation Management, 2021, 9(3): I-XI.
* [4]
   Frangella E, Herskind L. Aave v3 technical paper[J]. 2022.
* [5]
   Leshner R, Hayes G. Compound: The Money Market Protocol—Whitepaper[J]. 2019.
* [6]
   Team M. The Maker Protocol: MakerDAO’s Mulfi-Collateral Dai (MCD) System[J]. 2019.
* [7]
   Niemerg A, Robinson D, Livnev L. YieldSpace: An automated liquidity provider for fixed yield tokens[J]. 2020.
* [8]
   Notional Finance. Notional Whitepaper[J]. 2020.
* [9]
   Tran T, Tran D A, Truong K. Financially-Stable Automated Market Making for Decentralized Fixed-Rate Lending and Trading[C]//2024 IEEE International Conference on Blockchain and Cryptocurrency (ICBC). IEEE, 2024: 353-361.
* [10]
   Cox J C, Ingersoll Jr J E, Ross S A. A theory of the term structure of interest rates[J]. Econometrica, 1985, 53(2): 385-407.