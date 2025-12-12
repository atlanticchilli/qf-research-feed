---
authors:
- Tetsuya Takaishi
doc_id: arxiv:2512.10584v1
family_id: arxiv:2512.10584
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Volatility time series modeling by single-qubit quantum circuit learning
url_abs: http://arxiv.org/abs/2512.10584v1
url_html: https://arxiv.org/html/2512.10584v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tetsuya Takaishi
Hiroshima University of Economics, Hiroshima 731-0192, JAPAN
tt-taka@hue.ac.jp

###### Abstract

We employ single-qubit quantum circuit learning (QCL) to model the dynamics of volatility time series. To assess its effectiveness, we generate synthetic data using the Rational GARCH model, which is specifically designed to capture volatility asymmetry.
Our results show that QCL-based volatility predictions preserve the negative return–volatility correlation, a hallmark of asymmetric volatility dynamics.
Moreover, analysis of the Hurst exponent and multifractal characteristics indicates that the predicted series, like the original synthetic data, exhibits anti-persistent behavior and retains its multifractal structure.

## 1 Introduction

In finance, volatility is a key indicator used to measure the magnitude of fluctuations in the time series of financial assets, and is commonly employed as a risk measure.
For practitioners, predicting future volatility is an essential task for managing the risk of held financial assets and mitigating potential losses.
A common approach to forecasting volatility involves introducing time series models that replicate the statistical properties observed in financial data.
Therefore, constructing appropriate volatility models requires a prior understanding of the empirical characteristics inherent in financial time series.

According to various statistical studies, financial time series exhibit universal properties across different asset classes.
These properties are collectively referred to as ”stylized facts”[Cont2001QF].
One notable stylized fact is volatility clustering, which refers to the tendency for periods of high and low volatility to occur in succession.
A widely used model that captures this property is the generalized autoregressive conditional heteroscedasticity (GARCH) model[Bollerslev1986JOE], which has been extensively applied in empirical research.

A limitation of the GARCH model is its inability to capture volatility asymmetry.
Empirical studies have shown that volatility—particularly in equity markets—tends to increase more following negative returns than positive ones, a phenomenon known as the leverage effect[Black1976].

This effect can also be observed through the return–volatility correlation, where returns are negatively correlated with future volatility[bouchaud2001leverage, roman2008skewness, takaishi2020power]111Empirical studies have reported the presence of an anti-leverage effect in the Chinese market[qiu2006return, shen2009return]..
To accommodate volatility asymmetry, several extensions of the GARCH model have been proposed, including the Exponential GARCH[Nelson1991Econ], Quadratic GARCH[Sentana1995RES], GJR GARCH[Glosten1993JOF], Asymmetric Power GARCH[ding1993long] and Rational GARCH (RGARCH)[takaishi2017rational, takaishi2018volatility] models.

Recently, Gatheral et al.[gatheral2018volatility] found that the Hurst exponent of volatility increment time series is less than 0.5, indicating anti-persistent behavior and a rough volatility path.
Volatility exhibiting these properties is referred to as ”rough volatility.”
Focusing on this feature, they proposed a volatility model based on fractional Brownian motion.
Subsequent empirical studies have confirmed that volatility time series exhibit characteristics of rough volatility[bennedsen2022decoupling, livieri2018rough, takaishi2020rough, floc2022roughness, brandi2022multiscaling, takaishi2025multifractality].

Although numerous volatility models have been proposed, the estimated volatility values vary across models, necessitating careful consideration in model selection.
One approach to circumvent this issue is to use realized volatility (RV)[andersen1998answering, mcaleer2008realized], a model-free measure calculated from high-frequency intraday data.
While RV does not require model specification for its computation, forecasting volatility inevitably involves choosing a model, which reintroduces ambiguity.
Among the models for RV, the heterogeneous autoregressive (HAR) model[corsi2009simple] and realized stochastic volatility (RSV) models[takahashi2009estimating, takaishi2014RSV, takaishi2015GPU, takaishi2015application, takaishi2018bias], realized GARCH model[hansen2012realized] are well known.

In this study, we model volatility time series using quantum circuit learning (QCL)[mitarai2018quantum], a classical–quantum hybrid algorithm capable of approximating nonlinear functions.
In QCL, a parameterized quantum circuit (PQC) is introduced, and its parameters are optimized to minimize a loss function defined by the difference between the teacher data and the PQC outputs.
The advantage of QCL in volatility modeling lies in its flexibility: it does not require any prior assumptions about the properties of volatility.
Instead, QCL automatically generates a nonlinear function that approximates the volatility structure by tuning the PQC parameters.

We employ synthetic financial data generated by the RGARCH model, which produces asymmetric volatility time series.
Using these data, we investigate the feasibility of volatility modeling via QCL, with particular emphasis on capturing volatility asymmetry and multifractal characteristics.

## 2 Quantum Circuit Learning for Volatility Modeling

In the QCL framework,
we aim to learn a volatility function vi=v​(𝒙i,𝜽)v\_{i}=v(\boldsymbol{x}\_{i},\boldsymbol{\theta})
that approximates the target volatility data (i.e., teacher data) σi2\sigma\_{i}^{2}
by tuning the parameter vector 𝜽\boldsymbol{\theta}.
The input data is defined as 𝒙i=(ri,σi2)\boldsymbol{x}\_{i}=(r\_{i},\sigma\_{i}^{2}),
where rir\_{i} denotes the return and σi2\sigma\_{i}^{2} the corresponding volatility.

Figure LABEL:fig:volatility\_circuit illustrates the single-qubit PQC employed in this study.