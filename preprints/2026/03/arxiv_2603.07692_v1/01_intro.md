---
authors:
- Nick L. Gunther
- Alec N. Kercheval
- Ololade Sowunmi
doc_id: arxiv:2603.07692v1
family_id: arxiv:2603.07692
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Understanding the Long-Only Minimum Variance Portfolio
url_abs: http://arxiv.org/abs/2603.07692v1
url_html: https://arxiv.org/html/2603.07692v1
venue: arXiv q-fin
version: 1
year: 2026
---


Nicholas Gunther
  
Consortium for Data Analytics in Risk (CDAR), UC Berkeley
  
nlgunther@gmail.com
  
Alec Kercheval
  
Dept. of Mathematics, Florida State University and CDAR, UC Berkeley
  
akercheval@fsu.edu
  
Ololade Sowunmi
  
Dept. of Mathematics, Florida State University
  
osowunmi@fsu.edu

(First version: 10 Dec 2024; This version: 9 July 2025)

###### Abstract

For a covariance matrix coming from a factor model of returns, we investigate the relationship between the long-only global minimum variance portfolio and the asset exposures to the factors. In the case of a 1-factor model, we provide a rigorous and explicit description of the long-only solution in terms of the parameters of the covariance matrix. For q>1q>1 factors, we provide a description of the long-only portfolio in geometric terms. The results are illustrated with empirical daily returns of US stocks.

## 1  Long-only minimum variance

### 1.1  Introduction

There is a long-standing interest in equity portfolios optimized to have the lowest possible variance. The optimal such portfolio depends on the covariances between pairs of assets, and on the particular constraints of interest.

If there are pp assets available for investment, we denote by w=(w1,…,wp)⊤∈𝐑pw=(w\_{1},\dots,w\_{p})^{\top}\in\mathbf{R}^{p} the pp-dimensional vector of asset weights defining the portfolio. The global minimum variance portfolio wL​Sw^{LS} denotes the long-short portfolio solving the simplest problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minw∈𝐑p⁡w⊤​Σ​ww⊤​𝟏p=1,\begin{split}&\min\_{w\in\mathbf{R}^{p}}w^{\top}\Sigma w\\ &w^{\top}\mathbf{1}\_{p}=1,\end{split} |  | (1) |

where Σ\Sigma denotes the positive definite covariance matrix of asset returns; 𝟏p\mathbf{1}\_{p} denotes the vector of dimension pp whose every entry is 1;
and w⊤​𝟏p=1w^{\top}\mathbf{1}\_{p}=1 is the full investment condition setting the sum of the weights equal to 1.
For the long-short portfolio, some of the weights may be negative.

Our focus is the long-only minimum variance (LOMV) problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minw∈𝐑p⁡w⊤​Σ​ww⊤​𝟏p=1wi≥0​ for all i=1,2,…,p.\begin{split}&\min\_{w\in\mathbf{R}^{p}}w^{\top}\Sigma w\\ &w^{\top}\mathbf{1}\_{p}=1\\ &w\_{i}\geq 0\text{ }\text{for all $i=1,2,...,p$.}\end{split} |  | (2) |

The long-only constraints wi≥0w\_{i}\geq 0 are often required for real investment portfolios due to the complications and costs of short positions.

The solution w=wL{w=w^{L}} of ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) represents the long-only fully invested global minimum risk portfolio, and can be contrasted with the solution wL​Sw^{LS} of the long-short problem.
The portfolio wL​Sw^{LS} solving problem ([1](#S1.E1 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) is given by the
simple formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | wL​S=Σ−1​𝟏p𝟏p⊤​Σ−1​𝟏p.w^{LS}=\frac{\Sigma^{-1}\mathbf{1}\_{p}}{\mathbf{1}\_{p}^{\top}\Sigma^{-1}\mathbf{1}\_{p}}. |  | (3) |

The long-only problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) is less straightforward.

As we show in this article, the main difficulty in problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) is determining which are the active (positive weight) assets in the optimal portfolio, or, equivalently, which are the assets for which the long-only constraints are binding.
Denote by K={i≤p:wiL>0}K=\{i\leq p:w^{L}\_{i}>0\} the set of active assets in the long-only optimal portfolio, and let k≤pk\leq p denote the number of elements of KK . Once we have determined KK, Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") solves the problem: if we denote by ΣK\Sigma^{K} the k×kk\times k matrix obtained from Σ\Sigma by deleting all the rows and columns not in KK, then the kk positive weights of wLw^{L} are given by the corresponding entries of the kk-dimensional vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | wK=(ΣK)−1​𝟏k𝟏k⊤​(ΣK)−1​𝟏k.w^{K}=\frac{(\Sigma^{K})^{-1}\mathbf{1}\_{k}}{\mathbf{1}\_{k}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{k}}. |  | (4) |

In short, the active long-only minimum risk portfolio holdings are those of the long-short minimum risk portfolio corresponding to a reduced set of available assets. This is intuitively reasonable111Geometrically, if, for example, the active LOMV assets are the first kk in the list, then the corresponding kk-vector minimizes kk-dimensional variance in the interior of the positive kk-orthant. because the long-only constraints are not binding on the positive holdings of wLw^{L}.

