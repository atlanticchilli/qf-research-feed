---
authors:
- Mikhail Gennadievich Belov
- Victor Victorovich Dubov
- Vadim Konstantinovich Ivanov
- Alexander Yurievich Maslov
- Olga Vladimirovna Proshina
- Vladislav Gennadievich Malyshkin
doc_id: arxiv:2511.01471v1
family_id: arxiv:2511.01471
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Trade Execution Flow as the Underlying Source of Market Dynamics
url_abs: http://arxiv.org/abs/2511.01471v1
url_html: https://arxiv.org/html/2511.01471v1
venue: arXiv q-fin
version: 1
year: 2025
---


Mikhail Gennadievich Belov
[mikhail.belov@tafs.pro](mailto:mikhail.belov@tafs.pro)
Lomonosov Moscow State University, Faculty of Mechanics and Mathematics,
GSP-1, Moscow, Vorob’evy Gory, 119991, Russia
Autretech Group, Skolkovo Innovation Center, Nobel Street, Building 7, Moscow, 121205, Russia
  
Victor Victorovich Dubov
[dubov@spbstu.ru](mailto:dubov@spbstu.ru)
Peter the Great St. Petersburg Polytechnic University, 195251, Russia
  
Vadim Konstantinovich Ivanov 
[ivvadim@rambler.ru](mailto:ivvadim@rambler.ru)
Peter the Great St. Petersburg Polytechnic University, 195251, Russia
  
Alexander Yurievich Maslov 
[maslov.ton@mail.ioffe.ru](mailto:maslov.ton@mail.ioffe.ru)
Ioffe Institute, Politekhnicheskaya 26, St Petersburg, 194021, Russia
  
Olga Vladimirovna Proshina
[proshina.ton@mail.ioffe.ru](mailto:proshina.ton@mail.ioffe.ru)
Ioffe Institute, Politekhnicheskaya 26, St Petersburg, 194021, Russia
  
Vladislav Gennadievich Malyshkin 
[malyshki@ton.ioffe.ru](mailto:malyshki@ton.ioffe.ru)
Ioffe Institute, Politekhnicheskaya 26, St Petersburg, 194021, Russia

(June, 6, 2024)

###### Abstract

```
$Id: ExecutionFlow.tex,v 1.120 2025/11/03 10:34:43 mal Exp $
```

In this work, we demonstrate experimentally that the execution flow, I=d​V/d​tI=dV/dt, is the fundamental driving force of market dynamics.
We develop a numerical framework to calculate execution flow from sampled moments using the Radon-Nikodym derivative. A notable feature of this approach is its ability to automatically determine thresholds that can serve as actionable triggers.
The technique also determines the characteristic time scale directly from the corresponding eigenproblem.
The methodology has been validated on actual market data to support these findings.
Additionally, we introduce a framework based on the Christoffel function spectrum, which is invariant under arbitrary
non-degenerate linear transformations of input attributes and offers an alternative
to traditional principal component analysis (PCA), which is limited to unitary invariance.

††preprint: V.M.

## I Introduction

