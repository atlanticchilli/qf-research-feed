---
authors:
- Yao Wu
doc_id: arxiv:2511.20606v1
family_id: arxiv:2511.20606
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Limit Order Book Dynamics in Matching Markets: Microstructure, Spread, and
  Execution Slippage'
url_abs: http://arxiv.org/abs/2511.20606v1
url_html: https://arxiv.org/html/2511.20606v1
venue: arXiv q-fin
version: 1
year: 2025
---


threshold\_t = 0.80

if new\_theta < threshold\_t:

print("Result:␣Theta␣<␣T.␣Agent␣enters␣REGRET␣state.")

print("Prediction:␣High␣probability␣of␣marital␣dissatisfaction.")

else:

print("Result:␣Relationship␣absorbs␣the␣shock.")

run\_regret\_simulation()

## Appendix D A Microstructure Interpretation of the θ\theta–TT Marriage-Matching Model

This appendix provides a rigorous microstructure-based interpretation of the proposed marriage-matching model. The purpose is not metaphorical comparison but to demonstrate a structural isomorphism between:

* •

  the θ\theta–TT decision architecture in marriage markets, and
* •

  the bid–ask crossing mechanism in financial order-book markets.

This structural equivalence strengthens the theoretical validity of the model, clarifies its dynamic behavior, and explains a wide range of marriage-market phenomena.

### D.1 Structural Equivalence: θ\theta–TT as a Bid–Ask Crossing Rule

The core marriage-matching condition in the model is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Commit⇔θ=VreachVuncond>T,\text{Commit}\iff\theta=\frac{V\_{\text{reach}}}{V\_{\text{uncond}}}>T, |  | (30) |

where:

* •

  VreachV\_{\text{reach}} = achievable partner value
* •

  VuncondV\_{\text{uncond}} = unconditional ideal value
* •

  TT = subjective commit threshold (“marriage willingness index”)

This is structurally identical to the financial microstructure rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Transaction⇔Bid≥Ask.\text{Transaction}\iff\text{Bid}\geq\text{Ask}. |  | (31) |

Thus:

* •

  VreachV\_{\text{reach}} corresponds to bid side pressure,
* •

  VuncondV\_{\text{uncond}} corresponds to ask side price, and
* •

  TT functions as a limit-order threshold that must be crossed for execution.

This establishes the mathematical equivalence between marriage decisions and order-book matching.

Unconditional Value (Ask)Ask 1: V=6.20V=6.20Ask 2: V=5.80V=5.80Ask 3: V=5.60V=5.60Lowest Ask: Vuncondmax=5.40V\_{\text{uncond}}^{\max}=5.40Spread / Gap Δ​V\Delta VHighest Bid: Vreachmax=5.15V\_{\text{reach}}^{\max}=5.15Bid 2: V=4.80V=4.80Bid 3: V=4.60V=4.60Bid 4: V=4.20V=4.20Reachable Value (Bid)


Agent’s internal ceiling (Ideal Partner)

Best available suitor (Reality)
Matching Logic:Commit iff Highest BidLowest Ask>T\displaystyle\frac{\text{Highest Bid}}{\text{Lowest Ask}}>T


Figure 5: Marriage-Market Order-Book Structure. This schematic illustrates the structural equivalence between a financial order book and the LPSM. A match executes when the ratio of the highest bid to the lowest ask exceeds TT.

### D.2 Order Book Interpretation of the Preference Matrix (DF)

The agent’s internal preference Attribute Matrix (DF)—formalized in the paper as the Latent Preference State Matrix (LPSM)—can be interpreted as a multidimensional order book:

* •

  Each candidate partner is an entry analogous to a “price level”.
* •

  VreachV\_{\text{reach}} and VuncondV\_{\text{uncond}} are mapped to bid/ask pairs.
* •

  External information shocks (social media, peer marriages, class exposure) refresh the ask side.
* •

  Local experience, age, socioeconomic position anchor the bid side.

Thus, LPSM is not merely a data container but a dynamic order-book depth structure that evolves as information arrives.

### D.3 Information Shocks and Ask-Side Repricing

In financial markets, new information triggers ask-side repricing, shifting seller expectations upward. In the marriage model:

* •

  Exposure to higher-status peers,
* •

  Observing friends “marrying up”,
* •

  Encountering high-value males in professional/urban environments,
* •

  Consuming curated social-media content,

all act as informational shocks, inducing an upward shift in VuncondV\_{\text{uncond}}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vuncond←Vuncond+ϵshockV\_{\text{uncond}}\leftarrow V\_{\text{uncond}}+\epsilon\_{\text{shock}} |  | (32) |

This explains why marriage thresholds rise persistently in large cities or high-exposure environments.

Time ttVuncond​(t)V\_{\text{uncond}}(t)V0V\_{0}V1V\_{1}V2V\_{2}Shock 1: Peer MarriageShock 2: Social Media


