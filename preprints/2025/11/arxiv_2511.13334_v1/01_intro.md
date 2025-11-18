---
authors:
- Florent Segonne
doc_id: arxiv:2511.13334v1
family_id: arxiv:2511.13334
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Basis Immunity: Isotropy as a Regularizer for Uncertainty'
url_abs: http://arxiv.org/abs/2511.13334v1
url_html: https://arxiv.org/html/2511.13334v1
venue: arXiv q-fin
version: 1
year: 2025
---


Florent Ségonne
 The author would like to thank the 80 Technologies research team, especially M. Lapides and L. Jeannerod.
  
 Contact email: quantbasics101@gmail.com    —    Affiliation: WorkMotion

(November 2025)

Diversification is a cornerstone of robust portfolio construction, yet its application remains fraught with challenges due to model uncertainty and estimation errors. Practitioners often rely on sophisticated, proprietary heuristics to navigate these issues. Among recent advancements, Agnostic Risk Parity [benichou-16] introduces eigenrisk parity (ERP), an innovative approach that leverages isotropy to evenly allocate risk across eigenmodes, enhancing portfolio stability.

In this paper, we review and extend the isotropy-enforced philosophy of ERP proposing a versatile framework that integrates mean-variance optimization with an isotropy constraint acting as a geometric regularizer against signal uncertainty. The resulting allocations decompose naturally into *canonical portfolios* [CanonicalPortfolios2023], smoothly interpolating between full isotropy (closed-form isotropic-mean allocation) and pure mean-variance through a tunable isotropy penalty.

Beyond methodology, we revisit fundamental concepts and clarify foundational links between isotropy, canonical portfolios [CanonicalPortfolios2023], principal portfolios [PrincipalPortfolios2020], primal versus dual representations, and intrinsic basis-invariant metrics for returns, risk, and isotropy. Applied to sector trend-following [Grebenkov\_2015], the isotropy constraint systematically induces *negative average-signal exposure*—a structural, parameter-robust crash hedge.

This work offers both a practical, theoretically grounded tool for resilient allocation under signal uncertainty and a pedagogical synthesis of modern portfolio concepts.

Notations



ℛn​nreturn covariance =E​[𝒓​𝒓T]ℛm​msignal covariance =E​[𝒔​𝒔T]ℛn​mreturn/signal cross-covariance =E​[𝒓​𝒔T]tilde=−12−12normalized predictability𝒓=𝒔+regressing -assumption joint normal=E​[𝒓​𝒔]​E​[𝒔​𝒔]−1=−1E​[𝒓|𝒔]=𝒔=−1𝒔​𝒘=𝑳​𝒔positions: ​𝒘​ℛn,𝑳​ℛm​n𝒘​𝒓next-step PnL: ​𝒘​𝒓=𝒔​𝑳​𝒓E​[𝒘​𝒓]=Tr​(𝑳)​Var​[𝒘​𝒓]=Tr​(𝑳​𝑳)+Tr​(𝑳​𝑳)​𝑴nThe first-left n-vector columns of matrix M𝑴mThe last-right m-vector columns of matrix M|{𝒆𝒊𝒓}natural basis for returns{𝒆𝒊𝒔}natural basis for signals{𝒃bar}&{𝒖bar}pca basis =𝑩bar​𝑩bar&=𝑼bar​𝑼bar​{𝒃𝒊}Riccati basis ​𝒃i=−12𝒆𝒊𝒓​{𝒖𝒊}Riccati basis ​𝒖i=−12𝒆𝒊𝒔{𝒃hat𝒊}Isotropic basis ​𝒃hat𝒊=−12Rbhat​𝒆𝒊𝒓{𝒖hat𝒊}Isotropic basis ​𝒖hat𝒊=−12Ruhat​𝒆𝒊𝒔Used Singular Value Decompositions m​n,𝑴​ℛm​nb​u=tilde𝑩tilde​tilde​𝑼tilde=𝑩tilde​tilden​𝑼tilden​bhat​uhat=Rbhatb​uRuhat(Rbhat​𝑩tilde)​tilde​(Ruhat​𝑼tilde)​−12+12𝑩hat​hat​𝑼hat−12(𝑴𝑴)+12𝑩check​check​𝑼check​ ( same as 𝑩hat​hat​𝑼hat when 𝑴=I​d)−12𝑴+12𝑩dot​dot​𝑼dot​ ( same as 𝑩tilde​tilde​𝑼tilde when 𝑴=)\displaystyle\begin{array}[]{cc}\boldsymbol{\Omega}\in\mathcal{R}^{n\times n}&\text{return covariance }\boldsymbol{\Omega}=E[\boldsymbol{r}\boldsymbol{r}^{T}]\\
\boldsymbol{\Xi}\in\mathcal{R}^{m\times m}&\text{signal covariance }\boldsymbol{\Xi}=E[\boldsymbol{s}\boldsymbol{s}^{T}]\\
\boldsymbol{\Pi}\in\mathcal{R}^{n\times m}&\text{return/signal cross-covariance\ }\boldsymbol{\Pi}=E[\boldsymbol{r}\boldsymbol{s}^{T}]\\
\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}&\text{normalized predictability}\\
\\
\boldsymbol{r}=\boldsymbol{\beta}\boldsymbol{s}+\boldsymbol{\epsilon}&\text{regressing -assumption joint normal}\\
&\boldsymbol{\beta}=E\left[\boldsymbol{r}\boldsymbol{s}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\right]E\left[\boldsymbol{s}\boldsymbol{s}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\right]^{-1}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
&E[\boldsymbol{r}|\boldsymbol{s}]=\boldsymbol{\beta}\boldsymbol{s}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\\
\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}&\text{positions: }\boldsymbol{w}\in\mathcal{R}^{n}\ ,\boldsymbol{L}\in\mathcal{R}^{m\times n}\\
\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}&\text{next-step PnL: }\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}=\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\\
&E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]=\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
&\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]=\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)+\text{Tr}\left(\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{M}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}&\text{The first-left $n$-vector columns of matrix $M$}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{M}\_{\stackrel{{\scriptstyle\leftarrow}}{{m}}}&\text{The last-right $m$-vector columns of matrix $M$}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\end{array}\left|\begin{array}[]{cc}\{\boldsymbol{e\_{i}^{r}}\}&\text{natural basis for returns}\\
\{\boldsymbol{e\_{i}^{s}}\}&\text{natural basis for signals}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\{\boldsymbol{\bar{b}}\}\ \&\ \{\boldsymbol{\bar{u}}\}&\text{pca basis }\boldsymbol{\Omega}=\boldsymbol{\bar{B}}\boldsymbol{\Sigma}\boldsymbol{\bar{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \&\ \boldsymbol{\Xi}=\boldsymbol{\bar{U}}\boldsymbol{\Lambda}\boldsymbol{\bar{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\{\boldsymbol{b\_{i}}\}&\text{Riccati basis }\boldsymbol{b}\_{i}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{e\_{i}^{r}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\{\boldsymbol{u\_{i}}\}&\text{Riccati basis }\boldsymbol{u}\_{i}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{e\_{i}^{s}}\\
\{\boldsymbol{\hat{b}\_{i}}\}&\text{Isotropic basis }\boldsymbol{\hat{b}\_{i}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{e\_{i}^{r}}\\
\{\boldsymbol{\hat{u}\_{i}}\}&\text{Isotropic basis }\boldsymbol{\hat{u}\_{i}}=\boldsymbol{\Xi}^{-\frac{1}{2}}\mathbb{R}\_{\hat{u}}\boldsymbol{e\_{i}^{s}}\\
\\
\lx@intercol\hfil\textbf{Used Singular Value Decompositions $m\geq n,\ \boldsymbol{M}\in\mathcal{R}^{m\times n}$}\hfil\lx@intercol\\
\\
\boldsymbol{\Pi}\_{bu}=\boldsymbol{\tilde{\Pi}}&\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\Pi}\_{\hat{b}\hat{u}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\_{bu}\mathbb{R}\_{\hat{u}}&\left(\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{B}}\right)\boldsymbol{\tilde{\Psi}}\left(\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{U}}\right)^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{+\frac{1}{2}}&\boldsymbol{\hat{B}}\boldsymbol{\hat{\Psi}}\boldsymbol{\hat{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\\
\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\right)^{+\frac{1}{2}}&\boldsymbol{\check{B}}\boldsymbol{\check{\Psi}}\boldsymbol{\check{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \text{ ( same as $\boldsymbol{\hat{B}}\boldsymbol{\hat{\Psi}}\boldsymbol{\hat{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}$ when $\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\mathbb{Id}$)}\\
\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}&\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\boldsymbol{\dot{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \text{ ( same as $\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}$ when $\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\beta}$)}\\
\end{array}\right.

## 1 Introduction

### 1.1 Motivation

Risk management is a fundamental pillar of quantitative finance, with diversification serving as a primary strategy to reduce portfolio volatility and safeguard capital against market uncertainties.
Traditional diversification methods, such as Markowitz’s mean-variance optimization [markowitz\_1, markowitz\_2], rely on precise estimates of expected returns and covariances—assumptions that often fail in practice due to market non-stationarity and estimation errors.

These well-known limitations (see Section [2.2.3](https://arxiv.org/html/2511.13334v1#S2.SS2.SSS3 "2.2.3 Mean-Variance Limitations ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")), consistently highlighted in the literature (e.g. [ChoueifatyCoignard2008, BruderRoncalli2012, Meucci2015]), can lead to suboptimal risk allocations and significant losses when market conditions shift, especially during periods of market stress. This underscores the need for more robust, uncertainty-aware approaches.

Specifically, the mean-variance optimization is very sensitive to errors in the input parameters, as expected returns are typically scaled up by the inverse covariance of the returns (see [Stevens-1998]).
Small changes can lead to significant portfolio variations, resulting in unstable or extreme weights (e.g. corner solutions where the portfolio heavily concentrates on a few assets, defeating the diversification goal).

Agnostic Risk Parity, introduced by Benichou et al [benichou-16], aims to address some of these challenges through the concept of eigenrisk parity (ERP), allocating risk equally across uncorrelated factors111All the while using cleaned covariance matrices to mitigate the impact of noisy data [bun-2016]
.
At its core, the approach enforces *isotropy* in both return and signal spaces to prevent error compounding across correlated dimensions.
This isotropic framework enables balanced risk contributions with minimal distortion, offering resilience to both known risks and “unknown unknowns,” and proving particularly effective in strategies like trend-following.

In this paper, we review and extend the isotropy philosophy beyond ERP, examining a broader class of portfolio allocation schemes that operate under uncertainty.
Our focus is narrow and precise: within a stochastic mean-variance setting (asset returns 𝒓\boldsymbol{r} and predictors 𝒔\boldsymbol{s} both random), we treat *signal uncertainty* as the dominant threat and use *isotropy* as a geometric regularizer — a principle we frame as *Basis Immunity* (BI).

Signal errors compound when correlated: “bad things go together” in the signal basis, and mean-variance optimization amplifies them by exploiting return correlations to reduce variance. To break this dual compounding, we penalize anisotropy in both spaces, decoupling all directions. The resulting *Isotropy-Regularized Mean-Variance* (IRMV) allocations decompose naturally into *canonical components* [CanonicalPortfolios2023] with:

* •

  Closed-form *Isotropic-Mean* (IM) solutions for full isotropy,
* •

  A *tunable isotropy penalty* yielding cubic equations that smoothly interpolate between mean-variance (MV) and isotropic-mean (IM).

The paper is organized as follows:

* •

  First, we define notations (Section [2.1](https://arxiv.org/html/2511.13334v1#S2.SS1 "2.1 Notations ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")) and review the general mean-variance framework when asset returns and signals are stochastic (Section [2.2](https://arxiv.org/html/2511.13334v1#S2.SS2 "2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). The theoretical MV solution serves as the starting point for constructing isotropy-regularized allocations.

  Before proceeding, we introduce the concept of *isotropic bases* (Section [2.3.3](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS3 "2.3.3 Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). This allows us to reinterpret the ERP approach of [benichou-16]—where equal risk per eigenvector is a *consequence* of enforced isotropy, not the objective—and extend it systematically. Canonical portfolios [CanonicalPortfolios2023], key building blocks of MV, are defined in Section [2.3.6](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS6 "2.3.6 Canonical Portfolios ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").
* •

  In Section [3](https://arxiv.org/html/2511.13334v1#S3 "3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we construct exact isotropy-enforced allocations in two steps: first the balanced case (as in [benichou-16]), then the general case with more signals than assets.
* •

  In Section [4](https://arxiv.org/html/2511.13334v1#S4 "4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we depart from “pure” isotropy and augment mean-variance with a penalty on anisotropy. This is the core of the paper, unifying isotropy, canonical portfolios, and basis-invariant risk design.
* •

  A compact illustration using sector trend-following [Grebenkov\_2015] appears in Section [5](https://arxiv.org/html/2511.13334v1#S5 "5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"); isotropy systematically induces *negative average-signal exposure*—a structural crash hedge.

We deliberately omit empirical studies.
As any practitioner knows, the success of an investment strategy depends not only on the framework, but on countless implementation details—context-dependent, proprietary, and beyond the scope of this work.

However, by providing a comprehensive theoretical foundation, we aim to equip portfolio managers with tools to navigate the complexities of modern financial markets with greater confidence and resilience.

## 2 Setting up the scene

### 2.1 Notations

We consider the natural basis {𝒆𝒊𝒓}\{\boldsymbol{e\_{i}^{r}}\} of nn assets. A vector 𝒘​ℛn\boldsymbol{w}\in\mathcal{R}^{n} represents a portfolio allocation \slimits@​wi​𝒆𝒊𝒓\sumop\slimits@{w\_{i}\boldsymbol{e\_{i}^{r}}} across all assets, where wiw\_{i} is the percentage weight into asset SiS^{i}. The positions are derived from some signals 𝒔​ℛm\boldsymbol{s}\in\mathcal{R}^{m}. Over the next interval, the allocation 𝒘\boldsymbol{w} generates a PnL \slimits@​wi​ri\sumop\slimits@{w\_{i}r\_{i}} where rir\_{i} is the next-step return of SiS^{i}.

We work in an idealized framework where the stochastic variables of interest, i.e. the asset returns 𝒓​ℛn\boldsymbol{r}\in\mathcal{R}^{n} and the signals 𝒔​ℛm\boldsymbol{s}\in\mathcal{R}^{m}, are centered (i.e. of null unconditional expectation E​[𝒓]=E​[𝒔]=𝟎E[\boldsymbol{r}]=E[\boldsymbol{s}]=\boldsymbol{0}) and jointly normal. Furthermore, we assume that the quantities, such as conditional expectations or second-order moments, are well-estimated (potentially through regularization methods, such as linear shrinkage [LedoitWolf2004b], or other techniques, e.g. correlation cleaning [bun-2016], factor models [meucci-book, paleo-book2]).

The natural basis {𝒆𝒊𝒓}\{\boldsymbol{e\_{i}^{r}}\} is embedded with an inner product defined by the assets’ covariance structure:

|  |  |  |
| --- | --- | --- |
|  | 𝒆𝒊𝒓𝒆𝒋𝒓=E[𝒓𝒊𝒓𝒋]=i,j\boldsymbol{e\_{i}^{r}}\vysmblkcircle\boldsymbol{e\_{j}^{r}}=E[\boldsymbol{r\_{i}}\boldsymbol{r\_{j}}]={}\_{i,j} |  |

where 𝒓𝒊\boldsymbol{r\_{i}} is the return of the ithi^{\text{th}} asset.
A given position 𝒘\boldsymbol{w} generates a PnL 𝒘​𝒓\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r} with unconditional variance:

|  |  |  |
| --- | --- | --- |
|  | Var​[𝒘​𝒓]=𝒘​𝒘=𝒘​𝒘,\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]=\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}\boldsymbol{w}=\boldsymbol{w}\vysmblkcircle\boldsymbol{w}, |  |

where =E​[𝒓​𝒓]\boldsymbol{\Omega}=E[\boldsymbol{r}\boldsymbol{r}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}] is the covariance matrix of assets’ returns ( is symmetric definite positive). This defines a Hilbert space that we denote ℋr\mathcal{H}\_{r}.

The signals 𝒔​ℛm\boldsymbol{s}\in\mathcal{R}^{m} used to predict future returns are known on time for trading, that is before the realization of 𝒓\boldsymbol{r}. The information up to that time is captured by the filtration and denoted ℱ\mathcal{F} (e.g. the conditional expectation E​[𝒓|𝒔]=E​[𝒓|ℱ]E[\boldsymbol{r}|\boldsymbol{s}]=E[\boldsymbol{r}|\mathcal{F}]). We denote by =E​[𝒔​𝒔]\boldsymbol{\Xi}=E[\boldsymbol{s}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}] the signals’ covariance, which we also assume to be definite positive222When the signals are not linearly independent, we pre-process them and remove the linear dependencies.
 (the signal Hilbert space is denoted ℋs\mathcal{H}\_{s}).

In full generality, we do not assume m=nm=n. Several situations can be considered:

* •

  m<nm<n: less signals than assets. The features are typically aggregated factors, common to all assets, like macroeconomic variables (e.g. market volatility, unemployment rates, GPD growth rate, interest rate changes or yield curve slopes) or sector-level metrics (e.g. average sector valuation). We do not consider this case.
* •

  m=nm=n: when the number of signals equals the number of assets, each signal sis\_{i} is often specifically “designed” to predict the future return rir\_{i} of a corresponding asset (so that E​[si​ri]​0E[s\_{i}r\_{i}]\geq 0). We note that the case where signals are linearly combined as 𝒛=𝑴​𝒔\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} with 𝑴​ℛn​m\boldsymbol{M}\in\mathcal{R}^{n\times m} a given matrix, could be similarly tackled by working with the signals ziz\_{i} directly.
* •

  m>nm>n: this typical scenario where signals outnumber assets leverages high-dimensional datasets, including technical indicators (e.g. trends [Grebenkov\_2014], volume changes, Bollinger bands, carry [BaltasCarry2017, KoijenCarry2016]), alternative data (e.g. social media sentiment), and machine learning-derived features. In this general setting, common aggregated factors could also be included.

In this work, we only focus on the more common scenario m​nm\geq n.

The cross-covariance between returns and signals is denoted by =E​[𝒓​𝒔]\boldsymbol{\Pi}=E[\boldsymbol{r}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]. It is also termed the predictability matrix since it is a measure of the signal-return predictability. We note that it is typically not symmetric (even when m=nm=n), as the predictive strength of a signal i on asset j may be different from that of signal j on asset i. The accurate estimation of is difficult, where the source of uncertainty mainly lies.

𝒔​Rm=E​[𝒔​𝒔]\begin{array}[]{c}\boldsymbol{s}\in\mathbb{R}^{m}\\
\boldsymbol{\Xi}=E[\boldsymbol{s}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]\end{array}Signals ℋs\mathcal{H}\_{s}𝒓​Rn=E​[𝒓​𝒓]\begin{array}[]{c}\boldsymbol{r}\in\mathbb{R}^{n}\\
\boldsymbol{\Omega}=E[\boldsymbol{r}\boldsymbol{r}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]\end{array}Assets ℋr\mathcal{H}\_{r}𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}Trading=E​[𝒓​𝒔]\Pi=E[\boldsymbol{r}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]Predictability

### 2.2 Trading: Mean-Variance Framework

We suggest to trade the assets with some positions 𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} where the matrix 𝑳\boldsymbol{L} is of size m​nm\times n. At 𝑳\boldsymbol{L} fixed and given, the positions 𝒘\boldsymbol{w} become stochastic variables, functions of the signal realizations 𝒔\boldsymbol{s}. The operator 𝑳\boldsymbol{L} is typically chosen so as to maximize some objective function over the joint dynamics of signals and returns.

In this work, we consider a standard mean-variance framework where the functional to optimize is expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[𝒘​𝒓]−2​Var​[𝒘​𝒓],\displaystyle E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]-\frac{\gamma}{2}\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right], |  | (2) |

with a Lagrange coefficient used to set an expected level of risk. Thanks to our Gaussian assumptions (i.e. 𝒓\boldsymbol{r} and 𝒔\boldsymbol{s} being jointly normal), the different expectations (conditional and unconditional) can be computed efficiently in closed-form.

Some straight-forward calculations show that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[𝒘​𝒓]=E​[𝒔​𝑳​𝒓]=Tr​(𝑳)\displaystyle E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]=E\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]=\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right) |  | (3) |

The expectation is taken over asset returns 𝒓\boldsymbol{r} and signals 𝒔\boldsymbol{s}, which are both stochastic variables (again, assumed to centered and jointly normal). This is can be compared to the conditional expectation at signal fixed:

|  |  |  |
| --- | --- | --- |
|  | E​[𝒘​𝒓|𝒔]=𝒘​E​[𝒓|𝒔]=𝒘−1​𝒔E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}|\boldsymbol{s}]=\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}E[\boldsymbol{r}|\boldsymbol{s}]=\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s} |  |

We quickly verify that:

|  |  |  |
| --- | --- | --- |
|  | E​[𝒘​𝒓]=E​[𝒘​E​[𝒓|𝒔]]=E​[𝒔​𝑳−1​𝒔]=Tr​(𝑳)E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]=E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}E[\boldsymbol{r}|\boldsymbol{s}]\right]=E[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}]=\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right) |  |

The variance is slightly more challenging to compute. As we assume that all the variables of interest are centered Gaussian vectors, we can use the following identity for centered Gaussian variables (known as Wick’s theorem or Isserlis’ theorem):

|  |  |  |
| --- | --- | --- |
|  | E​[z1​z2​z3​z4]=E​[z1​z2]​E​[z3​z4]+E​[z1​z3]​E​[z2​z4]+E​[z1​z4]​E​[z2​z3]E[z\_{1}z\_{2}z\_{3}z\_{4}]=E[z\_{1}z\_{2}]E[z\_{3}z\_{4}]+E[z\_{1}z\_{3}]E[z\_{2}z\_{4}]+E[z\_{1}z\_{4}]E[z\_{2}z\_{3}] |  |

We find that:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Var​[𝒘​𝒓]\displaystyle\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right] | =\displaystyle= | E​[(𝒘​𝒓)2]−E​[𝒘​𝒓]2\displaystyle E\left[\left(\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right)^{2}\right]-E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]^{2} |  | (4) |
|  |  | =\displaystyle= | \slimits@i,j,k,l​Li,j​Lk,l​E​[si​sk​rj​rl]−Tr​(𝑳)2\displaystyle\sumop\slimits@\_{i,j,k,l}{L\_{i,j}L\_{k,l}E\left[s\_{i}s\_{k}r\_{j}r\_{l}\right]}-\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right)^{2} |  |
|  |  | =\displaystyle= | \slimits@i,j,k,l​Li,j​Lk,l​(E​[si​sk]​E​[rj​rl]+E​[si​rl]​E​[rj​sk])\displaystyle\sumop\slimits@\_{i,j,k,l}{L\_{i,j}L\_{k,l}\left(E[s\_{i}s\_{k}]E[r\_{j}r\_{l}]+E[s\_{i}r\_{l}]E[r\_{j}s\_{k}]\right)} |  |
|  |  | =\displaystyle= | Tr​(𝑳​𝑳)+Tr​(𝑳​𝑳)\displaystyle\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)+\text{Tr}\left(\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L}\right) |  |

The second term is typically much smaller than the first one (as it contains squared cross-correlations). This is almost always the case but would need to be checked in practice (see Section [5](https://arxiv.org/html/2511.13334v1#S5 "5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") in the case of a simple trend-following model, particularly Figure [5.2.4](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS4 "5.2.4 Validating the Closed-Form Solution Eq. 121 ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). Ignoring it is usually a sensible choice, while having the great advantage of leading to interpretable close-form solutions. In this work, we neglect it and focus only on the first part:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​[𝒘​𝒓]​Tr​(𝑳​𝑳)\displaystyle\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]\approx\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right) |  | (5) |

The conditional variance could also be computed as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​[𝒘​𝒓|𝒔]\displaystyle\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}|\boldsymbol{s}] | =\displaystyle= | 𝒘​(−−1)​𝒘\displaystyle\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\left(\boldsymbol{\Omega}-\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)\boldsymbol{w} |  |

and we can easily verify the law of total variance:

|  |  |  |
| --- | --- | --- |
|  | Var​[𝒘​𝒓]=E​[Var​[𝒘​𝒓|𝒔]]+Var​[E​[𝒘​𝒓|𝒔]]\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]=E[\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}|\boldsymbol{s}]]+\text{Var}[E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}|\boldsymbol{s}]] |  |

using E​[E​[𝒘​𝒓|𝒔]2]=Tr​(𝑳)2+Tr​(𝑳−1​𝑳+𝑳​𝑳)E[E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}|\boldsymbol{s}]^{2}]=\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right)^{2}+\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}+\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Xi}\boldsymbol{L}\right).

#### 2.2.1 Mean-Variance Functional and Solution

The standard mean-variance functional can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg𝑳⁡max⁡Tr​(𝑳)−2​Tr​(𝑳​𝑳),\displaystyle\arg\_{\boldsymbol{L}}\max\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right)-\frac{\gamma}{2}\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right), |  | (6) |

with first-order condition:

|  |  |  |
| --- | --- | --- |
|  | =𝑳\boldsymbol{\Pi}=\gamma\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi} |  |

This leads to the general solution 𝑳=1−1−1\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1} and the we finally obtain:

General Mean-Variance


𝒘=𝑳​𝒔=1−1−1​𝒔\displaystyle\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}

(7)

The risk is generally calibrated through the Lagrange coefficient to a target variance 2, so that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =212Tr(−1−1)=12Tr(tildetilde)\displaystyle{}^{2}=\frac{1}{{}^{2}}\text{Tr}\left(\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\right)=\frac{1}{{}^{2}}\text{Tr}\left(\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right) |  | (8) |

where tilde=−12−12\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}, the normalized predictability matrix (a key element of the framework).

