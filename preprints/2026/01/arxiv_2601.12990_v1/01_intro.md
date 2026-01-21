---
authors:
- Fan Zhang
- Jiabin Luo
- Zheng Zhang
- Shuanghong Huang
- Zhipeng Liu
- Yu Chen
doc_id: arxiv:2601.12990v1
family_id: arxiv:2601.12990
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Beyond Visual Realism: Toward Reliable Financial Time Series Generation'
url_abs: http://arxiv.org/abs/2601.12990v1
url_html: https://arxiv.org/html/2601.12990v1
venue: arXiv q-fin
version: 1
year: 2026
---


###### Abstract

Generative models for financial time series often create data that look realistic and even reproduce stylized facts such as fat tails or volatility clustering. However, these apparent successes break down under trading backtests: models like GANs or WGAN-GP frequently collapse, yielding extreme and unrealistic results that make the synthetic data unusable in practice. We identify the root cause in the neglect of financial asymmetry and rare tail events, which strongly affect market risk but are often overlooked by objectives focusing on distribution matching. To address this, we introduce the Stylized Facts Alignment GAN (SFAG), which converts key stylized facts into differentiable structural constraints and jointly optimizes them with adversarial loss. This multi-constraint design ensures that generated series remain aligned with market dynamics not only in plots but also in backtesting. Experiments on the Shanghai Composite Index (2004–2024) show that while baseline GANs produce unstable and implausible trading outcomes, SFAG generates synthetic data that preserve stylized facts and support robust momentum strategy performance. Our results highlight that structure-preserving objectives are essential to bridge the gap between superficial realism and practical usability in financial generative modeling.

Index Terms— Financial time series, generative adversarial networks, stylized facts, backtesting stability, volatility clustering

## 1 Introduction

