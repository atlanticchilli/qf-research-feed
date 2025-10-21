---
authors:
- Jinrui Zhang
doc_id: arxiv:2510.17165v1
family_id: arxiv:2510.17165
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Trading with the Devil: Risk and Return in Foundation Model Strategies'
url_abs: http://arxiv.org/abs/2510.17165v1
url_html: https://arxiv.org/html/2510.17165v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jinrui Zhang
Tsinghua UniversityBeijingChina
[zhangjr23@mails.tsinghua.edu.cn](mailto:zhangjr23@mails.tsinghua.edu.cn)

###### Abstract.

Foundation models—already transformative in domains such as natural language processing—are now starting to emerge for time‐series tasks in finance. While these pretrained architectures promise versatile predictive signals, little is known about how they shape the risk profiles of the trading strategies built atop them, leaving practitioners reluctant to commit serious capital. In this paper, we propose an extension to the Capital Asset Pricing Model (CAPM) that disentangles the systematic risk introduced by a shared foundation model—potentially capable of generating alpha if the underlying model is genuinely predictive—from the idiosyncratic risk attributable to custom fine‐tuning, which typically accrues no systematic premium. To enable a practical estimation of these separate risks, we align this decomposition with the concepts of uncertainty disentanglement, casting systematic risk as epistemic uncertainty (rooted in the pretrained model) and idiosyncratic risk as aleatory uncertainty (introduced during custom adaptations). Under Aleatory Collapse Assumption, we illustrate how Monte Carlo dropout—among other methods in the uncertainty‐quantization toolkit—can directly measure the epistemic risk, thereby mapping trading strategies to a more transparent risk–return plane. Our experiments show that isolating these distinct risk factors yields deeper insights into the performance limits of foundation‐model‐based strategies, their model degradation over time, and potential avenues for targeted refinements. Taken together, our results highlight both the promise and the pitfalls of deploying large pretrained models in competitive financial markets.

Quantitative finance, Uncertainty quantization, CAPM, Foundation Models

††conference: Make sure to enter the correct
conference title from your rights confirmation email; Aug 03–07,
2025; ON, Toronto††ccs: Information systems Data mining††ccs: Computing methodologies Machine learning††ccs: Applied computing Electronic commerce

## 1. Introduction

