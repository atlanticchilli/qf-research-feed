---
authors:
- Peter Carr
- Zhibai Zhang
doc_id: arxiv:1809.02245v1
family_id: arxiv:1809.02245
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[1809.02245] 1 Introduction'
url_abs: http://arxiv.org/abs/1809.02245v1
url_html: https://ar5iv.org/html/1809.02245v1
venue: arXiv q-fin
version: 1
year: 2018
---

Generalizing Geometric Brownian Motion

Peter Carr, Zhibai Zhang

Department of Finance and Risk Engineering
  
Tandon School of Engineering
  
New York University
  
12 Metro Tech Center
  
Brooklyn NY 11201, USA

pcarr@nyc.rr.com
  
z.zihbai@gmail.com

To convert standard Brownian motion Z𝑍Z into a positive process,
Geometric Brownian motion (GBM) eβ​Zt,β>0

superscript𝑒𝛽subscript𝑍𝑡𝛽
0e^{\beta Z\_{t}},\beta>0 is widely used.
We generalize this positive process
by introducing an asymmetry parameter α≥0𝛼0\alpha\geq 0
which describes the instantaneous volatility whenever the process reaches a new low.
For our new process, β𝛽\beta is the instantaneous volatility
as prices become arbitrarily high.
Our generalization preserves the positivity, constant proportional drift, and tractability of GBM, while expressing the instantaneous volatility as a randomly weighted
L2superscript𝐿2L^{2} mean of
α𝛼\alpha and β𝛽\beta. The running minimum and relative drawup of this process are also analytically tractable. Letting α=β𝛼𝛽\alpha=\beta, our positive process reduces to Geometric Brownian motion. By adding a jump to default to the new process, we introduce a non-negative martingale with the same tractabilities. Assuming a security’s dynamics are driven by these processes in risk neutral measure, we price several derivatives including vanilla, barrier and lookback options.

## 1 Introduction

Stochastic processes are used in option pricing models for multiple purposes.
A very common purpose is smile interpolation and extrapolation.
Given several co-terminal market quotes, the objective here is to
produce implied volatilities at a continuum of strike prices or delta levels.
A second purpose is to value path-dependent contingent claims such as
quantoed forward contracts or barrier options.
For both purposes, it is well known that
arbitrage is avoided so long as all relative price
processes
are specified as martingales under the appropriate probability measure.

In general, arbitrages can either be model-based or model-free.
An example of a model-free arbitrage is a violation of
put call parity.
An example of a model-based arbitrage is when two
European-style futures options have different implied volatilities in
the Black model.
A martingale specification produces prices that are free of both types of arbitrage.
For example, using driftless geometric Brownian motion to describe
a futures price under the futures measure ℚℚ\mathbb{Q}
leads to both put call parity holding and
to equal implied volatilities across strikes and maturity.

Suppose that a market maker uses one martingale specification on
an initial date and then uses a different martingale specification on a second date.
For example suppose that a market maker uses
a geometric Brownian martingale with 10% volatility
on the first date and then uses a
geometric Brownian martingale with 20% volatility
on the second date.
The prices produced on both dates are devoid of model-free arbitrages.
For example put call parity will hold on both dates.
The prices produced on both dates do produce an arbitrage
based on the Black model being correct.
For example, if the actual volatility in the Black model is constant at 10%, then the prices
produced on the second day allow model-based arbitrage.
If the actual volatility is instead constant at 20%, then the prices
produced on the first day allow model-based arbitrage.
If the actual volatility is instead constant at some other value e.g. 15%,
then the prices produced on both days allow arbitrage
based on the Black model being correct.
However, if the Black model is not describing the risk-neutral dynamics of the
underlying, then the market maker’s use
of time-inconsistent martingale specifications need not produce
any model-based arbitrages.
Nonetheless, the use of
time-inconsistent martingale specifications does produce
a set of values that are devoid of
model-free arbitrages.

When the only goal is to produce values
that are devoid of
model-free arbitrages,
the only challenge to be met is to be consistent with
all of the liquid and transparent quotes.
For this purpose, time-inconsistent martingale specifications
offer greater flexibility than a time-consistent specification.
A market maker using the Black model with the same volatility on
both dates is unlikely to be able to match the ATM quote on both dates.
In contrast, a market maker using the Black model
with the ability to change the volatility on the second date
is guaranteed to be able to match the ATM quotes on both dates.
In contrast this time-inconsistent Black model does not
guarantee the ability to match
more than one option price on any given date.
When two or more simultaneous quotes differ in maturity,
and are devoid of model-free arbitrage,
one can match them by moving from the constant
volatility model to the deterministic volatility Black model.
However, when two co-terminal quotes differ in strike
and are devoid of model-free arbitrage,
one cannot necessarily match them with
the deterministic volatility Black model.
A different type of martingale specification is required to guarantee a match.

In choosing an alternative martingale specification,
it is wise to understand the reasons
behind the success of the
Geometric Brownian Martingale as the benchmark process.
Once these reasons are understood, it becomes clearer
as to which
properties of GBM should be kept
and which properties should be jettisoned.
For example, at first glance, driftless arithmetic Brownian motion
(ABM)
appears to be an attractive alternative to driftless GBM due to its
simplicity and tractability.
However, it is widely agreed that the failure
of ABM to preserve the positivity property
of GBM makes it unviable as an alternative.
It is widely argued that this positivity property of GBM
makes it a good first approximation in
describing market prices of assets whose owners enjoy
limited liability.
However, GBM has state space (0,∞)0(0,\infty) while
prices of limited liability assets occupy [0,∞)0[0,\infty).
To capture the possibility that the price of a
limited liability asset can vanish, one
can add a jump to default to a GBM, as done in [[5](#bib.bib5)].

The GBM remains appropriate as a toy model
for a stock index, where it is widely agreed that zero is inaccessible.
The inaccessibility of the origin for GBM also makes it
a good toy model for an exchange rate, since if X𝑋X is an exchange rate,
1X1𝑋\frac{1}{X} needs to be well defined.
For a driftless GBM, its state space and dynamics
are preserved upon inversion of the coordinate and
a change of probability measure.
In foreign exchange (FX) markets, inverting an FX rate is a natural operation and
the change in probability measure
corresponds to a change of numeraire.
It is highly likely that these invariance properties of GBM
explain why this stochastic process plays such a large role in the FX options
market.
If one wants to address deficiencies of GBM while retaining applicability to
FX options pricing, it stands to reason that
preserving at least some notion of invariance under inversion is crucial.
The purpose of this paper is to propose a process that generalizes GBM while
respecting invariance under inversion.
Not surprisingly, hyperbolic functions play a large role in our analysis.

It is helpful to begin by reviewing some well-known properties of GBM.
Consider an arbitrage-free market and let ℚℚ\mathbb{Q}
be an equivalent martingale measure.
Let Z𝑍Z denote standard Brownian motion on the real line
under ℚℚ\mathbb{Q}. Consider the
process gt=eβ​Zt,t≥0formulae-sequencesubscript𝑔𝑡superscript𝑒𝛽subscript𝑍𝑡𝑡0g\_{t}=e^{\beta Z\_{t}},t\geq 0, where β>0𝛽0\beta>0.
Clearly, the process g𝑔g starts at one and stays positive forever.
From Itô’s formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​gtgt=β22​d​t+β​d​Zt,t≥0.formulae-sequence𝑑subscript𝑔𝑡subscript𝑔𝑡superscript𝛽22𝑑𝑡𝛽𝑑subscript𝑍𝑡𝑡0\frac{dg\_{t}}{g\_{t}}=\frac{\beta^{2}}{2}dt+\beta dZ\_{t},\qquad t\geq 0. |  | (1) |

We say the process g𝑔g has constant proportional drift at
rate β22superscript𝛽22\frac{\beta^{2}}{2} and constant proportional variance at rate β2superscript𝛽2\beta^{2}.
The parameter β𝛽\beta is called the volatility.
The process g𝑔g is called Geometric Brownian motion.

To obtain a non-negative martingale from g𝑔g, there are at least three approaches.
First, one can change the probability measure from ℚℚ\mathbb{Q}
to ℚ~~ℚ\tilde{\mathbb{Q}} by setting
d​ℚ~d​ℚ=e−β2​ZT−β24​T𝑑~ℚ𝑑ℚsuperscript𝑒𝛽2subscript𝑍𝑇superscript𝛽24𝑇\frac{d\tilde{\mathbb{Q}}}{d\mathbb{Q}}=e^{-\frac{\beta}{2}Z\_{T}-\frac{\beta^{2}}{4}T}.
Second, one can alternatively change the coordinate
by setting Ft=gt​e−β2​t/2subscript𝐹𝑡subscript𝑔𝑡superscript𝑒superscript𝛽2𝑡2F\_{t}=g\_{t}e^{-\beta^{2}t/2}.
Both of these approaches to creating a martingale
preserve the strict positivity of g𝑔g.
If only non-negativity of the martingale is required, one can
alternatively add a jump to default to the g𝑔g process with arrival rate
β2/2superscript𝛽22\beta^{2}/2.

In this paper, we propose a positive process which generalizes
GBM gt=eβ​Zt,t≥0formulae-sequencesubscript𝑔𝑡superscript𝑒𝛽subscript𝑍𝑡𝑡0g\_{t}=e^{\beta Z\_{t}},t\geq 0 by adding
an asymmetry parameter α≥0𝛼0\alpha\geq 0.
For our new process,
α𝛼\alpha
describes the instantaneous volatility whenever a new low is reached.
while β𝛽\beta is the instantaneous volatility
whenever the process becomes arbitrarily high.
Our generalization preserves the positivity, constant proportional drift, and tractability of GBM, while expressing the instantaneous variance rate at any time as a convex combination of
α2superscript𝛼2\alpha^{2} and β2superscript𝛽2\beta^{2}.
The model actually allows a third parameter γ𝛾\gamma which is
the initial instantaneous volatility, and hence
is required to lie
between α𝛼\alpha and β𝛽\beta.

For many options markets, three parameter models are widely used to
interpolate and extrapolate implied volatilities across strikes.
Intuitively, market participants agree that options markets
display nonzero skewness and kurtosis, but there is little discussion
about moments higher than the fourth power.
Put another way, market participants agree that it is necessary to match
some measure of level, slope, and convexity of implied volatility at the money,
but there is little discussion about the third or higher derivative of implied volatility.

Unfortunately, our particular three parameter model is
not as flexible as some other three parameter models e.g. SABR with fixed
β𝛽\beta or ρ𝜌\rho. As a result, our three parameter model is
only suitable for options markets where
the implied volatility slice appears to be monotone across strike e.g. SPX or VIX.
For non-monotone slices such as when implied volatilities smile, one must alter
the model by adding e.g. stochastic volatility.
So long as the implied volatility slice appears to be monotone across strike price,
our three parameters, α≥0𝛼0\alpha\geq 0, β>0𝛽0\beta>0 and
γ≥0𝛾0\gamma\geq 0 have distinct and well-defined roles.
The parameter α𝛼\alpha controls the asymptotic implied volatility at low strikes,
while the parameter β𝛽\beta controls the asymptotic
implied volatility at high strikes.
The parameter γ𝛾\gamma is used to meet an at-the-money implied volatility.

An overview of this paper is as follows.
The next section develops a new special function called
the two parameter exponential function.
The following section first uses this special function to construct a positive contibuous sub-martingale that has a constant drift.
Then we introduce a non-negative martingale
by adding a jump to default process to the sub-martingale.
This martingale has three parameters
α≥0𝛼0\alpha\geq 0, β>0𝛽0\beta>0, and γ𝛾\gamma between α𝛼\alpha and β𝛽\beta.
This is followed by derivations of the transition PDF’s for the new martingale.
The penultimate section presents closed form valuation formulas for
contingent claims written on these martingales.
In particular, we examine vanilla options,
lookback options and barrier options.
The final section provides both a summary of the paper
and some suggestions for future research.

## 2 Two Parameter Exponential Function

In this section, we construct a new
special function which we call a two parameter exponential function.
In the next section, we will use this special function to
construct our three parameter martingale.
For β>0𝛽0\beta>0, let y=eβ​x𝑦superscript𝑒𝛽𝑥y=e^{\beta x} be the standard one parameter exponential function.
While the function is defined for β∈ℂ𝛽ℂ\beta\in\mathbb{C} and
x∈ℂ𝑥ℂx\in\mathbb{C}, we consider it only for
β∈ℝ+𝛽superscriptℝ\beta\in\mathbb{R}^{+} and
x∈ℝ+𝑥superscriptℝx\in\mathbb{R}^{+}.
The defining characteristics
of eβ​xsuperscript𝑒𝛽𝑥e^{\beta x} are that the ratio of the function’s slope to its height is constant at β>0𝛽0\beta>0 for all x≥0𝑥0x\geq 0 and that the function has unit height at x=0𝑥0x=0 for all β>0𝛽0\beta>0.
Accordingly, our two parameter exponential function
will have unit height at x=0𝑥0x=0 for all values of its two parameters
α≥0𝛼0\alpha\geq 0 and β>0𝛽0\beta>0. We will show that the
ratio of the function’s slope to its height is α≥0𝛼0\alpha\geq 0 at
x=0𝑥0x=0 and approaches β>0𝛽0\beta>0 as x↑∞↑𝑥x\uparrow\infty.
Since infinitely many functions meet just these criteria,
we further require that the ratio of the function’s curvature to its height
be constant at β2>0superscript𝛽20\beta^{2}>0 for all x≥0𝑥0x\geq 0.
This property also belongs to
the one parameter exponential function and
serves to uniquely111Our special function f​(x)𝑓𝑥f(x) solves the ordinary differential equation
f′′​(x)=β2​f​(x)superscript𝑓′′𝑥superscript𝛽2𝑓𝑥f^{\prime\prime}(x)=\beta^{2}f(x) on x≥0𝑥0x\geq 0 subject to the Dirichlet boundary
condition f​(0)=1𝑓01f(0)=1 and the Neumann boundary condition f′​(0)=αsuperscript𝑓′0𝛼f^{\prime}(0)=\alpha.
determine our two parameter exponential function.

For x≥0𝑥0x\geq 0, β>0𝛽0\beta>0, and α≥0𝛼0\alpha\geq 0,
we define222Our function can also be expressed as cosh⁡(β​x)+αβ​sinh⁡(β​x),x≥0,α≥0,β>0formulae-sequence

𝛽𝑥𝛼𝛽𝛽𝑥𝑥
0formulae-sequence𝛼0𝛽0\cosh(\beta x)+\frac{\alpha}{\beta}\sinh(\beta x),x\geq 0,\alpha\geq 0,\beta>0
and so its properties will arise as a consequence of such a representation. the two parameter exponential function by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ−αβ​x≡β+α2​β​eβ​x+β−α2​β​e−β​x.subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛽𝛼2𝛽superscript𝑒𝛽𝑥𝛽𝛼2𝛽superscript𝑒𝛽𝑥e^{\beta x}\_{\beta-\alpha}\equiv\frac{\beta+\alpha}{2\beta}e^{\beta x}+\frac{\beta-\alpha}{2\beta}e^{-\beta x}. |  | (2) |

Thus, the subscripted exponential is a
linear combination of
the ordinary exponential eβ​xsuperscript𝑒𝛽𝑥e^{\beta x} and its reciprocal.
The β−α𝛽𝛼\beta-\alpha subscript in
eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}
describes the numerator of the fraction multiplying
the reciprocal e−β​xsuperscript𝑒𝛽𝑥e^{-\beta x}.
The numerator of the fraction multiplying
eβ​xsuperscript𝑒𝛽𝑥e^{\beta x} is always the sum of the
asymmetry parameter α𝛼\alpha and the
scaling factor
β𝛽\beta in the ordinary exponential eβ​xsuperscript𝑒𝛽𝑥e^{\beta x}.
The common denominator of both fractions
is twice this scaling factor β𝛽\beta.
These rules uniquely expand the LHS of ([2](#S2.E2 "In 2 Two Parameter Exponential Function")) into the RHS.

On our function’s domain x≥0𝑥0x\geq 0, the ordinary exponential
eβ​xsuperscript𝑒𝛽𝑥e^{\beta x}
in the linear combination is larger than its reciprocal
i.e. eβ​x≥e−β​xsuperscript𝑒𝛽𝑥superscript𝑒𝛽𝑥e^{\beta x}\geq e^{-\beta x}.
If α=0𝛼0\alpha=0, the two fractions simplify to one half and the function is
increasing and convex. Increasing α𝛼\alpha
increases the fraction multiplying the larger exponential eβ​xsuperscript𝑒𝛽𝑥e^{\beta x}
and decreases the fraction multiplying the smaller exponential e−β​xsuperscript𝑒𝛽𝑥e^{-\beta x}, while keeping the value of the function at x=0𝑥0x=0 fixed at one.
As a result, increasing α𝛼\alpha causes our special function to slope up faster at every x≥0𝑥0x\geq 0.
If α=β𝛼𝛽\alpha=\beta, then the two parameter exponential
e0β​xsubscriptsuperscript𝑒𝛽𝑥0e^{\beta x}\_{0} reduces to
the one parameter exponential eβ​xsuperscript𝑒𝛽𝑥e^{\beta x}.
Thus the subscript β−α𝛽𝛼\beta-\alpha
on eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha} is also a measure of the
deviation of our two parameter exponential function
from the one parameter exponential function.
Like the one parameter exponential function eβ​xsuperscript𝑒𝛽𝑥e^{\beta x},
the two parameter exponential function
eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}
defined by ([2](#S2.E2 "In 2 Two Parameter Exponential Function")) is
positive, increasing, and convex in x𝑥x
for all x≥0𝑥0x\geq 0 and for all
β>0𝛽0\beta>0.

The derivative w.r.t. x𝑥x of our two parameter exponential function is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​x​eβ−αβ​x=β​eα−ββ​x,α≥0,β>0,x≥0,formulae-sequence𝑑𝑑𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛽subscriptsuperscript𝑒𝛽𝑥𝛼𝛽formulae-sequence𝛼0formulae-sequence𝛽0𝑥0\frac{d}{dx}e^{\beta x}\_{\beta-\alpha}=\beta e^{\beta x}\_{\alpha-\beta},\qquad\alpha\geq 0,\beta>0,x\geq 0, |  | (3) |

where:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eα−ββ​x≡β+α2​β​eβ​x+α−β2​β​e−β​x,α≥0,β>0,x≥0.formulae-sequencesubscriptsuperscript𝑒𝛽𝑥𝛼𝛽𝛽𝛼2𝛽superscript𝑒𝛽𝑥𝛼𝛽2𝛽superscript𝑒𝛽𝑥formulae-sequence𝛼0formulae-sequence𝛽0𝑥0e^{\beta x}\_{\alpha-\beta}\equiv\frac{\beta+\alpha}{2\beta}e^{\beta x}+\frac{\alpha-\beta}{2\beta}e^{-\beta x},\qquad\alpha\geq 0,\beta>0,x\geq 0. |  | (4) |

At α=0𝛼0\alpha=0, eα−ββ​xsubscriptsuperscript𝑒𝛽𝑥𝛼𝛽e^{\beta x}\_{\alpha-\beta}
is the right arm of the hyperbolic sine and hence positive.
Increasing α𝛼\alpha increases the weight on both exponentials
and hence eα−ββ​x>0subscriptsuperscript𝑒𝛽𝑥𝛼𝛽0e^{\beta x}\_{\alpha-\beta}>0 for all
α≥0,β>0,x≥0formulae-sequence𝛼0formulae-sequence𝛽0𝑥0\alpha\geq 0,\beta>0,x\geq 0.
Since β>0𝛽0\beta>0 as well, ([3](#S2.E3 "In 2 Two Parameter Exponential Function")) implies that the derivative
dd​x​eβ−αβ​x𝑑𝑑𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼\frac{d}{dx}e^{\beta x}\_{\beta-\alpha} is positive.
Thus, the x𝑥x-derivative
of our two parameter exponential function
behaves the same way as the
x𝑥x-derivative of the ordinary
exponential function w.r.t to its
scaling factor β𝛽\beta.
Differentiating our two parameter exponential function
w.r.t. x𝑥x also switches the sign on the subscript.
To convert eα−ββ​xsubscriptsuperscript𝑒𝛽𝑥𝛼𝛽e^{\beta x}\_{\alpha-\beta} on the RHS of ([3](#S2.E3 "In 2 Two Parameter Exponential Function"))
back into an expression involving
its cohort eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}, one can again
differentiate w.r.t. x𝑥x.
In particular:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d2d​x2​eβ−αβ​x=β2​eβ−αβ​x,α≥0,β>0,x≥0.formulae-sequencesuperscript𝑑2𝑑superscript𝑥2subscriptsuperscript𝑒𝛽𝑥𝛽𝛼superscript𝛽2subscriptsuperscript𝑒𝛽𝑥𝛽𝛼formulae-sequence𝛼0formulae-sequence𝛽0𝑥0\frac{d^{2}}{dx^{2}}e^{\beta x}\_{\beta-\alpha}=\beta^{2}e^{\beta x}\_{\beta-\alpha},\qquad\alpha\geq 0,\beta>0,x\geq 0. |  | (5) |

Thus, the ratio of the function’s curvature to its height is constant
at β2>0superscript𝛽20\beta^{2}>0 for all x≥0𝑥0x\geq 0, as previously indicated.

There is an alternative way to convert
eα−ββ​xsubscriptsuperscript𝑒𝛽𝑥𝛼𝛽e^{\beta x}\_{\alpha-\beta} back into an expression involving
its cohort eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}.
The appendix shows that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eα−ββ​x=(eβ−αβ​x)2+α2−β2β2.subscriptsuperscript𝑒𝛽𝑥𝛼𝛽superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2superscript𝛼2superscript𝛽2superscript𝛽2e^{\beta x}\_{\alpha-\beta}=\sqrt{\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}+\frac{\alpha^{2}-\beta^{2}}{\beta^{2}}}. |  | (6) |

We now use this alternative conversion
mechanism to show that our
two parameter exponential function
sets the ratio of its slope to its height at
α𝛼\alpha at x=0𝑥0x=0.
We will also show in contrast that the ratio of its slope to its height approaches
β𝛽\beta as x↑∞↑𝑥x\uparrow\infty.
These behaviors define the role of each parameter in our
two parameter exponential function.

Consider the ratio of the slope of our two parameter exponential function
to its height:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​x​eβ−αβ​xeβ−αβ​x=β​eα−ββ​xeβ−αβ​x,𝑑𝑑𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛽subscriptsuperscript𝑒𝛽𝑥𝛼𝛽subscriptsuperscript𝑒𝛽𝑥𝛽𝛼\frac{\frac{d}{dx}e^{\beta x}\_{\beta-\alpha}}{e^{\beta x}\_{\beta-\alpha}}=\beta\frac{e^{\beta x}\_{\alpha-\beta}}{e^{\beta x}\_{\beta-\alpha}}, |  | (7) |

from ([3](#S2.E3 "In 2 Two Parameter Exponential Function")). Using ([6](#S2.E6 "In 2 Two Parameter Exponential Function")) on the RHS of ([7](#S2.E7 "In 2 Two Parameter Exponential Function")),
this ratio can also be represented as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​x​eβ−αβ​xeβ−αβ​x=β​(eβ−αβ​x)2+α2−β2β2eβ−αβ​x=β​1+α2−β2β2​(eβ−αβ​x)2.𝑑𝑑𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛽superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2superscript𝛼2superscript𝛽2superscript𝛽2subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛽1superscript𝛼2superscript𝛽2superscript𝛽2superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2\frac{\frac{d}{dx}e^{\beta x}\_{\beta-\alpha}}{e^{\beta x}\_{\beta-\alpha}}=\beta\frac{\sqrt{\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}+\frac{\alpha^{2}-\beta^{2}}{\beta^{2}}}}{e^{\beta x}\_{\beta-\alpha}}=\beta\sqrt{1+\frac{\alpha^{2}-\beta^{2}}{\beta^{2}\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}}}. |  | (8) |

Bringing β𝛽\beta under the square root:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​x​eβ−αβ​xeβ−αβ​x=α2​1(eβ−αβ​x)2+β2​[1−1(eβ−αβ​x)2].𝑑𝑑𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼subscriptsuperscript𝑒𝛽𝑥𝛽𝛼superscript𝛼21superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2superscript𝛽2delimited-[]11superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2\frac{\frac{d}{dx}e^{\beta x}\_{\beta-\alpha}}{e^{\beta x}\_{\beta-\alpha}}=\sqrt{\alpha^{2}\frac{1}{\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}}+\beta^{2}\left[1-\frac{1}{\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}}\right]}. |  | (9) |

Since 1/(eβ−αβ​x)2∈(0,1]1superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2011/\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}\in(0,1], the radicand is a convex combination
of α2superscript𝛼2\alpha^{2} and β2superscript𝛽2\beta^{2}.
At x=0𝑥0x=0, eβ−αβ​x=1subscriptsuperscript𝑒𝛽𝑥𝛽𝛼1e^{\beta x}\_{\beta-\alpha}=1, so
1(eβ−αβ​x)21superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2\frac{1}{\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}} also =1absent1=1 and the
ratio dd​x​eβ−αβ​xeβ−αβ​x=α𝑑𝑑𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛼\frac{\frac{d}{dx}e^{\beta x}\_{\beta-\alpha}}{e^{\beta x}\_{\beta-\alpha}}=\alpha.
As x↑∞↑𝑥x\uparrow\infty,
eβ−αβ​x↑∞↑subscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}\uparrow\infty, so
1(eβ−αβ​x)2↓0↓1superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼20\frac{1}{\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}}\downarrow 0
and the ratio
dd​x​eβ−αβ​xeβ−αβ​x𝑑𝑑𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼subscriptsuperscript𝑒𝛽𝑥𝛽𝛼\frac{\frac{d}{dx}e^{\beta x}\_{\beta-\alpha}}{e^{\beta x}\_{\beta-\alpha}}
converges to β𝛽\beta.

