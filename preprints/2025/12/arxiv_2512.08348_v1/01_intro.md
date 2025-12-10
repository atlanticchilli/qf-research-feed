---
authors:
- Laurence Carassus
- Miklós Rásonyi
doc_id: arxiv:2512.08348v1
family_id: arxiv:2512.08348
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'On the existence of personal equilibriaThe first author gratefully acknowledges
  the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003.
  The second author gratefully acknowledges the support of the National Research,
  Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and
  also within the framework of the Thematic Excellence Program 2021 (National Research
  subprogramme “Artificial intelligence, large networks, data security: mathematical
  foundation and applications”).'
url_abs: http://arxiv.org/abs/2512.08348v1
url_html: https://arxiv.org/html/2512.08348v1
venue: arXiv q-fin
version: 1
year: 2025
---


Laurence Carassus
Université Paris-Saclay, Centrale-Supélec, Mathématiques et Informatique pour la Complexité et les Systèmes and CNRS FR-3487, 91190, Gif-sur-Yvette, France; laurence.carassus@centralesupelec.fr
  
Miklós Rásonyi
HUN-REN Alfréd Rényi Institute of Mathematics and Eötvös Loránd University, Budapest,
Hungary; rasonyi@renyi.hu

(December 9, 2025)

###### Abstract

We consider an investor who, while maximizing his/her expected utility, also compares the outcome to a reference entity.
We recall the notion of personal equilibrium and show that, in a multistep, generically incomplete financial market model
such an equilibrium indeed exists, under appropriate technical assumptions.

JEL Classification: G11, G12.

AMS Mathematics Subject Classification (2020): 91G10, 91G80.

## 1 Introduction

