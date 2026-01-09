---
authors:
- Xiangxin He
- Fangda Liu
- Ruodu Wang
doc_id: arxiv:2601.04067v1
family_id: arxiv:2601.04067
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Diversification Preferences and Risk Attitudes
url_abs: http://arxiv.org/abs/2601.04067v1
url_html: https://arxiv.org/html/2601.04067v1
venue: arXiv q-fin
version: 1
year: 2026
---


Xiangxin He
Department of Statistics and Actuarial Science, University of Waterloo, Canada. ✉ <g34he@uwaterloo.ca>
  
Fangda Liu
Department of Statistics and Actuarial Science, University of Waterloo, Canada. ✉ <fangda.liu@uwaterloo.ca>
  
Ruodu Wang
Department of Statistics and Actuarial Science, University of Waterloo, Canada. ✉ <wang@uwaterloo.ca>

(January 7, 2026)

###### Abstract

Portfolio diversification is a cornerstone of modern finance, while risk aversion is central to decision theory; both concepts are long-standing and foundational. We investigate their connections by studying how different forms of diversification correspond to notions of risk aversion. We focus on the classical distinctions between weak and strong risk aversion, and consider diversification preferences for pairs of risks that are identically distributed, comonotonic, antimonotonic, independent, or exchangeable, as well as their intersections. Under a weak continuity condition and without assuming completeness of preferences, diversification for antimonotonic and identically distributed pairs implies weak risk aversion, and diversification for exchangeable pairs is equivalent to strong risk aversion.
The implication from diversification for independent pairs to weak risk aversion requires a stronger continuity.
We further provide results and examples that clarify the relationships between various diversification preferences and risk attitudes, in particular justifying the one-directional nature of many implications.

Keywords: Diversification, dependence, risk aversion, antimonotonicity, incomplete preferences

## 1 Introduction

