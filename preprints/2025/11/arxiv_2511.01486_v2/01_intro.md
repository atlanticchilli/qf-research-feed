---
authors:
- Karen Grigorian
- Robert Jarrow
doc_id: arxiv:2511.01486v2
family_id: arxiv:2511.01486
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Differential Beliefs in Financial Markets Under Information Constraints: A
  Modeling Perspective'
url_abs: http://arxiv.org/abs/2511.01486v2
url_html: https://arxiv.org/html/2511.01486v2
venue: arXiv q-fin
version: 2
year: 2025
---


Karen Grigorian
Department of Statistics and Applied Probability, University of California Santa Barbara; grigorian@ucsb.edu
  
Robert A. Jarrow
Samuel Curtis Johnson Graduate School of Management, Cornell University; robertjarrow@cornell.edu

(November 4, 2025)

###### Abstract

We apply the theory of McKean-Vlasov-type SDEs to study several problems related to market efficiency in the context of partial information and partially observable financial markets: (i) convergence of reduced-information market price processes to the true price process under an increasing information flow; (ii) a specific mechanism of shrinking biases under increasing information flows; (iii) optimal aggregation of expert opinions by a trader seeking a positive alpha. All these problems are studied by means of (conditional) McKean-Vlasov-type SDEs, Wasserstein barycenters, KL divergence and relevant tools from convex optimization, optimal control and nonlinear filtering. We supply the theoretical results in (i)-(iii) with concrete simulations demonstrating how the proposed models can be applied in practice to model financial markets under information constraints and the arbitrage-seeking behavior of traders with differential beliefs.

Keywords: differential beliefs; partially observable financial markets; McKean–Vlasov SDE; Wasserstein distance; Wasserstein barycenter; nonlinear filtering; measure–valued control.
  
MSC 2020: 49K45; 60H10; 93E11; 91G80.

## 1 Introduction

Our general goal is to study the interplay between the notions of market efficiency, partial information and partial observability from a modeling perspective. This is accomplished in a sequence of three successively more specialized models which, as we show, are highly amenable to practical implementation and simulation.