This leaves the problem of determining KK, the set of active assets of wLw^{L}, which is normally much smaller than the set of positive-weight assets in the long-short portfolio wL​Sw^{LS} (e.g. Figure ([2](#S2.F2 "Figure 2 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"))). In this article we analyze that problem when the covariance matrix comes from a factor model.
In the case of a single-factor model, we provide an essentially explicit description of KK below in Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"). There, one factor explains covariance between assets, and the covariance matrix takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=σ2​β​β⊤+Δ,\Sigma=\sigma^{2}\beta\beta^{\top}+\Delta, |  | (5) |

where σ2>0\sigma^{2}>0 is the factor return variance, β\beta is a pp-vector of exposures to the factor, and Δ\Delta is a diagonal matrix of specific variances.

In the case of a multiple factor model with q>1q>1 factors, the p×pp\times p covariance matrix takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=B​Ω​B⊤+Δ,\Sigma=B\Omega B^{\top}+\Delta, |  | (6) |

where BB is a p×qp\times q matrix whose columns are the asset exposures to each of qq factors, and Ω\Omega is a q×qq\times q invertible matrix of factor variances, diagonal in the case when the columns of BB are principal components. When q>1q>1, we know of no direct way to compute the set KK of active assets that is similar to Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"). However, Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") gives us a necessary condition satisfied by KK, as follows. Let Bi∈𝐑qB\_{i}\in\mathbf{R}^{q} denote the iith row of BB. Then there is a (q−1)(q-1)-dimensional hyperplane HH in 𝐑q\mathbf{R}^{q} such that the elements ii of KK are all those such that BiB\_{i} lies on the same side of HH as the origin.

The single factor case was studied in Clarke et al. [[2011](#bib.bib13 "Minimum-variance portfolio composition")], where they assume the single factor is the market return, and provide an implicit solution to the long-only problem that is equivalent to the one here when our vector beta of exposures to the single factor is taken to be the market beta. Their article inspired our work, and we discuss the relationship between their results and ours further below.

### 1.2  Main Results

We state the results outlined above in more detail in this section. The proofs of the following theorems appear in Section [3](#S3 "3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio").

Assumption for Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"). Suppose that the covariance matrix Σ\Sigma of returns for a universe of pp assets is an arbitrary p×pp\times p symmetric positive definite matrix.

###### Theorem 1.

Denote by wLw^{L} the solution of problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) and let KK denote the set of active assets in wLw^{L}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | K={i≤p:wiL>0},K=\{i\leq p:w^{L}\_{i}>0\}, |  | (7) |

and k=|K|≤pk=|K|\leq p, the number of active assets.
Let ΣK,0\Sigma^{K,0} be the modified matrix obtained from Σ\Sigma by setting to zero the rows and columns not belonging to KK.

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | wL=(ΣK,0)+​𝟏p𝟏p⊤​(ΣK,0)+​𝟏pw^{L}=\frac{(\Sigma^{K,0})^{+}\mathbf{1}\_{p}}{\mathbf{1}\_{p}^{\top}(\Sigma^{K,0})^{+}\mathbf{1}\_{p}} |  | (8) |

where + denotes the Moore-Penrose inverse.222For a symmetric matrix SS with singular value decomposition S=U​D​U⊤S=UDU^{\top} for orthogonal UU and diagonal DD, the Moore-Penrose inverse is defined by S+=U​D+​U⊤S^{+}=UD^{+}U^{\top}, where the diagonal matrix D+D^{+} is obtained by replacing each nonzero element by its inverse.

Equivalently, if we denote by wKw^{K} the kk-vector obtained by deleting all the zero entries of the pp-vector wLw^{L}, and ΣK\Sigma^{K} denotes the k×kk\times k matrix obtained from Σ\Sigma by deleting the rows and columns not belonging to KK, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | wK=(ΣK)−1​𝟏k𝟏k⊤​(ΣK)−1​𝟏k.w^{K}=\frac{(\Sigma^{K})^{-1}\mathbf{1}\_{k}}{\mathbf{1}\_{k}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{k}}. |  | (9) |

This is the unique solution of the kk-dimensional long-short problem ([1](#S1.E1 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) with
Σ\Sigma replaced by ΣK\Sigma^{K}, and wLw^{L} can be recovered from wKw^{K} by adding back zero entries for the deleted assets.

Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") allows us to determine the long-only minimum risk portfolio as soon as we know the set KK of active assets. It remains only to determine KK, and for the single-index case q=1q=1 this can be accomplished by an explicit method described next in Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio").

Assumptions for Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"). Assume now a single-factor returns model which gives the covariance matrix Σ\Sigma the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=σ2​β​β⊤+Δ,\Sigma=\sigma^{2}\beta\beta^{\top}+\Delta, |  | (10) |

where σ2>0\sigma^{2}>0 is the factor return variance, β\beta is a pp-vector of factor exposures, and Δ=d​i​a​g​(δ12,δ22,…,δp2)\Delta=diag(\delta\_{1}^{2},\delta\_{2}^{2},...,\delta\_{p}^{2}) is a diagonal matrix of non-zero idiosyncratic asset return variances δi2>0\delta\_{i}^{2}>0.

We permit the entries βi\beta\_{i} of β\beta to be positive, negative, or zero, but assume the generic condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1pβiδi2≠0.\sum\_{i=1}^{p}\frac{\beta\_{i}}{\delta\_{i}^{2}}\neq 0. |  | (11) |

Notice that the vector β\beta may be replaced by −β-\beta without changing Σ\Sigma, so without loss of generality we choose the sign so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1pβiδi2>0,\sum\_{i=1}^{p}\frac{\beta\_{i}}{\delta\_{i}^{2}}>0, |  | (12) |

as would be the case if all the betas were positive.

In addition, by re-ordering the assets if necessary, for convenience we further assume without loss of generality that the betas are arranged in increasing order:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β1≤β2≤⋯≤βp.\beta\_{1}\leq\beta\_{2}\leq\cdots\leq\beta\_{p}. |  | (13) |

With these assumptions, our main result is

###### Theorem 2.

(Explicit Solution to the long-only constrained problem under a 1-factor model)
Assume the betas βi\beta\_{i} are arranged in increasing order.

1. 1.

   Let R1=1σ2R\_{1}=\frac{1}{\sigma^{2}}, and for 2≤i≤p2\leq i\leq p, let

   |  |  |  |
   | --- | --- | --- |
   |  | Ri=1σ2+∑j=1i−1βjδj2​(βj−βi).R\_{i}={\frac{1}{\sigma^{2}}+\sum\_{j=1}^{i-1}\frac{\beta\_{j}}{\delta\_{j}^{2}}(\beta\_{j}-\beta\_{i})}. |  |

   Then there exists s≤ps\leq p such that the initially positive sequence {Ri}\{R\_{i}\} is monotonically increasing until i=si=s, then monotonically decreasing for i>si>s. That is,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 0<R1≤R2≤⋯≤Rs≥Rs+1≥⋯≥Rp.0<R\_{1}\leq R\_{2}\leq\cdots\leq R\_{s}\geq R\_{s+1}\geq\cdots\geq R\_{p}. |  | (14) |

   In particular, the sequence {Ri}\{R\_{i}\} crosses zero at most once.
2. 2.

   Let wLw^{L} denote the solution of problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")), K={i≤p:wiL>0}K=\{i\leq p:w^{L}\_{i}>0\}, and k=|K|k=|K|.

   Then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | k=max⁡{i≤p:Ri>0}​ and ​K={1,2,…,k}.k=\max\big\{i\leq p:R\_{i}>0\big\}\text{ and }K=\{1,2,\dots,k\}. |  | (15) |

   Applying Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"), we may conclude the following. Let ΣK,0\Sigma^{K,0} be the block-diagonal matrix obtained from Σ\Sigma by replacing all but the first kk rows and columns with zeros. Then the solution wLw^{L} is given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | wL=(ΣK,0)+​𝟏p𝟏p⊤​(ΣK,0)+​𝟏pw^{L}=\frac{(\Sigma^{K,0})^{+}\mathbf{1}\_{p}}{\mathbf{1}\_{p}^{\top}(\Sigma^{K,0})^{+}\mathbf{1}\_{p}} |  | (16) |

   where ++ denotes the Moore-Penrose inverse.

For an equivalent formulation in terms of ordinary matrix inverse, let ΣK\Sigma^{K} be the k×kk\times k submatrix of Σ\Sigma consisting of the first kk rows and columns. Denote by wKw^{K},

|  |  |  |  |
| --- | --- | --- | --- |
|  | wK=(ΣK)−1​𝟏k𝟏k⊤​(ΣK)−1​𝟏k,w^{K}=\frac{(\Sigma^{K})^{-1}\mathbf{1}\_{k}}{\mathbf{1}\_{k}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{k}}, |  | (17) |

the long-short fully invested minimum variance solution for the first kk assets.

Then the solution wL=(w1L,…,wpL)⊤w^{L}=(w\_{1}^{L},\dots,w\_{p}^{L})^{\top} of ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | wiL=wiK​ for i=1,…,kwiL=0​ for ​i=k+1,…,p.\begin{split}&w^{L}\_{i}=w^{K}\_{i}\text{ for $i=1,...,k$}\\ &w^{L}\_{i}=0\text{ for }i=k+1,\dots,p.\\ \end{split} |  | (18) |

We note that k=pk=p if the long-short fully invested minimum variance portfolio happens to be long-only already. Otherwise, k<pk<p, Rp<0R\_{p}<0, and the sequence {Ri}\{R\_{i}\} crosses zero exactly once. In this situation, kk has the property

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rk>0​ and ​Rk+1=Rk+(βk−βk+1)​∑j=1kβjδj2≤0.R\_{k}>0\mbox{ and }R\_{k+1}=R\_{k}+(\beta\_{k}-\beta\_{k+1})\sum\_{j=1}^{k}\frac{\beta\_{j}}{\delta\_{j}^{2}}\leq 0. |  | (19) |

This means that the threshold index kk and the solution ww are not influenced by the values of δj\delta\_{j} for j>kj>k, nor by the values of βj\beta\_{j} for βj>βk+1\beta\_{j}>\beta\_{k+1}.

The proof of Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") also establishes, via Lemma [4](#Thmlemma4 "Lemma 4. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio") below, the following

###### Corollary 1.

Under the assumptions above, if ww is the solution of problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi>0​ if and only if ​βi<1σ2+∑j=1kβj2δj2∑j=1kβjδj2.w\_{i}>0\mbox{ if and only if }\beta\_{i}<\frac{\frac{1}{\sigma^{2}}+\sum\_{j=1}^{k}\frac{\beta^{2}\_{j}}{\delta\_{j}^{2}}}{\sum\_{j=1}^{k}\frac{\beta\_{j}}{\delta\_{j}^{2}}}. |  | (20) |

The solution of problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) in semi-explicit form was previously described by R. Clarke, H. de Silva, and S. Thorley in Clarke et al. [[2011](#bib.bib13 "Minimum-variance portfolio composition")]. They give the following condition, which is closely related to
Corollary [1](#Thmcorollary1 "Corollary 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi>0​ if and only if ​βi<τ,w\_{i}>0\mbox{ if and only if }\beta\_{i}<\tau, |  | (21) |

where τ\tau is the solution of the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ=1σ2+∑βi<τβj2δj2∑βi<τβjδj2.\tau=\frac{\frac{1}{\sigma^{2}}+\sum\_{\beta\_{i}<\tau}\frac{\beta^{2}\_{j}}{\delta\_{j}^{2}}}{\sum\_{\beta\_{i}<\tau}\frac{\beta\_{j}}{\delta\_{j}^{2}}}. |  | (22) |

The solution described in Clarke et al. [[2011](#bib.bib13 "Minimum-variance portfolio composition")] is equivalent to ([17](#S1.E17 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) and ([20](#S1.E20 "In Corollary 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")). Both solutions require the assumption ([12](#S1.E12 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")), as a simple argument shows:
In the absence of any hypotheses about the signs of the betas, replacing β\beta by −β-\beta leaves the covariance matrix Σ\Sigma, and hence the solution ww, unchanged. But in that case the long positions of ww would correspond to betas above a threshold, not below it, contradicting the threshold condition.

The need for assumption ([12](#S1.E12 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) is easily overlooked because it likely always holds for betas actually observed in the market. In our one-factor world, if the betas are defined relative to a benchmark portfolio wBw\_{B} that belongs to our investable universe of pp assets, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | wB∈𝐑p​ and ​β=Σ​wBσB2,w\_{B}\in\mathbf{R}^{p}\mbox{ and }\beta=\frac{\Sigma w\_{B}}{\sigma\_{B}^{2}}, |  | (23) |

then a calculation similar to the ones in Section [3](#S3 "3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio") shows that ([12](#S1.E12 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) holds if and only if the benchmark wBw\_{B} is net long, wB⊤​𝟏p>0w\_{B}^{\top}\mathbf{1}\_{p}>0.
This will be the case for any reasonable benchmark.

The closed form solution ([17](#S1.E17 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) depends on first determining kk from ([15](#S1.E15 "In item 2 ‣ Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")). From the monotonicity properties of {Ri}\{R\_{i}\}, this may be quickly accomplished, for example, by the bisection method in O​(log⁡p)O(\log p) steps.

The multifactor case. When there are q>1q>1 factors, there is no simple way to order the betas or immediately use them directly to identify the active assets in the long-only portfolio. The next theorem tells us that we do know something about them: their corresponding betas are exactly those that lie in a particular half-space in 𝐑q\mathbf{R}^{q}.

Assumptions for Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio").
We assume asset returns follow a qq-factor model, so that the covariance matrix of asset returns takes the form of the p×pp\times p matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=B​Ω​B⊤+Δ,\Sigma=B\Omega B^{\top}+\Delta, |  | (24) |

where BB is a p×qp\times q matrix whose columns are the asset exposures to the qq factors, Ω\Omega is a q×qq\times q diagonal matrix of positive factor variances, and Δ\Delta is a p×pp\times p diagonal matrix of positive asset specific variances.

As before, for any subset KK of the indices
{1,2,…,p}\{1,2,\dots,p\}, if k=|K|k=|K|, we denote by ΣK,0\Sigma^{K,0} the p×pp\times p matrix obtained from Σ\Sigma by setting all the rows and columns not in KK to zero, ΣK\Sigma^{K} the k×kk\times k principal submatrix obtained by deleting the rows and columns not in KK, and BKB^{K} the k×qk\times q matrix obtained by deleting the rows of BB not in KK.

###### Theorem 3 (Hyperplane separation for qq-factor models).

Suppose that wLw^{L} is the solution of problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) for the covariance matrix ([24](#S1.E24 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")). Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | K={i≤p:wiL>0}K=\{i\leq p:w^{L}\_{i}>0\} |  | (25) |

and k=|K|k=|K| the cardinality of KK.

Define the qq-dimensional column vector hKh^{K} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | hK=Ω​(BK)⊤​(ΣK)−1​𝟏k=Ω​B⊤​(ΣK,0)+​𝟏p.h^{K}=\Omega(B^{K})^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{k}=\Omega B^{\top}(\Sigma^{K,0})^{+}\mathbf{1}\_{p}. |  | (26) |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | wiL>0​ if and only if ​Bi​hK<1,w^{L}\_{i}>0\text{ if and only if }B\_{i}h^{K}<1, |  | (27) |

where BiB\_{i} the qq-dimensional iith row of BB.

Geometrically, the condition of Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") can be described in terms of the hyperplane HH of 𝐑q\mathbf{R}^{q} defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | H={x∈𝐑q:x⊤​hK=1}.H=\{x\in\mathbf{R}^{q}:x^{\top}h^{K}=1\}. |  | (28) |

It says that the assets included in the long-only optimal portfolio are those whose factor exposure vectors BiB\_{i} in 𝐑q\mathbf{R}^{q} lie on the same side of HH as the origin. See Figure [5](#S2.F5 "Figure 5 ‣ 2.3 Empirical example for a two-factor model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") for an illustration when q=2q=2.

The next corollary gives alternative hyperplane formulation that is sometimes useful.

###### Corollary 2.

With the same assumptions and notation of Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"), let

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | hL\displaystyle h^{L} | =\displaystyle= | (Ω−1+(BK)⊤​(ΔK)−1​BK)−1​(BK)⊤​(ΔK)−1​𝟏k\displaystyle\left(\Omega^{-1}+(B^{K})^{\top}(\Delta^{K})^{-1}B^{K}\right)^{-1}(B^{K})^{\top}(\Delta^{K})^{-1}\mathbf{1}\_{k} |  | (29) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | =\displaystyle= | (Ω−1+B⊤​(ΔK,0)+​B)−1​B⊤​(ΔK,0)+​𝟏p.\displaystyle\left(\Omega^{-1}+B^{\top}(\Delta^{K,0})^{+}B\right)^{-1}B^{\top}(\Delta^{K,0})^{+}\mathbf{1}\_{p}. |  | (30) |

Then BK​hL=BK​hKB^{K}h^{L}=B^{K}h^{K}, and hence
wiL>0w^{L}\_{i}>0 if and only if Bi​hL<1.B\_{i}h^{L}<1.

We note that in the typical case where BKB^{K} has full rank q<kq<k,
BK​hL=BK​hKB^{K}h^{L}=B^{K}h^{K} implies hL=hKh^{L}=h^{K}, so the the formulations of Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") and Corollary [2](#Thmcorollary2 "Corollary 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") are equivalent.

Unlike Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"), Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") does not provide a direct computational method for determining wLw^{L}. Instead, it provides a necessary condition satisfied by the active assets in terms of their qq-vectors BiB\_{i}, i=1,…,pi=1,\dots,p, as a generalization of the 1-factor setting: the included BiB\_{i} are the ones below a certain threshold, where the threshold in qq dimensions is determined by a (q−1)(q-1)-dimensional hyperplane HH.

In typical applications, such as in the illustration below in section [2.3](#S2.SS3 "2.3 Empirical example for a two-factor model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"), pp is much greater than the number nn of samples. In this case, when the factor exposures are bounded and have a positive variance across assets, we expect that BK​(ΔK)−1​BKB^{K}(\Delta^{K})^{-1}B^{K} will dominate Ω−1\Omega^{-1} by a factor proportional to pp. In the limiting case where Ω−1\Omega^{-1} is set to zero, hLh^{L} in equation ([29](#S1.E29 "In Corollary 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) can be viewed as a vector of coefficients of a weighted least squares regression of 𝟏\mathbf{1} onto the columns of BKB^{K} with weight matrix Δ−1\Delta^{-1}.333We thank Lisa Goldberg for this observation.

In the one-factor case q=1q=1, the condition of Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") reduces
to ([20](#S1.E20 "In Corollary 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")): in this case, BB is a single column vector corresponding to β\beta in the single index model, and Ω\Omega is a scalar σ2\sigma^{2}. A computation using the Woodbury identity for the inverse of ΣK\Sigma^{K},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ΣK)−1=(ΔK)−1​{I−BK​[1σ2+(BK)⊤​(ΔK)−1​BK]−1​(BK)⊤​(ΔK)−1},\displaystyle(\Sigma^{K})^{-1}=(\Delta^{K})^{-1}\{I-B^{K}\left[\frac{1}{\sigma^{2}}+(B^{K})^{\top}(\Delta^{K})^{-1}B^{K}\right]^{-1}(B^{K})^{\top}(\Delta^{K})^{-1}\}, |  | (31) |

shows that the scalar hK=σ2​(BK)⊤​(ΣK)−1​𝟏kh^{K}=\sigma^{2}(B^{K})^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{k} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | hK=∑j∈KBjδj21σ2+∑j∈KBj2δj2h^{K}=\frac{\sum\_{j\in K}\frac{B\_{j}}{\delta\_{j}^{2}}}{\frac{1}{\sigma^{2}}+\sum\_{j\in K}\frac{B\_{j}^{2}}{\delta\_{j}^{2}}} |  | (32) |

and the condition Bi​hK<1B\_{i}h^{K}<1 is equivalent to ([20](#S1.E20 "In Corollary 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")).

## 2  Numerical Examples

### 2.1  Single factor exposure estimation

Given observed excess returns of pp assets over nn observation periods, we may form the p×np\times n data matrix YY and the resulting sample covariance matrix S=1n​Y​Y⊤S=\frac{1}{n}YY^{\top}.

In the likely event that p>np>n, the matrix SS will be rank deficient, so we need a model for estimating an invertible covariance matrix for use in portfolio optimization.

A standard approach is to use factor models to accomplish this. In this section we consider a one-factor model of returns,

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=β​f+ϵr=\beta f+\epsilon |  | (33) |

where β\beta is an unknown vector of factor exposures, ff is a random variable with mean zero and variance σ2\sigma^{2} representing the factor return, and ϵ\epsilon is a random vector whose entries are mutually independent and independent of ff, with mean zero and covariance Δ\Delta. The columns of YY are then assumed to be nn independent realizations of rr. The covariance matrix of rr is given by
([10](#S1.E10 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")):

|  |  |  |
| --- | --- | --- |
|  | Σ=σ2​β​β⊤+Δ.\Sigma=\sigma^{2}\beta\beta^{\top}+\Delta. |  |

Setting ζ2=|β|2​σ2\zeta^{2}=|\beta|^{2}\sigma^{2} and b=β/|β|b=\beta/|\beta|, the one-factor covariance model may be written

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=ζ2​b​b⊤+Δ,\Sigma=\zeta^{2}bb^{\top}+\Delta, |  | (34) |

where recall Δ=d​i​a​g​(δ12,…,δp2)\Delta=diag(\delta\_{1}^{2},\dots,\delta\_{p}^{2}).
Only YY and the corresponding sample covariance matrix SS are observed. Estimating Σ\Sigma requires estimating the scalar ζ2\zeta^{2}, the unit vector bb, and the vector (δ12,…,δp2)(\delta\_{1}^{2},\dots,\delta\_{p}^{2}) of idiosyncratic variances.

For the purpose of computing a minimum variance portfolio, we will consider three different data-driven estimators of ([34](#S2.E34 "In 2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio")): ΣJSE,ΣMJSE\Sigma^{\rm JSE},\Sigma^{\rm MJSE}, and ΣMS\Sigma^{\rm MS}, defined as follows.

The estimator ΣJSE\Sigma^{\rm JSE} is a Bayesian-style James-Stein shrinkage estimator
with the advantage that the shrinkage takes place entirely inside the class of single-factor models:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣJSE=η2​hJSE​(hJSE)⊤+ΔJSE,\Sigma^{\rm JSE}=\eta^{2}h^{\rm JSE}(h^{\rm JSE})^{\top}+\Delta^{\rm JSE}, |  | (35) |

where η2,hJSE,ΔJSE\eta^{2},h^{\rm JSE},\Delta^{\rm JSE} are estimators of ζ2,b,Δ\zeta^{2},b,\Delta described further in Section [4](#S4 "4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio").
The JSE estimators are designed for large p>>np>>n and correct for high-dimensional statistical bias in the sample eigenvectors. Suitable parameters are p=1000p=1000, n=126n=126 as in the empirical illustrations in the next section.
This is a single-factor model where the normalized factor loadings hJSEh^{\rm JSE} are asymptotically good estimates of the unknown population factor exposure unit vector b=β/|β|b=\beta/|\beta| responsible for generating the observed returns via ([33](#S2.E33 "In 2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio")).

The remaining two estimators ΣMJSE,ΣMS\Sigma^{\rm MJSE},\Sigma^{\rm MS} are single-index market models in the manner of Sharpe [[1963](#bib.bib5 "A simplified model for portfolio analysis")] and as used by Clarke et al. [[2011](#bib.bib13 "Minimum-variance portfolio composition")].

Given any data-driven estimator Σ^\hat{\Sigma} of Σ\Sigma, and cap-weighted market portfolio wMw\_{M}, we may define the estimated market variance and market beta by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σM2=wM⊤​Σ^​wM\sigma\_{M}^{2}=w\_{M}^{\top}\hat{\Sigma}w\_{M} |  | (36) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | βM=Σ^​wMσM2.\beta^{M}=\frac{\hat{\Sigma}w\_{M}}{\sigma\_{M}^{2}}. |  | (37) |

From these, we form a single index market covariance matrix ΣM,Σ^\Sigma^{M,{\hat{\Sigma}}} depending on wMw\_{M} and Σ^\hat{\Sigma}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣM,Σ^=σM2​βM​(βM)⊤+ΔM,\Sigma^{M,{\hat{\Sigma}}}=\sigma\_{M}^{2}\beta^{M}(\beta^{M})^{\top}+\Delta^{M}, |  | (38) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔM=d​i​a​g​((δiM)2),(δiM)2=Si​i−(βiM)2​σM2,\Delta^{M}=diag((\delta^{M}\_{i})^{2}),\quad(\delta^{M}\_{i})^{2}=S\_{ii}-(\beta^{M}\_{i})^{2}\sigma\_{M}^{2}, |  | (39) |

or, equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣM,Σ^=ζM2​bM​(bM)⊤+ΔM\Sigma^{M,{\hat{\Sigma}}}=\zeta\_{M}^{2}b^{M}(b^{M})^{\top}+\Delta^{M} |  | (40) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζM2=σM2​|βM|2,bM=βM/|βM|.\zeta\_{M}^{2}=\sigma\_{M}^{2}|\beta^{M}|^{2},\quad b^{M}=\beta^{M}/|\beta^{M}|. |  | (41) |

We examine the choices Σ^=ΣJSE\hat{\Sigma}=\Sigma^{\rm JSE} and Σ^=S\hat{\Sigma}=S, and define

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ΣMJSE\displaystyle\Sigma^{\rm MJSE} | =\displaystyle= | ΣM,ΣJSE\displaystyle\Sigma^{M,{\Sigma^{\rm JSE}}} |  | (42) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ΣMS\displaystyle\Sigma^{\rm MS} | =\displaystyle= | ΣM,S.\displaystyle\Sigma^{M,S}. |  | (43) |

It can be shown that ΣMJSE\Sigma^{\rm MJSE} and ΣJSE\Sigma^{\rm JSE} as asymptotically consistent (as p→∞p\to\infty) in a sense described in Section [4.2](#S4.SS2 "4.2 Consistency of single index estimators ‣ 4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio") below.

### 2.2  Empirical example for a single index model

In this section we apply our results in an empirical illustration using daily returns of the top p=1000p=1000 US stocks by market capitalization for the period January 3, 2022 to July 1, 2022.444Returns were gathered from the CRSP database via the Wharton Research Data Service, then cleaned and centered before use. We removed one smaller stock of a firm with artificially low volatility due to an imminent merger, and added the next largest asset to keep the total at 1,000.

From the market capitalizations m​c​(i),i=1,…,pmc(i),i=1,\dots,p, at the beginning of the period, we determine the market portfolio wMw\_{M} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | wM​(i)=m​c​(i)∑i=1pm​c​(i).w\_{M}(i)=\frac{mc(i)}{\sum\_{i=1}^{p}mc(i)}. |  | (44) |

We then use the formulas of section [2.1](#S2.SS1 "2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") to determine three choices555Clarke et al. [[2011](#bib.bib13 "Minimum-variance portfolio composition")] use a different choice of single-index market covariance matrix by taking Σ^\hat{\Sigma} to be a Ledoit-Wolf shrinkage estimator, see Ledoit and Wolf [[2004](#bib.bib14 "Honey, I shrunk the covariance matrix")]. The empirical outcomes are similar to the ones reported here.
of the data-driven covariance estimator for computing the LOMV portfolio: ΣJSE\Sigma^{\rm JSE}, ΣMJSE\Sigma^{\rm MJSE}, and
ΣMS\Sigma^{\rm MS}.

The outcomes for the resulting long only portfolio size, market factor variance, and estimated betas are summarized in Table 1.
For ΣJSE=η2​hJSE​hJSE⊤+ΔJSE\Sigma^{\rm JSE}=\eta^{2}h^{\rm JSE}{h^{\rm JSE}}^{\top}+\Delta^{\rm JSE}, the market quantities σM2\sigma\_{M}^{2} and βM\beta^{M} are undefined and hJSEh^{\rm JSE} is scaled as a unit vector by convention.

| estimator | kk | σM2\sigma^{2}\_{M}(%) | mean(βM)(\beta^{M}) |
| --- | --- | --- | --- |
| ΣMJSE\Sigma^{\rm MJSE} | 65 | 5.8 | 1.08 |
| ΣMS\Sigma^{\rm MS} | 51 | 6.2 | 1.13 |
| ΣJSE\Sigma^{\rm JSE} | 66 | \* | \* |

Table 1: Outcomes for each of three choices of covariance estimator. The value kk is the number of active assets in the long-only minimum variance portfolio (out of 1000). σM2\sigma^{2}\_{M} and βM\beta^{M} are the derived parameters according to equations ([36](#S2.E36 "In 2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio")) and ([37](#S2.E37 "In 2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio")) but does not apply to the last row.

Table 2 shows that the three methods mostly agree on which active assets should be included in the long-only minimum variance portfolio.

| portfolio | MJSE | MS | JSE | MJSE ∩\cap MS | MJSE ∩\cap JSE | JSE ∩\cap MS |
| --- | --- | --- | --- | --- | --- | --- |
| # assets | 65 | 51 | 66 | 49 | 65 | 49 |

Table 2: The number of assets that each of the three estimated minimum variance portfolios have in common, out of 1000 total assets considered.

Figures [1(a)](#S2.F1.sf1 "In Figure 1 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") and [1(b)](#S2.F1.sf2 "In Figure 1 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") show scatterplots demonstrating that the portfolios for the market model ΣMJSE\Sigma^{\rm MJSE} and the statistical factor model ΣJSE\Sigma^{\rm JSE} are almost the same in this experiment, but the ΣMS\Sigma^{\rm MS} portfolio noticeably differs.

![Refer to caption](2603.07692v1/mandjse.png)


(a) Weights of MJSE vs JSE portfolios.

![Refer to caption](2603.07692v1/sj.png)


(b) Weights of MS vs MJSE portfolios.

Figure 1: Comparison of portfolio asset weights for the three portfolios MJSE, JSE, and MS, plotted in percent.

Figures [2](#S2.F2 "Figure 2 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"), [3](#S2.F3 "Figure 3 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"), and [4](#S2.F4 "Figure 4 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") below illustrate the relationships between estimated market beta, portfolio weight, and idiosyncratic risk for the MSJE portfolio. (Plots look similar for the other portfolios.)

The betas range between −0.05-0.05 and 3.623.62 with the only negative beta being approximately −0.059-0.059. The maximum beta in the long-only portfolio is 0.281. The idiosyncratic risk ranges from 0 to 46%46\%.
Figures [2](#S2.F2 "Figure 2 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") and [3](#S2.F3 "Figure 3 ‣ 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") show the 1000 individual asset weights under the single-factor model for both the long-short (blue dots) and the long-only (black dots) minimum-variance portfolio plotted against market beta and delta. The weights of the active assets in the long-only portfolio had a maximum value of 5.81%5.81\%.

Of interest is the fact that only 65 of the 1000 securities were active in the long-only portfolio.
In addition to having lower beta, assets with low idiosyncratic risk are more likely to be active in the long-only portfolio. We also see that assets with lower idiosyncratic risk tend to have higher absolute value weights in the long-short portfolio.

![Refer to caption](2603.07692v1/jj6.png)


Figure 2: MJSE portfolio weights against market beta for the top 1000 US stocks, estimated for daily returns in the first half of 2022.

![Refer to caption](2603.07692v1/jj7.png)


Figure 3: MJSE portfolio weights against specific risk for the top 1000 US stocks, from daily returns in the first half of 2022.

![Refer to caption](2603.07692v1/jj5.png)


Figure 4: MJSE market beta against specific risk for the top 1000 US stocks in the first half of 2022.

### 2.3  Empirical example for a two-factor model

To illustrate the hyperplane separation of factor loadings described in Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"), we fit a two-factor model (q=2q=2) to the same daily returns of the 1,000 stocks used in Section [2.2](#S2.SS2 "2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"). Starting from
the leading two eigenvalue-eigenvector pairs of the sample covariance matrix,
as described further in Section [5](#S5 "5 Multifactor JSM estimation ‣ Understanding the Long-Only Minimum Variance Portfolio"), we apply the James-Stein-Markowitz (JSM) multifactor shrinkage method of Shkolnik et al. [[2024](#bib.bib15 "Portfolio selection revisited")] to obtain the covariance estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣJSM=B​Ω​B⊤+Δ,\Sigma^{\rm JSM}=B\Omega B^{\top}+\Delta, |  | (45) |

where BB is a 2×p2\times p matrix with orthogonal columns, obtained via shrinkage from the leading two sample eigenvectors; Δ\Delta is a diagonal matrix of specific variances; and Ω\Omega is a 2×22\times 2 diagonal matrix. The row BiB\_{i} of asset ii is that asset’s exposure vector to the two factors. The resulting long-only minimum variance portfolio is computed by means of the open source convex optimization package cvxpy (www.cvxpy.org).

The results are displayed in the left hand plot of Figure [5](#S2.F5 "Figure 5 ‣ 2.3 Empirical example for a two-factor model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") below, in which the horizontal axis shows the exposure to the leading (market) factor (the first component of BiB\_{i}), and the vertical axis to the second factor. Orange indicates assets included in the LOMV portfolio based on the model, and blue indicates excluded assets. The solid red line is the hyperplane of Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio") separating the active and inactive assets in the LOMV portfolio, while the dotted red line indicates the single-index model threshold value that would apply for the same data with a one-factor model. We observe a relatively small number of assets in the LOMV portfolio.

The right-hand plot in Figure [5](#S2.F5 "Figure 5 ‣ 2.3 Empirical example for a two-factor model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") shows a close-up of the LOMV portfolio’s active assets with the portfolio weights coded as marker size and color. The largest weight is 10%. The portfolio weight of an asset is proportional666With a proportionality constant that is the same for all assets. This follows from a computation using the Woodbury identity.
to the ratio di/δi2d\_{i}/\delta\_{i}^{2}, where δi2\delta\_{i}^{2} is the specific variance of asset ii, and did\_{i} is the perpendicular distance from the asset’s beta point BiB\_{i} to the separating hyperplane. Although the active asset portfolio weights shown in Figure [5](#S2.F5 "Figure 5 ‣ 2.3 Empirical example for a two-factor model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio") generally vary inversely with the distance from the separating hyperplane, unusually large or small specific variances can play a dominant role, as is the case for three assets with large exposure to the second factor.

![Refer to caption](2603.07692v1/betas2_1000jsm.png)


Figure 5: 2-vector exposures for each asset from a statistical 2-factor JSM return covariance matrix, plotted for each of the 1000 assets. On the right is a close-up showing portfolio weights.

An interesting comparison with the portfolio resulting from a single-index model is evident by examining the vertical dotted red line in the left-hand plot, which, as stated above, is the one-factor threshold for the same returns data. The 1-factor portfolio excludes a few of the assets with higher exposure to both factors and includes significantly more with negative exposure to the second factor. For the two-factor model portfolio, exposure to the second factor can compensate for a fairly significant positive exposure to the first factor, such as for the two uppermost orange assets in left-hand plot. These assets are significantly into the excluded region defined by the dotted line. Overall, the 2-factor model includes 41 assets, 24 fewer than the 65 assets of one-factor model.

The angle between the two lines could be considered a measure of the importance of the second factor in determining active long-only assets. The angle here is 21.5% of a right angle, which is relatively significant.

## 3  Proofs

### 3.1  Proof of Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")

Notation: 𝟏p\mathbf{1}\_{p} is the pp-dimensional vectors of all ones, and similarly 𝟎p\mathbf{0}\_{p} for all zeros.

The solution w=wLw=w^{L} of our constrained optimization problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) satisfies the well-known Karush-Kuhn-Tucker (KKT) conditions777See, for example, Boyd and Vandenberghe [[2004](#bib.bib4 "Convex optimization")] or Beck [[2023](#bib.bib12 "Introduction to nonlinear optimization: theory, algorithms, and applications with python and matlab")]., which are a set of equations in ww, an auxiliary pp-vector λ{\lambda}, and an auxiliary scalar ν\nu (the Lagrange multipliers) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​Σ​w−λ+ν​𝟏p=𝟎p\displaystyle 2\Sigma w-{\lambda}+\nu\mathbf{1}\_{p}=\mathbf{0}\_{p} |  | (46) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | w⊤​𝟏p=1\displaystyle w^{\top}\mathbf{1}\_{p}=1 |  | (47) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λi​wi=0​ ​i=1,2,…,p\displaystyle\lambda\_{i}w\_{i}=0\text{ }i=1,2,...,p |  | (48) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λi≥0,wi≥0​ ​i=1,2,…,p.\displaystyle\lambda\_{i}\geq 0,w\_{i}\geq 0\text{ }i=1,2,...,p. |  | (49) |

These KKT conditions include 2​p+12p+1 equations ([46](#S3.E46 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) – ([48](#S3.E48 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) in the 2​p+12p+1 unknowns

|  |  |  |
| --- | --- | --- |
|  | w1,…,wp,λ1,…,λp,ν,w\_{1},\dots,w\_{p},\lambda\_{1},\dots,\lambda\_{p},\nu, |  |

along
with 2​p2p inequality constraints ([49](#S3.E49 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")).

Define the (necessarily non-empty) set

|  |  |  |  |
| --- | --- | --- | --- |
|  | K={i≤p:wi>0}.K=\{i\leq p:w\_{i}>0\}. |  | (50) |

Let k>0k>0 denote the cardinality of KK. For any vector x∈𝐑px\in\mathbf{R}^{p}, denote by xK∈𝐑kx^{K}\in\mathbf{R}^{k} the kk-dimensional vector obtained from xx by deleting the entries xjx\_{j} for all j∉Kj\notin K.
Likewise, for any p×pp\times p matrix MM, denote by MKM^{K} the k×kk\times k principal submatrix obtained from MM by deleting all the rows and columns with indices outside KK.

Since Σ\Sigma is symmetric positive definite, so is the submatrix ΣK\Sigma^{K}, and hence ΣK\Sigma^{K} is invertible.
Further,

|  |  |  |  |
| --- | --- | --- | --- |
|  | w⊤​Σ​w=(wK)⊤​ΣK​wK.w^{\top}\Sigma w=(w^{K})^{\top}\Sigma^{K}w^{K}. |  | (51) |

Since λi=0\lambda\_{i}=0 for all i∈Ki\in K, taking the kk rows of equation ([46](#S3.E46 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) corresponding to indices in KK tells us

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​ΣK​wK+ν​𝟏k=𝟎k,2\Sigma^{K}w^{K}+\nu\mathbf{1}\_{k}=\mathbf{0}\_{k}, |  | (52) |

where here the vectors 𝟏k\mathbf{1}\_{k} and 𝟎k\mathbf{0}\_{k} are kk-dimensional. Multiplying ([52](#S3.E52 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) on the left by 𝟏k⊤​(ΣK)−1\mathbf{1}\_{k}^{\top}(\Sigma^{K})^{-1} and using 𝟏k⊤​wK=1\mathbf{1}\_{k}^{\top}w^{K}=1, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν=−2𝟏k⊤​(ΣK)−1​𝟏k\nu=\frac{-2}{\mathbf{1}\_{k}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{k}} |  | (53) |

and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | wK=(ΣK)−1​𝟏k𝟏k⊤​(ΣK)−1​𝟏k,w^{K}=\frac{(\Sigma^{K})^{-1}\mathbf{1}\_{k}}{\mathbf{1}\_{k}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{k}}, |  | (54) |

or, equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | wL=(ΣK,0)+​𝟏p𝟏p⊤​(ΣK,0)+​𝟏p.w^{L}=\frac{(\Sigma^{K,0})^{+}\mathbf{1}\_{p}}{\mathbf{1}\_{p}^{\top}(\Sigma^{K,0})^{+}\mathbf{1}\_{p}}. |  | (55) |

### 3.2  Proof of Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")

Part 1 of the theorem follows solely from the monotonicity of the sequence {βi}\{\beta\_{i}\}.
For convenience, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci=∑j=1iβjδj2.C\_{i}=\sum\_{j=1}^{i}\frac{\beta\_{j}}{\delta\_{j}^{2}}. |  | (56) |

It is easy to verify, for all i=1,…,p−1i=1,\dots,p-1, that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri+1−Ri=(−βi+1+βi)​Ci.R\_{i+1}-R\_{i}=(-\beta\_{i+1}+\beta\_{i})C\_{i}. |  | (57) |

Since (−βi+1+βi)(-\beta\_{i+1}+\beta\_{i}) is always non-positive, Ri+1−Ri≤0R\_{i+1}-R\_{i}\leq 0 when Ci≥0C\_{i}\geq 0 and Ri+1−Ri≥0R\_{i+1}-R\_{i}\geq 0 when Ci≤0C\_{i}\leq 0.

Let s=min⁡{i:Ci>0}s=\min\{i:C\_{i}>0\}, 1≤s≤p1\leq s\leq p.
If j<sj<s, then Cj≤0C\_{j}\leq 0 by definition of ss, so Rj+1−Rj≥0R\_{j+1}-R\_{j}\geq 0. Since βs>0\beta\_{s}>0, CiC\_{i} is increasing for i≥si\geq s, so if j≥sj\geq s then Cj>0C\_{j}>0, and we have Rj+1−Rj≤0R\_{j+1}-R\_{j}\leq 0. This establishes the conclusion of part 1.

We proceed to Part 2.
Our goal now is to determine K={i≤p:wiL>0}K=\{i\leq p:w^{L}\_{i}>0\} in explicit form in term of the parameters σ,β,δ\sigma,\beta,\delta of the problem.

Let k=|K|k=|K| and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ=max⁡{i≤p:Ri>0}.\ell=\max\{i\leq p:R\_{i}>0\}. |  | (58) |

We will complete the proof by establishing

|  |  |  |
| --- | --- | --- |
|  | k=ℓ​ and ​K={1,2,…,k}.k=\ell\mbox{ and }K=\{1,2,\dots,k\}. |  |

Let βK∈𝐑k\beta^{K}\in\mathbf{R}^{k} and the k×kk\times k matrix ΣK\Sigma^{K} be determined from KK as before, obtained from β\beta and Σ\Sigma by deleting rows or rows and columns corresponding to indices outside KK.

By the Woodbury identity,

|  |  |  |
| --- | --- | --- |
|  | (ΣK)−1=d​i​a​g​(1(δK)2)−(βK(δK)2)​(βK(δK)2)⊤1σ2+(βK(δK)2)⊤​βK(\Sigma^{K})^{-1}=diag(\frac{1}{(\delta^{K})^{2}})-\frac{(\frac{\beta^{K}}{(\delta^{K})^{2}})(\frac{\beta^{K}}{(\delta^{K})^{2}})^{\top}}{\frac{1}{\sigma^{2}}+(\frac{\beta^{K}}{(\delta^{K})^{2}})^{\top}\beta^{K}} |  |

where 1(δK)2=[1δj2:j∈K]⊤\frac{1}{({\delta^{K}})^{2}}=[\frac{1}{\delta\_{j}^{2}}:j\in K]^{\top} and
βK(δK)2=[βjδj2:j∈K]⊤\frac{\beta^{K}}{(\delta^{K})^{2}}=[\frac{\beta\_{j}}{\delta\_{j}^{2}}:j\in K]^{\top}.

This means

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ΣK)−1​𝟏k=1(δK)2−(βK(δK)2)​(βK(δK)2)⊤​𝟏k1σ2+(βK(δK)2)⊤​βK.(\Sigma^{K})^{-1}\mathbf{1}\_{k}=\frac{1}{(\delta^{K})^{2}}-\frac{(\frac{\beta^{K}}{(\delta^{K})^{2}})(\frac{\beta^{K}}{(\delta^{K})^{2}})^{\top}\mathbf{1}\_{k}}{\frac{1}{\sigma^{2}}+(\frac{\beta^{K}}{(\delta^{K})^{2}})^{\top}\beta^{K}}. |  | (59) |

Now if i∈Ki\in K, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ((ΣK)−1​𝟏k)i=1δi2−βiδi2​∑j∈Kβjδj21σ2+∑j∈Kβj2δj2>0.((\Sigma^{K})^{-1}\mathbf{1}\_{k})\_{i}=\frac{1}{\delta\_{i}^{2}}-\frac{\frac{\beta\_{i}}{\delta\_{i}^{2}}\sum\_{j\in K}\frac{\beta\_{j}}{\delta\_{j}^{2}}}{\frac{1}{\sigma^{2}}+\sum\_{j\in K}\frac{\beta^{2}\_{j}}{\delta\_{j}^{2}}}>0. |  | (60) |

Clearing the positive denominators, we
obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1σ2+∑j∈Kβj2δj2−βi​∑j∈Kβjδj2>0\frac{1}{\sigma^{2}}+\sum\_{j\in K}\frac{\beta^{2}\_{j}}{\delta\_{j}^{2}}-\beta\_{i}\sum\_{j\in K}\frac{\beta\_{j}}{\delta\_{j}^{2}}>0 |  | (61) |

or

|  |  |  |  |
| --- | --- | --- | --- |
|  | BK>βi​CKB\_{K}>\beta\_{i}C\_{K} |  | (62) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | BK=1σ2+∑j∈Kβj2δj2,CK=∑j∈Kβjδj2.B\_{K}=\frac{1}{\sigma^{2}}+\sum\_{j\in K}\frac{\beta^{2}\_{j}}{\delta\_{j}^{2}},\quad C\_{K}=\sum\_{j\in K}\frac{\beta\_{j}}{\delta\_{j}^{2}}. |  | (63) |

Now suppose instead i∉Ki\notin K, so wi=0w\_{i}=0.
Since Σ​w=σ2​β​β⊤​w+d​i​a​g​(δ2)​w\Sigma w=\sigma^{2}\beta\beta^{\top}w+diag(\delta^{2})w and wj=0w\_{j}=0 for all j∉Kj\notin K,
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Σ​w)i=σ2​βi​∑j∈Kβj​wj.(\Sigma w)\_{i}=\sigma^{2}\beta\_{i}\sum\_{j\in K}\beta\_{j}w\_{j}. |  | (64) |

Conditions ([46](#S3.E46 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) and ([49](#S3.E49 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) tell us

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤λi=2​(Σ​w)i+ν,0\leq\lambda\_{i}=2(\Sigma w)\_{i}+\nu, |  | (65) |

or, using ([64](#S3.E64 "In 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤2​σ2​βi​∑j∈Kβj​wj+ν.0\leq 2\sigma^{2}\beta\_{i}\sum\_{j\in K}\beta\_{j}w\_{j}+\nu. |  | (66) |

For j∈Kj\in K, we have, from ([54](#S3.E54 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | wj=((ΣK)−1​𝟏k)j𝟏k​(ΣK)−1​𝟏k.w\_{j}=\frac{((\Sigma^{K})^{-1}\mathbf{1}\_{k})\_{j}}{\mathbf{1}\_{k}(\Sigma^{K})^{-1}\mathbf{1}\_{k}}. |  | (67) |

Using this, substituting for ν\nu with ([53](#S3.E53 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")), and multiplying through by 𝟏k​(ΣK)−1​𝟏k/2\mathbf{1}\_{k}(\Sigma^{K})^{-1}\mathbf{1}\_{k}/2 gives us

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤σ2​βi​∑j∈Kβj​((ΣK)−1​𝟏k)j−1.0\leq\sigma^{2}\beta\_{i}\sum\_{j\in K}\beta\_{j}((\Sigma^{K})^{-1}\mathbf{1}\_{k})\_{j}-1. |  | (68) |

By ([60](#S3.E60 "In 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ((ΣK)−1​𝟏k)j=1δj2−βjδj2​CKBK.((\Sigma^{K})^{-1}\mathbf{1}\_{k})\_{j}=\frac{1}{\delta\_{j}^{2}}-\frac{\beta\_{j}}{\delta\_{j}^{2}}\frac{C\_{K}}{B\_{K}}. |  | (69) |

Using this in the previous inequality, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≤\displaystyle\leq | σ2​βi​∑j∈Kβjδj2​(1−βj​CKBK)−1\displaystyle\sigma^{2}\beta\_{i}\sum\_{j\in K}\frac{\beta\_{j}}{\delta\_{j}^{2}}(1-\frac{\beta\_{j}C\_{K}}{B\_{K}})-1 |  | (70) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | =\displaystyle= | σ2​βi​(CK−CKBK​(BK−1σ2))−1\displaystyle\sigma^{2}\beta\_{i}\big(C\_{K}-\frac{C\_{K}}{B\_{K}}(B\_{K}-\frac{1}{\sigma^{2}})\big)-1 |  | (71) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | =\displaystyle= | σ2​βi​CKσ2​BK−1=βi​CKBK−1,\displaystyle\sigma^{2}\beta\_{i}\frac{C\_{K}}{\sigma^{2}B\_{K}}-1=\beta\_{i}\frac{C\_{K}}{B\_{K}}-1, |  | (72) |

or

|  |  |  |  |
| --- | --- | --- | --- |
|  | BK≤βi​CK.B\_{K}\leq\beta\_{i}C\_{K}. |  | (73) |

Combining ([62](#S3.E62 "In 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) and ([73](#S3.E73 "In 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")), we have established the following

###### Lemma 1.

With BKB\_{K} and CKC\_{K} as defined above,
i∈Ki\in K if and only if BK>βi​CKB\_{K}>\beta\_{i}C\_{K}.

###### Corollary 3.

CK≠0C\_{K}\neq 0.

Proof of Corollary.
If k=p{k}=p, then CK≠0C\_{K}\neq 0 is our standing assumption. Otherwise there exists j∉Kj\notin K, so by Lemma [1](#Thmlemma1 "Lemma 1. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio") BK≤βj​CKB\_{K}\leq\beta\_{j}C\_{K}.
But BK>0B\_{K}>0, so again CKC\_{K} cannot be zero.
∎

###### Lemma 2.

Recall k{k} is the cardinality of KK.
If CK>0C\_{K}>0, then K={1,2,…,k}K=\{1,2,\dots,{k}\}. If CK<0C\_{K}<0, then K={p−k+1,…,p}K=\{p-{k}+1,\dots,p\}.

Proof of lemma. Recall that the βi\beta\_{i} are arranged in increasing order. For all i∈Ki\in K and j∉Kj\notin K, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | βi​CK<BK≤βj​CK,\beta\_{i}C\_{K}<B\_{K}\leq\beta\_{j}C\_{K}, |  | (74) |

hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | βi​CK<βj​CK.\beta\_{i}C\_{K}<\beta\_{j}C\_{K}. |  | (75) |

If CK>0C\_{K}>0, this means that βi<βj\beta\_{i}<\beta\_{j} for all i∈K,j∉Ki\in K,j\notin K, and hence
i<ji<j for all i∈K,j∉Ki\in K,j\notin K. Therefore KK must be an initial segment of the sequence {1,2,…,p}\{1,2,\dots,p\}.

Similarly, if CK<0C\_{K}<0, then the reverse inequality is true, and KK must be a terminal segment of {1,2,…,p}\{1,2,\dots,p\}. ∎

Next, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | CP=∑j=1pβjδj2,C\_{P}=\sum\_{j=1}^{p}\frac{\beta\_{j}}{\delta\_{j}^{2}}, |  | (76) |

and recall CP>0C\_{P}>0 by our standing assumption.

###### Lemma 3.

CK>0C\_{K}>0.

Proof. If k=p{k}=p then CK=CPC\_{K}=C\_{P} and there is nothing to prove, so consider the case k<p{k}<p. We know that CK≠0C\_{K}\neq 0. Suppose for
contradiction that CK<0C\_{K}<0. By Lemma [2](#Thmlemma2 "Lemma 2. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio"),
this means that K={p−k+1,…,p}K=\{p-{k}+1,\dots,p\}.

Note

|  |  |  |  |
| --- | --- | --- | --- |
|  | CP=∑j=1p−kβjδj2+CK.C\_{P}=\sum\_{j=1}^{p-{k}}\frac{\beta\_{j}}{\delta\_{j}^{2}}+C\_{K}. |  | (77) |

Now 0>CK=∑j=p−k+1pβjδj20>C\_{K}=\sum\_{j=p-{k}+1}^{p}\frac{\beta\_{j}}{\delta\_{j}^{2}}, so at least one of the terms of this sum must be negative. Then, since the beta sequence is increasing, βp−k+1<0\beta\_{p-{k}+1}<0 and βj<0\beta\_{j}<0 for all j≤p−kj\leq p-{k}, and hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1p−kβjδj2<0.\sum\_{j=1}^{p-{k}}\frac{\beta\_{j}}{\delta\_{j}^{2}}<0. |  | (78) |

This forces CP<0C\_{P}<0 via ([77](#S3.E77 "In 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")), a contradiction. Hence we must have CK>0C\_{K}>0 and CK=∑j=1kβjδj2C\_{K}=\sum\_{j=1}^{k}\frac{\beta\_{j}}{\delta\_{j}^{2}}.

∎

###### Lemma 4.

Under our standing assumption, for the long-only solution ww of problem ([2](#S1.E2 "In 1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi>0​ if and only if ​βi<BKCK=1σ2+∑j=1kβj2δj2∑j=1kβjδj2.w\_{i}>0\mbox{ if and only if }\beta\_{i}<\frac{B\_{K}}{C\_{K}}=\frac{\frac{1}{\sigma^{2}}+\sum\_{j=1}^{k}\frac{\beta^{2}\_{j}}{\delta\_{j}^{2}}}{\sum\_{j=1}^{k}\frac{\beta\_{j}}{\delta\_{j}^{2}}}. |  | (79) |

Proof. From Lemma [3](#Thmlemma3 "Lemma 3. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio"), CK>0C\_{K}>0.
By Lemma [2](#Thmlemma2 "Lemma 2. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio"), K={1,2,…,k}K=\{1,2,\dots,{k}\}.
The result follows from Lemma [1](#Thmlemma1 "Lemma 1. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio").
∎

By Lemmas [2](#Thmlemma2 "Lemma 2. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio") and [3](#Thmlemma3 "Lemma 3. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio"), we have established that

|  |  |  |  |
| --- | --- | --- | --- |
|  | K={1,2,…,k}.K=\{1,2,\dots,{k}\}. |  | (80) |

It remains to show that k=ℓ{k}=\ell.
Recall R1=1/σ2R\_{1}=1/\sigma^{2} and, for i=2,…,pi=2,\dots,p,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri=1σ2+∑j=1i−1βjδj2​(βj−βi).R\_{i}={\frac{1}{\sigma^{2}}+\sum\_{j=1}^{i-1}\frac{\beta\_{j}}{\delta\_{j}^{2}}(\beta\_{j}-\beta\_{i})}. |  | (81) |

Now, by Lemma [4](#Thmlemma4 "Lemma 4. ‣ 3.2 Proof of Theorem 2 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio"), βk<BK/CK≤βk+1\beta\_{k}<B\_{K}/C\_{K}\leq\beta\_{{k}+1}.
Also,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Rk\displaystyle R\_{{k}} | =\displaystyle= | 1σ2+∑j=1kβj2δj2−βk​∑j=1kβjδj2\displaystyle{\frac{1}{\sigma^{2}}+\sum\_{j=1}^{{k}}\frac{\beta\_{j}^{2}}{\delta\_{j}^{2}}-\beta\_{{k}}\sum\_{j=1}^{{k}}\frac{\beta\_{j}}{\delta\_{j}^{2}}} |  | (82) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | =\displaystyle= | BK−βk​CK>0.\displaystyle B\_{K}-\beta\_{{k}}C\_{K}>0. |  | (83) |

Likewise

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rk+1=BK−βk+1​CK≤0.\displaystyle R\_{{k}+1}=B\_{K}-\beta\_{{k}+1}C\_{K}\leq 0. |  | (84) |

By part 1 of the Theorem, the sequence {Ri}\{R\_{i}\} crosses zero at most once, so this establishes

|  |  |  |  |
| --- | --- | --- | --- |
|  | k=max⁡{i≤p:Ri>0}=ℓ,{k}=\max\{i\leq p:R\_{i}>0\}=\ell, |  | (85) |

completing the proof of Part 2.
∎

### 3.3  Proof of Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")

Let w=wLw=w^{L} be the solution of the long-only problem for

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=B​Ω​B⊤+Δ,\Sigma=B\Omega B^{\top}+\Delta, |  | (86) |

and K={i≤p:wiL>0}K=\{i\leq p:w^{L}\_{i}>0\},
with ℓ=|K|\ell=|K|.
For any pp-vector vv, for purposes of this proof we adopt the notation that vKv^{K} as defined before, and v′v^{\prime} is the complementary (p−ℓ)(p-\ell)-vector obtained from vv by deleting all the coordinates in KK; B′B^{\prime} is obtained by deleting all the rows labeled by entries in KK, and BKB^{K} by deleting the rows not in KK.

First recall that i∉Ki\notin K implies wi=0w\_{i}=0, and hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Σ​w)′=((B​Ω​B⊤+Δ)​w)′=(B​Ω​B⊤​w)′=B′​Ω​(BK)⊤​wK.\displaystyle(\Sigma w)^{\prime}=\left((B\Omega B^{\top}+\Delta)w\right)^{\prime}=(B\Omega B^{\top}w)^{\prime}=B^{\prime}\Omega(B^{K})^{\top}w^{K}. |  | (87) |

Recall equations ([46](#S3.E46 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) and ([49](#S3.E49 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")):

|  |  |  |
| --- | --- | --- |
|  | 2​Σ​w−λ+ν​𝟏p=𝟎p;λi≥0,wi≥0,i=1,…,p.2\Sigma w-\lambda+\nu\mathbf{1}\_{p}=\mathbf{0}\_{p};\quad\lambda\_{i}\geq 0,w\_{i}\geq 0,\,i=1,\dots,p. |  |

Therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟎p−ℓ≤λ′=2​(Σ​w)′+ν​𝟏p−ℓ\mathbf{0}\_{p-\ell}\leq\lambda^{\prime}=2(\Sigma w)^{\prime}+\nu\mathbf{1}\_{p-\ell} |  | (88) |

and hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟎p−ℓ≤2​B′​Ω​(BK)⊤​wK+ν​𝟏p−ℓ\mathbf{0}\_{p-\ell}\leq 2B^{\prime}\Omega(B^{K})^{\top}w^{K}+\nu\mathbf{1}\_{p-\ell} |  | (89) |

using equation ([87](#S3.E87 "In 3.3 Proof of Theorem 3 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")).

Substituting using ([53](#S3.E53 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")) and ([54](#S3.E54 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")), clearing denominators, and dividing by 2, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟎p−ℓ≤B′​Ω​(BK)⊤​(ΣK)−1​𝟏ℓ−𝟏p−ℓ=B′​hK−𝟏p−ℓ\displaystyle\mathbf{0}\_{p-\ell}\leq B^{\prime}\Omega(B^{K})^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{\ell}-\mathbf{1}\_{p-\ell}=B^{\prime}h^{K}-\mathbf{1}\_{p-\ell} |  | (90) |

with

|  |  |  |
| --- | --- | --- |
|  | hK=Ω​(BK)⊤​(ΣK)−1​𝟏ℓh^{K}=\Omega(B^{K})^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{\ell} |  |

as defined in ([26](#S1.E26 "In Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")) of
Theorem [3](#Thmtheorem3 "Theorem 3 (Hyperplane separation for 𝑞-factor models). ‣ 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio").

Thus we have established that for every i∉Ki\notin K,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1≤Bi​hK.1\leq B\_{i}h^{K}. |  | (91) |

Conversely, recall

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣK=BK​Ω​(BK)⊤+ΔK.\Sigma^{K}=B^{K}\Omega(B^{K})^{\top}+\Delta^{K}. |  | (92) |

We therefore have

|  |  |  |  |
| --- | --- | --- | --- |
|  | BK​hK=BK​Ω​(BK)⊤​(ΣK)−1​𝟏ℓ=(ΣK−ΔK)​(ΣK)−1​𝟏ℓ=𝟏ℓ−ΔK​(ΣK)−1​𝟏ℓ.B^{K}h^{K}=B^{K}\Omega(B^{K})^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{\ell}=(\Sigma^{K}-\Delta^{K})(\Sigma^{K})^{-1}\mathbf{1}\_{\ell}=\mathbf{1}\_{\ell}-\Delta^{K}(\Sigma^{K})^{-1}\mathbf{1}\_{\ell}. |  | (93) |

From equation ([54](#S3.E54 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio")),
(ΣK)−1​𝟏ℓ=(𝟏ℓ⊤​(ΣK)−1​𝟏ℓ)​wK(\Sigma^{K})^{-1}\mathbf{1}\_{\ell}=(\mathbf{1}\_{\ell}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{\ell})w^{K}, and hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | BK​hK=𝟏ℓ−(𝟏ℓ⊤​(ΣK)−1​𝟏ℓ)​ΔK​wK<𝟏ℓ,B^{K}h^{K}=\mathbf{1}\_{\ell}-(\mathbf{1}\_{\ell}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{\ell})\Delta^{K}w^{K}<\mathbf{1}\_{\ell}, |  | (94) |

since the entries of
(𝟏ℓ⊤​(ΣK)−1​𝟏ℓ)​ΔK​wK(\mathbf{1}\_{\ell}^{\top}(\Sigma^{K})^{-1}\mathbf{1}\_{\ell})\Delta^{K}w^{K} are all positive.
We conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bi​hK<1B\_{i}h^{K}<1 |  | (95) |

for all i∈Ki\in K.
∎

## 4  Single factor beta estimation

### 4.1  The JSE estimator

Covariance matrix shrinkage estimators, e.g. Ledoit and Wolf [[2004](#bib.bib14 "Honey, I shrunk the covariance matrix")], have enjoyed wide adoption for various problems when estimating large-dimensional covariance matrices from data, and typically take the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=α​S+(1−α)​T,\Sigma=\alpha S+(1-\alpha)T, |  | (96) |

where SS is a sample covariance matrix, TT is a suitable target matrix, such as a scalar matrix, and α∈(0,1)\alpha\in(0,1) is defined to minimize some error function.

However, in cases where we are working within the structure of a factor model, we are primarily interested in estimating the leading covariance eigenvector(s), from which an estimated factor model can be defined. Eigenvector shrinkage is the subject of a recent stream of research in Goldberg et al. [[2020](#bib.bib7 "Better betas")], Goldberg and Kercheval [[2023](#bib.bib8 "James-Stein for the leading eigenvector")], Goldberg et al. [[2022](#bib.bib9 "The dispersion bias"), [2025](#bib.bib11 "Portfolio optimization via strategy-specific eigenvector shrinkage")], Shkolnik [[2022](#bib.bib6 "James-Stein estimation of the first principal component")]. We call it JSE (James-Stein for Eigenvectors) because the shrinkage formulas themselves turn out to be close analogs of the classical James-Stein shrinkage formulas for estimation of multivariate means. The theory provides asymptotic improvements in the HL asymptotic regime corresponding to the limit as the dimension p→∞p\to\infty with the number of samples nn fixed.

In this section we describe how to compute the JSE estimator of the leading eigenvector.

As in Section [2.1](#S2.SS1 "2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"), we consider a single factor model of returns,

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=β​f+ϵ.r=\beta f+\epsilon. |  | (97) |

The covariance matrix of rr is given by
([10](#S1.E10 "In 1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio")):

|  |  |  |
| --- | --- | --- |
|  | Σ=σ2​β​βT+Δ.\Sigma=\sigma^{2}\beta\beta^{T}+\Delta. |  |

Setting ζ2=‖β‖2​σ2\zeta^{2}=||\beta||^{2}\sigma^{2} and b=β/‖β‖b=\beta/||\beta||, the single index model may be written

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=ζ2​b​b⊤+Δ,\Sigma=\zeta^{2}bb^{\top}+\Delta, |  | (98) |

where recall Δ=d​i​a​g​(δ12,…,δp2)\Delta=diag(\delta\_{1}^{2},\dots,\delta\_{p}^{2}).
Estimating Σ\Sigma requires estimating the scalar ζ2\zeta^{2}, the unit vector bb, and the vector (δ12,…,δp2)(\delta\_{1}^{2},\dots,\delta\_{p}^{2}) of idiosyncratic variances.

Suppose we observe a time series of nn returns of each of pp assets, and p>>np>>n as might typically be the case when nn is limited by non-stationarity or data availability. The observations can be summarized by a p×np\times n data matrix YY, and the resulting sample covariance matrix is

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=Y​Y⊤/n.\displaystyle S=YY^{\top}/n. |  | (99) |

Let λ2\lambda^{2} denote the leading eigenvalue of SS, and let

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ2=t​r​(S)−λ2n−1\ell^{2}=\frac{tr(S)-\lambda^{2}}{n-1} |  | (100) |

be the average of the non-zero eigenvalues that are less than λ2\lambda^{2}, where t​r​(S)tr(S) denotes trace. We can think of

|  |  |  |
| --- | --- | --- |
|  | η2=λ2−ℓ2\eta^{2}=\lambda^{2}-\ell^{2} |  |

as the average leading sample eigengap, and it turns out that η2\eta^{2} is an unbiased approximation of ζ2\zeta^{2}.

To approximate the vector b=β/‖β‖b=\beta/||\beta||, we could select the
leading sample eigenvector hh of SS.
However, for fixed nn, the asymptotic limit in pp of the cosine of the angle beetween hh and bb is positive. In fact it is equal to

|  |  |  |
| --- | --- | --- |
|  | (1+δ2n​B2​σ2)−1<1,\big(1+\frac{\delta^{2}}{nB^{2}\sigma^{2}}\big)^{-1}<1, |  |

where B2B^{2} is the limit of ‖β‖2/p||\beta||^{2}/p and δ2\delta^{2} is the limit of (1/p)​∑i=1pδi2(1/p)\sum\_{i=1}^{p}\delta\_{i}^{2} as p→∞p\to\infty.

A definite improvement is obtained with the James-Stein eigenvector shrinkage estimator, hJSEh^{\rm JSE}, defined as follows. Let
h1h\_{1} denote the projection of hh onto the line spanned by 𝟏\mathbf{1}. Define the shrinkage constant

|  |  |  |  |
| --- | --- | --- | --- |
|  | c=ℓ2λ2​(1−‖h1‖2)c=\frac{\ell^{2}}{\lambda^{2}(1-||h\_{1}||^{2})} |  | (101) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | H=c​h1+(1−c)​h.H=ch\_{1}+(1-c)h. |  | (102) |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | hJSE=H/‖H‖.h^{\rm JSE}=H/||H||. |  | (103) |

The unit vector hJSEh^{\rm JSE} is obtained from hh by correcting a concentration of measure effect that pushes hh farther away from 𝟏\mathbf{1} than bb.

Recalling that the iith diagonal element si​is\_{ii} of SS is the sample variance of the iith asset, we estimate the iith idiosyncratic variance as

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ^i2=si​i−η2​(hiJSE)2.\hat{\delta}\_{i}^{2}=s\_{ii}-\eta^{2}(h^{\rm JSE}\_{i})^{2}. |  | (104) |

Our estimated non-singular covariance matrix ΣJSE\Sigma^{\rm JSE} is now

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣJSE=η2​hJSE​(hJSE)⊤+d​i​a​g​(δ^12,…,δ^p2).\Sigma^{\rm JSE}=\eta^{2}h^{\rm JSE}(h^{\rm JSE})^{\top}+diag(\hat{\delta}\_{1}^{2},\dots,\hat{\delta}\_{p}^{2}). |  | (105) |

### 4.2  Consistency of single index estimators

When estimating betas from market data as in Section [2.1](#S2.SS1 "2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"), there are three covariance matrices in the picture:

1. 1.

   the unobserved population covariance

   |  |  |  |
   | --- | --- | --- |
   |  | Σ=σ2​β​β⊤+Δ,\Sigma=\sigma^{2}\beta\beta^{\top}+\Delta, |  |
2. 2.

   the covariance estimated from observed returns

   |  |  |  |
   | --- | --- | --- |
   |  | ΣJSE=η2​hJSE​(hJSE)⊤+ΔJSE,\Sigma^{\rm JSE}=\eta^{2}h^{\rm JSE}(h^{\rm JSE})^{\top}+\Delta^{\rm JSE}, |  |
3. 3.

   the market covariance incorporating the observed market portfolio wMw\_{M}

   |  |  |  |
   | --- | --- | --- |
   |  | ΣM=σM2​βM​(βM)⊤+ΔM\Sigma^{M}=\sigma^{2}\_{M}\beta^{M}(\beta^{M})^{\top}+\Delta^{M} |  |

   with notation defined in ([36](#S2.E36 "In 2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio")), ([37](#S2.E37 "In 2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio")), and ([39](#S2.E39 "In 2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio")).

There is a consistency question with this approach, because
wM⊤​ΣM​wM≠σM2w\_{M}^{\top}\Sigma^{M}w\_{M}\neq\sigma\_{M}^{2}. Further, the beta factors for the two estimators disagree: (η/σM)​hJSE≠βM(\eta/\sigma\_{M})h^{\rm JSE}\neq\beta^{M}.

However, a single factor estimator like ΣJSE\Sigma^{\rm JSE} has the benefit that the inconsistency above vanishes for a large number of assets, as p→∞p\to\infty.

Direct computation establishes the following

###### Theorem 4.

Consider a sequence in pp of pp-dimensional population covariance models

|  |  |  |
| --- | --- | --- |
|  | Σ=σ2​β​β⊤+Δ\Sigma=\sigma^{2}\beta\beta^{\top}+\Delta |  |

where σ2\sigma^{2} is fixed, Δ\Delta is bounded in pp, and |β|2/p|\beta|^{2}/p tends to a positive finite limit. Suppose the number of observations used to determine the sample covariance matrix is fixed independent of pp.

Then, with ΣM\Sigma^{M} computed using Σ^=ΣJSE\hat{\Sigma}=\Sigma^{\rm JSE}, we have, as p→∞p\to\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |bM−hJSE|→0\displaystyle|b^{M}-h^{\rm JSE}|\to 0 |  | (106) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |σM2​|βM|2−η2|/p→0\displaystyle|\sigma^{2}\_{M}|\beta^{M}|^{2}-\eta^{2}|/p\to 0 |  | (107) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |δiM−ΔiJSE|→0.\displaystyle|\delta^{M}\_{i}-\Delta^{\rm JSE}\_{i}|\to 0. |  | (108) |

This means that the market beta, if computed with ΣJSE\Sigma^{\rm JSE}, is asymptotically the same as the leading factor in the single index covariance matrix that defines it.

## 5  Multifactor JSM estimation

The multifactor JSM estimator is obtained from a PCA estimate by an appropriate shrinkage of the qq-dimensional factor subspace toward a suitable shrinkage target. It is suitable when p>>np>>n; complete discussion of this method appears in Shkolnik et al. [[2024](#bib.bib15 "Portfolio selection revisited")].

In this section we summarize the method, which is the same for any qq. The returns model is

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=B​f+ϵ,r=Bf+\epsilon, |  | (109) |

where ff is a mean-zero random qq-vector of returns to qq risk factors, ϵ\epsilon is a mean zero random pp-vector of specific returns whose components are independent of each other and of ff, and BB is an unknown p×qp\times q parameter matrix of sensitivities of the securities to the factors.

With a time series of nn i.i.d. returns, q<n<pq<n<p, let RR denote the p×np\times n matrix of centered returns data. For the sample covariance matrix S=R​R⊤/nS=RR^{\top}/n with rank n+≤nn\_{+}\leq n and positive eigenvalues λ12≥λ22≥λ32≥⋯≥λn+2\lambda\_{1}^{2}\geq\lambda\_{2}^{2}\geq\lambda\_{3}^{2}\geq\dots\geq\lambda\_{n\_{+}}^{2}, take the spectral decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=∑i=1n+λi2​hi​hi⊤=H​H⊤+N,S=\sum\_{i=1}^{n\_{+}}\lambda\_{i}^{2}h\_{i}h\_{i}^{\top}=HH^{\top}+N, |  | (110) |

where hih\_{i} is the unit eigenvector corresponding to λi2\lambda\_{i}^{2}, HH is the p×qp\times q matrix with columns λ1​h1,…,λq​hq\lambda\_{1}h\_{1},\dots,\lambda\_{q}h\_{q}, and N=S−H​H⊤N=S-HH^{\top}.
Then form the specific variance estimate Δ=d​i​a​g​(N)\Delta=diag(N) to be the diagonal matrix with the same diagonal as NN.

The qq-factor PCA covariance estimator is ΣPCA=H​H⊤+Δ\Sigma^{\rm PCA}=HH^{\top}+\Delta, but this can be improved by shrinking H to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣJSM=HJSM​HJSM⊤+Δ\Sigma^{\rm JSM}=H\_{\rm JSM}H\_{\rm JSM}^{\top}+\Delta |  | (111) |

as follows.

From the re-weighted data matrix Rw=Δ−1/2​RR\_{w}=\Delta^{-1/2}R, we can recompute the p×qp\times q leading eigenvector matrix HH via

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rw​Rw⊤/n=Hw​Hw⊤+NwR\_{w}R\_{w}^{\top}/n=H\_{w}H\_{w}^{\top}+N\_{w} |  | (112) |

and then let H¯=Δ1/2​Hw\bar{H}=\Delta^{1/2}H\_{w}.
Define a p×qp\times q shrinkage target

|  |  |  |  |
| --- | --- | --- | --- |
|  | M=𝟏p​(𝟏p⊤​Δ−1​𝟏p)−1​𝟏p⊤​Δ−1​H¯.M=\mathbf{1}\_{p}(\mathbf{1}\_{p}^{\top}\Delta^{-1}\mathbf{1}\_{p})^{-1}\mathbf{1}\_{p}^{\top}\Delta^{-1}\bar{H}. |  | (113) |

Then HJSMH\_{\rm JSM} is defined by linear shrinkage toward MM:

|  |  |  |  |
| --- | --- | --- | --- |
|  | HJSM=H¯​C+M​(I−C)H\_{\rm JSM}=\bar{H}C+M(I-C) |  | (114) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=I−ν2​J−1,J=(H¯−M)⊤​Δ−1​(H¯−M),C=I-\nu^{2}J^{-1},\quad J=(\bar{H}-M)^{\top}\Delta^{-1}(\bar{H}-M), |  | (115) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν2=t​r​a​c​e​(Δ)n+−q.\nu^{2}=\frac{trace(\Delta)}{n\_{+}-q}. |  | (116) |

The format

|  |  |  |  |
| --- | --- | --- | --- |
|  | HJSM=B​Ω​B⊤+ΔH\_{\rm JSM}=B\Omega B^{\top}+\Delta |  | (117) |

is obtained by setting the columns of BB to be the ordered unit eigenvectors of HJSM​HJSM⊤H\_{\rm JSM}{H\_{\rm JSM}}^{\top}, and Ω\Omega the diagonal matrix of corresponding eigenvalues.

## References

* A. Beck (2023)
  Introduction to nonlinear optimization: theory, algorithms, and applications with python and matlab.
  2nd edition, SIAM.
  Cited by: [footnote 7](#footnote7 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio").
* S. Boyd and L. Vandenberghe (2004)
  Convex optimization.
   Cambridge Univ. Press, Cambridge, UK.
  Cited by: [footnote 7](#footnote7 "In 3.1 Proof of Theorem 1 ‣ 3 Proofs ‣ Understanding the Long-Only Minimum Variance Portfolio").
* R. Clarke, H. D. Silva, and S. Thorley (2011)
  Minimum-variance portfolio composition.
  The Journal of Portfolio Management Winter,  pp. 31–45.
  Cited by: [§1.1](#S1.SS1.p9.1 "1.1 Introduction ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"),
  [§1.2](#S1.SS2.p14.6 "1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"),
  [§1.2](#S1.SS2.p14.7 "1.2 Main Results ‣ 1 Long-only minimum variance ‣ Understanding the Long-Only Minimum Variance Portfolio"),
  [§2.1](#S2.SS1.p7.1 "2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"),
  [footnote 5](#footnote5 "In 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio").
* L. R. Goldberg, H. Gurdogan, and A. Kercheval (2025)
  Portfolio optimization via strategy-specific eigenvector shrinkage.
  Finance and Stochastics https://doi.org/10.1007/s00780-025-00566-4.
  Cited by: [§4.1](#S4.SS1.p2.2 "4.1 The JSE estimator ‣ 4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio").
* L. R. Goldberg and A. N. Kercheval (2023)
  James-Stein for the leading eigenvector.
  Proceedings of the National Academy of Sciences 120 (2).
  Cited by: [§4.1](#S4.SS1.p2.2 "4.1 The JSE estimator ‣ 4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio").
* L. R. Goldberg, A. Papacinicolau, A. Shkolnik, and S. Ulucam (2020)
  Better betas.
  The Journal of Portfolio Management 47 (1),  pp. 119–136.
  Cited by: [§4.1](#S4.SS1.p2.2 "4.1 The JSE estimator ‣ 4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio").
* L. R. Goldberg, A. Papanicolau, and A. Shkolnik (2022)
  The dispersion bias.
  SIAM Journal of Financial Mathematics 13 (2),  pp. 521–550.
  Cited by: [§4.1](#S4.SS1.p2.2 "4.1 The JSE estimator ‣ 4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio").
* O. Ledoit and M. Wolf (2004)
  Honey, I shrunk the covariance matrix.
  The Journal of Portfolio Management Fall,  pp. 110–119.
  Cited by: [§4.1](#S4.SS1.p1.4 "4.1 The JSE estimator ‣ 4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio"),
  [footnote 5](#footnote5 "In 2.2 Empirical example for a single index model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio").
* W. F. Sharpe (1963)
  A simplified model for portfolio analysis.
  Management Science 9 (2),  pp. 277–293.
  Cited by: [§2.1](#S2.SS1.p7.1 "2.1 Single factor exposure estimation ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio").
* A. Shkolnik, A. Kercheval, H. Gurdogan, L. Goldberg, and H. Bar (2024)
  Portfolio selection revisited.
  Annals of Operations Research.
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Empirical example for a two-factor model ‣ 2 Numerical Examples ‣ Understanding the Long-Only Minimum Variance Portfolio"),
  [§5](#S5.p1.2 "5 Multifactor JSM estimation ‣ Understanding the Long-Only Minimum Variance Portfolio").
* A. Shkolnik (2022)
  James-Stein estimation of the first principal component.
  Stat 11 (1).
  Cited by: [§4.1](#S4.SS1.p2.2 "4.1 The JSE estimator ‣ 4 Single factor beta estimation ‣ Understanding the Long-Only Minimum Variance Portfolio").

BETA