It was first suggested by [[15](https://arxiv.org/html/2512.08348v1#bib.bib15)] that utility for an economic agent should be
defined not on wealth itself but on gains and losses relative to some reference point (present wealth in [[15](https://arxiv.org/html/2512.08348v1#bib.bib15)]).
Prospect theory, introduced in [[8](https://arxiv.org/html/2512.08348v1#bib.bib8)], is also based on comparison to a reference point. Becoming a cornerstone of
behavioural economics, this theory led to further developments, involving probability distortions, see [[18](https://arxiv.org/html/2512.08348v1#bib.bib18)].

The papers [[2](https://arxiv.org/html/2512.08348v1#bib.bib2), [14](https://arxiv.org/html/2512.08348v1#bib.bib14)] treated models with “disappointment aversion” where the actual outcome of
an investment is compared to an expected outcome via a gain-loss function. In [[9](https://arxiv.org/html/2512.08348v1#bib.bib9)] the
outcome of the investment and the reference point are compared pointwise.
See [[16](https://arxiv.org/html/2512.08348v1#bib.bib16)] for a review of reference-based
preferences.

Our starting point is the model of [[9](https://arxiv.org/html/2512.08348v1#bib.bib9)], further investigated in
[[10](https://arxiv.org/html/2512.08348v1#bib.bib10), [11](https://arxiv.org/html/2512.08348v1#bib.bib11), [12](https://arxiv.org/html/2512.08348v1#bib.bib12)]. A significant novelty of these papers is that the authors define the notion of *personal equilibrium*:
investors should rationally choose an action that is optimal when played against a reference point that is
an independent copy of *itself*.

The first natural question is whether such equilibria are realizable at all.
In one-step models, personal equilibria have been characterized in [[6](https://arxiv.org/html/2512.08348v1#bib.bib6)], under mild conditions.
Characterization has been given for complete markets, too, in [[7](https://arxiv.org/html/2512.08348v1#bib.bib7)].

Most markets of interest, however, are incomplete and have multiple time steps.
It is thus a fundamental question whether personal equilibria exist in such market models, too.
As far as we know, this problem has not been addressed elsewhere yet.

In order to demonstrate that the notion of
personal equilibrium has a bearing on practically relevant situations, we will prove its existence
in a fairly general setting of multi-step (generically incomplete) models. In this way, we provide a reassuring theoretical
guarantee that this notion is non-void for sufficiently complex models of financial markets.
As usual, our equilibrium considerations will be based on the existence of fixed points which, in the present case, requires
rather involved arguments. We show continuous dependence of the strategies “on the past” which allows to apply Schauder’s
fixed point theorem in a Banach space of continuous functions. We further rely on results of
[[5](https://arxiv.org/html/2512.08348v1#bib.bib5)] where continuity of strategies with respect to preferences was established.

Section [2](https://arxiv.org/html/2512.08348v1#S2 "2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") rigorously formulates our assumptions and main theorem. Proofs are given in Section [3](https://arxiv.org/html/2512.08348v1#S3 "3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), while
Section [4](https://arxiv.org/html/2512.08348v1#S4 "4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") presents certain technical results that are used in our main line of arguments.

## 2 Model assumptions and results

Throughout this paper, we will be working on a probability space
(Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). All sigma-algebras will
be assumed to be completed with respect to ℙ\mathbb{P}, without further mention.
Expectation under ℙ\mathbb{P} will be denoted by 𝔼​[⋅]\mathbb{E}[\cdot], ℝ+:={x∈ℝ:x≥0}\mathbb{R}\_{+}:=\{x\in\mathbb{R}:x\geq 0\}, |x||x| is for the Euclidean norm of x∈ℝkx\in\mathbb{R}^{k}, whatever k≥1k\geq 1,
and ℬ​(X)\mathcal{B}(X) designates the Borel sigma-algebra on any topological space XX.

### 2.1 Hypotheses on the financial market model

We first elaborate on the information structure.
We postulate that the filtration is generated by a sequence of bounded independent random variables, and the probability space is large enough to support an auxiliary random variable that will be used in the statements
of our results below.

###### Assumption 2.1.

Let m≥1m\geq 1 be an integer.

1. 1.

   Let
   εt\varepsilon\_{t}, 1≤t≤T1\leq t\leq T be ℝm\mathbb{R}^{m}-valued independent random variables. The investor’s decisions
   are based on the (completed) natural filtration ℱtε:=σ​(ε1,…,εt)\mathcal{F}^{\varepsilon}\_{t}:=\sigma(\varepsilon\_{1},\ldots,\varepsilon\_{t}), 1≤t≤T1\leq t\leq T.
   (ℱ0ε\mathcal{F}^{\varepsilon}\_{0} coincides with the ℙ\mathbb{P}-null sets.)
2. 2.

   Moreover, the εt\varepsilon\_{t} are bounded, say, |εt|≤Cε|\varepsilon\_{t}|\leq C\_{\varepsilon}, 1≤t≤T1\leq t\leq T for some
   constant CεC\_{\varepsilon}.
3. 3.

   There is a random variable ε^\hat{\varepsilon} which is
   independent of ℱTε\mathcal{F}^{\varepsilon}\_{T} and is uniformly distributed on [0,1][0,1].

An element of ℝT×m\mathbb{R}^{T\times m} will be denoted most often by ee, where e=(e1,…,eT)e=(e\_{1},\ldots,e\_{T}) with et∈ℝme\_{t}\in\mathbb{R}^{m}
for 1≤t≤T1\leq t\leq T. If e∈ℝT×me\in\mathbb{R}^{T\times m} then ete^{t} will refer to (e1,…,et)(e\_{1},\ldots,e\_{t}), for 1≤t≤T1\leq t\leq T.

A risky asset with price StS\_{t} at time tt will be considered.
We stipulate that
price increments are Hölder-continuous, bounded functions of the factors generating the investor’s filtration (ℱtε)0≤t≤T(\mathcal{F}^{\varepsilon}\_{t})\_{0\leq t\leq T}.

###### Assumption 2.2.

The initial price S0S\_{0} is constant.
For 1≤t≤T1\leq t\leq T there exist functions ft:ℝt×m→ℝf\_{t}:\mathbb{R}^{t\times m}\to\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | Δ​St:=St−St−1=ft​(ε1,…,εt).\Delta S\_{t}:=S\_{t}-S\_{t-1}=f\_{t}(\varepsilon\_{1},\ldots,\varepsilon\_{t}). |  |

For all 1≤t≤T1\leq t\leq T and for all et,e¯t∈ℝt×me^{t},\bar{e}^{t}\in\mathbb{R}^{t\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ft​(et)−ft​(e¯t)|≤Cf​|et−e¯t|χ,\displaystyle|f\_{t}(e^{t})-f\_{t}(\bar{e}^{t})|\leq C\_{f}|e^{t}-\bar{e}^{t}|^{\chi}, |  | (1) |

for some Cf>0C\_{f}>0, 0<χ≤1,0<\chi\leq 1, and for all 1≤t≤T1\leq t\leq T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supet∈ℝt×m|ft​(et)|≤Cf.\displaystyle\sup\_{e^{t}\in\mathbb{R}^{t\times m}}|f\_{t}(e^{t})|\leq C\_{f}. |  | (2) |

In particular, Assumption [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") implies that each ftf\_{t} is Borel measurable and the process (St)0≤t≤T(S\_{t})\_{0\leq t\leq T} is adapted to
the filtration (ℱtε)0≤t≤T(\mathcal{F}\_{t}^{\varepsilon})\_{0\leq t\leq T}.

###### Remark 2.3.

It is enough to postulate ([1](https://arxiv.org/html/2512.08348v1#S2.E1 "In Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([2](https://arxiv.org/html/2512.08348v1#S2.E2 "In Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) on the compact set Kt:=[−Cε,Cε]tK\_{t}:=[-C\_{\varepsilon},C\_{\varepsilon}]^{t} for all 1≤t≤T1\leq t\leq T, see Proposition [4.1](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below.

The next “uniform no-arbitrage” assumption has already been used multiple times in optimal investment problems,
see [[4](https://arxiv.org/html/2512.08348v1#bib.bib4), [5](https://arxiv.org/html/2512.08348v1#bib.bib5)].
It expresses that future price movements conditioned to the past make a move of at least a prescribed size both up and down, with at least a fixed positive probability. The word “uniform” comes from the fact that
α\alpha does not depend on et−1e^{t-1}.

###### Assumption 2.4.

There is 0<α≤10<\alpha\leq 1 such that, for all 1≤t≤T1\leq t\leq T, for all et−1∈ℝ(t−1)×me^{t-1}\in\mathbb{R}^{(t-1)\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[ft​(et−1,εt)≥α]≥α,ℙ​[ft​(et−1,εt)≤−α]≥α.\mathbb{P}[f\_{t}(e^{t-1},\varepsilon\_{t})\geq\alpha]\geq\alpha,\quad\mathbb{P}[f\_{t}(e^{t-1},\varepsilon\_{t})\leq-\alpha]\geq\alpha. |  | (3) |

(In the case t=1t=1 we mean f1​(e0,ε1):=f1​(ε1)f\_{1}(e^{0},\varepsilon\_{1}):=f\_{1}(\varepsilon\_{1}).)

###### Remark 2.5.

Translated into the language of conditional probabilities, ([3](https://arxiv.org/html/2512.08348v1#S2.E3 "In Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) means

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Δ​St≥α|ℱt−1ε]≥α,ℙ​[Δ​St≤−α|ℱt−1ε]≥αa.s.\mathbb{P}[\Delta S\_{t}\geq\alpha|\mathcal{F}^{\varepsilon}\_{t-1}]\geq\alpha,\quad\mathbb{P}[\Delta S\_{t}\leq-\alpha|\mathcal{F}^{\varepsilon}\_{t-1}]\geq\alpha\quad\mbox{a.s.} |  |

###### Example 2.6.

Let for all 1≤t≤T1\leq t\leq T, μt,σt:ℝt−1→ℝ\mu\_{t},\sigma\_{t}:\mathbb{R}^{t-1}\to\mathbb{R}
be bounded Hölder continuous functions (we mean that μ1,σ1\mu\_{1},\sigma\_{1} are constants).
Let 0<δ≤10<\delta\leq 1, C>0C>0 be such that |σt+1|+|μt+1|≤C|\sigma\_{t+1}|+|\mu\_{t+1}|\leq C and

|  |  |  |
| --- | --- | --- |
|  | |μt+1​(et)−μt+1​(e¯t)|+|σt+1​(et)−σt+1​(e¯t)|≤C​|et−e¯t|δ,|\mu\_{t+1}(e^{t})-\mu\_{t+1}(\bar{e}^{t})|+|\sigma\_{t+1}(e^{t})-\sigma\_{t+1}(\bar{e}^{t})|\leq C|e^{t}-\bar{e}^{t}|^{\delta}, |  |

for all 0≤t≤T−10\leq t\leq T-1 and for all et,e¯t∈ℝte^{t},\bar{e}^{t}\in\mathbb{R}^{t}. We assume that σt≥c>0\sigma\_{t}\geq c>0.
Let εt\varepsilon\_{t}, 1≤t≤T1\leq t\leq T be ℝ\mathbb{R}-valued bounded independent random variables (that is, m=1m=1) such that there exists
β>0\beta>0 with
ℙ​[εt≤−C−βc]≥β\mathbb{P}\bigl[\varepsilon\_{t}\leq\frac{-C-\beta}{c}\bigr]\geq\beta and
ℙ​[εt≥C+βc]≥β\mathbb{P}\bigl[\varepsilon\_{t}\geq\frac{C+\beta}{c}\bigr]\geq\beta for all 1≤t≤T1\leq t\leq T.
Let S0S\_{0} be constant and define the price process for all 1≤t≤T−11\leq t\leq T-1, recursively as

|  |  |  |
| --- | --- | --- |
|  | Δ​St+1=μt+1​(ε1,…,εt)+σt+1​(ε1,…,εt)​εt+1.\Delta S\_{t+1}=\mu\_{t+1}(\varepsilon\_{1},\ldots,\varepsilon\_{t})+\sigma\_{t+1}(\varepsilon\_{1},\ldots,\varepsilon\_{t})\varepsilon\_{t+1}. |  |

Then Assumptions [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") and [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") hold, see Lemma
[4.2](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below.

Now we describe the investor’s activities in the market.
Fix initial capital x0∈ℝx\_{0}\in\mathbb{R}. Predictable trading strategies
ϕ=(ϕ1,…,ϕT)\phi=(\phi\_{1},\ldots,\phi\_{T}) are such that ϕt\phi\_{t} is a ℱt−1ε\mathcal{F}^{\varepsilon}\_{t-1}-measurable
random variable, representing the investor’s position in the risky asset at time tt, for all 1≤t≤T1\leq t\leq T.
The set of all such strategies is denoted by Φ\Phi. We assume that there is a bank account with 0 interest rate in the market.

Trading according to ϕ∈Φ\phi\in\Phi in a self-financing way, portfolio value from initial capital x0x\_{0} at times 0≤t≤T0\leq t\leq T is then defined as

|  |  |  |
| --- | --- | --- |
|  | Wt​(x0,ϕ):=x0+∑j=1tϕj​Δ​Sj.W\_{t}(x\_{0},\phi):=x\_{0}+\sum\_{j=1}^{t}\phi\_{j}\Delta S\_{j}. |  |

We remark that, by Doob’s theorem, for each ϕ∈Φ\phi\in\Phi one can find Borel measurable
functions φt:ℝ(t−1)×m→ℝ\varphi\_{t}:\mathbb{R}^{(t-1)\times m}\to\mathbb{R},
1≤t≤T1\leq t\leq T such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt=φt​(ε1,…,εt−1).\phi\_{t}=\varphi\_{t}(\varepsilon\_{1},\ldots,\varepsilon\_{t-1}). |  | (4) |

(In the case t=1t=1 we mean that ϕ1=φ1\phi\_{1}=\varphi\_{1} is
a constant). Keeping this in mind, we now introduce the reference points corresponding to possible portfolio strategies.

The “extra randomness” provided by ε^\hat{\varepsilon} in Assumption [2.1](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") enables us to fabricate an
independent copy (ε^1,…,ε^T)(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{T}) of (ε1,…,εT)(\varepsilon\_{1},\ldots,\varepsilon\_{T}) in the next lemma,
whose proof is relegated to Section [4](https://arxiv.org/html/2512.08348v1#S4 "4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

###### Lemma 2.7.

There is a Borel measurable function Υ:[0,1]→ℝT×m\Upsilon:[0,1]\to\mathbb{R}^{T\times m} such that Υ​(ε^)\Upsilon(\hat{\varepsilon}) has the
same law as (ε1,…,εT)(\varepsilon\_{1},\ldots,\varepsilon\_{T}). We shall write (ε^1,…,ε^T)(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{T})
for Υ​(ε^)\Upsilon(\hat{\varepsilon}).

For any strategy ϕ∈Φ{\phi}\in\Phi, we define “the independent copy of its final wealth” by

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(ϕ):=x0+∑t=1Tφt​(ε^1,…,ε^t−1)​ft​(ε^1,…,ε^t),\displaystyle B({\phi}):=x\_{0}+\sum\_{t=1}^{T}\varphi\_{t}(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{t-1})f\_{t}(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{t}), |  | (5) |

where the φt\varphi\_{t} are as in ([4](https://arxiv.org/html/2512.08348v1#S2.E4 "In 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). We sometimes write B​(ϕ)=WT​(x0,ϕ)​(ε^T).B({\phi})=W\_{T}(x\_{0},\phi)(\hat{\varepsilon}^{T}).

This definition deserves some explanation. We imagine that independent copies
ft​(ε^1,…,ε^t)f\_{t}(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{t}) of the price increments Δ​St\Delta S\_{t}
exist “somewhere” and one can trade in this
asset following the strategy ϕ\phi, but using the driving factor ε^t\hat{\varepsilon}\_{t} instead of εt\varepsilon\_{t}.
To cut a long story short, B​(ϕ)B(\phi) is independent of the financial market the investor is trading in, but its distribution
is the same as that of WT​(x0,ϕ)W\_{T}(x\_{0},\phi). In the model proposed by [[9](https://arxiv.org/html/2512.08348v1#bib.bib9)], the investor compares his/her
portfolio performance to a reference entity of such type, see the next subsection for more details.

### 2.2 Hypotheses on the investor’s preferences

We consider a utility function satisfying the following properties.

###### Assumption 2.8.

1. 1.

   U:ℝ→ℝU:\mathbb{R}\to\mathbb{R} is twice continuously differentiable.
2. 2.

   UU is non-decreasing, bounded from above, that is, there is CU>0C\_{U}>0 such that U​(x)≤CUU(x)\leq C\_{U} for all x∈ℝx\in\mathbb{R}.
3. 3.

   For all xx, U′′​(x)<0U^{\prime\prime}(x)<0.

###### Remark 2.9.

Clearly, Assumption [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") implies that UU is strictly concave and strictly increasing. Also, |U′′||U^{\prime\prime}| and U′U^{\prime} are bounded away from 0
on every bounded set.

Next, we list our hypotheses about the gain-loss function ν\nu.

###### Assumption 2.10.

1. 1.

   ν:ℝ→ℝ\nu:\mathbb{R}\to\mathbb{R} is twice continuously differentiable, ν​(0)=0\nu(0)=0.
2. 2.

   ν\nu is bounded from above, and ν′′\nu^{\prime\prime} is bounded. That is, there is Cν>0C\_{\nu}>0 such that ν​(x)≤Cν\nu(x)\leq C\_{\nu} and |ν′′​(x)|≤Cν|\nu^{\prime\prime}(x)|\leq C\_{\nu} for all x∈ℝx\in\mathbb{R}.
3. 3.

   ν​(x)=k−​x\nu(x)=k\_{-}x for x≤0x\leq 0 with some k−>0k\_{-}>0.
4. 4.

   On (0,∞)(0,\infty), ν′\nu^{\prime} is nonincreasing and 0<ν′<k−0<\nu^{\prime}<k\_{-}.

###### Remark 2.11.

Note that under
Assumption [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), ν\nu is concave and stricly increasing on ℝ\mathbb{R}, and,

|  |  |  |
| --- | --- | --- |
|  | 0<ν′​(x)≤k−,x∈ℝ.0<\nu^{\prime}(x)\leq k\_{-},\ x\in\mathbb{R}. |  |

Using the Newton-Leibniz rule, this implies, for all x,y∈ℝx,y\in\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ν​(x)−ν​(y)|=|∫yxν′​(t)​𝑑t|≤k−​|x−y|.|\nu(x)-\nu(y)|=\big|\int\_{y}^{x}\nu^{\prime}(t)\,dt\big|\leq k\_{-}|x-y|. |  | (6) |

###### Remark 2.12.

In [[9](https://arxiv.org/html/2512.08348v1#bib.bib9)] the following assumptions were made about ν\nu:

* A0

  ν\nu is continuous, twice continuously differentiable on ℝ∖{0}\mathbb{R}\setminus\{0\}, ν​(0)=0\nu(0)=0.
* A1

  ν\nu is strictly increasing.
* A2

  For all 0<x<y0<x<y, ν​(y)−ν​(x)<ν​(−x)−ν​(−y)\nu(y)-\nu(x)<\nu(-x)-\nu(-y).
* A3

  ν′′​(x)≥0\nu^{\prime\prime}(x)\geq 0 for x<0x<0 and ν′′​(x)≤0\nu^{\prime\prime}(x)\leq 0 for x>0x>0.
* A4

  ν′​(0+)/ν′​(0−)<1\nu^{\prime}(0+)/\nu^{\prime}(0-)<1

One can easily check that ν\nu as in Assumption [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") satisfies A0–A3 above.

In [[6](https://arxiv.org/html/2512.08348v1#bib.bib6)] and [[7](https://arxiv.org/html/2512.08348v1#bib.bib7)] the specification ν0​(x)=α1​x\nu\_{0}(x)=\alpha\_{1}x, x<0x<0, ν0​(x)=α2​x\nu\_{0}(x)=\alpha\_{2}x, x≥0x\geq 0
with 0<α2<α10<\alpha\_{2}<\alpha\_{1} was assumed.
We deviate from both [[6](https://arxiv.org/html/2512.08348v1#bib.bib6)] and [[7](https://arxiv.org/html/2512.08348v1#bib.bib7)].
We still take ν\nu linear on the negative axis, but we assume it is twice continuously differentiable and bounded from above on the whole
of ℝ\mathbb{R}. Necessarily, we *do not* assume A4 above.
Incorporating functions like ν0\nu\_{0} is left for future research.

Let BB be an arbitrary σ​(ε^1,…,ε^T)\sigma(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{T})-measurable random variable that will represent the
reference point of the investor.
Following [[9](https://arxiv.org/html/2512.08348v1#bib.bib9)], we define the investor’s overall satisfaction from xx dollars by

|  |  |  |
| --- | --- | --- |
|  | U​(x,B)=U​(x)+ν​(U​(x)−U​(B)),x∈ℝ.U(x,B)=U(x)+\nu\bigl(U(x)-U(B)\bigr),\ x\in\mathbb{R}. |  |

This is easy to interpret: in addition to the direct utility U​(x)U(x) of xx, the investor also evaluates, using the gain-loss function ν\nu,
whether U​(x)U(x) exceeds or falls short of the reference utility U​(B)U(B).

### 2.3 Personal equilibrium

We now define the value function of the optimization problem we are dealing with. For each ϕ∈Φ\phi\in\Phi,
recalling B​(ϕ)B({\phi}) from ([5](https://arxiv.org/html/2512.08348v1#S2.E5 "In 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")),
set

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(x0,ϕ):=supψ∈Φ𝔼​[U​(WT​(x0,ψ),B​(ϕ))].\displaystyle u(x\_{0},\phi):=\sup\_{\psi\in\Phi}\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi),B(\phi)\bigr)\bigr]. |  | (7) |

A personal equilibrium is a portfolio ϕ†\phi^{\dagger} such that, choosing its “independent copy” B​(ϕ†)B(\phi^{\dagger}) as reference point,
the solution of the resulting optimization problem is just ϕ†\phi^{\dagger} itself. We formalize this heuristic description as follows.

###### Definition 2.13.

A strategy ϕ†∈Φ\phi^{\dagger}\in\Phi is called a *personal equilibrium* if

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U​(WT​(x0,ϕ†),B​(ϕ†))]=supψ∈Φ𝔼​[U​(WT​(x0,ψ),B​(ϕ†))]=u​(x0,ϕ†).\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\phi^{\dagger}),B(\phi^{\dagger})\bigr)\bigr]=\sup\_{\psi\in\Phi}\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi),B(\phi^{\dagger})\bigr)\bigr]=u(x\_{0},\phi^{\dagger}). |  |

The set of personal equilibria is denoted by Φ†\Phi^{\dagger}.
Furthermore, ϕ‡∈Φ†\phi^{\ddagger}\in\Phi^{\dagger} is called a *preferred personal equilibrium* if

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U​(WT​(x0,ϕ‡),B​(ϕ‡))]=supϕ†∈Φ†𝔼​[U​(WT​(x0,ϕ†),B​(ϕ†))].\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\phi^{\ddagger}),B(\phi^{\ddagger})\bigr)\bigr]=\sup\_{\phi^{\dagger}\in\Phi^{\dagger}}\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\phi^{\dagger}),B(\phi^{\dagger})\bigr)\bigr]. |  |

The set of preferred personal equilibria is denoted by Φ‡\Phi^{\ddagger}.

Preferred personal equilibria are thus the best-performing personal equilibria. It is not at all clear,
whether Φ†\Phi^{\dagger} or Φ‡\Phi^{\ddagger} are non-empty. Our principal result answers these questions in the affirmative.

###### Theorem 2.14.

Let Assumptions [2.1](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") and [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") be in force. Then
Φ†≠∅\Phi^{\dagger}\neq\emptyset and, actually, a preferred personal equilibrium exists, i.e. Φ‡≠∅\Phi^{\ddagger}\neq\emptyset.

###### Remark 2.15.

We know from Theorem 3.2 of [[6](https://arxiv.org/html/2512.08348v1#bib.bib6)] that there is no uniqueness for personal equilibria. We do not know
if there is uniqueness for *preferred* personal equilibria.

## 3 Proofs

### 3.1 One-step case

In this subsection, we solve a one-step optimization problem that will later be recursively applied to construct an optimal strategy for an investor in a multi-step market with utility function U​(x,B)U(x,B), see Proposition [3.4](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below.

###### Assumption 3.1.

Let 1≤t≤T1\leq t\leq T be given. Let a random variable BB be also given (this parametrizes the problem with respect to the
reference point).
We consider a ℬ​(ℝt×m)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{t\times m})\otimes\mathcal{B}(\mathbb{R})-measurable function

|  |  |  |
| --- | --- | --- |
|  | V​(B):ℝt×m×ℝ→ℝV(B):\mathbb{R}^{t\times m}\times\mathbb{R}\to\mathbb{R} |  |

such that, for all e∈ℝt×me\in\mathbb{R}^{t\times m}, x↦V​(B)​(e,x)x\mapsto V(B)(e,x) is twice continuously differentiable and bounded from above by CU+CνC\_{U}+C\_{\nu}.

There are continuous functions iV,jV,JV,ℓV,LVi\_{V},j\_{V},J\_{V},\ell\_{V},L\_{V} such that
iV:ℝ→ℝi\_{V}:\mathbb{R}\to\mathbb{R} and jV,JV,ℓV,LV:ℝ→(0,∞)j\_{V},J\_{V},\ell\_{V},L\_{V}:\mathbb{R}\to(0,\infty), and for all e,xe,x,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | iV​(x)\displaystyle i\_{V}(x) | ≤V​(B)​(e,x),jV​(x)≤V​(B)′​(e,x)≤JV​(x)\displaystyle\leq V(B)(e,x),\quad j\_{V}(x)\leq V(B)^{\prime}(e,x)\leq J\_{V}(x) |  | (8) |
|  | ℓV​(x)\displaystyle\ell\_{V}(x) | ≤−V​(B)′′​(e,x)≤LV​(x).\displaystyle\leq-V(B)^{\prime\prime}(e,x)\leq L\_{V}(x). |  |

Here V​(B)′,V​(B)′′V(B)^{\prime},V(B)^{\prime\prime} refer to derivatives with respect to xx.

Furthermore, there are θ∈(0,χ]\theta\in(0,\chi], and a continuous function CV:ℝ→ℝ+C\_{V}:\mathbb{R}\to\mathbb{R}\_{+} such that,
for each e,e¯∈ℝt×me,\bar{e}\in\mathbb{R}^{t\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |V​(B)​(e,x)−V​(B)​(e¯,x)|≤CV​(x)​|e−e¯|θ.|V(B)(e,x)-V(B)(\bar{e},x)|\leq C\_{V}(x)|e-\bar{e}|^{\theta}. |  | (9) |

Let ε\varepsilon be an ℝm\mathbb{R}^{m}-valued random variable with |ε|≤Cε|\varepsilon|\leq C\_{\varepsilon}.
There is a Borel function f:ℝt×m→ℝf:\mathbb{R}^{t\times m}\to\mathbb{R} such that,
for all o∈ℝ(t−1)×mo\in\mathbb{R}^{(t-1)\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[f​(o,ε)≥α]≥α,ℙ​[f​(o,ε)≤−α]≥α,\mathbb{P}[f(o,\varepsilon)\geq\alpha]\geq\alpha,\quad\mathbb{P}[f(o,\varepsilon)\leq-\alpha]\geq\alpha, |  | (10) |

and for all e,e¯∈ℝt×me,\bar{e}\in\mathbb{R}^{t\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |f​(e)−f​(e¯)|≤Cf​|e−e¯|χ,supe∈ℝt×m|f​(e)|≤Cf.|f(e)-f(\bar{e})|\leq C\_{f}|e-\bar{e}|^{\chi},\quad\sup\_{e\in\mathbb{R}^{t\times m}}|f(e)|\leq C\_{f}. |  | (11) |

In ([10](https://arxiv.org/html/2512.08348v1#S3.E10 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we write f​(o,ε)f(o,\varepsilon) instead of f​((o,ε))f((o,\varepsilon)) for the sake of simplicity, and we will use the same kind of notations in the rest of the paper. Remark that under Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), x↦V​(B)​(e,x)x\mapsto V(B)(e,x) is strictly increasing and strictly concave. Remark also that the functions jV,JV,ℓV,LVj\_{V},J\_{V},\ell\_{V},L\_{V} are continuous and strictly positive, hence
locally bounded away from 0.

The above assumption will be in force throughout this subsection.
We introduce the two following functions, for all (o,x,h)∈ℝ(t−1)×m×ℝ×ℝ(o,x,h)\in\mathbb{R}^{(t-1)\times m}\times\mathbb{R}\times\mathbb{R}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Γ​(B)​(o,x,h)\displaystyle\Gamma(B)(o,x,h) | :=\displaystyle:= | 𝔼​[V​(B)​(o,ε,x+h​f​(o,ε))],\displaystyle\mathbb{E}\bigl[V(B)\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)\bigr], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ​(B)​(o,x,h)\displaystyle\gamma(B)(o,x,h) | :=\displaystyle:= | 𝔼​[V​(B)′​(o,ε,x+h​f​(o,ε))​f​(o,ε)].\displaystyle\mathbb{E}\bigl[V(B)^{\prime}\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)f(o,\varepsilon)\bigr]. |  |

###### Lemma 3.2.

Under Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."),
γ​(B)\gamma(B) and Γ​(B)\Gamma(B) are well-defined Carathéodory integrands, i.e. for all (x,h)(x,h), o↦γ​(B)​(o,x,h),Γ​(B)​(o,x,h)o\mapsto\gamma(B)(o,x,h),\Gamma(B)(o,x,h) are ℬ​(ℝ(t−1)×m)\mathcal{B}(\mathbb{R}^{(t-1)\times m})-measurable functions,
and (x,h)↦γ​(B)​(o,x,h),Γ​(B)​(o,x,h)(x,h)\mapsto\gamma(B)(o,x,h),\Gamma(B)(o,x,h) are continuous functions for all oo.
Moreover, for all oo, the function (x,h)↦Γ​(B)​(o,x,h)(x,h)\mapsto\Gamma(B)(o,x,h) is twice continuously differentiable and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂xΓ​(B)​(o,x,h)\displaystyle\partial\_{x}\Gamma(B)(o,x,h) | =\displaystyle= | 𝔼​[V​(B)′​(o,ε,x+h​f​(o,ε))]\displaystyle\mathbb{E}\bigl[V(B)^{\prime}\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)\bigr] |  | (12) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂hΓ​(B)​(o,x,h)\displaystyle\partial\_{h}\Gamma(B)(o,x,h) | =\displaystyle= | 𝔼​[V​(B)′​(o,ε,x+h​f​(o,ε))​f​(o,ε)]=γ​(B)​(o,x,h)\displaystyle\mathbb{E}\bigl[V(B)^{\prime}\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)f(o,\varepsilon)\bigr]=\gamma(B)(o,x,h) |  | (13) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂x​h2Γ​(B)​(o,x,h)\displaystyle\partial^{2}\_{xh}\Gamma(B)(o,x,h) | =\displaystyle= | ∂xγ​(B)​(o,x,h)=𝔼​[V​(B)′′​(o,ε,x+h​f​(o,ε))​f​(o,ε)]\displaystyle\partial\_{x}\gamma(B)(o,x,h)=\mathbb{E}\bigl[V(B)^{\prime\prime}\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)f(o,\varepsilon)\bigr] |  | (14) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂h​h2Γ​(B)​(o,x,h)\displaystyle\partial^{2}\_{hh}\Gamma(B)(o,x,h) | =\displaystyle= | ∂hγ​(B)​(o,x,h)=𝔼​[V​(B)′′​(o,ε,x+h​f​(o,ε))​f2​(o,ε)].\displaystyle\partial\_{h}\gamma(B)(o,x,h)=\mathbb{E}\bigl[V(B)^{\prime\prime}\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)f^{2}(o,\varepsilon)\bigr]. |  | (15) |

###### Proof.

Since iV​(x)≤V​(B)​(⋅,x)≤CU+Cνi\_{V}(x)\leq V(B)(\cdot,x)\leq C\_{U}+C\_{\nu}, jV​(x)≤V​(B)′​(⋅,x)≤JV​(x)j\_{V}(x)\leq V(B)^{\prime}(\cdot,x)\leq J\_{V}(x), −LV​(x)≤V​(B)′′​(e,x)≤−ℓV​(x)-L\_{V}(x)\leq V(B)^{\prime\prime}(e,x)\leq-\ell\_{V}(x) and ff is bounded, the expectations above are well-defined (and finite).
Dominated convergence implies that for all oo, the functions (x,h)↦γ​(B)​(o,x,h),Γ​(B)​(o,x,h)(x,h)\mapsto\gamma(B)(o,x,h),\Gamma(B)(o,x,h) are continuous. Fix x,hx,h. As (o,e)↦x+h​f​(o,e)(o,e)\mapsto x+hf(o,e) and V​(B)V(B) are Borel measurable,
(o,e)↦V​(B)​(o,e,x+h​f​(o,e))(o,e)\mapsto V(B)(o,e,x+hf(o,e)) is Borel measurable and Fubini theorem as in [[3](https://arxiv.org/html/2512.08348v1#bib.bib3), Proposition 7.29] implies that
o↦Γ​(B)​(o,x,h)=𝔼​[V​(B)​(o,ε,x+h​f​(o,ε))]o\mapsto\Gamma(B)(o,x,h)=\mathbb{E}[V(B)(o,\varepsilon,x+hf(o,\varepsilon))] is Borel measurable. The same reasoning applies for
measurability in oo of γ​(B)\gamma(B).

Fix M,N>0M,N>0.
For all (x,h)∈[−M,M]×[−N,N](x,h)\in[-M,M]\times[-N,N], e↦V​(B)​(o,e,x+h​f​(o,e))e\mapsto V(B)\bigl(o,e,x+hf(o,e)\bigr) is integrable with respect to
the law of ε\varepsilon under
ℙ\mathbb{P}, since it is measurable and bounded by max⁡(supz∈D|iV​(z)|,CU+Cν)\max(\sup\_{z\in D}|i\_{V}(z)|,C\_{U}+C\_{\nu}), where D=[−M−N​Cf,M+N​Cf]D=[-M-NC\_{f},M+NC\_{f}].
Moreover, for all e∈ℝt×me\in\mathbb{R}^{t\times m}, (x,h)↦V​(B)​(o,e,x+h​f​(o,e))(x,h)\mapsto V(B)\bigl(o,e,x+hf(o,e)\bigr) is differentiable and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |∂xV​(B)​(o,e,x+h​f​(o,e))|\displaystyle|\partial\_{x}V(B)\bigl(o,e,x+hf(o,e)\bigr)| | =\displaystyle= | |V​(B)′​(o,e,x+h​f​(o,e))|≤supz∈DJV​(z)\displaystyle|V(B)^{\prime}\bigl(o,e,x+hf(o,e)\bigr)|\leq\sup\_{z\in D}J\_{V}(z) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |∂hV​(B)​(o,e,x+h​f​(o,e))|\displaystyle|\partial\_{h}V(B)\bigl(o,e,x+hf(o,e)\bigr)| | =\displaystyle= | |V​(B)′​(o,e,x+h​f​(o,e))​f​(o,e)|≤Cf​supz∈DJV​(z)\displaystyle|V(B)^{\prime}\bigl(o,e,x+hf(o,e)\bigr)f(o,e)|\leq C\_{f}\sup\_{z\in D}J\_{V}(z) |  |

and these are constant bounds.
Thus, dominated convergence implies that (x,h)→Γ​(B)​(o,x,h)(x,h)\to\Gamma(B)(o,x,h) is
differentiable on (−M,M)×(−N,N)(-M,M)\times(-N,N), hence on ℝ2\mathbb{R}^{2} (as MM and NN are arbitrary), and ([12](https://arxiv.org/html/2512.08348v1#S3.E12 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([13](https://arxiv.org/html/2512.08348v1#S3.E13 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) hold true.
The rest of the proof is similar,
using the other bounds of Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").
∎

We define, for all BB, the function v​(B):ℝ(t−1)×m×ℝ→ℝv(B):\mathbb{R}^{(t-1)\times m}\times\mathbb{R}\to\mathbb{R} by

|  |  |  |
| --- | --- | --- |
|  | v(B)(o,x):=suph∈ℝ𝔼[V(B)(o,ε,x+hf(o,ε))]=suph∈ℝΓ(B)(o,x,h),v(B)(o,x):=\sup\_{h\in\mathbb{R}}\mathbb{E}\bigr[V(B)\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)\bigr]={}\sup\_{h\in\mathbb{R}}\Gamma(B)(o,x,h), |  |

for o∈ℝ(t−1)×mo\in\mathbb{R}^{(t-1)\times m}, x∈ℝx\in\mathbb{R}. In the case t=1,t=1, we define

|  |  |  |
| --- | --- | --- |
|  | v(B)(x):=suph∈ℝ𝔼[V(B)(ε,x+hf(ε))].v(B)(x):=\sup\_{h\in\mathbb{R}}\mathbb{E}\bigr[V(B)\bigl(\varepsilon,x+hf(\varepsilon)\bigr)\bigr]. |  |

The following result forms the core of our arguments. It shows that if VV satisfies Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), then vv also satisfies it with a θ/2\theta/2 instead of θ\theta in ([9](https://arxiv.org/html/2512.08348v1#S3.E9 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).

###### Proposition 3.3.

Assume that Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") holds true. There exist functions
Ch:ℝ→(0,∞)C\_{h}:\mathbb{R}\to(0,\infty) and
h¯​(B):ℝ(t−1)×m×ℝ→ℝ\bar{h}(B):\mathbb{R}^{(t-1)\times m}\times\mathbb{R}\to\mathbb{R}
such that ChC\_{h} is continuous, does not depend on BB, h¯​(B)\bar{h}(B) is ℬ​(ℝ(t−1)×m)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{(t-1)\times m})\otimes\mathcal{B}(\mathbb{R})-measurable, and, for all o,xo,x,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h¯​(B)​(o,x)|≤Ch​(x),|\bar{h}(B)(o,x)|\leq C\_{h}(x), |  | (16) |

and h¯​(B)​(o,x)\bar{h}(B)(o,x) is the unique number that satisfies

|  |  |  |
| --- | --- | --- |
|  | v​(B)​(o,x)=𝔼​[V​(B)​(o,ε,x+h¯​(B)​(o,x)​f​(o,ε))].v(B)(o,x)=\mathbb{E}\bigl[V(B)\bigl(o,\varepsilon,x+\bar{h}(B)(o,x)f(o,\varepsilon)\bigr)\bigr]. |  |

Furthermore, for all o,o¯∈ℝ(t−1)×mo,\bar{o}\in\mathbb{R}^{(t-1)\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h¯​(B)​(o,x)−h¯​(B)​(o¯,x)|≤Ch​(x)​|o−o¯|θ/2.|\bar{h}(B)(o,x)-\bar{h}(B)(\bar{o},x)|\leq C\_{h}(x)|o-\bar{o}|^{\theta/2}. |  | (17) |

The function v​(B)v(B) is ℬ​(ℝ(t−1)×m)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{(t-1)\times m})\otimes\mathcal{B}(\mathbb{R})-measurable, bounded from above by CU+CνC\_{U}+C\_{\nu},
twice continuosly differentiable in its second variable; there is a continuous function Cv:ℝ→(0,∞)C\_{v}:\mathbb{R}\to(0,\infty), that does not depend on BB,
such that for all o,o¯∈ℝ(t−1)×mo,\bar{o}\in\mathbb{R}^{(t-1)\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v​(B)​(o,x)−v​(B)​(o¯,x)|≤Cv​(x)​|o−o¯|θ/2.\displaystyle|v(B)(o,x)-v(B)(\bar{o},x)|\leq C\_{v}(x)|o-\bar{o}|^{\theta/2}. |  | (18) |

There exist continuous functions iv,jv,Jv,ℓv,Lvi\_{v},j\_{v},J\_{v},\ell\_{v},L\_{v}, that do not depend on BB, such that
iv:ℝ→ℝi\_{v}:\mathbb{R}\to\mathbb{R} and jv,Jv,ℓv,Lv:ℝ→(0,∞)j\_{v},J\_{v},\ell\_{v},L\_{v}:\mathbb{R}\to(0,\infty), and for all o,xo,x,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | iv​(x)\displaystyle i\_{v}(x) | ≤v​(B)​(o,x),jv​(x)≤v​(B)′​(o,x)≤Jv​(x),\displaystyle\leq v(B)(o,x),\quad j\_{v}(x)\leq v(B)^{\prime}(o,x)\leq J\_{v}(x), |  | (19) |
|  | ℓv​(x)\displaystyle\ell\_{v}(x) | ≤−v​(B)′′​(o,x)≤Lv​(x).\displaystyle\leq-v(B)^{\prime\prime}(o,x)\leq L\_{v}(x). |  |

###### Proof.

We will divide this rather complex proof into several steps. First, as V​(B)V(B) is bounded above by CU+CνC\_{U}+C\_{\nu}, the same
holds true for v​(B)v(B).

Boundedness of optimizer sequences

Fix (o,x)∈ℝ(t−1)×m×ℝ(o,x)\in\mathbb{R}^{(t-1)\times m}\times\mathbb{R}. Let h∈ℝh\in\mathbb{R}.
Define

|  |  |  |
| --- | --- | --- |
|  | Bh:={ω∈Ω:f​(o,ε​(ω))​sgn​(h)≤−α},B\_{h}:=\{\omega\in\Omega:f\big(o,\varepsilon(\omega)\big)\mathrm{sgn}(h)\leq-\alpha\}, |  |

where
sgn​(h)=1\mathrm{sgn}(h)=1 if h≥0h\geq 0 and sgn​(h)=−1\mathrm{sgn}(h)=-1 else.
For hh such that
|x|−α​|h|<0|x|-\alpha|h|<0, using that V​(B)V(B) is nondecreasing and concave in xx, we estimate,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | 𝔼​[V​(B)​(o,ε,x+h​f​(o,ε))]\displaystyle\hskip-56.9055pt\mathbb{E}\bigl[V(B)\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)\bigr] |  |
|  |  | ≤\displaystyle\leq | CU+Cν+𝔼​[1Bh​V​(B)​(o,ε,x+h​f​(o,ε))]\displaystyle C\_{U}+C\_{\nu}+\mathbb{E}\bigl[1\_{B\_{h}}V(B)\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)\bigr] |  |
|  |  | ≤\displaystyle\leq | CU+Cν+𝔼​[1Bh​V​(B)​(o,ε,|x|−α​|h|)]\displaystyle C\_{U}+C\_{\nu}+\mathbb{E}[1\_{B\_{h}}V(B)(o,\varepsilon,|x|-\alpha|h|)] |  |
|  |  | ≤\displaystyle\leq | CU+Cν+𝔼​[1Bh​[V​(B)​(o,ε,0)+V​(B)′​(o,ε,0)​(|x|−α​|h|)]]\displaystyle C\_{U}+C\_{\nu}+\mathbb{E}\bigl[1\_{B\_{h}}[V(B)(o,\varepsilon,0)+V(B)^{\prime}(o,\varepsilon,0)(|x|-\alpha|h|)]\bigr] |  |
|  |  | ≤\displaystyle\leq | 2​(CU+Cν)+𝔼​[1Bh​[jV​(0)​(|x|−α​|h|)]]\displaystyle 2(C\_{U}+C\_{\nu})+\mathbb{E}\bigl[1\_{B\_{h}}[j\_{V}(0)(|x|-\alpha|h|)]\bigr] |  |
|  |  | =\displaystyle= | 2​(CU+Cν)+ℙ​[Bh]​jV​(0)​(|x|−α​|h|)\displaystyle 2(C\_{U}+C\_{\nu})+\mathbb{P}[B\_{h}]j\_{V}(0)(|x|-\alpha|h|) |  |
|  |  | ≤\displaystyle\leq | 2​(CU+Cν)+α​jV​(0)​(|x|−α​|h|),\displaystyle 2(C\_{U}+C\_{\nu})+\alpha j\_{V}(0)(|x|-\alpha|h|), |  |

where we have used ([10](https://arxiv.org/html/2512.08348v1#S3.E10 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) for the last inequality.

If |h|≥[2​(CU+Cν)+|iV​(x)|+jV​(0)​α​|x|]/(jV​(0)​α2)|h|\geq[2(C\_{U}+C\_{\nu})+|i\_{V}(x)|+j\_{V}(0)\alpha|x|]/(j\_{V}(0)\alpha^{2}) then

|  |  |  |
| --- | --- | --- |
|  | 2​(CU+Cν)+α​jV​(0)​(|x|−α​|h|)≤−|iV​(x)|2(C\_{U}+C\_{\nu})+\alpha j\_{V}(0)(|x|-\alpha|h|)\leq-|i\_{V}(x)| |  |

holds.
Let us now set

|  |  |  |
| --- | --- | --- |
|  | K​(x):=|x|α+2​(CU+Cν)+|iV​(x)|+jV​(0)​α​|x|jV​(0)​α2>0.K(x):=\frac{|x|}{\alpha}+\frac{2(C\_{U}+C\_{\nu})+|i\_{V}(x)|+j\_{V}(0)\alpha|x|}{j\_{V}(0)\alpha^{2}}>0. |  |

It is clear from the assumptions that KK is continuous.
If |h|≥K​(x)|h|\geq K(x), then using ([8](https://arxiv.org/html/2512.08348v1#S3.E8 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[V​(B)​(o,ε,x+h​f​(o,ε))]≤−|iV​(x)|≤𝔼​[V​(B)​(o,ε,x)]≤v​(B)​(o,x).\mathbb{E}\bigl[V(B)\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)\bigr]\leq-|i\_{V}(x)|\leq\mathbb{E}[V(B)(o,\varepsilon,x)]\leq v(B)(o,x). |  | (20) |

Existence of optimizer for Γ​(o,x,⋅)\Gamma(o,x,\cdot)

Fix (o,x)∈ℝ(t−1)×m×ℝ(o,x)\in\mathbb{R}^{(t-1)\times m}\times\mathbb{R}. Let hn​(B)​(o,x)∈ℝh\_{n}(B)(o,x)\in\mathbb{R}, n∈ℕn\in\mathbb{N} be a sequence such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[V​(B)​(o,ε,x+hn​(B)​(o,x)​f​(o,ε))]→v​(B)​(o,x),n→∞.\mathbb{E}\bigl[V(B)\bigl(o,\varepsilon,x+h\_{n}(B)(o,x)f(o,\varepsilon)\bigr)\bigr]\to v(B)(o,x),\ n\to\infty.{} |  | (21) |

By ([20](https://arxiv.org/html/2512.08348v1#S3.E20 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we may replace in ([21](https://arxiv.org/html/2512.08348v1#S3.E21 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) hn​(B)h\_{n}(B) by h~n​(B):=hn​(B)​1{|hn​(B)|≤K​(x)}\tilde{h}\_{n}(B):=h\_{n}(B)1\_{\{|h\_{n}(B)|\leq K(x)\}}. By compactness, there is a
subsequence h~n​(k)​(B)\tilde{h}\_{n(k)}(B), k∈ℕk\in\mathbb{N}
such that h~n​(k)​(B)​(o,x)→h¯​(B)​(o,x)\tilde{h}\_{n(k)}(B)(o,x)\to\bar{h}(B)(o,x) for some h¯​(B)​(o,x)\bar{h}(B)(o,x). By Fatou’s lemma and continuity of V​(B)V(B) in xx,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(B)​(o,x)\displaystyle v(B)(o,x) | ≤\displaystyle\leq | 𝔼​[lim supk→∞V​(B)​(o,ε,x+h~n​(k)​(B)​(o,x)​f​(o,ε))]\displaystyle\mathbb{E}\bigl[\limsup\_{k\to\infty}V(B)\bigl(o,\varepsilon,x+\tilde{h}\_{n(k)}(B)(o,x)f(o,\varepsilon)\bigr)\bigr] |  |
|  |  | =\displaystyle= | 𝔼​[V​(B)​(o,ε,x+h¯​(B)​(o,x)​f​(o,ε))].\displaystyle\mathbb{E}\bigl[V(B)\bigl(o,\varepsilon,x+\bar{h}(B)(o,x)f(o,\varepsilon)\bigr)\bigr]. |  |

Since V​(B)V(B) is strictly concave in xx, such h¯​(B)​(o,x)\bar{h}(B)(o,x) is unique.

Differentiability of h¯\bar{h} and v​(B)v(B)

For all (o,x)∈ℝ(t−1)×m×ℝ,(o,x)\in\mathbb{R}^{(t-1)\times m}\times\mathbb{R}, Γ​(B)​(o,x,⋅)\Gamma(B)\bigl(o,x,\cdot\bigr) is differentiable and
([13](https://arxiv.org/html/2512.08348v1#S3.E13 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds.
Since v​(B)​(o,x)=suph∈ℝΓ​(B)​(o,x,h)v(B)(o,x)=\sup\_{h\in\mathbb{R}}\Gamma(B)(o,x,h) and this supremum is attained at h¯​(B)​(o,x)\bar{h}(B)(o,x),
the derivative must be 0 at this point:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(B)​(o,x,h¯​(B)​(o,x))=0.\displaystyle\gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)=0. |  | (22) |

Fix o∈ℝ(t−1)×m.o\in\mathbb{R}^{(t-1)\times m}. Now, we want to apply the implicit function theorem (see p. 150 of Zeidler [[19](https://arxiv.org/html/2512.08348v1#bib.bib19)]) in order to show that h¯​(B)​(o,⋅)\bar{h}(B)(o,\cdot) is differentiable. First, Lemma [3.2](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") shows that γ​(B)​(o,⋅,⋅)\gamma(B)\bigl(o,\cdot,\cdot) is differentiable. So, to apply the implicit function theorem in (x,h¯​(B)​(o,x))(x,\bar{h}(B)(o,x)) for all x∈ℝx\in\mathbb{R}, we need to prove that

|  |  |  |
| --- | --- | --- |
|  | |∂hγ​(B)​(o,x,h¯​(B)​(o,x))|>0.\bigl|\partial\_{h}\gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)\bigr|>0. |  |

In fact, we show that for all (x,h)∈ℝ×ℝ(x,h)\in\mathbb{R}\times\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∂hγ​(B)​(o,x,h)|≥α3​infy∈D​(x)ℓV​(y),|\partial\_{h}\gamma(B)(o,x,h)|\geq\alpha^{3}\inf\_{y\in D(x)}\ell\_{V}(y), |  | (23) |

where α>0\alpha>0 is given in ([10](https://arxiv.org/html/2512.08348v1#S3.E10 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(x):=[x−K​(x)​Cf,x+K​(x)​Cf]D(x):=[x-K(x)C\_{f},x+K(x)C\_{f}] |  | (24) |

Recalling ([15](https://arxiv.org/html/2512.08348v1#S3.E15 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), and using ℓV>0\ell\_{V}>0 and ([10](https://arxiv.org/html/2512.08348v1#S3.E10 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we obtain that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |∂hγ​(B)​(o,x,h)|\displaystyle|\partial\_{h}\gamma(B)(o,x,h)| | =\displaystyle= | −𝔼​[V​(B)′′​(o,ε,x+h​f​(o,ε))​f2​(o,ε)]\displaystyle-\mathbb{E}\bigl[V(B)^{\prime\prime}\bigl(o,\varepsilon,x+hf(o,\varepsilon)\bigr)f^{2}(o,\varepsilon)\bigr] |  |
|  |  | ≥\displaystyle\geq | 𝔼​[ℓV​(x+h​f​(o,ε))​f2​(o,ε)]\displaystyle\mathbb{E}\bigl[\ell\_{V}\bigl(x+hf(o,\varepsilon)\bigr)f^{2}(o,\varepsilon)\bigr] |  |
|  |  | ≥\displaystyle\geq | infy∈D​(x)ℓV​(y)​𝔼​[f2​(o,ε)]≥infy∈D​(x)ℓV​(y)​𝔼​[f2​(o,ε)​1{f​(o,ε)≥α}]\displaystyle\inf\_{y\in D(x)}\ell\_{V}(y)\mathbb{E}\bigl[f^{2}(o,\varepsilon)\bigr]\geq\inf\_{y\in D(x)}\ell\_{V}(y)\mathbb{E}\bigl[f^{2}(o,\varepsilon)1\_{\{f(o,\varepsilon)\geq\alpha\}}\bigr] |  |
|  |  | ≥\displaystyle\geq | α2​infy∈D​(x)ℓV​(y)​ℙ​[f​(o,ε)≥α]\displaystyle\alpha^{2}\inf\_{y\in D(x)}\ell\_{V}(y)\mathbb{P}[f(o,\varepsilon)\geq\alpha] |  |
|  |  | ≥\displaystyle\geq | α3​infy∈D​(x)ℓV​(y).\displaystyle\alpha^{3}\inf\_{y\in D(x)}\ell\_{V}(y). |  |

Since ℓV\ell\_{V} is strictly positive, the conditions of the implicit function theorem
are met in every point xx, and there exist δ​(o)​(x)>0\delta(o)(x)>0 (recall that we have fixed oo), a continuously differentiable function
h^​(B)​(o):(x−δ​(o)​(x),x+δ​(o)​(x))→ℝ\hat{h}(B)(o):(x-\delta(o)(x),x+\delta(o)(x))\to\mathbb{R} such that
for all y∈(x−δ​(o)​(x),x+δ​(o)​(x))y\in(x-\delta(o)(x),x+\delta(o)(x)),

|  |  |  |
| --- | --- | --- |
|  | γ​(B)​(o,y,h^​(B)​(o)​(y))=0.\gamma(B)\bigl(o,y,\hat{h}(B)(o)(y)\bigr)=0. |  |

Now, by the unicity of the root of ([22](https://arxiv.org/html/2512.08348v1#S3.E22 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we necessarily have that for all y∈(x−δ​(o)​(x),x+δ​(o)​(x))y\in(x-\delta(o)(x),x+\delta(o)(x))

|  |  |  |
| --- | --- | --- |
|  | h¯​(B)​(o,y)=h^​(B)​(o)​(y).\bar{h}(B)(o,y)=\hat{h}(B)(o)(y). |  |

So h¯​(B)​(o,⋅)\bar{h}(B)(o,\cdot) is
continuously differentiable in a neighbourhood of xx (which depends of oo). Since this argument works for all xx,
h¯​(B)​(o,⋅)\bar{h}(B)(o,\cdot) is continuously differentiable on the whole real line with the derivative given by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂xh¯​(o,x)\displaystyle\partial\_{x}\bar{h}(o,x) | =\displaystyle= | −∂xγ​(B)​(o,x,h¯​(B)​(o,x))∂hγ​(B)​(o,x,h¯​(B)​(o,x)).\displaystyle-\frac{\partial\_{x}\gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)}{\partial\_{h}\gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)}. |  | (25) |

As oo was arbitrary in ℝ(t−1)×m,\mathbb{R}^{(t-1)\times m}, ([25](https://arxiv.org/html/2512.08348v1#S3.E25 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds for all o∈ℝ(t−1)×m.o\in\mathbb{R}^{(t-1)\times m}.
  
As v​(B)​(o,x)=Γ​(B)​(o,x,h¯​(o,x))v(B)(o,x)=\Gamma(B)(o,x,\bar{h}(o,x)) and x↦h¯​(o,x),Γ​(B)​(o,x,h)x\mapsto\bar{h}(o,x),\Gamma(B)(o,x,h) are differentiable, x↦v​(B)​(o,x)x\mapsto v(B)(o,x) is also differentiable, and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | v​(B)′​(o,x)\displaystyle v(B)^{\prime}(o,x) | =\displaystyle= | ∂xΓ​(B)​(o,x,h¯​(B)​(o,x))+∂hΓ​(B)​(o,x,h¯​(B)​(o,x))​∂xh¯​(o,x)\displaystyle\partial\_{x}\Gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)+\partial\_{h}\Gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)\partial\_{x}\bar{h}(o,x) |  | (26) |
|  |  | =\displaystyle= | ∂xΓ​(B)​(o,x,h¯​(B)​(o,x))\displaystyle\partial\_{x}\Gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr) |  |
|  |  | =\displaystyle= | 𝔼​[V​(B)′​(o,ε,x+h¯​(o,x)​f​(o,ε))],\displaystyle\mathbb{E}\bigl[V(B)^{\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)\bigr], |  |

recalling ([13](https://arxiv.org/html/2512.08348v1#S3.E13 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), ([22](https://arxiv.org/html/2512.08348v1#S3.E22 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([12](https://arxiv.org/html/2512.08348v1#S3.E12 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).

An estimate for Γ\Gamma

We claim that there is a continuous
function A>0A>0 such that, for all x∈ℝx\in\mathbb{R}, |h|≤K​(x)|h|\leq K(x), and o,o¯∈ℝ(t−1)×m{o},\bar{o}\in\mathbb{R}^{(t-1)\times m}

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Γ​(B)​(o,x,h)−Γ​(B)​(o¯,x,h)|≤A​(x)​|o−o¯|θ.\displaystyle|\Gamma(B)(o,x,h)-\Gamma(B)(\bar{o},x,h)|\leq A(x)|o-\bar{o}|^{\theta}. |  | (27) |

Recalling the interval D​(x)D(x) from ([24](https://arxiv.org/html/2512.08348v1#S3.E24 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we can estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Γ​(B)​(o,x,h)|≤CU+Cν+supy∈D​(x)|iV​(y)|,|\Gamma(B)(o,x,h)|\leq C\_{U}+C\_{\nu}+\sup\_{y\in D(x)}|i\_{V}(y)|, |  | (28) |

by ([8](https://arxiv.org/html/2512.08348v1#S3.E8 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and by V​(B)≤CU+CνV(B)\leq C\_{U}+C\_{\nu}.
Furthermore,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |Γ​(B)​(o,x,h)−Γ​(B)​(o¯,x,h)|\displaystyle\hskip-56.9055pt|\Gamma(B)(o,x,h)-\Gamma(B)(\bar{o},x,h)| |  |
|  |  | ≤\displaystyle\leq | 𝔼​[|V​(B)​(o,ε,x+h​f​(o,ε))−V​(B)​(o¯,ε,x+h​f​(o,ε))|]\displaystyle\mathbb{E}\bigl[\bigl|V(B)(o,\varepsilon,x+hf(o,\varepsilon))-V(B)\bigl(\bar{o},\varepsilon,x+hf(o,\varepsilon)\bigr)\bigr|\bigr] |  |
|  |  |  | +𝔼​[|V​(B)​(o¯,ε,x+h​f​(o,ε))−V​(B)​(o¯,ε,x+h​f​(o¯,ε))|]\displaystyle+\mathbb{E}\bigl[\bigl|V(B)\bigl(\bar{o},\varepsilon,x+hf(o,\varepsilon)\bigr)-V(B)\bigl(\bar{o},\varepsilon,x+hf(\bar{o},\varepsilon)\bigr)\bigr|\bigr] |  |
|  |  | ≤\displaystyle\leq | 𝔼​[CV​(x+h​f​(o,ε))]​|o−o¯|θ\displaystyle\mathbb{E}\bigl[C\_{V}\bigl(x+hf(o,\varepsilon)\bigr)\bigr]|o-\bar{o}|^{\theta} |  |
|  |  |  | +𝔼​[supy∈D​(x)V​(B)′​(o¯,ε,y)​|h|​|f​(o,ε)−f​(o¯,ε)|]\displaystyle+\mathbb{E}\bigl[\sup\_{y\in D(x)}V(B)^{\prime}(\bar{o},\varepsilon,y)|h|\bigr|f(o,\varepsilon)-f(\bar{o},\varepsilon)\bigr|\bigr] |  |
|  |  | ≤\displaystyle\leq | supy∈D​(x)CV​(y)​|o−o¯|θ+supy∈D​(x)JV​(y)​K​(x)​Cf​|o−o¯|χ\displaystyle\sup\_{y\in D(x)}C\_{V}(y)|o-\bar{o}|^{\theta}+\sup\_{y\in D(x)}J\_{V}(y)K(x)C\_{f}|o-\bar{o}|^{\chi} |  |
|  |  | ≤\displaystyle\leq | (supy∈D​(x)CV​(y)+supy∈D​(x)JV​(y)​K​(x)​Cf)​(|o−o¯|θ+|o−o¯|χ)\displaystyle\bigl(\sup\_{y\in D(x)}C\_{V}(y)+\sup\_{y\in D(x)}J\_{V}(y)K(x)C\_{f}\bigr)\bigl(|o-\bar{o}|^{\theta}+|o-\bar{o}|^{\chi}\bigr) |  |
|  |  | ≤\displaystyle\leq | A​(x)​|o−o¯|θ,\displaystyle A(x)|o-\bar{o}|^{\theta}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | A​(x):=2​(supy∈D​(x)CV​(y)+supy∈D​(x)JV​(y)​K​(x)​Cf)+2​(CU+Cν+supy∈D​(x)|iV​(y)|)>0,A(x):=2\bigl(\sup\_{y\in D(x)}C\_{V}(y)+\sup\_{y\in D(x)}J\_{V}(y)K(x)C\_{f}\bigr)+2\bigl(C\_{U}+C\_{\nu}+\sup\_{y\in D(x)}|i\_{V}(y)|\bigr)>0, |  |

recalling ([28](https://arxiv.org/html/2512.08348v1#S3.E28 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and
using Lemma [4.3](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") with the choice n=2n=2, θ1=θ\theta\_{1}=\theta, θ2=χ\theta\_{2}=\chi, since 0<θ≤χ≤10<\theta\leq\chi\leq 1.
The function AA is continuous as CV,JV,K,iVC\_{V},J\_{V},K,i\_{V} are, see Lemma [4.4](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

Estimates of vv and its derivatives

Let (o,x)∈ℝ(t−1)×m×ℝ.(o,x)\in\mathbb{R}^{(t-1)\times m}\times\mathbb{R}.
Clearly, v​(B)​(o,x)≥𝔼​[V​(B)​(o,ε,x)]≥iV​(x)v(B)(o,x)\geq\mathbb{E}[V(B)(o,\varepsilon,x)]\geq i\_{V}(x) so we may set iv​(x):=iV​(x)i\_{v}(x):=i\_{V}(x).
Furthermore, recalling ([26](https://arxiv.org/html/2512.08348v1#S3.E26 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and noting that V​(B)′V(B)^{\prime} is non-increasing in xx,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(B)′​(o,x)\displaystyle v(B)^{\prime}(o,x) | =\displaystyle= | 𝔼​[V​(B)′​(o,ε,x+h¯​(o,x)​f​(o,ε))]\displaystyle\mathbb{E}\bigl[V(B)^{\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)\bigr] |  |
|  |  | ≤\displaystyle\leq | V(B)′(o,ε,x−K(x)Cf)≤JV(x−K(x)Cf)=:Jv(x)\displaystyle V(B)^{\prime}(o,\varepsilon,x-K(x)C\_{f})\leq J\_{V}(x-K(x)C\_{f})=:J\_{v}(x) |  |

and

|  |  |  |
| --- | --- | --- |
|  | v(B)′(o,x)≥V(B)′(o,ε,x+K(x)Cf)≥jV(x+K(x)Cf)=:jv(x).v(B)^{\prime}(o,x)\geq V(B)^{\prime}(o,\varepsilon,x+K(x)C\_{f})\geq j\_{V}(x+K(x)C\_{f})=:j\_{v}(x). |  |

With these definitions, the functions iv,jv,Jvi\_{v},j\_{v},J\_{v} are continuous (recall that KK is continuous),
iv:ℝ→ℝi\_{v}:\mathbb{R}\to\mathbb{R} and jv,Jv:ℝ→(0,∞)j\_{v},J\_{v}:\mathbb{R}\to(0,\infty).

Recalling ([26](https://arxiv.org/html/2512.08348v1#S3.E26 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we prove as in Lemma [3.2](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(B)′′​(o,x)=𝔼​[V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))​(1+f​(o,ε)​∂xh¯​(o,x))],v(B)^{\prime\prime}(o,x)=\mathbb{E}\bigl[V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)\bigl(1+f(o,\varepsilon)\partial\_{x}\bar{h}(o,x)\bigr)\bigr], |  | (29) |

and that x↦v​(B)′′​(o,x)x\mapsto v(B)^{\prime\prime}(o,x) is continuous (here, ([25](https://arxiv.org/html/2512.08348v1#S3.E25 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) shows that x↦∂xh¯​(o,x)x\mapsto\partial\_{x}\bar{h}(o,x) is continuous).
Recall again the interval D​(x)D(x) from ([24](https://arxiv.org/html/2512.08348v1#S3.E24 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). Let the probability
ℚ\mathbb{Q} be defined as follows (see ([8](https://arxiv.org/html/2512.08348v1#S3.E8 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."))),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q\displaystyle q | :=\displaystyle:= | −𝔼​[V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))]≥infy∈D​(x)ℓ​(y)>0\displaystyle-\mathbb{E}\bigl[V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)\bigr]\geq\inf\_{y\in D(x)}\ell(y)>0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​ℚd​ℙ\displaystyle\frac{d\mathbb{Q}}{d\mathbb{P}} | :=\displaystyle:= | −V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))q.\displaystyle\frac{-V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)}{q}. |  |

We denote by 𝔼ℚ\mathbb{E}\_{\mathbb{Q}} the expectation under ℚ\mathbb{Q}.
Recalling ([25](https://arxiv.org/html/2512.08348v1#S3.E25 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), ([14](https://arxiv.org/html/2512.08348v1#S3.E14 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([15](https://arxiv.org/html/2512.08348v1#S3.E15 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we estimate that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −v​(B)′′​(o,x)\displaystyle-v(B)^{\prime\prime}(o,x) | =\displaystyle= | q​𝔼ℚ​[1+f​(o,ε)​∂xh¯​(o,x)]\displaystyle q\mathbb{E}\_{\mathbb{Q}}\bigl[1+f(o,\varepsilon)\partial\_{x}\bar{h}(o,x)\bigr] |  |
|  |  | =\displaystyle= | q​𝔼ℚ​[1−f​(o,ε)​𝔼​[V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))​f​(o,ε)]𝔼​[V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))​f2​(o,ε)]]\displaystyle q\mathbb{E}\_{\mathbb{Q}}\Bigl[1-f(o,\varepsilon)\frac{\mathbb{E}\bigl[V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)f(o,\varepsilon)\bigr]}{\mathbb{E}\bigl[V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)f^{2}(o,\varepsilon)\bigr]}\Bigr] |  |
|  |  | =\displaystyle= | q​𝔼ℚ​[1−f​(o,ε)​𝔼ℚ​[f​(o,ε)]𝔼ℚ​[f2​(o,ε)]]=q​𝔼ℚ​[f2​(o,ε)]−𝔼ℚ2​[f​(o,ε)]𝔼ℚ​[f2​(o,ε)]\displaystyle q\mathbb{E}\_{\mathbb{Q}}\Bigl[1-f(o,\varepsilon)\frac{\mathbb{E}\_{\mathbb{Q}}[f(o,\varepsilon)]}{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]}\Bigr]={}q\frac{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]-\mathbb{E}^{2}\_{\mathbb{Q}}[f(o,\varepsilon)]}{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]} |  |
|  |  | =\displaystyle= | q​𝔼ℚ​[(f​(o,ε)−𝔼ℚ​[f​(o,ε)])2]𝔼ℚ​[f2​(o,ε)].\displaystyle q\frac{\mathbb{E}\_{\mathbb{Q}}\bigl[\bigl(f(o,\varepsilon)-\mathbb{E}\_{\mathbb{Q}}[f(o,\varepsilon)]\bigr)^{2}\bigr]}{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]}. |  |

We now distinguish between two cases. If 𝔼ℚ​[f​(o,ε)]>0\mathbb{E}\_{\mathbb{Q}}[f(o,\varepsilon)]>0, then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −v​(B)′′​(o,x)\displaystyle-v(B)^{\prime\prime}(o,x) | ≥\displaystyle\geq | q​𝔼ℚ​[(f​(o,ε)−𝔼ℚ​[f​(o,ε)])2​1{f​(o,ε)≤−α}]𝔼ℚ​[f2​(o,ε)]\displaystyle q\frac{\mathbb{E}\_{\mathbb{Q}}\bigl[\bigl(f(o,\varepsilon)-\mathbb{E}\_{\mathbb{Q}}[f(o,\varepsilon)]\bigr)^{2}1\_{\{f(o,\varepsilon)\leq-\alpha\}}\bigr]}{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]} |  |
|  |  | ≥\displaystyle\geq | q​𝔼ℚ​[1{f​(o,ε)≤−α}​α2]𝔼ℚ​[f2​(o,ε)]≥q​α2Cf2​𝔼ℚ​[1{f​(o,ε)≤−α}]\displaystyle q\frac{\mathbb{E}\_{\mathbb{Q}}\bigl[1\_{\{f(o,\varepsilon)\leq-\alpha\}}\alpha^{2}\bigr]}{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]}\geq\frac{q\alpha^{2}}{C\_{f}^{2}}\mathbb{E}\_{\mathbb{Q}}\bigl[1\_{\{f(o,\varepsilon)\leq-\alpha\}}\bigr] |  |
|  |  | ≥\displaystyle\geq | α2Cf2​𝔼​[−V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))​1{f​(o,ε)≤−α}]\displaystyle\frac{\alpha^{2}}{C\_{f}^{2}}\mathbb{E}\bigl[-V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)1\_{\{f(o,\varepsilon)\leq-\alpha\}}\bigr] |  |
|  |  | ≥\displaystyle\geq | α2Cf2​infy∈D​(x)ℓV​(y)​𝔼​[1{f​(o,ε)≤−α}]≥α3Cf2​infy∈D​(x)ℓV​(y),\displaystyle\frac{\alpha^{2}}{C\_{f}^{2}}\inf\_{y\in D(x)}\ell\_{V}(y)\mathbb{E}\bigl[1\_{\{f(o,\varepsilon)\leq-\alpha\}}\bigr]\geq\frac{\alpha^{3}}{C\_{f}^{2}}\inf\_{y\in D(x)}\ell\_{V}(y), |  |

using ([10](https://arxiv.org/html/2512.08348v1#S3.E10 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). Now, if 𝔼ℚ​[f​(o,ε)]≤0\mathbb{E}\_{\mathbb{Q}}[f(o,\varepsilon)]\leq 0, then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −v​(B)′′​(o,x)\displaystyle-v(B)^{\prime\prime}(o,x) | ≥\displaystyle\geq | q​𝔼ℚ​[(f​(o,ε)−𝔼ℚ​[f​(o,ε)])2​1{f​(o,ε)≥α}]𝔼ℚ​[f2​(o,ε)]\displaystyle q\frac{\mathbb{E}\_{\mathbb{Q}}\bigl[\bigl(f(o,\varepsilon)-\mathbb{E}\_{\mathbb{Q}}[f(o,\varepsilon)]\bigr)^{2}1\_{\{f(o,\varepsilon)\geq\alpha\}}\bigr]}{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]} |  |
|  |  | ≥\displaystyle\geq | q​𝔼ℚ​[1{f​(o,ε)≥α}​α2]𝔼ℚ​[f2​(o,ε)]\displaystyle q\frac{\mathbb{E}\_{\mathbb{Q}}\bigl[1\_{\{f(o,\varepsilon)\geq\alpha\}}\alpha^{2}\bigr]}{\mathbb{E}\_{\mathbb{Q}}[f^{2}(o,\varepsilon)]} |  |
|  |  | ≥\displaystyle\geq | α2Cf2​𝔼​[−V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))​1{f​(o,ε)≥α}]\displaystyle\frac{\alpha^{2}}{C\_{f}^{2}}\mathbb{E}\bigl[-V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)1\_{\{f(o,\varepsilon)\geq\alpha\}}\bigr] |  |
|  |  | ≥\displaystyle\geq | α3Cf2​infy∈D​(x)ℓV​(y):=ℓv​(x).\displaystyle\frac{\alpha^{3}}{C\_{f}^{2}}\inf\_{y\in D(x)}\ell\_{V}(y):=\ell\_{v}(x). |  |

Then, ℓv:ℝ→(0,∞)\ell\_{v}:\mathbb{R}\to(0,\infty) is continuous, see Lemma [4.4](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").
For the upper bound, using ([25](https://arxiv.org/html/2512.08348v1#S3.E25 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), ([14](https://arxiv.org/html/2512.08348v1#S3.E14 "In Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([23](https://arxiv.org/html/2512.08348v1#S3.E23 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |∂xh¯​(o,x)|\displaystyle\left|\partial\_{x}\bar{h}(o,x)\right| | =\displaystyle= | |∂xγ​(B)​(o,x,h¯​(B)​(o,x))∂hγ​(B)​(o,x,h¯​(B)​(o,x))|\displaystyle\Bigl|\frac{\partial\_{x}\gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)}{\partial\_{h}\gamma(B)\bigl(o,x,\bar{h}(B)(o,x)\bigr)}\Bigr| |  |
|  |  | ≤\displaystyle\leq | 𝔼​[|V​(B)′′​(o,ε,x+h¯​(B)​(o,x)​f​(o,ε))​f​(o,ε)|]α3​infy∈D​(x)ℓV​(y)\displaystyle\frac{\mathbb{E}\bigl[|V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(B)(o,x)f(o,\varepsilon)\bigr)f(o,\varepsilon)|\bigr]}{\alpha^{3}\inf\_{y\in D(x)}\ell\_{V}(y)} |  |
|  |  | ≤\displaystyle\leq | Cf​supy∈D​(x)LV​(y)α3​infy∈D​(x)ℓV​(y)=supy∈D​(x)LV​(y)Cf​ℓv​(x).\displaystyle\frac{C\_{f}\sup\_{y\in D(x)}L\_{V}(y)}{\alpha^{3}\inf\_{y\in D(x)}\ell\_{V}(y)}=\frac{\sup\_{y\in D(x)}L\_{V}(y)}{C\_{f}\ell\_{v}(x)}. |  |

Recalling ([29](https://arxiv.org/html/2512.08348v1#S3.E29 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −v​(B)′′​(o,x)\displaystyle-v(B)^{\prime\prime}(o,x) | =\displaystyle= | 𝔼​[−V​(B)′′​(o,ε,x+h¯​(o,x)​f​(o,ε))​(1+f​(o,ε)​∂xh¯​(o,x))]\displaystyle\mathbb{E}\bigl[-V(B)^{\prime\prime}\bigl(o,\varepsilon,x+\bar{h}(o,x)f(o,\varepsilon)\bigr)\bigl(1+f(o,\varepsilon)\partial\_{x}\bar{h}(o,x)\bigr)\bigr] |  |
|  |  | ≤\displaystyle\leq | supy∈D​(x)LV(y)(1+supy∈D​(x)LV​(y)ℓv​(x))=:Lv(x),\displaystyle\sup\_{y\in D(x)}L\_{V}(y)\left(1+\frac{\sup\_{y\in D(x)}L\_{V}(y)}{\ell\_{v}(x)}\right)=:L\_{v}(x), |  |

and Lv:ℝ→(0,∞)L\_{v}:\mathbb{R}\to(0,\infty) is continuous using again Lemma [4.4](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

Continuity of h¯\bar{h} with respect to past

Let x∈ℝ.x\in\mathbb{R}. In this part of the proof, we suppress dependence on BB in the notation, for simplicity.
Let |h|≤K​(x)|h|\leq K(x) hold from now on. Recall the interval D​(x)D(x) from ([24](https://arxiv.org/html/2512.08348v1#S3.E24 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) again.

Let o,o¯∈ℝ(t−1)×mo,\bar{o}\in\mathbb{R}^{(t-1)\times m}. Let h∈ℝh\in\mathbb{R} and h¯​(o,x)\bar{h}(o,x) (resp. h¯​(o¯,x)\bar{h}(\bar{o},x)) be the optimizer of Γ​(B)​(o,x,⋅)\Gamma(B)(o,x,\cdot) (resp.
Γ​(B)​(o¯,x,⋅)\Gamma(B)(\bar{o},x,\cdot)).
One can write, by the Newton-Leibniz rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(o,x,h)−Γ​(o,x,h¯​(o,x))=∫h¯​(o,x)hγ​(o,x,ξ)​𝑑ξ.\Gamma(o,x,h)-\Gamma\bigl(o,x,\bar{h}(o,x)\bigr)=\int\_{\bar{h}(o,x)}^{h}\gamma(o,x,\xi)\,d\xi. |  | (30) |

The first order condition ([22](https://arxiv.org/html/2512.08348v1#S3.E22 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([23](https://arxiv.org/html/2512.08348v1#S3.E23 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) imply that for any ξ\xi,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |γ​(o,x,ξ)|=|γ​(o,x,ξ)−γ​(o,x,h¯​(o,x))|\displaystyle|\gamma(o,x,\xi)|=|\gamma(o,x,\xi)-\gamma\bigl(o,x,\bar{h}(o,x)\bigr)| | ≥\displaystyle\geq | |ξ−h¯​(o,x)|​α3​infy∈D​(x)ℓV​(y)\displaystyle|\xi-\bar{h}(o,x)|\alpha^{3}\inf\_{y\in D(x)}\ell\_{V}(y) |  |
|  |  | =\displaystyle= | |ξ−h¯​(o,x)|​Cf2​ℓv​(x).\displaystyle|\xi-\bar{h}(o,x)|C\_{f}^{2}\ell\_{v}(x). |  |

First assume that h¯​(o,x)≤h.\bar{h}(o,x)\leq h. Let ξ\xi such that h¯​(o,x)≤ξ≤h\bar{h}(o,x)\leq\xi\leq h. Then, as h¯​(o,x)\bar{h}(o,x) is the maximum of h↦Γ​(o,x,h)h\mapsto\Gamma(o,x,h) and
∂hΓ​(o,x,h)=γ​(o,x,h)\partial\_{h}\Gamma(o,x,h)=\gamma(o,x,h), we get that
γ​(o,x,h)≤0\gamma(o,x,h)\leq 0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | −γ​(o,x,ξ)≥|ξ−h¯​(o,x)|​Cf2​ℓv​(x)=(ξ−h¯​(o,x))​Cf2​ℓv​(x),-\gamma(o,x,\xi)\geq|\xi-\bar{h}(o,x)|C\_{f}^{2}\ell\_{v}(x)=\bigl(\xi-\bar{h}(o,x)\bigr)C\_{f}^{2}\ell\_{v}(x), |  | (31) |

so ([30](https://arxiv.org/html/2512.08348v1#S3.E30 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(o,x,h)−Γ​(o,x,h¯​(o,x))≤−Cf2​ℓv​(x)2​(h−h¯​(o,x))2.\Gamma(o,x,h)-\Gamma\bigl(o,x,\bar{h}(o,x)\bigr)\leq-\frac{C\_{f}^{2}\ell\_{v}(x)}{2}(h-\bar{h}(o,x))^{2}. |  | (32) |

Assume now that h¯​(o,x)>h\bar{h}(o,x)>h. Let ξ\xi such that h¯​(o,x)≥ξ>h\bar{h}(o,x)\geq\xi>h. Then γ​(o,x,h)≥0\gamma(o,x,h)\geq 0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(o,x,ξ)≥|ξ−h¯​(o,x)|​Cf2​ℓv​(x)=−(ξ−h¯​(o,x))​Cf2​ℓv​(x),\gamma(o,x,\xi)\geq|\xi-\bar{h}(o,x)|C\_{f}^{2}\ell\_{v}(x)=-(\xi-\bar{h}(o,x))C\_{f}^{2}\ell\_{v}(x), |  | (33) |

leading again to ([32](https://arxiv.org/html/2512.08348v1#S3.E32 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). For o,o¯o,\bar{o} ([32](https://arxiv.org/html/2512.08348v1#S3.E32 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) gives for h=h¯​(o¯,x)h=\bar{h}(\bar{o},x),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Cf2​ℓv​(x)2​(h¯​(o,x)−h¯​(o¯,x))2\displaystyle\frac{C\_{f}^{2}\ell\_{v}(x)}{2}\big(\bar{h}({o},x)-\bar{h}(\bar{o},x)\big)^{2} | ≤\displaystyle\leq | |Γ​(o,x,h¯​(o,x))−Γ​(o,x,h¯​(o¯,x))|\displaystyle|\Gamma\bigl(o,x,\bar{h}(o,x)\bigr)-\Gamma\bigl(o,x,\bar{h}(\bar{o},x)\bigr)| |  |
|  |  | ≤\displaystyle\leq | |Γ​(o,x,h¯​(o,x))−Γ​(o¯,x,h¯​(o¯,x))|\displaystyle|\Gamma\bigl(o,x,\bar{h}(o,x)\bigr)-\Gamma\bigl(\bar{o},x,\bar{h}(\bar{o},x)\bigr)| |  |
|  |  |  | +|Γ​(o,x,h¯​(o¯,x))−Γ​(o¯,x,h¯​(o¯,x))|\displaystyle+|\Gamma\bigl(o,x,\bar{h}(\bar{o},x)\bigr)-\Gamma\bigl(\bar{o},x,\bar{h}(\bar{o},x)\bigr)| |  |
|  |  | ≤\displaystyle\leq | |Γ​(o,x,h¯​(o,x))−Γ​(o¯,x,h¯​(o¯,x))|+A​(x)​|o−o¯|θ,\displaystyle|\Gamma\bigl(o,x,\bar{h}(o,x)\bigr)-\Gamma\bigl(\bar{o},x,\bar{h}(\bar{o},x)\bigr)|+A(x)|o-\bar{o}|^{\theta}, |  |

where for the last inequality, we have used ([27](https://arxiv.org/html/2512.08348v1#S3.E27 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) as |h¯​(o¯,x)|≤K​(x).|\bar{h}(\bar{o},x)|\leq K(x).
Recalling ([20](https://arxiv.org/html/2512.08348v1#S3.E20 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")):

|  |  |  |
| --- | --- | --- |
|  | v​(o,x)=suph∈ℝΓ​(o,x,h)=sup|h|≤K​(x)Γ​(o,x,h)=Γ​(o,x,h¯​(o,x)),v(o,x)=\sup\_{h\in\mathbb{R}}\Gamma(o,x,h)=\sup\_{|h|\leq K(x)}\Gamma(o,x,h)=\Gamma(o,x,\bar{h}(o,x)), |  |

and the same holds true for o¯\bar{o}. It follows that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Γ​(o,x,h¯​(o,x))−Γ​(o¯,x,h¯​(o¯,x))|\displaystyle|\Gamma\bigl(o,x,\bar{h}(o,x)\bigr)-\Gamma\bigl(\bar{o},x,\bar{h}(\bar{o},x)\bigr)| | =\displaystyle= | |sup|h|≤K​(x)Γ​(o,x,h)−sup|h|≤K​(x)Γ​(o¯,x,h)|\displaystyle\bigl|\sup\_{|h|\leq K(x)}\Gamma(o,x,h)-\sup\_{|h|\leq K(x)}\Gamma(\bar{o},x,h)\bigr| |  |
|  |  | ≤\displaystyle\leq | sup|h|≤K​(x)|Γ​(o,x,h)−Γ​(o¯,x,h)|\displaystyle\sup\_{|h|\leq K(x)}\bigl|\Gamma(o,x,h)-\Gamma(\bar{o},x,h)\bigr| |  |
|  |  | ≤\displaystyle\leq | A​(x)​|o−o¯|θ,\displaystyle A(x)|o-\bar{o}|^{\theta}, |  |

where the last inequality follows from ([27](https://arxiv.org/html/2512.08348v1#S3.E27 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) as every hh is such that |h|≤K​(x).|h|\leq K(x). So, we get that

|  |  |  |
| --- | --- | --- |
|  | |h¯​(o,x)−h¯​(o¯,x)|2≤4​A​(x)​|o−o¯|θCf2​ℓv​(x),|\bar{h}(o,x)-\bar{h}(\bar{o},x)|^{2}\leq\frac{4A(x)|o-\bar{o}|^{\theta}}{C\_{f}^{2}\ell\_{v}(x)}, |  |

which implies that, indeed, ([17](https://arxiv.org/html/2512.08348v1#S3.E17 "In Proposition 3.3. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) is valid with

|  |  |  |
| --- | --- | --- |
|  | Ch​(x):=K​(x)+2Cf​A​(x)ℓv​(x)>0.C\_{h}(x):=K(x)+\frac{2}{C\_{f}}\sqrt{\frac{A(x)}{\ell\_{v}(x)}}>0. |  |

As A,K,ℓvA,K,\ell\_{v} are continuous, so is ChC\_{h}. Remark that ChC\_{h} does not depend on BB.

Continuity of vv with respect to the past

Let x∈ℝ.x\in\mathbb{R}. Let o,o¯∈ℝ(t−1)×mo,\bar{o}\in\mathbb{R}^{(t-1)\times m}. Let h¯​(o,x)\bar{h}(o,x) (resp. h¯​(o¯,x)\bar{h}(\bar{o},x)) be the optimizer of Γ​(B)​(o,x,⋅)\Gamma(B)(o,x,\cdot) (resp.
Γ​(B)​(o¯,x,⋅)\Gamma(B)(\bar{o},x,\cdot)).
We have already estimated that (see ([19](https://arxiv.org/html/2512.08348v1#S3.E19 "In Proposition 3.3. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")))

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v​(B)​(o,x)|≤CU+Cν+|iv​(x)|.|v(B)(o,x)|\leq C\_{U}+C\_{\nu}+|i\_{v}(x)|. |  | (34) |

Note that |h¯​(o,x)​f​(o,ε)|≤K​(x)​Cf|\bar{h}(o,x)f(o,\varepsilon)|\leq K(x)C\_{f}. Recall ([8](https://arxiv.org/html/2512.08348v1#S3.E8 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([11](https://arxiv.org/html/2512.08348v1#S3.E11 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). Estimate

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |v​(B)​(o,x)−v​(B)​(o¯,x)|\displaystyle\hskip-28.45274pt|v(B)(o,x)-v(B)(\bar{o},x)| |  |
|  |  | ≤\displaystyle\leq | 𝔼​[|V​(B)​(o,ε,x+h¯​(B)​(o,x)​f​(o,ε))−V​(B)​(o¯,ε,x+h¯​(B)​(o¯,x)​f​(o¯,ε))|]\displaystyle\mathbb{E}\bigl[\bigl|V(B)\bigl(o,\varepsilon,x+\bar{h}(B)(o,x)f(o,\varepsilon)\bigr)-V(B)\bigl(\bar{o},\varepsilon,x+\bar{h}(B)(\bar{o},x)f(\bar{o},\varepsilon)\bigr)\bigr|\bigr] |  |
|  |  | ≤\displaystyle\leq | 𝔼​[|V​(B)​(o,ε,x+h¯​(B)​(o,x)​f​(o,ε))−V​(B)​(o¯,ε,x+h¯​(B)​(o,x)​f​(o,ε))|]\displaystyle\mathbb{E}\bigl[\bigl|V(B)\bigl(o,\varepsilon,x+\bar{h}(B)(o,x)f(o,\varepsilon)\bigr)-V(B)\bigl(\bar{o},\varepsilon,x+\bar{h}(B)(o,x)f(o,\varepsilon)\bigr)\bigr|\bigr] |  |
|  |  |  | +𝔼​[|V​(B)​(o¯,ε,x+h¯​(B)​(o,x)​f​(o,ε))−V​(B)​(o¯,ε,x+h¯​(B)​(o¯,x)​f​(o¯,ε))|]\displaystyle+\mathbb{E}\bigl[\bigl|V(B)\bigl(\bar{o},\varepsilon,x+\bar{h}(B)(o,x)f(o,\varepsilon)\bigr)-V(B)\bigl(\bar{o},\varepsilon,x+\bar{h}(B)(\bar{o},x)f(\bar{o},\varepsilon)\bigr)\bigr|\bigr] |  |
|  |  | ≤\displaystyle\leq | supy∈D​(x)CV​(y)​|o−o¯|θ\displaystyle\sup\_{y\in D(x)}C\_{V}(y)|o-\bar{o}|^{\theta} |  |
|  |  |  | +𝔼​[supy∈D​(x)V​(B)′​(o¯,ε,y)​|h¯​(B)​(o,x)​f​(o,ε)−h¯​(B)​(o¯,x)​f​(o¯,ε)|]\displaystyle+\mathbb{E}\bigl[\sup\_{y\in D(x)}V(B)^{\prime}\bigl(\bar{o},\varepsilon,y)|\bar{h}(B)(o,x)f(o,\varepsilon)-\bar{h}(B)(\bar{o},x)f(\bar{o},\varepsilon)|\bigr] |  |
|  |  | ≤\displaystyle\leq | supy∈D​(x)CV​(y)​|o−o¯|θ\displaystyle\sup\_{y\in D(x)}C\_{V}(y)|o-\bar{o}|^{\theta} |  |
|  |  |  | +supy∈D​(x)JV​(y)​[K​(x)​𝔼​[|f​(o,ε)−f​(o¯,ε)|]+Cf​|h¯​(B)​(o,x)−h¯​(B)​(o¯,x)|]\displaystyle+\sup\_{y\in D(x)}J\_{V}(y)\Bigl[K(x)\mathbb{E}\bigl[|f(o,\varepsilon)-f(\bar{o},\varepsilon)|\bigr]+C\_{f}|\bar{h}(B)(o,x)-\bar{h}(B)(\bar{o},x)|\Bigr] |  |
|  |  | ≤\displaystyle\leq | [supy∈D​(x)CV​(y)+supy∈D​(x)JV​(y)​Cf​[K​(x)+Ch​(x)]]\displaystyle\bigl[\sup\_{y\in D(x)}C\_{V}(y)+\sup\_{y\in D(x)}J\_{V}(y)C\_{f}[K(x)+C\_{h}(x)]\bigr] |  |
|  |  | ×\displaystyle\times | [|o−o¯|θ+|o−o¯|χ+|o−o¯|θ/2],\displaystyle[|o-\bar{o}|^{\theta}+|o-\bar{o}|^{\chi}+|o-\bar{o}|^{\theta/2}], |  |

where we have used

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |h¯​(B)​(o,x)​f​(o,ε)−h¯​(B)​(o¯,x)​f​(o¯,ε)|\displaystyle|\bar{h}(B)(o,x)f(o,\varepsilon)-\bar{h}(B)(\bar{o},x)f(\bar{o},\varepsilon)| | ≤\displaystyle\leq | |h¯​(B)​(o,x)​f​(o,ε)−h¯​(B)​(o,x)​f​(o¯,ε)|\displaystyle|\bar{h}(B)(o,x)f(o,\varepsilon)-\bar{h}(B)(o,x)f(\bar{o},\varepsilon)| |  |
|  |  |  | +|h¯​(B)​(o,x)​f​(o¯,ε)−h¯​(B)​(o¯,x)​f​(o¯,ε)|.\displaystyle+|\bar{h}(B)(o,x)f(\bar{o},\varepsilon)-\bar{h}(B)(\bar{o},x)f(\bar{o},\varepsilon)|. |  |

Recalling ([34](https://arxiv.org/html/2512.08348v1#S3.E34 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and Lemma [4.3](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") with the choice n=3n=3, θ1:=θ/2\theta\_{1}:=\theta/2, θ2:=θ\theta\_{2}:=\theta, θ3=χ\theta\_{3}=\chi,
we may set

|  |  |  |
| --- | --- | --- |
|  | Cv​(x):=3​[supy∈D​(x)CV​(y)+supy∈D​(x)JV​(y)​Cf​[K​(x)+Ch​(x)]]+2​(CU+Cν+|iv​(x)|),C\_{v}(x):=3\bigl[\sup\_{y\in D(x)}C\_{V}(y)+\sup\_{y\in D(x)}J\_{V}(y)C\_{f}[K(x)+C\_{h}(x)]\bigr]+2\bigl(C\_{U}+C\_{\nu}+|i\_{v}(x)|\bigr), |  |

and ([18](https://arxiv.org/html/2512.08348v1#S3.E18 "In Proposition 3.3. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds.
Since CV,JV,K,Ch,ivC\_{V},J\_{V},K,C\_{h},i\_{v} are continuous,
so is Cv​(x),C\_{v}(x), see Lemma [4.4](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

Measurability

It is known that Carathéodory integrand (i.e. a function of two variables that is measurable in the first and continuous in the second) is jointly
measurable, see [[1](https://arxiv.org/html/2512.08348v1#bib.bib1), Lemma 4.51]. So, the function Γ​(B)\Gamma(B) is
ℬ​(ℝ(t−1)×m)⊗ℬ​(ℝ)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{(t-1)\times m})\otimes\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R})-measurable,
see Lemma [3.2](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") (the first variable is here oo and the second (x,h)(x,h)). Now, h¯​(B)\bar{h}(B) is continuous in oo
(see ([17](https://arxiv.org/html/2512.08348v1#S3.E17 "In Proposition 3.3. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."))) and we have proved that h¯​(B)\bar{h}(B) is differentiable in xx (see ([25](https://arxiv.org/html/2512.08348v1#S3.E25 "In 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."))).
So, h¯​(B)\bar{h}(B) is continuous in each
variable separately, hence it is ℬ​(ℝ(t−1)×m)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{(t-1)\times m})\otimes\mathcal{B}(\mathbb{R})-measurable.
Then so is v​(B)v(B), as v​(B)​(o,x)=Γ​(B)​(o,x,h¯​(B)​(o,x))v(B)(o,x)=\Gamma(B)(o,x,\bar{h}(B)(o,x)).
Now our proof is complete.
∎

### 3.2 Dynamic programming

We prove that there exists some bounded and Hölder-continuous solution for the optimization problem ([7](https://arxiv.org/html/2512.08348v1#S2.E7 "In 2.3 Personal equilibrium ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).

###### Proposition 3.4.

Let Assumptions [2.1](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") and [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") hold.
Let x0∈ℝx\_{0}\in\mathbb{R} and ϕ∈Φ\phi\in\Phi be arbitrary. Then there exists a unique optimizer ψ∗:=ψ∗​(ϕ)​(⋅,x0)∈Φ\psi^{\*}:=\psi^{\*}(\phi)(\cdot,x\_{0})\in\Phi such that

|  |  |  |
| --- | --- | --- |
|  | u​(x0,ϕ)=supψ∈Φ𝔼​[U​(WT​(x0,ψ),B​(ϕ))]=𝔼​[U​(WT​(x0,ψ∗),B​(ϕ))].u(x\_{0},\phi)=\sup\_{\psi\in\Phi}\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi),B(\phi)\bigr)\bigr]=\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi^{\*}),B(\phi)\bigr)\bigr]. |  |

Denoting by ψ¯∗\bar{\psi}^{\*} a Borel function associated to ψ∗\psi^{\*} by Doob’s theorem, i.e.
ψt∗:=ψ¯t∗​(εt−1)\psi^{\*}\_{t}:=\bar{\psi}^{\*}\_{t}(\varepsilon^{t-1}), 1≤t≤T1\leq t\leq T (we mean that ψ¯1∗\bar{\psi}^{\*}\_{1} is constant),
ψ¯∗\bar{\psi}^{\*} can be chosen bounded and Hölder-continuous, where constants are independent of ϕ\phi. That is,
there exists a continuous function C:ℝ→(0,∞)C:\mathbb{R}\to(0,\infty) such that for all 1≤t≤T1\leq t\leq T, for all et−1,e¯t−1∈ℝ(t−1)×me^{t-1},\bar{e}^{t-1}\in\mathbb{R}^{(t-1)\times m},

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |ψ¯∗​(ϕ)t​(et−1,x0)|\displaystyle|\bar{\psi}^{\*}(\phi)\_{t}(e^{t-1},x\_{0})| | ≤\displaystyle\leq | C​(x0)\displaystyle C(x\_{0}) |  | (35) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |ψ¯∗​(ϕ)t​(et−1,x0)−ψ¯∗​(ϕ)t​(e¯t−1,x0)|\displaystyle|\bar{\psi}^{\*}(\phi)\_{t}(e^{t-1},x\_{0})-\bar{\psi}^{\*}(\phi)\_{t}(\bar{e}^{t-1},x\_{0})| | ≤\displaystyle\leq | C​(x0)​|et−1−e¯t−1|χ/2T−t+1.\displaystyle C(x\_{0})|e^{t-1}-\bar{e}^{t-1}|^{\chi/2^{T-t+1}}. |  | (36) |

Note again that the constant C​(x0)C(x\_{0}) depends only on x0x\_{0} and neither on BB nor on ϕ\phi.

###### Proof.

We will apply the results of Section [3.1](https://arxiv.org/html/2512.08348v1#S3.SS1 "3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") recursively. Let BB be an arbitrary bounded random variable
that is independent of ℱTε\mathcal{F}\_{T}^{\varepsilon}. First, we define for all x∈ℝx\in\mathbb{R}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VT​(B)​(eT,x)\displaystyle V\_{T}(B)(e^{T},x) | :=\displaystyle:= | 𝔼​[U​(x,B)]=𝔼​[U​(x)+ν​(U​(x)−U​(B))],eT∈ℝT×m,\displaystyle\mathbb{E}\bigl[U(x,B)\bigr]=\mathbb{E}\Bigl[U(x)+\nu\bigl(U(x)-U(B)\bigr)\Bigr],\ e^{T}\in\mathbb{R}^{T\times m}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt​(B)​(et,x)\displaystyle V\_{t}(B)(e^{t},x) | :=\displaystyle:= | suph∈ℝ𝔼​[Vt+1​(B)​(et,εt+1,x+h​ft+1​(et,εt+1))],et∈ℝt×m.\displaystyle\sup\_{h\in\mathbb{R}}\mathbb{E}\bigl[V\_{t+1}(B)\bigl(e^{t},\varepsilon\_{t+1},x+hf\_{t+1}(e^{t},\varepsilon\_{t+1})\bigr)\bigr],\ e^{t}\in\mathbb{R}^{t\times m}. |  |

We check Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") for V​(B)V(B) with V​(B)​(eT,x):=U​(x,B)V(B)(e^{T},x):=U(x,B), and then, for VT​(B)V\_{T}(B).
We take ε:=εT\varepsilon:=\varepsilon\_{T} and f​(eT):=fT​(eT)f(e^{T}):=f\_{T}(e^{T}), eT∈ℝT×me^{T}\in\mathbb{R}^{T\times m}; ([10](https://arxiv.org/html/2512.08348v1#S3.E10 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) follows from
Assumption [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), and ([11](https://arxiv.org/html/2512.08348v1#S3.E11 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) is true by Assumption [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").
Now, Assmptions [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") and [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") imply that V​(B)V(B) and VT​(B)V\_{T}(B) are bounded from above by CU+CνC\_{U}+C\_{\nu}, and that V​(B)V(B) is twice continuously
differentiable in xx.

Note that neither V​(B)V(B) nor VT​(B)V\_{T}(B) depend on eTe^{T}. So, ([9](https://arxiv.org/html/2512.08348v1#S3.E9 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) is trivial with CV=0C\_{V}=0 and
θ=χ\theta=\chi. As UU and ν\nu are Borel, V​(B)V(B) is
trivially
ℬ​(ℝT×m)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{T\times m})\otimes\mathcal{B}(\mathbb{R})-measurable.
Using Fubini theorem, VT​(B)V\_{T}(B) is also
ℬ​(ℝT×m)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{T\times m})\otimes\mathcal{B}(\mathbb{R})-measurable.

We now prove ([8](https://arxiv.org/html/2512.08348v1#S3.E8 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) for V​(B)V(B). On the event {B≤x}\{B\leq x\}, U​(x,B)≥U​(x)+ν​(0)=U​(x)U(x,B)\geq U(x)+\nu(0)=U(x) while on the event {B>x}\{B>x\} we may estimate

|  |  |  |
| --- | --- | --- |
|  | U​(x,B)=U​(x)+k−​(U​(x)−U​(B))≥(1+k−)​U​(x)−k−​CU.U(x,B)=U(x)+k\_{-}\bigl(U(x)-U(B)\bigr)\geq(1+k\_{-})U(x)-k\_{-}C\_{U}. |  |

Thus, we may set

|  |  |  |  |
| --- | --- | --- | --- |
|  | iV​(x):=min⁡{U​(x),(1+k−)​U​(x)−k−​CU}=(1+k−)​U​(x)−k−​CU,\displaystyle i\_{V}(x):=\min\{U(x),(1+k\_{-})U(x)-k\_{-}C\_{U}\}=(1+k\_{-})U(x)-k\_{-}C\_{U}, |  | (37) |

as U≤CUU\leq C\_{U}.
We have that U′​(x,B)=U′​(x)+ν′​(U​(x)−U​(B))​U′​(x)U^{\prime}(x,B)=U^{\prime}(x)+\nu^{\prime}\bigl(U(x)-U(B)\bigr)U^{\prime}(x). So, 0≤ν′≤k−0\leq\nu^{\prime}\leq k\_{-} and U′≥0U^{\prime}\geq 0 imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | U′​(x)≤U′​(x,B)≤U′​(x)+k−​U′​(x)\displaystyle U^{\prime}(x)\leq U^{\prime}(x,B)\leq U^{\prime}(x)+k\_{-}U^{\prime}(x) |  | (38) |

and we may set jV​(x):=U′​(x)j\_{V}(x):=U^{\prime}(x) and JV​(x):=(1+k−)​U′​(x)J\_{V}(x):=(1+k\_{-})U^{\prime}(x).
We have that

|  |  |  |
| --- | --- | --- |
|  | U′′​(x,B)=U′′​(x)+ν′′​(U​(x)−U​(B))​(U′​(x))2+ν′​(U​(x)−U​(B))​U′′​(x).U^{\prime\prime}(x,B)=U^{\prime\prime}(x)+\nu^{\prime\prime}\bigl(U(x)-U(B)\bigr)\bigl(U^{\prime}(x)\bigr)^{2}+\nu^{\prime}\bigl(U(x)-U(B)\bigr)U^{\prime\prime}(x). |  |

Furthermore, since U′′≤0,U^{\prime\prime}\leq 0, −Cν≤ν′′≤0-C\_{\nu}\leq\nu^{\prime\prime}\leq 0 and 0≤ν′≤k−0\leq\nu^{\prime}\leq k\_{-},

|  |  |  |
| --- | --- | --- |
|  | U′′​(x)−Cν​(U′​(x))2+k−​U′′​(x)≤U′′​(x,B)≤U′′​(x)\displaystyle U^{\prime\prime}(x)-C\_{\nu}\bigl(U^{\prime}(x)\bigr)^{2}+k\_{-}U^{\prime\prime}(x)\leq U^{\prime\prime}(x,B)\leq U^{\prime\prime}(x) |  |

so we may set ℓV​(x):=−U′′​(x)\ell\_{V}(x):=-U^{\prime\prime}(x) and LV​(x):=−(1+k−)​U′′​(x)+Cν​(U′​(x))2L\_{V}(x):=-(1+k\_{-})U^{\prime\prime}(x)+C\_{\nu}(U^{\prime}(x))^{2}. Assumption [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") implies that iV,jV,JV,ℓV,LVi\_{V},j\_{V},J\_{V},\ell\_{V},L\_{V} are continuous and that
iV:ℝ→ℝi\_{V}:\mathbb{R}\to\mathbb{R} and jV,JV,ℓV,LV:ℝ→(0,∞)j\_{V},J\_{V},\ell\_{V},L\_{V}:\mathbb{R}\to(0,\infty). Note that, as these functions do not depend on BB, the same bounds work for
VT​(B)V\_{T}(B), which prove ([8](https://arxiv.org/html/2512.08348v1#S3.E8 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) for VT​(B)V\_{T}(B).

So, Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") holds for V​(B)V(B), and we can apply Lemma [3.2](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."). As

|  |  |  |
| --- | --- | --- |
|  | Γ​(B)​(eT−1,x,0)=𝔼​[V​(B)​(eT−1,εT,x)]=𝔼​[U​(x,B)]=VT​(B)​(eT,x),\Gamma(B)(e^{T-1},x,0)=\mathbb{E}\bigl[V(B)\bigl(e^{T-1},\varepsilon\_{T},x\bigr)\bigr]=\mathbb{E}\bigl[U(x,B)\bigr]=V\_{T}(B)(e^{T},x), |  |

x↦VT​(B)​(eT,x)x\mapsto V\_{T}(B)(e^{T},x) is twice continuously differentiable, and VT​(B)V\_{T}(B) also satisfies Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

Setting B=B​(ϕ)B=B(\phi) now, VT​(B​(ϕ))V\_{T}(B(\phi)) also satisfies Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") for an arbitrary ϕ∈Φ\phi\in\Phi. For simplicity, we
don’t write the dependence of BB on ϕ\phi until ([39](https://arxiv.org/html/2512.08348v1#S3.E39 "In 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). Proposition [3.3](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") for VT​(B)V\_{T}(B) implies
that there exist some functions
CT:ℝ→(0,∞)C\_{T}:\mathbb{R}\to(0,\infty) and
h¯​(B)T:ℝ(T−1)×m×ℝ→ℝ\bar{h}(B)\_{T}:\mathbb{R}^{(T-1)\times m}\times\mathbb{R}\to\mathbb{R}
such that CTC\_{T} is continuous, h¯​(B)T\bar{h}(B)\_{T} is ℬ​(ℝ(T−1)×m)⊗ℬ​(ℝ)\mathcal{B}(\mathbb{R}^{(T-1)\times m})\otimes\mathcal{B}(\mathbb{R})-measurable, and, for all eT−1,xe^{T-1},x,
|h¯​(B)T​(eT−1,x)|≤CT​(x),|\bar{h}(B)\_{T}(e^{T-1},x)|\leq C\_{T}(x),
and h¯​(B)T​(eT−1,x)\bar{h}(B)\_{T}(e^{T-1},x) is the unique number that satisfies

|  |  |  |
| --- | --- | --- |
|  | VT−1​(B)​(eT−1,x)=𝔼​[VT​(B)​(eT−1,εT,x+h¯​(B)T​(eT−1,x)​fT​(eT−1,εT))].V\_{T-1}(B)(e^{T-1},x)=\mathbb{E}\bigl[V\_{T}(B)\bigl(e^{T-1},\varepsilon\_{T},x+\bar{h}(B)\_{T}(e^{T-1},x)f\_{T}(e^{T-1},\varepsilon\_{T})\bigr)\bigr]. |  |

Furthermore, for all eT−1,e¯T−1∈ℝ(t−1)×me^{T-1},\bar{e}^{T-1}\in\mathbb{R}^{(t-1)\times m}, (recall that θ=χ\theta=\chi in ([9](https://arxiv.org/html/2512.08348v1#S3.E9 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) for VT​(B)V\_{T}(B)),

|  |  |  |
| --- | --- | --- |
|  | |h¯​(B)T​(eT−1,x)−h¯​(B)T​(e¯T−1,x)|≤CT​(x)​|eT−1−e¯T−1|χ/2.|\bar{h}(B)\_{T}(e^{T-1},x)-\bar{h}(B)\_{T}(\bar{e}^{T-1},x)|\leq C\_{T}(x)|e^{T-1}-\bar{e}^{T-1}|^{\chi/2}. |  |

Moreover, VT−1​(B)V\_{T-1}(B) satisfies Assumption [3.1](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") with θ=χ/2\theta=\chi/2 in ([9](https://arxiv.org/html/2512.08348v1#S3.E9 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). So, we can repeat the applications of Proposition [3.3](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."),
construct Ct:ℝ→(0,∞)C\_{t}:\mathbb{R}\to(0,\infty) and
h¯​(B)t:ℝ(t−1)×m×ℝ→ℝ\bar{h}(B)\_{t}:\mathbb{R}^{(t-1)\times m}\times\mathbb{R}\to\mathbb{R}, and obtain the same properties for them (with θ=χ/2T−t+1\theta=\chi/2^{T-t+1} in ([9](https://arxiv.org/html/2512.08348v1#S3.E9 "In Assumption 3.1. ‣ 3.1 One-step case ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."))), and Vt​(B)V\_{t}(B) for 1≤t≤T1\leq t\leq T.

Let ψ¯1∗=ψ¯1∗​(e0,x0):=h¯​(B)1​(x0)\bar{\psi}^{\*}\_{1}=\bar{\psi}^{\*}\_{1}(e\_{0},x\_{0}):=\bar{h}(B)\_{1}(x\_{0}) and define recursively

|  |  |  |
| --- | --- | --- |
|  | ψ¯t+1∗(et,x0):=h¯(B)t+1(et,x0+∑j=1tψ¯j∗(ej−1,x0)fj(ej)),\bar{\psi}^{\*}\_{t+1}(e^{t},x\_{0}):=\bar{h}(B)\_{t+1}\Bigr(e^{t},x\_{0}+\sum\_{j=1}^{t}\bar{\psi}^{\*}\_{j}(e^{j-1},x\_{0})f\_{j}(e^{j})\Bigr), |  |

for 1≤t≤T−11\leq t\leq T-1 and et∈ℝt×me^{t}\in\mathbb{R}^{t\times m}.

We prove by induction that |ψ¯t∗​(et−1,x0)|≤C¯t​(x0)|\bar{\psi}^{\*}\_{t}(e^{t-1},x\_{0})|\leq\bar{C}\_{t}(x\_{0}) for all et−1∈ℝ(t−1)×me^{t-1}\in\mathbb{R}^{(t-1)\times m}, for some continuous function C¯t\bar{C}\_{t}.
For t=1t=1, just choose C¯1=C1.\bar{C}\_{1}={C}\_{1}. Assume that the induction holds until tt with 1≤t≤T−21\leq t\leq T-2. Then,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ψ¯t+1∗​(et,x0)|\displaystyle|\bar{\psi}^{\*}\_{t+1}(e^{t},x\_{0})| | ≤\displaystyle\leq | Ct+1(x0+∑j=1tψ¯j∗(ej−1,x0)fj(ej))\displaystyle C\_{t+1}\Bigr(x\_{0}+\sum\_{j=1}^{t}\bar{\psi}^{\*}\_{j}(e^{j-1},x\_{0})f\_{j}(e^{j})\Bigr) |  |
|  |  | ≤\displaystyle\leq | supy∈Kt​(x0)Ct+1(y)=:C¯t+1(x0)\displaystyle\sup\_{y\in K\_{t}(x\_{0})}C\_{t+1}(y)=:\bar{C}\_{t+1}(x\_{0}) |  |

where Kt​(x)=[x−Cf​∑j=1tC¯j​(x),x+Cf​∑j=1tC¯j​(x)]K\_{t}(x)=[x-C\_{f}\sum\_{j=1}^{t}\bar{C}\_{j}(x),x+C\_{f}\sum\_{j=1}^{t}\bar{C}\_{j}(x)]. Lemma [4.4](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") shows that C¯t+1\bar{C}\_{t+1} is continous.
Now, ([35](https://arxiv.org/html/2512.08348v1#S3.E35 "In Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds choosing C​(x0)=max1≤t≤T⁡C¯t​(x0).C(x\_{0})=\max\_{1\leq t\leq T}\bar{C}\_{t}(x\_{0}). It is clear that CC is continuous.
As the Ct{C}\_{t} do not depend on BB (and thus on ϕ\phi), CC does not depend on ϕ\phi.
For ([36](https://arxiv.org/html/2512.08348v1#S3.E36 "In Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), just observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |ψ¯t∗​(et−1,x0)−ψ¯t∗​(e¯t−1,x0)|\displaystyle\hskip-56.9055pt|\bar{\psi}^{\*}\_{t}(e^{t-1},x\_{0})-\bar{\psi}^{\*}\_{t}(\bar{e}^{t-1},x\_{0})| |  |
|  |  | ≤\displaystyle\leq | Ct​(x0+∑j=1t−1ψ¯j∗​(ej−1,x0)​fj​(ej))​|et−1−e¯t−1|χ/2T−t+1\displaystyle C\_{t}\Bigl(x\_{0}+\sum\_{j=1}^{t-1}\bar{\psi}^{\*}\_{j}(e^{j-1},x\_{0})f\_{j}(e^{j})\Bigr)|e^{t-1}-\bar{e}^{t-1}|^{\chi/2^{T-t+1}} |  |
|  |  | ≤\displaystyle\leq | C​(x0)​|et−1−e¯t−1|χ/2T−t+1.\displaystyle C(x\_{0})|e^{t-1}-\bar{e}^{t-1}|^{\chi/2^{T-t+1}}. |  |

We finally establish that the strategy ψ1∗:=ψ¯1∗\psi^{\*}\_{1}:=\bar{\psi}^{\*}\_{1} and
ψt+1∗:=ψ¯t+1∗​(εt)\psi^{\*}\_{t+1}:=\bar{\psi}^{\*}\_{t+1}(\varepsilon^{t}), 1≤t≤T−11\leq t\leq T-1
is optimal, that is, ψ∗∈Φ\psi^{\*}\in\Phi, and for all ψ∈Φ\psi\in\Phi,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[U​(WT​(x0,ψ∗​(ϕ)),B​(ϕ))]≥𝔼​[U​(WT​(x0,ψ),B​(ϕ))].\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi^{\*}(\phi)),B(\phi)\bigr)\bigr]\geq\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi),B(\phi)\bigr)\bigr]. |  | (39) |

As the h¯​(B)t\bar{h}(B)\_{t} are jointly Borel measurable and the fjf\_{j} are Borel measurable, we can show by induction that the ψ¯t∗\bar{\psi}^{\*}\_{t} are Borel functions, and thus ψ∗∈Φ\psi^{\*}\in\Phi.
  
Fix ψ∈Φ\psi\in\Phi. We write ψt=ψ¯t​(εt−1)\psi\_{t}=\bar{\psi}\_{t}(\varepsilon^{t-1}), where ψ¯t\bar{\psi}\_{t} is a Borel function given by Doob’s theorem for 1≤t≤T1\leq t\leq T.
Notice that, by independence of εT\varepsilon^{T} and ε^T\hat{\varepsilon}^{T}, and thus of εT\varepsilon^{T} and B​(ϕ)=WT​(x0,ϕ)​(ε^T)B(\phi)=W\_{T}(x\_{0},\phi)(\hat{\varepsilon}^{T}), we obtain that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | 𝔼​[U​(WT​(x0,ψ),B​(ϕ))]=𝔼​[U​(WT​(x0,ψ)​(εT),WT​(x0,ϕ)​(ε^T))]\displaystyle\hskip-28.45274pt\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi),B(\phi)\bigr)\bigr]=\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi)(\varepsilon^{T}),W\_{T}(x\_{0},\phi)(\hat{\varepsilon}^{T})\bigr)\bigr] |  |
|  |  | =\displaystyle= | 𝔼​[𝔼​[U​(WT​(x0,ψ)​(εT),WT​(x0,ϕ)​(ε^T))|ℱTε]]\displaystyle\mathbb{E}\bigl[\mathbb{E}[U\bigl(W\_{T}(x\_{0},\psi)(\varepsilon^{T}),W\_{T}(x\_{0},\phi)(\hat{\varepsilon}^{T})\bigr)|\mathcal{F}\_{T}^{\varepsilon}]\bigr] |  |
|  |  | =\displaystyle= | 𝔼​[𝔼​[U​(WT​(x0,ψ)​(eT),WT​(x0,ϕ)​(ε^T))]|eT=εT]\displaystyle\mathbb{E}\bigl[\mathbb{E}[U\bigl(W\_{T}(x\_{0},\psi)(e^{T}),W\_{T}(x\_{0},\phi)(\hat{\varepsilon}^{T})\bigr)]\big|\_{e^{T}=\varepsilon^{T}}\bigr] |  |
|  |  | =\displaystyle= | 𝔼​[VT​(B​(ϕ))​(εT,x0+∑j=1Tψ¯j​(εj−1)​fj​(εj))]\displaystyle\mathbb{E}\bigl[V\_{T}\bigl(B(\phi)\bigr)\bigl(\varepsilon^{T},x\_{0}+\sum\_{j=1}^{T}\bar{\psi}\_{j}(\varepsilon^{j-1})f\_{j}(\varepsilon^{j})\bigr)\bigr] |  |
|  |  | =\displaystyle= | 𝔼​[𝔼​[VT​(B​(ϕ))​(εT,x0+∑j=1T−1ψ¯j​(εj−1)​fj​(εj)+ψ¯T​(εT−1)​fT​(εT))|ℱT−1ε]]\displaystyle\mathbb{E}\Bigl[\mathbb{E}\bigl[V\_{T}\bigl(B(\phi)\bigr)\bigl(\varepsilon^{T},x\_{0}+\sum\_{j=1}^{T-1}\bar{\psi}\_{j}(\varepsilon^{j-1})f\_{j}(\varepsilon^{j})+\bar{\psi}\_{T}(\varepsilon^{T-1})f\_{T}(\varepsilon^{T})\bigr)|\mathcal{F}^{\varepsilon}\_{T-1}\bigr]\Bigr] |  |
|  |  | =\displaystyle= | 𝔼[𝔼[VT(B(ϕ))(eT−1,εT,x0+∑j=1T−1ψ¯j(ej−1)fj(ej)\displaystyle\mathbb{E}\Bigl[\mathbb{E}\bigl[V\_{T}\bigl(B(\phi)\bigr)\bigl(e^{T-1},\varepsilon\_{T},x\_{0}+\sum\_{j=1}^{T-1}\bar{\psi}\_{j}(e^{j-1})f\_{j}(e^{j}) |  |
|  |  |  | +ψ¯T(eT−1)fT(eT−1,εT))]|eT−1=εT−1]\displaystyle+\bar{\psi}\_{T}(e^{T-1})f\_{T}(e^{T-1},\varepsilon\_{T})\bigr)\bigr]\big|\_{e^{T-1}=\varepsilon^{T-1}}\Bigr] |  |
|  |  | ≤\displaystyle\leq | 𝔼​[VT−1​(B​(ϕ))​(εT−1,x0+∑j=1T−1ψ¯j​(εj−1)​fj​(εj))]\displaystyle\mathbb{E}\bigl[V\_{T-1}\bigl(B(\phi)\bigr)\bigl(\varepsilon^{T-1},x\_{0}+\sum\_{j=1}^{T-1}\bar{\psi}\_{j}(\varepsilon^{j-1})f\_{j}(\varepsilon^{j})\bigr)\bigr] |  |
|  |  | =\displaystyle= | 𝔼​[𝔼​[VT−1​(B​(ϕ))​(εT−1,x0+∑j=1T−1ψ¯j​(εj−1)​fj​(εj))|ℱT−2ε]]\displaystyle\mathbb{E}\Bigl[\mathbb{E}\bigl[V\_{T-1}\bigl(B(\phi)\bigr)\bigl(\varepsilon^{T-1},x\_{0}+\sum\_{j=1}^{T-1}\bar{\psi}\_{j}(\varepsilon^{j-1})f\_{j}(\varepsilon^{j})\bigr)|\mathcal{F}^{\varepsilon}\_{T-2}\bigr]\Bigr] |  |
|  |  | ≤\displaystyle\leq | 𝔼​[VT−2​(B​(ϕ))​(εT−2,x0+∑j=1T−2ψ¯j​(εj−1)​fj​(εj))]=…≤V0​(B​(ϕ))​(x0),\displaystyle\mathbb{E}\bigl[V\_{T-2}\bigl(B(\phi)\bigr)\bigl(\varepsilon^{T-2},x\_{0}+\sum\_{j=1}^{T-2}\bar{\psi}\_{j}(\varepsilon^{j-1})f\_{j}(\varepsilon^{j})\bigr)\bigr]=\ldots\leq V\_{0}\bigl(B(\phi)\bigr)(x\_{0}), |  |

holds by repeated applications of Lemma [4.5](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."): first we take X1=B​(ϕ)=WT​(x0,ϕ)​(ε^T)X\_{1}=B(\phi)=W\_{T}(x\_{0},\phi)(\hat{\varepsilon}^{T}) and X2=εTX\_{2}=\varepsilon^{T};
then X1=εTX\_{1}=\varepsilon\_{T} and X2=εT−1X\_{2}=\varepsilon^{T-1}, and so on.
If we insert ψ¯=ψ¯∗=ψ¯∗​(ϕ)​(⋅,x0)\bar{\psi}=\bar{\psi}^{\*}=\bar{\psi}^{\*}(\phi)(\cdot,x\_{0}) in the above estimate then it holds with *equalities* everywhere, i.e.

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U​(WT​(x0,ψ∗​(ϕ)),B​(ϕ))]=V0​(B​(ϕ))​(x0),\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},{\psi}^{\*}(\phi)),B(\phi)\bigr)\bigr]=V\_{0}\bigl(B(\phi)\bigr)(x\_{0}), |  |

and ([39](https://arxiv.org/html/2512.08348v1#S3.E39 "In 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds. Then,
taking the supremum over ψ\psi in ([39](https://arxiv.org/html/2512.08348v1#S3.E39 "In 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."))

|  |  |  |
| --- | --- | --- |
|  | u​(x0,ϕ)=supψ∈Φ𝔼​[U​(WT​(x0,ψ),B​(ϕ))]≤𝔼​[U​(WT​(x0,ψ∗​(ϕ)),B​(ϕ))]≤u​(x0,ϕ),\displaystyle u(x\_{0},\phi)=\sup\_{\psi\in\Phi}\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi),B(\phi)\bigr)\bigr]\leq\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},{\psi}^{\*}(\phi)),B(\phi)\bigr)\bigr]\leq u(x\_{0},\phi), |  |

as ψ∗​(ϕ)∈Φ.{\psi}^{\*}(\phi)\in\Phi.
This implies that

|  |  |  |
| --- | --- | --- |
|  | u​(x0,ϕ)=𝔼​[U​(WT​(x0,ψ∗​(ϕ)),B​(ϕ))]=V0​(B​(ϕ))​(x0).u(x\_{0},\phi)=\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},{\psi}^{\*}(\phi)),B(\phi)\bigr)\bigr]=V\_{0}\big(B(\phi)\big)(x\_{0}). |  |

The unicity of ψ∗{\psi}^{\*} follows from the unicity of the h¯​(B)t\bar{h}(B)\_{t} for 1≤t≤T1\leq t\leq T.
∎

### 3.3 Fixed point theorem, and remaining proofs

Recall that εT−1:=(ε1,…,εT−1){\varepsilon}^{T-1}:=(\varepsilon\_{1},\ldots,\varepsilon\_{T-1}). We now introduce 𝒮:=supp​(εT−1)\mathcal{S}:=\mathrm{supp}(\varepsilon^{T-1}), where supp​(⋅)\mathrm{supp}(\cdot) refers to the support (see for example, p 441 of [[1](https://arxiv.org/html/2512.08348v1#bib.bib1)]). Theorems 12.7 and 12.14 of [[1](https://arxiv.org/html/2512.08348v1#bib.bib1)] show that
ℙ[εT−1∈.]\mathbb{P}[\varepsilon^{T-1}\in.] admits a unique support such that ℙ​[εT−1∈𝒮]=1\mathbb{P}[\varepsilon^{T-1}\in\mathcal{S}]=1, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | supp​(εT−1):=⋂{A⊂ℝ(T−1)×m,closed,ℙ​[εT−1∈A]=1}.\displaystyle\mathrm{supp}(\varepsilon^{T-1}):=\bigcap\left\{A\subset\mathbb{R}^{(T-1)\times m},\;\mbox{closed},\;\mathbb{P}[\varepsilon^{T-1}\in A]=1\right\}. |  | (40) |

Assumptions [2.1](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), and [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") will be in force in the rest of this section.
By independence of (ε1,…,εT−1)(\varepsilon\_{1},\ldots,\varepsilon\_{T-1}) under ℙ\mathbb{P},
𝒮=supp​(ε1)×⋯×supp​(εT−1)\mathcal{S}=\mathrm{supp}(\varepsilon\_{1})\times\cdots\times\mathrm{supp}(\varepsilon\_{T-1}).

Let C​(𝒮)C(\mathcal{S}) denote the Banach space of ℝT\mathbb{R}^{T}-valued continuous functions on 𝒮\mathcal{S}, equipped with the norm

|  |  |  |
| --- | --- | --- |
|  | ‖φ‖∞:=supe∈𝒮|φ​(e)|,φ∈C​(𝒮).||\varphi||\_{\infty}:=\sup\_{e\in\mathcal{S}}|\varphi(e)|,\ \varphi\in C(\mathcal{S}). |  |

At this point, we explain an important identification. If ϕ∈Φ\phi\in\Phi then, by Doob’s theorem, there are
Borel measurable functions φ¯t:ℝ(t−1)×m→ℝ\bar{\varphi}\_{t}:\mathbb{R}^{(t-1)\times m}\to\mathbb{R}, 1≤t≤T1\leq t\leq T (we mean that φ¯1\bar{\varphi}\_{1} is
a constant) such that
ϕt=φ¯t​(ε1,…,εt−1)\phi\_{t}=\bar{\varphi}\_{t}(\varepsilon\_{1},\ldots,\varepsilon\_{t-1}). Now let us define for all 1≤t≤T1\leq t\leq T the functions ϕ~t:𝒮→ℝ\tilde{\phi}\_{t}:\mathcal{S}\to\mathbb{R}
by setting

|  |  |  |
| --- | --- | --- |
|  | ϕ~t​(e1,…,eT−1):=φ¯t​(e1,…,et−1).\tilde{\phi}\_{t}(e\_{1},\ldots,e\_{T-1}):=\bar{\varphi}\_{t}(e\_{1},\ldots,e\_{t-1}). |  |

In this way, we obtain a ℬ​(𝒮)\mathcal{B}(\mathcal{S})-measurable function ϕ~:=(ϕ~1,…,ϕ~T)\tilde{\phi}:=(\tilde{\phi}\_{1},\ldots,\tilde{\phi}\_{T}) with
ϕ~:𝒮→ℝT\tilde{\phi}:\mathcal{S}\to\mathbb{R}^{T} is such that the ttth coordinate function ϕ~t\tilde{\phi}\_{t}
depends uniquely on its first t−1t-1 coordinates.
Conversely, if ϕ~:𝒮→ℝT\tilde{\phi}:\mathcal{S}\to\mathbb{R}^{T} is such a function, then definining

|  |  |  |
| --- | --- | --- |
|  | ϕt:=ϕ~t​(ε1,…,εT−1), 1≤t≤T,\phi\_{t}:=\tilde{\phi}\_{t}(\varepsilon\_{1},\ldots,\varepsilon\_{T-1}),\;1\leq t\leq T, |  |

we obtain an element ϕ∈Φ\phi\in\Phi. Indeed, each ϕ~t\tilde{\phi}\_{t} is ℬ​(𝒮)\mathcal{B}(\mathcal{S})-measurable
and as ϕt=ϕ~t​(ε1,…,εt−1,0​…,0)\phi\_{t}=\tilde{\phi}\_{t}(\varepsilon\_{1},\ldots,\varepsilon\_{t-1},0\ldots,0) ϕt\phi\_{t} is ℱt−1ε\mathcal{F}^{\varepsilon}\_{t-1}-measurable.
¿From this moment on, we identify each ϕ∈Φ\phi\in\Phi
with a corresponding Borel measurable function ϕ~:𝒮→ℝT\tilde{\phi}:\mathcal{S}\to\mathbb{R}^{T}. When we write ϕ∈C​(𝒮)\phi\in C(\mathcal{S}) we mean that the ϕ~\tilde{\phi}
corresponding to ϕ\phi can be chosen continuous.
Note also that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Wt​(x0,ϕ)\displaystyle W\_{t}(x\_{0},\phi) | =\displaystyle= | x0+∑j=1tϕj​Δ​Sj=x0+∑j=1tϕ~j​(ε1,…,εT−1)​fj​(ε1,…,εj)\displaystyle x\_{0}+\sum\_{j=1}^{t}\phi\_{j}\Delta S\_{j}=x\_{0}+\sum\_{j=1}^{t}\tilde{\phi}\_{j}(\varepsilon\_{1},\ldots,\varepsilon\_{T-1})f\_{j}(\varepsilon\_{1},\ldots,\varepsilon\_{j}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | B​(ϕ)\displaystyle B({\phi}) | =\displaystyle= | x0+∑t=1Tϕ~t​(ε^1,…,ε^T−1)​ft​(ε^1,…,ε^t),\displaystyle x\_{0}+\sum\_{t=1}^{T}\tilde{\phi}\_{t}(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{T-1})f\_{t}(\hat{\varepsilon}\_{1},\ldots,\hat{\varepsilon}\_{t}), |  |

we stress one more time that here ϕ~j\tilde{\phi}\_{j} depends only on its first j−1j-1 coordinates.
Finally, for each M>0M>0, ϕ∈ΦM\phi\in\Phi\_{M} if and only if ϕ∈Φ\phi\in\Phi, and for all 1≤t≤T1\leq t\leq T, setting ϕt=φ~t​(ε1,…,εT−1)\phi\_{t}=\tilde{\varphi}\_{t}(\varepsilon\_{1},\ldots,\varepsilon\_{T-1}) as before,
for all eT−1,e¯T−1∈ℝ(T−1)×me^{T-1},\bar{e}^{T-1}\in\mathbb{R}^{(T-1)\times m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |φ~t​(eT−1)|≤M​ and ​|φ~t​(eT−1)−φ~t​(e¯T−1)|≤M​|eT−1−e¯T−1|χ/2T−t+1.\displaystyle|\tilde{\varphi}\_{t}(e^{T-1})|\leq M\mbox{ and }|\tilde{\varphi}\_{t}(e^{T-1})-\tilde{\varphi}\_{t}(\bar{e}^{T-1})|\leq M|e^{T-1}-\bar{e}^{T-1}|^{\chi/2^{T-t+1}}. |  | (41) |

It is clear that ΦM⊂C​(𝒮)\Phi\_{M}\subset C(\mathcal{S}). Moreover, Proposition [4.8](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below shows that ΦM\Phi\_{M} is relatively compact in
C​(𝒮)C(\mathcal{S}). Indeed, the left-hand side of ([41](https://arxiv.org/html/2512.08348v1#S3.E41 "In 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) implies that |φ~|≤M​T|\tilde{\varphi}|\leq M\sqrt{T}, which proves
the first condition of Proposition [4.8](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."). For the second one, let ϕ∈ΦM\phi\in\Phi\_{M}, eT−1,e¯T−1∈ℝ(T−1)×me^{T-1},\bar{e}^{T-1}\in\mathbb{R}^{(T-1)\times m}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |φ~​(eT−1)−φ~​(e¯T−1)|\displaystyle|\tilde{\varphi}(e^{T-1})-\tilde{\varphi}(\bar{e}^{T-1})| | =\displaystyle= | (∑t=1T|φ~t​(eT−1)−φ~t​(e¯T−1)|2)1/2\displaystyle\Big(\sum\_{t=1}^{T}|\tilde{\varphi}\_{t}(e^{T-1})-\tilde{\varphi}\_{t}(\bar{e}^{T-1})|^{2}\Big)^{1/2} |  |
|  |  | ≤\displaystyle\leq | M​(∑t=1T|eT−1−e¯T−1|χ/2T−t)1/2\displaystyle M\Big(\sum\_{t=1}^{T}|e^{T-1}-\bar{e}^{T-1}|^{\chi/2^{T-t}}\Big)^{1/2} |  |
|  |  | ≤\displaystyle\leq | T​M2+2​T​M2​|eT−1−e¯T−1|χ/2T−2,\displaystyle\sqrt{TM^{2}+2TM^{2}}|e^{T-1}-\bar{e}^{T-1}|^{\chi/2^{T-2}}, |  |

reasonning as in Lemma [4.3](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), which shows ([62](https://arxiv.org/html/2512.08348v1#S4.E62 "In Proposition 4.8. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).
Moreover, ΦM\Phi\_{M} is trivially closed, and thus compact.

One key result for our arguments is the following.

###### Proposition 3.5.

Let Assumptions [2.1](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") and [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") hold.
Let x0∈ℝx\_{0}\in\mathbb{R}. For all ϕ∈Φ\phi\in\Phi, let ψ∗:=ψ∗​(ϕ)​(⋅,x0)∈Φ\psi^{\*}:=\psi^{\*}(\phi)(\cdot,x\_{0})\in\Phi
be the optimizer of ([7](https://arxiv.org/html/2512.08348v1#S2.E7 "In 2.3 Personal equilibrium ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) given by Proposition [3.4](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").
Then, the mapping ϕ↦ψ∗​(ϕ)\phi\mapsto\psi^{\*}(\phi) is continuous (for the norm of C​(𝒮)C(\mathcal{S})) from
ΦC​(x0)\Phi\_{C(x\_{0})} to ΦC​(x0)\Phi\_{C(x\_{0})}.

###### Proof.

Recall the notation of Proposition [3.4](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."). However, for ease of exposition, we don’t indicate the dependence of ψ∗\psi^{\*} on x0x\_{0}.
We make the identification above and associate to ψ∗​(ϕ)\psi^{\*}(\phi), the function ψ~∗​(ϕ):𝒮→ℝT\tilde{\psi}^{\*}(\phi):\mathcal{S}\to\mathbb{R}^{T}, i.e. ψ~∗​(ϕ)t​(eT−1)=ψ¯∗​(ϕ)t​(et−1).\tilde{\psi}^{\*}(\phi)\_{t}(e^{T-1})=\bar{\psi}^{\*}(\phi)\_{t}(e^{t-1}).
Using ([35](https://arxiv.org/html/2512.08348v1#S3.E35 "In Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([36](https://arxiv.org/html/2512.08348v1#S3.E36 "In Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), ψ∗​(ϕ)∈ΦC​(x0).\psi^{\*}(\phi)\in\Phi\_{C(x\_{0})}. So, ϕ↦ψ~∗​(ϕ)\phi\mapsto\tilde{\psi}^{\*}(\phi) maps ΦC​(x0)\Phi\_{C(x\_{0})} (in fact, the whole of Φ\Phi)
into ΦC​(x0)\Phi\_{C(x\_{0})}.

Now let (ϕ~n)n⊂ΦC​(x0)(\tilde{\phi}^{n})\_{n}\subset\Phi\_{C(x\_{0})} that converge to ϕ~\tilde{\phi} in the topology of the Banach space C​(𝒮)C(\mathcal{S}), i.e. ‖ϕ~n−ϕ~‖∞→0,n→∞\|\tilde{\phi}^{n}-\tilde{\phi}\|\_{\infty}\to 0,\,n\to\infty.
We call ϕn{\phi}^{n} and ϕ{\phi} the associated elements of Φ\Phi.
We want to prove that ‖ψ~∗​(ϕn)−ψ~∗​(ϕ)‖∞→0,n→∞\|\tilde{\psi}^{\*}({\phi}^{n})-\tilde{\psi}^{\*}(\phi)\|\_{\infty}\to 0,\,n\to\infty.

First, remark that for all ω∈Ω\omega\in\Omega and n∈ℕn\in\mathbb{N}

|  |  |  |  |
| --- | --- | --- | --- |
|  | |B​(ϕn)​(ω)−B​(ϕ)​(ω)|≤∑j=1T‖ϕ~n−ϕ~‖∞​|fj​(ε^j​(ω))|≤T​Cf​‖ϕ~n−ϕ~‖∞\displaystyle|B({\phi}^{n})(\omega)-B({\phi})(\omega)|\leq\sum\_{j=1}^{T}\|\tilde{\phi}^{n}-\tilde{\phi}\|\_{\infty}|f\_{j}\big(\hat{\varepsilon}^{j}(\omega)\big)|\leq TC\_{f}\|\tilde{\phi}^{n}-\tilde{\phi}\|\_{\infty} |  | (42) |

so B​(ϕn)​(ω)→B​(ϕ)​(ω)B({\phi}^{n})(\omega)\to B(\phi)(\omega) for all ω∈Ω\omega\in\Omega.
Define the random utility functions for all n∈ℕn\in\mathbb{N}, x∈ℝx\in\mathbb{R}, ω∈Ω\omega\in\Omega

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔘n​(ω,x)\displaystyle\mathfrak{U}\_{n}(\omega,x) | :=\displaystyle:= | U​(x,B​(ϕn)​(ω))=U​(x)+ν​(U​(x)−U​(B​(ϕn)​(ω)))\displaystyle U\big(x,B({\phi}^{n})(\omega)\big)=U(x)+\nu\Big(U(x)-U\big(B({\phi}^{n})(\omega)\big)\Big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔘∞​(ω,x)\displaystyle\mathfrak{U}\_{\infty}(\omega,x) | :=\displaystyle:= | U​(x,B​(ϕ)​(ω))=U​(x)+ν​(U​(x)−U​(B​(ϕ)​(ω))).\displaystyle U\big(x,B({\phi})(\omega)\big)=U(x)+\nu\Big(U(x)-U\big(B({\phi})(\omega)\big)\Big). |  |

Let ℕ¯:=ℕ∪{∞}\bar{\mathbb{N}}:=\mathbb{N}\cup\{\infty\}.
We will now verify the conditions of Theorem [4.7](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem7 "Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below. Assumptions [2.8](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") and [2.10](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") imply that for all n∈ℕ¯n\in\bar{\mathbb{N}}, each 𝔘n\mathfrak{U}\_{n} is strictly concave and increasing, continuously differentiable in xx.
Using ([6](https://arxiv.org/html/2512.08348v1#S2.E6 "In Remark 2.11. ‣ 2.2 Hypotheses on the investor’s preferences ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), for all x1,x2∈ℝ,x\_{1},x\_{2}\in\mathbb{R}, all random variables B1,B2B\_{1},B\_{2}

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |U​(x1,B1)−U​(x2,B2)|\displaystyle|U(x\_{1},B\_{1})-U(x\_{2},B\_{2})| | ≤\displaystyle\leq | (1+k−)​|U​(x1)−U​(x2)|+k−​|B1−B2|.\displaystyle(1+k\_{-})|U(x\_{1})-U(x\_{2})|+k\_{-}|B\_{1}-B\_{2}|. |  | (43) |

This implies that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | supn∈ℕ¯,ω∈Ω[𝔘n​(ω,∞)−𝔘n​(ω,x)]\displaystyle\sup\_{n\in\bar{\mathbb{N}},\omega\in\Omega}\bigl[\mathfrak{U}\_{n}(\omega,\infty)-\mathfrak{U}\_{n}(\omega,x)\bigr] | =\displaystyle= | supn∈ℕ¯,ω∈Ω|U​(∞,B​(ϕn)​(ω))−U​(x,B​(ϕn)​(ω))|\displaystyle\sup\_{n\in\bar{\mathbb{N}},\omega\in\Omega}|U\big(\infty,B({\phi}^{n})(\omega)\big)-U\big(x,B({\phi}^{n})(\omega)\big)| |  | (44) |
|  |  | ≤\displaystyle\leq | (1+k−)​|U​(∞)−U​(x)|→0,\displaystyle(1+k\_{-})|U(\infty)-U(x)|\to 0, |  |

as x→∞x\to\infty, implying ([56](https://arxiv.org/html/2512.08348v1#S4.E56 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) below, and also

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |𝔘n​(ω,x)−𝔘∞​(ω,x)|\displaystyle\bigl|\mathfrak{U}\_{n}(\omega,x)-\mathfrak{U}\_{\infty}(\omega,x)\bigr| | =\displaystyle= | |U​(x,B​(ϕn)​(ω))−U​(x,B​(ϕ)​(ω))|\displaystyle\bigl|U\big(x,B({\phi}^{n})(\omega)\big)-U\big(x,B({\phi})(\omega)\big)\bigr| |  |
|  |  | ≤\displaystyle\leq | k−​|B​(ϕn)​(ω)−B​(ϕ)​(ω)|,\displaystyle k\_{-}|B({\phi}^{n})(\omega)-B({\phi})(\omega)|, |  |

and ([42](https://arxiv.org/html/2512.08348v1#S3.E42 "In 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) implies that 𝔘n​(ω,x)→𝔘∞​(ω,x),\mathfrak{U}\_{n}(\omega,x)\to\mathfrak{U}\_{\infty}(\omega,x), n→∞n\to\infty for all ω∈Ω\omega\in\Omega
and for all x∈ℝ.x\in\mathbb{R}. So, ([58](https://arxiv.org/html/2512.08348v1#S4.E58 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds true.
Moreover,

|  |  |  |
| --- | --- | --- |
|  | 𝔘n′​(ω,0)=U′​(0,B​(ϕn)​(ω)),𝔘∞′​(ω,0)=U′​(0,B​(ϕ)​(ω))\displaystyle\mathfrak{U}\_{n}^{\prime}(\omega,0)=U^{\prime}\big(0,B({\phi}^{n})(\omega)\big),\quad\mathfrak{U}\_{\infty}^{\prime}(\omega,0)=U^{\prime}\big(0,B({\phi})(\omega)\big) |  |

so ([38](https://arxiv.org/html/2512.08348v1#S3.E38 "In 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) implies that
ess.infn∈ℕ¯𝔘n′​(ω,0)≥U′​(0)>0\mathrm{ess.}\inf\_{n\in\bar{\mathbb{N}}}\mathfrak{U}\_{n}^{\prime}(\omega,0)\geq U^{\prime}(0)>0 and ([57](https://arxiv.org/html/2512.08348v1#S4.E57 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds true.
Morover, ([37](https://arxiv.org/html/2512.08348v1#S3.E37 "In 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) implies that

|  |  |  |
| --- | --- | --- |
|  | (1+k−)​U​(x)−k−​CU≤U​(x,B)≤CU+Cν.\displaystyle(1+k\_{-})U(x)-k\_{-}C\_{U}\leq U(x,B)\leq C\_{U}+C\_{\nu}. |  |

So, for all x∈ℝx\in\mathbb{R} and ω∈Ω\omega\in\Omega

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ess.supn∈ℕ¯|𝔘n​(ω,x)|\displaystyle\mathrm{ess.}\sup\_{n\in\bar{\mathbb{N}}}|\mathfrak{U}\_{n}(\omega,x)| | ≤\displaystyle\leq | (1+k−)​CU+Cν+(1+k−)​|U​(x)|<∞,\displaystyle(1+k\_{-})C\_{U}+C\_{\nu}+(1+k\_{-})|U(x)|<\infty, |  |

As, for all n∈ℕ¯n\in\bar{\mathbb{N}} and ω∈Ω\omega\in\Omega , 𝔘n​(ω,∞)≥𝔘n​(ω,0)\mathfrak{U}\_{n}(\omega,\infty)\geq\mathfrak{U}\_{n}(\omega,0),

|  |  |  |
| --- | --- | --- |
|  | CU+Cν≥ess.infn∈ℕ¯𝔘n​(ω,∞)≥(1+k−)​U​(0)−k−​CU>−∞,\displaystyle C\_{U}+C\_{\nu}\geq\mathrm{ess.}\inf\_{n\in\bar{\mathbb{N}}}\mathfrak{U}\_{n}(\omega,\infty)\geq(1+k\_{-})U(0)-k\_{-}C\_{U}>-\infty, |  |

and ([55](https://arxiv.org/html/2512.08348v1#S4.E55 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds true.

Recall that
ψ∗​(ϕn){\psi}^{\*}(\phi^{n}) (resp. ψ∗​(ϕ){\psi}^{\*}(\phi)) is the optimizer of ([7](https://arxiv.org/html/2512.08348v1#S2.E7 "In 2.3 Personal equilibrium ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) given by Proposition [3.4](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") for ϕn\phi^{n}
(resp. ϕ\phi). It is thus the (unique) optimizer for 𝔘n\mathfrak{U}\_{n} (resp. 𝔘∞\mathfrak{U}\_{\infty}) in ([59](https://arxiv.org/html/2512.08348v1#S4.E59 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).
Theorem [4.7](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem7 "Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ∗​(ϕn)t→ψ∗​(ϕ)t\psi^{\*}(\phi^{n})\_{t}\to\psi^{\*}(\phi)\_{t} |  | (45) |

almost surely for all 1≤t≤T1\leq t\leq T.
Recalling the notation of the beginning of the proof, providing the identification of the above of strategies with continuous functions on 𝒮\mathcal{S}, for all n∈ℕn\in\mathbb{N}, we have
ψ∗​(ϕn)=ψ~∗​(n)​(εT−1)\psi^{\*}(\phi^{n})=\tilde{\psi}^{\*}(n)(\varepsilon^{T-1}) and ψ∗​(ϕ)=ψ~∗​(εT−1).\psi^{\*}(\phi)=\tilde{\psi}^{\*}(\varepsilon^{T-1}). For ease of notation, we set ψ~∗​(n)\tilde{\psi}^{\*}(n) for ψ∗​(ϕn)\psi^{\*}(\phi^{n}) and ψ~∗\tilde{\psi}^{\*} for ψ∗​(ϕ)\psi^{\*}(\phi).
Then, ([45](https://arxiv.org/html/2512.08348v1#S3.E45 "In 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) implies that for all 1≤t≤T1\leq t\leq T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~t∗​(n)→ψ~t∗\tilde{\psi}^{\*}\_{t}(n)\to\tilde{\psi}^{\*}\_{t} |  | (46) |

μ\mu-almost surely, where μ\mu denotes the law of εT−1\varepsilon^{T-1} under ℙ\mathbb{P}. Since 𝒮\mathcal{S} is the support of μ\mu,
ψ~t∗​(n)→ψ~t∗\tilde{\psi}^{\*}\_{t}(n)\to\tilde{\psi}^{\*}\_{t} pointwise on a dense subset of 𝒮\mathcal{S}, see Lemma [4.6](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below.

Seeking a contradiction, suppose that ψ~∗​(n)\tilde{\psi}^{\*}({n}) do not converge to
ψ~∗\tilde{\psi}^{\*} in the norm of C​(𝒮)C(\mathcal{S}). Then, along a subsequence (still denoted by nn)
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | infn‖ψ~∗​(n)−ψ~∗‖∞>0.\inf\_{n}||\tilde{\psi}^{\*}(n)-\tilde{\psi}^{\*}||\_{\infty}>0. |  | (47) |

By compactness of ΦC​(x0)\Phi\_{C(x\_{0})}, a further subsequence of ψ~∗​(n)\tilde{\psi}^{\*}({n}) can be chosen (still denoted by nn)
such that ‖ψ~∗​(n)−ψ^‖∞→0||\tilde{\psi}^{\*}(n)-\hat{\psi}||\_{\infty}\to 0, n→∞n\to\infty for some ψ^∈ΦC​(x0)\hat{\psi}\in\Phi\_{C(x\_{0})}.
Since ([46](https://arxiv.org/html/2512.08348v1#S3.E46 "In 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds pointwise on a dense subset of 𝒮\mathcal{S}, ψ^=ψ~∗\hat{\psi}=\tilde{\psi}^{\*} on this set and, by continuity, on the whole of 𝒮\mathcal{S}.
But this contradicts ([47](https://arxiv.org/html/2512.08348v1#S3.E47 "In 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).
∎

We can finally achieve the proof of our main result.

###### Proof of Theorem [2.14](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem14 "Theorem 2.14. ‣ 2.3 Personal equilibrium ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

Recalling the notation of Proposition [3.5](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), the mapping ϕ↦ψ∗​(ϕ)\phi\mapsto\psi^{\*}(\phi) from ΦC​(x0)\Phi\_{C(x\_{0})} to ΦC​(x0)\Phi\_{C(x\_{0})} is continuous for the norm of C​(𝒮)C(\mathcal{S}).
The set ΦC​(x0)\Phi\_{C(x\_{0})} is compact in
C​(𝒮)C(\mathcal{S}) and also trivially convex.
With the choice 𝔹:=C​(𝒮)\mathbb{B}:=C(\mathcal{S}) and H=ΦC​(x0)H=\Phi\_{C(x\_{0})},
Theorem [4.9](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem9 "Theorem 4.9. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below gives a fixed point, i.e. some ϕ†∈ΦC​(x0)\phi^{\dagger}\in\Phi\_{C(x\_{0})} such that ϕ†=ψ∗​(ϕ†).\phi^{\dagger}=\psi^{\*}(\phi^{\dagger}).
This implies that,

|  |  |  |
| --- | --- | --- |
|  | u​(x0,ϕ†)=supψ∈Φ𝔼​[U​(WT​(x0,ψ),B​(ϕ†))]=𝔼​[U​(WT​(x0,ϕ†),B​(ϕ†))],u(x\_{0},\phi^{\dagger})=\sup\_{\psi\in\Phi}\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\psi),B(\phi^{\dagger})\bigr)\bigr]=\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\phi^{\dagger}),B(\phi^{\dagger})\bigr)\bigr], |  |

and ϕ†\phi^{\dagger} is by definition a personal equilibrium.

We now prove the existence of a preferred equilibrium.
It is convenient to introduce the notation, for ϕ,ψ∈Φ\phi,\psi\in\Phi,

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(ϕ,ψ):=𝔼​[U​(WT​(x0,ϕ),B​(ψ))].\mathcal{U}(\phi,\psi):=\mathbb{E}\bigl[U\bigl(W\_{T}(x\_{0},\phi),B(\psi)\bigr)\bigr]. |  |

Now let ϕ†​(n)∈Φ†\phi^{\dagger}(n)\in\Phi^{\dagger} be a sequence such that

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(ϕ†​(n),ϕ†​(n))→supϕ∈Φ†𝒰​(ϕ,ϕ),n→∞.\mathcal{U}\big(\phi^{\dagger}(n),\phi^{\dagger}(n)\big)\to\sup\_{\phi\in\Phi^{\dagger}}\mathcal{U}(\phi,\phi),\ n\to\infty. |  |

By compactness of ΦC​(x0)\Phi\_{C(x\_{0})}, there is a subsequence (still denoted by nn)
and ϕ♯∈ΦC​(x0)\phi^{\sharp}\in\Phi\_{C(x\_{0})} such that ϕ†​(n)→ϕ♯\phi^{\dagger}(n)\to\phi^{\sharp} in the topology of C​(𝒮)C(\mathcal{S}).
In particular, an estimate like ([42](https://arxiv.org/html/2512.08348v1#S3.E42 "In 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) shows that for all ω∈Ω\omega\in\Omega, B​(ϕ†​(n))​(ω)→B​(ϕ♯)​(ω)B(\phi^{\dagger}(n))(\omega)\to B(\phi^{\sharp})(\omega) and also

|  |  |  |
| --- | --- | --- |
|  | U​(WT​(x0,ϕ†​(n))​(ω),B​(ϕ†​(n))​(ω))→U​(WT​(x0,ϕ♯)​(ω),B​(ϕ♯)​(ω)).U\Bigl(W\_{T}\big(x\_{0},\phi^{\dagger}(n)\big)(\omega),B\big(\phi^{\dagger}(n)\big)(\omega)\Bigr)\to U\bigl(W\_{T}(x\_{0},\phi^{\sharp})(\omega),B(\phi^{\sharp})(\omega)\bigr). |  |

Dominated convergence implies 𝒰​(ϕ†​(n),ϕ†​(n))→𝒰​(ϕ♯,ϕ♯)\mathcal{U}(\phi^{\dagger}(n),\phi^{\dagger}(n))\to\mathcal{U}(\phi^{\sharp},\phi^{\sharp}) and

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(ϕ♯,ϕ♯)=supϕ∈Φ†𝒰​(ϕ,ϕ).\mathcal{U}(\phi^{\sharp},\phi^{\sharp})=\sup\_{\phi\in\Phi^{\dagger}}\mathcal{U}(\phi,\phi). |  |

It remains to show that ϕ♯\phi^{\sharp} itself is a personal equilibrium, i.e. u​(x0,ϕ♯)=𝒰​(ϕ♯,ϕ♯)u(x\_{0},\phi^{\sharp})=\mathcal{U}(\phi^{\sharp},\phi^{\sharp}).
By Proposition [3.4](https://arxiv.org/html/2512.08348v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2 Dynamic programming ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), there is an optimizer ψ∗=ψ∗​(ϕ♯)∈ΦC​(x0)\psi^{\*}=\psi^{\*}(\phi^{\sharp})\in\Phi\_{C(x\_{0})} such that

|  |  |  |
| --- | --- | --- |
|  | u​(x0,ϕ♯)=𝔼​[U​(WT​(x0,ψ∗),B​(ϕ♯))]=𝒰​(ψ∗,ϕ♯).u(x\_{0},\phi^{\sharp})=\mathbb{E}\bigl[U(W\_{T}\bigl(x\_{0},\psi^{\*}),B(\phi^{\sharp})\bigr)\bigr]=\mathcal{U}(\psi^{\*},\phi^{\sharp}). |  |

(At this point, we do not know yet that ψ∗=ϕ♯\psi^{\*}=\phi^{\sharp}.)
Since ϕ†​(n)\phi^{\dagger}(n) was
a personal equilibrium, for all nn,

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(ϕ†​(n),ϕ†​(n))≥𝒰​(ψ∗,ϕ†​(n)).\mathcal{U}\big(\phi^{\dagger}(n),\phi^{\dagger}(n)\big)\geq\mathcal{U}\big(\psi^{\*},\phi^{\dagger}(n)\big). |  |

Passing to the limit (again by dominated convergence),

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(ϕ♯,ϕ♯)≥𝒰​(ψ∗,ϕ♯)=u​(x0,ϕ♯)≥𝒰​(ψ,ϕ♯)\mathcal{U}(\phi^{\sharp},\phi^{\sharp})\geq\mathcal{U}(\psi^{\*},\phi^{\sharp})=u(x\_{0},\phi^{\sharp})\geq\mathcal{U}(\psi,\phi^{\sharp}) |  |

for all ψ∈Φ\psi\in\Phi. Choosing ψ=ϕ♯\psi=\phi^{\sharp}, we have equality,
so ϕ♯\phi^{\sharp} is indeed a personal equilibrium, and we may conclude.
We remark that, by uniqueness of the optimizer, necessarily ϕ♯=ψ∗\phi^{\sharp}=\psi^{\*}.
∎

## 4 Auxiliary results

###### Proposition 4.1.

Let Kt⊂ℝt×mK\_{t}\subset\mathbb{R}^{t\times m} be a non-empty compact set. Let Cf>0C\_{f}>0 and let χ∈(0,1]\chi\in(0,1].
Let ft:Kt→ℝf\_{t}:K\_{t}\to\mathbb{R} such that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |ft​(et)−ft​(e¯t)|\displaystyle|f\_{t}(e^{t})-f\_{t}(\bar{e}^{t})| | ≤\displaystyle\leq | Cf​|et−e¯t|χ,∀et,e¯t∈Kt,\displaystyle C\_{f}|e^{t}-\bar{e}^{t}|^{\chi},\qquad\forall e^{t},\bar{e}^{t}\in K\_{t}, |  | (48) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |ft​(et)|\displaystyle|f\_{t}(e^{t})| | ≤\displaystyle\leq | Cf∀et∈Kt.\displaystyle C\_{f}\qquad\forall e^{t}\in K\_{t}. |  | (49) |

Define Ft,gt:ℝt×m→ℝF\_{t},g\_{t}:\mathbb{R}^{t\times m}\to\mathbb{R} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ft​(et)\displaystyle F\_{t}(e^{t}) | :=\displaystyle:= | infe¯t∈Kt(ft​(e¯t)+Cf​|et−e¯t|χ),∀et∈ℝt×m.\displaystyle\inf\_{\bar{e}^{t}\in K\_{t}}\bigl(f\_{t}(\bar{e}^{t})+C\_{f}\,|e^{t}-\bar{e}^{t}|^{\chi}\bigr),\qquad\forall e^{t}\in\mathbb{R}^{t\times m}. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | gt​(et)\displaystyle g\_{t}(e^{t}) | :=\displaystyle:= | {Ft​(et),|et|≤R,Ft​(πR​(et)),|et|>R,\displaystyle\begin{cases}F\_{t}(e^{t}),&|e^{t}|\leq R,\\[5.69054pt] F\_{t}(\pi\_{R}(e^{t})),&|e^{t}|>R,\end{cases} |  |

where R>0R>0 is such that Kt⊂B​(0,R)K\_{t}\subset B(0,R), and πR​(et)\pi\_{R}(e^{t}) denotes the projection of ete^{t} onto the
closed ball of ℝt×m\mathbb{R}^{t\times m} of centre 0 and radius RR, B​(0,R)B(0,R). Then, gt|Kt=ftg\_{t}|\_{K\_{t}}=f\_{t} and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |gt​(et)−gt​(e¯t)|\displaystyle|g\_{t}(e^{t})-g\_{t}(\bar{e}^{t})| | ≤\displaystyle\leq | Cf​|et−e¯t|χ,∀et,e¯t∈ℝt×m\displaystyle C\_{f}\,|e^{t}-\bar{e}^{t}|^{\chi},\qquad\forall e^{t},\bar{e}^{t}\in\mathbb{R}^{t\times m} |  | (50) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |gt​(et)|\displaystyle|g\_{t}(e^{t})| | ≤\displaystyle\leq | Cf​(1+(2​R)χ),∀et∈Kt.\displaystyle C\_{f}(1+(2R)^{\chi}),\qquad\forall e^{t}\in K\_{t}. |  | (51) |

If Kt=B​(0,R)K\_{t}=B(0,R), then ([51](https://arxiv.org/html/2512.08348v1#S4.E51 "In Proposition 4.1. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds with CfC\_{f} instead of Cf​(1+(2​R)χ)C\_{f}(1+(2R)^{\chi}).

###### Proof.

We first prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Ft​(et)−Ft​(e¯t)|≤Cf​|et−e¯t|χ,∀et,e¯t∈ℝt×m.\displaystyle|F\_{t}(e^{t})-F\_{t}(\bar{e}^{t})|\leq C\_{f}\,|e^{t}-\bar{e}^{t}|^{\chi},\qquad\forall e^{t},\bar{e}^{t}\in\mathbb{R}^{t\times m}. |  | (52) |

Fix et∈ℝt×me^{t}\in\mathbb{R}^{t\times m}. Since ftf\_{t} satisfies ([48](https://arxiv.org/html/2512.08348v1#S4.E48 "In Proposition 4.1. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) for all e¯t,z¯t∈Kt\bar{e}^{t},\bar{z}^{t}\in K\_{t}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ft​(et)\displaystyle F\_{t}(e^{t}) | ≤\displaystyle\leq | ft​(e¯t)+Cf​|et−e¯t|χ\displaystyle f\_{t}(\bar{e}^{t})+C\_{f}\,|e^{t}-\bar{e}^{t}|^{\chi} |  |
|  |  | ≤\displaystyle\leq | ft​(z¯t)+Cf​|e¯t−z¯t|χ+Cf​|et−e¯t|χ.\displaystyle f\_{t}(\bar{z}^{t})+C\_{f}|\bar{e}^{t}-\bar{z}^{t}|^{\chi}+C\_{f}|e^{t}-\bar{e}^{t}|^{\chi}. |  |

So, taking the infimum over z¯t∈Kt\bar{z}^{t}\in K\_{t}, we get that Ft​(et)≤Ft​(e¯t)+Cf​|et−e¯t|χF\_{t}(e^{t})\leq F\_{t}(\bar{e}^{t})+C\_{f}\,|e^{t}-\bar{e}^{t}|^{\chi}. Then, ([52](https://arxiv.org/html/2512.08348v1#S4.E52 "In 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) follows by symmetry.
  
Extension property.
  
If et∈Kt⊂B​(0,R)e^{t}\in K\_{t}\subset B(0,R), then gt​(et)=Ft​(et)=ft​(et)g\_{t}(e^{t})=F\_{t}(e^{t})=f\_{t}(e^{t}).
Thus gt|Kt=ftg\_{t}|\_{K\_{t}}=f\_{t}.
  
Hölder property.
  
Case 1: et,e¯t∈B​(0,R)e^{t},\bar{e}^{t}\in B(0,R).
Then, ([52](https://arxiv.org/html/2512.08348v1#S4.E52 "In 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) shows that

|  |  |  |
| --- | --- | --- |
|  | |gt​(et)−gt​(e¯t)|=|Ft​(et)−Ft​(e¯t)|≤Cf​|et−e¯t|χ.|g\_{t}(e^{t})-g\_{t}(\bar{e}^{t})|=|F\_{t}(e^{t})-F\_{t}(\bar{e}^{t})|\leq C\_{f}|e^{t}-\bar{e}^{t}|^{\chi}. |  |

Case 2: et,e¯t∉B​(0,R)e^{t},\bar{e}^{t}\notin B(0,R).
Since the projection πR\pi\_{R} is 11-Lipschitz (see [[1](https://arxiv.org/html/2512.08348v1#bib.bib1), Lemma 6.54]), ([52](https://arxiv.org/html/2512.08348v1#S4.E52 "In 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) again shows that

|  |  |  |
| --- | --- | --- |
|  | |gt​(et)−gt​(e¯t)|=|Ft​(πR​(et))−Ft​(πR​(e¯t))|≤Cf​|πR​(et)−πR​(e¯t)|χ≤Cf​|et−e¯t|χ.|g\_{t}(e^{t})-g\_{t}(\bar{e}^{t})|=|F\_{t}(\pi\_{R}(e^{t}))-F\_{t}(\pi\_{R}(\bar{e}^{t}))|\leq C\_{f}|\pi\_{R}(e^{t})-\pi\_{R}(\bar{e}^{t})|^{\chi}\leq C\_{f}|e^{t}-\bar{e}^{t}|^{\chi}. |  |

Case 3: one point inside B​(0,R)B(0,R), one outside.
Without loss, assume |et|≤R<|e¯t||e^{t}|\leq R<|\bar{e}^{t}|.
Let e¯t=(1−s0)​et+s0​e¯t\underline{e}^{t}=(1-s\_{0})e^{t}+s\_{0}\bar{e}^{t} be the intersection of {(1−s)​et+s​e¯t:s∈[0,1]}\{(1-s)e^{t}+s\bar{e}^{t}:s\in[0,1]\} with the sphere ∂B​(0,R)\partial B(0,R). Note that πR​(e¯t)=e¯t\pi\_{R}(\underline{e}^{t})=\underline{e}^{t}.
Using ([52](https://arxiv.org/html/2512.08348v1#S4.E52 "In 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) again, we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Ft​(et)−Ft​(e¯t)|\displaystyle|F\_{t}(e^{t})-F\_{t}(\underline{e}^{t})| | ≤\displaystyle\leq | Cf​|et−e¯t|χ=s0​Cf​|et−e¯t|χ\displaystyle C\_{f}|e^{t}-\underline{e}^{t}|^{\chi}=s\_{0}C\_{f}|e^{t}-\bar{e}^{t}|^{\chi} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Ft​(e¯t)−Ft​(πR​(e¯t))|\displaystyle|F\_{t}(\underline{e}^{t})-F\_{t}\big(\pi\_{R}(\bar{e}^{t})\big)| | =\displaystyle= | |Ft​(πR​(e¯t))−Ft​(πR​(e¯t))|≤Cf​|πR​(e¯t)−πR​(e¯t)|χ\displaystyle|F\_{t}\big(\pi\_{R}(\underline{e}^{t})\big)-F\_{t}\big(\pi\_{R}(\bar{e}^{t})\big)|\leq C\_{f}|\pi\_{R}(\underline{e}^{t})-\pi\_{R}(\bar{e}^{t})|^{\chi} |  |
|  |  | ≤\displaystyle\leq | Cf​|e¯t−e¯t|χ=(1−s0)​Cf​|et−e¯t|χ\displaystyle C\_{f}|\underline{e}^{t}-\bar{e}^{t}|^{\chi}=(1-s\_{0})C\_{f}|e^{t}-\bar{e}^{t}|^{\chi} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |gt​(et)−gt​(e¯t)|\displaystyle|g\_{t}(e^{t})-g\_{t}(\bar{e}^{t})| | =\displaystyle= | |Ft​(et)−Ft​(πR​(e¯t))|\displaystyle|F\_{t}(e^{t})-F\_{t}\big(\pi\_{R}(\bar{e}^{t})\big)| |  |
|  |  | ≤\displaystyle\leq | |Ft​(et)−Ft​(e¯t)|+|Ft​(e¯t)−Ft​(πR​(e¯t))|≤Cf​|et−e¯t|χ.\displaystyle|F\_{t}(e^{t})-F\_{t}(\underline{e}^{t})|+|F\_{t}(\underline{e}^{t})-F\_{t}\big(\pi\_{R}(\bar{e}^{t})\big)|\leq C\_{f}|e^{t}-\bar{e}^{t}|^{\chi}. |  |

Uniform boundedness.
  
If et∈B​(0,R)e\_{t}\in B(0,R), then

|  |  |  |
| --- | --- | --- |
|  | gt​(et)=Ft​(et)≤Cf+Cf​infe¯t∈Kt|et−e¯t|χ≤Cf​(1+(2​R)χ),g\_{t}(e^{t})=F\_{t}(e^{t})\leq C\_{f}+C\_{f}\inf\_{\bar{e}^{t}\in K\_{t}}|e^{t}-\bar{e}^{t}|^{\chi}\leq C\_{f}(1+(2R)^{\chi}), |  |

as Kt⊂B​(0,R)K\_{t}\subset B(0,R). Note that if Kt=B​(0,R)K\_{t}=B(0,R), infe¯t∈Kt|et−e¯t|χ=0\inf\_{\bar{e}^{t}\in K\_{t}}|e^{t}-\bar{e}^{t}|^{\chi}=0.
If et∉B​(0,R)e\_{t}\notin B(0,R), then gt​(et)=Ft​(πR​(et))g\_{t}(e^{t})=F\_{t}(\pi\_{R}(e^{t})), so the preceding inequality applies as πR​(et)∈B​(0,R)\pi\_{R}(e^{t})\in B(0,R).
∎

###### Lemma 4.2.

The model of Example [2.6](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem6 "Example 2.6. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") satisfies Assumptions [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") and [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

###### Proof.

Let us fix Cε≥1C\_{\varepsilon}\geq 1 such that |εt+1|≤Cε|\varepsilon\_{t+1}|\leq C\_{\varepsilon}.
Let ft​(et):=μt​(et−1)+σt​(et−1)​etf\_{t}(e^{t}):=\mu\_{t}(e^{t-1})+\sigma\_{t}(e^{t-1})e\_{t}. Trivially, |ft|≤C+C​Cε|f\_{t}|\leq C+CC\_{\varepsilon} on [−Cε,Cε]t[-C\_{\varepsilon},C\_{\varepsilon}]^{t}.
For et,e¯t∈[−Cε,Cε]te^{t},\bar{e}^{t}\in[-C\_{\varepsilon},C\_{\varepsilon}]^{t},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |ft​(et)−ft​(e¯t)|\displaystyle\hskip-28.45274pt|f\_{t}(e^{t})-f\_{t}(\bar{e}^{t})| |  |
|  |  | ≤\displaystyle\leq | |μt​(et−1)−μt​(e¯t−1)|+|σt​(et−1)−σt​(e¯t−1)|​|et|+|et−e¯t|​|σt​(e¯t−1)|\displaystyle|\mu\_{t}(e^{t-1})-\mu\_{t}(\bar{e}^{t-1})|+|\sigma\_{t}(e^{t-1})-\sigma\_{t}(\bar{e}^{t-1})||e\_{t}|+|e\_{t}-\bar{e}\_{t}||\sigma\_{t}(\bar{e}^{t-1})| |  |
|  |  | ≤\displaystyle\leq | C​|et−1−e¯t−1|δ+C​|et−1−e¯t−1|δ​Cε+C​|et−e¯t|\displaystyle C|e^{t-1}-\bar{e}^{t-1}|^{\delta}+C|e^{t-1}-\bar{e}^{t-1}|^{\delta}C\_{\varepsilon}+C|e\_{t}-\bar{e}\_{t}| |  |
|  |  | ≤\displaystyle\leq | [3​(C+C​Cε)+2​(C+C​Cε)]​|et−e¯t|δ=5​C​(1+Cε)​|et−e¯t|δ,\displaystyle[3(C+CC\_{\varepsilon})+2(C+CC\_{\varepsilon})]|e^{t}-\bar{e}^{t}|^{\delta}=5C(1+C\_{\varepsilon})|e^{t}-\bar{e}^{t}|^{\delta}, |  |

using Lemma [4.3](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") below. Now, define gtg\_{t} as in Proposition [4.1](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") with R=T​CεR=\sqrt{T}C\_{\varepsilon}. Clearly,
Δ​St=gt​(ε1,…,εt)\Delta S\_{t}=g\_{t}(\varepsilon\_{1},\ldots,\varepsilon\_{t}) and Assumption [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") holds for gtg\_{t}. It remains to check Assumption [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").
By our hypothesis on εt+1\varepsilon\_{t+1},

|  |  |  |
| --- | --- | --- |
|  | ℙ​[μt+1​(et)+σt+1​(et)​εt+1≤−β]≥ℙ​[εt+1≤−C−βc]≥β\displaystyle\mathbb{P}[\mu\_{t+1}(e^{t})+\sigma\_{t+1}(e^{t})\varepsilon\_{t+1}\leq-\beta]\geq\mathbb{P}\left[\varepsilon\_{t+1}\leq\frac{-C-\beta}{c}\right]\geq\beta |  |
|  |  |  |
| --- | --- | --- |
|  | ℙ​[μt+1​(et)+σt+1​(et)​εt+1≥β]≥ℙ​[εt+1≥C+βc]≥β\displaystyle\mathbb{P}[\mu\_{t+1}(e^{t})+\sigma\_{t+1}(e^{t})\varepsilon\_{t+1}\geq\beta]\geq\mathbb{P}\left[\varepsilon\_{t+1}\geq\frac{C+\beta}{c}\right]\geq\beta |  |

and we choose α=β\alpha=\beta.

∎

Simple observations are noted next.

###### Proof of Lemma [2.7](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem7 "Lemma 2.7. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).").

There is a
bijection ζ:ℝ→ℝT×m\zeta:\mathbb{R}\to\mathbb{R}^{T\times m} such that
ζ,ζ−1\zeta,\zeta^{-1} are Borel measurable; see [[3](https://arxiv.org/html/2512.08348v1#bib.bib3), Corollary 7.16.1, p.122].

Consider the probability κ​(A):=ℙ​[(ε1,…,εT)∈ζ​(A)]\kappa(A):=\mathbb{P}[(\varepsilon\_{1},\ldots,\varepsilon\_{T})\in\zeta(A)],
defined for A∈ℬ​(ℝ)A\in\mathcal{B}(\mathbb{R}). The corresponding cumulative distribution function is

|  |  |  |
| --- | --- | --- |
|  | Fκ​(x):=κ​[(−∞,x]],x∈ℝ,F\_{\kappa}(x):=\kappa[(-\infty,x]],\ x\in\mathbb{R}, |  |

and its pseudo-inverse is

|  |  |  |
| --- | --- | --- |
|  | Fκ−​(u):=inf{x:Fκ​(x)≥u},u∈(0,1).F\_{\kappa}^{-}(u):=\inf\{x:F\_{\kappa}(x)\geq u\},\ u\in(0,1). |  |

It is well-known that the random variable Fκ−​(ε^)F\_{\kappa}^{-}(\hat{\varepsilon}) has law κ\kappa under ℙ\mathbb{P}.
Define Υ​(u):=ζ​(Fκ−​(u))\Upsilon(u):=\zeta(F\_{\kappa}^{-}(u)). By the definition of κ\kappa, Υ​(ε^)\Upsilon(\hat{\varepsilon})
has the same law as (ε1,…,εT)(\varepsilon\_{1},\ldots,\varepsilon\_{T}).
∎

###### Lemma 4.3.

Let n,N,M∈ℕn,N,M\in\mathbb{N} and 0≤θ1≤θ2≤…≤θn0\leq\theta\_{1}\leq\theta\_{2}\leq\ldots\leq\theta\_{n}.
Let f:ℝN→ℝMf:\mathbb{R}^{N}\to\mathbb{R}^{M} be a function with |f|≤C¯|f|\leq\bar{C}.
If, for all
e,e¯∈ℝNe,\bar{e}\in\mathbb{R}^{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |f​(e)−f​(e¯)|≤C​∑i=1n|e−e¯|θi|f(e)-f(\bar{e})|\leq C\sum\_{i=1}^{n}|e-\bar{e}|^{\theta\_{i}} |  | (53) |

for some constant C>0C>0, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |f​(e)−f​(e¯)|≤[n​C+2​C¯]​|e−e¯|θ1,e,e¯∈ℝN.|f(e)-f(\bar{e})|\leq[nC+2\bar{C}]|e-\bar{e}|^{\theta\_{1}},\ e,\bar{e}\in\mathbb{R}^{N}. |  | (54) |

###### Proof.

If |e−e¯|<1|e-\bar{e}|<1 then ([53](https://arxiv.org/html/2512.08348v1#S4.E53 "In Lemma 4.3. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) implies |f​(e)−f​(e¯)|≤n​C​|e−e¯|θ1.|f(e)-f(\bar{e})|\leq nC|e-\bar{e}|^{\theta\_{1}}.
In the opposite case,

|  |  |  |
| --- | --- | --- |
|  | |f​(e)−f​(e¯)|≤2​C¯≤2​C¯​|e−e¯|θ1,\displaystyle|f(e)-f(\bar{e})|\leq 2\bar{C}\leq 2\bar{C}|e-\bar{e}|^{\theta\_{1}}, |  |

showing our claim.
∎

###### Lemma 4.4.

Let F:ℝ→ℝF:\mathbb{R}\to\mathbb{R} and K:ℝ→(0,+∞)K:\mathbb{R}\to(0,+\infty) be two continuous functions. Define

|  |  |  |
| --- | --- | --- |
|  | f​(x):=supy∈[x−K​(x),x+K​(x)]F​(y).f(x):=\sup\_{y\in[x-K(x),x+K(x)]}F(y). |  |

Then ff is continuous on ℝ\mathbb{R}.

###### Proof.

Fix x∈ℝx\in\mathbb{R}. We perform the change of variable
t:=(y−x)/K​(x),t:={(y-x)}/{K(x)},
and rewrite:

|  |  |  |
| --- | --- | --- |
|  | f​(x)=supt∈[−1,1]F​(x+K​(x)​t).f(x)=\sup\_{t\in[-1,1]}F(x+K(x)t). |  |

Now define the auxiliary function on ℝ×[−1,1]\mathbb{R}\times[-1,1] by φ​(x,t):=F​(x+K​(x)​t).\varphi(x,t):=F(x+K(x)t).
Since FF and KK are continuous, so is φ\varphi, and we can apply the Maximum Theorem ([[1](https://arxiv.org/html/2512.08348v1#bib.bib1), Theorem 17.31]) on the
compact [−1,1][-1,1]: ff is continous.
∎

The following measure-theoretical result was needed in our argument for dynamic programming above.

###### Lemma 4.5.

Let X1∈ℝd1X\_{1}\in\mathbb{R}^{d\_{1}}, X2∈ℝd2X\_{2}\in\mathbb{R}^{d\_{2}} be independent random variables,
Ξ:ℝd1×ℝd2→ℝ\Xi:\mathbb{R}^{d\_{1}}\times\mathbb{R}^{d\_{2}}\to\mathbb{R} be Borel
measurable and bounded from above. Define

|  |  |  |
| --- | --- | --- |
|  | Ξ♯​(x2):=𝔼​[Ξ​(X1,x2)],x2∈ℝd2.\Xi^{\sharp}(x\_{2}):=\mathbb{E}[\Xi(X\_{1},x\_{2})],\ x\_{2}\in\mathbb{R}^{d\_{2}}. |  |

Then Ξ♯​(X2)\Xi^{\sharp}(X\_{2}) is a version of 𝔼​[Ξ​(X1,X2)|σ​(X2)]\mathbb{E}[\Xi(X\_{1},X\_{2})|\sigma(X\_{2})]. We may write

|  |  |  |
| --- | --- | --- |
|  | Ξ♯​(X2)=𝔼​[Ξ​(X1,x2)]|x2=X2.\Xi^{\sharp}(X\_{2})=\mathbb{E}[\Xi(X\_{1},x\_{2})]|\_{x\_{2}=X\_{2}}. |  |

###### Proof.

By standard measure-theoretic arguments, we can reduce that statement to the case where Ξ​(x1,x2)=1A1​(x1)​1A2​(x2)\Xi(x\_{1},x\_{2})=1\_{A\_{1}}(x\_{1})1\_{A\_{2}}(x\_{2})
with Borel sets A1,A2A\_{1},A\_{2}. By independence, we get that ℙ\mathbb{P}-a.s.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Ξ​(X1,X2)|σ​(X2)]\displaystyle\mathbb{E}[\Xi(X\_{1},X\_{2})|\sigma(X\_{2})] | =\displaystyle= | 1A2​(X2)​𝔼​[1A1​(X1)|σ​(X2)]\displaystyle 1\_{A\_{2}}(X\_{2})\mathbb{E}[1\_{A\_{1}}(X\_{1})|\sigma(X\_{2})] |  |
|  |  | =\displaystyle= | 1A2​(X2)​𝔼​[1A1​(X1)]=Ξ♯​(X2),\displaystyle 1\_{A\_{2}}(X\_{2})\mathbb{E}[1\_{A\_{1}}(X\_{1})]=\Xi^{\sharp}(X\_{2}), |  |

finishing the proof.
∎

###### Lemma 4.6.

Let k≥1k\geq 1. Assume that fn→ff\_{n}\to f, n→∞n\to\infty μ\mu-a.s. where μ\mu is a probability measure on ℬ​(ℝk)\mathcal{B}(\mathbb{R}^{k}).
Then, there exists a dense subset DD of
supp​(μ)\mathrm{supp}(\mu), where fn​(x)→f​(x)f\_{n}(x)\to f(x), n→∞n\to\infty, for all x∈Dx\in D.

###### Proof.

Let A∈ℬ​(ℝk)A\in\mathcal{B}(\mathbb{R}^{k}) such that for all x∈Ax\in A, fn​(x)→f​(x)f\_{n}(x)\to f(x), n→∞n\to\infty and μ​[A]=1\mu[A]=1.
Notice that μ​[supp​(μ)]=1\mu[\mathrm{supp}(\mu)]=1 hence D:=A∩supp​(μ)D:=A\cap\mathrm{supp}(\mu) and its closure D¯\bar{D} also
satisfy μ​[D]=μ​[D¯]=1\mu[D]=\mu[\bar{D}]=1. Then D¯⊃supp​(μ)\bar{D}\supset\mathrm{supp}(\mu) since the latter
is the smallest closed set of full μ\mu-measure, see ([40](https://arxiv.org/html/2512.08348v1#S3.E40 "In 3.3 Fixed point theorem, and remaining proofs ‣ 3 Proofs ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). This means precisely that DD is dense in supp​(μ)\mathrm{supp}(\mu).
∎

We recall the main result of [[5](https://arxiv.org/html/2512.08348v1#bib.bib5)] in a form that is convenient for the present setting.

###### Theorem 4.7.

Let Assumptions [2.1](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.2](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") be in vigour.
For all n∈ℕ¯:=ℕ∪{∞}n\in\bar{\mathbb{N}}:=\mathbb{N}\cup\{\infty\}, let the random utilities
𝔘n:Ω×ℝ→ℝ\mathfrak{U}\_{n}:\Omega\times\mathbb{R}\to\mathbb{R} satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∞​<ess.infn∈ℕ¯𝔘n​(⋅,∞)​<+∞​ a.s.ess.supn∈ℕ¯|​𝔘n​(⋅,x)|<∞​ a.s. ​∀x∈ℝ.\displaystyle-\infty<\mathrm{ess.}\inf\_{n\in\bar{\mathbb{N}}}\mathfrak{U}\_{n}(\cdot,\infty)<+\infty\mbox{ a.s.}\quad\mathrm{ess.}\sup\_{n\in\bar{\mathbb{N}}}|\mathfrak{U}\_{n}(\cdot,x)|<\infty\mbox{ a.s. }\forall x\in\mathbb{R}. |  | (55) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→∞supn∈ℕ¯,ω∈Ω[𝔘n​(ω,∞)−𝔘n​(ω,x)]=0\displaystyle\lim\_{x\to\infty}\sup\_{n\in\bar{\mathbb{N}},\omega\in\Omega}[\mathfrak{U}\_{n}(\omega,\infty)-\mathfrak{U}\_{n}(\omega,x)]=0 |  | (56) |

Assume that each 𝔘n\mathfrak{U}\_{n} is (almost surely) strictly concave and increasing, continuously differentiable in xx,
with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ess.infn∈ℕ¯𝔘n′​(⋅,0)>0​ a.s.\displaystyle\mathrm{ess.}\inf\_{n\in\bar{\mathbb{N}}}\mathfrak{U}\_{n}^{\prime}(\cdot,0)>0\mbox{ a.s.} |  | (57) |

Furthermore, assume that for each x∈ℝx\in\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔘n​(⋅,x)→𝔘∞​(⋅,x)​ a.s.,​n→∞.\displaystyle\mathfrak{U}\_{n}(\cdot,x)\to\mathfrak{U}\_{\infty}(\cdot,x)\mbox{ a.s.,}n\to\infty. |  | (58) |

Let x0∈ℝ.x\_{0}\in\mathbb{R}. Then, for all n∈ℕ¯n\in\bar{\mathbb{N}}, there are (a.s.) unique optimizers Ψ​(n):=Ψ​(n)​(⋅,x0)\Psi(n):=\Psi(n)(\cdot,x\_{0}), Ψ​(n)∈Φ\Psi(n)\in\Phi satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝔘n​(⋅,WT​(x0,Ψ​(n)))]=supϕ∈Φ𝔼​[𝔘n​(⋅,WT​(x0,ϕ))].\displaystyle\mathbb{E}\Bigl[\mathfrak{U}\_{n}\Bigl(\cdot,W\_{T}\bigl(x\_{0},\Psi(n)\bigr)\Bigr)\Bigr]={}\sup\_{\phi\in\Phi}\mathbb{E}\Bigl[\mathfrak{U}\_{n}\bigl(\cdot,W\_{T}(x\_{0},\phi)\bigr)\Bigr]. |  | (59) |

and for all 1≤t≤T1\leq t\leq T

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(n)t​(⋅,x0)→Ψ​(∞)t​(⋅,x0)​ a.s. ,n→∞.\Psi(n)\_{t}(\cdot,x\_{0})\to\Psi({\infty})\_{t}(\cdot,x\_{0})\mbox{ a.s. },n\to\infty. |  | (60) |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝔼​[𝔘n​(⋅,WT​(x0,Ψ​(n)))]=𝔼​[𝔘∞​(⋅,WT​(x0,Ψ​(∞)))],\lim\_{n\to\infty}\mathbb{E}\Bigl[\mathfrak{U}\_{n}\Bigl(\cdot,W\_{T}\bigl(x\_{0},\Psi(n)\bigr)\Bigr)\Bigr]=\mathbb{E}\Bigl[\mathfrak{U}\_{{\infty}}\Bigl(\cdot,W\_{T}\bigl(x\_{0},\Psi({\infty})\bigr)\Bigr)\Bigr], |  |

uniformly on compact sets.

###### Proof.

Hypothesis (R) of [[5](https://arxiv.org/html/2512.08348v1#bib.bib5)] is
automatic from Assumption [2.4](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."). Indeed, let μ\mu denote the law of ft​(et−1,εt)f\_{t}(e^{t-1},\varepsilon\_{t}) under
ℙ\mathbb{P}.
There exists x+∈Supp​(μ)x\_{+}\in\mathrm{Supp}(\mu) with x+≥αx\_{+}\geq\alpha. Else
[α,+∞)[\alpha,+\infty) would be disjoint from the support and therefore
μ​[[α,+∞)]=0,\mu\big[[\alpha,+\infty)\big]=0,
contradicting α>0\alpha>0 in ([3](https://arxiv.org/html/2512.08348v1#S2.E3 "In Assumption 2.4. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). Similarly there exists x−∈Supp​(μ)x\_{-}\in\mathrm{Supp}(\mu) with x−≤−αx\_{-}\leq-\alpha.
As the support contains at least two distinct points,
the affine hull
is the whole real line.

By Remark [2.5](https://arxiv.org/html/2512.08348v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2.1 Hypotheses on the financial market model ‣ 2 Model assumptions and results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."), Assumption 2.1 of [[5](https://arxiv.org/html/2512.08348v1#bib.bib5)] also holds.
Let Ω¯\bar{\Omega} be the full measure set where all the assumptions of Theorem [4.7](https://arxiv.org/html/2512.08348v1#S4.Thmtheorem7 "Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).") hold. Set for all ω∈Ω¯\omega\in\bar{\Omega},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ι​(ω)\displaystyle\iota(\omega) | :=\displaystyle:= | ess.infn∈ℕ¯𝔘n​(ω,∞)−1∈ℝ\displaystyle\mathrm{ess.}\inf\_{n\in\bar{\mathbb{N}}}\mathfrak{U}\_{n}(\omega,\infty)-1\in\mathbb{R} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔙n​(ω,x)\displaystyle\mathfrak{V}\_{n}(\omega,x) | :=\displaystyle:= | 𝔘n​(ω,x)−ι​(ω),x∈ℝ,n∈ℕ¯.\displaystyle\mathfrak{U}\_{n}(\omega,x)-\iota(\omega),\,x\in\mathbb{R},\;n\in\bar{\mathbb{N}}. |  |

Then, it is clear that ([59](https://arxiv.org/html/2512.08348v1#S4.E59 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) for 𝔘n\mathfrak{U}\_{n} and 𝔙n\mathfrak{V}\_{n} have the same optimizers.
Moreover, 𝔙n\mathfrak{V}\_{n} statisfies ([55](https://arxiv.org/html/2512.08348v1#S4.E55 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), ([56](https://arxiv.org/html/2512.08348v1#S4.E56 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), ([57](https://arxiv.org/html/2512.08348v1#S4.E57 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) and ([58](https://arxiv.org/html/2512.08348v1#S4.E58 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).
So, our conditions for 𝔙n\mathfrak{V}\_{n} also imply Assumption 2.2 and those
in Remark 2.5 of [[5](https://arxiv.org/html/2512.08348v1#bib.bib5)]. It remains to show that Assumption 2.3 of [[5](https://arxiv.org/html/2512.08348v1#bib.bib5)] is also true with,
say, γ=1/2\gamma=1/2, that is, there exists x~>0\tilde{x}>0, such that for all x≥x~,x\geq\tilde{x}, n∈ℕ¯n\in\bar{\mathbb{N}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔙n​(⋅,λ​x)≤λ1/2​𝔙n​(⋅,x)​ a.s. \mathfrak{V}\_{n}(\cdot,\lambda x)\leq\lambda^{1/2}\mathfrak{V}\_{n}(\cdot,x)\mbox{ a.s. } |  | (61) |

We remark that one could verify that assumption for arbitrary γ>0\gamma>0. ([61](https://arxiv.org/html/2512.08348v1#S4.E61 "In 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”)."))
is a condition on *asymptotic elasticity*, see Section 6 of [[13](https://arxiv.org/html/2512.08348v1#bib.bib13)] for
a detailed discussion of this notion.

Fix n∈ℕ¯n\in\bar{\mathbb{N}}. To show ([61](https://arxiv.org/html/2512.08348v1#S4.E61 "In 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")), notice first that for all y>0y>0, all ω∈Ω¯\omega\in\bar{\Omega},

|  |  |  |
| --- | --- | --- |
|  | y2​𝔙n′​(ω,y)≤∫y/2y𝔙n′​(ω,t)​𝑑t≤𝔙n​(ω,∞)−𝔙n​(ω,y/2).\displaystyle\frac{y}{2}\mathfrak{V}\_{n}^{\prime}(\omega,y)\leq\int\_{y/2}^{y}\mathfrak{V}\_{n}^{\prime}(\omega,t)\,dt\leq\mathfrak{V}\_{n}(\omega,\infty)-\mathfrak{V}\_{n}(\omega,y/2). |  |

Choose y~\tilde{y} so large that
supn∈ℕ¯,ω∈Ω[𝔙n​(ω,∞)−𝔙n​(ω,y~)]≤1/2\sup\_{n\in\bar{\mathbb{N}},\omega\in\Omega}[\mathfrak{V}\_{n}(\omega,\infty)-\mathfrak{V}\_{n}(\omega,\tilde{y})]\leq 1/2, this is
possible by ([56](https://arxiv.org/html/2512.08348v1#S4.E56 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). Then, since 𝔙n​(ω,∞)≥1\mathfrak{V}\_{n}(\omega,\infty)\geq 1, we have
𝔙n​(ω,y)≥1/2\mathfrak{V}\_{n}(\omega,y)\geq 1/2 for y≥y~y\geq\tilde{y}, so

|  |  |  |
| --- | --- | --- |
|  | 0≤y​𝔙n′​(ω,y)𝔙n​(ω,y)≤4​[𝔙n​(ω,∞)−𝔙n​(ω,y/2)]≤4​supn∈ℕ¯,ω∈Ω[𝔙n​(ω,∞)−𝔙n​(ω,y/2)].0\leq\frac{y\mathfrak{V}\_{n}^{\prime}(\omega,y)}{\mathfrak{V}\_{n}(\omega,y)}\leq 4[\mathfrak{V}\_{n}(\omega,\infty)-\mathfrak{V}\_{n}(\omega,y/2)]\leq 4\sup\_{n\in\bar{\mathbb{N}},\omega\in\Omega}[\mathfrak{V}\_{n}(\omega,\infty)-\mathfrak{V}\_{n}(\omega,y/2)]. |  |

Hence y​𝔙n′​(ω,y)𝔙n​(ω,y)\frac{y\mathfrak{V}\_{n}^{\prime}(\omega,y)}{\mathfrak{V}\_{n}(\omega,y)} tends to 0
as y→∞y\to\infty, uniformly in n∈ℕ¯n\in\bar{\mathbb{N}} and ω∈Ω\omega\in\Omega, by ([56](https://arxiv.org/html/2512.08348v1#S4.E56 "In Theorem 4.7. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")).
We obtain that there is y¯≥y~\bar{y}\geq\tilde{y}
such that for y≥y¯y\geq\bar{y}, n∈ℕ¯n\in\bar{\mathbb{N}}

|  |  |  |
| --- | --- | --- |
|  | y​𝔙n′​(ω,y)<12​𝔙n​(ω,y).y\mathfrak{V}\_{n}^{\prime}(\omega,y)<\frac{1}{2}\mathfrak{V}\_{n}(\omega,y). |  |

Now applying the argument of (i​i)⇒(i)(ii)\Rightarrow(i) in Lemma 6.3 of [[13](https://arxiv.org/html/2512.08348v1#bib.bib13)] with the choice γ=1/2\gamma=1/2,
it follows that for some x~≥y¯\tilde{x}\geq\bar{y}, ([61](https://arxiv.org/html/2512.08348v1#S4.E61 "In 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")) holds.
Now Theorem 2.1 and Remark 2.5 of [[5](https://arxiv.org/html/2512.08348v1#bib.bib5)] imply the statements of our theorem. ∎

An immediate corollary of the Ascoli theorem is noted next.

###### Proposition 4.8.

Let 𝒮\mathcal{S} be a compact subset in a Euclidean space ℝN\mathbb{R}^{N} with norm |⋅||\cdot|. Let Ψ⊂C​(𝒮)\Psi\subset C(\mathcal{S})
be such that,

|  |  |  |
| --- | --- | --- |
|  | supψ∈Ψ|ψ​(x)|<∞,x∈𝒮\sup\_{\psi\in\Psi}|\psi(x)|<\infty,\,x\in\mathcal{S} |  |

and, for some θ,A>0\theta,A>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supψ∈Ψ|ψ​(x)−ψ​(y)|≤A​|x−y|θ,x,y∈𝒮.\sup\_{\psi\in\Psi}|\psi(x)-\psi(y)|\leq A|x-y|^{\theta},\ x,y\in\mathcal{S}. |  | (62) |

Then Ψ\Psi is relatively compact in the Banach space C​(𝒮)C(\mathcal{S}).

###### Proof.

By Theorem A5 and its corollary in [[17](https://arxiv.org/html/2512.08348v1#bib.bib17)] (see also Theorem A4), we only need to check equicontinuity of the elements of Ψ\Psi, which is trivial from ([62](https://arxiv.org/html/2512.08348v1#S4.E62 "In Proposition 4.8. ‣ 4 Auxiliary results ‣ On the existence of personal equilibriaThe first author gratefully acknowledges the support of Université Paris-Saclay Springboard PIA Excellences, ANR 21-EXES-0003. The second author gratefully acknowledges the support of the National Research, Development and Innovation Office (NKFIH) through grants K 143529, KKP 137490 and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme “Artificial intelligence, large networks, data security: mathematical foundation and applications”).")). ∎

Finally, we recall the celebrated theorem of Schauder, see [[17](https://arxiv.org/html/2512.08348v1#bib.bib17), Theorem 5.28].

###### Theorem 4.9.

Let 𝔹\mathbb{B} be a Banach space,
H⊂𝔹H\subset\mathbb{B} a nonempty, compact, convex subset. If υ:H→H\upsilon:H\to H is a continuous mapping
then there is p∈Hp\in H with υ​(p)=p\upsilon(p)=p. □\square

## References

* [1]
   C. D. Aliprantis and K. C. Border.
  *Infinite Dimensional Analysis : A Hitchhiker’s Guide*
  3rd ed. Springer,Berlin, 2006.
* [2]
   D. E. Bell.
  Disappointment in Decision Making under Uncertainty.
  *Operations Research*, 33:1–27, 1985.
* [3]
   D. P. Bertsekas and S. E. Shreve.
  *Stochastic optimal control: the discrete time case.*
  Academic Press, New York, 1978.
* [4]
   L. Carassus and M. Rásonyi.
  Convergence of utility
  indifference prices to the superreplication price: the whole real line case.
  *Acta Applicandae Mathematicae*, 96, 119–135, 2007.
* [5]
   L. Carassus and M. Rásonyi.
  Optimal strategies and
  utility-based price converge when agents’ preferences do.
  *Mathematics of Operations Research*,
  32, 102–117, 2007.
* [6]
   P. Guasoni and A. Meireles-Rodrigues.
  Reference Dependence and Market Participation.
  *Mathematics of Operations Research*, 45(1), 129–156, 2019.
* [7]
   P. Guasoni and A. Meireles-Rodrigues.
  Reference Dependence: Endogenous Anchors and Life-Cycle Investing.
  *Mathematical Finance*, 34(3), 925–976, 2024.
* [8]
   D. Kahneman and A. Tversky.
  Prospect Theory: An Analysis of Decision under Risk.
  *Econometrica*, 47:263–291, 1979.
* [9]
   B. Kőszegi and M. Rabin.
  A model of reference-dependent preferences.
  *Quart. J. Econom.*, 121(4), 1133–1165, 2006.
* [10]
   B. Kőszegi and M. Rabin.
  Reference-dependent risk attitudes.
  *Am. Econ. Rev.*, 97(4):1047–1073,
  2007.
* [11]
   B. Kőszegi and M. Rabin.

  Choices, situations, and happiness.
  *Journal of Public Economics*,
  92(8):1821–1832, 2008.
* [12]
   B. Kőszegi and M. Rabin.
  Reference-dependent consumption plans.
  *The American Economic
  Review*, 99(3):909–936, 2009.
* [13]

  D. O. Kramkov and W. Schachermayer.
  The asymptotic elasticity of utility functions and optimal investment
  in incomplete markets.
  *Ann. Appl. Probab.*, 9:904–950, 1999.
* [14]
   G. Loomes and R. Sugden.
  Disappointment and Dynamic Consistency in
  Choice under Uncertainty.
  *Review of Economic Studies*, 53:271–282, 1986.
* [15]
   H. Markowitz.
  The Utility of Wealth.
  *Journal of Political Economy*, 60:151–158, 1952.
* [16]

  T. O’Donoghue and Ch. Sprenger.
  Reference-dependent preferences.
  *In: Handbook of behavioral economics: Applications and foundations 1*, 1–77,
  North-Holland, 2018.
* [17]
   W. Rudin.
  *Functional analysis.* 2nd ed.
  McGraw-Hill Inc., 1991.
* [18]
   A. Tversky and D. Kahneman.
  Advances in Prospect Theory: Cumulative Representation of Uncertainty.
  *Journal of Risk and Uncertainty*, 5:297–323, 1992.
* [19]
   E. Zeidler.
  *Nonlinear functional analysis and its applications I: fixed-point
  theorems.*
  Springer, New York, 1986.