Financial markets produce massive amounts of data that are central to risk management, portfolio optimization, and algorithmic trading [[5](https://arxiv.org/html/2601.12990v1#bib.bib1 "Empirical properties of asset returns: stylized facts and statistical issues"), [19](https://arxiv.org/html/2601.12990v1#bib.bib2 "Quant gans: deep generation of financial time series")].
Synthetic financial data are increasingly valuable for stress testing, scenario analysis, and privacy-preserving machine learning.

Yet generating realistic series remains challenging. Unlike images or text, returns exhibit persistent *stylized facts*: heavy tails [[14](https://arxiv.org/html/2601.12990v1#bib.bib3 "The variation of certain speculative prices")], volatility clustering [[8](https://arxiv.org/html/2601.12990v1#bib.bib4 "Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation")], long memory [[7](https://arxiv.org/html/2601.12990v1#bib.bib5 "A long memory property of stock market returns and a new model")], leverage effects [[2](https://arxiv.org/html/2601.12990v1#bib.bib6 "Studies of stock price volatility changes"), [3](https://arxiv.org/html/2601.12990v1#bib.bib7 "Leverage effect in financial markets: the retarded volatility model")], and cross-scale correlations [[4](https://arxiv.org/html/2601.12990v1#bib.bib8 "Multifractality in asset returns: theory and evidence")].

Existing generative models often reproduce marginal distributions but fail to preserve these deeper structures. In particular, they overlook the strong *asymmetry* of financial returns: long bull markets can be erased by a few sharp crashes, and rare tail events dominate risk. Distribution-matching objectives neglect such imbalances, leading to series that appear realistic in plots but collapse under trading evaluation. This gap highlights the need for generative models that move beyond superficial realism and explicitly preserve the structural properties that matter in financial practice.

To address this gap, we propose the Stylized Facts Alignment GAN (SFAG), a novel framework that embeds domain knowledge into the training process. SFAG augments the adversarial objective with *structural consistency losses* designed to explicitly preserve stylized facts: (i) fat-tailed return distributions, (ii) volatility clustering, (iii) leverage effects, and (iv) coarse-to-fine volatility correlations. Unlike prior models, SFAG ensures that generated data remain both statistically consistent with real markets and practically usable in trading strategy evaluation.

We validate SFAG through experiments on the Shanghai Composite Index.
Results show that SFAG outperforms baselines not only in stylized-fact alignment but also in momentum strategy backtests, where competing models exhibit extreme instability.
Our contributions are threefold:
(i) we introduce a structure-preserving generative framework that enforces stylized facts through differentiable loss functions,
(ii) we propose a comprehensive evaluation protocol for structural consistency beyond marginal distributions, including econometric tests and multi-scale volatility analysis, and
(iii) we demonstrate that SFAG bridges the gap between *visual realism* and *financial usability*, producing synthetic data that are both realistic and reliable for backtesting.

## 2 Related Work

Beyond classical econometric models and early GAN-based approaches, several other families of generative models have been explored for financial time series.
Autoregressive neural models such as RNNs and Temporal Convolutional Networks (TCNs) have been applied to capture sequential dependencies [[1](https://arxiv.org/html/2601.12990v1#bib.bib9 "An empirical evaluation of generic convolutional and recurrent networks for sequence modeling")],
though they often suffer from error accumulation and limited long-horizon fidelity.
More recently, Transformer-based architectures have demonstrated strong capabilities in modeling long-range temporal dependencies and scaling to large datasets,
as shown by models like GPT-TST [[11](https://arxiv.org/html/2601.12990v1#bib.bib10 "GPT-tst: generative pre-trained transformer for time series forecasting")], Temporal Fusion Transformer [[12](https://arxiv.org/html/2601.12990v1#bib.bib11 "Temporal fusion transformers for interpretable multi-horizon time series forecasting")], and FEDformer [[20](https://arxiv.org/html/2601.12990v1#bib.bib12 "FEDformer: frequency enhanced decomposed transformer for long-term series forecasting")], and TimeFormer [[13](https://arxiv.org/html/2601.12990v1#bib.bib13 "TimeFormer: transformer with attention modulation empowered by temporal characteristics for time series forecasting")]. However, these methods primarily optimize prediction accuracy and rarely incorporate domain-specific constraints, which limits their ability to reproduce the structural properties required for realistic financial simulation.

In parallel, a growing body of work has explored diffusion and score-based models for time series generation.
TimeGrad [[15](https://arxiv.org/html/2601.12990v1#bib.bib14 "Autoregressive denoising diffusion models for multivariate probabilistic time series forecasting")] and score-based SDEs [[18](https://arxiv.org/html/2601.12990v1#bib.bib15 "Score-based generative modeling through stochastic differential equations")] offer training stability and high coverage of data distributions,
yet they remain computationally expensive and lack mechanisms to enforce stylized facts or risk-sensitive behavior.
Recent studies have also begun to consider structure-aware or risk-aware objectives,
for example by constraining tail risk, volatility-of-volatility, or regime persistence during training.
These approaches highlight a shift from purely distribution-matching criteria toward incorporating financial domain knowledge.

Furthermore, related research outside the financial domain has shown that domain-constrained generative models [[9](https://arxiv.org/html/2601.12990v1#bib.bib16 "Deep generative modeling for financial time series with application in var: a comparative review")]
can substantially improve realism in other complex time series tasks such as climate modeling, traffic forecasting, and energy systems simulation.
These successes suggest that embedding domain priors and structural invariants can be a general principle for improving the reliability of generative models on non-stationary and high-volatility data, an insight that motivates our proposed SFAG.

Unlike prior work that only validates stylized facts in post-hoc analysis [[16](https://arxiv.org/html/2601.12990v1#bib.bib17 "Generative adversarial networks applied to synthetic financial scenarios generation")], our contribution is to embed them directly into the training objective [[6](https://arxiv.org/html/2601.12990v1#bib.bib18 "Quantum generative modeling for financial time series with temporal correlations")]. The proposed SFAG augments adversarial learning with domain-informed constraints that enforce fat tails, volatility clustering, leverage effects, and cross-scale volatility correlations. This approach transforms stylized facts from diagnostic tools into differentiable objectives, ensuring that generated data remain not only statistically consistent with real markets but also practically reliable in backtesting.

## 3 Method

We introduce the Stylized Facts Alignment GAN (SFAG), a structure-preserving framework for financial time series generation.
Rather than optimizing for visual or marginal distributional similarity, SFAG explicitly enforces alignment with financial stylized facts through a multi-constraint objective.

Architecture overview.
SFAG builds upon a standard adversarial architecture with generator GθG\_{\theta} and discriminator DϕD\_{\phi}, and augments it with a domain-informed alignment module.
Latent noise z∼𝒩​(0,I)z\sim\mathcal{N}(0,I) is mapped to a synthetic return series 𝐫^=Gθ​(z)\hat{\mathbf{r}}=G\_{\theta}(z), while DϕD\_{\phi} distinguishes 𝐫^\hat{\mathbf{r}} from real returns 𝐫\mathbf{r}.
We adopt a WGAN-GP [[10](https://arxiv.org/html/2601.12990v1#bib.bib20 "Improved training of wasserstein gans")] loss for training stability:

|  |  |  |
| --- | --- | --- |
|  | ℒadv=𝔼​[Dϕ​(𝐫^)]−𝔼​[Dϕ​(𝐫)]+λgp​ℒgp.\mathcal{L}\_{\text{adv}}=\mathbb{E}[D\_{\phi}(\hat{\mathbf{r}})]-\mathbb{E}[D\_{\phi}(\mathbf{r})]+\lambda\_{\text{gp}}\,\mathcal{L}\_{\text{gp}}. |  |

Stylized-fact alignment losses.
Financial realism cannot be captured by marginal distribution matching alone.
SFAG encodes domain knowledge into four differentiable constraints that together capture heavy tails, volatility memory, return–volatility asymmetry, and cross-scale dependencies.
Fat tails. We estimate the generalized Pareto tail index ξ\xi on positive and negative return tails and minimize their gap:

|  |  |  |
| --- | --- | --- |
|  | ℒGPD=|ξ​(𝐫)−ξ​(𝐫^)|.\mathcal{L}\_{\text{GPD}}=\left|\xi(\mathbf{r})-\xi(\hat{\mathbf{r}})\right|. |  |

Volatility clustering. We compute the autocorrelation function (ACF) of squared returns up to lag KK and align them via mean squared error:

|  |  |  |
| --- | --- | --- |
|  | ℒACF=1K​∑k=1K(ρk​(𝐫2)−ρk​(𝐫^2))2.\mathcal{L}\_{\text{ACF}}=\frac{1}{K}\sum\_{k=1}^{K}\big(\rho\_{k}(\mathbf{r}^{2})-\rho\_{k}(\hat{\mathbf{r}}^{2})\big)^{2}. |  |

Leverage effect. We measure the correlation between past returns and future realized volatility, enforcing negative dependence:

|  |  |  |
| --- | --- | --- |
|  | ℒLev=|ρ​(𝐫t,σt+1)−ρ​(𝐫^t,σ^t+1)|.\mathcal{L}\_{\text{Lev}}=\big|\rho(\mathbf{r}\_{t},\sigma\_{t+1})-\rho(\hat{\mathbf{r}}\_{t},\hat{\sigma}\_{t+1})\big|. |  |

Coarse-to-fine volatility correlation. We construct cross-scale realized volatility vectors using rolling windows {w1,…,wM}\{w\_{1},\dots,w\_{M}\}, and minimize the Frobenius norm between their correlation matrices:

|  |  |  |
| --- | --- | --- |
|  | ℒCFVC=‖Corr​(Σ​(𝐫))−Corr​(Σ​(𝐫^))‖F.\mathcal{L}\_{\text{CFVC}}=\left\|\mathrm{Corr}(\Sigma(\mathbf{r}))-\mathrm{Corr}(\Sigma(\hat{\mathbf{r}}))\right\|\_{F}. |  |

Multi-constraint optimization.
Unlike prior work that *validates* stylized facts post-hoc, SFAG *optimizes them jointly* during training.
The generator minimizes:

|  |  |  |
| --- | --- | --- |
|  | ℒSFAG=ℒadv+λ1​ℒGPD+λ2​ℒACF+λ3​ℒLev+λ4​ℒCFVC.\mathcal{L}\_{\text{SFAG}}=\mathcal{L}\_{\text{adv}}+\lambda\_{1}\mathcal{L}\_{\text{GPD}}+\lambda\_{2}\mathcal{L}\_{\text{ACF}}+\lambda\_{3}\mathcal{L}\_{\text{Lev}}+\lambda\_{4}\mathcal{L}\_{\text{CFVC}}. |  |

This formulation treats stylized facts as *structural invariants*, turning them into first-class optimization objectives.
Importantly, the alignment module is model-agnostic: while demonstrated with a GAN backbone, it can be applied to diffusion or transformer-based generators without modification.

Training procedure.
We train SFAG for 50,000 generator iterations using the Adam optimizer
(with β1=0.5\beta\_{1}=0.5 and β2=0.9\beta\_{2}=0.9) and a learning rate of 2×10−42\times 10^{-4}.
We set the gradient penalty weight to λgp=10\lambda\_{\text{gp}}=10,
and update the discriminator five times for every generator step following the WGAN-GP setting.
Stylized-fact losses are gradually annealed during the first 20% of training to stabilize early dynamics,
and training continues until convergence on stylized-fact gap metrics.

## 4 Experiments

Setup.
We use daily Shanghai Composite Index (SSE) returns from 2004–2024 (∼\sim5000 observations).
Each sample has a sequence length of 2520, latent dimension of 100, and batch size of 24.
Models are trained for 50,000 generator iterations using the Adam optimizer (β1=0.5,β2=0.9\beta\_{1}{=}0.5,\beta\_{2}{=}0.9) with a learning rate of 2×10−42\times 10^{-4}, and gradient penalty weight λgp=10\lambda\_{\text{gp}}=10. The discriminator is updated 5 times per generator step following the WGAN-GP setting.

All experiments are implemented in PyTorch and run on a single NVIDIA A100 GPU with 80GB memory.

### 4.1 Stylized Facts Preservation

We first provide a visual comparison of six well-documented stylized facts between real data and synthetic series.
These stylized facts include: (i) unpredictability (low linear autocorrelation), (ii) volatility clustering, (iii) heavy tails, (iv) leverage effects,
(v) cross-scale volatility correlation, and (vi) gain/loss asymmetry.
Figure [1](https://arxiv.org/html/2601.12990v1#S4.F1 "Figure 1 ‣ 4.1 Stylized Facts Preservation ‣ 4 Experiments ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation") illustrates that SFAG-generated data exhibit close qualitative similarity to real market data,
suggesting that our model captures the essential structural properties observed in financial time series.

![Refer to caption](stylized_facts_20250625_010747.png)

(a) Real Data Stylized Facts.

![Refer to caption](gen_stylized_facts_20250625_180415.png)

(b) SFAG Generated Data Stylized Facts.

Fig. 1: Visual comparison of six stylized facts between real and generated data. SFAG successfully preserves key properties such as unpredictability, volatility clustering, fat tails, leverage effects, coarse-fine correlations, and gain/loss asymmetry.

Observation.
Visual inspection indicates that SFAG captures the six fundamental stylized facts of financial markets with high fidelity.
However, purely qualitative checks can be misleading: baseline GANs often appear visually consistent while failing to preserve structural statistics in a quantitative sense.
We therefore proceed to a gap-based analysis to rigorously assess stylized-fact alignment.

### 4.2 Stylized-Fact Alignment

While visual inspection suggests that SFAG captures essential market characteristics,
a rigorous evaluation requires quantitative analysis of structural properties.
Unlike generic distributional distances [[17](https://arxiv.org/html/2601.12990v1#bib.bib21 "Wasserstein distance guided representation learning for domain adaptation")] (e.g., MMD or Wasserstein) that only compare marginal shapes,
stylized facts probe the temporal dynamics and risk structure of financial markets, which are crucial for practical usability.
We therefore evaluate four canonical stylized facts on both real and synthetic data.

(i) Heavy tails.
We estimate the tail index ξ\xi of the Generalized Pareto Distribution (GPD) on returns exceeding the 95th percentile threshold, using the Peak-Over-Threshold method.
A smaller gap in ξ\xi indicates that the generated data reproduce the same frequency and magnitude of rare extreme events as real markets, a critical property for risk modeling and stress testing.

(ii) Volatility clustering.
We compute the autocorrelation function (ACF) of absolute returns ρk​(|rt|)\rho\_{k}(|r\_{t}|) for lags k=1k=1 to 2020.
This measures the persistence of volatility shocks: real markets exhibit slowly decaying correlations, while models that fail to capture clustering show near-zero or oscillatory patterns.
Preserving this long memory is essential for modeling risk horizons.

(iii) Leverage effect.
We calculate the contemporaneous correlation between past returns rtr\_{t} and future realized volatility σt+1\sigma\_{t+1} (standard deviation of returns over the next 20 days).
Real markets typically show negative correlations, reflecting the risk-aversion response where price drops trigger higher volatility.
Failure to reproduce this asymmetry leads to unrealistic risk dynamics in downstream tasks.

(iv) Cross-scale volatility correlations (CFVC).
We construct realized volatility vectors using rolling windows of 5, 20, 60, and 120 days, and compute their pairwise correlation matrices.
We then report the Frobenius norm gap between the real and synthetic matrices, which reflects whether the model reproduces the hierarchical structure of market fluctuations across different time scales.

We train each model five times with different random seeds and report the average absolute gap to real data on each statistic.
Lower values indicate stronger alignment with real market structure and better preservation of stylized facts.

Table 1: Stylized-fact gaps (absolute differences). Lower values indicate better preservation.

| Model | GPD Tail | ACF | Leverage | CFVC |
| --- | --- | --- | --- | --- |
| Standard GAN | 0.2615 | 0.1431 | 32.4617 | 0.0863 |
| WGAN-GP | 0.0776 | 0.1053 | 33.7440 | 0.1021 |
| SFAG (ours) | 0.0146 | 0.0982 | 32.7516 | 0.0436 |

Findings.
As shown in Table [1](https://arxiv.org/html/2601.12990v1#S4.T1 "Table 1 ‣ 4.2 Stylized-Fact Alignment ‣ 4 Experiments ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation"), SFAG achieves the smallest gaps on GPD Tail and CFVC, reducing errors by over 80% and 50% respectively compared with WGAN-GP.
This indicates that SFAG can closely reproduce the heavy-tailed nature of market returns and the hierarchical dependence structure of volatility across time scales, both of which are essential for realistic risk modeling.
By contrast, Standard GAN exhibits a large tail index gap (0.2615), suggesting that it underestimates the probability of extreme events, while both baselines fail to capture multi-scale volatility interactions, reflected by their higher CFVC errors.

SFAG also yields competitive results on ACF and Leverage, consistently outperforming Standard GAN.
Although the leverage gap remains large across all models (around 32–33), SFAG slightly narrows it while maintaining a lower ACF gap, indicating that it preserves volatility persistence without amplifying noise.
These results suggest that conventional GANs, which optimize only for distributional similarity, tend to produce visually plausible but structurally fragile series, whereas SFAG’s structure-preserving objectives enable it to recover deeper temporal dependencies and asymmetries.

Overall, Table [1](https://arxiv.org/html/2601.12990v1#S4.T1 "Table 1 ‣ 4.2 Stylized-Fact Alignment ‣ 4 Experiments ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation") demonstrates that explicitly embedding stylized-fact consistency into the training objective leads to synthetic series that not only resemble real data in appearance, but also replicate the underlying statistical regularities that govern real financial markets.

### 4.3 Strategy Backtesting

We further evaluate practical usability by backtesting a simple momentum strategy on synthetic price series generated by each model.
The strategy goes long if the past 60-day return is positive and short otherwise, rebalanced daily, with transaction cost 5 bps and no leverage.
We retrain all models and generate 10 synthetic paths for each, then evaluate the strategy on both real and synthetic SSE returns (2004–2024).
Table [2](https://arxiv.org/html/2601.12990v1#S4.T2 "Table 2 ‣ 4.3 Strategy Backtesting ‣ 4 Experiments ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation") reports the average results across 10 synthetic runs.

Table 2: Momentum strategy performance. SFAG tracks real-data behavior, while Standard GAN and WGAN-GP collapse into unrealistic regimes.

| Metric | Real Data | Standard GAN | WGAN-GP | SFAG (Ours) |
| --- | --- | --- | --- | --- |
| Annualized Return | 33.10% | 2467.24% | 2152.07% | 27.80% |
| Annualized Volatility | 15.20% | 991.83% | 995.06% | 9.37% |
| Sharpe Ratio | 2.18 | 2.49 | 2.16 | 2.97 |
| Maximum Drawdown | 9.50% | 109.87% | 148.11% | 4.37% |
| VaR (95%) | -1.10% | -78.03% | -85.79% | -0.91% |
| CVaR (95%) | -2.23% | -141.79% | -144.62% | -0.92% |

Key Findings.
The backtesting results highlight a stark contrast between SFAG and conventional GAN-based models.
Standard GAN and WGAN-GP frequently collapse during strategy evaluation, producing extreme and implausible outcomes such as annualized returns exceeding 2000% and volatility approaching 1000%.
In sharp contrast, SFAG consistently generates synthetic series that yield realistic and stable performance: the momentum strategy achieves an annualized return of 27.8% and volatility of 9.37%, closely aligned with the real data benchmark.
Moreover, SFAG attains a Sharpe ratio of 2.97, surpassing the real market level (2.18), indicating that its higher risk-adjusted performance stems from enhanced robustness rather than spurious instability.
These findings demonstrate that merely producing visually plausible return patterns is insufficient. Only by enforcing structure-preserving constraints can generative models achieve financial realism and backtest validity.

## 5 Conclusion

We introduced the Stylized Facts Alignment GAN (SFAG), a structure-preserving framework that elevates stylized facts from post-hoc diagnostics to differentiable training objectives. By jointly optimizing adversarial realism and structural alignment, SFAG generates financial time series that not only reproduce statistical regularities but also remain robust in trading backtests. On the Shanghai Composite Index (2004–2024), SFAG consistently outperforms GAN and WGAN-GP, showing that explicit structure-preserving objectives are critical to bridge the gap between apparent realism and financial usability.

More broadly, this work suggests a new perspective: realism in finance should not be defined only by distributional similarity or visual plausibility, but by whether synthetic data behave plausibly under trading evaluation. Prior studies largely overlooked this criterion, leading to unstable outcomes. By embedding domain knowledge directly into training, SFAG highlights a principled path toward synthetic data that are both scientifically faithful and practically useful.

Future work.
This work opens several directions: (i) extending evaluation beyond a single equity index to multi-asset and cross-market settings, including FX, rates, and commodities, (ii) incorporating richer stylized facts such as tail asymmetry, volatility-of-volatility, and regime persistence, and (iii) exploring backbone-agnostic alignment, applying SFAG principles to diffusion and transformer-based generators for scalable and flexible financial simulation.

## References

* [1]
  S. Bai, J. Z. Kolter, and V. Koltun (2018)
  An empirical evaluation of generic convolutional and recurrent networks for sequence modeling.
  In Proceedings of the 35th International Conference on Machine Learning (ICML),
   pp. 481–490.
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p1.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [2]
  F. Black (1976)
  Studies of stock price volatility changes.
  In Proceedings of the 1976 Meeting of the Business and Economic Statistics Section,
   pp. 177–181.
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p2.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [3]
  J. Bouchaud, A. Matacz, and M. Potters (2001)
  Leverage effect in financial markets: the retarded volatility model.
  Physical review letters 87 (22),  pp. 228701.
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p2.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [4]
  L. Calvet and A. Fisher (2002)
  Multifractality in asset returns: theory and evidence.
  Review of Economics and Statistics 84 (3),  pp. 381–406.
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p2.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [5]
  R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative finance 1 (2),  pp. 223.
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p1.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [6]
  D. Dechant, E. J. E. Schwander, L. Van Drooge, C. Moussa, D. Garlaschelli, V. Dunjko, and J. Tura Brugués (2026)
  Quantum generative modeling for financial time series with temporal correlations.
  Machine Learning: Science and Technology.
  External Links: [Link](http://iopscience.iop.org/article/10.1088/2632-2153/ae39a2)
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p4.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [7]
  Z. Ding, C. W. Granger, and R. F. Engle (1993)
  A long memory property of stock market returns and a new model.
  Journal of empirical finance 1 (1),  pp. 83–106.
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p2.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [8]
  R. F. Engle (1982)
  Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation.
  Econometrica 50 (4),  pp. 987–1007.
  External Links: ISSN 00129682, 14680262,
  [Link](http://www.jstor.org/stable/1912773)
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p2.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [9]
  L. Ericson, X. Zhu, X. Han, R. Fu, S. Li, S. Guo, and P. Hu (2024)
  Deep generative modeling for financial time series with application in var: a comparative review.
  arXiv preprint arXiv:2401.10370.
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p3.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [10]
  I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. Courville (2017)
  Improved training of wasserstein gans.
  In Proceedings of the 31st International Conference on Neural Information Processing Systems (NIPS),
   pp. 5769–5779.
  Cited by: [§3](https://arxiv.org/html/2601.12990v1#S3.p2.7 "3 Method ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [11]
  Y. Li, H. Bai, X. Song, Y. Cheng, and X. Zhang (2023)
  GPT-tst: generative pre-trained transformer for time series forecasting.
  Expert Systems with Applications 230,  pp. 120675.
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p1.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [12]
  B. Lim, S. O. Arik, N. Loeff, and T. Pfister (2021)
  Temporal fusion transformers for interpretable multi-horizon time series forecasting.
  In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD),
   pp. 2967–2975.
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p1.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [13]
  Z. Liu, P. Duan, X. Tang, B. Li, Y. Huang, M. Geng, C. Zhang, B. Zhang, and B. Wang (2025)
  TimeFormer: transformer with attention modulation empowered by temporal characteristics for time series forecasting.
  Expert Systems with Applications,  pp. 131040.
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p1.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [14]
  B. Mandelbrot (1963)
  The variation of certain speculative prices.
  The Journal of Business 36 (4),  pp. 394–419.
  External Links: ISSN 00219398, 15375374,
  [Link](http://www.jstor.org/stable/2350970)
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p2.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [15]
  K. Rasul, C. Seward, I. Schuster, and R. Vollgraf (2021)
  Autoregressive denoising diffusion models for multivariate probabilistic time series forecasting.
  In Proceedings of the 38th International Conference on Machine Learning (ICML),
   pp. 8857–8868.
  External Links: [Link](https://api.semanticscholar.org/CorpusID:231719657)
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p2.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [16]
  M. Rizzato, J. Wallart, C. Geissler, N. Morizet, and N. Boumlaik (2023)
  Generative adversarial networks applied to synthetic financial scenarios generation.
  Physica A: Statistical Mechanics and its Applications 623,  pp. 128899.
  External Links: ISSN 0378-4371,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.physa.2023.128899),
  [Link](https://www.sciencedirect.com/science/article/pii/S0378437123004545)
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p4.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [17]
  J. Shen, Y. Qu, W. Zhang, and Y. Yu (2018)
  Wasserstein distance guided representation learning for domain adaptation.
  In Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence,
   pp. 4058–4065.
  External Links: ISBN 978-1-57735-800-8
  Cited by: [§4.2](https://arxiv.org/html/2601.12990v1#S4.SS2.p1.1 "4.2 Stylized-Fact Alignment ‣ 4 Experiments ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [18]
  Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole (2021)
  Score-based generative modeling through stochastic differential equations.
  In 9th International Conference on Learning Representations (ICLR),
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p2.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [19]
  M. Wiese, R. Knobloch, R. Korn, and P. Kretschmer (2020)
  Quant gans: deep generation of financial time series.
  Quantitative Finance 20 (9),  pp. 1419–1440.
  Cited by: [§1](https://arxiv.org/html/2601.12990v1#S1.p1.1 "1 Introduction ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").
* [20]
  H. Zhou, S. Zhang, J. Peng, S. Zhang, J. Li, H. Xiong, and W. Zhang (2022)
  FEDformer: frequency enhanced decomposed transformer for long-term series forecasting.
  Proceedings of the 39th International Conference on Machine Learning (ICML),  pp. 27268–27286.
  Cited by: [§2](https://arxiv.org/html/2601.12990v1#S2.p1.1 "2 Related Work ‣ Beyond Visual Realism: Toward Reliable Financial Time Series Generation").