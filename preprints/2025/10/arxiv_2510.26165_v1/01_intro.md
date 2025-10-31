---
authors:
- Maarten P. Scholl
- Mahmoud Mahfouz
- Anisoara Calinescu
- J. Doyne Farmer
doc_id: arxiv:2510.26165v1
family_id: arxiv:2510.26165
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Learning to Manage Investment Portfolios beyond Simple Utility Functions
url_abs: http://arxiv.org/abs/2510.26165v1
url_html: https://arxiv.org/html/2510.26165v1
venue: arXiv q-fin
version: 1
year: 2025
---


Maarten P. Scholl
[maarten.scholl@st-hughs.ox.ac.uk](mailto:maarten.scholl@st-hughs.ox.ac.uk)
University of OxfordOxfordUnited Kingdom
, 
Mahmoud Mahfouz
[mahmoud.mahfouz@jpmorgan.com](mailto:mahmoud.mahfouz@jpmorgan.com)
J.P. Morgan Chase & CoLondonUnited Kingdom
, 
Anisoara Calinescu
[anisoara.calinescu@cs.ox.ac.uk](mailto:anisoara.calinescu@cs.ox.ac.uk)
University of OxfordOxfordUnited Kingdom
 and 
J. Doyne Farmer
[doyne.farmer@inet.ox.ac.uk](mailto:doyne.farmer@inet.ox.ac.uk)
University of OxfordOxfordUnited Kingdom

(2025)

###### Abstract.

While investment funds publicly disclose their objectives in broad terms, their managers optimize for complex combinations of competing goals that go beyond simple risk-return trade-offs. Traditional approaches attempt to model this through multi-objective utility functions, but face fundamental challenges in specification and parameterization. We propose a generative framework that learns latent representations of fund manager strategies without requiring explicit utility specification.

Our approach directly models the conditional probability of a fund’s portfolio weights, given stock characteristics, historical returns, previous weights, and a latent variable representing the fund’s strategy. Unlike methods based on reinforcement learning or imitation learning, which require specified rewards or labeled expert objectives, our GAN-based architecture learns directly from the joint distribution of observed holdings and market data.

We validate our framework on a dataset of 1436 U.S. equity mutual funds. The learned representations successfully capture known investment styles, such as ”growth” and ”value,” while also revealing implicit manager objectives. For instance, we find that while many funds exhibit characteristics of Markowitz-like optimization, they do so with heterogeneous realizations for turnover, concentration, and latent factors. To analyze and interpret the end-to-end model, we develop a series of tests that explain the model, and we show that the benchmark’s expert labeling are contained in our model’s encoding in a linear interpretable way.
Our framework provides a data-driven approach for characterizing investment strategies for applications in market simulation, strategy attribution, and regulatory oversight.

generative adversarial networks, portfolio management, investment strategies, imitation learning, agent-based modeling

††copyright: cc††journalyear: 2025††conference: 6th ACM International Conference on AI in Finance; November 15–18, 2025; Singapore, Singapore††booktitle: 6th ACM International Conference on AI in Finance (ICAIF ’25), November 15–18, 2025, Singapore, Singapore††doi: 10.1145/3768292.3770426††isbn: 979-8-4007-2220-2/2025/11††ccs: Computing methodologies Neural networks††ccs: Applied computing Economics

## 1. Introduction

