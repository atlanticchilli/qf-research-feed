---
authors:
- Brian Ezinwoke
- Oliver Rhodes
doc_id: arxiv:2512.05868v1
family_id: arxiv:2512.05868
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Predicting Price Movements in High-Frequency Financial Data with Spiking Neural
  Networks
url_abs: http://arxiv.org/abs/2512.05868v1
url_html: https://arxiv.org/html/2512.05868v1
venue: arXiv q-fin
version: 1
year: 2025
---


Brian Ezinwoke1, Oliver Rhodes1
1Department of Computer Science, University of Manchester, UK

###### Abstract

Modern high-frequency trading (HFT) environments are characterized by sudden price spikes that present both risk and opportunity, but conventional financial models often fail to capture the required fine temporal structure. Spiking Neural Networks (SNNs) offer a biologically inspired framework well-suited to these challenges due to their natural ability to process discrete events and preserve millisecond-scale timing. This work investigates the application of SNNs to high-frequency price-spike forecasting, enhancing performance via robust hyperparameter tuning with Bayesian Optimization (BO). This work converts high-frequency stock data into spike trains and evaluates three architectures: an established unsupervised STDP-trained SNN, a novel SNN with explicit inhibitory competition, and a supervised backpropagation network. BO was driven by a novel objective, Penalized Spike Accuracy (PSA), designed to ensure a network’s predicted price spike rate aligns with the empirical rate of price events. Simulated trading demonstrated that models optimized with PSA consistently outperformed their Spike Accuracy (SA)-tuned counterparts and baselines. Specifically, the extended SNN model with PSA achieved the highest cumulative return (76.8%) in simple backtesting, significantly surpassing the supervised alternative (42.5% return). These results validate the potential of spiking networks, when robustly tuned with task-specific objectives, for effective price spike forecasting in HFT.

## I Introduction

High Frequency Trading (HFT) involves automated execution of trades on microsecond timescales, relying on tick data and adhering to extreme latency constraints [kohda2021hft, Gao2023]. Financial time series data are inherently difficult due to non-stationarity (statistical properties change over time) [KimTaeYoon2004Annf], which makes models vulnerable to concept drift [sezer2020financial]. They also exhibit volatility clustering and heavy-tailed distributions, indicating frequent extreme events and noise [Chakraborti, Gao2023].

Spiking Neural Networks (SNNs) offer a compelling solution for this domain [Lobo2020, Yamazaki2022]. They process information using discrete binary activations (spikes), naturally preserving the fine temporal dynamics essential for detecting significant movements in financial time series[Gao2023] . This sparse computation yields inherent low latency and energy efficiency compared to dense Artificial Neural Networks (ANNs) [tavanaei2018deep, Gao2023, davidson2021digital], especially on neuromorphic hardware.

However, a significant hurdle in training SNNs is the lack of a proven learning algorithm capable of extracting these temporal properties in real-world applications. The firing of a spiking neuron is a threshold-based, discontinuous event [Eshraghian2023, Roy2019], which complicates the direct application of gradient-based optimisation used in ANNs [KozdonThesis2018, Eshraghian2023]. To enable gradient descent training in multi-layer SNNs, surrogate gradient methods have become crucial [Roy2019]. These methods replace the discontinuous activation function with a smooth, differentiable surrogate during the backward pass [Eshraghian2023, Roy2019], allowing weight updates via backpropagation-like mechanisms [Eshraghian2023, Roy2019]. While successful for deep SNNs, these methods lack biological plausibility and fast online learning capabilities.