Modern financial markets display complex dynamics arising from internal and external factors,
and from stochastic (or deterministic) processes not linked to any identifiable cause.
Since Aristotle [[1](https://arxiv.org/html/2511.01471v1#bib.bib1)], this has been a fascinating topic of study, particularly price formation.
Price formation driven by market microstructure is the focus of this paper.
Most interestingly, the tâtonnement process [[2](https://arxiv.org/html/2511.01471v1#bib.bib2)],
used as a means to observe supply and demand curves, misses the entire aspect of market dynamics [[3](https://arxiv.org/html/2511.01471v1#bib.bib3)].

Modern financial markets generate a diverse array of information, including prices, execution volumes across different time scales, limit order book (LOB) data from exchanges, corporate financial reports, sovereign economic indicators, central bank actions, and more.
The accessibility, structure, time scale, and impact of this information on market behavior vary significantly.

In [[4](https://arxiv.org/html/2511.01471v1#bib.bib4)], we formulated the ultimate market dynamics problem:
to find evidence of the existence (or proof of the non-existence)
of an automated trading machine that consistently generates positive P&L in a free market as an autonomous agent.
In [[5](https://arxiv.org/html/2511.01471v1#bib.bib5)], we formulated the problem in weak and strong forms:

* •

  Weak form: Whether such an automated trading machine can exist at all using only legally available data.
  (It can certainly exist in an illegal form—for example, when a brokerage uses client order flow information to
  [frontrun](https://en.wikipedia.org/wiki/Front_running)
  their own clients. Such strategies typically rely on proprietary information about clients’ future supply-demand imbalances and on subsequent monetization of this information.)
* •

  Strong form: Whether such an automated trading machine can exist based solely on transaction sequences —
  for instance, the historical time series of market observation triples: (time, execution price, shares traded).
  In this information, supply and demand are matched for every observation: at time tt, trader AA sold vv
  shares of a security at price PP to trader BB and received v​PvP dollars.
  Such a strategy can utilize only information about volume and execution flows.

In this paper, we focus on determining information about the future solely from a sequence of past execution triples:
(time,execution price,shares traded).
The main result of our previous works [[6](https://arxiv.org/html/2511.01471v1#bib.bib6), [7](https://arxiv.org/html/2511.01471v1#bib.bib7)]
is that it is the share execution flow I=d​V/d​tI=dV/dt,
rather than the share trading volume VV,
that drives the market (see Figs. 2 and 3 of Ref. [[7](https://arxiv.org/html/2511.01471v1#bib.bib7)]: the asset price exhibits singularities at high II,
whereas no price singularity occurs at the maximal volume price – the median of the price-volume distribution).
In other words, it is the execution flow I=d​V/d​tI=dV/dt, not the traded volume, that drives the market.
This perspective differs significantly from the commonly studied[[8](https://arxiv.org/html/2511.01471v1#bib.bib8)] concept
of [market impact](https://en.wikipedia.org/wiki/Market_impact#Market_impact_cost).
The situation is analogous to the difference between Newtonian and Aristotelian dynamics:
force causes acceleration vs force causes velocity.

In this paper, we investigate market microstructure using trading data with sub-microsecond temporal resolution.
Previous research initiatives – beginning with the Penn-Lehman Automated Trading (PLAT) project [[9](https://arxiv.org/html/2511.01471v1#bib.bib9)]
and followed by others [[10](https://arxiv.org/html/2511.01471v1#bib.bib10), [11](https://arxiv.org/html/2511.01471v1#bib.bib11)] among many others –
have explored the performance characteristics of a variety of automated trading systems.
While our group has previously conducted high-frequency trading (HFT) on NASDAQ,
the present study focuses primarily on market microstructure analysis,
emphasizing execution flow as the fundamental driving mechanism of market dynamics.
The principal contributions of this work are as follows:

1. 1.

   Development of a fast and numerically stable method for moment calculation (Section [II](https://arxiv.org/html/2511.01471v1#S2 "II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
2. 2.

   Application of this method to real exchange data (Section [III](https://arxiv.org/html/2511.01471v1#S3 "III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
3. 3.

   Development of an execution flow estimation methodology (Section [IV](https://arxiv.org/html/2511.01471v1#S4 "IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
   and experimental evidence linking execution flow singularities to price singularities.
   The most important result is the automatic determination of the characteristic time scale from the corresponding eigenproblem.
4. 4.

   Derivation of a procedure for converting execution flow fluctuations into probabilistic forecasts of price changes (Sections [V](https://arxiv.org/html/2511.01471v1#S5 "V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics") and [VI](https://arxiv.org/html/2511.01471v1#S6 "VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
5. 5.

   Empirical comparison of the derived directional information with observed market behavior (Section [VII](https://arxiv.org/html/2511.01471v1#S7 "VII Directional Information: A Practical Demonstration ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

Additionally, we propose a framework based on the Christoffel function spectrum
for determining probability contribution components (Appendix [C](https://arxiv.org/html/2511.01471v1#A3 "Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
which is invariant under arbitrary non-degenerate transformations of input attributes.
This invariance property provides a significant advantage over conventional principal component analysis (PCA),
which is limited to unitary invariance.

This paper is accompanied by a software which
[is available](http://www.ioffe.ru/LNEPS/malyshkin/code_polynomials_quadratures.zip)
from Ref. [[12](https://arxiv.org/html/2511.01471v1#bib.bib12)];
all references to code in the paper correspond to this software.
A detailed description of its usage is provided in Appendix [D](https://arxiv.org/html/2511.01471v1#A4 "Appendix D Software Usage Description ‣ Trade Execution Flow as the Underlying Source of Market Dynamics").

## II Moment Calculation from Empirical Samples

Having established the role of the execution flow I=d​V/d​tI=dV/dt,
we now formulate a method for its calculation.
For a given time series tl,flt\_{l},f\_{l}, we introduce the moments
⟨Qj​f⟩\Braket{Q\_{j}f}
calculated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Qj​f⟩\displaystyle\Braket{Q\_{j}f} | =∫−∞tn​o​wQj​(x​(t))​f​(t)​ω​(t)​𝑑t\displaystyle=\int\limits\_{-\infty}^{t\_{now}}Q\_{j}(x(t))f(t)\omega(t)dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑lQj​(x​(tl))​fl​ω(l)​(tl−tl−1)\displaystyle=\sum\limits\_{l}Q\_{j}(x(t\_{l}))f\_{l}\,\omega^{(l)}(t\_{l}-t\_{l-1}) |  | (1) |

this sums the terms from the past till tn​o​wt\_{now}.
Here, x​(t)x(t) is a monotonic function; in this paper, we use either
x=(t−tn​o​w)/τx=(t-t\_{now})/\tau or x=exp⁡((t−tn​o​w)/τ)x=\exp((t-t\_{now})/\tau).
The function ω​(t)\omega(t)
is a decaying weight; in this paper, we consider only an exponential decay,
ω=exp⁡((t−tn​o​w)/τ)\omega=\exp((t-t\_{now})/\tau).
The function Qj​(x)Q\_{j}(x)
is a polynomial of degree jj.
One can simply use, for example, Qj​(x)=xjQ\_{j}(x)=x^{j},
but it is convenient to employ an arbitrary basis to improve numerical stability.
In this paper, we often use the basis of shifted Legendre polynomials:
Qj​(x​(t))=Pj​(2​exp⁡((t−tn​o​w)/τ)−1)Q\_{j}(x(t))=P\_{j}\left(2\exp((t-t\_{now})/\tau)-1\right),
where Pj​(x)P\_{j}(x)
denotes the Legendre polynomial of degree jj.
Equation ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is simply an exponential moving average of
Qj​(x​(t))​f​(t)Q\_{j}(x(t))f(t).
For example, a regular moving average price Pm​aP\_{ma}
and moving standard deviation σm​a\sigma\_{ma},
calculated from a sequence (tl,Pl)(t\_{l},P\_{l}), is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Pm​a​(tn​o​w)\displaystyle P\_{ma}(t\_{now}) | =⟨Q0​P⟩⟨Q0⟩\displaystyle=\frac{\Braket{Q\_{0}P}}{\Braket{Q\_{0}}} |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σm​a2​(tn​o​w)\displaystyle\sigma^{2}\_{ma}(t\_{now}) | =⟨Q0​P2⟩⟨Q0⟩−Pm​a2​(tn​o​w)\displaystyle=\frac{\Braket{Q\_{0}P^{2}}}{\Braket{Q\_{0}}}-P^{2}\_{ma}(t\_{now}) |  | (3) |

Equation ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) maps a long sequence of past observations tl,flt\_{l},f\_{l} to nn moments ⟨Qj​f⟩\Braket{Q\_{j}f},
with j=0​…​n−1j=0\dots n-1. The index jj captures contributions from different time scales.
If one chooses Qj​(x​(t))=exp⁡(i​j​t/τ)Q\_{j}(x(t))=\exp(i\,jt/\tau) and ω=1\omega=1,
the moments ⟨Qj​f⟩\Braket{Q\_{j}f} correspond essentially to Fourier amplitudes.
In this work, we adopt a decaying weight and an arbitrary basis Qj​(x)Q\_{j}(x)
to improve numerical stability and better capture the dynamics of interest.

Given a sequence of (time, execution price, shares traded) as (tl,Pl,vl)(t\_{l},P\_{l},v\_{l})111For convenience, we define vl=Vl−Vl−1v\_{l}=V\_{l}-V\_{l-1} as the number of shares traded at tlt\_{l},
where VlV\_{l} denotes the total volume traded at or before tlt\_{l}.
Consider all possible moments that can be calculated from such sequences.
They essentially differ only in the choice of integration variable in ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"));
instead of tl−tl−1t\_{l}-t\_{l-1}, one can use Pl−Pl−1P\_{l}-P\_{l-1} or Vl−Vl−1=vlV\_{l}-V\_{l-1}=v\_{l}.
Formally, consider, for example, I=d​V/d​t≈Vl−Vl−1tl−tl−1I=dV/dt\approx\frac{V\_{l}-V\_{l-1}}{t\_{l}-t\_{l-1}}.
The choice of integration variable allows us to calculate different rates.
We now list all the moments that can be calculated by direct sampling using the definition ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
with the following measures:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | d​t=tl−tl−1\displaystyle dt=t\_{l}-t\_{l-1} | for ⟨Pk​Qj⟩\Braket{P^{k}Q\_{j}} |  | (4a) |
|  | d​P=Pl−Pl−1\displaystyle dP=P\_{l}-P\_{l-1} | for ⟨Pk​Qj​d​Pd​t⟩\Braket{P^{k}Q\_{j}\frac{dP}{dt}}, ⟨Pk​Qj​V​d​Pd​t⟩\Braket{P^{k}Q\_{j}V\frac{dP}{dt}} |  | (4b) |
|  | d​V=Vl−Vl−1\displaystyle dV=V\_{l}-V\_{l-1} | for ⟨Pk​Qj​d​Vd​t⟩\Braket{P^{k}Q\_{j}\frac{dV}{dt}} |  | (4c) |

additionally, other moments, such as ⟨Pk​Qj​d​P​Vd​t⟩\Braket{P^{k}Q\_{j}\frac{dPV}{dt}}, can be obtained from these using integration by parts.

A fast, efficient, and numerically stable implementation of all these moment calculations in an arbitrary basis QjQ\_{j} is rather complex and has been discussed in [[6](https://arxiv.org/html/2511.01471v1#bib.bib6), [13](https://arxiv.org/html/2511.01471v1#bib.bib13)].
The implementation is available from [[12](https://arxiv.org/html/2511.01471v1#bib.bib12)]; see the classes
com/polytechnik/trading/{QVMDataM,QVMDataL,QVMDataP}.java
and
com/polytechnik/freemoney/{CommonlyUsedMomentsMonomials,CommonlyUsedMomentsLaguerre,CommonlyUsedMomentsLegendreShifted}.java for an implementation.

An alternative, though not fully rigorous, method of calculation that allows the use of additional measures beyond those in ([4](https://arxiv.org/html/2511.01471v1#S2.E4 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is the “secondary sampling” approach [[5](https://arxiv.org/html/2511.01471v1#bib.bib5)],
in which a calculated value at tlt\_{l} is treated in ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) as if it were a measured observation.
This enables the calculation of a new range of moments.
For example, in [[5](https://arxiv.org/html/2511.01471v1#bib.bib5)], the maximal eigenvalue of an eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) was used as an integration measure.

Note that all the measures in ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) allow us to calculate moments only of the first derivative,
such as I=d​V/d​tI=dV/dt, d​P/d​tdP/dt, and so on. Moments of second derivatives, such as d2​P/d​t2d^{2}P/dt^{2} or
d​I/d​t=d2​V/d​t2dI/dt=d^{2}V/dt^{2} (the latter being particularly important for our future considerations),
cannot be obtained from direct sampling.
We will discuss approaches for their calculation below.
For now, we assume that all necessary first-order derivative moments are calculable and present a few examples of useful calculations with them,
followed by a generalization toward a possible solution of the strong form of the ultimate market dynamics problem.

## III Available financial data and time scales

In this section, we discuss the available market data,
which can be regarded as a form of experimental data against which any theory should be tested.
We consider this topic important and therefore include a dedicated section on market data — more precisely,
on available trade execution data as a form of measured experimental evidence.
After that, we develop an efficient method for computing the moments from this data,
which arrive as a continuous stream of individual trades. Our theoretical framework is built upon these moments.

The transaction sequence data (tl,Pl,vl)(t\_{l},P\_{l},v\_{l}) is available across various markets and time scales —
from high-frequency exchange trading in liquid markets operating at sub-microsecond intervals,
to fixed-income over-the-counter markets with time scales of hours or even days,
and to real estate markets where transactions may take months to complete.
Derivatives, commodities, and emerging markets also exhibit their own specific characteristics.
In our approach, we require a liquid market with a large number of transactions and active participants.
The data must be of high quality and easily accessible at low or no cost.
For these reasons, the U.S. equities market is the natural first choice for applying our theory.

End-of-day market close data is freely available from numerous sources,
such as [Yahoo Finance](https://finance.yahoo.com/) and various data aggregators.
However, daily close data is insufficient for applying our theory.
The concept of execution flow maximization requires analysis at the level of individual transactions
as they occur in real time from market participants.
Moreover, the use of “daily close” data introduces an artificial time scale (one day),
which undermines the key strength of our approach —
the automatic selection of the relevant time scale based on the maximization of the execution flow.

The NASDAQ ITCH feed[[14](https://arxiv.org/html/2511.01471v1#bib.bib14)] provides LOB data and full lifecycle information for each order —
from its “add order” event to “cancel” or “execute”.
However, the daily traded volume on NASDAQ represents only a fraction of the total daily traded volume of the U.S.
equities market. Moreover, the primary value of this feed — the limit order book information —
has become much less significant. Since approximately 2008–2010,
exchange trading has become increasingly similar to dark pool trading.
The most typical LOB pattern is now[[4](https://arxiv.org/html/2511.01471v1#bib.bib4)] that an added order spends almost no time in the LOB;
it is either executed almost immediately or canceled.
Empirical observations show that over 90% of orders that reach the best price level at some point
are eventually canceled[[15](https://arxiv.org/html/2511.01471v1#bib.bib15), [6](https://arxiv.org/html/2511.01471v1#bib.bib6)].
The current exchange fee structure makes LOB cancellations very cheap,
creating a significant incentive for trading algorithms to submit orders for purposes other than actual execution.
Executed orders (trades) provide much more meaningful information,
since completing a round trip – buying and then selling an actual asset –
is considerably more costly and risky than simply adding and canceling orders in the LOB.

Moreover, current U.S. regulations require that all actual trades be published through the Consolidated Tape System (CTS),
which includes execution transactions from all exchanges and dark pools.
Historical tapes, known as daily TAQ (Trade and Quote), can be acquired from NYSE[[16](https://arxiv.org/html/2511.01471v1#bib.bib16)]
at a reasonable cost, or some free samples can be downloaded
from their website at <https://www.nyse.com/market-data/historical/daily-taq>.
A single daily TAQ file typically contains over 100 million execution transactions (lines)
and exceeds 10 GB in uncompressed size.
Across all tickers, the daily volume calculated from the daily TAQ files is slightly higher than
the value reported by Yahoo Finance and significantly larger than that computed from the NASDAQ ITCH daily file.

In this paper, we primarily use data from NYSE daily TAQ.
For the purpose of comparison with our previous works,
we also use data from Nasdaq ITCH for September 20, 2012.
This date was selected in [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)] for a simple reason:
the market exhibited a bear trend before 10:00 and a bull trend with high volatility afterward.
Such market behavior often leads to significant losses for automated trading machines.

For the purpose of testing, this market data can be viewed as a large file with lines of the form:

```
NVDA    31556271038450  156.26    3
TSLA    31556274115189  298.7     109
TQQQ    31556285245282  81.88     5
TQQQ    31556335367235  81.8899   5
PLTR    31556335813084  135.48    2
TSLA    31556519786918  298.675   1
NVDA    31556540197765  156.27    1
TSLA    31556542897531  298.6981  3
AAPL    31556561439699  207.2099  6
TSLA    31556591750551  298.7     20
TSLA    31556595205403  298.7     5
PLTR    31556602938660  135.48    5
TSLA    31556640789406  298.7     45
```

Each line contains the ticker, execution time (in nanoseconds since midnight), execution price, and the number of shares traded.
Such a file can be readily computed from NASDAQ ITCH or NYSE daily TAQ, see Appendix [D](https://arxiv.org/html/2511.01471v1#A4 "Appendix D Software Usage Description ‣ Trade Execution Flow as the Underlying Source of Market Dynamics") below.
The strong form of the ultimate market dynamics problem is equivalent to the existence of a stream processor
(possibly with an internal state) that reads such a file line-by-line, updates its internal state,
and posts trades that consistently result in a positive P&L.
As emphasized earlier [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)], the price prediction problem is distinct from P&L prediction;
we will discuss this difference below.
For now, let us note that all moments of the form ([4](https://arxiv.org/html/2511.01471v1#S2.E4 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) can be efficiently calculated from such a stream using an incremental recurrent update and a Newton-binomial type expansion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qj​(a​x+b)=∑k=0jck​Qk​(x)\displaystyle Q\_{j}(ax+b)=\sum\_{k=0}^{j}c\_{k}Q\_{k}(x) |  | (5) |

This generalizes the familiar expression (1+x)j=∑k=0jCjk​xk(1+x)^{j}=\sum\_{k=0}^{j}C\_{j}^{k}x^{k} to an arbitrary polynomial basis QjQ\_{j}.
The exponential weight ω=exp⁡((t−tn​o​w)/τ)\omega=\exp((t-t\_{now})/\tau) makes this calculation straightforward;
if a fixed-window weight function were used, the recurrent calculations would become problematic.

![Refer to caption](x1.png)


Figure 1: 
An example of regular exponential moving average
corresponding to τ=128\tau=128s and τ=512\tau=512s.
Standard deviation is also calculated with the same τ\tau and
moving average ±\pm standard deviation is plotted as a thin line in the same color.
As τ\tau increases – the moving average “shifts to the right”
(τ\tau-proportional time delay, lagging indicator).
The data is for AAPL stock on September, 20, 2012.

Let us provide a simple demonstration. Assume we have obtained three moments:
⟨Q0​I⟩\Braket{Q\_{0}I}, ⟨P​Q0​I⟩\Braket{PQ\_{0}I}, and ⟨P2​Q0​I⟩\Braket{P^{2}Q\_{0}I}.
Since Q0Q\_{0} is constant, these correspond (up to a constant factor)
to volume-weighted (I=d​V/d​tI=dV/dt) P0P^{0}, P1P^{1}, and P2P^{2}, respectively.
The moments ⟨Q0⟩\Braket{Q\_{0}}, ⟨P​Q0⟩\Braket{PQ\_{0}}, and ⟨P2​Q0⟩\Braket{P^{2}Q\_{0}}
represent time-weighted P0P^{0}, P1P^{1}, and P2P^{2}.
Using any of these moments, one can construct a moving average ([2](https://arxiv.org/html/2511.01471v1#S2.E2 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
and a moving standard deviation ([3](https://arxiv.org/html/2511.01471v1#S2.E3 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
In Fig. [1](https://arxiv.org/html/2511.01471v1#S3.F1 "Figure 1 ‣ III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"), two volume-weighted moving averages are calculated for τ=128\tau=128s and τ=512\tau=512s.
The time-weighted moving average would be slightly smoother than the volume-weighted version.
The xx-coordinate, consistent with our previous works, is expressed as a decimal fraction of an hour;
for example, 9.759.75 in plot corresponds to 9:45 am. A ±\pm single moving standard deviation is also shown in the plot.
As expected, the moving average is delayed (shifted to the right) by a time scale proportional to τ\tau
relative to the actual price, making it a lagging indicator.
When the input data undergoes a qualitative regime change, it takes a τ\tau-proportional lag for the moving average to reflect this transition.
Some popular trading strategies use events when the price crosses its moving average as triggers for action.
In [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)], we discuss the shortcomings of such approaches when operating on a single time scale.

As a demonstration, let us present another perspective on the meaning of the moving average.
Consider not 33, but 2​n+12n+1 moments ⟨Pk​I⟩\Braket{P^{k}I}, with k=0​…​2​nk=0\dots 2n.
Now consider the problem of constructing a polynomial of degree nn
that satisfies the optimization problem of minimizing the square
of the polynomial with respect to the measure ⟨⋅⟩\Braket{\cdot}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(Pn+an−1​Pn−1+an−2​Pn−2+⋯+a0)2​I⟩→min\displaystyle\Braket{\left(P^{n}+a\_{n-1}P^{n-1}+a\_{n-2}P^{n-2}+\dots+a\_{0}\right)^{2}I}\to\min |  | (6) |

The solution yields an orthogonal polynomial of degree nn constructed with respect to the given measure.
The roots of this polynomial can be found by solving the following generalized eigenproblem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑k=0n−1⟨Pj|P​I|Pk⟩​αk[i]\displaystyle\sum\limits\_{k=0}^{n-1}\Braket{P^{j}|PI|P^{k}}\alpha\_{k}^{[i]} | =π[i]​∑k=0n−1⟨Pj|I|Pk⟩​αk[i]\displaystyle=\pi^{[i]}\sum\limits\_{k=0}^{n-1}\Braket{P^{j}|I|P^{k}}\alpha\_{k}^{[i]} |  | (7) |

Here we have changed the notation to Paul Dirac [bra–ket notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation),
a form that will be very useful below. For real matrices, we simply have
⟨Pj|P​I|Pk⟩=⟨Pj+k+1​I⟩\Braket{P^{j}|PI|P^{k}}=\Braket{P^{j+k+1}I}, and ⟨Pj|I|Pk⟩=⟨Pj+k​I⟩\Braket{P^{j}|I|P^{k}}=\Braket{P^{j+k}I}.
As long as the right-hand side matrix ⟨Pj|I|Pk⟩\Braket{P^{j}|I|P^{k}} is positively definite, the problem has nn solutions.
The nn eigenvalues π[i]\pi^{[i]} of the eigenproblem ([7](https://arxiv.org/html/2511.01471v1#S3.E7 "In III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
correspond to the nn roots of the degree-nn polynomial defined in ([6](https://arxiv.org/html/2511.01471v1#S3.E6 "In III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The roots π[i]\pi^{[i]} correspond to the Gaussian quadrature nodes
that interpolate the measure used to construct the polynomial with an nn-point discrete measure.
The corresponding weights w[i]w^{[i]} can be obtained from the eigenvectors α[i]\alpha^{[i]}
by evaluating them at corresponding π[i]\pi^{[i]};
alternatively, they can be determined from the Christoffel function. The sum of all weights w[i]w^{[i]} equals ⟨I⟩\Braket{I}.
This is a common method for constructing
orthogonal polynomials from a given measure[[17](https://arxiv.org/html/2511.01471v1#bib.bib17)] and for finding their roots along with the corresponding measure weights.

![Refer to caption](x2.png)


Figure 2: 
An example of a higher-order orthogonal polynomial root calculated from the moments
⟨Pk​I⟩\Braket{P^{k}I}, k=0​…​2​nk=0\dots 2n, is shown for n=7n=7.
Seven roots are obtained, with a substantial volume expected to be traded at each corresponding price level.
In this example, the actual measure is approximated by a discrete measure with n=7n=7 support points.
The figure is reproduced from [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)].

One can note that the moving average ([2](https://arxiv.org/html/2511.01471v1#S2.E2 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) corresponds to the root of an orthogonal polynomial of degree n=1n=1, which has a single root;
the corresponding weight for this node is ⟨I⟩\Braket{I}.
Given a sufficient number of moments ⟨Pk​I⟩\Braket{P^{k}I},
which can be calculated from the market data as above,
one can construct higher-order polynomials and determine their roots.
A demonstration from Ref. [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)] is shown in Fig. [2](https://arxiv.org/html/2511.01471v1#S3.F2 "Figure 2 ‣ III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics") of this paper for n=7n=7 roots of a polynomial calculated from the moments ⟨Pk​I⟩\Braket{P^{k}I}, k=0​…​2​nk=0\dots 2n with τ=128​s\tau=128\mathrm{s}.
These roots serve as the nodes of a Gaussian quadrature,
which approximates the measure used to construct the orthogonal polynomial with a discrete measure at nn support points.
A quadrature with n=1n=1 corresponds to a moving average,
while a quadrature with n=2n=2 (two nodes) provides not only the average
but also allows the estimation of the distribution’s median and skewness.
This is an example of constructing orthogonal polynomials for a single asset.

For multiple assets (assuming the price phase space is relatively stable),
such an approach is not directly applicable.
A possible alternative is to construct the Christoffel function in the price space of several assets,
in a manner similar to that described in Appendix [C](https://arxiv.org/html/2511.01471v1#A3 "Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics").
For a full basis, this approach provides an analogue of the joint price distribution;
selecting a few states with large coverage could potentially create a predictive model (provided the distribution is stable).
However, this approach – similar to an orthogonal polynomial model – is not dynamic;
it is more akin to returning to frequently visited points in the phase space.

These demonstrations are simple examples illustrating the potential use of a large number of moments.
While they operate on prices and generate charts, they do not directly convey information about market dynamics.
Nevertheless, the availability of a large number of sampled moments is valuable,
as it allows us to formulate and solve generalized eigenproblems, such as ([7](https://arxiv.org/html/2511.01471v1#S3.E7 "In III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
This specific eigenproblem primarily serves to plot informative charts
that highlight the price levels at which substantial trading occurred in the past.
A useful application of this orthogonal polynomial technique for market practitioners is as follows.
Instead of relying on the commonly used symmetric plots Pm​a±σm​aP\_{ma}\pm\sigma\_{ma} to determine action thresholds,
a substantially better approach is to construct an orthogonal polynomial of degree 22 or 33
and monitor the crossing of the current last price with the minimum or maximum roots π[i]\pi^{[i]} of the polynomial.
These roots correspond to the support points of trading volume and can capture distribution asymmetry
and other relevant factors, providing a more informative basis for trading decisions.
However, our aim is far more ambitious — understanding market dynamics —
and this example was presented solely to illustrate the eigenproblem technique that we actively employ in the subsequent analysis.

## IV Execution Flow: Calculation and Methodology

Execution flow I=d​V/d​tI=dV/dt, the number of shares traded per unit time,
is a positive quantity — a ratio of two measures ω​d​V\omega dV and ω​d​t\omega dt — and can be considered
as their Radon–Nikodym derivative. To calculate its value at a specific
point xx, a number of approaches can be applied, from direct interval sampling
to a ratio of localized states[[6](https://arxiv.org/html/2511.01471v1#bib.bib6)]. Formally, even a least-squares
approach can be applied to interpolate d​V/d​tdV/dt, for example,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⟨(I−∑j=0n−1βj​Qj​(x))2⟩→min\displaystyle\hskip-30.00005pt\Braket{\left(I-\sum\_{j=0}^{n-1}\beta\_{j}Q\_{j}(x)\right)^{2}}\to\min |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | IL​S​(x)\displaystyle I\_{LS}(x) | =∑j,k=0n−1Qj​(x)​Gj​k−1​⟨Qk​I⟩\displaystyle=\sum\limits\_{j,k=0}^{n-1}Q\_{j}(x)G^{-1}\_{jk}\Braket{Q\_{k}I} |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gj​k\displaystyle G\_{jk} | =⟨Qj|Qk⟩\displaystyle=\Braket{Q\_{j}|Q\_{k}} |  | (10) |

where G−1G^{-1} is the inverse of the Gram matrix ([10](https://arxiv.org/html/2511.01471v1#S4.E10 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
This expansion uses nn moments ⟨Qk​I⟩\Braket{Q\_{k}I} and 2​n−12n-1 moments ⟨Qk⟩\Braket{Q\_{k}} to compute.
This approach does not preserve the internal structure of the execution flow (for example, its inherently positive sign)
and does not incorporate the full past history in a way that allows determining thresholds,
such as whether the execution flow at tn​o​wt\_{now} is small or large.
Moreover, expanding the highly fluctuating d​V/d​tdV/dt, which varies by many orders of magnitude,
in a polynomial basis discards the critical information contained in its spikes.

We need a general method to account for highly fluctuating values over the polynomial moments.
The idea is to interpolate not the observed value II, but the probability density.
Consider a function ψ​(x)=∑j=0n−1αj​Qj​(x)\psi(x)=\sum\_{j=0}^{n-1}\alpha\_{j}Q\_{j}(x) that defines the density ψ2​(x​(t))​ω​(t)​d​t\psi^{2}(x(t))\omega(t)dt,
and a value expressed as a ratio of two measures, such as I=d​V/d​tI=dV/dt.
The value of II corresponding to a given state ψ​(x)\psi(x) can then be estimated as measures ratio

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Iψ\displaystyle I\_{\psi} | =⟨ψ|I|ψ⟩⟨ψ|ψ⟩=∑j,k=0n−1αj​⟨Qj|I|Qk⟩​αk∑j,k=0n−1αj​⟨Qj|Qk⟩​αk\displaystyle=\frac{\Braket{\psi|I|\psi}}{\Braket{\psi|\psi}}=\frac{\sum\limits\_{j,k=0}^{n-1}\alpha\_{j}\Braket{Q\_{j}|I|Q\_{k}}\alpha\_{k}}{\sum\limits\_{j,k=0}^{n-1}\alpha\_{j}\Braket{Q\_{j}|Q\_{k}}\alpha\_{k}} |  | (11) |

Here, we continue to use bra–ket notation;
for real matrices, we have
⟨Qj|I|Qk⟩=⟨Qj​Qk​I⟩\Braket{Q\_{j}|I|Q\_{k}}=\Braket{Q\_{j}Q\_{k}I}, and ⟨ψ|I|ψ⟩=⟨ψ2​I⟩\Braket{\psi|I|\psi}=\Braket{\psi^{2}I}.
The ([11](https://arxiv.org/html/2511.01471v1#S4.E11 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) expansion uses 2​n−12n-1 moments ⟨Qk​I⟩\Braket{Q\_{k}I} in the numerator and 2​n−12n-1 moments ⟨Qk⟩\Braket{Q\_{k}} in the denominator.
The Gram matrix ⟨Qj|Qk⟩\Braket{Q\_{j}|Q\_{k}} is obtained from ⟨Qk⟩\Braket{Q\_{k}} using the multiplication operator cmj​kc\_{m}^{jk}.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qj​Qk\displaystyle Q\_{j}Q\_{k} | =∑m=0j+kcmj​k​Qm\displaystyle=\sum\_{m=0}^{j+k}c\_{m}^{jk}Q\_{m} |  | (12) |

Its form is straightforward for monomial and Chebyshev bases, but can be quite challenging in other cases.
See our previous works and the code in [[12](https://arxiv.org/html/2511.01471v1#bib.bib12)] for implementation details.
Below, we will assume that any matrix ⟨Qj|f|Qk⟩\Braket{Q\_{j}|f|Q\_{k}} for j,k=0​…​n−1j,k=0\dots n-1
can always be obtained from the moments ⟨Qm​f⟩\Braket{Q\_{m}f}, m=0​…​2​n−2m=0\dots 2n-2 with ([12](https://arxiv.org/html/2511.01471v1#S4.E12 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

In [[18](https://arxiv.org/html/2511.01471v1#bib.bib18)], we considered various forms of ψ​(x)\psi(x) to interpolate some value in two stages:
first, obtaining a state satisfying certain requirements (such as a state ψy​(x)\psi\_{y}(x) localized at x=yx=y),
and then computing the Radon-Nikodym derivative in that state.
We do not require this interpolation theory here.
The only important feature of ([11](https://arxiv.org/html/2511.01471v1#S4.E11 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) in the present context is that it is
a ratio of two quadratic forms of equal dimension nn, i.e., it is a Rayleigh quotient.
If at least one of the two matrices, ⟨Qj|I|Qk⟩\Braket{Q\_{j}|I|Q\_{k}} or ⟨Qj|Qk⟩\Braket{Q\_{j}|Q\_{k}} in ([11](https://arxiv.org/html/2511.01471v1#S4.E11 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
is positively definite, then they can be simultaneously diagonalized via a generalized eigenproblem.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |I|ψ[i]⟩\displaystyle\left|I\middle|\psi^{[i]}\right> | =λ[i]|G|ψ[i]⟩\displaystyle=\lambda^{[i]}\left|G\middle|\psi^{[i]}\right> |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑k=0n−1⟨Qj|I|Qk⟩​αk[i]\displaystyle\sum\limits\_{k=0}^{n-1}\Braket{Q\_{j}|I|Q\_{k}}\alpha^{[i]}\_{k} | =λ[i]​∑k=0n−1⟨Qj|Qk⟩​αk[i]\displaystyle=\lambda^{[i]}\sum\limits\_{k=0}^{n-1}\Braket{Q\_{j}|Q\_{k}}\alpha^{[i]}\_{k} |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ[i]\displaystyle\psi^{[i]} | =∑k=0n−1αk[i]​Qk\displaystyle=\sum\limits\_{k=0}^{n-1}\alpha^{[i]}\_{k}Q\_{k} |  | (15) |

Eq. ([13](https://arxiv.org/html/2511.01471v1#S4.E13 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is the bra–ket form of the explicit matrix form ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
This eigenproblem provides a solution for determining whether the current execution flow II is low or high:
one can simply compare it’s magnitude with the eigenvalues λ[i]\lambda^{[i]}, e.g., if the value is close to the λ[maxI]\lambda^{[\mathrm{maxI}]},
the current II is very high. In most situations, we are interested in determining whether the execution flow “now”,
in the state ψ0\psi\_{0}, is low or high.
In this case, it is often more convenient to consider the state projection
⟨ψ0|ψ[maxI]⟩2\Braket{\psi\_{0}|\psi^{[\mathrm{maxI}]}}^{2}, where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ0​(x)\displaystyle\psi\_{0}(x) | =c​o​n​s​t⋅∑j,k=0n−1Qj​(x0)​Gj​k−1​Qk​(x)\displaystyle=const\cdot\sum\_{j,k=0}^{n-1}Q\_{j}(x\_{0})G^{-1}\_{jk}Q\_{k}(x) |  | (16) |

is the state localized at x0x\_{0} corresponding to tn​o​wt\_{now},
rather than comparing I0=⟨ψ0|I|ψ0⟩I\_{0}=\Braket{\psi\_{0}|I|\psi\_{0}} with λ[maxI]\lambda^{[\mathrm{maxI}]}.
However, this is an implementation detail, and the most important features of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) are:

* •

  Given a sufficiently large nn, it contains information about long-past II values.
  The eigenproblem matrices in ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) incorporate different time scales,
  with the range of “stored” time scales determined by the value of τ\tau and the problem dimension nn.
  The corresponding realization of an observable in the state ψ​(x)\psi(x) is given by the Rayleigh quotient ([11](https://arxiv.org/html/2511.01471v1#S4.E11 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
* •

  The measures ω​d​V\omega dV and ω​d​t\omega dt enter symmetrically; there are two matrices forming the Rayleigh quotient.
  To compute the left- and right-hand side matrices in eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), 2​n−12n-1
  moments ⟨Qj​I⟩\Braket{Q\_{j}I} and ⟨Qj⟩\Braket{Q\_{j}} are required for each matrix respectively.
* •

  The problem inherently contains thresholds (the eigenvalues λ[i]\lambda^{[i]}),
  making it particularly simple to determine whether the current value is low or high.
* •

  For large enough nn, the method can handle large spikes.
  The approach separates probabilities and values: the situation is analogous to quantum mechanics,
  where a single “several-orders-off” state essentially does not affect the result if its probability is near zero.
  This contrasts with L2L^{2} approaches, such as in ([8](https://arxiv.org/html/2511.01471v1#S4.E8 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), where a single “several-orders-off”
  observation can completely distort the result.
* •

  The eigenvectors ([15](https://arxiv.org/html/2511.01471v1#S4.E15 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) have algebraic properties that are important for our subsequent considerations.

The approach described is a very general method that can be applied to any observable representable
as a Radon–Nikodym derivative d​μ/d​νd\mu/d\nu.
One simply constructs two matrices, ⟨Qj|d​μ/d​t|Qk⟩\Braket{Q\_{j}|d\mu/dt|Q\_{k}} and ⟨Qj|d​ν/d​t|Qk⟩\Braket{Q\_{j}|d\nu/dt|Q\_{k}},
corresponding to the numerator and denominator measures, and then solves the generalized eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
See Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)], Section III, which presents a table of different left- and right-hand
side matrices we previously considered.
As discussed in [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)], when applied to market dynamics,
the execution flow I=d​V/d​tI=dV/dt – a highly fluctuating quantity – is the most important characteristic.
Note that the eigenproblem ([7](https://arxiv.org/html/2511.01471v1#S3.E7 "In III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) considered earlier has a similar structure but is applied to price PP,
with matrices ⟨Qj|P​I|Qk⟩\Braket{Q\_{j}|PI|Q\_{k}} and ⟨Qj|I|Qk⟩\Braket{Q\_{j}|I|Q\_{k}}. The resulting eigenvalues indicate price levels with high traded volume. For a general basis QjQ\_{j}, this will no longer correspond to an orthogonal polynomial; however,
by setting Qj​(x​(t))=Pj​(t)Q\_{j}(x(t))=P^{j}(t) and d​V′=P​d​VdV^{\prime}=PdV and d​t′=d​Vdt^{\prime}=dV,
one recovers ([7](https://arxiv.org/html/2511.01471v1#S3.E7 "In III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) exactly from ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
With d​V′=P​d​tdV^{\prime}=Pdt and d​t′=d​tdt^{\prime}=dt, one also recovers ([7](https://arxiv.org/html/2511.01471v1#S3.E7 "In III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
but the eigenvalues now indicate the price levels at which the most time was spent.

Now we present several simple demonstrations of execution flow properties computed from exchange data.
Our goal is to illustrate the approach in a way similar to the industry-standard “moving average” concept.
We use the basis
x=exp⁡((t−tn​o​w)/τ)x=\exp((t-t\_{now})/\tau), ω=exp⁡((t−tn​o​w)/τ)\omega=\exp((t-t\_{now})/\tau), and Qj​(x)Q\_{j}(x) as a polynomial of degree jj
(the result is invariant with respect to the specific choice of polynomial basis).
Using these data, we compute 2​n−12n-1 moments ⟨Qm​I⟩\Braket{Q\_{m}I} by direct sampling ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The calculations are performed at each time tt over the interval preceding current tn​o​wt\_{now} – analogous to a moving average –
with tn​o​wt\_{now} advancing through the sample.
The moments ⟨Qm⟩\Braket{Q\_{m}} are known analytically for the chosen xx and ω\omega.
All these moments are then used to formulate the eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) and obtain the eigenvalues λ[i]\lambda^{[i]}
and eigenvectors ψ[i]​(x)\psi^{[i]}(x).
Finally, we compute the price PP and t−tn​o​wt-t\_{now} in the state ψ[maxI]\psi^{[\mathrm{maxI}]} corresponding to the maximal eigenvalue
λ[maxI]=⟨ψ[maxI]|I|ψ[maxI]⟩\lambda^{[\mathrm{maxI}]}=\Braket{\psi^{[\mathrm{maxI}]}|I|\psi^{[\mathrm{maxI}]}}, the states are assumed normalized
as ⟨ψ|ψ⟩=1\Braket{\psi|\psi}=1.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P[maxI]\displaystyle P^{[\mathrm{maxI}]} | =⟨ψ[maxI]|P​I|ψ[maxI]⟩⟨ψ[maxI]|I|ψ[maxI]⟩\displaystyle=\frac{\Braket{\psi^{[\mathrm{maxI}]}|PI|\psi^{[\mathrm{maxI}]}}}{\Braket{\psi^{[\mathrm{maxI}]}|I|\psi^{[\mathrm{maxI}]}}} |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | T[maxI]\displaystyle T^{[\mathrm{maxI}]} | =⟨ψ[maxI]|t−tn​o​wτ​I|ψ[maxI]⟩⟨ψ[maxI]|I|ψ[maxI]⟩\displaystyle=\frac{\Braket{\psi^{[\mathrm{maxI}]}|\frac{t-t\_{now}}{\tau}I|\psi^{[\mathrm{maxI}]}}}{\Braket{\psi^{[\mathrm{maxI}]}|I|\psi^{[\mathrm{maxI}]}}} |  | (18) |

The value of PP in the ψ[maxI]\psi^{[\mathrm{maxI}]} state ([17](https://arxiv.org/html/2511.01471v1#S4.E17 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is an important characteristic
of our approach to market dynamics[[6](https://arxiv.org/html/2511.01471v1#bib.bib6)].
The t−tn​o​wt-t\_{now} in this state ([18](https://arxiv.org/html/2511.01471v1#S4.E18 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) has a much simpler structure than PP and allows
a straightforward visualization of qualitative “switching” in the structure of the ψ[maxI]\psi^{[\mathrm{maxI}]} state.
While the moments ⟨Qm​I⟩\Braket{Q\_{m}I} and ⟨Qm​P​I⟩\Braket{Q\_{m}PI} are just glorified moving averages,
the P[maxI]P^{[\mathrm{maxI}]} and T[maxI]T^{[\mathrm{maxI}]} are not. There is an additional step –
selecting the state ψ[maxI]\psi^{[\mathrm{maxI}]} from the ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) solutions.
Thus, the P[maxI]P^{[\mathrm{maxI}]} (or T[maxI]T^{[\mathrm{maxI}]}) can be viewed as a moving average with internal degrees of freedom,
a concept we introduced in Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)].

A regular moving average is computed on a past sample by averaging an observable
with a density such as ω​(t)​d​t\omega(t)dt, which remains the same.
A moving average with internal degrees of freedom is computed on
a past sample by averaging an observable with a density such as ψ2​(x​(t))​ω​(t)​d​t\psi^{2}(x(t))\omega(t)dt,
which changes (according to some equation) as new observations are processed.
This is similar to the two-stage Radon-Nikodym approach of Ref. [[18](https://arxiv.org/html/2511.01471v1#bib.bib18)]:
first select the state, and then evaluate the observable in that state.
For market dynamics, the ψ​(x)\psi(x) in the integration density
is governed by the generalized eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")); the ψ​(x)\psi(x) in question is its maximal eigenvector.

![Refer to caption](x3.png)


Figure 3: 
A demonstration of execution flow. We present the original price PP and P[maxI]P^{[\mathrm{maxI}]} ([17](https://arxiv.org/html/2511.01471v1#S4.E17 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) (light blue).
The other plots are shifted to the 693 level and then scaled to avoid cluttering the chart.
We also present T[maxI]T^{[\mathrm{maxI}]} ([18](https://arxiv.org/html/2511.01471v1#S4.E18 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), the minimal and maximal eigenvalues of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
and I0=⟨ψ0|I|ψ0⟩I\_{0}=\Braket{\psi\_{0}|I|\psi\_{0}} (yellow); the result is obtained for n=12n=12 and τ=128\tau=128s.
All execution flows are scaled by a factor of 5⋅10−65\cdot 10^{-6} to fit the chart.
Among the calculated values, only I0=⟨ψ0|I|ψ0⟩I\_{0}=\Braket{\psi\_{0}|I|\psi\_{0}} can be regarded as a traditional moving average,
since ψ0​(x)\psi\_{0}(x) ([16](https://arxiv.org/html/2511.01471v1#S4.E16 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) does not change with the data.
The others — P[maxI]P^{[\mathrm{maxI}]}, T[maxI]T^{[\mathrm{maxI}]}, λ[minI]\lambda^{[\mathrm{minI}]}, and λ[maxI]\lambda^{[\mathrm{maxI}]} —
can be viewed as moving averages with internal degrees of freedom.
One can clearly observe an immediate switch due to these internal degrees of freedom,
without the τ\tau-proportional lag typical of regular moving averages shown in Fig. [1](https://arxiv.org/html/2511.01471v1#S3.F1 "Figure 1 ‣ III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics").

In Fig. [3](https://arxiv.org/html/2511.01471v1#S4.F3 "Figure 3 ‣ IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"), for the same AAPL dataset as in the figures above,
we present P[maxI]P^{[\mathrm{maxI}]} and T[maxI]T^{[\mathrm{maxI}]}, along with the maximal and minimal eigenvalues of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The value of II at tn​o​wt\_{now}, evaluated as I0=⟨ψ0|I|ψ0⟩I\_{0}=\Braket{\psi\_{0}|I|\psi\_{0}}, is also shown.
Note that P[maxI]P^{[\mathrm{maxI}]}, T[maxI]T^{[\mathrm{maxI}]}, λ[minI]\lambda^{[\mathrm{minI}]}, and λ[maxI]\lambda^{[\mathrm{maxI}]} are moving averages with internal degrees of freedom:
the state is determined by the eigenvalue problem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
Contrary to a regular moving average, where it takes a τ\tau-proportional lag to reflect a qualitative regime change
(see Fig. [1](https://arxiv.org/html/2511.01471v1#S3.F1 "Figure 1 ‣ III Available financial data and time scales ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), a moving average with internal degrees of freedom exhibits an immediate “switch”.
It is convenient to look at T[maxI]T^{[\mathrm{maxI}]} ([18](https://arxiv.org/html/2511.01471v1#S4.E18 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), which grows almost linearly when there is no spike in execution
flow and drops to nearly zero during an execution spike, when ψ[maxI]​(x​(t))\psi^{[\mathrm{maxI}]}(x(t)) is localized near tn​o​wt\_{now}
(i.e. when ⟨ψ[maxI]|ψ0⟩2=|ψ[maxI]​(x0)ψ0​(x0)|2\Braket{\psi^{[\mathrm{maxI}]}|\psi\_{0}}^{2}=\left|\frac{\psi^{[\mathrm{maxI}]}(x\_{0})}{\psi\_{0}(x\_{0})}\right|^{2} is close to 11).

The equation ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) for max⁡I\max I, along with P[maxI]P^{[\mathrm{maxI}]},
is the result we obtained back in [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)].
We even constructed a trading strategy that prevents catastrophic losses. The key idea is to predict I=d​V/d​tI=dV/dt, not price.
This approach is very accurate: if there is a liquidity excess event
(current I0I\_{0} is large, i.e., ⟨ψ[maxI]|ψ0⟩2>0.9\Braket{\psi^{[\mathrm{maxI}]}|\psi\_{0}}^{2}>0.9), then future I0I\_{0} will be low.
Similarly, if there is a liquidity deficit event
(current I0I\_{0} is low, i.e., ⟨ψ[minI]|ψ0⟩2>0.9\Braket{\psi^{[\mathrm{minI}]}|\psi\_{0}}^{2}>0.9), then future I0I\_{0} will be high.
This may seem trivial – alternating periods of low and high liquidity – but it demonstrates that liquidity (not price) undergoes large oscillations, with price changes being a consequence of these liquidity fluctuations.
The key element of the strategy is that it trades liquidity:
providing liquidity during deficits and taking it during excesses.
Specifically, the trader should open a position during liquidity deficits and close it during liquidity excesses.
The rationale is simple: holding a zero position during liquidity excess makes the system resilient to adverse market moves,
while entering a position during liquidity deficits (when volatility is small) allows the strategy
to capture the majority of market movement.
Our experiments (both paper trading and actual NASDAQ trading in 2010–2012)
confirm that this is the only strategy we found that avoids eventual catastrophic P&L loss.
A directional trading strategy that is not predisposed to catastrophic P&L loss
must include at least four types of events:

* •

  Open long position
* •

  Close existing long position
* •

  Open short position
* •

  Close existing short position

Note that a strategy with only two types of events (e.g., when “close existing long” is the same as “open short”)
will inevitably fail eventually, resulting in catastrophic P&L loss.
Equation ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) indicates when to open a position (current I0I\_{0} is low) and when to close it (current I0I\_{0} is large).
As shown above, these conditions translate into projections of ψ0\psi\_{0} onto ψ[maxI]\psi^{[\mathrm{maxI}]} and ψ[minI]\psi^{[\mathrm{minI}]}.
However, it does not specify the direction of the position when opening: whether to go long or short?
One could potentially express this execution flow prediction through volatility trading with options,
but this market is much less liquid, and transaction fees prevented us from performing experiments.

Since [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)], we have devoted substantial effort to determining the direction:
whether to open long or short when I0I\_{0} is low?
The best directional indicator we found back then, and failed to improve in subsequent works,
is the difference between the last price Pl​a​s​tP^{last} and P[maxI]P^{[\mathrm{maxI}]} from ([17](https://arxiv.org/html/2511.01471v1#S4.E17 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dird​P​I\displaystyle\mathrm{dir}\_{dPI} | =λ[maxI]​(Pl​a​s​t−P[maxI])\displaystyle=\lambda^{[\mathrm{maxI}]}\left(P^{last}-P^{[\mathrm{maxI}]}\right) |  | (19) |

Check Fig. [3](https://arxiv.org/html/2511.01471v1#S4.F3 "Figure 3 ‣ IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"): you can see fast regime switches and effective tracking of execution flow.
However, this result was not accurate enough to construct a profitable trading strategy with our available setup.
In this work, we developed a greatly improved directional indicator that brings us close to building such a strategy.
This new result is described below.

## V P&L Calculation Methods

Most trading systems focus on price prediction.
However, a trader is not actually interested in prices; what matters is the P&L.
From our point of view, the P&L, not the price, should be the quantity to predict.
Whereas the price P​(t)P(t) describes the market, the P&L incorporates both market data and trader actions.
Let us write a formal expression for the calculation of the P&L of an equity asset.

Define the position change d​SdS – the number of shares bought (d​S>0dS>0) or sold (d​S<0dS<0) during an interval d​tdt.
When integrated over the full time horizon, a trading strategy d​SdS must satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∫𝑑S\displaystyle 0=\int dS |  | (20) |

This constraint ensures that, for P&L calculation, the position is closed at the end of the investment horizon.
If a trading strategy is not yet closed at tn​o​wt\_{now}, one may formally add a single term −S0-S\_{0} for the currently held position:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | S0\displaystyle S\_{0} | =∫−∞tn​o​w𝑑S\displaystyle=\int\limits\_{-\infty}^{t\_{now}}dS |  | (21) |

and define the modified trading strategy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​S′\displaystyle dS^{\prime} | =d​S−S0​δ​(t−tn​o​w)​d​t\displaystyle=dS-S\_{0}\delta(t-t\_{now})dt |  | (22) |

which satisfies ([20](https://arxiv.org/html/2511.01471v1#S5.E20 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The meaning of this modified strategy is that all held positions are assumed to be sold at tn​o​wt\_{now};
if sold at Pl​a​s​tP^{last}, this corresponds to the calculation of unrealized P&L.
For a given strategy d​SdS satisfying ([20](https://arxiv.org/html/2511.01471v1#S5.E20 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), its P&L is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P&L\displaystyle\mathrm{P\&L} | =−∫P​𝑑S\displaystyle=-\int PdS |  | (23) |

This is the general form of the P&L operator.
A simple example: if one buys vv shares at P1P\_{1} and then sells them at P2P\_{2},
the corresponding d​S/d​t=v​δ​(t−t1)−v​δ​(t−t2)dS/dt=v\delta(t-t\_{1})-v\delta(t-t\_{2}); substituting into ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) gives P&L=v​(P2−P1)\mathrm{P\&L}=v(P\_{2}-P\_{1}).
For convenience, it is better to measure d​SdS in the number of shares and use a discrete measure instead of delta functions,
i.e., to consider d​S/d​VdS/dV and integrate it over d​VdV in ([20](https://arxiv.org/html/2511.01471v1#S5.E20 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) and ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), replacing the integral with a sum.

Integrating ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) by parts, we obtain a different form of the expression, now written in terms of price changes:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P&L\displaystyle\mathrm{P\&L} | =∫S​𝑑P\displaystyle=\int SdP |  | (24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | S​(ts​t​a​r​t)\displaystyle S(t\_{start}) | =S​(te​n​d)=0\displaystyle=S(t\_{end})=0 |  | (25) |

The constraints ([25](https://arxiv.org/html/2511.01471v1#S5.E25 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) explicitly require that the held position S​(t)S(t) equals zero
at both the beginning and the end of the trading interval.
This form is less preferable in practice, since integration over d​PdP is harder to perform than integration
over a discrete measure d​SdS.

The P&L above is presented on a “cash basis”.
Initially, a trader holds cash and zero asset positions,
trading between them with the goal of ending with zero asset position and a cash position increased by the P&L.
One can similarly consider a trading process that results in zero cash position and maximal asset position.
In this case, the P&L is measured in units of asset shares, and all P&L operator expressions remain the same.
It is also possible to require an explicit percentage split between cash and asset positions
to be achieved at the end of the trading strategy. In this case, the P&L operator is modified slightly.
In all considerations below, we will use P&L on a cash basis;
modifications for asset-based P&L are straightforward.
Although asset-based P&L may seem unnatural for equities trading, it is commonly used in currency trading.

![Refer to caption](x4.png)


Figure 4: 
A demonstration of P&L calculation according to ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The discrete measure d​SdS represents the trader’s actions, and its integral SS gives the position held.
Integrating d​SdS with the asset price yields the P&L.
It is important to emphasize that the P&L depends on both the asset price P​(t)P(t) and the trader’s actions d​SdS.

In Fig. [4](https://arxiv.org/html/2511.01471v1#S5.F4 "Figure 4 ‣ V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"), we present a simple demonstration of a trading strategy consisting of ten events (blue d​SdS “impulses”).
The position held is obtained by integrating d​SdS, and the P&L is calculated by integrating P​d​SPdS ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The P&L depends on both the asset price P​(t)P(t) and the trader’s actions d​SdS.
The ultimate problem of market dynamics is to construct d​SdS from past observations (tl,Pl,vl)(t\_{l},P\_{l},v\_{l})
such that it consistently yields a positive P&L.
Consider a few trivial strategies that yield a positive P&L.

Consider a strategy S​(t)=w​(t)​d​P/d​tS(t)=w(t)dP/dt, where w​(t)w(t) is an arbitrary positive function. For simplicity, assume w=1w=1,
and that d​P/d​tdP/dt is zero on the boundaries of the trading interval, thus the constraints ([25](https://arxiv.org/html/2511.01471v1#S5.E25 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) are satisfied.
Substituting this S​(t)S(t) into ([24](https://arxiv.org/html/2511.01471v1#S5.E24 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), we immediately obtain a positive P&L.
Differentiating this SS, we obtain d​S/d​t=d2​P/d​t2dS/dt=d^{2}P/dt^{2}.
This is an important result: the position increment d​S/d​tdS/dt should behave as the second derivative of price.
This may look trivial, but it is actually not.
The very important point is the symmetry of the trading strategy’s position increment:
the position increment should have the symmetry of the second derivative of price.
It must change sign for P→−PP\to-P, and, importantly, must not change sign for t→−tt\to-t.
Trading strategies that do not exhibit this symmetry will not consistently make money.
There is a well-known mantra in the HFT community: trade the second derivative of price.

Consider a strategy d​S=(Pm​aF−P)​d​VdS=(P^{F}\_{ma}-P)dV, where Pm​aFP^{F}\_{ma} is the “future” regular moving average of τ\tau scale,
calculated on the [tn​o​w,tn​o​w+τ][t\_{now},t\_{now}+\tau] interval.
Substituting this d​SdS into ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) yields a positive P&L proportional to the standard deviation squared.
If using the median price instead of Pm​aFP^{F}\_{ma}, the strategy is modified
to buy anything below the median price level and sell everything above it.
When using, instead of Pm​aFP^{F}\_{ma}, the past moving average Pm​aP\_{ma} (calculated on the past [tn​o​w−τ,tn​o​w][t\_{now}-\tau,t\_{now}] interval),
we obtain a typical “mean-reversion” strategy.
It may perform adequately as long as there is no large market move.
However, when such a move occurs, a catastrophic P&L loss typically results.

Consider a strategy
d​S=±(ψ[minI]2​(x​(t))−λ[minI]λ[maxI]​ψ[maxI]2​(x​(t)))​d​VdS=\pm\left({\psi^{[\mathrm{minI}]}}^{2}(x(t))-\frac{\lambda^{[\mathrm{minI}]}}{\lambda^{[\mathrm{maxI}]}}{\psi^{[\mathrm{maxI}]}}^{2}(x(t))\right)dV,
where ψ[i]\psi^{[i]} are the eigenvectors of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
This strategy opens a position at P[minI]P^{[\mathrm{minI}]} and closes it at P[maxI]P^{[\mathrm{maxI}]}.
Whether to go long or short (select the sign of ±\pm) depends on which price is lower.
This serves as an example of a strategy where d​SdS is determined by the probability density calculated from ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

These example strategies (along with several others presented in our previous works)
present a self-referential problem: to construct a d​SdS strategy with a positive P&L, we need to know future prices.
In these examples, we inject future prices into d​SdS to produce a positive P&L
from the terms ∫P​𝑑S\int PdS or ∫S​𝑑P\int SdP in the P&L operator.
Practically, no information about future prices can be used in d​SdS.
Yet, to achieve positive P&L, some information “from the future” is required.
As discussed in [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)], prices cannot serve as such a source.
Importantly, any practical d​SdS model must not explicitly depend on asset prices from the future.

However, if we examine the execution flow I=d​V/d​tI=dV/dt, we realize that we can have some information
“from the future” – specifically, information about the future execution flow.
This implies that a d​SdS model should depend on future execution flow only, not future prices.
In [[4](https://arxiv.org/html/2511.01471v1#bib.bib4)], we introduced the concept of the impact from the future.

## VI Impact From The Future

What information about the future can we obtain at t=tn​o​wt=t\_{now}
from past observations of the sequence (tl,Pl,vl)(t\_{l},P\_{l},v\_{l})?
Given the currently observed value of execution flow I0=⟨ψ0|I|ψ0⟩I\_{0}=\Braket{\psi\_{0}|I|\psi\_{0}},
we know with certainty that the future execution flow I0FI\_{0}^{F} will be greater than I0I\_{0},
since additional trading will inevitably occur in the future.
The maximal eigenvalue λ[maxI]\lambda^{[\mathrm{maxI}]} of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) serves as an estimate of the future execution flow I0FI\_{0}^{F}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I0F\displaystyle I\_{0}^{F} | =λ[maxI]\displaystyle=\lambda^{[\mathrm{maxI}]} |  | (26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​IF\displaystyle dI^{F} | =I0F−I0\displaystyle=I\_{0}^{F}-I\_{0} |  | (27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​IF\displaystyle dI^{F} | ≥0\displaystyle\geq 0 |  | (28) |

A very important fact is that the future II estimator, λ[maxI]\lambda^{[\mathrm{maxI}]},
is calculated based on already executed trades.
If trading activity “now” is slow (i.e., I0I\_{0} is small),
this indicates that buyers and sellers are not well matched at the current price,
implying that the asset price must adjust.
The price movement is expected to occur due to an increase in future II, driven by “future execution”.
In this sense, the slower the market is now, the more dramatic the expected price movement in the future.
The past most dramatic II, represented by λ[maxI]\lambda^{[\mathrm{maxI}]},
can therefore serve as a reasonably good estimator ([26](https://arxiv.org/html/2511.01471v1#S6.E26 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) of the future dramatic II.
Conceptually, this may appear similar to the “reversion to the moving average” type of strategy
often applied by market practitioners to asset prices or their standard deviations.
However, this analogy is incorrect.
Experimental observations [[7](https://arxiv.org/html/2511.01471v1#bib.bib7)] show that such reasoning
can be applied only to the execution flow I=d​V/d​tI=dV/dt,
not to the trading volume, asset price volatility, or any other observable.
Moreover, this prediction works only in one direction — the execution flow tends to increase.
A criterion for the absence of information about the future can also be formulated:
if the current I0I\_{0} is close to λ[maxI]\lambda^{[\mathrm{maxI}]},
it means that we are already in a “very dramatic market” at present,
and thus no additional information about the future state of the market can be inferred:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​IF\displaystyle dI^{F} | =0\displaystyle=0 |  | (29) |

In Fig. [3](https://arxiv.org/html/2511.01471v1#S4.F3 "Figure 3 ‣ IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"), one can identify the “no information” moments when I0I\_{0} (yellow line)
touches λ[maxI]\lambda^{[\mathrm{maxI}]} (top pink line).
Similarly, moments of slow current trading activity
(where a dramatic price movement is expected in the future)
can be identified when I0I\_{0} is close to
λ[minI]\lambda^{[\mathrm{minI}]} (bottom pink line).

The question now is how to use the future II ([26](https://arxiv.org/html/2511.01471v1#S6.E26 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) to obtain directional price information.
One might formally attempt to add some trading volume at t=tn​o​wt=t\_{now},
as discussed in Section VII.C “Impact From The Future Operator” of Ref. [[4](https://arxiv.org/html/2511.01471v1#bib.bib4)],
but this approach is likely incorrect, since these trades have not yet occurred.
Instead, the future II should propagate into the dynamic equation through the boundary condition at t=tn​o​wt=t\_{now}.

As discussed above, a trader should open a position during liquidity deficits and close it during liquidity excesses.
This statement defines the trading strategy. In the previous section, we developed a method to compute the strategy’s P&L.
Thus, this liquidity trading strategy can be represented by trading with the following d​SdS:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​S\displaystyle dS | =d​I\displaystyle=dI |  | (30) |

For this trading strategy, the change in position is equal to the change in execution flow.
To calculate its P&L, one needs to integrate ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")). Over which time interval?
One might think this should be in the ψ[maxI]\psi^{[\mathrm{maxI}]} state with the measure d​μ=ψ[maxI]2​(x​(t))​ω​(t)​d​td\mu={\psi^{[\mathrm{maxI}]}}^{2}(x(t))\omega(t)dt,
but this measure is localized in the past, and the contribution from tn​o​wt\_{now}, where we know the future II,
is small, of order ⟨ψ[maxI]|ψ0⟩2\Braket{\psi^{[\mathrm{maxI}]}|\psi\_{0}}^{2}.
Based on our previous most successful attempt at a directional indicator ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
it is clear that the strategy should be executed over the interval
from the spike in II corresponding to λ[maxI]\lambda^{[\mathrm{maxI}]} up to tn​o​wt\_{now}.
For the two bases we consider,
x=(t−tn​o​w)/τx=(t-t\_{now})/\tau and x=exp⁡((t−tn​o​w)/τ)x=\exp((t-t\_{now})/\tau)
with
ω=exp⁡((t−tn​o​w)/τ)\omega=\exp((t-t\_{now})/\tau),
both the infinitesimal time shifts and the partial interval integration
preserve the ω​(t)\omega(t) weight and the polynomial basis space.
This means that integration and differentiation can be expressed via the same moments (an analogue of integration by parts).
If there were no ω​(t)\omega(t) weight, this would correspond to plain differentiation and integration operators, but ω​(t)\omega(t) introduces extra terms.
The integration with weight corresponding to “since ψ​(x)\psi(x) until now” can be obtained via interval partial integration.
This transform is analytically known for the two bases we use, see Appendix A of Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)].
Basically, this means that if the value of ff in the state ψ\psi is ⟨ψ|f|ψ⟩\Braket{\psi|f|\psi},
then the value of ff in the state “since ψ\psi untill now” is Tr​ρ​f\mathrm{Tr}\rho f, where
the density matrix ρ\rho is calculated from the polynomial ψ2\psi^{2} as described in Appendix A of Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)].
This allows to obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(tn​o​w)−⟨ψ|f|ψ⟩\displaystyle f(t\_{now})-\Braket{\psi|f|\psi} | =Tr​‖ρ​d​fd​t‖\displaystyle=\mathrm{Tr}\left\|\rho\frac{df}{dt}\right\| |  | (31) |

This is essentially a glorified integration by parts:
the ff in the pure state |ψ⟩\Ket{\psi} can be expressed via d​f/d​tdf/dt in the mixed state ρ\rho,
which is calculated from ψ2\psi^{2} using an integration-like operation,
see Section II “Basis Selection” of Ref. [[4](https://arxiv.org/html/2511.01471v1#bib.bib4)], Section II “Basic Mathematics” of Ref. [[5](https://arxiv.org/html/2511.01471v1#bib.bib5)], and Appendix A of Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)].

Having the method ([31](https://arxiv.org/html/2511.01471v1#S6.E31 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) to calculate “since ψ\psi untill now”,
let us take f=If=I and ψ=ψ[maxI]\psi=\psi^{[\mathrm{maxI}]}, then calculate the density matrix ρ\rho corresponding to the polynomial ψ2​(x)\psi^{2}(x).
We immediately see that if the boundary value I​(tn​o​w)I(t\_{now}) equals the impact from the future ([26](https://arxiv.org/html/2511.01471v1#S6.E26 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
we have 0=Tr​‖ρ​d​Id​t‖0=\mathrm{Tr}\left\|\rho\frac{dI}{dt}\right\|,
i.e., it satisfies the P&L constraint ([20](https://arxiv.org/html/2511.01471v1#S5.E20 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
In calculating the P&L for the liquidity trading strategy ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
d​IdI should be used as the position change d​SdS in ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
and the integral should be replaced by a trace with respect to the density matrix ρ\rho.
The P&L for the trading strategy ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) provides the directional information.
The algorithm is straightforward:

* •

  From past observations, calculate the moments ⟨Qm​I⟩\Braket{Q\_{m}I}, construct the matrices ⟨Qj|I|Qk⟩\Braket{Q\_{j}|I|Q\_{k}} and ⟨Qj|Qk⟩\Braket{Q\_{j}|Q\_{k}},
  solve the eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), and determine λ[maxI]\lambda^{[\mathrm{maxI}]} and ψ[maxI]\psi^{[\mathrm{maxI}]}.
* •

  Using the procedure of Appendix A of Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)],
  construct the density matrix ρ\rho from the polynomial ψ[maxI]2​(x){\psi^{[\mathrm{maxI}]}}^{2}(x);
  ρ\rho corresponds to the state “since ψ​(x)\psi(x) until now”.
* •

  Calculate the P&L for the trading strategy ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | dirP​d​I\displaystyle\mathrm{dir}\_{PdI} | =Tr​‖ρ​P​d​Id​t‖\displaystyle=\mathrm{Tr}\left\|\rho\frac{PdI}{dt}\right\| |  | (32) |

  which provides the directional information.
  There is no “−-” sign from ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) included in ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) to match our old result ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

  This directional information has a clear meaning:
  if the current P&L of the trading strategy d​S=d​IdS=dI ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is positive (negative),
  then it will remain such for some (rather substantial) time in the future.
  A practical application is that when the current I0I\_{0} is small
  (e.g., ⟨ψ[minI]|ψ0⟩2>0.9\Braket{\psi^{[\mathrm{minI}]}|\psi\_{0}}^{2}>0.9)
  one should open a long (short) position to capture the future d​IFdI^{F} ([27](https://arxiv.org/html/2511.01471v1#S6.E27 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
  There is no such information available from a price move:
  if the price goes up, it can either continue the trend or bounce back.
  The difference between a past price move and the P&L ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
  is that the P&L preserves its sign for a rather substantial period of time.
  This is because we determined the optimal time scale of I=d​V/d​tI=dV/dt from ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
  by using ψ[maxI]\psi^{[\mathrm{maxI}]} to construct the integration measure in ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) (density matrix ρ\rho).

The only remaining difficulty is calculating the matrix elements
⟨Qj|P​d​Id​t|Qk⟩\Braket{Q\_{j}|P\frac{dI}{dt}|Q\_{k}}
required for taking the trace in ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
an analogue of the P&L integration ([23](https://arxiv.org/html/2511.01471v1#S5.E23 "In V P&L Calculation Methods ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
It would be straightforward if the P​d​SPdS operator were a full differential.
For example, if we formally take the operator d​P​Id​t\frac{dPI}{dt}
as a proxy to P​d​Id​tP\frac{dI}{dt},
we immediately obtain dir=λ[maxI]​(Pl​a​s​t−P[maxI])\mathrm{dir}=\lambda^{[\mathrm{maxI}]}\left(P^{last}-P^{[\mathrm{maxI}]}\right),
which exactly corresponds to our previous result ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))!
However, this is not a proper liquidity trading strategy
since it introduces an extra term I​d​P/d​tIdP/dt, but it demonstrates the correctness of our approach.
The calculation of the required matrix elements is discussed below in Appendix [A](https://arxiv.org/html/2511.01471v1#A1 "Appendix A Calculation of ⟨𝑄_𝑗|𝑃⁢{𝑑⁢𝐼/𝑑⁢𝑡}|𝑄_𝑘⟩ matrix elements from sampled moments ‣ Trade Execution Flow as the Underlying Source of Market Dynamics").
Also see Appendix A of Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)].

## VII Directional Information: A Practical Demonstration

In this section, we present the directional indicators ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) and ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
for the same dataset considered above; the datasets from [[16](https://arxiv.org/html/2511.01471v1#bib.bib16)] will be discussed later.
The goal of this section is to demonstrate the market microstructure,
especially its directional information.
One might consider processing the data statistically,
but any statistical analysis requires averaging over some time scale,
which would prevent us from examining the market microstructure —
a system that lacks a characteristic time scale for which stable statistical properties can be obtained
(heteroscedasticity of the market).
The only available source of a time scale is the averaging with the density
matrix ρ\rho, obtained from the ψ[maxI]\psi^{[\mathrm{maxI}]} solution of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
Whereas the market itself does not have a characteristic time scale, market participants do —
at least the minimal time scale at which they can execute a transaction.
An automated trading machine, built based on the time scale obtained from ψ[maxI]\psi^{[\mathrm{maxI}]},
also has intrinsic time scales.
They are determined by τ\tau and the basis dimension nn.
For the basis x=exp⁡((t−tn​o​w)/τ)x=\exp((t-t\_{now})/\tau), ω=exp⁡((t−tn​o​w)/τ)\omega=\exp((t-t\_{now})/\tau),
the ⟨Qj|I|Qk⟩\Braket{Q\_{j}|I|Q\_{k}} matrix has contributions from τ/(2​n−1)\tau/(2n-1) to τ\tau.
For the basis x=(t−tn​o​w)/τx=(t-t\_{now})/\tau, ω=exp⁡((t−tn​o​w)/τ)\omega=\exp((t-t\_{now})/\tau),
the ⟨Qj|I|Qk⟩\Braket{Q\_{j}|I|Q\_{k}} matrix has contributions from τ\tau to approximately 2​n​τ2n\tau.
Whereas a moving average operates with a single time scale,
our approach works with a range of time scales.
The solution ψ[maxI]\psi^{[\mathrm{maxI}]} corresponds to the optimal one.
In the demonstrations of this section, we use n=12n=12 and τ=128\tau=128s.
The range may not correspond precisely to any specific market,
but the ability to select the proper time scale (from a certain range) is the major result of our work.

![Refer to caption](x5.png)


Figure 5: 
The directional information ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) and ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) (shifted to 693 to fit the chart),
the price, and P[maxI]P^{[\mathrm{maxI}]} ([17](https://arxiv.org/html/2511.01471v1#S4.E17 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) are shown above.
Below (shifted to 691), we present an indicator of low II – a possible “entry point”,
⟨ψ[minI]|ψ0⟩2\Braket{\psi^{[\mathrm{minI}]}|\psi\_{0}}^{2} (if >0.8>0.8),
and an indicator of low II – a possible “exit point”,
⟨ψ[maxI]|ψ0⟩2\Braket{\psi^{[\mathrm{maxI}]}|\psi\_{0}}^{2} (if >0.8>0.8),
shown below the 691 level in the plot.

As discussed above, there should be at least four entry/exit signals.
In Fig. [5](https://arxiv.org/html/2511.01471v1#S7.F5 "Figure 5 ‣ VII Directional Information: A Practical Demonstration ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"), we present the directional indicators
dird​P​I\mathrm{dir}\_{dPI} ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) and dirP​d​I\mathrm{dir}\_{PdI} ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
One can clearly see that they switch when the market conditions change.
The older indicator dird​P​I\mathrm{dir}\_{dPI} [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)], having only a positive measure in P[maxI]P^{[\mathrm{maxI}]} ([17](https://arxiv.org/html/2511.01471v1#S4.E17 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
represents the difference between the last price and the price in the ψ[maxI]\psi^{[\mathrm{maxI}]} state.
The indicator dirP​d​I\mathrm{dir}\_{PdI} includes an additional term, d​Pd​t​d​Vd​t\frac{dP}{dt}\frac{dV}{dt} ([36](https://arxiv.org/html/2511.01471v1#A1.E36 "In Appendix A Calculation of ⟨𝑄_𝑗|𝑃⁢{𝑑⁢𝐼/𝑑⁢𝑡}|𝑄_𝑘⟩ matrix elements from sampled moments ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
which provides more “forward-looking” information.
Empirical results show that the main concept proposed in [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)] –
comparing the terms I​d​Pd​tI\frac{dP}{dt} and P​d​Id​tP\frac{dI}{dt} – is not particularly effective.
The best directional indicator is obtained from the P​d​Id​tP\frac{dI}{dt} term
in the P&L trading strategy ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
Note that this strategy assumes very specific entry/exit levels.
The corresponding entry/exit points are shown on the same chart
as the projections of ψ[minI]\psi^{[\mathrm{minI}]} and ψ[maxI]\psi^{[\mathrm{maxI}]}
on ψ0\psi\_{0}, exceeding 0.80.8. They are marked in orange/red on the chart.

This demonstration shows a highly accurate tracking of directional information.
Of particular interest is the regime switch at t=9.97t=9.97, which is precisely detected by dirP​d​I\mathrm{dir}\_{PdI} ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
A natural question arises: when does this approach fail?
Typically, this occurs when the basis dimension nn and the parameter τ\tau
do not correspond to the actual market dynamics, and the state with the optimal time scale cannot be constructed.
Although not shown in the chart, around t=14.00t=14.00 the trading data from NASDAQ ITCH – used in all charts above –
become significantly slower (a few thousand transactions every half hour)
compared to the beginning of the trading session (a few thousand transactions every few seconds).
Under such conditions, the chosen value n=12n=12 becomes insufficient to construct a ψ\psi corresponding to a large time scale,
and the behavior turns rather random.
A distant analogy would be plotting a moving average with a time window τ\tau that is too small.
In our case, this corresponds to τ\tau being so mismatched that the basis of nn functions
becomes insufficient to construct the proper state.

![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 6: 
The dirP​d​I\mathrm{dir}\_{PdI} ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is shown for AAPL on 2025.04.01, totaling 594,673 transactions [[16](https://arxiv.org/html/2511.01471v1#bib.bib16)].
The dirP​d​I\mathrm{dir}\_{PdI} is filtered by entry points; its value is displayed only when
⟨ψ[minI]|ψ0⟩2>0.8\Braket{\psi^{[\mathrm{minI}]}|\psi\_{0}}^{2}>0.8,
and otherwise it is set to zero; it is moved to 219 and 221 levels to fit the chart.
P[maxI]P^{[\mathrm{maxI}]} ([17](https://arxiv.org/html/2511.01471v1#S4.E17 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is also presented.
One can see that the term d​Pd​t​d​Vd​t\frac{dP}{dt}\frac{dV}{dt} ([36](https://arxiv.org/html/2511.01471v1#A1.E36 "In Appendix A Calculation of ⟨𝑄_𝑗|𝑃⁢{𝑑⁢𝐼/𝑑⁢𝑡}|𝑄_𝑘⟩ matrix elements from sampled moments ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
effectively “removes some signals” compared to
dird​P​I=λ[maxI]​(Pl​a​s​t−P[maxI])\mathrm{dir}\_{dPI}=\lambda^{[\mathrm{maxI}]}\left(P^{last}-P^{[\mathrm{maxI}]}\right) ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
Periods when the basis dimension n=12n=12 is insufficient for τ=128\tau=128s are also observed.

To demonstrate the approach on appropriate HFT data, we used NYSE TAQ files.
This source contains significantly more transactions than NASDAQ ITCH, making it more suitable for our approach.
See Appendix [D](https://arxiv.org/html/2511.01471v1#A4 "Appendix D Software Usage Description ‣ Trade Execution Flow as the Underlying Source of Market Dynamics") below for a description of software usage.
In Fig. [6](https://arxiv.org/html/2511.01471v1#S7.F6 "Figure 6 ‣ VII Directional Information: A Practical Demonstration ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"), we present data for AAPL stock on 2025.04.01, totaling 594,673 transactions;
the data is obtained from [[16](https://arxiv.org/html/2511.01471v1#bib.bib16)].
One can see from the figures that the ψ[maxI]\psi^{[\mathrm{maxI}]}
state is actually preserved for a substantial period of time.
This is why the P&L trading strategy can potentially provide information about the future.
The plots also highlight periods when the basis dimension n=12n=12 is insufficient for τ=128\tau=128s.
Based on these market observations, we can conclude the following:

* •

  Execution flow, I=d​V/d​tI=dV/dt, is the driving force of the market;
  price singularities are directly observed in Fig. [3](https://arxiv.org/html/2511.01471v1#S4.F3 "Figure 3 ‣ IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics") near large I0I\_{0}, also see [[7](https://arxiv.org/html/2511.01471v1#bib.bib7)].
* •

  The state ψ[maxI]\psi^{[\mathrm{maxI}]}, corresponding to the maximal execution flow solution of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
  is relatively stable for a time much longer than the price tick interval.
  This stability allows us to extract information based on the impact from the future assumption ([27](https://arxiv.org/html/2511.01471v1#S6.E27 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
* •

  The method to convert the impact from the future into a possible future price change is the P&L trading strategy,
  d​S=d​IdS=dI ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
  by calculating the P&L in the state “since ψ​(x)\psi(x) until now” ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

## VIII Conclusion

In this paper, we develop a quantitative approach based on trade execution flow, I=d​V/d​tI=dV/dt.
The data typically collected by society consist of individual transactions:
side AA sells vv units of a good to side BB at price PP, receiving v​PvP dollars.
In each such transaction, supply and demand are perfectly matched.
Information sources where supply and demand are not matched (such as limit order book or advertisement listings)
are much less accessible and collected with far less rigor.
In this work, we develop a dynamic theory that operates solely on transaction data:
instead of stating that price is determined by the balance of supply and demand,
we propose that price is determined by the maximum of the execution flow, I=d​V/d​tI=dV/dt,
which can be directly observed from transaction data.

An original mathematical framework, based on the Radon-Nikodym derivative,
is developed to calculate the execution flow from transaction data.
The fundamental question is what information about the future is available to us.
We show that it is information about future execution flow ([26](https://arxiv.org/html/2511.01471v1#S6.E26 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
This impact from the future is then converted into the expected price change
using the liquidity trading strategy ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
yielding directional information in the form of P&L ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
A demonstration for a single asset is presented using several data samples.

The theory can be extended to a multi-asset universe. There are two possible approaches:

* •

  Consider the capital flow for all assets aa of interest, d​C/d​t=∑aP(a)​I(a)dC/dt=\sum\_{a}P^{(a)}I^{(a)},
  and formulate a single eigenvalue problem similar to ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) for d​C/d​tdC/dt instead of d​V/d​tdV/dt.
* •

  Consider each asset separately, applying its own equation ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) for I(a)I^{(a)},
  and then combine the results as d​C/d​t=∑aI(a)​P(a)​l​a​s​tdC/dt=\sum\_{a}I^{(a)}P^{(a)\,last}

Our preliminary experiments indicate an advantage of the second approach,
since the states of maximal execution flow for different assets may lead or lag each other in a seemingly random manner.
While a full understanding of multi-asset dynamics remains a subject of future research,
we emphasize that the developed technique for incremental calculation of moments from
the execution flow is highly efficient and capable of processing data in real time.
Combined with parallelization of solving the eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) for each individual asset,
we see no obstacles to deploying this approach in real time across the entire U.S. equity market.

###### Acknowledgements.

This research was supported by Autretech Group,
a resident company of the Skolkovo Technopark.
We thank our colleagues from the Autretech R&D department
who provided insight and expertise that greatly assisted the research.
Our grateful thanks are also extended
to Mr. Gennady Belov for his methodological support in doing the data analysis.

## Appendix A Calculation of ⟨Qj|P​d​Id​t|Qk⟩\left<Q\_{j}\middle|P\frac{dI}{dt}\middle|Q\_{k}\right> matrix elements from sampled moments

Direct sampling ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) allows obtaining only the moments of first derivatives.
Second-order derivatives can be obtained either from secondary sampling or from another type of approximation.
The main matrix of interest ⟨Qj|P​d​Id​t|Qk⟩\Braket{Q\_{j}|P\frac{dI}{dt}|Q\_{k}} can be converted, using integration by parts,
to ⟨Qj|d​P​Id​t|Qk⟩\left<Q\_{j}\middle|\frac{dPI}{dt}\middle|Q\_{k}\right> (which is trivial to calculate)
and ⟨Qj|d​Pd​t​d​Vd​t|Qk⟩\left<Q\_{j}\middle|\frac{dP}{dt}\frac{dV}{dt}\middle|Q\_{k}\right>, which is much more difficult to compute.
In Appendix A of Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)], we considered several approximations for calculating the second derivative moments.
The main idea for computing the moments of a product of two functions is to introduce a delta-function-type expression.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Qj|f​g|Qk⟩=\displaystyle\Braket{Q\_{j}|fg|Q\_{k}}= |  | (33) |
|  |  |  |
| --- | --- | --- |
|  | ∫−∞tn​o​wω​(t)​𝑑t​∫−∞tn​o​w𝑑t′​Qj​(x​(t))​f​(t)​δ​(t−t′)​g​(t′)​Qk​(x​(t′))\displaystyle\int\limits\_{-\infty}^{t\_{now}}\omega(t)dt\int\limits\_{-\infty}^{t\_{now}}dt^{\prime}Q\_{j}(x(t))f(t)\delta(t-t^{\prime})g(t^{\prime})Q\_{k}(x(t^{\prime})) |  |

Then change the integration variable to xx and use a reproducing kernel
as an approximation of the delta function:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒦​(x,x′)\displaystyle\mathcal{K}(x,x^{\prime}) | =∑j,k=0nd−1Qj​(x)​Gj​k−1​Qk​(x′)\displaystyle=\sum\limits\_{j,k=0}^{n\_{d}-1}Q\_{j}(x)G^{-1}\_{jk}Q\_{k}(x^{\prime}) |  | (34) |

For a fixed x′=x0x^{\prime}=x\_{0}, the reproducing kernel gives a wavefunction localized at x0x\_{0},
e.g., ψ0​(x)=c​o​n​s​t⋅𝒦​(x,x0)\psi\_{0}(x)=const\cdot\mathcal{K}(x,x\_{0}), Eq. ([16](https://arxiv.org/html/2511.01471v1#S4.E16 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), where c​o​n​s​tconst is a normalizing constant such that ⟨ψ0|ψ0⟩=1\Braket{\psi\_{0}|\psi\_{0}}=1.
If nd=nn\_{d}=n, then we obtain the familiar approximation for the product of functions[[13](https://arxiv.org/html/2511.01471v1#bib.bib13)].

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨Qj|f​g|Qk⟩\displaystyle\Braket{Q\_{j}|fg|Q\_{k}} | ≈∑q,r=0nd−1⟨Qj|f|Qq⟩​Gq​r−1​⟨Qr|g|Qk⟩\displaystyle\approx\sum\limits\_{q,r=0}^{n\_{d}-1}\Braket{Q\_{j}|f|Q\_{q}}G^{-1}\_{qr}\Braket{Q\_{r}|g|Q\_{k}} |  | (35) |

This operator approximation, while being non-Hermitian,
creates no problem since it is used only in the calculation of the trace with the Hermitian density matrix ρ\rho,
as in ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
Numerical experiments show that it is the moments of d​Pd​t​d​Vd​t\frac{dP}{dt}\frac{dV}{dt}
that are well-approximated in this product-type expression.
The moments of functions containing second derivatives (especially of price, e.g.,
⟨Qj​I​d2​Pd​t2⟩\Braket{Q\_{j}I\frac{d^{2}P}{dt^{2}}}, ⟨Qj​V​d2​Pd​t2⟩\Braket{Q\_{j}V\frac{d^{2}P}{dt^{2}}}, etc.) are particularly poor in this type of approximation.
For simplicity, we will use f=d​P/d​tf=dP/dt and g=d​V/d​tg=dV/dt, the moments of which are obtained from sampling ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
to estimate ⟨Qj|d​Pd​t​d​Vd​t|Qk⟩\left<Q\_{j}\middle|\frac{dP}{dt}\frac{dV}{dt}\middle|Q\_{k}\right>.
This is the simplest version of the approximation theory developed in Appendix A of Ref. [[13](https://arxiv.org/html/2511.01471v1#bib.bib13)].

An important improvement is that now, in the reproducing kernel ([34](https://arxiv.org/html/2511.01471v1#A1.E34 "In Appendix A Calculation of ⟨𝑄_𝑗|𝑃⁢{𝑑⁢𝐼/𝑑⁢𝑡}|𝑄_𝑘⟩ matrix elements from sampled moments ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), we take the dimension nd>nn\_{d}>n.
This creates rectangular n×ndn\times n\_{d} matrices
⟨Qj|d​Pd​t|Qk⟩\left<Q\_{j}\middle|\frac{dP}{dt}\middle|Q\_{k}\right> and
⟨Qj|d​Vd​t|Qk⟩\left<Q\_{j}\middle|\frac{dV}{dt}\middle|Q\_{k}\right>,
and analytically known Gram matrix ([10](https://arxiv.org/html/2511.01471v1#S4.E10 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) now has dimension nd×ndn\_{d}\times n\_{d}.
Everything else in ([35](https://arxiv.org/html/2511.01471v1#A1.E35 "In Appendix A Calculation of ⟨𝑄_𝑗|𝑃⁢{𝑑⁢𝐼/𝑑⁢𝑡}|𝑄_𝑘⟩ matrix elements from sampled moments ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) remains the same; a typical good value for ndn\_{d} is nd≳2​nn\_{d}\gtrsim 2n.
The result is a well-approximated matrix
⟨Qj|d​Pd​t​d​Vd​t|Qk⟩\left<Q\_{j}\middle|\frac{dP}{dt}\frac{dV}{dt}\middle|Q\_{k}\right>
of dimension n×nn\times n,
which we use to obtain the matrix
⟨Qj|P​d​Id​t|Qk⟩\left<Q\_{j}\middle|P\frac{dI}{dt}\middle|Q\_{k}\right>
required for P&L calculation ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
of the liquidity trading strategy ([30](https://arxiv.org/html/2511.01471v1#S6.E30 "In VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨Qj|P​d​Id​t|Qk⟩\displaystyle\left<Q\_{j}\middle|P\frac{dI}{dt}\middle|Q\_{k}\right> | =⟨Qj|d​P​Id​t|Qk⟩−⟨Qj|d​Pd​t​d​Vd​t|Qk⟩\displaystyle=\left<Q\_{j}\middle|\frac{dPI}{dt}\middle|Q\_{k}\right>-\left<Q\_{j}\middle|\frac{dP}{dt}\frac{dV}{dt}\middle|Q\_{k}\right> |  | (36) |

If only the first term, ⟨Qj|d​P​Id​t|Qk⟩\left<Q\_{j}\middle|\frac{dPI}{dt}\middle|Q\_{k}\right>, is retained –
then the new result for directional information ([32](https://arxiv.org/html/2511.01471v1#S6.E32 "In 3rd item ‣ VI Impact From The Future ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) corresponds exactly
to the old result ([19](https://arxiv.org/html/2511.01471v1#S4.E19 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) obtained in Ref. [[6](https://arxiv.org/html/2511.01471v1#bib.bib6)].

## Appendix B Solving the Optimization Problem in the Localized Basis

![Refer to caption](x9.png)


Figure 7: 
A presentation of P[maxI]P^{[\mathrm{maxI}]} and T[maxI]T^{[\mathrm{maxI}]} calculated in the state ψ[maxI]\psi^{[\mathrm{maxI}]}
from the solution of ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) (Fig. [3](https://arxiv.org/html/2511.01471v1#S4.F3 "Figure 3 ‣ IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
is compared with the results obtained from the localized optimization ([40](https://arxiv.org/html/2511.01471v1#A2.E40 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"));
the result is obtained for n=12n=12 and τ=128\tau=128s.
One can see very similar results.
This confirms that the ψy​(x)\psi\_{y}(x) basis ([39](https://arxiv.org/html/2511.01471v1#A2.E39 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) can be used for optimization problems
for which an equivalent eigenproblem is not available.

In the considerations above, we studied the states of maximal execution flow, I=d​V/d​t→maxI=dV/dt\to\max,
which led to the eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
We may also consider the states related to a large volume traded in the past.
A concept that significantly simplifies this consideration is the Christoffel function:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K​(x)\displaystyle K(x) | =1𝒦​(x,x)=1∑j,k=0n−1Qj​(x)​Gj​k−1​Qk​(x)\displaystyle=\frac{1}{\mathcal{K}(x,x)}=\frac{1}{\sum\limits\_{j,k=0}^{n-1}Q\_{j}(x)G^{-1}\_{jk}Q\_{k}(x)} |  | (37) |

where 𝒦​(x,x)\mathcal{K}(x,x) is the reproducing kernel ([34](https://arxiv.org/html/2511.01471v1#A1.E34 "In Appendix A Calculation of ⟨𝑄_𝑗|𝑃⁢{𝑑⁢𝐼/𝑑⁢𝑡}|𝑄_𝑘⟩ matrix elements from sampled moments ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
and G−1G^{-1} is Gram matrix ⟨Qj|Qk⟩\Braket{Q\_{j}|Q\_{k}} ([10](https://arxiv.org/html/2511.01471v1#S4.E10 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) inverse.
The Christoffel function has been extensively studied in recent works [[19](https://arxiv.org/html/2511.01471v1#bib.bib19), [20](https://arxiv.org/html/2511.01471v1#bib.bib20)],
it is of significant value for data analysis[[21](https://arxiv.org/html/2511.01471v1#bib.bib21)].
Among the important results of [[18](https://arxiv.org/html/2511.01471v1#bib.bib18)]
is the consideration of the Christoffel function spectrum, obtained from the eigenproblem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑k=0n−1⟨Qj|K|Qk⟩​αk[i]\displaystyle\sum\limits\_{k=0}^{n-1}\Braket{Q\_{j}|K|Q\_{k}}\alpha^{[i]}\_{k} | =λ[i]​∑k=0n−1⟨Qj|Qk⟩​αk[i]\displaystyle=\lambda^{[i]}\sum\limits\_{k=0}^{n-1}\Braket{Q\_{j}|Q\_{k}}\alpha^{[i]}\_{k} |  | (38) |

that allows the construction of an invariant expansion — a promising basis-invariant alternative
to the PCA expansion (which is only unitary-invariant),
a transition from variance expansion to coverage expansion.
It is based on the eigenproblem ([38](https://arxiv.org/html/2511.01471v1#A2.E38 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
where each eigenvector gives the λ[i]\lambda^{[i]} contribution to coverage,
with the total coverage being ⟨1⟩=∑i=0n−1λ[i]\Braket{1}=\sum\_{i=0}^{n-1}\lambda^{[i]}, see Appendix [C](https://arxiv.org/html/2511.01471v1#A3 "Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics") below.

Consider the product of execution flow, I=d​V/d​tI=dV/dt, with the Christoffel function, K​(x)K(x).
Extra terms in the denominator make the problem difficult to approach.
However, if we consider only the states localized at x=yx=y, denoted as ψy​(x)\psi\_{y}(x),
for y=x0y=x\_{0} ψy​(x)\psi\_{y}(x) is just ([16](https://arxiv.org/html/2511.01471v1#S4.E16 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψy​(x)\displaystyle\psi\_{y}(x) | =∑i=0n−1ψ[i]​(y)​ψ[i]​(x)∑i=0n−1[ψ[i]​(y)]2=∑j,k=0n−1Qj​(y)​Gj​k−1​Qk​(x)∑j,k=0n−1Qj​(y)​Gj​k−1​Qk​(y)\displaystyle=\frac{\sum\limits\_{i=0}^{n-1}\psi^{[i]}(y)\psi^{[i]}(x)}{\sqrt{\sum\limits\_{i=0}^{n-1}\left[\psi^{[i]}(y)\right]^{2}}}=\frac{\sum\limits\_{j,k=0}^{n-1}Q\_{j}(y)G^{-1}\_{jk}Q\_{k}(x)}{\sqrt{\sum\limits\_{j,k=0}^{n-1}Q\_{j}(y)G^{-1}\_{jk}Q\_{k}(y)}} |  | (39) |

In this restricted form of ψ\psi, it becomes approachable.
Evaluating an operator in the ψy​(x)\psi\_{y}(x) state gives the Radon-Nikodym approximation [[18](https://arxiv.org/html/2511.01471v1#bib.bib18)],
which is reduced to a ratio of polynomials of equal degree

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(y)\displaystyle I(y) | ≈⟨ψy|I|ψy⟩⟨ψy|ψy⟩\displaystyle\approx\frac{\Braket{\psi\_{y}|I|\psi\_{y}}}{\Braket{\psi\_{y}|\psi\_{y}}} |  | (40) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j,j′,k′,k=0n−1Qj​(y)​Gj​j′−1​⟨Qj′|I|Qk′⟩​Gk′​k−1​Qk​(y)∑j,k=0n−1Qj​(y)​Gj​k−1​Qk​(y)\displaystyle=\frac{\sum\limits\_{j,j^{\prime},k^{\prime},k=0}^{n-1}Q\_{j}(y)G^{-1}\_{jj^{\prime}}\Braket{Q\_{j^{\prime}}|I|Q\_{k^{\prime}}}G^{-1}\_{k^{\prime}k}Q\_{k}(y)}{\sum\limits\_{j,k=0}^{n-1}Q\_{j}(y)G^{-1}\_{jk}Q\_{k}(y)} |  |

Compare this expression with the least squares approximation ([9](https://arxiv.org/html/2511.01471v1#S4.E9 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), which is a polynomial.
The K​(y)K(y) is known analytically from ([37](https://arxiv.org/html/2511.01471v1#A2.E37 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(y)​K​(y)\displaystyle I(y)K(y) | ≈∑j,j′,k′,k=0n−1Qj​(y)​Gj​j′−1​⟨Qj′|I|Qk′⟩​Gk′​k−1​Qk​(y)|∑j,k=0n−1Qj​(y)​Gj​k−1​Qk​(y)|2\displaystyle\approx\frac{\sum\limits\_{j,j^{\prime},k^{\prime},k=0}^{n-1}Q\_{j}(y)G^{-1}\_{jj^{\prime}}\Braket{Q\_{j^{\prime}}|I|Q\_{k^{\prime}}}G^{-1}\_{k^{\prime}k}Q\_{k}(y)}{\left|\sum\limits\_{j,k=0}^{n-1}Q\_{j}(y)G^{-1}\_{jk}Q\_{k}(y)\right|^{2}} |  | (41) |

The product I​(y)​K​(y)I(y)K(y), calculated using the Radon-Nikodym approximation,
is reduced to a ratio of polynomials.
Contrary to the Rayleigh quotient ([11](https://arxiv.org/html/2511.01471v1#S4.E11 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), where the numerator and denominator are of the same degree,
for the product I​(y)​K​(y)I(y)K(y) the denominator degree, 4​n−44n-4, is twice that of the numerator degree, 2​n−22n-2.
This means we cannot approach the optimization through an eigenvalue formulation. However, by considering polynomials ratio
and using our numerical library [[12](https://arxiv.org/html/2511.01471v1#bib.bib12)] for manipulating polynomials in an arbitrary basis QjQ\_{j},
we can find all the zeros of the first derivative of ([41](https://arxiv.org/html/2511.01471v1#A2.E41 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) with respect to yy,
and then select the one corresponding to the maximal I​KIK;
in this way, we reduce the optimization problem to finding the polynomial roots (the zeros of the derivative of ([41](https://arxiv.org/html/2511.01471v1#A2.E41 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))).
The cost of this reduction is that the optimization problem is now formulated in the basis of localized states
([39](https://arxiv.org/html/2511.01471v1#A2.E39 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), rather than in the arbitrary basis ψ\psi ([15](https://arxiv.org/html/2511.01471v1#S4.E15 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

![Refer to caption](x10.png)


Figure 8: 
A presentation of P[maxI]P^{[\mathrm{maxI}]} and T[maxI]T^{[\mathrm{maxI}]}, calculated in the state ψ[maxI]\psi^{[\mathrm{maxI}]}
that maximizes II ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), and P[maxIK]P^{[\mathrm{maxIK}]} and T[maxIK]T^{[\mathrm{maxIK}]}, corresponding to a localized ψy\psi\_{y} ([39](https://arxiv.org/html/2511.01471v1#A2.E39 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) that maximizes I​KIK ([41](https://arxiv.org/html/2511.01471v1#A2.E41 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), is shown; the result is obtained for n=12n=12 and τ=128\tau=128s.
Both exhibit state switching, but a switch in the states maximizing I​KIK is less likely.

Before we consider I​KIK, let us compare the two approaches: solve the optimization problem I→maxI\to\max
in the localized basis ([40](https://arxiv.org/html/2511.01471v1#A2.E40 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), and then compare the result with that obtained from the eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The result is presented in the plot in Fig. [7](https://arxiv.org/html/2511.01471v1#A2.F7 "Figure 7 ‣ Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics").
One can observe that the eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) and the localized optimization ([40](https://arxiv.org/html/2511.01471v1#A2.E40 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics"))
produce very similar results for PP and TT.
This allows us to conclude the validity of localized optimization in the basis of ψy​(x)\psi\_{y}(x) states ([39](https://arxiv.org/html/2511.01471v1#A2.E39 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).

Now, having established a technique that takes us beyond the eigenproblem,
let us solve the I​KIK maximization problem ([41](https://arxiv.org/html/2511.01471v1#A2.E41 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The I​KIK has the meaning of volume, rather than execution flow II.
The state ψy​(x)\psi\_{y}(x) that maximizes ([41](https://arxiv.org/html/2511.01471v1#A2.E41 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) corresponds to the state in which a large trading volume has occurred.
Technically, this is an optimization problem of a ratio of two polynomials.

The result is presented in Fig. [8](https://arxiv.org/html/2511.01471v1#A2.F8 "Figure 8 ‣ Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics").
One can observe a similar type of switching, but the K​(x)K(x) factor makes the switching less likely,
as it requires a substantial volume to be traded.
The plot demonstrates the validity of the localized states ψy\psi\_{y} ([39](https://arxiv.org/html/2511.01471v1#A2.E39 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) optimization approach.
Note that this localized optimization is applicable only for one-dimensional problems.
If we were to have a basis of several variables, Qj​(y)​Qk​(z)Q\_{j}(y)Q\_{k}(z),
the optimization ([41](https://arxiv.org/html/2511.01471v1#A2.E41 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) would not allow us to find the roots,
whereas the generalized eigenproblem ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) would still be applicable [[18](https://arxiv.org/html/2511.01471v1#bib.bib18)].

## Appendix C Christoffel Function Coverage Expansion

The problem ([38](https://arxiv.org/html/2511.01471v1#A2.E38 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) can be generalized to a multi-dimensional space to construct a coverage-type expansion.
Consider a sample in an nn-dimensional space 𝐱=(x0,x1,x2,…,xn−1)\mathbf{x}=(x\_{0},x\_{1},x\_{2},\dots,x\_{n-1});
in the scalar case, we have xj=Qj​(x)x\_{j}=Q\_{j}(x).
We also introduce a measure ⟨⋅⟩\Braket{\cdot} that enables the calculation of averages ⟨xj|f|xk⟩\Braket{x\_{j}|f|x\_{k}}.
The meaning of this average can be, for example, ω​d​V\omega dV, ω​d​t\omega dt, or a general sample sum.
The Gram matrix and the Christoffel function are given by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gj​k\displaystyle G\_{jk} | =⟨xj|xk⟩\displaystyle=\Braket{x\_{j}|x\_{k}} |  | (42) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K​(𝐱)\displaystyle K(\mathbf{x}) | =1∑j,k=0n−1xj​Gj​k−1​xk=1∑i=0n−1ψ[i]2​(𝐱)\displaystyle=\frac{1}{\sum\limits\_{j,k=0}^{n-1}x\_{j}G^{-1}\_{jk}x\_{k}}=\frac{1}{\sum\limits\_{i=0}^{n-1}{\psi^{[i]}}^{2}(\mathbf{x})} |  | (43) |

here, ψ[i]\psi^{[i]} is an arbitrary orthogonal basis, satisfying ⟨ψ[i]|ψ[j]⟩=δi​j\Braket{\psi^{[i]}|\psi^{[j]}}=\delta\_{ij}.
Eq. ([43](https://arxiv.org/html/2511.01471v1#A3.E43 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) is a generalization of ([37](https://arxiv.org/html/2511.01471v1#A2.E37 "In Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) to the multi-dimensional space 𝐱\mathbf{x},
the Christoffel function matrix elements are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨xj|K|xk⟩\displaystyle\Braket{x\_{j}|K|x\_{k}} | =⟨xj​xk∑j′,k′=0n−1xj′​Gj′​k′−1​xk′⟩\displaystyle=\left\langle\frac{x\_{j}x\_{k}}{\sum\limits\_{j^{\prime},k^{\prime}=0}^{n-1}x\_{j^{\prime}}G^{-1}\_{j^{\prime}k^{\prime}}x\_{k^{\prime}}}\right\rangle |  | (44) |

This requires calculating the average of a ratio of two quadratic functions,
where the one in the denominator is positively definite.
These averages always exist, but their computation is more demanding.
Moreover, due to the presence of the denominator term in ([44](https://arxiv.org/html/2511.01471v1#A3.E44 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
they cannot be computed incrementally.
A full scan of the entire sample is typically required to construct the matrix ⟨xj|K|xk⟩\Braket{x\_{j}|K|x\_{k}}.
Consider the eigenproblem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑k=0n−1⟨xj|K|xk⟩​αk[i]\displaystyle\sum\limits\_{k=0}^{n-1}\Braket{x\_{j}|K|x\_{k}}\alpha^{[i]}\_{k} | =λ[i]​∑k=0n−1⟨xj|xk⟩​αk[i]\displaystyle=\lambda^{[i]}\sum\limits\_{k=0}^{n-1}\Braket{x\_{j}|x\_{k}}\alpha^{[i]}\_{k} |  | (45) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ[i]​(𝐱)\displaystyle\psi^{[i]}(\mathbf{x}) | =∑j=0n−1αj[i]​xj\displaystyle=\sum\limits\_{j=0}^{n-1}\alpha^{[i]}\_{j}x\_{j} |  | (46) |

From the definition ([43](https://arxiv.org/html/2511.01471v1#A3.E43 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), it immediately follows that all eigenvalues are positive,
and their sum equals the total measure of the space considered.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨1⟩\displaystyle\Braket{1} | =∑i=0n−1λ[i]\displaystyle=\sum\limits\_{i=0}^{n-1}\lambda^{[i]} |  | (47) |

This expansion can be viewed as a generalization of Gaussian quadrature [[22](https://arxiv.org/html/2511.01471v1#bib.bib22)],
where the weights are
λ[i]\lambda^{[i]}
and the nodes are not discrete measure at nn support points, but nn probability densities K​ψ[i]2​(𝐱)K{\psi^{[i]}}^{2}(\mathbf{x}),
where λ[i]=⟨ψ[i]|K|ψ[i]⟩\lambda^{[i]}=\Braket{\psi^{[i]}|K|\psi^{[i]}}.
By sorting the eigenvalues λ[i]\lambda^{[i]} in descending order, we obtain the factors ψ[i]​(𝐱)\psi^{[i]}(\mathbf{x})
corresponding to a descending contribution to coverage.
By selecting a few eigenvectors, we can create a projected state that covers a large portion of the observations,
equal to the ratio of the sum of the selected λ[i]\lambda^{[i]} to the total sum ([47](https://arxiv.org/html/2511.01471v1#A3.E47 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
This expansion is completely scale-independent,
and the result is invariant under an arbitrary non-degenerate transformation of the 𝐱\mathbf{x} components:
xj′=∑k=0n−1Tj​k​xkx^{\prime}\_{j}=\sum\_{k=0}^{n-1}T\_{jk}x\_{k}.

For a PCA expansion, we need a function ff whose standard deviation we calculate, computing the minimal possible
least squares

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σmin2\displaystyle\sigma^{2}\_{\min} | =⟨(f−∑j=0n−1βj​xj)2⟩→min\displaystyle=\Braket{\left(f-\sum\limits\_{j=0}^{n-1}\beta\_{j}x\_{j}\right)^{2}}\to\min |  | (48) |

this is essentially ([8](https://arxiv.org/html/2511.01471v1#S4.E8 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) in the multi-dimensional case.
The standard deviation of ff can then be expressed as σmin2=⟨(f−f¯)2⟩−∑i=0n−1σi2\sigma^{2}\_{\min}=\Braket{(f-\overline{f})^{2}}-\sum\_{i=0}^{n-1}\sigma^{2}\_{i},
where the contributions σi2\sigma^{2}\_{i} correspond to the eigenvectors of an eigenproblem derived from ([48](https://arxiv.org/html/2511.01471v1#A3.E48 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
obtained by performing an eigen-decomposition of the covariance matrix and expanding ff in the resulting eigenbasis.
Selecting a few of the largest contributions yields the PCA factors “explanation” of ff.
This expansion, however, is only unitary invariant (e.g., the solution will change if we rescale one of the xkx\_{k}),
and it requires the introduction of some function ff, the variation of which is expanded.
In contrast, the coverage expansion ([47](https://arxiv.org/html/2511.01471v1#A3.E47 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) requires no function ff
and directly selects the states with the maximal probability of occurrence.
This expansion is of great value for the problem of clustering,
where selecting a few most probable states is of critical importance [[18](https://arxiv.org/html/2511.01471v1#bib.bib18)].

In some situations, when the behavior of ff needs to be inferred from the behavior of d​fd​t\frac{df}{dt},
it is convenient to consider the matrix elements
of the same structure as in ([44](https://arxiv.org/html/2511.01471v1#A3.E44 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")):
the average of a ratio of two quadratic functions, where the one in the denominator is positively definite.
Similar to the calculation in ([4](https://arxiv.org/html/2511.01471v1#S2.E4 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")), taking the matrix elements of d​f/d​tdf/dt
replaces the summation over tl−tl−1t\_{l}-t\_{l-1} with a summation over fl−fl−1f\_{l}-f\_{l-1}.
The expression for ⟨⋅⟩\Braket{\cdot} is identical to ([1](https://arxiv.org/html/2511.01471v1#S2.E1 "In II Moment Calculation from Empirical Samples ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")),
except that, instead of a polynomial Qj​(x​(tl))Q\_{j}(x(t\_{l})), we now have a ratio of two quadratic functions on xm(l)x\_{m}^{(l)}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨xj|K​d​fd​t|xk⟩\displaystyle\Braket{x\_{j}|K\frac{df}{dt}|x\_{k}} | =⟨xj​xk​d​fd​t∑j′,k′=0n−1xj′​Gj′​k′−1​xk′⟩\displaystyle=\left\langle\frac{x\_{j}x\_{k}\frac{df}{dt}}{\sum\limits\_{j^{\prime},k^{\prime}=0}^{n-1}x\_{j^{\prime}}G^{-1}\_{j^{\prime}k^{\prime}}x\_{k^{\prime}}}\right\rangle |  | (49) |

Then we solve a generalized eigenproblem with the matrices ⟨xj|K​d​fd​t|xk⟩\Braket{x\_{j}|K\frac{df}{dt}|x\_{k}} and ⟨xj|xk⟩\Braket{x\_{j}|x\_{k}}.
This approach is analogous to the treatment of K​d​Vd​tK\frac{dV}{dt} discussed in Appendix [B](https://arxiv.org/html/2511.01471v1#A2 "Appendix B Solving the Optimization Problem in the Localized Basis ‣ Trade Execution Flow as the Underlying Source of Market Dynamics") above.
A trivial example. Let ff being some portfolio, and d​fd​t\frac{df}{dt} being daily portfolio change,
xjx\_{j} are the factors affecting the porfolio value,
and the measure ⟨⋅⟩\Braket{\cdot} is taken as a sum over the days ll, with ω(l)=1\omega^{(l)}=1.
Then the eigenproblem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Kd​fd​t|ψ[i]⟩\displaystyle\left|K\frac{df}{dt}\middle|\psi^{[i]}\right> | =λ[i]|G|ψ[i]⟩\displaystyle=\lambda^{[i]}\left|G\middle|\psi^{[i]}\right> |  | (50) |

expands the P&L contributions by factors.
The sum of all eigenvalues λ[i]\lambda^{[i]} equals the total change in the portfolio value over the entire period,
⟨d​fd​t⟩\Braket{\frac{df}{dt}}, compare with ([47](https://arxiv.org/html/2511.01471v1#A3.E47 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")).
The solution of ([50](https://arxiv.org/html/2511.01471v1#A3.E50 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) can also be interpreted as a form of Lebesgue quadrature,
where the weights λ[i]\lambda^{[i]} represent P&L contributions (not necessarily positive),
and the nodes are not discrete measure at nn support points but rather nn probability densities K​ψ[i]2​(𝐱)K{\psi^{[i]}}^{2}(\mathbf{x}),
where λ[i]=⟨ψ[i]|K​d​fd​t|ψ[i]⟩\lambda^{[i]}=\Braket{\psi^{[i]}|K\frac{df}{dt}|\psi^{[i]}};
for other forms of Lebesgue quadrature, see [[22](https://arxiv.org/html/2511.01471v1#bib.bib22)].
Note that the observable (total P&L) is obtained as a sum of eigenvalues (Lebesgue weights),
representing a form of density matrix average,
rather than as a sum of eigenvalues multiplied by squared projections, as in traditional PCA.

If the Christoffel function KK is not used on the left-hand side –
i.e., if we consider an eigenproblem with the matrices ⟨xj|d​fd​t|xk⟩\Braket{x\_{j}|\frac{df}{dt}|x\_{k}} and ⟨xj|xk⟩\Braket{x\_{j}|x\_{k}} –
then the λ[i]\lambda^{[i]} would describe contributions to daily returns, rather than to the total P&L.
This situation is similar to that considered in Eq. ([14](https://arxiv.org/html/2511.01471v1#S4.E14 "In IV Execution Flow: Calculation and Methodology ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) for calculating the execution flow.
It is the presence of KK that allows the eigenvalues to describe contributions to the total P&L (rather than to daily changes),
which is a significant advantage for risk analysis.

Contrary to PCA, where the eigenvalues describe contributions to the variance of ff,
in ([50](https://arxiv.org/html/2511.01471v1#A3.E50 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) the eigenvalues describe contributions to the probability (with the density K​ψ[i]2​(𝐱)K{\psi^{[i]}}^{2}(\mathbf{x})),
were the P&L given by λ[i]\lambda^{[i]}.
This allows the expansion ([50](https://arxiv.org/html/2511.01471v1#A3.E50 "In Appendix C Christoffel Function Coverage Expansion ‣ Trade Execution Flow as the Underlying Source of Market Dynamics")) to separately study asymmetric factors that have positive and negative contributions.

## Appendix D Software Usage Description

The software [[12](https://arxiv.org/html/2511.01471v1#bib.bib12)] is written in Java.
The codebase is fairly large, but all code within the package com/polytechnik/trading/ –
which constitutes the largest part of it – represents our earlier,
less successful attempts and has since been converted into unit tests.
To test the provided software, install Java 25 or later.
Download the source code [[12](https://arxiv.org/html/2511.01471v1#bib.bib12)] from the archive
[AMuseOfCashFlowAndLiquidityDeficit.zip](http://www.ioffe.ru/LNEPS/malyshkin/AMuseOfCashFlowAndLiquidityDeficit.zip),
then decompress and recompile it:

```
unzip AMuseOfCashFlowAndLiquidityDeficit.zip
javac -g com/polytechnik/*/*java
```

Then run the software using the sample data located in the dataexamples/ directory.
Here, we use the backslash “\\backslash” to split lines to fit the two-column PRE format;
BASH interprets it correctly, allowing the commands to be copied directly from the article into the BASH prompt.

```
java com/polytechnik/algorithms/TestCall_PdI \
 --musein_file=dataexamples/aapl_old.csv.gz \
 --musein_cols=9:1:2:3 \
 --n=12 \
 --tau=128 \
 --measure=CommonlyUsedMomentsLegendreShifted \
 --museout_file=/tmp/museout_PdI_128_12.dat
```

and

```
java com/polytechnik/algorithms/TestCall_PdI \
 --musein_file=dataexamples/\
taq_AAPL_20250401.csv.gz \
 --musein_cols=4:1:2:3 \
 --n=12 \
 --tau=128 \
 --measure=CommonlyUsedMomentsLegendreShifted \
 --museout_file=/tmp/mo_PdI_128_12_taq.dat
```

The file specified with --museout\_file= contains the results.
The two generated files above include most of the results presented in this paper
and are obtained solely from data in the dataexamples/ directory.
For a general file from NYSE TAQ [[16](https://arxiv.org/html/2511.01471v1#bib.bib16)], one needs to create a `.csv`
file to use as input for --musein\_file=.
Original daily TAQ files from NYSE are typically not time-sorted; to create a time-sorted file, run:

```
com/polytechnik/taq/sort_taq_file.sh orig_TAQ.gz
```

The script sort\_taq\_file.sh sorts the TAQ records chronologically.
The script may need to be edited to adjust the temporary directory,
as the generated files are large and a temp directory of over 10Gb is required.
The name of the generated file is printed to stdout upon script completion.
The resulting sorted file (we recommend compressing and renaming it to sorted\_NYSE\_TAQ\_file.gz)
contains all TAQ transactions in chronological order. These “sorted” files,
converted from the original TAQ data, can be downloaded from
<https://mega.nz/folder/uORjRboa#bnNJnMt0bQRMkgLvhf5Xuw>.
Next, the data must be filtered to extract only execution transactions for the required stocks. To do this, run:

```
java com/polytechnik/taq/\
TAQPrintOutput\$DumpTickersExe \
 sorted_NYSE_TAQ_file.gz \
 >/tmp/all_NYSE_TAQ.csv 2>/tmp/diag.cap
```

This script generates the file all\_NYSE\_TAQ.csv containing (ticker,time,price,shares) data,
which can be used with the code presented in this paper.
The file diag.cap contains stock trading volumes and traded capital;
it is required to select the instruments of interest and to verify that the calculated volumes
match those reported for that day, e.g., by [Yahoo Finance](https://finance.yahoo.com/).
If the output needs to be filtered for specific stocks, such as AAPL, add a stock filter list after the input filename.

```
java com/polytechnik/taq/\
TAQPrintOutput\$DumpTickersExe \
 sorted_NYSE_TAQ_file.gz AAPL \
 >/tmp/AAPL_NYSE_TAQ.csv 2>/tmp/diag.cap
```

The resulting four-column file, AAPL\_NYSE\_TAQ.csv,
can be used as demonstrated above.
It can be `gzip`-compressed for convenience. For some selected assets, pre-generated files are available at
<https://mega.nz/folder/uORjRboa#bnNJnMt0bQRMkgLvhf5Xuw>.
Thus, the conversion software of NYSE TAQ data to `.csv` format is tested for the latest version,
[TAQ v4.2](https://www.nyse.com/market-data/historical/daily-taq).

The creation of `.csv` files from the NASDAQ ITCH feed [[14](https://arxiv.org/html/2511.01471v1#bib.bib14)]
is described in Appendix A of Ref. [[7](https://arxiv.org/html/2511.01471v1#bib.bib7)].
Currently, only ITCH 4.1 is implemented; conversion for ITCH 5.0 is straightforward but has not yet been completed.

## References

* Polanyi [1957]
  K. Polanyi, Aristotle discovers the
  economy, [Trade and market in the early
  empires , 64 (1957)](https://archive.org/details/in.gov.ignca.36501).
* Walras [2013]
  L. Walras, [*Elements of pure economics: Or the theory of social wealth*](https://doi.org/10.4324/9781315888958) (Routledge, 2013).
* Donier and Bouchaud [2016]
  J. Donier and J.-P. Bouchaud, From Walras’
  auctioneer to continuous time double auctions: A general dynamic theory of
  supply and demand, [Journal of Statistical Mechanics:
  Theory and Experiment 2016, 123406 (2016)](https://doi.org/10.1088/1742-5468/aa4e8e).
* Malyshkin [2017]
  V. G. Malyshkin, Market Dynamics. On A
  Muse Of Cash Flow And Liquidity Deficit, ArXiv e-prints [10.48550/arXiv.1709.06759](https://doi.org/10.48550/arXiv.1709.06759)
  (2017), [arXiv:1709.06759 [q-fin.TR]](https://arxiv.org/abs/1709.06759) .
* Malyshkin [2019a]
  V. G. Malyshkin, Market Dynamics: On
  Directional Information Derived From (Time, Execution Price, Shares Traded)
  Transaction Sequences, arXiv
  preprint arXiv:1903.11530 [10.48550/arXiv.1903.11530](https://doi.org/10.48550/arXiv.1903.11530)
  (2019a).
* Malyshkin and Bakhramov [2015]
  V. G. Malyshkin and R. Bakhramov, Mathematical
  Foundations of Realtime Equity Trading. Liquidity Deficit and Market
  Dynamics. Automated Trading Machines, arXiv preprint arXiv:1510.05510 [10.48550/arXiv.1510.05510](https://doi.org/10.48550/arXiv.1510.05510)
  (2015).
* Malyshkin [2016]
  V. G. Malyshkin, Market Dynamics. On
  Supply and Demand Concepts, [ArXiv e-prints (2016)](http://arxiv.org/abs/1602.04423), <http://arxiv.org/abs/1602.04423>, [arXiv:1602.04423](https://arxiv.org/abs/1602.04423) .
* Bucci *et al.* [2019]
  F. Bucci, M. Benzaquen,
  F. Lillo, and J.-P. Bouchaud, Crossover from linear to square-root market
  impact, [Physical review letters 122, 108302 (2019)](https://doi.org/10.1103/PhysRevLett.122.108302).
* Kearns and Ortiz [2003]
  M. Kearns and L. Ortiz, The Penn-Lehman automated trading
  project, [IEEE Intelligent systems 18, 22 (2003)](https://doi.org/10.1109/MIS.2003.1249166).
* LeBaron [2006]
  B. LeBaron, Agent-based
  computational finance, [Handbook of computational economics 2, 1187 (2006)](https://doi.org/10.1016/S1574-0021(05)02024-1).
* Chakole *et al.* [2021]
  J. B. Chakole, M. S. Kolhe,
  G. D. Mahapurush,
  A. Yadav, and M. P. Kurhekar, A Q-learning agent for automated trading in
  equity stock markets, [Expert Systems with
  Applications 163, 113761
  (2021)](https://doi.org/10.1016/j.eswa.2020.113761).
* Malyshkin [2014]
  V. G. Malyshkin, [The code for polynomials calculation](http://www.ioffe.ru/LNEPS/malyshkin/code.html) (2014), <http://www.ioffe.ru/LNEPS/malyshkin/code.html> and an
  [alternative
  location](https://disk.yandex.ru/d/AtPJ4a8copmZJ?locale=en).
* Malyshkin and Belov [2022]
  V. G. Malyshkin and M. G. Belov, Market Directional
  Information Derived From (Time, Execution Price, Shares Traded) Sequence of
  Transactions. On The Impact From The Future, arXiv preprint arXiv:2210.04223 [10.48550/arXiv.2210.04223](https://doi.org/10.48550/arXiv.2210.04223)
  (2022).
* Nasdaq OMX [2014]
  Nasdaq OMX, [*NASDAQ TotalView-ITCH 4.1*](http://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/nqtv-itch-v4_1.pdf), Report (Nasdaq OMX, 2014) see sample data files at <https://emi.nasdaq.com/ITCH/>
  and newest version specification
  [TotalView-ITCH
  5.0](https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/NQTVITCHSpecification.pdf) .
* Hautsch and Huang [2011]
  N. Hautsch and R. Huang, [Limit order flow, market impact and optimal order sizes: Evidence
  from nasdaq totalview-itch data](http://sfb649.wiwi.hu-berlin.de/papers/pdf/SFB649DP2011-056.pdf) (2011).
* NYSE [2025]
  NYSE, [*Daily TAQ Client Spec v4.2*](https://www.nyse.com/market-data/historical/daily-taq), Report (NYSE, 2025) see sample data files at
  <https://ftp.nyse.com/Historical%20Data%20Samples/DAILY%20TAQ/>, which
  provide two days of free data every quarter.
* Totik [2005]
  V. Totik, Orthogonal Polynomials, [Surveys in Approximation Theory 1, 70 (11 Nov. 2005)](https://doi.org/10.48550/arXiv.math/0512424).
* Malyshkin [2019b]
  V. G. Malyshkin, On The Radon-Nikodym
  Spectral Approach With Optimal Clustering, arXiv preprint arXiv:1906.00460 [10.48550/arXiv.1906.00460](https://doi.org/10.48550/arXiv.1906.00460)
  (2019b).
* Lasserre and Pauwels [2019]
  J.-B. Lasserre and E. Pauwels, The empirical
  Christoffel function with applications in data analysis, [Advances in Computational Mathematics , 1
  (2019)](https://doi.org/10.1007/s10444-019-09673-1).
* Lasserre [2022]
  J. B. Lasserre, A disintegration of the
  Christoffel function, [Comptes Rendus.
  Mathématique 360, 1071 (2022)](https://doi.org/10.5802/crmath.380).
* Lasserre [2009]
  J.-B. Lasserre, [*Moments, positive polynomials and their applications*](https://doi.org/10.1142/p665), Vol. 1 (World Scientific, 2009).
* Malyshkin [2018]
  V. G. Malyshkin, On Lebesgue Integral
  Quadrature, arXiv preprint
  arXiv:1807.06007 [10.48550/arXiv.1807.06007](https://doi.org/10.48550/arXiv.1807.06007) (2018).