Figure 6: Informational Shock and Upward Repricing. External shocks cause discontinuous upward jumps in the agent’s internal unconditional-value estimate.

### D.4 Liquidity, Market Depth, and Match Probability

Let LL be the local partner-market liquidity and DD be the order-book depth (population size ×\times socioeconomic variance). In microstructure terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(θ>T)=f​(L,D).P(\theta>T)=f(L,D). |  | (33) |

Low liquidity →\to low match probability →\to threshold TT grows more slowly or becomes unstable. High liquidity →\to faster crossing events →\to higher marriage rates. This explains low marriage rates in low-population regions and high competition in high-liquidity urban centers.

### D.5 Slippage: Psychological Disappointment as Execution Deviation

In financial execution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Slippage=Executed Price−Expected Price.\text{Slippage}=\text{Executed Price}-\text{Expected Price}. |  | (34) |

In marriage:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Emotional Slippage=Vuncond−Vreached.\text{Emotional Slippage}=V\_{\text{uncond}}-V\_{\text{reached}}. |  | (35) |

Large slippage predicts regret, dissatisfaction, or re-evaluation of the commit decision. This microstructure interpretation gives a quantitative explanation for post-marriage disappointment and persistent instability in relationships formed with a large Δ​V\Delta V.

Time ttRatio / ThresholdT​(t)T(t)θ​(t)\theta(t)t∗t^{\*}Crossing Eventθ>T\theta>T


Figure 7: Crossing Dynamics. Commitment occurs when the ratio θ​(t)\theta(t) crosses the decaying threshold T​(t)T(t).

### D.6 Circuit Breakers and the Role of CmaxC\_{\max}

The model proposes a maximum tolerable compensation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C∗=min⁡(Δ​V,Cmax),C^{\*}=\min(\Delta V,\ C\_{\max}), |  | (36) |

where CmaxC\_{\max} is the male agent’s “runaway threshold”—beyond which he exits the negotiation. This mirrors circuit breakers and price limits in financial markets:

* •

  They cap volatility,
* •

  Prevent runaway escalation,
* •

  Stabilize transactions.

Thus CmaxC\_{\max} is a necessary stabilizer that prevents infinite compensation bidding and pathological bargaining equilibria.

Δ​V\Delta VCCCmaxC\_{\max}Clipping Point


Figure 8: Compensation Clipping. Compensation is bounded by CmaxC\_{\max}, preventing unbounded bargaining.

### D.7 Market Orders vs. Limit Orders: Impulse Marriage Events

A market order in finance executes regardless of price, often producing slippage. The marriage analogue includes impulsive marriage decisions and sudden threshold drops. Formally:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T←T−δemotion,producing ​θ>T.T\leftarrow T-\delta\_{\text{emotion}},\quad\text{producing }\theta>T. |  | (37) |

This captures flash marriages, rebound relationships, and sudden acceptance of suboptimal partners.

### D.8 Lock-In and Stickiness

In market microstructure, investors become “locked in” due to sunk costs. The marriage equivalent occurs when exit costs (childbearing, social penalties) raise the effective threshold TT:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Texit=T+κlock-in.T\_{\text{exit}}=T+\kappa\_{\text{lock-in}}. |  | (38) |

Thus even when θ<T\theta<T, the relationship persists due to lock-in stickiness.

### D.9 Full Correspondence Table

