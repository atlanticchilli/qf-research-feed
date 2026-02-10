---
authors:
- Hongjian Wang
- Shubhada Agrawal
- Aaditya Ramdas
doc_id: arxiv:2602.08888v1
family_id: arxiv:2602.08888
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Almost sure null bankruptcy of testing-by-betting strategies
url_abs: http://arxiv.org/abs/2602.08888v1
url_html: https://arxiv.org/html/2602.08888v1
venue: arXiv q-fin
version: 1
year: 2026
---


Hongjian Wang
Carnegie Mellon University [hjnwang@cmu.edu](mailto:hjnwang@cmu.edu)

Shubhada Agrawal
Indian Institute of Science [shubhada@iisc.ac.in](mailto:shubhada@iisc.ac.in)

Aaditya Ramdas
Carnegie Mellon University [aramdas@cmu.edu](mailto:aramdas@cmu.edu)

(February 9, 2026)

###### Abstract

The bounded mean betting procedure serves as a crucial interface between the domains of (1) sequential, anytime-valid statistical inference, and (2) online learning and portfolio selection algorithms. While recent work in both domains has established the exponential wealth growth of numerous betting strategies under any alternative distribution, the tightness of the inverted confidence sets, and the pathwise minimax regret bounds, little has been studied regarding the asymptotics of these strategies under the null hypothesis. Under the null, a strategy
induces a wealth martingale converging to some random variable that can be zero (bankrupt) or non-zero (non-bankrupt, e.g. when it eventually stops betting).
In this paper, we show the conceptually intuitive but technically nontrivial fact that these strategies (universal portfolio, Krichevsky-Trofimov, GRAPA, hedging, etc.) all go bankrupt with probability one, under any non-degenerate null distribution. Part of our analysis is based on the subtle almost sure divergence of various sums of ∑Op​(n−1)\sum O\_{p}(n^{-1}) type,
a result of independent interest.
We also demonstrate the necessity of null bankruptcy by showing that non-bankrupt strategies are all improvable in some sense.
Our results significantly deepen our understanding of these betting strategies as they qualify their behavior on “almost all paths”, whereas previous results are usually on “all paths” (e.g. regret bounds) or “most paths” (e.g. concentration inequalities and confidence sets).

## 1 Introduction