Even though we worked in the natural asset basis, the mean-variance framework could be expressed anywhere. The resulting solution Eq [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") is totally invariant to the choice of basis. This is obviously the case because the definition of expected returns in Eq [3](https://arxiv.org/html/2511.13334v1#S2.E3 "In 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and the variance in Eq. [4](https://arxiv.org/html/2511.13334v1#S2.E4 "In 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") is intrinsic, that is independent from the choice of coordinates.

#### 2.2.2 The Regression Angle

Eq. [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") does not appear out of nowhere. There is a clear link between this approach and a standard regression problem where one tries to regress the returns 𝒓\boldsymbol{r} onto a set of predictors 𝒔\boldsymbol{s}:

|  |  |  |
| --- | --- | --- |
|  | 𝒓=𝒔+\boldsymbol{r}=\boldsymbol{\beta}\boldsymbol{s}+\boldsymbol{\epsilon} |  |

Under standard Gaussian assumptions, we find that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =E[𝒓𝒔]E[𝒔𝒔]−1=−1andE[𝒓|ℱ]=E[𝒓|𝒔]=𝒔\displaystyle\boldsymbol{\beta}=E\left[\boldsymbol{r}\boldsymbol{s}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\right]E\left[\boldsymbol{s}\boldsymbol{s}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\right]^{-1}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\ \ \text{and}\ \ E[\boldsymbol{r}|\mathcal{F}]=E\left[\boldsymbol{r}|\boldsymbol{s}\right]=\boldsymbol{\beta}\boldsymbol{s} |  | (9) |

and the solution of Eq. [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"):

|  |  |  |
| --- | --- | --- |
|  | 𝒘=1−1​𝒔=1−1−1​𝒔\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{\beta}\boldsymbol{s}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s} |  |

appears naturally.
The closed-form expression of Eq. [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), which we typically express as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘=1−1​E​[𝒓|ℱ]\displaystyle\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}E[\boldsymbol{r}|\mathcal{F}] |  | (10) |

is the starting point for constructing several isotropy-enforced portfolio allocations. Before we do so, we briefly review some of the limitations of the mean-variance framework.

#### 2.2.3 Mean-Variance Limitations

The formulations Eq. [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")-[10](https://arxiv.org/html/2511.13334v1#S2.E10 "In 2.2.2 The Regression Angle ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") can be used to review some of the well-documented limitations and challenges of the mean-variance approach. This also allows us to set the stage and explore how the concept of isotropy can be used to address some of these issues, particularly their robustness to signal uncertainty.

1. 1.

   Challenges with Covariance Estimation and Inversion

   Covariance matrices are notoriously difficult to estimate. Not enough samples and we are dealing with too much noise; too many samples and we are probably mixing different market dynamics.
   Inverting these matrices (see Eq. [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")) amplifies errors, especially for ill-conditioned matrices (e.g. highly correlated assets or small sample sizes). This can lead to numerical instability and unrealistic portfolio weights (for an enlightening discussion see [Stevens-1998]).

   Recent advances in the field of random matrix theory [bouchaudpotterslaloux2005, bouchaudpotters2009] have been proposed to mitigate those limitations [bun-2016]. In this work, we assume that the matrices and are accurate, well-estimated.
2. 2.

   Sensitivity to Input Estimates

   Mean-variance optimization is highly sensitive to errors in the covariance matrix and in the estimated expected returns E​[𝒓|ℱ]E[\boldsymbol{r}|\mathcal{F}] (that is implicitly in and , see Eq. [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). Small changes in these inputs can lead to significantly different portfolio allocations, resulting in unstable or extreme weights (e.g. corner solutions).

   Some (recent) techniques can greatly help with the estimates of covariances (e.g. linear shrinkage [LedoitWolf2004b], correlation cleaning [bun-2016], factor models [meucci-book, paleo-book2]), yet estimating expected returns and the predictability matrix remains problematic.
3. 3.

   Stability/Market Regime

   Market conditions evolve rapidly, undermining the stability of in-sample estimates. This is a core challenge in quantitative finance, and the mean-variance framework is particularly vulnerable.
   Diversified portfolios may be less affected than concentrated ones, but resilience to uncertainty remains critical.
4. 4.

   Model Risk and Distributional Assumptions

   The mean-variance model relies on simplistic assumptions, including normally distributed returns, ignoring fat tails, skewness, and kurtosis prevalent in real-world markets. It also overlooks transaction costs, constraints, and parameter uncertainty. This leads to overly optimistic risk-return trade-offs and underestimation of extreme risks (e.g. black swan events).

Practitioners address these well-known limitations by integrating mean-variance principles with proprietary practical adjustments informed by years of experience. Rigorous implementation is vital for real-world success.

Our approach, named Isotropy-Regularized Mean-Variance (IRMV), does not aim at resolving all mean-variance limitations but specifically targets sensitivity to input estimates and out-of-sample instability (mostly point 2 and arguably point 3). By emphasizing resilience to uncertainty—unmeasurable randomness distinct from quantifiable risk — they reduce dependence on mis-specified signals.

Built on the concept of isotropic bases, in the spirit of [benichou-16], they offer a pathway to stable portfolio construction in unpredictable markets. To explore this alternative, we first need a bit of algebra to understand how to change perspective.

### 2.3 Changing Perspective

The natural basis {𝒆𝒊𝒓}\{\boldsymbol{e\_{i}^{r}}\} of ℋr\mathcal{H}\_{r} is not orthonormal for the inner product (except if the covariance matrix is the identity matrix). Nothing prevents us from working in a different basis. In the following, we denote the belonging to a basis by the corresponding subscript (except at times for the natural basis when there is no ambiguity).

#### 2.3.1 Change of Basis

We consider a general basis {𝒚𝒊}\{\boldsymbol{y\_{i}}\} of ℋr\mathcal{H}\_{r} defined by an invertible transformation 𝒀\boldsymbol{Y}: the automorphism 𝒘y​𝒀​𝒘y\boldsymbol{w}\_{y}\mapsto\boldsymbol{Y}\boldsymbol{w}\_{y} is the change of coordinate operator that takes us from the basis {𝒚i}\{\boldsymbol{y}\_{i}\} into the natural basis {𝒆𝒊}\{\boldsymbol{e\_{i}}\}, i.e. a vector with coordinates 𝒘y\boldsymbol{w}\_{y} in {𝒚i}\{\boldsymbol{y}\_{i}\} has coordinates 𝒘e=𝒀​𝒘y\boldsymbol{w}\_{e}=\boldsymbol{Y}\boldsymbol{w}\_{y} in {𝒆𝒊}\{\boldsymbol{e\_{i}}\}. With an abuse of notation333One needs to be careful with this (abuse of) notation, particularly when working with more than 2 bases. For example, if 𝒇i=𝑭​𝒆i\boldsymbol{f}\_{i}=\boldsymbol{F}\boldsymbol{e}\_{i} and 𝒈i=𝑮​𝒇i\boldsymbol{g}\_{i}=\boldsymbol{G}\boldsymbol{f}\_{i} (i.e. the basis vector 𝒈i\boldsymbol{g}\_{i} has coordinates the ithi^{\text{th}}-column of 𝑮\boldsymbol{G} in the basis {𝒇i}\{\boldsymbol{f}\_{i}\}), then we have 𝒈i=(𝑭​𝑮)​𝒆i\boldsymbol{g}\_{i}=\left(\boldsymbol{F}\boldsymbol{G}\right)\boldsymbol{e}\_{i} (and certainly not 𝒈i=𝑮​𝑭​𝒆i\boldsymbol{g}\_{i}=\boldsymbol{G}\boldsymbol{F}\boldsymbol{e}\_{i} as a mis-interpretation of the abuse of notations could imply!).
, we say that the vector 𝒚i\boldsymbol{y}\_{i} whose coordinates in {𝒆𝒊}\{\boldsymbol{e\_{i}}\} are the ithi^{\text{th}}-column of 𝒀\boldsymbol{Y} is defined by 𝒚i=𝒀​𝒆i\boldsymbol{y}\_{i}=\boldsymbol{Y}\boldsymbol{e}\_{i}.

It is important to understand how our variables transform under changes of coordinates. First, we note that we are dealing with two distinct Hilbert spaces, the space ℋr\mathcal{H}\_{r} of asset returns 𝒓\boldsymbol{r} with inner product defined by and the space ℋs\mathcal{H}\_{s} of 𝒔\boldsymbol{s} with inner product defined by . The natural bases of ℋr\mathcal{H}\_{r} and of ℋs\mathcal{H}\_{s} are denoted by {𝒆ir}\{\boldsymbol{e}\_{i}^{r}\} and {𝒆is}\{\boldsymbol{e}\_{i}^{s}\} respectively, although we often drop the subscript for notional convenience.

The positions 𝒘\boldsymbol{w} are contravariant vectors of ℋr\mathcal{H}\_{r}, regular vectors of {𝒆𝒊}\{\boldsymbol{e\_{i}}\}, whereas returns 𝒓\boldsymbol{r} and signals 𝒔\boldsymbol{s} are covectors of ℋr\mathcal{H}\_{r} and ℋs\mathcal{H}\_{s}, i.e. they belong to the corresponding duals denoted ℋr\mathcal{H}\_{r} and ℋs\mathcal{H}\_{s}, with basis {𝒆𝒊𝒓}\{\boldsymbol{e^{r}\_{i}}\} and {𝒆𝒊𝒔}\{\boldsymbol{e^{s}\_{i}}\} (in the case where m=nm=n, both dual spaces can be identified together ℋr​ℋs\mathcal{H}\_{r}\sim\mathcal{H}\_{s}). To summarize the change of basis operations, we consider 𝒚𝒊=𝒀​𝒆𝒊𝒓\boldsymbol{y\_{i}}=\boldsymbol{Y}\boldsymbol{e\_{i}^{r}} of ℋr\mathcal{H}\_{r} and 𝒙𝒊=𝑿​𝒆𝒊𝒔\boldsymbol{x\_{i}}=\boldsymbol{X}\boldsymbol{e\_{i}^{s}} of ℋs\mathcal{H}\_{s} where 𝒀\boldsymbol{Y} and 𝑿\boldsymbol{X} are change of coordinate operators (i.e. invertible matrices):

|  |  |  |
| --- | --- | --- |
|  | 𝒆𝒊𝒓,𝒆𝒊𝒔𝒚𝒊=𝒀​𝒆𝒊𝒓,𝒙𝒊=𝑿​𝒆𝒊𝒔​𝒘𝒘y=𝒀−1​𝒘​𝒓,𝒔𝒓y=𝒀​𝒓,𝒔x=𝑿​𝒔​=E​[𝒓​𝒓]y=𝒀𝒀=E​[𝒔​𝒔]x=𝑿𝑿𝒘=𝑳​𝒔𝒘y=𝑳x​y​𝒔x​with​𝑳x​y=𝑿−1​𝑳​𝒀−​=E​[𝒓​𝒔]y​x=E[𝒓y𝒔x]=𝒀𝑿\displaystyle\begin{array}[]{| c | c |}\hline\cr\boldsymbol{e\_{i}^{r}}\ ,\ \boldsymbol{e\_{i}^{s}}&\boldsymbol{y\_{i}}=\boldsymbol{Y}\boldsymbol{e\_{i}^{r}}\ ,\ \boldsymbol{x\_{i}}=\boldsymbol{X}\boldsymbol{e\_{i}^{s}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{w}&\boldsymbol{w}\_{y}=\boldsymbol{Y}^{-1}\boldsymbol{w}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{r}\ ,\ \boldsymbol{s}&\boldsymbol{r}\_{y}=\boldsymbol{Y}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\ ,\ \boldsymbol{s}\_{x}=\boldsymbol{X}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{\Omega}=E[\boldsymbol{r}\boldsymbol{r}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]&\boldsymbol{\Omega}\_{y}=\boldsymbol{Y}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}\boldsymbol{Y}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{\Xi}=E[\boldsymbol{s}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]&\boldsymbol{\Xi}\_{x}=\boldsymbol{X}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{X}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}&\boldsymbol{w}\_{y}=\boldsymbol{L}\_{xy}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{x}\ \text{with}\ \boldsymbol{L}\_{xy}=\boldsymbol{X}^{-1}\boldsymbol{L}\boldsymbol{Y}^{-{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{\Pi}=E[\boldsymbol{r}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]&\boldsymbol{\Pi}\_{yx}=E[\boldsymbol{r}\_{y}\boldsymbol{s}\_{x}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]=\boldsymbol{Y}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\boldsymbol{X}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\end{array} |  |

As a sanity check, one can easily verify the following equalities: E​[𝒘y​𝒓y]=E​[𝒘​𝒓]E[\boldsymbol{w}\_{y}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\boldsymbol{r}\_{y}]=E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}], Tr​(𝑳x​yy​x)=Tr​(𝑳)\text{Tr}\left(\boldsymbol{L}\_{xy}\boldsymbol{\Pi}\_{yx}\right)=\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right), or Tr(x𝑳x​yy𝑳x​y)=Tr(𝑳𝑳)\text{Tr}\left(\boldsymbol{\Xi}\_{x}\boldsymbol{L}\_{xy}\boldsymbol{\Omega}\_{y}\boldsymbol{L}\_{xy}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)=\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right).

#### 2.3.2 Operator 𝑳\boldsymbol{L}

The operator 𝑳\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} takes us from the signal dual space ℋs​ℛm\mathcal{H}\_{s}\sim\mathcal{R}^{m} to the natural vector space ℋr​ℛn\mathcal{H}\_{r}\sim\mathcal{R}^{n}. It is enlightening to think of it as the combination of two steps:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑳=1​𝑷​𝑴\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{1}{\gamma}\boldsymbol{P}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  | (12) |

* •

  A mapping 𝑴\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} takes us from the dual ℋs​ℛm\mathcal{H}\_{s}\sim\mathcal{R}^{m} (where the signals live) to the dual ℋr​ℛn\mathcal{H}\_{r}\sim\mathcal{R}^{n} (where the returns live and where the positions are derived) with 𝒛=𝑴​𝒔\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}. The linear operator 𝑴\boldsymbol{M} is determined so that the mapped signals 𝒛\boldsymbol{z} are as predictive as possible of future returns 𝒓\boldsymbol{r}. The vector 𝒛\boldsymbol{z}, which is linearly constructed from the set of all signals 𝒔\boldsymbol{s}, is our best444Because we work in an idealized Gaussian setting, the best linear estimator is also the best estimator over all linear and non-linear operators (in the sense of the least-square distance).
   estimate/guess for E​[𝒓|ℱ]E[\boldsymbol{r}|\mathcal{F}].

  Many options are possible to obtain the mapping 𝑴\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}. As our best guess, it is not necessarily the best mapping in absolute and/or even within our framework. Many source of errors could creep in and the signals 𝒔\boldsymbol{s} could be mis-specified (known unknowns or unknown unknowns as described in [benichou-16]).

  To derive it, one could imagine using e.g. some deterministic relationships where some features 𝒔\boldsymbol{s} are explicitly designed/tailored for some assets (e.g. the carry of an asset), or some statistical estimation (typically through standard linear regressions/conditional expectations), or by directly integrating the unknown mapping 𝑴\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} into a general (e.g. mean-variance) functional as Eq. [2](https://arxiv.org/html/2511.13334v1#S2.E2 "In 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (as described in Section [2.2](https://arxiv.org/html/2511.13334v1#S2.SS2 "2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).
* •

  This first step is then followed by a transformation of the covector 𝒛​ℋr\boldsymbol{z}\in\mathcal{H}\_{r} (the space of returns) into a vector of tradable positions 𝒘=1​𝑷​𝒛​ℋr\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{P}\boldsymbol{z}\in\mathcal{H}\_{r}. This step depends on our choice of functional, which links dual and primal space together.

Working within the mean-variance framework corresponding to Eq. [2](https://arxiv.org/html/2511.13334v1#S2.E2 "In 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), the operator 𝑷\boldsymbol{P} is the decorrelation operator555For any vector 𝒛\boldsymbol{z} of the dual, representing our best estimate of future returns, we have the equality 𝒘E[𝒓|ℱ]=𝒘𝒛=𝒘(−1𝒛)\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}E[\boldsymbol{r}|\mathcal{F}]=\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{z}=\boldsymbol{w}\vysmblkcircle\left(\boldsymbol{\Omega}^{-1}\boldsymbol{z}\right).
 𝑷=−1\boldsymbol{P}=\boldsymbol{\Omega}^{-1}, while 𝑴\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} is a standard beta 𝑴=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\beta}.
The typical mean-variance allocation, which we use as a starting point, can be then expressed as:

Mean-Variance


𝒘e=1−1​E​[𝒓|ℱ]=1−1​𝑴​𝒔e\displaystyle\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}E[\boldsymbol{r}|\mathcal{F}]=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e}

(13)

Note that it could also be phrased in different bases of ℋs\mathcal{H}\_{s} and ℋr\mathcal{H}\_{r} without difficulty. For instance, in the two bases 𝒚𝒊=𝒀​𝒆𝒊𝒓\boldsymbol{y\_{i}}=\boldsymbol{Y}\boldsymbol{e\_{i}^{r}} of ℋr\mathcal{H}\_{r} and 𝒙𝒊=𝑿​𝒆𝒊𝒔\boldsymbol{x\_{i}}=\boldsymbol{X}\boldsymbol{e\_{i}^{s}} of ℋs\mathcal{H}\_{s}, we can easily check that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑴x​y=𝑿−1​𝑴​𝒀​and​𝑷y=𝒀−1​𝑷​𝒀−\displaystyle\boldsymbol{M}\_{xy}=\boldsymbol{X}^{-1}\boldsymbol{M}\boldsymbol{Y}\ \text{and}\ \boldsymbol{P}\_{y}=\boldsymbol{Y}^{-1}\boldsymbol{P}\boldsymbol{Y}^{-{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  | (14) |

so that we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘y=𝑳x​y​𝒔x=1​𝑷y​𝑴x​y​𝒔x\displaystyle\boldsymbol{w}\_{y}=\boldsymbol{L}\_{xy}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{x}=\frac{1}{\gamma}\boldsymbol{P}\_{y}\boldsymbol{M}\_{xy}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{x} |  | (15) |

As we already discussed, the mean in Eq [3](https://arxiv.org/html/2511.13334v1#S2.E3 "In 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and variance in Eq. [4](https://arxiv.org/html/2511.13334v1#S2.E4 "In 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") are intrinsic quantities and the mean-variance framework (in its simplest form, as in Eq [6](https://arxiv.org/html/2511.13334v1#S2.E6 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")) does not depend on the choice of basis666The addition of constraints, typically used in trading (e.g. limits on margin, on max trading, on max absolute positions, …), would obviously break this invariance property.
.

#### 2.3.3 Isotropic Bases

Some bases possess noticeable attractive properties. For example, let’s consider the one defined by 𝒃i=−12𝒆𝒊𝒓\boldsymbol{b}\_{i}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{e\_{i}^{r}} (also known as the Riccati root of ).
It is easy to see that {𝒃i}\{\boldsymbol{b}\_{i}\} is orthonormal (for the asset returns 𝒓b\boldsymbol{r}\_{b}).
From a variance perspective, it means that all directions are equivalent and carry the same risk: the space has become isotropic. This choice of basis is useful when aggregating signals together, since risk (as measured by the variance of the assets) is now the same in any direction. This is where the term “Eigenrisk Parity” comes from in [benichou-16].

The Riccati basis is not the only isotropic basis since any rotation of the basis would have the same property. In fact, one can show that all the isotropic basis are of the form 𝒃hati=−12Rbhat​𝒆ir\boldsymbol{\hat{b}}\_{i}=\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{e}\_{i}^{r} with Rbhat\mathbb{R}\_{\hat{b}} a rotation operator, i.e. Rbhat​Rbhat=Rbhat​Rbhat=I​d\mathbb{R}\_{\hat{b}}\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\mathbb{R}\_{\hat{b}}=\mathbb{Id}. The operator Rbhat\mathbb{R}\_{\hat{b}} belongs to the Special Orthogonal group, the set of rotations of Rn\mathbb{R}^{n} and denoted S​O​(n)SO(n), itself part of the orthogonal group, which includes rotations and symmetries and denoted O​(n)O(n).

For example, let’s consider the Cholesky decomposition of the covariance matrix =𝑳​𝑳\boldsymbol{\Omega}=\boldsymbol{L}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}
where 𝑳\boldsymbol{L} is a lower triangular matrix with positive coefficients on the diagonal. The Cholesky decomposition is unique and defines an isotropic basis 𝒃hati=𝑳−​𝒆i\boldsymbol{\hat{b}}\_{i}=\boldsymbol{L}^{-{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{e}\_{i}. One can easily show that 𝑳=12Rbhat\boldsymbol{L}=\boldsymbol{\Omega}^{\frac{1}{2}}\mathbb{R}\_{\hat{b}} where Rbhat\mathbb{R}\_{\hat{b}} is indeed a rotation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cholesky=𝑳​𝑳​𝑳=12Rbhat​and​𝒃hati=𝑳−​𝒆i​\displaystyle\textbf{Cholesky}\hskip 28.45274pt\begin{array}[]{c}\boldsymbol{\Omega}=\boldsymbol{L}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \boldsymbol{L}=\boldsymbol{\Omega}^{\frac{1}{2}}\mathbb{R}\_{\hat{b}}\ \text{and}\ \boldsymbol{\hat{b}}\_{i}=\boldsymbol{L}^{-{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{e}\_{i}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\hskip 28.45274pt |  | (18) |

Among all isotropic bases, the Riccati basis has the good behavior777The Cholesky basis might be preferred for a variety of reasons: slight computational efficiency, numerical stability, memory efficiency,
 of being the one that is the closest in the sense of the Mahalanobis distance D\text{D}\_{\boldsymbol{\Omega}}, as discussed in [benichou-16].
To show that, they consider the stochastic variable 𝒓𝒩(𝟎,)\boldsymbol{r}\sim\mathcal{N}(\boldsymbol{0},\boldsymbol{\Omega}), a centered Gaussian vector with covariance , and compare its expression across both bases as 𝒓e=𝒓\boldsymbol{r}\_{e}=\boldsymbol{r} in {𝒆ir}\{\boldsymbol{e}\_{i}^{r}\} and 𝒓bhat=R−12​𝒓\boldsymbol{r}\_{\hat{b}}=\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{r} in {𝒃hatir}\{\boldsymbol{\hat{b}}\_{i}^{r}\}.

We define the following generic distance D\text{D}\_{\boldsymbol{\Omega}} between 𝒓\boldsymbol{r} and R−12​𝒓\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{r} (from the reference point of 𝒓𝒩(𝟎,)\boldsymbol{r}\sim\mathcal{N}(\boldsymbol{0},\boldsymbol{\Omega})):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | D\displaystyle\text{D}\_{\boldsymbol{\Omega}} | =\displaystyle= | Dist​(R−12​𝒓,𝒓)\displaystyle\text{Dist}\_{\boldsymbol{\Omega}}\left(\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{r},\boldsymbol{r}\right) |  |
|  |  | =\displaystyle= | E​[(R−12​𝒓−𝒓)​(R−12​𝒓−𝒓)]\displaystyle E\left[\left(\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{r}-\boldsymbol{r}\right)^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}\left(\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{r}-\boldsymbol{r}\right)\right] |  |
|  |  | =\displaystyle= | E​[𝒓​(R−12−I​d)​(R−12−I​d)​𝒓]\displaystyle E\left[\boldsymbol{r}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\left(\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}-\mathbb{Id}\right)^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}\left(\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}-\mathbb{Id}\right)\boldsymbol{r}\right] |  |
|  |  | =\displaystyle= | E[𝒖(R−12−Id)1+(−12R−Id)𝒖]\displaystyle E\left[\boldsymbol{u}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\left(\mathbb{R}\boldsymbol{\Omega}^{-\frac{1}{2}}-\mathbb{Id}\right)\boldsymbol{\Omega}^{1+\eta}\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\mathbb{Id}\right)\boldsymbol{u}\right] |  |
|  |  | =\displaystyle= | Tr[(R−12−Id)1+(−12R−Id)]\displaystyle\text{Tr}\left[\left(\mathbb{R}\boldsymbol{\Omega}^{-\frac{1}{2}}-\mathbb{Id}\right)\boldsymbol{\Omega}^{1+\eta}\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\mathbb{Id}\right)\right] |  |
|  |  | =\displaystyle= | Tr[+1+−2R12+]\displaystyle\text{Tr}\left[\boldsymbol{\Omega}+\boldsymbol{\Omega}^{1+\eta}-2\mathbb{R}\boldsymbol{\Omega}^{\frac{1}{2}+\eta}\right] |  |

where we have expressed 𝒓=​𝒖\boldsymbol{r}=\sqrt{\boldsymbol{\Omega}}\boldsymbol{u} with 𝒖​𝒩​(𝟎,I​d)\boldsymbol{u}\sim\mathcal{N}(\boldsymbol{0},\mathbb{Id}). The Mahalanobis distance D\text{D}\_{\boldsymbol{\Omega}} corresponds to the value =−1\eta=-1.
Minimizing the distance amounts to maximizing Tr​[R12+]\text{Tr}\left[\mathbb{R}\boldsymbol{\Omega}^{\frac{1}{2}+\eta}\right]. By working in the basis of , we can then easily conclude that the minimum is reached when R=I​d\mathbb{R}=\mathbb{Id} (see [Higham89])888Interestingly, this result is valid for any choice of (since the correlation is definite positive and R\mathbb{R} is a rotation operator, hence with diagonal elements smaller than one).
.

The Mahalanobis metric999The term “Mahalanobis distance” is misleading as it is non-symmetric. quantifies the proximity of a basis {𝒛i}\{\boldsymbol{z}\_{i}\} from a reference one {𝒚i}\{\boldsymbol{y}\_{i}\}, where 𝒛i=𝑻y​𝒚i\boldsymbol{z}\_{i}=\boldsymbol{T}\_{y}\boldsymbol{y}\_{i} by measuring the following:

|  |  |  |
| --- | --- | --- |
|  | Dy(𝒓z,𝒓y)=Dy(𝑻y𝒓y,𝒓y)with𝒓y𝒩(𝟎,y)\text{D}\_{\boldsymbol{\Omega}\_{y}}\left(\boldsymbol{r}\_{z},\boldsymbol{r}\_{y}\right)=\text{D}\_{\boldsymbol{\Omega}\_{y}}\left(\boldsymbol{T}\_{y}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\_{y},\boldsymbol{r}\_{y}\right)\ \ \text{with}\ \ \boldsymbol{r}\_{y}\sim\mathcal{N}(\boldsymbol{0},\boldsymbol{\Omega}\_{y}) |  |

This proximity property is often used to build isotropic allocations, that is allocations which are less dependent on the risk that is naturally embedded in a specific basis through its inner product (more details in Section [3](https://arxiv.org/html/2511.13334v1#S3 "3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). This is the premise of the eigenrisk parity (ERP) allocations defined in [benichou-16].

As an example, let’s consider a fixed allocation 𝒘e=𝒘\boldsymbol{w}\_{e}=\boldsymbol{w} defined in the natural basis {𝒆i}\{\boldsymbol{e}\_{i}\} where 𝒘\boldsymbol{w} has been randomly chosen on the unit sphere of ℛn\mathcal{R}^{n}, that is such that \|​𝒘​\|2=\slimits@​wi2=1\|\boldsymbol{w}\|^{2}=\sumop\slimits@{w\_{i}^{2}}=1. It generates a PnL 𝒘​𝒓e\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\_{e} where the expected total variance 𝒘​𝒘\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}\boldsymbol{w} depends explicitly on the realized coefficients 𝒘i\boldsymbol{w}\_{i} on each basis vector 𝒆i\boldsymbol{e}\_{i} through the covariance . Large, significant (absolute) covariances generate pockets of risk101010Think of the main modes of the covariance matrix.
that we would want to avoid when invested in erroneous positions (e.g. constructed from inaccurate signal estimates). The cost of being wrong is embedded in the natural asset basis {𝒆i}\{\boldsymbol{e}\_{i}\} through the inner product defined by .

Now, if the Riccati basis {𝒃i}\{\boldsymbol{b}\_{i}\} is close enough from {𝒆i}\{\boldsymbol{e}\_{i}\}, one can hope that the realized PnL 𝒘​𝒓b\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\_{b} will be similar to 𝒘​𝒓e\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\_{e}. Yet, the basis risk would disappear, as no single coefficient would be exposed to excessive level of risk (the basis being isotropic), and the variance would then become \|​𝒘​\|2=1\|\boldsymbol{w}\|^{2}=1.

Clearly, everything that has been discussed so far can also be applied to the signal space and the associated bilinear form . We can similarly define the Riccati basis {𝒖i}\{\boldsymbol{u}\_{i}\} of the signals, defined by 𝒖i=−12𝒆𝒊𝒔\boldsymbol{u}\_{i}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{e\_{i}^{s}}. It is also the closest isotropic signal basis among all isotropic basis 𝒖hati=−12Ruhat​𝒆𝒊𝒔\boldsymbol{\hat{u}}\_{i}=\boldsymbol{\Xi}^{-\frac{1}{2}}\mathbb{R}\_{\hat{u}}\boldsymbol{e\_{i}^{s}} (where Ruhat​S​O​(m)\mathbb{R}\_{\hat{u}}\in SO(m)) from the perspective of D\text{D}\_{\boldsymbol{\Xi}}.

|  |  |  |
| --- | --- | --- |
|  | 𝒃i−12𝒆𝒊𝒓Riccati Root of​ℋr,𝒓−Isotropic𝒃hati−12Rbhat𝒆𝒊𝒓𝒓−Isotropic𝒖i−12𝒆𝒊𝒔Riccati Root of​ℋr,𝒔−Isotropic𝒖hati−12Ruhat𝒆𝒊𝒔𝒔−Isotropic\displaystyle\begin{array}[]{| c | c | c |}\hline\cr\boldsymbol{b}\_{i}&\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{e\_{i}^{r}}&\text{Riccati Root of}\ \mathcal{H}\_{r},\ \boldsymbol{r}-\text{Isotropic}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{\hat{b}}\_{i}&\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{e\_{i}^{r}}&\boldsymbol{r}-\text{Isotropic}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{u}\_{i}&\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{e\_{i}^{s}}&\text{Riccati Root of}\ \mathcal{H}\_{r},\ \boldsymbol{s}-\text{Isotropic}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\boldsymbol{\hat{u}}\_{i}&\boldsymbol{\Xi}^{-\frac{1}{2}}\mathbb{R}\_{\hat{u}}\boldsymbol{e\_{i}^{s}}&\boldsymbol{s}-\text{Isotropic}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \hline\cr\end{array} |  |

#### 2.3.4 Risk Decompositions in Dual Eigenbases

We consider a general allocation 𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} with 𝑳​Rm​n\boldsymbol{L}\in\mathbb{R}^{m\times n}. The portfolio variance is:

|  |  |  |
| --- | --- | --- |
|  | Var​[𝒘​𝒓]=Tr​(𝑳​𝑳)+Tr​(𝑳​𝑳)\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]=\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)+\cancel{\text{Tr}\left(\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L}\right)} |  |

We consider the eigenvalue decompositions =𝑩bar​𝑩bar\boldsymbol{\Omega}=\boldsymbol{\bar{B}}\boldsymbol{\Sigma}\boldsymbol{\bar{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} and =𝑼bar​𝑼bar\boldsymbol{\Xi}=\boldsymbol{\bar{U}}\boldsymbol{\Lambda}\boldsymbol{\bar{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} . We express 𝑳\boldsymbol{L} into the dual eigenbasis {𝒃bar},{𝒖bar}\{\boldsymbol{\bar{b}}\},\ \{\boldsymbol{\bar{u}}\}:

|  |  |  |
| --- | --- | --- |
|  | 𝑳bar=𝑳vbar​ubar=𝑼bar​𝑳​𝑩bar\boldsymbol{\bar{L}}=\boldsymbol{L}\_{\bar{v}\bar{u}}=\boldsymbol{\bar{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{\bar{B}} |  |

so that Lbarj​i=𝑼bar𝒋​𝑳​𝑩bar𝒊{\bar{L}}\_{ji}=\boldsymbol{\bar{U}\_{j}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{\bar{B}\_{i}} represents exposure to the “dual cross-mode” sbarj​rbari{\bar{s}}\_{j}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}{\bar{r}}\_{i} with 𝒓bari=𝒃bari​r\boldsymbol{\bar{r}}\_{i}={\boldsymbol{\bar{b}}\_{i}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}{r} in {𝑩bar}\{\boldsymbol{\bar{B}}\} and 𝒔barj=𝒖bar𝒋​𝒔\boldsymbol{\bar{s}}\_{j}=\boldsymbol{\bar{u}\_{j}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} in {𝒖bar}\{\boldsymbol{\bar{u}}\} with respective variance ii and jj. The n​mn\times m crossmodes are orthogonal (approximately, up to cross-covariances that we neglect) with:

|  |  |  |
| --- | --- | --- |
|  | E[sbarj𝒓bari]=bari​jandCoVar(sbarj𝒓bar𝒊,𝒔barl𝒓bark)=+i=kj=li​ij​jbari​j​bark​lE[\bar{s}\_{j}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\bar{r}}\_{i}]=\bar{\Pi}\_{ij}\ \ \text{and}\ \ \text{CoVar}(\bar{s}\_{j}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\bar{r}\_{i},\bar{s}}\_{l}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\bar{r}}\_{k})={}\_{i=k}{}\_{j=l}{}\_{ii}{}\_{jj}+\cancel{\bar{\Pi}\_{ij}\bar{\Pi}\_{kl}} |  |

The risk ℛbari​j\mathcal{\bar{R}}\_{ij} associated with each mode sbarj​rbari{\bar{s}}\_{j}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}{\bar{r}}\_{i} is:

|  |  |  |
| --- | --- | --- |
|  | ℛbari​j=Lbarj​i2(+i​ij​jbari​j2)Lbarj​i2j​ji​i\mathcal{\bar{R}}\_{ij}={\bar{L}}\_{ji}^{2}\left({}\_{ii}{}\_{jj}+\cancel{\bar{\Pi}\_{ij}^{2}}\right)\approx{\bar{L}}\_{ji}^{2}{}\_{ii}{}\_{jj} |  |

and the total variance decomposes as:

|  |  |  |
| --- | --- | --- |
|  | \slimits@i​jℛbarj​i\slimits@i​jLbarj​i2i​i=j​jTr(𝑳bar𝑳bar)Var[𝒘𝒓]\sumop\slimits@\_{ij}{\mathcal{\bar{R}}\_{ji}}\approx\sumop\slimits@\_{ij}{{}\_{ii}{\bar{L}}\_{ji}^{2}{}\_{jj}}=\text{Tr}\left(\boldsymbol{\Lambda}\boldsymbol{\bar{L}}\boldsymbol{\Sigma}\boldsymbol{\bar{L}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)\approx\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right] |  |

where we have neglected all n4n^{4}-covariance terms bar​𝑳bar​bar​𝑳bar\boldsymbol{\bar{\Pi}}\boldsymbol{\bar{L}}\boldsymbol{\bar{\Pi}}\boldsymbol{\bar{L}}.

Marginal risks per return or per signal eigenmode are:

|  |  |  |
| --- | --- | --- |
|  | {ℛbar​(𝒃bar𝒊)\slimits@ji​iLbarj​i2j​jℛbar​(𝒖bar𝒋)\slimits@ij​jLbarj​i2i​i\displaystyle\left\{\begin{array}[]{ccc}\mathcal{\bar{R}}(\boldsymbol{\bar{b}\_{i}})&\approx\hfil&{}\_{ii}\sumop\slimits@\_{j}{\bar{L}\_{ji}^{2}{}\_{jj}}\\ \mathcal{\bar{R}}(\boldsymbol{\bar{u}\_{j}})&\approx\hfil&{}\_{jj}\sumop\slimits@\_{i}{\bar{L}\_{ji}^{2}{}\_{ii}}\end{array}\right. |  |

Now, consider the Riccati basis {𝒃hat𝒊}\{\boldsymbol{\hat{b}\_{i}}\} and {𝒖hat𝒊}\{\boldsymbol{\hat{u}\_{i}}\} defined by rotations Rbhat,Ruhat\mathbb{R}\_{\hat{b}},\ \mathbb{R}\_{\hat{u}} from the whitened spaces. The transformed operator is:

|  |  |  |
| --- | --- | --- |
|  | 𝑳uhat​bhat=Ruhat​𝑳u​b​Rbhat=Ruhat12​𝑳12​Rbhat=Ruhat​𝑼bar12​𝑳bar12​𝑩bar​Rbhat\boldsymbol{L}\_{\hat{u}\hat{b}}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\_{ub}\mathbb{R}\_{\hat{b}}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\boldsymbol{L}\boldsymbol{\Omega}^{\frac{1}{2}}\mathbb{R}\_{\hat{b}}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\bar{U}}\boldsymbol{\Lambda}^{\frac{1}{2}}\boldsymbol{\bar{L}}\boldsymbol{\Sigma}^{\frac{1}{2}}\boldsymbol{\bar{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\mathbb{R}\_{\hat{b}} |  |

Variances simplifies to:

|  |  |  |
| --- | --- | --- |
|  | Var​[𝒘​𝒓]​Tr​(𝑳uhat​bhat​𝑳uhat​bhat)=Tr​(𝑳u​b​𝑳u​b)=\slimits@i​j​Luj​bi2\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]\approx\text{Tr}\left(\boldsymbol{L}\_{\hat{u}\hat{b}}\boldsymbol{L}\_{\hat{u}\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)=\text{Tr}\left(\boldsymbol{L}\_{ub}\boldsymbol{L}\_{ub}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)=\sumop\slimits@\_{ij}{L\_{u\_{j}b\_{i}}^{2}} |  |

while marginal risks per Riccati direction 𝒃hat𝒊\boldsymbol{\hat{b}\_{i}} and 𝒖hat𝒋\boldsymbol{\hat{u}\_{j}} become:

|  |  |  |
| --- | --- | --- |
|  | {ℛbar​(𝒃hat𝒊)\slimits@j​Luhatj​bhati2=\slimits@j​(Ruhat12​𝑳12​Rbhat)j​i2ℛbar​(𝒖hat𝒋)\slimits@i​Luhatj​bhati2=\slimits@i​(Ruhat12​𝑳12​Rbhat)j​i2\displaystyle\left\{\begin{array}[]{ccc}\mathcal{\bar{R}}(\boldsymbol{\hat{b}\_{i}})&\approx\hfil&\sumop\slimits@\_{j}{L\_{\hat{u}\_{j}\hat{b}\_{i}}^{2}}=\sumop\slimits@\_{j}{(\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\boldsymbol{L}\boldsymbol{\Omega}^{\frac{1}{2}}\mathbb{R}\_{\hat{b}})\_{ji}^{2}}\\ \mathcal{\bar{R}}(\boldsymbol{\hat{u}\_{j}})&\approx\hfil&\sumop\slimits@\_{i}{L\_{\hat{u}\_{j}\hat{b}\_{i}}^{2}}=\sumop\slimits@\_{i}{(\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\boldsymbol{L}\boldsymbol{\Omega}^{\frac{1}{2}}\mathbb{R}\_{\hat{b}})\_{ji}^{2}}\end{array}\right. |  |

Marginal risks expressed isotropic bases {𝒃hat𝒊}\{\boldsymbol{\hat{b}\_{i}}\} and {𝒖hat𝒊}\{\boldsymbol{\hat{u}\_{i}}\} serve as essential, basis-invariant metrics for enforcing isotropy across signal and return spaces. Those are exactly the Euclidean squared-norm of the column and row vectors of 𝑳uhat​bhat\boldsymbol{L}\_{\hat{u}\hat{b}} respectively.

#### 2.3.5 Isotropic Mappings Between Isotropic Bases

Isotropic bases admit no privileged directions. A signal 𝒔\boldsymbol{s} expressed as 𝒔uhat\boldsymbol{s}\_{\hat{u}} in an isotropic signal basis {𝒖hati}\{\hat{\boldsymbol{u}}\_{i}\} carries no *additional* risk from embedded correlations. Likewise, an isotropic return basis {𝒃hati}\{\hat{\boldsymbol{b}}\_{i}\} imposes no structural bias: all directions are equivalent. Working within such bases ensures *transparency*.

Yet, basis transformation is merely a computational tool, not a panacea. While certain bases may better withstand signal uncertainty, none are inherently superior.

Operating exclusively between isotropic bases {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\}, {𝒖hatj}\{\boldsymbol{\hat{u}}\_{j}\} eliminates default hidden basis bias in both signal and return spaces. However, this is insufficient: an arbitrary position 𝒘bhat=𝑳uhat​bhat​𝒔uhat\boldsymbol{w}\_{\hat{b}}=\boldsymbol{L}\_{\hat{u}\hat{b}}\boldsymbol{s}\_{\hat{u}} defined via a linear mapping 𝑳uhat​bhat\boldsymbol{L}\_{\hat{u}\hat{b}} between such bases can reintroduce anisotropy in the output. After all, this is just a change of perspective.

The critical question is: *which linear operators preserve dual isotropy*? These form the cornerstone of our approach. Allocations that enforce *basis immunity* by construction must rely on an *isotropic linear application* 𝑳u​b\boldsymbol{L}\_{ub} such that marginal risk is uniform across all Riccati directions.

* •

  Balanced (m=nm=n): The only matrices satisfying both conditions ℛ(𝒃i)=ℛ(𝒖j)=/2n\mathcal{R}(\boldsymbol{{b}}\_{i})=\mathcal{R}(\boldsymbol{{u}}\_{j})={}^{2}/n are *scaled orthogonal matrices*:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑳u​b=R,RR=I,=/n.\boldsymbol{L}\_{{u}{b}}=\kappa\cdot\mathbb{R},\ \mathbb{R}\mathbb{R}=\mathbb{I},\ \kappa=\sigma/\sqrt{n}. |  |

  In natural asset bases: 𝑳−12​R−12\boldsymbol{L}\propto\boldsymbol{\Xi}^{-\frac{1}{2}}\mathbb{R}\boldsymbol{\Omega}^{-\frac{1}{2}}
* •

  Unbalanced (m>nm>n): Only return-side isotropy ℛ(𝒃i)=/2n\mathcal{R}(\boldsymbol{{b}}\_{i})={}^{2}/n can be enforced everywhere. In signal space, there exist m−nm-n dimensions (i.e. n​(m−n)n\times(m-n) crossmodes) that have no contribution. The solution is a *scaled partial isometry*:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑳u​b=𝑼hat​[I​dn0(m−n),n]​𝑩hat,\boldsymbol{L}\_{{u}{b}}=\kappa\boldsymbol{\hat{U}}\begin{bmatrix}\mathbb{Id}\_{n}\\ \mathbb{0}\_{(m-n),n}\end{bmatrix}\boldsymbol{\hat{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}, |  |

  with 𝑩hat​Rn,n\boldsymbol{\hat{B}}\in\mathbb{R}^{n,n}, 𝑼hat​Rm,m\boldsymbol{\hat{U}}\in\mathbb{R}^{m,m} orthogonal, =/n\kappa=\sigma/\sqrt{n}.

  In natural bases: 𝑳−12​𝑼hatn​𝑩hat−12\boldsymbol{L}\propto\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\hat{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\hat{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}
  where 𝑼hatn\boldsymbol{\hat{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}} are the first-left vectors of the matrix 𝑼hat\boldsymbol{\hat{U}}. The remaining m−nm-n directions 𝑼hatm−n\boldsymbol{\hat{U}}\_{\stackrel{{\scriptstyle\leftarrow}}{{m-n}}} span the kernel and do not contribute.

In conclusion: isotropic linear applications are scaled orthogonal when m=nm=n and scaled partial isometries when m>nm>n. This structure is the geometric foundation of *Basis Immunity*.

This orthogonal (or partial isometry) form induces *uniform risk across return eigenmodes* in any isotropic basis {𝒃hat𝒊}\{\boldsymbol{\hat{b}\_{i}}\}, but also in the eigenbasis {𝒃bar𝒊}\{\boldsymbol{\bar{b}\_{i}}\} —hence the term “eigenrisk parity” in [benichou-16]. This equality is a *consequence* of enforced dual isotropy, not its objective.

#### 2.3.6 Canonical Portfolios

The mean-variance framework is agnostic to the choice of bases one decide to work with. It can be derived anywhere and will lead to the same solution (see Eq. [15](https://arxiv.org/html/2511.13334v1#S2.E15 "In 2.3.2 Operator 𝑳 ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")) when expressed in the natural asset and signal bases.

It is enlightening to rephrase the general closed-form solution within the perspective of the isotropic basis {𝒃i}\{\boldsymbol{b}\_{i}\} and {𝒖i}\{\boldsymbol{u}\_{i}\} (or any other isotropic basis {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\} and {𝒖hati}\{\boldsymbol{\hat{u}}\_{i}\}):

General Mean-Variance


𝒘e=1−1−1​𝒔e=1−12​\downarrow(−12−12){𝒃𝒊}​{𝒖𝒊}−12𝒔ein {𝒖𝒊}\displaystyle\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathop{\vbox{\halign{#\cr\kern 1.29167pt\cr$\braceld\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracerd$\crcr\kern 2.15277pt\cr$\hfil\displaystyle{\downarrow\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}\right)}\hfil$\crcr}}}\limits^{\{\boldsymbol{b\_{i}}\}\longleftarrow\{\boldsymbol{u\_{i}}\}}\mathop{\vbox{\halign{#\cr\kern 1.29167pt\cr$\braceld\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracerd$\crcr\kern 2.15277pt\cr$\hfil\displaystyle{\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}}\hfil$\crcr}}}\limits^{\text{in $\{\boldsymbol{u\_{i}}\}$}}

(26)

The above expression involves the correlation matrix:

|  |  |  |
| --- | --- | --- |
|  | tilde=b​u=−12−12,\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Pi}\_{bu}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}, |  |

The matrix tilde\boldsymbol{\tilde{\Pi}} is cross-correlation between normalized assets and normalized signals expressed into their corresponding Riccati basis {𝒃𝒊}\{\boldsymbol{b\_{i}}\} and {𝒖𝒊}\{\boldsymbol{u\_{i}}\}. It is also referred to as the canonical correlation matrix or just as the normalized predictability matrix.

The cross-correlation matrix tilde\boldsymbol{\tilde{\Pi}}, of size n​mn\times m, plays an important role through its singular value decomposition (SVD):

|  |  |  |  |
| --- | --- | --- | --- |
|  | tilde=𝑩tilde​tilde​𝑼tilde=𝑩tilde​tilden​𝑼tilden\displaystyle\boldsymbol{\tilde{\Pi}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}{\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\vskip-8.5359pt |  | (27) |

where 𝑩tilde\boldsymbol{\tilde{B}} and 𝑼tilde\boldsymbol{\tilde{U}} are the left and right singular vectors, of size n​nn\times n and m​mm\times m respectively, and tilde\boldsymbol{\tilde{\Psi}} is the matrix of singular values, of size n​mn\times m.

Because m​nm\geq n, tilde\boldsymbol{\tilde{\Psi}} and 𝑼tilde\boldsymbol{\tilde{U}} can be respectively block-decomposed as tilde=[tilden, 0n,m−n]\boldsymbol{\tilde{\Psi}}=[\boldsymbol{\tilde{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}},\ \mathbb{0}\_{n,m-n}] and 𝑼tilde=[𝑼tilden,𝑼tildem−n]\boldsymbol{\tilde{U}}=[\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}},\ \boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\leftarrow}}{{m-n}}}], where the notation 𝑴n\boldsymbol{M}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}} to refer to the nn first-left column vectors of a matrix 𝑴\boldsymbol{M}, while 𝑴n\boldsymbol{M}\_{\stackrel{{\scriptstyle\leftarrow}}{{n}}} are the nn last-right vectors.

Here, tilden\boldsymbol{\tilde{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}} of size n​nn\times n is diagonal positive (corresponding to the positive singular values), while 0n,m−n\mathbb{0}\_{n,m-n} is the null matrix of size n​(m−n)n\times(m-n). 𝑼tilden\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}} are the eigenvectors corresponding to tilden\boldsymbol{\tilde{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}} and 𝑼tildem−n\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\leftarrow}}{{m-n}}} is in the kernel of tilde\boldsymbol{\tilde{\Pi}}.

Through its singular value decomposition, we have the following:

* •

  The singular values tilde\boldsymbol{\tilde{\Psi}} can be used to compute the Sharpe ratio of the mean-variance allocation 𝑳=1−1−1\boldsymbol{L}=\frac{1}{\gamma}\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-1} as:

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | E​[𝒘​𝒓]\displaystyle E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}] | =\displaystyle= | 1Tr(−1−1)=1Tr(tildetilde)\displaystyle\frac{1}{\gamma}\text{Tr}\left(\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\right)=\frac{1}{\gamma}\text{Tr}\left(\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | Var​[𝒘​𝒓]\displaystyle\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right] |  | Tr​(𝑳​𝑳)=12​Tr​(tilde​tilde)​\displaystyle\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)=\frac{1}{{}^{2}}\text{Tr}\left(\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |
  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | Sharpe | =\displaystyle= | Tr​(tilde​tilde)=Tr​(tilde2)\displaystyle\sqrt{\text{Tr}\left(\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)}=\sqrt{\text{Tr}\left(\boldsymbol{\tilde{\Psi}}^{2}\right)} |  | (28) |

  Because the canonical eigenvalues are bounded by one, that is we have 0​tildei​10\leq\tilde{\Psi}\_{i}\leq 1, the Sharpe ratio is strictly bounded111111This comes from our definition of Sharpe ratio as E​[𝒘​𝒓]/Var​[𝒘​𝒓]E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]/\sqrt{\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]}. For example for any random variable xtx\_{t}, we have, we have the property 1n​\slimits@​|xt|​1n​\slimits@​xt2\frac{1}{n}\sumop\slimits@{|x\_{t}|}\leq\frac{1}{\sqrt{n}}\sqrt{\sumop\slimits@{x\_{t}^{2}}}.
   by nn. The cap is very large and not relevant in practice.
* •

  In addition, Eq. [27](https://arxiv.org/html/2511.13334v1#S2.E27 "In 2.3.6 Canonical Portfolios ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") clearly shows that the general mean-variance allocation of Eq. [26](https://arxiv.org/html/2511.13334v1#S2.E26 "In 2.3.6 Canonical Portfolios ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") can be decomposed into a set of nn orthogonal portfolios (out of n​mn\times m crossmodes), defined as canonical portfolios in [CanonicalPortfolios2023]:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑳=1−12​tilde−12=1−12​𝑩tilde​tilden​𝑼tilden−12\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{\Pi}}\boldsymbol{\Xi}^{-\frac{1}{2}}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} |  |

  Those form a set of uncorrelated allocations that combine assets and signals so as to optimize their join predictive power (in the sense of maximizing the Sharpe ratio).

Canonical Portfolios [CanonicalPortfolios2023]


𝒘e=𝑳​𝒔e=1​\slimits@k=1n​tildek​𝒘tildek​𝑳=arg𝑳⁡max⁡E​[𝒔​𝑳​𝒓]−2​Var​[𝒔​𝑳​𝒓]​𝑳=1−1−1​tilde=−12−12=𝑩tildetilde𝑼tilde𝒘tildek=−12𝑩tildek​𝑼tildek−12​𝒔e​\displaystyle\begin{array}[]{c}\boldsymbol{w}\_{e}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e}=\frac{1}{\gamma}\sumop\slimits@\_{k=1}^{n}{\tilde{\Psi}\_{k}\boldsymbol{\tilde{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}=\arg\_{\boldsymbol{L}}\max E\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]-\frac{\gamma}{2}\text{Var}\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}=\frac{1}{\gamma}\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}

(34)

We note that one could have used any other isotropic basis without having any impact on the canonical portfolios 𝒘tildek\boldsymbol{\tilde{w}}\_{k}. For instance, with bases 𝒃hati=−12Rbhat​𝒆𝒊\boldsymbol{\hat{b}}\_{i}=\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{e\_{i}} and 𝒖hati=−12Ruhat​𝒆𝒊\boldsymbol{\hat{u}}\_{i}=\boldsymbol{\Xi}^{-\frac{1}{2}}\mathbb{R}\_{\hat{u}}\boldsymbol{e\_{i}}, we would have:

|  |  |  |
| --- | --- | --- |
|  | bhat​uhat=Rbhatb​uRuhat=Rbhat𝑩tildetilde𝑼tildeRuhat\boldsymbol{\Pi}\_{\hat{b}\hat{u}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\_{bu}\mathbb{R}\_{\hat{u}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\mathbb{R}\_{\hat{u}} |  |

The eigenvalues tilde\boldsymbol{\tilde{\Psi}} are unchanged, while the eigenvectors have only been rotated, i.e. 𝑩tilde​Rbhat​𝑩tilde\boldsymbol{\tilde{B}}\mapsto\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{B}} and 𝑼tilde​Ruhat​𝑼tilde\boldsymbol{\tilde{U}}\mapsto\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{U}}, leaving canonical portfolios unimpaired. This concept of rotational invariance is significant and will be revisited multiple times in this work.