Table [4](https://arxiv.org/html/2511.20606v1#A4.T4 "Table 4 ‣ D.9 Full Correspondence Table ‣ Appendix D A Microstructure Interpretation of the 𝜃–𝑇 Marriage-Matching Model ‣ Limit Order Book Dynamics in Matching Markets: Microstructure, Spread, and Execution Slippage") demonstrates a clean structural isomorphism between the two systems.

Table 4: Structural Isomorphism between Financial Microstructure and Marriage Matching.

| Financial Microstructure Concept | Marriage-Matching Concept |
| --- | --- |
| Bid price | VreachV\_{\text{reach}} |
| Ask price | VuncondV\_{\text{uncond}} |
| Bid–ask crossing | Commit event (θ>T\theta>T) |
| Order book depth | LPSM / DF preference matrix |
| Liquidity | Partner availability / exposure |
| Information shocks | VuncondV\_{\text{uncond}} updates from social inputs |
| Slippage | Regret (Vuncond−VreachV\_{\text{uncond}}-V\_{\text{reach}}) |
| Circuit breaker | CmaxC\_{\max} constraint |
| Market order | Impulsive marriage choice |
| Limit order | Stable threshold TT |
| Lock-in | Marriage stickiness |
| Manipulation | Family intervention / bride-price pressure |

### D.10 Summary: Why the Microstructure View Strengthens the Theory

The microstructure interpretation provides three major benefits:

1. 1.

   Structural justification. It shows that the θ\theta–TT mechanism is not ad hoc, but consistent with well-established matching mechanisms in two-sided markets.
2. 2.

   Dynamic realism. Market microstructure captures volatility, shocks, depth, and liquidity—exactly the dynamics seen in marriage markets.
3. 3.

   Predictive power. Concepts such as slippage, lock-in, liquidity droughts, and repricing give the model new explanatory dimensions for regional marriage disparities and high-gap instability.

## Appendix E Appendix E: Prior Supply–Demand Buckets

This appendix introduces a meso-level behavioral extension to the main IDP model. While the core model assumes agents optimize θ\theta based on specific values (VreachV\_{\text{reach}}), in reality, agents often estimate market scarcity using heuristic priors.

We model this perception as a set of Five Prior Buckets, representing distinct tiers of perceived supply-demand pressure. Unlike a continuous curve, these buckets create rigid pricing regimes where the “Ask Price” (expected compensation or status) jumps discontinuously.

### The Five-Bucket Structure

We categorize the male value spectrum V∈[0,100]V\in[0,100] into five heuristic tiers, each characterized by a specific Supply-Demand Pressure Ratio (ρ=DemandSupply\rho=\frac{\text{Demand}}{\text{Supply}}):

1. 1.

   Bucket 1: Invisible (V<50V<50)
     
   ρ→0\rho\to 0. The supply is perceived as infinite relative to demand. Agents in this tier are effectively invisible in the dating market; no amount of compensation is expected to yield a match.
2. 2.

   Bucket 2: Provider / “ATM” (50≤V<7050\leq V<70)
     
   ρ<1\rho<1 (Buyer’s Market). Candidates are seen as abundant substitutes. High compensation (bride price) is strictly required to compensate for the utility gap.
3. 3.

   Bucket 3: Match (70≤V<8570\leq V<85)
     
   ρ≈1\rho\approx 1 (Balanced). The “Tradeable Zone.” Candidates are perceived as acceptable partners where mutual exchange occurs without excessive unilateral compensation.
4. 4.

   Bucket 4: Premium (85≤V<9585\leq V<95)
     
   ρ>1\rho>1 (Seller’s Market). Scarcity begins to bite. Agents here hold significant pricing power, often demanding “reverse compensation” (e.g., dowry or emotional subservience).
5. 5.

   Bucket 5: Idol / CEO (V≥95V\geq 95)
     
   ρ→∞\rho\to\infty (Monopoly). The “Unconditional Max” tier. Demand is absolute; supply is singular. The ask price becomes infinite (in terms of loyalty), yet financial compensation drops to zero.

0507085951001. Invisible(ρ≈0\rho\approx 0)2. Provider(Buyer’s Mkt)3. Match(Balanced)4. Premium(Seller’s Mkt)5. Idol(Monopoly)Male Intrinsic Value (VV)Subjective Perception / Ask PriceContinuous Reality (VV)


Figure 9: The Five-Tier Prior Bucket Model. Agents discretize the continuous value spectrum into five tiers based on Supply-Demand Pressure (ρ\rho). Pricing is rigid within each bucket, jumping discontinuously at heuristic thresholds.

## Appendix F Appendix F: The Gini Conical Structure

This appendix provides the macro-structural geometric explanation for the liquidity constraints observed in the main model. While Appendix E deals with subjective perception (behavioral heuristics), this section derives the objective physical constraints of the matching market from the societal distribution of wealth and status.

We model the socio-economic hierarchy not as a linear ladder, but as a rotational solid derived from the derivative of the societal Lorenz curve (the Gini distribution). Let g​(h)g(h) be the population density at height hh. The market structure can be visualized as a cone where the radius r​(h)∝g​(h)r(h)\propto\sqrt{g(h)}.

Asset Valuation / Status (hh)Base Liquidity DensityVmax=1V\_{\text{max}}=1Density Profiler​(h)=g​(h)r(h)=\sqrt{g(h)}(Derived from Gini)
Liquidity Threshold TTCurrent Tier (h0h\_{0})Reachable Volume(Scarce Candidate Set)Geometric Liquidity Constraint:V​o​l=∫h01π​[r​(t)]2​𝑑t\displaystyle Vol=\int\_{h\_{0}}^{1}\pi[r(t)]^{2}\,dt


Figure 10: The Gini Conical Structure. The hierarchy is modeled as a volume. As an agent’s execution threshold TT (orange line) rises linearly, the available volume of counterparties (shaded region) decays geometrically. This proves that high-tier liquidity droughts are a mathematical necessity of the density gradient.

This geometric isomorphism reveals a critical insight: a linear increase in the acceptance threshold TT results in a super-linear (cubic or exponential) collapse in the reachable partner volume. Thus, the difficulty of “marrying up” is not merely a friction of preferences but a geometric liquidity constraint imposed by the inequality structure of the population.