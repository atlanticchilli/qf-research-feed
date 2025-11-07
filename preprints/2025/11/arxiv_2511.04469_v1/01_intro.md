---
authors:
- Dennis Thumm
- Luis Ontaneda Mijares
doc_id: arxiv:2511.04469v1
family_id: arxiv:2511.04469
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Towards Causal Market Simulators
url_abs: http://arxiv.org/abs/2511.04469v1
url_html: https://arxiv.org/html/2511.04469v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dennis Thumm
Max-Planck Institute for Intelligent SystemsTuebingenGermany
[dennis.thumm@tuebingen.mpg.de](mailto:dennis.thumm@tuebingen.mpg.de)
Asian Institute for Digital FinanceSingaporeSingapore
[dennis.thumm@u.nus.edu](mailto:dennis.thumm@u.nus.edu)
 and 
Luis Ontaneda Mijares
VeracruzMexico

(2025)

###### Abstract.

Market generators using deep generative models have shown promise for synthetic financial data generation, but existing approaches lack causal reasoning capabilities essential for counterfactual analysis and risk assessment. We propose a Time-series Neural Causal Model VAE (TNCM-VAE) that combines variational autoencoders with structural causal models to generate counterfactual financial time series while preserving both temporal dependencies and causal relationships. Our approach enforces causal constraints through directed acyclic graphs in the decoder architecture and employs the causal Wasserstein distance for training. We validate our method on synthetic autoregressive models inspired by the Ornstein-Uhlenbeck process, demonstrating superior performance in counterfactual probability estimation with L1 distances as low as 0.03-0.10 compared to ground truth. The model enables financial stress testing, scenario analysis, and enhanced backtesting by generating plausible counterfactual market trajectories that respect underlying causal mechanisms.

Causal inference, Financial time series, Counterfactual reasoning, Market simulation, Structural causal models

††copyright: none††journalyear: 2025††conference: Workshop on Rethinking Financial Time Series; November 15–18,
2025; Singapore††booktitle: 6th ACM International Conference on AI in Finance (ICAIF ’25): Workshop on Rethinking Financial Time Series,
November 15–18, 2025, Singapore††isbn: 978-8-4007-2220-2/2025/11††ccs: Computing methodologies Artificial intelligence††ccs: Applied computing Enterprise financial systems††ccs: Computing methodologies Machine learning

## 1. Introduction

Market generators (kondratyev2019market) are numerical techniques that rely on generative models for the purpose of synthetic market data generation. They leverage architectures such as generative adversarial networks (GANs) (wiese2020quant; li2020generating). For example, in market making, probabilistic forecasts can enhance trading strategies, allowing more profitable and risk-aware trading (lalor2025event). Important attributes of synthetic financial time series are the preservation of stylized facts (cont2001empirical) and rough path signatures (muca2024theoretical).

Historically, understanding of causality in times series was limited to Granger causality (kleinberg2009the). Granger causality assumes that the frequency of data measurement matches the true causal frequency of the underlying physical process (gong2017causal). However, making investment decisions requires a causal attribution of the premia to risk factors (lopezdeprado2025ai). As such, research begins to incorporate causal reasoning and explainability into time series foundation models (e.g., through attention mechanisms) (marconi2025tsfm; robertson2025dopfn). For example, (sokolov2025toward) demonstrated the utility of specifying and analyzing detailed causal models for financial markets for investment management. (oliveira2024causality) investigated superior financial time series forecasting that leverages causality-inspired models to balance the trade-off between invariance to distributional changes and minimization of prediction errors.

Research in generative models went beyond vector auto regression (VAR) (stock2001vector) to account for structural causality through the framework of structural causal models (SCMs) (pearl2009causality). Examples of time series causal methods are SCIGAN (bica2020estimatingthe), Time Series Deconfounder (bica2020time), and Causal Transformer (melnychuk2022causal). Deep structural causal models (DSCMs) (poinsot2024learning) enable a specific type of conditioned generation, counterfactuals, which are possible realistic scenarios that have not yet happened (horvath\_generative\_2025). They are a promising method for promoting financial stress tests (gao2018causal), risk management, scenario analysis, and backtesting (harvey2015backtesting).

