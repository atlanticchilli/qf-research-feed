---
authors:
- Michał Sikorski
doc_id: arxiv:2512.02352v1
family_id: arxiv:2512.02352
is_current: false
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering
url_abs: http://arxiv.org/abs/2512.02352v1
url_html: https://arxiv.org/html/2512.02352v1
venue: arXiv q-fin
version: 1
year: 2025
---

[![[Uncaptioned image]](x1.png) Michał Sikorski](https://orcid.org/0009-0009-4253-9489)
  
Interdisciplinary Centre for Mathematical and Computational Modelling, University of Warsaw
  
Warsaw, Poland
  
mm.sikorski3@student.uw.edu.pl
  
Mail contact: mm.sikorski3@student.uw.edu.pl

###### Abstract

Volatility clustering is one of the most robust stylized facts of financial markets,
yet it is typically detected using moment-based diagnostics or parametric models such
as GARCH. This paper shows that clustered volatility also leaves a clear imprint on the
time-reversal symmetry of horizontal visibility graphs (HVGs) constructed on absolute
returns in physical time. For each time point, we compute the maximal forward and
backward visibility distances, L+​(t)L^{+}(t) and L−​(t)L^{-}(t), and use their empirical
distributions to build a visibility-asymmetry fingerprint comprising the
Kolmogorov–Smirnov distance, variance difference, entropy difference, and a ratio of
extreme visibility spans. In a Monte Carlo study, these HVG asymmetry
features sharply separate volatility-clustered GARCH(1,1) dynamics from i.i.d. Gaussian
noise and from randomly shuffled GARCH series that preserve the marginal distribution
but destroy temporal dependence; a simple linear classifier based on the fingerprint
achieves about 90% in-sample accuracy. Applying the method to daily S&P500 data
reveals a pronounced forward–backward imbalance, including a variance difference
Δ​Var\Delta\mathrm{Var} that exceeds the simulated GARCH values by two orders of magnitude
and vanishes after shuffling. Overall, the visibility-graph asymmetry fingerprint
emerges as a simple, model-free, and geometrically interpretable indicator of volatility
clustering and time irreversibility in financial time series.

*Keywords* financial markets; volatility clustering; horizontal visibility graph; complex networks; GARCH; stylized facts

## 1 Introduction

### 1.1 Motivation

Financial return series are well known to exhibit *volatility clustering*:
large price changes tend to be followed by large changes, and small changes by small
changes. This stylized fact has been documented across asset classes and time scales
and underpins a wide range of econometric models and risk-management tools
([1](https://arxiv.org/html/2512.02352v1#bib.bib1)). Traditional approaches quantify clustering through the autocorrelation
structure of squared or absolute returns, or via parametric volatility models such as
GARCH ([2](https://arxiv.org/html/2512.02352v1#bib.bib2)). While powerful, these methods characterize volatility in
terms of moments or latent parameters rather than in terms of the geometric structure
of the underlying time series.

Visibility graphs (VGs) offer a complementary, intrinsically geometric representation
of time-series structure ([3](https://arxiv.org/html/2512.02352v1#bib.bib3); [6](https://arxiv.org/html/2512.02352v1#bib.bib6)). By connecting data points that
“see” each other under a simple visibility criterion, VGs encode ordinal and
shape-related information in a graph structure, allowing one to apply tools from
network theory to time-series analysis. Prior work has used visibility graphs to study
chaos, irreversibility, and long-range dependence, as well as to build complexity
measures and classifiers ([7](https://arxiv.org/html/2512.02352v1#bib.bib7); [8](https://arxiv.org/html/2512.02352v1#bib.bib8)). Applications to finance include
tests of time irreversibility and market efficiency ([9](https://arxiv.org/html/2512.02352v1#bib.bib9); [10](https://arxiv.org/html/2512.02352v1#bib.bib10)),
but the relationship between visibility-graph structure and core stylized facts such as
volatility clustering remains largely unexplored.

### 1.2 Time Irreversibility

A fundamental property of many nonlinear time-series models is *time irreversibility*:
a statistical asymmetry between a process and its time-reversed counterpart. Formally ([4](https://arxiv.org/html/2512.02352v1#bib.bib4); [5](https://arxiv.org/html/2512.02352v1#bib.bib5)), a strictly stationary process {Xt}\{X\_{t}\} is called
*time-reversible* if for any k∈ℕk\in\mathbb{N} and any ordered times
t1<⋯<tkt\_{1}<\dots<t\_{k},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Xt1,…,Xtk)=d(X−t1,…,X−tk),(X\_{t\_{1}},\dots,X\_{t\_{k}})\stackrel{{\scriptstyle d}}{{=}}(X\_{-t\_{1}},\dots,X\_{-t\_{k}}), |  | (1) |

where =d\stackrel{{\scriptstyle d}}{{=}} denotes equality in distribution. Reversible processes “look the
same” when read forward or backward in time: the frequency of local motifs, magnitudes of
fluctuations, and geometric patterns are invariant under temporal inversion. Classical
examples include i.i.d. noise and, more generally, stationary Gaussian processes with
linear dependence, whose finite-dimensional distributions are fully characterized by
covariances that are symmetric under time reversal.

Financial time series, however, rarely satisfy this symmetry. Volatility clustering, the
persistence of high or low volatility over extended intervals, introduces a directional
structure into the dynamics of |rt||r\_{t}|. Even when raw returns rtr\_{t} are serially
uncorrelated, the conditional variance exhibits memory, evolving asymmetrically in time:
large shocks increase future volatility but are not anticipated by future values.
GARCH-type processes therefore violate time reversibility, as their transition structure
changes when the temporal order is flipped. Empirically, this irreversibility has been
observed across asset classes and is often interpreted as evidence of nonlinear
dependencies, asymmetric information flows, and structural inefficiencies in financial
markets.

Visibility graphs provide a natural geometric framework for detecting such asymmetries.
Once a time orientation is imposed, the HVG becomes a directed structure: each node has a
set of visible neighbors in the past and in the future. Prior research has shown that
imbalances between forward- and backward-looking graph statistics—including in-degree
versus out-degree, directed motifs, and causal visibility patterns—serve as robust tests
of irreversibility in chaotic, biological, and financial systems
([7](https://arxiv.org/html/2512.02352v1#bib.bib7); [5](https://arxiv.org/html/2512.02352v1#bib.bib5); [9](https://arxiv.org/html/2512.02352v1#bib.bib9); [12](https://arxiv.org/html/2512.02352v1#bib.bib12); [13](https://arxiv.org/html/2512.02352v1#bib.bib13); [10](https://arxiv.org/html/2512.02352v1#bib.bib10)). These approaches share a common intuition:
if the underlying dynamics are time-reversible, the directed visibility structure must be
distributionally symmetric; persistent deviations indicate temporal asymmetry in the
generating mechanism.

In the context of this study, we leverage this idea by analyzing the maximal forward and
backward visibility distances, L+​(t)L^{+}(t) and L−​(t)L^{-}(t), computed from the HVG of
absolute returns. These distances quantify, in each time direction, how far the local
volatility level permits visibility to extend before being obstructed by intervening peaks.
For time-reversible benchmarks such as i.i.d. Gaussian noise or randomly shuffled GARCH
returns, the distributions of L+L^{+} and L−L^{-} coincide. In contrast, clustered
volatility produces a systematic compression of forward visibility relative to backward
visibility, generating a clear and robust asymmetry. This directional imbalance thus
emerges as a purely geometric fingerprint of time irreversibility induced by volatility
clustering.

### 1.3 Related Work

Several studies have applied visibility graphs to financial data. Early contributions
focused on mapping price or return series to visibility graphs and analyzing degree
distributions, scale-freeness, or irreversibility as indicators of complexity or
inefficiency ([3](https://arxiv.org/html/2512.02352v1#bib.bib3); [7](https://arxiv.org/html/2512.02352v1#bib.bib7); [8](https://arxiv.org/html/2512.02352v1#bib.bib8); [9](https://arxiv.org/html/2512.02352v1#bib.bib9); [14](https://arxiv.org/html/2512.02352v1#bib.bib14)). More recently,
([10](https://arxiv.org/html/2512.02352v1#bib.bib10)) analyzed volatility clustering using a combination of clustering
indices, asymmetry measures, and the power of scale-freeness in visibility graphs,
primarily on raw returns and simulated processes, while ([15](https://arxiv.org/html/2512.02352v1#bib.bib15))
combined directed horizontal visibility graphs with Kullback–Leibler divergence to
characterize instability in financial time series. Beyond visibility-based approaches,
there exists a broad ecosystem of algorithmic techniques for assessing time
irreversibility, including entropy-based and symbolic methods; see
([13](https://arxiv.org/html/2512.02352v1#bib.bib13)) for a recent review.

In contrast to these works, the present contribution is threefold. First, we focus on
*maximal* visibility horizons L+​(t)L^{+}(t) and L−​(t)L^{-}(t), rather than on local
degrees or motif counts, and we use them as directional probes of volatility geometry
in physical time. Second, we aggregate these horizons into a compact asymmetry
fingerprint based on distributional distances, second moments, entropy, and extreme
visibility, which can be interpreted without specifying a parametric volatility model.
Third, we demonstrate that these purely geometric descriptors are sufficiently
informative to separate clustered from non-clustered dynamics and to reveal temporal
asymmetry in empirical index data.

### 1.4 Key Idea

The central idea of this paper is that volatility clustering should leave a
*directional* footprint in visibility graphs constructed on a volatility proxy,
such as absolute returns |rt||r\_{t}|. Intuitively, bursts of volatility create local
plateaus and jagged segments in |rt||r\_{t}|, while calm periods correspond to flatter
regions. When we construct a horizontal visibility graph (HVG) on |rt||r\_{t}|, these
patterns translate into differences between the maximal ranges over which each node can
“see” into the past versus into the future. To formalize this intuition, we define
for each time point tt the maximal forward and backward visibility distances
L+​(t)L^{+}(t) and L−​(t)L^{-}(t) and analyze the asymmetry between their empirical
distributions.

### 1.5 Contribution and Outline

This study addresses the following questions:

1. 1.

   Does volatility clustering generate a robust directional asymmetry in the
   visibility structure of absolute returns?
2. 2.

   Can this asymmetry be quantified in a simple way and used as a
   model-free indicator of clustered volatility?
3. 3.

   Is the asymmetry driven by temporal dependence rather than by static
   distributional properties such as heavy tails?

We answer these questions by constructing a *visibility-graph asymmetry
fingerprint* based on L+L^{+} and L−L^{-} and studying its behavior under three
settings: a GARCH(1,1) process with volatility clustering, i.i.d. Gaussian noise, and
a randomly shuffled GARCH series that preserves the marginal distribution of returns
but eliminates temporal dependence.

Our main contributions are:

* •

  We introduce maximal forward and backward visibility distances
  L+​(t)L^{+}(t) and L−​(t)L^{-}(t) as directional descriptors of HVG geometry on
  absolute returns.
* •

  We define a family of asymmetry metrics—including
  Kolmogorov–Smirnov distance, variance difference, entropy difference, and
  extreme-visibility ratios—that quantify differences between the
  distributions of L+L^{+} and L−L^{-}.
* •

  Through Monte Carlo simulation, we show that these asymmetry features
  sharply separate clustered (GARCH) from non-clustered (Gaussian and shuffled
  GARCH) dynamics and yield in-sample classification accuracy of roughly 90%.
* •

  Using randomly permuted series, we demonstrate that the asymmetry is driven by
  temporal volatility clustering rather than by the static marginal distribution of
  returns.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2512.02352v1#S2 "2 Models and Methods ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering") introduces
the time-series models, the HVG construction, and the asymmetry metrics. Section [3](https://arxiv.org/html/2512.02352v1#S3 "3 Numerical Results ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering")
presents the Monte Carlo results and the shuffled-control tests. Section [4](https://arxiv.org/html/2512.02352v1#S4 "4 Discussion ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering")
discusses the implications and limitations of the approach. Section [5](https://arxiv.org/html/2512.02352v1#S5 "5 Conclusion ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering")
concludes and outlines directions for future work.

## 2 Models and Methods

### 2.1 Return Processes and Volatility Clustering

We work with discrete-time log returns rtr\_{t} modeled under two regimes.

#### Gaussian i.i.d. benchmark.

The non-clustered baseline is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=σ​εt,εt∼𝒩​(0,1),r\_{t}=\sigma\,\varepsilon\_{t},\qquad\varepsilon\_{t}\sim\mathcal{N}(0,1), |  | (2) |

with constant volatility σ>0\sigma>0. In this case, the absolute returns {|rt|}\{|r\_{t}|\} have
no temporal dependence and exhibit no volatility clustering by construction.

#### GARCH(1,1) process.

To generate clustered volatility, we use a standard GARCH(1,1) model
([2](https://arxiv.org/html/2512.02352v1#bib.bib2))

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=σt​εt,σt2=ω+α​rt−12+β​σt−12,r\_{t}=\sigma\_{t}\varepsilon\_{t},\qquad\sigma\_{t}^{2}=\omega+\alpha r\_{t-1}^{2}+\beta\sigma\_{t-1}^{2}, |  | (3) |

where εt∼𝒩​(0,1)\varepsilon\_{t}\sim\mathcal{N}(0,1) and parameters are chosen such that
α,β>0\alpha,\beta>0 and α+β<1\alpha+\beta<1. In the simulations below we use
(ω,α,β)=(10−6,0.25,0.72)(\omega,\alpha,\beta)=(10^{-6},0.25,0.72), so that α+β=0.97\alpha+\beta=0.97 and the
process exhibits persistent volatility clustering. The Gaussian benchmark volatility
σ\sigma is chosen so that the unconditional variance of the Gaussian returns is of the
same order as that of the GARCH process.

Throughout the paper we focus on the absolute-return series xt=|rt|x\_{t}=|r\_{t}| as a
volatility proxy. Figure [1](https://arxiv.org/html/2512.02352v1#S2.F1 "Figure 1 ‣ GARCH(1,1) process. ‣ 2.1 Return Processes and Volatility Clustering ‣ 2 Models and Methods ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering")
shows representative realizations of |rt||r\_{t}| for both regimes.

![Refer to caption](fig1_paths.png)


Figure 1: 
Absolute returns |rt||r\_{t}| for a single realization of the GARCH(1,1) process
(top) and the Gaussian i.i.d. benchmark (bottom). The GARCH series exhibits
persistent bursts of high volatility separated by calm periods, whereas the
Gaussian series shows no visible clustering.

### 2.2 Visibility Graph Construction on Absolute Returns

Visibility methods map a scalar time series to a graph by connecting data points that
“see” each other according to a geometric criterion ([3](https://arxiv.org/html/2512.02352v1#bib.bib3); [7](https://arxiv.org/html/2512.02352v1#bib.bib7)).
Given a real-valued sequence {xt}t=1T\{x\_{t}\}\_{t=1}^{T}, each observation is represented by a
node at horizontal coordinate tt and vertical coordinate xtx\_{t}.

#### Natural and horizontal visibility.

In the *natural* visibility graph (VG) ([3](https://arxiv.org/html/2512.02352v1#bib.bib3)), two nodes i<ji<j are
connected if the straight line segment joining (i,xi)(i,x\_{i}) and (j,xj)(j,x\_{j}) lies strictly
above all intermediate data points:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xk<xi+xj−xij−i​(k−i)for all ​k∈(i,j).x\_{k}<x\_{i}+\frac{x\_{j}-x\_{i}}{j-i}\,(k-i)\qquad\text{for all }k\in(i,j). |  | (4) |

This construction preserves the full convex geometry of the series and has been used
to study irreversibility, long-range dependence, and multifractality.

In this work we focus on the *horizontal* visibility graph (HVG) ([7](https://arxiv.org/html/2512.02352v1#bib.bib7)),
a simplified variant obtained by replacing the oblique visibility line with a
horizontal one. Two nodes i<ji<j are connected by an undirected edge if

|  |  |  |  |
| --- | --- | --- | --- |
|  | xk<min⁡(xi,xj)for all ​k∈(i,j).x\_{k}<\min(x\_{i},x\_{j})\qquad\text{for all }k\in(i,j). |  | (5) |

The HVG is a subgraph of the natural VG but retains key properties that make it
particularly convenient for analytical work: it is invariant under strictly monotonic
transformations of the vertical axis, and for many stochastic processes (including
uncorrelated noise) exact results are known for degree distributions and other graph
statistics ([7](https://arxiv.org/html/2512.02352v1#bib.bib7)).

#### Application to absolute returns.

Throughout the paper we apply the HVG construction [5](https://arxiv.org/html/2512.02352v1#S2.E5 "In Natural and horizontal visibility. ‣ 2.2 Visibility Graph Construction on Absolute Returns ‣ 2 Models and Methods ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering") to the
absolute-return series xt=|rt|x\_{t}=|r\_{t}|. Episodes of large volatility manifest as peaks
and jagged segments in xtx\_{t}, while calm periods correspond to relatively flat
segments. By building the HVG on xtx\_{t} in *physical time*, we obtain an
undirected graph G=(V,E)G=(V,E) with V={1,…,T}V=\{1,\dots,T\} and edges EE defined by
[5](https://arxiv.org/html/2512.02352v1#S2.E5 "In Natural and horizontal visibility. ‣ 2.2 Visibility Graph Construction on Absolute Returns ‣ 2 Models and Methods ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering"). The maximal forward and backward visibility distances
L+​(t)L^{+}(t) and L−​(t)L^{-}(t) introduced in Section [2](https://arxiv.org/html/2512.02352v1#S2 "2 Models and Methods ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering") are computed
directly from this adjacency structure.

![Refer to caption](fig_hvg_overlay.png)


Figure 2: 
Example of a horizontal visibility graph (HVG) constructed on a short segment of
absolute returns xt=|rt|x\_{t}=|r\_{t}| from a simulated GARCH(1,1) path. Top: absolute
returns over a window of length TwinT\_{\mathrm{win}}. Bottom: corresponding HVG,
with nodes placed at their time indices and edges connecting pairs of points that
satisfy the horizontal visibility rule [5](https://arxiv.org/html/2512.02352v1#S2.E5 "In Natural and horizontal visibility. ‣ 2.2 Visibility Graph Construction on Absolute Returns ‣ 2 Models and Methods ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering").

### 2.3 Maximal Forward and Backward Visibility Distances

Let G=(V,E)G=(V,E) be the HVG built on {xt}t=1T\{x\_{t}\}\_{t=1}^{T}, where V={1,…,T}V=\{1,\dots,T\} is the
set of nodes and EE is the set of edges. For each node tt, we define the
*maximal forward visibility distance* and *maximal backward visibility
distance* as

|  |  |  |
| --- | --- | --- |
|  | L+​(t)=max⁡{j−t:(t,j)∈E,j>t},L^{+}(t)=\max\{j-t:(t,j)\in E,\ j>t\}, |  |

|  |  |  |
| --- | --- | --- |
|  | L−​(t)=max⁡{t−i:(i,t)∈E,i<t}.L^{-}(t)=\max\{t-i:(i,t)\in E,\ i<t\}. |  |

If a node has no neighbors in the forward (backward) direction, we set L+​(t)=0L^{+}(t)=0
(L−​(t)=0L^{-}(t)=0). In practice, we discard the first and last nodes when computing
statistics on {L+​(t),L−​(t)}\{L^{+}(t),L^{-}(t)\} to mitigate boundary effects.

These maximal distances quantify the longest temporal horizon over which node tt can
“see” in each direction. In the context of |rt||r\_{t}|, they reflect how far a given
volatility level is geometrically compatible with past and future volatility episodes.

### 2.4 Asymmetry Metrics

To quantify the directional asymmetry of visibility horizons, we compare the empirical
distributions of the forward and backward distances,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {L+​(t)}t=2T−1,{L−​(t)}t=2T−1.\{L^{+}(t)\}\_{t=2}^{T-1},\qquad\{L^{-}(t)\}\_{t=2}^{T-1}. |  | (6) |

We extract the following asymmetry metrics, which together form the
*visibility-graph asymmetry fingerprint*:

* •

  Kolmogorov–Smirnov distance between the two distributions:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | DKS=supℓ|FL+​(ℓ)−FL−​(ℓ)|,D\_{\mathrm{KS}}=\sup\_{\ell}\left|F\_{L^{+}}(\ell)-F\_{L^{-}}(\ell)\right|, |  | (7) |

  where FL+F\_{L^{+}} and FL−F\_{L^{-}} are the empirical cumulative distribution
  functions. This measures the overall shape difference.
* •

  Variance difference:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Δ​Var=Var​(L+)−Var​(L−).\Delta\mathrm{Var}=\mathrm{Var}(L^{+})-\mathrm{Var}(L^{-}). |  | (8) |

  Volatility clustering is expected to induce large fluctuations in visibility spans,
  leading to a large magnitude of Δ​Var\Delta\mathrm{Var}.
* •

  Entropy difference:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Δ​H=H​(L+)−H​(L−),\Delta H=H(L^{+})-H(L^{-}), |  | (9) |

  where HH denotes the Shannon entropy of the empirical distribution. This captures
  asymmetry in the spread and irregularity of visibility horizon lengths.
* •

  Maximal distance difference:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Δmax=max⁡(L+)−max⁡(L−),\Delta\_{\max}=\max(L^{+})-\max(L^{-}), |  | (10) |

  highlighting possible extreme asymmetry in long-range visibility.
* •

  Mean ratio:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | R=𝔼​[L+]𝔼​[L−]+ε,R=\frac{\mathbb{E}[L^{+}]}{\mathbb{E}[L^{-}]+\varepsilon}, |  | (11) |

  with a small regularization constant ε>0\varepsilon>0 to avoid division by zero.

For each simulated path, we compute this set of features
(DKS,Δ​Var,Δ​H,Δmax,R)(D\_{\mathrm{KS}},\Delta\mathrm{Var},\Delta H,\Delta\_{\max},R) and treat it as the
characteristic asymmetry fingerprint of that path.

### 2.5 Asymmetry Under Time-Reversible Benchmarks

For strictly stationary and time-reversible processes, such as Gaussian white noise or
more general linear Gaussian models, the joint law of the HVG is invariant under time
reversal. In particular, if ℛ\mathcal{R} denotes the operation that reverses the order
of the series and correspondingly flips the direction of time, then the distribution of
L+​(t)L^{+}(t) in the original series coincides with that of L−​(t)L^{-}(t) in the reversed
series, and conversely. Under mild regularity conditions this implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[L+]=𝔼​[L−],Var​(L+)=Var​(L−),\mathbb{E}[L^{+}]=\mathbb{E}[L^{-}],\qquad\mathrm{Var}(L^{+})=\mathrm{Var}(L^{-}), |  | (12) |

and, in the limit of large samples, DKSD\_{\mathrm{KS}}, Δ​Var\Delta\mathrm{Var},
Δ​H\Delta H, and Δmax\Delta\_{\max} converge to zero in expectation. In finite samples,
small residual asymmetries arise from sampling fluctuations, but they should remain of
order T−1/2T^{-1/2} and display no systematic bias toward either time direction. This
provides a theoretical baseline against which the empirical asymmetry observed in
clustered volatility models and real data can be interpreted.

### 2.6 Shuffle Control

To disentangle the influence of temporal volatility clustering from that of the marginal
distribution of returns, we use a shuffle-control test. Starting from a GARCH(1,1) return
series {rt}\{r\_{t}\}, we construct a *shuffled control* by randomly permuting the returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {rtshuf}=π​({rt}),\{r\_{t}^{\mathrm{shuf}}\}=\pi(\{r\_{t}\}), |  | (13) |

where π\pi is a random permutation. The shuffled series {rtshuf}\{r\_{t}^{\mathrm{shuf}}\}
preserves the marginal distribution of rtr\_{t} (and therefore of |rt||r\_{t}|) but destroys
all serial dependence and clustering.

Applying the same HVG asymmetry pipeline to |rtshuf||r\_{t}^{\mathrm{shuf}}| allows us to
compare:

* •

  a clustered process (GARCH),
* •

  a non-clustered process with thin tails (Gaussian),
* •

  a non-clustered randomly shuffled series with the *same* marginal distribution as GARCH.

If the asymmetry metrics observed in GARCH vanish or collapse to the Gaussian level
under shuffling, this indicates that they are driven by temporal clustering rather than
by the static marginal distribution.

## 3 Numerical Results

### 3.1 Simulation Design

We simulate n=5000n=5000 independent paths under each of the following regimes:

1. 1.

   Financial (GARCH): GARCH(1,1) returns with parameters
   (ω,α,β)=(10−6,0.25,0.72)(\omega,\alpha,\beta)=(10^{-6},0.25,0.72), yielding persistent volatility clustering.
2. 2.

   Nonfinancial (Gaussian): i.i.d. Gaussian returns with constant
   volatility chosen so that the unconditional variance is of the same order as that of
   the GARCH process.
3. 3.

   Shuffled GARCH: randomly shuffled GARCH series obtained by permuting
   each GARCH return series.

Each path has length T=6000T=6000 observations. For each path, we consider the absolute
returns xt=|rt|x\_{t}=|r\_{t}|, construct the HVG, compute L+​(t)L^{+}(t) and L−​(t)L^{-}(t), and
extract the asymmetry fingerprint (DKS,Δ​Var,Δ​H,Δmax,R)(D\_{\mathrm{KS}},\Delta\mathrm{Var},\Delta H,\Delta\_{\max},R).

### 3.2 Asymmetry Fingerprints: GARCH vs. Gaussian vs. Shuffled

Table [1](https://arxiv.org/html/2512.02352v1#S3.T1 "Table 1 ‣ 3.2 Asymmetry Fingerprints: GARCH vs. Gaussian vs. Shuffled ‣ 3 Numerical Results ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering") reports the empirical mean of each asymmetry metric across
paths, grouped by model:

Table 1: Mean HVG asymmetry features for GARCH (financial), Gaussian (nonfinancial),
and shuffled GARCH paths (n=5000n=5000 each).

| Model | DKSD\_{\mathrm{KS}} | Δ​Var\Delta\mathrm{Var} | Δmax\Delta\_{\max} | RR | Δ​H\Delta H |
| --- | --- | --- | --- | --- | --- |
| Financial (GARCH) | 0.01852 | −192.99-192.99 | 0.5570 | 0.9619 | −0.0600-0.0600 |
| Nonfinancial (Gaussian) | 0.01018 | −10.06-10.06 | 0.0000 | 1.0039 | +0.0000+0.0000 |
| Shuffled GARCH | 0.01037 | +20.23+20.23 | −0.1755-0.1755 | 1.0034 | −0.0001-0.0001 |

Several observations stand out:

* •

  The Kolmogorov–Smirnov asymmetry DKSD\_{\mathrm{KS}} is substantially larger
  for GARCH than for both Gaussian and shuffled series. Shuffling reduces
  DKSD\_{\mathrm{KS}} from approximately 0.01850.0185 to ≈0.0104\approx 0.0104, essentially
  matching the Gaussian baseline and in line with the time-reversible benchmark
  discussed above.
* •

  The variance difference Δ​Var\Delta\mathrm{Var} exhibits very large magnitude
  for GARCH (≈−193\approx-193) and much smaller magnitude for Gaussian and shuffled
  series (≈−10\approx-10 and +20+20, respectively). This indicates that clustered
  volatility strongly amplifies fluctuations in visibility horizon lengths.
* •

  The entropy difference Δ​H\Delta H is clearly negative for GARCH
  (≈−0.06\approx-0.06) but essentially zero for both Gaussian and shuffled series,
  indicating that volatility clustering induces a structural imbalance in the
  complexity of forward and backward visibility spans.
* •

  The mean ratio RR is slightly below unity for GARCH and approximately
  one for the non-clustered regimes, suggesting mild directional bias in average
  visibility distances.

Taken together, these results show that the HVG asymmetry fingerprint distinguishes
clustered from non-clustered dynamics and that the asymmetry largely disappears when
temporal dependence is destroyed via shuffling.

The separation between clustered and non-clustered regimes is visualized in
Figure [3](https://arxiv.org/html/2512.02352v1#S3.F3 "Figure 3 ‣ 3.2 Asymmetry Fingerprints: GARCH vs. Gaussian vs. Shuffled ‣ 3 Numerical Results ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering"), which plots DKSD\_{\mathrm{KS}} against
Δ​Var\Delta\mathrm{Var} for all simulated paths.

![Refer to caption](fig3_scatter_Dks_varDiff.png)


Figure 3: 
Scatter plot of Kolmogorov–Smirnov asymmetry DKSD\_{\mathrm{KS}} versus variance
difference Δ​Var\Delta\mathrm{Var} for all simulated paths. The GARCH ensemble
(clustered volatility) occupies a distinct region of the feature space compared
with the Gaussian and shuffled-GARCH ensembles, illustrating the discriminative
power of the visibility-graph asymmetry fingerprint.

To further highlight the entropy imbalance between forward and backward visibility
spans, Figure [4](https://arxiv.org/html/2512.02352v1#S3.F4 "Figure 4 ‣ 3.2 Asymmetry Fingerprints: GARCH vs. Gaussian vs. Shuffled ‣ 3 Numerical Results ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering") shows the distribution of Δ​H\Delta H for the three
ensembles.

![Refer to caption](fig4_box_entropy.png)


Figure 4: 
Boxplots of entropy asymmetry Δ​H=H​(L+)−H​(L−)\Delta H=H(L^{+})-H(L^{-}) for the GARCH,
Gaussian, and shuffled-GARCH ensembles. The GARCH paths exhibit a clear negative
entropy imbalance, whereas both Gaussian and shuffled-GARCH paths are centered
close to zero, consistent with the absence of directional volatility clustering.

### 3.3 Randomization Test: Isolating Clustering Effects

The comparison between GARCH and its randomly shuffled variant is particularly informative.

The shuffled series retains the heavy-tailed marginal distribution of |rt||r\_{t}| but
destroys all volatility clustering. The fact that both DKSD\_{\mathrm{KS}} and
Δ​H\Delta H for shuffled GARCH are nearly indistinguishable from Gaussian, and that
|Δ​Var||\Delta\mathrm{Var}| is an order of magnitude smaller than in the original GARCH
paths, strongly suggests that the visibility-graph asymmetry is driven by temporal
volatility clustering rather than by static distributional properties alone.

In other words, the asymmetry metrics react primarily to *how* volatility episodes
are organized in time, not merely to the presence of large or small returns in the
marginal distribution.

### 3.4 Empirical Study

The simulation results presented in the previous sections indicate that the horizontal visibility graph (HVG) encodes latent geometric information related to temporal symmetry properties of financial time series. In particular, clustered volatility induces measurable directional differences between forward and backward visibility horizons. To examine whether such structural asymmetries also appear in real markets, we apply the proposed methodology to daily absolute returns of the S&P500 index; for related HVG-based analyses of this index, see also ([16](https://arxiv.org/html/2512.02352v1#bib.bib16)).

For comparison, we additionally analyze a time-shuffled version of the same series. Shuffling preserves the marginal distribution of |rt||r\_{t}|, but removes all temporal dependence such as volatility clustering and long-memory effects. Therefore, any asymmetry that is present in the real series but absent after shuffling can be attributed to genuinely temporal—rather than purely distributional—structure.

Table [2](https://arxiv.org/html/2512.02352v1#S3.T2 "Table 2 ‣ 3.4 Empirical Study ‣ 3 Numerical Results ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering") reports the HVG asymmetry metrics for both the original and shuffled S&P500 data.

Table 2: HVG asymmetry features for the real S&P500 absolute-return series and its shuffled counterpart.

| Model | DKSD\_{\mathrm{KS}} | Δ​Var\Delta\mathrm{Var} | Δmax\Delta\_{\max} | RR | Δ​H\Delta H |
| --- | --- | --- | --- | --- | --- |
| Real S&P500 | 0.01069 | +14007.84+14007.84 | 0 | 1.2086 | +0.05300+0.05300 |
| Shuffled S&P500 | 0.00268 | −4665.74-4665.74 | 0 | 0.9472 | −0.00213-0.00213 |

Observation is straightforward: the real S&P500 data exhibit pronounced and highly structured forward–backward asymmetries, while the shuffled data do not. The variance difference is especially striking: Δ​Var≈1.4×104\Delta\mathrm{Var}\approx 1.4\times 10^{4} in the real series, exceeding by two orders of magnitude the values observed in the GARCH(1,1) simulations. Such an extensive imbalance in visibility-span variability reflects the presence of strong volatility bursts, persistent clustering, and heterogeneous temporal organization that disappear entirely once the temporal ordering is removed.

The ratio R≈1.21R\approx 1.21 and the positive entropy difference Δ​H=0.053\Delta H=0.053 further confirm that the forward and backward visibility distributions have fundamentally different shapes in real data. This indicates a clear violation of time-reversal symmetry in market volatility, consistent with well-documented empirical stylized facts such as leverage effects, rough volatility, and long-range dependence ([17](https://arxiv.org/html/2512.02352v1#bib.bib17)). In contrast, the shuffled series yields metrics close to those observed for Gaussian noise and shuffled GARCH, demonstrating that the detected asymmetry originates from temporal dependence rather than from the marginal distribution alone.

Taken together, these findings show that the HVG asymmetry fingerprint is capable of detecting and quantifying structural time asymmetry in real financial markets, thereby reinforcing the evidence obtained from synthetic data and demonstrating the practical relevance of the proposed approach.

### 3.5 Consistency Check via Simple Classification

As an additional diagnostic, we assess whether the asymmetry features possess enough
structure to distinguish clustered from non-clustered dynamics. To this end, we fit a
logistic regression model using the asymmetry metrics

|  |  |  |  |
| --- | --- | --- | --- |
|  | (DKS,Δ​Var,Δ​H,Δmax,R)(D\_{\mathrm{KS}},\Delta\mathrm{Var},\Delta H,\Delta\_{\max},R) |  | (14) |

as predictors and a binary label indicating whether a path is financial (GARCH) or
nonfinancial (Gaussian or shuffled). Using standardized features and the full ensemble
as training data, the classifier attains an in-sample accuracy of approximately
90%90\%.

This simple consistency check confirms that the asymmetry fingerprint contains
sufficient directional information to separate clustered from non-clustered regimes. We emphasize, however, that classification is not the purpose of our study; the model
is used only to validate that the structural asymmetry captured by the HVG metrics is
statistically coherent with the underlying volatility dynamics.

## 4 Discussion

The numerical results demonstrate that maximal visibility asymmetry in the HVG,
measured through differences between the distributions of L+L^{+} and L−L^{-}, is a
sensitive indicator of volatility clustering in absolute returns. Clustered volatility
generates bursts of large |rt||r\_{t}| interspersed with calm periods, which in turn produce
highly irregular visibility horizons in one temporal direction relative to the other.
This manifests as increased DKSD\_{\mathrm{KS}}, large-magnitude Δ​Var\Delta\mathrm{Var},
and a nonzero entropy imbalance Δ​H\Delta H between forward and backward visibility
spans.

The shuffle-control test is crucial for interpretation. Because shuffling preserves
the marginal distribution of |rt||r\_{t}|, any asymmetry that persists after shuffling
cannot be attributed solely to heavy tails or static distributional features. The
observed collapse of the asymmetry metrics toward Gaussian levels in the shuffled
controls provides strong evidence that the asymmetry is driven specifically by the
temporal organization of volatility—namely, by volatility clustering.

#### Why is Δ​Var\Delta\mathrm{Var} so large for the S&P500 series?

The real-data results exhibit an exceptionally large variance difference,
Δ​Var≈1.4×104\Delta\mathrm{Var}\approx 1.4\times 10^{4}, far exceeding the magnitudes observed in
the GARCH simulations. This is not an artefact, but a structural property of equity
markets. Unlike the stationary GARCH(1,1) model used in the Monte Carlo study, the
S&P500 combines several sources of long-range temporal organization: persistent
volatility bursts, volatility roughness, leverage effects, and regime shifts associated
with macroeconomic cycles. These features create long stretches of elevated absolute
returns separated by extended calm periods, producing extremely heterogeneous
visibility horizons. In such environments, very large forward visibility spans may
occur immediately after transitions out of high-volatility regimes, while backward
visibility spans remain short due to the preceding turbulent period. This temporal
asymmetry amplifies the dispersion of visibility distances far beyond what is possible
under stationary GARCH dynamics, thereby generating the very large positive
Δ​Var\Delta\mathrm{Var} observed in Table [2](https://arxiv.org/html/2512.02352v1#S3.T2 "Table 2 ‣ 3.4 Empirical Study ‣ 3 Numerical Results ‣ Visibility-Graph Asymmetry as a Structural Indicator of Volatility Clustering"). In this sense, the magnitude of
Δ​Var\Delta\mathrm{Var} in real markets reflects not only volatility clustering, but also the
multi-scale and nonstationary nature of empirical volatility dynamics ([11](https://arxiv.org/html/2512.02352v1#bib.bib11)).

By construction, the variance difference is sensitive to extreme visibility spans.
This can be seen as a feature rather than a bug: very long visibility horizons occur
precisely when the volatility path exhibits atypically long stretches of calm after a
turbulent period, and these episodes encode valuable information about regime
structure. Nevertheless, in applications where outliers may be driven by measurement
errors or data glitches, one may complement Δ​Var\Delta\mathrm{Var} with more robust
variants based on trimmed or winsorized visibility distances. Exploring such robust
extensions is a natural avenue for future work.

#### Stationarity and interpretation.

Our simulation study is based on stationary models (Gaussian and GARCH), whereas
the S&P500 index is only approximately stationary over long horizons and is subject
to structural breaks. The HVG asymmetry fingerprint should therefore be interpreted as
a *descriptive* structural diagnostic: it summarizes directional properties of the
observed volatility landscape without assuming that the underlying process satisfies
strict stationarity. In particular, nonstationary features such as regime shifts or
slowly varying volatility levels will be reflected in the distributions of L+L^{+} and
L−L^{-} and can contribute to the observed asymmetry. This is consistent with the
interpretation of large Δ​Var\Delta\mathrm{Var} in real data as a combined effect of
clustering, roughness, and regime changes ([11](https://arxiv.org/html/2512.02352v1#bib.bib11); [17](https://arxiv.org/html/2512.02352v1#bib.bib17)).

#### Relation to other measures of time irreversibility.

A wide range of statistics has been proposed to detect time asymmetry in financial
series, including signed measures based on higher-order moments, permutation entropy
asymmetry, and directed motif counts in visibility graphs. The present work is
complementary to these approaches. Rather than focusing on local patterns, we probe
how far visibility extends in each time direction and summarize the resulting
horizons through simple distributional features. The fact that such low-dimensional,
geometric descriptors are sufficient to separate clustered from non-clustered dynamics
suggests that horizontal visibility encodes a nontrivial amount of temporal structure
that is not captured by moment-based diagnostics alone. In this sense, the present
methodology is conceptually aligned with recent visibility-graph irreversibility
studies ([5](https://arxiv.org/html/2512.02352v1#bib.bib5); [12](https://arxiv.org/html/2512.02352v1#bib.bib12); [14](https://arxiv.org/html/2512.02352v1#bib.bib14); [15](https://arxiv.org/html/2512.02352v1#bib.bib15))
while providing a distinct, horizon-based viewpoint.

From a methodological standpoint, the proposed visibility-graph asymmetry fingerprint
is simple to compute, model-free, and interpretable. It does not require estimating a
parametric volatility model and can be applied to any time series of absolute returns.
At the same time, the approach inherits the limitations of visibility-graph methods:
it is primarily sensitive to geometric and ordinal structure and does not directly
yield quantitative volatility forecasts. Its role is best understood as providing a
structural diagnostic and a complementary perspective on volatility dynamics, rather
than as a standalone forecasting tool.

## 5 Conclusion

This paper introduced a visibility-graph asymmetry fingerprint for detecting volatility
clustering in financial time series. By constructing horizontal visibility graphs on
absolute returns in physical time and comparing maximal forward and backward visibility
distances, we defined a set of asymmetry metrics that capture directional imbalances in
the visibility structure. Monte Carlo experiments show that these metrics robustly
separate clustered (GARCH) from non-clustered (Gaussian and shuffled GARCH) dynamics,
with a simple linear classifier achieving roughly 90% in-sample accuracy using only
the asymmetry features.

The shuffle-based control test plays a key role in interpretation, demonstrating that the
observed asymmetry is induced by temporal volatility clustering rather than by static
distributional features. These findings suggest that visibility-graph asymmetry offers
a compact and interpretable structural indicator of clustered volatility, complementing
more traditional moment- and model-based approaches.

Future work will apply the method to a broader universe of empirical financial indices
and individual stocks, extend the analysis to alternative stylized facts such as leverage
effects and rough volatility, and explore related asymmetry measures in natural
visibility graphs and directed visibility graphs. It would also be interesting to design
robust variants of the asymmetry fingerprint tailored to high-frequency data and to
investigate potential links with model-based measures of implied or realized volatility.

## References

* (1)

  Cont, R.
  Empirical properties of asset returns: Stylized facts and statistical issues.
  Quant. Finance 2001, 1, 223–236.
* (2)

  Bollerslev, T.
  Generalized autoregressive conditional heteroskedasticity.
  J. Econom. 1986, 31, 307–327.
* (3)

  Lacasa, L.; Luque, B.; Ballesteros, F.; Luque, J.; Nuño, J.C.
  From time series to complex networks: The visibility graph.
  Proc. Natl. Acad. Sci. USA 2008, 105, 4972–4975.
* (4)

  Ramsey, J.B.; Rothman, P.
  Time Irreversibility and Business Cycle Asymmetry.
  J. Money Credit Bank. 1996, 28, 1–21.
  Available online: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6806>
  (accessed on DATE).
* (5)

  Lacasa, L.; Nuñez, A.; Roldán, É.; Parrondo, J.M.R.; Luque, B.
  Time Series Irreversibility: A Visibility Graph Approach.
  Eur. Phys. J. B 2012, 85, 217.
  Available online: <https://doi.org/10.1140/epjb/e2012-20809-8>
  (accessed on DATE).
* (6)

  Lacasa, L.; Luque, B.; Luque, J.; Nuño, J.C.
  The visibility graph: A new method for estimating the Hurst exponent of fractional
  Brownian motion.
  EPL 2009, 86, 30001.
* (7)

  Luque, B.; Lacasa, L.; Ballesteros, F.; Luque, J.
  Horizontal visibility graphs: Exact results for random time series.
  Phys. Rev. E 2009, 80, 046103.
* (8)

  Flanagan, R.; Lacasa, L.
  Irreversibility of financial time series: A graph-theoretical approach.
  Phys. Lett. A 2016, 380, 1689–1697.
* (9)

  Mansilla, R.
  Algorithmic complexity in financial markets.
  Eur. Phys. J. B 2012, 85, 1–6.
* (10)

  Kim, K.; Song, J.W.
  Analyses on Volatility Clustering in Financial Time-Series Using Clustering Indices,
  Asymmetry, and Visibility Graph.
  IEEE Access 2020, 8, 208779–208795.
* (11)

  Lacasa, L.
  Time reversibility from visibility graphs of nonstationary processes.
  Phys. Rev. E 2015, 92, 022817.
* (12)

  Mori, R.; Someya, H.; Ohtani, T.; Shimizu, Y.; Mizuno, T.
  Measuring the Topological Time Irreversibility of Time Series.
  Front. Phys. 2021, 9, 777958.
* (13)

  Zanin, M.
  Algorithmic Approaches for Assessing Irreversibility in Time Series.
  Entropy 2021, 23, 1474.
* (14)

  Zanin, M.
  Manipulating Time Series Irreversibility Through Continuous Ordinal Patterns Symmetry 2024, 16, 1696.
* (15)

  Fan, Y.; Li, Y.; Zhang, X.; et al.
  Instability of Financial Time Series Revealed by Directed Horizontal Visibility Graph and Kullback–Leibler Divergence.
  Entropy 2025, 27, 402.
* (16)

  Vamvakaris, M.; Lykidis, T.; Papadimitriou, C.; et al.
  Time Series Analysis of S&P 500 Index: A Horizontal Visibility Graph Approach.
  Available online: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3031781> (accessed on DATE).
* (17)

  Gatheral, J.; Jaisson, T.; Rosenbaum, M.
  Volatility Is Rough.
  Quant. Finance 2018, 18, 933–949.