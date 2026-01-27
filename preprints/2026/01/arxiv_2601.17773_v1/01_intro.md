---
authors:
- Jeonggyu Huh
- Seungwon Jeong
- Hyun-Gyoon Kim
- Hyeng Keun Koo
- Byung Hwa Lim
doc_id: arxiv:2601.17773v1
family_id: arxiv:2601.17773
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'MarketGANs: Multivariate financial time-series data augmentation using generative
  adversarial networks'
url_abs: http://arxiv.org/abs/2601.17773v1
url_html: https://arxiv.org/html/2601.17773v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jeonggyu Huh
Department of Mathematics, Sungkyunkwan University, Republic of Korea.

Seungwon Jeong
Global-Learning & Academic research institution for Master’s ⋅\cdot PhD students, and Postdocs, Chonnam National University, Republic of Korea.

Hyun-Gyoon Kim111Corresponding author, E-mail address: hyungoonkim@ajou.ac.kr, limbh@skku.edu
Department of Financial Engineering, Ajou University, Republic of Korea.

Hyeng Keun Koo
Department of Financial Engineering, Ajou University, Republic of Korea.

Byung Hwa Lim∗
Department of FinTech, SKK Business School, Sungkyunkwan University, Republic of Korea.

###### Abstract

This paper introduces MarketGAN, a factor-based generative framework for high-dimensional asset return generation under severe data scarcity. We embed an explicit asset-pricing factor structure as an economic inductive bias and generate returns as a single joint vector, thereby preserving cross-sectional dependence and tail co-movement alongside inter-temporal dynamics. MarketGAN employs generative adversarial learning with a temporal convolutional network (TCN) backbone, which models stochastic, time-varying factor loadings and volatilities and captures long-range temporal dependence. Using daily returns of large U.S. equities, we find that MarketGAN more closely matches empirical stylized facts of asset returns, including heavy-tailed marginal distributions, volatility clustering, leverage effects, and, most notably, high-dimensional cross-sectional correlation structures and tail co-movement across assets, than conventional factor-model-based bootstrap approaches. In portfolio applications, covariance estimates derived from MarketGAN-generated samples outperform those derived from other methods when factor information is at least weakly informative, demonstrating tangible economic value.

Keywords: Multivariate time-series, Data augmentation, Factor models, Generative adversarial networks

## 1 Introduction