The original inspiration for some of the suggested models came from several examples of model uncertainty presented in [[31](https://arxiv.org/html/2511.01486v2#bib.bib31)] and the interesting application of the notion of barycenters in [[26](https://arxiv.org/html/2511.01486v2#bib.bib26)], as well as the authors’ own published research [[18](https://arxiv.org/html/2511.01486v2#bib.bib18), [19](https://arxiv.org/html/2511.01486v2#bib.bib19), [20](https://arxiv.org/html/2511.01486v2#bib.bib20), [21](https://arxiv.org/html/2511.01486v2#bib.bib21), [22](https://arxiv.org/html/2511.01486v2#bib.bib22), [23](https://arxiv.org/html/2511.01486v2#bib.bib23), [28](https://arxiv.org/html/2511.01486v2#bib.bib28)] which naturally suggested a deeper study of financial markets under information constraints.

In the first application, the most general setting, we propose a model
based on a McKean-Vlasov-type stochastic differential equation (MKVSDE)
with a barycentric measure input that explicitly describes how increasing
information flows impact stock prices and market efficiency. Here,
we first construct a hypothetical market with price SS that satisfies
No Free Lunch with Vanishing Risk (NFLVR) and No Dominance (ND) with
respect to the information set 𝔽\mathbb{F}, which represents all
the information available in the market. These properties imply that
there exists an equivalent martingale measure (EMM) with respect to
𝔽\mathbb{F} in the hypothetical market, see [[27](https://arxiv.org/html/2511.01486v2#bib.bib27)] for the
definitions of NFLVR, ND, and EMM and the stated theorems. Using the
definition of an efficient market as in Jarrow and Larsson [[28](https://arxiv.org/html/2511.01486v2#bib.bib28)],
by construction, this hypothetical market is efficient with respect
to 𝔽\mathbb{F} in the sense of strong-form efficiency [[27](https://arxiv.org/html/2511.01486v2#bib.bib27)],
Ch.16.

Next, we consider a sequence of actual markets, indexed by nn. The
markets differ by the private information available to the mm traders,
indexed by ii, and denoted 𝔾i,n⊂𝔽\mathbb{G}^{i,n}\subset\mathbb{F}.
We assume that the true price process SS is not
observable in the actual market, hence it is not 𝔾i,n\mathbb{G}^{i,n}-adapted. We call it the true market price because it is the market
price that would exist if all the traders knew 𝔽\mathbb{F}. For
the actual market, the total information available (in the sense of strong-form
efficiency) is ℍn:=\slimits@i=1m​𝔾i,n\mathbb{H}^{n}:=\bigveeop\slimits@\_{i=1}^{m}\mathbb{G}^{i,n}.
The market price for the stock in the actual market is denoted Stilden\tilde{S}^{n}.

For the actual market with price Stilden\tilde{S}^{n}, we no longer assume
that there exist an EMM ℚtilde\mathbb{\tilde{Q}}, hence the actual market
may violate either NFLVR or ND. It follows that the actual market
may be inefficient with respect to ℍn\mathbb{H}^{n}. We show that
as the information increases in a market, i.e. ℍn↑𝔽\mathbb{H}^{n}\uparrow\mathbb{F},
the actual markets approach the hypothetical market that satisfies
NFLVR and ND, i.e. they approach an efficient market with respect
to 𝔽\mathbb{F}.

The second and third applications studied are motivated by the observation
that in financial markets, traders (hedge funds, investment and commercial
banks, pension funds, insurance companies) use different factor models
to identify mispriced securities looking for arbitrage opportunities
(see Jarrow and Protter [[29](https://arxiv.org/html/2511.01486v2#bib.bib29)]), this is called “the
search for positive alphas.” The search for positive
alphas is the search for a security’s “true” drift (expected return).

For the second application, using the same market set-up as in the
first application, the nnth market may not satisfy NFLVR or ND
with respect to 𝔾n\mathbb{G}^{n}. Here, we represent the search for
positive alphas by a single trader using their private information
to estimate the drift of the actual market price. We study how increasing
this information impacts the market price process. We show that the
search for a positive alpha removes FLVR and dominated assets in the
market, thereby increasing market efficiency.

Finally, in the third application, we study an optimal aggregation problem where a trader seeking arbitrage opportunities (positive alphas) is acting under information constraints 𝔾⊂𝔽\mathbb{G}\subset\mathbb{F} and consults a (possibly continuous) set of experts , who propose corrections to the observed drift, represented by expert-indexed random field ρλ\rho^{\lambda}, which the trader wishes to aggregate to obtain the best estimate of the unknown true drift aa. The trader tries to minimize the distance between the aggregated correction term ρbar\bar{\rho} and the trader’s own estimate a^\mathaccent 866{a} based on available information 𝔾\mathbb{G}, taking into account their own prior beliefs on the expert community, represented by a flow π\pi of probability measures over . Here as well, we have that the hypothetical market with price SS satisfies NFLVR and
ND and is efficient with respect to 𝔽\mathbb{F}.
As in the preceding case, we now no longer assume that there exist an EMM ℚtilde\mathbb{\tilde{Q}} for the market price Stilde\tilde{S} in the actual market, hence the actual market may violate either NFLVR or ND. It follows that the actual market may be inefficient with respect to 𝔾\mathbb{G}.

This analysis begins from purely financial arguments, and eventually arrives at well-known variational formulas for KL divergence, exponential tilting, and KL-regularized decision/control.
The Gibbs measure form of the optimizer follows from the variational characterization of log-partition functions and the Donsker–Varadhan (DV) variational principle for relative entropy; see standard treatments of large deviations [[33](https://arxiv.org/html/2511.01486v2#bib.bib33), [13](https://arxiv.org/html/2511.01486v2#bib.bib13), [14](https://arxiv.org/html/2511.01486v2#bib.bib14), [11](https://arxiv.org/html/2511.01486v2#bib.bib11)].
The geometry of II–projections (KL projections) onto convex sets under linear constraints is classical and gives exponential-family solutions closely related to our characterization, see [[12](https://arxiv.org/html/2511.01486v2#bib.bib12)].

KL-based distributionally robust optimization (DRO) provides another close analogue: worst-case expectations over a KL-ball ambiguity set admit dual solutions that are exponential tilts of the nominal distribution, similar to our optimal Gibbs measure-valued controls and KL constraints, see [[25](https://arxiv.org/html/2511.01486v2#bib.bib25)].

Aggregation and opinion pooling also often lead to exponential reweighting. The logarithmic opinion pool and its characterizations (and weighting schemes) provide aggregation rules that formally coincide with our optimal Gibbs measures, but most commonly use KL-barycetners, see, e.g., [[24](https://arxiv.org/html/2511.01486v2#bib.bib24), [17](https://arxiv.org/html/2511.01486v2#bib.bib17)]. However, the core ideas of this paper are inherently financial in nature and admit very explicit interpretation in the context of partial information and partially observable financial markets. We end each section with explicit simulations showing how the proposed models can be applied in finance.

We acknowledge the use of ChatGPT 5 Pro in obtaining the code for simulations as well as in testing out a large number of model hypotheses which often led to dead ends, and hence expediting the creative part of research. It helped with transferring handwritten notes to LaTex, and finding connections to information theory. It also suggested proof strategies and arguments in several technical lemmas and propositions that eventually worked after our guided fixing and helping it identify its own errors. While in most of these cases we continually steered it away from erroneous suggestions and arguments, it was very helpful nevertheless and saved from hours of cumbersome work.

The paper is structured as follows: section 2 introduces a general McKean-Vlasov-type SDE-based model of price dynamics affected by traders’ beliefs and studies the convergence of a sequence of reduced-information markets to the market with full information; section 3 proposes a specialized model to analyze the evolution of individual biases under increasing information; section 4 investigates the problem of optimal aggregation of experts’ opinions by a trader seeking to find an arbitrage opportunity or a dominated asset; section 5 concludes, and the appendix contains some well-known facts about the measurability properties of flows of probability kernels.

## 2 Differential Beliefs and Convergence to an Efficient Market

### 2.1 Preliminaries and Model Set-Up

We study a financial market supported on some complete filtered probability space (,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}) endowed with a filtration 𝔽=(ℱt)t∈[0,T]\mathbb{F}=(\mathcal{F}\_{t})\_{t\in[0,T]} for a fixed finite horizon T>0T>0 which satisfies the usual conditions. Let WW be a DD–dimensional 𝔽\mathbb{F}–Brownian motion. The dd–dimensional *true price* process SS is the 𝔽\mathbb{F}–adapted Markov diffusion

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=bbar​(t,St)​d​t+σbar​(t,St)​d​Wt,S0∈L2,𝔼​[supt≤T|St|2]<∞,dS\_{t}=\bar{b}(t,S\_{t})\,dt+\bar{\sigma}(t,S\_{t})\,dW\_{t},\qquad S\_{0}\in L^{2},\qquad\mathbb{E}\Big[\sup\_{t\leq T}|S\_{t}|^{2}\Big]<\infty, |  | (2.1) |

where bbar:[0,T]×ℝd→ℝd\bar{b}:[0,T]\times\mathbb{R}^{d}\to\mathbb{R}^{d} and σbar:[0,T]×ℝd→ℝd×D\bar{\sigma}:[0,T]\times\mathbb{R}^{d}\to\mathbb{R}^{d\times D} satisfy the usual global Lipschitz and linear–growth conditions ensuring well–posedness.

The true price process SS is not fully observable and each of the mm traders has access to their respective information flow defined by a right–continuous, complete subfiltration 𝔾i,n=(𝒢ti,n)t∈[0,T]\mathbb{G}^{i,n}=(\mathcal{G}^{i,n}\_{t})\_{t\in[0,T]} of 𝔽\mathbb{F}, i∈{1,…,m},n∈ℕi\in\{1,\dots,m\},n\in\mathbb{N} fixed, which determines their individual opinions/proposals on the drift and volatility, assumed to be some functions of the flows πi\pi^{i} of conditional distributions of the price process given their respective information flow. Thus, for each (i,n)(i,n) and t∈[0,T]t\in[0,T], the *i*th *trader’s beliefs* are given by

|  |  |  |
| --- | --- | --- |
|  | πti,n:=ℒ​(St​𝒢ti,n),\pi\_{t}^{i,n}:=\mathcal{L}(S\_{t}\mid\mathcal{G}\_{t}^{i,n}), |  |

the conditional law of StS\_{t} given 𝒢ti,n\mathcal{G}^{i,n}\_{t}, i.e. a 𝒫2​(ℝd)\mathcal{P}\_{2}(\mathbb{R}^{d})-valued random variable, where 𝒫2​(ℝd)\mathcal{P}\_{2}(\mathbb{R}^{d}) is the set of all probability measures on ℝd\mathbb{R}^{d} with finite second moments.

We stress that the traders have different conditional beliefs, given their information, and the conditional law is based on the statistical probability measure ℙ\mathbb{P}. When only drifts are affected by the views, this is not a serious restriction and, with obvious modifications of the arguments below, the results can easily be generalized to the case when the the individual conditional laws also depend on the traders’ probability measures
ℙi\mathbb{P}^{i} that are equivalent to ℙ\mathbb{P}, and hence the drifts can be changed by Girsanov’s theorem. When volatilities are affected, the argument has to be refined, see [[26](https://arxiv.org/html/2511.01486v2#bib.bib26)] for one approach.

The market combines their respective beliefs into a single price process Stilde\tilde{S}, whose drift and volatility depend on the barycenter of the mm traders’ views, denoted by πtilde\tilde{\pi}. Hence, the total available information in the market is

|  |  |  |
| --- | --- | --- |
|  | ℍn:=\slimits@i=1m​𝔾i,n,ℋtn:=\slimits@i=1m​𝒢ti,n.\mathbb{H}^{n}:=\bigveeop\slimits@\_{i=1}^{m}\mathbb{G}^{i,n},\qquad\mathcal{H}\_{t}^{n}:=\bigveeop\slimits@\_{i=1}^{m}\mathcal{G}\_{t}^{i,n}. |  |

The aggregate belief of the market, called the *market beliefs*,
is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πtildetn∈argminν∈𝒫2​(ℝd)​\slimits@i=1m​wi,t(n)​W22​(ν,πti,n),wi,t(n)>0,t∈[0,T],\tilde{\pi}\_{t}^{\,n}\in\text{argmin}\_{\nu\in\mathcal{P}\_{2}(\mathbb{R}^{d})}\ \sumop\slimits@\_{i=1}^{m}w\_{i,t}^{(n)}\,W\_{2}^{2}\big(\nu,\pi\_{t}^{i,n}\big),\qquad w\_{i,t}^{(n)}>0,\qquad t\in[0,T], |  | (2.2) |

where W2W\_{2} is the 2-Wasserstein distance between two probability measures. Thus, ([2.2](https://arxiv.org/html/2511.01486v2#S2.E2 "Equation 2.2 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) is the standard Wasserstein barycenter of probability measures, see [[1](https://arxiv.org/html/2511.01486v2#bib.bib1)] for details on existence and properties. Existence of minimizers for ([2.2](https://arxiv.org/html/2511.01486v2#S2.E2 "Equation 2.2 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) is classical for a finite family of inputs in (𝒫2​(ℝd),W2)(\mathcal{P}\_{2}(\mathbb{R}^{d}),W\_{2}), and, assuming the individual flows of measures are 𝔾i,n\mathbb{G}^{i,n}-progressively measurable, by a measurable selection theorem one may choose (t,ω)↦πtildetn​(ω)(t,\omega)\mapsto\tilde{\pi}^{\,n}\_{t}(\omega) to be ℍn\mathbb{H}^{n}–progressively measurable. The argument is nontrivial, but standard and rests on checking the properties of normal integrands and using a measurable selection theorem, as in [[32](https://arxiv.org/html/2511.01486v2#bib.bib32)], Thm. 14.37. Thus, our market beliefs are represented by the minimizer of a weighted average of W2W\_{2}-distances to the traders’ beliefs. The weights wi,t(n)>0w\_{i,t}^{(n)}>0
imply that each trader has a positive impact on the market beliefs. This condition and the technical assumption of at least one of the measures πti,n\pi\_{t}^{i,n} being absolutely continuous wrt the Lebesgue measure ensure the uniqueness of the barycenter measure πtildetn\tilde{\pi}\_{t}^{\,n}, [[1](https://arxiv.org/html/2511.01486v2#bib.bib1)] Prop. 3.5. Our analysis, however, does not rely on uniqueness and only requires the existence of one such measure.

The weight selection mechanism is not explicitly given. However, intuitively
it is generated by each trader’s market impact on prices either through
the magnitude of the trader’s trade size or the trader’s influence
on the market via media communication and online followers (e.g. Warren
Buffet).

We define the *market price* to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Stildet(n)=b​(t,Stildet(n),πtildetn)​d​t+σ​(t,Stildet(n),πtildetn)​d​Wt,Stilde0(n)=S0,d\tilde{S}\_{t}^{(n)}=b\big(t,\tilde{S}\_{t}^{(n)},\tilde{\pi}\_{t}^{\,n}\big)\,dt+\sigma\big(t,\tilde{S}\_{t}^{(n)},\tilde{\pi}\_{t}^{\,n}\big)\,dW\_{t},\qquad\tilde{S}\_{0}^{(n)}=S\_{0}, |  | (2.3) |

driven by the *same* Brownian motion WW. This assumption is not restrictive and will be relaxed in the subsequent sections. We adopt it in this section to focus our analysis on the pure impact of differential beliefs. We assume the Lipschitz and linear–growth conditions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | L≥1s.t.t∈[0,T],x,y∈ℝd,μ,ν∈𝒫2(ℝd):\displaystyle\exists L\geq 1\ \text{s.t.}\ \forall t\in[0,T],\ x,y\in\mathbb{R}^{d},\ \mu,\nu\in\mathcal{P}\_{2}(\mathbb{R}^{d}): |  | (2.4) |
|  |  | |b​(t,x,μ)−b​(t,y,ν)|+\|​σ​(t,x,μ)−σ​(t,y,ν)​\|≤L​(|x−y|+W2​(μ,ν)),\displaystyle\quad|b(t,x,\mu)-b(t,y,\nu)|+\|\sigma(t,x,\mu)-\sigma(t,y,\nu)\|\ \leq\ L\big(|x-y|+W\_{2}(\mu,\nu)\big), |  |
|  |  | |b​(t,x,μ)|2+\|​σ​(t,x,μ)​\|2≤L​(1+|x|2+\ilimits@​|z|2​μ​(d​z)),\displaystyle\quad|b(t,x,\mu)|^{2}+\|\sigma(t,x,\mu)\|^{2}\ \leq\ L\big(1+|x|^{2}+\intslop\ilimits@|z|^{2}\,\mu(dz)\big), |  |

together with the *compatibility condition* linking ([2.1](https://arxiv.org/html/2511.01486v2#S2.E1 "Equation 2.1 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and ([2.3](https://arxiv.org/html/2511.01486v2#S2.E3 "Equation 2.3 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | bbar​(t,x)=b​(t,x,δx),σbar​(t,x)=σ​(t,x,δx),(t,x)∈[0,T]×ℝd.\bar{b}(t,x)=b\big(t,x,\delta\_{x}\big),\qquad\bar{\sigma}(t,x)=\sigma\big(t,x,\delta\_{x}\big),\qquad\forall(t,x)\in[0,T]\times\mathbb{R}^{d}. |  | (2.5) |

Under ([2.4](https://arxiv.org/html/2511.01486v2#S2.E4 "Equation 2.4 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), ([2.3](https://arxiv.org/html/2511.01486v2#S2.E3 "Equation 2.3 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) is well–posed and 𝔼​supt≤T|Stildet(n)|2<∞\mathbb{E}\sup\_{t\leq T}|\tilde{S}^{(n)}\_{t}|^{2}<\infty.

The true price is the market price that would exist if all the traders knew 𝔽\mathbb{F}. 𝔽\mathbb{F} represents all the available information in the sense of strong form efficiency [[27](https://arxiv.org/html/2511.01486v2#bib.bib27)], Ch.16.

We consider a sequence of markets, indexed by nn. The markets differ by the information available to the mm traders, indexed by ii with private information 𝔾i,n⊂𝔽\mathbb{G}^{i,n}\subset\mathbb{F}. We want to study how increasing the information available to traders impacts market efficiency, i.e. the convergence of prices as n→∞n\rightarrow\infty.

The mechanism that generates the market price based on the trader’s
beliefs and trading strategies is outside the model’s structure. This
is a “reduced form” model. This contrasts with a “structural
model” that determines the market price given a specification of
each trader’s endowments, portfolio and consumption optimization problem,
and market clearing mechanism. In the classical asset pricing literature,
this is given by a Radner equilibrium. In the market microstructure
literature, this would be based on a Nash equilibrium.

We note that our reduced form specification of the price process is consistent with these structural models, and possibly other market clearing mechanisms. However, the converse is also true. The
market price process need not be an equilibrium price with respect
to the standard paradigms mentioned above.

We assume that the filtration generated by Stildet(n)\tilde{S}\_{t}^{(n)}
is contained in ℍn\mathbb{H}^{n}. Thus, we have constructed two markets: a hypothetical market with price SS and
the actual market with price Stilde\tilde{S}. We assume that these markets
have the standard asset pricing structure, trading strategies, etc.
as in [[28](https://arxiv.org/html/2511.01486v2#bib.bib28)]. We assume that there exists an equivalent martingale measure
(EMM) ℚ\mathbb{Q} for the true price SS in the hypothetical market
constructed above. This hypothetical market satisfies No Free Lunch with Vanishing Risk (NFLVR) and No Dominance (ND), see [[27](https://arxiv.org/html/2511.01486v2#bib.bib27)].
The EMM need not be unique, so the hypothetical market can be incomplete.

Using the definition of an efficient market in Jarrow and Larsson
[[28](https://arxiv.org/html/2511.01486v2#bib.bib28)], the hypothetical market is efficient with respect to 𝔽\mathbb{F}, i.e. it is strong-form efficient.
It is also efficient with respect to smaller information sets, so
it is semi-strong form and weak-form efficient as well. Hence, it is the ideal market.

We do not assume that there exists an EMM ℚtilde\mathbb{\tilde{Q}}
for the market price Stilde\tilde{S} in the actual market constructed
above. Hence, the actual market may violate either NFLVR or ND. If it exists, the EMM need not
be unique, so the actual market can be incomplete. By the definition
of an efficient market in [[28](https://arxiv.org/html/2511.01486v2#bib.bib28)], the actual
market may be inefficient with respect to ℍn\mathbb{H}^{n}, and is efficient
with respect to 𝔽\mathbb{F} if for some finite nn

|  |  |  |
| --- | --- | --- |
|  | Stilde(n)=S.\tilde{S}^{(n)}=S. |  |

In our case, the actual market may be inefficient with respect to ℍn\mathbb{H}^{n}, and is inefficient with respect to 𝔽\mathbb{F}. In the actual market, the information from 𝔽\mathbb{F} could generate
arbitrage opportunities, as discussed in [[23](https://arxiv.org/html/2511.01486v2#bib.bib23)]. This issue in studied in section 2.
We also note that if there is an EMM in the actual market and one trader ii for which 𝔾i,n=𝔽\mathbb{G}^{i,n}=\mathbb{F},
then, because ℍn\mathbb{H}^{n} includes 𝔾i,n=𝔽\mathbb{G}^{i,n}=\mathbb{F},
the nnth market is efficient with respect to 𝔽\mathbb{F} immediately. This implies the interesting structure is where no individual trader knows 𝔽\mathbb{F}, therefore we assume that

|  |  |  |
| --- | --- | --- |
|  | 𝔾i,n⊊𝔽\mathbb{G}^{i,n}\subsetneq\mathbb{F} |  |

for all ii and all nn.

In this section we do not posit a specific functional form for the individual/combined proposed drift and volatility, and their explicit dependence on traders’ beliefs. In the subsequent sections we study more specialized models where these dependencies are given explicitly. Finaly, we provide explicit simulations of our theoretical results and demonstrate how they can be implemented in practice.

We shall repeatedly use the following stability estimate; its proof is standard and included for completeness.

###### Lemma 2.1.

Assume ([2.4](https://arxiv.org/html/2511.01486v2#S2.E4 "Equation 2.4 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and ([2.11](https://arxiv.org/html/2511.01486v2#S2.E11 "Equation 2.11 ‣ 2.4 Simulation of Convergence under Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Then for each nn and all t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sups≤t|Stildes(n)−Ss|2]≤CL,T​\ilimits@0t​𝔼​W22​(πtildeun,δSu)​d​u,\mathbb{E}\Big[\sup\_{s\leq t}\big|\tilde{S}^{(n)}\_{s}-S\_{s}\big|^{2}\Big]\ \leq\ C\_{L,T}\intslop\ilimits@\_{0}^{t}\mathbb{E}\,W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{u},\delta\_{S\_{u}}\big)\,du, |  | (2.6) |

for a constant CL,T<∞C\_{L,T}<\infty depending only on LL and TT.

###### Proof.

Let :=tStildet(n)−St{}\_{t}:=\tilde{S}^{(n)}\_{t}-S\_{t}. Using ([2.3](https://arxiv.org/html/2511.01486v2#S2.E3 "Equation 2.3 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), ([2.1](https://arxiv.org/html/2511.01486v2#S2.E1 "Equation 2.1 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), and the compatibility ([2.11](https://arxiv.org/html/2511.01486v2#S2.E11 "Equation 2.11 ‣ 2.4 Simulation of Convergence under Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")),

|  |  |  |
| --- | --- | --- |
|  | d=t(b(t,Stildet(n),πtildetn)−b(t,St,δSt))dt+(σ(t,Stildet(n),πtildetn)−σ(t,St,δSt))dWt,=00.d{}\_{t}=\Big(b\big(t,\tilde{S}^{(n)}\_{t},\tilde{\pi}^{\,n}\_{t}\big)-b\big(t,S\_{t},\delta\_{S\_{t}}\big)\Big)\,dt+\Big(\sigma\big(t,\tilde{S}^{(n)}\_{t},\tilde{\pi}^{\,n}\_{t}\big)-\sigma\big(t,S\_{t},\delta\_{S\_{t}}\big)\Big)\,dW\_{t},\qquad{}\_{0}=0. |  |

By Burkholder–Davis–Gundy, Jensen, and ([2.4](https://arxiv.org/html/2511.01486v2#S2.E4 "Equation 2.4 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), for some C=CL,TC=C\_{L,T},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[sups≤t||2s]\displaystyle\mathbb{E}\Big[\sup\_{s\leq t}|{}\_{s}|^{2}\Big] | ≤C​𝔼​\ilimits@0t​|b​(u,Stildeu(n),πtildeun)−b​(u,Su,δSu)|2​d​u\displaystyle\leq C\,\mathbb{E}\intslop\ilimits@\_{0}^{t}\Big|b\big(u,\tilde{S}^{(n)}\_{u},\tilde{\pi}^{\,n}\_{u}\big)-b\big(u,S\_{u},\delta\_{S\_{u}}\big)\Big|^{2}\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C​𝔼​\ilimits@0t​\|​σ​(u,Stildeu(n),πtildeun)−σ​(u,Su,δSu)​\|2​d​u\displaystyle\quad+C\,\mathbb{E}\intslop\ilimits@\_{0}^{t}\big\|\sigma\big(u,\tilde{S}^{(n)}\_{u},\tilde{\pi}^{\,n}\_{u}\big)-\sigma\big(u,S\_{u},\delta\_{S\_{u}}\big)\big\|^{2}\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C𝔼\ilimits@0t(||2u+W22(πtildeun,δSu))du.\displaystyle\leq C\,\mathbb{E}\intslop\ilimits@\_{0}^{t}\Big(|{}\_{u}|^{2}+W\_{2}^{2}(\tilde{\pi}^{\,n}\_{u},\delta\_{S\_{u}})\Big)\,du. |  |

Gronwall’s lemma yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼[sups≤t||2s]≤CL,T\ilimits@0t𝔼W22(πtildeun,δSu)du,\mathbb{E}\Big[\sup\_{s\leq t}|{}\_{s}|^{2}\Big]\ \leq\ C\_{L,T}\intslop\ilimits@\_{0}^{t}\mathbb{E}\,W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{u},\delta\_{S\_{u}}\big)\,du, |  |

as claimed.
∎

We also record a basic identity and a simple domination bound that will be used repeatedly.

###### Lemma 2.2.

Let X∈L2X\in L^{2} and 𝒢⊂ℱ\mathcal{G}\subset\mathcal{F} be a sub-σ\sigma-algebra. Then

|  |  |  |
| --- | --- | --- |
|  | W22​(ℒ​(X​𝒢),δX)=\ilimits@​|y−X|2​ℒ​(X​𝒢)​(d​y)=Var​(X​𝒢)+|X−𝔼​[X​𝒢]|2.W\_{2}^{2}\big(\mathcal{L}(X\mid\mathcal{G}),\delta\_{X}\big)=\intslop\ilimits@|y-X|^{2}\,\mathcal{L}(X\mid\mathcal{G})(dy)=\mathrm{Var}(X\mid\mathcal{G})+\big|X-\mathbb{E}[X\mid\mathcal{G}]\big|^{2}. |  |

In particular, 𝔼​W22​(ℒ​(X​𝒢),δX)=2​𝔼​|X−𝔼​[X​𝒢]|2≤2​𝔼​|X|2\mathbb{E}\,W\_{2}^{2}\big(\mathcal{L}(X\mid\mathcal{G}),\delta\_{X}\big)=2\,\mathbb{E}\big|X-\mathbb{E}[X\mid\mathcal{G}]\big|^{2}\leq 2\,\mathbb{E}|X|^{2}.

###### Proof.

Standard.
∎

###### Lemma 2.3.

Let μ1,…,μm∈𝒫2​(ℝd)\mu\_{1},\dots,\mu\_{m}\in\mathcal{P}\_{2}(\mathbb{R}^{d}), w∈mw\in{}\_{m}, and let Barw​(μ1,…,μm)\mathrm{Bar}\_{w}(\mu\_{1},\dots,\mu\_{m}) be any minimizer in ([2.2](https://arxiv.org/html/2511.01486v2#S2.E2 "Equation 2.2 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Then, for every ρ∈𝒫2​(ℝd)\rho\in\mathcal{P}\_{2}(\mathbb{R}^{d}),

|  |  |  |
| --- | --- | --- |
|  | W22​(Barw​(μ1,…,μm),ρ)≤ 4​max1≤i≤m⁡W22​(μi,ρ).W\_{2}^{2}\big(\mathrm{Bar}\_{w}(\mu\_{1},\dots,\mu\_{m}),\rho\big)\ \leq\ 4\,\max\_{1\leq i\leq m}W\_{2}^{2}(\mu\_{i},\rho). |  |

###### Proof.

Let μbar:=Barw​(μ1,…,μm)\bar{\mu}:=\mathrm{Bar}\_{w}(\mu\_{1},\dots,\mu\_{m}). Pick i⋆i^{\star} minimizing W2​(μbar,μi)W\_{2}(\bar{\mu},\mu\_{i}). By optimality of μbar\bar{\mu},

|  |  |  |
| --- | --- | --- |
|  | \slimits@i=1m​wi​W22​(μbar,μi)≤\slimits@i=1m​wi​W22​(ρ,μi)≤maxi⁡W22​(ρ,μi).\sumop\slimits@\_{i=1}^{m}w\_{i}\,W\_{2}^{2}(\bar{\mu},\mu\_{i})\ \leq\ \sumop\slimits@\_{i=1}^{m}w\_{i}\,W\_{2}^{2}(\rho,\mu\_{i})\ \leq\ \max\_{i}W\_{2}^{2}(\rho,\mu\_{i}). |  |

Hence W22​(μbar,μi⋆)≤maxi⁡W22​(ρ,μi)W\_{2}^{2}(\bar{\mu},\mu\_{i^{\star}})\leq\max\_{i}W\_{2}^{2}(\rho,\mu\_{i}). By the triangle inequality and (a+b)2≤2​(a2+b2)(a+b)^{2}\leq 2(a^{2}+b^{2}),

|  |  |  |
| --- | --- | --- |
|  | W22​(μbar,ρ)≤ 2​W22​(μbar,μi⋆)+2​W22​(μi⋆,ρ)≤ 4​maxi⁡W22​(μi,ρ).∎W\_{2}^{2}(\bar{\mu},\rho)\ \leq\ 2\,W\_{2}^{2}(\bar{\mu},\mu\_{i^{\star}})+2\,W\_{2}^{2}(\mu\_{i^{\star}},\rho)\ \leq\ 4\,\max\_{i}W\_{2}^{2}(\mu\_{i},\rho).\qed |  |

### 2.2 Convergence Under Uniformly Increasing Information

The following assumption plays a key role in ensuring convergence to the true price process.

###### Assumption 2.4.

For each i∈{1,…,m}i\in\{1,\dots,m\} and each t∈[0,T]t\in[0,T], the σ\sigma–algebras increase in nn and exhaust ℱt\mathcal{F}\_{t}:

|  |  |  |
| --- | --- | --- |
|  | 𝒢ti,1⊆𝒢ti,2⊆⋯,σ​(\slimits@n≥1​𝒢ti,n)=ℱt(up to ℙ–null sets).\mathcal{G}^{i,1}\_{t}\subseteq\mathcal{G}^{i,2}\_{t}\subseteq\cdots,\qquad\sigma\Big(\bigcupop\slimits@\_{n\geq 1}\mathcal{G}^{i,n}\_{t}\Big)=\mathcal{F}\_{t}\quad\text{(up to $\mathbb{P}$--null sets)}. |  |

###### Theorem 2.5.

Under Assumption [2.4](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.2 Convergence Under Uniformly Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), for each t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | W2​(πtildetn,δSt)→𝑛L1​() 0.W\_{2}\big(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}}\big)\ \xrightarrow[n]{\ L^{1}(\Omega)\ }\ 0. |  |

###### Proof.

Fix t∈[0,T]t\in[0,T]. By the martingale convergence theorem,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|St−𝔼​[St​𝒢ti,n]|2→𝑛 0,i=1,…,m.\mathbb{E}\big|S\_{t}-\mathbb{E}[S\_{t}\mid\mathcal{G}^{i,n}\_{t}]\big|^{2}\ \xrightarrow[n]{}\ 0,\qquad i=1,\dots,m. |  |

By Lemma [2.2](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), 𝔼​W22​(πti,n,δSt)=2​𝔼​|St−𝔼​[St​𝒢ti,n]|2→0\mathbb{E}\,W\_{2}^{2}(\pi^{i,n}\_{t},\delta\_{S\_{t}})=2\,\mathbb{E}|S\_{t}-\mathbb{E}[S\_{t}\mid\mathcal{G}^{i,n}\_{t}]|^{2}\to 0. Using Lemma [2.3](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem3 "Lemma 2.3. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") with ρ=δSt\rho=\delta\_{S\_{t}},

|  |  |  |
| --- | --- | --- |
|  | W22​(πtildetn,δSt)≤ 4​max1≤i≤m⁡W22​(πti,n,δSt),W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}}\big)\ \leq\ 4\,\max\_{1\leq i\leq m}W\_{2}^{2}\big(\pi^{i,n}\_{t},\delta\_{S\_{t}}\big), |  |

and hence, taking expectations and using max≤\slimits@\max\leq\sumop\slimits@,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​W22​(πtildetn,δSt)≤ 4​\slimits@i=1m​𝔼​W22​(πti,n,δSt)→𝑛 0.\mathbb{E}\,W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}}\big)\ \leq\ 4\sumop\slimits@\_{i=1}^{m}\mathbb{E}\,W\_{2}^{2}\big(\pi^{i,n}\_{t},\delta\_{S\_{t}}\big)\ \xrightarrow[n]{}\ 0. |  |

By Cauchy–Schwarz, 𝔼​W2​(πtildetn,δSt)≤𝔼​W22​(πtildetn,δSt)→0\mathbb{E}\,W\_{2}(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}})\leq\sqrt{\mathbb{E}\,W\_{2}^{2}(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}})}\to 0.
∎

###### Corollary 2.6.

If ([2.4](https://arxiv.org/html/2511.01486v2#S2.E4 "Equation 2.4 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and ([2.11](https://arxiv.org/html/2511.01486v2#S2.E11 "Equation 2.11 ‣ 2.4 Simulation of Convergence under Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) hold, then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt≤T|Stildet(n)−St|2]→𝑛 0.\mathbb{E}\Big[\sup\_{t\leq T}\big|\tilde{S}^{(n)}\_{t}-S\_{t}\big|^{2}\Big]\ \xrightarrow[n]{}\ 0. |  |

###### Proof.

By Lemma [2.3](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem3 "Lemma 2.3. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") with ρ=δSt\rho=\delta\_{S\_{t}},

|  |  |  |
| --- | --- | --- |
|  | W22​(πtildetn,δSt)≤4​max1≤i≤m⁡W22​(πti,n,δSt)≤4​\slimits@i=1m​W22​(πti,n,δSt).W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}}\big)\leq 4\,\max\_{1\leq i\leq m}W\_{2}^{2}\big(\pi^{i,n}\_{t},\delta\_{S\_{t}}\big)\leq 4\sumop\slimits@\_{i=1}^{m}W\_{2}^{2}\big(\pi^{i,n}\_{t},\delta\_{S\_{t}}\big). |  |

Taking expectations and using Lemma [2.2](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") together with the martingale convergence theorem (applied under Assumption [2.4](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem4 "Assumption 2.4. ‣ 2.2 Convergence Under Uniformly Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) gives, for each fixed tt,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​W22​(πtildetn,δSt)≤4​\slimits@i=1m​𝔼​W22​(πti,n,δSt)→𝑛 0.\mathbb{E}\,W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}}\big)\leq 4\sumop\slimits@\_{i=1}^{m}\mathbb{E}\,W\_{2}^{2}\big(\pi^{i,n}\_{t},\delta\_{S\_{t}}\big)\ \xrightarrow[n]{}\ 0. |  |

Moreover, still by Lemma [2.2](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​W22​(πtildetn,δSt)≤ 4​\slimits@i=1m​𝔼​W22​(πti,n,δSt)≤ 8​m​𝔼​|St|2,\mathbb{E}\,W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}}\big)\ \leq\ 4\sumop\slimits@\_{i=1}^{m}\mathbb{E}\,W\_{2}^{2}\big(\pi^{i,n}\_{t},\delta\_{S\_{t}}\big)\ \leq\ 8m\,\mathbb{E}|S\_{t}|^{2}, |  |

and t↦𝔼​|St|2t\mapsto\mathbb{E}|S\_{t}|^{2} is integrable on [0,T][0,T] by ([2.1](https://arxiv.org/html/2511.01486v2#S2.E1 "Equation 2.1 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Hence

|  |  |  |
| --- | --- | --- |
|  | \ilimits@0T​𝔼​W22​(πtildesn,δSs)​d​s→𝑛 0\intslop\ilimits@\_{0}^{T}\mathbb{E}\,W\_{2}^{2}\big(\tilde{\pi}^{\,n}\_{s},\delta\_{S\_{s}}\big)\,ds\ \xrightarrow[n]{}\ 0 |  |

by dominated convergence. Inserting this into ([2.6](https://arxiv.org/html/2511.01486v2#S2.E6 "Equation 2.6 ‣ Lemma 2.1. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) yields
𝔼​[supt≤T|Stildet(n)−St|2]→0\mathbb{E}\big[\sup\_{t\leq T}|\tilde{S}^{(n)}\_{t}-S\_{t}|^{2}\big]\to 0.
∎

### 2.3 Failure of Convergence Under Non-Uniformly Increasing Information

We first show that improvement of the combined information pool ℍn\mathbb{H}^{n} alone is not sufficient to ensure convergence of the barycenter.

###### Assumption 2.7.

For each t∈[0,T]t\in[0,T], ℋt1⊆ℋt2⊆⋯\mathcal{H}^{1}\_{t}\subseteq\mathcal{H}^{2}\_{t}\subseteq\cdots and σ​(\slimits@n≥1​ℋtn)=ℱt\sigma\!\big(\bigcupop\slimits@\_{n\geq 1}\mathcal{H}^{n}\_{t}\big)=\mathcal{F}\_{t} (ℙ\mathbb{P}-a.s.), but for at least one expert ii,
σ​(\slimits@n≥1​𝒢ti,n)⊊ℱt\sigma\!\big(\bigcupop\slimits@\_{n\geq 1}\mathcal{G}^{i,n}\_{t}\big)\subsetneq\mathcal{F}\_{t} (ℙ\mathbb{P}-a.s.).

###### Example 2.8.

Let d=1d=1 and fix t∈(0,T]t\in(0,T]. On a product space supporting an 𝔽\mathbb{F}–Brownian motion WW, take independent Rademacher variables U,VU,V with ℙ​(U=±1)=ℙ​(V=±1)=12\mathbb{P}(U=\pm 1)=\mathbb{P}(V=\pm 1)=\tfrac{1}{2}, independent of WW. Define Ss:=U​VS\_{s}:=UV for all s∈[0,T]s\in[0,T], which solves ([2.1](https://arxiv.org/html/2511.01486v2#S2.E1 "Equation 2.1 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) with bbar≡0=σbar\bar{b}\equiv 0=\bar{\sigma}. Define

|  |  |  |
| --- | --- | --- |
|  | ℱt:=σ(U,V)∨σ(Wr:r≤t)(completed and right–continuous),t∈[0,T].\mathcal{F}\_{t}:=\sigma(U,V)\ \vee\ \sigma(W\_{r}:\,r\leq t)\quad\text{(completed and right--continuous)},\qquad t\in[0,T]. |  |

For all nn set

|  |  |  |
| --- | --- | --- |
|  | 𝒢t1,n:=σ(U)∨σ(Wr:r≤t),𝒢t2,n:=σ(V)∨σ(Wr:r≤t),\mathcal{G}^{1,n}\_{t}:=\sigma(U)\ \vee\ \sigma(W\_{r}:\,r\leq t),\qquad\mathcal{G}^{2,n}\_{t}:=\sigma(V)\ \vee\ \sigma(W\_{r}:\,r\leq t), |  |

and, without changing notation, let 𝔾i,n\mathbb{G}^{i,n} be their right–continuous, complete versions. Then
ℋtn=σ(U,V)∨σ(Wr:r≤t)=ℱt\mathcal{H}^{n}\_{t}=\sigma(U,V)\vee\sigma(W\_{r}:\,r\leq t)=\mathcal{F}\_{t} for all nn, so the join is already full, while
σ(\slimits@n𝒢t1,n)=σ(U)∨σ(Wr:r≤t)⊊ℱt\sigma(\bigcupop\slimits@\_{n}\mathcal{G}^{1,n}\_{t})=\sigma(U)\vee\sigma(W\_{r}:\,r\leq t)\subsetneq\mathcal{F}\_{t} and similarly for i=2i=2.
Since St=U​VS\_{t}=UV is independent of WW and ℙ​(V=±1​σ​(U))=12\mathbb{P}(V=\pm 1\mid\sigma(U))=\tfrac{1}{2}, we have

|  |  |  |
| --- | --- | --- |
|  | πt1,n=πt2,n=12​δ−1+12​δ+1a.s.,δSt∈{δ−1,δ+1}​a.s.\pi^{1,n}\_{t}=\pi^{2,n}\_{t}=\tfrac{1}{2}\delta\_{-1}+\tfrac{1}{2}\delta\_{+1}\quad\text{a.s.,}\qquad\delta\_{S\_{t}}\in\{\delta\_{-1},\delta\_{+1}\}\ \text{a.s.} |  |

Therefore, for any weights w1,t(n),w2,t(n)∈2w^{(n)}\_{1,t},w^{(n)}\_{2,t}\in{}\_{2},

|  |  |  |
| --- | --- | --- |
|  | πtildetn=Barwt(n)​(12​δ−1+12​δ+1,12​δ−1+12​δ+1)=12​δ−1+12​δ+1,\tilde{\pi}^{\,n}\_{t}=\mathrm{Bar}\_{w^{(n)}\_{t}}\Big(\tfrac{1}{2}\delta\_{-1}+\tfrac{1}{2}\delta\_{+1},\,\tfrac{1}{2}\delta\_{-1}+\tfrac{1}{2}\delta\_{+1}\Big)=\tfrac{1}{2}\delta\_{-1}+\tfrac{1}{2}\delta\_{+1}, |  |

and hence

|  |  |  |
| --- | --- | --- |
|  | W2​(πtildetn,δSt)={2,St=+1,2,St=−1,W\_{2}\!\big(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}}\big)=\begin{cases}\sqrt{2},&S\_{t}=+1,\\ \sqrt{2},&S\_{t}=-1,\end{cases} |  |

so W2​(πtildetn,δSt)=2W\_{2}(\tilde{\pi}^{\,n}\_{t},\delta\_{S\_{t}})=\sqrt{2} a.s. and in particular does not converge to 0.

It is easy to show that this may cause the actual price process not to converge to the true price process. We do not pursue this here.

### 2.4 Simulation of Convergence under Increasing Information

We assume d=1d=1 and a filtered space (,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}) carrying a one–dimensional Brownian motion WW. The *true* price SS is a geometric Brownian motion (GBM)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=bbar​(t,St)​d​t+σbar​(t,St)​d​Wtwithbbar​(t,x)=μ⋆​x,σbar​(t,x)=σ⋆​x,S0>0,dS\_{t}=\bar{b}(t,S\_{t})\,dt+\bar{\sigma}(t,S\_{t})\,dW\_{t}\quad\text{with}\quad\bar{b}(t,x)=\mu\_{\star}x,\ \ \bar{\sigma}(t,x)=\sigma\_{\star}x,\qquad S\_{0}>0, |  | (2.7) |

where μ⋆\mu\_{\star} and σ⋆>0\sigma\_{\star}>0 are some constants. Fix m∈ℕm\in\mathbb{N} traders and information levels n∈ℕn\in\mathbb{N}. Let Xt:=log⁡StX\_{t}:=\log S\_{t} and suppose trader ii at level nn observes

|  |  |  |
| --- | --- | --- |
|  | Yti,n=Xt+εti,n,εti,n∼𝒩​(0,τi2/n),Y^{i,n}\_{t}\;=\;X\_{t}+\varepsilon^{i,n}\_{t},\qquad\varepsilon^{i,n}\_{t}\sim\mathcal{N}\!\big(0,\tau\_{i}^{2}/n\big), |  |

independent of WW and across (i,n)(i,n). Then πti,n:=ℒ​(St​Yti,n)\pi^{i,n}\_{t}:=\mathcal{L}(S\_{t}\mid Y^{i,n}\_{t}) is lognormal. For weights w(n)∈mw^{(n)}\in{}\_{m}, define the (one–dimensional) W2W\_{2}–barycenter of the traders at time tt by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πtildetn∈argminν∈𝒫2​(ℝ+)⁡\slimits@i=1m​wi(n)​W22​(ν,πti,n).\tilde{\pi}^{\,n}\_{t}\in\operatorname{argmin}\_{\nu\in\mathcal{P}\_{2}(\mathbb{R}\_{+})}\sumop\slimits@\_{i=1}^{m}w^{(n)}\_{i}\,W\_{2}^{2}\!\big(\nu,\pi^{i,n}\_{t}\big). |  | (2.8) |

In d=1d=1, πtildetn\tilde{\pi}^{\,n}\_{t} is the quantile average (comonotone coupling), which we evaluate in closed form via its first two moments.

|  |  |  |
| --- | --- | --- |
|  | πtildetn=ℒ​(\slimits@i=1m​wi,t(n)​emti,n+sti,n​Z),Z∼𝒩​(0,1),mti,n:=𝔼​[log⁡St​𝒢ti,n],(sti,n)2:=Var​(log⁡St​𝒢ti,n).\tilde{\pi}^{\,n}\_{t}=\mathcal{L}\!\Big(\sumop\slimits@\_{i=1}^{m}w^{(n)}\_{i,t}\,\mathrm{e}^{\,m^{i,n}\_{t}+s^{i,n}\_{t}Z}\Big),\quad Z\sim\mathcal{N}(0,1),\ \ m^{i,n}\_{t}:=\mathbb{E}[\log S\_{t}\mid\mathcal{G}^{i,n}\_{t}],\ \ (s^{i,n}\_{t})^{2}:=\mathrm{Var}(\log S\_{t}\mid\mathcal{G}^{i,n}\_{t}). |  |

We assume the drift and volatility depend on the barycentric mean and standard deviation:

|  |  |  |
| --- | --- | --- |
|  | m1​(μ):=\ilimits@​y​μ​(d​y),s​(μ):=\ilimits@​(y−m1​(μ))2​μ​(d​y).m\_{1}(\mu):=\intslop\ilimits@y\,\mu(dy),\qquad s(\mu):=\sqrt{\intslop\ilimits@(y-m\_{1}(\mu))^{2}\,\mu(dy)}. |  |

For κd,κv≥0\kappa\_{d},\kappa\_{v}\geq 0, set for (t,x,μ)∈[0,T]×ℝ+×𝒫2​(ℝ+)(t,x,\mu)\in[0,T]\times\mathbb{R}\_{+}\times\mathcal{P}\_{2}(\mathbb{R}\_{+})

|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(t,x,μ):=x​(μ⋆+κd​log⁡m1​(μ)x),σ​(t,x,μ):=x​σ⋆​(1+κv​s​(μ)m1​(μ)).b(t,x,\mu)\;:=\;x\!\left(\mu\_{\star}+\kappa\_{d}\log\!\frac{m\_{1}(\mu)}{x}\right),\qquad\sigma(t,x,\mu)\;:=\;x\,\sigma\_{\star}\!\left(1+\kappa\_{v}\,\frac{s(\mu)}{m\_{1}(\mu)}\right). |  | (2.9) |

The actual market price Stilde(n)\tilde{S}^{(n)} follows the McKean-Vlasov-type SDE driven by the same WW:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Stildet(n)=b​(t,Stildet(n),πtildetn)​d​t+σ​(t,Stildet(n),πtildetn)​d​Wt,Stilde0(n)=S0.d\tilde{S}^{(n)}\_{t}\;=\;b\!\big(t,\tilde{S}^{(n)}\_{t},\tilde{\pi}^{\,n}\_{t}\big)\,dt\;+\;\sigma\!\big(t,\tilde{S}^{(n)}\_{t},\tilde{\pi}^{\,n}\_{t}\big)\,dW\_{t},\qquad\tilde{S}^{(n)}\_{0}=S\_{0}. |  | (2.10) |

By construction,

|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(t,x,δx)=μ⋆​x=bbar​(t,x),σ​(t,x,δx)=σ⋆​x=σbar​(t,x),b(t,x,\delta\_{x})=\mu\_{\star}x=\bar{b}(t,x),\qquad\sigma(t,x,\delta\_{x})=\sigma\_{\star}x=\bar{\sigma}(t,x), |  | (2.11) |

so ([4.34](https://arxiv.org/html/2511.01486v2#S4.E34 "Equation 4.34 ‣ 4.6 Simulation of the True, Observed and Opinion-Biased Price Processes ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) is *compatible* with ([2.7](https://arxiv.org/html/2511.01486v2#S2.E7 "Equation 2.7 ‣ 2.4 Simulation of Convergence under Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) in the sense b​(⋅,⋅,δx)=bbarb(\cdot,\cdot,\delta\_{x})=\bar{b}, σ​(⋅,⋅,δx)=σbar\sigma(\cdot,\cdot,\delta\_{x})=\bar{\sigma}. As n→∞n\to\infty the posterior variances scale as τi2/n\tau\_{i}^{2}/n, the barycenter πtildetn⇒δSt\tilde{\pi}^{\,n}\_{t}\Rightarrow\delta\_{S\_{t}}, and under standard Lipschitz and linear growth conditions of ([2.9](https://arxiv.org/html/2511.01486v2#S2.E9 "Equation 2.9 ‣ 2.4 Simulation of Convergence under Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) one has convergence of Stilde(n)\tilde{S}^{(n)} to SS in L2(;C)L^{2}(\Omega;C).
We simulate 3030 paths on [0,1][0,1] year with daily steps. For each n∈{1,10,100,1000}n\in\{1,10,100,1000\} we draw a common Brownian path per row and plot: left (blue) the true SS, right (red) the synthetic Stilde(n)\tilde{S}^{(n)} built from the W2W\_{2}–barycenter ([2.8](https://arxiv.org/html/2511.01486v2#S2.E8 "Equation 2.8 ‣ 2.4 Simulation of Convergence under Increasing Information ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Parameters used in the figure:
S0=100S\_{0}=100, μ⋆=8%\mu\_{\star}=8\%, σ⋆=60%\sigma\_{\star}=60\%, m=4m=4, w=(0.4,0.3,0.2,0.1)w=(0.4,0.3,0.2,0.1), τ=(2.0,1.2,2.5,1.5)\tau=(2.0,1.2,2.5,1.5), κd=0.35\kappa\_{d}=0.35, κv=2.75\kappa\_{v}=2.75.

It must be noted that other choices are possible, as long as they satisfy the compatibility condition. Some suggestions are given below. For μ∈𝒫2​(ℝ+)\mu\in\mathcal{P}\_{2}(\mathbb{R}\_{+}) set
m1​(μ):=\ilimits@​y​μ​(d​y)m\_{1}(\mu):=\intslop\ilimits@y\,\mu(dy),
s​(μ):=\ilimits@​(y−m1​(μ))2​μ​(d​y)s(\mu):=\sqrt{\intslop\ilimits@(y-m\_{1}(\mu))^{2}\,\mu(dy)},
cv​(μ):=s​(μ)/(m1​(μ)+ε)\mathrm{cv}(\mu):=s(\mu)/(m\_{1}(\mu)+\varepsilon) for small ε>0\varepsilon>0.
Let bbar,σbar\bar{b},\bar{\sigma} be the true coefficients from ([2.1](https://arxiv.org/html/2511.01486v2#S2.E1 "Equation 2.1 ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).
All parameters κ,κd,κv,λ≥0\kappa,\kappa\_{d},\kappa\_{v},\lambda\geq 0.

| # | Drift b​(t,x,μ)b(t,x,\mu) | Volatility σ​(t,x,μ)\sigma(t,x,\mu) |
| --- | --- | --- |
| 1 | bbar​(t,x)+κ​(m1​(μ)−x)\displaystyle\bar{b}(t,x)\;+\;\kappa\big(m\_{1}(\mu)-x\big) | σbar​(t,x)\displaystyle\bar{\sigma}(t,x) |
| 2 | bbar​(t,x)\displaystyle\bar{b}(t,x) | σbar​(t,x)​(1+κ​cv​(μ))\displaystyle\bar{\sigma}(t,x)\!\left(1+\kappa\,\mathrm{cv}(\mu)\right) |
| 3 | bbar​(t,x)+κd​(m1​(μ)−x)\displaystyle\bar{b}(t,x)\;+\;\kappa\_{d}\big(m\_{1}(\mu)-x\big) | σbar​(t,x)​(1+κv​cv​(μ))\displaystyle\bar{\sigma}(t,x)\!\left(1+\kappa\_{v}\,\mathrm{cv}(\mu)\right) |
| 4 | bbar​(t,x)​(1+κ​(m1​(μ)x−1))\displaystyle\bar{b}(t,x)\Big(1+\kappa\!\left(\tfrac{m\_{1}(\mu)}{x}-1\right)\Big) | σbar​(t,x)\displaystyle\bar{\sigma}(t,x) |
| 5 | bbar​(t,x)−λ​x​cv​(μ)2\displaystyle\bar{b}(t,x)\;-\;\lambda\,x\,\mathrm{cv}(\mu)^{2} | σbar​(t,x)\displaystyle\bar{\sigma}(t,x) |
| 6 | bbar​(t,x)\displaystyle\bar{b}(t,x) | σbar​(t,x)​ 1+κ​(m1​(μ)−xm1​(μ)+ε)2\displaystyle\bar{\sigma}(t,x)\,\sqrt{\,1+\kappa\!\left(\tfrac{m\_{1}(\mu)-x}{m\_{1}(\mu)+\varepsilon}\right)^{\!2}} |

Table 1: Each pair satisfies the compatibility condition: for μ=δx\mu=\delta\_{x} one has m1​(δx)=xm\_{1}(\delta\_{x})=x, s​(δx)=cv​(δx)=0s(\delta\_{x})=\mathrm{cv}(\delta\_{x})=0, hence b​(t,x,δx)=bbar​(t,x)b(t,x,\delta\_{x})=\bar{b}(t,x) and σ​(t,x,δx)=σbar​(t,x)\sigma(t,x,\delta\_{x})=\bar{\sigma}(t,x).

However, it is obvious that any choice of the drift and volatility must be meaningful from the modeling perspective, i.e. admit financial interpretation. In the next sections, we will provide more concrete (and much more sophisticated) structures that admit clear interpretation and generate a wide range of nontrivial implications and results.

![Refer to caption](Sim1.png)


Figure 1: Increasing information. Rows n=1,10,100,1000n=1,10,100,1000; left: true price SS (blue); right: synthetic Stilde(n)\tilde{S}^{(n)} (red). Common Brownian shocks per row; we observe convergence as the dispersion in traders’ posteriors vanishes.

## 3 Individual Biases under Increasing Information

### 3.1 Preliminaries and Model Set-Up

In this section, we propose a much more explicit and financially motivated drift perturbation scheme capturing model uncertainty in which a single trader’s belief is represented by *a drift perturbation term ρ\rho* which is convexly combined with the true drift α\alpha,
with a (random, time–varying) *bias weight β\beta that shrinks to 0 as information increases*. Thus, we want to study how a single trader uses the information available to them, combining observations with personal biases to arrive at a candidate price process. In the next section we will study how a trader seeking arbitrage opportunities should aggregate the individual (biased) proposal processes. This is an elaboration on the ideas of the previous section, showing more explicitly how an increasing information flow implies convergence of the proposal process to the true price process for a single trader. In this setting, the weight of the bias depends on the distance between the conditional distribution of the price StS\_{t} given the available information 𝒢tn\mathcal{G}^{n}\_{t} and the value of the optimal estimate of StS\_{t} provided by the filtered S^t\mathaccent 866{S}\_{t}. This structure corresponds to the intuition that the *the distance between the conditional distribution and the estimated value captures ambiguity* regarding the true value of the price process, and this ambiguity shrinks as more information is revealed, as n→∞n\to\infty, eventually collapsing to a Dirac measure at the correct value. Thus, this more specialized model also incorporates a fairly novel way of measuring the impact of a trader’s intuitive sense of ambiguity regarding the true value of a partially observed price process.

Let (,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}) be a complete probability space
with a right–continuous, complete filtration
𝔽=(ℱt)t∈[0,T]\mathbb{F}=(\mathcal{F}\_{t})\_{t\in[0,T]} supporting a DD–dimensional Brownian motion WW.
The true dd–dimensional price process SS is the unique strong solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | dSt=α(t,St)dt+σ(t,St)dWt,S0∈L2(;ℝd),dS\_{t}=\alpha(t,S\_{t})\,dt+\sigma(t,S\_{t})\,dW\_{t},\qquad S\_{0}\in L^{2}(\Omega;\mathbb{R}^{d}), |  | (3.1) |

where the coefficients α:[0,T]×ℝd→ℝd\alpha:[0,T]\times\mathbb{R}^{d}\to\mathbb{R}^{d} and
σ:[0,T]×ℝd→ℝd×D\sigma:[0,T]\times\mathbb{R}^{d}\to\mathbb{R}^{d\times D} satisfy:

###### Assumption 3.1.

There exists L≥1L\geq 1 such that for all t∈[0,T]t\in[0,T], x,y∈ℝdx,y\in\mathbb{R}^{d},

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |α​(t,x)−α​(t,y)|+\|​σ​(t,x)−σ​(t,y)​\|≤L​|x−y|,\displaystyle|\alpha(t,x)-\alpha(t,y)|+\|\sigma(t,x)-\sigma(t,y)\|\leq L|x-y|, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |α​(t,x)|2+\|​σ​(t,x)​\|2≤L​(1+|x|2).\displaystyle|\alpha(t,x)|^{2}+\|\sigma(t,x)\|^{2}\leq L\,(1+|x|^{2}). |  |

Under Assumption [3.1](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), ([3.1](https://arxiv.org/html/2511.01486v2#S3.E1 "Equation 3.1 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) is well posed and
𝔼​[supt≤T|St|2]<∞\mathbb{E}\!\left[\sup\_{t\leq T}|S\_{t}|^{2}\right]<\infty.

We model increasingly informative observers by a fixed index n∈ℕn\in\mathbb{N}
and a subfiltration 𝔾n=(𝒢tn)t∈[0,T]\mathbb{G}^{n}=(\mathcal{G}^{n}\_{t})\_{t\in[0,T]} of 𝔽\mathbb{F} such that for each t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢t1⊆𝒢t2⊆⋯,σ​(\slimits@n≥1​𝒢tn)=ℱt(up to ​ℙ​-null sets).\mathcal{G}^{1}\_{t}\subseteq\mathcal{G}^{2}\_{t}\subseteq\cdots,\qquad\sigma\Big(\bigcupop\slimits@\_{n\geq 1}\mathcal{G}^{n}\_{t}\Big)=\mathcal{F}\_{t}\quad(\text{up to }\mathbb{P}\text{-null sets}). |  | (3.2) |

We assume right–continuity and completeness of each 𝔾n\mathbb{G}^{n} without changing notation.

Fix nn and t∈[0,T]t\in[0,T]. Set

|  |  |  |
| --- | --- | --- |
|  | S^t(n):=𝔼​[St​𝒢tn],πtn:=ℒ​(St​𝒢tn)∈𝒫2​(ℝd).\mathaccent 866{S}^{(n)}\_{t}:=\mathbb{E}[S\_{t}\mid\mathcal{G}^{n}\_{t}],\qquad\pi^{n}\_{t}:=\mathcal{L}(S\_{t}\mid\mathcal{G}^{n}\_{t})\in\mathcal{P}\_{2}(\mathbb{R}^{d}). |  |

Recall the identity (see Lemma [2.2](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | W22​(πtn,δS^t(n))=𝔼​[|St−S^t(n)|2|𝒢tn]=Var​(St​𝒢tn).W\_{2}^{2}\big(\pi^{n}\_{t},\delta\_{\mathaccent 866{S}^{(n)}\_{t}}\big)=\mathbb{E}\!\left[\,|S\_{t}-\mathaccent 866{S}^{(n)}\_{t}|^{2}\ \Big|\ \mathcal{G}^{n}\_{t}\right]=\mathrm{Var}\big(S\_{t}\mid\mathcal{G}^{n}\_{t}\big). |  | (3.3) |

Define the *measure of ambiguity* and the *bias weight* correspondingly by

|  |  |  |  |
| --- | --- | --- | --- |
|  | γt(n):=Var​(St​𝒢tn)=W2​(πtn,δS^t(n)),βt(n):=β​(γt(n)),\gamma^{(n)}\_{t}:=\sqrt{\mathrm{Var}(S\_{t}\mid\mathcal{G}^{n}\_{t})}=W\_{2}\!\big(\pi^{n}\_{t},\delta\_{\mathaccent 866{S}^{(n)}\_{t}}\big),\qquad\beta^{(n)}\_{t}:=\beta\!\left(\gamma^{(n)}\_{t}\right), |  | (3.4) |

where β:[0,∞)→[0,1]\beta:[0,\infty)\to[0,1] satisfies:

###### Assumption 3.2.

β\beta is continuous at 0 with β​(0)=0\beta(0)=0, bounded by 11, and locally Lipschitz on [0,∞)[0,\infty).

Define the *bias-perturbed drift* by

|  |  |  |  |
| --- | --- | --- | --- |
|  | αβ(n)​(t,x,ω):=(1−βt(n)​(ω))​α​(t,x)+βt(n)​(ω)​ρt(n)​(ω).\alpha^{(n)}\_{\beta}(t,x,\omega):=(1-\beta^{(n)}\_{t}(\omega))\,\alpha(t,x)+\beta^{(n)}\_{t}(\omega)\,\rho^{(n)}\_{t}(\omega). |  | (3.5) |

Consider *the proposed synthetic price process* S~(n)\mathaccent 869{S}^{(n)} given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S~t(n)=αβ(n)​(t,S~t(n))​d​t+σ​(t,S~t(n))​d​Wt,S~0(n)=S0.d\mathaccent 869{S}^{(n)}\_{t}=\alpha^{(n)}\_{\beta}\big(t,\mathaccent 869{S}^{(n)}\_{t}\big)\,dt+\sigma\big(t,\mathaccent 869{S}^{(n)}\_{t}\big)\,dW\_{t},\qquad\mathaccent 869{S}^{(n)}\_{0}=S\_{0}. |  | (3.6) |

Note γt(n)\gamma^{(n)}\_{t} is 𝒢tn\mathcal{G}^{n}\_{t}–measurable by ([3.3](https://arxiv.org/html/2511.01486v2#S3.E3 "Equation 3.3 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). By considering the 𝔾n\mathbb{G}^{n}-progressively measurable versions of πtn\pi\_{t}^{n} (see the remark [4.7](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem7 "Remark 4.7. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") in section 4) and the optional modifications of S^t(n)\mathaccent 866{S}^{(n)}\_{t}, we obtain that β(n)\beta^{(n)} can be chosen to be 𝔾n\mathbb{G}^{n}–progressively measurable.

###### Lemma 3.3.

Assume ([3.2](https://arxiv.org/html/2511.01486v2#S3.E2 "Equation 3.2 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Then for each t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(γt(n))2]=𝔼​|St−S^t(n)|2→𝑛 0,𝔼​[(βt(n))2]→𝑛 0,\mathbb{E}\big[(\gamma^{(n)}\_{t})^{2}\big]=\mathbb{E}\big|S\_{t}-\mathaccent 866{S}^{(n)}\_{t}\big|^{2}\ \xrightarrow[n]{}\ 0,\qquad\mathbb{E}\big[(\beta^{(n)}\_{t})^{2}\big]\ \xrightarrow[n]{}\ 0, |  |

and by dominated convergence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | \ilimits@0T​𝔼​[(βt(n))2]​d​t→𝑛 0.\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{t})^{2}\big]\,dt\ \xrightarrow[n]{}\ 0. |  | (3.7) |

###### Proof.

By ([3.2](https://arxiv.org/html/2511.01486v2#S3.E2 "Equation 3.2 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and the martingale convergence theorem,
S^t(n)→St\mathaccent 866{S}^{(n)}\_{t}\to S\_{t} in L2L^{2}, hence 𝔼​(γt(n))2=𝔼​|St−S^t(n)|2→0\mathbb{E}(\gamma^{(n)}\_{t})^{2}=\mathbb{E}|S\_{t}-\mathaccent 866{S}^{(n)}\_{t}|^{2}\to 0.
By Assumption [3.2](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), β\beta is locally Lipschitz at 0 and β​(0)=0\beta(0)=0, hence
(βt(n))2≤C​(γt(n))2(\beta^{(n)}\_{t})^{2}\leq C\,(\gamma^{(n)}\_{t})^{2} for all γt(n)\gamma^{(n)}\_{t} sufficiently small.
Set γn:=γt(n)\gamma\_{n}:=\gamma\_{t}^{(n)} and βn:=β​(γn)\beta\_{n}:=\beta(\gamma\_{n}); fix δ>0\delta>0 and let LδL\_{\delta} be the Lipschitz constant of β\beta on [−δ,δ][-\delta,\delta]. Then, using 0≤(βt(n))2≤10\leq(\beta^{(n)}\_{t})^{2}\leq 1 and Chebyshev’s inequality, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[βn2]=𝔼​[βn2​𝟏{|γn|≤δ}]+𝔼​[βn2​𝟏{|γn|>δ}]≤Lδ2​𝔼​[γn2​𝟏{|γn|≤δ}]+ℙ​(|γn|>δ)≤(Lδ2+δ−2)​𝔼​[γn2]→n→∞0.\mathbb{E}[\beta\_{n}^{2}]=\mathbb{E}\big[\beta\_{n}^{2}\mathbf{1}\_{\{|\gamma\_{n}|\leq\delta\}}\big]+\mathbb{E}\big[\beta\_{n}^{2}\mathbf{1}\_{\{|\gamma\_{n}|>\delta\}}\big]\leq L\_{\delta}^{2}\,\mathbb{E}\big[\gamma\_{n}^{2}\mathbf{1}\_{\{|\gamma\_{n}|\leq\delta\}}\big]+\mathbb{P}(|\gamma\_{n}|>\delta)\leq\big(L\_{\delta}^{2}+\delta^{-2}\big)\,\mathbb{E}[\gamma\_{n}^{2}]\xrightarrow[n\to\infty]{}0. |  |

Hence ([3.7](https://arxiv.org/html/2511.01486v2#S3.E7 "Equation 3.7 ‣ Lemma 3.3. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) follows by dominated convergence.
∎

Let ρ(n)=(ρt(n))t∈[0,T]\rho^{(n)}=(\rho^{(n)}\_{t})\_{t\in[0,T]} be a 𝔾n\mathbb{G}^{n}–progressively measurable ℝd\mathbb{R}^{d}–valued process interpreted as the trader’s opinion on the correct drift. We assume:

###### Assumption 3.4.

There exists p>1p>1 such that

|  |  |  |
| --- | --- | --- |
|  | supn≥1\ilimits@0T​𝔼​[|ρt(n)|2​p]​d​t<∞.\sup\_{n\geq 1}\ \intslop\ilimits@\_{0}^{T}\mathbb{E}\big[\,|\rho^{(n)}\_{t}|^{2p}\,\big]\,dt\ <\ \infty. |  |

###### Proposition 3.5.

Under Assumptions [3.1](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), [3.2](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), [3.4](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem4 "Assumption 3.4. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), for every nn the SDE ([3.6](https://arxiv.org/html/2511.01486v2#S3.E6 "Equation 3.6 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) admits a unique strong solution
with

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt≤T|S~t(n)|2]≤C​(1+𝔼​|S0|2+𝔼​\ilimits@0T​|ρt(n)|2​d​t),\mathbb{E}\Big[\sup\_{t\leq T}\big|\mathaccent 869{S}^{(n)}\_{t}\big|^{2}\Big]\ \leq\ C\Big(1+\mathbb{E}|S\_{0}|^{2}+\mathbb{E}\intslop\ilimits@\_{0}^{T}|\rho^{(n)}\_{t}|^{2}\,dt\Big), |  |

for a constant C=C​(L,T)C=C(L,T) independent of nn.

###### Proof.

The drift x↦αβ(n)​(t,x)x\mapsto\alpha^{(n)}\_{\beta}(t,x) is globally Lipschitz with the same constant LL
as α\alpha, since βt(n)∈[0,1]\beta^{(n)}\_{t}\in[0,1] and ρt(n)\rho^{(n)}\_{t} does not depend on xx.
Moreover,

|  |  |  |
| --- | --- | --- |
|  | |αβ(n)​(t,x)|≤|α​(t,x)|+|ρt(n)|≤C​(1+|x|)+|ρt(n)||\alpha^{(n)}\_{\beta}(t,x)|\leq|\alpha(t,x)|+|\rho^{(n)}\_{t}|\leq C(1+|x|)+|\rho^{(n)}\_{t}| |  |

with C=C​(L)C=C(L). Standard SDE estimates (e.g. Itô, BDG, Gronwall) yield the moment bound under Assumption [3.4](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem4 "Assumption 3.4. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective").
∎

### 3.2 Stability and Convergence to the True Process

Set :=t(n)S~t(n)−St{}^{(n)}\_{t}:=\mathaccent 869{S}^{(n)}\_{t}-S\_{t}. Using ([3.1](https://arxiv.org/html/2511.01486v2#S3.E1 "Equation 3.1 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and ([3.6](https://arxiv.org/html/2511.01486v2#S3.E6 "Equation 3.6 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | d=t(n)(α(t,S~t(n))−α(t,St))dt+(σ(t,S~t(n))−σ(t,St))dWt+βt(n)(ρt(n)−α(t,S~t(n)))dt.d{}^{(n)}\_{t}=\Big(\alpha\big(t,\mathaccent 869{S}^{(n)}\_{t}\big)-\alpha(t,S\_{t})\Big)\,dt+\Big(\sigma\big(t,\mathaccent 869{S}^{(n)}\_{t}\big)-\sigma(t,S\_{t})\Big)\,dW\_{t}+\beta^{(n)}\_{t}\Big(\rho^{(n)}\_{t}-\alpha\big(t,\mathaccent 869{S}^{(n)}\_{t}\big)\Big)\,dt. |  | (3.8) |

###### Theorem 3.6.

Under Assumptions [3.1](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"),  [3.2](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), [3.4](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem4 "Assumption 3.4. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), there exists C=C​(L,T)C=C(L,T) such that for every nn and t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[sups≤t||2s(n)]≤C\ilimits@0t𝔼[||2u(n)+(βu(n))2(1+|ρu(n)|2+|Su|2)]du.\mathbb{E}\Big[\sup\_{s\leq t}\big|{}^{(n)}\_{s}\big|^{2}\Big]\ \leq\ C\intslop\ilimits@\_{0}^{t}\mathbb{E}\Big[\big|{}^{(n)}\_{u}\big|^{2}+(\beta^{(n)}\_{u})^{2}\big(1+|\rho^{(n)}\_{u}|^{2}+|S\_{u}|^{2}\big)\Big]\,du. |  | (3.9) |

###### Proof.

Applying BDG and the Lipschitz properties of (α,σ)(\alpha,\sigma),

|  |  |  |
| --- | --- | --- |
|  | 𝔼[sups≤t||2s(n)]≤C\ilimits@0t𝔼||2u(n)du+C\ilimits@0t𝔼[(βu(n))2|ρu(n)−α(u,S~u(n))|2]du.\mathbb{E}\!\left[\sup\_{s\leq t}\big|{}^{(n)}\_{s}\big|^{2}\right]\leq C\intslop\ilimits@\_{0}^{t}\mathbb{E}\big|{}^{(n)}\_{u}\big|^{2}\,du+C\intslop\ilimits@\_{0}^{t}\mathbb{E}\!\left[(\beta^{(n)}\_{u})^{2}\,\big|\rho^{(n)}\_{u}-\alpha(u,\mathaccent 869{S}^{(n)}\_{u})\big|^{2}\right]\,du. |  |

Using (a+b)2≤2​(a2+b2)(a+b)^{2}\leq 2(a^{2}+b^{2}) and the linear growth of α\alpha,

|  |  |  |
| --- | --- | --- |
|  | |ρu(n)−α​(u,S~u(n))|2≤2​|ρu(n)|2+2​|α​(u,S~u(n))|2≤C​(1+|S~u(n)|2+|ρu(n)|2).\big|\rho^{(n)}\_{u}-\alpha(u,\mathaccent 869{S}^{(n)}\_{u})\big|^{2}\leq 2|\rho^{(n)}\_{u}|^{2}+2\,|\alpha(u,\mathaccent 869{S}^{(n)}\_{u})|^{2}\leq C\big(1+|\mathaccent 869{S}^{(n)}\_{u}|^{2}+|\rho^{(n)}\_{u}|^{2}\big). |  |

By Proposition [3.5](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem5 "Proposition 3.5. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") and (a+b)2≤2​(a2+b2)(a+b)^{2}\leq 2(a^{2}+b^{2}),
|S~u(n)|2≤2|Su|2+2||2u(n)|\mathaccent 869{S}^{(n)}\_{u}|^{2}\leq 2|S\_{u}|^{2}+2|{}^{(n)}\_{u}|^{2}, from which we obtain

|  |  |  |
| --- | --- | --- |
|  | |ρu(n)−α(u,S~u(n))|2≤C(1+|Su|2+||2u(n)+|ρu(n)|2).\big|\rho^{(n)}\_{u}-\alpha(u,\mathaccent 869{S}^{(n)}\_{u})\big|^{2}\leq C\big(1+|S\_{u}|^{2}+|{}^{(n)}\_{u}|^{2}+|\rho^{(n)}\_{u}|^{2}\big). |  |

Inserting this bound and absorbing the resulting (βu(n))2||2u(n)(\beta^{(n)}\_{u})^{2}|{}^{(n)}\_{u}|^{2} term
into the first integral (since (βu(n))2≤1(\beta^{(n)}\_{u})^{2}\leq 1), we obtain ([3.9](https://arxiv.org/html/2511.01486v2#S3.E9 "Equation 3.9 ‣ Theorem 3.6. ‣ 3.2 Stability and Convergence to the True Process ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).
∎

###### Theorem 3.7.

Assume  [3.1](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"),  [3.2](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"),  [3.4](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem4 "Assumption 3.4. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") and ([3.2](https://arxiv.org/html/2511.01486v2#S3.E2 "Equation 3.2 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt≤T|S~t(n)−St|2]→𝑛 0.\mathbb{E}\Big[\sup\_{t\leq T}\big|\mathaccent 869{S}^{(n)}\_{t}-S\_{t}\big|^{2}\Big]\ \xrightarrow[n]{}\ 0. |  |

###### Proof.

From ([3.9](https://arxiv.org/html/2511.01486v2#S3.E9 "Equation 3.9 ‣ Theorem 3.6. ‣ 3.2 Stability and Convergence to the True Process ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) with t=Tt=T and Gronwall’s inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝔼[sups≤T||2s(n)]≤C\ilimits@0T𝔼[(βu(n))2(1+|ρu(n)|2+|Su|2)]du,\mathbb{E}\Big[\sup\_{s\leq T}\big|{}^{(n)}\_{s}\big|^{2}\Big]\ \leq\ C\intslop\ilimits@\_{0}^{T}\mathbb{E}\Big[(\beta^{(n)}\_{u})^{2}\big(1+|\rho^{(n)}\_{u}|^{2}+|S\_{u}|^{2}\big)\Big]\,du, |  |

for C=C​(L,T)C=C(L,T). Write

|  |  |  |
| --- | --- | --- |
|  | An:=\ilimits@0T​𝔼​[(βu(n))2]​d​u,Bn:=\ilimits@0T​𝔼​[(βu(n))2​|ρu(n)|2]​d​u,Cn:=\ilimits@0T​𝔼​[(βu(n))2​|Su|2]​d​u.A\_{n}:=\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}\big]\,du,\qquad B\_{n}:=\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}|\rho^{(n)}\_{u}|^{2}\big]\,du,\qquad C\_{n}:=\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}|S\_{u}|^{2}\big]\,du. |  |

By Lemma [3.3](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), An→0A\_{n}\to 0.

For BnB\_{n}, apply Hölder’s inequality on the product space ([0,T]×,dt⊗dℙ)([0,T]\times\Omega,\,dt\otimes d\mathbb{P}) with conjugate exponents p>1p>1, q:=pp−1∈(1,∞)q:=\frac{p}{p-1}\in(1,\infty):

|  |  |  |
| --- | --- | --- |
|  | Bn=\|​(β(n))2​|ρ(n)|2​\|L1≤\|​(β(n))2​\|Lq​\|​|ρ(n)|2​\|Lp.B\_{n}=\|(\beta^{(n)})^{2}\,|\rho^{(n)}|^{2}\|\_{L^{1}}\ \leq\ \|(\beta^{(n)})^{2}\|\_{L^{q}}\ \||\rho^{(n)}|^{2}\|\_{L^{p}}. |  |

Since 0≤(β(n))2≤10\leq(\beta^{(n)})^{2}\leq 1, we have (β(n))2​q≤(β(n))2(\beta^{(n)})^{2q}\leq(\beta^{(n)})^{2} and hence
\|​(β(n))2​\|Lq≤An1/q\|(\beta^{(n)})^{2}\|\_{L^{q}}\leq A\_{n}^{1/q}. By Assumption [3.4](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem4 "Assumption 3.4. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"),
\|​|ρ(n)|2​\|Lp=(\ilimits@0T​𝔼​|ρu(n)|2​p​d​u)1/p≤C\||\rho^{(n)}|^{2}\|\_{L^{p}}=(\intslop\ilimits@\_{0}^{T}\mathbb{E}|\rho^{(n)}\_{u}|^{2p}du)^{1/p}\leq C uniformly in nn.
Therefore Bn≤C​An1/q→0B\_{n}\leq C\,A\_{n}^{1/q}\to 0.

For CnC\_{n}, fix A>0A>0 and split

|  |  |  |
| --- | --- | --- |
|  | Cn=\ilimits@0T​𝔼​[(βu(n))2​|Su|2​𝟏{|Su|≤A}]​d​u+\ilimits@0T​𝔼​[(βu(n))2​|Su|2​𝟏{|Su|>A}]​d​u≤A2​An+\ilimits@0T​𝔼​[|Su|2​𝟏{|Su|>A}]​d​u.C\_{n}=\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}|S\_{u}|^{2}\mathbf{1}\_{\{|S\_{u}|\leq A\}}\big]\,du+\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}|S\_{u}|^{2}\mathbf{1}\_{\{|S\_{u}|>A\}}\big]\,du\ \leq\ A^{2}A\_{n}+\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[|S\_{u}|^{2}\mathbf{1}\_{\{|S\_{u}|>A\}}\big]\,du. |  |

The second term is independent of nn and goes to 0 as A→∞A\to\infty because
\ilimits@0T​𝔼​|Su|2​d​u<∞\intslop\ilimits@\_{0}^{T}\mathbb{E}|S\_{u}|^{2}\,du<\infty (from ([3.1](https://arxiv.org/html/2511.01486v2#S3.E1 "Equation 3.1 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and Assumption [3.1](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).
Hence, given ε>0\varepsilon>0, choose AA such that the tail term ≤ε\leq\varepsilon, and then nn large so that A2​An≤εA^{2}A\_{n}\leq\varepsilon, yielding Cn≤2​εC\_{n}\leq 2\varepsilon for nn large. Combining, we obtain An+Bn+Cn→0A\_{n}+B\_{n}+C\_{n}\to 0, and the claim follows.
∎

The above analysis hinges on the following precise identification, which also
motivates our choice of the functional form for measuring ambiguity.

###### Proposition 3.8.

For any sub–σ\sigma–algebra 𝒢⊂ℱ\mathcal{G}\subset\mathcal{F} and any X∈L2(;ℝd)X\in L^{2}(\Omega;\mathbb{R}^{d}),

|  |  |  |
| --- | --- | --- |
|  | infz∈ℝdW22​(ℒ​(X​𝒢),δz)=W22​(ℒ​(X​𝒢),δ𝔼​[X​𝒢])=Var​(X​𝒢).\inf\_{z\in\mathbb{R}^{d}}W\_{2}^{2}\big(\mathcal{L}(X\mid\mathcal{G}),\delta\_{z}\big)=W\_{2}^{2}\big(\mathcal{L}(X\mid\mathcal{G}),\delta\_{\mathbb{E}[X\mid\mathcal{G}]}\big)=\mathrm{Var}(X\mid\mathcal{G}). |  |

Consequently, the choice

|  |  |  |
| --- | --- | --- |
|  | βt(n)=β​(W2​(ℒ​(St​𝒢tn),δS^t(n)))=β​(Var​(St​𝒢tn))\beta^{(n)}\_{t}=\beta\!\Big(W\_{2}\!\big(\mathcal{L}(S\_{t}\mid\mathcal{G}^{n}\_{t}),\delta\_{\mathaccent 866{S}^{(n)}\_{t}}\big)\Big)=\beta\!\Big(\sqrt{\mathrm{Var}(S\_{t}\mid\mathcal{G}^{n}\_{t})}\Big) |  |

shrinks to 0 exactly at the (square–root) rate at which the conditional variance vanishes.

###### Proof.

Immediate from Lemma [2.2](https://arxiv.org/html/2511.01486v2#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1 Preliminaries and Model Set-Up ‣ 2 Differential Beliefs and Convergence to an Efficient Market ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") by minimizing over zz.
∎

### 3.3 Rate of Information Convergence

Suppose, in addition, that for some η∈(0,1]\eta\in(0,1] and all u∈[0,T]u\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​Var​(Su​𝒢un)≤C​n−2​η(a numerical rate of information gain).\mathbb{E}\,\mathrm{Var}\!\big(S\_{u}\mid\mathcal{G}^{n}\_{u}\big)\ \leq\ C\,n^{-2\eta}\qquad\text{(a numerical rate of information gain).} |  | (3.10) |

Assume further that β\beta is *globally* Lipschitz on [0,∞)[0,\infty) with constant LβL\_{\beta} and β​(0)=0\beta(0)=0.
Then, recalling γu(n)=Var​(Su​𝒢un)\gamma^{(n)}\_{u}=\sqrt{\mathrm{Var}(S\_{u}\mid\mathcal{G}^{n}\_{u})},

|  |  |  |
| --- | --- | --- |
|  | (βu(n))2=β​(γu(n))2≤Lβ2​Var​(Su​𝒢un),hence\ilimits@0T​𝔼​(βu(n))2​d​u≤C​Lβ2​n−2​η.\big(\beta^{(n)}\_{u}\big)^{2}=\beta(\gamma^{(n)}\_{u})^{2}\ \leq\ L\_{\beta}^{2}\,\mathrm{Var}\!\big(S\_{u}\mid\mathcal{G}^{n}\_{u}\big),\qquad\text{hence}\qquad\intslop\ilimits@\_{0}^{T}\mathbb{E}\big(\beta^{(n)}\_{u}\big)^{2}\,du\ \leq\ C\,L\_{\beta}^{2}\,n^{-2\eta}. |  |

To convert this into a rate for 𝔼​[supt≤T|S~t(n)−St|2]\mathbb{E}\big[\sup\_{t\leq T}|\mathaccent 869{S}^{(n)}\_{t}-S\_{t}|^{2}\big], we need to control the
mixed terms containing |S|2|S|^{2} and |ρ(n)|2|\rho^{(n)}|^{2} appearing in ([3.9](https://arxiv.org/html/2511.01486v2#S3.E9 "Equation 3.9 ‣ Theorem 3.6. ‣ 3.2 Stability and Convergence to the True Process ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).
Assume the following fourth–moment bounds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | \ilimits@0T​𝔼​|Su|4​d​u<∞,supn≥1\ilimits@0T​𝔼​[|ρu(n)|4]​d​u<∞.\intslop\ilimits@\_{0}^{T}\mathbb{E}|S\_{u}|^{4}\,du\ <\ \infty,\qquad\sup\_{n\geq 1}\ \intslop\ilimits@\_{0}^{T}\mathbb{E}\big[|\rho^{(n)}\_{u}|^{4}\big]\,du\ <\ \infty. |  | (3.11) |

###### Proposition 3.9.

Under ([3.10](https://arxiv.org/html/2511.01486v2#S3.E10 "Equation 3.10 ‣ 3.3 Rate of Information Convergence ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), the global Lipschitz condition on β\beta, and ([3.11](https://arxiv.org/html/2511.01486v2#S3.E11 "Equation 3.11 ‣ 3.3 Rate of Information Convergence ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")),
there exists C′=C′​(L,T,Lβ,data)C^{\prime}=C^{\prime}(L,T,L\_{\beta},\text{data}) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt≤T|S~t(n)−St|2]≤C′​n−η,n→∞.\mathbb{E}\Big[\sup\_{t\leq T}\big|\mathaccent 869{S}^{(n)}\_{t}-S\_{t}\big|^{2}\Big]\ \leq\ C^{\prime}\,n^{-\eta},\qquad n\to\infty. |  |

###### Proof.

From ([3.9](https://arxiv.org/html/2511.01486v2#S3.E9 "Equation 3.9 ‣ Theorem 3.6. ‣ 3.2 Stability and Convergence to the True Process ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) with t=Tt=T and Gronwall’s inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝔼[sups≤T||2s(n)]≤C\ilimits@0T𝔼[(βu(n))2]du+C\ilimits@0T𝔼[(βu(n))2|ρu(n)|2]du+C\ilimits@0T𝔼[(βu(n))2|Su|2]du,\mathbb{E}\Big[\sup\_{s\leq T}\big|{}^{(n)}\_{s}\big|^{2}\Big]\ \leq\ C\!\intslop\ilimits@\_{0}^{T}\mathbb{E}\Big[(\beta^{(n)}\_{u})^{2}\Big]\,du+C\!\intslop\ilimits@\_{0}^{T}\mathbb{E}\Big[(\beta^{(n)}\_{u})^{2}|\rho^{(n)}\_{u}|^{2}\Big]\,du+C\!\intslop\ilimits@\_{0}^{T}\mathbb{E}\Big[(\beta^{(n)}\_{u})^{2}|S\_{u}|^{2}\Big]\,du, |  |

with C=C​(L,T)C=C(L,T). Denote

|  |  |  |
| --- | --- | --- |
|  | An:=\ilimits@0T​𝔼​[(βu(n))2]​d​u,Bn:=\ilimits@0T​𝔼​[(βu(n))2​|ρu(n)|2]​d​u,Cn:=\ilimits@0T​𝔼​[(βu(n))2​|Su|2]​d​u.A\_{n}:=\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}\big]\,du,\qquad B\_{n}:=\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}|\rho^{(n)}\_{u}|^{2}\big]\,du,\qquad C\_{n}:=\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{2}|S\_{u}|^{2}\big]\,du. |  |

By the computation above, An≤C​Lβ2​n−2​ηA\_{n}\leq CL\_{\beta}^{2}n^{-2\eta}. Since 0≤βu(n)≤10\leq\beta^{(n)}\_{u}\leq 1, we have (βu(n))4≤(βu(n))2(\beta^{(n)}\_{u})^{4}\leq(\beta^{(n)}\_{u})^{2} and hence

|  |  |  |
| --- | --- | --- |
|  | \ilimits@0T​𝔼​[(βu(n))4]​d​u≤An≤C​Lβ2​n−2​η.\intslop\ilimits@\_{0}^{T}\mathbb{E}\big[(\beta^{(n)}\_{u})^{4}\big]\,du\ \leq\ A\_{n}\ \leq\ CL\_{\beta}^{2}n^{-2\eta}. |  |

By Hölder’s inequality on ([0,T]×,dt⊗dℙ)([0,T]\times\Omega,dt\otimes d\mathbb{P}) with exponents (2,2)(2,2) and ([3.11](https://arxiv.org/html/2511.01486v2#S3.E11 "Equation 3.11 ‣ 3.3 Rate of Information Convergence ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")),

|  |  |  |
| --- | --- | --- |
|  | Bn≤(\ilimits@0T​𝔼​[(βu(n))4]​d​u)1/2​(\ilimits@0T​𝔼​[|ρu(n)|4]​d​u)1/2≤C​n−η,B\_{n}\leq\Big(\intslop\ilimits@\_{0}^{T}\mathbb{E}[(\beta^{(n)}\_{u})^{4}]\,du\Big)^{1/2}\Big(\intslop\ilimits@\_{0}^{T}\mathbb{E}[|\rho^{(n)}\_{u}|^{4}]\,du\Big)^{1/2}\ \leq\ C\,n^{-\eta}, |  |

and similarly

|  |  |  |
| --- | --- | --- |
|  | Cn≤(\ilimits@0T​𝔼​[(βu(n))4]​d​u)1/2​(\ilimits@0T​𝔼​[|Su|4]​d​u)1/2≤C​n−η.C\_{n}\leq\Big(\intslop\ilimits@\_{0}^{T}\mathbb{E}[(\beta^{(n)}\_{u})^{4}]\,du\Big)^{1/2}\Big(\intslop\ilimits@\_{0}^{T}\mathbb{E}[|S\_{u}|^{4}]\,du\Big)^{1/2}\ \leq\ C\,n^{-\eta}. |  |

Thus An+Bn+Cn≤C′​(n−2​η+n−η+n−η)≤C′′​n−ηA\_{n}+B\_{n}+C\_{n}\leq C^{\prime}(n^{-2\eta}+n^{-\eta}+n^{-\eta})\leq C^{\prime\prime}\,n^{-\eta}, and the claim follows.
∎

### 3.4 Simulation of the Shrinking Bias

We work on a filtered probability space (,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}) carrying a one–dimensional Brownian motion WW. The *true* price process SS solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=α​(t,St)​d​t+σ​(t,St)​d​Wt,S0>0,dS\_{t}=\alpha(t,S\_{t})\,dt+\sigma(t,S\_{t})\,dW\_{t},\qquad S\_{0}>0, |  | (3.12) |

and for the simulation we again take the geometric Brownian motion (GBM) model

|  |  |  |
| --- | --- | --- |
|  | α​(t,x)=μ⋆​x,σ​(t,x)=σ⋆​x.\alpha(t,x)=\mu\_{\star}x,\qquad\sigma(t,x)=\sigma\_{\star}x. |  |

We set the weight function to be

|  |  |  |
| --- | --- | --- |
|  | βt(n)= 1−exp⁡(−κb​(γt(n))pb)= 1−exp⁡(−κb​(Var​(St​𝒢tn))pb/2),κb=10−3,pb=2.4.\beta^{(n)}\_{t}\;=\;1-\exp\!\Big(-\kappa\_{b}\,(\gamma^{(n)}\_{t})^{p\_{b}}\Big)\;=\;1-\exp\!\Big(-\kappa\_{b}\,\big(\mathrm{Var}(S\_{t}\mid\mathcal{G}^{n}\_{t})\big)^{p\_{b}/2}\Big),\quad\kappa\_{b}=10^{-3},\ p\_{b}=2.4. |  |

We use a specification of ρ(n)\rho^{(n)} proportional to the conditional mean (amplified by relative ambiguity):

|  |  |  |
| --- | --- | --- |
|  | ρt(n)=μop​S^t(n)​(1+crel​γt(n)S^t(n)+ε),μop>0,crel≥0,ε>0.\rho^{(n)}\_{t}=\mu\_{\mathrm{op}}\,\mathaccent 866{S}^{(n)}\_{t}\Big(1+c\_{\mathrm{rel}}\frac{\gamma^{(n)}\_{t}}{\mathaccent 866{S}^{(n)}\_{t}+\varepsilon}\Big),\qquad\mu\_{\mathrm{op}}>0,\ c\_{\mathrm{rel}}\geq 0,\ \varepsilon>0. |  |

The synthetic price S~(n)\mathaccent 869{S}^{(n)} is obtained by convexly mixing the true drift with the opinion drift, with β(n)\beta^{(n)} as weight, and keeping the same diffusion and the same Brownian motion WW:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S~t(n)=[(1−βt(n))​α​(t,S~t(n))+βt(n)​ρt(n)]​d​t+σ​(t,S~t(n))​d​Wt,S~0(n)=S0.d\mathaccent 869{S}^{(n)}\_{t}=\Big[(1-\beta^{(n)}\_{t})\,\alpha\!\big(t,\mathaccent 869{S}^{(n)}\_{t}\big)+\beta^{(n)}\_{t}\,\rho^{(n)}\_{t}\Big]\,dt+\sigma\!\big(t,\mathaccent 869{S}^{(n)}\_{t}\big)\,dW\_{t},\qquad\mathaccent 869{S}^{(n)}\_{0}=S\_{0}. |  | (3.13) |

At zero ambiguity (γt(n)=0\gamma^{(n)}\_{t}=0) one has βt(n)=0\beta^{(n)}\_{t}=0, so ([4.34](https://arxiv.org/html/2511.01486v2#S4.E34 "Equation 4.34 ‣ 4.6 Simulation of the True, Observed and Opinion-Biased Price Processes ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) reduces to the true dynamics ([4.6](https://arxiv.org/html/2511.01486v2#S4.Ex75 "4.6 Simulation of the True, Observed and Opinion-Biased Price Processes ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Under the standard Lipschitz and linear–growth assumptions, increasing information implies γ(n)→0\gamma^{(n)}\to 0, which in turn implies β(n)→0\beta^{(n)}\to 0, and stability yields S~(n)→S\mathaccent 869{S}^{(n)}\to S in L2(;C)L^{2}(\Omega;C). The common Brownian motion WW couples the paths so differences are solely driven by the bias term.

Below are 4×24\times 2 plots, with rows corresponding to information levels n∈{1,10,100,1000}n\in\{1,10,100,1000\}. The true process SS (blue) is on the left, the synthetic process S~(n)\mathaccent 869{S}^{(n)} (red) is on the right. We generated 3030 paths per panel with daily steps over [0,1][0,1] year.

![Refer to caption](Sim2.png)


Figure 2: Ambiguity–driven bias: at low information (n=1,10n=1,10) the synthetic process deviates due to a nonzero β(n)\beta^{(n)}, while as nn increases (100,1000100,1000) the bias weight shrinks and S~(n)\mathaccent 869{S}^{(n)} collapses to SS.

### 3.5 Conclusions

We have constructed a rigorous, explicit mechanism in which a trader’s opinion drift
ρ(n)\rho^{(n)} is convexly combined with the true drift α\alpha, with weight

|  |  |  |
| --- | --- | --- |
|  | βt(n)=β​(W2​(ℒ​(St​𝒢tn),δS^t(n)))=β​(Var​(St​𝒢tn))∈[0,1].\beta^{(n)}\_{t}=\beta\!\Big(W\_{2}\!\big(\mathcal{L}(S\_{t}\mid\mathcal{G}^{n}\_{t}),\delta\_{\mathaccent 866{S}^{(n)}\_{t}}\big)\Big)=\beta\!\Big(\sqrt{\mathrm{Var}(S\_{t}\mid\mathcal{G}^{n}\_{t})}\Big)\ \in[0,1]. |  |

*The Wasserstein distance measures a sense of ambiguity regarding using the estimate S^t\mathaccent 866{S}\_{t} instead of the true value of StS\_{t}*. As the sub–σ\sigma–algebras 𝒢tn\mathcal{G}^{n}\_{t} increase to ℱt\mathcal{F}\_{t} (for each tt),
β(n)\beta^{(n)} vanishes in L2​(d​t⊗d​ℙ)L^{2}(dt\otimes d\mathbb{P}), and the modified (synthetic) price process
([3.6](https://arxiv.org/html/2511.01486v2#S3.E6 "Equation 3.6 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) converges to the true price process ([3.1](https://arxiv.org/html/2511.01486v2#S3.E1 "Equation 3.1 ‣ 3.1 Preliminaries and Model Set-Up ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) in
L2(;C([0,T];ℝd))L^{2}(\Omega;C([0,T];\mathbb{R}^{d})) ([Theorem˜3.7](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.2 Stability and Convergence to the True Process ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). The shrinking mechanism is
explicitly tied to the conditional variance of StS\_{t} given the current information level (Proposition [3.8](https://arxiv.org/html/2511.01486v2#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2 Stability and Convergence to the True Process ‣ 3 Individual Biases under Increasing Information ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).

## 4 Optimal Aggregation of Expert Opinions under Information Constraints

### 4.1 Preliminaries and Model Set-Up

We now study an optimal aggregation problem where a *trader is acting under information constraints 𝔾⊂𝔽\mathbb{G}\subset\mathbb{F} and consults a (now possibly continuous) set of experts*, represented by some compact space , who propose corrections to the observed drift, represented by expert-indexed flows of probability measures ρλ\rho^{\lambda}, which the *trader wishes to aggregate to obtain the best estimate of the unknown true drift aa*. The trader tries to minimize the distance between the aggregated correction term ρbar\bar{\rho} and the trader’s own estimate a^\mathaccent 866{a} based on available information 𝔾\mathbb{G}, taking into account their own prior beliefs on the expert community, represented by a flow π\pi of probability measures over . From a financial point of view, the trader is seeking positive alphas as defined in [[29](https://arxiv.org/html/2511.01486v2#bib.bib29)], i.e. an arbitrage opportunity or a dominated asset.

We fix a finite horizon T>0T>0 and a filtered probability space
(,ℱ,𝔽=(ℱt)0≤t≤T,ℙ)(\Omega,\mathcal{F},\mathbb{F}=(\mathcal{F}\_{t})\_{0\leq t\leq T},\mathbb{P}) satisfying the usual conditions. Let WW and BB be independent one–dimensional 𝔽\mathbb{F}–Brownian motions.
Assume the stock price follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | dSt=atdt+σtdWt,S0∈L2(,ℱ0,ℙ),dS\_{t}=a\_{t}\,dt+\sigma\_{t}\,dW\_{t},\qquad S\_{0}\in L^{2}(\Omega,\mathcal{F}\_{0},\mathbb{P}), |  | (4.1) |

with a,σa,\sigma 𝔽\mathbb{F}–progressively measurable and 𝔼​\ilimits@0T​|at|​d​t<∞,𝔼​\ilimits@0T​σt2​d​t<∞,σt≥0​a.s.\mathbb{E}\!\intslop\ilimits@\_{0}^{T}|a\_{t}|\,dt<\infty,\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\sigma\_{t}^{2}\,dt<\infty,\sigma\_{t}\geq 0\ \text{a.s.}

We assume that SS is only *partially observable* and the trader is only able to observe the process YY given by

|  |  |  |
| --- | --- | --- |
|  | d​Yt=ht​(St)​d​t+Rt1/2​d​Bt,Rt∈[r−,r+]​ a.s. for some ​0<r−≤r+<∞,dY\_{t}\;=\;h\_{t}(S\_{t})\,dt\;+\;R\_{t}^{1/2}\,dB\_{t},\qquad R\_{t}\in[r\_{-},r\_{+}]\text{ a.s. for some }0<r\_{-}\leq r\_{+}<\infty, |  |

where hh is 𝔾\mathbb{G}–progressively measurable with ht:ℝ→ℝh\_{t}:\mathbb{R}\to\mathbb{R} and linear growth
|ht​(x)|≤C​(1+|x|)|h\_{t}(x)|\leq C(1+|x|) a.s.
Define the observation filtration 𝔾\mathbb{G} as the usual augmentation of
σ(Ys:0≤s≤t)\sigma(Y\_{s}:0\leq s\leq t). Set

|  |  |  |
| --- | --- | --- |
|  | h^t:=𝔼[ht(St)|𝒢t].W^t:=\ilimits@0tRs−1/2(dYs−h^sds).\mathaccent 866{h}\_{t}:=\mathbb{E}\!\left[h\_{t}(S\_{t})\,\middle|\,\mathcal{G}\_{t}\right].\qquad\mathaccent 866{W}\_{t}\ :=\ \intslop\ilimits@\_{0}^{t}R\_{s}^{-1/2}\big(dY\_{s}-\mathaccent 866{h}\_{s}\,ds\big). |  |

Then W^\mathaccent 866{W} is the innovation process, see [[6](https://arxiv.org/html/2511.01486v2#bib.bib6), [34](https://arxiv.org/html/2511.01486v2#bib.bib34)], which is a 𝔾\mathbb{G}–Brownian motion, and the following standard representation holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=h^t​d​t+Rt1/2​d​W^t.dY\_{t}\ =\ \mathaccent 866{h}\_{t}\,dt\ +\ R\_{t}^{1/2}\,d\mathaccent 866{W}\_{t}. |  | (4.2) |

Consider the (conditional–mean) filter S^t:=𝔼​[St​𝒢t]\mathaccent 866{S}\_{t}:=\mathbb{E}[S\_{t}\mid\mathcal{G}\_{t}].
Under the integrability condition above, S^\mathaccent 866{S} is an 𝔾\mathbb{G}–continuous semimartingale with the *innovation representation*

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S^t=a^t​d​t+σ^t​d​W^t,d\mathaccent 866{S}\_{t}\;=\;\mathaccent 866{a}\_{t}\,dt\;+\;\mathaccent 866{\sigma}\_{t}\,d\mathaccent 866{W}\_{t}, |  | (4.3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | a^t:=𝔼​[at​𝒢t],σ^t:=(𝔼​[St​ht​𝒢t]−𝔼​[St​𝒢t]​𝔼​[ht​𝒢t])​Rt−1/2.\mathaccent 866{a}\_{t}\;:=\;\mathbb{E}[a\_{t}\mid\mathcal{G}\_{t}],\qquad\mathaccent 866{\sigma}\_{t}\;:=\;\big(\mathbb{E}[S\_{t}h\_{t}\mid\mathcal{G}\_{t}]-\mathbb{E}[S\_{t}\mid\mathcal{G}\_{t}]\mathbb{E}[h\_{t}\mid\mathcal{G}\_{t}]\big)R\_{t}^{-1/2}. |  | (4.4) |

Writing πt​(φ):=𝔼​[φ​(St)​𝒢t]\pi\_{t}(\varphi):=\mathbb{E}[\varphi(S\_{t})\mid\mathcal{G}\_{t}], ([4.3](https://arxiv.org/html/2511.01486v2#S4.E3 "Equation 4.3 ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"))–([4.4](https://arxiv.org/html/2511.01486v2#S4.E4 "Equation 4.4 ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) follow from the standard Kushner–Stratonovich equation, see [[6](https://arxiv.org/html/2511.01486v2#bib.bib6), [34](https://arxiv.org/html/2511.01486v2#bib.bib34)],

|  |  |  |
| --- | --- | --- |
|  | d​πt​(φ)=πt​(at)​d​t+(πt​(φ​ht)−πt​(φ)​πt​(ht))​Rt−1/2​d​W^td\pi\_{t}(\varphi)=\pi\_{t}(a\_{t})\,dt+\big(\pi\_{t}(\varphi h\_{t})-\pi\_{t}(\varphi)\pi\_{t}(h\_{t})\big)\,R\_{t}^{-1/2}\,d\mathaccent 866{W}\_{t} |  |

for the test function φ​(x)=x\varphi(x)=x.

Besides partial observability, we incorporate *expert biases* by defining the expert-indexed proposal drifts ρλ≔(ρtλ)0≤t≤T\rho^{\lambda}\coloneqq(\rho\_{t}^{\lambda})\_{0\leq t\leq T} such that the real-valued map (t,ω,λ)↦ρtλ​(w)(t,\omega,\lambda)\mapsto\rho^{\lambda}\_{t}(w) is 𝒫​(𝔾)⊗ℬ​()\mathcal{P}(\mathbb{G})\otimes\mathcal{B}(\Lambda)-measurable and m=(mt)0≤t≤Tm=(m\_{t})\_{0\leq t\leq T} is a 𝔾\mathbb{G}-progressively measurable flow of probability kernels on which is some compact metric space representing the set of experts that, for simplicity, we take to be [0,1][0,1], and let

|  |  |  |
| --- | --- | --- |
|  | ρbart​(mt):=\ilimits@​ρtλ​mt​(d​λ)\bar{\rho}\_{t}(m\_{t})\;:=\;\intslop\ilimits@\rho\_{t}^{\lambda}\,m\_{t}(d\lambda) |  |

be the *aggregated bias/correction term* at time tt, and mm is the aggregator which dynamically assigns weight to each expert’s opinion. With a progressively measurable weight process β=(βt)0≤t≤T\beta=(\beta\_{t})\_{0\leq t\leq T} taking values in [0,1][0,1], we define the *bias–adjusted filtered price* S~\mathaccent 869{S} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S~t=(a^t+βt​(ρbart​(mt)−a^t))​d​t+σ^t​d​W^t.d\mathaccent 869{S}\_{t}\;=\;\Big(\mathaccent 866{a}\_{t}\;+\;\beta\_{t}\big(\bar{\rho}\_{t}(m\_{t})-\mathaccent 866{a}\_{t}\big)\Big)\,dt\;+\;\mathaccent 866{\sigma}\_{t}\,d\mathaccent 866{W}\_{t}. |  | (4.5) |

Thus βt≡0\beta\_{t}\equiv 0 recovers the baseline filter ([4.3](https://arxiv.org/html/2511.01486v2#S4.E3 "Equation 4.3 ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), while βt≡1\beta\_{t}\equiv 1 replaces the filtered drift by the aggregated bias ρbart​(mt)\bar{\rho}\_{t}(m\_{t}). Below, π=(πt)0≤t≤T\pi=(\pi\_{t})\_{0\leq t\leq T} is an 𝔾\mathbb{G}–progressively measurable flow of probability kernels on representing the prior beliefs of the trader regarding the experts. Note that the bias-adjusted price process can be written in the following equivalent form, emphasizing the fact that the *trader forms a convex combination of the observed drift with the proposed correction term*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S~t=((1−βt)​a^t+βt​ρbart​(mt))​d​t+σ^t​d​W^t.d\mathaccent 869{S}\_{t}\;=\;\Big((1-\beta\_{t})\mathaccent 866{a}\_{t}\;+\;\beta\_{t}\bar{\rho}\_{t}(m\_{t})\Big)\,dt\;+\;\mathaccent 866{\sigma}\_{t}\,d\mathaccent 866{W}\_{t}. |  | (4.6) |

We measure the discrepancy between ρbar\bar{\rho} and a^\mathaccent 866{a} by the functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(m):=𝔼​\ilimits@0T​γ2​(ρbart​(mt)−a^t)2​d​t,γ>0,\mathcal{L}(m)\ :=\ \mathbb{E}\!\intslop\ilimits@\_{0}^{T}\frac{\gamma}{2}\,\big(\bar{\rho}\_{t}(m\_{t})-\mathaccent 866{a}\_{t}\big)^{2}\,dt,\qquad\gamma>0, |  | (4.7) |

which is convex in mm because m↦ρbart​(m)m\mapsto\bar{\rho}\_{t}(m) is linear.

Finally, for flows of measures m,πm,\pi as above, we define the time–integrated relative entropy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟KL​(m​\|​π):=𝔼​\ilimits@0T​KL​(mt​\|​πt)​d​t=𝔼​\ilimits@0T​\ilimits@​log⁡(d​mtd​πt)​mt​(d​λ)​d​t,\mathcal{D}\_{\mathrm{KL}}(m\|\pi):=\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}\!\big(m\_{t}\|\pi\_{t}\big)\,dt=\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\!\intslop\ilimits@\log\!\Big(\frac{dm\_{t}}{d\pi\_{t}}\Big)\,m\_{t}(d\lambda)\,dt, |  | (4.8) |

with KL​(mt​\|​πt)=+∞\mathrm{KL}(m\_{t}\|\pi\_{t})=+\infty if mt​πtm\_{t}\nll\pi\_{t}.

###### Problem 4.1.

Fix 0<K<∞0<K<\infty. Minimize ℒ​(m)\mathcal{L}(m) over 𝔾\mathbb{G}–progressively measurable flows of probability kernels m=(mt)t∈[0,T]m=(m\_{t})\_{t\in[0,T]} subject to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟KL​(m​\|​π)≤K,mt≪πta.s. for a.e. ​t.\mathcal{D}\_{\mathrm{KL}}(m\|\pi)\ \leq\ K,\qquad m\_{t}\ll\pi\_{t}\quad\text{a.s.\ for a.e.\ }t. |  | (4.9) |

Thus, we study an optimization problem where the *trader wants to select an optimal aggregator process* m∗m^{\ast} such that the posited drift is close to the filtered drift a^\mathaccent 866{a}, while keeping mm close to the given prior π\pi. We make the following assumptions.

###### Assumption 4.2.

1. (A1)

   For
   each (t,ω)(t,\omega), λ↦ρtλ​(ω)\lambda\mapsto\rho\_{t}^{\lambda}(\omega) is continuous and (t,ω,λ)↦ρtλ​(ω)(t,\omega,\lambda)\mapsto\rho\_{t}^{\lambda}(\omega) is bounded.
2. (A2)

   a^=(a^t)0≤t≤T\mathaccent 866{a}=(\mathaccent 866{a}\_{t})\_{0\leq t\leq T} satisfies 𝔼​\ilimits@0T​|a^t|2​d​t<∞\displaystyle\mathbb{E}\intslop\ilimits@\_{0}^{T}|\mathaccent 866{a}\_{t}|^{2}\,dt<\infty.
3. (A3)

   For each fixed tt, the kernel πt\pi\_{t} has full support. Since is compact and λ↦ρtλ\lambda\mapsto\rho\_{t}^{\lambda} is bounded, the log–moment generating function

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (η)t:=log\ilimits@eη​ρtλπt(dλ){}\_{t}(\eta)\ :=\ \log\!\intslop\ilimits@e^{\eta\,\rho\_{t}^{\lambda}}\,\pi\_{t}(d\lambda) |  | (4.10) |

   is finite for all η∈ℝ\eta\in\mathbb{R}, a.s., for a.e. tt.
4. (A4)

   m=(mt)0≤t≤Tm=(m\_{t})\_{0\leq t\leq T} satisfies mt≪πtm\_{t}\ll\pi\_{t} a.s. for a.e. tt.

###### Assumption 4.3.

For a.e. (t,ω)(t,\omega), the filtered drift a^t​(ω)\mathaccent 866{a}\_{t}(\omega) belongs to the closed convex hull of the expert range:

|  |  |  |
| --- | --- | --- |
|  | a^t(ω)∈co¯{ρtλ(ω):λ∈}=[infλρtλ(ω),supλρtλ(ω)].\mathaccent 866{a}\_{t}(\omega)\ \in\ \overline{\mathrm{co}}\big\{\rho\_{t}^{\lambda}(\omega):\lambda\in\Lambda\big\}\ =\ \big[\mathrm{inf}\_{\lambda}\rho\_{t}^{\lambda}(\omega),\ \mathrm{sup}\_{\lambda}\rho\_{t}^{\lambda}(\omega)\big]. |  |

###### Problem 4.4.

Minimize ℒ​(m)\mathcal{L}(m) in ([4.7](https://arxiv.org/html/2511.01486v2#S4.E7 "Equation 4.7 ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) over *all* 𝔽\mathbb{F}–progressively measurable flows of probability kernels m=(mt)0≤t≤Tm=(m\_{t})\_{0\leq t\leq T} on (no absolute continuity requirement with respect to π\pi).

###### Proposition 4.5.

Under Assumption [4.3](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem3 "Assumption 4.3. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), Problem [4.4](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem4 "Problem 4.4. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") has minimal value 0. Moreover, there exists an 𝔽\mathbb{F}–progressively measurable flow m0=(mt0)t∈[0,T]m^{0}=(m\_{t}^{0})\_{t\in[0,T]} such that

|  |  |  |
| --- | --- | --- |
|  | ρbart​(mt0)=\ilimits@​ρtλ​mt0​(d​λ)=a^ta.s. for a.e. ​t,\bar{\rho}\_{t}(m\_{t}^{0})\ =\ \intslop\ilimits@\rho\_{t}^{\lambda}\,m\_{t}^{0}(d\lambda)\ =\ \mathaccent 866{a}\_{t}\quad\text{a.s.\ for a.e.\ }t, |  |

so ℒ​(m0)=0\mathcal{L}(m^{0})=0.

###### Remark 4.6.

In Problem [4.1](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem1 "Problem 4.1. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), for each finite KK we keep the absolute continuity constraint mt≪πtm\_{t}\ll\pi\_{t}. As K↑∞K\uparrow\infty, the KL constraint becomes asymptotically nonbinding and the optimizers may concentrate (in the limit) on sets of πt\pi\_{t}–measure zero; thus Problem [4.1](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem1 "Problem 4.1. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") –converges to Problem [4.4](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem4 "Problem 4.4. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), and the minimum loss approaches 0.

###### Remark 4.7.

Basic facts regarding measurability properties of flows of probability kernels are collected in the appendix, where references are also given. In the following, we will use some techniques from the theory of relaxed controls, see e.g. [[10](https://arxiv.org/html/2511.01486v2#bib.bib10)], [[2](https://arxiv.org/html/2511.01486v2#bib.bib2)], [[16](https://arxiv.org/html/2511.01486v2#bib.bib16)]. In particular, once a 𝔾\mathbb{G}-adapted relaxed control Q​(ω,d​t,d​λ)Q(\omega,dt,d\lambda) is disintegrated into a product d​t​Q​(t,ω,d​λ)dtQ(t,\omega,d\lambda), the Proposition 6.41, p.584, [[10](https://arxiv.org/html/2511.01486v2#bib.bib10)], allows to choose a 𝔾\mathbb{G}-progressively measurable version of (t,ω)→Q​(t,ω,d​λ)(t,\omega)\to Q(t,\omega,d\lambda), hence we do not always differentiate between adaptedness and progressiveness below.

###### Lemma 4.8.

Equip 𝒫​()\mathcal{P}(\Lambda) with the weak topology. The map
(μ,ν)↦KL​(μ​\|​ν)(\mu,\nu)\mapsto\mathrm{KL}(\mu\|\nu), extended by +∞+\infty when μ​ν\mu\nll\nu,
is Borel and lower semicontinuous on 𝒫​()×𝒫​()\mathcal{P}(\Lambda)\times\mathcal{P}(\Lambda).
Consequently, if m,πm,\pi are 𝔾\mathbb{G}-progressively measurable kernels, then
(t,ω)↦KL​(mt​(ω)​\|​πt​(ω))(t,\omega)\mapsto\mathrm{KL}(m\_{t}(\omega)\|\pi\_{t}(\omega)) is 𝒫​(𝔾)\mathcal{P}(\mathbb{G})–measurable.

###### Proof.

See Tim van Erven, Peter Harremoës, [[15](https://arxiv.org/html/2511.01486v2#bib.bib15)], Theorem 19.
∎

For each (t,ω)(t,\omega) the map μ↦KL​(μ​\|​πt​(ω))\mu\mapsto\mathrm{KL}(\mu\|\pi\_{t}(\omega)) is proper, strictly convex, and lower semicontinuous on 𝒫​()\mathcal{P}(\Lambda) (for the weak topology). Since (A1) ensures that m↦ρbart​(m)m\mapsto\bar{\rho}\_{t}(m) is continuous and bounded on 𝒫​()\mathcal{P}(\Lambda), integrands below will be normal convex integrands in the sense of Rockafellar; this allows the interchange of infimum and integral used later, see [[7](https://arxiv.org/html/2511.01486v2#bib.bib7)], Section 3.2.

For F:𝒫​()→ℝF:\mathcal{P}(\Lambda)\to\mathbb{R}, the (linear) functional derivative δ​Fδ​m​(m,λ)\frac{\delta F}{\delta m}(m,\lambda) is characterized by

|  |  |  |
| --- | --- | --- |
|  | dd​ε​F​((1−ε)​m+ε​m′)|ε=0=\ilimits@​δ​Fδ​m​(m,λ)​(m′−m)​(d​λ),m′∈𝒫​(),\frac{d}{d\varepsilon}F\big((1-\varepsilon)m+\varepsilon m^{\prime}\big)\Big|\_{\varepsilon=0}=\intslop\ilimits@\frac{\delta F}{\delta m}(m,\lambda)\,(m^{\prime}-m)(d\lambda),\quad\forall\,m^{\prime}\in\mathcal{P}(\Lambda), |  |

and we normalize it by \ilimits@​δ​Fδ​m​(m,λ)​m​(d​λ)=0\intslop\ilimits@\frac{\delta F}{\delta m}(m,\lambda)\,m(d\lambda)=0.
For the linear map ρbart​(m)=\ilimits@​ρtλ​m​(d​λ)\bar{\rho}\_{t}(m)=\intslop\ilimits@\rho\_{t}^{\lambda}\,m(d\lambda) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​ρbartδ​m​(m,λ)=ρtλ−ρbart​(m).\frac{\delta\bar{\rho}\_{t}}{\delta m}(m,\lambda)=\rho\_{t}^{\lambda}-\bar{\rho}\_{t}(m). |  | (4.11) |

### 4.2 Existence of the Minimizing Flow

###### Theorem 4.9.

Under Assumption [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), Problem [4.1](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem1 "Problem 4.1. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") admits a solution m∗m^{\ast}.
Moreover, there exists a scalar α∗≥0\alpha^{\ast}\geq 0 such that m∗m^{\ast} minimizes the Lagrangian

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​\ilimits@0T​[γ2​(ρbart​(mt)−a^t)2+α∗​KL​(mt​\|​πt)]​d​t,\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\Big[\tfrac{\gamma}{2}\big(\bar{\rho}\_{t}(m\_{t})-\mathaccent 866{a}\_{t}\big)^{2}+\alpha^{\ast}\,\mathrm{KL}(m\_{t}\|\pi\_{t})\Big]\,dt, |  | (4.12) |

and complementary slackness holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α∗​(𝒟KL​(m∗​\|​π)−K)=0.\alpha^{\ast}\Big(\mathcal{D}\_{\mathrm{KL}}(m^{\ast}\|\pi)-K\Big)=0. |  | (4.13) |

###### Proof.

We begin by setting up some notation. The proof is technical but is in fact a modification of standard arguments used for relaxed controls, which can be found in [[2](https://arxiv.org/html/2511.01486v2#bib.bib2), [16](https://arxiv.org/html/2511.01486v2#bib.bib16)]. Write the optimization over flows m=(mt)t∈[0,T]m=(m\_{t})\_{t\in[0,T]} with the absolute continuity constraint mt≪πtm\_{t}\ll\pi\_{t} by means of the Radon–Nikodým densities

|  |  |  |
| --- | --- | --- |
|  | ft​(ω,λ):=d​mt​(ω,⋅)d​πt​(ω,⋅)​(λ),ft≥0,\ilimits@​ft​(ω,λ)​πt​(ω,d​λ)=1a.s. for a.e. ​t.f\_{t}(\omega,\lambda)\ :=\ \frac{dm\_{t}(\omega,\cdot)}{d\pi\_{t}(\omega,\cdot)}(\lambda),\qquad f\_{t}\geq 0,\qquad\intslop\ilimits@f\_{t}(\omega,\lambda)\,\pi\_{t}(\omega,d\lambda)=1\ \ \text{a.s.\ for a.e.\ }t. |  |

Set

|  |  |  |
| --- | --- | --- |
|  | 𝖷:=×[0,T],ℚ:=ℙ⊗dt,(dω,dt,dλ):=ℙ(dω)dtπt(ω,dλ).\mathsf{X}:=\Omega\times[0,T],\qquad\mathbb{Q}:=\mathbb{P}\otimes dt,\qquad\Pi(d\omega,dt,d\lambda):=\mathbb{P}(d\omega)\,dt\,\pi\_{t}(\omega,d\lambda). |  |

Note is well-defined on (×[0,T]×,𝒫(𝔾)⊗ℬ()(\Omega\times[0,T]\times\Lambda,\mathcal{P}(\mathbb{G})\otimes\mathcal{B}(\Lambda).

Then f∈L1​()f\in L^{1}(\Pi) and the integrated KL constraint can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝒟KL​(m​\|​π)=\ilimits@​f​log⁡f​d.\mathcal{D}\_{\mathrm{KL}}(m\|\pi)\,=\,\intslop\ilimits@f\log f\,d\Pi. |  |

Let Mt​(ω):=supλ∈|ρtλ​(ω)|M\_{t}(\omega):=\sup\_{\lambda\in\Lambda}|\rho\_{t}^{\lambda}(\omega)|; by (A1), M∈L1​(ℚ)M\in L^{1}(\mathbb{Q}) and |ρbart​(mt)|=|\ilimits@​ρtλ​ft​πt​(d​λ)|≤Mt|\bar{\rho}\_{t}(m\_{t})|=\Big|\intslop\ilimits@\rho\_{t}^{\lambda}f\_{t}\,\pi\_{t}(d\lambda)\Big|\leq M\_{t} a.s. for a.e. tt.
Finally, denote

|  |  |  |
| --- | --- | --- |
|  | 𝒜K:={f∈L1​():f≥0,\ilimits@​ft​(ω,λ)​πt​(ω,d​λ)=1ℚ​-a.e.,\ilimits@​f​log⁡f​d≤K}.\mathcal{A}\_{K}\ :=\ \Big\{f\in L^{1}(\Pi):\ f\geq 0,\ \intslop\ilimits@f\_{t}(\omega,\lambda)\,\pi\_{t}(\omega,d\lambda)=1\ \ \mathbb{Q}\text{-a.e.},\ \intslop\ilimits@f\log f\,d\Pi\leq K\Big\}. |  |

Feasibility holds since f≡1∈𝒜Kf\equiv 1\in\mathcal{A}\_{K} (this corresponds to m≡πm\equiv\pi), and 𝒟KL​(π​\|​π)=0<K\mathcal{D}\_{\mathrm{KL}}(\pi\|\pi)=0<K, i.e. Slater’s condition is satisfied.

We now show compactness of the feasible set. Let {fn}⊂𝒜K\{f^{n}\}\subset\mathcal{A}\_{K}. Since \ilimits@​ftn​d​πt=1\intslop\ilimits@f\_{t}^{n}\,d\pi\_{t}=1 ℚ\mathbb{Q}-a.e., we have \|​fn​\|L1​()=\ilimits@​fn​d=\ilimits@​1​d​ℚ=ℚ​(𝖷)<∞\|f^{n}\|\_{L^{1}(\Pi)}=\intslop\ilimits@f^{n}\,d\Pi=\intslop\ilimits@1\,d\mathbb{Q}=\mathbb{Q}(\mathsf{X})<\infty for all nn. Moreover, the KL bound \ilimits@​fn​log⁡fn​d≤K\intslop\ilimits@f^{n}\log f^{n}\,d\Pi\leq K gives uniform integrability of {fn}\{f^{n}\} by the de la Vallée Poussin criterion (use (u)=u​log⁡u−u+1\Phi(u)=u\log u-u+1, which is superlinear and \ilimits@​(fn)​d≤K+ℚ​(𝖷)\intslop\ilimits@\Phi(f^{n})\,d\Pi\leq K+\mathbb{Q}(\mathsf{X})). Hence, by the Dunford–Pettis theorem, there is a subsequence (not relabelled) of {fn}\{f^{n}\} and f∈L1​()f\in L^{1}(\Pi) with fn⇀ff^{n}\rightharpoonup f in L1​()L^{1}(\Pi), i.e. 𝒜K\mathcal{A}\_{K} is relatively weakly compact in L1​()L^{1}(\Pi).

We next verify weak closedness. Let fn∈𝒜Kf^{n}\in\mathcal{A}\_{K} with fn⇀ff^{n}\rightharpoonup f in L1​()L^{1}(\Pi).
Nonnegativity is preserved under L1L^{1}–weak limits. The normalization constraint passes to the limit because for every φ∈L∞​(𝖷)\varphi\in L^{\infty}(\mathsf{X}),

|  |  |  |
| --- | --- | --- |
|  | \ilimits@𝖷​φ​(ω,t)​(\ilimits@​ftn​(ω,λ)​πt​(ω,d​λ))​d​ℚ=\ilimits@​φ​(ω,t)​fn​(ω,t,λ)​d⟶\ilimits@​φ​f​d,\intslop\ilimits@\_{\mathsf{X}}\!\varphi(\omega,t)\Big(\intslop\ilimits@f^{n}\_{t}(\omega,\lambda)\,\pi\_{t}(\omega,d\lambda)\Big)\,d\mathbb{Q}=\intslop\ilimits@\varphi(\omega,t)\,f^{n}(\omega,t,\lambda)\,d\Pi\ \longrightarrow\ \intslop\ilimits@\varphi\,f\,d\Pi, |  |

which implies \ilimits@​f​πt​(d​λ)=1\intslop\ilimits@f\,\pi\_{t}(d\lambda)=1 ℚ\mathbb{Q}-a.e. Likewise, the KL constraint is weakly lower semicontinuous: since u↦u​log⁡uu\mapsto u\log u is convex l.s.c. on [0,∞)[0,\infty), the functional f↦\ilimits@​f​log⁡f​df\mapsto\intslop\ilimits@f\log f\,d\Pi is l.s.c. for the L1L^{1}–weak topology, hence \ilimits@​f​log⁡f​d≤lim infn\ilimits@​fn​log⁡fn​d≤K\intslop\ilimits@f\log f\,d\Pi\leq\liminf\_{n}\intslop\ilimits@f^{n}\log f^{n}\,d\Pi\leq K. We also note that, by standard arguments, integrals of the limiting function ff with respect to πt\pi\_{t} are progressively measurable. Thus 𝒜K\mathcal{A}\_{K} is weakly closed, hence weakly compact in L1​()L^{1}(\Pi).

First we prove existence for bounded targets.
For n∈ℕn\in\mathbb{N}, set the truncation a^t(n):=(−n)∨(a^t∧n)\mathaccent 866{a}^{(n)}\_{t}:=(-n)\vee(\mathaccent 866{a}\_{t}\wedge n). Define the truncated functional

|  |  |  |
| --- | --- | --- |
|  | ℒn​(f):=𝔼​\ilimits@0T​γ2​(\ilimits@​ρtλ​ft​(⋅,λ)​πt​(d​λ)−a^t(n))2​d​t=γ2​\ilimits@𝖷​(Sf​(ω,t)−a^t(n)​(ω))2​d​ℚ,\mathcal{L}\_{n}(f)\ :=\ \mathbb{E}\!\intslop\ilimits@\_{0}^{T}\frac{\gamma}{2}\Big(\textstyle\intslop\ilimits@\rho\_{t}^{\lambda}f\_{t}(\cdot,\lambda)\,\pi\_{t}(d\lambda)-\mathaccent 866{a}^{(n)}\_{t}\Big)^{2}dt=\frac{\gamma}{2}\intslop\ilimits@\_{\mathsf{X}}\Big(S\_{f}(\omega,t)-\mathaccent 866{a}^{(n)}\_{t}(\omega)\Big)^{2}\,d\mathbb{Q}, |  |

where Sf​(ω,t):=\ilimits@​ρtλ​(ω)​ft​(ω,λ)​πt​(ω,d​λ)S\_{f}(\omega,t):=\intslop\ilimits@\rho\_{t}^{\lambda}(\omega)f\_{t}(\omega,\lambda)\,\pi\_{t}(\omega,d\lambda) (note this is just ρbart\bar{\rho}\_{t}).
For each nn, we claim that ℒn\mathcal{L}\_{n} is weakly lower semicontinuous on 𝒜K\mathcal{A}\_{K}. Define (Sf)n≔ℒn(f){}\_{n}(S\_{f})\coloneqq\mathcal{L}\_{n}(f) and note that since x↦(x−a^(n))2x\mapsto(x-\mathaccent 866{a}^{(n)})^{2} is convex and continuous in xx, then by it is standard that (Sf)n{}\_{n}(S\_{f}) is weakly lower semicontinuous as a functional of SfS\_{f}, hence it suffices to show that Sfk⇀SfS\_{f^{k}}\rightharpoonup S\_{f} in L1​(𝖷)L^{1}(\mathsf{X}) as fk⇀ff^{k}\rightharpoonup f in L1​()L^{1}(\Pi). Indeed, if fk⇀ff^{k}\rightharpoonup f in L1​()L^{1}(\Pi), then for any ψ∈L∞​(𝖷)\psi\in L^{\infty}(\mathsf{X}),

|  |  |  |
| --- | --- | --- |
|  | \ilimits@𝖷​ψ​Sfk​d​ℚ=\ilimits@​ψ​(ω,t)​ρtλ​(ω)​fk​(ω,t,λ)​d⟶\ilimits@​ψ​(ω,t)​ρtλ​(ω)​f​(ω,t,λ)​d=\ilimits@𝖷​ψ​Sf​d​ℚ,\intslop\ilimits@\_{\mathsf{X}}\psi S\_{f^{k}}\,d\mathbb{Q}=\intslop\ilimits@\psi(\omega,t)\rho\_{t}^{\lambda}(\omega)\,f^{k}(\omega,t,\lambda)\,d\Pi\ \longrightarrow\ \intslop\ilimits@\psi(\omega,t)\rho\_{t}^{\lambda}(\omega)\,f(\omega,t,\lambda)\,d\Pi=\intslop\ilimits@\_{\mathsf{X}}\psi S\_{f}\,d\mathbb{Q}, |  |

because (ω,t,λ)↦ψ​(ω,t)​ρtλ​(ω)∈L∞​()(\omega,t,\lambda)\mapsto\psi(\omega,t)\rho\_{t}^{\lambda}(\omega)\in L^{\infty}(\Pi) by (A1). Hence Sfk⇀SfS\_{f^{k}}\rightharpoonup S\_{f} in L1​(𝖷)L^{1}(\mathsf{X}).

By the above, 𝒜K\mathcal{A}\_{K} is weakly compact. Since ℒn\mathcal{L}\_{n} is weakly lower semicontinuous on 𝒜K\mathcal{A}\_{K}, there exists a minimizer f(n)∈𝒜Kf^{(n)}\in\mathcal{A}\_{K} of ℒn\mathcal{L}\_{n}.

We now remove the boundedness assumption.
By Step 1, the sequence {f(n)}n≥1⊂𝒜K\{f^{(n)}\}\_{n\geq 1}\subset\mathcal{A}\_{K} is relatively weakly compact in L1​()L^{1}(\Pi). Extract a subsequence (not relabelled) such that f(n)⇀f∗f^{(n)}\rightharpoonup f^{\ast} in L1​()L^{1}(\Pi). Then f∗∈𝒜Kf^{\ast}\in\mathcal{A}\_{K} by the above.

For each fixed ff, we have by elementary algebra

|  |  |  |
| --- | --- | --- |
|  | |(Sf−a^(n))2−(Sf−a^)2|≤2​|Sf−a^|​|a^−a^(n)|+(a^−a^(n))2.\big|(S\_{f}-\mathaccent 866{a}^{(n)})^{2}-(S\_{f}-\mathaccent 866{a})^{2}\big|\leq 2\,|S\_{f}-\mathaccent 866{a}|\,|\mathaccent 866{a}-\mathaccent 866{a}^{(n)}|+(\mathaccent 866{a}-\mathaccent 866{a}^{(n)})^{2}. |  |

By (A1)–(A2), Sf∈L2​(𝖷)S\_{f}\in L^{2}(\mathsf{X}) (since |Sf|≤M∈L2|S\_{f}|\leq M\in L^{2}) and a^(n)→a^\mathaccent 866{a}^{(n)}\to\mathaccent 866{a} in L2​(𝖷)L^{2}(\mathsf{X}). Hence the right-hand side converges to 0 in L1​(𝖷)L^{1}(\mathsf{X}), and thus

|  |  |  |
| --- | --- | --- |
|  | ℒn​(f)→n→∞ℒ​(f):=γ2​\ilimits@𝖷​(Sf−a^)2​d​ℚ.\mathcal{L}\_{n}(f)\ \xrightarrow[n\to\infty]{}\ \mathcal{L}(f):=\frac{\gamma}{2}\intslop\ilimits@\_{\mathsf{X}}\big(S\_{f}-\mathaccent 866{a}\big)^{2}\,d\mathbb{Q}. |  |

Since f(n)⇀f∗f^{(n)}\rightharpoonup f^{\ast} in L1​()L^{1}(\Pi) and f∗∈𝒜Kf^{\ast}\in\mathcal{A}\_{K}, Fatou and the pointwise convergence of ℒn\mathcal{L}\_{n} yield ℒ​(f∗)=inf𝒜Kℒ\mathcal{L}(f^{\ast})=\inf\_{\mathcal{A}\_{K}}\mathcal{L}.

Therefore, with ℓn:=infg∈𝒜Kℒn​(g)=ℒn​(f(n))\ell\_{n}:=\inf\_{g\in\mathcal{A}\_{K}}\mathcal{L}\_{n}(g)=\mathcal{L}\_{n}(f^{(n)}) and ℓ:=infg∈𝒜Kℒ​(g)\ell:=\inf\_{g\in\mathcal{A}\_{K}}\mathcal{L}(g), we have ℓn↓L∞:=limn→∞ℓn\ell\_{n}\downarrow L\_{\infty}:=\lim\_{n\to\infty}\ell\_{n} and, by the previous result and Fatou,

|  |  |  |
| --- | --- | --- |
|  | ℒ​(f∗)≤lim infn→∞ℒn​(f(n))=L∞.\mathcal{L}(f^{\ast})\ \leq\ \liminf\_{n\to\infty}\mathcal{L}\_{n}(f^{(n)})\ =\ L\_{\infty}. |  |

On the other hand, for any g∈𝒜Kg\in\mathcal{A}\_{K}, ℒ​(g)=limn→∞ℒn​(g)≥limn→∞ℓn=L∞\mathcal{L}(g)=\lim\_{n\to\infty}\mathcal{L}\_{n}(g)\geq\lim\_{n\to\infty}\ell\_{n}=L\_{\infty}; taking the infimum over gg yields ℓ≥L∞\ell\geq L\_{\infty}. Combining the two expressions,

|  |  |  |
| --- | --- | --- |
|  | ℓ≤ℒ​(f∗)≤L∞≤ℓ,\ell\ \leq\ \mathcal{L}(f^{\ast})\ \leq\ L\_{\infty}\ \leq\ \ell, |  |

so ℒ​(f∗)=ℓ\mathcal{L}(f^{\ast})=\ell. In terms of kernels mt∗​(ω,d​λ):=ft∗​(ω,λ)​πt​(ω,d​λ)m^{\ast}\_{t}(\omega,d\lambda):=f^{\ast}\_{t}(\omega,\lambda)\,\pi\_{t}(\omega,d\lambda), this proves existence of an optimal adapted flow m∗m^{\ast} for Problem [4.1](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem1 "Problem 4.1. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective").

Finally, we show strong duality and the existence of the Lagrange multiplier. The problem is convex (the map m↦ρbart​(m)m\mapsto\bar{\rho}\_{t}(m) is linear and x↦x2x\mapsto x^{2} is convex; KL is convex) and proper, and Slater’s condition holds. Therefore, classical convex duality yields strong duality and existence of a Lagrange multiplier α∗≥0\alpha^{\ast}\geq 0 such that m∗m^{\ast} minimizes the Lagrangian

|  |  |  |
| --- | --- | --- |
|  | 𝔼​\ilimits@0T​[γ2​(ρbart​(mt)−a^t)2+α∗​KL​(mt​\|​πt)]​d​t\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\!\Big[\tfrac{\gamma}{2}\big(\bar{\rho}\_{t}(m\_{t})-\mathaccent 866{a}\_{t}\big)^{2}+\alpha^{\ast}\,\mathrm{KL}(m\_{t}\|\pi\_{t})\Big]\,dt |  |

over all 𝔾\mathbb{G}–progressively measurable flows mm with mt≪πtm\_{t}\ll\pi\_{t} a.s. for a.e. tt, and hence over all progressively measurable flows, since KL​(mt​\|​πt)=+∞\mathrm{KL}(m\_{t}\|\pi\_{t})=+\infty when mt​πtm\_{t}\nll\pi\_{t}. Moreover, complementary slackness holds:
α∗​(𝒟KL​(m∗​\|​π)−K)=0\alpha^{\ast}\big(\mathcal{D}\_{\mathrm{KL}}(m^{\ast}\|\pi)-K\big)=0.
∎

The Lagrangian integrand is a normal convex integrand in (t,ω,mt)(t,\omega,m\_{t}) in the sense of Rockafellar, hence the minimization problem separates pointwise in (t,ω)(t,\omega) into independent convex problems over 𝒫​()\mathcal{P}(\Lambda).
Fix (t,ω)(t,\omega) and abbreviate a=a^t​(ω)a=\mathaccent 866{a}\_{t}(\omega), ρ​(⋅)=ρt⋅​(ω)\rho(\cdot)=\rho\_{t}^{\cdot}(\omega), and π=πt​(ω)\pi=\pi\_{t}(\omega).
The pointwise problem is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minμ∈𝒫​(),μ≪π⁡f​(μ)\displaystyle\min\_{\mu\in\mathcal{P}(\Lambda),\,\mu\ll\pi}\ f(\mu) | :=γ2​(\ilimits@​ρ​d​μ−a)2+α​KL​(μ​\|​π),α:=α∗≥0.\displaystyle=\frac{\gamma}{2}\Big(\intslop\ilimits@\rho\,d\mu-a\Big)^{2}+\alpha\,\mathrm{KL}(\mu\|\pi),\qquad\alpha=\alpha^{\ast}\geq 0. |  | (4.14) |

### 4.3 Identification of the Form of the Minimizing Measures

Let b​(μ):=\ilimits@​ρ​d​μb(\mu):=\intslop\ilimits@\rho\,d\mu.
By equation [4.11](https://arxiv.org/html/2511.01486v2#S4.E11 "Equation 4.11 ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") and the Gâteaux derivative of KL, the Lions first variation of ff at μ\mu is

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​fδ​μ​(μ,λ)=γ​(b​(μ)−a)​ρ​(λ)+α​(log⁡d​μd​π​(λ)+1)+const,\frac{\delta f}{\delta\mu}(\mu,\lambda)=\gamma\big(b(\mu)-a\big)\,\rho(\lambda)\ +\ \alpha\Big(\log\tfrac{d\mu}{d\pi}(\lambda)+1\Big)\ +\ \mathrm{const}, |  | (4.15) |

with the additive constant fixed by normalization.

At any minimizer μ∗\mu^{\ast} (necessarily with strictly positive density when α>0\alpha>0), the KKT optimality condition yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(b∗−a)​ρ​(λ)+α​(log⁡d​μ∗d​π​(λ)+1)=const,b∗:=\ilimits@​ρ​d​μ∗.\gamma\big(b^{\ast}-a\big)\,\rho(\lambda)+\alpha\Big(\log\tfrac{d\mu^{\ast}}{d\pi}(\lambda)+1\Big)=\mathrm{const},\qquad b^{\ast}:=\intslop\ilimits@\rho\,d\mu^{\ast}. |  | (4.16) |

###### Proposition 4.10.

If α>0\alpha>0, the unique minimizer of ([4.14](https://arxiv.org/html/2511.01486v2#S4.E14 "Equation 4.14 ‣ 4.2 Existence of the Minimizing Flow ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) is the Gibbs measure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​μθ∗​(λ)\displaystyle d\mu^{\ast}\_{\theta}(\lambda) | =e−θ​ρ​(λ)Z​(θ)​π​(d​λ),\displaystyle=\frac{e^{-\theta\,\rho(\lambda)}}{Z(\theta)}\,\pi(d\lambda), |  | (4.17) |
|  | Z​(θ)\displaystyle Z(\theta) | :=\ilimits@​e−θ​ρ​(λ)​π​(d​λ),\displaystyle=\intslop\ilimits@e^{-\theta\rho(\lambda)}\,\pi(d\lambda), |  |
|  | θ\displaystyle\theta | =γα​(b∗−a),\displaystyle=\frac{\gamma}{\alpha}\,(b^{\ast}-a), |  |

with mean

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ​(θ)\displaystyle\psi(\theta) | :=\ilimits@​ρ​d​μθ∗=\ilimits@​ρ​(λ)​e−θ​ρ​(λ)​π​(d​λ)\ilimits@​e−θ​ρ​(λ)​π​(d​λ)=−dd​θ​log⁡Z​(θ).\displaystyle=\intslop\ilimits@\rho\,d\mu^{\ast}\_{\theta}=\frac{\displaystyle\intslop\ilimits@\rho(\lambda)e^{-\theta\rho(\lambda)}\,\pi(d\lambda)}{\displaystyle\intslop\ilimits@e^{-\theta\rho(\lambda)}\,\pi(d\lambda)}=-\frac{d}{d\theta}\log Z(\theta). |  | (4.18) |

The scalar θ\theta is the unique solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(θ)=a+αγ​θ.\psi(\theta)=a+\frac{\alpha}{\gamma}\,\theta. |  | (4.19) |

###### Proof.

Fix (t,ω)(t,\omega) and set ρ:=ρt⋅​(ω)\rho:=\rho\_{t}^{\cdot}(\omega), π:=πt​(ω)\pi:=\pi\_{t}(\omega) and a:=a^t​(ω)a:=\mathaccent 866{a}\_{t}(\omega); we suppress the indices for clarity. For μ≪π\mu\ll\pi set

|  |  |  |
| --- | --- | --- |
|  | F​(μ):=γ2​(b​(μ)−a)2+α​KL​(μ​\|​π),b​(μ):=\ilimits@​ρ​d​μ.F(\mu):=\frac{\gamma}{2}\big(b(\mu)-a\big)^{2}+\alpha\,\mathrm{KL}(\mu\|\pi),\qquad b(\mu):=\intslop\ilimits@\rho\,d\mu. |  |

Assume α>0\alpha>0. By the boundedness of ρ\rho (Assumption [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) the partition function

|  |  |  |
| --- | --- | --- |
|  | Z​(θ):=\ilimits@​e−θ​ρ​(λ)​π​(d​λ)∈(0,∞),θ∈ℝ,Z(\theta):=\intslop\ilimits@e^{-\theta\rho(\lambda)}\,\pi(d\lambda)\in(0,\infty),\qquad\theta\in\mathbb{R}, |  |

is finite and C1C^{1} in θ\theta, with

|  |  |  |
| --- | --- | --- |
|  | ψ​(θ):=\ilimits@​ρ​d​μθ∗=\ilimits@​ρ​e−θ​ρ​d​π\ilimits@​e−θ​ρ​d​π=−dd​θ​log⁡Z​(θ),\psi(\theta):=\intslop\ilimits@\rho\,d\mu\_{\theta}^{\ast}=\frac{\intslop\ilimits@\rho e^{-\theta\rho}\,d\pi}{\intslop\ilimits@e^{-\theta\rho}\,d\pi}=-\frac{d}{d\theta}\log Z(\theta), |  |

where μθ∗\mu\_{\theta}^{\ast} is defined by ([4.17](https://arxiv.org/html/2511.01486v2#S4.E17 "Equation 4.17 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).

The variational formula for KL divergence, see, e.g., [[14](https://arxiv.org/html/2511.01486v2#bib.bib14)], p.29, Lemma 1.4.3, asserts that for any bounded measurable φ\varphi and any μ≪π\mu\ll\pi,

|  |  |  |
| --- | --- | --- |
|  | KL​(μ​\|​π)≥\ilimits@​φ​d​μ−log⁡\ilimits@​eφ​d​π,\mathrm{KL}(\mu\|\pi)\ \geq\ \intslop\ilimits@\varphi\,d\mu-\log\!\intslop\ilimits@e^{\varphi}\,d\pi, |  |

with equality iff d​μd​π∝eφ\frac{d\mu}{d\pi}\propto e^{\varphi}. Applying this with φ=−θ​ρ\varphi=-\theta\rho gives, for all θ∈ℝ\theta\in\mathbb{R} and μ≪π\mu\ll\pi,

|  |  |  |  |
| --- | --- | --- | --- |
|  | KL​(μ​\|​π)≥−θ​b​(μ)−log⁡Z​(θ),\mathrm{KL}(\mu\|\pi)\ \geq\ -\theta\,b(\mu)-\log Z(\theta), |  | (4.20) |

with equality iff μ=μθ∗\mu=\mu\_{\theta}^{\ast} as in ([4.17](https://arxiv.org/html/2511.01486v2#S4.E17 "Equation 4.17 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Hence

|  |  |  |
| --- | --- | --- |
|  | F(μ)≥α(−θb(μ)−logZ(θ))+γ2(b(μ)−a)2=:(b(μ))θ.F(\mu)\ \geq\ \alpha\big(-\theta\,b(\mu)-\log Z(\theta)\big)+\frac{\gamma}{2}\big(b(\mu)-a\big)^{2}=:{}\_{\theta}\big(b(\mu)\big). |  |

For fixed θ\theta, (x)θ{}\_{\theta}(x) is a strictly convex quadratic in xx with unique minimizer

|  |  |  |
| --- | --- | --- |
|  | x∗​(θ)=a+αγ​θ,x^{\ast}(\theta)=a+\frac{\alpha}{\gamma}\,\theta, |  |

and minimal value

|  |  |  |  |
| --- | --- | --- | --- |
|  | infx∈ℝ(x)θ=−α(θa+logZ(θ))−α22​γθ2.\inf\_{x\in\mathbb{R}}{}\_{\theta}(x)=-\alpha\Big(\theta a+\log Z(\theta)\Big)-\frac{\alpha^{2}}{2\gamma}\,\theta^{2}. |  | (4.21) |

Therefore, for all μ≪π\mu\ll\pi and θ∈ℝ\theta\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(μ)≥−α​(θ​a+log⁡Z​(θ))−α22​γ​θ2.F(\mu)\ \geq\ -\alpha\Big(\theta a+\log Z(\theta)\Big)-\frac{\alpha^{2}}{2\gamma}\,\theta^{2}. |  | (4.22) |

Equality in ([4.22](https://arxiv.org/html/2511.01486v2#S4.E22 "Equation 4.22 ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) for some θ\theta occurs iff simultaneously:
(i) equality holds in ([4.20](https://arxiv.org/html/2511.01486v2#S4.E20 "Equation 4.20 ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), i.e. μ=μθ∗\mu=\mu\_{\theta}^{\ast}, and
(ii) b​(μ)=x∗​(θ)b(\mu)=x^{\ast}(\theta), i.e. b​(μθ∗)=a+αγ​θb(\mu\_{\theta}^{\ast})=a+\frac{\alpha}{\gamma}\theta.
Since b​(μθ∗)=ψ​(θ)b(\mu\_{\theta}^{\ast})=\psi(\theta), condition (ii) is equivalent to the fixed–point equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(θ)=a+αγ​θ,\psi(\theta)=a+\frac{\alpha}{\gamma}\,\theta, |  | (4.23) |

which is precisely ([4.19](https://arxiv.org/html/2511.01486v2#S4.E19 "Equation 4.19 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). If θ∗\theta^{\ast} solves ([4.23](https://arxiv.org/html/2511.01486v2#S4.E23 "Equation 4.23 ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), then μθ∗∗\mu\_{\theta^{\ast}}^{\ast} achieves equality in ([4.22](https://arxiv.org/html/2511.01486v2#S4.E22 "Equation 4.22 ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and is therefore optimal for the primal problem, with optimizer of the form ([4.17](https://arxiv.org/html/2511.01486v2#S4.E17 "Equation 4.17 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and tilted mean given by ([4.18](https://arxiv.org/html/2511.01486v2#S4.E18 "Equation 4.18 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).

Because ρ\rho is bounded, ZZ is C2C^{2} and

|  |  |  |
| --- | --- | --- |
|  | ψ′​(θ)=−d2d​θ2​log⁡Z​(θ)=−Varμθ∗​(ρ)≤0.\psi^{\prime}(\theta)=-\frac{d^{2}}{d\theta^{2}}\log Z(\theta)=-\mathrm{Var}\_{\mu\_{\theta}^{\ast}}(\rho)\leq 0. |  |

Hence the function g​(θ):=ψ​(θ)−a−αγ​θg(\theta):=\psi(\theta)-a-\frac{\alpha}{\gamma}\theta is strictly decreasing:

|  |  |  |
| --- | --- | --- |
|  | g′​(θ)=ψ′​(θ)−αγ≤−αγ<0.g^{\prime}(\theta)=\psi^{\prime}(\theta)-\frac{\alpha}{\gamma}\leq-\frac{\alpha}{\gamma}<0. |  |

Moreover, ψ​(θ)\psi(\theta) is bounded while the linear term diverges, so g​(θ)→+∞g(\theta)\to+\infty as θ→−∞\theta\to-\infty and g​(θ)→−∞g(\theta)\to-\infty as θ→+∞\theta\to+\infty. By continuity there exists a unique θ∗\theta^{\ast} solving ([4.23](https://arxiv.org/html/2511.01486v2#S4.E23 "Equation 4.23 ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). For α>0\alpha>0, FF is strictly convex on {μ≪π}\{\mu\ll\pi\} (sum of the strictly convex αKL(⋅\|π)\alpha\,\mathrm{KL}(\cdot\|\pi) and a convex function of the linear statistic b​(μ)b(\mu)), hence the minimizer is unique. Since μθ∗∗\mu\_{\theta^{\ast}}^{\ast} is feasible and optimal, it is the unique minimizer.

This proves that for α>0\alpha>0 the unique optimizer is the Gibbs measure ([4.17](https://arxiv.org/html/2511.01486v2#S4.E17 "Equation 4.17 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")); its mean is ψ​(θ)\psi(\theta) in ([4.18](https://arxiv.org/html/2511.01486v2#S4.E18 "Equation 4.18 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), and the parameter θ\theta is uniquely determined by ([4.19](https://arxiv.org/html/2511.01486v2#S4.E19 "Equation 4.19 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).
∎

###### Lemma 4.11.

Under Assumption [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") (A3), ψ\psi in ([4.18](https://arxiv.org/html/2511.01486v2#S4.E18 "Equation 4.18 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) is continuous and nonincreasing on ℝ\mathbb{R}, with range
ψ​(ℝ)=[infλ​ρ​(λ),supλ​ρ​(λ)]\psi(\mathbb{R})=[\mathrm{inf}\_{\lambda}\rho(\lambda),\ \mathrm{sup}\_{\lambda}\rho(\lambda)].
Hence ([4.19](https://arxiv.org/html/2511.01486v2#S4.E19 "Equation 4.19 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) admits a unique solution θ∈ℝ\theta\in\mathbb{R}.

###### Proof.

Fix (t,ω)(t,\omega) and set ρ:=ρt⋅​(ω)\rho:=\rho\_{t}^{\cdot}(\omega) and π:=πt​(ω)\pi:=\pi\_{t}(\omega), as well as

|  |  |  |
| --- | --- | --- |
|  | Z​(θ):=\ilimits@​e−θ​ρ​(λ)​π​(d​λ),d​μθ​(λ):=e−θ​ρ​(λ)Z​(θ)​π​(d​λ),ψ​(θ):=\ilimits@​ρ​d​μθ.Z(\theta):=\intslop\ilimits@e^{-\theta\,\rho(\lambda)}\,\pi(d\lambda),\qquad d\mu\_{\theta}(\lambda):=\frac{e^{-\theta\,\rho(\lambda)}}{Z(\theta)}\,\pi(d\lambda),\qquad\psi(\theta):=\intslop\ilimits@\rho\,d\mu\_{\theta}. |  |

Write m:=ess​infλ​ρ​(λ)m:=\mathrm{ess\,inf}\_{\lambda}\rho(\lambda) and M:=ess​supλ​ρ​(λ)M:=\mathrm{ess\,sup}\_{\lambda}\rho(\lambda) (finite due to the assumptions).

By Assumption [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") (A3), (η):=log⁡\ilimits@​eη​ρ​d​π\Phi(\eta):=\log\!\intslop\ilimits@e^{\eta\rho}\,d\pi is finite for all η∈ℝ\eta\in\mathbb{R}. Hence Z​(θ)=e(−θ)∈(0,∞)Z(\theta)=e^{\Phi(-\theta)}\in(0,\infty) for every θ∈ℝ\theta\in\mathbb{R}. Moreover, on any compact interval I⊂ℝI\subset\mathbb{R} there exists c=supθ∈I|θ|<∞c=\sup\_{\theta\in I}|\theta|<\infty and, for any δ>0\delta>0,

|  |  |  |
| --- | --- | --- |
|  | |ρ|​e−θ​ρ≤1δ​e(c+δ)​|ρ|≤1δ​(e(c+δ)​ρ+e−(c+δ)​ρ),ρ2​e−θ​ρ≤2δ2​e(c+δ)​|ρ|,|\,\rho\,|e^{-\theta\rho}\ \leq\ \tfrac{1}{\delta}e^{(c+\delta)|\rho|}\ \leq\ \tfrac{1}{\delta}\big(e^{(c+\delta)\rho}+e^{-(c+\delta)\rho}\big),\qquad\rho^{2}e^{-\theta\rho}\ \leq\ \tfrac{2}{\delta^{2}}e^{(c+\delta)|\rho|}, |  |

so Assumption [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") (A3) implies the right-hand sides are π\pi–integrable. Dominated convergence then yields Z∈C2​(ℝ)Z\in C^{2}(\mathbb{R}) with

|  |  |  |
| --- | --- | --- |
|  | Z′​(θ)=−\ilimits@​ρ​e−θ​ρ​d​π,Z′′​(θ)=\ilimits@​ρ2​e−θ​ρ​d​π.Z^{\prime}(\theta)=-\!\intslop\ilimits@\rho\,e^{-\theta\rho}\,d\pi,\qquad Z^{\prime\prime}(\theta)=\!\intslop\ilimits@\rho^{2}e^{-\theta\rho}\,d\pi. |  |

Let A​(θ):=log⁡Z​(θ)A(\theta):=\log Z(\theta). Then A′​(θ)=Z′​(θ)/Z​(θ)=−ψ​(θ)A^{\prime}(\theta)=Z^{\prime}(\theta)/Z(\theta)=-\psi(\theta) and

|  |  |  |
| --- | --- | --- |
|  | A′′​(θ)=Z′′​(θ)Z​(θ)−(Z′​(θ)Z​(θ))2=Varμθ​(ρ)≥ 0,A^{\prime\prime}(\theta)\ =\ \frac{Z^{\prime\prime}(\theta)}{Z(\theta)}-\Big(\frac{Z^{\prime}(\theta)}{Z(\theta)}\Big)^{2}\ =\ \mathrm{Var}\_{\mu\_{\theta}}(\rho)\ \geq\ 0, |  |

so ψ​(θ)=−A′​(θ)\psi(\theta)=-A^{\prime}(\theta) is continuous and nonincreasing on ℝ\mathbb{R}. If ρ\rho is not π\pi–a.s. constant, then μθ\mu\_{\theta} is equivalent to π\pi (its density e−θ​ρ/Z​(θ)e^{-\theta\rho}/Z(\theta) is strictly positive π\pi–a.s.), hence ρ\rho is not μθ\mu\_{\theta}–a.s. constant and Varμθ​(ρ)>0\mathrm{Var}\_{\mu\_{\theta}}(\rho)>0 for all θ\theta, i.e. ψ\psi is strictly decreasing.

For every θ\theta, since μθ\mu\_{\theta} is a probability measure and ρ∈L1​(μθ)\rho\in L^{1}(\mu\_{\theta}),

|  |  |  |
| --- | --- | --- |
|  | m≤ψ​(θ)≤M.m\ \leq\ \psi(\theta)\ \leq\ M. |  |

We show limθ→+∞ψ​(θ)=m\lim\_{\theta\to+\infty}\psi(\theta)=m; the case θ→−∞\theta\to-\infty is analogous (with limit MM). Fix ε>0\varepsilon>0 and set

|  |  |  |
| --- | --- | --- |
|  | Aε:={λ:ρ​(λ)≤m+ε},Bε:=∖Aε={λ:ρ​(λ)>m+ε}.A\_{\varepsilon}:=\{\lambda:\rho(\lambda)\leq m+\varepsilon\},\qquad B\_{\varepsilon}:=\Lambda\setminus A\_{\varepsilon}=\{\lambda:\rho(\lambda)>m+\varepsilon\}. |  |

By definition of m=infλ​ρ​(λ)m=\mathrm{inf}\_{\lambda}\rho(\lambda), π​(Aε)>0\pi(A\_{\varepsilon})>0 due to (A4). Decompose, for θ>0\theta>0,

|  |  |  |
| --- | --- | --- |
|  | Z​(θ)=\ilimits@​e−θ​ρ​d​π=e−θ​(m+ε)​(\ilimits@Aε​e−θ​(ρ−m−ε)​d​π⏟=⁣:Cε​(θ)+\ilimits@Bε​e−θ​(ρ−m−ε)​d​π⏟=⁣:Lε​(θ)),Z(\theta)=\!\intslop\ilimits@e^{-\theta\rho}\,d\pi=e^{-\theta(m+\varepsilon)}\!\left(\underbrace{\intslop\ilimits@\_{A\_{\varepsilon}}e^{-\theta(\rho-m-\varepsilon)}\,d\pi}\_{=:C\_{\varepsilon}(\theta)}+\underbrace{\intslop\ilimits@\_{B\_{\varepsilon}}e^{-\theta(\rho-m-\varepsilon)}\,d\pi}\_{=:L\_{\varepsilon}(\theta)}\right), |  |

and

|  |  |  |
| --- | --- | --- |
|  | \ilimits@​ρ​e−θ​ρ​d​π=e−θ​(m+ε)​(\ilimits@Aε​ρ​e−θ​(ρ−m−ε)​d​π+\ilimits@Bε​ρ​e−θ​(ρ−m−ε)​d​π).\intslop\ilimits@\rho\,e^{-\theta\rho}\,d\pi=e^{-\theta(m+\varepsilon)}\!\left(\intslop\ilimits@\_{A\_{\varepsilon}}\rho\,e^{-\theta(\rho-m-\varepsilon)}\,d\pi+\intslop\ilimits@\_{B\_{\varepsilon}}\rho\,e^{-\theta(\rho-m-\varepsilon)}\,d\pi\right). |  |

Since ρ≤m+ε\rho\leq m+\varepsilon on AεA\_{\varepsilon}, we have

|  |  |  |
| --- | --- | --- |
|  | \ilimits@Aε​ρ​e−θ​(ρ−m−ε)​d​π≤(m+ε)​Cε​(θ).\intslop\ilimits@\_{A\_{\varepsilon}}\rho\,e^{-\theta(\rho-m-\varepsilon)}\,d\pi\ \leq\ (m+\varepsilon)\,C\_{\varepsilon}(\theta). |  |

On BεB\_{\varepsilon} we have ρ−m−ε>0\rho-m-\varepsilon>0, hence e−θ​(ρ−m−ε)↓0e^{-\theta(\rho-m-\varepsilon)}\downarrow 0 pointwise as θ→∞\theta\to\infty and is dominated by 11. Because ρ∈L1​(π)\rho\in L^{1}(\pi) (by Assumption [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")  using |x|≤δ−1​eδ​|x||x|\leq\delta^{-1}e^{\delta|x|} and two-sided exponential integrability), dominated convergence gives

|  |  |  |
| --- | --- | --- |
|  | Lε​(θ)⟶ 0andRε​(θ):=\ilimits@Bε​ρ​e−θ​(ρ−m−ε)​d​π⟶ 0as ​θ→∞.L\_{\varepsilon}(\theta)\ \longrightarrow\ 0\quad\text{and}\quad R\_{\varepsilon}(\theta):=\intslop\ilimits@\_{B\_{\varepsilon}}\rho\,e^{-\theta(\rho-m-\varepsilon)}\,d\pi\ \longrightarrow\ 0\qquad\text{as }\theta\to\infty. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | ψ​(θ)=\ilimits@​ρ​e−θ​ρ​d​πZ​(θ)≤(m+ε)​Cε​(θ)+Rε​(θ)Cε​(θ)+Lε​(θ)→θ→∞m+ε.\psi(\theta)=\frac{\intslop\ilimits@\rho\,e^{-\theta\rho}\,d\pi}{Z(\theta)}\ \leq\ \frac{(m+\varepsilon)\,C\_{\varepsilon}(\theta)+R\_{\varepsilon}(\theta)}{C\_{\varepsilon}(\theta)+L\_{\varepsilon}(\theta)}\ \xrightarrow[\theta\to\infty]{}\ m+\varepsilon. |  |

Since ε>0\varepsilon>0 is arbitrary and ψ​(θ)≥m\psi(\theta)\geq m, it follows that limθ→∞ψ​(θ)=m\lim\_{\theta\to\infty}\psi(\theta)=m. The limit limθ→−∞ψ​(θ)=M\lim\_{\theta\to-\infty}\psi(\theta)=M is proved symmetrically by applying the same argument to the sets Aε+:={ρ≥M−ε}A\_{\varepsilon}^{+}:=\{\rho\geq M-\varepsilon\} and Bε+:={ρ<M−ε}B\_{\varepsilon}^{+}:=\{\rho<M-\varepsilon\}. Consequently,

|  |  |  |
| --- | --- | --- |
|  | ψ​(ℝ)=[m,M]=[infλ​ρ​(λ),supλ​ρ​(λ)].\psi(\mathbb{R})=[m,M]=\big[\mathrm{inf}\_{\lambda}\rho(\lambda),\ \mathrm{sup}\_{\lambda}\rho(\lambda)\big]. |  |

The map θ↦ψ​(θ)\theta\mapsto\psi(\theta) is continuous and bounded, with ψ​(θ)→M\psi(\theta)\to M as θ→−∞\theta\to-\infty and ψ​(θ)→m\psi(\theta)\to m as θ→+∞\theta\to+\infty. If α>0\alpha>0, then

|  |  |  |
| --- | --- | --- |
|  | g​(θ):=ψ​(θ)−a−αγ​θg(\theta):=\psi(\theta)-a-\frac{\alpha}{\gamma}\theta |  |

is strictly decreasing, with limθ→−∞g​(θ)=+∞\lim\_{\theta\to-\infty}g(\theta)=+\infty and limθ→+∞g​(θ)=−∞\lim\_{\theta\to+\infty}g(\theta)=-\infty, hence there exists a unique θ∈ℝ\theta\in\mathbb{R} solving ([4.19](https://arxiv.org/html/2511.01486v2#S4.E19 "Equation 4.19 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). If α=0\alpha=0, then ([4.19](https://arxiv.org/html/2511.01486v2#S4.E19 "Equation 4.19 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) reduces to ψ​(θ)=a\psi(\theta)=a, which has a solution iff a∈[m,M]a\in[m,M]; it is unique when ρ\rho is not π\pi–a.s. constant (since ψ\psi is strictly decreasing), and either has no solution or infinitely many solutions when ρ\rho is π\pi–a.s. constant (according as a​m=Ma\neq m=M or a=m=Ma=m=M).

∎

###### Lemma 4.12.

For α2>α1>0\alpha\_{2}>\alpha\_{1}>0, the corresponding optimizers μαi∗\mu^{\ast}\_{\alpha\_{i}} satisfy

|  |  |  |
| --- | --- | --- |
|  | KL​(μα2∗​\|​π)≤KL​(μα1∗​\|​π).\mathrm{KL}(\mu^{\ast}\_{\alpha\_{2}}\|\pi)\ \leq\ \mathrm{KL}(\mu^{\ast}\_{\alpha\_{1}}\|\pi). |  |

###### Proof.

Let Fα​(μ):=γ2​(b​(μ)−a)2+α​KL​(μ​\|​π)F\_{\alpha}(\mu):=\frac{\gamma}{2}\big(b(\mu)-a\big)^{2}+\alpha\,\mathrm{KL}(\mu\|\pi) and let μαi∗\mu^{\*}\_{\alpha\_{i}} be any minimizer of FαiF\_{\alpha\_{i}} for i=1,2i=1,2. By boundedness of ρ\rho we have Fαi​(π)<∞F\_{\alpha\_{i}}(\pi)<\infty, hence Fαi​(μαi∗)≤Fαi​(π)<∞F\_{\alpha\_{i}}(\mu^{\*}\_{\alpha\_{i}})\leq F\_{\alpha\_{i}}(\pi)<\infty, which in particular implies KL​(μαi∗​\|​π)<∞\mathrm{KL}(\mu^{\*}\_{\alpha\_{i}}\|\pi)<\infty.

By optimality,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Fα2​(μα2∗)\displaystyle F\_{\alpha\_{2}}(\mu^{\*}\_{\alpha\_{2}}) | ≤Fα2​(μα1∗),\displaystyle\leq F\_{\alpha\_{2}}(\mu^{\*}\_{\alpha\_{1}}), |  | (4.24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Fα1​(μα1∗)\displaystyle F\_{\alpha\_{1}}(\mu^{\*}\_{\alpha\_{1}}) | ≤Fα1​(μα2∗).\displaystyle\leq F\_{\alpha\_{1}}(\mu^{\*}\_{\alpha\_{2}}). |  | (4.25) |

Expanding ([4.24](https://arxiv.org/html/2511.01486v2#S4.E24 "Equation 4.24 ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"))–([4.25](https://arxiv.org/html/2511.01486v2#S4.E25 "Equation 4.25 ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ2​(b​(μα2∗)−a)2+α2​KL​(μα2∗​\|​π)\displaystyle\frac{\gamma}{2}\big(b(\mu^{\*}\_{\alpha\_{2}})-a\big)^{2}+\alpha\_{2}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{2}}\|\pi) | ≤γ2​(b​(μα1∗)−a)2+α2​KL​(μα1∗​\|​π),\displaystyle\leq\frac{\gamma}{2}\big(b(\mu^{\*}\_{\alpha\_{1}})-a\big)^{2}+\alpha\_{2}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{1}}\|\pi), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | γ2​(b​(μα1∗)−a)2+α1​KL​(μα1∗​\|​π)\displaystyle\frac{\gamma}{2}\big(b(\mu^{\*}\_{\alpha\_{1}})-a\big)^{2}+\alpha\_{1}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{1}}\|\pi) | ≤γ2​(b​(μα2∗)−a)2+α1​KL​(μα2∗​\|​π).\displaystyle\leq\frac{\gamma}{2}\big(b(\mu^{\*}\_{\alpha\_{2}})-a\big)^{2}+\alpha\_{1}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{2}}\|\pi). |  |

Adding the two inequalities and cancelling the matching quadratic terms gives

|  |  |  |
| --- | --- | --- |
|  | α2​KL​(μα2∗​\|​π)+α1​KL​(μα1∗​\|​π)≤α2​KL​(μα1∗​\|​π)+α1​KL​(μα2∗​\|​π),\alpha\_{2}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{2}}\|\pi)+\alpha\_{1}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{1}}\|\pi)\ \leq\ \alpha\_{2}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{1}}\|\pi)+\alpha\_{1}\,\mathrm{KL}(\mu^{\*}\_{\alpha\_{2}}\|\pi), |  |

i.e.

|  |  |  |
| --- | --- | --- |
|  | (α2−α1)​(KL​(μα2∗​\|​π)−KL​(μα1∗​\|​π))≤ 0.(\alpha\_{2}-\alpha\_{1})\Big(\mathrm{KL}(\mu^{\*}\_{\alpha\_{2}}\|\pi)-\mathrm{KL}(\mu^{\*}\_{\alpha\_{1}}\|\pi)\Big)\ \leq\ 0. |  |

Since α2>α1>0\alpha\_{2}>\alpha\_{1}>0, it follows that KL​(μα2∗​\|​π)≤KL​(μα1∗​\|​π)\mathrm{KL}(\mu^{\*}\_{\alpha\_{2}}\|\pi)\leq\mathrm{KL}(\mu^{\*}\_{\alpha\_{1}}\|\pi), as claimed.
∎

### 4.4 Optimal Adapted Measure-Valued Control

Define θt∗​(ω)\theta\_{t}^{\ast}(\omega) to be the unique solution of ([4.19](https://arxiv.org/html/2511.01486v2#S4.E19 "Equation 4.19 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) with a=a^t​(ω)a=\mathaccent 866{a}\_{t}(\omega), ρ=ρt⋅​(ω)\rho=\rho\_{t}^{\cdot}(\omega), and π=πt​(ω)\pi=\pi\_{t}(\omega).
Set

|  |  |  |  |
| --- | --- | --- | --- |
|  | mt∗​(d​λ):=exp⁡(−θt∗​(ω)​ρtλ​(ω))\ilimits@​exp⁡(−θt∗​(ω)​ρtλ′​(ω))​πt​(ω,d​λ′)​πt​(ω,d​λ).m\_{t}^{\ast}(d\lambda)\ :=\ \frac{\exp\!\big(-\theta\_{t}^{\ast}(\omega)\,\rho\_{t}^{\lambda}(\omega)\big)}{\displaystyle\intslop\ilimits@\exp\!\big(-\theta\_{t}^{\ast}(\omega)\,\rho\_{t}^{\lambda^{\prime}}(\omega)\big)\,\pi\_{t}(\omega,d\lambda^{\prime})}\ \pi\_{t}(\omega,d\lambda). |  | (4.26) |

###### Proposition 4.13.

(θt∗)t∈[0,T](\theta\_{t}^{\ast})\_{t\in[0,T]} is a 𝔾\mathbb{G}–adapted real–valued process. Consequently, for every t∈[0,T],B∈ℬ​()t\in[0,T],B\in\mathcal{B}(\Lambda), the map ω↦mt∗​(ω,B)\omega\mapsto m\_{t}^{\ast}(\omega,B) is 𝒢t\mathcal{G}\_{t}–measurable, so (mt∗)t∈[0,T](m\_{t}^{\ast})\_{t\in[0,T]} is an 𝔾\mathbb{G}–adapted flow of probability kernels. Moreover, m∗m^{\ast} is optimal for Problem [4.1](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem1 "Problem 4.1. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective").

If, in addition, the maps (t,ω)↦ρtλ​(ω)(t,\omega)\mapsto\rho\_{t}^{\lambda}(\omega), (t,ω)↦a^t​(ω)(t,\omega)\mapsto\mathaccent 866{a}\_{t}(\omega), and (t,ω)↦πt​(ω,B)(t,\omega)\mapsto\pi\_{t}(\omega,B) are progressively measurable for each fixed λ∈\lambda\in\Lambda and B∈ℬ​()B\in\mathcal{B}(\Lambda), then the maps (t,ω)↦θt∗​(ω)(t,\omega)\mapsto\theta\_{t}^{\ast}(\omega) and (t,ω)↦mt∗​(ω,B)(t,\omega)\mapsto m\_{t}^{\ast}(\omega,B) are 𝒫​(𝔾)\mathcal{P}(\mathbb{G})–measurable (i.e. progressively measurable).

###### Proof.

Fix t∈[0,T]t\in[0,T] and set ρ​(ω,λ):=ρtλ​(ω)\rho(\omega,\lambda):=\rho\_{t}^{\lambda}(\omega), π​(ω,⋅):=πt​(ω,⋅)\pi(\omega,\cdot):=\pi\_{t}(\omega,\cdot) and a​(ω):=a^t​(ω)a(\omega):=\mathaccent 866{a}\_{t}(\omega). For each θ∈ℝ\theta\in\mathbb{R} set

|  |  |  |
| --- | --- | --- |
|  | Z​(ω,θ):=\ilimits@​e−θ​ρ​(ω,λ)​π​(ω,d​λ),ψ​(ω,θ):=\ilimits@​ρ​(ω,λ)​e−θ​ρ​(ω,λ)​π​(ω,d​λ)Z​(ω,θ).Z(\omega,\theta):=\intslop\ilimits@e^{-\theta\,\rho(\omega,\lambda)}\,\pi(\omega,d\lambda),\qquad\psi(\omega,\theta):=\frac{\displaystyle\intslop\ilimits@\rho(\omega,\lambda)\,e^{-\theta\,\rho(\omega,\lambda)}\,\pi(\omega,d\lambda)}{Z(\omega,\theta)}. |  |

We begin by showing the measurability of (ω,θ)↦ψ​(ω,θ)(\omega,\theta)\mapsto\psi(\omega,\theta) at fixed tt.
From assumptions it follows that (ω,λ)↦ρ​(ω,λ)(\omega,\lambda)\mapsto\rho(\omega,\lambda) is 𝒢t⊗ℬ​()\mathcal{G}\_{t}\otimes\mathcal{B}(\Lambda)–measurable. Consequently, for each fixed θ\theta, the functions

|  |  |  |
| --- | --- | --- |
|  | (ω,λ)↦e−θ​ρ​(ω,λ)and(ω,λ)↦ρ​(ω,λ)​e−θ​ρ​(ω,λ)(\omega,\lambda)\mapsto e^{-\theta\,\rho(\omega,\lambda)}\quad\text{and}\quad(\omega,\lambda)\mapsto\rho(\omega,\lambda)\,e^{-\theta\,\rho(\omega,\lambda)} |  |

are 𝒢t⊗ℬ​()\mathcal{G}\_{t}\otimes\mathcal{B}(\Lambda)–measurable and bounded. Since ω↦π​(ω,⋅)\omega\mapsto\pi(\omega,\cdot) is an 𝒢t\mathcal{G}\_{t}–measurable kernel on , the map ω↦\ilimits@​g​(ω,λ)​π​(ω,d​λ)\omega\mapsto\intslop\ilimits@g(\omega,\lambda)\,\pi(\omega,d\lambda) is 𝒢t\mathcal{G}\_{t}–measurable for any 𝒢t\mathcal{G}\_{t}–measurable ω↦g​(ω,λ)\omega\mapsto g(\omega,\lambda), see [[30](https://arxiv.org/html/2511.01486v2#bib.bib30)], Lemma 1.41. Therefore, for each θ\theta, both ω↦Z​(ω,θ)\omega\mapsto Z(\omega,\theta) and ω↦\ilimits@​ρ​(ω,λ)​e−θ​ρ​(ω,λ)​d​π​(ω,d​λ)\omega\mapsto\intslop\ilimits@\rho(\omega,\lambda)e^{-\theta\rho(\omega,\lambda)}\,d\pi(\omega,d\lambda) are 𝒢t\mathcal{G}\_{t}–measurable; as Z​(ω,θ)>0Z(\omega,\theta)>0, the ratio ψ​(ω,θ)\psi(\omega,\theta) is 𝒢t\mathcal{G}\_{t}–measurable. Moreover, by boundedness of ρ\rho and dominated convergence, θ↦ψ​(ω,θ)\theta\mapsto\psi(\omega,\theta) is continuous for each ω\omega, hence a Caratheodory function, hence by Lemma 4.51, [[3](https://arxiv.org/html/2511.01486v2#bib.bib3)], p.153, it is 𝒢t⊗ℬ​(ℝ)\mathcal{G}\_{t}\otimes\mathcal{B}(\mathbb{R})–measurable.

Then, we show 𝒢t\mathcal{G}\_{t}–measurability of the fixed point θt∗\theta\_{t}^{\ast}.
Assume α>0\alpha>0. Define

|  |  |  |
| --- | --- | --- |
|  | f​(ω,θ):=ψ​(ω,θ)−a​(ω)−αγ​θ.f(\omega,\theta):=\psi(\omega,\theta)-a(\omega)-\frac{\alpha}{\gamma}\,\theta. |  |

By the previous step and measurability of a​(⋅)a(\cdot), for each fixed θ\theta the map ω↦f​(ω,θ)\omega\mapsto f(\omega,\theta) is 𝒢t\mathcal{G}\_{t}–measurable, and for each ω\omega, θ↦f​(ω,θ)\theta\mapsto f(\omega,\theta) is continuous and strictly decreasing (Lemma [4.11](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem11 "Lemma 4.11. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). For each ω\omega there is a unique root θt∗​(ω)\theta\_{t}^{\ast}(\omega) of f​(ω,θ)=0f(\omega,\theta)=0. Using monotonicity,

|  |  |  |
| --- | --- | --- |
|  | θt∗​(ω)=inf{q∈ℚ:f​(ω,q)≤0}.\theta\_{t}^{\ast}(\omega)\ =\ \inf\big\{q\in\mathbb{Q}:\ f(\omega,q)\leq 0\big\}. |  |

Hence, for any r∈ℝr\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | {ω:θt∗​(ω)<r}=\slimits@q∈ℚ,q<r​{ω:f​(ω,q)≤0}∈𝒢t,\{\omega:\ \theta\_{t}^{\ast}(\omega)<r\}=\bigcupop\slimits@\_{q\in\mathbb{Q},\ q<r}\{\omega:\ f(\omega,q)\leq 0\}\in\mathcal{G}\_{t}, |  |

since each ω↦f​(ω,q)\omega\mapsto f(\omega,q) is 𝒢t\mathcal{G}\_{t}–measurable. Thus ω↦θt∗​(ω)\omega\mapsto\theta\_{t}^{\ast}(\omega) is 𝒢t\mathcal{G}\_{t}–measurable.

If α∗=0\alpha^{\*}=0 and, in addition,
a^t​(ω)∈[infλ​ρ​(λ),supλ​ρ​(λ)]for a.e. (t,ω),\mathaccent 866{a}\_{t}(\omega)\in\big[\mathrm{inf}\_{\lambda}\rho(\lambda),\ \mathrm{sup}\_{\lambda}\rho(\lambda)\big]\quad\text{for a.e.\ $(t,\omega)$}, then one can define θt∗​(ω)\theta\_{t}^{\*}(\omega) as any (measurable) solution of ψt​(ω,θ)=a^t​(ω)\psi\_{t}(\omega,\theta)=\mathaccent 866{a}\_{t}(\omega) (e.g., the minimal root), and the conclusions above still hold.

To show the adaptedness of mt∗m\_{t}^{\ast}, define

|  |  |  |
| --- | --- | --- |
|  | ht​(ω,λ):=exp⁡(−θt∗​(ω)​ρ​(ω,λ)).h\_{t}(\omega,\lambda):=\exp\!\big(-\theta\_{t}^{\ast}(\omega)\,\rho(\omega,\lambda)\big). |  |

Note ht​(ω,λ)h\_{t}(\omega,\lambda) is 𝒢t\mathcal{G}\_{t}-measurable in ω\omega and continuous in λ\lambda, hence a Caratheodory function, hence the map (ω,λ)↦ht​(ω,λ)(\omega,\lambda)\mapsto h\_{t}(\omega,\lambda) is 𝒢t⊗ℬ​()\mathcal{G}\_{t}\otimes\mathcal{B}(\Lambda)–measurable, and strictly positive. Therefore, for each B∈ℬ​()B\in\mathcal{B}(\Lambda) the numerator

|  |  |  |
| --- | --- | --- |
|  | ω⟼\ilimits@B​ht​(ω,λ)​π​(ω,d​λ)\omega\ \longmapsto\ \intslop\ilimits@\_{B}h\_{t}(\omega,\lambda)\,\pi(\omega,d\lambda) |  |

and the (strictly positive) denominator

|  |  |  |
| --- | --- | --- |
|  | ω⟼\ilimits@​ht​(ω,λ)​π​(ω,d​λ)\omega\ \longmapsto\ \intslop\ilimits@h\_{t}(\omega,\lambda)\,\pi(\omega,d\lambda) |  |

are 𝒢t\mathcal{G}\_{t}–measurable. Their ratio equals ω↦mt∗​(ω,B)\omega\mapsto m\_{t}^{\ast}(\omega,B) by ([4.26](https://arxiv.org/html/2511.01486v2#S4.E26 "Equation 4.26 ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), hence mt∗m\_{t}^{\ast} is 𝒢t\mathcal{G}\_{t}–measurable for each tt, i.e., (mt∗)t∈[0,T](m\_{t}^{\ast})\_{t\in[0,T]} is an 𝔾\mathbb{G}–adapted flow of kernels.

Finally, we must show that the obtained controls are optimal. Let α∗\alpha^{\ast} be the scalar from Theorem [4.9](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem9 "Theorem 4.9. ‣ 4.2 Existence of the Minimizing Flow ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"). For this choice, the above gives θt∗\theta\_{t}^{\ast} and that m∗m^{\ast} is adapted. By Proposition [4.10](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem10 "Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), for each (t,ω)(t,\omega) the measure mt∗​(ω,⋅)m\_{t}^{\ast}(\omega,\cdot) solves the corresponding pointwise minimization of the Lagrangian integrand, hence m∗m^{\ast} minimizes ([4.12](https://arxiv.org/html/2511.01486v2#S4.E12 "Equation 4.12 ‣ Theorem 4.9. ‣ 4.2 Existence of the Minimizing Flow ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). Theorem [4.9](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem9 "Theorem 4.9. ‣ 4.2 Existence of the Minimizing Flow ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") then implies m∗m^{\ast} is optimal for Problem [4.1](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem1 "Problem 4.1. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective").
∎

###### Lemma 4.14.

At (t,ω)(t,\omega) and θ=θt∗​(ω)\theta=\theta\_{t}^{\ast}(\omega),

|  |  |  |  |
| --- | --- | --- | --- |
|  | KL​(mt∗​\|​πt)=−θ​ψt​(θ)−log⁡Zt​(θ),Zt​(θ):=\ilimits@​e−θ​ρtλ​πt​(d​λ).\mathrm{KL}\big(m\_{t}^{\ast}\|\pi\_{t}\big)=-\theta\,\psi\_{t}(\theta)-\log Z\_{t}(\theta),\qquad Z\_{t}(\theta):=\intslop\ilimits@e^{-\theta\rho\_{t}^{\lambda}}\,\pi\_{t}(d\lambda). |  | (4.27) |

The map α↦𝔼​\ilimits@0T​KL​(mt∗​(α)​\|​πt)​d​t\alpha\mapsto\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}(\alpha)\|\pi\_{t})\,dt is continuous and nonincreasing on (0,∞)(0,\infty). It is strictly decreasing provided

|  |  |  |
| --- | --- | --- |
|  | ℚ​{(t,ω):at​(ω)​ψt​(0,ω)}>0andρt⋅​(ω)​is not ​πt​(ω)​-a.s. constant a.e.\mathbb{Q}\big\{(t,\omega):a\_{t}(\omega)\neq\psi\_{t}(0,\omega)\big\}>0\quad\text{and}\quad\rho\_{t}^{\cdot}(\omega)\ \text{is not }\pi\_{t}(\omega)\text{-a.s.\ constant a.e.} |  |

Hence there exists at least one α∗≥0\alpha^{\ast}\geq 0 enforcing the global constraint:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​\ilimits@0T​KL​(mt∗​\|​πt)​d​t=K,\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}\|\pi\_{t})\,dt\ =\ K, |  |

with α∗>0\alpha^{\ast}>0 when 0<K<G​(0+):=limα↓0𝔼​\ilimits@0T​KL​(mt∗​(α)​\|​πt)​d​t0<K<G(0+):=\lim\_{\alpha\downarrow 0}\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}(\alpha)\|\pi\_{t})\,dt, and α∗=0\alpha^{\ast}=0 when K≥G​(0+)K\geq G(0+). If, in addition, the strictness condition holds, then this α∗\alpha^{\*} is unique.

###### Proof.

We omit the dependence on tt for simplicity. Since d​mθ∗d​π​(λ)=e−θ​ρ​(λ)/Z​(θ)\frac{dm^{\ast}\_{\theta}}{d\pi}(\lambda)=e^{-\theta\,\rho(\lambda)}/Z(\theta), we have

|  |  |  |
| --- | --- | --- |
|  | log⁡(d​mθ∗d​π)=−θ​ρ−log⁡Z​(θ),\log\!\Big(\frac{dm^{\ast}\_{\theta}}{d\pi}\Big)=-\theta\,\rho-\log Z(\theta), |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | KL​(mθ∗​\|​π)=\ilimits@​log⁡(d​mθ∗d​π)​d​mθ∗=−θ​\ilimits@​ρ​d​mθ∗−log⁡Z​(θ)=−θ​ψ​(θ)−log⁡Z​(θ).\mathrm{KL}(m^{\ast}\_{\theta}\|\pi)=\intslop\ilimits@\log\!\Big(\frac{dm^{\ast}\_{\theta}}{d\pi}\Big)\,dm^{\ast}\_{\theta}=-\theta\!\intslop\ilimits@\rho\,dm^{\ast}\_{\theta}-\log Z(\theta)=-\theta\,\psi(\theta)-\log Z(\theta). |  |

This yields ([4.27](https://arxiv.org/html/2511.01486v2#S4.E27 "Equation 4.27 ‣ Lemma 4.14. ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")).

Recall that by Lemma [4.12](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem12 "Lemma 4.12. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") α↦KL​(μα∗​\|​π)\alpha\mapsto\mathrm{KL}(\mu^{\ast}\_{\alpha}\|\pi) is nonincreasing pointwise in (t,ω)(t,\omega). Consequently, α↦𝔼​\ilimits@0T​KL​(mt∗​(α)​\|​πt)​d​t\alpha\mapsto\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}(\alpha)\|\pi\_{t})\,dt is nonincreasing. It is strictly decreasing if

|  |  |  |
| --- | --- | --- |
|  | ℚ​{(t,ω):at​(ω)​ψt​(0,ω)}>0​and​ρt⋅​(ω)​is not ​πt​(ω)​-a.s. constant a.e.\mathbb{Q}\big\{(t,\omega):a\_{t}(\omega)\neq\psi\_{t}(0,\omega)\big\}>0\ \text{and}\ \rho\_{t}^{\cdot}(\omega)\ \text{is not }\pi\_{t}(\omega)\text{-a.s.\ constant a.e.} |  |

To show continuity of α↦𝔼​\ilimits@0T​KL​(mt∗​(α)​\|​πt)​d​t\alpha\mapsto\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}(\alpha)\|\pi\_{t})\,dt on (0,∞)(0,\infty), fix α0>0\alpha\_{0}>0 and work pointwise in (t,ω)(t,\omega).
Let θ​(α)\theta(\alpha) denote the unique solution of the fixed–point equation

|  |  |  |
| --- | --- | --- |
|  | ψ​(θ)=a+αγ​θ.\psi(\theta)=a+\frac{\alpha}{\gamma}\,\theta. |  |

Set f​(θ,α):=ψ​(θ)−a−(α/γ)​θf(\theta,\alpha):=\psi(\theta)-a-(\alpha/\gamma)\theta. Then f​(θ​(α),α)=0f(\theta(\alpha),\alpha)=0 and

|  |  |  |
| --- | --- | --- |
|  | ∂θf​(θ,α)=ψ′​(θ)−αγ=−Varmθ∗​(ρ)−αγ< 0.\partial\_{\theta}f(\theta,\alpha)=\psi^{\prime}(\theta)-\frac{\alpha}{\gamma}=-\mathrm{Var}\_{m^{\ast}\_{\theta}}(\rho)-\frac{\alpha}{\gamma}\ <\ 0. |  |

By the (deterministic) implicit function theorem, α↦θ​(α)\alpha\mapsto\theta(\alpha) is C1C^{1} in a neighborhood of α0\alpha\_{0}; hence

|  |  |  |
| --- | --- | --- |
|  | α⟼KL​(mθ​(α)∗​\|​π)=−θ​(α)​ψ​(θ​(α))−log⁡Z​(θ​(α))\alpha\ \longmapsto\ \mathrm{KL}\big(m^{\ast}\_{\theta(\alpha)}\|\pi\big)=-\theta(\alpha)\,\psi(\theta(\alpha))-\log Z(\theta(\alpha)) |  |

is continuous pointwise in (t,ω)(t,\omega).

To pass to expectation and time–integration, observe that for all α\alpha and any competitor μ\mu,

|  |  |  |
| --- | --- | --- |
|  | KL​(μα∗​\|​π)≤1α​Fα​(μ).\mathrm{KL}\big(\mu^{\ast}\_{\alpha}\|\pi\big)\ \leq\ \frac{1}{\alpha}\,F\_{\alpha}(\mu). |  |

Choosing μ=μα0∗\mu=\mu\_{\alpha\_{0}}^{\ast} and restricting α∈[α0/2,2​α0]\alpha\in[\alpha\_{0}/2,2\alpha\_{0}] yields the pointwise bound

|  |  |  |
| --- | --- | --- |
|  | KL​(m∗​(α)​\|​π)≤1α​Fα​(μα0∗)≤γα0​(b​(μα0∗)−a)22+KL​(μα0∗​\|​π).\mathrm{KL}\big(m^{\ast}(\alpha)\|\pi\big)\ \leq\ \frac{1}{\alpha}\,F\_{\alpha}\big(\mu^{\ast}\_{\alpha\_{0}}\big)\ \leq\ \frac{\gamma}{\alpha\_{0}}\,\frac{\big(b(\mu^{\ast}\_{\alpha\_{0}})-a\big)^{2}}{2}\ +\ \mathrm{KL}\big(\mu^{\ast}\_{\alpha\_{0}}\|\pi\big). |  |

Both terms on the right are integrable (they appear in Fα0​(μα0∗)F\_{\alpha\_{0}}(\mu^{\ast}\_{\alpha\_{0}})), so they provide an α\alpha–uniform integrable bound on [α0/2,2​α0][\alpha\_{0}/2,2\alpha\_{0}]. Dominated convergence then gives continuity of

|  |  |  |
| --- | --- | --- |
|  | α⟼𝔼​\ilimits@0T​KL​(mt∗​(α)​\|​πt)​d​t\alpha\ \longmapsto\ \mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}\big(m\_{t}^{\ast}(\alpha)\|\pi\_{t}\big)\,dt |  |

at α0\alpha\_{0}. Since α0>0\alpha\_{0}>0 was arbitrary, continuity holds on (0,∞)(0,\infty).
Write G​(α):=𝔼​\ilimits@0T​KL​(mt∗​(α)​\|​πt)​d​tG(\alpha):=\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}(\alpha)\|\pi\_{t})\,dt. By the above, GG is continuous and nonincreasing on (0,∞)(0,\infty). Moreover, for each (t,ω)(t,\omega), θ​(α)→0\theta(\alpha)\to 0 as α→∞\alpha\to\infty (since α​θ​(α)=γ​(ψ​(θ​(α))−a)\alpha\,\theta(\alpha)=\gamma(\psi(\theta(\alpha))-a) and ψ\psi is bounded), so KL​(mt∗​(α)​\|​πt)↓0\mathrm{KL}(m\_{t}^{\ast}(\alpha)\|\pi\_{t})\downarrow 0. By the monotone convergence theorem, G​(α)↓0G(\alpha)\downarrow 0 as α→∞\alpha\to\infty. Therefore, for any K∈(0,G​(0+))K\in(0,G(0+)) there exists at least one α∗>0\alpha^{\ast}>0 with G​(α∗)=KG(\alpha^{\ast})=K; if K≥G​(0+)K\geq G(0+), the budget is slack and we set α∗=0\alpha^{\ast}=0. If, in addition, GG is strictly decreasing (e.g. under the strictness condition stated above), then α∗\alpha^{\*} is unique.
∎

###### Remark 4.15.

In information geometry, the *II-projection of π∈𝒫​()\pi\in\mathcal{P}(\Lambda) onto ℰ⊂𝒫​()\mathcal{E}\subset\mathcal{P}(\Lambda)* is any

|  |  |  |
| --- | --- | --- |
|  | μ⋆∈arg⁡minμ∈ℰ⁡KL​(μ​\|​π),\mu^{\star}\ \in\ \arg\min\_{\mu\in\mathcal{E}}\ \mathrm{KL}(\mu\|\pi), |  |

whenever the minimum exists, where (,ℬ())(\Lambda,\mathcal{B}(\Lambda)) is a measurable space and 𝒫​()\mathcal{P}(\Lambda) is the set of probability measures on it. When ℰ\mathcal{E} is convex and suitably closed and DKL(⋅\|π)D\_{\mathrm{KL}}(\cdot\|\pi) is finite on ℰ\mathcal{E}, the II-projection exists and is unique. In particular, if ℰ\mathcal{E} is defined by linear moment constraints (e.g., \ilimits@​fi​d​μ=ci\intslop\ilimits@f\_{i}\,d\mu=c\_{i}), then the II-projection μ⋆\mu^{\star} has an exponential-tilt density with respect to π\pi.

We collect the previous results into a single main theorem.

###### Theorem 4.16.

Under Assumption [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), there exists α∗≥0\alpha^{\ast}\geq 0 and a 𝔾\mathbb{G}–progressively measurable optimal control m∗m^{\ast} given by ([4.26](https://arxiv.org/html/2511.01486v2#S4.E26 "Equation 4.26 ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), where θt∗\theta\_{t}^{\ast} solves

|  |  |  |
| --- | --- | --- |
|  | ψt​(θ)=a^t+α∗γ​θ,ψt​(θ)=\ilimits@​ρtλ​e−θ​ρtλ​πt​(d​λ)\ilimits@​e−θ​ρtλ​πt​(d​λ).\psi\_{t}(\theta)\ =\ \mathaccent 866{a}\_{t}+\frac{\alpha^{\ast}}{\gamma}\,\theta,\qquad\psi\_{t}(\theta)=\frac{\displaystyle\intslop\ilimits@\rho\_{t}^{\lambda}e^{-\theta\rho\_{t}^{\lambda}}\,\pi\_{t}(d\lambda)}{\displaystyle\intslop\ilimits@e^{-\theta\rho\_{t}^{\lambda}}\,\pi\_{t}(d\lambda)}. |  |

If α∗>0\alpha^{\ast}>0, then for a.e. (t,ω)(t,\omega) the equation has a *unique* solution θt∗​(ω)\theta\_{t}^{\ast}(\omega), and the constraint is binding:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​\ilimits@0T​KL​(mt∗​\|​πt)​d​t=K.\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}\|\pi\_{t})\,dt=K. |  |

If α∗=0\alpha^{\ast}=0, then any adapted mm with ρ𝑏𝑎𝑟t​(mt)=a^t\bar{\rho}\_{t}(m\_{t})=\mathaccent 866{a}\_{t} a.e. and 𝒟KL​(m​\|​π)≤K\mathcal{D}\_{\mathrm{KL}}(m\|\pi)\leq K is optimal. In particular, whenever a^t∈[ess​infλ​ρtλ,ess​supλ​ρtλ]\mathaccent 866{a}\_{t}\in\big[\mathrm{ess\,inf}\_{\lambda}\rho\_{t}^{\lambda},\ \mathrm{ess\,sup}\_{\lambda}\rho\_{t}^{\lambda}\big] a.s., one may select the (possibly nonunique) KL II–projection given by any solution θt\theta\_{t} of ψt​(θt)=a^t\psi\_{t}(\theta\_{t})=\mathaccent 866{a}\_{t} as a canonical adapted minimizer.

###### Proof.

Combine Theorem [4.9](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem9 "Theorem 4.9. ‣ 4.2 Existence of the Minimizing Flow ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), Propositions [4.10](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem10 "Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") and [4.13](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem13 "Proposition 4.13. ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"), Lemmas [4.11](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem11 "Lemma 4.11. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") and [4.14](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem14 "Lemma 4.14. ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective").
∎

Finally, we check that relaxing the constraints produces the filtered price process.

###### Theorem 4.17.

Assume [4.2](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem2 "Assumption 4.2. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") and [4.3](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem3 "Assumption 4.3. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"). For K>0K>0, let m∗,Km^{\ast,K} denote an optimal solution to Problem [4.1](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem1 "Problem 4.1. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective") and write

|  |  |  |
| --- | --- | --- |
|  | ψt(K):=ρbart​(mt∗,K)=\ilimits@​ρtλ​mt∗,K​(d​λ).\psi\_{t}^{(K)}\ :=\ \bar{\rho}\_{t}\big(m\_{t}^{\ast,K}\big)\ =\ \intslop\ilimits@\rho\_{t}^{\lambda}\,m\_{t}^{\ast,K}(d\lambda). |  |

Let S^\mathaccent 866{S} solve ([4.3](https://arxiv.org/html/2511.01486v2#S4.E3 "Equation 4.3 ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), and for a fixed β∈[0,1]\beta\in[0,1] let S~(K)\mathaccent 869{S}^{(K)} solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S~t(K)=((1−β)​a^t+β​ψt(K))​d​t+σ^t​d​W^t,S~0(K)=S^0.d\mathaccent 869{S}^{(K)}\_{t}\ =\ \Big((1-\beta)\mathaccent 866{a}\_{t}+\beta\,\psi\_{t}^{(K)}\Big)\,dt\ +\ \mathaccent 866{\sigma}\_{t}\,d\mathaccent 866{W}\_{t},\qquad\mathaccent 869{S}^{(K)}\_{0}=\mathaccent 866{S}\_{0}. |  | (4.28) |

Then, as K↑∞K\uparrow\infty,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒ​(m∗,K)=γ2​𝔼​\ilimits@0T​(ψt(K)−a^t)2​d​t\displaystyle\mathcal{L}\big(m^{\ast,K}\big)\ =\ \frac{\gamma}{2}\,\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\!\big(\psi\_{t}^{(K)}-\mathaccent 866{a}\_{t}\big)^{2}\,dt | ⟶ 0,\displaystyle\;\longrightarrow\;0, |  | (4.29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supt∈[0,T]|S~t(K)−S^t|≤β​\ilimits@0T​|ψt(K)−a^t|​d​t\displaystyle\sup\_{t\in[0,T]}\big|\mathaccent 869{S}^{(K)}\_{t}-\mathaccent 866{S}\_{t}\big|\;\leq\;\beta\intslop\ilimits@\_{0}^{T}\big|\psi\_{t}^{(K)}-\mathaccent 866{a}\_{t}\big|\,dt | →K→∞ℙ 0,\displaystyle\;\xrightarrow[\ K\to\infty\ ]{\ \ \mathbb{P}\ \ }\;0, |  | (4.30) |

and, in particular,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T]|S~t(K)−S^t|]≤β​2​Tγ​ℒ​(m∗,K)1/2→K→∞ 0.\mathbb{E}\!\left[\sup\_{t\in[0,T]}\big|\mathaccent 869{S}^{(K)}\_{t}-\mathaccent 866{S}\_{t}\big|\right]\ \leq\ \beta\sqrt{\tfrac{2T}{\gamma}}\;\mathcal{L}\big(m^{\ast,K}\big)^{1/2}\ \xrightarrow[\ K\to\infty\ ]{}\ 0. |  |

###### Proof sketch.

By complementary slackness ([4.13](https://arxiv.org/html/2511.01486v2#S4.E13 "Equation 4.13 ‣ Theorem 4.9. ‣ 4.2 Existence of the Minimizing Flow ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), the optimal multiplier satisfies α∗​(K)↓0\alpha^{\ast}(K)\downarrow 0 as K↑∞K\uparrow\infty. Hence the constrained optimizers m∗,Km^{\ast,K} minimize

|  |  |  |
| --- | --- | --- |
|  | 𝔼​\ilimits@0T​[γ2​(ρbart​(mt)−a^t)2+α∗​(K)​KL⁡(mt​\|​πt)]​d​t.\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\!\Big[\tfrac{\gamma}{2}\big(\bar{\rho}\_{t}(m\_{t})-\mathaccent 866{a}\_{t}\big)^{2}+\alpha^{\ast}(K)\,\operatorname{KL}(m\_{t}\|\pi\_{t})\Big]\,dt. |  |

Let m0m^{0} be as in Proposition [4.5](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1 Preliminaries and Model Set-Up ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective"); using it as a competitor yields ℒ​(m∗,K)≤α∗​(K)​𝔼​\ilimits@0T​KL⁡(mt0​\|​πt)​d​t\mathcal{L}(m^{\ast,K})\leq\alpha^{\ast}(K)\,\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\!\operatorname{KL}(m^{0}\_{t}\|\pi\_{t})\,dt. Since α∗​(K)→0\alpha^{\ast}(K)\to 0, this forces ([4.29](https://arxiv.org/html/2511.01486v2#S4.E29 "Equation 4.29 ‣ Theorem 4.17. ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")). For ([4.30](https://arxiv.org/html/2511.01486v2#S4.E30 "Equation 4.30 ‣ Theorem 4.17. ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), note that S~(K)−S^\mathaccent 869{S}^{(K)}-\mathaccent 866{S} solves d​(S~(K)−S^)t=β​(ψt(K)−a^t)​d​td(\mathaccent 869{S}^{(K)}-\mathaccent 866{S})\_{t}=\beta(\psi\_{t}^{(K)}-\mathaccent 866{a}\_{t})\,dt, therefore the pathwise bound and the L1L^{1}–bound follow by Cauchy–Schwarz.
∎

### 4.5 Example: Uniform Prior and Affine Proposal Drifts

Fix tt and suppose πt\pi\_{t} is uniform on [0,1][0,1]. To ensure relaxing the constraint leads to matching the observable drift, define the expert proposal as a deviation from the filtered drift:

|  |  |  |
| --- | --- | --- |
|  | ρtλ=a^t+c1​(t)​λ,c1​(t)>0,λ∈[0,1],\rho\_{t}^{\lambda}\;=\;\mathaccent 866{a}\_{t}\;+\;c\_{1}(t)\,\lambda,\qquad c\_{1}(t)>0,\ \ \lambda\in[0,1], |  |

and write c1=c1​(t)c\_{1}=c\_{1}(t) for brevity. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Zt​(θ)\displaystyle Z\_{t}(\theta) | =\ilimits@01​e−θ​(a^t+c1​λ)​d​λ=e−θ​a^t​1−e−θ​c1θ​c1,\displaystyle=\intslop\ilimits@\_{0}^{1}e^{-\theta(\mathaccent 866{a}\_{t}+c\_{1}\lambda)}\,d\lambda=e^{-\theta\mathaccent 866{a}\_{t}}\,\frac{1-e^{-\theta c\_{1}}}{\theta c\_{1}}, |  | (4.31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψt​(θ)\displaystyle\psi\_{t}(\theta) | =\ilimits@01​(a^t+c1​λ)​e−θ​(a^t+c1​λ)​d​λ\ilimits@01​e−θ​(a^t+c1​λ)​d​λ=a^t+c1​(1θ​c1−1eθ​c1−1),\displaystyle=\frac{\intslop\ilimits@\_{0}^{1}(\mathaccent 866{a}\_{t}+c\_{1}\lambda)\,e^{-\theta(\mathaccent 866{a}\_{t}+c\_{1}\lambda)}\,d\lambda}{\intslop\ilimits@\_{0}^{1}e^{-\theta(\mathaccent 866{a}\_{t}+c\_{1}\lambda)}\,d\lambda}=\mathaccent 866{a}\_{t}+c\_{1}\left(\frac{1}{\theta c\_{1}}-\frac{1}{e^{\theta c\_{1}}-1}\right), |  | (4.32) |

with ψt​(0)=a^t+c1/2\psi\_{t}(0)=\mathaccent 866{a}\_{t}+c\_{1}/2 and ψt​(θ)↓a^t\psi\_{t}(\theta)\downarrow\mathaccent 866{a}\_{t} as θ→∞\theta\to\infty.

For any α>0\alpha>0 there is a unique θt∗\theta\_{t}^{\ast} solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | c1​(1θ​c1−1eθ​c1−1)=αγ​θ,c\_{1}\left(\frac{1}{\theta c\_{1}}-\frac{1}{e^{\theta c\_{1}}-1}\right)=\frac{\alpha}{\gamma}\,\theta, |  | (4.33) |

and the optimal kernel ([4.26](https://arxiv.org/html/2511.01486v2#S4.E26 "Equation 4.26 ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) has density

|  |  |  |
| --- | --- | --- |
|  | mt∗​(d​λ)=θt∗​c1​e−θt∗​c1​λ1−e−θt∗​c1​d​λon ​[0,1].m\_{t}^{\ast}(d\lambda)=\frac{\theta\_{t}^{\ast}c\_{1}\,e^{-\theta\_{t}^{\ast}c\_{1}\,\lambda}}{1-e^{-\theta\_{t}^{\ast}c\_{1}}}\,d\lambda\quad\text{on }[0,1]. |  |

The pointwise KL reads

|  |  |  |
| --- | --- | --- |
|  | KL​(mt∗​\|​πt)=−θt∗​ψt​(θt∗)−log⁡Zt​(θt∗)=−1+θt∗​c1eθt∗​c1−1−log⁡(1−e−θt∗​c1)+log⁡(θt∗​c1),\mathrm{KL}(m\_{t}^{\ast}\|\pi\_{t})=-\theta\_{t}^{\ast}\,\psi\_{t}(\theta\_{t}^{\ast})-\log Z\_{t}(\theta\_{t}^{\ast})=-1+\frac{\theta\_{t}^{\ast}c\_{1}}{e^{\theta\_{t}^{\ast}c\_{1}}-1}-\log\!\big(1-e^{-\theta\_{t}^{\ast}c\_{1}}\big)+\log(\theta\_{t}^{\ast}c\_{1}), |  |

and the global constraint uniquely selects α∗>0\alpha^{\ast}>0 solving
𝔼​\ilimits@0T​KL​(mt∗​\|​πt)​d​t=K\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\mathrm{KL}(m\_{t}^{\ast}\|\pi\_{t})\,dt=K,
or returns α∗=0\alpha^{\ast}=0 if the constraint is slack. Since θ↦KL​(mt∗​\|​πt)\theta\mapsto\mathrm{KL}(m\_{t}^{\ast}\|\pi\_{t}) is strictly increasing for θ>0\theta>0, K↑K\uparrow implies θt∗↑\theta\_{t}^{\ast}\uparrow and thus ψt​(θt∗)↓a^t\psi\_{t}(\theta\_{t}^{\ast})\downarrow\mathaccent 866{a}\_{t}, so the aggregated mean (and hence the synthetic drift) converges to the filtered drift as K→∞K\to\infty. More precisely, as θ↑∞\theta\uparrow\infty, the mt∗​(d​λ)m\_{t}^{\ast}(d\lambda) converges weakly to δ{λ=0}\delta\_{\{\lambda=0\}}, the zero–loss selector m0m^{0}, and ψ​(θ)↓a^\psi(\theta)\downarrow\mathaccent 866{a}. Therefore, for the synthetic model

|  |  |  |
| --- | --- | --- |
|  | d​S~t=((1−β)​a^t+β​ψt​(θt∗))​d​t+σ^t​d​W^t,d\mathaccent 869{S}\_{t}\ =\ \big((1-\beta)\mathaccent 866{a}\_{t}+\beta\,\psi\_{t}(\theta^{\ast}\_{t})\big)dt\ +\ \mathaccent 866{\sigma}\_{t}\,d\mathaccent 866{W}\_{t}, |  |

the drift collapses monotonically to a^t\mathaccent 866{a}\_{t} as K↑∞K\uparrow\infty, and S~\mathaccent 869{S} converges to the observable filter S^\mathaccent 866{S} in the sense of Theorem [4.17](https://arxiv.org/html/2511.01486v2#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.4 Optimal Adapted Measure-Valued Control ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective").

###### Remark 4.18.

If a^t\mathaccent 866{a}\_{t} equals the essential infimum/supremum of ρtλ\rho\_{t}^{\lambda} (e.g. here the infimum at λ=0\lambda=0 when c1>0c\_{1}>0), then θt∗=±∞\theta\_{t}^{\ast}=\pm\infty in ([4.33](https://arxiv.org/html/2511.01486v2#S4.E33 "Equation 4.33 ‣ 4.5 Example: Uniform Prior and Affine Proposal Drifts ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and mt∗m\_{t}^{\ast} concentrates on the corresponding extremal set; this is obtained as a limit of the formulas above.

### 4.6 Simulation of the True, Observed and Opinion-Biased Price Processes

On a filtered probability space, the *true* log–price XX is given by

|  |  |  |
| --- | --- | --- |
|  | d​Xt=at​d​t−12​σ2​d​t+σ​d​WtS,St=S0​eXt.dX\_{t}\;=\;a\_{t}\,dt\;-\;\tfrac{1}{2}\,\sigma^{2}\,dt\;+\;\sigma\,dW\_{t}^{S},\qquad S\_{t}=S\_{0}e^{X\_{t}}. |  |

The trader observes a drift–signal (used in the code for filtering)

|  |  |  |
| --- | --- | --- |
|  | d​Yt=at​d​t+R1/2​d​Bt,dY\_{t}\;=\;a\_{t}\,dt\;+\;R^{1/2}\,dB\_{t}, |  |

and forms the filtered drift a^t:=𝔼​[at​ℱt]\mathaccent 866{a}\_{t}:=\mathbb{E}[a\_{t}\mid\mathcal{F}\_{t}]. The *filtered* price admits the innovation representation

|  |  |  |
| --- | --- | --- |
|  | d​S^t=a^t​d​t+σ^t​d​W^t,d\mathaccent 866{S}\_{t}\;=\;\mathaccent 866{a}\_{t}\,dt\;+\;\mathaccent 866{\sigma}\_{t}\,d\mathaccent 866{W}\_{t}, |  |

with W^\mathaccent 866{W} an 𝔽\mathbb{F}–Brownian motion and σ^t≥0\mathaccent 866{\sigma}\_{t}\geq 0.
Given an aggregation weight β∈[0,1]\beta\in[0,1] and an aggregated mean ψt\psi\_{t}, the *synthetic* price is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S~t=((1−β)​a^t+β​ψt)​d​t+σ^t​d​W^t,S~0=S^0.d\mathaccent 869{S}\_{t}\;=\;\Big((1-\beta)\,\mathaccent 866{a}\_{t}+\beta\,\psi\_{t}\Big)dt\;+\;\mathaccent 866{\sigma}\_{t}\,d\mathaccent 866{W}\_{t},\qquad\mathaccent 869{S}\_{0}=\mathaccent 866{S}\_{0}. |  | (4.34) |

At time tt, experts λ∈[0,1]\lambda\in[0,1] propose their individual bias terms

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρtλ=a^t+c1​(t)​λ,c1​(t)>0,\rho\_{t}^{\lambda}\;=\;\mathaccent 866{a}\_{t}\;+\;c\_{1}(t)\,\lambda,\qquad c\_{1}(t)>0, |  | (4.35) |

with prior πt\pi\_{t} on [0,1][0,1], where πt=Beta​(aπ,bπ)\pi\_{t}=\mathrm{Beta}(a\_{\pi},b\_{\pi}). For θ∈ℝ\theta\in\mathbb{R} the Gibbs measure optimizer is

|  |  |  |
| --- | --- | --- |
|  | mt∗​(d​λ)=e−θ​ρtλZt​(θ)​πt​(d​λ),Zt​(θ):=\ilimits@01​e−θ​ρtλ​πt​(d​λ),m\_{t}^{\ast}(d\lambda)\;=\;\frac{e^{-\theta\,\rho\_{t}^{\lambda}}}{Z\_{t}(\theta)}\,\pi\_{t}(d\lambda),\qquad Z\_{t}(\theta):=\intslop\ilimits@\_{0}^{1}e^{-\theta\,\rho\_{t}^{\lambda}}\,\pi\_{t}(d\lambda), |  |

and the *aggregated mean* ψt​(θ):=\ilimits@01​ρtλ​mt∗​(d​λ)=−dd​θ​log⁡Zt​(θ)\psi\_{t}(\theta)\;:=\;\intslop\ilimits@\_{0}^{1}\rho\_{t}^{\lambda}\,m\_{t}^{\ast}(d\lambda)\;=\;-\frac{d}{d\theta}\log Z\_{t}(\theta).

For the Beta prior πt=Beta​(aπ,bπ)\pi\_{t}=\mathrm{Beta}(a\_{\pi},b\_{\pi}) and ρtλ=a^t+c1​λ\rho\_{t}^{\lambda}=\mathaccent 866{a}\_{t}+c\_{1}\lambda, letting u:=−θ​c1u:=-\theta c\_{1} and M​(u):=F11​(aπ;aπ+bπ;u)M(u):={}\_{1}F\_{1}(a\_{\pi};a\_{\pi}+b\_{\pi};u), the confluent hypergeometric function,

|  |  |  |
| --- | --- | --- |
|  | Zt​(θ)=e−θ​a^t​M​(u),ψt​(θ)=a^t+c1​aπaπ+bπ​F11​(aπ+1;aπ+bπ+1;u)F11​(aπ;aπ+bπ;u).Z\_{t}(\theta)=e^{-\theta\mathaccent 866{a}\_{t}}M(u),\qquad\psi\_{t}(\theta)=\mathaccent 866{a}\_{t}+c\_{1}\frac{a\_{\pi}}{a\_{\pi}+b\_{\pi}}\frac{{}\_{1}F\_{1}(a\_{\pi}{+}1;a\_{\pi}{+}b\_{\pi}{+}1;u)}{{}\_{1}F\_{1}(a\_{\pi};a\_{\pi}{+}b\_{\pi};u)}. |  |

The pointwise KL at the optimizer is

|  |  |  |
| --- | --- | --- |
|  | KL⁡(mt∗​\|​πt)=−θ​ψt​(θ)−log⁡Zt​(θ)=−θ​c1​aπaπ+bπ​F11​(aπ+1;aπ+bπ+1;u)F11​(aπ;aπ+bπ;u)−log⁡M​(u).\operatorname{KL}\!\big(m\_{t}^{\ast}\|\pi\_{t}\big)\;=\;-\theta\,\psi\_{t}(\theta)-\log Z\_{t}(\theta)\;=\;-\theta c\_{1}\,\frac{a\_{\pi}}{a\_{\pi}+b\_{\pi}}\frac{{}\_{1}F\_{1}(a\_{\pi}{+}1;a\_{\pi}{+}b\_{\pi}{+}1;u)}{{}\_{1}F\_{1}(a\_{\pi};a\_{\pi}{+}b\_{\pi};u)}-\log M(u). |  |

θ=θ​(K)\theta=\theta(K) is selected from
𝔼​\ilimits@0T​KL⁡(mt∗​\|​πt)​d​t=K\mathbb{E}\!\intslop\ilimits@\_{0}^{T}\operatorname{KL}(m\_{t}^{\ast}\|\pi\_{t})\,dt=K.

From ([4.18](https://arxiv.org/html/2511.01486v2#S4.E18 "Equation 4.18 ‣ Proposition 4.10. ‣ 4.3 Identification of the Form of the Minimizing Measures ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) and Zt′′/Zt−(Zt′/Zt)2=Varmt∗​(ρtλ)Z\_{t}^{\prime\prime}/Z\_{t}-(Z\_{t}^{\prime}/Z\_{t})^{2}=\mathrm{Var}\_{m\_{t}^{\ast}}(\rho\_{t}^{\lambda}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​θ​ψt​(θ)=−Varmt∗​(ρtλ)≤0,dd​θ​KL⁡(mt∗​\|​πt)=θ​Varmt∗​(ρtλ)≥0.\frac{d}{d\theta}\psi\_{t}(\theta)\;=\;-\mathrm{Var}\_{m\_{t}^{\ast}}(\rho\_{t}^{\lambda})\ \leq 0,\qquad\frac{d}{d\theta}\operatorname{KL}\big(m\_{t}^{\ast}\|\pi\_{t}\big)\;=\;\theta\,\mathrm{Var}\_{m\_{t}^{\ast}}(\rho\_{t}^{\lambda})\ \geq 0. |  | (4.36) |

Hence K1<K2⇒θ​(K1)<θ​(K2)⇒ψt​(θ​(K1))>ψt​(θ​(K2))K\_{1}<K\_{2}\Rightarrow\theta(K\_{1})<\theta(K\_{2})\Rightarrow\psi\_{t}\big(\theta(K\_{1})\big)>\psi\_{t}\big(\theta(K\_{2})\big).
With the choice ([4.35](https://arxiv.org/html/2511.01486v2#S4.E35 "Equation 4.35 ‣ 4.6 Simulation of the True, Observed and Opinion-Biased Price Processes ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")), ψt​(θ)↓a^t\psi\_{t}(\theta)\downarrow\mathaccent 866{a}\_{t} as θ↑∞\theta\uparrow\infty,
so the synthetic drift in ([4.34](https://arxiv.org/html/2511.01486v2#S4.E34 "Equation 4.34 ‣ 4.6 Simulation of the True, Observed and Opinion-Biased Price Processes ‣ 4 Optimal Aggregation of Expert Opinions under Information Constraints ‣ Differential Beliefs in Financial Markets Under Information Constraints: A Modeling Perspective")) converges monotonically to a^t\mathaccent 866{a}\_{t} when K→∞K\to\infty
(S~\mathaccent 869{S} collapses to S^\mathaccent 866{S}).

| KK | θ\theta | α\alpha | KL/T\mathrm{KL}/T | δshift\delta\_{\text{shift}} |
| --- | --- | --- | --- | --- |
| 0.010.01 | 1.0138111.013811 | 0.233880.23388 | 0.0100000.010000 | 0.2371100.237110 |
| 0.50.5 | 9.4862389.486238 | 0.01381320.0138132 | 0.5000000.500000 | 0.1310350.131035 |
| 55 | 192.478831192.478831 | 5.27449×10−55.27449\times 10^{-5} | 5.0000005.000000 | 0.0101520.010152 |
| 2020 | 364373.533564364373.533564 | 1.50637×10−111.50637\times 10^{-11} | 20.00000020.000000 | 5×10−65\times 10^{-6} |

![Refer to caption](Sim3.png)


Figure 3: Rows: increasing constraints K1<K2<K3<K4K\_{1}<K\_{2}<K\_{3}<K\_{4}. Columns: true StS\_{t} (blue), filtered S^t\mathaccent 866{S}\_{t} (black), synthetic S~t\mathaccent 869{S}\_{t} (red). Common yy–scale across all panels. Average Corr​(a,a^)\mathrm{Corr}(a,\mathaccent 866{a}) across 30 paths is 0.85010.8501.

## 5 Conclusion

We have studied three successively more specialized models of financial markets under information constraints with traders with differential beliefs. Our analysis has shown that under a fairly natural compatibility condition, increasing information leads to an efficient market as defined in [[28](https://arxiv.org/html/2511.01486v2#bib.bib28)] provided the increase in information is uniform across different traders. The more specialized model incorporating an individual trader’s biases introduced a novel way of measuring the impact of a trader’s intuitive sense of ambiguity regarding the true value of a partially observed price process. Again, under some natural assumptions, increasing information leads to a decrease in this ambiguity and hence shrinking biases. Finally, we solved a stochastic optimal control problem for a trader seeking positive alphas as defined in [[29](https://arxiv.org/html/2511.01486v2#bib.bib29)], i.e. an arbitrage opportunity or a dominated asset. From a mathematical point of view, our optimal solution is formally similar to well-known results in information theory and information geometry. All our theoretical results were implemented in simulations and hence are well-suited for practical applications to asset pricing in markets with significant information constraints and price evolutions affected by differential beliefs of market participants.

## References

* [1]

  M. Agueh and G. Carlier.
  *Barycenters in the Wasserstein Space*.
  SIAM Journal on Mathematical Analysis, 43(2):904–924, 2011.
* [2]

  N. U. Ahmed.
  *Dynamic Systems and Control with Applications*.
  World Scientific, 2006.
* [3]

  C. D. Aliprantis and K. C. Border.
  *Infinite Dimensional Analysis: A Hitchhiker’s Guide*.
  3rd ed., Springer, 2006.
* [4]

  K. Bahlali, M. A. Mezerdi, and B. Mezerdi.
  Stability of McKean–Vlasov stochastic differential equations and applications.
  arXiv:1902.03478, 2019.
* [5]

  K. Bahlali, M. Mezerdi, and B. Mezerdi.
  Existence and optimality conditions for relaxed mean-field stochastic control problems.
  *Systems & Control Letters* 102 (2017), 1–8.
* [6]

  A. Bain and D. Crisan.
  *Fundamentals of Stochastic Filtering*.
  Springer, 2009.
* [7]

  J. Frédéric Bonnans.
  *Convex and Stochastic Optimization*.
  Springer, 2019.
* [8]

  R. Carmona.
  *Lectures on BSDEs, Stochastic Control, and Stochastic Differential Games with Financial Applications*.
  SIAM, 2016.
* [9]

  R. Carmona and F. Delarue.
  *Probabilistic Theory of Mean Field Games with Applications I*.
  Springer, 2018.
* [10]

  R. Carmona and F. Delarue.
  *Probabilistic Theory of Mean Field Games with Applications II*.
  Springer, 2018.
* [11]

  T. M. Cover and J. A. Thomas.
  *Elements of Information Theory*.
  Wiley, 2nd ed., 2006.
* [12]

  I. Csiszár.
  II-divergence geometry of probability distributions and minimization problems.
  *Annals of Probability*, 3(1):146–158, 1975.
* [13]

  A. Dembo and O. Zeitouni.
  *Large Deviations Techniques and Applications*.
  Springer, 2nd ed., 1998.
* [14]

  P. Dupuis and R. S. Ellis.
  *A Weak Convergence Approach to the Theory of Large Deviations*.
  Wiley, 1997.
* [15]

  T. van Erven and P. Harremoës.
  *Rényi Divergence and Kullback–Leibler Divergence*.
  arXiv:1206.2459, 2012.
* [16]

  H. O. Fattorini.
  *Infinite Dimensional Optimization and Control Theory*.
  Encyclopedia of Mathematics and its Applications, Vol. 62. Cambridge University Press, Cambridge, 1999.
* [17]

  C. Genest, K. J. McConway, and M. J. Schervish.
  Characterization of externally Bayesian pooling operators.
  *Annals of Statistics*, 14(2):487–501, 1986.
* [18]
   K. Grigorian, R.A. Jarrow, 2023, Enlargement of
  Filtrations: An Exposition of Core Ideas with Financial Examples,
  working paper, Cornell University.
* [19]
   K. Grigorian, R.A. Jarrow, 2024, Filtration Reduction
  and Incomplete Markets, Frontiers of Mathematical Finance, 3(1), 78-105.
* [20]
   K. Grigorian, R.A. Jarrow, 2025, Filtration Reduction
  and Completeness in Brownian Motion Models, Frontiers of Mathematical Finance, Vol. 5, 94-120.
* [21]
   K. Grigorian, R.A. Jarrow, 2023, Filtration Reduction and Completeness in Jump-Diffusion Models, working paper, Cornell University.
* [22]
   K. Grigorian, R.A. Jarrow, 2024, Option Pricing in an Incomplete Market, The Quarterly Journal of Finance, Vol. 14, No 03.
* [23]
   K. Grigorian, R.A. Jarrow,
  2025, No arbitrage for a special class of filtration expansions, Annals of Finance, 21, 45-68.
* [24]

  T. Heskes.
  Selecting weighting factors in logarithmic opinion pools.
  In *NeurIPS*, 1998.
* [25]

  Z. Hu and L. J. Hong.
  Kullback–Leibler divergence constrained distributionally robust optimization.
  *Optimization Online* preprint, 2013.
* [26]

  S. Jaimungal and S. M. Pesenti,
  *Kullback–Leibler Barycentre of Stochastic Processes*, Apr 2025. <https://arxiv.org/abs/2407.04860>.
* [27]

  R. A. Jarrow.
  *Continuous-Time Asset Pricing Theory: A Martingale-Based Approach*, 2nd ed.
  Springer, 2021.
* [28]

  R. A. Jarrow and M. Larsson.
  The Meaning of Market Efficiency.
  *Mathematical Finance*, 22(1):1–30, 2012.
* [29]

  R. A. Jarrow and P. Protter.
  *Positive alphas and a generalized multiple-factor asset pricing model*.
  Mathematics and Financial Economics, 10(1):29–48, 2016.
* [30]

  O. Kallenberg.
  *Foundations of Modern Probability*, 2nd ed.
  Springer, 2002.
* [31]

  B. Øksendal and A. Sulem,
  *Applied Stochastic Control of Jump Diffusions*, 3rd ed., Springer, 2019.
* [32]

  R. T. Rockafellar and R. J.-B. Wets.
  *Variational Analysis*.
  Springer, 1998.
* [33]

  M. J. Wainwright and M. I. Jordan.
  *Graphical Models, Exponential Families, and Variational Inference*.
  Foundations and Trends in Machine Learning, 1(1–2):1–305, 2008.
* [34]

  J. Xiong.
  *An Introduction to Stochastic Filtering Theory*.
  Oxford University Press, 2008.

## Appendix A

Let (,d)(\Lambda,d) be a compact metric space and let 𝒫​()\mathcal{P}(\Lambda) denote the space of Borel probability measures on . Write W2W\_{2} for the 2–Wasserstein distance on 𝒫​()\mathcal{P}(\Lambda) induced by dd. Since is compact, every probability measure has finite second moment, so 𝒫​()=𝒫2​()\mathcal{P}(\Lambda)=\mathcal{P}\_{2}(\Lambda), and the W2W\_{2}–topology coincides with the topology of weak convergence. In particular, (𝒫​(),W2)(\mathcal{P}(\Lambda),W\_{2}) is compact and its Borel σ\sigma–algebra, denoted as ℬ​(𝒫​())\mathcal{B}(\mathcal{P}(\Lambda)), agrees with the Borel σ\sigma–algebra ℬw​(𝒫​())\mathcal{B}\_{w}(\mathcal{P}(\Lambda)) for the weak topology.

A *flow of probability kernels* on is a map (t,ω)⟼mt​(ω)∈𝒫​()(t,\omega)\longmapsto m\_{t}(\omega)\in\mathcal{P}(\Lambda) that is (ℬ​([0,T])⊗ℱ)(\mathcal{B}([0,T])\otimes\mathcal{F})–measurable as a map from [0,T]×[0,T]\times\Omega into the Polish space (𝒫​(),ℬ​(𝒫​()))(\mathcal{P}(\Lambda),\mathcal{B}(\mathcal{P}(\Lambda))).

We say mm is *𝔽\mathbb{F}–adapted* if, for each fixed t∈[0,T]t\in[0,T], the map ω⟼mt​(ω)\omega\longmapsto m\_{t}(\omega) is (ℱt,ℬ(𝒫())(\mathcal{F}\_{t},\mathcal{B}(\mathcal{P}(\Lambda))–measurable.

Let 𝒫​(𝔽)\mathcal{P}(\mathbb{F}) denote the progressive σ\sigma–algebra on [0,T]×[0,T]\times\Omega so that, for each tt, the restriction to [0,t]×[0,t]\times\Omega coincides with ℬ​([0,t])⊗ℱt\mathcal{B}([0,t])\otimes\mathcal{F}\_{t}. We say mm is *progressively measurable* if (t,ω)⟼mt​(ω)(t,\omega)\longmapsto m\_{t}(\omega) is 𝒫​(𝔽)\mathcal{P}(\mathbb{F})–measurable as a map into (𝒫​(),ℬ​(𝒫​()))(\mathcal{P}(\Lambda),\mathcal{B}(\mathcal{P}(\Lambda))).

###### Lemma .1.

Let be Polish and let (,ℱ)(\Omega,\mathcal{F}) be a measurable space. For a map
μ:→𝒫()\mu:\Omega\to\mathcal{P}(\Lambda) with 𝒫​()\mathcal{P}(\Lambda) endowed with the weak topology and its Borel σ\sigma–algebra ℬw​(𝒫​())\mathcal{B}\_{w}(\mathcal{P}(\Lambda)), the following are equivalent:

1. (i)

   μ\mu is (ℱ,ℬw​(𝒫​()))(\mathcal{F},\mathcal{B}\_{w}(\mathcal{P}(\Lambda)))–measurable;
2. (ii)

   for all φ∈Cb​()\varphi\in C\_{b}(\Lambda), the map ω↦\ilimits@​φ​(λ)​d​μ​(ω,d​λ)\omega\mapsto\intslop\ilimits@\varphi(\lambda)\,d\mu(\omega,d\lambda) is ℱ\mathcal{F}–measurable;
3. (iii)

   for all open G⊂G\subset\Lambda, the map ω↦μ​(ω,G)\omega\mapsto\mu(\omega,G) is ℱ\mathcal{F}–measurable;
4. (iv)

   for all B∈ℬ​()B\in\mathcal{B}(\Lambda), the map ω↦μ​(ω,B)\omega\mapsto\mu(\omega,B) is ℱ\mathcal{F}–measurable.

###### Proof.

Standard. See Kallenberg, [[30](https://arxiv.org/html/2511.01486v2#bib.bib30)], Lemma 1.40.
∎

###### Lemma .2.

Assume (A1). Then

1. 1.

   If mm is adapted, then for each fixed tt, the map
   ω↦ρbart​(mt)​(ω):=\ilimits@​ρtλ​(ω)​mt​(ω,d​λ)\omega\mapsto\bar{\rho}\_{t}(m\_{t})(\omega):=\intslop\ilimits@\rho\_{t}^{\lambda}(\omega)\,m\_{t}(\omega,d\lambda) is
   ℱt\mathcal{F}\_{t}–measurable.
2. 2.

   If mm is progressively measurable, then the map
   (t,ω)↦ρbart​(mt)​(ω)(t,\omega)\mapsto\bar{\rho}\_{t}(m\_{t})(\omega) is 𝒫​(𝔽)\mathcal{P}(\mathbb{F})–measurable (hence progressively
   measurable as a real–valued process).

###### Proof.

Standard. Follows from Kallenberg, [[30](https://arxiv.org/html/2511.01486v2#bib.bib30)], Lemma 1.41 by standard arguments.
∎