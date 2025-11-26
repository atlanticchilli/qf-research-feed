---
authors:
- Katia Colaneri
- Federico D'Amario
- Daniele Mancinelli
doc_id: arxiv:2511.19186v1
family_id: arxiv:2511.19186
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model
  with Partial Information
url_abs: http://arxiv.org/abs/2511.19186v1
url_html: https://arxiv.org/html/2511.19186v1
venue: arXiv q-fin
version: 1
year: 2025
---


Katia Colaneri
katia.colaneri@uniroma2.it
Department of Economics and Finance, University of Rome Tor Vergata.

Federico D’Amario
federico.damario@uniroma1.it
Department of Economics and Law, Sapienza University of Rome.

Daniele Mancinelli
Corresponding author: daniele.mancinelli@uniroma2.it
Department of Economics and Finance, University of Rome Tor Vergata.

(November 24, 2025)

###### Abstract

Given the increasing importance of environmental, social and governance (ESG) factors, particularly carbon emissions, we investigate optimal proportional portfolio insurance (PPI) strategies accounting for carbon footprint reduction. PPI strategies enable investors to mitigate downside risk while retaining the potential for upside gains. This paper aims to determine the multiplier of the PPI strategy to maximise the expected utility of the terminal cushion, where the terminal cushion is penalised proportionally to the realised volatility of stocks issued by firms operating in carbon-intensive sectors. We model the risky assets’ dynamics using geometric Brownian motions whose drift rates are modulated by an unobservable common stochastic factor to capture market-specific or economy-wide state variables that are typically not directly observable. Using the classical stochastic filtering theory, we formulate a suitable optimisation problem and solve it for the CRRA utility function. We characterise optimal carbon-penalised PPI strategies and optimal value functions under full and partial information and quantify the loss of utility due to incomplete information. Finally, we carry a numerical analysis showing that the proposed strategy reduces carbon-emissions intensity without compromising financial performance.

Keywords: Portfolio insurance strategies, Optimal control, Sustainable investment strategies, Partial information.
  
JEL classification: C61, G11, G22.
  
AMS classification: 49L12, 60J76, 91B16, 91G20.

## 1 Introduction

