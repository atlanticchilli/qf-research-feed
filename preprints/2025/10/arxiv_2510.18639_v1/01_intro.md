---
authors:
- Samuel Perreault
- Silvana M. Pesenti
- Daniyal Shahzad
doc_id: arxiv:2510.18639v1
family_id: arxiv:2510.18639
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Distributional regression for seasonal data: an application to river flows'
url_abs: http://arxiv.org/abs/2510.18639v1
url_html: https://arxiv.org/html/2510.18639v1
venue: arXiv q-fin
version: 1
year: 2025
---


Samuel Perreault


Silvana M. Pesenti


Daniyal Shahzad

###### Abstract

Risk assessment in casualty insurance, such as flood risk, traditionally relies on extreme-value methods that emphasizes rare events. These approaches are well-suited for characterizing tail risk, but do not capture the broader dynamics of environmental variables such as moderate or frequent loss events. To complement these methods, we propose a modelling framework for estimating the full (daily) distribution of environmental variables as a function of time, that is a distributional version of typical climatological summary statistics, thereby incorporating both seasonal variation and gradual long-term changes. Aside from the time trend, to capture seasonal variation our approach simultaneously estimates the distribution for each instant of the seasonal cycle, without explicitly modelling the temporal dependence present in the data. To do so, we adopt a framework inspired by GAMLSS (Generalized Additive Models for Location, Scale, and Shape), where the parameters of the distribution vary over the seasonal cycle as a function of explanatory variables depending only on the time of year, and not on the past values of the process under study. Ignoring the temporal dependence in the seasonal variation greatly simplifies the modelling but poses inference challenges that we clarify and overcome.

We apply our framework to daily river flow data from three hydrometric stations along the Fraser River in British Columbia, Canada, and analyse the flood of the Fraser River in early winter of 2021.

Keywords: GAMLSS, Climatology, Misspecified model, Environmental risk, Flooding

## 1 Introduction

