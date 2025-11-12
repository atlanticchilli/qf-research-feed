---
authors:
- N. S. Gonchar
doc_id: arxiv:2010.13630v1
family_id: arxiv:2010.13630
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2010.13630] 1 Introduction.'
url_abs: http://arxiv.org/abs/2010.13630v1
url_html: https://ar5iv.org/html/2010.13630v1
venue: arXiv q-fin
version: 1
year: 2020
---

Derivatives Pricing in Non-Arbitrage Market

N.S. Gonchar 111This work was partially supported by the Program of Fundamental Research of the Department of Physics and Astronomy of the National Academy of Sciences of Ukraine ”Mathematical models of non equilibrium processes in open systems” N 0120U100857.

Bogolyubov Institute for Theoretical Physics of NAS of Ukraine.

###### Abstract

The general method is proposed for constructing a family of martingale measures for a wide class of evolution of risky assets. The sufficient conditions are formulated for the evolution of risky assets under which the family of equivalent martingale measures to the original measure is a non-empty set. The set of martingale measures is constructed from a set of strictly nonnegative random variables, satisfying certain conditions. The inequalities are obtained for the non-negative random variables satisfying certain conditions. Using these inequalities, a new simple proof of optional decomposition theorem for the nonnegative super-martingale is proposed. The family of spot measures is introduced and the representation is found for them. The conditions are found under which each martingale measure is an integral over the set of spot measures. On the basis of nonlinear processes such as ARCH and GARCH, the parametric family of random processes is introduced for which the interval of non-arbitrage prices are found.
The formula is obtained for the fair price of the contract with option of European type for the considered parametric processes. The parameters of the introduced random processes are estimated and the estimate is found at which the fair price of contract with option is the least.

Keywords: Random process; Spot set of measures;

Optional Doob decomposition; Super-martingale;

Martingale; Assessment of derivatives.

## 1 Introduction.

The study of non-arbitrage markets was begun for the first time in Bachelier’s work [[1](#bib.bib1)]. Then, in the famous works of Black F. and Scholes M. [[2](#bib.bib2)] and Merton R. S. [[3](#bib.bib3)] the formula was found for the fair price of the standard call option of European type.
The absence of arbitrage in the financial market has a very transparent economic sense, since it can be considered reasonably arranged.
The concept of non arbitrage in financial market is associated with the fact that one cannot earn money without risking, that is,
to make money you need to invest in risky or risk-free assets.
The exact mathematical substantiation of the concept of non arbitrage was first made in the papers
[[4](#bib.bib4)], [[5](#bib.bib5)] for the finite probability space and in the general case in the paper [[6](#bib.bib6)]. In the continuous time evolution of risky asset, the proof of absent of arbitrage possibility see in [[7](#bib.bib7)]. The value of the established Theorems is that they make it possible to value assets.
They got a special name ”The First and The Second Fundamental Asset Pricing Theorems.” Generalizations of these Theorems are contained in papers [[8](#bib.bib8)], [[9](#bib.bib9)], [[10](#bib.bib10)].

If the martingale measure is not the only one for a given evolution of a risky asset, then a rather difficult problem of describing all martingale measures arises in order to evaluate, for example, derivatives.

Assessment of risk in various systems was begun in papers [[11](#bib.bib11)],[[12](#bib.bib12)], [[13](#bib.bib13)], [[14](#bib.bib14)].

Statistical studies of the time series of the logarithm of the price ratio of risky assets contain heavy tails in distributions with strong elongation in the central region. The temporal behavior of these quantities exhibits the property of clustering and a strong dependence on the past. All this should be taken into account when building models for the evolution of risky assets.

In this paper, we generalize the results of the papers [[15](#bib.bib15)], [[16](#bib.bib16)], [[17](#bib.bib17)] and construct the evolution of risky assets for which we completely describe the set of equivalent martingale measures.

The aim of this study is to describe the family of martingale measures for a wide class of risky asset evolutions. The paper proposes the general concept for constructing the family of martingale measures equivalent to a given measure for a wide class of evolutions of risky assets.
In particular, it also contains the description of the family of martingale measures for the evolution of risky assets given by the ARCH [[18](#bib.bib18)] and GARCH [[19](#bib.bib19)], [[20](#bib.bib20)] models.
In section 2, we formulate the conditions relative to the evolution of risky assets
and give the examples of risky asset evolution satisfying these conditions.
Section 3 contains the construction of measures by recurrent relations.
It is shown that under the conditions relative to the evolution of risky assets such construction is meaningful. It is proved that the constructed set of measures is equivalent to an initial measure. In theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures."), we are proved that under certain integrability conditions of risky asset evolution the set of constructed measures is a set of martingale measures relative to this evolution of risky asset. In Section 4 we prove the inequalities for the nonnegative random values very useful for the proof of optional decomposition for the non negative super-martingales relative to the set of all martingale measures.

First, we show an integral inequality for a nonnegative random variable under the inequality for this nonnegative random variable with respect to the constructed family of measures. Further, using this integral inequality for the non-negative random variable, a pointwise system of inequalities is obtained for this non-negative random variable for a particular case. After that, the pointwise system of inequalities is obtained for the non-negative random variable in the general case. Then, using the resulting pointwise system of inequalities, an inequality is established for this non-negative random variable whose right-hand side is such that its conditional mathematical expectation is equal to one.

On the basis of the results of Section 4, in Section 5, we prove the optional decomposition for the non negative super-martingales.
In Section 6, we introduce the spot measures by the recurrent relations and find the representation for them. Using these facts under certain conditions we prove
integral representation for every martingale measure over the set of spot measures.

First, the optional decomposition for diffusion processes super-martingale was opened by by El Karoui N. and Quenez M. C. [[21](#bib.bib21)]. After that, Kramkov D. O. and Follmer H. [[22](#bib.bib22)], [[23](#bib.bib23)] proved the optional decomposition for the nonnegative bounded super-martingales. Folmer H. and Kabanov Yu. M. [[24](#bib.bib24)], [[25](#bib.bib25)] proved analogous result for an arbitrary super-martingale. Recently, Bouchard B. and Nutz M. [[26](#bib.bib26)] considered a class of discrete models and proved the necessary and sufficient conditions for the validity of the optional decomposition.

Section 7 contains applications of the results obtained.
A class of random processes is considered, which contains well-known processes of the type ARCH and GARCH ones. Two types of random processes are considered, those for which the price of an asset cannot go down to zero and those for which the price can go down to zero during the period under consideration. The first class of processes describes the evolution of well-managed assets. We will call these assets relatively stable.
For the evolution of relatively stable assets in the period under consideration, the family of martingale measures is one and the same.
The family of martingale measures for the evolution of risky assets whose price can drop to zero is contained in the family of martingale measures for the evolution of relatively stable assets. Each of the martingale measures for the considered class of evolutions is an integral over the set of spot martingale measures.

The interval of non-arbitrage prices is found for a wide class of payoff functions in the case when evolution describes relatively unstable assets.
This range is quite wide for the payoff functions of standard put and call options. The fair price of the super hedge is in this case the starting price of the underlying asset.
The estimates are found for the fair price of the super-hedge for the introduced class of evolutions with respect to stable assets.
The formulas are found for the fair price of contracts with call and put options for the evolution of assets described by parametric processes.

The same formulas are found for Asian-type put and call options. A characteristic feature of these estimates is that for the evolution of relatively stable assets the fair price of the super hedge is less than the price of the underlying asset.

In Section 8, the estimates of the parameters of risky assets included in the evolution are obtained.
The formulas are found for the fair price of contracts with call and put options for the obtained parameter estimates, and the interval of non-arbitrage prices for different statistics is found. The same results are obtained for Asian-style call and put options.

## 2 Evolutions of risky assets.

Let {ΩN,ℱN,PN}subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\} be a direct product
of the probability spaces {Ωi0,ℱi0,Pi0},i=1,N¯,

superscriptsubscriptΩ𝑖0superscriptsubscriptℱ𝑖0superscriptsubscript𝑃𝑖0𝑖
¯

1𝑁\{\Omega\_{i}^{0},{\cal F}\_{i}^{0},P\_{i}^{0}\},\ i=\overline{1,N},
ΩN=∏i=1NΩi0,subscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁superscriptsubscriptΩ𝑖0\Omega\_{N}=\prod\limits\_{i=1}^{N}\Omega\_{i}^{0}, PN=∏i=1NPi0,subscript𝑃𝑁superscriptsubscriptproduct𝑖1𝑁superscriptsubscript𝑃𝑖0P\_{N}=\prod\limits\_{i=1}^{N}P\_{i}^{0},
ℱN=∏i=1Nℱi0,subscriptℱ𝑁superscriptsubscriptproduct𝑖1𝑁superscriptsubscriptℱ𝑖0{\cal F}\_{N}=\prod\limits\_{i=1}^{N}{\cal F}\_{i}^{0}, where
the σ𝜎\sigma-algebra ℱNsubscriptℱ𝑁{\cal F}\_{N} is a minimal σ𝜎\sigma-algebra, generated by the sets ∏i=1NGi,Gi∈ℱi0.

superscriptsubscriptproduct𝑖1𝑁subscript𝐺𝑖subscript𝐺𝑖
superscriptsubscriptℱ𝑖0\prod\limits\_{i=1}^{N}G\_{i},\ G\_{i}\in{\cal F}\_{i}^{0}.
On the measurable space {ΩN,ℱN},subscriptΩ𝑁subscriptℱ𝑁\{\Omega\_{N},{\cal F}\_{N}\}, under the filtration ℱn,n=1,N¯,

subscriptℱ𝑛𝑛
¯

1𝑁{\cal F}\_{n},\ n=\overline{1,N}, we understand the minimal
σ𝜎\sigma-algebra generated by the sets ∏i=1NGi,Gi∈ℱi0,

superscriptsubscriptproduct𝑖1𝑁subscript𝐺𝑖subscript𝐺𝑖
superscriptsubscriptℱ𝑖0\prod\limits\_{i=1}^{N}G\_{i},\ G\_{i}\in{\cal F}\_{i}^{0}, where Gi=Ωi0subscript𝐺𝑖superscriptsubscriptΩ𝑖0G\_{i}=\Omega\_{i}^{0} for i>n.𝑖𝑛i>n.
We also introduce the probability spaces {Ωn,ℱn,Pn},n=1,N¯,

subscriptΩ𝑛subscriptℱ𝑛subscript𝑃𝑛𝑛
¯

1𝑁\{\Omega\_{n},{\cal F}\_{n},P\_{n}\},n=\overline{1,N}, where Ωn=∏i=1nΩi0,subscriptΩ𝑛superscriptsubscriptproduct𝑖1𝑛superscriptsubscriptΩ𝑖0\Omega\_{n}=\prod\limits\_{i=1}^{n}\Omega\_{i}^{0}, ℱn=∏i=1nℱi0,subscriptℱ𝑛superscriptsubscriptproduct𝑖1𝑛superscriptsubscriptℱ𝑖0{\cal F}\_{n}=\prod\limits\_{i=1}^{n}{\cal F}\_{i}^{0}, Pn=∏i=1nPi0.subscript𝑃𝑛superscriptsubscriptproduct𝑖1𝑛superscriptsubscript𝑃𝑖0P\_{n}=\prod\limits\_{i=1}^{n}P\_{i}^{0}.
There is a one-to-one correspondence between the sets of the σ𝜎\sigma-algebra ℱn,subscriptℱ𝑛{\cal F}\_{n}, belonging to the introduced filtration, and the sets of the σ𝜎\sigma-algebra ℱn=∏i=1nℱi0subscriptℱ𝑛superscriptsubscriptproduct𝑖1𝑛superscriptsubscriptℱ𝑖0{\cal F}\_{n}=\prod\limits\_{i=1}^{n}{\cal F}\_{i}^{0} of the measurable space {Ωn,ℱn},n=1,N¯.

subscriptΩ𝑛subscriptℱ𝑛𝑛
¯

1𝑁\{\Omega\_{n},{\cal F}\_{n}\},n=\overline{1,N}. Therefore, we don’t introduce new denotation for the σ𝜎\sigma-algebra ℱnsubscriptℱ𝑛{\cal F}\_{n} of the measurable space {Ωn,ℱn},subscriptΩ𝑛subscriptℱ𝑛\{\Omega\_{n},{\cal F}\_{n}\}, since it always will be clear the difference between
the above introduced σ𝜎\sigma-algebra ℱnsubscriptℱ𝑛{\cal F}\_{n} of filtration on the measurable space {ΩN,ℱN}subscriptΩ𝑁subscriptℱ𝑁\{\Omega\_{N},{\cal F}\_{N}\} and the σ𝜎\sigma-algebra ℱnsubscriptℱ𝑛{\cal F}\_{n} of the measurable space {Ωn,ℱn},n=1,N¯.

subscriptΩ𝑛subscriptℱ𝑛𝑛
¯

1𝑁\{\Omega\_{n},{\cal F}\_{n}\},n=\overline{1,N}.

We assume that the evolution of risky asset {Sn}n=0N,superscriptsubscriptsubscript𝑆𝑛𝑛0𝑁\{S\_{n}\}\_{n=0}^{N},
given on the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, is consistent with the filtration ℱnsubscriptℱ𝑛{\cal F}\_{n}, that is, Snsubscript𝑆𝑛S\_{n} is a ℱnsubscriptℱ𝑛{\cal F}\_{n}-measurable.
Due to the above one-to-one correspondence between the sets of the σ𝜎\sigma-algebra ℱn,subscriptℱ𝑛{\cal F}\_{n}, belonging to the introduced filtration, and the sets of the σ𝜎\sigma-algebra ℱnsubscriptℱ𝑛{\cal F}\_{n} of the measurable space {Ωn,ℱn},n=1,N¯,

subscriptΩ𝑛subscriptℱ𝑛𝑛
¯

1𝑁\{\Omega\_{n},{\cal F}\_{n}\},n=\overline{1,N}, we give the evolution of risky assets in the form {Sn​(ω1,…,ωn)}n=0N,superscriptsubscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛𝑛0𝑁\{S\_{n}(\omega\_{1},\ldots,\omega\_{n})\}\_{n=0}^{N}, where
Sn​(ω1,…,ωn)subscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛S\_{n}(\omega\_{1},\ldots,\omega\_{n}) is an ℱnsubscriptℱ𝑛{\cal F}\_{n}-measurable random variable, given on the measurable space {Ωn,ℱn}.subscriptΩ𝑛subscriptℱ𝑛\{\Omega\_{n},{\cal F}\_{n}\}. It is evident that such evolution is consistent with the filtration ℱnsubscriptℱ𝑛{\cal F}\_{n} on the measurable space {ΩN,ℱN,PN}.subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}.

Further, we assume that

|  |  |  |
| --- | --- | --- |
|  | Pn​((ω1,…,ωn)∈Ωn,Δ​Sn>0)>0,subscript𝑃𝑛formulae-sequencesubscript𝜔1…subscript𝜔𝑛subscriptΩ𝑛Δsubscript𝑆𝑛00P\_{n}((\omega\_{1},\ldots,\omega\_{n})\in\Omega\_{n},\ \Delta S\_{n}>0)>0, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn​((ω1,…,ωn)∈Ωn,Δ​Sn<0)>0,n=1,N¯,formulae-sequencesubscript𝑃𝑛formulae-sequencesubscript𝜔1…subscript𝜔𝑛subscriptΩ𝑛Δsubscript𝑆𝑛00𝑛¯  1𝑁\displaystyle P\_{n}((\omega\_{1},\ldots,\omega\_{n})\in\Omega\_{n},\ \Delta S\_{n}<0)>0,\quad n=\overline{1,N}, |  | (1) |

where Δ​Sn=Sn​(ω1,…,ωn)−Sn−1​(ω1,…,ωn−1),n=1,N¯.formulae-sequenceΔsubscript𝑆𝑛subscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1𝑛¯

1𝑁\Delta S\_{n}=S\_{n}(\omega\_{1},\ldots,\omega\_{n})-S\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}),\ n=\overline{1,N}.

Let us introduce the denotations

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωn−={(ω1,…,ωn)∈Ωn,Δ​Sn≤0},Ωn+={(ω1,…,ωn)∈Ωn,Δ​Sn>0},formulae-sequencesuperscriptsubscriptΩ𝑛formulae-sequencesubscript𝜔1…subscript𝜔𝑛subscriptΩ𝑛Δsubscript𝑆𝑛0superscriptsubscriptΩ𝑛formulae-sequencesubscript𝜔1…subscript𝜔𝑛subscriptΩ𝑛Δsubscript𝑆𝑛0\displaystyle\Omega\_{n}^{-}=\{(\omega\_{1},\ldots,\omega\_{n})\in\Omega\_{n},\ \Delta S\_{n}\leq 0\},\quad\Omega\_{n}^{+}=\{(\omega\_{1},\ldots,\omega\_{n})\in\Omega\_{n},\ \Delta S\_{n}>0\}, |  | (2) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−=−Δ​Sn​χΩn−​(ω1,…,ωn),Δ​Sn+=Δ​Sn​χΩn+​(ω1,…,ωn),formulae-sequenceΔsuperscriptsubscript𝑆𝑛Δsubscript𝑆𝑛subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛Δsuperscriptsubscript𝑆𝑛Δsubscript𝑆𝑛subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛\displaystyle\Delta S\_{n}^{-}=-\Delta S\_{n}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n}),\quad\Delta S\_{n}^{+}=\Delta S\_{n}\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n}), |  | (3) |

|  |  |  |
| --- | --- | --- |
|  | Vn​(ω1,…,ωn−1,ωn1,ωn2)=Δ​Sn−​(ω1,…,ωn−1,ωn1)+Δ​Sn+​(ω1,…,ωn−1,ωn2),subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})=\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ω1,…,ωn−1,ωn1)∈Ωn−,(ω1,…,ωn−1,ωn2)∈Ωn+.formulae-sequencesubscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛\displaystyle(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\in\Omega\_{n}^{-},\quad(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\in\Omega\_{n}^{+}. |  | (4) |

We use the following denotation Ωna,n=1,N¯,

superscriptsubscriptΩ𝑛𝑎𝑛
¯

1𝑁\Omega\_{n}^{a},\ n=\overline{1,N}, where a𝑎a takes two values −- and +.+.

Our assumption, in this paper, is that for Ωna,a=−,+,formulae-sequence

superscriptsubscriptΩ𝑛𝑎𝑎
\Omega\_{n}^{a},\ a=-,+, the representations

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωn−=⋃k=1Nn[An0,k−×Vn−1k],Ωn+=⋃k=1Nn[An0,k+×Vn−1k],Nn≤∞,formulae-sequencesuperscriptsubscriptΩ𝑛superscriptsubscript𝑘1subscript𝑁𝑛delimited-[]superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝑉𝑛1𝑘formulae-sequencesuperscriptsubscriptΩ𝑛superscriptsubscript𝑘1subscript𝑁𝑛delimited-[]superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝑉𝑛1𝑘subscript𝑁𝑛\displaystyle\Omega\_{n}^{-}=\bigcup\limits\_{k=1}^{N\_{n}}[A\_{n}^{0,k-}\times V\_{n-1}^{k}],\quad\Omega\_{n}^{+}=\bigcup\limits\_{k=1}^{N\_{n}}[A\_{n}^{0,k+}\times V\_{n-1}^{k}],\quad N\_{n}\leq\infty, |  | (5) |

are true, where

|  |  |  |
| --- | --- | --- |
|  | Ωn−1=⋃k=1NnVn−1k,An0,k−,An0,k+∈ℱn0,An0,k−∪An0,k+=Ωn0,formulae-sequencesubscriptΩ𝑛1  superscriptsubscript𝑘1subscript𝑁𝑛superscriptsubscript𝑉𝑛1𝑘superscriptsubscript𝐴𝑛  0limit-from𝑘formulae-sequencesuperscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscriptℱ𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscriptΩ𝑛0\Omega\_{n-1}=\bigcup\limits\_{k=1}^{N\_{n}}V\_{n-1}^{k},\ A\_{n}^{0,k-},\ A\_{n}^{0,k+}\in{\cal F}\_{n}^{0},\quad A\_{n}^{0,k-}\cup A\_{n}^{0,k+}=\Omega\_{n}^{0}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | An0,k−∩An0,k+=∅,Vn−1k∩Vn−1j=∅,k≠j,Vn−1k∈ℱn−1.formulae-sequencesuperscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐴𝑛  0limit-from𝑘formulae-sequencesuperscriptsubscript𝑉𝑛1𝑘superscriptsubscript𝑉𝑛1𝑗formulae-sequence𝑘𝑗superscriptsubscript𝑉𝑛1𝑘subscriptℱ𝑛1\displaystyle\quad A\_{n}^{0,k-}\cap A\_{n}^{0,k+}=\emptyset,\quad V\_{n-1}^{k}\cap V\_{n-1}^{j}=\emptyset,\quad k\neq j,\quad V\_{n-1}^{k}\in{\cal F}\_{n-1}. |  | (6) |

The number Nnsubscript𝑁𝑛N\_{n} may be finite or infinite. Since Ωn−∪Ωn+=Ωn,superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛subscriptΩ𝑛\Omega\_{n}^{-}\cup\Omega\_{n}^{+}=\Omega\_{n}, Ωn−∩Ωn+=∅,superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛\Omega\_{n}^{-}\cap\Omega\_{n}^{+}=\emptyset, and Pn​(Ωn−)>0,Pn​(Ωn+)>0,formulae-sequencesubscript𝑃𝑛superscriptsubscriptΩ𝑛0subscript𝑃𝑛superscriptsubscriptΩ𝑛0P\_{n}(\Omega\_{n}^{-})>0,\ P\_{n}(\Omega\_{n}^{+})>0, we have

|  |  |  |
| --- | --- | --- |
|  | Pn​(Ωn−)=∑k=1NnPn0​(An0,k−)​Pn−1​(Vn−1k),subscript𝑃𝑛superscriptsubscriptΩ𝑛superscriptsubscript𝑘1subscript𝑁𝑛superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘subscript𝑃𝑛1superscriptsubscript𝑉𝑛1𝑘P\_{n}(\Omega\_{n}^{-})=\sum\limits\_{k=1}^{N\_{n}}P\_{n}^{0}(A\_{n}^{0,k-})P\_{n-1}(V\_{n-1}^{k}), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn​(Ωn+)=∑k=1NnPn0​(An0,k+)​Pn−1​(Vn−1k),Pn0​(An0,k−)+Pn0​(An0,k+)=1.formulae-sequencesubscript𝑃𝑛superscriptsubscriptΩ𝑛superscriptsubscript𝑘1subscript𝑁𝑛superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘subscript𝑃𝑛1superscriptsubscript𝑉𝑛1𝑘superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘1\displaystyle P\_{n}(\Omega\_{n}^{+})=\sum\limits\_{k=1}^{N\_{n}}P\_{n}^{0}(A\_{n}^{0,k+})P\_{n-1}(V\_{n-1}^{k}),\quad P\_{n}^{0}(A\_{n}^{0,k-})+P\_{n}^{0}(A\_{n}^{0,k+})=1. |  | (7) |

Further, in this paper, we assume that Pn0​(An0,k−)>0,Pn0​(An0,k+)>0,n=1,N¯,k=1,Nn¯.formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛

0limit-from𝑘0formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛

0limit-from𝑘0formulae-sequence𝑛¯

1𝑁𝑘¯

1subscript𝑁𝑛P\_{n}^{0}(A\_{n}^{0,k-})>0,\ P\_{n}^{0}(A\_{n}^{0,k+})>0,\ n=\overline{1,N},\ k=\overline{1,N\_{n}}.
We also assume some technical suppositions: there exist subsets Bn,i0,k−∈ℱn0,superscriptsubscript𝐵

𝑛𝑖

0limit-from𝑘superscriptsubscriptℱ𝑛0B\_{n,i}^{0,k-}\in{\cal F}\_{n}^{0}, i=1,In¯,In>1,formulae-sequence𝑖¯

1subscript𝐼𝑛subscript𝐼𝑛1\ i=\overline{1,I\_{n}},\ I\_{n}>1, and Bn,s0,k+∈ℱn0,superscriptsubscript𝐵

𝑛𝑠

0limit-from𝑘superscriptsubscriptℱ𝑛0B\_{n,s}^{0,k+}\in{\cal F}\_{n}^{0}, s=1,Sn¯,Sn>1,formulae-sequence𝑠¯

1subscript𝑆𝑛subscript𝑆𝑛1\ s=\overline{1,S\_{n}},\ S\_{n}>1,
satisfying the conditions

|  |  |  |
| --- | --- | --- |
|  | Bn,i0,k−∩Bn,j0,k−=∅,i≠j,Bn,s0,k+∩Bn,l0,k+=∅,s≠l,k=1,Nn¯,formulae-sequencesuperscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑗  0limit-from𝑘formulae-sequence𝑖𝑗formulae-sequencesuperscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑙  0limit-from𝑘formulae-sequence𝑠𝑙𝑘¯  1subscript𝑁𝑛\ B\_{n,i}^{0,k-}\cap B\_{n,j}^{0,k-}=\emptyset,\ i\neq j,\quad\ B\_{n,s}^{0,k+}\cap B\_{n,l}^{0,k+}=\emptyset,\ s\neq l,\quad k=\overline{1,N\_{n}}, |  |

|  |  |  |
| --- | --- | --- |
|  | Pn0​(Bn,i0,k−)>0,i=1,In¯,Pn0​(Bn,s0,k+)>0,s=1,Sn¯,k=1,Nn¯,formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘0formulae-sequence𝑖¯  1subscript𝐼𝑛formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘0formulae-sequence𝑠¯  1subscript𝑆𝑛𝑘¯  1subscript𝑁𝑛P\_{n}^{0}(B\_{n,i}^{0,k-})>0,\ i=\overline{1,I\_{n}},\ P\_{n}^{0}(B\_{n,s}^{0,k+})>0,\ s=\overline{1,S\_{n}},\quad k=\overline{1,N\_{n}}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | An0,k−=⋃i=1InBn,i0,k−,An0,k+=⋃s=1SnBn,s0,k+,k=1,Nn¯.formulae-sequencesuperscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝑖1subscript𝐼𝑛superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘formulae-sequencesuperscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝑠1subscript𝑆𝑛superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘𝑘¯  1subscript𝑁𝑛\displaystyle A\_{n}^{0,k-}=\bigcup\limits\_{i=1}^{I\_{n}}B\_{n,i}^{0,k-},\quad A\_{n}^{0,k+}=\bigcup\limits\_{s=1}^{S\_{n}}B\_{n,s}^{0,k+},\quad k=\overline{1,N\_{n}}. |  | (8) |

Below, we give the examples of evolutions {Sn​(ω1,…,ωn)}n=1Nsuperscriptsubscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛𝑛1𝑁\{S\_{n}(\omega\_{1},\ldots,\omega\_{n})\}\_{n=1}^{N} for which the representations ([5](#S2.E5 "In 2 Evolutions of risky assets.")) are true.

Suppose that the random values ai​(ω1,…,ωi),subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖a\_{i}(\omega\_{1},\ldots,\omega\_{i}), ηi​(ωi)subscript𝜂𝑖subscript𝜔𝑖\eta\_{i}(\omega\_{i}) satisfy the inequalities
0<ai​(ω1,…,ωi)≤1,0subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖10<a\_{i}(\omega\_{1},\ldots,\omega\_{i})\leq 1, 1+ηi​(ωi)≥0,1subscript𝜂𝑖subscript𝜔𝑖01+\eta\_{i}(\omega\_{i})\geq 0,
Pi0​(ηi​(ωi)<0)>0,superscriptsubscript𝑃𝑖0subscript𝜂𝑖subscript𝜔𝑖00P\_{i}^{0}(\eta\_{i}(\omega\_{i})<0)>0, Pi0​(ηi​(ωi)>0)>0,superscriptsubscript𝑃𝑖0subscript𝜂𝑖subscript𝜔𝑖00P\_{i}^{0}(\eta\_{i}(\omega\_{i})>0)>0,
i=1,N¯.𝑖¯

1𝑁i=\overline{1,N}.
If Sn​(ω1,…,ωn)subscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛S\_{n}(\omega\_{1},\ldots,\omega\_{n}) is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn​(ω1,…,ωn)=S0​∏i=1n(1+ai​(ω1,…,ωi)​ηi​(ωi)),n=1,N¯,formulae-sequencesubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑆0superscriptsubscriptproduct𝑖1𝑛1subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖subscript𝜂𝑖subscript𝜔𝑖𝑛¯  1𝑁\displaystyle S\_{n}(\omega\_{1},\ldots,\omega\_{n})=S\_{0}\prod\limits\_{i=1}^{n}(1+a\_{i}(\omega\_{1},\ldots,\omega\_{i})\eta\_{i}(\omega\_{i})),\quad n=\overline{1,N}, |  | (9) |

then

|  |  |  |
| --- | --- | --- |
|  | {ωi∈Ωi0,ηi​(ωi)≤0}=Ai0,1−,{ωi∈Ωi0,ηi​(ωi)>0}=Ai0,1+,formulae-sequenceformulae-sequencesubscript𝜔𝑖superscriptsubscriptΩ𝑖0subscript𝜂𝑖subscript𝜔𝑖0superscriptsubscript𝐴𝑖  0limit-from1formulae-sequencesubscript𝜔𝑖superscriptsubscriptΩ𝑖0subscript𝜂𝑖subscript𝜔𝑖0superscriptsubscript𝐴𝑖  0limit-from1\{\omega\_{i}\in\Omega\_{i}^{0},\ \eta\_{i}(\omega\_{i})\leq 0\}=A\_{i}^{0,1-},\quad\{\omega\_{i}\in\Omega\_{i}^{0},\ \eta\_{i}(\omega\_{i})>0\}=A\_{i}^{0,1+}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi−11=Ωi−1,Ωi−=Ai0,1−×Ωi−1,Ωi+=Ai0,1+×Ωi−1,i=1,N¯.formulae-sequencesuperscriptsubscript𝑉𝑖11subscriptΩ𝑖1formulae-sequencesuperscriptsubscriptΩ𝑖superscriptsubscript𝐴𝑖  0limit-from1subscriptΩ𝑖1formulae-sequencesuperscriptsubscriptΩ𝑖superscriptsubscript𝐴𝑖  0limit-from1subscriptΩ𝑖1𝑖¯  1𝑁\displaystyle V\_{i-1}^{1}=\Omega\_{i-1},\quad\Omega\_{i}^{-}=A\_{i}^{0,1-}\times\Omega\_{i-1},\quad\Omega\_{i}^{+}=A\_{i}^{0,1+}\times\Omega\_{i-1},\quad i=\overline{1,N}. |  | (10) |

In general case, let us consider the evolution of risky asset {Sn​(ω1,…,ωn)}n=1N,superscriptsubscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛𝑛1𝑁\{S\_{n}(\omega\_{1},\ldots,\omega\_{n})\}\_{n=1}^{N}, given by the formula

|  |  |  |
| --- | --- | --- |
|  | Sn​(ω1,…,ωn)=subscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛absentS\_{n}(\omega\_{1},\ldots,\omega\_{n})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | S0​∏i=1n(1+∑k=1Niηik​(ωi)​χVi−1k​(ω1,…,ωi−1)​aik​(ω1,…,ωi)),n=1,N¯,  subscript𝑆0superscriptsubscriptproduct𝑖1𝑛1superscriptsubscript𝑘1subscript𝑁𝑖superscriptsubscript𝜂𝑖𝑘subscript𝜔𝑖subscript𝜒superscriptsubscript𝑉𝑖1𝑘subscript𝜔1…subscript𝜔𝑖1superscriptsubscript𝑎𝑖𝑘subscript𝜔1…subscript𝜔𝑖𝑛 ¯  1𝑁\displaystyle S\_{0}\prod\limits\_{i=1}^{n}(1+\sum\limits\_{k=1}^{N\_{i}}\eta\_{i}^{k}(\omega\_{i})\chi\_{V\_{i-1}^{k}}(\omega\_{1},\ldots,\omega\_{i-1})a\_{i}^{k}(\omega\_{1},\ldots,\omega\_{i})),\quad n=\overline{1,N}, |  | (11) |

where the random values aik​(ω1,…,ωi),superscriptsubscript𝑎𝑖𝑘subscript𝜔1…subscript𝜔𝑖a\_{i}^{k}(\omega\_{1},\ldots,\omega\_{i}), ηik​(ωi)superscriptsubscript𝜂𝑖𝑘subscript𝜔𝑖\eta\_{i}^{k}(\omega\_{i}) satisfy the inequalities
  
0<aik​(ω1,…,ωi)≤1,0superscriptsubscript𝑎𝑖𝑘subscript𝜔1…subscript𝜔𝑖10<a\_{i}^{k}(\omega\_{1},\ldots,\omega\_{i})\leq 1, 1+ηik​(ωi)≥0,1superscriptsubscript𝜂𝑖𝑘subscript𝜔𝑖01+\eta\_{i}^{k}(\omega\_{i})\geq 0,
Pi0​(ηik​(ωi)<0)>0,superscriptsubscript𝑃𝑖0superscriptsubscript𝜂𝑖𝑘subscript𝜔𝑖00P\_{i}^{0}(\eta\_{i}^{k}(\omega\_{i})<0)>0, Pi0​(ηik​(ωi)>0)>0,superscriptsubscript𝑃𝑖0superscriptsubscript𝜂𝑖𝑘subscript𝜔𝑖00P\_{i}^{0}(\eta\_{i}^{k}(\omega\_{i})>0)>0,
i=1,N¯,𝑖¯

1𝑁i=\overline{1,N},   k=1,Nn¯,𝑘¯

1subscript𝑁𝑛k=\overline{1,N\_{n}},
and
⋃k=1NiVi−1k=Ωi−1,Vi−1k∩Vi−1s,superscriptsubscript𝑘1subscript𝑁𝑖superscriptsubscript𝑉𝑖1𝑘

subscriptΩ𝑖1superscriptsubscript𝑉𝑖1𝑘superscriptsubscript𝑉𝑖1𝑠\bigcup\limits\_{k=1}^{N\_{i}}V\_{i-1}^{k}=\Omega\_{i-1},\ V\_{i-1}^{k}\cap V\_{i-1}^{s}, k≠s.𝑘𝑠k\neq s.
Then, if to put

|  |  |  |
| --- | --- | --- |
|  | {ωi∈Ωi0,ηik​(ωi)≤0}=Ai0,k−,{ωi∈Ωi0,ηik​(ωi)>0}=Ai0,k+,formulae-sequenceformulae-sequencesubscript𝜔𝑖superscriptsubscriptΩ𝑖0superscriptsubscript𝜂𝑖𝑘subscript𝜔𝑖0superscriptsubscript𝐴𝑖  0limit-from𝑘formulae-sequencesubscript𝜔𝑖superscriptsubscriptΩ𝑖0superscriptsubscript𝜂𝑖𝑘subscript𝜔𝑖0superscriptsubscript𝐴𝑖  0limit-from𝑘\{\omega\_{i}\in\Omega\_{i}^{0},\ \eta\_{i}^{k}(\omega\_{i})\leq 0\}=A\_{i}^{0,k-},\quad\{\omega\_{i}\in\Omega\_{i}^{0},\ \eta\_{i}^{k}(\omega\_{i})>0\}=A\_{i}^{0,k+}, |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωi−=⋃k=1Ni[Ai0,k−×Vi−1k],Ωi+=⋃k=1Ni[Ai0,k+×Vi−1k],i=1,N¯.formulae-sequencesuperscriptsubscriptΩ𝑖superscriptsubscript𝑘1subscript𝑁𝑖delimited-[]superscriptsubscript𝐴𝑖  0limit-from𝑘superscriptsubscript𝑉𝑖1𝑘formulae-sequencesuperscriptsubscriptΩ𝑖superscriptsubscript𝑘1subscript𝑁𝑖delimited-[]superscriptsubscript𝐴𝑖  0limit-from𝑘superscriptsubscript𝑉𝑖1𝑘𝑖¯  1𝑁\displaystyle\Omega\_{i}^{-}=\bigcup\limits\_{k=1}^{N\_{i}}[A\_{i}^{0,k-}\times V\_{i-1}^{k}],\quad\Omega\_{i}^{+}=\bigcup\limits\_{k=1}^{N\_{i}}[A\_{i}^{0,k+}\times V\_{i-1}^{k}],\quad i=\overline{1,N}. |  | (12) |

|  |  |  |
| --- | --- | --- |
|  | ΔSn(ω1,…,ωn−1,ωn)≤0,(ω1,…,ωn−1,ωn)∈Ωn−,,n=1,N¯,\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\leq 0,\quad(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\in\Omega\_{n}^{-},,\quad n=\overline{1,N}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn​(ω1,…,ωn−1,ωn)>0,(ω1,…,ωn−1,ωn)∈Ωn+,n=1,N¯.formulae-sequenceΔsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛0formulae-sequencesubscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscriptΩ𝑛𝑛¯  1𝑁\displaystyle\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})>0,\quad(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\in\Omega\_{n}^{+},\quad n=\overline{1,N}. |  | (13) |

## 3 Construction of the set of martingale measures.

In this section, we present the construction of the set of measures on the basis of evolution of risky assets given by the formulas ([9](#S2.E9 "In 2 Evolutions of risky assets.")), ([11](#S2.E11 "In 2 Evolutions of risky assets.")) on the measurable space {ΩN,ℱN}.subscriptΩ𝑁subscriptℱ𝑁\{\Omega\_{N},{\cal F}\_{N}\}. For this purpose, we use the set of nonnegative random values αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}), given on the probability space
{Ωn−×Ωn+,ℱn−×ℱn+,Pn−×Pn+},n=1,N¯,

superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛superscriptsubscriptℱ𝑛superscriptsubscriptℱ𝑛superscriptsubscript𝑃𝑛superscriptsubscript𝑃𝑛𝑛
¯

1𝑁\{\Omega\_{n}^{-}\times\Omega\_{n}^{+},{\cal F}\_{n}^{-}\times{\cal F}\_{n}^{+},P\_{n}^{-}\times P\_{n}^{+}\},\ n=\overline{1,N}, where ℱn−=ℱn∩Ωn−,ℱn+=ℱn∩Ωn+.formulae-sequencesuperscriptsubscriptℱ𝑛subscriptℱ𝑛superscriptsubscriptΩ𝑛superscriptsubscriptℱ𝑛subscriptℱ𝑛superscriptsubscriptΩ𝑛{\cal F}\_{n}^{-}={\cal F}\_{n}\cap\Omega\_{n}^{-},\ {\cal F}\_{n}^{+}={\cal F}\_{n}\cap\Omega\_{n}^{+}. The measure Pn−superscriptsubscript𝑃𝑛P\_{n}^{-} is a contraction of the measure Pnsubscript𝑃𝑛P\_{n} on the σ𝜎\sigma-algebra ℱn−superscriptsubscriptℱ𝑛{\cal F}\_{n}^{-} and
the measure Pn+superscriptsubscript𝑃𝑛P\_{n}^{+} is a contraction of the measure Pnsubscript𝑃𝑛P\_{n} on the σ𝜎\sigma-algebra ℱn+.superscriptsubscriptℱ𝑛{\cal F}\_{n}^{+}.
After that, we prove that this set of measures, defined the above set of random values, is equivalent to the measure PN.subscript𝑃𝑁P\_{N}.
At last, Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures.") gives the sufficient conditions under that the constructed set of measures is a set of martingale measures for the considered evolution of risky assets.
Sometimes, we use the abbreviated denotations {ω11,…,ωn1}={ω}n1,{ω12,…,ωn2}={ω}n2.formulae-sequencesuperscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2superscriptsubscript𝜔𝑛2\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\}=\{\omega\}\_{n}^{1},\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}=\{\omega\}\_{n}^{2}.

We assume that the set of random values αn​({ω11,…,ωn1};{ω12,…,ωn2})=αn​({ω}n1;{ω}n2),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})=\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}), ({ω}n1;{ω}n2)∈Ωn−×Ωn+,

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2
superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2})\in\Omega\_{n}^{-}\times\Omega\_{n}^{+}, n=1,N¯,𝑛¯

1𝑁\ n=\overline{1,N}, satisfies the following conditions:

|  |  |  |
| --- | --- | --- |
|  | Pn−×Pn+​(({ω}n1;{ω}n2)∈Ωn−×Ωn+,αn​({ω}n1;{ω}n2)>0)=superscriptsubscript𝑃𝑛superscriptsubscript𝑃𝑛formulae-sequence  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2 superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛subscript𝛼𝑛  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛20absentP\_{n}^{-}\times P\_{n}^{+}((\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2})\in\Omega\_{n}^{-}\times\Omega\_{n}^{+},\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2})>0)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn​(Ωn−)×Pn​(Ωn+),n=1,N¯;  subscript𝑃𝑛superscriptsubscriptΩ𝑛subscript𝑃𝑛superscriptsubscriptΩ𝑛𝑛 ¯  1𝑁\displaystyle P\_{n}(\Omega\_{n}^{-})\times P\_{n}(\Omega\_{n}^{+}),\quad n=\overline{1,N}; |  | (14) |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn−(ω11,…,ωn−11,ωn1)χΩn+(ω12,…,ωn−12,ωn2)×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})×\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)​Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn1)​d​Pn0​(ωn2)<∞,Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})<\infty, |  |

|  |  |  |
| --- | --- | --- |
|  | ({ω11,…,ωn−11};{ω12,…,ωn−12})∈Ωn−1×Ωn−1,  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12 subscriptΩ𝑛1subscriptΩ𝑛1(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2}\})\in\Omega\_{n-1}\times\Omega\_{n-1}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ω1,…,ωn−1)∈Ωn−1,n=1,N¯;formulae-sequencesubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1𝑛¯  1𝑁\displaystyle(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1},\quad n=\overline{1,N}; |  | (15) |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn−(ω11,…,ωn−11,ωn1)χΩn+(ω12,…,ωn−12,ωn2)×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})​d​Pn0​(ωn1)​d​Pn0​(ωn2)=1,subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2 𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛21\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})=1, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({ω11,…,ωn−11};{ω12,…,ωn−12})∈Ωn−1×Ωn−1,n=1,N¯.formulae-sequence  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12 subscriptΩ𝑛1subscriptΩ𝑛1𝑛¯  1𝑁\displaystyle(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2}\})\in\Omega\_{n-1}\times\Omega\_{n-1},\quad n=\overline{1,N}. |  | (16) |

In the next Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures."), we give the sufficient conditions under which the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")) are valid.

###### Lemma 1.

Suppose that for Ωna,a=−,+,n=1,N¯,formulae-sequence

superscriptsubscriptΩ𝑛𝑎𝑎

𝑛
¯

1𝑁\Omega\_{n}^{a},a=-,+,\ n=\overline{1,N}, the representations ([5](#S2.E5 "In 2 Evolutions of risky assets."))
are true. If the conditions

|  |  |  |
| --- | --- | --- |
|  | inf1≤k≤NnPn0​(An0,k−∖Bn,i0,k−)>0,i=1,In¯,In>1,n=1,N¯,formulae-sequencesubscriptinfimum1𝑘subscript𝑁𝑛superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘0formulae-sequence𝑖¯  1subscript𝐼𝑛formulae-sequencesubscript𝐼𝑛1𝑛¯  1𝑁\inf\limits\_{1\leq k\leq N\_{n}}P\_{n}^{0}(A\_{n}^{0,k-}\setminus B\_{n,i}^{0,k-})>0,\quad i=\overline{1,I\_{n}},\quad I\_{n}>1,\quad n=\overline{1,N}, |  |

|  |  |  |
| --- | --- | --- |
|  | inf1≤k≤NnPn0​(An0,k+∖Bn,s0,k+)>0,s=1,Sn¯,Sn>1,n=1,N¯,formulae-sequencesubscriptinfimum1𝑘subscript𝑁𝑛superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘0formulae-sequence𝑠¯  1subscript𝑆𝑛formulae-sequencesubscript𝑆𝑛1𝑛¯  1𝑁\inf\limits\_{1\leq k\leq N\_{n}}P\_{n}^{0}(A\_{n}^{0,k+}\setminus B\_{n,s}^{0,k+})>0,\quad s=\overline{1,S\_{n}},\quad S\_{n}>1,\quad n=\overline{1,N}, |  |

|  |  |  |
| --- | --- | --- |
|  | inf1≤k≤NnPn0​(Bn,i0,k−)>0,i=1,In¯,In>1,n=1,N¯,formulae-sequencesubscriptinfimum1𝑘subscript𝑁𝑛superscriptsubscript𝑃𝑛0superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘0formulae-sequence𝑖¯  1subscript𝐼𝑛formulae-sequencesubscript𝐼𝑛1𝑛¯  1𝑁\inf\limits\_{1\leq k\leq N\_{n}}P\_{n}^{0}(B\_{n,i}^{0,k-})>0,\quad i=\overline{1,I\_{n}},\quad I\_{n}>1,\quad n=\overline{1,N}, |  |

|  |  |  |
| --- | --- | --- |
|  | inf1≤k≤NnPn0​(Bn,s0,k+)>0,s=1,Sn¯,Sn>1,n=1,N¯,formulae-sequencesubscriptinfimum1𝑘subscript𝑁𝑛superscriptsubscript𝑃𝑛0superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘0formulae-sequence𝑠¯  1subscript𝑆𝑛formulae-sequencesubscript𝑆𝑛1𝑛¯  1𝑁\inf\limits\_{1\leq k\leq N\_{n}}P\_{n}^{0}(B\_{n,s}^{0,k+})>0,\quad s=\overline{1,S\_{n}},\quad S\_{n}>1,\quad n=\overline{1,N}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩNΔ​Sn−​(ω1,…,ωn−1,ωn)​𝑑PN<∞,n=1,N¯,formulae-sequencesubscriptsubscriptΩ𝑁Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛differential-dsubscript𝑃𝑁𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{N}}\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})dP\_{N}<\infty,\quad\ n=\overline{1,N}, |  | (17) |

are true,
then the set of bounded random values αn​({ω}n1;{ω}n2),subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}), satisfying the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")), is a nonempty set.

###### Proof.

Let us put

|  |  |  |
| --- | --- | --- |
|  | αni−​(ω11,…,ωn1)=∑k=1Nnαn,k,i−​(ωn1)​χAn0,k−​(ωn1)​χVn−1k​(ω11,…,ωn−11),superscriptsubscript𝛼𝑛limit-from𝑖superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝑘1subscript𝑁𝑛superscriptsubscript𝛼  𝑛𝑘𝑖superscriptsubscript𝜔𝑛1subscript𝜒superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝜔𝑛1subscript𝜒superscriptsubscript𝑉𝑛1𝑘superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11\alpha\_{n}^{i-}(\omega\_{1}^{1},\ldots,\omega\_{n}^{1})=\sum\limits\_{k=1}^{N\_{n}}\alpha\_{n,k,i}^{-}(\omega\_{n}^{1})\chi\_{A\_{n}^{0,k-}}(\omega\_{n}^{1})\chi\_{V\_{n-1}^{k}}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1}), |  |

|  |  |  |
| --- | --- | --- |
|  | αns+​(ω12,…,ωn2)=∑k=1Nnαn,k,s+​(ωn2)​χAn0,k+​(ωn2)​χVn−1k​(ω12,…,ωn−12),superscriptsubscript𝛼𝑛limit-from𝑠superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2superscriptsubscript𝑘1subscript𝑁𝑛superscriptsubscript𝛼  𝑛𝑘𝑠superscriptsubscript𝜔𝑛2subscript𝜒superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝜔𝑛2subscript𝜒superscriptsubscript𝑉𝑛1𝑘superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12\alpha\_{n}^{s+}(\omega\_{1}^{2},\ldots,\omega\_{n}^{2})=\sum\limits\_{k=1}^{N\_{n}}\alpha\_{n,k,s}^{+}(\omega\_{n}^{2})\chi\_{A\_{n}^{0,k+}}(\omega\_{n}^{2})\chi\_{V\_{n-1}^{k}}(\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | αn,k,i−​(ωn1)=(1−δin)​χBn,i0,k−​(ωn1)Pn0​(Bn,i0,k−)+δin​χAn0,k−∖Bn,i0,k−​(ωn1)Pn0​(An0,k−∖Bn,i0,k−),superscriptsubscript𝛼  𝑛𝑘𝑖superscriptsubscript𝜔𝑛11superscriptsubscript𝛿𝑖𝑛subscript𝜒superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘superscriptsubscript𝜔𝑛1superscriptsubscript𝑃𝑛0superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘superscriptsubscript𝛿𝑖𝑛subscript𝜒superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘superscriptsubscript𝜔𝑛1superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑖  0limit-from𝑘\alpha\_{n,k,i}^{-}(\omega\_{n}^{1})=(1-\delta\_{i}^{n})\frac{\chi\_{B\_{n,i}^{0,k-}}(\omega\_{n}^{1})}{P\_{n}^{0}(B\_{n,i}^{0,k-})}+\delta\_{i}^{n}\frac{\chi\_{A\_{n}^{0,k-}\setminus B\_{n,i}^{0,k-}}(\omega\_{n}^{1})}{P\_{n}^{0}(A\_{n}^{0,k-}\setminus B\_{n,i}^{0,k-})}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<δin<1,i=1,In¯,k=1,Nn¯,formulae-sequence0superscriptsubscript𝛿𝑖𝑛1formulae-sequence𝑖¯  1subscript𝐼𝑛𝑘¯  1subscript𝑁𝑛\displaystyle\ 0<\delta\_{i}^{n}<1,\quad i=\overline{1,I\_{n}},\quad k=\overline{1,N\_{n}}, |  | (18) |

|  |  |  |
| --- | --- | --- |
|  | αn,k,s+​(ωn2)=(1−μsn)​χBn,s0,k+​(ωn2)Pn0​(Bn,s0,k+)+μsn​χAn0,k+∖Bn,s0,k+​(ωn2)Pn0​(An0,k+∖Bn,s0,k+),superscriptsubscript𝛼  𝑛𝑘𝑠superscriptsubscript𝜔𝑛21superscriptsubscript𝜇𝑠𝑛subscript𝜒superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝑃𝑛0superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘superscriptsubscript𝜇𝑠𝑛subscript𝜒superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝐵  𝑛𝑠  0limit-from𝑘\alpha\_{n,k,s}^{+}(\omega\_{n}^{2})=(1-\mu\_{s}^{n})\frac{\chi\_{B\_{n,s}^{0,k+}}(\omega\_{n}^{2})}{P\_{n}^{0}(B\_{n,s}^{0,k+})}+\mu\_{s}^{n}\frac{\chi\_{A\_{n}^{0,k+}\setminus B\_{n,s}^{0,k+}}(\omega\_{n}^{2})}{P\_{n}^{0}(A\_{n}^{0,k+}\setminus B\_{n,s}^{0,k+})}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<μsn<1,s=1,Sn¯,k=1,Nn¯.formulae-sequence0superscriptsubscript𝜇𝑠𝑛1formulae-sequence𝑠¯  1subscript𝑆𝑛𝑘¯  1subscript𝑁𝑛\displaystyle 0<\mu\_{s}^{n}<1,\quad s=\overline{1,S\_{n}},\quad k=\overline{1,N\_{n}}. |  | (19) |

If to introduce the nonnegative set of real numbers

|  |  |  |  |
| --- | --- | --- | --- |
|  | γi,s≥0,i=1,In¯,s=1,Sn¯,∑i,s=1In,Snγi,s=1,n=1,N¯,formulae-sequencesubscript𝛾  𝑖𝑠0formulae-sequence𝑖¯  1subscript𝐼𝑛formulae-sequence𝑠¯  1subscript𝑆𝑛formulae-sequencesuperscriptsubscript  𝑖𝑠 1  subscript𝐼𝑛subscript𝑆𝑛subscript𝛾  𝑖𝑠1𝑛¯  1𝑁\displaystyle\gamma\_{i,s}\geq 0,\quad i=\overline{1,I\_{n}},\quad s=\overline{1,S\_{n}},\quad\sum\limits\_{i,s=1}^{I\_{n},S\_{n}}\gamma\_{i,s}=1,\quad n=\overline{1,N}, |  | (20) |

then

|  |  |  |
| --- | --- | --- |
|  | αn​({ω11,…,ωn1};{ω12,…,ωn2})=subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2absent\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i,s=1In,Snγi,s​αni−​(ω11,…,ωn1)​αns+​(ω12,…,ωn2),n=1,N¯,  superscriptsubscript  𝑖𝑠 1  subscript𝐼𝑛subscript𝑆𝑛subscript𝛾  𝑖𝑠superscriptsubscript𝛼𝑛limit-from𝑖superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝛼𝑛limit-from𝑠superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2𝑛 ¯  1𝑁\displaystyle\sum\limits\_{i,s=1}^{I\_{n},S\_{n}}\gamma\_{i,s}\alpha\_{n}^{i-}(\omega\_{1}^{1},\ldots,\omega\_{n}^{1})\alpha\_{n}^{s+}(\omega\_{1}^{2},\ldots,\omega\_{n}^{2}),\quad n=\overline{1,N}, |  | (21) |

satisfies the condition ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")).

Really, due to the Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") conditions, the random values αn({ω}n1;{ω}n2}),\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}\}), n=1,N¯,𝑛¯

1𝑁\ n=\overline{1,N}, are strictly positive by construction. Therefore, the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) are true.

Due to the boundedness of αn({ω}n1;{ω}n2})≤C,n=1,N¯, 0<C<∞,\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}\})\leq C,\ n=\overline{1,N},\ 0<C<\infty, the inequalities

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn−(ω11,…,ωn−11,ωn1)χΩn+(ω12,…,ωn−12,ωn2)×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})×\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)​Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn1)​d​Pn0​(ωn2)≤Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2absent\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})\leq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​∫Ωn0Δ​Sn−​(ω1,…,ωn−1,ωn1)​𝑑Pn0​(ωn1)<∞,n=1,N¯,formulae-sequence𝐶subscriptsuperscriptsubscriptΩ𝑛0Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1differential-dsuperscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑛¯  1𝑁\displaystyle C\int\limits\_{\Omega\_{n}^{0}}\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{1})<\infty,\quad n=\overline{1,N}, |  | (22) |

are true for almost everywhere
(ω1,…,ωn−1)∈Ωn−1,n=1,N¯,formulae-sequencesubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1𝑛¯

1𝑁(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1},\ n=\overline{1,N},
relative to the measure Pn−1,subscript𝑃𝑛1P\_{n-1}, owing to the inequalities ([17](#S3.E17 "In Lemma 1. ‣ 3 Construction of the set of martingale measures.")) and Foubini Theorem. This proves the inequality ([15](#S3.E15 "In 3 Construction of the set of martingale measures.")).
The equality ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")) is also satisfied due to the construction of αn​({ω}n1;{ω}n2).subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}).
Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") is proved.
∎

The values, which the random variables αn({ω}n1;{ω}n2}),n=1,N¯,\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}\}),\ n=\overline{1,N}, constructed in Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures."), take, are determined by the values at points ωn1∈Ωn0−superscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛limit-from0\omega\_{n}^{1}\in\Omega\_{n}^{0-} and ωn2∈Ωn0+superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛limit-from0\omega\_{n}^{2}\in\Omega\_{n}^{0+} for all (ω1,…,ωn−1)∈Ωn−1.subscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}.

On the basis of the set of random values αn​({ω}n1;{ω}n2),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}),\ n=\overline{1,N}, constructed in Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures."), let us introduce into consideration the family of measure μ0​(A)subscript𝜇0𝐴\mu\_{0}(A) on the measurable space {ΩN,ℱN}subscriptΩ𝑁subscriptℱ𝑁\{\Omega\_{N},{\cal F}\_{N}\} by the recurrent relations

|  |  |  |
| --- | --- | --- |
|  | μN(ω1,…,ωN−1)(A)=∫ΩN0×ΩN0χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A)=\int\limits\_{\Omega\_{N}^{0}\times\Omega\_{N}^{0}}\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αN({ω1,…,ωN−1,ωN1};{ω1,…,ωN−1,ωN2})×\alpha\_{N}(\{\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1}\};\{\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)μN(ω1,…,ωN−1,ωN1)(A)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)μN(ω1,…,ωN−1,ωN2)(A)]dPN0(ωN1)dPN0(ωN2),\displaystyle\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}(A)\right]dP\_{N}^{0}(\omega\_{N}^{1})dP\_{N}^{0}(\omega\_{N}^{2}), |  | (23) |

|  |  |  |
| --- | --- | --- |
|  | μn−1(ω1,…,ωn−1)(A)=∫Ωn0×Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\mu\_{n-1}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A)=\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn1)(A)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn2)(A)]dPn0(ωn1)dPn0(ωn2),n=2,N¯,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2}),\quad n=\overline{2,N}, |  | (24) |

|  |  |  |
| --- | --- | --- |
|  | μ0(A)=∫Ω10×Ω10χΩ1−(ω11)χΩ1+(ω12)α1(ω11;ω12)×\mu\_{0}(A)=\int\limits\_{\Omega\_{1}^{0}\times\Omega\_{1}^{0}}\chi\_{\Omega\_{1}^{-}}(\omega\_{1}^{1})\chi\_{\Omega\_{1}^{+}}(\omega\_{1}^{2})\alpha\_{1}(\omega\_{1}^{1};\omega\_{1}^{2})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | [Δ​S1+​(ω12)V1​(ω11,ω12)​μ1(ω11)​(A)+Δ​S1−​(ω11)V1​(ω11,ω12)​μ1(ω12)​(A)]​d​P10​(ω11)​d​P10​(ω12),delimited-[]Δsuperscriptsubscript𝑆1superscriptsubscript𝜔12subscript𝑉1superscriptsubscript𝜔11superscriptsubscript𝜔12superscriptsubscript𝜇1superscriptsubscript𝜔11𝐴Δsuperscriptsubscript𝑆1superscriptsubscript𝜔11subscript𝑉1superscriptsubscript𝜔11superscriptsubscript𝜔12superscriptsubscript𝜇1superscriptsubscript𝜔12𝐴𝑑superscriptsubscript𝑃10superscriptsubscript𝜔11𝑑superscriptsubscript𝑃10superscriptsubscript𝜔12\displaystyle\left[\frac{\Delta S\_{1}^{+}(\omega\_{1}^{2})}{V\_{1}(\omega\_{1}^{1},\omega\_{1}^{2})}\mu\_{1}^{(\omega\_{1}^{1})}(A)+\frac{\Delta S\_{1}^{-}(\omega\_{1}^{1})}{V\_{1}(\omega\_{1}^{1},\omega\_{1}^{2})}\mu\_{1}^{(\omega\_{1}^{2})}(A)\right]dP\_{1}^{0}(\omega\_{1}^{1})dP\_{1}^{0}(\omega\_{1}^{2}), |  | (25) |

where we put

|  |  |  |  |
| --- | --- | --- | --- |
|  | μN(ω1,…,ωN−1,ωN)​(A)=χA​(ω1,…,ωN−1,ωN),A∈ℱN.formulae-sequencesuperscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴subscriptℱ𝑁\displaystyle\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})}(A)=\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}),\quad A\in{\cal F}\_{N}. |  | (26) |

###### Lemma 2.

Suppose that the conditions of Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") are true.
For the measure μ0​(A),A∈ℱN,

subscript𝜇0𝐴𝐴
subscriptℱ𝑁\mu\_{0}(A),\ A\in{\cal F}\_{N}, constructed by the recurrent relations ([23](#S3.E23 "In 3 Construction of the set of martingale measures.")) - ([25](#S3.E25 "In 3 Construction of the set of martingale measures.")), the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ0​(A)=∫ΩN∏n=1Nψn​(ω1,…,ωn)​χA​(ω1,…,ωN)​∏i=1Nd​Pi0​(ωi)subscript𝜇0𝐴subscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑛1𝑁subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖\displaystyle\mu\_{0}(A)=\int\limits\_{\Omega\_{N}}\prod\limits\_{n=1}^{N}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N})\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i}) |  | (27) |

is true and μ0​(ΩN)=1,subscript𝜇0subscriptΩ𝑁1\mu\_{0}(\Omega\_{N})=1, that is, the measure μ0​(A)subscript𝜇0𝐴\mu\_{0}(A) is a probability measure being equivalent to the measure PN,subscript𝑃𝑁P\_{N}, where we put

|  |  |  |
| --- | --- | --- |
|  | ψn​(ω1,…,ωn)=χΩn−​(ω1,…,ωn−1,ωn)​ψn1​(ω1,…,ωn)+subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛limit-fromsubscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})=\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})+ |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΩn+​(ω1,…,ωn−1,ωn)​ψn2​(ω1,…,ωn),subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛\displaystyle\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n}), |  | (28) |

|  |  |  |
| --- | --- | --- |
|  | ψn1​(ω1,…,ωn−1,ωn)=superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0χΩn+(ω1,…,ωn−1,ωn2)αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn2),(ω1,…,ωn−1)∈Ωn−1,  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{2}),\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (29) |

|  |  |  |
| --- | --- | --- |
|  | ψn2​(ω1,…,ωn−1,ωn)=superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn1),(ω1,…,ωn−1)∈Ωn−1.  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{1}),\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}. |  | (30) |

###### Proof.

Due to Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") conditions, the set of the strictly positive
bounded random values αn​({ω}n1;{ω}n2),subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}), n=1,N¯,𝑛¯

1𝑁n=\overline{1,N}, satisfying the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")), is a non empty set.
We prove Lemma [2](#Thmleme2 "Lemma 2. ‣ 3 Construction of the set of martingale measures.") by induction down.
Let us denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | μN(ω1,…,ωN−1,ωN)​(A)=χA​(ω1,…,ωN).superscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁\displaystyle\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})}(A)=\chi\_{A}(\omega\_{1},\ldots,\omega\_{N}). |  | (31) |

Then,

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0ψN​(ω1,…,ωN−1,ωN)​μN(ω1,…,ωN−1,ωN)​(A)​𝑑PN0​(ωN)=subscriptsuperscriptsubscriptΩ𝑁0subscript𝜓𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁superscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴differential-dsuperscriptsubscript𝑃𝑁0subscript𝜔𝑁absent\int\limits\_{\Omega\_{N}^{0}}\psi\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})}(A)dP\_{N}^{0}(\omega\_{N})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0χΩN−​(ω1,…,ωN−1,ωN)​ψN1​(ω1,…,ωN−1,ωN)​μN(ω1,…,ωN−1,ωN)​(A)​𝑑PN0​(ωN)+limit-fromsubscriptsuperscriptsubscriptΩ𝑁0subscript𝜒superscriptsubscriptΩ𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁superscriptsubscript𝜓𝑁1subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁superscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴differential-dsuperscriptsubscript𝑃𝑁0subscript𝜔𝑁\int\limits\_{\Omega\_{N}^{0}}\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})\psi\_{N}^{1}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})}(A)dP\_{N}^{0}(\omega\_{N})+ |  |

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0χΩN+​(ω1,…,ωN−1,ωN)​ψN2​(ω1,…,ωN−1,ωN)​μN(ω1,…,ωN−1,ωN)​(A)​𝑑PN0​(ωN)=subscriptsuperscriptsubscriptΩ𝑁0subscript𝜒superscriptsubscriptΩ𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁superscriptsubscript𝜓𝑁2subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁superscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴differential-dsuperscriptsubscript𝑃𝑁0subscript𝜔𝑁absent\int\limits\_{\Omega\_{N}^{0}}\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})\psi\_{N}^{2}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})}(A)dP\_{N}^{0}(\omega\_{N})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0χΩN−​(ω1,…,ωN−1,ωN1)​ψN1​(ω1,…,ωN−1,ωN1)​μN(ω1,…,ωN−1,ωN1)​(A)​𝑑PN0​(ωN1)+limit-fromsubscriptsuperscriptsubscriptΩ𝑁0subscript𝜒superscriptsubscriptΩ𝑁subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1superscriptsubscript𝜓𝑁1subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1superscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1𝐴differential-dsuperscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁1\int\limits\_{\Omega\_{N}^{0}}\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\psi\_{N}^{1}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}(A)dP\_{N}^{0}(\omega\_{N}^{1})+ |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN0χΩN+​(ω1,…,ωN−1,ωN2)​ψN2​(ω1,…,ωN−1,ωN2)​μN(ω1,…,ωN−1,ωN2)​(A)​𝑑PN0​(ωN2).subscriptsuperscriptsubscriptΩ𝑁0subscript𝜒superscriptsubscriptΩ𝑁subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2superscriptsubscript𝜓𝑁2subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2superscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴differential-dsuperscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁2\displaystyle\int\limits\_{\Omega\_{N}^{0}}\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\psi\_{N}^{2}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}(A)dP\_{N}^{0}(\omega\_{N}^{2}). |  | (32) |

Substituting ψN1​(ω1,…,ωN−1,ωN1),ψN2​(ω1,…,ωN−1,ωN2)

superscriptsubscript𝜓𝑁1subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1superscriptsubscript𝜓𝑁2subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2\psi\_{N}^{1}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1}),\ \psi\_{N}^{2}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2}) into ([32](#S3.E32 "In Proof. ‣ 3 Construction of the set of martingale measures.")), we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0ψN​(ω1,…,ωN−1,ωN)​μN(ω1,…,ωN−1,ωN)​(A)​𝑑PN0​(ωN)=subscriptsuperscriptsubscriptΩ𝑁0subscript𝜓𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁superscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴differential-dsuperscriptsubscript𝑃𝑁0subscript𝜔𝑁absent\int\limits\_{\Omega\_{N}^{0}}\psi\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})}(A)dP\_{N}^{0}(\omega\_{N})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0×ΩN0χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\int\limits\_{\Omega\_{N}^{0}\times\Omega\_{N}^{0}}\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αN({ω1,…,ωN−1,ωN1};{ω1,…,ωN−1,ωN2})×\alpha\_{N}(\{\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1}\};\{\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)μN(ω1,…,ωN−1,ωN1)(A)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}(A)+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)μN(ω1,…,ωN−1,ωN2)(A)]dPN0(ωN1)dPN0(ωN2)=\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}(A)\right]dP\_{N}^{0}(\omega\_{N}^{1})dP\_{N}^{0}(\omega\_{N}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μN−1(ω1,…,ωN−1)​(A).superscriptsubscript𝜇𝑁1subscript𝜔1…subscript𝜔𝑁1𝐴\displaystyle\mu\_{N-1}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A). |  | (33) |

Suppose that we are proved that

|  |  |  |
| --- | --- | --- |
|  | μn(ω1,…,ωn−1,ωn)​(A)=superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝐴absent\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫∏i=n+1NΩi0∏i=n+1Nψi​(ω1,…,ωi)​χA​(ω1,…,ωN)​∏i=n+1Nd​Pi0​(ωi).subscriptsuperscriptsubscriptproduct𝑖𝑛1𝑁superscriptsubscriptΩ𝑖0superscriptsubscriptproduct𝑖𝑛1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁superscriptsubscriptproduct𝑖𝑛1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖\displaystyle\int\limits\_{\prod\limits\_{i=n+1}^{N}\Omega\_{i}^{0}}\prod\limits\_{i=n+1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N})\prod\limits\_{i=n+1}^{N}dP\_{i}^{0}(\omega\_{i}). |  | (34) |

Let us calculate

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn−1,ωn)​μn(ω1,…,ωn−1,ωn)​(A)​𝑑Pn0​(ωn)=subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝐴differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛absent\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})}(A)dP\_{n}^{0}(\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0χΩn−​(ω1,…,ωn−1,ωn)​ψn1​(ω1,…,ωn−1,ωn)​μn(ω1,…,ωn−1,ωn)​(A)​𝑑Pn0​(ωn)+limit-fromsubscriptsuperscriptsubscriptΩ𝑛0subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝐴differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})}(A)dP\_{n}^{0}(\omega\_{n})+ |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0χΩn+​(ω1,…,ωn−1,ωn)​ψn2​(ω1,…,ωn−1,ωn)​μn(ω1,…,ωn−1,ωn)​(A)​𝑑Pn0​(ωn)=subscriptsuperscriptsubscriptΩ𝑛0subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝐴differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛absent\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})}(A)dP\_{n}^{0}(\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0χΩn−​(ω1,…,ωn−1,ωn1)​ψn1​(ω1,…,ωn−1,ωn1)​μn(ω1,…,ωn−1,ωn1)​(A)​𝑑Pn0​(ωn1)+limit-fromsubscriptsuperscriptsubscriptΩ𝑛0subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1𝐴differential-dsuperscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)dP\_{n}^{0}(\omega\_{n}^{1})+ |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn0χΩn+​(ω1,…,ωn−1,ωn2)​ψn2​(ω1,…,ωn−1,ωn2)​μn(ω1,…,ωn−1,ωn2)​(A)​𝑑Pn0​(ωn2).subscriptsuperscriptsubscriptΩ𝑛0subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝐴differential-dsuperscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2\displaystyle\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)dP\_{n}^{0}(\omega\_{n}^{2}). |  | (35) |

Substituting ψn1​(ω1,…,ωn−1,ωn1),ψn2​(ω1,…,ωn−1,ωn2)

superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}),\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}) into ([35](#S3.E35 "In Proof. ‣ 3 Construction of the set of martingale measures.")), we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn−1,ωn)​μn(ω1,…,ωn−1,ωn)​(A)​𝑑Pn0​(ωn)=subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝐴differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛absent\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})}(A)dP\_{n}^{0}(\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn1)(A)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn2)(A)]dPn0(ωn1)dPn0(ωn2).\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2}). |  | (36) |

From the recurrent relations ([23](#S3.E23 "In 3 Construction of the set of martingale measures.")) - ([25](#S3.E25 "In 3 Construction of the set of martingale measures.")), we have

|  |  |  |
| --- | --- | --- |
|  | μn−1(ω1,…,ωn−1)(A)=∫Ωn0×Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\mu\_{n-1}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A)=\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn1)(A)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn2)(A)]dPn0(ωn1)dPn0(ωn2),n=1,N¯.\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2}),\quad n=\overline{1,N}. |  | (37) |

From the last equality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn−1(ω1,…,ωn−1)=∫Ωn0ψn​(ω1,…,ωn−1,ωn)​μn(ω1,…,ωn−1,ωn)​(A)​𝑑Pn0​(ωn),n=1,N¯.formulae-sequencesuperscriptsubscript𝜇𝑛1subscript𝜔1…subscript𝜔𝑛1subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝐴differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛𝑛¯  1𝑁\displaystyle\mu\_{n-1}^{(\omega\_{1},\ldots,\omega\_{n-1})}=\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})}(A)dP\_{n}^{0}(\omega\_{n}),\quad n=\overline{1,N}. |  | (38) |

Substituting into ([38](#S3.E38 "In Proof. ‣ 3 Construction of the set of martingale measures.")) the induction supposition ([34](#S3.E34 "In Proof. ‣ 3 Construction of the set of martingale measures.")),
we obtain

|  |  |  |
| --- | --- | --- |
|  | μn−1(ω1,…,ωn−1)​(A)=superscriptsubscript𝜇𝑛1subscript𝜔1…subscript𝜔𝑛1𝐴absent\mu\_{n-1}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫∏i=nNΩi0∏i=nNψi​(ω1,…,ωi)​χA​(ω1,…,ωN)​∏i=nNd​Pi0​(ωi).subscriptsuperscriptsubscriptproduct𝑖𝑛𝑁superscriptsubscriptΩ𝑖0superscriptsubscriptproduct𝑖𝑛𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁superscriptsubscriptproduct𝑖𝑛𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖\displaystyle\int\limits\_{\prod\limits\_{i=n}^{N}\Omega\_{i}^{0}}\prod\limits\_{i=n}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N})\prod\limits\_{i=n}^{N}dP\_{i}^{0}(\omega\_{i}). |  | (39) |

To prove that μ0​(ΩN)=1,subscript𝜇0subscriptΩ𝑁1\mu\_{0}(\Omega\_{N})=1, let us prove the equality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​𝑑Pn0​(ωn)=1,(ω1,…,ωn−1)∈Ωn−1,n=1,N¯.formulae-sequencesubscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛1formulae-sequencesubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})=1,\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1},\quad\quad n=\overline{1,N}. |  | (40) |

We have

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​𝑑Pn0​(ωn)=subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛absent\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)]dPn0(ωn1)dPn0(ωn2)=\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})​d​Pn0​(ωn1)​d​Pn0​(ωn2)=1.subscript𝛼𝑛  subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2 𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛21\displaystyle\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})=1. |  | (41) |

The last equality follows from the fact that the set of random values αn​({ω1}n1;{ω1}n2),subscript𝛼𝑛

superscriptsubscriptsubscript𝜔1𝑛1superscriptsubscriptsubscript𝜔1𝑛2\alpha\_{n}(\{\omega\_{1}\}\_{n}^{1};\{\omega\_{1}\}\_{n}^{2}), n=1,N¯,𝑛¯

1𝑁\ n=\overline{1,N}, satisfies the condition ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")).
The equalities ([40](#S3.E40 "In Proof. ‣ 3 Construction of the set of martingale measures.")) proves that every measure ([27](#S3.E27 "In Lemma 2. ‣ 3 Construction of the set of martingale measures.")), defined by the set of random values αn​({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), n=1,N¯,𝑛¯

1𝑁n=\overline{1,N}, satisfying the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")), ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")), is a probability measure being equivalent to the measure PN.subscript𝑃𝑁P\_{N}.

This proves Lemma [2](#Thmleme2 "Lemma 2. ‣ 3 Construction of the set of martingale measures.")
∎

###### Note 1.

Due to the equality ([40](#S3.E40 "In Proof. ‣ 3 Construction of the set of martingale measures.")), the contraction of measure μ0​(A),A∈ℱN,

subscript𝜇0𝐴𝐴
subscriptℱ𝑁\mu\_{0}(A),A\in{\cal F}\_{N}, on the σ𝜎\sigma-algebra ℱnsubscriptℱ𝑛{\cal F}\_{n} of filtration we denote by μ0n.superscriptsubscript𝜇0𝑛\mu\_{0}^{n}. If A𝐴A belongs to the σ𝜎\sigma-algebra ℱnsubscriptℱ𝑛{\cal F}\_{n} of filtration, then A=B×∏i=n+1NΩi0,𝐴𝐵superscriptsubscriptproduct𝑖𝑛1𝑁superscriptsubscriptΩ𝑖0A=B\times\prod\limits\_{i=n+1}^{N}\Omega\_{i}^{0}, where B𝐵B belongs to the σ𝜎\sigma-algebra ℱnsubscriptℱ𝑛{\cal F}\_{n} of the measurable space {Ωn,ℱn},subscriptΩ𝑛subscriptℱ𝑛\{\Omega\_{n},{\cal F}\_{n}\}, therefore, for this contraction we obtain the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ0n​(A)=∫Ωn∏i=1nψi​(ω1,…,ωi)​χB​(ω1,…,ωn)​∏i=1nd​Pi0​(ωi),B∈ℱn.formulae-sequencesuperscriptsubscript𝜇0𝑛𝐴subscriptsubscriptΩ𝑛superscriptsubscriptproduct𝑖1𝑛subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝜒𝐵subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖𝐵subscriptℱ𝑛\displaystyle\mu\_{0}^{n}(A)=\int\limits\_{\Omega\_{n}}\prod\limits\_{i=1}^{n}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\chi\_{B}(\omega\_{1},\ldots,\omega\_{n})\prod\limits\_{i=1}^{n}dP\_{i}^{0}(\omega\_{i}),\quad B\in{\cal F}\_{n}. |  | (42) |

Further, we also use the probability spaces {Ωn,ℱn,μ0n},n=1,N¯,

subscriptΩ𝑛subscriptℱ𝑛superscriptsubscript𝜇0𝑛𝑛
¯

1𝑁\{\Omega\_{n},{\cal F}\_{n},\mu\_{0}^{n}\},\ n=\overline{1,N}, where under the measure μ0n​(B),B∈ℱn,

superscriptsubscript𝜇0𝑛𝐵𝐵
subscriptℱ𝑛\mu\_{0}^{n}(B),B\in{\cal F}\_{n}, we understand the measure, given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ0n​(B)=∫Ωn∏i=1nψi​(ω1,…,ωi)​χB​(ω1,…,ωn)​∏i=1nd​Pi0​(ωi),B∈ℱn.formulae-sequencesuperscriptsubscript𝜇0𝑛𝐵subscriptsubscriptΩ𝑛superscriptsubscriptproduct𝑖1𝑛subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝜒𝐵subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖𝐵subscriptℱ𝑛\displaystyle\mu\_{0}^{n}(B)=\int\limits\_{\Omega\_{n}}\prod\limits\_{i=1}^{n}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\chi\_{B}(\omega\_{1},\ldots,\omega\_{n})\prod\limits\_{i=1}^{n}dP\_{i}^{0}(\omega\_{i}),\quad B\in{\cal F}\_{n}. |  | (43) |

###### Note 2.

Assume that for αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}), constructed in Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures."), the inequalities

|  |  |  |
| --- | --- | --- |
|  | 0<cn≤αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})≤Cn<∞,0subscript𝑐𝑛subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2subscript𝐶𝑛0<c\_{n}\leq\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\leq C\_{n}<\infty, |  |

are true. Suppose that the conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn)≤Bn<∞,n=1,N¯,formulae-sequenceΔsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛subscript𝐵𝑛𝑛¯  1𝑁\displaystyle\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\leq B\_{n}<\infty,\quad n=\overline{1,N}, |  | (44) |

are valid, where cn,Cn,Bn

subscript𝑐𝑛subscript𝐶𝑛subscript𝐵𝑛c\_{n},\ C\_{n},\ B\_{n} are constant,
then
the set of equivalent measures to the measure PN,subscript𝑃𝑁P\_{N}, described in Lemma [2](#Thmleme2 "Lemma 2. ‣ 3 Construction of the set of martingale measures."), is nonempty one.

###### Proof.

Due to Lemma [2](#Thmleme2 "Lemma 2. ‣ 3 Construction of the set of martingale measures.") conditions, the equality ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) is true.
Further,

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn−(ω11,…,ωn−11,ωn1)χΩn+(ω12,…,ωn−12,ωn2)×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})×\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)​Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn1)​d​Pn0​(ωn2)≤Bn,Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2subscript𝐵𝑛\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})\leq B\_{n}, |  |

|  |  |  |
| --- | --- | --- |
|  | ({ω11,…,ωn−11};{ω12,…,ωn−12})∈Ωn−1×Ωn−1,(ω1,…,ωn−1)∈Ωn−1,formulae-sequence  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12 subscriptΩ𝑛1subscriptΩ𝑛1subscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2}\})\in\Omega\_{n-1}\times\Omega\_{n-1},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn−(ω11,…,ωn−11,ωn1)χΩn+(ω12,…,ωn−12,ωn2)×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})​d​Pn0​(ωn1)​d​Pn0​(ωn2)=1,subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2 𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛21\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})=1, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({ω11,…,ωn−11};{ω12,…,ωn−12})∈Ωn−1×Ωn−1.  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12 subscriptΩ𝑛1subscriptΩ𝑛1\displaystyle(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2}\})\in\Omega\_{n-1}\times\Omega\_{n-1}. |  | (45) |

The last inequality and the equality ([45](#S3.E45 "In Proof. ‣ 3 Construction of the set of martingale measures.")) means that the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")) are satisfied.
Note [2](#Thmnote12 "Note 2. ‣ 3 Construction of the set of martingale measures.") is proved.
∎

For the nonnegative random value αn​({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), given
on the measurable space {Ωn−×Ωn+,ℱn−×ℱn+},superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛superscriptsubscriptℱ𝑛superscriptsubscriptℱ𝑛\{\Omega\_{n}^{-}\times\Omega\_{n}^{+},{\cal F}\_{n}^{-}\times{\cal F}\_{n}^{+}\}, ℱn−=ℱn∩Ωn−,superscriptsubscriptℱ𝑛subscriptℱ𝑛superscriptsubscriptΩ𝑛{\cal F}\_{n}^{-}={\cal F}\_{n}\cap\Omega\_{n}^{-}, ℱn+=ℱn∩Ωn+,n=1,N¯,formulae-sequencesuperscriptsubscriptℱ𝑛subscriptℱ𝑛superscriptsubscriptΩ𝑛𝑛¯

1𝑁{\cal F}\_{n}^{+}={\cal F}\_{n}\cap\Omega\_{n}^{+},n=\overline{1,N},
let us define the integral for the nonnegative random value fN​(ω1,…,ωN)subscript𝑓𝑁subscript𝜔1…subscript𝜔𝑁f\_{N}(\omega\_{1},\ldots,\omega\_{N}) relative to the measure μ0​(A)subscript𝜇0𝐴\mu\_{0}(A) using the recurrent relations

|  |  |  |
| --- | --- | --- |
|  | μn−1fN​(ω1,…,ωn−1)=superscriptsubscript𝜇𝑛1subscript𝑓𝑁subscript𝜔1…subscript𝜔𝑛1absent\mu\_{n-1}^{f\_{N}}(\omega\_{1},\ldots,\omega\_{n-1})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μnfN(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{f\_{N}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μnfN(ω1,…,ωn−1,ωn2)]dPn0(ωn1)dPn0(ωn2),n=1,N¯,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{f\_{N}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2}),\quad n=\overline{1,N}, |  | (46) |

|  |  |  |
| --- | --- | --- |
|  | μN−1fN(ω1,…,ωN−1)=∫ΩN0×ΩN0χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\mu\_{N-1}^{f\_{N}}(\omega\_{1},\ldots,\omega\_{N-1})=\int\limits\_{\Omega\_{N}^{0}\times\Omega\_{N}^{0}}\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αN({ω1,…,ωN−1,ωN1};{ω1,…,ωN−1,ωN2})×\alpha\_{N}(\{\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1}\};\{\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)fN(ω1,…,ωN−1,ωN1)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}f\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)fN(ω1,…,ωN−1,ωN2)]dPN0(ωN1)dPN0(ωN2).\displaystyle\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}f\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\right]dP\_{N}^{0}(\omega\_{N}^{1})dP\_{N}^{0}(\omega\_{N}^{2}). |  | (47) |

From the formula ([27](#S3.E27 "In Lemma 2. ‣ 3 Construction of the set of martingale measures.")) of Lemma [2](#Thmleme2 "Lemma 2. ‣ 3 Construction of the set of martingale measures."), it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eμ0​fN=∫ΩN∏n=1Nψn​(ω1,…,ωn)​fN​(ω1,…,ωN−1,ωN)​∏i=1Nd​Pi0​(ωi)superscript𝐸subscript𝜇0subscript𝑓𝑁subscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑛1𝑁subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑓𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖\displaystyle E^{\mu\_{0}}f\_{N}=\int\limits\_{\Omega\_{N}}\prod\limits\_{n=1}^{N}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})f\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i}) |  | (48) |

for every nonnegative ℱNsubscriptℱ𝑁{\cal F}\_{N}-measurable random value fN​(ω1,…,ωN−1,ωN).subscript𝑓𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁f\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}).

###### Theorem 1.

Suppose that the conditions of Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.")
are true.
Then, the set of nonnegative random values αn​({ω}n1;{ω}n2),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}),n=\overline{1,N}, satisfying the conditions

|  |  |  |
| --- | --- | --- |
|  | Eμ0​|Δ​Sn​(ω1,…,ωn−1,ωn)|=superscript𝐸subscript𝜇0Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absentE^{\mu\_{0}}|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN∏i=1Nψi​(ω1,…,ωi)​|Δ​Sn​(ω1,…,ωn−1,ωn)|​∏i=1Nd​Pi0​(ωi)<∞,n=1,N¯,formulae-sequencesubscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{N}}\prod\limits\_{i=1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i})<\infty,\quad n=\overline{1,N}, |  | (49) |

is a nonempty one and the convex linear span of the set of measures ([27](#S3.E27 "In Lemma 2. ‣ 3 Construction of the set of martingale measures.")), defined by the random values αn​({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), n=1,N¯,𝑛¯

1𝑁n=\overline{1,N}, satisfying the conditions ([49](#S3.E49 "In Theorem 1. ‣ 3 Construction of the set of martingale measures.")), is a set of martingale measures being equivalent to the measure PN.subscript𝑃𝑁P\_{N}.

###### Proof.

Taking into account the equality ([40](#S3.E40 "In Proof. ‣ 3 Construction of the set of martingale measures.")), the conditions ([49](#S3.E49 "In Theorem 1. ‣ 3 Construction of the set of martingale measures.")) can be written in the form

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN∏i=1Nψi​(ω1,…,ωi)​|Δ​Sn​(ω1,…,ωn−1,ωn)|​∏i=1Nd​Pi0​(ωi)=subscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖absent\int\limits\_{\Omega\_{N}}\prod\limits\_{i=1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn∏i=1nψi​(ω1,…,ωi)​|Δ​Sn​(ω1,…,ωn−1,ωn)|​∏i=1nd​Pi0​(ωi)=subscriptsubscriptΩ𝑛superscriptsubscriptproduct𝑖1𝑛subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖absent\int\limits\_{\Omega\_{n}}\prod\limits\_{i=1}^{n}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|\prod\limits\_{i=1}^{n}dP\_{i}^{0}(\omega\_{i})= |  |

|  |  |  |
| --- | --- | --- |
|  | 2∫Ωn−1∏i=1n−1ψi(ω1,…,ωi)∫Ωn0∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×2\int\limits\_{\Omega\_{n-1}}\prod\limits\_{i=1}^{n-1}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)​Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)×\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Pn0​(ωn1)​d​Pn0​(ωn2)​∏i=1n−1d​Pi0​(ωi),n=1,N¯.  𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2superscriptsubscriptproduct𝑖1𝑛1𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖𝑛 ¯  1𝑁\displaystyle dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})\prod\limits\_{i=1}^{n-1}dP\_{i}^{0}(\omega\_{i}),\quad n=\overline{1,N}. |  | (50) |

Since the conditions of Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") are true, then the the set of bounded random values αn​({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), n=1,N¯,𝑛¯

1𝑁n=\overline{1,N}, constructed in Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures."),
satisfy the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")).

From the equality ([50](#S3.E50 "In Proof. ‣ 3 Construction of the set of martingale measures.")) for the set of bounded random values αn​({ω}n1;{ω}n2),subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}), n=1,N¯,𝑛¯

1𝑁n=\overline{1,N}, satisfying the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")), we obtain the inequality

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN∏i=1Nψi​(ω1,…,ωi)​|Δ​Sn​(ω1,…,ωn−1,ωn)|​∏i=1Nd​Pi0​(ωi)≤subscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖absent\int\limits\_{\Omega\_{N}}\prod\limits\_{i=1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i})\leq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​∫ΩNΔ​Sn−​(ω1,…,ωn−1,ωn1)​𝑑PN<∞,n=1,N¯,formulae-sequence𝐶subscriptsubscriptΩ𝑁Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1differential-dsubscript𝑃𝑁𝑛¯  1𝑁\displaystyle C\int\limits\_{\Omega\_{N}}\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})dP\_{N}<\infty,\quad n=\overline{1,N}, |  | (51) |

for a certain constant 0<C<∞.0𝐶0<C<\infty. This proves that the set of nonnegative random values αn​({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), n=1,N¯,𝑛¯

1𝑁n=\overline{1,N}, satisfying the conditions ([49](#S3.E49 "In Theorem 1. ‣ 3 Construction of the set of martingale measures.")), is a non empty set.

Let us prove that

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​Δ​Sn​(ω1,…,ωn)​𝑑Pn0​(ωn)=0,subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛0\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})=0, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ω1,…,ωn−1)∈Ωn−1,n=1,N¯.formulae-sequencesubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1𝑛¯  1𝑁\displaystyle(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1},\quad n=\overline{1,N}. |  | (52) |

Really,

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​Δ​Sn​(ω1,…,ωn)​𝑑Pn0​(ωn)=subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛absent\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [−Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)ΔSn−(ω1,…,ωn−1,ωn1)+\left[-\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)ΔSn+(ω1,…,ωn−1,ωn2)]dPn0(ωn1)dPn0(ωn2)=0,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})=0, |  | (53) |

due to the condition ([15](#S3.E15 "In 3 Construction of the set of martingale measures.")).

To complete the proof of Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures."), let A𝐴A belongs to the filtration ℱn−1,subscriptℱ𝑛1{\cal F}\_{n-1}, then A=B×∏i=nNΩi0,𝐴𝐵superscriptsubscriptproduct𝑖𝑛𝑁superscriptsubscriptΩ𝑖0A=B\times\prod\limits\_{i=n}^{N}\Omega\_{i}^{0}, where B𝐵B belongs to the σ𝜎\sigma-algebra ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1} of the measurable space {Ωn−1,ℱn−1}.subscriptΩ𝑛1subscriptℱ𝑛1\{\Omega\_{n-1},{\cal F}\_{n-1}\}. Taking into account the equality ([41](#S3.E41 "In Proof. ‣ 3 Construction of the set of martingale measures.")), ([53](#S3.E53 "In Proof. ‣ 3 Construction of the set of martingale measures.")), we have, due to Foubini theorem,

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN∏i=1Nψi​(ω1,…,ωi)​χA​(ω1,…,ωN)​Δ​Sn​(ω1,…,ωn)​∏i=1Nd​Pi0​(ωi)=subscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖absent\int\limits\_{\Omega\_{N}}\prod\limits\_{i=1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn∏i=1nψi​(ω1,…,ωi)​χB​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn)​∏i=1nd​Pi0​(ωi)=subscriptsubscriptΩ𝑛superscriptsubscriptproduct𝑖1𝑛subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝜒𝐵subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖absent\int\limits\_{\Omega\_{n}}\prod\limits\_{i=1}^{n}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\chi\_{B}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})\prod\limits\_{i=1}^{n}dP\_{i}^{0}(\omega\_{i})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn−1∏i=1n−1ψi(ω1,…,ωi)χB(ω1,…,ωn−1)∏i=1n−1dPi0(ωi)×\int\limits\_{\Omega\_{n-1}}\prod\limits\_{i=1}^{n-1}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})\chi\_{B}(\omega\_{1},\ldots,\omega\_{n-1})\prod\limits\_{i=1}^{n-1}dP\_{i}^{0}(\omega\_{i})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn0ψi​(ω1,…,ωn)​Δ​Sn​(ω1,…,ωn)​𝑑Pn0​(ωn)=0.subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑛Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛0\displaystyle\int\limits\_{\Omega\_{n}^{0}}\psi\_{i}(\omega\_{1},\ldots,\omega\_{n})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})=0. |  | (54) |

The last means that Eμ0​{Sn​(ω1,…,ωn)|ℱn−1}=Sn−1​(ω1,…,ωn−1).superscript𝐸subscript𝜇0conditional-setsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛subscriptℱ𝑛1subscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1E^{\mu\_{0}}\{S\_{n}(\omega\_{1},\ldots,\omega\_{n})|{\cal F}\_{n-1}\}=S\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}).
Since every measure, belonging to the convex linear span of the measures considered above, is a finite sum of such measures, then it is a martingale measure being equivalent to the measure PN.subscript𝑃𝑁P\_{N}.
Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures.") is proved.
∎

Our aim is to describe this convex span of martingale measures in particular cases.

## 4 Inequalities for the nonnegative random values.

In this section, we prove some inequalities, which will be very useful for to prove optional decomposition for super-martingale relative to all martingale measures.
First, we prove an integral inequality for a nonnegative random variable under the fulfillment of the inequality for this nonnegative random variable with respect to the constructed family of measures μ0​(A).subscript𝜇0𝐴\mu\_{0}(A). Further, using this integral inequality for the non-negative random variable, a pointwise system of inequalities is obtained for this non-negative random variable for a particular case. After that, the pointwise system of inequalities is obtained for the non-negative random variable in the general case. Then, using the resulting pointwise system of inequalities, the inequality is established for this non-negative random variable whose right-hand side is such that its conditional mathematical expectation is equal to one.

###### Definition 1.

Let {Ω1,ℱ1}subscriptΩ1subscriptℱ1\{\Omega\_{1},{\cal F}\_{1}\} be a measurable space. The decomposition An,k,n,k=1,∞¯,

subscript𝐴

𝑛𝑘𝑛𝑘
¯

1A\_{n,k},\ n,k=\overline{1,\infty}, of the space Ω1subscriptΩ1\Omega\_{1} we call exhaustive one, if the following conditions are valid:
  
1) An,k∈ℱ1,subscript𝐴

𝑛𝑘subscriptℱ1A\_{n,k}\in{\cal F}\_{1},  An,k∩An,s=∅,k≠s,formulae-sequencesubscript𝐴

𝑛𝑘subscript𝐴

𝑛𝑠𝑘𝑠A\_{n,k}\cap A\_{n,s}=\emptyset,\ k\neq s,  ⋃k=1∞An,k=Ω1,n=1,∞¯;formulae-sequencesuperscriptsubscript𝑘1subscript𝐴

𝑛𝑘subscriptΩ1𝑛¯

1\bigcup\limits\_{k=1}^{\infty}A\_{n,k}=\Omega\_{1},\ n=\overline{1,\infty};
  
2) the (n+1)𝑛1(n+1)-th decomposition is a sub-decomposition of the n𝑛n-th one, that is, for every j,𝑗j, An+1,j⊆An,ksubscript𝐴

𝑛1𝑗subscript𝐴

𝑛𝑘A\_{n+1,j}\subseteq A\_{n,k} for a certain k=k​(j);𝑘𝑘𝑗k=k(j);
  
3) the minimal σ𝜎\sigma-algebra containing all An,k,n,k=1,∞¯,

subscript𝐴

𝑛𝑘𝑛𝑘
¯

1A\_{n,k},\ n,k=\overline{1,\infty}, coincides with ℱ1.subscriptℱ1{\cal F}\_{1}.

###### Lemma 3.

Let {Ω1,ℱ1}subscriptΩ1subscriptℱ1\{\Omega\_{1},{\cal F}\_{1}\} be a measurable space with a complete separable metric space Ω1subscriptΩ1\Omega\_{1} and Borel σ𝜎\sigma-algebra ℱ1subscriptℱ1{\cal F}\_{1} on it. Then,
{Ω1,ℱ1}subscriptΩ1subscriptℱ1\{\Omega\_{1},{\cal F}\_{1}\} has an exhaustive decomposition.

The proof of Lemma [3](#Thmleme3 "Lemma 3. ‣ 4 Inequalities for the nonnegative random values.") see, for example, in [[15](#bib.bib15)],
[[16](#bib.bib16)].

For the proof of integral inequalities,
we cannot require the fulfillment for the random values αn​({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), n=1,N¯,𝑛¯

1𝑁n=\overline{1,N}, the condition ([15](#S3.E15 "In 3 Construction of the set of martingale measures.")) in the Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values.").

###### Lemma 4.

Suppose that Ωn0superscriptsubscriptΩ𝑛0\Omega\_{n}^{0} is a complete separable metric space,
ℱn0superscriptsubscriptℱ𝑛0{\cal F}\_{n}^{0} is a corresponding Borel σ𝜎\sigma-algebra on Ωn0,n=1,N¯,

superscriptsubscriptΩ𝑛0𝑛
¯

1𝑁\Omega\_{n}^{0},\ n=\overline{1,N}, and the conditions of Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") are valid.
If, on the probability space
{Ωn−1,ℱn−1,μ0n−1},subscriptΩ𝑛1subscriptℱ𝑛1superscriptsubscript𝜇0𝑛1\{\Omega\_{n-1},{\cal F}\_{n-1},\mu\_{0}^{n-1}\}, for each B∈ℱn−1,𝐵subscriptℱ𝑛1B\in{\cal F}\_{n-1}, μ0n−1​(B)>0,superscriptsubscript𝜇0𝑛1𝐵0\mu\_{0}^{n-1}(B)>0, the nonnegative random value fn​(ω1,…,ωn−1,ωn)subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}) satisfies
the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1μ0n−1​(B)​∫B∫Ωn0∏i=1nψi​(ω1,…,ωi)​fn​(ω1,…,ωn)​∏i=1nd​Pi0​(ωi)≤1,B∈ℱn−1,formulae-sequence1superscriptsubscript𝜇0𝑛1𝐵subscript𝐵subscriptsuperscriptsubscriptΩ𝑛0superscriptsubscriptproduct𝑖1𝑛subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖1𝐵subscriptℱ𝑛1\displaystyle\frac{1}{\mu\_{0}^{n-1}(B)}\int\limits\_{B}\int\limits\_{\Omega\_{n}^{0}}\prod\limits\_{i=1}^{n}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})f\_{n}(\omega\_{1},\ldots,\omega\_{n})\prod\limits\_{i=1}^{n}dP\_{i}^{0}(\omega\_{i})\leq 1,\quad B\in{\cal F}\_{n-1}, |  | (55) |

then the inequality

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​fn​(ω1,…,ωn)​𝑑Pn0​(ωn)≤1,subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛1\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})f\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})\leq 1, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ω1,…,ωn−1}∈Ωn−1,n=1,N¯,formulae-sequencesubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1𝑛¯  1𝑁\displaystyle\{\omega\_{1},\ldots,\omega\_{n-1}\}\in\Omega\_{n-1},\ n=\overline{1,N}, |  | (56) |

is true almost everywhere relative to the measure Pn−1.subscript𝑃𝑛1P\_{n-1}.

###### Proof.

The metric space Ωn−1subscriptΩ𝑛1\Omega\_{n-1} is a complete separable metric space with the metric ρ​(x,y)=∑i=1n−1ρi​(xi,yi),𝜌𝑥𝑦superscriptsubscript𝑖1𝑛1subscript𝜌𝑖subscript𝑥𝑖subscript𝑦𝑖\rho(x,y)=\sum\limits\_{i=1}^{n-1}\rho\_{i}(x\_{i},y\_{i}), where x=(x1,…,xn−1),y=(y1,…,yn−1)∈Ωn−1,formulae-sequence𝑥subscript𝑥1…subscript𝑥𝑛1𝑦subscript𝑦1…subscript𝑦𝑛1subscriptΩ𝑛1x=(x\_{1},\ldots,x\_{n-1}),y=(y\_{1},\ldots,y\_{n-1})\in\Omega\_{n-1},  (xi,yi)∈Ωi0,subscript𝑥𝑖subscript𝑦𝑖superscriptsubscriptΩ𝑖0\ (x\_{i},y\_{i})\in\Omega\_{i}^{0},   ρi​(xi,yi)subscript𝜌𝑖subscript𝑥𝑖subscript𝑦𝑖\rho\_{i}(x\_{i},y\_{i}) is a metric in Ωi0.superscriptsubscriptΩ𝑖0\Omega\_{i}^{0}. This means that the metric space Ωn−1subscriptΩ𝑛1\Omega\_{n-1} has an exhaustive decomposition{Bm​k}m,k=1∞.superscriptsubscriptsubscript𝐵𝑚𝑘

𝑚𝑘
1\{B\_{mk}\}\_{m,k=1}^{\infty}. Suppose that (ω1,…,ωn−1)∈Bm,ksubscript𝜔1…subscript𝜔𝑛1subscript𝐵

𝑚𝑘(\omega\_{1},\ldots,\omega\_{n-1})\in B\_{m,k} for a certain k,𝑘k, depending on m,𝑚m, and there exists an infinite number of m𝑚m for which μ0n−1​(Bm,k)>0.superscriptsubscript𝜇0𝑛1subscript𝐵

𝑚𝑘0\mu\_{0}^{n-1}(B\_{m,k})>0.
On the probability space
{Ωn−1,ℱn−1,μ0n−1},subscriptΩ𝑛1subscriptℱ𝑛1superscriptsubscript𝜇0𝑛1\{\Omega\_{n-1},{\cal F}\_{n-1},\mu\_{0}^{n-1}\}, for every integrable finite valued random value φn−1​(ω1,…,ωn−1)subscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) the sequence
Eμ0n−1​{φn−1​(ω1,…,ωn−1)|ℱ¯m}superscript𝐸superscriptsubscript𝜇0𝑛1conditional-setsubscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1subscript¯ℱ𝑚E^{\mu\_{0}^{n-1}}\{\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})|\bar{\cal F}\_{m}\} converges to φn−1​(ω1,…,ωn−1)subscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) with probability one, as m→∞,→𝑚m\to\infty, since it is a regular martingale. Here, we denoted ℱ¯msubscript¯ℱ𝑚\bar{\cal F}\_{m} the σ𝜎\sigma-algebra, generated by the sets Bm,k,k=1,∞¯.

subscript𝐵

𝑚𝑘𝑘
¯

1B\_{m,k},k=\overline{1,\infty}.

It is evident that for those Bm,k,subscript𝐵

𝑚𝑘B\_{m,k}, for which μ0n−1​(Bm,k)≠0,superscriptsubscript𝜇0𝑛1subscript𝐵

𝑚𝑘0\mu\_{0}^{n-1}(B\_{m,k})\neq 0,

|  |  |  |
| --- | --- | --- |
|  | Eμ0n−1​{φn−1​(ω1,…,ωn)|ℱ¯m}=superscript𝐸superscriptsubscript𝜇0𝑛1conditional-setsubscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛subscript¯ℱ𝑚absentE^{\mu\_{0}^{n-1}}\{\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n})|\bar{\cal F}\_{m}\}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Bm,kφn−1​(ω1,…,ωn−1)​𝑑μ0n−1μ0n−1​(Bm,k),(ω1,…,ωn)∈Bm,k.  subscriptsubscript𝐵  𝑚𝑘subscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1differential-dsuperscriptsubscript𝜇0𝑛1superscriptsubscript𝜇0𝑛1subscript𝐵  𝑚𝑘subscript𝜔1…subscript𝜔𝑛 subscript𝐵  𝑚𝑘\displaystyle\frac{\int\limits\_{B\_{m,k}}\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})d\mu\_{0}^{n-1}}{\mu\_{0}^{n-1}(B\_{m,k})},\quad(\omega\_{1},\ldots,\omega\_{n})\in B\_{m,k}. |  | (57) |

Denote Am=Am​(ω1,…,ωn−1)subscript𝐴𝑚subscript𝐴𝑚subscript𝜔1…subscript𝜔𝑛1A\_{m}=A\_{m}(\omega\_{1},\ldots,\omega\_{n-1}) those sets Bm,ksubscript𝐵

𝑚𝑘B\_{m,k} for which (ω1,…,ωn)∈Bm,ksubscript𝜔1…subscript𝜔𝑛subscript𝐵

𝑚𝑘(\omega\_{1},\ldots,\omega\_{n})\in B\_{m,k} for a certain k,𝑘k, depending on m,𝑚m, and μ0n−1​(Am)>0superscriptsubscript𝜇0𝑛1subscript𝐴𝑚0\mu\_{0}^{n-1}(A\_{m})>0. Then, for every integrable finite valued φn−1​(ω1,…,ωn−1)subscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})

|  |  |  |  |
| --- | --- | --- | --- |
|  | limm→∞∫Amφn−1​(ω1,…,ωn−1)​𝑑μ0n−1μ0n−1​(Am)=φn−1​(ω1,…,ωn−1)subscript→𝑚subscriptsubscript𝐴𝑚subscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1differential-dsuperscriptsubscript𝜇0𝑛1superscriptsubscript𝜇0𝑛1subscript𝐴𝑚subscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1\displaystyle\lim\limits\_{m\to\infty}\frac{\int\limits\_{A\_{m}}\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})d\mu\_{0}^{n-1}}{\mu\_{0}^{n-1}(A\_{m})}=\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) |  | (58) |

almost everywhere relative to the measure μ0n−1.superscriptsubscript𝜇0𝑛1\mu\_{0}^{n-1}.
If to put

|  |  |  |
| --- | --- | --- |
|  | φn−1​(ω1,…,ωn−1)=subscript𝜑𝑛1subscript𝜔1…subscript𝜔𝑛1absent\varphi\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​fn​(ω1,…,ωn)​𝑑Pn0​(ωn),(ω1,…,ωn−1)∈Ωn−1,  subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})f\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n}),\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (59) |

then we obtain the proof of Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values.").
∎

In Theorem [2](#Thmte2 "Theorem 2. ‣ 4 Inequalities for the nonnegative random values."), we assume that for Δ​Sn​(ω1,…,ωn−1,ωn),n=1,N¯,

Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝑛
¯

1𝑁\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}),\ n=\overline{1,N}, the representation

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn​(ω1,…,ωn−1,ωn)=Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | Sn−1​(ω1,…,ωn−1)​an​(ω1,…,ωn−1,ωn)​ηn​(ωn)=subscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛subscript𝜂𝑛subscript𝜔𝑛absentS\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\eta\_{n}(\omega\_{n})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | dn​(ω1,…,ωn−1,ωn)​ηn​(ωn),n=1,N¯,S0>0,formulae-sequence  subscript𝑑𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛subscript𝜂𝑛subscript𝜔𝑛𝑛 ¯  1𝑁subscript𝑆00\displaystyle d\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\eta\_{n}(\omega\_{n}),\quad n=\overline{1,N},\quad S\_{0}>0, |  | (60) |

is true, where the random values
dn​(ω1,…,ωn−1,ωn),subscript𝑑𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛d\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}),
an​(ω1,…,ωn−1,ωn),subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛a\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}), ηn​(ωn),subscript𝜂𝑛subscript𝜔𝑛\eta\_{n}(\omega\_{n}), n=1,N¯,𝑛¯

1𝑁\ n=\overline{1,N}, given on the probability space {Ωn,ℱn,Pn},subscriptΩ𝑛subscriptℱ𝑛subscript𝑃𝑛\{\Omega\_{n},{\cal F}\_{n},P\_{n}\}, satisfy the conditions

|  |  |  |
| --- | --- | --- |
|  | 0<an​(ω1,…,ωn−1,ωn)≤1,1+an​(ω1,…,ωn−1,ωn)​ηn​(ωn)>0,formulae-sequence0subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛11subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛subscript𝜂𝑛subscript𝜔𝑛00<a\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\leq 1,\quad 1+a\_{n}(\omega\_{1},\quad\ldots,\omega\_{n-1},\omega\_{n})\eta\_{n}(\omega\_{n})>0, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | dn​(ω1,…,ωn−1,ωn)>0,Pn0​(ηn​(ωn)>0)>0,Pn0​(ηn​(ωn)<0)>0.formulae-sequencesubscript𝑑𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛0formulae-sequencesuperscriptsubscript𝑃𝑛0subscript𝜂𝑛subscript𝜔𝑛00superscriptsubscript𝑃𝑛0subscript𝜂𝑛subscript𝜔𝑛00\displaystyle d\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})>0,\quad P\_{n}^{0}(\eta\_{n}(\omega\_{n})>0)>0,\quad P\_{n}^{0}(\eta\_{n}(\omega\_{n})<0)>0. |  | (61) |

From these conditions we obtain
Ωn−=Ωn0−×Ωn−1,Ωn+=Ωn0+×Ωn−1,formulae-sequencesuperscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛limit-from0subscriptΩ𝑛1superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛limit-from0subscriptΩ𝑛1\Omega\_{n}^{-}=\Omega\_{n}^{0-}\times\Omega\_{n-1},\ \Omega\_{n}^{+}=\Omega\_{n}^{0+}\times\Omega\_{n-1},
where Ωn0−={ωn∈Ωn0,ηn​(ωn)≤0},Ωn0+={ωn∈Ωn0,ηn​(ωn)>0}.formulae-sequencesuperscriptsubscriptΩ𝑛limit-from0formulae-sequencesubscript𝜔𝑛superscriptsubscriptΩ𝑛0subscript𝜂𝑛subscript𝜔𝑛0superscriptsubscriptΩ𝑛limit-from0formulae-sequencesubscript𝜔𝑛superscriptsubscriptΩ𝑛0subscript𝜂𝑛subscript𝜔𝑛0\Omega\_{n}^{0-}=\{\omega\_{n}\in\Omega\_{n}^{0},\eta\_{n}(\omega\_{n})\leq 0\},\ \Omega\_{n}^{0+}=\{\omega\_{n}\in\Omega\_{n}^{0},\eta\_{n}(\omega\_{n})>0\}.

From the suppositions above, it follows that Pn0​(Ωn0−)>0,Pn0​(Ωn0+)>0.formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscriptΩ𝑛limit-from00superscriptsubscript𝑃𝑛0superscriptsubscriptΩ𝑛limit-from00P\_{n}^{0}(\Omega\_{n}^{0-})>0,\ P\_{n}^{0}(\Omega\_{n}^{0+})>0.
The measure Pn0−superscriptsubscript𝑃𝑛limit-from0P\_{n}^{0-} is a contraction of the measure Pn0superscriptsubscript𝑃𝑛0P\_{n}^{0} on the σ𝜎\sigma-algebra ℱn0−=Ωn0−∩ℱn0,superscriptsubscriptℱ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptℱ𝑛0{\cal F}\_{n}^{0-}=\Omega\_{n}^{0-}\cap{\cal F}\_{n}^{0}, Pn0+superscriptsubscript𝑃𝑛limit-from0P\_{n}^{0+} is a contraction of the measure Pn0superscriptsubscript𝑃𝑛0P\_{n}^{0} on the σ𝜎\sigma-algebra ℱn0+=Ωn0+∩ℱn0.superscriptsubscriptℱ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptℱ𝑛0{\cal F}\_{n}^{0+}=\Omega\_{n}^{0+}\cap{\cal F}\_{n}^{0}.

###### Theorem 2.

Let Ωi0superscriptsubscriptΩ𝑖0\Omega\_{i}^{0} be a complete separable metric space and let ℱi0superscriptsubscriptℱ𝑖0{\cal F}\_{i}^{0} be a Borell σ𝜎\sigma-algebra on Ωi0,i=1,N¯.

superscriptsubscriptΩ𝑖0𝑖
¯

1𝑁\Omega\_{i}^{0},\ i=\overline{1,N}.
Suppose that for Δ​Sn​(ω1,…,ωn−1,ωn),n=1,N¯,

Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝑛
¯

1𝑁\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}),\ n=\overline{1,N}, the representation ([60](#S4.E60 "In 4 Inequalities for the nonnegative random values.")) is valid and
Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values.") conditions are true.
Then, for the nonnegative random value fn​(ω1,…,ωn−1,ωn)subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}) the inequalities

|  |  |  |
| --- | --- | --- |
|  | χΩn0−(ωn1)χΩn0+(ωn2)[Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\chi\_{\Omega\_{n}^{0-}}(\omega\_{n}^{1})\chi\_{\Omega\_{n}^{0+}}(\omega\_{n}^{2})\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]≤1,\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]\leq 1, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ω1,…,ωn−1)∈Ωn−1,(ωn1,ωn2)∈Ωn0−×Ωn0+,n=1,N¯,formulae-sequencesubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1formulae-sequencesuperscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0𝑛¯  1𝑁\displaystyle(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1},\quad(\omega\_{n}^{1},\omega\_{n}^{2})\in\Omega\_{n}^{0-}\times\Omega\_{n}^{0+},\quad n=\overline{1,N}, |  | (62) |

are true almost everywhere relative to the measure Pn−1×Pn0−×Pn0+subscript𝑃𝑛1superscriptsubscript𝑃𝑛limit-from0superscriptsubscript𝑃𝑛limit-from0P\_{n-1}\times P\_{n}^{0-}\times P\_{n}^{0+} on the measurable space {Ωn−1×Ωn0−×Ωn0+,ℱn−1×ℱn0−×ℱn0+}subscriptΩ𝑛1superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0subscriptℱ𝑛1superscriptsubscriptℱ𝑛limit-from0superscriptsubscriptℱ𝑛limit-from0\{\Omega\_{n-1}\times\Omega\_{n}^{0-}\times\Omega\_{n}^{0+},{\cal F}\_{n-1}\times{\cal F}\_{n}^{0-}\times{\cal F}\_{n}^{0+}\}.

###### Proof.

Under Theorem [2](#Thmte2 "Theorem 2. ‣ 4 Inequalities for the nonnegative random values.") conditions, the set of martingale measures is a nonempty one.
Due to the equality ([40](#S3.E40 "In Proof. ‣ 3 Construction of the set of martingale measures.")), we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN∏i=1Nψi​(ω1,…,ωi)​fn​(ω1,…,ωn)​∏i=1Nd​Pi0​(ωi)=subscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖absent\int\limits\_{\Omega\_{N}}\prod\limits\_{i=1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})f\_{n}(\omega\_{1},\ldots,\omega\_{n})\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn∏i=1nψi​(ω1,…,ωi)​fn​(ω1,…,ωn)​∏i=1nd​Pi0​(ωi).subscriptsubscriptΩ𝑛superscriptsubscriptproduct𝑖1𝑛subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖\displaystyle\int\limits\_{\Omega\_{n}}\prod\limits\_{i=1}^{n}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})f\_{n}(\omega\_{1},\ldots,\omega\_{n})\prod\limits\_{i=1}^{n}dP\_{i}^{0}(\omega\_{i}). |  | (63) |

Further,

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​fn​(ω1,…,ωn)​𝑑Pn0​(ωn)=subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛absent\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})f\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]dPn0(ωn1)dPn0(ωn2).\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2}). |  | (64) |

|  |  |  |
| --- | --- | --- |
|  | χΩn−​(ω1,…,ωn1)=χΩn−1​(ω1,…,ωn−1)​χΩn0−​(ωn1),subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…superscriptsubscript𝜔𝑛1subscript𝜒subscriptΩ𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜒superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝜔𝑛1\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n}^{1})=\chi\_{\Omega\_{n-1}}(\omega\_{1},\ldots,\omega\_{n-1})\chi\_{\Omega\_{n}^{0-}}(\omega\_{n}^{1}), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΩn+​(ω1,…,ωn2)=χΩn−1​(ω1,…,ωn−1)​χΩn0+​(ωn2).subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…superscriptsubscript𝜔𝑛2subscript𝜒subscriptΩ𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜒superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝜔𝑛2\displaystyle\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n}^{2})=\chi\_{\Omega\_{n-1}}(\omega\_{1},\ldots,\omega\_{n-1})\chi\_{\Omega\_{n}^{0+}}(\omega\_{n}^{2}). |  | (65) |

Due to Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values."), the inequality

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn0−(ωn1)χΩn0+(ωn2)αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{0-}}(\omega\_{n}^{1})\chi\_{\Omega\_{n}^{0+}}(\omega\_{n}^{2})\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]dPn0(ωn1)dPn0(ωn2)≤1,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})\leq 1, |  | (66) |

is true almost everywhere relative to the measure Pn−1subscript𝑃𝑛1P\_{n-1} on the σ𝜎\sigma-algebra ℱn−1.subscriptℱ𝑛1{\cal F}\_{n-1}.
Let us put

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})=αn​(ωn1;ωn2),subscript𝛼𝑛  subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝛼𝑛  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\displaystyle\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})=\alpha\_{n}(\omega\_{n}^{1};\omega\_{n}^{2}), |  | (67) |

where αn​(ωn1;ωn2)subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\alpha\_{n}(\omega\_{n}^{1};\omega\_{n}^{2}) satisfy the condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn0−∫Ωn0+αn​(ωn1;ωn2)​𝑑Pn0​(ωn1)​𝑑Pn0​(ωn2)=1.subscriptsuperscriptsubscriptΩ𝑛limit-from0subscriptsuperscriptsubscriptΩ𝑛limit-from0subscript𝛼𝑛  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2 differential-dsuperscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1differential-dsuperscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛21\displaystyle\int\limits\_{\Omega\_{n}^{0-}}\int\limits\_{\Omega\_{n}^{0+}}\alpha\_{n}(\omega\_{n}^{1};\omega\_{n}^{2})dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})=1. |  | (68) |

Since, on the probability space {Ωn0−×Ωn0+,\{\Omega\_{n}^{0-}\times\Omega\_{n}^{0+},ℱn0−×ℱn0+,Pn0−×Pn0+},{\cal F}\_{n}^{0-}\times{\cal F}\_{n}^{0+},P\_{n}^{0-}\times P\_{n}^{0+}\}, there exists an exhaustive decomposition {Am,k}m,k=1∞,superscriptsubscriptsubscript𝐴

𝑚𝑘

𝑚𝑘
1\{A\_{m,k}\}\_{m,k=1}^{\infty}, let us put

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​(ωn1;ωn2)=(1−ε)​χAm,k​(ωn1;ωn2)μn​(Am,k)+ε​χΩn0−×Ωn0+∖Am,k​(ωn1;ωn2)μn​(Ωn0−×Ωn0+∖Am,k),subscript𝛼𝑛  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛21𝜀subscript𝜒subscript𝐴  𝑚𝑘  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝜇𝑛subscript𝐴  𝑚𝑘𝜀subscript𝜒superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0subscript𝐴  𝑚𝑘  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝜇𝑛superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0subscript𝐴  𝑚𝑘\displaystyle\alpha\_{n}(\omega\_{n}^{1};\omega\_{n}^{2})=(1-\varepsilon)\frac{\chi\_{A\_{m,k}}(\omega\_{n}^{1};\omega\_{n}^{2})}{\mu\_{n}(A\_{m,k})}+\varepsilon\frac{\chi\_{\Omega\_{n}^{0-}\times\Omega\_{n}^{0+}\setminus A\_{m,k}}(\omega\_{n}^{1};\omega\_{n}^{2})}{\mu\_{n}(\Omega\_{n}^{0-}\times\Omega\_{n}^{0+}\setminus A\_{m,k})}, |  | (69) |

where μn​(A)=[Pn0−×Pn0+]​(A),A∈ℱn0−×ℱn0+,formulae-sequencesubscript𝜇𝑛𝐴delimited-[]superscriptsubscript𝑃𝑛limit-from0superscriptsubscript𝑃𝑛limit-from0𝐴𝐴superscriptsubscriptℱ𝑛limit-from0superscriptsubscriptℱ𝑛limit-from0\mu\_{n}(A)=[P\_{n}^{0-}\times P\_{n}^{0+}](A),\ A\in{\cal F}\_{n}^{0-}\times{\cal F}\_{n}^{0+}, and we assume that μn​(Am,k)>0,subscript𝜇𝑛subscript𝐴

𝑚𝑘0\mu\_{n}(A\_{m,k})>0, μn​(Ωn0−×Ωn0+∖Am,k)>0.subscript𝜇𝑛superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0subscript𝐴

𝑚𝑘0\mu\_{n}(\Omega\_{n}^{0-}\times\Omega\_{n}^{0+}\setminus A\_{m,k})>0.
Suppose that (ωn1;ωn2)∈Am,k

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2
subscript𝐴

𝑚𝑘(\omega\_{n}^{1};\omega\_{n}^{2})\in A\_{m,k} and μn​(Am,k)>0subscript𝜇𝑛subscript𝐴

𝑚𝑘0\mu\_{n}(A\_{m,k})>0 for the infinite number of m𝑚m and k.𝑘k.
Then,

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn0−(ωn1)χΩn0+(ωn2)[(1−ε)χAm,k​(ωn1;ωn2)μn​(Am,k)+εχΩn0−×Ωn0+∖Am,k​(ωn1;ωn2)μn​(Ωn0−×Ωn0+∖Am,k)]×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{0-}}(\omega\_{n}^{1})\chi\_{\Omega\_{n}^{0+}}(\omega\_{n}^{2})\left[(1-\varepsilon)\frac{\chi\_{A\_{m,k}}(\omega\_{n}^{1};\omega\_{n}^{2})}{\mu\_{n}(A\_{m,k})}+\varepsilon\frac{\chi\_{\Omega\_{n}^{0-}\times\Omega\_{n}^{0+}\setminus A\_{m,k}}(\omega\_{n}^{1};\omega\_{n}^{2})}{\mu\_{n}(\Omega\_{n}^{0-}\times\Omega\_{n}^{0+}\setminus A\_{m,k})}\right]\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]dPn0(ωn1)dPn0(ωn2)≤1.\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})\leq 1. |  | (70) |

Going to the limit as m,k→∞→

𝑚𝑘
m,k\to\infty and then as ε→0,→𝜀0\varepsilon\to 0, we obtain the inequality

|  |  |  |
| --- | --- | --- |
|  | χΩn0,−(ωn1)χΩn0,+(ωn2)[Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\chi\_{\Omega\_{n}^{0,-}}(\omega\_{n}^{1})\chi\_{\Omega\_{n}^{0,+}}(\omega\_{n}^{2})\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]≤1,(ω1,…,ωn−1)∈Ωn−1.\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]\leq 1,\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}. |  | (71) |

which is valid almost everywhere relative to the measure μn.subscript𝜇𝑛\mu\_{n}.
Theorem [2](#Thmte2 "Theorem 2. ‣ 4 Inequalities for the nonnegative random values.") is proved.
∎

###### Lemma 5.

Let Ωn0superscriptsubscriptΩ𝑛0\Omega\_{n}^{0} be a complete separable metric space and let ℱn0superscriptsubscriptℱ𝑛0{\cal F}\_{n}^{0} be a Borel σ𝜎\sigma-algebra on Ωn0,n=1,N¯

superscriptsubscriptΩ𝑛0𝑛
¯

1𝑁\Omega\_{n}^{0},\ n=\overline{1,N}.
If the conditions of Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values.") are true, then the inequality

|  |  |  |
| --- | --- | --- |
|  | χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]≤1,(ω1,…,ωn−1)∈Ωn−1,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]\leq 1,\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (72) |

is valid almost everywhere relative to the measure Pn−1×[Pn0×Pn0]subscript𝑃𝑛1delimited-[]superscriptsubscript𝑃𝑛0superscriptsubscript𝑃𝑛0P\_{n-1}\times[P\_{n}^{0}\times P\_{n}^{0}] on the measurable space {Ωn−1×Ωn0×Ωn0,ℱn−1×ℱn0×ℱn0}.subscriptΩ𝑛1superscriptsubscriptΩ𝑛0superscriptsubscriptΩ𝑛0subscriptℱ𝑛1superscriptsubscriptℱ𝑛0superscriptsubscriptℱ𝑛0\{\Omega\_{n-1}\times\Omega\_{n}^{0}\times\Omega\_{n}^{0},{\cal F}\_{n-1}\times{\cal F}\_{n}^{0}\times{\cal F}\_{n}^{0}\}.

###### Proof.

Due to the conditions for Ωna,a=−,+,formulae-sequence

superscriptsubscriptΩ𝑛𝑎𝑎
\Omega\_{n}^{a},a=-,+, the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωna=⋃k=1Nn[An0,k​a×Vn−1k]superscriptsubscriptΩ𝑛𝑎superscriptsubscript𝑘1subscript𝑁𝑛delimited-[]superscriptsubscript𝐴𝑛  0𝑘𝑎superscriptsubscript𝑉𝑛1𝑘\displaystyle\Omega\_{n}^{a}=\bigcup\limits\_{k=1}^{N\_{n}}[A\_{n}^{0,ka}\times V\_{n-1}^{k}] |  | (73) |

is true. Owing to Lemma [5](#Thmleme5 "Lemma 5. ‣ 4 Inequalities for the nonnegative random values.") conditions, there exists an exhaustive decomposition Dm​in,m,i=1,∞¯,

superscriptsubscript𝐷𝑚𝑖𝑛𝑚𝑖
¯

1D\_{mi}^{n},\ m,i=\overline{1,\infty}, such that ⋃i=1∞Dm​in=Ωn0,m=1,∞¯.formulae-sequencesuperscriptsubscript𝑖1superscriptsubscript𝐷𝑚𝑖𝑛superscriptsubscriptΩ𝑛0𝑚¯

1\bigcup\limits\_{i=1}^{\infty}D\_{mi}^{n}=\Omega\_{n}^{0},\ m=\overline{1,\infty}.
Let us denote An0,k​a∩Dm​in=Em​in​k​a.superscriptsubscript𝐴𝑛

0𝑘𝑎superscriptsubscript𝐷𝑚𝑖𝑛superscriptsubscript𝐸𝑚𝑖𝑛𝑘𝑎A\_{n}^{0,ka}\cap D\_{mi}^{n}=E\_{mi}^{nka}.
It is evident that Em​in​k​asuperscriptsubscript𝐸𝑚𝑖𝑛𝑘𝑎E\_{mi}^{nka} forms an exhaustive decomposition of sets An0,k​a,n=1,N¯,k=1,∞¯,a=−,+,formulae-sequence

superscriptsubscript𝐴𝑛

0𝑘𝑎𝑛
¯

1𝑁formulae-sequence𝑘¯

1𝑎

A\_{n}^{0,ka},\ n=\overline{1,N},\ k=\overline{1,\infty},\ a=-,+, correspondingly.
Due to Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values."), the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​fn​(ω1,…,ωn)​𝑑Pn0​(ωn)≤1,(ω1,…,ωn−1)∈Ωn−1,formulae-sequencesubscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛1subscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1\displaystyle\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})f\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})\leq 1,\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (74) |

is true almost everywhere relative to the measure Pn−1.subscript𝑃𝑛1P\_{n-1}.
The equality

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​fn​(ω1,…,ωn)​𝑑Pn0​(ωn)=subscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛absent\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})f\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]dPn0(ωn1)dPn0(ωn2)\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2}) |  | (75) |

is valid.
From the equality ([75](#S4.E75 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")) and Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values."), the inequality

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}}\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω1,…,ωn−1,ωn1};{ω1,…,ωn−1,ωn2})×\alpha\_{n}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]dPn0(ωn1)dPn0(ωn2)≤1,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})\leq 1, |  | (76) |

is true almost everywhere relative to the measure Pn−1subscript𝑃𝑛1P\_{n-1} on the σ𝜎\sigma-algebra ℱn−1.subscriptℱ𝑛1{\cal F}\_{n-1}.
Let us put

|  |  |  |
| --- | --- | --- |
|  | αnr,s−​(ω11,…,ωn1)=∑k=1Nnαn,k,r,s−​(ωn1)​χAn0,k−​(ωn1)​χVn−1k​(ω11,…,ωn1),superscriptsubscript𝛼𝑛  𝑟limit-from𝑠superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝑘1subscript𝑁𝑛superscriptsubscript𝛼  𝑛𝑘𝑟𝑠superscriptsubscript𝜔𝑛1subscript𝜒superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝜔𝑛1subscript𝜒superscriptsubscript𝑉𝑛1𝑘superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1\alpha\_{n}^{r,s-}(\omega\_{1}^{1},\ldots,\omega\_{n}^{1})=\sum\limits\_{k=1}^{N\_{n}}\alpha\_{n,k,r,s}^{-}(\omega\_{n}^{1})\chi\_{A\_{n}^{0,k-}}(\omega\_{n}^{1})\chi\_{V\_{n-1}^{k}}(\omega\_{1}^{1},\ldots,\omega\_{n}^{1}), |  |

|  |  |  |
| --- | --- | --- |
|  | αnm,i+​(ω12,…,ωn2)=∑k=1Nnαn,k,m,i+​(ωn2)​χAn0,k+​(ωn2)​χVn−1k​(ω12,…,ωn−12),superscriptsubscript𝛼𝑛  𝑚limit-from𝑖superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2superscriptsubscript𝑘1subscript𝑁𝑛superscriptsubscript𝛼  𝑛𝑘𝑚𝑖superscriptsubscript𝜔𝑛2subscript𝜒superscriptsubscript𝐴𝑛  0limit-from𝑘superscriptsubscript𝜔𝑛2subscript𝜒superscriptsubscript𝑉𝑛1𝑘superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12\alpha\_{n}^{m,i+}(\omega\_{1}^{2},\ldots,\omega\_{n}^{2})=\sum\limits\_{k=1}^{N\_{n}}\alpha\_{n,k,m,i}^{+}(\omega\_{n}^{2})\chi\_{A\_{n}^{0,k+}}(\omega\_{n}^{2})\chi\_{V\_{n-1}^{k}}(\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2}), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | αnr,s,m,i​({ω11,…,ωn1};{ω12,…,ωn2})=αnr,s−​(ω11,…,ωn1)​αnm,i+​(ω12,…,ωn2),superscriptsubscript𝛼𝑛  𝑟𝑠𝑚𝑖  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2superscriptsubscript𝛼𝑛  𝑟limit-from𝑠superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝛼𝑛  𝑚limit-from𝑖superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\displaystyle\alpha\_{n}^{r,s,m,i}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})=\alpha\_{n}^{r,s-}(\omega\_{1}^{1},\ldots,\omega\_{n}^{1})\alpha\_{n}^{m,i+}(\omega\_{1}^{2},\ldots,\omega\_{n}^{2}), |  | (77) |

where

|  |  |  |
| --- | --- | --- |
|  | αn,k,r,s−​(ωn1)=[(1−δ)​χEr​sn​k−​(ωn1)Pn0​(Er​sn​k−)+δ​χAn0​k−∖Er​sn​k−​(ωn1)Pn0​(An0​k−∖Er​sn​k−)],superscriptsubscript𝛼  𝑛𝑘𝑟𝑠superscriptsubscript𝜔𝑛1delimited-[]1𝛿subscript𝜒superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘superscriptsubscript𝜔𝑛1superscriptsubscript𝑃𝑛0superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘𝛿subscript𝜒superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘superscriptsubscript𝜔𝑛1superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘\alpha\_{n,k,r,s}^{-}(\omega\_{n}^{1})=\left[(1-\delta)\frac{\chi\_{E\_{rs}^{nk-}}(\omega\_{n}^{1})}{P\_{n}^{0}(E\_{rs}^{nk-})}+\delta\frac{\chi\_{A\_{n}^{0k-}\setminus E\_{rs}^{nk-}}(\omega\_{n}^{1})}{P\_{n}^{0}(A\_{n}^{0k-}\setminus E\_{rs}^{nk-})}\right], |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn,k,m,i+​(ωn2)=[(1−δ)​χEm​in​k+​(ωn2)Pn0​(Em​in​k+)+δ​χAn0​k+∖Em​in​k+​(ωn2)Pn0​(An0​k+∖Em​in​k+)],0<δ<1.formulae-sequencesuperscriptsubscript𝛼  𝑛𝑘𝑚𝑖superscriptsubscript𝜔𝑛2delimited-[]1𝛿subscript𝜒superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝑃𝑛0superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘𝛿subscript𝜒superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘0𝛿1\displaystyle\alpha\_{n,k,m,i}^{+}(\omega\_{n}^{2})=\left[(1-\delta)\frac{\chi\_{E\_{mi}^{nk+}}(\omega\_{n}^{2})}{P\_{n}^{0}(E\_{mi}^{nk+})}+\delta\frac{\chi\_{A\_{n}^{0k+}\setminus E\_{mi}^{nk+}}(\omega\_{n}^{2})}{P\_{n}^{0}(A\_{n}^{0k+}\setminus E\_{mi}^{nk+})}\right],\quad 0<\delta<1. |  | (78) |

In the formulas ([78](#S4.E78 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), we assume that the inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn0​(Er​sn​k−)>0,Pn0​(An0​k−∖Er​sn​k−)>0,Pn0​(Em​in​k+)>0,Pn0​(An0​k+∖Em​in​k+)>0,formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘0formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘0formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘0superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘0\displaystyle P\_{n}^{0}(E\_{rs}^{nk-})>0,\ P\_{n}^{0}(A\_{n}^{0k-}\setminus E\_{rs}^{nk-})>0,\ P\_{n}^{0}(E\_{mi}^{nk+})>0,\ P\_{n}^{0}(A\_{n}^{0k+}\setminus E\_{mi}^{nk+})>0, |  | (79) |

are true.
Let us consider

|  |  |  |
| --- | --- | --- |
|  | αnr,s,m,i​({ω1,…,ωn−1,ωn−11};{ω1,…,ωn−1,ωn2})=superscriptsubscript𝛼𝑛  𝑟𝑠𝑚𝑖  subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛11subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2absent\alpha\_{n}^{r,s,m,i}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n-1}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | αnr,s−​(ω1,…,ωn−1,ωn1)​αnm,i+​(ω1,…,ωn−1,ωn2).superscriptsubscript𝛼𝑛  𝑟limit-from𝑠subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝛼𝑛  𝑚limit-from𝑖subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2\displaystyle\alpha\_{n}^{r,s-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\alpha\_{n}^{m,i+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}). |  | (80) |

Suppose that (ω1,…,ωn−1)∈Vn−1ksubscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑉𝑛1𝑘(\omega\_{1},\ldots,\omega\_{n-1})\in V\_{n-1}^{k} for a certain k.𝑘k.
Then,

|  |  |  |
| --- | --- | --- |
|  | αnr,s,m,i​({ω1,…,ωn−1,ωn−11};{ω1,…,ωn−1,ωn2})=superscriptsubscript𝛼𝑛  𝑟𝑠𝑚𝑖  subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛11subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2absent\alpha\_{n}^{r,s,m,i}(\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n-1}^{1}\};\{\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}\})= |  |

|  |  |  |
| --- | --- | --- |
|  | [(1−δ)χEr​sn​k−​(ωn1)Pn0​(Er​sn​k−)+δχAn0​k−∖Er​sn​k−​(ωn1)Pn0​(An0​k−∖Er​sn​k−)]×\left[(1-\delta)\frac{\chi\_{E\_{rs}^{nk-}}(\omega\_{n}^{1})}{P\_{n}^{0}(E\_{rs}^{nk-})}+\delta\frac{\chi\_{A\_{n}^{0k-}\setminus E\_{rs}^{nk-}}(\omega\_{n}^{1})}{P\_{n}^{0}(A\_{n}^{0k-}\setminus E\_{rs}^{nk-})}\right]\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | [(1−δ)​χEm​in​k+​(ωn2)Pn0​(Em​in​k+)+δ​χAn0​k+∖Em​in​k+​(ωn2)Pn0​(An0​k+∖Em​in​k+)].delimited-[]1𝛿subscript𝜒superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝑃𝑛0superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘𝛿subscript𝜒superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝑃𝑛0superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘\displaystyle\left[(1-\delta)\frac{\chi\_{E\_{mi}^{nk+}}(\omega\_{n}^{2})}{P\_{n}^{0}(E\_{mi}^{nk+})}+\delta\frac{\chi\_{A\_{n}^{0k+}\setminus E\_{mi}^{nk+}}(\omega\_{n}^{2})}{P\_{n}^{0}(A\_{n}^{0k+}\setminus E\_{mi}^{nk+})}\right]. |  | (81) |

We assume that the point (ωn1,ωn2)∈Er​sn​k−×Em​in​k+superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘(\omega\_{n}^{1},\omega\_{n}^{2})\in E\_{rs}^{nk-}\times E\_{mi}^{nk+} for the infinite number of r,s

𝑟𝑠r,s and m,i

𝑚𝑖m,i , where Pn0​(Er​sn​k−)>0,Pn0​(Em​in​k+)>0.formulae-sequencesuperscriptsubscript𝑃𝑛0superscriptsubscript𝐸𝑟𝑠limit-from𝑛𝑘0superscriptsubscript𝑃𝑛0superscriptsubscript𝐸𝑚𝑖limit-from𝑛𝑘0P\_{n}^{0}(E\_{rs}^{nk-})>0,\ P\_{n}^{0}(E\_{mi}^{nk+})>0.

Substituting ([81](#S4.E81 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")) into ([76](#S4.E76 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")) and going to the limit as m,k→∞→

𝑚𝑘
m,k\to\infty r,s→∞→

𝑟𝑠
r,s\to\infty and then as δ→0,→𝛿0\delta\to 0, we obtain the needed inequality. Lemma [5](#Thmleme5 "Lemma 5. ‣ 4 Inequalities for the nonnegative random values.") is proved.
∎

###### Theorem 3.

Suppose that the conditions of Theorem [2](#Thmte2 "Theorem 2. ‣ 4 Inequalities for the nonnegative random values.") are true. If
for a certain ωn1∈Ωn0−superscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛limit-from0\omega\_{n}^{1}\in\Omega\_{n}^{0-} and ωn2∈Ωn0+superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛limit-from0\omega\_{n}^{2}\in\Omega\_{n}^{0+} the inequalities

|  |  |  |
| --- | --- | --- |
|  | sup(ω1,…,ωn−1)∈Ωn−11Δ​Sn−​(ω1,…,ωn−1,ωn1)<∞,subscriptsupremumsubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛11Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1\sup\limits\_{(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}}\frac{1}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}<\infty, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(ω1,…,ωn−1)∈Ωn−11Δ​Sn+​(ω1,…,ωn−1,ωn2)<∞,n=1,N¯,formulae-sequencesubscriptsupremumsubscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛11Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑛¯  1𝑁\displaystyle\sup\limits\_{(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}}\frac{1}{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}<\infty,\quad n=\overline{1,N}, |  | (82) |

are true, then the nonnegative random values fn​(ω1,…,ωn−1,ωn),n=1,N¯,

subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝑛
¯

1𝑁f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}),\ n=\overline{1,N}, satisfy the inequalities

|  |  |  |
| --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn)≤subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absentf\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\leq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1+γn−1​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn−1,ωn)),n=1,N¯,  1subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝑛 ¯  1𝑁\displaystyle(1+\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})),\quad n=\overline{1,N}, |  | (83) |

where γn−1​(ω1,…,ωn−1)subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) is a bounded ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1}-measurable random value.

###### Proof.

From the inequality ([71](#S4.E71 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), it follows the inequality

|  |  |  |
| --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn2)≤subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2absentf\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\leq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1+1−fn​(ω1,…,ωn−1,ωn1)Δ​Sn−​(ω1,…,ωn−1,ωn1)​Δ​Sn+​(ω1,…,ωn−1,ωn2),ωn1∈Ωn0−,ωn2∈Ωn0+.formulae-sequence  11subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscript𝜔𝑛1 superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛limit-from0\displaystyle 1+\frac{1-f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}\Delta S\_{n}^{+}(\omega\_{1},\quad\ldots,\omega\_{n-1},\omega\_{n}^{2}),\ \omega\_{n}^{1}\in\Omega\_{n}^{0-},\ \omega\_{n}^{2}\in\Omega\_{n}^{0+}. |  | (84) |

Let us define

|  |  |  |  |
| --- | --- | --- | --- |
|  | γn−1​(ω1,…,ωn−1)=inf{ωn1,ηn−​(ωn1)>0}1−fn​(ω1,…,ωn−1,ωn1)Δ​Sn−​(ω1,…,ωn−1,ωn1),subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1subscriptinfimum  superscriptsubscript𝜔𝑛1superscriptsubscript𝜂𝑛superscriptsubscript𝜔𝑛1 01subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1\displaystyle\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})=\inf\_{\{\omega\_{n}^{1},\eta\_{n}^{-}(\omega\_{n}^{1})>0\}}\frac{1-f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}, |  | (85) |

then, taking into account the inequality ([84](#S4.E84 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), we obtain the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn2)≤1+γn−1​(ω1,…,ωn−1)​Δ​Sn+​(ω1,…,ωn−1,ωn2).subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛21subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\leq 1+\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}). |  | (86) |

From the definition of γn−1​(ω1,…,ωn−1),subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}), we obtain the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn1)≤1−γn−1​(ω1,…,ωn−1)​Δ​Sn−​(ω1,…,ωn−1,ωn1).subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛11subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\leq 1-\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}). |  | (87) |

The inequalities ([86](#S4.E86 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), ([87](#S4.E87 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")) give the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn)≤1+γn−1​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn−1,ωn).subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛1subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\leq 1+\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}). |  | (88) |

Let us prove the boundedness of γn−1​(ω1,…,ωn−1).subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}). From the inequalities ([86](#S4.E86 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), ([87](#S4.E87 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")) we obtain

|  |  |  |
| --- | --- | --- |
|  | 1Δ​Sn−​(ω1,…,ωn−1,ωn1)≥1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1absent\frac{1}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | γn−1​(ω1,…,ωn−1)≥−1Δ​Sn+​(ω1,…,ωn−1,ωn2).subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛11Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2\displaystyle\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\geq-\frac{1}{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}. |  | (89) |

Due to Theorem [3](#Thmte3 "Theorem 3. ‣ 4 Inequalities for the nonnegative random values.") conditions, we obtain the boundedness of γn−1​(ω1,…,ωn−1).subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}).
The ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1} measurability of the random value γn−1​(ω1,…,ωn−1)subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) follows from the fact that Ωn0superscriptsubscriptΩ𝑛0\Omega\_{n}^{0} is separable metric space and infimum is reached on the countable set, which is dense in Ωn0.superscriptsubscriptΩ𝑛0\Omega\_{n}^{0}. Theorem [3](#Thmte3 "Theorem 3. ‣ 4 Inequalities for the nonnegative random values.") is proved.
∎

###### Theorem 4.

Let the conditions of Lemma [5](#Thmleme5 "Lemma 5. ‣ 4 Inequalities for the nonnegative random values.") be valid. If there exist
ωn1∈An0​k−,ωn2∈An0​k+,formulae-sequencesuperscriptsubscript𝜔𝑛1superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝐴𝑛limit-from0𝑘\omega\_{n}^{1}\in A\_{n}^{0k-},\ \omega\_{n}^{2}\in A\_{n}^{0k+}, and
the real numbers ak,bk,k=1,Nn¯,

subscript𝑎𝑘subscript𝑏𝑘𝑘
¯

1subscript𝑁𝑛a\_{k},\ b\_{k},\ k=\overline{1,N\_{n}}, such that

|  |  |  |
| --- | --- | --- |
|  | sup(ω1,…,ωn−1)∈Vn−1k1Δ​Sn−​(ω1,…,ωn−1,ωn1)=akn<∞,subscriptsupremumsubscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑉𝑛1𝑘1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝑎𝑘𝑛\sup\limits\_{(\omega\_{1},\ldots,\omega\_{n-1})\in V\_{n-1}^{k}}\frac{1}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}=a\_{k}^{n}<\infty, |  |

|  |  |  |
| --- | --- | --- |
|  | sup(ω1,…,ωn−1)∈Vn−1k1Δ​Sn+​(ω1,…,ωn−1,ωn2)=bkn<∞,k=1,Nn¯,n=1,N¯,formulae-sequencesubscriptsupremumsubscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑉𝑛1𝑘1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscript𝑏𝑘𝑛formulae-sequence𝑘¯  1subscript𝑁𝑛𝑛¯  1𝑁\sup\limits\_{(\omega\_{1},\ldots,\omega\_{n-1})\in V\_{n-1}^{k}}\frac{1}{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}=b\_{k}^{n}<\infty,\quad k=\overline{1,N\_{n}},\quad n=\overline{1,N}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | max1≤n≤N​sup1≤k≤Nnmax⁡{akn,bkn}<∞,subscript1𝑛𝑁subscriptsupremum1𝑘subscript𝑁𝑛superscriptsubscript𝑎𝑘𝑛superscriptsubscript𝑏𝑘𝑛\displaystyle\max\limits\_{1\leq n\leq N}\sup\limits\_{1\leq k\leq N\_{n}}\max\{a\_{k}^{n},b\_{k}^{n}\}<\infty, |  | (90) |

then there exists a bounded ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1}-measurable random value γn−1​(ω1,…,ωn−1)subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) such that the inequalities

|  |  |  |
| --- | --- | --- |
|  | fn(ω1,…,ωn−1,ωn))≤f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}))\leq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1+γn−1​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn−1,ωn)),n=1,N¯,  1subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝑛 ¯  1𝑁\displaystyle(1+\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})),\quad n=\overline{1,N}, |  | (91) |

are true.

###### Proof.

For ωn1∈An0​k−,ωn2∈An0​k+formulae-sequencesuperscriptsubscript𝜔𝑛1superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝐴𝑛limit-from0𝑘\omega\_{n}^{1}\in A\_{n}^{0k-},\ \omega\_{n}^{2}\in A\_{n}^{0k+} and
(ω1,…,ωn−1)∈Vn−1k,subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑉𝑛1𝑘(\omega\_{1},\ldots,\omega\_{n-1})\in V\_{n-1}^{k}, we have that
(ω1,…,ωn−1,ωn1)∈Ωn−,subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\in\Omega\_{n}^{-}, (ω1,…,ωn−1,ωn2)∈Ωn+.subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛\ (\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\in\Omega\_{n}^{+}.
Then, from the inequality ([72](#S4.E72 "In Lemma 5. ‣ 4 Inequalities for the nonnegative random values.")), we obtain the inequality

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn1)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)fn(ω1,…,ωn−1,ωn2)]≤1.\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\right]\leq 1. |  | (92) |

From the inequality ([92](#S4.E92 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), it follows the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn2)≤1+1−fn​(ω1,…,ωn−1,ωn1)Δ​Sn−​(ω1,…,ωn−1,ωn1)​Δ​Sn+​(ω1,…,ωn−1,ωn2).subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛211subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\leq 1+\frac{1-f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}). |  | (93) |

Let us define

|  |  |  |
| --- | --- | --- |
|  | γn−1k​(ω1,…,ωn−1)=superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1absent\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf{ωn1∈An0,k−}1−fn​(ω1,…,ωn−1,ωn1)Δ​Sn−​(ω1,…,ωn−1,ωn1),(ω1,…,ωn−1)∈Vn−1k,  subscriptinfimumsuperscriptsubscript𝜔𝑛1superscriptsubscript𝐴𝑛  0limit-from𝑘1subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝜔1…subscript𝜔𝑛1 superscriptsubscript𝑉𝑛1𝑘\displaystyle\inf\_{\{\omega\_{n}^{1}\in A\_{n}^{0,k-}\}}\frac{1-f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in V\_{n-1}^{k}, |  | (94) |

then, taking into account the inequality ([93](#S4.E93 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), we have the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn2)≤1+γn−1k​(ω1,…,ωn−1)​Δ​Sn+​(ω1,…,ωn−1,ωn2).subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛21superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\leq 1+\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2}). |  | (95) |

From the definition of γn−1k​(ω1,…,ωn−1),superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1}), we obtain the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn1)≤1−γn−1k​(ω1,…,ωn−1)​Δ​Sn−​(ω1,…,ωn−1,ωn1).subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛11superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\leq 1-\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1}). |  | (96) |

The inequalities ([95](#S4.E95 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), ([96](#S4.E96 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")) give the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn−1,ωn)≤1+γn−1k​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn−1,ωn).subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛1superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\leq 1+\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}). |  | (97) |

Let us prove the boundedness of γn−1k​(ω1,…,ωn−1).superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1}). From the inequalities ([95](#S4.E95 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), ([96](#S4.E96 "In Proof. ‣ 4 Inequalities for the nonnegative random values.")), we obtain the inequalities

|  |  |  |
| --- | --- | --- |
|  | akn=sup(ω1,…,ωn−1)∈Vn−1k1Δ​Sn−​(ω1,…,ωn−1,ωn1)≥superscriptsubscript𝑎𝑘𝑛subscriptsupremumsubscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑉𝑛1𝑘1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1absenta\_{k}^{n}=\sup\limits\_{(\omega\_{1},\ldots,\omega\_{n-1})\in V\_{n-1}^{k}}\frac{1}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | γn−1k​(ω1,…,ωn−1)≥−sup(ω1,…,ωn−1)∈Vn−1k1Δ​Sn+​(ω1,…,ωn−1,ωn2)=−bkn.superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1subscriptsupremumsubscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑉𝑛1𝑘1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscript𝑏𝑘𝑛\displaystyle\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1})\geq-\sup\limits\_{(\omega\_{1},\ldots,\omega\_{n-1})\in V\_{n-1}^{k}}\frac{1}{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}=-b\_{k}^{n}. |  | (98) |

From this, it follows the boundedness of γn−1k​(ω1,…,ωn−1).superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1}).
The ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1} measurability of the random value γn−1k​(ω1,…,ωn−1)superscriptsubscript𝛾𝑛1𝑘subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1}) follows from the fact that Ωn0superscriptsubscriptΩ𝑛0\Omega\_{n}^{0} is separable metric space and infimum is reached on the countable set, which is dense in Ωn0.superscriptsubscriptΩ𝑛0\Omega\_{n}^{0}.
To complete the proof of Theorem [4](#Thmte4 "Theorem 4. ‣ 4 Inequalities for the nonnegative random values."), let us put

|  |  |  |  |
| --- | --- | --- | --- |
|  | γn−1(ω1,…,ωn−1)=∑k=1NnχVn−1k((ω1,…,ωn−1)γn−1k(ω1,…,ωn−1),\displaystyle\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})=\sum\limits\_{k=1}^{N\_{n}}\chi\_{V\_{n-1}^{k}}((\omega\_{1},\ldots,\omega\_{n-1})\gamma\_{n-1}^{k}(\omega\_{1},\ldots,\omega\_{n-1}), |  | (99) |

then for such γn−1​(ω1,…,ωn−1)subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) the inequality ([91](#S4.E91 "In Theorem 4. ‣ 4 Inequalities for the nonnegative random values."))
are satisfied. Theorem [4](#Thmte4 "Theorem 4. ‣ 4 Inequalities for the nonnegative random values.") is proved.
∎

## 5 Optional decomposition for super-martingales.

In this section, we give simple proof of optional decomposition for the nonnegative super-martingale relative to the set of equivalent martingale measures. Such a proof first appeared in the paper [[16](#bib.bib16)].
First, the optional decomposition for diffusion processes super-martingale was opened by El Karoui N. and Quenez M. C. [[21](#bib.bib21)]. After that, Kramkov D. O. and Follmer H. [[22](#bib.bib22)], [[23](#bib.bib23)] proved the optional decomposition for the nonnegative bounded super-martingales. Folmer H. and Kabanov Yu. M. [[24](#bib.bib24)], [[25](#bib.bib25)] proved analogous result for an arbitrary super-martingale. Recently, Bouchard B. and Nutz M. [[26](#bib.bib26)] considered a class of discrete models and proved the necessary and sufficient conditions for the validity of the optional decomposition.

###### Theorem 5.

Let Ωi0superscriptsubscriptΩ𝑖0\Omega\_{i}^{0} be a complete separable metric space and let ℱi0superscriptsubscriptℱ𝑖0{\cal F}\_{i}^{0} be a Borell σ𝜎\sigma-algebra on Ωi0,i=1,N¯.

superscriptsubscriptΩ𝑖0𝑖
¯

1𝑁\Omega\_{i}^{0},\ i=\overline{1,N}. Suppose that the
evolution {Sn​(ω1,…,ωn)}n=1Nsuperscriptsubscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛𝑛1𝑁\{S\_{n}(\omega\_{1},\ldots,\omega\_{n})\}\_{n=1}^{N} of risky assets satisfies the conditions of Theorems [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures."), [2](#Thmte2 "Theorem 2. ‣ 4 Inequalities for the nonnegative random values."), [3](#Thmte3 "Theorem 3. ‣ 4 Inequalities for the nonnegative random values."), [4](#Thmte4 "Theorem 4. ‣ 4 Inequalities for the nonnegative random values."), then for every nonnegative super-martingale {fn1​(ω1,…,ωn)}n=0Nsuperscriptsubscriptsuperscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛𝑛0𝑁\{f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})\}\_{n=0}^{N} relative to the set of martingale measure M,𝑀M, described in Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures."), the optional decomposition is true.

###### Proof.

Without loss of generality, we assume that fn1​(ω1,…,ωn)≥a,superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛𝑎f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})\geq a, where a𝑎a is a real positive number. If it is not so, then we can come to the super-martingale fn1​(ω1,…,ωn)+a.superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛𝑎f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})+a. Let us consider the set of random values

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(ω1,…,ωn)=fn1​(ω1,…,ωn)fn−11​(ω1,…,ωn−1),n=1,N¯.formulae-sequencesubscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑓𝑛11subscript𝜔1…subscript𝜔𝑛1𝑛¯  1𝑁\displaystyle f\_{n}(\omega\_{1},\ldots,\omega\_{n})=\frac{f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})}{f\_{n-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})},\quad n=\overline{1,N}. |  | (100) |

Every random value fn​(ω1,…,ωn)subscript𝑓𝑛subscript𝜔1…subscript𝜔𝑛f\_{n}(\omega\_{1},\ldots,\omega\_{n}) satisfies the conditions of Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values."). Due to Theorems [3](#Thmte3 "Theorem 3. ‣ 4 Inequalities for the nonnegative random values."), [4](#Thmte4 "Theorem 4. ‣ 4 Inequalities for the nonnegative random values."), the inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn1​(ω1,…,ωn)fn−11​(ω1,…,ωn−1)≤1+γn−1​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn),n=1,N¯,formulae-sequencesuperscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑓𝑛11subscript𝜔1…subscript𝜔𝑛11subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛𝑛¯  1𝑁\displaystyle\frac{f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})}{f\_{n-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})}\leq 1+\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n}),\quad n=\overline{1,N}, |  | (101) |

are true, where γn−1​(ω1,…,ωn−1)subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}) is a bounded ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1}-measurable random value. Since EQ​|Δ​Sn​(ω1,…,ωn)|<∞,Q∈M,formulae-sequencesuperscript𝐸𝑄Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛𝑄𝑀E^{Q}|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})|<\infty,\ Q\in M, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ​{γn−1​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn)|ℱn−1}=0,Q∈M,n=1,N¯.formulae-sequencesuperscript𝐸𝑄conditional-setsubscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛subscriptℱ𝑛10formulae-sequence𝑄𝑀𝑛¯  1𝑁\displaystyle E^{Q}\{\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})|{\cal F}\_{n-1}\}=0,\quad Q\in M,\quad n=\overline{1,N}. |  | (102) |

Let us denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξn0​(ω1,…,ωn)=1+γn−1​(ω1,…,ωn−1)​Δ​Sn​(ω1,…,ωn),n=1,N¯.formulae-sequencesuperscriptsubscript𝜉𝑛0subscript𝜔1…subscript𝜔𝑛1subscript𝛾𝑛1subscript𝜔1…subscript𝜔𝑛1Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛𝑛¯  1𝑁\displaystyle\xi\_{n}^{0}(\omega\_{1},\ldots,\omega\_{n})=1+\gamma\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n}),\quad n=\overline{1,N}. |  | (103) |

Then, from the inequalities ([101](#S5.E101 "In Proof. ‣ 5 Optional decomposition for super-martingales.")), we obtain the inequalities

|  |  |  |
| --- | --- | --- |
|  | fn1​(ω1,…,ωn)≤superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛absentf\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})\leq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn−11​(ω1,…,ωn−1)+fn−11​(ω1,…,ωn−1)​[ξn0​(ω1,…,ωn)−1],n=1,N¯.  superscriptsubscript𝑓𝑛11subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑓𝑛11subscript𝜔1…subscript𝜔𝑛1delimited-[]superscriptsubscript𝜉𝑛0subscript𝜔1…subscript𝜔𝑛1𝑛 ¯  1𝑁\displaystyle f\_{n-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})+f\_{n-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})[\xi\_{n}^{0}(\omega\_{1},\ldots,\omega\_{n})-1],\quad n=\overline{1,N}. |  | (104) |

Introduce the denotations

|  |  |  |
| --- | --- | --- |
|  | gn​(ω1,…,ωn)=subscript𝑔𝑛subscript𝜔1…subscript𝜔𝑛absentg\_{n}(\omega\_{1},\ldots,\omega\_{n})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | −fn1​(ω1,…,ωn)+fn−11​(ω1,…,ωn−1)​ξn0​(ω1,…,ωn),n=1,N¯.  superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑓𝑛11subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜉𝑛0subscript𝜔1…subscript𝜔𝑛𝑛 ¯  1𝑁\displaystyle-f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})+f\_{n-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})\xi\_{n}^{0}(\omega\_{1},\ldots,\omega\_{n}),\quad n=\overline{1,N}. |  | (105) |

Then, gn​(ω1,…,ωn)≥0,n=1,N¯,formulae-sequencesubscript𝑔𝑛subscript𝜔1…subscript𝜔𝑛0𝑛¯

1𝑁g\_{n}(\omega\_{1},\ldots,\omega\_{n})\geq 0,\ n=\overline{1,N}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ​gn​(ω1,…,ωn)≤EQ​fn1​(ω1,…,ωn)+EQ​fn1​(ω1,…,ωn−1).superscript𝐸𝑄subscript𝑔𝑛subscript𝜔1…subscript𝜔𝑛superscript𝐸𝑄superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛superscript𝐸𝑄superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛1\displaystyle E^{Q}g\_{n}(\omega\_{1},\ldots,\omega\_{n})\leq E^{Q}f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})+E^{Q}f\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1}). |  | (106) |

The equalities ([105](#S5.E105 "In Proof. ‣ 5 Optional decomposition for super-martingales.")) give the equalities

|  |  |  |
| --- | --- | --- |
|  | fn1​(ω1,…,ωn)=superscriptsubscript𝑓𝑛1subscript𝜔1…subscript𝜔𝑛absentf\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f01+∑i=1nfi−11​(ω1,…,ωn−1)​[ξi0​(ω1,…,ωi)−1]−∑i=1ngi​(ω1,…,ωi),n=1,N¯.  superscriptsubscript𝑓01superscriptsubscript𝑖1𝑛superscriptsubscript𝑓𝑖11subscript𝜔1…subscript𝜔𝑛1delimited-[]superscriptsubscript𝜉𝑖0subscript𝜔1…subscript𝜔𝑖1superscriptsubscript𝑖1𝑛subscript𝑔𝑖subscript𝜔1…subscript𝜔𝑖𝑛 ¯  1𝑁\displaystyle f\_{0}^{1}+\sum\limits\_{i=1}^{n}f\_{i-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})[\xi\_{i}^{0}(\omega\_{1},\ldots,\omega\_{i})-1]-\sum\limits\_{i=1}^{n}g\_{i}(\omega\_{1},\ldots,\omega\_{i}),\ n=\overline{1,N}. |  | (107) |

Let us put

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mn​(ω1,…,ωn)=f01+∑i=1nfi−11​(ω1,…,ωi−1)​[ξi0​(ω1,…,ωi)−1],n=1,N¯,formulae-sequencesubscript𝑀𝑛subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑓01superscriptsubscript𝑖1𝑛superscriptsubscript𝑓𝑖11subscript𝜔1…subscript𝜔𝑖1delimited-[]superscriptsubscript𝜉𝑖0subscript𝜔1…subscript𝜔𝑖1𝑛¯  1𝑁\displaystyle M\_{n}(\omega\_{1},\ldots,\omega\_{n})=f\_{0}^{1}+\sum\limits\_{i=1}^{n}f\_{i-1}^{1}(\omega\_{1},\ldots,\omega\_{i-1})[\xi\_{i}^{0}(\omega\_{1},\ldots,\omega\_{i})-1],\quad n=\overline{1,N}, |  | (108) |

then EQ​{Mn​(ω1,…,ωn)|ℱn−1}=Mn−1​(ω1,…,ωn−1).superscript𝐸𝑄conditional-setsubscript𝑀𝑛subscript𝜔1…subscript𝜔𝑛subscriptℱ𝑛1subscript𝑀𝑛1subscript𝜔1…subscript𝜔𝑛1E^{Q}\{M\_{n}(\omega\_{1},\ldots,\omega\_{n})|{\cal F}\_{n-1}\}=M\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1}). Theorem [5](#Thmte5 "Theorem 5. ‣ 5 Optional decomposition for super-martingales.") is proved.
∎

## 6 Spot measures and integral representation for martingale measures.

In this section, we introduce the family of spot measures. After that, we obtain the representations for the family of spot measures and define integral over these set of measures. The sufficient conditions are found, under which the integral over these set of measures is a set of martingale measures being equivalent to the initial measure. The introduced family of spot measures is a family
of extreme points for these set of equivalent measures.

We give an evident construction of the set of martingale measures for risky assets evolution, given by the formula ([9](#S2.E9 "In 2 Evolutions of risky assets.")). First of all, to do that we consider a simple case as the measures Pn0superscriptsubscript𝑃𝑛0P\_{n}^{0} is concentrated at two points ωn1,ωn2∈Ωn0,

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2
superscriptsubscriptΩ𝑛0\omega\_{n}^{1},\omega\_{n}^{2}\in\Omega\_{n}^{0}, where ωn1∈An0​k−,ωn2∈An0​k+formulae-sequencesuperscriptsubscript𝜔𝑛1superscriptsubscript𝐴𝑛limit-from0𝑘superscriptsubscript𝜔𝑛2superscriptsubscript𝐴𝑛limit-from0𝑘\omega\_{n}^{1}\in A\_{n}^{0k-},\omega\_{n}^{2}\in A\_{n}^{0k+} for a certain k,𝑘k, depending on n,𝑛n, for the representation Ωn−superscriptsubscriptΩ𝑛\Omega\_{n}^{-} and Ωn+,superscriptsubscriptΩ𝑛\Omega\_{n}^{+}, given by the formula ([5](#S2.E5 "In 2 Evolutions of risky assets.")). Let us put Pn0​(ωn1)=pnk,superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1superscriptsubscript𝑝𝑛𝑘P\_{n}^{0}(\omega\_{n}^{1})=p\_{n}^{k}, Pn0​(ωn2)=1−pnk,superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛21superscriptsubscript𝑝𝑛𝑘P\_{n}^{0}(\omega\_{n}^{2})=1-p\_{n}^{k}, where 0<pnk<1.0superscriptsubscript𝑝𝑛𝑘10<p\_{n}^{k}<1. Then, to satisfy the conditions
([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")), we need to put

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​({ω11,…,ωn1};{ω12,…,ωn2})=1pnk​(1−pnk),n=1,N¯,formulae-sequencesubscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛21superscriptsubscript𝑝𝑛𝑘1superscriptsubscript𝑝𝑛𝑘𝑛¯  1𝑁\displaystyle\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})=\frac{1}{p\_{n}^{k}(1-p\_{n}^{k})},\quad n=\overline{1,N}, |  | (109) |

and to require that

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)<∞,(ω1,…,ωn−1,ωn1)∈Ωn−,formulae-sequenceΔsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})<\infty,\quad(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\in\Omega\_{n}^{-}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)<∞,(ω1,…,ωn−1,ωn2)∈Ωn+.formulae-sequenceΔsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛\displaystyle\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})<\infty,\quad(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\in\Omega\_{n}^{+}. |  | (110) |

Let us denote μ{ωn1,ωn2},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) the measure, generated by the recurrent relations ([23](#S3.E23 "In 3 Construction of the set of martingale measures.")) - ([25](#S3.E25 "In 3 Construction of the set of martingale measures.")), for the measures Pn0,n=1,N¯,

superscriptsubscript𝑃𝑛0𝑛
¯

1𝑁P\_{n}^{0},\ n=\overline{1,N}, concentrated at two points.
For the point {ωn1,ωn2},…,{ωN1,ωN2}∈ΩN×ΩN,

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2
subscriptΩ𝑁subscriptΩ𝑁\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}\in\Omega\_{N}\times\Omega\_{N},
the recurrent relations ([23](#S3.E23 "In 3 Construction of the set of martingale measures.")) - ([25](#S3.E25 "In 3 Construction of the set of martingale measures.")) is converted
relative to the set of measures μ{ωn1,ωn2},…,{ωN1,ωN2}(ω1,…,ωn−1)​(A)superscriptsubscript𝜇

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑛1𝐴\mu\_{\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A) into the recurrent relations

|  |  |  |
| --- | --- | --- |
|  | μ{ωN1,ωN2}(ω1,…,ωN−1)(A)=χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\mu\_{\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A)=\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)μN(ω1,…,ωN−1,ωN1)(A)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)μN(ω1,…,ωN−1,ωN2)(A)],A∈ℱN,\displaystyle\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}(A)\right],\quad A\in{\cal F}\_{N}, |  | (111) |

|  |  |  |
| --- | --- | --- |
|  | μ{ωn1,ωn2},…,{ωN1,ωN2}(ω1,…,ωn−1)(A)=χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\mu\_{\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A)=\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωn1)(A)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωn2)(A)],n=2,N¯,A∈ℱN,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right],\quad n=\overline{2,N},\quad A\in{\cal F}\_{N}, |  | (112) |

|  |  |  |
| --- | --- | --- |
|  | μ{ωn1,ωn2},…,{ωN1,ωN2}(A)=χΩ1−(ω11)χΩ1+(ω12)×\mu\_{\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A)=\chi\_{\Omega\_{1}^{-}}(\omega\_{1}^{1})\chi\_{\Omega\_{1}^{+}}(\omega\_{1}^{2})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | [Δ​S1+​(ωn2)V1​(ω11,ω12)​μ{ω21,ω22},…,{ωN1,ωN2}(ω11)​(A)+Δ​S1−​(ω11)V1​(ω11,ω12)​μ{ω21,ω22},…,{ωN1,ωN2}(ω12)​(A)],delimited-[]Δsuperscriptsubscript𝑆1superscriptsubscript𝜔𝑛2subscript𝑉1superscriptsubscript𝜔11superscriptsubscript𝜔12superscriptsubscript𝜇  superscriptsubscript𝜔21superscriptsubscript𝜔22…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2superscriptsubscript𝜔11𝐴Δsuperscriptsubscript𝑆1superscriptsubscript𝜔11subscript𝑉1superscriptsubscript𝜔11superscriptsubscript𝜔12superscriptsubscript𝜇  superscriptsubscript𝜔21superscriptsubscript𝜔22…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2superscriptsubscript𝜔12𝐴\displaystyle\left[\frac{\Delta S\_{1}^{+}(\omega\_{n}^{2})}{V\_{1}(\omega\_{1}^{1},\omega\_{1}^{2})}\mu\_{\{\omega\_{2}^{1},\omega\_{2}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1}^{1})}(A)+\frac{\Delta S\_{1}^{-}(\omega\_{1}^{1})}{V\_{1}(\omega\_{1}^{1},\omega\_{1}^{2})}\mu\_{\{\omega\_{2}^{1},\omega\_{2}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1}^{2})}(A)\right], |  | (113) |

where we put

|  |  |  |  |
| --- | --- | --- | --- |
|  | μN(ω1,…,ωN−1,ωN)​(A)=χA​(ω1,…,ωN−1,ωN),A∈ℱN.formulae-sequencesuperscriptsubscript𝜇𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁𝐴subscriptℱ𝑁\displaystyle\mu\_{N}^{(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})}(A)=\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}),\quad A\in{\cal F}\_{N}. |  | (114) |

The recurrent relations ([111](#S6.E111 "In 6 Spot measures and integral representation for martingale measures.")) - ([113](#S6.E113 "In 6 Spot measures and integral representation for martingale measures.")) we call the recurrent relations for the spot measures μ{ωn1,ωn2},…,{ωN1,ωN2}​(A).subscript𝜇

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A).

Let us consider the random values

|  |  |  |
| --- | --- | --- |
|  | ψn​(ω1,…,ωn)=χΩn−​(ω1,…,ωn−1,ωn)​ψn1​(ω1,…,ωn)+subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛limit-fromsubscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})=\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})+ |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΩn+​(ω1,…,ωn−1,ωn)​ψn2​(ω1,…,ωn),subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛\displaystyle\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n}), |  | (115) |

where

|  |  |  |
| --- | --- | --- |
|  | ψn1(ω1,…,ωn−1,ωn)=χΩn+(ω1,…,ωn−1,ωn2)×\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})=\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2),(ω1,…,ωn−1)∈Ωn−1,  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (116) |

|  |  |  |
| --- | --- | --- |
|  | ψn2(ω1,…,ωn−1,ωn)=χΩn−(ω1,…,ωn−1,ωn1)×\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})=\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2),(ω1,…,ωn−1)∈Ωn−1.  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}. |  | (117) |

###### Lemma 6.

For the spot measure μ{ω11,ω12},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) the representation

|  |  |  |
| --- | --- | --- |
|  | μ{ω11,ω12},…,{ωN1,ωN2}​(A)=subscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴absent\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i1=12…​∑iN=12∏j=1Nψj​(ω1i1,…,ωjij)​χA​(ω1i1,…,ωNiN),A∈ℱN,  superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐴superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁𝐴 subscriptℱ𝑁\displaystyle\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{A}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}}),\quad A\in{\cal F}\_{N}, |  | (118) |

is true.

###### Proof.

The proof of Lemma [6](#Thmleme6 "Lemma 6. ‣ 6 Spot measures and integral representation for martingale measures.") we lead by induction down. Let us prove the equality

|  |  |  |
| --- | --- | --- |
|  | μ{ωN1,ωN2}(ω1,…,ωN−1)​(A)=superscriptsubscript𝜇superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑁1𝐴absent\mu\_{\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑iN=12ψN​(ω1,…,ωN−1,ωNiN)​χA​(ω1,…,ωN−1,ωNiN).superscriptsubscriptsubscript𝑖𝑁12subscript𝜓𝑁subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁\displaystyle\sum\limits\_{i\_{N}=1}^{2}\psi\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}}). |  | (119) |

Really,

|  |  |  |
| --- | --- | --- |
|  | ψN​(ω1,…,ωN−1,ωN1)​χA​(ω1,…,ωN−1,ωN1)+limit-fromsubscript𝜓𝑁subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1\psi\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+ |  |

|  |  |  |
| --- | --- | --- |
|  | ψN​(ω1,…,ωN−1,ωN2)​χA​(ω1,…,ωN−1,ωN2)=subscript𝜓𝑁subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2absent\psi\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | [χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)+\left[\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN1)Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)]×\left.\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\right]\times |  |

|  |  |  |
| --- | --- | --- |
|  | χA​(ω1,…,ωN−1,ωN1)+limit-fromsubscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+ |  |

|  |  |  |
| --- | --- | --- |
|  | [χΩN−(ω1,…,ωN−1,ωN2)χΩN+(ω1,…,ωN−1,ωN2)Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)+\left[\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)]×\left.\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\right]\times |  |

|  |  |  |
| --- | --- | --- |
|  | χA​(ω1,…,ωN−1,ωN2)=subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2absent\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN1)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN2)],A∈ℱN.\displaystyle\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\right],\quad A\in{\cal F}\_{N}. |  | (120) |

The last prove the needed. Suppose that we proved that the equality

|  |  |  |
| --- | --- | --- |
|  | μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωn)​(A)=superscriptsubscript𝜇  superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛𝐴absent\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})}(A)= |  |

|  |  |  |
| --- | --- | --- |
|  | ∑in+1=12…​∑iN=12∏j=n+1Nψj​(ω1,…,ωn,ωn+1in+1,…,ωjij)​χA​(ω1,…,ωn,ωn+1in+1,…,ωNiN),superscriptsubscriptsubscript𝑖𝑛112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗𝑛1𝑁subscript𝜓𝑗subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝜔𝑛1subscript𝑖𝑛1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝜔𝑛1subscript𝑖𝑛1…superscriptsubscript𝜔𝑁subscript𝑖𝑁\sum\limits\_{i\_{n+1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=n+1}^{N}\psi\_{j}(\omega\_{1},\ldots,\omega\_{n},\omega\_{n+1}^{i\_{n+1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{A}(\omega\_{1},\ldots,\omega\_{n},\omega\_{n+1}^{i\_{n+1}},\ldots,\omega\_{N}^{i\_{N}}), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | A∈ℱN,𝐴subscriptℱ𝑁\displaystyle A\in{\cal F}\_{N}, |  | (121) |

is true. By the same way as above, we have

|  |  |  |
| --- | --- | --- |
|  | ∑in=12ψn​(ω1,…,ωn−1,ωnin)​μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωnin)​(A)=superscriptsubscriptsubscript𝑖𝑛12subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛subscript𝑖𝑛superscriptsubscript𝜇  superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛subscript𝑖𝑛𝐴absent\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{i\_{n}})\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{i\_{n}})}(A)= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωn1)(A)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωn2)(A)]=\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right]= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ{ωn1,ωn2},…,{ωN1,ωN2}(ω1,…,ωn−1)​(A),A∈ℱN.  superscriptsubscript𝜇  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑛1𝐴𝐴 subscriptℱ𝑁\displaystyle\mu\_{\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A),\quad A\in{\cal F}\_{N}. |  | (122) |

The last proves Lemma [6](#Thmleme6 "Lemma 6. ‣ 6 Spot measures and integral representation for martingale measures.").
∎

Let us define the integral for the random value fN​(ω1,…,ωN−1,ωN)subscript𝑓𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁f\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}) relative to the measure μ{ω11,ω12},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) by the formula

|  |  |  |
| --- | --- | --- |
|  | ∫ΩNfN​(ω1,…,ωN−1,ωN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}=subscriptsubscriptΩ𝑁subscript𝑓𝑁subscript𝜔1…subscript𝜔𝑁1subscript𝜔𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2absent\int\limits\_{\Omega\_{N}}f\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i1=12…​∑iN=12∏j=1Nψj​(ω1i1,…,ωjij)​fN​(ω1i1,…,ωNiN).superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝑓𝑁superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁\displaystyle\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})f\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}}). |  | (123) |

To describe the convex set of equivalent martingale measures, we introduce the family of α𝛼\alpha-spot measures, depending on the point ({ω11,{ω12},…,{ωN1,{ωN2})(\{\omega\_{1}^{1},\{\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\{\omega\_{N}^{2}\}) belonging to ΩN×ΩNsubscriptΩ𝑁subscriptΩ𝑁\Omega\_{N}\times\Omega\_{N} and the set of strictly positive random values

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2}),n=1,N¯,  subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2𝑛 ¯  1𝑁\displaystyle\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}),\quad n=\overline{1,N}, |  | (124) |

at points Wn=({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝑊𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2W\_{n}=(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), being constructed by the point ({ω11,ω12},…,{ωN1,ωN2}).superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2(\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}).

Further, in this section, we assume that the evolution of risky asset is given by the formula ([9](#S2.E9 "In 2 Evolutions of risky assets.")). Therefore, in this case

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωn−=Ωn0−×Ωn−1,Ωn+=Ωn0+×Ωn−1,n=1,N¯,formulae-sequencesuperscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛limit-from0subscriptΩ𝑛1formulae-sequencesuperscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛limit-from0subscriptΩ𝑛1𝑛¯  1𝑁\displaystyle\Omega\_{n}^{-}=\Omega\_{n}^{0-}\times\Omega\_{n-1},\quad\Omega\_{n}^{+}=\Omega\_{n}^{0+}\times\Omega\_{n-1},\quad n=\overline{1,N}, |  | (125) |

and the condition ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")) is formulated, as follows:

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn0−(ωn1)χΩn0+(ωn2)αn({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{0-}}(\omega\_{n}^{1})\chi\_{\Omega\_{n}^{0+}}(\omega\_{n}^{2})\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Pn0​(ωn1)​d​Pn0​(ωn2)=1,n=1,N¯.formulae-sequence𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛21𝑛¯  1𝑁\displaystyle dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})=1,\quad n=\overline{1,N}. |  | (126) |

Let us determine the random values

|  |  |  |
| --- | --- | --- |
|  | ψnα​(ω1,…,ωn)=χΩn−​(ω1,…,ωn−1,ωn)​ψn1​(ω1,…,ωn)+superscriptsubscript𝜓𝑛𝛼subscript𝜔1…subscript𝜔𝑛limit-fromsubscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛\psi\_{n}^{\alpha}(\omega\_{1},\ldots,\omega\_{n})=\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})+ |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΩn+​(ω1,…,ωn−1,ωn)​ψn2​(ω1,…,ωn),subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛\displaystyle\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n}), |  | (127) |

|  |  |  |
| --- | --- | --- |
|  | ψn1​(ω1,…,ωn−1,ωn)=superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})χΩn+(ω1,…,ωn−1,ωn2)×\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2),(ω1,…,ωn−1)∈Ωn−1,  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (128) |

|  |  |  |
| --- | --- | --- |
|  | ψn2​(ω1,…,ωn−1,ωn)=superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})= |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})χΩn−(ω1,…,ωn−1,ωn1)×\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2),(ω1,…,ωn−1)∈Ωn−1.  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}. |  | (129) |

Let us define the set of α𝛼\alpha-spot measures on the σ𝜎\sigma-algebra ℱNsubscriptℱ𝑁{\cal F}\_{N} by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | μWNα​(A)=∑i1=12…​∑iN=12∏j=1Nψjα​(ω1i1,…,ωjij)​χA​(ω1i1,…,ωNiN),A∈ℱN,formulae-sequencesubscriptsuperscript𝜇𝛼subscript𝑊𝑁𝐴superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁superscriptsubscript𝜓𝑗𝛼superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐴superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁𝐴subscriptℱ𝑁\displaystyle\mu^{\alpha}\_{W\_{N}}(A)=\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}^{\alpha}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{A}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}}),\quad A\in{\cal F}\_{N}, |  | (130) |

and the set of the measures

|  |  |  |
| --- | --- | --- |
|  | μ0​(A)=subscript𝜇0𝐴absent\mu\_{0}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN×ΩN∑i1=12…​∑iN=12∏j=1Nψjα​(ω1i1,…,ωjij)​χA​(ω1i1,…,ωNiN)​d​PN×d​PN,A∈ℱN.  subscriptsubscriptΩ𝑁subscriptΩ𝑁superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁superscriptsubscript𝜓𝑗𝛼superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐴superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁𝑑subscript𝑃𝑁𝑑subscript𝑃𝑁𝐴 subscriptℱ𝑁\displaystyle\int\limits\_{\Omega\_{N}\times\Omega\_{N}}\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}^{\alpha}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{A}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}})dP\_{N}\times dP\_{N},\ A\in{\cal F}\_{N}. |  | (131) |

###### Theorem 6.

Suppose that the conditions of Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.")
are true. If the strictly positive random values

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​({ω11,…,ωn1};{ω12,…,ωn2}),n=1,N¯,  subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2𝑛 ¯  1𝑁\displaystyle\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}),\ n=\overline{1,N}, |  | (132) |

given on the
probability space {Ωn×Ωn,ℱn×ℱn,Pn×Pn},n=1,N¯,

subscriptΩ𝑛subscriptΩ𝑛subscriptℱ𝑛subscriptℱ𝑛subscript𝑃𝑛subscript𝑃𝑛𝑛
¯

1𝑁\{\Omega\_{n}\times\Omega\_{n},{\cal F}\_{n}\times{\cal F}\_{n},P\_{n}\times P\_{n}\},\ n=\overline{1,N},
satisfy the conditions ([126](#S6.E126 "In 6 Spot measures and integral representation for martingale measures.")),
then for the measure μ0​(A),subscript𝜇0𝐴\mu\_{0}(A), given by the formula ([131](#S6.E131 "In 6 Spot measures and integral representation for martingale measures.")),
the representation

|  |  |  |
| --- | --- | --- |
|  | μ0​(A)=subscript𝜇0𝐴absent\mu\_{0}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN×ΩN∏i=1Nαi​({ω11,…,ωi1};{ω12,…,ωi2})​μ{ω11,ω12},…,{ωN1,ωN2}​(A)​d​PN×d​PNsubscriptsubscriptΩ𝑁subscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝛼𝑖  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑖1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑖2 subscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴𝑑subscript𝑃𝑁𝑑subscript𝑃𝑁\displaystyle\int\limits\_{\Omega\_{N}\times\Omega\_{N}}\prod\limits\_{i=1}^{N}\alpha\_{i}(\{\omega\_{1}^{1},\ldots,\omega\_{i}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{i}^{2}\})\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A)dP\_{N}\times dP\_{N} |  | (133) |

is true.

###### Proof.

Due to Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures."), the set of random values αn​({ω11,…,ωn1};{ω12,…,ωn2}),subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}), n=1,N¯,𝑛¯

1𝑁\ n=\overline{1,N}, satisfying the conditions ([126](#S6.E126 "In 6 Spot measures and integral representation for martingale measures.")), is a non empty set.

We prove Theorem [6](#Thmte6 "Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures.") by induction down. For the spot measure the relation

|  |  |  |
| --- | --- | --- |
|  | μ{ωN1,ωN2}(ω1,…,ωN−1)​(A)=superscriptsubscript𝜇superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑁1𝐴absent\mu\_{\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A)= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN1)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN2)],A∈ℱN,\displaystyle\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\right],\quad A\in{\cal F}\_{N}, |  | (134) |

is true.
Multiplying the relation ([134](#S6.E134 "In Proof. ‣ 6 Spot measures and integral representation for martingale measures.")) on αN​({ω11,…,ωN−11,ωN1};{ω12,…,ωN−12,ωN2})subscript𝛼𝑁

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁11superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁12superscriptsubscript𝜔𝑁2\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N-1}^{1},\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N-1}^{2},\omega\_{N}^{2}\}) and after that,
integrating relative to the measure PN0×PN0superscriptsubscript𝑃𝑁0superscriptsubscript𝑃𝑁0P\_{N}^{0}\times P\_{N}^{0} on the set ΩN0×ΩN0,superscriptsubscriptΩ𝑁0superscriptsubscriptΩ𝑁0\Omega\_{N}^{0}\times\Omega\_{N}^{0}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0∫ΩN0αN({ω11,…,ωN−11,ωN1};{ω12,…,ωN−12,ωN2})×\int\limits\_{\Omega\_{N}^{0}}\int\limits\_{\Omega\_{N}^{0}}\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N-1}^{1},\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N-1}^{2},\omega\_{N}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | μ{ωN1,ωN2}(ω1,…,ωN−1)​(A)​d​PN0​(ωN1)​d​PN0​(ωN2)=superscriptsubscript𝜇superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑁1𝐴𝑑superscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁1𝑑superscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁2absent\mu\_{\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A)dP\_{N}^{0}(\omega\_{N}^{1})dP\_{N}^{0}(\omega\_{N}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0∫ΩN0αN({ω11,…,ωN−11,ωN1};{ω12,…,ωN−12,ωN2})×\int\limits\_{\Omega\_{N}^{0}}\int\limits\_{\Omega\_{N}^{0}}\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N-1}^{1},\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N-1}^{2},\omega\_{N}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN1)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN2)]dPN0(ωN1)dPN0(ωN2)=\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\right]dP\_{N}^{0}(\omega\_{N}^{1})dP\_{N}^{0}(\omega\_{N}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μN−1(ω1,…,ωN−1)​(A),A∈ℱN.  superscriptsubscript𝜇𝑁1subscript𝜔1…subscript𝜔𝑁1𝐴𝐴 subscriptℱ𝑁\displaystyle\mu\_{N-1}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A),\quad A\in{\cal F}\_{N}. |  | (135) |

Suppose that we proved the equality

|  |  |  |
| --- | --- | --- |
|  | ∫∏i=n+1N[Ωi0×Ωi0]∏i=n+1Nαi({ω11,…,ωn1,ωn+11,…,ωi1};{ω12,…,ωn2,ωn+12,…,ωi2})×\int\limits\_{\prod\limits\_{i=n+1}^{N}[\Omega\_{i}^{0}\times\Omega\_{i}^{0}]}\prod\limits\_{i=n+1}^{N}\alpha\_{i}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1},\omega\_{n+1}^{1},\ldots,\omega\_{i}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2},\omega\_{n+1}^{2},\ldots,\omega\_{i}^{2}\})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn)​(A)​∏i=n+1Nd​Pi0​(ωi1)​d​Pi0​(ωi2)=μn(ω1,…,ωn)​(A).superscriptsubscript𝜇  superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑛𝐴superscriptsubscriptproduct𝑖𝑛1𝑁𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖1𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖2superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛𝐴\displaystyle\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n})}(A)\prod\limits\_{i=n+1}^{N}dP\_{i}^{0}(\omega\_{i}^{1})dP\_{i}^{0}(\omega\_{i}^{2})=\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n})}(A). |  | (136) |

Then, using the induction supposition ([136](#S6.E136 "In Proof. ‣ 6 Spot measures and integral representation for martingale measures.")), the relation for the spot measure

|  |  |  |
| --- | --- | --- |
|  | μ{ωn1,ωn2},…,{ωN1,ωN2}(ω1,…,ωn−1)​(A)=superscriptsubscript𝜇  superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜔1…subscript𝜔𝑛1𝐴absent\mu\_{\{\omega\_{n}^{1},\omega\_{n}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A)= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωn1)(A)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μ{ωn+11,ωn+12},…,{ωN1,ωN2}(ω1,…,ωn−1,ωn2)(A)],A∈ℱN,\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{\{\omega\_{n+1}^{1},\omega\_{n+1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right],\quad A\in{\cal F}\_{N}, |  | (137) |

and multiplying it on
∏i=nNαi​({ω11,…,ωn−11,ωn1,…,ωi1};{ω12,…,ωn−12,ωn2,…,ωi2})superscriptsubscriptproduct𝑖𝑛𝑁subscript𝛼𝑖

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1…superscriptsubscript𝜔𝑖1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2…superscriptsubscript𝜔𝑖2\prod\limits\_{i=n}^{N}\alpha\_{i}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1},\ldots,\omega\_{i}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2},\ldots,\omega\_{i}^{2}\}) and then integrating relative to the measure ∏i=nN[Pi0×Pi0]superscriptsubscriptproduct𝑖𝑛𝑁delimited-[]superscriptsubscript𝑃𝑖0superscriptsubscript𝑃𝑖0\prod\limits\_{i=n}^{N}[P\_{i}^{0}\times P\_{i}^{0}] on the set ∏i=nN[Ωi0×Ωi0],superscriptsubscriptproduct𝑖𝑛𝑁delimited-[]superscriptsubscriptΩ𝑖0superscriptsubscriptΩ𝑖0\prod\limits\_{i=n}^{N}[\Omega\_{i}^{0}\times\Omega\_{i}^{0}], we obtain the equality

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω11,…,ωn1};{ω12,…,ωn2})[Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn1)(A)+\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn2)(A)]dPn0(ωn1)dPn0(ωn2)=\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn−1(ω1,…,ωn−1)​(A),n=1,N¯.  superscriptsubscript𝜇𝑛1subscript𝜔1…subscript𝜔𝑛1𝐴𝑛 ¯  1𝑁\displaystyle\mu\_{n-1}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A),\quad n=\overline{1,N}. |  | (138) |

Thus, we proved the following recurrent relations

|  |  |  |
| --- | --- | --- |
|  | μn−1(ω1,…,ωn−1)(A)=∫Ωn0×Ωn0χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\mu\_{n-1}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A)=\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | αn({ω11,…,ωn1};{ω12,…,ωn2})[Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn1)(A)+\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn2)(A)]dPn0(ωn1)dPn0(ωn2),n=1,N¯.\displaystyle\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2}),\quad n=\overline{1,N}. |  | (139) |

To finish the proof of Theorem [6](#Thmte6 "Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures."), let us calculate

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN0×ΩN0∑iN=12ψNα​(ω1,…,ωN−1,ωNiN)​χA​(ω1,…,ωN−1,ωNiN)​d​PN0​(ωN1)​d​PN0​(ωN2).subscriptsuperscriptsubscriptΩ𝑁0superscriptsubscriptΩ𝑁0superscriptsubscriptsubscript𝑖𝑁12superscriptsubscript𝜓𝑁𝛼subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁𝑑superscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁1𝑑superscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁2\displaystyle\int\limits\_{\Omega\_{N}^{0}\times\Omega\_{N}^{0}}\sum\limits\_{i\_{N}=1}^{2}\psi\_{N}^{\alpha}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}})dP\_{N}^{0}(\omega\_{N}^{1})dP\_{N}^{0}(\omega\_{N}^{2}). |  | (140) |

Calculating the expression

|  |  |  |
| --- | --- | --- |
|  | ∑iN=12ψNα​(ω1,…,ωN−1,ωNiN)​χA​(ω1,…,ωN−1,ωNiN)=superscriptsubscriptsubscript𝑖𝑁12superscriptsubscript𝜓𝑁𝛼subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁absent\sum\limits\_{i\_{N}=1}^{2}\psi\_{N}^{\alpha}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}})= |  |

|  |  |  |
| --- | --- | --- |
|  | ψNα​(ω1,…,ωN−1,ωN1)​χA​(ω1,…,ωN−1,ωN1)+limit-fromsuperscriptsubscript𝜓𝑁𝛼subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁1\psi\_{N}^{\alpha}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+ |  |

|  |  |  |
| --- | --- | --- |
|  | ψNα​(ω1,…,ωN−1,ωN2)​χA​(ω1,…,ωN−1,ωN2)=superscriptsubscript𝜓𝑁𝛼subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁2absent\psi\_{N}^{\alpha}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | αN({ω11,…,ωN1};{ω12,…,ωN2})×\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | χΩN−(ω1,…,ωN−1,ωN1)χΩN+(ω1,…,ωN−1,ωN2)×\chi\_{\Omega\_{N}^{-}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})\chi\_{\Omega\_{N}^{+}}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​SN+​(ω1,…,ωN−1,ωN2)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN1)+\left[\frac{\Delta S\_{N}^{+}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​SN−​(ω1,…,ωN−1,ωN1)VN​(ω1,…,ωN−1,ωN1,ωN2)χA(ω1,…,ωN−1,ωN2)],A∈ℱN,\displaystyle\left.\frac{\Delta S\_{N}^{-}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1})}{V\_{N}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{1},\omega\_{N}^{2})}\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{2})\right],\quad A\in{\cal F}\_{N}, |  | (141) |

and substituting ([141](#S6.E141 "In Proof. ‣ 6 Spot measures and integral representation for martingale measures.")) into ([140](#S6.E140 "In Proof. ‣ 6 Spot measures and integral representation for martingale measures.")), we obtain the equality

|  |  |  |
| --- | --- | --- |
|  | ∫ΩN0×ΩN0∑iN=12ψNα​(ω1,…,ωN−1,ωNiN)​χA​(ω1,…,ωN−1,ωNiN)​d​PN0​(ωN1)​d​PN0​(ωN2)=subscriptsuperscriptsubscriptΩ𝑁0superscriptsubscriptΩ𝑁0superscriptsubscriptsubscript𝑖𝑁12superscriptsubscript𝜓𝑁𝛼subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁1superscriptsubscript𝜔𝑁subscript𝑖𝑁𝑑superscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁1𝑑superscriptsubscript𝑃𝑁0superscriptsubscript𝜔𝑁2absent\int\limits\_{\Omega\_{N}^{0}\times\Omega\_{N}^{0}}\sum\limits\_{i\_{N}=1}^{2}\psi\_{N}^{\alpha}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N-1},\omega\_{N}^{i\_{N}})dP\_{N}^{0}(\omega\_{N}^{1})dP\_{N}^{0}(\omega\_{N}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μN−1(ω1,…,ωN−1)​(A).superscriptsubscript𝜇𝑁1subscript𝜔1…subscript𝜔𝑁1𝐴\displaystyle\mu\_{N-1}^{(\omega\_{1},\ldots,\omega\_{N-1})}(A). |  | (142) |

Suppose that we already proved the equality

|  |  |  |
| --- | --- | --- |
|  | ∫∏i=n+1NΩi0×Ωi0∑in+1=12…​∑iN=12∏j=1Nψjα​(ω1,…,ωn,ωn+1in+1​…,ωjij)​∏i=n+1Nd​Pi0​(ωi1)​d​Pi0​(ωi2)=subscriptsuperscriptsubscriptproduct𝑖𝑛1𝑁superscriptsubscriptΩ𝑖0superscriptsubscriptΩ𝑖0superscriptsubscriptsubscript𝑖𝑛112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁superscriptsubscript𝜓𝑗𝛼subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝜔𝑛1subscript𝑖𝑛1…superscriptsubscript𝜔𝑗subscript𝑖𝑗superscriptsubscriptproduct𝑖𝑛1𝑁𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖1𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖2absent\int\limits\_{\prod\limits\_{i=n+1}^{N}\Omega\_{i}^{0}\times\Omega\_{i}^{0}}\sum\limits\_{i\_{n+1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}^{\alpha}(\omega\_{1},\ldots,\omega\_{n},\omega\_{n+1}^{i\_{n+1}}\ldots,\omega\_{j}^{i\_{j}})\prod\limits\_{i=n+1}^{N}dP\_{i}^{0}(\omega\_{i}^{1})dP\_{i}^{0}(\omega\_{i}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn(ω1,…,ωn)​(A).superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛𝐴\displaystyle\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n})}(A). |  | (143) |

Then, acting as above, we obtain the equalities

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0∑in=12ψnα​(ω1,…,ωn−1,ωnin)​μn(ω1,…,ωn−1,ωnin)​(A)​d​Pn0​(ωn1)​d​Pn0​(ωn2)=subscriptsuperscriptsubscriptΩ𝑛0superscriptsubscriptΩ𝑛0superscriptsubscriptsubscript𝑖𝑛12superscriptsubscript𝜓𝑛𝛼subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛subscript𝑖𝑛superscriptsubscript𝜇𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛subscript𝑖𝑛𝐴𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2absent\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}^{\alpha}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{i\_{n}})\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{i\_{n}})}(A)dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0×Ωn0αn({ω11,…,ωN1};{ω12,…,ωN2})×\int\limits\_{\Omega\_{n}^{0}\times\Omega\_{n}^{0}}\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | χΩn−(ω1,…,ωn−1,ωn1)χΩn+(ω1,…,ωn−1,ωn2)×\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn1)(A)+\left[\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}(A)+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)μn(ω1,…,ωn−1,ωn2)(A)]dPn0(ωn1)dPn0(ωn2)=\left.\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}\mu\_{n}^{(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}(A)\right]dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn−1(ω1,…,ωn−1)​(A),A∈ℱN.  superscriptsubscript𝜇𝑛1subscript𝜔1…subscript𝜔𝑛1𝐴𝐴 subscriptℱ𝑁\displaystyle\mu\_{n-1}^{(\omega\_{1},\ldots,\omega\_{n-1})}(A),\quad A\in{\cal F}\_{N}. |  | (144) |

We proved that the recurrent relations ([144](#S6.E144 "In Proof. ‣ 6 Spot measures and integral representation for martingale measures.")) are the same as the recurrent relations ([139](#S6.E139 "In Proof. ‣ 6 Spot measures and integral representation for martingale measures.")).
This proves Theorem [6](#Thmte6 "Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures.").
∎

Let us introduce the denotations

|  |  |  |
| --- | --- | --- |
|  | μ{ω11,ω12},…,{ωN1,ωN2}​(ΩN)=∑i1=12…​∑iN=12∏j=1Nψj​(ω1i1,…,ωjij),subscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscriptΩ𝑁superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(\Omega\_{N})=\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}}), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | WN={ω11,…,ωN1;ω12,…,ωN2}={{ω}N1,{ω}N2}.subscript𝑊𝑁superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2\displaystyle W\_{N}=\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1};\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\}=\{\{\omega\}\_{N}^{1},\{\omega\}\_{N}^{2}\}. |  | (145) |

Further, only those points ({ω11,ω12},…,{ωN1,ωN2})∈ΩN×ΩNsuperscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscriptΩ𝑁subscriptΩ𝑁(\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\})\in\Omega\_{N}\times\Omega\_{N} play important role for which
μ{ω11,ω12},…,{ωN1,ωN2}​(ΩN)≠0.subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2subscriptΩ𝑁0\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(\Omega\_{N})\neq 0.

Below, in the next two Theorems, we assume that
the random value

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​({ω11,…,ωn1};{ω12,…,ωn2})subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\displaystyle\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}) |  | (146) |

given on the
probability space {Ωn×Ωn,ℱn×ℱn,Pn×Pn},n=1,N¯,

subscriptΩ𝑛subscriptΩ𝑛subscriptℱ𝑛subscriptℱ𝑛subscript𝑃𝑛subscript𝑃𝑛𝑛
¯

1𝑁\{\Omega\_{n}\times\Omega\_{n},{\cal F}\_{n}\times{\cal F}\_{n},P\_{n}\times P\_{n}\},\ n=\overline{1,N},
satisfy the conditions ([126](#S6.E126 "In 6 Spot measures and integral representation for martingale measures.")).

Under the above conditions, for the measure μ0​(A),subscript𝜇0𝐴\mu\_{0}(A), given by the formula ([133](#S6.E133 "In Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures.")), the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ0​(A)=∫ΩN∏n=1Nψn​(ω1,…,ωn)​χA​(ω1,…,ωN)​∏i=1Nd​Pi0​(ωi)subscript𝜇0𝐴subscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑛1𝑁subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛subscript𝜒𝐴subscript𝜔1…subscript𝜔𝑁superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖\displaystyle\mu\_{0}(A)=\int\limits\_{\Omega\_{N}}\prod\limits\_{n=1}^{N}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})\chi\_{A}(\omega\_{1},\ldots,\omega\_{N})\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i}) |  | (147) |

is true, where

|  |  |  |
| --- | --- | --- |
|  | ψn​(ω1,…,ωn)=χΩn−​(ω1,…,ωn−1,ωn)​ψn1​(ω1,…,ωn)+subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛limit-fromsubscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛1subscript𝜔1…subscript𝜔𝑛\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})=\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})+ |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΩn+​(ω1,…,ωn−1,ωn)​ψn2​(ω1,…,ωn),subscript𝜒superscriptsubscriptΩ𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝜓𝑛2subscript𝜔1…subscript𝜔𝑛\displaystyle\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n}), |  | (148) |

|  |  |  |
| --- | --- | --- |
|  | ψn1(ω1,…,ωn−1,ωn)=∫Ωn0χΩn+(ω1,…,ωn−1,ωn2)αn({ω11,…,ωn1};{ω12,…,ωn2})×\psi\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})=\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{+}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn2),(ω1,…,ωn−1)∈Ωn−1,  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{2}),\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (149) |

|  |  |  |
| --- | --- | --- |
|  | ψn2(ω1,…,ωn−1,ωn)=∫Ωn0χΩn−(ω1,…,ωn−1,ωn1)αn({ω11,…,ωn1};{ω12,…,ωn2})×\psi\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})=\int\limits\_{\Omega\_{n}^{0}}\chi\_{\Omega\_{n}^{-}}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn1),(ω1,…,ωn−1)∈Ωn−1.  Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1subscript𝜔1…subscript𝜔𝑛1 subscriptΩ𝑛1\displaystyle\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{1}),\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}. |  | (150) |

Due to the conditions ([126](#S6.E126 "In 6 Spot measures and integral representation for martingale measures.")) relative to the random values αn​({ω}n1;{ω}n2),subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωn0ψn​(ω1,…,ωn)​𝑑Pn0​(ωn)=1,n=1,N¯.formulae-sequencesubscriptsuperscriptsubscriptΩ𝑛0subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛differential-dsuperscriptsubscript𝑃𝑛0subscript𝜔𝑛1𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{n}^{0}}\psi\_{n}(\omega\_{1},\ldots,\omega\_{n})dP\_{n}^{0}(\omega\_{n})=1,\quad n=\overline{1,N}. |  | (151) |

for ψn​(ω1,…,ωn),subscript𝜓𝑛subscript𝜔1…subscript𝜔𝑛\psi\_{n}(\omega\_{1},\ldots,\omega\_{n}), given by the formula ([148](#S6.E148 "In 6 Spot measures and integral representation for martingale measures.")). The proof of the equalities ([151](#S6.E151 "In 6 Spot measures and integral representation for martingale measures.")) is the same as in Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures.").

###### Theorem 7.

Suppose that the conditions of Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") are true.
Then, the set of strictly positive random values αn​({ω}n1;{ω}n2),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}),n=\overline{1,N}, satisfying the conditions

|  |  |  |
| --- | --- | --- |
|  | Eμ0​|Δ​Sn​(ω1,…,ωn−1,ωn)|=superscript𝐸subscript𝜇0Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absentE^{\mu\_{0}}|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN∏i=1Nψi​(ω1,…,ωi)​|Δ​Sn​(ω1,…,ωn−1,ωn)|​∏i=1Nd​Pi0​(ωi)<∞,n=1,N¯,formulae-sequencesubscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{N}}\prod\limits\_{i=1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i})<\infty,\quad n=\overline{1,N}, |  | (152) |

is a non empty set for the measures μ0​(A),subscript𝜇0𝐴\mu\_{0}(A), given by the formula ([133](#S6.E133 "In Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures.")). The measure μ0​(A),subscript𝜇0𝐴\mu\_{0}(A), constructed by the
strictly positive random values αn​({ω}n1;{ω}n2),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}),n=\overline{1,N}, satisfying the conditions ([126](#S6.E126 "In 6 Spot measures and integral representation for martingale measures.")), ([152](#S6.E152 "In Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures.")) is a martingale measure for the evolution of risky asset, given by the formula ([9](#S2.E9 "In 2 Evolutions of risky assets.")). Every measure, belonging to the convex linear span of such measures, is also
martingale measure for the evolution of risky asset, given by the formula ([9](#S2.E9 "In 2 Evolutions of risky assets.")). They are equivalent to the measure PN.subscript𝑃𝑁P\_{N}.
The set of spot measures μ{ω11,ω12},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) is a set of martingale measures for the evolution of risky asset, given by the formula ([9](#S2.E9 "In 2 Evolutions of risky assets.")).

###### Proof.

The first fact, that the set of random values αn​({ω}n1;{ω}n2),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}),n=\overline{1,N}, satisfying the conditions ([126](#S6.E126 "In 6 Spot measures and integral representation for martingale measures.")), ([152](#S6.E152 "In Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures.")) is a non empty one, follows from Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.").
From the representation ([147](#S6.E147 "In 6 Spot measures and integral representation for martingale measures.")) for the set of measures μ0​(A)subscript𝜇0𝐴\mu\_{0}(A), given by the formula ([133](#S6.E133 "In Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures.")), as in the proof of Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures."), it is proved that this set of measures is a set of martingale measures being equivalent to the measure PN.subscript𝑃𝑁P\_{N}.

Let us prove the last statement of Theorem [7](#Thmte7 "Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures.").
Since for the spot measure μ{ω11,ω12},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) the representation

|  |  |  |
| --- | --- | --- |
|  | μ{ω11,ω12},…,{ωN1,ωN2}​(A)=subscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴absent\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i1=12…​∑iN=12∏j=1Nψj​(ω1i1,…,ωjij)​χA​(ω1i1,…,ωNiN),A∈ℱN,  superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐴superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁𝐴 subscriptℱ𝑁\displaystyle\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{A}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}}),\quad A\in{\cal F}\_{N}, |  | (153) |

is true, let us calculate

|  |  |  |
| --- | --- | --- |
|  | ∑ij=12ψj​(ω1i1,…,ωjij)=ψj​(ω1i1,…,ωj−1ij−1,ωj1)+ψj​(ω1i1,…,ωj−1ij−1,ωj2)=superscriptsubscriptsubscript𝑖𝑗12subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2absent\sum\limits\_{i\_{j}=1}^{2}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})=\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})+\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj−​(ω1i1,…,ωj−1ij−1,ωj1)​ψj1​(ω1i1,…,ωj−1ij−1​ωj1)+limit-fromsubscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜓𝑗1superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\psi\_{j}^{1}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}}\omega\_{j}^{1})+ |  |

|  |  |  |
| --- | --- | --- |
|  | χΩn+​(ω1i1,…,ωj−1ij−1,ωj1)​ψj2​(ω1i1,…,ωj−1ij−1​ωj1)+limit-fromsubscript𝜒superscriptsubscriptΩ𝑛superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜓𝑗2superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1\chi\_{\Omega\_{n}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\psi\_{j}^{2}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}}\omega\_{j}^{1})+ |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj−​(ω1i1,…,ωj−1ij−1,ωj2)​ψj1​(ω1i1,…,ωj−1ij−1​ωj2)+limit-fromsubscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2superscriptsubscript𝜓𝑗1superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\psi\_{j}^{1}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}}\omega\_{j}^{2})+ |  |

|  |  |  |
| --- | --- | --- |
|  | χΩn+​(ω1i1,…,ωj−1ij−1,ωj2)​ψj2​(ω1i1,…,ωj−1ij−1​ωj2)=subscript𝜒superscriptsubscriptΩ𝑛superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2superscriptsubscript𝜓𝑗2superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2absent\chi\_{\Omega\_{n}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\psi\_{j}^{2}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}}\omega\_{j}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj−​(ω1i1,…,ωj−1ij−1,ωj1)​χΩj+​(ω1i1,…,ωj−1ij−1,ωj2)​Δ​Sj+​(ω1i1,…,ωj−1ij−1,ωj2)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj2)+limit-fromsubscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2Δsuperscriptsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2subscript𝑉𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜔𝑗2\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\frac{\Delta S\_{j}^{+}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{2})}+ |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj+​(ω1i1,…,ωj−1ij−1,ωj1)​χΩj−​(ω1i1,…,ωj−1ij−1,ωj1)​Δ​Sj−​(ω1i1,…,ωj−1ij−1,ωj1)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj1)+limit-fromsubscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1Δsuperscriptsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝑉𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜔𝑗1\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\frac{\Delta S\_{j}^{-}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{1})}+ |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj−​(ω1i1,…,ωj−1ij−1,ωj2)​χΩj+​(ω1i1,…,ωj−1ij−1,ωj2)​Δ​Sj+​(ω1i1,…,ωj−1ij−1,ωj2)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj2)+limit-fromsubscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2Δsuperscriptsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2subscript𝑉𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜔𝑗2\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\frac{\Delta S\_{j}^{+}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{2})}+ |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj+​(ω1i1,…,ωj−1ij−1,ωj2)​χΩj−​(ω1i1,…,ωj−1ij−1,ωj1)​Δ​Sj−​(ω1i1,…,ωj−1ij−1,ωj1)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj1)=subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1Δsuperscriptsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝑉𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜔𝑗1absent\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\frac{\Delta S\_{j}^{-}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{1})}= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj−​(ω1i1,…,ωj−1ij−1,ωj1)​χΩj+​(ω1i1,…,ωj−1ij−1,ωj2)​Δ​Sj+​(ω1i1,…,ωj−1ij−1,ωj2)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj2)+limit-fromsubscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2Δsuperscriptsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2subscript𝑉𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜔𝑗2\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\frac{\Delta S\_{j}^{+}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{2})}+ |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj+​(ω1i1,…,ωj−1ij−1,ωj2)​χΩj−​(ω1i1,…,ωj−1ij−1,ωj1)​Δ​Sj−​(ω1i1,…,ωj−1ij−1,ωj1)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj1)=subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1Δsuperscriptsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝑉𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1superscriptsubscript𝜔𝑗1absent\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\frac{\Delta S\_{j}^{-}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{1})}= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj−​(ω1i1,…,ωj−1ij−1,ωj1)​χΩj+​(ω1i1,…,ωj−1ij−1,ωj2)=χΩj0−​(ωj1)​χΩj0+​(ωj2)=subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1subscript𝜒superscriptsubscriptΩ𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2subscript𝜒superscriptsubscriptΩ𝑗limit-from0superscriptsubscript𝜔𝑗1subscript𝜒superscriptsubscriptΩ𝑗limit-from0superscriptsubscript𝜔𝑗2absent\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})=\chi\_{\Omega\_{j}^{0-}}(\omega\_{j}^{1})\chi\_{\Omega\_{j}^{0+}}(\omega\_{j}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {1,ωj1∈Ωj0−ωj2∈Ωj0+,0,otherwise,,j=1,N¯.  cases1superscriptsubscript𝜔𝑗1superscriptsubscriptΩ𝑗limit-from0superscriptsubscript𝜔𝑗2superscriptsubscriptΩ𝑗limit-from0missing-subexpression0otherwise,missing-subexpressionmissing-subexpression𝑗 ¯  1𝑁\displaystyle\left\{\begin{array}[]{l l l l}1,&\omega\_{j}^{1}\in\Omega\_{j}^{0-}&\omega\_{j}^{2}\in\Omega\_{j}^{0+},\\ 0,&\mbox{otherwise,}\end{array}\right.,\quad j=\overline{1,N}. |  | (156) |

Further,

|  |  |  |
| --- | --- | --- |
|  | ∑ij=12ψj​(ω1i1,…,ωjij)​Δ​Sj​(ω1i1,…,ωjij)=superscriptsubscriptsubscript𝑖𝑗12subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗Δsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗absent\sum\limits\_{i\_{j}=1}^{2}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\Delta S\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})= |  |

|  |  |  |
| --- | --- | --- |
|  | ψj​(ω1i1,…,ωj−1ij−1,ωj1)​Δ​Sj​(ω1i1,…,ωj−1ij−1,ωj1)+limit-fromsubscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1Δsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗1\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\Delta S\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})+ |  |

|  |  |  |
| --- | --- | --- |
|  | ψj​(ω1i1,…,ωj−1ij−1,ωj2)​Δ​Sj​(ω1i1,…,ωj−1ij−1,ωj2)=subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2Δsubscript𝑆𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗1subscript𝑖𝑗1superscriptsubscript𝜔𝑗2absent\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\Delta S\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})= |  |

|  |  |  |
| --- | --- | --- |
|  | χΩj−(ω1i1,…,ωj−1ij−1,ωj1)χΩj+(ω1i1,…,ωj−1ij−1,ωj2)×\chi\_{\Omega\_{j}^{-}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})\chi\_{\Omega\_{j}^{+}}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\times |  |

|  |  |  |
| --- | --- | --- |
|  | [−Δ​Sj+​(ω1i1,…,ωj−1ij−1,ωj2)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj2)ΔSj−(ω1i1,…,ωj−1ij−1,ωj1)+\left[-\frac{\Delta S\_{j}^{+}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{2})}\Delta S\_{j}^{-}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})+\right. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Sj−​(ω1i1,…,ωj−1ij−1,ωj1)Vj​(ω1i1,…,ωj−1ij−1,ωj1,ωj1)ΔSj+(ω1i1,…,ωj−1ij−1,ωj2)]=0,j=1,N¯.\displaystyle\left.\frac{\Delta S\_{j}^{-}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1})}{V\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{1},\omega\_{j}^{1})}\Delta S\_{j}^{+}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j-1}^{i\_{j-1}},\omega\_{j}^{2})\right]=0,\quad j=\overline{1,N}. |  | (157) |

Let us prove that the set of measures μ{ω11,ω12},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) is a set of martingale measures.
Really, for A,𝐴A, belonging to the σ𝜎\sigma-algebra ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1} of the filtration we have A=B×∏i=nNΩi0,𝐴𝐵superscriptsubscriptproduct𝑖𝑛𝑁superscriptsubscriptΩ𝑖0A=B\times\prod\limits\_{i=n}^{N}\Omega\_{i}^{0}, where B𝐵B belongs to σ𝜎\sigma-algebra ℱn−1subscriptℱ𝑛1{\cal F}\_{n-1} of the measurable space {Ωn−1,ℱn−1}.subscriptΩ𝑛1subscriptℱ𝑛1\{\Omega\_{n-1},{\cal F}\_{n-1}\}. Then,

|  |  |  |
| --- | --- | --- |
|  | ∫AΔ​Sn​(ω1,…,ωn)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}=subscript𝐴Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2absent\int\limits\_{A}\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}= |  |

|  |  |  |
| --- | --- | --- |
|  | ∑i1=12…​∑iN=12∏j=1Nψj​(ω1i1,…,ωjij)​χB​(ω1i1,…,ωn−1in−1)​Δ​Sn​(ω1i1,…,ωnin)=superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐵superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑛1subscript𝑖𝑛1Δsubscript𝑆𝑛superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑛subscript𝑖𝑛absent\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{B}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{n-1}^{i\_{n-1}})\Delta S\_{n}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{n}^{i\_{n}})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∑i1=12…​∑in=12∏j=1nψj​(ω1i1,…,ωjij)​χB​(ω1i1,…,ωn−1in−1)​Δ​Sn​(ω1i1,…,ωnin)=superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑛12superscriptsubscriptproduct𝑗1𝑛subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐵superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑛1subscript𝑖𝑛1Δsubscript𝑆𝑛superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑛subscript𝑖𝑛absent\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{n}=1}^{2}\prod\limits\_{j=1}^{n}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{B}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{n-1}^{i\_{n-1}})\Delta S\_{n}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{n}^{i\_{n}})= |  |

|  |  |  |
| --- | --- | --- |
|  | ∑i1=12…∑in−1=12∏j=1n−1ψj(ω1i1,…,ωjij)χB(ω1i1,…,ωn−1in−1)×\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{n-1}=1}^{2}\prod\limits\_{j=1}^{n-1}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{B}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{n-1}^{i\_{n-1}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑in=12ψn​(ω1i1,…,ωnin)​Δ​Sn​(ω1i1,…,ωnin)=0,A∈ℱn−1.formulae-sequencesuperscriptsubscriptsubscript𝑖𝑛12subscript𝜓𝑛superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑛subscript𝑖𝑛Δsubscript𝑆𝑛superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑛subscript𝑖𝑛0𝐴subscriptℱ𝑛1\displaystyle\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{n}^{i\_{n}})\Delta S\_{n}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{n}^{i\_{n}})=0,\quad A\in{\cal F}\_{n-1}. |  | (158) |

The last means the needed statement.
Theorem [7](#Thmte7 "Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures.") is proved.

∎

Below, in Theorem [8](#Thmte8 "Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures."), we present the consequence of Theorems [6](#Thmte6 "Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures."), [7](#Thmte7 "Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures.").

###### Theorem 8.

Let the evolution of risky asset be given by the formula ([9](#S2.E9 "In 2 Evolutions of risky assets.")) and let Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures.") conditions be true.
Suppose that the random value
αN​({ω}N1;{ω}N2),subscript𝛼𝑁

superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2\alpha\_{N}(\{\omega\}\_{N}^{1};\{\omega\}\_{N}^{2}), given on the
probability space {ΩN−×ΩN+,ℱN−×ℱN+,PN−×PN+},superscriptsubscriptΩ𝑁superscriptsubscriptΩ𝑁superscriptsubscriptℱ𝑁superscriptsubscriptℱ𝑁superscriptsubscript𝑃𝑁superscriptsubscript𝑃𝑁\{\Omega\_{N}^{-}\times\Omega\_{N}^{+},{\cal F}\_{N}^{-}\times{\cal F}\_{N}^{+},P\_{N}^{-}\times P\_{N}^{+}\},
satisfy the conditions

|  |  |  |
| --- | --- | --- |
|  | PN−×PN+​(({ω11,…,ωN1};{ω12,…,ωN2}),αN​({ω11,…,ωN1};{ω12,…,ωN2})>0)=superscriptsubscript𝑃𝑁superscriptsubscript𝑃𝑁    superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2 subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2 0absentP\_{N}^{-}\times P\_{N}^{+}((\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\}),\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})>0)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∏n=1NPn0​(Ωn0−)×Pn0​(Ωn0+);superscriptsubscriptproduct𝑛1𝑁superscriptsubscript𝑃𝑛0superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝑃𝑛0superscriptsubscriptΩ𝑛limit-from0\displaystyle\prod\limits\_{n=1}^{N}P\_{n}^{0}(\Omega\_{n}^{0-})\times P\_{n}^{0}(\Omega\_{n}^{0+}); |  | (159) |

|  |  |  |
| --- | --- | --- |
|  | ∫Ωn0−×Ωn0+αn({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})×\int\limits\_{\Omega\_{n}^{0-}\times\Omega\_{n}^{0+}}\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\times |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)​Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)​d​Pn0​(ωn1)​d​Pn0​(ωn2)<∞,Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1𝑑superscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})<\infty, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ω1,…,ωn−1)∈Ωn−1;subscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1\displaystyle(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}; |  | (160) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫∏i=1N[Ωi0−×Ωi0+]αN​({ω11,…,ωN1};{ω12,…,ωN2})​∏i=1Nd​Pi0​(ωi1)​d​Pi0​(ωi2)=1,subscriptsuperscriptsubscriptproduct𝑖1𝑁delimited-[]superscriptsubscriptΩ𝑖limit-from0superscriptsubscriptΩ𝑖limit-from0subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2 superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖1𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖21\displaystyle\int\limits\_{\prod\limits\_{i=1}^{N}[\Omega\_{i}^{0-}\times\Omega\_{i}^{0+}]}\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i}^{1})dP\_{i}^{0}(\omega\_{i}^{2})=1, |  | (161) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})=subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2absent\displaystyle\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})= |  | (162) |

|  |  |  |
| --- | --- | --- |
|  | ∫∏i=n+1N[Ωi0−×Ωi0+]αN​({ω11,…,ωN1};{ω12,…,ωN2})​∏i=n+1Nd​Pi0​(ωi1)​d​Pi0​(ωi2)∫∏i=nN[Ωi0−×Ωi0+]αN​({ω11,…,ωN1};{ω12,…,ωN2})​∏i=nNd​Pi0​(ωi1)​d​Pi0​(ωi2),n=1,N¯.  subscriptsuperscriptsubscriptproduct𝑖𝑛1𝑁delimited-[]superscriptsubscriptΩ𝑖limit-from0superscriptsubscriptΩ𝑖limit-from0subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2 superscriptsubscriptproduct𝑖𝑛1𝑁𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖1𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖2subscriptsuperscriptsubscriptproduct𝑖𝑛𝑁delimited-[]superscriptsubscriptΩ𝑖limit-from0superscriptsubscriptΩ𝑖limit-from0subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2 superscriptsubscriptproduct𝑖𝑛𝑁𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖1𝑑superscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖2𝑛 ¯  1𝑁\frac{\int\limits\_{\prod\limits\_{i=n+1}^{N}[\Omega\_{i}^{0-}\times\Omega\_{i}^{0+}]}\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})\prod\limits\_{i=n+1}^{N}dP\_{i}^{0}(\omega\_{i}^{1})dP\_{i}^{0}(\omega\_{i}^{2})}{\int\limits\_{\prod\limits\_{i=n}^{N}[\Omega\_{i}^{0-}\times\Omega\_{i}^{0+}]}\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})\prod\limits\_{i=n}^{N}dP\_{i}^{0}(\omega\_{i}^{1})dP\_{i}^{0}(\omega\_{i}^{2})},\ n=\overline{1,N}. |  |

If the set of strictly positive random values αn​({ω}n1;{ω}n2),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\}\_{n}^{1};\{\omega\}\_{n}^{2}),n=\overline{1,N}, given by the formula ([162](#S6.E162 "In Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.")), satisfies the condition

|  |  |  |
| --- | --- | --- |
|  | Eμ0​|Δ​Sn​(ω1,…,ωn−1,ωn)|=superscript𝐸subscript𝜇0Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absentE^{\mu\_{0}}|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN∏i=1Nψi​(ω1,…,ωi)​|Δ​Sn​(ω1,…,ωn−1,ωn)|​∏i=1Nd​Pi0​(ωi)<∞,n=1,N¯,formulae-sequencesubscriptsubscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁subscript𝜓𝑖subscript𝜔1…subscript𝜔𝑖Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑁𝑑superscriptsubscript𝑃𝑖0subscript𝜔𝑖𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{N}}\prod\limits\_{i=1}^{N}\psi\_{i}(\omega\_{1},\ldots,\omega\_{i})|\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|\prod\limits\_{i=1}^{N}dP\_{i}^{0}(\omega\_{i})<\infty,\quad n=\overline{1,N}, |  | (163) |

then, for the martingale measure μ0​(A)subscript𝜇0𝐴\mu\_{0}(A)
the representation

|  |  |  |
| --- | --- | --- |
|  | μ0​(A)=subscript𝜇0𝐴absent\mu\_{0}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩN×ΩNαN​({ω11,…,ωN1};{ω12,…,ωN2})​μ{ω11,ω12},…,{ωN1,ωN2}​(A)​𝑑PN×𝑑PNsubscriptsubscriptΩ𝑁subscriptΩ𝑁subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2 subscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴differential-dsubscript𝑃𝑁differential-dsubscript𝑃𝑁\displaystyle\int\limits\_{\Omega\_{N}\times\Omega\_{N}}\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A)dP\_{N}\times dP\_{N} |  | (164) |

is true.

###### Proof.

The random values
αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2}),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}),\ n=\overline{1,N}, satisfy the conditions
([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")), due to the conditions of Theorem [8](#Thmte8 "Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.").
It is evident that

|  |  |  |  |
| --- | --- | --- | --- |
|  | αN​({ω11,…,ωN1};{ω12,…,ωN2})=∏n=1Nαn​({ω11,…,ωn1};{ω12,…,ωn2}).subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2superscriptsubscriptproduct𝑛1𝑁subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2\displaystyle\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})=\prod\limits\_{n=1}^{N}\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n}^{2}\}). |  | (165) |

Due to Theorem [7](#Thmte7 "Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures."), μ0​(A),subscript𝜇0𝐴\mu\_{0}(A), given by the formula ([164](#S6.E164 "In Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.")), is a martingale measure being equivalent to the measure PN.subscript𝑃𝑁P\_{N}.

Let us indicate how to construct the random values αN​({ω}N1;{ω}N2),subscript𝛼𝑁

superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2\alpha\_{N}(\{\omega\}\_{N}^{1};\{\omega\}\_{N}^{2}), since these random values determine the set of all martingale measures. Suppose that the random value αik​(ωi1,ωi2),k=1,K¯,

superscriptsubscript𝛼𝑖𝑘superscriptsubscript𝜔𝑖1superscriptsubscript𝜔𝑖2𝑘
¯

1𝐾\alpha\_{i}^{k}(\omega\_{i}^{1},\omega\_{i}^{2}),\ k=\overline{1,K}, is a bounded strictly positive random value, given on the measurable space {Ωi0−×Ωi0+,ℱi0−×ℱi0+},superscriptsubscriptΩ𝑖limit-from0superscriptsubscriptΩ𝑖limit-from0superscriptsubscriptℱ𝑖limit-from0superscriptsubscriptℱ𝑖limit-from0\{\Omega\_{i}^{0-}\times\Omega\_{i}^{0+},{\cal F}\_{i}^{0-}\times{\cal F}\_{i}^{0+}\}, i=1,N¯,𝑖¯

1𝑁i=\overline{1,N}, and satisfying the conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωi0−×Ωi0+αik​(ωi1,ωi2)​𝑑Pi0​(ωi1)​𝑑Pi0​(ωi2)=1,i=1,N¯,k=1,K¯.formulae-sequencesubscriptsuperscriptsubscriptΩ𝑖limit-from0superscriptsubscriptΩ𝑖limit-from0superscriptsubscript𝛼𝑖𝑘superscriptsubscript𝜔𝑖1superscriptsubscript𝜔𝑖2differential-dsuperscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖1differential-dsuperscriptsubscript𝑃𝑖0superscriptsubscript𝜔𝑖21formulae-sequence𝑖¯  1𝑁𝑘¯  1𝐾\displaystyle\int\limits\_{\Omega\_{i}^{0-}\times\Omega\_{i}^{0+}}\alpha\_{i}^{k}(\omega\_{i}^{1},\omega\_{i}^{2})dP\_{i}^{0}(\omega\_{i}^{1})dP\_{i}^{0}(\omega\_{i}^{2})=1,\quad i=\overline{1,N},\quad k=\overline{1,K}. |  | (166) |

Let us denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | αNk​({ω11,…,ωN1};{ω12,…,ωN2})=∏i=1Nαik​(ωi1,ωi2),k=1,K¯,formulae-sequencesuperscriptsubscript𝛼𝑁𝑘  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2superscriptsubscriptproduct𝑖1𝑁superscriptsubscript𝛼𝑖𝑘superscriptsubscript𝜔𝑖1superscriptsubscript𝜔𝑖2𝑘¯  1𝐾\displaystyle\alpha\_{N}^{k}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})=\prod\limits\_{i=1}^{N}\alpha\_{i}^{k}(\omega\_{i}^{1},\omega\_{i}^{2}),\quad k=\overline{1,K}, |  | (167) |

where K𝐾K runs natural numbers. If γk,k=1,K¯,

subscript𝛾𝑘𝑘
¯

1𝐾\gamma\_{k},\ k=\overline{1,K}, are strictly positive real numbers such that ∑k=1Kγk=1,superscriptsubscript𝑘1𝐾subscript𝛾𝑘1\sum\limits\_{k=1}^{K}\gamma\_{k}=1, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | αN​({ω11,…,ωN1};{ω12,…,ωN2})=∑k=1Kγk​αNk​({ω11,…,ωN1};{ω12,…,ωN2})subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2superscriptsubscript𝑘1𝐾subscript𝛾𝑘superscriptsubscript𝛼𝑁𝑘  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2\displaystyle\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})=\sum\limits\_{k=1}^{K}\gamma\_{k}\alpha\_{N}^{k}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\}) |  | (168) |

satisfy the conditions of Theorem [8](#Thmte8 "Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures."). The set of random values ([168](#S6.E168 "In Proof. ‣ 6 Spot measures and integral representation for martingale measures.")) is dense in the set of random values αN​({ω11,…,ωN1};{ω12,…,ωN2}),subscript𝛼𝑁

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\}), satisfying the condition ([159](#S6.E159 "In Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.")) - ([161](#S6.E161 "In Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.")).
Theorem [8](#Thmte8 "Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.") is proved.
∎

Another way to construct αN​({ω11,…,ωN1};{ω12,…,ωN2})subscript𝛼𝑁

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\}) is to use the equalities ([126](#S6.E126 "In 6 Spot measures and integral representation for martingale measures.")).
The set of αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}) can construct as follows: suppose that αn1​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})superscriptsubscript𝛼𝑛1

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2\alpha\_{n}^{1}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})
satisfies the inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<hn≤αn1​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})≤Hn<∞0subscriptℎ𝑛superscriptsubscript𝛼𝑛1  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2subscript𝐻𝑛\displaystyle 0<h\_{n}\leq\alpha\_{n}^{1}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})\leq H\_{n}<\infty |  | (169) |

for a certain real positive numbers hn,Hn.

subscriptℎ𝑛subscript𝐻𝑛h\_{n},H\_{n}. If to put

|  |  |  |
| --- | --- | --- |
|  | αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})=subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2absent\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn1​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})∫Ωn0−×Ωn0+αn1​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2})​𝑑Pn0​(ωn1)​𝑑Pn0​(ωn2),superscriptsubscript𝛼𝑛1  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2subscriptsuperscriptsubscriptΩ𝑛limit-from0superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝛼𝑛1  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2 differential-dsuperscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛1differential-dsuperscriptsubscript𝑃𝑛0superscriptsubscript𝜔𝑛2\displaystyle\frac{\alpha\_{n}^{1}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})}{\int\limits\_{\Omega\_{n}^{0-}\times\Omega\_{n}^{0+}}\alpha\_{n}^{1}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\})dP\_{n}^{0}(\omega\_{n}^{1})dP\_{n}^{0}(\omega\_{n}^{2})}, |  | (170) |

then the set of random values αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2}),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}),\ n=\overline{1,N}, is bounded and satisfy the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")) under the conditions of Theorem [7](#Thmte7 "Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures.").
We can put

|  |  |  |
| --- | --- | --- |
|  | αN​({ω11,…,ωN1};{ω12,…,ωN2})=subscript𝛼𝑁  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁2absent\alpha\_{N}(\{\omega\_{1}^{1},\ldots,\omega\_{N}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{N}^{2}\})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∏n=1Nαn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2}).superscriptsubscriptproduct𝑛1𝑁subscript𝛼𝑛  superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2\displaystyle\prod\limits\_{n=1}^{N}\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}). |  | (171) |

It is evident that αn​({ω11,…,ωn−11,ωn1};{ω12,…,ωn−12,ωn2}),n=1,N¯,

subscript𝛼𝑛

superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛12superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\{\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1}\};\{\omega\_{1}^{2},\ldots,\omega\_{n-1}^{2},\omega\_{n}^{2}\}),\ n=\overline{1,N},
must satisfy the conditions ([163](#S6.E163 "In Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.")).

## 7 Derivatives assessment.

In the papers [[27](#bib.bib27)], [[28](#bib.bib28)], the range of non arbitrage prices are established. In the paper [[27](#bib.bib27)], for the Levy exponential model, the price of super-hedge for call option coincides with the price of the underlying asset under the assumption that the Levy process has unlimited variation, does not contain a Brownian component, with negative jumps of arbitrary magnitude.
The same result is true, obtained in the paper [[28](#bib.bib28)], if the process describing the evolution of the underlying asset is a diffusion process with the jumps described by Poisson jump process.
In these papers the evolution is described by continuous processes. Below, we consider the discrete evolution of risky assets that is more realistic from the practical point of view.
Two types of risky asset evolutions are considered: 1) the price of an asset can take any non negative value; 2) the price of the risky asset may not fall below a given positive value for finite time of evolution. For each of these types of evolutions of risky assets, the bounds of non-arbitrage prices for a wide class of contingent liabilities are found, among which are the payoff functions of standard call and put options.

Below, on the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, where ΩN=∏i=1NΩi0,subscriptΩ𝑁superscriptsubscriptproduct𝑖1𝑁superscriptsubscriptΩ𝑖0\Omega\_{N}=\prod\limits\_{i=1}^{N}\Omega\_{i}^{0}, ℱN=∏i=1Nℱi0,subscriptℱ𝑁superscriptsubscriptproduct𝑖1𝑁superscriptsubscriptℱ𝑖0{\cal F}\_{N}=\prod\limits\_{i=1}^{N}{\cal F}\_{i}^{0}, PN=∏i=1NPi0,subscript𝑃𝑁superscriptsubscriptproduct𝑖1𝑁superscriptsubscript𝑃𝑖0P\_{N}=\prod\limits\_{i=1}^{N}P\_{i}^{0},
Ωi0superscriptsubscriptΩ𝑖0\Omega\_{i}^{0} is a complete separable metric space, ℱi0superscriptsubscriptℱ𝑖0{\cal F}\_{i}^{0} is a Borel σ𝜎\sigma-algebra on Ωi0,superscriptsubscriptΩ𝑖0\Omega\_{i}^{0}, Pi0superscriptsubscript𝑃𝑖0P\_{i}^{0} is a probability measure on ℱi0,i=1,N¯,

superscriptsubscriptℱ𝑖0𝑖
¯

1𝑁{\cal F}\_{i}^{0},\ i=\overline{1,N}, we consider the evolution of risky asset given by the formula

|  |  |  |
| --- | --- | --- |
|  | Sn​(ω1,…,ωn)=subscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛absentS\_{n}(\omega\_{1},\ldots,\omega\_{n})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | S0​∏i=1n(1+ai​(ω1,…,ωi−1)​(eσi​(ω1,…,ωi−1)​εi​(ωi)−1)),n=1,N¯,  subscript𝑆0superscriptsubscriptproduct𝑖1𝑛1subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1𝑛 ¯  1𝑁\displaystyle S\_{0}\prod\limits\_{i=1}^{n}(1+a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})(e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}-1)),\quad n=\overline{1,N}, |  | (172) |

where ai​(ω1,…,ωi−1),σi​(ω1,…,ωi−1)

subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1a\_{i}(\omega\_{1},\ldots,\omega\_{i-1}),\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1}) are ℱi−1subscriptℱ𝑖1{\cal F}\_{i-1}-measurable random values, satisfying the conditions 0<ai​(ω1,…,ωi−1)≤1,σi​(ω1,…,ωi−1)≥σi>0,formulae-sequence0subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖11subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖00<a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\leq 1,\ \sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\geq\sigma\_{i}>0, where σi,i=1,N¯,

subscript𝜎𝑖𝑖
¯

1𝑁\sigma\_{i},\ i=\overline{1,N}, are real positive numbers. Further, we assume that the random value εi​(ωi)subscript𝜀𝑖subscript𝜔𝑖\varepsilon\_{i}(\omega\_{i}) satisfy the conditions: there exists ωi1∈Ωi0superscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖0\omega\_{i}^{1}\in\Omega\_{i}^{0} such that εi​(ωi1)=0,i=1,N¯,formulae-sequencesubscript𝜀𝑖superscriptsubscript𝜔𝑖10𝑖¯

1𝑁\varepsilon\_{i}(\omega\_{i}^{1})=0,\ i=\overline{1,N},
and for every real number t>0,𝑡0t>0,  Pi0​(εi​(ωi)<−t)>0,superscriptsubscript𝑃𝑖0subscript𝜀𝑖subscript𝜔𝑖𝑡0P\_{i}^{0}(\varepsilon\_{i}(\omega\_{i})<-t)>0,  Pi0​(εi​(ωi)>t)>0,superscriptsubscript𝑃𝑖0subscript𝜀𝑖subscript𝜔𝑖𝑡0P\_{i}^{0}(\varepsilon\_{i}(\omega\_{i})>t)>0,  i=1,N¯.𝑖¯

1𝑁i=\overline{1,N}.

For the evolution of risky asset ([172](#S7.E172 "In 7 Derivatives assessment.")), we have

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn​(ω1,…,ωn−1,ωn)=Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−1​(ω1,…,ωn−1)​an​(ω1,…,ωn−1)​(eσn​(ω1,…,ωn−1)​εn​(ωn)−1)=subscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛subscript𝜔𝑛1absent\displaystyle S\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})(e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n})}-1)= |  | (173) |

|  |  |  |
| --- | --- | --- |
|  | dn​(ω1,…,ωn−1,ωn)​(eσn​εn​(ωn)−1),subscript𝑑𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscript𝑒subscript𝜎𝑛subscript𝜀𝑛subscript𝜔𝑛1d\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})(e^{\sigma\_{n}\varepsilon\_{n}(\omega\_{n})}-1), |  |

where

|  |  |  |
| --- | --- | --- |
|  | dn​(ω1,…,ωn−1,ωn)=subscript𝑑𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absentd\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−1​(ω1,…,ωn−1)​an​(ω1,…,ωn−1)​(eσn​(ω1,…,ωn−1)​εn​(ωn)−1)(eσn​εn​(ωn)−1).subscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛subscript𝜔𝑛1superscript𝑒subscript𝜎𝑛subscript𝜀𝑛subscript𝜔𝑛1\displaystyle S\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\frac{(e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n})}-1)}{(e^{\sigma\_{n}\varepsilon\_{n}(\omega\_{n})}-1)}. |  | (174) |

It is evident that dn​(ω1,…,ωn−1,ωn)>0,subscript𝑑𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛0d\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})>0, therefore for Δ​Sn​(ω1,…,ωn−1,ωn)Δsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛\Delta S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}) the representation
([60](#S4.E60 "In 4 Inequalities for the nonnegative random values.")) is true with ηn​(ωn)=(eσn​εn​(ωn)−1).subscript𝜂𝑛subscript𝜔𝑛superscript𝑒subscript𝜎𝑛subscript𝜀𝑛subscript𝜔𝑛1\eta\_{n}(\omega\_{n})=(e^{\sigma\_{n}\varepsilon\_{n}(\omega\_{n})}-1).
Therefore,

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)Vn​(ω1,…,ωn−1,ωn1,ωn2)=Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2absent\frac{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | eσn​(ω1,…,ωn−1)​εn​(ωn2)−1eσn​(ω1,…,ωn−1)​εn​(ωn2)−eσn​(ω1,…,ωn−1)​εn​(ωn1),ωn2∈Ωn0+,(ω1,…,ωn−1)∈Ωn−1,formulae-sequence  superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛21superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛2superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2 superscriptsubscriptΩ𝑛limit-from0subscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1\displaystyle\frac{e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{2})}-1}{e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{2})}-e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{1})}},\quad\omega\_{n}^{2}\in\Omega\_{n}^{0+},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (175) |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)Vn​(ω1,…,ωn−1,ωn1,ωn2)=Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔superscript𝑛1subscript𝑉𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛2absent\frac{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n^{1}})}{V\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1},\omega\_{n}^{2})}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−eσn​(ω1,…,ωn−1)​εn​(ωn1)eσn​(ω1,…,ωn−1)​εn​(ωn2)−eσn​(ω1,…,ωn−1)​εn​(ωn1),ωn1∈Ωn0−,(ω1,…,ωn−1)∈Ωn−1,formulae-sequence  1superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛1superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛2superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛1 superscriptsubscriptΩ𝑛limit-from0subscript𝜔1…subscript𝜔𝑛1subscriptΩ𝑛1\displaystyle\frac{1-e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{1})}}{e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{2})}-e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{1})}},\quad\omega\_{n}^{1}\in\Omega\_{n}^{0-},\quad(\omega\_{1},\ldots,\omega\_{n-1})\in\Omega\_{n-1}, |  | (176) |

where we denoted

|  |  |  |
| --- | --- | --- |
|  | Ωn0−={ωn∈Ωn0,εn​(ωn)≤0},Ωn0+={ωn∈Ωn0,εn​(ωn)>0},formulae-sequencesuperscriptsubscriptΩ𝑛limit-from0formulae-sequencesubscript𝜔𝑛superscriptsubscriptΩ𝑛0subscript𝜀𝑛subscript𝜔𝑛0superscriptsubscriptΩ𝑛limit-from0formulae-sequencesubscript𝜔𝑛superscriptsubscriptΩ𝑛0subscript𝜀𝑛subscript𝜔𝑛0\Omega\_{n}^{0-}=\{\omega\_{n}\in\Omega\_{n}^{0},\varepsilon\_{n}(\omega\_{n})\leq 0\},\quad\Omega\_{n}^{0+}=\{\omega\_{n}\in\Omega\_{n}^{0},\varepsilon\_{n}(\omega\_{n})>0\}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωn−=Ωn0−×Ωn−1,Ωn+=Ωn0+×Ωn−1.formulae-sequencesuperscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛limit-from0subscriptΩ𝑛1superscriptsubscriptΩ𝑛superscriptsubscriptΩ𝑛limit-from0subscriptΩ𝑛1\displaystyle\Omega\_{n}^{-}=\Omega\_{n}^{0-}\times\Omega\_{n-1},\quad\Omega\_{n}^{+}=\Omega\_{n}^{0+}\times\Omega\_{n-1}. |  | (177) |

From the formulas ([175](#S7.E175 "In 7 Derivatives assessment.")), ([176](#S7.E176 "In 7 Derivatives assessment.")) and Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures."),
it follows that the set of martingale measures M𝑀M do not depend on the random values
ai​(ω1,…,ωi−1),i=1,N¯.

subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1𝑖
¯

1𝑁a\_{i}(\omega\_{1},\ldots,\omega\_{i-1}),\ i=\overline{1,N}.
If to put ai​(ω1,…,ωi−1)=1,i=1,N¯,formulae-sequencesubscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖11𝑖¯

1𝑁a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})=1,\ i=\overline{1,N}, in the formula ([172](#S7.E172 "In 7 Derivatives assessment.")), then for the risky asset evolution we obtain the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn​(ω1,…,ωn−1,ωn)=S0​∏i=1neσi​(ω1,…,ωi−1)​εi​(ωi),n=1,N¯.formulae-sequencesubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛subscript𝑆0superscriptsubscriptproduct𝑖1𝑛superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖𝑛¯  1𝑁\displaystyle S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})=S\_{0}\prod\limits\_{i=1}^{n}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})},\quad n=\overline{1,N}. |  | (178) |

The evolution of risky assets, given by the formula ([178](#S7.E178 "In 7 Derivatives assessment.")), includes a wide class of evolutions of risky assets, used in economics.
For example, under an appropriate choice of probability spaces {Ωi0,ℱi0,Pi0}superscriptsubscriptΩ𝑖0superscriptsubscriptℱ𝑖0superscriptsubscript𝑃𝑖0\{\Omega\_{i}^{0},{\cal F}\_{i}^{0},P\_{i}^{0}\} and a choice of sequence of independent random values εi​(ωi)subscript𝜀𝑖subscript𝜔𝑖\varepsilon\_{i}(\omega\_{i}) with the normal distribution N​(0,1),𝑁01N(0,1), we obtain ARCH model (Autoregressive Conditional Heteroskedastic Model) introduced by Engle in [[18](#bib.bib18)] and GARCH model (Generalized Autoregressive Conditional Heteroskedastic Model) introduced later by Bollerslev in [[19](#bib.bib19)]. In these models, the random variables σi​(ω1,…,ωi−1),i=1,N¯,

subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1𝑖
¯

1𝑁\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1}),\ i=\overline{1,N}, are called the volatilities which satisfy the nonlinear set of equations.

The very important case of evolution of risky assets ([172](#S7.E172 "In 7 Derivatives assessment.")) is when ai​(ω1,…,ωi−1)=ai,i=1,N¯,formulae-sequencesubscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝑎𝑖𝑖¯

1𝑁a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})=a\_{i},\ i=\overline{1,N}, are constants, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn​(ω1,…,ωn−1,ωn)=S0​∏i=1n(1+ai​(eσi​(ω1,…,ωi−1)​εi​(ωi)−1)),n=1,N¯,formulae-sequencesubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛subscript𝑆0superscriptsubscriptproduct𝑖1𝑛1subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1𝑛¯  1𝑁\displaystyle S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})=S\_{0}\prod\limits\_{i=1}^{n}(1+a\_{i}(e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}-1)),\quad n=\overline{1,N}, |  | (179) |

where 0≤ai≤1.0subscript𝑎𝑖10\leq a\_{i}\leq 1.

If 0<ai<1,i=1,N¯,formulae-sequence0subscript𝑎𝑖1𝑖¯

1𝑁0<a\_{i}<1,i=\overline{1,N}, then the evolution of risky asset, given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")), we call the evolution of relatively stable asset.

Further, we assume that the evolution of risky asset given by the formulas ([172](#S7.E172 "In 7 Derivatives assessment.")), ([178](#S7.E178 "In 7 Derivatives assessment.")), ([179](#S7.E179 "In 7 Derivatives assessment.")) satisfy the conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩNSn​(ω1,…,ωn−1,ωn)​𝑑PN<∞,n=1,N¯.formulae-sequencesubscriptsubscriptΩ𝑁subscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛differential-dsubscript𝑃𝑁𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{N}}S\_{n}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})dP\_{N}<\infty,\quad n=\overline{1,N}. |  | (180) |

From the conditions ([180](#S7.E180 "In 7 Derivatives assessment.")), it follows the inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΩNΔ​Sn−​(ω1,…,ωn)​𝑑PN<∞,n=1,N¯.formulae-sequencesubscriptsubscriptΩ𝑁Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛differential-dsubscript𝑃𝑁𝑛¯  1𝑁\displaystyle\int\limits\_{\Omega\_{N}}\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n})dP\_{N}<\infty,\quad n=\overline{1,N}. |  | (181) |

Taking into account that

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω1,…,ωn−1,ωn1)=Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛1absent\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−1​(ω1,…,ωn−1)​an​(ω1,…,ωn−1)​(1−eσn​(ω1,…,ωn−1)​εn​(ωn1)),ωn1∈Ωn0−,  subscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛11superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛1superscriptsubscript𝜔𝑛1 superscriptsubscriptΩ𝑛limit-from0\displaystyle S\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})(1-e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{1})}),\quad\omega\_{n}^{1}\in\Omega\_{n}^{0-}, |  | (182) |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn+​(ω1,…,ωn−1,ωn2)=Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛2absent\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−1​(ω1,…,ωn−1)​an​(ω1,…,ωn−1)​(eσn​(ω1,…,ωn−1)​εn​(ωn2)−1),ωn2∈Ωn0+,  subscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛21superscriptsubscript𝜔𝑛2 superscriptsubscriptΩ𝑛limit-from0\displaystyle S\_{n-1}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})(e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n}^{2})}-1),\quad\omega\_{n}^{2}\in\Omega\_{n}^{0+}, |  | (183) |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1Δ​Sn−​(ω1,…,ωn−1,ωn1)≤1∏i=1n−1(1−ai1)​an0​(1−eσn​εn​(ωn1))<∞,εn​(ωn1)<0,formulae-sequence1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛11superscriptsubscriptproduct𝑖1𝑛11superscriptsubscript𝑎𝑖1superscriptsubscript𝑎𝑛01superscript𝑒subscript𝜎𝑛subscript𝜀𝑛superscriptsubscript𝜔𝑛1subscript𝜀𝑛superscriptsubscript𝜔𝑛10\displaystyle\frac{1}{\Delta S\_{n}^{-}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{1})}\leq\frac{1}{\prod\limits\_{i=1}^{n-1}(1-a\_{i}^{1})a\_{n}^{0}(1-e^{\sigma\_{n}\varepsilon\_{n}(\omega\_{n}^{1})})}<\infty,\quad\varepsilon\_{n}(\omega\_{n}^{1})<0, |  | (184) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1Δ​Sn+​(ω1,…,ωn−1,ωn2)≤1∏i=1n−1(1−ai1)​an0​(eσn​εn​(ωn2)−1)<∞,εn​(ωn2)>0,formulae-sequence1Δsuperscriptsubscript𝑆𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝜔𝑛21superscriptsubscriptproduct𝑖1𝑛11superscriptsubscript𝑎𝑖1superscriptsubscript𝑎𝑛0superscript𝑒subscript𝜎𝑛subscript𝜀𝑛superscriptsubscript𝜔𝑛21subscript𝜀𝑛superscriptsubscript𝜔𝑛20\displaystyle\frac{1}{\Delta S\_{n}^{+}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n}^{2})}\leq\frac{1}{\prod\limits\_{i=1}^{n-1}(1-a\_{i}^{1})a\_{n}^{0}(e^{\sigma\_{n}\varepsilon\_{n}(\omega\_{n}^{2})}-1)}<\infty,\quad\varepsilon\_{n}(\omega\_{n}^{2})>0, |  | (185) |

under the conditions that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<an0≤an​(ω1,…,ωn−1)≤an1<1,n=1,N¯.formulae-sequence0superscriptsubscript𝑎𝑛0subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑎𝑛11𝑛¯  1𝑁\displaystyle 0<a\_{n}^{0}\leq a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\leq a\_{n}^{1}<1,\quad n=\overline{1,N}. |  | (186) |

###### Theorem 9.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by one of the formula ([172](#S7.E172 "In 7 Derivatives assessment.")), ([178](#S7.E178 "In 7 Derivatives assessment.")), ([179](#S7.E179 "In 7 Derivatives assessment.")) that satisfies the conditions ([180](#S7.E180 "In 7 Derivatives assessment.")).

If the inequalities 0<an0≤an​(ω1,…,ωn−1)≤an1<1, 0<ai<1,i=1,N¯,formulae-sequence0superscriptsubscript𝑎𝑛0subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑎𝑛11 0subscript𝑎𝑖1𝑖¯

1𝑁0<a\_{n}^{0}\leq a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\leq a\_{n}^{1}<1,\ 0<a\_{i}<1,\ i=\overline{1,N}, are true, then the set of martingale measures M𝑀M is the same for every evolution of risky assets, given by the formulas ([172](#S7.E172 "In 7 Derivatives assessment.")), ([179](#S7.E179 "In 7 Derivatives assessment.")).
For every non-negative super-martingale relative to the set of martingale measures M𝑀M the optional decomposition is valid.
Every measure of M𝑀M is an integral over the spot measures. The fair price f0subscript𝑓0f\_{0} of super-hedge for the nonnegative payoff function f​(x)𝑓𝑥f(x) is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | f0=supP∈MEP​f​(SN)=supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}.subscript𝑓0subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2\displaystyle f\_{0}=\sup\limits\_{P\in M}E^{P}f(S\_{N})=\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}. |  | (187) |

The set of martingale measures M1subscript𝑀1M\_{1} for the evolution of risky asset, given by the formula ([178](#S7.E178 "In 7 Derivatives assessment.")), is contained in the set M.𝑀M.

###### Proof.

From the equalities ([175](#S7.E175 "In 7 Derivatives assessment.")) - ([176](#S7.E176 "In 7 Derivatives assessment.")) and the inequalities ([180](#S7.E180 "In 7 Derivatives assessment.")), it follows that the set M𝑀M
is a nonempty one and every martingale measure constructed by the set of random values
αn​(ω11,…,ωn1;ω12,…,ωn2),n=1,N¯,

subscript𝛼𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1superscriptsubscript𝜔12…superscriptsubscript𝜔𝑛2𝑛
¯

1𝑁\alpha\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n}^{1};\omega\_{1}^{2},\ldots,\omega\_{n}^{2}),\ n=\overline{1,N}, belongs to the set M,𝑀M, if the inequalities ([49](#S3.E49 "In Theorem 1. ‣ 3 Construction of the set of martingale measures.")) are true.
To prove that the set of martingale measures, defined by the evolutions ([172](#S7.E172 "In 7 Derivatives assessment.")), ([179](#S7.E179 "In 7 Derivatives assessment.")), coincide it is necessary to prove the inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<An1≤Sn1​(ω1,…,ωn)Sn2​(ω1,…,ωn)≤Bn1<∞,n=1,N¯,formulae-sequence0superscriptsubscript𝐴𝑛1superscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝐵𝑛1𝑛¯  1𝑁\displaystyle 0<A\_{n}^{1}\leq\frac{S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})}{S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n})}\leq B\_{n}^{1}<\infty,\quad n=\overline{1,N}, |  | (188) |

where we denoted by Sn1​(ω1,…,ωn)superscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n}) the evolution, given by the formula ([172](#S7.E172 "In 7 Derivatives assessment.")), and by Sn2​(ω1,…,ωn)superscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n}) the evolution, given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")). Under the conditions of Theorem [9](#Thmte9 "Theorem 9. ‣ 7 Derivatives assessment."), we have

|  |  |  |
| --- | --- | --- |
|  | Sn1​(ω1,…,ωn)Sn2​(ω1,…,ωn)=superscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛absent\frac{S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})}{S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n})}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | S0​∏i=1n(1+ai​(ω1,…,ωi−1)​(eσi​(ω1,…,ωi−1)​εi​(ωi)−1))S0​∏i=1n(1+ai​(eσi​(ω1,…,ωi−1)​εi​(ωi)−1)),n=1,N¯.  subscript𝑆0superscriptsubscriptproduct𝑖1𝑛1subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1subscript𝑆0superscriptsubscriptproduct𝑖1𝑛1subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1𝑛 ¯  1𝑁\displaystyle\frac{S\_{0}\prod\limits\_{i=1}^{n}(1+a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})(e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}-1))}{S\_{0}\prod\limits\_{i=1}^{n}(1+a\_{i}(e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}-1))},\quad n=\overline{1,N}. |  | (189) |

Since

|  |  |  |
| --- | --- | --- |
|  | 1+ai​(ω1,…,ωi−1)​(eσi​(ω1,…,ωi−1)​εi​(ωi)−1)1+ai​(eσi​(ω1,…,ωi−1)​εi​(ωi)−1)=1subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖11subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1absent\frac{1+a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})(e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}-1)}{1+a\_{i}(e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}-1)}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−ai​(ω1,…,ωi−1)+ai​(ω1,…,ωi−1)​eσi​(ω1,…,ωi−1)​εi​(ωi)1−ai+ai​eσi​(ω1,…,ωi−1)​εi​(ωi)=Di,i=1,N¯,formulae-sequence1subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖1superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1subscript𝑎𝑖subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖subscript𝐷𝑖𝑖¯  1𝑁\displaystyle\frac{1-a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})+a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}}{1-a\_{i}+a\_{i}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}}=D\_{i},\quad i=\overline{1,N}, |  | (190) |

we have

|  |  |  |
| --- | --- | --- |
|  | 1−ai1+ai0​eσi​(ω1,…,ωi−1)​εi​(ωi)1−ai+ai​eσi​(ω1,…,ωi−1)​εi​(ωi)≤Di≤1superscriptsubscript𝑎𝑖1superscriptsubscript𝑎𝑖0superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1subscript𝑎𝑖subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖subscript𝐷𝑖absent\frac{1-a\_{i}^{1}+a\_{i}^{0}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}}{1-a\_{i}+a\_{i}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}}\leq D\_{i}\leq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−ai0+ai1​eσi​(ω1,…,ωi−1)​εi​(ωi)1−ai+ai​eσi​(ω1,…,ωi−1)​εi​(ωi),i=1,N¯.  1superscriptsubscript𝑎𝑖0superscriptsubscript𝑎𝑖1superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1subscript𝑎𝑖subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖𝑖 ¯  1𝑁\displaystyle\frac{1-a\_{i}^{0}+a\_{i}^{1}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}}{1-a\_{i}+a\_{i}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}},\quad i=\overline{1,N}. |  | (191) |

Let us denote

|  |  |  |
| --- | --- | --- |
|  | Ai=inf(ω1,…,ωi)∈Ωi1−ai1+ai0​eσi​(ω1,…,ωi−1)​εi​(ωi)1−ai+ai​eσi​(ω1,…,ωi−1)​εi​(ωi),i=1,N¯,formulae-sequencesubscript𝐴𝑖subscriptinfimumsubscript𝜔1…subscript𝜔𝑖subscriptΩ𝑖1superscriptsubscript𝑎𝑖1superscriptsubscript𝑎𝑖0superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1subscript𝑎𝑖subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖𝑖¯  1𝑁A\_{i}=\inf\limits\_{(\omega\_{1},\ldots,\omega\_{i})\in\Omega\_{i}}\frac{1-a\_{i}^{1}+a\_{i}^{0}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}}{1-a\_{i}+a\_{i}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}},\quad i=\overline{1,N}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bi=sup(ω1,…,ωi)∈Ωi1−ai0+ai1​eσi​(ω1,…,ωi−1)​εi​(ωi)1−ai+ai​eσi​(ω1,…,ωi−1)​εi​(ωi),i=1,N¯.formulae-sequencesubscript𝐵𝑖subscriptsupremumsubscript𝜔1…subscript𝜔𝑖subscriptΩ𝑖1superscriptsubscript𝑎𝑖0superscriptsubscript𝑎𝑖1superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖1subscript𝑎𝑖subscript𝑎𝑖superscript𝑒subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜀𝑖subscript𝜔𝑖𝑖¯  1𝑁\displaystyle B\_{i}=\sup\limits\_{(\omega\_{1},\ldots,\omega\_{i})\in\Omega\_{i}}\frac{1-a\_{i}^{0}+a\_{i}^{1}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}}{1-a\_{i}+a\_{i}e^{\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\varepsilon\_{i}(\omega\_{i})}},\quad i=\overline{1,N}. |  | (192) |

It is evident that 0<Ai,Bi<∞,i=1,N¯,formulae-sequence0subscript𝐴𝑖formulae-sequencesubscript𝐵𝑖𝑖¯

1𝑁0<A\_{i},B\_{i}<\infty,\ i=\overline{1,N}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai≤Di≤Bi,i=1,N¯,formulae-sequencesubscript𝐴𝑖subscript𝐷𝑖subscript𝐵𝑖𝑖¯  1𝑁\displaystyle A\_{i}\leq D\_{i}\leq B\_{i},\quad i=\overline{1,N}, |  | (193) |

therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | An1=∏i=1nAi≤Sn1​(ω1,…,ωn)Sn2​(ω1,…,ωn)≤∏i=1nBi=Bn1,n=1,N¯.formulae-sequencesuperscriptsubscript𝐴𝑛1superscriptsubscriptproduct𝑖1𝑛subscript𝐴𝑖superscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛subscript𝐵𝑖superscriptsubscript𝐵𝑛1𝑛¯  1𝑁\displaystyle A\_{n}^{1}=\prod\limits\_{i=1}^{n}A\_{i}\leq\frac{S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})}{S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n})}\leq\prod\limits\_{i=1}^{n}B\_{i}=B\_{n}^{1},\quad n=\overline{1,N}. |  | (194) |

So,

|  |  |  |  |
| --- | --- | --- | --- |
|  | AN2≤Sn1​(ω1,…,ωn)Sn2​(ω1,…,ωn)≤BN2,n=1,N¯,formulae-sequencesuperscriptsubscript𝐴𝑁2superscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝐵𝑁2𝑛¯  1𝑁\displaystyle A\_{N}^{2}\leq\frac{S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n})}{S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n})}\leq B\_{N}^{2},\quad n=\overline{1,N}, |  | (195) |

where we put
AN2=min1≤n≤N⁡An1,BN2=max1≤n≤N⁡Bn1.formulae-sequencesuperscriptsubscript𝐴𝑁2subscript1𝑛𝑁superscriptsubscript𝐴𝑛1superscriptsubscript𝐵𝑁2subscript1𝑛𝑁superscriptsubscript𝐵𝑛1A\_{N}^{2}=\min\limits\_{1\leq n\leq N}A\_{n}^{1},\ B\_{N}^{2}=\max\limits\_{1\leq n\leq N}B\_{n}^{1}.
Since

|  |  |  |
| --- | --- | --- |
|  | |Δ​Sn1​(ω1,…,ωn−1,ωn)|=Δsuperscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent|\Delta S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−11​(ω1,…,ωn−1)​an​(ω1,…,ωn−1)​|(eσn​(ω1,…,ωn−1)​εn​(ωn)−1)|,superscriptsubscript𝑆𝑛11subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛subscript𝜔𝑛1\displaystyle S\_{n-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})|(e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n})}-1)|, |  | (196) |

|  |  |  |
| --- | --- | --- |
|  | |Δ​Sn2​(ω1,…,ωn−1,ωn)|=Δsuperscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent|\Delta S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−12​(ω1,…,ωn−1)​an​|(eσn​(ω1,…,ωn−1)​εn​(ωn)−1)|,superscriptsubscript𝑆𝑛12subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛superscript𝑒subscript𝜎𝑛subscript𝜔1…subscript𝜔𝑛1subscript𝜀𝑛subscript𝜔𝑛1\displaystyle S\_{n-1}^{2}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}|(e^{\sigma\_{n}(\omega\_{1},\ldots,\omega\_{n-1})\varepsilon\_{n}(\omega\_{n})}-1)|, |  | (197) |

we have

|  |  |  |
| --- | --- | --- |
|  | |Δ​Sn1​(ω1,…,ωn−1,ωn)||Δ​Sn2​(ω1,…,ωn−1,ωn)|=Δsuperscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛Δsuperscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\frac{|\Delta S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|}{|\Delta S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−11​(ω1,…,ωn−1)​an​(ω1,…,ωn−1)Sn−12​(ω1,…,ωn−1)​an.superscriptsubscript𝑆𝑛11subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑆𝑛12subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛\displaystyle\frac{S\_{n-1}^{1}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}(\omega\_{1},\ldots,\omega\_{n-1})}{S\_{n-1}^{2}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}}. |  | (198) |

Taking into account the obtained inequalities, we have the inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | AN2​min1≤n≤N⁡an0max1≤n≤N⁡an≤|Δ​Sn1​(ω1,…,ωn−1,ωn)||Δ​Sn2​(ω1,…,ωn−1,ωn)|≤BN2​max1≤n≤N⁡an1min1≤n≤N⁡an,n=1,N¯.formulae-sequencesuperscriptsubscript𝐴𝑁2subscript1𝑛𝑁superscriptsubscript𝑎𝑛0subscript1𝑛𝑁subscript𝑎𝑛Δsuperscriptsubscript𝑆𝑛1subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛Δsuperscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛superscriptsubscript𝐵𝑁2subscript1𝑛𝑁superscriptsubscript𝑎𝑛1subscript1𝑛𝑁subscript𝑎𝑛𝑛¯  1𝑁\displaystyle A\_{N}^{2}\frac{\min\limits\_{1\leq n\leq N}a\_{n}^{0}}{\max\limits\_{1\leq n\leq N}a\_{n}}\leq\frac{|\Delta S\_{n}^{1}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|}{|\Delta S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|}\leq B\_{N}^{2}\frac{\max\limits\_{1\leq n\leq N}a\_{n}^{1}}{\min\limits\_{1\leq n\leq N}a\_{n}},\quad n=\overline{1,N}. |  | (199) |

The inequalities ([199](#S7.E199 "In Proof. ‣ 7 Derivatives assessment.")) proves that the set of martingale measures for the evolutions of risky assets given by the formulas ([172](#S7.E172 "In 7 Derivatives assessment.")), ([179](#S7.E179 "In 7 Derivatives assessment.")) are the same, since the inequalities ([49](#S3.E49 "In Theorem 1. ‣ 3 Construction of the set of martingale measures.")) for the evolutions of risky assets, given by formulas ([172](#S7.E172 "In 7 Derivatives assessment.")), ([179](#S7.E179 "In 7 Derivatives assessment.")), are fulfilled simultaneously.

For the evolution of risky assets ([179](#S7.E179 "In 7 Derivatives assessment.")), satisfying the conditions ([186](#S7.E186 "In 7 Derivatives assessment.")), the inequalities ([184](#S7.E184 "In 7 Derivatives assessment.")), ([185](#S7.E185 "In 7 Derivatives assessment.")) are true. From this, it follows that the conditions of Theorem [5](#Thmte5 "Theorem 5. ‣ 5 Optional decomposition for super-martingales.") are valid. This proves the optional decomposition for every nonnegative super-martingale relative to the family of martingale measures M.𝑀M. From [[17](#bib.bib17)], it follows the formula for the fair price f0subscript𝑓0f\_{0} of super-hedge

|  |  |  |  |
| --- | --- | --- | --- |
|  | f0=supP∈MEP​f​(SN).subscript𝑓0subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁\displaystyle f\_{0}=\sup\limits\_{P\in M}E^{P}f(S\_{N}). |  | (200) |

Further, the conditions of Theorem [8](#Thmte8 "Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.") is also true. Therefore, the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supP∈MEP​f​(SN)=supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2\displaystyle\sup\limits\_{P\in M}E^{P}f(S\_{N})=\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}} |  | (201) |

is valid.

To complete the proof of Theorem [9](#Thmte9 "Theorem 9. ‣ 7 Derivatives assessment."), it needs to show that the set
M1⊆M.subscript𝑀1𝑀M\_{1}\subseteq M.
Let us denote Sn3​(ω1,…,ωn)superscriptsubscript𝑆𝑛3subscript𝜔1…subscript𝜔𝑛S\_{n}^{3}(\omega\_{1},\ldots,\omega\_{n}) the evolution of risky asset, given by the formula ([178](#S7.E178 "In 7 Derivatives assessment.")). Then, as above

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn3​(ω1,…,ωn)Sn2​(ω1,…,ωn)≤∏i=1n1ai=Cn,n=1,N¯.formulae-sequencesuperscriptsubscript𝑆𝑛3subscript𝜔1…subscript𝜔𝑛superscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛superscriptsubscriptproduct𝑖1𝑛1subscript𝑎𝑖subscript𝐶𝑛𝑛¯  1𝑁\displaystyle\frac{S\_{n}^{3}(\omega\_{1},\ldots,\omega\_{n})}{S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n})}\leq\prod\limits\_{i=1}^{n}\frac{1}{a\_{i}}=C\_{n},\quad n=\overline{1,N}. |  | (202) |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | |Δ​Sn3​(ω1,…,ωn−1,ωn)||Δ​Sn2​(ω1,…,ωn−1,ωn)|=Δsuperscriptsubscript𝑆𝑛3subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛Δsuperscriptsubscript𝑆𝑛2subscript𝜔1…subscript𝜔𝑛1subscript𝜔𝑛absent\frac{|\Delta S\_{n}^{3}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|}{|\Delta S\_{n}^{2}(\omega\_{1},\ldots,\omega\_{n-1},\omega\_{n})|}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn−13​(ω1,…,ωn−1)Sn−12​(ω1,…,ωn−1)​an≤max1≤n≤N⁡Cnmin1≤n≤N⁡an,n=1,N¯.formulae-sequencesuperscriptsubscript𝑆𝑛13subscript𝜔1…subscript𝜔𝑛1superscriptsubscript𝑆𝑛12subscript𝜔1…subscript𝜔𝑛1subscript𝑎𝑛subscript1𝑛𝑁subscript𝐶𝑛subscript1𝑛𝑁subscript𝑎𝑛𝑛¯  1𝑁\displaystyle\frac{S\_{n-1}^{3}(\omega\_{1},\ldots,\omega\_{n-1})}{S\_{n-1}^{2}(\omega\_{1},\ldots,\omega\_{n-1})a\_{n}}\leq\frac{\max\limits\_{1\leq n\leq N}C\_{n}}{\min\limits\_{1\leq n\leq N}a\_{n}},\quad n=\overline{1,N}. |  | (203) |

The inequality ([203](#S7.E203 "In Proof. ‣ 7 Derivatives assessment.")) proves the needed statement.
Theorem [9](#Thmte9 "Theorem 9. ‣ 7 Derivatives assessment.") is proved.
∎

###### Theorem 10.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([172](#S7.E172 "In 7 Derivatives assessment.")). Suppose that 0≤ai​(ω1,…,ωi−1)≤1,0subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖110\leq a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\leq 1, σi​(ω1,…,ωi−1)>σi>0,i=1,N¯,formulae-sequencesubscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0𝑖¯

1𝑁\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,\ i=\overline{1,N},
and an=1subscript𝑎𝑛1a\_{n}=1 for a certain 1≤n≤N.1𝑛𝑁1\leq n\leq N.
If the nonnegative payoff function f​(x),x∈[0,∞),

𝑓𝑥𝑥
0f(x),\ x\in[0,\infty), satisfies the conditions:
  
1) f​(0)=0,f​(x)≤a​x,limx→∞f​(x)x=a,a>0,formulae-sequence𝑓00formulae-sequence𝑓𝑥𝑎𝑥formulae-sequencesubscript→𝑥𝑓𝑥𝑥𝑎𝑎0f(0)=0,\ f(x)\leq ax,\ \lim\limits\_{x\to\infty}\frac{f(x)}{x}=a,\ a>0,
then

|  |  |  |  |
| --- | --- | --- | --- |
|  | supP∈MEP​f​(SN)=a​S0.subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑎subscript𝑆0\displaystyle\sup\limits\_{P\in M}E^{P}f(S\_{N})=aS\_{0}. |  | (204) |

If, in addition, the nonnegative payoff function f​(x)𝑓𝑥f(x) is a convex down one, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)=f​(S0),subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})=f(S\_{0}), |  | (205) |

where M𝑀M is a set of equivalent martingale measures for the evolution of risky asset, given by the formula ([172](#S7.E172 "In 7 Derivatives assessment.")). The interval of non-arbitrage prices of contingent liability f​(SN)𝑓subscript𝑆𝑁f(S\_{N}) lies in the set [f​(S0),a​S0].𝑓subscript𝑆0𝑎subscript𝑆0[f(S\_{0}),aS\_{0}].

###### Proof.

Since the conditions of Theorem [9](#Thmte9 "Theorem 9. ‣ 7 Derivatives assessment.") are satisfied, then the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈M∫ΩNf​(SN)​𝑑Q=supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}subscriptsupremum𝑄𝑀subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-d𝑄subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2\displaystyle\sup\limits\_{Q\in M}\int\limits\_{\Omega\_{N}}f(S\_{N})dQ=\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}} |  | (206) |

is true, where for the spot measure μ{ω11,ω12},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) the representation

|  |  |  |
| --- | --- | --- |
|  | μ{ω11,ω12},…,{ωN1,ωN2}​(A)=subscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴absent\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i1=12…​∑iN=12∏j=1Nψj​(ω1i1,…,ωjij)​χA​(ω1i1,…,ωNiN),A∈ℱN,  superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐴superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁𝐴 subscriptℱ𝑁\displaystyle\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{A}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}}),\quad A\in{\cal F}\_{N}, |  | (207) |

is valid, and

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}=subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2absent\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}= |  |

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))),𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right), |  | (208) |

where we denoted
Ωs0−={ωs∈Ωs0,εs​(ωs)≤0},superscriptsubscriptΩ𝑠limit-from0formulae-sequencesubscript𝜔𝑠superscriptsubscriptΩ𝑠0subscript𝜀𝑠subscript𝜔𝑠0\Omega\_{s}^{0-}=\{\omega\_{s}\in\Omega\_{s}^{0},\ \varepsilon\_{s}(\omega\_{s})\leq 0\},
Ωs0+={ωs∈Ωs0,εs​(ωs)>0}.superscriptsubscriptΩ𝑠limit-from0formulae-sequencesubscript𝜔𝑠superscriptsubscriptΩ𝑠0subscript𝜀𝑠subscript𝜔𝑠0\Omega\_{s}^{0+}=\{\omega\_{s}\in\Omega\_{s}^{0},\ \varepsilon\_{s}(\omega\_{s})>0\}.
From the inequality, f​(SN)≤a​SN,𝑓subscript𝑆𝑁𝑎subscript𝑆𝑁f(S\_{N})\leq aS\_{N}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈M∫Ωf​(SN)​𝑑Q≤a​S0.subscriptsupremum𝑄𝑀subscriptΩ𝑓subscript𝑆𝑁differential-d𝑄𝑎subscript𝑆0\displaystyle\sup\limits\_{Q\in M}\int\limits\_{\Omega}f(S\_{N})dQ\leq aS\_{0}. |  | (209) |

To prove the inverse inequality, we use the inequality

|  |  |  |
| --- | --- | --- |
|  | supQ∈M∫Ωf​(SN)​𝑑Q≥subscriptsupremum𝑄𝑀subscriptΩ𝑓subscript𝑆𝑁differential-d𝑄absent\sup\limits\_{Q\in M}\int\limits\_{\Omega}f(S\_{N})dQ\geq |  |

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))).𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right). |  | (210) |

In the right hand side of the last inequality, let us put εs​(ωs1)=0,s≠n.formulae-sequencesubscript𝜀𝑠superscriptsubscript𝜔𝑠10𝑠𝑛\varepsilon\_{s}(\omega\_{s}^{1})=0,\ s\neq n. Such elementary events ωs1superscriptsubscript𝜔𝑠1\omega\_{s}^{1} exist, due to the conditions relative to the random values εs​(ωs),s=1,N¯.

subscript𝜀𝑠subscript𝜔𝑠𝑠
¯

1𝑁\varepsilon\_{s}(\omega\_{s}),\ s=\overline{1,N}.
We obtain

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))=𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑in=12ψn​(ω11,…,ωn−11,ωnin)​f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωnin)).superscriptsubscriptsubscript𝑖𝑛12subscript𝜓𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛subscript𝑖𝑛𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛subscript𝑖𝑛\displaystyle\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{i\_{n}})f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{i\_{n}})}\right). |  | (211) |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | supQ∈M∫Ωf​(SN)​𝑑Q≥subscriptsupremum𝑄𝑀subscriptΩ𝑓subscript𝑆𝑁differential-d𝑄absent\sup\limits\_{Q\in M}\int\limits\_{\Omega}f(S\_{N})dQ\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | supωn1∈Ωn0−,ωn2∈Ωn0+∑in=12ψn​(ω11,…,ωn−11,ωnin)​f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωnin)).subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptsubscript𝑖𝑛12subscript𝜓𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛subscript𝑖𝑛𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛subscript𝑖𝑛\displaystyle\sup\limits\_{\omega\_{n}^{1}\in\Omega\_{n}^{0-},\omega\_{n}^{2}\in\Omega\_{n}^{0+}}\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{i\_{n}})f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{i\_{n}})}\right). |  | (212) |

Further,

|  |  |  |
| --- | --- | --- |
|  | supωn1∈Ωn0−,ωn2∈Ωn0+∑in=12ψn(ω11,…,ωnin)×\sup\limits\_{\omega\_{n}^{1}\in\Omega\_{n}^{0-},\omega\_{n}^{2}\in\Omega\_{n}^{0+}}\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n}^{i\_{n}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωnin))=𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛subscript𝑖𝑛absentf\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{i\_{n}})}\right)= |  |

|  |  |  |
| --- | --- | --- |
|  | supωn1∈Ωn0−,ωn2∈Ωn0+[Δ​Sn+​(ω11,…,ωn−11,ωn2)Vn​(ω11,…,ωn−11,ωn1,ωn2)f(S0eσn​(ω11,…,ωn−11)​εn​(ωn1))+\sup\limits\_{\omega\_{n}^{1}\in\Omega\_{n}^{0-},\omega\_{n}^{2}\in\Omega\_{n}^{0+}}\left[\frac{\Delta S\_{n}^{+}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1},\omega\_{n}^{2})}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}\right)+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω11,…,ωn−11,ωn1)Vn​(ω11,…,ωn−11,ωn1,ωn2)f(S0eσn​(ω11,…,ωn−11)​εn​(ωn2))]≥\left.\frac{\Delta S\_{n}^{-}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1},\omega\_{n}^{2})}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}\right)\right]\geq |  |

|  |  |  |
| --- | --- | --- |
|  | limεn​(ωn2)→∞limεn​(ωn1)→−∞[eσn​(ω11,…,ωn−11)​εn​(ωn2)−1eσn​(ω11,…,ωn−11)​εn​(ωn2)−eσn​(ω11,…,ωn−11)​εn​(ωn1)×\lim\limits\_{\varepsilon\_{n}(\omega\_{n}^{2})\to\infty}\lim\limits\_{\varepsilon\_{n}(\omega\_{n}^{1})\to-\infty}\left[\frac{e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}-1}{e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}-e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}}\times\right. |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωn1))+limit-from𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛1f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}\right)+ |  |

|  |  |  |
| --- | --- | --- |
|  | 1−eσn​(ω11,…,ωn−11)​εn​(ωn1)eσn​(ω11,…,ωn−11)​εn​(ωn2)−eσn​(ω11,…,ωn−11)​εn​(ωn1)f(S0eσn​(ω11,…,ωn−11)​εn​(ωn2))]=\left.\frac{1-e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}}{e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}-e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}\right)\right]= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | limεn​(ωn2)→∞1eσn​(ω11,…,ωn−11)​εn​(ωn2)​f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωn2))=a​S0.subscript→subscript𝜀𝑛superscriptsubscript𝜔𝑛21superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛2𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛2𝑎subscript𝑆0\displaystyle\lim\limits\_{\varepsilon\_{n}(\omega\_{n}^{2})\to\infty}\frac{1}{e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}\right)=aS\_{0}. |  | (213) |

Substituting the inequality ([213](#S7.E213 "In Proof. ‣ 7 Derivatives assessment.")) into the inequality ([211](#S7.E211 "In Proof. ‣ 7 Derivatives assessment.")), we obtain the needed inequality.

Let us prove the equality ([205](#S7.E205 "In Theorem 10. ‣ 7 Derivatives assessment.")).
Using the Jensen inequality, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)≥f​(EP​SN)=f​(S0).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓superscript𝐸𝑃subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})\geq f(E^{P}S\_{N})=f(S\_{0}). |  | (214) |

Let us prove the inverse inequality. It is evident that

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≥𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N}). |  | (215) |

Putting in this inequality εi​(ωi1)=0,i=1,N¯,formulae-sequencesubscript𝜀𝑖superscriptsubscript𝜔𝑖10𝑖¯

1𝑁\varepsilon\_{i}(\omega\_{i}^{1})=0,\ i=\overline{1,N}, we obtain the needed. The last statement about the interval of non-arbitrage prices follows from [[7](#bib.bib7)] and [[6](#bib.bib6)]. Theorem [10](#Thmte10 "Theorem 10. ‣ 7 Derivatives assessment.") is proved.
∎

###### Theorem 11.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([172](#S7.E172 "In 7 Derivatives assessment.")). Suppose that 0≤ai​(ω1,…,ωi−1)≤1,0subscript𝑎𝑖subscript𝜔1…subscript𝜔𝑖110\leq a\_{i}(\omega\_{1},\ldots,\omega\_{i-1})\leq 1, σi​(ω1,…,ωi−1)>σi>0,i=1,N¯,formulae-sequencesubscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0𝑖¯

1𝑁\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,\ i=\overline{1,N},
and an=1subscript𝑎𝑛1a\_{n}=1 for a certain 1≤n≤N.1𝑛𝑁1\leq n\leq N.
If the nonnegative payoff function f​(x),x∈[0,∞),

𝑓𝑥𝑥
0f(x),\ x\in[0,\infty), satisfies the conditions:
  
1) f​(0)=K,f​(x)≤K,formulae-sequence𝑓0𝐾𝑓𝑥𝐾f(0)=K,\ f(x)\leq K,
then

|  |  |  |  |
| --- | --- | --- | --- |
|  | supP∈MEP​f​(SN)=K.subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝐾\displaystyle\sup\limits\_{P\in M}E^{P}f(S\_{N})=K. |  | (216) |

If, in addition, the nonnegative payoff function f​(x)𝑓𝑥f(x) is a convex down one, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)=f​(S0),subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})=f(S\_{0}), |  | (217) |

where M𝑀M is a set of equivalent maqtingale measures for the evolution of risky asset, given by the formula ([172](#S7.E172 "In 7 Derivatives assessment.")). The interval of non-arbitrage prices of contingent liability f​(SN)𝑓subscript𝑆𝑁f(S\_{N}) coincides with the set [f​(S0),K].𝑓subscript𝑆0𝐾[f(S\_{0}),K].

###### Proof.

Due to Theorem [9](#Thmte9 "Theorem 9. ‣ 7 Derivatives assessment."), the equality

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈M∫ΩNf​(SN)​𝑑Q=supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}subscriptsupremum𝑄𝑀subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-d𝑄subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2\displaystyle\sup\limits\_{Q\in M}\int\limits\_{\Omega\_{N}}f(S\_{N})dQ=\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}} |  | (218) |

is valid, where for the spot measure μ{ω11,ω12},…,{ωN1,ωN2}​(A)subscript𝜇

superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A) the representation

|  |  |  |
| --- | --- | --- |
|  | μ{ω11,ω12},…,{ωN1,ωN2}​(A)=subscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2𝐴absent\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}(A)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i1=12…​∑iN=12∏j=1Nψj​(ω1i1,…,ωjij)​χA​(ω1i1,…,ωNiN),A∈ℱN,  superscriptsubscriptsubscript𝑖112…superscriptsubscriptsubscript𝑖𝑁12superscriptsubscriptproduct𝑗1𝑁subscript𝜓𝑗superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑗subscript𝑖𝑗subscript𝜒𝐴superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁𝐴 subscriptℱ𝑁\displaystyle\sum\limits\_{i\_{1}=1}^{2}\ldots\sum\limits\_{i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\chi\_{A}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}}),\quad A\in{\cal F}\_{N}, |  | (219) |

is true, and

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}=subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2absent\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}= |  |

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))).𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right). |  | (220) |

It is evident that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supP∈MEP​f​(SN)≤K.subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝐾\displaystyle\sup\limits\_{P\in M}E^{P}f(S\_{N})\leq K. |  | (221) |

Further,

|  |  |  |
| --- | --- | --- |
|  | supQ∈M∫Ωf​(SN)​𝑑Q≥subscriptsupremum𝑄𝑀subscriptΩ𝑓subscript𝑆𝑁differential-d𝑄absent\sup\limits\_{Q\in M}\int\limits\_{\Omega}f(S\_{N})dQ\geq |  |

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))).𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right). |  | (222) |

In the right hand side of the last inequality, let us put εs​(ωs1)=0,s≠n.formulae-sequencesubscript𝜀𝑠superscriptsubscript𝜔𝑠10𝑠𝑛\varepsilon\_{s}(\omega\_{s}^{1})=0,\ s\neq n.
We obtain

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))=𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑in=12ψn​(ω11,…,ωn−11,ωnin)​f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωnin)).superscriptsubscriptsubscript𝑖𝑛12subscript𝜓𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛subscript𝑖𝑛𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛subscript𝑖𝑛\displaystyle\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{i\_{n}})f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{i\_{n}})}\right). |  | (223) |

From the last equality, we obtain

|  |  |  |
| --- | --- | --- |
|  | supQ∈M∫Ωf​(SN)​𝑑Q≥subscriptsupremum𝑄𝑀subscriptΩ𝑓subscript𝑆𝑁differential-d𝑄absent\sup\limits\_{Q\in M}\int\limits\_{\Omega}f(S\_{N})dQ\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | supωn1∈Ωn0−,ωn2∈Ωn0+∑in=12ψn​(ω11,…,ωn−11,ωnin)​f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωnin)).subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptsubscript𝑖𝑛12subscript𝜓𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛subscript𝑖𝑛𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛subscript𝑖𝑛\displaystyle\sup\limits\_{\omega\_{n}^{1}\in\Omega\_{n}^{0-},\omega\_{n}^{2}\in\Omega\_{n}^{0+}}\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{i\_{n}})f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{i\_{n}})}\right). |  | (224) |

Further,

|  |  |  |
| --- | --- | --- |
|  | supωn1∈Ωn0−,ωn2∈Ωn0+∑in=12ψn​(ω11,…,ωn−11,ωnin)​f​(S0​eσn​(ω11,…,ωn−11)​εn​(ωnin))=subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑛1superscriptsubscriptΩ𝑛limit-from0superscriptsubscript𝜔𝑛2superscriptsubscriptΩ𝑛limit-from0superscriptsubscriptsubscript𝑖𝑛12subscript𝜓𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11superscriptsubscript𝜔𝑛subscript𝑖𝑛𝑓subscript𝑆0superscript𝑒subscript𝜎𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛11subscript𝜀𝑛superscriptsubscript𝜔𝑛subscript𝑖𝑛absent\sup\limits\_{\omega\_{n}^{1}\in\Omega\_{n}^{0-},\omega\_{n}^{2}\in\Omega\_{n}^{0+}}\sum\limits\_{i\_{n}=1}^{2}\psi\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{i\_{n}})f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{i\_{n}})}\right)= |  |

|  |  |  |
| --- | --- | --- |
|  | supωn1∈Ωn0−,ωn2∈Ωn0+[Δ​Sn+​(ω11,…,ωn−11,ωn2)Vn​(ω11,…,ωn−11,ωn1,ωn2)f(S0eσn​(ω11,…,ωn−11)​εn​(ωn1))+\sup\limits\_{\omega\_{n}^{1}\in\Omega\_{n}^{0-},\omega\_{n}^{2}\in\Omega\_{n}^{0+}}\left[\frac{\Delta S\_{n}^{+}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{2})}{V\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1},\omega\_{n}^{2})}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}\right)+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Sn−​(ω11,…,ωn−11,ωn1)Vn​(ω11,…,ωn−11,ωn1,ωn2)f(S0eσn​(ω11,…,ωn−11)​εn​(ωn2))]≥\left.\frac{\Delta S\_{n}^{-}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1})}{V\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1},\omega\_{n}^{1},\omega\_{n}^{2})}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}\right)\right]\geq |  |

|  |  |  |
| --- | --- | --- |
|  | limε​(ωn2)→∞limε​(ωn1)→−∞[eσn​(ω11,…,ωn−11)​εn​(ωn2)−1eσn​(ω11,…,ωn−11)​εn​(ωn2)−eσn​(ω11,…,ωn−11)​εn​(ωn1)f(S0eσn​(ω11,…,ωn−11)​εn​(ωn1))+\lim\limits\_{\varepsilon(\omega\_{n}^{2})\to\infty}\lim\limits\_{\varepsilon(\omega\_{n}^{1})\to-\infty}\left[\frac{e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}-1}{e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}-e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}\right)+\right. |  |

|  |  |  |
| --- | --- | --- |
|  | 1−eσn​(ω11,…,ωn−11)​εn​(ωn1)eσn​(ω11,…,ωn−11)​εn​(ωn2)−eσn​(ω11,…,ωn−11)​εn​(ωn1)f(S0eσn​(ω11,…,ωn−11)​εn​(ωn2))]=\left.\frac{1-e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}}{e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}-e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{1})}}f\left(S\_{0}e^{\sigma\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n-1}^{1})\varepsilon\_{n}(\omega\_{n}^{2})}\right)\right]= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(0)=K.𝑓0𝐾\displaystyle f(0)=K. |  | (225) |

Substituting the inequality ([225](#S7.E225 "In Proof. ‣ 7 Derivatives assessment.")) into the inequality ([223](#S7.E223 "In Proof. ‣ 7 Derivatives assessment.")), we obtain the needed inequality.

Let us prove the equality ([217](#S7.E217 "In Theorem 11. ‣ 7 Derivatives assessment.")). Due to the convexity of the payoff function f​(x),𝑓𝑥f(x), using the Jensen inequality, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)≥f​(EP​SN)=f​(S0).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓superscript𝐸𝑃subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})\geq f(E^{P}S\_{N})=f(S\_{0}). |  | (226) |

Let us prove the inverse inequality. It is evident that

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(ω1i1,…,ωs−1is−1)​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≥𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N}). |  | (227) |

Putting in this inequality εi​(ωi1)=0,i=1,N¯,formulae-sequencesubscript𝜀𝑖superscriptsubscript𝜔𝑖10𝑖¯

1𝑁\varepsilon\_{i}(\omega\_{i}^{1})=0,\ i=\overline{1,N}, we obtain the needed. The last statement about the interval of non-arbitrage prices follows from [[7](#bib.bib7)] and [[6](#bib.bib6)].
Theorem [11](#Thmte11 "Theorem 11. ‣ 7 Derivatives assessment.") is proved.
∎

###### Theorem 12.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")). Suppose that 0≤ai≤1,0subscript𝑎𝑖10\leq a\_{i}\leq 1, σi​(ω1,…,ωi−1)>σi>0,subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,
i=1,N¯.𝑖¯

1𝑁\ i=\overline{1,N}.
If the nonnegative payoff function f​(x),x∈[0,∞),

𝑓𝑥𝑥
0f(x),\ x\in[0,\infty), satisfies the conditions:
  
1) f​(0)=0,f​(x)≤a​x,limx→∞f​(x)x=a,a>0,formulae-sequence𝑓00formulae-sequence𝑓𝑥𝑎𝑥formulae-sequencesubscript→𝑥𝑓𝑥𝑥𝑎𝑎0f(0)=0,\ f(x)\leq ax,\ \lim\limits\_{x\to\infty}\frac{f(x)}{x}=a,\ a>0,
then the inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏i=1N(1−ai))+a​S0​(1−∏i=1N(1−ai))≤supP∈MEP​f​(SN)≤a​S0𝑓subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖𝑎subscript𝑆01superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑎subscript𝑆0\displaystyle f\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right)+aS\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right)\leq\sup\limits\_{P\in M}E^{P}f(S\_{N})\leq aS\_{0} |  | (228) |

are true.
If, in addition, the nonnegative payoff function f​(x)𝑓𝑥f(x) is a convex down one, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)=f​(S0),subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})=f(S\_{0}), |  | (229) |

where M𝑀M is the set of equivalent martingale measures for the evolution of risky asset, given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")).

###### Proof.

As before,

|  |  |  |
| --- | --- | --- |
|  | a​S0≥supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}=𝑎subscript𝑆0subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2absentaS\_{0}\geq\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}= |  |

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))).𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right). |  | (230) |

|  |  |  |
| --- | --- | --- |
|  | supωN1∈ΩN0−,ωN2∈ΩN0+∑iN=12ψN(ω1i1,…,ωNiN)×\sup\limits\_{\omega\_{N}^{1}\in\Omega\_{N}^{0-},\omega\_{N}^{2}\in\Omega\_{N}^{0+}}\sum\limits\_{i\_{N}=1}^{2}\psi\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))=𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)= |  |

|  |  |  |
| --- | --- | --- |
|  | supωN1∈ΩN0−,ωN2∈ΩN0+[Δ​SN+​(ω1i1,…,ωN−1iN−1,ωN2)VN​(ω1i1,…,ωN−1iN−1,ωN1,ωN2)×\sup\limits\_{\omega\_{N}^{1}\in\Omega\_{N}^{0-},\omega\_{N}^{2}\in\Omega\_{N}^{0+}}\left[\frac{\Delta S\_{N}^{+}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{2})}{V\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{1},\omega\_{N}^{2})}\times\right. |  |

|  |  |  |
| --- | --- | --- |
|  | f​(SN−1​(1+aN​(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)−1)))+limit-from𝑓subscript𝑆𝑁11subscript𝑎𝑁superscript𝑒subscript𝜎𝑁superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁1subscript𝑖𝑁1subscript𝜀𝑁superscriptsubscript𝜔𝑁11f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}-1\right)\right)\right)+ |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​SN−​(ω1i1,…,ωN−1iN−1,ωN1)VN​(ω1i1,…,ωN−1iN−1,ωN1,ωN2)f(SN−1(1+aN(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−1)))]≥\left.\frac{\Delta S\_{N}^{-}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{1})}{V\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{1},\omega\_{N}^{2})}f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-1\right)\right)\right)\right]\geq |  |

|  |  |  |
| --- | --- | --- |
|  | limεN​(ωN2)→∞limεN​(ωN1)→−∞[eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−1eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)×\lim\limits\_{\varepsilon\_{N}(\omega\_{N}^{2})\to\infty}\lim\limits\_{\varepsilon\_{N}(\omega\_{N}^{1})\to-\infty}\left[\frac{e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-1}{e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}}\times\right. |  |

|  |  |  |
| --- | --- | --- |
|  | f​(SN−1​(1+aN​(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)−1)))+limit-from𝑓subscript𝑆𝑁11subscript𝑎𝑁superscript𝑒subscript𝜎𝑁superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁1subscript𝑖𝑁1subscript𝜀𝑁superscriptsubscript𝜔𝑁11f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}-1\right)\right)\right)+ |  |

|  |  |  |
| --- | --- | --- |
|  | 1−eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)×\left.\frac{1-e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}}{e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}}\times\right. |  |

|  |  |  |
| --- | --- | --- |
|  | f(SN−1(1+aN(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−1)))]=\left.f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-1\right)\right)\right)\right]= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(SN−1​(1−aN))+a​aN​SN−1,𝑓subscript𝑆𝑁11subscript𝑎𝑁𝑎subscript𝑎𝑁subscript𝑆𝑁1\displaystyle f(S\_{N-1}(1-a\_{N}))+aa\_{N}S\_{N-1}, |  | (231) |

where we put

|  |  |  |  |
| --- | --- | --- | --- |
|  | SN−1=S0​∏s=1N−1(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)).subscript𝑆𝑁1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁11subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle S\_{N-1}=S\_{0}\prod\limits\_{s=1}^{N-1}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right). |  | (232) |

Substituting the inequality ([231](#S7.E231 "In Proof. ‣ 7 Derivatives assessment.")) into ([230](#S7.E230 "In Proof. ‣ 7 Derivatives assessment.")), we obtain the inequality

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≥𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\geq |  |

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N−1¯∑i1=1,…,iN−1=12∏j=1N−1ψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N-1}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N-1}=1}^{2}\prod\limits\_{j=1}^{N-1}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​(1−aN)​∏s=1N−1(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))+a​aN​S0.𝑓subscript𝑆01subscript𝑎𝑁superscriptsubscriptproduct𝑠1𝑁11subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1𝑎subscript𝑎𝑁subscript𝑆0\displaystyle f\left(S\_{0}(1-a\_{N})\prod\limits\_{s=1}^{N-1}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)+aa\_{N}S\_{0}. |  | (233) |

Applying (N−1)𝑁1(N-1) times the inequality ([233](#S7.E233 "In Proof. ‣ 7 Derivatives assessment.")), we obtain the inequality

|  |  |  |
| --- | --- | --- |
|  | supQ∈M∫Ωf​(SN)​𝑑Q≥f​(S0​∏i=1N(1−ai))+a​S0​∑i=1Nai​∏s=i+1N(1−as)=subscriptsupremum𝑄𝑀subscriptΩ𝑓subscript𝑆𝑁differential-d𝑄𝑓subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖𝑎subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑎𝑖superscriptsubscriptproduct𝑠𝑖1𝑁1subscript𝑎𝑠absent\sup\limits\_{Q\in M}\int\limits\_{\Omega}f(S\_{N})dQ\geq f(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i}))+aS\_{0}\sum\limits\_{i=1}^{N}a\_{i}\prod\limits\_{s=i+1}^{N}(1-a\_{s})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏i=1N(1−ai))+a​S0​(1−∏i=1N(1−ai)).𝑓subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖𝑎subscript𝑆01superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖\displaystyle f\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right)+aS\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right). |  | (234) |

Let us prove the equality ([229](#S7.E229 "In Theorem 12. ‣ 7 Derivatives assessment.")). Using the Jensen inequality, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)≥f​(S0).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})\geq f(S\_{0}). |  | (235) |

Let us prove the inverse inequality. It is evident that

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≥𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N}). |  | (236) |

Putting in the inequality ([236](#S7.E236 "In Proof. ‣ 7 Derivatives assessment.")) εn​(ωn)=0,n=1,N¯,formulae-sequencesubscript𝜀𝑛subscript𝜔𝑛0𝑛¯

1𝑁\varepsilon\_{n}(\omega\_{n})=0,n=\overline{1,N}, we obtain the inverse inequality.
∎

###### Theorem 13.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")). Suppose that 0≤ai≤1,0subscript𝑎𝑖10\leq a\_{i}\leq 1, σi​(ω1,…,ωi−1)>σi>0,subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,
i=1,N¯.𝑖¯

1𝑁\ i=\overline{1,N}.
If the nonnegative payoff function f​(x),x∈[0,∞),

𝑓𝑥𝑥
0f(x),\ x\in[0,\infty), satisfies the conditions:
  
1) f​(0)=K,f​(x)≤K,formulae-sequence𝑓0𝐾𝑓𝑥𝐾f(0)=K,\ f(x)\leq K,
then

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏i=1N(1−ai))≤supP∈MEP​f​(SN)≤K.𝑓subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖subscriptsupremum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝐾\displaystyle f\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right)\leq\sup\limits\_{P\in M}E^{P}f(S\_{N})\leq K. |  | (237) |

If, in addition, the nonnegative payoff function f​(x)𝑓𝑥f(x) is a convex down one, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)=f​(S0),subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})=f(S\_{0}), |  | (238) |

where M𝑀M is the set of equivalent martingale measures for the evolution of risky asset, given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")).

###### Proof.

Let us obtain the estimate from below. Really,

|  |  |  |
| --- | --- | --- |
|  | a​K≥supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∫ΩNf​(SN)​𝑑μ{ω11,ω12},…,{ωN1,ωN2}=𝑎𝐾subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑖1superscriptsubscriptΩ𝑖limit-from0formulae-sequencesuperscriptsubscript𝜔𝑖2superscriptsubscriptΩ𝑖limit-from0𝑖¯  1𝑁subscriptsubscriptΩ𝑁𝑓subscript𝑆𝑁differential-dsubscript𝜇  superscriptsubscript𝜔11superscriptsubscript𝜔12…superscriptsubscript𝜔𝑁1superscriptsubscript𝜔𝑁2absentaK\geq\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\int\limits\_{\Omega\_{N}}f(S\_{N})d\mu\_{\{\omega\_{1}^{1},\omega\_{1}^{2}\},\ldots,\{\omega\_{N}^{1},\omega\_{N}^{2}\}}= |  |

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))).𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right). |  | (239) |

Further,

|  |  |  |
| --- | --- | --- |
|  | supωN1∈ΩN0−,ωN2∈ΩN0+∑iN=12ψN​(ω1i1,…,ωNiN)​f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))=subscriptsupremumformulae-sequencesuperscriptsubscript𝜔𝑁1superscriptsubscriptΩ𝑁limit-from0superscriptsubscript𝜔𝑁2superscriptsubscriptΩ𝑁limit-from0superscriptsubscriptsubscript𝑖𝑁12subscript𝜓𝑁superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁subscript𝑖𝑁𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absent\sup\limits\_{\omega\_{N}^{1}\in\Omega\_{N}^{0-},\omega\_{N}^{2}\in\Omega\_{N}^{0+}}\sum\limits\_{i\_{N}=1}^{2}\psi\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N}^{i\_{N}})f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)= |  |

|  |  |  |
| --- | --- | --- |
|  | supωN1∈ΩN0−,ωN2∈ΩN0+[Δ​SN+​(ω1i1,…,ωN−1iN−1,ωN2)VN​(ω1i1,…,ωN−1iN−1,ωN1,ωN2)×\sup\limits\_{\omega\_{N}^{1}\in\Omega\_{N}^{0-},\omega\_{N}^{2}\in\Omega\_{N}^{0+}}\left[\frac{\Delta S\_{N}^{+}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{2})}{V\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{1},\omega\_{N}^{2})}\times\right. |  |

|  |  |  |
| --- | --- | --- |
|  | f​(SN−1​(1+aN​(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)−1)))+limit-from𝑓subscript𝑆𝑁11subscript𝑎𝑁superscript𝑒subscript𝜎𝑁superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁1subscript𝑖𝑁1subscript𝜀𝑁superscriptsubscript𝜔𝑁11f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}-1\right)\right)\right)+ |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​SN−​(ω1i1,…,ωN−1iN−1,ωN1)VN​(ω1i1,…,ωN−1iN−1,ωN1,ωN2)f(SN−1(1+aN(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−1)))]≥\left.\frac{\Delta S\_{N}^{-}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{1})}{V\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}},\omega\_{N}^{1},\omega\_{N}^{2})}f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-1\right)\right)\right)\right]\geq |  |

|  |  |  |
| --- | --- | --- |
|  | limεN​(ωN2)→∞limεN​(ωN1)→−∞[eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−1eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)×\lim\limits\_{\varepsilon\_{N}(\omega\_{N}^{2})\to\infty}\lim\limits\_{\varepsilon\_{N}(\omega\_{N}^{1})\to-\infty}\left[\frac{e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-1}{e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}}\times\right. |  |

|  |  |  |
| --- | --- | --- |
|  | f​(SN−1​(1+aN​(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)−1)))+limit-from𝑓subscript𝑆𝑁11subscript𝑎𝑁superscript𝑒subscript𝜎𝑁superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑁1subscript𝑖𝑁1subscript𝜀𝑁superscriptsubscript𝜔𝑁11f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}-1\right)\right)\right)+ |  |

|  |  |  |
| --- | --- | --- |
|  | 1−eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN1)×\left.\frac{1-e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}}{e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{1})}}\times\right. |  |

|  |  |  |
| --- | --- | --- |
|  | f(SN−1(1+aN(eσN​(ω1i1,…,ωN−1iN−1)​εN​(ωN2)−1)))]=\left.f\left(S\_{N-1}\left(1+a\_{N}\left(e^{\sigma\_{N}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{N-1}^{i\_{N-1}})\varepsilon\_{N}(\omega\_{N}^{2})}-1\right)\right)\right)\right]= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(SN−1​(1−aN)),𝑓subscript𝑆𝑁11subscript𝑎𝑁\displaystyle f(S\_{N-1}(1-a\_{N})), |  | (240) |

where we put

|  |  |  |  |
| --- | --- | --- | --- |
|  | SN−1=S0​∏s=1N−1(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)).subscript𝑆𝑁1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁11subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle S\_{N-1}=S\_{0}\prod\limits\_{s=1}^{N-1}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right). |  | (241) |

Substituting the inequality ([240](#S7.E240 "In Proof. ‣ 7 Derivatives assessment.")) into ([239](#S7.E239 "In Proof. ‣ 7 Derivatives assessment.")), we obtain the inequality

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≥𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\geq |  |

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N−1¯∑i1=1,…,iN−1=12∏j=1N−1ψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N-1}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N-1}=1}^{2}\prod\limits\_{j=1}^{N-1}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​(1−aN)​∏s=1N−1(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))).𝑓subscript𝑆01subscript𝑎𝑁superscriptsubscriptproduct𝑠1𝑁11subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}(1-a\_{N})\prod\limits\_{s=1}^{N-1}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right). |  | (242) |

Applying (N−1)𝑁1(N-1) times the inequality ([242](#S7.E242 "In Proof. ‣ 7 Derivatives assessment.")), we obtain the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈M∫Ωf​(SN)​𝑑Q≥f​(S0​∏i=1N(1−ai)).subscriptsupremum𝑄𝑀subscriptΩ𝑓subscript𝑆𝑁differential-d𝑄𝑓subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖\displaystyle\sup\limits\_{Q\in M}\int\limits\_{\Omega}f(S\_{N})dQ\geq f(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})). |  | (243) |

Let us prove the equality ([238](#S7.E238 "In Theorem 13. ‣ 7 Derivatives assessment.")). Using the Jensen inequality we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN)≥f​(S0).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁𝑓subscript𝑆0\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N})\geq f(S\_{0}). |  | (244) |

Let us prove the inverse inequality. It is evident that

|  |  |  |
| --- | --- | --- |
|  | ∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≥𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absentf\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\geq |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈MEP​f​(SN).subscriptinfimum𝑃𝑀superscript𝐸𝑃𝑓subscript𝑆𝑁\displaystyle\inf\limits\_{P\in M}E^{P}f(S\_{N}). |  | (245) |

Putting in the inequality ([245](#S7.E245 "In Proof. ‣ 7 Derivatives assessment.")) εn​(ωn)=0,n=1,N¯,formulae-sequencesubscript𝜀𝑛subscript𝜔𝑛0𝑛¯

1𝑁\varepsilon\_{n}(\omega\_{n})=0,\ n=\overline{1,N}, we obtain the inverse inequality.
∎

###### Theorem 14.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")). Suppose that 0≤ai≤1,0subscript𝑎𝑖10\leq a\_{i}\leq 1, σi​(ω1,…,ωi−1)>σi>0,subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,
i=1,N¯.𝑖¯

1𝑁\ i=\overline{1,N}.
For the payoff function f​(x)=(x−K)+,x∈(0,∞),K>0,formulae-sequence𝑓𝑥superscript𝑥𝐾formulae-sequence𝑥0𝐾0f(x)=(x-K)^{+},\ x\in(0,\infty),\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |
| --- | --- | --- |
|  | supQ∈MEQ​f​(SN)=subscriptsupremum𝑄𝑀superscript𝐸𝑄𝑓subscript𝑆𝑁absent\sup\limits\_{Q\in M}E^{Q}f(S\_{N})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS0∏i=1N(1−ai))≥K,S0​(1−∏i=1N(1−ai)),ifS0​∏i=1N(1−ai)<K.\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i}))\geq K,\\ S\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right),&\mbox{if}\quad S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})<K.\end{array}\right. |  | (248) |

If S0∏i=1N(1−ai))≥K,S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i}))\geq K,
then the set of non arbitrage prices coincides with the point (S0−K)+,superscriptsubscript𝑆0𝐾(S\_{0}-K)^{+}, in case if S0​∏i=1N(1−ai)<Ksubscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖𝐾S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})<K the set of non arbitrage prices coincides with the set [(S0−K)+,S0​(1−∏i=1N(1−ai))].superscriptsubscript𝑆0𝐾subscript𝑆01superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖\left[(S\_{0}-K)^{+},S\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right)\right].

###### Proof.

Let us introduce the denotations

|  |  |  |
| --- | --- | --- |
|  | IN=∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×I\_{N}=\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))),𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right), |  | (249) |

|  |  |  |
| --- | --- | --- |
|  | IN1=∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×I\_{N}^{1}=\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))),subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right), |  | (250) |

|  |  |  |
| --- | --- | --- |
|  | IN0=supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×I\_{N}^{0}=\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1))),𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right), |  | (251) |

where we put f1​(x)=(K−x)+.subscript𝑓1𝑥superscript𝐾𝑥f\_{1}(x)=(K-x)^{+}.
Let us estimate from above the value IN.subscript𝐼𝑁I\_{N}. For this we use the equality

|  |  |  |  |
| --- | --- | --- | --- |
|  | IN=IN1+S0−K,subscript𝐼𝑁superscriptsubscript𝐼𝑁1subscript𝑆0𝐾\displaystyle I\_{N}=I\_{N}^{1}+S\_{0}-K, |  | (252) |

which follows from the identity: f​(x)=f1​(x)+x−K,x≥0.formulae-sequence𝑓𝑥subscript𝑓1𝑥𝑥𝐾𝑥0f(x)=f\_{1}(x)+x-K,\ x\geq 0.
Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≤f1​(S0​∏s=1N(1−as)),subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠\displaystyle f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\leq f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}(1-a\_{s})\right), |  | (253) |

we obtain the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | IN≤S0−K+f1​(S0​∏s=1N(1−as)).subscript𝐼𝑁subscript𝑆0𝐾subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠\displaystyle I\_{N}\leq S\_{0}-K+f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}(1-a\_{s})\right). |  | (254) |

From the inequality ([254](#S7.E254 "In Proof. ‣ 7 Derivatives assessment.")), we have

|  |  |  |
| --- | --- | --- |
|  | IN0≤S0−K+f1(S0∏s=1N(1−as)))=I\_{N}^{0}\leq S\_{0}-K+f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}(1-a\_{s}))\right)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS0∏i=1N(1−ai))≥K,S0​(1−∏i=1N(1−ai)),ifS0​∏i=1N(1−ai)<K.\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i}))\geq K,\\ S\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right),&\mbox{if}\quad S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})<K.\end{array}\right. |  | (257) |

Due to the inequality ([228](#S7.E228 "In Theorem 12. ‣ 7 Derivatives assessment.")) of Theorem [12](#Thmte12 "Theorem 12. ‣ 7 Derivatives assessment."),

|  |  |  |  |
| --- | --- | --- | --- |
|  | IN0≥f​(S0​∏i=1N(1−ai))+S0​(1−∏i=1N(1−ai))superscriptsubscript𝐼𝑁0𝑓subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖subscript𝑆01superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖\displaystyle I\_{N}^{0}\geq f\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right)+S\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right) |  | (258) |

and the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | IN0≥(S0−K)+,superscriptsubscript𝐼𝑁0superscriptsubscript𝑆0𝐾\displaystyle I\_{N}^{0}\geq(S\_{0}-K)^{+}, |  | (259) |

which follows from the Jensen inequality, we have

|  |  |  |
| --- | --- | --- |
|  | IN0≥max{S0−K)+,f(S0∏i=1N(1−ai))+S0(1−∏i=1N(1−ai))}=I\_{N}^{0}\geq\max\left\{S\_{0}-K)^{+},f\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right)+S\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right)\right\}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS0∏i=1N(1−ai))≥K,S0​(1−∏i=1N(1−ai)),ifS0​∏i=1N(1−ai)<K.\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i}))\geq K,\\ S\_{0}\left(1-\prod\limits\_{i=1}^{N}(1-a\_{i})\right),&\mbox{if}\quad S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})<K.\end{array}\right. |  | (262) |

This proves Theorem [14](#Thmte14 "Theorem 14. ‣ 7 Derivatives assessment.").
∎

###### Theorem 15.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")). Suppose that 0≤ai≤1,0subscript𝑎𝑖10\leq a\_{i}\leq 1, σi​(ω1,…,ωi−1)>σi>0,subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,
i=1,N¯.𝑖¯

1𝑁\ i=\overline{1,N}.
For the payoff function f1​(x)=(K−x)+,x∈(0,∞),K>0,formulae-sequencesubscript𝑓1𝑥superscript𝐾𝑥formulae-sequence𝑥0𝐾0f\_{1}(x)=(K-x)^{+},\ x\in(0,\infty),\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f1​(SN)=f1​(S0​∏i=1N(1−ai)).subscriptsupremum𝑄𝑀superscript𝐸𝑄subscript𝑓1subscript𝑆𝑁subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖\displaystyle\sup\limits\_{Q\in M}E^{Q}f\_{1}(S\_{N})=f\_{1}\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right). |  | (263) |

The set of non arbitrage prices coincides with the interval
  
[(K−S0)+,f1​(S0​∏i=1N(1−ai))].superscript𝐾subscript𝑆0subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖\left[(K-S\_{0})^{+},f\_{1}\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right)\right].

###### Proof.

The inequality

|  |  |  |
| --- | --- | --- |
|  | IN1=∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×I\_{N}^{1}=\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≤f1​(S0​∏i=1N(1−ai))subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖\displaystyle f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\leq f\_{1}\left(S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})\right) |  | (264) |

is true.
Taking into account the inequality ([237](#S7.E237 "In Theorem 13. ‣ 7 Derivatives assessment.")) of Theorem [13](#Thmte13 "Theorem 13. ‣ 7 Derivatives assessment."), we prove Theorem [15](#Thmte15 "Theorem 15. ‣ 7 Derivatives assessment.").
∎

###### Theorem 16.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")). Suppose that 0≤ai≤1,0subscript𝑎𝑖10\leq a\_{i}\leq 1, σi​(ω1,…,ωi−1)>σi>0,subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,
i=1,N¯.𝑖¯

1𝑁\ i=\overline{1,N}.
For the payoff function f1​(S0,S1,…,SN)=(K−∑i=0NSiN+1)+,K>0,formulae-sequencesubscript𝑓1subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscript𝐾superscriptsubscript𝑖0𝑁subscript𝑆𝑖𝑁1𝐾0f\_{1}(S\_{0},S\_{1},\ldots,S\_{N})=\left(K-\frac{\sum\limits\_{i=0}^{N}S\_{i}}{N+1}\right)^{+},\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f1​(S0,S1,…,SN)=(K−S0​∑i=0N∏s=1i(1−as)N+1)+.subscriptsupremum𝑄𝑀superscript𝐸𝑄subscript𝑓1subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscript𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1\displaystyle\sup\limits\_{Q\in M}E^{Q}f\_{1}(S\_{0},S\_{1},\ldots,S\_{N})=\left(K-\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right)^{+}. |  | (265) |

The set of non arbitrage prices coincides with the interval
  
[(K−S0)+,(K−S0​∑i=0N∏s=1i(1−as)N+1)+],superscript𝐾subscript𝑆0superscript𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1\left[(K-S\_{0})^{+},\left(K-\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right)^{+}\right], if K>S0​∑i=0N∏s=1i(1−as)N+1.𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1K>\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}.
  
For K≤S0​∑i=0N∏s=1i(1−as)N+1𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1K\leq\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1} the set of non arbitrage prices coincides with the point 0.00.

###### Proof.

Let us denote

|  |  |  |
| --- | --- | --- |
|  | Sn​(ω11,…,ωn1)=S0​∏s=1n(1+as​(eσs​(ω11,…,ωs−11)​εs​(ωs1)−1)),n=1,N¯,formulae-sequencesubscript𝑆𝑛superscriptsubscript𝜔11…superscriptsubscript𝜔𝑛1subscript𝑆0superscriptsubscriptproduct𝑠1𝑛1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔11…superscriptsubscript𝜔𝑠11subscript𝜀𝑠superscriptsubscript𝜔𝑠11𝑛¯  1𝑁S\_{n}(\omega\_{1}^{1},\ldots,\omega\_{n}^{1})=S\_{0}\prod\limits\_{s=1}^{n}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{1},\ldots,\omega\_{s-1}^{1})\varepsilon\_{s}(\omega\_{s}^{1})}-1\right)\right),\quad n=\overline{1,N}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | tN​(ω11,…,ωN1)=∏s=1Neσs​(ω11,…,ωs−11)​εs​(ωs2)−1eσs​(ω11,…,ωs−11)​εs​(ωs2)−eσs​(ω11,…,ωs−11)​εs​(ωs1).subscript𝑡𝑁superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1superscriptsubscriptproduct𝑠1𝑁superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔11…superscriptsubscript𝜔𝑠11subscript𝜀𝑠superscriptsubscript𝜔𝑠21superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔11…superscriptsubscript𝜔𝑠11subscript𝜀𝑠superscriptsubscript𝜔𝑠2superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔11…superscriptsubscript𝜔𝑠11subscript𝜀𝑠superscriptsubscript𝜔𝑠1\displaystyle t\_{N}(\omega\_{1}^{1},\ldots,\omega\_{N}^{1})=\prod\limits\_{s=1}^{N}\frac{e^{\sigma\_{s}(\omega\_{1}^{1},\ldots,\omega\_{s-1}^{1})\varepsilon\_{s}(\omega\_{s}^{2})}-1}{e^{\sigma\_{s}(\omega\_{1}^{1},\ldots,\omega\_{s-1}^{1})\varepsilon\_{s}(\omega\_{s}^{2})}-e^{\sigma\_{s}(\omega\_{1}^{1},\ldots,\omega\_{s-1}^{1})\varepsilon\_{s}(\omega\_{s}^{1})}}. |  | (266) |

It is evident that

|  |  |  |
| --- | --- | --- |
|  | IN2=supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×I\_{N}^{2}=\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))≥subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absent\displaystyle f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)\geq |  | (267) |

|  |  |  |
| --- | --- | --- |
|  | limεs​(ωs1)=−∞,εs​(ωs2)→∞,s=1,N¯f1(S0,S1(ω11),…,SN(ω11,…,ωN1))×\lim\limits\_{\varepsilon\_{s}(\omega\_{s}^{1})=-\infty,\ \varepsilon\_{s}(\omega\_{s}^{2})\to\infty,s=\overline{1,N}}f\_{1}\left(S\_{0},S\_{1}(\omega\_{1}^{1}),\ldots,S\_{N}(\omega\_{1}^{1},\ldots,\omega\_{N}^{1})\right)\times\\ |  |

|  |  |  |
| --- | --- | --- |
|  | tN​(ω11,…,ωN1)=f1​(S0,S0​(1−a1),…,S0​∏s=1N(1−as))=subscript𝑡𝑁superscriptsubscript𝜔11…superscriptsubscript𝜔𝑁1subscript𝑓1subscript𝑆0subscript𝑆01subscript𝑎1…subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠absentt\_{N}(\omega\_{1}^{1},\ldots,\omega\_{N}^{1})=f\_{1}\left(S\_{0},S\_{0}(1-a\_{1}),\ldots,S\_{0}\prod\limits\_{s=1}^{N}(1-a\_{s})\right)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (K−S0​∑i=0N∏s=1i(1−as)N+1)+.superscript𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1\displaystyle\left(K-\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right)^{+}. |  | (268) |

Let us prove the inverse inequality. We have

|  |  |  |
| --- | --- | --- |
|  | IN2≤supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×I\_{N}^{2}\leq\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |
| --- | --- | --- |
|  | f1​(S0,S0​(1−a1),…,S0​∏s=1N(1−as))=subscript𝑓1subscript𝑆0subscript𝑆01subscript𝑎1…subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠absentf\_{1}\left(S\_{0},S\_{0}(1-a\_{1}),\ldots,S\_{0}\prod\limits\_{s=1}^{N}(1-a\_{s})\right)= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(S0,S0​(1−a1),…,S0​∏s=1N(1−as))=(K−S0​∑i=0N∏s=1N(1−as)N+1)+.subscript𝑓1subscript𝑆0subscript𝑆01subscript𝑎1…subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠𝑁1\displaystyle f\_{1}\left(S\_{0},S\_{0}(1-a\_{1}),\ldots,S\_{0}\prod\limits\_{s=1}^{N}(1-a\_{s})\right)=\left(K-\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{N}(1-a\_{s})}{N+1}\right)^{+}. |  | (269) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | IN2≤(K−S0​∑i=0N∏s=1i(1−as)N+1)+.superscriptsubscript𝐼𝑁2superscript𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1\displaystyle I\_{N}^{2}\leq\left(K-\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right)^{+}. |  | (270) |

The inequalities ([268](#S7.E268 "In Proof. ‣ 7 Derivatives assessment.")), ([270](#S7.E270 "In Proof. ‣ 7 Derivatives assessment.")) prove Theorem [16](#Thmte16 "Theorem 16. ‣ 7 Derivatives assessment.").
∎

###### Theorem 17.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")). Suppose that 0≤ai≤1,0subscript𝑎𝑖10\leq a\_{i}\leq 1, σi​(ω1,…,ωi−1)>σi>0,subscript𝜎𝑖subscript𝜔1…subscript𝜔𝑖1subscript𝜎𝑖0\sigma\_{i}(\omega\_{1},\ldots,\omega\_{i-1})>\sigma\_{i}>0,
i=1,N¯.𝑖¯

1𝑁\ i=\overline{1,N}.
For the payoff function f​(S0,S1,…,SN)=(∑i=0NSiN+1−K)+,K>0,formulae-sequence𝑓subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscriptsuperscriptsubscript𝑖0𝑁subscript𝑆𝑖𝑁1𝐾𝐾0f(S\_{0},S\_{1},\ldots,S\_{N})=\left(\frac{\sum\limits\_{i=0}^{N}S\_{i}}{N+1}-K\right)^{+},\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |
| --- | --- | --- |
|  | supQ∈MEQ​f​(S0,S1,…,SN)=subscriptsupremum𝑄𝑀superscript𝐸𝑄𝑓subscript𝑆0subscript𝑆1…subscript𝑆𝑁absent\sup\limits\_{Q\in M}E^{Q}f(S\_{0},S\_{1},\ldots,S\_{N})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS0​∑i=0N∏s=1i(1−ai)N+1≥K,S0​(1−∑i=0N∏s=1i(1−as)N+1),ifS0​∑i=0N∏s=1i(1−as)N+1<K.casessuperscriptsubscript𝑆0𝐾  ifsubscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑖𝑁1 𝐾subscript𝑆01superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1  ifsubscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1 𝐾\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{i})}{N+1}\geq K,\\ S\_{0}\left(1-\frac{\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right),&\mbox{if}\quad S\_{0}\frac{\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}<K.\end{array}\right. |  | (273) |

If S0​∑i=0N∏s=1i(1−ai)N+1≥K,subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑖𝑁1𝐾\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{i})}{N+1}\geq K, then the set of non arbitrage prices coincides with the point (S0−K)+,superscriptsubscript𝑆0𝐾(S\_{0}-K)^{+}, in case if S0​∑i=0N∏s=1i(1−as)N+1<Ksubscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1𝐾S\_{0}\frac{\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}<K the set of non arbitrage prices coincides with the interval [(S0−K)+,S0​(1−∑i=0N∏s=1i(1−as)N+1)].superscriptsubscript𝑆0𝐾subscript𝑆01superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1\left[(S\_{0}-K)^{+},S\_{0}\left(1-\frac{\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right)\right].

###### Proof.

We have

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))=𝑓subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1absent\displaystyle f\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)= |  | (274) |

|  |  |  |
| --- | --- | --- |
|  | supωi1∈Ωi0−,ωi2∈Ωi0+,i=1,N¯∑i1=1,…,iN=12∏j=1Nψj(ω1i1,…,ωjij)×\sup\limits\_{\omega\_{i}^{1}\in\Omega\_{i}^{0-},\omega\_{i}^{2}\in\Omega\_{i}^{0+},i=\overline{1,N}}\sum\limits\_{i\_{1}=1,\ldots,i\_{N}=1}^{2}\prod\limits\_{j=1}^{N}\psi\_{j}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{j}^{i\_{j}})\times |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(S0​∏s=1N(1+as​(eσs​(ω1i1,…,ωs−1is−1)​εs​(ωsis)−1)))+S0−K=subscript𝑓1subscript𝑆0superscriptsubscriptproduct𝑠1𝑁1subscript𝑎𝑠superscript𝑒subscript𝜎𝑠superscriptsubscript𝜔1subscript𝑖1…superscriptsubscript𝜔𝑠1subscript𝑖𝑠1subscript𝜀𝑠superscriptsubscript𝜔𝑠subscript𝑖𝑠1subscript𝑆0𝐾absent\displaystyle f\_{1}\left(S\_{0}\prod\limits\_{s=1}^{N}\left(1+a\_{s}\left(e^{\sigma\_{s}(\omega\_{1}^{i\_{1}},\ldots,\omega\_{s-1}^{i\_{s-1}})\varepsilon\_{s}(\omega\_{s}^{i\_{s}})}-1\right)\right)\right)+S\_{0}-K= |  | (275) |

|  |  |  |
| --- | --- | --- |
|  | (S0−K)+(K−S0​∑i=0N∏s=1i(1−as)N+1)+=subscript𝑆0𝐾superscript𝐾subscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1absent(S\_{0}-K)+\left(K-\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right)^{+}= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS0​∑i=0N∏s=1i(1−ai)N+1≥K,S0​(1−∑i=0N∏s=1i(1−as)N+1),ifS0​∑i=0N∏s=1i(1−as)N+1<K.casessuperscriptsubscript𝑆0𝐾  ifsubscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑖𝑁1 𝐾subscript𝑆01superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1  ifsubscript𝑆0superscriptsubscript𝑖0𝑁superscriptsubscriptproduct𝑠1𝑖1subscript𝑎𝑠𝑁1 𝐾\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad\frac{S\_{0}\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{i})}{N+1}\geq K,\\ S\_{0}\left(1-\frac{\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}\right),&\mbox{if}\quad S\_{0}\frac{\sum\limits\_{i=0}^{N}\prod\limits\_{s=1}^{i}(1-a\_{s})}{N+1}<K.\end{array}\right. |  | (278) |

In the formula ([275](#S7.E275 "In Proof. ‣ 7 Derivatives assessment.")) we introduced the denotation

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(S0,S1,…,SN)=(K−∑i=0NSiN+1)+.subscript𝑓1subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscript𝐾superscriptsubscript𝑖0𝑁subscript𝑆𝑖𝑁1\displaystyle f\_{1}(S\_{0},S\_{1},\ldots,S\_{N})=\left(K-\frac{\sum\limits\_{i=0}^{N}S\_{i}}{N+1}\right)^{+}. |  | (279) |

The proof of Theorem [17](#Thmte17 "Theorem 17. ‣ 7 Derivatives assessment.") follows from the equality ([275](#S7.E275 "In Proof. ‣ 7 Derivatives assessment.")).
∎

## 8 Estimation of parameters.

Suppose that {gi​(XN)}i=1Nsuperscriptsubscriptsubscript𝑔𝑖subscript𝑋𝑁𝑖1𝑁\{g\_{i}(X\_{N})\}\_{i=1}^{N} is a mapping from the set [0,1]Nsuperscript01𝑁[0,1]^{N} into itself, where XN={x1,…,xN}, 0≤xi≤1,i=1,N¯.formulae-sequenceformulae-sequencesubscript𝑋𝑁subscript𝑥1…subscript𝑥𝑁 0subscript𝑥𝑖1𝑖¯

1𝑁X\_{N}=\{x\_{1},\ldots,x\_{N}\},\ 0\leq\ x\_{i}\leq 1,\ i=\overline{1,N}. If S0,S1,…,SN

subscript𝑆0subscript𝑆1…subscript𝑆𝑁S\_{0},S\_{1},\ldots,S\_{N} is a sample of the process ([179](#S7.E179 "In 7 Derivatives assessment.")), let us denote the order statistic S(0),S(1),…,S(N)

subscript𝑆0subscript𝑆1…subscript𝑆𝑁S\_{(0)},S\_{(1)},\ldots,S\_{(N)} of this sample. Introduce also the denotation gi​([S]N)=gi​(S(0)S(N),…,S(N−1)S(N)),i=1,N¯.formulae-sequencesubscript𝑔𝑖subscriptdelimited-[]𝑆𝑁subscript𝑔𝑖subscript𝑆0subscript𝑆𝑁…subscript𝑆𝑁1subscript𝑆𝑁𝑖¯

1𝑁g\_{i}\left([S]\_{N}\right)=g\_{i}\left(\frac{S\_{(0)}}{S\_{(N)}},\ldots,\frac{S\_{(N-1)}}{S\_{(N)}}\right),\ i=\overline{1,N}.

###### Theorem 18.

Suppose that S0,S1,…,SN

subscript𝑆0subscript𝑆1…subscript𝑆𝑁S\_{0},S\_{1},\ldots,S\_{N} is
a sample of the random process ([179](#S7.E179 "In 7 Derivatives assessment.")). Then, for the parameters
a1,…,aN

subscript𝑎1…subscript𝑎𝑁a\_{1},\ldots,a\_{N} the estimation

|  |  |  |
| --- | --- | --- |
|  | a1=1−τ0​S(0)S0​g1​([S]N),0<τ0≤1,formulae-sequencesubscript𝑎11subscript𝜏0subscript𝑆0subscript𝑆0subscript𝑔1subscriptdelimited-[]𝑆𝑁0subscript𝜏01a\_{1}=1-\tau\_{0}\frac{S\_{(0)}}{S\_{0}}g\_{1}\left([S]\_{N}\right),\quad 0<\tau\_{0}\leq 1, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ai=1−gi​([S]N)gi−1​([S]N),i=2,N¯,formulae-sequencesubscript𝑎𝑖1subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁subscript𝑔𝑖1subscriptdelimited-[]𝑆𝑁𝑖¯  2𝑁\displaystyle a\_{i}=1-\frac{g\_{i}\left([S]\_{N}\right)}{g\_{i-1}\left([S]\_{N}\right)},\quad i=\overline{2,N}, |  | (280) |

is valid, if for gN​([S]N)>0,[S]N∈[0,1]N,formulae-sequencesubscript𝑔𝑁subscriptdelimited-[]𝑆𝑁0subscriptdelimited-[]𝑆𝑁superscript01𝑁\ g\_{N}([S]\_{N})>0,\ [S]\_{N}\in[0,1]^{N}, the inequalities g1​([S]N)≥g2​([S]N)≥…≥gN​([S]N)subscript𝑔1subscriptdelimited-[]𝑆𝑁subscript𝑔2subscriptdelimited-[]𝑆𝑁…subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁g\_{1}([S]\_{N})\geq g\_{2}([S]\_{N})\geq\ldots\geq g\_{N}([S]\_{N}) are true.
If τ0=0,subscript𝜏00\tau\_{0}=0, then ai=1,i=1,N¯.formulae-sequencesubscript𝑎𝑖1𝑖¯

1𝑁a\_{i}=1,\ i=\overline{1,N}.

###### Proof.

The estimation of the parameters a1,…,aN

subscript𝑎1…subscript𝑎𝑁a\_{1},\ldots,a\_{N} we do using the representation of random process Sn,n=1,N¯.

subscript𝑆𝑛𝑛
¯

1𝑁S\_{n},\ n=\overline{1,N}.
The smallest value of the random variable Snsubscript𝑆𝑛S\_{n} is equal S0​∏i=1n(1−ai),n=1,N¯.

subscript𝑆0superscriptsubscriptproduct𝑖1𝑛1subscript𝑎𝑖𝑛
¯

1𝑁S\_{0}\prod\limits\_{i=1}^{n}(1-a\_{i}),\ n=\overline{1,N}.
Let us determine the parameters aisubscript𝑎𝑖a\_{i} from the relations

|  |  |  |
| --- | --- | --- |
|  | S0​∏i=1N(1−ai)=τ​gN​([S]N),…,S0​∏i=1N−k(1−ai)=τ​gN−k​([S]N),…,formulae-sequencesubscript𝑆0superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖  𝜏subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁…subscript𝑆0superscriptsubscriptproduct𝑖1𝑁𝑘1subscript𝑎𝑖  𝜏subscript𝑔𝑁𝑘subscriptdelimited-[]𝑆𝑁…S\_{0}\prod\limits\_{i=1}^{N}(1-a\_{i})=\tau g\_{N}\left([S]\_{N}\right),\ldots,S\_{0}\prod\limits\_{i=1}^{N-k}(1-a\_{i})=\tau g\_{N-k}\left([S]\_{N}\right),\ldots, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | S0​∏i=1N−k−1(1−ai)=τ​gN−k−1​([S]N),…,S0​(1−a1)=τ​g1​([S]N),formulae-sequencesubscript𝑆0superscriptsubscriptproduct𝑖1𝑁𝑘11subscript𝑎𝑖  𝜏subscript𝑔𝑁𝑘1subscriptdelimited-[]𝑆𝑁…subscript𝑆01subscript𝑎1𝜏subscript𝑔1subscriptdelimited-[]𝑆𝑁\displaystyle S\_{0}\prod\limits\_{i=1}^{N-k-1}(1-a\_{i})=\tau g\_{N-k-1}\left([S]\_{N}\right),\ldots,S\_{0}(1-a\_{1})=\tau g\_{1}\left([S]\_{N}\right), |  | (281) |

where τ>0.𝜏0\tau>0. Taking into account the relations ([281](#S8.E281 "In Proof. ‣ 8 Estimation of parameters.")), we obtain

|  |  |  |
| --- | --- | --- |
|  | S0​(1−a1)=τ​g1​([S]N),subscript𝑆01subscript𝑎1𝜏subscript𝑔1subscriptdelimited-[]𝑆𝑁S\_{0}(1-a\_{1})=\tau g\_{1}\left([S]\_{N}\right), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ​gN−k−1​([S]N)​(1−aN−k)=τ​gN−k​([S]N),k=2,N¯.formulae-sequence𝜏subscript𝑔𝑁𝑘1subscriptdelimited-[]𝑆𝑁1subscript𝑎𝑁𝑘𝜏subscript𝑔𝑁𝑘subscriptdelimited-[]𝑆𝑁𝑘¯  2𝑁\displaystyle\tau g\_{N-k-1}\left([S]\_{N}\right)(1-a\_{N-k})=\tau g\_{N-k}\left([S]\_{N}\right),\quad k=\overline{2,N}. |  | (282) |

Solving the relations ([282](#S8.E282 "In Proof. ‣ 8 Estimation of parameters.")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | a1=1−τS0​g1​([S]N),aN−k=1−gN−k​([S]N)gN−k−1​([S]N),k=2,N¯.formulae-sequencesubscript𝑎11𝜏subscript𝑆0subscript𝑔1subscriptdelimited-[]𝑆𝑁formulae-sequencesubscript𝑎𝑁𝑘1subscript𝑔𝑁𝑘subscriptdelimited-[]𝑆𝑁subscript𝑔𝑁𝑘1subscriptdelimited-[]𝑆𝑁𝑘¯  2𝑁\displaystyle a\_{1}=1-\frac{\tau}{S\_{0}}g\_{1}\left([S]\_{N}\right),\quad a\_{N-k}=1-\frac{g\_{N-k}\left([S]\_{N}\right)}{g\_{N-k-1}\left([S]\_{N}\right)},\quad k=\overline{2,N}. |  | (283) |

It is evident that aN−k≥0,k=2,N¯.formulae-sequencesubscript𝑎𝑁𝑘0𝑘¯

2𝑁a\_{N-k}\geq 0,\ k=\overline{2,N}. To provide the positiveness
of a1subscript𝑎1a\_{1} and the inequalities τ​gN−n​([S]N)≤SN−n,n=0,N−1¯,S0≥S(0),formulae-sequence𝜏subscript𝑔𝑁𝑛subscriptdelimited-[]𝑆𝑁subscript𝑆𝑁𝑛formulae-sequence𝑛¯

0𝑁1subscript𝑆0subscript𝑆0\tau g\_{N-n}\left([S]\_{N}\right)\leq S\_{N-n},\ n=\overline{0,N-1},\ S\_{0}\geq S\_{(0)}, meaning that the random process ([179](#S7.E179 "In 7 Derivatives assessment.")) takes all the values from the sample Sn,n=0,N¯,

subscript𝑆𝑛𝑛
¯

0𝑁S\_{n},\ n=\overline{0,N}, we must to put τ=τ0​S(0), 0<τ0≤1.formulae-sequence𝜏subscript𝜏0subscript𝑆0 0subscript𝜏01\tau=\tau\_{0}S\_{(0)},\ 0<\tau\_{0}\leq 1. It is evident that, if τ0=0,subscript𝜏00\tau\_{0}=0, then ai=1,i=1,N¯formulae-sequencesubscript𝑎𝑖1𝑖¯

1𝑁a\_{i}=1,\ i=\overline{1,N} Theorem [18](#Thmte18 "Theorem 18. ‣ 8 Estimation of parameters.") is proved.
∎

###### Remark 1.

It is evident that

|  |  |  |
| --- | --- | --- |
|  | ai=1,i=N−k,N¯, 1<k≤N−1,ai=1−gi​([S]N)gi−1​([S]N),i=2,N−k−1¯,formulae-sequenceformulae-sequencesubscript𝑎𝑖1formulae-sequence𝑖¯  𝑁𝑘𝑁1𝑘𝑁1formulae-sequencesubscript𝑎𝑖1subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁subscript𝑔𝑖1subscriptdelimited-[]𝑆𝑁𝑖¯  2𝑁𝑘1a\_{i}=1,\quad i=\overline{N-k,N},\ 1<k\leq N-1,\ a\_{i}=1-\frac{g\_{i}([S]\_{N})}{g\_{i-1}([S]\_{N})},\ i=\overline{2,N-k-1}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | a1=1−τ0​S(0)S0​g1​([S]N),0<τ0≤1,formulae-sequencesubscript𝑎11subscript𝜏0subscript𝑆0subscript𝑆0subscript𝑔1subscriptdelimited-[]𝑆𝑁0subscript𝜏01\displaystyle a\_{1}=1-\frac{\tau\_{0}S\_{(0)}}{S\_{0}}g\_{1}([S]\_{N}),\quad 0<\tau\_{0}\leq 1, |  | (284) |

is also estimation of the parameters a1,…,aN

subscript𝑎1…subscript𝑎𝑁a\_{1},\ldots,a\_{N} if

|  |  |  |
| --- | --- | --- |
|  | 0<gN−k−1​([S]N)≤gN−k−2​([S]N)​…≤g1​([S]N),[S]N∈[0,1]N.formulae-sequence0subscript𝑔𝑁𝑘1subscriptdelimited-[]𝑆𝑁subscript𝑔𝑁𝑘2subscriptdelimited-[]𝑆𝑁…subscript𝑔1subscriptdelimited-[]𝑆𝑁subscriptdelimited-[]𝑆𝑁superscript01𝑁0<g\_{N-k-1}([S]\_{N})\leq g\_{N-k-2}([S]\_{N})\ldots\leq g\_{1}([S]\_{N}),\ [S]\_{N}\in[0,1]^{N}. |  |

Such estimation is not interesting since

|  |  |  |
| --- | --- | --- |
|  | ∏i=1N−i(1−ai)=0,i=0,k¯.formulae-sequencesuperscriptsubscriptproduct𝑖1𝑁𝑖1subscript𝑎𝑖0𝑖¯  0𝑘\prod\limits\_{i=1}^{N-i}(1-a\_{i})=0,\quad i=\overline{0,k}. |  |

###### Remark 2.

If

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)={S0S(0)​x,if0≤x≤S(0)S0,1,ifS(0)S0<x≤1,𝑔𝑥casessubscript𝑆0subscript𝑆0𝑥  if0 𝑥subscript𝑆0subscript𝑆01  ifsubscript𝑆0subscript𝑆0 𝑥1\displaystyle g(x)=\left\{\begin{array}[]{l l}\frac{S\_{0}}{S\_{(0)}}x,&\mbox{if}\quad 0\leq x\leq\frac{S\_{(0)}}{S\_{0}},\\ 1,&\mbox{if}\quad\frac{S\_{(0)}}{S\_{0}}<x\leq 1,\end{array}\right. |  | (287) |

|  |  |  |
| --- | --- | --- |
|  | gi​([S]N)=g​(S(N−i)S(N)),i=1,N¯,τ0=1,formulae-sequencesubscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑔subscript𝑆𝑁𝑖subscript𝑆𝑁formulae-sequence𝑖¯  1𝑁subscript𝜏01g\_{i}([S]\_{N})=g\left(\frac{S\_{(N-i)}}{S\_{(N)}}\right),\quad i=\overline{1,N},\ \tau\_{0}=1, |  |

then for the parameters
a1,…,aN

subscript𝑎1…subscript𝑎𝑁a\_{1},\ldots,a\_{N} the estimation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ai={1−S(N−i)S(N−i+1),ifS(N−i+1)S(N)≤S(0)S0,1−S(N−i)S(N)​S0S(0),ifS(N−i+1)S(N)>S(0)S0,S(N−i)S(N)≤S(0)S0,0,ifS(N−i)S(N)>S(0)S0.i=2,N¯,formulae-sequencesubscript𝑎𝑖cases1subscript𝑆𝑁𝑖subscript𝑆𝑁𝑖1  ifsubscript𝑆𝑁𝑖1subscript𝑆𝑁 subscript𝑆0subscript𝑆01subscript𝑆𝑁𝑖subscript𝑆𝑁subscript𝑆0subscript𝑆0formulae-sequence  ifsubscript𝑆𝑁𝑖1subscript𝑆𝑁 subscript𝑆0subscript𝑆0subscript𝑆𝑁𝑖subscript𝑆𝑁subscript𝑆0subscript𝑆00  ifsubscript𝑆𝑁𝑖subscript𝑆𝑁 subscript𝑆0subscript𝑆0𝑖¯  2𝑁\displaystyle a\_{i}=\left\{\begin{array}[]{l l}1-\frac{S\_{(N-i)}}{S\_{(N-i+1)}},&\mbox{if}\quad\frac{S\_{(N-i+1)}}{S\_{(N)}}\leq\frac{S\_{(0)}}{S\_{0}},\\ 1-\frac{S\_{(N-i)}}{S\_{(N)}}\frac{S\_{0}}{S\_{(0)}},&\mbox{if}\quad\frac{S\_{(N-i+1)}}{S\_{(N)}}>\frac{S\_{(0)}}{S\_{0}},\ \frac{S\_{(N-i)}}{S\_{(N)}}\leq\frac{S\_{(0)}}{S\_{0}},\\ 0,&\mbox{if}\quad\frac{S\_{(N-i)}}{S\_{(N)}}>\frac{S\_{(0)}}{S\_{0}}.\end{array}\right.\quad i=\overline{2,N}, |  | (291) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | a1={1−S(N−1)S(N),ifS(N−1)S(N)≤S(0)S0,1−S(0)S0,ifS(N−1)S(N)>S(0)S0subscript𝑎1cases1subscript𝑆𝑁1subscript𝑆𝑁  ifsubscript𝑆𝑁1subscript𝑆𝑁 subscript𝑆0subscript𝑆01subscript𝑆0subscript𝑆0  ifsubscript𝑆𝑁1subscript𝑆𝑁 subscript𝑆0subscript𝑆0\displaystyle a\_{1}=\left\{\begin{array}[]{l l}1-\frac{S\_{(N-1)}}{S\_{(N)}},&\mbox{if}\quad\frac{S\_{(N-1)}}{S\_{(N)}}\leq\frac{S\_{(0)}}{S\_{0}},\\ 1-\frac{S\_{(0)}}{S\_{0}},&\mbox{if}\quad\frac{S\_{(N-1)}}{S\_{(N)}}>\frac{S\_{(0)}}{S\_{0}}\end{array}\right. |  | (294) |

is true.
The following equalities

|  |  |  |
| --- | --- | --- |
|  | ∏i=1N(1−ai)=S(0)S0​g​(S(0)S(N))=S(0)S(N),superscriptsubscriptproduct𝑖1𝑁1subscript𝑎𝑖subscript𝑆0subscript𝑆0𝑔subscript𝑆0subscript𝑆𝑁subscript𝑆0subscript𝑆𝑁\prod\limits\_{i=1}^{N}(1-a\_{i})=\frac{S\_{(0)}}{S\_{0}}g\left(\frac{S\_{(0)}}{S\_{(N)}}\right)=\frac{S\_{(0)}}{S\_{(N)}}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∏i=1N−k(1−ai)={S(k)S(N),ifS(k)S(N)≤S(0)S0,S(0)S0,ifS(k)S(N)>S(0)S0,k=1,N−1¯,formulae-sequencesuperscriptsubscriptproduct𝑖1𝑁𝑘1subscript𝑎𝑖casessubscript𝑆𝑘subscript𝑆𝑁  ifsubscript𝑆𝑘subscript𝑆𝑁 subscript𝑆0subscript𝑆0subscript𝑆0subscript𝑆0  ifsubscript𝑆𝑘subscript𝑆𝑁 subscript𝑆0subscript𝑆0𝑘¯  1𝑁1\displaystyle\prod\limits\_{i=1}^{N-k}(1-a\_{i})=\left\{\begin{array}[]{l l}\frac{S\_{(k)}}{S\_{(N)}},&\mbox{if}\quad\frac{S\_{(k)}}{S\_{(N)}}\leq\frac{S\_{(0)}}{S\_{0}},\\ \frac{S\_{(0)}}{S\_{0}},&\mbox{if}\quad\frac{S\_{(k)}}{S\_{(N)}}>\frac{S\_{(0)}}{S\_{0}},\end{array}\right.\quad k=\overline{1,N-1}, |  | (297) |

are valid.

###### Remark 3.

Suppose that g​(x)=x,x∈[0,1].formulae-sequence𝑔𝑥𝑥𝑥01g(x)=x,\ x\in[0,1]. Let us put gN−i​([S]N)=g​(S(i)S(N))=S(i)S(N),i=0,k¯,gN−i​([S]N)=1,i=k+1,N−1¯.formulae-sequencesubscript𝑔𝑁𝑖subscriptdelimited-[]𝑆𝑁𝑔subscript𝑆𝑖subscript𝑆𝑁subscript𝑆𝑖subscript𝑆𝑁formulae-sequence𝑖¯

0𝑘formulae-sequencesubscript𝑔𝑁𝑖subscriptdelimited-[]𝑆𝑁1𝑖¯

𝑘1𝑁1g\_{N-i}([S]\_{N})=g(\frac{S\_{(i)}}{S\_{(N)}})=\frac{S\_{(i)}}{S\_{(N)}},\ i=\overline{0,k},\ g\_{N-i}([S]\_{N})=1,\ i=\overline{k+1,N-1}.
Then,

|  |  |  |
| --- | --- | --- |
|  | a1=1−τ0​S(0)S0,0<τ0≤1,ai=0,i=2,N−k−1¯,formulae-sequenceformulae-sequencesubscript𝑎11subscript𝜏0subscript𝑆0subscript𝑆00subscript𝜏01formulae-sequencesubscript𝑎𝑖0𝑖¯  2𝑁𝑘1a\_{1}=1-\tau\_{0}\frac{S\_{(0)}}{S\_{0}},\quad 0<\tau\_{0}\leq 1,\quad a\_{i}=0,\quad i=\overline{2,N-k-1}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ai=1−gi​([S]N)gi−1​([S]N),i=N−k,N¯,formulae-sequencesubscript𝑎𝑖1subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁subscript𝑔𝑖1subscriptdelimited-[]𝑆𝑁𝑖¯  𝑁𝑘𝑁\displaystyle a\_{i}=1-\frac{g\_{i}([S]\_{N})}{g\_{i-1}([S]\_{N})},\quad i=\overline{N-k,N}, |  | (298) |

is an estimation for the parameters a1,…,aN.

subscript𝑎1…subscript𝑎𝑁a\_{1},\ldots,a\_{N}.

In the next Theorems we put τ0=1.subscript𝜏01\tau\_{0}=1. This corresponds to the fact that fair price of super-hedge is minimal for the considered statistic.

###### Theorem 19.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment.")),
with parameters ai,i=1,N¯,

subscript𝑎𝑖𝑖
¯

1𝑁a\_{i},\ i=\overline{1,N}, given by the formula ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")). For the payoff function f​(x)=(x−K)+,x∈(0,∞),K>0,formulae-sequence𝑓𝑥superscript𝑥𝐾formulae-sequence𝑥0𝐾0f(x)=(x-K)^{+},\ x\in(0,\infty),\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |
| --- | --- | --- |
|  | supQ∈MEQ​f​(SN)=subscriptsupremum𝑄𝑀superscript𝐸𝑄𝑓subscript𝑆𝑁absent\sup\limits\_{Q\in M}E^{Q}f(S\_{N})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS(0)​gN​([S]N)≥K,S0​(1−S(0)​gN​([S]N)S0),ifS(0)​gN​([S]N)<K.casessuperscriptsubscript𝑆0𝐾  ifsubscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁 𝐾subscript𝑆01subscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁subscript𝑆0  ifsubscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁 𝐾\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad S\_{(0)}g\_{N}\left([S]\_{N}\right)\geq K,\\ S\_{0}\left(1-\frac{S\_{(0)}g\_{N}\left([S]\_{N}\right)}{S\_{0}}\right),&\mbox{if}\quad S\_{(0)}g\_{N}\left([S]\_{N}\right)<K.\end{array}\right. |  | (301) |

If S(0)​gN​([S]N)≥K,subscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁𝐾S\_{(0)}g\_{N}\left([S]\_{N}\right)\geq K,
then the set of non arbitrage prices coincides with the point (S0−K)+,superscriptsubscript𝑆0𝐾(S\_{0}-K)^{+}, in case if S(0)​gN​([S]N)<Ksubscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁𝐾S\_{(0)}g\_{N}\left([S]\_{N}\right)<K the set of non arbitrage prices coincides with the closed set [(S0−K)+,S0​(1−S(0)​gN​([S]N)S0)].superscriptsubscript𝑆0𝐾subscript𝑆01subscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁subscript𝑆0\left[(S\_{0}-K)^{+},S\_{0}\left(1-\frac{S\_{(0)}g\_{N}\left([S]\_{N}\right)}{S\_{0}}\right)\right].

The fair price of super-hedge for the statistic ([291](#S8.E291 "In Remark 2. ‣ 8 Estimation of parameters.")), ([294](#S8.E294 "In Remark 2. ‣ 8 Estimation of parameters.")) is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f​(SN)={(S0−K)+,ifS0​S(0)S(N)≥K,S0​(1−S(0)S(N)),ifS0​S(0)S(N)<K.subscriptsupremum𝑄𝑀superscript𝐸𝑄𝑓subscript𝑆𝑁casessuperscriptsubscript𝑆0𝐾  ifsubscript𝑆0subscript𝑆0subscript𝑆𝑁 𝐾subscript𝑆01subscript𝑆0subscript𝑆𝑁  ifsubscript𝑆0subscript𝑆0subscript𝑆𝑁 𝐾\displaystyle\sup\limits\_{Q\in M}E^{Q}f(S\_{N})=\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad S\_{0}\frac{S\_{(0)}}{S\_{(N)}}\geq K,\\ S\_{0}\left(1-\frac{S\_{(0)}}{S\_{(N)}}\right),&\mbox{if}\quad S\_{0}\frac{S\_{(0)}}{S\_{(N)}}<K.\end{array}\right. |  | (304) |

If S0​S(0)S(N)≥K,subscript𝑆0subscript𝑆0subscript𝑆𝑁𝐾S\_{0}\frac{S\_{(0)}}{S\_{(N)}}\geq K,
then the set of non arbitrage prices coincides with the point (S0−K)+,superscriptsubscript𝑆0𝐾(S\_{0}-K)^{+}, in case if S0​S(0)S(N)<Ksubscript𝑆0subscript𝑆0subscript𝑆𝑁𝐾S\_{0}\frac{S\_{(0)}}{S\_{(N)}}<K the set of non arbitrage prices coincides with the closed set [(S0−K)+,S0​(1−S(0)S(N))].superscriptsubscript𝑆0𝐾subscript𝑆01subscript𝑆0subscript𝑆𝑁\left[(S\_{0}-K)^{+},S\_{0}\left(1-\frac{S\_{(0)}}{S\_{(N)}}\right)\right].

The fair price of super-hedge is minimal one for the statistic ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")) with gi​(XN)=gN​(XN)=1,i=1,N−1¯,formulae-sequencesubscript𝑔𝑖subscript𝑋𝑁subscript𝑔𝑁subscript𝑋𝑁1𝑖¯

1𝑁1g\_{i}(X\_{N})=g\_{N}(X\_{N})=1,\ i=\overline{1,N-1}, and is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f​(SN)={(S0−K)+,ifS(0)≥K,S0−S(0),ifS(0)<K.subscriptsupremum𝑄𝑀superscript𝐸𝑄𝑓subscript𝑆𝑁casessuperscriptsubscript𝑆0𝐾  ifsubscript𝑆0 𝐾subscript𝑆0subscript𝑆0  ifsubscript𝑆0 𝐾\displaystyle\sup\limits\_{Q\in M}E^{Q}f(S\_{N})=\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad S\_{(0)}\geq K,\\ S\_{0}-S\_{(0)},&\mbox{if}\quad S\_{(0)}<K.\end{array}\right. |  | (307) |

If S(0)≥K,subscript𝑆0𝐾S\_{(0)}\geq K,
then the set of non arbitrage prices coincides with the point (S0−K)+,superscriptsubscript𝑆0𝐾(S\_{0}-K)^{+}, in case if S(0)<Ksubscript𝑆0𝐾S\_{(0)}<K the set of non arbitrage prices coincides with the closed set [(S0−K)+,S0−S(0)].superscriptsubscript𝑆0𝐾subscript𝑆0subscript𝑆0[(S\_{0}-K)^{+},S\_{0}-S\_{(0)}].

###### Theorem 20.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment."))
with the parameters ai,i=1,N¯,

subscript𝑎𝑖𝑖
¯

1𝑁a\_{i},\ i=\overline{1,N}, given by the formula ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")). For the payoff function f1​(x)=(K−x)+,x∈(0,∞),K>0,formulae-sequencesubscript𝑓1𝑥superscript𝐾𝑥formulae-sequence𝑥0𝐾0f\_{1}(x)=(K-x)^{+},\ x\in(0,\infty),\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f1​(SN)=f1​(S(0)​gN​([S]N)).subscriptsupremum𝑄𝑀superscript𝐸𝑄subscript𝑓1subscript𝑆𝑁subscript𝑓1subscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁\displaystyle\sup\limits\_{Q\in M}E^{Q}f\_{1}(S\_{N})=f\_{1}\left(S\_{(0)}g\_{N}\left([S]\_{N}\right)\right). |  | (308) |

The set of non arbitrage prices coincides with the closed interval
  
[(K−S0)+,f1​(S(0)​gN​([S]N))].superscript𝐾subscript𝑆0subscript𝑓1subscript𝑆0subscript𝑔𝑁subscriptdelimited-[]𝑆𝑁\left[(K-S\_{0})^{+},f\_{1}\left(S\_{(0)}g\_{N}\left([S]\_{N}\right)\right)\right].

The fair price of super-hedge for the statistic ([291](#S8.E291 "In Remark 2. ‣ 8 Estimation of parameters.")), ([294](#S8.E294 "In Remark 2. ‣ 8 Estimation of parameters.")) is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f1​(SN)=f1​(S0​S(0)S(N)).subscriptsupremum𝑄𝑀superscript𝐸𝑄subscript𝑓1subscript𝑆𝑁subscript𝑓1subscript𝑆0subscript𝑆0subscript𝑆𝑁\displaystyle\sup\limits\_{Q\in M}E^{Q}f\_{1}(S\_{N})=f\_{1}\left(S\_{0}\frac{S\_{(0)}}{S\_{(N)}}\right). |  | (309) |

The set of non arbitrage prices coincides with the closed interval [(K−S0)+,f1​(S0​S(0)S(N))].superscript𝐾subscript𝑆0subscript𝑓1subscript𝑆0subscript𝑆0subscript𝑆𝑁\left[(K-S\_{0})^{+},f\_{1}\left(S\_{0}\frac{S\_{(0)}}{S\_{(N)}}\right)\right].

The fair price of super-hedge is minimal one for the statistic ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")) with gi​(XN)=gN​(XN)=1,i=1,N−1¯,formulae-sequencesubscript𝑔𝑖subscript𝑋𝑁subscript𝑔𝑁subscript𝑋𝑁1𝑖¯

1𝑁1g\_{i}(X\_{N})=g\_{N}(X\_{N})=1,\ i=\overline{1,N-1}, and is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f1​(SN)=f1​(S(0)).subscriptsupremum𝑄𝑀superscript𝐸𝑄subscript𝑓1subscript𝑆𝑁subscript𝑓1subscript𝑆0\displaystyle\sup\limits\_{Q\in M}E^{Q}f\_{1}(S\_{N})=f\_{1}\left(S\_{(0)}\right). |  | (310) |

The set of non arbitrage prices coincides with the closed interval [(K−S0)+,f1​(S(0))].superscript𝐾subscript𝑆0subscript𝑓1subscript𝑆0\left[(K-S\_{0})^{+},f\_{1}\left(S\_{(0)}\right)\right].

###### Theorem 21.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment."))
with the parameters ai,i=1,N¯,

subscript𝑎𝑖𝑖
¯

1𝑁a\_{i},\ i=\overline{1,N}, given by the formula ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")). For the payoff function f1​(S0,S1,…,SN)=(K−∑i=0NSiN+1)+,K>0,formulae-sequencesubscript𝑓1subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscript𝐾superscriptsubscript𝑖0𝑁subscript𝑆𝑖𝑁1𝐾0f\_{1}(S\_{0},S\_{1},\ldots,S\_{N})=\left(K-\frac{\sum\limits\_{i=0}^{N}S\_{i}}{N+1}\right)^{+},\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f1​(S0,S1,…,SN)=(K−S0+S(0)​∑i=1Ngi​([S]N)(N+1))+.subscriptsupremum𝑄𝑀superscript𝐸𝑄subscript𝑓1subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscript𝐾subscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1\displaystyle\sup\limits\_{Q\in M}E^{Q}f\_{1}(S\_{0},S\_{1},\ldots,S\_{N})=\left(K-\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}\right)^{+}. |  | (311) |

The set of non arbitrage prices coincides with the closed interval
  
[(K−S0)+,(K−S0+S(0)​∑i=1Ngi​([S]N)(N+1))+],superscript𝐾subscript𝑆0superscript𝐾subscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1\left[(K-S\_{0})^{+},\left(K-\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}\right)^{+}\right], if K>S0+S(0)​∑i=1Ngi​([S]N)(N+1).𝐾subscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1K>\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}.
  
For K≤S0+S(0)​∑i=1Ngi​([S]N)(N+1)𝐾subscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1K\leq\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)} the set of non arbitrage prices coincides with the point 0.00.

The fair price of super-hedge is minimal one for the statistic ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")) with gi​(XN)=gN​(XN)=1,i=1,N−1¯,formulae-sequencesubscript𝑔𝑖subscript𝑋𝑁subscript𝑔𝑁subscript𝑋𝑁1𝑖¯

1𝑁1g\_{i}(X\_{N})=g\_{N}(X\_{N})=1,\ i=\overline{1,N-1}, and is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈MEQ​f1​(S0,S1,…,SN)=(K−S0+S(0)​N(N+1))+.subscriptsupremum𝑄𝑀superscript𝐸𝑄subscript𝑓1subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscript𝐾subscript𝑆0subscript𝑆0𝑁𝑁1\displaystyle\sup\limits\_{Q\in M}E^{Q}f\_{1}(S\_{0},S\_{1},\ldots,S\_{N})=\left(K-\frac{S\_{0}+S\_{(0)}N}{(N+1)}\right)^{+}. |  | (312) |

The set of non arbitrage prices coincides with the closed interval
  
[(K−S0)+,(K−S0+S(0)​N(N+1))+],superscript𝐾subscript𝑆0superscript𝐾subscript𝑆0subscript𝑆0𝑁𝑁1\left[(K-S\_{0})^{+},\left(K-\frac{S\_{0}+S\_{(0)}N}{(N+1)}\right)^{+}\right], if K>S0+S(0)​N(N+1).𝐾subscript𝑆0subscript𝑆0𝑁𝑁1K>\frac{S\_{0}+S\_{(0)}N}{(N+1)}. For K≤S0+S(0)​N(N+1)𝐾subscript𝑆0subscript𝑆0𝑁𝑁1K\leq\frac{S\_{0}+S\_{(0)}N}{(N+1)} the set of non arbitrage prices coincides with the point 0.00.

###### Theorem 22.

On the probability space {ΩN,ℱN,PN},subscriptΩ𝑁subscriptℱ𝑁subscript𝑃𝑁\{\Omega\_{N},{\cal F}\_{N},P\_{N}\}, let the evolution of risky asset be given by the formula ([179](#S7.E179 "In 7 Derivatives assessment."))
with the parameters ai,i=1,N¯,

subscript𝑎𝑖𝑖
¯

1𝑁a\_{i},\ i=\overline{1,N}, given by the formula ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")). For the payoff function f​(S0,S1,…,SN)=(∑i=0NSiN+1−K)+,K>0,formulae-sequence𝑓subscript𝑆0subscript𝑆1…subscript𝑆𝑁superscriptsuperscriptsubscript𝑖0𝑁subscript𝑆𝑖𝑁1𝐾𝐾0f(S\_{0},S\_{1},\ldots,S\_{N})=\left(\frac{\sum\limits\_{i=0}^{N}S\_{i}}{N+1}-K\right)^{+},\ K>0, the fair price of super-hedge is given by the formula

|  |  |  |
| --- | --- | --- |
|  | supQ∈MEQ​f​(S0,S1,…,SN)=subscriptsupremum𝑄𝑀superscript𝐸𝑄𝑓subscript𝑆0subscript𝑆1…subscript𝑆𝑁absent\sup\limits\_{Q\in M}E^{Q}f(S\_{0},S\_{1},\ldots,S\_{N})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS0+S(0)​∑i=1Ngi​([S]N)(N+1)≥K,(S0−S0+S(0)​∑i=1Ngi​([S]N)(N+1)),ifS0+S(0)​∑i=1Ngi​([S]N)(N+1)<K.casessuperscriptsubscript𝑆0𝐾  ifsubscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1 𝐾subscript𝑆0subscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1  ifsubscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1 𝐾\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}\geq K,\\ \left(S\_{0}-\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}\right),&\mbox{if}\quad\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}<K.\end{array}\right. |  | (315) |

If S0+S(0)​∑i=1Ngi​([S]N)(N+1)≥K,subscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1𝐾\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}\geq K, then the set of non arbitrage prices coincides with the point (S0−K)+,superscriptsubscript𝑆0𝐾(S\_{0}-K)^{+}, in case if
S0+S(0)​∑i=1Ngi​([S]N)(N+1)<Ksubscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1𝐾\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}<K the set of non arbitrage prices coincides with the closed interval [(S0−K)+,(S0−S0+S(0)​∑i=1Ngi​([S]N)(N+1))].superscriptsubscript𝑆0𝐾subscript𝑆0subscript𝑆0subscript𝑆0superscriptsubscript𝑖1𝑁subscript𝑔𝑖subscriptdelimited-[]𝑆𝑁𝑁1\left[(S\_{0}-K)^{+},\left(S\_{0}-\frac{S\_{0}+S\_{(0)}\sum\limits\_{i=1}^{N}g\_{i}\left([S]\_{N}\right)}{(N+1)}\right)\right].

The fair price of super-hedge is minimal one for the statistic ([280](#S8.E280 "In Theorem 18. ‣ 8 Estimation of parameters.")) with gi​(XN)=gN​(XN)=1,i=1,N−1¯,formulae-sequencesubscript𝑔𝑖subscript𝑋𝑁subscript𝑔𝑁subscript𝑋𝑁1𝑖¯

1𝑁1g\_{i}(X\_{N})=g\_{N}(X\_{N})=1,\ i=\overline{1,N-1}, and is given by the formula

|  |  |  |
| --- | --- | --- |
|  | supQ∈MEQ​f​(S0,S1,…,SN)=subscriptsupremum𝑄𝑀superscript𝐸𝑄𝑓subscript𝑆0subscript𝑆1…subscript𝑆𝑁absent\sup\limits\_{Q\in M}E^{Q}f(S\_{0},S\_{1},\ldots,S\_{N})= |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(S0−K)+,ifS0+S(0)​N(N+1)≥K,(S0−S0+S(0)​N(N+1)),ifS0+S(0)​N(N+1)<K.casessuperscriptsubscript𝑆0𝐾  ifsubscript𝑆0subscript𝑆0𝑁𝑁1 𝐾subscript𝑆0subscript𝑆0subscript𝑆0𝑁𝑁1  ifsubscript𝑆0subscript𝑆0𝑁𝑁1 𝐾\displaystyle\left\{\begin{array}[]{l l}(S\_{0}-K)^{+},&\mbox{if}\quad\frac{S\_{0}+S\_{(0)}N}{(N+1)}\geq K,\\ \left(S\_{0}-\frac{S\_{0}+S\_{(0)}N}{(N+1)}\right),&\mbox{if}\quad\frac{S\_{0}+S\_{(0)}N}{(N+1)}<K.\end{array}\right. |  | (318) |

If S0+S(0)​N(N+1)≥K,subscript𝑆0subscript𝑆0𝑁𝑁1𝐾\frac{S\_{0}+S\_{(0)}N}{(N+1)}\geq K, then the set of non arbitrage prices coincides with the point (S0−K)+,superscriptsubscript𝑆0𝐾(S\_{0}-K)^{+}, in case if
S0+S(0)​N(N+1)<Ksubscript𝑆0subscript𝑆0𝑁𝑁1𝐾\frac{S\_{0}+S\_{(0)}N}{(N+1)}<K the set of non arbitrage prices coincides with the closed interval [(S0−K)+,(S0−S0+S(0)​N(N+1))].superscriptsubscript𝑆0𝐾subscript𝑆0subscript𝑆0subscript𝑆0𝑁𝑁1\left[(S\_{0}-K)^{+},\left(S\_{0}-\frac{S\_{0}+S\_{(0)}N}{(N+1)}\right)\right].

## 9 Conclusions.

Section 1 provides an overview of the achievements and formulates the main problem that has been solved.
Section 2 contains the formulation of conditions which must satisfy the evolution of risky assets.
In Section 3, conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")) are formulated for the set of nonnegative random variables with the help of which a family of measures is constructed in a recurrent way. In Lemma [1](#Thmleme1 "Lemma 1. ‣ 3 Construction of the set of martingale measures."), conditions were found for the existence of bounded nonnegative random variables satisfying the conditions ([14](#S3.E14 "In 3 Construction of the set of martingale measures.")) - ([16](#S3.E16 "In 3 Construction of the set of martingale measures.")).
In Lemma [2](#Thmleme2 "Lemma 2. ‣ 3 Construction of the set of martingale measures."), it was proved that the family of measures introduced in the recurrent way is equivalent to the original measure.

Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures.") gives sufficient conditions under which the introduced family of measures is the set of martingale measures equivalent to the original measure for the evolution of risky assets considered in Section 1.

In Section 4, relying on the concept of an exhaustive decomposition of a measurable space, in Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values."), we prove an integral inequality for a nonnegative random variable for the constructed family of martingale measures.

In Theorem [2](#Thmte2 "Theorem 2. ‣ 4 Inequalities for the nonnegative random values."), for a special class of evolutions of risky assets for the nonnegative random variable satisfying the integral inequality, obtained in Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values."), a pointwise system of inequalities is obtained.

In Lemma [5](#Thmleme5 "Lemma 5. ‣ 4 Inequalities for the nonnegative random values."), on the basis of Lemma [4](#Thmleme4 "Lemma 4. ‣ 4 Inequalities for the nonnegative random values."), we obtained a pointwise system of inequalities for a nonnegative random variable for the general case of the evolution of risky assets.

Theorem [3](#Thmte3 "Theorem 3. ‣ 4 Inequalities for the nonnegative random values.") contains sufficient conditions under the fulfillment of which the resulting system of inequalities with respect to the nonnegative random variable has a solution whose right-hand side satisfies the condition: the conditional expectation of the right-hand side of the inequality with respect to the filtration is equal to 1.

Theorem [4](#Thmte4 "Theorem 4. ‣ 4 Inequalities for the nonnegative random values.") solves the same problem as in Theorem [5](#Thmte5 "Theorem 5. ‣ 5 Optional decomposition for super-martingales.") for the general case of the evolution of risky assets.

In Section 5, based on the inequalities obtained in Theorems [3](#Thmte3 "Theorem 3. ‣ 4 Inequalities for the nonnegative random values.") and [4](#Thmte4 "Theorem 4. ‣ 4 Inequalities for the nonnegative random values."), we prove a theorem on the optional decomposition of nonnegative super-martingales with respect to the family of equivalent martingale measures.

The description of the family of equivalent martingale measures given in Theorem [1](#Thmte1 "Theorem 1. ‣ 3 Construction of the set of martingale measures.") is rather general, therefore, in Section 6, a spot set of measures is introduced.
In Lemma [6](#Thmleme6 "Lemma 6. ‣ 6 Spot measures and integral representation for martingale measures."), the representation is obtained for the family of spot measures.

Based on the concept of the spot family of measures, the family of α𝛼\alpha-spot
measures based on a set of positive random variables is introduced.
Theorem [6](#Thmte6 "Theorem 6. ‣ 6 Spot measures and integral representation for martingale measures.") provides sufficient conditions for the integral over the set of α𝛼\alpha-spot measures to be an integral over the set of spot measures.

In Theorem [7](#Thmte7 "Theorem 7. ‣ 6 Spot measures and integral representation for martingale measures."), sufficient conditions are given when the family of spot measures is a family of martingale measures and the constructed family of measures, that is an integral over the set of α𝛼\alpha-spot measures, is a family of martingale measures being equivalent to the original measure.

Theorem [8](#Thmte8 "Theorem 8. ‣ 6 Spot measures and integral representation for martingale measures.") describes the class of evolutions of risky assets for which the family of equivalent martingale measures is such that each martingale measure is an integral over the set of spot measures.

Section 7 is devoted to the application of the results obtained in the previous sections. A class of random processes is considered, which contains well-known processes of the type ARCH and GARCH ones. Two types of random processes are considered, those for which the price of an asset cannot go down to zero and those for which the price can go down to zero during the period under consideration. The first class of processes describes the evolution of well-managed assets. We will call these assets relatively stable.

Theorem [9](#Thmte9 "Theorem 9. ‣ 7 Derivatives assessment.") asserts that for the evolution of relatively stable assets in the period under consideration, the family of martingale measures is one and the same.
The family of martingale measures for the evolution of risky assets whose price can drop to zero is contained in the family of martingale measures for the evolution of relatively stable assets. Each of the martingale measures for the considered class of evolutions is an integral over the set of spot martingale measures. On this basis, the fair price of the super hedge is given by the formula ([187](#S7.E187 "In Theorem 9. ‣ 7 Derivatives assessment.")).
In Theorems [10](#Thmte10 "Theorem 10. ‣ 7 Derivatives assessment.") and [11](#Thmte11 "Theorem 11. ‣ 7 Derivatives assessment."), an interval of non-arbitrage prices is found for a wide class of payoff functions in the case when evolution describes relatively unstable assets.
This range is quite wide for the payment functions of standard put and call options. The fair price of the super hedge is in this case the starting price of the underlying asset. In Theorems [12](#Thmte12 "Theorem 12. ‣ 7 Derivatives assessment."), [13](#Thmte13 "Theorem 13. ‣ 7 Derivatives assessment.") estimates are found for the fair price of the super-hedge for the introduced class of evolutions with respect to stable assets.
In Theorems [14](#Thmte14 "Theorem 14. ‣ 7 Derivatives assessment.") and [15](#Thmte15 "Theorem 15. ‣ 7 Derivatives assessment."), formulas are found for the fair price of contracts with call and put options for the evolution of assets described by parametric processes.

In Theorems [16](#Thmte16 "Theorem 16. ‣ 7 Derivatives assessment.") and [17](#Thmte17 "Theorem 17. ‣ 7 Derivatives assessment."), the same formulas are found for Asian-type put and call options. A characteristic feature of these estimates is that for the evolution of relatively stable assets, the fair price of the super hedge is less than the price of the initial price of the asset.

In Section 8, the estimates of the parameters of risky assets included in the evolution are obtained. This result is contained in Theorem [18](#Thmte18 "Theorem 18. ‣ 8 Estimation of parameters.").
In Theorems [19](#Thmte19 "Theorem 19. ‣ 8 Estimation of parameters.") and [20](#Thmte20 "Theorem 20. ‣ 8 Estimation of parameters."), formulas are found for the fair price of contracts with call and put options for the obtained parameter estimates, and the interval of non-arbitrage prices for different statistics is found. The same results are contained in Theorems [21](#Thmte21 "Theorem 21. ‣ 8 Estimation of parameters."), [22](#Thmte22 "Theorem 22. ‣ 8 Estimation of parameters.") for Asian-style call and put options.

## References

* 1.
   Bachelier L.(1900) Theorie de la speculation. Annales de l’Ecole Normal Superieure. V. 17, P. 21-86.
* 2.
   Black F., Scholes M. (1973) The pricing of options and corporate liabilities. Journal of Political Economy, V. 81, N 3, P. 637 - 659.
* 3.
   Merton R. S. (1973) Theory of rational option pricing. Bell Journal of Economics and Management Science. N 4 (Spring), P. 141 - 183.
* 4.
   Harrison J.M., Kreps D.M. (1979) Martingales and Arbitrage in Multiperiod Securities Markets. Journal of Economic Theory, 20, 381–
  408. https://doi.org/ 10.1016/0022-0531(79)90043-?
* 5.
   Harrison J.M., Pliska S.R. (1981) Martingales and Stochastic Integrals in the Theory of Continuous Trading. Stochastic Processes and their Applications. 11, 215–260.
* 6.
   Dalang R.C., Morton A., Willinger W. (1990): Equivalent Martingale measures and no-arbitrage in stochastic securities market model. Stochastics and Stochastic Reports. 29, 185–201. https://doi.org/10.1080/17442509008833613
* 7.
   Delbaen, F., and Schachermayer, W.(2006): The Mathematics and Arbitrage. Berlin: Springer.
* 8.
   Rogers L.C. G. (1995) Equivalent martingale measures and no-arbitrage. Stochastics and Stochastics Reports, V. 51, P. 41 - 50.
* 9.
   Shiryaev A. N. (1998) Foundations of Stochastic Financial Mathematics. V.1 Theory. PHAZIS, Moskow (in Russian).
* 10.
   Shiryaev A. N. (1998) Foundations of Stochastic Financial Mathematics. V.2 Theory. PHAZIS, Moskow (in Russian).
* 11.
   Gonchar, N. S. (2008) Mathematical foundations of information economics. Bogolyubov Institute for Theoretical Physics, Kiev.
* 12.
   Gonchar, N. S. (2015): Mathematical Model of Banking Operation. Cybernetics and System Analysis, 51, 378-399. https://doi.org/ 10.1007/s10559-015-9730-0
* 13.
   Gonchar, N. S., and Terentieva, L.S.(2008)
  Default Risk Valuation of the Firm with the
  Special Process of Internal Yield.
  Journal of Automation and Information Sciences, 40, 57-71. https://doi.org/ 10.1615/ AutomatInfScien.v40.18.60
* 14.
   Gonchar N.S. (2017) Banking and Risk Assessment.
  In: Jerzy, K., Ed., Banking: Services, Opportunity and Risks, Chapter 8, Nova Science Publisher, Inc.,New York.
* 15.
   Gonchar N.S. (2020):
  Assessment of contingent liabilities for risk assets evolutions built on Brownian motion. Advances in Pure Mathematics, 9, 259 - 296. https://doi.org/10.4236/apm.2020.105016
* 16.
   Gonchar N.S. (2019): Description of incomplete financial markets for time evolution of risk assets. Advances in Pure Mathematics, 10, 567 - 610. https://doi.org/10.4236/apm.2019.96029
* 17.
   Gonchar N.S. (2018): Martingales and super-martingales relative to a convex set of equivalent measures. Advances in Pure Mathematics, 8, 428 - 462. https://doi.org/10.4236/apm.2018.84025
* 18.
   Engle R. F. (1982) Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. Econometrica V. 50, N 4, P 987-1008.
* 19.
   Bollerslev T. (1986) Generalized autoregressive conditional heteroskedasticity. Journal of Econometrics, V. 31, P. 307-327.
* 20.
   Engle R. F., Bollerslev T. (1986) Moddeling the persistence of conditional variance. Econometrics Reviews, V. 5, P. 1-50.
* 21.
   El Karoui, N., and Quenez, M.C. (1995):
  Dynamic programming and pricing of contingent claims in an incomplete market.
  SIAM J. Control Optimizat., 33, 27-66.
* 22.
   Kramkov, D. O. (1996) Optional decomposition of super-martingales and hedging in
  incomplete security markets. Probab. Theory Relat. Fields, 105, 459-479. https://doi.org/ 10.1007/BF01191909
* 23.
   Follmer, H., and Kramkov, D.O. (1997):
  Optional decomposition theorem
  under constraints. Probability Theory and Related Fields, 109, 1-25. https://doi.org/ 10.1007/s004400050122
* 24.
   Follmer, H., and Kabanov, Yu. M.(1996): ’Optional decomposition theorems
  in discrete time,’ in Atti del convegno in onore di Oliviero Lessi, Padova , 25-26
  marzo, 47-68.
* 25.
   Follmer, H., and Kabanov, Yu. M. (1998):
  Optional decomposition and Lagrange multipliers. Finance Stochast., 2, 69-81.https://doi.org/ 10.1007/s007800050033
* 26.
   Bouchard, B., and Nutz, M. (2015): Arbitrage and duality in nondominated discrete-time models. The Annals of Applied Probability., 25.2, 823-859.
* 27.
   Eberlein, E., Jacod, J. (1997): On the range of option price. Finance Stoch. 1.
* 28.
   Bellamy, N., Jeanblanc, M. (1999): Incompleteness of markets driven by mixed diffusion. Finance Stoch. 4, 209 - 222.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2010.13630)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2010.13630)
[View original  
on arXiv](https://arxiv.org/abs/2010.13630)[►](javascript: void(0))