The canonical portfolios, which are defined by the allocations 𝒘tildek\boldsymbol{\tilde{w}}\_{k} in Eq. [34](https://arxiv.org/html/2511.13334v1#S2.E34 "In 2.3.6 Canonical Portfolios ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), are leveraged and ordered by their canonical correlations tilde1​tilde2​…​tilden​0\tilde{\Psi}\_{1}\geq\tilde{\Psi}\_{2}\geq...\tilde{\Psi}\_{n}\geq 0, and as such, by their amount of linear predictability. The risk of overfitting is clearly visible in the decomposition into canonical portfolios. Assuming stable covariances and , the danger lurks within the predictability matrix tilde\boldsymbol{\tilde{\Pi}}, precisely in the eigenspectrum tilde\boldsymbol{\tilde{\Psi}}. Isotropy-enforced allocations that we explore next might offer some interesting alternative.

## 3 Basis Immunity: Pure Isotropic Allocations

Mean-variance allocations are notoriously sensitive to input estimates, particularly the conditional expected returns E​[𝒓|ℱ]E[\boldsymbol{r}|\mathcal{F}], where small perturbations can induce dramatic shifts in portfolio weights (see Section [2.2.3](https://arxiv.org/html/2511.13334v1#S2.SS2.SSS3 "2.2.3 Mean-Variance Limitations ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

Basis Immunity (BI) addresses the fragility of forecast signals that may be misaligned, spurious, or correlated in ways that amplify error. The central concern is not estimation noise per se, but the *compounding of uncertainty* across dimensions.

To achieve resilience, we construct allocations that minimize dependence on the implicit structure of the asset and signal covariances and (both assumed well-estimated). The goal is to prevent inevitable forecast errors from propagating—either through signal clustering (“when it rains, it pours”) or through return-side hedging that exploits fragile correlations.

The starting point is the standard mean-variance solution (Eq. [13](https://arxiv.org/html/2511.13334v1#S2.E13 "In 2.3.2 Operator 𝑳 ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘=1−1​E​[𝒓|ℱ]=1−1​𝑴​𝒔\displaystyle\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}E[\boldsymbol{r}|\mathcal{F}]=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} |  | (35) |

where E​[𝒓​ℱ]=𝑴​𝒔E[\boldsymbol{r}\mid\mathcal{F}]=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} captures our best estimate of future returns as a linear function of the signals 𝒔\boldsymbol{s}, and is fixed via the variance constraint (Eq. [8](https://arxiv.org/html/2511.13334v1#S2.E8 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

BI minimally perturbs Eq. [35](https://arxiv.org/html/2511.13334v1#S3.E35 "In 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") while *strictly enforcing isotropy* in both signal and return spaces. That is BI follows exactly the isotropy philosophy of ERP introduced in [benichou-16].

The objective is not to eliminate risk, but to neutralize the *basis risk* arising from privileged coordinate systems—such as the natural asset and signal bases.
Robustness to uncertainty is achieved *through enforced isotropy*.
The difficulty comes from the impossibility of finding an optimal transformation that fits both asset and signal perspectives simultaneously.

To ensure transparency, we work in *isotropic bases*.
As defined in Section [2.3.3](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS3 "2.3.3 Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), the set of isotropic asset bases 𝒮​ℋr\mathcal{S}\_{\boldsymbol{\Omega}}\subset\mathcal{H}\_{r} consists of all coordinate systems of the form 𝒃hati=−1/2Rbhat​𝒆i\boldsymbol{\hat{b}}\_{i}=\boldsymbol{\Omega}^{-1/2}\mathbb{R}\_{\hat{b}}\boldsymbol{e}\_{i}, where Rbhat\mathbb{R}\_{\hat{b}} is a rotation.
In such a basis, the asset covariance becomes bhat=I\boldsymbol{\Omega}\_{\hat{b}}=\mathbb{I}, eliminating privileged risk directions. From the return viewpoint, any predictive signal generates no additional structural risk.
Similarly, isotropic signal bases 𝒮​ℋs\mathcal{S}\_{\boldsymbol{\Xi}}\subset\mathcal{H}\_{s} are given by 𝒖hati=−1/2Ruhat​𝒆i\boldsymbol{\hat{u}}\_{i}=\boldsymbol{\Xi}^{-1/2}\mathbb{R}\_{\hat{u}}\boldsymbol{e}\_{i}, yielding uhat=I\boldsymbol{\Xi}\_{\hat{u}}=\mathbb{I}.

Under full isotropy, the allocation must satisfy dual symmetry: risk is spherical in *both* whitened return and signal spaces — the underlying principle of Basis Immunity.

We describe the high-level principles on which such allocations are constructed:

* •

  The original signals 𝒔\boldsymbol{s} carry some risk through their covariance . Unavoidable (and frequent) errors in 𝒔\boldsymbol{s} could be magnified due to their covariance (bad things come together). The idea is then to adjust them through a small transformation 𝑻\boldsymbol{T} designed such that 𝑻​𝒔\boldsymbol{T}\boldsymbol{s} becomes isotropic, that is 𝑻​𝑻=I​d\boldsymbol{T}\boldsymbol{\Xi}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\mathbb{Id}. This is equivalent to expressing 𝑻=Ruhat−12\boldsymbol{T}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} and the deformation effectively amounts to replacing the original signals 𝒔\boldsymbol{s} by some isotropic signals 𝒔uhat=Ruhat−12​𝒔\boldsymbol{s}\_{\hat{u}}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}.

  If the deformation 𝑻\boldsymbol{T} is small enough, one can hope to retain the predictive power of the original signals, while being less exposed to all the unavoidable errors that will arise time after time (known unknowns and unknown unknowns).
* •

  In return space, a similar situation occurs. The positions 𝒘\boldsymbol{w} in {𝒆i}\{\boldsymbol{e}\_{i}\}, which are derived from the expected returns E​[𝒓|ℱ]E[\boldsymbol{r}|\mathcal{F}], might carry some covariance risk121212In the mean-variance framework, where the variance is constrained, this leads to the decorrelation operator −1\boldsymbol{\Omega}^{-1} being applied to E​[𝒓|ℱ]E[\boldsymbol{r}|\mathcal{F}] in Eq. [35](https://arxiv.org/html/2511.13334v1#S3.E35 "In 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").
   in the form of 𝒘​𝒘\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}\boldsymbol{w}. Errors in the position vector 𝒘\boldsymbol{w} could get magnified because of the non-diagonal covariance terms of . Clearly, if the natural basis were to be isotropic, this risk would naturally disappear.

  To emulate this desired behavior, the expected return E​[𝒓|ℱ]E[\boldsymbol{r}|\mathcal{F}], originally derived in {𝒆i}\{\boldsymbol{e}\_{i}\}, are used as such in a different isotropic basis {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\}. The newly derived positions 𝒘bhat\boldsymbol{w}\_{\hat{b}}, which would not carry any covariance risk since bhat=Id\boldsymbol{\Omega}\_{\hat{b}}=\mathbb{Id}, would then be expressed back into the original basis (where trading takes place), leading to 𝒘e=−12Rbhat​𝒘bhat\boldsymbol{w}\_{e}=\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{w}\_{\hat{b}}.

  Bu there is no free-lunch. As we are now using E​[𝒓e|ℱ]E[\boldsymbol{r}\_{e}|\mathcal{F}] instead of E​[𝒓bhat|ℱ]E[\boldsymbol{r}\_{\hat{b}}|\mathcal{F}] in the isotropic basis {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\}, we are modifying our expected PnL.
  Now, if the isotropic basis {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\} is close enough from {𝒆i}\{\boldsymbol{e}\_{i}\}, one can hope that the difference is small enough, while the basis risk would disappear.

In a nutshell, the rough idea behind BI allocations is:

1. 1.

   replace the original signals 𝒔\boldsymbol{s} by some better-behaved ones 𝒔uhat\boldsymbol{s}\_{\hat{u}} (better-behaved from a risk-perspective),
2. 2.

   replace the natural basis {𝒆i}\{\boldsymbol{e}\_{i}\} where expected returns E​[𝒓|ℱ]E[\boldsymbol{r}|\mathcal{F}] are computed by an isotropic basis {𝒃i}\{\boldsymbol{b}\_{i}\} with the approximation E​[𝒓b|ℱ]​E​[𝒓e|ℱ]E[\boldsymbol{r}\_{b}|\mathcal{F}]\approx E[\boldsymbol{r}\_{e}|\mathcal{F}].

Both approximations must obviously be done in a controlled way so that Eq. [35](https://arxiv.org/html/2511.13334v1#S3.E35 "In 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), our departing point, is not completely “destroyed”.
This is not a trivial task as both approximations are rarely compatible with a given optimization problem.

To investigate, we start below with the simpler balanced case m=nm=n. The general case where m​nm\geq n will be explored in Section [3.2](https://arxiv.org/html/2511.13334v1#S3.SS2 "3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

### 3.1 The Balanced Case m=nm=n and E​[𝒓|ℱ]​𝒔E[\boldsymbol{r}|\mathcal{F}]\propto\boldsymbol{s}

It is usual to work with as many signals as there are assets, where each signal sis\_{i} has been designed specifically for a corresponding asset SiS\_{i}, with E​[ri|ℱ]​siE[r\_{i}|\mathcal{F}]\propto s\_{i}. In that case, we can link the two dual bases {𝒆𝒊𝒓}\{\boldsymbol{e^{r}\_{i}}\} and {𝒆𝒊𝒔}\{\boldsymbol{e^{s}\_{i}}\}, setting the mapping operator to the identity 𝑴=I​d\boldsymbol{M}=\mathbb{Id}.

Within this setup (identical to the one described in [benichou-16]), the goal is to minimally disrupt the mean-variance (MV) allocation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘e=1−1​𝒔e\displaystyle\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{s}\_{e} |  | (36) |

while ensuring isotropy on both sides (asset returns and signals).

#### 3.1.1 Previous Approaches

As we discussed above, the asset Riccati basis 𝒃𝒊=−12𝒆𝒊\boldsymbol{b\_{i}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{e\_{i}} and the signal Riccati basis 𝒖𝒊=−12𝒆𝒊\boldsymbol{u\_{i}}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{e\_{i}} that we previously defined are the closest to the natural basis {𝒆𝒊}\{\boldsymbol{e\_{i}}\} for the Mahalanobis distances D\text{D}\_{\boldsymbol{\Omega}} and D\text{D}\_{\boldsymbol{\Xi}} defined above.

From this proximity property and using a symmetry argument, Benichou and al. advocate in [benichou-16] for an allocation of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘e=1−12−12​𝒔e\displaystyle\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  | (37) |

The signals 𝒔e=𝒔\boldsymbol{s}\_{e}=\boldsymbol{s} are replaced by the closest isotropic transformation 𝒔u=−12𝒔e\boldsymbol{s}\_{u}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} (in the sense of D\text{D}\_{\boldsymbol{\Xi}}):

|  |  |  |
| --- | --- | --- |
|  | 𝒔e​𝒔u=−12𝒔e,\boldsymbol{s}\_{e}\longleftarrow\boldsymbol{s}\_{u}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}, |  |

while the natural assets is substituted for its closest isotropic asset basis (in the sense of D\text{D}\_{\boldsymbol{\Omega}}), thereby replacing 𝒘e=−1E​[𝒓|ℱ]\boldsymbol{w}\_{e}=\boldsymbol{\Omega}^{-1}E[\boldsymbol{r}|\mathcal{F}] by 𝒘e=−12𝒘b\boldsymbol{w}\_{e}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{w}\_{b} where the expected returns in {𝒃i}\{\boldsymbol{b}\_{i}\} are interchanged by the ones in {𝒆i}\{\boldsymbol{e}\_{i}\}, that is:

|  |  |  |
| --- | --- | --- |
|  | 𝒘e=−12𝒘bwhereE​[𝒓b|ℱ]​E​[𝒓e|ℱ]\boldsymbol{w}\_{e}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{w}\_{b}\ \ \text{where}\ \ E[\boldsymbol{r}\_{b}|\mathcal{F}]\longleftarrow E[\boldsymbol{r}\_{e}|\mathcal{F}] |  |

Issued from a simple argument of symmetry (in return and signal spaces) and proximity (in the sense of the Mahalanobis distance), the solution Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") is elegant, practical, and effective.

However, this is not the only approach. Segonne et al. advocate in [segonne-2024] to directly work in the isotropic basis {𝒃𝒊}\{\boldsymbol{b\_{i}}\} where the targeted MV allocation of Eq. [36](https://arxiv.org/html/2511.13334v1#S3.E36 "In 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") takes the simple form:

|  |  |  |
| --- | --- | --- |
|  | 𝒘b=1​𝒔b\boldsymbol{w}\_{b}=\frac{1}{\gamma}\boldsymbol{s}\_{b} |  |

In {𝒃𝒊}\{\boldsymbol{b\_{i}}\}, only the signal approximation is needed (since {𝒃𝒊}\{\boldsymbol{b\_{i}}\} is already return-isotropic, no return approximation is required). Using a similar argument of proximity in {𝒃𝒊}\{\boldsymbol{b\_{i}}\} (and not in {𝒆𝒊}\{\boldsymbol{e\_{i}}\}), the closest isotropic signal basis of ℋs\mathcal{H}\_{s} is not 𝒖i=−12𝒆i\boldsymbol{u}\_{i}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{e}\_{i} but 𝒖hati=b−12𝒃i\boldsymbol{\hat{u}}\_{i}=\boldsymbol{\Xi}\_{b}^{-\frac{1}{2}}\boldsymbol{b}\_{i} where b=−12−12\boldsymbol{\Xi}\_{b}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}\boldsymbol{\Omega}^{-\frac{1}{2}} (that is using Db​D\text{D}\_{\boldsymbol{\Xi}\_{b}}\ne\text{D}\_{\boldsymbol{\Xi}}). Therefore, from the perspective of the signal distance Db\text{D}\_{\boldsymbol{\Xi}\_{b}}, one should replace 𝒔b\boldsymbol{s}\_{b} by b−12𝒔b\boldsymbol{\Xi}\_{b}^{-\frac{1}{2}}\boldsymbol{s}\_{b}, leading to a different allocation:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒘e\displaystyle\boldsymbol{w}\_{e} | =\displaystyle= | −12𝒘bchange of basis𝒃𝒊𝒆𝒊\displaystyle\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{w}\_{b}\hskip 54.06006pt\text{change of basis}\ \boldsymbol{b\_{i}}\mapsto\boldsymbol{e\_{i}} |  | (38) |
|  |  | =\displaystyle= | −12(1b−12𝒔b)approximation𝒔b𝒔uhat\displaystyle\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\frac{1}{\gamma}\boldsymbol{\Xi}\_{b}^{-\frac{1}{2}}\boldsymbol{s}\_{b}\right)\hskip 14.22636pt\text{approximation}\ \boldsymbol{s}\_{b}\longleftarrow\boldsymbol{s}\_{\hat{u}} |  |
|  |  | =\displaystyle= | 1−12(−12−12)−12−12𝒔e\displaystyle\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  |

The solution Eq [38](https://arxiv.org/html/2511.13334v1#S3.E38 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") coincides with Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") when the two covariances and commute131313This would be the case if the covariance is chosen as +(1−)​I​d\boldsymbol{\Xi}\propto\varphi\boldsymbol{\Omega}+(1-\varphi)\mathbb{Id} as advocated in [benichou-16].
. However, when this is not the case, Eq [38](https://arxiv.org/html/2511.13334v1#S3.E38 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") is “closer” (in the Mahalanobis sense) to the initial mean-variance solution Eq. [36](https://arxiv.org/html/2511.13334v1#S3.E36 "In 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") than the allocation Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") proposed in [benichou-16]. As we discuss below in Section [3.1.3](https://arxiv.org/html/2511.13334v1#S3.SS1.SSS3 "3.1.3 Discussion ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), the difference is small.

Interestingly, the solution does not depend on the specific isotropic basis {𝒃𝒊}\{\boldsymbol{b\_{i}}\}. It would be identical in any other isotropic asset basis {𝒃hat𝒊}\{\boldsymbol{\hat{b}\_{i}}\} (that is of the form 𝒃hat𝒊=u−12Rbhat​𝒆𝒊\boldsymbol{\hat{b}\_{i}}=\boldsymbol{\Omega}\_{u}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{e\_{i}}).

Finally, we note that we can rewrite Eq. [38](https://arxiv.org/html/2511.13334v1#S3.E38 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘e=1−12​Rb−12​𝒔e\displaystyle\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{b}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  | (39) |

where we can verify that Rb=(−12−12)−12−1212\mathbb{R}\_{b}=\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{\frac{1}{2}} is a rotation.
By explicitly working in the isotropic basis {𝒃𝒊}\{\boldsymbol{b\_{i}}\}, only a signal proximity argument is needed and the symmetry argument not required anymore. From the perspective of the Mahalanobis distance, Eq. [39](https://arxiv.org/html/2511.13334v1#S3.E39 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") is less disruptive than Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

Now, a symmetrical argument could also be constructed by considering the isotropic signal basis {𝒖𝒊}\{\boldsymbol{u\_{i}}\} and slightly adjusting the asset basis. In this scenario, no signal approximation would be needed, only the approximation in return space. We substitute the targeted solution of Eq. [36](https://arxiv.org/html/2511.13334v1#S3.E36 "In 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"):

|  |  |  |
| --- | --- | --- |
|  | 𝒘u=u−1E​[𝒓u|ℱ]=u−1𝒔u,\boldsymbol{w}\_{u}=\boldsymbol{\Omega}\_{u}^{-1}E[\boldsymbol{r}\_{u}|\mathcal{F}]=\boldsymbol{\Omega}\_{u}^{-1}\boldsymbol{s}\_{u}, |  |

by its closest isotropic asset allocation:

|  |  |  |
| --- | --- | --- |
|  | 𝒘u=u−12𝒘bhatwhereE​[𝒓bhat|ℱ]​E​[𝒓u|ℱ]=𝒔u,\boldsymbol{w}\_{u}=\boldsymbol{\Omega}\_{u}^{-\frac{1}{2}}\boldsymbol{w}\_{\hat{b}}\ \ \text{where}\ \ E[\boldsymbol{r}\_{\hat{b}}|\mathcal{F}]\approx E[\boldsymbol{r}\_{u}|\mathcal{F}]=\boldsymbol{s}\_{u}, |  |

where we have u=−12−12\boldsymbol{\Omega}\_{u}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}\boldsymbol{\Xi}^{-\frac{1}{2}}. This would lead to the solution:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒘e\displaystyle\boldsymbol{w}\_{e} | =\displaystyle= | u−12𝒘uchange of basis𝒖𝒊𝒆𝒊\displaystyle\boldsymbol{\Xi}\_{u}^{-\frac{1}{2}}\boldsymbol{w}\_{{u}}\hskip 56.9055pt\text{change of basis}\ \boldsymbol{u\_{i}}\mapsto\boldsymbol{e\_{i}} |  |
|  |  | =\displaystyle= | u−12u−12𝒘bhatchange of basis𝒃hat𝒊𝒖𝒊\displaystyle\boldsymbol{\Xi}\_{u}^{-\frac{1}{2}}\boldsymbol{\Omega}\_{u}^{-\frac{1}{2}}\boldsymbol{w}\_{\hat{b}}\hskip 36.98866pt\text{change of basis}\ \boldsymbol{\hat{b}\_{i}}\mapsto\boldsymbol{u\_{i}} |  |
|  |  | =\displaystyle= | 1u−12u−12​𝒔uapprox​E​[𝒓bhat|ℱ]​𝒔u\displaystyle\frac{1}{\gamma}\boldsymbol{\Xi}\_{u}^{-\frac{1}{2}}\boldsymbol{\Omega}\_{u}^{-\frac{1}{2}}\boldsymbol{s}\_{u}\hskip 34.14322pt\text{approx}\ E[\boldsymbol{r}\_{\hat{b}}|\mathcal{F}]\longleftarrow\boldsymbol{s}\_{u} |  |
|  |  | =\displaystyle= | 1−12(−12−12)−12−12𝒔e\displaystyle\frac{1}{\gamma}\boldsymbol{\Xi}^{-\frac{1}{2}}\left(\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}\boldsymbol{\Xi}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  |

Similarly, the solution is valid for all isotropic signal basis {𝒖hat𝒊}\{\boldsymbol{\hat{u}\_{i}}\} (that is not only for {𝒖𝒊}\{\boldsymbol{u\_{i}}\}) and could be rewritten as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘e=1−12​Ru−12​𝒔e\displaystyle\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{u}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  | (40) |

where Ru=12−12(−12−12)−12\mathbb{R}\_{u}=\boldsymbol{\Omega}^{\frac{1}{2}}\boldsymbol{\Xi}^{-\frac{1}{2}}\left(\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}\boldsymbol{\Xi}^{-\frac{1}{2}}\right)^{-\frac{1}{2}} is a rotation.

#### 3.1.2 Balanced Isotropic Allocations

One should quickly realize that the three above allocations Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (from [benichou-16]), Eq [39](https://arxiv.org/html/2511.13334v1#S3.E39 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (from [segonne-2024]), and Eq [40](https://arxiv.org/html/2511.13334v1#S3.E40 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") are not unique and that the space of potential solutions is infinite. Specificaly, any isotropic solution can be written as (see Section [2.3.5](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS5 "2.3.5 Isotropic Mappings Between Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")):

|  |  |  |
| --- | --- | --- |
|  | Balanced Isotropy-Enforced Allocation Form |  |
|  |  |  |
| --- | --- | --- |
|  | m=n,𝑴=I​d\displaystyle m=n,\ \boldsymbol{M}=\mathbb{Id}\hskip 56.9055pt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘e=1−12​R−12​𝒔e=n​−12Rbhatreturn\downarrow​Ruhat−12𝒔esignal\displaystyle\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}=\frac{\sigma}{\sqrt{n}}\mathop{\vtop{\halign{#\cr$\hfil\displaystyle{\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}}\hfil$\crcr\kern 2.15277pt\cr$\bracelu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemd\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\braceru$\crcr\kern 1.29167pt\cr}}}\limits\_{\text{return}}\ \downarrow\ \mathop{\vbox{\halign{#\cr\kern 1.29167pt\cr$\braceld\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracerd$\crcr\kern 2.15277pt\cr$\hfil\displaystyle{\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}}\hfil$\crcr}}}\limits^{\text{signal}}\ \ \ |  | (45) |

where Rbhat\mathbb{R}\_{\hat{b}}, Ruhat\mathbb{R}\_{\hat{u}} are rotation operators associated with isotropic bases 𝒃hat𝒊=u−12Rbhat​𝒆𝒊\boldsymbol{\hat{b}\_{i}}=\boldsymbol{\Omega}\_{u}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{e\_{i}} and 𝒖hat𝒊=u−12Ruhat​𝒆𝒊\boldsymbol{\hat{u}\_{i}}=\boldsymbol{\Xi}\_{u}^{-\frac{1}{2}}\mathbb{R}\_{\hat{u}}\boldsymbol{e\_{i}}.
The down-arrow has been added to explicitly indicate a transformation from ℋr\mathcal{H}\_{r} to ℋr\mathcal{H}\_{r} in the basis {𝒃hat𝒊}\{\boldsymbol{\hat{b}\_{i}}\}. Plugging Eq. [45](https://arxiv.org/html/2511.13334v1#S3.E45 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") into the variance constraint, the leverage coefficient can be computed as =n\gamma\sigma=\sqrt{n}.

As discussed in Section [2.3.5](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS5 "2.3.5 Isotropic Mappings Between Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), isotropic allocations, i.e. of the form Eq. [45](https://arxiv.org/html/2511.13334v1#S3.E45 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), carry the same risk in all directions (both in signal and return spaces). In particular, each eigenmode, in return and signal spaces, carries the same risk, equal to 1/n1/n of the total variance 2.
This justifies the term “Eigenrisk Parity” coined in [benichou-16].

Within the manifold of isotropic allocations, a selection problem remains: we must choose the orthogonal operator R=Rbhat​Ruhat\mathbb{R}=\mathbb{R}\_{\hat{b}}\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} that connects the return and signal bases. Not all choices are equal—some induce excessive deformation of the original mean-variance signal, failing to preserve predictive structure.

Although the Mahalanobis distances D\text{D}\_{\boldsymbol{\Omega}} and D\text{D}\_{\boldsymbol{\Xi}} could be used to rank candidate solutions, we adopt an alternative, provably equivalent approach that generalizes naturally to the over-determined case m​nm\geq n.

To do so, we rephrase the mean-variance solution of Eq. [36](https://arxiv.org/html/2511.13334v1#S3.E36 "In 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (our starting point) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘=1−1​𝒔=1−12​Rbhat​(Rbhat−1212​Ruhat)​Ruhat−12​𝒔\displaystyle\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{s}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\left(\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}\right)\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s} |  | (46) |

By comparing Eq. [45](https://arxiv.org/html/2511.13334v1#S3.E45 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") with Eq. [46](https://arxiv.org/html/2511.13334v1#S3.E46 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we then define the optimal allocation by selecting the rotations Rbhat\mathbb{R}\_{\hat{b}} and Ruhat\mathbb{R}\_{\hat{u}} that best aligns the linear mapping Rbhat−1212​Ruhat\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}} with I​dn\mathbb{Id}\_{n}. That is we search for the closest isotropy. To do so, we minimize:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Rbhat−1212​Ruhat−I​dn‖F2=‖R−1212−I​dn‖F2\displaystyle||\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}-\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}}=||\mathbb{R}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{\frac{1}{2}}-\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}} |  | (47) |

where ‖𝑨‖F=Tr​(𝑨​𝑨)||\boldsymbol{A}||\_{\mathbb{F}}=\sqrt{\text{Tr}\left(\boldsymbol{A}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{A}\right)} is the usual Frobenius norm.
The optimal rotation R\mathbb{R} is the one maximizing the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R=argR⁡max⁡Tr​(R−1212)\displaystyle\mathbb{R}=\arg\_{\mathbb{R}}\max\text{Tr}\left(\mathbb{R}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{\frac{1}{2}}\right) |  | (48) |

Using the singular value decomposition141414Please note that hat2\boldsymbol{\hat{\Psi}}^{2}, the squared singular values of −12+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{+\frac{1}{2}}, are the eigenvalues of b=−12−12\boldsymbol{\Xi}\_{b}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}\boldsymbol{\Omega}^{-\frac{1}{2}} while hat−2\boldsymbol{\hat{\Psi}}^{-2} are the eigenvalues of b=−12−12\boldsymbol{\Omega}\_{b}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}\boldsymbol{\Xi}^{-\frac{1}{2}}.
 of −12+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{+\frac{1}{2}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −12+12=𝑩hathat𝑼hat,\displaystyle\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\hat{B}}\boldsymbol{\hat{\Psi}}\boldsymbol{\hat{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}, |  | (49) |

the solution can be expressed as:

Balanced Dual-Isotropy Allocationm=n,𝑴=I​d𝒘e=n−12​R−12​𝒔e​with​R=𝑩hat​𝑼hat−12+12=𝑩hathat𝑼hat\displaystyle\begin{array}[]{c}\text{\bf Balanced Dual-Isotropy Allocation}\\
m=n,\boldsymbol{M}=\mathbb{Id}\\
\\
\boldsymbol{w}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\ \text{with}\ \mathbb{R}=\boldsymbol{\hat{B}}\boldsymbol{\hat{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\\
\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\hat{B}}\boldsymbol{\hat{\Psi}}\boldsymbol{\hat{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\\
\end{array}

(55)

#### 3.1.3 Discussion

The solution only depends on the product R=Rbhat​Ruhat\mathbb{R}=\mathbb{R}\_{\hat{b}}\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}, not on specific realizations of Rbhat\mathbb{R}\_{\hat{b}} and Ruhat\mathbb{R}\_{\hat{u}} (a similar observation was made with the solutions Eq. [39](https://arxiv.org/html/2511.13334v1#S3.E39 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and Eq. [40](https://arxiv.org/html/2511.13334v1#S3.E40 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). Because −12+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{+\frac{1}{2}} is not symmetric (except in some special cases, such as having and commute), 𝑩hat​𝑼hat\boldsymbol{\hat{B}}\ne\boldsymbol{\hat{U}} and R\mathbb{R} is not the identity matrix.

The closed-form solution of Eq. [55](https://arxiv.org/html/2511.13334v1#S3.E55 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") is the isotropic allocation that minimizes the deformation between the set of all isotropic bases 𝒮\mathcal{S}\_{\boldsymbol{\Omega}} and 𝒮\mathcal{S}\_{\boldsymbol{\Xi}}. It finds the rotation R\mathbb{R} that align best the two isotropic subspaces (see [Schonemann66, GolubVanLoan2013]).

Equivalence with the Distance Approach [benichou-16, segonne-2024]

Interestingly, we can show that the above approach is equivalent to the distance minimization. Focusing on Eq. [45](https://arxiv.org/html/2511.13334v1#S3.E45 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we follow the same reasoning that led to Eq. [39](https://arxiv.org/html/2511.13334v1#S3.E39 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and Eq. [40](https://arxiv.org/html/2511.13334v1#S3.E40 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). Two views are then possible, depending if we chose to work from the return or the signal angles:

* •

  From the asset perspective, working within the isotropic asset basis 𝒃hati=−12Rbhat​𝒆i\boldsymbol{\hat{b}}\_{i}=\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{e}\_{i}, we are replacing the signal vector 𝒔bhat=Rbhat−12​𝒔e\boldsymbol{s}\_{\hat{b}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{s}\_{e} by another one 𝒔uhat=Ruhat−12​𝒔e\boldsymbol{s}\_{\hat{u}}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} that has the desired property of being signal isotropic151515Because is {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\} is return isotropic, the transformation associated with the bilinear form from covectors space 𝒃hati\boldsymbol{\hat{b}}\_{i} into 𝒃hati\boldsymbol{\hat{b}}\_{i} is the identity.:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝒔uhat=Ruhat−12​𝒔e=Ruhat−12+12​Rbhat​𝒔bhat\boldsymbol{s}\_{\hat{u}}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}^{+\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{s}\_{\hat{b}} |  |

  The distance associated with the approximation is:

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | Dbhat​(𝒔uhat,𝒔bhat)\displaystyle\text{D}\_{\boldsymbol{\Xi}\_{\hat{b}}}\left(\boldsymbol{s}\_{\hat{u}},\boldsymbol{s}\_{\hat{b}}\right) | =\displaystyle= | Dbhat​(Ruhat−12+12​Rbhat​𝒔bhat,𝒔bhat)\displaystyle\text{D}\_{\boldsymbol{\Xi}\_{\hat{b}}}\left(\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}^{+\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{s}\_{\hat{b}},\boldsymbol{s}\_{\hat{b}}\right) |  | (56) |
  |  |  | =\displaystyle= | D(+12R−12𝒔e,𝒔e)\displaystyle\text{D}\_{\boldsymbol{\Xi}}\left(\boldsymbol{\Omega}^{+\frac{1}{2}}\mathbb{R}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e},\boldsymbol{s}\_{e}\right) |  |
  |  |  | =\displaystyle= | ||−1212R−Id||F2\displaystyle||\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}^{\frac{1}{2}}\mathbb{R}-\mathbb{Id}||^{2}\_{\mathbb{F}} |  |
* •

  Conversely, we could be working from the signal perspective using the isotropic signal basis 𝒖hati=−12Ruhat​𝒆i\boldsymbol{\hat{u}}\_{i}=\boldsymbol{\Xi}^{-\frac{1}{2}}\mathbb{R}\_{\hat{u}}\boldsymbol{e}\_{i} as a starting point. That is, instead of working in the return-isotropic basis {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\} and choosing the closest isotropic signals from 𝒔bhat\boldsymbol{s}\_{\hat{b}} (based on Dbhat\text{D}\_{\boldsymbol{\Xi}\_{\hat{b}}}), we would now fix the used signals as 𝒔uhat\boldsymbol{s}\_{\hat{u}} and pick the closest isotropic basis from {𝒖hati}\{\boldsymbol{\hat{u}}\_{i}\} (based on Duhat\text{D}\_{\boldsymbol{\Omega}\_{\hat{u}}}).

  By doing that, we are effectively replacing the expected position 𝒘uhat=1uhat−1​𝒔uhat\boldsymbol{w}\_{\hat{u}}=\frac{1}{\gamma}\boldsymbol{\Omega}\_{\hat{u}}^{-1}\boldsymbol{s}\_{\hat{u}}, which carries some return covariance risk, by another one 𝒘bhat=1​𝒔uhat\boldsymbol{w}\_{\hat{b}}=\frac{1}{\gamma}\boldsymbol{s}\_{\hat{u}} that is now return-isotropic:

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | 𝒘e\displaystyle\boldsymbol{w}\_{e} | =\displaystyle= | −12Rbhat𝒘bhat\displaystyle\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{w}\_{\hat{b}} |  |
  |  |  | =\displaystyle= | 1−12​Rbhat​𝒔uhat\displaystyle\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\boldsymbol{s}\_{\hat{u}} |  |
  |  |  | =\displaystyle= | 1−12​Rbhat​Ruhat−12​𝒔e\displaystyle\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  |

  The approximation E​[𝒓bhat|ℱ]​E​[𝒓uhat|ℱ]=𝒔uhatE[\boldsymbol{r}\_{\hat{b}}|\mathcal{F}]\longleftarrow E[\boldsymbol{r}\_{\hat{u}}|\mathcal{F}]=\boldsymbol{s}\_{\hat{u}} is measured as:

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | Duhat​(𝒓bhat,𝒓uhat)\displaystyle\text{D}\_{\boldsymbol{\Omega}\_{\hat{u}}}\left(\boldsymbol{r}\_{\hat{b}},\boldsymbol{r}\_{\hat{u}}\right) | =\displaystyle= | Duhat​(Rbhat−12​𝒓e,Ruhat−12​𝒓e)\displaystyle\text{D}\_{\boldsymbol{\Omega}\_{\hat{u}}}\left(\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{r}\_{e},\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{r}\_{e}\right) |  | (57) |
  |  |  | =\displaystyle= | D(+12R−12𝒓e,𝒓e)\displaystyle\text{D}\_{\boldsymbol{\Omega}}\left(\boldsymbol{\Xi}^{+\frac{1}{2}}\mathbb{R}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{r}\_{e},\boldsymbol{r}\_{e}\right) |  |
  |  |  | =\displaystyle= | ‖R12−12−I​d‖F2\displaystyle||\mathbb{R}\boldsymbol{\Xi}^{\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}-\mathbb{Id}||^{2}\_{\mathbb{F}} |  |

Using the singular value decomposition of −12+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{+\frac{1}{2}} in Eq. [49](https://arxiv.org/html/2511.13334v1#S3.E49 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), one can quickly see that both Eq. [56](https://arxiv.org/html/2511.13334v1#S3.E56 "In 1st item ‣ 3.1.3 Discussion ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and Eq. [57](https://arxiv.org/html/2511.13334v1#S3.E57 "In 2nd item ‣ 3.1.3 Discussion ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") lead to the same solution R=𝑩hat​𝑼hat\mathbb{R}=\boldsymbol{\hat{B}}\boldsymbol{\hat{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}.

Besides, one can easily show that both allocations Eq. [39](https://arxiv.org/html/2511.13334v1#S3.E39 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and Eq. [40](https://arxiv.org/html/2511.13334v1#S3.E40 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") are the same and equal to the optimal allocation of Eq. [55](https://arxiv.org/html/2511.13334v1#S3.E55 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). This is not surprising, since both were designed to minimize D\text{D}\_{\boldsymbol{\Xi}} and D\text{D}\_{\boldsymbol{\Omega}} respectively:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | R\displaystyle\mathbb{R} | =\displaystyle= | Rb=Ru=𝑩hat​𝑼hat\displaystyle\mathbb{R}\_{b}\ =\ \mathbb{R}\_{u}\ =\ \boldsymbol{\hat{B}}\boldsymbol{\hat{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Rb\displaystyle\mathbb{R}\_{b} | =\displaystyle= | (−12−12)−12−1212\displaystyle\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{\frac{1}{2}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ru\displaystyle\mathbb{R}\_{u} | =\displaystyle= | 12−12(−12−12)−12\displaystyle\boldsymbol{\Omega}^{\frac{1}{2}}\boldsymbol{\Xi}^{-\frac{1}{2}}\left(\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\Omega}\boldsymbol{\Xi}^{-\frac{1}{2}}\right)^{-\frac{1}{2}} |  |

On the other hand, the ERP allocation of Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") proposed in [benichou-16], which amounts to R=I​d\mathbb{R}=\mathbb{Id}, does not generally correspond to an optimum of our metric in Eq. [47](https://arxiv.org/html/2511.13334v1#S3.E47 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"),
but should most of the time be close (except for rare pathological cases that would not make sense in practice, see below). The distortion of the entry signals 𝒔\boldsymbol{s} is still controlled, although to a lesser extent, thanks to the proximity of the two Riccati basis {𝒃i}\{\boldsymbol{b}\_{i}\} and {𝒖i}\{\boldsymbol{u}\_{i}\}. We can show (as noticed in [segonne-2024]) that when both covariances commute =\boldsymbol{\Xi}\boldsymbol{\Omega}=\boldsymbol{\Omega}\boldsymbol{\Xi}, then R=I​d\mathbb{R}=\mathbb{Id} and all solutions collapse to Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

BI versus ERP [benichou-16]: Study of a Pathological Case

To illustrate some differences, we consider a pathological case. We consider 3 assets, where only asset 1 and 2 two are return-correlated at , whereas asset 2 and 3 are signal-correlated at −-\rho.

|  |  |  |
| --- | --- | --- |
|  | =(1010000)=(10001−0−1)\boldsymbol{\Omega}=\begin{pmatrix}\begin{array}[]{ccc}1&\rho\hfil&0\\ \rho\hfil&1&0\\ 0&0&0\end{array}\end{pmatrix}\ \ \boldsymbol{\Xi}=\begin{pmatrix}\begin{array}[]{ccc}1&0&0\\ 0&1&-\rho\\ 0&-\rho&1\end{array}\end{pmatrix} |  |

As varies from 0 to 1, the optimal rotation R\mathbb{R} deviates more and more from the identity matrix. As an element of S​O​(3)SO(3), we display below the minimal rotation angle =cos−1⁡(Tr​(R)−12)\theta=\cos^{-1}\left(\frac{\text{Tr}(\mathbb{R})-1}{2}\right) as a function of . Even for extreme values 1\rho\rightarrow 1, the distortion remains rather small.

![[Uncaptioned image]](theta.png)

Agnostic Risk Parity

Agnostic Risk Parity is derived in [benichou-16] as a special case of the ERP framework. The authors note that is difficult to reliably estimate and propose a simple parametric form:

|  |  |  |
| --- | --- | --- |
|  | =+(1−)​I​d,\boldsymbol{\Xi}=\varphi\boldsymbol{\Omega}+(1-\varphi)\mathbb{Id}, |  |

which has proven effective in trend-following applications.

Under this assumption, and commute, and in the balanced case (m=nm=n), the ARP allocation exactly coincides with *Basis Immunity*.

Conclusion

Allocations such as Eq. [37](https://arxiv.org/html/2511.13334v1#S3.E37 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") or Eq. [55](https://arxiv.org/html/2511.13334v1#S3.E55 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") are pure isotropic allocations.
They assume that the signals 𝒔\boldsymbol{s} are predictive of future returns, with E​[𝒓|ℱ]​𝒔E[\boldsymbol{r}|\mathcal{F}]\propto\boldsymbol{s}, and seek to *minimally perturb* the mean-variance benchmark −1E[𝒓ℱ]−1𝒔\boldsymbol{\Omega}^{-1}E[\boldsymbol{r}\mid\mathcal{F}]\propto\boldsymbol{\Omega}^{-1}\boldsymbol{s}, while enforcing dual isotropy.

However, there is *no guarantee* that the transformed signals retain sufficient predictive power, as the construction is driven *solely by risk considerations*. Even when isotropy is optimally aligned, the final allocation may deviate significantly from the original, particularly when and are poorly conditioned, potentially leading to *unintended concentration or catastrophic underperformance*.

Controlling the amount of lost predictability while aiming to be as isotropic as possible (in signal space and/or asset space) is therefore essential. We explore this *tunable regularization* in Section [4](https://arxiv.org/html/2511.13334v1#S4 "4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") via the *Isotropy-Regularized Mean-Variance* framework.

Before doing so, we extend the “pure” isotropic construction to the general case where the mapping 𝑴\boldsymbol{M} is not the identity, while the number of signals differ from the number of assets m​nm\ne n.

### 3.2 Unbalanced Case m​nm\geq n and E​[𝒓|ℱ]​𝑴​𝒔E[\boldsymbol{r}|\mathcal{F}]\propto\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}

The general case where the number of signals differs from the number of assets requires a mapping, assumed to be a linear application, from the space of signals into the space of assets. This is achieved through the operator 𝑴\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} from signal dual space ℋs\mathcal{H}\_{s} into return dual space ℋr\mathcal{H}\_{r}:

|  |  |  |
| --- | --- | --- |
|  | 𝒔​ℋs​𝒛=𝑴​𝒔​ℋz​ℋr\boldsymbol{s}\in\mathcal{H}\_{s}\mapsto\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\in\mathcal{H}\_{z}\sim\mathcal{H}\_{r} |  |

Each signal ziz\_{i}, assumed to be predictive of future return rir\_{i}, is constructed as a linear aggregation (fixed given weights) of several signals zi=\slimits@j​Mj​i​sjz\_{i}=\sumop\slimits@\_{j}{M\_{ji}s\_{j}} (potentially all of them):

|  |  |  |
| --- | --- | --- |
|  | E​[𝒓|ℱ]​𝒛=𝑴​𝒔E[\boldsymbol{r}|\mathcal{F}]\propto\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} |  |

𝒔​ℋs=E​[𝒔​𝒔]\begin{array}[]{c}\boldsymbol{s}\in\mathcal{H}\_{s}\\
\boldsymbol{\Xi}=E[\boldsymbol{s}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]\end{array}𝒛​ℋz=E​[𝒛​𝒛]\begin{array}[]{c}\boldsymbol{z}\in\mathcal{H}\_{z}\\
\boldsymbol{\Phi}=E[\boldsymbol{z}\boldsymbol{z}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]\end{array}𝒓​ℋr=E​[𝒓​𝒓]\begin{array}[]{c}\boldsymbol{r}\in\mathcal{H}\_{r}\\
\boldsymbol{\Omega}=E[\boldsymbol{r}\boldsymbol{r}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]\end{array}𝒛=𝑴​𝒔\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}Mapping𝒘=1−12​R−12​𝒛\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\boldsymbol{\Phi}^{-\frac{1}{2}}\boldsymbol{z}\ \ \ \ 𝒘=1−12​𝑩​𝑼−12​𝒔\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{B}\boldsymbol{U}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\ \

As we already discussed, the mapping 𝑴\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} can be obtained through several options, for instance e.g. based on explicit deterministic relationships, or by using statistical linear regression with 𝑴=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\beta}, or even directly within a mean-variance optimization leading to 𝑴=−1\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1} (see section [2.2](https://arxiv.org/html/2511.13334v1#S2.SS2 "2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). The important point is that 𝑴\boldsymbol{M} is known and given.

The matrix =E​[𝒛​𝒛]=𝑴​𝑴\boldsymbol{\Phi}=E[\boldsymbol{z}\boldsymbol{z}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M} is then the covariance of the mapped signals 𝒛=𝑴​𝒔\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} in ℋz​ℋr\mathcal{H}\_{z}\sim\mathcal{H}\_{r}; it is typically invertible when m​nm\geq n (except in pathological cases)161616When m<nm<n, the inverse of does not exist, but we do not consider this case here.
.

We extend our definition of isotropic allocation in Eq. [45](https://arxiv.org/html/2511.13334v1#S3.E45 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") to accommodate/link signal and return spaces with potentially different dimensions (as m​nm\geq n) as (see Section [2.3.5](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS5 "2.3.5 Isotropic Mappings Between Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")):

|  |  |  |
| --- | --- | --- |
|  | Unbalanced Isotropy-Enforced Allocation Form |  |
|  |  |  |
| --- | --- | --- |
|  | m​n\displaystyle m\geq n\hskip 85.35826pt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘e=1−12𝑩hatasset\downarrow​𝑼hatn−12𝒔esignalwith𝑩hat​𝑩hat=𝑼hatn​𝑼hatn=I​dn\displaystyle\mathop{\vtop{\halign{#\cr$\hfil\displaystyle{\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\hat{B}}}\hfil$\crcr\kern 2.15277pt\cr$\bracelu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemd\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\braceru$\crcr\kern 1.29167pt\cr}}}\limits\_{\text{asset}}\ \downarrow\ \mathop{\vbox{\halign{#\cr\kern 1.29167pt\cr$\braceld\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracerd$\crcr\kern 2.15277pt\cr$\hfil\displaystyle{\boldsymbol{\hat{U}}\_{n}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}}\hfil$\crcr}}}\limits^{\text{signal}}\ \ \text{with}\ \ \boldsymbol{\hat{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\hat{B}}=\boldsymbol{\hat{U}}\_{n}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\hat{U}}\_{n}=\mathbb{Id}\_{n} |  | (62) |

where the two matrices 𝑩hat\boldsymbol{\hat{B}} (of size n​nn\times n) and 𝑼hatn\boldsymbol{\hat{U}}\_{n} (of size m​nm\times n) encode nn orthonormal vectors of ℋr\mathcal{H}\_{r} and ℋs\mathcal{H}\_{s} respectively, i.e. 𝑩hat​𝑩hat=𝑼hatn​𝑼hatn=I​dn\boldsymbol{\hat{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\hat{B}}=\boldsymbol{\hat{U}}\_{n}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\hat{U}}\_{n}=\mathbb{Id}\_{n}. The linear application 𝑩hat​𝑼hatn\boldsymbol{\hat{B}}\boldsymbol{\hat{U}}\_{n}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} is the equivalent of the operator R=Rbhat​Ruhat\mathbb{R}=\mathbb{R}\_{\hat{b}}\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} in Eq. [45](https://arxiv.org/html/2511.13334v1#S3.E45 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). Those are partial isometry (see Section [2.3.5](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS5 "2.3.5 Isotropic Mappings Between Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

When m>nm>n, Eq. [62](https://arxiv.org/html/2511.13334v1#S3.E62 "In 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") extracts nn orthogonal directions 𝑼hatn\boldsymbol{\hat{U}}\_{n} of the isotropic signals −12𝒔e\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} (hence the subscript nn), thereby focusing on a submanifold (Rn​Rm\sim\mathbb{R}^{n}\subset\mathbb{R}^{m}) of an isotropic basis {𝒖hati}\{\boldsymbol{\hat{u}}\_{i}\}. The nn features are then mapped to an isotropic basis {𝒃hati}\{\boldsymbol{\hat{b}}\_{i}\} through 𝑩hat\boldsymbol{\hat{B}}.

Compared to the balanced case where m=nm=n, unbalanced isotropic allocations of the form Eq. [45](https://arxiv.org/html/2511.13334v1#S3.E45 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") cannot carry the same risk in all signal directions. As m>nm>n, any linear operator of the form 𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} will have m−nm-n directions that be in the kernel.
However, as in the balanced case, each return eigenmode in the Riccati basis carries equal risk—precisely 1/n1/n of the total portfolio variance 2. The term “eigenrisk parity” remains descriptively valid.

The mapped signals 𝒛=𝑴​𝒔\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} provides us with some estimates of future returns as E​[𝒓|ℱ]=𝒛E[\boldsymbol{r}|\mathcal{F}]=\boldsymbol{z}. Two approaches are possible depending if we prefer to work in the space of mapped signals ℋz\mathcal{H}\_{z} or in the original space ℋs\mathcal{H}\_{s}.

#### 3.2.1 Working with mapped signals 𝒛=𝑴​𝒔\boldsymbol{z}=\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}

Working from the perspective of the signals 𝒛\boldsymbol{z} in ℋz\mathcal{H}\_{z}, we directly apply the previous results of section [3.1](https://arxiv.org/html/2511.13334v1#S3.SS1 "3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). For instance, using Eq. [39](https://arxiv.org/html/2511.13334v1#S3.E39 "In 3.1.1 Previous Approaches ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we obtain:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒘e\displaystyle\boldsymbol{w}\_{e} | =\displaystyle= | n−12b−12​𝒛b\displaystyle\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Phi}\_{b}^{-\frac{1}{2}}\boldsymbol{z}\_{b} |  | (63) |
|  |  | =\displaystyle= | n−12(−12𝑴𝑴−12)−12−12𝑴𝒔e\displaystyle\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e} |  |
|  |  | =\displaystyle= | n−12​Rb​(𝑴​𝑴)−12​𝑴​𝒔e\displaystyle\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{b}\left(\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\right)^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e} |  |

where Rb=(−12𝑴𝑴−12)−12−12(𝑴𝑴)12\mathbb{R}\_{b}=\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\right)^{\frac{1}{2}} is a rotation.

From our previous discussion, we know that it can expressed from the singular value decomposition of −12+12=−12(𝑴𝑴)+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Phi}^{+\frac{1}{2}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\right)^{+\frac{1}{2}} as:

|  |  |  |
| --- | --- | --- |
|  | Rb=𝑩check​𝑼check​with−12​(𝑴​𝑴)+12=𝑩check​check​𝑼check\mathbb{R}\_{b}=\boldsymbol{\check{B}}\boldsymbol{\check{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \text{with}\ \boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\right)^{+\frac{1}{2}}=\boldsymbol{\check{B}}\boldsymbol{\check{\Psi}}\boldsymbol{\check{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  |

#### 3.2.2 Working in ℋs\mathcal{H}\_{s}

We can also work directly from the space of signals 𝒔\boldsymbol{s} in ℋs\mathcal{H}\_{s}. The mean-variance framework can be rephrased as:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒘e\displaystyle\boldsymbol{w}\_{e} | =\displaystyle= | 1−1​𝑴​𝒔e\displaystyle\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e} |  | (64) |
|  |  | =\displaystyle= | 1−12​𝑼​(𝑼−12​𝑴12​𝑽)​𝑽−12​𝒔e\displaystyle\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{U}\left(\boldsymbol{U}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\boldsymbol{V}\right)\boldsymbol{V}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  |

Comparing Eq. [64](https://arxiv.org/html/2511.13334v1#S3.E64 "In 3.2.2 Working in ℋ_𝑠 ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") with Eq. [62](https://arxiv.org/html/2511.13334v1#S3.E62 "In 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we define the “best” isotropic allocation as the two orthonormal bases, encoded by the matrices 𝑩dot\boldsymbol{\dot{B}} and 𝑼dot\boldsymbol{\dot{U}} of size n​nn\times n and size m​nm\times n respectively, that aligns best 𝑩dot−12​𝑴12​𝑼dot\boldsymbol{\dot{B}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\boldsymbol{\dot{U}} with the identity matrix I​dn\mathbb{Id}\_{n}. The basis 𝑼dot\boldsymbol{\dot{U}} spans a linear space Rn\sim\mathbb{R}^{n} that is strictly included in ℋs​Rm\mathcal{H}\_{s}\sim\mathbb{R}^{m} as soon as n<mn<m.

This can be easily determined through a singular value decomposition of −12𝑴+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}} (and keeping for 𝑼dot\boldsymbol{\dot{U}} only the first nn right-singular vectors 𝑼dotn\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | −12𝑴+12=𝑩dotdot𝑼dot=𝑩dotdotn𝑼dotn\displaystyle\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\boldsymbol{\dot{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  | (65) |

We end up with a generalization of Eq. [55](https://arxiv.org/html/2511.13334v1#S3.E55 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"):

Isotropy-Enforced Allocationm​n,E​[𝒓|ℱ]​𝑴​𝒔𝒘e=n−12​𝑩dot​𝑼dotn−12​𝒔e​with−12​𝑴+12=𝑩dot​dot​𝑼dot\displaystyle\begin{array}[]{c}\text{\bf Isotropy-Enforced Allocation}\\
m\geq n,\ \ E[\boldsymbol{r}|\mathcal{F}]\propto\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\\
\\
\boldsymbol{w}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\dot{B}}\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\ \text{with}\ \boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\boldsymbol{\dot{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\end{array}

(70)

As m​nm\geq n, the rank of −12𝑴+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}} is nn (except in pathological cases). We note that we have the following:

|  |  |  |
| --- | --- | --- |
|  | (−12𝑴𝑴−12)−12−12𝑴+12=𝑩dot𝑼dotn\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  |

This leads to the same solution as Eq. [63](https://arxiv.org/html/2511.13334v1#S3.E63 "In 3.2.1 Working with mapped signals 𝒛=𝑴^\"\"⁢𝒔 ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") above, that is:

|  |  |  |
| --- | --- | --- |
|  | 𝒘e=n−12(−12𝑴𝑴−12)−12−12𝑴𝒔e\boldsymbol{w}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}\boldsymbol{M}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e} |  |

It is worth mentioning that one could have chosen to work from the perspective of any other isotropic basis. This would not change the theoretical results, but might be recommended for some efficiency reasons, e.g. numerical stability.

For instance, we might want to use the Cholesky decompositions =𝑳​𝑳\boldsymbol{\Omega}=\boldsymbol{L}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} and =𝑳​𝑳\boldsymbol{\Xi}=\boldsymbol{L}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} (see Eq. [18](https://arxiv.org/html/2511.13334v1#S2.E18 "In 2.3.3 Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).
We rephrase Eq. [70](https://arxiv.org/html/2511.13334v1#S3.E70 "In 3.2.2 Working in ℋ_𝑠 ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") as:

|  |  |  |
| --- | --- | --- |
|  | 𝒘e=1​𝑳−​𝑩check​𝑼checkn​𝑳−1​𝒔e​with​𝑳−1​𝑴​𝑳=𝑩check​check​𝑼check\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{L}^{-{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\check{B}}\boldsymbol{\check{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}^{-1}\boldsymbol{s}\_{e}\ \text{with}\ \boldsymbol{L}^{-1}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}=\boldsymbol{\check{B}}\boldsymbol{\check{\Psi}}\boldsymbol{\check{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  |

Because we have 𝑳=12Rbhat\boldsymbol{L}=\boldsymbol{\Omega}^{\frac{1}{2}}\mathbb{R}\_{\hat{b}} and 𝑳=12Ruhat\boldsymbol{L}=\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}, we can easily see that the solution is identical with:

|  |  |  |
| --- | --- | --- |
|  | check=dot,𝑩check=Rbhat​𝑩dot,𝑼check=Ruhat​𝑼dot\boldsymbol{\check{\Psi}}=\boldsymbol{\dot{\Psi}},\hskip 28.45274pt\boldsymbol{\check{B}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\dot{B}},\hskip 28.45274pt\boldsymbol{\check{U}}=\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\dot{U}} |  |

#### 3.2.3 Isotropic-Mean Allocation

Let’s look at the main case of interest, the general mean-variance solution of Eq. [7](https://arxiv.org/html/2511.13334v1#S2.E7 "In 2.2.1 Mean-Variance Functional and Solution ‣ 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") where 𝑴==−1\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\beta}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}. We can compare the mean-variance solution, our departing point:

|  |  |  |
| --- | --- | --- |
|  | 𝒘e=1−1−1​𝒔e=1−12​tilde−12​𝒔e\boldsymbol{w}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{\Pi}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  |

with the allocation of Eq. [63](https://arxiv.org/html/2511.13334v1#S3.E63 "In 3.2.1 Working with mapped signals 𝒛=𝑴^\"\"⁢𝒔 ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") that we express as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘e=n−12​(tilde​tilde)−12​tilde−12​𝒔e\displaystyle\boldsymbol{w}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)^{-\frac{1}{2}}\boldsymbol{\tilde{\Pi}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e} |  | (71) |

The effect of the isotropic allocation is to replace the normalized canonical correlation tilde=𝑩tilde​tilde​𝑼tilde\boldsymbol{\tilde{\Pi}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} (see Eq. [27](https://arxiv.org/html/2511.13334v1#S2.E27 "In 2.3.6 Canonical Portfolios ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")) by another version (tilde​tilde)−12​tilde=tilde​(tilde​tilde)−12=𝑩tilde​𝑼tilden\left(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)^{-\frac{1}{2}}\boldsymbol{\tilde{\Pi}}=\boldsymbol{\tilde{\Pi}}\left(\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)^{-\frac{1}{2}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}, leading to a concept of eigenrisk parity across canonical portfolios (see Section [2.3.6](https://arxiv.org/html/2511.13334v1#S2.SS3.SSS6 "2.3.6 Canonical Portfolios ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). We refer to this allocation as Isotropic-Mean (IM).

Isotropic-Mean Allocationm​n,E​[𝒓|ℱ]=−1𝒔𝒘e=n−12​𝑩tilde​𝑼tilden−12​𝒔e=n​\slimits@k=1N​𝒘tildek​tilde=−12−12=𝑩tildetilde𝑼tildeand𝒘tildek=−12𝑩tildek𝑼tildek−12𝒔e\displaystyle\begin{array}[]{c}\text{\bf Isotropic-Mean Allocation}\\
m\geq n,\ \ E[\boldsymbol{r}|\mathcal{F}]=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}\\
\\
\boldsymbol{w}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}=\frac{\sigma}{\sqrt{n}}\sumop\slimits@\_{k=1}^{N}{\boldsymbol{\tilde{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \ \text{and}\ \ \boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}

(77)

The canonical portfolios 𝒘tildek\boldsymbol{\tilde{w}}\_{k} (still ordered by their canonical correlations tilde1​tilde2​…​0\tilde{\Psi}\_{1}\geq\tilde{\Psi}\_{2}\geq...\geq 0) are equally invested, leading to a realized Sharpe (measured in-sample)171717Note that we have 0​1n​Tr​(tilde)​Tr​(tilde2)0\leq\frac{1}{\sqrt{n}}\text{Tr}\left(\boldsymbol{\tilde{\Psi}}\right)\leq\sqrt{\text{Tr}\left(\boldsymbol{\tilde{\Psi}}^{2}\right)}, so that in-sample 0​Sharpe(Eigenrisk)Sharpe(Mean-Variance)0\leq\text{Sharpe(Eigenrisk)}\leq\text{Sharpe(Mean-Variance)}. We have equality when all singular values are identical.
:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sharpe=1n​Tr​(tilde)​0\displaystyle\text{Sharpe}=\frac{1}{\sqrt{n}}\text{Tr}\left(\boldsymbol{\tilde{\Psi}}\right)\geq 0 |  | (78) |

The general allocation of Eq. [70](https://arxiv.org/html/2511.13334v1#S3.E70 "In 3.2.2 Working in ℋ_𝑠 ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and its reduced version Isotropic-Mean of Eq. [70](https://arxiv.org/html/2511.13334v1#S3.E70 "In 3.2.2 Working in ℋ_𝑠 ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (when 𝑴==−1\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\beta}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}) extend and generalize the concept of ERP allocation introduced in [benichou-16] and [segonne-2024].

It is the best isotropy optimally aligned in the MV direction as encoded by the normalized predictability matrix tilde\boldsymbol{\tilde{\Pi}}.

Isotropic-Mean as expressed as Eq. [71](https://arxiv.org/html/2511.13334v1#S3.E71 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") shares some striking similarities with the principal portfolio allocation derived in [PrincipalPortfolios2020]; both approaches have been designed to manage some form of uncertainty, although through two different perspectives.

#### 3.2.4 Principal Portfolios [PrincipalPortfolios2020] and Invariance

Principal Portfolios, introduced in [PrincipalPortfolios2020], have been designed to add robustness to the inference problem by introducing a different risk measure. The original formulation assumes the same number of signals as assets (i.e. m=nm=n), where each signal sis\_{i} has been designed for a particular asset rir\_{i} (as discussed in Section [3.1](https://arxiv.org/html/2511.13334v1#S3.SS1 "3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

The main idea is to deviate replace the variance estimation by a more robust measure of risk that is independent of the distribution of 𝒔\boldsymbol{s}.
Instead of estimating risk as the variance Var​[𝒔​𝑳​𝒓]\text{Var}\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right] computed over the joint distribution of 𝒔\boldsymbol{s} and 𝒓\boldsymbol{r} (see Eq. [5](https://arxiv.org/html/2511.13334v1#S2.E5 "In 2.2 Trading: Mean-Variance Framework ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")), [PrincipalPortfolios2020] suggests to use a worst-case scenario, estimating risk as the maximum variance realized across a universe of bounded signals:

|  |  |  |
| --- | --- | --- |
|  | max\|​𝒔​\|​1⁡Var​[𝒔​𝑳​𝒓]=max𝒔​𝟎⁡1\|​𝒔​\|2​Var​[𝒔​𝑳​𝒓]\max\_{\|\boldsymbol{s}\|\leq 1}\text{Var}\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]=\max\_{\boldsymbol{s}\ne\boldsymbol{0}}\frac{1}{\|\boldsymbol{s}\|^{2}}\text{Var}\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right] |  |

The definition avoids the integral over the signal distribution (𝒔\boldsymbol{s} is not considered as a stochastic variable), using only a bounding Euclidean sphere. Consequently, it does not require estimating the signal correlation (those are usually harder to estimate than and tends to be less stable). It is also a more robust measure since it requires the variance to be bounded independently of the realization of the signal 𝒔\boldsymbol{s} (this is a worst-case scenario).

The above risk measure depends on the basis one is working with (where the bounding sphere is defined and where the variance is computed). This means that there is ambiguity but also flexibility. To avoid being implicitly impacted by the asset correlation/covariance , the norm should be defined in an isotropic basis [PrincipalPortfolios2020].

For instance, working in the Riccati basis {𝒃i}\{\boldsymbol{b}\_{i}\}, we have the following equality 𝒔Var​[𝒔​𝑳b​b​𝒓b]=\|​𝑳b​b​𝒔​\|2\forall\boldsymbol{s}\ \ \text{Var}\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\_{bb}\boldsymbol{r}\_{b}\right]=\|\boldsymbol{L}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\|^{2}, and the risk constraint becomes a straight-forward constraint on the (triple) norm of the operator 𝑳b​b\boldsymbol{L}\_{bb} (expressed in {𝒃i}\{\boldsymbol{b}\_{i}\} with 𝑳b​b=12𝑳12\boldsymbol{L}\_{bb}=\boldsymbol{\Omega}^{\frac{1}{2}}\boldsymbol{L}\boldsymbol{\Omega}^{\frac{1}{2}} - recall that m=nm=n in the original publication [PrincipalPortfolios2020]):

|  |  |  |
| --- | --- | --- |
|  | \|​𝑳b​b​\|2=max𝒔​𝟎⁡\|​𝑳b​b​𝒔​\|2\|​𝒔​\|2\displaystyle\|\boldsymbol{L}\_{bb}\|^{2}=\max\_{\boldsymbol{s}\ne\boldsymbol{0}}\frac{\|\boldsymbol{L}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\|^{2}}{\|\boldsymbol{s}\|^{2}} |  |

The allocation problem can then be expressed (in {𝒃i}\{\boldsymbol{b}\_{i}\}) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑳b​b=arg𝑳⁡max\|​𝑳​\|⁡Tr​(𝑳b​b)\displaystyle\boldsymbol{L}\_{bb}=\arg\_{\boldsymbol{L}}\max\_{\|\boldsymbol{L}\|\leq\sigma}{\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\_{bb}\right)} |  | (79) |

with solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑳b​b=n(b​bb​b)−12b​b=nb​b(b​bb​b)−12,\displaystyle\boldsymbol{L}\_{bb}=\frac{\sigma}{\sqrt{n}}\left(\boldsymbol{\Pi}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\_{bb}\right)^{-\frac{1}{2}}\boldsymbol{\Pi}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Pi}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\left(\boldsymbol{\Pi}\_{bb}\boldsymbol{\Pi}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)^{-\frac{1}{2}}, |  | (80) |

which exhibits a similar form as Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").
The concept of principal portfolios follows nicely from another singular value decomposition of the predictability matrix b​b\boldsymbol{\Pi}\_{bb} expressed in {𝒃i}\{\boldsymbol{b}\_{i}\}.

To explore further the similarities between both solutions Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and Eq. [80](https://arxiv.org/html/2511.13334v1#S3.E80 "In 3.2.4 Principal Portfolios [PrincipalPortfolios2020] and Invariance ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we depart from the original spirit of [PrincipalPortfolios2020] and suggest to choose different bases, searching directly for an operator 𝑳u​b\boldsymbol{L}\_{ub} defined between isotropic bases {𝒖i}\{\boldsymbol{u}\_{i}\} and {𝒃i}\{\boldsymbol{b}\_{i}\} and under the constraint \|​𝑳u​b​\|\|\boldsymbol{L}\_{ub}\|\leq\sigma. We also do not assume that m=nm=n anymore and put ourselves in the general setting m​nm\geq n.

The allocation problem can be rephrased as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑳u​b\displaystyle\boldsymbol{L}\_{ub} | =\displaystyle= | arg𝑳⁡max\|​𝑳​\|⁡Tr​(𝑳​tilde)\displaystyle\arg\_{\boldsymbol{L}}\max\_{\|\boldsymbol{L}\|\leq\sigma}{\text{Tr}\left(\boldsymbol{L}\boldsymbol{\tilde{\Pi}}\right)} |  |

with solution:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝑳\displaystyle\boldsymbol{L} | =\displaystyle= | −12𝑳u​b−12\displaystyle\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{L}\_{ub}\boldsymbol{\Omega}^{-\frac{1}{2}} |  | (81) |
|  |  | =\displaystyle= | n−12​tilde​(tilde​tilde)−12−12\displaystyle\frac{\sigma}{\sqrt{n}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\left(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}} |  |

This is the same solution as Eq. [71](https://arxiv.org/html/2511.13334v1#S3.E71 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") above. This is puzzling at first. Although both approaches are different in spirit (one is force-aligning an isotropic form Eq. [55](https://arxiv.org/html/2511.13334v1#S3.E55 "In 3.1.2 Balanced Isotropic Allocations ‣ 3.1 The Balanced Case 𝑚=𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") in the direction of the normalized predictability, the other is maximizing expected returns under a robust risk metric defined between isotropic bases), we end up with the same solution. Both are trying to build resilience.

The reason is structural: by working in isotropic bases {𝒃i}\{\boldsymbol{b}\_{i}\}, {𝒖i}\{\boldsymbol{u}\_{i}\}, we constrain the solution space to isotropic linear applications. This is explicit in BI; implicit in principal portfolios [PrincipalPortfolios2020].

Crucially, the allocation is *invariant under rotations* of the isotropic bases181818Let 𝒃hati=−1/2Rbhat​𝒆i\boldsymbol{\hat{b}}\_{i}=\boldsymbol{\Omega}^{-1/2}\mathbb{R}\_{\hat{b}}\boldsymbol{e}\_{i}, 𝒖hati=−1/2Ruhat​𝒆i\boldsymbol{\hat{u}}\_{i}=\boldsymbol{\Xi}^{-1/2}\mathbb{R}\_{\hat{u}}\boldsymbol{e}\_{i}. Then (bhat​uhatbhat​uhat)−1/2=Rbhat(tildetilde)−1/2Rbhat(\boldsymbol{\Pi}\_{\hat{b}\hat{u}}\boldsymbol{\Pi}\_{\hat{b}\hat{u}})^{-1/2}=\mathbb{R}\_{\hat{b}}(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}})^{-1/2}\mathbb{R}\_{\hat{b}}, so 𝑳=−1/2𝑳u​b−1/2\boldsymbol{L}=\boldsymbol{\Xi}^{-1/2}\boldsymbol{L}\_{ub}\boldsymbol{\Omega}^{-1/2} is rotation-invariant.
. Only isotropy itself, and not orientation, conditions the solution191919This rotational invariance mirrors gauge symmetry in physics: the constraint, not the coordinate, defines the physics.
.

This perspective is particularly relevant in the context of principal portfolio methodology, where the choice of basis might obscure this invariance (to rotations) at first glance. The BI approach makes the invariance clearer, as the isotropic constraint directly shapes the solution space.

Rotational invariance is not exclusive to isotropic bases: the triple-norm objective and expected return are both invariant under S​O​(n)​S​O​(m)SO(n)\times SO(m) rotations of the anchor bases in ℋr\mathcal{H}\_{r} and ℋs\mathcal{H}\_{s}.

The principal portfolio optimization thus defines solutions on a principal bundle with S​O​(m)​S​O​(n)SO(m)\times SO(n) symmetry: entire orbits of equivalent allocations collapse to a single geometric configuration.

Only when anchors are isotropic do principal portfolios reduce to canonical portfolios:

|  |  |  |
| --- | --- | --- |
|  | 𝒘tildek=−1/2𝑩tildek​𝑼tildek−1/2​𝒔,\boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-1/2}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}\boldsymbol{\Xi}^{-1/2}\boldsymbol{s}, |  |

with equal weighting across modes, reproducing the isotropic-mean allocation (Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).
Isotropy is the symmetry that unifies.

### 3.3 Take-Aways

•

Given a general allocation expressed as 𝒘−1​𝑴​𝒔\boldsymbol{w}\propto\boldsymbol{\Omega}^{-1}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}, a “pure” isotropic allocation with “minimal” distortion can be achieved by enforcing isotropy in the direction most aligned with the matrix −12𝑴+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}, that is by identifying the orthogonal transformations 𝑼\boldsymbol{U} and 𝑽\boldsymbol{V} so that 𝑼−12​𝑴+12​𝑽\boldsymbol{U}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}\boldsymbol{V} is as close as possible to the identity matrix I​d\mathbb{Id} (in the sense of the Frobenius norm). We obtain:



𝒘=n−12​𝑩dot​𝑼dotn−12​𝒔​where−12​𝑴+12=𝑩dot​dot​𝑼dot\boldsymbol{w}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\dot{B}}\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\ \text{where}\ \boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\boldsymbol{\dot{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}
•

When the allocation is issued from a general mean-variance optimization 𝒘−1−1​𝒔\boldsymbol{w}\propto\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}, the resulting isotropic-mean solution is equally allocated along canonical portfolios 𝒘tildek\boldsymbol{\tilde{w}}\_{k}, built from the singular vectors of the normalized predictability matrix tilde=−12−12\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}:



𝒘\displaystyle\boldsymbol{w}
=\displaystyle=
n−12​(tilde​tilde)−12​tilde−12​𝒔=n​\slimits@k=1N​𝒘tildek​\displaystyle\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)^{-\frac{1}{2}}\boldsymbol{\tilde{\Pi}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}=\frac{\sigma}{\sqrt{n}}\sumop\slimits@\_{k=1}^{N}{\boldsymbol{\tilde{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}
•

In the simple setup where E​[𝒓|ℱ]​𝒔E[\boldsymbol{r}|\mathcal{F}]\propto\boldsymbol{s} (that is when m=nm=n and 𝑴=Id)\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\mathbb{Id}) , the isotropy-enforced allocation takes the form 𝑳=n−12(−12−12)−12−12𝒔\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{s}, slightly different from the ERP approach of [benichou-16].
•

Principal portfolios [PrincipalPortfolios2020] have the same solution when the initial choice of basis is isotropic (i.e. when the triple norm is expressed between isotropic bases). Therefore, similar techniques of principal exposure portfolios and principal alpha portfolios could be applied (see [PrincipalPortfolios2020]), and will be explored in further work.
•

Although the solution does not depend on the specific choice of isotropic bases, one could employ alternative ones, such as those designed for enhanced stability (e.g. Cholesky or others).

The above methodology enforces strictly isotropy on both return and signal sides. This strong constraint might deform significantly the initial mean-variance allocation and the approach lacks direct control over portfolio deformation. We address this issue next.

## 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty

The “pure” (or exact) isotropic allocations of Section [3](https://arxiv.org/html/2511.13334v1#S3 "3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") have been achieved by enforcing isotropy in the direction most aligned with the normalized predictability matrix tilde\boldsymbol{\tilde{\Pi}}. However, the resulting allocations could deviate significantly from the original mean-variance solution, as no direct control is offered202020To be exact, we noticed an equivalence with the principal portfolios methodology, so there exist nonetheless an element of control through the triple norm of the operator 𝑳\boldsymbol{L}. However, this requires anchoring the solution exactly between two isotropic bases, a forced implicit constraint on which no control exist.
. By working from a risk perspective only, the resulting solution might deviate significantly from the departing mean-variance allocation (especially when the covariances and become large).

We suggest to augment the mean-variance framework by adding an isotropy constraint, thereby offering an adjustable trade-off between return maximization, variance minimization, and isotropic control.

To naturally integrate some notion of isotropy within the mean-variance framework,
we decompose our generic portfolio allocation 𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} in the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑳=n−12​𝑻−12,\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{T}\boldsymbol{\Xi}^{-\frac{1}{2}}, |  | (82) |

where 𝑻​ℛn​m\boldsymbol{T}\in\mathcal{R}^{n\times m} is the unknown mapping from ℋs​ℛm\mathcal{H}\_{s}\sim\mathcal{R}^{m} into ℋr​ℛn\mathcal{H}\_{r}\sim\mathcal{R}^{n}. The linear operator 𝑻\boldsymbol{T} is our unknown.

Using the formulation Eq. [82](https://arxiv.org/html/2511.13334v1#S4.E82 "In 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we have the following:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​[𝒘​𝒓]\displaystyle E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right] | =\displaystyle= | Tr​(𝑳)=n​Tr​(𝑻​tilde)\displaystyle\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right)=\frac{\sigma}{\sqrt{n}}\text{Tr}\left(\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​[𝒘​𝒓]\displaystyle\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right] |  | Tr​(𝑳​𝑳)=2n​Tr​(𝑻​𝑻)\displaystyle\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)=\frac{{}^{2}}{n}\text{Tr}\left(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right) |  |

where tilde\boldsymbol{\tilde{\Pi}} is the cross-correlation between normalized assets and normalized signals expressed into their corresponding Riccati basis {𝒃𝒊}\{\boldsymbol{b\_{i}}\} and {𝒖𝒊}\{\boldsymbol{u\_{i}}\}:

|  |  |  |
| --- | --- | --- |
|  | tilde=b​u=−12−12\displaystyle\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Pi}\_{bu}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}} |  |

Our isotropy-regularized mean-variance (IRMV) framework aims to maximize the returns under two constraints:

* •

  a standard volatility constraint where we cap the total variance at 2:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Var[𝒘𝒓]2\displaystyle\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]\leq{}^{2} |  | (83) |
* •

  an isotropy (i.e. orthogonality) constraint through:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 1n​‖𝑻​𝑻−I​dn‖F2​2\displaystyle\frac{1}{n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}}\leq 2\tau |  | (84) |

  where controls the amount of isotropy we desire. The positive parameter 1\eta\leq 1, typically chosen close to 1, tilts slightly the variance down to take care of the convexity. This implicitly bounds the variance as we discuss below212121We could have used an orthogonality penalty of the form 1n​‖𝑻​𝑻−Tr​(𝑻​𝑻)n​I​dn‖F2\frac{1}{n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\frac{\text{Tr}(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}})}{n}\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}}; our choice allows for a volatility control even in the absence of volatility constraint.
  .

### 4.1 Isotropy Penalty and Participation Ratio

To better understand our additional isotropy penalty, we consider a general portfolio allocation 𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}. Without loss of generality, we express the allocation as:

|  |  |  |
| --- | --- | --- |
|  | 𝒘=n−1​𝑴​𝒔\boldsymbol{w}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-1}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} |  |

the volatility is set at the current level =Tr​(𝑳​𝑳)\sigma=\sqrt{\text{Tr}\left(\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Xi}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)} and 𝑴=n​𝑳​ℛn​m\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sqrt{n}}{\sigma}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\in\mathcal{R}^{n\times m}.

We follow the same decomposition as Eq. [82](https://arxiv.org/html/2511.13334v1#S4.E82 "In 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑳=n−12​Rbhat​(Rbhat−12​𝑴12​Ruhat)​Ruhat−12\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\left(\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}\right)\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} |  | (85) |

where Rbhat\mathbb{R}\_{\hat{b}} and Ruhat\mathbb{R}\_{\hat{u}} are two rotations, corresponding to the isotropic bases {𝒃hat}\{\boldsymbol{\hat{b}}\} and {𝒖hat}\{\boldsymbol{\hat{u}}\} respectively.

As we saw above, the linear operator:

|  |  |  |
| --- | --- | --- |
|  | 𝑻bhat​uhat=Rbhat−12​𝑴12​Ruhat​ℛn​m\boldsymbol{T}\_{\hat{b}\hat{u}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}\in\mathcal{R}^{n\times m} |  |

facilitates the computation of a few important metrics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {returnE​[𝒘​𝒓]=n​Tr​(𝑻bhat​uhatbhat​uhat)​varianceVar​[𝒘​𝒓]=2n​Tr​(𝑻bhat​uhat​𝑻bhat​uhat)​anisotropy1n​‖𝑻bhat​uhat​𝑻bhat​uhat−I𝑻​dn‖F2\displaystyle\left\{\begin{array}[]{cc}\text{return}&E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]=\frac{\sigma}{\sqrt{n}}\text{Tr}\left(\boldsymbol{T}\_{\hat{b}\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\_{\hat{b}\hat{u}}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \text{variance}&\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]=\frac{{}^{2}}{n}\text{Tr}(\boldsymbol{T}\_{\hat{b}\hat{u}}\boldsymbol{T}\_{\hat{b}\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}})\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \text{anisotropy}&\frac{1}{n}||\boldsymbol{T}\_{\hat{b}\hat{u}}\boldsymbol{T}\_{\hat{b}\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-{}\_{\boldsymbol{T}}\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}}\end{array}\right.\hskip-28.45274pt |  | (89) |

where the parameter T could be chosen as n​Tr​(𝑻𝒃hat​𝒖hat​𝑻𝒃hat​𝒖hat)\frac{\eta}{n}\text{Tr}(\boldsymbol{T\_{\hat{b}\hat{u}}}\boldsymbol{T\_{\hat{b}\hat{u}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}) or as constant =𝑻{}\_{\boldsymbol{T}}=\eta. We can easily check that those metrics are intrinsic as they do not depend on the specifics of Rbhat\mathbb{R}\_{\hat{b}} and Ruhat\mathbb{R}\_{\hat{u}}.

The singular value decomposition of the matrix 𝑻𝒃hat​𝒖hat\boldsymbol{T\_{\hat{b}\hat{u}}} is:

|  |  |  |
| --- | --- | --- |
|  | 𝑻bhat​uhat=Rbhat−12​𝑴12​Ruhat=Rbhat​𝑩dot​dot​(Ruhat​𝑼dot)\boldsymbol{T}\_{\hat{b}\hat{u}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\left(\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\dot{U}}\right)^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  |

where −12𝑴+12=𝑩dotdot𝑼dot\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\boldsymbol{\dot{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}. This is the same singular value decomposition that we already saw in Eq. [65](https://arxiv.org/html/2511.13334v1#S3.E65 "In 3.2.2 Working in ℋ_𝑠 ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

By setting =Tr​(𝑳​𝑳)\sigma=\text{Tr}\left(\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Xi}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right), we are in a situation where the variance of the general portfolio 𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} is set at the variance cap in Eq. [83](https://arxiv.org/html/2511.13334v1#S4.E83 "In 1st item ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). In this scenario, Tr​(dot2)=n\text{Tr}(\boldsymbol{\dot{\Psi}}^{2})=n by construction and the isotropy metric takes the following simplified form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | anisotropy=1n​‖dot2−I𝑻​dn‖F2=1n​Tr​(dot4)−(2−)\displaystyle\text{anisotropy}=\frac{1}{n}||\boldsymbol{\dot{\Psi}}^{2}-{}\_{\boldsymbol{T}}\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}}=\frac{1}{n}\text{Tr}(\boldsymbol{\dot{\Psi}}^{4})-\eta(2-\eta) |  | (90) |

The isotropy metric measures the variability of the eigenpectrum dot\boldsymbol{\dot{\Psi}} of the matrix −12𝑴+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}. This is achieved through its participation ratio dot\dot{\psi}:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | variance constraint | :\displaystyle: | Tr​(dot2)=n​\displaystyle\text{Tr}(\boldsymbol{\dot{\Psi}}^{2})=n\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (91) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | participation ratiodot\displaystyle\text{participation ratio}\ \ \dot{\psi} | =\displaystyle= | 1n​Tr2​(tilde𝟐)Tr​(tilde4)=nTr​(tilde4)​\displaystyle\frac{1}{n}\frac{\text{Tr}^{2}(\boldsymbol{\tilde{\Psi}^{2}})}{\text{Tr}(\boldsymbol{\tilde{\Psi}}^{4})}=\frac{n}{\text{Tr}(\boldsymbol{\tilde{\Psi}}^{4})}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (92) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | anisotropy | =\displaystyle= | 1dot−(2−)​\displaystyle\frac{1}{\dot{\psi}}-\eta(2-\eta)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (93) |

When =Tr​(𝑳​𝑳)\sigma=\text{Tr}\left(\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Xi}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right), our isotropy penalty act as geometric regularizer on the eigenspectrum of −12𝑴+12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}} through the inverse of its participation ratio dot\dot{\psi}. It is purely intrinsic as it does not depend on the previous choice of isotropic bases.

Let’s look at the special case of the mean-variance framework. We have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒘\displaystyle\boldsymbol{w} | =\displaystyle= | Tr​(tilde​tilde)−12​tilde−12​𝒔\displaystyle\frac{\sigma}{\sqrt{\text{Tr}(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}})}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{\Pi}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s} |  |

We can easily see that Var[𝒘𝒓]=2\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]={}^{2} by construction. With variance saturated at , the isotropy metric becomes a function of the participation ratio tilde\tilde{\psi} of the normalized predictability matrix tilde\boldsymbol{\tilde{\Pi}}. It measures the variability of the eigenspectrum tilde\boldsymbol{\tilde{\Psi}} through its inverse of the participation ratio.

The above analysis sheds some light on our isotropy-regularized mean-variance framework and the constraints applied to the operator 𝑻\boldsymbol{T} through Eq. [83](https://arxiv.org/html/2511.13334v1#S4.E83 "In 1st item ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and Eq. [84](https://arxiv.org/html/2511.13334v1#S4.E84 "In 2nd item ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). As the solution tries to line up on tilde\boldsymbol{\tilde{\Pi}} through return maximization, a concentrated eigenspectrum tilde\boldsymbol{\tilde{\Psi}} with a low participation ratio tilde\tilde{\psi} will generate a conflicting situation, as both constraints won’t be able to be saturated. As variance approaches saturation, the isotropy metric becomes exactly — ignoring the constant −(2−)-\eta(2-\eta) — the inverse participation ratio.

As we work between isotropic bases {𝒃i}\{\boldsymbol{b}\_{i}\} and {𝒖i}\{\boldsymbol{u}\_{i}\}, our formulation naturally penalizes situations where the uncertainty loads onto too few modes, reconciling the pure isotropic allocations (e.g. isotropic-mean) defined in Section [3](https://arxiv.org/html/2511.13334v1#S3 "3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") with the mean-variance framework [markowitz\_1, markowitz\_2]. The approach is intrinsic, as the solution do not depend on the specific choice of {𝒃i}\{\boldsymbol{b}\_{i}\} and {𝒖i}\{\boldsymbol{u}\_{i}\}.

### 4.2 Functional Formulation

Introducing Lagrange coefficient 2\frac{\gamma}{2} and 4\frac{\lambda}{4}, the IMV functional to optimize takes the following form:

|  |  |  |
| --- | --- | --- |
|  | 1n​Tr​(𝑻​tilde)−2​n​Tr​(𝑻​𝑻)−4​n​‖𝑻​𝑻−I​dn‖F2\displaystyle\frac{1}{\sqrt{n}}\text{Tr}\left(\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)-\frac{\gamma}{2n}\text{Tr}\left(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)-\frac{\lambda}{4n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}} |  |

with first-order condition:

|  |  |  |
| --- | --- | --- |
|  | n​tilde=𝑻+𝑻​(𝑻​𝑻−I​dn)\sqrt{n}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\gamma\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}+\lambda\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\left(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}\_{n}\right) |  |

We can gain some insight by working the bases 𝑩tilde\boldsymbol{\tilde{B}} and 𝑼tilde\boldsymbol{\tilde{U}} obtained through the singular value decomposition of the predictability matrix tilde\boldsymbol{\tilde{\Pi}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | tilde=𝑩tilde​tilde​𝑼tilde=𝑩tilde​tilden​𝑼tilden\displaystyle\boldsymbol{\tilde{\Pi}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  | (94) |

We express the operator 𝑻\boldsymbol{T} in the bases 𝑩tilde\boldsymbol{\tilde{B}} and 𝑼tilde\boldsymbol{\tilde{U}} as:

|  |  |  |
| --- | --- | --- |
|  | 𝑻=𝑩tilde​𝑼tildewithℛn​m\boldsymbol{T}=\boldsymbol{\tilde{B}}\boldsymbol{\Theta}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \ \text{with}\ \ \boldsymbol{\Theta}\in\mathcal{R}^{n\times m} |  |

We obtain the following equality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ntilde=+(−Idn)\displaystyle\sqrt{n}\boldsymbol{\tilde{\Psi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\gamma\boldsymbol{\Theta}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}+\lambda\boldsymbol{\Theta}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\left(\boldsymbol{\Theta}\boldsymbol{\Theta}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}\_{n}\right) |  | (95) |

We can show that the solution takes the form =[n, 0n,m−n]\boldsymbol{\Theta}=[\boldsymbol{\Theta}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}},\ \mathbb{0}\_{n,m-n}] where n\boldsymbol{\Theta}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}} is diagonal with elements i verifying:

