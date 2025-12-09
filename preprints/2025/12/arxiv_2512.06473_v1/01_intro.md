---
authors:
- Stanisław Drożdż
- Paweł Jarosz
- Jarosław Kwapień
- Maria Skupień
- Marcin Wątorek
doc_id: arxiv:2512.06473v1
family_id: arxiv:2512.06473
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2512.06473v1
url_html: https://arxiv.org/html/2512.06473v1
venue: arXiv q-fin
version: 1
year: 2025
---

###### Abstract

Correlations in complex systems are often obscured by nonstationarity, long-range memory, and heavy-tailed fluctuations, which limit the usefulness of traditional covariance-based analyses. To address these challenges, we construct scale and fluctuation-dependent correlation matrices using the multifractal detrended cross-correlation coefficient ρr\rho\_{r} that selectively emphasizes fluctuations of different amplitudes. We examine the spectral properties of these detrended correlation matrices and compare them to the spectral properties of the matrices calculated in the same way from synthetic Gaussian and qqGaussian signals. Our results show that detrending, heavy tails, and the fluctuation-order parameter rr jointly produce spectra, which substantially depart from the random case even under absence of cross-correlations in time series. Applying this framework to one-minute returns of 140 major cryptocurrencies from 2021–2024 reveals robust collective modes, including a dominant market factor and several sectoral components whose strength depends on the analyzed scale and fluctuation order. After filtering out the market mode, the empirical eigenvalue bulk aligns closely with the limit of random detrended cross-correlations, enabling clear identification of structurally significant outliers. Overall, the study provides a refined spectral baseline for detrended cross-correlations and offers a promising tool for distinguishing genuine interdependencies from noise in complex, nonstationary, heavy-tailed systems.

###### keywords:

Multifractal cross-correlations; Detrended cross-correlation analysis; random matrix theory; eigenvalue spectra; cryptocurrency market

\pubvolume

1
\issuenum1
\articlenumber0
\datereceived
\daterevised
\dateaccepted
\datepublished
\hreflinkhttps://doi.org/
\TitleDetrended cross-correlations and their random matrix limit: an example from the cryptocurrency market\TitleCitationDetrended cross-correlations and their random matrix limit\AuthorStanisław Drożdż 1,2,\*\orcidA, Paweł Jarosz 2\orcidB, Jarosław Kwapień 1\orcidC, Maria Skupień 3\orcidD, Marcin Wątorek 2\orcidE\AuthorNamesStanisław Drożdż, Paweł Jarosz, Jarosław Kwapień, Maria Skupień and Marcin Wątorek\corresCorrespondence: marcin.watorek@pk.edu.pl; stanislaw.drozdz@ifj.edu.pl;

## 1 Introduction

