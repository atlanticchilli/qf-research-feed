---
authors:
- Giuseppe Brandi
- Tiziana Di Matteo
doc_id: arxiv:2601.11305v1
family_id: arxiv:2601.11305
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Multiscaling in the Rough Bergomi Model: A Tale of Tails'
url_abs: http://arxiv.org/abs/2601.11305v1
url_html: https://arxiv.org/html/2601.11305v1
venue: arXiv q-fin
version: 1
year: 2026
---


Giuseppe Brandi
Corresponding authors: Giuseppe Brandi ([giuseppe.brandi@nulondon.ac.uk](mailto:giuseppe.brandi@nulondon.ac.uk)), Tiziana Di Matteo ([tiziana.di\_matteo@kcl.ac.uk](mailto:tiziana.di_matteo@kcl.ac.uk))
CoMENS, Northeastern University London, London, UK

T. Di Matteo
CoMENS, Northeastern University London, London, UK
Complexity Science Hub Vienna, Vienna, Austria
Centro Ricerche Enrico Fermi, Via Panisperna 89 A, Rome, Italy

###### Abstract

The rough Bergomi (rBergomi) model, characterised by its roughness parameter HH, has been shown to exhibit multiscaling behaviour as HH approaches zero. Multiscaling has profound implications for financial modelling: it affects extreme risk estimation, influences optimal portfolio allocation across different time horizons, and challenges traditional option pricing approaches that assume uniscaling behaviours. Understanding whether multiscaling arises primarily from the roughness of volatility paths or from the resulting fat-tailed returns has important implications for financial modelling, option pricing, and risk management. This paper investigates the real source of this multiscaling behaviour by introducing a novel two-stage statistical testing procedure. In the first stage, we establish the presence of multiscaling in the rBergomi model against an uniscaling fractional Brownian motion process. We quantify multiscaling by using weighted least squares regression that accounts for heteroscedastic estimation errors across moments. In the second stage, we apply shuffled surrogates that preserve return distributions while destroying temporal correlations. This is done by using distance-based permutation tests robust to asymmetric null distributions. In order to validate our procedure, we check the robustness of the results by using synthetic processes with known multifractal properties, namely the Multifractal Random Walk (MRW) and the Fractional Lévy Stable Motion (FLSM). We provide compelling evidence that multiscaling in the rBergomi model arises primarily from fat-tailed return distributions rather than memory effects. Our findings suggest that the apparent multiscaling in rough volatility models is largely attributable to distributional properties rather than genuine temporal scaling behaviour.

Keywords— R
ough volatility; Multiscaling; Generalised Hurst exponent; Surrogate data testing

JEL Classification—
C58; C22; C12; C15; G12

## 1 Introduction