ci=ntildei=+i(−i2)i=(−)+ii3\displaystyle c\_{i}=\sqrt{n}\tilde{\Psi}\_{i}=\gamma{}\_{i}+\lambda{}\_{i}({}\_{i}^{2}-\eta)=(\gamma-\eta\lambda){}\_{i}+\lambda{}\_{i}^{3}

(96)

where we have defined ci=n​tildeic\_{i}=\sqrt{n}\tilde{\Psi}\_{i}. The optimized allocation can be decomposed along a set of nn canonical portfolios (as in [CanonicalPortfolios2023]):

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝑻\displaystyle\boldsymbol{T} | =\displaystyle= | 𝑩tilde​𝑼tilde=𝑩tilden​𝑼tilden​\displaystyle\boldsymbol{\tilde{B}}\boldsymbol{\Theta}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\tilde{B}}\boldsymbol{\Theta}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (97) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝑳\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} | =\displaystyle= | n−12​𝑻−12​\displaystyle\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{T}\boldsymbol{\Xi}^{-\frac{1}{2}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (98) |
|  |  | =\displaystyle= | \slimits@i=1n​n−12i​𝑩tildei​𝑼tildei−12​\displaystyle\sumop\slimits@\_{i=1}^{n}{}\_{i}\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{i}\boldsymbol{\tilde{U}}\_{i}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |

The expected returns and variance are computed as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​[𝒘​𝒓]\displaystyle E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right] | =\displaystyle= | nTr(tilde)=n\slimits@tildekk=n\slimits@ckk\displaystyle\frac{\sigma}{\sqrt{n}}\text{Tr}\left(\boldsymbol{\Theta}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Psi}}\right)=\frac{\sigma}{\sqrt{n}}\sumop\slimits@{{}\_{k}\tilde{\Psi}\_{k}}=\frac{\sigma}{n}\sumop\slimits@{{}\_{k}c\_{k}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​[𝒘​𝒓]\displaystyle\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right] |  | 2nTr()=2n\slimits@k2\displaystyle\frac{{}^{2}}{n}\text{Tr}\left(\boldsymbol{\Theta}\boldsymbol{\Theta}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)=\frac{{}^{2}}{n}\sumop\slimits@{{}\_{k}^{2}} |  |