In casualty insurance, risk at a given location can broadly be viewed as the combination of two components: the probability of an event and the exposure, typically measured by the number of people or value of assets in the region. While exposure is often well-documented, understanding how the probability component evolves throughout the year remains a critical challenge—particularly in the context of environmental hazards such as floods. Traditionally, flood risk is summarized using return periods (average time between events of a certain magnitude), which are computed based on annual or seasonal maxima, or using peaks-over-threshold methods [[7](https://arxiv.org/html/2510.18639v1#bib.bibx7), [19](https://arxiv.org/html/2510.18639v1#bib.bibx19)]. We also refer to [[2](https://arxiv.org/html/2510.18639v1#bib.bibx2)] who study the spatial and long-term temporal dependence of food risk. These extreme risk approaches are well-established and particularly effective for characterizing tail risk; however, they provide only a partial view of the underlying phenomenon. In particular, they may not fully capture the range of conditions leading to moderate or frequent events, which also have implications for accumulated damages and operational risk. Modelling the full univariate distribution of river flow can serve as a valuable complement to classical extreme-value techniques. In this framework, seasonality and time trend are equally important. In particular, incorporating seasonality in a continuous fashion allows for a more refined understanding of how risk varies throughout the year, which is not possible when only studying seasonal maxima. Allowing for the inclusion of temporal trends makes it possible to account, at least on relatively short time horizons, for evolving patterns potentially associated with climate change. These considerations are highly relevant in insurance and risk management, where understanding the full structure of environmental variability is essential for pricing, underwriting, and capital allocation.

To motivate our work, we consider daily average river flow data (in  m3/s\text{\,}\mathrm{m}^{3}\mathrm{/}\mathrm{s}) from three hydrometric stations along the Fraser River in British Columbia, Canada. These stations provide long and uninterrupted records, ranging from a few decades to over a century of observations. One of them is located in the Fraser Valley, a region that has experienced major flooding events, including the notable November 2021 flood. The Fraser River is the longest river in British Columbia and exhibits interesting features. It originates in the Canadian Rocky Mountains, which are heavily snow covered in winter, then passes through the Fraser Canyon to the Fraser Valley, a lowland valley, and then empties into the Strait of Georgia close to Vancouver. The Fraser River is known for flooding, in particular, the Fraser Valley and Vancouver, which due to the proximity to the city results in large losses.

The primary aim of this paper is to introduce a flexible seasonal modelling framework motivated by the need to analyse long-term environmental data with evolving patterns. Building on the methodology proposed by [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)], we make two main contributions. First, we extend their purely seasonal model to accommodate temporal trends and interactions between seasonality and long-term variation. This generalization enables the modelling of more complex nonstationary behaviours often observed in environmental processes. Second, we explore the use of the (extended) generalized gamma distribution for modelling river flow data. We find that it offers a highly flexible and accurate fit for this type of data.

[[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)] propose a parametric approach for modelling how the distribution of a seasonal process varies throughout the year. By treating distributional parameters as smooth functions of the day of the year, their method provides a continuous, climatology-like summary of seasonal behaviour that is easily interpretable. It can be understood as a form of distributional regression [[11](https://arxiv.org/html/2510.18639v1#bib.bibx11), see, e.g.,], and more specifically as a generalized additive model for location, scale, and shape [[22](https://arxiv.org/html/2510.18639v1#bib.bibx22), GAMLSS], a modelling framework that is well adopted in hydrology [[28](https://arxiv.org/html/2510.18639v1#bib.bibx28), [15](https://arxiv.org/html/2510.18639v1#bib.bibx15), see, e.g.,]. Since temporal dependence is not the target of inference and a relatively complex phenomena, it is purposefully left unspecified, that is we treat the data as independent. This greatly simplifies the model structure but requires appropriate corrections during inference, where we draw from the literature on misspecified models, to account for residual serial correlation. While the focus is on modelling seasonal variation independently of temporal dependence, the proposed methodology can serve as the first step in a more general modelling pipeline, where the resulting fitted distributions are used to construct copula pseudo-observations (via the probability integral transform), from which temporal dependence can then be modelled separately.

A key assumption in the original formulation of [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)] is that the process is cyclostationary, meaning that the full distribution of the variable repeats itself periodically. Cyclostationary processes have been studied since at least the 1960s [[6](https://arxiv.org/html/2510.18639v1#bib.bibx6), [10](https://arxiv.org/html/2510.18639v1#bib.bibx10), [8](https://arxiv.org/html/2510.18639v1#bib.bibx8)], and remained an active area of research since then, particularly in signal processing [[5](https://arxiv.org/html/2510.18639v1#bib.bibx5), [16](https://arxiv.org/html/2510.18639v1#bib.bibx16), [17](https://arxiv.org/html/2510.18639v1#bib.bibx17), [18](https://arxiv.org/html/2510.18639v1#bib.bibx18), see, e.g.,]. While this is a natural and appealing framework for modelling seasonal phenomena, it can be too restrictive in practice, especially when long-term changes or gradual shifts in seasonal behaviour are present. As noted by [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)], however, their modelling approach is naturally extensible to accommodate more realistic forms of nonstationarity. In this paper, we do so by introducing slow, non-periodic temporal variation, allowing the seasonal profile to evolve gradually over time.

Our second objective, which is more applied in nature, is to explore the use of the generalized gamma distribution for modelling river flows. This distribution, often traced back to [[3](https://arxiv.org/html/2510.18639v1#bib.bibx3)] and later popularized by the works of [[25](https://arxiv.org/html/2510.18639v1#bib.bibx25)] and [[26](https://arxiv.org/html/2510.18639v1#bib.bibx26)], has been advocated for hydrological applications very early on [[12](https://arxiv.org/html/2510.18639v1#bib.bibx12), [13](https://arxiv.org/html/2510.18639v1#bib.bibx13), see, e.g.,]. One of its key advantages is its flexibility: it encompasses several well-known distributions as special cases, including the gamma and Weibull distributions, and approaches the lognormal distribution as a limiting case. In a particularly elegant contribution, [[21](https://arxiv.org/html/2510.18639v1#bib.bibx21)] showed how the lognormal distribution could be embedded as a proper special case within the generalized gamma family. Building on the same ideas, [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)] proposes practical approximations that make it possible to implement this extension in a stable and reliable manner. In what follows, we adopt this extended version, referred to simply as the generalized gamma distribution.
When paired with the aforementioned seasonal modelling framework, this choice allows for a continuous and flexible representation of seasonal dynamics, accommodating changes in distributional shape throughout the year. As we highlight, it captures the empirical variability observed in river flow data quite well.

The paper is structured as follow. Section [2](https://arxiv.org/html/2510.18639v1#S2 "2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows") introduces the model for daily univariate environmental data, with a focus on purely seasonal model and seasonal models with time trends. Section [3](https://arxiv.org/html/2510.18639v1#S3 "3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows") is devoted to fit the misspecified model, model selection and analysis. In Section [4](https://arxiv.org/html/2510.18639v1#S4 "4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), we illustrate how to fit a seasonal model with time trends to real data from the Fraser River. We first analyse a single station and then illustrate how to jointly model multiple stations. Section [5](https://arxiv.org/html/2510.18639v1#S5 "5 Discussion ‣ Distributional regression for seasonal data: an application to river flows") concludes and provides thoughts for future studies.

## 2 Daily environmental model

### 2.1 Model setting

To make the scope of our methodology explicit, we begin by providing general assumptions under which the proposed model is developed. Let 𝒯⊂ℝ\mathcal{T}\subset\mathbb{R} be a set of NN ordered timestamps, possibly irregularly spaced, and 𝑿=(Xt)t∈𝒯\bm{X}=(X\_{t})\_{t\in\mathcal{T}} be some available data of interest. The core assumption, specifically designed for environmental data, is that 𝑿\bm{X} comes from a process (Xt)t∈ℝ(X\_{t})\_{t\in\mathbb{R}} that is seasonal in the following weak sense.
For all t∈ℝt\in\mathbb{R}, let FtF\_{t} be the cumulative distribution function (cdf) of XtX\_{t} and suppose that Ft(⋅)=F(⋅|𝜽t)F\_{t}(\cdot)=F(\cdot|\bm{\theta}\_{t}) for some parameter 𝜽t\bm{\theta}\_{t} that varies with the time index tt; without loss of generality, assume that 𝜽t=(μt,σt,νt)\bm{\theta}\_{t}=(\mu\_{t},\sigma\_{t},\nu\_{t}).
To incorporate some seasonality and long-term variation in the parameters, we adopt what is essentially a generalized additive model for location, shape, and scale [[22](https://arxiv.org/html/2510.18639v1#bib.bibx22), GAMLSS,], using covariates that depends exclusively on the time index tt. Specifically, we let

|  |  |  |  |
| --- | --- | --- | --- |
|  | gμ​(μt)=𝒂μ​t⊤​𝜷μ,gσ​(σt)=𝒂σ​t⊤​𝜷σandgν​(νt)=𝒂ν​t⊤​𝜷ν,g\_{\mu}(\mu\_{t})=\bm{a}\_{\mu t}^{\top}\bm{\beta}\_{\mu}\;,\qquad g\_{\sigma}(\sigma\_{t})=\bm{a}\_{\sigma t}^{\top}\bm{\beta}\_{\sigma}\quad\text{and}\quad g\_{\nu}(\nu\_{t})=\bm{a}\_{\nu t}^{\top}\bm{\beta}\_{\nu}\;, |  | (1) |

where (gμ,gσ,gν)(g\_{\mu},g\_{\sigma},g\_{\nu}) are known monotonic and differentiable link functions, (𝒂μ​t,𝒂σ​t,𝒂ν​t)(\bm{a}\_{\mu t},\bm{a}\_{\sigma t},\bm{a}\_{\nu t}) are the time-based covariates, and (𝜷μ,𝜷σ,𝜷ν)(\bm{\beta}\_{\mu},\bm{\beta}\_{\sigma},\bm{\beta}\_{\nu}) are the unknown coefficients to be estimated.

In the original formulation of [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)], the model is purely seasonal in that it supposes Ft=Ft+pF\_{t}=F\_{t+p} for some period or cycle length pp. In this paper we work with p≈365.25p\approx 365.25, which corresponds to the length of the solar year. Such a model is built by restricting oneself to periodic functions of tt when defining (𝒂μ​t,𝒂σ​t,𝒂ν​t)(\bm{a}\_{\mu t},\bm{a}\_{\sigma t},\bm{a}\_{\nu t}); e.g., Fourier basis functions (i.e., pairs of cosine and sine functions) or cyclic B-splines. Here, we extend their framework by further including covariates defined via polynomials of tt, thus capturing more general non-stationary behaviours. Moreover, we consider covariates constructed as interactions between seasonal and drift components, which allows the seasonal pattern to evolve as time passes.

While the results in [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)] do not strictly speaking allow for drift terms, they can be adapted to include polynomial terms or different basis functions.
The proofs in [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)] however may require more substantial modifications when incorporating drift terms based on basis functions such as B-splines, since the coefficient associated with a given B-spline depends only on a localized subset of the data. This is enough to justify the use of linear drift terms and Fourier basis functions, which we prioritize in this paper.

### 2.2 Univariate model for river flows

As the above assumptions suggest, one of the core components of our approach is the univariate distribution FtF\_{t}, which is ultimately based on a fixed function F(⋅|𝜽t)F(\cdot|\bm{\theta}\_{t}) with time-varying parameters 𝜽t\bm{\theta}\_{t}.
For modelling river flows, we propose to use an extension, due to [[21](https://arxiv.org/html/2510.18639v1#bib.bibx21)], of the three-parameter generalized gamma distribution described in various forms in, e.g., [[25](https://arxiv.org/html/2510.18639v1#bib.bibx25)], [[26](https://arxiv.org/html/2510.18639v1#bib.bibx26)]; see also [[9](https://arxiv.org/html/2510.18639v1#bib.bibx9), Section 8.7 ] for a more comprehensive treatment.
Many common distributions are special cases of this family, most notably the Weibull, gamma and lognormal distributions, three popular choices in hydrology; see, e.g., Table 1 in [[26](https://arxiv.org/html/2510.18639v1#bib.bibx26)] for a list associated with the standard (non-extended) generalized gamma distribution.
As its absence from the latter list suggest, the lognormal distribution is not a proper member of the standard generalized gamma family; it is however a limit case of it, as we explain below.

Following the parametrization in [[24](https://arxiv.org/html/2510.18639v1#bib.bibx24), Section 19.4.3 ], we say that a positive random variable has a generalized gamma distribution, denoted G​Γ​(μt,σt,νt)\mathrm{G}\Gamma(\mu\_{t},\sigma\_{t},\nu\_{t}), when its density has the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(xt|μt,σt,νt):={|νt|​ξtξt​ztξt​exp⁡(−ξt​zt)xt​Γ​(ξt)νt≠0exp⁡{−log2⁡(xt/μt)/(2​σt2)}xt​σt​2​πνt=0,f(x\_{t}|\mu\_{t},\sigma\_{t},\nu\_{t}):=\begin{cases}\displaystyle\frac{|\nu\_{t}|\xi\_{t}^{\xi\_{t}}z\_{t}^{\xi\_{t}}\exp(-\xi\_{t}z\_{t})}{x\_{t}\Gamma(\xi\_{t})}&\nu\_{t}\neq 0\\[10.00002pt] \displaystyle\frac{\exp\{-\log^{2}(x\_{t}/\mu\_{t})/(2\sigma\_{t}^{2})\}}{x\_{t}\sigma\_{t}\sqrt{2\pi}}&\nu\_{t}=0\;,\end{cases} |  | (2) |

where zt:=(xt/μt)νtz\_{t}:=(x\_{t}/\mu\_{t})^{\nu\_{t}}, ξt:=(σt​νt)−2\xi\_{t}:=(\sigma\_{t}\nu\_{t})^{-2}, μt>0\mu\_{t}>0, σt>0\sigma\_{t}>0, and where Γ​(⋅)\Gamma(\cdot) denotes the Gamma function.
For νt≠0\nu\_{t}\neq 0, ff is the standard generalized gamma density, while for νt=0\nu\_{t}=0 it is the lognormal density with parameters log⁡(μt)\log(\mu\_{t}) and σt2\sigma\_{t}^{2}.
Given the parameter constraints, we set gμ​(x)=gσ​(x)=log⁡(x)g\_{\mu}(x)=g\_{\sigma}(x)=\log(x) (log links), thereby ensuring that μt\mu\_{t} and σt\sigma\_{t} always stay positive during estimation, and further set gν​(x)=xg\_{\nu}(x)=x (the identity link).

Despite its appearance, ff is indeed continuous in νt\nu\_{t} everywhere, including at νt=0\nu\_{t}=0.
In other words, the lognormal density defined for νt=0\nu\_{t}=0 is the limit of ff as νt→0\nu\_{t}\to 0, irrespective of the side from which νt\nu\_{t} approaches zero.
By showing that the score and Hessian of (a transformation of) this density exist at νt=0\nu\_{t}=0, with the latter being positive definite, [[21](https://arxiv.org/html/2510.18639v1#bib.bibx21)] demonstrated that the lognormal could be included in the family without violating the standard regularity conditions for maximum likelihood estimation.
Doing so does however introduce some practical challenges due to the numerical instability in the evaluation of ff when |νt||\nu\_{t}| is positive but small.
These technicalities and solutions for them are discussed in Section [3.1](https://arxiv.org/html/2510.18639v1#S3.SS1 "3.1 Objective function ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows") below and in more details in [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)].

One of the key advantages of the extended generalized gamma distribution, particularly in river flow modelling, is its flexible tail behaviour.
Unlike the gamma and lognormal distributions, not all moments of the generalized gamma distribution necessarily exist; indeed, their existence depends on the values of the parameters σt\sigma\_{t} and νt\nu\_{t}, and more precisely σt2​νt\sigma\_{t}^{2}\nu\_{t}, which we refer to as the tail-index coefficient.
For Xt∼G​Γ​(μt,σt,νt)X\_{t}\sim\mathrm{G}\Gamma(\mu\_{t},\sigma\_{t},\nu\_{t}) and k∈ℕ+k\in\mathbb{N}\_{+},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(Xtk)={μtk​Γ​(ξt+k/νt)ξk/νt​Γ​(ξ)if ​σt2​νt>−1/k​ and ​νt≠0μtk​exp⁡(k2​σt2/2)if ​νt=0∞if ​σt2​νt⩽−1/k.\mathbb{E}(X\_{t}^{k})=\begin{cases}\displaystyle\mu\_{t}^{k}\;\frac{\Gamma(\xi\_{t}+k/\nu\_{t})}{\xi^{k/\nu\_{t}}\Gamma(\xi)}&\qquad\text{if }\sigma\_{t}^{2}\nu\_{t}>-1/k\text{ and }\nu\_{t}\neq 0\\[10.00002pt] \mu\_{t}^{k}\,\exp(k^{2}\sigma\_{t}^{2}/2)&\qquad\text{if }\nu\_{t}=0\\[10.00002pt] \infty&\qquad\text{if }\sigma\_{t}^{2}\nu\_{t}\leqslant-1/k\;.\end{cases} |  |

Note that the kk-th moment exists if and only if σt2​νt>−1/k\sigma\_{t}^{2}\nu\_{t}>-1/k. Thus, the larger the tail-index σt2​νt\sigma\_{t}^{2}\nu\_{t}, the more moments exist, with all of them existing whenever νt⩾0\nu\_{t}\geqslant 0.
Moreover, the mean and variance are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | 𝔼​(Xt)\displaystyle\mathbb{E}(X\_{t}) | ={μt​γt​1ξ1/νt​γt​0if ​νt≠0μt​exp⁡(σt2/2)if ​νt=0,and\displaystyle=\begin{cases}\displaystyle\mu\_{t}\,\frac{\gamma\_{t1}}{\xi^{1/\nu\_{t}}\gamma\_{t0}}&\quad\text{if }\nu\_{t}\neq 0\\[10.00002pt] \mu\_{t}\,\exp(\sigma\_{t}^{2}/2)&\quad\text{if }\nu\_{t}=0\;,\quad\text{and}\quad\end{cases} |  | (3a) |
|  | 𝕍​ar​(Xt)\displaystyle\mathbb{V}\mathrm{ar}(X\_{t}) | ={μt2​(γt​0​γt​2−γt​12)(ξ1/νt​γt​0)2if ​νt≠0μt2​{exp⁡(2​σt2)−exp⁡(σt2)}if ​νt=0,\displaystyle=\begin{cases}\displaystyle\mu\_{t}^{2}\,\frac{(\gamma\_{t0}\gamma\_{t2}-\gamma\_{t1}^{2})}{(\xi^{1/\nu\_{t}}\gamma\_{t0})^{2}}&\text{if }\nu\_{t}\neq 0\\[10.00002pt] \mu\_{t}^{2}\,\{\exp(2\sigma\_{t}^{2})-\exp(\sigma\_{t}^{2})\}&\text{if }\nu\_{t}=0\;,\\ \end{cases} |  | (3b) |

where γt​k:=Γ​(ξt+k/νt)\gamma\_{tk}:=\Gamma(\xi\_{t}+k/\nu\_{t}), provided that σt2​νt>−1\sigma\_{t}^{2}\nu\_{t}>-1 and σt2​νt>−1/2\sigma\_{t}^{2}\nu\_{t}>-1/2, respectively.

### 2.3 Purely seasonal model

To incorporate periodicity in the parameters (μt,σt,νt)(\mu\_{t},\sigma\_{t},\nu\_{t}), we include as covariates, in (𝒂μ​t,𝒂σ​t,𝒂ν​t)(\bm{a}\_{\mu t},\bm{a}\_{\sigma t},\bm{a}\_{\nu t}) of ([1](https://arxiv.org/html/2510.18639v1#S2.E1 "In 2.1 Model setting ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows")), so-called Fourier basis functions, that is, pairs of functions Ck​(t)=cos⁡(2​π​k​t/p)C\_{k}(t)=\cos(2\pi kt/p) and Sk​(t)=sin⁡(2​π​k​t/p)S\_{k}(t)=\sin(2\pi kt/p) for some integer values of frequencies kk and where p∈ℕ+p\in\mathbb{N}\_{+} is the cycle length.
Specifically, when defining a purely seasonal model, we suppose that for each parameter θt∈{μt,σt,νt}\theta\_{t}\in\{\mu\_{t},\sigma\_{t},\nu\_{t}\} and all t∈ℝt\in\mathbb{R}, the link functions satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | gθ​(θt):=𝒂θ​t⊺​𝜷θ=βθ​0+∑k=1dθ{βθ​kc​Ck​(t)+βθ​ks​Sk​(t)},g\_{\theta}(\theta\_{t}):=\bm{a}\_{\theta t}^{\intercal}\bm{\beta}\_{\theta}=\beta\_{\theta 0}+\sum\_{k=1}^{d\_{\theta}}\Big\{\beta\_{\theta k}^{c}C\_{k}(t)+\beta\_{\theta k}^{s}S\_{k}(t)\Big\}\;, |  | (4) |

where 𝜷θ:=(βθ​0,{βθ​kc,βθ​ks}k⩽dθ)\bm{\beta}\_{\theta}:=\big(\beta\_{\theta 0},\{\beta\_{\theta k}^{c},\beta\_{\theta k}^{s}\}\_{k\leqslant d\_{\theta}}\big) concatenates βθ​0\beta\_{\theta 0}, βθ​kc\beta\_{\theta k}^{c}, and βθ​ks\beta\_{\theta k}^{s} (k⩽dθk\leqslant d\_{\theta}) to a vector of length 2​dθ+12d\_{\theta}+1. Similarly we have a 2​dθ+12d\_{\theta}+1 dimensional vector of covariates 𝒂θ​t:=(1,{Ck​(t)+Sk​(t)}k⩽dθ)\bm{a}\_{\theta t}:=\big(1,\{C\_{k}(t)+S\_{k}(t)\}\_{k\leqslant d\_{\theta}}\big) and dθd\_{\theta} is either specified by the user, or learned via model selection (see Section [3.3](https://arxiv.org/html/2510.18639v1#S3.SS3 "3.3 Model selection ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")).
Implicit in ([4](https://arxiv.org/html/2510.18639v1#S2.E4 "In 2.3 Purely seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows")) is that we allow a given sine-cosine pair to be included only if all pairs of smaller integer frequency are also included.

To better interpret the linear predictor in ([4](https://arxiv.org/html/2510.18639v1#S2.E4 "In 2.3 Purely seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows")), note that for a given frequency kk, the pair of coefficients (βθ​kc,βθ​ks)(\beta\_{\theta k}^{c},\beta\_{\theta k}^{s}) can be jointly interpreted as a transformation of the amplitude and phase parameters (αθ​k,ρθ​k)(\alpha\_{\theta k},\rho\_{\theta k}) of a single frequency kk cosine term.
This is seen by letting βθ​kc=αθ​k​cos⁡(ρθ​k)\beta\_{\theta k}^{c}=\alpha\_{\theta k}\cos(\rho\_{\theta k}) and βθ​ks=αθ​k​sin⁡(ρθ​k)\beta\_{\theta k}^{s}=\alpha\_{\theta k}\sin(\rho\_{\theta k}), so that

|  |  |  |
| --- | --- | --- |
|  | αθ​k​cos⁡(2​π​k​t/p−ρθ​k)=βθ​kc​Ck​(t)+βθ​ks​Sk​(t).\alpha\_{\theta k}\cos\big(2\pi kt/p-\rho\_{\theta k}\big)=\beta\_{\theta k}^{c}C\_{k}(t)+\beta\_{\theta k}^{s}S\_{k}(t)\;. |  |

While the amplitude-phase representation is more intuitive, the sine-cosine formulation enables expressing gθ​(θt)g\_{\theta}(\theta\_{t}) as a linear predictor, which is better suited for optimization routines.

### 2.4 Dynamic seasonal model

The model presented in Section [2.3](https://arxiv.org/html/2510.18639v1#S2.SS3 "2.3 Purely seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows") is essentially that proposed in [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)].
In the present paper, we further allow the periodic pattern, including the intercept, to evolve over time.
We do so by including the time-index tt as a covariate, effectively creating a linear time trend, as well as interactions between tt and the sine-cosine pairs.
In fact, as we mentioned in Section [2](https://arxiv.org/html/2510.18639v1#S2 "2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows"), the model can in theory also contain higher-order polynomials. However, including both higher-order polynomials and interactions with the sine-cosine terms may introduce unnecessary complexity, so we opt for a simpler model. Concretely, we consider

|  |  |  |  |
| --- | --- | --- | --- |
|  | gθ​(θt)=βθ​0+βθ​0t​t+∑k=1dθ{βθ​kc​Ck​(t)+βθ​ks​Sk​(t)}+∑k′=1pθ{βθ​k′c​t​Ck′​(t)+βθ​k′s​t​Sk′​(t)}​t,g\_{\theta}(\theta\_{t})=\beta\_{\theta 0}+\beta\_{\theta 0}^{t}t+\sum\_{k=1}^{d\_{\theta}}\Big\{\beta\_{\theta k}^{c}C\_{k}(t)+\beta\_{\theta k}^{s}S\_{k}(t)\Big\}+\sum\_{k^{\prime}=1}^{p\_{\theta}}\Big\{\beta\_{\theta k^{\prime}}^{ct}C\_{k^{\prime}}(t)+\beta\_{\theta k^{\prime}}^{st}S\_{k^{\prime}}(t)\Big\}\,t\;, |  | (5) |

where pθp\_{\theta} is constrained such that pθ⩽dθp\_{\theta}\leqslant d\_{\theta} and, like dθd\_{\theta}, can be either specified by the user, or learned via model selection (see Section [3.3](https://arxiv.org/html/2510.18639v1#S3.SS3 "3.3 Model selection ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")). As before, interactions with sine-cosine pairs of a given frequency are permitted only if all lower-frequency pairs are also included, both individually and in interaction with tt (of frequency k′=1k^{\prime}=1). In particular, we require the inclusion of the linear time trend (i.e., the interaction at frequency zero) as a prerequisite for including any higher-frequency interactions.

We summarize the structure of the linear predictor associated with θt\theta\_{t} using the notation 𝒮θ=(dθ,pθ)\mathcal{S}\_{\theta}=(d\_{\theta},p\_{\theta}), where dθ,pθ∈{0,1,…,}d\_{\theta},p\_{\theta}\in\{0,1,\dots,\} and dθ⩽pθd\_{\theta}\leqslant p\_{\theta}. For example, 𝒮θ=(2,1)\mathcal{S}\_{\theta}=(2,1) indicates a model with an intercept, two sine-cosine pairs (of frequency k=1k=1 and k=2k=2), a time trend, and an interaction between the frequency one pair and tt. For purely seasonal models, we use the notation 𝒮θ=(dθ,−)\mathcal{S}\_{\theta}=(d\_{\theta},-); e.g., 𝒮θ=(0,−)\mathcal{S}\_{\theta}=(0,-) indicates a model with only an intercept.

## 3 Model fitting procedure

### 3.1 Objective function

In Sections [2.3](https://arxiv.org/html/2510.18639v1#S2.SS3 "2.3 Purely seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows") and [2.4](https://arxiv.org/html/2510.18639v1#S2.SS4 "2.4 Dynamic seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows"), we introduced coefficients 𝜷:=(𝜷μ,𝜷σ,𝜷ν)\bm{\beta}:=(\bm{\beta}\_{\mu},\bm{\beta}\_{\sigma},\bm{\beta}\_{\nu}) that, along with the link functions and design matrices, fully determine the value of the marginal parameters (μt,σt,νt)(\mu\_{t},\sigma\_{t},\nu\_{t}) at any time tt.
Although our primary interest lies in the marginal parameters, model estimation is conducted by maximizing an objective that is a function of 𝜷\bm{\beta}.
Specifically, given a dataset of river flows 𝑿\bm{X}, we obtain estimates 𝜷^\bm{\hat{\beta}} of 𝜷\bm{\beta} by maximizing

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(𝜷|𝑿):=∑t∈𝒯log⁡f​(Xt|μt,σt,νt),\ell(\bm{\beta}|\bm{X}):=\sum\_{t\in\mathcal{T}}\log f(X\_{t}|\mu\_{t},\sigma\_{t},\nu\_{t})\;, |  | (6) |

where 𝝁:=(μt)t∈𝒯:=gμ−1​(𝑨μ​𝜷μ)\bm{\mu}:=(\mu\_{t})\_{t\in\mathcal{T}}:=g\_{\mu}^{-1}(\bm{A}\_{\mu}\bm{\beta}\_{\mu}), 𝝈:=(σt)t∈𝒯:=gσ−1​(𝑨σ​𝜷σ)\bm{\sigma}:=(\sigma\_{t})\_{t\in\mathcal{T}}:=g\_{\sigma}^{-1}(\bm{A}\_{\sigma}\bm{\beta}\_{\sigma}) and 𝝂:=(νt)t∈𝒯:=gν−1​(𝑨ν​𝜷ν)\bm{\nu}:=(\nu\_{t})\_{t\in\mathcal{T}}:=g\_{\nu}^{-1}(\bm{A}\_{\nu}\bm{\beta}\_{\nu}).
Note that our objective function is in fact the log-likelihood for independent observations drawn from the marginal model of Section [2.2](https://arxiv.org/html/2510.18639v1#S2.SS2 "2.2 Univariate model for river flows ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows").
This simplifying (working) assumption of independence, that is, intentionally ignoring potential temporal dependence between observations, is made to avoid the complexities of modelling temporal structure, which is often challenging for natural phenomena such as river flows.

In view of this latter fact, and the GAMLSS-like structure of ([5](https://arxiv.org/html/2510.18639v1#S2.E5 "In 2.4 Dynamic seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows")), our model can be interpreted as a misspecified GAMLSS.
In cases where νt\nu\_{t} is bounded away from zero for all tt, one may use existing statistical software that implements the standard generalized gamma distribution [[23](https://arxiv.org/html/2510.18639v1#bib.bibx23), [24](https://arxiv.org/html/2510.18639v1#bib.bibx24), e.g., the R package gamlss] to maximize ([6](https://arxiv.org/html/2510.18639v1#S3.E6 "In 3.1 Objective function ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")).
However, we expect the lognormal distribution to provide a reasonable fit for river flow data, making it likely that νt\nu\_{t} hovers around zero for some tt.
As a consequence, maximizing ([6](https://arxiv.org/html/2510.18639v1#S3.E6 "In 3.1 Objective function ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")) as explicitly defined via ([2](https://arxiv.org/html/2510.18639v1#S2.E2 "In 2.2 Univariate model for river flows ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows")) may be numerically unstable.
To alleviate these difficulties, we rely on the implementation of the extended generalized gamma distribution provided by [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)], which uses (Taylor and Stirling’s formula) approximations to handle cases when ν\nu is small or ξ\xi is large.

### 3.2 Inference for misspecified models

Using independence as a working assumption simplifies the model but introduces complications for inference.
With correctly specified models, inference is usually based on the classical asymptotic theory that exploits the second Bartlett identity. The identity states that the Fisher information matrix ℐ𝜷:=−𝔼​(∇𝜷2ℓ​(𝜷|𝑿))\mathcal{I}\_{\bm{\beta}}:=-\mathbb{E}\big(\nabla\_{\bm{\beta}}^{2}\ell(\bm{\beta}|\bm{X})\big) coincides with the variance of the score function 𝒦𝜷:=𝕍​ar​(∇𝜷ℓ​(𝜷|𝑿))\mathcal{K}\_{\bm{\beta}}:=\mathbb{V}\mathrm{ar}\big(\nabla\_{\bm{\beta}}\ell(\bm{\beta}|\bm{X})\big).
When the model is misspecified, this identity no longer holds.
Nevertheless, under suitable regularity conditions, the estimator 𝜷^\bm{\hat{\beta}} remains asymptotically normal.
Its covariance matrix takes the so-called sandwich form, that is, 𝕍​ar​(𝜷^)≈𝒢𝜷:=ℐ𝜷​𝒦𝜷−1​ℐ𝜷\mathbb{V}\mathrm{ar}(\bm{\hat{\beta}})\approx\mathcal{G}\_{\bm{\beta}}:=\mathcal{I}\_{\bm{\beta}}\mathcal{K}\_{\bm{\beta}}^{-1}\mathcal{I}\_{\bm{\beta}}. More precisely

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​(𝜷^−𝜷)↝𝒩​(𝟎,𝔊𝜷−1)as ​n:=|𝒯|→∞.\sqrt{n}(\bm{\hat{\beta}}-\bm{\beta})\rightsquigarrow\mathcal{N}(\bm{0},\mathfrak{G}\_{\bm{\beta}}^{-1})\quad\text{as }n:=|\mathcal{T}|\to\infty\;. |  | (7) |

where 𝔊𝜷:=ℑ𝜷​𝔎𝜷−1​ℑ𝜷\mathfrak{G}\_{\bm{\beta}}:=\mathfrak{I}\_{\bm{\beta}}\mathfrak{K}\_{\bm{\beta}}^{-1}\mathfrak{I}\_{\bm{\beta}} and ℑ𝜷\mathfrak{I}\_{\bm{\beta}} and 𝔎𝜷\mathfrak{K}\_{\bm{\beta}} are such that ℐ𝜷/n→ℑ𝜷\mathcal{I}\_{\bm{\beta}}/n\to\mathfrak{I}\_{\bm{\beta}} and 𝒦𝜷/n→𝔎𝜷\mathcal{K}\_{\bm{\beta}}/n\to\mathfrak{K}\_{\bm{\beta}}, as n→∞n\to\infty.

To perform inference based on ([7](https://arxiv.org/html/2510.18639v1#S3.E7 "In 3.2 Inference for misspecified models ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")), we require a consistent estimator 𝒢^𝜷\hat{\mathcal{G}}\_{\bm{\beta}} of 𝒢𝜷\mathcal{G}\_{\bm{\beta}}, in the sense that 𝒢^𝜷/n→𝔊𝜷\hat{\mathcal{G}}\_{\bm{\beta}}/n\to\mathfrak{G}\_{\bm{\beta}} in probability as n→∞n\to\infty, or alternatively, a resampling method that achieves this consistency implicitly.
In this work, we use a sandwich-type estimator, i.e., of the form 𝒢^𝜷−1=ℐ^𝜷−1​𝒦^𝜷​ℐ^𝜷−1\hat{\mathcal{G}}\_{\bm{\beta}}^{-1}=\hat{\mathcal{I}}\_{\bm{\beta}}^{-1}\hat{\mathcal{K}}\_{\bm{\beta}}\hat{\mathcal{I}}\_{\bm{\beta}}^{-1}, based on consistent estimators of ℐ𝜷\mathcal{I}\_{\bm{\beta}} and 𝒦𝜷\mathcal{K}\_{\bm{\beta}} computed from the fitted null model.
The estimation of ℐ𝜷\mathcal{I}\_{\bm{\beta}} is relatively straightforward, but that of 𝒦𝜷\mathcal{K}\_{\bm{\beta}} requires greater care due to the temporal dependence among the individual score contributions; as the usual assumption of independence among summands in ∇𝜷ℓ​(𝜷|𝑿)=∑t∈𝒯∇𝜷ℓ​(𝜷|Xt)\nabla\_{\bm{\beta}}\ell(\bm{\beta}|\bm{X})=\sum\_{t\in\mathcal{T}}\nabla\_{\bm{\beta}}\ell(\bm{\beta}|X\_{t}) does not hold. A common approach consists of using a weighted sample variance [[4](https://arxiv.org/html/2510.18639v1#bib.bibx4), [14](https://arxiv.org/html/2510.18639v1#bib.bibx14), see, e.g.,], where covariances between score terms are downweighted as their temporal separation increases. In this work, we adopt the Tukey-Hanning weighting scheme with a 31-day bandwidth, that is, assigning zero weight to covariances between observations separated by more than 31 days. See [[20](https://arxiv.org/html/2510.18639v1#bib.bibx20)] for more details on the sandwich estimator that we use and some alternatives, and [[14](https://arxiv.org/html/2510.18639v1#bib.bibx14)] for a useful discussion that connects related approaches.

Given an estimate of 𝒢𝜷\mathcal{G}\_{\bm{\beta}}, we can compute approximate confidence intervals for the parameters in the standard fashion using normal quantiles.
Similarly, hypothesis tests can be performed using test statistics of the form (𝜷^−𝜷)⊤​𝒢^𝜷​(𝜷^−𝜷)(\bm{\hat{\beta}}-\bm{\beta})^{\top}\hat{\mathcal{G}}\_{\bm{\beta}}(\bm{\hat{\beta}}-\bm{\beta}), which in view of ([7](https://arxiv.org/html/2510.18639v1#S3.E7 "In 3.2 Inference for misspecified models ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")) is asymptotically χ2\chi^{2} as n→∞n\to\infty.
For example, one may test the hypothesis H0:νt=0H\_{0}:\nu\_{t}=0 for all tt (reducing the generalized gamma to a log-normal), which can be restated as H0:𝜷ν=𝟎H\_{0}:\bm{\beta}\_{\nu}=\bm{0}, by comparing 𝜷^ν⊤​𝒢^𝜷,ν​𝜷^ν\bm{\hat{\beta}}\_{\nu}^{\top}\hat{\mathcal{G}}\_{\bm{\beta},\nu}\bm{\hat{\beta}}\_{\nu} to the quantiles of the χdν2\chi\_{d\_{\nu}}^{2} distribution with dνd\_{\nu} degrees of freedom; here 𝒢^𝜷,ν\hat{\mathcal{G}}\_{\bm{\beta},\nu} is the inverse of the submatrix of 𝒢^𝜷−1\hat{\mathcal{G}}\_{\bm{\beta}}^{-1} associated with 𝜷^ν\bm{\hat{\beta}}\_{\nu}.

### 3.3 Model selection

The construction of confidence intervals discussed in Section [3.2](https://arxiv.org/html/2510.18639v1#S3.SS2 "3.2 Inference for misspecified models ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows") assumes that a working model has been specified a priori, i.e., that for each parameter θ\theta, the quantities dθd\_{\theta} and pθ​kp\_{\theta k} are given.
When the model structure is uncertain, a method is needed to select a suitable, yet parsimonious model.
This can be achieved either through penalization or by applying an appropriate information criterion.
Given the strict order in which we want to introduce new sine-cosine pairs, time trends and their interactions, we adopt a stepwise procedure that builds a sequence of candidate models of increasing complexity.

To initialize the model structure, we use as linear predictors only intercepts:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(μt)=βμ​0,log⁡(σt)=βσ​0,andνt=βν​0,\log(\mu\_{t})=\beta\_{\mu 0}\;,\quad\log(\sigma\_{t})=\beta\_{\sigma 0}\;,\quad\text{and}\quad\nu\_{t}=\beta\_{\nu 0}\;, |  | (8) |

which, in the notation introduced in Section [2.4](https://arxiv.org/html/2510.18639v1#S2.SS4 "2.4 Dynamic seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows"), is summarized by 𝒮μ=𝒮σ=𝒮ν=(0,−)\mathcal{S}\_{\mu}=\mathcal{S}\_{\sigma}=\mathcal{S}\_{\nu}=(0,-).
Then, given this model (or any subsequent one), we generate a set of candidate models (see below) and identify that corresponding to the highest relative increase of the objective function, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓk+1−ℓkqk+1−qk,\frac{\ell\_{k+1}-\ell\_{k}}{q\_{k+1}-q\_{k}}\;, |  | (9) |

where ℓk\ell\_{k} and ℓk+1\ell\_{k+1} are the values of the objective (misspecified likelihood) for the base and candidate models, respectively, and qkq\_{k} and qk+1q\_{k+1} the total number of coefficients they respectively involve. Using the ratio of increases in the objective and number of parameters favours a fairer comparison of candidate models of distinct complexity.

When building a purely seasonal model, we generate the candidate models as follows. Given the model in ([8](https://arxiv.org/html/2510.18639v1#S3.E8 "In 3.3 Model selection ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")), or any subsequent model, we generate six new candidates by further updating either of the three linear predictors in one of the following two ways: (i) 𝒮θ=(k,−)←𝒮θ=(k+1,−)\mathcal{S}\_{\theta}=(k,-)\leftarrow\mathcal{S}\_{\theta}=(k+1,-), or (ii) 𝒮θ=(k,−)←𝒮θ=(k+2,−)\mathcal{S}\_{\theta}=(k,-)\leftarrow\mathcal{S}\_{\theta}=(k+2,-).
In other words, we increase the number of sine-cosine pairs by either one or two. Considering increases of size two allows us, using parallel computations, to speed up the exploration of the parameter space, but more importantly to overcome the possibility that a sine-cosine pair of low relative impact on the objective prevents the algorithm to reach a better model with a few more parameters; a phenomenon that we have witnessed in preliminary tests. We proceed similarly when building a dynamic seasonal model, by further allowing the update (iii) 𝒮θ=(k,r)←𝒮θ=(k,r+1)\mathcal{S}\_{\theta}=(k,r)\leftarrow\mathcal{S}\_{\theta}=(k,r+1), and (iv) 𝒮θ=(k,r)←𝒮θ=(k,r+2)\mathcal{S}\_{\theta}=(k,r)\leftarrow\mathcal{S}\_{\theta}=(k,r+2), provided that r+1⩽kr+1\leqslant k and r+2⩽kr+2\leqslant k, respectively. When updating the model for first time, that is from 𝒮θ=(k,−)\mathcal{S}\_{\theta}=(k,-) to 𝒮θ=(k,c)\mathcal{S}\_{\theta}=(k,c), c∈ℕc\in\mathbb{N}, we interpret the dash in 𝒮θ=(k,−)\mathcal{S}\_{\theta}=(k,-) as −1-1. Note that when the base model is a purely seasonal, we do not consider the update (iv), which adds interactions between the time trend and the sin-cosine basis. This strategy introduces the time trend first before adding interaction terms. This leads to at most 1212 candidates models.

We iterate the above procedure multiple times to create a sequence of models {(𝒮μ(k),𝒮σ(k),𝒮ν(k))}k=0K\{(\mathcal{S}\_{\mu}^{(k)},\mathcal{S}\_{\sigma}^{(k)},\mathcal{S}\_{\nu}^{(k)})\}\_{k=0}^{K}, where KK is such that (𝒮μ(K),𝒮σ(K),𝒮ν(K))(\mathcal{S}\_{\mu}^{(K)},\mathcal{S}\_{\sigma}^{(K)},\mathcal{S}\_{\nu}^{(K)}) is clearly overparametrized.
From this sequence, we select a model using Takeuchi’s information criterion [[27](https://arxiv.org/html/2510.18639v1#bib.bibx27), TIC], defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | −ℓ​(𝜷^|𝑿)+2​trace​(𝒦^𝜷​ℐ^𝜷−1),-\ell(\bm{\hat{\beta}}|\bm{X})+2\;\mathrm{trace}(\hat{\mathcal{K}}\_{\bm{\beta}}\hat{\mathcal{I}}\_{\bm{\beta}}^{-1})\;, |  | (10) |

where ℐ^𝜷\hat{\mathcal{I}}\_{\bm{\beta}} and 𝒦^𝜷\hat{\mathcal{K}}\_{\bm{\beta}} are as described in Section [3.2](https://arxiv.org/html/2510.18639v1#S3.SS2 "3.2 Inference for misspecified models ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows") and are computed for each candidate model.
The second term in ([10](https://arxiv.org/html/2510.18639v1#S3.E10 "In 3.3 Model selection ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")) serves a role analogous to the dimensionality penalty in the more standard Akaike information criterion [[1](https://arxiv.org/html/2510.18639v1#bib.bibx1), AIC], but it is adapted to accommodate model misspecification. While it is common to select a final model by minimized TIC, we use it more as an analytic tool to guide model selection, to guard against the potential effects of the uncertainty in the estimation of ℐ𝜷\mathcal{I}\_{\bm{\beta}} and 𝒦𝜷\mathcal{K}\_{\bm{\beta}}.

### 3.4 Diagnostics

To assess the fit of a given model we analyse the normalized pseudo-observations (z-scores) given by Φ−1​(F​(Xt|μt,σt,νt))\Phi^{-1}(F(X\_{t}|\mu\_{t},\sigma\_{t},\nu\_{t})), where FF is the generalized gamma cdf and Φ−1\Phi^{-1} denotes the quantile function of the standard Gaussian distribution.
Expressing the residuals on the standard normal scale allows for intuitive assessment using standard normal-based diagnostics in statistical modelling.
In particular, we visually assess the fit by means of quantile-to-quantile plots (QQ-plots), that is, by plotting the z-scores against the theoretical quantile of the standard Gaussian distribution.
Since model performance may vary over the seasonal cycle, it is also useful to stratify the z-scores by month, to evaluate whether the model performs consistently throughout the year. Examples of this methodology are shown in Figures [3](https://arxiv.org/html/2510.18639v1#S4.F3 "Figure 3 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")–[9](https://arxiv.org/html/2510.18639v1#S4.F9 "Figure 9 ‣ 4.4 Joint dynamic seasonal models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows").

## 4 Application to river flow

### 4.1 Data and models

To illustrate our methodology, we consider river flow data (daily average flow in  m3/s\text{\,}\mathrm{m}^{3}\mathrm{/}\mathrm{s}) from three distinct hydrometric stations located on the Fraser River in British Columbia (Canada), referred to as stations A, B, and C; their locations are given by Figure [1](https://arxiv.org/html/2510.18639v1#S4.F1 "Figure 1 ‣ 4.1 Data and models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows").

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1: Left panel: Location of the three hydrometric stations on the Fraser River from which the data in Section [4](https://arxiv.org/html/2510.18639v1#S4 "4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows") were collected. Right panel: River flow series for the three stations in 1990, with four additional points marking the major flood event of November 2021 at station A.

As mentioned in the introduction, the Fraser river originates in the Canadian Rocky Mountains, passes through the Fraser Canyon and the Fraser Valley, and finally empties into the Strait of Georgia close to Vancouver. Station A lies at the end of the Fraser Valley and is known for flooding that incur large losses due to its proximity to the city of Vancouver. Station B is upstream and in the Fraser Canyon, thus already significantly closer to the mountains. Station C is in the Fraser Canyon is even further upstream, thus subject to significant snow coverage in winter.

The data consist of uninterrupted series from 1965-05-01 to 1992-12-31 for station A (∼\sim27.67 years, 10,107 observations), 1912-03-01 to 2023-12-31 for station B (∼\sim111.8 years, 40,848 observations), and 1951-08-12 to 2023-12-31 for station C (∼\sim72.4 years, 26,440 observations).

We define three situations based on the available data, chosen to illustrate different aspects of the modelling framework.
We begin with station A, which has the shortest series, and fit a purely seasonal model (Section [2.3](https://arxiv.org/html/2510.18639v1#S2.SS3 "2.3 Purely seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows")), as this is the setting where such a specification is most reasonable.
An additional 1,360 observations are available for this station, but these are mostly concentrated in the May–July months of 2000–2023, and addressing this imbalance lies outside the scope of the paper.
We nevertheless investigate the November 2021 flood shown in Figure [1](https://arxiv.org/html/2510.18639v1#S4.F1 "Figure 1 ‣ 4.1 Data and models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), to illustrate the potential pitfalls of extrapolating beyond the data range by examining its associated estimated return period.
We then turn to station B, which has the longest time data series, and fit the dynamic seasonal model (Section [2.4](https://arxiv.org/html/2510.18639v1#S2.SS4 "2.4 Dynamic seasonal model ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows")). Finally, we illustrate how data from multiple stations, here stations B and C, can be combined to inform the choice of model structure, again in the context of a dynamic seasonal model.

As explained in Section [3.3](https://arxiv.org/html/2510.18639v1#S3.SS3 "3.3 Model selection ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows"), we use TIC to guide us with the selection of the final model. For each of the applications, we include in the computation of 𝒦𝜷\mathcal{K}\_{\bm{\beta}} all covariance terms corresponding to pairs of observations separated by up to 31 days, which we weight using the Tukey-Hanning scheme briefly described in Section [3.2](https://arxiv.org/html/2510.18639v1#S3.SS2 "3.2 Inference for misspecified models ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows"); see also [[4](https://arxiv.org/html/2510.18639v1#bib.bibx4)]. For the last application, which involves two stations, we also include the between-station covariances that fall within the considered time-windows.
The 31-day bandwidth parameter corresponds roughly to n3/8n^{3/8}, n1/3n^{1/3}, and n4/9n^{4/9} for the three applications in their respective order. Some tests with smaller (20) and larger (60) bandwidth parameters suggests that the results are robust to this choice.

### 4.2 Purely seasonal model

We begin by fitting a purely seasonal model to the n=10,107n=10,107 observations from station A. To provide a more concrete description of our procedure, we explain the first few steps of the algorithm.

![Refer to caption](x3.png)


Figure 2: Scaled negative log-likelihood (solid line) and scaled Takeuchi Information Criterion (dashed line) for the purely seasonal model fitted to station A. Values are plotted against the total number of coefficients used in the linear predictors for μt\mu\_{t}, σt\sigma\_{t}, and νt\nu\_{t}; the scaling factor for the y-axis is 10−310^{-3}. Left panel: Overall behaviour across all models on the path. Right panel: Closer view of the region where the criteria stabilize, with the selected model circled.

A depiction of the full model selection procedure is given by Figure [2](https://arxiv.org/html/2510.18639v1#S4.F2 "Figure 2 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"). It displays the evolution of the TIC criterion, the parameter whose linear predictor was updated at each step, and the total number of coefficients after each update.
As shown therein, fitting the base model in ([8](https://arxiv.org/html/2510.18639v1#S3.E8 "In 3.3 Model selection ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows")) results in a TIC value of ∼\sim179,893.
From this initial model, the algorithm evaluates potential updates to the linear predictor of each parameter θt∈{μt,σt,νt}\theta\_{t}\in\{\mu\_{t},\sigma\_{t},\nu\_{t}\}. That is for a given parameter, we consider the two candidate linear predictors given by

|  |  |  |
| --- | --- | --- |
|  | gθ​(θt)=βθ​0+βθ​1c​C1​(t)+βθ​1s​S1​(t),andgθ​(θt)=βθ​0+∑k=12βθ​kc​Ck​(t)+βθ​ks​Sk​(t),g\_{\theta}(\theta\_{t})=\beta\_{\theta 0}+\beta\_{\theta 1}^{c}C\_{1}(t)+\beta\_{\theta 1}^{s}S\_{1}(t)\;,\quad\text{and}\quad g\_{\theta}(\theta\_{t})=\beta\_{\theta 0}+\sum\_{k=1}^{2}\beta\_{\theta k}^{c}C\_{k}(t)+\beta\_{\theta k}^{s}S\_{k}(t)\;, |  |

where gθg\_{\theta} is the parameter-dependent link function. The two models are denoted 𝒮θ=(1,−)\mathcal{S}\_{\theta}=(1,-) and 𝒮θ=(2,−)\mathcal{S}\_{\theta}=(2,-), respectively.
Among the six models generated (two for each of {μt,σt,νt}\{\mu\_{t},\sigma\_{t},\nu\_{t}\}), 𝒮μ​(1,−)\mathcal{S}\_{\mu}(1,-) achieves the largest decrease in relative negative log-likelihood per additional parameter (see criterion ([9](https://arxiv.org/html/2510.18639v1#S3.E9 "In 3.3 Model selection ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows"))), and is therefore selected as the new base model.
In fact, this update, going from 𝒮μ=(k,−)\mathcal{S}\_{\mu}=(k,-) to 𝒮μ=(k+1,−)\mathcal{S}\_{\mu}=(k+1,-), is applied four times in a row in the first steps of the algorithm, resulting in the intermediate model given by 𝒮μ=(4,−)\mathcal{S}\_{\mu}=(4,-) and 𝒮σ=𝒮ν=(0,−)\mathcal{S}\_{\sigma}=\mathcal{S}\_{\nu}=(0,-), and a cumulative reduction of ∼\sim17,421 in TIC.
The first two updates account for most of this reduction, ∼\sim12,033 and ∼\sim4,526, respectively.
This is intuitive, as μt\mu\_{t} is closely linked to the mean of the distribution and thus captures the strong seasonal pattern evident in the right panel of Figure [1](https://arxiv.org/html/2510.18639v1#S4.F1 "Figure 1 ‣ 4.1 Data and models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows").

Subsequently, the algorithm applies two analogous updates to σt\sigma\_{t} yielding 𝒮σ=(2,−)\mathcal{S}\_{\sigma}=(2,-), and a single update to νt\nu\_{t} yielding 𝒮ν=(2,−)\mathcal{S}\_{\nu}=(2,-). This model, given by
𝒮μ=(4,−)\mathcal{S}\_{\mu}=(4,-) and 𝒮σ=𝒮ν=(2,−)\mathcal{S}\_{\sigma}=\mathcal{S}\_{\nu}=(2,-),
corresponds to a TIC value of ∼\sim162,175 and turns out to be the minimum attained by any of the 23 models visited by the algorithm before the early stopping criterion (15 iterations without improving the current best TIC) was triggered.
Note that, after the 88th iteration, some updates do lead to decreases in TIC relative to the immediately preceding model, but these reductions are not large enough to offset earlier increases.
We conclude that the 8th model is the most appropriate choice for the final model.

We assess the fit provided by our final model using the QQ-plots described in Section [3.4](https://arxiv.org/html/2510.18639v1#S3.SS4 "3.4 Diagnostics ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows") and plotted in Figure [3](https://arxiv.org/html/2510.18639v1#S4.F3 "Figure 3 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"). The QQ-plot based on the full dataset (left panel of Figure [3](https://arxiv.org/html/2510.18639v1#S4.F3 "Figure 3 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")) suggests that the model performs very well overall. However, the QQ-plots specific to the months of March–July (see right panel of Figure [3](https://arxiv.org/html/2510.18639v1#S4.F3 "Figure 3 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")) show some noticeable deviations in the tails. These may reflect the absence of a time trend in the model, which could disproportionately affect those months. Alternatively, the data may not be rich enough to support the addition of higher-frequency terms, even if such features would ultimately be necessary to capture the seasonal variation for these months. In this context, using B-splines might offer a more flexible alternative. It is important to note, however, that departures from a straight line can be more pronounced than usual when the residuals are not independent, as is the case here, and should thus be interpreted with caution.

![Refer to caption](x4.png)

![Refer to caption](x5.png)

Figure 3: QQ-plots of normalized residuals for the purely seasonal model fitted to station A. Left panel: Global QQ-plot. Right panel: Month-specific QQ-plots.

![Refer to caption](x6.png)


Figure 4: Estimated generalized gamma parameters (μt,σt,νt)(\mu\_{t},\sigma\_{t},\nu\_{t}) and associated statistics (mean, standard deviation, and tail-index σt2​νt\sigma\_{t}^{2}\nu\_{t}) for the purely seasonal model fitted to station A, as a function of the time of the year.

The first three panels of Figure [4](https://arxiv.org/html/2510.18639v1#S4.F4 "Figure 4 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows") depict the seasonal evolution of the estimated parameters, the mean and standard deviation (given in ([3](https://arxiv.org/html/2510.18639v1#S2.E3 "In 2.2 Univariate model for river flows ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows"))), and σ^t2​ν^t\hat{\sigma}\_{t}^{2}\hat{\nu}\_{t}, which can be interpreted as a tail-index. As mentioned in Section [2.2](https://arxiv.org/html/2510.18639v1#S2.SS2 "2.2 Univariate model for river flows ‣ 2 Daily environmental model ‣ Distributional regression for seasonal data: an application to river flows"), the tail-index determines which moments of XtX\_{t} exists, indeed σ^t2​ν^t>−1/k\hat{\sigma}\_{t}^{2}\hat{\nu}\_{t}>-1/k means that all moments up to order kk are finite.
In accordance with the relatively simple form of the linear predictors, the estimated parameters vary smoothly over the year. Recall that we fit a purely seasonal model, thus, the parameters vary periodically and are the same for different years.
For the location parameter μ^t\hat{\mu}\_{t}, we observe in Figure [4](https://arxiv.org/html/2510.18639v1#S4.F4 "Figure 4 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows") a relatively sharp increase during spring, followed by a gradual decrease and a stabilization through the summer and fall, consistent with seasonal streamflow dynamics.
This is also reflected in the shape of the mean and standard deviation, which are driven mostly by the location parameter.
The patterns in σ^t\hat{\sigma}\_{t} and ν^t\hat{\nu}\_{t} are similar to one another, but they attain their peak (in absolute value) at different times. Their combined effect creates a noticeable bump in the standard deviation during the later part of the winter (February) and, to a lesser extent, in the later part of fall (November).
The bottom panel displaying σ^t2​ν^t\hat{\sigma}\_{t}^{2}\hat{\nu}\_{t} suggests that the first four moments exist throughout the seasonal cycle, as σ^t2​ν^t⩾−1/4\hat{\sigma}\_{t}^{2}\hat{\nu}\_{t}\geqslant-1/4 for all tt. In contrast, the fifth moment appears to diverge during the later part of the winter. Although initially surprising, a tentative explanation is that snow cover may be substantial at this time of year (note that the Fraser River originates in the Rocky Mountains), which could in turn allow for unusually large increases in river flow.

While these results are sensible, it is important to keep in mind that the cyclostationarity assumption might be too strong even for such a relatively short time series. This manifest itself, for example, in the estimated return period of the largest flow recorded during the November 2021 flood (on the 15th, see Figure [1](https://arxiv.org/html/2510.18639v1#S4.F1 "Figure 1 ‣ 4.1 Data and models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")), which is well outside the range of the training data.
This model yields a return period of 411,968 years, a highly implause result, even considering that the return period is day-specific (i.e., we expect the river flow on November 15th to exceed that number once every 411,968 years). This result, and for that matter a careful analysis of the data itself, point to the presence of a systematic time trend. Since the flood lies far outside the range of the training sample, it is unsurprising that the purely seasonal model fails to provide a meaningful estimate. When we extend the model to allow linear time trends (without interactions), the estimated day-specific return period decreases to about 129 years, which is of a far more realistic magnitude.

### 4.3 Dynamic seasonal model

We next fit a seasonal model with time trends and interactions to the n=40,848n=40,848 observations from station B. A depiction of the model path travelled by the algorithm is given in Figure [5](https://arxiv.org/html/2510.18639v1#S4.F5 "Figure 5 ‣ 4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows").

![Refer to caption](x7.png)


Figure 5: Scaled negative log-likelihood (solid line) and scaled Takeuchi Information Criterion (dashed line) for the dynamic seasonal model fitted to station B. Values are plotted against the total number of coefficients used in the linear predictors for μt\mu\_{t}, σt\sigma\_{t}, and νt\nu\_{t}; the scaling factor for the y-axis is 10−310^{-3}. Left panel: Overall behaviour across all models on the path. Right panel: Closer view of the region where the criteria stabilize, with the selected model circled in black and the TIC-optimal model circled in gray.

It shows that, the first coefficients added are a few sine-cosine pairs for μt\mu\_{t}, as in the previous case. A few sine-cosine pairs are also again included for σt\sigma\_{t} among the first steps, but this time they are preceded by a time trend for νt\nu\_{t}.
After these, two sine-cosine pairs are added for νt\nu\_{t} and the remaining steps involve mostly time trends or interactions. The algorithm was stopped after 10 iterations that did not improve the current best model in terms of TIC.
As expected, the TIC continues to decrease further along the model selection path, suggesting that models with more parameters remain justifiable – which is in contrast to the more limited dataset from station A – resulting in a TIC-optimal model with significantly more coefficients, 46 in total. This model, given by 𝒮μ=(4,4)\mathcal{S}\_{\mu}=(4,4), 𝒮σ=(5,4)\mathcal{S}\_{\sigma}=(5,4) and 𝒮ν=(2,2)\mathcal{S}\_{\nu}=(2,2) (circled in gray in Figure [5](https://arxiv.org/html/2510.18639v1#S4.F5 "Figure 5 ‣ 4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")), does not, however, seem significantly more advantageous than the model obtained five iterations earlier, which contains 35 coefficients (circled in black in Figure [5](https://arxiv.org/html/2510.18639v1#S4.F5 "Figure 5 ‣ 4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")). Upon further inspection, we chose this latter more parsimonious model, given by 𝒮μ=(4,2)\mathcal{S}\_{\mu}=(4,2), 𝒮σ=(5,−)\mathcal{S}\_{\sigma}=(5,-) and 𝒮ν=(2,2)\mathcal{S}\_{\nu}=(2,2).

We again assess the fit using the QQ-plots described in Section [3.4](https://arxiv.org/html/2510.18639v1#S3.SS4 "3.4 Diagnostics ‣ 3 Model fitting procedure ‣ Distributional regression for seasonal data: an application to river flows"); these are shown in Figure [6](https://arxiv.org/html/2510.18639v1#S4.F6 "Figure 6 ‣ 4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"). As with the purely seasonal model selected for station A in Section [4.2](https://arxiv.org/html/2510.18639v1#S4.SS2 "4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), the QQ-plot based on the full dataset suggest that the fit is overall very good. In contrast to the model for station A, the month-specific QQ-plots, especially those associated with the months of March–July, are significantly more satisfying. We find the fit to be convincing, indicating that the extended generalized gamma distribution is well suited for modelling river flow data.

![Refer to caption](x8.png)

![Refer to caption](x9.png)

Figure 6: QQ-plots of normalized residuals for the dynamic seasonal model fitted to station B. Left panel: Global QQ-plot. Right panel: Month-specific QQ-plots.

![Refer to caption](x10.png)


Figure 7: Estimated generalized gamma parameters (μt,σt,νt)(\mu\_{t},\sigma\_{t},\nu\_{t}) and associated statistics (mean, standard deviation, and tail-index σt2​νt\sigma\_{t}^{2}\nu\_{t}) for the dynamic seasonal model fitted to station B, as a function of the date for years 1920, 1970, and 2020.

To visualize the estimated parameters and related quantities, it is not sufficient, due to the presence of long term time trends, to report a single seasonal cycle (as in Figure [4](https://arxiv.org/html/2510.18639v1#S4.F4 "Figure 4 ‣ 4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")).
To account for the variations over the years, we report in Figure [7](https://arxiv.org/html/2510.18639v1#S4.F7 "Figure 7 ‣ 4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows") the parameter values as well as the corresponding mean, standard deviation and tail-index, for three representative years (1920, 1970, and 2020), spanning most of the data range. We observe the same broad seasonal patterns as for station A, and thus focus here on the aspects linked to the inclusion of time trends and interactions.
One noticeable feature is that the spring peak of the estimated location parameter μ^t\hat{\mu}\_{t}, as well as the estimated mean, occurs progressively earlier over time.
While we do not claim expertise on the subject, this pattern seems consistent with expectations related to climate change.
Another feature is the absence of long-term trend in the final model for σt\sigma\_{t}.
This, however, should be interpreted with caution, since the standard deviation, higher-moments and tail-index, which all involve other parameters, still exhibit long-term trends.
In particular, the results suggest that the tail of the distribution becomes heavier over time during late winter and early spring, and lighter during autumn. It is worth noting, however, that the estimated fourth moment remains finite throughout the entire period.
More broadly, these results are consistent with popular criticisms about the assumption of stationarity (cyclostationarity) when dealing with environmental time series. This is especially true for the return period estimated in Section [4.2](https://arxiv.org/html/2510.18639v1#S4.SS2 "4.2 Purely seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), which corresponds to a date well outside the training data.

### 4.4 Joint dynamic seasonal models

In practice, combining information across nearby stations can provide more stable estimates, though there is a risk of imposing constraints that may not fully capture local differences. While directly sharing parameter values across stations would be inappropriate, sharing structural components provides a more plausible compromise. While the true structure for each station likely differs, pooling the data could reduce the variance enough to outweigh the potential bias introduced by this constraint. To examine this, we jointly fit the dynamic seasonal models to data from stations B and C, recall that stations B and C are on the Fraser River and that station B is downstream of station C (see Figure [1](https://arxiv.org/html/2510.18639v1#S4.F1 "Figure 1 ‣ 4.1 Data and models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")). For the fit, we use the 26,440 dates (1951–2023) for which both stations have observations. More specifically, we fit a distinct model to each station, with parameter values estimated independently, while imposing a shared structure through identical 𝒮μ\mathcal{S}\_{\mu}, 𝒮σ\mathcal{S}\_{\sigma}, and 𝒮ν\mathcal{S}\_{\nu}. The model selection procedure is as in Section [4.3](https://arxiv.org/html/2510.18639v1#S4.SS3 "4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows") with the difference that the objective is the sum of the objective functions of each station-specific model.

The path travelled by the algorithm is reported in Figure [8](https://arxiv.org/html/2510.18639v1#S4.F8 "Figure 8 ‣ 4.4 Joint dynamic seasonal models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows").

![Refer to caption](x11.png)


Figure 8: Scaled negative log-likelihood (solid line) and scaled Takeuchi Information Criterion (dashed line) for the joint dynamic seasonal model fitted to stations B and C. Values are plotted against the total number of coefficients used in the linear predictors for μt\mu\_{t}, σt\sigma\_{t}, and νt\nu\_{t}; the scaling factor for the y-axis is 10−310^{-3}. Left panel: Overall behaviour across all models on the path. Right panel: Closer view of the region where the criteria stabilize, with the selected model circled in black and the TIC-optimal model circled in gray.

We obserce a similar pattern as for the dynamic model for station B alone in Section [4.3](https://arxiv.org/html/2510.18639v1#S4.SS3 "4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), and again we favour a simpler model, namely that given by 𝒮μ=(4,1)\mathcal{S}\_{\mu}=(4,1), 𝒮σ=(4,−)\mathcal{S}\_{\sigma}=(4,-) and 𝒮ν=(2,0)\mathcal{S}\_{\nu}=(2,0) (circled in black in Figure [8](https://arxiv.org/html/2510.18639v1#S4.F8 "Figure 8 ‣ 4.4 Joint dynamic seasonal models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")) to the TIC-optimal one, given by 𝒮μ=(4,3)\mathcal{S}\_{\mu}=(4,3), 𝒮σ=(4,3)\mathcal{S}\_{\sigma}=(4,3) and 𝒮ν=(2,0)\mathcal{S}\_{\nu}=(2,0) (circled in gray in Figure [8](https://arxiv.org/html/2510.18639v1#S4.F8 "Figure 8 ‣ 4.4 Joint dynamic seasonal models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows")). Comparing the final model to that for station B in Section [4.3](https://arxiv.org/html/2510.18639v1#S4.SS3 "4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), we obtain here a model with fewer time trend coefficients, which is consistent with the fact that the time series under study here covers a significantly shorter window of time; these results also carries over to the comparison of the two TIC-optimal models. The QQ-plot assessment for the two stations, shown in Figure [9](https://arxiv.org/html/2510.18639v1#S4.F9 "Figure 9 ‣ 4.4 Joint dynamic seasonal models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), is broadly similar to that observed in Section [4.3](https://arxiv.org/html/2510.18639v1#S4.SS3 "4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows").

![Refer to caption](x12.png)

![Refer to caption](x13.png)

Figure 9: QQ-plots of normalized residuals for the joint dynamic seasonal model fitted to station B and C. Left panel: Global QQ-plot. Right panel: Month-specific QQ-plots.

![Refer to caption](x14.png)


Figure 10: Estimated generalized gamma parameters (μt,σt,νt)(\mu\_{t},\sigma\_{t},\nu\_{t}) and associated statistics (mean, standard deviation, and tail-index σt2​νt\sigma\_{t}^{2}\nu\_{t}) for the joint dynamic seasonal model fitted to stations B and C, as a function of the date for years 1952, 1987, and 2022.

Similar to the dynamic model for station B of Section [4.3](https://arxiv.org/html/2510.18639v1#S4.SS3 "4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"), Figure [10](https://arxiv.org/html/2510.18639v1#S4.F10 "Figure 10 ‣ 4.4 Joint dynamic seasonal models ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows") presents the estimated parameters and related quantities for three representative years spanning the range of the data: 1952, 1987, and 2022. This time, however, the figure now depicts two sets of parameters, one for each station.
We begin by comparing the present results for station B with those obtained in Section [4.3](https://arxiv.org/html/2510.18639v1#S4.SS3 "4.3 Dynamic seasonal model ‣ 4 Application to river flow ‣ Distributional regression for seasonal data: an application to river flows"). Recall that for the single-station model for B, we used all available data for that station, i.e., from 1912 to 2023, while for the joint-station model, that is fitting stations B and C jointly, we only consider data from 1951 to 2023, the dates when both stations have data available.
The two models are broadly consistent, with the main discrepancy arising in ν^t\hat{\nu}\_{t}, which exhibits stronger temporal variation (through interaction effects) in the single-station model. This pattern suggests that the earlier data (pre-1950) exert substantial influence on the fit, indicating that a more deliberate treatment of long-term time trends may be warranted. In particular, the pronounced rise in ν^t\hat{\nu}\_{t} during more recent winters in the single-station model appears questionable, as it may reflect an artifact introduced during optimization to better accommodate early observations.

When comparing the two stations, the main difference emerges in μ^t\hat{\mu}\_{t}. We observe that station C has overall a smaller amount of river flow, which is consistent with the fact that B is downstream from station C and the watershed of station B is significantly larger than that of C.
By contrast, the estimates of σt\sigma\_{t} and νt\nu\_{t} are very similar across stations, raising the question of whether additional constraints in the specifications of their linear predictors should be considered; we return to this matter in the discussion.
These patterns extend to the corresponding mean, standard deviation, and tail-index quantities. The mean and standard deviation for each station exhibit broadly similar shapes, with differences that naturally mirror those seen in μ^t\hat{\mu}\_{t}, while the estimated tail-indices are closely aligned across the two stations.

## 5 Discussion

We offer a convenient and intuitive framework for studying environmental processes, leveraging the theory of misspecified models to avoid explicitly specifying temporal dependence. Conceptually, the model is a distributional regression based on periodic and smoothly varying functions of the time index. In this sense, it can be interpreted as a dynamic climatology: dynamic both because it is conditional on the time of year and because it accounts for changes in climate over time. Indices representing large-scale oscillatory phenomena (e.g., the North Atlantic Oscillation or El Niño–Southern Oscillation indices) could be incorporated to account for quasi-periodic variations in climate, if such conditions are desired [[15](https://arxiv.org/html/2510.18639v1#bib.bibx15), see, e.g.,].

Within our proposed framework, we find that the extended generalized gamma distribution provides a particularly useful family for modelling daily river flows. Beyond offering a flexible and generally good fit, it also allows us to indirectly assess which of two widely used distributions in hydrology, the log-normal (νt=0\nu\_{t}=0) and the gamma (νt=1\nu\_{t}=1), is more appropriate in a given setting. Our empirical results suggest that, at least for the stations considered here, the log-normal distribution generally provides a better fit than the gamma. At the same time, there are indications that the underlying process may shift between regimes during the seasonal cycle, at times resembling a gamma distribution, at others a log-normal, and in some periods extending beyond either classical form, generally on the log-normal side.

For the sake of simplicity, we have not accounted for several potentially important issues. For instance, changes in the observational record could arise from instrument replacement, site relocation, or other measurement artifacts, rather than genuine hydrological variation. For this reason, any applied use of the methodology should ideally be undertaken in collaboration with domain experts (e.g., hydrologists in the case of river flow modelling) familiar with the data sources and their limitations.

Finally, our applications underscore certain technical considerations that merit further attention. The use of Fourier basis functions, while convenient, imposes global smoothness and can generate artifacts that might be avoided with alternative representations such as cyclic B-splines, which act locally. Our model does allow for structural changes through time, but very long data series may require more flexible specifications for the trend component; such flexibility, however, comes with the risk of overfitting rather than underfitting. Other directions worth investigating include addressing seasonal imbalance through appropriate weighting schemes to correct distortions from uneven data distribution across the seasonal cycle, and enhancing the model’s ability to capture tail behaviours, by potentially directly modelling extreme events using extreme-value distributions.

Acknowledgments
S. Pesenti would like to acknowledge support from the Natural Sciences and Engineering Research Council of Canada (RGPIN-2025-05847) and from the Canadian Statistical Sciences Institute (CANSSI). S. Perreault and S. Pesenti are grateful for the support from the Data Science Institute.

## References

* [1]
  H. Akaike
  “A new look at the statistical model identification”
  In *IEEE Transactions on Automatic Control* 19.6, 1974, pp. 716–723
  DOI: [10.1109/TAC.1974.1100705](https://dx.doi.org/10.1109/TAC.1974.1100705)
* [2]
  Hansjörg Albreacher, Maria Laura Battagliola, Martin Bladt, Alaric Ja Müller and Tina Swierczynski
  “Flood occurrence in the European alps: a generalised additive mixed model approach based on lake sediments of the last 1500 years.”
  In *preprint*, 2025
* [3]
  Luigi Amoroso
  “Ricerche intorno alla curva dei redditi”
  In *Ann. Mat. Pura Appl.* 2.1, 1925, pp. 123–159
  DOI: [10.1007/BF02409935](https://dx.doi.org/10.1007/BF02409935)
* [4]
  Donald W.. Andrews
  “Heteroskedasticity and Autocorrelation Consistent Covariance Matrix Estimation”
  In *Econometrica* 59.3
  [Wiley, Econometric Society], 1991, pp. 817–858
  URL: <http://www.jstor.org/stable/2938229>
* [5]
  William A. Gardner, Antonio Napolitano and Luigi Paura
  “Cyclostationarity: Half a century of research”
  In *Signal Processing* 86.4, 2006, pp. 639–697
* [6]
  E.. Gladyshev
  “Periodically and Almost-Periodically Correlated Random Processes with a Continuous Time Parameter”
  In *Theory of Probability & Its Applications* 8.2, 1963, pp. 173–177
  DOI: [10.1137/1108016](https://dx.doi.org/10.1137/1108016)
* [7]
  Khaled Hamed and A Ramachandro Rao
  “Flood frequency analysis”
  Boca Raton, FL: CRC press, 2019
* [8]
  Harry Lee Hurd
  “An Investigation of Periodically Correlated Stochastic Processes”, 1970, pp. 250
* [9]
  Norman L. Johnson, Samuel Kotz and N. Balakrishnan
  “Continuous univariate distributions. Vol. 1”, Wiley Series in Probability and Mathematical Statistics: Applied Probability and Statistics
  New York, NY: Wiley, 1994, pp. xxii+756
* [10]
  Richard H. Jones and William M. Brelsford
  “Time series with periodic structure”
  In *Biometrika* 54.3-4, 1967, pp. 403–408
  DOI: [10.1093/biomet/54.3-4.403](https://dx.doi.org/10.1093/biomet/54.3-4.403)
* [11]
  Nadja Klein
  “Distributional Regression for Data Analysis”
  In *Annual Review of Statistics and Its Application* 11.Volume 11, 2024
  Annual Reviews, 2024, pp. 321–346
  DOI: [https://doi.org/10.1146/annurev-statistics-040722-053607](https://dx.doi.org/https://doi.org/10.1146/annurev-statistics-040722-053607)
* [12]
  John H. Lienhard
  “A statistical mechanical prediction of the dimensionless unit hydrograph”
  In *Journal of Geophysical Research (1896-1977)* 69.24, 1964, pp. 5231–5238
  DOI: [https://doi.org/10.1029/JZ069i024p05231](https://dx.doi.org/https://doi.org/10.1029/JZ069i024p05231)
* [13]
  John H. Lienhard and Paul L. Meyer
  “A Physical Basis for the Generalized Gamma Distribution”
  In *Quarterly of Applied Mathematics* 25.3
  Brown University, 1967, pp. 330–334
  URL: <http://www.jstor.org/stable/43635720>
* [14]
  T. Lumley and P. Heagerty
  “Weighted Empirical Adaptive Variance Estimators for Correlated Data Regression”
  In *J. R. Stat. Soc. B* 61.2, 1999, pp. 459–477
  DOI: [10.1111/1467-9868.00187](https://dx.doi.org/10.1111/1467-9868.00187)
* [15]
  M.. Machado, B.. Botero, J. López, F. Francés, A. Díez-Herrero and G. Benito
  “Flood frequency analysis of historical flood data under stationary and non-stationary modelling”
  In *Hydrology and Earth System Sciences* 19.6, 2015, pp. 2561–2576
  DOI: [10.5194/hess-19-2561-2015](https://dx.doi.org/10.5194/hess-19-2561-2015)
* [16]
  Antonio Napolitano
  “Cyclostationarity: Limits and generalizations”
  In *Signal Processing* 120, 2016, pp. 323–347
  DOI: [https://doi.org/10.1016/j.sigpro.2015.09.013](https://dx.doi.org/https://doi.org/10.1016/j.sigpro.2015.09.013)
* [17]
  Antonio Napolitano
  “Cyclostationarity: New trends and applications”
  In *Signal Processing* 120, 2016, pp. 385–408
  DOI: [https://doi.org/10.1016/j.sigpro.2015.09.011](https://dx.doi.org/https://doi.org/10.1016/j.sigpro.2015.09.011)
* [18]
  Antonio Napolitano
  “Cyclostationary Processes and Time Series”
  Cambridge, MA: Academic Press, 2020
* [19]
  Xiao Pan, Ataur Rahman, Khaled Haddad and Taha B… Ouarda
  “Peaks-over-threshold model in flood frequency analysis: a scoping review”
  In *Stochastic Environmental Research and Risk Assessment* 36.9, 2022, pp. 2419–2435
  DOI: [10.1007/s00477-022-02174-6](https://dx.doi.org/10.1007/s00477-022-02174-6)
* [20]
  Samuel Perreault, Silvana Pesenti and Nancy F. Reid
  “Parametric copula pseudo-observations for seasonal processes with a focus on the generalized gamma distribution” Working paper, 2025
* [21]
  R.. Prentice
  “A Log Gamma Model and Its Maximum Likelihood Estimation”
  In *Biometrika* 61.3
  [Oxford University Press, Biometrika Trust], 1974, pp. 539–544
  URL: <http://www.jstor.org/stable/2334737>
* [22]
  R.. Rigby and D.. Stasinopoulos
  “Generalized Additive Models for Location, Scale and Shape”
  In *J. R. Stat. Soc. C* 54.3, 2005, pp. 507–554
* [23]
  R.. Rigby and D.. Stasinopoulos
  “gamlss: Generalized Additive Models for Location Scale and Shape” R package, 2024
  DOI: [10.32614/CRAN.package.gamlss](https://dx.doi.org/10.32614/CRAN.package.gamlss)
* [24]
  Robert A Rigby, Mikis D Stasinopoulos, Gillian Z Heller and Fernanda De Bastiani
  “Distributions for modeling location, scale, and shape”
  New York, NY: Chapman & Hall/CRC, 2019
* [25]
  E.. Stacy
  “A Generalization of the Gamma Distribution”
  In *Ann. Math. Stat.* 33.3
  Institute of Mathematical Statistics, 1962, pp. 1187–1192
  URL: <http://www.jstor.org/stable/2237889>
* [26]
  E.. Stacy and G.. Mihram
  “Parameter Estimation for a Generalized Gamma Distribution”
  In *Technometrics* 7.3
  [Taylor Francis, Ltd., American Statistical Association, American Society for Quality], 1965, pp. 349–358
  URL: <http://www.jstor.org/stable/1266594>
* [27]
  K Takeuchi
  “Distribution of information number statistics and criteria for adequacy of models (in Japanese)”
  In *Suri-Kagaku (Mathematical Sciences)* 153, 1976, pp. 12–18
* [28]
  Gabriele Villarini, James A. Smith, Francesco Serinaldi, Jerad Bales, Paul D. Bates and Witold F. Krajewski
  “Flood frequency analysis for nonstationary annual peak records in an urban drainage basin”
  In *Advances in Water Resources* 32.8, 2009, pp. 1255–1266
  DOI: [https://doi.org/10.1016/j.advwatres.2009.05.003](https://dx.doi.org/https://doi.org/10.1016/j.advwatres.2009.05.003)