Diversification and risk attitudes are two of the most fundamental ideas in economics and finance. Diversification is central to portfolio selection and risk management since the seminal work of Markowitz ([1952](https://arxiv.org/html/2601.04067v1#bib.bib23)), while risk aversion is fundamental to models of decision making under risk (Arrow, [1963](https://arxiv.org/html/2601.04067v1#bib.bib2); Pratt, [1964](https://arxiv.org/html/2601.04067v1#bib.bib28); Rothschild and Stiglitz, [1970](https://arxiv.org/html/2601.04067v1#bib.bib31)). Both concepts are classical and deeply embedded in practice, and yet their precise relationship is subtle. A unified understanding of how “wanting to diversify” constrains a decision maker’s risk attitude is essential both for theory—to organize the rich landscape of preference models—and for applications, where one would like to infer risk attitudes from observed diversification behavior, or to predict diversification behavior from risk attitudes.

Dekel ([1989](https://arxiv.org/html/2601.04067v1#bib.bib9)) introduced an axiomatic notion of preference for portfolio diversification and showed diversification is strictly stronger than strong risk aversion of Rothschild and Stiglitz ([1970](https://arxiv.org/html/2601.04067v1#bib.bib31)), although these two concepts are equivalent under the expected utility (EU) model. Dekel formulated diversification as a preference for any convex combination of outcomes that are already equally desirable. This approach is conceptually natural, and it is mathematically elegant as it reduces to quasi-convexity of the preferences under mild conditions, highlighted by Chateauneuf and Tallon ([2002](https://arxiv.org/html/2601.04067v1#bib.bib5)) and Chateauneuf and Lakhnati ([2007](https://arxiv.org/html/2601.04067v1#bib.bib4)). Nevertheless, requiring
diversification for all dependence structures in the portfolio, including those without hedging effects, is quite demanding. In practice, investors may only actively seek diversification in specific situations—for example, when combining market positions that hedge each other, when combining insurance and reinsurance contracts, or when pooling uncorrelated assets. Outside these situations, there may be no compelling reason to treat mixing as strictly desirable, and the empirical verification of Dekel’s global notion of diversification needs to consider all types of dependence.

This observation raises a natural question: how should diversification be formulated when decision makers only exhibit it in certain economically meaningful configurations of the portfolio risks?
For pairs of risks, there are four fundamental dependence structures: comonotonicity, antimonotonicity, exchangeability, and independence; see McNeil et al. ([2015](https://arxiv.org/html/2601.04067v1#bib.bib24)) for these dependence concepts in risk management.
Diversification on antimonotonic pairs is intuitive and empirically observable, as it is common in practice for an investor to combine random payoffs that hedge each other, or to purchase an insurance policy on a potential random loss; in both cases, the decision maker prefers the combination of antimonotonic random variables.
Diversification on independent pairs is also compelling in the context of finance and insurance, as the average of independent payoffs reduces the total payoff’s variance, which is desirable as argued by Markowitz ([1952](https://arxiv.org/html/2601.04067v1#bib.bib23)).
Diversification on exchangeable pairs
reflects a tendency to combine risks that exhibit symmetry, a structure that is common for similar assets that share a common risk factor.
On the other hand, diversification on comontonic pairs may not be appealing, as such pairs do not provide hedging or risk reduction intuitively.111These dependence concepts are also prominent in decision theory.
Comonotonicity is fundamental to the axiomatization of the risk preferences of Yaari ([1987](https://arxiv.org/html/2601.04067v1#bib.bib36)) and the ambiguity model of Schmeidler ([1989](https://arxiv.org/html/2601.04067v1#bib.bib32)),
independence is used to axiomatize risk preferences by Pomatto et al. ([2020](https://arxiv.org/html/2601.04067v1#bib.bib27)) and
Mu et al. ([2024](https://arxiv.org/html/2601.04067v1#bib.bib25)), and antimonotonicity has special features in sharp contrast to comonotonicity, as studied by Aouani et al. ([2021](https://arxiv.org/html/2601.04067v1#bib.bib1)) and Principi et al. ([2025](https://arxiv.org/html/2601.04067v1#bib.bib29)). For a pair of identically distributed (ID) risks, exchangeability includes comonotonicity, independence, and antimonotonicity as special cases.

Our contributions are a systematic study of how diversification preferences on various classes of pairs relate to the classic notions of weak and strong risk aversion; thereby, we formally connect decision theory to dependence modeling, two popular research fields.
Our diversification preferences are formulated on (i) all pairs of risks, (ii) ID pairs, (iii) comonotonic pairs; (iv) antimonotonic pairs, (v) exchangeable pairs, (vi) independent pairs, and (vii) intersections such as antimonotonic and ID. We weaken the assumptions of Dekel in several ways: (a) we require diversification only for economically relevant dependence structures and pairs of risks,
(b) we do not impose completeness or monotonicity on the preferences, and (c) our continuity assumption, upper semicontinuity with respect to the L∞L^{\infty}-norm, is very weak.
Each weakening
makes our results stronger. The generalization in (a) offers new economic insights on the relationship between dependence and risk attitudes, a topic recently explored by Maccheroni et al. ([2025](https://arxiv.org/html/2601.04067v1#bib.bib21)) in the context of insurance.
The generalizations in (b)–(c) are not just technical, as they allow for more important risk preferences such as the incomplete mean-variance model of Markowitz ([1952](https://arxiv.org/html/2601.04067v1#bib.bib23))
and quantile maximizers (Rostek, [2010](https://arxiv.org/html/2601.04067v1#bib.bib30)).

Our main results are first formulated on L∞L^{\infty}, the space of bounded random variables. We find that diversification on antimonotonic and ID pairs lies strictly between weak and strong risk aversion (Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")),
whereas diversification on comonotonic pairs or independent pairs is too weak: neither implies weak risk aversion, and they are indeed compatible with strong risk-seeking models (Propositions [1](https://arxiv.org/html/2601.04067v1#Thmproposition1 "Proposition 1. ‣ 4.1 Comonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")–[2](https://arxiv.org/html/2601.04067v1#Thmproposition2 "Proposition 2. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")).
Diversification on exchangeable pairs,
or ID pairs with no restriction on the dependence, is equivalent to strong risk aversion (Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")).
We further show that under a stronger form of continuity, called compact upper semicontinuity (Chew and Mao, [1995](https://arxiv.org/html/2601.04067v1#bib.bib6)), diversification on independent and ID pairs lies strictly between weak and strong risk aversion (Theorem [3](https://arxiv.org/html/2601.04067v1#Thmtheorem3 "Theorem 3. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")). These results highlight
that the intuitively plausible and empirically observable property of diversification on antimonotonic (or independent) and ID pairs leads to weak risk aversion,
and extending the property to exchangeable pairs
gives rise to strong risk aversion.
Figure [1](https://arxiv.org/html/2601.04067v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Diversification Preferences and Risk Attitudes") summarizes the main obtained implications.
Furthermore, under mild conditions, neutrality to any of the diversification classes above is equivalent to risk neutrality (Theorem [4](https://arxiv.org/html/2601.04067v1#Thmtheorem4 "Theorem 4. ‣ 5 Neutrality ‣ Diversification Preferences and Risk Attitudes")).
The results are generalized to LpL^{p} for p⩾1p\geqslant 1 through a new result (Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes")) that can be seen as a law of large numbers for negatively dependent sequences (Lehmann, [1966](https://arxiv.org/html/2601.04067v1#bib.bib20)) on LpL^{p}, which may be of independent interest in probability theory.

|  |  |  |
| --- | --- | --- |
|  | Diversification on all⟹⇓⟹Diversification on AM  ／⇔Diversification on EX  ／⇔Diversification on IN⇓⇕⇓Diversification on AM & ID ⟸Diversification on ID ⟹Diversification on IN & ID ⇓⇕⇓∗Weak risk aversion ⟸Strong risk aversion⟹Weak risk aversion\begin{array}[]{ccccc}&&\mbox{Diversification on all}&&\vskip 5.69046pt\\ \vskip 5.69046pt&\mathrel{\rotatebox[origin={c}]{225.0}{$\implies$}}&\big\Downarrow&\mathrel{\rotatebox[origin={c}]{315.0}{$\implies$}}&\\ \mbox{Diversification on AM }&\mathchoice{\mathrel{\hbox to0.0pt{\kern 5.0pt\kern-5.27776pt$\displaystyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 5.0pt\kern-5.27776pt$\textstyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 3.98611pt\kern-4.45831pt$\scriptstyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 3.40282pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\iff}}}&\mbox{Diversification on EX }&\mathchoice{\mathrel{\hbox to0.0pt{\kern 5.0pt\kern-5.27776pt$\displaystyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 5.0pt\kern-5.27776pt$\textstyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 3.98611pt\kern-4.45831pt$\scriptstyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 3.40282pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\iff}}}&\mbox{Diversification on IN}\vskip 5.69046pt\\ \vskip 5.69046pt\big\Downarrow&&\big\Updownarrow&&\big\Downarrow\\ \mbox{Diversification on AM \& ID }&\impliedby&\mbox{Diversification on ID }&\implies&\mbox{Diversification on IN \& ID }\vskip 5.69046pt\\ \vskip 5.69046pt\big\Downarrow&&\big\Updownarrow&&~\big\Downarrow^{\*}\\ \mbox{Weak risk aversion }&\impliedby&\mbox{Strong risk aversion}&\implies&\mbox{Weak risk aversion}\end{array} |  |

Figure 1: Summary of results for risk preferences,
where “AM” stands for “antimonotonic” (we omit “pairs”), “EX” stands for “exchangeable”, “IN” stands for “independent”,  ／⇔\mathchoice{\mathrel{\hbox to0.0pt{\kern 5.0pt\kern-5.27776pt$\displaystyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 5.0pt\kern-5.27776pt$\textstyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 3.98611pt\kern-4.45831pt$\scriptstyle\not$\hss}{\iff}}}{\mathrel{\hbox to0.0pt{\kern 3.40282pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\iff}}} means incomparable, and ⇓∗\Downarrow^{\*} requires compact upper semicontinuity. The converse statements of all single-direction implications do not hold for general risk preferences.

The results in the paper require substantial technical innovations.
The proofs of the main results involve
iterative averaging and symmetrization scheme based on antimonotonic and independent couplings, using quantile transforms and a representation of Strassen ([1965](https://arxiv.org/html/2601.04067v1#bib.bib35)). For antimonotonic couplings, this iteration yields a sequence of payoffs with the same mean and strictly shrinking range, utilizing a technical lemma of Han et al. ([2024](https://arxiv.org/html/2601.04067v1#bib.bib14)). The shrinking range is important for us to use L∞L^{\infty}-upper semicontinuity.
Theorems [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")–[3](https://arxiv.org/html/2601.04067v1#Thmtheorem3 "Theorem 3. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") generalize
several results in the literature, including
Dekel ([1989](https://arxiv.org/html/2601.04067v1#bib.bib9)) and Chateauneuf and Lakhnati ([2007](https://arxiv.org/html/2601.04067v1#bib.bib4)) on strong risk aversion,
Leitner ([2005](https://arxiv.org/html/2601.04067v1#bib.bib18)) and Föllmer and Schied ([2016](https://arxiv.org/html/2601.04067v1#bib.bib12)) on law-invariant risk measures,
Principi et al. ([2025](https://arxiv.org/html/2601.04067v1#bib.bib29)) on antimonotonic convexity.
For independent pairs, L∞L^{\infty}-continuity is not sufficient because the laws of large numbers do not offer convergence in L∞L^{\infty}.
The law of large numbers for negatively dependent sequences on LpL^{p}
requires classic techniques in stochastic order (Müller and Stoyan, [2002](https://arxiv.org/html/2601.04067v1#bib.bib26); Shaked and Shanthikumar, [2007](https://arxiv.org/html/2601.04067v1#bib.bib34)) and a recent result on uniform integrability by Leskelä and Vihola ([2013](https://arxiv.org/html/2601.04067v1#bib.bib19)).
We offer many (counter)examples that carefully design law-invariant and continuous mappings that violate various versions of diversification while satisfying or failing risk aversion. These examples illustrate the necessity of our assumptions and the exact scope of each result, which justify the strictness of the single-direction implications in Figure [1](https://arxiv.org/html/2601.04067v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Diversification Preferences and Risk Attitudes").

## 2 Preferences and risk aversion

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be an atomless probability space and L∞L^{\infty} be the set of essentially bounded random variables on this space. Almost-sure equal random variables are treated as identical.
Random variables in L∞L^{\infty} are interpreted as random payoffs in one period. Constant random variables are identified with elements in ℝ\mathbb{R}. The L∞L^{\infty}-norm of a random variable XX is given by

|  |  |  |
| --- | --- | --- |
|  | ‖X‖∞=inf{x∈ℝ:ℙ​(|X|>x)=0},\|X\|\_{\infty}=\inf\{x\in\mathbb{R}:\mathbb{P}(|X|>x)=0\}, |  |

which is the essential supremum of |X|.|X|.
In the main part of the paper, we work with the domain L∞L^{\infty}, which is the standard space in decision theory and risk measures. The results can be generalized to LpL^{p} with p∈[1,∞)p\in[1,\infty), the space of random variables with finite pp-th moment, which we discuss in Section [6](https://arxiv.org/html/2601.04067v1#S6 "6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes").
Let Δn\Delta\_{n} be the standard simplex in ℝn\mathbb{R}^{n}.
All terms like “increasing” in this paper are in the weak sense.

We write X=dYX\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y when two random variables (or random vectors) XX and YY are identically distributed (ID).
The decision maker’s preferences are represented by
a transitive binary relation ≿\succsim on L∞L^{\infty}, called a preference relation, with strict part ≻\succ and symmetric part ≃\simeq.
A *risk preference* ≿\succsim is a preference relation satisfying the following two standard properties.

1. (a)

   Law invariance: X=dY⟹X≃YX\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y\implies X\simeq Y for all X,Y∈L∞X,Y\in L^{\infty},
2. (b)

   Upper semicontinuity: the set
   {Y∈L∞:Y≿X}\left\{Y\in L^{\infty}:Y\succsim X\right\} is closed with respect to L∞L^{\infty}-norm for each X∈L∞X\in L^{\infty}.

If in (b), the set {Y∈L∞:X≿Y}\left\{Y\in L^{\infty}:X\succsim Y\right\} is also closed, then ≿\succsim is *continuous*.
Throughout, continuity is with respect to L∞L^{\infty}-norm when not specified otherwise.
Virtually all decision models satisfy this form of continuity.
We do not assume completeness of ≿\succsim (each pair is comparable by ≿\succsim)
or monotonicity (X⩾YX\geqslant Y implies X≿YX\succsim Y).
This allows for incomplete and nonmonotone preferences, such as the mean-variance preferences of Markowitz ([1952](https://arxiv.org/html/2601.04067v1#bib.bib23)), that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | X≿Y⇔𝔼​[X]⩾𝔼​[Y]​ and ​Var​(X)⩽Var​(Y).X\succsim Y~\iff~\mathbb{E}[X]\geqslant\mathbb{E}[Y]\mbox{ and }\mathrm{Var}(X)\leqslant\mathrm{Var}(Y). |  | (1) |

In all results, we do not assume any particular decision model for the risk preferences.

In many financial applications, the preference relation
≿\succsim is represented by
a utility functional 𝒰\mathcal{U} on L∞L^{\infty}, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | X≿Y⇔𝒰​(X)⩾𝒰​(Y),X\succsim Y~\iff~\mathcal{U}(X)\geqslant\mathcal{U}(Y), |  | (2) |

or
a risk measure ρ\rho on L∞L^{\infty} (with a sign flip), that is, X≿Y⇔ρ​(−X)⩽ρ​(−Y).X\succsim Y\iff\rho(-X)\leqslant\rho(-Y).
The input of the risk measure is −X-X, interpreted as the potential loss/gain from the payoff XX, following the convention of McNeil et al. ([2015](https://arxiv.org/html/2601.04067v1#bib.bib24)).
With ([2](https://arxiv.org/html/2601.04067v1#S2.E2 "In 2 Preferences and risk aversion ‣ Diversification Preferences and Risk Attitudes")), property (a) of ≿\succsim translates into law invariance of 𝒰\mathcal{U}, i.e., X=dYX\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y implies 𝒰​(X)=𝒰​(Y)\mathcal{U}(X)=\mathcal{U}(Y), and property (b) translates into
the upper semicontinuity of 𝒰\mathcal{U}. These are standard properties and satisfied by common utility functionals and risk measures.

For some results, we need a stronger notion of continuity, called compact continuity (Chew and Mao, [1995](https://arxiv.org/html/2601.04067v1#bib.bib6); Chateauneuf and Lakhnati, [2007](https://arxiv.org/html/2601.04067v1#bib.bib4)).
We say that
a sequence (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} of random variables converges to XX in *bounded convergence* if (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} is uniformly bounded and Xn→XX\_{n}\to X almost surely. For law-invariant preference relations, it is safe to replace almost sure convergence here with convergence in distribution.

1. (c)

   Compact continuity: the sets
   {Y∈L∞:Y≿X}\left\{Y\in L^{\infty}:Y\succsim X\right\}
   and
   {Y∈L∞:X≿Y}\left\{Y\in L^{\infty}:X\succsim Y\right\}
   are closed with respect to bounded convergence for each X∈L∞X\in L^{\infty}.

Compact upper semicontinuity
is defined analogously.
Compact (semi)continuity is stronger than L∞L^{\infty}-(semi)continuity. For instance,
denote by
QXQ\_{X} the left quantile function of a random variable XX, that is, QX​(t)=inf{x∈ℝ:ℙ​(X⩽x)⩾t}Q\_{X}(t)=\inf\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)\geqslant t\} for t∈(0,1)t\in(0,1). The quantile mapping X↦QX​(t)X\mapsto Q\_{X}(t) for any t∈(0,1)t\in(0,1) is L∞L^{\infty}-continuous but not compact continuous; another such example is the essential supremum functional X↦ess​-​sup​XX\mapsto\mathrm{ess\mbox{-}sup}X.

Next, we introduce notions of risk aversion.
First, we need the concave order between two random variables X,Y∈L∞X,Y\in L^{\infty}, written as X⩾cvYX\geqslant\_{\rm cv}Y, when

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[u​(X)]⩾𝔼​[u​(Y)]for all concave​u:ℝ→ℝ.\mathbb{E}[u(X)]\geqslant\mathbb{E}[u(Y)]\quad\text{for all concave}\ u:\mathbb{R}\to\mathbb{R}. |  |

For technical treatments on the concave order and its variants, see Shaked and Shanthikumar ([2007](https://arxiv.org/html/2601.04067v1#bib.bib34)). In risk management, it is common to use the convex order, which is the reverse relation of the concave order, that is, X⩾cxY⇔X⩽cvYX\geqslant\_{\rm cx}Y\iff X\leqslant\_{\rm cv}Y.

The weak and strong notions of risk aversion are defined next. For various notions of risk aversion in popular decision models and their characterization, see Cohen ([1995](https://arxiv.org/html/2601.04067v1#bib.bib8)) and Schmidt and Zank ([2008](https://arxiv.org/html/2601.04067v1#bib.bib33)).

###### Definition 1.

A risk preference ≿\succsim exhibits weak risk aversion if for X∈L∞X\in L^{\infty},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X]≿X.\mathbb{E}[X]\succsim X. |  |

A risk preference ≿\succsim exhibits strong risk aversion if for X,Y∈L∞X,Y\in L^{\infty},

|  |  |  |
| --- | --- | --- |
|  | X⩾cvY⟹X≿Y.X\geqslant\_{\rm cv}Y\implies X\succsim Y. |  |

Weak and strong notions of risk seeking are defined by replacing ≿\succsim with ≾\precsim in the above implications, respectively.
Risk neutrality means 𝔼​[X]≃X\mathbb{E}[X]\simeq X for all X∈L∞X\in L^{\infty}.

It is straightforward to see that strong risk aversion implies weak risk aversion, and risk neutrality is equivalent to both (either weak or strong) risk aversion and risk seeking.
In the expected utility (EU) model, each of weak risk aversion and strong risk aversion is equivalent to a concave utility function. In the dual utility model of Yaari ([1987](https://arxiv.org/html/2601.04067v1#bib.bib36)), weak risk aversion is strictly weaker than strong risk aversion. Incomplete and non-monotone preferences can exhibit risk aversion; for instance, ([1](https://arxiv.org/html/2601.04067v1#S2.E1 "In 2 Preferences and risk aversion ‣ Diversification Preferences and Risk Attitudes")) exhibits strong risk aversion.

## 3 Diversification and dependence

We first introduce a few notions of dependence that are important in statistical modeling. They will be essential in our formulation of diversification.

1. (a)

   A pair (X,Y)(X,Y) of random variables is comonotonic if

   |  |  |  |
   | --- | --- | --- |
   |  | (X​(ω)−X​(ω′))​(Y​(ω)−Y​(ω′))⩾0for ​(ω,ω′)∈Ω2, ℙ×ℙ-a.s.(X(\omega)-X(\omega^{\prime}))(Y(\omega)-Y(\omega^{\prime}))\geqslant 0\quad\text{for }(\omega,\omega^{\prime})\in\Omega^{2},\mbox{~$\mathbb{P}\times\mathbb{P}$-a.s.} |  |
2. (b)

   a pair (X,Y)(X,Y) is *antimonotonic* (also called *anticomonotonic*, or *counter-monotonic*) if (X,−Y)(X,-Y) is comonotonic.
3. (c)

   A pair
   (X,Y)(X,Y) is exchangeable
   if (X,Y)=d(Y,X)(X,Y)\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}(Y,X).

Comonotonicity describes the strongest form of positive dependence,
whereas antimonotonicity describes the strongest form of negative dependence.
An exchangeable pair is necessarily ID. For ID pairs, all of comonotonicity, independence, and antimonotonicity are special cases of exchangeability. For a general treatment on these dependence concepts, see Joe ([1997](https://arxiv.org/html/2601.04067v1#bib.bib15)).

We now define diversification in a similar way to Dekel ([1989](https://arxiv.org/html/2601.04067v1#bib.bib9)), with the difference that we will restrict the random payoffs at comparison to those satisfying certain conditions specified by a class 𝒳⊆(L∞)2\mathcal{X}\subseteq(L^{\infty})^{2} of pairs of random variables.

###### Definition 2.

For 𝒳⊆(L∞)2\mathcal{X}\subseteq(L^{\infty})^{2}, a risk preference ≿\succsim exhibits
*diversification on 𝒳\mathcal{X}* if

|  |  |  |  |
| --- | --- | --- | --- |
|  | X≃Y⟹λ​X+(1−λ)​Y≿Y​ for all λ∈[0,1],X\simeq Y\implies\lambda X+(1-\lambda)Y\succsim Y\mbox{ for all $\lambda\in[0,1]$}, |  | (3) |

and for all (X,Y)∈𝒳(X,Y)\in\mathcal{X}.

We use natural language to describe the class 𝒳\mathcal{X}. For instance, we say “diversification on antimonotonic and ID pairs”, meaning that ([3](https://arxiv.org/html/2601.04067v1#S3.E3 "In Definition 2. ‣ 3 Diversification and dependence ‣ Diversification Preferences and Risk Attitudes")) holds for (X,Y)(X,Y) that satisfy both antimonotonicity and ID.
When 𝒳=(L∞)2\mathcal{X}=(L^{\infty})^{2}, we simply say “diversification on all pairs”.

Dekel ([1989](https://arxiv.org/html/2601.04067v1#bib.bib9)) formulated diversification on an arbitrary number of random payoffs, that is,

|  |  |  |
| --- | --- | --- |
|  | n∈ℕ,X1≃⋯≃Xn⟹∑i=1nλi​Xi≿X1​ for all (λ1,…,λn)∈Δn,n\in\mathbb{N},~X\_{1}\simeq\dots\simeq X\_{n}\implies\sum\_{i=1}^{n}\lambda\_{i}X\_{i}\succsim X\_{1}\mbox{~for all $(\lambda\_{1},\dots,\lambda\_{n})\in\Delta\_{n}$}, |  |

where Δn\Delta\_{n} is the standard simplex in ℝn\mathbb{R}^{n}.
Our formulation ([3](https://arxiv.org/html/2601.04067v1#S3.E3 "In Definition 2. ‣ 3 Diversification and dependence ‣ Diversification Preferences and Risk Attitudes")) only involves pairs of payoffs in a set 𝒳\mathcal{X}, thus a weaker requirement in general; some conditions on more than two payoffs are indirectly imposed through transitivity
of ≿\succsim.
A slightly stronger formulation than ([3](https://arxiv.org/html/2601.04067v1#S3.E3 "In Definition 2. ‣ 3 Diversification and dependence ‣ Diversification Preferences and Risk Attitudes")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | X≿Y⟹λ​X+(1−λ)​Y≿Y​ for all λ∈[0,1],\displaystyle X\succsim Y\implies\lambda X+(1-\lambda)Y\succsim Y\mbox{ for all $\lambda\in[0,1]$}, |  | (4) |

and under mild conditions the two formulations are equivalent (e.g., Chateauneuf and Tallon, [2002](https://arxiv.org/html/2601.04067v1#bib.bib5)).
The property in ([4](https://arxiv.org/html/2601.04067v1#S3.E4 "In 3 Diversification and dependence ‣ Diversification Preferences and Risk Attitudes")) for all pairs (X,Y)(X,Y) is called *convexity*, *concavity*, *quasi-convexity*, or *quasi-concavity* of ≿\succsim by different authors.
In the context of risk measures, ([4](https://arxiv.org/html/2601.04067v1#S3.E4 "In 3 Diversification and dependence ‣ Diversification Preferences and Risk Attitudes")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(λ​X+(1−λ)​Y)⩽max⁡{ρ​(X),ρ​(Y)},X,Y∈L∞,λ∈[0,1],\rho(\lambda X+(1-\lambda)Y)\leqslant\max\{\rho(X),\rho(Y)\},~~~X,Y\in L^{\infty},~\lambda\in[0,1], |  | (5) |

which is called the quasi-convexity of ρ\rho, and is well studied by Cerreia-Vioglio et al. ([2011](https://arxiv.org/html/2601.04067v1#bib.bib3)).222A *monetary* risk measure (Föllmer and Schied, [2016](https://arxiv.org/html/2601.04067v1#bib.bib12)) is a mapping ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} that satisfies *monotonicity*: ρ​(X)⩾ρ​(Y)\rho(X)\geqslant\rho(Y) if X⩾YX\geqslant Y,
and *cash additivity*: ρ​(X+c)=ρ​(X)+c\rho(X+c)=\rho(X)+c for c∈ℝc\in\mathbb{R} and X∈L∞X\in L^{\infty}.
For monetary risk measures, quasi-convexity is equivalent to the usual convexity. All law-invariant convex and monetary risk measures, as well as their maximum, minimum, and convex combinations,
exhibit strong risk aversion (Mao and Wang, [2020](https://arxiv.org/html/2601.04067v1#bib.bib22), Proposition 3.2).

## 4 Relations between diversification and risk aversion

Diversification is closely related to risk aversion, as already observed by Dekel ([1989](https://arxiv.org/html/2601.04067v1#bib.bib9)). In this section we explore how imposing specific dependence structures in diversification affects risk aversion.

### 4.1 Comonotonic pairs

Our first observation is that diversification for comonotonic pairs does not lead to any notion of risk aversion. Intuitively, XX and YY in a comonotonic pair do not hedge each other in the portfolio λ​X+(1−λ)​Y\lambda X+(1-\lambda)Y.
If (X,Y)(X,Y) is comonotonic, then

|  |  |  |
| --- | --- | --- |
|  | Qλ​X+(1−λ)​Y=λ​QX+(1−λ)​QY.Q\_{\lambda X+(1-\lambda)Y}=\lambda Q\_{X}+(1-\lambda)Q\_{Y}. |  |

Therefore, the left quantile is affine on comonotonic pairs, although quantiles do not exhibit risk aversion or risk seeking in general; see McNeil et al. ([2015](https://arxiv.org/html/2601.04067v1#bib.bib24)) for more discussions on comonotonicity and using quantiles as risk measures in finance.
Hence, diversification on comonotonic pairs is not directly related to hedging considerations and it does not
force the decision maker to be risk averse. The following proposition makes this simple point clear. It further illustrates that a risk preference can exhibit both diversification on comonotonic pairs and *strict strong risk seeking*, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | for all X,Y with X​=d​Y,X⩾cvY⟹Y≻X.\mbox{ for all $X,Y$ with $X\not\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y$},~X\geqslant\_{\rm cv}Y\implies Y\succ X. |  | (6) |

###### Proposition 1.

For a risk preference, diversification on comonotonic pairs
does not imply weak risk aversion. Indeed, the risk preference ≿\succsim represented by UU via ([2](https://arxiv.org/html/2601.04067v1#S2.E2 "In 2 Preferences and risk aversion ‣ Diversification Preferences and Risk Attitudes")) with

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(X)=∫01g​(t)​QX​(t)​dt,X∈L∞, for any increasing function g,\mathcal{U}(X)=\int\_{0}^{1}g(t)Q\_{X}(t)\mathrm{d}t,~~X\in L^{\infty},\mbox{~~for any increasing function $g$,} |  |

exhibits diversification on comonotonic pairs and strict strong risk seeking in ([6](https://arxiv.org/html/2601.04067v1#S4.E6 "In 4.1 Comonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")).

###### Proof.

It suffices to show the second statement.
Note that ≿\succsim belongs to the dual utility of Yaari ([1987](https://arxiv.org/html/2601.04067v1#bib.bib36)) with a strictly concave weighting function. As a common property of the dual utility functional, 𝒰\mathcal{U} is affine on comonotonic pairs, and hence diversification on comonotonic pairs holds. We can check that it also satisfies ([6](https://arxiv.org/html/2601.04067v1#S4.E6 "In 4.1 Comonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")); a precise statement of this fact can be found in Lauzier et al. ([2025](https://arxiv.org/html/2601.04067v1#bib.bib17), Corollary 1).
∎

Chateauneuf and Tallon ([2002](https://arxiv.org/html/2601.04067v1#bib.bib5)) showed that in the EU model, diversification on comonotonic pairs is equivalent to both diversification on all pairs and strong risk aversion. Combined with Proposition [1](https://arxiv.org/html/2601.04067v1#Thmproposition1 "Proposition 1. ‣ 4.1 Comonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"), this highlights the coarse nature of the EU model in its treatment of diversification.

### 4.2 Antimonotonic pairs

In contrast to the negative result in
Proposition [1](https://arxiv.org/html/2601.04067v1#Thmproposition1 "Proposition 1. ‣ 4.1 Comonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"), we present a positive result that diversification on antimonotonic pairs, which is intuitively plausible,
has a
normatively appealing consequence, that is, weak risk aversion.

###### Theorem 1.

For a risk preference, diversification on antimonotonic and ID pairs implies weak risk aversion,
and it is implied by strong risk aversion.
Both implications are in general strict.

###### Proof.

We first show the implication from diversification on antimonotonic and ID pairs to weak risk aversion.
Let X∈L∞X\in L^{\infty} and UU be uniformly distributed on [0,1][0,1]. Define

|  |  |  |
| --- | --- | --- |
|  | X0(1)=QX​(U),X0(2)=QX​(1−U),andX1=X0(1)+X0(2)2.X\_{0}^{(1)}=Q\_{X}(U),\quad X\_{0}^{(2)}=Q\_{X}(1-U),\quad\mbox{and}\quad X\_{1}=\frac{X\_{0}^{(1)}+X\_{0}^{(2)}}{2}. |  |

Clearly, X=dX0(1)=dX0(2)X\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}X\_{0}^{(1)}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}X\_{0}^{(2)}.
Further, by construction, X0(1)X\_{0}^{(1)} and X0(2)X\_{0}^{(2)} are anti-comonotonic. By diversification on antimonotonic pairs and law invariance of ≿\succsim, we have

|  |  |  |
| --- | --- | --- |
|  | X1=12​X0(1)+12​X0(2)≿X0(1)≃X,X\_{1}=\frac{1}{2}X\_{0}^{(1)}+\frac{1}{2}X\_{0}^{(2)}\succsim X\_{0}^{(1)}\simeq X, |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X1]=12​𝔼​[X0(1)]+12​𝔼​[X0(2)]=𝔼​[X].\mathbb{E}[X\_{1}]=\frac{1}{2}\mathbb{E}\left[X\_{0}^{(1)}\right]+\frac{1}{2}\mathbb{E}\left[X\_{0}^{(2)}\right]=\mathbb{E}[X]. |  |

Inductively, for n∈ℕn\in\mathbb{N}, we can construct

|  |  |  |
| --- | --- | --- |
|  | Xn(1)=QXn​(U),Xn(2)=QXn​(1−U),andXn+1=Xn(1)+Xn(2)2.X\_{n}^{(1)}=Q\_{X\_{n}}(U),\quad X\_{n}^{(2)}=Q\_{X\_{n}}(1-U),\quad\text{and}\quad X\_{n+1}=\frac{X\_{n}^{(1)}+X\_{n}^{(2)}}{2}. |  |

Following the same arguments, we have

|  |  |  |
| --- | --- | --- |
|  | Xn≿Xn−1≿⋯≿X1≿Xand𝔼​[Xn]=𝔼​[X].X\_{n}\succsim X\_{n-1}\succsim\dots\succsim X\_{1}\succsim X\ \ \text{and}\ \ \mathbb{E}[X\_{n}]=\mathbb{E}[X]. |  |

For n∈ℕn\in\mathbb{N}, let Rn=ess​-​sup​Xn−ess​-​inf​XnR\_{n}=\mathrm{ess\mbox{-}sup}X\_{n}-\mathrm{ess\mbox{-}inf}X\_{n}, where for any random variable ZZ, ess​-​sup​Z\mathrm{ess\mbox{-}sup}Z is its essential supremum and ess​-​inf​Z\mathrm{ess\mbox{-}inf}Z is its essential infinimum. Clearly,

|  |  |  |
| --- | --- | --- |
|  | ess​-​inf​Xn⩽𝔼​[Xn]=𝔼​[X]⩽ess​-​sup​Xn.\mathrm{ess\mbox{-}inf}X\_{n}\leqslant\mathbb{E}[X\_{n}]=\mathbb{E}[X]\leqslant\mathrm{ess\mbox{-}sup}X\_{n}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | |Xn−𝔼​[X]|⩽ess​-​sup​Xn−ess​-​inf​Xn=Rnℙ-a.s.|X\_{n}-\mathbb{E}[X]|\leqslant\mathrm{ess\mbox{-}sup}X\_{n}-\mathrm{ess\mbox{-}inf}X\_{n}=R\_{n}\quad\mbox{$\mathbb{P}$-a.s.} |  |

and thus ‖Xn−𝔼​[X]‖∞⩽Rn.\|X\_{n}-\mathbb{E}[X]\|\_{\infty}\leqslant R\_{n}.
Lemma 3.1 of Han et al. ([2024](https://arxiv.org/html/2601.04067v1#bib.bib14)) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rn+1⩽Rn2​ for n⩾0.R\_{n+1}\leqslant\frac{R\_{n}}{2}~~~\mbox{ for $n\geqslant 0$.} |  | (7) |

We here give a short self-contained proof of ([7](https://arxiv.org/html/2601.04067v1#S4.E7 "In Proof. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")).
Let m=QXn​(1/2)m=Q\_{X\_{n}}(1/2).
When U⩽1/2U\leqslant 1/2, it is QXn​(U)⩽m⩽QXn​(1−U)Q\_{X\_{n}}(U)\leqslant m\leqslant Q\_{X\_{n}}(1-U).
When U>1/2U>1/2, it is QXn​(U)⩾m⩾QXn​(1−U)Q\_{X\_{n}}(U)\geqslant m\geqslant Q\_{X\_{n}}(1-U).
In both cases, we have

|  |  |  |
| --- | --- | --- |
|  | ess​-​inf​Xn+m2⩽QXn​(U)+QXn​(1−U)2⩽m+ess​-​sup​Xn2.\frac{\mathrm{ess\mbox{-}inf}X\_{n}+m}{2}\leqslant\frac{Q\_{X\_{n}}(U)+Q\_{X\_{n}}(1-U)}{2}\leqslant\frac{m+\mathrm{ess\mbox{-}sup}X\_{n}}{2}. |  |

Therefore, Xn+1X\_{n+1} is between (ess​-​inf​Xn+m)/2(\mathrm{ess\mbox{-}inf}X\_{n}+m)/2 and (ess​-​sup​Xn+m)/2(\mathrm{ess\mbox{-}sup}X\_{n}+m)/2, thus showing ([7](https://arxiv.org/html/2601.04067v1#S4.E7 "In Proof. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")). As a consequence of this,
Rn⩽R0/2n→0R\_{n}\leqslant{R\_{0}}/{2^{n}}\to 0 as n→∞n\to\infty.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | 0⩽limn→∞‖Xn−𝔼​[X]‖∞⩽limn→∞Rn=0.0\leqslant\lim\_{n\to\infty}\|X\_{n}-\mathbb{E}[X]\|\_{\infty}\leqslant\lim\_{n\to\infty}R\_{n}=0. |  |

By the upper semicontinuity of ≿\succsim, we conclude

|  |  |  |
| --- | --- | --- |
|  | Xn≿Xfor all ​n∈ℕ⟹𝔼​[X]≿X.X\_{n}\succsim X\ \ \text{for all }\ n\in\mathbb{N}~\implies~\mathbb{E}[X]\succsim X. |  |

To show strong risk aversion implies diversification on ID pairs (antimonotonic or not), it suffices to note that for any X=dYX\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y and λ∈[0,1]\lambda\in[0,1], we have λ​X+(1−λ)​Y⩾cvX\lambda X+(1-\lambda)Y\geqslant\_{\rm cv}X, which follows directly by Jensen’s inequality.
The strictness of both implications
is justified by Example [1](https://arxiv.org/html/2601.04067v1#Thmexample1 "Example 1 (Weak risk aversion \" ／\"⟹ diversification on AM and ID). ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") and Remark [1](https://arxiv.org/html/2601.04067v1#Thmremark1 "Remark 1 (Diversification on AM \" ／\"⟹ strong risk aversion). ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes").
∎

###### Example 1 (Weak risk aversion  ／⟹\mathchoice{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\displaystyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\textstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 2.625pt\kern-4.45831pt$\scriptstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 1.875pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\implies}}} diversification on AM and ID).

Let the risk preference ≿\succsim be given by

|  |  |  |
| --- | --- | --- |
|  | X≿Y⇔𝒰​(X)⩾𝒰​(Y),X\succsim Y~\iff~\mathcal{U}(X)\geqslant\mathcal{U}(Y), |  |

where 𝒰​(Z)=𝔼​[Z]−Var​(Z)​|2−Var​(Z)|\mathcal{U}(Z)=\mathbb{E}[Z]-\mathrm{Var}(Z)|2-\mathrm{Var}(Z)| for Z∈L∞Z\in L^{\infty}.
It is clear that ≿\succsim exhibits weak risk aversion because 𝒰​(X)⩽𝔼​[X]=𝒰​(𝔼​[X])\mathcal{U}(X)\leqslant\mathbb{E}[X]=\mathcal{U}(\mathbb{E}[X]).
Let A,B,CA,B,C form a partition of Ω\Omega with equal probability, X=3​𝟙AX=3\mathds{1}\_{A}, and Y=3​𝟙BY=3\mathds{1}\_{B}. Clearly, (X,Y)(X,Y) is an antimonotonic and ID pair. Let Z=(X+Y)/2Z=(X+Y)/2.
We can compute 𝔼​[X]=1\mathbb{E}[X]=1, Var​(X)=2\mathrm{Var}(X)=2, 𝔼​[Z]=1\mathbb{E}[Z]=1, and Var​(Z)=1/2\mathrm{Var}(Z)=1/2.
Therefore,
𝒰​(X)=1>1/4=𝒰​(Z),\mathcal{U}(X)=1>1/4=\mathcal{U}(Z),
violating diversification on antimonotonic and ID pairs.

###### Remark 1 (Diversification on AM  ／⟹\mathchoice{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\displaystyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\textstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 2.625pt\kern-4.45831pt$\scriptstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 1.875pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\implies}}} strong risk aversion).

Aouani et al. ([2021](https://arxiv.org/html/2601.04067v1#bib.bib1)) showed that, for preferences represented by Choquet integrals, quasi-convexity on antimonotonic pairs is strictly weaker than convexity. Applying this to the dual utility model of Yaari ([1987](https://arxiv.org/html/2601.04067v1#bib.bib36)), we get that diversification for antimonotonic pairs does not imply strong risk aversion. An analysis of their differences in the dual utility model is provided by Ghossoub et al. ([2025](https://arxiv.org/html/2601.04067v1#bib.bib13)).

###### Example 2 (Strong risk aversion  ／⟹\mathchoice{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\displaystyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\textstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 2.625pt\kern-4.45831pt$\scriptstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 1.875pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\implies}}} diversification on AM).

Let the risk preference ≿\succsim be given by

|  |  |  |
| --- | --- | --- |
|  | X≿Y⇔𝔼​[X]−(Var​(X))1/4⩾𝔼​[Y]−(Var​(Y))1/4.X\succsim Y~\iff~\mathbb{E}[X]-(\mathrm{Var}(X))^{1/4}\geqslant\mathbb{E}[Y]-(\mathrm{Var}(Y))^{1/4}. |  |

It is straightforward to check that ≿\succsim exhibits strong risk aversion. Let X=1X=1, YY take values 11 and 33 with equal probability, and Z=(X+Y)/2Z=(X+Y)/2. Note that (X,Y)(X,Y) is antimonotonic since XX is a constant. We have 𝔼​[Y]=2\mathbb{E}[Y]=2, Var​(Y)=1\mathrm{Var}(Y)=1, 𝔼​[Z]=3/2\mathbb{E}[Z]=3/2, and Var​(Z)=1/4\mathrm{Var}(Z)=1/4.
Hence, X≃YX\simeq Y and
𝔼​[Z]−(Var​(Z))1/4=3/2−(1/2)1/2<1=𝔼​[X]−(Var​(X))1/4\mathbb{E}[Z]-(\mathrm{Var}(Z))^{1/4}=3/2-(1/2)^{1/2}<1=\mathbb{E}[X]-(\mathrm{Var}(X))^{1/4}, showing that Z≺XZ\prec X, violating diversification on antimonotonic pairs.
Nevertheless, diversification on antimonotonic and ID pairs holds by Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes").

###### Remark 2.

In order to get an equivalent characterization of weak risk aversion, one needs to exclusively restrict attention to comparisons between a constant and a random variable. Chateauneuf and Lakhnati ([2007](https://arxiv.org/html/2601.04067v1#bib.bib4), Theorem 3.1) show that weak risk aversion is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | n∈ℕ,X1≃⋯≃Xn,(λ1,…,λn)∈Δn,∑i=1nλi​Xi∈ℝ⟹∑i=1nλi​Xi≿X1,n\in\mathbb{N},~X\_{1}\simeq\dots\simeq X\_{n},~(\lambda\_{1},\dots,\lambda\_{n})\in\Delta\_{n},~\sum\_{i=1}^{n}\lambda\_{i}X\_{i}\in\mathbb{R}\implies\sum\_{i=1}^{n}\lambda\_{i}X\_{i}\succsim X\_{1}, |  | (8) |

under additional conditions: completeness, monotonicity, and compact continuity. Maccheroni et al. ([2025](https://arxiv.org/html/2601.04067v1#bib.bib21), Theorem 1) characterized weak risk aversion via

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y=dZ​ and X+Y∈ℝ⟹X+Y≿X+Z,Y\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Z\mbox{ and $X+Y\in\mathbb{R}$}\implies X+Y\succsim X+Z, |  | (9) |

with no additional assumptions on ≿\succsim other than law invariance and transitivity.
None of ([8](https://arxiv.org/html/2601.04067v1#S4.E8 "In Remark 2. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")) (even restricted to n=2n=2) and ([9](https://arxiv.org/html/2601.04067v1#S4.E9 "In Remark 2. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")) is compatible with Definition [2](https://arxiv.org/html/2601.04067v1#Thmdefinition2 "Definition 2. ‣ 3 Diversification and dependence ‣ Diversification Preferences and Risk Attitudes").

### 4.3 Exchangeable pairs

We next focus on diversification on exchangeable pairs, which turns out to be equivalent to diversification on ID pairs.

###### Theorem 2.

For a risk preference, the following are equivalent:

1. (i)

   strong risk aversion;
2. (ii)

   diversification on ID pairs;
3. (iii)

   diversification on exchangeable pairs.

###### Proof.

(i)⇒\Rightarrow(ii):
Strong risk aversion implies diversification on ID pairs, as we see in the proof of Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes").
(ii)⇒\Rightarrow(iii): This follows by definition.
We will prove the most involved direction, (iii)⇒\Rightarrow(i), below.

Take X,Y∈L∞X,Y\in L^{\infty} with X⩾cvYX\geqslant\_{\rm cv}Y. By Strassen’s Theorem (Strassen, [1965](https://arxiv.org/html/2601.04067v1#bib.bib35)), there exists (X′,Y′)(X^{\prime},Y^{\prime}) such that X′=dXX^{\prime}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}X, Y′=dYY^{\prime}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y, and 𝔼​[Y′∣X′]=X′\mathbb{E}[Y^{\prime}\mid X^{\prime}]=X^{\prime}. By law invariance of ≿\succsim, it suffices to show X′≿Y′X^{\prime}\succsim Y^{\prime}. Therefore, it is without loss of generality to assume 𝔼​[Y|X]=X\mathbb{E}[Y|X]=X. Further, since the risk preference is law invariant, it does not lose generality to assume that there exists a sequence (Un)n∈ℕ(U\_{n})\_{n\in\mathbb{N}} of independent and ID uniformly distributed random variables on [0,1][0,1] independent of XX.

We first analyze the case when XX takes values in a finite set 𝒮\mathcal{S}.
Let Z0=Y−XZ\_{0}=Y-X. Inductively for n⩾0n\geqslant 0, we define the following quantities.
Define the function

|  |  |  |
| --- | --- | --- |
|  | Qn​(s,t)=inf{z∈ℝ:ℙ​(Zn⩽z∣X=s)⩾t},t∈(0,1),s∈𝒮,Q\_{n}(s,t)=\inf\{z\in\mathbb{R}:\mathbb{P}(Z\_{n}\leqslant z\mid X=s)\geqslant t\},~~~t\in(0,1),~s\in\mathcal{S}, |  |

which is the conditional quantile of ZnZ\_{n} given X=sX=s.
Let

|  |  |  |
| --- | --- | --- |
|  | Zn(1)=Qn​(X,Un),Zn(2)=Qn​(X,1−Un),andZn+1=Zn(1)+Zn(2)2.Z\_{n}^{(1)}=Q\_{n}(X,U\_{n}),\quad Z\_{n}^{(2)}=Q\_{n}(X,1-U\_{n}),\quad\mbox{and}\quad Z\_{n+1}=\frac{Z\_{n}^{(1)}+Z\_{n}^{(2)}}{2}. |  |

Further, set Yn(i)=X+Zn(i)Y\_{n}^{(i)}=X+Z\_{n}^{(i)} for i∈{1,2}i\in\{1,2\}
and Yn=X+ZnY\_{n}=X+Z\_{n}.
It is clear that for n∈ℕn\in\mathbb{N}, Yn+1=(Yn(1)+Yn(2))/2Y\_{n+1}=(Y\_{n}^{(1)}+Y\_{n}^{(2)})/2.

By independence between UnU\_{n} and XX, we have that Zn(1)Z\_{n}^{(1)}, Zn(2)Z\_{n}^{(2)}, and ZnZ\_{n} have the same conditional distribution on X=sX=s for each s∈𝒮s\in\mathcal{S}, because they have the same conditional quantile function.
This implies
Yn(1)=dYn(2)=dYn,Y\_{n}^{(1)}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y\_{n}^{(2)}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y\_{n},
and moreover, (Yn(1),Yn(2))(Y\_{n}^{(1)},Y\_{n}^{(2)}) is exchangeable.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Zn+1∣X]=12​𝔼​[Zn(1)∣X]+12​𝔼​[Zn(2)∣X]=𝔼​[Zn∣X].\mathbb{E}[Z\_{n+1}\mid X]=\frac{1}{2}\mathbb{E}[Z\_{n}^{(1)}\mid X]+\frac{1}{2}\mathbb{E}[Z\_{n}^{(2)}\mid X]=\mathbb{E}[Z\_{n}\mid X]. |  |

By induction from 𝔼​[Z0∣X]=0\mathbb{E}[Z\_{0}\mid X]=0 we get 𝔼​[Zn∣X]=0\mathbb{E}[Z\_{n}\mid X]=0 for all nn.

Note that ‖Yn−X‖∞=‖Zn‖∞\|Y\_{n}-X\|\_{\infty}=\|Z\_{n}\|\_{\infty}. Using the same argument as in part (i) for ([7](https://arxiv.org/html/2601.04067v1#S4.E7 "In Proof. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")), we get that the length of the range of ZnZ\_{n} conditionally on X=sX=s for each s∈𝒮s\in\mathcal{S} shrinks 0. Since 𝒮\mathcal{S} is a finite set, this implies ‖Zn‖∞→0\|Z\_{n}\|\_{\infty}\to 0 as n→∞n\to\infty.
Because (Yn(1),Yn(2))(Y\_{n}^{(1)},Y\_{n}^{(2)}) is exchangeable and Yn+1=(Yn(1)+Yn(2))/2Y\_{n+1}=({Y\_{n}^{(1)}+Y\_{n}^{(2)}})/{2}, diversification on exchangeable pairs implies
Yn+1≿YnY\_{n+1}\succsim Y\_{n} for all n∈ℕ.n\in\mathbb{N}.
By the upper semicontinuity of ≿\succsim and ‖Yn−X‖∞=‖Zn‖∞→0\|Y\_{n}-X\|\_{\infty}=\|Z\_{n}\|\_{\infty}\to 0 as n→∞n\to\infty, we obtain
X≿Y0=X+Z0=Y,X\succsim Y\_{0}=X+Z\_{0}=Y, showing strong risk aversion.

For general XX that may take infinitely many values, we rely on the following simple lemma.

###### Lemma 1.

For X∈L∞X\in L^{\infty}, there exists a sequence of finitely valued random variables (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} such that

|  |  |  |
| --- | --- | --- |
|  | ‖Xn−X‖∞→0andXn⩾cvX​for all ​n∈ℕ.\|X\_{n}-X\|\_{\infty}\to 0\quad\text{and}\quad X\_{n}\geqslant\_{\mathrm{cv}}X\ \text{for all }n\in\mathbb{N}. |  |

###### Proof of the lemma.

For each n∈ℕn\in\mathbb{N}, let 𝒢n\mathcal{G}\_{n} be the finite σ\sigma-algebra generated by {X∈Ink}k=1,…,gn\{X\in I\_{n}^{k}\}\_{k=1,\dots,g\_{n}}, where (In1,…,Ingn)(I\_{n}^{1},\dots,I\_{n}^{g\_{n}}) is a finite partition of the support of XX into intervals of length at most 2−n2^{-n}, and define

|  |  |  |
| --- | --- | --- |
|  | Xn=𝔼​[X∣𝒢n].X\_{n}=\mathbb{E}[X\mid\mathcal{G}\_{n}]. |  |

Then XnX\_{n} is finitely valued and ‖Xn−X‖∞→0\|X\_{n}-X\|\_{\infty}\to 0. Moreover, Xn⩾cvXX\_{n}\geqslant\_{\rm cv}X for all n∈ℕn\in\mathbb{N} by the conditional Jensen’s inequality.
∎

Now we continue to prove Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"). Let the sequence (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} be as in Lemma [1](https://arxiv.org/html/2601.04067v1#Thmlemma1 "Lemma 1. ‣ Proof. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"). Transitivity of the concave order gives Xn⩾cvX⩾cvY.X\_{n}\geqslant\_{\rm cv}X\geqslant\_{\rm cv}Y.
Using the obtained result on finitely-valued random variables, we conclude Xn≿YX\_{n}\succsim Y for each nn. Applying the upper semicontinuity of ≿\succsim to the above relation with ‖Xn−X‖∞→0\|X\_{n}-X\|\_{\infty}\to 0, we get X≿YX\succsim Y, thus showing the desired statement of strong risk aversion.
∎

The most important direction in Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")
is (iii)⇒\Rightarrow(i), and it
generalizes
several results in the literature.
Chateauneuf and Lakhnati ([2007](https://arxiv.org/html/2601.04067v1#bib.bib4), Theorem 4.2) obtained that, under completeness, strict monotonicity, and compact continuity (essential to their proof),
diversification on ID pairs is equivalent to strong risk aversion.
Our result relaxes ID pairs to exchangeable pairs, remove completeness and monotonicity, and uses L∞L^{\infty}-upper semicontinuity that is weaker than compact continuity.
In the risk measure literature, L∞L^{\infty}-continuity is common and satisfied by all monetary risk measures.
Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") thus generalizes a classic result in the risk measure literature: A law-invariant convex and monetary risk measure on L∞L^{\infty} with the Fatou property exhibits strong risk aversion (Föllmer and Schied, [2016](https://arxiv.org/html/2601.04067v1#bib.bib12), Corollary 4.65).333The result was shown for coherent risk measures by Leitner ([2005](https://arxiv.org/html/2601.04067v1#bib.bib18)). The Fatou property can be omitted, which is first shown by Jouini et al. ([2006](https://arxiv.org/html/2601.04067v1#bib.bib16)) and then strengthened by Delbaen ([2012](https://arxiv.org/html/2601.04067v1#bib.bib10), Theorem 30).
Since convex risk measures satisfy ([5](https://arxiv.org/html/2601.04067v1#S3.E5 "In 3 Diversification and dependence ‣ Diversification Preferences and Risk Attitudes")), the above result is a special case of Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"). We present a corollary here, stronger than the existing results on risk measures, using the convex order.

###### Corollary 1.

A law-invariant mapping ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} satisfying lower semicontinuity and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(λ​X+(1−λ)​Y)⩽ρ​(X)​ for all X,Y∈L∞ with (X,Y)=d(Y,X) and λ∈[0,1]\rho(\lambda X+(1-\lambda)Y)\leqslant\rho(X)\mbox{ for all $X,Y\in L^{\infty}$ with $(X,Y)\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}(Y,X)$ and $\lambda\in[0,1]$} |  | (10) |

is increasing in the convex order.

###### Remark 3.

A simple sufficient condition for ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} to satisfy both law invariance and ([10](https://arxiv.org/html/2601.04067v1#S4.E10 "In Corollary 1. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")) is
ρ​(λ​X+(1−λ)​Y)⩽ρ​(X)​ for all X,Y∈L∞ with X=dY and λ∈[0,1].\rho(\lambda X+(1-\lambda)Y)\leqslant\rho(X)\mbox{ for all $X,Y\in L^{\infty}$ with $X\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y$ and $\lambda\in[0,1]$}.

For the EU model, weak and strong notions of risk aversion coincide, and hence Theorems [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")–[2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") together imply that diversification for antimonotonic pairs is equivalent to the concavity of the utility function, stated in Principi et al. ([2025](https://arxiv.org/html/2601.04067v1#bib.bib29), Theorem 7).

### 4.4 Independent pairs

We now consider diversification on independent pairs, whose implications on risk aversion depend on the continuity assumptions, as we will see from the results in this section.

###### Proposition 2.

For a risk preference, diversification on independent pairs
does not imply weak risk aversion. Indeed, the risk preference ≿\succsim represented by 𝒰\mathcal{U} via ([2](https://arxiv.org/html/2601.04067v1#S2.E2 "In 2 Preferences and risk aversion ‣ Diversification Preferences and Risk Attitudes")) with

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(X)=ess​-​sup​X,X∈L∞\mathcal{U}(X)=\mathrm{ess\mbox{-}sup}X,~~~X\in L^{\infty} |  |

exhibits diversification on independent pairs and strong risk seeking.

###### Proof.

It is clear that ≿\succsim exhibits strong risk seeking, because X⩾cvYX\geqslant\_{\rm cv}Y implies ess​-​sup​X⩽ess​-​sup​Y\mathrm{ess\mbox{-}sup}X\leqslant\mathrm{ess\mbox{-}sup}Y and thus X≾YX\precsim Y.
For X,YX,Y independent with X≃YX\simeq Y, we have

|  |  |  |
| --- | --- | --- |
|  | ess​-​sup​(λ​X+(1−λ)​Y)=λ​ess​-​sup​X+(1−λ)​ess​-​sup​Y=ess​-​sup​Y,\mathrm{ess\mbox{-}sup}(\lambda X+(1-\lambda)Y)=\lambda\mathrm{ess\mbox{-}sup}X+(1-\lambda)\mathrm{ess\mbox{-}sup}Y=\mathrm{ess\mbox{-}sup}Y, |  |

and hence
λ​X+(1−λ)​Y≃Y\lambda X+(1-\lambda)Y\simeq Y.
Therefore, ≿\succsim exhibits diversification on independent pairs.
∎

###### Remark 4.

Example [2](https://arxiv.org/html/2601.04067v1#Thmexample2 "Example 2 (Strong risk aversion \" ／\"⟹ diversification on AM). ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")
illustrates that strong risk aversion does not imply
diversification on independent pairs, noting that (X,Y)(X,Y) in that example is independent.
Together with Proposition [2](https://arxiv.org/html/2601.04067v1#Thmproposition2 "Proposition 2. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"), we see that these two concepts are incomparable.

###### Remark 5.

As we see in Proposition [1](https://arxiv.org/html/2601.04067v1#Thmproposition1 "Proposition 1. ‣ 4.1 Comonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"), diversification on comonotonic pairs is compatible with strict strong risk seeking in ([6](https://arxiv.org/html/2601.04067v1#S4.E6 "In 4.1 Comonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")).
In contrast, diversification on independent pairs conflicts with strict strong risk seeking.
To see this, take XX and YY independent and both following a uniform distribution on [0,1][0,1].
Diversification on independent pairs would imply X/2+Y/2≿YX/2+Y/2\succsim Y, and strict strong risk seeking would imply X/2+Y/2≺YX/2+Y/2\prec Y, conflicting each other.
That is why in Proposition [2](https://arxiv.org/html/2601.04067v1#Thmproposition2 "Proposition 2. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") we can only state strong risk aversion but not the strict version.

Our next result connects diversification on independent and ID pairs to strong risk aversion under compact upper semicontinuity, which is stronger than L∞L^{\infty}-upper semicontinuity and weaker than LpL^{p}-upper semicontinuity for any p∈[1,∞)p\in[1,\infty).

###### Theorem 3.

For a compact upper semicontinuous risk preference, diversification on independent and ID pairs implies weak risk aversion,
and it is implied by strong risk aversion.
Both implications are in general strict.

###### Proof.

The implication
that strong risk aversion implies diversification on independent and ID pairs
follows from Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"). We now show that diversification on independent and ID pairs implies weak risk aversion.
Let X∈L∞X\in L^{\infty} and (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} be a sequence of independent random variables with the same distribution as XX.
Write Sn=∑i=12nXiS\_{n}=\sum\_{i=1}^{2^{n}}X\_{i} for n∈ℕn\in\mathbb{N}.
By the law of large numbers, we have that Sn/2n→𝔼​[X]S\_{n}/2^{n}\to\mathbb{E}[X] almost surely. Note that Sn/2nS\_{n}/2^{n} is uniformly bounded, so Sn/2n→𝔼​[X]S\_{n}/2^{n}\to\mathbb{E}[X] in bounded convergence.
Diversification on independent and ID pairs implies Sn+1≿SnS\_{n+1}\succsim S\_{n} for n∈ℕn\in\mathbb{N}. Transitivity and compact upper semicontinuity of
≿\succsim give
𝔼​[X]≿Sn≿⋯≿S1≃X\mathbb{E}[X]\succsim S\_{n}\succsim\dots\succsim S\_{1}\simeq X.
Therefore, weak risk aversion holds.
Examples demonstrating that the converses of the two implications fail are given in Examples [3](https://arxiv.org/html/2601.04067v1#Thmexample3 "Example 3 (Diversification on IN \" ／\"⟹ strong risk aversion). ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") and [4](https://arxiv.org/html/2601.04067v1#Thmexample4 "Example 4 (Weak risk aversion \" ／\"⟹ diversification on IN and ID). ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"), respectively.
∎

###### Example 3 (Diversification on IN  ／⟹\mathchoice{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\displaystyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\textstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 2.625pt\kern-4.45831pt$\scriptstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 1.875pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\implies}}} strong risk aversion).

Define
𝒱​(X)=𝔼​[e2​X]/𝔼​[eX]\mathcal{V}(X)=\mathbb{E}[e^{2X}]/\mathbb{E}[e^{X}] for X∈L∞X\in L^{\infty},
and let the risk preference ≿\succsim be given by X⪰Y⟺𝒱​(X)⩽𝒱​(Y).X\succeq Y\Longleftrightarrow\mathcal{V}(X)\leqslant\mathcal{V}(Y).
It is straightforward to check that ≿\succsim satisfies compact continuity.
It also satisfies diversification on independent pairs by noting that
𝒱​(λ​X+(1−λ)​Y)⩽𝒱​(X)λ​𝒱​(Y)1−λ\mathcal{V}(\lambda X+(1-\lambda)Y)\leqslant\mathcal{V}(X)^{\lambda}\mathcal{V}(Y)^{1-\lambda} for X,YX,Y independent and λ∈[0,1]\lambda\in[0,1]; this follows from standard calculus.
Therefore, if X≃YX\simeq Y and X,YX,Y independent, then 𝒱​(λ​X+(1−λ)​Y)⩽𝒱​(Y)\mathcal{V}(\lambda X+(1-\lambda)Y)\leqslant\mathcal{V}(Y).
Finally, ≿\succsim does not exhibit strong risk aversion, with the counterexample (X,Y)(X,Y) specified by ℙ​(X=1)=ℙ​(X=−1)=ℙ​(Y=1)=1/2\mathbb{P}(X=1)=\mathbb{P}(X=-1)=\mathbb{P}(Y=1)=1/2 and ℙ​(Y=−3/2)=ℙ​(Y=−1/2)=1/4\mathbb{P}(Y=-3/2)=\mathbb{P}(Y=-1/2)=1/4, which satisfies X⩾cvYX\geqslant\_{\rm cv}Y and X≺YX\prec Y.

###### Example 4 (Weak risk aversion  ／⟹\mathchoice{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\displaystyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 3.75pt\kern-5.27776pt$\textstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 2.625pt\kern-4.45831pt$\scriptstyle\not$\hss}{\implies}}}{\mathrel{\hbox to0.0pt{\kern 1.875pt\kern-3.95834pt$\scriptscriptstyle\not$\hss}{\implies}}} diversification on IN and ID).

Consider the risk preference ≿\succsim exhibiting weak risk aversion given in Example [1](https://arxiv.org/html/2601.04067v1#Thmexample1 "Example 1 (Weak risk aversion \" ／\"⟹ diversification on AM and ID). ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"), represented by the utility functional 𝒰​(Z)=𝔼​[Z]−Var​(Z)​|2−Var​(Z)|\mathcal{U}(Z)=\mathbb{E}[Z]-\mathrm{Var}(Z)|2-\mathrm{Var}(Z)| for Z∈L∞Z\in L^{\infty}.
It is clear that ≿\succsim is compact continuous.
Let the distribution of XX be the same as in Example [1](https://arxiv.org/html/2601.04067v1#Thmexample1 "Example 1 (Weak risk aversion \" ／\"⟹ diversification on AM and ID). ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes"), that is, ℙ​(X=3)=1/3\mathbb{P}(X=3)=1/3 and ℙ​(X=0)=2/3\mathbb{P}(X=0)=2/3, XX and YY be independent and ID, and Z=(X+Y)/2Z=(X+Y)/2.
We can compute 𝔼​[X]=1\mathbb{E}[X]=1, Var​(X)=2\mathrm{Var}(X)=2, 𝔼​[Z]=1\mathbb{E}[Z]=1, and Var​(Z)=1\mathrm{Var}(Z)=1.
Therefore,
𝒰​(X)=1>0=𝒰​(Z),\mathcal{U}(X)=1>0=\mathcal{U}(Z),
violating diversification on independent and ID pairs.

### 4.5 Strict single-directional implications in Figure [1](https://arxiv.org/html/2601.04067v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Diversification Preferences and Risk Attitudes")

We now justify that the single-direction implications
in
Figure [1](https://arxiv.org/html/2601.04067v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Diversification Preferences and Risk Attitudes") are strict in general, using the abbreviations therein.
We have shown that diversification on AM pairs is incomparable to strong risk aversion (Remark [1](https://arxiv.org/html/2601.04067v1#Thmremark1 "Remark 1 (Diversification on AM \" ／\"⟹ strong risk aversion). ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") and Example [2](https://arxiv.org/html/2601.04067v1#Thmexample2 "Example 2 (Strong risk aversion \" ／\"⟹ diversification on AM). ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")),
and so is diversification on IN pairs (Remark [4](https://arxiv.org/html/2601.04067v1#Thmremark4 "Remark 4. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")). These observations and Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") imply that the three notions in the second row of Figure [1](https://arxiv.org/html/2601.04067v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Diversification Preferences and Risk Attitudes") are incomparable, and hence diversification on all pairs is strictly stronger than each of them.
The strictness of the implication from
diversification on ID pairs to diversification on AM (resp. IN) and ID pairs follows from Theorems [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") and [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") (resp. Theorems [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") and [3](https://arxiv.org/html/2601.04067v1#Thmtheorem3 "Theorem 3. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")).
The strictness of the implication from diversification on AM (resp. IN) and ID pairs to weak risk aversion is given in
Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") (resp. Theorem [3](https://arxiv.org/html/2601.04067v1#Thmtheorem3 "Theorem 3. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")).
The strictness of the implication from
diversification on AM (reps. IN) pairs to diversification on AM (resp. IN) and ID pairs is justified by the fact that the former is incomparable to strong risk aversion and the latter is implied by strong risk aversion.
The strict implication from strong to weak risk aversion is well known.

## 5 Neutrality

The opposite side of risk aversion is risk seeking, and a combination of both is risk neutrality.
Similarly, we can define the opposite of diversification preferences, and the corresponding neutrality.

###### Definition 3.

For 𝒳⊆(L∞)2\mathcal{X}\subseteq(L^{\infty})^{2}, a risk preference ≿\succsim exhibits
*anti-diversification on 𝒳\mathcal{X}* if

|  |  |  |  |
| --- | --- | --- | --- |
|  | X≃Y⟹X≿λ​X+(1−λ)​Y​ for all λ∈[0,1],X\simeq Y\implies X\succsim\lambda X+(1-\lambda)Y\mbox{ for all $\lambda\in[0,1]$}, |  | (11) |

and for all (X,Y)∈𝒳(X,Y)\in\mathcal{X}.
A risk preference exhibits *diversification neutrality* if both diversification and
anti-diversification hold.

Anti-diversification on different classes describes situations in which the decision maker does not wish to diversify.
By applying our results to the reverse relation of ≿\succsim, we can see that all results hold when we replace “risk aversion” with “risk seeking”
and “diversification” with “anti-diversification”.
Moreover,
combining our main results in the previous section, we obtain the following equivalence between various forms of neutrality. We will involve an additional assumption of *monotonicity (on constants)*:

|  |  |  |
| --- | --- | --- |
|  | x⩾y⟹x≿y for all x,y∈ℝ.x\geqslant y~\implies~x\succsim y\qquad\mbox{ for all $x,y\in\mathbb{R}$.} |  |

###### Theorem 4.

For a continuous risk preference ≿\succsim,
the following are equivalent:

1. (i)

   risk neutrality;
2. (ii)

   diversification neutrality on ID pairs;
3. (iii)

   diversification neutrality on exchangeable pairs;
4. (iv)

   diversification neutrality on antimonotonic and ID pairs.

If ≿\succsim is monotone, then each of the above is equivalent to

1. (v)

   diversification neutrality on all pairs;
2. (vi)

   diversification neutrality on antimonotonic pairs.

If ≿\succsim is monotone and compact continuous, then each of the above is equivalent to

1. (vii)

   diversification neutrality on independent pairs;
2. (viii)

   diversification neutrality on independent and ID pairs.

###### Proof.

(i)⇒\Rightarrow(ii): Risk neutrality implies 𝔼​[X]≃X\mathbb{E}[X]\simeq X for all X∈L∞X\in L^{\infty}. For X=dYX\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y and λ∈[0,1]\lambda\in[0,1],
we have
λ​X+(1−λ)​Y≃𝔼​[λ​X+(1−λ)​Y]=𝔼​[X]≃X,\lambda X+(1-\lambda)Y\simeq\mathbb{E}[\lambda X+(1-\lambda)Y]=\mathbb{E}[X]\simeq X,
and thus diversification neutrality on ID pairs holds. (ii)⇒\Rightarrow(iii)⇒\Rightarrow(iv): These follow by definition. (iv)⇒\Rightarrow(i): This follows by applying Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") to both ≿\succsim and ≾\precsim, and noting that weak risk aversion and weak risk seeking together imply risk neutrality.

Next, assume monotonicity.
(i)⇒\Rightarrow(v): For X≃YX\simeq Y and λ∈[0,1]\lambda\in[0,1] with 𝔼​[X]⩽𝔼​[Y]\mathbb{E}[X]\leqslant\mathbb{E}[Y]
we have

|  |  |  |
| --- | --- | --- |
|  | X≃𝔼​[X]⩽λ​X+(1−λ)​Y≃𝔼​[λ​X+(1−λ)​Y]⩽𝔼​[Y]≃Y≃X,X\simeq\mathbb{E}[X]\leqslant\lambda X+(1-\lambda)Y\simeq\mathbb{E}[\lambda X+(1-\lambda)Y]\leqslant\mathbb{E}[Y]\simeq Y\simeq X, |  |

and by transitivity of ≿\succsim diversification neutrality on all pairs holds.
(v)⇒\Rightarrow(vi)⇒\Rightarrow(iv): These follow by definition.

Finally, assume monotonicity and compact continuity.
(v)⇒\Rightarrow(vii)⇒\Rightarrow(viii): These follow by definition.
(viii)⇒\Rightarrow(i): This follows by applying Theorem [3](https://arxiv.org/html/2601.04067v1#Thmtheorem3 "Theorem 3. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") to both ≿\succsim and ≾\precsim and, again, noting that weak risk aversion and weak risk seeking together imply risk neutrality.
∎

If we assume
*strict monotonicity* for the risk preference ≿\succsim, that is,

|  |  |  |
| --- | --- | --- |
|  | x>y⟹x≻y for all x,y∈ℝ,x>y~\implies~x\succ y\qquad\mbox{ for all $x,y\in\mathbb{R}$,} |  |

then statements (i)–(vi) in Theorem [4](https://arxiv.org/html/2601.04067v1#Thmtheorem4 "Theorem 4. ‣ 5 Neutrality ‣ Diversification Preferences and Risk Attitudes")
are all equivalent to a representation of ≿\succsim by the mean, that is,
X≿Y⇔𝔼​[X]⩾𝔼​[Y].X\succsim Y\iff\mathbb{E}[X]\geqslant\mathbb{E}[Y].
The next example shows that monotonicity cannot be removed from the implications (i)⇒\Rightarrow(v)
and
(i)⇒\Rightarrow(vi)
in Theorem [4](https://arxiv.org/html/2601.04067v1#Thmtheorem4 "Theorem 4. ‣ 5 Neutrality ‣ Diversification Preferences and Risk Attitudes").

###### Example 5.

The risk preference ≿\succsim given by
X≿Y⇔(𝔼​[X])2⩾(𝔼​[Y])2X\succsim Y\iff(\mathbb{E}[X])^{2}\geqslant(\mathbb{E}[Y])^{2}
exhibits risk neutrality but it is not monotone.
It does not satisfy diversification for antimonotonic pairs because for XX with 𝔼​[X]≠0\mathbb{E}[X]\neq 0, we have
X≃−XX\simeq-X and 0=(X−X)/2≺X0=(X-X)/2\prec X.
Therefore, (i) in Theorem [4](https://arxiv.org/html/2601.04067v1#Thmtheorem4 "Theorem 4. ‣ 5 Neutrality ‣ Diversification Preferences and Risk Attitudes") holds but neither (v) nor (vi) does.

The risk preference represented by the essential supremum in Proposition [2](https://arxiv.org/html/2601.04067v1#Thmproposition2 "Proposition 2. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") satisfies diversification neutrality on independent pairs. This shows that the compact continuity assumed for the implication (viii)⇒\Rightarrow(i)
cannot be dispensed with.

## 6 Extension to unbounded random variables

In many financial applications concerning diversification,
the payoffs of assets are not necessarily bounded; see the textbook McNeil et al. ([2015](https://arxiv.org/html/2601.04067v1#bib.bib24)) for discussions on the empirical evidence.
The natural domain to define the two forms of risk aversion is L1L^{1}, as both notions require integrability of the random payoffs to compare.

All our main results can be naturally extended to law-invariant preference relations ≿\succsim on LpL^{p} for p∈[1,∞)p\in[1,\infty) with similar proof techniques, but the L∞L^{\infty}- and compact upper semicontinuity of ≿\succsim need to be strengthened to LpL^{p}-upper semicontinuity to accommodate convergence in the larger space. In this section, we show that the results in Theorems [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes")–[4](https://arxiv.org/html/2601.04067v1#Thmtheorem4 "Theorem 4. ‣ 5 Neutrality ‣ Diversification Preferences and Risk Attitudes") hold in the LpL^{p} setting under LpL^{p}-upper semicontinuity of ≿\succsim, following similar proof arguments with some manipulations.

For Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") in the LpL^{p} setting, we use the same construction of (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} as in the proof for the case of L∞L^{\infty}, and instead of Xn→𝔼​[X]X\_{n}\to\mathbb{E}[X] in L∞L^{\infty} we need to show Xn→𝔼​[X]X\_{n}\to\mathbb{E}[X] in LpL^{p}. This is guaranteed by Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes") below. To prove Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes"), we first present a standard result on the concave order and negative dependence.
We say that a pair (X1,X2)(X\_{1},X\_{2}) of random variables is *negatively quadrant dependent* (NQD, Lehmann, [1966](https://arxiv.org/html/2601.04067v1#bib.bib20)) if

|  |  |  |
| --- | --- | --- |
|  | ℙ​(X1⩽x1,X2⩽x2)⩽ℙ​(X1⩽x1)​ℙ​(X2⩽x2)​ for all x1,x2∈ℝ.\mathbb{P}(X\_{1}\leqslant x\_{1},X\_{2}\leqslant x\_{2})\leqslant\mathbb{P}(X\_{1}\leqslant x\_{1})\mathbb{P}(X\_{2}\leqslant x\_{2})\mbox{ for all $x\_{1},x\_{2}\in\mathbb{R}$}. |  |

Clearly, both independence and antimonotonicity belong to NQD, and indeed they have the largest and smallest ℙ​(X1⩽x1,X2⩽x2)\mathbb{P}(X\_{1}\leqslant x\_{1},X\_{2}\leqslant x\_{2}) satisfying the above inequality.

###### Lemma 2.

For random variables X1,X2,Y1,Y2∈L1X\_{1},X\_{2},Y\_{1},Y\_{2}\in L^{1} satisfying (X1,X2)(X\_{1},X\_{2}) NQD,
(Y1,Y2)(Y\_{1},Y\_{2}) independent, X1⩾cvY1X\_{1}\geqslant\_{\rm cv}Y\_{1}
and X2⩾cvY2X\_{2}\geqslant\_{\rm cv}Y\_{2}, we have
X1+X2⩾cvY1+Y2.X\_{1}+X\_{2}\geqslant\_{\rm cv}Y\_{1}+Y\_{2}.

###### Proof.

Take X1′=dX1X\_{1}^{\prime}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}X\_{1} and X2′=dX2X\_{2}^{\prime}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}X\_{2} such that (X1′,X2′)(X\_{1}^{\prime},X\_{2}^{\prime}) is independent. We have

|  |  |  |
| --- | --- | --- |
|  | X1+X2⩾cvX1′+X2′⩾cvY1+Y2,X\_{1}+X\_{2}\geqslant\_{\rm cv}X\_{1}^{\prime}+X\_{2}^{\prime}\geqslant\_{\rm cv}Y\_{1}+Y\_{2}, |  |

where the first inequality follows from the fact that for given marginal distributions, ordering in the bivariate distribution function implies the convex order of the sum (Müller and Stoyan, [2002](https://arxiv.org/html/2601.04067v1#bib.bib26), Theorem 3.8.2), and the second inequality follows from the closure property of the concave order under convolution (Shaked and Shanthikumar, [2007](https://arxiv.org/html/2601.04067v1#bib.bib34), Theorem 3.A.12).
∎

The next result gives an LpL^{p}-law of large numbers for negatively dependent sequences of ID random variables, which may be of some interest in probability theory.

###### Theorem 5.

For X∈LpX\in L^{p}, let
(Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} be a sequence satisfying X0=XX\_{0}=X and for n∈ℕn\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xn\displaystyle X\_{n} | =Xn−1(1)+Xn−1(2)2, where Xn−1(1)=dXn−1(2)=dXn−1 and (Xn−1(1),Xn−1(2)) is NQD.\displaystyle=\frac{X\_{n-1}^{(1)}+X\_{n-1}^{(2)}}{2},\mbox{ where $X\_{n-1}^{(1)}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}X\_{n-1}^{(2)}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}X\_{n-1}$ and $(X\_{n-1}^{(1)},X\_{n-1}^{(2)})$ is NQD}. |  |

Then Xn→𝔼​[X]X\_{n}\to\mathbb{E}[X] in LpL^{p}.

###### Remark 6.

We comment on a few special cases of Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes"). The case with independent (Xn−1(1),Xn−1(2))(X\_{n-1}^{(1)},X\_{n-1}^{(2)}) is a version of the LpL^{p}-law of large numbers for independent and ID sequences in LpL^{p}.
The construction of (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} with antimonotonic (Xn−1(1),Xn−1(2))(X\_{n-1}^{(1)},X\_{n-1}^{(2)}) appears in the proof of Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes").
We note that (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} is only specified in terms of its marginal distributions, and hence we cannot expect Xn→𝔼​[X]X\_{n}\to\mathbb{E}[X] almost surely.

###### Proof of Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes").

We will compare (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} with another sequence (Sn)n∈ℕ(S\_{n})\_{n\in\mathbb{N}} given by Sn=∑i=12nYi/2nS\_{n}=\sum\_{i=1}^{2^{n}}Y\_{i}/2^{n} for n∈ℕn\in\mathbb{N}, where (Yn)n∈ℕ(Y\_{n})\_{n\in\mathbb{N}} is an independent and ID sequence with the same distribution as XX.
Because X0=dS0X\_{0}\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}S\_{0}, we can apply Lemma [2](https://arxiv.org/html/2601.04067v1#Thmlemma2 "Lemma 2. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes") to get X1⩾cvS1X\_{1}\geqslant\_{\rm cv}S\_{1}. By induction on n∈ℕn\in\mathbb{N} and using Lemma [2](https://arxiv.org/html/2601.04067v1#Thmlemma2 "Lemma 2. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes") repeatedly, we get Xn⩾cvSnX\_{n}\geqslant\_{\rm cv}S\_{n} for all n∈ℕn\in\mathbb{N}.
Next, let us check that |Sn|p|S\_{n}|^{p} is uniformly integrable. Note that since Sn⩽cxXS\_{n}\leqslant\_{\rm cx}X
where ⩽cx\leqslant\_{\rm cx} is the convex order, we have that
(Sn)+p⩽icxX+p(S\_{n})\_{+}^{p}\leqslant\_{\rm icx}X\_{+}^{p},
where ⩽icx\leqslant\_{\rm icx} is the increasing convex order and (x)+=max⁡{x,0}(x)\_{+}=\max\{x,0\}; see e.g., Shaked and Shanthikumar ([2007](https://arxiv.org/html/2601.04067v1#bib.bib34), Theorem 4.A.15).
This implies that ((Sn)+p)n∈ℕ((S\_{n})\_{+}^{p})\_{n\in\mathbb{N}} is uniformly integrable by using Leskelä and Vihola ([2013](https://arxiv.org/html/2601.04067v1#bib.bib19), Theorem 1).
By a symmetric argument, ((−Sn)+p)n∈ℕ((-S\_{n})\_{+}^{p})\_{n\in\mathbb{N}} is also uniformly integrable. This shows (|Sn|p)n∈ℕ(|S\_{n}|^{p})\_{n\in\mathbb{N}} is uniformly integrable.
By the strong law of large numbers, Sn→𝔼​[X]S\_{n}\to\mathbb{E}[X] almost surely. Using the uniform integrability of (|Sn|p)n∈ℕ(|S\_{n}|^{p})\_{n\in\mathbb{N}} and Sn→𝔼​[X]S\_{n}\to\mathbb{E}[X], we get 𝔼​[|Sn−𝔼​[X]|p]→0\mathbb{E}[|S\_{n}-\mathbb{E}[X]|^{p}]\to 0 by Chung ([2001](https://arxiv.org/html/2601.04067v1#bib.bib7), Theorem 4.5.4).
Since x↦|x−𝔼​[X]|px\mapsto|x-\mathbb{E}[X]|^{p} is convex, we have 𝔼​[|Xn−𝔼​[X]|p]⩽𝔼​[|Sn−𝔼​[X]|p]→0\mathbb{E}[|X\_{n}-\mathbb{E}[X]|^{p}]\leqslant\mathbb{E}[|S\_{n}-\mathbb{E}[X]|^{p}]\to 0.
∎

Theorem [1](https://arxiv.org/html/2601.04067v1#Thmtheorem1 "Theorem 1. ‣ 4.2 Antimonotonic pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") in the LpL^{p} setting follows by using Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes") with antimonotonicity and the same proof arguments for the case of L∞L^{\infty}.
Theorem [2](https://arxiv.org/html/2601.04067v1#Thmtheorem2 "Theorem 2. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") in the LpL^{p} setting follows from the a similar argument, by using Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes") on the conditional distributions and replacing the L∞L^{\infty}-approximation in Lemma [1](https://arxiv.org/html/2601.04067v1#Thmlemma1 "Lemma 1. ‣ Proof. ‣ 4.3 Exchangeable pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") with an LpL^{p}-approximation. We omit the details here. The proof of
Theorem [3](https://arxiv.org/html/2601.04067v1#Thmtheorem3 "Theorem 3. ‣ 4.4 Independent pairs ‣ 4 Relations between diversification and risk aversion ‣ Diversification Preferences and Risk Attitudes") in the LpL^{p} setting follows by applying Theorem [5](https://arxiv.org/html/2601.04067v1#Thmtheorem5 "Theorem 5. ‣ 6 Extension to unbounded random variables ‣ Diversification Preferences and Risk Attitudes") with independence
and and the same proof arguments for the case of L∞L^{\infty}. The proof of Theorem [4](https://arxiv.org/html/2601.04067v1#Thmtheorem4 "Theorem 4. ‣ 5 Neutrality ‣ Diversification Preferences and Risk Attitudes") in the LpL^{p}
setting carries over verbatim.

## 7 Conclusion

The results in this paper show that one can recover rich information about risk attitudes from relatively modest diversification principles, provided they are formulated on economically meaningful classes of pairs such as antimonotonic, exchangeable, and independent risks.
The main obtained relations are summarized in Figure [1](https://arxiv.org/html/2601.04067v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Diversification Preferences and Risk Attitudes").
Especially, if a decision maker prefers to combine antimonotonic risks, as in hedging or purchasing insurance, then weak risk aversion can be deduced; if they prefer to combine exchangeable risks, as in pooling similar assets, then strong risk aversion can be deduced.
Our counterexamples highlight the limits of diversification as a diagnostic for risk aversion, and they underscore the role played by law invariance, continuity, and completeness assumptions in existing axiomatic frameworks.

## References

* Aouani et al. (2021)
   Aouani, Z., Chateauneuf, A., and Ventura, C. (2021). Propensity for hedging and ambiguity aversion. *Journal of Mathematical Economics*, 97, 102543.
* Arrow (1963)

  Arrow, K. J. (1963). Uncertainty and the welfare economics of medical care. *American Economic Review*, 53(5), 941–973.
* Cerreia-Vioglio et al. (2011)

  Cerreia-Vioglio, S., Maccheroni, F., Marinacci, M. and Montrucchio, L. (2011). Risk measures:
  Rationality and diversification. *Mathematical Finance*, 21(4), 743–774.
* Chateauneuf and Lakhnati (2007)

  Chateauneuf, A. and Lakhnati, G. (2007). From sure to strong diversification. *Economic Theory*, 32(3), 511–522.
* Chateauneuf and Tallon (2002)

  Chateauneuf, A. and Tallon, J. M. (2002). Diversification, convex preferences and non-empty core in the Choquet expected utility model. *Economic Theory*, 19(3), 509–523.
* Chew and Mao (1995)

  Chew, S. and Mao, M. (1995). A Schur concave characterization of risk aversion for non-expected utility preferences. *Journal of Economic Theory*, 67(2), 402–435.
* Chung (2001)

  Chung, K. L. (2001).  *A Course in Probability Theory*. Third Edition. Academic Press, London, UK.
* Cohen (1995)

  Cohen, M. D. (1995). Risk-aversion concepts in expected- and non-expected-utility models. *Geneva Papers on Risk and Insurance Theory*, 20(1), 73–91.
* Dekel (1989)

  Dekel, E. (1989). Asset demand without the independence axiom. *Econometrica*, 57, 163–169.
* Delbaen (2012)

  Delbaen, F. (2012). *Monetary Utility Functions*. Osaka University Press, Osaka.
* Embrechts et al. (2015)
   Embrechts, P., Wang, B. and Wang, R. (2015). Aggregation-robustness and model uncertainty of regulatory risk measures. Finance and Stochastics, 19(4), 763–790.
* Föllmer and Schied (2016)
   Föllmer, H. and Schied, A. (2016). *Stochastic Finance. An Introduction in Discrete Time*. Fourth Edition. Walter de Gruyter, Berlin.
* Ghossoub et al. (2025)
   Ghossoub, M., Ren, Q., and Wang, R. (2025).
  Counter-monotonic risk allocations and distortion risk measures.
  *Scandinavian Actuarial Journal*, forthcoming.
* Han et al. (2024)

  Han, X., Wang, B., Wang, R. and Wu, Q. (2024). Risk concentration and the mean-Expected Shortfall criterion. *Mathematical Finance*, 34(3), 819–846.
* Joe (1997)

  Joe, H. (1997).
  Multivariate Models and Dependence Concepts.
  Chapman & Hall, London.
* Jouini et al. (2006)

  Jouini, E., Schachermayer, W. and Touzi, N. (2006). Law invariant risk measures have the Fatou property. *Advances in Mathematical Economics*, 9, 49–71.
* Lauzier et al. (2025)

  Lauzier, J.-G., Lin, L. and Wang, R. (2025). Risk sharing, measuring variability, and distortion riskmetrics. Mathematical Finance, forthcoming.
* Leitner (2005)

  Leitner, J. (2005). A short note on second-order stochastic dominance preserving coherent risk
  measures. *Mathematical Finance* 15(4), 649–651.
* Leskelä and Vihola (2013)

  Leskelä, L. and Vihola, M. (2013). Stochastic order characterization of uniform integrability and tightness. *Statistics and Probability Letters*, 83(1), 382–389.
* Lehmann (1966)

  Lehmann, E. L. (1966). Some concepts of dependence. *Annals of Mathematical Statistics*, 37(5), 1137–1153.
* Maccheroni et al. (2025)

  Maccheroni, F., Marinacci, M., Wang, R. and Wu, Q. (2025). Risk aversion and insurance propensity. *American Economic Review*, 115(5), 1597–1649.
* Mao and Wang (2020)

  Mao, T. and Wang, R. (2020). Risk aversion in regulatory capital calculation. *SIAM Journal on Financial Mathematics*, 11(1), 169–200.
* Markowitz (1952)

  Markowitz, H. (1952). Portfolio selection. *Journal of Finance*, 7(1), 77–91.
* McNeil et al. (2015)

  McNeil, A. J., Frey, R. and Embrechts, P. (2015). *Quantitative
  Risk Management: Concepts, Techniques and Tools*. Revised Edition. Princeton, NJ:
  Princeton University Press.
* Mu et al. (2024)

  Mu, X., Pomatto, L., Strack, P. and Tamuz, O. (2024). Monotone additive statistics. *Econometrica*, 92(4), 995–1031.
* Müller and Stoyan (2002)
   Müller, A. and Stoyan, D. (2002). *Comparison Methods for Stochastic Models and Risks*. Wiley, England.
* Pomatto et al. (2020)

  Pomatto, L., Strack, P. and Tamuz, O. (2020). Stochastic dominance under independent noise. *Journal of Political Economy*, 128(5), 1877–1900.
* Pratt (1964)

  Pratt, J. W. (1964). Risk aversion in the small and in the large. *Econometrica*, 32, 122–136.
* Principi et al. (2025)

  Principi, G., Wakker, P. and Wang, R. (2025). Anticomonotonicity for preference axioms: The natural counterpart to comonotonicity. *Theoretical Economics*, 20(3), 831–855.
* Rostek (2010)

  Rostek, M. (2010).
  Quantile maximization in
  decision theory. *Review of Economic Studies*, 77, 339–371.
* Rothschild and Stiglitz (1970)

  Rothschild, M. and Stiglitz, J. E. (1970). Increasing risk: I. A definition. *Journal of Economic Theory*, 2(3), 225–243.
* Schmeidler (1989)

  Schmeidler, D. (1989). Subjective probability and expected utility without additivity.
  *Econometrica*, 57(3), 571–587.
* Schmidt and Zank (2008)

  Schmidt, U. and Zank, H. (2008). Risk aversion in cumulative prospect theory. *Management Science*, 54, 208–216.
* Shaked and Shanthikumar (2007)
   Shaked, M. and Shanthikumar, J. G. (2007). *Stochastic
  Orders*. Springer Series in Statistics.
* Strassen (1965)
   Strassen, V. (1965). The existence of probability measures with given marginals. *Annals of Mathematical Statistics*, 36(2), 423–439.
* Yaari (1987)

  Yaari, M. E. (1987). The dual theory of choice under risk. *Econometrica*, 55(1), 95–115.