with corresponding Sharpe ratio expressed as:

|  |  |  |
| --- | --- | --- |
|  | Sharpe(,𝒄)=1n\slimits@ckk/1n\slimits@k2\text{Sharpe}(\boldsymbol{\theta},\boldsymbol{c})=\frac{1}{n}\sumop\slimits@{{}\_{k}c\_{k}}/\sqrt{\frac{1}{n}\sumop\slimits@{{}\_{k}^{2}}} |  |

The two constraints can be expressed as:

1n\slimits@k2\displaystyle\frac{1}{n}\sumop\slimits@{{}\_{k}^{2}}

1variance\displaystyle 1\ \ \ \ \ \text{variance}

(99)


1n\slimits@(−k2)2\displaystyle\frac{1}{n}\sumop\slimits@{({}\_{k}^{2}-\eta)^{2}}

2isotropy\displaystyle 2\tau\ \ \ \ \ \text{isotropy}

(100)

The Jensen inequality shows that the isotropy constraint offers an implicit control of volatility:

|  |  |  |
| --- | --- | --- |
|  | 1n\slimits@(−k2)2(1n\slimits@−k2)2\frac{1}{n}\sumop\slimits@{({}\_{k}^{2}-\eta)^{2}}\geq\left(\frac{1}{n}\sumop\slimits@{{}\_{k}^{2}-\eta}\right)^{2} |  |

The variance will be bounded by (2)2{}^{2}(\eta\pm\sqrt{2\tau}) as:

|  |  |  |
| --- | --- | --- |
|  | −21n\slimits@+k22\eta-\sqrt{2\tau}\leq\frac{1}{n}\sumop\slimits@{{}\_{k}^{2}}\leq\eta+\sqrt{2\tau} |  |

However, depending on the choice of , the solution might be lower and settle around our desired value of 11.

We note that the solution does not depend on the magnitude of the eigencurve 𝒄\boldsymbol{c}, only on its shape. Solving the set of coupled equations of Eq. [96](https://arxiv.org/html/2511.13334v1#S4.E96 "In 4.2 Functional Formulation ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") subject to the constraints Eq. [99](https://arxiv.org/html/2511.13334v1#S4.E99 "In 4.2 Functional Formulation ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and Eq. [100](https://arxiv.org/html/2511.13334v1#S4.E100 "In 4.2 Functional Formulation ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") can only be done numerically (without difficulty), but we can gain some insight by looking into some simple scenarios.

### 4.3 Special Cases

We first study some simplifying scenarios and limit properties.

No Isotropy Constraint when +\tau\longrightarrow+\infty (or 0\lambda\longrightarrow 0)

The orthogonality penalization becomes insignificant and we end up with the standard mean-variance solution:

|  |  |  |
| --- | --- | --- |
|  | =ici1n​\slimits@​ck2mean-variance{}\_{i}=\frac{c\_{i}}{\sqrt{\frac{1}{n}\sumop\slimits@{c\_{k}^{2}}}}\ \ \ \ \text{mean-variance} |  |

The solution can be decomposed into canonical portfolios n−12​𝑩tildei​𝑼tildei−12\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{i}\boldsymbol{\tilde{U}}\_{i}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} (each with weight i), leading to an in-sample Sharpe ratio of 1n​\slimits@​ck2\sqrt{\frac{1}{n}\sumop\slimits@c\_{k}^{2}} (see Eq. [28](https://arxiv.org/html/2511.13334v1#S2.E28 "In 1st item ‣ 2.3.6 Canonical Portfolios ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).
We can also check that the operator 𝑻\boldsymbol{T} is 𝑻=1​𝑩tilde​tilde​𝑼tilde=1​tilde\boldsymbol{T}=\frac{1}{\gamma}\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{1}{\gamma}\boldsymbol{\tilde{\Pi}} as expected, and where the leverage coefficient is =Tr​(tilde​tilde)n\gamma=\sqrt{\frac{\text{Tr}\left(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)}{n}}.

There is a value of + for which, the isotropy constraints kicks-in as defined by Eq. [100](https://arxiv.org/html/2511.13334v1#S4.E100 "In 4.2 Functional Formulation ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). The region where only the variance constraint matters is defined by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | + | =\displaystyle= | 12(1n\slimits@−k42+)2\displaystyle\frac{1}{2}\left(\frac{1}{n}\sumop\slimits@{{}\_{k}^{4}}-2\eta+{}^{2}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |
|  |  | =\displaystyle= | 12(1n​\slimits@​ck4(1n​\slimits@​ck2)2−2+)2\displaystyle\frac{1}{2}\left(\frac{\frac{1}{n}\sumop\slimits@{c\_{k}^{4}}}{(\frac{1}{n}\sumop\slimits@{c\_{k}^{2}})^{2}}-2\eta+{}^{2}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |
|  |  |  | 12​(1−)2​\displaystyle\frac{1}{2}\left(1-\eta\right)^{2}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |

We note that the term 1n​\slimits@​ck4/(1n​\slimits@​ck2)2\frac{1}{n}\sumop\slimits@{c\_{k}^{4}}/(\frac{1}{n}\sumop\slimits@{c\_{k}^{2}})^{2} is one over the participation ratio tilde\tilde{\psi} of the eigenspectrum of tilde\boldsymbol{\tilde{\Pi}} as defined in Eq. [92](https://arxiv.org/html/2511.13334v1#S4.E92 "In 4.1 Isotropy Penalty and Participation Ratio ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

When the eigenspectrum is more concentrated (as tilde​0\tilde{\psi}\longrightarrow 0), the limit + increases and the isotropy constraint would be harder and harder to avoid (as desired). On the other hand, when the eigenspectrum becomes flatter (i.e. less concentrated, as tilde​1\tilde{\psi}\longrightarrow 1), although + would decrease towards its lower limit 12​(1−)2\frac{1}{2}\left(1-\eta\right)^{2}, the isotropy constraint would be less and less required (since the eigenspectrum is more and more isotropic).

Full Isotropy when 0\tau\longrightarrow 0 (or +)\lambda\longrightarrow+\infty)

We end up with the same isotropic-mean allocation of Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"):

|  |  |  |
| --- | --- | --- |
|  | iisotropic-mean{}\_{i}\approx\sqrt{\eta}\ \ \ \ \text{isotropic-mean} |  |

The solution can still be decomposed into (the same) canonical portfolios ​n−12​𝑩tildei​𝑼tildei−12\sqrt{\eta}\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{i}\boldsymbol{\tilde{U}}\_{i}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}, but with unit weights. We obtain a lower in-sample Sharpe ratio of 1n​\slimits@​ck\frac{1}{n}\sumop\slimits@c\_{k} (see Eq. [78](https://arxiv.org/html/2511.13334v1#S3.E78 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). We can verify that 𝑻=​𝑩tilde​𝑼tilden\boldsymbol{T}=\sqrt{\eta}\boldsymbol{\tilde{B}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}.

The variance constraint of Eq. [99](https://arxiv.org/html/2511.13334v1#S4.E99 "In 4.2 Functional Formulation ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") is verified (and saturated if and only if =1\eta=1):

|  |  |  |
| --- | --- | --- |
|  | 1n\slimits@=k21\frac{1}{n}\sumop\slimits@{{}\_{k}^{2}}=\eta\leq 1 |  |

No Variance Constraint when 0<10<\tau\mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}}1 and =0\gamma=0

As isotropy implicitly bounds the variance at (+2)2{}^{2}(\eta+\sqrt{2\tau}) thanks to the Jensen inequality, we consider here the case where the variance constraint is fully ignored (setting =0\gamma=0) while the isotropy constraint is tight (i.e. small but strictly positive, only slightly below one).

This leads to an interesting allocation where the coefficients i are the largest zeros of the third-order polynomials (see Figure):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (−i2)i=ci\displaystyle{}\_{i}({}\_{i}^{2}-\eta)=\frac{c\_{i}}{\lambda} |  | (102) |

subject to the isotropy constraint only (again neglecting the variance constraint).

We can use Cardano’s method to express the general solution as:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 0\displaystyle\eta\ne 0\ \ |  | =i23cos(13arccos[3​3232ci])\displaystyle{}\_{i}=2\sqrt{\frac{\eta}{3}}\cos{\left(\frac{1}{3}\arccos[\frac{3\sqrt{3}}{2{}^{\frac{3}{2}}}\frac{c\_{i}}{\lambda}]\right)} |  | (103) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =0\displaystyle\eta=0\ \ |  | =i(ci)13\displaystyle{}\_{i}=\left(\frac{c\_{i}}{\lambda}\right)^{\frac{1}{3}} |  |

with verifying the isotropy condition, which can be written as:

|  |  |  |
| --- | --- | --- |
|  | 1n\slimits@ci>0ci22i=22\frac{1}{n}\sumop\slimits@\_{c\_{i}>0}{\frac{c\_{i}^{2}}{{}\_{i}^{2}}}=2\tau{}^{2}\\ |  |

![[Uncaptioned image]](poly3rd.png)

Although the cubic equation of Eq. [102](https://arxiv.org/html/2511.13334v1#S4.E102 "In 4.3 Special Cases ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") hints at a power-law scaling in ci3\sqrt[3]{\frac{c\_{i}}{\lambda}} for large cic\_{i}, the orthogonal constraint (on ) introduces a non-linear balancing act that caps deviations, pushing the dominant modes to bounded values (typically larger than 11), while the smaller modes hover near isotropy around \sqrt{\eta}. Recall that the solution only depends on the shape of the eigencurve 𝒄\boldsymbol{c}, and not on its magnitude.

The isotropy constraint, while partially controlling the overall variance, with an implicit hard constraint at the cap (+2)2{}^{2}(\eta+\sqrt{2\tau}), adjust the weighting of the eigenmodes of tilde\boldsymbol{\tilde{\Pi}}, tilting the allocation in favor of the most predictable ones, while retaining some level of isotropy overall.

When <1\eta<1, there is a value - (that depends on the shape of the eigenspectrum) under which the variance cap might not be met (saturation or not might depend on the eigenspectrum tilde\boldsymbol{\tilde{\Psi}}). From the bounded variance, we know that:

|  |  |  |
| --- | --- | --- |
|  | 12(1−)2−\frac{1}{2}(1-\eta)^{2}\leq{}^{-} |  |

For instance, when is zero, one can easily see that:

|  |  |  |
| --- | --- | --- |
|  | ==0−12​n\slimits@tildek43/(1n\slimits@tildek23)212{}^{-}\_{\eta=0}=\frac{1}{2n}\sumop\slimits@{\tilde{\Psi}\_{k}^{\frac{4}{3}}}/(\frac{1}{n}\sumop\slimits@{\tilde{\Psi}\_{k}^{\frac{2}{3}}})^{2}\geq\frac{1}{2} |  |

### 4.4 Parameter Selection & Regions

The limit scenarios we discussed above clearly displayed some distinct regions where the constraints (variance and isotropy) might be active or not. Those would depend on the shape of eigenspectrum.

In most application, the number of significant eigenvalues would be small, as computed by the effective rank or the participation ratio, denoted tilde\tilde{\psi}, to determine the variance concentration:

|  |  |  |  |
| --- | --- | --- | --- |
|  | effective rank1n​(\slimits@​ci)2\slimits@​ci2=1n​Tr2​(tilde)Tr​(tilde2)=1n​Tr2​(tilde)Tr​(tilde​tilde)​participation ratio1n​(\slimits@​ci2)2\slimits@​ci4=1n​Tr2​(tilde𝟐)Tr​(tilde4)=1n​Tr2​(tilde​tilde)Tr​(tilde​tilde​tilde​tilde)​\displaystyle\begin{array}[]{lc}\text{effective rank}&\frac{1}{n}\frac{(\sumop\slimits@{c\_{i}})^{2}}{\sumop\slimits@{c\_{i}^{2}}}=\frac{1}{n}\frac{\text{Tr}^{2}(\boldsymbol{\tilde{\Psi}})}{\text{Tr}(\boldsymbol{\tilde{\Psi}}^{2})}=\frac{1}{n}\frac{\text{Tr}^{2}(\boldsymbol{\tilde{\Pi}})}{\text{Tr}(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}})}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \text{participation ratio}&\frac{1}{n}\frac{(\sumop\slimits@{c\_{i}^{2}})^{2}}{\sumop\slimits@{c\_{i}^{4}}}=\frac{1}{n}\frac{\text{Tr}^{2}(\boldsymbol{\tilde{\Psi}^{2}})}{\text{Tr}(\boldsymbol{\tilde{\Psi}}^{4})}=\frac{1}{n}\frac{\text{Tr}^{2}\left(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)}{\text{Tr}\left(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array} |  | (106) |

As we discussed above in Section [4.3](https://arxiv.org/html/2511.13334v1#S4.SS3 "4.3 Special Cases ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), the upper limit + in Eq. [4.3](https://arxiv.org/html/2511.13334v1#S4.Ex148 "4.3 Special Cases ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") where the isotropic constraint kicks-in can be expressed as:

|  |  |  |
| --- | --- | --- |
|  | =+12(1tilde−2+)2{}^{+}=\frac{1}{2}\left(\frac{1}{\tilde{\psi}}-2\eta+{}^{2}\right) |  |

where tilde\tilde{\psi} is the participation ratio. The more concentrated an eigenspectrum is (as the participation ratio tilde\tilde{\psi} decreases towards 0), the more impacted it becomes by the isotropy constraint. Conversely, a flat eigenspectrum (with tilde​1\tilde{\psi}\longrightarrow 1) would require less isotropy constraint, as the problem is naturally more isotropic to start with.

The consequence is that choosing in the 1−21-2 range should offer a good balance between isotropy and mean-variance, independently of the shape of the eigenspectrum.

The lower bound - where variance is not saturated also depends on the shape of the eigenspectrum. Low values of would bound the variance strictly (through the Jensen equality) with the isotropic constraint dominating, but values close to 1 would avoid such scenarios, setting the framework within the influence of the two constraints.

To illustrate the boundaries, we consider two idealized examples, two different eigencurve shapes (recall that the magnitude has no impact on the solution ), where the participation ratio tilde\tilde{\psi} is identical in both cases.

A two-mode case where the mm first eigenmodes are constant and equal to ci​m=cmaxc\_{i\leq m}=c\_{\max}, while the remaining ones are constant equal to a value significantly smaller ci>m=cmincmaxc\_{i>m}=c\_{\min}\mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}}c\_{\max}. For simplicity, we set cmin=0c\_{\min}=0 so that tilde=mn\tilde{\psi}=\frac{m}{n}.

An exponential eigenspectrum ci​exp⁡(−i/tilde​n)c\_{i}\approx\exp(-i/\tilde{\psi}n).

Solving the system for different values of (,)(\eta,\tau), we find the following regions:

![Refer to caption](regions.png)


Figure 1: - Region Diagram.

To better understand the boundary where the variance constraint disappears, we focus on the two-mode case that can easily be solved explicitly. We express the solution as:

|  |  |  |
| --- | --- | --- |
|  | |2i​m=+2​x1​2i>m=+2​x2​\displaystyle\left|\begin{array}[]{ccc}{}\_{i\leq m}^{2}&=&\eta+\sqrt{2\tau}x\_{1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ {}\_{i>m}^{2}&=&\eta+\sqrt{2\tau}x\_{2}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\right. |  |

We have the following:

|  |  |  |
| --- | --- | --- |
|  | |m​x12+(n−m)​x22=n​cmin​(+2​x1)​x12=cmax​(+2​x2)​x22​\displaystyle\left|\begin{array}[]{ccc}mx\_{1}^{2}+(n-m)x\_{2}^{2}&=&n\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ c\_{\min}(\eta+\sqrt{2\tau}x\_{1})x\_{1}^{2}&=&c\_{\max}(\eta+\sqrt{2\tau}x\_{2})x\_{2}^{2}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\right. |  |

The limit case with cmin=0c\_{\min}=0 and tilde=mn\tilde{\psi}=\frac{m}{n} is enlightening. We observe that:

|  |  |  |
| --- | --- | --- |
|  | casecmax>cmin=0|i​m=+2​nm​i>m=​\displaystyle\text{case}\ \ c\_{\max}>c\_{\min}=0\ \ \left|\begin{array}[]{ccc}{}\_{i\leq m}&=&\sqrt{\eta+\sqrt{2\tau\frac{n}{m}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ {}\_{i>m}&=&\sqrt{\eta}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\right. |  |

and the variance is:

|  |  |  |
| --- | --- | --- |
|  | casecmax>cmin=01n\slimits@=k2+2​mn\text{case}\ \ c\_{\max}>c\_{\min}=0\ \ \ \ \ \ \frac{1}{n}\sumop\slimits@{{}\_{k}^{2}}=\eta+\sqrt{2\tau\frac{m}{n}}\hskip 36.98866pt |  |

In this simple scenario (i.e. cmin=0c\_{\min}=0 and tilde=mn\tilde{\psi}=\frac{m}{n}), we note that:
  
 When is chosen as =1−2​mn=1−2​tilde\eta=1-\sqrt{2\tau\frac{m}{n}}=1-\sqrt{2\tau\tilde{\psi}}, the variance ends up around 2, as desired.
  
 As decreases towards 0, we converge towards full isotropy with i{}\_{i}\rightarrow\sqrt{\eta}.
  
 Conversely, as n2​m=12​tilde1\tau\rightarrow\frac{n}{2m}=\frac{1}{2\tilde{\psi}}\mathbin{\rotatebox[origin={c}]{-90.0}{$\Wedge$}}1 while =1−2​mn=1−2​tilde​0\eta=1-\sqrt{2\tau\frac{m}{n}}=1-\sqrt{2\tau\tilde{\psi}}\rightarrow 0, we end up with zero exposure on the lower mode and nm=tilde>1\sqrt{\frac{n}{m}}=\sqrt{\tilde{\psi}}>1 on the higher mode.

![Refer to caption](roots.png)


Figure 2: Roots of the two-mode model.

With the variance saturated through the choice of =1−2​tilde\eta=1-\sqrt{2\tau\tilde{\psi}}, the resulting Sharpe of the strategy is:

|  |  |  |
| --- | --- | --- |
|  | Sharpe(,𝒄)=1n\slimits@ckk=mncmaxmax=+2tildemncmax\displaystyle\text{Sharpe}(\boldsymbol{\theta},\boldsymbol{c})=\frac{1}{n}\sumop\slimits@{{}\_{k}c\_{k}}=\frac{m}{n}{}\_{\max}c\_{\max}=\sqrt{\eta+\sqrt{\frac{2\tau}{\tilde{\psi}}}}\frac{m}{n}c\_{\max} |  |

where mn​cmax\frac{m}{n}c\_{\max} is the value of the (in-sample) isotropic Sharpe.

![Refer to caption](sharpe.png)


Figure 3: Sharpes of the two-mode and exponential models.

We quickly see that as 12​tilde\tau\longrightarrow\frac{1}{2\tilde{\psi}}, the (in-sample) Sharpe converges towards its mean-variance value (as expected!):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sharpe​(12​tilde)\displaystyle\text{Sharpe}(\tau\longrightarrow\frac{1}{2\tilde{\psi}}) | =\displaystyle= | mn​cmax=1tilde​mn​cmax\displaystyle\sqrt{\frac{m}{n}}c\_{\max}=\sqrt{\frac{1}{\tilde{\psi}}}\frac{m}{n}c\_{\max} |  |

### 4.5 Take-Aways

•

By decomposing a general portfolio allocation 𝒘=𝑳​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} as 𝑳=n−12​𝑻−12\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{T}\boldsymbol{\Xi}^{-\frac{1}{2}}, fixing as =Tr​(𝑳​𝑳)\sigma=\text{Tr}\left(\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Xi}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right), one can easily measure (and potentially penalize) the portfolio isotropy thanks to Eq. [89](https://arxiv.org/html/2511.13334v1#S4.E89 "In 4.1 Isotropy Penalty and Participation Ratio ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). With variance fixed, the isotropy metric is a function of the participation ratio of the eigenspectrum of 𝑻\boldsymbol{T}.
•

By enforcing exactly isotropy, “pure” isotropic allocations (i.e. isotropic-mean portfolios) could deviate significantly from the original mean-variance allocation. In order to retain some amount of control, we augment the mean-variance framework by adding an isotropy constraint, thereby offering an adjustable trade-off between return maximization, variance minimization, and isotropic control.
•

The isotropy constraint acts as a geometric regulizer, in the orthonormal SVD basis of the normalized predictability matrix tilde\boldsymbol{\tilde{\Pi}}. As a function of its inverse participation ratio (when variance saturates on its constraint), it prevents loading up on too few concentrated modes.
•

The approach defines the solution as a modulation of the shape of the eigenspectrum tilde\boldsymbol{\tilde{\Psi}} of the normalized predictability matrix tilde\boldsymbol{\tilde{\Pi}}. The resulting solution offers a trade-off between pure isotropy (with flat allocation) and mean-variance (proportional to tilde\boldsymbol{\tilde{\Psi}}).
•

The parameters and controlling the amount of isotropy can be fine-tuned. The region 1−2​tilde​1​with​ 11-\sqrt{2\tau\tilde{\psi}}\leq\eta\leq 1\ \text{with}\ \tau\approx 1 defines an area of interest where both constraints co-exist: setting ==1\eta=\tau=1 is generally a sensible choice. The general solution solves nn-cubic equations coupled through both constraints.





Isotropic Mean-Variance FrameworkSolution𝒘e=𝑳​𝒔e=n−12​𝑻−12​𝒔e=n​\slimits@k=1N​𝒘tildekk​𝑻=𝑩tilden𝑼tildenwheretilde=−12−12=𝑩tildetilde𝑼tilde𝑻=arg𝑻⁡max⁡1n​Tr​(𝑻​tilde)−2​n​Tr​(𝑻​𝑻)−4​n​‖𝑻​𝑻−I​dn‖F2​Constraints​{variance:1n​Tr​(𝑻​𝑻)​2isotropy:1n​‖𝑻​𝑻−I​d‖F2​2​​ntildei=+i(−i2)i=(−)+ii3Canonical Portfolios:𝒘tildek=−12𝑩tildek​𝑼tildek−12​𝒔e​mean-variancefull-isotropicgeneral casecondition01 1​in\slimits@​tildei2​tildeiiPnL\slimits@​tildei2n​\slimits@​tildei1n​\slimits@​tildeii​Risk222n​\slimits@​i2Sharpe\slimits@​tildei21n​\slimits@​tildei\slimits@​tildeii\slimits@i2​\displaystyle\hskip-7.11317pt\begin{array}[]{c|c}\text{\bf Isotropic Mean-Variance Framework}&\text{\bf Solution}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\begin{array}[]{c}\boldsymbol{w}\_{e}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{T}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}=\frac{\sigma}{\sqrt{n}}\sumop\slimits@\_{k=1}^{N}{{}\_{k}\boldsymbol{\tilde{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{T}=\boldsymbol{\tilde{B}}\boldsymbol{\Theta}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \ \text{where}\ \ \boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{T}=\arg\_{\boldsymbol{T}}\max\frac{1}{\sqrt{n}}\text{Tr}\left(\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)-\frac{\gamma}{2n}\text{Tr}\left(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)-\frac{\lambda}{4n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\text{Constraints}\left\{\begin{array}[]{cc}\text{variance:}&\frac{1}{n}\text{Tr}\left(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)\leq{}^{2}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\text{isotropy:}&\frac{1}{n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}||^{2}\_{\mathbb{F}}\leq 2\tau\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\right.\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\sqrt{n}\tilde{\Psi}\_{i}=\gamma{}\_{i}+\lambda{}\_{i}({}\_{i}^{2}-\eta)=(\gamma-\eta\lambda){}\_{i}+\lambda{}\_{i}^{3}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\text{Canonical Portfolios:}\ \ \boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}&\begin{array}[]{| c | c | c | c |}\hline\cr&\text{mean-variance}&\text{full-isotropic}&\text{general case}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\hline\cr\text{condition}&\infty\rightarrow\tau\hfil&\tau\rightarrow 0&\tau\leq 1\ \eta\leq 1\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\hline\cr{}\_{i}&\sqrt{\frac{n}{\sumop\slimits@{\tilde{\Psi}\_{i}^{2}}}}\tilde{\Psi}\_{i}&\sqrt{\eta}&{}\_{i}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\hline\cr\text{PnL}&\sigma\sqrt{\sumop\slimits@{\tilde{\Psi}\_{i}^{2}}}&\sigma\sqrt{\frac{\eta}{n}}\sumop\slimits@{\tilde{\Psi}\_{i}}&\sigma\frac{1}{\sqrt{n}}\sumop\slimits@{{}\_{i}\tilde{\Psi}\_{i}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\hline\cr\text{Risk}&{}^{2}&{}^{2}\eta&\frac{{}^{2}}{n}\sumop\slimits@{{}\_{i}^{2}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\hline\cr\text{Sharpe}&\sqrt{\sumop\slimits@{\tilde{\Psi}\_{i}^{2}}}&\frac{1}{\sqrt{n}}\sumop\slimits@{\tilde{\Psi}\_{i}}&\frac{\sumop\slimits@{{}\_{i}\tilde{\Psi}\_{i}}}{\sumop\slimits@{{}\_{i}^{2}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\hline\cr\end{array}\end{array}

•

The approach emphasizes the importance of canonical portfolios as essential building blocks.
However, it also highlights the limitations of the approach:
  
  
 The described framework depends critically on the estimation and stability of both return and signal covariances and (through the whitening operators −12\boldsymbol{\Omega}^{-\frac{1}{2}} and −12\boldsymbol{\Xi}^{-\frac{1}{2}}). When the requirement is met, the approach would be able to manage some level of uncertainty present in the prediction matrix, e.g. or equivalently tilde\boldsymbol{\tilde{\Pi}}. But those are strong assumptions, certainly not met in practice, particularly for the signal covariance .
  
  
 The uncertainty is only tackled by modifying the shape of the eigencurve, nothing more. Analysis of the eigenspectrum of the normalized predictability matrix tilde\boldsymbol{\tilde{\Pi}} is therefore of critical importance.
•

Although we explicitly choose to work from the perspective of the Riccati basis 𝒃i\boldsymbol{b}\_{i} and 𝒖i\boldsymbol{u}\_{i}, focusing on the predictability matrix b​u\boldsymbol{\Pi}\_{bu}, any other isotropic basis could have been used (the approach is intrinsic). For example, one might prefer to work with Cholesky decomposition =𝑳​𝑳\boldsymbol{\Omega}=\boldsymbol{L}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} and =𝑳​𝑳\boldsymbol{\Xi}=\boldsymbol{L}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} (see Eq. [18](https://arxiv.org/html/2511.13334v1#S2.E18 "In 2.3.3 Isotropic Bases ‣ 2.3 Changing Perspective ‣ 2 Setting up the scene ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")), due to numerical stability.

## 5 Application: Sector Trend-Following

### 5.1 Setup

We consider a simple sector model where the returns 𝒓t\boldsymbol{r}\_{t} of a set of nn similar assets are driven by white noises t\boldsymbol{\epsilon}\_{t} and some stochastic autocorrelated trends t\boldsymbol{\mu}\_{t} slowly mean-reverting around zero as defined in [Grebenkov\_2014, Grebenkov\_2015]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {𝒓t=t+tt=qt−t+t\displaystyle\left\{\begin{array}[]{ccc}\boldsymbol{r}\_{t}&=&\beta\boldsymbol{\mu}\_{t}+\boldsymbol{\epsilon}\_{t}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \boldsymbol{\mu}\_{t}&=&q\boldsymbol{\mu}\_{t-\delta t}+\boldsymbol{\xi}\_{t}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\right. |  | (115) |

The stochastic variables t\boldsymbol{\epsilon}\_{t} and t\boldsymbol{\xi}\_{t} are supposed to be independent and identically distributed through time, with zero mean and correlation structures:

|  |  |  |
| --- | --- | --- |
|  | E[tu]=t−uandE[tu]=t−uE[\boldsymbol{\epsilon}\_{t}\boldsymbol{\epsilon}\_{u}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]={}\_{t-u}\ \boldsymbol{\Omega}\ \ \text{and}\ \ E[\boldsymbol{\xi}\_{t}\boldsymbol{\xi}\_{u}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}]={}\_{t-u}\ \boldsymbol{\Omega} |  |

In a sector model (e.g. pharma, banking, futures on Equity, futures on bonds), the trend innovations t\boldsymbol{\xi}\_{t} should be heavily influenced by common factors, whereas the noise components t\boldsymbol{\epsilon}\_{t} should reflect idiosyncratic shocks, likely to be less “syncronized”. We do expect the overall level of correlation to be higher for than for .

The parameter (identical for all assets for simplicity reason) scales the trend and is of the order of the signal-to-noise ratio, i.e. 1\beta\mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}}1. The parameter qq (also chosen constant across assets in our naive sector model) captures the speed at which the trend mean-reverts. It is a critical market parameter that shapes the dynamics of returns:

|  |  |  |
| --- | --- | --- |
|  | 𝒓t=t+\slimits@k​0​qt−k​tk\boldsymbol{r}\_{t}=\boldsymbol{\epsilon}\_{t}+\beta\sumop\slimits@\_{k\geq 0}{q^{k}\boldsymbol{\xi}\_{t-k\delta t}} |  |

Most often, the value of 1−q11-q\mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}}1 models a slow frequency, typically several months with 1−q​1%1-q\approx 1\% or less.

We consider a standard trend-following strategy where the trading signals are computed as exponential moving averages:

|  |  |  |
| --- | --- | --- |
|  | 𝒔t=1−p2​\slimits@k>0​pk−1​𝒓t−k​t\boldsymbol{s}\_{t}=\sqrt{1-p^{2}}\sumop\slimits@\_{k>0}{p^{k-1}\boldsymbol{r}\_{t-k\delta t}} |  |

The strategy parameter pp should be chosen to approximately match the mean-reversion speed qq. Unfortunately, the market parameter qq is not known exactly [Grebenkov\_2014] (and prone to sudden temporary changes). During a crisis, negative returns 𝒓t−1\boldsymbol{r}\_{t}\approx-\mathbb{1} (positively auto-correlated in time and positively correlated in space) would pile up (with higher volatility >1>1), while most model assumptions would break (e.g. increase volatility and fat tails, sudden decrease of the qq parameter, strong auto-correlation of the stochastic variables, …).

We denote =1−q20\beta={}\_{0}\sqrt{1-q^{2}}. Following [Grebenkov\_2014], we use an order of magnitude around 0.10{}\_{0}\approx 0.1, while p​q​0.99p\approx q\approx 0.99; we also use n=10n=10 in our numerical simulations.

We can compute the different matrices:

|  |  |  |
| --- | --- | --- |
|  | {=+02=q​1−p21−p​q​02=+1+p​q1−p​q​02\displaystyle\left\{\begin{array}[]{ccc}\boldsymbol{\Omega}&=&\boldsymbol{\Omega}+{}\_{0}^{2}\boldsymbol{\Omega}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \boldsymbol{\Pi}&=&\frac{q\sqrt{1-p^{2}}}{1-pq}{}\_{0}^{2}\boldsymbol{\Omega}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \boldsymbol{\Xi}&=&\boldsymbol{\Omega}+\frac{1+pq}{1-pq}{}\_{0}^{2}\boldsymbol{\Omega}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\right. |  |

Despite its simplicity, this model is a sensible reflection of reality (that is ignoring the non-Gaussian nature of financial distributions, the presence of fat tails, asymmetry, and so on). Combined with trend-following signals, we obtain a convincing allocation problem faced by portfolio managers (e.g. CTAs). Unfortunately, even in this simple model, the dynamics is complex and hard to solve. As noticed in [Grebenkov\_2015], unexpected properties appear.

The “alpha”, e.g the predictive information needed to trade successfully future returns, is embedded in the cross-correlation matrix , that is implicitly within the covariance matrix . Unfortunately, is much harder to accurately estimate than . Hidden in a see of noise, it is also typically less stable.

The single-asset case is straight-forward. The theoretical in-sample (annualized) Sharpe ratio of a trend-following strategy applied to a single asset is:

Single-Asset Trend-Following



𝒮1=252​q​1−p2Q2+2​Q+R​0.78\displaystyle\mathcal{S}\_{1}=\sqrt{252}\frac{q\sqrt{1-p^{2}}}{\sqrt{Q^{2}+2Q+R}}\approx 0.78

(117)
where Q=(1−pq)/1.9902Q=(1-pq)/{}\_{0}^{2}\approx 1.99 and R=1+q2−2​p2​q2​0.058R=1+q^{2}-2p^{2}q^{2}\approx 0.058 (using the same notations as in [Grebenkov\_2015]).
The value 0.78\approx 0.78 is obviously unrealistic and massively inflated. In practice, the expected Sharpe ratio of a single-asset trend-following system would be barely positive, around 0.1−0.20.1-0.2.

From the symmetry of , we know that the solution 𝑳\boldsymbol{L} is also symmetrical. We can develop the following equalities:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑳​𝑳\displaystyle\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} | =\displaystyle= | 𝑳​𝑳+2021−p​q​𝑳​𝑳+1+p​q1−p​q​𝑳04​𝑳\displaystyle\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}+\frac{2{}\_{0}^{2}}{1-pq}\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}+\frac{1+pq}{1-pq}{}\_{0}^{4}\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑳​𝑳\displaystyle\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L} | =\displaystyle= | q2​(1−p2)(1−p​q)2​𝑳04​𝑳\displaystyle\frac{q^{2}(1-p^{2})}{(1-pq)^{2}}{}\_{0}^{4}\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L} |  |

The second variance term Tr​(𝑳​𝑳)\text{Tr}(\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L}) is typically much smaller than the first one Tr​(𝑳​𝑳)\text{Tr}(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}). Its inclusion rarely changes significantly the solution, while complicating significantly the methodology (e.g. the complexity is obvious in [Grebenkov\_2015]).

We can derive the expected PnL and total variance, obtaining the same expressions as in [Grebenkov\_2015]:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | E​[𝒘​𝒓]\displaystyle E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}] | =\displaystyle= | Tr​(𝑳)=q​1−p2Q​Tr​(𝑳)​\displaystyle\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right)=\frac{q\sqrt{1-p^{2}}}{Q}\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Omega}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (118) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Var​[𝒘​𝒓]\displaystyle\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}] | =\displaystyle= | Tr(𝑳𝑳+2Q𝑳𝑳\displaystyle\text{Tr}\left(\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}+\frac{2}{Q}\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}\right.\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (119) |
|  |  |  | +RQ2𝑳𝑳)\displaystyle\hskip 28.45274pt\left.+\frac{R}{Q^{2}}\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |

The first-order condition writes:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 1\displaystyle\frac{1}{\gamma}\boldsymbol{\Pi} | =\displaystyle= | 𝑳+2Q​𝑳+RQ2​𝑳\displaystyle\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}+\frac{2}{Q}\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega}+\frac{R}{Q^{2}}\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Omega} |  | (120) |

where is the leverage coefficient (e.g. Lagrange multiplier of the variance constraint).

The last term is often negligible and the exact mean-variance solution barely differs from our departing closed-form solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑳=Tr​(tilde​tilde)−1−1\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{\text{Tr}(\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}})}}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1} |  | (121) |

We discuss those differences in a simplifying scenario below.

### 5.2 Simplifying Assumption: Uniformity

To simplify further, we model the two covariance matrices as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =(1−)Id+Jand=(1−)Id+J\displaystyle\boldsymbol{\Omega}=(1-)\mathbb{Id}+\mathbb{J}\ \ \text{and}\ \ \boldsymbol{\Omega}=(1-)\mathbb{Id}+\mathbb{J} |  | (122) |

with J=11\mathbb{J}=\mathbb{1}\mathbb{1}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}, the matrix full of ones. That is we are assuming that all return and signal correlations are equal to −1n−1\geq-\frac{1}{n-1} and −1n−1\geq-\frac{1}{n-1} respectively (note that the variances are also the same for the assets and signals).
This scenario is explored in details in [Grebenkov\_2015], which we refer for another perspective. Our results corroborate their findings.

In a typical sector, such as equity stocks (e.g. pharma or banking), equity futures, or bond futures, the correlation of the trend innovations is generally higher than the correlation of the idiosyncratic noise , as trends capture systematic, sector-wide movements, while noise reflects asset-specific fluctuations.

Although it is difficult to provide some accurate order of magnitudes, it is sensible to estimate around 0.6 to 0.9, reflecting strong sector-wide correlations in trends, versus around 0.1 to 0.4, reflecting lower residual correlations in idiosyncratic noise, with potential increases during crises.

#### 5.2.1 Attractive Properties

Thanks to the assumption of Eq. [122](https://arxiv.org/html/2511.13334v1#S5.E122 "In 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), all matrices end up of the form a​I​d+b​Ja\mathbb{Id}+b\mathbb{J} and commute (since J2=n​J\mathbb{J}^{2}=n\mathbb{J}). This has several implications. At a high level, we already know that the optimal solution 𝒘\boldsymbol{w} will be of the form 𝒘=(aw​I​d+bw​J)​𝒔\boldsymbol{w}=\left(a\_{w}\mathbb{Id}+b\_{w}\mathbb{J}\right)\boldsymbol{s}. As such, it can only have two expositions, the idiosyncratic signals aw​𝒔a\_{w}\boldsymbol{s} and the market mode through n​bw​𝒔bar​1nb\_{w}\boldsymbol{\bar{s}}\mathbb{1} where 𝒔bar=1n​1​𝒔\boldsymbol{\bar{s}}=\frac{1}{n}\mathbb{1}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}.

There are only two eigenspaces identical for all operators. Choosing an allocation (e.g. mean-variance or isotropic-mean) only amounts to modulating the weights allocated to both modes. Besides, one can easily solve the exact first-order condition of Eq. [120](https://arxiv.org/html/2511.13334v1#S5.E120 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") by working independently on each eigenmode (and where the Lagrange coefficient links the modes together through the variance constraint).

Practically, we have the following:

|  |  |  |
| --- | --- | --- |
|  | :a=1−+(1−)02b=+02:a=q​1−p21−p​q(1−)02b=q​1−p21−p​q​02:a=1−+1+p​q1−p​q(1−)02b=+1+p​q1−p​q​02\displaystyle\begin{array}[]{ccc}\boldsymbol{\Omega}:&a=1-+{}\_{0}^{2}(1-)&b=+{}\_{0}^{2}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \boldsymbol{\Pi}:&a=\frac{q\sqrt{1-p^{2}}}{1-pq}{}\_{0}^{2}(1-)&b=\frac{q\sqrt{1-p^{2}}}{1-pq}{}\_{0}^{2}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \boldsymbol{\Xi}:&a=1-+\frac{1+pq}{1-pq}{}\_{0}^{2}(1-)&b=+\frac{1+pq}{1-pq}{}\_{0}^{2}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array} |  |

For a matrix of the form a​I​d+b​Ja\mathbb{Id}+b\mathbb{J} (with a>0a>0 and a+n​b>0a+n\times b>0 to ensure positive definiteness), we have some basic properties :

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (a​I​d+b​J)−1\displaystyle\left(a\mathbb{Id}+b\mathbb{J}\right)^{-1} | =\displaystyle= | 1a​(I​d−ba+n​b​J)\displaystyle\frac{1}{a}\left(\mathbb{Id}-\frac{b}{a+nb}\mathbb{J}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (a​I​d+b​J)−12\displaystyle\left(a\mathbb{Id}+b\mathbb{J}\right)^{-\frac{1}{2}} | =\displaystyle= | 1a​(I​d+a−a+n​bn​a+n​b​J)\displaystyle\frac{1}{\sqrt{a}}\left(\mathbb{Id}+\frac{\sqrt{a}-\sqrt{a+nb}}{n\sqrt{a+nb}}\mathbb{J}\right) |  |

One can also compute the eigenvalues and singular values without any difficulty and the whole problem is solvable in closed-form.
The symmetric matrix a​I​d+b​Ja\mathbb{Id}+b\mathbb{J} is diagonalizable, with two eigenvalues: one eigenvalue =a​I​d+b​J1a+nb{}^{1}\_{a\mathbb{Id}+b\mathbb{J}}=a+nb with multiplicity 1 and eigenvector 1n​1\frac{1}{\sqrt{n}}\mathbb{1} and a second one =a​I​d+b​J2a{}^{2}\_{a\mathbb{Id}+b\mathbb{J}}=a with multiplicity n−1n-1 in the space orthogonal to 1\mathbb{1} (e.g. the basis can be computed using the Gram-Schmidt process). Depending on the coefficient bb, we could have 1 smaller than 2. We also have:

|  |  |  |
| --- | --- | --- |
|  | Tr(aId+bJ)=n(a+b)=+a​I​d+b​J1(n−1)a​I​d+b​J2\text{Tr}\left(a\mathbb{Id}+b\mathbb{J}\right)=n(a+b)={}\_{a\mathbb{Id}+b\mathbb{J}}^{1}+(n-1){}\_{a\mathbb{Id}+b\mathbb{J}}^{2} |  |

Since all matrices are of the form a​I​d+b​Ja\mathbb{Id}+b\mathbb{J}, they commute and have the same basis of eigenvectors. This greatly simplifies the computations and analysis, yet demonstrates incidentally the limitations of the approach. As long as the covariances and maintains the simplified structure of Eq. [122](https://arxiv.org/html/2511.13334v1#S5.E122 "In 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), no complex dynamics can emerge as the eigenspaces remaining stable.

#### 5.2.2 Portfolio Allocation Form

From the symmetry of the assets and signals, we know that any optimal solution will be of the form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑳\displaystyle\boldsymbol{L} | =\displaystyle= | 𝑳=aw​I​d+bw​J\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=a\_{w}\mathbb{Id}+b\_{w}\mathbb{J} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒘\displaystyle\boldsymbol{w} | =\displaystyle= | (aw​I​d+bw​J)​𝒔\displaystyle\left(a\_{w}\mathbb{Id}+b\_{w}\mathbb{J}\right)\boldsymbol{s} |  |
|  |  | =\displaystyle= | aw​𝒔+n​bw​𝒔bar​1\displaystyle a\_{w}\boldsymbol{s}+nb\_{w}\boldsymbol{\bar{s}}\mathbb{1} |  |
|  |  | =\displaystyle= | 𝒔w2+(−w1)w2𝒔bar1\displaystyle{}^{2}\_{w}\boldsymbol{s}+({}\_{w}^{1}-{}\_{w}^{2})\boldsymbol{\bar{s}}\mathbb{1} |  |

where 𝒔bar=1n​1​𝒔\boldsymbol{\bar{s}}=\frac{1}{n}\mathbb{1}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}. The ratio xw=n​bwawx\_{w}=\frac{nb\_{w}}{a\_{w}}
captures a position trade-off between being exposed to the average signal factor 𝒔bar\boldsymbol{\bar{s}} and idiosyncratic signals 𝒔\boldsymbol{s} (note that the eigenvalues 1w{}\_{w}^{1} and 2w{}\_{w}^{2} are for the operator 𝑳\boldsymbol{L}; they are not the ones of tilde\boldsymbol{\tilde{\Pi}}, nor the weights of canonical portfolios as encoded in n\frac{\sigma}{\sqrt{n}}\boldsymbol{\Theta}).

The coefficient bwb\_{w} is referred as the lead-lag term in [Grebenkov\_2015]. It provides an exposition to the average signal factor 𝒔bar\boldsymbol{\bar{s}} (the exposure is multiplied by nn). The ratio xwx\_{w} measures the deviation from a conventional trading where cross-asset allocations term are ignored:

|  |  |  |
| --- | --- | --- |
|  | lead-lag ratio:xw=n​bwaw=1w2w−1\text{lead-lag ratio:}\ \ \ x\_{w}=n\frac{b\_{w}}{a\_{w}}=\frac{{}\_{w}^{1}}{{}\_{w}^{2}}-1 |  |

In a “conventional trading” trend-following strategy, where the lead-lag term is ignored, setting bw=0b\_{w}=0 and 𝑳=aw​I​d\boldsymbol{L}=a\_{w}\mathbb{Id}, we can easily compute the theoretical in-sample (annualized) Sharpe ratio 𝒮nt​f\mathcal{S}^{tf}\_{n} as:

Conventional Trend-Following



𝑳t​f​I​d​𝒮nt​f(,)=252​n​q​1−p2Q2+2Q+R+(n−1)(Q2+22Q+R2)\displaystyle\begin{array}[]{c}\boldsymbol{L}^{tf}\propto\mathbb{Id}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\mathcal{S}^{tf}\_{n}(,)=\frac{\sqrt{252}\sqrt{n}\ q\sqrt{1-p^{2}}}{\sqrt{Q^{2}+2Q+R+(n-1)(Q^{2}{}^{2}+2Q+R^{2})}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}

(126)

We find as expected that 𝒮nt​f(=0,=0)=n𝒮1\mathcal{S}^{tf}\_{n}(=0,=0)=\sqrt{n}\mathcal{S}\_{1}: in the uncorrelated case, the Sharpe ratio scales in n\sqrt{n}. However, the benefit of diversification appears to diminish in the presence of correlations. To illustrate this point, we plot below the ratio 1n𝒮nt​f(,)\frac{1}{\sqrt{n}}\mathcal{S}^{tf}\_{n}(,) as a function of for different value of .

![Refer to caption](tfsharpe.png)


Figure 4: Annualized Sharpe ratio per asset computed as 1n𝒮nt​f(,)\frac{1}{\sqrt{n}}\mathcal{S}^{tf}\_{n}(,) as a function of .

Surprisingly, the inclusion of the lead-lag term through the proper optimization of the functional allows one to compensate the loss. This property is explained clearly in [Grebenkov\_2015].

To illustrate this point, let’s consider the case where ==. All the matrices of interest (e.g. , , ) are proportional to =\boldsymbol{\Omega}=\boldsymbol{\Omega}, and the mean-variance solution takes the form:

|  |  |  |
| --- | --- | --- |
|  | =𝑳−1\boldsymbol{\Omega}=\boldsymbol{\Omega}\ \ \Longrightarrow\ \ \boldsymbol{L}\propto\boldsymbol{\Omega}^{-1} |  |

From there, we can quickly compute the annualized Sharpe ratio and the lead-lag ratio:

Optimal Allocation when ====\rho



=𝑳o​p​t−1​xwo​p​t=−n1+(n−1)​𝒮no​p​t=252​n​q​1−p2Q2+2​Q+R=n​𝒮1​\displaystyle\begin{array}[]{c}\boldsymbol{\Omega}=\boldsymbol{\Omega}\ \ \Longrightarrow\ \ \boldsymbol{L}^{opt}\propto\boldsymbol{\Omega}^{-1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
x^{opt}\_{w}=-\frac{n\rho}{1+(n-1)\rho}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\mathcal{S}^{opt}\_{n}=\frac{\sqrt{252}\sqrt{n}\ q\sqrt{1-p^{2}}}{\sqrt{Q^{2}+2Q+R}}=\sqrt{n}\ \mathcal{S}\_{1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}

(130)

When ====\rho, the annualized Sharpe ratio does not depend on the correlation level and equals n​𝒮1\sqrt{n}\ \mathcal{S}\_{1}. The addition of a lead-lag term compensates exactly the drop observed in the conventional trend-following allocation.

#### 5.2.3 Eigen-Equations

The strategies we consider are as follows:

1. 1.

   Conventional Trend-Following
     
     
   In a standard trend-following strategy, the positions are usually directly proportional to the signals, while the lead-lag term is ignored:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝑳​I​d\boldsymbol{L}\propto\mathbb{Id} |  |
2. 2.

   Isotropic-Mean
     
     
   The framework is described in Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). Because all matrices commute, the istropic-mean allocation takes the following form:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝑳=n−12−12​\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}^{-\frac{1}{2}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |
3. 3.

   Closed-Form Mean-Variance
     
     
   Neglecting the second variance term leads to the simple closed-form solution of Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") that we have used throughout this work:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝑳=Tr​(tilde​tilde)−1−1\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{\text{Tr}(\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}})}}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1} |  |
4. 4.

   Exact Mean-Variance Allocation
     
     
   The exact mean-variance solution can be obtained by directly solving Eq. [120](https://arxiv.org/html/2511.13334v1#S5.E120 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").
5. 5.

   Isotropy-Regularized Mean-Variance Framework
     
     
   We also investigate the impact of adding an isotropy constraint using the framework described in Section [4](https://arxiv.org/html/2511.13334v1#S4 "4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (with parameters =1\tau=1 and =1\eta=1).

   |  |  |  |
   | --- | --- | --- |
   |  | 𝑳=n−12​𝑩tilde​𝑩tilde−12\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\boldsymbol{\Theta}\boldsymbol{\tilde{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} |  |

   where 𝑩tilde\boldsymbol{\tilde{B}} is the orthonormal matrix of eigenvectors (e.g. 𝑩tilde1=1n​1\boldsymbol{\tilde{B}}\_{1}=\frac{1}{\sqrt{n}}\mathbb{1}) and the coefficients 1 and 2 verify 2 cubic equations (see Eq. [96](https://arxiv.org/html/2511.13334v1#S4.E96 "In 4.2 Functional Formulation ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

We have the following equations for the eigenvalues of the corresponding operators:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (trend-following)wi=+11(1)2+(n−1)(2+2(2)2)​(iso-mean Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"))wi=nii​(mean-variance Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"))wi=\slimits@​tildek2​i1i​=nii​tildei1n​\slimits@​tildek2​( exact mean-var Eq. [120](https://arxiv.org/html/2511.13334v1#S5.E120 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"))wii(i)2+21−p​q+02ii1+q2−2​p2​q2(1−p​q)2()i204​(mean-var-iso)wi=nii​i\displaystyle\begin{array}[]{ccl}{}\_{w}^{i}(\text{trend-following})&=&\frac{\sigma}{\sqrt{{}^{1}{}^{1}+(^{1})^{2}+(n-1)(^{2}{}^{2}+(^{2})^{2})}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ {}\_{w}^{i}(\text{iso-mean Eq.~\ref{Eq:OptAgnostic3}})&=&\frac{\sigma}{\sqrt{n^{i}{}^{i}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ {}\_{w}^{i}(\text{mean-variance Eq.~\ref{Eq:TypicalMeanVarianceSolution}})&=&\frac{\sigma}{\sqrt{\sumop\slimits@{\tilde{\Psi}\_{k}^{2}}}}\frac{{}^{i}}{{}^{i}{}^{1}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ &=&\frac{\sigma}{\sqrt{n^{i}{}^{i}}}\frac{\tilde{\Psi}\_{i}}{\sqrt{\frac{1}{n}\sumop\slimits@{\tilde{\Psi}\_{k}^{2}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ {}\_{w}^{i}(\text{ exact mean-var Eq.~\ref{Eq:GeneralSimpleFirstOrderCondition}})&\propto\hfil&\frac{{}^{i}}{(^{i})^{2}+\frac{2}{1-pq}{}\_{0}^{2}{}^{i}{}^{i}+\frac{1+q^{2}-2p^{2}q^{2}}{(1-pq)^{2}}{}\_{0}^{4}({}^{i})^{2}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ {}\_{w}^{i}(\text{mean-var-iso})&=&\frac{\sigma}{\sqrt{n^{i}{}^{i}}}{}\_{i}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\hskip-28.45274pt |  | (137) |

where tildei=(i)i−12i\tilde{\Psi}\_{i}=(^{i}{}^{i})^{-\frac{1}{2}}{}^{i} and \slimits@​tildek2=tilde12+(n−1)​tilde22\sumop\slimits@{\tilde{\Psi}\_{k}^{2}}=\tilde{\Psi}\_{1}^{2}+(n-1)\tilde{\Psi}\_{2}^{2}.

#### 5.2.4 Validating the Closed-Form Solution Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")

Before analyzing those strategies, we first validate the closed-form solution of Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). We verify that the second variance term can be neglected. Figure [5.2.4](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS4 "5.2.4 Validating the Closed-Form Solution Eq. 121 ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")-left displays the ratio Tr​(𝑳​𝑳)/Tr​(𝑳​𝑳)\text{Tr}\left(\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L}\right)/\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right) when the allocation is determined as the closed-form mean-variance solution of Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). For most values of and , the ratio remains below 2%2\%. In the worst cases, corresponding to parameters where |−|0|-|\mathbin{\rotatebox[origin={c}]{-90.0}{$\Wedge$}}0, the ratio barely exceeds a couple of %\%. The resulting Sharpe inflation due to the approximation is negligible.

![Refer to caption](accuracy0.png)


Figure 5: Ratio Tr​(𝑳​𝑳)/Tr​(𝑳​𝑳)\text{Tr}\left(\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L}\right)/\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right) as a function of for different values of (n=10n=10) for the closed-form solution 𝑳−1−1\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\propto\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1} of Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

We also compare the exact solution Eq. [120](https://arxiv.org/html/2511.13334v1#S5.E120 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") with the closed-form approach Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") used throughout this work. We display in Figure [5.2.4](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS4 "5.2.4 Validating the Closed-Form Solution Eq. 121 ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") the ratio (mean-variance Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"))wi{}\_{w}^{i}(\text{mean-variance Eq.~\ref{Eq:TypicalMeanVarianceSolution}}) over ( solution Eq. [120](https://arxiv.org/html/2511.13334v1#S5.E120 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"))wi{}\_{w}^{i}(\text{ solution Eq.~\ref{Eq:GeneralSimpleFirstOrderCondition}}) for a range of parameters. We observe that both eigenmodes rarely diverge by more than 2%2\%. The impact on the theoretical in-sample Sharpe ratio is also minimal (not displayed here).

![Refer to caption](lambdaratios1.png)


Figure 6: Ratios of eigenmodes (Top = first eigenmode; Bottom = second eigenmode) for the exact model Eq. [120](https://arxiv.org/html/2511.13334v1#S5.E120 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and the closed-form approch Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

#### 5.2.5 Lead-Lag Correction

Without lead-lag term, the presence of positive correlations (in returns and/or signals) deteriorates significantly the expected in-sample Sharpe ratio. The expected diversification benefit expected from using a large numbers of assets and signals is muted as correlations increase.

However, as we saw above, the introduction of a lead-lag term can drastically change the situation and help recover (and even improve) the diversification effect, expected to be in the magnitude of n​𝒮1\sqrt{n}\ \mathcal{S}\_{1}. The lead-lag ratio xwx\_{w} is the amount of exposure into 𝒔bar\boldsymbol{\bar{s}} per unit of exposure in 𝒔\boldsymbol{s}:

|  |  |  |
| --- | --- | --- |
|  | 𝒘=aw​(𝒔+xw​𝒔bar​1)\boldsymbol{w}=a\_{w}\left(\boldsymbol{s}+x\_{w}\boldsymbol{\bar{s}}\mathbb{1}\right) |  |

For instance, in the case of equal correlations, i.e. ====\rho, the optimal lead-lag ratio is equal to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xo​p​t=−n1+(n−1)\displaystyle x^{opt}=-\frac{n\rho}{1+(n-1)\rho} |  | (138) |

with a resulting (in-sample) Sharpe ratio exactly equal to n​𝒮1\sqrt{n}\ \mathcal{S}\_{1}. The exposure per asset to 𝒔bar\boldsymbol{\bar{s}} is always negative, with xo​p​tx^{opt} converging towards −1-1 as nn increases (and >0\rho>0).

In the general case where , a proper accounting of the correlations through an optimized lead-lag term can improve even further the in-sample Sharpe ratio, reaching (theoreticaland non-realistic) values greater than n​𝒮1\sqrt{n}\ \mathcal{S}\_{1}. This a strong result, which was noticed and emphasized in [Grebenkov\_2015].

The Isotropic-Mean Case

In the case of the isotropic-mean allocation of Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), the lead-lag ratio takes the following form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xe​p\displaystyle x^{ep} | =\displaystyle= | ((1+n​ba)​(1+n​ba))−12−10​\displaystyle\left((1+n\frac{b}{a})(1+n\frac{b}{a})\right)^{-\frac{1}{2}}-1\leq 0\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |
|  |  | =\displaystyle= | 1−1+(n−1)​(1−1−+)02(1−1−+1+p​q1−p​q)02(1−(n−1)1−(n−1)+)02(1−(n−1)1−(n−1)+1+p​q1−p​q)02−1\displaystyle\frac{1-}{1+(n-1)}\sqrt{\frac{(\frac{1-}{1-}+{}\_{0}^{2})(\frac{1-}{1-}+\frac{1+pq}{1-pq}{}\_{0}^{2})}{(\frac{1-(n-1)}{1-(n-1)}+{}\_{0}^{2})(\frac{1-(n-1)}{1-(n-1)}+\frac{1+pq}{1-pq}{}\_{0}^{2})}}-1 |  |

The non-diagonal coefficient is always negative and quickly becomes significant (e.g. when |−|>15%|-|>15\% or as soon as >50%>50\%).

![Refer to caption](leadlag0.png)


Figure 7: Lead-lag ratio for the Eigenrisk Allocation (n=10n=10).

The position of each asset SiS^{i} is a linear combination of its own signal sis^{i} and a negative contribution of the average signal 𝒔bar\boldsymbol{\bar{s}}. This negative contribution serves as a hedge and tends to diminish the over-reliance on the individual signals.

As expected when ==, we end up with the same allocation as in Eq. [138](https://arxiv.org/html/2511.13334v1#S5.E138 "In 5.2.5 Lead-Lag Correction ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") with a corresponding Sharpe equal to n​𝒮1\sqrt{n}\ \mathcal{S}\_{1}. We observe that when , the annualized Sharpe ratio per asset is even higher (see Figure [5.2.5](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS5 "5.2.5 Lead-Lag Correction ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). Yet, in the most likely scenario where >>, the Sharpe per asset remains lower than 𝒮1\mathcal{S}\_{1}. The advocated hedging is costly in-sample, but could prevent some painful situation as we discuss below in Section [5.2.6](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS6 "5.2.6 Impact of Market Crash ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

![Refer to caption](sharpes0.png)


Figure 8: Annualized Sharpe per asset for the Isotropic-Mean Portfolio (n=10n=10).

The Case of Mean-Variance

The case of the mean-variance framework is even more interesting, as the sign of the lead-lag term depends on the choice of parameters (e.g. >0>0, >0>0, but also nn). The lead-lag ratio takes the following form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xo​p​t\displaystyle x^{opt} | =\displaystyle= | 1−1+(n−1)​(1−1−+)02(1−1−+1+p​q1−p​q)02(1−(n−1)1−(n−1)+)02(1−(n−1)1−(n−1)+1+p​q1−p​q)02−1\displaystyle\frac{1-}{1+(n-1)}\frac{(\frac{1-}{1-}+{}\_{0}^{2})(\frac{1-}{1-}+\frac{1+pq}{1-pq}{}\_{0}^{2})}{(\frac{1-(n-1)}{1-(n-1)}+{}\_{0}^{2})(\frac{1-(n-1)}{1-(n-1)}+\frac{1+pq}{1-pq}{}\_{0}^{2})}-1 |  |

The optimal lead-lag ratio can turn positive when when the noise correlation is much smaller than the innovation correlation , e.g. when 0\approx 0 and >0>0. In this scenario, the optimization of the mean-variance functional leads to some positions that reinforce the individual signal views 𝒔\boldsymbol{s} with a positive exposure to 𝒔bar\boldsymbol{\bar{s}}, thereby increasing the level of risk associated with the strategy. This could prove dangerous in the case of a sudden market crash (see below in Section [5.2.6](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS6 "5.2.6 Impact of Market Crash ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

![Refer to caption](leadlag1.png)


Figure 9: Lead-lag ratio for the Mean-Variance Solution (n=10n=10).

We display the Sharpe ratio of the mean-variance solution in Figure [5.2.5](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS5 "5.2.5 Lead-Lag Correction ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") for n=10n=10. Many parameter configurations shows an annualized Sharpe per asset higher than 𝒮1\mathcal{S}\_{1}. This is particularly the case when the noise correlation is much higher than the innovation correlation, i.e. >>.

However, the case that concerns us more in practice where << is less advantageous. Taking into account the proper correlations obviously leads to an improvement over the Sharpe 𝒮nt​f(,)\mathcal{S}^{tf}\_{n}(,) of a conventional strategy (see Eq. [126](https://arxiv.org/html/2511.13334v1#S5.E126 "In 5.2.2 Portfolio Allocation Form ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")), yet the gain appears more marginal.

In the realistic region where 0.75\approx 0.75 and 0.25−0.5\approx 0.25-0.5, both isotropic-mean and mean-variance annualized Sharpe ratio per asset hover around 0.50.5 with a negative lead-lag ratio lower than −0.5-0.5.

![Refer to caption](sharpes1.png)


Figure 10: Annualized Sharpe per asset for the Mean-Variance Solution (n=10n=10).

The region where 0​and\approx 0\ \text{and}\ \mathbin{\rotatebox[origin={c}]{-90.0}{$\Wedge$}} merits some comments. As tends towards 0, the Sharpe ratio per asset converges around 𝒮1\mathcal{S}\_{1}. There even appears to be an improvement of the Sharpe per asset over 𝒮1\mathcal{S}\_{1}, but it remains minimal. However, as displayed in Figure [5.2.5](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS5 "5.2.5 Lead-Lag Correction ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), this corresponds to lead-lag ratios significantly positive (increasing as increases), which boosts the Sharpe by reinforcing the individual signal 𝒔\boldsymbol{s} with a positive exposure to 𝒔bar\boldsymbol{\bar{s}}. This is a well-known fallacy of the mean-variance framework, which creates at times large, unreasonable, and risky positions just for the sake of maximization.

![Refer to caption](tfsharpe_n.png)


Figure 11: Evolution of the annualized Sharpe per asset as a function of nn for different parameters and .

Going further, the region where 00\leq\mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}} exhibits some non-intuitive properties, as they also depend on the number nn of assets. As noted in [Grebenkov\_2015], there is a non-monotonous behavior, with an inflexion point around 5050 assets. For a large number of assets (e.g. higher than 100100), the lead-lag ratio and the Sharpe ratio per asset would start to decrease. This is visible in Figure [5.2.5](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS5 "5.2.5 Lead-Lag Correction ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty").

Mean-Variance versus Eigenrisk: Differences

Both isotropic-mean and mean-variance allocations are defined by their exposures to two (orthogonal) eigenspaces.
For each mode, the exposure ratio is captured by tildei1n​\slimits@​tildek2\frac{\tilde{\Psi}\_{i}}{\sqrt{\frac{1}{n}\sumop\slimits@{\tilde{\Psi}\_{k}^{2}}}} (see Eq. [137](https://arxiv.org/html/2511.13334v1#S5.E137 "In 5.2.3 Eigen-Equations ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

This ratio is linked to the notion of effective rank and participation ratio as defined in Eq. [106](https://arxiv.org/html/2511.13334v1#S4.E106 "In 4.4 Parameter Selection & Regions ‣ 4 Isotropy-Regularized Mean-Variance: A Geometric Regularizer for Signal Uncertainty ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). A low effective rank/participation ratio would happen when the imbalance tilde1tilde2\tilde{\Psi}\_{1}\mathbin{\rotatebox[origin={c}]{-90.0}{$\Wedge$}}\tilde{\Psi}\_{2} is large, typically in the region with strongly correlated stochastic trends and low noise correlation (see Figure [5.2.7](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS7 "5.2.7 Isotropy-Regularized Mean-Variance as a Safeguard ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") further below). This is where the lead-lag difference is at its maximum. The mean-variance solution exploits meaningful differences to optimize the Sharpe ratio pushing the allocation into dangerous territory.

![Refer to caption](sharpe_diff.png)


Figure 12: Difference of Sharpe ratios between the mean-variance solution Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and the isotropic-mean approach Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (note that it cancels exactly when ==).

At the opposite, isotropic-mean allocation enforces a negative lead-lag term and acts as a hedge. The impact on the in-sample Sharpe ratio could be large depending on current parameters (see Figure [5.2.5](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS5 "5.2.5 Lead-Lag Correction ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")). This is particularly the case in the region when \mathbin{\rotatebox[origin={c}]{-90.0}{$\Wedge$}}, as up to 0.60.6 point of Sharpe could be lost between both approaches (see Figure [5.2.5](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS5 "5.2.5 Lead-Lag Correction ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

However, those are in-sample measures. In case of a sudden crash, this difference might not become so important anymore, as the benefit of a negative lead-lag ratio might really make the difference.

#### 5.2.6 Impact of Market Crash

During a market crash, things go haywire. Our set of assumptions and the whole model would not make much sense anymore. We assume that the returns would all suddenly drop 𝒓−1\boldsymbol{r}\approx-\mathbb{1}. As a consequence, the realized PnL would take the following form:

|  |  |  |
| --- | --- | --- |
|  | 𝒘𝒓=𝒔w2𝒓+(−w1)w2𝒔bar1𝒓−n𝒔barw1\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}={}^{2}\_{w}\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}+({}\_{w}^{1}-{}\_{w}^{2})\boldsymbol{\bar{s}}\mathbb{1}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\approx-n{}\_{w}^{1}\boldsymbol{\bar{s}} |  |

Depending on the sign of 𝒔bar\boldsymbol{\bar{s}} right before the crash, it is certainly possible to envision an unexpected PnL jump to the upside. This would be the case if there is a progressive crisis build-up, reflected in a progressive downtrend of the market leading to negative signals before the crash. However, sudden, unanticipated, and negative news would typically work against the general macro-environment, and would likely cause large losses rather than large gains.

The first eigenvalue 1w{}\_{w}^{1} (with multiplicity 11) is the one modulating the risk during the crash. We have:

|  |  |  |
| --- | --- | --- |
|  | (mean-variance)w1(iso-mean)w1{}\_{w}^{1}(\text{mean-variance})\geq{}\_{w}^{1}(\text{iso-mean}) |  |

if and only if tilde1​tilde2\tilde{\Psi}\_{1}\geq\tilde{\Psi}\_{2}, or equivalently:

|  |  |  |
| --- | --- | --- |
|  | 1+n​ba​(1+n​ba)​(1+n​ba)1+n\frac{b}{a}\geq\sqrt{(1+n\frac{b}{a})(1+n\frac{b}{a})} |  |

Now, at first-order in 20{}\_{0}^{2}, assuming a large number of assets nn and strictly positive correlations and , this condition is equivalent to:

|  |  |  |
| --- | --- | --- |
|  | >0\geq>0 |  |

which seems a reasonable assumption in the case in a standard sector model. The isotropic-mean allocation would have a smaller exposure to the principal market mode −1-\mathbb{1}.

![Refer to caption](ratiomv2eigen.png)


Figure 13: Log2-ratio (mean-variance)w1/(iso-mean)w1{}\_{w}^{1}(\text{mean-variance})/{}\_{w}^{1}(\text{iso-mean}) of first eigenmodes of mean-variance over isotropic-mean.

The crash ratio, defined as (mean-variance)w1/(iso-mean)w1−1{}\_{w}^{1}(\text{mean-variance})/{}\_{w}^{1}(\text{iso-mean})-1, takes the form:

|  |  |  |
| --- | --- | --- |
|  | tilde11n​\slimits@​tildek2=1+n​ba1n​(1+n​ba)2+n−1n​(1+n​ba)​(1+n​ba)​\frac{\tilde{\Psi}\_{1}}{\sqrt{\frac{1}{n}\sumop\slimits@{\tilde{\Psi}\_{k}^{2}}}}=\frac{1+n\frac{b}{a}}{\sqrt{\frac{1}{n}(1+n\frac{b}{a})^{2}+\frac{n-1}{n}(1+n\frac{b}{a})(1+n\frac{b}{a})}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  |

Using some sensible approximations (e.g. 0<<10<\leq<1, p​qp\approx q so that 1+p​q1−p​q021\frac{1+pq}{1-pq}{}\_{0}^{2}\mathbin{\rotatebox[origin={c}]{-90.0}{$\Wedge$}}1), an order of magnitude can be computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | tilde11n​\slimits@​tildek2​ba​ab​ab​1−​1−​\displaystyle\frac{\tilde{\Psi}\_{1}}{\sqrt{\frac{1}{n}\sumop\slimits@{\tilde{\Psi}\_{k}^{2}}}}\approx\frac{b}{a}\sqrt{\frac{a}{b}\frac{a}{b}}\approx\sqrt{\frac{}{1-}\frac{1-}{}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt} |  | (139) |

The crash ratio is easily around 150%150\% as soon as −>25%->25\%. Figure [5.2.6](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS6 "5.2.6 Impact of Market Crash ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") displays the ratio of the first eigenmode between the closed-form solution and the isotropic-mean allocation.

#### 5.2.7 Isotropy-Regularized Mean-Variance as a Safeguard

We now investigate how our isotropy-regularized mean-variance framework would naturally safeguard against perilous regions.
We simply set ==1\tau=\eta=1 and solve our isometric mean-variance functional.

To start, we plot the isotropy metric of the exact mean-variance closed-form solution. Figure [5.2.7](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS7 "5.2.7 Isotropy-Regularized Mean-Variance as a Safeguard ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") displays 1tilde−1\frac{1}{\tilde{\psi}}-1 (in y-log-coordinate) where tilde\tilde{\psi} is the participation ratio of the normalized predictability matrix tilde\boldsymbol{\tilde{\Pi}}. As we can observe, the departure from isotropy is maximal in the region of interest 00\approx\mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}}. The isotropy penalization would kick-in in that risky region and naturally avoid zones that are more isotropic to start with.

![Refer to caption](iso_metric.png)


Figure 14: Isotropy metric of the mean-variance solution.

By capping the isotropy metric at 22\tau, we prevent absurdly large lead-lag ratios through the over-optimization of the Sharpe ratio. Figure [5.2.7](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS7 "5.2.7 Isotropy-Regularized Mean-Variance as a Safeguard ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") displays the resulting lead-lag ratio. We also observe in Figure [5.2.7](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS7 "5.2.7 Isotropy-Regularized Mean-Variance as a Safeguard ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") some clear inflection points where the isotropy metric reaches its cap 22\tau. Interestingly, the resulting lead-lag ratios do not exceed 11, even in the worst cases.

![Refer to caption](iso_leadlag.png)


Figure 15: Lead-lag ratio of the Isotropy-Regularized Mean-Variance Solution (n=10,==1n=10,\eta=\tau=1). The mean-variance ratios are indicated by dotted lines.

We also investigate how the crash ratio, which we now define as (mean-variance)w1/(iso-reg-mean-var)w1−1{}\_{w}^{1}(\text{mean-variance})/{}\_{w}^{1}(\text{iso-reg-mean-var})-1, evolves as a function of and . In the riskiest region, the exposure to the first eigenmode is decreased by more than 30%30\% (see Figure [5.2.7](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS7 "5.2.7 Isotropy-Regularized Mean-Variance as a Safeguard ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")).

![Refer to caption](ratiomv2eigen3.png)


Figure 16: Log2-ratio (mean-variance)w1/(iso-reg-mean-var)w1{}\_{w}^{1}(\text{mean-variance})/{}\_{w}^{1}(\text{iso-reg-mean-var}) of first eigenmodes of mean-variance over our isotropy-regularized mean-variance approach.

The cost in Sharpe ratio is rather small, as displayed in Figure [5.2.7](https://arxiv.org/html/2511.13334v1#S5.SS2.SSS7 "5.2.7 Isotropy-Regularized Mean-Variance as a Safeguard ‣ 5.2 Simplifying Assumption: Uniformity ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). Even in the problematic region, the mean-variance Sharpe ratio is only marginally better, thereby confirming that the excessive magnitude of the lead-lag ratio is a dangerous by-product of the untamed mean-variance optimization. The isotropic penalty works by preventing corner solution, and avoid naturally unbalanced risky allocations.

![Refer to caption](iso_sharpe_diff.png)


Figure 17: Difference of Sharpe ratios between the mean-variance solution Eq. [121](https://arxiv.org/html/2511.13334v1#S5.E121 "In 5.1 Setup ‣ 5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") and the isotropic-mean approach Eq. [77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") (note that it cancels exactly when ==).

## 6 Final Words

It seems important to start with a disclaimer stating clearly that the described approach is overly simplistic and unrealistic.
Markets show fat tails, sudden regime breaks, and execution frictions (costs, slippage, impact), while signals and covariances are rarely joint Gaussians.
Those were all ignored for the sake of simplicity, tractability, and clarity.

Besides, we focused on a specific narrow problem, that is how to mitigate the over-reliance on untrustworthy signals within a mean-variance framework. It does so by introducing isotropy as a safeguard, but relies on a critical assumption that and are well-estimated, accurate, and stable through time, a property that is rarely met in practice.

On that point, we also did not discuss the estimation of parameters. Even if a model as straight-forward as the sector trend-following model presented in Section [5](https://arxiv.org/html/2511.13334v1#S5 "5 Application: Sector Trend-Following ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") had the good behavior of being valid, the estimation of the unknown parameters, especially the covariances, e.g. and , would be a challenging and critical task.

In light of those strong limitations, it should be clear that the conclusions should be taken with a large pinch of salt and that additional considerations are required in practice.

However, Basis Immunity (BI) introduces some original ideas and sheds light on a few noteworthy issues:

* •

  By careful analysis of the concept of isotropy, we designed a sound framework where the uncertainty of the signals is mitigated through the concept of isotropy. We properly defined isotropic bases and showed the importance of canonical portfolios as building blocks.
* •

  A general portfolio allocation that takes the form (without loss of generality) 𝒘=𝑳​𝒔=n−1​𝑴​𝒔\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-1}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s} with 𝑴​Rn​m\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\in\mathbb{R}^{n\times m} can be expressed as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝑳=n−12​Rbhat​(Rbhat−12​𝑴12​Ruhat)​Ruhat−12\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\left(\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}\right)\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} |  | (140) |

  where Rbhat\mathbb{R}\_{\hat{b}} and Ruhat\mathbb{R}\_{\hat{u}} are two rotations, corresponding to the isotropic bases {𝒃hat}\{\boldsymbol{\hat{b}}\} and {𝒖hat}\{\boldsymbol{\hat{u}}\} respectively. The linear operator:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑻=Rbhat−12​𝑴12​Ruhat​ℛn​m\boldsymbol{T}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}\mathbb{R}\_{\hat{u}}\in\mathcal{R}^{n\times m} |  |

  facilitates the computation of a few important expressions:

  |  |  |  |
  | --- | --- | --- |
  |  | returnE​[𝒘​𝒓]=n​Tr​(𝑻bhat​uhat)​varianceVar​[𝒘​𝒓]=2n​Tr​(𝑻​𝑻)​anisotropy1n||𝑻𝑻−I𝑻dn||F2,=𝑻Tr​(𝑻​𝑻)nor=𝑻cst\begin{array}[]{cc}\text{return}&E[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]=\frac{\sigma}{\sqrt{n}}\text{Tr}\left(\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\_{\hat{b}\hat{u}}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \text{variance}&\text{Var}[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}]=\frac{{}^{2}}{n}\text{Tr}(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}})\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\ \text{anisotropy}&\frac{1}{n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-{}\_{\boldsymbol{T}}\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}},\ {}\_{\boldsymbol{T}}=\frac{\text{Tr}(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}})}{n}\ \text{or}\ {}\_{\boldsymbol{T}}=\text{cst}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array} |  |

  where bhat​uhat=RbhattildeRuhat\boldsymbol{\Pi}\_{\hat{b}\hat{u}}=\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\mathbb{R}\_{\hat{u}} and tilde=b​u=−12−12\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Pi}\_{bu}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}} is the normalized predictability matrix.

  These measures are intrinsic and do not depend on a specific choice of isotropic basis (because the trace and Frobenius norm are invariant under simultaneous rotations of Rbhat\mathbb{R}\_{\hat{b}} and Ruhat\mathbb{R}\_{\hat{u}}).

  In Eq. [140](https://arxiv.org/html/2511.13334v1#S6.E140 "In 2nd item ‣ 6 Final Words ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), fixing the volatility at =2Tr(𝑳𝑳){}^{2}=\text{Tr}\left(\boldsymbol{\Omega}\boldsymbol{L}\boldsymbol{\Xi}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right) shows that the isotropy metric is inversely proportional to the participation ratio of −12𝑴12\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}} (computed from its eigenspectrum).

  In the mean-variance framework, a closed-form solution can be (approximately) expressed as (𝑴=−1\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝑳=Tr​(tilde​tilde)−12​Rbhat​(Rbhat​tilde​Ruhat)​Ruhat−12\displaystyle\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{\text{Tr}(\boldsymbol{\tilde{\Pi}}\boldsymbol{\tilde{\Pi}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}})}}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathbb{R}\_{\hat{b}}\left(\mathbb{R}\_{\hat{b}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\mathbb{R}\_{\hat{u}}\right)\mathbb{R}\_{\hat{u}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} |  | (141) |
* •

  Enforcing full isotropy (with variance at 2) while preserving some directional information encoded within the matrix 𝑴\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} can be achieved by identifying the two operators Rbhat\mathbb{R}\_{\hat{b}} and Ruhat\mathbb{R}\_{\hat{u}} so that 𝑻\boldsymbol{T}, which is of rank nn, becomes as close as possible (in the sense of the Frobenius norm) to the linear operator [I​dn,0n,m−n][\mathbb{Id}\_{n},\mathbb{0}\_{n,m-n}] and then replacing 𝑻\boldsymbol{T} by [I​dn,0n,m−n][\mathbb{Id}\_{n},\mathbb{0}\_{n,m-n}] in Eq. [140](https://arxiv.org/html/2511.13334v1#S6.E140 "In 2nd item ‣ 6 Final Words ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"), i.e. keeping only the first n right singular vectors.

  This is easily achieved through the singular value decomposition of the matrix:

  |  |  |  |
  | --- | --- | --- |
  |  | −12𝑴12=𝑩dotdot𝑼dot=𝑩dotdotn𝑼dotn\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{\frac{1}{2}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\boldsymbol{\dot{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}} |  |

  leading to:

  |  |  |  |
  | --- | --- | --- |
  |  | Rbhat=𝑩dot,Ruhat=𝑼dot,𝑳=n−12​𝑩dot​𝑼dotn−12\mathbb{R}\_{\hat{b}}=\boldsymbol{\dot{B}},\ \mathbb{R}\_{\hat{u}}=\boldsymbol{\dot{U}},\ \boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\dot{B}}\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}} |  |

  Some noteworthy comments:

  + The solution can be decomposed into a set of nn orthogonal portfolios −12𝑩doti𝑼doti−12𝒔\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\dot{B}}\_{i}\boldsymbol{\dot{U}}\_{i}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}, equally weighted.
  + There are m−nm-n signal basis vectors that span a linear space with no contribution - those are uninformative for the nn-returns. Those could form a basis for statistical arbitrage on signal residuals, analogous to idiosyncratic risk in factor models. This will be explored in future work.
  + When m=nm=n and 𝑴=I​dn\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\mathbb{Id}\_{n} the allocation is the same as the one proposed in [segonne-2024] and takes the form:

    |  |  |  |
    | --- | --- | --- |
    |  | 𝑳=n−12(−12−12)−12−12𝒔,\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Xi}\boldsymbol{\Omega}^{-\frac{1}{2}}\right)^{-\frac{1}{2}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{s}, |  |

    It is slightly different from the ERP approach of [benichou-16] (except when and commute).
  + Agnostic Risk Parity [benichou-16] (ARP) is a special case of ERP, where the signal covariance is chosen as +(1−)​I​d\boldsymbol{\Xi}\propto\varphi\boldsymbol{\Omega}+(1-\varphi)\mathbb{Id}. In this scenario BI=ARP.
  + Isotropic-Mean Allocation

    In the case of the mean-variance approach 𝑴=−1\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}, the orthogonal portfolios 𝒘tildek\boldsymbol{\tilde{w}}\_{k} are constructed from the singular vectors 𝑩tilde\boldsymbol{\tilde{B}} and 𝑼tilde\boldsymbol{\tilde{U}} of the normalized predictability matrix tilde=−12−12\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}, also known as canonical portfolios [CanonicalPortfolios2023]:

    |  |  |  |
    | --- | --- | --- |
    |  | 𝒘tildek=−12𝑩tildek​𝑼tildek−12​𝒔\boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s} |  |
