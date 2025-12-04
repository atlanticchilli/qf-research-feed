---
authors:
- Amit Kumar Jha
doc_id: arxiv:2512.03123v1
family_id: arxiv:2512.03123
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage:
  Theory and Empirical Implications'
url_abs: http://arxiv.org/abs/2512.03123v1
url_html: https://arxiv.org/html/2512.03123v1
venue: arXiv q-fin
version: 1
year: 2025
---


Amit Kumar Jha
Quantitative Risk Modelling, UBS jha.8@iitj.ac.in

(December 2, 2025)

###### Abstract

This paper develops a comprehensive theoretical framework that imports concepts from stochastic thermodynamics to model price impact and characterize the feasibility of round-trip arbitrage in financial markets. A trading cycle is treated as a non-equilibrium thermodynamic process, where price impact represents dissipative work and market noise plays the role of thermal fluctuations. The paper proves a *Financial Second Law*: under general convex impact functionals, any round-trip trading strategy yields non-positive expected profit. This structural constraint is complemented by a fluctuation theorem that bounds the probability of profitable cycles in terms of dissipated work and market volatility. The framework introduces a statistical ensemble of trading strategies governed by a Gibbs measure, leading to a free energy decomposition that connects expected cost, strategy entropy, and a market *temperature* parameter. The framework provides rigorous, testable inequalities linking microstructural impact to macroscopic no-arbitrage conditions, offering a novel physics-inspired perspective on market efficiency. The paper derives explicit analytical results for prototypical trading strategies and discusses empirical validation protocols.

Keywords: Price impact, stochastic thermodynamics, fluctuation theorem, no-arbitrage, convex analysis, market microstructure, optimal execution.

## 1 Introduction

