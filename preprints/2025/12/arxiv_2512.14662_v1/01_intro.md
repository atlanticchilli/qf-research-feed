---
authors:
- Damir Filipović
doc_id: arxiv:2512.14662v1
family_id: arxiv:2512.14662
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote
  1This paper was written while the author was a guest of the FinsureTech Hub, Department
  of Mathematics, ETH Zurich.
url_abs: http://arxiv.org/abs/2512.14662v1
url_html: https://arxiv.org/html/2512.14662v1
venue: arXiv q-fin
version: 1
year: 2025
---


Damir Filipović222EPFL, Swiss Finance Institute, 1015 Lausanne, Switzerland. Email: damir.filipovic@epfl.ch

(16 December 2025)

###### Abstract

This paper develops a model-free framework for static fixed-income pricing and
the replication of liability cash flows. We show that the absence
of static arbitrage across a universe of fixed-income instruments is equivalent
to the existence of a strictly positive discount curve that
reproduces all observed market prices. We then study the replication and
super-replication of liabilities and establish conditions ensuring the existence
of least-cost super-replicating portfolios, including a rigorous interpretation
of swap–repo replication within this static framework. The results provide a
unified foundation for discount-curve construction and liability-driven
investment, with direct relevance for economic capital assessment and regulatory
practice.

Keywords: Fixed-Income Pricing; Static Arbitrage; Discount Curves; Liability Replication; Swap–Repo Replication

## 1 Introduction

The valuation and replication of insurance liabilities rely fundamentally on the
structure of fixed-income markets. Regulatory frameworks such as Solvency II and
the Swiss Solvency Test require insurers to discount expected liability
cash flows using market-consistent yield curves and to assess hedging strategies
based on portfolios of bonds, swaps, and repo transactions.333For Solvency II see <https://www.eiopa.europa.eu/browse/regulation-and-policy/solvency-ii_en>. For the Swiss Solvency Test see <https://www.finma.ch/en/supervision/insurers/cross-sectoral-tools/swiss-solvency-test-sst>. Despite the
operational importance of these practices, a basic structural question remains:
under what conditions do the observed prices of fixed-income instruments define
an arbitrage-free pricing system that admits a common discount curve and
supports a consistent valuation and replication of expected liability cash
flows?

This paper develops a general and model-free framework for fixed-income pricing
based solely on static arbitrage. We show that the absence of (strict) arbitrage
across a universe of fixed-income instruments is equivalent to the existence of
a strictly positive (nonnegative) discount curve that reproduces all observed
market prices. This result constitutes a fundamental theorem of fixed-income
pricing and provides a theoretical foundation for discount-curve construction
in insurance asset–liability management. To the best of our knowledge, this
paper provides the first systematic treatment of static arbitrage in fixed-income
price systems formulated directly in terms of dated cash flows and observed
market prices, with an explicit focus on liability replication.

We then turn to the replication of expected insurance liability cash flows. Perfect
replication typically fails when liability and asset cash-flow dates and cash flows do not
align. This motivates a super-replication
approach, for which we establish existence of a least-cost replicating portfolio
and outline conditions ensuring well-posedness. A key insight is that
swap–repo strategies naturally produce fixed-income cash-flow profiles,
allowing swaps, repos, and floating-rate notes to be treated within the same
static framework as coupon bonds.

The results presented here are consistent with standard fixed-income valuation
and replication practices and clarify the conditions under which current
regulatory discounting and liability valuation methodologies are well founded,
as well as their structural limitations. They also point toward several avenues
for further research, including uniqueness of super-replication portfolios,
numerical methods for liability hedging, and implications for the construction
of regulatory discount curves.

The theoretical foundations of arbitrage-free pricing are well established in
the discrete-time and static asset pricing literature. Seminal contributions by [har\_kre\_79] and [dal\_mor\_wil\_90] establish the
equivalence between arbitrage-free price systems and the existence of linear
pricing functionals, or state-price vectors; see [coc\_01] and
[foe\_sch\_16] for surveys and further references. These results apply to general financial markets and are not tailored
to fixed-income price systems described directly in terms of dated cash flows.
To the best of our knowledge, a systematic treatment of static arbitrage in
fixed-income markets formulated explicitly at the level of cash-flow matrices
and observed prices, and linked to the replication of expected liability
cash flows, has not appeared in the literature.