Modern empirical finance increasingly confronts a fundamental tension between high dimensionality and limited data availability. Asset pricing, portfolio choice, and risk management problems routinely involve dozens or hundreds of assets, yet the effective length of available financial time series remains short relative to the dimensionality of the objects of interest. Even classical mean–variance portfolio optimization requires estimating a large number of parameters. For example, the mean vector and covariance matrix of 100 assets alone entail more than 5,000 parameters, and extensions incorporating higher-order co-moments quickly become infeasible, as described in Martellini and Ziemann ([2010](https://arxiv.org/html/2601.17773v1#bib.bib46 "Improved estimates of higher-order comoments and implications for portfolio selection")).222If one considers higher-order co-moments to improve upon traditional methodologies Martellini and Ziemann ([2010](https://arxiv.org/html/2601.17773v1#bib.bib46 "Improved estimates of higher-order comoments and implications for portfolio selection")), the number of required parameters rapidly becomes infeasible.
Specifically, incorporating third-order co-moments requires estimating over 170,000 parameters, and including fourth-order moments increases this number to more than 4 million.
Given that 20 years of daily data yield roughly 5,000 observations, and even fewer observations are available from less-noisy monthly data, these estimation problems are highly underdetermined.
Furthermore, even if one collects sufficient historical data over the past several decades, structural shifts in macroeconomic conditions and changes in individual firm-specific characteristics can significantly alter asset correlations over time, which makes the historical sample covariance matrix unreliable. With only a few thousand daily observations over several decades—and even fewer reliable observations at lower frequencies—such estimation problems are inherently underdetermined. Moreover, structural changes in macroeconomic conditions and firm characteristics further undermine the reliability of purely historical estimates of dependence.

These challenges are amplified in the context of financial machine learning. Deep learning and reinforcement learning methods offer flexible nonlinear representations but are inherently data intensive (Goodfellow et al., [2016](https://arxiv.org/html/2601.17773v1#bib.bib51 "Deep learning")). When trained on finite historical samples, such models are prone to overfitting and poor out-of-sample generalization. This issue has been formally documented in the context of deep empirical risk minimization and deep stochastic optimization, where neural-network-based models trained on fixed datasets exhibit strong in-sample performance but deteriorate sharply out of sample unless additional simulated or synthetic data are supplied (Reppen and Soner, [2023](https://arxiv.org/html/2601.17773v1#bib.bib64 "Deep empirical risk minimization in finance: looking into the future"); Reppen et al., [2023](https://arxiv.org/html/2601.17773v1#bib.bib63 "Deep stochastic optimization in finance")). These findings suggest that, in high-dimensional financial settings, synthetic data play a structural role in enabling reliable learning and decision-making.

Motivated by this observation, a growing literature employs generative models, particularly generative adversarial networks (GANs), to augment financial datasets and improve model performance. Early studies show that GAN-generated data can replicate stylized features of asset returns and enhance forecasting or trading performance, primarily in single-asset or low-dimensional settings (Takahashi et al., [2019](https://arxiv.org/html/2601.17773v1#bib.bib18 "Modeling financial time-series with generative adversarial networks"); Wiese et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib1 "Quant GANs: deep generation of financial time series"); Buehler et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib24 "A data-driven market simulator for small data environments")). However, most existing approaches treat synthetic data as local augmentation aimed at reproducing marginal distributions, and rarely address joint return distributions, cross-sectional dependence, or portfolio-relevant risk structures. As a result, their evaluation is often confined to predictive accuracy rather than economically meaningful distributional properties.

Recent work emphasizes that the usefulness of synthetic data depends critically on whether it extends learning beyond historical realizations. Viewing financial markets as complex adaptive systems, Wei et al. ([2025](https://arxiv.org/html/2601.17773v1#bib.bib61 "Enhancing return forecasting using lstm with agent-based synthetic data")) and Horvath et al. ([2026](https://arxiv.org/html/2601.17773v1#bib.bib68 "Market generators: a paradigm shift in financial modeling")) argue that merely replicating past distributions is insufficient to prepare models for regime shifts and rare but economically consequential events. At the same time, a growing literature on missing data and sparsity in high-dimensional asset pricing panels shows that even sophisticated regularization and imputation methods struggle to recover economically relevant dependence structures—particularly low-variance directions and cross-sectional correlations central to portfolio choice (Bryzgalova et al., [2025a](https://arxiv.org/html/2601.17773v1#bib.bib58 "Missing financial data"), [b](https://arxiv.org/html/2601.17773v1#bib.bib57 "Forest through the trees: building cross-sections of stock returns"); Freyberger et al., [2025](https://arxiv.org/html/2601.17773v1#bib.bib59 "Missing data in asset pricing panels"); Chen and McCoy, [2024](https://arxiv.org/html/2601.17773v1#bib.bib60 "Missing values handling for machine learning portfolios")). These findings point to a deeper limitation that the joint distribution of asset returns is only weakly identified from historical observations alone in high dimensions.

This paper addresses this gap by proposing MarketGAN, a factor-based generative framework for high-dimensional asset return generation. The central objective of MarketGAN is not to improve point prediction accuracy, but to learn and generate the joint distribution of asset returns in a manner that preserves economically meaningful dependence structures. The approach embeds a traditional asset-pricing factor model, such as the CAPM and Fama–French factor models, as an economic inductive bias, while using generative learning to model stochastic, time-varying factor loadings and idiosyncratic risks. By generating returns as a single joint vector, MarketGAN directly targets cross-sectional dependence across assets, which underpins diversification and portfolio risk.

While we illustrate our framework using financial portfolios, the problem we address is more general. Many decision-making environments are characterized by high-dimensional uncertainty and severe data scarcity, in which historical observations are insufficient to reliably estimate the joint distribution of relevant variables. Examples include demand forecasting across large product assortments in supply chains, risk aggregation in energy and insurance systems, and scenario generation for stress testing and capacity planning. In such settings, decisions are typically nonlinear functions of the underlying uncertainty, and small errors in dependence modeling can be amplified through optimization and control. Consequently, the central challenge is not point prediction, but learning and extending a joint distribution that is suitable as an input to downstream decision problems. From this perspective, financial portfolios serve as a canonical and transparent test-bed rather than a special case. Portfolio optimization provides a well-understood nonlinear decision mapping in which dependence structures, such as cross-sectional correlation and tail co-movement, play a decisive role. The proposed framework is therefore best viewed as a data-driven approach to decision-making under weak identification, where economic or structural constraints are used to regularize distributional learning and to generate synthetic scenarios that improve decision quality. This interpretation highlights the relevance of our approach beyond finance, positioning MarketGAN as a general framework for high-dimensional decision problems under data scarcity.

When generating synthetic multivariate asset return data, two aspects are of central importance. The first is the cross-sectional dependence across assets, and the other is inter-temporal dependence over time. To address inter-temporal dependence, we employ temporal convolutional networks (TCNs), which capture long-range causal dependence through stacked dilated convolutions (Bai et al., [2018](https://arxiv.org/html/2601.17773v1#bib.bib5 "An empirical evaluation of generic convolutional and recurrent networks for sequence modeling")). Importantly, in our framework TCNs are used not to generate returns directly, but to model the time-varying evolution of factor model coefficients, thereby linking temporal dynamics to risk exposures.333To address inter-temporal dependence, we incorporate temporal architectures explicitly designed to model sequential dynamics, including recurrent neural networks (Elman, [1990](https://arxiv.org/html/2601.17773v1#bib.bib55 "Finding structure in time")), self-attention-based transformers (Vaswani et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib54 "Attention is all you need")), and temporal convolutional networks (TCNs) (Bai et al., [2018](https://arxiv.org/html/2601.17773v1#bib.bib5 "An empirical evaluation of generic convolutional and recurrent networks for sequence modeling")). In this study, we employ TCNs due to their structural advantages in modeling long-range causal dependence with efficient parallel computation. TCNs have been successfully applied to sequential data such as audio generation (Oord et al., [2016](https://arxiv.org/html/2601.17773v1#bib.bib4 "Wavenet: A generative model for raw audio")) and financial time series modeling (Wiese et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib1 "Quant GANs: deep generation of financial time series")).  The factor structure organizes cross-sectional dependence, while stochastic, time-varying coefficients allow dependence patterns to evolve with market conditions. We implement this framework using adversarial distribution learning as a flexible engine for approximating complex high-dimensional distributions.444Applying generative neural networks to financial data raises a fundamental challenge of data scarcity. Generative models themselves are data intensive, and learning high-dimensional joint distributions without additional structure can lead to underfitting or overfitting when historical samples are limited. To break this circular dilemma, MarketGAN incorporates domain knowledge in the form of asset-pricing factor models. The factor structure provides the overall organization of cross-sectional dependence across assets, while its coefficients which are intercepts, factor loadings, and idiosyncratic volatilities are modeled as stochastic, time-varying objects generated by a generative network. This design can be interpreted as a time-varying coefficient factor model similar to Fabozzi and Francis ([1978](https://arxiv.org/html/2601.17773v1#bib.bib44 "Beta as a random coefficient")), Chamberlain ([1982](https://arxiv.org/html/2601.17773v1#bib.bib37 "Multivariate regression models for panel data")) and Ang and Chen ([2007](https://arxiv.org/html/2601.17773v1#bib.bib33 "CAPM over the long run: 1926–2001")), in which factor exposures evolve dynamically rather than remaining fixed or deterministically specified. To ensure stable training, we adopt the Wasserstein GAN with gradient penalty (Arjovsky et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib11 "Wasserstein generative adversarial networks"); Gulrajani et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib12 "Improved training of wasserstein gans")). Importantly, adversarial learning plays an instrumental role in providing distributional flexibility, while the factor structure supplies economic discipline.

We empirically evaluate MarketGAN using daily excess returns of 98 large U.S. equities from the S&P 100 universe. Across one-, three-, and five-factor specifications, MarketGAN generates synthetic returns that (i) closely match empirical marginal distributions and higher-order moments, (ii) reproduce canonical intertemporal stylized facts such as volatility clustering and leverage effects, and—most importantly—(iii) substantially improve the fidelity of cross-sectional dependence, including dependence in extreme returns, relative to transparent factor-model-based bootstrap benchmarks. Quantitative distributional metrics commonly used in the generative modeling (Heusel et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib40 "Gans trained by a two time-scale update rule converge to a local nash equilibrium"); Bonneel et al., [2015](https://arxiv.org/html/2601.17773v1#bib.bib21 "Sliced and radon wasserstein barycenters of measures")) confirm these gains.

We further assess economic value through mean–variance portfolio optimization using MarketGAN-generated synthetic data. The results show that when future factor information is even weakly informative, MarketGAN achieves superior portfolio performance relative to factor-model-based bootstrap methods, while remaining competitive with strong covariance-based benchmarks. These gains do not arise from improved factor forecasting or marginal distributional accuracy alone, but from MarketGAN’s ability to generate coherent high-dimensional return distributions that preserve economically meaningful dependence structures. In sum, by embedding factor-model discipline into a generative architecture and by demonstrating gains in both statistical fidelity and downstream portfolio performance, MarketGAN provides a practical framework for decision-making in high-dimensional financial settings where historical data alone are insufficient.

Related Literature

This paper is related to the growing literature that applies machine learning and deep learning methods to asset pricing and return modeling.
Gu et al. ([2020](https://arxiv.org/html/2601.17773v1#bib.bib29 "Empirical asset pricing via machine learning")) provide a comprehensive evaluation of a wide range of machine learning models using firm characteristics and macroeconomic variables, showing that flexible nonlinear methods can outperform traditional linear regressions in predicting equity risk premia and in portfolio applications.
Building on this insight, Gu et al. ([2021](https://arxiv.org/html/2601.17773v1#bib.bib52 "Autoencoder asset pricing models")) integrate deep learning with factor models by allowing factor exposures to depend nonlinearly on conditioning information. Their approach shares with ours a structural motivation grounded in factor models. While these approaches enhance predictive performance and factor representation, factor loadings are treated as deterministic functions of conditioning information, and the focus remains on prediction or estimation rather than on generating joint return distributions for data augmentation. Related work also applies adversarial learning to asset pricing problems. Chen et al. ([2024](https://arxiv.org/html/2601.17773v1#bib.bib66 "Deep learning in asset pricing")) propose an adversarially trained stochastic discount factor estimator combining macroeconomic state variables with a GAN-style objective. In contrast, our focus is not on SDF estimation but on learning and generating joint return distributions relevant for high-dimensional decision problems.

A second strand of the literature studies generative neural networks for financial time-series data, with GAN-based models playing a central role. Early contributions focus primarily on univariate or low-dimensional settings and demonstrate that generative models can reproduce canonical stylized facts such as heavy tails and volatility clustering (Takahashi et al., [2019](https://arxiv.org/html/2601.17773v1#bib.bib18 "Modeling financial time-series with generative adversarial networks"); Wiese et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib1 "Quant GANs: deep generation of financial time series")). Subsequent work extends these approaches to multivariate settings (Yoon et al., [2019](https://arxiv.org/html/2601.17773v1#bib.bib19 "Time-series generative adversarial networks"); Liao et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib25 "Conditional sig-wasserstein gans for time series generation"); Rizzato et al., [2023](https://arxiv.org/html/2601.17773v1#bib.bib22 "Generative adversarial networks applied to synthetic financial scenarios generation"); Cont et al., [2022](https://arxiv.org/html/2601.17773v1#bib.bib27 "Tail-gan: Learning to simulate tail risk scenarios")), but empirical validation is typically confined to small cross sections or to marginal distributions. As a result, these models often fall short of capturing the high-dimensional joint return distributions and cross-sectional dependence structures that are central to portfolio risk management.

More recent approaches begin to address higher-dimensional generation by incorporating structural or economic inductive biases (Wang and Chen, [2024](https://arxiv.org/html/2601.17773v1#bib.bib30 "Factor-gan: enhancing stock price prediction and factor investment with generative adversarial networks"); Duan et al., [2022](https://arxiv.org/html/2601.17773v1#bib.bib45 "Factorvae: A probabilistic dynamic factor model based on variational autoencoder for predicting cross-sectional stock returns"); Tepelyan and Gopal, [2023](https://arxiv.org/html/2601.17773v1#bib.bib56 "Generative machine learning for multivariate equity returns"); Cho et al., [2025](https://arxiv.org/html/2601.17773v1#bib.bib69 "Diffolio: A Diffusion Model for Multivariate Probabilistic Financial Time-Series Forecasting and Portfolio Construction")). In particular, Cho et al. ([2025](https://arxiv.org/html/2601.17773v1#bib.bib69 "Diffolio: A Diffusion Model for Multivariate Probabilistic Financial Time-Series Forecasting and Portfolio Construction")) propose a hierarchical attention-based diffusion model that integrates asset-specific and systematic covariates to produce calibrated conditional predictive distributions for multivariate returns, with a primary focus on probabilistic forecasting and portfolio allocation.

In contrast, MarketGAN is designed as a distributional learning framework that embeds economic structure directly into the data generating process through a factor-model-based architecture. Rather than emphasizing conditional prediction at short horizons, MarketGAN aims to learn and extend the joint distribution of asset returns itself, preserving complex cross-sectional dependence and tail co-movement across a large universe of assets. While many existing models rely on latent factors without clear economic interpretation or generate assets independently and concatenate them post hoc, MarketGAN directly targets high-dimensional joint dependence in a manner that is explicitly grounded in asset-pricing theory.

Our work is also closely related, at a conceptual level, to a recent literature on missing data and sparsity in high-dimensional asset pricing panels.
Bryzgalova et al. ([2025a](https://arxiv.org/html/2601.17773v1#bib.bib58 "Missing financial data"), [b](https://arxiv.org/html/2601.17773v1#bib.bib57 "Forest through the trees: building cross-sections of stock returns")) show that missing characteristics and noise in large cross sections distort the estimation of economically relevant directions in return space, particularly low-variance components important for portfolio choice.
Similarly, Freyberger et al. ([2025](https://arxiv.org/html/2601.17773v1#bib.bib59 "Missing data in asset pricing panels")) document the instability of cross-sectional dependence in sparse panels, and Chen and McCoy ([2024](https://arxiv.org/html/2601.17773v1#bib.bib60 "Missing values handling for machine learning portfolios")) show that small covariance estimation errors induced by missing data can translate into large portfolio losses. While this literature focuses on imputation, regularization, and dimensionality reduction within observed panels, it highlights a deeper limitation that in high-dimensional settings, the joint distribution of asset returns is only weakly identified from historical observations alone. Our approach takes a complementary perspective by treating the problem as one of distributional representation rather than data reconstruction, and by directly learning and generating joint return distributions subject to an economically motivated structure.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2601.17773v1#S2 "2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") describes the components of our proposed model, including GANs, TCNs, and their integration.
The architecture of our proposed model and its perspective as a stochastic coefficient factor model are then described in Section [3](https://arxiv.org/html/2601.17773v1#S3 "3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
Empirical experiments are presented in Section [4](https://arxiv.org/html/2601.17773v1#S4 "4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") where we evaluate the fidelity of the generated data, assess its ability to reproduce stylized facts. Section [5](https://arxiv.org/html/2601.17773v1#S5 "5 Applications: Portfolio Optimization ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") demonstrates the generated synthetic data’s utility in portfolio optimization and Section [6](https://arxiv.org/html/2601.17773v1#S6 "6 Conclusion ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") concludes.

## 2 Methodological Background

### 2.1 Generative Adversarial Networks (GANs)

GANs provide a flexible framework for learning complex data distributions by formulating a two-player game between a generator and a discriminator (Goodfellow et al., [2014](https://arxiv.org/html/2601.17773v1#bib.bib10 "Generative adversarial nets")). The generator GG aims to produce samples that resemble the true data distribution pd​a​t​a​(x)p\_{data}(x), while the discriminator DD aims to distinguish real from generated samples. Through adversarial training, the generator learns to approximate the underlying data distribution without requiring an explicit likelihood specification. Formally, the generator GG takes as input a random noise vector z∼pz​(z)z\sim p\_{z}(z) drawn from a simple prior distribution (e.g., Gaussian) and outputs synthetic samples G​(z)G(z) that resemble the real data. Then, these two neural networks compete against each other in a minimax game described by the following objective function:

|  |  |  |
| --- | --- | --- |
|  | minG⁡maxD⁡V​(D,G)=𝔼x∼pd​a​t​a​(x)​[log⁡D​(x)]+𝔼z∼pz​(z)​[log⁡(1−D​(G​(z)))].\min\_{G}\max\_{D}V(D,G)=\mathbb{E}\_{x\sim p\_{data}(x)}\left[\log D\left(x\right)\right]+\mathbb{E}\_{z\sim p\_{z}(z)}\left[\log\left(1-D\left(G(z)\right)\right)\right]. |  |

When the discriminator is optimal, the minimization of this objective corresponds to minimizing the Jensen-Shannon divergence between the real and generated distributions:

|  |  |  |
| --- | --- | --- |
|  | J​S​D​(pd​a​t​a,qG)=12​DK​L​(pd​a​t​a∥M)+12​DK​L​(qG∥M),JSD(p\_{data},q\_{G})=\frac{1}{2}D\_{KL}\left(p\_{data}\|M\right)+\frac{1}{2}D\_{KL}\left(q\_{G}\|M\right), |  |

where qGq\_{G} denotes the model distribution induced by the generator, and M=12​(pd​a​t​a+qG)M=\frac{1}{2}\left(p\_{data}+q\_{G}\right) and DK​LD\_{KL} is the Kullback-Leibler divergence.
In essence, the generator is trained to approximate the real data distribution pd​a​t​ap\_{data}.

In the context of financial data, GANs are attractive because they operate at the distributional level, rather than focusing on point predictions. This feature makes GANs well-suited for applications such as scenario generation, stress testing, and portfolio analysis, where the joint distribution of returns is more relevant than conditional means. However, standard GANs are known to be challenging to train and sensitive to data limitations, particularly in high-dimensional and noisy environments such as financial markets.

To improve training stability, several variants of GANs have been proposed. Among them, the Wasserstein GAN with gradient penalty (WGAN-GP) replaces the original Jensen-Shannon divergence with the Wasserstein distance and enforces Lipschitz continuity through a gradient penalty (Arjovsky et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib11 "Wasserstein generative adversarial networks"); Gulrajani et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib12 "Improved training of wasserstein gans")).555The formal objective function of WGAN-GP is provided in Online Appendix [A](https://arxiv.org/html/2601.17773v1#A1 "Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"). We adopt the WGAN-GP objective to ensure stable training in continuous-valued financial data.

### 2.2 Temporal Convolutional Networks (TCNs)

Modeling temporal dependence is essential for financial time-series data. TCNs provide an effective alternative to recurrent architectures by employing causal and dilated convolutions along the time dimension (Bai et al., [2018](https://arxiv.org/html/2601.17773v1#bib.bib5 "An empirical evaluation of generic convolutional and recurrent networks for sequence modeling")). Through stacked convolutional layers with increasing dilation, TCNs capture long-range temporal dependencies while maintaining computational efficiency and stable gradients. Thanks to this advantage, in the context of deep learning-based sequence modeling, TCNs (Bai et al., [2018](https://arxiv.org/html/2601.17773v1#bib.bib5 "An empirical evaluation of generic convolutional and recurrent networks for sequence modeling")) have been shown to achieve competitive performance compared to other widely-used recurrent or self-attention-based models.
TCNs apply one-dimensional convolution along the temporal axis and effectively extract features from long-range input sequences through dilated convolutions. In addition, they can offer efficient computation owing to their low computational complexity and ability to perform parallel operations.

The receptive field size (RFS) of a TCN, i.e., the number of input time steps that influence a single output time step, grows exponentially with depth. Specifically, the RFS is given by
RFS=1+2​(k−1)⋅DL−1D−1,\mathrm{RFS}=1+2(k-1)\cdot\frac{D^{L}-1}{D-1},
where kk is the kernel size, DD is the dilation factor, and LL is the number of residual blocks.
This allows TCNs to model long-term temporal dependencies effectively, even with a relatively shallow architecture.

Compared to recurrent neural networks, TCNs offer several practical advantages in financial applications. They enable parallel computation over time, avoid vanishing or exploding gradients associated with long sequences, and provide a flexible receptive field that can be adjusted to the desired temporal horizon. As a result, TCNs have been successfully applied to various sequential data problems, including audio generation and financial time series modeling (Wiese et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib1 "Quant GANs: deep generation of financial time series")).

### 2.3 GAN with TCN backbone

While GANs excel at capturing cross-sectional dependence, they do not natively account for temporal structure. A natural approach to modeling financial time series is therefore to combine GANs with architectures designed for temporal representation learning. In such hybrid models, temporal networks such as RNNs, transformers, or TCNs are used to encode historical information, while the GAN framework learns the distribution of future observations conditional on this temporal state.

This separation of roles is particularly appealing in finance. The temporal network extracts latent features that summarize market dynamics over time, whereas the GAN focuses on learning the conditional distribution of returns. By integrating temporal modeling into the generative process, GAN-based models can generate synthetic time-series data that reflect both inter-temporal dependence and cross-sectional structure.

Another important aspect of GANs with a TCN backbone is the inherent stochastic nature of the generator. Since the input to the generator is a sequence of random variables, the output synthetic sequence is also a random sequence.
Even under fixed conditions, repeated evaluations yield different synthetic sequences.
Hence, the generator models the conditional probability distribution of the data, which performs density estimation rather than deterministic point estimation. In addition, due to the receptive field structure of TCNs, the output at time tt, denoted by x^t\hat{x}\_{t}, depends not only on ztz\_{t} but also on a range of past latent variables {zt−k}k=0R​F​S−1\{z\_{t-k}\}\_{k=0}^{RFS-1}.
This dependence on a finitely extended temporal window implies that the process is non-Markovian, as future states are not independent of the distant past given the present. Thus, the GAN with a TCN backbone defines a multi-dimensional discrete-time non-Markovian stochastic process. This formulation enables the generator to capture intricate temporal dependencies and structural features of sequential financial data while allowing for generating diverse and statistically consistent synthetic samples.

Building on the generative and temporal modeling frameworks reviewed in this section,
the next section introduces MarketGAN, a factor-based generative model tailored to
high-dimensional asset returns.

## 3 MarketGAN

Building on the generative and temporal modeling frameworks in Section [2](https://arxiv.org/html/2601.17773v1#S2 "2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"), we introduce a factor-based generative model tailored to high-dimensional asset return generation under severe data scarcity. The central objective of MarketGAN is not to improve point predcition accuracy, but to learn joint distribution of asset returns in a manner that preserves economically meaningful cross-sectional dependence, inter-temporal dynamics, and portfolio relevant risk characteristics.

### 3.1 MarketGAN Architecture

The primary challenge addressed by MarketGAN is the severe scarcity of informative financial time-series data in high-dimensional settings. While generative models provide a natural mechanism for data augmentation, they themselves require structural regularization to remain effective in noisy and data-poor financial environments. To this end, MarketGAN incorporates domain knowledge in the form of an asset-pricing factor model, which serves as an economic inductive bias that displines the generative learning problem.

We model the excess return of NN assets at time t+1t+1, dented by 𝒓t+1∈ℝN\boldsymbol{r}\_{t+1}\in\mathbb{R}^{N}, using the following factor-model-based formulation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓t+1=𝜶t+𝜷t⋅𝑭t+1+𝝈t⊙ϵt+1,\boldsymbol{r}\_{t+1}=\boldsymbol{\alpha}\_{t}+\boldsymbol{\beta}\_{t}\cdot\boldsymbol{F}\_{t+1}+\boldsymbol{\sigma}\_{t}\odot\boldsymbol{\epsilon}\_{t+1}, |  | (1) |

where 𝑭t+1∈ℝK\boldsymbol{F}\_{t+1}\in\mathbb{R}^{K} denotes observable risk factors such as CAPM or Fama-French factors, 𝜶t∈ℝN\boldsymbol{\alpha}\_{t}\in\mathbb{R}^{N} is the vector of intercepts, 𝜷t∈ℝN×K\boldsymbol{\beta}\_{t}\in\mathbb{R}^{N\times K} is the matrix of factor loadings, 𝝈t∈ℝN\boldsymbol{\sigma}\_{t}\in\mathbb{R}^{N} scales the idiosyncratic component, and ϵt+1∈ℝN\boldsymbol{\epsilon}\_{t+1}\in\mathbb{R}^{N} represents standardized residuals. The operator ⊙\odot indicates element-wise multiplication.

The defining feature of MarketGAN is that the coefficients 𝜶t\boldsymbol{\alpha}\_{t}, 𝜷t\boldsymbol{\beta}\_{t}, and 𝝈t\boldsymbol{\sigma}\_{t} are not treated as deterministic parameters, but are instead generated as stochastic, time-varing objects by conditional GANs with a TCN backbone, as described in Section [2.3](https://arxiv.org/html/2601.17773v1#S2.SS3 "2.3 GAN with TCN backbone ‣ 2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
This design integrates three complementary components. First, the TCN backbone extracts latent temporal features from historical data, allowing the model to capture long-range inter-temporal dependence. Second, adversarial training enables flexible learning of high-dimensional joint distributions across assets. Third, the factor structure imposes economically meaningful constraints that regularize the learning problem and improve robustness under data scarcity.

Formally, the generative networks take as input sequences of latent noise vectors and observed covariates over a rolling temporal window determined by the RFS of the TCN. Specifically, for a normal random variable 𝒛u∈ℝdz\boldsymbol{z}\_{u}\in\mathbb{R}^{d\_{z}} and a covariate 𝒚u∈ℝdy\boldsymbol{y}\_{u}\in\mathbb{R}^{d\_{y}}, let 𝒛t−(RFS−1):t:={𝒛u}u=t−(RFS−1)t\boldsymbol{z}\_{t-(\mathrm{RFS}-1):t}:=\{\boldsymbol{z}\_{u}\}\_{u=t-(\mathrm{RFS}-1)}^{t} denote a sequence of latent noise vectors, and 𝒚t−(RFS−1):t:={𝒚u}u=t−(RFS−1)t\boldsymbol{y}\_{t-(\mathrm{RFS}-1):t}:=\{\boldsymbol{y}\_{u}\}\_{u=t-(\mathrm{RFS}-1)}^{t} denote a sequence of covariates over the period from t−(RFS−1)t-(\mathrm{RFS}-1) to tt.
The networks are trained to extract informative features from these past sequences, thereby capturing both cross-sectional and inter-temporal dependencies conditioned on the covariates.
In particular, the interweaving of the randomness from the dzd\_{z}-dimensional noise vectors and the dyd\_{y}-dimensional covariate inputs allows the model to approximate the joint conditional distribution of the NN-dimensional asset returns.

To enhance training stability and anchor the generative process to economically plausible scales, MarketGAN incorporates ex-post coefficient estimates obtained from standard regression.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶t=𝜶^t⊙(1+fα​(𝒛t−(RFS−1):t,𝒚t−(RFS−1):t)),𝜷t=𝜷^t⊙(1+fβ​(𝒛t−(RFS−1):t,𝒚t−(RFS−1):t)),𝝈t=𝝈^t⊙(1+fσ​(𝒛t−(RFS−1):t,𝒚t−(RFS−1):t)),\begin{gathered}\boldsymbol{\alpha}\_{t}=\hat{\boldsymbol{\alpha}}\_{t}\odot\left(1+f\_{\alpha}\left(\boldsymbol{z}\_{t-(\textrm{RFS}-1):t},\boldsymbol{y}\_{t-(\textrm{RFS}-1):t}\right)\right),\\ \boldsymbol{\beta}\_{t}=\hat{\boldsymbol{\beta}}\_{t}\odot\left(1+f\_{\beta}\left(\boldsymbol{z}\_{t-(\textrm{RFS}-1):t},\boldsymbol{y}\_{t-(\textrm{RFS}-1):t}\right)\right),\\ \boldsymbol{\sigma}\_{t}=\hat{\boldsymbol{\sigma}}\_{t}\odot\left(1+f\_{\sigma}\left(\boldsymbol{z}\_{t-(\textrm{RFS}-1):t},\boldsymbol{y}\_{t-(\textrm{RFS}-1):t}\right)\right),\end{gathered} |  | (2) |

where 𝜶^t\hat{\boldsymbol{\alpha}}\_{t}, 𝜷^t\hat{\boldsymbol{\beta}}\_{t}, and 𝝈^t\hat{\boldsymbol{\sigma}}\_{t} denote ex-post regression estimates, and fαf\_{\alpha}, fβf\_{\beta}, and fσf\_{\sigma} are TCN-based modules that generate stochastic correction terms. The multiplicative specification preserves the scale and sign structure of the baseline coefficients while allowing flexible stochastic deviations. Moreover, the three networks share all TCN layers except for their final 1×11\times 1 convolutional output layers, reflecting the idea that the coefficients are driven by common latent market dynamics. This parameter sharing scheme reduces computational complexity and improves estimation efficiency. The overall architecture of MarketGAN is illustrated in Figure [1](https://arxiv.org/html/2601.17773v1#S3.F1 "Figure 1 ‣ 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

![Refer to caption](x1.png)


Figure 1: Architecture of MarketGAN.

The idiosyncratic residual component ϵt+1\boldsymbol{\epsilon}\_{t+1} is produced via a conditional GAN with a simplified TCN structure. To ensure that residuals are independent of past uncertainty, the generator employs 1×11\times 1 convolutions for all layers, resulting in a RFS of one, and takes (𝒛𝒕+𝟏,𝒚𝒕)(\boldsymbol{z\_{t+1}},\boldsymbol{y\_{t}}) as input. This design allows the residual to depend only on contemporaneous latent noise and covariates and to be isolated from past uncertainty. Meanwhile, each noise sample 𝒛t+1\boldsymbol{z}\_{t+1}—the innovation at time t+1t+1—is subsequently reused to generate the factor model coefficients for the following period (e.g., 𝜶t+1,𝜷t+1,𝝈t+1\boldsymbol{\alpha}\_{t+1},\boldsymbol{\beta}\_{t+1},\boldsymbol{\sigma}\_{t+1}). This reuse of latent noise across periods elaborates the model’s temporal dependency and induces a nonlinear moving average type dependence structure. Consequently, MarketGAN captures rich inter-temporal dynamics without imposing a Markovian restriction.

The discriminator mirrors the generator’s temporal structure and operates on a sequence of asset returns and covariates. For a given input window, it produces a single scalar score that reflects the discrepancy between real and generated return sequences, consistent with the WGAN-based training objective.666The discriminator employs a TCN with a final linear layer mapping to a scalar value, and takes as input a sequence (𝒙t+1:t+TL,𝒚t+1:t+TL)(\boldsymbol{x}\_{t+1:t+T\_{L}},\boldsymbol{y}\_{t+1:t+T\_{L}}), where 𝒙u\boldsymbol{x}\_{u} denotes either real or generated excess returns at time uu.
In other words, the discriminator outputs a single scalar value for a given sequence of length TLT\_{L}.
In standard GAN formulations, this scalar passes through a sigmoid activation function, and, in WGANs, it directly serves as a critic score for measuring the Wasserstein distance.

In the next subsection, we interpret MarkeGAN as both a data generator and a stochastic coefficient factor model, and discuss how these perspectives clarify its role in financial applications.

### 3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model

MarketGAN is designed primarily as a data generation framework that produces synthetic realizations of high-dimensional asset returns. Rather than estimating model coefficients once and treating them as fixed, MarketGAN generates the coefficients of the factor model through neural networks and uses them to construct return realizations. As each inference, the model produces a distinct NN-dimensional vector of excess returns, allowing the generation of an effectively unlimited number of synthetic samples. These samples are designed to preserve the statistical properties of the high-dimensional real data distribution learned during training.

Because MarketGAN is implemented using a conditional GAN, it naturally supports conditional data generation. By conditioning on observed covariates, such as macroeconomic variables or market state indicators, the model approximates time-varying conditional return distributions. This capability enables MarketGAN to generate realistic return paths that adapt to evolving economic conditions, making it suitable for applications such as scenario analysis, stress testing, and portfolio evaluation under alternative economic states. From this perspective, MarketGAN functions as a flexible return generator operating at the distributional level rather than as a point forecasting model.

Beyond its role as a return data generator, MarketGAN can also be interpreted as a stochastic coefficient factor model. While generative neural networks are often used primarily for data augmentation, their fundamental capability lies in high-dimensional density estimation. In this framework, training MarketGAN corresponds to optimizing the deterministic weights of the generative neural networks that parameterize the stochastic coefficient processes. Specifically, instead of providing fixed point-estimates for the model parameters, MarketGAN implicitly learns the high-dimensional joint distribution of these coefficients—𝜶t,𝜷t,\boldsymbol{\alpha}\_{t},\boldsymbol{\beta}\_{t}, and 𝝈t\boldsymbol{\sigma}\_{t}—across the NN assets via adversarial training.

The use of conditional GANs allows the coefficient distributions to vary over time as functions of observed covariates, capturing changes in market conditions and risk exposures. Moreover, since MarketGAN employs a TCN backbone to model temporal dependence, the resulting coefficient processes are non-Markovian as described in Section [2.3](https://arxiv.org/html/2601.17773v1#S2.SS3 "2.3 GAN with TCN backbone ‣ 2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"). Current realizations depend on a finite but extended history of latent noise and covariates, rather than solely on the most recent state. From this viewpoint, fitting MarketGAN to historical data can be seen as calibrating nonlinear, non-Markovian stochastic processes that govern the dynamics of factor model coefficients.

This interpretation connects MarketGAN to the broader literature on stochastic coefficient and time-varying factor models (Fabozzi and Francis, [1978](https://arxiv.org/html/2601.17773v1#bib.bib44 "Beta as a random coefficient"); Chamberlain, [1982](https://arxiv.org/html/2601.17773v1#bib.bib37 "Multivariate regression models for panel data"); Ang and Chen, [2007](https://arxiv.org/html/2601.17773v1#bib.bib33 "CAPM over the long run: 1926–2001"); Dangl and Halling, [2012](https://arxiv.org/html/2601.17773v1#bib.bib32 "Predictive regressions with time-varying coefficients"); Jostova and Philipov, [2005](https://arxiv.org/html/2601.17773v1#bib.bib34 "Bayesian analysis of stochastic betas"); Boloorforoosh et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib35 "Beta risk in the cross-section of equities"); Armstrong et al., [2013](https://arxiv.org/html/2601.17773v1#bib.bib36 "Factor-loading uncertainty and expected returns")). Classical approaches in this literature allow factor loadings to evolve over time, typically through linear state-space or parametric specifications. MarketGAN generalizes these models by allowing for nonlinear dynamics, high-dimensional cross-sectional dependence, and flexible conditional distributions, while retaining the economically disciplined structure of a factor model.

## 4 Empirical Experiments

This section evaluates the empirical performance of MarketGAN as a generative model for high-dimensional asset returns. The objective of the empirical analysis is not to assess predictive accuracy in the conventional sense, but to examine whether synthetic data generated by MarketGAN replicate key statistical and economic properties of real financial data. In particular, we focus on the model’s ability to preserve cross-sectional dependence, inter-temporal dynamics, and portfolio-relevant risk characteristics under realistic data constraints.

### 4.1 Data and Experimental Setup

We conduct our empirical analysis using daily excess returns of stocks in the S&P 100 index. The sample is constructed using constituents observed as of December 31, 2023, and includes all assets that appeared at least once during the in-sample period. The selection yields a balanced universe of 98 assets, allowing us to focus on high-dimensional cross-sectional dependence while avoiding survivorship bias from restricting attention to continuously traded stocks. The sample is divided into an in-sample period from January 1, 1991, to December 31, 2015, and an out-of-sample period from January 1, 2016, to December 31, 2023. The in-sample period is used to train and validate the generative models, while the out-of-sample period is reserved exclusively for evaluation. Excess returns are computed using the one-month U.S. Treasury bill rate as the risk-free rate. As covariates, we employ macroeconomic predictors from Welch and Goyal ([2008](https://arxiv.org/html/2601.17773v1#bib.bib28 "A comprehensive look at the empirical performance of equity premium prediction")) and Gu et al. ([2020](https://arxiv.org/html/2601.17773v1#bib.bib29 "Empirical asset pricing via machine learning")) which consist of the following eight variables, such as dividend-price ratio (dp), earnings-price ratio (ep), book-to-market ratio (bm), T-bill rate (tbl), term spread (tms), default spread (dfy), net equity  issue (ntis), and stock variance (svar).
Since these macroeconomic variables are available at a monthly frequency, missing values are forward-filled with the most recent observations.

Because not all assets are observed continuously throughout the in-sample period, missing returns and coefficients are imputed using a conventional regression-based factor model. For each asset with missing observations, factor model coefficients, 𝜶^i\hat{\boldsymbol{\alpha}}\_{i} and 𝜷^i\hat{\boldsymbol{\beta}}\_{i}, are estimated using the full in-sample data. Missing values are then filled by identifying dates with macroeconomic conditions most similar to those of the missing observations, measured by Euclidean distance in the covariate space, and averaging the corresponding estimated coefficients. Specifically, the missing returns is filled with 𝜶^i+𝜷^i⋅𝑭\hat{\boldsymbol{\alpha}}\_{i}+\hat{\boldsymbol{\beta}}\_{i}\cdot\boldsymbol{F} where
𝑭\boldsymbol{F} denotes the factor values on that day.

We propose three types of MarketGAN models, each based on widely used factor models. The first is based on the CAPM and includes only the market factor. The second and third are based on the Fama-French three-factor and five-factor models, respectively. We refer to these factor models as FF-1, FF-3, and FF-5, and denote the corresponding generative models by MarketGAN1, MarketGAN3, and MarketGAN5, respectively. Then, MarketGAN1 is based on the single-factor CAPM and uses only the excess return on the market portfolio as the risk factor to capture time-varying market exposure and idiosyncratic risk dynamics while maintaining a parsimonious structure. MarketGAN3 extends this framework by incorporating the market factor, the size factor (SMB), and the value factor (HML). This specification allows the generative model to capture cross-sectional variation in returns associated with firm size and value characteristics, as well as their time-varying dynamics. MarketGAN5 further enriches the factor structure by adopting the market, size, and value factors with profitability (RMW) and investment (CMA) factors. By including these additional sources of systematic risk, MarketGAN5 provides the most flexible specification and allows us to assess whether a richer economic structure improves the quality of synthetic return generation.777For detailed descriptions of these factor portfolios, we refer to Fama and French ([1993](https://arxiv.org/html/2601.17773v1#bib.bib38 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.17773v1#bib.bib39 "A five-factor asset pricing model")). Across all three variants, the TCN backbone and adversarial training procedure remain identical. This design ensures that differences in empirical performance can be attributed primarily to the underlying factor specification rather than to changes in network architecture or training methodology.

Each FF-kk, k=1,3,5,k=1,3,5, model is of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓t+1=𝜶^t+𝜷^t⋅𝑭t+1+𝝈^t⊙ϵt+1,\boldsymbol{r}\_{t+1}=\hat{\boldsymbol{\alpha}}\_{t}+\hat{\boldsymbol{\beta}}\_{t}\cdot\boldsymbol{F}\_{t+1}+\hat{\boldsymbol{\sigma}}\_{t}\odot\boldsymbol{\epsilon}\_{t+1}, |  | (3) |

where the coefficients 𝜶^t\hat{\boldsymbol{\alpha}}\_{t}, 𝜷t^\hat{\boldsymbol{\beta}\_{t}}, and 𝝈t^\hat{\boldsymbol{\sigma}\_{t}} are deterministically estimated at each time tt, and 𝑭t+1\boldsymbol{F}\_{t+1} is the kk-dimensional factor.
Specifically, the coefficients 𝜶^t\hat{\boldsymbol{\alpha}}\_{t} and 𝜷^t\hat{\boldsymbol{\beta}}\_{t} are estimated by rolling window regressions over the past one year of data including time tt, and 𝝈^t\hat{\boldsymbol{\sigma}}\_{t} is given by the standard deviation of the regression residuals within the same window. This conventional factor model serves two purposes. First, it provides a transparent benchmark against which the performance of MarketGAN can be evaluated. Second, rolling-window estimates of the factor model coefficients are used as ex-post baseline coefficients in the multiplicative correction structure of MarketGAN, defined in ([2](https://arxiv.org/html/2601.17773v1#S3.E2 "In 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks")). Specifically, intercepts and factor loadings are estimated using one-year rolling regressions, and idiosyncratic volatility is computed as the standard deviation of residuals within the same window.

The generators for the time-varying intercepts 𝜶t\boldsymbol{\alpha}\_{t}, factor loadings 𝜷t\boldsymbol{\beta}\_{t}, and volatilities 𝝈t\boldsymbol{\sigma}\_{t} share a common TCN backbone, reflecting the assumption that these coefficients are driven by shared latent market dynamics. The backbone employs a kernel size of two (k=2k=2), a dilation factor of two (D=2D=2), and six residual blocks (L=6L=6), resulting in a receptive field that spans 127 time steps (RFS=127). Each coefficient has its own output layer, while all intermediate layers are shared. The idiosyncratic residual component is generated by a separate conditional GAN with a simplified temporal structure, ensuring that residual shocks are contemporaneous while temporal dependence is captured primarily through the coefficients.888Specifically, these networks share all layers except the final output layer ϕO\phi\_{O}: the input mapping ϕI\phi\_{I} and the residual blocks gℓg\_{\ell} for ℓ=1,2,…,L\ell=1,2,\dots,L are shared across the three coefficient networks, while each coefficient has its own output mapping layer, denoted by ϕOα\phi\_{O}^{\alpha}, ϕOβ\phi\_{O}^{\beta}, and ϕOσ\phi\_{O}^{\sigma}, respectively.
On the other hand, the generator for ϵt+1\boldsymbol{\epsilon}\_{t+1} uses a kernel size of k=1k=1, a dilation factor of D=1D=1, and L=6L=6 residual blocks, which leads to an RFS of 1.
The latent dimension of normal random variables 𝒛\boldsymbol{z} is set to dz=10d\_{z}=10.
As a result, the generator takes a total of (127+1)×dz=1280(127+1)\times d\_{z}=1280 independent standard normal random inputs 𝒛t−(RFS−1):t+1\boldsymbol{z}\_{t-(\mathrm{RFS}-1):t+1} to generate a single sample of NN-dimensional returns at each time step.

All models are trained for 300 epochs. The in-sample period is split into training and validation subsets in a 7:1 ratio, with the most recent portion reserved for validation. Model selection is based on the similarity between the correlation matrix of generated returns and that of real returns, measured using the Frobenuis norm. To mitigate the loss of recent information due to this split, we perform an additional fine-tuning stage on the validation set with a one-tenth of the original learning rate. Consistent with standard practice in GAN training, the discriminator is updated more frequently than the generator to promote training stability. Other implementation details and hyperparameters used in the three MarketGAN models are presented in Online Appendix [B](https://arxiv.org/html/2601.17773v1#A2 "Appendix B Implementational Details and Hyperparameters of MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

As benchmark methods, we consider factor-model-based bootstrap procedures corresponding to the FF-1, FF-3 and FF-5 models. These approaches generate synthetic returns by combining rolling-window estimates fo factor model coefficients with independently drawn Gaussian residuals. Specifically, these use the following formulation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓^t+1=𝜶^t+𝜷^t⋅𝑭t+1+𝝈^t⊙ϵt+1,ϵt+1∼𝒩​(0,I),\hat{\boldsymbol{r}}\_{t+1}=\hat{\boldsymbol{\alpha}}\_{t}+\hat{\boldsymbol{\beta}}\_{t}\cdot\boldsymbol{F}\_{t+1}+\hat{\boldsymbol{\sigma}}\_{t}\odot\boldsymbol{\epsilon}\_{t+1},\quad\boldsymbol{\epsilon}\_{t+1}\sim\mathcal{N}(0,I), |  | (4) |

where 𝑭t+1\boldsymbol{F}\_{t+1} denotes the factor realizations at time t+1t+1, defined by the respective FF-kk model.
The coefficients 𝜶^t\hat{\boldsymbol{\alpha}}\_{t}, 𝜷^t\hat{\boldsymbol{\beta}}\_{t}, and 𝝈^t\hat{\boldsymbol{\sigma}}\_{t} are estimated ex post using a rolling window of one-year data ending at time tt, and are also used in ([2](https://arxiv.org/html/2601.17773v1#S3.E2 "In 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks")) as ex-post coefficients.
Because these bootstrap methods share the same factor structure but lack a generative neural network component, they provide transparent baselines that isolate the incremental contribution of MarketGAN. Comparing MarketGAN to these benchmarks allows us to assess whether adversarial learning adds value beyond traditional factor-based resampling.

### 4.2 Marginal Return Distributions

We begin the empirical evaluation by examining whether MarketGAN preserves the marginal distributional properties of asset returns. Reproducing marginal distributions constitutes a necessary, though not sufficient, condition for realistic synthetic data generation, and has been widely used as a baseline diagnostic on financial generative models (e.g., Takahashi et al., [2019](https://arxiv.org/html/2601.17773v1#bib.bib18 "Modeling financial time-series with generative adversarial networks"); Wiese et al., [2020](https://arxiv.org/html/2601.17773v1#bib.bib1 "Quant GANs: deep generation of financial time series"); Cont et al., [2022](https://arxiv.org/html/2601.17773v1#bib.bib27 "Tail-gan: Learning to simulate tail risk scenarios")). In financial markets, asset returns are known to exhibit non-Gaussian features such as heavy tails and excess kurtosis, which play a central role in risk assessment and portfolio management. We therefore assess the extent to which MarketGAN-generated returns replicate these stylized marginal characteristics relative to factor-model-based bootstrap benchmarks.

We begin by examining market-level behavior, constructing an equal-weighted portfolio of the NN
assets and comparing its excess return paths across real data, MarketGAN-generated data, and factor-model-based bootstrap benchmarks. We plot the realized equal-weighted excess returns over the out-of-sample period together with the mean and one-standard-deviation bands computed from 100 synthetic sample paths. Across all factor specifications, both MarketGAN and bootstrap methods closely track the realized aggregate returns. This result highlights the importance of the factor structure in capturing aggregate market dynamics and suggests that even simple factor-based approaches can effectively reproduce market-level behavior.999See Figure [8](https://arxiv.org/html/2601.17773v1#A5.F8 "Figure 8 ‣ Appendix E Additional Figures ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") in the Online Appendix. The relatively narrow dispersion bands indicate that idiosyncratic variations largely cancel out at the portfolio level. We also examine marginal distribution at the individual asset level, using GOOG as a representative example. Figure [9](https://arxiv.org/html/2601.17773v1#A5.F9 "Figure 9 ‣ Appendix E Additional Figures ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") compares the realized excess returns of GOOG with synthetic returns generated by MarketGAN and the corresponding bootstrap methods. Similar to equal-weighted portfolio, all models capture the mean behavior reasonably well, but MarketGAN-generated returns exhibit substantially narrower standard deviation bands than those produced by bootstrap methods, indicating a closer fit to the empirical distribution of individual asset returns. In contrast, bootstrap-based synthetic paths exhibit greater variability, reflecting their reliance on independently drawn residuals rather than on a learned distributional structure.

To complement these visual comparisons, we quantify marginal reconstruction accuracy using root-mean-square error (RMSE) and mean absolute error (MAE), computed by comparing 100 synthetic sample paths with realized returns and averaging across assets and time. Table [1](https://arxiv.org/html/2601.17773v1#S4.T1 "Table 1 ‣ 4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") reports these metrics for MarketGAN and bootstrap methods under different factor specifications. MarketGAN consistently outperforms the corresponding bootstrap benchmarks. It demonstrates superior marginal explanatory power. Moreover, performance improves for both approaches as the number of factors increases, consistent with the factor models (e.g., Fama and French, [1993](https://arxiv.org/html/2601.17773v1#bib.bib38 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.17773v1#bib.bib39 "A five-factor asset pricing model")). Notably, MarketGAN with three factors achieves lower error metrics than the five-factor bootstrap, which underscores the added value of adversarial distribution learning beyond factor richness alone.

| Metric | MarketGAN | | | Factor-model-based bootstrap | | |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 5 | 1 | 3 | 5 |
| RMSE | 0.01743 | 0.01570 | 0.01541 | 0.01775 | 0.01648 | 0.01610 |
| MAE | 0.01390 | 0.01271 | 0.01256 | 0.01480 | 0.01375 | 0.01345 |

Table 1: Comparisons of RMSE and MAE of synthetic sample paths for models and factor specifications. Bold indicates the best.

We further assess the shape of marginal return distributions by comparing histograms of daily excess returns aggregated across assets. Figure [2](https://arxiv.org/html/2601.17773v1#S4.F2 "Figure 2 ‣ 4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") contrasts the empirical distributions with those generated by MarketGAN and bootstrap methods under one-, three-, and five-factor specifications. Consistent with prior evidence on financial returns (Mandelbrot, [1963](https://arxiv.org/html/2601.17773v1#bib.bib26 "The variation of certain speculative prices"); Cont, [2001](https://arxiv.org/html/2601.17773v1#bib.bib16 "Empirical properties of asset returns: stylized facts and statistical issues")), real data display pronounced leptokurtosis and heavy tails. MarketGAN-generated distributions closely resemble these features, whereas bootstrap-based distributions are visibly less peaked and exhibit thinner tails across all factor specifications. As the number of factors increases, MarketGAN tends to align more closely with the empirical distribution, whereas bootstrap methods do not exhibit a comparable improvement. We observe similar results for return distributions aggregated at weekly and monthly frequencies, where MarketGANs consistently demonstrate better alignment with real data than their bootstrap counterparts. These additional results are presented in Online Appendix [C](https://arxiv.org/html/2601.17773v1#A3 "Appendix C Histograms of Aggregated Excess Returns at Weekly and Monthly Frequencies ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

![Refer to caption](x2.png)


(a) One-factor models

![Refer to caption](x3.png)


(b) Three-factor models

![Refer to caption](x4.png)


(c) Five-factor models

Figure 2: Marginal distributions of daily excess returns. FF-1, FF-3, and FF-5 denote the respective factor-model-based bootstrap methods.

To provide a more systematic assessment, we compare the first four moments (mean, variance, skewness, and kurtosis) of marginal return distributions across assets. For each asset, these moments are computed using realized returns for the real data and using synthetic returns averaged over 100 generated paths for each model. Figure [3](https://arxiv.org/html/2601.17773v1#S4.F3 "Figure 3 ‣ 4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") summarizes the cross-sectional distribution of these moments using boxplots. For the sample means, MarketGAN models may appear less aligned with the real data than the bootstrap methods. However, a closer inspection reveals that the discrepancies are not that significant, typically ranging between 2×10−42\times 10^{-4} to 3×10−43\times 10^{-4}. The bootstrap methods’ slightly closer alignment can be attributed to their construction based on factor models with symmetric noise components. Conversely, MarketGAN generates synthetic returns by learning the distribution of stochastic coefficient processes via adversarial training without explicitly imposing symmetry restrictions. Nevertheless, MarketGAN models still produce nearly unbiased synthetic returns. Regarding the variance, both methods show comparable performance. However, MarketGAN exhibits a clear advantage in reproducing higher-order moments. MarketGAN captures skewness and kurtosis more accurately, reflecting its ability to model asymmetry and tail risk in return distribution.

![Refer to caption](x5.png)


(a) One-factor models

![Refer to caption](x6.png)


(b) Three-factor models

![Refer to caption](x7.png)


(c) Five-factor models

Figure 3: Boxplots of the first to fourth moments (mean, variance, skewness, kurtosis) of asset returns generated by MarketGAN and factor-model-based bootstrap methods.
Each boxplot summarizes the 10th, 25th, 50th, 75th, and 90th percentiles across assets.

Despite these improvements, some limitations remain. For example, about 10% of the real data exhibit extremely high kurtosis values exceeding 20 and a substantial deviation from the median kurtosis value of approximately 10, which MarketGAN does not fully reproduce. This suggests that while the model captures heavy-tailed behavior overall, it does not perfectly replicate the most extreme marginal tail events. These findings highlight both the strengths and current limitations of the proposed generative framework and motivate the subsequent analysis of inter-temporal and cross-sectional dependence, where MarketGAN’s advantages are more pronounced.

### 4.3 Inter-temporal Dependencies

We next evaluate whether MarketGAN reproduces inter-temporal dependence structures observed in financial return data. While marginal distributions capture static features of returns, realistic synthetic data must also reflect dynamic properties that characterize financial time series. We focus on three widely documented stylized facts: linear unpredictability, volatility clustering, and leverage effects. These features capture the absence of linear predictability in returns alongside the presence of persistent and asymmetric volatility dynamics.

Linear unpredictability refers to the empirical observation that asset returns exhibit negligible autocorrelation at short horizons. This property is commonly assessed through the autocorrelation function (ACF), which measures the correlation between returns at different lags and typically decays rapidly toward zero. Specifically, ACF​(k)=Corr​(rt+k,rt)\mathrm{ACF}(k)=\mathrm{Corr}(r\_{t+k},r\_{t}). In contrast, volatility clustering is characterized by positive, persistent autocorrelation in squared returns, indicating that periods of high volatility tend to be followed by further periods of high volatility. It implies that VC​(k)=Corr​(rt+k2,rt2)\mathrm{VC}(k)=\mathrm{Corr}(r\_{t+k}^{2},r\_{t}^{2}) starts with a significant positive value and diminishes to zero. A related phenomenon is the leverage effect, whereby negative returns are associated with higher subsequent volatility, leading to a negative correlation between returns and future squared returns. In particular, Lev​(k)=Corr​(rt+k2,rt)\mathrm{Lev}(k)=\mathrm{Corr}(r\_{t+k}^{2},r\_{t}) has a negative value for small lag and reverts to zero. The leverage effect is associated with increased volatility following negative returns, commonly observed in markets and closely related to negative skewness.

We begin by examining these inter-temporal characteristics at the market level using equal-weighted returns. Figure [4](https://arxiv.org/html/2601.17773v1#S4.F4 "Figure 4 ‣ 4.3 Inter-temporal Dependencies ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") displays the ACF, volatility clustering (VC), and leverage effect (Lev) computed from synthetic sample paths generated by MarketGAN and from factor-model-based bootstrap methods, alongside the corresponding statistics from real data. For visual clarity, we randomly select 10 out of the 100 generated sample paths for plotting and focus on the five-factor specification in the main text, with results for one- and three-factor models reported separately in Online Appendix [E](https://arxiv.org/html/2601.17773v1#A5 "Appendix E Additional Figures ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"). Across all three measures, MarketGAN-generated returns closely replicate the patterns observed in real data. The autocorrelation of returns remains close to zero across lags, while squared returns exhibit significant positive autocorrelation at short horizons that gradually decay. Similarly, the leverage effect is evident in the negative correlation between current returns and future volatility. The factor-model-based bootstrap methods exhibit broadly similar aggregate behavior, reflecting the role of the factor structure in capturing market-wide dynamics. This similarity is consistent with the accurate reconstruction of aggregate returns observed in the marginal distribution analysis. At the market level, therefore, both approaches succeed in reproducing key inter-temporal stylized facts.

![Refer to caption](x8.png)


(a) ACF of MarketGAN5

![Refer to caption](x9.png)


(b) ACF of FF-5 bootstrap

![Refer to caption](x10.png)


(c) VC of MarketGAN5

![Refer to caption](x11.png)


(d) VC of FF-5 bootstrap

![Refer to caption](x12.png)


(e) Lev of MarketGAN5

![Refer to caption](x13.png)


(f) Lev of FF-5 bootstrap

Figure 4: ACF, VC, and Lev of real and synthetic equal-weighted excess return samples generated by the MarketGAN5 and FF-5 bootstrap.

We also examine the individual asset dynamics, again using GOOG as an illustrative example.101010The ACF, VC, and Lev functions computed from real GOOG returns with those obtained from synthetic returns generated by five-factor MarketGAN and bootstrap methods are compared for one-, three-, and five-factor models, as provided in Online Appendix [E](https://arxiv.org/html/2601.17773v1#A5 "Appendix E Additional Figures ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"). Compared to the equal-weighted portfolio, individual asset returns exhibit greater variability in their autocorrelation patterns. Nevertheless, MarketGAN-generated series reproduce the qualitative features observed in the real data. Linear unpredictability is preserved, volatility clustering remains pronounced at short lags, and the leverage effect is clearly evident. Bootstrap methods yield similar qualitative patterns, though with slightly greater dispersion across synthetic paths.

Overall, the results indicate that MarketGAN effectively captures inter-temporal dependence structures characteristic of financial return series. Importantly, this performance is achieved without imposing explicit parametric assumptions on volatility dynamics, such as GARCH-type specifications. Instead, temporal dependence emerges endogenously through the TCN backbone that governs the evolution of stochastic factor loadings and volatilities. At the same time, the similarity between MarketGAN and bootstrap methods in some inter-temporal metrics suggests that factor structure alone accounts for a substantial portion of temporal dynamics at both the market and individual asset levels. These findings highlight a key distinction between temporal and cross-sectional aspects of generative fidelity. While factor-based approaches are often sufficient to reproduce aggregate and individual time-series dynamics, capturing cross-sectional dependence across many assets requires explicitly modeling the joint distribution. We examine this dimension in the next subsection, where we assess MarketGAN’s ability to reproduce cross-sectional correlations and co-movements in asset returns.

### 4.4 Cross-sectional Dependence

We now turn to cross-sectional dependence, which constitutes a central requirement for synthetic data intended for portfolio analysis and risk management. While marginal distributions and inter-temporal dynamics assess univariate and time-series fidelity, realistic multivariate return generation hinges on accurately reproducing dependence structures across assets. In particular, cross-sectional correlations and co-movements during extreme market events play a decisive role in diversification benefits and tail risk.

We assess the ability of MarketGAN to reproduce cross-sectional dependence along two complementary dimensions, which are cross-correlations of returns and cross-correlations of extreme returns. The first captures average co-movement across assets under normal market conditions, while the second focuses on dependence in the tail, which is known to intensify during market stress. These measures provide a comprehensive view of cross-asset dependence relevant for portfolio applications.

We begin by examining cross-correlations of returns defined by XCorr=Corr​(ri,t,rj,t),\text{XCorr}=\text{Corr}(r\_{i,t},r\_{j,t}), where rir\_{i} and rjr\_{j} represent excess returns for assets ii and jj, respectively. The matrix for real data represents the realized correlation of historical excess returns. For MarketGAN and bootstrap methods, we generate 100 independent synthetic paths covering the full out-of-sample period, compute the correlation matrix for each individual path and report the average of these 100 matrices. Figure [5](https://arxiv.org/html/2601.17773v1#S4.F5 "Figure 5 ‣ 4.4 Cross-sectional Dependence ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") shows the sample-estimated correlation matrices computed over the entire out-of-sample period for one-factor models. While the FF-1 bootstrap struggles to reproduce the rich correlation structure among nearly 100 assets using a single factor, MarketGAN captures a substantially more realistic dependence pattern. This result highlights the ability of adversarial learning to model complex joint distributions beyond what is achievable through factor structure alone,111111Across all factor specifications, MarketGAN-generated correlation matrices more closely resemble those observed in real data than their bootstrap counterparts, as shown in Figure [15](https://arxiv.org/html/2601.17773v1#A5.F15 "Figure 15 ‣ Appendix E Additional Figures ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") in Online Appendix. This improvement is particularly pronounced in the one-factor specification.

![Refer to caption](x14.png)


(a) Real data

![Refer to caption](x15.png)


(b) MarketGAN1

![Refer to caption](x16.png)


(c) FF-1 bootstrap

Figure 5: Cross-correlation of real and synthetic excess return samples generated by MarketGANs and factor-model-based bootstrap methods.

As the number of factors increases, both MarketGAN and bootstrap methods show improved performance in reproducing cross-sectional correlations. However, MarketGAN consistently exhibits closer alignment with the empirical correlation structure. In particular, the difference between MarketGAN and bootstrap methods narrows for the three- and five-factor models but does not disappear, suggesting that generative modeling complements, rather than replaces, economic factor structure in capturing cross-sectional dependence. This advantage can be attributed to the inherent ability of GANs to model complex joint distributions among multiple components, just as GANs applied to image data effectively capture pixel-level correlation structures.

We next examine dependence in extreme returns defined by
XCorrE=P​(ri,t​<−qi∣​rj,t<−qj),\mathrm{XCorr\_{E}}=P(r\_{i,t}<-q\_{i}\mid r\_{j,t}<-q\_{j}), where qiq\_{i} and qjq\_{j} denote the 95% quantile levels for the returns of assets ii and jj, respectively. It is measured by the conditional probability that one asset experiences a large negative return, given that another asset simultaneously experiences an extreme loss. This measure captures the tendency for correlations to increase sharply during market downturns, a well-documented empirical phenomenon with direct implications for tail risk. Extreme cross-sectional correlations display patterns similar to those observed for general cross-correlations, with MarketGAN models exhibiting superior performance and fidelity improving as the number of factors increases. For brevity, detailed figures for extreme cross-correlations are provided in Online Appendix [E](https://arxiv.org/html/2601.17773v1#A5 "Appendix E Additional Figures ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

These findings underscore a key distinction between factor-based resampling and generative modeling. Factor-model-based bootstrap methods rely on independently drawn residuals and therefore struggle to capture complex dependence structures, particularly in the tails. In contrast, MarketGAN generates returns as a single joint vector, allowing the model to learn and reproduce high-dimensional dependence patterns across assets. This joint-generation design is critical for accurately representing correlation structures that matter for portfolio diversification and risk assessment.

### 4.5 Quantitative Evaluation Metrics

Having primarily focused on qualitative evaluations thus far, we now turn to quantitative metrics to rigorously assess MarketGAN’s performance. While the visual and descriptive results in Sections [4.2](https://arxiv.org/html/2601.17773v1#S4.SS2 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks")-[4.4](https://arxiv.org/html/2601.17773v1#S4.SS4 "4.4 Cross-sectional Dependence ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") highlight how MarketGAN reproduces marginal distributions, inter-temporal dynamics, and cross-sectional dependence, quantitative measures provide a compact and comparable assessment across models and factor specifications. We consider four distance-based metrics that capture different aspects of distributional and temporal similarity. They are the Fréchet Inception Distance (FID), the Sliced Wasserstein Distance (SWD), the Mahalanobis Distance (MD), and the Dynamic Time Warping (DTW).121212FID, SWD, and MD are widely utilized metrics for evaluating generative neural networks.
FID approximates the Wasserstein-2 distance by using only the first two moments, mean and covariance.
This amounts to estimating the Wasserstein-2 distance assuming multivariate Gaussian distributions (Heusel et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib40 "Gans trained by a two time-scale update rule converge to a local nash equilibrium")).
SWD approximates the Wasserstein-1 distance by projecting high-dimensional distributions onto multiple one-dimensional subspaces and averaging their respective Wasserstein distances (Bonneel et al., [2015](https://arxiv.org/html/2601.17773v1#bib.bib21 "Sliced and radon wasserstein barycenters of measures")).
MD measures the distance between a point and a distribution considering the covariance structure.
It thus becomes particularly sensitive to anomalies and useful for anomaly detection (De Maesschalck et al., [2000](https://arxiv.org/html/2601.17773v1#bib.bib41 "The mahalanobis distance")).
DTW computes an optimal alignment between two time-series, accommodating nonlinear temporal distortions and capturing phase-shifted patterns (Müller, [2007](https://arxiv.org/html/2601.17773v1#bib.bib42 "Dynamic time warping")). In addition, we compute quantitative scores for the inter-temporal and cross-sectional characteristics examined previously, including measures based on ACF, VC, Lev, XCorr\mathrm{XCorr}, and XCorrE\mathrm{XCorr\_{E}}. For all metrics, lower values indicate closer alignment between synthetic and real data. These scores are defined as the L2L^{2} distance (Frobenius norm) between estimates from real and synthetic data, with lags up to 100 considered for inter-temporal metrics.

All metrics are computed by averaging over 100 synthetic sample paths generated by each model. Table [2](https://arxiv.org/html/2601.17773v1#S4.T2 "Table 2 ‣ 4.5 Quantitative Evaluation Metrics ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") reports the results for MarketGAN and factor-model-based bootstrap methods under one-, three-, and five-factor specifications. Consistent with the qualitative evidence, MarketGAN outperforms bootstrap methods across nearly all metrics. In particular, MarketGAN achieves substantially lower values in FID and SWD, indicating that the distributions induced by MarketGAN more closely match the empirical return distribution in terms of Wasserstein-based distances. Improvements are also evident in MD and DTW, suggesting that MarketGAN-generated samples exhibit fewer distributional anomalies and better temporal alignment with real return series.

| Metrics |  | MarketGAN | | | Factor-model-based bootstrap | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Factors | 1 | 3 | 5 | 1 | 3 | 5 |
| FID | | 0.00189 | 0.00148 | 0.00146 | 0.00362 | 0.00189 | 0.00149 |
| SWD | | 0.00116 | 0.00086 | 0.00092 | 0.00147 | 0.00123 | 0.00117 |
| MD | | 11.23570 | 10.69934 | 10.46770 | 15.44894 | 14.26671 | 13.86999 |
| DTW | | 9.17709 | 8.43424 | 8.32902 | 9.19236 | 8.57615 | 8.41928 |
| ACF | | 0.02438 | 0.02378 | 0.02356 | 0.02417 | 0.02326 | 0.02301 |
| VC | | 0.04108 | 0.03837 | 0.03952 | 0.05202 | 0.05330 | 0.05283 |
| Lev | | 0.02609 | 0.02593 | 0.02570 | 0.02650 | 0.02613 | 0.02603 |
| XCorr | | 5.54324 | 4.51026 | 4.87561 | 8.90126 | 5.93517 | 4.89255 |
| XCorrE\mathrm{XCorr\_{E}} | | 5.76577 | 5.16640 | 4.97701 | 6.36357 | 5.49201 | 5.27223 |

Table 2: Comparison of evaluation metrics across the MarketGANs and factor-model-based bootstrap methods under different factor specifications. Lower values indicate better performance, and bold represents the best.

Turning to metrics associated with inter-temporal dependence, MarketGAN and bootstrap methods perform similarly with respect to linear autocorrelation and leverage effects. It implies the strong role of factor structure in capturing these dynamics. However, MarketGAN exhibits a marked advantage in reproducing volatility clustering, consistent with the results in Section [4.3](https://arxiv.org/html/2601.17773v1#S4.SS3 "4.3 Inter-temporal Dependencies ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") and the model’s explicit temporal representation through a TCN backbone.

The most pronounced differences arise in cross-sectional metrics. MarketGAN substantially outperforms bootstrap methods in both XCorr\mathrm{XCorr} and XCorrE\mathrm{XCorr\_{E}}, particularly under lower-dimensional factor specifications. These results quantitatively confirm the visual evidence presented in Section [4.4](https://arxiv.org/html/2601.17773v1#S4.SS4 "4.4 Cross-sectional Dependence ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"). In particular, it generates asset returns as a single joint vector, allowing MarketGAN to capture complex dependence structures that are difficult to reproduce with independently sampled residuals. Notably, MarketGAN with three or five factors achieves comparable or superior performance relative to bootstrap methods with richer factor structures, underscoring the complementary role of adversarial learning and economic factor specification.

## 5 Applications: Portfolio Optimization

The preceding section demonstrates that MarketGAN generates synthetic asset returns that closely replicate key statistical properties of real financial data. In this section, we assess the economic value of MarketGAN-generated data through a standard portfolio optimization exercise—specifically, the construction of a daily-rebalanced long-only mean-variance tangency portfolio.131313Since MarketGAN is designed to generate returns at a daily frequency, adopting a daily rebalancing scheme allows us to directly evaluate the economic value of the synthetic joint distribution. Portfolio choice provides a natural and demanding downstream test for generative models, as optimal allocations are highly sensitive to estimation errors in return distributions, especially in the presence of cross-sectional correlation and tail risk. Models that fail to capture joint dependence structures may appear adequate when evaluated marginally, yet perform poorly when used for portfolio construction. Our objective is not to propose a new portfolio strategy, but to evaluate whether synthetic data generated by MarketGAN can serve as reliable inputs for standard portfolio optimization problems. To this end, we compare portfolios constructed using MarketGAN-generated returns with those based on synthetic data from factor-model-based bootstrap methods and, where appropriate, real historical data. By holding the portfolio optimization procedure fixed, we isolate the effect of the data generation mechanism on economic outcomes. In words, we focus on whether improvements in statistical fidelity documented in Section [4](https://arxiv.org/html/2601.17773v1#S4 "4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") lead to economically meaningful gains in portfolio performance.

### 5.1 Portfolio Construction and Experimental Design

We consider daily-rebalaned long-only mean-variance tangency portfolios based on covariance matrices estimated from NN-dimensional synthetic return samples. The portfolio is based on the same universe of N=98N=98 S&P 100 constituents detailed in Section [4.1](https://arxiv.org/html/2601.17773v1#S4.SS1 "4.1 Data and Experimental Setup ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"), with the construction procedure implemented as follows. At each rebalancing date tt, we first obtain a realized future factor vector 𝑭t+1\boldsymbol{F}\_{t+1} using the forecasting or simulation methods described below. MarketGAN then generates a large set of synthetic excess returns for time t+1t+1 by combining generated stochastic coefficients with realizations of the factor vector. Specifically, for a given factor realization 𝑭t+1\boldsymbol{F}\_{t+1}, MarketGAN exploits the stochasticity of its generated coefficients (𝜶t,𝜷t,𝝈t\boldsymbol{\alpha}\_{t},\boldsymbol{\beta}\_{t},\boldsymbol{\sigma}\_{t}) and idiosyncratic residuals (ϵt+1\boldsymbol{\epsilon}\_{t+1}) to produce 10,000 distinct synthetic return vectors. The expected return vector μ^t+1\hat{\mu}\_{t+1} and the covariance matrix Σ^t+1\hat{\Sigma}\_{t+1} are computed as the empirical mean and sample covariance of this generated set, respectively. Because the covariance matrix is estimated dynamically at each date using these synthetic returns, portfolios are rebalanced daily to align with the data generation process.

A key practical consideration is the availability of future factor realizations 𝑭t+1\boldsymbol{F}\_{t+1} as given in ([1](https://arxiv.org/html/2601.17773v1#S3.E1 "In 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks")). To address this issue, we consider two approaches. First, we forecast future factor values using simple time-series methods, including a one-year rolling average and a vector autoregression (VAR). Second, we conduct a perturbed forecast simulation in which controlled levels of noise are added to realized factor values to generate unbiased but noisy predictors with predetermined predictive accuracy. These two approaches allow us to separate the effect of factor forecasting error from the effect of the synthetic data generation mechanism itself.

To isolate the contribution of MarketGAN, we compare portfolio performance against several benchmark portfolios. These include the market portfolio and mean–variance portfolios constructed using alternative covariance estimation methods. Specifically, we consider covariance matrices estimated from historical sample returns, the Ledoit–Wolf shrinkage estimator (Ledoit and Wolf, [2004](https://arxiv.org/html/2601.17773v1#bib.bib43 "A well-conditioned estimator for large-dimensional covariance matrices")), and factor-model-based covariance estimates using FF-1, FF-3, and FF-5 models. All benchmark covariance matrices are estimated using rolling windows of three years of daily return data.

Portfolio performance is evaluated using multiple criteria, including annualized excess return, annualized volatility, Sharpe ratio, maximum drawdown, and turnover. Turnover is computed as given in Gu et al. ([2020](https://arxiv.org/html/2601.17773v1#bib.bib29 "Empirical asset pricing via machine learning")),

|  |  |  |
| --- | --- | --- |
|  | Turnover=1T​∑t=1T(∑i|wi,t+1−wi,t​(1+ri,t+1)1+∑jwj,t​rj,t+1|).\mathrm{Turnover}=\frac{1}{T}\sum\_{t=1}^{T}\left(\sum\_{i}\left|w\_{i,t+1}-\frac{w\_{i,t}(1+r\_{i,t+1})}{1+\sum\_{j}w\_{j,t}r\_{j,t+1}}\right|\right). |  |

It captures the extent of portfolio rebalancing required by each approach. While transaction costs are not explicitly incorporated into the optimization problem, we later assess the robustness of performance to plausible levels of trading costs.

MarketGAN models are trained using a rolling window procedure designed to reflect evolving market conditions. Initially, we train the models using data from the in-sample period spanning January 1, 1991, to December 31, 2015, splitting this interval into training and validation subsets with a 7:1 ratio as described in Section [4.1](https://arxiv.org/html/2601.17773v1#S4.SS1 "4.1 Data and Experimental Setup ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"). The trained model parameters are then updated quarterly by rolling the estimation window forward. Each rolling update maintains the same 7:1 training-to-validation ratio and uses the previously trained model parameters as initialization. Given the pre-trained initialization, we train MarketGANs for only 50 epochs per rolling window and apply an early stopping criterion based on the Frobenius norm between correlation matrices computed from synthetic and real validation data. To mitigate the exclusion of the most recent observations from direct training, we perform a brief fine-tuning step using the validation data with a reduced learning rate.141414Training stops if no improvement is observed over 20 consecutive epochs, and the best-performing parameters are retained. However, this splitting strategy has a limitation: the most recent data in each window are used only for validation and are not included in the training set, so they are not directly fed into the model.
Since the purpose of rolling training is to adapt to evolving market conditions, excluding the most recent data from direct training may reduce the model’s responsiveness. To address this issue, we fine-tune the trained models on the validation data for an additional 10 epochs, with the learning rate reduced to one-tenth of the original.

### 5.2 Results

We now present portfolio optimization results and explicitly compare MarketGAN-based portfolios with a comprehensive set of benchmark portfolios. The objective is to assess whether synthetic data generated by MarketGAN provides incremental economic value relative to both traditional covariance estimators and factor-model-based bootstrap methods.

We begin by summarizing the performance of benchmark portfolios under daily rebalancing. Table [3](https://arxiv.org/html/2601.17773v1#S5.T3 "Table 3 ‣ 5.2 Results ‣ 5 Applications: Portfolio Optimization ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") reports annualized excess returns, volatility, Sharpe ratios, maximum drawdown, and turnover for the benchmark strategies. Portfolios constructed using factor-model-based covariance estimators achieve particularly strong performance, with Sharpe ratios close to or slightly above one. This strong performance reflects the favorable market conditions during the out-of-sample period and confirms that well-specified factor models already provide a competitive baseline for portfolio construction.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | Factors | SR | Return | Std | MDD | Turnover |
| Market Portfolio | - | 0.6613 | 0.1265 | 0.1913 | −0.3437-0.3437 | - |
| Sample-estimate covariance | - | 0.9034 | 0.1911 | 0.2116 | −0.3538-0.3538 | 1.5748 |
| Ledoit-Wolf Shrinkage covariance | - | 0.9119 | 0.1932 | 0.2118 | −0.3551-0.3551 | 1.5656 |
| Factor-model-based covariance | 1 | 0.9838 | 0.1750 | 0.1779 | −0.2407-0.2407 | 1.5069 |
| 3 | 1.0183 | 0.1937 | 0.1902 | −0.2702-0.2702 | 1.6642 |
| 5 | 0.9975 | 0.1875 | 0.1880 | −0.2698-0.2698 | 1.6458 |

Table 3: Performance of benchmark portfolios under daily rebalancing frequency.
The table compares portfolios based on different covariance matrix estimation methods including the sample-estimate covariance, Ledoit–Wolf shrinkage, and factor-model-based covariance using 1, 3, and 5 factors.
SR, Return, Std, MDD and Turnover indicate the Sharpe ratio, annualized excess return, annualized standard deviation, maximum drawdown, and monthly turnover.

In comparison, portfolios based on the sample covariance matrix and Ledoit–Wolf shrinkage perform slightly worse but remain economically meaningful. These results imply that synthetic-data-based approaches should be evaluated relative to covariance estimation methods that already exhibit strong out-of-sample performance, rather than against weak or ad hoc benchmarks.

We next examine portfolios constructed from synthetic returns, 𝒓t+1\boldsymbol{r}\_{t+1}, generated by MarketGAN and factor-model-based bootstrap methods, with future factor realizations forecast, 𝑭t+1\boldsymbol{F}\_{t+1}, using standard time-series techniques. Two forecasting methods are considered: a one-year rolling average and a VAR. The resulting portfolio performance is reported in Tables [4](https://arxiv.org/html/2601.17773v1#S5.T4 "Table 4 ‣ 5.2 Results ‣ 5 Applications: Portfolio Optimization ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") and [5](https://arxiv.org/html/2601.17773v1#S5.T5 "Table 5 ‣ 5.2 Results ‣ 5 Applications: Portfolio Optimization ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"), respectively.

| Model | Factors | SR | Return | Std | MDD | Turnover |
| --- | --- | --- | --- | --- | --- | --- |
| MarketGAN | 1 | 0.7406 | 0.1357 | 0.1832 | −0.3555-0.3555 | 5.2746 |
| 3 | 0.8952 | 0.1593 | 0.1780 | −0.3312-0.3312 | 4.9584 |
| 5 | 0.8360 | 0.1426 | 0.1706 | −0.3084-0.3084 | 4.1749 |
| Factor-model-based  bootstrap | 1 | 0.8044 | 0.1399 | 0.1739 | −0.3080-0.3080 | 4.7030 |
| 3 | 0.8194 | 0.1444 | 0.1763 | −0.3091-0.3091 | 4.5435 |
| 5 | 0.8174 | 0.1449 | 0.1772 | −0.3040-0.3040 | 4.5067 |

Table 4: Performance of long-only mean-variance portfolios using synthetic sample covariance matrices, with factors 𝑭t+1\boldsymbol{F}\_{t+1} predicted via 1-year rolling averages. SR, Return, Std, MDD, and Turnover indicate the Sharpe ratio, annualized excess return, annualized standard deviation, maximum drawdown, and monthly turnover.



| Model | Factors | SR | Return | Std | MDD | Turnover |
| --- | --- | --- | --- | --- | --- | --- |
| MarketGAN | 1 | 1.0610 | 0.2110 | 0.1989 | −0.3223-0.3223 | 13.4172 |
| 3 | 0.6849 | 0.1444 | 0.2109 | −0.4108-0.4108 | 17.5554 |
| 5 | 0.6428 | 0.1388 | 0.2159 | −0.3953-0.3953 | 18.0836 |
| Factor-model-based  bootstrap | 1 | 0.8588 | 0.1979 | 0.2304 | −0.4189-0.4189 | 12.8247 |
| 3 | 0.6328 | 0.1481 | 0.2340 | −0.4506-0.4506 | 16.5555 |
| 5 | 0.8109 | 0.1926 | 0.2375 | −0.4528-0.4528 | 17.9810 |

Table 5: Performance of mean-variance portfolios using synthetic sample covariance matrices, with factors 𝑭t+1\boldsymbol{F}\_{t+1} predicted via a VAR model. SR, Return, Std, MDD, and Turnover indicate the Sharpe ratio, annualized excess return, annualized standard deviation, maximum drawdown, and monthly turnover.

Across both forecasting approaches, MarketGAN-based portfolios modestly outperform their corresponding bootstrap counterparts in some cases, but their performance is not consistently superior to that of benchmark portfolios based on traditional covariance estimators or factor-model-based covariance estimates. In particular, Sharpe ratios achieved by MarketGAN-based portfolios under forecasted factors remain comparable to, but not markedly higher than, those of the best-performing benchmark portfolios. These results imply that when factor forecasts are imprecise, improvements in modeling return distributions alone are insufficient to generate large economic gains. In such settings, factor predictability becomes the primary bottleneck, and even sophisticated generative models cannot fully compensate for inaccurate inputs.

A key insight underlying these results is that independent resampling errors propagate nonlinearly through the optimization process. Factor-model-based bootstrap methods generate synthetic returns by resampling idiosyncratic components independently across assets, implicitly assuming that residual dependence is either negligible or sufficiently captured by the factor structure. While this assumption may appear innocuous at the level of marginal distributions or covariance estimation, it becomes consequential once synthetic data are used as inputs to nonlinear decision problems such as portfolio optimization. Mean–variance portfolio choice is a nonlinear mapping from the joint return distribution to optimal allocations, and small distortions in dependence structures—particularly in low-variance directions or in the tails—can be amplified through covariance inversion and constraint interactions. This mechanism motivates the perturbed forecast simulation design that follows, which isolates the value of accurately modeling joint dependence independently of factor predictability.

To isolate the contribution of synthetic data generation from factor forecasting accuracy, we conduct a perturbed forecast simulation. Instead of relying on a specific factor forecasting model, we analyze the economic value of the generated joint distributions across a spectrum of factor information quality. This is achieved by taking the realized future factors 𝑭t+1\boldsymbol{F}\_{t+1} and injecting controlled levels of Gaussian noise 𝜼t+1\boldsymbol{\eta}\_{t+1} to simulate varying degrees of predictive reliability. Specifically, we construct noisy predictors 𝑭~t+1=𝑭t+1+𝜼t+1\tilde{\boldsymbol{F}}\_{t+1}=\boldsymbol{F}\_{t+1}+\boldsymbol{\eta}\_{t+1}, where the noise variance is calibrated to yield targeted predictive R2R^{2} levels: 100% (i.e., without any perturbation), 50%, 10%, 1%, and 0.1%. Given these simulated factor realizations, we generate the NN-dimensional asset returns through the generative models and utilize them to construct portfolios. This simulation experiment enables us to assess the fidelity with which MarketGAN replicates high-dimensional dependence structures, independent of the inherent difficulty in forecasting the underlying factors.

The results, summarized in Table [6](https://arxiv.org/html/2601.17773v1#S5.T6 "Table 6 ‣ 5.2 Results ‣ 5 Applications: Portfolio Optimization ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"), reveal a sharp contrast between MarketGAN-based portfolios and both bootstrap-based portfolios and traditional benchmarks. When factor information is highly informative, MarketGAN3 and MarketGAN5 achieve exceptionally high Sharpe ratios, substantially exceeding those of all benchmark portfolios. In particular, under ideal predictive conditions (R2=100%R^{2}=100\%), mean-variance portfolio Sharpe ratios approach values around 5. Notably, even at low predictive accuracies for future factors (e.g., R2=0.1%R^{2}=0.1\%), MarketGAN3 and MarketGAN5 achieve Sharpe ratios exceeding 3.3 and outperform their corresponding bootstrap counterparts by margins greater than 1. Their results also substantially surpass those of MarketGAN1, which delivers less pronounced improvements while still outperforming its corresponding bootstrap method. In contrast, bootstrap portfolios experience a pronounced deterioration in performance as factor predictability declines. This divergence underscores the importance of accurately modeling cross-sectional dependence structures, which MarketGAN captures through joint generation of asset returns. This superior performance can be attributable to the capability of MarketGAN3 and MarketGAN5 to accurately capture cross-sectional correlation structures as previously demonstrated in Table [2](https://arxiv.org/html/2601.17773v1#S4.T2 "Table 2 ‣ 4.5 Quantitative Evaluation Metrics ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

The superior performance of MarketGAN-based portfolios, particularly under perturbed factor simulations, is accompanied by higher turnover due to daily rebalancing. To assess economic robustness, we evaluate performance under plausible assumptions with a transaction cost of 10 basis points and a monthly turnover of 3,400%. Even after accounting for these assumptions, MarketGAN3 and MarketGAN5 retain economically meaningful Sharpe ratios and positive excess returns across a wide range of factor predictability levels. For example, even at a low predictive accuracy R2=0.1%R^{2}=0.1\%, the annualized returns net of transaction costs are 38.74% and 35.80%, respectively, with Sharpe ratios of 1.62 in both cases. Importantly, benchmark portfolios with lower turnover do not exhibit comparable robustness when factor information is noisy. This suggests that the gains from MarketGAN are not solely artifacts of aggressive trading, but reflect genuine improvements in covariance estimation driven by higher-fidelity synthetic data.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R2R^{2} | Model | Factors | Sharpe Ratio | Annualized Return | Annualized Std | MDD | Turnover |
| 100%100\% | MarketGAN | 1 | 2.4339 | 0.5739 | 0.2358 | −0.3310-0.3310 | 28.0504 |
| 3 | 5.3444 | 1.1332 | 0.2120 | −0.2570-0.2570 | 31.9897 |
| 5 | 4.9003 | 1.0748 | 0.2193 | −0.2402-0.2402 | 32.3922 |
| Factor-model-based  bootstrap | 1 | −0.2663-0.2663 | −0.0905-0.0905 | 0.3399 | −0.7172-0.7172 | 26.7663 |
| 3 | 2.1898 | 0.6241 | 0.2850 | −0.3763-0.3763 | 27.9007 |
| 5 | 3.3567 | 0.8860 | 0.2639 | −0.3584-0.3584 | 27.9944 |
| 50%50\% | MarketGAN | 1 | 2.0380 | 0.4853 | 0.2381 | −0.3262-0.3262 | 28.4286 |
| 3 | 3.9247 | 0.9073 | 0.2312 | −0.2766-0.2766 | 33.3657 |
| 5 | 3.5286 | 0.7978 | 0.2261 | −0.2087-0.2087 | 33.6198 |
| Factor-model-based  bootstrap | 1 | 0.1598 | 0.0600 | 0.3753 | −0.4712-0.4712 | 26.1087 |
| 3 | 2.1049 | 0.6413 | 0.3047 | −0.4238-0.4238 | 28.8547 |
| 5 | 2.4166 | 0.6858 | 0.2838 | −0.4113-0.4113 | 28.5285 |
| 10%10\% | MarketGAN | 1 | 2.0055 | 0.4758 | 0.2372 | −0.3267-0.3267 | 28.6623 |
| 3 | 3.3418 | 0.7978 | 0.2387 | −0.3222-0.3222 | 33.7781 |
| 5 | 3.5675 | 0.7844 | 0.2199 | −0.2666-0.2666 | 33.9254 |
| Factor-model-based  bootstrap | 1 | 0.5258 | 0.1986 | 0.3777 | −0.4712-0.4712 | 25.7059 |
| 3 | 1.8999 | 0.6037 | 0.3178 | −0.4705-0.4705 | 29.1764 |
| 5 | 2.4771 | 0.6706 | 0.2707 | −0.4174-0.4174 | 28.6850 |
| 1%1\% | MarketGAN | 1 | 2.0284 | 0.4829 | 0.2381 | −0.3267-0.3267 | 28.6691 |
| 3 | 3.3033 | 0.7880 | 0.2386 | −0.3148-0.3148 | 33.8637 |
| 5 | 3.4772 | 0.7668 | 0.2205 | −0.2673-0.2673 | 33.9707 |
| Factor-model-based  bootstrap | 1 | 0.5201 | 0.1968 | 0.3785 | −0.4712-0.4712 | 25.6837 |
| 3 | 2.0226 | 0.6345 | 0.3137 | −0.4704-0.4704 | 29.1606 |
| 5 | 2.4797 | 0.6722 | 0.2711 | −0.4197-0.4197 | 28.6375 |
| 0.1%0.1\% | MarketGAN | 1 | 2.0334 | 0.4844 | 0.2382 | −0.3267-0.3267 | 28.7304 |
| 3 | 3.3312 | 0.7954 | 0.2388 | −0.3148-0.3148 | 33.8667 |
| 5 | 3.4729 | 0.7660 | 0.2206 | −0.2673-0.2673 | 33.9751 |
| Factor-model-based  bootstrap | 1 | 0.5287 | 0.1996 | 0.3774 | −0.4712-0.4712 | 25.7047 |
| 3 | 2.0253 | 0.6358 | 0.3139 | −0.4704-0.4704 | 29.1663 |
| 5 | 2.4513 | 0.6659 | 0.2716 | −0.4199-0.4199 | 28.6864 |

Table 6: Performance of long-only mean-variance portfolios using synthetic sample covariance matrices under various levels of predictive R2R^{2} for future factors 𝑭t+1\boldsymbol{F}\_{t+1}. SR, Return, Std, MDD, and Turnover indicate the Sharpe ratio, annualized excess return, annualized standard deviation, maximum drawdown, and monthly turnover.

In sum, when future factor realizations are poorly predicted, portfolio performance is largely constrained by factor predictability, and even sophisticated generative models cannot fully overcome this limitation. However, once factor information is even weakly informative, MarketGAN consistently achieves superior portfolio outcomes relative to factor-model-based bootstrap methods, while remaining competitive with strong covariance-based benchmarks. Crucially, these gains do not arise from improved factor forecasting or from marginal distributional accuracy alone. Instead, they stem from MarketGAN’s ability to generate coherent high-dimensional return distributions that preserve cross-sectional dependence and tail co-movement across assets. Traditional covariance estimators and bootstrap methods, while effective in estimating second moments, are inherently limited in capturing complex joint dependence structures in high-dimensional settings. By generating returns as a single joint vector and learning dependence patterns directly from the data, MarketGAN provides an additional layer of information that is particularly valuable for portfolio construction. These findings suggest that synthetic data-based approaches should be evaluated not only by their marginal or low-dimensional performance, but also by their capacity to generate economically meaningful high-dimensional structures. In this sense, MarketGAN complements existing covariance estimation techniques by extending their applicability to settings where accurate modeling of joint return distributions is essential for economic decision-making.

## 6 Conclusion

This paper proposes MarketGAN, a factor-based generative framework for high-dimensional asset return generation under severe data scarcity. MarketGAN reframes the problem from point prediction to distributional learning, embedding a standard factor structure as an economic inductive bias while using conditional generative models with a temporal convolutional backbone to generate stochastic, time-varying factor loadings and idiosyncratic risks. By generating returns as a single joint vector, the framework is designed to learn and preserve cross-sectional dependence patterns that are central to portfolio analysis and risk management.

Empirically, using daily excess returns of 98 large U.S. equities from the S&P 100 universe, we evaluate MarketGAN against transparent factor-model-based bootstrap baselines across one-, three-, and five-factor specifications. MarketGAN-generated data more closely match empirical marginal distributions. particularly in higher-order moments, while reproducing key inter-temporal stylized facts such as linear unpredictability, volatility clustering, and leverage effects. The most pronounced improvements arise in cross-sectional dependence, where MarketGAN more accurately replicates asset-level correlation structures, including dependence in extreme returns, as reflected in standard quantitative distributional metrics.

We further assess economic value through mean–variance portfolio optimization using MarketGAN-generated samples. Rather than relying on a specific factor forecasting model, we isolate the role of distributional fidelity through perturbed forecast simulations. In this setting, covariance matrices estimated from MarketGAN-generated data lead to substantially improved portfolio performance relative to bootstrap-based approaches, even when factor information is only weakly informative. These results indicate that the gains do not arise from improved forecasts or marginal accuracy alone, but from preserving joint dependence structures that are amplified through optimization.

From a broader decision-systems perspective, our findings underscore that the primary value of synthetic data lies in its role as input to downstream decision problems. In high-dimensional environments with limited and noisy data, decisions depend on nonlinear mappings of uncertainty, leading to small misspecifications in dependence being magnified. MarketGAN addresses this challenge by combining structural domain knowledge with generative distribution learning to produce joint uncertainty representations that remain informative under weak identification. While we illustrate the framework using financial portfolios, the underlying problem of learning and extending high-dimensional joint distributions for optimization and control under data scarcity is ubiquitous across operations, risk management, and data-driven decision systems. Viewed through this lens, generative models such as MarketGAN act as structural regularizers for decision-making, offering a principled approach to improving decision quality when historical data alone are insufficient.

## Acknowledgement

This work is also supported by the National Research Foundation of Korea(NRF) grant funded by the Korea government(MSIT) (RS-2025-00513038).

## Declaration of competing interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## References

* A. Ang and J. Chen (2007)
  CAPM over the long run: 1926–2001.
  Journal of Empirical Finance 14 (1),  pp. 1–40.
  Cited by: [§3.2](https://arxiv.org/html/2601.17773v1#S3.SS2.p5.1 "3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 4](https://arxiv.org/html/2601.17773v1#footnote4 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* M. Arjovsky, S. Chintala, and L. Bottou (2017)
  Wasserstein generative adversarial networks.
  In International conference on machine learning,
   pp. 214–223.
  Cited by: [§A.1](https://arxiv.org/html/2601.17773v1#A1.SS1.p3.1 "A.1 Generative Adversarial Networks ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p7.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§2.1](https://arxiv.org/html/2601.17773v1#S2.SS1.p3.1 "2.1 Generative Adversarial Networks (GANs) ‣ 2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* C. S. Armstrong, S. Banerjee, and C. Corona (2013)
  Factor-loading uncertainty and expected returns.
  The Review of Financial Studies 26 (1),  pp. 158–207.
  Cited by: [§3.2](https://arxiv.org/html/2601.17773v1#S3.SS2.p5.1 "3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Bai, J. Z. Kolter, and V. Koltun (2018)
  An empirical evaluation of generic convolutional and recurrent networks for sequence modeling.
  arXiv preprint arXiv:1803.01271.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p7.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§2.2](https://arxiv.org/html/2601.17773v1#S2.SS2.p1.1 "2.2 Temporal Convolutional Networks (TCNs) ‣ 2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 3](https://arxiv.org/html/2601.17773v1#footnote3 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* A. Boloorforoosh, P. Christoffersen, M. Fournier, and C. Gouriéroux (2020)
  Beta risk in the cross-section of equities.
  The Review of Financial Studies 33 (9),  pp. 4318–4366.
  Cited by: [§3.2](https://arxiv.org/html/2601.17773v1#S3.SS2.p5.1 "3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* N. Bonneel, J. Rabin, G. Peyré, and H. Pfister (2015)
  Sliced and radon wasserstein barycenters of measures.
  Journal of Mathematical Imaging and Vision 51,  pp. 22–45.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p8.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 12](https://arxiv.org/html/2601.17773v1#footnote12 "In 4.5 Quantitative Evaluation Metrics ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Bryzgalova, S. Lerner, M. Lettau, and M. Pelger (2025a)
  Missing financial data.
  The Review of Financial Studies 38 (),  pp. 803–882.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p15.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p4.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Bryzgalova, M. Pelger, and J. Zhu (2025b)
  Forest through the trees: building cross-sections of stock returns.
  Journal of Finance 80 (5),  pp. 2447–2506.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p15.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p4.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* H. Buehler, B. Horvath, T. Lyons, I. P. Arribas, and B. Wood (2020)
  A data-driven market simulator for small data environments.
  arXiv preprint arXiv:2006.14498.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p3.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* G. Chamberlain (1982)
  Multivariate regression models for panel data.
  Journal of Econometrics 18 (1),  pp. 5–46.
  Cited by: [§3.2](https://arxiv.org/html/2601.17773v1#S3.SS2.p5.1 "3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 4](https://arxiv.org/html/2601.17773v1#footnote4 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* A. Y. Chen and J. McCoy (2024)
  Missing values handling for machine learning portfolios.
  Journal of Financial Economics 155 (),  pp. 103815.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p15.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p4.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* L. Chen, M. Pelger, and J. Zhu (2024)
  Deep learning in asset pricing.
  Management Science 70 (2),  pp. 714–750.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p11.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Cho, J. Kim, K. Ban, H. K. Koo, and H. Kim (2025)
  Diffolio: A Diffusion Model for Multivariate Probabilistic Financial Time-Series Forecasting and Portfolio Construction.
  arXiv preprint arXiv:2511.07014.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p13.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* R. Cont, M. Cucuringu, R. Xu, and C. Zhang (2022)
  Tail-gan: Learning to simulate tail risk scenarios.
  arXiv preprint arXiv:2203.01664.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p12.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§4.2](https://arxiv.org/html/2601.17773v1#S4.SS2.p1.1 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative Finance 1 (2),  pp. 223.
  Cited by: [§4.2](https://arxiv.org/html/2601.17773v1#S4.SS2.p4.1 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* T. Dangl and M. Halling (2012)
  Predictive regressions with time-varying coefficients.
  Journal of Financial Economics 106 (1),  pp. 157–181.
  Cited by: [§3.2](https://arxiv.org/html/2601.17773v1#S3.SS2.p5.1 "3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* R. De Maesschalck, D. Jouan-Rimbaud, and D. L. Massart (2000)
  The mahalanobis distance.
  Chemometrics and intelligent laboratory systems 50 (1),  pp. 1–18.
  Cited by: [footnote 12](https://arxiv.org/html/2601.17773v1#footnote12 "In 4.5 Quantitative Evaluation Metrics ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* Y. Duan, L. Wang, Q. Zhang, and J. Li (2022)
  Factorvae: A probabilistic dynamic factor model based on variational autoencoder for predicting cross-sectional stock returns.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  Vol. 36,  pp. 4468–4476.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p13.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* J. L. Elman (1990)
  Finding structure in time.
  Cognitive science 14 (2),  pp. 179–211.
  Cited by: [footnote 3](https://arxiv.org/html/2601.17773v1#footnote3 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* F. J. Fabozzi and J. C. Francis (1978)
  Beta as a random coefficient.
  Journal of Financial and Quantitative Analysis 13 (1),  pp. 101–116.
  Cited by: [§3.2](https://arxiv.org/html/2601.17773v1#S3.SS2.p5.1 "3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 4](https://arxiv.org/html/2601.17773v1#footnote4 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* E. F. Fama and K. R. French (1993)
  Common risk factors in the returns on stocks and bonds.
  Journal of Financial Economics 33 (1),  pp. 3–56.
  Cited by: [§4.2](https://arxiv.org/html/2601.17773v1#S4.SS2.p3.1 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 7](https://arxiv.org/html/2601.17773v1#footnote7 "In 4.1 Data and Experimental Setup ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* E. F. Fama and K. R. French (2015)
  A five-factor asset pricing model.
  Journal of Financial Economics 116 (1),  pp. 1–22.
  Cited by: [§4.2](https://arxiv.org/html/2601.17773v1#S4.SS2.p3.1 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 7](https://arxiv.org/html/2601.17773v1#footnote7 "In 4.1 Data and Experimental Setup ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* J. Freyberger, B. Hoeppner, A. Neuhierl, and M. Weber (2025)
  Missing data in asset pricing panels.
  The Review of Financial Studies 38 (),  pp. 760–802.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p15.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p4.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* I. Goodfellow, Y. Bengio, A. Courville, and Y. Bengio (2016)
  Deep learning.
  Vol. 1, MIT press Cambridge.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p2.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio (2014)
  Generative adversarial nets.
  Advances in neural information processing systems 27.
  Cited by: [§A.1](https://arxiv.org/html/2601.17773v1#A1.SS1.p1.9 "A.1 Generative Adversarial Networks ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§2.1](https://arxiv.org/html/2601.17773v1#S2.SS1.p1.6 "2.1 Generative Adversarial Networks (GANs) ‣ 2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Gu, B. Kelly, and D. Xiu (2020)
  Empirical asset pricing via machine learning.
  The Review of Financial Studies 33 (5),  pp. 2223–2273.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p11.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§4.1](https://arxiv.org/html/2601.17773v1#S4.SS1.p1.1 "4.1 Data and Experimental Setup ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§5.1](https://arxiv.org/html/2601.17773v1#S5.SS1.p4.1 "5.1 Portfolio Construction and Experimental Design ‣ 5 Applications: Portfolio Optimization ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Gu, B. Kelly, and D. Xiu (2021)
  Autoencoder asset pricing models.
  Journal of Econometrics 222 (1),  pp. 429–450.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p11.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. C. Courville (2017)
  Improved training of wasserstein gans.
  Advances in Neural Information Processing Systems 30.
  Cited by: [§A.1](https://arxiv.org/html/2601.17773v1#A1.SS1.p3.1 "A.1 Generative Adversarial Networks ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§A.1](https://arxiv.org/html/2601.17773v1#A1.SS1.p5.3 "A.1 Generative Adversarial Networks ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p7.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§2.1](https://arxiv.org/html/2601.17773v1#S2.SS1.p3.1 "2.1 Generative Adversarial Networks (GANs) ‣ 2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter (2017)
  Gans trained by a two time-scale update rule converge to a local nash equilibrium.
  Advances in neural information processing systems 30.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p8.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 12](https://arxiv.org/html/2601.17773v1#footnote12 "In 4.5 Quantitative Evaluation Metrics ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* B. Horvath, J. Plenk, and M. Vuletić (2026)
  Market generators: a paradigm shift in financial modeling.
  In Signature Methods in Finance: An Introduction with Computational Applications, C. Bayer, G. dos Reis, B. Horvath, and H. Oberhauser (Eds.),
   pp. 127–159.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p4.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* G. Jostova and A. Philipov (2005)
  Bayesian analysis of stochastic betas.
  Journal of Financial and Quantitative Analysis 40 (4),  pp. 747–778.
  Cited by: [§3.2](https://arxiv.org/html/2601.17773v1#S3.SS2.p5.1 "3.2 MarketGAN as a Data Generator and a Stochastic Coefficient Factor Model ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* O. Ledoit and M. Wolf (2004)
  A well-conditioned estimator for large-dimensional covariance matrices.
  Journal of multivariate analysis 88 (2),  pp. 365–411.
  Cited by: [§5.1](https://arxiv.org/html/2601.17773v1#S5.SS1.p3.1 "5.1 Portfolio Construction and Experimental Design ‣ 5 Applications: Portfolio Optimization ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Liao, H. Ni, L. Szpruch, M. Wiese, M. Sabate-Vidales, and B. Xiao (2020)
  Conditional sig-wasserstein gans for time series generation.
  arXiv preprint arXiv:2006.05421.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p12.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* B. Mandelbrot (1963)
  The variation of certain speculative prices.
  The Journal of Business 36 (4),  pp. 394–419.
  Cited by: [§4.2](https://arxiv.org/html/2601.17773v1#S4.SS2.p4.1 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* L. Martellini and V. Ziemann (2010)
  Improved estimates of higher-order comoments and implications for portfolio selection.
  The Review of Financial Studies 23 (4),  pp. 1467–1502.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p1.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 2](https://arxiv.org/html/2601.17773v1#footnote2 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* M. Mirza and S. Osindero (2014)
  Conditional generative adversarial nets.
  arXiv preprint arXiv:1411.1784.
  Cited by: [§A.1](https://arxiv.org/html/2601.17773v1#A1.SS1.p2.2 "A.1 Generative Adversarial Networks ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* O. Mogren (2016)
  C-rnn-gan: continuous recurrent neural networks with adversarial training.
  arXiv preprint arXiv:1611.09904.
  Cited by: [§A.3](https://arxiv.org/html/2601.17773v1#A1.SS3.p1.1 "A.3 GAN with TCN Backbones ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* M. Müller (2007)
  Dynamic time warping.
  Information retrieval for music and motion,  pp. 69–84.
  Cited by: [footnote 12](https://arxiv.org/html/2601.17773v1#footnote12 "In 4.5 Quantitative Evaluation Metrics ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* A. v. d. Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu (2016)
  Wavenet: A generative model for raw audio.
  arXiv preprint arXiv:1609.03499.
  Cited by: [footnote 3](https://arxiv.org/html/2601.17773v1#footnote3 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* A. Radford, L. Metz, and S. Chintala (2015)
  Unsupervised representation learning with deep convolutional generative adversarial networks.
  arXiv preprint arXiv:1511.06434.
  Cited by: [§A.3](https://arxiv.org/html/2601.17773v1#A1.SS3.p1.1 "A.3 GAN with TCN Backbones ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* A. M. Reppen, H. M. Soner, and V. Tissot-Daguette (2023)
  Deep stochastic optimization in finance.
  Digital Finance 5 (),  pp. 91–111.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p2.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* A. M. Reppen and H. M. Soner (2023)
  Deep empirical risk minimization in finance: looking into the future.
  Mathematical Finance 33 (1),  pp. 116–145.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p2.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* M. Rizzato, J. Wallart, C. Geissler, N. Morizet, and N. Boumlaik (2023)
  Generative adversarial networks applied to synthetic financial scenarios generation.
  Physica A: Statistical Mechanics and its Applications 623,  pp. 128899.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p12.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* S. Takahashi, Y. Chen, and K. Tanaka-Ishii (2019)
  Modeling financial time-series with generative adversarial networks.
  Physica A: Statistical Mechanics and its Applications 527,  pp. 121261.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p12.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p3.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§4.2](https://arxiv.org/html/2601.17773v1#S4.SS2.p1.1 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* R. Tepelyan and A. Gopal (2023)
  Generative machine learning for multivariate equity returns.
  In Proceedings of the Fourth ACM International Conference on AI in Finance,
   pp. 159–166.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p13.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017)
  Attention is all you need.
  Advances in neural information processing systems 30.
  Cited by: [footnote 3](https://arxiv.org/html/2601.17773v1#footnote3 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* J. Wang and Z. Chen (2024)
  Factor-gan: enhancing stock price prediction and factor investment with generative adversarial networks.
  Plos one 19 (6),  pp. e0306094.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p13.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* T. Wang, M. Liu, J. Zhu, A. Tao, J. Kautz, and B. Catanzaro (2018)
  High-resolution image synthesis and semantic manipulation with conditional gans.
  In Proceedings of the IEEE conference on computer vision and pattern recognition,
   pp. 8798–8807.
  Cited by: [§A.3](https://arxiv.org/html/2601.17773v1#A1.SS3.p1.1 "A.3 GAN with TCN Backbones ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* L. Wei, S. Chen, J. Lin, and L. Shi (2025)
  Enhancing return forecasting using lstm with agent-based synthetic data.
  Decision Support Systems 193 (),  pp. 114452.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p4.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* I. Welch and A. Goyal (2008)
  A comprehensive look at the empirical performance of equity premium prediction.
  The Review of Financial Studies 21 (4),  pp. 1455–1508.
  Cited by: [§4.1](https://arxiv.org/html/2601.17773v1#S4.SS1.p1.1 "4.1 Data and Experimental Setup ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* M. Wiese, R. Knobloch, R. Korn, and P. Kretschmer (2020)
  Quant GANs: deep generation of financial time series.
  Quantitative Finance 20 (9),  pp. 1419–1440.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p12.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§1](https://arxiv.org/html/2601.17773v1#S1.p3.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§2.2](https://arxiv.org/html/2601.17773v1#S2.SS2.p3.1 "2.2 Temporal Convolutional Networks (TCNs) ‣ 2 Methodological Background ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [§4.2](https://arxiv.org/html/2601.17773v1#S4.SS2.p1.1 "4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"),
  [footnote 3](https://arxiv.org/html/2601.17773v1#footnote3 "In 1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* J. Yoon, D. Jarrett, and M. Van der Schaar (2019)
  Time-series generative adversarial networks.
  Advances in neural information processing systems 32.
  Cited by: [§1](https://arxiv.org/html/2601.17773v1#S1.p12.1 "1 Introduction ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").
* H. Zhang, I. Goodfellow, D. Metaxas, and A. Odena (2019)
  Self-attention generative adversarial networks.
  In International conference on machine learning,
   pp. 7354–7363.
  Cited by: [§A.3](https://arxiv.org/html/2601.17773v1#A1.SS3.p1.1 "A.3 GAN with TCN Backbones ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

Online Appendix for “MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks”

## Appendix A Formal Introductions of GAN and TCN Models

### A.1 Generative Adversarial Networks

GANs (Goodfellow et al., [2014](https://arxiv.org/html/2601.17773v1#bib.bib10 "Generative adversarial nets")) are neural networks designed to generate synthetic samples analogously distributed to the target data samples.
GANs implicitly estimate complex target distributions through an adversarial training framework involving two distinct neural network components: a generator and a discriminator.
Formally, the GAN framework aims to model an unknown data distribution pd​a​t​a​(x)p\_{data}(x) based on a given set of samples {xi}i=1n\{x\_{i}\}\_{i=1}^{n}, where xix\_{i} represents observed data such as handwritten digits, human face images, or asset returns.
The generator GG takes as input a random noise vector z∼pz​(z)z\sim p\_{z}(z) drawn from a simple prior distribution (e.g. Gaussian) and outputs synthetic samples G​(z)G(z) that resemble the real data.
The discriminator DD, on the other hand, acts as a binary classifier that assesses whether an input sample originates from the real data distribution or from the generator’s synthetic data distribution.
Specifically, the discriminator is designed to output values in the interval [0,1][0,1], and it is trained to output 1 for real samples and 0 for generated samples. To this end, a sigmoid activation function is typically applied at the output layer of DD.
These two neural networks compete against each other in a minimax game described by the following objective function:

|  |  |  |
| --- | --- | --- |
|  | minG⁡maxD⁡V​(D,G)=𝔼x∼pd​a​t​a​(x)​[log⁡D​(x)]+𝔼z∼pz​(z)​[log⁡(1−D​(G​(z)))].\min\_{G}\max\_{D}V(D,G)=\mathbb{E}\_{x\sim p\_{data}(x)}\left[\log D\left(x\right)\right]+\mathbb{E}\_{z\sim p\_{z}(z)}\left[\log\left(1-D\left(G(z)\right)\right)\right]. |  |

In this adversarial game, the discriminator DD seeks to maximize its ability to distinguish between real and synthetic samples by estimating the divergence between the two distributions.
Simultaneously, the generator GG is trained to minimize this discrepancy and thereby generate increasingly realistic synthetic samples.
This training process continues until convergence is achieved; i.e., the generator successfully captures the true data distribution pd​a​t​a​(x)p\_{data}(x), and the discriminator can no longer distinguish real from synthetic samples.
When the discriminator is optimal, the minimization of this objective corresponds to minimizing the Jensen-Shannon divergence between the real and generated distributions:

|  |  |  |
| --- | --- | --- |
|  | J​S​D​(pd​a​t​a,qG)=12​DK​L​(pd​a​t​a∥M)+12​DK​L​(qG∥M),JSD(p\_{data},q\_{G})=\frac{1}{2}D\_{KL}\left(p\_{data}\|M\right)+\frac{1}{2}D\_{KL}\left(q\_{G}\|M\right), |  |

where qGq\_{G} denotes the model distribution induced by the generator, and M=12​(pd​a​t​a+qG)M=\frac{1}{2}\left(p\_{data}+q\_{G}\right) and DK​LD\_{KL} is the Kullback-Leibler divergence.
In essence, the generator is trained to approximate the real data distribution pd​a​t​ap\_{data}.

When the goal is to generate data conditioned on auxiliary information (e.g., class labels or macroeconomic indicators), conditional GANs (Mirza and Osindero, [2014](https://arxiv.org/html/2601.17773v1#bib.bib31 "Conditional generative adversarial nets")) can be employed.
In this setting, both the generator and discriminator take the conditioning variable yy as an additional input.
The generator is trained to learn the conditional distribution of the data given yy, and the discriminator is trained to distinguish real from synthetic data conditioned on the same information.
The resulting objective function becomes:

|  |  |  |
| --- | --- | --- |
|  | minG⁡maxD⁡V​(D,G)=𝔼x∼pd​a​t​a​(x|y),y∼py​(y)​[log⁡D​(x;y)]+𝔼z∼pz​(z),y∼py​(y)​[log⁡(1−D​(G​(z;y);y))].\min\_{G}\max\_{D}V(D,G)=\mathbb{E}\_{x\sim p\_{data}(x|y),\ y\sim p\_{y}(y)}\left[\log D\left(x;y\right)\right]+\mathbb{E}\_{z\sim p\_{z}(z),\ y\sim p\_{y}(y)}\left[\log\left(1-D\left(G(z;y);y\right)\right)\right]. |  |

This framework enables tasks such as generating specific digit classes in handwritten digit image datasets or synthesizing asset returns under specific macroeconomic conditions.

Despite their conceptual elegance, GANs often face practical challenges during training.
One major challenge is the inherent instability caused by the adversarial minimax optimization process.
Another common issue is the vanishing gradient problem, which frequently arises from the use of a sigmoid activation function at the discriminator’s output layer.
To mitigate such limitations, improved models such as WGAN (Arjovsky et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib11 "Wasserstein generative adversarial networks")) and WGAN-GP (Gulrajani et al., [2017](https://arxiv.org/html/2601.17773v1#bib.bib12 "Improved training of wasserstein gans")) have been proposed.
These models introduce different optimization formulations that enhance training stability and convergence.

The WGAN replaces the Jensen-Shannon divergence used in the original GAN formulation with the Wasserstein-1 distance.
While the Wasserstein distance is generally computationally intractable, WGAN utilizes the Kantorovich-Rubinstein duality to reformulate the problem into a tractable optimization form.
The WGAN objective is given by:

|  |  |  |
| --- | --- | --- |
|  | minG⁡maxD∈𝒟⁡𝔼x∼pd​a​t​a​(x)​[D​(x)]−𝔼z∼pz​(z)​[D​(G​(z))],\min\_{G}\max\_{D\in\mathcal{D}}\mathbb{E}\_{x\sim p\_{data}(x)}\left[D\left(x\right)\right]-\mathbb{E}\_{z\sim p\_{z}(z)}\left[D\left(G(z)\right)\right], |  |

where 𝒟\mathcal{D} is the set of 1-Lipschitz functions.
In this framework, DD is no longer a binary classifier but a *critic* that estimates the Wasserstein distance between the real and generated distributions.
As a result, WGAN eliminates the need for a sigmoid activation function at the discriminator’s output layer and thereby avoids the vanishing gradient problem.

To enforce the 1-Lipschitz constraint in practice, the original WGAN employs weight clipping on the discriminator’s parameters.
However, this crude approach can restrict the model capacity and lead to suboptimal performance. To mitigate this, Gulrajani et al. ([2017](https://arxiv.org/html/2601.17773v1#bib.bib12 "Improved training of wasserstein gans")) proposed the WGAN-GP, which introduces a soft gradient penalty based on the theoretical result that the optimal critic function has gradients of unit norm almost everywhere. The modified objective of the WGAN-GP becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | minG⁡maxD⁡𝔼x∼pd​a​t​a​(x)​[D​(x)]−𝔼z∼pz​(z)​[D​(G​(z))]+λ​𝔼x~∼px~​(x~)​[(∥∇x~D​(x~)∥2−1)2],\min\_{G}\max\_{D}\mathbb{E}\_{x\sim p\_{data}(x)}\left[D\left(x\right)\right]-\mathbb{E}\_{z\sim p\_{z}(z)}\left[D\left(G(z)\right)\right]+\lambda\mathbb{E}\_{\tilde{x}\sim p\_{\tilde{x}}(\tilde{x})}\left[\left(\lVert\nabla\_{\tilde{x}}D(\tilde{x})\rVert\_{2}-1\right)^{2}\right], |  | (5) |

where x~\tilde{x} denotes points sampled uniformly along straight lines between real and generated samples, and λ\lambda is a penalty coefficient typically set to 10.
This modification has been shown to yield more stable training and reliable convergence, and is therefore widely adopted in applications involving continuous-valued data.

### A.2 Temporal Convolutional Networks (TCNs)

To formalize TCN model, let X∈ℝCin×TX\in\mathbb{R}^{C\_{\text{in}}\times T} denote a one-dimensional input sequence of length TT with CinC\_{\text{in}} channels.
A dilated causal convolutional operator with kernel size kk, dilation factor DD, and output channels CoutC\_{\text{out}} is defined as:

|  |  |  |
| --- | --- | --- |
|  | (W∗X)c,t=∑i=0k−1∑j=1CinWi,j,c⋅Xj,t−D⋅i+bc,\left(W\*X\right)\_{c,t}=\sum\_{i=0}^{k-1}\sum\_{j=1}^{C\_{\text{in}}}W\_{i,j,c}\cdot X\_{j,t-D\cdot i}+b\_{c}, |  |

for c=1,⋯,Coutc=1,\cdots,C\_{\text{out}} and t≥D​(k−1)t\geq D(k-1), where W∈ℝk×Cin×CoutW\in\mathbb{R}^{k\times C\_{\text{in}}\times C\_{\text{out}}} is the weight tensor and b∈ℝCoutb\in\mathbb{R}^{C\_{\text{out}}} is the bias vector.
When D=1D=1, the operation reduces to a standard causal convolution.

A complete TCN consists of a stack of such convolutional blocks with increasing dilation factors at deeper layers.
Formally, a TCN f:ℝnin×T0→ℝnout×TLf:\mathbb{R}^{n\_{\text{in}}\times T\_{0}}\rightarrow\mathbb{R}^{n\_{\text{out}}\times T\_{L}} is composed of:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(X)=ϕO∘gL∘gL−1∘⋯∘g1∘ϕI​(X),f(X)=\phi\_{O}\circ g\_{L}\circ g\_{L-1}\circ\dots\circ g\_{1}\circ\phi\_{I}(X), |  | (6) |

where ϕI:ℝnin×T0→ℝC0×T0\phi\_{I}:\mathbb{R}^{n\_{\text{in}}\times T\_{0}}\rightarrow\mathbb{R}^{C\_{0}\times T\_{0}} and ϕO:ℝCL×TL→ℝnout×TL\phi\_{O}:\mathbb{R}^{C\_{L}\times T\_{L}}\rightarrow\mathbb{R}^{n\_{\text{out}}\times T\_{L}} are 1×11\times 1 convolutional layers that project the input and output channels, respectively.
Each intermediate mapping gℓ:ℝCℓ−1×Tℓ−1→ℝCℓ×Tℓg\_{\ell}:\mathbb{R}^{C\_{\ell-1}\times T\_{\ell-1}}\rightarrow\mathbb{R}^{C\_{\ell}\times T\_{\ell}} is implemented as a residual block composed of two dilated causal convolutions with dilation d=Dℓ−1d=D^{\ell-1}, non-linear activation (e.g., ReLU), dropout, and a residual skip connection.
This composition can be written as

|  |  |  |
| --- | --- | --- |
|  | gℓ​(X)=ReLU​(Convℓ(2)​(Dropout​(ReLU​(Convℓ(1)​(X)))))+Resℓ​(X),g\_{\ell}(X)=\mathrm{ReLU}\left(\mathrm{Conv}^{(2)}\_{\ell}\left(\mathrm{Dropout}\left(\mathrm{ReLU}\left(\mathrm{Conv}^{(1)}\_{\ell}(X)\right)\right)\right)\right)+\mathrm{Res}\_{\ell}(X), |  |

where Convℓ(1)\mathrm{Conv}^{(1)}\_{\ell} and Convℓ(2)\mathrm{Conv}^{(2)}\_{\ell} are dilated causal convolutional layers with dilation Dℓ−1D^{\ell-1}, and Resℓ​(X)\mathrm{Res}\_{\ell}(X) denote either the identity map or a 1×11\times 1 convolution applied to XX to match dimensions when Cℓ−1≠CℓC\_{\ell-1}\neq C\_{\ell}. The overall structure of the TCN is illustrated in Figure [6](https://arxiv.org/html/2601.17773v1#A1.F6 "Figure 6 ‣ A.2 Temporal Convolutional Networks (TCNs) ‣ Appendix A Formal Introductions of GAN and TCN Models ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

![Refer to caption](x17.png)


Figure 6: TCN with the kernel size k=2k=2, the dilation factor D=2D=2, and the number of residual blocks L=2L=2

For computational convenience, we ensure that the output sequence length TLT\_{L} matches the input sequence length T0T\_{0} by applying zero padding to the input of each convolutional layer Convℓ(j)\mathrm{Conv}\_{\ell}^{(j)}.
Each convolution extracts features from kk time points within a fixed window of size D​(k−1)+1D(k-1)+1 and compresses them into a single output vector at the corresponding time step.
This operation reduces the length along the temporal axis.
To prevent this reduction, we pad zeros to the beginning of each input sequence, so that the output sequence at each layer remains the same length as the input.
However, since the padded values do not originate from actual data, they inevitably introduce some bias into the output.
To mitigate this effect, we generate an output sequence over a sufficiently long time horizon and discard the initial portion affected by zero padding, which ensures that the segment of interest is unaffected by its influence.

### A.3 GAN with TCN Backbones

To enhance the generative performance of GANs, various neural network architectures have been employed as the backbone structure of GAN depending on the specific characteristics of the target data (e.g., Radford et al. ([2015](https://arxiv.org/html/2601.17773v1#bib.bib13 "Unsupervised representation learning with deep convolutional generative adversarial networks")); Mogren ([2016](https://arxiv.org/html/2601.17773v1#bib.bib20 "C-rnn-gan: continuous recurrent neural networks with adversarial training")); Zhang et al. ([2019](https://arxiv.org/html/2601.17773v1#bib.bib14 "Self-attention generative adversarial networks")); Wang et al. ([2018](https://arxiv.org/html/2601.17773v1#bib.bib15 "High-resolution image synthesis and semantic manipulation with conditional gans"))).
In this work, to capture the temporal dependencies of financial data, we adopt TCNs as the backbone structure for both the generator and discriminator in GAN to exploit their ability to model long-range inter-temporal dependencies inherent in sequential data.

In this architecture, the generator GG takes as input a sequence of i.i.d. random noise vectors {zt}t=1T\{z\_{t}\}\_{t=1}^{T} typically drawn from a standard normal distribution.
As this input sequence propagates through stacked layers of dilated convolutions in the TCN, initially independent noise variables become progressively intertwined.
This process induces intricate inter-temporal dependencies across time steps in the output sequence.
Through adversarial training, the generator learns to map these latent noise sequences into synthetic data sequences that accurately reflect the temporal dynamics and distributional properties of the real data.
Simultaneously, the discriminator DD is trained to measure discrepancies between the true data distribution pd​a​t​a​(x)p\_{data}(x) and the model-induced distribution pG​(x)p\_{G}(x), explicitly taking into account the sequential structure of the data.

This framework can be naturally extended to the conditional GANs by concatenating additional covariates to the input of both the generator and the discriminator.
The generator then learns to generate condition-specific sequences while the discriminator evaluates distributional discrepancies conditioned on these covariates.

## Appendix B Implementational Details and Hyperparameters of MarketGAN

The generator networks are implemented using a TCN with 80 hidden channels across all layers.
Each convolutional layer is followed by ReLU activation and weight normalization.
A dropout rate of 20% is applied after each activation.
The weights of all convolutional layers are initialized from a normal distribution 𝒩​(0,0.52)\mathcal{N}(0,0.5^{2}).
To ensure that the output sequence length TLT\_{L} matches the input sequence length T0T\_{0}, we apply zero-padding to the input of each convolutional layer.
In our implementation, we set T0=TL=RFS+252×4T\_{0}=T\_{L}=\mathrm{RFS}+252\times 4, where the relatively long TLT\_{L} helps mitigate the impact of zero padding during training.
The discriminator shares the same architecture as the generator except that it uses 160 hidden channels instead of 80.
We use a batch size of B=128B=128.
The Adam optimizer is employed with a learning rate of 0.001 for all neural networks.
The gradient penalty coefficient λ\lambda is set to 10.
The overall training procedure is summarized in Algorithm [1](https://arxiv.org/html/2601.17773v1#algorithm1 "In Appendix B Implementational Details and Hyperparameters of MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

for *epoch =1=1 to EE* do

for *each training mini-batch of time indices {t1,…,tB}\{t\_{1},\dots,t\_{B}\}* do

for *k=1k=1 to nDn\_{D}* do

(a) Sample latent inputs and prepare factor values, real excess return data and covariates

For each tbt\_{b}:

Sample 𝒛tb:tb+T0∼𝒩​(0,I)\boldsymbol{z}\_{t\_{b}:t\_{b}+T\_{0}}\sim\mathcal{N}(0,I)

Obtain covariates 𝒚tb:tb+T0−1\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}

Obtain factor values 𝑭tb+1:tb+TL\boldsymbol{F}\_{t\_{b}+1:t\_{b}+T\_{L}} and real excess returns 𝒓tb+1:tb+TLreal\boldsymbol{r}^{\mathrm{real}}\_{t\_{b}+1:t\_{b}+T\_{L}}

(b) Generate synthetic excess returns

Generate coefficients
𝜶tb:tb+TL−1\boldsymbol{\alpha}\_{t\_{b}:t\_{b}+T\_{L}-1},
𝜷tb:tb+TL−1\boldsymbol{\beta}\_{t\_{b}:t\_{b}+T\_{L}-1},
𝝈tb:tb+TL−1\boldsymbol{\sigma}\_{t\_{b}:t\_{b}+T\_{L}-1} from
(𝒛tb:tb+T0−1,𝒚tb:tb+T0−1)\left(\boldsymbol{z}\_{t\_{b}:t\_{b}+T\_{0}-1},\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}\right) using ([2](https://arxiv.org/html/2601.17773v1#S3.E2 "In 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"))

Generate residuals
ϵtb+1:tb+TL\boldsymbol{\epsilon}\_{t\_{b}+1:t\_{b}+T\_{L}}
from (𝒛tb+1:tb+T0,𝒚tb:tb+T0−1)\left(\boldsymbol{z}\_{t\_{b}+1:t\_{b}+T\_{0}},\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}\right)

Compute 𝒓tb+1:tb+TLsynthetic\boldsymbol{r}^{\mathrm{synthetic}}\_{t\_{b}+1:t\_{b}+T\_{L}} using ([1](https://arxiv.org/html/2601.17773v1#S3.E1 "In 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"))

(c) Update discriminator DD by maximizing the conditional WGAN-GP loss:


|  |  |  |
| --- | --- | --- |
|  | maxD1B∑b=1B[D(𝒓tb+1:tb+TLreal;𝒚tb:tb+T0−1)−D(𝒓tb+1:tb+TLsynthetic;𝒚tb:tb+T0−1)\max\_{D}\frac{1}{B}\sum\_{b=1}^{B}\left[D\left(\boldsymbol{r}^{\mathrm{real}}\_{t\_{b}+1:t\_{b}+T\_{L}};\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}\right)-D\left(\boldsymbol{r}^{\mathrm{synthetic}}\_{t\_{b}+1:t\_{b}+T\_{L}};\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}\right)\right. |  |



|  |  |  |
| --- | --- | --- |
|  | +λ(∥∇𝒓~tb+1:tb+TLD(𝒓~tb+1:tb+TL;𝒚tb:tb+T0−1)∥2−1)2],\left.+\lambda\left(\left\|\nabla\_{\tilde{\boldsymbol{r}}\_{t\_{b}+1:t\_{b}+T\_{L}}}D(\tilde{\boldsymbol{r}}\_{t\_{b}+1:t\_{b}+T\_{L}};\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1})\right\|\_{2}-1\right)^{2}\right], |  |

where 𝒓~=u​𝒓real+(1−u)​𝒓synthetic\tilde{\boldsymbol{r}}=u\boldsymbol{r}^{\mathrm{real}}+(1-u)\boldsymbol{r}^{\mathrm{synthetic}}, and u∼𝒰​(0,1)u\sim\mathcal{U}(0,1)

end for

for *k=1k=1 to nGn\_{G}* do

(a) Sample latent inputs and prepare factor values and covariates

For each tbt\_{b}:

Sample 𝒛tb:tb+T0∼𝒩​(0,I)\boldsymbol{z}\_{t\_{b}:t\_{b}+T\_{0}}\sim\mathcal{N}(0,I)

Obtain covariates 𝒚tb:tb+T0−1\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}
      Obtain factor values 𝑭tb+1:tb+TL\boldsymbol{F}\_{t\_{b}+1:t\_{b}+T\_{L}}

(b) Generate synthetic excess returns

Generate coefficients
𝜶tb:tb+TL−1\boldsymbol{\alpha}\_{t\_{b}:t\_{b}+T\_{L}-1},
𝜷tb:tb+TL−1\boldsymbol{\beta}\_{t\_{b}:t\_{b}+T\_{L}-1},
𝝈tb:tb+TL−1\boldsymbol{\sigma}\_{t\_{b}:t\_{b}+T\_{L}-1} from
(𝒛tb:tb+T0−1,𝒚tb:tb+T0−1)\left(\boldsymbol{z}\_{t\_{b}:t\_{b}+T\_{0}-1},\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}\right) using ([2](https://arxiv.org/html/2601.17773v1#S3.E2 "In 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"))

Generate residuals
ϵtb+1:tb+TL\boldsymbol{\epsilon}\_{t\_{b}+1:t\_{b}+T\_{L}} from
(𝒛tb+1:tb+T0,𝒚tb:tb+T0−1)\left(\boldsymbol{z}\_{t\_{b}+1:t\_{b}+T\_{0}},\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}\right)

Compute 𝒓tb+1:tb+TLsynthetic\boldsymbol{r}^{\mathrm{synthetic}}\_{t\_{b}+1:t\_{b}+T\_{L}} using ([1](https://arxiv.org/html/2601.17773v1#S3.E1 "In 3.1 MarketGAN Architecture ‣ 3 MarketGAN ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"))

(c) Update generator GG by minimizing the conditional WGAN-GP loss:


|  |  |  |
| --- | --- | --- |
|  | minG⁡1B​∑b=1B[−D​(𝒓tb+1:tb+TLsynthetic;𝒚tb:tb+T0−1)]\min\_{G}\frac{1}{B}\sum\_{b=1}^{B}\left[-D\left(\boldsymbol{r}^{\mathrm{synthetic}}\_{t\_{b}+1:t\_{b}+T\_{L}};\boldsymbol{y}\_{t\_{b}:t\_{b}+T\_{0}-1}\right)\right] |  |

end for

end for

end for

Validation check:

Generate synthetic samples 𝒓synthetic\boldsymbol{r}^{\mathrm{synthetic}} over the validation period

Estimate correlation matrix Σ^syn\hat{\Sigma}\_{\text{syn}} from synthetic returns

Estimate correlation matrix Σ^real\hat{\Sigma}\_{\text{real}} from real returns

Compute Frobenius norm ‖Σ^real−Σ^syn‖F\|\hat{\Sigma}\_{\text{real}}-\hat{\Sigma}\_{\text{syn}}\|\_{F}

if *the Frobenius norm is reduced* then Save model parameters;

Fine-tuning:

Train generator for EfineE\_{\text{fine}} epochs on the validation set with reduced learning rate

Algorithm 1 Training Procedure for MarketGAN

## Appendix C Histograms of Aggregated Excess Returns at Weekly and Monthly Frequencies

To evaluate how well the generative models capture return distributional properties beyond the daily level, we analyze the marginal distributions of excess returns aggregated to weekly and monthly frequencies.
Figure [7](https://arxiv.org/html/2601.17773v1#A3.F7 "Figure 7 ‣ Appendix C Histograms of Aggregated Excess Returns at Weekly and Monthly Frequencies ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks") shows the corresponding histograms for both the real data and the synthetic data generated by the MarketGAN models and the factor-model-based bootstrap methods.
Compared to the daily returns shown in Figure [2](https://arxiv.org/html/2601.17773v1#S4.F2 "Figure 2 ‣ 4.2 Marginal Return Distributions ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks"), the aggregated return distributions exhibit lower kurtosis, which aligns with the well-known empirical observations that temporal aggregation tends to smooth extreme events.
At these lower frequencies, the differences between models become less pronounced, and increasing the number of factors does not lead to a clear improvement in the shape of the marginal distribution for either method.
Nonetheless, MarketGAN models consistently provide return distributions that more closely resemble the real data than those generated by the bootstrap methods.
Across both weekly and monthly horizons, the MarketGAN-generated returns preserve higher peaks and better replicate the overall shape of the real return distributions.
In contrast, bootstrap-generated distributions tend to underestimate the kurtosis.

![Refer to caption](x18.png)

![Refer to caption](x19.png)

(a) One-factor model

![Refer to caption](x20.png)

![Refer to caption](x21.png)

(b) Three-factor model

![Refer to caption](x22.png)

![Refer to caption](x23.png)

(c) Five-factor model

Figure 7: Marginal distributions of weekly and monthly aggregated excess returns. FF-1, FF-3, and FF-5 denote the respective factor-model-based bootstrap methods.

## Appendix D Mathematical Formulation of Distance Metrics

This appendix provides the mathematical definitions and underlying assumptions for the distance metrics used to quantitatively compare the distributions of synthetic and real data in Section [4.5](https://arxiv.org/html/2601.17773v1#S4.SS5 "4.5 Quantitative Evaluation Metrics ‣ 4 Empirical Experiments ‣ MarketGANs: Multivariate financial time-series data augmentation using generative adversarial networks").

Fréchet Inception Distance (FID)
Given two sets of data points or feature embeddings—one from real data and one from generated data—FID approximates the Wasserstein-2 distance between the two datasets by using only their empirical means μr\mu\_{r}, μg\mu\_{g} and covariances Σr\Sigma\_{r}, Σg\Sigma\_{g}.
The distance is computed as:

|  |  |  |
| --- | --- | --- |
|  | FID2=∥μr−μg∥22+Tr​(Σr+Σg−2​(Σr​Σg)1/2).\mathrm{FID}^{2}=\lVert\mu\_{r}-\mu\_{g}\rVert\_{2}^{2}+\mathrm{Tr}\left(\Sigma\_{r}+\Sigma\_{g}-2(\Sigma\_{r}\Sigma\_{g})^{1/2}\right). |  |

This formulation captures the discrepancy in both the first and second moments.
It implicitly assumes that the distributions are approximately Gaussian in the data or embedding space.
Higher-order differences or multimodality are not reflected.

Sliced Wasserstein Distance (SWD)
The SWD approximates the Wasserstein-1 distance between high-dimensional distributions PP and QQ by projecting them onto multiple random directions θ∈𝕊d−1\theta\in\mathbb{S}^{d-1} and computing the 1-dimensional Wasserstein distance for each projection:

|  |  |  |
| --- | --- | --- |
|  | SWD​(P,Q)≈1L​∑ℓ=1LW1​(Pθℓ,Qθℓ),\mathrm{SWD}(P,Q)\approx\frac{1}{L}\sum\_{\ell=1}^{L}W\_{1}(P\_{\theta\_{\ell}},Q\_{\theta\_{\ell}}), |  |

where LL is the number of projection directions, and PθℓP\_{\theta\_{\ell}} and QθℓQ\_{\theta\_{\ell}} denote the one-dimensional marginal distributions obtained by projecting PP and QQ onto the direction θℓ\theta\_{\ell}, respectively. In our experiments, we set L=100L=100. SWD does not rely on distributional assumptions such as Gaussianity. It is effective at detecting fine-grained differences, provided that the projection directions are sufficiently expressive.

Mahalanobis Distance (MD)
The MD between a sample xx and a distribution with mean μ\mu and covariance matrix Σ\Sigma is defined as:

|  |  |  |
| --- | --- | --- |
|  | MD​(x,μ)=(x−μ)⊤​Σ−1​(x−μ).\mathrm{MD}(x,\mu)=\sqrt{(x-\mu)^{\top}\Sigma^{-1}(x-\mu)}. |  |

This metric takes into account the covariance structure by rescaling the distance along directions of varying variance. MD is particularly sensitive to deviations from the main distributional structure and therefore useful in detecting anomalies. If Σ\Sigma is ill-conditioned or contaminated by outliers, MD may yield misleading results.

Dynamic Time Warping (DTW)
DTW computes the optimal nonlinear alignment between two time series X=(x1,…,xn)X=(x\_{1},\dots,x\_{n}) and Y=(y1,…,ym)Y=(y\_{1},\dots,y\_{m}) using dynamic programming. The recurrence relation for the cumulative cost matrix γ​(i,j)\gamma(i,j) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(i,j)=D​(i,j)+min⁡{γ​(i−1,j),γ​(i,j−1),γ​(i−1,j−1)},\gamma(i,j)=D(i,j)+\min\left\{\gamma(i-1,j),\;\gamma(i,j-1),\;\gamma(i-1,j-1)\right\}, |  | (7) |

where D​(i,j)=‖xi−yj‖D(i,j)=\|x\_{i}-y\_{j}\| is the pointwise cost, and γ​(n,m)\gamma(n,m) gives the final DTW distance. Unlike other metrics, DTW does not rely on distributional assumptions but assumes that meaningful similarity can be recovered via time-aligned warping. While effective for misaligned sequences, it may be sensitive to local noise and computationally expensive.

## Appendix E Additional Figures

![Refer to caption](x24.png)


(a) MarketGAN1

![Refer to caption](x25.png)


(b) FF-1 bootstrap

![Refer to caption](x26.png)


(c) MarketGAN3

![Refer to caption](x27.png)


(d) FF-3 bootstrap

![Refer to caption](x28.png)


(e) MarketGAN5

![Refer to caption](x29.png)


(f) FF-5 bootstrap

Figure 8: Comparison of real and synthetic equal-weighted excess returns generated by the MarketGAN models and factor-model-based bootstrap methods.



![Refer to caption](x30.png)


(a) MarketGAN1

![Refer to caption](x31.png)


(b) FF-1 bootstrap

![Refer to caption](x32.png)


(c) MarketGAN3

![Refer to caption](x33.png)


(d) FF-3 bootstrap

![Refer to caption](x34.png)


(e) MarketGAN5

![Refer to caption](x35.png)


(f) FF-5 bootstrap

Figure 9: Comparison of real and synthetic excess returns for GOOG generated by the MarketGAN models and factor-model-based bootstrap methods.



![Refer to caption](x36.png)


(a) ACF of MarketGAN1

![Refer to caption](x37.png)


(b) ACF of FF-1 bootstrap

![Refer to caption](x38.png)


(c) VC of MarketGAN1

![Refer to caption](x39.png)


(d) VC of FF-1 bootstrap

![Refer to caption](x40.png)


(e) Lev of MarketGAN1

![Refer to caption](x41.png)


(f) Lev of FF-1 bootstrap

Figure 10: ACF, VC, and Lev of real and synthetic equal-weighted excess return samples generated by the MarketGAN1 and FF-1 bootstrap.



![Refer to caption](x42.png)


(a) ACF of MarketGAN3

![Refer to caption](x43.png)


(b) ACF of FF-3 bootstrap

![Refer to caption](x44.png)


(c) VC of MarketGAN3

![Refer to caption](x45.png)


(d) VC of FF-3 bootstrap

![Refer to caption](x46.png)


(e) Lev of MarketGAN3

![Refer to caption](x47.png)


(f) Lev of FF-3 bootstrap

Figure 11: ACF, VC, and Lev of real and synthetic equal-weighted excess return samples generated by the MarketGAN3 and FF-3 bootstrap.



![Refer to caption](x48.png)


(a) ACF of MarketGAN1

![Refer to caption](x49.png)


(b) ACF of FF-1 bootstrap

![Refer to caption](x50.png)


(c) VC of MarketGAN1

![Refer to caption](x51.png)


(d) VC of FF-1 bootstrap

![Refer to caption](x52.png)


(e) Lev of MarketGAN1

![Refer to caption](x53.png)


(f) Lev of FF-1 bootstrap

Figure 12: ACF, VC, and Lev of real and synthetic excess return samples for GOOG generated by the MarketGAN1 and FF-1 bootstrap.



![Refer to caption](x54.png)


(a) ACF of MarketGAN3

![Refer to caption](x55.png)


(b) ACF of FF-3 bootstrap

![Refer to caption](x56.png)


(c) VC of MarketGAN3

![Refer to caption](x57.png)


(d) VC of FF-3 bootstrap

![Refer to caption](x58.png)


(e) Lev of MarketGAN3

![Refer to caption](x59.png)


(f) Lev of FF-3 bootstrap

Figure 13: ACF, VC, and Lev of real and synthetic excess return samples for GOOG generated by the MarketGAN3 and FF-3 bootstrap.



![Refer to caption](x60.png)


(a) ACF of MarketGAN5

![Refer to caption](x61.png)


(b) ACF of FF-5 bootstrap

![Refer to caption](x62.png)


(c) VC of MarketGAN5

![Refer to caption](x63.png)


(d) VC of FF-5 bootstrap

![Refer to caption](x64.png)


(e) Lev of MarketGAN5

![Refer to caption](x65.png)


(f) Lev of FF-5 bootstrap

Figure 14: ACF, VC, and Lev of synthetic excess return samples for GOOG generated by the MarketGAN5 and FF-5 bootstrap.



![Refer to caption](x66.png)


(a) real

![Refer to caption](x67.png)


(b) MarketGAN1

![Refer to caption](x68.png)


(c) MarketGAN3

![Refer to caption](x69.png)


(d) MarketGAN5

![Refer to caption](x70.png)


(e) FF-1 bootstrap

![Refer to caption](x71.png)


(f) FF-3 bootstrap

![Refer to caption](x72.png)


(g) FF-5 bootstrap

Figure 15: Cross-correlation of real and synthetic excess return samples generated by MarketGANs and factor-model-based bootstrap methods.



![Refer to caption](x73.png)


(a) real

![Refer to caption](x74.png)


(b) MarketGAN1

![Refer to caption](x75.png)


(c) MarketGAN3

![Refer to caption](x76.png)


(d) MarketGAN5

![Refer to caption](x77.png)


(e) FF-1 bootstrap

![Refer to caption](x78.png)


(f) FF-3 bootstrap

![Refer to caption](x79.png)


(g) FF-5 bootstrap

Figure 16: Extreme cross-correlation of real and synthetic excess return samples generated by the MarketGAN models and factor-model-based bootstrap methods.