We consider the problem of testing the mean of i.i.d. random variables taking values in [0,1][0,1] via betting, studied by various authors including Shafer and Vovk [[2005](https://arxiv.org/html/2602.08888v1#bib.bib24 "Probability and finance: it’s only a game!"), [2019](https://arxiv.org/html/2602.08888v1#bib.bib30 "Game-theoretic foundations for probability and finance")], Shafer [[2021](https://arxiv.org/html/2602.08888v1#bib.bib111 "Testing by betting: a strategy for statistical and scientific communication")], Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")], Orabona and Jun [[2023](https://arxiv.org/html/2602.08888v1#bib.bib107 "Tight concentrations and confidence sequences from the regret of universal portfolio")], Voracek and Orabona [[2025](https://arxiv.org/html/2602.08888v1#bib.bib110 "STAR-bets: sequential TArget-recalculating bets for tighter confidence intervals")]. Let (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P where PP is some distribution on [0,1][0,1] with unknown mean μ​(P)=𝔼​X1∈[0,1]\mu(P)=\mathbb{E}X\_{1}\in[0,1], and let the null hypothesis be H0:μ​(P)=mH\_{0}:\mu(P)=m. To set the stage for our upcoming discourse, we recall that the *betting wealth process* that sequentially tests H0H\_{0} with
a *fixed* bet fraction λ∈[−11−m,1m]\lambda\in[-\frac{1}{1-m},\frac{1}{m}] is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wnλ:=∏k=1n(1+λ​(Xk−m)).W\_{n}^{\lambda}:=\prod\_{k=1}^{n}(1+\lambda(X\_{k}-m)). |  | (1) |

(Wnλ)(W\_{n}^{\lambda}) is interpreted as follows. The statistician starts with unit wealth, and bets round by round on the outcomes of X1,X2,…X\_{1},X\_{2},\dots, where x∈ℝx\in\mathbb{R} units of bet on XkX\_{k} placed before the revelation of XkX\_{k} leads to x⋅(Xk−m)x\cdot(X\_{k}-m) units of profit (if positive) or loss (if negative). Each round, the statistician bets a fixed fraction λ\lambda of the current wealth.
WnλW\_{n}^{\lambda} is therefore the statistician’s wealth after nn such rounds. Clearly, (Wnλ)(W^{\lambda}\_{n}) forms
a nonnegative martingale under any distribution PP on [0,1][0,1] that satisfies the null H0:μ​(P)=mH\_{0}:\mu(P)=m (“null distribution” henceforth). Therefore, a key doctrine of game-theoretic statistics [Ramdas et al., [2023](https://arxiv.org/html/2602.08888v1#bib.bib31 "Game-theoretic statistics and safe anytime-valid inference")] states that (Wnλ)(W^{\lambda}\_{n}) quantifies the accumulation of evidence carried by the observations (Xn)(X\_{n}) against the null hypothesis H0:μ​(P)=mH\_{0}:\mu(P)=m in favor of the alternative hypothesis H1:μ​(P)≠mH\_{1}:\mu(P)\neq m.

The fixed-fraction betting strategy ([1](https://arxiv.org/html/2602.08888v1#S1.E1 "Equation 1 ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")), however, fails to be universally powerful in the sense that there always exists some alternative distribution (i.e. PP such that μ​(P)≠m\mu(P)\neq m) under which Wnλ→0W\_{n}^{\lambda}\to 0 almost surely. To see that, when λ>0\lambda>0, under any non-degenerate PP such that μ​(P)<m\mu(P)<m, log⁡Wnλ⩽∑k=1nλ​(Xk−m)→−∞\log W\_{n}^{\lambda}\leqslant\sum\_{k=1}^{n}\lambda(X\_{k}-m)\to-\infty and consequently Wnλ→0W\_{n}^{\lambda}\to 0. To overcome this, three (overlapping) classes of betting strategies derived from ([1](https://arxiv.org/html/2602.08888v1#S1.E1 "Equation 1 ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) are
commonly employed.

##### Predictable plug-in.

Let 𝝀=(λn)n⩾1\boldsymbol{\lambda}=(\lambda\_{n})\_{n\geqslant 1} be a [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}]-valued stochastic process that is predictable with respect to the filtration σ​(X1,…,Xn)\sigma(X\_{1},\dots,X\_{n}). The wealth process corresponding to betting λk\lambda\_{k} fraction of wealth on the upcoming XkX\_{k} reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn𝝀:=∏k=1n(1+λk​(Xk−m)).W\_{n}^{\boldsymbol{\lambda}}:=\prod\_{k=1}^{n}(1+\lambda\_{k}(X\_{k}-m)). |  | (2) |

(Wn𝝀)(W\_{n}^{\boldsymbol{\lambda}}) remains a nonnegative martingale under H0H\_{0}. Usually, the value of λn\lambda\_{n} is picked based on X1,…,Xn−1X\_{1},\dots,X\_{n-1} to match the sign of the “reality-house discrepancy” μ​(P)−m\mu(P)-m. The simplest idea is to use the empirical mean of X1−m,…,Xn−1−mX\_{1}-m,\dots,X\_{n-1}-m, leading to the Krichevsky-Trofimov-type (KT) bettor [Krichevsky and Trofimov, [1981](https://arxiv.org/html/2602.08888v1#bib.bib116 "The performance of universal encoding"), Orabona and Pál, [2016](https://arxiv.org/html/2602.08888v1#bib.bib43 "Coin betting and parameter-free online learning")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λn𝖪𝖳:=1/2+∑k=1n−1(Xk−m)C​n,\lambda^{\mathsf{KT}}\_{n}:=\frac{1/2+\sum\_{k=1}^{n-1}(X\_{k}-m)}{Cn}, |  | (3) |

where C⩾m​(1−m)C\geqslant{m(1-m)} is an appropriate constant.
The (standard) KT bettor with C=m​(1−m)C={m(1-m)} estimates μ​(P)−mm​(1−m)\frac{\mu(P)-m}{m(1-m)}, which in the binary coin-toss case X1∼P=bernoulli⁡(μ​(P))X\_{1}\sim P=\operatorname{bernoulli}(\mu(P)) equals the *Kelly-optimal* bet fraction

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ𝖪𝖾𝗅𝗅𝗒=arg​maxλ∈[−11−m,1m]⁡{𝔼P​(log⁡(1+λ​(X1−m)))}\lambda^{\mathsf{Kelly}}=\operatorname\*{arg\,max}\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}\bigg\{\mathbb{E}\_{P}(\log(1+\lambda(X\_{1}-m)))\bigg\} |  | (4) |

maximizing the expected log-payoff per round. In general for non-Bernoulli PP, ([4](https://arxiv.org/html/2602.08888v1#S1.E4 "Equation 4 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) can be estimated instead by its natural M-estimator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λn𝖦𝖱𝖠𝖯𝖠:=arg​maxλ∈[−11−m,1m]⁡{1n−1​∑k=1n−1log⁡(1+λ​(Xk−m))}=arg​maxλ∈[−11−m,1m]⁡Wn−1λ.\lambda^{\mathsf{GRAPA}}\_{n}:=\operatorname\*{arg\,max}\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}\left\{\frac{1}{n-1}\sum\_{k=1}^{n-1}\log(1+\lambda(X\_{k}-m))\right\}=\operatorname\*{arg\,max}\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}W\_{n-1}^{\lambda}. |  | (5) |

That is, λn𝖦𝖱𝖠𝖯𝖠\lambda^{\mathsf{GRAPA}}\_{n} is the hindsight optimal fixed bet fraction after n−1n-1 rounds (a.k.a. “follow-the-leader”), and is therefore named the “growth rate adaptive to the particular alternative” (GRAPA) bettor by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")]. GRAPA requires an optimization procedure that may be computationally undesirable, therefore Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")] also propose the approximate GRAPA (aGRAPA) bettor, which we discuss later.

The method of predictable plugin betting ([2](https://arxiv.org/html/2602.08888v1#S1.E2 "Equation 2 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) is the widest class of testing by betting strategies, among which we name KT and GRAPA here and include the additional aGRAPA in [Section 2.3](https://arxiv.org/html/2602.08888v1#S2.SS3 "2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"). The other two classes of betting strategies are both subclasses of predictable plugin betting. In fact, Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting"), Proposition 2] prove that *all* nonnegative martingales under H0:μ​(P)=mH\_{0}:\mu(P)=m are representable by ([2](https://arxiv.org/html/2602.08888v1#S1.E2 "Equation 2 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) for some predictable sequence (λn)(\lambda\_{n}). Nonetheless, we introduce the other two classes of betting strategies, since it is often easier to analyze the property of a betting strategy if it falls in to one of these two subclasses.

##### Mixture.

Let π\pi be a probability measure on [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}]. The wealth process corresponding to the portfolio consisting of the (possibly continuous) collection of different fixed-fraction bets {(Wnλ):λ∈supp⁡(π)}\{(W\_{n}^{\lambda}):\lambda\in\operatorname{supp}(\pi)\}, weighted by λ∼π\lambda\sim\pi, is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wnπ:=∫Wnλ​π​(d​λ)=∫{∏k=1n(1+λ​(Xk−μ))}​π​(d​λ).W\_{n}^{\pi}:=\int W\_{n}^{\lambda}\,\pi(\mathrm{d}\lambda)=\int\left\{\prod\_{k=1}^{n}(1+\lambda(X\_{k}-\mu))\right\}\pi(\mathrm{d}\lambda). |  | (6) |

It is easy to verify that the mixture wealth ([6](https://arxiv.org/html/2602.08888v1#S1.E6 "Equation 6 ‣ Mixture. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) can be represented as an instance of predictable plug-in ([2](https://arxiv.org/html/2602.08888v1#S1.E2 "Equation 2 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) with the predictable fraction sequence λkπ=∫λ​Wk−1λ​π​(d​λ)∫Wk−1λ​π​(d​λ)\lambda\_{k}^{\pi}=\frac{\int\lambda W\_{k-1}^{\lambda}\pi(\mathrm{d}\lambda)}{\int W\_{k-1}^{\lambda}\pi(\mathrm{d}\lambda)}, and is also a nonnegative martingale under H0H\_{0}.
Some choices of mixture measure π\pi that are continuously supported on [−1,1][-1,1] trace back to Robbins [[1970](https://arxiv.org/html/2602.08888v1#bib.bib77 "Statistical methods related to the law of the iterated logarithm")] in the context of subGaussian mean testing, as well as to Cover [[1991](https://arxiv.org/html/2602.08888v1#bib.bib94 "Universal portfolios")], Cover and Ordentlich [[2002](https://arxiv.org/html/2602.08888v1#bib.bib97 "Universal portfolios with side information")] in the context of portfolio selection (“universal portfolios”). Via these mixture measures, Orabona and Jun [[2023](https://arxiv.org/html/2602.08888v1#bib.bib107 "Tight concentrations and confidence sequences from the regret of universal portfolio")] establish a link from regret bounds to confidence sequences for μ​(P)\mu(P); and
we shall soon see that the specific expressions of these measures do not matter for our current paper.

##### Predictable hedging.

Finally, there is a class of strategies that resemble in form both predictable plug-in and mixture. Let 𝝀=(λn)\boldsymbol{\lambda}=(\lambda\_{n}) be a [0,min⁡(11−m,1m))[0,\min(\frac{1}{1-m},\frac{1}{m}))-valued predictable process. The hedged betting wealth process based on 𝝀\boldsymbol{\lambda} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn±𝝀:=12​∏k=1n(1+λk​(Xk−m))+12​∏k=1n(1−λk​(Xk−m)),W\_{n}^{\pm\boldsymbol{\lambda}}:=\frac{1}{2}\prod\_{k=1}^{n}(1+\lambda\_{k}(X\_{k}-m))+\frac{1}{2}\prod\_{k=1}^{n}(1-\lambda\_{k}(X\_{k}-m)), |  | (7) |

and is also a nonnegative martingale under H0H\_{0}.
That is, one takes a two-point mixture among the strategies Wn𝝀W\_{n}^{\boldsymbol{\lambda}} and Wn−𝝀W\_{n}^{-\boldsymbol{\lambda}}. The fraction sequence 𝝀\boldsymbol{\lambda} here is often taken at the decreasing rate λn≍n−1/2\lambda\_{n}\asymp n^{-1/2} or (n​log⁡n)−1/2(n\log n)^{-1/2}, choices demonstrated by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")], Shekhar and Ramdas [[2023](https://arxiv.org/html/2602.08888v1#bib.bib100 "On the near-optimality of betting confidence sets for bounded means")] to enable optimal (1−α)(1-\alpha)-confidence sets for μ​(P)\mu(P). A specific choice recommended by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting"), Equation (26)] reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | λn𝖯𝗋𝖧=(−C1−m)∨2​log⁡(2/α)σ^n−12​n​log⁡(n+1)∧Cm,\lambda\_{n}^{\mathsf{PrH}}=\left(-\frac{C}{1-m}\right)\vee\sqrt{\frac{2\log(2/\alpha)}{\widehat{\sigma}\_{n-1}^{2}n\log(n+1)}}\wedge\frac{C}{m}, |  | (8) |

where σ^n−12\widehat{\sigma}\_{n-1}^{2} is an appropriate consistent variance estimator from X1,…,Xn−1X\_{1},\dots,X\_{n-1}, and C∈(0,1)C\in(0,1) some clipping constant.

Many variations of these betting strategies exist.
To quote from Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")],
“each of these betting strategies have their respective benefits, whether computational, conceptual, or
statistical”. We refer the reader to the original work by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")] and Orabona and Jun [[2023](https://arxiv.org/html/2602.08888v1#bib.bib107 "Tight concentrations and confidence sequences from the regret of universal portfolio")] as well as the papers cited therein for more discussions on betting strategies for the bounded mean problem.

A crucial shared property that separates all these involved strategies from the naïve fixed-fraction strategy ([1](https://arxiv.org/html/2602.08888v1#S1.E1 "Equation 1 ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) is that they are all *universally power-one*. That is, for *any* alternative distribution PP (i.e. PP on [0,1][0,1] with mean μ​(P)≠m\mu(P)\neq m), the wealth process (Wn)(W\_{n}) of these strategies always grows to infinitely almost surely: P​(Wn→∞)=1P(W\_{n}\to\infty)=1.
Very often, the wealth growth happens almost surely at an exponential rate: P​(lim infn−1​log⁡Wn>0)=1P(\liminf n^{-1}\log W\_{n}>0)=1. Indeed, it is not hard to see that the KT bettor with C=2C=2, the GRAPA bettor, and the mixture bettor with continuous π\pi on [−1,1][-1,1] are all exponentially powerful in this sense.

Additionally, as is frequently alluded to in our introduction to them, many of these strategies are adapted from the online learning and portfolio selection literature where there is neither hypothesis testing framework nor probability distribution assumed on the observation sequence (Xn)(X\_{n}); they enjoy sharp pathwise regret bounds Rn:=supλ(log⁡Wnλ)−log⁡WnR\_{n}:=\sup\_{\lambda}(\log W\_{n}^{\lambda})-\log W\_{n} at the rate of Rn≲log⁡nR\_{n}\lesssim\log n on *every* sample path (Xn)∈[0,1]∞(X\_{n})\in[0,1]^{\infty}. Many, on the other hand, lead to (1−α)(1-\alpha)-confidence sequences for μ​(P)\mu(P) by inversion CIn={m:Wn​(m)⩽1/α}\operatorname{CI}\_{n}=\{m:W\_{n}(m)\leqslant 1/\alpha\} (where Wn​(m)W\_{n}(m) is the wealth testing H0:μ​(P)=mH\_{0}:\mu(P)=m) of optimal size.

The key contribution of our current paper is that, these well-designed betting strategies which oftentimes enjoy exponential almost sure growth rates under alternative distributions, or logarithmic regret bounds in the pathwise sense, or minimax optimal confidence sequences under inversion, would *all fall into bankruptcy with probability one under any non-degenerate null distribution*.
That is, as long as μ​(P)=m\mu(P)=m and PP is not a point mass at mm,

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Wn→0)=1P(W\_{n}\to 0)=1 |  | (9) |

for all these wealth processes (Wn)(W\_{n}). Further, we demonstrate that the null bankruptcy phenomenon ([9](https://arxiv.org/html/2602.08888v1#S1.E9 "Equation 9 ‣ Predictable hedging. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) does *not* happen on some suboptimal variants of these betting strategies, which suggests that null bankruptcy is a fundamental property of “good” strategies.

Our results that P​(Wn→0)=1P(W\_{n}\to 0)=1 under any non-degenerate null PP complete the picture regarding the behavior of these betting strategies in the asymptotic regime, complementary to the fact that P​(Wn→∞)=1P(W\_{n}\to\infty)=1 under any alternative PP mentioned earlier. They also deepen our prior understanding of these wealth processes under the null: we previously were only aware of the fact that (Wn)(W\_{n}) is a nonnegative martingale under any null PP, and therefore (1) it must converge a.s. to *some random variable*, and (2) it satisfies the nonasymptotic Ville’s inequality P​(supWn<x)⩾1−x−1P(\sup W\_{n}<x)\geqslant 1-x^{-1}, i.e. it is unlikely to accumulate wealth more than xx, *for xx (much) larger than 1*.

The null bankruptcy of the simple and less powerful fixed-fraction betting strategy ([1](https://arxiv.org/html/2602.08888v1#S1.E1 "Equation 1 ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")), we note, is well-understood and known as the “gambler’s ruin” in elementary probability textbooks. The null bankruptcy of these involved, power-one, pathwise minimal-regret strategies that we prove in this paper, in contrary, requires applying and devising of some insightful results in asymptotic probability, and oftentimes happens much more subtly. At the end of this paper, we also
show that strategies that do not go bankrupt under the null are all “improvable” in some sense.

##### Notation.

We shall frequently employ the asymptotic notations in its both pathwise and in-probability usages. Let (Xn)(X\_{n}) be a sequence of random variables and (an)(a\_{n}) a sequence of nonrandom positive numbers. We say Xn=Oa.s.​(an)X\_{n}=O\_{a.s.}(a\_{n}) etc. if the pathwise event Xn=O​(an)X\_{n}=O(a\_{n}) happens with probability 1.
We recall Xn=Op​(an)X\_{n}=O\_{p}(a\_{n}) if for any ε>0\varepsilon>0, there exists M>0M>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|Xn|⩽M​an)⩾1−εfor all but finitely many ​n.\mathbb{P}(|X\_{n}|\leqslant Ma\_{n})\geqslant 1-\varepsilon\quad\text{for all but finitely many }n. |  | (10) |

Similarly, we say Xn=Ωp​(an)X\_{n}=\Omega\_{p}(a\_{n}) if for any ε>0\varepsilon>0 there exists δ>0\delta>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|Xn|⩾δ​an)⩾1−εfor all but finitely many ​n.\mathbb{P}(|X\_{n}|\geqslant\delta a\_{n})\geqslant 1-\varepsilon\quad\text{for all but finitely many }n. |  | (11) |

It is well-known that if (Xn)(X\_{n}) converges weakly to some distribution, Xn=Op​(1)X\_{n}=O\_{p}(1); and if to some distribution that does not charge 0 with positive probability, Xn=Ωp​(1)X\_{n}=\Omega\_{p}(1). The sample mean of i.i.d. random variables with positive and finite variance is both Op​(n−1/2)O\_{p}(n^{-1/2}) and Ωp​(n−1/2)\Omega\_{p}(n^{-1/2}), but neither Oa.s.​(n−1/2)O\_{a.s.}(n^{-1/2}) nor Ωa.s.​(n−1/2)\Omega\_{a.s.}(n^{-1/2}).

We use the symbols ℙ​(⋅)\mathbb{P}(\cdot) and 𝔼​(⋅)\mathbb{E}(\cdot) to denote probability and expected value in a generic context; we use P​(⋅)P(\cdot) and 𝔼P​(⋅)\mathbb{E}\_{P}(\cdot) for probability and expected value when specifically (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P.

##### Additional related work.

A few other categories of recent research are surveyed in [Appendix A](https://arxiv.org/html/2602.08888v1#A1 "Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"), including (1) subGaussian and sub-ψ\psi test processes; (2) the contrasts among “all”, “PP-almost all”, and “PP-most” paths, and between “always” and “eventually” valid statements; (3) past papers that occasionally mention or hint at null bankruptcy.

## 2 Bankruptcy of predictable plug-in and hedging

### 2.1 Necessary and sufficient condition for null bankruptcy

Our first theoretical contribution is that we identify the necessary and sufficient condition for the null bankruptcy *event* (and consequently for this event to happen almost surely) of any predictable plugin betting strategy. As we cited earlier from Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")], all nonnegative martingales are some predictable plugin betting strategy, this completely characterizes the null bankruptcy behavior of all these processes.
The following result states that,
under any non-degenerate null PP, bankruptcy happens exactly on the sample paths where the sum of squares of the bet fractions ∑λn2\sum\lambda\_{n}^{2} diverges, and sample paths where an “all-in bet” loses all current wealth, up to a PP-negligible set.

###### Theorem 2.1 (Sum-of-squares criterion).

Let PP be a non-degenerate distribution on [0,1][0,1] with mean mm and (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P.
Let 𝛌=(λn)\boldsymbol{\lambda}=(\lambda\_{n}) be a predictable process taking values in [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}].
Then, the 𝛌\boldsymbol{\lambda}-betting wealth process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn𝝀=∏k=1n(1+λk​(Xk−m))W\_{n}^{\boldsymbol{\lambda}}=\prod\_{k=1}^{n}(1+\lambda\_{k}(X\_{k}-m)) |  | (12) |

converges almost surely to a random variable W∞W\_{\infty} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | {W∞=0}={∑n=1∞λn2=∞}∪⋃n=1∞{λn​(Xn−m)=−1}\{W\_{\infty}=0\}=\left\{\sum\_{n=1}^{\infty}\lambda\_{n}^{2}=\infty\right\}\cup\bigcup\_{n=1}^{\infty}\{\lambda\_{n}(X\_{n}-m)=-1\} |  | (13) |

and consequently

|  |  |  |  |
| --- | --- | --- | --- |
|  | {W∞>0}={∑n=1∞λn2<∞}∩⋂n=1∞{λn​(Xn−m)>−1}.\{W\_{\infty}>0\}=\left\{\sum\_{n=1}^{\infty}\lambda\_{n}^{2}<\infty\right\}\cap\bigcap\_{n=1}^{\infty}\{\lambda\_{n}(X\_{n}-m)>-1\}. |  | (14) |

We prove [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") in [Section B.1](https://arxiv.org/html/2602.08888v1#A2.SS1 "B.1 Proof of Theorem 2.1 (sum-of-squares criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"), using martingale convergence and divergence characterizations found in Hall and Heyde [[2014](https://arxiv.org/html/2602.08888v1#bib.bib118 "Martingale limit theory and its application")], Fitzsimmons [[2005](https://arxiv.org/html/2602.08888v1#bib.bib117 "SLLN for Martingales")].
Note that the event {λn​(Xn−m)=−1}\{\lambda\_{n}(X\_{n}-m)=-1\} only happens when both the bet fraction and the observation take extreme values:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {λn​(Xn−m)=−1}={λn=−11−m,Xn=1}∪{λn=1m,Xn=0}\{\lambda\_{n}(X\_{n}-m)=-1\}=\left\{\lambda\_{n}=-\frac{1}{1-m},X\_{n}=1\right\}\cup\left\{\lambda\_{n}=\frac{1}{m},X\_{n}=0\right\} |  | (15) |

thus losing all current wealth.
We also note that Ramdas et al. [[2020](https://arxiv.org/html/2602.08888v1#bib.bib93 "Admissible anytime-valid sequential inference must rely on nonnegative martingales"), Lemma 33] also prove a sufficient condition for martingale bankruptcy, which, in this case, states that P​(∑k=1∞λk2​(Xk−m)2=∞)=1P(\sum\_{k=1}^{\infty}\lambda\_{k}^{2}(X\_{k}-m)^{2}=\infty)=1 implies P​(Wn𝝀→0)=1P(W\_{n}^{\boldsymbol{\lambda}}\to 0)=1. It is easy to see that our [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") implies their result, because ∑k=1∞λk2​(Xk−m)2=∞\sum\_{k=1}^{\infty}\lambda\_{k}^{2}(X\_{k}-m)^{2}=\infty implies ∑k=1∞λk2=∞\sum\_{k=1}^{\infty}\lambda\_{k}^{2}=\infty, due to the boundedness (Xk−m)2⩽1(X\_{k}-m)^{2}\leqslant 1.
Let us demonstrate in the following subsections that [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") facilitates the bankruptcy analysis of various betting strategies with explicit (λn)(\lambda\_{n}) expression.

### 2.2 Almost sure divergence of ∑Ωp​(n−1)\sum\Omega\_{p}(n^{-1})

Consider for a moment the simplest predictable plug-in betting strategy, the KT bettor ([3](https://arxiv.org/html/2602.08888v1#S1.E3 "Equation 3 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")).
From [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"), it is clear that KT ([3](https://arxiv.org/html/2602.08888v1#S1.E3 "Equation 3 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) with any CC is null-bankrupt if and only if the sum ∑Sn2/n2\sum S\_{n}^{2}/n^{2} diverges, where SnS\_{n} is the sum of nn i.i.d. mean-zero random variables X1−m,…,Xn−mX\_{1}-m,\dots,X\_{n}-m. From the central limit theorem, we know that Sn/n=Ωp​(n−1/2)S\_{n}/n=\Omega\_{p}(n^{-1/2}), and therefore this sum is of the form ∑Ωp​(n−1)\sum\Omega\_{p}(n^{-1}).

However, we were unable to locate existing work on the divergence of either the specific sum ∑Sn2/n2\sum S\_{n}^{2}/n^{2}, or the general sums of form ∑Ωp​(n−1)\sum\Omega\_{p}(n^{-1}), even though these, at first sight, seem elementary problems. In particular, as we shall discuss soon, the law of the iterated logarithm (LIL) does *not* imply ∑Sn2/n2=∞\sum S\_{n}^{2}/n^{2}=\infty almost surely. On the other hand, it is tempting to conjecture that, unlike ∑Ωa.s.​(n−1)=∞\sum\Omega\_{a.s.}(n^{-1})=\infty, the event ∑Ωp​(n−1)=∞\sum\Omega\_{p}(n^{-1})=\infty does not necessarily happen almost surely, in light of various textbook counterexamples where convergence in probability does not imply convergence almost surely. Nevertheless, in the following theorem, we defy this conventional wisdom and assert that ∑Ωp​(n−1)=∞\sum\Omega\_{p}(n^{-1})=\infty always happens almost surely.

###### Theorem 2.2.

Let (Zn)(Z\_{n}) be a nonnegative sequence of random variables such that Zn=Ωp​(n−1)Z\_{n}=\Omega\_{p}(n^{-1}). Then, ℙ​(∑n=1∞Zn=∞)=1\mathbb{P}(\sum\_{n=1}^{\infty}Z\_{n}=\infty)=1.

The proof of [Theorem 2.2](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.2 Almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)} ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"), a result arguably of independent interest, is in [Section B.2](https://arxiv.org/html/2602.08888v1#A2.SS2 "B.2 Proof of Theorem 2.2 (almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)}) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies").
We can immediately apply the theorem to Zn=Sn2/n2=Ωp​(n−1)Z\_{n}=S\_{n}^{2}/n^{2}=\Omega\_{p}(n^{-1}) due to the central limit theorem. This special case, we believe, also deserves its separate attention and dissemination to the broader audience due to its simple form but not-that-simple proof. We therefore write it down separately.

###### Corollary 2.3.

Let Y1,Y2,…Y\_{1},Y\_{2},\dots be i.i.d. random variables with mean 0 and variance σ2>0\sigma^{2}>0 and Sn=Y1+⋯+YnS\_{n}=Y\_{1}+\dots+Y\_{n}.
Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=1∞Sn2n2=∞almost surely.\sum\_{n=1}^{\infty}\frac{S\_{n}^{2}}{n^{2}}=\infty\quad\text{almost surely}. |  | (16) |

We point out that an invalid “one-line” proof attempt of [Corollary 2.3](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.2 Almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)} ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") is the following: via the law of the iterated logarithm (LIL), |Sn|≍n​log⁡log⁡n|S\_{n}|\asymp\sqrt{n\log\log n} almost surely, and therefore ∑Sn2/n2≍∑n−1​log⁡log⁡n=∞\sum S\_{n}^{2}/n^{2}\asymp\sum n^{-1}\log\log n=\infty. The pitfall, we note, is that LIL only ensures that a *subsequence* (nk)(n\_{k}) with Snk=Ωa.s.​(nk​log⁡log⁡nk)S\_{n\_{k}}=\Omega\_{a.s.}(\sqrt{n\_{k}\log\log n\_{k}}), and ∑knk−1​log⁡log⁡nk\sum\_{k}n\_{k}^{-1}\log\log n\_{k} may converge if this subsequence (nk)(n\_{k}) is “sparse” (e.g. nk=k2n\_{k}=k^{2}). On the contrary, our statement is based conceptually on the fact that sample sizes nn such that Zn≍1/nZ\_{n}\asymp 1/n occupy a non-sparse subset among natural numbers: if one looks at the proof, the inclusions ([44](https://arxiv.org/html/2602.08888v1#A2.E44 "Equation 44 ‣ Proof. ‣ B.2 Proof of Theorem 2.2 (almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)}) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")), ([45](https://arxiv.org/html/2602.08888v1#A2.E45 "Equation 45 ‣ Proof. ‣ B.2 Proof of Theorem 2.2 (almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)}) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) state that ∑Zn\sum Z\_{n} converges only when, as nn grows, the number of events Ak={Zk⩾δ/k}A\_{k}=\{Z\_{k}\geqslant\delta/k\} among 1⩽k⩽n1\leqslant k\leqslant n happen grows sublinearly, which, we later show, is of low probability. This fact is not captured by LIL. Finally, an alternative proof of [Corollary 2.3](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.2 Almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)} ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") based on Donsker’s invariance principle is provided in [Section B.3](https://arxiv.org/html/2602.08888v1#A2.SS3 "B.3 Divergence of ∑{𝑆_𝑛²/𝑛²} via Donsker’s invariance principle ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies").

### 2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc.

The combination of [Theorems 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") and [2.2](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.2 Almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)} ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") leads to the following sufficient condition for bankruptcy. Namely, almost sure null bankruptcy happens if the bet fractions (λn)(\lambda\_{n}) have a decay rate Ωp​(n−1/2)\Omega\_{p}(n^{-1/2}) or Ωa.s.​((n​log⁡n)−1/2)\Omega\_{a.s.}((n\log n)^{-1/2}) under the null.

###### Corollary 2.4 (n−1/2n^{-1/2} criterion).

Let PP be a non-degenerate distribution on [0,1][0,1] with mean mm and (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P. Let 𝛌=(λn)\boldsymbol{\lambda}=(\lambda\_{n}) be a predictable process taking values in [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}].
Suppose that either λn=Ωp​(n−1/2)\lambda\_{n}=\Omega\_{p}(n^{-1/2}) or λn=Ωa.s.​((n​log⁡n)−1/2)\lambda\_{n}=\Omega\_{a.s.}((n\log n)^{-1/2}) under PP.
Then, the 𝛌\boldsymbol{\lambda}-betting wealth process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn𝝀=∏k=1n(1+λk​(Xk−m))W\_{n}^{\boldsymbol{\lambda}}=\prod\_{k=1}^{n}(1+\lambda\_{k}(X\_{k}-m)) |  | (17) |

converges almost surely to 0.

λn=Ωp​(n−1/2)\lambda\_{n}=\Omega\_{p}(n^{-1/2}) and λn=Ωa.s.​((n​log⁡n)−1/2)\lambda\_{n}=\Omega\_{a.s.}((n\log n)^{-1/2}) are two very different conditions and neither implies the other.
Various predictable plug-in betting and hedging strategies mentioned in [Section 1](https://arxiv.org/html/2602.08888v1#S1 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies") and by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")] fall into this category. First, the standard CLT for the sample mean immediately implies the following bankruptcy for KT.

###### Proposition 2.5.

Let (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P with mean mm and variance σ2>0\sigma^{2}>0. The KT bet fractions λn𝖪𝖳\lambda^{\mathsf{KT}}\_{n} defined in ([3](https://arxiv.org/html/2602.08888v1#S1.E3 "Equation 3 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) satisfies the asymptotic normality

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​λn𝖪𝖳=1/2+∑k=1n−1(Xk−m)C​n⟶weakly𝒩​(0,C−2​σ2).\sqrt{n}\lambda^{\mathsf{KT}}\_{n}=\frac{1/2+\sum\_{k=1}^{n-1}(X\_{k}-m)}{C\sqrt{n}}\stackrel{{\scriptstyle\text{weakly}}}{{\longrightarrow}}\mathcal{N}(0,C^{-2}\sigma^{2}). |  | (18) |

Therefore λn𝖪𝖳=Ωp​(n−1/2)\lambda^{\mathsf{KT}}\_{n}=\Omega\_{p}(n^{-1/2}), and consequently the KT wealth process ∏k=1n(1+λk𝖪𝖳​(Xk−m))\prod\_{k=1}^{n}(1+\lambda^{\mathsf{KT}}\_{k}(X\_{k}-m)) converges to 0 almost surely.

Second, GRAPA ([5](https://arxiv.org/html/2602.08888v1#S1.E5 "Equation 5 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) is almost sure null-bankrupt because, as a standard M-estimator, the GRAPA bet fractions (λn𝖦𝖱𝖠𝖯𝖠)(\lambda^{\mathsf{GRAPA}}\_{n}) also satisfy asymptotic normality and an Ω​(n−1/2)\Omega(n^{-1/2}) decay rate under any non-degenerate null.

###### Proposition 2.6.

Let (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P with mean mm and variance σ2>0\sigma^{2}>0.
The GRAPA bet fraction λn𝖦𝖱𝖠𝖯𝖠\lambda^{\mathsf{GRAPA}}\_{n} defined in ([5](https://arxiv.org/html/2602.08888v1#S1.E5 "Equation 5 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) satisfies the almost sure Bahadur expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​λn+1𝖦𝖱𝖠𝖯𝖠=1σ2⋅∑k=1n(Xk−m)n+oa.s.​(n−1/4​log⁡n)⟶weakly𝒩​(0,σ−2).\sqrt{n}\lambda^{\mathsf{GRAPA}}\_{n+1}=\frac{1}{\sigma^{2}}\cdot\frac{\sum\_{k=1}^{n}(X\_{k}-m)}{\sqrt{n}}+o\_{a.s.}(n^{-1/4}\log n)\stackrel{{\scriptstyle\text{weakly}}}{{\longrightarrow}}\mathcal{N}(0,\sigma^{-2}). |  | (19) |

Therefore λn𝖦𝖱𝖠𝖯𝖠=Ωp​(n−1/2)\lambda^{\mathsf{GRAPA}}\_{n}=\Omega\_{p}(n^{-1/2}), and consequently the GRAPA wealth process ∏k=1n(1+λk𝖦𝖱𝖠𝖯𝖠​(Xk−m))\prod\_{k=1}^{n}(1+\lambda^{\mathsf{GRAPA}}\_{k}(X\_{k}-m)) converges to 0 almost surely.

The proof of [Proposition 2.6](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem6 "Proposition 2.6. ‣ 2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") involves checking that the M-estimation problem for λ↦𝔼P​(log⁡(1+λ​(X1−m)))\lambda\mapsto\mathbb{E}\_{P}(\log(1+\lambda(X\_{1}-m))) satisfies all of the seven regularity conditions for the Bahadur expansion result of M-estimators due to Niemiro [[1992](https://arxiv.org/html/2602.08888v1#bib.bib123 "Asymptotics for M-estimators defined by convex minimization")]. We put these details in [Section B.4](https://arxiv.org/html/2602.08888v1#A2.SS4 "B.4 Proof of Proposition 2.6 (Bahadur expansion of GRAPA/KL_inf bet fractions) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"). As a quick sanity check of these two asymptotics, we note that KT with C=m​(1−m)=σ2C=m(1-m)=\sigma^{2} coincides with GRAPA in the Bernoulli coin-toss case (see e.g. Orabona and Pál [[2016](https://arxiv.org/html/2602.08888v1#bib.bib43 "Coin betting and parameter-free online learning"), Section 4]).

Next, the approximate GRAPA (aGRAPA) bettor by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting"), Section B.3] reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | λn𝖺𝖦𝖱𝖠𝖯𝖠=(−C1−m)∨μ^n−1−mσ^n−12+(μ^n−1−m)2∧Cm,\lambda^{\mathsf{aGRAPA}}\_{n}=\left(-\frac{C}{1-m}\right)\vee\frac{\widehat{\mu}\_{n-1}-m}{\widehat{\sigma}^{2}\_{n-1}+(\widehat{\mu}\_{n-1}-m)^{2}}\wedge\frac{C}{m}, |  | (20) |

where μ^n−1\widehat{\mu}\_{n-1} and σ^n−12\widehat{\sigma}^{2}\_{n-1} are the sample mean and variance of X1,…,Xn−1X\_{1},\dots,X\_{n-1}, and C∈(0,1)C\in(0,1) a clipping constant (cf. the null Bahadur expansion of GRAPA ([19](https://arxiv.org/html/2602.08888v1#S2.E19 "Equation 19 ‣ Proposition 2.6. ‣ 2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"))). The consistency of these estimators as well as the standard CLT immediately give rise to its asymptotic normality similar to that of KT and GRAPA.

###### Proposition 2.7.

Let (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P with mean mm and variance σ2>0\sigma^{2}>0.
The aGRAPA bet fraction λn𝖺𝖦𝖱𝖠𝖯𝖠\lambda^{\mathsf{aGRAPA}}\_{n} defined above satisfies the asymptotic normality

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​λn𝖺𝖦𝖱𝖠𝖯𝖠⟶weakly𝒩​(0,σ−2).\sqrt{n}\lambda^{\mathsf{aGRAPA}}\_{n}\stackrel{{\scriptstyle\text{weakly}}}{{\longrightarrow}}\mathcal{N}(0,\sigma^{-2}). |  | (21) |

Therefore λn𝖺𝖦𝖱𝖠𝖯𝖠=Ωp​(n−1/2)\lambda^{\mathsf{aGRAPA}}\_{n}=\Omega\_{p}(n^{-1/2}), and the aGRAPA wealth process ∏k=1n(1+λk𝖺𝖦𝖱𝖠𝖯𝖠​(Xk−m))\prod\_{k=1}^{n}(1+\lambda^{\mathsf{aGRAPA}}\_{k}(X\_{k}-m)) converges to 0 almost surely.

Finally, predictable hedging betting strategies of form ([7](https://arxiv.org/html/2602.08888v1#S1.E7 "Equation 7 ‣ Predictable hedging. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")), proposed on grounds of tightness of the implied confidence sequences (as opposed to wealth growth), are also almost surely null-bankrupt as λn\lambda\_{n} is set to always be Ωa.s.​(n−1/2)\Omega\_{a.s.}(n^{-1/2}) or Ωa.s.​((n​log⁡n)−1/2)\Omega\_{a.s.}((n\log n)^{-1/2}), regardless of null or alternative.

###### Proposition 2.8.

Let (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P with mean mm and variance σ2>0\sigma^{2}>0.
Let λn𝖯𝗋𝖧\lambda\_{n}^{\mathsf{PrH}} be the bet fraction defined in ([8](https://arxiv.org/html/2602.08888v1#S1.E8 "Equation 8 ‣ Predictable hedging. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")).
Then, λn𝖯𝗋𝖧=Ωa.s.​((n​log⁡n)−1/2)\lambda\_{n}^{\mathsf{PrH}}=\Omega\_{a.s.}((n\log n)^{-1/2}), and consequently the hedged wealth process 0.5⋅∏k=1n(1+λk𝖯𝗋𝖧​(Xk−m))+0.5⋅∏k=1n(1−λk𝖯𝗋𝖧​(Xk−m))0.5\cdot\prod\_{k=1}^{n}(1+\lambda\_{k}^{\mathsf{PrH}}(X\_{k}-m))+0.5\cdot\prod\_{k=1}^{n}(1-\lambda\_{k}^{\mathsf{PrH}}(X\_{k}-m)) converges to 0 almost surely.

As a short summary of this section, we have shown that many of the proposed “good” betting strategies are null-bankrupt almost surely via the sum-of-square criterion, [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"). It is natural to ask if there are “equally good” strategies that do not go bankrupt. We delay this profound question to [Section 4](https://arxiv.org/html/2602.08888v1#S4 "4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies"), after discussing mixture strategies among which the question has a much clearer answer.

## 3 Bankruptcy of mixture strategies

We next study the null bankruptcy behavior of mixture strategies ([6](https://arxiv.org/html/2602.08888v1#S1.E6 "Equation 6 ‣ Mixture. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")). While it is true that mixture strategies form a subclass of predictable plugin strategies via λkπ=∫λ​Wk−1λ​π​(d​λ)∫Wk−1λ​π​(d​λ)\lambda\_{k}^{\pi}=\frac{\int\lambda W\_{k-1}^{\lambda}\pi(\mathrm{d}\lambda)}{\int W\_{k-1}^{\lambda}\pi(\mathrm{d}\lambda)}, and therefore [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") implies the π\pi-mixture strategy bankrupts if and only if ∑(λkπ)2\sum(\lambda\_{k}^{\pi})^{2} diverges, we shall soon see that the bankruptcy of the mixture strategy is much easier to analyze directly via its native integration form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wnπ=∫Wnλ​π​(d​λ)=∫{∏k=1n(1+λ​(Xk−m))}​π​(d​λ).W\_{n}^{\pi}=\int W\_{n}^{\lambda}\,\pi(\mathrm{d}\lambda)=\int\left\{\prod\_{k=1}^{n}(1+\lambda(X\_{k}-m))\right\}\pi(\mathrm{d}\lambda). |  | (22) |

Specifically, the only condition that determines if a mixture strategy is null-bankrupt is whether the mixture distribution π\pi is an atom at 0 (i.e. it charges the set {0}\{0\} with a positive probability π​({0})>0\pi(\{0\})>0). Intuitively, if π\pi is an atom at 0, the mixture strategy always keeps some capital unwagered (“cash”), therefore it never goes bankrupt. The precise statement below is proved in [Section B.5](https://arxiv.org/html/2602.08888v1#A2.SS5 "B.5 Proof of Theorem 3.1 (no-cash criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies").

###### Theorem 3.1 (No-cash criterion).

Let PP be a non-degenerate distribution on [0,1][0,1] with mean mm and (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P.
Let π\pi be a probability measure on [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}]. Then, the mixture wealth (Wnπ)(W\_{n}^{\pi}) converges to π​({0})\pi(\{0\}) almost surely. In particular, W∞π=0W\_{\infty}^{\pi}=0 almost surely if and only if π\pi does not have an atom at 0, i.e. π​({0})=0\pi(\{0\})=0.

That is, any mixture betting strategy converges almost surely the fraction of the mixture assigned to λ=0\lambda=0. For any mixture distribution π\pi on [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}], we can decompose the π\pi-mixture strategy into its “cash component” π|{0}\pi|\_{\{0\}} and its “bet component” π|[−11−m,0)∪(0,1m]\pi|\_{[-\frac{1}{1-m},0)\cup(0,\frac{1}{m}]}, with the former staying constant and the latter going to bankruptcy.

In particular, the two mixtures employed by Orabona and Jun [[2023](https://arxiv.org/html/2602.08888v1#bib.bib107 "Tight concentrations and confidence sequences from the regret of universal portfolio")] are both continuous, thus atomless at 0, and are consequently null-bankrupt.

###### Proposition 3.2.

The universal portfolio betting strategy proposed by Orabona and Jun [[2023](https://arxiv.org/html/2602.08888v1#bib.bib107 "Tight concentrations and confidence sequences from the regret of universal portfolio"), Section 4], which corresponds to WnπW\_{n}^{\pi} where π\pi is a Beta distribution rescaled to [−1,1][-1,1], and the Robbins’ iterated logarithm betting strategy proposed by Orabona and Jun [[2023](https://arxiv.org/html/2602.08888v1#bib.bib107 "Tight concentrations and confidence sequences from the regret of universal portfolio"), Section 5], which corresponds to WnπW\_{n}^{\pi} where π\pi has density fπ​(λ)=𝟙{|λ|⩽1}​log⁡log⁡C2​|λ|​log⁡(C​|λ|)​(log⁡log⁡(C​|λ|))2f\_{\pi}(\lambda)=\frac{\mathbbmss{1}\_{\{|\lambda|\leqslant 1\}}\log\log C}{2|\lambda|\log(C|\lambda|)(\log\log(C|\lambda|))^{2}} where C=6.6​eC=6.6e, both converge to 0 almost surely under any non-degenerate null distribution.

We now revisit the question asked at the end of [Section 2](https://arxiv.org/html/2602.08888v1#S2 "2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"). Among mixture strategies, we know from [Theorem 3.1](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem1 "Theorem 3.1 (No-cash criterion). ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies") that null-bankrupt strategies are exactly those without the cash component π​({0})\pi(\{0\}). Given any null-non-bankrupt mixture strategy, its bet component π′=π|[−11−m,0)∪(0,1m]\pi^{\prime}=\pi|\_{[-\frac{1}{1-m},0)\cup(0,\frac{1}{m}]} yields a strictly more powerful, null-bankrupt strategy as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wnπ′=Wnπ−π​({0})1−π​({0})>WnπW^{\pi^{\prime}}\_{n}=\frac{W\_{n}^{\pi}-\pi(\{0\})}{1-\pi(\{0\})}>W\_{n}^{\pi} |  | (23) |

eventually on every sample path where Wnπ→∞W^{\pi}\_{n}\to\infty. In this sense, all good *mixture* betting strategies must be cash-free and go bankrupt almost surely under the null.

## 4 Do all good strategies go bankrupt?

While we demonstrated above that “good” mixture betting strategies are null-bankrupt, it remains to be answered if the same principle holds universally for all betting strategies.
Revisiting that argument around ([23](https://arxiv.org/html/2602.08888v1#S3.E23 "Equation 23 ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies")), given an original strategy MnπM\_{n}^{\pi}, we constructed another strategy Mnπ′M\_{n}^{\pi^{\prime}} that makes more money under the alternative, at the price of making less money (and possible bankruptcy) under the null; it *improves*
upon the original strategy MnπM\_{n}^{\pi} in this sense.

Our key result in this section is that it is possible to generalize the cash-removal improvement ([23](https://arxiv.org/html/2602.08888v1#S3.E23 "Equation 23 ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies")) to *all* strategies
on certain sample paths which we refer to as being “predictably non-bankrupt”. Let (Wn)(W\_{n}) be the wealth process of some strategy whose bet fraction process is (λn)(\lambda\_{n}). Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | W^n=minx∈[0,1]⁡Wn−1​(1+λn​(x−m))=min⁡{Wn−1​(1+λn​(0−m)),Wn−1​(1+λn​(1−m))}.\widehat{W}\_{n}=\min\_{x\in[0,1]}W\_{n-1}(1+\lambda\_{n}(x-m))=\min\{W\_{n-1}(1+\lambda\_{n}(0-m)),W\_{n-1}(1+\lambda\_{n}(1-m))\}. |  | (24) |

That is, W^n\widehat{W}\_{n} is the minimum possible wealth at time nn conditioned on the information available up to time n−1n-1. Therefore, it forms a predictable process. For ρ>0\rho>0, we define the *ρ\rho-predictably non-bankrupt* event as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nρ:=⋂n=1∞{W^n>ρ}.N^{\rho}:=\bigcap\_{n=1}^{\infty}\{\widehat{W}\_{n}>\rho\}. |  | (25) |

The event NρN^{\rho} says that it is always guaranteed that the next-round wealth cannot drop below ρ\rho. It implies wealth never *actually* drops below ρ\rho, and is implied by bet fraction being always small enough:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {|λn|<1−ρ​Wn−1−1}⊆{W^n>ρ}⊆{Wn>ρ}.\{|\lambda\_{n}|<1-\rho W\_{n-1}^{-1}\}\subseteq\{\widehat{W}\_{n}>\rho\}\subseteq\{W\_{n}>\rho\}. |  | (26) |

Clearly, for mixture strategies with cash component π​({0})⩾ρ\pi(\{0\})\geqslant\rho and non-degenerate bet component, the event NρN^{\rho} is the entire space. Our result below states that we can improve any strategy on the event NρN^{\rho}.

###### Theorem 4.1 (Improvability on predictably non-bankrupt paths).

Let (Wn)(W\_{n}) be the wealth process of some betting strategy, ρ∈(0,1)\rho\in(0,1), and NρN^{\rho} be its ρ\rho-predictably non-bankrupt event as defined in ([25](https://arxiv.org/html/2602.08888v1#S4.E25 "Equation 25 ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies")). There exists another betting strategy whose wealth process (Wn♯)(W\_{n}^{\sharp}) satisfies Wn♯=Wn−ρ1−ρW\_{n}^{\sharp}=\frac{W\_{n}-\rho}{1-\rho} on the event NρN^{\rho}. Consequently, on the event NρN^{\rho}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Wn>1}⊆{Wn♯>Wn},{Wn→∞}⊆{lim infWn♯/Wn=1/(1−ρ)>1};\displaystyle\{W\_{n}>1\}\subseteq\{W\_{n}^{\sharp}>W\_{n}\},\quad\{W\_{n}\to\infty\}\subseteq\{\liminf W\_{n}^{\sharp}/W\_{n}=1/(1-\rho)>1\}; |  | (27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | {Wn<1}⊆{Wn♯<Wn},{W∞<1}⊆{W∞♯=(W∞−ρ)/(1−ρ)<W∞}.\displaystyle\{W\_{n}<1\}\subseteq\{W\_{n}^{\sharp}<W\_{n}\},\quad\{W\_{\infty}<1\}\subseteq\{W\_{\infty}^{\sharp}=(W\_{\infty}-\rho)/(1-\rho)<W\_{\infty}\}. |  | (28) |

To summarize [Theorem 4.1](https://arxiv.org/html/2602.08888v1#S4.Thmtheorem1 "Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies") in a nutshell: when the original strategy is predictably non-bankrupt, the improvement strategy makes more money under the alternative ([27](https://arxiv.org/html/2602.08888v1#S4.E27 "Equation 27 ‣ Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies")), and loses more money under the null ([28](https://arxiv.org/html/2602.08888v1#S4.E28 "Equation 28 ‣ Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies")).
The intuition behind [Theorem 4.1](https://arxiv.org/html/2602.08888v1#S4.Thmtheorem1 "Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies") is the *borrowing* or *leveraging*
nature of the cash-removal improvement ([23](https://arxiv.org/html/2602.08888v1#S3.E23 "Equation 23 ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies")) for mixture strategies: the cash-removed strategy Wnπ′W\_{n}^{\pi^{\prime}} is equivalent to borrowing some cash and investing in a leveraged cash-holding strategy WnπW\_{n}^{\pi}. Analogously, the improvement strategy Wn♯W\_{n}^{\sharp} in [Theorem 4.1](https://arxiv.org/html/2602.08888v1#S4.Thmtheorem1 "Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies") is equivalent to leveraging the original strategy WnW\_{n} on NρN^{\rho}. The full roadmap to developing these concepts of borrowing, the construction of Wn♯W\_{n}^{\sharp}, as well as the proof of [Theorem 4.1](https://arxiv.org/html/2602.08888v1#S4.Thmtheorem1 "Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies") can all be found in [Section B.6](https://arxiv.org/html/2602.08888v1#A2.SS6 "B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies").

As we admitted, the predictably non-bankrupt event NρN^{\rho} is a subset of the actually non-bankrupt event ⋂n=1∞{Wn>ρ}\bigcap\_{n=1}^{\infty}\{W\_{n}>\rho\} (which must happen for some ρ\rho on a W∞>0W\_{\infty}>0 path). Therefore, there is still a narrow gap between our result above and the general question “do all good strategies go bankrupt”. We expect future work to close this gap.
We further our discussion on this intriguing question in [Appendix C](https://arxiv.org/html/2602.08888v1#A3 "Appendix C Further discussions on good strategies’ necessary bankruptcy ‣ Almost sure null bankruptcy of testing-by-betting strategies"), with examples and reasoning around (in fact, against) (1) whether exponentially powerful strategies are all null-bankrupt, (2) whether the Cramér-Rao bounds imply the necessary null-bankruptcy of some strategies.

## 5 Further discussions

### 5.1 Null asymptotics of KLinf\operatorname{KL}\_{\inf}

Let (Wn)(W\_{n}) be the wealth process of some betting strategy.
Much has been studied on the pathwise regret

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rn=maxλ∈[−11−m,1m]⁡(log⁡Wnλ)−log⁡Wn.R\_{n}=\max\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}(\log W\_{n}^{\lambda})-\log W\_{n}. |  | (29) |

Having showed that log⁡Wn→−∞\log W\_{n}\to-\infty on PP-almost all paths for non-degenerate null PP, and knowing that RnR\_{n} is usually O​(log⁡n)O(\log n) on *all* sample paths from the online learning literature (e.g. KT ([3](https://arxiv.org/html/2602.08888v1#S1.E3 "Equation 3 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) in the binary case [Orabona and Pál, [2016](https://arxiv.org/html/2602.08888v1#bib.bib43 "Coin betting and parameter-free online learning")], the two mixtures mentioned in [Proposition 3.2](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies")),
we now investigate the behavior of

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ln∗:=maxλ∈[−11−m,1m]⁡(log⁡Wnλ)=maxλ∈[−11−m,1m]​∑k=1nlog⁡(1+λ​(Xk−m)),L\_{n}^{\*}:=\max\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}(\log W\_{n}^{\lambda})=\max\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}\sum\_{k=1}^{n}\log(1+\lambda(X\_{k}-m)), |  | (30) |

the best-in-hindsight log-wealth, under the null.

It is worth noting that the quantity Ln∗L\_{n}^{\*}
is better known as being related to the KLinf\operatorname{KL}\_{\inf} statistic in the bandit literature. Many bandit methods [Agrawal, [2023](https://arxiv.org/html/2602.08888v1#bib.bib9 "Bandits with heavy tails: algorithms analysis and optimality")] are derived from controlling KLinf⁡(Pn,m)\operatorname{KL}\_{\inf}(P\_{n},m)
where PnP\_{n} is the empirical measure and KLinf⁡(P,m)=min⁡{DKL​(P∥Q):Q​ on ​[0,1]​ with mean ​m}\operatorname{KL}\_{\inf}(P,m)=\min\{D\_{\operatorname{KL}}(P\|Q):Q\text{ on }[0,1]\text{ with mean }m\}.
Crucially, the KLinf\operatorname{KL}\_{\inf} statistic defined via this minimization is shown by Honda and Takemura [[2010](https://arxiv.org/html/2602.08888v1#bib.bib4 "An asymptotically optimal bandit algorithm for bounded support models.")] to have a dual representation that coincides with the hindsight maximum log-wealth, n​KLinf⁡(Pn,m)=Ln∗n\operatorname{KL}\_{\inf}(P\_{n},m)=L\_{n}^{\*}.
We thus denote λn𝖪𝖫=arg​maxλ∈[−11−m,1m]⁡Wnλ\lambda^{\mathsf{KL}}\_{n}=\operatorname\*{arg\,max}\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}W\_{n}^{\lambda}, and so Ln∗=Wnλn𝖪𝖫L\_{n}^{\*}=W\_{n}^{\lambda^{\mathsf{KL}}\_{n}}. Recalling the definition of GRAPA from ([5](https://arxiv.org/html/2602.08888v1#S1.E5 "Equation 5 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")), we see that λn+1𝖦𝖱𝖠𝖯𝖠=λn𝖪𝖫\lambda^{\mathsf{GRAPA}}\_{n+1}=\lambda^{\mathsf{KL}}\_{n}.

An *unconstrained* version of the hindsight maximum log-wealth,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ELn=supλ∑k=1nlog⁡(1+λ​(Xk−m)),\operatorname{EL}\_{n}=\sup\_{\lambda}\sum\_{k=1}^{n}\log(1+\lambda(X\_{k}-m)), |  | (31) |

where λ\lambda can take any value as long as the logarithms are all defined, on the other hand, has been studied in the concept of the empirical likelihood by Owen [[2001](https://arxiv.org/html/2602.08888v1#bib.bib114 "Empirical likelihood")] and the dual likelihood by Mykland [[1995](https://arxiv.org/html/2602.08888v1#bib.bib124 "Dual likelihood")]. See also the discussion by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting"), Section E.6]. These authors show that the unconstrained supremum ELn\operatorname{EL}\_{n} converges weakly to a χ(1)2\chi^{2}\_{(1)} limit. We note that as a well-behaved M-estimation procedure, adding the constraint λ∈[−11−m,1m]\lambda\in[-\frac{1}{1-m},\frac{1}{m}] does not alter its asymptotic behavior, so the same χ(1)2\chi^{2}\_{(1)} limit applies to the constrained maximum Ln∗L\_{n}^{\*} as well. We prove this fact formally in [Section B.7](https://arxiv.org/html/2602.08888v1#A2.SS7 "B.7 Proof of Theorem 5.1 (𝜒²₍₁₎ limit of KL_inf) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies") using the Bahadur expansion of the GRAPA/KLinf\operatorname{KL}\_{\inf} bet fractions λn+1𝖦𝖱𝖠𝖯𝖠=λn𝖪𝖫\lambda^{\mathsf{GRAPA}}\_{n+1}=\lambda^{\mathsf{KL}}\_{n} in [Proposition 2.6](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem6 "Proposition 2.6. ‣ 2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies").

###### Theorem 5.1.

Let PP be a non-degenerate distribution on [0,1][0,1] with mean mm and (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P. Then, twice the hindsight maximum log-wealth

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​Ln∗=2​maxλ∈[−11−m,1m]⁡log⁡Wnλ=2​∑k=1nlog⁡(1+λn𝖪𝖫​(Xk−m))2L^{\*}\_{n}=2\max\_{\lambda\in[-\frac{1}{1-m},\frac{1}{m}]}\log W\_{n}^{\lambda}=2\sum\_{k=1}^{n}\log(1+\lambda^{\mathsf{KL}}\_{n}(X\_{k}-m)) |  | (32) |

converges weakly to a χ2\chi^{2} distribution with 1 degree of freedom.
Consequently, a null-bankrupt strategy must have unbounded regret on PP-almost all paths:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Wn→0)=1⟹P​(sup(Ln∗−log⁡Wn)=∞)=1.P(W\_{n}\to 0)=1\implies P(\sup(L\_{n}^{\*}-\log W\_{n})=\infty)=1. |  | (33) |

The hindsight maximum wealth ∏k=1n(1+λn𝖪𝖫​(Xk−m))\prod\_{k=1}^{n}(1+\lambda^{\mathsf{KL}}\_{n}(X\_{k}-m)), therefore, converges weakly to exp⁡(Z2/2)\exp(Z^{2}/2) where Z∼𝒩​(0,1)Z\sim\mathcal{N}(0,1). We remark that this distribution is named the “standard critical log-chi-squared distribution” by Wang and Ramdas [[2025b](https://arxiv.org/html/2602.08888v1#bib.bib125 "The extended Ville’s inequality for nonintegrable nonnegative supermartingales"), Proposition 5.7], and has infinite expected value.
This is in contrast to the almost sure bankruptcy of the GRAPA wealth ∏k=1n(1+λk−1𝖪𝖫​(Xk−m))\prod\_{k=1}^{n}(1+\lambda^{\mathsf{KL}}\_{k-1}(X\_{k}-m)). These two have similar forms but have significantly different asymptotic behaviors, which is unsurprising: the hindsight maximum wealth is not a martingale, whereas the GRAPA wealth is.

### 5.2 Null bankruptcy in subGaussian and sub-ψ\psi testing

Counterparts of the divergence criteria [Theorems 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") and [3.1](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem1 "Theorem 3.1 (No-cash criterion). ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies") can also be established for the plug-in and mixture strategies based on the subGaussian test martingale

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mnλ=exp⁡(∑k=1n(Xk−m)2−(Xk−λ)22),M^{\lambda}\_{n}=\exp\left(\sum\_{k=1}^{n}\frac{(X\_{k}-m)^{2}-(X\_{k}-\lambda)^{2}}{2}\right), |  | (34) |

for which the online learning perspective is recently establish by Agrawal and Ramdas [[2026](https://arxiv.org/html/2602.08888v1#bib.bib119 "Eventually LIL regret: almost sure lnlnT regret for a sub-Gaussian mixture on unbounded data")]. See [Appendix A](https://arxiv.org/html/2602.08888v1#A1 "Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies") for a short introduction.

###### Theorem 5.2 (Sum-of-squares criterion II).

Let PP be a non-degenerate 1-subGaussian distribution with mean mm and (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P.
Let 𝛌=(λn)\boldsymbol{\lambda}=(\lambda\_{n}) be a predictable process taking values in ℝ\mathbb{R}.
Then, the 𝛌\boldsymbol{\lambda}-plugin test process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mn𝝀=exp⁡(∑k=1n(Xk−m)2−(Xk−λk)22)M\_{n}^{\boldsymbol{\lambda}}=\exp\left(\sum\_{k=1}^{n}\frac{(X\_{k}-m)^{2}-(X\_{k}-\lambda\_{k})^{2}}{2}\right) |  | (35) |

converges almost surely to a random variable W∞W\_{\infty} satisfying

|  |  |  |
| --- | --- | --- |
|  | {M∞=0}={∑n=1∞(λn−m)2=∞}, and consequently ​{M∞>0}={∑n=1∞(λn−m)2<∞}.\{M\_{\infty}=0\}=\left\{\sum\_{n=1}^{\infty}(\lambda\_{n}-m)^{2}=\infty\right\},\text{\; and consequently \;}\{M\_{\infty}>0\}=\left\{\sum\_{n=1}^{\infty}(\lambda\_{n}-m)^{2}<\infty\right\}. |  |

###### Theorem 5.3 (No-cash criterion II).

Let PP be a non-degenerate 1-subGaussian distribution with mean mm and (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P. Let π\pi be a probability measure on ℝ\mathbb{R}.
Then, the π\pi-mixture test process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mnπ=∫exp⁡(∑k=1n(Xk−m)2−(Xk−λ)22)​π​(d​λ)M\_{n}^{\pi}=\int\exp\left(\sum\_{k=1}^{n}\frac{(X\_{k}-m)^{2}-(X\_{k}-\lambda)^{2}}{2}\right)\pi(\mathrm{d}\lambda) |  | (36) |

converges almost surely to π​({m})\pi(\{m\}).

Both theorems above are proved in [Section B.8](https://arxiv.org/html/2602.08888v1#A2.SS8 "B.8 Proofs of the subGaussian criteria, Theorems 5.2 and 5.3 ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies").
Finally, there is a generalization of the subGaussian mean testing martingale ([38](https://arxiv.org/html/2602.08888v1#A1.E38 "Equation 38 ‣ SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies")) for the general *sub-ψ\psi* random variables. See e.g. Howard et al. [[2020](https://arxiv.org/html/2602.08888v1#bib.bib69 "Time-uniform Chernoff bounds via nonnegative supermartingales"), [2021](https://arxiv.org/html/2602.08888v1#bib.bib68 "Time-uniform, nonparametric, nonasymptotic confidence sequences")] for an introduction. In the sub-ψ\psi case, the process ([34](https://arxiv.org/html/2602.08888v1#S5.E34 "Equation 34 ‣ 5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies")) (taking m=0m=0 for simplicity)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mn𝝀=exp⁡{∑k=1n(λ​Xk−12​λ2)}becomesexp⁡{∑k=1n(λ​Xk−ψ​(λ))}M\_{n}^{\boldsymbol{\lambda}}=\exp\left\{\sum\_{k=1}^{n}\left(\lambda X\_{k}-\frac{1}{2}\lambda^{2}\right)\right\}\quad\text{becomes}\quad\exp\left\{\sum\_{k=1}^{n}\left(\lambda X\_{k}-\psi(\lambda)\right)\right\} |  | (37) |

where ψ​(⋅)\psi(\cdot) is a function that locally behaves like ψ​(x)≈x22\psi(x)\approx\frac{x^{2}}{2} for x≈0x\approx 0. Therefore, one may prove similar sum-of-squares and no cash criteria for these testing strategies. We omit these straightforward extensions from our paper.

## 6 Conclusion

Many successful betting strategies for the bounded mean testing problem converge almost surely to zero wealth under all non-degenerate null distributions, and we provided some preliminary insight that this principle may apply more broadly to all betting strategies that satisfy some growth condition.
We also discussed the null asymptotic χ2\chi^{2} distribution of the hindsight maximum wealth (KLinf\operatorname{KL}\_{\inf}); and presented the analogous bankruptcy results for the unbounded (sub-ψ\psi) test martingales.
Our results are complementary to numerous results on the regret, null maximal concentration, and confidence sets corresponding to these strategies.

#### Acknowledgments

AR was funded by NSF grant DMS-2310718.

## References

* S. Agrawal and A. Ramdas (2026)
  Eventually LIL regret: almost sure ln⁡ln⁡T\ln\ln T regret for a sub-Gaussian mixture on unbounded data.
  Algorithmic Learning Theory.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px2.p1.13 "All vs. 𝑃-almost all vs. 𝑃-most paths; always vs. eventually valid. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§5.2](https://arxiv.org/html/2602.08888v1#S5.SS2.p1.2 "5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* S. Agrawal (2023)
  Bandits with heavy tails: algorithms analysis and optimality.
  Ph.D. Thesis, Tata Institute of Fundamental Research, (English).
  External Links: [Link](http://hdl.handle.net/10603/478863)
  Cited by: [§5.1](https://arxiv.org/html/2602.08888v1#S5.SS1.p2.10 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* T. M. Cover and E. Ordentlich (2002)
  Universal portfolios with side information.
  IEEE Transactions on Information Theory 42 (2),  pp. 348–363.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px2.p1.13 "All vs. 𝑃-almost all vs. 𝑃-most paths; always vs. eventually valid. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px2.p1.9 "Mixture. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* T. M. Cover (1991)
  Universal portfolios.
  Mathematical finance 1 (1),  pp. 1–29.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px2.p1.13 "All vs. 𝑃-almost all vs. 𝑃-most paths; always vs. eventually valid. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px2.p1.9 "Mixture. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* P. J. Fitzsimmons (2005)
  SLLN for Martingales.
  Note: Lecture handout of Probability Theory (Math 280B) taught at the University of California, San Diego in Winter 2005
  External Links: [Link](https://mathweb.ucsd.edu/~pfitz/downloads/courses/winter05/math280b/martslln.pdf)
  Cited by: [§B.1](https://arxiv.org/html/2602.08888v1#A2.SS1.2.p2.13 "Proof. ‣ B.1 Proof of Theorem 2.1 (sum-of-squares criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§B.8](https://arxiv.org/html/2602.08888v1#A2.SS8.2.p2.2 "Proof. ‣ B.8 Proofs of the subGaussian criteria, Theorems 5.2 and 5.3 ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.1](https://arxiv.org/html/2602.08888v1#S2.SS1.p2.1 "2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* P. D. Grünwald (2023)
  The e-posterior.
  Philosophical Transactions of the Royal Society A 381 (2247),  pp. 20220146.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px3.p1.1 "Other work on null-bankrupt test processes. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* P. Hall and C. C. Heyde (2014)
  Martingale limit theory and its application.
   Academic press.
  Cited by: [§B.1](https://arxiv.org/html/2602.08888v1#A2.SS1.2.p2.13 "Proof. ‣ B.1 Proof of Theorem 2.1 (sum-of-squares criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§B.1](https://arxiv.org/html/2602.08888v1#A2.SS1.3.p3.13 "Proof. ‣ B.1 Proof of Theorem 2.1 (sum-of-squares criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§B.8](https://arxiv.org/html/2602.08888v1#A2.SS8.1.p1.5 "Proof. ‣ B.8 Proofs of the subGaussian criteria, Theorems 5.2 and 5.3 ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.1](https://arxiv.org/html/2602.08888v1#S2.SS1.p2.1 "2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* J. Honda and A. Takemura (2010)
  An asymptotically optimal bandit algorithm for bounded support models..
  In Conference on Learning Theory,
   pp. 67–79.
  Cited by: [§5.1](https://arxiv.org/html/2602.08888v1#S5.SS1.p2.10 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* S. R. Howard, A. Ramdas, J. McAuliffe, and J. Sekhon (2020)
  Time-uniform Chernoff bounds via nonnegative supermartingales.
  Probability Surveys.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px1.p1.19 "SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px1.p1.8 "SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px2.p1.13 "All vs. 𝑃-almost all vs. 𝑃-most paths; always vs. eventually valid. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§5.2](https://arxiv.org/html/2602.08888v1#S5.SS2.p2.3 "5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* S. R. Howard, A. Ramdas, J. Mcauliffe, and J. Sekhon (2021)
  Time-uniform, nonparametric, nonasymptotic confidence sequences.
  The Annals of Statistics 49 (2),  pp. 1055–1080.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px1.p1.8 "SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§5.2](https://arxiv.org/html/2602.08888v1#S5.SS2.p2.3 "5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* R. Krichevsky and V. Trofimov (1981)
  The performance of universal encoding.
  IEEE Transactions on Information Theory 27 (2),  pp. 199–207.
  Cited by: [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px1.p1.11 "Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* P. A. Mykland (1995)
  Dual likelihood.
  The Annals of Statistics,  pp. 396–421.
  Cited by: [§5.1](https://arxiv.org/html/2602.08888v1#S5.SS1.p3.8 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* W. Niemiro (1992)
  Asymptotics for M-estimators defined by convex minimization.
  The Annals of Statistics,  pp. 1514–1533.
  Cited by: [§B.4](https://arxiv.org/html/2602.08888v1#A2.SS4.3.p2.5 "Proof. ‣ B.4 Proof of Proposition 2.6 (Bahadur expansion of GRAPA/KL_inf bet fractions) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§B.4](https://arxiv.org/html/2602.08888v1#A2.SS4.4.p3.4 "Proof. ‣ B.4 Proof of Proposition 2.6 (Bahadur expansion of GRAPA/KL_inf bet fractions) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.3](https://arxiv.org/html/2602.08888v1#S2.SS3.p4.2 "2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* F. Orabona and K. Jun (2023)
  Tight concentrations and confidence sequences from the regret of universal portfolio.
  IEEE Transactions on Information Theory.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px2.p1.13 "All vs. 𝑃-almost all vs. 𝑃-most paths; always vs. eventually valid. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px2.p1.9 "Mixture. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px3.p2.1 "Predictable hedging. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.p1.8 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [Proposition 3.2](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem2.p1.7.7 "Proposition 3.2. ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§3](https://arxiv.org/html/2602.08888v1#S3.p3.1 "3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* F. Orabona and D. Pál (2016)
  Coin betting and parameter-free online learning.
  Advances in Neural Information Processing Systems 29.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px2.p1.13 "All vs. 𝑃-almost all vs. 𝑃-most paths; always vs. eventually valid. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px1.p1.11 "Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.3](https://arxiv.org/html/2602.08888v1#S2.SS3.p4.2 "2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§5.1](https://arxiv.org/html/2602.08888v1#S5.SS1.p1.6 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* A. B. Owen (2001)
  Empirical likelihood.
   Chapman and Hall/CRC.
  Cited by: [§5.1](https://arxiv.org/html/2602.08888v1#S5.SS1.p3.8 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* A. Ramdas, P. Grünwald, V. Vovk, and G. Shafer (2023)
  Game-theoretic statistics and safe anytime-valid inference.
  Statistical Science 38 (4),  pp. 576–601.
  Cited by: [§1](https://arxiv.org/html/2602.08888v1#S1.p1.25 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* A. Ramdas, J. Ruf, M. Larsson, and W. M. Koolen (2022)
  Testing exchangeability: fork-convexity, supermartingales and e-processes.
  International Journal of Approximate Reasoning 141,  pp. 83–109.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px3.p1.1 "Other work on null-bankrupt test processes. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* A. Ramdas, J. Ruf, M. Larsson, and W. Koolen (2020)
  Admissible anytime-valid sequential inference must rely on nonnegative martingales.
  arXiv:2009.03167.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px3.p1.1 "Other work on null-bankrupt test processes. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.1](https://arxiv.org/html/2602.08888v1#S2.SS1.p2.7 "2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* H. Robbins and D. Siegmund (1968)
  Iterated logarithm inequalities and related statistical procedures.
  Mathematics of the Decision Sciences 2,  pp. 267–279.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px1.p1.8 "SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* H. Robbins (1970)
  Statistical methods related to the law of the iterated logarithm.
  The Annals of Mathematical Statistics 41 (5),  pp. 1397–1409.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px1.p1.8 "SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px2.p1.9 "Mixture. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* G. Shafer and V. Vovk (2005)
  Probability and finance: it’s only a game!.
  Vol. 491, John Wiley & Sons.
  Cited by: [§1](https://arxiv.org/html/2602.08888v1#S1.p1.8 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* G. Shafer and V. Vovk (2019)
  Game-theoretic foundations for probability and finance.
   John Wiley & Sons.
  Cited by: [§1](https://arxiv.org/html/2602.08888v1#S1.p1.8 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* G. Shafer (2021)
  Testing by betting: a strategy for statistical and scientific communication.
  Journal of the Royal Statistical Society Series A: Statistics in Society 184 (2),  pp. 407–431.
  Cited by: [§1](https://arxiv.org/html/2602.08888v1#S1.p1.8 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* S. Shekhar and A. Ramdas (2023)
  On the near-optimality of betting confidence sets for bounded means.
  arXiv preprint arXiv:2310.01547.
  Cited by: [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px3.p1.11 "Predictable hedging. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* V. Voracek and F. Orabona (2025)
  STAR-bets: sequential TArget-recalculating bets for tighter confidence intervals.
  In The Thirty-ninth Annual Conference on Neural Information Processing Systems,
  External Links: [Link](https://openreview.net/forum?id=LHsQSC89Pt)
  Cited by: [§1](https://arxiv.org/html/2602.08888v1#S1.p1.8 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* H. Wang and A. Ramdas (2024)
  Testing by betting while borrowing and bargaining.
  arXiv preprint arXiv:2407.11465.
  Cited by: [Remark B.5](https://arxiv.org/html/2602.08888v1#A2.Thmtheorem5.p1.1.1 "Remark B.5. ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* H. Wang and A. Ramdas (2025a)
  Anytime-valid t-tests and confidence sequences for gaussian means with unknown variance.
  Sequential Analysis 44 (1),  pp. 56–110.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px3.p1.1 "Other work on null-bankrupt test processes. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* H. Wang and A. Ramdas (2025b)
  The extended Ville’s inequality for nonintegrable nonnegative supermartingales.
  Bernoulli 31 (4),  pp. 2723 – 2746.
  Cited by: [§5.1](https://arxiv.org/html/2602.08888v1#S5.SS1.p4.4 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").
* I. Waudby-Smith and A. Ramdas (2024)
  Estimating means of bounded random variables by betting.
  Journal of the Royal Statistical Society Series B: Statistical Methodology 86 (1),  pp. 1–27.
  Cited by: [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px2.p1.13 "All vs. 𝑃-almost all vs. 𝑃-most paths; always vs. eventually valid. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [Appendix A](https://arxiv.org/html/2602.08888v1#A1.SS0.SSS0.Px3.p1.1 "Other work on null-bankrupt test processes. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px1.p1.18 "Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px1.p2.2 "Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px3.p1.11 "Predictable hedging. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.SS0.SSS0.Px3.p2.1 "Predictable hedging. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§1](https://arxiv.org/html/2602.08888v1#S1.p1.8 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.1](https://arxiv.org/html/2602.08888v1#S2.SS1.p1.3 "2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.3](https://arxiv.org/html/2602.08888v1#S2.SS3.p2.2 "2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§2.3](https://arxiv.org/html/2602.08888v1#S2.SS3.p5.5 "2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
  [§5.1](https://arxiv.org/html/2602.08888v1#S5.SS1.p3.8 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies").

## Appendix A Additional related work

Our research on the null bankruptcy of bounded mean betting wealth processes is also related to the following topics.

##### SubGaussian and sub-ψ\psi mean testing.

Many of the betting strategies/wealth processes we mentioned in [Section 1](https://arxiv.org/html/2602.08888v1#S1 "1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies") have counterparts in the (equally) classic Gaussian, subGaussian [Robbins, [1970](https://arxiv.org/html/2602.08888v1#bib.bib77 "Statistical methods related to the law of the iterated logarithm"), Robbins and Siegmund, [1968](https://arxiv.org/html/2602.08888v1#bib.bib76 "Iterated logarithm inequalities and related statistical procedures")], and sub-ψ\psi [Howard et al., [2020](https://arxiv.org/html/2602.08888v1#bib.bib69 "Time-uniform Chernoff bounds via nonnegative supermartingales"), [2021](https://arxiv.org/html/2602.08888v1#bib.bib68 "Time-uniform, nonparametric, nonasymptotic confidence sequences")] mean testing literature.
Let (Xn)​∼iid​P(X\_{n})\overset{\mathrm{iid}}{\sim}P where PP is a subGaussian distribution on ℝ\mathbb{R} with variance factor 1 and unknown mean μ​(P)\mu(P). That is, 𝔼P​exp⁡(t​(X1−μ​(P)))⩽exp⁡(t2/2)\mathbb{E}\_{P}\exp(t(X\_{1}-\mu(P)))\leqslant\exp(t^{2}/2) for all t∈ℝt\in\mathbb{R}. The analogy of “fixed fraction bet” ([1](https://arxiv.org/html/2602.08888v1#S1.E1 "Equation 1 ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) testing the null μ​(P)=m\mu(P)=m is the likelihood ratio martingale

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mnλ=∏k=1np​(Xk;λ,1)p​(Xk;m,1)=exp⁡(∑k=1n(Xk−m)2−(Xk−λ)22),M^{\lambda}\_{n}=\prod\_{k=1}^{n}\frac{p(X\_{k};\lambda,1)}{p(X\_{k};m,1)}=\exp\left(\sum\_{k=1}^{n}\frac{(X\_{k}-m)^{2}-(X\_{k}-\lambda)^{2}}{2}\right), |  | (38) |

where p​(⋅;μ,σ2)p(\cdot;\mu,\sigma^{2}) is the probability density function of 𝒩​(μ,σ2)\mathcal{N}(\mu,\sigma^{2}).
Predictable plugin

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡(∑k=1n(Xk−m)2−(Xk−λk)22)\exp\left(\sum\_{k=1}^{n}\frac{(X\_{k}-m)^{2}-(X\_{k}-\lambda\_{k})^{2}}{2}\right) |  | (39) |

or mixture

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫exp⁡(∑k=1n(Xk−m)2−(Xk−λ)22)​π​(d​λ)\int\exp\left(\sum\_{k=1}^{n}\frac{(X\_{k}-m)^{2}-(X\_{k}-\lambda)^{2}}{2}\right)\pi(\mathrm{d}\lambda) |  | (40) |

test processes that achieve universal power compared to the constant λ\lambda are similarly available. More generally, we say PP is sub-ψ\psi with variance factor 1 if 𝔼P​exp⁡(t​(X1−μ​(P)))⩽exp⁡(ψ​(t))\mathbb{E}\_{P}\exp(t(X\_{1}-\mu(P)))\leqslant\exp(\psi(t)) for all t∈[0,tmax)t\in[0,t\_{\max}), where ψ\psi is usually a function satisfying ψ​(t)≈t2/2\psi(t)\approx t^{2}/2 when t→0t\to 0 [Howard et al., [2020](https://arxiv.org/html/2602.08888v1#bib.bib69 "Time-uniform Chernoff bounds via nonnegative supermartingales")]. The fixed-fraction test martingale testing the null μ​(P)=m\mu(P)=m is now

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡{∑k=1n((λ−m)​(Xk−m)−ψ​(λ−m))}.\exp\left\{\sum\_{k=1}^{n}\left((\lambda-m)(X\_{k}-m)-\psi(\lambda-m)\right)\right\}. |  | (41) |

When ψ​(t)=t2/2\psi(t)=t^{2}/2, ([41](https://arxiv.org/html/2602.08888v1#A1.E41 "Equation 41 ‣ SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies")) equals ([38](https://arxiv.org/html/2602.08888v1#A1.E38 "Equation 38 ‣ SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies")). Predictable plug-in and mixture are similarly available.
In [Section 5.2](https://arxiv.org/html/2602.08888v1#S5.SS2 "5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies"), we discuss the null bankruptcy of these processes too.

##### All vs. PP-almost all vs. PP-most paths; always vs. eventually valid.

We have mentioned a line of work either belonging to or inspired by the online learning and portfolio selection literature, notably that of Cover [[1991](https://arxiv.org/html/2602.08888v1#bib.bib94 "Universal portfolios")], Cover and Ordentlich [[2002](https://arxiv.org/html/2602.08888v1#bib.bib97 "Universal portfolios with side information")], Orabona and Pál [[2016](https://arxiv.org/html/2602.08888v1#bib.bib43 "Coin betting and parameter-free online learning")], Orabona and Jun [[2023](https://arxiv.org/html/2602.08888v1#bib.bib107 "Tight concentrations and confidence sequences from the regret of universal portfolio")]. Indeed, the betting process ([2](https://arxiv.org/html/2602.08888v1#S1.E2 "Equation 2 ‣ Predictable plug-in. ‣ 1 Introduction ‣ Almost sure null bankruptcy of testing-by-betting strategies")) is equivalent to the online prediction game with logarithmic loss, with the total accumulated loss being −log⁡Wn𝝀-\log W\_{n}^{\boldsymbol{\lambda}}. These authors usually prove regret bounds that characterize the *always-valid largeness* of (Wn)(W\_{n}) on *all* sample paths. The sequential inference literature [Howard et al., [2020](https://arxiv.org/html/2602.08888v1#bib.bib69 "Time-uniform Chernoff bounds via nonnegative supermartingales"), Waudby-Smith and Ramdas, [2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting")], on the other hand, draws heavily on the standard Ville’s inequality which characterizes the *always-valid smallness* of (Wn)(W\_{n}) on *PP-most* sample paths: sample paths where sup(Wn)⩽1/α\sup(W\_{n})\leqslant 1/\alpha is of PP measure at most 1−α1-\alpha.
Recently, Agrawal and Ramdas [[2026](https://arxiv.org/html/2602.08888v1#bib.bib119 "Eventually LIL regret: almost sure lnlnT regret for a sub-Gaussian mixture on unbounded data")] deliver some very novel findings on the regret bounds that apply to PP-most paths, not for the bounded betting game but for the *subGaussian* game ([38](https://arxiv.org/html/2602.08888v1#A1.E38 "Equation 38 ‣ SubGaussian and sub-𝜓 mean testing. ‣ Appendix A Additional related work ‣ Almost sure null bankruptcy of testing-by-betting strategies")). They reason that in the subGaussian regime with unbounded observations, (always-valid) regret bounds may only apply to PP-most paths.
We, on the other hand, primarily focus on the *eventual smallness* of (Wn)(W\_{n}) on *PP-almost all* sample paths. These sample paths constitute a larger set than a PP-most set, but a proper subset of all paths. Agrawal and Ramdas [[2026](https://arxiv.org/html/2602.08888v1#bib.bib119 "Eventually LIL regret: almost sure lnlnT regret for a sub-Gaussian mixture on unbounded data")] also notice that *eventual largeness* statements (asymptotic regret bounds) can be proved on a PP-almost all set of paths.

##### Other work on null-bankrupt test processes.

In the sequential statistics literature, many authors have proposed test processes that are nonnegative martingales, supermartingales, or e-processes under the null hypothesis, and mentioned along the way that these processes converge to 0 under (some) null distributions. These include Ramdas et al. [[2022](https://arxiv.org/html/2602.08888v1#bib.bib26 "Testing exchangeability: fork-convexity, supermartingales and e-processes"), Section 4.1] in the context of testing exchangeable bits, Wang and Ramdas [[2025a](https://arxiv.org/html/2602.08888v1#bib.bib120 "Anytime-valid t-tests and confidence sequences for gaussian means with unknown variance"), Table 3] in the context of mixture-based t-tests and Z-tests. A sufficient condition for martingale bankruptcy is proposed by Ramdas et al. [[2020](https://arxiv.org/html/2602.08888v1#bib.bib93 "Admissible anytime-valid sequential inference must rely on nonnegative martingales"), Lemma 33],
which we discussed
when presenting a more useful necessary and sufficient condition [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"). Finally, it is noted by Grünwald [[2023](https://arxiv.org/html/2602.08888v1#bib.bib121 "The e-posterior")] that test processes generalize the Bayesian prior-posterior ratio, and the null bankruptcy is therefore analogous to the concentration of posterior distribution towards the point mass on the ground truth, a concept visualized in passing in the bounded betting case by Waudby-Smith and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib61 "Estimating means of bounded random variables by betting"), Figure 18].

## Appendix B Omitted and additional proofs

### B.1 Proof of [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") (sum-of-squares criterion)

###### Proof.

Consider the process Sn=∑k=1nλk​(Xk−m)S\_{n}=\sum\_{k=1}^{n}\lambda\_{k}(X\_{k}-m), a square-integrable martingale with quadratic variation ⟨S⟩n=σ2​∑k=1nλk2\langle S\rangle\_{n}=\sigma^{2}\sum\_{k=1}^{n}\lambda\_{k}^{2} where σ2=𝐕𝐚𝐫​X1>0\sigma^{2}=\mathbf{Var}X\_{1}>0.

First, on the event {∑n=1∞λn2=∞}={⟨S⟩∞=∞}\{\sum\_{n=1}^{\infty}\lambda\_{n}^{2}=\infty\}=\{\langle S\rangle\_{\infty}=\infty\}, since 𝔼​(supn(Sn−Sn−1)2)⩽max⁡(m2/(1−m)2,(1−m)2/m2)<∞\mathbb{E}(\sup\_{n}(S\_{n}-S\_{n-1})^{2})\leqslant\max(m^{2}/(1-m)^{2},(1-m)^{2}/m^{2})<\infty, by Fitzsimmons [[2005](https://arxiv.org/html/2602.08888v1#bib.bib117 "SLLN for Martingales"), Theorem 2(b)], SnS\_{n} diverges almost surely. Further, on the event {Sn​ diverges}\{S\_{n}\text{ diverges}\}, since 𝔼​(supn|Sn−Sn−1|)<∞\mathbb{E}(\sup\_{n}|S\_{n}-S\_{n-1}|)<\infty, we learn from Hall and Heyde [[2014](https://arxiv.org/html/2602.08888v1#bib.bib118 "Martingale limit theory and its application"), Theorem 2.14] that lim infSn=−∞\liminf S\_{n}=-\infty almost surely. Because Wn𝝀⩽exp⁡(Sn)W\_{n}^{\boldsymbol{\lambda}}\leqslant\exp(S\_{n}), this further implies that lim infWn𝝀=0\liminf W\_{n}^{\boldsymbol{\lambda}}=0 a.s. on this event. Since WnW\_{n} is a nonnegative martingale, it converges a.s. on the entire probability space to some W∞W\_{\infty}, so we can take W∞W\_{\infty} such that W∞=limWn𝝀=lim infWn𝝀=0W\_{\infty}=\lim W\_{n}^{\boldsymbol{\lambda}}=\liminf W\_{n}^{\boldsymbol{\lambda}}=0 on {∑n=1∞λn2=∞}\{\sum\_{n=1}^{\infty}\lambda\_{n}^{2}=\infty\}.

Second, on the event {∑n=1∞λn2<∞}∩⋂n=1∞{λn​(Xn−m)>−1}\left\{\sum\_{n=1}^{\infty}\lambda\_{n}^{2}<\infty\right\}\cap\bigcap\_{n=1}^{\infty}\{\lambda\_{n}(X\_{n}-m)>-1\}, there exists a random finite sample size NN such that when n>Nn>N, |λn|⩽1/2|\lambda\_{n}|\leqslant 1/2. Using the inequality log⁡(1+x)⩾x−x2\log(1+x)\geqslant x-x^{2} for |x|⩽1/2|x|\leqslant 1/2:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Wn𝝀⩾∑k=1Nlog⁡(1+λk​(Xk−m))+∑k=N+1nλk​(Xk−μ)−∑k=N+1nλk2​(Xk−m)2.\log W\_{n}^{\boldsymbol{\lambda}}\geqslant\sum\_{k=1}^{N}\log(1+\lambda\_{k}(X\_{k}-m))+\sum\_{k=N+1}^{n}\lambda\_{k}(X\_{k}-\mu)-\sum\_{k=N+1}^{n}\lambda\_{k}^{2}(X\_{k}-m)^{2}. |  | (42) |

First, the standard martingale convergence result from Hall and Heyde [[2014](https://arxiv.org/html/2602.08888v1#bib.bib118 "Martingale limit theory and its application"), Theorem 2.15] states that SnS\_{n} converges a.s. to a finite random variable on the event {∑n=1∞λn2<∞}={⟨S⟩∞<∞}\{\sum\_{n=1}^{\infty}\lambda\_{n}^{2}<\infty\}=\{\langle S\rangle\_{\infty}<\infty\}; ∑k=1nλk2​(Xk−m)2\sum\_{k=1}^{n}\lambda\_{k}^{2}(X\_{k}-m)^{2} also converges on this event as |λk2​(Xk−m)2|⩽λk2|\lambda\_{k}^{2}(X\_{k}-m)^{2}|\leqslant\lambda\_{k}^{2}. These indicate that the second and third terms in ([42](https://arxiv.org/html/2602.08888v1#A2.E42 "Equation 42 ‣ Proof. ‣ B.1 Proof of Theorem 2.1 (sum-of-squares criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) both converge.
The events {λn​(Xn−m)>−1}\{\lambda\_{n}(X\_{n}-m)>-1\} further ensure the first term in ([42](https://arxiv.org/html/2602.08888v1#A2.E42 "Equation 42 ‣ Proof. ‣ B.1 Proof of Theorem 2.1 (sum-of-squares criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) is finite.
Therefore, the right hand side of ([42](https://arxiv.org/html/2602.08888v1#A2.E42 "Equation 42 ‣ Proof. ‣ B.1 Proof of Theorem 2.1 (sum-of-squares criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) converges a.s. to a finite variable on the event {∑n=1∞λn2<∞}∩⋂n=1∞{λn​(Xn−m)>−1}\left\{\sum\_{n=1}^{\infty}\lambda\_{n}^{2}<\infty\right\}\cap\bigcap\_{n=1}^{\infty}\{\lambda\_{n}(X\_{n}-m)>-1\}. This implies we can ensure W∞>0W\_{\infty}>0 on this event.

Finally, on any event {λn​(Xn−m)=−1}\{\lambda\_{n}(X\_{n}-m)=-1\}, it is clear that Wk𝝀=0W\_{k}^{\boldsymbol{\lambda}}=0 for all k⩾nk\geqslant n.
∎

### B.2 Proof of [Theorem 2.2](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.2 Almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)} ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") (almost sure divergence of ∑Ωp​(n−1)\sum\Omega\_{p}(n^{-1}))

###### Proof.

Take any ε∈(0,0.5)\varepsilon\in(0,0.5).
The condition Zn=Ωp​(n−1)Z\_{n}=\Omega\_{p}(n^{-1}) implies that there exist δ>0\delta>0 and N⩾1N\geqslant 1 such that ℙ​(n​Zn⩾δ)⩾1−ε\mathbb{P}(nZ\_{n}\geqslant\delta)\geqslant 1-\varepsilon for all n⩾Nn\geqslant N.
Consider the events An={n​Zn⩾δ}A\_{n}=\{nZ\_{n}\geqslant\delta\} and the convergence event C={∑n=1∞Zn<∞}C=\{\sum\_{n=1}^{\infty}Z\_{n}<\infty\}. We have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zn⩾Zn​𝟙An⩾δ​𝟙Ann.Z\_{n}\geqslant Z\_{n}\mathbbmss{1}\_{A\_{n}}\geqslant\frac{\delta\mathbbmss{1}\_{A\_{n}}}{n}. |  | (43) |

Therefore,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C\displaystyle C | ⊆{∑n=1∞δ​𝟙Ann<∞}={∑n=N+1∞𝟙Ann<∞}\displaystyle\subseteq\left\{\sum\_{n=1}^{\infty}\frac{\delta\mathbbmss{1}\_{A\_{n}}}{n}<\infty\right\}=\left\{\sum\_{n=N+1}^{\infty}\frac{\mathbbmss{1}\_{A\_{n}}}{n}<\infty\right\} |  | (44) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⊆(∗){limn→∞1n​∑k=N+1n𝟙Ak=0}={limn→∞1n−N​∑k=N+1n𝟙Ak=0}.\displaystyle\stackrel{{\scriptstyle(\*)}}{{\subseteq}}\left\{\lim\_{n\to\infty}\frac{1}{n}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}=0\right\}=\left\{\lim\_{n\to\infty}\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}=0\right\}. |  | (45) |

where the inclusion (∗)(\*) is due to Kronecker’s lemma. Now, recalling that lim infEn\liminf E\_{n} is the event that all but finitely many of events among (En)(E\_{n}) happen simultaneously, and noting that liman=0\lim a\_{n}=0 implies that an<0.5a\_{n}<0.5 for all but finitely many nn,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {limn→∞1n−N​∑k=N+1n𝟙Ak=0}⊆lim infn→∞{1n−N​∑k=N+1n𝟙Ak<0.5}.\left\{\lim\_{n\to\infty}\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}=0\right\}\subseteq\liminf\_{n\to\infty}\left\{\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}<0.5\right\}. |  | (46) |

Next, noting that the random variable Gn:=1n−N​∑k=N+1n𝟙Ak∈[0,1]G\_{n}:=\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}\in[0,1] has expected value 𝔼​Gn=1n−N​∑k=N+1nℙ​(Ak)⩾1−ε\mathbb{E}G\_{n}=\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbb{P}(A\_{k})\geqslant 1-\varepsilon, Markov’s inequality implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(1n−N​∑k=N+1n𝟙Ak<0.5)=ℙ​(1−Gn⩾0.5)⩽𝔼​(1−Gn)0.5⩽2​ε.\mathbb{P}\left(\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}<0.5\right)=\mathbb{P}(1-G\_{n}\geqslant 0.5)\leqslant\frac{\mathbb{E}(1-G\_{n})}{0.5}\leqslant 2\varepsilon. |  | (47) |

Combining everything above, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(C)⩽ℙ​(lim infn→∞{1n−N​∑k=N+1n𝟙Ak<0.5})⩽(∗∗)lim infn→∞ℙ​(1n−N​∑k=N+1n𝟙Ak<0.5)⩽2​ε\mathbb{P}(C)\leqslant\mathbb{P}\left(\liminf\_{n\to\infty}\left\{\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}<0.5\right\}\right)\stackrel{{\scriptstyle(\*\*)}}{{\leqslant}}\liminf\_{n\to\infty}\mathbb{P}\left(\frac{1}{n-N}\sum\_{k=N+1}^{n}\mathbbmss{1}\_{A\_{k}}<0.5\right)\leqslant 2\varepsilon |  | (48) |

where we applied Fatou’s lemma to obtain the inequality (∗∗)(\*\*). Since ε∈(0,0.5)\varepsilon\in(0,0.5) is arbitrary, we see that ℙ​(C)=0\mathbb{P}(C)=0.
∎

### B.3 Divergence of ∑Sn2/n2\sum S\_{n}^{2}/n^{2} via Donsker’s invariance principle

Below is an alternative proof of [Corollary 2.3](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.2 Almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)} ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies").

###### Proof.

Assume σ2=1\sigma^{2}=1 without loss of generality.
Let us study

|  |  |  |  |
| --- | --- | --- | --- |
|  | Tn=S12+⋯+Sn2.T\_{n}=S\_{1}^{2}+\dots+S\_{n}^{2}. |  | (49) |

By Donsker’s invariance principle, as random variables in the Skorokhod space 𝒟​[0,1]\mathcal{D}[0,1], the functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | B(n)​(t):=n−1/2​S⌊n​t⌋,t∈[0,1]B^{(n)}(t):=n^{-1/2}S\_{\lfloor nt\rfloor},\quad t\in[0,1] |  | (50) |

converge weakly to the standard Wiener process B​(t)B(t). Now consider the following function FF from the Skorokhod space 𝒟​[0,1]\mathcal{D}[0,1] to ℝ\mathbb{R}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(f)=∫01f​(t)2​𝑑t.F(f)=\int\_{0}^{1}f(t)^{2}dt. |  | (51) |

We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(B(n))=∫01n−1​S⌊n​t⌋2​𝑑t=n−1​∑k=1nn−1​Sk2=n−2​TnF(B^{(n)})=\int\_{0}^{1}n^{-1}S\_{\lfloor nt\rfloor}^{2}dt=n^{-1}\sum\_{k=1}^{n}n^{-1}S\_{k}^{2}=n^{-2}T\_{n} |  | (52) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | F(B)=∫01B2(t)dt=:B∗.F(B)=\int\_{0}^{1}B^{2}(t)dt=:B^{\*}. |  | (53) |

FF is a continuous function from the Skorokhod space to real numbers, a technical fact which we discuss later.
Therefore, the continuous mapping theorem implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | n−2​Tn⟶weaklyB∗,n^{-2}T\_{n}\stackrel{{\scriptstyle\text{weakly}}}{{\longrightarrow}}B^{\*}, |  | (54) |

a random variable with a continuous distribution on (0,∞)(0,\infty). For any δ>0\delta>0, let wδ>0w\_{\delta}>0 be the δ\delta-quantile of B∗B^{\*}. That is, P​(B∗⩽wδ)=δP(B^{\*}\leqslant w\_{\delta})=\delta. By Fatou’s lemma,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(lim inf{n−2​Tn⩽wδ})⩽lim infℙ​(n−2​Tn⩽wδ)=ℙ​(B∗⩽wδ)=δ,\mathbb{P}(\liminf\{n^{-2}T\_{n}\leqslant w\_{\delta}\})\leqslant\liminf\mathbb{P}(n^{-2}T\_{n}\leqslant w\_{\delta})=\mathbb{P}(B^{\*}\leqslant w\_{\delta})=\delta, |  | (55) |

where we recall that lim infAn\liminf A\_{n} is the event that all but finitely many of events among (An)(A\_{n}) happen simultaneously.
Noting that limn→∞n−2​Tn=0\lim\_{n\to\infty}n^{-2}T\_{n}=0 would imply n−2​Tn⩽wδn^{-2}T\_{n}\leqslant w\_{\delta} for all but finitely many nn:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(limn−2​Tn=0)⩽ℙ​(lim inf{n−2​Tn⩽wδ})⩽δ,\mathbb{P}(\lim n^{-2}T\_{n}=0)\leqslant\mathbb{P}(\liminf\{n^{-2}T\_{n}\leqslant w\_{\delta}\})\leqslant\delta, |  | (56) |

and the arbitrariness of δ\delta implies that ℙ​(limn−2​Tn=0)=0\mathbb{P}(\lim n^{-2}T\_{n}=0)=0.

Finally, by Kronecker’s lemma, ∑n=1∞n−2​Sn2<∞\sum\_{n=1}^{\infty}n^{-2}S\_{n}^{2}<\infty implies n−2​Tn=n−2​∑k=1nSk2→0n^{-2}T\_{n}=n^{-2}\sum\_{k=1}^{n}S\_{k}^{2}\to 0. Since the latter happens with probability 0,
we see that ∑n=1∞n−2​Sn2=∞\sum\_{n=1}^{\infty}n^{-2}S\_{n}^{2}=\infty almost surely. This completes the proof.
∎

Several remarks on this proof are as follows. First, the Skorokhod continuity of FF is proved below as [Lemma B.1](https://arxiv.org/html/2602.08888v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.3 Divergence of ∑{𝑆_𝑛²/𝑛²} via Donsker’s invariance principle ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"). Second, (yet) an alternative proof strategy that avoids the Skorokhod topology is to consider an appropriate “linear interpolation” of B(n)B^{(n)}, which converges to BB in the space of continuous functions (where the continuity of FF is straightforward).

###### Lemma B.1.

Let 𝒟​[0,1]\mathcal{D}[0,1] be the space of càdlàg functions on [0,1][0,1] equipped with the Skorokhod J1J\_{1} topology. Consider the square-integral functional F:𝒟​[0,1]→[0,∞)F:\mathcal{D}[0,1]\to[0,\infty),

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(f)=∫01f2​(x)​𝑑x.F(f)=\int\_{0}^{1}f^{2}(x)dx. |  | (57) |

Then, FF is continuous with respect to the standard topology on [0,∞)[0,\infty) and the Skorokhod J1J\_{1} topology on 𝒟​[0,1]\mathcal{D}[0,1].

###### Proof.

First, we observe that càdlàg functions on [0,1][0,1] are all bounded, implying that F​(f)<∞F(f)<\infty for all f∈𝒟​[0,1]f\in\mathcal{D}[0,1].

Next, given an f∈𝒟​[0,1]f\in\mathcal{D}[0,1], assume ‖f​(x)‖∞⩽C\|f(x)\|\_{\infty}\leqslant C. Consider the Skorokhod J1J\_{1} metric dd defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(f,g):=infλ∈𝕋{‖f∘λ−g‖∞+‖λ−i​d‖∞}d(f,g):=\inf\_{\lambda\in\mathbb{T}}\left\{\|f\circ\lambda-g\|\_{\infty}+\|\lambda-id\|\_{\infty}\right\} |  | (58) |

where 𝕋\mathbb{T} is the set of all increasing bijections on [0,1][0,1]. Consider the ε\varepsilon-ball around ff:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(f;ε)={g∈𝒟​[0,1]:d​(f,g)<ε}.B(f;\varepsilon)=\{g\in\mathcal{D}[0,1]:d(f,g)<\varepsilon\}. |  | (59) |

For any g∈B​(f;ε)g\in B(f;\varepsilon), there must exist a λ∈𝕋\lambda\in\mathbb{T} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f∘λ−g‖∞+‖λ−i​d‖∞⩽ε.\|f\circ\lambda-g\|\_{\infty}+\|\lambda-id\|\_{\infty}\leqslant\varepsilon. |  | (60) |

Therefore, for any x∈[0,1]x\in[0,1],

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)⩽f∘λ​(x)+ε⩽sup|y−x|⩽εf​(y)+ε,\displaystyle g(x)\leqslant f\circ\lambda(x)+\varepsilon\leqslant\sup\_{|y-x|\leqslant\varepsilon}f(y)+\varepsilon, |  | (61) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)⩾f∘λ​(x)−ε⩾inf|y−x|⩽εf​(y)−ε,\displaystyle g(x)\geqslant f\circ\lambda(x)-\varepsilon\geqslant\inf\_{|y-x|\leqslant\varepsilon}f(y)-\varepsilon, |  | (62) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |g​(x)|⩽C+ε.\displaystyle|g(x)|\leqslant C+\varepsilon. |  | (63) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |g2​(x)−f2​(x)|⩽|g​(x)+f​(x)|​|g​(x)−f​(x)|⩽(2​C+ε)​(sup|y−x|⩽εf​(y)−inf|y−x|⩽εf​(y)+2​ε).\displaystyle|g^{2}(x)-f^{2}(x)|\leqslant|g(x)+f(x)||g(x)-f(x)|\leqslant(2C+\varepsilon)\left(\sup\_{|y-x|\leqslant\varepsilon}f(y)-\inf\_{|y-x|\leqslant\varepsilon}f(y)+2\varepsilon\right). |  | (64) |

Now, consider the two Riemann integrals

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01(sup|y−x|⩽1/2​Nf​(y))​𝑑xand∫01(inf|y−x|⩽1/2​Nf​(y))​𝑑x.\int\_{0}^{1}\left(\sup\_{|y-x|\leqslant 1/2N}f(y)\right)dx\quad\text{and}\quad\int\_{0}^{1}\left(\inf\_{|y-x|\leqslant 1/2N}f(y)\right)dx. |  | (65) |

The Riemann sum of the first (resp. second) integral above on the partition

|  |  |  |  |
| --- | --- | --- | --- |
|  | (0,1/N,…,(N−1)/N,1),(0,1/N,\dots,(N-1)/N,1), |  | (66) |

which has mesh 1/N1/N,
is close to the upper (resp. a lower) Darboux sum of ∫01f​(x)​𝑑x\int\_{0}^{1}f(x)dx on the partition

|  |  |  |  |
| --- | --- | --- | --- |
|  | (0,1/2​N,3/2​N,…,(2​N−1)/2​N,1),(0,1/2N,3/2N,\dots,(2N-1)/2N,1), |  | (67) |

which has mesh 1/N1/N, and their difference (occurring only near the end points 0 and 1) is at most 2​C/N2C/N. Since ff is Riemann, hence Darboux, integrable,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→∞∫01(sup|y−x|⩽1/2​Nf​(y)−inf|y−x|⩽1/2​Nf​(y))​𝑑x=0.\lim\_{N\to\infty}\int\_{0}^{1}\left(\sup\_{|y-x|\leqslant 1/2N}f(y)-\inf\_{|y-x|\leqslant 1/2N}f(y)\right)dx=0. |  | (68) |

It therefore follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0supg∈B​(f;ε)|F​(g)−F​(f)|=limε→0∫01(2​C+ε)​(sup|y−x|⩽εf​(y)−inf|y−x|⩽εf​(y)+2​ε)​𝑑x=0,\lim\_{\varepsilon\to 0}\sup\_{g\in B(f;\varepsilon)}|F(g)-F(f)|=\lim\_{\varepsilon\to 0}\int\_{0}^{1}(2C+\varepsilon)\left(\sup\_{|y-x|\leqslant\varepsilon}f(y)-\inf\_{|y-x|\leqslant\varepsilon}f(y)+2\varepsilon\right)dx=0, |  | (69) |

concluding that FF is continuous at ff.
∎

### B.4 Proof of [Proposition 2.6](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem6 "Proposition 2.6. ‣ 2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") (Bahadur expansion of GRAPA/KLinf\operatorname{KL}\_{\inf} bet fractions)

###### Proof.

Define f​(λ,x)=−log⁡(1+λ​(x−m))f(\lambda,x)=-\log(1+\lambda(x-m)), Q​(λ)=𝔼P​f​(λ,X)Q(\lambda)=\mathbb{E}\_{P}{f(\lambda,X)}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qn​(λ)=1n​∑i=1nf​(λ,Xi),Q\_{n}(\lambda)=\frac{1}{n}\sum\_{i=1}^{n}f(\lambda,X\_{i}), |  | (70) |

where we consider the domain λ∈[−1/(1−m),1/m]\lambda\in[-1/(1-m),1/m]. Let λ∗\lambda^{\*} and λn𝖪𝖫\lambda^{\mathsf{KL}}\_{n} be the minimizers of QQ and QnQ\_{n} respectively. Then, λn+1𝖦𝖱𝖠𝖯𝖠=λn𝖪𝖳\lambda^{\mathsf{GRAPA}}\_{n+1}=\lambda^{\mathsf{KT}}\_{n}. (See [Section 5.1](https://arxiv.org/html/2602.08888v1#S5.SS1 "5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies") for the concept of λn𝖪𝖳\lambda^{\mathsf{KT}}\_{n} and KLinf\operatorname{KL}\_{\inf}.)

We now verify that the M-estimation problem above meets all assumptions for Theorem 5 in Niemiro [[1992](https://arxiv.org/html/2602.08888v1#bib.bib123 "Asymptotics for M-estimators defined by convex minimization")], with regularity constants s=0s=0 and r=10r=10. Note that while the asymptotic results of Niemiro [[1992](https://arxiv.org/html/2602.08888v1#bib.bib123 "Asymptotics for M-estimators defined by convex minimization")] are stated for open domains, they also apply to our closed domain [−1/(1−m),1/m][-1/(1-m),1/m] as the minimizer is allowed to be defined arbitrarily when QnQ\_{n} has no minimum on the open domain (−1/(1−m),1/m)(-1/(1-m),1/m).

* •

  f​(⋅,x)f(\cdot,x) is convex for any x∈[0,1]x\in[0,1].
* •

  For any λ∈(−1/(1−m),1/m\lambda\in(-1/(1-m),1/m, the expected value Q​(λ)=𝔼P​(f​(λ,X))Q(\lambda)=\mathbb{E}\_{P}\left(f(\lambda,X)\right) is finite, since f​(λ,⋅)f(\lambda,\cdot) is an upper and lower bounded function.
* •

  λ∗=0\lambda^{\*}=0 is the unique minimizer of Q​(λ)Q(\lambda). To see this, Q​(0)=0Q(0)=0 and if λ≠0\lambda\neq 0, because (1)
  t↦−log⁡(1+t)t\mapsto-\log(1+t) is strictly convex, (2) λ​(X−μ)\lambda(X-\mu) is not a point mass:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Q​(λ)=𝔼P​(−log⁡(1+λ​(X−m)))>−log⁡(1+𝔼P​(λ​(X−μ)))=0.Q(\lambda)=\mathbb{E}\_{P}\left(-\log(1+\lambda(X-m))\right)>-\log(1+\mathbb{E}\_{P}\left(\lambda(X-\mu)\right))=0. |  | (71) |

The properties above already ensured λn𝖪𝖳→λ∗\lambda^{\mathsf{KT}}\_{n}\to\lambda^{\*} almost surely. The following additional properties ensure normality and almost sure Bahadur expansion. Let g​(λ,x)=f′​(λ,x)=−x+m1+λ​(x−m)g(\lambda,x)=f^{\prime}(\lambda,x)=\frac{-x+m}{1+\lambda(x-m)}.

* •

  𝔼P​(g2​(λ,X))<∞\mathbb{E}\_{P}\left(g^{2}(\lambda,X)\right)<\infty for each λ\lambda, since g​(λ,⋅)g(\lambda,\cdot) is bounded.
* •

  Q​(λ)Q(\lambda) is twice differentiable at the minimum λ=0\lambda=0, and Q′′​(0)>0Q^{\prime\prime}(0)>0. To see this, for small λ\lambda:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Q′′​(λ)=𝔼P​(g′​(λ,X))=𝔼P​((X−m)2(1+λ​(X−m))2),Q′′​(0)=𝐕𝐚𝐫​X>0.Q^{\prime\prime}(\lambda)=\mathbb{E}\_{P}\left(g^{\prime}(\lambda,X)\right)=\mathbb{E}\_{P}\left(\frac{(X-m)^{2}}{(1+\lambda(X-m))^{2}}\right),\quad Q^{\prime\prime}(0)=\mathbf{Var}{X}>0. |  | (72) |
* •

  Expanding Q′​(λ)=𝔼P​(g​(λ,X))Q^{\prime}(\lambda)=\mathbb{E}\_{P}\left(g(\lambda,X)\right) near λ≈0\lambda\approx 0:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Q′​(λ)=𝔼P​(g​(λ,X))=𝔼P​(g​(0,X)+λ​g′​(0,X)+λ22​g′′​(ξX,X))=\displaystyle Q^{\prime}(\lambda)=\mathbb{E}\_{P}\left(g(\lambda,X)\right)=\mathbb{E}\_{P}\left(g(0,X)+\lambda g^{\prime}(0,X)+\frac{\lambda^{2}}{2}g^{\prime\prime}(\xi\_{X},X)\right)= |  | (73) |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | λ​𝐕𝐚𝐫​X−λ22​𝔼P​(2​(X−m)3(1+ξX​(X−m))3)\displaystyle\lambda\mathbf{Var}X-\frac{\lambda^{2}}{2}\mathbb{E}\_{P}\left(\frac{2(X-m)^{3}}{(1+\xi\_{X}(X-m))^{3}}\right) |  | (74) |

  where |ξX|⩽|λ||\xi\_{X}|\leqslant|\lambda| is the Lagrange remainder that depends on XX. It is easy to see that if |λ|<1/2|\lambda|<1/2,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |Q′​(λ)−λ​Q′′​(0)|⩽8​λ2.|Q^{\prime}(\lambda)-\lambda Q^{\prime\prime}(0)|\leqslant 8\lambda^{2}. |  | (75) |
* •

  Consider 𝔼P​((g​(λ,X)−g​(0,X))2)\mathbb{E}\_{P}\left((g(\lambda,X)-g(0,X))^{2}\right) near λ≈0\lambda\approx 0. With a similar Lagrange remainder |ζX|⩽|λ||\zeta\_{X}|\leqslant|\lambda|:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼P​((g​(λ,X)−g​(0,X))2)=𝔼P​((X−m)2​(1−11+λ​(X−m))2)=\displaystyle\mathbb{E}\_{P}\left((g(\lambda,X)-g(0,X))^{2}\right)=\mathbb{E}\_{P}\left((X-m)^{2}\left(1-\frac{1}{1+\lambda(X-m)}\right)^{2}\right)= |  | (76) |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼P​((X−m)2​(λ​(X−μ)(1+ζX​(X−m))2)2).\displaystyle\mathbb{E}\_{P}\left((X-m)^{2}\left(\frac{\lambda(X-\mu)}{(1+\zeta\_{X}(X-m))^{2}}\right)^{2}\right). |  | (77) |

  Therefore if |λ|<1/2|\lambda|<1/2,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼P​((g​(λ,X)−g​(0,X))2)⩽16​λ2.\mathbb{E}\_{P}\left((g(\lambda,X)-g(0,X))^{2}\right)\leqslant 16\lambda^{2}. |  | (78) |
* •

  Finally, for |λ|<1/2|\lambda|<1/2,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼P​(g10​(λ,X))=𝔼P​(|X−m|10|1+λ​(X−m)|10)⩽1024.\mathbb{E}\_{P}\left(g^{10}(\lambda,X)\right)=\mathbb{E}\_{P}\left(\frac{|X-m|^{10}}{|1+\lambda(X-m)|^{10}}\right)\leqslant 1024. |  | (79) |

From these properties, we have verified that all conditions for Theorem 5 in Niemiro [[1992](https://arxiv.org/html/2602.08888v1#bib.bib123 "Asymptotics for M-estimators defined by convex minimization")] hold with s=0s=0 and r=10r=10. It thus follows that, *almost surely*,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | n​λn𝖪𝖫\displaystyle\sqrt{n}\lambda^{\mathsf{KL}}\_{n} | =−1Q′′​(0)⋅∑k=1ng​(0,Xk)n+o​(n−1/4​log⁡n)\displaystyle=-\frac{1}{Q^{\prime\prime}(0)}\cdot\frac{\sum\_{k=1}^{n}g(0,X\_{k})}{\sqrt{n}}+o(n^{-1/4}\log n) |  | (80) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1𝐕𝐚𝐫​X⋅∑k=1n(Xk−m)n+o​(n−1/4​log⁡n),\displaystyle=\frac{1}{\mathbf{Var}X}\cdot\frac{\sum\_{k=1}^{n}(X\_{k}-m)}{\sqrt{n}}+o(n^{-1/4}\log n), |  | (81) |

which concludes the proof.
∎

We also remark that the Bahadur expansion of λn+1𝖦𝖱𝖠𝖯𝖠=λn𝖪𝖫\lambda^{\mathsf{GRAPA}}\_{n+1}=\lambda^{\mathsf{KL}}\_{n} above can be combined with [Corollary 2.3](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.2 Almost sure divergence of ∑{Ω_𝑝⁢(𝑛⁻¹)} ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") to show that ∑(λn𝖦𝖱𝖠𝖯𝖠)2=∞\sum(\lambda^{\mathsf{GRAPA}}\_{n})^{2}=\infty almost surely, thus an alternative proof of the bankruptcy of GRAPA.

### B.5 Proof of [Theorem 3.1](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem1 "Theorem 3.1 (No-cash criterion). ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies") (no-cash criterion)

The proof of [Theorem 3.1](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem1 "Theorem 3.1 (No-cash criterion). ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies") is made convenient by the following lemma.

###### Lemma B.2.

Let γ\gamma be a measure on [0,∞)[0,\infty). Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞∫0∞exp⁡(−x​An)​γ​(d​x)=γ​({0})\lim\_{n\to\infty}\int\_{0}^{\infty}\exp(-xA\_{n})\gamma(\mathrm{d}x)=\gamma(\{0\}) |  | (82) |

for any positive increasing sequence (An)(A\_{n}) that increases to ∞\infty.

###### Proof.

The functions (exp(−xAn):x∈[0,∞))n⩾1(\exp(-xA\_{n}):x\in[0,\infty))\_{n\geqslant 1} are pointwise monotone decreasing, and bounded in [0,1][0,1]. Therefore, due to the monotone convergence theorem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞∫0∞exp⁡(−x​An)​γ​(d​x)=∫0∞{limn→∞exp⁡(−x​An)}​γ​(d​x)=∫0∞𝟙{x=0}​γ​(d​x)=γ​({0}),\lim\_{n\to\infty}\int\_{0}^{\infty}\exp(-xA\_{n})\gamma(\mathrm{d}x)=\int\_{0}^{\infty}\left\{\lim\_{n\to\infty}\exp(-xA\_{n})\right\}\gamma(\mathrm{d}x)=\int\_{0}^{\infty}\mathbbmss{1}\_{\{x=0\}}\gamma(\mathrm{d}x)=\gamma(\{0\}), |  | (83) |

concluding the proof.
∎

Now we prove [Theorem 3.1](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem1 "Theorem 3.1 (No-cash criterion). ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies").

###### Proof.

First, let us prove the case when π\pi does not have an atom at 0, i.e., π​({0})=0\pi(\{0\})=0.
Let π+\pi^{+} and π−\pi^{-} be the restrictions of π\pi on (0,1/m](0,1/m] and [−1/(1−m),0)[-1/(1-m),0) respectively. Since π\pi does not have an atom at 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wnπ=∫01/m{∏k=1n(1+λ​(Xk−m))}​π+​(d​λ)⏟Wn++∫−1/(1−m)0{∏k=1n(1+λ​(Xk−m))}​π−​(d​λ)⏟Wn−.W\_{n}^{\pi}=\underbrace{\int\_{0}^{1/m}\left\{\prod\_{k=1}^{n}(1+\lambda(X\_{k}-m))\right\}\pi^{+}(\mathrm{d}\lambda)}\_{W^{+}\_{n}}+\underbrace{\int\_{-1/(1-m)}^{0}\left\{\prod\_{k=1}^{n}(1+\lambda(X\_{k}-m))\right\}\pi^{-}(\mathrm{d}\lambda)}\_{W^{-}\_{n}}. |  | (84) |

(Wn+)(W^{+}\_{n}) and (Wn−)(W^{-}\_{n}) are both nonnegative martingales (since they are mixtures of nonnegative martingales), and let us show that they both converge to 0 almost surely. By the inequality 1+x⩽exp⁡(x)1+x\leqslant\exp(x):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn+⩽∫01/mexp⁡(λ​∑k=1n(Xk−m))​π+​(d​λ).W\_{n}^{+}\leqslant\int\_{0}^{1/m}\exp\left(\lambda\sum\_{k=1}^{n}(X\_{k}-m)\right)\pi^{+}(\mathrm{d}\lambda). |  | (85) |

By the law of the iterated logarithm, lim inf∑k=1n(Xk−m)=−∞\liminf\sum\_{k=1}^{n}(X\_{k}-m)=-\infty almost surely, so
there exists a (random) sequence of positive integers n1<n2<…n\_{1}<n\_{2}<\dots such that sN:=−∑k=1nN(Xk−m)s\_{N}:=-\sum\_{k=1}^{n\_{N}}(X\_{k}-m) is a positive increasing sequence that increases to ∞\infty. By [Lemma B.2](https://arxiv.org/html/2602.08888v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.5 Proof of Theorem 3.1 (no-cash criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"), the sequence (WnN+)N⩾0(W\_{n\_{N}}^{+})\_{N\geqslant 0} then converges to 0. Therefore we see that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infn→∞Wn+=0,almost surely.\liminf\_{n\to\infty}W\_{n}^{+}=0,\quad\text{almost surely}. |  | (86) |

However, Wn+W\_{n}^{+} is a nonnegative martingale, so it must converge almost surely, therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞Wn+=0,almost surely.\lim\_{n\to\infty}W\_{n}^{+}=0,\quad\text{almost surely}. |  | (87) |

The same reasoning holds for Wn−W\_{n}^{-}, using lim sup∑k=1n(Xk−m)=∞\limsup\sum\_{k=1}^{n}(X\_{k}-m)=\infty almost surely. This concludes the proof that Wnπ→0W\_{n}^{\pi}\to 0 almost surely.

Next, if π\pi has an atom at 0, i.e., π​({0})>0\pi(\{0\})>0, we can simply decompose the wealth into its “cash component” and its “bet component”

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wnπ=π​({0})⋅Wn0+∫Wnλ​π|[−11−m,0)∪(0,1m]​(d​λ),W\_{n}^{\pi}=\pi(\{0\})\cdot W\_{n}^{0}+\int W\_{n}^{\lambda}\,\pi|\_{[-\frac{1}{1-m},0)\cup(0,\frac{1}{m}]}(\mathrm{d}\lambda), |  | (88) |

where Wn0=1W\_{n}^{0}=1, and the second part converges to 0. Therefore, Wnπ→π​({0})W\_{n}^{\pi}\to\pi(\{0\}) almost surely.
∎

### B.6 Discussion and proof for [Theorem 4.1](https://arxiv.org/html/2602.08888v1#S4.Thmtheorem1 "Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies") (improvability of non-bankrupt strategies)

We begin our argument by noting that the cash-removal ([23](https://arxiv.org/html/2602.08888v1#S3.E23 "Equation 23 ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies")) is actually a mixture of two strategies, π\pi-mixture and cash (Mn𝟎=1M\_{n}^{\bf 0}=1), with a *negative* weight on cash. That is, one leverages (longs) the original strategy π\pi-mixture by borrowing (shorting) some cash.
Let us therefore clarify the general scenarios for the mixture of two strategies that may or may not allow shorting.

###### Fact 1 (Mixture of two predictable plug-ins, long only).

Let (Wn𝛌)(W\_{n}^{\boldsymbol{\lambda}}) and (Wn𝛎)(W\_{n}^{\boldsymbol{\nu}}) be the wealth processes corresponding to two predictable bet fraction sequences 𝛌\boldsymbol{\lambda} and 𝛎\boldsymbol{\nu}. Then, the portfolio consisting of these two strategies

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−κ)​Wn𝝀+κ​Wn𝝂(1-\kappa)W\_{n}^{\boldsymbol{\lambda}}+\kappa W\_{n}^{\boldsymbol{\nu}} |  | (89) |

is equivalent to the predictable plug-in strategy Wn𝛃W\_{n}^{\boldsymbol{\beta}} with bet fraction sequence

|  |  |  |  |
| --- | --- | --- | --- |
|  | βn=(1−κ)​Wn−1𝝀​λn+κ​Wn−1𝝂​νn(1−κ)​Wn−1𝝀+κ​Wn−1𝝂,\beta\_{n}=\frac{(1-\kappa)W\_{n-1}^{\boldsymbol{\lambda}}\lambda\_{n}+\kappa W\_{n-1}^{\boldsymbol{\nu}}\nu\_{n}}{(1-\kappa)W\_{n-1}^{\boldsymbol{\lambda}}+\kappa W\_{n-1}^{\boldsymbol{\nu}}}, |  | (90) |

where κ∈[0,1]\kappa\in[0,1] is a constant.

To see that the bet fraction ([90](https://arxiv.org/html/2602.08888v1#A2.E90 "Equation 90 ‣ Fact 1 (Mixture of two predictable plug-ins, long only). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) βn∈[−11−m,1m]\beta\_{n}\in[-\frac{1}{1-m},\frac{1}{m}], it is a convex combination of λn,νn∈[−11−m,1m]\lambda\_{n},\nu\_{n}\in[-\frac{1}{1-m},\frac{1}{m}].

###### Fact 2 (Mixture of two predictable plug-ins, short allowed).

Let (Wn𝛌)(W\_{n}^{\boldsymbol{\lambda}}) and (Wn𝛎)(W\_{n}^{\boldsymbol{\nu}}) be the wealth processes corresponding to two predictable bet fraction sequences 𝛌\boldsymbol{\lambda} and 𝛎\boldsymbol{\nu}. If these strategies further ensure that, on all binary paths (Xn)∈{0,1}∞(X\_{n})\in\{0,1\}^{\infty},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn𝝀Wn𝝂>ρ∈[0,1),∀n\frac{W\_{n}^{\boldsymbol{\lambda}}}{W\_{n}^{\boldsymbol{\nu}}}>\rho\in[0,1),\quad\forall n |  | (91) |

then, the portfolio consisting of these two strategies

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−κ)​Wn𝝀+κ​Wn𝝂(1-\kappa)W\_{n}^{\boldsymbol{\lambda}}+\kappa W\_{n}^{\boldsymbol{\nu}} |  | (92) |

is equivalent to the predictable plug-in strategy Wn𝛃W\_{n}^{\boldsymbol{\beta}} with bet fraction sequence

|  |  |  |  |
| --- | --- | --- | --- |
|  | βn=(1−κ)​Wn−1𝝀​λn+κ​Wn−1𝝂​νn(1−κ)​Wn−1𝝀+κ​Wn−1𝝂,\beta\_{n}=\frac{(1-\kappa)W\_{n-1}^{\boldsymbol{\lambda}}\lambda\_{n}+\kappa W\_{n-1}^{\boldsymbol{\nu}}\nu\_{n}}{(1-\kappa)W\_{n-1}^{\boldsymbol{\lambda}}+\kappa W\_{n-1}^{\boldsymbol{\nu}}}, |  | (93) |

where we can now long 𝛌\boldsymbol{\lambda} and short 𝛎\boldsymbol{\nu}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ∈[−ρ1−ρ,1].\kappa\in\left[-\frac{\rho}{1-\rho},1\right]. |  | (94) |

In particular, when 𝛎=𝟎\boldsymbol{\nu}=\bf 0, it means that starting with any strategy 𝛌\boldsymbol{\lambda} with always-valid strict wealth lower bound Wn𝛌>ρW\_{n}^{\boldsymbol{\lambda}}>\rho on all binary paths, one can borrow b=−κ∈(0,ρ/(1−ρ)]b=-\kappa\in(0,\rho/(1-\rho)] amount of cash and execute the leveraged bets

|  |  |  |  |
| --- | --- | --- | --- |
|  | βn=(1+b)​Wn−1𝝀​λn(1+b)​Wn−1𝝀−b⟹Wn𝜷=(1+b)​Wn𝝀−b\beta\_{n}=\frac{(1+b)W\_{n-1}^{\boldsymbol{\lambda}}\lambda\_{n}}{(1+b)W\_{n-1}^{\boldsymbol{\lambda}}-b}\quad\implies\quad W\_{n}^{\boldsymbol{\beta}}=(1+b)W\_{n}^{\boldsymbol{\lambda}}-b |  | (95) |

instead.

To see that the bet fraction βn\beta\_{n} defined in ([93](https://arxiv.org/html/2602.08888v1#A2.E93 "Equation 93 ‣ Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) is in [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}] even when κ<0\kappa<0,

|  |  |  |
| --- | --- | --- |
|  | 1+βn​(Xn−m)=(1−κ)​Wn𝝀+κ​Wn𝝂(1−κ)​Wn−1𝝀+κ​Wn−1𝝂>01+\beta\_{n}(X\_{n}-m)=\frac{(1-\kappa)W\_{n}^{\boldsymbol{\lambda}}+\kappa W\_{n}^{\boldsymbol{\nu}}}{(1-\kappa)W\_{n-1}^{\boldsymbol{\lambda}}+\kappa W\_{n-1}^{\boldsymbol{\nu}}}>0 |  |

for all binary paths, it holds in particular when Xn=0X\_{n}=0 and 11. This is why we require the bound ([91](https://arxiv.org/html/2602.08888v1#A2.E91 "Equation 91 ‣ Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) to hold on binary paths when formulating shorting here: if we merely know by oracle that Wn𝝀Wn𝝂>ρ\frac{W\_{n}^{\boldsymbol{\lambda}}}{W\_{n}^{\boldsymbol{\nu}}}>\rho without knowing XnX\_{n} can take 0 and 11, the bet fraction equivalent to shorting ([93](https://arxiv.org/html/2602.08888v1#A2.E93 "Equation 93 ‣ Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) might correspond to an infeasible fraction that just “happens not to” lead to negative wealth. The assumption of ([91](https://arxiv.org/html/2602.08888v1#A2.E91 "Equation 91 ‣ Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) on all binary paths is weaker than ([91](https://arxiv.org/html/2602.08888v1#A2.E91 "Equation 91 ‣ Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) on all bounded paths (Xn)∈[0,1]∞(X\_{n})\in[0,1]^{\infty}, and in general incomparable to ([91](https://arxiv.org/html/2602.08888v1#A2.E91 "Equation 91 ‣ Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) on PP-almost all paths under some distribution PP.

We also see here that for a mixture strategy with cash component π​({0})>0\pi(\{0\})>0, removing the cash component is an instance of the above with ρ=π​({0})\rho=\pi(\{0\}) and b=ρ/(1−ρ)b=\rho/(1-\rho). However, in general, a non-bankrupt strategy’s minimum wealth is a path-dependent quantity that is not known in advance. We thus employ the following idea: we fix *some* ρ>0\rho>0, and execute the bet fraction equivalent to borrowing b=ρ/(1−ρ)b=\rho/(1-\rho)

|  |  |  |  |
| --- | --- | --- | --- |
|  | βnρ=(1+ρ1−ρ)​Wn−1𝝀​λn(1+ρ1−ρ)​Wn−1𝝀−ρ1−ρ=Wn−1𝝀​λnWn−1𝝀−ρ\beta\_{n}^{\rho}=\frac{(1+\frac{\rho}{1-\rho})W\_{n-1}^{\boldsymbol{\lambda}}\lambda\_{n}}{(1+\frac{\rho}{1-\rho})W\_{n-1}^{\boldsymbol{\lambda}}-\frac{\rho}{1-\rho}}=\frac{W\_{n-1}^{\boldsymbol{\lambda}}\lambda\_{n}}{W\_{n-1}^{\boldsymbol{\lambda}}-\rho} |  | (96) |

when it is valid (i.e. βnρ∈[−11−m,1m]\beta\_{n}^{\rho}\in[-\frac{1}{1-m},\frac{1}{m}]). Analogous to the discussion around the validity of ([93](https://arxiv.org/html/2602.08888v1#A2.E93 "Equation 93 ‣ Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) above, we have the following statement characterizing when the validity βnρ∈[−11−m,1m]\beta\_{n}^{\rho}\in[-\frac{1}{1-m},\frac{1}{m}] holds. We recall from [Section 4](https://arxiv.org/html/2602.08888v1#S4 "4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | W^n𝝀=minx∈[0,1]⁡Wn−1𝝀​(1+λn​(x−m))=min⁡{Wn−1𝝀​(1+λn​(0−m)),Wn−1𝝀​(1+λn​(1−m))}.\widehat{W}\_{n}^{\boldsymbol{\lambda}}=\min\_{x\in[0,1]}W\_{n-1}^{\boldsymbol{\lambda}}(1+\lambda\_{n}(x-m))=\min\{W\_{n-1}^{\boldsymbol{\lambda}}(1+\lambda\_{n}(0-m)),W\_{n-1}^{\boldsymbol{\lambda}}(1+\lambda\_{n}(1-m))\}. |  | (97) |

###### Lemma B.3.

{W^n𝝀>ρ}⊆{−11−m<βnρ<1m}\{\widehat{W}\_{n}^{\boldsymbol{\lambda}}>\rho\}\subseteq\{-\frac{1}{1-m}<\beta\_{n}^{\rho}<\frac{1}{m}\}.

###### Proof.

On the event {W^n𝝀>ρ}\{\widehat{W}\_{n}^{\boldsymbol{\lambda}}>\rho\},
we have Wn−1𝝀​(1+λn​(x−m))>ρW\_{n-1}^{\boldsymbol{\lambda}}(1+\lambda\_{n}(x-m))>\rho for x=0x=0, mm, and 11. So

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1+βnρ​(x−m)=11−ρ​Wn−1𝝀​(1+λn​(x−m))−ρ1−ρ11−ρ​Wn−1𝝀−ρ1−ρ>0,x∈{0,1}.1+\beta\_{n}^{\rho}(x-m)=\frac{\frac{1}{1-\rho}W\_{n-1}^{\boldsymbol{\lambda}}(1+\lambda\_{n}(x-m))-\frac{\rho}{1-\rho}}{\frac{1}{1-\rho}W\_{n-1}^{\boldsymbol{\lambda}}-\frac{\rho}{1-\rho}}>0,\quad x\in\{0,1\}. |  | (98) |

Therefore, βnρ<1m\beta\_{n}^{\rho}<\frac{1}{m} by x=0x=0, and βnρ>−11−m\beta\_{n}^{\rho}>-\frac{1}{1-m} by x=1x=1.
∎

That is, one can bet βnρ\beta\_{n}^{\rho} when {W^n𝝀>ρ}\{\widehat{W}\_{n}^{\boldsymbol{\lambda}}>\rho\} happens. This leads us to the following definition of a new strategy that “opportunistically” executes the ρ\rho-leverage.

###### Definition B.4 (Opportunistic leveraging).

Let 𝛌=(λn)\boldsymbol{\lambda}=(\lambda\_{n}) be a predictable plugin betting strategy and ρ>0\rho>0. Define En={W^n𝛌>ρ}E\_{n}=\{\widehat{W}\_{n}^{\boldsymbol{\lambda}}>\rho\}. Then the events (En)(E\_{n}) are predictable. Define the new plugin fraction

|  |  |  |  |
| --- | --- | --- | --- |
|  | γn=𝟙En​Wn−1𝝀​λnWn−1𝝀−ρ+(1−𝟙En)​λn,\gamma\_{n}=\mathbbmss{1}\_{E\_{n}}\frac{W\_{n-1}^{\boldsymbol{\lambda}}\lambda\_{n}}{W\_{n-1}^{\boldsymbol{\lambda}}-\rho}+(1-\mathbbmss{1}\_{E\_{n}})\lambda\_{n}, |  | (99) |

which is predictable and always belongs to [−11−m,1m][-\frac{1}{1-m},\frac{1}{m}]. Therefore 𝛄=(γn)\boldsymbol{\gamma}=(\gamma\_{n}) is also a predictable plugin betting strategy.
Further, on ∩k=1nEk\cap\_{k=1}^{n}E\_{k}, Wn𝛄=Wn𝛌−ρ1−ρW\_{n}^{\boldsymbol{\gamma}}=\frac{W\_{n}^{\boldsymbol{\lambda}}-\rho}{1-\rho}.
We call this new strategy 𝛄\boldsymbol{\gamma} the *ρ\rho-opportunistic leverage* of the strategy 𝛌\boldsymbol{\lambda}.

In words, the transformation above defines a new strategy that, at each step, first checks if it is safe to execute a bet fraction corresponding to borrowing b=ρ/(1−ρ)b=\rho/(1-\rho) by seeing if the precondition En={W^n𝝀>ρ}E\_{n}=\{\widehat{W}\_{n}^{\boldsymbol{\lambda}}>\rho\} holds, then does so if it is and executes the original bet fraction if otherwise. Thus, if next-step minimum wealth W^n𝝀\widehat{W}\_{n}^{\boldsymbol{\lambda}} is indeed always above ρ\rho, the new strategy’s wealth process is indistinguishable from borrowing b=ρ/(1−ρ)b=\rho/(1-\rho) and leveraging the original strategy from the outset. This transformation leads to the proof of [Theorem 4.1](https://arxiv.org/html/2602.08888v1#S4.Thmtheorem1 "Theorem 4.1 (Improvability on predictably non-bankrupt paths). ‣ 4 Do all good strategies go bankrupt? ‣ Almost sure null bankruptcy of testing-by-betting strategies").

###### Proof.

Let (Wn♯)(W\_{n}^{\sharp}) be the wealth process of the ρ\rho-opportunistic leverage of the original strategy. On the event Nρ=⋂n=1∞EnN^{\rho}=\bigcap\_{n=1}^{\infty}E\_{n}, Wn♯=Wn−ρ1−ρW\_{n}^{\sharp}=\frac{W\_{n}-\rho}{1-\rho} for all nn, thus Wn♯<WnW\_{n}^{\sharp}<W\_{n} if Wn<1W\_{n}<1, Wn♯>WnW\_{n}^{\sharp}>W\_{n} if Wn>1W\_{n}>1, and Wn♯/Wn→1/(1−ρ)W\_{n}^{\sharp}/W\_{n}\to 1/(1-\rho) if Wn→∞W\_{n}\to\infty.
∎

###### Remark B.5.

The construction above uses the concept of borrowing. Recently, Wang and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib122 "Testing by betting while borrowing and bargaining")] discuss at length the definition, effect, and utility of borrowing in testing-by-betting. Our definition in [Fact 2](https://arxiv.org/html/2602.08888v1#Thmfact2 "Fact 2 (Mixture of two predictable plug-ins, short allowed). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies") corresponds to the “net wealth” (i.e. always paying back the debt after borrowing) discussed by Wang and Ramdas [[2024](https://arxiv.org/html/2602.08888v1#bib.bib122 "Testing by betting while borrowing and bargaining")], and differs from it in that we do not allow negative wealth.

### B.7 Proof of [Theorem 5.1](https://arxiv.org/html/2602.08888v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5.1 Null asymptotics of KL_inf ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies") (χ(1)2\chi^{2}\_{(1)} limit of KLinf\operatorname{KL}\_{\inf})

###### Proof.

Due to the Bahadur expansion of the GRAPA bet fractions in [Proposition 2.6](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem6 "Proposition 2.6. ‣ 2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | λn𝖪𝖫=1σ2⋅∑k=1n(Xk−m)n+rn\lambda^{\mathsf{KL}}\_{n}=\frac{1}{\sigma^{2}}\cdot\frac{\sum\_{k=1}^{n}(X\_{k}-m)}{n}+r\_{n} |  | (100) |

where rn=oa.s.​(n−3/4​log⁡n)r\_{n}=o\_{a.s.}(n^{-3/4}\log n). Expanding log⁡(1+x)\log(1+x), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ln∗=\displaystyle L^{\*}\_{n}= | ∑k=1nlog⁡(1+λn𝖪𝖫​(Xk−m))=∑k=1nλn𝖪𝖫​(Xk−m)−∑k=1n(λn𝖪𝖫)2​(Xk−m)22​(1+ξn​k)2,\displaystyle\sum\_{k=1}^{n}\log(1+\lambda^{\mathsf{KL}}\_{n}(X\_{k}-m))=\sum\_{k=1}^{n}\lambda^{\mathsf{KL}}\_{n}(X\_{k}-m)-\sum\_{k=1}^{n}\frac{(\lambda^{\mathsf{KL}}\_{n})^{2}(X\_{k}-m)^{2}}{2(1+\xi\_{nk})^{2}}, |  | (101) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | Sn2n​σ2+rn​Sn−(−Sn+n​σ2​rn)22​n​σ2​∑k=1n(Xk−m)2n​σ2​(1+ξn​k)2=Sn22​n​σ2+oa.s.​(n−1/4​log2⁡n).\displaystyle\frac{S\_{n}^{2}}{n\sigma^{2}}+r\_{n}S\_{n}-\frac{(-S\_{n}+n\sigma^{2}r\_{n})^{2}}{2n\sigma^{2}}\sum\_{k=1}^{n}\frac{(X\_{k}-m)^{2}}{n\sigma^{2}(1+\xi\_{nk})^{2}}=\frac{S\_{n}^{2}}{2n\sigma^{2}}+o\_{a.s.}(n^{-1/4}\log^{2}n). |  | (102) |

where |ξn​k|⩽|λn𝖪𝖫|=oa.s.​(n−1​log⁡n)|\xi\_{nk}|\leqslant|\lambda^{\mathsf{KL}}\_{n}|=o\_{a.s.}(\sqrt{n^{-1}\log n}) is the Lagrange remainder, and Sn=∑k=1n(Xk−m)=oa.s.​(n​log⁡n)S\_{n}=\sum\_{k=1}^{n}(X\_{k}-m)=o\_{a.s.}(\sqrt{n\log n}). Noting that Sn2n​σ2\frac{S\_{n}^{2}}{n\sigma^{2}} converges weakly to χ(1)2\chi^{2}\_{(1)}, we see that so does 2​Ln∗2L\_{n}^{\*} via Slutsky’s theorem.
∎

### B.8 Proofs of the subGaussian criteria, [Theorems 5.2](https://arxiv.org/html/2602.08888v1#S5.Thmtheorem2 "Theorem 5.2 (Sum-of-squares criterion II). ‣ 5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies") and [5.3](https://arxiv.org/html/2602.08888v1#S5.Thmtheorem3 "Theorem 5.3 (No-cash criterion II). ‣ 5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies")

The proof of [Theorem 5.2](https://arxiv.org/html/2602.08888v1#S5.Thmtheorem2 "Theorem 5.2 (Sum-of-squares criterion II). ‣ 5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies") is below.

###### Proof.

Without loss of generality, let m=0m=0. Consider the log-process

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Mn𝝀=∑k=1nλk​Xk−12​∑k=1nλk2.\log M\_{n}^{\boldsymbol{\lambda}}=\sum\_{k=1}^{n}\lambda\_{k}X\_{k}-\frac{1}{2}\sum\_{k=1}^{n}\lambda\_{k}^{2}. |  | (103) |

On the event {∑λn2<∞}\{\sum\lambda\_{n}^{2}<\infty\}, the martingale ∑k=1nλk​Xk\sum\_{k=1}^{n}\lambda\_{k}X\_{k} has convergent quadratic variation, therefore it a.s. converges due to Hall and Heyde [[2014](https://arxiv.org/html/2602.08888v1#bib.bib118 "Martingale limit theory and its application"), Theorem 2.15], so log⁡Mn𝝀\log M\_{n}^{\boldsymbol{\lambda}} converges a.s. on this event. Therefore, Mn𝝀M\_{n}^{\boldsymbol{\lambda}} converges a.s. to a non-zero random variable on this event.

On the event {∑λn2=∞}\{\sum\lambda\_{n}^{2}=\infty\}, we invoke the martingale strong law of large numbers [Fitzsimmons, [2005](https://arxiv.org/html/2602.08888v1#bib.bib117 "SLLN for Martingales"), Theorem 3] and see that ∑k=1nλk​Xk∑k=1nλk2→0\frac{\sum\_{k=1}^{n}\lambda\_{k}X\_{k}}{\sum\_{k=1}^{n}\lambda\_{k}^{2}}\to 0 almost surely. Therefore, on this event,

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Mn𝝀=(∑k=1nλk​Xk∑k=1nλk2−12)⋅(∑k=1nλk2)→(0−0.5)⋅(+∞)=−∞\log M\_{n}^{\boldsymbol{\lambda}}=\left(\frac{\sum\_{k=1}^{n}\lambda\_{k}X\_{k}}{\sum\_{k=1}^{n}\lambda\_{k}^{2}}-\frac{1}{2}\right)\cdot\left({\sum\_{k=1}^{n}\lambda\_{k}^{2}}\right)\to(0-0.5)\cdot(+\infty)=-\infty |  | (104) |

almost surely. So Mn𝝀→0M\_{n}^{\boldsymbol{\lambda}}\to 0 a.s. on this event.
∎

The proof of [Theorem 5.3](https://arxiv.org/html/2602.08888v1#S5.Thmtheorem3 "Theorem 5.3 (No-cash criterion II). ‣ 5.2 Null bankruptcy in subGaussian and sub-𝜓 testing ‣ 5 Further discussions ‣ Almost sure null bankruptcy of testing-by-betting strategies") is below.

###### Proof.

It suffices to consider m=0m=0 and π​({0})=0\pi(\{0\})=0. Similar to the proof of [Theorem 3.1](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem1 "Theorem 3.1 (No-cash criterion). ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies"), we show that the nonnegative martingales

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mn+=∫0∞exp⁡(∑k=1nXk2−(Xk−λ)22)​π+​(d​λ),Mn−=∫−∞0exp⁡(∑k=1nXk2−(Xk−λ)22)​π−​(d​λ)M\_{n}^{+}=\int\_{0}^{\infty}\exp\left(\sum\_{k=1}^{n}\frac{X\_{k}^{2}-(X\_{k}-\lambda)^{2}}{2}\right)\pi^{+}(\mathrm{d}\lambda),\;M\_{n}^{-}=\int\_{-\infty}^{0}\exp\left(\sum\_{k=1}^{n}\frac{X\_{k}^{2}-(X\_{k}-\lambda)^{2}}{2}\right)\pi^{-}(\mathrm{d}\lambda) |  | (105) |

both converge a.s. to 0, where π+\pi^{+} and π−\pi^{-} are the (0,∞)(0,\infty) and (−∞,0)(-\infty,0) parts of π\pi respectively. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mn+=∫0∞exp⁡(∑k=1n2​λ​Xk−λ22)​π+​(d​λ)⩽∫0∞exp⁡(λ​∑k=1nXk)​π+​(d​λ).M\_{n}^{+}=\int\_{0}^{\infty}\exp\left(\sum\_{k=1}^{n}\frac{2\lambda X\_{k}-\lambda^{2}}{2}\right)\pi^{+}(\mathrm{d}\lambda)\leqslant\int\_{0}^{\infty}\exp\left(\lambda\sum\_{k=1}^{n}X\_{k}\right)\pi^{+}(\mathrm{d}\lambda). |  | (106) |

Using the same technique as in the proof of [Theorem 3.1](https://arxiv.org/html/2602.08888v1#S3.Thmtheorem1 "Theorem 3.1 (No-cash criterion). ‣ 3 Bankruptcy of mixture strategies ‣ Almost sure null bankruptcy of testing-by-betting strategies"), lim inf∑k=1nXk=−∞\liminf\sum\_{k=1}^{n}X\_{k}=-\infty a.s. and [Lemma B.2](https://arxiv.org/html/2602.08888v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.5 Proof of Theorem 3.1 (no-cash criterion) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies") imply that limMn+=lim infMn+=0\lim M\_{n}^{+}=\liminf M\_{n}^{+}=0 a.s.. The same works for Mn−M\_{n}^{-}.
∎

## Appendix C Further discussions on good strategies’ necessary bankruptcy

We first present additional examples exploring the question “do all good strategies go bankrupt”.
Below, a slightly modified predictable plug-in strategy is no longer null-bankrupt, still remains universally power, but is always only *sub*exponentially powerful.

###### Example C.1 (Increasingly intermittent bets).

Let α>1\alpha>1 and consider the set Iα={⌊nα⌋:n=1,2,…}I\_{\alpha}=\{\lfloor n^{\alpha}\rfloor:n=1,2,\dots\}.
Let λn′=𝟙n∈Iα​λn\lambda\_{n}^{\prime}=\mathbbmss{1}\_{n\in I\_{\alpha}}\lambda\_{n}, where λn\lambda\_{n} is either the KT bet fraction λn𝖪𝖳\lambda^{\mathsf{KT}}\_{n} with C=2C=2, the GRAPA bet fraction λn𝖦𝖱𝖠𝖯𝖠\lambda^{\mathsf{GRAPA}}\_{n}, or the aGRAPA bet fraction λn𝖺𝖦𝖱𝖠𝖯𝖠\lambda^{\mathsf{aGRAPA}}\_{n}. Then, the wealth process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn′=∏k=1n(1+λk′(Xk−m)=∏k∈Iα,k⩽n(1+λk′(Xk−m))W\_{n}^{\prime}=\prod\_{k=1}^{n}(1+\lambda\_{k}^{\prime}(X\_{k}-m)=\prod\_{k\in I\_{\alpha},k\leqslant n}(1+\lambda\_{k}^{\prime}(X\_{k}-m)) |  | (107) |

grows sub-exponentially fast log⁡Wn′=Θa.s.​(n1/α)\log W\_{n}^{\prime}=\Theta\_{a.s.}(n^{1/\alpha}) under any alternative distribution, and converges a.s. to a positive random variable under any null distribution.

That is, one only bets at times n=1,4,9,16​…n=1,4,9,16\dots if, for example, α=2\alpha=2. The almost sure non-bankruptcy of these strategies is an easy corollary of [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies"). This strategy is improvable by “betting more frequently”: the standard KT/GRAPA/aGRAPA strategy that does not withhold from betting at n∉Iαn\notin I\_{\alpha}. The improvement makes more money under the alternative, at the price of making less money (and possible bankruptcy) under the null.

Given the subexponentially growing wealth in [Example C.1](https://arxiv.org/html/2602.08888v1#A3.Thmtheorem1 "Example C.1 (Increasingly intermittent bets). ‣ Appendix C Further discussions on good strategies’ necessary bankruptcy ‣ Almost sure null bankruptcy of testing-by-betting strategies"),
it is tempting to think that exponential wealth growth log⁡Wn=Θa.s.​(n)\log W\_{n}=\Theta\_{a.s.}(n) under any alternative implies null-bankruptcy. The following strategy, however, is a simple counterexample to this conjecture.

###### Example C.2 (Cash-GRAPA mixture).

By the argument from [Fact 1](https://arxiv.org/html/2602.08888v1#Thmfact1 "Fact 1 (Mixture of two predictable plug-ins, long only). ‣ B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies"), there exists a betting strategy constituting of a 50-50 mixture between cash and GRAPA:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn=12+12​∏k=1n(1+λk𝖦𝖱𝖠𝖯𝖠​(Xk−m)).W\_{n}=\frac{1}{2}+\frac{1}{2}\prod\_{k=1}^{n}(1+\lambda^{\mathsf{GRAPA}}\_{k}(X\_{k}-m)). |  | (108) |

Then, WnW\_{n} converges a.s. to 1/21/2 under any non-degenerate null, but also grows exponentially fast under any alternative distribution, attaining the same rate n−1​log⁡Wn=λ𝖪𝖾𝗅𝗅𝗒n^{-1}\log W\_{n}=\lambda^{\mathsf{Kelly}} as the cashless GRAPA.

This strategy can be improved by, again, “removing the cash”. We note that
our “generalized cash-removal” idea elaborated in ([B.6](https://arxiv.org/html/2602.08888v1#A2.SS6 "B.6 Discussion and proof for Theorem 4.1 (improvability of non-bankrupt strategies) ‣ Appendix B Omitted and additional proofs ‣ Almost sure null bankruptcy of testing-by-betting strategies")) can make already exponentially powerful strategies like [Example C.2](https://arxiv.org/html/2602.08888v1#A3.Thmtheorem2 "Example C.2 (Cash-GRAPA mixture). ‣ Appendix C Further discussions on good strategies’ necessary bankruptcy ‣ Almost sure null bankruptcy of testing-by-betting strategies") make multiplicatively more money, but cannot make subexponentially powerful strategies like [Example C.1](https://arxiv.org/html/2602.08888v1#A3.Thmtheorem1 "Example C.1 (Increasingly intermittent bets). ‣ Appendix C Further discussions on good strategies’ necessary bankruptcy ‣ Almost sure null bankruptcy of testing-by-betting strategies") make exponentially money. Generalizing the “betting more frequently” improvement we mentioned above for [Example C.1](https://arxiv.org/html/2602.08888v1#A3.Thmtheorem1 "Example C.1 (Increasingly intermittent bets). ‣ Appendix C Further discussions on good strategies’ necessary bankruptcy ‣ Almost sure null bankruptcy of testing-by-betting strategies") to more subexponentially powerful strategies is of interest for future work.

Finally, we discuss the relevance (or lack thereof) of the Cramér-Rao lower bounds.
One might notice that for the null-bankrupt strategies
KT, GRAPA, and aGRAPA, the bet fractions are estimators that converge a.s. to a fixed number λn𝖪𝖳→μ​(P)−mC\lambda^{\mathsf{KT}}\_{n}\to\frac{\mu(P)-m}{C}, λn𝖦𝖱𝖠𝖯𝖠→λ𝖪𝖾𝗅𝗅𝗒\lambda^{\mathsf{GRAPA}}\_{n}\to\lambda^{\mathsf{Kelly}}, and λn𝖺𝖦𝖱𝖠𝖯𝖠→μ​(P)−mσ2​(P)+(μ​(P)−m)2\lambda^{\mathsf{aGRAPA}}\_{n}\to\frac{\mu(P)-m}{\sigma^{2}(P)+(\mu(P)-m)^{2}} that is some functional f​(P)f(P) of the distribution PP such that f​(P)=0f(P)=0 for null PP, and 𝔼P​(log⁡(1+f​(P)⋅(X−m)))>0\mathbb{E}\_{P}(\log(1+f(P)\cdot(X-m)))>0 for alternative PP. For readers familiar with statistical lower bounds, it is also tempting to relate sum-of-squares criterion [Theorem 2.1](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem1 "Theorem 2.1 (Sum-of-squares criterion). ‣ 2.1 Necessary and sufficient condition for null bankruptcy ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") or the n−1/2n^{-1/2} criterion [Corollary 2.4](https://arxiv.org/html/2602.08888v1#S2.Thmtheorem4 "Corollary 2.4 (𝑛^{-1/2} criterion). ‣ 2.3 Null bankruptcy of KT, GRAPA, aGRAPA, etc. ‣ 2 Bankruptcy of predictable plug-in and hedging ‣ Almost sure null bankruptcy of testing-by-betting strategies") to the Cramér-Rao bounds. Indeed, they all concern the optimal n−1/2n^{-1/2} rate of regular statistical estimation problems. If a strategy’s bet fractions (λn)(\lambda\_{n}) estimate one such functional f​(P)f(P) subject to some Cramér-Rao bounds, can we show the null bankruptcy of the strategy since |λn−f​(P)||\lambda\_{n}-f(P)|, which is |λn||\lambda\_{n}| under the null, is at least ≈n−1/2\approx n^{-1/2}?

A closer look at the Cramér-Rao bounds suggests otherwise. With some additional regularity assumptions on f​(P)f(P) and λn\lambda\_{n}, the Cramér-Rao bounds lower bound the *mean-square errors* of these estimators:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼P​((λn−f​(P))2)=Ω​(n−1).\mathbb{E}\_{P}((\lambda\_{n}-f(P))^{2})=\Omega(n^{-1}). |  | (109) |

However, it is easy to see that these variance bounds would imply neither λn−f​(P)=Ωp​(n−1/2)\lambda\_{n}-f(P)=\Omega\_{p}(n^{-1/2}) nor ∑n=1∞(λn−f​(P))2=∞\sum\_{n=1}^{\infty}(\lambda\_{n}-f(P))^{2}=\infty; a sequence of random variables may have infinite expected values while vanishing to 0 at an arbitrarily fast almost sure rate.