Like the one parameter exponential function,
our two parameter exponential function has an explicit inverse.
To derive it, let:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=eβ−αβ​x=β+α2​β​eβ​x+β−α2​β​e−β​x,x≥0,α≥0,β>0.formulae-sequence𝑦subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛽𝛼2𝛽superscript𝑒𝛽𝑥𝛽𝛼2𝛽superscript𝑒𝛽𝑥formulae-sequence𝑥0formulae-sequence𝛼0𝛽0y=e^{\beta x}\_{\beta-\alpha}=\frac{\beta+\alpha}{2\beta}e^{\beta x}+\frac{\beta-\alpha}{2\beta}e^{-\beta x},\qquad x\geq 0,\alpha\geq 0,\beta>0. |  | (10) |

We need to solve for x𝑥x as a function of y𝑦y.
Multiplying ([10](#S2.E10 "In 2 Two Parameter Exponential Function")) by β​eβ​x𝛽superscript𝑒𝛽𝑥\beta e^{\beta x} leads to a quadratic
function of eβ​xsuperscript𝑒𝛽𝑥e^{\beta x}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β+α2​e2​β​x−β​y​eβ​x+β−α2=0,x≥0,α≥0,β>0.formulae-sequence𝛽𝛼2superscript𝑒2𝛽𝑥𝛽𝑦superscript𝑒𝛽𝑥𝛽𝛼20formulae-sequence𝑥0formulae-sequence𝛼0𝛽0\frac{\beta+\alpha}{2}e^{2\beta x}-\beta ye^{\beta x}+\frac{\beta-\alpha}{2}=0,\qquad x\geq 0,\alpha\geq 0,\beta>0. |  | (11) |

By the quadratic root formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​x=β​y+β2​y2−(β2−α2)β+α,x≥0,α≥0,β>0,formulae-sequencesuperscript𝑒𝛽𝑥𝛽𝑦superscript𝛽2superscript𝑦2superscript𝛽2superscript𝛼2𝛽𝛼formulae-sequence𝑥0formulae-sequence𝛼0𝛽0e^{\beta x}=\frac{\beta y+\sqrt{\beta^{2}y^{2}-(\beta^{2}-\alpha^{2})}}{\beta+\alpha},\qquad x\geq 0,\alpha\geq 0,\beta>0, |  | (12) |

where we have chosen ++ in ±plus-or-minus\pm since eβ​x>0superscript𝑒𝛽𝑥0e^{\beta x}>0.
Solving for x𝑥x:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x=1β​ln⁡β​y+α2+β2​(y2−1)β+α,x≥0,α≥0,β>0.formulae-sequence𝑥1𝛽𝛽𝑦superscript𝛼2superscript𝛽2superscript𝑦21𝛽𝛼formulae-sequence𝑥0formulae-sequence𝛼0𝛽0x=\frac{1}{\beta}\ln\frac{\beta y+\sqrt{\alpha^{2}+\beta^{2}(y^{2}-1)}}{\beta+\alpha},\qquad x\geq 0,\alpha\geq 0,\beta>0. |  | (13) |

Hence, for y≥1𝑦1y\geq 1, the function on the RHS of
([13](#S2.E13 "In 2 Two Parameter Exponential Function")) is the explicit inverse of our two parameter exponential function.

Notice that from ([12](#S2.E12 "In 2 Two Parameter Exponential Function")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | β+α2​β​eβ​x=y2+y24−β2−α24​β2,𝛽𝛼2𝛽superscript𝑒𝛽𝑥𝑦2superscript𝑦24superscript𝛽2superscript𝛼24superscript𝛽2\frac{\beta+\alpha}{2\beta}e^{\beta x}=\frac{y}{2}+\sqrt{\frac{y^{2}}{4}-\frac{\beta^{2}-\alpha^{2}}{4\beta^{2}}}, |  | (14) |

where we observe from ([10](#S2.E10 "In 2 Two Parameter Exponential Function")) that β2−α24​β2superscript𝛽2superscript𝛼24superscript𝛽2\frac{\beta^{2}-\alpha^{2}}{4\beta^{2}} is
just the product of the
two terms which sum to y𝑦y.
Equation ([14](#S2.E14 "In 2 Two Parameter Exponential Function")) is an explicit formula that maps y𝑦y to the first term in the sum
([10](#S2.E10 "In 2 Two Parameter Exponential Function")) defining it.
When x=0𝑥0x=0 and α=0𝛼0\alpha=0, this first term has the same size
of 1212\frac{1}{2} as the second term, but otherwise, the first term is larger.
To obtain an
explicit formula that maps y𝑦y to the smaller term in the sum defining it,
notice that multiplying ([10](#S2.E10 "In 2 Two Parameter Exponential Function")) by β​e−β​x𝛽superscript𝑒𝛽𝑥\beta e^{-\beta x} leads to a quadratic
function of e−β​xsuperscript𝑒𝛽𝑥e^{-\beta x}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β−α2​e−2​β​x−β​y​eβ​x+β+α2=0.𝛽𝛼2superscript𝑒2𝛽𝑥𝛽𝑦superscript𝑒𝛽𝑥𝛽𝛼20\frac{\beta-\alpha}{2}e^{-2\beta x}-\beta ye^{\beta x}+\frac{\beta+\alpha}{2}=0. |  | (15) |

By the quadratic root formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−β​x=β​y−β2​y2−(β2−α2)β−α,superscript𝑒𝛽𝑥𝛽𝑦superscript𝛽2superscript𝑦2superscript𝛽2superscript𝛼2𝛽𝛼e^{-\beta x}=\frac{\beta y-\sqrt{\beta^{2}y^{2}-(\beta^{2}-\alpha^{2})}}{\beta-\alpha}, |  | (16) |

where now we have chosen −- in ±plus-or-minus\pm since e−β​x<1superscript𝑒𝛽𝑥1e^{-\beta x}<1.
Hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β−α2​β​e−β​x=y2−y24−β2−α24​β2.𝛽𝛼2𝛽superscript𝑒𝛽𝑥𝑦2superscript𝑦24superscript𝛽2superscript𝛼24superscript𝛽2\frac{\beta-\alpha}{2\beta}e^{-\beta x}=\frac{y}{2}-\sqrt{\frac{y^{2}}{4}-\frac{\beta^{2}-\alpha^{2}}{4\beta^{2}}}. |  | (17) |

This equation is an explicit formula that maps y𝑦y to the
last smaller term in the sum ([10](#S2.E10 "In 2 Two Parameter Exponential Function")) defining it.

For the one parameter exponential function y=eβ​x,x≥0,β>0formulae-sequence𝑦superscript𝑒𝛽𝑥formulae-sequence𝑥0𝛽0y=e^{\beta x},x\geq 0,\beta>0,
adding one to the input variable x𝑥x causes the output variable y𝑦y
to grow by the factor eβ>1superscript𝑒𝛽1e^{\beta}>1. We say the exponential function turns addition into multiplication.
For our two parameter exponential function defined by ([10](#S2.E10 "In 2 Two Parameter Exponential Function")),
adding one to the input variable x𝑥x causes the output variable y𝑦y
to grow as follows. First,
split y𝑦y into its larger term involving eβ​xsuperscript𝑒𝛽𝑥e^{\beta x}
given explicitly by ([14](#S2.E14 "In 2 Two Parameter Exponential Function"))
and its smaller term involving
e−β​xsuperscript𝑒𝛽𝑥e^{-\beta x},
given explicitly by ([17](#S2.E17 "In 2 Two Parameter Exponential Function")).
Next, grow the larger term by a factor
eβ>1superscript𝑒𝛽1e^{\beta}>1 and shrink the smaller term by
a factor e−β∈(0,1)superscript𝑒𝛽01e^{-\beta}\in(0,1).
Finally, add the two altered terms together
to obtain the new value of y𝑦y.
We say the two parameter exponential function turns addition into
a blend of multiplication and division.

## 3 Constructing a 3 Parameter Non-Negative Continuous Martingale

In this section, we use
the two parameter exponential function
constructed in the last section
to define a new three parameter non-negative continuous martingale
denoted by Ftsubscript𝐹𝑡F\_{t}.
Recall that
to create a driftless GBM Fbsuperscript𝐹𝑏F^{b} ,
one first creates an auxiliary positive continuous process
gt=eβ​Ztsubscript𝑔𝑡superscript𝑒𝛽subscript𝑍𝑡g\_{t}=e^{\beta Z\_{t}} with constant positive drift of β2/2superscript𝛽22\beta^{2}/2
and then one corrects for this constant drift by setting
FtbF0b=gt​e−β2​t/2subscriptsuperscript𝐹𝑏𝑡subscriptsuperscript𝐹𝑏0subscript𝑔𝑡superscript𝑒superscript𝛽2𝑡2\frac{F^{b}\_{t}}{F^{b}\_{0}}=g\_{t}e^{-\beta^{2}t/2}.
We will mimic this construction in the next subsection by
first constructing an auxiliary positive continuous process G𝐺G with
positive constant drift of β2/2superscript𝛽22\beta^{2}/2.
The following subsection then
corrects for this constant drift by
adding a jump to default process.

### 3.1 Constructing a Positive Continuous Process with Constant Drift

Let 00 be the valuation time and let Z𝑍Z be
a standard Brownian motion Z𝑍Z
under ℚℚ\mathbb{Q} whose value at t=0𝑡0t=0 is Z0=0subscript𝑍00Z\_{0}=0 as usual.
We allow
Z𝑍Z to exist prior to time 0.
Let t0≤0subscript𝑡00t\_{0}\leq 0 and we suppose that
Z𝑍Z exists for all t≥t0𝑡subscript𝑡0t\geq t\_{0}.
For t≥t0𝑡subscript𝑡0t\geq t\_{0},
let Z¯t≡s∈[t0,t]infZs\underline{Z}\_{t}\equiv\stackrel{{\scriptstyle\inf}}{{\scriptstyle s\in[t\_{0},t]}}Z\_{s} denote the running minimum of the standard Brownian motion Z𝑍Z under ℚℚ\mathbb{Q}.
Notice that Z𝑍Z’s path monitoring begins at time t0≤0subscript𝑡00t\_{0}\leq 0, so
Z¯0≤0subscript¯𝑍00\underline{Z}\_{0}\leq 0.
For t≥t0𝑡subscript𝑡0t\geq t\_{0},
let Zˇt≡Zt−Z¯tsubscriptˇ𝑍𝑡subscript𝑍𝑡subscript¯𝑍𝑡\check{Z}\_{t}\equiv Z\_{t}-\underline{Z}\_{t} denote Z𝑍Z’s running drawup process. Let:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gˇt=eβ−αβ​Zˇt,t≥t0,β>0,formulae-sequencesubscriptˇ𝐺𝑡subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼formulae-sequence𝑡subscript𝑡0𝛽0\check{G}\_{t}=e^{\beta\check{Z}\_{t}}\_{\beta-\alpha},\qquad t\geq t\_{0},\beta>0, |  | (18) |

be a new stochastic process with state space [1,∞)1[1,\infty).

Recall that setting α𝛼\alpha to zero reduces the two parameter exponential
eβ−αβ​x,x≥0,β>0formulae-sequence

subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝑥
0𝛽0e^{\beta x}\_{\beta-\alpha},x\geq 0,\beta>0
to the ordinary exponential eβ​x,x≥0,β>0formulae-sequence

superscript𝑒𝛽𝑥𝑥
0𝛽0e^{\beta x},x\geq 0,\beta>0.
The GBM eβ​Ztsuperscript𝑒𝛽subscript𝑍𝑡e^{\beta Z\_{t}} and the processes cosh⁡(β​Zt)𝛽subscript𝑍𝑡\cosh(\beta Z\_{t}), cosh⁡(β​|Zt|)𝛽subscript𝑍𝑡\cosh(\beta|Z\_{t}|),
and cosh⁡(β​Zˇt)𝛽subscriptˇ𝑍𝑡\cosh(\beta\check{Z}\_{t})
all grow in expectation at the rate β2/2superscript𝛽22\beta^{2}/2.
The hyperbolic cosine is a simple average of the increasing exponential
eβ​x,x≥0,β>0formulae-sequence

superscript𝑒𝛽𝑥𝑥
0𝛽0e^{\beta x},x\geq 0,\beta>0,
and its reciprocal.
When the asymmetry parameter α𝛼\alpha is made positive,
this simple average is replaced with an asymmetric average putting more weight on
the increasing exponential. The effect on the mean of this skewing is
the same as the effect on the mean of the GBM eβ​Ztsuperscript𝑒𝛽subscript𝑍𝑡e^{\beta Z\_{t}}
if Z𝑍Z behaved asymmetrically just when visiting its minimum Z¯¯𝑍\bar{Z}.
In particular, if Z𝑍Z is interpreted as a the limit of a scaled random walk,
then putting greater probability on rising above the minimum raises the mean
growth rate of eβ​Ztsuperscript𝑒𝛽subscript𝑍𝑡e^{\beta Z\_{t}} above β2/2superscript𝛽22\beta^{2}/2.
Let Z^^𝑍\hat{Z} denote this skewed Brownian motion.
The effect on the mean of
etβ​Z^subscriptsuperscript𝑒𝛽^𝑍𝑡e^{\beta\hat{Z}}\_{t} of
this rarely imposed asymmetry can be removed by multiplying
by eα​Z¯tsuperscript𝑒𝛼subscript¯𝑍𝑡e^{\alpha\bar{Z}\_{t}}.
We will similarly remove the effect on the mean of
Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t} of replacing
cosh⁡(β​Zˇt)𝛽subscriptˇ𝑍𝑡\cosh(\beta\check{Z}\_{t})
with
eβ−αβ​Zˇt,β>0,α≥0formulae-sequence

subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼𝛽
0𝛼0e^{\beta\check{Z}\_{t}}\_{\beta-\alpha},\beta>0,\alpha\geq 0
by multiplying Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t}
by eα​Z¯tsuperscript𝑒𝛼subscript¯𝑍𝑡e^{\alpha\bar{Z}\_{t}}.

We introduce a new parameter γ𝛾\gamma which will be used to
determine the value of
Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t} at t=0𝑡0t=0. We require that γ𝛾\gamma be between α𝛼\alpha and β𝛽\beta.
For technical reasons, we allow γ=α𝛾𝛼\gamma=\alpha, but we do not allow
γ=β𝛾𝛽\gamma=\beta. This allows us to set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gˇ0=α2−β2γ2−β2.subscriptˇ𝐺0superscript𝛼2superscript𝛽2superscript𝛾2superscript𝛽2\check{G}\_{0}=\sqrt{\frac{\alpha^{2}-\beta^{2}}{\gamma^{2}-\beta^{2}}}. |  | (19) |

The radicand is ≥1absent1\geq 1 and hence so is Gˇ0subscriptˇ𝐺0\check{G}\_{0}.
We next use ([13](#S2.E13 "In 2 Two Parameter Exponential Function")) to set Zˇ0subscriptˇ𝑍0\check{Z}\_{0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zˇ0=1β​ln⁡β​Gˇ0+α2+β2​[Gˇ02−1]β+α,x≥0,α≥0,β>0.formulae-sequencesubscriptˇ𝑍01𝛽𝛽subscriptˇ𝐺0superscript𝛼2superscript𝛽2delimited-[]superscriptsubscriptˇ𝐺021𝛽𝛼formulae-sequence𝑥0formulae-sequence𝛼0𝛽0\check{Z}\_{0}=\frac{1}{\beta}\ln\frac{\beta\check{G}\_{0}+\sqrt{\alpha^{2}+\beta^{2}[\check{G}\_{0}^{2}-1]}}{\beta+\alpha},\qquad x\geq 0,\alpha\geq 0,\beta>0. |  | (20) |

Since Gˇ0≥1subscriptˇ𝐺01\check{G}\_{0}\geq 1, Zˇ0≥0subscriptˇ𝑍00\check{Z}\_{0}\geq 0.
At each t≥0𝑡0t\geq 0, Gˇt≥1subscriptˇ𝐺𝑡1\check{G}\_{t}\geq 1 defined in ([18](#S3.E18 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
is increasing in its driver Zˇt≥0subscriptˇ𝑍𝑡0\check{Z}\_{t}\geq 0.
Equation ([21](#S3.E21 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that ([18](#S3.E18 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) can be explicitly inverted:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zˇt=1β​ln⁡(β​Gˇt+α2+β2​[Gˇt2−1]α+β),t≥t0,α≥0,β>0.formulae-sequencesubscriptˇ𝑍𝑡1𝛽𝛽subscriptˇ𝐺𝑡superscript𝛼2superscript𝛽2delimited-[]superscriptsubscriptˇ𝐺𝑡21𝛼𝛽formulae-sequence𝑡subscript𝑡0formulae-sequence𝛼0𝛽0\check{Z}\_{t}=\frac{1}{\beta}\ln\left(\frac{\beta\check{G}\_{t}+\sqrt{\alpha^{2}+\beta^{2}[\check{G}\_{t}^{2}-1]}}{\alpha+\beta}\right),\qquad t\geq t\_{0},\alpha\geq 0,\beta>0. |  | (21) |

We next set Z¯0=−Zˇ0subscript¯𝑍0subscriptˇ𝑍0\underline{Z}\_{0}=-\check{Z}\_{0} so that
Z0≡Z¯0+Zˇ0=0subscript𝑍0subscript¯𝑍0subscriptˇ𝑍00Z\_{0}\equiv\underline{Z}\_{0}+\check{Z}\_{0}=0.
With Z¯0subscript¯𝑍0\underline{Z}\_{0} determined at some non-positive value, let:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G¯t=eα​Z¯tt≥t0,α≥0,formulae-sequencesubscript¯𝐺𝑡superscript𝑒𝛼subscript¯𝑍𝑡formulae-sequence𝑡subscript𝑡0𝛼0\underline{G}\_{t}=e^{\alpha\underline{Z}\_{t}}\qquad t\geq t\_{0},\alpha\geq 0, |  | (22) |

be a super-martingale with state space (0,1]01(0,1].
The process G¯t∈(0,1]subscript¯𝐺𝑡01\underline{G}\_{t}\in(0,1] defined in ([22](#S3.E22 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
is increasing in its driver Z¯t≤0subscript¯𝑍𝑡0\underline{Z}\_{t}\leq 0,
For α>0𝛼0\alpha>0, ([26](#S3.E26 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) can be explicitly inverted:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z¯t=1α​ln⁡G¯t,t≥t0.formulae-sequencesubscript¯𝑍𝑡1𝛼subscript¯𝐺𝑡𝑡subscript𝑡0\underline{Z}\_{t}=\frac{1}{\alpha}\ln\underline{G}\_{t},\qquad t\geq t\_{0}. |  | (23) |

For α≥0,β>0formulae-sequence𝛼0𝛽0\alpha\geq 0,\beta>0 and γ𝛾\gamma between them, let:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=G¯t​Gˇt,t≥0,formulae-sequencesubscript𝐺𝑡subscript¯𝐺𝑡subscriptˇ𝐺𝑡𝑡0G\_{t}=\underline{G}\_{t}\check{G}\_{t},\qquad t\geq 0, |  | (24) |

be our auxiliary continuous process with state space (0,∞)0(0,\infty).
We claim that G¯t=s∈[t0,t]infGs\underline{G}\_{t}=\stackrel{{\scriptstyle\inf}}{{\scriptstyle s\in[t\_{0},t]}}G\_{s}.
In words, we claim that the super-martingale G¯t∈(0,1]subscript¯𝐺𝑡01\underline{G}\_{t}\in(0,1] defined in ([22](#S3.E22 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
is just the running minimum of the G𝐺G process defined in ([24](#S3.E24 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")).
To see why, note that substituting ([18](#S3.E18 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) and ([22](#S3.E22 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) in ([24](#S3.E24 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
implies that for α≥0,β>0formulae-sequence𝛼0𝛽0\alpha\geq 0,\beta>0 and γ𝛾\gamma between them:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=eα​Z¯t​eβ−αβ​Zˇt,t≥t0.formulae-sequencesubscript𝐺𝑡superscript𝑒𝛼subscript¯𝑍𝑡subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼𝑡subscript𝑡0G\_{t}=e^{\alpha\underline{Z}\_{t}}e^{\beta\check{Z}\_{t}}\_{\beta-\alpha},\qquad t\geq t\_{0}. |  | (25) |

Since Z¯¯𝑍\underline{Z} only declines when Zˇ=0ˇ𝑍0\check{Z}=0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s∈[t0,t]infGs=eα​Z¯t,t≥t0,α≥0,β>0,formulae-sequencesuperscript𝑠subscript𝑡0𝑡infimumabsentsubscript𝐺𝑠superscript𝑒𝛼subscript¯𝑍𝑡formulae-sequence𝑡subscript𝑡0formulae-sequence𝛼0𝛽0\stackrel{{\scriptstyle\inf}}{{\scriptstyle s\in[t\_{0},t]}}G\_{s}=e^{\alpha\underline{Z}\_{t}},\qquad t\geq t\_{0},\alpha\geq 0,\beta>0, |  | (26) |

which matches the defining equation ([22](#S3.E22 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) for G¯tsubscript¯𝐺𝑡\underline{G}\_{t}.
Hence G¯tsubscript¯𝐺𝑡\underline{G}\_{t} is the running minimum of the G𝐺G process
defined in ([24](#S3.E24 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")).
Since G¯tsubscript¯𝐺𝑡\underline{G}\_{t} has state space (0,1]01(0,1], G𝐺G is positive forever.
From ([24](#S3.E24 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gˇt=GtG¯t,t≥0,formulae-sequencesubscriptˇ𝐺𝑡subscript𝐺𝑡subscript¯𝐺𝑡𝑡0\check{G}\_{t}=\frac{G\_{t}}{\underline{G}\_{t}},\qquad t\geq 0, |  | (27) |

so Gˇˇ𝐺\check{G} is the relative drawup process of G𝐺G.

Applying Itô’s formula to ([18](#S3.E18 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")), ([3](#S2.E3 "In 2 Two Parameter Exponential Function")) implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Gˇt=β​eα−ββ​Zˇt​d​Zˇt+β22​eβ−αβ​Zˇt​d​⟨Zˇ⟩t,t≥t0.formulae-sequence𝑑subscriptˇ𝐺𝑡𝛽subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛼𝛽𝑑subscriptˇ𝑍𝑡superscript𝛽22subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼𝑑subscriptdelimited-⟨⟩ˇ𝑍𝑡𝑡subscript𝑡0d\check{G}\_{t}=\beta e^{\beta\check{Z}\_{t}}\_{\alpha-\beta}d\check{Z}\_{t}+\frac{\beta^{2}}{2}e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}d\langle\check{Z}\rangle\_{t},\qquad t\geq t\_{0}. |  | (28) |

Thus the increments of Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t} depend on the increments of
Zˇtsubscriptˇ𝑍𝑡\check{Z}\_{t} and the squared increments of Zˇtsubscriptˇ𝑍𝑡\check{Z}\_{t}.
Since Z¯¯𝑍\underline{Z} is a process of bounded variation, it has zero quadratic variation and hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Zˇ⟩t=⟨Z−Z¯⟩t=⟨Z⟩t=t,t≥t0.formulae-sequencesubscriptdelimited-⟨⟩ˇ𝑍𝑡subscriptdelimited-⟨⟩𝑍¯𝑍𝑡subscriptdelimited-⟨⟩𝑍𝑡𝑡𝑡subscript𝑡0\langle\check{Z}\rangle\_{t}=\langle Z-\underline{Z}\rangle\_{t}=\langle Z\rangle\_{t}=t,\qquad t\geq t\_{0}. |  | (29) |

Substituting ([6](#S2.E6 "In 2 Two Parameter Exponential Function")) and ([29](#S3.E29 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) in ([28](#S3.E28 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies
that the coefficients just depend on
eβ−αβ​Zˇtsubscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Gˇt=β22​eβ−αβ​Zˇt​d​t+β​(eβ−αβ​Zˇt)2+α2−β2β2​d​Zˇt,t≥t0.formulae-sequence𝑑subscriptˇ𝐺𝑡superscript𝛽22subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼𝑑𝑡𝛽superscriptsubscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼2superscript𝛼2superscript𝛽2superscript𝛽2𝑑subscriptˇ𝑍𝑡𝑡subscript𝑡0d\check{G}\_{t}=\frac{\beta^{2}}{2}e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}dt+\beta\sqrt{\left(e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}\right)^{2}+\frac{\alpha^{2}-\beta^{2}}{\beta^{2}}}d\check{Z}\_{t},\qquad t\geq t\_{0}. |  | (30) |

Substituting ([18](#S3.E18 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) in ([30](#S3.E30 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies
that Gˇˇ𝐺\check{G} solves
the following
stochastic differential equation
(SDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Gˇt=β22​Gˇt​d​t+α2+β2​[(Gˇt)2−1]​d​Zˇt,t≥t0.formulae-sequence𝑑subscriptˇ𝐺𝑡superscript𝛽22subscriptˇ𝐺𝑡𝑑𝑡superscript𝛼2superscript𝛽2delimited-[]superscriptsubscriptˇ𝐺𝑡21𝑑subscriptˇ𝑍𝑡𝑡subscript𝑡0d\check{G}\_{t}=\frac{\beta^{2}}{2}\check{G}\_{t}dt+\sqrt{\alpha^{2}+\beta^{2}\left[\left(\check{G}\_{t}\right)^{2}-1\right]}d\check{Z}\_{t},\qquad t\geq t\_{0}. |  | (31) |

This SDE is univariate since the
coefficients for Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t} just depend on Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t}.
Dividing by Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t} implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​GˇtGˇt=β22​d​t+α2​1Gˇt2+β2​[1−1Gˇt2]​d​Zˇt,t≥t0.formulae-sequence𝑑subscriptˇ𝐺𝑡subscriptˇ𝐺𝑡superscript𝛽22𝑑𝑡superscript𝛼21subscriptsuperscriptˇ𝐺2𝑡superscript𝛽2delimited-[]11subscriptsuperscriptˇ𝐺2𝑡𝑑subscriptˇ𝑍𝑡𝑡subscript𝑡0\frac{d\check{G}\_{t}}{\check{G}\_{t}}=\frac{\beta^{2}}{2}dt+\sqrt{\alpha^{2}\frac{1}{\check{G}^{2}\_{t}}+\beta^{2}\left[1-\frac{1}{\check{G}^{2}\_{t}}\right]}d\check{Z}\_{t},\qquad t\geq t\_{0}. |  | (32) |

Hence, Gˇˇ𝐺\check{G} solves the above simple SDE when the two drivers
are t𝑡t and Zˇˇ𝑍\check{Z}. To determine the coefficients of Ztsubscript𝑍𝑡Z\_{t} and Z¯¯𝑍\underline{Z}, note that
substituting d​Zˇt=d​Zt−d​Z¯t𝑑subscriptˇ𝑍𝑡𝑑subscript𝑍𝑡𝑑subscript¯𝑍𝑡d\check{Z}\_{t}=dZ\_{t}-d\underline{Z}\_{t} in ([32](#S3.E32 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​GˇtGˇt=β22​d​t+α2​(1Gˇt)2+β2​[1−1Gˇt2]​(d​Zt−d​Z¯t),t≥t0.formulae-sequence𝑑subscriptˇ𝐺𝑡subscriptˇ𝐺𝑡superscript𝛽22𝑑𝑡superscript𝛼2superscript1subscriptˇ𝐺𝑡2superscript𝛽2delimited-[]11subscriptsuperscriptˇ𝐺2𝑡𝑑subscript𝑍𝑡𝑑subscript¯𝑍𝑡𝑡subscript𝑡0\frac{d\check{G}\_{t}}{\check{G}\_{t}}=\frac{\beta^{2}}{2}dt+\sqrt{\alpha^{2}\left(\frac{1}{\check{G}\_{t}}\right)^{2}+\beta^{2}\left[1-\frac{1}{\check{G}^{2}\_{t}}\right]}\left(dZ\_{t}-d\underline{Z}\_{t}\right),\qquad t\geq t\_{0}. |  | (33) |

Since Z¯¯𝑍\underline{Z} only decreases when Gˇ=1ˇ𝐺1\check{G}=1, the
net coefficient of d​Z¯𝑑¯𝑍d\underline{Z} in ([33](#S3.E33 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) is zero.
As a result,
Gˇˇ𝐺\check{G} also solves the following
SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​GˇtGˇt=−α​d​Z¯t+β22​d​t+α2​1Gˇt2+β2​[1−1Gˇt2]​d​Zt,t≥t0.formulae-sequence𝑑subscriptˇ𝐺𝑡subscriptˇ𝐺𝑡𝛼𝑑subscript¯𝑍𝑡superscript𝛽22𝑑𝑡superscript𝛼21subscriptsuperscriptˇ𝐺2𝑡superscript𝛽2delimited-[]11subscriptsuperscriptˇ𝐺2𝑡𝑑subscript𝑍𝑡𝑡subscript𝑡0\frac{d\check{G}\_{t}}{\check{G}\_{t}}=-\alpha d\underline{Z}\_{t}+\frac{\beta^{2}}{2}dt+\sqrt{\alpha^{2}\frac{1}{\check{G}^{2}\_{t}}+\beta^{2}\left[1-\frac{1}{\check{G}^{2}\_{t}}\right]}dZ\_{t},\qquad t\geq t\_{0}. |  | (34) |

The coefficient of d​Zt𝑑subscript𝑍𝑡dZ\_{t} in
([34](#S3.E34 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) is the instantaneous lognormal volatility of Gˇˇ𝐺\check{G},
which is a randomly weighted L2superscript𝐿2L^{2} mean of α𝛼\alpha and β𝛽\beta.
This form is clearly just a consequence of ([9](#S2.E9 "In 2 Two Parameter Exponential Function")).
Since (1Gˇt)2∈(0,1]superscript1subscriptˇ𝐺𝑡201\left(\frac{1}{\check{G}\_{t}}\right)^{2}\in(0,1], the
instantaneous lognormal variance rate of
Gˇtsubscriptˇ𝐺𝑡\check{G}\_{t} is just a convex combination of
α2superscript𝛼2\alpha^{2} and β2superscript𝛽2\beta^{2}.
When Z𝑍Z is at its minimum Z¯¯𝑍\underline{Z},
Zˇ=0ˇ𝑍0\check{Z}=0,
and hence Gˇ=1ˇ𝐺1\check{G}=1.
At such times, ([34](#S3.E34 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that the
instantaneous volatility of Gˇˇ𝐺\check{G} is α𝛼\alpha.
In contrast, as the difference between Z𝑍Z
and its minimum Z¯¯𝑍\underline{Z} approaches infinity,
Gˇˇ𝐺\check{G} also approaches infinity, and ([34](#S3.E34 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that
the instantaneous volatility of Gˇˇ𝐺\check{G} approaches β𝛽\beta.
These results clearly follow from the
behavior of our two parameter exponential function
eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}
at x=0𝑥0x=0 and at x=∞𝑥x=\infty.

The dynamics in ([34](#S3.E34 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) clearly depend on our
first two parameters
α𝛼\alpha and β𝛽\beta, which are
the respective instantaneous volatilities of
Gˇˇ𝐺\check{G} at Gˇˇ𝐺\check{G}’s extremes of one and infinity.
To interpret our third parameter γ𝛾\gamma, note that
squaring both sides of ([19](#S3.E19 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gˇ02=α2−β2γ2−β2.superscriptsubscriptˇ𝐺02superscript𝛼2superscript𝛽2superscript𝛾2superscript𝛽2\check{G}\_{0}^{2}=\frac{\alpha^{2}-\beta^{2}}{\gamma^{2}-\beta^{2}}. |  | (35) |

Cross multiplying and re-arranging:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ2​Gˇ02=α2−β2+β2​(Gˇ0)2.superscript𝛾2superscriptsubscriptˇ𝐺02superscript𝛼2superscript𝛽2superscript𝛽2superscriptsubscriptˇ𝐺02\gamma^{2}\check{G}\_{0}^{2}=\alpha^{2}-\beta^{2}+\beta^{2}(\check{G}\_{0})^{2}. |  | (36) |

Dividing by Gˇ02superscriptsubscriptˇ𝐺02\check{G}\_{0}^{2} and taking the square root implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=α2​1Gˇ02+β2​[1−1Gˇ02].𝛾superscript𝛼21subscriptsuperscriptˇ𝐺20superscript𝛽2delimited-[]11subscriptsuperscriptˇ𝐺20\gamma=\sqrt{\alpha^{2}\frac{1}{\check{G}^{2}\_{0}}+\beta^{2}\left[1-\frac{1}{\check{G}^{2}\_{0}}\right]}. |  | (37) |

Comparing ([37](#S3.E37 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) to the volatility in ([34](#S3.E34 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) evaluated at t=0𝑡0t=0 implies that
our third parameter γ𝛾\gamma is just the initial volatility of Gˇˇ𝐺\check{G}.

We next determine the dynamics of the G𝐺G process, which
([24](#S3.E24 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) defined as the product:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=G¯t​Gˇtt≥t0,formulae-sequencesubscript𝐺𝑡subscript¯𝐺𝑡subscriptˇ𝐺𝑡𝑡subscript𝑡0G\_{t}=\underline{G}\_{t}\check{G}\_{t}\qquad t\geq t\_{0}, |  | (38) |

for α≥0,β>0formulae-sequence𝛼0𝛽0\alpha\geq 0,\beta>0 and γ𝛾\gamma between them.
Itô’s formula implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​GtGt=d​G¯tG¯t+d​GˇtGˇt=α​d​Z¯t+d​GˇtGˇt,t≥t0,formulae-sequence𝑑subscript𝐺𝑡subscript𝐺𝑡𝑑subscript¯𝐺𝑡subscript¯𝐺𝑡𝑑subscriptˇ𝐺𝑡subscriptˇ𝐺𝑡𝛼𝑑subscript¯𝑍𝑡𝑑subscriptˇ𝐺𝑡subscriptˇ𝐺𝑡𝑡subscript𝑡0\frac{dG\_{t}}{G\_{t}}=\frac{d\underline{G}\_{t}}{\underline{G}\_{t}}+\frac{d\check{G}\_{t}}{\check{G}\_{t}}=\alpha d\underline{Z}\_{t}+\frac{d\check{G}\_{t}}{\check{G}\_{t}},\qquad t\geq t\_{0}, |  | (39) |

since G¯t=eα​Z¯tsubscript¯𝐺𝑡superscript𝑒𝛼subscript¯𝑍𝑡\underline{G}\_{t}=e^{\alpha\underline{Z}\_{t}}.
Substituting in ([32](#S3.E32 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that
G𝐺G solves the following
SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​GtGt=β22​d​t+α2​(G¯tGt)2+β2​[1−(G¯tGt)2]​d​Zt,t≥t0,formulae-sequence𝑑subscript𝐺𝑡subscript𝐺𝑡superscript𝛽22𝑑𝑡superscript𝛼2superscriptsubscript¯𝐺𝑡subscript𝐺𝑡2superscript𝛽2delimited-[]1superscriptsubscript¯𝐺𝑡subscript𝐺𝑡2𝑑subscript𝑍𝑡𝑡subscript𝑡0\frac{dG\_{t}}{G\_{t}}=\frac{\beta^{2}}{2}dt+\sqrt{\alpha^{2}\left(\frac{\underline{G}\_{t}}{G\_{t}}\right)^{2}+\beta^{2}\left[1-\left(\frac{\underline{G}\_{t}}{G\_{t}}\right)^{2}\right]}dZ\_{t},\qquad t\geq t\_{0}, |  | (40) |

since 1Gˇt=G¯tGt1subscriptˇ𝐺𝑡subscript¯𝐺𝑡subscript𝐺𝑡\frac{1}{\check{G}\_{t}}=\frac{\underline{G}\_{t}}{G\_{t}}.

Like the Gˇˇ𝐺\check{G} process,
the G𝐺G process has constant proportional drift at rate
β22superscript𝛽22\frac{\beta^{2}}{2}.
Unlike the SDE ([34](#S3.E34 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) for Gˇˇ𝐺\check{G}, the SDE
([40](#S3.E40 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) for
G𝐺G has coefficients that depend on the auxiliary process
G¯¯𝐺\underline{G}.
Since (G¯tGt)2∈(0,1]superscriptsubscript¯𝐺𝑡subscript𝐺𝑡201\left(\frac{\underline{G}\_{t}}{G\_{t}}\right)^{2}\in(0,1],
the lognormal variance rate of G𝐺G
is also a convex combination of α2superscript𝛼2\alpha^{2} and β2superscript𝛽2\beta^{2}.
When Gt=G¯tsubscript𝐺𝑡subscript¯𝐺𝑡G\_{t}=\underline{G}\_{t}, the
G𝐺G process behaves locally like a
GBM with constant proportional drift rate
β22superscript𝛽22\frac{\beta^{2}}{2}
and constant proportional variance rate α2superscript𝛼2\alpha^{2}.
As G𝐺G rises above G¯tsubscript¯𝐺𝑡\underline{G}\_{t},
the lognormal variance rate moves towards
β2superscript𝛽2\beta^{2} and asymptotes to this value in the limit as
G↑∞↑𝐺G\uparrow\infty.

Substituting 1Gˇ0=G¯0G01subscriptˇ𝐺0subscript¯𝐺0subscript𝐺0\frac{1}{\check{G}\_{0}}=\frac{\underline{G}\_{0}}{G\_{0}}
in ([37](#S3.E37 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=α2​(G¯0G0)2+β2​[1−(G¯0G0)2].𝛾superscript𝛼2superscriptsubscript¯𝐺0subscript𝐺02superscript𝛽2delimited-[]1superscriptsubscript¯𝐺0subscript𝐺02\gamma=\sqrt{\alpha^{2}\left(\frac{\underline{G}\_{0}}{G\_{0}}\right)^{2}+\beta^{2}\left[1-\left(\frac{\underline{G}\_{0}}{G\_{0}}\right)^{2}\right]}. |  | (41) |

Evaluating the coefficient of d​Zt𝑑subscript𝑍𝑡dZ\_{t} in ([40](#S3.E40 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
at t=0𝑡0t=0, ([41](#S3.E41 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that
the instantaneous lognormal volatility of G𝐺G is γ𝛾\gamma.
Hence, the three parameters
α,γ

𝛼𝛾\alpha,\gamma, and β𝛽\beta
can be respectively interpreted as the instantaneous
lognormal volatility of G𝐺G at each new low,
at the initial time, and at infinitely high values of G𝐺G.

The bivariate transition PDF of the pair (Z¯,Zˇ)¯𝑍ˇ𝑍(\underline{Z},\check{Z}) is known in
closed form and is given in [[2](#bib.bib2)].
Since G¯¯𝐺\underline{G} and Gˇˇ𝐺\check{G} are each just univariate, increasing,
explicitly invertible transformations of
Z¯¯𝑍\underline{Z} and Zˇˇ𝑍\check{Z} respectively,
it follows that
the bivariate transition PDF of the pair (G¯,Gˇ)¯𝐺ˇ𝐺(\underline{G},\check{G})
can easily be obtained in closed form.

Recall from ([25](#S3.E25 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=eα​Z¯t​eβ−αβ​Zˇt,t≥t0.formulae-sequencesubscript𝐺𝑡superscript𝑒𝛼subscript¯𝑍𝑡subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼𝑡subscript𝑡0G\_{t}=e^{\alpha\underline{Z}\_{t}}e^{\beta\check{Z}\_{t}}\_{\beta-\alpha},\qquad t\geq t\_{0}. |  | (42) |

As β↓0↓𝛽0\beta\downarrow 0, the
G𝐺G process becomes driftless and
two parameter exponential
function eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha} in ([42](#S3.E42 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
converges to the linear function
1+α​x1𝛼𝑥1+\alpha x.
As a result, the process G𝐺G converges to the martingale
F𝐹F in [[2](#bib.bib2)] in this limit when F0=1subscript𝐹01F\_{0}=1.
Setting α=β𝛼𝛽\alpha=\beta in ([42](#S3.E42 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")), the two parameter
exponential reduces to the one parameter exponential
and hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=eβ​Z¯t​eβ​Zˇt=eβ​(Z¯t+Zˇt)=eβ​Zt,t≥t0.formulae-sequencesubscript𝐺𝑡superscript𝑒𝛽subscript¯𝑍𝑡superscript𝑒𝛽subscriptˇ𝑍𝑡superscript𝑒𝛽subscript¯𝑍𝑡subscriptˇ𝑍𝑡superscript𝑒𝛽subscript𝑍𝑡𝑡subscript𝑡0G\_{t}=e^{\beta\underline{Z}\_{t}}e^{\beta\check{Z}\_{t}}=e^{\beta(\underline{Z}\_{t}+\check{Z}\_{t})}=e^{\beta Z\_{t}},\qquad t\geq t\_{0}. |  | (43) |

Thus, the G𝐺G process generalizes the exponential of
standard Brownian motion, by adding parameters α𝛼\alpha and
γ𝛾\gamma.

Being a sub-martingale, the G𝐺G process can be used directly to model spot price (e.g. spot FX rates) and price derivatives written on G𝐺G in risk neutral measure. For this purpose, we introduce a new sub-martingale process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=F0​Gt,t≥t0,formulae-sequencesubscript𝐹𝑡subscript𝐹0subscript𝐺𝑡𝑡subscript𝑡0\displaystyle F\_{t}=F\_{0}G\_{t},\quad t\geq t\_{0}, |  | (44) |

where F0>0subscript𝐹00F\_{0}>0 is the initial value of the process. Like G𝐺G, F𝐹F is positive and has a positive drift. Note that the positivity of the drift of G𝐺G is not a binding restriction due to the international put-call equivalence [[6](#bib.bib6)]. For instance, if a positive process Stsubscript𝑆𝑡S\_{t} has a negative drift, one can use it to model the inverse of a process that has a positive drift via Ft=1Stsubscript𝐹𝑡1subscript𝑆𝑡F\_{t}=\frac{1}{S\_{t}}. For derivatives on future price, the underlying security is required to be driven by a martingale in the risk neutral measure for derivative pricing. In the next subsection we introduce a new martingale process from G𝐺G by adding a jump to default process which has a negative drift. However, one should interpret the sub-martingale Eqn ([44](#S3.E44 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) and the new martingale as dynamics of two different securities, instead of spot and future prices of one security.

### 3.2 Constructing a Non-Negative Martingale via Jump to Default

For α≥0,β>0formulae-sequence𝛼0𝛽0\alpha\geq 0,\beta>0, and for γ𝛾\gamma between them,
the G𝐺G process constructed in the last subsection
starts at one and has constant positive drift β22superscript𝛽22\frac{\beta^{2}}{2}.
In this section, we change the starting point to F0>0subscript𝐹00F\_{0}>0 and interpret this
positive drift as compensation for a possible jump to zero.
This allows us to
construct a tractable non-negative martingale
F𝐹F which starts at F0subscript𝐹0F\_{0}. Let Ntsubscript𝑁𝑡N\_{t} be a standard Poisson process with
arrival rate β22superscript𝛽22\frac{\beta^{2}}{2} under ℚℚ\mathbb{Q}.
For F0>0subscript𝐹00F\_{0}>0, let:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=F0​Gt​𝟙Nt=0,t≥t0.formulae-sequencesubscript𝐹𝑡subscript𝐹0subscript𝐺𝑡subscript1subscript𝑁𝑡0𝑡subscript𝑡0F\_{t}=F\_{0}G\_{t}\mathbbm{1}\_{N\_{t}=0},\qquad t\geq t\_{0}. |  | (45) |

be a non-negative process started at F0>0subscript𝐹00F\_{0}>0.
Then F𝐹F is a ℚℚ\mathbb{Q} martingale which drifts up at
the constant rate
β22superscript𝛽22\frac{\beta^{2}}{2} in order to compensate for
a possible jump to zero. Once F𝐹F hits zero, it is absorbed there.
Let:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F¯t=s∈[t0,t]infFs,t≥t0\underline{F}\_{t}=\stackrel{{\scriptstyle\inf}}{{\scriptstyle s\in[t\_{0},t]}}F\_{s},\qquad t\geq t\_{0} |  | (46) |

be the running minimum of F𝐹F. Let τ𝜏\tau be the exponentially distributed
random time at which F𝐹F jumps to zero.
For t∈[t0,τ)𝑡subscript𝑡0𝜏t\in[t\_{0},\tau), ([45](#S3.E45 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F¯t=F0​G¯t.subscript¯𝐹𝑡subscript𝐹0subscript¯𝐺𝑡\underline{F}\_{t}=F\_{0}\underline{G}\_{t}. |  | (47) |

Dividing ([47](#S3.E47 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) by ([46](#S3.E46 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) implies that for t∈[t0,τ)𝑡subscript𝑡0𝜏t\in[t\_{0},\tau):

|  |  |  |  |
| --- | --- | --- | --- |
|  | F¯tFt=G¯tGt.subscript¯𝐹𝑡subscript𝐹𝑡subscript¯𝐺𝑡subscript𝐺𝑡\frac{\underline{F}\_{t}}{F\_{t}}=\frac{\underline{G}\_{t}}{G\_{t}}. |  | (48) |

As a result, the SDE for F𝐹F is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ft=Ft−​[α2​(F¯t−Ft−)2+β2​[1−(F¯t−Ft−)2]​d​Zt−(d​Nt−β22​d​t)],t≥t0.formulae-sequence𝑑subscript𝐹𝑡subscript𝐹limit-from𝑡delimited-[]superscript𝛼2superscriptsubscript¯𝐹limit-from𝑡subscript𝐹limit-from𝑡2superscript𝛽2delimited-[]1superscriptsubscript¯𝐹limit-from𝑡subscript𝐹limit-from𝑡2𝑑subscript𝑍𝑡𝑑subscript𝑁𝑡superscript𝛽22𝑑𝑡𝑡subscript𝑡0dF\_{t}=F\_{t-}\left[\sqrt{\alpha^{2}\left(\frac{\underline{F}\_{t-}}{F\_{t-}}\right)^{2}+\beta^{2}\left[1-\left(\frac{\underline{F}\_{t-}}{F\_{t-}}\right)^{2}\right]}dZ\_{t}-\left(dN\_{t}-\frac{\beta^{2}}{2}dt\right)\right],\qquad t\geq t\_{0}. |  | (49) |

Substituting ([24](#S3.E24 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) in ([45](#S3.E45 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
implies that Ftsubscript𝐹𝑡F\_{t} can be related to the
contemporaneous values of the pair
(Z¯,Zˇ)¯𝑍ˇ𝑍(\underline{Z},\check{Z}) and Ntsubscript𝑁𝑡N\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=F0​eα​Z¯t​eβ−αβ​Zˇt​𝟙Nt=0,t≥t0.formulae-sequencesubscript𝐹𝑡subscript𝐹0superscript𝑒𝛼subscript¯𝑍𝑡subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼subscript1subscript𝑁𝑡0𝑡subscript𝑡0F\_{t}=F\_{0}e^{\alpha\underline{Z}\_{t}}e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}\mathbbm{1}\_{N\_{t}=0},\qquad t\geq t\_{0}. |  | (50) |

The price relative FtF0subscript𝐹𝑡subscript𝐹0\frac{F\_{t}}{F\_{0}} is a non-negative
martingale started at one. From ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")), this price relative
decomposes into the product of a positive strict supermartingale started at one,
eα​Z¯t​𝟙Nt=0superscript𝑒𝛼subscript¯𝑍𝑡subscript1subscript𝑁𝑡0e^{\alpha\underline{Z}\_{t}}\mathbbm{1}\_{N\_{t}=0} and a
positive strict submartingale started at one, namely
Gˇt=eβ−αβ​Zˇtsubscriptˇ𝐺𝑡subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼\check{G}\_{t}=e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}.

If α=β𝛼𝛽\alpha=\beta, then the two parameter
exponential function
eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}
in ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale"))
reduces to the one parameter exponential function
eβ​xsuperscript𝑒𝛽𝑥e^{\beta x},
and hence ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) simplifies to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=F0​eβ​Z¯t​eβ​Zˇt​𝟙Nt=0=F0​eβ​(Z¯t+Zˇt)​𝟙Nt=0=eβ​Zt​𝟙Nt=0,t≥t0,formulae-sequencesubscript𝐹𝑡subscript𝐹0superscript𝑒𝛽subscript¯𝑍𝑡superscript𝑒𝛽subscriptˇ𝑍𝑡subscript1subscript𝑁𝑡0subscript𝐹0superscript𝑒𝛽subscript¯𝑍𝑡subscriptˇ𝑍𝑡subscript1subscript𝑁𝑡0superscript𝑒𝛽subscript𝑍𝑡subscript1subscript𝑁𝑡0𝑡subscript𝑡0F\_{t}=F\_{0}e^{\beta\underline{Z}\_{t}}e^{\beta\check{Z}\_{t}}\mathbbm{1}\_{N\_{t}=0}=F\_{0}e^{\beta(\underline{Z}\_{t}+\check{Z}\_{t})}\mathbbm{1}\_{N\_{t}=0}=e^{\beta Z\_{t}}\mathbbm{1}\_{N\_{t}=0},\qquad t\geq t\_{0}, |  | (51) |

which is GBM with jump to default.
When β→0→𝛽0\beta\rightarrow 0, then ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) asymptotes to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft→F0​eα​Z¯t​(1+α​Zˇt),t≥t0,formulae-sequence→subscript𝐹𝑡subscript𝐹0superscript𝑒𝛼subscript¯𝑍𝑡1𝛼subscriptˇ𝑍𝑡𝑡subscript𝑡0F\_{t}\rightarrow F\_{0}e^{\alpha\underline{Z}\_{t}}(1+\alpha\check{Z}\_{t}),\qquad t\geq t\_{0}, |  | (52) |

which is a two parameter positive continuous martingale.
Setting γ=α𝛾𝛼\gamma=\alpha further reduces
F𝐹F to the one parameter
positive continuous martingale in [[2](#bib.bib2)].

From [[2](#bib.bib2)], the bivariate transition PDF of
the Brownian Minimum and Brownian Drawup:

|  |  |  |
| --- | --- | --- |
|  | ℚt​{Z¯T∈d​j,ZˇT∈d​kˇ;Z¯t=Z¯,Zˇt=Zˇ}=b​(j,kˇ;w,T−t)​d​j​d​kˇsubscriptℚ𝑡formulae-sequencesubscript¯𝑍𝑇𝑑𝑗formulae-sequencesubscriptˇ𝑍𝑇𝑑ˇ𝑘formulae-sequencesubscript¯𝑍𝑡¯𝑍subscriptˇ𝑍𝑡ˇ𝑍𝑏𝑗ˇ𝑘𝑤𝑇𝑡𝑑𝑗𝑑ˇ𝑘\displaystyle\mathbb{Q}\_{t}\{\underline{Z}\_{T}\in dj,\check{Z}\_{T}\in d\check{k};\underline{Z}\_{t}=\underline{Z},\check{Z}\_{t}=\check{Z}\}=b(j,\check{k};w,T-t)djd\check{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(j,kˇ;w,T−t)≡2π​(T−t)3​(kˇ−j+w)​e−(kˇ−j+w)22​(T−t),j<w¯,kˇ≥0,formulae-sequence𝑏𝑗ˇ𝑘𝑤𝑇𝑡2𝜋superscript𝑇𝑡3ˇ𝑘𝑗𝑤superscript𝑒superscriptˇ𝑘𝑗𝑤22𝑇𝑡formulae-sequence𝑗¯𝑤ˇ𝑘0\displaystyle b(j,\check{k};w,T-t)\equiv\sqrt{\frac{2}{\pi(T-t)^{3}}}(\check{k}-j+w)e^{-\frac{(\check{k}-j+w)^{2}}{2(T-t)}},\qquad j<\underline{w},\quad\check{k}\geq 0, |  | (53) |

where w=Z¯+Zˇ𝑤¯𝑍ˇ𝑍w=\underline{Z}+\check{Z} and w¯=Z¯¯𝑤¯𝑍\underline{w}=\underline{Z}. Note that in a special case when Z¯T=Z¯tsubscript¯𝑍𝑇subscript¯𝑍𝑡\underline{Z}\_{T}=\underline{Z}\_{t}, the bivariate transition PDF becomes a univariate one:

|  |  |  |
| --- | --- | --- |
|  | ℚ~t​{Z¯T=Z¯t,ZˇT∈d​kˇ;Z¯t=Z¯,Zˇt=Zˇ}=b~​(kˇ;w,T−t)​d​kˇsubscript~ℚ𝑡formulae-sequencesubscript¯𝑍𝑇subscript¯𝑍𝑡formulae-sequencesubscriptˇ𝑍𝑇𝑑ˇ𝑘formulae-sequencesubscript¯𝑍𝑡¯𝑍subscriptˇ𝑍𝑡ˇ𝑍~𝑏  ˇ𝑘𝑤𝑇𝑡 𝑑ˇ𝑘\displaystyle\tilde{\mathbb{Q}}\_{t}\{\underline{Z}\_{T}=\underline{Z}\_{t},\check{Z}\_{T}\in d\check{k};\underline{Z}\_{t}=\underline{Z},\check{Z}\_{t}=\check{Z}\}=\tilde{b}(\check{k};w,T-t)d\check{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | b~​(kˇ;w,T−t)≡2π​(T−t)​(e−kˇ22​(T−t)−e−(kˇ+w−w¯)22​(T−t)),kˇ≥0.formulae-sequence~𝑏  ˇ𝑘𝑤𝑇𝑡2𝜋𝑇𝑡superscript𝑒superscriptˇ𝑘22𝑇𝑡superscript𝑒superscriptˇ𝑘𝑤¯𝑤22𝑇𝑡ˇ𝑘0\displaystyle\tilde{b}(\check{k};w,T-t)\equiv\sqrt{\frac{2}{\pi(T-t)}}\left(e^{-\frac{\check{k}^{2}}{2(T-t)}}-e^{-\frac{(\check{k}+w-\underline{w})^{2}}{2(T-t)}}\right),\qquad\check{k}\geq 0\,. |  | (54) |

Next we construct the bivariate transition PDF for the double-exponential process ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")). Let F¯Tssubscriptsuperscript¯𝐹𝑠𝑇\underline{F}^{s}\_{T} be the minimum of F𝐹F at T𝑇T conditional on surviving to T𝑇T.
Similarly, let FˇTssubscriptsuperscriptˇ𝐹𝑠𝑇\check{F}^{s}\_{T}
be the drawup of F𝐹F at T𝑇T, conditional on surviving to T𝑇T.
The bivariate transition PDF of
the Brownian Minimum and Brownian Drawup can be used to
derive the bivariate PDF of the pair (F¯Ts,FˇTs)subscriptsuperscript¯𝐹𝑠𝑇subscriptsuperscriptˇ𝐹𝑠𝑇(\underline{F}^{s}\_{T},\check{F}^{s}\_{T}),
conditional both on surviving to T𝑇T and on (F¯ts,Fˇt)=(F¯,Fˇ)subscriptsuperscript¯𝐹𝑠𝑡subscriptˇ𝐹𝑡¯𝐹ˇ𝐹(\underline{F}^{s}\_{t},\check{F}\_{t})=(\underline{F},\check{F}).
For J∈(0,F0]𝐽0subscript𝐹0J\in(0,F\_{0}], and Kˇ≥1ˇ𝐾1\check{K}\geq 1, we seek:

|  |  |  |
| --- | --- | --- |
|  | ℚ​{F¯Ts∈d​J,FˇTs∈d​Kˇ|NT=0,F¯ts=F¯,Fˇt=Fˇ}.ℚconditional-setformulae-sequencesubscriptsuperscript¯𝐹𝑠𝑇𝑑𝐽subscriptsuperscriptˇ𝐹𝑠𝑇𝑑ˇ𝐾formulae-sequencesubscript𝑁𝑇0formulae-sequencesubscriptsuperscript¯𝐹𝑠𝑡¯𝐹subscriptˇ𝐹𝑡ˇ𝐹\mathbb{Q}\{\underline{F}^{s}\_{T}\in dJ,\check{F}^{s}\_{T}\in d\check{K}|N\_{T}=0,\underline{F}^{s}\_{t}=\underline{F},\check{F}\_{t}=\check{F}\}. |  |

In other words, we wish to know the bivariate conditional PDF when we change variables from (j,kˇ)𝑗ˇ𝑘(j,\check{k}) to:

|  |  |  |
| --- | --- | --- |
|  | (J,Kˇ)=(F0​eα​j,eβ−αβ​kˇ).𝐽ˇ𝐾subscript𝐹0superscript𝑒𝛼𝑗subscriptsuperscript𝑒𝛽ˇ𝑘𝛽𝛼(J,\check{K})=(F\_{0}e^{\alpha j},e^{\beta\check{k}}\_{\beta-\alpha}). |  |

Let j​(J)𝑗𝐽j(J) be the inverse of J=F0​eα​j𝐽subscript𝐹0superscript𝑒𝛼𝑗J=F\_{0}e^{\alpha j}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | j​(J)=1α​ln⁡(JF0),J∈(0,F0].formulae-sequence𝑗𝐽1𝛼𝐽subscript𝐹0𝐽0subscript𝐹0j(J)=\frac{1}{\alpha}\ln\left(\frac{J}{F\_{0}}\right),\qquad J\in(0,F\_{0}]. |  | (55) |

Similarly, let kˇ​(Kˇ)ˇ𝑘ˇ𝐾\check{k}(\check{K}) be the inverse of Kˇ=eβ−αβ​kˇˇ𝐾subscriptsuperscript𝑒𝛽ˇ𝑘𝛽𝛼\check{K}=e^{\beta\check{k}}\_{\beta-\alpha}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | kˇ​(Kˇ)=1β​ln⁡[β​Kˇ+α2+β2​(Kˇ2−1)α+β],Kˇ≥1.formulae-sequenceˇ𝑘ˇ𝐾1𝛽𝛽ˇ𝐾superscript𝛼2superscript𝛽2superscriptˇ𝐾21𝛼𝛽ˇ𝐾1\check{k}(\check{K})=\frac{1}{\beta}\ln\left[\frac{\beta\check{K}+\sqrt{\alpha^{2}+\beta^{2}(\check{K}^{2}-1)}}{\alpha+\beta}\right],\qquad\check{K}\geq 1. |  | (56) |

The determinant of the Jacobian for this change of variables is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (α​J​α2+β2​(Kˇ2−1))−1.superscript𝛼𝐽superscript𝛼2superscript𝛽2superscriptˇ𝐾211\left(\alpha J\sqrt{\alpha^{2}+\beta^{2}(\check{K}^{2}-1)}\right)^{-1}\,. |  | (57) |

Using the standard change of variables formula, it follows that for J∈(0,F0],Kˇ≥1formulae-sequence𝐽0subscript𝐹0ˇ𝐾1J\in(0,F\_{0}],\check{K}\geq 1,
the conditional bivariate PDF of the pair (F¯Ts,FˇTs)subscriptsuperscript¯𝐹𝑠𝑇subscriptsuperscriptˇ𝐹𝑠𝑇(\underline{F}^{s}\_{T},\check{F}^{s}\_{T}) is given by:

|  |  |  |
| --- | --- | --- |
|  | ℚ​{F¯Ts∈d​J,FˇTs∈d​Kˇ|NT=0,F¯ts=F¯,Fˇt=Fˇ}=f​(J,Kˇ;w,T−t)​d​J​d​Kˇℚconditional-setformulae-sequencesubscriptsuperscript¯𝐹𝑠𝑇𝑑𝐽subscriptsuperscriptˇ𝐹𝑠𝑇𝑑ˇ𝐾formulae-sequencesubscript𝑁𝑇0formulae-sequencesubscriptsuperscript¯𝐹𝑠𝑡¯𝐹subscriptˇ𝐹𝑡ˇ𝐹𝑓𝐽ˇ𝐾𝑤𝑇𝑡𝑑𝐽𝑑ˇ𝐾\displaystyle\mathbb{Q}\{\underline{F}^{s}\_{T}\in dJ,\check{F}^{s}\_{T}\in d\check{K}|N\_{T}=0,\underline{F}^{s}\_{t}=\underline{F},\check{F}\_{t}=\check{F}\}=f(J,\check{K};w,T-t)dJd\check{K} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(J,Kˇ;w,T−t)≡2π​(T−t)3​(kˇ​(Kˇ)−j​(J)+w)​e−(kˇ​(Kˇ)−j​(J)+w)22​(T−t)α​J​α2+β2​(Kˇ2−1),𝑓𝐽ˇ𝐾𝑤𝑇𝑡2𝜋superscript𝑇𝑡3ˇ𝑘ˇ𝐾𝑗𝐽𝑤superscript𝑒superscriptˇ𝑘ˇ𝐾𝑗𝐽𝑤22𝑇𝑡𝛼𝐽superscript𝛼2superscript𝛽2superscriptˇ𝐾21\displaystyle f(J,\check{K};w,T-t)\equiv\sqrt{\frac{2}{\pi(T-t)^{3}}}\frac{\left(\check{k}(\check{K})-j(J)+w\right)e^{-\frac{\left(\check{k}(\check{K})-j(J)+w\right)^{2}}{2(T-t)}}}{\alpha J\sqrt{\alpha^{2}+\beta^{2}(\check{K}^{2}-1)}}\,, |  | (58) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | w=j​(F¯)+kˇ​(Fˇ).𝑤𝑗¯𝐹ˇ𝑘ˇ𝐹w=j(\underline{F})+\check{k}(\check{F}). |  | (59) |

Note that w=Zt𝑤subscript𝑍𝑡w=Z\_{t}, and the reason we use w𝑤w is that it is written on market observables Fˇˇ𝐹\check{F} and F¯¯𝐹\underline{F} while Ztsubscript𝑍𝑡Z\_{t} is not.

Let FTs=F¯Ts​FˇTssubscriptsuperscript𝐹𝑠𝑇subscriptsuperscript¯𝐹𝑠𝑇subscriptsuperscriptˇ𝐹𝑠𝑇F^{s}\_{T}=\underline{F}^{s}\_{T}\check{F}^{s}\_{T} be the forward price at T𝑇T
conditional on survival to T𝑇T.
The bivariate PDF of the pair (F¯Ts,FˇTs)subscriptsuperscript¯𝐹𝑠𝑇subscriptsuperscriptˇ𝐹𝑠𝑇(\underline{F}^{s}\_{T},\check{F}^{s}\_{T})
can be used calculate the conditional transition PDF of FTssubscriptsuperscript𝐹𝑠𝑇F^{s}\_{T}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ​{FTs∈d​F|NT=0,F¯ts=F¯,Fˇt=Fˇ}=g​(F;w,T−t)​d​F,ℚconditional-setsubscriptsuperscript𝐹𝑠𝑇𝑑𝐹formulae-sequencesubscript𝑁𝑇0formulae-sequencesubscriptsuperscript¯𝐹𝑠𝑡¯𝐹subscriptˇ𝐹𝑡ˇ𝐹𝑔  𝐹𝑤𝑇𝑡 𝑑𝐹\displaystyle\mathbb{Q}\{F^{s}\_{T}\in dF|N\_{T}=0,\underline{F}^{s}\_{t}=\underline{F},\check{F}\_{t}=\check{F}\}=g(F;w,T-t)dF\,, |  | (60) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(F;w,T−t)𝑔  𝐹𝑤𝑇𝑡\displaystyle g(F;w,T-t) | =\displaystyle= | ∫0F0f​(J,FJ;w,T−t)​𝑑Jsuperscriptsubscript0subscript𝐹0𝑓𝐽𝐹𝐽𝑤𝑇𝑡differential-d𝐽\displaystyle\int\_{0}^{F\_{0}}f\left(J,\frac{F}{J};w,T-t\right)dJ |  |
|  |  | =\displaystyle= | ∫0F02π​(T−t)3​(k​(FJ)−j​(J)+w)​e−(k​(FJ)−j​(J)+w)22​(T−t)α​J​α2+β2​[(FJ)2−1]​𝑑J,superscriptsubscript0subscript𝐹02𝜋superscript𝑇𝑡3𝑘𝐹𝐽𝑗𝐽𝑤superscript𝑒superscript𝑘𝐹𝐽𝑗𝐽𝑤22𝑇𝑡𝛼𝐽superscript𝛼2superscript𝛽2delimited-[]superscript𝐹𝐽21differential-d𝐽\displaystyle\int\_{0}^{F\_{0}}\sqrt{\frac{2}{\pi(T-t)^{3}}}\frac{\left(k\left(\frac{F}{J}\right)-j(J)+w\right)e^{-\frac{\left(k\left(\frac{F}{J}\right)-j(J)+w\right)^{2}}{2(T-t)}}}{\alpha J\sqrt{\alpha^{2}+\beta^{2}\left[\left(\frac{F}{J}\right)^{2}-1\right]}}dJ, |  |

and w𝑤w is given in ([59](#S3.E59 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")).
When F𝐹F is only conditioned on surviving to t𝑡t rather than to T𝑇T,
the transition PDF’s of both (F¯T,FˇT)subscript¯𝐹𝑇subscriptˇ𝐹𝑇(\underline{F}\_{T},\check{F}\_{T}) and FTsubscript𝐹𝑇F\_{T} are just given by the product of
their corresponding transition PDF conditioned on survival to T𝑇T and the probability of further surviving to T𝑇T,
which is e−β22​(T−t)superscript𝑒superscript𝛽22𝑇𝑡e^{-\frac{\beta^{2}}{2}(T-t)}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℚ​{F¯T∈d​J,FˇT∈d​Kˇ|Nt=0,F¯ts=F¯,Fˇt=Fˇ}ℚconditional-setformulae-sequencesubscript¯𝐹𝑇𝑑𝐽subscriptˇ𝐹𝑇𝑑ˇ𝐾formulae-sequencesubscript𝑁𝑡0formulae-sequencesubscriptsuperscript¯𝐹𝑠𝑡¯𝐹subscriptˇ𝐹𝑡ˇ𝐹\displaystyle\mathbb{Q}\{\underline{F}\_{T}\in dJ,\check{F}\_{T}\in d\check{K}|N\_{t}=0,\underline{F}^{s}\_{t}=\underline{F},\check{F}\_{t}=\check{F}\} | =\displaystyle= | f​(J,Kˇ;w,T−t)​e−β22​(T−t)​d​J​d​Kˇ,𝑓𝐽ˇ𝐾𝑤𝑇𝑡superscript𝑒superscript𝛽22𝑇𝑡𝑑𝐽𝑑ˇ𝐾\displaystyle f(J,\check{K};w,T-t)e^{-\frac{\beta^{2}}{2}(T-t)}dJd\check{K}\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ℚ​{FT∈d​F|Nt=0,F¯ts=F¯,Fˇt=Fˇ}ℚconditional-setsubscript𝐹𝑇𝑑𝐹formulae-sequencesubscript𝑁𝑡0formulae-sequencesubscriptsuperscript¯𝐹𝑠𝑡¯𝐹subscriptˇ𝐹𝑡ˇ𝐹\displaystyle\mathbb{Q}\{F\_{T}\in dF|N\_{t}=0,\underline{F}^{s}\_{t}=\underline{F},\check{F}\_{t}=\check{F}\} | =\displaystyle= | g​(F;w,T−t)​e−β22​(T−t)​d​F.𝑔  𝐹𝑤𝑇𝑡 superscript𝑒superscript𝛽22𝑇𝑡𝑑𝐹\displaystyle g(F;w,T-t)e^{-\frac{\beta^{2}}{2}(T-t)}dF\,. |  | (62) |

The PDF of FTsubscript𝐹𝑇F\_{T} is an integral over a bounded domain and it cannot be simplified further.
We will find that
when common payoffs are integrated against this PDF, additional quadratures are not introduced.
It is for this reason that we consider the process F𝐹F to be tractable.

There are two similar constructions of a non-negative martingale which also
use jump to default.
The cumulative hazard process of N𝑁N is
Λt=eβ22​tsubscriptΛ𝑡superscript𝑒superscript𝛽22𝑡\Lambda\_{t}=e^{\frac{\beta^{2}}{2}t}
which is deterministic.
Suppose instead that the cumulative hazard process is
Λ^t=e−α​Z¯tsubscript^Λ𝑡superscript𝑒𝛼subscript¯𝑍𝑡\hat{\Lambda}\_{t}=e^{-\alpha\underline{Z}\_{t}}, which is random.
Let N^^𝑁\hat{N} denote the corresponding counting process and
let F^^𝐹\hat{F} denote the desired non-negative martingale:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^t=F0​e−β22​t​eβ−αβ​Zˇt​𝟙Nt=0,t≥t0formulae-sequencesubscript^𝐹𝑡subscript𝐹0superscript𝑒superscript𝛽22𝑡subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼subscript1subscript𝑁𝑡0𝑡subscript𝑡0\hat{F}\_{t}=F\_{0}e^{-\frac{\beta^{2}}{2}t}e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}\mathbbm{1}\_{N\_{t}=0}\,,\qquad t\geq t\_{0} |  | (63) |

is a non-negative martingale started at F0>0subscript𝐹00F\_{0}>0.
Since Z¯0=0subscript¯𝑍00\underline{Z}\_{0}=0, this process start off with no chance of
jumping to zero but soon endures the possibility of such a default.
More generally, one can start the process Z¯¯𝑍\underline{Z} at some non-positive number m0≤0subscript𝑚00m\_{0}\leq 0 and rename the process Z¯¯𝑍\underline{Z} to say m𝑚m
since Z0subscript𝑍0Z\_{0} is still zero.
Since Zˇt=Zt−mtsubscriptˇ𝑍𝑡subscript𝑍𝑡subscript𝑚𝑡\check{Z}\_{t}=Z\_{t}-m\_{t} starts at −m0>0subscript𝑚00-m\_{0}>0,
one must then also adjust its origin:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=F0​e−β22​t​eβ−αβ​(Zˇt+m0)​𝟙N^t=0,t≥t0formulae-sequencesubscript𝐹𝑡subscript𝐹0superscript𝑒superscript𝛽22𝑡subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡subscript𝑚0𝛽𝛼subscript1subscript^𝑁𝑡0𝑡subscript𝑡0F\_{t}=F\_{0}e^{-\frac{\beta^{2}}{2}t}e^{\beta(\check{Z}\_{t}+m\_{0})}\_{\beta-\alpha}\mathbbm{1}\_{\hat{N}\_{t}=0},\qquad t\geq t\_{0} |  | (64) |

There is yet another construction of a non-negative martingale possibly jumping to zero.
Now suppose that the cumulative hazard process of N𝑁N is
Λ~t=e−α​Z¯t+β22​tsubscript~Λ𝑡superscript𝑒𝛼subscript¯𝑍𝑡superscript𝛽22𝑡\tilde{\Lambda}\_{t}=e^{-\alpha\underline{Z}\_{t}+\frac{\beta^{2}}{2}t}, where we return to
Zˇt=Zt−Z¯tsubscriptˇ𝑍𝑡subscript𝑍𝑡subscript¯𝑍𝑡\check{Z}\_{t}=Z\_{t}-\underline{Z}\_{t} with Z¯0=0subscript¯𝑍00\underline{Z}\_{0}=0.
Let N~~𝑁\tilde{N} denote the corresponding counting process and
let F~~𝐹\tilde{F} denote the desired non-negative martingale:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F~t=F0​eβ−αβ​Zˇt​𝟙N~t=0,t≥t0formulae-sequencesubscript~𝐹𝑡subscript𝐹0subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑡𝛽𝛼subscript1subscript~𝑁𝑡0𝑡subscript𝑡0\tilde{F}\_{t}=F\_{0}e^{\beta\check{Z}\_{t}}\_{\beta-\alpha}\mathbbm{1}\_{\tilde{N}\_{t}=0},\qquad t\geq t\_{0} |  | (65) |

is a non-negative martingale started at F0>0subscript𝐹00F\_{0}>0.
This process is convenient if an event happens
at the first passage time τ𝜏\tau of
F𝐹F to a constant upper barrier
H=eβ−αβ​h𝐻subscriptsuperscript𝑒𝛽ℎ𝛽𝛼H=e^{\beta h}\_{\beta-\alpha} where h>0ℎ0h>0.
In this case, τ𝜏\tau is also the first passage time of
Zˇˇ𝑍\check{Z} to hℎh.
Since FF0𝐹subscript𝐹0\frac{F}{F\_{0}} is a martingale started at one, the
bivariate Laplace transform of Z¯τsubscript¯𝑍𝜏\underline{Z}\_{\tau} and τ𝜏\tau becomes known:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =E​eα​Z¯τ−β22​τ​1eβ−αβ​h.absent𝐸superscript𝑒𝛼subscript¯𝑍𝜏superscript𝛽22𝜏1subscriptsuperscript𝑒𝛽ℎ𝛽𝛼=Ee^{\alpha\underline{Z}\_{\tau}-\frac{\beta^{2}}{2}\tau}\frac{1}{e^{\beta h}\_{\beta-\alpha}}. |  | (66) |

One can develop yet other tractable constructions of non-negative martingales
by altering the cumulative hazard process yet again
and compensating by coordinate change as was done above.

## 4 Application in Option Pricing

In risk neutral measure, non-arbitrage insures that the expected payoff of a security is equal to its current price. In this section we show how our model can be applied in derivative pricing assuming the underlying asset follows the dynamics of either the sub-martingale Eqn ([44](#S3.E44 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) or the martingale Eqn ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) in risk neutral measure. The former is used for derivatives written on spot price of a security while the latter is for future price of a security. Since the two processes only differ by the inclusion of a jump to default process, the pricing formulas for them are quite close. For this reason, we only present the derivation of pricing for the martingale dynamics. The results for the sub-martingale dynamics are labelled by subscripts for clarification. Note since our model tracks the asset’s running minimum and drawup rate, it is especially useful in pricing barrier type of path-dependent options.

### 4.1 One-Touch with a lower barrier

We first price a One-Touch with a lower barrier. A One-Touch option pays one dollar if the underlying asset’s price touches the lower barrier price before maturity, and otherwise expires worthless. Assuming that the present time is t𝑡t and the underlying asset has not defaulted (Nt=0subscript𝑁𝑡0N\_{t}=0). The price of a One-Touch with a lower barrier L𝐿L and maturity T𝑇T is

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | O​Tt​(L,T)𝑂subscript𝑇𝑡𝐿𝑇\displaystyle OT\_{t}(L,T) | =\displaystyle= | 𝟙F¯t≤L+𝟙F¯t>L⋅(𝟙NT=0​Et​[𝟙F¯T≤L]+𝟙NT≠0)subscript1subscript¯𝐹𝑡𝐿⋅subscript1subscript¯𝐹𝑡𝐿subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscript1subscript¯𝐹𝑇𝐿subscript1subscript𝑁𝑇0\displaystyle\mathbbm{1}\_{\underline{F}\_{t}\leq L}+\mathbbm{1}\_{\underline{F}\_{t}>L}\cdot\left(\mathbbm{1}\_{N\_{T}=0}E\_{t}\left[\mathbbm{1}\_{\underline{F}\_{T}\leq L}\right]+\mathbbm{1}\_{N\_{T}\neq 0}\right) |  | (67) |
|  |  | =\displaystyle= | 𝟙F¯t≤L+𝟙F¯t>L⋅(e−β2​(T−t)2​Et​[𝟙Z¯T≤ln⁡L−ln⁡F0α]+1−e−β2​(T−t)2),subscript1subscript¯𝐹𝑡𝐿⋅subscript1subscript¯𝐹𝑡𝐿superscript𝑒superscript𝛽2𝑇𝑡2subscript𝐸𝑡delimited-[]subscript1subscript¯𝑍𝑇𝐿subscript𝐹0𝛼1superscript𝑒superscript𝛽2𝑇𝑡2\displaystyle\mathbbm{1}\_{\underline{F}\_{t}\leq L}+\mathbbm{1}\_{\underline{F}\_{t}>L}\cdot\left(e^{-\frac{\beta^{2}(T-t)}{2}}E\_{t}\left[\mathbbm{1}\_{\underline{Z}\_{T}\leq\frac{\ln L-\ln F\_{0}}{\alpha}}\right]+1-e^{-\frac{\beta^{2}(T-t)}{2}}\right)\,, |  |

to get the second line, F¯T=F0​eα​Z¯Tsubscript¯𝐹𝑇subscript𝐹0superscript𝑒𝛼subscript¯𝑍𝑇\underline{F}\_{T}=F\_{0}e^{\alpha\underline{Z}\_{T}} has been used. After substituting the transition PDF on Z¯Tsubscript¯𝑍𝑇\underline{Z}\_{T} one obtains

|  |  |  |  |
| --- | --- | --- | --- |
|  | O​Tt​(L,T)=𝟙F¯t≤L+𝟙F¯t>L⋅(e−β2​(T−t)2​[2​N​(ln⁡L−ln⁡F0α−wT−t)−1]+1),𝑂subscript𝑇𝑡𝐿𝑇subscript1subscript¯𝐹𝑡𝐿⋅subscript1subscript¯𝐹𝑡𝐿superscript𝑒superscript𝛽2𝑇𝑡2delimited-[]2𝑁𝐿subscript𝐹0𝛼𝑤𝑇𝑡11\displaystyle OT\_{t}(L,T)=\mathbbm{1}\_{\underline{F}\_{t}\leq L}+\mathbbm{1}\_{\underline{F}\_{t}>L}\cdot\left(e^{-\frac{\beta^{2}(T-t)}{2}}\left[2N\left(\frac{\frac{\ln L-\ln F\_{0}}{\alpha}-w}{\sqrt{T-t}}\right)-1\right]+1\right)\,, |  | (68) |

where w𝑤w is given in ([59](#S3.E59 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) and N𝑁N is the standard normal distribution function. Taking α=1𝛼1\alpha=1 the price of the One-Touch reduces to that in [[2](#bib.bib2)]. This is because essentially the payoff of a One-Touch option is only determined by the minimum of the underlying, which is driven by the running minimum of a Brownian motion in both cases.

A One-Touch written on spot price can be priced similarly with Eqn ([44](#S3.E44 "In 3.1 Constructing a Positive Continuous Process with Constant Drift ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")), which is equivalent to dropping the probability induced by the jump to default process in Eqn ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")). The price is then given by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | O​TtSpot​(L,T)𝑂subscriptsuperscript𝑇Spot𝑡𝐿𝑇\displaystyle OT^{\rm{Spot}}\_{t}(L,T) | =\displaystyle= | 𝟙F¯t≤L+𝟙F¯t>L⋅Et​[𝟙F¯T≤L]subscript1subscript¯𝐹𝑡𝐿⋅subscript1subscript¯𝐹𝑡𝐿subscript𝐸𝑡delimited-[]subscript1subscript¯𝐹𝑇𝐿\displaystyle\mathbbm{1}\_{\underline{F}\_{t}\leq L}+\mathbbm{1}\_{\underline{F}\_{t}>L}\cdot E\_{t}\left[\mathbbm{1}\_{\underline{F}\_{T}\leq L}\right] |  | (69) |
|  |  | =\displaystyle= | 𝟙F¯t≤L+𝟙F¯t>L⋅2​N​(ln⁡L−ln⁡F0α−wT−t).subscript1subscript¯𝐹𝑡𝐿⋅subscript1subscript¯𝐹𝑡𝐿2𝑁𝐿subscript𝐹0𝛼𝑤𝑇𝑡\displaystyle\mathbbm{1}\_{\underline{F}\_{t}\leq L}+\mathbbm{1}\_{\underline{F}\_{t}>L}\cdot 2N\left(\frac{\frac{\ln L-\ln F\_{0}}{\alpha}-w}{\sqrt{T-t}}\right)\,. |  |

### 4.2 Lookback option

A lookback call option matures at T𝑇T with a floating strike price pays off the difference between the terminal value of the asset and its minimum, namely the terminal drawup. If default happens (NT≠0)subscript𝑁𝑇0(N\_{T}\neq 0), the option expires worthless (FT=F¯T)subscript𝐹𝑇subscript¯𝐹𝑇(F\_{T}=\underline{F}\_{T}). So under the martingale ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) the value of this option at maturity is then

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L​Cf​l​o​a​t,t𝐿subscript𝐶  𝑓𝑙𝑜𝑎𝑡𝑡\displaystyle LC\_{float,t} | =\displaystyle= | 𝟙NT=0​Et​[FT−F¯T]=𝟙NT=0​Et​[F¯T​(FˇT−1)]subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscript𝐹𝑇subscript¯𝐹𝑇subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscript¯𝐹𝑇subscriptˇ𝐹𝑇1\displaystyle\mathbbm{1}\_{N\_{T}=0}E\_{t}\left[F\_{T}-\underline{F}\_{T}\right]=\mathbbm{1}\_{N\_{T}=0}E\_{t}\left[\underline{F}\_{T}\left(\check{F}\_{T}-1\right)\right] |  | (70) |
|  |  | =\displaystyle= | 𝟙NT=0​Et​[F0​eα​Z¯T​(eβ−αβ​ZˇT−1)].subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscript𝐹0superscript𝑒𝛼subscript¯𝑍𝑇subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑇𝛽𝛼1\displaystyle\mathbbm{1}\_{N\_{T}=0}E\_{t}\left[F\_{0}e^{\alpha\underline{Z}\_{T}}\left(e^{\beta\check{Z}\_{T}}\_{\beta-\alpha}-1\right)\right]\,. |  |

The expectation value in Eqn ([70](#S4.E70 "In 4.2 Lookback option ‣ 4 Application in Option Pricing")) can be evaluated using the bivariate transition PDF of (Z¯T,ZˇT)subscript¯𝑍𝑇subscriptˇ𝑍𝑇(\underline{Z}\_{T},\check{Z}\_{T}) the in Eqn ([53](#S3.E53 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) if the security runs into a new minimum after t𝑡t, or otherwise the univariate transition PDF of ZˇTsubscriptˇ𝑍𝑇\check{Z}\_{T} in Eqn([54](#S3.E54 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) if Z¯T=Z¯tsubscript¯𝑍𝑇subscript¯𝑍𝑡\underline{Z}\_{T}=\underline{Z}\_{t}:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Et​[F0​eα​Z¯T​(eβ−αβ​ZˇT−1)]subscript𝐸𝑡delimited-[]subscript𝐹0superscript𝑒𝛼subscript¯𝑍𝑇subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑇𝛽𝛼1\displaystyle E\_{t}\left[F\_{0}e^{\alpha\underline{Z}\_{T}}\left(e^{\beta\check{Z}\_{T}}\_{\beta-\alpha}-1\right)\right] | =\displaystyle= | F0​∫−∞Z¯t𝑑j​∫0∞𝑑kˇ​2π​(T−t)3​(kˇ−j+w)​e−(kˇ−j+w)22​(T−t)​eα​j​(eβ−αβ​kˇ−1)subscript𝐹0subscriptsuperscriptsubscript¯𝑍𝑡differential-d𝑗superscriptsubscript0differential-dˇ𝑘2𝜋superscript𝑇𝑡3ˇ𝑘𝑗𝑤superscript𝑒superscriptˇ𝑘𝑗𝑤22𝑇𝑡superscript𝑒𝛼𝑗subscriptsuperscript𝑒𝛽ˇ𝑘𝛽𝛼1\displaystyle F\_{0}\int^{\underline{Z}\_{t}}\_{-\infty}dj\int\_{0}^{\infty}d\check{k}\sqrt{\frac{2}{\pi(T-t)^{3}}}(\check{k}-j+w)e^{-\frac{(\check{k}-j+w)^{2}}{2(T-t)}}e^{\alpha j}\left(e^{\beta\check{k}}\_{\beta-\alpha}-1\right) |  | (71) |
|  |  | +\displaystyle+ | F0​∫0∞𝑑kˇ​2π​(T−t)​(e−kˇ22​(T−t)−e−(kˇ+wˇ)22​(T−t))​eα​w¯​(eβ−αβ​kˇ−1),subscript𝐹0superscriptsubscript0differential-dˇ𝑘2𝜋𝑇𝑡superscript𝑒superscriptˇ𝑘22𝑇𝑡superscript𝑒superscriptˇ𝑘ˇ𝑤22𝑇𝑡superscript𝑒𝛼¯𝑤subscriptsuperscript𝑒𝛽ˇ𝑘𝛽𝛼1\displaystyle F\_{0}\int\_{0}^{\infty}d\check{k}\sqrt{\frac{2}{\pi(T-t)}}\left(e^{-\frac{\check{k}^{2}}{2(T-t)}}-e^{-\frac{(\check{k}+\check{w})^{2}}{2(T-t)}}\right)e^{\alpha\underline{w}}\left(e^{\beta\check{k}}\_{\beta-\alpha}-1\right)\,, |  |

where wˇ=w−w¯ˇ𝑤𝑤¯𝑤\check{w}=w-\underline{w}. By working out the integral we obtain the price of this option evaluated at t𝑡t

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L​Cf​l​o​a​t,t𝐿subscript𝐶  𝑓𝑙𝑜𝑎𝑡𝑡\displaystyle LC\_{float,t} | =\displaystyle= | F0eα​w¯[αβeβ​wˇN(−wˇ−β​(T−t)T−t)−αβe−β​wˇN(−wˇ+β​(T−t)T−t)\displaystyle F\_{0}e^{\alpha\underline{w}}\bigg{[}\frac{\alpha}{\beta}e^{\beta\check{w}}N\left(\frac{-\check{w}-\beta(T-t)}{\sqrt{T-t}}\right)-\frac{\alpha}{\beta}e^{-\beta\check{w}}N\left(\frac{-\check{w}+\beta(T-t)}{\sqrt{T-t}}\right) |  | (72) |
|  |  | +\displaystyle+ | β+αβ​N​(β​T−t)+β−αβ​N​(−β​T−t)+e−β2​(T−t)2​(2​N​(−wˇT−t)−1)𝛽𝛼𝛽𝑁𝛽𝑇𝑡𝛽𝛼𝛽𝑁𝛽𝑇𝑡superscript𝑒superscript𝛽2𝑇𝑡22𝑁ˇ𝑤𝑇𝑡1\displaystyle\frac{\beta+\alpha}{\beta}N\left(\beta\sqrt{T-t}\right)+\frac{\beta-\alpha}{\beta}N\left(-\beta\sqrt{T-t}\right)+e^{-\frac{\beta^{2}(T-t)}{2}}\left(2N\left(\frac{-\check{w}}{\sqrt{T-t}}\right)-1\right) |  |
|  |  | −\displaystyle- | 2eα​wˇ+(α2−β2)​(T−t)2N(−wˇ−α​(T−t)T−t)].\displaystyle 2e^{\alpha\check{w}+\frac{(\alpha^{2}-\beta^{2})(T-t)}{2}}N\left(\frac{-\check{w}-\alpha(T-t)}{\sqrt{T-t}}\right)\bigg{]}\,. |  |

A lookback call option on spot price can be priced the same way:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L​Cf​l​o​a​t,tSpot𝐿subscriptsuperscript𝐶Spot  𝑓𝑙𝑜𝑎𝑡𝑡\displaystyle LC^{\rm{Spot}}\_{float,t} | =\displaystyle= | Et​[FT−F¯T]=Et​[F0​eα​Z¯T​(eβ−αβ​ZˇT−1)]subscript𝐸𝑡delimited-[]subscript𝐹𝑇subscript¯𝐹𝑇subscript𝐸𝑡delimited-[]subscript𝐹0superscript𝑒𝛼subscript¯𝑍𝑇subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑇𝛽𝛼1\displaystyle E\_{t}\left[F\_{T}-\underline{F}\_{T}\right]=E\_{t}\left[F\_{0}e^{\alpha\underline{Z}\_{T}}\left(e^{\beta\check{Z}\_{T}}\_{\beta-\alpha}-1\right)\right] |  | (73) |
|  |  | =\displaystyle= | eβ2​(T−t)2​L​Cf​l​o​a​t,t.superscript𝑒superscript𝛽2𝑇𝑡2𝐿subscript𝐶  𝑓𝑙𝑜𝑎𝑡𝑡\displaystyle e^{\frac{\beta^{2}(T-t)}{2}}LC\_{float,t}\,. |  |

If we instead consider a lookback option with a fixed strike price, then the payoff is determined by the minimum/maximum for a put/call lookback option at maturity. Since Eqn ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")) tracks minimum and drawup, it can also be used to evaluate a lookback put option with fixed price. The price is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L​Pf​i​x​e​d,t​(K,T)𝐿subscript𝑃  𝑓𝑖𝑥𝑒𝑑𝑡𝐾𝑇\displaystyle LP\_{fixed,t}(K,T) | =\displaystyle= | 𝟙NT=0​Et​[(K−F¯T)+]+𝟙NT≠0⋅K,subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]superscript𝐾subscript¯𝐹𝑇⋅subscript1subscript𝑁𝑇0𝐾\displaystyle\mathbbm{1}\_{N\_{T}=0}E\_{t}\left[(K-\underline{F}\_{T})^{+}\right]+\mathbbm{1}\_{N\_{T}\neq 0}\cdot K\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L​Pf​i​x​e​d,tSpot​(K,T)𝐿subscriptsuperscript𝑃Spot  𝑓𝑖𝑥𝑒𝑑𝑡𝐾𝑇\displaystyle LP^{\rm{Spot}}\_{fixed,t}(K,T) | =\displaystyle= | Et​[(K−F¯T)+],subscript𝐸𝑡delimited-[]superscript𝐾subscript¯𝐹𝑇\displaystyle E\_{t}\left[(K-\underline{F}\_{T})^{+}\right]\,, |  | (74) |

where K𝐾K is the strike price. This can be evaluated by integrating the price of a one-touch barrier with respect to the barrier, so we will not carry out the derivation for simplicity.

We can also engineer another derivative analogous to a lookback call option with a floating strike price, which pays off the ratio between the terminal price and the minimum price before maturity. Since the underlying asset can default (FT=F¯T=0subscript𝐹𝑇subscript¯𝐹𝑇0F\_{T}=\underline{F}\_{T}=0), we assume the payoff is zero in that case. The price of this option is given by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L​Cf​l​o​a​t,t∗𝐿subscriptsuperscript𝐶  𝑓𝑙𝑜𝑎𝑡𝑡\displaystyle LC^{\*}\_{float,t} | =\displaystyle= | 𝟙NT=0​Et​[FT−F¯TF¯T]=𝟙NT=0​(Et​[FTF¯T]−1)subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscript𝐹𝑇subscript¯𝐹𝑇subscript¯𝐹𝑇subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscript𝐹𝑇subscript¯𝐹𝑇1\displaystyle\mathbbm{1}\_{N\_{T}=0}E\_{t}\left[\frac{F\_{T}-\underline{F}\_{T}}{\underline{F}\_{T}}\right]=\mathbbm{1}\_{N\_{T}=0}\left(E\_{t}\left[\frac{F\_{T}}{\underline{F}\_{T}}\right]-1\right) |  | (75) |
|  |  | =\displaystyle= | 𝟙NT=0​(Et​[eβ−αβ​ZˇT]−1),subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑇𝛽𝛼1\displaystyle\mathbbm{1}\_{N\_{T}=0}\left(E\_{t}\left[e^{\beta\check{Z}\_{T}}\_{\beta-\alpha}\right]-1\right)\,, |  |

and the expectation can be evaluated with the bivariate PDF:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Et​[eβ−αβ​ZˇT]subscript𝐸𝑡delimited-[]subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑇𝛽𝛼\displaystyle E\_{t}\left[e^{\beta\check{Z}\_{T}}\_{\beta-\alpha}\right] | =\displaystyle= | ∫−∞Z¯t𝑑j​∫0∞𝑑kˇ​2π​(T−t)3​(kˇ−j+w)​e−(kˇ−j+w)22​(T−t)​eβ−αβ​kˇsubscriptsuperscriptsubscript¯𝑍𝑡differential-d𝑗superscriptsubscript0differential-dˇ𝑘2𝜋superscript𝑇𝑡3ˇ𝑘𝑗𝑤superscript𝑒superscriptˇ𝑘𝑗𝑤22𝑇𝑡subscriptsuperscript𝑒𝛽ˇ𝑘𝛽𝛼\displaystyle\int^{\underline{Z}\_{t}}\_{-\infty}dj\int\_{0}^{\infty}d\check{k}\sqrt{\frac{2}{\pi(T-t)^{3}}}(\check{k}-j+w)e^{-\frac{(\check{k}-j+w)^{2}}{2(T-t)}}e^{\beta\check{k}}\_{\beta-\alpha} |  | (76) |
|  |  | +\displaystyle+ | ∫0∞𝑑kˇ​2π​(T−t)​(e−kˇ22​(T−t)−e−(kˇ+wˇ)22​(T−t))​(eβ−αβ​kˇ−1)superscriptsubscript0differential-dˇ𝑘2𝜋𝑇𝑡superscript𝑒superscriptˇ𝑘22𝑇𝑡superscript𝑒superscriptˇ𝑘ˇ𝑤22𝑇𝑡subscriptsuperscript𝑒𝛽ˇ𝑘𝛽𝛼1\displaystyle\int\_{0}^{\infty}d\check{k}\sqrt{\frac{2}{\pi(T-t)}}\left(e^{-\frac{\check{k}^{2}}{2(T-t)}}-e^{-\frac{(\check{k}+\check{w})^{2}}{2(T-t)}}\right)\left(e^{\beta\check{k}}\_{\beta-\alpha}-1\right) |  |

which can be evaluated similar to Eqn ([72](#S4.E72 "In 4.2 Lookback option ‣ 4 Application in Option Pricing")),

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L​Cf​l​o​a​t,t∗𝐿superscriptsubscript𝐶  𝑓𝑙𝑜𝑎𝑡𝑡\displaystyle LC\_{float,t}^{\*} | =\displaystyle= | β+αβ​N​(β​T−t)+β−αβ​N​(−β​T−t)−1.𝛽𝛼𝛽𝑁𝛽𝑇𝑡𝛽𝛼𝛽𝑁𝛽𝑇𝑡1\displaystyle\frac{\beta+\alpha}{\beta}N\left(\beta\sqrt{T-t}\right)+\frac{\beta-\alpha}{\beta}N\left(-\beta\sqrt{T-t}\right)-1\,. |  | (77) |

Note that the value of L​Cf​l​o​a​t,t∗𝐿superscriptsubscript𝐶

𝑓𝑙𝑜𝑎𝑡𝑡LC\_{float,t}^{\*} is unitless, since the option is written on the drawup ratio. If there is a size associated to the underlying security, it can be multiplied to L​Cf​l​o​a​t,t∗𝐿superscriptsubscript𝐶

𝑓𝑙𝑜𝑎𝑡𝑡LC\_{float,t}^{\*} which gives it a dollar amount. As in Eqn ([73](#S4.E73 "In 4.2 Lookback option ‣ 4 Application in Option Pricing")), the price for this derivative on spot price is

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​Cf​l​o​a​t,t∗Spot=eβ2​(T−t)2​L​Cf​l​o​a​t,t∗.𝐿subscriptsuperscript𝐶absentSpot  𝑓𝑙𝑜𝑎𝑡𝑡superscript𝑒superscript𝛽2𝑇𝑡2𝐿subscriptsuperscript𝐶  𝑓𝑙𝑜𝑎𝑡𝑡\displaystyle LC^{\*\,\rm{Spot}}\_{float,t}=e^{\frac{\beta^{2}(T-t)}{2}}LC^{\*}\_{float,t}\,. |  | (78) |

### 4.3 Vanilla and Down-and-In Call

Now we price a Down-and-In Call (DIC) option which becomes from worthless to a vanilla call if the lower barrier is hit before maturity. A vanilla call can be viewed as a special case of a Down-and-In barrier call (DIC) with the lower barrier has been hit prior to presence. The value of a DIC option written on Ftsubscript𝐹𝑡F\_{t} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | DICt​(L,K,T)=𝟙F¯t≤L⋅𝟙NT=0⋅Ct​(K,T)+𝟙F¯t>L⋅𝟙NT=0⋅Et​[𝟙F¯T≤L​(FT−K)+],subscriptDIC𝑡𝐿𝐾𝑇⋅subscript1subscript¯𝐹𝑡𝐿subscript1subscript𝑁𝑇0subscript𝐶𝑡𝐾𝑇⋅subscript1subscript¯𝐹𝑡𝐿subscript1subscript𝑁𝑇0subscript𝐸𝑡delimited-[]subscript1subscript¯𝐹𝑇𝐿superscriptsubscript𝐹𝑇𝐾{\rm{DIC}}\_{t}(L,K,T)=\mathbbm{1}\_{\underline{F}\_{t}\leq L}\cdot\mathbbm{1}\_{N\_{T}=0}\cdot C\_{t}(K,T)+\mathbbm{1}\_{\underline{F}\_{t}>L}\cdot\mathbbm{1}\_{N\_{T}=0}\cdot E\_{t}\left[\mathbbm{1}\_{\underline{F}\_{T}\leq L}(F\_{T}-K)^{+}\right]\,, |  | (79) |

where L𝐿L is the barrier, K𝐾K is the strike price, T𝑇T is maturity and Ctsubscript𝐶𝑡C\_{t} is a vanilla call priced at t𝑡t. Note setting L=F0𝐿subscript𝐹0L={F}\_{0} reduces the DIC to a vanilla call. As implied by Eqn ([79](#S4.E79 "In 4.3 Vanilla and Down-and-In Call ‣ 4 Application in Option Pricing")) if default happens (NT≠0subscript𝑁𝑇0N\_{T}\neq 0), the option becomes worthless. To evaluate the expectation value of the second term in ([79](#S4.E79 "In 4.3 Vanilla and Down-and-In Call ‣ 4 Application in Option Pricing")), we once again apply the bivariate transition PDF:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Et​[𝟙F¯T≤L​(FT−K)+]subscript𝐸𝑡delimited-[]subscript1subscript¯𝐹𝑇𝐿superscriptsubscript𝐹𝑇𝐾\displaystyle E\_{t}\left[\mathbbm{1}\_{\underline{F}\_{T}\leq L}(F\_{T}-K)^{+}\right] | =\displaystyle= | Et​[𝟙Z¯T≤1α​ln⁡LF0​(F0​eα​Z¯T​eβ−αβ​ZˇT−K)+]subscript𝐸𝑡delimited-[]subscript1subscript¯𝑍𝑇1𝛼𝐿subscript𝐹0superscriptsubscript𝐹0superscript𝑒𝛼subscript¯𝑍𝑇subscriptsuperscript𝑒𝛽subscriptˇ𝑍𝑇𝛽𝛼𝐾\displaystyle E\_{t}\left[\mathbbm{1}\_{\underline{Z}\_{T}\leq\frac{1}{\alpha}\ln{\frac{L}{F\_{0}}}}(F\_{0}e^{\alpha\underline{Z}\_{T}}e^{\beta\check{Z}\_{T}}\_{\beta-\alpha}-K)^{+}\right] |  | (80) |
|  |  | =\displaystyle= | ∫−∞1α​ln⁡LF0𝑑j​∫k∗∞𝑑kˇ​2π​(T−t)3​(kˇ−j+w)​e−(kˇ−j+w)22​(T−t)​(F0​eα​j​eβ−αβ​kˇ−K),superscriptsubscript1𝛼𝐿subscript𝐹0differential-d𝑗superscriptsubscriptsuperscript𝑘differential-dˇ𝑘2𝜋superscript𝑇𝑡3ˇ𝑘𝑗𝑤superscript𝑒superscriptˇ𝑘𝑗𝑤22𝑇𝑡subscript𝐹0superscript𝑒𝛼𝑗subscriptsuperscript𝑒𝛽ˇ𝑘𝛽𝛼𝐾\displaystyle\int\_{-\infty}^{\frac{1}{\alpha}\ln{\frac{L}{F\_{0}}}}dj\int\_{k^{\*}}^{\infty}d\check{k}\sqrt{\frac{2}{\pi(T-t)^{3}}}(\check{k}-j+w)e^{-\frac{(\check{k}-j+w)^{2}}{2(T-t)}}\left(F\_{0}e^{\alpha j}e^{\beta\check{k}}\_{\beta-\alpha}-K\right)\,, |  |

where k∗​(j)superscript𝑘𝑗k^{\*}(j) is determined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | k∗=max​(f−1​(SF0​eα​j),0),f​(x)=eβ−αβ​x.formulae-sequencesuperscript𝑘maxsuperscript𝑓1𝑆subscript𝐹0superscript𝑒𝛼𝑗0𝑓𝑥subscriptsuperscript𝑒𝛽𝑥𝛽𝛼\displaystyle k^{\*}={\rm{max}}\left(f^{-1}\left(\frac{S}{F\_{0}e^{\alpha j}}\right),0\right)\,,\qquad f(x)=e^{\beta x}\_{\beta-\alpha}\,. |  | (81) |

For the dependence of k∗superscript𝑘k^{\*} on j𝑗j, the integral above cannot be obtained in closed form, a similar situation as in [[2](#bib.bib2)]. Nonetheless, the result can be further simplified as

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Et​[𝟙F¯T≤L​(FT−K)+]subscript𝐸𝑡delimited-[]subscript1subscript¯𝐹𝑇𝐿superscriptsubscript𝐹𝑇𝐾\displaystyle E\_{t}\left[\mathbbm{1}\_{\underline{F}\_{T}\leq L}(F\_{T}-K)^{+}\right] | =\displaystyle= | F0∫−∞1α​ln⁡LF0djeα​j+β2​(T−t)2[(β+α)eβ​(j−w)N(j−w−k∗+β​(T−t)T−t)\displaystyle F\_{0}\int\_{-\infty}^{\frac{1}{\alpha}\ln{\frac{L}{F\_{0}}}}dje^{\alpha j+\frac{\beta^{2}(T-t)}{2}}\bigg{[}(\beta+\alpha)e^{\beta(j-w)}N\left(\frac{j-w-k^{\*}+\beta(T-t)}{\sqrt{T-t}}\right) |  | (82) |
|  |  |  | −(β−α)e−β​(j−w)N(j−w−k∗−β​(T−t)T−t)],\displaystyle\qquad-(\beta-\alpha)e^{-\beta(j-w)}N\left(\frac{j-w-k^{\*}-\beta(T-t)}{\sqrt{T-t}}\right)\bigg{]}\,, |  |

which gives rise to the value of the DIC option
After replacing Ztsubscript𝑍𝑡Z\_{t} with the market observable w𝑤w, we now have the price for the DIC option:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | DICt​(L,K,T)subscriptDICt𝐿𝐾𝑇\displaystyle{\rm{DIC\_{t}}}(L,K,T) | =\displaystyle= | 𝟙F¯t≤LCt(K,T)+𝟙F¯t>LF0∫−∞1α​ln⁡LF0djeα​j[(β+α)eβ​(j−w)N(j−w−k∗+β​(T−t)T−t)\displaystyle\mathbbm{1}\_{\underline{F}\_{t}\leq L}C\_{t}(K,T)+\mathbbm{1}\_{\underline{F}\_{t}>L}F\_{0}\int\_{-\infty}^{\frac{1}{\alpha}\ln{\frac{L}{F\_{0}}}}dje^{\alpha j}\bigg{[}(\beta+\alpha)e^{\beta(j-w)}N\left(\frac{j-w-k^{\*}+\beta(T-t)}{\sqrt{T-t}}\right) |  | (83) |
|  |  |  | −(β−α)e−β​(j−w)N(j−w−k∗−β​(T−t)T−t)].\displaystyle\qquad\qquad-(\beta-\alpha)e^{-\beta(j-w)}N\left(\frac{j-w-k^{\*}-\beta(T-t)}{\sqrt{T-t}}\right)\bigg{]}\,. |  |

In the special case when L=F0𝐿subscript𝐹0L=F\_{0}, the DIC option reduces to a vanilla call with a price of

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Ct​(K,T)subscript𝐶𝑡𝐾𝑇\displaystyle C\_{t}(K,T) | =\displaystyle= | F0∫−∞0djeα​j[(β+α)eβ​(j−w)N(j−w−k∗+β​(T−t)T−t)\displaystyle F\_{0}\int\_{-\infty}^{0}dje^{\alpha j}\bigg{[}(\beta+\alpha)e^{\beta(j-w)}N\left(\frac{j-w-k^{\*}+\beta(T-t)}{\sqrt{T-t}}\right) |  | (84) |
|  |  |  | −(β−α)e−β​(j−w)N(j−w−k∗−β​(T−t)T−t)],\displaystyle\quad\quad-(\beta-\alpha)e^{-\beta(j-w)}N\left(\frac{j-w-k^{\*}-\beta(T-t)}{\sqrt{T-t}}\right)\bigg{]}\,, |  |

which completes the pricing of a DIC option on Eqn ([50](#S3.E50 "In 3.2 Constructing a Non-Negative Martingale via Jump to Default ‣ 3 Constructing a 3 Parameter Non-Negative Continuous Martingale")). For a DIC option on spot price, Eqn ([79](#S4.E79 "In 4.3 Vanilla and Down-and-In Call ‣ 4 Application in Option Pricing")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | DICtSpot​(L,K,T)=𝟙F¯t≤L⋅CtFX​Spot​(K,T)+𝟙F¯t>L⋅Et​[𝟙F¯T≤L​(FT−K)+],subscriptsuperscriptDICSpot𝑡𝐿𝐾𝑇⋅subscript1subscript¯𝐹𝑡𝐿subscriptsuperscript𝐶FXSpot𝑡𝐾𝑇⋅subscript1subscript¯𝐹𝑡𝐿subscript𝐸𝑡delimited-[]subscript1subscript¯𝐹𝑇𝐿superscriptsubscript𝐹𝑇𝐾{\rm{DIC}}^{\rm{Spot}}\_{t}(L,K,T)=\mathbbm{1}\_{\underline{F}\_{t}\leq L}\cdot C^{\rm{FX\,\,Spot}}\_{t}(K,T)+\mathbbm{1}\_{\underline{F}\_{t}>L}\cdot E\_{t}\left[\mathbbm{1}\_{\underline{F}\_{T}\leq L}(F\_{T}-K)^{+}\right]\,, |  | (85) |

which leads to slight modification on both Eqn ([83](#S4.E83 "In 4.3 Vanilla and Down-and-In Call ‣ 4 Application in Option Pricing")) and Eqn ([84](#S4.E84 "In 4.3 Vanilla and Down-and-In Call ‣ 4 Application in Option Pricing")), and the results are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | DICtSpot​(L,K,T)subscriptsuperscriptDICSpot𝑡𝐿𝐾𝑇\displaystyle{\rm{DIC}}^{\rm{Spot}}\_{t}(L,K,T) | =\displaystyle= | 𝟙F¯t≤L​CtSpot​(K,T)subscript1subscript¯𝐹𝑡𝐿subscriptsuperscript𝐶Spot𝑡𝐾𝑇\displaystyle\mathbbm{1}\_{\underline{F}\_{t}\leq L}C^{\rm{Spot}}\_{t}(K,T) |  |
|  |  | +\displaystyle+ | 𝟙F¯t>LF0eβ2​(T−t)2∫−∞1α​ln⁡LF0djeα​j[(β+α)eβ​(j−w)N(j−w−k∗+β​(T−t)T−t)\displaystyle\mathbbm{1}\_{\underline{F}\_{t}>L}F\_{0}e^{\frac{\beta^{2}(T-t)}{2}}\int\_{-\infty}^{\frac{1}{\alpha}\ln{\frac{L}{F\_{0}}}}dje^{\alpha j}\bigg{[}(\beta+\alpha)e^{\beta(j-w)}N\left(\frac{j-w-k^{\*}+\beta(T-t)}{\sqrt{T-t}}\right) |  |
|  |  |  | −(β−α)e−β​(j−w)N(j−w−k∗−β​(T−t)T−t)],\displaystyle\qquad\qquad-(\beta-\alpha)e^{-\beta(j-w)}N\left(\frac{j-w-k^{\*}-\beta(T-t)}{\sqrt{T-t}}\right)\bigg{]}\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | CtSpot​(K,T)subscriptsuperscript𝐶Spot𝑡𝐾𝑇\displaystyle C^{\rm{Spot}}\_{t}(K,T) | =\displaystyle= | F0eβ2​(T−t)2∫−∞0djeα​j[(β+α)eβ​(j−w)N(j−w−k∗+β​(T−t)T−t)\displaystyle F\_{0}e^{\frac{\beta^{2}(T-t)}{2}}\int\_{-\infty}^{0}dje^{\alpha j}\bigg{[}(\beta+\alpha)e^{\beta(j-w)}N\left(\frac{j-w-k^{\*}+\beta(T-t)}{\sqrt{T-t}}\right) |  | (86) |
|  |  |  | −(β−α)e−β​(j−w)N(j−w−k∗−β​(T−t)T−t)].\displaystyle\quad\quad-(\beta-\alpha)e^{-\beta(j-w)}N\left(\frac{j-w-k^{\*}-\beta(T-t)}{\sqrt{T-t}}\right)\bigg{]}\,. |  |

Before closing this section, we would like to point out that Eqn ([83](#S4.E83 "In 4.3 Vanilla and Down-and-In Call ‣ 4 Application in Option Pricing")) is related to several options. For instance, when α=1𝛼1\alpha=1 and β=0𝛽0\beta=0 the result reduces to that in [[2](#bib.bib2)]. In the special case of a zero strike DIC option (K=0𝐾0K=0), Eqn ([83](#S4.E83 "In 4.3 Vanilla and Down-and-In Call ‣ 4 Application in Option Pricing")) has closed form expressions:

|  |  |  |
| --- | --- | --- |
|  | DICt(L,0,T)=F0[(LF0)α+βe−β​wN(1α​ln⁡LF0−w+β​(T−t)T−t)\displaystyle DIC\_{t}(L,0,T)=F\_{0}\bigg{[}\left(\frac{L}{F\_{0}}\right)^{\alpha+\beta}e^{-\beta w}N\left(\frac{\frac{1}{\alpha}\ln\frac{L}{F\_{0}}-w+\beta(T-t)}{\sqrt{T-t}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −2eα​w+(α2−β2)​(T−t)2N(1α​ln⁡LF0−w−α​(T−t)T−t)+(LF0)α−βeβ​wN(1α​ln⁡LF0−w−β​(T−t)T−t)].\displaystyle\quad\quad-2e^{\alpha w+\frac{(\alpha^{2}-\beta^{2})(T-t)}{2}}N\left(\frac{\frac{1}{\alpha}\ln\frac{L}{F\_{0}}-w-\alpha(T-t)}{\sqrt{T-t}}\right)+\left(\frac{L}{F\_{0}}\right)^{\alpha-\beta}e^{\beta w}N\left(\frac{\frac{1}{\alpha}\ln\frac{L}{F\_{0}}-w-\beta(T-t)}{\sqrt{T-t}}\right)\bigg{]}. |  | (87) |

## 5 Summary and Extensions

We proposed a three parameter continuous martingale
with state space [0,∞)0[0,\infty). This is done by first generating a process with a positive drift driven by the running minimum and drawup of a Brownian motion in the Azéma-Yor setting, and adding a jump to default process.
The process generalizes driftless Geometric Brownian motion by adding two more parameters
while preserving its tractability. In particular, its running minimum and drawup rate (the ratio between level and running minimum) are both analytically tractable.
The three model parameters
α,γ

𝛼𝛾\alpha,\gamma, and β𝛽\beta
can be respectively interpreted as the instantaneous volatility
of the underlying at each new low,
at the initial time, and at infinitely high prices of the underlying.
The parameter α𝛼\alpha controls the implied volatility at
low strikes, while the parameter β𝛽\beta controls the implied volatility at
high strikes.
So long as implied volatility is monotonic in strike price,
the parameter γ𝛾\gamma can be used to meet an at-the-money implied
volatility. It is shown that in certain limits, this new process can reduce to Geometric Brownian motion and the positive martingale given in [[2](#bib.bib2)]. We also presented the bivariate transition PDF of the process’ running minimum and drawup rate. By utilizing the transition PDF, we priced several options assuming the dynamics are driven by the three parameter martingale in risk neutral measure. The options include a one-touch option with a lower barrier, lookback options with floating and fixed strike prices, vanilla call and a down-and-in call option.

Since not all implied volatility slices are monotonic,
future research should be directed towards
extending the model by introducing either stochastic volatility or jumps.
One can also use the process without jump to default to model dynamics that involve a positive drift, for instance, the cumulative return of an investment strategy.
Moreover, Girsanov’s theorem can be used to remove the drift of G𝐺G,
at which point a reflection principle becomes available.
In the interests of brevity, these extensions are best left for future research.

## Acknowledgement

We are grateful to Matthew Lorig, Vasily Strela, Jane Yu, and especially
Travis Fisher,
for their comments.
They are not responsible for any errors.

## Appendix

### 1. More about eβ−αβ​xsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼e^{\beta x}\_{\beta-\alpha}

This technical appendix proves the result ([6](#S2.E6 "In 2 Two Parameter Exponential Function")).
For x≥0𝑥0x\geq 0, α≥0𝛼0\alpha\geq 0, and β>0𝛽0\beta>0,
our two parameter exponential function
is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eα−ββ​x≡α+β2​β​eβ​x+α−β2​β​e−β​x.subscriptsuperscript𝑒𝛽𝑥𝛼𝛽𝛼𝛽2𝛽superscript𝑒𝛽𝑥𝛼𝛽2𝛽superscript𝑒𝛽𝑥e^{\beta x}\_{\alpha-\beta}\equiv\frac{\alpha+\beta}{2\beta}e^{\beta x}+\frac{\alpha-\beta}{2\beta}e^{-\beta x}. |  | (88) |

Squaring this result implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (eα−ββ​x)2=(α+β2​β)2​e2​β​x+α2−β22​β2+(α−β2​β)2​e−2​β​x.superscriptsubscriptsuperscript𝑒𝛽𝑥𝛼𝛽2superscript𝛼𝛽2𝛽2superscript𝑒2𝛽𝑥superscript𝛼2superscript𝛽22superscript𝛽2superscript𝛼𝛽2𝛽2superscript𝑒2𝛽𝑥\left(e^{\beta x}\_{\alpha-\beta}\right)^{2}=\left(\frac{\alpha+\beta}{2\beta}\right)^{2}e^{2\beta x}+\frac{\alpha^{2}-\beta^{2}}{2\beta^{2}}+\left(\frac{\alpha-\beta}{2\beta}\right)^{2}e^{-2\beta x}. |  | (89) |

Consider the cohort of ([88](#Sx2.E88 "In 1. More about 𝑒^{𝛽⁢𝑥}_{𝛽-𝛼} ‣ Appendix")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ−αβ​x≡α+β2​β​eβ​x+β−α2​β​e−β​x.subscriptsuperscript𝑒𝛽𝑥𝛽𝛼𝛼𝛽2𝛽superscript𝑒𝛽𝑥𝛽𝛼2𝛽superscript𝑒𝛽𝑥e^{\beta x}\_{\beta-\alpha}\equiv\frac{\alpha+\beta}{2\beta}e^{\beta x}+\frac{\beta-\alpha}{2\beta}e^{-\beta x}. |  | (90) |

Squaring this cohort implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (eβ−αβ​x)2=(α+β2​β)2​e2​β​x−α2−β22​β2+(α−β2​β)2​e−2​β​x.superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2superscript𝛼𝛽2𝛽2superscript𝑒2𝛽𝑥superscript𝛼2superscript𝛽22superscript𝛽2superscript𝛼𝛽2𝛽2superscript𝑒2𝛽𝑥\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}=\left(\frac{\alpha+\beta}{2\beta}\right)^{2}e^{2\beta x}-\frac{\alpha^{2}-\beta^{2}}{2\beta^{2}}+\left(\frac{\alpha-\beta}{2\beta}\right)^{2}e^{-2\beta x}. |  | (91) |

Subtracting ([91](#Sx2.E91 "In 1. More about 𝑒^{𝛽⁢𝑥}_{𝛽-𝛼} ‣ Appendix")) from ([89](#Sx2.E89 "In 1. More about 𝑒^{𝛽⁢𝑥}_{𝛽-𝛼} ‣ Appendix")) implies that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (eα−ββ​x)2−(eβ−αβ​x)2=α2−β2β2.superscriptsubscriptsuperscript𝑒𝛽𝑥𝛼𝛽2superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2superscript𝛼2superscript𝛽2superscript𝛽2\left(e^{\beta x}\_{\alpha-\beta}\right)^{2}-\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}=\frac{\alpha^{2}-\beta^{2}}{\beta^{2}}. |  | (92) |

Taking the positive square root of each side leads to the desired result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eα−ββ​x=(eβ−αβ​x)2+α2−β2β2.subscriptsuperscript𝑒𝛽𝑥𝛼𝛽superscriptsubscriptsuperscript𝑒𝛽𝑥𝛽𝛼2superscript𝛼2superscript𝛽2superscript𝛽2e^{\beta x}\_{\alpha-\beta}=\sqrt{\left(e^{\beta x}\_{\beta-\alpha}\right)^{2}+\frac{\alpha^{2}-\beta^{2}}{\beta^{2}}}. |  | (93) |

## References

* [1]
   Black, F., 1976,
  “The Pricing of Commodity Contracts”,
  Journal of Financial Economics,
  3, 167–179.
* [2]
   Carr P., 2014, “First Order Calculus and Option Pricing”,
  Journal of Financial Engineering 1, 1.
* [3]
   Guyon, J., 2014, “Path-Dependent Volatility”, Risk,
  10.
* [4]
   Hobson, D. G. and L. C. G. Rogers, 1998,
  “Complete Models with Stochastic Volatility”,
  Mathematical Finance, 8, 27- 48.
* [5]
   Merton, R.C., 1976, “Option pricing when underlying
  stock returns are discontinuous”, Journal of Financial
  Economics, 3, 125- 144.
* [6]
   Grabbe, J.O., 1983, “The pricing of call and put options on foreign exchange”, Journal of International Money and Finance, 2, 239- 253.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/1809.02245)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1809.02245)
[View original  
on arXiv](https://arxiv.org/abs/1809.02245)[►](javascript: void(0))