Modern Portfolio Theory assumes fund managers maximize a simple utility function that balances risk and return (Markowitz, [1952](https://arxiv.org/html/2510.26165v1#bib.bib15)).
In practice, managers balance multiple competing objectives: tracking error limits, turnover costs, liquidity requirements, regulatory mandates, and behavioral biases (Sharpe, [1966](https://arxiv.org/html/2510.26165v1#bib.bib20)). While these could in theory be combined into complex utility functions, this approach faces the fundamental challenge of specifying unknown objective weights that vary across managers, time, and economic regimes.
Generative modeling offers new ways to understand complex behaviors without specifying explicit objectives. Generative Adversarial Networks (GANs) are frequently used to generate synthetic financial time series (Cont et al., [2025](https://arxiv.org/html/2510.26165v1#bib.bib6)), but no one has applied them *to learn investment strategies and generate realistic populations of investors*. This gap matters for agent-based market simulations, which need realistic models of diverse market participants (Farmer and Foley, [2009](https://arxiv.org/html/2510.26165v1#bib.bib8)).

We present a generative adversarial framework that sidesteps utility specification problems by learning fund manager strategies directly from portfolio holdings data. We model a manager’s strategy as a conditional probability distribution over portfolio weights, without specifying a utility function. Our goal is not theoretical optimality of the portfolio, but capturing real-world manager behavior with all its complexity and imperfections.

Our method enables three applications. First, strategy discovery: the model learns representations that capture known style factors like ”value” and ”growth” alongside subtle, implicit objectives. Second, behavioral cloning: the model generates realistic portfolio allocations for any market state. These synthetic portfolios enable stress testing and counterfactual analysis. Third, agent-based modeling: our framework creates diverse, realistic agents for market simulations.

We make four contributions.

(1) Formulating strategy learning as conditional generation of portfolio allocation:
p​(𝐰t∣𝐗,𝐫,ϕ,𝐰t−1)p\left(\mathbf{w}\_{t}\mid\mathbf{X},\mathbf{r},\boldsymbol{\phi},\mathbf{w}\_{t-1}\right).

(2) Designing a generative architecture that integrates financial factor models with adversarial training.

(3) Evaluating the framework comprehensively on 1,436 U.S. mutual fund portfolios, demonstrating superior performance over baselines.

(4) Providing evidence that learned representations capture known financial patterns and reveal undisclosed manager objectives.

## 2. Related Work

Our research builds on four areas: GANs in finance, strategy classification, imitation learning, and agent-based modeling.

### 2.1. GANs in Finance

Generative Adversarial Networks have gained traction in finance, primarily for synthetic data generation. QuantGAN uses temporal convolutional networks to generate financial price series (Wiese et al., [2019](https://arxiv.org/html/2510.26165v1#bib.bib23)). Conditional tabular GANs have been adapted for financial tasks (Xu et al., [2019](https://arxiv.org/html/2510.26165v1#bib.bib24)), including portfolio optimization for higher Sharpe ratios (Ramirez et al., [2023](https://arxiv.org/html/2510.26165v1#bib.bib18)).
Recent work has further explored these topics for stylized facts in equities markets (Kwon and Lee, [2024](https://arxiv.org/html/2510.26165v1#bib.bib13)) and factor models (Gopal, [2024](https://arxiv.org/html/2510.26165v1#bib.bib9)). Unlike these approaches that focus on either data generation or optimization, our work uses GANs to
learn and represent underlying investment strategies from portfolio holdings.

### 2.2. Strategy Classification

The task of identifying a fund’s investment strategy has traditionally been approached from two main angles. The first, known as returns-based style analysis (RBSA), uses a fund’s historical returns to regress them against the returns of various market indices or factors, thereby inferring the fund’s style (Sharpe, [1992](https://arxiv.org/html/2510.26165v1#bib.bib21); Hasanhodzic and Lo, [2007](https://arxiv.org/html/2510.26165v1#bib.bib11)). The second, holdings-based analysis, examines the characteristics of the securities within a fund’s portfolio at a given point in time to classify its strategy (Brown et al., [2009](https://arxiv.org/html/2510.26165v1#bib.bib3)). Recently, machine learning techniques have improved upon these methods. For instance, researchers have applied neural networks to fund characteristics to achieve higher classification accuracy (Kaniel et al., [2023](https://arxiv.org/html/2510.26165v1#bib.bib12)), while others have used machine learning to explore the nonlinear relationships between a fund’s holdings and its style (DeMiguel et al., [2023](https://arxiv.org/html/2510.26165v1#bib.bib7)). These methods label funds but do not capture the generative process behind a strategy.

### 2.3. Imitation Learning in Finance

Imitation learning provides a framework for mimicking expert behavior from demonstrations, which aligns closely with our goal of cloning fund manager strategies without a predefined reward function. Research in this area has explored methods for inferring latent investment objectives. For example, (Maeda et al., [2020](https://arxiv.org/html/2510.26165v1#bib.bib14)) used multi-modal learning to segment traders based on their implicit goals. These approaches have inspired our work, but they typically depend on some form of expert labeling or require a supplementary reward signal to guide the learning process. Our approach avoids this requirement by learning directly from the observed joint distribution of holdings and market data.

### 2.4. Agent-Based Market Modeling

Agent-based models (ABMs) study financial markets as complex adaptive systems emerging from individual agent interactions (Farmer and Foley, [2009](https://arxiv.org/html/2510.26165v1#bib.bib8); Paulin et al., [2018](https://arxiv.org/html/2510.26165v1#bib.bib16)). ABM realism depends on diverse, authentic agent behaviors. Current approaches use hand-crafted utility functions or simplified rules that need significant effort to properly calibrate (Platt, [2020](https://arxiv.org/html/2510.26165v1#bib.bib17)). For example, (Scholl et al., [2021](https://arxiv.org/html/2510.26165v1#bib.bib19)) demonstrates how three stylized trading strategies (value investors, trend followers, and noise traders) interact in complex, density-dependent ways, but the model relies on manually specified strategy parameters and behaviors. Recent work has advanced market simulation: (Vyetrenko et al., [2019](https://arxiv.org/html/2510.26165v1#bib.bib22)) developed realism metrics for limit order book simulations, while (Yagi et al., [2020](https://arxiv.org/html/2510.26165v1#bib.bib25)) analyzed maker-taker fee impacts using agent-based simulation.

Our work directly addresses ABM calibration challenges by providing a data-driven method for learning diverse, empirically-grounded investment strategies from mutual fund data, enabling more realistic agent populations in market simulations.

## 3. Methods

### 3.1. Generative Problem Formulation

We formulate fund strategy learning as estimating the conditional distribution:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | pM​(𝐰i,t∣𝐰i,t−1,𝐗i,t−1,𝐫i,t−T​…​t−1,ϕa,t)p\_{M}\left(\mathbf{w}\_{i,t}\mid\mathbf{w}\_{i,t{-}1},~\mathbf{X}\_{i,t{-}1},~\mathbf{r}\_{i,t{-}T\ldots t{-}1},~\boldsymbol{\phi}\_{a,t}\right) |  |

where 𝐰∈ℝN\mathbf{w}\in\mathbb{R}^{N} represents portfolio weights, 𝐗∈ℝN×K\mathbf{X}\in\mathbb{R}^{N\times K} captures asset characteristics, 𝐫∈ℝN×T\mathbf{r}\in\mathbb{R}^{N\times T} contains historical returns for t−T,…,t−2,t−1t{-}T,\ldots,t{-}2,t{-}1, and ϕa∈ℝd\boldsymbol{\phi}\_{a}\in\mathbb{R}^{d} encodes the latent strategy of manager aa.

This formulation differs fundamentally from portfolio optimization-based approaches. Rather than assuming managers maximize some composite utility function of returns and risk and associated weights, which not only are heterogeneous among fund managers, but are often not publicly declared and must be assumed, we learn the implicit mapping from market states to portfolio decisions probabilistically.
This means we model the distribution of plausible portfolios, that resemble a manager’s previously observed allocations, conditional on market states.

![Refer to caption](diagram.png)


Figure 1. Architecture of the generative adversarial network for learning investment strategies. The framework consists of four main components: (1) A market model that generates synthetic stock universes (𝐗^,𝐫^)(\mathbf{\hat{X}},\mathbf{\hat{r}}) based on the Carhart four-factor model; (2) A strategy encoder that maps observed portfolio allocations to latent strategy representations ϕ\boldsymbol{\phi}’ (3) A portfolio allocator (decoder) that generates realistic portfolio weights 𝐰^\mathbf{\hat{w}} conditioned on market states and strategy encodings; and (4) A discriminator that distinguishes between real and generated portfolio-market data tuples. Blue boxes represent input data, red boxes show latent representations and synthetic recreations, beige nodes indicate neural network components, and green nodes denote training objectives and evaluation metrics.††: A diagram showing a Neural Network Architecture.

### 3.2. Architecture

Our architecture is a conditional Generative Adversarial Network (GAN). The diagram in Figure [1](https://arxiv.org/html/2510.26165v1#acmlabel1 "Figure 1 ‣ 3.1. Generative Problem Formulation ‣ 3. Methods ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions") summarizes the architecture. It has two components: a Generator that creates realistic portfolio allocations and a Discriminator that distinguishes generated portfolios from real ones. The investment universe contains thousands of stocks with numerous characteristics, creating a high-dimensional learning problem. We address this by using characteristic representations from a market model and an encoder-decoder generator structure.

The dimensionality of market states is large, with thousands of stocks with many characteristics each. The number of samples is small. Early experiments showed models trained only on the real data stock universe performed poorly out-of-sample. For this reason we use a two-stage generator that can be evaluated on synthetic stock universes.

#### 3.2.1. Generative Component for the Investment Universe

The investment universe 𝒰=(X,r)\mathcal{U}=(X,r) is a tuple of characteristics and returns, for a collection of N=500N=500 stocks in random order. X∈ℝN×KX\in\mathbb{R}^{N\times K} are KK characteristics, and r∈ℝN×Tr\in\mathbb{R}^{N\times T} provides a history of TT periods of log returns. We choose N=500N=500 because most funds invest in 500 or fewer stocks, typically using the S&P 500 as their benchmark and universe.

A stock universe generator G𝒰​(X,r)G\_{\mathcal{U}}(X,r) creates synthetic market states. Rather than learning complex asset return dynamics from scratch, we embed the Carhart four-factor model (Carhart, [1997](https://arxiv.org/html/2510.26165v1#bib.bib4)) structure directly into our Variational Autoencoder architecture. The model posits that asset returns are explained by exposures β\beta, obtained from a regression on four risk factors:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | ri,t=αi+∑k=14βi,k​yk,t+ϵi,tr\_{i,t}=\alpha\_{i}+\sum\_{k=1}^{4}\beta\_{i,k}y\_{k,t}+\epsilon\_{i,t} |  |

where αi\alpha\_{i} are idiosyncratic returns and ϵi,t\epsilon\_{i,t} are the residuals of the regression.

The model provides good explanatory power while remaining parsimonious. It has features from three important categories: market, fundamental, and technical characteristics:

y1y\_{1} Market: Value-weighted market return minus risk-free rate

y2y\_{2} Size (SMB): Small minus big market capitalization

y3y\_{3} Value (HML): High minus low book-to-market ratio

y4y\_{4} Momentum (UMD): Prior 12-month return winners minus losers

Pre-computed loadings are available from CRSP (Center for Research in Security Prices, [2024](https://arxiv.org/html/2510.26165v1#bib.bib5)), making the model and coefficients well-studied.

The encoder maps real market states (X,r)(X,r) to latent distributions. After solving the factor model (Eq. [2](https://arxiv.org/html/2510.26165v1#S3.E2 "In 3.2.1. Generative Component for the Investment Universe ‣ 3.2. Architecture ‣ 3. Methods ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions")), it uses attention mechanisms over dimensionally-reduced return cross-sections to learn low-dimensional representations of systematic factor shocks yy and residuals ϵ\epsilon. It separately encodes asset characteristics XX (containing factor loadings β\beta and intercepts α\alpha). The output provides parameters (mean and log-variance) for the latent market state.

The decoder samples from the latent distribution to generate a synthetic market state (X^,r^)(\hat{X},\hat{r}). Both components structurally enforce the factor model. The decoder first decodes the latent variable into synthetic characteristics X^\hat{X} (containing α^,β^\hat{\alpha},\hat{\beta}) and factor shocks y^\hat{y}. The systematic portion of returns is then deterministically computed directly as β^​y^⊺\hat{\beta}\hat{y}^{\intercal}. We further sample the idiosyncratic returns ϵ\epsilon, for which the decoder neural network learns idiosyncratic volatility. Finally, the returns with the desired structure are constructed by applying the factor model Equation [2](https://arxiv.org/html/2510.26165v1#S3.E2 "In 3.2.1. Generative Component for the Investment Universe ‣ 3.2. Architecture ‣ 3. Methods ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions").

#### 3.2.2. Strategy Encoder

The strategy encoder EϕE\_{\phi} maps observed portfolio allocations to a latent strategy representation ϕ∈ℝ8\boldsymbol{\phi}\in\mathbb{R}^{8}. This encoder processes the complete portfolio context through three parallel lanes, one for each input tensor (characteristics, returns, weights), in order to preserve interpretability of how different data sources contribute to strategy representation.

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | Eϕ​(𝐗,𝐫,𝐰t−1,𝐰t)→(𝝁ϕ,log⁡𝝈ϕ2)E\_{\phi}(\mathbf{X},\mathbf{r},\mathbf{w}\_{t{-}1},\mathbf{w}\_{t})\rightarrow(\boldsymbol{\mu}\_{\phi},\log\boldsymbol{\sigma}^{2}\_{\phi}) |  |

The first lane processes characteristics 𝐗\mathbf{X} and weights 𝐰\mathbf{w}, to capture how the portfolio tilts relative to market factors. It computes both portfolio-weighted and universe-average statistics, producing a 4-dimensional latent representation of factor exposures, ϕ1−4\phi\_{1-4}.

The second lane analyzes historical returns 𝐫\mathbf{r} weighted by portfolio allocations. It uses temporal reduction followed by attention mechanisms to capture return patterns and risk dynamics, outputting a 2-dimensional latent ϕ5−6\phi\_{5-6} for performance characteristics.

The third lane examines weight changes 𝐰t−𝐰t−1\mathbf{w}\_{t}-\mathbf{w}\_{t{-}1}, to understand trading patterns and turnover behavior. This produces a 2-dimensional latent encoding the manager’s trading aggressiveness and re-balancing style ϕ7−8\phi\_{7-8}.

Each lane employs the same architecture: after normalization and dimensionality reduction using dense layers, we use multi-head attention. The outputs are combined and processed through dense layers to produce the final 8-dimensional latent distribution parameters (𝝁ϕ,log⁡𝝈ϕ2)(\boldsymbol{\mu}\_{\phi},\log\boldsymbol{\sigma}^{2}\_{\phi}).

![Refer to caption](x1.png)


Figure 2. Two-dimensional visualization of learned strategy representations in latent space for December 2020. Each point represents a fund’s strategy encoding ϕa\boldsymbol{\phi}\_{a}, with coordinates detrended relative to the S&P 500 index (positioned at origin). The separation between groups of portfolios with the same label demonstrates that the learned representations successfully capture known investment styles without supervision.††: Four scatter plots of latent spaces.

#### 3.2.3. Portfolio Allocator (Decoder)

The portfolio allocator DwD\_{w} generates portfolio weights conditioned on the market state and latent strategy:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | Dw​(𝐗,𝐫,ϕ,𝐰t−1)→𝐰^tD\_{w}(\mathbf{X},\mathbf{r},\boldsymbol{\phi},\mathbf{w}\_{t{-}1})\rightarrow\mathbf{\hat{w}}\_{t} |  |

The allocator must produce valid portfolio allocations with appropriate sparsity while capturing the manager’s strategy. It processes the latent strategy ϕ\boldsymbol{\phi} alongside market information, to produce weights reflecting both systematic factor exposures and idiosyncratic selection.

#### 3.2.4. Discriminator

The discriminator DD distinguishes observations of real portfolios from generated allocations based on the complete context. To allow the discriminator to investigate all possible metrics of a portfolio, we design it to examine the full empirical distributions (𝐰T​𝐗,𝐰T​𝐫,𝐰t,𝐰t−1,ϕ)(\mathbf{w}^{T}\mathbf{X},\mathbf{w}^{T}\mathbf{r},\mathbf{w}\_{t},\mathbf{w}\_{t{-}1},\boldsymbol{\phi}). This design enables the discriminator to learn portfolio weighted-average features and other distributional properties.
We employ a Wasserstein GAN (Arjovsky et al., [2017](https://arxiv.org/html/2510.26165v1#bib.bib2)) with gradient penalty (WGAN-GP) (Gulrajani et al., [2017](https://arxiv.org/html/2510.26165v1#bib.bib10)) for stable training. The discriminator determines the Wasserstein distance between sample sets. When presented with real and synthetic data, we interpret this distance as a generator loss: larger distances mean the discriminator easily distinguishes real from synthetic samples. Its architecture resembles the strategy encoder, applying multi-head attention to a reduced portfolio form. This design is sufficient to evaluate the generator on two related tasks:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | ℒreplication=ℒD​((𝐗,𝐫,𝐰,ϕ),(𝐗,𝐫,𝐰^,ϕ)),ℒsynthetic=ℒD​((𝐗,𝐫,𝐰,ϕ),(𝐗^,𝐫^,𝐰^,ϕ)).\mathcal{L}\_{\text{replication}}=\mathcal{L}\_{D}\left(\left(\mathbf{X},\mathbf{r},\mathbf{w},\boldsymbol{\phi}\right),~\left(\mathbf{X},\mathbf{r},\mathbf{\hat{w}},\boldsymbol{\phi}\right)\right),\\ \mathcal{L}\_{\text{synthetic}}=\mathcal{L}\_{D}\left(\left(\mathbf{X},\mathbf{r},\mathbf{w},\boldsymbol{\phi}\right),~\left(\mathbf{\hat{X}},\mathbf{\hat{r}},\mathbf{\hat{w}},\boldsymbol{\phi}\right)\right). |  |

In this equation, the first loss ℒreplication\mathcal{L}\_{\text{replication}} measures the conditional portfolio allocation component’s ability to replicate the original weights given the real market data. The second loss ℒsynthetic\mathcal{L}\_{\text{synthetic}} compares the distributions of real data against fully synthetic data comprising both the simulated stock universe and hypothetical allocation therein. This dual evaluation allows us to separately assess the quality of portfolio generation and the realism of the complete generative model.

### 3.3. Training Objectives

We use the Wasserstein GAN with Gradient Penalty (WGAN-GP) objective for its training stability (Gulrajani et al., [2017](https://arxiv.org/html/2510.26165v1#bib.bib10)). The Discriminator loss ℒD\mathcal{L}\_{D} follows the standard WGAN-GP formulation. The Generator’s objective combines the adversarial loss with regularization terms to ensure financial realism while maintaining stability. The regularization terms also enable an ablation study where we evaluate the generator without discriminator feedback.

The full generator loss ℒG\mathcal{L}\_{G} is:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | ℒG=λ1​ℒreplication+λ2​ℒsynthetic+λ3​ℒexposure\mathcal{L}\_{G}=\lambda\_{1}\mathcal{L}\_{\text{replication}}+\lambda\_{2}\mathcal{L}\_{\text{synthetic}}+\lambda\_{3}\mathcal{L}\_{\text{exposure}} |  |

where all terms are adversarial losses. The L2L\_{2} regularization term Lexposure=(𝐰^T​𝐗−𝐰T​𝐗)2{L}\_{\text{exposure}}=(\mathbf{\hat{w}}^{T}\mathbf{X}-\mathbf{w}^{T}\mathbf{X})^{2} encourages the generated portfolio 𝐰^\hat{\mathbf{w}} to match the real portfolio 𝐰\mathbf{w} on the key metric of factor tilt.

### 3.4. Implementation Details

We use 8 latent dimensions, following the rule of thumb of one dimension per metric we can think of (4 Carhart factors, 2 for mean and variance parameters of returns, 2 more for turnover and concentration, based on weights). Our results suggest this number of latent dimensions provides more than sufficient capacity to capture information about the strategies, as several dimensions exhibit redundancy as there is significant cross-correlation in the latent dimensions. We think the dimensions of the latent representation could be reduced to favor parsimony, or the extra dimensionality can be exploited to shape the latent space in a way that is better interpretable. That is out of scope for this paper. We train using the Adam optimizer with learning rates 10−410^{-4} (generator) and 10−410^{-4} (discriminator), updating the discriminator 3 times per generator update.

## 4. Experiments

We design experiments to test our framework’s ability to reconstruct realistic portfolios, learn meaningful strategy representations, and discover implicit objectives beyond stated investment styles.

### 4.1. Data

We use the CRSP Survivor-Bias-Free US Mutual Fund Database, a standard academic finance dataset. Our sample covers actively managed U.S. equity funds from 2010 to 2024. We apply several quality filters: funds must have at least 12 months of holdings data, report at least 75% of holdings by weight, and allocate at least 75% within our stock universe (the largest 500 U.S. stocks by market cap). After filtering, we have 1436 unique mutual funds with at least one year of observations each. This gives us over 120,000 portfolio observations. We use Lipper classifications (e.g., ”Large-Cap Growth”, ”Small-Cap Value”) as ground-truth labels.
The data splits temporally: training on 2010-2018, validation on 2019, and testing on 2020-2024, ensuring no look-ahead bias.

### 4.2. Baselines

We evaluate our model against increasingly sophisticated baselines and an ablation study:

(1) Zero-Trade (ZT): Maintains previous period weights as a buy-and-hold strategy: 𝐰^t=𝐰t−1\mathbf{\hat{w}}\_{t}=\mathbf{w}\_{t{-}1}. This simple baseline is surprisingly strong.
(2) Turnover-Matched Random (TMR): Tests whether allocations can be explained by random trading at the manager’s typical rate. It adds random perturbations to previous weights, scaling the magnitude so turnover |𝐰^t−𝐰t−1|1|\mathbf{\hat{w}}\_{t}-\mathbf{w}\_{t{-}1}|\_{1} matches the target fund’s historical rate. This isolates strategic selection from trading frequency.

(3) Factor-Tilt Matched (FTM): Argues that managers primarily maintain target factor exposures. It generates portfolios using TMR, then adjusts through rejection sampling until factor exposures 𝐰^tT​𝐗\mathbf{\hat{w}}\_{t}^{T}\mathbf{X} are within 10% of the target’s actual exposures 𝐰tT​𝐗\mathbf{w}\_{t}^{T}\mathbf{X}. This controls for both turnover and explicit factor tilting.

(4) Generator-Only (Ablation): Our generator trained without the discriminator, using only reconstruction losses (ℒ​exposure\mathcal{L}{\text{exposure}}, ℒ​concentration\mathcal{L}{\text{concentration}}, ℒturnover\mathcal{L}\_{\text{turnover}}). This tests whether matching explicit characteristics suffices for realistic portfolios.

### 4.3. Evaluation Metrics

A fundamental challenge in evaluating fund manager models stems from the absence of formal utility specifications. Real-world portfolio construction involves proprietary processes and undisclosed objectives that extend far beyond simple risk-return optimization. We cannot write a comprehensive objective function capturing all manager behaviors because the heterogeneous true objectives remain unknown.
This creates a methodological challenge: while we could add numerous loss components through weighted combinations, choosing weights becomes arbitrary and doesn’t address hidden objectives. We cannot determine whether the discriminator identifies meaningful characteristics or exploits modeling deficiencies.
We address this by evaluating using metrics deliberately excluded from training. This tests whether the model captures genuine investment behaviors that we know to exist, rather than overfitting to misspecified or incorrectly weighted training objectives.

#### 4.3.1. Portfolio Reconstruction Quality

We measure error between generated portfolio 𝐰^\mathbf{\hat{w}} and ground-truth 𝐰\mathbf{w} using metrics not in the regularization loss:

Count Error (ℒcount\mathcal{L}\_{\text{count}}): The absolute difference in the number of assets held (with weight >> 0.01%). Tests realistic portfolio sparsity.

Concentration Error (ℒconcentration\mathcal{L}\_{\text{concentration}}): The absolute difference between the Herfindahl indices of the generated and real portfolios, abs​(‖𝐰^‖22−‖𝐰‖22)\text{abs}(\|\mathbf{\hat{w}}\|\_{2}^{2}-\|\mathbf{w}\|\_{2}^{2}). This measures the accuracy of portfolio concentration.

Turnover Error (ℒturnover\mathcal{L}\_{\text{turnover}}): The squared difference in portfolio turnover, abs((∥𝐰^t−𝐰t−1∥1−∥𝐰t−𝐰t−1∥1)\text{abs}((\|\mathbf{\hat{w}}\_{t}-\mathbf{w}\_{t{-}1}\|\_{1}-\|\mathbf{w}\_{t}-\mathbf{w}\_{t{-}1}\|\_{1}). This tests if the model captures the manager’s trading aggressiveness.

#### 4.3.2. Strategy Representation Quality

A good model should organize strategies meaningfully in latent space ϕ\boldsymbol{\phi}. We probe this with a linear classifier (SVM) to recover Lipper classifications from learned embeddings ϕa\boldsymbol{\phi}\_{a}. The key metric is macro-averaged recall, measuring average per-class accuracy while being robust to class imbalance. High scores indicate the latent space linearly separates real investment styles.

##### Classification

We verify our latent space captures meaningful strategies by testing linear separation of known investment styles. The Lipper scheme categorizes funds by averaging factor exposures over 36-month rolling windows to mitigate market noise, we do the same with the latent representation ϕa\boldsymbol{\phi}\_{a} for each portfolio aa. We then train a linear SVM on these averaged embeddings to predict Lipper classifications. Using simple linear classifiers tests whether the latent space contains expert knowledge in an easily interpretable form.
We use macro-averaged recall for evaluation. For each category, recall is TP/(TP+FN)\text{TP}/(\text{TP}+\text{FN}), measuring the fraction of true members correctly identified. These scores are averaged across categories, giving equal weight regardless of class size. This suits our imbalanced dataset where some styles are more common. High macro-averaged recall indicates the model discovers financially meaningful representations without supervision.

#### 4.3.3. Behavioral Fidelity

We design two tests for subtle, implicit behaviors:

Strategy Stability: Real managers are constrained by the prospectus to maintain consistent styles over time. We measure stability by calculating factor tilt drift relative to market average. For fund aa: ua=1T​∑t=1T|(𝜷a,t−𝜷¯t)−(𝜷a,t−1−𝜷¯t−1)|1u\_{a}=\frac{1}{T}\sum\_{t=1}^{T}|(\boldsymbol{\beta}\_{a,t}-\bar{\boldsymbol{\beta}}\_{t})-(\boldsymbol{\beta}\_{a,t{-}1}-\bar{\boldsymbol{\beta}}\_{t{-}1})|\_{1}, where 𝜷a,t=𝐰a,tT​𝐗\boldsymbol{\beta}\_{a,t}=\mathbf{w}\_{a,t}^{T}\mathbf{X} are factor tilts. Lower drift implies higher stability.

Markowitz Optimal-Proximity: We test whether managers implicitly behave like Markowitz optimizers. There are many models of optimality, but this is well-known and easy to test. For each period, we construct the ex-post efficient frontier from realized returns and covariance. We calculate each fund’s distance from this frontier in risk-return space and rank it compared to a sample of style-matched random portfolios. Smaller distances compared to random suggest a higher likelihood that the portfolio is optimized. We report the average proximity score per Lipper class.

#### 4.3.4. Counterfactual Analysis

We verify that learned strategies encode transferable investment principles rather than memorization through comprehensive counterfactual experiments. These tests examine whether strategies learned in one market context apply meaningfully to different conditions while preserving essential characteristics. We extract latent strategies ϕa\boldsymbol{\phi}\_{a} from portfolios in one time period and apply them to different market regimes, including completely novel synthetic environments, testing whether fundamental investment approaches remain consistent.

Our analysis focuses on three aspects of strategy transfer. First, we verify that factor exposures—systematic tilts toward Value and Growth remain stable when applied to new market conditions. This tests whether the model captures persistent investment philosophies rather than temporary positions. Second, we examine portfolio concentration and turnover patterns to ensure generated portfolios maintain realistic structural properties across contexts. Finally, we perform bidirectional strategy swaps between time periods to confirm that relative differences between strategies are preserved regardless of market regime, which also informs us about the stability of the classification over time.

Table 1. Comparative performance across training objectives and hold-out evaluation metrics (test set average). Baseline models are specified in Section [4.2](https://arxiv.org/html/2510.26165v1#S4.SS2 "4.2. Baselines ‣ 4. Experiments ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions"). Training objectives include replication loss (portfolio reconstruction on real data), synthetic loss (generation on synthetic universes), and overall generator loss. Hold-out metrics assess portfolio realism on characteristics deliberately excluded from training ([4.3](https://arxiv.org/html/2510.26165v1#S4.SS3 "4.3. Evaluation Metrics ‣ 4. Experiments ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions")).

|  | Training Objectives | | | Hold-Out Metrics | | |
| --- | --- | --- | --- | --- | --- | --- |
| Model | ℒreplication\mathcal{L}\_{\text{replication}} | ℒsynthetic\mathcal{L}\_{\text{synthetic}} | ℒgenerator\mathcal{L}\_{\text{generator}} | ℒcount\mathcal{L}\_{\text{count}} | ℒconcentration\mathcal{L}\_{\text{concentration}} | ℒturnover\mathcal{L}\_{\text{turnover}} |
| 1. Zero-Trade | 0.063 | 0.830 | 2.817 | 23 | 0.0072 | 0.1716 |
| 2. Random Trade | 0.068 | 0.831 | 2.810 | 34 | 0.0095 | 0.0415 |
| 3. Factor-Tilt | 0.144 | 0.506 | 3.003 | 31 | 0.0064 | 1.2776 |
| 4. Generator-Only | 0.201 | 0.263 | 2.820 | 84 | 0.0089 | 0.9232 |
| 5. Full GAN | 0.061 | 0.236 | 1.0882 | 15 | 0.0047 | 0.5451 |

##### Experimental Design

We implement the following tests of strategy transfer quality:

(1) Strategy Swap Test: We extract the latent strategy ϕ1\boldsymbol{\phi}\_{1} from one portfolio operating in universe 𝒰1\mathcal{U}\_{1} and apply it to a different universe 𝒰2\mathcal{U}\_{2}. This tests whether strategies encode transferable allocation principles rather than universe-specific memorization.

(2) Strategy Preservation Test: We compare factor exposures between original and counterfactual portfolios to verify that key investment characteristics are maintained during transfer.

## 5. Results

We evaluate our framework across reconstruction quality, strategy representation, and behavioral fidelity metrics. The full GAN architecture outperforms baselines on most metrics, demonstrating the value of adversarial training for learning realistic investment strategies.

### 5.1. Reconstruction Quality

Table [1](https://arxiv.org/html/2510.26165v1#S4.T1 "Table 1 ‣ 4.3.4. Counterfactual Analysis ‣ 4.3. Evaluation Metrics ‣ 4. Experiments ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions") presents reconstruction metrics across all models. The discriminator maintains positive Wasserstein distances even at convergence which is a common outcome, confirming slight discriminator dominance rather than theoretical equilibrium . Despite this, the full model achieves the lowest errors on key hold-out metrics: count error (15 stocks), concentration matching (0.0047).

The Zero-Trade baseline performs surprisingly well on concentration, replication metrics, reflecting the slow turnover in fund holdings. Indeed, the average turnover in our sample ranges between 100%-250% per year. The Generator-Only ablation test shows degraded performance across many metrics except the performance on the synthetic data, with count error increasing to 84 stocks, demonstrating that adversarial feedback is essential for realistic portfolio generation beyond the basic statistical moments of the exposure. That is, the Generator-Only model fails to be realistic because it finds it easier to achieve the desired exposures through allocating to a large number of different stocks. As expected, the random trades with matching turnover score best on the turnover metrics.

### 5.2. Classification Performance

Linear probing of the 8-dimensional latent space achieves a macro-averaged recall of 77% when predicting Lipper classes. Brief experimentation reveals this can be increased to 95% with a non-linear SVM kernel, suggesting that the bulk of the Lipper classes is embedded in the latent space in a straightforward linear way, and that if increased congruence is desired this could be achieved by transformation of the latent space. Figure [2](https://arxiv.org/html/2510.26165v1#acmlabel2 "Figure 2 ‣ 3.2.2. Strategy Encoder ‣ 3.2. Architecture ‣ 3. Methods ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions") visualizes the learned representations for December 2020, with coordinates detrended relative to the S&P 500 index. Growth and value funds form distinct clusters in the latent space, while core funds occupy intermediate positions. Dimensions 1-4, constructed from factor exposures, show the clearest separation between investment styles, raising our confidence the strategy encoder is using risk factor exposures to model different investment styles.

Table 2. Classification performance for investment style prediction using learned latent representations. Linear SVM trained on strategy encodings ϕ\boldsymbol{\phi} to recovered Lipper fund categories. A macro-averaged score of 77% shows the Lipper scheme is contained in the latent space in a simple linear form.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Precision | Recall | F1 Score | Support |
| Large Cap Core | 0.81 | 0.88 | 0.84 | 214 |
| Large Cap Growth | 0.88 | 0.83 | 0.85 | 138 |
| Large Cap Value | 0.68 | 0.44 | 0.53 | 39 |
| S&P 500 Index | 0.86 | 0.94 | 0.90 | 32 |
| Macro Average | 0.81 | 0.77 | 0.78 | 423 |

#### 5.2.1. Latent Space Interpretation

We analyze correlations between the 8-dimensional latent space and portfolio characteristics including Carhart factor loadings, Sharpe ratio, allocation size, and turnover rate.
The latent dimensions show moderate but interpretable correlations with known factors. Dimensions ϕ1\phi\_{1} and ϕ7\phi\_{7} strongly correlate with SMB factor loading and Sharpe ratio, capturing small-cap exposure and performance. Dimension ϕ2\phi\_{2} correlates most strongly with HML, encoding value-growth orientation. Dimensions ϕ4\phi\_{4} and ϕ6\phi\_{6} correlate with allocation size, reflecting portfolio concentration.
The moderate correlation strengths indicate the latent space captures more than simple (linear) factor combinations in each dimension. The apparent redundancy across multiple dimensions likely reflects the model’s adaptation to noisy financial data, where redundant but similar representations built from different inputs can provide additional consistency in noisy tasks.

### 5.3. Behavioral Consistency Metrics

#### 5.3.1. Strategy Stability

Real fund strategies exhibit an average drift of u=0.13u=0.13 in factor space units, compared to u=1.34u=1.34 for the unconstrained random trading baseline. This metric remains consistent between the Generator-Only model and the full architecture, suggesting the exposure regularization alone suffices for capturing strategy persistence, as the generator on its own achieves the desired mean exposures. When trading randomly but constrained by investment style (FTM), the drift is roughly twice that of the real funds and one-fifth of purely random trading, suggesting that the latent space is strongly laid out to reflect average exposures.

#### 5.3.2. Proximity to Efficient Frontier

Table [3](https://arxiv.org/html/2510.26165v1#S5.T3 "Table 3 ‣ 5.3.2. Proximity to Efficient Frontier ‣ 5.3. Behavioral Consistency Metrics ‣ 5. Results ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions") reports the average proximity score for real portfolios and portfolios generated by the models. Among real funds, 95.5% of Index funds and 90.4% of Growth funds show evidence of mean-variance optimization compared to simple random portfolios, while only 67.0% of Value funds exhibit this pattern. The same test repeated for the portfolios generated by the two models produces different percentages. The Generator-Only model does not achieve the same level of optimization, while the full mode does slightly better. This is an area for improvement, and we find that it can be improved by explicit utility modeling by including the Sharpe ratio as an objective. This remains out of scope for this paper.

Table 3. This table shows the proximity scores for different classes of portfolios.

| Fund Category | Empirical | Generator Only | Full Model |
| --- | --- | --- | --- |
| S&P 500 Index | 95.5% | 61.6% | 91.1% |
| Growth (all caps) | 90.4% | 49.8% | 48.7% |
| Core (all caps) | 82.7% | 37.7% | 58.2% |
| Value (all caps) | 67.0% | 37.4% | 52.5% |

### 5.4. Counterfactual Results

We evaluate strategy transferability by extracting latent representations from one market context and applying them to generate portfolios in different universes. Table [4](https://arxiv.org/html/2510.26165v1#S5.T4 "Table 4 ‣ 5.4. Counterfactual Results ‣ 5. Results ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions") summarizes the key metrics.
The full GAN model demonstrates robust strategy transfer. When swapping strategies between different market universes, the generated portfolios maintain factor exposures close to the original strategy. For instance, the SMB exposure changes minimally from -0.773 to -0.767, while the market beta shifts from -1.037 to -0.835—preserving the fund’s defensive stance.
In contrast, the Generator-Only model struggles with strategy transfer. Factor exposures deviate significantly: SMB exposure collapses from -0.773 to -0.164, and momentum (UMD) drops from 0.171 to 0.042.
We combine these insights with results form Table [1](https://arxiv.org/html/2510.26165v1#S4.T1 "Table 1 ‣ 4.3.4. Counterfactual Analysis ‣ 4.3. Evaluation Metrics ‣ 4. Experiments ‣ Learning to Manage Investment Portfolios beyond Simple Utility Functions"). Most tellingly, the model generates portfolios with 189 holdings—nearly double the original—with a Herfindahl index of 0.0089, indicating excessive diversification. This confirms our earlier finding that, without adversarial feedback, the generator achieves target exposures through unrealistic over-diversification.

Table 4. This table summarizes strategy transfer across different market universes. Δ\Delta values show the absolute change in factor exposures between original and transferred strategies. The full GAN model demonstrates robust strategy transfer with minimal drift in key factors, while the Generator-Only model shows significant degradation. These results validate that adversarial training learns transferable investment principles.

| Metric | Full GAN | Generator-Only |
| --- | --- | --- |
| Δ\Delta Market Beta | 0.202 | 0.438 |
| Δ\Delta SMB | 0.006 | 0.609 |
| Δ\Delta HML | 0.055 | 0.052 |
| Δ\Delta UMD | 0.098 | 0.129 |

These results validate that the adversarial training is necessary not just for realistic portfolio generation, but for learning transferable strategy representations. The discriminator forces the generator to capture the essence of investment strategies—their systematic tilts and concentration preferences—rather than merely matching statistical moments through any available means.

## 6. Discussion

Our generative framework successfully learns fund manager strategies without explicit utility specification. The results reveal several important findings. First, adversarial training proves essential—the discriminator forces the generator beyond simple moment matching to capture the full distributional properties of real portfolios. Second, the learned 8-dimensional latent space meaningfully organizes investment strategies, with linear separability of expert classifications achieving high macro-averaged recall. Third, our analysis uncovers implicit optimization behaviors: over four-fifths of active funds exhibit Markowitz-like efficiency seeking.
The framework faces unique challenges inherent to financial data. Very few holdings-level data is publicly available. Market regimes shift over time, making stationarity assumptions problematic for long-term predictions of behavior. Our temporal data splitting prevents look-ahead bias but may not capture sufficient variety of regimes. Additionally, monthly holdings snapshots and the relatively short history of high-quality data (post-2010) limit our ability to model higher-frequency trading strategies or validate performance across multiple market cycles.

### 6.1. Beyond Utility Functions

Our results demonstrate the practical value of learning complex fund strategies without explicit utility specification. The learned representations capture interactions between multiple competing objectives as per the prospectus (style adherence) and unstated constraints (turnover limits, tracking error), as these funds form a continuum in representations.
The partitioned latent space reveals that while factor exposures explain significant variance (dimensions ϕ1\phi\_{1}-ϕ4\phi\_{4}), additional dimensions capturing return patterns and turnover are necessary for realistic strategy generation. This supports the hypothesis that managers behave heterogeneously, optimizing or trading off multiple potentially conflicting objectives, with various degrees of success.
This approach offers particular advantages for agent-based market modeling, where specifying realistic utility functions for diverse agents has been a persistent challenge. Rather than hand-tuning utility parameters (which often results in unrealistic agent behaviors), our framework enables sampling from the empirical distribution of real fund strategies. This data-driven approach can improve the realism of market simulations by populating them with agents whose behaviors are grounded in observed fund management practices.

### 6.2. Implications for Market Simulation

Our framework directly addresses a fundamental challenge in agent-based market modeling: the specification of realistic, heterogeneous agent behaviors. Current ABMs rely on hand-crafted utility functions or simplified trading rules that may poorly approximate real market participants. By learning strategies directly from fund data, we enable a new approach for ABM construction. We can now populate simulations with agents whose behaviors are empirically grounded rather than theoretically postulated. The learned strategy representations can be sampled to create diverse agent populations, interpolated to explore strategy variations, or perturbed to study market dynamics under counterfactual scenarios. This data-driven approach promises more realistic emergent market properties and better calibration to empirical stylized facts.

### 6.3. Limitations and Future Work

Our monthly holdings data cannot capture higher-frequency components of a strategy, potentially missing important market dynamics. The focus on U.S. equity funds, while providing clean data, excludes multi-asset strategies, derivatives usage, and international markets. The 2010-2024 training period, does miss such interesting periods as the 2008 crisis, and may not generalize to different market regimes or future conditions.
Future work should explore conditional generation based on market regimes, investigating robustness to changing conditions. Extending to multi-asset portfolios would require modeling cross-asset dependencies. Integration with market microstructure models could bridge the gap between monthly holdings and daily price formation. Real-time applications might use the framework for strategy monitoring, anomaly detection, or regulatory oversight. Finally, theoretical work connecting our empirical findings to economic models of bounded rationality and multiple objectives could deepen our understanding of investment behavior.

## 7. Conclusions

We present a generative adversarial framework for learning investment strategies from fund holdings data without assuming explicit utility specifications. Our key finding is that fund manager behavior exhibits fundamental heterogeneity that is difficult to capture at scale using traditional utility-based models.
The learned representations reveal a continuous spectrum of strategies rather than discrete clusters. Even within expert-defined categories we observe variation of behaviors. The Lipper classification’s hard boundaries impose artificial discretization. This heterogeneity extends beyond style factors to multiple behavioral dimensions: the degree of mean-variance optimization varies across funds. This heterogeneity explains why explicit utility specification approaches face fundamental challenges. The generative approach sidesteps these specification challenges by learning the complete decision process from observed behavior. Rather than requiring researchers to identify all relevant objectives and estimate their relative importance, our framework captures the full complexity of manager preferences through the learned strategy distributions. This data-driven approach represents a key advantage over methods that require explicit specification of all relevant objectives. While many aspects of the current model can be improved, we think that over the long run leveraging computation and data beats human domain knowledge and engineered features. Therefore this work opens new directions for practical applications where realistic behavior is needed but explicit specification is challenging. Agent-based market simulations, risk management systems, and regulatory monitoring can benefit from models that capture the full diversity of real investment strategies without requiring explicit parameterization of manager objectives. By learning what fund managers actually do rather than assuming what theory suggests they should do, we can model market participants more realistically.

###### Acknowledgements.

This paper was prepared for informational purposes in part by the Artificial Intelligence Research group of JPMorgan Chase & Co and its affiliates (“JP Morgan”), and is not a product of the Research Department of JP Morgan. JP Morgan makes no representation and warranty whatsoever and disclaims all liability, for the completeness, accuracy or reliability of the information contained herein. This document is not intended as investment research or investment advice, or a recommendation, offer or solicitation for the purchase or sale of any security, financial instrument, financial product or service, or to be used in any way for evaluating the merits of participating in any transaction, and shall not constitute a solicitation under any jurisdiction or to any person, if such solicitation under such jurisdiction or to such person would be unlawful. AC acknowledges funding from a UKRI AI World Leading Researcher Fellowship (grant EP/W002949/1) and from a JPMC Faculty Research Award.

## References

* (1)
* Arjovsky et al. (2017)

  Martin Arjovsky, Soumith
  Chintala, and Léon Bottou.
  2017.
  Wasserstein GAN.
  *Proceedings of the 34th International
  Conference on Machine Learning* 70 (1
  2017), 214–223.

  <https://arxiv.org/abs/1701.07875v3>
* Brown et al. (2009)

  Keith C. Brown, W. Van
  Harlow, and Hanjiang Zhang.
  2009.
  *Staying the Course: The Role of Investment
  Style Consistency in the Performance of Mutual Funds*.
  Technical Report.
  University of Texas at Austin.
  [doi:10.2139/SSRN.1364737](https://doi.org/10.2139/SSRN.1364737)
* Carhart (1997)

  Mark M. Carhart.
  1997.
  On Persistence in Mutual Fund Performance.
  *The Journal of Finance*
  52, 1 (3
  1997), 57–82.

  [doi:10.1111/j.1540-6261.1997.tb03808.x](https://doi.org/10.1111/j.1540-6261.1997.tb03808.x)
* Center for Research in Security Prices (2024)

  Center for Research in Security Prices.
  2024.
  CRSP/Compustat Merged Database: Carhart Four-Factor
  Model Loadings.
  Wharton Research Data Services (WRDS).

  <https://wrds-www.wharton.upenn.edu/>
  Accessed: [2024].
* Cont et al. (2025)

  Rama Cont, Mihai
  Cucuringu, Renyuan Xu, and Chao
  Zhang. 2025.
  Tail-GAN: Learning to Simulate Tail Risk
  Scenarios.
  *Management Science* 0,
  0 (2025), 1.
  [doi:10.1287/mnsc.2023.00936](https://doi.org/10.1287/mnsc.2023.00936)
  Articles in Advance.
* DeMiguel et al. (2023)

  Victor DeMiguel, Javier
  Gil-Bazo, Francisco J. Nogales, and
  André A.P. Santos. 2023.
  Machine learning and fund characteristics help to
  select mutual funds with positive alpha.
  *Journal of Financial Economics*
  150, 3 (12
  2023), 103737.

  [doi:10.1016/J.JFINECO.2023.103737](https://doi.org/10.1016/J.JFINECO.2023.103737)
* Farmer and Foley (2009)

  J Doyne Farmer and
  Duncan Foley. 2009.
  The economy needs agent-based modelling.
  *Nature* 460,
  7256 (2009), 685–686.

  <https://doi.org/10.1038/460685a>
* Gopal (2024)

  Achintya Gopal.
  2024.
  NeuralFactors: A Novel Factor Learning Approach to
  Generative Modeling of Equities. In *Proceedings of
  the 5th ACM International Conference on AI in Finance*
  *(ICAIF ’24)*. Association for
  Computing Machinery, New York, NY, USA,
  99–107.
  [doi:10.1145/3677052.3698647](https://doi.org/10.1145/3677052.3698647)
* Gulrajani et al. (2017)

  Ishaan Gulrajani, Faruk
  Ahmed, Martin Arjovsky, Vincent
  Dumoulin, and Aaron Courville.
  2017.
  Improved Training of Wasserstein GANs.
  *Advances in Neural Information Processing
  Systems* 2017-December (3
  2017), 5768–5778.

  <https://arxiv.org/abs/1704.00028v3>
* Hasanhodzic and Lo (2007)

  Jasmina Hasanhodzic and
  Andrew W Lo. 2007.
  Can Hedge-Fund Returns Be Replicated?: The Linear
  Case.
  *Journal of Investment Management*
  5, 2 (2007),
  5–45.
* Kaniel et al. (2023)

  Ron Kaniel, Zihan Lin,
  Markus Pelger, and Stijn
  Van Nieuwerburgh. 2023.
  Machine-learning the skill of mutual fund
  managers.
  *Journal of Financial Economics*
  150, 1 (10
  2023), 94–138.

  [doi:10.1016/J.JFINECO.2023.07.004](https://doi.org/10.1016/J.JFINECO.2023.07.004)
* Kwon and Lee (2024)

  Sohyeon Kwon and Yongjae
  Lee. 2024.
  Can GANs Learn the Stylized Facts of Financial
  Time Series?
  *ICAIF 2024 - 5th ACM International Conference
  on AI in Finance* 1 (10
  2024), 126–133.

  [doi:10.1145/3677052.3698661](https://doi.org/10.1145/3677052.3698661)
* Maeda et al. (2020)

  Iwao Maeda, David deGraw,
  Michiharu Kitano, Hiroyasu Matsushima,
  Kiyoshi Izumi, Hiroki Sakaji, and
  Atsuo Kato. 2020.
  Latent Segmentation of Stock Trading Strategies
  Using Multi-Modal Imitation Learning.
  *Journal of Risk and Financial Management
  2020, Vol. 13, Page 250* 13, 11
  (10 2020), 250.

  [doi:10.3390/JRFM13110250](https://doi.org/10.3390/JRFM13110250)
* Markowitz (1952)

  Harry Markowitz.
  1952.
  Portfolio Selection.
  *The Journal of Finance* 7,
  1 (1952), 77–91.

  <https://www.jstor.org/stable/2975974>
* Paulin et al. (2018)

  James Paulin, Anisoara
  Calinescu, and Michael Wooldridge.
  2018.
  Agent-based modeling for complex financial
  systems.
  *IEEE Intelligent Systems*
  33, 2 (2018),
  74–82.
* Platt (2020)

  Donovan Platt.
  2020.
  A comparison of economic agent-based model
  calibration methods.
  *Journal of Economic Dynamics and Control*
  113 (4 2020),
  103859.

  [doi:10.1016/J.JEDC.2020.103859](https://doi.org/10.1016/J.JEDC.2020.103859)
* Ramirez et al. (2023)

  Domingo Ramirez,
  Jose Manuel Peña, Fernando
  Suárez, Omar Larré, and
  Arturo Cifuentes. 2023.
  A Machine Learning Plus-Features Based Approach
  for Optimal Asset Allocation.
  *ICAIF 2023 - 4th ACM International Conference
  on AI in Finance* (11 2023),
  549–556.

  [doi:10.1145/3604237.3626865](https://doi.org/10.1145/3604237.3626865)
* Scholl et al. (2021)

  Maarten P. Scholl,
  Anisoara Calinescu, and J. Doyne
  Farmer. 2021.
  How market ecology explains market malfunction.
  *Proceedings of the National Academy of
  Sciences* 118, 26
  (2021), e2015574118.
  [doi:10.1073/pnas.2015574118](https://doi.org/10.1073/pnas.2015574118)
* Sharpe (1966)

  William F. Sharpe.
  1966.
  Mutual Fund Performance.
  *The Journal of Business*
  39, 1 (1
  1966), 119–138.

  <https://www.jstor.org/stable/2351741>
* Sharpe (1992)

  William F. Sharpe.
  1992.
  Asset allocation.
  *The Journal of Portfolio Management*
  18, 2 (1
  1992), 7–19.

  [doi:10.3905/JPM.1992.409394](https://doi.org/10.3905/JPM.1992.409394)
* Vyetrenko et al. (2019)

  Svitlana Vyetrenko, David
  Byrd, Nick Petosa, Mahmoud Mahfouz,
  Danial Dervovic, Manuela Veloso, and
  Tucker Balch. 2019.
  Get Real: Realism Metrics for Robust Limit Order
  Book Market Simulations.
  *ICAIF 2020 - 1st ACM International Conference
  on AI in Finance* (12 2019).

  [doi:10.1145/3383455.3422561](https://doi.org/10.1145/3383455.3422561)
* Wiese et al. (2019)

  Magnus Wiese, Robert
  Knobloch, Ralf Korn, and Peter
  Kretschmer. 2019.
  Quant GANs: Deep Generation of Financial Time
  Series.
  *Quantitative Finance* 20,
  9 (12 2019),
  1419–1440.
  [doi:10.1080/14697688.2020.1730426](https://doi.org/10.1080/14697688.2020.1730426)
* Xu et al. (2019)

  Lei Xu, Maria
  Skoularidou, Alfredo Cuesta-Infante, and
  Kalyan Veeramachaneni. 2019.
  Modeling Tabular data using Conditional GAN.
  *Advances in Neural Information Processing
  Systems* 32 (7 2019).

  <https://arxiv.org/pdf/1907.00503>
* Yagi et al. (2020)

  Isao Yagi, Mahiro
  Hoshino, and Takanobu Mizuta.
  2020.
  Analysis of the impact of maker-taker fees on the
  stock market using agent-based simulation.
  *ICAIF 2020 - 1st ACM International Conference
  on AI in Finance* (10 2020).

  [doi:10.1145/3383455.3422523](https://doi.org/10.1145/3383455.3422523)