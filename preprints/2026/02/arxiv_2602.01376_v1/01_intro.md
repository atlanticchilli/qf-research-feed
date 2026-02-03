---
authors:
- Mark Higgins
doc_id: arxiv:2602.01376v1
family_id: arxiv:2602.01376
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and
  Exotic Pricing
url_abs: http://arxiv.org/abs/2602.01376v1
url_html: https://arxiv.org/html/2602.01376v1
venue: arXiv q-fin
version: 1
year: 2026
---


Mark Higgins
  
mghiggins@yahoo.com

###### Abstract

We consider a novel use case for the Double Heston model (Christoffersen et al., [2009](https://arxiv.org/html/2602.01376v1#bib.bib9 "The shape and term structure of the index option smirk: why multifactor stochastic volatility models work so well")), where the two Heston sub-variances have different spot/volatility correlations but the same volatility of volatility and mean reversion speed.

This parameterization generalizes the traditional Heston stochastic volatility model (Heston, [1993](https://arxiv.org/html/2602.01376v1#bib.bib2 "A closed-form solution for options with stochastic volatility with applications to bond and currency options")) to include stochastic spot/volatility correlation. It is an affine model, allowing European options to be priced efficiently by numerically integrating over a closed-form characteristic function.

This model incorporates a key dynamic relevant for pricing barrier derivatives in the foreign exchange markets: a positive correlation between moves in implied volatility skew and moves in the spot price. We analyze that correlation and its impact on both barrier option pricing and volatility swap pricing. Those price impacts are comparable to or larger than the bid/ask spreads for these products.

Adding stochastic spot/volatility correlation increases the prices of out-of-the-money knockout options and one touch options, assuming that the model is calibrated to market vanilla option prices. It also increases the fair strike of volatility swaps compared to the Heston model.

## 1 Introduction

The Heston stochastic volatility model is a standard extension to the Black-Scholes model (Black and Scholes, [1973](https://arxiv.org/html/2602.01376v1#bib.bib1 "The pricing of options and corporate liabilities")) that allows the instantaneous volatility of the asset spot price to be stochastic and mean reverting, capturing an important real world dynamic for most financial markets.

One Heston model parameter is the spot/volatility correlation, which defines the expected move in instantaneous volatility for a given move in the asset spot price. A positive correlation leads to an upward-sloping implied volatility skew, and vice versa.

In the Heston model this correlation parameter is a constant. In practice, however, this correlation does vary over time, and moves in that correlation can themselves be well correlated with moves in the spot price.

That dynamic - the correlation of the spot/volatility correlation with the spot price - is important in practice for the pricing of barrier derivatives such as knockout options and one touch options (sometimes called American digital options). This is particularly relevant in the foreign exchange options markets where that correlation is significant and barrier derivatives are relatively liquid.

In this paper we cleanly generalize the Heston model to include stochastic spot/volatility correlation. We analyze volatility skew dynamics in the foreign exchange options markets to estimate the size of this effect. We also discuss how the pricing of barrier derivatives and volatility swaps is affected by this correlation, developing intuition for the impact based on hedging arguments and quantifying the price impact compared to the Heston model.

An important result is that adding stochastic spot/volatility correlation increases the prices of one touch and out-of-the-money knockout options on a scale comparable to or larger than the bid/ask spread for these derivatives, assuming the model is calibrated to market vanilla option prices. Similarly, it meaningfully increases the fair strikes of volatility swaps. Market makers using the Heston model to price and manage risk for these derivatives may find themselves selling these derivatives at below-market prices and accumulating mispriced short positions.

## 2 The Model

We define a generalization of the Heston stochastic volatility model as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt\displaystyle\frac{dS\_{t}}{S\_{t}} | =(r−q)​d​t+vt​d​WtS\displaystyle=(r-q)\,dt+\sqrt{v\_{t}}\,dW^{S}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | vt​d​WtS\displaystyle\sqrt{v\_{t}}dW^{S}\_{t} | =vt+​d​WtS++vt−​d​WtS−\displaystyle=\sqrt{v^{+}\_{t}}dW^{S+}\_{t}+\sqrt{v^{-}\_{t}}dW^{S-}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | vt\displaystyle v\_{t} | =vt++vt−\displaystyle=v^{+}\_{t}+v^{-}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​vt+\displaystyle dv^{+}\_{t} | =β​(θ+−vt+)​d​t+α​vt+​d​Wt+\displaystyle=\beta(\theta\_{+}-v^{+}\_{t})\,dt+\alpha\sqrt{v^{+}\_{t}}\,dW^{+}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​vt−\displaystyle dv^{-}\_{t} | =β​(θ−−vt−)​d​t+α​vt−​d​Wt−\displaystyle=\beta(\theta\_{-}-v^{-}\_{t})\,dt+\alpha\sqrt{v^{-}\_{t}}\,dW^{-}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨WS+,W+⟩t\displaystyle d\langle W^{S+},W^{+}\rangle\_{t} | =(ρ¯+η)​d​t\displaystyle=(\bar{\rho}+\eta)\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨WS−,W−⟩t\displaystyle d\langle W^{S-},W^{-}\rangle\_{t} | =(ρ¯−η)​d​t\displaystyle=(\bar{\rho}-\eta)\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨W+,W−⟩t\displaystyle d\langle W^{+},W^{-}\rangle\_{t} | =d​⟨WS+,WS−⟩t=d​⟨WS+,W−⟩t=d​⟨WS−,W+⟩t=0\displaystyle=d\langle W^{S+},W^{S-}\rangle\_{t}=d\langle W^{S+},W^{-}\rangle\_{t}=d\langle W^{S-},W^{+}\rangle\_{t}=0 |  |

StS\_{t} is the asset spot price (“spot”) and vtv\_{t} is the instantaneous volatility squared, often called the “variance”, which equals the sum of the two sub-variance processes vt+v^{+}\_{t} and vt−v^{-}\_{t}. Those two processes share a mean reversion strength β\beta and volatility of volatility α\alpha, but have different spot/volatility correlations. v+v^{+} has a more positive correlation, equal to the average correlation ρ¯\bar{\rho} plus the correlation half-range η\eta. v−v^{-} has a more negative correlation, equal to the average correlation ρ¯\bar{\rho} minus η\eta. Naturally, ρ¯−η>−1\bar{\rho}-\eta>-1 and ρ¯+η<1\bar{\rho}+\eta<1 to keep all correlations in (−1,1)(-1,1).

This is how correlation becomes stochastic in this model: by changing the weights of the two sub-variance processes and thereby letting the correlation range between ρ¯−η\bar{\rho}-\eta and ρ¯+η\bar{\rho}+\eta.

This model naturally induces a positive correlation between moves in spot and moves in the spot/volatility correlation: as spot increases, the sub-variance process with the higher correlation will tend to increase more than the sub-variance process with the lower correlation, and the instantaneous spot/volatility correlation will get closer to the higher correlation.

As the parameter η\eta goes to zero the model reduces to the original Heston stochastic volatility model with constant spot/volatility correlation ρ¯\bar{\rho}. In this sense, η\eta is a kind of volatility of correlation.

We can also rewrite the SDE for d​StSt\frac{dS\_{t}}{S\_{t}} in terms of just three uncorrelated Brownian motions Wt0W^{0}\_{t}, Wt+W^{+}\_{t}, and Wt−W^{-}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt\displaystyle\frac{dS\_{t}}{S\_{t}} | =(r−q)​d​t\displaystyle=(r-q)\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +((ρ¯+η)​vt+​d​Wt++(ρ¯−η)​vt−​d​Wt−+(1−(ρ¯+η)2)​vt++(1−(ρ¯−η)2)​vt−​d​Wt0)\displaystyle+\left((\bar{\rho}+\eta)\sqrt{v\_{t}^{+}}\,\mathrm{d}W\_{t}^{+}+(\bar{\rho}-\eta)\sqrt{v\_{t}^{-}}\,\mathrm{d}W\_{t}^{-}+\sqrt{(1-(\bar{\rho}+\eta)^{2})v\_{t}^{+}+(1-(\bar{\rho}-\eta)^{2})v\_{t}^{-}}\,\mathrm{d}W\_{t}^{0}\right) |  |

which is convenient for Monte Carlo simulation and demonstrates the three driving factors in this model.

Note that this is a version of the Double Heston model (Christoffersen et al., [2009](https://arxiv.org/html/2602.01376v1#bib.bib9 "The shape and term structure of the index option smirk: why multifactor stochastic volatility models work so well")). That model was designed for matching a full term structure of implied volatilities because the two sub-variances have different mean reversion speeds and affect different parts of the term structure. In this case we have the same mean reversion speed for both sub-variances, but different spot/volatility correlations.

## 3 The Variance Process

Our model defines the processes for the two sub-variances; we can use those to write down the SDE for the total variance vt=vt++vt−v\_{t}=v\_{t}^{+}+v\_{t}^{-}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​vt\displaystyle\mathrm{d}v\_{t} | =d​vt++d​vt−\displaystyle=dv^{+}\_{t}+dv^{-}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =β​(θ+−vt+)​d​t+α​vt+​d​Wt++β​(θ−−vt−)​d​t+α​vt−​d​Wt−\displaystyle=\beta(\theta\_{+}-v\_{t}^{+})\,dt+\alpha\sqrt{v^{+}\_{t}}\,dW^{+}\_{t}+\beta(\theta\_{-}-v\_{t}^{-})\,dt+\alpha\sqrt{v^{-}\_{t}}\,dW^{-}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =β​(θ−vt)​d​t+α​(vt+​d​Wt++vt−​d​Wt−)\displaystyle=\beta(\theta-v\_{t})\,dt+\alpha\left(\sqrt{v^{+}\_{t}}\,dW^{+}\_{t}+\sqrt{v^{-}\_{t}}\,dW^{-}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =β​(θ−vt)​d​t+α​vt​d​Wtv\displaystyle=\beta(\theta-v\_{t})\,dt+\alpha\sqrt{v\_{t}}\,dW\_{t}^{v} |  |

where θ=θ++θ−\theta=\theta\_{+}+\theta\_{-} is the long run variance level. This is exactly the Heston/CIR variance SDE, so this model reproduces the Heston model’s marginal variance dynamics.

## 4 The Spot/Volatility Correlation

A key feature of our model is the stochastic spot/volatility correlation. To calculate that correlation, we first compute the instantaneous covariation between Xt=ln⁡StX\_{t}=\ln S\_{t} and the total variance vt=vt++vt−v\_{t}=v\_{t}^{+}+v\_{t}^{-}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨X,v⟩t\displaystyle\mathrm{d}\langle X,v\rangle\_{t} | =d​⟨X,v++v−⟩t=d​⟨X,v+⟩t+d​⟨X,v−⟩t\displaystyle=\mathrm{d}\langle X,v^{+}+v^{-}\rangle\_{t}=\mathrm{d}\langle X,v^{+}\rangle\_{t}+\mathrm{d}\langle X,v^{-}\rangle\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =α​(ρ¯+η)​vt+​d​t+α​(ρ¯−η)​vt−​d​t.\displaystyle=\alpha(\bar{\rho}+\eta)v\_{t}^{+}\,\mathrm{d}t+\alpha(\bar{\rho}-\eta)v\_{t}^{-}\,\mathrm{d}t. |  |

Define the spot/variance covariance factor

|  |  |  |
| --- | --- | --- |
|  | ct:=(ρ¯+η)​vt++(ρ¯−η)​vt−=ρ¯​vt+η​(vt+−vt−)=ρ¯​vt+η​ut,c\_{t}:=(\bar{\rho}+\eta)v\_{t}^{+}+(\bar{\rho}-\eta)v\_{t}^{-}=\bar{\rho}\,v\_{t}+\eta(v\_{t}^{+}-v\_{t}^{-})=\bar{\rho}\,v\_{t}+\eta u\_{t}, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | d​⟨X,v⟩t=α​ct​d​t.\mathrm{d}\langle X,v\rangle\_{t}=\alpha c\_{t}\,\mathrm{d}t. |  |

Define the instantaneous spot/volatility correlation (between WSW^{S} and the Brownian driver of vtv\_{t}) by the identity

|  |  |  |
| --- | --- | --- |
|  | d​⟨X,v⟩t=α​vt​ρt​d​t,\mathrm{d}\langle X,v\rangle\_{t}=\alpha v\_{t}\rho\_{t}\,\mathrm{d}t, |  |

which gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt=ctvt=ρ¯+ηutvt=ρ¯+ηvt+−vt−vt++vt−.\boxed{\rho\_{t}=\frac{c\_{t}}{v\_{t}}=\bar{\rho}+\eta\,\frac{u\_{t}}{v\_{t}}=\bar{\rho}+\eta\,\frac{v\_{t}^{+}-v\_{t}^{-}}{v\_{t}^{+}+v\_{t}^{-}}.} |  | (1) |

That is, when the difference between the two sub-variance processes is zero, ρt=ρ¯\rho\_{t}=\bar{\rho}. When v+≫v−v^{+}\gg v^{-}, ρt=ρ¯+η\rho\_{t}=\bar{\rho}+\eta, and when v−≫v+v^{-}\gg v^{+}, ρt=ρ¯−η\rho\_{t}=\bar{\rho}-\eta. So the spot/volatility correlation is constrained to the range ρ¯−η\bar{\rho}-\eta to ρ¯+η\bar{\rho}+\eta, as the sub-variances are always non-negative.

## 5 Model Parameterization and Correlation Structure

There are two ways in this model to define the correlation structure: ρ¯\bar{\rho} and η\eta, which control the allowed range of the spot/volatility correlation; and θ+\theta\_{+} and θ−\theta\_{-}, which control the mean reversion levels of the two sub-variance processes. The long run values of v+v^{+} and v−v^{-} are θ+\theta\_{+} and θ−\theta\_{-}, respectively, so the long run correlation is

|  |  |  |
| --- | --- | --- |
|  | ρa=ρ¯+η​(θ+−θ−)θ\rho\_{a}=\bar{\rho}+\eta\frac{(\theta\_{+}-\theta\_{-})}{\theta} |  |

The instantaneous correlation is

|  |  |  |
| --- | --- | --- |
|  | ρ0=ρ¯+η​(v0+−v0−)v0\rho\_{0}=\bar{\rho}+\eta\frac{(v^{+}\_{0}-v^{-}\_{0})}{v\_{0}} |  |

where v0+v^{+}\_{0} and v0−v^{-}\_{0} are the initial values of the two sub-variance processes. On expectation ρt\rho\_{t} varies between these two levels, starting at ρ0\rho\_{0} and mean reverting to ρa\rho\_{a} (not ρ¯\bar{\rho}).

In this paper we look at calibrating just to a single expiration tenor at a time, so we are less concerned with the term structure of correlation. For this purpose we set v0+=θ+v^{+}\_{0}=\theta\_{+} and v0−=θ−v^{-}\_{0}=\theta\_{-} so that the initial correlation matches the long run correlation.

We choose then to parameterize the model in terms of θ=θ++θ−\theta=\theta\_{+}+\theta\_{-}, ρa\rho\_{a}, and ρ0\rho\_{0}, from which we can calculate θ+\theta\_{+}, θ−\theta\_{-}, v0+v^{+}\_{0}, and v0−v^{-}\_{0}. This is a more natural parameterization: θ\sqrt{\theta} is the long run volatility level, ρa\rho\_{a} is the long run correlation level, and ρ0\rho\_{0} is the initial correlation level. We generally choose ρ¯=ρa\bar{\rho}=\rho\_{a}, and when calibrating to a single expiration tenor assume ρ0=ρa\rho\_{0}=\rho\_{a} also, which implies θ+=θ−=v0+=v0−=θ/2\theta\_{+}=\theta\_{-}=v^{+}\_{0}=v^{-}\_{0}=\theta/2. This parameterization centers the allowed correlation range at the initial correlation level and ensures that in the η→0\eta\rightarrow 0 limit the current correlation is always in the allowed range.

## 6 The Stochastic Differential Equation for ρt\rho\_{t}

We can apply Ito’s Lemma to equation [1](https://arxiv.org/html/2602.01376v1#S4.E1 "In 4 The Spot/Volatility Correlation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") for ρt\rho\_{t} to find the SDE that ρt\rho\_{t} satisfies. Write vt=vt++vt−v\_{t}=v\_{t}^{+}+v\_{t}^{-} and ut=vt+−vt−u\_{t}=v\_{t}^{+}-v\_{t}^{-}. Then

|  |  |  |
| --- | --- | --- |
|  | ρt=ρ¯+η​utvt⟹utvt=ρt−ρ¯η.\rho\_{t}=\bar{\rho}+\eta\,\frac{u\_{t}}{v\_{t}}\qquad\Longrightarrow\qquad\frac{u\_{t}}{v\_{t}}=\frac{\rho\_{t}-\bar{\rho}}{\eta}. |  |

Using the (independent) Brownian drivers (W+,W−)(W^{+},W^{-}) for (v+,v−)(v^{+},v^{-}), one finds

|  |  |  |
| --- | --- | --- |
|  | d​vt=β​(θ−vt)​d​t+α​(vt+​d​Wt++vt−​d​Wt−),d​ut=β​((θ+−θ−)−ut)​d​t+α​(vt+​d​Wt+−vt−​d​Wt−)\mathrm{d}v\_{t}=\beta(\theta-v\_{t})\,\mathrm{d}t+\alpha\left(\sqrt{v\_{t}^{+}}\,\mathrm{d}W\_{t}^{+}+\sqrt{v\_{t}^{-}}\,\mathrm{d}W\_{t}^{-}\right),\quad\mathrm{d}u\_{t}=\beta\left((\theta\_{+}-\theta\_{-})-u\_{t}\right)\,\mathrm{d}t+\alpha\left(\sqrt{v\_{t}^{+}}\,\mathrm{d}W\_{t}^{+}-\sqrt{v\_{t}^{-}}\,\mathrm{d}W\_{t}^{-}\right) |  |

Applying Ito to ut/vtu\_{t}/v\_{t} gives a drift

|  |  |  |
| --- | --- | --- |
|  | β​θvt​(ρa−ρt)​d​t\frac{\beta\theta}{v\_{t}}(\rho\_{a}-\rho\_{t})\,\mathrm{d}t |  |

where we used θ+−θ−=θ​(ρa−ρ¯)/η\theta\_{+}-\theta\_{-}=\theta\,(\rho\_{a}-\bar{\rho})/\eta, and an instantaneous variance

|  |  |  |
| --- | --- | --- |
|  | d​⟨ρ,ρ⟩t=α2vt​(η2−(ρt−ρ¯)2)​d​t.\mathrm{d}\langle\rho,\rho\rangle\_{t}=\frac{\alpha^{2}}{v\_{t}}\left(\eta^{2}-(\rho\_{t}-\bar{\rho})^{2}\right)\,\mathrm{d}t. |  |

Therefore, there exists a Brownian motion WρW^{\rho} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ρt=β​θvt​(ρa−ρt)​d​t+αvt​η2−(ρt−ρ¯)2​d​Wtρ\boxed{\mathrm{d}\rho\_{t}=\beta\frac{\theta}{v\_{t}}(\rho\_{a}-\rho\_{t})\,\mathrm{d}t+\frac{\alpha}{\sqrt{v\_{t}}}\sqrt{\eta^{2}-(\rho\_{t}-\bar{\rho})^{2}}\,\mathrm{d}W\_{t}^{\rho}} |  | (2) |

This looks like a process that mean reverts to ρa\rho\_{a} with a variable speed determined by β​θvt\beta\frac{\theta}{v\_{t}}; thus, the mean reversion speed for ρt\rho\_{t} is quite similar to the volatility mean reversion speed. When ρt=ρ¯\rho\_{t}=\bar{\rho}, the ”volatility of correlation” is α​ηvt\frac{\alpha\eta}{\sqrt{v\_{t}}} - that is, proportional to η\eta.

This process constrains ρt\rho\_{t} to lie in the range ρ¯−η\bar{\rho}-\eta to ρ¯+η\bar{\rho}+\eta - its volatility goes to zero at those edges - but that was already clear from the definition of ρt\rho\_{t}.

## 7 Spot/Rho Correlation

The key market dynamic that we are introducing with this model is the correlation of moves in the asset spot price with moves in the spot/volatility correlation. This “spot/rho correlation” ρc​s\rho\_{cs} is positive in this model: as spot increases, the sub-variance process with the more positive correlation tends to increase in comparison to the one with more negative correlation, and the instantaneous correlation (per equation [1](https://arxiv.org/html/2602.01376v1#S4.E1 "In 4 The Spot/Volatility Correlation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing")) tends to turn more positive as well.

We can use the SDE for ρt\rho\_{t} from equation [2](https://arxiv.org/html/2602.01376v1#S6.E2 "In 6 The Stochastic Differential Equation for 𝜌_𝑡 ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") to quantify the covariance between moves in the log spot price Xt=ln⁡(St)X\_{t}=\ln(S\_{t}) and moves in ρt\rho\_{t}:

|  |  |  |
| --- | --- | --- |
|  | d​⟨X,ρ⟩t=α​(η2−(ρ¯−ρt)2)​d​td\langle X,\rho\rangle\_{t}=\alpha(\eta^{2}-(\bar{\rho}-\rho\_{t})^{2})dt |  |

And the instantaneous variance of ρt\rho\_{t} is

|  |  |  |
| --- | --- | --- |
|  | d​⟨ρ,ρ⟩t=α2vt​(η2−(ρ¯−ρt)2)​d​td\langle\rho,\rho\rangle\_{t}=\frac{\alpha^{2}}{v\_{t}}(\eta^{2}-(\bar{\rho}-\rho\_{t})^{2})dt |  |

The instantaneous variance of XtX\_{t} is just vt​d​tv\_{t}dt. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρc​s=Corr​(d​Xt,d​ρt)=η2−(ρ¯−ρt)2\boxed{\rho\_{cs}=\mathrm{Corr}(\mathrm{d}X\_{t},\mathrm{d}\rho\_{t})=\sqrt{\eta^{2}-(\bar{\rho}-\rho\_{t})^{2}}} |  | (3) |

When ρt=ρ¯\rho\_{t}=\bar{\rho} this simplifies to η\eta: this parameter controls both the volatility of correlation and the spot/rho correlation.

## 8 European Vanilla Option Pricing

We will follow the same approach to pricing European vanilla prices as in the Heston model derivation, by finding a closed-form expression for the characteristic function of XT=ln⁡(ST)X\_{T}=\ln(S\_{T}) on the option expiration date TT.

### 8.1 Affine Generator in State (x,v+,v−)(x,v^{+},v^{-})

Let Xt=ln⁡StX\_{t}=\ln S\_{t}. Using the independent Brownian drivers (W+,W−,W0)(W^{+},W^{-},W^{0}) and the dynamics above, the nonzero instantaneous covariations involving the state are:

|  |  |  |
| --- | --- | --- |
|  | d​⟨X,X⟩t=(v++v−)​d​t,d​⟨v+,v+⟩t=α2​v+​d​t,d​⟨v−,v−⟩t=α2​v−​d​t,\mathrm{d}\langle X,X\rangle\_{t}=(v^{+}+v^{-})\mathrm{d}t,\quad\mathrm{d}\langle v^{+},v^{+}\rangle\_{t}=\alpha^{2}v^{+}\mathrm{d}t,\quad\mathrm{d}\langle v^{-},v^{-}\rangle\_{t}=\alpha^{2}v^{-}\mathrm{d}t, |  |

|  |  |  |
| --- | --- | --- |
|  | d​⟨X,v+⟩t=α​(ρ¯+η)​v+​d​t,d​⟨X,v−⟩t=α​(ρ¯−η)​v−​d​t.\mathrm{d}\langle X,v^{+}\rangle\_{t}=\alpha(\bar{\rho}+\eta)v^{+}\mathrm{d}t,\quad\mathrm{d}\langle X,v^{-}\rangle\_{t}=\alpha(\bar{\rho}-\eta)v^{-}\mathrm{d}t. |  |

Hence the backward operator ℒ\mathcal{L} acting on smooth f​(x,v+,v−)f(x,v^{+},v^{-}) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​f\displaystyle\mathcal{L}f | =(r−q−12​(v++v−))​fx+β​(θ+−v+)​fv++β​(θ−−v−)​fv−\displaystyle=\left(r-q-\tfrac{1}{2}(v^{+}+v^{-})\right)f\_{x}+\beta(\theta\_{+}-v^{+})f\_{v^{+}}+\beta(\theta\_{-}-v^{-})f\_{v^{-}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​(v++v−)​fx​x+12​α2​v+​fv+​v++12​α2​v−​fv−​v−\displaystyle\quad+\tfrac{1}{2}(v^{+}+v^{-})f\_{xx}+\tfrac{1}{2}\alpha^{2}v^{+}f\_{v^{+}v^{+}}+\tfrac{1}{2}\alpha^{2}v^{-}f\_{v^{-}v^{-}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +α​(ρ¯+η)​v+​fx​v++α​(ρ¯−η)​v−​fx​v−.\displaystyle\quad+\alpha(\bar{\rho}+\eta)v^{+}f\_{xv^{+}}+\alpha(\bar{\rho}-\eta)v^{-}f\_{xv^{-}}. |  |

All coefficients are affine in (v+,v−)(v^{+},v^{-}).

### 8.2 Exponential-Affine Ansatz and Riccati System

For ξ∈ℂ\xi\in\mathbb{C}, define the characteristic function as

|  |  |  |
| --- | --- | --- |
|  | Φ​(t,x,v+,v−;ξ)=𝔼​[ei​ξ​XT∣Xt=x,vt+=v+,vt−=v−]\Phi(t,x,v^{+},v^{-};\xi)=\mathbb{E}\!\left[e^{i\xi X\_{T}}\mid X\_{t}=x,\ v\_{t}^{+}=v^{+},\ v\_{t}^{-}=v^{-}\right] |  |

and define the remaining time to expiration τ=T−t\tau=T-t.
Use the affine form

|  |  |  |
| --- | --- | --- |
|  | Φ=exp⁡(A​(τ;ξ)+B+​(τ;ξ)​v++B−​(τ;ξ)​v−+i​ξ​x),A​(τ=0)=B+​(0)=B−​(0)=0.\Phi=\exp\!\left(A(\tau;\xi)+B\_{+}(\tau;\xi)v^{+}+B\_{-}(\tau;\xi)v^{-}+i\xi x\right),\qquad A(\tau=0)=B\_{+}(0)=B\_{-}(0)=0. |  |

Matching coefficients yields the Riccati ODEs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A′​(τ)\displaystyle A^{\prime}(\tau) | =i​ξ​(r−q)+β​θ+​B+​(τ)+β​θ−​B−​(τ),\displaystyle=i\xi(r-q)+\beta\theta\_{+}\,B\_{+}(\tau)+\beta\theta\_{-}\,B\_{-}(\tau), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B+′​(τ)\displaystyle B\_{+}^{\prime}(\tau) | =−12​(ξ2+i​ξ)−β​B+​(τ)+12​α2​B+​(τ)2+i​ξ​α​(ρ¯+η)​B+​(τ),\displaystyle=-\tfrac{1}{2}(\xi^{2}+i\xi)-\beta B\_{+}(\tau)+\tfrac{1}{2}\alpha^{2}B\_{+}(\tau)^{2}+i\xi\,\alpha(\bar{\rho}+\eta)\,B\_{+}(\tau), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B−′​(τ)\displaystyle B\_{-}^{\prime}(\tau) | =−12​(ξ2+i​ξ)−β​B−​(τ)+12​α2​B−​(τ)2+i​ξ​α​(ρ¯−η)​B−​(τ).\displaystyle=-\tfrac{1}{2}(\xi^{2}+i\xi)-\beta B\_{-}(\tau)+\tfrac{1}{2}\alpha^{2}B\_{-}(\tau)^{2}+i\xi\,\alpha(\bar{\rho}-\eta)\,B\_{-}(\tau). |  |

### 8.3 Closed-Form Solution to the Riccati ODEs

This system of ODEs can be solved analytically to give the characteristic function. Appendix [A](https://arxiv.org/html/2602.01376v1#A1 "Appendix A Closed-Form Solution of the Model Riccati System ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") contains the full derivation, but the results are given below.

Define the two limiting correlations

|  |  |  |
| --- | --- | --- |
|  | ρ+:=ρ¯+η,ρ−:=ρ¯−η.\rho\_{+}:=\bar{\rho}+\eta,\qquad\rho\_{-}:=\bar{\rho}-\eta. |  |

and define the following complex constants, depending on ξ\xi, the Fourier argument of the characteristic function:

|  |  |  |
| --- | --- | --- |
|  | b±​(ξ):=β−i​ξ​α​ρ±,d±​(ξ):=b±​(ξ)2+α2​(ξ2+i​ξ),g±​(ξ):=b±​(ξ)−d±​(ξ)b±​(ξ)+d±​(ξ).b\_{\pm}(\xi):=\beta-i\xi\,\alpha\,\rho\_{\pm},\qquad d\_{\pm}(\xi):=\sqrt{b\_{\pm}(\xi)^{2}+\alpha^{2}(\xi^{2}+i\xi)},\qquad g\_{\pm}(\xi):=\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{b\_{\pm}(\xi)+d\_{\pm}(\xi)}. |  |

then the characteristic function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(τ;ξ)=i​ξ​(r−q)​τ+βα2​∑±θ±​[(b±​(ξ)−d±​(ξ))​τ−2​ln⁡(1−g±​(ξ)​e−d±​(ξ)​τ1−g±​(ξ))]B±​(τ;ξ)=b±​(ξ)−d±​(ξ)α2​(1−e−d±​(ξ)​τ)(1−g±​(ξ)​e−d±​(ξ)​τ),\boxed{\begin{aligned} A(\tau;\xi)&=i\xi(r-q)\tau+\frac{\beta}{\alpha^{2}}\sum\_{\pm}\theta\_{\pm}\left[(b\_{\pm}(\xi)-d\_{\pm}(\xi))\,\tau-2\ln\!\left(\frac{1-g\_{\pm}(\xi)e^{-d\_{\pm}(\xi)\tau}}{1-g\_{\pm}(\xi)}\right)\right]\\ B\_{\pm}(\tau;\xi)&=\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{\alpha^{2}}\,\frac{(1-e^{-d\_{\pm}(\xi)\tau})}{(1-g\_{\pm}(\xi)e^{-d\_{\pm}(\xi)\tau})},\end{aligned}} |  | (4) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ(t,x,v+,v−;u)=𝔼[ei​u​ln⁡ST∣ℱt]=exp(A(τ;u)+B+(τ;u)vt++B−(τ;u)vt−+iulnSt).\boxed{\Phi(t,x,v^{+},v^{-};u)=\mathbb{E}\!\left[e^{iu\ln S\_{T}}\mid\mathcal{F}\_{t}\right]=\exp\!\left(A(\tau;u)+B\_{+}(\tau;u)v\_{t}^{+}+B\_{-}(\tau;u)v\_{t}^{-}+iu\ln S\_{t}\right).} |  | (5) |

Given the characteristic function, European vanilla option prices can be computed efficiently via Fourier inversion; a standard approach is the Carr-Madan FFT method (Carr and Madan, [1999](https://arxiv.org/html/2602.01376v1#bib.bib3 "Option valuation using the fast fourier transform")).

## 9 Model Implied Volatilities

Adding stochastic spot/volatility correlation tends to increase the implied volatility smile beyond the smile that comes from pure stochastic volatility. That happens because we expect the skew to get more positive as spot goes up, so instantaneous volatility rises relatively faster than a pure Heston model as spot increases (and vice versa as spot decreases).

Figure [1](https://arxiv.org/html/2602.01376v1#S9.F1 "Figure 1 ‣ 9 Model Implied Volatilities ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows a chart of the implied volatility smile for a simplified set of parameters: S=100S=100, r=q=0r=q=0, T=0.25T=0.25, θ=0.01\theta=0.01, α=0.3\alpha=0.3, β=2\beta=2, and ρ¯=ρa=ρ0=0\bar{\rho}=\rho\_{a}=\rho\_{0}=0. As η\eta increases, the smile gets more pronounced. Note that the η=0\eta=0 limit is the Heston model, with constant spot/volatility correlation.

![Refer to caption](imp_vols.png)

Figure 1: Implied Volatility Impact of Adding Stochastic Spot/Volatility Correlation

Increasing η\eta tends to increase the implied volatility smile beyond the smile that comes from pure stochastic volatility. The η=0\eta=0 limit is the Heston model.

## 10 Model Calibration

One important use of this model is pricing exotic derivatives like knockout options. For that purpose it is important that the model reliably reproduce the prices of benchmark vanilla options traded in the market so that the model is accurately representing the cost of hedges in the market.

We consider calibration to three implied volatilities on a single expiration date, and, following FX market conventions, choose to calibrate to the at-the-money implied volatility, the 25-delta risk reversal, and the 25-delta butterfly. The risk reversal is a measure of volatility skew: the 25-delta risk reversal is the implied volatility of a high strike call option whose delta equals 0.25, less the implied volatility of a low strike put option whose delta equals -0.25. The butterfly is a measure of smile, and the 25-delta butterfly equals the average of those two out-of-the-money option implied volatilities, less the at-the-money volatility. Given the at-the-money volatility, the 25-delta risk reversal, and the 25-delta butterfly, one can invert to calculate the implied volatilities of the high- and low-strike options.

As we have three input implied volatilities to calibrate the model to, we must choose just three model parameters to participate in the calibration. For the Heston stochastic volatility model, v0v\_{0} and θ\theta mostly determine the at-the-money volatility - generally these are set to the same value when calibrating to a single expiration, since their difference mostly affects the term structure of at-the-money implied volatility. The value of α\alpha mostly determines the level of the butterfly, and the product of α\alpha and ρ\rho determine the level of the risk reversal. Typically β\beta is specified a priori for single-expiration calibrations: it affects the term structure of at-the-money volatility as well as the butterfly. We are doing single-expiration calibrations so we do not care about the term structure of at-the-money volatility, and we can use α\alpha to match the level of the butterfly.

We will use a similar approach for calibrating our model parameters. The parameters we calibrate are θ(=v0)\theta(=v\_{0}), α\alpha, and ρ¯(=ρa=ρ0)\bar{\rho}(=\rho\_{a}=\rho\_{0}). The parameters we fix a priori are β\beta and η\eta.

We consider an example market for options with 0.25y to expiration, at-the-money volatility 8.0%, 25-delta risk reversal +1.0%, and 25-delta butterfly +0.5%. We use β=2\beta=2 as a representative value. We then calibrate the three parameters such that the model implied volatilities match the market implied volatilities at the three strikes (25-delta put strike, at-the-money strike, and 25-delta call strike).

Figure [2](https://arxiv.org/html/2602.01376v1#S10.F2 "Figure 2 ‣ 10 Model Calibration ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows a chart of the values of the three calibrated parameters, recalibrating at different values of η\eta so that the model implied volatilities continue to match the market implied volatilities.

Increasing η\eta has only a small impact on the overall volatility level, θ\theta. It has a larger effect on the calibrated ρ¯\bar{\rho} correlation level, but still relatively modest.

However, it has a much larger effect on the calibrated α\alpha values: as we saw above, the stochastic correlation contributes to the smile, so less volatility of volatility is needed to match a given implied volatility smile. This is an interesting effect, since there are well known issues with Heston-style models when the α\alpha values get so big that v=0v=0 becomes accessible (Lord et al., [2010](https://arxiv.org/html/2602.01376v1#bib.bib4 "A comparison of biased simulation schemes for stochastic volatility models")) - violating the Feller condition α22​β​θ<1\frac{\alpha^{2}}{2\beta\theta}<1. Adding stochastic correlation means that the model parameters are less likely to break the Feller threshold, making the distribution of vtv\_{t} more stable.

![Refer to caption](params_by_eta.png)

Figure 2: Calibrated Parameters vs Volatility of Correlation

Increasing η\eta has noticeable but relatively limited impact on the calibrated values of θ\theta and ρ¯=ρa\bar{\rho}=\rho\_{a}. However, it has a larger impact on the volatility of volatility parameter α\alpha, which decreases as η\eta increases.

## 11 The Risk Reversal Beta and Parameter Estimation

### 11.1 The Risk Reversal Beta Empirically

An important market dynamic that this model incorporates is the correlation between moves in the spot/volatility correlation and spot returns.

The spot/volatility correlation is not directly observable in the market. A reasonable proxy, however, is the implied volatility skew, quantified as the risk reversal111If a delta is not specified for a risk reversal we assume it is a 25-delta risk reversal. in foreign exchange markets. There is a separate risk reversal for each option expiration tenor quoted in the market.

In the Heston stochastic volatility model, as in most stochastic volatility models, the risk reversal is well approximated as proportional to the spot/volatility correlation. That suggests that we can get an estimate of the spot/volatility correlation dynamics by looking at the dynamics of market risk reversal levels.

Figure [3](https://arxiv.org/html/2602.01376v1#S11.F3 "Figure 3 ‣ 11.1 The Risk Reversal Beta Empirically ‣ 11 The Risk Reversal Beta and Parameter Estimation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows a time series of EURUSD 3m-expiration risk reversal on the left axis, and EURUSD spot on the right axis, between 2022 and 2025222Data courtesy of JPMorgan Chase’s foreign exchange options trading desk: London 11am representative daily closes. Figure [4](https://arxiv.org/html/2602.01376v1#S11.F4 "Figure 4 ‣ 11.1 The Risk Reversal Beta Empirically ‣ 11 The Risk Reversal Beta and Parameter Estimation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows the same for the USDJPY currency pair.

![Refer to caption](rrs_eurusd.png)

Figure 3: EURUSD 3m-Expiration 25-Delta Risk Reversals and EURUSD Spot

EURUSD 3m 25-delta risk reversal (left) and EURUSD spot (right) between 2022 and 2025. Note the strong relationship between the two.



![Refer to caption](rrs_usdjpy.png)

Figure 4: USDJPY 3m-Expiration 25-Delta Risk Reversals and USDJPY Spot

USDJPY 3m 25-delta risk reversal (left) and USDJPY spot (right) between 2022 and 2025. The relationship is not as consistent over time as it is for EURUSD but day to day changes are still quite correlated.



![Refer to caption](rr_betas_eurusd.png)

Figure 5: EURUSD 3m-Expiration Risk Reversal Beta

A regression of daily changes in EURUSD 3m 25-delta risk reversals vs daily spot log returns using daily data from 2025. The R2R^{2} of the fit is 43%, giving a spot/risk reversal correlation of 66%. The risk reversal beta is the slope of the line: the risk reversal tends to get more positive by 0.16% for every 1% increase in spot.



![Refer to caption](rr_betas_usdjpy.png)

Figure 6: USDJPY 3m-Expiration Risk Reversal Beta

A regression of daily changes in USDJPY 3m 25-delta risk reversals vs daily spot log returns using daily data from 2025. The R2R^{2} of the fit is 31%, giving a spot/risk reversal correlation of 55%. The risk reversal beta is the slope of the line: the risk reversal tends to get more positive by 0.12% for every 1% increase in spot.

Figures [5](https://arxiv.org/html/2602.01376v1#S11.F5 "Figure 5 ‣ 11.1 The Risk Reversal Beta Empirically ‣ 11 The Risk Reversal Beta and Parameter Estimation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") and [6](https://arxiv.org/html/2602.01376v1#S11.F6 "Figure 6 ‣ 11.1 The Risk Reversal Beta Empirically ‣ 11 The Risk Reversal Beta and Parameter Estimation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") show linear regressions of daily change in 3m 25-delta risk reversal vs daily spot log returns. These figures highlight the strong dependence between these two market factors: the R2R^{2} for the EURUSD regression is 43%, translating to a spot/rho correlation of 66%; for USDJPY the R2R^{2} is 31%, leading to a spot/rho correlation of 55%. These regressions use a one year window, including all daily market data in 2025.

![Refer to caption](rr_beta_by_tenor_mkt.png)

Figure 7: Empirical EURUSD and USDJPY Risk Reversal Beta by Expiration Tenor

Risk reversal betas tend to be larger for shorter expirations, which suggests mean reversion in the underlying spot/volatility correlation process. These values were calculated as the slopes of linear regressions of daily changes in 25-delta risk reversals vs daily spot log returns, using daily data from 2025.

The slopes of those regression lines are exactly what we define as the “risk reversal beta”333“Risk reversal beta” is not a standard term in the foreign exchange markets.: how much we expect the risk reversal to move given a small move in spot. For EURUSD that risk reversal beta is 0.16 (for 3m-expiration options, regressed over data in the 2025 calendar year) - that is, the EURUSD 3m 25-delta risk reversal is expected to increase 0.16% for every 1% increase in spot. Note that these are absolute, not relative, changes in risk reversals, whose values happen to be quoted in percent volatilities. For USDJPY the risk reversal beta was estimated as 0.12 in this dataset.

We are using 3m-expiration data as an example, but there is a different risk reversal beta for each expiration. Figure [7](https://arxiv.org/html/2602.01376v1#S11.F7 "Figure 7 ‣ 11.1 The Risk Reversal Beta Empirically ‣ 11 The Risk Reversal Beta and Parameter Estimation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows a chart of the EURUSD and USDJPY risk reversal betas as a function of expiration tenor, calculated from linear regressions of 25-delta risk reversal changes vs spot returns (using the same daily data from 2025).444The risk reversal beta is also a function of delta. The 10-delta risk reversal beta is almost always the 25-delta risk reversal beta multiplied by a scale factor greater than 1. Note that risk reversal beta declines with tenor, which is what we would expect from a mean reverting spot/volatility correlation process.

### 11.2 Model Risk Reversal Beta

Now we turn to calculating our model’s risk reversal beta, which will help us estimate η\eta. In this model the expression for the risk reversal beta is a somewhat complicated function of the model parameters and FX options market conventions for how to calculate a strike from a benchmark delta. However, in practice the model risk reversal value’s dependence on ρ0\rho\_{0} - the initial spot/volatility correlation - is very close to linear. The slope of that line depends on the model parameters and the option expiration.

We write

|  |  |  |
| --- | --- | --- |
|  | d​R​R​(τ)=k​(τ)​d​ρtdRR(\tau)=k(\tau)d\rho\_{t} |  |

to express this dependence, where k​(τ)k(\tau) is the slope, written here as a function of the expiration tenor τ\tau, but it is also a function of the other model parameters.

We do this to give us a way to estimate how much we expect the risk reversal to move for a given log spot change. If we restrict ourselves to ρ0=ρ¯\rho\_{0}=\bar{\rho} and v0=θv\_{0}=\theta for simplicity, we see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​R​R​(τ)\displaystyle dRR(\tau) | =k​(τ)​d​ρt=k​(τ)​α​ηθ​d​Wtρ=k​(τ)​α​η​ρc​sθ​d​WtS+…\displaystyle=k(\tau)d\rho\_{t}=k(\tau)\frac{\alpha\eta}{\sqrt{\theta}}dW^{\rho}\_{t}=k(\tau)\frac{\alpha\eta\rho\_{cs}}{\sqrt{\theta}}dW^{S}\_{t}+... |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =k​(τ)​α​η2θ​d​Xt+…\displaystyle=\frac{k(\tau)\alpha\eta^{2}}{\theta}dX\_{t}+... |  |

where the ellipses refer to noise independent of the log return d​XdX. Here we used the expression for ρc​s\rho\_{cs} from equation [3](https://arxiv.org/html/2602.01376v1#S7.E3 "In 7 Spot/Rho Correlation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing"), and d​WtS=d​Xt/vtdW^{S}\_{t}=dX\_{t}/\sqrt{v\_{t}}.

In this formulation, then, the risk reversal beta βr​r\beta\_{rr} is given by the slope,

|  |  |  |  |
| --- | --- | --- | --- |
|  | βr​r=k​(τ)​α​η2θ\beta\_{rr}=\frac{k(\tau)\alpha\eta^{2}}{\theta} |  | (6) |

This result highlights that this model implies a risk reversal beta that is proportional to η2\eta^{2}. The term structure of the risk reversal beta is determined by k​(τ)k(\tau), which has no simple closed form, but can be calculated numerically by measuring the slope of change in model-implied risk reversal for small changes in the initial correlation ρ0\rho\_{0}. It decays on a timescale of about 1/β1/\beta.

Figure [8](https://arxiv.org/html/2602.01376v1#S11.F8 "Figure 8 ‣ 11.2 Model Risk Reversal Beta ‣ 11 The Risk Reversal Beta and Parameter Estimation ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows a chart of the model’s risk reversal beta as a function of expiration tenor, for η=0.25\eta=0.25 and η=0.5\eta=0.5. This was calibrated (tenor by tenor, independently) to a market where the at-the-money volatility is 8.0%, the 25-delta risk reversal is +1.0%, and the 25-delta butterfly is 0.5% - the same for all tenors. We used β=2\beta=2.

![Refer to caption](rr_beta_by_tenor_svscd.png)

Figure 8: Model Risk Reversal Beta by Option Expiration Tenor

The model’s risk reversal beta has a term structure that is determined by the value of β\beta, with a level determined by η2\eta^{2}. The chart shows the model risk reversal beta for two different values of η\eta. For this the model was calibrated independently to the same at-the-money volatility, 25-delta risk reversal, and 25-delta butterfly values for all tenors.

### 11.3 Estimating η\eta from Risk Reversal Beta

We can now estimate parameter values: if we use an empirical risk reversal beta for EURUSD 3m options of 0.16, use θ=0.01\theta=0.01 as a representative variance level, and use α=0.3\alpha=0.3 as a representative volatility of volatility, we can numerically calculate k​(τ)=0.037k(\tau)=0.037. Then η=(θ​βr​r)/(k​(τ)​α)≈0.4\eta=\sqrt{(\theta\beta\_{rr})/(k(\tau)\alpha)}\approx 0.4 is one estimate of the stochastic correlation parameter for the EURUSD market.

This method of empirically estimating η\eta based on the historical dynamics of risk reversals is one way of estimating this parameter’s value. Another is to imply it from the market prices of exotic derivatives that depend on it, such as barrier derivatives.

## 12 Barrier Option Pricing and the Risk Reversal Beta

Barrier derivatives are popular products in the foreign exchange markets, often trading as knockout options (vanilla options whose payoffs go to zero if a continuous barrier is breached by the asset spot price any time before expiration) and one touch options (digital options where the owner is paid one unit of currency only if a continuous barrier is breached any time before expiration).

Bid/ask spreads on “out-of-the-money” knockout options, where the option is out of the money when the barrier is breached, are comparable to bid/ask spreads on vanilla options in the foreign exchange markets - so very tight indeed, typically measured in a few basis points of the knockout’s asset currency notional. Bid/ask spreads on one touch options, whose prices are quoted in percent of the payoff, are typically one or two percent. Accurate pricing models are important when bid/ask spreads are tight on exotic derivatives.

### 12.1 Model Barrier Pricing

Unlike with vanilla option pricing, we have found no computational shortcut for barrier option pricing. We use Monte Carlo simulation below to price these derivatives, after calibrating the model to market vanilla option implied volatilities using the fast vanilla option pricing.

We price continuously monitored barrier claims under our model via Monte Carlo simulation of the log-asset with CIR variance evolved by Andersen ([2008](https://arxiv.org/html/2602.01376v1#bib.bib12 "Simple and efficient simulation of the heston stochastic volatility model")) quadratic-exponential (QE) scheme (with non-negativity enforced). Barrier crossing is detected each time step using a log-space Brownian-bridge crossing probability that uses expected volatility over the interval. We also use a Feller-ratio-based heuristic that increases the time-step resolution when α22​β​θ\frac{\alpha^{2}}{2\beta\theta} is large.

We use the underlying vanilla option as a control variate for out-of-the-money knockout options. For one touches we use a European digital with strike equal to the one touch barrier level as a control variate.

### 12.2 One Touch Options

The risk reversal beta is a key dynamic for pricing one touch options. We can build intuition on this front by considering a hedging strategy for a long one touch position: selling twice the notional of a European digital option with strike equal to the one touch option’s barrier level, and sharing the same expiration date. An up-barrier one touch would be hedged by selling twice the notional of a European digital call option, and a down-barrier one touch would be hedged by selling twice the notional of a European digital put option.

Consider an up-barrier one touch option, hedged with twice the notional of a European digital call option. If spot never touches the barrier before the expiration, the one touch ends up worthless - as does the European digital call option. If spot does drift up and touch the barrier before expiration, the one touch pays off and is worth one unit of the payoff currency. The European digital option does not pay off yet - but because spot is at the digital option strike price, assuming small risk neutral drift, the digital has roughly even odds of ending in the money and paying two units of the payoff currency. That means the European digital price is around 50%, and so the product of twice the notional and a 50% price gives a value of the European digital that roughly offsets the payoff of the one touch option. Therefore twice the notional of the European digital call option is a fairly close cash flow hedge for the up-barrier one touch, and in practice is a good semi-static vega and gamma hedge as well - semi-static in the sense that the hedge needs to be adjusted - unwound - only if the barrier is breached.

The European digital’s price is not exactly 50% with spot at its strike, however. If we replicate a European digital call option as a tight call spread, its price PEP\_{E} can be written as

|  |  |  |
| --- | --- | --- |
|  | PE=−d​C​(K)d​K=−∂CB​S​(K,σi​v)∂K−∂CB​S∂σi​v​d​σi​vd​KP\_{E}=-\frac{dC(K)}{dK}=-\frac{\partial C\_{BS}(K,\sigma\_{iv})}{\partial K}-\frac{\partial C\_{BS}}{\partial\sigma\_{iv}}\frac{d\sigma\_{iv}}{dK} |  |

Here CB​S​(K,σi​v​(K))C\_{BS}(K,\sigma\_{iv}(K)) is the price of a European vanilla call option with strike KK and implied volatility σi​v​(K)\sigma\_{iv}(K).

When spot is at the European digital strike, the first term - the Black-Scholes digital price - is indeed close to 50%. But the second term shifts the price by an amount proportional to the slope of implied volatility vs strike - that is, the implied volatility skew, or the risk reversal.

If we think back to our portfolio of long one touch, short twice the notional of European digital, when spot touches the barrier, we need to buy back the European digital hedge, since the one touch no longer has any risk to hedge. Per above, the price we buy it back at depends on the risk reversal: the more positive the risk reversal is, the cheaper the European digital is to buy back, so the better it is for us. The total expected hedging cost of the one touch, based on unwinding the European digital hedge conditioned on hitting the barrier at different times, goes down as the risk reversal gets more positive.

This links us back to the risk reversal beta, and why that affects one touch pricing. When we put on the one touch trade, we know the value of the risk reversal; if spot drifts up to the barrier and we expect a positive correlation between moves in risk reversal and moves in spot due to the risk reversal beta, we expect to pay less to buy back the European digital. So the higher the risk reversal beta, the higher the up-barrier one touch price should be.

We can estimate the magnitude of this effect by approximating the unwind cost change due to the risk reversal beta. We approximate

|  |  |  |
| --- | --- | --- |
|  | ∂C∂σ=k1​S​T\frac{\partial C}{\partial\sigma}=k\_{1}S\sqrt{T} |  |

where k1k\_{1} is a constant of order 1, SS is the asset spot price, and TT is the time to expiration. We approximate the slope of implied volatility vs strike in terms of the risk reversal, approximating the 25-delta strike difference as k2​S​σ​Tk\_{2}S\sigma\sqrt{T}:

|  |  |  |
| --- | --- | --- |
|  | d​σd​K=k2​R​RS​σ​T\frac{d\sigma}{dK}=k\_{2}\frac{RR}{S\sigma\sqrt{T}} |  |

where k2k\_{2} is another constant of order 1 and R​RRR is the 25-delta risk reversal for expiration TT.

That means the European digital price correction is

|  |  |  |
| --- | --- | --- |
|  | −∂CB​S∂σi​v​d​σi​vd​K=−k1​k2​R​Rσ-\frac{\partial C\_{BS}}{\partial\sigma\_{iv}}\frac{d\sigma\_{iv}}{dK}=-k\_{1}k\_{2}\frac{RR}{\sigma} |  |

For our purposes we care how much this price correction changes due to the risk reversal beta. Call this extra price correction, on top of what you would expect from a model like Heston where the risk reversal beta is approximately zero, Δ​PE\Delta P\_{E}:

|  |  |  |
| --- | --- | --- |
|  | Δ​PE=k1​k2​βr​r​ln⁡(B/S)σ\Delta P\_{E}=k\_{1}k\_{2}\frac{\beta\_{rr}\ln(B/S)}{\sigma} |  |

The expected extra unwind cost due to the risk reversal beta is (roughly) this quantity multiplied by the probability of hitting the barrier, which is just the one touch price itself, also of order 1.

Therefore, we can estimate the sign and magnitude of the one touch price correction as approximately Po​t​Δ​PEP\_{ot}\Delta P\_{E}.

Consider a market where the risk reversal beta βr​r=0.15\beta\_{rr}=0.15, at-the-money volatility is 8%, the barrier is 5% above spot, and the price of the one touch is 50%. k1≈0.4k\_{1}\approx 0.4 and k2≈0.7k\_{2}\approx 0.7. The price correction is then around 1.5%. So we should expect a price impact of the order of a few percent (of the one touch payout amount) from this effect.

One can follow a similar argument for down-barrier one touches and their European digital put option hedges and find the same effect: the price impact of a positive risk reversal beta should be positive, and has the same approximate expression.

![Refer to caption](ot_by_barrier.png)

Figure 9: One Touch Price Differences to Heston by Barrier Level

This chart shows the difference between our model price for a one touch and its Heston model price, as a function of barrier level. On the x-axis we show, rather than barrier level, the equivalent Black-Scholes one touch price, with the current asset spot price in the center. That is, the barrier level of the one touch is set such that the Black-Scholes one touch price matches the target price. Increasing η\eta shows the expected positive price impact to one touch prices, with magnitude near our approximate estimate.

Let us compare this rough estimation with the actual results from the model. Figure [9](https://arxiv.org/html/2602.01376v1#S12.F9 "Figure 9 ‣ 12.2 One Touch Options ‣ 12 Barrier Option Pricing and the Risk Reversal Beta ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows one touch prices as a function of barrier level. The x-axis shows the barrier strike, but in terms of the Black-Scholes price of one touches - that is, pricing them assuming a constant volatility equal to the at-the-money volatility. The y-axis shows the difference between our model price and the Heston model price, which represents the price impact of stochastic spot/volatility correlation - calibrating model parameters to match the market implied volatilities in both cases. Notice that the model prices always move higher as η\eta increases, as expected by the hedging analysis. Also notice that the scale of the impact from stochastic correlation matches our order of magnitude estimate: that is, a few percent.

The price impact of stochastic correlation is proportional to the risk reversal beta, so should be roughly quadratic in η\eta. Figure [10](https://arxiv.org/html/2602.01376v1#S12.F10 "Figure 10 ‣ 12.2 One Touch Options ‣ 12 Barrier Option Pricing and the Risk Reversal Beta ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows this behavior for a 3m-expiration up-barrier one touch with a Black-Scholes price of 50%, and a 3m-expiration down-barrier one touch with a Black-Scholes price of 50%, for η\eta between 0 and 0.5.

![Refer to caption](ot_by_eps.png)

Figure 10: One Touch Price Differences to Heston by η\eta

This chart shows the difference between the model price for two one touches and their Heston model prices, as a function of η\eta. The “Up-Barrier” line shows the price difference for a 3m-expiration up-barrier one touch with a Black-Scholes price of 50%, and the “Down-Barrier” line shows the price difference for a 3m down-barrier one touch with a Black-Scholes price of 50%.

A consequence of this analysis is that using the Heston model to price one touch options, after calibrating the model to vanilla options, leads to one touch prices that are too low, by an amount comparable to or larger than the bid/ask spread. A market maker who uses that model to price new deals and manage risk will find that they tend to accumulate a short position in one touches: their desk tends to make prices that are too low, so counterparties tend to buy from the market maker more often than they sell to them. The trading desk may accumulate quite a large short position until they discover that their model prices are below market prices; when they correct their model they will finally realize their loss as they increase their model prices of positions which they are short.

### 12.3 Out-of-the-Money Knockout Options

A similar hedging argument can be used to demonstrate that the risk reversal beta has a significant positive impact on knockout option prices.

An “out-of-the-money” knockout option is one where the underlying option is out of the money when the barrier is hit. For example, a “down-and-out” knockout call option is one where the option knocks down and out - the barrier is below the current spot price - and the barrier level is below the option strike price. Similarly, an “up-and-out” knockout put option is one where the option knocks up and out, and the barrier level is above the option strike price.

Consider a long position in a down-and-out knockout call option, with strike KK and barrier B<KB<K. A decent semi-static hedge for this derivative is to sell a call option with strike KK and buy a put option with strike K′=B2/KK^{\prime}=B^{2}/K, which is less than BB. If spot never trades down through the barrier, the vanilla call option exactly hedges the expiration cashflows of the knockout call. If, though, spot does trade down to the barrier, the knockout option price goes to zero. At that point, the put option in the hedge is roughly as much out-of-the-money as the call option, so, assuming small risk neutral drift, the call and put prices will be close. The hedge portfolio is short the call and long the put, so if the two prices are similar, the hedge portfolio’s price is also close to zero when spot is at the barrier. This two-vanilla portfolio is a decent cashflow hedge for the knockout, and roughly hedges vega and gamma until the barrier is breached.

However, like with the European digital, the price of the two option hedge portfolio is not exactly zero when spot touches the barrier. At that point, as part of this semi-static hedging strategy, we would need to buy the call and sell the put, at whatever the market prices are for the options at that point.

When spot is at the barrier, both options are roughly the same distance out of the money. That means the vega of the two options also roughly cancels, like the price does: the cost of unwinding that hedge does not depend much on the level of at-the-money volatility when the barrier is breached. Similarly, the risk to the implied volatility smile - the butterfly - roughly cancels off, and the unwind cost does not depend on the butterfly either. However, the portfolio looks like a short risk reversal position for whatever delta the options have when the barrier is breached - which means that the closeout costs do depend sensitively on the level of the risk reversal when the barrier is hit. To close out the hedge we must buy back that risk reversal option position: the more positive the risk reversal, the more we have to pay to unwind the portfolio.

Our best estimate for the level of the risk reversal when spot trades down to the barrier is the current market level less a shift (as spot goes down to the barrier) due to the risk reversal beta. That is, we expect the risk reversal when spot goes to the barrier to be more negative than the current level. The larger the risk reversal beta, the more negative the risk reversal will be when the barrier is breached, and the cheaper it is to buy back the option hedge - which therefore increases the price of the knockout option.

We can again estimate the magnitude of this effect. This is trickier than for the one touch case, because we do not know the delta of the options when spot touches the barrier. That affects both the vega of the options - and hence their sensitivity to risk reversal moves - and the scale factor for the risk reversal beta. Remember that the risk reversal betas we saw above were for 25-delta options; the risk reversal beta of a risk reversal with delta less than 0.25 is larger than that for a 25-delta option, and the risk reversal beta of a risk reversal with delta greater than 0.25 is smaller.

Each option’s vega is

|  |  |  |
| --- | --- | --- |
|  | Vega=k1​S​T2​π\mathrm{Vega}=k\_{1}S\sqrt{\frac{T}{2\pi}} |  |

where k1k\_{1} depends on the delta of the option, and is between 0 and 1; for a 25-delta option k1≈0.4k\_{1}\approx 0.4. We can also write the move in risk reversal as

|  |  |  |
| --- | --- | --- |
|  | Δ​R​R=k2​βr​r​ln⁡(S/B)\Delta RR=k\_{2}\beta\_{rr}\ln(S/B) |  |

where k2k\_{2} depends on the delta of the option, since the risk reversal in question is that for the delta of the options when spot touches the barrier. For deltas less than 0.25, k2>1k\_{2}>1; for deltas greater than 0.25, k2<1k\_{2}<1.

Then the price correction due to the move in risk reversal from the risk reversal beta is

|  |  |  |
| --- | --- | --- |
|  | Δ​Pv​a​nS=k1​k2​βr​r​ln⁡(S/B)​T2​π\frac{\Delta P\_{van}}{S}=k\_{1}k\_{2}\beta\_{rr}\ln(S/B)\sqrt{\frac{T}{2\pi}} |  |

For a rough estimate, consider the case when the options are 25-delta at the barrier, so k1=0.4k\_{1}=0.4 and k2=1k\_{2}=1. Using a risk reversal beta of 0.16, a barrier 5% below spot, and 0.25 years left to expiration, the price correction is approximately 6 basis points of the asset currency notional. As with one touches, that correction needs to be multiplied by the probability of hitting the barrier - if that is 50%, then the price impact is 3 basis points. That is comparable to or larger than the bid/ask spread for out-of-the-money knockout options in the foreign exchange inter-bank market.

A similar argument can be used to estimate the price impact of the risk reversal beta on up-and-out knockout put options; the price impact is approximately the same, and also positive.

![Refer to caption](ko_by_barrier.png)

Figure 11: Knockout Price Differences to Heston by Barrier Level

This chart shows the difference between the model price for an out-of-the-money knockout option and its Heston model price, as a function of barrier level, in basis points of asset currency notional. On the x-axis we show, rather than barrier level, the equivalent Black-Scholes one touch price, with the current asset spot price in the center. That is, the barrier level of the one touch is set such that the Black-Scholes one touch price matches the target price. Increasing η\eta shows the expected positive price impact to knockout prices, with magnitude near our approximate estimate.

Figure [11](https://arxiv.org/html/2602.01376v1#S12.F11 "Figure 11 ‣ 12.3 Out-of-the-Money Knockout Options ‣ 12 Barrier Option Pricing and the Risk Reversal Beta ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") quantifies this in our model, showing how knockout prices are affected by η\eta at different barrier levels. For barrier levels above spot we use up-and-out knockout put options, and for barrier levels below spot we use down-and-out knockout call options. All options have a strike equal to the initial spot price - that is, they are at-the-money options. The barrier levels are displayed in terms of the Black-Scholes one touch prices as with the one touch chart. The y-axis shows the model price difference to the Heston model price. The price impact is positive as we expected from the hedging analysis, and the price impact is comparable to the approximate estimates we made above.

As with one touches, the price impact of adding stochastic correlation is always positive, if the model is always calibrated to market vanilla option prices. So a market maker using the Heston model to price out-of-the-money knockouts risks finding themselves selling knockout options at what they only discover later to be below-market prices.

## 13 Volatility Swap Fair Strikes and the Risk Reversal Beta

### 13.1 Volatility Swaps

Volatility swaps are another example of liquid exotic derivatives in the foreign exchange markets. Bid/ask spreads are quoted in volatility terms and are typically almost as tight as bid/ask spreads on vanilla option implied volatilities, around 0.1%. Volatility swaps cannot be statically hedged with vanilla options and so their prices are sensitive to market dynamics not captured in vanilla option prices.

A volatility swap pays the realized volatility of an asset, computed from a set of published once-per-day spot fixings, and exchanges it against a fixed strike set at trade inception. With unit notional, the payoff Pv​sP\_{vs} is

|  |  |  |
| --- | --- | --- |
|  | Pv​s=σr−σKP\_{vs}=\sigma\_{r}-\sigma\_{K} |  |

where σK\sigma\_{K} is the fixed level of the volatility swap and σr\sigma\_{r} is the realized volatility:

|  |  |  |
| --- | --- | --- |
|  | σr=NdN​∑i=1NRi2\sigma\_{r}=\sqrt{\frac{N\_{d}}{N}\sum\_{i=1}^{N}R\_{i}^{2}} |  |

Here, NdN\_{d} is the contract-specified number of trading days per year, which annualizes the daily realized volatility. NN is the number of returns in the calculation. RiR\_{i} is the return between consecutive fixings, computed as the log return of the spot price on day ii versus the previous fixing:

|  |  |  |
| --- | --- | --- |
|  | Ri=ln⁡SiSi−1R\_{i}=\ln\frac{S\_{i}}{S\_{i-1}} |  |

Fixing times tit\_{i} are typically daily. There are N+1N+1 spot fixings for the NN returns555This is a simplified realized-volatility definition; some contracts use variations (for example, de-meaning returns before squaring). We will use this simplified form for our analysis..

The “fair strike” for a volatility swap is the value of σK\sigma\_{K} that makes the swap have zero value at inception; equivalently, it is the strike that makes the (discounted) risk-neutral expected payoff Pv​sP\_{vs} equal to zero. The tenor of the volatility swap is the time to the final spot fixing.

### 13.2 Volatility Swaps and Volatility of Volatility Sensitivity

A related product to a volatility swap is a variance swap, which swaps that realized volatility *squared* against a fixed level. Variance swaps can be statically666Approximately hedged, assuming continuous fixings and no jumps in the underlying spot price process. hedged by a portfolio of vanilla options (Demeterfi et al., [1999](https://arxiv.org/html/2602.01376v1#bib.bib13 "A guide to volatility and variance swaps")), which means that the variance swap fair strike should not change when we add stochastic spot/volatility correlation to the model, assuming the model remains calibrated to market vanilla option prices.

That means we can treat the variance swap as a separate asset, fully specified by the vanilla options market, and consider the volatility swap as a derivative of the variance swap that has a square root payoff. That convex payoff means that volatility swaps cannot be statically hedged by a portfolio of vanilla options, so their prices can depend on market dynamics that are not pinned down by vanilla prices.

The key market dynamic that affects a volatility swap fair strike is the volatility of volatility. To build intuition, consider a dynamic hedging strategy for a long volatility swap: sell a variance swap with the same fixing schedule, with notional 1/(2​σK)1/(2\sigma\_{K}), to hedge the first-order sensitivity to moves in the variance swap fair strike (which is effectively the underlying asset price for the volatility swap). As volatility rises, the volatility swap’s vega is roughly unchanged, while the variance swap’s vega increases because of its quadratic payoff. The combined position therefore becomes net short vega, and the trader must buy additional variance swap at the now-higher volatility level to re-hedge. When volatility falls, the variance swap’s vega decreases and the trader must sell more variance swap at the lower level. In other words, the hedge is short convexity in the variance swap fair strike - a kind of volatility gamma - so rebalancing losses increase as the volatility of volatility increases.

### 13.3 Volatility Swap Fair Strikes and Stochastic Spot/Volatility Correlation

This suggests that the volatility swap fair strike should increase as the volatility of volatility decreases, because these short “volatility gamma” hedging costs are decreased. As we saw above, increasing η\eta and recalibrating to market vanilla prices means that α\alpha - the volatility of volatility parameter in our model - decreases. Therefore the volatility swap fair strike should increase as η\eta increases.

![Refer to caption](vs_by_eta.png)

Figure 12: Volatility Swap Fair Strikes vs Volatility of Correlation

Increasing the volatility of correlation parameter η\eta increases the fair strike of a 3m volatility swap because the model needs less volatility of volatility from α\alpha to match the market implied volatilities.

Figure [12](https://arxiv.org/html/2602.01376v1#S13.F12 "Figure 12 ‣ 13.3 Volatility Swap Fair Strikes and Stochastic Spot/Volatility Correlation ‣ 13 Volatility Swap Fair Strikes and the Risk Reversal Beta ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") shows the volatility swap fair strike as a function of η\eta. The x-axis shows η\eta, and the y-axis shows the fair strike for a volatility swap with a 3-month horizon and daily spot fixings. The fair strike increases as η\eta increases, consistent with the hedging argument above. We used Nd=250N\_{d}=250 as a representative value. The model is calibrated to an at-the-money volatility of 8.0%, a 25-delta risk reversal of +1.0%, and a 25-delta butterfly of +0.5%.

Note that a volatility swap price does not explicitly directly depend much on the risk reversal beta dynamic: if we keep other model parameters fixed and only change η\eta, the volatility swap fair strike hardly changes. The effect displayed in Figure [12](https://arxiv.org/html/2602.01376v1#S13.F12 "Figure 12 ‣ 13.3 Volatility Swap Fair Strikes and Stochastic Spot/Volatility Correlation ‣ 13 Volatility Swap Fair Strikes and the Risk Reversal Beta ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing") is due to recalibrating the model parameters at different values of η\eta to match a fixed implied volatility smile, which changes the calibrated volatility of volatility parameter α\alpha.

The size of this pricing adjustment is comparable to or larger than the bid/ask spread for volatility swaps, and it is always positive because increasing η\eta always decreases the (calibrated) volatility of volatility α\alpha. As with out-of-the-money knockout options, market makers who use the Heston model for volatility swap pricing risk selling volatility swaps below market levels.

For this analysis we calculated volatility swap fair strikes using Monte Carlo simulation, following the same approach as the one touch and knockout option pricing algorithm.

## 14 Related Literature and Model Context

Our model is an extension of the Heston stochastic volatility model (Heston, [1993](https://arxiv.org/html/2602.01376v1#bib.bib2 "A closed-form solution for options with stochastic volatility with applications to bond and currency options")), which itself extends the Black-Scholes framework (Black and Scholes, [1973](https://arxiv.org/html/2602.01376v1#bib.bib1 "The pricing of options and corporate liabilities")) by introducing a stochastic volatility. Our goal was to add stochastic correlation between spot and volatility, where that correlation is itself correlated with the spot price, and lets us model risk reversal beta.

There are several other approaches in the literature that incorporate the risk reversal beta dynamic for pricing exotic derivatives, or follow a similar approach to our model.

### 14.1 The Double Heston Model

Our model is a version of the Double Heston model defined in (Christoffersen et al., [2009](https://arxiv.org/html/2602.01376v1#bib.bib9 "The shape and term structure of the index option smirk: why multifactor stochastic volatility models work so well")). That model included a second sub-variance not to explicitly introduce stochastic spot/volatility correlation (though it does, and the paper investigates that quantity), but to better match the full implied volatility surface with a small set of constant model parameters. That is, it is more geared at matching implied volatilities across different expiration tenors than focused on the impact of stochastic spot/volatility correlation on exotic derivative prices.

### 14.2 Stochastic Correlation in Heston-Type Models

A natural way to enrich Heston is to relax the assumption of constant spot/volatility correlation and allow correlation itself to be stochastic by explicitly specifying the process it follows. For example, Teng et al. ([2016](https://arxiv.org/html/2602.01376v1#bib.bib5 "On the heston model with stochastic correlation")) study Heston-type models with stochastic correlation (including Ornstein-Uhlenbeck and bounded “Jacobi”-type specifications for correlation), and Teng et al. ([2018](https://arxiv.org/html/2602.01376v1#bib.bib6 "Numerical simulation of the heston model under stochastic correlation")) investigate numerical simulation and option pricing implications under stochastic correlation dynamics. These are not affine models and do not admit closed-form characteristic functions, and therefore are more difficult to use in practice: model calibration involves generating many vanilla option prices with different parameters during a numerical rootfinding, and if vanilla option pricing is slow, that calibration process becomes unwieldy. They do admit affine approximations.

Our model differs by making the variance the sum of two sub-variance processes that have different spot/volatility correlations. This allows the spot/volatility correlation to be stochastic, and to be bounded by construction, but still maintains the affine structure of the Heston model.

### 14.3 Stochastic Volatility/Local Volatility Mixture Models

Another common approach to modeling risk reversal beta is to combine stochastic volatility with a deterministic local volatility . These models are often called *local stochastic volatility* (LSV) or *stochastic-local volatility* (SLV) models. A standard specification is

|  |  |  |
| --- | --- | --- |
|  | σinst​(t,St)=σL​(t,St)​vt,\sigma\_{\text{inst}}(t,S\_{t})=\sigma\_{L}(t,S\_{t})\,\sqrt{v\_{t}}, |  |

where vtv\_{t} is a Heston/CIR-type variance factor and σL​(t,S)\sigma\_{L}(t,S) is the “local volatility”: a deterministic function of spot StS\_{t} and calendar time tt. In the pure stochastic volatility limit of this model, σL\sigma\_{L} is a constant and vtv\_{t} drives the implied volatility skew and smile; in the pure local volatility limit, vtv\_{t} is deterministic and σL\sigma\_{L} drives the smile.

An example of a paper that explicitly develops this LSV framework and discusses both vanilla and exotic pricing is Lipton et al. ([2014](https://arxiv.org/html/2602.01376v1#bib.bib10 "Pricing of vanilla and first-generation exotic options in the local stochastic volatility framework: survey and new results")). A closely related and widely used practical incarnation is the “Heston stochastic-local volatility” (HSLV) model, in which the Heston dynamics are enhanced by a nonparametric local-volatility component; see van der Stoep et al. ([2014](https://arxiv.org/html/2602.01376v1#bib.bib11 "The Heston stochastic-local volatility model: efficient monte carlo simulation")) for an efficient Monte Carlo approach and discussion of calibration.

These mixture models are regularly used in foreign exchange markets because the local volatility and stochastic volatility limits of the mixture deliver very different risk reversal betas. In a pure stochastic volatility model like the Heston model, the risk reversal is roughly constant since the spot/volatility correlation is constant, and the risk reversal beta is close to zero. In a local volatility model the risk reversal tends to move up and down according to the smile and moves in risk reversal have a high correlation with spot: the risk reversal beta is high. Tuning the mixture parameter lets the model user tune the model’s risk reversal beta.

### 14.4 Affine Matrix Models and Wishart Stochastic Volatility

Another common route to stochastic correlation is to model a full stochastic covariance matrix whose implied correlations evolve over time. Wishart (matrix-affine) stochastic volatility models, originating with Wishart processes (Bru, [1991](https://arxiv.org/html/2602.01376v1#bib.bib7 "Wishart processes")), provide affine multivariate dynamics and lead to matrix Riccati equations for transforms; see, e.g., Gourieroux and Sufana ([2010](https://arxiv.org/html/2602.01376v1#bib.bib8 "Derivative pricing with wishart multivariate stochastic volatility")). These approaches work well for modeling multiple correlated assets which all follow Heston processes, but not as well for modeling a single asset with stochastic correlation: we could not find an example of a model that remained affine and also allowed for a separate parameter that controls correlation volatility and risk reversal beta.

## 15 Conclusions and Future Work

We have introduced a variation of the Double Heston model that adds stochastic, mean-reverting spot/volatility correlation to the Heston model. That stochastic correlation is itself correlated with moves in the asset spot price, which we demonstrated is an important dynamic for barrier option pricing.

The model admits fast European vanilla option pricing, aiding in model calibration: like with the Heston model, our model admits a closed-form expression for the characteristic function of the log-spot, and vanilla options can be priced with a single numerical integration.

We derived an expression for the risk reversal beta in this model and compared it to the values we observed in the EURUSD and USDJPY foreign exchange markets. We then used those results to estimate the model parameter η\eta that controls the volatility of the spot/volatility correlation.

We also showed how one touch and out-of-the-money knockout option prices in those markets are affected by increasing the volatility of spot/volatility correlation, assuming that the model stays calibrated to a fixed set of vanilla option implied volatilities, and discussed why the sign and magnitude of those effects were expected based on hedging arguments. The price impacts of stochastic spot/volatility correlation are comparable or larger than the bid/ask spread for these derivatives.

We also considered pricing of volatility swaps, another liquid exotic product in the foreign exchange markets. Volatility swap fair strikes are sensitive to the volatility of volatility, and increasing the spot/volatility correlation volatility η\eta reduces the volatility of volatility required to match the market implied volatility smile. This means that the fair strike of a volatility swap should increase as η\eta increases.

An interesting consequence of this model is that adding stochastic spot/volatility correlation always increases the prices of one touch and knockout options, assuming the model is calibrated to market vanilla option prices. This should be concerning to market makers using the Heston model to price and manage risk for these derivatives, as they may find themselves selling these derivatives at below-market prices. Similarly, it increases the fair strike of volatility swaps, so market makers using the Heston model to price volatility swaps risk selling them below market levels.

One path for future work is to generalize the model to have parameters that are piecewise-constant in calendar time to allow a full term structure calibration to implied volatilities of different strikes and expiration dates. The pricing impact of implied volatility term structure on a barrier option can be significant. In addition, generalizing the model to calibrate cleanly to both 25- and 10-delta implied volatilities, instead of just 25-delta volatilities, would be a useful extension, as 10-delta volatilities are regularly quoted in the FX market.

Another path for future work is to look at traded prices of barrier derivatives in the FX inter-bank market and see whether their prices are better approximated with this model than with other kinds of model used in practice to incorporate this effect, such as stochastic volatility/local volatility mixture models.

## Appendixes

## Appendix A Closed-Form Solution of the Model Riccati System

### A.1 Key Definitions and Notation

Define the two limiting correlations

|  |  |  |
| --- | --- | --- |
|  | ρ+:=ρ¯+η,ρ−:=ρ¯−η\rho\_{+}:=\bar{\rho}+\eta,\qquad\rho\_{-}:=\bar{\rho}-\eta |  |

For each sign ±\pm, define the complex constants (depending on ξ\xi, the Fourier argument of the characteristic function)

|  |  |  |
| --- | --- | --- |
|  | b±​(ξ):=β−i​ξ​α​ρ±,d±​(ξ):=b±​(ξ)2+α2​(ξ2+i​ξ),g±​(ξ):=b±​(ξ)−d±​(ξ)b±​(ξ)+d±​(ξ)b\_{\pm}(\xi):=\beta-i\xi\,\alpha\,\rho\_{\pm},\qquad d\_{\pm}(\xi):=\sqrt{b\_{\pm}(\xi)^{2}+\alpha^{2}(\xi^{2}+i\xi)},\qquad g\_{\pm}(\xi):=\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{b\_{\pm}(\xi)+d\_{\pm}(\xi)} |  |

We take the square-root branch such that ℜ⁡(d±​(ξ))≥0\Re(d\_{\pm}(\xi))\geq 0 (standard for stability in affine models).

### A.2 Solving the Riccati Equations for B±B\_{\pm}

#### A.2.1 Put each B±B\_{\pm} into canonical Riccati form

Fix a sign ±\pm and write B​(τ):=B±​(τ;ξ)B(\tau):=B\_{\pm}(\tau;\xi), ρ:=ρ±\rho:=\rho\_{\pm}. The ODE is

|  |  |  |
| --- | --- | --- |
|  | B′​(τ)=−12​(ξ2+i​ξ)+(i​ξ​α​ρ−β)​B​(τ)+12​α2​B​(τ)2B^{\prime}(\tau)=-\tfrac{1}{2}(\xi^{2}+i\xi)+(i\xi\alpha\rho-\beta)B(\tau)+\tfrac{1}{2}\alpha^{2}B(\tau)^{2} |  |

Using b=β−i​ξ​α​ρb=\beta-i\xi\alpha\rho (so i​ξ​α​ρ−β=−bi\xi\alpha\rho-\beta=-b), this is

|  |  |  |
| --- | --- | --- |
|  | B′​(τ)=−12​(ξ2+i​ξ)−b​B​(τ)+12​α2​B​(τ)2B^{\prime}(\tau)=-\tfrac{1}{2}(\xi^{2}+i\xi)-b\,B(\tau)+\tfrac{1}{2}\alpha^{2}B(\tau)^{2} |  |

Equivalently,

|  |  |  |
| --- | --- | --- |
|  | B′​(τ)=12​α2​B​(τ)2−b​B​(τ)−12​(ξ2+i​ξ)B^{\prime}(\tau)=\tfrac{1}{2}\alpha^{2}B(\tau)^{2}-b\,B(\tau)-\tfrac{1}{2}(\xi^{2}+i\xi) |  |

#### A.2.2 Factorization by the quadratic roots

Consider the quadratic polynomial in BB:

|  |  |  |
| --- | --- | --- |
|  | Q​(B):=12​α2​B2−b​B−12​(ξ2+i​ξ)Q(B):=\tfrac{1}{2}\alpha^{2}B^{2}-bB-\tfrac{1}{2}(\xi^{2}+i\xi) |  |

Its discriminant is

|  |  |  |
| --- | --- | --- |
|  | Δ=b2+α2​(ξ2+i​ξ)=d2,d:=b2+α2​(ξ2+i​ξ)\Delta=b^{2}+\alpha^{2}(\xi^{2}+i\xi)=d^{2},\qquad d:=\sqrt{b^{2}+\alpha^{2}(\xi^{2}+i\xi)} |  |

The roots are

|  |  |  |
| --- | --- | --- |
|  | r1=b+dα2,r2=b−dα2r\_{1}=\frac{b+d}{\alpha^{2}},\qquad r\_{2}=\frac{b-d}{\alpha^{2}} |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | Q​(B)=12​α2​(B−r1)​(B−r2),and henceB′​(τ)=12​α2​(B−r1)​(B−r2).Q(B)=\tfrac{1}{2}\alpha^{2}(B-r\_{1})(B-r\_{2}),\qquad\text{and hence}\qquad B^{\prime}(\tau)=\tfrac{1}{2}\alpha^{2}(B-r\_{1})(B-r\_{2}). |  |

#### A.2.3 Separation of variables and explicit solution

Separate variables:

|  |  |  |
| --- | --- | --- |
|  | d​B(B−r1)​(B−r2)=12​α2​d​τ\frac{dB}{(B-r\_{1})(B-r\_{2})}=\tfrac{1}{2}\alpha^{2}\,d\tau |  |

Using the partial fraction identity

|  |  |  |
| --- | --- | --- |
|  | 1(B−r1)​(B−r2)=1r1−r2​(1B−r1−1B−r2)\frac{1}{(B-r\_{1})(B-r\_{2})}=\frac{1}{r\_{1}-r\_{2}}\left(\frac{1}{B-r\_{1}}-\frac{1}{B-r\_{2}}\right) |  |

integrate to obtain

|  |  |  |
| --- | --- | --- |
|  | 1r1−r2​ln⁡(B​(τ)−r1B​(τ)−r2)=12​α2​τ+C\frac{1}{r\_{1}-r\_{2}}\ln\!\left(\frac{B(\tau)-r\_{1}}{B(\tau)-r\_{2}}\right)=\tfrac{1}{2}\alpha^{2}\,\tau+C |  |

Since r1−r2=2​dα2r\_{1}-r\_{2}=\frac{2d}{\alpha^{2}}, we have 12​α2​(r1−r2)=d\tfrac{1}{2}\alpha^{2}(r\_{1}-r\_{2})=d, hence

|  |  |  |
| --- | --- | --- |
|  | ln⁡(B​(τ)−r1B​(τ)−r2)=d​τ+C′\ln\!\left(\frac{B(\tau)-r\_{1}}{B(\tau)-r\_{2}}\right)=d\tau+C^{\prime} |  |

Impose B​(0)=0B(0)=0:

|  |  |  |
| --- | --- | --- |
|  | −r1−r2=r1r2=eC′\frac{-r\_{1}}{-r\_{2}}=\frac{r\_{1}}{r\_{2}}=e^{C^{\prime}} |  |

Thus

|  |  |  |
| --- | --- | --- |
|  | B​(τ)−r1B​(τ)−r2=r1r2​ed​τ\frac{B(\tau)-r\_{1}}{B(\tau)-r\_{2}}=\frac{r\_{1}}{r\_{2}}e^{d\tau} |  |

Solving this algebraically for B​(τ)B(\tau) and rewriting in the numerically stable e−d​τe^{-d\tau} form yields

|  |  |  |
| --- | --- | --- |
|  | B​(τ)=r2​1−e−d​τ1−r2r1​e−d​τ=b−dα2​1−e−d​τ1−g​e−d​τ,g=r2r1=b−db+d\boxed{B(\tau)=r\_{2}\,\frac{1-e^{-d\tau}}{1-\frac{r\_{2}}{r\_{1}}e^{-d\tau}}=\frac{b-d}{\alpha^{2}}\,\frac{1-e^{-d\tau}}{1-ge^{-d\tau}},\qquad g=\frac{r\_{2}}{r\_{1}}=\frac{b-d}{b+d}} |  |

#### A.2.4 Apply to B+B\_{+} and B−B\_{-}

Therefore, for ±∈{+,−}\pm\in\{+,-\},

|  |  |  |
| --- | --- | --- |
|  | B±​(τ;ξ)=b±​(ξ)−d±​(ξ)α2​1−e−d±​(ξ)​τ1−g±​(ξ)​e−d±​(ξ)​τ,b±​(ξ)=β−i​ξ​α​ρ±\boxed{B\_{\pm}(\tau;\xi)=\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{\alpha^{2}}\,\frac{1-e^{-d\_{\pm}(\xi)\tau}}{1-g\_{\pm}(\xi)\,e^{-d\_{\pm}(\xi)\tau}},\qquad b\_{\pm}(\xi)=\beta-i\xi\alpha\rho\_{\pm}} |  |

### A.3 ClosedForm Solution for A​(τ;ξ)A(\tau;\xi)

#### A.3.1 Reduce to integrating B±B\_{\pm}

From the first ODE,

|  |  |  |
| --- | --- | --- |
|  | A​(τ;ξ)=∫0τ(i​ξ​(r−q)+β​(θ+​B+​(s;ξ)+θ−​B−​(s;ξ)))​𝑑sA(\tau;\xi)=\int\_{0}^{\tau}\left(i\xi(r-q)+\beta(\theta\_{+}B\_{+}(s;\xi)+\theta\_{-}B\_{-}(s;\xi))\right)\,ds |  |

so

|  |  |  |
| --- | --- | --- |
|  | A​(τ;ξ)=i​ξ​(r−q)​τ+β​(θ+​∫0τB+​(s;ξ)​𝑑s+θ−​∫0τB−​(s;ξ)​𝑑s)A(\tau;\xi)=i\xi(r-q)\tau+\beta\left(\theta\_{+}\int\_{0}^{\tau}B\_{+}(s;\xi)\,ds+\theta\_{-}\int\_{0}^{\tau}B\_{-}(s;\xi)\,ds\right) |  |

Thus it suffices to compute ∫0τB​(s)​𝑑s\int\_{0}^{\tau}B(s)\,ds for the generic closed-form B​(s)=b−dα2​1−e−d​s1−g​e−d​sB(s)=\frac{b-d}{\alpha^{2}}\frac{1-e^{-ds}}{1-ge^{-ds}}.

#### A.3.2 Explicit primitive of BB

Let b,d,gb,d,g correspond to one of the signs ±\pm. Define

|  |  |  |
| --- | --- | --- |
|  | B​(s)=b−dα2​1−e−d​s1−g​e−d​sB(s)=\frac{b-d}{\alpha^{2}}\frac{1-e^{-ds}}{1-ge^{-ds}} |  |

A direct rational substitution (set y=e−d​sy=e^{-ds}) gives the elementary antiderivative

|  |  |  |
| --- | --- | --- |
|  | ∫0τB​(s)​𝑑s=b−dα2​τ−2α2​ln⁡(1−g​e−d​τ1−g)\boxed{\int\_{0}^{\tau}B(s)\,ds=\frac{b-d}{\alpha^{2}}\,\tau-\frac{2}{\alpha^{2}}\ln\!\left(\frac{1-ge^{-d\tau}}{1-g}\right)} |  |

(One checks the constant by evaluating at τ=0\tau=0, where the logarithm vanishes and the integral is 0.)

#### A.3.3 Assemble A​(τ;ξ)A(\tau;\xi)

Applying the above to both components,

|  |  |  |
| --- | --- | --- |
|  | A​(τ;ξ)=i​ξ​(r−q)​τ+β​∑±θ±​[b±​(ξ)−d±​(ξ)α2​τ−2α2​ln⁡(1−g±​(ξ)​e−d±​(ξ)​τ1−g±​(ξ))]\boxed{\begin{aligned} A(\tau;\xi)&=i\xi(r-q)\tau+\beta\sum\_{\pm}\theta\_{\pm}\left[\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{\alpha^{2}}\,\tau-\frac{2}{\alpha^{2}}\ln\!\left(\frac{1-g\_{\pm}(\xi)\,e^{-d\_{\pm}(\xi)\tau}}{1-g\_{\pm}(\xi)}\right)\right]\end{aligned}} |  |

### A.4 Final Closed-Form Characteristic Function

With τ=T−t\tau=T-t and ρ±=ρ¯±η\rho\_{\pm}=\bar{\rho}\pm\eta, define

|  |  |  |
| --- | --- | --- |
|  | b±​(ξ)=β−i​ξ​α​ρ±,d±​(ξ)=b±​(ξ)2+α2​(ξ2+i​ξ),g±​(ξ)=b±​(ξ)−d±​(ξ)b±​(ξ)+d±​(ξ)b\_{\pm}(\xi)=\beta-i\xi\alpha\rho\_{\pm},\qquad d\_{\pm}(\xi)=\sqrt{b\_{\pm}(\xi)^{2}+\alpha^{2}(\xi^{2}+i\xi)},\qquad g\_{\pm}(\xi)=\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{b\_{\pm}(\xi)+d\_{\pm}(\xi)} |  |

Then the Riccati solutions are

|  |  |  |
| --- | --- | --- |
|  | B±​(τ;ξ)=b±​(ξ)−d±​(ξ)α2​1−e−d±​(ξ)​τ1−g±​(ξ)​e−d±​(ξ)​τ\boxed{B\_{\pm}(\tau;\xi)=\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{\alpha^{2}}\,\frac{1-e^{-d\_{\pm}(\xi)\tau}}{1-g\_{\pm}(\xi)e^{-d\_{\pm}(\xi)\tau}}} |  |

and

|  |  |  |
| --- | --- | --- |
|  | A​(τ;ξ)=i​ξ​(r−q)​τ+β​∑±θ±​[b±​(ξ)−d±​(ξ)α2​τ−2α2​ln⁡(1−g±​(ξ)​e−d±​(ξ)​τ1−g±​(ξ))]\boxed{A(\tau;\xi)=i\xi(r-q)\tau+\beta\sum\_{\pm}\theta\_{\pm}\left[\frac{b\_{\pm}(\xi)-d\_{\pm}(\xi)}{\alpha^{2}}\,\tau-\frac{2}{\alpha^{2}}\ln\!\left(\frac{1-g\_{\pm}(\xi)e^{-d\_{\pm}(\xi)\tau}}{1-g\_{\pm}(\xi)}\right)\right]} |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ei​ξ​XT∣ℱt]=exp⁡(A​(τ;ξ)+B+​(τ;ξ)​vt++B−​(τ;ξ)​vt−+i​ξ​Xt)\boxed{\mathbb{E}\!\left[e^{i\xi X\_{T}}\mid\mathcal{F}\_{t}\right]=\exp\!\left(A(\tau;\xi)+B\_{+}(\tau;\xi)v\_{t}^{+}+B\_{-}(\tau;\xi)v\_{t}^{-}+i\xi X\_{t}\right)} |  |

## References

* L. B. G. Andersen (2008)
  Simple and efficient simulation of the heston stochastic volatility model.
  Journal of Computational Finance 11 (3),  pp. 1–42.
  External Links: [Link](https://www.risk.net/journal-of-computational-finance/2160370/simple-and-efficient-simulation-of-the-heston-stochastic-volatility-model),
  [Document](https://dx.doi.org/10.21314/JCF.2008.189)
  Cited by: [§12.1](https://arxiv.org/html/2602.01376v1#S12.SS1.p2.1 "12.1 Model Barrier Pricing ‣ 12 Barrier Option Pricing and the Risk Reversal Beta ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* F. Black and M. Scholes (1973)
  The pricing of options and corporate liabilities.
  Journal of Political Economy 81 (3),  pp. 637–654.
  External Links: [Document](https://dx.doi.org/10.1086/260062)
  Cited by: [§1](https://arxiv.org/html/2602.01376v1#S1.p1.1 "1 Introduction ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing"),
  [§14](https://arxiv.org/html/2602.01376v1#S14.p1.1 "14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* M. Bru (1991)
  Wishart processes.
  Journal of Theoretical Probability 4 (4),  pp. 725–751.
  External Links: [Document](https://dx.doi.org/10.1007/bf01259552)
  Cited by: [§14.4](https://arxiv.org/html/2602.01376v1#S14.SS4.p1.1 "14.4 Affine Matrix Models and Wishart Stochastic Volatility ‣ 14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* P. Carr and D. B. Madan (1999)
  Option valuation using the fast fourier transform.
  Journal of Computational Finance 2 (4),  pp. 61–73.
  External Links: [Document](https://dx.doi.org/10.21314/JCF.1999.043)
  Cited by: [§8.3](https://arxiv.org/html/2602.01376v1#S8.SS3.p10.1 "8.3 Closed-Form Solution to the Riccati ODEs ‣ 8 European Vanilla Option Pricing ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* P. Christoffersen, S. Heston, and K. Jacobs (2009)
  The shape and term structure of the index option smirk: why multifactor stochastic volatility models work so well.
  Management Science 55 (12),  pp. 1914–1932.
  External Links: [Document](https://dx.doi.org/10.1287/mnsc.1090.1065)
  Cited by: [§14.1](https://arxiv.org/html/2602.01376v1#S14.SS1.p1.1 "14.1 The Double Heston Model ‣ 14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing"),
  [§2](https://arxiv.org/html/2602.01376v1#S2.p10.1 "2 The Model ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing"),
  [Keeping Up with the Correlations  Stochastic Spot/Volatility Correlation and Exotic Pricing](https://arxiv.org/html/2602.01376v1#id3.id1 "Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* K. Demeterfi, E. Derman, M. Kamal, and J. Zou (1999)
  A guide to volatility and variance swaps.
  The Journal of Derivatives 6 (4),  pp. 9–32.
  External Links: [Document](https://dx.doi.org/10.3905/jod.1999.319129)
  Cited by: [§13.2](https://arxiv.org/html/2602.01376v1#S13.SS2.p1.1 "13.2 Volatility Swaps and Volatility of Volatility Sensitivity ‣ 13 Volatility Swap Fair Strikes and the Risk Reversal Beta ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* C. Gourieroux and R. Sufana (2010)
  Derivative pricing with wishart multivariate stochastic volatility.
  Journal of Business & Economic Statistics 28 (3),  pp. 438–451.
  External Links: [Document](https://dx.doi.org/10.1198/jbes.2009.08105)
  Cited by: [§14.4](https://arxiv.org/html/2602.01376v1#S14.SS4.p1.1 "14.4 Affine Matrix Models and Wishart Stochastic Volatility ‣ 14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* S. L. Heston (1993)
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  The Review of Financial Studies 6 (2),  pp. 327–343.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/6.2.327)
  Cited by: [§14](https://arxiv.org/html/2602.01376v1#S14.p1.1 "14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing"),
  [Keeping Up with the Correlations  Stochastic Spot/Volatility Correlation and Exotic Pricing](https://arxiv.org/html/2602.01376v1#id4.id2 "Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* A. Lipton, A. Gal, and A. Lasis (2014)
  Pricing of vanilla and first-generation exotic options in the local stochastic volatility framework: survey and new results.
  Quantitative Finance 14 (11),  pp. 1899–1922.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2014.930965)
  Cited by: [§14.3](https://arxiv.org/html/2602.01376v1#S14.SS3.p2.1 "14.3 Stochastic Volatility/Local Volatility Mixture Models ‣ 14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* R. Lord, R. Koekkoek, and D. van Dijk (2010)
  A comparison of biased simulation schemes for stochastic volatility models.
  Quantitative Finance 10 (2),  pp. 177–194.
  External Links: [Document](https://dx.doi.org/10.1080/14697680802392496),
  [Link](https://doi.org/10.1080/14697680802392496)
  Cited by: [§10](https://arxiv.org/html/2602.01376v1#S10.p8.5 "10 Model Calibration ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* L. Teng, M. Ehrhardt, and M. Günther (2016)
  On the heston model with stochastic correlation.
  International Journal of Theoretical and Applied Finance 19 (06),  pp. 1650033.
  External Links: [Document](https://dx.doi.org/10.1142/S0219024916500333)
  Cited by: [§14.2](https://arxiv.org/html/2602.01376v1#S14.SS2.p1.1 "14.2 Stochastic Correlation in Heston-Type Models ‣ 14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* L. Teng, M. Ehrhardt, and M. Günther (2018)
  Numerical simulation of the heston model under stochastic correlation.
  International Journal of Financial Studies 6 (1),  pp. 3.
  External Links: [Document](https://dx.doi.org/10.3390/ijfs6010003)
  Cited by: [§14.2](https://arxiv.org/html/2602.01376v1#S14.SS2.p1.1 "14.2 Stochastic Correlation in Heston-Type Models ‣ 14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").
* A. W. van der Stoep, L. A. Grzelak, and C. W. Oosterlee (2014)
  The Heston stochastic-local volatility model: efficient monte carlo simulation.
  International Journal of Theoretical and Applied Finance 17 (7),  pp. 1450045.
  External Links: [Document](https://dx.doi.org/10.1142/S0219024914500459)
  Cited by: [§14.3](https://arxiv.org/html/2602.01376v1#S14.SS3.p2.1 "14.3 Stochastic Volatility/Local Volatility Mixture Models ‣ 14 Related Literature and Model Context ‣ Keeping Up with the Correlations Stochastic Spot/Volatility Correlation and Exotic Pricing").