The remainder of the paper is organized as follows.
Section [2](https://arxiv.org/html/2512.14662v1#S2 "2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") develops the fundamental theorem of fixed-income pricing
and establishes the equivalence between arbitrage-free prices and the existence
of a discount curve.
Section [3](https://arxiv.org/html/2512.14662v1#S3 "3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") applies this framework to the replication and
super-replication of liabilities and derives conditions under
which least-cost super-replication is feasible.
Section [4](https://arxiv.org/html/2512.14662v1#S4 "4 Illustrative Examples ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") illustrates the theory through canonical fixed-income
instruments, including coupon bonds, swaps, and repo-based strategies.
Section [5](https://arxiv.org/html/2512.14662v1#S5 "5 Conclusion and Outlook ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") concludes with an outlook on open questions and directions
for further research.
All proofs are collected in the Appendix.

## 2 A Fundamental Theorem of Fixed-Income Pricing

We consider a universe of MM fixed-income instruments, indexed by i=1,…,Mi=1,\dots,M,
with prices PiP\_{i} and deterministic cash flows Ci​1,…,Ci​NC\_{i1},\dots,C\_{iN} occurring at
a common set of dates 0<x1<⋯<xN0<x\_{1}<\cdots<x\_{N}.444If instrument ii has no cash flow at xjx\_{j}, we set Ci​j=0C\_{ij}=0.
We collect the prices in the M×1M\times 1 vector PP and the cash flows in the
M×NM\times N cash-flow matrix CC.

We assume a frictionless market in which these instruments can be traded freely.
A portfolio is represented by a vector q∈ℝMq\in\mathbb{R}^{M}, where qiq\_{i} denotes
the position in instrument ii.
Such a portfolio generates the cash-flow vector q⊤​Cq^{\top}C and has price q⊤​Pq^{\top}P.

A central question, which has received surprisingly little attention in the literature, is whether the
observed price system is *internally consistent*, in the sense that it does
not permit static arbitrage across the fixed-income instruments. To address this question, we formalize the standard notions of static arbitrage
in this setting. We begin with the most basic consistency requirement, namely
that prices depend linearly on cash flows.

###### Theorem 2.1 (Law of one price).

The following statements are equivalent:

1. (L1)

   The *law of one price* holds: every portfolio q∈ℝMq\in{\mathbb{R}}^{M} that generates zero cash flows, q⊤​C=0q^{\top}C=0, has zero price, q⊤​P=0q^{\top}P=0.
2. (L2)

   There exists a real-valued discount curve g:[0,∞)→ℝg:[0,\infty)\to{\mathbb{R}} with g​(0)=1g(0)=1 and such that P=C​g​(𝒙)P=C\,g(\bm{x}).

This basic consistency property is strengthened by the following notions of
arbitrage.

###### Definition 2.2.

A portfolio q∈ℝMq\in\mathbb{R}^{M} is called

1. (i)

   a *strict arbitrage* if it has strictly negative price,
   q⊤​P<0q^{\top}P<0, and generates nonnegative cash flows,
   q⊤​C≥0q^{\top}C\geq 0;
2. (ii)

   an *arbitrage* if it has nonpositive price, q⊤​P≤0q^{\top}P\leq 0, and
   generates nonnegative cash flows, q⊤​C≥0q^{\top}C\geq 0, with at least one
   strictly positive component, that is, (q⊤​C)j>0(q^{\top}C)\_{j}>0 for some
   j≤Nj\leq N.

We now derive the fundamental characterization of arbitrage in fixed-income
pricing. To this end, define

|  |  |  |
| --- | --- | --- |
|  | 𝒞≔{C⊤​q:q⊤​P<0},𝒞¯≔{C⊤​q:q⊤​P≤0},\mathcal{C}\coloneq\{\,C^{\top}q:q^{\top}P<0\,\},\qquad\overline{\mathcal{C}}\coloneq\{\,C^{\top}q:q^{\top}P\leq 0\,\}, |  |

the sets of cash-flow vectors generated by portfolios with strictly negative and
nonpositive prices, respectively.
By construction, 𝒞\mathcal{C} is an open convex cone in ℝN\mathbb{R}^{N},
𝒞¯\overline{\mathcal{C}} is a closed convex cone, and indeed
𝒞¯=cl⁡(𝒞)\overline{\mathcal{C}}=\operatorname{cl}(\mathcal{C}).

The next two theorems characterize, first, the absence of strict arbitrage
and, second, the absence of arbitrage, together with their implications for
fixed-income pricing.

###### Theorem 2.3 (Absence of strict arbitrage).

The following statements are equivalent:

1. (W1)

   There is no strict arbitrage.
2. (W2)

   𝒞∩ℝ+N=∅\mathcal{C}\cap\mathbb{R}^{N}\_{+}=\emptyset.
3. (W3)

   There exists a nonnegative discount curve g≥0g\geq 0 with g​(0)=1g(0)=1 and such that P=C​g​(𝒙)P=C\,g(\bm{x}).

Moreover, each of the conditions [(W1)](https://arxiv.org/html/2512.14662v1#S2.I3.i1 "item (W1) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")–[(W3)](https://arxiv.org/html/2512.14662v1#S2.I3.i3 "item (W3) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") implies the law of one price [(L1)](https://arxiv.org/html/2512.14662v1#S2.I1.i1 "item (L1) ‣ Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")–[(L2)](https://arxiv.org/html/2512.14662v1#S2.I1.i2 "item (L2) ‣ Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") in Theorem [2.1](https://arxiv.org/html/2512.14662v1#S2.Thmproposition1 "Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.").

###### Theorem 2.4 (Absence of arbitrage).

The following statements are equivalent:

1. (S1)

   There is no arbitrage.
2. (S2)

   𝒞¯∩ℝ+N={0}\overline{\mathcal{C}}\cap\mathbb{R}^{N}\_{+}=\{0\}.
3. (S3)

   There exists a strictly positive discount curve g>0g>0 with g​(0)=1g(0)=1 and such that P=C​g​(𝒙)P=C\,g(\bm{x}).

Moreover, each of the conditions [(S1)](https://arxiv.org/html/2512.14662v1#S2.I4.i1 "item (S1) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")–[(S3)](https://arxiv.org/html/2512.14662v1#S2.I4.i3 "item (S3) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") implies each
of the weak conditions [(W1)](https://arxiv.org/html/2512.14662v1#S2.I3.i1 "item (W1) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")–[(W3)](https://arxiv.org/html/2512.14662v1#S2.I3.i3 "item (W3) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") in
Theorem [2.3](https://arxiv.org/html/2512.14662v1#S2.Thmproposition3 "Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.").

Here is an example illustrating that no arbitrage is strictly stronger than no strict arbitrage.

###### Example 2.5.

Consider M=N=2M=N=2 fixed-income instruments with prices P1=1P\_{1}=1 and P2=cP\_{2}=c,
and cash-flow vectors C1=[1,0]C\_{1}=[1,0] and C2=[c,1]C\_{2}=[c,1], occurring at dates
0<x1<x20<x\_{1}<x\_{2}, where c>0c>0 is a fixed coupon rate.
The pricing equations imply that any discount curve must satisfy g​(x1)=1g(x\_{1})=1 and g​(x2)=0g(x\_{2})=0.
Thus the discount curve is nonnegative but not strictly positive.
Consequently, there is no strict arbitrage, but arbitrage opportunities exist.

Indeed, the portfolio q=[−c, 1]⊤q=[-c,\,1]^{\top} has price
q⊤​P=0q^{\top}P=0 and generates the nonnegative, nonzero cash-flow
vector q⊤​C=[0,1]q^{\top}C=[0,1].
Hence qq is an arbitrage but not a strict arbitrage.

## 3 Liability Replication and Super-Replication

We consider a liability portfolio that generates expected cash flows
Z=[Z1,…,ZN]Z=[Z\_{1},\dots,Z\_{N}] at the dates xjx\_{j}.555Expected cash flows are understood as
expectations taken under the relevant risk-neutral forward measures. Under
standard assumptions in insurance liability modeling, these expectations
coincide with expectations under the real-world measure.666As for the fixed-income instruments, Zj=0Z\_{j}=0 indicates that no expected
liability cash flow occurs at date xjx\_{j}. Our aim is to replicate these liability cash flows using a portfolio in the
fixed-income instruments.
In the strict sense, this means finding a portfolio q∈ℝMq\in\mathbb{R}^{M} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | q⊤​C=Z.q^{\top}C=Z. |  | (1) |

A portfolio qq satisfying ([1](https://arxiv.org/html/2512.14662v1#S3.E1 "In 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")) exists if and only if
Z⊤∈Im⁡(C⊤)Z^{\top}\in\operatorname{Im}(C^{\top}), or equivalently,
ker⁡(C)⊆ker⁡(Z)\ker(C)\subseteq\ker(Z).
In practice, this requirement may be too strong and need not hold.
We therefore relax perfect replication to *super-replication* and define the
super-replication set

|  |  |  |
| --- | --- | --- |
|  | 𝒬≔{q∈ℝM:q⊤​C≥Z}.\mathcal{Q}\coloneqq\{\,q\in\mathbb{R}^{M}:q^{\top}C\geq Z\,\}. |  |

It is immediate that 𝒬=∩j≤N{q∈ℝM:q⊤​C:,j≥Zj}\mathcal{Q}=\cap\_{j\leq N}\{\,q\in\mathbb{R}^{M}:q^{\top}C\_{:,j}\geq Z\_{j}\,\} is a closed convex polyhedron in ℝM\mathbb{R}^{M},
and every portfolio satisfying ([1](https://arxiv.org/html/2512.14662v1#S3.E1 "In 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")) belongs to 𝒬\mathcal{Q}.

The following result characterizes the feasibility of super-replication.
It shows that the super-replication set 𝒬\mathcal{Q} is nonempty if and only if
there exists no nonnegative discount vector that assigns zero value to all
attainable cash flows while assigning strictly positive value to the liability
cash flows ZZ.

###### Theorem 3.1 (Well-posedness).

The following statements are equivalent:

1. (F1)

   Super-replication is feasible, that is, 𝒬≠∅\mathcal{Q}\neq\emptyset.
2. (F2)

   There exists no vector v∈ℝ+Nv\in\mathbb{R}^{N}\_{+} such that
   C​v=0Cv=0 and Z​v>0Zv>0.

A sufficient condition for [(F1)](https://arxiv.org/html/2512.14662v1#S3.I1.i1 "item (F1) ‣ Theorem 3.1 (Well-posedness). ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")–[(F2)](https://arxiv.org/html/2512.14662v1#S3.I1.i2 "item (F2) ‣ Theorem 3.1 (Well-posedness). ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") to hold is the existence of a
fixed-income instrument ii with nonnegative cash flows whose effective
cash-flow dates coincide with those of the liabilities, in the sense that
Zj≠0Z\_{j}\neq 0 if and only if Ci​j>0C\_{ij}>0 for all j≤Nj\leq N.

In view of Theorem [3.1](https://arxiv.org/html/2512.14662v1#S3.Thmproposition1 "Theorem 3.1 (Well-posedness). ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."), super-replication is more likely to be feasible
when the effective cash-flow dates of the fixed-income instruments and the
liabilities are aligned. When such alignment fails, one may instead work with a
*proxy* cash-flow matrix obtained by aggregating intermediate payments
between liability dates. This proxy has a natural operational interpretation if
intermediate cash proceeds can be held in a cash buffer, or, under no
arbitrage, reinvested at forward-equivalent rates when the corresponding
instruments are available.

###### Remark 3.2 (Cash-flow aggregation).

Let xj1<⋯<xjnx\_{j\_{1}}<\cdots<x\_{j\_{n}} denote the liability payment dates, that is,
Zjk≠0Z\_{j\_{k}}\neq 0. For each fixed-income instrument ii, define a modified
cash-flow matrix C~\tilde{C} by aggregating payments between liability payment dates: with
j0≔0j\_{0}\coloneq 0 and for k=1,…,nk=1,\dots,n,

|  |  |  |
| --- | --- | --- |
|  | C~i,j≔{0,jk−1<j<jk,∑jk−1<s≤jkCi,s,j=jk,Ci,j,j>jn.\tilde{C}\_{i,j}\coloneq\begin{cases}0,&j\_{k-1}<j<j\_{k},\\ \sum\_{j\_{k-1}<s\leq j\_{k}}C\_{i,s},&j=j\_{k},\\ C\_{i,j},&j>j\_{n}.\end{cases} |  |

Operationally, this corresponds to assuming that intermediate cash flows can be
held in a cash buffer until the next liability payment date.

Alternatively, under no arbitrage [(S1)](https://arxiv.org/html/2512.14662v1#S2.I4.i1 "item (S1) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."), intermediate cash flows may be accumulated at
forward-equivalent rates using a strictly positive discount curve g>0g>0 by
setting

|  |  |  |
| --- | --- | --- |
|  | C~i,jk=∑jk−1<s≤jkg​(xs)g​(xjk)​Ci,s.\tilde{C}\_{i,j\_{k}}=\sum\_{j\_{k-1}<s\leq j\_{k}}\frac{g(x\_{s})}{g(x\_{j\_{k}})}\,C\_{i,s}. |  |

In this case gg is also a discount curve for the modified cash-flow matrix,
P=C​g​(𝐱)=C~​g​(𝐱)P=C\,g(\bm{x})=\tilde{C}\,g(\bm{x}). This construction presumes the
availability of the corresponding forward rate agreements.

We now seek a super-replication portfolio of minimal initial cost, that is, a solution to the linear program

|  |  |  |  |
| --- | --- | --- | --- |
|  | minq∈𝒬⁡q⊤​P.\min\_{q\in\mathcal{Q}}q^{\top}P. |  | (2) |

The next theorem provides sufficient conditions under which a minimizer exists.

###### Theorem 3.3.

Assume that there is no arbitrage [(S1)](https://arxiv.org/html/2512.14662v1#S2.I4.i1 "item (S1) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."), that ker⁡(C⊤)={0}\ker(C^{\top})=\{0\}, and that
super-replication is feasible [(F1)](https://arxiv.org/html/2512.14662v1#S3.I1.i1 "item (F1) ‣ Theorem 3.1 (Well-posedness). ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."). Then the optimization problem
([2](https://arxiv.org/html/2512.14662v1#S3.E2 "In 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")) admits at least one solution.

In summary, under the absence of arbitrage and mild regularity conditions, the
super-replication problem is well posed: whenever super-replication is feasible,
there exists a least-cost portfolio that dominates the liability cash flows.

###### Remark 3.4 (Alternative replication criteria).

An alternative to super-replication is quadratic hedging, which seeks a portfolio
q∈ℝMq\in\mathbb{R}^{M} minimizing

|  |  |  |
| --- | --- | --- |
|  | ‖Z−q⊤​C‖22+λ​‖q‖22,\|Z-q^{\top}C\|\_{2}^{2}+\lambda\|q\|\_{2}^{2}, |  |

for some λ>0\lambda>0. This problem is strictly convex and therefore admits a
unique solution. However, it penalizes over- and under-replication symmetrically,
which is typically undesirable in liability replication. Asymmetric loss
functions, such as smoothed hinge penalties, may provide a compromise between
existence, uniqueness, and the one-sided nature of super-replication.

## 4 Illustrative Examples

We illustrate the framework with two prototypical classes of fixed-income
instruments: coupon bonds and interest-rate swaps combined with repo financing.

### 4.1 Coupon Bonds

Government coupon bonds are the canonical fixed-income instruments in our setup.
Such a bond is specified by a face value F>0F>0 paid at maturity TT and coupon
payments c1,…,cnc\_{1},\dots,c\_{n} at dates 0<T1<⋯<Tn=T0<T\_{1}<\dots<T\_{n}=T.
If the bond is indexed by ii, its cash-flow vector is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci,j={cn+F,if ​xj=T,ck,if ​xj=Tk,k=1,…,n−1,0,otherwise.C\_{i,j}=\begin{cases}c\_{n}+F,&\text{if }x\_{j}=T,\\ c\_{k},&\text{if }x\_{j}=T\_{k},\ k=1,\dots,n-1,\\ 0,&\text{otherwise}.\end{cases} |  | (3) |

The corresponding price PiP\_{i} is observed in the bond market.

### 4.2 Interest-Rate Swaps and Repo

We next illustrate how fixed-income cash flows can be generated by combining
interest-rate swaps with repo financing.777Repo refers to a standard
repurchase agreement.

Consider an overnight indexed receiver swap with fixed rate RR, notional 1, and
maturity T=n​ΔT=n\Delta, for a fixed accrual period Δ>0\Delta>0.888For
formal definitions of overnight indexed swaps (OIS), see, for example,
[fil\_tro\_13, Section 2].
The holder receives fixed payments Δ​R\Delta R at dates Tk=k​Δ≤TT\_{k}=k\Delta\leq T and
pays floating interest ξ1,…,ξm\xi\_{1},\dots,\xi\_{m} at dates
0<t1<⋯<tm=T0<t\_{1}<\dots<t\_{m}=T, where ξj\xi\_{j} is the repo rate earned over [tj−1,tj][t\_{j-1},t\_{j}].

We construct the following swap–repo strategy.
Investing 1 in the repo market at inception and rolling it forward produces a
unit payoff at TT and floating cash flows ξj\xi\_{j} at the dates tj≤Tt\_{j}\leq T. Entering the receiver swap at zero initial cost offsets these floating payments
and yields fixed payments Δ​R\Delta R at Tk≤TT\_{k}\leq T. Thus the combined strategy produces exactly the cash flows of a coupon bond with
face value F=1F=1 and coupons ck=Δ​Rc\_{k}=\Delta R. Under the absence of dynamic arbitrage, this synthetic bond must have initial
price 1, since it is generated by a zero-cost swap combined with a unit repo
investment.999This notion of dynamic arbitrage is broader than the static definition in
Definition [2.2](https://arxiv.org/html/2512.14662v1#S2.Thmproposition2 "Definition 2.2. ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.").
If the market price of the bond exceeded 1, one could short the bond and
replicate it using the swap–repo strategy to lock in a risk-free profit, and
similarly if the price were below 1.
Hence the swap–repo strategy can be encoded in the form ([3](https://arxiv.org/html/2512.14662v1#S4.E3 "In 4.1 Coupon Bonds ‣ 4 Illustrative Examples ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")) with
price Pi=1P\_{i}=1.

###### Remark 4.1 (Swap spread puzzle).

Under the absence of dynamic arbitrage, the swap–repo replication of coupon
bonds implies that government bonds and interest rate swaps should be priced
using the same discount curve.
Empirically, however, government bond–swap spreads are persistently nonzero.
This *swap spread puzzle* is commonly attributed to limits to arbitrage arising
from market frictions, balance-sheet and regulatory constraints, and the safe-asset
premium; see, for example, [chr\_mir\_21, wu\_jar\_24, aqu\_etal\_24].

To operationalize the swap–repo strategy in super-replication, suppose there are
MM receiver swaps indexed by i=1,…,Mi=1,\dots,M.
For simplicity we assume that the floating payment dates of the swaps and the
repo roll dates coincide with the fixed-income grid, that is, xj=tjx\_{j}=t\_{j}.
Swap ii has maturity ni​Δn\_{i}\Delta and fixed rate RiR\_{i}.

We collect the fixed and floating swap payments in the M×NM\times N matrices
SS and Ξ\Xi, defined by

|  |  |  |
| --- | --- | --- |
|  | Si,j={Δ​Ri,if ​xj=k​Δ,k=1,…,ni,0,otherwise,Ξi,j={ξj,if ​xj≤ni​Δ,0,otherwise.S\_{i,j}=\begin{cases}\Delta R\_{i},&\text{if }x\_{j}=k\Delta,\ k=1,\dots,n\_{i},\\ 0,&\text{otherwise},\end{cases}\qquad\Xi\_{i,j}=\begin{cases}\xi\_{j},&\text{if }x\_{j}\leq n\_{i}\Delta,\\ 0,&\text{otherwise}.\end{cases} |  |

We also define an M×NM\times N face-value matrix FF by

|  |  |  |
| --- | --- | --- |
|  | Fi,j={1,if ​xj=ni​Δ,0,otherwise.F\_{i,j}=\begin{cases}1,&\text{if }x\_{j}=n\_{i}\Delta,\\ 0,&\text{otherwise}.\end{cases} |  |

The coupon-bond cash-flow matrix corresponding to the swap–repo strategy is

|  |  |  |
| --- | --- | --- |
|  | C=S+F=S−Ξ⏟swap net cash flows+Ξ+F⏟repo net cash flows,C=S+F=\underbrace{S-\Xi}\_{\text{swap net cash flows}}+\underbrace{\Xi+F}\_{\text{repo net cash flows}}, |  |

and the initial prices of these synthetic bonds satisfy P=𝟏P=\bm{1},
since the swap has zero cost and the repo investment requires one unit of initial
funding.101010The cash flows Ξ+F\Xi+F may also be interpreted as those of floating-rate notes
with matching payment and maturity dates.

Suppose that the assumptions of Theorem [3.3](https://arxiv.org/html/2512.14662v1#S3.Thmproposition3 "Theorem 3.3. ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") are satisfied, and let qq be a minimizer of ([2](https://arxiv.org/html/2512.14662v1#S3.E2 "In 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")). The super-replication price of the liabilities is therefore q⊤​𝟏q^{\top}\bm{1}.
To implement the corresponding swap–repo strategy in practice, proceed as
follows.

At inception x0=0x\_{0}=0:

* •

  Invest (lend or borrow) the amount q⊤​𝟏q^{\top}\bm{1} in the repo market.
* •

  Enter qiq\_{i} units of receiver swap ii (zero cost).

At each payment date xjx\_{j}:

1. (i)

   Receive (or pay) floating interest and notional
   ∑i:xj≤ni​Δqi​(ξj+1)\sum\_{i:x\_{j}\leq n\_{i}\Delta}q\_{i}(\xi\_{j}+1) from the repo market.
2. (ii)

   Reinvest ∑i:xj<ni​Δqi\sum\_{i:x\_{j}<n\_{i}\Delta}q\_{i} in the repo market.
3. (iii)

   Offset the floating legs of the swaps, contributing
   (q⊤​Ξ)j=∑i:xj≤ni​Δqi​ξj(q^{\top}\Xi)\_{j}=\sum\_{i:x\_{j}\leq n\_{i}\Delta}q\_{i}\xi\_{j}.
4. (iv)

   Receive (or pay) fixed swap interest (q⊤​S)j(q^{\top}S)\_{j}.

The repo-related transactions in [(i)](https://arxiv.org/html/2512.14662v1#S4.I2.i1 "item (i) ‣ 4.2 Interest-Rate Swaps and Repo ‣ 4 Illustrative Examples ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")–[(ii)](https://arxiv.org/html/2512.14662v1#S4.I2.i2 "item (ii) ‣ 4.2 Interest-Rate Swaps and Repo ‣ 4 Illustrative Examples ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") generate the cash flow
(q⊤​(Ξ+F))j(q^{\top}(\Xi+F))\_{j}, while the swap-related transactions in [(iii)](https://arxiv.org/html/2512.14662v1#S4.I2.i3 "item (iii) ‣ 4.2 Interest-Rate Swaps and Repo ‣ 4 Illustrative Examples ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")–[(iv)](https://arxiv.org/html/2512.14662v1#S4.I2.i4 "item (iv) ‣ 4.2 Interest-Rate Swaps and Repo ‣ 4 Illustrative Examples ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") generate
(q⊤​(S−Ξ))j(q^{\top}(S-\Xi))\_{j}.
Altogether, the net cash flow is (q⊤​(S+F))j=(q⊤​C)j(q^{\top}(S+F))\_{j}=(q^{\top}C)\_{j}, which by
construction satisfies

|  |  |  |
| --- | --- | --- |
|  | (q⊤​C)j≥Zj,(q^{\top}C)\_{j}\;\geq\;Z\_{j}, |  |

and thus super-replicates the expected liability cash flows.

## 5 Conclusion and Outlook

This paper develops a static, model-free framework for fixed-income pricing and
the replication of liabilities. We establish a fundamental
theorem of fixed-income pricing, characterizing arbitrage-free prices through
the existence of a discount curve, and apply this framework to the
super-replication of expected liability cash flows.

An important open question concerns the uniqueness of least-cost
super-replicating portfolios. While existence follows under mild assumptions,
the linear structure of the optimization problem generally permits multiple
solutions. Identifying conditions under which uniqueness holds, or
characterizing the structure of the optimal solution set, remains an interesting
direction for further research.

Overall, the results provide a unified static foundation for fixed-income
pricing and liability replication, with implications for asset–liability
management, discount-curve construction, and economic and regulatory capital
assessment.

## Appendix A Proofs

This appendix collects all proofs.

### A.1 Proof of Theorem [2.1](https://arxiv.org/html/2512.14662v1#S2.Thmproposition1 "Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")

The law of one price is equivalent to ker⁡(C⊤)⊆ker⁡(P⊤)\ker(C^{\top})\subseteq\ker(P^{\top}), which again is equivalent to Im⁡P∈Im⁡C\operatorname{Im}P\in\operatorname{Im}C.

[(L1)](https://arxiv.org/html/2512.14662v1#S2.I1.i1 "item (L1) ‣ Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇒\Rightarrow[(L2)](https://arxiv.org/html/2512.14662v1#S2.I1.i2 "item (L2) ‣ Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): By the above there exists a v∈ℝNv\in{\mathbb{R}}^{N} such that P=C​vP=Cv. Given such a vv, we obtain a curve g:[0,∞)→ℝg:[0,\infty)\to{\mathbb{R}} with g​(0)=1g(0)=1 by linearly interpolating g​(𝒙)=vg(\bm{x})=v and g​(0)=1g(0)=1, for x∈[0,xN]x\in[0,x\_{N}], and setting g​(x)=e−y∞​(x−xN)​g​(xN)g(x)={\rm e}^{-y\_{\infty}(x-x\_{N})}g(x\_{N}) for x>xNx>x\_{N}, for some auxiliary long maturity yield y∞≥0y\_{\infty}\geq 0.

[(L2)](https://arxiv.org/html/2512.14662v1#S2.I1.i2 "item (L2) ‣ Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇒\Rightarrow[(L1)](https://arxiv.org/html/2512.14662v1#S2.I1.i1 "item (L1) ‣ Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): This follows trivially by the above.

### A.2 Proof of Theorem [2.3](https://arxiv.org/html/2512.14662v1#S2.Thmproposition3 "Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")

[(W1)](https://arxiv.org/html/2512.14662v1#S2.I3.i1 "item (W1) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇔\Leftrightarrow[(W2)](https://arxiv.org/html/2512.14662v1#S2.I3.i2 "item (W2) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): this is elementary.

[(W2)](https://arxiv.org/html/2512.14662v1#S2.I3.i2 "item (W2) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇔\Leftrightarrow[(W3)](https://arxiv.org/html/2512.14662v1#S2.I3.i3 "item (W3) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): Farkas’ Lemma [roc\_97, Corollary 22.3.1] states that [(W2)](https://arxiv.org/html/2512.14662v1#S2.I3.i2 "item (W2) ‣ Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") holds if and only if there exists a vector v≥0v\geq 0 such that P=C​vP=Cv. Given such a vv, we obtain a desired nonnegative curve g:[0,∞)→[0,∞)g:[0,\infty)\to[0,\infty) by linearly inter-extrapolating gg as in the proof of Theorem [2.1](https://arxiv.org/html/2512.14662v1#S2.Thmproposition1 "Theorem 2.1 (Law of one price). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.").

For the last statement, let qq be such that q⊤​C=0q^{\top}C=0. Now apply no strict arbitrage to qq and −q-q, which implies q⊤​P≥0q^{\top}P\geq 0 and −q⊤​P≥0-q^{\top}P\geq 0, and thus q⊤​P=0q^{\top}P=0.

### A.3 Proof of Theorem [2.4](https://arxiv.org/html/2512.14662v1#S2.Thmproposition4 "Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")

[(S1)](https://arxiv.org/html/2512.14662v1#S2.I4.i1 "item (S1) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇔\Leftrightarrow[(S2)](https://arxiv.org/html/2512.14662v1#S2.I4.i2 "item (S2) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): this is elementary.

[(S2)](https://arxiv.org/html/2512.14662v1#S2.I4.i2 "item (S2) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇒\Rightarrow[(S3)](https://arxiv.org/html/2512.14662v1#S2.I4.i3 "item (S3) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): as ℝ+N{\mathbb{R}}^{N}\_{+} is a pointed convex cone, i.e., ℝ+N∩(−ℝ+N)={0}{\mathbb{R}}^{N}\_{+}\cap(-{\mathbb{R}}^{N}\_{+})=\{0\}, Klee’s separation theorem [kle\_55, Theorem (2.5)] applies, stating that there exists a v∈ℝNv\in{\mathbb{R}}^{N} such that v⊤​w>0v^{\top}w>0 for all w∈ℝ+N∖{0}w\in{\mathbb{R}}^{N}\_{+}\setminus\{0\} and z⊤​v≤0z^{\top}v\leq 0 for all z∈𝒞¯z\in\overline{{\mathcal{C}}}. From the first it follows that vj>0v\_{j}>0 for all j≤Nj\leq N. From the second it follows that q⊤​C​v≤0q^{\top}Cv\leq 0 for all q∈ℝMq\in{\mathbb{R}}^{M} with q⊤​P≤0q^{\top}P\leq 0. This implies that P=s​C​vP=sCv for some s>0s>0. Setting g​(𝒙)=s​vg(\bm{x})=sv and inter-extrapolating gg as in the proof of Theorem [2.3](https://arxiv.org/html/2512.14662v1#S2.Thmproposition3 "Theorem 2.3 (Absence of strict arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.") gives the desired positive discount curve g:[0,∞)→(0,∞)g:[0,\infty)\to(0,\infty).

[(S3)](https://arxiv.org/html/2512.14662v1#S2.I4.i3 "item (S3) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇒\Rightarrow[(S2)](https://arxiv.org/html/2512.14662v1#S2.I4.i2 "item (S2) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): Let g>0g>0 be a positive discount curve such that P=C​g​(𝒙)P=Cg(\bm{x}). Let w=C⊤​q∈𝒞¯∩ℝ+Nw=C^{\top}q\in\overline{{\mathcal{C}}}\cap{\mathbb{R}}^{N}\_{+}. Then 0≥q⊤​P=q⊤​C​g​(𝒙)≥00\geq q^{\top}P=q^{\top}Cg(\bm{x})\geq 0, as also q⊤​C≥0q^{\top}C\geq 0. This implies q⊤​C=0q^{\top}C=0, which proves [(S2)](https://arxiv.org/html/2512.14662v1#S2.I4.i2 "item (S2) ‣ Theorem 2.4 (Absence of arbitrage). ‣ 2 A Fundamental Theorem of Fixed-Income Pricing ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.").

The last statement follows trivially.

### A.4 Proof of Theorem [3.1](https://arxiv.org/html/2512.14662v1#S3.Thmproposition1 "Theorem 3.1 (Well-posedness). ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")

[(F1)](https://arxiv.org/html/2512.14662v1#S3.I1.i1 "item (F1) ‣ Theorem 3.1 (Well-posedness). ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")⇔\Leftrightarrow[(F2)](https://arxiv.org/html/2512.14662v1#S3.I1.i2 "item (F2) ‣ Theorem 3.1 (Well-posedness). ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich."): this follows from Farks’s lemma (in the form of [roc\_97, Theorem 22.1]) applied to the system C⊤​q≥Z⊤C^{\top}q\geq Z^{\top}.

The last statement follows by setting q=t​eiq=te\_{i}, for t=max⁡{maxj⁡Zj,0}minj⁡Ci​j>0t=\frac{\max\{\max\_{j}Z\_{j},0\}}{\min\_{j}C\_{ij}}>0 and where eie\_{i} is the iith standard basis vector in ℝN{\mathbb{R}}^{N}.

### A.5 Proof of Theorem [3.3](https://arxiv.org/html/2512.14662v1#S3.Thmproposition3 "Theorem 3.3. ‣ 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")

Let q0∈𝒬q\_{0}\in{\mathcal{Q}} and define the lower level set 𝒬0≔{q∈𝒬:q⊤​P≤q0⊤​P}{\mathcal{Q}}\_{0}\coloneqq\{q\in{\mathcal{Q}}:q^{\top}P\leq q\_{0}^{\top}P\} the set of all super-replicating strategies with price less than or equal to q0⊤​Pq\_{0}^{\top}P. Then 𝒬0≠∅{\mathcal{Q}}\_{0}\neq\emptyset and we can replace 𝒬{\mathcal{Q}} by 𝒬0{\mathcal{Q}}\_{0} in ([2](https://arxiv.org/html/2512.14662v1#S3.E2 "In 3 Liability Replication and Super-Replication ‣ Fixed-Income Pricing and the Replication of Liabilities1footnote 11footnote 1This paper was written while the author was a guest of the FinsureTech Hub, Department of Mathematics, ETH Zurich.")). We now show that 𝒬0{\mathcal{Q}}\_{0} is compact, from which the theorem then follows.

Thereto, let r​e​c​(𝒬0)={v∈ℝM:q+t​v∈𝒬0,∀t≥0,∀q∈𝒬0}rec({\mathcal{Q}}\_{0})=\{v\in{\mathbb{R}}^{M}:q+tv\in{\mathcal{Q}}\_{0},\,\forall t\geq 0,\,\forall q\in{\mathcal{Q}}\_{0}\} denote the recession cone of 𝒬0{\mathcal{Q}}\_{0}. Let v∈r​e​c​(𝒬0)v\in rec({\mathcal{Q}}\_{0}) and q∈𝒬0q\in{\mathcal{Q}}\_{0}. Then it holds (q+t​v)⊤​C≥Z(q+tv)^{\top}C\geq Z for all t≥0t\geq 0, which implies that v⊤​C≥0v^{\top}C\geq 0. We claim that v=0v=0. Indeed, suppose v≠0v\neq 0. Then (v⊤​C)j>0(v^{\top}C)\_{j}>0 for at least one cash flow j≤Nj\leq N by assumption. By no arbitrage therefore v⊤​P>0v^{\top}P>0 and thus (q+t​v)⊤​P(q+tv)^{\top}P is unbounded from above in t≥0t\geq 0, which is absurd. Hence r​e​c​(𝒬0)={0}rec({\mathcal{Q}}\_{0})=\{0\}.

On the other hand, 𝒬0{\mathcal{Q}}\_{0} is closed and convex by construction. Hence 𝒬0{\mathcal{Q}}\_{0} is compact, see [roc\_97, Theorem 8.4], which completes the proof.