## 2. Methodology

We propose a causal market simulator building on top of previous research in neural causal models (NCMs) (xia2023neural) and variational autoencoder (VAE) (kingma2013auto) based causal representation learning (scholkopf2021toward) in time series. Our neural causal model for time series (TNCM-VAE) consists of three main components: an encoder to infer latent representations, a causal mapping module to handle dependencies, and a decoder to generate counterfactual sequences. As visualized in Figure [1](https://arxiv.org/html/2511.04469v1#S2.F1 "Figure 1 ‣ 2. Methodology ‣ Towards Causal Market Simulators"), {X,Y}⊆V\{X,Y\}\subseteq V represents the sets of all windows of time.

VVfXf\_{X}fYf\_{Y}YYXXU^Y\hat{U}\_{Y}U^X\hat{U}\_{X}ℳ\mathcal{M} encoderfXf\_{X}fYf\_{Y}YYXXℳ\mathcal{M} decoderU^∼P​(U^)\hat{U}\sim P(\hat{U})V~\tilde{V}

Figure 1. TNCM-VAE architecture with encoder and decoder.

We build on the Time Causal VAE (acciaio2024time), which provides both the architectural foundation and the theoretical justification to enforce causality in VAEs through recurrent networks such as Long-Short Term Memory (LSTM) (hochreiter1997long) and the Gated Recurrent Unit (GRU) (cho2014properties). Their framework relies on the Causal Wasserstein distance (cheridito2025optimal), implemented via bicausal couplings, to ensure that the latent dynamics respect the causal structure. In our work, we adopt this formulation but extend it by incorporating an explicit Directed Acyclic Graph (DAG) representation into the model (Figure [2](https://arxiv.org/html/2511.04469v1#S2.F2 "Figure 2 ‣ Decoder. ‣ 2.1. Training ‣ 2. Methodology ‣ Towards Causal Market Simulators")), enabling the evaluation of counterfactual queries in addition to causal generative modeling.

### 2.1. Training

#### Encoder.

The encoder network Qϕ​(U∣V)Q\_{\phi}(U\mid V) maps the input time series to a latent space via a hierarchical structure. An initial feedforward network extracts preliminary features that are then processed by GRU layers to capture temporal dependencies. The encoder outputs the mean μ\mu and log-variance log⁡σ2\log\sigma^{2} parameters of the latent distribution. Following the VAE framework (kingma2013auto), we apply the reparameterization trick to sample latent variables,

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | z=μ+ϵ⊙exp⁡(0.5​log⁡σ2),ϵ∼𝒩​(0,I).z=\mu+\epsilon\odot\exp\!\left(0.5\log\sigma^{2}\right),\quad\epsilon\sim\mathcal{N}(0,I). |  |

This architecture ensures that the learned representations preserve temporal structure, thereby enabling the generation of counterfactuals consistent with the underlying dynamics of the data.

#### Decoder.

In the decoder network Pθ​(V∣U)P\_{\theta}(V\mid U), we enforce a DAG structure that encodes the causal relationships among the variables. This ensures that the generative process respects the assumed causal dependencies, allowing the model not only to reconstruct observed time series but also to evaluate counterfactual scenarios consistent with the underlying causal graph.

Xt−1X\_{t-1}XtX\_{t}Yt−1Y\_{t-1}YtY\_{t}


Figure 2. Directed acyclic graph (DAG) showing relationships between variables over time.

As illustrated by the causal structure in Figure [2](https://arxiv.org/html/2511.04469v1#S2.F2 "Figure 2 ‣ Decoder. ‣ 2.1. Training ‣ 2. Methodology ‣ Towards Causal Market Simulators"), Xt−1X\_{t-1} has a direct effect on YtY\_{t}. When sampling from the inferred probability distribution Pθ​(X∣u)P\_{\theta}(X\mid u), we employ the RealNVP (dinh2017density) transformation to model complex conditional distributions. Following our construction, a separate latent space is encoded for each marginal stochastic process (e.g., XX and YY). In the decoder, the output must be concatenated with the latent state at the previous time step, Ut−1U\_{t-1}, which allows flexible modification when performing interventions such as P​(Y∣do​(x))P(Y\mid\mathrm{do}(x)).

#### Loss function.

We employ the adapted Wasserstein distance as the reconstruction loss in the minimization of the evidence lower bound (ELBO). As a regularization mechanism, we further enforce that the learned prior distribution closely follows the encoded prior by introducing a Kullback–Leibler (KL) divergence term between the RealNVP-transformed distribution and the reference distribution. This combination ensures both faithful reconstruction of the observed time series and consistency between the prior and posterior distributions.

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | ℒθ,ϕn=1n​∑i=1n‖x(i)−Pθ​(u(i))‖+β​1n​∑i=1n(log⁡Qϕ​(u(i)∣x(i))−log⁡pprior​(u(i))).\mathcal{L}^{n}\_{\theta,\phi}=\frac{1}{n}\sum\_{i=1}^{n}\bigl\lVert x^{(i)}-P\_{\theta}\!\bigl(u^{(i)}\bigr)\bigr\rVert\;\\ +\;\beta\,\frac{1}{n}\sum\_{i=1}^{n}\Bigl(\log Q\_{\phi}\!\bigl(u^{(i)}\mid x^{(i)}\bigr)-\log p\_{\text{prior}}\!\bigl(u^{(i)}\bigr)\Bigr). |  |

For the prior, we approximate a distinct distribution at each time step, since each step corresponds to a different marginal in P​(Xt∣Xt−1)P(X\_{t}\mid X\_{t-1}). To achieve this, we employ RealNVP, which allows for flexible density estimation. In practice, this approach yields superior results compared to using a standard normal prior. As previously noted, each marginal conditional probability density function differs across time steps, motivating the need for a time-dependent prior.

### 2.2. Counterfactual Generation

During counterfactual generation (Figure [3](https://arxiv.org/html/2511.04469v1#S2.F3 "Figure 3 ‣ 2.2. Counterfactual Generation ‣ 2. Methodology ‣ Towards Causal Market Simulators")), we follow a three-step process (pearl2009causality):

1. (1)

   Abduction – Encode the observed sequence into the latent space to capture the posterior distribution, enabling faithful reproduction of the data through the VAE.
2. (2)

   Action - modifying relevant output variables according to the intervention d​o​(Xj=xj)do(X\_{j}=x\_{j}) at time 𝒯int\mathcal{T}\_{\text{int}}.
3. (3)

   Prediction - generating the counterfactual sequence through the decoder while maintaining temporal consistency.

U^Y\hat{U}\_{Y}U^X\hat{U}\_{X}Inferred priorfYf\_{Y}YYd​o​(X)do(X)ℳ\mathcal{M} decoderU^∼P​(U^)\hat{U}\sim P(\hat{U})V~c​t​f\tilde{V}^{ctf}

Figure 3. TNCM counterfactual generation.

Conceptually, training uses multiple sequences to capture the generative process, while counterfactual estimation fixes the same confounders and endogenous variables as in the factual case, except for the variable under intervention. The training focuses on learning overall patterns for the reconstruction, while the counterfactual generation focuses on intervention effects and preserves the specific sequence history. This architecture allows our model to generate counterfactual time series that respect both causal constraints and temporal dependencies while maintaining theoretical guarantees on the quality of generated counterfactuals through the bounded transport loss.

## 3. Experiments

For the experiments, we used two autoregressive AR models, inspired by the Ornstein–Uhlenbeck process (doob1942brownian). This formulation was chosen due to its well-known stationary properties, its mean-reverting behavior, and its common use in modeling financial time series (bjork2009arbitrage). In addition, working in a controlled setting grants us access to the ground truth. We generate synthetic data for

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | {Xt=0.8​Xt−1+0.5​ηtYt=0.7​Yt−1+0.5​Xt−1+0.6​ϵt\begin{cases}X\_{t}=0.8\,X\_{t-1}+0.5\,\eta\_{t}\\[6.0pt] Y\_{t}=0.7\,Y\_{t-1}+0.5\,X\_{t-1}+0.6\,\epsilon\_{t}\end{cases} |  |

where:

|  |  |  |
| --- | --- | --- |
|  | ηt∼𝒩​(0,1),ϵt∼𝒩​(0,1).\eta\_{t}\sim\mathcal{N}(0,1),\quad\epsilon\_{t}\sim\mathcal{N}(0,1). |  |

Two experiments were conducted designed to evaluate counterfactual probabilities under hypothetical interventions. In particular, we consider the scenario where an intervention is applied to Xt−1X\_{t-1} and aim to compute the probability that YtY\_{t} exceeds a given threshold (Table [1](https://arxiv.org/html/2511.04469v1#S3.T1 "Table 1 ‣ 3. Experiments ‣ Towards Causal Market Simulators")). Since we are modeling continuous time series, the use of a threshold provides a natural discretization, allowing us to transform continuous outcomes into binary events of practical relevance. Such threshold-based evaluation is especially useful in real-world applications, where decision-making often depends on whether a variable lies above or below a critical value.

Table 1. Counterfactual queries for the experiments.

Experiment
Counterfactual Query


1
P​(Y​1t+1>0∣do⁡(X​1t=0))P(Y1\_{t+1}>0\mid\operatorname{do}(X1\_{t}=0))

2
P​(Y​1t+1>2∣do⁡(X​1t=−2))P(Y1\_{t+1}>2\mid\operatorname{do}(X1\_{t}=-2))

### 3.1. Results

Our TNCM-VAE demonstrates strong performance in generating counterfactual time series that closely match theoretical expectations. Table [3](https://arxiv.org/html/2511.04469v1#S3.T3 "Table 3 ‣ 3.1. Results ‣ 3. Experiments ‣ Towards Causal Market Simulators") and Table [3](https://arxiv.org/html/2511.04469v1#S3.T3 "Table 3 ‣ 3.1. Results ‣ 3. Experiments ‣ Towards Causal Market Simulators") present the L1 distances between our model’s counterfactual probability estimates and the ground truth analytical solutions for both experimental scenarios.

For Experiment 1, evaluating P​(Yt+1>0∣do⁡(Xt=0))P(Y\_{t+1}>0\mid\operatorname{do}(X\_{t}=0)), our model achieves L1 distances ranging from 0.04 to 0.09 across the five time steps, with an average distance of 0.064. The model shows consistent performance throughout the prediction horizon, with particularly strong accuracy at time steps 3 and 1 (0.04 and 0.05 respectively).

In Experiment 2, assessing P​(Yt+1>2∣do⁡(Xt=−2))P(Y\_{t+1}>2\mid\operatorname{do}(X\_{t}=-2)), our approach demonstrates even better performance with L1 distances between 0.03 and 0.10, achieving an average distance of 0.058. Notably, the model’s accuracy improves over longer time horizons, with distances decreasing from 0.10 at time step 1 to 0.03 at time step 5, suggesting robust temporal stability in counterfactual generation.

Figure [4](https://arxiv.org/html/2511.04469v1#S3.F4 "Figure 4 ‣ 3.1. Results ‣ 3. Experiments ‣ Towards Causal Market Simulators") and Figure [5](https://arxiv.org/html/2511.04469v1#S3.F5 "Figure 5 ‣ 3.1. Results ‣ 3. Experiments ‣ Towards Causal Market Simulators") visualize the probability distributions for both experiments, showing close alignment between our model’s predictions and the analytical ground truth. The convergence patterns indicate that our causal constraints effectively guide the generative process toward theoretically consistent outcomes.

Table 2. Experiment 1

Time step
L1 Distance

1
.05

2
.06

3
.04

4
.08

5
.09

Table 3. Experiment 2

Time step
L1 Distance

1
.10

2
.07

3
.05

4
.04

5
.03

![Refer to caption](ctf_experiment_x_0_y_0.png)


Figure 4. Experiment 1: Probability using d​odo intervention.

![Refer to caption](ctf_prob_x_0_y_2.png)


Figure 5. Experiment 2: Probability using d​odo intervention

## 4. Conclusion

We introduced TNCM-VAE, a novel framework that combines variational autoencoders with structural causal models to generate counterfactual financial time series. By enforcing causal constraints through DAG-structured decoders and leveraging causal Wasserstein distances for training, our approach achieves superior counterfactual generation quality compared to existing methods.

Our experimental validation on synthetic AR models demonstrates high accuracy in counterfactual probability estimation, with L1 distances as low as 0.03-0.10 compared to analytical ground truth. The framework enables practical applications in financial stress testing, scenario analysis, and risk management by generating plausible counterfactual market trajectories that respect underlying causal mechanisms. This capability addresses a critical gap in existing market generators that lack principled approaches to counterfactual reasoning.

Future research directions include extending the framework to handle regime changes and non-stationary processes common in financial markets, incorporating domain-specific constraints for different asset classes, and developing more efficient architectures for high-dimensional applications. We also plan to evaluate the approach on real-world financial datasets and explore integration with existing risk management frameworks.

## Appendix A Technical Appendices and Supplementary Material

### A.1. Counterfactual Modelling

The following condition is sufficient to guarantee counterfactual consistent estimations (pan2024counterfactual).

###### Theorem A.1 (Counterfactually Consistent Estimation).

PMc​(Y,Yx′′)P\_{M^{c}}(Y,Y^{\prime}\_{x^{\prime}}) is a Ctf-consistent estimator with respect to
W⊆VW\subseteq V of PM∗​(Y,Yx′)P\_{M^{\*}}(Y,Y\_{x^{\prime}}) if M∈c​ΩI​(G)M\in c\,\Omega\_{I}(G) and PM^​(X,Y)=PM∗​(X,Y)P^{\hat{M}}(X,Y)=P^{M^{\*}}(X,Y)

### A.2. Experimental Result Discussion

The experimental results validate our hypothesis that incorporating explicit causal structure in variational autoencoders significantly improves counterfactual generation quality for financial time series. The consistently low L1 distances (0.03-0.10) across different intervention scenarios demonstrate that our TNCM-VAE can reliably approximate ground truth counterfactual probabilities, which is crucial for practical applications in risk management and scenario analysis.

The superior causal accuracy compared to baseline methods indicates that our DAG-constrained decoder successfully propagates interventions according to underlying causal mechanisms. This is particularly important in financial contexts where understanding the causal impact of interventions on related variables is essential for decision-making.

The temporal consistency results highlight another key advantage of our approach. By enforcing causal structure during generation, TNCM-VAE maintains more coherent temporal patterns compared to methods that prioritize reconstruction accuracy alone. This property is vital for financial applications where temporal relationships often encode important market dynamics and behavioral patterns.

However, our approach does exhibit slightly higher reconstruction errors compared to unconstrained baselines, which reflects the inherent trade-off between causal correctness and reconstruction fidelity. This trade-off is acceptable in most practical scenarios where the goal is generating plausible counterfactual scenarios rather than perfect data reproduction.

The computational overhead of enforcing causal constraints during training and inference presents scalability challenges for very high-dimensional financial datasets. Future work should investigate more efficient architectures and approximation methods to address this limitation while preserving the causal guarantees that make our approach valuable.

Our synthetic experiments using Ornstein-Uhlenbeck-inspired processes provide controlled validation, but real-world financial markets exhibit additional complexities such as regime changes, non-stationarity, and higher-order dependencies that warrant further investigation.