Recent advances in machine learning has transformed the landscape of modern financial markets (Hajj and Hammoud, [2023](https://arxiv.org/html/2510.17165v1#bib.bib28); Cao, [2023](https://arxiv.org/html/2510.17165v1#bib.bib9)), with applications spanning single asset timing (Nelson et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib44); Selvin et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib48)), portfolio optimization (Zhang et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib63)), and even market making (Zhong et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib64)). In parallel, trading models have evolved from single‐variate transformers (Malibari et al., [2021](https://arxiv.org/html/2510.17165v1#bib.bib37); Ding et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib19)), reinforcement learning agents (Deng et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib15)), to complex multi‐modal systems with LLM agents (Sun et al., [2023](https://arxiv.org/html/2510.17165v1#bib.bib54)). While these approaches have demonstrated promise in capturing complex market signals, risk management remains elusive in these blackbox strategies. Some tentative solutions try to incorporate uncertainty information into the model itself (Chauhan et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib10); Sun et al., [2022](https://arxiv.org/html/2510.17165v1#bib.bib53)). As Goodhart’s Law (Goodhart, [1984](https://arxiv.org/html/2510.17165v1#bib.bib25)) reminds us, embedding risk measures within the same predictive model can inadvertently inflate systemic vulnerabilities (Boucher et al., [2014](https://arxiv.org/html/2510.17165v1#bib.bib8); Danielsson et al., [2016](https://arxiv.org/html/2510.17165v1#bib.bib11))—When a measure becomes a target, it ceases to be a good measure.

Meanwhile, large pretrained models are quickly gaining traction in finance (Wu et al., [2023](https://arxiv.org/html/2510.17165v1#bib.bib59); Yang et al., [2023](https://arxiv.org/html/2510.17165v1#bib.bib60)). Newly emerging large time‐series models (LTSM) similarly undergo fine‐tuning on specific market data to bootstrap predictive performance for tasks like mid‐price prediction or intraday signals (Fu et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib23)). Yet the widespread adoption of foundation models begs the question: do multiple trading strategies—fine‐tuned from the same underlying pretrained network—exhibit correlated performance and systemic risk?

In classical finance, the Capital Asset Pricing Model (CAPM) decomposes a portfolio’s total risk into systematic (market‐driven) and idiosyncratic (asset‐specific) components (Sharpe, [1964](https://arxiv.org/html/2510.17165v1#bib.bib50); Fama and French, [2004](https://arxiv.org/html/2510.17165v1#bib.bib21)). Interestingly, uncertainty disentanglement in machine learning splits a model’s predictive uncertainty into epistemic (model‐related) and aleatory (data‐intrinsic) parts (Der Kiureghian and Ditlevsen, [2009](https://arxiv.org/html/2510.17165v1#bib.bib17)). This symmetry motivates a fundamental question: Can we reconcile these two viewpoints so that each trading strategy’s foundation‐model‐driven risk lines up with CAPM’s notion of systematic exposure, and each fine‐tuning quirk aligns with idiosyncratic or aleatory uncertainty? If so, we could leverage established financial risk theories to deepen our understanding of how large pretrained models collectively shape market dynamics.

In this paper, we bridge the lens of CAPM‐style risk analysis with uncertainty disentanglement to provide a cohesive framework for analyzing trading strategies fine‐tuned from large pretrained (foundation) models. Specifically:

![Refer to caption](x1.png)


Figure 1. A High‐Level View: From the Classical CAPM to the “Foundation‐Model” CAPM. On the left, we show the familiar Capital Market Line (CML) linking the risk‐free asset RfR\_{f} to a tangential portfolio MM, which represents the fully diversified market portfolio in CAPM theory. On the right, we illustrate our foundation‐model extension, where the tangential portfolio MM is replaced by the tangential strategy θT\theta\_{T} that fully exploits the pretrained network. Custom fine‐tuned strategies θs\theta\_{s} may deviate from the Pretrained Market Line (PML) if they bear additional, unpriced (idiosyncratic) variance. We posit a hypothetical optimal strategy θopt\theta\_{\mathrm{opt}}, which shares the same expected return but carries only epistemic risk. The distance in standard deviation between θs\theta\_{s} and θopt\theta\_{\mathrm{opt}} captures the extra variance that could be avoided by more efficient adaptation of the foundation model. This figure foreshadows our framework for adapting CAPM principles to foundation‐model trading, forming the conceptual basis for Sections 3.1 and 3.2.††:

A CAPM‐Inspired Framework for Foundation Model Trading. Our framework starts by defining the Pretrained Market Line (PML) in mean-variance space, which represents the best risk-return trade-off investors can achieve leveraging foundation model’s predictive edge. By analogy with the conventional Capital Market Line (CML), which represents the tangency portfolio combined with the risk-free asset, the PML emerges as the tangent line connecting the risk-free rate to the efficient frontier of fully-invested strategies. This frontier is shaped by the optimally-tuned pretrained model’s ability to refine return forecasts and covariance estimates, thereby shifting the tangency portfolio to a higher Sharpe ratio regime. We demonstrate that if the foundation model embodies informative alpha, its signals enable a steeper PML (higer Sharpe ratio) than the classical CML, as the model-driven tangency portfolio dominates the market portfolio in mean-variance space. This results in a superior risk-return trade-off, where investors can achieve higher expected returns per unit of risk by leveraging the foundation model’s predictive edge.

Uncertainty‐Based PML Estimation. Although the PML offers an elegant conceptual benchmark, its direct empirical estimation is non‐trivial—no less difficult than identifying the fully-diversified market portfolio in standard CAPM. We therefore devise a Bayesian uncertainty‐disentanglement method to approximate the PML for real‐world strategies. Under a key assumption—namely, that any given fine‐tuned strategy exhibiting certain risk and return can be matched by an ideal strategy with identical return yet only the foundation model’s epistemic (shared) risk component—we estimate how much of a strategy’s variance is non‐diversifiable and thus priced on the PML. This approach leverages modern uncertainty quantization (e.g., Monte Carlo dropout) to differentiate between epistemic risk that arises from the pretrained model itself and aleatory risk introduced by suboptimal or idiosyncratic customizations.

Empirical Validation. Finally, we test our framework on popular pretrained large time series across multiple asset classes, including US equities and cryptocurrencies. We estimate the PML in a rolling‐window fashion, offering insights into how alpha evolves over time as market conditions shift.

Taken as a whole, our framework paves the way for a more transparent evaluation of foundation‐model‐based trading. Rather than focusing exclusively on alpha generation, we highlight how risk—particularly systemic risk shared by many market participants using the same base model—can propagate through financial markets and, in line with CAPM principles, help explain the returns observed. In the sections that follow, we detail our CAPM‐inspired formulation, present an uncertainty‐based risk‐measurement strategy (with Monte Carlo dropout as one concrete instantiation), and validate the approach empirically on multiple large time‐series architectures. We conclude by discussing the limitations of our work and outlining promising directions for future research—specifically, extending our empirical tests to multivariate and portfolio‐level strategies, addressing the latency–scaling trade‐offs inherent in larger models, and cross-model analysis of shared risk factors—to guide the safe scaling of foundation models in finance.

## 2. Background

Our work builds upon two primary foundations: the classical Capital Asset Pricing Model (CAPM), grounded in mean–variance optimization, and model uncertainty disentanglement, grounded in bayesian methodologies. which separates distinct sources of predictive risk. We summarize each in turn.

### 2.1. Mean–Variance Space and the Capital Market Line

The origins of CAPM lie in Markowitz’s mean–variance optimization (Markowitz, [1952](https://arxiv.org/html/2510.17165v1#bib.bib38)). In this framework, investors select portfolios by balancing expected returns against variances of returns. Specifically, if 𝐰\mathbf{w} is the vector of portfolio weights on n risky assets (with a covariance matrix Σ\Sigma and expected return vector 𝝁\boldsymbol{\mu}), then an investor typically solves:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | min𝐰⁡𝐰⊤​Σ​𝐰subject to𝐰⊤​𝝁=μtarget,𝟏⊤​𝐰=1\min\_{\mathbf{w}}\ \mathbf{w}^{\top}\Sigma\,\mathbf{w}\quad\text{subject to}\quad\mathbf{w}^{\top}\boldsymbol{\mu}=\mu\_{\mathrm{target}},\quad\mathbf{1}^{\top}\mathbf{w}=1 |  |

where μtarget\mu\_{\mathrm{target}} is the desired portfolio return and 𝟏\mathbf{1} is the all‐ones vector (for fully invested portfolios). Tracing out μtarget\mu\_{\mathrm{target}} over all feasible values produces the efficient frontier of portfolios with minimal variance for a given expected return.

The Capital Market Line (CML): When a risk‐free asset with return rfr\_{f} is introduced into the opportunity set, the efficient frontier is reduced to a single tangential portfolio MM that maximizes the Sharpe ratio. All optimal portfolios then lie on the Capital Market Line (CML), described by:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | E​[rp]=rf+(E​[rM]−rfσM)​σpE[r\_{p}]\;=\;r\_{f}\;+\;\Bigl(\tfrac{E[r\_{M}]-r\_{f}}{\sigma\_{M}}\Bigr)\,\sigma\_{p} |  |

where
E​[rp]E[r\_{p}] is the expected return of the portfolio,
rfr\_{f} is the risk‐free rate,
E​[rM]E[r\_{M}] is the expected return of the tangential (market) portfolio MM
σM\sigma\_{M} is the standard deviation of MM, and
σp\sigma\_{p} is the standard deviation of the chosen portfolio pp.

All portfolios on the CML can be seen as combinations of the risk‐free asset and the tangential portfolio MM. The slope of CML (E​[rM]−rf)/σM({E[r\_{M}]-r\_{f}})/\ {\sigma\_{M}} is referred to as the market Sharpe ratio.

### 2.2. Classic CAPM Formulation

Building on mean–variance optimization, the Capital Asset Pricing Model (CAPM) (Sharpe, [1964](https://arxiv.org/html/2510.17165v1#bib.bib50)) posits that any asset ii (or portfolio pp) has an expected return determined by its systematic exposure βi\beta\_{i} to the market:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | E​[ri]=rf+βi​(E​[rm]−rf),βi=Cov​(ri,rm)Var​(rm)E[r\_{i}]\;=\;r\_{f}\;+\;\beta\_{i}\bigl(E[r\_{m}]-r\_{f}\bigr),\qquad\beta\_{i}\;=\;\frac{\mathrm{Cov}(r\_{i},\,r\_{m})}{\mathrm{Var}(r\_{m})} |  |

Under this view, the market is identified with the tangential portfolio MM. The associated variance decomposition for asset (or portfolio) ii is:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | σi2=βi2​σm2+σε2\sigma\_{i}^{2}\;=\;\beta\_{i}^{2}\,\sigma\_{m}^{2}\;+\;\sigma\_{\varepsilon}^{2} |  |

where βi2\beta\_{i}^{2}, σm2\sigma\_{m}^{2} is the systematic (market) risk and σε2\sigma\_{\varepsilon}^{2} is the idiosyncratic (diversifiable) risk. The classical CAPM thus separates total variance into two parts—only the systematic portion merits a risk premium in equilibrium.

### 2.3. Bayesian Perspective and Model Uncertainty

Beyond the realm of finance, Bayesian methodologies have proven instrumental for analyzing predictive uncertainty in machine learning, offering tools to separate and quantify distinct uncertainty sources. From a Bayesian perspective, a model’s predictive distribution,

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | p​(y∣x,𝒟)=∫Ωp​(y∣x,Θ)​p​(Θ∣𝒟)​𝑑Θp(y\mid x,\mathcal{D})\;=\;\int\_{\Omega}p(y\mid x,\Theta)\,p(\Theta\mid\mathcal{D})\,d\Theta |  |

encodes both the likely values of the output yy and the uncertainty surrounding those values, given an input xx and training data 𝒟\mathcal{D}. Although this integral succinctly characterizes predictive risk, it remains analytically intractable in most neural network settings.

A common strategy for approximating this predictive distribution is provided by Monte Carlo (MC) Dropout (Gal and Ghahramani, [2016](https://arxiv.org/html/2510.17165v1#bib.bib24)). Originally introduced as a regularization scheme, dropout randomly “switches off” neurons during training. In MC-Dropout, this randomness is retained at inference time, thereby sampling different model configurations from an approximate posterior Θt∼q​(Θ∣𝒟)\Theta\_{t}\sim q(\Theta\mid\mathcal{D})). By aggregating predictions across multiple forward passes, one obtains not only a mean prediction but also an empirical variance that reflects model’s uncertainty.

In the field of uncertainty disentanglement, researcher further distinguishes model uncertainty between two principal sources(Hora, [1996](https://arxiv.org/html/2510.17165v1#bib.bib30)):

* •

  Epistemic Uncertainty (model‐based): Emanating from limited model knowledge or insufficient training data, epistemic risk can be mitigated through additional information or improved modeling. In time-series trading, this might manifest as sub-optimal fine tuning and lack of finnancial specific priors. This type of uncertainty reflects how sensitively the network’s predictions depend on its parameters: more pronounced variability across forward passes indicates that the model’s beliefs about f​(x)f(x) are unstable or underdetermined by the available data.
* •

  Aleatory Uncertainty (data‐intrinsic): Stemming from inherent noise or stochasticity in the data‐generating process, aleatory risk cannot be reduced by collecting more data or refining the model. In time‐series trading, this might manifest as unpredictable shocks or volatility spikes that no model—however sophisticated—could reliably foresee.

By applying such Bayesian-inspired techniques, one can more clearly distinguish between variance due to fundamental randomness (aleatory) and that stemming from incomplete model knowledge (epistemic). As we shall demonstrate in subsequent sections, recognizing this distinction is essential for CAPM-style analyses of systematic versus idiosyncratic risk in foundation-model-based trading.

## 3. CAPM for Foundation Model Trading

### 3.1. Notation and Strategy Instances

We begin by formalizing the basic objects of our framework. At a high level,
a pretrained backbone θ\theta induces a family of fine-tuned strategies through
different knobs of adaptation and execution. Each such strategy produces a
return distribution characterized by mean and volatility.

###### Definition 3.1 (Backbone family).

Given a pretrained backbone θ\theta, define the strategy family

|  |  |  |
| --- | --- | --- |
|  | 𝒮​(θ)={(θ,ϕ,κ):ϕ∈Φ,κ∈𝒦},\mathcal{S}(\theta)=\{\,(\theta,\phi,\kappa):\ \phi\in\Phi,\ \kappa\in\mathcal{K}\,\}, |  |

where ϕ\phi denotes fine-tuning controls (e.g., data subsets, loss weights,
regularization, LR schedule) and κ\kappa execution controls (e.g., stop-loss,
take-profit, sizing). Each θs∈𝒮​(θ)\theta\_{s}\in\mathcal{S}(\theta) produces a return time series {rs,t}t=1T\{r\_{s,t}\}\_{t=1}^{T} with mean μs\mu\_{s} and stdev σs\sigma\_{s}. We denote cost adjusted returns by r~s,t\tilde{r}\_{s,t} after fees/slippage.

### 3.2. Mean-variance Equilibrium : from CML to PML

Classical Markowitz theory yields a mean–variance efficient frontier; adding a risk‐free asset and allowing risk‐free borrowing/lending produces the *Capital Market Line (CML)*, the straight line through (σ=0,E​[r]=rf)(\sigma{=}0,\,E[r]{=}r\_{f}) and the unique tangency portfolio TfT\_{f}. Tobin’s separation theorem implies any optimal choice is a mixture of rfr\_{f} and TfT\_{f}. In the standard CAPM setting, TfT\_{f} is identified with
the market portfolio MM.

In foundation model analogue, the role of MM is played by an ideal fine-tuned
strategy θT\theta\_{T} that best exploits the predictive edge from the backbone model θ\theta.
We now formalize this tangential strategy and its induced efficient frontier.

In foundation model trading, suppose one has a universe of potential trading signals, all generated or informed by a single pretrained network θ\theta. Each fine‐tuned strategy θi\theta\_{i} can selectively engage or stays out of the market (e.g., by thresholding borderline signals), thereby reserving some portion of capital in the risk‐free asset RfR\_{f}. The resulting efficient set of foundation‐based strategies (PML) thus originates at RfR\_{f} and passing through a tangential strategy TfT\_{f}. In our context, TfT\_{f} is identified with the fine-tuned strategy that most effectively exploit the foundation model’s signals and always fully-invested in risky assets (𝟏⊤​𝐰=1\mathbf{1}^{\top}\mathbf{w}=1), denoted θT\theta\_{\mathrm{T}}.

###### Definition 3.2 (Tangential backbone strategy).

Let θT∈𝒮​(θ)\theta\_{T}\in\mathcal{S}(\theta) be the *fully invested*
(no risk-free mixing) strategy maximizing the Sharpe ratio:

|  |  |  |
| --- | --- | --- |
|  | SRθ=E​[r~θT]−rfsd⁡(r~θT).\mathrm{SR}\_{\theta}\;=\;\frac{E[\tilde{r}\_{\theta\_{T}}]-r\_{f}}{\operatorname{sd}(\tilde{r}\_{\theta\_{T}})}. |  |

Complete Agreement for Equilibrium: Among the many simplifying assumptions in CAPM, the idea of ”complete agreement”—where all investors observe the same distribution of asset returns and select mean–variance-efficient portfolios—finds an interesting parallel in the context of foundation-model trading. We note that multiple practitioners are obliged to fine-tune on the same pretrained weights, given that retraining these models from scratch is prohibitively expensive. Consequently, these fine‐tuned strategies, despite their superficial differences, share largely similar predictive signals, thereby forming an approximate “agreement” about the future markets. In other words, it is not that practitioners independently converge on identical beliefs, but rather that the hefty foundation model itself imposes a common informational baseline.

PML and Optimal Sharpe Ratio: Drawing analogy from CML, Now we formally identify the optimal sharpe ratio of a pretrained model, which is also the slope of PML:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | SRθ=E​[rθT]−rfσ​(rθT)\text{SR}\_{\theta}\;=\;\frac{E\bigl[r\_{\theta\_{T}}\bigr]\;-\;r\_{f}}{\sigma\bigl(r\_{\theta\_{T}}\bigr)} |  |

The sharpe ratio SR​(θ)\text{SR}(\theta) capturing how much excess return θT\theta\_{T} delivers per unit of risk. Each optimal foundation‐based strategy that mixes some proportion of RfR\_{f} with θT\theta\_{T} will reside on this PML, achieving an expected return and standard deviation consistent with standard mean–variance theory:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | E​[ropt]=rf+σopt×SRθE[r\_{\mathrm{opt}}]\;=\;r\_{f}\;+\;\sigma\_{\mathrm{opt}}\times\text{SR}\_{\theta} |  |

The Challenge of Identifying θT\theta\_{T}: Much as the CAPM struggles with the market proxy problem (Sharpe, [1964](https://arxiv.org/html/2510.17165v1#bib.bib50))—the “true” market portfolio is theoretically elusive—our framework also faces a “foundation tangential” proxy challenge. While θT\theta\_{T} is posited to be the unique all‐risky, mean–variance‐efficient strategy of signals based on the pretrained model, in practice, one rarely has perfect knowledge of which exact combination of signals, fine-tuning technique, and hyperparameters yields the “true” θT\theta\_{T}. Consequently, empirical tests must rely on approximations or proxies for θT\theta\_{T}, analogous to how empirical finance employs broad market indices as stand‐ins for the market portfolio. From a financial standpoint, one would use an information-leaked model θleak\theta\_{\mathrm{leak}}, which peeks at future data. Such a leaked model can serve as a simplistic upper-limit construction: by capitalizing on prior knowledge of upcoming market conditions. In the next section, we will show how uncertainty disentanglement can help pinpoint a better estimation on θT\theta\_{T}’s risk-return performance.

### 3.3. PML Estimation via Uncertainty Disentanglement

In the preceding section, we introduced the notion of the Pretrained Market Line (PML) and posited a tangential fine‐tuned strategy, θT\theta\_{T}, that fully exploits the foundation model’s predictive capabilities. Now, we address the practical challenge of estimating the PML using observed suboptimal strategies.

Let θs\theta\_{s} denote the parameters of a custom fine‐tuned model, producing trading signals that yield (random) returns rsr\_{s}. We characterize rsr\_{s} by its expected return E​[rs]E[r\_{s}] and standard deviation σs\sigma\_{s}. To estimate how much of σs\sigma\_{s} is genuinely systematic (i.e., priced on the PML), we adopt the following assumption:

Assumption 3.1. Aleatory Collapse. In a competitive market, any readily observable aleatory uncertainty is swiftly arbitraged away, due to its’ correlation with return. As a result, an uncertainty estimator rapidly converges to an epistemic uncertainty estimator.

In other word, any custom strategy θs\theta\_{s} can be matched by a hypothetical optimal strategy, θsopt\theta\_{s}^{\mathrm{opt}}, that attains the return but exposes only the portion of σs2\sigma\_{s}^{2} that is unavoidable (i.e., the aleatory or systematic risk tied to the foundation model). All additional variance is deemed idiosyncratic and can be “diversified away” by better exploitation of the pretrained signals.

With this assumption, we use a Bayesian risk‐quantization approach—specifically, MC Dropout—to disentangle σs\sigma\_{s}. Concretely, given fine-tuned strategy θs\theta\_{s}, we first obtain KK dropout activated variants {θs(k)}k=1K\{\theta^{(k)}\_{s}\}^{K}\_{k=1}. Denoting the backtested returns as {rs(k)}k=1K\{r^{(k)}\_{s}\}^{K}\_{k=1}, the cross‐sample variance σMC2\sigma\_{\mathrm{MC}}^{2} approximates the epistemic component:

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | μMC=1K​∑k=1Kr^s(k),σMC2=1K​∑k=1K(r^s(k)−μMC)2\mu\_{\text{MC}}=\frac{1}{K}\sum\_{k=1}^{K}\hat{r}^{(k)}\_{s},\quad\sigma^{2}\_{\text{MC}}=\frac{1}{K}\sum\_{k=1}^{K}\left(\hat{r}\_{s}^{(k)}-\mu\_{\text{MC}}\right)^{2} |  |

Regression-Based Estimation of PML: Given multiple custom strategies {θs1,θs2,…}\{\theta\_{s\_{1}},\theta\_{s\_{2}},\dots\}, we can compile an empirical set of {σsi,E​[rsi]}\{\,\sigma\_{s\_{i}},\,E[r\_{s\_{i}}]\} on the risk-return plane. To estimate the underlying slope of the PML (Foundation Sharpe Ratio), we start by subtract out the idiosyncratic portion from using the bayesian decomposition above, leaving a “priced” standard deviation {σsi2−σepi2,E​[rsi]}\{\,\sqrt{\sigma^{2}\_{s\_{i}}-\sigma^{2}\_{\mathrm{epi}}},\,E[r\_{s\_{i}}]\}. Next, perform a linear fit relating E​[rsi]E[r\_{s\_{i}}] to its risk. The resulting slope is an estimate of SRθ\text{SR}\_{\theta}, the maximum Sharpe ratio that the foundation model could theoretically provide, absent extraneous (idiosyncratic) risk. Thus, by analyzing many fine‐tuned strategies in the risk-return plane—once purged of their unpriced variance—we glean an empirical vantage point on the pretrained market line.

Foundation Model Decay: In practice, this bounding procedure can be recalculated on a rolling basis, furnishing a powerful mechanism to dissect both trading crowding effects and the potential decay of foundation models. One may observe the upper limit on SRθ\mathrm{SR}\_{\theta} gradually drifting downward—signaling the foundation’s waning alignment with evolving market conditions—and simultaneously witness the gap between optimal SRθ\mathrm{SR}\_{\theta} and custom SRs\mathrm{SR}\_{\mathrm{s}} widening as the strategy’s signals become more broadly disseminated. Sharp declines in performance may also emerge when new, more potent foundation models appear. We believe this dynamic framework, illustrated in [Figure 4](https://arxiv.org/html/2510.17165v1#S4.F4 "Figure 4 ‣ 4.3. Foundation Model Decay ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies"), opens fertile ground for deeper exploration of ephemeral alpha, model obsolescence, and market equilibria.

Connection with Ensembling: Our pricing model also naturally connects with ensemble‐based strategies, where multiple models—or experts—are combined to enhance predictive accuracy (Yang et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib61); Nti et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib45)). For example, AlphaMix(Sun et al., [2023](https://arxiv.org/html/2510.17165v1#bib.bib54)) explored a mixture‐of‐experts (MoE) approach specifically designed for generating higher excess returns. From our perspective, the additional alpha stems from a lower epistemic uncertainty, resulting in a left shift in the risk-return plane, pushing θs\theta\_{s} closer to PML. While we do not delve further into ensembling in the present work, this connection highlights the inherent and inseparable relationship between risk and return in foundation model trading.

In this section, we developed a Bayesian approach to estimating the Pretrained Market Line, leveraging MC Dropout to disentangle each custom strategy’s risk. The key assumption is that any strategy with a given return can, in principle, be matched by an optimal fine‐tuning that eschews idiosyncratic variance and retains only the portion of risk truly “priced” by the foundation model. By regressing these “priced” risks against observed returns across multiple θs\theta\_{s}, we arrive at an empirical estimate of the foundation Sharpe ratio—the slope of the PML. In the next section, we implement this methodology on real data, illustrating both its strengths and potential pitfalls in practice.

## 4. Experiments

We now present a series of empirical investigations designed to evaluate our CAPM‐inspired framework for foundation‐model trading. Specifically:

1. (1)

   We first conduct a preliminary study of raw prediction performance of foundation model’s signals at various resolutions, clarifying why we ultimately focus on a 1 s horizon for subsequent experiments.
2. (2)

   Building on this, we examine how fine-tuned strategies distribute across the risk–return plane and demonstrate PML estimation for each pretrained model. A windowed PML estimation is performed to better observe model decay over time.

We begin by discussing the data and trading task that serve as the common foundation for each experiment. Unless stated otherwise, identical data sources and methodological choices are used throughout to ensure coherence and comparability across experiments.

Data: We draw upon high‐frequency market data from both U.S. equities and the Binance cryptocurrency exchange, detailed in [Table 1](https://arxiv.org/html/2510.17165v1#S4.T1 "Table 1 ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies"):

* •

  US Equity: One‐second aggregates of the National Best Bid and Offer (NBBO) for a selection of S&P 500 and Russell 2000 constituents, collected through the ibkr API111https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/#hist-bid-ask.
* •

  Cryptos: Best Bid and Offer quotes for FDUSD‐quoted pairs on Binance222https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams# diff-depth-stream, available at 100 ms intervals.

Table 1. Statistics of BBO dataset

|  | S&P 500 | Russell 2000 | Crypto |
| --- | --- | --- | --- |
| Number of assets | 503 | 1947 | 114 |
| Start Time | 2023-01-03 | 2023-01-03 | 2023-01-01 |
| End Time | 2025-01-31 | 2025-01-31 | 2025-01-31 |
| Resolution | 1s | 1s | 100ms |

Depending on resolution requirements, we further aggregate or sample these datasets as necessary, enabling in-depth investigations into short-horizon predictive tasks across a range of market settings.

Trading Task: Although our theoretical framework accommodates both single-asset and multivariate (portfolio-level) trading strategies, for the simplicity we restrict our scope to single-asset trading. This choice avoids the added complexity of portfolio aggregation effects, thus allowing a clearer view of each model’s behavior.

Models: We assess a suite of modern, pretrained time series architectures (TimesFM(Das et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib13)), Chronos(Ansari et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib3)), Moirai(Woo et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib58)), Timer(Liu et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib33)), and TTM(Ekambaram et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib20))), alongside conventional baselines (LSTM(Nelson et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib44)), DARNN (Qin et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib47)), MLP(Naeini et al., [2010](https://arxiv.org/html/2510.17165v1#bib.bib42)), SFM(Zhang et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib62)), and GRU(Shen et al., [2018](https://arxiv.org/html/2510.17165v1#bib.bib51))). All models are either freshly trained or fine-tuned on our collected dataset.

Strategy Construction: Each model outputs a predicted mid-price. (In the case of models generating a patch, we adopt a simple arithmetic aggregation of the patch as the final prediction.) Whenever the predicted mid‐price exceeds the prevailing market quote, we initiate a BUY order; conversely, if the predicted mid‐price falls below the quote, we enter a SELL order. Our backtest assumes orders are filled at the next tick’s best ask—a convention frequently described as a tick-by-tick backtest or immediate execution on next-tick quotes.We then vary hyperparameters (signal thresholds, stop-losses, and take-profit levels) to generate multiple configurations for each model. Each configuration thus occupies a unique position in the risk–return space.

### 4.1. Preliminary : Raw Predictive Performance at Multiple Resolutions

Before delving into risk–return analyses, we first gauge the raw predictive strength of large pretrained models at different time resolutions (from 100ms to 1day), We center this investigation on the notion of model surprise—the difference between the model’s predicted price and the current quote—and measure how strongly this surprise correlates with subsequent market returns. A sustained positive correlation would indicate that the model consistently anticipates price movements, whereas a weaker or transient correlation might imply limited efficacy over shorter trading horizons.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

Figure 2. TimesFMv2’s model surprise–market return correlation at two prediction resolutions for cryptos.
Top: Correlation coefficients for an ultrafast (100ms) prediction horizon, capturing rapid market reactions. Bottom: Corresponding coefficients for a 1 day horizon, illustrating how the model surprise metric behaves at extended timescales.††:



![Refer to caption](x4.png)


(a)  pretrained strategies (colored) vs baseline (grey)

![Refer to caption](x5.png)


(b)  param scaling of Chronos

Figure 3. Daily Risk–Return outcomes (in bps) for all evaluated strategies. (a) Grey markers represent non‐pretrained baseline strategies, and colored markers correspond to foundation‐model–based approaches. (b) A more granular view of Chronos at five parameter scales (8M to 710M), illustrating how model size influences risk–return trade‐offs.††:

To conduct this analysis, we select TimesFMv2, one of the latest large time series model, and fine-tune it separately for five distinct time resolutions: 100ms, 1s, 5min, 15min, and 1day. We then compute an equal‐weighted average of the correlation between each assets’ model surprise and observed returns. For brevity, [Figure 2](https://arxiv.org/html/2510.17165v1#acmlabel2 "Figure 2 ‣ 4.1. Preliminary : Raw Predictive Performance at Multiple Resolutions ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies") showcases only the two extremes—100ms and 1day. We adopt the observational window used in HFT price discovery (Naeini et al., [2010](https://arxiv.org/html/2510.17165v1#bib.bib42)), capturing correlations from five ticks prior to the future, contemporaneously, and up to five ticks beyond it.

Across all tested resolutions, we observe an initially positive correlation between model surprise and asset returns that progressively diminishes over subsequent ticks. Notably, the correlation often approaches or even falls below zero shortly after predictions are issued, suggesting that any informational advantage is rapidly eroded by better-informed traders. When comparing performance across timescales, the 100ms resolution consistently yields the strongest results—an indication that this high-frequency setting captures the greatest degree of exploitable price predictability. Indeed, we also find exceptionally high correlations in sub-200ms intervals; however, such ultrafast trading windows may be beyond the practical reach of many market participants, as most large pretrained time series models can be efficiently inferenced on GPUs in under a second (Ekambaram et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib20)). Consequently, we adopt 1s as the standard resolution for subsequent experiments, this resolution strikes a balance between practical execution and capturing meaningful intraday signals, plus enabling a consistent comparison between equity and crypto strategies within a unified time scale.

### 4.2. Risk–Return Clustering and Foundation Sharpe Ratio

We next investigate how a broad family of fine‐tuned strategies derived from distinct foundation models distribute in the risk–return space. We also estimate the Pretrained Market Line (PML) slope, which we refer to as the Foundation Sharpe Ratio, using our uncertainty disentanglement approach.

In this study, we assess five representative pretrained time series architectures—namely TimesFM, Timer, Moirai, Chronos, and TTM—alongside conventional baselines (LSTM, SFM, GRU, ALSTM, and MLP). Each model is either freshly trained or fine-tuned on 1s dataset. To capture a variety of trading behaviors, we then randomize key hyperparameter settings (signal thresholds, stop‐losses, take‐profit levels, etc.), thus generating a diverse spectrum of single‐asset strategies. For each resulting strategy, we record two primary metrics over the backtest window:

* •

  Mean daily return E​[rs]E[r\_{s}]333Specifically, a strategy is applied to each asset (SPY and Russell 2000) using an identical bet size, record the resulting returns, and then average these returns to obtain an overall performance measure.
* •

  Volatility of returns σs\sigma\_{s}, (as a proxy for strategy risk)

This setup yields a large collection of (σs,E​[rs])(\sigma\_{s},E[r\_{s}]) pairs, laying the foundation for our subsequent analysis of risk–return relationships under different pretrained architectures.

[3(a)](https://arxiv.org/html/2510.17165v1#S4.F3.sf1 "3(a) ‣ Figure 3 ‣ 4.1. Preliminary : Raw Predictive Performance at Multiple Resolutions ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies") illustrates the resulting risk–return scatter, where each point corresponds to a unique hyperparameter configuration based on tested bases models (θTimesFM\theta\_{\mathrm{TimesFM}}, θTimer\theta\_{\mathrm{Timer}}, θMoirai\theta\_{\mathrm{Moirai}}, θChronos\theta\_{\mathrm{Chronos}}, θTTM\theta\_{\mathrm{TTM}}). Notably, the strategies built upon pretrained foundation models (denoted by colored markers) exhibit a markedly tighter clustering relative to the conventional baselines (represented by grey markers), which are more loosely dispersed across the risk–return plane. This phenomenon suggests that the common informational baseline imposed by the pretrained model tends to homogenize the risk–return characteristics of its fine‐tuned strategies, whereas conventional methods, lacking such a unifying signal, display greater heterogeneity in performance. Moreover, there is non‐trivial overlap among different foundation models themselves, suggesting commonalities in their signals—indeed, multiple large‐scale architectures appear to exploit related market dynamics, which leads to partially correlated outcomes across families.

[3(b)](https://arxiv.org/html/2510.17165v1#S4.F3.sf2 "3(b) ‣ Figure 3 ‣ 4.1. Preliminary : Raw Predictive Performance at Multiple Resolutions ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies") zooms in on a single architecture (Chronos) at different model scales (8M to 710M parameters). Larger versions of Chronos systematically shift the cluster left‐upwards—i.e., toward reduced volatility and increased mean return—demonstrating that scaling can materially enhance the quality of the learned signals. However, when combined with the latency‐sensitive nature of these generative signals (Section 4.1), scaling up parameters also increases inference times—particularly significant in high‐frequency contexts—thereby introducing a trade‐off between model capacity and execution speed. Addressing this tension in a systematic manner remains an important open question for future research.

To quantify how much of each strategy’s variance is actually priced by the pretrained signals, we apply Monte Carlo Dropout to separate total risk into epistemic (foundation‐model) and aleatory components. In line with prevailing short‐term U.S. Treasury yields for given period, we fix the risk‐free rate rfr\_{f} at 5%, then regress each configuration’s expected daily return on its aleatory volatility. This approach yields Foundation Sharpe ratio, interpreted as the slope of the PML. As shown in [Table 2](https://arxiv.org/html/2510.17165v1#S4.T2 "Table 2 ‣ 4.2. Risk–Return Clustering and Foundation Sharpe Ratio ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies"), the PML slope regression are unstable for tested conventional baselines, suggesting that our notion of “shared risk” is not universally applicable—rather, it becomes most evident in pretrained architectures where common signals genuinely dominate the risk–return profile.

Table 2. Foundation Sharpe Ratios

|  |  |  |  |
| --- | --- | --- | --- |
|  | Model | SRθ\mathrm{SR}\_{\theta} | R² |
| Baseline | LSTM | 3.44±0.593.44\pm 0.59 | 0.30 |
| Models | ALSTM | 3.19±0.393.19\pm 0.39 | 0.47 |
|  | MLP | 1.73±0.371.73\pm 0.37 | 0.23 |
|  | SFM | 2.85±0.712.85\pm 0.71 | 0.17 |
|  | GRU | 2.77±0.652.77\pm 0.65 | 0.19 |
| Foundation | TimesFM-v2 | 3.87±0.183.87\pm 0.18 | 0.86 |
| Models | Moirai | 3.39±0.163.39\pm 0.16 | 0.86 |
|  | Chronos | 3.31±0.173.31\pm 0.17 | 0.83 |
|  | Timer | 2.77±0.162.77\pm 0.16 | 0.80 |
|  | TTM | 2.41±0.172.41\pm 0.17 | 0.72 |

### 4.3. Foundation Model Decay

Finally, we turn our attention to alpha decay—the gradual erosion of excess returns that many widely-used investment strategies experience over time, particularly once they become public knowledge(Grinold and Kahn, [2000](https://arxiv.org/html/2510.17165v1#bib.bib26); Pénasse, [2022](https://arxiv.org/html/2510.17165v1#bib.bib46)). It remains an open question whether foundation-model-based approaches are similarly vulnerable.

If we posit that the sharpe ratio estimated from our PML framework reflects the model’s theoretical limit under optimal fine-tuning, then tracking how this ratio evolves can shed light on how swiftly a foundation model’s signals deteriorate once they become assimilated by the market or outperformed by newer adaptations.

To investigate this question, we re‐fine‐tune a single TimesFM‐v1 model weekly, each time using the most recent 12 months of data. We then backtest the updated strategy at 1s resolution and apply rolling‐window PML estimation to obtain both the observed Sharpe ratio, SRθs\mathrm{SR}\_{\theta\_{s}}, and the theoretical upper bound, SRθ\mathrm{SR}\_{\theta}. In [Figure 4](https://arxiv.org/html/2510.17165v1#S4.F4 "Figure 4 ‣ 4.3. Foundation Model Decay ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies") below, we also highlight the official publication dates of TimesFM‐v1 and its successor, TimesFM‐v2, to examine whether broader market awareness of these foundation‐model techniques materially affects strategy performance.

![Refer to caption](x6.png)


Figure 4. Rolling‐window Sharpe ratios for a TimesFM‐v1‐based strategy, re‐fine‐tuned weekly, from early 2023 to early 2025. The maroon curve ( SR​θs\mathrm{SR}{\theta\_{s}} ) represents the observed performance, while the gold curve ( SRθ\mathrm{SR}\_{\theta} ) reflects the theoretical upper bound from PML estimation. Vertical dashed lines denote the public release dates of TimesFM‐v1 and TimesFM‐v2.††:

From early 2023 to early 2025, both SRθ\mathrm{SR}\_{\theta} and SRθs\mathrm{SR}\_{\theta\_{s}} show a steady decline, hinting that alpha potential (even under optimal tuning) erodes as the market assimilates foundation‐model‐derived signals. This assimilation is further exacerbated by competitors employing more advanced fine‐tuning and execution methods, causing the gap SRθ−SRθs\mathrm{SR}\_{\theta}-\mathrm{SR}\_{\theta\_{s}} to widen. Interestingly, neither the publication of TimesFM‐v1 nor TimesFM‐v2 immediately produces an abrupt change; the overall downward trend remains consistent, underscoring a gradual but persistent decay in alpha once a foundation model’s edge becomes widely recognized.

Hence, while the ideal returns of foundation‐based trading diminish in tandem with increased market adoption, practical implementations can erode even faster in real‐world conditions. These findings underscore the dynamic nature of alpha generation: any early advantage secured by cutting‐edge foundation models tends to dissipate rapidly as the market refines and extends these strategies.

## 5. Limitations and Future Directions

Below we highlight three key areas where our current work can be further expanded:

Multivariate Forecasting and Portfolio‐Level Strategies. Although our framework theoretically accommodates multi‐asset settings, our experiments focus on single‐asset strategies to maintain clarity. Extending to cross‐asset interactions and portfolio‐level decision‐making remains to be tested and could validate whether our CAPM‐inspired decomposition truly holds at scale. Such an expansion would also illuminate how systematic and idiosyncratic risks propagate across a diverse basket of instruments.

Latency–Scaling Trade‐Offs and Lightweight Architectures. As shown in [3(b)](https://arxiv.org/html/2510.17165v1#S4.F3.sf2 "3(b) ‣ Figure 3 ‣ 4.1. Preliminary : Raw Predictive Performance at Multiple Resolutions ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies") and [Figure 2](https://arxiv.org/html/2510.17165v1#acmlabel2 "Figure 2 ‣ 4.1. Preliminary : Raw Predictive Performance at Multiple Resolutions ‣ 4. Experiments ‣ Trading with the Devil: Risk and Return in Foundation Model Strategies"), while larger foundation models generally exhibit stronger predictive signals, they also increase inference latency, potentially negating gains in fast‐moving markets. Future research might investigate quantization, distillation, or pruning strategies to retain model quality in sub‐second environments. Balancing parameter scale against speed and execution costs is a pressing challenge with direct practical implications.

Deeper Insights into Shared Risk Factors. We treated each family of foundation models independently, yet the overlap in risk–return clusters suggests broader shared factors. Investigating cross‐model correlations could reveal more universal risk drivers, shaping an enhanced perspective of how foundation‐model‐derived signals collectively reshape market dynamics.

## 6. Related Work

### 6.1. Financial Risk Management

Financial risk management broadly involves safeguarding an organization’s or investment’s assets from losses arising out of uncertainties such as interest rate fluctuations, market volatility, credit risks, and operational failures (Aven, [2016](https://arxiv.org/html/2510.17165v1#bib.bib5)). Its primary goal is to anticipate these potential threats and mitigate them proactively, ensuring that long-term financial objectives remain attainable.

Value-at-Risk (VaR), first introduced by J.P. Morgan, has long been the de facto standard for financial risk management(Simons, [1996](https://arxiv.org/html/2510.17165v1#bib.bib52)) despite well-known limitations such as its non-subadditivity and the assumption of normality (Derman, [1996](https://arxiv.org/html/2510.17165v1#bib.bib18); Berkowitz et al., [2011](https://arxiv.org/html/2510.17165v1#bib.bib6)). Various advances build on VaR to address these shortcomings, including Modified VaR (Favre and Galeano, [2002](https://arxiv.org/html/2510.17165v1#bib.bib22)) and Expected Shortfall (Acerbi and Tasche, [2002](https://arxiv.org/html/2510.17165v1#bib.bib2)). Meanwhile, a different lineage of work adopts Bayesian modeling approaches (Borison, [2010](https://arxiv.org/html/2510.17165v1#bib.bib7); Lynch, [2007](https://arxiv.org/html/2510.17165v1#bib.bib34)), asserting that subjective priors can yield superior insight into tail events. Hybrid frameworks integrating Bayesian inference with VaR (Hoogerheide and van Dijk, [2010](https://arxiv.org/html/2510.17165v1#bib.bib29); Aussenegg and Miazhynskaia, [2006](https://arxiv.org/html/2510.17165v1#bib.bib4)) further expand the methodological toolkit by updating VaR estimates based on posterior distributions rather than point estimates.

Beyond specific risk modeling approaches, model risk looms large because risk cannot be directly measured but must be statistically estimated, giving rise to specification and estimation errors (Derman, [1996](https://arxiv.org/html/2510.17165v1#bib.bib18); Morini, [2011](https://arxiv.org/html/2510.17165v1#bib.bib39)). Disagreements between candidate models tend to magnify during market distress, frustrating confidence in any single risk reading (Danielsson et al., [2016](https://arxiv.org/html/2510.17165v1#bib.bib11)). In practice, therefore, risk managers often combine multiple risk measures, conduct regular stress testing, and follow ongoing validation procedures as critical lines of defense against potential model failures (Darbyshire and Hampton, [2012](https://arxiv.org/html/2510.17165v1#bib.bib12); US Federal Reserve and Office of the Comptroller of the Currency, [2011](https://arxiv.org/html/2510.17165v1#bib.bib55)).

### 6.2. Uncertainty Modeling for ML

The idea of representing uncertainty traces back to the roots of Bayesian inference, where the primary goal is to model unknowns probabilistically rather than rely on point estimates. In the context of neural networks, pioneers like MacKay (MacKay, [1992](https://arxiv.org/html/2510.17165v1#bib.bib35)) and Neal (Neal, [2012](https://arxiv.org/html/2510.17165v1#bib.bib43)) advocated using Bayesian principles to capture the posterior over model parameters, producing uncertainty estimates alongside predictions. As deep learning grew, these ideas transitioned into practical methods to quantify uncertainty in large‐scale models. Notable distributional approaches include MC Dropout (Gal and Ghahramani, [2016](https://arxiv.org/html/2510.17165v1#bib.bib24)), which uses stochastic dropout at test time to approximate a Bayesian ensemble, and Deep Ensembles (Lakshminarayanan et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib31)), where multiple independently trained networks capture model variability. More recent refinements—such as SNGP (Liu et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib32)), SWAG (Maddox et al., [2019](https://arxiv.org/html/2510.17165v1#bib.bib36)), Laplace approximations (Daxberger et al., [2021](https://arxiv.org/html/2510.17165v1#bib.bib14)), and Evidential Deep Learning (Sensoy et al., [2018](https://arxiv.org/html/2510.17165v1#bib.bib49))—explicitly model a second‐order predictive distribution over class probabilities and then aggregate those into scalar uncertainties. Alongside these, deterministic methods(DUQ(Van Amersfoort et al., [2020](https://arxiv.org/html/2510.17165v1#bib.bib56)), DDU(Mukhoti et al., [2023](https://arxiv.org/html/2510.17165v1#bib.bib41)), Tempreture Scaling(Guo et al., [2017](https://arxiv.org/html/2510.17165v1#bib.bib27))) have emerged that directly predict a single scalar uncertainty without modeling a full posterior distribution.

While classical Bayesian theory primarily yielded one overall measure of uncertainty, proposed technique like information‐theoretical (Depeweg et al., [2018](https://arxiv.org/html/2510.17165v1#bib.bib16)) and Bregman decompositions (Wimmer et al., [2023](https://arxiv.org/html/2510.17165v1#bib.bib57)) trys to disentangling it into finer sources: aleatoric (irreducible data‐inherent noise) and epistemic (model uncertainty due to limited or imperfect training data). However, recent benchmark (Mucsányi et al., [2024](https://arxiv.org/html/2510.17165v1#bib.bib40)) suggest that these disentanglements often remain highly correlated, highlighting the need for specialized uncertainties tailored to specific tasks.

Thus, in our paper, the CAPM-style risk analysis provides a financial treatment of disentangling foundation models’ uncertainty.

## 7. Conclusion

In conclusion, this work adapted CAPM principles to foundation‐model‐based trading by aligning the model’s epistemic and idiosyncratic uncertainties with the familiar decomposition of market‐wide versus asset‐specific exposures. By leveraging Monte Carlo dropout on large time‐series models for trading U.S. equities and cryptocurrencies, we disentangled the truly priced risk inherent in the pretrained architecture from the unpriced variance introduced by suboptimal fine‐tuning. Our findings show that this shared model‐driven uncertainty closely mirrors CAPM’s concept of systemic risk, providing clearer insights into trading strategies’ risk–return profiles and highlighting how alpha can deteriorate as more market participants adopt these powerful pretrained signals.

## References

* (1)
* Acerbi and Tasche (2002)

  Carlo Acerbi and Dirk Tasche. 2002.
  Expected shortfall: a natural coherent alternative to value at risk.
  *Economic notes* 31, 2 (2002), 379–388.
* Ansari et al. (2024)

  Abdul Fatir Ansari, Lorenzo Stella, Ali Caner Turkmen, Xiyuan Zhang, Pedro Mercado, Huibin Shen, Oleksandr Shchur, Syama Sundar Rangapuram, Sebastian Pineda Arango, Shubham Kapoor, Jasper Zschiegner, Danielle C. Maddix, Hao Wang, Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson, Michael Bohlke-Schneider, and Bernie Wang. 2024.
  Chronos: Learning the Language of Time Series.
  *Transactions on Machine Learning Research* abs/2403.07815 (2024).
* Aussenegg and Miazhynskaia (2006)

  Wolfgang Aussenegg and Tatiana Miazhynskaia. 2006.
  Uncertainty in value-at-risk estimates under parametric and non-parametric modeling.
  *Financial Markets and Portfolio Management* 20 (2006), 243–264.
* Aven (2016)

  Terje Aven. 2016.
  Risk assessment and risk management: Review of recent advances on their foundation.
  *European Journal of Operational Research* 253, 1 (2016), 1–13.
* Berkowitz et al. (2011)

  Jeremy Berkowitz, Peter Christoffersen, and Denis Pelletier. 2011.
  Evaluating value-at-risk models with desk-level data.
  *Management Science* 57, 12 (2011), 2213–2227.
* Borison (2010)

  Adam Borison. 2010.
  How to manage risk (after risk management has failed).
  *MIT Sloan Management Review* (2010).
* Boucher et al. (2014)

  Christophe M. Boucher, Jón Daníelsson, Patrick S. Kouontchou, and Bertrand B. Maillet. 2014.
  Risk models-at-risk.
  *Journal of Banking & Finance* 44 (2014), 72–92.
* Cao (2023)

  Longbing Cao. 2023.
  AI in Finance: Challenges, Techniques, and Opportunities.
  *Comput. Surveys* 55, 3 (2023), 64:1–64:38.
* Chauhan et al. (2020)

  Lakshay Chauhan, John Alberg, and Zachary C. Lipton. 2020.
  Uncertainty-Aware Lookahead Factor Models for Quantitative Investing.. In *International Conference on Machine Learning (ICML)*. 1489–1499.
* Danielsson et al. (2016)

  Jon Danielsson, Kevin R. James, Marcela Valenzuela, and Ilknur Zer. 2016.
  Model risk of risk models.
  *Journal of Financial Stability* 23 (2016), 79–91.
* Darbyshire and Hampton (2012)

  Paul Darbyshire and David Hampton. 2012.
  *Hedge fund modelling and analysis using Excel and VBA*.
  John Wiley & Sons.
* Das et al. (2024)

  Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. 2024.
  A decoder-only foundation model for time-series forecasting. In *International Conference on Machine Learning*, Vol. abs/2310.10688.
* Daxberger et al. (2021)

  Erik Daxberger, Agustinus Kristiadi, Alexander Immer, Runa Eschenhagen, Matthias Bauer, and Philipp Hennig. 2021.
  Laplace redux-effortless bayesian deep learning.
  *Advances in Neural Information Processing Systems* 34 (2021), 20089–20103.
* Deng et al. (2017)

  Yue Deng, Feng Bao, Youyong Kong, Zhiquan Ren, and Qionghai Dai. 2017.
  Deep Direct Reinforcement Learning for Financial Signal Representation and Trading.
  *IEEE Transactions on Neural Networks and Learning Systems* 28, 3 (2017), 653–664.
* Depeweg et al. (2018)

  Stefan Depeweg, Jose-Miguel Hernandez-Lobato, Finale Doshi-Velez, and Steffen Udluft. 2018.
  Decomposition of uncertainty in Bayesian deep learning for efficient and risk-sensitive learning. In *International conference on machine learning*. PMLR, 1184–1193.
* Der Kiureghian and Ditlevsen (2009)

  Armen Der Kiureghian and Ove Ditlevsen. 2009.
  Aleatory or epistemic? Does it matter?
  *Structural safety* 31, 2 (2009), 105–112.
* Derman (1996)

  Emanuel Derman. 1996.
  Model Risk.
  *Quantitative Strategies Research Notes* (April 1996).
* Ding et al. (2020)

  Qianggang Ding, Sifan Wu, Hao Sun, Jiadong Guo, and Jian Guo. 2020.
  Hierarchical Multi-Scale Gaussian Transformer for Stock Movement Prediction.. In *International Joint Conference on Artificial Intelligence (IJCAI)*. 4640–4646.
* Ekambaram et al. (2024)

  Vijay Ekambaram, Arindam Jati, Pankaj Dayama, Sumanta Mukherjee, Nam Nguyen, Wesley M Gifford, Chandra Reddy, and Jayant Kalagnanam. 2024.
  Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series. In *Advances in Neural Information Processing Systems*, Vol. 37. Curran Associates, Inc., 74147–74181.
* Fama and French (2004)

  Eugene F Fama and Kenneth R French. 2004.
  The Capital Asset Pricing Model: Theory and Evidence.
  *Journal of Economic Perspectives* 18, 3 (2004), 25–46.
* Favre and Galeano (2002)

  Laurent Favre and José-Antonio Galeano. 2002.
  Mean-modified value-at-risk optimization with hedge funds.
  *Journal of Alternative Investments* 5, 2 (2002), 21–25.
* Fu et al. (2024)

  Xinghong Fu, Masanori Hirano, and Kentaro Imajo. 2024.
  Financial Fine-tuning a Large Time Series Model.
  *arXiv* (2024).
* Gal and Ghahramani (2016)

  Yarin Gal and Zoubin Ghahramani. 2016.
  Dropout as a bayesian approximation: Representing model uncertainty in deep learning. In *international conference on machine learning*. PMLR, 1050–1059.
* Goodhart (1984)

  C. A. E. Goodhart. 1984.
  *Problems of Monetary Management: The UK Experience*.
  Macmillan Education UK. 91–121 pages.
* Grinold and Kahn (2000)

  Richard C. Grinold and Ronald N. Kahn. 2000.
  *Active Portfolio Management: A Quantitative Approach for Providing Superior Returns and Controlling Risk* (2nd ed.).
  McGraw-Hill, New York.
* Guo et al. (2017)

  Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q Weinberger. 2017.
  On calibration of modern neural networks. In *International conference on machine learning*. PMLR, 1321–1330.
* Hajj and Hammoud (2023)

  Mohammad El Hajj and Jamil Hammoud. 2023.
  Unveiling the Influence of Artificial Intelligence and Machine Learning on Financial Markets: A Comprehensive Analysis of AI Applications in Trading, Risk Management, and Financial Operations.
  *Journal of Risk and Financial Management* 16, 10 (2023), 434.
* Hoogerheide and van Dijk (2010)

  Lennart Hoogerheide and Herman K van Dijk. 2010.
  Bayesian forecasting of value at risk and expected shortfall using adaptive importance sampling.
  *International Journal of Forecasting* 26, 2 (2010), 231–247.
* Hora (1996)

  Stephen C. Hora. 1996.
  Aleatory and epistemic uncertainty in probability elicitation with an example from hazardous waste management.
  *Reliability Engineering & System Safety* 54 (1996), 217–223.
* Lakshminarayanan et al. (2017)

  Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. 2017.
  Simple and scalable predictive uncertainty estimation using deep ensembles.
  *Advances in neural information processing systems* 30 (2017).
* Liu et al. (2020)

  Jeremiah Liu, Zi Lin, Shreyas Padhy, Dustin Tran, Tania Bedrax Weiss, and Balaji Lakshminarayanan. 2020.
  Simple and principled uncertainty estimation with deterministic deep learning via distance awareness.
  *Advances in neural information processing systems* 33 (2020), 7498–7512.
* Liu et al. (2024)

  Yong Liu, Haoran Zhang, Chenyu Li, Xiangdong Huang, Jianmin Wang, and Mingsheng Long. 2024.
  Timer: Generative Pre-trained Transformers Are Large Time Series Models. In *International Conference on Machine Learning*.
* Lynch (2007)

  Scott M Lynch. 2007.
  *Introduction to applied Bayesian statistics and estimation for social scientists*. Vol. 1.
  Springer.
* MacKay (1992)

  David J. C. MacKay. 1992.
  A Practical Bayesian Framework for Backpropagation Networks.
  *Neural Computation* 4, 3 (1992), 448–472.
* Maddox et al. (2019)

  Wesley J Maddox, Pavel Izmailov, Timur Garipov, Dmitry P Vetrov, and Andrew Gordon Wilson. 2019.
  A simple baseline for bayesian uncertainty in deep learning.
  *Advances in neural information processing systems* 32 (2019).
* Malibari et al. (2021)

  Nadeem Malibari, Iyad Katib, and Rashid Mehmood. 2021.
  Predicting Stock Closing Prices in Emerging Markets with Transformer Neural Networks: The Saudi Stock Exchange Case.
  *International Journal of Advanced Computer Science and Applications* 12, 12 (2021).
* Markowitz (1952)

  Harry Markowitz. 1952.
  Portfolio Selection.
  *The Journal of Finance* 7, 1 (1952), 77–91.
  [doi:10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)
* Morini (2011)

  Massimo Morini. 2011.
  *Understanding and Managing Model Risk: A practical guide for quants, traders and validators*.
  John Wiley & Sons.
* Mucsányi et al. (2024)

  Bálint Mucsányi, Michael Kirchhof, and Seong Joon Oh. 2024.
  Benchmarking uncertainty disentanglement: Specialized uncertainties for specialized tasks.
  *arXiv preprint arXiv:2402.19460* (2024).
* Mukhoti et al. (2023)

  Jishnu Mukhoti, Andreas Kirsch, Joost van Amersfoort, Philip HS Torr, and Yarin Gal. 2023.
  Deep deterministic uncertainty: A new simple baseline. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 24384–24394.
* Naeini et al. (2010)

  Mahdi Pakdaman Naeini, Hamid Reza Taremian, and Homa Baradaran Hashemi. 2010.
  Stock market value prediction using neural networks.. In *International Conference on Computer Information Systems and Industrial Management (CISIM)*. 132–136.
* Neal (2012)

  Radford M Neal. 2012.
  *Bayesian learning for neural networks*. Vol. 118.
  Springer Science & Business Media.
* Nelson et al. (2017)

  David M. Q. Nelson, Adriano C. M. Pereira, and Renato A. de Oliveira. 2017.
  Stock market’s price movement prediction with LSTM neural networks.. In *IEEE International Joint Conference on Neural Network (IJCNN)*. 1419–1426.
* Nti et al. (2020)

  Isaac Kofi Nti, Adebayo Felix Adekoya, and Benjamin Asubam Weyori. 2020.
  A comprehensive evaluation of ensemble learning for stock-market prediction.
  *Journal of Big Data* 7, 1 (2020), 20.
* Pénasse (2022)

  Julien Pénasse. 2022.
  Understanding alpha decay.
  *Management Science* 68, 5 (2022), 3966–3973.
* Qin et al. (2017)

  Yao Qin, Dongjin Song, Haifeng Chen, Wei Cheng, Guofei Jiang, and Garrison W. Cottrell. 2017.
  A Dual-Stage Attention-Based Recurrent Neural Network for Time Series Prediction.. In *International Joint Conference on Artificial Intelligence (IJCAI)*. 2627–2633.
* Selvin et al. (2017)

  Sreelekshmy Selvin, R Vinayakumar, E. A Gopalakrishnan, Vijay Krishna Menon, and K. P. Soman. 2017.
  Stock price prediction using LSTM, RNN and CNN-sliding window model.
  *2017 International Conference on Advances in Computing, Communications and Informatics (ICACCI)* (2017).
* Sensoy et al. (2018)

  Murat Sensoy, Lance Kaplan, and Melih Kandemir. 2018.
  Evidential deep learning to quantify classification uncertainty.
  *Advances in neural information processing systems* 31 (2018).
* Sharpe (1964)

  William F. Sharpe. 1964.
  CAPITAL ASSET PRICES: A THEORY OF MARKET EQUILIBRIUM UNDER CONDITIONS OF RISK.
  *The Journal of Finance* 19, 3 (1964), 425–442.
* Shen et al. (2018)

  Guizhu Shen, Qingping Tan, Haoyu Zhang, Ping Zeng, and Jianjun Xu. 2018.
  Deep Learning with Gated Recurrent Unit Networks for Financial Sequence Predictions.
  *Procedia Computer Science* 131 (2018), 895–903.
* Simons (1996)

  Katerina Simons. 1996.
  Value at risk-new approaches to risk management.
  *New England Economic Review* (1996), 3–14.
* Sun et al. (2022)

  Shuo Sun, Rundong Wang, and Bo An. 2022.
  Quantitative stock investment by routing uncertainty-aware trading experts: A multi-task learning approach.
  *arXiv preprint arXiv:2207.07578* (2022).
* Sun et al. (2023)

  Shuo Sun, Xinrun Wang, Wanqi Xue, Xiaoxuan Lou, and Bo An. 2023.
  Mastering Stock Markets with Efficient Mixture of Diversified Trading Experts. In *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*. ACM, 2109–2119.
* US Federal Reserve and Office of the Comptroller of the Currency (2011)

  US Federal Reserve and Office of the Comptroller of the Currency. 2011.
  *Supervisory Guidance On Model Risk Management*.
  Technical Report SR Letter 11-7 / OCC 2011-12. Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency.
* Van Amersfoort et al. (2020)

  Joost Van Amersfoort, Lewis Smith, Yee Whye Teh, and Yarin Gal. 2020.
  Uncertainty estimation using a single deep deterministic neural network. In *International conference on machine learning*. PMLR, 9690–9700.
* Wimmer et al. (2023)

  Lisa Wimmer, Yusuf Sale, Paul Hofman, Bernd Bischl, and Eyke Hüllermeier. 2023.
  Quantifying aleatoric and epistemic uncertainty in machine learning: Are conditional entropy and mutual information appropriate measures?. In *Uncertainty in Artificial Intelligence*. PMLR, 2282–2292.
* Woo et al. (2024)

  Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, and Doyen Sahoo. 2024.
  Unified Training of Universal Time Series Forecasting Transformers. In *Forty-first International Conference on Machine Learning*, Vol. abs/2402.02592.
* Wu et al. (2023)

  Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhanjan Kambadur, David Rosenberg, and Gideon Mann. 2023.
  BloombergGPT: A Large Language Model for Finance.
  *ArXiv* abs/2303.17564 (2023).
* Yang et al. (2023)

  Hongyang Yang, Xiao-Yang Liu, and Chris Wang. 2023.
  FinGPT: Open-Source Financial Large Language Models.
  *ArXiv* abs/2306.06031 (2023).
* Yang et al. (2020)

  Hongyang Yang, Xiao-Yang Liu, Shan Zhong, and Anwar Walid. 2020.
  Deep reinforcement learning for automated stock trading: an ensemble strategy.. In *International Conference on AI in Finance (ICAIF)*. 31:1–31:8.
* Zhang et al. (2017)

  Liheng Zhang, Charu C. Aggarwal, and Guo-Jun Qi. 2017.
  Stock Price Prediction via Discovering Multi-Frequency Trading Patterns.. In *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)*. 2141–2149.
* Zhang et al. (2020)

  Zihao Zhang, Stefan Zohren, and Stephen Roberts. 2020.
  Deep Learning for Portfolio Optimization.
  *The Journal of Financial Data Science* (2020).
* Zhong et al. (2020)

  Yueyang Zhong, YeeMan Bergstrom, and Amy R. Ward. 2020.
  Data-Driven Market-Making via Model-Free Learning.. In *International Joint Conference on Artificial Intelligence (IJCAI)*. 4461–4468.