As recently documented in several studies, including Hartzmark and Sussman ([2019](https://arxiv.org/html/2511.19186v1#bib.bib15)), Lagerkvist et al. ([2020](https://arxiv.org/html/2511.19186v1#bib.bib17)), and Anquetin et al. ([2022](https://arxiv.org/html/2511.19186v1#bib.bib2)), stakeholders around the world have increasingly perceived climate change as a global threat. As a result, institutional investors increasingly integrate ESG criteria into portfolio design and assess the carbon footprint of their investments. For example, as reported by Peng et al. ([2024](https://arxiv.org/html/2511.19186v1#bib.bib22)), the Government Pension Investment Fund has allocated 163163 trillion yen in passive ESG index products, and the California Public Employees’ Retirement System follows a “social change investment” approach with ESG guidelines. Although ESG is multidimensional and encompasses several pillars, this article focuses on carbon risk and emissions reduction, which carry regulatory, market, and reputational implications. In particular, institutional investors seek to reduce the carbon footprint of their investments for two main reasons. First, they face environmental and regulatory risks associated with carbon-intensive investments, such as the risk of stranded assets and the risks of catastrophic events linked with climate change. Second, institutional investors are subject to a high degree of public scrutiny since their decisions significantly impact firms’ behaviour. Therefore, incorporating carbon-footprint considerations into institutional investors’ portfolio choices is crucial for long-term financial sustainability. Accordingly, measuring firms’ carbon emissions is an essential task. Two widely used metrics are the Brown-Green Score, developed by Görgen et al. ([2020](https://arxiv.org/html/2511.19186v1#bib.bib13)), and carbon intensity, by Hellmich and Kiesel ([2021](https://arxiv.org/html/2511.19186v1#bib.bib16)); in the present article, we adopt the latter approach.

Against this backdrop, Proportional Portfolio Insurance (PPI) strategies offer an appealing framework for integrating downside protection with sustainability considerations. PPI strategies emerged in the aftermath of the 19731973-19741974 market collapse, which led to the withdrawal of several pension funds. They were first developed by Rubinstein and Leland ([1976](https://arxiv.org/html/2511.19186v1#bib.bib25)) and Brennan and Schwartz ([1976](https://arxiv.org/html/2511.19186v1#bib.bib8)) as a response to this crisis. After a period of relative obscurity, PPI strategies experienced a remarkable resurgence during the 20082008 financial crisis. Today, they constitute a cornerstone of modern asset management and are widely implemented by institutional investors – such as mutual funds, insurance companies, and pension funds (see, e.g., Temocin et al. ([2018](https://arxiv.org/html/2511.19186v1#bib.bib27)) and Di Giacinto et al. ([2024](https://arxiv.org/html/2511.19186v1#bib.bib11))). A key purpose of PPI strategies is to ensure a predetermined level of wealth over a fixed investment horizon while still allowing participation in equity market upturns (see, e.g., Grossman and Villa ([1989](https://arxiv.org/html/2511.19186v1#bib.bib14)) and Basak ([2002](https://arxiv.org/html/2511.19186v1#bib.bib4))). The strategy achieves this through dynamic allocation between a risky reference portfolio and a reserve asset. This allocation is governed by the concept of the cushion, defined as the difference between the current portfolio value and the floor, i.e., the minimum level of wealth to be protected at all times. The investor’s exposure to the risky portfolio is proportional to the cushion (when positive), and the proportionality factor – known as the multiplier – varies over time. Because the strategy is self-financing, any remaining wealth is automatically invested in the reserve asset.

To meet the dual objectives of institutional investors, i.e. achieving downside protection and reducing the carbon footprint of their portfolios, we propose a modified version of the PPI strategy characterised by a carbon-penalised cushion. More precisely, we add a penalty term to the terminal cushion, which is proportional to the realised variance of the stocks issued by firms operating in carbon-intensive businesses. Such a proportionality factor represents the fund manager’s attitude toward the portfolio’s carbon intensity, that is, its carbon aversion. A similar approach has recently been adopted in Colaneri et al. ([2025](https://arxiv.org/html/2511.19186v1#bib.bib9)) to construct optimal investment portfolios in a more general carbon-penalisation framework. In contrast to the existing literature (see, e.g., Andersson et al. ([2016](https://arxiv.org/html/2511.19186v1#bib.bib1)), Bolton et al. ([2022](https://arxiv.org/html/2511.19186v1#bib.bib5)), Le Guenedal and Roncalli ([2023](https://arxiv.org/html/2511.19186v1#bib.bib18))), we do not pre-select stocks characterised by low carbon emission levels to be included in the risky reference portfolio, nor do we impose constraints on the overall carbon intensity of the strategy. Instead, this new methodology allows a flexible trade-off between the risk–return profile and the carbon intensity of each asset in the portfolio. Indeed, if the risk–return trade-off of a given carbon-intensive asset is sufficiently favourable, it can offset the negative impact of its high carbon footprint. This property is particularly desirable from the perspective of a portfolio insurer whose primary concern is to achieve the guaranteed amount at the end of the investment horizon. Building upon these considerations, our study bridges the gap between portfolio insurance techniques and environmental sustainability objectives.

We contribute to the existing literature by including environmental sustainability criteria in determining the optimal design of the PPI strategy within an empirically grounded market framework. In doing so, we extend the traditional PPI approach – primarily focused on downside protection – by embedding it in a dynamic setting where both financial and environmental risks are jointly accounted for. In particular, we model risky assets as geometric Brownian motions whose drifts are modulated by a single unobservable common factor to capture market-specific and economy-wide states that are not directly observable and evolve over time. Such a latent factor can be interpreted as a composite macro-financial state that jointly drives the expected returns of assets. It aggregates several cyclical forces, such as the business cycle, monetary and financial conditions, credit and funding conditions, systemic liquidity, inflation pressures, and transition-to-net-zero pressure. Although each component admits observable proxies, none of them is directly observed in a noise-free way. Consequently, we assume that this state variable is unobservable and model its dynamics with an Ornstein–Uhlenbeck process, which reflects the mean-reverting nature of the aforementioned components.
  
Within this framework, we characterize the optimal profile of the proposed carbon-penalised PPI strategy, namely, the optimal multiplier and the composition of the risky reference portfolio, to maximise the expected CRRA utility of the carbon-penalised terminal cushion. As a by-product, we obtain a characterisation of the optimal strategy in the special case where the portfolio manager is endowed with a logarithmic utility function. Using dynamic programming techniques, we compute the optimal policy under both full and partial information settings. To address the partial information case, we derive the filter providing the conditional distribution of the unobservable factor given the available information set. In particular, in our setup the conditional distribution is described by the finite-dimensional linear Kalman filter. The optimisation problem is solved by dynamic programming principle using a guess-and-verify approach. We also quantify the information premium arising from observing the latent factor, by deriving closed-form expressions for the loss of utility and for the relative efficiency of the partial-information strategy with respect to its full-information benchmark.
We conclude the paper with a numerical study based on simulations, which allows to compare the behaviour of different investors. In particular, we focus on two key aspects: (i) the comparison between the portfolio composition of carbon-penalised PPI strategies and standard PPI strategies, and (ii) the strategies followed by a fully informed versus a partially informed portfolio insurer.

The remainder of the paper is organised as follows. Section [2](https://arxiv.org/html/2511.19186v1#S2 "2 The market setup ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") introduces the model setting. In Section [3](https://arxiv.org/html/2511.19186v1#S3 "3 The carbon-penalised proportional portfolio insurance strategy ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), we introduce the carbon-penalised PPI strategy. In Section [4](https://arxiv.org/html/2511.19186v1#S4 "4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), we solve the optimisation problem in a full information setting. In Section [5](https://arxiv.org/html/2511.19186v1#S5 "5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") we solve the maximisation problem under partial information. We perform a numerical analysis in Section [6](https://arxiv.org/html/2511.19186v1#S6 "6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), and Section [7](https://arxiv.org/html/2511.19186v1#S7 "7 Concluding remarks ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") poses the conclusions. In order to improve the flow of the paper, we provide proof of all results in the Appendix.

#### Literature review.

This article refers to different strands of the literature that address the problem of integrating sustainability – measured either in terms of carbon emissions or ESG factors – as an additional objective in portfolio optimisation, alongside return maximisation and risk minimisation. From a methodological perspective, these optimisation problems can be addressed using three main approaches.
  
The first approach is to preemptively exclude stocks and portfolios that do not reflect pre-specified sustainability criteria from the selection process. One pioneering work within this first approach is that of Andersson et al. ([2016](https://arxiv.org/html/2511.19186v1#bib.bib1)). The authors propose preliminarily excluding stocks characterised by high carbon intensity and selecting the remainder to minimise the tracking error relative to a benchmark portfolio. The authors show that such a method can reduce the portfolio’s carbon footprint by 5050% while achieving negligible tracking error. In addition, they show that the optimal portfolio can outperform the benchmark portfolio since the market gradually incorporates the carbon risk into equity prices. Bolton et al. ([2022](https://arxiv.org/html/2511.19186v1#bib.bib5)) extend this approach by including the additional constraint that the optimal portfolio must meet the targets enshrined in the Paris Agreement. The proposed methodology maintains negligible tracking error relative to major market indices, gradually decarbonising the portfolio over time.
  
The second approach consists in keeping the investment universe unchanged and allowing all stocks to be selected as long as the overall portfolio meets certain sustainability requirements. In this context, Le Guenedal and Roncalli ([2023](https://arxiv.org/html/2511.19186v1#bib.bib18)) study an optimisation problem in which the deviation from a benchmark portfolio is minimised under the constraint that the portfolio does not exceed a certain level of carbon risk. Similarly, De Spiegeleer et al. ([2023](https://arxiv.org/html/2511.19186v1#bib.bib10)) keep the initial universe of investment opportunities unchanged and select stocks such that the portfolio meets sustainability constraints measured not only in terms of carbon intensity but also in terms of ESG ratings. Their study shows that portfolios with low ESG scores initially show higher performance, while those with high ESG scores show better performance only in the long run. Moreover, they find that more stringent carbon intensity constraints do not significantly impact portfolio performance. Bolton et al. ([2024](https://arxiv.org/html/2511.19186v1#bib.bib6)) develops a framework for constructing equity portfolios aligned with the net-zero emissions target that balances broad diversification with a steady reduction in carbon footprint. Starting from a standard market index, the authors impose a time-varying carbon budget consistent with climate targets and solve a constrained tracking-error minimisation problem subject to decarbonisation constraint. The resulting “carbon budget” indices deliver substantial reductions in portfolio emissions while preserving diversification and low tracking error.
  
The third approach, which includes our contribution, incorporates sustainability directly into investor preferences and thereby increases the attractiveness of sustainable portfolios in terms of higher expected utility. More realistically, these models do not guarantee that a specific sustainability target will be achieved. Indeed, if the expected return (respectively, volatility) of a given carbon-intensive stock remains sufficiently high (respectively, low), it can offset the negative impact of carbon risk. Here, Pástor et al. ([2021](https://arxiv.org/html/2511.19186v1#bib.bib21)) develop an equilibrium model in which investors integrate sustainability into the risk–return trade-off, reducing the cost of capital of sustainable firms and, consequently, the level of their investments. In contrast, firms with a high carbon footprint are characterised by a high cost of capital, which reduces the level of investment. Escobar-Anel ([2022](https://arxiv.org/html/2511.19186v1#bib.bib12)) proposes a multivariate CRRA utility that allows investors to assign different risk-aversion levels to green and brown assets. Numerical results show that higher risk aversion toward brown assets can substantially increase optimal green allocations, while treating all assets with the same risk aversion can lead to large welfare losses.

## 2 The market setup

Let (Ω,𝔾,ℙ)\left(\Omega,\mathbb{G},\mathbb{P}\right) be a fixed probability space and TT a finite time horizon coinciding with the terminal time of an investment. We also introduce a ℙ\mathbb{P}-complete and right-continuous filtration 𝔾={𝒢t}t∈[0,T]\mathbb{G}=\left\{\mathcal{G}\_{t}\right\}\_{t\in[0,T]} representing the global information flow, and we assume that all processes below are 𝔾\mathbb{G}-adapted. We consider a financial market model consisting of nn stocks with nn-dimensional price processes 𝐒={𝐒t}t∈[0,T]\mathbf{S}=\left\{\mathbf{S}\_{t}\right\}\_{t\in[0,T]}
where 𝐒t=(St1,…,Stn)⊤\mathbf{S}\_{t}=(S^{1}\_{t},\,\dots,\,S^{n}\_{t})^{\top} for all t∈[0,T]t\in[0,T], and one risk-free asset BB, that are traded continuously on [0,T][0,T]. The dynamics of the risk-free are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Bt=r​Bt​d​t,B0=1,\mathrm{d}B\_{t}=rB\_{t}\mathrm{d}t,\quad B\_{0}=1, |  | (2.1) |

where r>0r>0 denotes the constant risk-free interest rate. The price dynamics of the risky assets 𝐒\mathbf{S} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐒t=diag​(𝐒t)​(𝝁t​d​t+𝚺𝐒​d​𝐖t𝐒),\mathrm{d}\mathbf{S}\_{t}=\text{diag}\left(\mathbf{S}\_{t}\right)\left(\bm{\mu}\_{t}\mathrm{d}t+\mathbf{\Sigma}\_{\mathbf{S}}\mathrm{d}\mathbf{W}^{\mathbf{S}}\_{t}\right), |  | (2.2) |

where 𝐒0=(S01,…,S0n)⊤\mathbf{S}\_{0}=(S^{1}\_{0},\,\dots,\,S^{n}\_{0})^{\top} and S0i∈ℝ+S^{i}\_{0}\in\mathbb{R}\_{+} for all i=1,…,ni=1,\dots,n. In equation ([2.2](https://arxiv.org/html/2511.19186v1#S2.E2 "In 2 The market setup ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), 𝚺𝐒=diag​(σ1,…,σn)\mathbf{\Sigma}\_{\mathbf{S}}=\text{diag}\left(\sigma\_{1},\dots,\sigma\_{n}\right), with σi>0\sigma\_{i}>0 for every i=1,…,ni=1,\dots,n, and 𝐖𝐒={𝐖𝐒}t∈[0,T]\mathbf{W}^{\mathbf{S}}=\{\mathbf{W}^{\mathbf{S}}\}\_{t\in[0,T]} is a standard 𝔾\mathbb{G}-Brownian motion in ℝn\mathbb{R}^{n} with correlated components, namely d​⟨Wi𝐒,Wj𝐒⟩t=ρi,j​d​t,\mathrm{d}\langle W^{\mathbf{S}}\_{i},\,W^{\mathbf{S}}\_{j}\rangle\_{t}=\rho\_{i,j}\mathrm{d}t, for constant correlation coefficients ρi,j∈[−1,1]\rho\_{i,j}\in[-1,1], such that ρi,j=ρj,i\rho\_{i,j}=\rho\_{j,i}, for every i,j=1,…,ni,\,j=1,\dots,n, and ρi,i=1\rho\_{i,i}=1, for every i=1,…,ni=1,\dots,n.
Moreover, 𝝁t\bm{\mu}\_{t} is stochastic and unobservable. This assumption is motivated by the fact that drifts of financial assets are rarely constant and subject to random fluctuations. In particular, we assume that the drift process 𝝁={𝝁t}t∈[0,T]\bm{\mu}=\left\{\bm{\mu}\_{t}\right\}\_{t\in[0,T]} is of the form 𝝁t=𝝁​(Yt)=𝒂​Yt+𝐛\bm{\mu}\_{t}=\bm{\mu}(Y\_{t})=\bm{a}Y\_{t}+\mathbf{b} for every t∈[0,T]t\in[0,T], with 𝒂∈ℝn\bm{a}\in\mathbb{R}^{n} and 𝐛∈ℝn\mathbf{b}\in\mathbb{R}^{n}, where Y={Yt}t∈[0,T]Y=\{Y\_{t}\}\_{t\in[0,T]} is the common unobservable factor process. Indeed, YtY\_{t} can represents macro-financial states that are hard to observe cleanly over time. Typical examples include the business cycle, monetary and financial conditions, credit and funding conditions, systemic liquidity, inflation pressures, and transition-to-net-zero emissions pressure. While these variables have observable proxies, none of them is directly observed in a noise-free way. Consequently, a partial information framework is necessary to model these state processes. In this paper, we model the common latent factor YY as an Ornstein-Uhlenbeck (OU) process, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=(λ​Yt+β)​d​t+σY​d​WtY,Y0∼N​(Γ0,P0),\mathrm{d}Y\_{t}=\left(\lambda Y\_{t}+\beta\right)\mathrm{d}t+\sigma\_{Y}\mathrm{d}W\_{t}^{Y},\quad Y\_{0}\sim N\left(\Gamma\_{0},P\_{0}\right), |  | (2.3) |

with λ,β∈ℝ,σY>0\lambda,\,\beta\in\mathbb{R},\,\sigma\_{Y}>0. Here, WY={WtY}t∈[0,T]W^{Y}=\left\{W\_{t}^{Y}\right\}\_{t\in[0,T]} is a standard one-dimensional 𝔾\mathbb{G}-Brownian motion correlated with 𝐖𝐒\mathbf{W}^{\mathbf{S}} with d​⟨WY,Wi𝐒⟩t=ρi,Y​d​t\mathrm{d}\langle W^{Y},\,W\_{i}^{\mathbf{S}}\rangle\_{t}=\rho\_{i,Y}\mathrm{d}t, where ρi,Y∈[−1,1]\rho\_{i,Y}\in[-1,1] for every i=1,…,ni=1,\dots,n. The OU choice captures the cyclical, mean-reverting nature of the above macro-financial variables while preserving the linear–Gaussian structure that makes filtering under partial information analytically tractable (see Section [5](https://arxiv.org/html/2511.19186v1#S5 "5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). Stocks are assumed to be issued by firms with different levels of carbon emissions, measured by carbon intensity. A firm’s carbon intensity is defined as the ratio between the total greenhouse gas emissions in metric tonnes of CO2 and total revenues (in USD millions). Based on carbon intensity, we cluster the stocks into two groups; in particular, we assume that the first kk assets are characterised by low carbon intensity (green stocks) and the remaining n−kn-k assets by high carbon intensity (brown stocks). From a practical perspective, a common approach (see, e.g., Ardia et al. ([2023](https://arxiv.org/html/2511.19186v1#bib.bib3))) is to rank firms’ carbon intensity cross-sectionally and identify the two groups using percentiles. For instance, firms with carbon intensity above (respectively, below) the pp-th (respectively, (1−p)(1-p)-th) percentile are labeled as brown (respectivel, green).

#### A convenient representation for the latent factor–stock model.

We denote by 𝐑\mathbf{R} the positive definite correlation matrix of (𝐖𝐒,WY)⊤\left(\mathbf{W}^{\mathbf{S}},\,W^{Y}\right)^{\top},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐑=(1ρ1,2…ρ1,nρ1,Yρ1,21…ρ2,nρ2,Y⋮⋮⋱⋮⋮ρ1,nρ2,n…1ρn,Yρ1,Yρ2,Y…ρn,Y1).\mathbf{R}=\begin{pmatrix}1&\rho\_{1,2}&\dots&\rho\_{1,n}&\rho\_{1,Y}\\ \rho\_{1,2}&1&\dots&\rho\_{2,n}&\rho\_{2,Y}\\ \vdots&\vdots&\ddots&\vdots&\vdots\\ \rho\_{1,n}&\rho\_{2,n}&\dots&1&\rho\_{n,Y}\\ \rho\_{1,Y}&\rho\_{2,Y}&\dots&\rho\_{n,Y}&1\end{pmatrix}. |  | (2.4) |

We express 𝐖𝐒\mathbf{W}^{\mathbf{S}} and WYW^{Y} as a linear combination of uncorrelated standard 𝔾\mathbb{G}-Brownian motions, namely 𝐙=(𝐙𝐒,ZY)⊤=(Z1S,…,ZnS,ZY)⊤\mathbf{Z}=\left(\mathbf{Z}^{\mathbf{S}},\,Z^{Y}\right)^{\top}=\left(Z^{S}\_{1},\,\dots,\,Z\_{n}^{S},\,Z^{Y}\right)^{\top}, as follow

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐖t𝐒WtY)=𝐋​(𝐙t𝐒ZtY),t∈[0,T],\begin{pmatrix}\mathbf{W}^{\mathbf{S}}\_{t}\\ W^{Y}\_{t}\end{pmatrix}=\mathbf{L}\begin{pmatrix}\mathbf{Z}^{\mathbf{S}}\_{t}\\ Z^{Y}\_{t}\end{pmatrix},\quad t\in[0,T], |  | (2.5) |

where 𝐋=(li,j)i,j∈{1,…,n+1}∈ℝ(n+1)×(n+1)\mathbf{L}=\left(l\_{i,j}\right)\_{i,j\in\left\{1,\dots,n+1\right\}}\in\mathbb{R}^{\left(n+1\right)\times\left(n+1\right)} is a lower triangular matrix obtained through the Cholesky decomposition of the correlation matrix 𝐑\mathbf{R}, that is 𝐑=𝐋𝐋⊤\mathbf{R}=\mathbf{L}\mathbf{L}^{\top}. Thus, the dynamics in ([2.3](https://arxiv.org/html/2511.19186v1#S2.E3 "In 2 The market setup ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([2.2](https://arxiv.org/html/2511.19186v1#S2.E2 "In 2 The market setup ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) can be rewritten as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =(λ​Yt+β)​d​t+𝚺~Y​d​𝐙t𝐒+σ~Y​d​ZtY,Y0∼N​(Γ0,P0),\displaystyle=\left(\lambda Y\_{t}+\beta\right)\mathrm{d}t+\mathbf{\tilde{\Sigma}}\_{Y}\mathrm{d}\mathbf{Z}\_{t}^{\mathbf{S}}+\tilde{\sigma}\_{Y}\mathrm{d}Z\_{t}^{Y},\quad Y\_{0}\sim N\left(\Gamma\_{0},P\_{0}\right), |  | (2.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​𝐒t\displaystyle\mathrm{d}\mathbf{S}\_{t} | =diag​(𝐒t)​[(𝐚​Yt+𝐛)​d​t+𝚺~𝐒​d​𝐙t𝐒],𝐒0∈ℝ+n,\displaystyle=\text{diag}\left(\mathbf{S}\_{t}\right)\left[\left(\mathbf{a}Y\_{t}+\mathbf{b}\right)\mathrm{d}t+\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{t}\right],\quad\mathbf{S}\_{0}\in\mathbb{R}^{n}\_{+}, |  | (2.7) |

respectively, where 𝚺~Y=σY​𝐋Y∈ℝ1×n\mathbf{\tilde{\Sigma}}\_{Y}=\sigma\_{Y}\mathbf{L}\_{Y}\in\mathbb{R}^{1\times n}, σ~Y=σY​ln+1,n+1∈ℝ\tilde{\sigma}\_{Y}=\sigma\_{Y}l\_{n+1,n+1}\in\mathbb{R}, 𝚺~𝐒=𝚺𝐒​𝐋𝐒=(σ~i,j)i,j∈{1,…,n}∈ℝn×n\mathbf{\tilde{\Sigma}\_{S}}=\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{L}\_{\mathbf{S}}=\left(\tilde{\sigma}\_{i,j}\right)\_{i,j\in\left\{1,\dots,n\right\}}\in\mathbb{R}^{n\times n}, with 𝐋Y=(ln+1,j)j∈{1,…,n}∈ℝ1×n\mathbf{L}\_{Y}=\left(l\_{n+1,j}\right)\_{j\in\left\{1,\dots,n\right\}}\in\mathbb{R}^{1\times n} and 𝐋𝐒=(li,j)i,j∈{1,…,n}∈ℝn×n\mathbf{L}\_{\mathbf{S}}=\left(l\_{i,j}\right)\_{i,j\in\left\{1,\dots,n\right\}}\in\mathbb{R}^{n\times n}.

## 3 The carbon-penalised proportional portfolio insurance strategy

The portfolio insurer employs a proportional portfolio insurance (PPI) strategy. Such strategies are designed to capitalise on the returns of the risky assets traded on the market while securing a pre-specified amount GG at maturity TT. To achieve this goal, the fund manager divides her position between the bank account BB, and a risky reference portfolio with value X={Xt}t∈[0,T]X=\left\{X\_{t}\right\}\_{t\in[0,T]}. The fund manager defines a floor process F={Ft}t∈[0,T]F=\left\{F\_{t}\right\}\_{t\in[0,T]} and a cushion process C={Ct}t∈[0,T]C=\left\{C\_{t}\right\}\_{t\in[0,T]}. The floor FF is given by the present value of the guarantee amount GG at maturity, that is Ft=G​e−r​(T−t)F\_{t}=Ge^{-r(T-t)} for all t∈[0,T]t\in[0,T], and represents the capital to be protected at every time.111Typically, the guaranteed amount GG is a pre-specified percentage of the initial endowment V0V\_{0}, namely G=V0⋅P​LG=V\_{0}\cdot PL, where PL∈(0,1]\mathrm{PL}\in(0,1] is the so-called protection level. The cushion CC is the difference between the current PPI portfolio value V={Vt}t∈[0,T]V=\left\{V\_{t}\right\}\_{t\in[0,T]} and the floor, that is Ct=Vt−FtC\_{t}=V\_{t}-F\_{t} for every t∈[0,T]t\in[0,T]. The exposure to the risky reference portfolio XX is linked to the cushion in the following way. At every time t∈[0,T]t\in[0,T], if Vt>FtV\_{t}>F\_{t} the exposure to XX is given by mt​Ctm\_{t}C\_{t}, where m={mt}t∈[0,T]m=\left\{m\_{t}\right\}\_{t\in[0,T]} is the proportionality factor known as multiplier. However, if there exists a time τ:=inf{t>0:Vt≤Ft}∧T\tau:=\inf\left\{t>0:V\_{t}\leq F\_{t}\right\}\wedge T, the portfolio value is entirely invested into the bank account BB, since Ct=0C\_{t}=0 for all t∈[τ∧T,T]t\in\left[\tau\wedge T,T\right]. To summarize, the exposure to the market index is given by mt​(Ct)+m\_{t}\left(C\_{t}\right)^{+} for every t∈[0,T]t\in[0,T]. Hence, the dynamics of the PPI portfolio is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt={r​Vt​d​t+(Vt−Ft)​mt​(d​XtXt−r​d​t),t<τ,r​Vt​d​t,t≥τ,\mathrm{d}V\_{t}=\begin{cases}\begin{aligned} &rV\_{t}\mathrm{d}t+\left(V\_{t}-F\_{t}\right)m\_{t}\left(\frac{\mathrm{d}X\_{t}}{X\_{t}}-rdt\right),\quad t<\tau,\\[8.0pt] &rV\_{t}\mathrm{d}t,\quad t\geq\tau,\end{aligned}\end{cases} |  | (3.1) |

with V0=v0V\_{0}=v\_{0} being the initial endowment, and the dynamics of the cushion C={Ct}t∈[τ∧T,T]C=\{C\_{t}\}\_{t\in[\tau\wedge T,T]} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​CtCt=\displaystyle\dfrac{\mathrm{d}C\_{t}}{C\_{t}}= | r​d​t+mt​(d​XtXt−r​d​t),C0=c0=v0−F0.\displaystyle r\mathrm{d}t+m\_{t}\left(\frac{\mathrm{d}X\_{t}}{X\_{t}}-r\mathrm{d}t\right),\quad C\_{0}=c\_{0}=v\_{0}-F\_{0}. |  | (3.2) |

Next, we introduce the dynamics of the risky reference portfolio. Let 𝝅={π1,t,…,πn,t}t∈[0,T]\bm{\pi}=\left\{\pi\_{1,t},\dots,\pi\_{n,t}\right\}\_{t\in[0,T]} be the vector-valued process in ℝn\mathbb{R}^{n} containing the composition percentage of the ii-th stock in the risky reference portfolio, for every i=1,…,ni=1,\dots,n and t∈[0,T]t\in[0,T]. Hence, the dynamics of X𝝅={Xt𝝅}t∈[0,T]X^{\bm{\pi}}=\left\{X\_{t}^{\bm{\pi}}\right\}\_{t\in[0,T]} read as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt𝝅Xt𝝅=𝝅t⊤​(𝐚​Yt+𝐛)​d​t+𝝅t⊤​𝚺~𝐒​d​𝐙𝐒,X0=x0.\dfrac{\mathrm{d}X\_{t}^{\bm{\pi}}}{X\_{t}^{\bm{\pi}}}=\bm{\pi}\_{t}^{\top}\left(\mathbf{a}Y\_{t}+\mathbf{b}\right)\mathrm{d}t+\bm{\pi}^{\top}\_{t}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}},\quad X\_{0}=x\_{0}. |  | (3.3) |

Assuming that ∑i=1nπi,t=1\sum\_{i=1}^{n}\pi\_{i,t}=1 for every t∈[0,T]t\in[0,T], for any given couple (m,𝝅)={mt,𝝅t}t∈[0,T]\left(m,\bm{\pi}\right)=\left\{m\_{t},\bm{\pi}\_{t}\right\}\_{t\in[0,T]}, equation ([3.1](https://arxiv.org/html/2511.19186v1#S3.E1 "In 3 The carbon-penalised proportional portfolio insurance strategy ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vtm,𝝅={r​Vtm,𝝅​d​t+(Vtm,𝝅−Ft)​mt​[𝝅t⊤​(𝐚​Yt+𝐛−𝐫n)​d​t+𝝅t⊤​𝚺~𝐒​d​𝐙t𝐒],t<τ,r​Vtm,𝝅​d​t,t≥τ,\mathrm{d}V\_{t}^{m,\bm{\pi}}=\begin{cases}\begin{aligned} &rV\_{t}^{m,\bm{\pi}}\mathrm{d}t+\left(V\_{t}^{m,\bm{\pi}}-F\_{t}\right)m\_{t}\left[\bm{\pi}\_{t}^{\top}\left(\mathbf{a}Y\_{t}+\mathbf{b}-\mathbf{r}\_{n}\right)\mathrm{d}t+\bm{\pi}\_{t}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{t}\right],\quad t<\tau,\\[8.0pt] &rV\_{t}^{m,\bm{\pi}}\mathrm{d}t,\quad t\geq\tau,\end{aligned}\end{cases} |  | (3.4) |

with V0m,𝝅=v0V\_{0}^{m,\bm{\pi}}=v\_{0} being the initial endowment, and consequently, ([3.2](https://arxiv.org/html/2511.19186v1#S3.E2 "In 3 The carbon-penalised proportional portfolio insurance strategy ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ctm,𝝅Ctm,𝝅=\displaystyle\dfrac{\mathrm{d}C\_{t}^{m,\bm{\pi}}}{C\_{t}^{m,\bm{\pi}}}= | [r+mt​𝝅t⊤​(𝐚​Yt+𝐛−𝐫n)]​d​t+mt​𝝅t⊤​𝚺~𝐒​d​𝐙t𝐒,C0m,𝝅=c0.\displaystyle\left[r+m\_{t}\bm{\pi}\_{t}^{\top}\left(\mathbf{a}Y\_{t}+\mathbf{b}-\mathbf{r}\_{n}\right)\right]\mathrm{d}t+m\_{t}\bm{\pi}\_{t}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{t},\quad C\_{0}^{m,\bm{\pi}}=c\_{0}. |  | (3.5) |

Here, we stress the dependence of the risky reference portfolio XX on its composition 𝝅\bm{\pi}, and the dependence of both the PPI portfolio value VV and the cushion CC on 𝝅\bm{\pi} and the multiplier mm. The fund manager’s objective is to maximise the expected utility from the terminal cushion in a carbon-penalised setting. In particular, the fund manager wants to prevent a high exposure of the strategy to brown stocks by adding a penalty term to the terminal cushion. In the same spirit of Rogers ([2013](https://arxiv.org/html/2511.19186v1#bib.bib24)), we assume that such penalisation is proportional to the riskiness of brown stocks, which is measured according to their realised variance. The carbon-penalised cushion at maturity is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^Tm,𝝅=CTm,𝝅​exp⁡{−12​∫0Tms2​𝝅s⊤​(𝚺𝐒​𝚺𝐒⊤⊙𝐞)​𝝅s​ds},\hat{C}^{m,\bm{\pi}}\_{T}=C^{m,\bm{\pi}}\_{T}\exp\left\{-\dfrac{1}{2}\int\_{0}^{T}m\_{s}^{2}\bm{\pi}\_{s}^{\top}\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}\right)\bm{\pi}\_{s}\mathrm{d}s\right\}, |  | (3.6) |

where ⊙\odot denotes the Hadamard product, and 𝐞=(𝟎k𝟏n−k​ε)⊤∈ℝn\mathbf{e}=\begin{pmatrix}\bm{0}\_{k}&\bm{1}\_{n-k}\varepsilon\end{pmatrix}^{\top}\in\mathbb{R}^{n} with ε≥0\varepsilon\geq 0 represents the fund manager’s carbon aversion with respect to brown stocks. It follows from Itô’s formula that the dynamics of C^m,𝝅={C^tm,𝝅}t∈[τ∧T,T]\hat{C}^{m,\bm{\pi}}=\{\hat{C}\_{t}^{m,\bm{\pi}}\}\_{t\in[\tau\wedge T,T]} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​C^tm,𝝅C^tm,𝝅=[r+mt​𝝅t⊤​(𝐚​Yt+𝐛−𝐫n)−12​mt2​𝝅t⊤​(𝚺𝐒​𝚺𝐒⊤⊙𝐞)​𝝅t]​d​t+mt​𝝅t⊤​𝚺~𝐒​d​𝐙t𝐒,C^0𝝅=c^0.\displaystyle\dfrac{\mathrm{d}\hat{C}\_{t}^{m,\bm{\pi}}}{\hat{C}\_{t}^{m,\bm{\pi}}}=\left[r+m\_{t}\bm{\pi}\_{t}^{\top}\left(\mathbf{a}Y\_{t}+\mathbf{b}-\mathbf{r}\_{n}\right)-\dfrac{1}{2}m\_{t}^{2}\bm{\pi}^{\top}\_{t}\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}\right)\bm{\pi}\_{t}\right]\mathrm{d}t+m\_{t}\bm{\pi}\_{t}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{t},\quad\hat{C}\_{0}^{\bm{\pi}}=\hat{c}\_{0}. |  | (3.7) |

###### Remark 3.1.

* (i)

  The penalisation embeds sustainability into the portfolio insurer’s preferences by increasing risk aversion specifically toward high–carbon-intensity stocks. Unlike Rogers ([2013](https://arxiv.org/html/2511.19186v1#bib.bib24)), our penalty excludes the variance–covariance matrix to avoid bias from negatively correlated brown stocks; instead, it relies solely on realised variance. Moreover, we do not impose a fixed sustainability target as in Bolton et al. ([2022](https://arxiv.org/html/2511.19186v1#bib.bib5)) and Le Guenedal and Roncalli ([2023](https://arxiv.org/html/2511.19186v1#bib.bib18)). This allows a flexible trade-off between a stock’s carbon intensity and its risk–return characteristics: high-carbon assets may still be held if their low volatility or high expected return compensates for their emissions. This is crucial for PI strategies, whose main goal is capital protection, as it prevents excessive penalisation of low-risk brown assets.
* (ii)

  The carbon penalty admits two interpretations. It can be seen as (i) a proportional cost on carbon-intensive holdings, balancing risk premia against reputational or regulatory costs, or (ii) an endogenous increase in the insurer’s risk aversion toward brown stocks. As shown in Example [4.1](https://arxiv.org/html/2511.19186v1#S4.Thmexample1 "Example 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), the effective risk aversion to such assets equals the market risk-aversion parameter plus the penalty term, naturally reducing exposure to carbon-intensive stocks (see, e.g. Colaneri et al. ([2025](https://arxiv.org/html/2511.19186v1#bib.bib9)) for more details on this point).

To reduce the number of controls of the optimisation problem, we introduce the process 𝜽={𝜽t}t∈[0,T]\bm{\theta}=\{\bm{\theta}\_{t}\}\_{t\in[0,T]} such that 𝜽t=mt​𝝅t\bm{\theta}\_{t}=m\_{t}\bm{\pi}\_{t}, for every t∈[0,T]t\in[0,T]. Hence, the dynamics of the carbon-penalised cushion can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​C^t𝜽C^t𝜽=[r+𝜽t⊤​(𝐚​Yt+𝐛−𝐫n)−12​𝜽t⊤​(𝚺𝐒​𝚺𝐒⊤⊙𝐞)​𝜽t]​d​t+𝜽t⊤​𝚺~𝐒​d​𝐙t𝐒,C^0𝜽=c^0.\displaystyle\dfrac{\mathrm{d}\hat{C}\_{t}^{\bm{\theta}}}{\hat{C}\_{t}^{\bm{\theta}}}=\left[r+\bm{\theta}\_{t}^{\top}\left(\mathbf{a}Y\_{t}+\mathbf{b}-\mathbf{r}\_{n}\right)-\dfrac{1}{2}\bm{\theta}^{\top}\_{t}\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}\right)\bm{\theta}\_{t}\right]\mathrm{d}t+\bm{\theta}\_{t}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{t},\quad\hat{C}\_{0}^{\bm{\theta}}=\hat{c}\_{0}. |  | (3.8) |

In the next section, we address the optimisation problem of the portfolio insurer under two different information settings. We begin with the case where she has full information on all factor processes that drive the market, and we refer to this as the full information case. Second, we assume that she cannot observe the common stochastic factor YY directly, but she can only infer its value from the observation of stock prices, and we call this case the partial information setting.

## 4 Optimisation problem under full information

We introduce the set of admissible strategies.

###### Definition 4.1.

A 𝔾\mathbb{G}-admissible carbon-penalised PPI strategy 𝛉={𝛉t}t∈[0,T]\bm{\theta}=\left\{\bm{\theta}\_{t}\right\}\_{t\in[0,T]} is a self-financing, 𝔾\mathbb{G}-predictable process such that

* (i)

  𝔼​[∫0T|Ys|​‖𝜽s‖1+‖𝜽s‖22​d​s]<∞\mathbb{E}\left[\int\_{0}^{T}|Y\_{s}|\|\bm{\theta}\_{s}\|\_{1}+\|\bm{\theta}\_{s}\|\_{2}^{2}\mathrm{d}s\right]<\infty,
* (ii)

  supt∈[0,T]𝔼​[(C^t𝜽)d​(1−δ)​(1+α)]<∞\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}\_{t}^{\bm{\theta}})^{d\left(1-\delta\right)(1+\alpha)}\right]<\infty, for some α>0\alpha>0 and d>1d>1.

We denote the set of 𝔾\mathbb{G}-admissible strategies by 𝒜𝔾\mathcal{A}^{\mathbb{G}}.

Note that we can equivalently rewrite the set of admissible strategies in terms of (m,𝝅)\left(m,\,\bm{\pi}\right) as follows. Precisely, a 𝔾\mathbb{G}-admissible carbon-penalised PPI strategy (m,𝝅)={mt,𝝅t}t∈[0,T]\left(m,\,\bm{\pi}\right)=\left\{m\_{t},\,\bm{\pi}\_{t}\right\}\_{t\in[0,T]} is a self-financing, 𝔾\mathbb{G}-predictable process such that

* (i)

  the following integrability condition holds

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼​[∫0T|Ys|​|ms|​‖𝝅s‖1+ms2​‖𝝅s‖22​d​s]<∞,\mathbb{E}\left[\int\_{0}^{T}|Y\_{s}||m\_{s}|\|\bm{\pi}\_{s}\|\_{1}+m\_{s}^{2}\|\bm{\pi}\_{s}\|\_{2}^{2}\mathrm{d}s\right]<\infty, |  | (4.1) |

  where ∥⋅∥1\|\cdot\|\_{1} and ∥⋅∥2\|\cdot\|\_{2} denote the ℓ1\ell\_{1} and ℓ2\ell\_{2} norms in ℝn\mathbb{R}^{n},
* (ii)

  supt∈[0,T]𝔼​[(C^tm,𝝅)d​(1−δ)​(1+α)]<∞\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}\_{t}^{m,\,\bm{\pi}})^{d\left(1-\delta\right)(1+\alpha)}\right]<\infty, for some α>0\alpha>0 and d>1d>1.

A fully informed portfolio insurer seeks to solve the following optimisation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Maximise ​𝔼t,c,y​[(C^T𝜽)1−δ1−δ], over all ​𝜽∈𝒜𝔾,\mbox{Maximise }\mathbb{E}^{t,c,y}\left[\dfrac{(\hat{C}\_{T}^{\bm{\theta}})^{1-\delta}}{1-\delta}\right],\mbox{ over all }\bm{\theta}\in\mathcal{A}^{\mathbb{G}}, |  | (4.2) |

where δ∈(0,1)∪(1,+∞)\delta\in\left(0,1\right)\cup\left(1,+\infty\right) represents the fund manager’s risk aversion parameter, and 𝔼t,c,y\mathbb{E}^{t,c,y} denotes the conditional expectation given C^t=c\hat{C}\_{t}=c and Yt=yY\_{t}=y. The value function of the optimisation problem in equation ([4.2](https://arxiv.org/html/2511.19186v1#S4.E2 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v^​(t,c,y):=sup𝜽∈𝒜𝔾𝔼t,c,y​[(C^T𝜽)1−δ1−δ].\hat{v}(t,c,y):=\sup\_{\bm{\theta}\in\mathcal{A}^{\mathbb{G}}}\mathbb{E}^{t,c,y}\left[\dfrac{(\hat{C}\_{T}^{\bm{\theta}})^{1-\delta}}{1-\delta}\right]. |  | (4.3) |

The problem is solved by employing dynamic programming principle. We consider the following Hamilton-Jacobi-Bellman equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | {sup𝜽∈𝒜v^t​(t,c,y)+ℒ𝜽​v^​(t,c,y)=0,(t,c,y)∈[0,T)×ℝ+×ℝ,v^​(T,c,y)=c1−δ1−δ,(c,y)∈ℝ+×ℝ,\begin{cases}\displaystyle\sup\_{\bm{\theta}\in\mathcal{A}}\hat{v}\_{t}(t,c,y)+\mathcal{L}^{\bm{\theta}}\hat{v}(t,c,y)=0,&(t,c,y)\in[0,T)\times\mathbb{R}\_{+}\times\mathbb{R},\\[8.0pt] \hat{v}(T,c,y)=\dfrac{c^{1-\delta}}{1-\delta},&(c,y)\in\mathbb{R}\_{+}\times\mathbb{R},\end{cases} |  | (4.4) |

where for any constant control 𝜽∈ℝn\bm{\theta}\in\mathbb{R}^{n}, the operator ℒθ\mathcal{L}^{\theta} denotes the infinitesimal generator of the process (C^t𝜽,Yt)(\hat{C}\_{t}^{\bm{\theta}},Y\_{t}) which is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒ𝜽​F​(t,c,y)=\displaystyle\mathcal{L}^{\bm{\theta}}F(t,c,y)= | c​[r+𝜽⊤​(𝐚​y+𝐛−𝒓n)−12​𝜽⊤​(𝚺𝐒​𝚺𝐒⊤⊙𝐞)​𝜽]​Fc​(t,c,y)+c22​𝜽⊤​𝚺~𝐒​𝚺~𝐒⊤​𝜽​Fc,c​(t,c,y)\displaystyle c\left[r+\bm{\theta}^{\top}\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right)-\dfrac{1}{2}\bm{\theta}^{\top}\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}\right)\bm{\theta}\right]F\_{c}(t,c,y)+\frac{c^{2}}{2}\bm{\theta}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\bm{\theta}F\_{c,c}(t,c,y) |  | (4.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(λ​y+β)​Fy​(t,c,y)+σY22​Fy,y​(t,c,y)+c​𝜽⊤​𝚺~𝐒​𝚺~Y⊤​Fc,y​(t,c,y),\displaystyle+\left(\lambda y+\beta\right)F\_{y}(t,c,y)+\dfrac{\sigma\_{Y}^{2}}{2}F\_{y,y}(t,c,y)+c\bm{\theta}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}F\_{c,y}(t,c,y), |  | (4.6) |

for every function F​(⋅)∈𝒞1,2,2​([0,T]×ℝ+×ℝ)F(\cdot)\in\mathcal{C}^{1,2,2}\left([0,T]\times\mathbb{R}\_{+}\times\mathbb{R}\right). In the sequel, we prove that the value function, defined in equation ([4.3](https://arxiv.org/html/2511.19186v1#S4.E3 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), solves the equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). We begin our analysis of the optimisation problem under full information with a verification result.

###### Theorem 4.2 (Verification Theorem).

Let f​(t,c,y)∈𝒞1,2,2​([0,T]×ℝ+×ℝ)f(t,c,y)\in\mathcal{C}^{1,2,2}([0,T]\times\mathbb{R}\_{+}\times\mathbb{R}) be a classical solution to the HJB equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and assume that the following conditions hold:

* (i)

  for any 𝜽∈𝒜𝔾\bm{\theta}\in\mathcal{A}^{\mathbb{G}}
  the family {f​(t∧τ,C^t∧τ,Yt∧τ), for all ​𝔾​–stopping times ​τ}\{f(t\wedge\tau,\hat{C}\_{t\wedge\tau},Y\_{t\wedge\tau}),\text{ for all }\mathbb{G}\text{--stopping times }\tau\} is uniformly integrable;
* (ii)

  there exists 𝜽⋆\bm{\theta}^{\star} at which the supremum in equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is attained.

Then f​(t,c,y)=v^​(t,c,y)f(t,c,y)=\hat{v}(t,c,y) and if {𝛉⋆​(t,Yt)}t∈[0,T]∈𝒜𝔾\{\bm{\theta}^{\star}(t,Y\_{t})\}\_{t\in[0,T]}\in\mathcal{A}^{\mathbb{G}} this is an optimal Markovian control.

###### Proof.

See Appendix [A.1](https://arxiv.org/html/2511.19186v1#A1.SS1 "A.1 Proof of Theorem 4.2 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

###### Theorem 4.3.

Let f^​(t),g^​(t),h^​(t)∈𝒞b1​([0,T])\hat{f}(t),\hat{g}(t),\hat{h}(t)\in\mathcal{C}\_{b}^{1}([0,T]) be the unique solutions to the following system of ODEs

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=\displaystyle 0= | f^t​(t)+[(1−δ)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝚺~𝐒​𝚺~Y⊤+σY2]​f^2​(t)+2​[(1−δ)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝐚+λ]​f^​(t)\displaystyle\hat{f}\_{t}(t)+\left[\left(1-\delta\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}+\sigma\_{Y}^{2}\right]\hat{f}^{2}(t)+2\left[\left(1-\delta\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a}+\lambda\right]\hat{f}(t) |  | (4.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−δ)​𝐚⊤​𝚯^−1​𝐚,\displaystyle+\left(1-\delta\right)\mathbf{a}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a}, |  | (4.8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=\displaystyle 0= | g^t​(t)+[(1−δ)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝐚+λ]​g^​(t)+[(1−δ)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​(𝐛−𝐫n)+β]​f^​(t)\displaystyle\hat{g}\_{t}(t)+\left[\left(1-\delta\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a}+\lambda\right]\hat{g}(t)+\left[\left(1-\delta\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)+\beta\right]\hat{f}(t) |  | (4.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +[(1−δ)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝚺~𝐒​𝚺~Y⊤+σY2]​f^​(t)​g^​(t)+(1−δ)​𝐚⊤​𝚯^−1​(𝐛−𝒓n),\displaystyle+\left[\left(1-\delta\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}+\sigma\_{Y}^{2}\right]\hat{f}(t)\hat{g}(t)+\left(1-\delta\right)\mathbf{a}^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\bm{r}\_{n}\right), |  | (4.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=\displaystyle 0= | h^t​(t)+(1−δ)​r+[(1−δ)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​(𝐛−𝐫n)+β]​g^​(t)+σY22​f^​(t)\displaystyle\hat{h}\_{t}(t)+\left(1-\delta\right)r+\left[\left(1-\delta\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)+\beta\right]\hat{g}(t)+\dfrac{\sigma\_{Y}^{2}}{2}\hat{f}(t) |  | (4.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12​[(1−δ)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝚺~𝐒​𝚺~Y⊤+σY2]​g^2​(t)+1−δ2​(𝐛−𝒓n)⊤​𝚯^−1​(𝐛−𝒓n),\displaystyle+\dfrac{1}{2}\left[\left(1-\delta\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}+\sigma\_{Y}^{2}\right]\hat{g}^{2}(t)+\dfrac{1-\delta}{2}\left(\mathbf{b}-\bm{r}\_{n}\right)^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\bm{r}\_{n}\right), |  | (4.12) |

with terminal conditions f^​(T)=g^​(T)=h^​(T)=0\hat{f}(T)=\hat{g}(T)=\hat{h}(T)=0, where 𝚯^=(𝚺𝐒​𝚺𝐒⊤)⊙𝐞+δ​𝚺~𝐒​𝚺~𝐒⊤\mathbf{\hat{\Theta}}=\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\right)\odot\mathbf{e}+\delta\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}. Then, the optimal control is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽⋆​(t,y)=𝚯^−1​(𝐚​y+𝐛−𝒓n)+𝚯^−1​𝚺~𝐒​𝚺~Y⊤​(f^​(t)​y+g^​(t)),\bm{\theta}^{\star}(t,y)=\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right)+\mathbf{\hat{\Theta}}^{-1}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}\left(\hat{f}(t)y+\hat{g}(t)\right), |  | (4.13) |

and the value function satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | v^​(t,c,y)=c1−δ1−δ​exp⁡{f^​(t)2​y2+g^​(t)​y+h^​(t)}.\hat{v}(t,c,y)=\dfrac{c^{1-\delta}}{1-\delta}\exp\left\{\frac{\hat{f}(t)}{2}y^{2}+\hat{g}(t)y+\hat{h}(t)\right\}. |  | (4.14) |

###### Proof.

See Appendix [A.2](https://arxiv.org/html/2511.19186v1#A1.SS2 "A.2 Proof of Theorem 4.3 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

We now characterise the range of risk aversion parameters that guarantee f^​(t)∈𝒞b1​([0,T])\hat{f}(t)\in\mathcal{C}^{1}\_{b}([0,T]). We define the function Δ​(x):(0,+∞)→ℝ\Delta(x):(0,+\infty)\to\mathbb{R} as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(x)=4​{[(1−x)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝐚+λ]2−[(1−x)2​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝚺~𝐒​𝚺~Y⊤+(1−x)​σY2]​𝐚⊤​𝚯^−1​𝐚},\Delta(x)=4\left\{\left[\left(1-x\right)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a}+\lambda\right]^{2}-\left[\left(1-x\right)^{2}\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}+\left(1-x\right)\sigma\_{Y}^{2}\right]\mathbf{a}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a}\right\}, |  | (4.15) |

which represents the discriminant of the Riccati ODE f^\hat{f} in ([4.8](https://arxiv.org/html/2511.19186v1#S4.E8 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), and define the set 𝒫={δ∈(0,1)∪(1,+∞):Δ​(δ)>0}\mathcal{P}=\{\delta\in(0,1)\cup(1,+\infty):\Delta(\delta)>0\}. The set 𝒫\mathcal{P} represents set of risk aversion parameters for which f^​(t)∈𝒞b1​([0,T])\hat{f}(t)\in\mathcal{C}^{1}\_{b}([0,T]).

###### Proposition 4.4.

The set 𝒫\mathcal{P} is not empty.

###### Proof.

This result is a consequence of the fact that Δ​(x)\Delta(x) is a continuous function and that Δ​(1)=λ2>0\Delta(1)=\lambda^{2}>0; hence, there exists a neighborhood of δ=1\delta=1 contained in 𝒫\mathcal{P} such that Δ​(δ)>0\Delta(\delta)>0.
∎

By virtue of Proposition [4.4](https://arxiv.org/html/2511.19186v1#S4.Thmthm4 "Proposition 4.4. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), there exist values of δ\delta contained in 𝒫\mathcal{P} such that f^​(t)∈𝒞b1​([0,T])\hat{f}(t)\in\mathcal{C}^{1}\_{b}([0,T]). As a consequence, the solutions of the linear ODEs in equations ([4.10](https://arxiv.org/html/2511.19186v1#S4.E10 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([4.12](https://arxiv.org/html/2511.19186v1#S4.E12 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) also exist and share the same regularity.

###### Remark 4.5.

Proposition [4.4](https://arxiv.org/html/2511.19186v1#S4.Thmthm4 "Proposition 4.4. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") ensures that the system of ODEs in equations ([4.8](https://arxiv.org/html/2511.19186v1#S4.E8 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([4.10](https://arxiv.org/html/2511.19186v1#S4.E10 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), and ([4.12](https://arxiv.org/html/2511.19186v1#S4.E12 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) admits a solution that does not explode in finite time, for some values of the risk aversion parameter δ\delta. In particular, it guarantees the existence of a solution for risk aversion parameters that are close to logarithmic utility. In a multidimensional setting, such as the one considered in this paper, deriving conditions for the existence of a solution over a broader range of δ\delta is not straightforward. As a result, identifying the largest possible set 𝒫\mathcal{P}, which depends on several model parameters (e.g., the variance-covariance matrices), remains a challenging task. Nevertheless, 𝒫\mathcal{P} can be explicitly identified in a simplified setting with two uncorrelated assets, independent of the common stochastic factor YY (see Appendix [B](https://arxiv.org/html/2511.19186v1#A2 "Appendix B An example involving two uncorrelated assets, independent of the factor process ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")).

The optimal candidate strategy 𝜽⋆={𝜽⋆​(t,Yt)}t∈[0,T]\bm{\theta}^{\star}=\{\bm{\theta}^{\star}(t,Y\_{t})\}\_{t\in[0,T]}, where 𝜽⋆​(t,y)\bm{\theta}^{\star}(t,y) is defined by equation ([4.13](https://arxiv.org/html/2511.19186v1#S4.E13 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), is Markovian, as it depends exclusively on time and the exogenous factor YY. We now provide conditions on the model parameters ensuring that condition (i) of Theorem [4.2](https://arxiv.org/html/2511.19186v1#S4.Thmthm2 "Theorem 4.2 (Verification Theorem). ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") is satisfied and that 𝜽⋆\bm{\theta}^{\star} is an admissible control, according to Definition [4.1](https://arxiv.org/html/2511.19186v1#S4.Thmthm1 "Definition 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). These results are stated and proved in the following propositions.

###### Proposition 4.6.

Assume that one of the two following conditions holds

* (i)

  δ∈𝒫∩(1,+∞)\delta\in\mathcal{P}\cap(1,+\infty),
* (ii)

  δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1) and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 1−q​(1+α)​f^​(0)​max⁡{P0,Var​[YT]}>0,1-q(1+\alpha)\hat{f}(0)\max\left\{P\_{0},\text{Var}[Y\_{T}]\right\}>0, |  | (4.16) |

  for some q>1q>1.

Then, for any admissible strategy 𝛉∈𝒜𝔾\bm{\theta}\in\mathcal{A}^{\mathbb{G}}, {v​(τ,C^τ,Yτ), for all ​𝔾​-stopping times ​τ≤T}\{v(\tau,\hat{C}\_{\tau},Y\_{\tau}),\mbox{ for all }\mathbb{G}\mbox{-stopping times }\tau\leq T\} forms a uniformly integrable family.

###### Proof.

The proof is provided in Appendix [A.3](https://arxiv.org/html/2511.19186v1#A1.SS3 "A.3 Proof of Proposition 4.6 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

In the next Proposition, we provide sufficient conditions for admissibility of the optimal strategy.

###### Proposition 4.7.

Assume that one of the two following conditions holds

* (i)

  δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1) and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 1−8​d​(1−δ)​(1+α)​n​T​[(1∨d​(1−δ)​(1+α)​w)​c12+aM2]​max⁡{P0,Var​[YT]}>0,1-8d(1-\delta)(1+\alpha)nT\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)c\_{1}^{2}+a\_{M}^{2}\right]\max\left\{P\_{0},\text{Var}[Y\_{T}]\right\}>0, |  | (4.17) |
* (ii)

  δ∈𝒫∩(1,+∞)\delta\in\mathcal{P}\cap(1,+\infty) and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 1−8​d​(1−δ)​(1+α)​n​T​[(−(1+w)∧d​(1−δ)​(1+α)​w~)​c12−aM2]​max⁡{P0,Var​[YT]}>0,1-8d(1-\delta)(1+\alpha)nT\left[\left(-(1+w)\wedge d(1-\delta)(1+\alpha)\tilde{w}\right)c\_{1}^{2}-a\_{M}^{2}\right]\max\left\{P\_{0},\text{Var}[Y\_{T}]\right\}>0, |  | (4.18) |

  for some d>1d>1, where

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | aM\displaystyle a\_{M} | =maxi=1,…,n⁡|(𝐚)i|,\displaystyle=\max\_{i=1,\dots,n}|\left(\mathbf{a}\right)\_{i}|, |  | (4.19) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | w\displaystyle w | =maxi,j=1,…,n⁡|(𝚺~𝐒​𝚺~𝐒⊤)i,j|,\displaystyle=\max\_{i,j=1,\dots,n}\left|\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)\_{i,j}\right|, |  | (4.20) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | w~\displaystyle\tilde{w} | =maxi,j=1,…,n⁡|(𝚯^)i,j|,\displaystyle=\max\_{i,j=1,\dots,n}|(\mathbf{\hat{\Theta}})\_{i,j}|, |  | (4.21) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | c1\displaystyle c\_{1} | =maxi=1,…,n⁡|(𝚯^−1​(𝐚+𝚺~𝐒​𝚺~Y⊤​supt∈[0,T]f^​(t)))i|.\displaystyle=\max\_{i=1,\dots,n}\bigg|\left(\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}+\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\sup\_{t\in[0,T]}\hat{f}(t)\right)\right)\_{i}\bigg|. |  | (4.22) |

Then, the process 𝛉⋆\bm{\theta}^{\star} given by equation ([4.13](https://arxiv.org/html/2511.19186v1#S4.E13 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is an admissible strategy.

###### Proof.

The proof is provided in Appendix [A.4](https://arxiv.org/html/2511.19186v1#A1.SS4 "A.4 Proof of Proposition 4.7 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

Under the assumption of Proposition [4.6](https://arxiv.org/html/2511.19186v1#S4.Thmthm6 "Proposition 4.6. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), the value function v^\hat{v} is the unique solution of the optimisation problem [4.2](https://arxiv.org/html/2511.19186v1#S4.E2 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") and 𝜽⋆∈𝒜\bm{\theta}^{\star}\in\mathcal{A}. Given 𝜽⋆\bm{\theta}^{\star}, we can characterise the optimal multiplier m⋆m^{\star} and the optimal stock composition percentages 𝝅⋆\bm{\pi}^{\star} of the risky reference portfolio as in the following Proposition.

###### Proposition 4.8.

The optimal multiplier is given by mt⋆=𝛉⋆,⊤​𝟏nm^{\star}\_{t}=\bm{\theta}^{\star,\top}\mathbf{1}\_{n} and the optimal composition percentage of the ii-th stock in the risky reference portfolio XX is given by πi,t⋆=θi,t⋆𝛉⋆,⊤​𝟏n\pi^{\star}\_{i,t}=\frac{\theta^{\star}\_{i,t}}{\bm{\theta}^{\star,\top}\mathbf{1}\_{n}}, for every i=1,…,ni=1,\dots,n, and t∈[0,T]t\in[0,T].

###### Proof.

The proof is provided in Appendix [A.5](https://arxiv.org/html/2511.19186v1#A1.SS5 "A.5 Proof of Proposition 4.8 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

###### Example 4.1.

To analyze the optimal PPI strategy, we consider the case in which only two stocks, S1S\_{1} and S2S\_{2}, are traded on the market, representing a green and a brown stock, respectively. For simplicity, we assume that S1S\_{1} and S2S\_{2} are driven by independent Brownian motions. Applying Proposition [4.8](https://arxiv.org/html/2511.19186v1#S4.Thmthm8 "Proposition 4.8. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), the optimal multiplier m⋆m^{\star} reads as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | m⋆​(t,y;δ,ε)=θ1⋆​(t,y;δ)+θ2⋆​(t,y;δ,ε),m^{\star}(t,y;\delta,\varepsilon)=\theta\_{1}^{\star}(t,y;\delta)+\theta\_{2}^{\star}(t,y;\delta,\varepsilon), |  | (4.23) |

where θ1⋆​(t,y;δ)=ξ1M​(t,y;δ)+ξ1I​(t,y;δ)\theta\_{1}^{\star}(t,y;\delta)=\xi\_{1}^{M}(t,y;\delta)+\xi\_{1}^{I}(t,y;\delta) and θ2⋆​(t,y;δ,ε)=ξ2M​(t,y;δ,ε)+ξ2I​(t,y;δ,ε)\theta\_{2}^{\star}(t,y;\delta,\varepsilon)=\xi\_{2}^{M}(t,y;\delta,\varepsilon)+\xi\_{2}^{I}(t,y;\delta,\varepsilon), with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ1M​(t,y;δ)\displaystyle\xi\_{1}^{M}(t,y;\delta) | =1δ​a1​y+b1−rσ12,ξ1I​(t,y;δ)=1δ​σY​ρ1,Yσ1​(f^​(t)​y+g^​(t)),\displaystyle=\dfrac{1}{\delta}\dfrac{a\_{1}y+b\_{1}-r}{\sigma\_{1}^{2}},\quad\xi\_{1}^{I}(t,y;\delta)=\dfrac{1}{\delta}\dfrac{\sigma\_{Y}\rho\_{1,Y}}{\sigma\_{1}}\left(\hat{f}(t)y+\hat{g}(t)\right), |  | (4.24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ2M​(t,y;δ,ε)\displaystyle\xi\_{2}^{M}(t,y;\delta,\varepsilon) | =1ε+δ​a2​y+b2−rσ22,ξ2I​(t,y;δ,ε)=1ε+δ​σY​ρ2,Yσ2​(f^​(t)​y+g^​(t)),\displaystyle=\dfrac{1}{\varepsilon+\delta}\dfrac{a\_{2}y+b\_{2}-r}{\sigma\_{2}^{2}},\quad\xi\_{2}^{I}(t,y;\delta,\varepsilon)=\dfrac{1}{\varepsilon+\delta}\dfrac{\sigma\_{Y}\rho\_{2,Y}}{\sigma\_{2}}\left(\hat{f}(t)y+\hat{g}(t)\right), |  | (4.25) |

for every (t,y)∈[0,T]×ℝ\left(t,y\right)\in[0,T]\times\mathbb{R}. The optimal multiplier is the sum of the myopic and intertemporal hedging demand relative to each of the two stocks included in the risky reference portfolio. Both the myopic and the intertemporal components relative to the brown stock depend on the carbon aversion factor ε\varepsilon. Hence, by introducing a penalty term proportional to the realised volatilities of brown stocks in the objective function, we have effectively increased the fund manager’s risk aversion toward this category of assets. The optimal composition percentages of the stocks in the risky reference portfolio (π1⋆,π2⋆)\left(\pi^{\star}\_{1},\pi^{\star}\_{2}\right) are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π1⋆​(t,y;δ,ε)\displaystyle\pi\_{1}^{\star}(t,y;\delta,\varepsilon) | =(ε+δ)​[a1​y+b1−r+σ1​σY​ρ1,Y​(f^​(t)​y+g^​(t))]​σ22(ε+δ)​(a1​y+b1−r)​σ22+δ​(a2​y+b2−r)​σ12+[(ε+δ)​σ1​σ22​ρ1,Y+δ​σ12​σ2​ρ2,Y]​σY​(f^​(t)​y+g^​(t)),\displaystyle=\dfrac{\left(\varepsilon+\delta\right)\left[a\_{1}y+b\_{1}-r+\sigma\_{1}\sigma\_{Y}\rho\_{1,Y}\left(\hat{f}(t)y+\hat{g}(t)\right)\right]\sigma\_{2}^{2}}{\left(\varepsilon+\delta\right)\left(a\_{1}y+b\_{1}-r\right)\sigma\_{2}^{2}+\delta\left(a\_{2}y+b\_{2}-r\right)\sigma\_{1}^{2}+\left[\left(\varepsilon+\delta\right)\sigma\_{1}\sigma\_{2}^{2}\rho\_{1,Y}+\delta\sigma\_{1}^{2}\sigma\_{2}\rho\_{2,Y}\right]\sigma\_{Y}(\hat{f}(t)y+\hat{g}(t))}, |  | (4.26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π2⋆​(t,y;δ,ε)\displaystyle\pi\_{2}^{\star}(t,y;\delta,\varepsilon) | =δ​[a2​y+b2−r+σ2​σY​ρ2,Y​(f^​(t)​y+g^​(t))]​σ12(ε+δ)​(a1​y+b1−r)​σ22+δ​(a2​y+b2−r)​σ12+[(ε+δ)​σ1​σ22​ρ1,Y+δ​σ12​σ2​ρ2,Y]​σY​(f^​(t)​y+g^​(t)),\displaystyle=\dfrac{\delta\left[a\_{2}y+b\_{2}-r+\sigma\_{2}\sigma\_{Y}\rho\_{2,Y}(\hat{f}(t)y+\hat{g}(t))\right]\sigma\_{1}^{2}}{\left(\varepsilon+\delta\right)\left(a\_{1}y+b\_{1}-r\right)\sigma\_{2}^{2}+\delta\left(a\_{2}y+b\_{2}-r\right)\sigma\_{1}^{2}+\left[\left(\varepsilon+\delta\right)\sigma\_{1}\sigma\_{2}^{2}\rho\_{1,Y}+\delta\sigma\_{1}^{2}\sigma\_{2}\rho\_{2,Y}\right]\sigma\_{Y}(\hat{f}(t)y+\hat{g}(t))}, |  | (4.27) |

for every (t,y)∈[0,T]×ℝ\left(t,y\right)\in[0,T]\times\mathbb{R}. We observe that π1⋆\pi\_{1}^{\star} (respectively, π2⋆\pi\_{2}^{\star}) is increasing (respectively, decreasing) with respect to the carbon aversion parameter ε\varepsilon. As expected, the higher ε\varepsilon, the lower (respectively, higher) the presence of brown (respectively, green) stock in XX. Hence, any increase of ε\varepsilon results in a reduction of the overall carbon intensity of the risky reference portfolio and, consequently, of the PPI strategy. In the limiting case where ε→∞\varepsilon\to\infty, π1⋆=1\pi^{\star}\_{1}=1 and π2⋆=0\pi^{\star}\_{2}=0, meaning that the risky reference portfolio fully coincides with the green stock. Moreover, the optimal multiplier becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | m⋆​(t,y;δ,ε=+∞)=1δ​[a1​y+b1−rσ12+σY​ρ1,Y​(f^​(t;ε=∞)​y+g^​(t;ε=∞))σ1],m^{\star}(t,y;\delta,\varepsilon=+\infty)=\dfrac{1}{\delta}\left[\dfrac{a\_{1}y+b\_{1}-r}{\sigma\_{1}^{2}}+\dfrac{\sigma\_{Y}\rho\_{1,Y}(\hat{f}(t;\varepsilon=\infty)y+\hat{g}(t;\varepsilon=\infty))}{\sigma\_{1}}\right], |  | (4.28) |

recovering the optimal PPI strategy with one single investment asset, see, e.g., Zieling et al. ([2014](https://arxiv.org/html/2511.19186v1#bib.bib28)).

#### Logarithmic case.

We assume that the fund manager is endowed with a logarithmic utility function. In such a case, the optimisation problem ([4.2](https://arxiv.org/html/2511.19186v1#S4.E2 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) can be reformulated as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Maximise ​𝔼t,c,y​[log⁡(C^T𝜽)],\mbox{Maximise }\mathbb{E}^{t,c,y}\left[\log(\hat{C}\_{T}^{\bm{\theta}})\right], |  | (4.29) |

over all 𝜽∈𝒜𝔾\bm{\theta}\in\mathcal{A}^{\mathbb{G}}, and the corresponding value function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,c,y):=sup𝜽∈𝒜𝔾𝔼t,c,y​[log⁡(C^T𝜽)].v(t,c,y):=\sup\_{\bm{\theta}\in\mathcal{A}^{\mathbb{G}}}\mathbb{E}^{t,c,y}\left[\log(\hat{C}\_{T}^{\bm{\theta}})\right]. |  | (4.30) |

For the logarithmic case, the optimal strategy can be derived by applying pointwise maximisation, which also yields an explicit characterisation for the value function. This result is presented in the following corollary.

###### Corollary 4.9.

Consider a fund manager endowed with a logarithmic utility function and a carbon aversion ε≥0\varepsilon\geq 0, then the optimal controls 𝛉⋆∈𝒜𝔾\bm{\theta}^{\star}\in\mathcal{A}^{\mathbb{G}} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽⋆​(t,y)=𝚯−1​(𝐚​y+𝐛−𝐫n),\displaystyle\bm{\theta}^{\star}(t,y)=\mathbf{\Theta}^{-1}\left(\mathbf{a}y+\mathbf{b}-\mathbf{r}\_{n}\right), |  | (4.31) |

where 𝚯=(𝚺𝐒​𝚺𝐒⊤)⊙𝐞+𝚺~𝐒​𝚺~𝐒⊤\mathbf{\Theta}=\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\right)\odot\mathbf{e}+\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}. The value function reads as

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,c,y)=log⁡(c)+r​(T−t)+f​(t)​y2+g​(t)​y+h​(t),v(t,c,y)=\log(c)+r(T-t)+f(t)y^{2}+g(t)y+h(t), |  | (4.32) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t)=𝐚⊤​𝚯−1​𝐚2​λ​(e2​λ​(T−t)−1),\displaystyle f(t)=\frac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2\lambda}\left(e^{2\lambda\left(T-t\right)}-1\right), |  | (4.33) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t)=𝐚⊤​𝚯−1​(𝐛−𝐫n)λ​(eλ​(T−t)−1)+β​𝐚⊤​𝚯−1​𝐚2​λ2​(eλ​(T−t)−1)2,\displaystyle g(t)=\frac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}(\mathbf{b}-\mathbf{r}\_{n})}{\lambda}\left(e^{\lambda\left(T-t\right)}-1\right)+\beta\frac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2\lambda^{2}}\left(e^{\lambda\left(T-t\right)}-1\right)^{2}, |  | (4.34) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(t)=[r+12​(𝐛−𝐫n)⊤​𝚯−1​(𝐛−𝐫n)]​(T−t)+β​𝐚⊤​𝚯−1​(𝐛−𝐫n)λ​[eλ​(T−t)−1λ−(T−t)]\displaystyle h(t)=\left[r+\dfrac{1}{2}\left(\mathbf{b}-\mathbf{r}\_{n}\right)^{\top}\mathbf{\Theta}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)\right]\left(T-t\right)+\beta\dfrac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)}{\lambda}\left[\frac{e^{\lambda\left(T-t\right)}-1}{\lambda}-\left(T-t\right)\right] |  | (4.35) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +β2​𝐚⊤​𝚯−1​𝐚2​λ2​[e2​λ​(T−t)−12​λ−2λ​(eλ​(T−t)−1)+T−t]+σY22​𝐚⊤​𝚯−1​𝐚2​λ​[e2​λ​(T−t)−12​λ−(T−t)],\displaystyle+\beta^{2}\dfrac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2\lambda^{2}}\left[\dfrac{e^{2\lambda\left(T-t\right)}-1}{2\lambda}-\frac{2}{\lambda}\left(e^{\lambda\left(T-t\right)}-1\right)+T-t\right]+\frac{\sigma\_{Y}^{2}}{2}\dfrac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2\lambda}\left[\frac{e^{2\lambda\left(T-t\right)}-1}{2\lambda}-\left(T-t\right)\right], |  | (4.36) |

for every t∈[0,T]t\in[0,T].

###### Proof.

The proof is provided in Appendix [A.6](https://arxiv.org/html/2511.19186v1#A1.SS6 "A.6 Proof of Corollary 4.9 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

In the case of the logarithmic utility function, the optimal strategy (m⋆,π1⋆,π2⋆)\left(m^{\star},\pi\_{1}^{\star},\pi\_{2}^{\star}\right) discussed in Example [4.1](https://arxiv.org/html/2511.19186v1#S4.Thmexample1 "Example 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | m⋆​(t,y;1,ε)\displaystyle m^{\star}(t,y;1,\varepsilon) | =ξ1M​(t,y;1)+ξ2M​(t,y;1,ε),\displaystyle=\xi^{M}\_{1}(t,y;1)+\xi^{M}\_{2}(t,y;1,\varepsilon), |  | (4.37) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π1⋆​(t,y;1,ε)\displaystyle\pi^{\star}\_{1}(t,y;1,\varepsilon) | =ξ1M​(t,y;1)m⋆​(t,y;1,ε),π2⋆​(t,y;1,ε)=ξ2M​(t,y;1,ε)m⋆​(t,y;1,ε),\displaystyle=\dfrac{\xi\_{1}^{M}(t,y;1)}{m^{\star}(t,y;1,\varepsilon)},\quad\pi^{\star}\_{2}(t,y;1,\varepsilon)=\dfrac{\xi\_{2}^{M}(t,y;1,\varepsilon)}{m^{\star}(t,y;1,\varepsilon)}, |  | (4.38) |

for every (t,y)∈[0,T]×ℝ\left(t,y\right)\in[0,T]\times\mathbb{R}. As expected by the nature of the utility function, the optimal multiplier presents only the myopic component. The factor ξ2\xi\_{2} depends on carbon penalisation in the same form as for the power utility case. Similar considerations on (π1⋆,π2⋆)\left(\pi\_{1}^{\star},\pi\_{2}^{\star}\right), as for the power utility case, hold for logarithmic utility.

## 5 Optimisation problem under partial information

In this section, we address the utility maximisation problem faced by a portfolio insurer who cannot directly observe the common stochastic factor YY. The portfolio insurer’s available information is limited to observing the price processes of green and brown stocks. Mathematically, the information flow accessible to the fund manager is given by the natural filtration generated by 𝐒\mathbf{S}, referred to as 𝔽={ℱt}t∈[0,T]\mathbb{F}=\left\{\mathcal{F}\_{t}\right\}\_{t\in[0,T]}, where ℱt=σ​{𝐒u, 0≤u≤t}∨𝒩\mathcal{F}\_{t}=\sigma\left\{\mathbf{S}\_{u},\,0\leq u\leq t\right\}\vee\mathcal{N} such that ℱt⊂𝒢t\mathcal{F}\_{t}\subset\mathcal{G}\_{t}. Here, 𝒩\mathcal{N} represents the collection of ℙ\mathbb{P}-null sets, and ℱ0\mathcal{F}\_{0} is the trivial σ\sigma-algebra. The portfolio insurer, operating under partial information, seeks to maximise the expected CRRA utility of the terminal carbon-penalised cushion over the set of 𝔽\mathbb{F}-admissible strageies 𝒜𝔽\mathcal{A}^{\mathbb{F}} defined below (see Definition [5.1](https://arxiv.org/html/2511.19186v1#S5.Thmthm1 "Definition 5.1. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). To address the optimisation problem with partial observations, we introduce the conditional distribution of the unobservable factor process YY, using stochastic filtering theory.

Let Γ\Gamma and PP be the conditional expectation and the conditional variance of the common stochastic factor YY given the available information, that is, Γt:=𝔼​[Yt|ℱt]\Gamma\_{t}:=\mathbb{E}\left[Y\_{t}|\mathcal{F}\_{t}\right] and Pt:=𝔼​[(Yt−Γt)2|ℱt]P\_{t}:=\mathbb{E}\left[\left(Y\_{t}-\Gamma\_{t}\right)^{2}|\mathcal{F}\_{t}\right] for every t∈[0,T]t\in[0,T], respectively. Since the conditional distribution of YY is Gaussian, it is fully characterised by its conditional mean and variance dynamics. Moreover, since ℱ0\mathcal{F}\_{0} is the trivial σ\sigma-algebra, the initial values Γ\Gamma and PP correspond to the parameters of the initial distribution of YY, that is, Y0∼N​(Γ0,P0)Y\_{0}\sim N(\Gamma\_{0},P\_{0}).
To characterise the dynamics of Γ\Gamma and PP, we introduce the innovation process 𝐈𝐒={𝐈t𝐒}t∈[0,T]\mathbf{I}^{\mathbf{S}}=\left\{\mathbf{I}^{\mathbf{S}}\_{t}\right\}\_{t\in[0,T]},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐈t𝐒=𝚺~𝐒−1​𝐚​∫0t(Ys−Γs)​ds+𝐙t𝐒,\displaystyle\mathbf{I}^{\mathbf{S}}\_{t}=\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{-1}\mathbf{a}\int\_{0}^{t}\left(Y\_{s}-\Gamma\_{s}\right)\mathrm{d}s+\mathbf{Z}\_{t}^{\mathbf{S}}, |  | (5.1) |

for every t∈[0,T]t\in[0,T]. As proven in (Liptser and Shiryaev, [2013](https://arxiv.org/html/2511.19186v1#bib.bib20), Section 10.310.3), 𝐈𝐒\mathbf{I}^{\mathbf{S}} is an (𝔽,ℙ)\left(\mathbb{F},\mathbb{P}\right)-Brownian motion in ℝn\mathbb{R}^{n}, and the processes Γ\Gamma and PP are the unique solutions
to the system

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Γt\displaystyle\mathrm{d}\Gamma\_{t} | =(λ​Γt+β)​d​t+𝐏¯t​(𝚺~𝐒⊤)−1​d​𝐈t𝐒,Γ0∈ℝ,\displaystyle=\left(\lambda\Gamma\_{t}+\beta\right)\mathrm{d}t+\mathbf{\bar{P}}\_{t}\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\mathrm{d}\mathbf{I}\_{t}^{\mathbf{S}},\quad\Gamma\_{0}\in\mathbb{R}, |  | (5.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ptd​t\displaystyle\dfrac{\mathrm{d}P\_{t}}{\mathrm{d}t} | =2​λ​Pt+σY2−𝐏¯t​(𝚺~𝐒​𝚺~𝐒⊤)−1​𝐏¯t⊤,P0∈ℝ+,\displaystyle=2\lambda P\_{t}+\sigma\_{Y}^{2}-\mathbf{\bar{P}}\_{t}\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\mathbf{\bar{P}}\_{t}^{\top},\quad P\_{0}\in\mathbb{R}\_{+}, |  | (5.3) |

where 𝐏¯t=𝚺~Y​𝚺~𝐒⊤+Pt​𝐚⊤\mathbf{\bar{P}}\_{t}=\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}+P\_{t}\mathbf{a}^{\top} for every t∈[0,T]t\in[0,T], and PtP\_{t} and 𝐏¯t\mathbf{\bar{P}}\_{t} are deterministic functions. To highlight this property, from now on we will write P​(t)P(t) and 𝐏¯​(t)\mathbf{\bar{P}}(t) instead of PtP\_{t} and 𝐏¯t\mathbf{\bar{P}}\_{t}, respectively. The semimartingale representations of 𝐒\mathbf{S} with respect to the information filtration 𝔽\mathbb{F} are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​𝐒t\displaystyle\mathrm{d}\mathbf{S}\_{t} | =diag​(𝐒t)​[(𝐚​Γt+𝐛)​d​t+𝚺~𝐒​d​𝐈t𝐒],𝐒0∈ℝ+n,\displaystyle=\text{diag}\left(\mathbf{S}\_{t}\right)\left[\left(\mathbf{a}\Gamma\_{t}+\mathbf{b}\right)\mathrm{d}t+\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{I}\_{t}^{\mathbf{S}}\right],\quad\mathbf{S}\_{0}\in\mathbb{R}\_{+}^{n}, |  | (5.4) |

leading to the following representation for the carbon-penalised cushion process

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​C^t𝜽C^t𝜽=[r+𝜽t⊤​(𝐚​Γt+𝐛−𝐫n)−12​𝜽t⊤​(𝚺𝐒​𝚺𝐒⊤⊙𝐞)​𝜽t]​d​t+𝜽t⊤​𝚺~𝐒​d​𝐈t𝐒,C^0𝜽=c^0.\displaystyle\dfrac{\mathrm{d}\hat{C}\_{t}^{\bm{\theta}}}{\hat{C}\_{t}^{\bm{\theta}}}=\left[r+\bm{\theta}\_{t}^{\top}\left(\mathbf{a}\Gamma\_{t}+\mathbf{b}-\mathbf{r}\_{n}\right)-\dfrac{1}{2}\bm{\theta}^{\top}\_{t}\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}\right)\bm{\theta}\_{t}\right]\mathrm{d}t+\bm{\theta}\_{t}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{I}^{\mathbf{S}}\_{t},\quad\hat{C}\_{0}^{\bm{\theta}}=\hat{c}\_{0}. |  | (5.5) |

Since the portfolio insurer’s decisions depend on the information available at time tt, we define the set of admissible strategies 𝜽\bm{\theta} as follows.

###### Definition 5.1.

A 𝔽\mathbb{F}-admissible carbon-penalised PPI strategy 𝛉={𝛉}t∈[0,T]\bm{\theta}=\left\{\bm{\theta}\right\}\_{t\in[0,T]} is a self-financing, 𝔽\mathbb{F}-predictable process such that

* (i)

  𝔼​[∫0T|Γs|​‖𝜽s‖1+‖𝜽s‖22​d​s]<∞,\mathbb{E}\left[\int\_{0}^{T}|\Gamma\_{s}|\|\bm{\theta}\_{s}\|\_{1}+\|\bm{\theta}\_{s}\|\_{2}^{2}\mathrm{d}s\right]<\infty,
* (ii)

  supt∈[0,T]𝔼​[(C^t𝜽)d​(1−δ)​(1+α)]<∞\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}\_{t}^{\bm{\theta}})^{d\left(1-\delta\right)(1+\alpha)}\right]<\infty, for some α>0\alpha>0 and d>1d>1.

We denote the set of 𝔽\mathbb{F}-admissible strategies by 𝒜𝔽\mathcal{A}^{\mathbb{F}}.222As in the full-information case, the set of admissible strategies can also be characterised in terms of mm and 𝛑\bm{\pi}, but we omit reporting it here for brevity.

Thanks to uniqueness of the solution of the filtering equation, we can consider C^\hat{C} and Γ\Gamma as state processes and formulate the separated problem as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Maximise ​𝔼t,c,γ​[(C^T𝜽)1−δ1−δ], over all ​𝜽∈𝒜𝔽,\mbox{Maximise }\mathbb{E}^{t,c,\gamma}\left[\dfrac{(\hat{C}\_{T}^{\bm{\theta}})^{1-\delta}}{1-\delta}\right],\mbox{ over all }\bm{\theta}\in\mathcal{A}^{\mathbb{F}}, |  | (5.6) |

where 𝔼t,c,γ\mathbb{E}^{t,c,\gamma} denotes the conditional expectation given C^t=c\hat{C}\_{t}=c and Γt=γ\Gamma\_{t}=\gamma, where (c,γ)∈ℝ+×ℝ\left(c,\gamma\right)\in\mathbb{R}\_{+}\times\mathbb{R}. We define the value function by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(t,c,γ):=sup𝜽∈𝒜𝔽𝔼t,c,γ​[(C^T𝜽)1−δ1−δ].\hat{V}(t,c,\gamma):=\sup\_{\bm{\theta}\in\mathcal{A}^{\mathbb{F}}}\mathbb{E}^{t,c,\gamma}\left[\dfrac{(\hat{C}\_{T}^{\bm{\theta}})^{1-\delta}}{1-\delta}\right]. |  | (5.7) |

Also in this case, we resort to dynamic programming principle. The HJB equation is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {sup𝜽∈𝒜𝔽V^t​(t,c,γ)+ℒ𝜽​V^​(t,c,γ)=0,(t,c,γ)∈[0,T)×ℝ+×ℝ,V^​(T,c,γ)=c1−δ1−δ,(c,γ)∈ℝ+×ℝ,\begin{cases}\displaystyle\sup\_{\bm{\theta}\in\mathcal{A}^{\mathbb{F}}}\hat{V}\_{t}(t,c,\gamma)+\mathcal{L}^{\bm{\theta}}\hat{V}(t,c,\gamma)=0,&(t,c,\gamma)\in[0,T)\times\mathbb{R}\_{+}\times\mathbb{R},\\[8.0pt] \hat{V}(T,c,\gamma)=\dfrac{c^{1-\delta}}{1-\delta},&(c,\gamma)\in\mathbb{R}\_{+}\times\mathbb{R},\end{cases} |  | (5.8) |

where for any constant control 𝜽∈ℝn\bm{\theta}\in\mathbb{R}^{n}, the operator ℒ𝜽\mathcal{L}^{\bm{\theta}} is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒ𝜽​F​(t,c,γ)=\displaystyle\mathcal{L}^{\bm{\theta}}F(t,c,\gamma)= | c​[r+𝜽t⊤​(𝐚​γ+𝐛−𝐫n)−12​𝜽⊤​(𝚺𝐒​𝚺𝐒⊤⊙𝐞)​𝜽]​Fc​(t,c,γ)\displaystyle c\left[r+\bm{\theta}\_{t}^{\top}\left(\mathbf{a}\gamma+\mathbf{b}-\mathbf{r}\_{n}\right)-\dfrac{1}{2}\bm{\theta}^{\top}\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}\right)\bm{\theta}\right]F\_{c}(t,c,\gamma) |  | (5.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +c22​𝜽⊤​𝚺~𝐒​𝚺~𝐒⊤​𝜽⊤​Fc,c​(t,c,γ)+(λ​γ+β)​Fγ​(t,c,γ)\displaystyle+\frac{c^{2}}{2}\bm{\theta}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\bm{\theta}^{\top}F\_{c,c}(t,c,\gamma)+\left(\lambda\gamma+\beta\right)F\_{\gamma}(t,c,\gamma) |  | (5.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12​𝐏¯​(t)​(𝚺~𝐒​𝚺~𝐒⊤)−1​𝐏¯​(t)⊤​Fγ,γ​(t,c,γ)+c​𝜽⊤​𝐏¯​(t)⊤​Fc,γ​(t,c,γ),\displaystyle+\frac{1}{2}\mathbf{\bar{P}}(t)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\mathbf{\bar{P}}(t)^{\top}F\_{\gamma,\gamma}(t,c,\gamma)+c\bm{\theta}^{\top}\mathbf{\bar{P}}(t)^{\top}F\_{c,\gamma}(t,c,\gamma), |  | (5.11) |

for every function F​(⋅)∈𝒞1,2,2​([0,T]×ℝ+×ℝ)F\left(\cdot\right)\in\mathcal{C}^{1,2,2}\left([0,T]\times\mathbb{R}\_{+}\times\mathbb{R}\right). First, we establish the following verification result.

###### Theorem 5.2 (Verification Theorem).

Let f​(t,c,γ)∈𝒞1,2,2​([0,T]×ℝ+×ℝ)f(t,c,\gamma)\in\mathcal{C}^{1,2,2}([0,T]\times\mathbb{R}\_{+}\times\mathbb{R}) be a classical solution to the HJB equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and assume that the following conditions hold:

* (i)

  for any 𝜽∈𝒜𝔽\bm{\theta}\in\mathcal{A}^{\mathbb{F}}
  the family {f​(t∧τ,C^t∧τ,Γt∧τ), for all ​𝔽−stopping times ​τ}\{f(t\wedge\tau,\hat{C}\_{t\wedge\tau},\Gamma\_{t\wedge\tau}),\text{ for all }\mathbb{F}-\text{stopping times }\tau\} is uniformly integrable;
* (ii)

  there exists 𝜽¯⋆\bar{\bm{\theta}}^{\star} at which the supremum in equation ([5.8](https://arxiv.org/html/2511.19186v1#S5.E8 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is attained.

Then f​(t,c,γ)=V^​(t,c,γ)f(t,c,\gamma)=\hat{V}(t,c,\gamma) and if {𝛉¯⋆​(t,Γt)}t∈[0,T]∈𝒜𝔽\{\bar{\bm{\theta}}^{\star}(t,\Gamma\_{t})\}\_{t\in[0,T]}\in\mathcal{A}^{\mathbb{F}} this is an optimal Markovian control.

###### Proof.

The proof replicates the line of that of Theorem [4.2](https://arxiv.org/html/2511.19186v1#S4.Thmthm2 "Theorem 4.2 (Verification Theorem). ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

In view of the Verification Theorem, we characterise the value function as the unique classical solution
of the HJB equation. Also in this case, we resort to a guess-and-verify approach. The following result presents a candidate for the value function V^\hat{V} and the optimal control 𝜽¯⋆\bar{\bm{\theta}}^{\star} under partial information. We let 𝚯^\mathbf{\hat{\Theta}} be the same of Theorem [4.3](https://arxiv.org/html/2511.19186v1#S4.Thmthm3 "Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") and we introduce the following system od ODEs:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=\displaystyle 0= | f¯t​(t)+[(1−δ)​𝐏¯​(t)​𝚯^−1​(𝐏¯​(t))⊤+𝐏¯​(t)​(𝚺~𝐒​𝚺~𝐒⊤)−1​(𝐏¯​(t))⊤]​f¯2​(t)\displaystyle\bar{f}\_{t}(t)+\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}+\mathbf{\bar{P}}(t)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}\right]\bar{f}^{2}(t) |  | (5.12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2​[(1−δ)​𝐏¯​(t)​𝚯^−1​𝐚+λ]​f¯​(t)+(1−δ)​𝐚⊤​𝚯^−1​𝐚,\displaystyle+2\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\mathbf{a}+\lambda\right]\bar{f}(t)+\left(1-\delta\right)\mathbf{a}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a}, |  | (5.13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=\displaystyle 0= | g¯t​(t)+[(1−δ)​𝐏¯​(t)​𝚯^−1​𝐚+λ]​g¯​(t)+[(1−δ)​𝐏¯​(t)​𝚯^−1​(𝐛−𝐫n)+β]​f¯​(t)\displaystyle\bar{g}\_{t}(t)+\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\mathbf{a}+\lambda\right]\bar{g}(t)+\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)+\beta\right]\bar{f}(t) |  | (5.14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +[(1−δ)​𝐏¯​(t)​𝚯^−1​(𝐏¯​(t))⊤+𝐏¯​(t)​(𝚺~𝐒​𝚺~𝐒⊤)−1​(𝐏¯​(t))⊤]​f¯​(t)​g¯​(t)\displaystyle+\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}+\mathbf{\bar{P}}(t)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}\right]\bar{f}(t)\bar{g}(t) |  | (5.15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−δ)​𝐚⊤​𝚯^−1​(𝐛−𝐫n),\displaystyle+\left(1-\delta\right)\mathbf{a}^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right), |  | (5.16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=\displaystyle 0= | h¯t​(t)+(1−δ)​r+[(1−δ)​𝐏¯​(t)​𝚯^−1​(𝐛−𝐫n)+β]​g¯​(t)+12​𝐏¯​(t)​(𝚺~𝐒​𝚺~𝐒⊤)−1​(𝐏¯​(t))⊤​f¯​(t)\displaystyle\bar{h}\_{t}(t)+(1-\delta)r+\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)+\beta\right]\bar{g}(t)+\frac{1}{2}\mathbf{\bar{P}}(t)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}\bar{f}(t) |  | (5.17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12​[(1−δ)​𝐏¯​(t)​𝚯^−1​(𝐏¯​(t))⊤+𝐏¯​(t)​(𝚺~𝐒​𝚺~𝐒⊤)−1​(𝐏¯​(t))⊤]​g¯2​(t)\displaystyle+\dfrac{1}{2}\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}+\mathbf{\bar{P}}(t)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}\right]\bar{g}^{2}(t) |  | (5.18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1−δ2​(𝐛−𝐫n)⊤​𝚯^−1​(𝐛−𝐫n).\displaystyle+\dfrac{1-\delta}{2}\left(\mathbf{b}-\mathbf{r}\_{n}\right)^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right). |  | (5.19) |

###### Theorem 5.3.

Let f¯​(⋅),g¯​(⋅),h¯​(⋅)∈𝒞b1​([0,T])\bar{f}(\cdot),\,\bar{g}(\cdot),\,\bar{h}(\cdot)\in\mathcal{C}^{1}\_{b}([0,T]) be the unique solutions of the following system of ODEs ([5.13](https://arxiv.org/html/2511.19186v1#S5.E13 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")),([5.16](https://arxiv.org/html/2511.19186v1#S5.E16 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")),([5.19](https://arxiv.org/html/2511.19186v1#S5.E19 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")),
with terminal conditions f¯​(T)=g¯​(T)=h¯​(T)=0\bar{f}(T)=\bar{g}(T)=\bar{h}(T)=0. Then, the optimal control 𝛉¯⋆\bar{\bm{\theta}}^{\star} is given by 𝛉¯t⋆=𝛉¯⋆​(t,Γt)\bar{\bm{\theta}}^{\star}\_{t}=\bar{\bm{\theta}}^{\star}(t,\Gamma\_{t}) where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽¯⋆​(t,γ)=𝚯^−1​(𝐚​γ+𝐛−𝐫n)+𝚯^−1​𝐏¯​(t)⊤​(f¯​(t)​γ+g¯​(t)),\bar{\bm{\theta}}^{\star}(t,\gamma)=\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}\gamma+\mathbf{b}-\mathbf{r}\_{n}\right)+\mathbf{\hat{\Theta}}^{-1}\mathbf{\bar{P}}(t)^{\top}\left(\bar{f}(t)\gamma+\bar{g}(t)\right), |  | (5.20) |

and the value function satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^​(t,c,γ)=c1−δ1−δ​exp⁡{f¯​(t)2​γ2+g¯​(t)​γ+h¯​(t)}.\hat{V}(t,c,\gamma)=\dfrac{c^{1-\delta}}{1-\delta}\exp\left\{\dfrac{\bar{f}(t)}{2}\gamma^{2}+\bar{g}(t)\gamma+\bar{h}(t)\right\}. |  | (5.21) |

Moreover, let (f^​(t),g^​(t),h^​(t))(\hat{f}(t),\,\hat{g}(t),\,\hat{h}(t)) be the unique solutions on [0,T][0,T] of the systems of ODEs given by equations ([4.8](https://arxiv.org/html/2511.19186v1#S4.E8 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([4.10](https://arxiv.org/html/2511.19186v1#S4.E10 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")),([4.12](https://arxiv.org/html/2511.19186v1#S4.E12 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) with f^​(T)=g^​(T)=h^​(T)=0\hat{f}(T)=\hat{g}(T)=\hat{h}(T)=0. Then, for all t∈[0,T]t\in[0,T], 1−P​(t)​f^​(t)>01-P(t)\hat{f}(t)>0 and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f¯​(t)=\displaystyle\bar{f}(t)= | f^​(t)1−P​(t)​f^​(t),\displaystyle\dfrac{\hat{f}(t)}{1-P(t)\hat{f}(t)}, |  | (5.22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g¯​(t)=\displaystyle\bar{g}(t)= | g^​(t)1−P​(t)​f^​(t),\displaystyle\dfrac{\hat{g}(t)}{1-P(t)\hat{f}(t)}, |  | (5.23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h¯​(t)=\displaystyle\bar{h}(t)= | h^​(t)−12​log⁡(1−P​(t)​f^​(t))+12​g^2​(t)​P​(t)1−P​(t)​f^​(t)\displaystyle\hat{h}(t)-\dfrac{1}{2}\log\left(1-P(t)\hat{f}(t)\right)+\dfrac{1}{2}\dfrac{\hat{g}^{2}(t)P(t)}{1-P(t)\hat{f}(t)} |  | (5.24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −1−δ2​∫tTP​(s)1−P​(s)​f^​(s)​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]​𝚯^−1​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]⊤​ds,\displaystyle-\dfrac{1-\delta}{2}\int\_{t}^{T}\dfrac{P(s)}{1-P(s)\hat{f}(s)}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]\mathbf{\hat{\Theta}}^{-1}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]^{\top}\mathrm{d}s, |  | (5.25) |

implying that f¯​(t),g¯​(t),h¯​(t)∈𝒞b1​([0,T]).\bar{f}(t),\,\bar{g}(t),\,\bar{h}(t)\in\mathcal{C}^{1}\_{b}([0,T]).

###### Proof.

The proof is provided in Appendix [C.1](https://arxiv.org/html/2511.19186v1#A3.SS1 "C.1 Proof of Theorem 5.3 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

Note that, in view of the relationship between f^,g^,h^\hat{f},\hat{g},\hat{h} and f¯,g¯,h¯\bar{f},\bar{g},\bar{h} and the properties of the solution of the system ([4.8](https://arxiv.org/html/2511.19186v1#S4.E8 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([4.10](https://arxiv.org/html/2511.19186v1#S4.E10 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([4.12](https://arxiv.org/html/2511.19186v1#S4.E12 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we immediately get that the system ([5.19](https://arxiv.org/html/2511.19186v1#S5.E19 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([5.16](https://arxiv.org/html/2511.19186v1#S5.E16 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([5.19](https://arxiv.org/html/2511.19186v1#S5.E19 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) admits a unique solution in 𝒞b1​([0,T])\mathcal{C}\_{b}^{1}([0,T]).

As in the full information case, the candidate optimal strategy 𝜽¯⋆\bar{\bm{\theta}}^{\star} in equation ([5.20](https://arxiv.org/html/2511.19186v1#S5.E20 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is Markovian; the difference is that under partial information the common stochastic factor YY is replaced by its filtered estimate Γ\Gamma. We now provide sufficient conditions on model parameters that guarantee that condition (ii) of Theorem [5.2](https://arxiv.org/html/2511.19186v1#S5.Thmthm2 "Theorem 5.2 (Verification Theorem). ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") is satisfied and that 𝜽¯⋆\bar{\bm{\theta}}^{\star} given by equation ([5.20](https://arxiv.org/html/2511.19186v1#S5.E20 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is an admissible control, according to Definition [5.1](https://arxiv.org/html/2511.19186v1#S5.Thmthm1 "Definition 5.1. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). The following Proposition is a preliminary results.

###### Proposition 5.4.

Let f¯​(t)\bar{f}(t) be solution of the ODE in equation ([5.13](https://arxiv.org/html/2511.19186v1#S5.E13 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) on [0,T][0,T]. Then, f¯​(t)\bar{f}(t) is strictly positive and decreasing on [0,T][0,T] if δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1) and is strictly negative and increasing if δ∈𝒫∩(1,+∞)\delta\in\mathcal{P}\cap(1,+\infty).

###### Proof.

The proof is provided in Appendix [C.2](https://arxiv.org/html/2511.19186v1#A3.SS2 "C.2 Proof of Proposition 5.4 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

Next, we will use this result to show that condition (ii) of Theorem [5.2](https://arxiv.org/html/2511.19186v1#S5.Thmthm2 "Theorem 5.2 (Verification Theorem). ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") is satisfied.

###### Proposition 5.5.

Assume that one of the two following conditions holds

* (i)

  δ∈𝒫∩(1,+∞)\delta\in\mathcal{P}\cap(1,+\infty),
* (ii)

  δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1) and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 1−q​(1+α)​f^​(0)1−P​(0)​f^​(0)​max⁡{P0,Var​[YT]}>01-q(1+\alpha)\dfrac{\hat{f}(0)}{1-P(0)\hat{f}(0)}\max\left\{P\_{0},\mbox{Var}[Y\_{T}]\right\}>0 |  | (5.26) |

  for some q>1q>1.

Then, for any admissible strategy 𝛉∈𝒜𝔽\bm{\theta}\in\mathcal{A}^{\mathbb{F}}, {V^​(τ,C^τ,Yτ), for all ​𝔽​–stopping times ​τ≤T}\{\hat{V}(\tau,\hat{C}\_{\tau},Y\_{\tau}),\mbox{ for all }\mathbb{F}\mbox{--stopping times }\tau\leq T\} forms a uniformly integrable family.

###### Proof.

The proof is provided in Appendix [C.4](https://arxiv.org/html/2511.19186v1#A3.SS4 "C.4 Proof of Corollary 5.7 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

To close the loop, we provide sufficient conditions for admissibility of the optimal strategy.

###### Proposition 5.6.

Assume that one of the two following conditions holds

* (i)

  δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1) and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 1−8​d​(1−δ)​(1+α)​n​T​[(1∨d​(1−δ)​(1+α)​w)​c~12+aM2]​max⁡{P0,Var​[YT]}>0,1-8d(1-\delta)(1+\alpha)nT\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)\tilde{c}\_{1}^{2}+a\_{M}^{2}\right]\max\left\{P\_{0},\text{Var}[Y\_{T}]\right\}>0, |  | (5.27) |
* (ii)

  δ∈𝒫∩(1,+∞)\delta\in\mathcal{P}\cap(1,+\infty) and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 1−8​d​(1−δ)​(1+α)​n​T​[(−(1+w)∧d​(1−δ)​(1+α)​w~)​c~12−aM2]​max⁡{P0,Var​[YT]}>0,1-8d(1-\delta)(1+\alpha)nT\left[\left(-(1+w)\wedge d(1-\delta)(1+\alpha)\tilde{w}\right)\tilde{c}\_{1}^{2}-a\_{M}^{2}\right]\max\left\{P\_{0},\text{Var}[Y\_{T}]\right\}>0, |  | (5.28) |

  where ww and w~\tilde{w} are given by equations ([4.20](https://arxiv.org/html/2511.19186v1#S4.E20 "In item (ii) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([4.21](https://arxiv.org/html/2511.19186v1#S4.E21 "In item (ii) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) respectively, and c~1\tilde{c}\_{1} is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | c~1=maxi=1,…,n⁡|(𝚯^−1​[𝐚+𝚺~𝐒​(𝚺~𝐒−1)⊤​(𝐚​supu∈[0,T]P​(u)​f¯​(u)+𝚺~𝐒​𝚺~Y⊤​supu∈[0,T]f¯​(u))])i|\tilde{c}\_{1}=\max\_{i=1,\dots,n}\bigg|\left(\mathbf{\hat{\Theta}}^{-1}\left[\mathbf{a}+\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{-1}\right)^{\top}\left(\mathbf{a}\sup\_{u\in[0,T]}P(u)\bar{f}(u)+\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\sup\_{u\in[0,T]}\bar{f}(u)\right)\right]\right)\_{i}\bigg| |  | (5.29) |

Then the process 𝛉¯⋆\bar{\bm{\theta}}^{\star} given by equation ([5.20](https://arxiv.org/html/2511.19186v1#S5.E20 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is an admissible strategy.

###### Proof.

The proof replicates the line of that of Theorem [4.7](https://arxiv.org/html/2511.19186v1#S4.Thmthm7 "Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

Under the assumption of Proposition [5.5](https://arxiv.org/html/2511.19186v1#S5.Thmthm5 "Proposition 5.5. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), the candidate optimal strategy is admissible and V^\hat{V} in equation ([5.21](https://arxiv.org/html/2511.19186v1#S5.E21 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is the unique solution of the optimisation problem. As for the full information case, we can derive the original controls m¯⋆\bar{m}^{\star} and 𝝅¯⋆\bar{\bm{\pi}}^{\star} by applying proposition [4.8](https://arxiv.org/html/2511.19186v1#S4.Thmthm8 "Proposition 4.8. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). Adapting Example [4.1](https://arxiv.org/html/2511.19186v1#S4.Thmexample1 "Example 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") to the case of a PI insurer with partial information, the optimal multiplier becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | m¯⋆​(t,γ;ε,δ)=θ¯1⋆​(t,γ;δ)+θ¯2⋆​(t,γ;δ,ε),\displaystyle\bar{m}^{\star}(t,\gamma;\varepsilon,\delta)=\bar{\theta}\_{1}^{\star}(t,\gamma;\delta)+\bar{\theta}\_{2}^{\star}(t,\gamma;\delta,\varepsilon), |  | (5.30) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θ¯1⋆​(t,γ;δ)\displaystyle\bar{\theta}\_{1}^{\star}(t,\gamma;\delta) | =ξ1M​(t,γ;δ)+ξ~1I​(t,γ;δ)+ξ1P​(t,γ;δ),\displaystyle=\xi\_{1}^{M}(t,\gamma;\delta)+\tilde{\xi}\_{1}^{I}(t,\gamma;\delta)+\xi\_{1}^{P}(t,\gamma;\delta), |  | (5.31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θ¯2⋆​(t,γ;δ,ε)\displaystyle\bar{\theta}\_{2}^{\star}(t,\gamma;\delta,\varepsilon) | =ξ2M​(t,γ;δ,ε)+ξ~2I​(t,γ;δ,ε)+ξ2P​(t,γ;δ,ε),\displaystyle=\xi\_{2}^{M}(t,\gamma;\delta,\varepsilon)+\tilde{\xi}\_{2}^{I}(t,\gamma;\delta,\varepsilon)+\xi\_{2}^{P}(t,\gamma;\delta,\varepsilon), |  | (5.32) |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ~1I​(t,γ;δ)\displaystyle\tilde{\xi}\_{1}^{I}(t,\gamma;\delta) | =1δ​σY​ρ1,Yσ1​(f¯​(t)​γ+g¯​(t)),ξ1P​(t,γ;δ)=1δ​a1​P​(t)σ12​(f¯​(t)​γ+g¯​(t)),\displaystyle=\dfrac{1}{\delta}\dfrac{\sigma\_{Y}\rho\_{1,Y}}{\sigma\_{1}}\left(\bar{f}(t)\gamma+\bar{g}(t)\right),\quad\xi\_{1}^{P}(t,\gamma;\delta)=\dfrac{1}{\delta}\dfrac{a\_{1}P(t)}{\sigma\_{1}^{2}}\left(\bar{f}(t)\gamma+\bar{g}(t)\right), |  | (5.33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ~2I​(t,γ;δ,ε)\displaystyle\tilde{\xi}\_{2}^{I}(t,\gamma;\delta,\varepsilon) | =1ε+δ​σY​ρ2,Yσ2​(f¯​(t)​γ+g¯​(t)),ξ2P​(t,γ;δ,ε)=1ε+δ​a2​P​(t)σ22​(f¯​(t)​γ+g¯​(t)),\displaystyle=\dfrac{1}{\varepsilon+\delta}\dfrac{\sigma\_{Y}\rho\_{2,Y}}{\sigma\_{2}}\left(\bar{f}(t)\gamma+\bar{g}(t)\right),\quad\xi\_{2}^{P}(t,\gamma;\delta,\varepsilon)=\dfrac{1}{\varepsilon+\delta}\dfrac{a\_{2}P(t)}{\sigma\_{2}^{2}}\left(\bar{f}(t)\gamma+\bar{g}(t)\right), |  | (5.34) |

for every (t,γ)∈[0,T]×ℝ\left(t,\gamma\right)\in[0,T]\times\mathbb{R}. ξ1M​(t,γ;δ)\xi\_{1}^{M}(t,\gamma;\delta) and ξ2M​(t,γ;δ,ε)\xi\_{2}^{M}(t,\gamma;\delta,\varepsilon) are defined as in equations ([4.24](https://arxiv.org/html/2511.19186v1#S4.E24 "In Example 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([4.25](https://arxiv.org/html/2511.19186v1#S4.E25 "In Example 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). As shown in equation ([5.30](https://arxiv.org/html/2511.19186v1#S5.E30 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), the optimal multiplier retains the same structure obtained for the CRRA investor under complete information. However, in this case, two additional terms appear, namely ξ1P\xi^{P}\_{1} and ξ2P\xi^{P}\_{2}, which act as correction factors accounting for the uncertainty due to the non-observability of the common stochastic factor YY. As for the previous cases, all the components related to the brown stock depend on the carbon aversion parameter ε\varepsilon.

#### Logarithmic case.

For the logarithmic case the separated problem reads as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Maximise ​𝔼t,c,γ​[log⁡(C^T𝜽)], over all ​𝜽∈𝒜𝔽\mbox{Maximise }\mathbb{E}^{t,c,\gamma}\left[\log(\hat{C}\_{T}^{\bm{\theta}})\right],\mbox{ over all }\bm{\theta}\in\mathcal{A}^{\mathbb{F}} |  | (5.35) |

and the corresponding value function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~​(t,c,γ):=sup𝜽∈𝒜𝔽𝔼t,c,γ​[log⁡(C^T𝜽)].\tilde{V}(t,c,\gamma):=\sup\_{\bm{\theta}\in\mathcal{A}^{\mathbb{F}}}\mathbb{E}^{t,c,\gamma}\left[\log(\hat{C}\_{T}^{\bm{\theta}})\right]. |  | (5.36) |

The next theorem characterizes the optimal strategy and the value function V~\tilde{V}.

###### Corollary 5.7.

Consider a fund manager endowed with logarithmic utility function and a carbon aversion ε≥0\varepsilon\geq 0, then the optimal controls 𝛉¯⋆∈𝒜𝔽\bar{\bm{\theta}}^{\star}\in\mathcal{A}^{\mathbb{F}} is given by 𝛉¯t⋆=𝛉¯⋆​(t,Γt)\bar{\bm{\theta}}^{\star}\_{t}=\bar{\bm{\theta}}^{\star}(t,\Gamma\_{t}) where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽¯⋆​(t,γ)=𝚯−1​(𝐚​γ+𝐛−𝐫n).\displaystyle\bar{\bm{\theta}}^{\star}(t,\gamma)=\mathbf{\Theta}^{-1}\left(\mathbf{a}\gamma+\mathbf{b}-\mathbf{r}\_{n}\right). |  | (5.37) |

where 𝚯\mathbf{\Theta} is the same of Corollary [4.9](https://arxiv.org/html/2511.19186v1#S4.Thmthm9 "Corollary 4.9. ‣ Logarithmic case. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). The value function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~​(t,c,γ)=log⁡(c)+r​(T−t)+f​(t)2​γ2+g​(t)​γ+h~​(t),\tilde{V}(t,c,\gamma)=\log(c)+r(T-t)+\dfrac{f(t)}{2}\gamma^{2}+g(t)\gamma+\tilde{h}(t), |  | (5.38) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | h~​(t)=h​(t)+𝐚⊤​𝚯−1​𝐚2​(∫tTP​(s)​ds−P​(t)​e2​λ​(T−t)−12),\tilde{h}(t)=h(t)+\dfrac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2}\left(\int\_{t}^{T}P(s)\mathrm{d}s-P(t)\dfrac{e^{2\lambda(T-t)}-1}{2}\right), |  | (5.39) |

for every t∈[0,T]t\in[0,T], with ff, gg and hh being the same of Corollary [4.9](https://arxiv.org/html/2511.19186v1#S4.Thmthm9 "Corollary 4.9. ‣ Logarithmic case. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").

###### Proof.

The proof is provided in Appendix [C.3](https://arxiv.org/html/2511.19186v1#A3.SS3 "C.3 Proof of Proposition 5.5 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

### 5.1 Loss of utility

Since full information allows the portfolio insurer to observe the common stochastic factor directly, the fully informed portfolio insurer has an advantage over its partial-information counterpart. Therefore, as shown in Lee and Papanicolaou ([2016](https://arxiv.org/html/2511.19186v1#bib.bib19)), there is always an information premium, which is non-negative. In the present paper, we quantify this premium by computing the loss of utility L={Lt}t∈[0,T]L=\{L\_{t}\}\_{t\in[0,T]} due to partial information, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=𝔼c​[Vfull​(t,C,Yt)−Vpartial​(t,C,Γt)|ℱt],t∈[0,T].L\_{t}=\mathbb{E}^{c}\left[V^{\mathrm{full}}(t,C,Y\_{t})-V^{\mathrm{partial}}(t,C,\Gamma\_{t})|\mathcal{F}\_{t}\right],\quad t\in[0,T]. |  | (5.40) |

An alternative way to assess the informational advantage is to express the information premium in monetary terms; this is the so-called efficiency (see, e.g., Rogers ([2001](https://arxiv.org/html/2511.19186v1#bib.bib23)), Brendle ([2006](https://arxiv.org/html/2511.19186v1#bib.bib7)) and Sass et al. ([2017](https://arxiv.org/html/2511.19186v1#bib.bib26))).
Specifically, in the PPI framework, the efficiency of the partially-informed strategy relative to the full-information strategy is defined as the fraction of the initial cushion ξ\xi that a fully informed investor would need to obtain the same the expected utility of the terminal cushion achieved by a partially informed investor starting with a unitary cushion. Hence, it is found by solving the following equation for ζ\zeta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Vfull​(0,ζ,Y0)−Vpartial​(0,1,Γ0)|ℱ0]=0.\mathbb{E}\left[V^{\mathrm{full}}(0,\zeta,Y\_{0})-V^{\mathrm{partial}}(0,1,\Gamma\_{0})|\mathcal{F}\_{0}\right]=0. |  | (5.41) |

In what follows, we analytically characterise the loss of utility and the efficiency of a portfolio insurer who does not directly observe the common stochastic factor YY, for both the CRRA and log-utility cases.

###### Proposition 5.8.

The loss of utility of a partially informed portfolio insurer endowed with a CRRA utility function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=c1−δ1−δ​(e1−δ2​∫tTP​(s)1−P​(s)​f^​(s)​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]​𝚯^−1​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]⊤​ds−1)​ef¯​(t)2​Γt2+g¯​(t)​Γt+h¯​(t),L\_{t}=\frac{c^{1-\delta}}{1-\delta}\left(e^{\frac{1-\delta}{2}\int\_{t}^{T}\frac{P(s)}{1-P(s)\hat{f}(s)}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]\mathbf{\hat{\Theta}}^{-1}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]^{\top}\mathrm{d}s}-1\right)e^{\frac{\bar{f}(t)}{2}\Gamma^{2}\_{t}+\bar{g}(t)\Gamma\_{t}+\bar{h}(t)}, |  | (5.42) |

for every t∈[0,T]t\in[0,T], and the corresponding efficiency of the carbon-penalised PPI strategy is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ=exp⁡{−12​∫0TP​(s)1−P​(s)​f^​(s)​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]​𝚯^−1​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]⊤​ds}.\zeta=\exp\left\{-\frac{1}{2}\int\_{0}^{T}\frac{P(s)}{1-P(s)\hat{f}(s)}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]\mathbf{\hat{\Theta}}^{-1}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]^{\top}\mathrm{d}s\right\}. |  | (5.43) |

###### Proof.

The proof is provided in Appendix [C.5](https://arxiv.org/html/2511.19186v1#A3.SS5 "C.5 Proof of Proposition 5.8 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

###### Proposition 5.9.

The loss of utility of a partially informed portfolio insurer endowed with a logarithmic utility function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=𝐚⊤​𝚯−1​𝐚2​∫tTP​(s)​ds,L\_{t}=\frac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2}\int\_{t}^{T}P(s)\mathrm{d}s, |  | (5.44) |

for every t∈[0,T]t\in[0,T], and the efficiency of the corresponding carbon-penalised PPI strategy is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ=exp⁡{−𝐚⊤​𝚯−1​𝐚2​∫0TP​(s)​ds}.\zeta=\exp\left\{-\frac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2}\int\_{0}^{T}P(s)\mathrm{d}s\right\}. |  | (5.45) |

###### Proof.

See Appendix [C.6](https://arxiv.org/html/2511.19186v1#A3.SS6 "C.6 Proof of Corollary 5.9 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").
∎

Proposition [5.8](https://arxiv.org/html/2511.19186v1#S5.Thmthm8 "Proposition 5.8. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), and more evidently Proposition [5.9](https://arxiv.org/html/2511.19186v1#S5.Thmthm9 "Proposition 5.9. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), show that the loss of utility is strictly positive. This outcome was to be expected, since partially informed strategies constitute a subset of the fully informed ones. Consequently, a portfolio insurer with full information can always replicate, or improve upon, the performance achievable under partial information. Equivalently, the relative efficiency of the carbon-penalised strategy under partial information, vis-à-vis its full-information counterpart, is given by ζ<1\zeta<1, confirming that partial information entail a reduction in attainable utility.

## 6 Numerical experiments

In this section, we perform a simulation study to examine the behavior of the optimal carbon-penalised PPI strategy and to compare the strategies of a fully informed versus a partially informed portfolio insurer. We consider n=4n=4 traded stocks: the first two are low-carbon (green), while the remaining two are high-carbon (brown). Unless otherwise stated, model parameters are fixed as in Table [6.1](https://arxiv.org/html/2511.19186v1#S6.T1 "Table 6.1 ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). Moreover, throughout the numerical experiments, we fix the risk-free rate at r=0.01r=0.01, the PPI protection level at PL=1\mathrm{PL}=1, and the initial wealth at V0=1V\_{0}=1.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐚\mathbf{a} | 𝐛\mathbf{b} | 𝚺𝐒\mathbf{\Sigma}\_{\mathbf{S}} |
| S1S\_{1} | 0.0800.080 | −0.03-0.03 | 0.190.19 |
| S2S\_{2} | 0.0550.055 | 0.01\phantom{-}0.01 | 0.210.21 |
| S3S\_{3} | 0.0450.045 | 0.01\phantom{-}0.01 | 0.220.22 |
| S4S\_{4} | 0.0750.075 | −0.03-0.03 | 0.150.15 |
|  |  |  |  |

(a) Parameters of the stock prices.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| λ\lambda | β\beta | σY\sigma\_{Y} | Γ0\Gamma\_{0} | P0P\_{0} |
| −0.5-0.5 | 0.50.5 | 0.050.05 | 11 | 0.00250.0025 |
|  |  |  |  |  |

(b) Parameters of the common stochastic factor YY.

𝐑=(1.000.320.250.100.350.321.000.300.12−0.250.250.301.000.20−0.150.100.120.201.000.3250.35−0.25−0.150.3251)\mathbf{R}=\begin{pmatrix}1.00&\phantom{-}0.32&\phantom{-}0.25&0.10&\phantom{-}0.35\\
0.32&\phantom{-}1.00&\phantom{-}0.30&0.12&-0.25\\
0.25&\phantom{-}0.30&\phantom{-}1.00&0.20&-0.15\\
0.10&\phantom{-}0.12&\phantom{-}0.20&1.00&\phantom{-}0.325\\
0.35&-0.25&-0.15&0.325&\phantom{-}1\end{pmatrix}

(c) Correlation matrix 𝐑\mathbf{R}.

Table 6.1: General parameters for the numerical study.

To understand the relationship between the unobservable factor process YY at its filtered estimate Γ\Gamma, we compare a single trajectory of these processes in Figure [6.1](https://arxiv.org/html/2511.19186v1#S6.F1 "Figure 6.1 ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). The filter (dashed magenta line) shows less variability than the true trajectory, yet is able to capture the upward and downward trends of the factor YY (solid blue line). We recall that the goodness of the filter depends highly on the signal-to-noise ratio. In particular, if volatility of stock prices is large, the observation is noisy, the filter gets worse.

![Refer to caption](x1.png)


Figure 6.1: True trajectory of the common stochastic factor YY (solid blue line) and trajectory of its filtered estimate Γ\Gamma (dashed magenta line).

### 6.1 Numerical Experiments for the partial information case

We begin our analysis with a numerical study of the optimal exposures of the carbon-penalised PPI strategy to the traded stocks. We focus on the partial information case, which is one of the key features of our model. We denote by 𝐄¯⋆={𝐄¯t⋆}t∈[0,T]\mathbf{\bar{E}}^{\star}=\{\mathbf{\bar{E}}\_{t}^{\star}\}\_{t\in[0,T]} the exposure to the risky assets, where 𝐄¯t⋆=(E¯1,t⋆,…,E¯n,t⋆)⊤\mathbf{\bar{E}}^{\star}\_{t}=\left(\bar{E}^{\star}\_{1,t},\,\dots,\,\bar{E}^{\star}\_{n,t}\right)^{\top}, are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | E¯i,t⋆:=m¯t⋆​π¯i,t⋆​(Vtm¯⋆,𝝅¯⋆−Ft)+Vtm¯⋆,𝝅¯⋆,t∈[0,T],\bar{E}^{\star}\_{i,t}:=\bar{m}^{\star}\_{t}\bar{\pi}\_{i,t}^{\star}\frac{(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{t}-F\_{t})^{+}}{V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{t}},\quad t\in[0,T], |  | (6.1) |

for every i=1,…,ni=1,\,\dots,\,n, and for the optimal strategy under partial information (m¯⋆,𝝅¯⋆)(\bar{m}^{\star},\bar{\bm{\pi}}^{\star}) (we recall here that Vm¯⋆,𝝅¯⋆V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}} is the value of the strategy under partial information). We conduct a static analysis at t=0t=0 and a dynamic one thereafter. The histograms in Figure [6.2](https://arxiv.org/html/2511.19186v1#S6.F2 "Figure 6.2 ‣ 6.1 Numerical Experiments for the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") show the optimal exposures E¯i,0⋆\bar{E}^{\star}\_{i,0} to each traded stock at t=0t=0, for every i=1,…,ni=1,\dots,n, across different levels of the portfolio insurer’s risk aversion δ\delta and carbon aversion ε\varepsilon. Each panel corresponds to a specific combination of δ∈{0.7, 1, 3}\delta\in\{0.7,\,1,\,3\} and ε∈{0, 1}\varepsilon\in\{0,\,1\}, for a direct comparison of the effects of carbon aversion. The results show that, as carbon aversion ε\varepsilon increases, the optimal exposures to brown stocks decrease and those to green stocks increase, thereby reducing the PPI strategy’s carbon footprint.333There are several possible definitions of the carbon footprint of a portfolio or a fund. Here, we refer to the weighted sum of the carbon intensity of each asset in the risky reference portfolio. A reduction in exposure to carbon-intensive stocks appears in every configuration, but the magnitude of this reduction depends on risk aversion. In particular, when δ=3\delta=3, which corresponds to a high level of risk aversion, the percentage reduction is smaller. This is because the risky reference portfolio is conservative, hence the exposure is already low in that case. Similar results apply to the optimal PPI strategy under full information.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

Figure 6.2: Histograms displaying the optimal exposure to the ii-th stock in the risk reference portfolio X𝝅⋆X^{{\bm{\pi}}^{\star}} at t=0t=0 for different levels of δ\delta and ε\varepsilon.

Figure [6.3](https://arxiv.org/html/2511.19186v1#S6.F3 "Figure 6.3 ‣ 6.1 Numerical Experiments for the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), illustrates the optimal multiplier m¯⋆\bar{m}^{\star} (left panel) and the optimal exposure to the risk-free asset S0S\_{0} (right panel) at t=0t=0 as functions of carbon aversion ε\varepsilon, and offers a description of the same effect from a different angle.
When ε=0\varepsilon=0, the PPI strategy’s exposure to the risky assets is entirely determined by risk aversion δ\delta. In particular, relatively low levels of the risk-aversion parameter (e.g., δ=0.7\delta=0.7 and δ=1\delta=1) lead to high values of the multiplier and large exposures to 𝐒\mathbf{S}, thereby making the strategy leveraged. Conversely, a higher δ\delta implies a lower optimal multiplier m¯⋆\bar{m}^{\star} and thus a smaller exposure to 𝐒\mathbf{S}, which – under the PPI mechanism – results in a larger allocation to the risk-free asset S0S\_{0}. Similarly, as ε\varepsilon increases, m¯⋆\bar{m}^{\star} decreases, implying a lower exposure to carbon intensive stocks. This translates in a higher allocation to S0S\_{0}, in particular in cases where the risk aversion δ\delta is low.

![Refer to caption](x8.png)

![Refer to caption](x9.png)

Figure 6.3: Optimal multiplier m¯0⋆\bar{m}^{\star}\_{0} (left panel) and optimal exposure to the risk-free asset S0S\_{0} (right panel) as a function of carbon aversion ε\varepsilon. The optimal PPI strategy’s exposure to S0S\_{0} is given by 1−𝟏⊤​𝐄¯t⋆1-\mathbf{1}^{\top}\mathbf{\bar{E}}^{\star}\_{t} for every t∈[0,T]t\in[0,T].

We now turn to the dynamic analysis. To illustrate how the proposed carbon-penalised PPI strategy shapes the allocation mechanism, we simulate the optimal exposures 𝐄¯⋆\mathbf{\bar{E}}^{\star} over the entire investment horizon. The results, reported in Figure [6.4](https://arxiv.org/html/2511.19186v1#S6.F4 "Figure 6.4 ‣ 6.1 Numerical Experiments for the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), indicate that our strategy successfully manages the trade-off between stock’s risk–return and the carbon footprint. In particular, brown stock number 33 is assigned the lowest average exposure, reflecting the strategy’s sensitivity to sustainability criteria. However, the methodology is not limited to a naïve exclusion of carbon-intensive assets. Indeed, although stock number 44 is also brown, it has a similar exposure as that of the green stock number 11. This is because stock number 44 exhibits the highest Sharpe ratio (SR\mathrm{SR}). This demonstrates that the penalisation mechanism does not merely exclude high-carbon assets; rather, it adjusts allocations based on a balanced evaluation of both environmental and financial features.

![Refer to caption](x10.png)


Figure 6.4: Simulated paths of the carbon-penalised PPI strategy’s optimal exposures to 𝐒\mathbf{S}. Parameters of 𝐒\mathbf{S} and YY are reported in Table [6.1](https://arxiv.org/html/2511.19186v1#S6.T1 "Table 6.1 ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). PPI strategy parameters: δ=1\delta=1, ε=1\varepsilon=1, V0=1V\_{0}=1, PL=1\mathrm{PL}=1 and T=5T=5 years.

Table [6.3](https://arxiv.org/html/2511.19186v1#S6.T3 "Table 6.3 ‣ 6.1 Numerical Experiments for the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") shows how carbon aversion ε\varepsilon and risk aversion δ\delta shape the distribution of the terminal wealth of the optimal PPI strategy, under three scenarios: Scenario 11, where green stocks outperform brown stocks; Scenario 22, where green and brown stocks perform similarly; and Scenario 33, where green stocks underperform brown stocks.
To generate the three scenarios, we specify three different drift vectors 𝐚\mathbf{a} for the stock price process 𝐒\mathbf{S} (reported in Table [6.2](https://arxiv.org/html/2511.19186v1#S6.T2 "Table 6.2 ‣ 6.1 Numerical Experiments for the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), while keeping all other parameters fixed as in Table [6.1](https://arxiv.org/html/2511.19186v1#S6.T1 "Table 6.1 ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a1a\_{1} | a2a\_{2} | a3a\_{3} | a4a\_{4} |
| Scenario 1 | 0.0900.090 | 0.0800.080 | 0.0450.045 | 0.0450.045 |
| Scenario 2 | 0.0800.080 | 0.0550.055 | 0.0450.045 | 0.0750.075 |
| Scenario 3 | 0.0450.045 | 0.0450.045 | 0.0800.080 | 0.0900.090 |
|  |  |  |  |  |

Table 6.2: Drift vector 𝐚\mathbf{a} for the three different scenarios.

The results in Table [6.3](https://arxiv.org/html/2511.19186v1#S6.T3 "Table 6.3 ‣ 6.1 Numerical Experiments for the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") show that, comparing the cases ε=0\varepsilon=0 and ε=1\varepsilon=1, the expected value of the optimal PPI strategy remains essentially unchanged, while the variance markedly reduces, in all scenarios and level of risk aversion δ\delta. Furthermore, looking at the 55th and 9090th quantiles, an increase in ε\varepsilon raises the left tail and lowers the right tail, improving downside protection while reducing upside capture. Such a shrinkage effect is weaker in Scenario 11 where green stocks outperform brown ones, moderate in Scenario 22 where green and brown securities have similar performance, and stronger where brown stocks are more attractive than green ones.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| δ=0.7\delta=0.7 | | | | | | | | |
|  | Scenario 1 | |  | Scenario 2 | |  | Scenario 3 | |
|  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |
| 𝔼​[VTm¯⋆,𝝅¯⋆]\mathbb{E}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 1.15751.1575 | 1.15341.1534 |  | 1.12081.1208 | 1.10251.1025 |  | 1.24451.2445 | 1.12131.1213 |
| Var​[VTm¯⋆,𝝅¯⋆]\mathrm{Var}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 0.08210.0821 | 0.07900.0790 |  | 0.03470.0347 | 0.01420.0142 |  | 0.35220.3522 | 0.01770.0177 |
| q0.05​(VTm¯⋆,𝝅¯⋆)q\_{0.05}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.00841.0084 | 1.00851.0085 |  | 1.01171.0117 | 1.01391.0139 |  | 1.00761.0076 | 1.01861.0186 |
| q0.50​(VTm¯⋆,𝝅¯⋆)q\_{0.50}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.07711.0771 | 1.07731.0773 |  | 1.06921.0692 | 1.06681.0668 |  | 1.08171.0817 | 1.08451.0845 |
| q0.90​(VTm¯⋆,𝝅¯⋆)q\_{0.90}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.35381.3538 | 1.33531.3353 |  | 1.25561.2556 | 1.22081.2208 |  | 1.49601.4960 | 1.24731.2473 |
| δ=1\delta=1 | | | | | | | | |
|  | Scenario 1 | |  | Scenario 2 | |  | Scenario 3 | |
|  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |
| 𝔼​[VTm¯⋆,𝝅¯⋆]\mathbb{E}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 1.11541.1154 | 1.11351.1135 |  | 1.09491.0949 | 1.08601.0860 |  | 1.15401.1540 | 1.10161.1016 |
| Var​[VTm¯⋆,𝝅¯⋆]\mathrm{Var}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 0.01450.0145 | 0.01360.0136 |  | 0.00720.0072 | 0.00400.0040 |  | 0.04470.0447 | 0.00600.0060 |
| q0.05​(VTm¯⋆,𝝅¯⋆)q\_{0.05}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.01741.0174 | 1.01741.0174 |  | 1.02101.0210 | 1.02271.0227 |  | 1.01721.0172 | 1.02631.0263 |
| q0.50​(VTm¯⋆,𝝅¯⋆)q\_{0.50}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.08201.0820 | 1.08141.0814 |  | 1.07281.0728 | 1.06981.0698 |  | 1.09121.0912 | 1.08161.0816 |
| q0.90​(VTm¯⋆,𝝅¯⋆)q\_{0.90}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.23731.2373 | 1.22851.2285 |  | 1.18231.1823 | 1.16201.1620 |  | 1.31751.3175 | 1.18731.1873 |
| δ=3\delta=3 | | | | | | | | |
|  | Scenario 1 | |  | Scenario 2 | |  | Scenario 3 | |
|  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |  | ε=0\varepsilon=0 | ε=1\varepsilon=1 |
| 𝔼​[VTm¯⋆,𝝅¯⋆]\mathbb{E}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 1.06811.0681 | 1.06791.0679 |  | 1.06351.0635 | 1.06251.0625 |  | 1.07431.0743 | 1.06941.0694 |
| Var​[VTm¯⋆,𝝅¯⋆]\mathrm{Var}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 0.00040.0004 | 0.00040.0004 |  | 0.00030.0003 | 0.00020.0002 |  | 0.00070.0007 | 0.00040.0004 |
| q0.05​(VTm¯⋆,𝝅¯⋆)q\_{0.05}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.03941.0394 | 1.03971.0397 |  | 1.04091.0409 | 1.04151.0415 |  | 1.04031.0403 | 1.04221.0422 |
| q0.50​(VTm¯⋆,𝝅¯⋆)q\_{0.50}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.06591.0659 | 1.06561.0656 |  | 1.06191.0619 | 1.06121.0612 |  | 1.07061.0706 | 1.06661.0666 |
| q0.90​(VTm¯⋆,𝝅¯⋆)q\_{0.90}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}) | 1.09391.0939 | 1.09311.0931 |  | 1.08431.0843 | 1.08161.0816 |  | 1.10681.1068 | 1.09351.0935 |
|  |  |  |  |  |  |  |  |  |

Table 6.3: Mean, variance, and 55th/5050th/9090th quantiles of the distribution of the optimal carbon-penalised PPI strategy at T=5T=5 in the partial information case, for risk-aversion levels δ=0.7\delta=0.7 (top panel), δ=1\delta=1 (middle panel), and δ=3\delta=3 (bottom panel), comparing ε=0\varepsilon=0 and ε=1\varepsilon=1, under the three scenarios.

As an example, at δ=0.7\delta=0.7, the variance decreases by 5.55.5% in Scenario 11, 58.158.1% in Scenario 22 and 94.794.7% in Scenario 33, while the interquartile range ([q0.05,q0.90][q\_{0.05},q\_{0.90}]) is reduced by 6.36.3%, 18.618.6% and 53.853.8%, respectively. Similar considerations apply to δ=1\delta=1 and δ=3\delta=3, albeit with smaller numbers.

Figure [6.3](https://arxiv.org/html/2511.19186v1#S6.F3 "Figure 6.3 ‣ 6.1 Numerical Experiments for the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") reports the optimal multiplier (left panel) and the corresponding exposure to the risk free asset (right panel) as functions of ε\varepsilon for different values of δ\delta. These plots consent us to draw the following conclusions. The multiplier is decreasing in the carbon aversion ε\varepsilon and in risk aversion δ\delta. On the contrary the exposure to the risk free asset is increasing. The effect of an increase in carbon aversion is more contained when portfolio insurer is more risk averse. In summary, δ\delta produces a generalized reduction in the riskiness of the strategy as it indiscriminately decreases the investments in green and brown stocks. In contrast, carbon aversion acts in a targeted manner on carbon-intensive stocks, providing a balanced trade-off between the carbon footprint and the overall riskiness of the PPI strategy. Importantly, these conclusions are not restricted to PPI strategies under partial information; they apply in a similar way to the full-information setting.

### 6.2 Comparison results between the full and the partial information case

In this final section, we compare the performance of the optimal strategies under full and partial information. Figure [6.5](https://arxiv.org/html/2511.19186v1#S6.F5 "Figure 6.5 ‣ 6.2 Comparison results between the full and the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") displays the optimal multiplier in full (solid blue line) and partial information (dashed magenta line).
In the left panel, we plot the standard, non-penalised case ε=0\varepsilon=0, and in the right panel, the penalised case ε=1\varepsilon=1. Both panels show that the multiplier under partial information shows slightly less variability, yet displaying very similar behaviour. The performance of the strategy under full and partial information, in terms of portfolio values are also very close as indicated in Table [6.4](https://arxiv.org/html/2511.19186v1#S6.T4 "Table 6.4 ‣ 6.2 Comparison results between the full and the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). This is a signal that, if markets are affected by random factors that are not easily measured, it is worth performing the portfolio analysis under partial information, rather than assuming a naive point of view and taking parameters constant.444We are ignoring here model misspecifications, which represent an additional source of error.

![Refer to caption](x11.png)

![Refer to caption](x12.png)

Figure 6.5: Trajectories of the optimal multiplier under full and partial information for risk-aversion level δ=1\delta=1 and carbon penalisation levels ε=0\varepsilon=0 (left panel) and ε=1\varepsilon=1 (right panel). The solid blue line corresponds to the partially informed case, while the dashed magenta line corresponds to the full-information case.



|  |  |  |  |
| --- | --- | --- | --- |
|  | Full information |  | Partial information |
| 𝔼​[VTm¯⋆,𝝅¯⋆]\mathbb{E}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 1.12071.1207 |  | 1.12131.1213 |
| Var​[VTm¯⋆,𝝅¯⋆]\mathrm{Var}[V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}}\_{T}] | 0.01660.0166 |  | 0.01770.0177 |
| q0.05​(Vm¯⋆,𝝅¯T⋆)q\_{0.05}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}\_{T}}) | 1.01821.0182 |  | 1.01861.0186 |
| q0.50​(Vm¯⋆,𝝅¯T⋆)q\_{0.50}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}\_{T}}) | 1.08501.0850 |  | 1.08451.0845 |
| q0.90​(Vm¯⋆,𝝅¯T⋆)q\_{0.90}(V^{\bar{m}^{\star},\bar{\bm{\pi}}^{\star}\_{T}}) | 1.25081.2508 |  | 1.24731.2473 |
|  |  |  |  |

Table 6.4: Mean, variance, and 55th/5050th/9090th quantiles of the distribution of the optimal carbon-penalised PPI strategy at T=5T=5 in the full and partial information case, for risk-aversion level δ=0.7\delta=0.7 and ε=1\varepsilon=1, under Scenario 33.

We conclude with an analysis of the loss of utility and efficiency. Figure [6.6](https://arxiv.org/html/2511.19186v1#S6.F6 "Figure 6.6 ‣ 6.2 Comparison results between the full and the partial information case ‣ 6 Numerical experiments ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information") reports the loss of utility at time t=0t=0 (left panel) and the efficiency (right panel) as functions of the carbon-aversion parameter ε\varepsilon, for different levels of risk aversion δ\delta. The results indicate that the loss of utility decreases with both risk aversion and carbon aversion. Interestingly, the effect is more pronounced for small values of ε\varepsilon, and becomes essentially constant for larger ε\varepsilon. The opposite monotonic behavior is observed for efficiency, although the sensitivity remains greater at lower levels of ε\varepsilon. Overall, these plots suggest that carbon penalisation can improve the relative performance of the partially informed investor compared with the fully informed one, narrowing the gap between their utilities. Under high levels of risk aversion, the loss of utility becomes practically negligible, indicating that the informational advantage of the fully informed investor is largely offset by investor preferences, as both types of investors behave in an extremely prudent manner.
Finally, the presence of even a modest carbon penalisation increases the relative efficiency of the partially informed strategy vis-à-vis its fully informed counterpart.

![Refer to caption](x13.png)

![Refer to caption](x14.png)

Figure 6.6: Loss of utility (left panel) and efficiency (right panel) of a partially informed, carbon-penalised PPI insurer relative to a full-information one, with initial cushion equal to 11, as a function of ε\varepsilon at t=0t=0 for different values of δ\delta.

## 7 Concluding remarks

This paper has proposed an optimal design of carbon-penalised proportional portfolio insurance (PPI) strategies in a market driven by an unobservable factor. By embedding carbon aversion into the investor’s utility function, we have shown that sustainability considerations can be consistently integrated into dynamic portfolio insurance without compromising its risk-mitigation role. The introduction of a carbon penalisation term naturally reduces exposure to carbon-intensive assets, leading to a lower overall carbon footprint. Importantly, this reduction does not stem from an ex-ante exclusion of “brown” stocks, but from an endogenous adjustment of the optimal allocation that balances environmental impact and financial performance.

From an economic perspective, the carbon penalty operates as an implicit cost of holding high-emission assets, inducing portfolio insurers to internalise the externalities associated with carbon risk. Our numerical results indicate that even moderate levels of carbon aversion can achieve substantial emission reductions with only marginal losses in expected utility.
Nevertheless, assets with high carbon intensity are not completely excluded; instead, a trade-off emerges between performance characteristics, e.g, a high Sharpe ratio, and carbon intensity. Consequently, a portfolio insurer considers both aspects simultaneously when designing the PPI strategy, balancing return potential against environmental impact.
Interestingly, we get that carbon penalisation improves the relative efficiency of the partially informed investor, narrowing the performance gap vis-à-vis the fully informed benchmark. When risk aversion is high, the informational premium virtually vanishes, suggesting that prudence can offset informational disadvantages.

Overall, these findings highlight that environmental preferences and informational constraints interact in shaping sustainable investment behavior. Carbon penalisation acts as a powerful mechanism to align portfolio insurance objectives with broader climate-finance goals, while partial information amplifies the conservative nature of the PPI framework.

Future research could extend this analysis in several directions. First, one may consider non-Gaussian or regime-switching latent factors to capture abrupt transitions in macro-financial or climate conditions. Second, incorporating transaction costs or market frictions would enhance the practical relevance of the model, especially for long-horizon institutional investors. Further developments might also explore multi-factor carbon risks or stochastic floors to assess how policy uncertainty and adaptive guarantees affect sustainable portfolio insurance design.

## Acknowledgements and fundings

The work of Katia Colaneri has been partially funded by the European Union - Next Generation EU - Project PRIN 2022 [2022BEMMLZ - CUP E53D23005660006] with the title Stochastic control and games and the role of information. Katia Colaneri is member of Gruppo Nazionale per l’Analisi Matematica, la Probabilità e le loro Applicazioni (GNAMPA) of Istituto
Nazionale di Alta Matematica (INdAM). The work of Daniele Mancinelli has been funded by European Union - Next Generation EU, Mission 4, Component 2 as part of the GRINS project - Growing Resilient, INclusive and Sustainable (PE0000018, CUP: E83C22004690001) - National Recovery and Resilience Plan (PNRR). The views and opinions expressed are solely those of the authors and do not necessarily reflect those of the European Union, nor can the European Union be held responsible for them.

## Declaration of generative AI in scientific writing

During the preparation of this work the authors used Writefull AcademicGPT 2025 in the writing process in order to improve the readability and language of the manuscript. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.

## Conflict of interest

The authors declare no competing interests.

## Appendix

## Appendix A Proofs of some technical results of Section [4](https://arxiv.org/html/2511.19186v1#S4 "4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

### A.1 Proof of Theorem [4.2](https://arxiv.org/html/2511.19186v1#S4.Thmthm2 "Theorem 4.2 (Verification Theorem). ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

From Itô’s formula applied to f​(t,C^t𝜽,Yt)f(t,\hat{C}^{\bm{\theta}}\_{t},Y\_{t}) we get that, for any 0≤t≤T0\leq t\leq T and 𝜽∈𝒜\bm{\theta}\in\mathcal{A}, it holds

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(T,C^T𝜽,YT)=\displaystyle f(T,\hat{C}^{\bm{\theta}}\_{T},Y\_{T})= | f​(t,c,y)+∫tT(fs​(s,C^s𝜽,Ys)+ℒ𝜽​f​(s,C^s𝜽,Ys))​ds+∫tTfy​(s,C^s𝜽,Ys)​σ~Y​ZsY\displaystyle f(t,c,y)+\int\_{t}^{T}\left(f\_{s}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})+\mathcal{L}^{\bm{\theta}}f(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\right)\mathrm{d}s+\int\_{t}^{T}f\_{y}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\tilde{\sigma}\_{Y}Z\_{s}^{Y} |  | (A1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫tT(fc^​(s,C^s𝜽,Ys)​C^s𝜽​𝜽s⊤​𝚺~𝐒+fy​(s,C^s𝜽,Ys)​𝚺~Y)​d𝐙s𝐒.\displaystyle+\int\_{t}^{T}\left(f\_{\hat{c}}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\hat{C}^{\bm{\theta}}\_{s}\bm{\theta}\_{s}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}+f\_{y}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\mathbf{\tilde{\Sigma}}\_{Y}\right)\mathrm{d}\mathbf{Z}\_{s}^{\mathbf{S}}. |  | (A2) |

Let M={Mt}t∈[0,T]M=\left\{M\_{t}\right\}\_{t\in[0,T]} be the stochastic process given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mt=∫0tfy​(s,C^s𝜽,Ys)​σ~Y​ZsY+∫0t(fc^​(s,C^s𝜽,Ys)​C^s𝜽​𝜽s⊤​𝚺~𝐒+fy​(s,C^s𝜽,Ys)​𝚺~Y)​d𝐙s𝐒,t∈[0,T],M\_{t}=\int\_{0}^{t}f\_{y}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\tilde{\sigma}\_{Y}Z\_{s}^{Y}+\int\_{0}^{t}\left(f\_{\hat{c}}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\hat{C}^{\bm{\theta}}\_{s}\bm{\theta}\_{s}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}+f\_{y}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\mathbf{\tilde{\Sigma}}\_{Y}\right)\mathrm{d}\mathbf{Z}\_{s}^{\mathbf{S}},\quad t\in[0,T], |  | (A3) |

and define τn=inf{t≥0:C^tθ≥n​ and ​|Yt|≤n}\tau\_{n}=\inf\{t\geq 0:\hat{C}^{\theta}\_{t}\geq n\text{ and }|Y\_{t}|\leq n\}. This is an increasing sequence of stopping times such that τn∧T↑T\tau\_{n}\wedge T\uparrow T for n→∞n\to\infty.
Moreover, by assumption, ff is a classical solution of the HJB equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), hence its derivatives are continuous and bounded on compact sets. This implies that the stopped process {Mt∧τn}t∈[0,T]\{M\_{t\wedge\tau\_{n}}\}\_{t\in[0,T]} is a martingale. Indeed, it holds that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​[∫0T∧τnfy2​(s,C^s𝜽,Ys)​ds+∫0T∧τnfc^2​(s,C^s𝜽,Ys)​(C^s𝜽)2​𝜽s⊤​𝚺~𝐒​𝚺~𝐒⊤​𝜽s​ds]\displaystyle\mathbb{E}\left[\int\_{0}^{T\wedge\tau\_{n}}f^{2}\_{y}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\mathrm{d}s+\int\_{0}^{T\wedge\tau\_{n}}f^{2}\_{\hat{c}}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})(\hat{C}\_{s}^{\bm{\theta}})^{2}\bm{\theta}\_{s}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\bm{\theta}\_{s}\mathrm{d}s\right] |  | (A4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤supt≤T,(c,y)∈[−n,n]2|fy2​(t,C^t𝜽,Yt)|​T+k​|fc2​(t,C^t𝜽,Yt)|​n2​𝔼​[∫0T‖𝜽s‖22​ds]<∞.\displaystyle\leq\sup\_{t\leq T,(c,y)\in[-n,n]^{2}}|f^{2}\_{y}(t,\hat{C}^{\bm{\theta}}\_{t},Y\_{t})|T+k|f^{2}\_{c}(t,\hat{C}^{\bm{\theta}}\_{t},Y\_{t})|n^{2}\mathbb{E}\left[\int\_{0}^{T}\|\bm{\theta}\_{s}\|^{2}\_{2}\mathrm{d}s\right]<\infty. |  | (A5) |

Now, since ff solves equation ([4.3](https://arxiv.org/html/2511.19186v1#S4.E3 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we get that for every n∈ℕn\in\mathbb{N}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(T∧τn,C^T∧τn,YT∧τn)≤\displaystyle f(T\wedge\tau\_{n},\hat{C}\_{T\wedge\tau\_{n}},Y\_{T\wedge\tau\_{n}})\leq | f​(t∧τn,C^t∧τn,Yt∧τn)+∫t∧τnT∧τnfy​(s,C^s𝜽,Ys)​σ~Y​ZsY\displaystyle f(t\wedge\tau\_{n},\hat{C}\_{t\wedge\tau\_{n}},Y\_{t\wedge\tau\_{n}})+\int\_{t\wedge\tau\_{n}}^{T\wedge\tau\_{n}}f\_{y}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\tilde{\sigma}\_{Y}Z\_{s}^{Y} |  | (A6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫t∧τnT∧τn(fc^​(s,C^s𝜽,Ys)​C^s​𝜽s⊤​𝚺~𝐒+fy​(s,C^s𝜽,Ys)​𝚺~Y)​d𝐙s𝐒,\displaystyle+\int\_{t\wedge\tau\_{n}}^{T\wedge\tau\_{n}}\left(f\_{\hat{c}}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\hat{C}\_{s}\bm{\theta}\_{s}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}+f\_{y}(s,\hat{C}^{\bm{\theta}}\_{s},Y\_{s})\mathbf{\tilde{\Sigma}}\_{Y}\right)\mathrm{d}\mathbf{Z}\_{s}^{\mathbf{S}}, |  | (A7) |

for every 𝜽∈𝒜\bm{\theta}\in\mathcal{A}. Thus, taking the conditional expectation on both sides of inequality ([A7](https://arxiv.org/html/2511.19186v1#A1.E7 "In A.1 Proof of Theorem 4.2 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) between t∧τnt\wedge\tau\_{n} and T∧τnT\wedge\tau\_{n}, leads to 𝔼​[f​(T∧τn,C^T∧τn𝜽,YT∧τn)]≤𝔼​[f​(t∧τn,C^t∧τn𝜽,Yt∧τn)]\mathbb{E}[f(T\wedge\tau\_{n},\hat{C}^{\bm{\theta}}\_{T\wedge\tau\_{n}},Y\_{T\wedge\tau\_{n}})]\leq\mathbb{E}\left[f(t\wedge\tau\_{n},\hat{C}^{\bm{\theta}}\_{t\wedge\tau\_{n}},Y\_{t\wedge\tau\_{n}})\right].
Next we take the limit for n→∞n\to\infty, and thanks to condition (i)(i) of the theorem ([4.3](https://arxiv.org/html/2511.19186v1#S4.E3 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,c,y​[11−δ​(C^T𝜽)1−δ]≤f​(t,c,y),\mathbb{E}^{t,c,y}\left[\dfrac{1}{1-\delta}\left(\hat{C}^{\bm{\theta}}\_{T}\right)^{1-\delta}\right]\leq f(t,c,y), |  | (A8) |

hence v^​(t,c,y)≤f​(t,c,y)\hat{v}(t,c,y)\leq f(t,c,y).
Similar computations prove that equality holds in ([A8](https://arxiv.org/html/2511.19186v1#A1.E8 "In A.1 Proof of Theorem 4.2 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) when taking the control {𝜽⋆​(t,Yt)}t∈[0,T]∈𝒜\{\bm{\theta}^{\star}(t,Y\_{t})\}\_{t\in[0,T]}\in\mathcal{A}. Consequently, v^​(t,c,y)=𝔼t,c,y​[11−δ​(C^T𝜽⋆)1−δ]=f​(t,c,y)\hat{v}(t,c,y)=\mathbb{E}^{t,c,y}\left[\frac{1}{1-\delta}(\hat{C}^{\bm{\theta}^{\star}}\_{T})^{1-\delta}\right]=f(t,c,y). This concludes the proof.

### A.2 Proof of Theorem [4.3](https://arxiv.org/html/2511.19186v1#S4.Thmthm3 "Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

Assume that a classical solution ff of the Hamilton Jacobi Bellman equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t,c,y)=c1−δ1−δ​φ^​(t,y),f(t,c,y)=\dfrac{c^{1-\delta}}{1-\delta}\hat{\varphi}(t,y), |  | (A9) |

where φ^​(t,y)\hat{\varphi}(t,y) does not depend on cc and is a positive function. Then, equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | {φ^t​(t,y)1−δ+r​φ^​(t,y)+(λ​y+β)1−δ​φ^y​(t,y)+12​σY21−δ​φ^y,y​(t,y)+max𝜽∈ℝn⁡Ψ𝜽​(t,y)=0,(t,y)∈[0,T)×ℝ,φ^​(T,y)=1,y∈ℝ,\begin{cases}\dfrac{\hat{\varphi}\_{t}(t,y)}{1-\delta}+r\hat{\varphi}(t,y)+\dfrac{\left(\lambda y+\beta\right)}{1-\delta}\hat{\varphi}\_{y}(t,y)+\dfrac{1}{2}\dfrac{\sigma\_{Y}^{2}}{1-\delta}\hat{\varphi}\_{y,y}(t,y)+\displaystyle\max\_{\bm{\theta}\in\mathbb{R}^{n}}\Psi^{\bm{\theta}}(t,y)=0,&(t,y)\in[0,T)\times\mathbb{R},\\ \hat{\varphi}(T,y)=1,&y\in\mathbb{R},\end{cases} |  | (A10) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ𝜽​(t,y):=𝜽⊤​(𝐚​y+𝐛−𝒓n)​φ^​(t,y)−12​𝜽⊤​𝚯^​𝜽​φ^​(t,y)+𝜽⊤​𝚺~𝐒​𝚺~Y⊤​φ^y​(t,y),(t,y)∈[0,T]×ℝ,\Psi^{\bm{\theta}}(t,y):=\bm{\theta}^{\top}\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right)\hat{\varphi}(t,y)-\dfrac{1}{2}\bm{\theta}^{\top}\bm{\hat{\Theta}}\bm{\theta}\hat{\varphi}(t,y)+\bm{\theta}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}\hat{\varphi}\_{y}(t,y),\quad(t,y)\in[0,T]\times\mathbb{R}, |  | (A11) |

with 𝚯^=(𝚺𝐒​𝚺𝐒⊤⊙𝐞)+δ​𝚺~𝐒​𝚺~𝐒⊤\mathbf{\hat{\Theta}}=\left(\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}\right)+\delta\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}. We let 𝜽⋆=arg​max⁡Ψ𝜽​(t,y)\bm{\theta}^{\star}=\operatorname\*{arg\,max}\Psi^{\bm{\theta}}(t,y). Taking the gradient and the Hessian of Ψ𝜽\Psi^{\bm{\theta}} with respect to 𝜽\bm{\theta}, we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇θΨ𝜽​(t,y)\displaystyle\nabla\_{\theta}\Psi^{\bm{\theta}}(t,y) | =(𝐚​y+𝐛−𝒓n)​φ^​(t,y)−𝚯^​𝜽​φ^​(t,y)+𝚺~𝐒​𝚺~Y⊤​φ^y​(t,y),\displaystyle=\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right)\hat{\varphi}(t,y)-\bm{\hat{\Theta}}\bm{\theta}\hat{\varphi}(t,y)+\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}\hat{\varphi}\_{y}(t,y), |  | (A12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hess𝜽​Ψ𝜽​(t,y)\displaystyle\text{Hess}\_{\bm{\theta}}\Psi^{\bm{\theta}}(t,y) | =−𝚯^​φ^​(t,y).\displaystyle=-\bm{\hat{\Theta}}\hat{\varphi}(t,y). |  | (A13) |

Then, setting ∇𝜽Ψ𝜽​(t,y)=𝟎\nabla\_{\bm{\theta}}\Psi^{\bm{\theta}}(t,y)=\mathbf{0}, provides the candidate optimal strategy 𝜽⋆​(t,y)\bm{\theta}^{\star}(t,y) given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽⋆​(t,y)=𝚯^−1​(𝐚​y+𝐛−𝒓n)+𝚯^−1​𝚺~𝐒​𝚺~Y⊤​φ^y​(t,y)φ^​(t,y).\bm{\theta}^{\star}(t,y)=\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right)+\mathbf{\hat{\Theta}}^{-1}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top}\dfrac{\hat{\varphi}\_{y}(t,y)}{\hat{\varphi}(t,y)}. |  | (A14) |

Moreover, since Hess𝜽​Ψ𝜽​(t,y)\text{Hess}\_{\bm{\theta}}\Psi^{\bm{\theta}}(t,y) is negative definite for every 𝜽∈ℝn\bm{\theta}\in\mathbb{R}^{n}, this ensure that 𝜽⋆​(t,y)\bm{\theta}^{\star}(t,y) is the well defined global maximiser. Next, we insert the optimal strategy in the HJB equation, yielding to the following PDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=\displaystyle 0= | φ^t​(t,y)+(1−δ)​r​φ^​(t,y)+1−δ2​φ^​(t,y)​(𝐚​y+𝐛−𝒓n)⊤​𝚯^−1​(𝐚​y+𝐛−𝒓n)\displaystyle\hat{\varphi}\_{t}(t,y)+\left(1-\delta\right)r\hat{\varphi}(t,y)+\dfrac{1-\delta}{2}\hat{\varphi}(t,y)\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right)^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right) |  | (A15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−δ)​φ^y​(t,y)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​(𝐚​y+𝐛−𝒓n)+1−δ2​(φ^y​(t,y))2φ^​(t,y)​𝚺~Y​𝚺~𝐒⊤​𝚯^−1​𝚺~𝐒​𝚺~Y⊤\displaystyle+\left(1-\delta\right)\hat{\varphi}\_{y}(t,y)\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}y+\mathbf{b}-\bm{r}\_{n}\right)+\dfrac{1-\delta}{2}\dfrac{\left(\hat{\varphi}\_{y}(t,y)\right)^{2}}{\hat{\varphi}(t,y)}\mathbf{\tilde{\Sigma}}\_{Y}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{Y}^{\top} |  | (A16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(λ​y+β)​φ^y​(t,y)+12​σY2​φ^y,y​(t,y),(t,y)∈[0,T)×ℝ,\displaystyle+\left(\lambda y+\beta\right)\hat{\varphi}\_{y}(t,y)+\dfrac{1}{2}\sigma\_{Y}^{2}\hat{\varphi}\_{y,y}(t,y),\quad(t,y)\in[0,T)\times\mathbb{R}, |  | (A17) |

with terminal condition φ​(T,y)=1\varphi(T,y)=1, for every y∈ℝy\in\mathbb{R}. We conjecture that φ^​(t,y)\hat{\varphi}(t,y) has an exponential affine form, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ^​(t,y)=exp⁡{f^​(t)2​y2+g^​(t)​y+h^​(t)},\hat{\varphi}(t,y)=\exp\left\{\frac{\hat{f}(t)}{2}y^{2}+\hat{g}(t)y+\hat{h}(t)\right\}, |  | (A18) |

with f^​(T)=g^​(T)=h^​(T)=0\hat{f}(T)=\hat{g}(T)=\hat{h}(T)=0. Clearly, the terminal value of the function in ([A18](https://arxiv.org/html/2511.19186v1#A1.E18 "In A.2 Proof of Theorem 4.3 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) satisfies the terminal condition in ([A17](https://arxiv.org/html/2511.19186v1#A1.E17 "In A.2 Proof of Theorem 4.3 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and φ^​(t,y)>0\hat{\varphi}(t,y)>0, for every (t,y)∈[0,T]×ℝ(t,y)\in[0,T]\times\mathbb{R}. Substituting this ansatz in
equation ([A17](https://arxiv.org/html/2511.19186v1#A1.E17 "In A.2 Proof of Theorem 4.3 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) results in a quadratic equation for yy. Setting the coefficients of the terms y2y^{2}, yy and the independent term to zero yields that the functions f^\hat{f}, g^\hat{g} and h^\hat{h} solve the system of ODEs in equations ([4.8](https://arxiv.org/html/2511.19186v1#S4.E8 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([4.10](https://arxiv.org/html/2511.19186v1#S4.E10 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([4.12](https://arxiv.org/html/2511.19186v1#S4.E12 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). If f^\hat{f}, g^\hat{g} and h^\hat{h} belong to the class 𝒞b1​([0,T])\mathcal{C}^{1}\_{b}([0,T]), then ff in equation ([A9](https://arxiv.org/html/2511.19186v1#A1.E9 "In A.2 Proof of Theorem 4.3 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is also regular and solves the HJB equation ([4.4](https://arxiv.org/html/2511.19186v1#S4.E4 "In 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). Finally, by substituting equation ([A18](https://arxiv.org/html/2511.19186v1#A1.E18 "In A.2 Proof of Theorem 4.3 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) in ([A14](https://arxiv.org/html/2511.19186v1#A1.E14 "In A.2 Proof of Theorem 4.3 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we obtain the candidate for the optimal control in equation ([4.13](https://arxiv.org/html/2511.19186v1#S4.E13 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). This concludes the proof.

### A.3 Proof of Proposition [4.6](https://arxiv.org/html/2511.19186v1#S4.Thmthm6 "Proposition 4.6. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

We will show that supt∈[0,T]𝔼​[v^1+α​(t,C^t,Yt)]<∞\sup\_{t\in[0,T]}\mathbb{E}\left[\hat{v}^{1+\alpha}(t,\hat{C}\_{t},Y\_{t})\right]<\infty, for some α>0\alpha>0. Using the form of the function vv (cfr. equation ([4.14](https://arxiv.org/html/2511.19186v1#S4.E14 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"))) we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supt∈[0,T]𝔼​[v^1+α​(t,C^t𝜽,Yt)]=\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[\hat{v}^{1+\alpha}(t,\hat{C}\_{t}^{\bm{\theta}},Y\_{t})\right]= | supt∈[0,T]𝔼​[11−δ​(C^t𝜽)(1−δ)​(1+α)​e(1+α)​f^​(t)2​Yt2+(1+α)​g^​(t)​Yt+(1+α)​h^​(t)]\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[\dfrac{1}{1-\delta}(\hat{C}^{\bm{\theta}}\_{t})^{(1-\delta)(1+\alpha)}e^{\frac{(1+\alpha)\hat{f}(t)}{2}Y\_{t}^{2}+(1+\alpha)\hat{g}(t)Y\_{t}+(1+\alpha)\hat{h}(t)}\right] |  | (A19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | κ​supt∈[0,T]𝔼​[(C^t𝜽)(1−δ)​(1+α)​e(1+α)​f^​(t)2​Yt2+(1+α)​g^​(t)​Yt]\displaystyle\kappa\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}^{\bm{\theta}}\_{t})^{(1-\delta)(1+\alpha)}e^{\frac{(1+\alpha)\hat{f}(t)}{2}Y\_{t}^{2}+(1+\alpha)\hat{g}(t)Y\_{t}}\right] |  | (A20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | κ​(supt∈[0,T]𝔼​[(C^t𝜽)d​(1−δ)​(1+α)]1d)​(supt∈[0,T]𝔼​[eq​(1+α)​f^​(t)2​Yt2+q​(1+α)​g^​(t)​Yt]1q),\displaystyle\kappa\left(\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}^{\bm{\theta}}\_{t})^{d(1-\delta)(1+\alpha)}\right]^{\frac{1}{d}}\right)\left(\sup\_{t\in[0,T]}\mathbb{E}\left[e^{\frac{q(1+\alpha)\hat{f}(t)}{2}Y\_{t}^{2}+q(1+\alpha)\hat{g}(t)Y\_{t}}\right]^{\frac{1}{q}}\right), |  | (A21) |

for some positive constant κ\kappa and some d,q>1d,q>1, where in the first inequality we have used that h^​(⋅)∈𝒞b1​([0,T])\hat{h}(\cdot)\in\mathcal{C}^{1}\_{b}([0,T]), and in the second comes from applying Hölder’s inequality. The first expectation is finite because of admissibility of the strategy (see the second condition of Definition [4.1](https://arxiv.org/html/2511.19186v1#S4.Thmthm1 "Definition 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). The second expectation is finite because the process YtY\_{t} is Gaussian. Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[eq​(1+α)​f^​(t)2​Yt2+q​(1+α)​g^​(t)​Yt]<∞,\mathbb{E}\left[e^{\frac{q(1+\alpha)\hat{f}(t)}{2}Y\_{t}^{2}+q(1+\alpha)\hat{g}(t)Y\_{t}}\right]<\infty, |  |

for every t∈[0,T]t\in[0,T] if and only if 1−q​(1+α)​f^​(t)​Var​[Yt]>01-q(1+\alpha)\hat{f}(t)\mbox{Var}[Y\_{t}]>0, where Var​[Yt]=P0​e2​λ​t+V∞​(1−e2​λ​t)\mbox{Var}[Y\_{t}]=P\_{0}e^{2\lambda t}+V\_{\infty}(1-e^{2\lambda t}), with V∞=−σY/2​λV\_{\infty}=-\sigma\_{Y}/2\lambda. To show that 1−q​(1+α)​f^​(t)​Var​[Yt]>01-q(1+\alpha)\hat{f}(t)\mbox{Var}[Y\_{t}]>0 for every t∈[0,T]t\in[0,T], we need to distinguish between two cases. If δ∈𝒫∩(1,+∞)\delta\in\mathcal{P}\cap(1,+\infty), f^​(t)\hat{f}(t) is strictly negative and increasing for every t∈[0,T]t\in[0,T], guaranteeing that 1−q​(1+α)​f^​(t)​Var​[Yt]>01-q(1+\alpha)\hat{f}(t)\mbox{Var}[Y\_{t}]>0. If δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1), f^​(t)\hat{f}(t) is positive and decreasing in [0,T][0,T], implying that f^​(t)<f^​(0)\hat{f}(t)<\hat{f}(0) for every t∈[0,T]t\in[0,T]. If P0>V∞P\_{0}>V\_{\infty} (respectively, P0≤V∞P\_{0}\leq V\_{\infty}), Var​(Yt)\mbox{Var}(Y\_{t}) is decreasing (respectively, increasing) meaning that P0≤Var​[Yt]≤Var​[YT]P\_{0}\leq\mbox{Var}[Y\_{t}]\leq\mbox{Var}[Y\_{T}] (respectively, Var​[YT]≤Var​[Yt]<P0\mbox{Var}[Y\_{T}]\leq\mbox{Var}[Y\_{t}]<P\_{0}). This means that f^​(t)​Var​[Yt]<f^​(0)​max⁡{P0,Var​[YT]}\hat{f}(t)\mbox{Var}[Y\_{t}]<\hat{f}(0)\max\left\{P\_{0},\mbox{Var}[Y\_{T}]\right\}, or equivalently, 1−q​(1+α)​f^​(t)​Var​[Yt]>1−q​(1+α)​f^​(0)​max⁡{P0,Var​[YT]}1-q(1+\alpha)\hat{f}(t)\mbox{Var}[Y\_{t}]>1-q(1+\alpha)\hat{f}(0)\max\left\{P\_{0},\mbox{Var}[Y\_{T}]\right\}, for every t∈[0,T]t\in[0,T]. Then the result follows from equation ([4.16](https://arxiv.org/html/2511.19186v1#S4.E16 "In item (ii) ‣ Proposition 4.6. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and concludes the proof.

### A.4 Proof of Proposition [4.7](https://arxiv.org/html/2511.19186v1#S4.Thmthm7 "Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

First, we discuss the first condition of Definition [4.1](https://arxiv.org/html/2511.19186v1#S4.Thmthm1 "Definition 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). For the 𝔾\mathbb{G}-predictable process 𝜽⋆\bm{\theta}^{\star} given by ([4.13](https://arxiv.org/html/2511.19186v1#S4.E13 "In Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), it holds that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼\displaystyle\mathbb{E} | [∫0T|Ys|​‖𝜽s⋆‖1+‖𝜽s⋆‖22​d​s]\displaystyle\left[\int\_{0}^{T}|Y\_{s}|\|\bm{\theta}^{\star}\_{s}\|\_{1}+\|\bm{\theta}^{\star}\_{s}\|\_{2}^{2}\mathrm{d}s\right] |  | (A22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[∫0T|Ys|​‖𝚯^−1​(𝐚​Ys+𝐛−𝐫n)+𝚯^−1​𝚺~𝐒​𝚺~Y⊤​(f^​(s)​Ys+g^​(s))‖1​ds]\displaystyle\mathbb{E}\left[\int\_{0}^{T}|Y\_{s}|\|\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}Y\_{s}+\mathbf{b}-\mathbf{r}\_{n}\right)+\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\left(\hat{f}(s)Y\_{s}+\hat{g}(s)\right)\|\_{1}\mathrm{d}s\right] |  | (A23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼​[∫0T‖𝚯^−1​(𝐚​Ys+𝐛−𝐫n)+𝚯^−1​𝚺~𝐒​𝚺~Y⊤​(f^​(s)​Ys+g^​(s))‖22​ds]\displaystyle+\mathbb{E}\left[\int\_{0}^{T}\|\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}Y\_{s}+\mathbf{b}-\mathbf{r}\_{n}\right)+\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\left(\hat{f}(s)Y\_{s}+\hat{g}(s)\right)\|\_{2}^{2}\mathrm{d}s\right] |  | (A24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​[∫0T|Ys|​‖𝚯^−1​(𝐚​Ys+𝐛−𝐫n)‖1+|Ys|​‖𝚯^−1​𝚺~𝐒​𝚺~Y⊤​(f^​(s)​Ys+g^​(s))‖1​d​s]\displaystyle\mathbb{E}\left[\int\_{0}^{T}|Y\_{s}|\|\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}Y\_{s}+\mathbf{b}-\mathbf{r}\_{n}\right)\|\_{1}+|Y\_{s}|\|\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\left(\hat{f}(s)Y\_{s}+\hat{g}(s)\right)\|\_{1}\mathrm{d}s\right] |  | (A25) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼​[∫0T(‖𝚯^−1​(𝐚​Ys+𝐛−𝐫n)‖2+‖𝚯^−1​𝚺~𝐒​𝚺~Y⊤​(f^​(s)​Ys+g^​(s))‖2)2​ds]\displaystyle+\mathbb{E}\left[\int\_{0}^{T}\left(\|\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{a}Y\_{s}+\mathbf{b}-\mathbf{r}\_{n}\right)\|\_{2}+\|\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\left(\hat{f}(s)Y\_{s}+\hat{g}(s)\right)\|\_{2}\right)^{2}\mathrm{d}s\right] |  | (A26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼[∫0TYs2∥𝚯^−1𝐚∥1+|Ys|∥𝚯^−1(𝐛−𝐫n)∥1+Ys2|f^(s)|∥𝚯^−1𝚺~𝐒𝚺~Y⊤∥1\displaystyle\mathbb{E}\bigg[\int\_{0}^{T}Y\_{s}^{2}\|\mathbf{\hat{\Theta}}^{-1}\mathbf{a}\|\_{1}+|Y\_{s}|\|\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)\|\_{1}+Y\_{s}^{2}|\hat{f}(s)|\|\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\|\_{1} |  | (A27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +|Ys||g^(s)|∥𝚯^−1𝚺~𝐒𝚺~Y⊤∥1ds]+4𝔼[∫0TYs2∥𝚯^−1𝐚∥22+∥𝚯^−1(𝐛−𝐫n)∥22\displaystyle+|Y\_{s}||\hat{g}(s)|\|\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\|\_{1}\mathrm{d}s\bigg]+4\mathbb{E}\bigg[\int\_{0}^{T}Y^{2}\_{s}\|\mathbf{\hat{\Theta}}^{-1}\mathbf{a}\|^{2}\_{2}+\|\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)\|\_{2}^{2} |  | (A28) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +Ys2f^2(s)∥𝚯^−1𝚺~𝐒𝚺~Y⊤∥22+g^2(s)∥𝚯^−1𝚺~𝐒𝚺~Y⊤∥22ds]\displaystyle+Y\_{s}^{2}\hat{f}^{2}(s)\|\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\|\_{2}^{2}+\hat{g}^{2}(s)\|\mathbf{\hat{\Theta}}^{-1}\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\|\_{2}^{2}\mathrm{d}s\bigg] |  | (A29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | η1+η2​𝔼​[∫0T|Ys|+Ys2​d​s]<∞\displaystyle\eta\_{1}+\eta\_{2}\mathbb{E}\left[\int\_{0}^{T}|Y\_{s}|+Y\_{s}^{2}\mathrm{d}s\right]<\infty |  | (A30) |

for some positive constant η1\eta\_{1} and η2\eta\_{2}. The first inequality follows by applying the triangle inequality to the l1l\_{1} and l2l\_{2} norms, then using the Cauchy–Schwarz inequality on the second term to bound the square of the sum by the sum of squares, and finally using the positive homogeneity of norms to factor out scalar terms.
The second inequality follows by applying the same arguments as the first. The third inequality holds because f^​(t),g^​(t)∈𝒞b1​([0,T])\hat{f}(t),\,\hat{g}(t)\in\mathcal{C}^{1}\_{b}([0,T]) and the last inequality comes from the fact that YY is a Gaussian random variable, which implies that it has finite moments of all orders. We now discuss the second condition of Definition [4.1](https://arxiv.org/html/2511.19186v1#S4.Thmthm1 "Definition 4.1. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). We would like to show that

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼​[(C^t𝜽⋆)d​(1−δ)​(1+α)]<∞,\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}^{\bm{\theta}^{\star}}\_{t})^{d(1-\delta)(1+\alpha)}\right]<\infty, |  |

for some α>0\alpha>0 and d>1d>1. Using the explicit solution of equation ([3.8](https://arxiv.org/html/2511.19186v1#S3.E8 "In 3 The carbon-penalised proportional portfolio insurance strategy ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), i.e

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^t𝜽=C^0𝜽​exp⁡{∫0t[r+𝜽u⊤​(𝐚​Yu+𝐛−𝐫n)−12​𝜽u⊤​𝚯^​𝜽u]​du+∫0t𝜽u⊤​𝚺~𝐒​d𝐙u𝐒},\hat{C}^{\bm{\theta}}\_{t}=\hat{C}\_{0}^{\bm{\theta}}\exp\left\{\int\_{0}^{t}\left[r+\bm{\theta}\_{u}^{\top}\left(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\right)-\frac{1}{2}\bm{\theta}\_{u}^{\top}\mathbf{\hat{\Theta}}\bm{\theta}\_{u}\right]\mathrm{d}u+\int\_{0}^{t}\bm{\theta}\_{u}^{\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{u}\right\}, |  | (A31) |

we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supt∈[0,T]\displaystyle\sup\_{t\in[0,T]} | 𝔼​[(C^t𝜽⋆)d​(1−δ)​(1+α)]\displaystyle\mathbb{E}\left[(\hat{C}^{\bm{\theta}^{\star}}\_{t})^{d(1-\delta)(1+\alpha)}\right] |  | (A32) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | supt∈[0,T](C^0𝜽⋆​er​t)d​(1−δ)​(1+α)​𝔼​[ed​(1−δ)​(1+α)​∫0t[(𝜽u⋆)⊤​(𝐚​Yu+𝐛−𝐫n)−12​𝜽u⋆,⊤​𝚯^​𝜽u⋆]​du+d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​𝚺~𝐒​d𝐙u𝐒]\displaystyle\sup\_{t\in[0,T]}(\hat{C}\_{0}^{\bm{\theta}^{\star}}e^{rt})^{d(1-\delta)(1+\alpha)}\mathbb{E}\left[e^{d(1-\delta)(1+\alpha)\int\_{0}^{t}[(\bm{\theta}^{\star}\_{u})^{\top}(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n})-\frac{1}{2}\bm{\theta}^{\star,\top}\_{u}\mathbf{\hat{\Theta}}\bm{\theta}^{\star}\_{u}]\mathrm{d}u+d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{u}}\right] |  | (A33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (C^0𝜽⋆)d​(1−δ)​(1+α)2(supt∈[0,T]er​d​(1−δ)​(1+α)​t𝔼[e2​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​(𝐚​Yu+𝐛−𝐫n)​du\displaystyle\dfrac{(\hat{C}^{\bm{\theta}^{\star}}\_{0})^{d(1-\delta)(1+\alpha)}}{2}\left(\sup\_{t\in[0,T]}e^{rd(1-\delta)(1+\alpha)t}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\left(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\right)\mathrm{d}u}\right.\right. |  | (A34) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | e−d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​𝚯^​𝜽u⋆​du]+supt∈[0,T]er​d​(1−δ)​(1+α)​t𝔼[e2​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​𝚺~𝐒​d𝐙u𝐒])\displaystyle\left.\left.e^{-d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\mathbf{\hat{\Theta}}\bm{\theta}^{\star}\_{u}\mathrm{d}u}\right]+\sup\_{t\in[0,T]}e^{rd(1-\delta)(1+\alpha)t}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}\_{u}^{\star,\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{u}}\right]\right) |  | (A35) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | κ4(supt∈[0,T]𝔼[e4​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​(𝐚​Yu+𝐛−𝐫n)​du]+supt∈[0,T]𝔼[e−2​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​𝚯^​𝜽u⋆​du]\displaystyle\dfrac{\kappa}{4}\left(\sup\_{t\in[0,T]}\mathbb{E}\left[e^{4d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\left(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\right)\mathrm{d}u}\right]+\sup\_{t\in[0,T]}\mathbb{E}\left[e^{-2d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\mathbf{\hat{\Theta}}\bm{\theta}^{\star}\_{u}\mathrm{d}u}\right]\right. |  | (A36) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2supt∈[0,T]𝔼[e2​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​𝚺~𝐒​d𝐙u𝐒])\displaystyle\left.+2\sup\_{t\in[0,T]}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}\_{u}^{\star,\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{u}}\right]\right) |  | (A37) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | κ4(supt∈[0,T]𝔼[e4​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​(𝐚​Yu+𝐛−𝐫n)​du]+supt∈[0,T]𝔼[e−2​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​𝚯^​𝜽u⋆​du]\displaystyle\dfrac{\kappa}{4}\left(\sup\_{t\in[0,T]}\mathbb{E}\left[e^{4d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\left(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\right)\mathrm{d}u}\right]+\sup\_{t\in[0,T]}\mathbb{E}\left[e^{-2d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\mathbf{\hat{\Theta}}\bm{\theta}^{\star}\_{u}\mathrm{d}u}\right]\right. |  | (A38) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2supt∈[0,T]𝔼[e2​d2​(1−δ)2​(1+α)2​∫0t‖𝜽u⋆,⊤​𝚺~𝐒‖22​du]),\displaystyle\left.+2\sup\_{t\in[0,T]}\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}\int\_{0}^{t}\|\bm{\theta}\_{u}^{\star,\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\|\_{2}^{2}\mathrm{d}u}\right]\right), |  | (A39) |

where κ=(C^0𝜽⋆​er​T)d​(1−δ)​(1+α)\kappa=(\hat{C}^{\bm{\theta}^{\star}}\_{0}e^{rT})^{d(1-\delta)(1+\alpha)}. In the first and second inequality we have used a​b≤12​(a2+b2)ab\leq\frac{1}{2}(a^{2}+b^{2}) for any a,b∈ℝa,b\in\mathbb{R}, and the last equality comes from the fact that 𝔼​[e2​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​𝚺~𝐒​d𝐙u𝐒]=𝔼​[e2​d2​(1−δ)2​(1+α)2​∫0t‖𝜽u⋆,⊤​𝚺~𝐒‖22​du]\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}\_{u}^{\star,\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathrm{d}\mathbf{Z}^{\mathbf{S}}\_{u}}\right]=\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}\int\_{0}^{t}\|\bm{\theta}\_{u}^{\star,\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\|\_{2}^{2}\mathrm{d}u}\right]. Now, we need to distinguish between two cases: δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1) and δ∈𝒫∩(1+∞)\delta\in\mathcal{P}\cap(1+\infty). Assuming that δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1), equation ([A39](https://arxiv.org/html/2511.19186v1#A1.E39 "In A.4 Proof of Proposition 4.7 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supt∈[0,T]𝔼​[(C^t𝜽⋆)d​(1−δ)​(1+α)]\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}\_{t}^{\bm{\theta}^{\star}})^{d(1-\delta)(1+\alpha)}\right] |  | (A40) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤κ4​(1+supt∈[0,T]𝔼​[e4​d​(1−δ)​(1+α)​∫0t𝜽u⋆,⊤​(𝐚​Yu+𝐛−𝐫n)​du]+2​supt∈[0,T]𝔼​[e2​d2​(1−δ)2​(1+α)2​∫0t‖𝜽u⋆,⊤​𝚺~𝐒‖22​du])\displaystyle\leq\dfrac{\kappa}{4}\left(1+\sup\_{t\in[0,T]}\mathbb{E}\left[e^{4d(1-\delta)(1+\alpha)\int\_{0}^{t}\bm{\theta}^{\star,\top}\_{u}\left(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\right)\mathrm{d}u}\right]+2\sup\_{t\in[0,T]}\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}\int\_{0}^{t}\|\bm{\theta}\_{u}^{\star,\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\|\_{2}^{2}\mathrm{d}u}\right]\right) |  | (A41) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤κ4​(1+supt∈[0,T]𝔼​[e2​d​(1−δ)​(1+α)​∫0t(‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖2)​du]+2​supt∈[0,T]𝔼​[e2​d2​(1−δ)2​(1+α)2​∫0tw​‖𝜽u⋆‖22​du])\displaystyle\leq\dfrac{\kappa}{4}\left(1+\sup\_{t\in[0,T]}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\int\_{0}^{t}\left(\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|^{2}\right)\mathrm{d}u}\right]+2\sup\_{t\in[0,T]}\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}\int\_{0}^{t}w\|\bm{\theta}\_{u}^{\star}\|\_{2}^{2}\mathrm{d}u}\right]\right) |  | (A42) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤κ4​(1+𝔼​[e2​d​(1−δ)​(1+α)​∫0T(‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖22)​du]+2​𝔼​[e2​d2​(1−δ)2​(1+α)2​w​∫0T‖𝜽u⋆‖22​du]),\displaystyle\leq\dfrac{\kappa}{4}\left(1+\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\int\_{0}^{T}\left(\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|\_{2}^{2}\right)\mathrm{d}u}\right]+2\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}w\int\_{0}^{T}\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}\mathrm{d}u}\right]\right), |  | (A43) |

where in the second inequality we have used 𝜽u⋆,⊤​(𝐚​Yu+𝐛−𝐫n)≤12​(‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖22)\bm{\theta}^{\star,\top}\_{u}\left(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\right)\leq\frac{1}{2}\left(\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|\_{2}^{2}\right),
and ‖𝜽u⋆,⊤​𝚺~𝐒‖22≤w​‖𝜽u⋆‖22\|\bm{\theta}\_{u}^{\star,\top}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\|\_{2}^{2}\leq w\|\bm{\theta}\_{u}^{\star}\|\_{2}^{2}, for every u∈[0,T]u\in[0,T], with ww given by equation ([4.20](https://arxiv.org/html/2511.19186v1#S4.E20 "In item (ii) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). The third inequality follows from the monotonicity of the integrals in tt, which implies that the supremum over t∈[0,T]t\in[0,T] is attained at t=Tt=T. By Jensen’s inequality, we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | e2​d​(1−δ)​(1+α)​∫0T(‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖22)​du\displaystyle e^{2d(1-\delta)(1+\alpha)\int\_{0}^{T}\left(\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|\_{2}^{2}\right)\mathrm{d}u} | ≤1T​∫0Te2​d​(1−δ)​(1+α)​T​(‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖22)​du,\displaystyle\leq\frac{1}{T}\int\_{0}^{T}e^{2d(1-\delta)(1+\alpha)T\left(\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|\_{2}^{2}\right)}\mathrm{d}u, |  | (A44) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | e2​d2​(1−δ)2​(1+α)2​w​∫0T‖𝜽u⋆‖22​du\displaystyle e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}w\int\_{0}^{T}\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}\mathrm{d}u} | ≤1T​∫0Te2​d2​(1−δ)2​(1+α)2​w​T​‖𝜽u⋆‖22​du,\displaystyle\leq\frac{1}{T}\int\_{0}^{T}e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}wT\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}}\mathrm{d}u, |  | (A45) |

therefore

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[e2​d​(1−δ)​(1+α)​∫0T(‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖22)​du]\displaystyle\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\int\_{0}^{T}\left(\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|\_{2}^{2}\right)\mathrm{d}u}\right] | ≤1T​∫0T𝔼​[e2​d​(1−δ)​(1+α)​T​(‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖22)]​du,\displaystyle\leq\frac{1}{T}\int\_{0}^{T}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)T\left(\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|\_{2}^{2}\right)}\right]\mathrm{d}u, |  | (A46) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[e2​d2​(1−δ)2​(1+α)2​w​∫0T‖𝜽u⋆‖22​du]\displaystyle\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}w\int\_{0}^{T}\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}\mathrm{d}u}\right] | ≤1T​∫0T𝔼​[e2​d2​(1−δ)2​(1+α)2​w​T​‖𝜽u⋆‖22]​du.\displaystyle\leq\dfrac{1}{T}\int\_{0}^{T}\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}wT\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}}\right]\mathrm{d}u. |  | (A47) |

Hence, equation ([A43](https://arxiv.org/html/2511.19186v1#A1.E43 "In A.4 Proof of Proposition 4.7 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈[0,T]𝔼​[(C^t𝜽⋆)d​(1−δ)​(1+α)]\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}\_{t}^{\bm{\theta}^{\star}})^{d(1-\delta)(1+\alpha)}\right] |  | (A48) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤κ4​(1+1T​∫0T𝔼​[e2​d​(1−δ)​(1+α)​T​[‖𝜽u⋆‖22+‖𝐚​Yu+𝐛−𝐫n‖22]]​du+2T​∫0T𝔼​[e2​d2​(1−δ)2​(1+α)2​w​T​‖𝜽u⋆‖22]​du)\displaystyle\leq\dfrac{\kappa}{4}\left(1+\dfrac{1}{T}\int\_{0}^{T}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)T\left[\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|^{2}\_{2}\right]}\right]\mathrm{d}u+\dfrac{2}{T}\int\_{0}^{T}\mathbb{E}\left[e^{2d^{2}(1-\delta)^{2}(1+\alpha)^{2}wT\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}}\right]\mathrm{d}u\right) |  | (A49) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤κ4​(1+3T​∫0T𝔼​[e2​d​(1−δ)​(1+α)​[(1∨d​(1−δ)​(1+α)​w)​T​‖𝜽u⋆‖22+T​‖𝐚​Yu+𝐛−𝐫n‖22]]​du)\displaystyle\leq\dfrac{\kappa}{4}\left(1+\dfrac{3}{T}\int\_{0}^{T}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)T\|\bm{\theta}^{\star}\_{u}\|\_{2}^{2}+T\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|^{2}\_{2}\right]}\right]\mathrm{d}u\right) |  | (A50) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤κ4​(1+3T​∫0T𝔼​[e2​d​(1−δ)​(1+α)​[(1∨d​(1−δ)​(1+α)​w)​2​n​T​(c12​Yu2+c22)+2​n​T​(aM2​Yu2+bM2)]]​du)\displaystyle\leq\dfrac{\kappa}{4}\left(1+\dfrac{3}{T}\int\_{0}^{T}\mathbb{E}\left[e^{2d(1-\delta)(1+\alpha)\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)2nT(c\_{1}^{2}Y\_{u}^{2}+c\_{2}^{2})+2nT(a\_{M}^{2}Y\_{u}^{2}+b\_{M}^{2})\right]}\right]\mathrm{d}u\right) |  | (A51) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤κ4​(1+3​κ1T​∫0T𝔼​[e4​d​(1−δ)​(1+α)​n​T​[(1∨d​(1−δ)​(1+α)​w)​c12+aM2]​Yu2]​du),\displaystyle\leq\dfrac{\kappa}{4}\left(1+\dfrac{3\kappa\_{1}}{T}\int\_{0}^{T}\mathbb{E}\left[e^{4d(1-\delta)(1+\alpha)nT\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)c\_{1}^{2}+a\_{M}^{2}\right]Y\_{u}^{2}}\right]\mathrm{d}u\right), |  | (A52) |

for some positive constant κ1\kappa\_{1}. In the third inequality we have used

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxi=1,…,n⁡|θi,u⋆|\displaystyle\max\_{i=1,\dots,n}|\theta^{\star}\_{i,u}| | ≤c1​|Yu|+c2,\displaystyle\leq c\_{1}|Y\_{u}|+c\_{2}, |  | (A53) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxi=1,…,n⁡|(𝐚​Yu+𝐛−𝐫n)i|\displaystyle\max\_{i=1,\dots,n}|\left(\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\right)\_{i}| | ≤aM​|Yu|+bM,\displaystyle\leq a\_{M}|Y\_{u}|+b\_{M}, |  | (A54) |

for every u∈[0,T]u\in[0,T], where c1c\_{1} and ama\_{m} are given by equations ([4.19](https://arxiv.org/html/2511.19186v1#S4.E19 "In item (ii) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([4.22](https://arxiv.org/html/2511.19186v1#S4.E22 "In item (ii) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) respectively, and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | c2\displaystyle c\_{2} | =maxi=1,…,n⁡|(𝚯^−1​(𝐛−𝒓n+𝚺~𝐒​𝚺~Y⊤​supt∈[0,T]g^​(t)))i|,\displaystyle=\max\_{i=1,\dots,n}\bigg|\left(\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{b}-\bm{r}\_{n}+\bm{\tilde{\Sigma}}\_{\mathbf{S}}\bm{\tilde{\Sigma}}\_{Y}^{\top}\sup\_{t\in[0,T]}\hat{g}(t)\right)\right)\_{i}\bigg|, |  | (A55) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | bM\displaystyle b\_{M} | =maxi=1,…,n⁡|(𝐛−𝐫n)i|.\displaystyle=\max\_{i=1,\dots,n}|\left(\mathbf{b}-\mathbf{r}\_{n}\right)\_{i}|. |  | (A56) |

Consequently,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖𝜽u‖22\displaystyle\|\bm{\theta}\_{u}\|\_{2}^{2} | ≤2​n​(c12​Yu2+c22),\displaystyle\leq 2n\left(c\_{1}^{2}Y\_{u}^{2}+c\_{2}^{2}\right), |  | (A57) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖𝐚​Yu+𝐛−𝐫n‖22\displaystyle\|\mathbf{a}Y\_{u}+\mathbf{b}-\mathbf{r}\_{n}\|\_{2}^{2} | ≤n​(aM2​|Yu|+bM)2≤2​n​(aM2​Yu+bM2),\displaystyle\leq n\left(a\_{M}^{2}|Y\_{u}|+b\_{M}\right)^{2}\leq 2n\left(a\_{M}^{2}Y\_{u}+b\_{M}^{2}\right), |  | (A58) |

for every u∈[0,T]u\in[0,T]. Finally, since YtY\_{t} is Gaussian,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[e4​d​(1−δ)​(1+α)​n​T​[(1∨d​(1−δ)​(1+α)​w)​c12+aM2]​Yu2]<∞\mathbb{E}\left[e^{4d(1-\delta)(1+\alpha)nT\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)c\_{1}^{2}+a\_{M}^{2}\right]Y\_{u}^{2}}\right]<\infty |  | (A59) |

for every u∈[0,T]u\in[0,T] if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−8​d​(1−δ)​(1+α)​n​T​[(1∨d​(1−δ)​(1+α)​w)​c12+aM2]​Var​[Yu]>0.1-8d(1-\delta)(1+\alpha)nT\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)c\_{1}^{2}+a\_{M}^{2}\right]\mbox{Var}[Y\_{u}]>0. |  | (A60) |

Recalling that Var​[Yu]<max⁡{P0,Var​[YT]}\mbox{Var}[Y\_{u}]<\max\left\{P\_{0},\mbox{Var}[Y\_{T}]\right\}, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−8​d​(1−δ)​(1+α)​n​T​[(1∨d​(1−δ)​(1+α)​w)​c12+aM2]​Var​[Yu]>1−8​d​(1−δ)​(1+α)​n​T​[(1∨d​(1−δ)​(1+α)​w)​c12+aM2]​max⁡{P0,Var​[YT]},1-8d(1-\delta)(1+\alpha)nT\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)c\_{1}^{2}+a\_{M}^{2}\right]\mbox{Var}[Y\_{u}]>\\ 1-8d(1-\delta)(1+\alpha)nT\left[\left(1\vee d(1-\delta)(1+\alpha)w\right)c\_{1}^{2}+a\_{M}^{2}\right]\max\left\{P\_{0},\mbox{Var}[Y\_{T}]\right\}, |  | (A61) |

for every u∈[0,T]u\in[0,T]. Then, the result then follows from ([4.17](https://arxiv.org/html/2511.19186v1#S4.E17 "In item (i) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). Now we discuss the second case where δ∈(1,∞)\delta\in(1,\infty). Applying the same steps as in the previous case, equation ([A39](https://arxiv.org/html/2511.19186v1#A1.E39 "In A.4 Proof of Proposition 4.7 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈[0,T]𝔼​[(C^t𝜽⋆)d​(1−δ)​(1+α)]≤κ2T​∫0T𝔼​[e4​d​(1−δ)​(1+α)​n​T​[(−(1+w)∧d​(1−δ)​(1+α)​w~)​c12−aM2]​Yu2]​du.\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}\_{t}^{\bm{\theta}^{\star}})^{d(1-\delta)(1+\alpha)}\right]\leq\dfrac{\kappa\_{2}}{T}\int\_{0}^{T}\mathbb{E}\left[e^{4d(1-\delta)(1+\alpha)nT\left[\left(-(1+w)\wedge d(1-\delta)(1+\alpha)\tilde{w}\right)c\_{1}^{2}-a\_{M}^{2}\right]Y\_{u}^{2}}\right]\mathrm{d}u. |  | (A62) |

where w~\tilde{w} is given by equation ([4.21](https://arxiv.org/html/2511.19186v1#S4.E21 "In item (ii) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). As in the previous case,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[e4​d​(1−δ)​(1+α)​n​T​[(−(1+w)∧d​(1−δ)​(1+α)​w~)​c12−aM2]​Yu2]<∞,\mathbb{E}\left[e^{4d(1-\delta)(1+\alpha)nT\left[\left(-(1+w)\wedge d(1-\delta)(1+\alpha)\tilde{w}\right)c\_{1}^{2}-a\_{M}^{2}\right]Y\_{u}^{2}}\right]<\infty, |  | (A63) |

for every u∈[0,T]u\in[0,T] if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−8​d​(1−δ)​(1+α)​n​T​[(−(1+w)∧d​(1−δ)​(1+α)​w~)​c12−aM2]​max⁡{P0,Var​[YT]}>0.1-8d(1-\delta)(1+\alpha)nT\left[\left(-(1+w)\wedge d(1-\delta)(1+\alpha)\tilde{w}\right)c\_{1}^{2}-a\_{M}^{2}\right]\max\left\{P\_{0},\mbox{Var}[Y\_{T}]\right\}>0. |  | (A64) |

The result then follows from ([4.18](https://arxiv.org/html/2511.19186v1#S4.E18 "In item (ii) ‣ Proposition 4.7. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")).

### A.5 Proof of Proposition [4.8](https://arxiv.org/html/2511.19186v1#S4.Thmthm8 "Proposition 4.8. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

The optimal controls 𝜽⋆\bm{\theta}^{\star} are linked to m⋆m^{\star} and 𝝅⋆\bm{\pi}^{\star} through the following system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {mt​𝝅t=𝜽t⋆,𝝅t⊤​𝟏n=1,\begin{cases}\begin{aligned} m\_{t}\bm{\pi}\_{t}&=\bm{\theta}^{\star}\_{t},\\ \bm{\pi}\_{t}^{\top}\mathbf{1}\_{n}&=1,\end{aligned}\end{cases} |  | (A65) |

whose solutions are given by (mt⋆,𝝅t⋆)=(𝜽t⋆,⊤​𝟏n,θ1,t⋆𝜽t⋆,⊤​𝟏n,…,θn,t⋆𝜽t⋆,⊤​𝟏n)(m^{\star}\_{t},\,\bm{\pi}\_{t}^{\star})=\left(\bm{\theta}\_{t}^{\star,\top}\mathbf{1}\_{n},\,\frac{\theta^{\star}\_{1,t}}{\bm{\theta}\_{t}^{\star,\top}\mathbf{1}\_{n}},\,\dots,\frac{\theta^{\star}\_{n,t}}{\bm{\theta}\_{t}^{\star,\top}\mathbf{1}\_{n}}\right)
for every t∈[0,T]t\in[0,T]. This concludes the proof.

### A.6 Proof of Corollary [4.9](https://arxiv.org/html/2511.19186v1#S4.Thmthm9 "Corollary 4.9. ‣ Logarithmic case. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

We apply pointwise optimisation to obtain the optimal controls. Computing the expectation in ([4.29](https://arxiv.org/html/2511.19186v1#S4.E29 "In Logarithmic case. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(c)+r​(T−t)+𝔼t,y​[∫tT𝜽s⊤​(𝐚​Ys+𝐛−𝐫n)​ds]−12​𝔼t,y​[∫tT𝜽s⊤​𝚯​𝜽s​ds],\log\left(c\right)+r\left(T-t\right)+\mathbb{E}^{t,y}\left[\int\_{t}^{T}\bm{\theta}\_{s}^{\top}\left(\mathbf{a}Y\_{s}+\mathbf{b}-\mathbf{r}\_{n}\right)\mathrm{d}s\right]-\dfrac{1}{2}\mathbb{E}^{t,y}\left[\int\_{t}^{T}\bm{\theta}\_{s}^{\top}\mathbf{\Theta}\bm{\theta}\_{s}\mathrm{d}s\right], |  | (A66) |

where 𝚯=𝚺~𝐒​𝚺~𝐒⊤+𝚺𝐒​𝚺𝐒⊤⊙𝐞\mathbf{\Theta}=\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}+\mathbf{\Sigma}\_{\mathbf{S}}\mathbf{\Sigma}\_{\mathbf{S}}^{\top}\odot\mathbf{e}.
Taking the first order conditions, we obtain the following system of linear equations 𝐚​Yt+𝐛−𝐫n−𝚯​𝜽t=𝟎n\mathbf{a}Y\_{t}+\mathbf{b}-\mathbf{r}\_{n}-\mathbf{\Theta}\bm{\theta}\_{t}=\mathbf{0}\_{n}, whose solution provide a candidate for the optimal control 𝜽⋆​(t,y)=𝚯−1​(𝐚​y+𝐛−𝐫n)\bm{\theta}^{\star}(t,y)=\mathbf{\Theta}^{-1}\left(\mathbf{a}y+\mathbf{b}-\mathbf{r}\_{n}\right). The Hessian matrix −𝚯-\mathbf{\Theta} is negative definite for every 𝜽\bm{\theta}, ensuring that 𝜽⋆\bm{\theta}^{\star} is the the unique well-defined maximiser of ([A66](https://arxiv.org/html/2511.19186v1#A1.E66 "In A.6 Proof of Corollary 4.9 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and hence the optimal control. By inserting 𝜽⋆\bm{\theta}^{\star} into ([A66](https://arxiv.org/html/2511.19186v1#A1.E66 "In A.6 Proof of Corollary 4.9 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we obtain a stochastic representation of the value function, namely

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(t,c,y)=\displaystyle v(t,c,y)= | log⁡(c)+[r+12​(𝐛−𝐫n)⊤​𝚯−1​(𝐛−𝐫n)]​(T−t)+12​𝐚⊤​𝚯−1​𝐚​𝔼t,y​[∫tTYs2​ds]\displaystyle\log\left(c\right)+\left[r+\dfrac{1}{2}\left(\mathbf{b}-\mathbf{r}\_{n}\right)^{\top}\mathbf{\Theta}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)\right]\left(T-t\right)+\dfrac{1}{2}\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}\mathbb{E}^{t,y}\left[\int\_{t}^{T}Y^{2}\_{s}\mathrm{d}s\right] |  | (A67) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝐚⊤​𝚯−1​(𝐛−𝐫n)​𝔼t,y​[∫tTYs​ds].\displaystyle+\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)\mathbb{E}^{t,y}\left[\int\_{t}^{T}Y\_{s}\mathrm{d}s\right]. |  | (A68) |

Since YY is modeled as an OU process, we can explicitly compute 𝔼t,y​[∫tTYs​ds]\mathbb{E}^{t,y}\left[\int\_{t}^{T}Y\_{s}\mathrm{d}s\right] and 𝔼t,y​[∫tTYs2​ds]\mathbb{E}^{t,y}\left[\int\_{t}^{T}Y\_{s}^{2}\mathrm{d}s\right], which are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼t,y​[∫tTYs​ds]=\displaystyle\mathbb{E}^{t,y}\left[\int\_{t}^{T}Y\_{s}\mathrm{d}s\right]= | y​eλ​(T−t)−1λ+βλ​[eλ​(T−t)−1λ−(T−t)],\displaystyle y\dfrac{e^{\lambda\left(T-t\right)}-1}{\lambda}+\dfrac{\beta}{\lambda}\left[\frac{e^{\lambda\left(T-t\right)}-1}{\lambda}-\left(T-t\right)\right], |  | (A69) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼t,y​[∫tTYs2​𝑑s]=\displaystyle\mathbb{E}^{t,y}\left[\int\_{t}^{T}Y\_{s}^{2}\,ds\right]= | (y+βλ)2​e2​λ​(T−t)−12​λ−2​βλ​(y+βλ)​eλ​(T−t)−1λ+β2λ2​(T−t)\displaystyle\left(y+\dfrac{\beta}{\lambda}\right)^{2}\dfrac{e^{2\lambda\left(T-t\right)}-1}{2\lambda}-\frac{2\beta}{\lambda}\left(y+\dfrac{\beta}{\lambda}\right)\frac{e^{\lambda\left(T-t\right)}-1}{\lambda}+\dfrac{\beta^{2}}{\lambda^{2}}\left(T-t\right) |  | (A70) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +σY22​λ​[e2​λ​(T−t)−12​λ−(T−t)].\displaystyle+\dfrac{\sigma\_{Y}^{2}}{2\lambda}\left[\frac{e^{2\lambda\left(T-t\right)}-1}{2\lambda}-\left(T-t\right)\right]. |  | (A71) |

for every t∈[0,T]t\in[0,T], respectively. By inserting the above expressions into ([A68](https://arxiv.org/html/2511.19186v1#A1.E68 "In A.6 Proof of Corollary 4.9 ‣ Appendix A Proofs of some technical results of Section 4 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and rearranging the terms, we obtain the closed-form expression of the value function in equation ([4.32](https://arxiv.org/html/2511.19186v1#S4.E32 "In Corollary 4.9. ‣ Logarithmic case. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). This concludes the proof.

## Appendix B An example involving two uncorrelated assets, independent of the factor process

We consider a simplified setting in which only two stocks, S1S\_{1} and S2S\_{2}, are traded on the market, representing a green and a brown stock, respectively. Moreover, we assume that S1S\_{1} and S2S\_{2} are driven by independent Brownian motions, and are also independent of the factor process YY. In this case, it is possible to show that the function Δ​(x)\Delta(x) is positive for x∈(δ∗,+∞)x\in(\delta^{\*},+\infty), for some δ∗<1\delta^{\*}<1 that can be explicitly computed. In particular, we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(x)=λ2−(1−x)​(a12x​σ12+a22(x+ε)​σ22)​σY2,x∈(0,+∞).\Delta(x)=\lambda^{2}-(1-x)\left(\dfrac{a\_{1}^{2}}{x\sigma\_{1}^{2}}+\dfrac{a\_{2}^{2}}{(x+\varepsilon)\sigma\_{2}^{2}}\right)\sigma\_{Y}^{2},\quad x\in(0,+\infty). |  | (B1) |

This function is monotonic increasing and concave, moreover

|  |  |  |  |
| --- | --- | --- | --- |
|  | limδ→+∞Δ​(δ)=λ2+(a12σ12+a22σ22)​σY2>0,\lim\_{\delta\to+\infty}\Delta(\delta)=\lambda^{2}+\left(\dfrac{a\_{1}^{2}}{\sigma\_{1}^{2}}+\dfrac{a\_{2}^{2}}{\sigma\_{2}^{2}}\right)\sigma\_{Y}^{2}>0, |  | (B2) |

for all a1,a2∈ℝa\_{1},a\_{2}\in\mathbb{R} and555Recall that for a1=0a\_{1}=0 and a2=0a\_{2}=0 there is no factor process YY and in this case Δ​(x)=λ2>0\Delta(x)=\lambda^{2}>0, hence trivially, 𝒫=(0,1)∪(1,+∞)\mathcal{P}=(0,1)\cup(1,+\infty).

|  |  |  |  |
| --- | --- | --- | --- |
|  | limδ→0+Δ​(δ)={−∞,if ​a1≠0,λ2−a22ε​σ22​σY2,if ​a1=0​ and ​a2≠0.\lim\_{\delta\to 0^{+}}\Delta(\delta)=\begin{cases}-\infty,&\quad\mbox{if }a\_{1}\neq 0,\\ \lambda^{2}-\dfrac{a\_{2}^{2}}{\varepsilon\sigma\_{2}^{2}}\sigma\_{Y}^{2},&\quad\mbox{if }a\_{1}=0\mbox{ and }a\_{2}\neq 0.\end{cases} |  | (B3) |

For a1=0a\_{1}=0 and a2≠0a\_{2}\neq 0, we distinguish between two cases:

* (i)

  if λ2−σY2​a22ε​σ22≥0\lambda^{2}-\frac{\sigma\_{Y}^{2}a\_{2}^{2}}{\varepsilon\sigma\_{2}^{2}}\geq 0, then Δ​(δ)>0\Delta(\delta)>0 for every δ∈(0,+∞)\delta\in(0,+\infty), hence δ∗=0\delta^{\*}=0 and 𝒫=(0,1)∪(1,+∞)\mathcal{P}=(0,1)\cup(1,+\infty),
* (ii)

  if λ2<σY2​a22ε​σ22\lambda^{2}<\frac{\sigma\_{Y}^{2}a\_{2}^{2}}{\varepsilon\sigma\_{2}^{2}}, then there exists a unique δ¯​(ε)=a22​σY2−ε​λ2​σ22λ2​σ22+a22​σY2<1\bar{\delta}(\varepsilon)=\frac{a\_{2}^{2}\sigma\_{Y}^{2}-\varepsilon\lambda^{2}\sigma\_{2}^{2}}{\lambda^{2}\sigma\_{2}^{2}+a\_{2}^{2}\sigma\_{Y}^{2}}<1, which depends on ε\varepsilon such that Δ​(δ¯)=0\Delta(\bar{\delta})=0. Hence, setting δ∗=δ¯∧0\delta^{\*}=\bar{\delta}\wedge 0, we get that 𝒫=(δ∗,1)∪(1,+∞)\mathcal{P}=(\delta^{\*},1)\cup(1,+\infty). Note that the larger the value of ε\varepsilon, the larger the set of admissible risk aversion parameters.

In the case a1≠0a\_{1}\neq 0, δ∗\delta^{\*} is the positive solution of the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | [λ2​σ12​σ22+(a12​σ22+a22​σ12)​σY2]​δ2+[ε​λ2​σ12​σ22−((1−ε)​a12​σ22+a22​σ12)​σY2]​δ−ε​a12​σ22​σY2=0.\left[\lambda^{2}\sigma\_{1}^{2}\sigma\_{2}^{2}+\left(a\_{1}^{2}\sigma\_{2}^{2}+a\_{2}^{2}\sigma\_{1}^{2}\right)\sigma\_{Y}^{2}\right]\delta^{2}+\left[\varepsilon\lambda^{2}\sigma\_{1}^{2}\sigma\_{2}^{2}-\left(\left(1-\varepsilon\right)a\_{1}^{2}\sigma\_{2}^{2}+a\_{2}^{2}\sigma\_{1}^{2}\right)\sigma\_{Y}^{2}\right]\delta-\varepsilon a\_{1}^{2}\sigma\_{2}^{2}\sigma\_{Y}^{2}=0. |  | (B4) |

Note that this solution is still smaller than 11 and depends on ε\varepsilon, but it can never become zero or negative. Hence, 𝒫=(δ∗,1)∪(1,+∞)⊂(0,1)∪(1,+∞)\mathcal{P}=(\delta^{\*},1)\cup(1,+\infty)\subset(0,1)\cup(1,+\infty). This example provides additional insight. Indeed, by comparing the critical value δ⋆\delta^{\star} for different values of the penalisation ε\varepsilon, we find that the penalty for brown assets generally enlarges the set of admissible risk aversion parameters, which in turn implies that a lower risk aversion may be allowed for green assets.

## Appendix C Proofs of some technical results of Section [5](https://arxiv.org/html/2511.19186v1#S5 "5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

### C.1 Proof of Theorem [5.3](https://arxiv.org/html/2511.19186v1#S5.Thmthm3 "Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

To prove the first part of the theorem we replicate the same argument as in the proof of Theorem [4.3](https://arxiv.org/html/2511.19186v1#S4.Thmthm3 "Theorem 4.3. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), with the ansatz

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t,c,γ)=c1−δ1−δ​ψ^​(t,γ),f(t,c,\gamma)=\dfrac{c^{1-\delta}}{1-\delta}\hat{\psi}(t,\gamma), |  | (C1) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ^​(t,γ)=exp⁡{f¯​(t)2​γ2+g¯​(t)​γ+h¯​(t)}.\displaystyle\hat{\psi}(t,\gamma)=\exp\left\{\dfrac{\bar{f}(t)}{2}\gamma^{2}+\bar{g}(t)\gamma+\bar{h}(t)\right\}. |  | (C2) |

In the second part of the proof we establish
the relationship between between the solutions to the ODE systems in the full and partial information settings. In particular, applying equations (28)(28)–(30)(30) in Brendle ([2006](https://arxiv.org/html/2511.19186v1#bib.bib7)), we get ([5.22](https://arxiv.org/html/2511.19186v1#S5.E22 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([5.23](https://arxiv.org/html/2511.19186v1#S5.E23 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), and ([5.25](https://arxiv.org/html/2511.19186v1#S5.E25 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). Moreover, since f^​(t),g^​(t),h^​(t)∈𝒞b1​([0,T])\hat{f}(t),\,\hat{g}(t),\,\hat{h}(t)\in\mathcal{C}\_{b}^{1}([0,T]) (see Section [4](https://arxiv.org/html/2511.19186v1#S4 "4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), to show that f¯​(t)\bar{f}(t), g¯​(t)\bar{g}(t), and h¯​(t)\bar{h}(t) belong to the same class of regularity, it suffices to prove that 1−P​(t)​f^​(t)>01-P(t)\hat{f}(t)>0 for all t∈[0,T]t\in[0,T]. To show 1−f^​(t)​P​(t)>01-\hat{f}(t)P(t)>0 for every t∈[0,T]t\in[0,T], we start by proving that the closed set 𝒯:={t∈[0,T]:1−P​(t)​f^​(t)=0}\mathcal{T}:=\{t\in[0,T]:1-P(t)\hat{f}(t)=0\} is empty. Let us assume by contradiction that it is not empty and let t¯\bar{t} be its maximum. From the boundary condition of f^\hat{f} we see that 1−P​(T)​f^​(T)=11-P(T)\hat{f}(T)=1, hence t¯<T\bar{t}<T. Relation in ([5.22](https://arxiv.org/html/2511.19186v1#S5.E22 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) hold in the set 𝒯C∩[0,T]\mathcal{T}^{C}\cap[0,T], where 𝒯C\mathcal{T}^{C} is the complement of 𝒯\mathcal{T}. Therefore, for any z>0z>0 such that t¯+z<T\bar{t}+z<T, (1−P​(t¯+z)​f^​(t¯+z))​f¯​(t¯+z)=f^​(t¯+z)(1-P(\bar{t}+z)\hat{f}(\bar{t}+z))\bar{f}(\bar{t}+z)=\hat{f}(\bar{t}+z) and, by continuity of all the functions involved in the equality, (1−P​(t¯)​f^​(t¯))​f¯​(t¯)=f^​(t¯)(1-P(\bar{t})\hat{f}(\bar{t}))\bar{f}(\bar{t})=\hat{f}(\bar{t}). Since f^​(t)\hat{f}(t) is a monotone function (either increasing or decreasing, depending on the parameter δ\delta) and f^​(T)=0\hat{f}(T)=0, then f^​(t¯)=0\hat{f}(\bar{t})=0, hence t¯∉𝒯\bar{t}\not\in\mathcal{T}, which is a contradiction and 𝒯\mathcal{T} is the empty set. Since 𝒯\mathcal{T} is empty, 1−P​(t)​f^​(t)1-P(t)\hat{f}(t) is continuous on [0,T][0,T] and f^​(T)=1\hat{f}(T)=1, it follows that 1−P​(t)​f^​(t)>01-P(t)\hat{f}(t)>0 is strictly positive on [0,T][0,T]. This concludes the proof.

### C.2 Proof of Proposition [5.4](https://arxiv.org/html/2511.19186v1#S5.Thmthm4 "Proposition 5.4. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

Since, as shown in Proposition [5.3](https://arxiv.org/html/2511.19186v1#S5.Thmthm3 "Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), 1−P​(t),f^​(t)>01-P(t),\hat{f}(t)>0, it follows that f^​(t)\hat{f}(t) and f¯​(t)\bar{f}(t) must have the same sign (positive if δ∈(0,1)∩𝒫\delta\in(0,1)\cap\mathcal{P} and negative if δ∈(1,+∞)∩𝒫\delta\in(1,+\infty)\cap\mathcal{P}). We now prove that, if δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1), f¯​(t)\bar{f}(t) is positive strictly decreasing on [0,T][0,T]. This can be proved by rewriting the ODE in equation ([5.13](https://arxiv.org/html/2511.19186v1#S5.E13 "In 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) as f¯t​(t)=G​(f¯​(t))\bar{f}\_{t}(t)=G(\bar{f}(t)), where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​(t):=\displaystyle G(t):= | −[(1−δ)​𝐏¯​(t)​𝚯^−1​(𝐏¯​(t))⊤+𝐏¯​(t)​(𝚺~𝐒​𝚺~𝐒⊤)−1​(𝐏¯​(t))⊤]​t2\displaystyle-\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}+\mathbf{\bar{P}}(t)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\left(\mathbf{\bar{P}}(t)\right)^{\top}\right]t^{2} |  | (C3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −2​[(1−δ)​𝐏¯​(t)​𝚯^−1​𝐚+λ]​t−(1−δ)​𝐚⊤​𝚯^−1​𝐚,t∈[0,T].\displaystyle-2\left[\left(1-\delta\right)\mathbf{\bar{P}}(t)\mathbf{\hat{\Theta}}^{-1}\mathbf{a}+\lambda\right]t-\left(1-\delta\right)\mathbf{a}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a},\quad t\in[0,T]. |  | (C4) |

The boundary condition
implies that f¯​(T)=0\bar{f}(T)=0 and that G​(0)=−(1−δ)​𝐚⊤​𝚯^−1​𝐚<0G(0)=-\left(1-\delta\right)\mathbf{a}^{\top}\mathbf{\hat{\Theta}}^{-1}\mathbf{a}<0. Then, the function G​(t)G(t) must be negative
on [0,T][0,T] for the boundary condition to be satisfied, and hence f¯​(t)\bar{f}(t) is strictly decreasing. The
same argument applies to the case δ∈(1+∞)∩𝒫\delta\in(1+\infty)\cap\mathcal{P}, where the derivative of f¯​(t)\bar{f}(t) is positive, and hence f¯​(t)\bar{f}(t) is strictly increasing. This concludes the proof.

### C.3 Proof of Proposition [5.5](https://arxiv.org/html/2511.19186v1#S5.Thmthm5 "Proposition 5.5. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

The proof replicates the lines of that of Proposition [4.6](https://arxiv.org/html/2511.19186v1#S4.Thmthm6 "Proposition 4.6. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). Also in this case, we will show that supt∈[0,T]𝔼​[V^1+α​(t,C^t,Γt)]<∞\sup\_{t\in[0,T]}\mathbb{E}\left[\hat{V}^{1+\alpha}(t,\hat{C}\_{t},\Gamma\_{t})\right]<\infty, for some α>0\alpha>0. Using the form of the function V^\hat{V} (cfr. equation ([5.21](https://arxiv.org/html/2511.19186v1#S5.E21 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"))) we get that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supt∈[0,T]𝔼​[V^1+α​(t,C^t𝜽,Γt)]=\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[\hat{V}^{1+\alpha}(t,\hat{C}\_{t}^{\bm{\theta}},\Gamma\_{t})\right]= | supt∈[0,T]𝔼​[11−δ​(C^t𝜽)(1−δ)​(1+α)​e(1+α)​f¯​(t)2​Γt2+(1+α)​g¯​(t)​Γt+(1+α)​h¯​(t)]\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\left[\dfrac{1}{1-\delta}(\hat{C}^{\bm{\theta}}\_{t})^{(1-\delta)(1+\alpha)}e^{\frac{(1+\alpha)\bar{f}(t)}{2}\Gamma\_{t}^{2}+(1+\alpha)\bar{g}(t)\Gamma\_{t}+(1+\alpha)\bar{h}(t)}\right] |  | (C5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | κ~​supt∈[0,T]𝔼​[(C^t𝜽)(1−δ)​(1+α)​e(1+α)​f¯​(t)2​Γt2+(1+α)​g¯​(t)​Γt]\displaystyle\tilde{\kappa}\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}^{\bm{\theta}}\_{t})^{(1-\delta)(1+\alpha)}e^{\frac{(1+\alpha)\bar{f}(t)}{2}\Gamma\_{t}^{2}+(1+\alpha)\bar{g}(t)\Gamma\_{t}}\right] |  | (C6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | κ~​(supt∈[0,T]𝔼​[(C^t𝜽)d​(1−δ)​(1+α)]1d)​(supt∈[0,T]𝔼​[eq​(1+α)​f¯​(t)2​Γt2+q​(1+α)​g¯​(t)​Γt]1q),\displaystyle\tilde{\kappa}\left(\sup\_{t\in[0,T]}\mathbb{E}\left[(\hat{C}^{\bm{\theta}}\_{t})^{d(1-\delta)(1+\alpha)}\right]^{\frac{1}{d}}\right)\left(\sup\_{t\in[0,T]}\mathbb{E}\left[e^{\frac{q(1+\alpha)\bar{f}(t)}{2}\Gamma\_{t}^{2}+q(1+\alpha)\bar{g}(t)\Gamma\_{t}}\right]^{\frac{1}{q}}\right), |  | (C7) |

for some positive constant κ\kappa and some d,q>1d,\,q>1, where the first inequality comes from the fact that h¯​(⋅)∈𝒞b1​([0,T])\bar{h}(\cdot)\in\mathcal{C}^{1}\_{b}([0,T]), and the second follows from Hölder’s inequality. The first expectation is finite because of admissibility of the strategy (see the second condition of Definition [5.1](https://arxiv.org/html/2511.19186v1#S5.Thmthm1 "Definition 5.1. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). The second expectation, instead, is finite because the process Γ\Gamma is Gaussian. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[eq​(1+α)​f¯​(t)2​Γt2+q​(1+α)​g¯​(t)​Γt]<∞,\mathbb{E}\left[e^{\frac{q(1+\alpha)\bar{f}(t)}{2}\Gamma\_{t}^{2}+q(1+\alpha)\bar{g}(t)\Gamma\_{t}}\right]<\infty, |  | (C8) |

for every t∈[0,T]t\in[0,T] if and only if 1−q​(1+α)​f¯​(t)​Var​[Γt]>01-q(1+\alpha)\bar{f}(t)\mbox{Var}[\Gamma\_{t}]>0, where Var​[Γt]=Var​[Yt]−P​(t)\mbox{Var}[\Gamma\_{t}]=\mbox{Var}[Y\_{t}]-P(t). If δ∈𝒫∩(1,+∞)\delta\in\mathcal{P}\cap(1,+\infty), from Proposition [5.4](https://arxiv.org/html/2511.19186v1#S5.Thmthm4 "Proposition 5.4. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), f¯​(t)<0\bar{f}(t)<0. Hence, 1−q​(1+α)​f¯​(t)​Var​[Γt]>01-q(1+\alpha)\bar{f}(t)\mbox{Var}[\Gamma\_{t}]>0 and ([C8](https://arxiv.org/html/2511.19186v1#A3.E8 "In C.3 Proof of Proposition 5.5 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) is satisfied. If δ∈𝒫∩(0,1)\delta\in\mathcal{P}\cap(0,1), still from Proposition [5.4](https://arxiv.org/html/2511.19186v1#S5.Thmthm4 "Proposition 5.4. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"), f¯​(t)\bar{f}(t) is strictly positive and decreasing for every [0,T][0,T]. Therefore,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1−q​(1+α)​f¯​(t)​Var​[Γt]\displaystyle 1-q(1+\alpha)\bar{f}(t)\mbox{Var}[\Gamma\_{t}] | >1−q​(1+α)​f¯​(0)​Var​[Yt]\displaystyle>1-q(1+\alpha)\bar{f}(0)\mbox{Var}[Y\_{t}] |  | (C9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥1−q​(1+α)​f^​(0)1−P​(0)​f^​(0)​max⁡{P0,Var​[YT]},\displaystyle\geq 1-q(1+\alpha)\dfrac{\hat{f}(0)}{1-P(0)\hat{f}(0)}\max\left\{P\_{0},\mbox{Var}[Y\_{T}]\right\}, |  | (C10) |

where the first inequality follows from the monotonicity of f¯\bar{f} and from the fact that Var​[Γt]<Var​[Yt]\mbox{Var}[\Gamma\_{t}]<\mbox{Var}[Y\_{t}]. The second inequality follows from f¯​(t)=f^​(t)1−P​(t)​f^​(t)\bar{f}(t)=\frac{\hat{f}(t)}{1-P(t)\hat{f}(t)} for every t∈[0,T]t\in[0,T], and from the fact that Var​[Yt]\mbox{Var}[Y\_{t}] is always lower than its maximum value on [0,T][0,T], that is P0P\_{0} or Var​[YT]\mbox{Var}[Y\_{T}] depending on Var​[Yt]\mbox{Var}[Y\_{t}] being decreasing or increasing. Then the result follows immediately from ([5.26](https://arxiv.org/html/2511.19186v1#S5.E26 "In item (ii) ‣ Proposition 5.5. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")).

### C.4 Proof of Corollary [5.7](https://arxiv.org/html/2511.19186v1#S5.Thmthm7 "Corollary 5.7. ‣ Logarithmic case. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

The proof follows the same lines as that of Corollary [4.9](https://arxiv.org/html/2511.19186v1#S4.Thmthm9 "Corollary 4.9. ‣ Logarithmic case. ‣ 4 Optimisation problem under full information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"). Computing 𝔼t,c,γ​[log⁡(C^T𝜽)]\mathbb{E}^{t,c,\gamma}\left[\log(\hat{C}^{\bm{\theta}}\_{T})\right],
we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(c)+r​(T−t)+𝔼t,γ​[∫tT𝜽s⊤​(𝐚​Γs+𝐛−𝐫n)​ds]−12​𝔼t,γ​[∫tT𝜽s⊤​𝚯​𝜽s​ds],\log\left(c\right)+r\left(T-t\right)+\mathbb{E}^{t,\gamma}\left[\int\_{t}^{T}\bm{\theta}\_{s}^{\top}\left(\mathbf{a}\Gamma\_{s}+\mathbf{b}-\mathbf{r}\_{n}\right)\mathrm{d}s\right]-\dfrac{1}{2}\mathbb{E}^{t,\gamma}\left[\int\_{t}^{T}\bm{\theta}\_{s}^{\top}\mathbf{\Theta}\bm{\theta}\_{s}\mathrm{d}s\right],\\ |  | (C11) |

Taking the first order conditions, we obtain the following system of linear equations

|  |  |  |
| --- | --- | --- |
|  | 𝐚​Γt+𝐛−𝐫n−𝚯​𝜽t=𝟎n,\mathbf{a}\Gamma\_{t}+\mathbf{b}-\mathbf{r}\_{n}-\mathbf{\Theta}\bm{\theta}\_{t}=\mathbf{0}\_{n}, |  |

whose solution 𝜽¯⋆\bar{\bm{\theta}}^{\star} is given in equation ([5.37](https://arxiv.org/html/2511.19186v1#S5.E37 "In Corollary 5.7. ‣ Logarithmic case. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). The Hessian matrix is given by −𝚯-\bm{\Theta} and it is negative definite for every 𝜽∈ℝn\bm{\theta}\in\mathbb{R}^{n}. This ensure that 𝜽¯⋆\bar{\bm{\theta}}^{\star} is the unique well-defined maximiser and hence the optimal controls. Inserting the optimal strategy into the value function, we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V~​(t,c,γ)=\displaystyle\tilde{V}(t,c,\gamma)= | log⁡(c)+[r+12​(𝐛−𝐫n)⊤​𝚯−1​(𝐛−𝐫n)]​(T−t)+12​𝐚⊤​𝚯−1​𝐚​𝔼t,γ​[∫tTΓs2​ds]\displaystyle\log\left(c\right)+\left[r+\dfrac{1}{2}\left(\mathbf{b}-\mathbf{r}\_{n}\right)^{\top}\mathbf{\Theta}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)\right]\left(T-t\right)+\dfrac{1}{2}\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}\mathbb{E}^{t,\gamma}\left[\int\_{t}^{T}\Gamma^{2}\_{s}\mathrm{d}s\right] |  | (C12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝐚⊤​𝚯−1​(𝐛−𝐫n)​𝔼t,γ​[∫tTΓs​ds].\displaystyle+\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\left(\mathbf{b}-\mathbf{r}\_{n}\right)\mathbb{E}^{t,\gamma}\left[\int\_{t}^{T}\Gamma\_{s}\mathrm{d}s\right]. |  | (C13) |

Since Γt\Gamma\_{t} is a Gaussian process, we can easily compute which are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼t,γ​[∫tTΓs​ds]=\displaystyle\mathbb{E}^{t,\gamma}\left[\int\_{t}^{T}\Gamma\_{s}\mathrm{d}s\right]= | (γ+βλ)​eλ​(T−t)−1λ−βλ​(T−t),\displaystyle\left(\gamma+\dfrac{\beta}{\lambda}\right)\dfrac{e^{\lambda(T-t)}-1}{\lambda}-\dfrac{\beta}{\lambda}(T-t), |  | (C14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼t,γ​[∫tTΓs2​ds]=\displaystyle\mathbb{E}^{t,\gamma}\left[\int\_{t}^{T}\Gamma\_{s}^{2}\mathrm{d}s\right]= | (γ+βλ)2​e2​λ​(T−t)−12​λ−2​(γ+βλ)​(βλ)​eλ​(T−t)−1λ+(βλ)2​(T−t)\displaystyle\left(\gamma+\dfrac{\beta}{\lambda}\right)^{2}\dfrac{e^{2\lambda(T-t)}-1}{2\lambda}-2\left(\gamma+\dfrac{\beta}{\lambda}\right)\left(\dfrac{\beta}{\lambda}\right)\dfrac{e^{\lambda(T-t)}-1}{\lambda}+\left(\dfrac{\beta}{\lambda}\right)^{2}(T-t) |  | (C15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫tT𝐏¯​(u)​(𝚺~𝐒​𝚺~𝐒⊤)−1​𝐏¯​(u)⊤​e2​λ​(T−u)−12​λ​du,\displaystyle+\int\_{t}^{T}\mathbf{\bar{P}}(u)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\mathbf{\bar{P}}(u)^{\top}\dfrac{e^{2\lambda(T-u)}-1}{2\lambda}\mathrm{d}u, |  | (C16) |

for every t∈[0,T]t\in[0,T], respectively. By inserting equations ([C14](https://arxiv.org/html/2511.19186v1#A3.E14 "In C.4 Proof of Corollary 5.7 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and ([C16](https://arxiv.org/html/2511.19186v1#A3.E16 "In C.4 Proof of Corollary 5.7 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) into ([C13](https://arxiv.org/html/2511.19186v1#A3.E13 "In C.4 Proof of Corollary 5.7 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and rearranging the
terms, we obtain the value function V~\tilde{V} in equation equation ([5.38](https://arxiv.org/html/2511.19186v1#S5.E38 "In Corollary 5.7. ‣ Logarithmic case. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). This concludes the proof.

### C.5 Proof of Proposition [5.8](https://arxiv.org/html/2511.19186v1#S5.Thmthm8 "Proposition 5.8. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

Applying the definition of LtL\_{t} for the CRRA utility case, we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=𝔼c​[v^​(t,C^t,Yt)−V^​(t,C^,Γt)|ℱt]=c1−δ1−δ​(𝔼​[ef^​(t)2​Yt+g^​(t)​Yt+h^​(t)|ℱt]−ef¯​(t)2​Yt+g¯​(t)​Yt+h¯​(t)).L\_{t}=\mathbb{E}^{c}\left[\hat{v}(t,\hat{C}\_{t},Y\_{t})-\hat{V}(t,\hat{C},\Gamma\_{t})|\mathcal{F}\_{t}\right]=\dfrac{c^{1-\delta}}{1-\delta}\left(\mathbb{E}\left[e^{\frac{\hat{f}(t)}{2}Y\_{t}+\hat{g}(t)Y\_{t}+\hat{h}(t)}|\mathcal{F}\_{t}\right]-e^{\frac{\bar{f}(t)}{2}Y\_{t}+\bar{g}(t)Y\_{t}+\bar{h}(t)}\right). |  | (C17) |

Since, Yt|ℱt∼N​(Γt,Pt)Y\_{t}|\mathcal{F}\_{t}\sim N(\Gamma\_{t},P\_{t}), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ef^​(t)2​Yt+g^​(t)​Yt+h^​(t)|ℱt]=eh^​(t)+12​g^2​(t)​P​(t)1−f^​(t)​P​(t)+g^​(t)​Γt1−f^​(t)​P​(t)+12​f^​(t)​Γt21−f^​(t)​P​(t)1−P​(t)​f^​(t),t∈[0,T].\mathbb{E}\left[e^{\frac{\hat{f}(t)}{2}Y\_{t}+\hat{g}(t)Y\_{t}+\hat{h}(t)}|\mathcal{F}\_{t}\right]=\frac{e^{\hat{h}(t)+\frac{1}{2}\frac{\hat{g}^{2}(t)P(t)}{1-\hat{f}(t)P(t)}+\frac{\hat{g}(t)\Gamma\_{t}}{1-\hat{f}(t)P(t)}+\frac{1}{2}\frac{\hat{f}(t)\Gamma^{2}\_{t}}{1-\hat{f}(t)P(t)}}}{\sqrt{1-P(t)\hat{f}(t)}},\quad t\in[0,T]. |  | (C18) |

It is worth noting that the above expression is well defined because 1−P​(t)​f^​(t)>01-P(t)\hat{f}(t)>0 for every t∈[0,T]t\in[0,T] (see Theorem [5.3](https://arxiv.org/html/2511.19186v1#S5.Thmthm3 "Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). Inserting ([C18](https://arxiv.org/html/2511.19186v1#A3.E18 "In C.5 Proof of Proposition 5.8 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) into ([C17](https://arxiv.org/html/2511.19186v1#A3.E17 "In C.5 Proof of Proposition 5.8 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) and using ([5.22](https://arxiv.org/html/2511.19186v1#S5.E22 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([5.23](https://arxiv.org/html/2511.19186v1#S5.E23 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), and ([5.25](https://arxiv.org/html/2511.19186v1#S5.E25 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) yields the result in equation ([5.42](https://arxiv.org/html/2511.19186v1#S5.E42 "In Proposition 5.8. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). Applying the definition of efficiency (see equation ([5.41](https://arxiv.org/html/2511.19186v1#S5.E41 "In 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"))), ξ\xi can be found by solving the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ1−δ1−δ​𝔼​[ef^​(0)2​Y02+g^​(0)​Y0+h^​(0)|ℱ0]=11−δ​ef¯​(0)2​Γ02+g¯​(0)​Γ0+h¯​(0).\dfrac{\zeta^{1-\delta}}{1-\delta}\mathbb{E}\left[e^{\frac{\hat{f}(0)}{2}Y^{2}\_{0}+\hat{g}(0)Y\_{0}+\hat{h}(0)}|\mathcal{F}\_{0}\right]=\dfrac{1}{1-\delta}e^{\frac{\bar{f}(0)}{2}\Gamma^{2}\_{0}+\bar{g}(0)\Gamma\_{0}+\bar{h}(0)}. |  | (C19) |

Using ([C18](https://arxiv.org/html/2511.19186v1#A3.E18 "In C.5 Proof of Proposition 5.8 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) together with ([5.22](https://arxiv.org/html/2511.19186v1#S5.E22 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), ([5.23](https://arxiv.org/html/2511.19186v1#S5.E23 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), and ([5.25](https://arxiv.org/html/2511.19186v1#S5.E25 "In Theorem 5.3. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), the foregoing equation can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ1−δ​e1−δ2​∫0TP​(s)1−P​(s)​f^​(s)​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]​𝚯^−1​[𝚺~Y​𝚺~𝐒⊤​f^​(s)+𝐚⊤]⊤​ds=1.\zeta^{1-\delta}e^{\frac{1-\delta}{2}\int\_{0}^{T}\frac{P(s)}{1-P(s)\hat{f}(s)}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]\mathbf{\hat{\Theta}}^{-1}\left[\bm{\tilde{\Sigma}}\_{Y}\bm{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\hat{f}(s)+\mathbf{a}^{\top}\right]^{\top}\mathrm{d}s}=1. |  | (C20) |

Hence, the result in ([5.43](https://arxiv.org/html/2511.19186v1#S5.E43 "In Proposition 5.8. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) immediately follows. This concludes the proof.

### C.6 Proof of Corollary [5.9](https://arxiv.org/html/2511.19186v1#S5.Thmthm9 "Proposition 5.9. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")

Applying the definition of LtL\_{t} for the logarithmic utility case, noticing that 𝔼​[Yt2|ℱt]=Γt2+P​(t)\mathbb{E}[Y\_{t}^{2}|\mathcal{F}\_{t}]=\Gamma\_{t}^{2}+P(t), and using equation ([5.39](https://arxiv.org/html/2511.19186v1#S5.E39 "In Corollary 5.7. ‣ Logarithmic case. ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=𝐚⊤​𝚯−1​𝐚4​λ​[ϕ​(t)​P​(t)+σY2​(ϕ​(t)2​λ−(T−t))−∫tT𝐏¯​(s)​(𝚺~𝐒​𝚺~𝐒⊤)−1​𝐏¯​(s)⊤​ϕ​(s)​ds],L\_{t}=\frac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{4\lambda}\left[\phi(t)P(t)+\sigma\_{Y}^{2}\left(\frac{\phi(t)}{2\lambda}-\left(T-t\right)\right)-\int\_{t}^{T}\mathbf{\bar{P}}(s)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\mathbf{\bar{P}}(s)^{\top}\phi(s)\mathrm{d}s\right], |  | (C21) |

where ϕ​(t):=e2​λ​(T−t)−1\phi(t):=e^{2\lambda(T-t)}-1, for every t∈[0,T]t\in[0,T]. Since,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tTϕ​(s)​dP​(s)=∫tTϕ​(s)​(2​λ​P​(s)+σY2)−∫tT𝐏¯​(s)​(𝚺~𝐒​𝚺~𝐒⊤)−1​𝐏¯​(s)⊤​ϕ​(s)​ds,t∈[0,T],\int\_{t}^{T}\phi(s)\mathrm{d}P(s)=\int\_{t}^{T}\phi(s)\left(2\lambda P(s)+\sigma\_{Y}^{2}\right)-\int\_{t}^{T}\mathbf{\bar{P}}(s)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\mathbf{\bar{P}}(s)^{\top}\phi(s)\mathrm{d}s,\quad t\in[0,T], |  | (C22) |

we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tT𝐏¯​(s)​(𝚺~𝐒​𝚺~𝐒⊤)−1​𝐏¯​(s)⊤​ϕ​(s)​ds=∫tTϕ​(s)​(2​λ​P​(s)+σY2)​ds−∫tTϕ​(s)​dP​(s),\displaystyle\int\_{t}^{T}\mathbf{\bar{P}}(s)\left(\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}\mathbf{\tilde{\Sigma}}\_{\mathbf{S}}^{\top}\right)^{-1}\mathbf{\bar{P}}(s)^{\top}\phi(s)\mathrm{d}s=\int\_{t}^{T}\phi(s)\left(2\lambda P(s)+\sigma\_{Y}^{2}\right)\mathrm{d}s-\int\_{t}^{T}\phi(s)\mathrm{d}P(s), |  | (C23) |

for every t∈[0,T]t\in[0,T]. Inserting equation ([C23](https://arxiv.org/html/2511.19186v1#A3.E23 "In C.6 Proof of Corollary 5.9 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) into ([C21](https://arxiv.org/html/2511.19186v1#A3.E21 "In C.6 Proof of Corollary 5.9 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")), we obtain the expression for the loss of utility stated in ([5.44](https://arxiv.org/html/2511.19186v1#S5.E44 "In Proposition 5.9. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")). Applying the definition of efficiency (see equation ([5.41](https://arxiv.org/html/2511.19186v1#S5.E41 "In 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information"))), ξ\xi can be found by solving the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[v​(0,ζ,Y0)−V~​(0,1,Γ0)|ℱ0]=0.\mathbb{E}\left[v(0,\zeta,Y\_{0})-\tilde{V}(0,1,\Gamma\_{0})|\mathcal{F}\_{0}\right]=0. |  | (C24) |

Following the same steps used to derive the loss of utility, equation ([C24](https://arxiv.org/html/2511.19186v1#A3.E24 "In C.6 Proof of Corollary 5.9 ‣ Appendix C Proofs of some technical results of Section 5 ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(ζ)+𝐚⊤​𝚯−1​𝐚2​∫0TP​(s)​ds=0.\log(\zeta)+\frac{\mathbf{a}^{\top}\mathbf{\Theta}^{-1}\mathbf{a}}{2}\int\_{0}^{T}P(s)\mathrm{d}s=0. |  | (C25) |

Hence, the result in ([5.45](https://arxiv.org/html/2511.19186v1#S5.E45 "In Proposition 5.9. ‣ 5.1 Loss of utility ‣ 5 Optimisation problem under partial information ‣ Carbon-Penalised Portfolio Insurance Strategies in a Stochastic Factor Model with Partial Information")) immediately follows. This concludes the proof.

## References

* Andersson et al. [2016]

  M. Andersson, P. Bolton, and F. Samama.
  Hedging climate risk.
  *Financial Analysts Journal*, 72(3):13–32,
  2016.
* Anquetin et al. [2022]

  T. Anquetin, G. Coqueret, B. Tavin, and L. Welgryn.
  Scopes of carbon emissions and their impact on green portfolios.
  *Economic modelling*, 115:105951, 2022.
* Ardia et al. [2023]

  D. Ardia, K. Bluteau, G. Lortie-Cloutier, and T.D. Tran.
  Factor exposure heterogeneity in green and brown stocks.
  *Finance Research Letters*, 55:103900, 2023.
* Basak [2002]

  S. Basak.
  A comparative study of portfolio insurance.
  *Journal of Economic Dynamics and Control*, 26(7-8):1217–1241, 2002.
* Bolton et al. [2022]

  P. Bolton, M. Kacperczyk, and F. Samama.
  Net-zero carbon portfolio alignment.
  *Financial Analysts Journal*, 78(2):19–33,
  2022.
* Bolton et al. [2024]

  P. Bolton, M.T. Kacperczyk, H.L. Rasmussen, and F. Samama.
  Reconciling Portfolio Diversification with a Shrinking Carbon
  Footprint.
  Technical report, CFA Institute Research and Policy Center, 2024.
  URL
  <https://rpc.cfainstitute.org/research/reports/2024/reconciling-portfolio-diversification-with-shrinking-carbon-footprint>.
* Brendle [2006]

  S. Brendle.
  Portfolio selection under incomplete information.
  *Stochastic processes and their Applications*, 116(5):701–723, 2006.
* Brennan and Schwartz [1976]

  M.J. Brennan and E.S. Schwartz.
  The pricing of equity-linked life insurance policies with an asset
  value guarantee.
  *Journal of Financial Economics*, 3(3):195–213, 1976.
* Colaneri et al. [2025]

  K. Colaneri, A. Cretarola, E. Lombardo, and D. Mancinelli.
  Design and hedging of unit linked life insurance with environmental
  factors.
  *arXiv preprint arXiv:2509.05676*, 2025.
* De Spiegeleer et al. [2023]

  J. De Spiegeleer, S. Höcht, D. Jakubowski, S. Reyners, and W. Schoutens.
  ESG: A new dimension in portfolio allocation.
  *Journal of Sustainable Finance and Investment*, 13(2):827–867, 2023.
* Di Giacinto et al. [2024]

  M. Di Giacinto, D. Mancinelli, M. Marino, and I. Oliva.
  Pension funds with longevity risk: an optimal portfolio insurance
  approach.
  *Insurance: Mathematics and Economics*, 119:268–297,
  2024.
* Escobar-Anel [2022]

  M. Escobar-Anel.
  Multivariate risk aversion utility, application to ESG investments.
  *The North American Journal of Economics and Finance*,
  63:101790, 2022.
* Görgen et al. [2020]

  M. Görgen, A. Jacob, M. Nerlinger, R. Riordan, M. Rohleder, and M. Wilkens.
  Carbon risk.
  *Working paper*, 2020.
* Grossman and Villa [1989]

  S.J. Grossman and J.L. Villa.
  Portfolio insurance in complete markets: A note.
  *Journal of Business*, 62(4):473–476, 1989.
* Hartzmark and Sussman [2019]

  S.M. Hartzmark and A.B. Sussman.
  Do investors value sustainability? A natural experiment examining
  ranking and fund flows.
  *The Journal of Finance*, 74(6):2789–2837,
  2019.
* Hellmich and Kiesel [2021]

  M. Hellmich and R. Kiesel.
  *Carbon Finance: A Risk Management View*.
  World Scientific, 2021.
* Lagerkvist et al. [2020]

  C.J. Lagerkvist, A.K. Edenbrandt, I. Tibbelin, and Y. Wahlstedt.
  Preferences for sustainable and responsible equity funds - A choice
  experiment with Swedish private investors.
  *Journal of Behavioral and Experimental Finance*, 28:100406, 2020.
* Le Guenedal and Roncalli [2023]

  T. Le Guenedal and T. Roncalli.
  Portfolio construction with climate risk measures.
  In *Climate Investing: New Strategies and Implementation
  Challenges*, pages 49–86. Emmanuel Jurczenko, Wiley, 2023.
* Lee and Papanicolaou [2016]

  S. Lee and A. Papanicolaou.
  Pairs trading of two assets with uncertainty in co-integration’s
  level of mean reversion.
  *International Journal of Theoretical and Applied Finance*,
  19(8):1650054, 2016.
* Liptser and Shiryaev [2013]

  R.S. Liptser and A.N. Shiryaev.
  *Statistics of random processes: I. General theory*, volume 5.
  Springer Science & Business Media, 2013.
* Pástor et al. [2021]

  L. Pástor, R.F. Stambaugh, and L.A. Taylor.
  Sustainable investing in equilibrium.
  *Journal of financial economics*, 142(2):550–571, 2021.
* Peng et al. [2024]

  F. Peng, M. Yan, and S. Zhang.
  Optimal investment of defined contribution pension plan with
  environmental, social, and governance (ESG) factors in regime-switching
  jump diffusion models.
  *Communications in Statistics-Theory and Methods*, pages 1–27,
  2024.
* Rogers [2001]

  L.C.G. Rogers.
  The relaxed investor and parameter uncertainty.
  *Finance and stochastics*, 5:131–154, 2001.
* Rogers [2013]

  L.C.G. Rogers.
  *Optimal investment*.
  Berlin, Heidelberg: Springer-Verlag, 2013.
* Rubinstein and Leland [1976]

  M. Rubinstein and H.E. Leland.
  The evolution of portfolio insurance.
  *D. Luskin (Szerk.), Dynamic Hedging: A Guide to Portfolio
  Insurance. John Wiley and Sons*, 1976.
* Sass et al. [2017]

  J. Sass, D. Westphal, and R. Wunderlich.
  Expert opinions and logarithmic utility maximization for multivariate
  stock returns with gaussian drift.
  *International Journal of Theoretical and Applied Finance*,
  20(04):1750022, 2017.
* Temocin et al. [2018]

  B.Z. Temocin, R. Korn, and A.S. Selcuk-Kestel.
  Constant proportion portfolio insurance in defined contribution
  pension plan management.
  *Annals of Operations Research*, 266(1):329–348, 2018.
* Zieling et al. [2014]

  D. Zieling, A. Mahayni, and S. Balder.
  Performance evaluation of optimized portfolio insurance strategies.
  *Journal of Banking and Finance*, 43:212–225, 2014.