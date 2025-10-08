---
authors:
- Vasily Tolstikov
- Marcus Wentz
- Joseph Schiarizzi
- Derek Ding
doc_id: arxiv:2510.05428v1
family_id: arxiv:2510.05428
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Concentrated N-dimensional AMM with Polar Coordinates in Rust
url_abs: http://arxiv.org/abs/2510.05428v1
url_html: https://arxiv.org/html/2510.05428v1
venue: arXiv q-fin
version: 1
year: 2025
---


## 1 INTRODUCTION

00footnotetext: Acknowledgments: special thanks to Dan Robinson for liquidity fingerprint discussions and Ciamac Moallemi for explaining stablecoin pool liquidity skew phenomenon.

There exist two schools of thought for liquidity concentration in Automated Market Makers (AMM). One approach involves the specification of a custom curve with parameters controlling the shape of how liquidity is distributed [[1](https://arxiv.org/html/2510.05428v1#bib.bib1)] such as Curve [[2](https://arxiv.org/html/2510.05428v1#bib.bib2)], CavalRe [[3](https://arxiv.org/html/2510.05428v1#bib.bib3)], and Eulerswap [[4](https://arxiv.org/html/2510.05428v1#bib.bib4)]. The second approach consists in giving the Liquidity Provider (LP) the freedom to select a discrete price range where liquidity can be concentrated such as Uniswap v3 [[5](https://arxiv.org/html/2510.05428v1#bib.bib5)] and Orbital AMM [[6](https://arxiv.org/html/2510.05428v1#bib.bib6)]. By combining both we herein focus on an n-dimensional AMM for stablecoins where we:

(1) Explain the Orbswap invariant.

(2) Explain limitations of symmetric ticks and propose a mechanism to shift liquidity.

(3) Demonstrate swap function in polar coordinates.

(4) Concentrate ticks in polar coordinates.

(5) Highlight the fragility of multi-dimensional stablecoin pools and show a path for mitigation.

(6) Introduce multi-modal liquidity fingerprints.

## 2 Orbswap Invariant

Uniswap v2 introduced a continuous uniform liquidity distribution [[1](https://arxiv.org/html/2510.05428v1#bib.bib1)] allowing for the trading of a token in the price range of zero to infinity. Yet prices are not infinite nor bound by the zero barrier, to address part of this problem Uniswap v3 was introduced to allow for the sharp concentration of liquidity based on an LP’s preferred viewpoint on the range of price movement between zero and infinity [[5](https://arxiv.org/html/2510.05428v1#bib.bib5)]. To achieve a softer concentration of liquidity we can adjust the Uniswap v3 AMM invariant equation below by allowing the curve to fold in on itself. A side effect of it is the ability to access negative prices [[7](https://arxiv.org/html/2510.05428v1#bib.bib7)] which can be disabled for our stablecoin use case.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1n(xi−l)2=l2\sum\_{i=1}^{n}(x\_{i}-l)^{2}=l^{2} |  | (1) |

where l=2+2l=2+\sqrt{2} is an offset parameter to pin liquidity to the axes. The liquidity fingerprint of this Concentrated Circular Market Maker (CCMM) is derived in Appendix B and can be extended to create a Concentrated Super-Elliptical Market Maker (CSEMM) [[8](https://arxiv.org/html/2510.05428v1#bib.bib8)] to further widen/narrow and skew the liquidity allocation with the invariant becoming:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1n|xiαi−1|η​(αi)=1\sum\_{i=1}^{n}\left|\frac{x\_{i}}{\alpha\_{i}}-1\right|^{\eta(\alpha\_{i})}=1 |  | (2) |

where η​(x)=l​n​(2)l​n​(xx−1)\eta(x)=\frac{ln(2)}{ln(\frac{x}{x-1})}. Parameters αi\alpha\_{i} allow for the skew of liquidity in the tails. By setting αi\alpha\_{i} to the same number, decreasing their values towards two one can approach the liquidity concentration of a Constant Sum Market Maker (CSMM) x+y=1x+y=1, by decreasing further to αi=−1\alpha\_{i}=-1 one can recover the Constant Product Market Maker (CPMM) x∗y=1x\*y=1, by widening αi\alpha\_{i} towards infinity one increases the tails of the distribution until it converges to the Logarithmic Market Scoring Rule (LMSR) invariant [[1](https://arxiv.org/html/2510.05428v1#bib.bib1)]. At αi=2+2\alpha\_{i}=2+\sqrt{2} we get the CCMM from equation (1) which is the version that we have launched on Arbitrum and expanded the stablecoin pool dimensions n=6n=6 on our github [[9](https://arxiv.org/html/2510.05428v1#bib.bib9)].

### 2.1 Liquidity Limitations with Circles

The Orbital AMM [[5](https://arxiv.org/html/2510.05428v1#bib.bib5)] provides symmetric ticks, yet liquidity can be demonstrated to be asymmetric in stable pools [Figure [1](https://arxiv.org/html/2510.05428v1#S5.F1 "Figure 1 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")], making it capital inefficient to not adjust liquidity. We can construct shifts in the liquidity fingerprint while concentrating liquidity at a specific price peak cc by modifying the circular invariant as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (x−l)β+(yc−l)β=lβ\left(x-l\right)^{\beta}+\left(\frac{y}{c}-l\right)^{\beta}=l^{\beta} |  | (3) |

where parameter β=2\beta=2 for an elliptical case, which is shown to have computational benefits [[10](https://arxiv.org/html/2510.05428v1#bib.bib10)], and is available in desmos [[11](https://arxiv.org/html/2510.05428v1#bib.bib11)]. It can be extended to 1<β<21<\beta<2 for further concentrating liquidity around a particular price. Each β\beta value corresponds to a specific center-curve C​(x)C(x) for the superellipse

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(x)=11−(1−(x−1x)β)1βC(x)=\frac{1}{1-(1-(\frac{x-1}{x})^{\beta})^{\frac{1}{\beta}}} |  | (4) |

along which a scale invariant trading function can be constructed and along which its LP payoff, given via Fenchel conjugacy [[12](https://arxiv.org/html/2510.05428v1#bib.bib12)], and its liquidity fingerprint, explained in appendix 3.1, shifts [Figure [2](https://arxiv.org/html/2510.05428v1#S5.F2 "Figure 2 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")].

### 2.2 Polar Swap Function

Unlike traditional AMM swap functions that operate in the Cartesian plane by moving along a curve, a side effect of circular invariants is that it allows one to rotate using polar coordinates [[13](https://arxiv.org/html/2510.05428v1#bib.bib13)] from a focal point with distance ll [Figure [3](https://arxiv.org/html/2510.05428v1#S5.F3 "Figure 3 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")]. This rotation involves a particular step where the quantity of one stablecoin Δx\Delta\_{x} is exchanged for the quantity of a second stablecoin Δy\Delta\_{y} while passing through a trigonometric conversion outlined in Rust in Appendix 3.3.

### 2.3 Ticks in Polar Coordinates

The additional step of trigonometric conversion for Orbswap can be used to construct ticks [[5](https://arxiv.org/html/2510.05428v1#bib.bib5)] in the polar coordinate system based on a particular granularity level [Figure [3](https://arxiv.org/html/2510.05428v1#S5.F3 "Figure 3 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust"), 4B]. For the sake of simplicity, if our pool initiation consists of n-tokens all priced initially at $1.00, then the polar tick ϕ\phi sits at 45 degrees and has the ability to range from 0 to 90 degrees with the price-to-angle conversion formula being:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ=90P​r​i​c​e+1\phi=\frac{90}{Price+1} |  | (5) |

As the swap function passes through a particular tick, it can adjust parameter LL to change the price impact. Such a discretization approach, when unwrapped [Figure [5](https://arxiv.org/html/2510.05428v1#S5.F5 "Figure 5 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")D], happens to be an excellent fit for stable pairs given that ticks are more granular at the body of a price distribution while also being able to capture fat tails, allowing for more accurate capture of price diffusion [Figure [4](https://arxiv.org/html/2510.05428v1#S5.F4 "Figure 4 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")].

### 2.4 Risk of N-dimensional Pools

In the event of a permanent stablecoin depeg we witness significant divergence loss for the LP and an accumulation of the unwanted depegged stablecoin. For assets with n-dimensional pools, the first n>2n>2 stablecoin example being Curve’s Tricrypto pool (USDC,USDT,DAI), one can historically recall the event of Silicon Valley Bank in 2023 [[14](https://arxiv.org/html/2510.05428v1#bib.bib14)] where a bankrun forced USDC to $0.850.85, resulting in a serious run on the pool and a flight to USDT. The LP of this n=3n=3 pool, in the event of a total depeg would have suffered significant divergence loss had the peg not returned. Extending this concept to nn stablecoin pools towards infinity poses a significant problem, considering it is building in fragility [[15](https://arxiv.org/html/2510.05428v1#bib.bib15)] of assets that are inherently fat tailed [Figure [5](https://arxiv.org/html/2510.05428v1#S5.F5 "Figure 5 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")] and in some cases may even anti-correlate as we’ve seen with USDC and USDT during the bank run.

To counter the fragility of adding more stablecoins to a pool, we suggest not exceeding such high dimensions, but if one wishes to expand to n>3n>3 tokens and include stablecoins with a higher chance of depegging, then LPs could consider hedging their position by constructing a synthetic binary payoff directly with ticks.

The way to replicate the equivalent of a prediction market in the event of a depeg in an N-dimensional pool is by constructing one LP position out of range by one degree and a second LP position that one shorts right below it [Figure [6](https://arxiv.org/html/2510.05428v1#S5.F6 "Figure 6 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")] via a vertical spread [[16](https://arxiv.org/html/2510.05428v1#bib.bib16)]. This gives us a good approximation for depeg insurance by mimicking a prediction market for a depeg directly inside of Orbswap by utilizing the existing unused LP positions.

## 3 Appendix

### 3.1 Orbswap Liquidity Fingerprint

The liquidity fingerprint can be viewed as the second derivative with respect to the square root of the price [[1](https://arxiv.org/html/2510.05428v1#bib.bib1)].
In Cartesian tick space tt we get the following distribution of liquidity for the CCMM:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LC​C​M​M​(t)=2​l​e3​t2(1+e2​t)32L\_{CCMM}(t)=\frac{2le^{\frac{3t}{2}}}{\left(1+e^{2t}\right)^{\frac{3}{2}}} |  | (6) |

which can also be seen in [Figure [2](https://arxiv.org/html/2510.05428v1#S5.F2 "Figure 2 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")D] for the $​1\mathdollar 1 price peak. The elliptical case has a similar liquidity fingerprint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LC​E​M​M​(t)=2​c2​l​e32​t(c2+e2​t)32L\_{CEMM}\left(t\right)=\frac{2c^{2}le^{\frac{3}{2}t}}{\left(c^{2}+e^{2t}\right)^{\frac{3}{2}}} |  | (7) |

The superelliptical case has only a closed-form solution when α=β\alpha=\beta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LC​S​E​M​M​(t)=2​αη−1⋅eη+12​(η−1)​(t−ln⁡(sysx))(1+eηη−1​(t−ln⁡(sysx)))η+1ηL\_{CSEMM}\left(t\right)=\frac{2\alpha}{\eta-1}\cdot\frac{e^{\frac{\eta+1}{2\left(\eta-1\right)}\left(t-\ln\left(\frac{s\_{y}}{s\_{x}}\right)\right)}}{\left(1+e^{\frac{\eta}{\eta-1}\left(t-\ln\left(\frac{s\_{y}}{s\_{x}}\right)\right)}\right)^{\frac{\eta+1}{\eta}}} |  | (8) |

The value function of an LP payoff is given by the Legendre transform with the Greeks for Delta=Δ\Delta, Gamma=Γ\Gamma, and Theta=Θ\Theta being available in desmos [[17](https://arxiv.org/html/2510.05428v1#bib.bib17)].

### 3.2 Cartesian Swap Functions

By solving for y in equation (1) for the lower half of the CCMM we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=−2​l​x−x2+ly=-\sqrt{2lx-x^{2}}+l |  | (9) |

Adding Δx\Delta\_{x} and Δy\Delta\_{y} into our swap function to get the quantity of yy for quantity xx:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δy=−2​l​(x−Δx)−(x−Δx)2+l−y\Delta\_{y}=-\sqrt{2l(x-\Delta\_{x})-(x-\Delta\_{x})^{2}}+l-y |  | (10) |

to solve for Δx\Delta\_{x} simply rearrange the variables given the function’s symmetric nature.

For n=2 CSEMM the swap function becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=−αy​((1−|xαx−1|ln⁡(2)ln⁡(αxαx−1))ln⁡(αyαy−1)ln⁡(2)−1)y=-\alpha\_{y}\left(\left(1-\left|\frac{x}{\alpha\_{x}}-1\right|^{\frac{\ln\left(2\right)}{\ln\left(\frac{\alpha\_{x}}{\alpha\_{x}-1}\right)}}\right)^{\frac{\ln\left(\frac{\alpha\_{y}}{\alpha\_{y}-1}\right)}{\ln\left(2\right)}}-1\right) |  | (11) |

Adding Δx\Delta\_{x} and Δy\Delta\_{y} into our swap function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δy=−αy​((1−|x+Δxαx−1|η​(αx))1η​(αy)−1)−y\Delta\_{y}=-\alpha\_{y}\left(\left(1-\left|\frac{x+\Delta\_{x}}{\alpha\_{x}}-1\right|^{\eta(\alpha\_{x})}\right)^{\frac{1}{\eta(\alpha\_{y})}}-1\right)-y |  | (12) |

For Δx\Delta\_{x} due to the asymmetric nature of the superellipse our swap function order for u​(x)u(x) is reversed:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δx=−αy​((1−|y+Δyαx−1|η​(αy))1η​(αx)−1)−x\Delta\_{x}=-\alpha\_{y}\left(\left(1-\left|\frac{y+\Delta\_{y}}{\alpha\_{x}}-1\right|^{\eta(\alpha\_{y})}\right)^{\frac{1}{\eta(\alpha\_{x})}}-1\right)-x |  | (13) |

### 3.3 Polar Swap in Rust Arbitrum Stylus

Rust WASM smart contracts from Arbitrum Stylus can help make Solidity contracts more expressive. For example, math in Solidity can be limited. In contrast, Rust has more math function support with its standard library, and has a large Rust cargo collection of math libraries for even more complex math operations. Some of these Rust crate libraries can even be used where the Rust standard library might need to be disabled for compiling WASM binaries.

#### 3.3.1 Remark 1

It is recommended to used fixed point math libraries, since floating point calculations can be non deterministic based on the hardware the math is computed on.

#### 3.3.2 Remark 2

The Rust math function below uses
decimal values that aren’t scaled. For EVM production deployments, these values should be scaled up in a similar way to how Solidity library prb-math uses WAD values to represent decimal values since the EVM currently only supports integer values.

Rust math function related to the swap function with Line referring to equations outlined in desmos [[18](https://arxiv.org/html/2510.05428v1#bib.bib18)]:

[⬇](data:text/plain;base64,CmZuIGdldF9kZWx0YV95X2Z1bmN0aW9uKCkgLT4gZjY0IHsKXHBhcmxldCBjb25zdGFudF9sOiBmNjQgPSBnZXRfY29uc3RhbnRfbCgpOyAvLyBMaW5lIDEKbGV0IGxfc2NhbGVkOiBmNjQgPSBjb25zdGFudF9sICogMTAwMDAuMDsKcHJpbnRsbiEoImxfc2NhbGVkOiB7fSIsIGxfc2NhbGVkKTsKXHBhcmxldCByYWRpYW5zXzQ1X2RlZyA9IHN0ZDo6ZjY0Ojpjb25zdHM6OkZSQUNfUElfNDsKbGV0IHJhZGlhbnNfMTM1X2RlZzogZjY0ID0gMy4wICogcmFkaWFuc180NV9kZWc7CmxldCBjb3NfZXhwcmVzc2lvbiA9IHJhZGlhbnNfMTM1X2RlZy5jb3MoKTsKbGV0IGxfY29zX2V4cHJlc3Npb24gPSBsX3NjYWxlZCAqIGNvc19leHByZXNzaW9uOwpccGFybGV0IHhfaW46IGY2NCA9IDEuMDsgLy8gTGluZSA2CmxldCByYWRpYW5zXzQ1X2RlZyA9IHN0ZDo6ZjY0Ojpjb25zdHM6OkZSQUNfUElfNDsKbGV0IHJhZGlhbnNfMTM1X2RlZzogZjY0ID0gMy4wICogcmFkaWFuc180NV9kZWc7CmxldCBzaW5fZXhwcmVzc2lvbiA9IHJhZGlhbnNfMTM1X2RlZy5zaW4oKTsKbGV0IGxfc2luX2V4cHJlc3Npb24gPSBsX3NjYWxlZCAqIHNpbl9leHByZXNzaW9uOwpsZXQgbnVtZXJhdG9yID0gbF9zaW5fZXhwcmVzc2lvbiAtIHhfaW47CmxldCByYXRpbzogZjY0ID0gbnVtZXJhdG9yIC8gbF9zY2FsZWQ7CmxldCByYXRpb19zcXVhcmVkID0gZjY0Ojpwb3dmKHJhdGlvLCAyLjApOwpsZXQgcmFkaWNhbmQ6IGY2NCA9IDEuMCAtIHJhdGlvX3NxdWFyZWQ7CmxldCBzcXVhcmVfcm9vdCA9IHJhZGljYW5kLnNxcnQoKTsKbGV0IGxfc3F1YXJlX3Jvb3QgPSBsX3NjYWxlZCAqIHNxdWFyZV9yb290OwpccGFybGV0IG91dHB1dDogZjY0ID0gbF9zcXVhcmVfcm9vdCArIGxfY29zX2V4cHJlc3Npb247ClxwYXJyZXR1cm4gb3V0cHV0OyAvLyAwLjk5OTk1ODU4MDM2MzsgLy8gTGluZSA3Cn0K)

fn get\_delta\_y\_function() -> f64 {

\parlet constant\_l: f64 = get\_constant\_l(); // Line 1

let l\_scaled: f64 = constant\_l \* 10000.0;

println!(”l\_scaled: {}”, l\_scaled);

\parlet radians\_45\_deg = std::f64::consts::FRAC\_PI\_4;

let radians\_135\_deg: f64 = 3.0 \* radians\_45\_deg;

let cos\_expression = radians\_135\_deg.cos();

let l\_cos\_expression = l\_scaled \* cos\_expression;

\parlet x\_in: f64 = 1.0; // Line 6

let radians\_45\_deg = std::f64::consts::FRAC\_PI\_4;

let radians\_135\_deg: f64 = 3.0 \* radians\_45\_deg;

let sin\_expression = radians\_135\_deg.sin();

let l\_sin\_expression = l\_scaled \* sin\_expression;

let numerator = l\_sin\_expression - x\_in;

let ratio: f64 = numerator / l\_scaled;

let ratio\_squared = f64::powf(ratio, 2.0);

let radicand: f64 = 1.0 - ratio\_squared;

let square\_root = radicand.sqrt();

let l\_square\_root = l\_scaled \* square\_root;

\parlet output: f64 = l\_square\_root + l\_cos\_expression;

\parreturn output; // 0.999958580363; // Line 7

}

## 4 Further Research

Polar coordinates allow us to add a sinusoidal wave onto the circular invariant. This gives us the ability to construct multimodal liquidity fingerprints with the following equation where α=[4,…​∞)\alpha=[4,...\infty) in intervals of 22 and β=α2\beta=\alpha^{2}

|  |  |  |  |
| --- | --- | --- | --- |
|  | r​(θ)=L1−12sin(αθ)2β.r\left(\theta\right)=\frac{L}{\sqrt[\beta]{1-\frac{1}{2}\sin\left(\alpha\theta\right)^{2}}}. |  | (14) |

At α=4\alpha=4 our trading function resembles Curve [[2](https://arxiv.org/html/2510.05428v1#bib.bib2)]. At α=6\alpha=6 it resembles a bimodal liquidity fingerprint the middle part of which can be compared to convex liquidity - liquidity that grows as we move away from the current price [[19](https://arxiv.org/html/2510.05428v1#bib.bib19)]. We would like to particularly draw attention to α=8\alpha=8 where we have a trimodal liquidity fingerprint which can be very useful for capturing dynamics of collateralized debt position (CDP) stablecoin such as DAI. We can see empirically that such stablecoins exhibit sinusoidal peaks at 0, 1%1\%, and −1%-1\% when minting and burning are activated [Figure [7](https://arxiv.org/html/2510.05428v1#S5.F7 "Figure 7 ‣ Concentrated N-dimensional AMM with Polar Coordinates in Rust")]. We provide an interactive model for further research for such CDP stablecoins in desmos [[20](https://arxiv.org/html/2510.05428v1#bib.bib20)].

## 5 Disclaimer

This paper is for general information purposes only. It does not constitute investment advice or a recommendation or solicitation to buy or sell any investment and should not be used in the evaluation of the merits of making any investment decision. It should not be relied upon for accounting, legal or tax advice or investment recommendations.

## References

* [1]

  Robinson, D: Uniswap v3 - The Universal AMM, <https://www.paradigm.xyz/2021/06/uniswap-v3-the-universal-amm>, last accessed 2025/09/19
* [2]

  Egorov, M: StableSwap - efficient mechanism for Stablecoin
  liquidity, <https://docs.curve.finance/assets/pdf/whitepaper_stableswap.pdf>, last accessed 2025/09/19
* [3]

  Forgy, E., Lau, L.: A Family of Multi-Asset Automated Market Makers, <https://arxiv.org/abs/2111.08115>, last accessed 2025/09/19
* [4]

  Euler Labs: EulerSwap White Paper, <https://github.com/euler-xyz/euler-swap/blob/master/docs/whitepaper/EulerSwap_White_Paper.pdf>, last accessed 2025/09/19
* [5]

  Adams, H et al: Uniswap v3 Whitepaper, <https://uniswap.org/whitepaper-v3.pdf>, last accessed 2025/09/19
* [6]

  White, D., Robinson, D., Moallemi, C.: Orbital, <https://www.paradigm.xyz/2025/06/orbital>, last accessed 2025/09/19
* [7]

  v-for-vasya: Negative Price AMM, <https://ethresear.ch/t/negative-price-amm/17833>, last accessed 2025/09/19
* [8]

  Tolstikov, V.: Concentrated Superelliptical Market Maker, <https://arxiv.org/abs/2410.13265>, last accessed 2025/09/19
* [9]

  Schiarizzi, J. Tolstikov, V.: Orbswap, <https://github.com/cupOJoseph/orbswap>, last accessed 2025/09/19
* [10]

  Wang, Y.: Automated Market Makers for Decentralized Finance (DeFi), <https://arxiv.org/abs/2009.01676>, last accessed 2025/09/19
* [11]

  Tolstikov, V.: Desmos - Elliptical Orbswap VT, <https://www.desmos.com/calculator/ndckdhzbc5>, last accessed 2025/09/19
* [12]

  Angeris, G., Evans, A., Chitra, T.: Replicating Market Makers, <https://arxiv.org/pdf/2103.14769>, last accessed 2025/09/19
* [13]

  Tolstikov, V.: Desmos - Orbswap beta2 c1 VT, <https://www.desmos.com/calculator/pmeynkqexn>, last accessed 2025/09/19
* [14]

  University of Washington School of Law: The Silicon Valley Bank Collapse <https://www.law.uw.edu/news-events/news/2023/svb-collapse>, last accessed 2025/09/19
* [15]

  Taleb, N.: Youtube - MINI LECTURE 14 A First Course on Fragility, Convexity, and Antifragility, <https://www.youtube.com/watch?v=ovEPIQR65hc>, last accessed 2025/09/19
* [16]

  Lambert, G., Kristensen, J.: Panoptic: the perpetual, oracle-free options protocol, <https://arxiv.org/abs/2204.14232>, last accessed 2025/09/19
* [17]

  Tolstikov, V.: Desmos - CCMM and CSEMM, <https://www.desmos.com/calculator/wy74cucie0>, last accessed 2025/09/19
* [18]

  Tolstikov, V.: Desmos - Swap in Polar Coordinates VT, <https://www.desmos.com/calculator/xxeeuzbvvp>, last accessed 2025/09/19
* [19]

  Wentz, M., Tolstikov, V.: Curvy - Custom Curve, <https://ethglobal.com/showcase/curvy-vjk7e>, last accessed 2025/09/19
* [20]

  Tolstikov, V.: Desmos - Polarswap with Multimodal Liquidity VT, <https://www.desmos.com/calculator/vrsexjue5o>, last accessed 2025/09/19

![Refer to caption](F1_asymmetry.png)

Figure 1:  1A: Price behavior of USDC/USDT on Uniswap v3 since inception. 1B: Notice the asymmetric skew of the price movement, indicating that providing liquidity to the left of the price makes more sense rather than the right. A personal discussion with Ciamac Moallemi led to the conclusion that the reason for this skew is the redemption fee barrier imposed on one of the stablecoin issuers, which created an incentive to swap the stablecoin on Uniswap into another token without the redemption fee. 1C and 1D in log-log hint at fat-tailed behavior of stablecoin pools. Data retrieved from [Dune Analytics](https://www.dune.com) from the period since the pool’s inception on Uniswap v3 until 2025/06/27.



![Refer to caption](F2_ellipse.png)

Figure 2:  2A: The Center-curve in red allows us to shift the center of our superellipse while retaining the trading function’s scale invariance as demonstrated by having them cross through coordinate (1,1). 2B: The LP Payoff is given to us via the Legendre Transform. 2C: We can think of liquidity living in polar tick space where each angle represents a particular level of liquidity. 2D: If we were to unwrap the liquidity, we would observe that most of the polar ticks are concentrated at the center of the body of a symmetric liquidity fingerprint, making such a polar discretization a very good building block for liquidity concentration with ticks.



![Refer to caption](F3_polar_swap.png)

Figure 3:  L​P1LP\_{1} provides liquidity in the polar range of [0​…​90][0...90], corresponding to a price range of [0​…​∞)[0...\infty), while L​P2LP\_{2} provide liquidity between the angle range [40​…​55][40...55]. The swap function from the price PaP\_{a} of $1 to PbP\_{b} of $0.80 can move via polar coordinates. The red contour of the liquidity distribution is where the swap function resides, which expands and contracts based on the amount of liquidity different LPs have concentrated along each polar tick range. To convert from tick angle to price the formula is reverted: 90ϕ−1=P\frac{90}{\phi}-1=P.



![Refer to caption](F4_polar_integration.png)

Figure 4:  4A: Inaccurate capture at the body of the heavy tailed distribution as well as the need for increasing Riemann partitions required to capture the tail with each LP position costing more in gas. 4B: Integration of partitions along polar ticks results in both the body being accurately captured while also capturing the heavy tail.



![Refer to caption](F5_img_USDC_USDT_TAIL.png)

Figure 5:  We have examined the top three most populated and oldest mainnet stablecoin pools on Uniswap v3 retrieved from [Dune Analytics](https://www.dune.com) since inception in rank-frequency plots and found the same pattern for all of them. We have a fat-tail with the power law statistically preferred over the stretched exponential. Its alpha exceeds that of the Cauchy distribution (α<2\alpha<2), making the act of stacking multiple such assets into one pool grow in fragility.



![Refer to caption](F6_prediction_market1.png)

Figure 6:  6A: Constructing an LP position along a particular degree out of range give us a concave payoff resembling a Uniswap v3 position. 6B: By borrowing, unwrapping, and shorting an LP position below our long position we can have a convex payoff. 6C: combining both positions gives us a binary-like option payoff resembling prediction markets.



![Refer to caption](F7_dai_wave.png)

Figure 7: 7A: DAI-USD Log-Y price dynamics on a Centralized Exchange (CEX). 7B: Log-Y histogram and fits of
Levy, Student-T and Pareto. For stablecoins, the Pareto distribution provides the
better fit while the Student-T, focusing on outliers, fails to capture the body
giving an inaccurate read. 7C: Log-Log histogram of the tails.
Note the histogram bump at ±​1%\textpm 1\% has a unique sinusoidal bump. 7D: The rank-frequency plot allows us to look more closely at the outliers. There is a unique step function
at the low returns range and a sinusoidal ripple in the tail starting at 1%1\%. 7E: We select the earliest minimum xm​i​nx\_{min} cutoff value of the Kolmogorov-Smirnov Divergence visualized as dashed verticals in order to minimize our error rate σ\sigma. 7F: We map the power law spectrum showing the fatness of the tail and see the sinusoidal bump prior to xm​i​nx\_{min} = ±​1%\textpm 1\%. Data retrieved from [polygon.io](https://www.polygon.io) for CEX data for the price of DAI from the period 2022/07/10 until 2025/01/29 at a one minute time interval and processed in Python.