* •

  Full isotropy could potentially deform significantly the theoretical closed-form solution of Eq. [141](https://arxiv.org/html/2511.13334v1#S6.E141 "In 2nd item ‣ 6 Final Words ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty"). In order to retain some amount of control, we augment the mean-variance framework with a tunable isotropy penalty, thereby offering an adjustable trade-off between return maximization, variance minimization, and isotropic control:

  |  |  |  |
  | --- | --- | --- |
  |  | arg𝑻⁡max⁡1n​Tr​(𝑻​tilde)−2​n​Tr​(𝑻​𝑻)−4​n​‖𝑻​𝑻−I​dn‖F2\arg\_{\boldsymbol{T}}\max\frac{1}{\sqrt{n}}\text{Tr}\left(\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)-\frac{\gamma}{2n}\text{Tr}\left(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)-\frac{\lambda}{4n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}\_{n}||^{2}\_{\mathbb{F}} |  |

  Canonical portfolios 𝒘tildek\boldsymbol{\tilde{w}}\_{k} emerge naturally as the core building blocks:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝒘=n​\slimits@k=1n​𝒘tildekk\boldsymbol{w}=\frac{\sigma}{\sqrt{n}}\sumop\slimits@\_{k=1}^{n}{{}\_{k}\boldsymbol{\tilde{w}}\_{k}} |  |

  where the parameters i solve nn coupled cubic equations:

  |  |  |  |
  | --- | --- | --- |
  |  | ntildei=(−)+ii3\sqrt{n}\tilde{\Psi}\_{i}=(\gamma-\eta\lambda){}\_{i}+\lambda{}\_{i}^{3} |  |

  where tildei\tilde{\Psi}\_{i} are the singular values of tilde\boldsymbol{\tilde{\Pi}}.

  This creates a smooth trade-off between isotropic-mean portfolios and mean-variance allocations. Pure isotropy flattens allocations (=i{}\_{i}=\sqrt{\eta}), while mean-variance scales them by eigenvalue strength (tildeii{}\_{i}\propto\tilde{\Psi}\_{i}).

  The parameters and controling the amount of isotropy can be fine-tuned (generally, setting ==1\tau=\eta=1 appears a sensible choice).
* •

  Although the general solution and the decomposition into canonical portfolios do not depend on the specific choice of isotropic bases, one could employ alternative ones, such as those designed for enhanced stability (e.g. Cholesky or others).
* •

  We showed an existing link with the principal portfolio approach [PrincipalPortfolios2020]. Principal portfolios are not purely intrinsic and depend on the choice of basis (modulo an invariance to rotations).

  Principal portfolios emerge naturally as canonical portfolios when the triple norm is expressed between isotropic bases, e.g. {𝒃hat}\{\boldsymbol{\hat{b}}\} and {𝒖hat}\{\boldsymbol{\hat{u}}\}. Therefore, similar techniques of principal beta portfolios and principal alpha portfolios could be applied (see [PrincipalPortfolios2020]), and will be explored in further work.
* •

  As an application, we reviewed the sector trend-following model introduced in [Grebenkov\_2015] (mixing stochastic trends with noise). We recovered the same expressions222222We note that the closed-form mean-variance solution of Eq. [141](https://arxiv.org/html/2511.13334v1#S6.E141 "In 2nd item ‣ 6 Final Words ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty") has the advantage of greatly simplifying some of the calculations.
   and reached similar conclusions. Some features of the models are counter-intuitive and could generate some risky allocations.

  Depending on parameters, such as the number of assets nn, but particularly the correlations (noise) and (trend), the optimal cross-asset position (referred to as lead-lag term) could either be negative (e.g. when \mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}}) or turn significantly positive (e.g. when \mathbin{\rotatebox[origin={c}]{90.0}{$\Wedge$}}). This is particularly the case in the realistic scenario where stochastic trends are significantly correlated.

  The isotropy constraint would certainly help in this case. Isotropic-mean allocation always possess a negative lead-lag term, acting as a hedging component with a negative exposure to the average signal 𝒔bar\boldsymbol{\bar{s}}. Depending on the market regime and unknown model parameters, such allocations would be less impacted by sudden regime changes as a market crash.

  Our isotropy-regularized mean-variance (IRMV) approach naturally tames the propensity of the mean-variance framework to amplify imbalances as captured by the participation ratio of the normalized predictability matrix, thereby preventing undiversified corner solutions.

While fragile to estimation error and regime shifts, out framework reframes signal uncertainty as a *measurable geometric defect* and mitigates it via *canonical, isotropic structure*. The isotropy-regularized mean-variance portfolios interpolates between full isotropic portfolios (i.e. isotropic-mean portfolios) and mean-variance allocations.

## 7 Summary

Extending Mean-Variance



=E​[𝒓​𝒓T]asset covariance=E​[𝒔​𝒔T]signal covariance=E​[𝒓​𝒔T]prediction/cross-covariance​{𝒆𝒊}natural basis{𝒃𝒊}Riccati basisbi=−12𝒆𝒊{𝒖𝒊}Riccati basisui=−12𝒆𝒊\displaystyle\begin{array}[]{cc}\boldsymbol{\Omega}=E[\boldsymbol{r}\boldsymbol{r}^{T}]&\text{asset covariance}\\
\boldsymbol{\Xi}=E[\boldsymbol{s}\boldsymbol{s}^{T}]&\text{signal covariance}\\
\boldsymbol{\Pi}=E[\boldsymbol{r}\boldsymbol{s}^{T}]&\text{prediction/cross-covariance}\end{array}\ \begin{array}[]{|ccc}\{\boldsymbol{e\_{i}}\}&\text{natural basis}&\\
\{\boldsymbol{b\_{i}}\}&\text{Riccati basis}&b\_{i}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{e\_{i}}\\
\{\boldsymbol{u\_{i}}\}&\text{Riccati basis}&u\_{i}=\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{e\_{i}}\\
\end{array}


regression-based𝒓=𝒔+=E​[𝒓​𝒔]​E​[𝒔​𝒔]−1=−1E​[𝒓|𝒔]=𝒔=−1𝒔​𝒘=arg𝒘⁡max⁡𝒘​E​[𝒓|𝒔]−2​𝒘​𝒘​𝒘=1−1​E​[𝒓|𝒔]=1−1−1​𝒔​​general mean-variance𝒘=𝑳​𝒔​E​[𝒘​𝒓]=Tr​(𝑳)​Var​[𝒘​𝒓]=Tr​(𝑳​𝑳)+Tr​(𝑳​𝑳)​𝑳=arg𝑳⁡max⁡E​[𝒔​𝑳​𝒓]−2​Var​[𝒔​𝑳​𝒓]​𝑳=1−1−1​\displaystyle\vskip-5.69046pt\begin{array}[]{c}\text{\bf regression-based}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{r}=\boldsymbol{\beta}\boldsymbol{s}+\boldsymbol{\epsilon}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\beta}=E\left[\boldsymbol{r}\boldsymbol{s}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\right]E\left[\boldsymbol{s}\boldsymbol{s}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\right]^{-1}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
E[\boldsymbol{r}|\boldsymbol{s}]=\boldsymbol{\beta}\boldsymbol{s}=\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{w}=\arg\_{\boldsymbol{w}}\max\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}E[\boldsymbol{r}|\boldsymbol{s}]-\frac{\gamma}{2}\boldsymbol{w}^{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}\boldsymbol{\Omega}\boldsymbol{w}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{w}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}E[\boldsymbol{r}|\boldsymbol{s}]=\frac{1}{\gamma}\boldsymbol{\Omega}^{-1}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-1}\boldsymbol{s}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\begin{array}[]{|c}\text{\bf general mean-variance}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{w}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
E\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]=\text{Tr}\left(\boldsymbol{L}\boldsymbol{\Pi}\right)\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\text{Var}\left[\boldsymbol{w}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{r}\right]=\text{Tr}\left(\boldsymbol{\Xi}\boldsymbol{L}\boldsymbol{\Omega}\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)+\cancel{\text{Tr}\left(\boldsymbol{\Pi}\boldsymbol{L}\boldsymbol{\Pi}\boldsymbol{L}\right)}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}=\arg\_{\boldsymbol{L}}\max E\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]-\frac{\gamma}{2}\text{Var}\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}=\frac{1}{\gamma}\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}



𝒘e=1−12​(−12−12){𝒃𝒊}​{𝒖𝒊}−12𝒔ein {𝒖𝒊}in {𝒃𝒊}\displaystyle{\boldsymbol{w}}\_{e}=\frac{1}{\gamma}\boldsymbol{\Omega}^{-\frac{1}{2}}\mathop{\vtop{\halign{#\cr$\hfil\displaystyle{\mathop{\vbox{\halign{#\cr\kern 1.29167pt\cr$\braceld\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracerd$\crcr\kern 2.15277pt\cr$\hfil\displaystyle{\left(\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}\right)}\hfil$\crcr}}}\limits^{\{\boldsymbol{b\_{i}}\}\longleftarrow\{\boldsymbol{u\_{i}}\}}\mathop{\vbox{\halign{#\cr\kern 1.29167pt\cr$\braceld\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracerd$\crcr\kern 2.15277pt\cr$\hfil\displaystyle{\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}}\hfil$\crcr}}}\limits^{\text{in $\{\boldsymbol{u\_{i}}\}$}}}\hfil$\crcr\kern 2.15277pt\cr$\bracelu\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\bracemd\thinspace\leaders{\hbox{$\braceex$}}{\hfill}\thinspace\braceru$\crcr\kern 1.29167pt\cr}}}\limits\_{\text{in $\{\boldsymbol{b\_{i}}\}$}}

Canonical Portfolios [m​n] [CanonicalPortfolios2023]Principal Portfolios [m=n] [PrincipalPortfolios2020]𝒘e=𝑳​𝒔e=1​\slimits@k=1n​tildek​𝒘tildek​𝑳=arg𝑳⁡max⁡E​[𝒔​𝑳​𝒓]−2​Var​[𝒔​𝑳​𝒓]​𝑳=1−1−1​tilde=−12−12=𝑩tildetilde𝑼tildecanonical portfolios𝒘tildek=−12𝑩tildek​𝑼tildek−12​𝒔e𝒘e=−12𝒘b=−12𝑳b​b​𝒔b=1​\slimits@k=1n​𝒘ddotk​𝑳b​b=arg𝑳⁡max\|​𝑳​\|​1⁡E​[𝒔b​𝑳​𝒓b]​𝑳b​b=1(b​bb​b)−12b​bwithb​b=−12−12𝑳=𝑼ddot​𝑩ddot=\slimits@k​𝑼ddotk​𝑩ddotk​𝒘ddotk=−12𝑩ddotk​𝑼ddotk​𝒔b=−12𝑩ddotk​𝑼ddotk−12​𝒔e​\displaystyle\begin{array}[]{c|c}\text{\bf Canonical Portfolios $[m\geq n]$ \cite[cite]{[\@@bibref{}{CanonicalPortfolios2023}{}{}]}}&\text{\bf Principal Portfolios $[m=n]$ \cite[cite]{[\@@bibref{}{PrincipalPortfolios2020}{}{}]}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\begin{array}[]{c}\boldsymbol{w}\_{e}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e}=\frac{1}{\gamma}\sumop\slimits@\_{k=1}^{n}{\tilde{\Psi}\_{k}\boldsymbol{\tilde{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}=\arg\_{\boldsymbol{L}}\max E\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]-\frac{\gamma}{2}\text{Var}\left[\boldsymbol{s}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\right]\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}=\frac{1}{\gamma}\boldsymbol{\Xi}^{-1}\boldsymbol{\Pi}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-1}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\text{canonical portfolios}\ \ \boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\hskip 28.45274pt\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}&\hskip 56.9055pt\begin{array}[]{c}\boldsymbol{w}\_{e}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{w}\_{b}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{L}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{b}=\frac{1}{\gamma}\sumop\slimits@\_{k=1}^{n}{\boldsymbol{\ddot{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}\_{bb}=\arg\_{\boldsymbol{L}}\max\_{\|\boldsymbol{L}\|\leq 1}{E\left[\boldsymbol{s}\_{b}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{L}\boldsymbol{r}\_{b}\right]}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}\_{bb}=\frac{1}{\gamma}\left(\boldsymbol{\Pi}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Pi}\_{bb}\right)^{-\frac{1}{2}}\boldsymbol{\Pi}\_{bb}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \text{with}\ \boldsymbol{\Pi}\_{bb}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Omega}^{-\frac{1}{2}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{L}=\boldsymbol{\ddot{U}}\boldsymbol{\ddot{B}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}=\sumop\slimits@\_{k}{\boldsymbol{\ddot{U}}\_{k}\boldsymbol{\ddot{B}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\ddot{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\ddot{B}}\_{k}\boldsymbol{\ddot{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{b}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\ddot{B}}\_{k}\boldsymbol{\ddot{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\\
\end{array}




Isotropic-Mean [m​n] ​E​q.[77](https://arxiv.org/html/2511.13334v1#S3.E77 "In 3.2.3 Isotropic-Mean Allocation ‣ 3.2 Unbalanced Case 𝑚⁢𝑛 and 𝐸⁢[𝒓|ℱ]⁢𝑴^\"\"⁢𝒔 ‣ 3 Basis Immunity: Pure Isotropic Allocations ‣ Basis Immunity: Isotropy as a Regularizer for Uncertainty")Isotropy-Regularized Mean-Variance [m​n] 𝒘e=n−12​𝑩tilde​𝑼tilden−12​𝒔e=n​\slimits@k=1N​𝒘tildek​tilde=−12−12=𝑩tildetilde𝑼tilde𝒘tildek=−12𝑩tildek​𝑼tildek−12​𝒔e​Case when​E​[𝒓|ℱ]​𝑴​𝒔​𝒘e=n−12​𝑩dot​𝑼dotn−12​𝒔e​with−12​𝑴+12=𝑩dot​dot​𝑼dot𝒘e=𝑳​𝒔e=n−12​𝑻−12​𝒔e=n​\slimits@k=1N​𝒘tildekk​𝑻=𝑩tilde𝑼tildewheretilde=−12−12=𝑩tildetilde𝑼tilde𝑻=arg𝑻⁡max⁡1n​Tr​(𝑻​tilde)−2​n​Tr​(𝑻​𝑻)−4​n​‖𝑻​𝑻−I​d‖F2​ntildei=+i(−i2)i=(−)+ii3𝒘tildek=−12𝑩tildek​𝑼tildek−12​𝒔e​\displaystyle\begin{array}[]{c|c}\text{\bf Isotropic-Mean $[m\geq n]$ }Eq.~\ref{Eq:OptAgnostic3}&\text{\bf Isotropy-Regularized Mean-Variance $[m\geq n]$ }\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\begin{array}[]{c}\boldsymbol{w}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\boldsymbol{\tilde{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}=\frac{\sigma}{\sqrt{n}}\sumop\slimits@\_{k=1}^{N}{\boldsymbol{\tilde{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\\
\text{Case when}\ E[\boldsymbol{r}|\mathcal{F}]\propto\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{w}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\dot{B}}\boldsymbol{\dot{U}}\_{\stackrel{{\scriptstyle\rightarrow}}{{n}}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\ \text{with}\ \boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{M}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{+\frac{1}{2}}=\boldsymbol{\dot{B}}\boldsymbol{\dot{\Psi}}\boldsymbol{\dot{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\par\end{array}&\begin{array}[]{c}\boldsymbol{w}\_{e}=\boldsymbol{L}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{s}\_{e}=\frac{\sigma}{\sqrt{n}}\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{T}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}=\frac{\sigma}{\sqrt{n}}\sumop\slimits@\_{k=1}^{N}{{}\_{k}\boldsymbol{\tilde{w}}\_{k}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{T}=\boldsymbol{\tilde{B}}\boldsymbol{\Theta}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\ \ \text{where}\ \ \boldsymbol{\tilde{\Pi}}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\Pi}\boldsymbol{\Xi}^{-\frac{1}{2}}=\boldsymbol{\tilde{B}}\boldsymbol{\tilde{\Psi}}\boldsymbol{\tilde{U}}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{T}=\arg\_{\boldsymbol{T}}\max\frac{1}{\sqrt{n}}\text{Tr}\left(\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\tilde{\Pi}}\right)-\frac{\gamma}{2n}\text{Tr}\left(\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\right)-\frac{\lambda}{4n}||\boldsymbol{T}\boldsymbol{T}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}-\eta\mathbb{Id}||^{2}\_{\mathbb{F}}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\sqrt{n}\tilde{\Psi}\_{i}=\gamma{}\_{i}+\lambda{}\_{i}({}\_{i}^{2}-\eta)=(\gamma-\eta\lambda){}\_{i}+\lambda{}\_{i}^{3}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\\
\boldsymbol{\tilde{w}}\_{k}=\boldsymbol{\Omega}^{-\frac{1}{2}}\boldsymbol{\tilde{B}}\_{k}\boldsymbol{\tilde{U}}\_{k}^{{\mathchoice{\raise 0.0pt\hbox{$\displaystyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\textstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptstyle\mkern 0.0mu\intercal$}}{\raise 0.0pt\hbox{$\scriptscriptstyle\mkern 0.0mu\intercal$}}}}\boldsymbol{\Xi}^{-\frac{1}{2}}\boldsymbol{s}\_{e}\rule{0.0pt}{12.48604pt}\rule[-3.87495pt]{0.0pt}{0.0pt}\end{array}\\
\end{array}