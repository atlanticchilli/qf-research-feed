---
authors:
- Alexander McFarlane
doc_id: arxiv:2510.10171v1
family_id: arxiv:2510.10171
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Toxicity Bounds for Dynamic Liquidation Incentives
url_abs: http://arxiv.org/abs/2510.10171v1
url_html: https://arxiv.org/html/2510.10171v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alexander McFarlane

(October 11, 2025)

###### Abstract

We derive a slippage-aware toxicity condition for on-chain liquidations executed via a constant-product automated market maker (CP-AMM). For a fixed (constant) liquidation incentive ii, the familiar toxicity frontier ν<1/(1+i)\nu<1/(1+i) tightens to
ν<1/(1+i)​λ\nu<1/(1+i)\lambda for a liquidity penalty factor, λ\lambda, that we derive for both the CP-AMM and a generalised form. Using a dynamic health-linked liquidation incentive i​(h)=i​(1−h)i(h)=i(1-h), we obtain a state-dependent bound and, at the liquidation boundary, a liquidity depth-only condition v<1/λ\,v<1/\lambda. This reconciles dynamic incentives with the impact of the CP-AMM price and clarifies when dynamic liquidation incentives reduce versus exacerbate spiral risk.

## 1 Introduction

Liquidations in on‑chain lending repay debt by selling collateral, typically with a bonus paid to liquidators. When sales route through AMMs, execution moves prices: the sale lowers the pool price and the borrower’s remaining collateral is re‑marked. If the loss on the remainder exceeds the debt reduction, health falls after the step; repeating such steps creates a *toxic liquidation spiral*. Protocols prefer *partial* liquidations to limit slippage, yet in the toxic regime each partial step increases LTV and drives the position toward *full* liquidation or bad debt.

We consider a borrower with collateral value cc (measured in units of the debt asset) and debt qq. Let

|  |  |  |
| --- | --- | --- |
|  | ℓ:=qc(LTV),v∈(0,1)(protocol LLTV parameter).\ell:=\frac{q}{c}\quad\text{(LTV)},\qquad v\in(0,1)\quad\text{(protocol LLTV parameter)}. |  |

for health h:=v​cq=v/ℓh:=v\,\frac{c}{q}=v/\ell. Upon a small liquidation repaying d​ada units of debt, the liquidator is entitled to a bonus i≥0i\geq 0 (possibly state dependent); a fraction (1+i)​d​a(1+i)\,da of collateral value is seized.

## 2 Slippage-aware toxicity

### 2.1 CP-AMM price impact model

We consider liquidations that are routed through a CP-AMM with reserves (x,y)(x,y) for (collateral,debt), price P=y/xP=y/x, and invariant x​y=kxy=k. The local price impact of the CP-AMM is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(ln⁡P)=d​(ln⁡y−ln⁡x)=−2​d​xxd(\ln P)\;=\;d(\ln y-\ln x)\;=\;-2\,\frac{dx}{x} |  | (1) |

The sale (1+i)​d​a(1+i)\,da of *value* in collateral implies d​x=(1+i)​d​aPdx=\frac{(1+i)\,da}{P}, and hence d​(ln⁡P)=−2​(1+i)y​d​ad(\ln P)=-\frac{2(1+i)}{y}\,da.

Let collateral c=s​Pc=sP, with ss the remaining units and PP the price. The infinitesimal change in the collateral value is d​c=P​d​s+s​d​Pdc=P\,ds+s\,dP to the first order, neglecting d​s​d​PdsdP. The seizure contributes P​d​s=−(1+i)​d​aP\,ds=-(1+i)\,da, and the price move re-marks the remainder by s​d​P=c​d​(ln⁡P)s\,dP=c\,d(\ln P). Therefore, the remaining collateral is re-marked by

|  |  |  |
| --- | --- | --- |
|  | c​d​(ln⁡P)=−2​c​(1+i)y​d​a,c\,d(\ln P)=-\frac{2c(1+i)}{y}\,da, |  |

and direct seizure removes (1+i)​d​a(1+i)\,da, so

|  |  |  |
| --- | --- | --- |
|  | d​c=−(1+i)​d​a−2​c​(1+i)y​d​a=−(1+i)​(1+2​cy)​d​a,d​q=−d​a.dc=-(1+i)\,da\;-\;\frac{2c(1+i)}{y}\,da=-(1+i)\Bigl(1+\frac{2c}{y}\Bigr)da,\qquad dq=-da. |  |

Differentiating h=v​c/qh=vc/q yields

|  |  |  |
| --- | --- | --- |
|  | d​h=vq​[d​c−cq​d​q]=vq​[−(1+i)​(1+2​cy)+cq]​d​adh\;=\;\frac{v}{q}\!\left[dc-\frac{c}{q}\,dq\right]\;=\;\frac{v}{q}\!\left[-(1+i)\!\left(1+\frac{2c}{y}\right)+\frac{c}{q}\right]\!da |  |