Correlations among complex systems’ components play a central role in understanding their collective dynamics Kwapień and Drożdż ([2012](https://arxiv.org/html/2512.06473v1#bib.bib1)). In fields ranging from finance Bun et al. ([2017](https://arxiv.org/html/2512.06473v1#bib.bib2)); Jiang et al. ([2019](https://arxiv.org/html/2512.06473v1#bib.bib3)); Bardoscia et al. ([2021](https://arxiv.org/html/2512.06473v1#bib.bib4)), climatology Srikanthan and McMahon ([2001](https://arxiv.org/html/2512.06473v1#bib.bib5)); Al-Kandari and Jolliffe ([2005](https://arxiv.org/html/2512.06473v1#bib.bib6)); Feijóo and Villanueva ([2016](https://arxiv.org/html/2512.06473v1#bib.bib7)); Mengis et al. ([2018](https://arxiv.org/html/2512.06473v1#bib.bib8)), molecular and biological systems Dykeman and Sankey ([2010](https://arxiv.org/html/2512.06473v1#bib.bib9)); Kamberaj ([2011](https://arxiv.org/html/2512.06473v1#bib.bib10)) to neuroscience Kwapień et al. ([2000](https://arxiv.org/html/2512.06473v1#bib.bib11)); de Cheveigné et al. ([2019](https://arxiv.org/html/2512.06473v1#bib.bib12)); Snyder et al. ([2022](https://arxiv.org/html/2512.06473v1#bib.bib13)), and physics Izenman ([2021](https://arxiv.org/html/2512.06473v1#bib.bib14)), correlation matrices serve as key tools for quantifying interdependencies between multivariate time series. However, the presence of nonstationarities and long-range dependencies in empirical data often leads to spurious correlations, challenging traditional covariance-based analyses Peng et al. ([1994](https://arxiv.org/html/2512.06473v1#bib.bib15)); Chen et al. ([2002](https://arxiv.org/html/2512.06473v1#bib.bib16)); Bryce and Sprague ([2012](https://arxiv.org/html/2512.06473v1#bib.bib17)). To address these issues, detrended cross-correlation analysis (DCCA) Podobnik and Stanley ([2008](https://arxiv.org/html/2512.06473v1#bib.bib18)) and its generalizations Zhou ([2008](https://arxiv.org/html/2512.06473v1#bib.bib19)); Oświęcimka et al. ([2014](https://arxiv.org/html/2512.06473v1#bib.bib20)); Zebende ([2011](https://arxiv.org/html/2512.06473v1#bib.bib21)) have been developed as robust methods for quantifying power-law cross-correlations between nonstationary signals.

Correlation analysis-based methods are widely used in financial markets. They have been successfully applied to stock markets Drożdż et al. ([2000](https://arxiv.org/html/2512.06473v1#bib.bib22)); Plerou et al. ([2000](https://arxiv.org/html/2512.06473v1#bib.bib23), [2002](https://arxiv.org/html/2512.06473v1#bib.bib24)); Utsugi et al. ([2004](https://arxiv.org/html/2512.06473v1#bib.bib25)); Wang et al. ([2013](https://arxiv.org/html/2512.06473v1#bib.bib26)); Zhao et al. ([2018](https://arxiv.org/html/2512.06473v1#bib.bib27)); James and Menzies ([2021](https://arxiv.org/html/2512.06473v1#bib.bib28)); James et al. ([2022](https://arxiv.org/html/2512.06473v1#bib.bib29)), forex Drożdż et al. ([2007](https://arxiv.org/html/2512.06473v1#bib.bib30)); Mai et al. ([2018](https://arxiv.org/html/2512.06473v1#bib.bib31)); Gębarowski et al. ([2019](https://arxiv.org/html/2512.06473v1#bib.bib32)); Miśkiewicz ([2021](https://arxiv.org/html/2512.06473v1#bib.bib33)); Miśkiewicz and Bonarska-Kujawa ([2022](https://arxiv.org/html/2512.06473v1#bib.bib34)), cryptocurrencies Stosic et al. ([2018](https://arxiv.org/html/2512.06473v1#bib.bib35)); Basnarkov et al. ([2019](https://arxiv.org/html/2512.06473v1#bib.bib36)); Zięba et al. ([2019](https://arxiv.org/html/2512.06473v1#bib.bib37)); Drożdż et al. ([2020](https://arxiv.org/html/2512.06473v1#bib.bib38)); Briola and Aste ([2022](https://arxiv.org/html/2512.06473v1#bib.bib39)); James and Menzies ([2022](https://arxiv.org/html/2512.06473v1#bib.bib40)); James ([2022](https://arxiv.org/html/2512.06473v1#bib.bib41)); Jing and Rocha ([2023](https://arxiv.org/html/2512.06473v1#bib.bib42)); Wątorek et al. ([2023](https://arxiv.org/html/2512.06473v1#bib.bib43)); Jin et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib44)), and even NFT tokens Wątorek et al. ([2024](https://arxiv.org/html/2512.06473v1#bib.bib45)). These methods are useful in trading, risk management and portfolio optimization Cohen and Qadan ([2022](https://arxiv.org/html/2512.06473v1#bib.bib46)); James and Menzies ([2022](https://arxiv.org/html/2512.06473v1#bib.bib40)); James ([2022](https://arxiv.org/html/2512.06473v1#bib.bib41)); James et al. ([2022](https://arxiv.org/html/2512.06473v1#bib.bib47), [2023](https://arxiv.org/html/2512.06473v1#bib.bib48)); Bhattacherjee et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib49)); Sila et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib50)); Tsioutsios et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib51)).

In this work, we study the spectral properties of matrices constructed from detrended cross-correlation coefficients ρr\rho\_{r} (also denoted in literature as ρq)\rho\_{q}), which generalize the detrended cross-correlation coefficient ρDCCA\rho\_{{}\_{\rm DCCA}} Zebende ([2011](https://arxiv.org/html/2512.06473v1#bib.bib21)), which is an equivalent of the Pearson cross-correlation for the detrended fluctuation analysis Kwapień et al. ([2015](https://arxiv.org/html/2512.06473v1#bib.bib52)). Each element of the resulting matrix captures the scale-dependent correlation between detrended fluctuations of two time series, controlled by the parameter rr that governs sensitivity to fluctuation amplitudes. This approach allows us to explore interdependencies in systems characterized by heterogeneous scaling behaviors or multifractality, going beyond the scope of linear correlation measures.

Our primary interest lies in the eigenvalue spectra of such detrended correlation matrices. In conventional correlation matrix theory, the Marčenko–Pastur (M-P) distribution provides the null hypothesis for the eigenvalue density when entries are independent and identically distributed random variables, i.e. when no genuine correlations are present Marčenko and Pastur ([1967](https://arxiv.org/html/2512.06473v1#bib.bib53)). However, when matrix elements are derived from detrended cross-correlations, the statistical structure may differ substantially from that assumed by the M-P framework. The detrending procedure introduces scale-dependent filtering and residual cross-structure even under nominally uncorrelated conditions. Consequently, the classical random matrix limit cannot be directly applied as a baseline for identifying significant correlations.

We therefore investigate the eigenvalue spectra of the detrended correlation matrices, constructed from the ensemble of synthetic time series representing Gaussian and qqGaussian models Umarov et al. ([2008](https://arxiv.org/html/2512.06473v1#bib.bib54)). We aim to characterize how detrending and fluctuation-based weighting modify the spectral density and the onset of collective modes. The results provide insights into the appropriate null hypotheses for spectral analysis of detrended correlations and offer a refined framework for distinguishing genuine collective behavior from stochastic background fluctuations in complex systems.

As a practical application of this formalism, we analyze a representative set of the most liquid 140 cryptocurrencies from Binance exchange ([Binance,](https://arxiv.org/html/2512.06473v1#bib.bib55) ). The cryptocurrency market provides a particularly suitable testing ground for detrended correlation analysis due to its pronounced nonstationarity, strong cross-dependencies, and heterogeneity in trading activity and capitalization Wątorek et al. ([2021](https://arxiv.org/html/2512.06473v1#bib.bib56)). Price series of digital assets exhibit complex temporal structures, including volatility clustering Drożdż et al. ([2018](https://arxiv.org/html/2512.06473v1#bib.bib57)); James ([2021](https://arxiv.org/html/2512.06473v1#bib.bib58)); Evrim Mandaci and Cagli ([2022](https://arxiv.org/html/2512.06473v1#bib.bib59)); Nguyen et al. ([2023](https://arxiv.org/html/2512.06473v1#bib.bib60)); Brouty and Garcin ([2024](https://arxiv.org/html/2512.06473v1#bib.bib61)); Sila et al. ([2024](https://arxiv.org/html/2512.06473v1#bib.bib62)); Queiroz et al. ([2024](https://arxiv.org/html/2512.06473v1#bib.bib63)); Bui et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib64)) and multifractal scaling Takaishi ([2018](https://arxiv.org/html/2512.06473v1#bib.bib65)); Stosic et al. ([2019](https://arxiv.org/html/2512.06473v1#bib.bib66)); Takaishi and Adachi ([2020](https://arxiv.org/html/2512.06473v1#bib.bib67)); Bariviera ([2021](https://arxiv.org/html/2512.06473v1#bib.bib68)); Kwapień et al. ([2022a](https://arxiv.org/html/2512.06473v1#bib.bib69), [b](https://arxiv.org/html/2512.06473v1#bib.bib70)); Wątorek et al. ([2024](https://arxiv.org/html/2512.06473v1#bib.bib71)); Drożdż et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib72)), which render standard correlation measures inadequate. Their price changes are also susceptible to external influences from other financial markets Conlon and McGee ([2020](https://arxiv.org/html/2512.06473v1#bib.bib73)); James ([2021](https://arxiv.org/html/2512.06473v1#bib.bib58)); Zhang et al. ([2021](https://arxiv.org/html/2512.06473v1#bib.bib74)); Choi and Shin ([2022](https://arxiv.org/html/2512.06473v1#bib.bib75)); Elmelki et al. ([2022](https://arxiv.org/html/2512.06473v1#bib.bib76)); Wątorek et al. ([2023](https://arxiv.org/html/2512.06473v1#bib.bib77)); Kristjanpoller and Tabak ([2025](https://arxiv.org/html/2512.06473v1#bib.bib78)); Li et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib79)); Nguyen et al. ([2025](https://arxiv.org/html/2512.06473v1#bib.bib80)), as well as geopolitical shocks Bouri et al. ([2022](https://arxiv.org/html/2512.06473v1#bib.bib81)); Hong and Yoon ([2022](https://arxiv.org/html/2512.06473v1#bib.bib82)); Khalfaoui et al. ([2023](https://arxiv.org/html/2512.06473v1#bib.bib83)); Fang et al. ([2024](https://arxiv.org/html/2512.06473v1#bib.bib84)) or social media impact (Poongodi et al., [2021](https://arxiv.org/html/2512.06473v1#bib.bib85); Aharon et al., [2022](https://arxiv.org/html/2512.06473v1#bib.bib86)).

By constructing the detrended correlation matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) from the ρr​(s)\rho\_{r}(s) coefficients computed across multiple time scales ss, we are able to probe the underlying architecture of interdependencies among these assets while suppressing the influence of global trends and nonstationary effects. Examination of the eigenvalue spectra reveals the presence of collective modes associated with market-wide behavior, sectoral groupings, and noise-dominated components. Comparing these empirical spectra with the corresponding limits derived for uncorrelated signals allows us to identify statistically significant deviations indicative of genuine market structure. This approach thus offers a refined spectral perspective on the collective dynamics and information flow within the cryptocurrency market.

## 2 Methods

### 2.1 Detrended cross-correlations

We start from a set of time series: Ui={ui​(j)}j=1T{\rm U}\_{i}=\{u\_{i}(j)\}\_{j=1}^{T} with i=1,…,Ni=1,...,N. For each time series, a corresponding signal profile is constructed by integrating the data along the time axis:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯i​(k)=∑j=1kui​(j),k=1,…,T.\bar{u}\_{i}(k)=\sum\_{j=1}^{k}u\_{i}(j),\quad k=1,...,T. |  | (1) |

Next, for a given scale ss, this signal profile is divided into 2​Ms2M\_{s} non-overlapping windows of width ss starting from both ends of the time series, and, subsequently, it is detrended by best-fitting a polynomial Pν(m)P\_{\nu}^{(m)} of order mm in each window ν\nu individually:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi​(s​ν+k)=u¯i​(s​ν+k)−Pν(m)​(k),k=1,…,s,ν=0,…,2​Ms−1.x\_{i}(s\nu+k)=\bar{u}\_{i}(s\nu+k)-P\_{\nu}^{(m)}(k),\quad k=1,...,s,\quad\nu=0,...,2M\_{s}-1. |  | (2) |

By proceeding along this way with all time series, we obtain a set of the detrended time series Xi{\rm X}\_{i}, where i=1,…,Ni=1,...,N that will be subject to further analysis. Signal covariance is then calculated in each window:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fi​j2​(s,ν)=1s​∑k=1sxi​(s​ν+k)​xj​(s​ν+k),i,j=1,…,N,f^{2}\_{ij}(s,\nu)=\frac{1}{s}\sum\_{k=1}^{s}x\_{i}(s\nu+k)x\_{j}(s\nu+k),\quad i,j=1,...,N, |  | (3) |

which becomes variance if i=ji=j. In order to allow for a multiscale analysis, a parameter r∈ℝr\in\mathbb{R} is introduced and a family of bivariate rr-fluctuation functions is introduced:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fi​jr​(s)=12​Ms​∑ν=02​Ms−1sign​[fi​j2​(s,ν)]​|fi​j2​(s,ν)|r/2,F^{r}\_{ij}(s)=\frac{1}{2M\_{s}}\sum\_{\nu=0}^{2M\_{s}-1}{\rm sign}[f^{2}\_{ij}(s,\nu)]|f^{2}\_{ij}(s,\nu)|^{r/2}, |  | (4) |

where sign of each covariance is preserved while the modulus allows us to avoid complex values if fi​j2​(s,ν)<0f^{2}\_{ij}(s,\nu)<0 and r/2r/2 is not integer Oświęcimka et al. ([2013](https://arxiv.org/html/2512.06473v1#bib.bib87)). These functions become univariate if i=ji=j. Based on Eq. ([4](https://arxiv.org/html/2512.06473v1#S2.E4 "Equation 4 ‣ 2.1 Detrended cross-correlations ‣ 2 Methods")), it is possible to define an rr-dependent detrended cross-correlation coefficient Kwapień et al. ([2015](https://arxiv.org/html/2512.06473v1#bib.bib52)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρri​j​(s)=Fi​jr​(s)Fi​ir​(s)​Fj​jr​(s),\rho\_{r}^{ij}(s)=\frac{F\_{ij}^{r}(s)}{\sqrt{F\_{ii}^{r}(s)F\_{jj}^{r}(s)}}, |  | (5) |

whose values −1⩽ρri​j​(s)⩽1-1\leqslant\rho\_{r}^{ij}(s)\leqslant 1 have similar interpretation as the Pearson cross-correlation coefficient in the case of r>0r>0. However, by considering different values of rr, we are able to focus on the cross-correlations among specific range of fluctuation amplitudes: large-amplitude fluctuation contribution is amplified if r>2r>2 and small-amplitude fluctuation contribution is amplified if r<2r<2.

For a given set of time series, the coefficient ρri​j​(s)\rho\_{r}^{ij}(s) is symmetric with respect to time series order and it can be calculated for all pairs (i,j)(i,j) with j=i+1,…,Nj=i+1,...,N. An rr-dependent detrended cross-correlation matrix is then constructed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝆r​(s)=[ρri​j​(s)]i,j=1N.\boldsymbol{\rho}\_{r}(s)=[\rho\_{r}^{ij}(s)]\_{i,j=1}^{N}. |  | (6) |

The whole procedure from the detrending step to the matrix construction can be repeated for different scales ss in some range smin⩽s⩽smaxs\_{\rm min}\leqslant s\leqslant s\_{\rm max}.

### 2.2 Spectral characteristics of the detrended cross-correlation matrix

Spectral properties of 𝝆r\boldsymbol{\rho}\_{r} can be determined by solving the eigenvalue problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝆r​(s)​𝐯i​(s)=λi​(s)​𝐯i​(s),i=1,…,N,\boldsymbol{\rho}\_{r}(s){\bf v}\_{i}(s)=\lambda\_{i}(s){\bf v}\_{i}(s),\quad i=1,...,N, |  | (7) |

where the ordering is such that λ1⩾λ2⩾…⩾λN\lambda\_{1}\geqslant\lambda\_{2}\geqslant...\geqslant\lambda\_{N}. While the eigenvalues of 𝝆r\boldsymbol{\rho}\_{r} are real-valued owing to the symmetry of the matrix, this matrix is not necessarily positive semi-definite. First, let us look at the simplest case of r=2r=2 and construct a matrix of the fluctuation functions ([4](https://arxiv.org/html/2512.06473v1#S2.E4 "Equation 4 ‣ 2.1 Detrended cross-correlations ‣ 2 Methods")) for all pairs of the time series:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐅2​(s)=1Ms​∑ν𝐟2​(s,ν)=1Ms​∑ν1s​𝐗νT​(s)​𝐗ν​(s)=1T​𝐗T​(s)​𝐗​(s),{\bf F}^{2}(s)=\frac{1}{M\_{s}}\sum\_{\nu}{\bf f}^{2}(s,\nu)=\frac{1}{M\_{s}}\sum\_{\nu}\frac{1}{s}{\bf X}\_{\nu}^{\rm T}(s){\bf X}\_{\nu}(s)=\frac{1}{T}{\bf X}^{\rm T}(s){\bf X}(s), |  | (8) |

where 𝐗ν{\bf X}\_{\nu} is a data matrix created from all time series in a window ν\nu and 𝐗{\bf X} is an analogous data matrix for the whole time series (to simplify notation, we assume that their length TT is a multiple of ss). A dependence of 𝐗{\bf X} on scale ss comes from the fact that detrending a signal with a polynomial of a given degree leaves the more trend in the residual signal the larger the scale ss is. Since it can be expressed as the product 𝐗T​𝐗{\bf X}^{\rm T}{\bf X}, the matrix 𝐅2{\bf F}^{2} is positive semi-definite.

Now, let us consider the case of r=2​nr=2n, n∈ℕn\in\mathbb{N}, in which

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐅2​n​(s)=1Ms​∑ν[𝐟2​(s,ν)]∘n=1Ms​∑ν1sn​[𝐗νT​(s)​𝐗ν​(s)]∘n,{\bf F}^{2n}(s)=\frac{1}{M\_{s}}\sum\_{\nu}\big[{\bf f}^{2}(s,\nu)\big]^{\circ n}=\frac{1}{M\_{s}}\sum\_{\nu}\frac{1}{s^{n}}\big[{\bf X}\_{\nu}^{\rm T}(s){\bf X}\_{\nu}(s)\big]^{\circ n}, |  | (9) |

where [⋅]∘n[\cdot]^{\circ n} denotes the Hadamard product of nn matrices ⋅\cdot (i.e., their element-wise multiplication). It can be shown that this operation preserves the property of positive semi-definiteness (the Schur theorem Johnson ([1974](https://arxiv.org/html/2512.06473v1#bib.bib88))). A sum of matrices preserves the positive semidefiniteness of the components, therefore there exists a matrix 𝐗~​(s){\bf\widetilde{X}}(s) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐅2​n​(s)=1sn​Ms​𝐗~T​(s)​𝐗~​(s).{\bf F}^{2n}(s)=\frac{1}{s^{n}M\_{s}}\widetilde{\bf X}^{\rm T}(s)\widetilde{\bf X}(s). |  | (10) |

This is generally not true for r≠2​nr\neq 2n, however. If this is the case, a condition r/2⩾N−2r/2\geqslant N-2 must hold to guarantee positive semi-definiteness of 𝐅r​(s){\bf F}^{r}(s) as stated by the FitzGerald-Horn theorem FitzGerald and Horn ([1977](https://arxiv.org/html/2512.06473v1#bib.bib89)). Otherwise, this matrix may have negative eigenvalues. When they are negative indeed and when the whole spectrum is non-negative is a delicate question: typically, the smaller is rr (especially if r<1r<1), the larger is the probability that some eigenvalues fall below 0. The opposite is true if rr increases and, eventually, the matrix enters the r/2⩾N−2r/2\geqslant N-2 region. Finally, based on Eq. ([5](https://arxiv.org/html/2512.06473v1#S2.E5 "Equation 5 ‣ 2.1 Detrended cross-correlations ‣ 2 Methods")), we arrive at the conclusion that 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) is positive semi-definite if 𝐅r​(s){\bf F}^{r}(s) reveals this property.

### 2.3 Random matrix limit and departures

The property of positive semi-definiteness of 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) is important from the statistical point of view, because we may then ask a question how is a given matrix related to the Wishart ensemble of random correlation matrices 𝐖{\bf W} Wishart ([1928](https://arxiv.org/html/2512.06473v1#bib.bib90)). In the absence of genuine cross-correlations in 𝐗{\bf X}, this relation is straightforward for r=2r=2, because the structure of 𝐅2​(s){\bf F}^{2}(s) is in this situation similar to the structure of a Pearson correlation matrix. However, for r≠2r\neq 2 the matrix structure of 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) requires applying of different random matrix ensembles.

If the Wishart case is valid, there is a well-defined distribution of eigenvalues of a matrix constructed for a set of uncorrelated Gaussian-distributed time series in the thermodynamical limit N,T→∞N,T\to\infty, T/N=Q=constT/N=Q={\rm const} (the Marčenko-Pastur distribution Marčenko and Pastur ([1967](https://arxiv.org/html/2512.06473v1#bib.bib53))):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕW​(λ)=12​π​Q​λ​(λmax−λ)​(λ−λmin),λmin⩽λ⩽λmax,\phi\_{W}(\lambda)=\frac{1}{2\pi Q\lambda}\sqrt{(\lambda\_{\rm max}-\lambda)(\lambda-\lambda\_{\rm min})},\quad\lambda\_{\rm min}\leqslant\lambda\leqslant\lambda\_{\rm max}, |  | (11) |

where λmin=(1−Q)2\lambda\_{\rm min}=(1-\sqrt{Q})^{2} and λmax=(1+Q)2\lambda\_{\rm max}=(1+\sqrt{Q})^{2}.

In the case of detrended correlations considered here, however, some deviations from the M-P distribution may arise even for random series due to detrending of fluctuations Chen et al. ([2002](https://arxiv.org/html/2512.06473v1#bib.bib16)). The space for such deviations increases with increasing the range of detrending (longer scale ss). To obtain appropriate null hypotheses for the empirical correlations under consideration, in the absence of analytical formulas for the eigenvalue distributions of correlation matrices constructed in such a generalized manner, numerical simulations are necessary. Therefore, such simulated eigenvalue distributions will be conducted in parallel to such analyses for the empirical data.

Another factor that, in the presence of detrending, may lead to further modification of the above characteristics is the fluctuation distributions of the analyzed time series. Distributions of fluctuations of time series representing many natural phenomena develop thicker tails than the ones obeying the normal distribution. For instance, the distributions of fluctuations in financial rates of return on short time scales quite universally Wątorek et al. ([2021](https://arxiv.org/html/2512.06473v1#bib.bib91)) satisfy the so-called inverse-cubic power law Gopikrishnan et al. ([1998](https://arxiv.org/html/2512.06473v1#bib.bib92)) and this applies even to the cryptocurrency markets Stosic et al. ([2018](https://arxiv.org/html/2512.06473v1#bib.bib35)); James et al. ([2021](https://arxiv.org/html/2512.06473v1#bib.bib93)); Drożdż et al. ([2023](https://arxiv.org/html/2512.06473v1#bib.bib94)). Such distributions are quite efficiently described by functions called qqGaussians Tsallis ([2009](https://arxiv.org/html/2512.06473v1#bib.bib95)).

### 2.4 qqGaussian distribution

In general qqGaussian distributions provide a highly practical analytical framework for modeling the corresponding probability distributions. They constitute a natural extension of the standard Gaussian distribution in analogy of how the Tsallis entropy SqS\_{q} extends the classical Boltzmann-Gibbs entropy SS Umarov et al. ([2008](https://arxiv.org/html/2512.06473v1#bib.bib54)); Tsallis et al. ([1995](https://arxiv.org/html/2512.06473v1#bib.bib96)). This class of distributions 𝒢​q\mathcal{G}q is characterized by two parameters: a shape parameter q∈(−∞,3)q\in(-\infty,3) and a scale (width) parameter β>0\beta>0. The corresponding probability density function (PDF) assumes the form Umarov et al. ([2008](https://arxiv.org/html/2512.06473v1#bib.bib54)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕq​(x)=βCq​eq​(−β​x2),\phi\_{q}(x)=\frac{\sqrt{\beta}}{C\_{q}}e\_{q}(-\beta x^{2}), |  | (12) |

where eq​(x)e\_{q}(x) denotes the qq-exponential function

|  |  |  |  |
| --- | --- | --- | --- |
|  | eq​(x)={(1+(1−q)​x)1/(1−q)if ​q≠1​ and ​1+(1−q)​x>00if ​q≠1​ and ​1+(1−q)​x≤0exif ​q=1,e\_{q}(x)=\begin{cases}(1+(1-q)x)^{1/(1-q)}&\text{if }q\neq 1\text{ and }1+(1-q)x>0\\ 0&\text{if }q\neq 1\text{ and }1+(1-q)x\leq 0\\ e^{x}&\text{if }q=1,\end{cases} |  | (13) |

and Cq=∫−∞∞​eq​(x2),d​xC\_{q}=\int{-\infty}^{\infty}e\_{q}(x^{2}),dx is a normalization constant.

Asymptotic behavior at large |x||x| of a qqGaussian for q=3/2q=3/2 then corresponds to the inverse-cubic power law Drożdż et al. ([2010](https://arxiv.org/html/2512.06473v1#bib.bib97)).

### 2.5 Outlying eigenvalues and collectivity

The above considerations concern a set of independently generated random time series, within and between which there are no synchronous correlations. However, the essence of real, natural complex systems is the coexistence of randomness with collective synchronous effects. For fundamental and practical reasons, the latter are, of course, the primary object of interest. Within the general formalism of correlation matrices, such effects manifest themselves in significant deviations from the spectrum of eigenvalues assumed by the appropriate null hypothesis as indicated above.
More specifically Drożdż and Wójcik ([2001](https://arxiv.org/html/2512.06473v1#bib.bib98)); Drożdż et al. ([2002](https://arxiv.org/html/2512.06473v1#bib.bib99)); Guhr and Kälber ([2003](https://arxiv.org/html/2512.06473v1#bib.bib100)), when coherent or collective behavior arises, it effectively reduces the rank of the correlation matrix: a small number of dominant modes capture most of the system’s variance, while the remaining degrees of freedom behave as random noise. This reduced rank is reflected in the presence of a few large eigenvalues that stand well above the random matrix bounds, separating them from the random bulk of the spectrum. Such spectral segregation reveals the emergence of collective dynamics and the formation of correlated groups or patterns within the system. In this way, deviations from full-rank randomness — i.e., the appearance of a low effective rank — serve as a quantitative signature of collective effects and organized structure emerging from an otherwise random background.

## 3 Data

The empirical dataset consists of N=140N=140 exchange rates for the most actively traded cryptocurrencies, quoted in USDT on the Binance exchange ([Binance,](https://arxiv.org/html/2512.06473v1#bib.bib55) ). It covers the period from January 1, 2021, to September 30, 2024, with data publicly available in an open repository ([Dat,](https://arxiv.org/html/2512.06473v1#bib.bib101) ). The time series were recorded at a 1 min sampling frequency and transformed into logarithmic returns R​(tk)=ln⁡p​(tk+1)−ln⁡p​(tk)R(t\_{k})=\ln p(t\_{k+1})-\ln p(t\_{k}), where k=1,…,Tk=1,...,T.

![Refer to caption](Figs/szereginseticT.png)


Figure 1: (Main) Evolution of the cumulative log-returns R^i​(tk)\hat{R}\_{i}(t\_{k}) of the 140 cryptocurrencies over the whole time period from Jan 1, 2021 to Sep 30, 2024. The bulk of the cryptocurrencies is shown in the background (grey lines), while BTC and ETH are distinguished by red and blue lines, respectively. Four specific periods are distinguished by narrow vertical rectangles (a)-(d). (Inset) Evolution of the same data during a selected shorter period (b): Aug 15, 2023 to Aug 18, 2023.

In order for the relative price changes to be directly comparable, the evolution of the cumulative logarithmic returns R^i​(tk)=∑k=1TRi​(tk)\hat{R}\_{i}(t\_{k})=\sum\_{k=1}^{T}R\_{i}(t\_{k}) of the N=140N=140 cryptocurrencies considered here indexed by ii (i=1,…,Ni=1,...,N) over the analyzed time period is presented in Fig. [1](https://arxiv.org/html/2512.06473v1#S3.F1 "Figure 1 ‣ 3 Data"). Various phases of the market can be observed. The bull market in 2021, then the bear market in 2022 with the crash in May 2022. After reaching its bottom at the end of 2022, the market was in a slower growth phase until mid-2024, then moved sideways until the end of September 2024. Thus, the selected dataset allows for market analysis under various conditions.

![Refer to caption](Figs/rozkladRqG.png)


Figure 2: Complementary cumulative distribution function (CCDF) of the log-returns Ri​(tk)R\_{i}(t\_{k}) for all 140 cryptocurrencies together with qqGaussian (q=3/2q=3/2) and power law (γ=3\gamma=3) CCDFs.

From the above rates of return their fluctuation distributions can be directly generated. In the complementary cumulative distribution function (CCDF) representation they are displayed in Fig. [2](https://arxiv.org/html/2512.06473v1#S3.F2 "Figure 2 ‣ 3 Data"). As can be seen from the also shown comparison to the corresponding theoretical references, a very good fit of this distribution is obtained in terms of the qqGaussian with q=3/2q=3/2 which not only provides an overall good fit but also asymptotically corresponds to the inverse cubic law.

The richness of the dynamics of the set of 140 most actively traded cryptocurrencies considered here is illustrated in Fig. 3, where using a moving 7-day window (with a step of one day), the evolution of the largest eigenvalue λ1\lambda\_{1} of the corresponding matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) for r=2r=2 and r=4r=4 and three different values of the detrending scale (ss=10, 60, and 360 min) is shown. As can be seen, λ1\lambda\_{1} strongly depends on the window location and, in some places, exhausts a large part of the maximum possible value equal to the trace of the matrix which in this case equals 140. In the vast majority of cases, λ1\lambda\_{1} is larger for r=2r=2 case matrix than for r=4r=4, which means that cross-correlations occur here rather at the level of fluctuations with medium amplitude. However, it happens, especially in the later part of the time period considered here, that λ1\lambda\_{1} for r=4r=4 takes higher values, which signals the dominance of cross-correlation at the level of larger fluctuation amplitudes. A more detailed inspection indicates that this is associated with more rapid price changes in the cryptocurrency market at such moments. It should also be noted that on average the value of λ1\lambda\_{1} increases for increasingly larger detrending scales which is an effect reminiscent of the Epps effect Epps ([1979](https://arxiv.org/html/2512.06473v1#bib.bib102)); Kwapień et al. ([2004](https://arxiv.org/html/2512.06473v1#bib.bib103)); Wątorek et al. ([2019](https://arxiv.org/html/2512.06473v1#bib.bib104)).

![Refer to caption](Figs/zmiany_wczasie_q2_q4u.png)


Figure 3: Time evolution of the largest eigenvalue λ1\lambda\_{1} of the matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) with r=2r=2 (red) and r=4r=4 (blue) for s=10s=10 (top), s=60s=60 (middle), and s=360s=360 (bottom). A rolling window of length 7 days, shifted by 1 day, was applied. Four specific periods are marked by vertical dashed lines (a)-(d).

## 4 Detrended correlation matrices from random series

Even for random series, the form of the cross-correlation matrix depends significantly on the parameter rr, on the detrending scale ss, and on the fluctuation distributions of these series. As representative examples the synthetic 140 random series of length 10,080 data points (the same as the length of the empirical series) generated from qqGaussian distributions, for three values q=1q=1, which corresponds to the normal distribution, q=3/2q=3/2, which corresponds to the inverse-cubic power law satisfied by the empirical data considered, and for q=2q=2, which corresponds to fluctuations already in the Lévy-stable regime are used here.

### 4.1 Distribution of matrix elements

For these three values of qq, two significantly different detrending scales ss and five values of parameter rr from 2 to 10 with step 2, the distributions of off-diagonal entries (diagonals are units by construction) of the corresponding detrended correlation matrix are systematically illustrated in Fig. [4](https://arxiv.org/html/2512.06473v1#S4.F4 "Figure 4 ‣ 4.1 Distribution of matrix elements ‣ 4 Detrended correlation matrices from random series"). As can be seen, all these elements are important and the normal distribution of these entries — as for traditional random matrices — is obtained only for q=1q=1, r=2r=2 at small detrending scales ss. Otherwise, the probability distributions of these entries develop increasingly fatter tails as qq, rr, and ss increase, although this increase is progressing in a slightly different form for each of these parameters.

![Refer to caption](Figs/zaleznoscodq_140_10k_elmac.png)


Figure 4: Probability density function (PDF) of the off-diagonal elements of the matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) obtained from random uncorrelated time series with qqGaussian distribution defined by q=1q=1 (i.e., a Gaussian distribution, top), q=3/2q=3/2 (middle), and q=2q=2 (bottom). Results for a few even values of the index rr in a range 2⩽r⩽102\leqslant r\leqslant 10 and two scales s=10s=10 (left) and s=360s=360 (right) are shown. Each PDF was created from 100 independent realizations of the random data set. The dashed line represents a Gaussian PDF corresponding to random Wishart matrices.

Another perspective on these relationships, somewhat complementary, is presented in Fig. [5](https://arxiv.org/html/2512.06473v1#S4.F5 "Figure 5 ‣ 4.1 Distribution of matrix elements ‣ 4 Detrended correlation matrices from random series"), where more variants of the scale parameter ss are considered. A systematic increase in the thickness of the tails of these off-diagonal entries is visible. In general, such effects signal a reduction in the effective rank of the matrix Drożdż et al. ([2002](https://arxiv.org/html/2512.06473v1#bib.bib99)), i.e., the appearance of several large eigenvalues relative to the global bulk, where the dominant portion of small eigenvalues is located.

![Refer to caption](Figs/zaleznoscods_140_10k_elmacq2.png)


Figure 5: Probability density function (PDF) of the off-diagonal elements of the matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) obtained from random uncorrelated time series with qqGaussian distribution defined by q=1q=1 (i.e., a Gaussian distribution, top), q=3/2q=3/2 (middle), and q=2q=2 (bottom). Results for different scales 10⩽s⩽100010\leqslant s\leqslant 1000 and for two even values of the index r=2r=2 (left) and r=4r=4 (right) are shown. Each PDF was created from 100 independent realizations of the random data set. The dashed line represents a Gaussian PDF corresponding to random Wishart matrices.

### 4.2 Distribution of eigenvalues

![Refer to caption](Figs/zaleznoscodq_140_10k_all.png)


Figure 6: Eigenvalue distribution ϕ​(λ)\phi(\lambda) for the matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) obtained from random uncorrelated time series with qqGaussian distribution defined by q=1q=1 (i.e., a Gaussian distribution, top), q=3/2q=3/2 (middle), and q=2q=2 (bottom). Results for a few even values of the index rr in a range 2⩽r⩽102\leqslant r\leqslant 10 two scales s=10s=10 (left) and s=360s=360 (right) are shown. Each PDF was created from 100 independent realizations of the random data set. Dashed black line - corresponding Marčenko-Pastur distribution.

![Refer to caption](Figs/zaleznoscods_140_10kq2_all.png)


Figure 7: Eigenvalue distribution ϕ​(λ)\phi(\lambda) for the matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) obtained from random uncorrelated time series with qqGaussian distribution defined by q=1q=1 (i.e., a Gaussian distribution, top), q=3/2q=3/2 (middle), and q=2q=2 (bottom). Results for different scales 10⩽s⩽100010\leqslant s\leqslant 1000 and for two even values of the index r=2r=2 (left) and r=4r=4 (right) are shown. Dashed black line - corresponding Marčenko-Pastur distribution.

What is typically analyzed first in the context of cross-correlation is the eigenvalue spectrum {λi}i=1N\{\lambda\_{i}\}\_{i=1}^{N} of the corresponding correlation matrix. For the cases of the matrices in Fig. [4](https://arxiv.org/html/2512.06473v1#S4.F4 "Figure 4 ‣ 4.1 Distribution of matrix elements ‣ 4 Detrended correlation matrices from random series") and Fig. [5](https://arxiv.org/html/2512.06473v1#S4.F5 "Figure 5 ‣ 4.1 Distribution of matrix elements ‣ 4 Detrended correlation matrices from random series"), the density distributions ϕ​(λ)\phi(\lambda) of the eigenvalues are displayed in Fig. [6](https://arxiv.org/html/2512.06473v1#S4.F6 "Figure 6 ‣ 4.2 Distribution of eigenvalues ‣ 4 Detrended correlation matrices from random series") and Fig. [7](https://arxiv.org/html/2512.06473v1#S4.F7 "Figure 7 ‣ 4.2 Distribution of eigenvalues ‣ 4 Detrended correlation matrices from random series"), respectively. It can be clearly seen that, as the deviations of the off-diagonal element distributions from the normal distribution increase, the departures of the eigenvalue distributions from the M-P distribution increase. The detrending scale ss turns out to be more effective in this respect, and for larger values of ss, even the maximum ϕ​(λ)\phi(\lambda) shifts slightly to the left in relation to the M-P distribution. In turn, with a fixed scale, ϕ​(λ)\phi(\lambda) narrows quite significantly towards the M-P distribution with increasing values of the rr parameter. Let us recall that all these effects occur already at the level of the set (here 140) of random time series.

## 5 Cross-correlations in empirical data

Potential real correlations in the empirical data are reflected in the deviations of the characteristics of the respective correlation matrices from the results presented above for the matrices corresponding to random time series.
In order to inspect various aspects of such correspondence in varying situations we selected four specific positions of the moving window spanning 7 days, generated the corresponding detrended correlation matrices 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) and calculated a complete set of the eigenvalues in each case. The following situations were distinguished: (a) a minimum value of λ1​(r,s,t)\lambda\_{1}(r,s,t) over the whole period analyzed, which occurred in a window that ends on Feb 4, 2021 (see Fig [3](https://arxiv.org/html/2512.06473v1#S3.F3 "Figure 3 ‣ 3 Data")); the position of this minimum was stable across all scales ss and for both considered values of the exponent rr; (b) the large-amplitude cross-correlations are significantly stronger than the average ones: λ1​(r=4)>λ1​(r=2)\lambda\_{1}(r=4)>\lambda\_{1}(r=2) for all considered scales ss; a sample window with such a property ends on Aug 18, 2023; (c) the opposite case of λ1​(r=2)>λ1​(r=4)\lambda\_{1}(r=2)>\lambda\_{1}(r=4); a sample window with such a property ends on Apr 20, 2024; (d) a sample case of an approximate equality λ1​(r=2)≈λ1​(r=4)\lambda\_{1}(r=2)\approx\lambda\_{1}(r=4), which occurred in a window that ends on Aug 12, 2024.
As in the case of the numerical simulations, we consider two even values of the exponent: r=2r=2 and r=4r=4, as well as three scales: s=10s=10 min, s=60s=60 min, and s=360s=360 min.

### 5.1 Distribution of matrix elements

![Refer to caption](Figs/okno_nr24elmac.png)

![Refer to caption](Figs/okno_nr948elmac.png)

![Refer to caption](Figs/okno_nr1194elmac.png)

![Refer to caption](Figs/okno_nr1308elmac.png)

Figure 8: Probability density function of the off-diagonal elements of the empirical matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) (histogram) calculated in rolling windows ending on (a) Feb 4, 2021, (b) Aug 18, 2023, (c) Apr 20, 2024, and (d) Aug 12, 2024. In each case, results for three scales: s=10s=10 (top), s=60s=60 (middle), and s=360s=360 (bottom) and for two index values: r=2r=2 (left) and r=4r=4 (right) are shown (histogram) and the corresponding random matrix ensemble (red dashed line). The random case represents a time series with qqGaussian distribution with q=3/2q=3/2 and ss and rr parameters corresponding to cases shown in the middle row of Fig. [5](https://arxiv.org/html/2512.06473v1#S4.F5 "Figure 5 ‣ 4.1 Distribution of matrix elements ‣ 4 Detrended correlation matrices from random series").

The distributions of the off-diagonal matrix elements of the resulting correlation matrices are displayed in Fig. [8](https://arxiv.org/html/2512.06473v1#S5.F8 "Figure 8 ‣ 5.1 Distribution of matrix elements ‣ 5 Cross-correlations in empirical data") where their random counterparts for q=3/2q=3/2 (inverse-cubic power law) are indicated by the red dashed lines. The deviations of the empirical results from the corresponding random ones are very pronounced (and the weakest for case (a)) and consist mainly in the appearance of a large number of sizable matrix elements, many of them even close to unity. These effects signal an effective reduction in the dimension of the leading component of the correlation matrix, i.e., the appearance of one large or at most several larger eigenvalues repelled from many small ones, which are remnants of the random part of this matrix Drożdż et al. ([2002](https://arxiv.org/html/2512.06473v1#bib.bib99)).

### 5.2 Distribution of eigenvalues

![Refer to caption](Figs/okno_nr24i.png)

![Refer to caption](Figs/okno_nr948i.png)

![Refer to caption](Figs/okno_nr1194i.png)

![Refer to caption](Figs/okno_nr1308i.png)

Figure 9: (Main) Eigenvalue distribution ϕ​(λ)\phi(\lambda) for the matrix 𝝆r​(s)\boldsymbol{\rho}\_{r}(s) obtained from the empirical data in rolling windows ending on (a) Feb 4, 2021, (b) Aug 18, 2023, (c) Apr 20, 2024, and (d) Aug 12, 2024. In each case, results for three scales: s=10s=10 (top), s=60s=60 (middle), and s=360s=360 (bottom) and for two index values: r=2r=2 (left) and r=4r=4 (right) are shown (histogram). Eigenvalue distributions representing random data with qqGaussian distribution with q=3/2q=3/2 and ss and rr parameters corresponding to cases shown in middle row in Fig. [6](https://arxiv.org/html/2512.06473v1#S4.F6 "Figure 6 ‣ 4.2 Distribution of eigenvalues ‣ 4 Detrended correlation matrices from random series") are denoted by red dashed line in each panel. (Inset) Magnification of the bulk-λ\lambda region of the main panel.

The resulting eigenvalue probability density functions for these four cases denoted by (a)-(d) are shown in Fig. [9](https://arxiv.org/html/2512.06473v1#S5.F9 "Figure 9 ‣ 5.2 Distribution of eigenvalues ‣ 5 Cross-correlations in empirical data"). These eigenvalue spectra are compared with the corresponding eigenvalue distribution obtained for uncorrelated time series with an inverse cubic power-law pdf (q=3/2q=3/2, see Fig. [7](https://arxiv.org/html/2512.06473v1#S4.F7 "Figure 7 ‣ 4.2 Distribution of eigenvalues ‣ 4 Detrended correlation matrices from random series")). The same pattern is always observed: the largest eigenvalue λ1\lambda\_{1} is separated from the rest, and the longer the scale ss under analysis is, the larger the gap between λ1\lambda\_{1} and λ2\lambda\_{2} becomes. This result is characteristic of all financial markets, where λ1\lambda\_{1} can be associated with the collective movement of prices of all assets (the market factor) and the strength of this collectivity increases as longer return intervals Δ​t=tk+1−tk\Delta t=t\_{k+1}-t\_{k} are considered. This comes as a natural consequence of delays in the information transfer between the assets stemming from the fact that transactions on different assets are asynchronous and take place at random moments. The market factor is not a unique collective aspect of the cross-correlations among cryptocurrencies: depending on the position of the rolling window on the time axis and on the values of the parameters rr and ss, a 2nd one or more eigenvalues appear to be larger than it would be expected from the eigenvalue distribution for random data. Such individual detached eigenvalues typically describe the sectoral structure of the market, in which groups of assets are more strongly correlated within the group than outside it. Depending on the specific case, in Fig. [9](https://arxiv.org/html/2512.06473v1#S5.F9 "Figure 9 ‣ 5.2 Distribution of eigenvalues ‣ 5 Cross-correlations in empirical data") the number of such eigenvalues ranges from 1 to 5, with the typical pattern being that for r=4r=4 there are more of them than for r=2r=2. It is worth noting, however, that such eigenvalues lying outside the range predicted for random data also appear below the lower bound λmin\lambda\_{\rm min} of the random spectrum. In that case, such small eigenvalues describe correlations between individual pairs of assets, without any signs of broader collectivity.

### 5.3 Filtering out the market factor

An important feature of the spectra shown in almost all panels of Fig. [9](https://arxiv.org/html/2512.06473v1#S5.F9 "Figure 9 ‣ 5.2 Distribution of eigenvalues ‣ 5 Cross-correlations in empirical data") is also a sizable displacement towards zero of the bulk of empirical eigenvalues relative to the corresponding eigenvalue distribution for random data. One of the key causes of this displacement is a fact that when the matrix trace is fixed, the presence of a large, repelled eigenvalue λ1≫λmax\lambda\_{1}\gg\lambda\_{\rm max} and several other eigenvalues above λmax\lambda\_{\rm max} reduces the available range for the remaining eigenvalues, which effectively shifts them leftward (reminiscent of the slaving principle of synergetics Haken ([2004](https://arxiv.org/html/2512.06473v1#bib.bib105))). To reduce this effect, it is necessary to filter out the market factor and construct an analogous eigenvalue distribution for the residual data. This can be done by using a regression-based method (Plerou et al., [2002](https://arxiv.org/html/2512.06473v1#bib.bib24); Kwapień and Drożdż, [2012](https://arxiv.org/html/2512.06473v1#bib.bib1)):

|  |  |  |
| --- | --- | --- |
|  | Rires​(tk)=Ri​(tk)−ai−bi​Z1​(tk)\displaystyle R^{\rm res}\_{i}(t\_{k})=R\_{i}(t\_{k})-a\_{i}-b\_{i}Z\_{1}(t\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Z1​(tk)=∑m=1Nv1​m​Rm​(tk),\displaystyle Z\_{1}(t\_{k})=\sum\_{m=1}^{N}v\_{1m}R\_{m}(t\_{k}), |  | (14) |

where Z1​(tk)Z\_{1}(t\_{k}) is the contribution to total variance associated with λ1\lambda\_{1} and the filtered matrix 𝝆′r​(s)\boldsymbol{\rho^{\prime}}\_{r}(s) is constructed from the residual time series Rires​(tk)R^{\rm res}\_{i}(t\_{k}) with i=1,…,Ni=1,...,N and k=1,…,Tk=1,...,T. The results of diagonalization are analogously illustrated in Fig. [10](https://arxiv.org/html/2512.06473v1#S5.F10 "Figure 10 ‣ 5.3 Filtering out the market factor ‣ 5 Cross-correlations in empirical data"). Indeed, the bulk of the eigenvalues of the empirical correlation matrix coincides quite well with that of the matrix generated from random series with the same detrending scales ss and other parameters. Some eigenvalues slightly pushed towards larger values remain and they reflect more local and sectoral cross-correlations.

![Refer to caption](Figs/okno_nr24Zb.png)

![Refer to caption](Figs/okno_nr948Zb.png)

![Refer to caption](Figs/okno_nr1194Zb.png)

![Refer to caption](Figs/okno_nr1308Zb.png)

Figure 10: Eigenvalue distribution ϕ​(λ)\phi(\lambda) for the filtered matrix 𝝆r′​(s)\boldsymbol{\rho}\_{r}^{\prime}(s) obtained from the empirical data in rolling windows ending on (a) Feb 4, 2021, (b) Aug 18, 2023, (c) Apr 20, 2024, and (d) Aug 12, 2024. In each case, results for three scales: s=10s=10 (top), s=60s=60 (middle), and s=360s=360 (bottom) and for two index values: r=2r=2 (left) and r=4r=4 (right) are shown (histogram). Eigenvalue distributions representing random data with qqGaussian distribution with q=3/2q=3/2 and ss and rr parameters corresponding to cases shown in middle row in Fig. [6](https://arxiv.org/html/2512.06473v1#S4.F6 "Figure 6 ‣ 4.2 Distribution of eigenvalues ‣ 4 Detrended correlation matrices from random series") are denoted by red dashed line in each panel.

## 6 Summary

This study investigates the spectral properties of detrended cross-correlation matrices constructed from the multifractal detrended cross-correlation coefficient ρr​(s)\rho\_{r}(s) which generalizes the Pearson correlation to fluctuation-dependent and scale-dependent settings. Because real world multivariate time series — especially financial ones — exhibit strong nonstationarities, heavy-tailed distributions, and long-range dependence, traditional covariance-based correlation matrices often generate misleading structures. To address this, the paper examines how detrending, fluctuation-selection via the parameter rr and empirical heavy-tailed distributions collectively influence the eigenvalue spectra of empirical detrended correlation matrices and their counterparts constructed from random time series. Synthetic ensembles of Gaussian and qqGaussian time series are first used to characterize the “null” spectral behavior of detrended correlation matrices. The results show that detrending modifies matrix-element distributions and eigenvalue spectra in systematic ways—most notably by fattening the tails of off-diagonal entries and producing departures from the standard Marčenko–Pastur (M-P) distribution even in fully uncorrelated data. The extent of these deviations grows with the detrending scale s,s, the fluctuation-order parameter rr, and the heaviness of the underlying distribution tails.

The empirical analysis employs 1 min returns of 140 the most liquid cryptocurrencies traded on Binance between 2021 and 2024. Across rolling windows and multiple detrending scales, the leading eigenvalues of the detrended correlation matrices consistently rise above their bounds for uncorrelated time series, indicating strong collective behavior. The dominant mode corresponds to market-wide synchronous motion, while several subleading modes reflect sectoral or structural groupings within the cryptocurrency market. The number and size of these outlying eigenvalues depend on both the temporal scale and the chosen fluctuation order with r=4r=4 generally highlighting cross-correlations among large-amplitude price movements. By filtering out the dominant market mode and reanalyzing the residual covariance structure, the paper demonstrates that the empirical bulk eigenvalue distribution aligns closely with the corresponding null spectra derived from detrended random series. The remaining outliers then cleanly reveal local, sector-specific dependencies.

Overall, the work provides a refined spectral benchmark - beyond the classical M-P framework - suitable for systems in which detrending and heavy-tailed fluctuations cannot be neglected. Future research could extend this framework by deriving analytical approximations for the random-matrix limits of detrended correlation spectra, helping to formalize the empirical baselines established in this work.

\authorcontributions

Conceptualization, S.D., J.K and M.W.; methodology, S.D., J.K. and M.W.; software, M.W.; validation, S.D., J.P., J.K. and M.W.; formal analysis, S.D., J.K. and M.W.; investigation, S.D., J.P., J.K., M.S. and M.W.; resources, M.S. and M.W.; data curation, M.S. and M.W.; writing—original draft preparation, S.D. and J.K.; writing—review and editing, S.D., J.P., J.K. and M.W.; visualization, M.S. and M.W.; supervision, S.D.; project administration, S.D. J.P., J.K. and M.W.; funding acquisition, J.P. All authors have read and agreed to the published version of the manuscript.

\funding

This research received no external funding.

\institutionalreview

Not applicable.

\informedconsent

Not applicable.

\dataavailability

The data are available in an open repository ([Dat,](https://arxiv.org/html/2512.06473v1#bib.bib101) )

\conflictsofinterest

The authors declare no conflicts of interest.

\reftitle

References

## References

* Kwapień and Drożdż (2012)

  Kwapień, J.; Drożdż, S.
  Physical approach to complex systems.
  Physics Reports 2012, 515, 115–226.
  <https://doi.org/10.1016/j.physrep.2012.01.007>.
* Bun et al. (2017)

  Bun, J.; Bouchaud, J.P.; Potter, M.
  Cleaning large correlation matrices: tools from random matrix theory.
  Physics Reports 2017, 666, 1–109.
  <https://doi.org/10.1016/j.physrep.2016.10.005>.
* Jiang et al. (2019)

  Jiang, Z.Q.; Xie, W.J.; Zhou, W.X.; Sornette, D.
  Multifractal analysis of financial markets: A review.
  Reports on Progress in Physics 2019, 82, 125901.
  <https://doi.org/10.1088/1361-6633/ab42fb>.
* Bardoscia et al. (2021)

  Bardoscia, M.; Barucca, P.; Battiston, S.; Caccioli, F.; Cimini, G.; Garlaschelli, D.; Saracco, F.; Squartini, T.; Caldarelli, G.
  The physics of financial networks.
  Nature Reviews Physics 2021, 3, 490–507.
  <https://doi.org/10.1038/s42254-021-00322-5>.
* Srikanthan and McMahon (2001)

  Srikanthan, R.; McMahon, T.A.
  Stochastic generation of annual, monthly and daily climate data: A review.
  Hydrology and Earth System Sciences 2001, 5, 653–670.
  <https://doi.org/10.5194/hess-5-653-2001>.
* Al-Kandari and Jolliffe (2005)

  Al-Kandari, N.M.; Jolliffe, I.T.
  Variable selection and interpretation in correlation principal components.
  Environmetrics: The official journal of the International Environmetrics Society 2005, 16, 659–672.
  <https://doi.org/10.1002/env.728>.
* Feijóo and Villanueva (2016)

  Feijóo, A.; Villanueva, D.
  Assessing wind speed simulation methods.
  Renewable and Sustainable Energy Reviews 2016, 56, 473–483.
  <https://doi.org/https://doi.org/10.1016/j.rser.2015.11.094>.
* Mengis et al. (2018)

  Mengis, N.; Keller, D.P.; .; Oschlies, A.
  Systematic Correlation Matrix Evaluation (SCoMaE) - a bottom–up, science-led approach to identifying indicators.
  Earth System Dynamics 2018, 9, 15–31.
  <https://doi.org/10.5194/esd-9-15-2018>.
* Dykeman and Sankey (2010)

  Dykeman, E.C.; Sankey, O.F.
  Normal mode analysis and applications in biological physics.
  Journal of Physics: Condensed Matter 2010, 22, 423202.
  <https://doi.org/10.1088/0953-8984/22/42/423202>.
* Kamberaj (2011)

  Kamberaj, H.
  A theoretical model for the collective motion of proteins by means of principal component analysis.
  Central European Journal of Physics 2011, 9, 96–109.
  <https://doi.org/10.2478/s11534-010-0048-2>.
* Kwapień et al. (2000)

  Kwapień, J.; Drożdż, S.; Joannides, A.
  Temporal correlations versus noise in the correlation matrix formalism: An example of the brain auditory response.
  Physical Review E 2000, 62, 5557–5564.
  <https://doi.org/10.1103/PhysRevE.62.5557>.
* de Cheveigné et al. (2019)

  de Cheveigné, A.; Di Liberto, G.M.; Arzounian, D.; Wong, D.D.; Hjortkjær, J.; Fuglsang, S.; Parra, L.C.
  Multiway canonical correlation analysis of brain data.
  NeuroImage 2019, 186, 728–740.
  <https://doi.org/https://doi.org/10.1016/j.neuroimage.2018.11.026>.
* Snyder et al. (2022)

  Snyder, A.Z.; Nishino, T.; Shimony, J.S.; Lenze, E.J.; Wetherell, J.L.; Voegtle, M.; Miller, J.P.; Yingling, M.D.; Marcus, D.; Gurney, J.; et al.
  Covariance and Correlation Analysis of Resting State Functional Magnetic Resonance Imaging Data Acquired in a Clinical Trial of Mindfulness-Based Stress Reduction and Exercise in Older Individuals.
  Frontiers in Neuroscience 2022, 16, 825547.
  <https://doi.org/10.3389/fnins.2022.825547>.
* Izenman (2021)

  Izenman, A.J.
  Random Matrix Theory and Its Applications.
  Statistical Science 2021, 36, 421–442.
  <https://doi.org/10.1214/20-STS799>.
* Peng et al. (1994)

  Peng, C.K.; Buldyrev, S.V.; Havtin, S.; Simons, M.; Stanley, H.E.; Goldberger, A.L.
  Mosaic organization of DNA nucleotides.
  Physical Review E 1994, 49, 1685–1689.
  <https://doi.org/10.1103/PhysRevE.49.1685>.
* Chen et al. (2002)

  Chen, Z.; Ivanov, P.; Hu, K.; H.E, S.
  Effect of nonstationarities on detrended fluctuation analysis.
  Physical Review E 2002, p. 041107.
  <https://doi.org/10.1103/PhysRevE.65.041107>.
* Bryce and Sprague (2012)

  Bryce, R.M.; Sprague, K.B.
  Revisiting detrended fluctuation analysis.
  Scientific Reports 2012, 2, 315.
  <https://doi.org/10.1038/srep00315>.
* Podobnik and Stanley (2008)

  Podobnik, B.; Stanley, H.E.
  Detrended cross-correlation analysis: A new method for analyzing two nonstationary time series.
  Physical Review Letters 2008, 100, 084102.
  <https://doi.org/10.1103/PhysRevLett.100.084102>.
* Zhou (2008)

  Zhou, W.X.
  Multifractal detrended cross-correlation analysis for two nonstationary signals.
  Physical Review E 2008, 77, 066211.
  <https://doi.org/10.1103/PhysRevE.77.066211>.
* Oświęcimka et al. (2014)

  Oświęcimka, P.; Drożdż, S.; Forczek, M.; Jadach, S.; Kwapień, J.
  Detrended cross-correlation analysis consistently extended to multifractality.
  Physical Review E 2014, 89, 023305.
  <https://doi.org/10.1103/PhysRevE.89.023305>.
* Zebende (2011)

  Zebende, G.
  DCCA cross-correlation coefficient: Quantifying level of cross-correlation.
  Physica A 2011, 390, 614–618.
  <https://doi.org/10.1016/j.physa.2010.10.022>.
* Drożdż et al. (2000)

  Drożdż, S.; Gümmer, F.; Górski, A.Z.; Ruf, F.; Speth, J.
  Dynamics of competition between collectivity and noise in the stock market.
  Physica A 2000, 287, 440–449.
  <https://doi.org/10.1016/S0378-4371(00)00383-6>.
* Plerou et al. (2000)

  Plerou, V.; Gopikrishnan, P.; Rosenow, B.; Amaral, L.; Stanley, H.
  A random matrix theory approach to financial cross-correlations.
  Physica A 2000, 287, 374–382.
  <https://doi.org/https://doi.org/10.1016/S0378-4371(00)00376-9>.
* Plerou et al. (2002)

  Plerou, V.; Gopikrishnan, P.; Rosenow, B.; Amaral, L.A.; Guhr, T.; Stanley, H.E.
  Random matrix approach to cross correlations in financial data.
  Physical Review E 2002, 65, 066126.
  <https://doi.org/10.1103/PhysRevE.65.066126>.
* Utsugi et al. (2004)

  Utsugi, A.; Ino, K.; Oshikawa, M.
  Random matrix theory analysis of cross correlations in financial markets.
  Phys. Rev. E 2004, 70, 026110.
  <https://doi.org/10.1103/PhysRevE.70.026110>.
* Wang et al. (2013)

  Wang, G.J.; Xie, C.; Chen, S.; Yang, J.J.; Yang, M.Y.
  Random matrix theory analysis of cross-correlations in the US stock market: Evidence from Pearson’s correlation coefficient and detrended cross-correlation coefficient.
  Physica A 2013, 392, 3715–3730.
  <https://doi.org/https://doi.org/10.1016/j.physa.2013.04.027>.
* Zhao et al. (2018)

  Zhao, L.; Li, W.; Fenu, A.; Podobnik, B.; Wang, Y.; Stanley, H.E.
  The q-dependent detrended cross-correlation analysis of stock market.
  Journal of Statistical Mechanics: Theory and Experiment 2018, 2018, 023402.
  <https://doi.org/10.1088/1742-5468/aa9db0>.
* James and Menzies (2021)

  James, N.; Menzies, M.
  Efficiency of communities and financial markets during the 2020 pandemic.
  Chaos 2021, 31, 083116.
  <https://doi.org/10.1063/5.005449>.
* James et al. (2022)

  James, N.; Menzies, M.; Gottwald, G.A.
  On financial market correlation structures and diversification benefits across and within equity sectors.
  Physica A 2022, 604, 127682.
  <https://doi.org/10.1016/j.physa.2022.127682.>
* Drożdż et al. (2007)

  Drożdż, S.; Górski, A.; Kwapień, J.
  World currency exchange rate cross-correlations.
  The European Physical Journal B 2007, 58, 499–502.
  <https://doi.org/10.1140/epjb/e2007-00246-8>.
* Mai et al. (2018)

  Mai, Y.; Chen, H.; Zou, J.Z.; Li, S.P.
  Currency co-movement and network correlation structure of foreign exchange market.
  Physica A 2018, 492, 65–74.
  <https://doi.org/https://doi.org/10.1016/j.physa.2017.09.068>.
* Gębarowski et al. (2019)

  Gębarowski, R.; Oświęcimka, P.; Wątorek, M.; Drożdż, S.
  Detecting correlations and triangular arbitrage opportunities in the Forex by means of multifractal detrended cross-correlations analysis.
  Nonlinear Dynamics 2019, 98, 2349–2364.
  <https://doi.org/10.1007/s11071-019-05335-5>.
* Miśkiewicz (2021)

  Miśkiewicz, J.
  Network Analysis of Cross-Correlations on Forex Market during Crises. Globalisation on Forex Market.
  Entropy 2021, 23.
  <https://doi.org/10.3390/e23030352>.
* Miśkiewicz and Bonarska-Kujawa (2022)

  Miśkiewicz, J.; Bonarska-Kujawa, D.
  Evolving Network Analysis of S&P500 Components: COVID-19 Influence of Cross-Correlation Network Structure.
  Entropy 2022, 24.
  <https://doi.org/10.3390/e24010021>.
* Stosic et al. (2018)

  Stosic, D.; Stosic, D.; Ludermir, T.B.; Stosic, T.
  Collective behavior of cryptocurrency price changes.
  Physica A 2018, 507, 499–509.
  <https://doi.org/10.1016/j.physa.2018.05.050>.
* Basnarkov et al. (2019)

  Basnarkov, L.; Stojkoski, V.; Utkovski, Z.; Kocarev, L.
  Correlation patterns in foreign exchange markets.
  Physica A 2019, 525, 1026–1037.
  <https://doi.org/https://doi.org/10.1016/j.physa.2019.04.044>.
* Zięba et al. (2019)

  Zięba, D.; Kokoszczyński, R.; Śledziewska, K.
  Shock transmission in the cryptocurrency market. Is Bitcoin the most influential?
  International Review of Financial Analysis 2019, 64, 102–125.
  <https://doi.org/10.1016/j.irfa.2019.04.009>.
* Drożdż et al. (2020)

  Drożdż, S.; Minati, L.; Oświęcimka, P.; Stanuszek, M.; Wątorek, M.
  Competition of noise and collectivity in global cryptocurrency trading: Route to a self-contained market.
  Chaos 2020, 30, 023122.
  <https://doi.org/10.1063/1.5139634>.
* Briola and Aste (2022)

  Briola, A.; Aste, T.
  Dependency Structures in Cryptocurrency Market from High to Low Frequency.
  Entropy 2022, 24, 1548.
  <https://doi.org/10.3390/e24111548>.
* James and Menzies (2022)

  James, N.; Menzies, M.
  Collective correlations, dynamics, and behavioural inconsistencies of the cryptocurrency market over time.
  Nonlinear Dynamics 2022, 107, 4001–4017.
  <https://doi.org/10.1007/s11071-021-07166-9>.
* James (2022)

  James, N.
  Evolutionary correlation, regime switching, spectral dynamics and optimal trading strategies for cryptocurrencies and equities.
  Physica D 2022, 434, 133262.
  <https://doi.org/10.1016/j.physd.2022.133262>.
* Jing and Rocha (2023)

  Jing, R.; Rocha, L.E.
  A network-based strategy of price correlations for optimal cryptocurrency portfolios.
  Finance Research Letters 2023, 58, 104503.
  <https://doi.org/10.1016/j.frl.2023.104503>.
* Wątorek et al. (2023)

  Wątorek, M.; Skupień, M.; Kwapień, J.; Drożdż, S.
  Decomposing cryptocurrency high-frequency price dynamics into recurring and noisy components.
  Chaos 2023, 33, 083146.
  <https://doi.org/10.1063/5.0165635>.
* Jin et al. (2025)

  Jin, L.; Zheng, B.; Jiang, X.; Xiong, L.; Zhang, J.; Ma, J.
  Dynamic cross-correlation in emerging cryptocurrency market.
  Physica A 2025, 668, 130568.
  <https://doi.org/https://doi.org/10.1016/j.physa.2025.130568>.
* Wątorek et al. (2024)

  Wątorek, M.; Szydło, P.; Kwapień, J.; Drożdż, S.
  Correlations versus noise in the NFT market.
  Chaos 2024, 34, 073112.
  <https://doi.org/10.1063/5.0214399>.
* Cohen and Qadan (2022)

  Cohen, G.; Qadan, M.
  The complexity of cryptocurrencies algorithmic trading.
  Mathematics 2022, 10, 2037.
  <https://doi.org/10.3390/math10122037>.
* James et al. (2022)

  James, N.; Menzies, M.; Chin, K.
  Economic state classification and portfolio optimisation with application to stagflationary environments.
  Chaos, Solitons & Fractals 2022, 164, 112664.
  <https://doi.org/10.1016/j.chaos.2022.112664>.
* James et al. (2023)

  James, N.; Menzies, M.; Chan, J.
  Semi-Metric Portfolio Optimization: A New Algorithm Reducing Simultaneous Asset Shocks.
  Econometrics 2023, 11.
  <https://doi.org/10.3390/econometrics11010008>.
* Bhattacherjee et al. (2025)

  Bhattacherjee, P.; Mishra, S.; Kang, S.H.
  Extreme frequency connectedness, determinants and portfolio analysis of major cryptocurrencies: Insights from quantile time-frequency approach.
  The Quarterly Review of Economics and Finance 2025, 100, 101974.
  <https://doi.org/https://doi.org/10.1016/j.qref.2025.101974>.
* Sila et al. (2025)

  Sila, J.; Mark, M.; Kristoufek, L.; Weber, T.A.
  Crypto market betas: the limits of predictability and hedging.
  Financial Innovation 2025, 11, 107.
  <https://doi.org/10.1186/s40854-025-00777-w>.
* Tsioutsios et al. (2025)

  Tsioutsios, A.; Yarovaya, L.; Dimitriou, D.
  Exploring portfolio diversification with alternative investments: An international TVP-VAR approach.
  Research in International Business and Finance 2025, 80, 103143.
  <https://doi.org/https://doi.org/10.1016/j.ribaf.2025.103143>.
* Kwapień et al. (2015)

  Kwapień, J.; Oświęcimka, P.; Drożdż, S.
  Detrended fluctuation analysis made flexible to detect range of cross-correlated fluctuations.
  Physical Review E 2015, 92, 052815.
  <https://doi.org/10.1103/PhysRevE.92.052815>.
* Marčenko and Pastur (1967)

  Marčenko, V.A.; Pastur, L.A.
  Distribution of eigenvalues for some sets of random matrices.
  Mathematics of the USSR-Sbornik 1967, 1, 457–483.
  <https://doi.org/10.1070/SM1967v001n04ABEH001994>.
* Umarov et al. (2008)

  Umarov, S.; Tsallis, C.; Steinberg, S.
  On a q-Central Limit Theorem Consistent with Nonextensive Statistical Mechanics.
  Milan Journal of Mathematics 2008, 76, 307–328.
  <https://doi.org/10.1007/s00032-008-0087-y>.
* (55)

  Binance.
  <https://www.binance.com/>.
* Wątorek et al. (2021)

  Wątorek, M.; Drożdż, S.; Kwapień, J.; Minati, L.; Oświęcimka, P.; Stanuszek, M.
  Multiscale characteristics of the emerging global cryptocurrency market.
  Physics Reports 2021, 901, 1–82.
  <https://doi.org/10.1016/j.physrep.2020.10.005>.
* Drożdż et al. (2018)

  Drożdż, S.; Gębarowski, R.; Minati, L.; Oświęcimka, P.; Wątorek, M.
  Bitcoin market route to maturity? Evidence from return fluctuations, temporal correlations and multiscaling effects.
  Chaos 2018, 28, 071101.
  <https://doi.org/10.1063/1.5036517>.
* James (2021)

  James, N.
  Dynamics, behaviours, and anomaly persistence in cryptocurrencies and equities surrounding COVID-19.
  Physica A 2021, 570, 125831.
  <https://doi.org/10.1016/j.physa.2021.125831>.
* Evrim Mandaci and Cagli (2022)

  Evrim Mandaci, P.; Cagli, E.C.
  Herding intensity and volatility in cryptocurrency markets during the COVID-19.
  Finance Research Letters 2022, 46, 102382.
  <https://doi.org/10.1016/j.frl.2021.102382>.
* Nguyen et al. (2023)

  Nguyen, A.P.N.; Mai, T.T.; Bezbradica, M.; Crane, M.
  Volatility and returns connectedness in cryptocurrency markets: Insights from graph-based methods.
  Physica A 2023, 632, 129349.
  <https://doi.org/10.1016/j.physa.2023.129349>.
* Brouty and Garcin (2024)

  Brouty, X.; Garcin, M.
  Fractal properties, information theory, and market efficiency.
  Chaos, Solitons & Fractals 2024, 180, 114543.
  <https://doi.org/10.1016/j.chaos.2024.114543>.
* Sila et al. (2024)

  Sila, J.; Kocenda, E.; Kristoufek, L.; Kukacka, J.
  Good vs. bad volatility in major cryptocurrencies: The dichotomy and drivers of connectedness.
  Journal of International Financial Markets, Institutions and Money 2024, 96, 102062.
  <https://doi.org/https://doi.org/10.1016/j.intfin.2024.102062>.
* Queiroz et al. (2024)

  Queiroz, R.; Kristoufek, L.; David, S.
  A combined framework to explore cryptocurrency volatility and dependence using multivariate GARCH and Copula modeling.
  Physica A 2024, 652, 130046.
  <https://doi.org/https://doi.org/10.1016/j.physa.2024.130046>.
* Bui et al. (2025)

  Bui, H.Q.; Schinckus, C.; Al-Jaifi, H.
  Long-range correlations in cryptocurrency markets: A multi-scale DFA approach.
  Physica A 2025, 661, 130417.
  <https://doi.org/10.1016/j.physa.2025.130417>.
* Takaishi (2018)

  Takaishi, T.
  Statistical properties and multifractality of Bitcoin.
  Physica A 2018, 506, 507–519.
  <https://doi.org/10.1016/j.physa.2018.04.046>.
* Stosic et al. (2019)

  Stosic, D.; Stosic, D.; Ludermir, T.B.; Stosic, T.
  Multifractal behavior of price and volume changes in the cryptocurrency market.
  Physica A 2019, 520, 54–61.
  <https://doi.org/https://doi.org/10.1016/j.physa.2018.12.038>.
* Takaishi and Adachi (2020)

  Takaishi, T.; Adachi, T.
  Market efficiency, liquidity, and multifractality of Bitcoin: a dynamic study.
  Asia-Pacific Financial Markets 2020, 27, 145–154.
  <https://doi.org/10.1007/s10690-019-09286-0>.
* Bariviera (2021)

  Bariviera, A.F.
  One model is not enough: Heterogeneity in cryptocurrencies’ multifractal profiles.
  Finance Research Letters 2021, 39, 101649.
  <https://doi.org/https://doi.org/10.1016/j.frl.2020.101649>.
* Kwapień et al. (2022a)

  Kwapień, J.; Wątorek, M.; Bezbradica, M.; Crane, M.; Tan Mai, T.; Drożdż, S.
  Analysis of inter-transaction time fluctuations in the cryptocurrency market.
  Chaos 2022, 32, 083142.
  <https://doi.org/10.1063/5.0104707>.
* Kwapień et al. (2022b)

  Kwapień, J.; Wątorek, M.; Drożdż, S.
  Multifractal cross-correlations of bitcoin and ether trading characteristics in the post-COVID-19 time.
  Future Internet 2022, 14, 215.
  <https://doi.org/doi.org/10.3390/fi14070215>.
* Wątorek et al. (2024)

  Wątorek, M.; Królczyk, M.; Kwapień, J.; Stanisz, T.; Drożdż, S.
  Approaching Multifractal Complexity in Decentralized Cryptocurrency Trading.
  Fractal and Fractional 2024, 8.
  <https://doi.org/10.3390/fractalfract8110652>.
* Drożdż et al. (2025)

  Drożdż, S.; Kluszczyński, R.; Kwapień, J.; Wątorek, M.
  Multifractality and Its Sources in the Digital Currency Market.
  Future Internet 2025, 17.
  <https://doi.org/10.3390/fi17100470>.
* Conlon and McGee (2020)

  Conlon, T.; McGee, R.
  Safe haven or risky hazard? Bitcoin during the Covid-19 bear market.
  Finance Research Letters 2020, 35, 101607.
  <https://doi.org/10.1016/j.frl.2020.101607>.
* Zhang et al. (2021)

  Zhang, Y.J.; Bouri, E.; Gupta, R.; Ma, S.J.
  Risk spillover between Bitcoin and conventional financial markets: An expectile-based approach.
  The North American Journal of Economics and Finance 2021, 55, 101296.
  <https://doi.org/https://doi.org/10.1016/j.najef.2020.101296>.
* Choi and Shin (2022)

  Choi, S.; Shin, J.
  Bitcoin: An inflation hedge but not a safe haven.
  Finance Research Letters 2022, 46, 102379.
  <https://doi.org/10.1016/j.frl.2021.102379>.
* Elmelki et al. (2022)

  Elmelki, A.; Chaâbane, N.; Benammar, R.
  Exploring the relationship between cryptocurrency and S&P500: evidence from wavelet coherence analysis.
  International Journal of Blockchains and Cryptocurrencies 2022, 3, 256–268.
  <https://doi.org/10.1504/IJBC.2022.126287>.
* Wątorek et al. (2023)

  Wątorek, M.; Kwapień, J.; Drożdż, S.
  Cryptocurrencies are becoming part of the world global financial market.
  Entropy 2023, 25, 377.
  <https://doi.org/10.3390/e25020377>.
* Kristjanpoller and Tabak (2025)

  Kristjanpoller, W.; Tabak, B.M.
  Multifractal Cross-Correlations of Dirty and Clean Cryptocurrencies with main financial indices.
  Physica A 2025, 668, 130541.
  <https://doi.org/https://doi.org/10.1016/j.physa.2025.130541>.
* Li et al. (2025)

  Li, J.C.; Xu, Y.Z.; Tao, C.; Zhong, G.Y.
  Multi-period impacts and network connectivity of cryptocurrencies to international stock markets.
  Physica A 2025, 658, 130299.
  <https://doi.org/https://doi.org/10.1016/j.physa.2024.130299>.
* Nguyen et al. (2025)

  Nguyen, A.P.N.; Crane, M.; Conlon, T.; Bezbradica, M.
  Herding unmasked: Insights into cryptocurrencies, stocks and US ETFs.
  PloS one 2025, 20, e0316332.
  <https://doi.org/10.1371/journal.pone.0316332>.
* Bouri et al. (2022)

  Bouri, E.; Gupta, R.; Vo, X.V.
  Jumps in Geopolitical Risk and the Cryptocurrency Market: The Singularity of Bitcoin.
  Defence and Peace Economics 2022, 33, 150–161.
  <https://doi.org/10.1080/10242694.2020.1848285>.
* Hong and Yoon (2022)

  Hong, M.Y.; Yoon, J.W.
  The impact of COVID-19 on cryptocurrency markets: A network analysis based on mutual information.
  PLoS ONE 2022, 17.
  <https://doi.org/10.1371/journal.pone.0259869>.
* Khalfaoui et al. (2023)

  Khalfaoui, R.; Gozgor, G.; Goodell, J.W.
  Impact of Russia-Ukraine war attention on cryptocurrency: Evidence from quantile dependence analysis.
  Finance Research Letters 2023, 52, 103365.
  <https://doi.org/10.1016/j.frl.2022.103365>.
* Fang et al. (2024)

  Fang, Y.; Tang, Q.; Wang, Y.
  Geopolitical Risk and Cryptocurrency Market Volatility.
  Emerging Markets Finance and Trade 2024, 60, 3254–3270.
  <https://doi.org/10.1080/1540496X.2024.2343948>.
* Poongodi et al. (2021)

  Poongodi, M.; Nguyen, T.N.; Hamdi, M.; Cengiz, K.
  Global cryptocurrency trend prediction using social media.
  Information Processing and Management 2021, 58, 102708.
  <https://doi.org/10.1016/j.ipm.2021.102708>.
* Aharon et al. (2022)

  Aharon, D.Y.; Demir, E.; Lau, C.K.M.; Zaremba, A.
  Twitter-Based uncertainty and cryptocurrency returns.
  Research in International Business and Finance 2022, 59, 101546.
  <https://doi.org/10.1016/j.ribaf.2021.101546>.
* Oświęcimka et al. (2013)

  Oświęcimka, P.; Drożdż, S.; Kwapień, J.; Górski, A.Z.
  Effect of Detrending on Multifractal Characteristics.
  Acta Physica Polonica A 2013, 123, 597–603.
  <https://doi.org/10.12693/APhysPolA.123.597>.
* Johnson (1974)

  Johnson, C.R.
  Hadamard products of matrices.
  Linear and Multilinear Algebra 1974, 1, 295–307.
  <https://doi.org/10.1080/03081087408817030>.
* FitzGerald and Horn (1977)

  FitzGerald, C.H.; Horn, R.A.
  On Fractional Hadamard Powers of Positive Definite Matrices.
  Journal of Mathematical Analysis and Applications 1977, 61, 633–342.
  <https://doi.org/10.1016/0022-247X(77)90167-6>.
* Wishart (1928)

  Wishart, J.
  The Generalised Product Moment Distribution in Samples from a Normal Multivariate Population.
  Biometrika 1928, 20A, 32–52.
  <https://doi.org/0.1093/biomet/20A.1-2.32>.
* Wątorek et al. (2021)

  Wątorek, M.; Kwapień, J.; Drożdż, S.
  Financial return distributions: Past, present, and covid-19.
  Entropy 2021, 23, 884.
  <https://doi.org/10.3390/e23070884>.
* Gopikrishnan et al. (1998)

  Gopikrishnan, P.; Meyer, M.; Amaral, L.N.; Stanley, H.E.
  Inverse cubic law for the distribution of stock price variations.
  The European Physical Journal B 1998, 3, 139–140.
  <https://doi.org/10.1007/s100510050292>.
* James et al. (2021)

  James, N.; Menzies, M.; Chan, J.
  Changes to the extreme and erratic behaviour of cryptocurrencies during COVID-19.
  Physica A 2021, 565, 125581.
  <https://doi.org/10.1016/j.physa.2020.125581>.
* Drożdż et al. (2023)

  Drożdż, S.; Kwapień, J.; Wątorek, M.
  What is mature and what is still emerging in the cryptocurrency market?
  Entropy 2023, 25.
  <https://doi.org/10.1080/713665670>.
* Tsallis (2009)

  Tsallis, C.
  Nonadditive entropy and nonextensive statistical mechanics -an overview after 20 years.
  Brazilian Journal of Physics 2009, 39, 337–356.
  <https://doi.org/10.1590/s0103-97332009000400002>.
* Tsallis et al. (1995)

  Tsallis, C.; Levy, S.V.F.; Souza, A.M.C.; Maynard, R.
  Statistical-Mechanical Foundation of the Ubiquity of Lévy Distributions in Nature.
  Physical Review Letters 1995, 75, 3589–3593.
  <https://doi.org/10.1103/physrevlett.75.3589>.
* Drożdż et al. (2010)

  Drożdż, S.; Kwapień, J.; Oświęcimka, P.; Rak, R.
  The foreign exchange market: Return distributions, multifractality, anomalous multifractality and the Epps effect.
  New Journal of Physics 2010, 12, 105003.
  <https://doi.org/10.1088/1367-2630/12/10/105003>.
* Drożdż and Wójcik (2001)

  Drożdż, S.; Wójcik, M.
  Nature of order from random two-body interactions.
  Physica A 2001, 301, 291–300.
  <https://doi.org/10.1016/S0378-4371(01)00403-4>.
* Drożdż et al. (2002)

  Drożdż, S.; Kwapień, J.; Speth, J.; Wójcik, M.
  Identifying complexity by means of matrices.
  Physica A 2002, 314, 355–361.
  <https://doi.org/10.1016/S0378-4371(02)01066-X>.
* Guhr and Kälber (2003)

  Guhr, T.; Kälber, B.
  A new method to estimate the noise in financial correlation matrices.
  Journal of Physics A 2003, 36, 3009.
  <https://doi.org/10.1088/0305-4470/36/12/310>.
* (101)

  A dataset of 140 exchange rates from the Binance exchange.
  <https://doi.org/10.18150/WPGY4R>.
* Epps (1979)

  Epps, T.W.
  Comovements in Stock Prices in the Very Short Run.
  Journal of the American Statistical Association 1979, 74, 291–298.
  <https://doi.org/10.1080/01621459.1979.10482508>.
* Kwapień et al. (2004)

  Kwapień, J.; Drożdż, S.; Speth, J.
  Time scales involved in emergent market coherence.
  Physica A 2004, 337, 231–242.
  <https://doi.org/10.1016/j.physa.2004.01.050.>
* Wątorek et al. (2019)

  Wątorek, M.; Drożdż, S.; Oświęcimka, P.; Stanuszek, M.
  Multifractal cross-correlations between the world oil and other financial markets in 2012–2017.
  Energy Economics 2019, 81, 874–885.
  <https://doi.org/10.1016/j.eneco.2019.05.015>.
* Haken (2004)

  Haken, H.
  Synergetics: Introduction and Advanced Topics – Nonequilibrium Phase Transitions and Self-Organization in Physics, Chemistry and Biology; Springer, 2004.
  <https://doi.org/10.1007/978-3-662-10184-1>.