The advent of rough volatility models has significantly transformed financial modelling in recent years, offering superior fits to both implied volatility surfaces and historical time series data (Gatheral et al., [2018](https://arxiv.org/html/2601.11305v1#bib.bib1 "Volatility is rough"); Bennedsen et al., [2022](https://arxiv.org/html/2601.11305v1#bib.bib15 "Decoupling the short- and long-term behavior of stochastic volatility")). These models, characterised by volatility paths with low regularity, have gained attention for their ability to capture both the stylised facts of asset returns and the empirical features of option markets. The roughness of volatility was initially identified through the analysis of realised volatility time series, with empirical studies consistently finding Hurst parameters well below 0.5 (Gatheral et al., [2018](https://arxiv.org/html/2601.11305v1#bib.bib1 "Volatility is rough"); Fukasawa, [2021](https://arxiv.org/html/2601.11305v1#bib.bib29 "Volatility has to be rough")).

Among these models, the rough Bergomi (rBergomi) model introduced by Bayer et al. ([2016](https://arxiv.org/html/2601.11305v1#bib.bib10 "Pricing under rough volatility")) has emerged as a prominent framework. It incorporates fractional Brownian motion with Hurst parameter H<1/2H<1/2 to generate rough volatility paths. As the roughness parameter HH approaches zero, the volatility process becomes increasingly irregular, better matching the observed characteristics of financial markets. The model’s success in capturing market behaviour has been demonstrated through various applications, including option pricing (Bayer et al., [2020](https://arxiv.org/html/2601.11305v1#bib.bib30 "Pricing american options by exercise rate optimization"); McCrickerd and Pakkanen, [2018](https://arxiv.org/html/2601.11305v1#bib.bib31 "Turbocharging monte carlo pricing for the rough bergomi model")), VIX derivatives (Jacquier et al., [2018](https://arxiv.org/html/2601.11305v1#bib.bib20 "On vix futures in the rough bergomi model"); Bonesini et al., [2023](https://arxiv.org/html/2601.11305v1#bib.bib32 "Functional quantization of rough volatility and applications to the vix")), and portfolio optimization under rough volatility (Abi Jaber et al., [2021](https://arxiv.org/html/2601.11305v1#bib.bib33 "Markowitz portfolio selection for multivariate affine and quadratic volterra models")).

The theoretical foundations of rough volatility have been further developed through connections with market microstructure. El Euch et al. ([2018](https://arxiv.org/html/2601.11305v1#bib.bib34 "The microstructural foundations of leverage effect and rough volatility")) and Jusselin and Rosenbaum ([2020](https://arxiv.org/html/2601.11305v1#bib.bib35 "No-arbitrage implies power-law market impact and rough volatility")) demonstrated that rough volatility naturally emerges from Hawkes process models of market activity, providing a microscopic foundation for the observed roughness. More recently, Horst et al. ([2023](https://arxiv.org/html/2601.11305v1#bib.bib36 "Convergence of heavy-tailed hawkes processes and the microstructure of rough volatility")) showed how heavy-tailed Hawkes processes converge to rough volatility models, establishing a direct link between market microstructure and the empirical properties of volatility. The universal nature of volatility formation has been explored by Rosenbaum and Zhang ([2022](https://arxiv.org/html/2601.11305v1#bib.bib37 "On the universality of the volatility formation process: when machine learning and rough volatility agree")), who demonstrated that machine learning approaches independently recover the rough volatility paradigm from market data.

Several studies have explored how rough volatility models affect option pricing, particularly for exotic derivatives. Alòs et al. ([2022](https://arxiv.org/html/2601.11305v1#bib.bib38 "On smile properties of volatility derivatives and exotic products: understanding the vix skew")) investigated the smile properties of volatility derivatives under rough volatility, while Horváth et al. ([2020](https://arxiv.org/html/2601.11305v1#bib.bib39 "Volatility options in rough volatility models")) examined the pricing of volatility options in rough volatility models. The impact on implied volatility surfaces has been studied extensively, with Fukasawa ([2022](https://arxiv.org/html/2601.11305v1#bib.bib40 "On asymptotically arbitrage-free approximations of the implied volatility")) providing asymptotic expansions and Friz and Gatheral ([2022](https://arxiv.org/html/2601.11305v1#bib.bib41 "Diamonds and forward variance models")) developing forward variance models that capture the rough volatility dynamics.

Recent advances in numerical methods have made the implementation of rough volatility models more practical. Bayer et al. ([2022](https://arxiv.org/html/2601.11305v1#bib.bib42 "Weak error rates for option pricing under linear rough volatility")) developed weak error rates for option pricing under linear rough volatility, while Bourgey and De Marco ([2021](https://arxiv.org/html/2601.11305v1#bib.bib43 "Multilevel monte carlo simulation for vix options in the rough bergomi model")) introduced multilevel Monte Carlo methods for the rough Bergomi model. Machine learning approaches have also been applied, with Bayer et al. ([2025](https://arxiv.org/html/2601.11305v1#bib.bib44 "On deep calibration of (rough) stochastic volatility models")) using deep learning for calibration and Jacquier and Zuric ([2023](https://arxiv.org/html/2601.11305v1#bib.bib45 "Random neural networks for rough volatility")) employing random neural networks for rough volatility modelling.

A particularly intriguing property observed in both empirical studies and theoretical analyses is that the rBergomi model exhibits multiscaling behaviour, especially for small values of HH (Brandi and Di Matteo, [2022a](https://arxiv.org/html/2601.11305v1#bib.bib16 "Multiscaling and rough volatility: an empirical investigation"); Comte and Renault, [2012](https://arxiv.org/html/2601.11305v1#bib.bib18 "Affine fractional stochastic volatility models"); Forde et al., [2022](https://arxiv.org/html/2601.11305v1#bib.bib14 "The riemann–liouville field and its gmc as →H0, and skew flattening for the rough bergomi model")). Multiscaling implies that different moments of price changes scale with different exponents, contradicting the simple scaling found in classical Brownian motion models. This property has been interpreted as evidence of complex dynamics in financial markets that go beyond standard diffusion processes. The presence of multiscaling in financial markets was initially proposed by Mandelbrot et al. ([1997](https://arxiv.org/html/2601.11305v1#bib.bib21 "A multifractal model of asset returns")) and has since been documented across various asset classes and markets (Calvet and Fisher, [2002](https://arxiv.org/html/2601.11305v1#bib.bib22 "Multifractality in asset returns: theory and evidence"); Di Matteo et al., [2003](https://arxiv.org/html/2601.11305v1#bib.bib2 "Scaling behaviors in differently developed markets"); Green et al., [2014](https://arxiv.org/html/2601.11305v1#bib.bib8 "The origins of multifractality in financial time series and the effect of extreme events"); Zhou, [2009](https://arxiv.org/html/2601.11305v1#bib.bib7 "The components of empirical multifractality in financial returns"); Barunik et al., [2012](https://arxiv.org/html/2601.11305v1#bib.bib6 "Understanding the source of multifractality in financial markets"); Buonocore et al., [2016](https://arxiv.org/html/2601.11305v1#bib.bib5 "Measuring multiscaling in financial time-series"); Kantelhardt et al., [2002](https://arxiv.org/html/2601.11305v1#bib.bib3 "Multifractal detrended fluctuation analysis of nonstationary time series"); Buonocore et al., [2020](https://arxiv.org/html/2601.11305v1#bib.bib9 "On the interplay between multiscaling and stock dependence"); Di Matteo, [2007](https://arxiv.org/html/2601.11305v1#bib.bib23 "Multi-scaling in finance"); Luitz et al., [2020](https://arxiv.org/html/2601.11305v1#bib.bib28 "Multifractality and its role in anomalous transport in the disordered xxz spin-chain")).
The results of our investigation have significant implications for financial modelling, option pricing, and risk management. They contribute to the ongoing debate about the nature of financial market complexity and the appropriate mathematical frameworks for capturing this complexity, building on the foundational work of Gatheral et al. ([2018](https://arxiv.org/html/2601.11305v1#bib.bib1 "Volatility is rough")) and extending it to address the fundamental question of whether rough volatility models capture genuine temporal complexity of asset returns or primarily reflect distributional phenomena.
Indeed, the relationship between rough volatility and multiscaling has important implications for derivative pricing and risk management.

However, despite these theoretical and computational advances, a fundamental question remains open: what is the primary source of the multiscaling behaviour observed in rough volatility models? The literature has identified three potential sources of multiscaling. First, multiscaling can arise solely from fat-tailed (non-Gaussian) distributions, with temporal structure playing no essential role beyond creating these distributional properties (Zhou, [2009](https://arxiv.org/html/2601.11305v1#bib.bib7 "The components of empirical multifractality in financial returns")). Second, multiscaling can emerge purely from complex memory structures and temporal dependencies, even in the absence of fat tails, as demonstrated in long-range correlated Gaussian processes (Green et al., [2014](https://arxiv.org/html/2601.11305v1#bib.bib8 "The origins of multifractality in financial time series and the effect of extreme events")). Third, multiscaling can result from the combination of both distributional effects and temporal dependencies, where fat tails and memory contribute together to the scaling behaviour (Stanley, [2003](https://arxiv.org/html/2601.11305v1#bib.bib4 "Statistical physics and economic fluctuations: do outliers exist?")). While all three mechanisms are theoretically possible, distinguishing between them requires careful statistical methodology.

The distinction between these hypotheses has profound implications. Recent work by Chong et al. ([2024](https://arxiv.org/html/2601.11305v1#bib.bib46 "Statistical inference for rough volatility: central limit theorems")) on statistical inference for rough volatility has highlighted the importance of understanding the sources of apparent roughness, while Fukasawa et al. ([2019](https://arxiv.org/html/2601.11305v1#bib.bib47 "Is volatility rough?")) questioned whether volatility truly needs to be rough or whether distributional effects could explain the observed phenomena. The debate extends to the interpretation of market efficiency and the nature of price formation processes, as discussed in Gatheral et al. ([2020](https://arxiv.org/html/2601.11305v1#bib.bib48 "The quadratic rough heston model and the joint s&p 500/vix smile calibration problem")) in the context of the quadratic rough Heston model.

This paper presents a systematic investigation of this question, using surrogate data methods to isolate the contributions of distributional properties and memory effects to the observed multiscaling in the rBergomi model (Zhou, [2009](https://arxiv.org/html/2601.11305v1#bib.bib7 "The components of empirical multifractality in financial returns")). Through statistical testing, we aim to determine whether the multiscaling observed in rough volatility models is simply an artefact of their distributional characteristics or if it also reflects genuine temporal complexities. Our approach involves two key steps: first, we establish the presence of multiscaling in the rBergomi model using appropriate benchmark processes; second, we apply surrogate data techniques to disentangle distributional and temporal sources of multiscaling.

The remainder of this paper is structured as follows. Section 2 introduces the rough Bergomi model and discusses its key properties, with particular emphasis on the role of the roughness parameter HH. Section 3 presents the generalised Hurst exponent framework for quantifying multiscaling behaviour in financial time series. Section 4 develops our statistical methodology, including surrogate data generation techniques and hypothesis testing procedures for identifying the source of multiscaling. Section 5 presents our main results for the rough Bergomi model across different roughness regimes, along with robustness checks using synthetic models with known multifractal properties. Section 7 concludes.

## 2 The Rough Bergomi Model

The rough Bergomi model extends the standard stochastic volatility framework by incorporating fractional Brownian motion to generate rough volatility paths Gatheral et al. ([2018](https://arxiv.org/html/2601.11305v1#bib.bib1 "Volatility is rough")); Bayer et al. ([2016](https://arxiv.org/html/2601.11305v1#bib.bib10 "Pricing under rough volatility")); Brandi and Di Matteo ([2022a](https://arxiv.org/html/2601.11305v1#bib.bib16 "Multiscaling and rough volatility: an empirical investigation")). The model is characterised by the following dynamics for the asset price process StS\_{t} and the instantaneous variance process vtv\_{t}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​StSt\displaystyle\frac{dS\_{t}}{S\_{t}} | =vt​(ρ​d​Wt+1−ρ2​d​Wt⟂)\displaystyle=\sqrt{v\_{t}}\left(\rho dW\_{t}+\sqrt{1-\rho^{2}}dW^{\perp}\_{t}\right) |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vt\displaystyle v\_{t} | =ξ0​exp⁡(η​WtH−12​η2​t2​H),t∈[0,T]\displaystyle=\xi\_{0}\exp\left(\eta W^{H}\_{t}-\frac{1}{2}\eta^{2}t^{2H}\right),\quad t\in[0,T] |  | (2) |

where WtW\_{t} and Wt⟂W^{\perp}\_{t} are independent Brownian motions, WtHW^{H}\_{t} is a fractional Brownian motion with Hurst parameter HH, ρ\rho is the correlation between returns and volatility, η\eta controls the volatility of volatility, and ξ0\xi\_{0} is the initial variance.

The fractional Brownian motion WtHW^{H}\_{t} is a Gaussian process with the following covariance structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[WtH​WsH]=12​(t2​H+s2​H−|t−s|2​H).\mathbb{E}[W^{H}\_{t}W^{H}\_{s}]=\frac{1}{2}(t^{2H}+s^{2H}-|t-s|^{2H}). |  | (3) |

This formulation leads to a volatility process with Hölder regularity of order H−ϵH-\epsilon for any ϵ>0\epsilon>0, making the paths increasingly rough as HH approaches zero.

The rough Bergomi model has gained significant attention in financial mathematics for several key properties. When H<1/2H<1/2, the volatility paths exhibit roughness, with the degree of irregularity increasing as HH decreases. This roughness better captures the empirical properties of realised volatility observed in financial markets (Gatheral et al., [2018](https://arxiv.org/html/2601.11305v1#bib.bib1 "Volatility is rough")). Despite the roughness of individual paths, the model generates long-memory behaviour in volatility autocorrelations, consistent with empirical observations in financial markets (Bennedsen et al., [2022](https://arxiv.org/html/2601.11305v1#bib.bib15 "Decoupling the short- and long-term behavior of stochastic volatility")).

The model produces realistic implied volatility surfaces, particularly capturing the at-the-money skew behaviour observed in options markets (Bayer et al., [2016](https://arxiv.org/html/2601.11305v1#bib.bib10 "Pricing under rough volatility"); Jacquier et al., [2018](https://arxiv.org/html/2601.11305v1#bib.bib20 "On vix futures in the rough bergomi model")). Additionally, the stochastic volatility framework naturally generates returns with heavier tails than Gaussian distributions, another stylised fact of financial time series (Cont, [2001](https://arxiv.org/html/2601.11305v1#bib.bib19 "Empirical properties of asset returns: stylized facts and statistical issues")).

These properties make the rough Bergomi model valuable for applications including option pricing, risk management, and volatility forecasting. The model has been particularly successful in capturing the term structure of volatility skew observed in equity and index options.

The roughness parameter HH plays a crucial role in determining the behaviour of the volatility process. Empirical estimates of HH typically fall in the range of 0.05 to 0.15, significantly below the value of 0.5 that would correspond to standard Brownian motion (Gatheral et al., [2018](https://arxiv.org/html/2601.11305v1#bib.bib1 "Volatility is rough")).

As HH approaches zero, several notable effects occur: the volatility paths become increasingly irregular and rough, the return distribution becomes more heavy-tailed, and the model exhibits stronger multiscaling behaviour (Brandi and Di Matteo, [2022a](https://arxiv.org/html/2601.11305v1#bib.bib16 "Multiscaling and rough volatility: an empirical investigation"); Forde et al., [2022](https://arxiv.org/html/2601.11305v1#bib.bib14 "The riemann–liouville field and its gmc as →H0, and skew flattening for the rough bergomi model")).
For our analysis, we generate simulations of the rough Bergomi model with different values of H∈[0.05,0.3]H\in[0.05,0.3], fixing other parameters to empirically relevant values: ξ0=0.1\xi\_{0}=0.1 (initial variance), ρ=−0.9\rho=-0.9 (correlation between returns and volatility), and η=1.9\eta=1.9 (volatility of volatility). These parameter choices align with calibrations to market data conducted in previous studies (Bayer et al., [2016](https://arxiv.org/html/2601.11305v1#bib.bib10 "Pricing under rough volatility"); Gatheral et al., [2018](https://arxiv.org/html/2601.11305v1#bib.bib1 "Volatility is rough")).
Figure [1](https://arxiv.org/html/2601.11305v1#S2.F1 "Figure 1 ‣ 2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") reports these effects by showing simulated price paths, return distributions, and volatility dynamics for three representative values of HH.

![Refer to caption](rBergomi.png)


Figure 1: Rough Bergomi model characteristics for different values of HH. Top row: Simulated price paths StS\_{t} over 10000 observations. Middle row: Discrete returns rt=St−St−1r\_{t}=S\_{t}-S\_{t-1} computed from the price process. Bottom row: Realised volatility vt\sqrt{v\_{t}} where vtv\_{t} is the instantaneous variance process. Parameters: ξ0=0.1\xi\_{0}=0.1 (initial variance), ρ=−0.9\rho=-0.9 (correlation between returns and volatility), η=1.9\eta=1.9 (volatility of volatility). As HH decreases, price paths become more irregular, return distributions develop heavier tails, and volatility exhibits more pronounced clustering and roughness.

As evident from Figure [1](https://arxiv.org/html/2601.11305v1#S2.F1 "Figure 1 ‣ 2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"), decreasing the roughness parameter HH leads to three key effects. First, price paths become increasingly irregular with more frequent and pronounced jumps. Second, return distributions develop substantially heavier tails, departing further from the Gaussian benchmark. Third, volatility paths exhibit greater roughness and more extreme clustering, characteristic of the empirically observed volatility dynamics in financial markets.

The relationship between these effects, particularly between the heavy-tailed return distribution and the multiscaling behaviour, is the central focus of our investigation. Understanding whether multiscaling arises primarily from the roughness of volatility paths or from the resulting fat-tailed returns has important implications for financial modelling and interpretability.

## 3 Scaling and Multiscaling Analysis in Finance

Multiscaling in financial time series has several important implications that affect practical financial applications. The nonlinear scaling of moments affects the estimation of extreme risks, particularly for longer time horizons (Brandi and Di Matteo, [2022b](https://arxiv.org/html/2601.11305v1#bib.bib17 "On the statistics of scaling exponents and the multiscaling value at risk")). Traditional risk measures that assume simple scaling can significantly underestimate tail risks. In portfolio management, multiscaling affects the relationship between short-term and long-term investment strategies, influencing optimal portfolio allocation across different time horizons (Calvet and Fisher, [2002](https://arxiv.org/html/2601.11305v1#bib.bib22 "Multifractality in asset returns: theory and evidence")). For option pricing, models that incorporate multiscaling can better capture the term structure of implied volatility and improve option pricing accuracy, especially for long-dated options (Bacry et al., [2001a](https://arxiv.org/html/2601.11305v1#bib.bib24 "Multifractal random walk")). The presence of multiscaling has also been interpreted as evidence of market inefficiencies or complex market structures that cannot be captured by standard diffusion models (Lux, [2008](https://arxiv.org/html/2601.11305v1#bib.bib27 "The markov-switching multifractal model of asset returns: GMM estimation and linear forecasting of volatility")). Understanding the true nature of observed multiscaling, whether it reflects genuine temporal complexities or merely distributional characteristics, is therefore crucial for appropriate financial modelling and risk management. Previous studies have documented multiscaling behaviour in empirical financial time series across various markets and instruments (Di Matteo, [2007](https://arxiv.org/html/2601.11305v1#bib.bib23 "Multi-scaling in finance"); Luitz et al., [2020](https://arxiv.org/html/2601.11305v1#bib.bib28 "Multifractality and its role in anomalous transport in the disordered xxz spin-chain")). However, the question of whether this observed multiscaling arises from complex temporal dependencies or from the heavy-tailed nature of return distributions remains debated.

Throughout this paper, we use standard notation conventions: X​(t)X(t) denotes a continuous-time stochastic process, while XtX\_{t} represents discrete observations in practical implementations. When analysing general time series, we use XX to denote an arbitrary process, whereas SS specifically refers to the asset price process in the rough Bergomi model. In our empirical analysis, the general methods developed for process XX are applied to the specific case of the rough Bergomi log-price process s=l​o​g​Ss=logS.

### 3.1 Generalised Hurst Exponent (GHE) Framework

For a process X​(t)X(t) with stationary increments rτ​(t)=X​(t+τ)−X​(t)r\_{\tau}(t)=X(t+\tau)-X(t) at time aggregation τ\tau, the GHE methodology examines how the qq-th order moment of absolute returns scales with the time aggregation (Di Matteo, [2007](https://arxiv.org/html/2601.11305v1#bib.bib23 "Multi-scaling in finance")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|rτ​(t)|q]∼Kq​τq​H​(q).\mathbb{E}\left[|r\_{\tau}(t)|^{q}\right]\sim K\_{q}\tau^{qH(q)}. |  | (4) |

Two broad classes of scaling behaviour can be distinguished. For uniscaling time series, H​(q)H(q) is constant for all qq, meaning all moments scale with the same exponent (e.g., Brownian motion, fractional Brownian motion), while for multiscaling time series, H​(q)H(q) varies with qq, indicating a more complex structure associated with intermittency and heterogeneous volatility. Such behaviour was first proposed for financial markets by Mandelbrot et al. ([1997](https://arxiv.org/html/2601.11305v1#bib.bib21 "A multifractal model of asset returns")) and has since been widely observed (Calvet and Fisher, [2002](https://arxiv.org/html/2601.11305v1#bib.bib22 "Multifractality in asset returns: theory and evidence"); Di Matteo, [2007](https://arxiv.org/html/2601.11305v1#bib.bib23 "Multi-scaling in finance")). To quantify multiscaling, we employ the GHE framework (Di Matteo, [2007](https://arxiv.org/html/2601.11305v1#bib.bib23 "Multi-scaling in finance")). This approach examines how different statistical moments scale with the time aggregation τ\tau.

For a time series X​(t)X(t), we compute the qq-th order moments of absolute returns over different time horizons τ∈[τm​i​n,τm​a​x]\tau\in[\tau\_{min},\tau\_{max}]111τm​i​n\tau\_{min} is generally taken to be 1, the time grequency of the original data, while τm​a​x\tau\_{max} needs to be calibrated.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ​(τ,q)=𝔼​[|X​(t+τ)−X​(t)|q].\Xi(\tau,q)=\mathbb{E}[|X(t+\tau)-X(t)|^{q}]. |  | (5) |

In a scaling process, these moments follow a power-law relationship:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ​(τ,q)∼K​(q)​τq​ζ​(q)=K​(q)​τq​H​(q),\Xi(\tau,q)\sim K(q)\tau^{q\zeta(q)}=K(q)\tau^{qH(q)}, |  | (6) |

where H​(q)H(q) is the generalised Hurst exponent. Taking logarithms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Ξ​(τ,q)∼q​H​(q)​log⁡τ+log⁡K​(q)\log\Xi(\tau,q)\sim qH(q)\log\tau+\log K(q) |  | (7) |

For uniscaling processes (e.g., fractional Brownian motion), H​(q)H(q) is constant across all qq. For multiscaling processes, H​(q)H(q) varies with qq. We estimate H​(q)H(q) by linear regression in log-log space:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(q)=∑i(xi−x¯)​(yi−y¯)q​∑i(xi−x¯)2,H(q)=\frac{\sum\_{i}(x\_{i}-\bar{x})(y\_{i}-\bar{y})}{q\sum\_{i}(x\_{i}-\bar{x})^{2}}, |  | (8) |

where xi=log⁡τix\_{i}=\log\tau\_{i}, yi=log⁡Ξ​(τi,q)y\_{i}=\log\Xi(\tau\_{i},q), and bars indicate means.The standard error of the estimate is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σH​(q)=∑i(yi−y^i)2/(n−2)q2​∑i(xi−x¯)2\sigma\_{H(q)}=\sqrt{\frac{\sum\_{i}(y\_{i}-\hat{y}\_{i})^{2}/(n-2)}{q^{2}\sum\_{i}(x\_{i}-\bar{x})^{2}}} |  | (9) |

where y^i=q​H​(q)​xi+log⁡K​(q)\hat{y}\_{i}=qH(q)x\_{i}+\log K(q) are the fitted values and n=|𝒯|n=|\mathcal{T}| is the cardinality of the set of time scales 𝒯={τ1,τ2,…,τn}\mathcal{T}=\{\tau\_{1},\tau\_{2},...,\tau\_{n}\}.
We estimate the moments by using:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ^​(τ,q)=1Nτ​∑i=1Nτ|X​((i+1)​τ)−X​(i​τ)|q,\hat{\Xi}(\tau,q)=\frac{1}{N\_{\tau}}\sum\_{i=1}^{N\_{\tau}}|X((i+1)\tau)-X(i\tau)|^{q}, |  | (10) |

where NτN\_{\tau} is the number of non-overlapping intervals of length τ\tau. Before computing the scaling exponents, we apply two important transformations to the moments.

First, we apply normalisation by scaling the moments by their value at τ=1\tau=1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ~​(τ,q)=Ξ^​(τ,q)Ξ^​(1,q)=Ξ^​(τ,q)K​(q).\widetilde{\Xi}(\tau,q)=\frac{\hat{\Xi}(\tau,q)}{\hat{\Xi}(1,q)}=\frac{\hat{\Xi}(\tau,q)}{K(q)}. |  | (11) |

This eliminates the constant factor in the power-law relationship and ensures all scaling curves start from the same point (1.0 at τ=1\tau=1).

Second, we apply standardisation by taking the qq-th root of the normalised moments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ˙˙˙​(τ,q)=[Ξ~​(τ,q)]1/q∼τH​(q).\dddot{\Xi}(\tau,q)=[\widetilde{\Xi}(\tau,q)]^{1/q}\sim\tau^{H(q)}. |  | (12) |

This transforms all moment orders to the same scale and simplifies the scaling relationship, allowing the direct estimation of H​(q)H(q) from the slope of log⁡Ξ˙˙˙​(τ,q)\log\dddot{\Xi}(\tau,q) versus log⁡τ\log\tau.

After these transformations, the intercept in the log-log regression should be zero, and we should use a regression model without an intercept term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Ξ˙˙˙​(τ,q)=H​(q)​log⁡τ+ϵ\log\dddot{\Xi}(\tau,q)=H(q)\log\tau+\epsilon |  | (13) |

To quantify the degree of multiscaling, we model H​(q)H(q) as a linear function of qq (Brandi and Di Matteo, [2022b](https://arxiv.org/html/2601.11305v1#bib.bib17 "On the statistics of scaling exponents and the multiscaling value at risk"), [a](https://arxiv.org/html/2601.11305v1#bib.bib16 "Multiscaling and rough volatility: an empirical investigation")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(q)=A+B​qH(q)=A+Bq |  | (14) |

The coefficient BB serves as our multiscaling proxy. For uniscaling processes, B=0B=0 theoretically, while for multiscaling processes, B<0B<0. The more negative BB is, the stronger the multiscaling behaviour. We estimate (A,B)(A,B) by minimizing:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (A,B)=arg⁡min(A,B)​∑jwj​[H​(qj)−(A+B​qj)]2(A,B)=\arg\min\_{(A,B)}\sum\_{j}w\_{j}[H(q\_{j})-(A+Bq\_{j})]^{2} |  | (15) |

where the weights wj=1/σH​(qj)2w\_{j}=1/\sigma\_{H(q\_{j})}^{2} account for the varying precision of different H​(qj)H(q\_{j}) estimates. The standard error of BB is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σB=∑jwj∑jwj​∑jwj​qj2−(∑jwj​qj)2\sigma\_{B}=\sqrt{\frac{\sum\_{j}w\_{j}}{\sum\_{j}w\_{j}\sum\_{j}w\_{j}q\_{j}^{2}-(\sum\_{j}w\_{j}q\_{j})^{2}}} |  | (16) |

This linear modelling approach, combined with the normalization and standardization transformations described above, enhances the robustness and interpretability of the multiscaling analysis. The framework allows us to quantify both the presence and strength of multiscaling in a time series through a single parameter BB.
When estimating the linear relationship H​(q)=A+B​qH(q)=A+Bq to quantify multiscaling, the precision of individual H​(q)H(q) estimates varies across moment orders qq, with higher-order moments typically exhibiting greater estimation error due to their sensitivity to extreme values. Weighted least squares (WLS) addresses this heteroscedasticity by assigning weights inversely proportional to the variance of each estimate: wj=1/σH​(qj)2w\_{j}=1/\sigma\_{H(q\_{j})}^{2}, minimising the weighted sum of squared residuals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (AW​L​S,BW​L​S)=arg⁡min(A,B)​∑j1σH​(qj)2​[H​(qj)−(A+B​qj)]2(A\_{WLS},B\_{WLS})=\arg\min\_{(A,B)}\sum\_{j}\frac{1}{\sigma\_{H(q\_{j})}^{2}}[H(q\_{j})-(A+Bq\_{j})]^{2} |  | (17) |

This ensures that more precisely estimated moments contribute more to the parameter estimation, reducing the disproportionate influence of noisy order moments and improving the robustness of the multiscaling proxy BB in heavy-tailed processes.

### Hyperparameter tuning: valid ranges for qq and optimal scale selection for τ\tau

The choice of moment orders qq is crucial for robust multiscaling estimation. For processes with power-law tails characterised by tail exponent α\alpha, the qq-th moment 𝔼​[|X|q]\mathbb{E}[|X|^{q}] exists only for q<αq<\alpha (Luitz et al., [2020](https://arxiv.org/html/2601.11305v1#bib.bib28 "Multifractality and its role in anomalous transport in the disordered xxz spin-chain")). Using q≥αq\geq\alpha leads to divergent moments that, in finite samples, produce unreliable estimates dominated by rare extreme events, potentially generating spurious multiscaling (Barunik and Kristoufek, [2010](https://arxiv.org/html/2601.11305v1#bib.bib55 "On hurst exponent estimation under heavy-tailed distributions")).

Brandi and Di Matteo ([2022b](https://arxiv.org/html/2601.11305v1#bib.bib17 "On the statistics of scaling exponents and the multiscaling value at risk")) addressed this issue by adopting a conservative approach, restricting analysis to q≤1q\leq 1 based on empirical evidence that financial returns have tail exponents ranging from approximately 1.5 to 3 (Weron, [2001](https://arxiv.org/html/2601.11305v1#bib.bib59 "Lévy-stable distributions revisited: tail index >2 does not exclude the Lévy-stable regime"); Scalas and Kim, [2006](https://arxiv.org/html/2601.11305v1#bib.bib60 "The art of fitting financial time series with lévy stable distributions"); Eom et al., [2019](https://arxiv.org/html/2601.11305v1#bib.bib61 "Fat tails in financial return distributions revisited: evidence from the korean stock market"); Luitz et al., [2020](https://arxiv.org/html/2601.11305v1#bib.bib28 "Multifractality and its role in anomalous transport in the disordered xxz spin-chain")). While this ensures moment existence, it may be overly conservative for series with heavier tails (α>2\alpha>2) and unnecessarily restrictive for lighter-tailed processes.
In this work, we adopt a data-driven approach that directly estimates the tail exponent for each series. We employ maximum likelihood estimation of α\alpha-stable distributions (Nolan, [2001](https://arxiv.org/html/2601.11305v1#bib.bib58 "Maximum likelihood estimation and diagnostics for stable distributions")) using the fast Lévy estimator. This method provides robust estimates of the stability parameter α\alpha, which characterises the tail behaviour of the return distribution.

To ensure conservative inference, we apply a safety factor to the estimated tail exponent:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αsafe=s⋅αstable\alpha\_{\text{safe}}=s\cdot\alpha\_{\text{stable}} |  | (18) |

where s=0.8s=0.8 is a safety factor that accounts for estimation uncertainty and ensures we remain well within the domain of moments’ existence (Brandi and Di Matteo, [2022a](https://arxiv.org/html/2601.11305v1#bib.bib16 "Multiscaling and rough volatility: an empirical investigation")). We then restrict our analysis to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qmax=αsafeq\_{\max}=\alpha\_{\text{safe}} |  | (19) |

This ensures that all moments used in the multiscaling analysis are theoretically finite and that estimates are not dominated by rare extreme events (Barunik and Kristoufek, [2010](https://arxiv.org/html/2601.11305v1#bib.bib55 "On hurst exponent estimation under heavy-tailed distributions")).
This approach offers several advantages over the fixed q≤1q\leq 1 approach. It is adaptive, automatically adjusting to the tail behaviour of each specific series, and efficient, using the full valid range of moments to improve statistical power for series with α>1.25\alpha>1.25. The method remains conservative through multiple estimators and a safety factor that prevents overestimation of the valid qq range, while being transparent since direct estimation of α\alpha makes assumptions explicit and testable. For the rough Bergomi model with stable increments, this approach is particularly appropriate as it directly estimates the stability parameter from the simulated return distribution, ensuring that only valid moments are analysed (Barunik and Kristoufek, [2010](https://arxiv.org/html/2601.11305v1#bib.bib55 "On hurst exponent estimation under heavy-tailed distributions")).

The choice of maximum time scale τmax\tau\_{\max} is critical for reliable estimation of scaling exponents. Several approaches have been proposed in the literature. Yue et al. ([2017](https://arxiv.org/html/2601.11305v1#bib.bib57 "Linear and nonlinear correlations in the order aggressiveness of chinese stocks")) suggests segmented regression on the structure function itself to identify scaling and non-scaling regimes. Buonocore et al. ([2017](https://arxiv.org/html/2601.11305v1#bib.bib56 "Asymptotic scaling properties and estimation of the generalized hurst exponents in financial data")) propose using autocorrelation significance tests to determine the minimum aggregation time. Brandi and Di Matteo ([2022b](https://arxiv.org/html/2601.11305v1#bib.bib17 "On the statistics of scaling exponents and the multiscaling value at risk")) introduced the Autocorrelation Segmented Regression (ACSR) method, which performs segmented regression on the autocorrelation function of absolute returns. While the ACSR method effectively identifies the scale where temporal correlations decay, it does not directly ensure that the scaling relationship in Equation [4](https://arxiv.org/html/2601.11305v1#S3.E4 "In 3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") holds with good linear fit quality across all moments qq. In this work, we adopt a complementary approach that explicitly optimises for scaling quality.
For each candidate τmax\tau\_{\max}, we compute the goodness-of-fit (R2R^{2} values) of the log-log regression for all moments q∈[qmin,qmax]q\in[q\_{\min},q\_{\max}]. We then determine:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rmin2​(τmax)=minq⁡R2​(q,τmax)R^{2}\_{\min}(\tau\_{\max})=\min\_{q}R^{2}(q,\tau\_{\max}) |  | (20) |

We select the largest τmax\tau\_{\max} for which Rmin2​(τmax)R^{2}\_{\min}(\tau\_{\max}) exceeds a stringent threshold (typically 0.95-0.98):

|  |  |  |  |
| --- | --- | --- | --- |
|  | τmax∗=max⁡{τmax:Rmin2​(τmax)≥0.98}\tau\_{\max}^{\*}=\max\{\tau\_{\max}:R^{2}\_{\min}(\tau\_{\max})\geq 0.98\} |  | (21) |

This approach ensures that:

1. 1.

   All moments exhibit good power-law scaling over the same range
2. 2.

   Comparisons of H​(q)H(q) across different qq values are based on equally reliable estimates
3. 3.

   The selected range maximises statistical power while maintaining fit quality

Our method differs from ACSR in that it directly targets the quality of the scaling relationship itself, rather than inferring it from autocorrelation structure. This is particularly important for multiscaling analysis where different moments may have different sensitivities to finite-size effects and boundary conditions (Kantelhardt et al., [2002](https://arxiv.org/html/2601.11305v1#bib.bib3 "Multifractal detrended fluctuation analysis of nonstationary time series")).

## 4 Source of Multiscaling

To rigorously investigate the source of multiscaling in the rough Bergomi model, we develop a comprehensive two-stage testing methodology. Given that the rough Bergomi model generates fat-tailed returns, our approach focuses on distinguishing between two scenarios: whether the observed multiscaling arises purely from the fat-tailed distribution of returns (Zhou, [2009](https://arxiv.org/html/2601.11305v1#bib.bib7 "The components of empirical multifractality in financial returns")), or whether temporal dependencies contribute additional multiscaling beyond the distributional effects (Stanley, [2003](https://arxiv.org/html/2601.11305v1#bib.bib4 "Statistical physics and economic fluctuations: do outliers exist?")). Our shuffling procedure preserves the exact return distribution while destroying temporal correlations, allowing us to isolate the distributional contribution and test whether memory effects provide any additional multiscaling. First, we test whether significant multiscaling exists beyond what would be expected in a uniscaling process. Second, if multiscaling is present, we determine whether it is purely distributional or whether temporal dependencies also contribute.

Our approach combines established techniques from multiscaling analysis with specialised surrogate data methods designed to isolate different potential sources of multiscaling, formulated within a rigorous statistical hypothesis testing framework.

### 4.1 Surrogate Data Generation

To isolate different sources of multiscaling, we employ two carefully designed surrogate data methods:

#### 4.1.1 Matched Fractional Brownian Motion

For testing the presence of multiscaling, we generate fractional Brownian motion (fBm) with Hurst exponent matching the H​(1)H(1) of the original series using the Davies-Harte method (Davies and Harte, [1987](https://arxiv.org/html/2601.11305v1#bib.bib51 "Tests for hurst effect")). The algorithm computes the theoretical autocovariance function γ​(k)=ν22​(|k+1|2​H−2​|k|2​H+|k−1|2​H)\gamma(k)=\frac{\nu^{2}}{2}(|k+1|^{2H}-2|k|^{2H}+|k-1|^{2H}), where ν2\nu^{2} is the variance of the process, embeds this in a circulant matrix whose eigenvalues are computed via Fast Fourier Transform, and generates fBm as X​(t)=∑k=0n−1gk​e2​π​i​k​t/nX(t)=\sum\_{k=0}^{n-1}g\_{k}e^{2\pi ikt/n}, where gkg\_{k} are complex Gaussian random variables with variance proportional to the eigenvalues. This produces a uniscaling process with the same overall scaling behaviour as the original series at the first moment.

#### 4.1.2 Shuffled Surrogates

To separate distributional from temporal contributions to multiscaling, we generate shuffled surrogates by randomly permuting the returns of the original time series (Theiler et al., [1992](https://arxiv.org/html/2601.11305v1#bib.bib49 "Testing for nonlinearity in time series: the method of surrogate data"); Schreiber and Schmitz, [2000](https://arxiv.org/html/2601.11305v1#bib.bib50 "Surrogate time series")). For a price series {Xt}t=0N\{X\_{t}\}\_{t=0}^{N}, we compute returns rt=Xt−Xt−1r\_{t}=X\_{t}-X\_{t-1}, randomly permute them to obtain {r~π​(t)}\{\tilde{r}\_{\pi(t)}\} where π\pi is a random permutation implemented via the Fisher-Yates algorithm (Fisher and Yates, [1938](https://arxiv.org/html/2601.11305v1#bib.bib64 "Statistical tables for biological, agricultural and medical research"); Knuth, [2014](https://arxiv.org/html/2601.11305v1#bib.bib65 "The art of computer programming: seminumerical algorithms, volume 2")), and reconstruct the price series as X~t=X0+∑s=1tr~s\tilde{X}\_{t}=X\_{0}+\sum\_{s=1}^{t}\tilde{r}\_{s}.This procedure preserves the exact marginal distribution of returns (including all moments and tail behaviour) while completely destroying temporal correlations, including autocorrelations and volatility clustering.

### 4.2 Statistical Hypothesis Testing Framework

Previous approaches to testing multiscaling have typically relied on examining whether the slope BB in the regression of Eq. [14](https://arxiv.org/html/2601.11305v1#S3.E14 "In 3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") is statistically significant using standard t-tests against zero. However, this approach is fundamentally flawed because even genuinely uniscaling processes like fractional Brownian motion can produce non-zero BB values in finite samples due to estimation noise and sampling variability. Testing against zero assumes the theoretical value of BB under uniscaling is exactly zero, which is unrealistic in practice. We propose a rigorous two-stage framework using surrogate data methods: first, we test for multiscaling presence by comparing against the empirical distribution of BB values from fractional Brownian motion surrogates with matched Hurst exponent, capturing the actual range of BB values expected under uniscaling; second, we employ nonparametric permutation tests with shuffled surrogates to identify whether the multiscaling arises from distributional or temporal sources, using distance-based statistics that remain valid even under asymmetric null distributions.

#### 4.2.1 Stage 1: Testing for Presence of Multiscaling

We test whether significant multiscaling exists beyond what would be expected in a uniscaling process. The null hypothesis is222We use the notation Hϕ(n)H\_{\phi}^{(n)}, where ϕ\phi is the null hypothesis (0) or the alternative hypothesis (A) while the superscript nn refers to the first stage n=1n=1 or the second stage (n=2)n=2) of the testing procedure.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0(1):The process is uniscaling fBm with ​H=H​(q)​w​i​t​h​q=1H\_{0}^{(1)}:\text{The process is uniscaling fBm with }H=H(q)\ with\ q=1 |  | (22) |

with alternative hypothesis HA(1)H\_{A}^{(1)}: the process exhibits genuine multiscaling with H​(q)H(q) varying with qq.

We generate MM independent simulations of fractional Brownian motion with H=H​(1)rBergomiH=H(1)\_{\text{rBergomi}}. For each simulation ii, we compute the multiscaling proxy BfBm,iB\_{\text{fBm},i}. Since genuine multiscaling in financial time series implies B<0B<0 (decreasing H​(q)H(q) with increasing qq), we perform a *one-sided* permutation test (Good, [2005](https://arxiv.org/html/2601.11305v1#bib.bib52 "Permutation, parametric, and bootstrap tests of hypotheses")). The p-value is computed directly as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ppresence=1I​∑i=1I𝕀​(BfBm,i≤BrBergomi)p\_{\text{presence}}=\frac{1}{I}\sum\_{i=1}^{I}\mathbb{I}(B\_{\text{fBm},i}\leq B\_{\text{rBergomi}}) |  | (23) |

where 𝕀​(⋅)\mathbb{I}(\cdot) is the indicator function.333An alternative approach involves standardizing by the empirical standard deviation of the surrogate distribution: TrBergomi=(BrBergomi−B¯fBm)/SD​(BfBm)T\_{\text{rBergomi}}=(B\_{\text{rBergomi}}-\bar{B}\_{\text{fBm}})/\text{SD}(B\_{\text{fBm}}) and similarly for each surrogate, computing p=1M​∑i=1M𝕀​(TfBm,i≤TrBergomi)p=\frac{1}{M}\sum\_{i=1}^{M}\mathbb{I}(T\_{\text{fBm},i}\leq T\_{\text{rBergomi}}). This standardization does not affect the p-value but expresses the test statistic in units of standard deviations, which may aid interpretation. This percentile-based approach directly estimates the probability that a uniscaling process would generate a multiscaling proxy as extreme as or more extreme than the observed value, naturally incorporating all sources of variability in the surrogate generation and estimation process.

We reject H0(1)H\_{0}^{(1)} at significance level α=0.05\alpha=0.05 if ppresence<αp\_{\text{presence}}<\alpha, concluding that significant multiscaling is present.

#### 4.2.2 Stage 2: Testing the Source of Multiscaling

If the first test confirms multiscaling, we examine whether it arises from distributional properties or temporal dependencies. The null hypothesis is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0(2):Multiscaling is purely distributional (no temporal contribution)H\_{0}^{(2)}:\text{Multiscaling is purely distributional (no temporal contribution)} |  | (24) |

with alternative HA(2)H\_{A}^{(2)}: temporal dependencies contribute significantly to multiscaling.

We generate NN shuffled surrogates and compute Bshuf,iB\_{\text{shuf},i} for each. Since the null distribution may be asymmetric (particularly for heavy-tailed processes (Barunik and Kristoufek, [2010](https://arxiv.org/html/2601.11305v1#bib.bib55 "On hurst exponent estimation under heavy-tailed distributions"))), we use a robust distance-based approach for the two-sided test (Phipson and Smyth, [2010](https://arxiv.org/html/2601.11305v1#bib.bib54 "Permutation p-values should never be zero: calculating exact p-values when permutations are randomly drawn")). We compute the median of surrogates as the center:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B~=median​(Bshuf,1,…,Bshuf,N)\tilde{B}=\text{median}(B\_{\text{shuf},1},\ldots,B\_{\text{shuf},N}) |  | (25) |

which is more robust to outliers than the mean.

The distance from the center for the original series is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dorig=|BrBergomi−B~|d\_{\text{orig}}=|B\_{\text{rBergomi}}-\tilde{B}| |  | (26) |

and for each surrogate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dshuf,i=|Bshuf,i−B~|d\_{\text{shuf},i}=|B\_{\text{shuf},i}-\tilde{B}| |  | (27) |

The *two-sided* p-value is computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | psource=1J​∑i=1J𝕀​(dshuf,i≥dorig)p\_{\text{source}}=\frac{1}{J}\sum\_{i=1}^{J}\mathbb{I}(d\_{\text{shuf},i}\geq d\_{\text{orig}}) |  | (28) |

This formulation correctly tests whether BrBergomiB\_{\text{rBergomi}} is unusually far from the typical distributional-only value in *either direction*, handling asymmetric null distributions by measuring absolute deviation from the center (Good, [2005](https://arxiv.org/html/2601.11305v1#bib.bib52 "Permutation, parametric, and bootstrap tests of hypotheses")). The test is two-sided because temporal structure could either enhance multiscaling (making BB more negative) or reduce it (making BB less negative).

We reject H0(2)H\_{0}^{(2)} at α=0.05\alpha=0.05 if psource<αp\_{\text{source}}<\alpha. If rejected with BrBergomi<B~B\_{\text{rBergomi}}<\tilde{B}, temporal dependencies *enhance* multiscaling; if BrBergomi>B~B\_{\text{rBergomi}}>\tilde{B}, they *reduce* it. If not rejected, multiscaling is primarily attributable to distributional properties (fat tails).

### 4.3 Implementation Details

For all analyses, we use I=1000I=1000 fractional Brownian motion surrogates for testing multiscaling presence (Stage 1) and J=1000J=1000 shuffled surrogates for identifying the source (Stage 2), which provides sufficient Monte Carlo precision. The multiscaling proxy BB is estimated via weighted least squares regression of H​(q)H(q) on qq using the relationship in eq. [14](https://arxiv.org/html/2601.11305v1#S3.E14 "In 3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"), with weights inversely proportional to the variance of H​(q)H(q) estimates. We determine the valid range of qq values based on the tail index of the return distribution to ensure moment existence, and select the optimal scale range [τmin,τmax][\tau\_{\min},\tau\_{\max}] to maximize regression fit quality (R2>0.95R^{2}>0.95) across all qq values simultaneously.

## 5 Results

We present our findings in two parts. First, we apply our two-stage testing methodology to the rough Bergomi model across a range of roughness parameters H∈[0.001,0.2]H\in[0.001,0.2], examining both the presence of multiscaling and its underlying source. For each parameter value, we generate n=1000n=1000 independent simulations of length N=10000N=10000 to ensure robust statistical inference. Second, we validate our methodology using two synthetic models with known multiscaling properties, the Multifractal Random Walk (MRW) and Fractional Lévy Stable Motion (FLSM), to demonstrate that our testing framework correctly identifies different sources of multiscaling. Throughout, we report the percentage of simulations exhibiting significant multiscaling at the 5% level, along with the attribution to distributional versus temporal sources.

### 5.1 Main Results: Rough Bergomi Model

#### 5.1.1 Presence of Multiscaling

We first test whether the rough Bergomi model exhibits significant multiscaling compared to matched fractional Brownian motion. Figure [2](https://arxiv.org/html/2601.11305v1#S5.F2 "Figure 2 ‣ 5.1.1 Presence of Multiscaling ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") shows the multiscaling proxy BB as a function of the Hurst parameter HH across 1000 simulations for different values of HH. Each boxplot displays the distribution of BB values: the central line indicates the median, the box boundaries represent the first and third quartiles (containing 50% of the data), the whiskers extend to values within 1.5 times the interquartile range, and individual points mark outliers beyond this range. The decreasing trend in BB as HH decreases demonstrates increasingly strong multiscaling behaviour for rougher volatility.

![Refer to caption](rbegomi_B_orig_H_max_0_25_boxplot.png)


Figure 2: Multiscaling proxy BB as a function of HH in the rough Bergomi model.

The results confirm that the rough Bergomi model exhibits significant multiscaling for all values of HH, with the strength of multiscaling increasing dramatically as HH decreases. Next, we investigate whether the observed multiscaling arises from the fat-tailed return distribution or from temporal dependencies. We apply the testing framework described in Section [4.2](https://arxiv.org/html/2601.11305v1#S4.SS2 "4.2 Statistical Hypothesis Testing Framework ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") to distinguish between these sources across different roughness regimes. The results for the critical range of very rough volatility (H≤0.01H\leq 0.01) are presented in Table [1](https://arxiv.org/html/2601.11305v1#S5.T1 "Table 1 ‣ 5.1.1 Presence of Multiscaling ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").

Table 1: rBergomi Model: Multiscaling Significance and Source Attribution (Very Rough)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Multiscaling | Source of Multiscaling | | Multiscaling Statistics | |
| H | Sig (%) | Distributional(%) | Temporal(%) | Mean B | SD(B) |
| 0.001 | 100.0 | 95.3 | 4.7 | −0.0802-0.0802 | 0.0058 |
| 0.005 | 100.0 | 90.3 | 9.7 | −0.0767-0.0767 | 0.0064 |
| 0.010 | 100.0 | 78.4 | 21.6 | −0.0747-0.0747 | 0.0068 |

The "Sig (%)" column shows the percentage of simulations (out of 1000) that exhibit statistically significant multiscaling at the 5% level when compared to matched fractional Brownian motion. The "Distribution (%)" indicates cases where multiscaling is solely attributed to distributional properties, while "Temporal (%)" represents cases where temporal dependencies (either enhancing or diminishing) contribute to the multiscaling behaviour. Mean B and SD(B) provide the statistical characteristics of the multiscaling coefficient. These results provide overwhelming evidence that for empirically relevant roughness parameters (H≤0.01H\leq 0.01), the multiscaling in the rough Bergomi model is primarily attributable to the fat-tailed return distribution. All 1000 simulations exhibit significant multiscaling (100% detection rate). For H=0.001H=0.001, 95.3% of the multiscaling is solely distributional, with only 4.7% showing any temporal contribution. As H increases to 0.01, the distributional component remains dominant at 78.4%, though temporal effects become more noticeable at 21.6%. For moderate roughness values (0.05≤H≤0.20.05\leq H\leq 0.2), we observe a dramatic transition in the nature of multiscaling, as shown in Table [2](https://arxiv.org/html/2601.11305v1#S5.T2 "Table 2 ‣ 5.1.1 Presence of Multiscaling ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").

Table 2: rBergomi Model: Multiscaling Significance and Source Attribution

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Multiscaling | Source of Multiscaling | | Multiscaling Statistics | |
| H | Sig (%) | Distributional(%) | Temporal(%) | Mean B | SD(B) |
| 0.050 | 99.9 | 29.1 | 70.9 | −0.0482-0.0482 | 0.0102 |
| 0.100 | 98.6 | 10.0 | 90.0 | −0.0287-0.0287 | 0.0101 |
| 0.200 | 71.5 | 3.5 | 96.5 | −0.0095-0.0095 | 0.0087 |

A striking transition occurs as HH increases toward less rough regimes. While the percentage of simulations exhibiting significant multiscaling remains high for H≤0.1H\leq 0.1 (above 98%), the source attribution completely reverses. At H=0.05H=0.05, temporal effects begin to dominate with 70.9% of cases showing temporal contribution. This temporal dominance intensifies dramatically for H=0.2H=0.2, where 96.5% of significant cases involve temporal dependencies, with only 3.5% being purely distributional.

#### 5.1.2 Distributional and Temporal Characteristics

To better understand the mechanism behind the regime transition observed in Tables [1](https://arxiv.org/html/2601.11305v1#S5.T1 "Table 1 ‣ 5.1.1 Presence of Multiscaling ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") and [2](https://arxiv.org/html/2601.11305v1#S5.T2 "Table 2 ‣ 5.1.1 Presence of Multiscaling ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"), we examine two key characteristics of the rough Bergomi model across different roughness regimes: the kurtosis of the return distribution (capturing tail heaviness) and the degree of volatility clustering (capturing temporal dependencies). Figures [3](https://arxiv.org/html/2601.11305v1#S5.F3 "Figure 3 ‣ 5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") and [4](https://arxiv.org/html/2601.11305v1#S5.F4 "Figure 4 ‣ 5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") report these results as functions of the Hurst parameter HH.

![Refer to caption](rbegomi_kurtosis_H_max_0_25_boxplot.png)


Figure 3: Kurtosis of returns (log scale) in the rough Bergomi model as a function of the Hurst parameter HH. Tail heaviness decreases substantially as HH increases, with median values dropping from around 50 for very rough processes (H=0.001H=0.001) to approximately 5 for H=0.2H=0.2. Each boxplot summarises 1000 independent simulations.

![Refer to caption](rbegomi_vol_clustering_H_max_0_25_boxplot.png)


Figure 4: Volatility clustering in the rough Bergomi model as a function of the Hurst parameter HH, measured as the sum of the first 10 autocorrelation coefficients of absolute returns. Temporal persistence increases dramatically with HH, rising from near zero for very rough processes (H≤0.01H\leq 0.01) to approximately 3 for H=0.2H=0.2. Each boxplot summarises 1000 independent simulations.

The results in Figures [3](https://arxiv.org/html/2601.11305v1#S5.F3 "Figure 3 ‣ 5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") and [4](https://arxiv.org/html/2601.11305v1#S5.F4 "Figure 4 ‣ 5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") provide a clear mechanistic explanation for the regime transition observed in our statistical tests. Figure [3](https://arxiv.org/html/2601.11305v1#S5.F3 "Figure 3 ‣ 5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") shows that kurtosis decreases by approximately an order of magnitude as HH increases from 0.001 to 0.200, with median values dropping from around 50 to approximately 5. This dramatic reduction in tail heaviness explains why distributional contributions to multiscaling diminish at higher HH values. Conversely, Figure [4](https://arxiv.org/html/2601.11305v1#S5.F4 "Figure 4 ‣ 5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails") reveals that volatility clustering, which is nearly absent for very rough processes (H≤0.01H\leq 0.01), increases substantially as HH approaches 0.2, with values rising from near zero to approximately 3. This emergence of temporal persistence explains why temporal contributions become the dominant source of multiscaling in less rough regimes.

These findings demonstrate that the rough Bergomi model exhibits fundamentally different dynamics depending on the roughness parameter: very rough volatility (H→0H\to 0) generates extreme tail behaviour with minimal temporal structure, while moderately rough volatility produces milder tails but pronounced volatility clustering. Both mechanisms can generate multiscaling, but through different contributions. Notably, this flexibility of the model implies that for intermediate values of HH, the rough Bergomi model can simultaneously exhibit volatility clustering together with mild multiscaling. This combination is particularly relevant from an empirical perspective, as it aligns with the stylised facts commonly observed in real financial assets, where both persistent volatility dynamics and moderate departures from simple scaling are well documented (Cont, [2001](https://arxiv.org/html/2601.11305v1#bib.bib19 "Empirical properties of asset returns: stylized facts and statistical issues"); Di Matteo, [2007](https://arxiv.org/html/2601.11305v1#bib.bib23 "Multi-scaling in finance")).

### 5.2 Robustness Check: Validation on Synthetic Models

To check the robustness of our findings, we apply the same methodology to two synthetic processes with known multiscaling properties.

#### 5.2.1 Multifractal Random Walk

The Multifractal Random Walk (MRW) (Bacry et al., [2001a](https://arxiv.org/html/2601.11305v1#bib.bib24 "Multifractal random walk"), [b](https://arxiv.org/html/2601.11305v1#bib.bib25 "Modelling financial time series using multifractal random walks"); Muzy and Bacry, [2002](https://arxiv.org/html/2601.11305v1#bib.bib26 "Multifractal stationary random measures and multifractal random walks with log-infinitely divisible scaling laws"); Brandi and Di Matteo, [2022b](https://arxiv.org/html/2601.11305v1#bib.bib17 "On the statistics of scaling exponents and the multiscaling value at risk"); Buonocore et al., [2017](https://arxiv.org/html/2601.11305v1#bib.bib56 "Asymptotic scaling properties and estimation of the generalized hurst exponents in financial data")) is a widely used model that exhibits genuine multiscaling behaviour arising from both temporal dependencies and potentially heavy-tailed distributions. The parameter λ2\lambda^{2} controls the strength of multiscaling, with larger values leading to stronger multiscaling.

We generate MRW simulations with different λ\lambda values and apply our testing methodology. The results, presented in Table [3](https://arxiv.org/html/2601.11305v1#S5.T3 "Table 3 ‣ 5.2.1 Multifractal Random Walk ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"), show that our framework correctly identifies both the presence of multiscaling and its source.

Table 3: MRW Model: Multiscaling Significance and Source Attribution

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Multiscaling | Source of Multiscaling | | Multiscaling Statistics | |
| λ\lambda | Sig (%) | Distributional(%) | Temporal(%) | Mean B | SD(B) |
| 0.050 | 18.8 | 95.2 | 4.8 | −0.0018-0.0018 | 0.0039 |
| 0.150 | 78.5 | 75.3 | 24.7 | −0.0094-0.0094 | 0.0053 |
| 0.250 | 97.7 | 21.5 | 78.5 | −0.0248-0.0248 | 0.0081 |

For low multifractal intensity (λ=0.05\lambda=0.05), the detected multiscaling is almost entirely distributional (above 95%). However, at high multifractal intensity (λ=0.25\lambda=0.25), 78.5% of the multiscaling involves temporal dependencies, with only 21.5% being purely distributional. This confirms that the MRW exhibits genuine temporal multiscaling when λ\lambda is sufficiently large.

#### 5.2.2 Fractional Lévy Stable Motion

Fractional Lévy Stable Motion (FLSM) combines long-range dependence with heavy-tailed innovations (Huillet, [1999](https://arxiv.org/html/2601.11305v1#bib.bib11 "Fractional lévy motions and related processes"); Mazur et al., [2020](https://arxiv.org/html/2601.11305v1#bib.bib12 "Estimation of the linear fractional stable motion"); Stoev and Taqqu, [2004](https://arxiv.org/html/2601.11305v1#bib.bib13 "Simulation methods for linear fractional stable motion and farima using the fast fourier transform")). It is defined as a fractional integration of Lévy stable noise with stability parameter α∈(0,2]\alpha\in(0,2] and Hurst exponent HH. We generate FLSM simulations with α=1.90\alpha=1.90 and different HH values and apply our testing methodology. Given that the model, although composed of both tail and memory components, is not inherently multiscaling, we expect that the majority of cases will be uniscaling. The results, presented in Table [4](https://arxiv.org/html/2601.11305v1#S5.T4 "Table 4 ‣ 5.2.2 Fractional Lévy Stable Motion ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"), show that our framework correctly identifies that the apparent multiscaling in FLSM is primarily distributional.

Table 4: LFSM Model: Multiscaling Significance and Source Attribution

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Multiscaling | Source of Multiscaling | | Multiscaling Statistics | |
| H | Sig (%) | Distributional(%) | Temporal(%) | Mean B | SD(B) |
| 0.10 | 23.0 | 93.9 | 6.1 | −0.0003-0.0003 | 0.0058 |
| 0.50 | 23.3 | 94.0 | 6.0 | −0.0020-0.0020 | 0.0078 |
| 0.90 | 27.3 | 65.2 | 34.8 | −0.0107-0.0107 | 0.0103 |

For FLSM with α=1.90\alpha=1.90, the vast majority of significant multiscaling cases are attributed to distributional properties across all H values. Even at high memory parameter H=0.90H=0.90, 65.2% of the multiscaling remains purely distributional, with 34.8% showing some temporal contribution. This correctly identifies the heavy-tailed distribution as the primary source of multiscaling in FLSM.
The validation results using synthetic data demonstrate that our testing framework successfully distinguishes between different sources of multiscaling, lending strong support to our findings for the rough Bergomi model.

## 6 Discussion and Conclusions

This paper has addressed a fundamental question about the rough Bergomi model: what is the source of its multiscaling behaviour? Through rigorous statistical analysis, we have provided compelling evidence that multiscaling in the rough Bergomi model arises predominantly from the fat-tailed distribution of returns rather than from complex temporal dependencies or memory effects in the volatility process. Our comprehensive analysis reveals that all simulations in the empirically relevant parameter range (H≤0.01H\leq 0.01) exhibit significant multiscaling, with 78.4% to 95.3% of this effect attributable to distributional properties. The temporal dependencies contribute between 4.7% and 21.6% to the multiscaling in this critical range, effectively ruling out complex memory structures as a significant source. We observe a clear transition around H=0.1H=0.1, where the nature of multiscaling shifts from being predominantly distributional to increasingly temporal, providing insights into how the roughness parameter fundamentally alters the model’s behaviour. The analyses of the distributional and temporal characteristics across roughness regimes reveal a regime switch in the underlying source of multiscaling. For H≤0.01H\leq 0.01, the model exhibits strong multiscaling that is predominantly driven by extremely fat-tailed return distributions, with kurtosis values exceeding 50 on average. As HH increases and the process becomes less rough, the multiscaling weakens in absolute terms (mean BB approaches zero), but a fundamental transition occurs in its source: the tails become progressively less pronounced while volatility clustering emerges and intensifies. For H≥0.1H\geq 0.1, it is this temporal persistence in volatility, rather than tail behaviour, that accounts for the majority of the remaining multiscaling. This regime switch has important practical implications: models calibrated to very rough parameters capture market complexity through distributional channels, while those with moderate roughness do so through temporal dependence structures. The choice of roughness parameter thus determines not only the strength but also the fundamental nature of the model’s scaling properties. Crucially, this flexibility allows the rough Bergomi model, in specific ranges of HH, to exhibit volatility clustering together with mild multiscaling, a combination that closely matches the stylised facts observed in many real financial assets. These findings change how we should interpret the rough Bergomi model’s properties. The model’s ability to generate multiscaling, previously seen as evidence of complex temporal dynamics, is primarily a consequence of its stochastic volatility structure leading to fat-tailed returns. The fractional Brownian motion driving the volatility contributes to multiscaling mainly through its effect on the return distribution rather than through intricate memory effects. As HH decreases, the model generates increasingly fat-tailed returns, which in turn produce stronger multiscaling through a mechanism fundamentally different from the temporal complexity that might have been expected from a fractional process. Our methodological contribution provides a rigorous statistical framework for distinguishing between different sources of multiscaling. The combination of shuffled surrogates and matched fractional Brownian motion offers a powerful way to isolate distributional from temporal contributions, while our two-stage testing procedure, first establishing the presence of multiscaling, then identifying its source, provides a systematic approach to analysing scaling properties. The successful validation using synthetic data (MRW and FLSM) with known properties strengthens confidence in both our methodology and results. For practitioners, these results have important implications. The rough Bergomi model’s value for option pricing remains intact, as it still captures important features of implied volatility surfaces. However, risk management applications should focus on the model’s distributional properties rather than attempting to exploit supposed fractal scaling laws. The multiscaling should not be interpreted as evidence of market inefficiency or complex microstructure effects, but rather as a natural consequence of stochastic volatility generating heavy-tailed returns. Our results also reconcile several aspects of previous research. The strong multiscaling observed for small HH values (Brandi and Di Matteo, [2022a](https://arxiv.org/html/2601.11305v1#bib.bib16 "Multiscaling and rough volatility: an empirical investigation")) is confirmed, but we now understand it as a distributional rather than temporal phenomenon. The finding that volatility appears rough aligns with our observation of strong multiscaling in this regime, both arising from the fat-tailed nature of returns. In conclusion, while financial markets undoubtedly exhibit complex behaviours, our results demonstrate that one particular manifestation of this complexity, multiscaling, can be largely explained by the relatively simple mechanism of stochastic volatility leading to fat-tailed return distributions. The rough Bergomi model remains a valuable tool for financial applications, but its apparent complexity, at least as manifested through multiscaling, has a simpler origin than might have been expected. This finding represents an important step toward a more nuanced understanding of financial market dynamics, distinguishing between genuine temporal complexity and distributional effects that merely appear complex when viewed through the lens of scaling analysis.

## Acknowledgements

We are grateful to Pasquale Casaburi for valuable discussions in the early stages of this project.

## Declaration of competing interests

The authors declare that they have no known competing financial interests or personal relationships
that could have appeared to influence the work reported in this paper.

## Declaration of funding

No funding was received.

## References

* E. Abi Jaber, E. Miller, and H. Pham (2021)
  Markowitz portfolio selection for multivariate affine and quadratic volterra models.
  SIAM Journal on Financial Mathematics 12 (1),  pp. 369–409.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p2.2 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* E. Alòs, D. García-Lorite, and A. Muguruza (2022)
  On smile properties of volatility derivatives and exotic products: understanding the vix skew.
  SIAM Journal on Financial Mathematics 13 (1),  pp. 32–69.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p4.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* E. Bacry, J. Delour, and J. Muzy (2001a)
  Multifractal random walk.
  Physical Review E 64 (2),  pp. 026103.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.p1.1 "3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§5.2.1](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS1.p1.1 "5.2.1 Multifractal Random Walk ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* E. Bacry, J. Delour, and J. Muzy (2001b)
  Modelling financial time series using multifractal random walks.
  Physica A: Statistical Mechanics and its Applications 299 (1),  pp. 84–92.
  External Links: [Document](https://dx.doi.org/10.1016/S0378-4371%2801%2900284-9)
  Cited by: [§5.2.1](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS1.p1.1 "5.2.1 Multifractal Random Walk ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. Barunik, T. Aste, T. Di Matteo, and R. Liu (2012)
  Understanding the source of multifractality in financial markets.
  Physica A: Statistical Mechanics and its Applications 391 (17),  pp. 4234–4251.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. Barunik and L. Kristoufek (2010)
  On hurst exponent estimation under heavy-tailed distributions.
  Physica A: Statistical Mechanics and its Applications 389 (18),  pp. 3844–3855.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p1.6 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p7.4 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§4.2.2](https://arxiv.org/html/2601.11305v1#S4.SS2.SSS2.p2.2 "4.2.2 Stage 2: Testing the Source of Multiscaling ‣ 4.2 Statistical Hypothesis Testing Framework ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* C. Bayer, P. Friz, and J. Gatheral (2016)
  Pricing under rough volatility.
  Quantitative Finance 16 (6),  pp. 887–904.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p2.2 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p1.2 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p10.6 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p7.1 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* C. Bayer, E. J. Hall, and R. Tempone (2022)
  Weak error rates for option pricing under linear rough volatility.
  International Journal of Theoretical and Applied Finance 25 (07n08),  pp. 2250029.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p5.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* C. Bayer, B. Horvath, A. Muguruza, B. Stemper, and M. Tomas (2025)
  On deep calibration of (rough) stochastic volatility models.
  The Journal of FinTech 05 (01),  pp. 2550005.
  External Links: [Document](https://dx.doi.org/10.1142/S2705109925500051)
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p5.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* C. Bayer, R. Tempone, and S. Wolfers (2020)
  Pricing american options by exercise rate optimization.
  Quantitative Finance 18 (9),  pp. 1513–1543.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p2.2 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* M. Bennedsen, A. Lunde, and M. S. Pakkanen (2022)
  Decoupling the short- and long-term behavior of stochastic volatility.
  Journal of Financial Econometrics 15 (4),  pp. 516–542.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p1.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p6.2 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* O. Bonesini, G. Callegaro, and A. Jacquier (2023)
  Functional quantization of rough volatility and applications to the vix.
  Quantitative Finance 21 (10),  pp. 1627–1641.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p2.2 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* F. Bourgey and S. De Marco (2021)
  Multilevel monte carlo simulation for vix options in the rough bergomi model.
  arXiv preprint arXiv:2105.05356.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p5.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* G. Brandi and T. Di Matteo (2022a)
  Multiscaling and rough volatility: an empirical investigation.
  International Review of Financial Analysis 84,  pp. 102201.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p1.2 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p10.6 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3.1](https://arxiv.org/html/2601.11305v1#S3.SS1.p20.2 "3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p5.1 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§6](https://arxiv.org/html/2601.11305v1#S6.p1.9 "6 Discussion and Conclusions ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* G. Brandi and T. Di Matteo (2022b)
  On the statistics of scaling exponents and the multiscaling value at risk.
  The European Journal of Finance 28 (13-15),  pp. 1361–1382.
  Cited by: [§3.1](https://arxiv.org/html/2601.11305v1#S3.SS1.p20.2 "3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p2.4 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p8.5 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.p1.1 "3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§5.2.1](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS1.p1.1 "5.2.1 Multifractal Random Walk ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. J. Buonocore, G. Brandi, R. N. Mantegna, and T. Di Matteo (2020)
  On the interplay between multiscaling and stock dependence.
  Quantitative Finance 20 (1),  pp. 133–145.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. J. Buonocore, T. Aste, and T. Di Matteo (2017)
  Asymptotic scaling properties and estimation of the generalized hurst exponents in financial data.
  Physical Review E 95 (4),  pp. 042311.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p8.5 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§5.2.1](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS1.p1.1 "5.2.1 Multifractal Random Walk ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. J. Buonocore, T. Aste, and T. Di Matteo (2016)
  Measuring multiscaling in financial time-series.
  Chaos, Solitons & Fractals 88,  pp. 38–47.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* L. E. Calvet and A. J. Fisher (2002)
  Multifractality in asset returns: theory and evidence.
  Review of Economics and Statistics 84 (3),  pp. 381–406.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3.1](https://arxiv.org/html/2601.11305v1#S3.SS1.p2.5 "3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.p1.1 "3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* C. Chong, M. Hoffmann, Y. Liu, M. Rosenbaum, and G. Szymanski (2024)
  Statistical inference for rough volatility: central limit theorems.
  The Annals of Applied Probability 32 (4),  pp. 2610–2649.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p8.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* F. Comte and E. Renault (2012)
  Affine fractional stochastic volatility models.
  Annals of Finance 8 (2),  pp. 337–378.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative Finance 1 (2),  pp. 223–236.
  Cited by: [§2](https://arxiv.org/html/2601.11305v1#S2.p7.1 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§5.1.2](https://arxiv.org/html/2601.11305v1#S5.SS1.SSS2.p3.2 "5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. B. Davies and D. S. Harte (1987)
  Tests for hurst effect.
  Biometrika 74 (1),  pp. 95–101.
  Cited by: [§4.1.1](https://arxiv.org/html/2601.11305v1#S4.SS1.SSS1.p1.5 "4.1.1 Matched Fractional Brownian Motion ‣ 4.1 Surrogate Data Generation ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* T. Di Matteo, T. Aste, and M. M. Dacorogna (2003)
  Scaling behaviors in differently developed markets.
  Physica A: Statistical Mechanics and its Applications 324 (1-2),  pp. 183–188.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* T. Di Matteo (2007)
  Multi-scaling in finance.
  Quantitative Finance 7 (1),  pp. 21–36.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3.1](https://arxiv.org/html/2601.11305v1#S3.SS1.p1.4 "3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3.1](https://arxiv.org/html/2601.11305v1#S3.SS1.p2.5 "3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.p1.1 "3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§5.1.2](https://arxiv.org/html/2601.11305v1#S5.SS1.SSS2.p3.2 "5.1.2 Distributional and Temporal Characteristics ‣ 5.1 Main Results: Rough Bergomi Model ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* O. El Euch, M. Fukasawa, and M. Rosenbaum (2018)
  The microstructural foundations of leverage effect and rough volatility.
  Finance and Stochastics 22 (2),  pp. 241–280.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p3.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* C. Eom, T. Kaizoji, and E. Scalas (2019)
  Fat tails in financial return distributions revisited: evidence from the korean stock market.
  Physica A: Statistical Mechanics and its Applications 526,  pp. 121055.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p2.4 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. A. Fisher and F. Yates (1938)
  Statistical tables for biological, agricultural and medical research.
   Oliver and Boyd, London.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.11305v1#S4.SS1.SSS2.p1.5 "4.1.2 Shuffled Surrogates ‣ 4.1 Surrogate Data Generation ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* M. Forde, M. Fukasawa, S. Gerhold, and B. Smith (2022)
  The riemann–liouville field and its gmc as H→0H\to 0, and skew flattening for the rough bergomi model.
  Statistics & Probability Letters 181,  pp. 109265.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p10.6 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* P. Friz and J. Gatheral (2022)
  Diamonds and forward variance models.
  Note: Available at SSRN
  External Links: [Link](https://ssrn.com/abstract=4099930),
  [Document](https://dx.doi.org/10.2139/ssrn.4099930)
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p4.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* M. Fukasawa, T. Takabatake, and R. Westphal (2019)
  Is volatility rough?.
  arXiv preprint arXiv:1905.04852.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p8.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* M. Fukasawa (2021)
  Volatility has to be rough.
  Quantitative finance 21 (1),  pp. 1–8.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p1.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* M. Fukasawa (2022)
  On asymptotically arbitrage-free approximations of the implied volatility.
  Frontiers of Mathematical Finance 1 (4),  pp. 525–537.
  External Links: [Document](https://dx.doi.org/10.3934/fmf.2022006),
  [Link](https://www.aimsciences.org/article/id/6348ae864cedfd00071dcbde)
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p4.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. Gatheral, T. Jaisson, and M. Rosenbaum (2018)
  Volatility is rough.
  Quantitative Finance 18 (6),  pp. 933–949.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2017.1393551)
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p1.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p1.2 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p10.6 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p6.2 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p9.2 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. Gatheral, P. Jusselin, and M. Rosenbaum (2020)
  The quadratic rough heston model and the joint s&p 500/vix smile calibration problem.
  arXiv preprint arXiv:2001.01789.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p8.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* P. I. Good (2005)
  Permutation, parametric, and bootstrap tests of hypotheses.
  3rd edition, Springer Science & Business Media, New York.
  Cited by: [§4.2.1](https://arxiv.org/html/2601.11305v1#S4.SS2.SSS1.p2.7 "4.2.1 Stage 1: Testing for Presence of Multiscaling ‣ 4.2 Statistical Hypothesis Testing Framework ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§4.2.2](https://arxiv.org/html/2601.11305v1#S4.SS2.SSS2.p5.3 "4.2.2 Stage 2: Testing the Source of Multiscaling ‣ 4.2 Statistical Hypothesis Testing Framework ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* E. Green, W. Hanan, and D. Heffernan (2014)
  The origins of multifractality in financial time series and the effect of extreme events.
  The European Physical Journal B 87 (6),  pp. 129.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§1](https://arxiv.org/html/2601.11305v1#S1.p7.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* U. Horst, W. Xu, and R. Zhang (2023)
  Convergence of heavy-tailed hawkes processes and the microstructure of rough volatility.
  arXiv preprint arXiv:2312.08784.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p3.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* B. Horváth, A. Jacquier, and P. Tankov (2020)
  Volatility options in rough volatility models.
  SIAM Journal on Financial Mathematics 11 (2),  pp. 437–469.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p4.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* T. Huillet (1999)
  Fractional lévy motions and related processes.
  Journal of Physics A: Mathematical and General 32 (42),  pp. 7225.
  Cited by: [§5.2.2](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS2.p1.4 "5.2.2 Fractional Lévy Stable Motion ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* A. Jacquier, C. Martini, and A. Muguruza (2018)
  On vix futures in the rough bergomi model.
  Quantitative Finance 18 (1),  pp. 45–61.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p2.2 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§2](https://arxiv.org/html/2601.11305v1#S2.p7.1 "2 The Rough Bergomi Model ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* A. Jacquier and Z. Zuric (2023)
  Random neural networks for rough volatility.
  arXiv preprint arXiv:2305.01035.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p5.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* P. Jusselin and M. Rosenbaum (2020)
  No-arbitrage implies power-law market impact and rough volatility.
  Mathematical Finance 30 (4),  pp. 1309–1336.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p3.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. W. Kantelhardt, S. A. Zschiegner, E. Koscielny-Bunde, S. Havlin, A. Bunde, and H. E. Stanley (2002)
  Multifractal detrended fluctuation analysis of nonstationary time series.
  Physica A: Statistical Mechanics and its Applications 316 (1-4),  pp. 87–114.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p13.1 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* D. E. Knuth (2014)
  The art of computer programming: seminumerical algorithms, volume 2.
   Addison-Wesley Professional.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.11305v1#S4.SS1.SSS2.p1.5 "4.1.2 Shuffled Surrogates ‣ 4.1 Surrogate Data Generation ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* D. J. Luitz, I. M. Khaymovich, and Y. Bar Lev (2020)
  Multifractality and its role in anomalous transport in the disordered xxz spin-chain.
  SciPost Physics Core 2 (2),  pp. 006.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p1.6 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p2.4 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3](https://arxiv.org/html/2601.11305v1#S3.p1.1 "3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* T. Lux (2008)
  The markov-switching multifractal model of asset returns: GMM estimation and linear forecasting of volatility.
  Journal of Business & Economic Statistics 26 (2),  pp. 194–210.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.p1.1 "3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* B. Mandelbrot, A. Fisher, and L. Calvet (1997)
  A multifractal model of asset returns.
  Cowles Foundation Discussion Paper
  Technical Report 1164, Cowles Foundation for Research in Economics, Yale University.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§3.1](https://arxiv.org/html/2601.11305v1#S3.SS1.p2.5 "3.1 Generalised Hurst Exponent (GHE) Framework ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* S. Mazur, D. Otryakhin, and M. Podolskij (2020)
  Estimation of the linear fractional stable motion.
  Bernoulli 26 (1),  pp. 466–499.
  Cited by: [§5.2.2](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS2.p1.4 "5.2.2 Fractional Lévy Stable Motion ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. McCrickerd and M. S. Pakkanen (2018)
  Turbocharging monte carlo pricing for the rough bergomi model.
  Quantitative Finance 18 (11),  pp. 1877–1886.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p2.2 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. Muzy and E. Bacry (2002)
  Multifractal stationary random measures and multifractal random walks with log-infinitely divisible scaling laws.
  Physical Review E 66 (5),  pp. 056121.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevE.66.056121)
  Cited by: [§5.2.1](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS1.p1.1 "5.2.1 Multifractal Random Walk ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. P. Nolan (2001)
  Maximum likelihood estimation and diagnostics for stable distributions.
  In Lévy Processes: Theory and Applications, O. E. Barndorff-Nielsen, T. Mikosch, and S. I. Resnick (Eds.),
   pp. 379–400.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p2.4 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* B. Phipson and G. K. Smyth (2010)
  Permutation p-values should never be zero: calculating exact p-values when permutations are randomly drawn.
  Statistical Applications in Genetics and Molecular Biology 9 (1),  pp. Article 39.
  Cited by: [§4.2.2](https://arxiv.org/html/2601.11305v1#S4.SS2.SSS2.p2.2 "4.2.2 Stage 2: Testing the Source of Multiscaling ‣ 4.2 Statistical Hypothesis Testing Framework ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* M. Rosenbaum and J. Zhang (2022)
  On the universality of the volatility formation process: when machine learning and rough volatility agree.
  arXiv preprint arXiv:2206.14114.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p3.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* E. Scalas and K. Kim (2006)
  The art of fitting financial time series with lévy stable distributions.
  arXiv preprint physics/0608224.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p2.4 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* T. Schreiber and A. Schmitz (2000)
  Surrogate time series.
  Physica D: Nonlinear Phenomena 142 (3-4),  pp. 346–382.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.11305v1#S4.SS1.SSS2.p1.5 "4.1.2 Shuffled Surrogates ‣ 4.1 Surrogate Data Generation ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* H. E. Stanley (2003)
  Statistical physics and economic fluctuations: do outliers exist?.
  Physica A: Statistical Mechanics and its Applications 318 (1-2),  pp. 279–292.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p7.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§4](https://arxiv.org/html/2601.11305v1#S4.p1.1 "4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* S. Stoev and M. S. Taqqu (2004)
  Simulation methods for linear fractional stable motion and farima using the fast fourier transform.
  Fractals 12 (01),  pp. 95–121.
  Cited by: [§5.2.2](https://arxiv.org/html/2601.11305v1#S5.SS2.SSS2.p1.4 "5.2.2 Fractional Lévy Stable Motion ‣ 5.2 Robustness Check: Validation on Synthetic Models ‣ 5 Results ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* J. Theiler, S. Eubank, A. Longtin, B. Galdrikian, and J. D. Farmer (1992)
  Testing for nonlinearity in time series: the method of surrogate data.
  Physica D: Nonlinear Phenomena 58 (1-4),  pp. 77–94.
  Cited by: [§4.1.2](https://arxiv.org/html/2601.11305v1#S4.SS1.SSS2.p1.5 "4.1.2 Shuffled Surrogates ‣ 4.1 Surrogate Data Generation ‣ 4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* R. Weron (2001)
  Lévy-stable distributions revisited: tail index >2>2 does not exclude the Lévy-stable regime.
  International Journal of Modern Physics C 12 (2),  pp. 209–223.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p2.4 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* P. Yue, H. Xu, W. Chen, X. Xiong, and W. Zhou (2017)
  Linear and nonlinear correlations in the order aggressiveness of chinese stocks.
  Fractals 25 (05),  pp. 1750041.
  Cited by: [§3](https://arxiv.org/html/2601.11305v1#S3.SSx1.p8.5 "Hyperparameter tuning: valid ranges for 𝑞 and optimal scale selection for 𝜏 ‣ 3 Scaling and Multiscaling Analysis in Finance ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").
* W. Zhou (2009)
  The components of empirical multifractality in financial returns.
  Europhysics Letters 88 (2),  pp. 28004.
  Cited by: [§1](https://arxiv.org/html/2601.11305v1#S1.p6.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§1](https://arxiv.org/html/2601.11305v1#S1.p7.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§1](https://arxiv.org/html/2601.11305v1#S1.p9.1 "1 Introduction ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails"),
  [§4](https://arxiv.org/html/2601.11305v1#S4.p1.1 "4 Source of Multiscaling ‣ Multiscaling in the Rough Bergomi Model: A Tale of Tails").