A liquidation is *toxic* (reduces health) iff d​h<0dh<0, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | cq<(1+i)​(1+2​cy)equivalentlyℓ>1(1+i)​λ,λ:=1+2​cy.\frac{c}{q}\;<\;(1+i)\!\left(1+\frac{2c}{y}\right)\qquad\text{equivalently}\qquad\ell\;>\;\frac{1}{(1+i)\,\lambda},\quad\lambda:=1+2\,\frac{c}{y}. |  | (2) |

In the infinite-liquidity limit y→∞y\to\infty (so λ→1\lambda\to 1), this reduces to the constant incentive frontier ℓ<1/(1+i)\ell<1/(1+i) [[1](https://arxiv.org/html/2510.10171v1#bib.bib1)].

### 2.2 Linear price impact model

Warmuz, Chaudhary and Pinna [[1](https://arxiv.org/html/2510.10171v1#bib.bib1)] propose a linear slippage model to capture execution costs in decentralised liquidations:

|  |  |  |
| --- | --- | --- |
|  | s​(x)=γ+σL​x,s(x)=\gamma+\frac{\sigma}{L}\,x, |  |

where s​(x)s(x) is the relative price discount on trade size xx, γ\gamma is the spread, σ\sigma is the slippage parameter, and LL is a liquidity scale. The execution price is 1−s​(x)1-s(x) relative to the oracle.

Linearising around small trades yields an effective per-unit price impact

|  |  |  |
| --- | --- | --- |
|  | ϕ=σL​(1−γ)\phi=\frac{\sigma}{L(1-\gamma)} |  |

This is directly analogous to Kyle’s λ\lambda in market microstructure theory [[2](https://arxiv.org/html/2510.10171v1#bib.bib2)], which measures the permanent price impact per unit of order flow. The slippage penalty factor now becomes

|  |  |  |
| --- | --- | --- |
|  | λ=1+ϕ​c\lambda=1+\phi c |  |

## 3 Removing toxicity

We choose a linear incentive function linked to health, increasing as health falls,

|  |  |  |
| --- | --- | --- |
|  | i→i​(h)=i​(1−h)=i​(1−vℓ),i\to i(h)\;=\;i\,\bigl(1-h\bigr)\;=\;i\!\left(1-\frac{v}{\ell}\right), |  |

capped at the protocol maximum ii. Substituting i​(h)i(h) into ([2](https://arxiv.org/html/2510.10171v1#S2.E2 "In 2.1 CP-AMM price impact model ‣ 2 Slippage-aware toxicity ‣ Toxicity Bounds for Dynamic Liquidation Incentives")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ>1+i​v​λ(1+i)​λ.\ell\;>\;\frac{1+i\,v\,\lambda}{(1+i)\,\lambda}. |  | (3) |

#### Boundary condition (model-agnostic).

At the LLTV boundary we have ℓ=v\ell=v (equivalently h=1h=1). Since the linear function satisfies i​(h)=i​(1−h)=0i(h)=i(1-h)=0 at h=1h=1, substituting ℓ=v\ell=v into ([3](https://arxiv.org/html/2510.10171v1#S3.E3 "In 3 Removing toxicity ‣ Toxicity Bounds for Dynamic Liquidation Incentives")) removes any dependence on ii and yields a depth-only criterion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v≤1λ\,v\;\leq\;\frac{1}{\lambda}\, |  | (4) |

This statement is *model-agnostic*: it holds for any monotone impact summarised by a penalty factor λ\lambda. For a CP-AMM, λ=1+2​c/y\lambda=1+2c/y; for the linear (Kyle) model, λ=1+ϕ​c\lambda=1+\phi c. Writing the result in terms of λ\lambda avoids unnecessary specialisation and makes clear that a greater depth (smaller λ\lambda) relaxes the admissible LLTV vv.

## 4 Discussion and limitations

Equation ([4](https://arxiv.org/html/2510.10171v1#S3.E4 "In Boundary condition (model-agnostic). ‣ 3 Removing toxicity ‣ Toxicity Bounds for Dynamic Liquidation Incentives")) isolates CP-AMM *depth* as the critical determinant of safety at the LLTV boundary: greater depth (larger yy) lowers λ\lambda and raises the allowable vv. The derivation is local (infinitesimal step, CP-AMM); integrating over large sales or routing across venues is straightforward in principle but model-specific. Nevertheless, the local condition precisely characterises when a liquidation step is health-improving versus health-worsening and reconciles dynamic incentives with price impact.

## References

* [1]

  J. Warmuz, A. Chaudhary, and D. Pinna,
  “Toxic Liquidation Spirals,”
  *arXiv preprint arXiv:2212.07306*, 2022. [Online]. Available: <https://arxiv.org/abs/2212.07306>
* [2]

  A. S. Kyle,
  “Continuous Auctions and Insider Trading,”
  *Econometrica*, vol. 53, no. 6, pp. 1315–1335, Nov. 1985. [Online]. Available: <https://www.jstor.org/stable/1913210>