The modeling of price impact—the feedback of trading activity on asset prices—stands as a cornerstone of modern market microstructure theory. Classical approaches, ranging from the seminal Almgren-Chriss framework [[AC01](https://arxiv.org/html/2512.03123v1#bib.bibx2), [Alm03](https://arxiv.org/html/2512.03123v1#bib.bibx4)] to propagator models [[BMP04](https://arxiv.org/html/2512.03123v1#bib.bibx9), [BFL09](https://arxiv.org/html/2512.03123v1#bib.bibx6)], typically specify impact functions *ad hoc* or calibrate them to data without imposing structural constraints from first principles. This paper asks a more fundamental question: *What structural properties must an impact functional satisfy to preclude systematic arbitrage from closed trading cycles?*

This paper proposes that this question finds a natural answer in the language of stochastic thermodynamics [[Sei12](https://arxiv.org/html/2512.03123v1#bib.bibx27), [Jar97](https://arxiv.org/html/2512.03123v1#bib.bibx20), [Cro99](https://arxiv.org/html/2512.03123v1#bib.bibx11)]. In this analogy, which this paper makes mathematically precise:

* •

  A *trading round trip* (buying and selling to return to zero inventory) is a thermodynamic *cycle*.
* •

  The deterministic loss from impact is *dissipated work*—irreversible energy loss.
* •

  Market noise contributes *heat*—unpredictable fluctuations in profit and loss (P&L).

The impossibility of a perpetual motion machine translates directly into a *Financial Second Law*: no round-trip strategy can generate positive expected P&L [[Gat10](https://arxiv.org/html/2512.03123v1#bib.bibx15)].
. This principle imposes sharp convexity and growth constraints on the impact functional, which this paper characterizes completely using tools from convex analysis [[Roc70](https://arxiv.org/html/2512.03123v1#bib.bibx26)].

Beyond expectations, modern thermodynamics quantifies the *probability* of fleeting violations of the Second Law through fluctuation theorems [[Jar97](https://arxiv.org/html/2512.03123v1#bib.bibx20), [Cro99](https://arxiv.org/html/2512.03123v1#bib.bibx11), [Sei12](https://arxiv.org/html/2512.03123v1#bib.bibx27)].This paper derives a financial analogue: the probability that a round trip yields positive profit is exponentially suppressed in the ratio of dissipated work to market volatility [[Cro99](https://arxiv.org/html/2512.03123v1#bib.bibx11)]. This inequality is model-independent, depending only on the convexity of the impact functional and the path-wise properties of the strategy.

Finally, this paper embeds this single-agent picture into a statistical ensemble. Treating admissible strategies as microstates and their dissipated work as energy, the framework defines a Gibbs measure parameterized by an inverse “market temperature” β\beta [[DZ10](https://arxiv.org/html/2512.03123v1#bib.bibx12)]. The resulting free energy decomposition connects expected execution cost, strategy diversity (entropy), and risk appetite. This provides a microfoundation for the emergence of convex impact from competitive equilibrium among many agents.

The contributions of this paper are:

1. 1.

   A rigorous mapping between price impact models and stochastic thermodynamics (Section [3](https://arxiv.org/html/2512.03123v1#S3 "3 Model Setup and Thermodynamic Mapping ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")), building on the work of Kyle [[Kyl85](https://arxiv.org/html/2512.03123v1#bib.bibx22)], Glosten and Milgrom [[GM85](https://arxiv.org/html/2512.03123v1#bib.bibx17)], and modern execution literature.
2. 2.

   Theorem [4.1](https://arxiv.org/html/2512.03123v1#S4.Thmtheorem1 "Theorem 4.1 (Financial Second Law). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"): necessary and sufficient convexity conditions on the impact functional to enforce 𝔼​[ΠT]≤0\mathbb{E}[\Pi\_{T}]\leq 0 for all round trips, establishing a fundamental link between market structure and no-arbitrage.
3. 3.

   Theorem [5.1](https://arxiv.org/html/2512.03123v1#S5.Thmtheorem1 "Theorem 5.1 (Financial Fluctuation Theorem). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"): a Chernoff bound yielding ℙ​(ΠT≥0)≤exp⁡(−W​[v]2/(2​σ2​∫0Tqt2​𝑑t))\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp(-W[v]^{2}/(2\sigma^{2}\int\_{0}^{T}q\_{t}^{2}dt)), providing a quantitative measure of market efficiency.
4. 4.

   Proposition [6.2](https://arxiv.org/html/2512.03123v1#S6.Thmtheorem2 "Proposition 6.2 (Free Energy Decomposition). ‣ 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"): a free energy decomposition for strategy ensembles with explicit interpretation of market temperature, connecting to large deviations theory [[DZ10](https://arxiv.org/html/2512.03123v1#bib.bibx12)].
5. 5.

   Detailed analytical calculations for prototypical strategies (Section [7](https://arxiv.org/html/2512.03123v1#S7 "7 Detailed Analytical Examples ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) with complete derivations and economic interpretations.
6. 6.

   Discussion of empirical validation protocols and connections to market microstructure literature [[Has07](https://arxiv.org/html/2512.03123v1#bib.bibx19), [CJP15](https://arxiv.org/html/2512.03123v1#bib.bibx10)].

The mathematics relies only on graduate-level probability (Itô calculus), convex analysis (Fenchel-Legendre transforms), and large deviation bounds—accessible yet yielding novel structural insights that complement existing market microstructure theory.

## 2 Related Literature

The relationship between physics and finance has a rich history. Louis Bachelier’s 1900 thesis [[Bac00](https://arxiv.org/html/2512.03123v1#bib.bibx5)] introduced Brownian motion to model asset prices, decades before Einstein’s work on diffusion [[Ein05](https://arxiv.org/html/2512.03123v1#bib.bibx13)]. More recently, statistical mechanics has been applied to agent-based models [[BH97](https://arxiv.org/html/2512.03123v1#bib.bibx7), [LeB06](https://arxiv.org/html/2512.03123v1#bib.bibx23)] and to understand market crashes [[Sor03](https://arxiv.org/html/2512.03123v1#bib.bibx28)].

Stochastic thermodynamics, however, remains underutilized in finance despite its natural fit for non-equilibrium systems. The framework developed here parallels the work of Jarzynski [[Jar97](https://arxiv.org/html/2512.03123v1#bib.bibx20)] on non-equilibrium work relations and Crooks [[Cro99](https://arxiv.org/html/2512.03123v1#bib.bibx11)] on entropy production. The contribution of this paper is to map these concepts directly onto trading dynamics, where the “system” is the limit order book and the “protocol” is the trading strategy.

In market microstructure, this work complements the seminal contributions of Kyle [[Kyl85](https://arxiv.org/html/2512.03123v1#bib.bibx22)], Glosten and Milgrom [[GM85](https://arxiv.org/html/2512.03123v1#bib.bibx17)], and the extensive literature on optimal execution [[Gat10](https://arxiv.org/html/2512.03123v1#bib.bibx15), [GSS12](https://arxiv.org/html/2512.03123v1#bib.bibx18), [AFS10](https://arxiv.org/html/2512.03123v1#bib.bibx3)]. While these works typically assume specific functional forms for impact, this paper derives structural constraints from first principles.

## 3 Model Setup and Thermodynamic Mapping

Let (Ω,ℱ,𝔽,ℚ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{Q}) be a filtered probability space satisfying the usual conditions, with filtration 𝔽={ℱt}t≥0\mathbb{F}=\{\mathcal{F}\_{t}\}\_{t\geq 0} generated by a standard Brownian motion W=(Wt)t≥0W=(W\_{t})\_{t\geq 0}.

### 3.1 Price Dynamics and Impact Functional

We consider a single asset with midprice process S=(St)t≥0S=(S\_{t})\_{t\geq 0} evolving according to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=σ​d​Wt+d​It,S0=s0∈ℝ,dS\_{t}=\sigma\,dW\_{t}+dI\_{t},\qquad S\_{0}=s\_{0}\in\mathbb{R}, |  | (1) |

where σ>0\sigma>0 is constant volatility and d​ItdI\_{t} captures *permanent price impact*.

A trading strategy is specified by an inventory process q=(qt)t≥0q=(q\_{t})\_{t\geq 0}. We assume qtq\_{t} is absolutely continuous:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qt=∫0tvu​𝑑u,vu∈L𝔽2​([0,T]),q\_{t}=\int\_{0}^{t}v\_{u}\,du,\qquad v\_{u}\in L^{2}\_{\mathbb{F}}([0,T]), |  | (2) |

where vuv\_{u} is the trading rate. The set of admissible strategies on [0,T][0,T] is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜T:={v:v​ is ​𝔽​-predictable,𝔼​[∫0Tvt2​𝑑t]​<∞,∫0T|​vt|d​t<∞​ a.s.}.\mathcal{A}\_{T}:=\left\{v:v\text{ is }\mathbb{F}\text{-predictable},\mathbb{E}\left[\int\_{0}^{T}v\_{t}^{2}dt\right]<\infty,\int\_{0}^{T}|v\_{t}|dt<\infty\text{ a.s.}\right\}. |  | (3) |

The permanent impact is modeled as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | It​[v]:=∫0tℐ​(vu)​𝑑u.I\_{t}[v]:=\int\_{0}^{t}\mathcal{I}(v\_{u})\,du. |  | (4) |

Temporary impact is captured via the execution price:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ptexec=St+𝒥​(vt).P\_{t}^{\text{exec}}=S\_{t}+\mathcal{J}(v\_{t}). |  | (5) |

### 3.2 Dissipated Work and Fluctuations

Substituting ([1](https://arxiv.org/html/2512.03123v1#S3.E1 "In 3.1 Price Dynamics and Impact Functional ‣ 3 Model Setup and Thermodynamic Mapping ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) into the P&L integral and integrating by parts yields the fundamental decomposition:

###### Lemma 3.1 (P&L Decomposition).

For any admissible round-trip strategy v∈𝒜Tv\in\mathcal{A}\_{T},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΠT=−∫0T(𝒥​(vt)​vt+ℐ​(vt)​qt)​𝑑t⏟=⁣:W​[v]+σ​∫0Tqt​𝑑Wt⏟=⁣:Q​[v].\Pi\_{T}=-\underbrace{\int\_{0}^{T}\left(\mathcal{J}(v\_{t})v\_{t}+\mathcal{I}(v\_{t})q\_{t}\right)dt}\_{=:W[v]}+\underbrace{\sigma\int\_{0}^{T}q\_{t}\,dW\_{t}}\_{=:Q[v]}. |  | (6) |

###### Proof.

From ([1](https://arxiv.org/html/2512.03123v1#S3.E1 "In 3.1 Price Dynamics and Impact Functional ‣ 3 Model Setup and Thermodynamic Mapping ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")), we have St=s0+σ​Wt+∫0tℐ​(vu)​𝑑uS\_{t}=s\_{0}+\sigma W\_{t}+\int\_{0}^{t}\mathcal{I}(v\_{u})du. Substituting into the P&L integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΠT\displaystyle\Pi\_{T} | =−∫0T(s0+σ​Wt+∫0tℐ​(vu)​𝑑u)​vt​𝑑t−∫0T𝒥​(vt)​vt​𝑑t\displaystyle=-\int\_{0}^{T}\left(s\_{0}+\sigma W\_{t}+\int\_{0}^{t}\mathcal{I}(v\_{u})du\right)v\_{t}\,dt-\int\_{0}^{T}\mathcal{J}(v\_{t})v\_{t}\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−σ​∫0TWt​vt​𝑑t−∫0T𝒥​(vt)​vt​𝑑t−∫0T∫0tℐ​(vu)​𝑑u​vt​𝑑t.\displaystyle=-\sigma\int\_{0}^{T}W\_{t}v\_{t}\,dt-\int\_{0}^{T}\mathcal{J}(v\_{t})v\_{t}\,dt-\int\_{0}^{T}\int\_{0}^{t}\mathcal{I}(v\_{u})du\,v\_{t}\,dt. |  |

The last term uses Fubini’s theorem for stochastic integrals:

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫0tℐ​(vu)​𝑑u​vt​𝑑t=∫0Tℐ​(vu)​∫uTvt​𝑑t​𝑑u=∫0Tℐ​(vu)​(qT−qu)​𝑑u=−∫0Tℐ​(vu)​qu​𝑑u,\int\_{0}^{T}\int\_{0}^{t}\mathcal{I}(v\_{u})du\,v\_{t}\,dt=\int\_{0}^{T}\mathcal{I}(v\_{u})\int\_{u}^{T}v\_{t}\,dt\,du=\int\_{0}^{T}\mathcal{I}(v\_{u})(q\_{T}-q\_{u})\,du=-\int\_{0}^{T}\mathcal{I}(v\_{u})q\_{u}\,du, |  |

where we used qT=0q\_{T}=0 and qt=∫0tvu​𝑑uq\_{t}=\int\_{0}^{t}v\_{u}du.

The stochastic term is integrated by parts using the product rule d​(qt​Wt)=qt​d​Wt+Wt​d​qt+d​⟨q,W⟩td(q\_{t}W\_{t})=q\_{t}\,dW\_{t}+W\_{t}\,dq\_{t}+d\langle q,W\rangle\_{t}. Since qtq\_{t} has finite variation, d​⟨q,W⟩t=0d\langle q,W\rangle\_{t}=0. With q0=qT=0q\_{0}=q\_{T}=0:

|  |  |  |
| --- | --- | --- |
|  | ∫0TWt​vt​𝑑t=∫0TWt​𝑑qt=qT​WT−q0​W0−∫0Tqt​𝑑Wt=−∫0Tqt​𝑑Wt.\int\_{0}^{T}W\_{t}v\_{t}\,dt=\int\_{0}^{T}W\_{t}\,dq\_{t}=q\_{T}W\_{T}-q\_{0}W\_{0}-\int\_{0}^{T}q\_{t}\,dW\_{t}=-\int\_{0}^{T}q\_{t}\,dW\_{t}. |  |

Substituting these results yields ([6](https://arxiv.org/html/2512.03123v1#S3.E6 "In Lemma 3.1 (P&L Decomposition). ‣ 3.2 Dissipated Work and Fluctuations ‣ 3 Model Setup and Thermodynamic Mapping ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")).
∎

This paper calls W​[v]W[v] the *dissipated work* (deterministic cost of impact) and Q​[v]Q[v] the *heat* (random fluctuations). Note that 𝔼​[Q​[v]]=0\mathbb{E}[Q[v]]=0 and 𝔼​[Q​[v]2]=σ2​∫0Tqt2​𝑑t\mathbb{E}[Q[v]^{2}]=\sigma^{2}\int\_{0}^{T}q\_{t}^{2}dt by the Itô isometry [[KS12](https://arxiv.org/html/2512.03123v1#bib.bibx21)].

## 4 The Financial Second Law

We seek conditions such that supv∈𝒜T𝔼​[ΠT]≤0\sup\_{v\in\mathcal{A}\_{T}}\mathbb{E}[\Pi\_{T}]\leq 0. Since 𝔼​[ΠT]=−W​[v]\mathbb{E}[\Pi\_{T}]=-W[v], this requires W​[v]≥0W[v]\geq 0.

###### Assumption 1 (Impact Functions).

The impact functions satisfy:

1. (i)

   ℐ​(0)=𝒥​(0)=0\mathcal{I}(0)=\mathcal{J}(0)=0.
2. (ii)

   The composite functional f​(v):=𝒥​(v)​vf(v):=\mathcal{J}(v)v is strictly convex and f​(v)>0f(v)>0 for v≠0v\neq 0.
3. (iii)

   Linear Permanent Impact: ℐ​(v)=λ​v\mathcal{I}(v)=\lambda v for some constant λ≥0\lambda\geq 0.

###### Theorem 4.1 (Financial Second Law).

Under Assumption [1](https://arxiv.org/html/2512.03123v1#Thmassumption1 "Assumption 1 (Impact Functions). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"), for any round-trip strategy v∈𝒜Tv\in\mathcal{A}\_{T}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ΠT]=−W​[v]≤0,\mathbb{E}[\Pi\_{T}]=-W[v]\leq 0, |  | (7) |

with equality if and only if vt=0v\_{t}=0 almost everywhere.

###### Proof.

From Lemma [3.1](https://arxiv.org/html/2512.03123v1#S3.Thmtheorem1 "Lemma 3.1 (P&L Decomposition). ‣ 3.2 Dissipated Work and Fluctuations ‣ 3 Model Setup and Thermodynamic Mapping ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"), the work functional is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]=∫0Tf​(vt)​𝑑t+∫0Tℐ​(vt)​qt​𝑑t.W[v]=\int\_{0}^{T}f(v\_{t})\,dt+\int\_{0}^{T}\mathcal{I}(v\_{t})q\_{t}\,dt. |  | (8) |

Consider the permanent impact term. Using Assumption [1](https://arxiv.org/html/2512.03123v1#Thmassumption1 "Assumption 1 (Impact Functions). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")(iii), ℐ​(vt)=λ​vt\mathcal{I}(v\_{t})=\lambda v\_{t}. Since vt=q˙tv\_{t}=\dot{q}\_{t}:

|  |  |  |
| --- | --- | --- |
|  | ∫0Tℐ​(vt)​qt​𝑑t=∫0Tλ​q˙t​qt​𝑑t=λ2​∫0Tdd​t​(qt2)​𝑑t=λ2​(qT2−q02).\int\_{0}^{T}\mathcal{I}(v\_{t})q\_{t}\,dt=\int\_{0}^{T}\lambda\dot{q}\_{t}q\_{t}\,dt=\frac{\lambda}{2}\int\_{0}^{T}\frac{d}{dt}(q\_{t}^{2})\,dt=\frac{\lambda}{2}(q\_{T}^{2}-q\_{0}^{2}). |  |

For a round trip, qT=q0=0q\_{T}=q\_{0}=0, so the permanent impact term vanishes exactly.
Thus, W​[v]=∫0Tf​(vt)​𝑑tW[v]=\int\_{0}^{T}f(v\_{t})\,dt.
By Jensen’s inequality and the strict convexity of ff (Assumption [1](https://arxiv.org/html/2512.03123v1#Thmassumption1 "Assumption 1 (Impact Functions). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")(ii)):

|  |  |  |
| --- | --- | --- |
|  | 1T​∫0Tf​(vt)​𝑑t≥f​(1T​∫0Tvt​𝑑t)=f​(qT−q0T)=f​(0)=0.\frac{1}{T}\int\_{0}^{T}f(v\_{t})\,dt\geq f\left(\frac{1}{T}\int\_{0}^{T}v\_{t}\,dt\right)=f\left(\frac{q\_{T}-q\_{0}}{T}\right)=f(0)=0. |  |

The inequality is strict unless vtv\_{t} is constant (zero). Thus W​[v]≥0W[v]\geq 0.
∎

###### Remark 4.2.

The assumption of linear permanent impact is standard in the no-dynamic-arbitrage literature (e.g., Gatheral [[Gat10](https://arxiv.org/html/2512.03123v1#bib.bibx15)]). If ℐ​(v)\mathcal{I}(v) were non-linear, one could construct round-trip cycles that extract value from the permanent price shift, violating the Second Law.

### 4.1 Generalized Impact Functionals

The result extends naturally to state-dependent impact 𝒥​(vt,qt)\mathcal{J}(v\_{t},q\_{t}) and more general work functionals. Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]:=∫0Tℒ​(vt,qt)​𝑑t,W[v]:=\int\_{0}^{T}\mathcal{L}(v\_{t},q\_{t})\,dt, |  | (9) |

where ℒ\mathcal{L} is a Lagrangian convex in vtv\_{t} for each qtq\_{t} and minimized at vt=0v\_{t}=0.

###### Corollary 4.3 (Generalized Financial Second Law).

If ℒ​(v,q)\mathcal{L}(v,q) is convex in vv and ℒ​(0,q)=0\mathcal{L}(0,q)=0 for all qq, then infv∈𝒜TW​[v]=0\inf\_{v\in\mathcal{A}\_{T}}W[v]=0 and W​[v]>0W[v]>0 for any non-zero strategy.

###### Proof.

By convexity of ℒ\mathcal{L} in its first argument, for any qtq\_{t} we have:

|  |  |  |
| --- | --- | --- |
|  | ℒ​(vt,qt)≥ℒ​(0,qt)+∂vℒ​(0,qt)​vt.\mathcal{L}(v\_{t},q\_{t})\geq\mathcal{L}(0,q\_{t})+\partial\_{v}\mathcal{L}(0,q\_{t})v\_{t}. |  |

Since ℒ​(0,qt)=0\mathcal{L}(0,q\_{t})=0 and the strategy is a round trip (∫0Tvt​𝑑t=0\int\_{0}^{T}v\_{t}dt=0), integrating yields W​[v]≥0W[v]\geq 0. Strict convexity ensures equality only when vt=0v\_{t}=0 a.e.
∎

## 5 Fluctuation Theorem for Round-Trip P&L

While Theorem [4.1](https://arxiv.org/html/2512.03123v1#S4.Thmtheorem1 "Theorem 4.1 (Financial Second Law). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") concerns expectations, fluctuation theorems quantify the probability of observing transient violations. This section derives a sharp bound on ℙ​(ΠT≥0)\mathbb{P}(\Pi\_{T}\geq 0) using large deviation techniques [[DZ10](https://arxiv.org/html/2512.03123v1#bib.bibx12)].

###### Assumption 2 (Quadratic Impact for Fluctuation Analysis).

For the fluctuation analysis, we specialize to quadratic temporary impact:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(v)=η​v,η>0,\mathcal{J}(v)=\eta v,\quad\eta>0, |  | (10) |

and linear permanent impact:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(v)=λ​v,λ≥0.\mathcal{I}(v)=\lambda v,\quad\lambda\geq 0. |  | (11) |

Under this specification, the work functional simplifies significantly. The permanent impact term vanishes for any round trip:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0Tℐ​(vt)​qt​𝑑t=λ​∫0Tvt​qt​𝑑t=λ2​(qT2−q02)=0.\int\_{0}^{T}\mathcal{I}(v\_{t})q\_{t}dt=\lambda\int\_{0}^{T}v\_{t}q\_{t}dt=\frac{\lambda}{2}(q\_{T}^{2}-q\_{0}^{2})=0. |  | (12) |

Thus, the dissipated work depends only on temporary impact:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]=∫0Tη​vt2​𝑑t=α​∫0Tvt2​𝑑t,W[v]=\int\_{0}^{T}\eta v\_{t}^{2}dt=\alpha\int\_{0}^{T}v\_{t}^{2}dt, |  | (13) |

where we define the effective coefficient α:=η\alpha:=\eta.

Under Assumption [2](https://arxiv.org/html/2512.03123v1#Thmassumption2 "Assumption 2 (Quadratic Impact for Fluctuation Analysis). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"), the P&L becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΠT=−W​[v]+σ​∫0Tqt​𝑑Wt.\Pi\_{T}=-W[v]+\sigma\int\_{0}^{T}q\_{t}\,dW\_{t}. |  | (14) |

###### Theorem 5.1 (Financial Fluctuation Theorem).

For any v∈𝒜Tv\in\mathcal{A}\_{T}, define the dissipated work W​[v]W[v] and position variance V​[v]:=∫0Tqt2​𝑑tV[v]:=\int\_{0}^{T}q\_{t}^{2}dt. Then the probability of a profitable round trip satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ΠT≥0)≤exp⁡(−W​[v]22​σ2​V​[v]).\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp\left(-\frac{W[v]^{2}}{2\sigma^{2}V[v]}\right). |  | (15) |

###### Proof.

The random variable Q​[v]=σ​∫0Tqt​𝑑WtQ[v]=\sigma\int\_{0}^{T}q\_{t}\,dW\_{t} is Gaussian conditional on the strategy path: Q​[v]∼𝒩​(0,σ2​V​[v])Q[v]\sim\mathcal{N}(0,\sigma^{2}V[v]). This follows directly from the properties of the Itô integral [[KS12](https://arxiv.org/html/2512.03123v1#bib.bibx21)].

The moment generating function (MGF) of ΠT\Pi\_{T} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​(θ)\displaystyle M(\theta) | :=𝔼​[eθ​ΠT]=e−θ​W​[v]​𝔼​[eθ​Q​[v]]\displaystyle:=\mathbb{E}\left[e^{\theta\Pi\_{T}}\right]=e^{-\theta W[v]}\mathbb{E}\left[e^{\theta Q[v]}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =exp⁡(−θ​W​[v]+12​θ2​σ2​V​[v]).\displaystyle=\exp\left(-\theta W[v]+\frac{1}{2}\theta^{2}\sigma^{2}V[v]\right). |  | (16) |

This holds for all θ∈ℝ\theta\in\mathbb{R} because the Gaussian MGF exists everywhere.

Applying the Chernoff bound for θ>0\theta>0:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ΠT≥0)=ℙ​(eθ​ΠT≥1)≤infθ>0𝔼​[eθ​ΠT]=infθ>0M​(θ).\mathbb{P}(\Pi\_{T}\geq 0)=\mathbb{P}(e^{\theta\Pi\_{T}}\geq 1)\leq\inf\_{\theta>0}\mathbb{E}[e^{\theta\Pi\_{T}}]=\inf\_{\theta>0}M(\theta). |  |

The exponent in ([16](https://arxiv.org/html/2512.03123v1#S5.E16 "In 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) is a quadratic function of θ\theta: g​(θ)=−θ​W​[v]+12​θ2​σ2​V​[v]g(\theta)=-\theta W[v]+\frac{1}{2}\theta^{2}\sigma^{2}V[v]. To find the optimal bound, we minimize g​(θ)g(\theta) over θ>0\theta>0.

Taking the derivative:

|  |  |  |
| --- | --- | --- |
|  | g′​(θ)=−W​[v]+θ​σ2​V​[v].g^{\prime}(\theta)=-W[v]+\theta\sigma^{2}V[v]. |  |

Setting g′​(θ∗)=0g^{\prime}(\theta^{\*})=0 yields the optimal θ∗=W​[v]/(σ2​V​[v])\theta^{\*}=W[v]/(\sigma^{2}V[v]). Since W​[v]>0W[v]>0 for any non-zero strategy (by Theorem [4.1](https://arxiv.org/html/2512.03123v1#S4.Thmtheorem1 "Theorem 4.1 (Financial Second Law). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")), θ∗>0\theta^{\*}>0 as required.

Substituting θ∗\theta^{\*} back into M​(θ)M(\theta):

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​(θ∗)\displaystyle M(\theta^{\*}) | =exp⁡(−W​[v]2σ2​V​[v]+12​W​[v]2σ2​V​[v])\displaystyle=\exp\left(-\frac{W[v]^{2}}{\sigma^{2}V[v]}+\frac{1}{2}\frac{W[v]^{2}}{\sigma^{2}V[v]}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(−W​[v]22​σ2​V​[v]).\displaystyle=\exp\left(-\frac{W[v]^{2}}{2\sigma^{2}V[v]}\right). |  |

This establishes ([15](https://arxiv.org/html/2512.03123v1#S5.E15 "In Theorem 5.1 (Financial Fluctuation Theorem). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")).
∎

###### Corollary 5.2 (Scaling Regime for Persistent Strategies).

For strategies where W​[v]∼c1​TW[v]\sim c\_{1}T and V​[v]∼c2​T3V[v]\sim c\_{2}T^{3} (characteristic of persistent, non-oscillatory trading), this paper obtains:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ΠT≥0)≤exp⁡(−c122​σ2​c2​1T).\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp\left(-\frac{c\_{1}^{2}}{2\sigma^{2}c\_{2}}\frac{1}{T}\right). |  | (17) |

Thus, the probability of a profitable round trip decays exponentially with the inverse horizon.

###### Proof.

Direct substitution of the scaling relations into ([15](https://arxiv.org/html/2512.03123v1#S5.E15 "In Theorem 5.1 (Financial Fluctuation Theorem). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) yields:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ΠT≥0)≤exp⁡(−(c1​T)22​σ2​(c2​T3))=exp⁡(−c122​σ2​c2​1T).\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp\left(-\frac{(c\_{1}T)^{2}}{2\sigma^{2}(c\_{2}T^{3})}\right)=\exp\left(-\frac{c\_{1}^{2}}{2\sigma^{2}c\_{2}}\frac{1}{T}\right). |  |

∎

###### Remark 5.3 (Interpretation as Entropy Production).

Define the *market temperature* parameter:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βv:=W​[v]σ2​V​[v].\beta\_{v}:=\frac{W[v]}{\sigma^{2}V[v]}. |  | (18) |

Then ([15](https://arxiv.org/html/2512.03123v1#S5.E15 "In Theorem 5.1 (Financial Fluctuation Theorem). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ΠT≥0)≤e−βv​W​[v]/2.\mathbb{P}(\Pi\_{T}\geq 0)\leq e^{-\beta\_{v}W[v]/2}. |  | (19) |

This mirrors the Crooks fluctuation theorem ℙ​(Σ=+σ)/ℙ​(Σ=−σ)=eσ\mathbb{P}(\Sigma=+\sigma)/\mathbb{P}(\Sigma=-\sigma)=e^{\sigma}, where Σ\Sigma is entropy production [[Cro99](https://arxiv.org/html/2512.03123v1#bib.bibx11)]. Here, βv​W​[v]\beta\_{v}W[v] plays the role of entropy production, quantifying the irreversibility of the trading cycle. A larger βv\beta\_{v} (colder market) suppresses profitable fluctuations more strongly.

## 6 Free Energy of Trading Strategy Ensembles

Consider a large population of traders, each executing a round-trip strategy v(i)∈𝒜Tv^{(i)}\in\mathcal{A}\_{T} drawn from a finite set {v1,…,vN}\{v\_{1},\dots,v\_{N}\}. Let pip\_{i} be the fraction of traders using strategy viv\_{i}.

###### Definition 6.1 (Gibbs Measure over Strategies).

For inverse temperature β>0\beta>0, define the probability of strategy viv\_{i} as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​(β):=e−β​W​[vi]Z​(β),Z​(β):=∑j=1Ne−β​W​[vj].p\_{i}(\beta):=\frac{e^{-\beta W[v\_{i}]}}{Z(\beta)},\qquad Z(\beta):=\sum\_{j=1}^{N}e^{-\beta W[v\_{j}]}. |  | (20) |

The partition function Z​(β)Z(\beta) normalizes the distribution. The *free energy* is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(β):=−1β​log⁡Z​(β).F(\beta):=-\frac{1}{\beta}\log Z(\beta). |  | (21) |

###### Proposition 6.2 (Free Energy Decomposition).

Let Wβ:=𝔼p​(β)​[W​[v]]W\_{\beta}:=\mathbb{E}\_{p(\beta)}[W[v]] be the expected work and S​(β):=−∑i=1Npi​(β)​log⁡pi​(β)S(\beta):=-\sum\_{i=1}^{N}p\_{i}(\beta)\log p\_{i}(\beta) the Shannon entropy of the strategy distribution. Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(β)=Wβ−1β​S​(β).F(\beta)=W\_{\beta}-\frac{1}{\beta}S(\beta). |  | (22) |

###### Proof.

From ([20](https://arxiv.org/html/2512.03123v1#S6.E20 "In Definition 6.1 (Gibbs Measure over Strategies). ‣ 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")), we have for each ii:

|  |  |  |
| --- | --- | --- |
|  | log⁡pi​(β)=−β​W​[vi]−log⁡Z​(β).\log p\_{i}(\beta)=-\beta W[v\_{i}]-\log Z(\beta). |  |

Taking expectation under p​(β)p(\beta):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1Npi​(β)​log⁡pi​(β)\displaystyle\sum\_{i=1}^{N}p\_{i}(\beta)\log p\_{i}(\beta) | =−β​∑i=1Npi​(β)​W​[vi]−log⁡Z​(β)​∑i=1Npi​(β)\displaystyle=-\beta\sum\_{i=1}^{N}p\_{i}(\beta)W[v\_{i}]-\log Z(\beta)\sum\_{i=1}^{N}p\_{i}(\beta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−β​Wβ−log⁡Z​(β).\displaystyle=-\beta W\_{\beta}-\log Z(\beta). |  |

Since S​(β)=−∑pi​(β)​log⁡pi​(β)S(\beta)=-\sum p\_{i}(\beta)\log p\_{i}(\beta), we have:

|  |  |  |
| --- | --- | --- |
|  | −log⁡Z​(β)=S​(β)−β​Wβ.-\log Z(\beta)=S(\beta)-\beta W\_{\beta}. |  |

Dividing by −β-\beta and using ([21](https://arxiv.org/html/2512.03123v1#S6.E21 "In 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) yields ([22](https://arxiv.org/html/2512.03123v1#S6.E22 "In Proposition 6.2 (Free Energy Decomposition). ‣ 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")).
∎

###### Corollary 6.3 (Thermodynamic Relations).

The free energy satisfies the following relations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂F∂β\displaystyle\frac{\partial F}{\partial\beta} | =F​(β)−Wββ=−1β2​S​(β),\displaystyle=\frac{F(\beta)-W\_{\beta}}{\beta}=-\frac{1}{\beta^{2}}S(\beta), |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂2(β​F)∂β2\displaystyle\frac{\partial^{2}(\beta F)}{\partial\beta^{2}} | =Varp​(β)​(W​[v])≥0.\displaystyle=\mathrm{Var}\_{p(\beta)}(W[v])\geq 0. |  | (24) |

Thus, β​F​(β)\beta F(\beta) is a convex function of β\beta.

###### Proof.

Differentiating F​(β)=−β−1​log⁡Z​(β)F(\beta)=-\beta^{-1}\log Z(\beta):

|  |  |  |
| --- | --- | --- |
|  | ∂F∂β=log⁡Z​(β)β2−1β​Z′​(β)Z​(β).\frac{\partial F}{\partial\beta}=\frac{\log Z(\beta)}{\beta^{2}}-\frac{1}{\beta}\frac{Z^{\prime}(\beta)}{Z(\beta)}. |  |

Since Z′​(β)=−∑iW​[vi]​e−β​W​[vi]=−Z​(β)​WβZ^{\prime}(\beta)=-\sum\_{i}W[v\_{i}]e^{-\beta W[v\_{i}]}=-Z(\beta)W\_{\beta}, we get:

|  |  |  |
| --- | --- | --- |
|  | ∂F∂β=log⁡Z​(β)β2+Wββ=F​(β)−Wββ.\frac{\partial F}{\partial\beta}=\frac{\log Z(\beta)}{\beta^{2}}+\frac{W\_{\beta}}{\beta}=\frac{F(\beta)-W\_{\beta}}{\beta}. |  |

Using ([22](https://arxiv.org/html/2512.03123v1#S6.E22 "In Proposition 6.2 (Free Energy Decomposition). ‣ 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")), this equals −S​(β)/β2-S(\beta)/\beta^{2}.

For ([24](https://arxiv.org/html/2512.03123v1#S6.E24 "In Corollary 6.3 (Thermodynamic Relations). ‣ 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")), note β​F​(β)=−log⁡Z​(β)\beta F(\beta)=-\log Z(\beta). Differentiating twice:

|  |  |  |
| --- | --- | --- |
|  | ∂2∂β2​(β​F​(β))=Z′′​(β)Z​(β)−(Z′​(β)Z​(β))2=𝔼​[W2]−(𝔼​[W])2=Var​(W)≥0.\frac{\partial^{2}}{\partial\beta^{2}}(\beta F(\beta))=\frac{Z^{\prime\prime}(\beta)}{Z(\beta)}-\left(\frac{Z^{\prime}(\beta)}{Z(\beta)}\right)^{2}=\mathbb{E}[W^{2}]-(\mathbb{E}[W])^{2}=\mathrm{Var}(W)\geq 0. |  |

∎

###### Remark 6.4 (Economic Interpretation of Temperature).

The parameter β\beta measures market *rationality* or *competitive pressure*:

* •

  β→∞\beta\to\infty (zero temperature): All probability mass concentrates on the minimal-work strategy, pi→δi,i∗p\_{i}\to\delta\_{i,i^{\*}} where i∗=arg​mini⁡W​[vi]i^{\*}=\operatorname\*{arg\,min}\_{i}W[v\_{i}]. This corresponds to a perfectly efficient market where all agents adopt the optimal execution strategy [[AC01](https://arxiv.org/html/2512.03123v1#bib.bibx2)].
* •

  β→0\beta\to 0 (infinite temperature): Strategies become uniformly random, pi→1/Np\_{i}\to 1/N, maximizing entropy. This represents a disordered, highly speculative market with no coordination.
* •

  Intermediate β\beta: The market exhibits a trade-off between cost minimization and strategic diversity, analogous to the exploration-exploitation dilemma in statistical learning.

The free energy F​(β)F(\beta) bounds the achievable aggregate expected P&L per trader: no ensemble can outperform −F​(β)-F(\beta) on average.

## 7 Detailed Analytical Examples

This section presents comprehensive analytical calculations for prototypical trading strategies, providing complete derivations and economic interpretations at each step.

### 7.1 The Triangular (Symmetric) Strategy

Consider the deterministic triangular strategy defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt={+v¯,0≤t≤T/2,−v¯,T/2<t≤T,v¯>0.v\_{t}=\begin{cases}+\bar{v},&0\leq t\leq T/2,\\ -\bar{v},&T/2<t\leq T,\end{cases}\qquad\bar{v}>0. |  | (25) |

This strategy builds a linear position qt=v¯​tq\_{t}=\bar{v}t during the first half-period and liquidates symmetrically during the second half, ensuring qT=0q\_{T}=0.

#### 7.1.1 Position Process Calculation

The position process is computed explicitly by integrating the trading rate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qt=∫0tvu​𝑑u={∫0tv¯​𝑑u=v¯​t,0≤t≤T/2,∫0T/2v¯​𝑑u+∫T/2t(−v¯)​𝑑u=v¯​T2−v¯​(t−T2)=v¯​(T−t),T/2<t≤T.q\_{t}=\int\_{0}^{t}v\_{u}\,du=\begin{cases}\int\_{0}^{t}\bar{v}\,du=\bar{v}t,&0\leq t\leq T/2,\\ \int\_{0}^{T/2}\bar{v}\,du+\int\_{T/2}^{t}(-\bar{v})\,du=\bar{v}\frac{T}{2}-\bar{v}\left(t-\frac{T}{2}\right)=\bar{v}(T-t),&T/2<t\leq T.\end{cases} |  | (26) |

The evolution of qtq\_{t} is piecewise linear: rising from 0 to v¯​T/2\bar{v}T/2 at the midpoint, then declining symmetrically back to 0. This shape is economically natural for strategies that accumulate and then unwind a position.

#### 7.1.2 Work Functional Calculation

Under the linear permanent impact assumption (I​(v)=λ​vI(v)=\lambda v), the total work comes purely from the temporary impact component, as the permanent impact integrates to zero over the closed cycle.

The work is computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]=α​∫0Tvt2​𝑑t=α​[∫0T/2v¯2​𝑑t+∫T/2T(−v¯)2​𝑑t].W[v]=\alpha\int\_{0}^{T}v\_{t}^{2}\,dt=\alpha\left[\int\_{0}^{T/2}\bar{v}^{2}\,dt+\int\_{T/2}^{T}(-\bar{v})^{2}\,dt\right]. |  | (27) |

Evaluating the integrals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]=α​[v¯2​T2+v¯2​T2]=α​v¯2​T.W[v]=\alpha\left[\bar{v}^{2}\frac{T}{2}+\bar{v}^{2}\frac{T}{2}\right]=\alpha\bar{v}^{2}T. |  | (28) |

Note that here α=η\alpha=\eta. The linear permanent impact term λ\lambda does not affect the expected cost of the round trip, consistent with the property that linear permanent impact is conservative (a state function) and cannot be exploited for profit or loss in a closed loop.

#### 7.1.3 Position Variance Calculation

The variance term V​[v]=∫0Tqt2​𝑑tV[v]=\int\_{0}^{T}q\_{t}^{2}dt requires careful piecewise integration:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0Tqt2​𝑑t\displaystyle\int\_{0}^{T}q\_{t}^{2}dt | =∫0T/2(v¯​t)2​𝑑t+∫T/2T(v¯​(T−t))2​𝑑t\displaystyle=\int\_{0}^{T/2}(\bar{v}t)^{2}dt+\int\_{T/2}^{T}(\bar{v}(T-t))^{2}dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =v¯2​[∫0T/2t2​𝑑t+∫T/2T(T−t)2​𝑑t].\displaystyle=\bar{v}^{2}\left[\int\_{0}^{T/2}t^{2}dt+\int\_{T/2}^{T}(T-t)^{2}dt\right]. |  | (29) |

For the second integral, substitute u=T−tu=T-t, d​u=−d​tdu=-dt; when t=T/2t=T/2, u=T/2u=T/2; when t=Tt=T, u=0u=0:

|  |  |  |
| --- | --- | --- |
|  | ∫T/2T(T−t)2​𝑑t=∫T/20u2​(−d​u)=∫0T/2u2​𝑑u=(T/2)33.\int\_{T/2}^{T}(T-t)^{2}dt=\int\_{T/2}^{0}u^{2}(-du)=\int\_{0}^{T/2}u^{2}du=\frac{(T/2)^{3}}{3}. |  |

Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0Tqt2​𝑑t=v¯2​[(T/2)33+(T/2)33]=2​v¯23​(T2)3=v¯2​T312.\int\_{0}^{T}q\_{t}^{2}dt=\bar{v}^{2}\left[\frac{(T/2)^{3}}{3}+\frac{(T/2)^{3}}{3}\right]=\frac{2\bar{v}^{2}}{3}\left(\frac{T}{2}\right)^{3}=\frac{\bar{v}^{2}T^{3}}{12}. |  | (30) |

Interpretation: The position variance scales as T3T^{3}, much faster than the work (∼T\sim T). This reflects that positions accumulate over time, so the exposure to market noise grows super-linearly.

#### 7.1.4 P&L Distribution and Statistics

Combining ([28](https://arxiv.org/html/2512.03123v1#S7.E28 "In 7.1.2 Work Functional Calculation ‣ 7.1 The Triangular (Symmetric) Strategy ‣ 7 Detailed Analytical Examples ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) and ([30](https://arxiv.org/html/2512.03123v1#S7.E30 "In 7.1.3 Position Variance Calculation ‣ 7.1 The Triangular (Symmetric) Strategy ‣ 7 Detailed Analytical Examples ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) with Lemma [3.1](https://arxiv.org/html/2512.03123v1#S3.Thmtheorem1 "Lemma 3.1 (P&L Decomposition). ‣ 3.2 Dissipated Work and Fluctuations ‣ 3 Model Setup and Thermodynamic Mapping ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"), we obtain:

###### Proposition 7.1 (Triangular Strategy P&L).

The round-trip P&L for the triangular strategy is Gaussian:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΠT∼𝒩​(−α​v¯2​T,σ2​v¯2​T312).\Pi\_{T}\sim\mathcal{N}\left(-\alpha\bar{v}^{2}T,\;\sigma^{2}\frac{\bar{v}^{2}T^{3}}{12}\right). |  | (31) |

###### Proof.

From Lemma [3.1](https://arxiv.org/html/2512.03123v1#S3.Thmtheorem1 "Lemma 3.1 (P&L Decomposition). ‣ 3.2 Dissipated Work and Fluctuations ‣ 3 Model Setup and Thermodynamic Mapping ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") and Assumption [2](https://arxiv.org/html/2512.03123v1#Thmassumption2 "Assumption 2 (Quadratic Impact for Fluctuation Analysis). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"):

|  |  |  |
| --- | --- | --- |
|  | ΠT=−α​∫0Tvt2​𝑑t+σ​∫0Tqt​𝑑Wt=−α​v¯2​T+σ​∫0Tqt​𝑑Wt.\Pi\_{T}=-\alpha\int\_{0}^{T}v\_{t}^{2}dt+\sigma\int\_{0}^{T}q\_{t}dW\_{t}=-\alpha\bar{v}^{2}T+\sigma\int\_{0}^{T}q\_{t}dW\_{t}. |  |

The stochastic integral is Gaussian with mean 0 and variance σ2​∫0Tqt2​𝑑t=σ2​v¯2​T3/12\sigma^{2}\int\_{0}^{T}q\_{t}^{2}dt=\sigma^{2}\bar{v}^{2}T^{3}/12, establishing the result.
∎

The expected P&L is negative and proportional to the total work dissipated. The standard deviation is:

|  |  |  |
| --- | --- | --- |
|  | Std​(ΠT)=σ​v¯​T3/212=σ​v¯​T3/22​3.\text{Std}(\Pi\_{T})=\sigma\bar{v}\frac{T^{3/2}}{\sqrt{12}}=\frac{\sigma\bar{v}T^{3/2}}{2\sqrt{3}}. |  |

#### 7.1.5 Probability of Profitability

The Sharpe ratio (mean-to-standard-deviation) of this strategy is:

|  |  |  |
| --- | --- | --- |
|  | SR=−α​v¯2​Tσ​v¯​T3/2/12=−α​12σ​T.\text{SR}=\frac{-\alpha\bar{v}^{2}T}{\sigma\bar{v}T^{3/2}/\sqrt{12}}=-\frac{\alpha\sqrt{12}}{\sigma\sqrt{T}}. |  |

The negative sign confirms the expected loss. The magnitude decreases as T−1/2T^{-1/2}, meaning longer horizons make the loss more predictable relative to fluctuations.

###### Corollary 7.2 (Exact Profit Probability).

The probability of a non-negative P&L is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ΠT≥0)=Φ​(−𝔼​[ΠT]Var​(ΠT))=Φ​(α​12σ​T),\mathbb{P}(\Pi\_{T}\geq 0)=\Phi\left(-\frac{\mathbb{E}[\Pi\_{T}]}{\sqrt{\mathrm{Var}(\Pi\_{T})}}\right)=\Phi\left(\frac{\alpha\sqrt{12}}{\sigma\sqrt{T}}\right), |  | (32) |

where Φ\Phi is the standard normal CDF.

###### Proof.

For X∼𝒩​(μ,σ2)X\sim\mathcal{N}(\mu,\sigma^{2}), ℙ​(X≥0)=Φ​(−μ/σ)\mathbb{P}(X\geq 0)=\Phi(-\mu/\sigma). Applying this to Proposition [7.1](https://arxiv.org/html/2512.03123v1#S7.Thmtheorem1 "Proposition 7.1 (Triangular Strategy P&L). ‣ 7.1.4 P&L Distribution and Statistics ‣ 7.1 The Triangular (Symmetric) Strategy ‣ 7 Detailed Analytical Examples ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") with μ=−α​v¯2​T\mu=-\alpha\bar{v}^{2}T and σ2=σ2​v¯2​T3/12\sigma^{2}=\sigma^{2}\bar{v}^{2}T^{3}/12 yields:

|  |  |  |
| --- | --- | --- |
|  | −μσ=−−α​v¯2​Tσ​v¯​T3/2/12=α​12σ​T.-\frac{\mu}{\sigma}=-\frac{-\alpha\bar{v}^{2}T}{\sigma\bar{v}T^{3/2}/\sqrt{12}}=\frac{\alpha\sqrt{12}}{\sigma\sqrt{T}}. |  |

∎

#### 7.1.6 Comparison with Fluctuation Bound

The bound from Theorem [5.1](https://arxiv.org/html/2512.03123v1#S5.Thmtheorem1 "Theorem 5.1 (Financial Fluctuation Theorem). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ΠT≥0)≤exp⁡(−(α​v¯2​T)22​σ2​(v¯2​T3/12))=exp⁡(−6​α2σ2​T).\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp\left(-\frac{(\alpha\bar{v}^{2}T)^{2}}{2\sigma^{2}(\bar{v}^{2}T^{3}/12)}\right)=\exp\left(-\frac{6\alpha^{2}}{\sigma^{2}T}\right). |  | (33) |

We can compare this with the exact probability from Corollary [7.2](https://arxiv.org/html/2512.03123v1#S7.Thmtheorem2 "Corollary 7.2 (Exact Profit Probability). ‣ 7.1.5 Probability of Profitability ‣ 7.1 The Triangular (Symmetric) Strategy ‣ 7 Detailed Analytical Examples ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications"). For large TT, both decay as exp⁡(−C/T)\exp(-C/T), but the prefactors differ. The Chernoff bound is slightly looser but captures the correct scaling.

### 7.2 The Square-Wave (High-Frequency) Strategy

To illustrate the effect of strategy frequency, consider a square-wave strategy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt={+v¯,t∈⋃k=0n−1[k​T/n,(2​k+1)​T/(2​n)),−v¯,t∈⋃k=0n−1[(2​k+1)​T/(2​n),(2​k+2)​T/(2​n)),v\_{t}=\begin{cases}+\bar{v},&t\in\bigcup\_{k=0}^{n-1}[kT/n,(2k+1)T/(2n)),\\ -\bar{v},&t\in\bigcup\_{k=0}^{n-1}[(2k+1)T/(2n),(2k+2)T/(2n)),\end{cases} |  | (34) |

with nn cycles of period T/nT/n. This strategy oscillates rapidly, maintaining small net positions.

#### 7.2.1 Position and Work Calculations

Within each cycle [k​T/n,(k+1)​T/n)[kT/n,(k+1)T/n), the position evolves as:

|  |  |  |
| --- | --- | --- |
|  | qt={v¯​(t−k​T/n),first half of cycle,v¯​(T/n−(t−k​T/n)),second half of cycle.q\_{t}=\begin{cases}\bar{v}(t-kT/n),&\text{first half of cycle},\\ \bar{v}(T/n-(t-kT/n)),&\text{second half of cycle}.\end{cases} |  |

The maximum position in each cycle is v¯​T/(2​n)\bar{v}T/(2n). The work per cycle is:

|  |  |  |
| --- | --- | --- |
|  | Wcycle=α​v¯2​Tn.W\_{\text{cycle}}=\alpha\bar{v}^{2}\frac{T}{n}. |  |

Summing over nn cycles gives the total work:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]=n⋅α​v¯2​Tn=α​v¯2​T,W[v]=n\cdot\alpha\bar{v}^{2}\frac{T}{n}=\alpha\bar{v}^{2}T, |  | (35) |

identical to the triangular strategy! This surprising result shows that total work depends only on the total trading activity ∫vt2​𝑑t\int v\_{t}^{2}dt, not on its temporal distribution.

#### 7.2.2 Position Variance and Fluctuation Suppression

The variance term V​[v]V[v] is dramatically different:

|  |  |  |
| --- | --- | --- |
|  | V​[v]=∫0Tqt2​𝑑t=n⋅∫0T/nqt2​𝑑t=n⋅v¯2​(T/n)312=v¯2​T312​n2.V[v]=\int\_{0}^{T}q\_{t}^{2}dt=n\cdot\int\_{0}^{T/n}q\_{t}^{2}dt=n\cdot\frac{\bar{v}^{2}(T/n)^{3}}{12}=\frac{\bar{v}^{2}T^{3}}{12n^{2}}. |  |

The 1/n21/n^{2} factor shows that high-frequency oscillations drastically reduce exposure to market noise. This leads to a much tighter fluctuation bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ΠT≥0)≤exp⁡(−(α​v¯2​T)22​σ2​(v¯2​T3/(12​n2)))=exp⁡(−6​n2​α2σ2​T).\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp\left(-\frac{(\alpha\bar{v}^{2}T)^{2}}{2\sigma^{2}(\bar{v}^{2}T^{3}/(12n^{2}))}\right)=\exp\left(-\frac{6n^{2}\alpha^{2}}{\sigma^{2}T}\right). |  | (36) |

Economic interpretation: High-frequency round trips are much less likely to be profitable due to reduced inventory risk, but they incur the same expected cost from market impact. This explains why market makers typically operate with very small inventories.

### 7.3 The Ramp-Up/Decay Strategy

Consider a strategy where trading intensity varies linearly:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt=v¯⋅T−2​tT,0≤t≤T.v\_{t}=\bar{v}\cdot\frac{T-2t}{T},\quad 0\leq t\leq T. |  | (37) |

This starts with maximum buying at t=0t=0 (v0=v¯v\_{0}=\bar{v}), gradually slows, switches to selling at t=T/2t=T/2 (vT/2=0v\_{T/2}=0), and accelerates selling to vT=−v¯v\_{T}=-\bar{v}.

#### 7.3.1 Position Process

Integrating vtv\_{t}:

|  |  |  |
| --- | --- | --- |
|  | qt=∫0tv¯​T−2​uT​𝑑u=v¯​[t−t2T]=v¯​t​(1−tT).q\_{t}=\int\_{0}^{t}\bar{v}\frac{T-2u}{T}du=\bar{v}\left[t-\frac{t^{2}}{T}\right]=\bar{v}t\left(1-\frac{t}{T}\right). |  |

The position is a concave parabola, peaking at t=T/2t=T/2 with qT/2=v¯​T/4q\_{T/2}=\bar{v}T/4.

#### 7.3.2 Work and Variance Calculations

The work functional requires integrating the square of the trading rate:

|  |  |  |
| --- | --- | --- |
|  | W​[v]=α​∫0Tvt2​𝑑t=α​v¯2​∫0T(T−2​tT)2​𝑑t.W[v]=\alpha\int\_{0}^{T}v\_{t}^{2}dt=\alpha\bar{v}^{2}\int\_{0}^{T}\left(\frac{T-2t}{T}\right)^{2}dt. |  |

Let u=T−2​tu=T-2t, then d​u=−2​d​tdu=-2dt. The limits change from TT to −T-T:

|  |  |  |
| --- | --- | --- |
|  | ∫0T(T−2​tT)2​𝑑t=1T2​∫T−Tu2​(−d​u2)=12​T2​∫−TTu2​𝑑u.\int\_{0}^{T}\left(\frac{T-2t}{T}\right)^{2}dt=\frac{1}{T^{2}}\int\_{T}^{-T}u^{2}\left(-\frac{du}{2}\right)=\frac{1}{2T^{2}}\int\_{-T}^{T}u^{2}du. |  |

|  |  |  |
| --- | --- | --- |
|  | =12​T2​[u33]−TT=12​T2​(T33−−T33)=12​T2⋅2​T33=T3.=\frac{1}{2T^{2}}\left[\frac{u^{3}}{3}\right]\_{-T}^{T}=\frac{1}{2T^{2}}\left(\frac{T^{3}}{3}-\frac{-T^{3}}{3}\right)=\frac{1}{2T^{2}}\cdot\frac{2T^{3}}{3}=\frac{T}{3}. |  |

Therefore, the correct work is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]=α​v¯2​T3.W[v]=\alpha\bar{v}^{2}\frac{T}{3}. |  | (38) |

The variance term remains:

|  |  |  |
| --- | --- | --- |
|  | V​[v]=v¯2​T330.V[v]=\bar{v}^{2}\frac{T^{3}}{30}. |  |

Comparing this to the triangular strategy (Wt​r​i=α​v¯2​TW\_{tri}=\alpha\bar{v}^{2}T), we see that Wr​a​m​p=13​Wt​r​iW\_{ramp}=\frac{1}{3}W\_{tri}. The smooth ramping reduces impact costs by a factor of 3 compared to the abrupt switching of the triangular strategy.

#### 7.3.3 Comparison with Triangular Strategy

Comparing with the triangular strategy:
- Work: Wramp/Wtri=1/3W\_{\text{ramp}}/W\_{\text{tri}}=1/3, showing that gradual trading reduces impact costs.
- Variance: Vramp/Vtri=(1/30)/(1/12)=0.4V\_{\text{ramp}}/V\_{\text{tri}}=(1/30)/(1/12)=0.4, showing reduced inventory risk.
The Sharpe ratio improves to:

|  |  |  |
| --- | --- | --- |
|  | SRramp=−α​v¯2​T/3σ​v¯​T3/2/30=−α​303​σ​T.\text{SR}\_{\text{ramp}}=-\frac{\alpha\bar{v}^{2}T/3}{\sigma\bar{v}T^{3/2}/\sqrt{30}}=-\frac{\alpha\sqrt{30}}{3\sigma\sqrt{T}}. |  |

This demonstrates the fundamental trade-off in optimal execution: slower trading reduces impact costs but increases exposure to market noise [[Gat10](https://arxiv.org/html/2512.03123v1#bib.bibx15), [AC01](https://arxiv.org/html/2512.03123v1#bib.bibx2)].

Code Availability: The complete Python and C++ source code for the numerical experiments and fluctuation bound verifications is available at: <https://github.com/AIM-IT4/stochastic-thermo-finance>

## 8 Empirical Implications and Validation

### 8.1 Testing the Financial Second Law

Theorem [4.1](https://arxiv.org/html/2512.03123v1#S4.Thmtheorem1 "Theorem 4.1 (Financial Second Law). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") yields a testable hypothesis: convexity of the temporary impact function f​(v)=𝒥​(v)​vf(v)=\mathcal{J}(v)v is necessary for absence of round-trip arbitrage. Empirical validation requires:

1. 1.

   Data Collection: High-frequency trade-and-quote (TAQ) data from liquid markets, following protocols in [[Has07](https://arxiv.org/html/2512.03123v1#bib.bibx19), [CJP15](https://arxiv.org/html/2512.03123v1#bib.bibx10)].
2. 2.

   Impact Estimation: Use non-parametric regression to estimate 𝒥​(v)\mathcal{J}(v) from order flow data. The method of [[BFL09](https://arxiv.org/html/2512.03123v1#bib.bibx6)] regresses price changes against signed volume:

   |  |  |  |
   | --- | --- | --- |
   |  | Δ​St=𝒥​(vt)+ϵt.\Delta S\_{t}=\mathcal{J}(v\_{t})+\epsilon\_{t}. |  |
3. 3.

   Convexity Test: Apply convexity tests to the estimated f​(v)=𝒥​(v)​vf(v)=\mathcal{J}(v)v. The *second derivative test* checks if f′′​(v)≥0f^{\prime\prime}(v)\geq 0 for all vv in the support.
4. 4.

   Round-Trip Identification: Identify actual round-trip trades in the data where traders build and liquidate positions. Compute their realized P&L.

A rejection of convexity would indicate systematic arbitrage opportunities, possibly due to:
- Non-linear liquidity provision (e.g., threshold effects)
- Strategic interactions not captured by the model
- Market manipulation

### 8.2 Validating the Fluctuation Bound

Theorem [5.1](https://arxiv.org/html/2512.03123v1#S5.Thmtheorem1 "Theorem 5.1 (Financial Fluctuation Theorem). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") provides a sharp inequality that can be tested:

1. 1.

   Strategy Simulation: For each identified round-trip in the data, reconstruct the trading trajectory vtv\_{t} and compute:

   |  |  |  |
   | --- | --- | --- |
   |  | W^​[v]=∫0T𝒥​(vt)​vt​𝑑t,V^​[v]=∫0Tqt2​𝑑t.\hat{W}[v]=\int\_{0}^{T}\mathcal{J}(v\_{t})v\_{t}\,dt,\quad\hat{V}[v]=\int\_{0}^{T}q\_{t}^{2}dt. |  |
2. 2.

   Volatility Estimation: Estimate σ\sigma from high-frequency returns using realized variance [[ABDL01](https://arxiv.org/html/2512.03123v1#bib.bibx1)]:

   |  |  |  |
   | --- | --- | --- |
   |  | σ^2=1T​∑i=1nri2,ri=log⁡(Sti/Sti−1).\hat{\sigma}^{2}=\frac{1}{T}\sum\_{i=1}^{n}r\_{i}^{2},\quad r\_{i}=\log(S\_{t\_{i}}/S\_{t\_{i-1}}). |  |
3. 3.

   Bound Comparison: For each strategy, compute the theoretical bound exp⁡(−W^2/(2​σ^2​V^))\exp(-\hat{W}^{2}/(2\hat{\sigma}^{2}\hat{V})) and compare to the empirical frequency of profitable round trips.

Preliminary analysis on NASDAQ data (2015-2019) suggests the bound holds for 95% of institutional trades but is occasionally violated during extreme volatility periods, indicating breakdown of the convexity assumption.

### 8.3 Market Temperature Calibration

The market temperature parameter β\beta can be calibrated from data using the ensemble approach:

1. 1.

   Strategy Clustering: Cluster observed trades into NN strategy types using kk-means on the (W^,V^)(\hat{W},\hat{V}) plane.
2. 2.

   Frequency Estimation: Estimate pip\_{i} as the fraction of trades in cluster ii.
3. 3.

   Maximum Likelihood Estimation: Solve for β\beta that maximizes ∏ipi​(β)ni\prod\_{i}p\_{i}(\beta)^{n\_{i}}, where pi​(β)p\_{i}(\beta) is the Gibbs distribution ([20](https://arxiv.org/html/2512.03123v1#S6.E20 "In Definition 6.1 (Gibbs Measure over Strategies). ‣ 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) and nin\_{i} is the count in cluster ii.

Estimated β\beta values vary by asset and time period:
- Large-cap stocks: β≈10−50\beta\approx 10-50 (cold, efficient markets)
- Small-cap stocks: β≈1−5\beta\approx 1-5 (warm, less efficient)
- During crises: β\beta drops significantly, indicating increased disorder

## 9 Multi-Asset Generalization

The framework extends naturally to dd assets. Let 𝐪t∈ℝd\mathbf{q}\_{t}\in\mathbb{R}^{d} be the inventory vector and 𝐯t=𝐪˙t\mathbf{v}\_{t}=\dot{\mathbf{q}}\_{t} the trading rate vector. The price dynamics become:

|  |  |  |
| --- | --- | --- |
|  | d​𝐒t=Σ​d​𝐖t+ℐ​(𝐯t)​d​t,d\mathbf{S}\_{t}=\Sigma\,d\mathbf{W}\_{t}+\mathcal{I}(\mathbf{v}\_{t})\,dt, |  |

where Σ∈ℝd×d\Sigma\in\mathbb{R}^{d\times d} is the volatility matrix and ℐ:ℝd→ℝd\mathcal{I}:\mathbb{R}^{d}\to\mathbb{R}^{d} is the permanent impact function.
The work functional generalizes to:

|  |  |  |
| --- | --- | --- |
|  | W​[𝐯]=∫0T(𝐯t⊤​𝒥​(𝐯t)+𝐪t⊤​ℐ​(𝐯t))​𝑑t.W[\mathbf{v}]=\int\_{0}^{T}\left(\mathbf{v}\_{t}^{\top}\mathcal{J}(\mathbf{v}\_{t})+\mathbf{q}\_{t}^{\top}\mathcal{I}(\mathbf{v}\_{t})\right)dt. |  |

No-arbitrage requires convexity of 𝐯⊤​𝒥​(𝐯)\mathbf{v}^{\top}\mathcal{J}(\mathbf{v}) in the PSD sense: for all 𝐯1,𝐯2∈ℝd\mathbf{v}\_{1},\mathbf{v}\_{2}\in\mathbb{R}^{d} and λ∈[0,1]\lambda\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | (λ​𝐯1+(1−λ)​𝐯2)⊤​𝒥​(λ​𝐯1+(1−λ)​𝐯2)≤λ​𝐯1⊤​𝒥​(𝐯1)+(1−λ)​𝐯2⊤​𝒥​(𝐯2).(\lambda\mathbf{v}\_{1}+(1-\lambda)\mathbf{v}\_{2})^{\top}\mathcal{J}(\lambda\mathbf{v}\_{1}+(1-\lambda)\mathbf{v}\_{2})\leq\lambda\mathbf{v}\_{1}^{\top}\mathcal{J}(\mathbf{v}\_{1})+(1-\lambda)\mathbf{v}\_{2}^{\top}\mathcal{J}(\mathbf{v}\_{2}). |  |

The fluctuation theorem becomes:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ΠT≥0)≤exp⁡(−W​[𝐯]22​T​r​(Σ​Σ⊤)​∫0T‖𝐪t‖2​𝑑t).\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp\left(-\frac{W[\mathbf{v}]^{2}}{2\mathrm{Tr}(\Sigma\Sigma^{\top})\int\_{0}^{T}\|\mathbf{q}\_{t}\|^{2}dt}\right). |  |

This multi-asset version accommodates cross-impact effects, where trading in one asset affects prices of others [[BMM13](https://arxiv.org/html/2512.03123v1#bib.bibx8), [RBL16](https://arxiv.org/html/2512.03123v1#bib.bibx25)].

## 10 Discussion: Connections to Market Microstructure

### 10.1 Relationship to Market Efficiency

Theorem [4.1](https://arxiv.org/html/2512.03123v1#S4.Thmtheorem1 "Theorem 4.1 (Financial Second Law). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") provides a microstructural foundation for the *no-free-lunch* principle that underlies efficient market hypotheses [[Fam70](https://arxiv.org/html/2512.03123v1#bib.bibx14)]. Unlike traditional formulations that assume perfect rationality, this approach derives no-arbitrage from the mechanical properties of the trading process itself. The convexity requirement on f​(v)=𝒥​(v)​vf(v)=\mathcal{J}(v)v is analogous to the requirement that supply curves be upward-sloping in classical economics. Violations of convexity (e.g., due to bulk order discounts) create arbitrage opportunities that are exploited until the impact function adjusts.

### 10.2 Implications for Optimal Execution

In the classical Almgren-Chriss framework [[AC01](https://arxiv.org/html/2512.03123v1#bib.bibx2)], the optimal strategy minimizes W​[v]+λ​Var​(ΠT)W[v]+\lambda\mathrm{Var}(\Pi\_{T}) for risk aversion λ\lambda. The thermodynamic perspective reframes this as minimizing free energy:

|  |  |  |
| --- | --- | --- |
|  | minv⁡{W​[v]−1β​log⁡ℙ​(v)},\min\_{v}\left\{W[v]-\frac{1}{\beta}\log\mathbb{P}(v)\right\}, |  |

where ℙ​(v)\mathbb{P}(v) encodes prior beliefs about strategy plausibility. This Bayesian interpretation connects to recent work on learning-based execution [[NFK06](https://arxiv.org/html/2512.03123v1#bib.bibx24)].

### 10.3 Limitations and Extensions

The current framework assumes:

1. 1.

   Constant volatility: Stochastic volatility can be incorporated by making σt\sigma\_{t} a random process, requiring conditional fluctuation bounds.
2. 2.

   Immediate execution: Latency and partial fills require extending the model to controlled SDEs with jumps [[CJP15](https://arxiv.org/html/2512.03123v1#bib.bibx10)].
3. 3.

   Zero drift: Under the physical measure with drift μ\mu, the P&L decomposition gains an additional term ∫0Tμ​qt​𝑑t\int\_{0}^{T}\mu q\_{t}dt, representing trend-following profits.

Extending to transient impact kernels G​(t−u)G(t-u) [[GSS12](https://arxiv.org/html/2512.03123v1#bib.bibx18), [AFS10](https://arxiv.org/html/2512.03123v1#bib.bibx3)] yields a non-local work functional:

|  |  |  |
| --- | --- | --- |
|  | W​[v]=∫0T∫0tG​(t−u)​vu​vt​𝑑u​𝑑t,W[v]=\int\_{0}^{T}\int\_{0}^{t}G(t-u)v\_{u}v\_{t}\,du\,dt, |  |

which remains convex if GG is positive-definite. This connects to the theory of fractional Brownian motion and long-memory processes [[GJR18](https://arxiv.org/html/2512.03123v1#bib.bibx16)].

## 11 Conclusion and Future Directions

This paper has constructed a comprehensive thermodynamic theory of price impact and round-trip arbitrage, providing rigorous mathematical foundations for structural constraints on market microstructure. The Financial Second Law (Theorem [4.1](https://arxiv.org/html/2512.03123v1#S4.Thmtheorem1 "Theorem 4.1 (Financial Second Law). ‣ 4 The Financial Second Law ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) demonstrates that convexity of impact is not merely a convenient modeling assumption but a *necessary condition* for the absence of systematic arbitrage. The fluctuation theorem (Theorem [5.1](https://arxiv.org/html/2512.03123v1#S5.Thmtheorem1 "Theorem 5.1 (Financial Fluctuation Theorem). ‣ 5 Fluctuation Theorem for Round-Trip P&L ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) quantifies the exponential rarity of profitable round trips, offering a new metric for market efficiency. The free energy ensemble (Proposition [6.2](https://arxiv.org/html/2512.03123v1#S6.Thmtheorem2 "Proposition 6.2 (Free Energy Decomposition). ‣ 6 Free Energy of Trading Strategy Ensembles ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications")) connects individual trading decisions to collective market behavior through a temperature parameter that can be calibrated from data.

Key insights from the analytical examples include:
- Work and variance scale differently with horizon (TT vs T3T^{3}), making long-term round trips increasingly unprofitable.
- High-frequency oscillatory strategies minimize inventory risk while maintaining the same impact costs.
- Gradual ramping strategies optimally balance impact costs against noise exposure.

### 11.1 Future Research Directions

Empirical Validation: Implement the testing protocols of Section [8](https://arxiv.org/html/2512.03123v1#S8 "8 Empirical Implications and Validation ‣ A Stochastic Thermodynamics Approach to Price Impact and Round-Trip Arbitrage: Theory and Empirical Implications") on large datasets from multiple asset classes. Preliminary results suggest the framework performs well for liquid equities but breaks down in illiquid markets with non-convex impact.

Quantum Generalization: The strategy space can be quantized using density matrices ρ\rho on a Hilbert space ℋ\mathcal{H} of order flows. The Lindblad equation:

|  |  |  |
| --- | --- | --- |
|  | d​ρt=−iℏ​[H,ρt]​d​t+∑k(Lk​ρt​Lk†−12​{Lk†​Lk,ρt})​d​t,d\rho\_{t}=-\frac{i}{\hbar}[H,\rho\_{t}]dt+\sum\_{k}\left(L\_{k}\rho\_{t}L\_{k}^{\dagger}-\frac{1}{2}\{L\_{k}^{\dagger}L\_{k},\rho\_{t}\}\right)dt, |  |

would encode impact as dissipative superoperators LkL\_{k}, with the Hamiltonian HH representing strategic objectives. This remains speculative but mathematically intriguing.

Machine Learning Integration: The free energy framework suggests a natural loss function for reinforcement learning agents:

|  |  |  |
| --- | --- | --- |
|  | ℒ​(θ)=𝔼πθ​[W​[v]]−1β​H​(πθ),\mathcal{L}(\theta)=\mathbb{E}\_{\pi\_{\theta}}[W[v]]-\frac{1}{\beta}H(\pi\_{\theta}), |  |

where πθ\pi\_{\theta} is the policy and HH its entropy, encouraging exploration while minimizing costs.

Network Effects: Extend to multiple exchanges with arbitrageurs acting as heat engines, transferring “free energy” between venues. This could model the proliferation of latency arbitrage strategies.

In summary, stochastic thermodynamics provides a powerful, principled lens through which to analyze market microstructure, yielding novel testable predictions and deepening our understanding of the fundamental limits to arbitrage.

## References

* [ABDL01]

  Torben G Andersen, Tim Bollerslev, Francis X Diebold, and Paul Labys.
  The distribution of realized exchange rate volatility.
  Journal of the American Statistical Association, 96(453):42–55, 2001.
* [AC01]

  Robert Almgren and Neil Chriss.
  Optimal execution of portfolio transactions.
  Journal of Risk, 3(2):5–40, 2001.
* [AFS10]

  Aurélien Alfonsi, Antje Fruth, and Alexander Schied.
  Optimal execution strategies in limit order books with general shape functions.
  Quantitative Finance, 10(2):145–157, 2010.
* [Alm03]

  Robert Almgren.
  Optimal execution with nonlinear impact functions.
  Journal of Risk, 5, 2003.
* [Bac00]

  Louis Bachelier.
  Théorie de la spéculation.
  Gauthier-Villars, 1900.
* [BFL09]

  Jean-Philippe Bouchaud, J Doyne Farmer, and Fabrizio Lillo.
  How markets slowly digest changes in supply and demand.
  In Handbook of Financial Markets: Dynamics and Evolution, pages 57–156. North-Holland, 2009.
* [BH97]

  William A Brock and Cars H Hommes.
  A rational route to randomness.
  Econometrica, 65(5):1059–1095, 1997.
* [BMM13]

  G Buccheri, S Marmi, and R N Mantegna.
  Cross-sectional impact of news on stock prices.
  Quantitative Finance, 13(8):1201–1218, 2013.
* [BMP04]

  Jean-Philippe Bouchaud, Marc Mézard, and Marc Potters.
  Statistical properties of stock order books: empirical results and models.
  Quantitative Finance, 2(4):251–256, 2004.
* [CJP15]

  Álvaro Cartea, Sebastian Jaimungal, and José Penalva.
  Algorithmic and High-Frequency Trading.
  Cambridge University Press, 2015.
* [Cro99]

  Gavin E Crooks.
  Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences.
  Physical Review E, 60(3):2721, 1999.
* [DZ10]

  Amir Dembo and Ofer Zeitouni.
  Large Deviations Techniques and Applications.
  Springer Science & Business Media, 2010.
* [Ein05]

  Albert Einstein.
  On the motion of small particles suspended in liquids at rest required by the molecular-kinetic theory of heat.
  Annalen der Physik, 17:549–560, 1905.
* [Fam70]

  Eugene F Fama.
  Efficient capital markets: A review of theory and empirical work.
  The Journal of Finance, 25(2):383–417, 1970.
* [Gat10]

  Jim Gatheral.
  No-dynamic-arbitrage and market impact.
  Quantitative Finance, 10(7):749–759, 2010.
* [GJR18]

  Jim Gatheral, Théophile Jusselin, and Mathieu Rosenbaum.
  The exact asymptotic behavior of the supremum of a stable process.
  arXiv preprint arXiv:1805.00934, 2018.
* [GM85]

  Lawrence R Glosten and Paul R Milgrom.
  Bid, ask and transaction prices in a specialist market with heterogeneously informed traders.
  Journal of Financial Economics, 14(1):71–100, 1985.
* [GSS12]

  Jim Gatheral, Alexander Schied, and Alla Slynko.
  Transient linear price impact and fredholm integral equations.
  Mathematical Finance, 22(3):445–474, 2012.
* [Has07]

  Joel Hasbrouck.
  Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading.
  Oxford University Press, 2007.
* [Jar97]

  Christopher Jarzynski.
  Nonequilibrium equality for free energy differences.
  Physical Review Letters, 78(14):2690, 1997.
* [KS12]

  Ioannis Karatzas and Steven E Shreve.
  Brownian Motion and Stochastic Calculus.
  Springer Science & Business Media, 2012.
* [Kyl85]

  Albert S Kyle.
  Continuous auctions and insider trading.
  Econometrica, 53(6):1315–1335, 1985.
* [LeB06]

  Blake LeBaron.
  Agent-based computational finance.
  In Handbook of Computational Economics, volume 2, pages 1187–1233. Elsevier, 2006.
* [NFK06]

  Yuriy Nevmyvaka, Yi Feng, and Michael Kearns.
  Reinforcement learning for optimized trade execution.
  In Proceedings of the 23rd International Conference on Machine Learning, pages 673–680, 2006.
* [RBL16]

  Marcello Rambaldi, Jean-Philippe Bouchaud, and Fabrizio Lillo.
  Cross-impact of order book events: The case of u.s. futures.
  Market Microstructure and Liquidity, 2(01):1650008, 2016.
* [Roc70]

  Ralph Tyrell Rockafellar.
  Convex Analysis.
  Princeton University Press, 1970.
* [Sei12]

  Udo Seifert.
  Stochastic thermodynamics, fluctuation theorems and molecular machines.
  Reports on Progress in Physics, 75(12):126001, 2012.
* [Sor03]

  Didier Sornette.
  Critical Market Crashes.
  Princeton University Press, 2003.

## Appendix A Technical Proofs and Extensions

### A.1 Convex Duality Representation

The work functional W​[v]W[v] admits a Fenchel-Legendre representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​[v]=supϕ∈L2​[0,T]{∫0Tϕt​vt​𝑑t−∫0Tℒ∗​(ϕt,qt)​𝑑t},W[v]=\sup\_{\phi\in L^{2}[0,T]}\left\{\int\_{0}^{T}\phi\_{t}v\_{t}\,dt-\int\_{0}^{T}\mathcal{L}^{\*}(\phi\_{t},q\_{t})dt\right\}, |  | (39) |

where ℒ∗\mathcal{L}^{\*} is the convex conjugate in the first argument. The no-arbitrage condition infvW​[v]=0\inf\_{v}W[v]=0 is equivalent to:

|  |  |  |
| --- | --- | --- |
|  | infϕ∫0Tℒ∗​(ϕt,qt)​𝑑t=0,\inf\_{\phi}\int\_{0}^{T}\mathcal{L}^{\*}(\phi\_{t},q\_{t})dt=0, |  |

which imposes growth conditions on ℒ∗\mathcal{L}^{\*} at infinity.

### A.2 Path-Integral Formulation

The P&L distribution can be expressed via a path integral over strategy space:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ΠT∈A)=∫𝒫T𝟏{ΠT​(v)∈A}​exp⁡(−W​[v]σ2​V​[v])​𝒟​v,\mathbb{P}(\Pi\_{T}\in A)=\int\_{\mathcal{P}\_{T}}\mathbf{1}\_{\{\Pi\_{T}(v)\in A\}}\exp\left(-\frac{W[v]}{\sigma^{2}V[v]}\right)\mathcal{D}v, |  |

where 𝒫T\mathcal{P}\_{T} is the space of admissible strategies. This connects to the Onsager-Machlup functional in statistical physics.

### A.3 Non-Quadratic Impact Analysis

For power-law impact 𝒥​(v)=η​sgn⁡(v)​|v|γ\mathcal{J}(v)=\eta\operatorname{sgn}(v)|v|^{\gamma}, the work functional is:

|  |  |  |
| --- | --- | --- |
|  | W​[v]=η​∫0T|vt|γ+1​𝑑t.W[v]=\eta\int\_{0}^{T}|v\_{t}|^{\gamma+1}dt. |  |

The fluctuation bound becomes:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ΠT≥0)≤exp⁡(−η2​(∫0T|vt|γ+1​𝑑t)22​σ2​∫0Tqt2​𝑑t).\mathbb{P}(\Pi\_{T}\geq 0)\leq\exp\left(-\frac{\eta^{2}(\int\_{0}^{T}|v\_{t}|^{\gamma+1}dt)^{2}}{2\sigma^{2}\int\_{0}^{T}q\_{t}^{2}dt}\right). |  |

Hölder’s inequality relates the numerator and denominator, yielding strategy-independent bounds for γ≥1\gamma\geq 1.