This work focuses on training models using an unsupervised learning rule based on Spike-Timing-Dependent-Plasticity (STDP), a mechanism where synaptic strength (Δ​w\Delta w) is modified by the relative timing (Δ​t\Delta t) of pre- and postsynaptic spikes [Gerstner1996, Hebb1949, Bi1998]. Specifically, a presynaptic spike preceding a postsynaptic spike causes strengthening (LTP), while the reverse causes weakening (LTD) [KozdonThesis2018]. The magnitude and direction of Δ​w\Delta w are determined by a learning window, W​(Δ​t)W(\Delta t) [KozdonThesis2018]. A common mathematical formulation of the STDP learning window is the exponential window [Gao2023]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​w=η⋅W​(Δ​t)={A+​exp⁡(−Δ​t/τ+)if ​Δ​t>0−A−​exp⁡(Δ​t/τ−)if ​Δ​t<00otherwise   \Delta w=\eta\cdot W(\Delta t)=\begin{cases}A\_{+}\exp(-\Delta t/\tau\_{+})&\text{if }\Delta t>0\\ -A\_{-}\exp(\Delta t/\tau\_{-})&\text{if }\Delta t<0\\ 0&\text{otherwise }\end{cases} |  | (1) |

where A+A\_{+} and A−A\_{-} are the maximum learning rates for potentiation and depression, respectively (with A−≤A+A\_{-}\leq A\_{+}); τ+\tau\_{+} and τ−\tau\_{-} are the corresponding time constants defining the temporal window; and η\eta is a learning rate parameter, typically set to 11 [KozdonThesis2018].

STDP-trained SNNs are highly sensitive to their many hyperparameters (Eq. [1](https://arxiv.org/html/2512.05868v1#S1.E1 "In I Introduction ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks") and neuronal dynamics). Therefore, a robust hyperparameter search method is necessary. Bayesian optimisation (BO) is a probabilistic model-based approach designed to optimise computationally expensive functions, such as model validation performance [frazier2018bayesian]. Unlike grid or random search, BO uses the results of previous evaluations to inform the choice of the next hyperparameters, efficiently finding the optimal configuration with fewer evaluations [bergstra2013hyperparams]. In this paper, BO is used to optimise model and learning algorithm parameters in tandem.

Reid, Hussain, and Tawfik (2014) introduced Polychronous Spiking Networks (PSNs), leveraging their intrinsic temporal capabilities for general financial time series prediction [Reid2013]. Benchmarking the PSN against MLPs, DRPNNs, and a linear model, they demonstrated favourable results, confirming the PSN paradigm’s potential in non-stationary environments, though their approach was supervised [Reid2013].

Most relevant to this work is the study by Gao et al. (2021), which specifically targets high-frequency price-spike prediction using SNNs [Gao2023]. Addressing the research gap focused on supervised direction prediction, and proposed a novel method based on unsupervised STDP. This approach enabled the network to become selective to temporal patterns in intra-day data, demonstrating SNN potential for identifying specific events such as price spikes. A limitation noted was the need for improved computational efficiency for ultra-low latency HFT requirements [Gao2023].

To address the challenge of hyperparameter optimisation in SNNs, Parsa et al. (2019) proposed and evaluated a Bayesian-based hyperparameter optimisation framework for neuromorphic systems [parsa2019bayesian]. They highlighted that conventional methods such as grid search are inefficient in the high-dimensional parameter space of SNNs. Their iterative Bayesian methodology significantly streamlined the search process, finding optimal parameters with substantially fewer evaluations (e.g., 400 vs. 24,000 for input encoding), underscoring BO’s utility for complex SNN architectures [parsa2019bayesian].

This work explores the continuation and extension of these concepts, particularly STDP-based unsupervised training for HFT predictions. Specifically, the work contributes:

* •

  Development of an extended SNN integrating temporal features and inhibitory synapses for financial time series prediction.
* •

  Empirical demonstration that unsupervised STDP-trained networks significantly outperform supervised gradient-based methods and baseline strategies in HFT.
* •

  Establishment of a fully reproducible, end-to-end training framework utilizing Bayesian optimisation to achieve fine-grained control over network performance, through hyperparameter optimisation.
* •

  Proposal of a new penalised spike accuracy metric as a target for BO, which was able to outperform the spike accuracy metric proposed by Gao et al.

## II Method

### II-A Data and Preprocessing

High-frequency $AAPL stock price and volume data with microsecond precision from the 19 trading days of February 2015 was used for training and evaluating the model. This dataset provides sufficient granularity to capture the rapid price movements characteristic of HFT environments while maintaining a manageable size for computational efficiency.

The raw price time series cannot be input directly to the SNN as it must first be converted into spike trains. A series of preprocessing steps are conducted as follows.

#### II-A1 Volume Weighted Average Prices

The volume weighted average price (VWAP) is used across all models presented in this paper. For a time period with nn transactions, VWAP is evaluated according to Eqn. [2](https://arxiv.org/html/2512.05868v1#S2.E2 "In II-A1 Volume Weighted Average Prices ‣ II-A Data and Preprocessing ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | VWAP=∑i=1nPi⋅Vi∑i=1nVi\text{VWAP}=\frac{\sum\_{i=1}^{n}P\_{i}\cdot V\_{i}}{\sum\_{i=1}^{n}V\_{i}} |  | (2) |

where PiP\_{i} represents the price of the ii-th transaction, and ViV\_{i} represents its corresponding volume. A window length of n=10n=10 timestamps to average across was selected during this study, effectively reducing overall data size by 90%.

The VWAP conversion serves multiple purposes: smooths the data to eliminate zig-zag noise from bid-ask oscillations; reduces the number of data points, improving computational efficiency; and incorporates volume information, which is economically significant as price changes correlate with trading volume [Gao2023]. Figure [1](https://arxiv.org/html/2512.05868v1#S2.F1 "Figure 1 ‣ II-A1 Volume Weighted Average Prices ‣ II-A Data and Preprocessing ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks"), provides a direct comparison of the raw price time series (left) compared to the smoothed VWAP time series (right). The two panels show the price move for the same contract for the same period, yet the VWAP is visibly smoother and the significant price spikes are more obvious. Note that the horizontal-axis of the left panel is 10 times the x-axis of the right panel since a window length 10 timestamps was used to aggregate the raw price into VWAP [Gao2023].

![Refer to caption](x1.png)


Figure 1: Comparison of the raw transaction price (left) and the VWAP (right).

#### II-A2 Feature Creation

The next step is to select the features necessary to train the SNN models; however, feeding the VWAP directly is insufficient for several reasons. First, there exist day-trend components in price time series which can add noise into the SNN and cause disturbance to the detection of price spikes [Gao2023], as seen in Figure [2](https://arxiv.org/html/2512.05868v1#S2.F2 "Figure 2 ‣ II-A2 Feature Creation ‣ II-A Data and Preprocessing ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks"). Second, the effect of the different price magnitudes cannot be ignored. Large differences between the open and close prices would cause the rate of the generated spike trains in the beginning hour of trading to be higher than the rate at the day’s end. This bias could lead to a systematic difference in spike frequency for different trading hours, and have a negative influence on the performance of an SNN.

The proposed solution to these problems is to take the difference of the prices since price spikes are related only to the price change and not the magnitude [Gao2023]. As seen in Figure [2](https://arxiv.org/html/2512.05868v1#S2.F2 "Figure 2 ‣ II-A2 Feature Creation ‣ II-A Data and Preprocessing ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks"), this removes the trend component and prevents systematic time biases from entering the model. Additional features providing more relative information relating to the price change can also be included, given the trend component is removed by differencing or some other method.

![Refer to caption](x2.png)


Figure 2: Comparison of trend components in price vs. differenced price series using unobserved component analysis (UCA) [durbin2012timeseries][seabold2010statsmodels].

#### II-A3 Normalisation

Before data encoding into spike trains, features are normalised to the range [0,1][0,1]. This range then corresponds to the probability of a spike at a timestamp or the rate parameter for Poisson encoding.

In the unsupervised spike learning method proposed by Gao et al., data is normalised using a variant of min-max z-score normalisation. A normalised feature ziz\_{i} is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi=max⁡{xi−μ𝐱σ𝐱⋅σnorm+μnorm,0}  z\_{i}=\max\{\frac{x\_{i}-\mu\_{\mathbf{x}}}{\sigma\_{\mathbf{x}}}\cdot\sigma\_{\text{norm}}+\mu\_{\text{norm}},0\} |  | (3) |

where xix\_{i} is the ii-th value in the feature vector 𝐱\mathbf{x}, and μ𝐱\mu\_{\mathbf{x}} and σ𝐱\sigma\_{\mathbf{x}} are the mean and standard deviation of 𝐱\mathbf{x}. The parameters μnorm\mu\_{\text{norm}} and σnorm\sigma\_{\text{norm}} are network hyperparameters. This method presents two major challenges.

First, finding optimal μnorm\mu\_{\text{norm}} and σnorm\sigma\_{\text{norm}} is computationally expensive, requiring multiple rounds of data encoding and model training. Poor selection of μnorm\mu\_{\text{norm}} can lead to network over-excitation due to high spiking rates. Likewise, an improper σnorm\sigma\_{\text{norm}} selection can result in a contracted or overly wide data range, either causing all spike trains to be overly similar or causing similar input values to have drastically different spike counts.

Second, the normalisation is significantly affected by outliers (e.g., abnormally large values). If a large outlier exists, most non-outlier data clusters near the new minimum (zero) after scaling. This distortion adversely impacts the predictive performance of the network by obscuring the true information within the time-series data.

To address these issues, an alternative three-step normalisation approach is adopted:

1. 1.

   Robust Scaling & Clipping: Apply robust scaling using the interquartile range (IQR) [0.1,0.9][0.1,0.9]. Values outside this range are clipped to the nearest boundary. This mitigates outlier effects, preventing data clustering near the [0,1][0,1] bounds after subsequent scaling.
2. 2.

   Channel Separation: Split the scaled features into positive and negative channels to represent bipolar data, as Poisson encoding requires non-negative values. The positive (negative) channel retains only the positive (negative) values of the feature vector.
3. 3.

   Min-Max Rescaling: Each channel is transformed to the range [0,1][0,1]. This sets the average spiking rate near 0.50.5 spikes per timestep, balancing network excitation and energy efficiency. To increase sparsity, the upper bound can be lowered such that the range becomes [0,x][0,x] where x<1x<1.

The proposed method is straightforward to implement and eliminates the need for computationally expensive hyperparameter searches to find optimal values of μnorm\mu\_{\text{norm}} and σnorm\sigma\_{\text{norm}}. Additionally it gracefully handles outliers while effectively setting the average spiking rate to an appropriate value.

#### II-A4 Encoding

The final preprocessing step uses Poisson encoding to generate spike trains from the normalised time series data. For a feature vector with values xix\_{i}, a spike train of length TT is generated for all i=1,2,…,Ni=1,2,...,N, following the pseudo-code in Algorithm [1](https://arxiv.org/html/2512.05868v1#alg1 "Algorithm 1 ‣ II-A4 Encoding ‣ II-A Data and Preprocessing ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks"). This is repeated for all KK features, hence the resulting dataset contains KK features, with NN timestamps and TT timesteps per spike train. In total, there are N⋅KN\cdot K spike trains generated.
For the results presented here, TT was chosen to be 20, balancing both encoding precision and computational costs.

Algorithm 1  Generate Poisson Spike Train

0: TT (number of timesteps)

0: xix\_{i} (firing rate)

s​p​i​k​e​T​r​a​i​n←zeros​(T)spikeTrain\leftarrow\text{zeros}(T) {Initialize spike train}

for t=1t=1 to TT do

p←xip\leftarrow x\_{i} {Spike probability in bin}

u∼Uniform​(0,1)u\sim\text{Uniform}(0,1) {Random number}

if u<pu<p then

s​p​i​k​e​T​r​a​i​n​[t]←1spikeTrain[t]\leftarrow 1 {Generate spike}

end if

end for

return s​p​i​k​e​T​r​a​i​nspikeTrain

### II-B Spike Definitions and Predictive Metrics

The concept of “spikes” in this research carries specific technical meaning within the context of unsupervised price-spike learning for financial time series prediction. These definitions provide the framework for evaluating the neural network’s ability to identify significant market events.

#### II-B1 Real vs Fake Price Spikes

A primary distinction in the proposed evaluation framework is between *real* and *fake* price spikes, which determines the fundamental accuracy of the SNN predictions.

A real price spike occurs when the SNN emits a signal that precedes a significant price movement. This significance is quantified by comparing the subsequent price movement to a predefined threshold. Formally, we define the absolute percentage return at time tt as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=|Xt+1Xt−1|,t=1,2,…,n−1r\_{t}=\left|\frac{X\_{t+1}}{X\_{t}}-1\right|,\quad t=1,2,\ldots,n-1 |  | (4) |

where XtX\_{t} represents the volume-weighted average price (VWAP) at time tt. The threshold for determining significance is defined as the median of the intra-day absolute return series:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rthresh=median​(rt),t=1,2,…,n−1r\_{\text{thresh}}=\text{median}(r\_{t}),\quad t=1,2,\ldots,n-1 |  | (5) |

For each price spike signal emitted by the network at time tt, its strength is calculated over a subsequent window, ww, of time:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sstrength=|rt+1|+|rt+2|+…+|rt+w|wS\_{\text{strength}}=\frac{|r\_{t+1}|+|r\_{t+2}|+...+|r\_{t+w}|}{w} |  | (6) |

A price spike is classified as real if Sstrength>rthreshS\_{\text{strength}}>r\_{\text{thresh}}, indicating that the network has identified a price movement of above-median magnitude. All other spikes not meeting this criteria are considered fake spikes.

#### II-B2 Momentum vs Reversion Spikes

Another categorisation of price spikes is based on the directional relationship between the preceding price trend and the subsequent movement. A *momentum spike* occurs when a price movement continues in the same direction as the immediate trend preceding the current price. A *reversion spike* occurs when a real spike is followed by a price movement in the opposite direction to the immediate preceding trend. Mathematically, a real price spike at time tt, is subsequently classified as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Class={Momentum,if ​(Xt−Xt−w)⋅(Xt+w−Xt)>0Reversion,if ​(Xt−Xt−w)⋅(Xt+w−Xt)<0None,otherwise\text{Class}=\begin{cases}\text{Momentum},&\text{if }(X\_{t}-X\_{t-w})\cdot(X\_{t+w}-X\_{t})>0\\ \text{Reversion},&\text{if }(X\_{t}-X\_{t-w})\cdot(X\_{t+w}-X\_{t})<0\\ \text{None},&\text{otherwise}\end{cases} |  | (7) |

where ww represents the window size for trend determination.

#### II-B3 Predictive Metrics

A range of predictive metrics are defined to support quantitative evaluation of performance. They are summarised in Table [I](https://arxiv.org/html/2512.05868v1#S2.T1 "TABLE I ‣ II-B3 Predictive Metrics ‣ II-B Spike Definitions and Predictive Metrics ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")

TABLE I: Performance Metrics for Evaluating SNN Models

| Metric | Equation | Purpose |
| --- | --- | --- |
| Spike Accuracy | Npredicted realNpredicted\frac{N\_{\text{predicted real}}}{N\_{\text{predicted}}} | Measures the precision of identified signals |
| Momentum Spike Percentage | Npredicted momentumNpredicted\frac{N\_{\text{predicted momentum}}}{N\_{\text{predicted}}} | Assesses suitability for momentum strategies |
| Spiking Rate | NpredictedNtotal timestamps\frac{N\_{\text{predicted}}}{N\_{\text{total timestamps}}} | Quantifies model activation frequency |
| Real Spiking Rate | Nreal spikesNtotal timestamps\frac{N\_{\text{real spikes}}}{N\_{\text{total timestamps}}} | Establishes baseline for comparison |
| True Positive Rate | Npredicted realNreal\frac{N\_{\text{predicted real}}}{N\_{\text{real}}} | Measures sensitivity/recall |
| False Positive Rate | Npredicted fakeNfake\frac{N\_{\text{predicted fake}}}{N\_{\text{fake}}} | Quantifies false signal generation |

#### II-B4 The Penalised Spike Accuracy (PSA) Objective

The selection of an appropriate optimisation objective is paramount for effective hyperparameter tuning with Bayesian optimisation. While price spike accuracy provides a natural target, it presents limitations when used in isolation. The primary limitation is that it results in a preference for lower SNN spiking rates and can give drastically different results for different time frames. To compel BO to discover models with both high accuracy and an actionable spike rates, this work introduces the novel Penalised Spike Accuracy (PSA) metric:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PSA=Spike Accuracy×Penalty Factor\text{PSA}=\text{Spike Accuracy}\times\text{Penalty Factor} |  | (8) |

The Penalty Factor exponentially diminishes the score if the model’s output rate deviates too far from the empirically determined Real Spike Rate (RSR), thus rewarding balance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Penalty Factor=exp⁡(−max⁡(|SRD|−α,0))\text{Penalty Factor}=\exp\left(-\max(|\text{SRD}|-\alpha,0)\right) |  | (9) |

where α=0.05\alpha=0.05 is a tolerance threshold and Spike Rate Deviation (SRD), is defined as the proportional difference from the true frequency (Eq [10](https://arxiv.org/html/2512.05868v1#S2.E10 "In II-B4 The Penalised Spike Accuracy (PSA) Objective ‣ II-B Spike Definitions and Predictive Metrics ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | SRD=Spike RateReal Spike Rate−1\text{SRD}=\frac{\text{Spike Rate}}{\text{Real Spike Rate}}-1 |  | (10) |

### II-C Model Architectures

Three SNN model architectures are proposed, sharing fundamental characteristics that form the foundation of this research. All implementations employ LIF neurons with preset membrane thresholds determined as a hyperparameter, and employ current-based synapses throughout the architecture. A standard simulation process describing the flow of data from input to output is constant across models, containing: input, propagation, and output. Input For each timestep t=1,2,…,Tt=1,2,...,T, KK spike trains are input to the network, where TT is the number of timesteps and KK is the number of features. Propagation Once the input spikes enter the network, they propagate according to the dynamics of LIF neurons.
The membrane potential, VV, of an LIF neuron evolves according to the differential equation [Gerstner1996]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β​d​Vd​t=−V+R​I​(t)\beta\frac{dV}{dt}=-V+RI(t) |  | (11) |

Where β\beta is the membrane time constant (decay rate), RR is the membrane resistance and I​(t)I(t) is the input current (sum of weighted incoming spikes).
Upon receiving a spike, a neuron’s membrane potential is incremented by the synapse’s weight. If this potential exceeds the preset threshold, VthreshV\_{\text{thresh}}, the neuron emits a spike that propagates forward. In the absence of a spike, the potential decays over time, and after a spike, the neuron’s potential resets by subtracting the membrane threshold from the current potential. Lastly, the neuron enters a brief refractory period of precisely one timestep to prevent immediate re-firing. Output In the final layer, a single spike train is outputted. The number of spikes in each spike train corresponds to the confidence that a price spike has occurred. If this number exceeds a decoding threshold, Dt​h​r​e​s​hD\_{thresh}, this is interpreted as the model predicting a price spike.

### Model 1 - Double Input SNN

![Refer to caption](image_double_input_inhib.png)


Figure 3: The extended architecture incorporating multiple time lags (additional nodes in X1​ and ​X2X\_{1}\text{ and }X\_{2}) and explicit inhibitory connections (in red).

The first model, an existing architecture proposed by Gao et al. (2021) [Gao2023], is designed for the competitive temporal dynamics of STDP learning for price spike detection. Its structure (blue connections in Figure [3](https://arxiv.org/html/2512.05868v1#S2.F3 "Figure 3 ‣ Model 1 - Double Input SNN ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")) is distinct from a standard feedforward network, instead opting for the creation of two distinct pathways. The input layer consists of two neurons, one in X1X\_{1} and one in X2X\_{2}, processing the positive and negative price difference series at time tt, respectively, which are encoded into spike trains via Poisson rate encoding. The hidden layer is segregated into two sub-layers, H1H\_{1} and H2H\_{2}, each exclusively connected to one input stream (X1→H1X\_{1}\to H\_{1}, X2→H2X\_{2}\to H\_{2}), ensuring structural separation. The single output LIF neuron receives full connectivity from H1H\_{1} and H2H\_{2}, with its spikes serving as price-spike predictions.

Training employs the STDP rule, adjusting synaptic weights based on the temporal relationship between pre- and postsynaptic spikes, defined by an exponential window function ([1](https://arxiv.org/html/2512.05868v1#S1.E1 "In I Introduction ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")). The network maintains stability through a synaptic homeostasis mechanism: weights are bounded between 0 and 1, and a 5% reduction is applied to all layer weights if the mean weight exceeds 0.5. This process prevents unconstrained growth and maintains stable dynamics. The training process operates in an unsupervised manner, relying solely on historical data for real-time deployment viability. The hyperparameters, found in Table [II](https://arxiv.org/html/2512.05868v1#S2.T2 "TABLE II ‣ Model 1 - Double Input SNN ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks") include the neuron, structural and synaptic plasticity parameters that were tuned using Bayesian optimisation.

TABLE II: Hyperparameters for Model 1 and Model 2

|  |  |  |
| --- | --- | --- |
| Parameter | Symbol | Function |
| Neuron and Structural Parameters | | |
| Decay Rate | β\beta | Rate of membrane potential decay |
| Membrane Threshold | VthreshV\_{\text{thresh}} | Spike generation threshold |
| Hidden Layer Neurons | Nh​i​d​d​e​nN\_{hidden} | Size of the network’s hidden layer |
| Input Neurons | Ni​n​p​u​tN\_{input} | Number of lags used as features |
| Synaptic Plasticity Parameters (Excitatory/Inhibitory) | | |
| Potentiation Learning Rate | A+/B+A\_{+}/B\_{+} | Controls weight strengthening |
| Depression Learning Rate | A−/B−A\_{-}/B\_{-} | Controls weight weakening |
| Potentiation Time Constant | τ+/θ+\tau\_{+}/\theta\_{+} | Temporal window for potentiation |
| Depression Time Constant | τ−/θ−\tau\_{-}/\theta\_{-} | Temporal window for depression |

### Model 2: Double Input SNN (Extended)

This extended architecture builds on Model 1 by incorporating additional temporal information and explicit inhibitory connections (Figure [3](https://arxiv.org/html/2512.05868v1#S2.F3 "Figure 3 ‣ Model 1 - Double Input SNN ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")), to enhance predictive performance. The model maintains the core segregated structure but introduces two significant enhancements. First, the input layer is expanded to incorporate kk multiple time lags for price differences, providing the network with comprehensive temporal information across different time scales. Input encoding is defined by X1​i←(Pn−Pn−i)+X\_{1i}\leftarrow(P\_{n}-P\_{n-i})\_{+} and X2​i←(Pn−Pn−i)−X\_{2i}\leftarrow(P\_{n}-P\_{n-i})\_{-}, for i∈[1,k]i\in[1,k]. Second, explicit inhibitory connections are integrated from X1X\_{1} to H2H\_{2} and from X2X\_{2} to H1H\_{1}. These inhibitory synapses, constrained to weights between 0 and -1, introduce direct competition, enhancing the model’s ability to isolate price momentum by mutually suppressing activity during noisy, bidirectional fluctuations. Essentially, the network architecture is optimised to isolate moments of price momentum over kk time lags, interpreted as price spikes that constitute actionable trading signals.

The training methodology maintains the core unsupervised STDP framework of Model 1, but critically modifies weight adjustments for inhibitory synapses. For inhibitory connections, weight updates Δ​w\Delta w are subtracted from existing weights, ensuring their inhibitory nature. The specific adjustment rule is: Δ​w=−W​(Δ​t)\Delta w=-W(\Delta t), where W​(Δ​t)W(\Delta t) follows the standard exponential window STDP function (Equation [1](https://arxiv.org/html/2512.05868v1#S1.E1 "In I Introduction ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")), ensuring stable learning dynamics while improving selectivity.

Model 2 includes all hyperparameters from Model 1, plus additional parameters for governing the inhibitory STDP dynamics and the increased complexity of the input layer (Table [II](https://arxiv.org/html/2512.05868v1#S2.T2 "TABLE II ‣ Model 1 - Double Input SNN ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")), which were determined using Bayesian optimisation.

### Model 3: Fully Connected SNN

The final model serves as a supervised learning reference to benchmark against the unsupervised Models 1 and 2. It employs a conventional, fully connected feedforward Spiking Neural Network (SNN) architecture with two hidden layers and two output neurons. This structure processes a broad range of financial features, including Returns, Volatility, and Volume, encoded into spike trains using Poisson rate encoding. Unlike the STDP-trained models, the architecture allows all input features to influence all subsequent neurons. The two output neurons enable binary classification for identifying significant price movements (real spikes) versus non-significant movements, allowing for direct optimisation against known labels.

Training is performed using supervised learning via Spike-based Backpropagation Through Time (BPTT). The loss function is a mean squared error count (target rates: 80%80\% of the time for the correct class, 20%20\% otherwise), encouraging targeted firing. Optimisation uses the Adam algorithm [Eshraghian2023, kingma2017adammethodstochasticoptimization] with the fast sigmoid as the surrogate gradient descent method.

The following fixed hyperparameters were manually selected to balance capacity, stability, and efficiency: the learning rate was set to 0.0050.005; the number of hidden neurons (NhiddenN\_{\text{hidden}}) was 128128; the membrane threshold (VthreshV\_{\text{thresh}}) was 11; and temporal dependencies were captured using time lags of 11, 33, and 55. The input features included Returns, Volatility, and Volume, selected for their strong temporal dependencies.

### II-D Experimental Design

Two complementary experimental frameworks were designed to rigorously evaluate the proposed methods and models: a rolling train-test experiment to assess temporal predictive performance, and a hyperparameter optimisation experiment to validate the novel Penalised Spike Accuracy (PSA) metric.

#### Experiment 1: Comparison of Objective Values

To assess the effectiveness of PSA against standard Spike Accuracy (SA), we employ Bayesian optimisation over 100 iterations for both metrics. In each iteration, models are trained and evaluated using sequential batches of 50005000 timestamps to enhance generalisability and mitigate overfitting. This process is repeated for both Model 1 and Model 2. The hyperparameters yielding the highest objective score for each metric (SA and PSA) are selected as optimal for subsequent analysis. These optimal parameters are used to train the definitive models for final comparison. Further analysis isolates the most impactful hyperparameters and maps their search spaces, detailed in Table [III](https://arxiv.org/html/2512.05868v1#S2.T3 "TABLE III ‣ Experiment 1: Comparison of Objective Values ‣ II-D Experimental Design ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks").

TABLE III: Hyperparameter Search Space

| Parameter | Values | Scale |
| --- | --- | --- |
| A+A\_{+} | [0.0001, 0.01] | Logarithmic |
| A−A\_{-} | [A+A\_{+} - 0.001, A+A\_{+}] | Logarithmic |
| τ+\tau\_{+} | [5, 100] | Linear (Integer) |
| τ−\tau\_{-} | [τ+\tau\_{+} - 5, τ+\tau\_{+} + 5] | Linear (Integer) |
| B+B\_{+} | [0.0001, 0.01] | Logarithmic |
| B−B\_{-} | [B+B\_{+} - 0.001, B+]B\_{+}] | Logarithmic |
| θ+\theta\_{+} | [5, 100] | Linear (Integer) |
| θ−\theta\_{-} | [θ+\theta\_{+} - 5, θ+\theta\_{+} + 5] | Linear (Integer) |
| β\beta | [ 0.5, 0.99] | Linear (step=0.01) |
| Vt​h​r​e​s​hV\_{thresh} | [0.8, 2.5] | Linear (step=0.1) |
| Dt​h​r​e​s​hD\_{thresh} | [4, 16] | Linear (Integer) |
| Ni​n​p​u​tN\_{input} | [1, 10] | Linear (Integer) |
| Nh​i​d​d​e​nN\_{hidden} | {16, 32, 64, 128} | Categorical |

#### Experiment 2: Comparison of Model Performance

The second experiment compares the predictive performance of all models using a day-by-day rolling window structure to replicate real-world data workflows. The dataset consists of high-frequency intra-day price series spanning 1919 consecutive trading days in February 2015. The model is trained on one day’s data and tested on the subsequent day. This process rolls forward sequentially: Day ii trains for prediction on Day i+1i+1. This methodology ensures that each day (except the first and last) serves exactly once as a training set and once as a testing set. This design prevents future information from contaminating predictions, maintaining the integrity and validity of the results. The key performance metrics for evaluation are summarised in Table [I](https://arxiv.org/html/2512.05868v1#S2.T1 "TABLE I ‣ II-B3 Predictive Metrics ‣ II-B Spike Definitions and Predictive Metrics ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks").

### II-E SNN Based Momentum Strategy

The SNN based momentum strategy combines the SNN’s ability to detect significant temporal patterns (spikes) with established momentum-trading logic.
The core principle of momentum trading suggests that major price movements typically continue in their current direction due to market inertia. This manifests as autocorrelation in price movements, where recent price changes predict short-term future movements.
When the SNN emits a spike signal at time tt, a position is initiated. The trade’s direction is determined by analysing the immediate preceding price trend using a look-back window of nn timestamps (default 3), quantified by a position flag, FtF\_{t} (Equation [12](https://arxiv.org/html/2512.05868v1#S2.E12 "In II-E SNN Based Momentum Strategy ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=Pt−1n​∑i=1nPt−iF\_{t}=P\_{t}-\frac{1}{n}\sum\_{i=1}^{n}P\_{t-i} |  | (12) |

A positive flag (current price below recent average) suggests a downward trend, triggering a short position; a negative flag suggests an upward trend, prompting a long position (Algorithm [2](https://arxiv.org/html/2512.05868v1#alg2 "Algorithm 2 ‣ II-E SNN Based Momentum Strategy ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")). This ensures the neural network identifies the opportune entry time, while the momentum calculation dictates the trade’s direction.

Algorithm 2  Spike-Based Momentum Strategy

1: if FtF\_{t} << 0 then

2:  Enter short position

3: else if FtF\_{t} >> 0 then

4:  Enter long position

5: end if

The back-testing framework integrates the spike signal for entry timing. Upon spike detection, the trade is executed as a market order at the VWAP of the subsequent timestamp. Key back-testing parameters ensure consistent evaluation: initial capital is normalised to 1 unit, trades use full capital (1×\times leverage), and only one position is open at any time, maintained for a predetermined duration before closing at the exit timestamp’s VWAP.

Performance is evaluated using metrics detailed in Table [IV](https://arxiv.org/html/2512.05868v1#S2.T4 "TABLE IV ‣ II-E SNN Based Momentum Strategy ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks"), which assess both profitability and risk characteristics. Results are benchmarked against random and naive momentum strategies to quantify the value added by the SNN approach.

TABLE IV: Trading Performance Metrics and Importance

| Metric | Importance |
| --- | --- |
| Cumulative Return | Measures overall strategy effectiveness regardless of timeframe |
| Sharpe Ratio | Evaluates return quality by accounting for volatility and risk taken |
| Maximum Drawdown | Quantifies worst-case capital decline, essential for risk management |
| Win Rate | Indicates strategy consistency and psychological sustainability |
| Profit Factor | Assesses overall profitability efficiency and capital utilisation |
| Profit-Loss Ratio | Reveals if winning trades sufficiently outweigh losing trades |
| Expectancy | Provides mathematical expectation of profit per trade over time |

## III Results

### III-A Hyperparameter Optimisation

Following Experiment 1, Bayesian optimisation was conducted for 100 iterations on both Model 1 and Model 2 across two objective metrics: Spike Accuracy (SA) and Predictive Spike Accuracy (PSA). The results, gathered using the Optuna library [akiba2019optuna], are presented in Table [V](https://arxiv.org/html/2512.05868v1#S3.T5 "TABLE V ‣ III-A Hyperparameter Optimisation ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks").

TABLE V: Hyperparameters for Models

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Parameter | Model 1 | | Model 2 | |
| SA | PSA | SA | PSA |
| A+A\_{+} | 0.0037 | 0.0067 | 0.0096 | 0.0012 |
| A−A\_{-} | 0.0032 | 0.0063 | 0.0093 | 0.0009 |
| B+B\_{+} | – | – | 0.0059 | 0.0016 |
| B−B\_{-} | – | – | 0.0052 | 0.0009 |
| τ+\tau\_{+} | 45 | 71 | 74 | 54 |
| τ−\tau\_{-} | 42 | 72 | 72 | 58 |
| θ+\theta\_{+} | – | – | 44 | 51 |
| θ−\theta\_{-} | – | – | 44 | 51 |
| β\beta | 0.96 | 0.79 | 0.87 | 0.86 |
| VthreshV\_{\text{thresh}} | 2.20 | 0.80 | 2.50 | 2.00 |
| NhiddenN\_{\text{hidden}} | 16 | 32 | 128 | 64 |
| NinputN\_{\text{input}} | – | – | 1 | 3 |
| DthreshD\_{\text{thresh}} | 12 | 9 | 12 | 11 |
| Objective Value | 0.90 | 0.76 | 0.77 | 0.71 |
| Spike Rate Deviation | -0.69 | -0.01 | -0.43 | 0.078 |



|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) Model 1 | (b) Model 2 |

Figure 4: Parameter importance ranking for Models 1 & 2, explored for performance metrics SA and PSA.

#### III-A1 Analysis of Optimal Parameters

The optimised hyperparameters in Table [V](https://arxiv.org/html/2512.05868v1#S3.T5 "TABLE V ‣ III-A Hyperparameter Optimisation ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks") reveal key differences dictated by the SA and PSA objectives. The table lists the highest objective score achieved and the corresponding spike rate deviation.

For Model 1, PSA generally selected larger excitatory learning rates (A+,A−A\_{+},A\_{-}) and learning windows (τ+,τ−\tau\_{+},\tau\_{-}) compared to SA. This, combined with a low membrane threshold (Vthresh=0.80V\_{\text{thresh}}=0.80) and spike decoding threshold (Dthresh=9D\_{\text{thresh}}=9), promotes higher network activity and increased spike rates. Conversely, the SA parameters (e.g., Vthresh=2.2V\_{\text{thresh}}=2.2) favor conservative network action and higher selectivity, resulting in much lower spike rates.

Model 2 exhibited different trends, underscoring the challenge in tuning STDP-trained networks. PSA selected low learning rates and time constants for both excitatory and inhibitory synapses, alongside a higher membrane threshold (Vthresh=2.0V\_{\text{thresh}}=2.0). This suppression is likely a necessary control mechanism, as Model 2 PSA selected three input features (Ninput=3N\_{\text{input}}=3), providing a considerable volume of input spiking activity. Model 2 SA, however, selected only one input feature (Ninput=1N\_{\text{input}}=1) and could thus afford larger learning rates. SA also selected the upper bound membrane threshold (Vthresh=2.5V\_{\text{thresh}}=2.5), confirming its preference for conservative behavior.

Across both models, VthreshV\_{\text{thresh}}, β\beta, and DthreshD\_{\text{thresh}} were consistently lower for PSA than SA, further supporting the observation that PSA optimization drives higher network activity. Observing the Spike Rate Deviation (Table [V](https://arxiv.org/html/2512.05868v1#S3.T5 "TABLE V ‣ III-A Hyperparameter Optimisation ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")) confirms that SA consistently yields large negative deviations (lower spike rates), while PSA results in minor fluctuations close to the true rate. The higher objective values for Model 1 relative to Model 2 suggest greater training difficulty for the latter. Overall, while PSA shows better performance regarding adherence to the true spike rate, further analysis is required to determine its overall practical efficacy.

#### III-A2 Parameter Importance

As shown in Figure [4](https://arxiv.org/html/2512.05868v1#S3.F4 "Figure 4 ‣ III-A Hyperparameter Optimisation ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks"), the membrane threshold (VthreshV\_{\text{thresh}}) and the decay rate (β\beta) were consistently the two most critical hyperparameters across both models and metrics. Importance was highly skewed toward these two parameters for Model 1. In contrast, Model 2 showed a more even distribution of importance, likely due to its added complexity (inhibitory synapses) requiring tuning of multiple parameters for improved results. For both models, PSA increased the skew toward the membrane threshold, suggesting that fine control over spiking rates was primarily achieved by adjusting VthreshV\_{\text{thresh}} to suppress or increase spiking activity. Other parameters, such as the depression learning rates and windows, had minimal effect, as their optimal values were generally dependent on their potentiating counterparts.

### III-B Predictive Performance

Table [VI](https://arxiv.org/html/2512.05868v1#S3.T6 "TABLE VI ‣ III-B Predictive Performance ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks") summarises key metrics for models optimised via SA and PSA respectively, alongside Model 3. The random model had a 50% chance of spiking at any timestamp and adds additional context to these metrics. These measures provide insight into each optimisation method’s ability to balance accuracy against network activity and error rates.

TABLE VI: Comparison of the predictive performance of all models and a random baseline

| Metric | Random | Model 1 | | Model 2 | | Model 3 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | SA | PSA | SA | PSA |  |
| Spike Acc. (%\%) | 59.8559.85 | 73.8573.85 | 62.6762.67 | 67.1367.13 | 65.1165.11 | 69.3569.35 |
| Mom. Spike (%\%) | 54.4754.47 | 54.3454.34 | 54.4954.49 | 55.0855.08 | 55.0655.06 | 55.0955.09 |
| TPR (%\%) | 50.0050.00 | 12.9612.96 | 67.3367.33 | 12.5112.51 | 48.6248.62 | 36.8836.88 |
| FPR (%\%) | 50.0050.00 | 7.037.03 | 59.8159.81 | 9.139.13 | 38.8338.83 | 24.3024.30 |
| Spiking Rate (%\%) | 50.0050.00 | 10.5810.58 | 64.3164.31 | 11.1511.15 | 44.6944.69 | 31.8331.83 |

Models optimised with PSA exhibit significantly higher spike rates and True Positive Rates (TPR), suggesting that this method drives greater network sensitivity and spiking activity. Conversely, SA optimisation leads to high precision (Spike Acc.) but much lower spiking rates and TPR, indicating a highly conservative firing strategy that may improve efficiency but risks missing true events. All models demonstrate a consistent Momentum Spike Percentage near the baseline, confirming reliable directional prediction regardless of the specific optimisation objective. All models successfully surpass the random baseline in Spike Accuracy, validating the utility of the SNN approach. Model 3, representing a supervised learning baseline, shows performance that is generally average compared to the diverse outcomes of the unsupervised SA and PSA methods.

### III-C Trading Performance

Trading performance is assessed and compared against two baselines: a naive momentum strategy (following Algorithm [2](https://arxiv.org/html/2512.05868v1#alg2 "Algorithm 2 ‣ II-E SNN Based Momentum Strategy ‣ II Method ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks") at every step) and a random trading approach (50% spike chance). Each model was run three times (100 for the random model), and results were averaged. For a fair comparison, cumulative returns in Table [VII](https://arxiv.org/html/2512.05868v1#S3.T7 "TABLE VII ‣ III-C Trading Performance ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks") are scaled to 1,0001,000 trades per day, totalling 19,00019,000 trades over the one-month period. All other metrics are reported using their original values.

TABLE VII: Trading Performance Comparison Across Models (Returns Scaled to 1,0001,000 Trades per Day)

| Metric | Model 1 | | Model 2 | | Model 3 | Naive | Random |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | SA | PSA | SA | PSA |  |  |  |
| Cum. Return (%\%) | 15.4915.49 | 15.4815.48 | 13.6313.63 | 17.44\mathbf{17.44} | 12.4412.44 | 13.4913.49 | 12.7112.71 |
| Sharpe Ratio | 10.7010.70 | 16.4816.48 | 16.7216.72 | 19.72\mathbf{19.72} | 15.9115.91 | 16.3216.32 | 17.9917.99 |
| Max. DD (%\%) | 5.855.85 | 2.522.52 | 2.252.25 | 2.692.69 | 2.952.95 | 1.76\mathbf{1.76} | 2.772.77 |
| Win Rate (%\%) | 52.6352.63 | 52.6052.60 | 52.8952.89 | 53.49\mathbf{53.49} | 52.7952.79 | 52.4252.42 | 52.2852.28 |
| Profit Factor | 1.151.15 | 1.211.21 | 1.161.16 | 1.22\mathbf{1.22} | 1.131.13 | 1.181.18 | 1.171.17 |
| Profit-Loss Ratio | 1.001.00 | 1.09\mathbf{1.09} | 1.031.03 | 1.061.06 | 1.011.01 | 1.071.07 | 1.071.07 |
| Expectancy (×10−6\times 10^{-6}) | 8.158.15 | 8.158.15 | 7.177.17 | 9.18\mathbf{9.18} | 6.556.55 | 7.107.10 | 6.696.69 |

The models optimised with the PSA metric consistently outperform their SA counterparts and both baselines across most key performance measures (Table [VII](https://arxiv.org/html/2512.05868v1#S3.T7 "TABLE VII ‣ III-C Trading Performance ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")). Notably, Model 2–PSA achieves the highest cumulative return (17.44%17.44\%), the strongest risk-adjusted return (Sharpe=19.71\text{Sharpe}=19.71), the best win rate (53.49%53.49\%), Profit Factor (1.221.22), and Expectancy (9.18×10−69.18\times 10^{-6}). Although its Max Drawdown (2.69%2.69\%) is slightly higher than the Naive strategy (1.76%1.76\%), its overall profile is superior.

Comparing optimisation methods directly, PSA significantly improved risk control for Model 1, halving the drawdown (2.52%2.52\% vs 5.85%5.85\%) and substantially boosting the Sharpe Ratio (16.4816.48 vs 10.7010.70), despite a negligible change in headline return (15.48%15.48\% vs 15.49%15.49\%). Model 2 saw a more pronounced benefit from PSA, with return increasing from 13.63%13.63\% to 17.44%17.44\% and Sharpe Ratio enhancing from 16.7216.72 to 19.7119.71.

In contrast, Model 3 (supervised) yielded moderate outcomes, falling short of both PSA-optimised models in cumulative return (12.44%12.44\%) and Sharpe Ratio (15.9115.91). Its maximum drawdown (2.95%2.95\%) was acceptable, but its Profit Factor (1.131.13) and Expectancy (6.55×10−66.55\times 10^{-6}) were lower than the STDP-trained models.

|  |
| --- |
| Refer to caption |
| (a) Drawdown |
| Refer to caption |
| (b) Equity (unscaled) |

Figure 5: Equity (unscaled) and Drawdown over time.

The equity and drawdown curves (Figure [5](https://arxiv.org/html/2512.05868v1#S3.F5 "Figure 5 ‣ III-C Trading Performance ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")) further confirm the superiority of the PSA-optimised models. The drawdown plot highlights Model 1–SA’s susceptibility to high volatility, particularly around the 12th and 13th day. In the unscaled equity curves, both PSA variants markedly outperform their SA counterparts, achieving total returns over 70%70\% for the month, while SA models remain below 30%30\%. Model 3 achieved a moderate 42%42\% return. The primary driver of the PSA models’ higher returns is their higher spiking rate, enabling them to exploit more trading opportunities, as detailed by the total trade counts in Table [VIII](https://arxiv.org/html/2512.05868v1#S3.T8 "TABLE VIII ‣ III-C Trading Performance ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks").

TABLE VIII: Model Performance Comparison (unscaled)

| Model | Final Equity | Total Return | Num Trades |
| --- | --- | --- | --- |
| Model 1-SA | 1.296311 | 29.63% | 36,336 |
| Model 1-PSA | 1.824112 | 82.41% | 101,126 |
| Model 2-SA | 1.295183 | 29.52% | 41,141 |
| Model 2-PSA | 1.768009 | 76.80% | 83,673 |
| Model 3 | 1.424655 | 42.47% | 51,229 |

## IV Conclusion

Building upon the foundational work of Gao et al., this research successfully validated the application of Spike-Timing-Dependent Plasticity (STDP)-trained Spiking Neural Networks for high-frequency trading price-spike prediction using a reproducible framework to rigorously compare three architectures: the original replication (Model 1), a novel extended SNN featuring inhibitory synapses and enriched temporal inputs (Model 2), and a supervised feedforward SNN (Model 3).

Key achievements include the design of Model 2 and the effective application of Bayesian optimisation steered by a Penalised Spike Accuracy (PSA) objective. This metric reliably tuned the networks, ensuring close alignment with empirical spiking rates (e.g., Model 2 deviated by only +0.07+0.07). Crucially, backtesting a HFT momentum strategy demonstrated that all SNN models outperformed random benchmarks and decisively surpassed the supervised Model 3, with Model 2 (PSA) yielding the strongest trading performance, highest cumulative returns, and superior risk-adjusted metrics (Table [VII](https://arxiv.org/html/2512.05868v1#S3.T7 "TABLE VII ‣ III-C Trading Performance ‣ III Results ‣ Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks")), thereby confirming the predictive power of the novel architecture combined with precise, PSA-driven hyperparameter tuning.

While this study establishes the efficacy of STDP-trained SNNs for HFT, several challenges remain. The current quantitative finance literature would benefit from additional peer-reviewed SNN benchmarks and standardization of SNN-based metrics for financial time series analysis (such as those presented in this work) to better facilitate comparison efforts and pave the way towards standardized deployment on neuromorphic hardware, allowing improved quantification of energy and latency performance essential for HFT applications.

## V Funding

This research was supported through the NimbleAI project, funded via the Horizon Europe Research and Innovation programme (Grant Agreement 101070679), and UKRI under the UK government’s Horizon Europe funding guarantee (Grant Agreement 10039070); the Horizon Europe AIDA4Edge project (Grant Agreement 101160293); and the EPSRC Edgy Organism project (EP/Y030133/1).