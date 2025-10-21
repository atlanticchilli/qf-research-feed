---
authors:
- Alok Das
- Kiseop Lee
doc_id: arxiv:2510.16938v1
family_id: arxiv:2510.16938
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Topological Approach to Parameterizing Deep Hedging Networks
url_abs: http://arxiv.org/abs/2510.16938v1
url_html: https://arxiv.org/html/2510.16938v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alok Das


 Kiseop Lee

###### Abstract

Deep hedging uses recurrent neural networks to hedge financial products that cannot be fully hedged in incomplete markets. Previous work in this area focuses on minimizing some measure of quadratic hedging error by calculating pathwise gradients, but doing so requires large batch sizes and can make training effective models in a reasonable amount of time challenging. We show that by adding certain topological features, we can reduce batch sizes substantially and make training these models more practically feasible without greatly compromising hedging performance.

## 1 Introduction

The classical hedging problem entails replicating the payoff of a contingent claim under a certain stochastic model. While we can find a complete hedging strategy in a complete market like Black-Scholes, a market is in general incomplete, including jump diffusion, and stochastic volatility models. While there are several hedging approaches in an incomplete market, it is often very difficult to get a closed form solution or even calculate numerically.

Even in a complete market like Black-Scholes, there are drawbacks to this strategy in both execution and the theory it is based on. A traditional asset pricing and hedging method assumes frictionless markets, perfect liquidity, and normally distributed returns among many other conditions. Volatility in between re-balancing periods can also create losses, as our hedging is ”too late” to compensate for underlying movements. These losses can accumulate quickly, and since continuous hedging is not feasible, there is not much improvement that can be made. The model itself is also memoryless in the sense that only the current model parameters are relevant; the path of the underlying price process itself is not of concern.

Thanks to the development of deep neural networks, we can address these difficulties through ”Deep Hedging”, which involves training neural networks to determine optimal hedging actions without being constrained by assumptions about the market.

Deep hedging [[1](https://arxiv.org/html/2510.16938v1#bib.bib1)] [[7](https://arxiv.org/html/2510.16938v1#bib.bib7)] has experienced more development in recent years mainly due to its flexibility in handling market conditions and ability to learn from simulated data. The work itself began when Buehler et al. [[1](https://arxiv.org/html/2510.16938v1#bib.bib1)] optimized long short-term memory networks to learn global hedging policies by utilizing mean-square error (MSE) and semi-mean-square error (SMSE) as loss functions. Carbonneau [[3](https://arxiv.org/html/2510.16938v1#bib.bib3)] built upon this work by considering applications to long-term look-back options while also utilizing non-quadratic loss functions. Imaki et al. [[10](https://arxiv.org/html/2510.16938v1#bib.bib10)] also trained networks to hedge look-back options but with the dependency of past hedging actions omitted as a parameter. The work done in [[12](https://arxiv.org/html/2510.16938v1#bib.bib12)][[2](https://arxiv.org/html/2510.16938v1#bib.bib2)] [[14](https://arxiv.org/html/2510.16938v1#bib.bib14)] takes into account factors such as real-world data, transaction costs and market impact.

The main improvements of this paper come from a broader area of study known as Topological Data Analysis (TDA) which has recently emerged as a way to understand the structure of complex data when viewing it as an embedding in dd-dimensional space [[4](https://arxiv.org/html/2510.16938v1#bib.bib4)]. Rai et al .[[16](https://arxiv.org/html/2510.16938v1#bib.bib16)] employed TDA to identify ”extreme” events in the stock market via spikes in L1L^{1}/L2L^{2} norms and Wasserstein distances. The work done in terms of training optimization is fairly limited, but recent research has focused on gradient-based approaches [[13](https://arxiv.org/html/2510.16938v1#bib.bib13)] rather than optimized parameterizations. We do this by incorporating topological features into the model inputs. We evaluate four models: with and without topological features, each trained using batch sizes of 20 and 1000. On an independent set of price paths, the models with topological features achieve lower PnL variance and maintain stable performance even at the smaller batch size.

The paper is organized as follows. We briefly introduce ”Deep Hedging” in Chapter 2. Chapter 3 explains our model. We introduce a topological approach in Chapter 4. We provide examples in Chapter 5. Chapter 6 concludes.

## 2 Deep Hedging

Deep hedging originated in an effort to hedge financial products within incomplete markets by using neural networks to create deterministic hedging policies. As mentioned previously conventional hedging strategies involve many simplifying assumptions and as such are not particularly well suited outside a purely theoretical environment. For practical applications, neural networks allow us to adapt to market conditions rather than ignoring them as a whole. In practice, neural networks utilize gradient descent to find optimal parameters and are particularly useful in convex risk measure environments[[11](https://arxiv.org/html/2510.16938v1#bib.bib11)]. By virtue of its construction, neural networks let us specify hedging instruments, cost functions, and any market frictions we want to optimize. This flexibility has been utilized recently in applications to path dependent options like barrier options[[5](https://arxiv.org/html/2510.16938v1#bib.bib5)] and bermuda swaptions [[15](https://arxiv.org/html/2510.16938v1#bib.bib15)], 2 financial products that cannot be completely hedged discretely in an incomplete market. A recurrent neural network structure is common as it not only takes into account the features provided as they evolve over time, but also past hedging decisions. However, over extended time periods, this can be difficult to unravel when back-propagating and can lead to training times that grow exponentially as model depth increases. Mueller et al. [[13](https://arxiv.org/html/2510.16938v1#bib.bib13)] addressed this issue by adopting a 2nd order optimization scheme in which they precondition gradients by approximating a curvature matrix as block diagonal and Kronecker factored. In doing so, they observed a 75%\% improvement in training steps needed to reach a target loss. Our topological approach is more forward-facing and in Chapter 5, we can see the direct impact this has on hedging performance.+

## 3 Model

The underlying spot price and volatility are derived from the Heston Model[[8](https://arxiv.org/html/2510.16938v1#bib.bib8)] in which both the underlying and volatility is determined by a stochastic process. The cliquet itself tracks capped cumulative returns over periods of length 20 and is an example of a path dependent option. The payout is updated every 20 steps and gains (losses) in the current time period are not counted until the period has concluded.

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St\displaystyle dS\_{t} | =μ​St​d​t+vt​St​d​WtS,\displaystyle=\mu S\_{t}\,dt+\sqrt{v\_{t}}\,S\_{t}\,dW\_{t}^{S}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​vt\displaystyle dv\_{t} | =κ​(θ−vt)​d​t+ξ​vt​d​Wtv.\displaystyle=\kappa(\theta-v\_{t})\,dt+\xi\sqrt{v\_{t}}\,dW\_{t}^{v}. |  |

For our experiments we assign drift μ=0.02\mu=0.02, v0=0.025v\_{0}=0.025, κ=2.5\kappa=2.5, θ=0.02\theta=0.02, ξ=0.6\xi=0.6, with correlation ρ=−0.5\rho=-0.5 for brownian motions WtSW\_{t}^{S} and WtvW\_{t}^{v}. To define our topological features effectively we define a 3-dimensional Euclidean plane with some e>0e>0. We can use the Vietoris-Rips complex (Rips complex) ℛ​(X,ϵ)\mathcal{R}(X,\epsilon)[[4](https://arxiv.org/html/2510.16938v1#bib.bib4)] to capture connectivity between the data points in our moving window. In this setting any subset of k+1k+1 points from out data set forms a k-simplex in ℛ​(X,ϵ)\mathcal{R}(X,\epsilon) where distances between points is the standard euclidean norm satisfying ‖xi−xj‖<ϵ||x\_{i}-x\_{j}||<\epsilon. By increasing ϵ\epsilon we can track when simplexes are formed as more pairwise distances satisfy the distance condition. These updates are referred to as ”birth” and ”death” rates to signify the creation and destruction of connections between points in ℝ3\mathbb{R}^{3}. Topologically this process of quantifying connectivity in 3-dimensional space reflects the creation of a persistence diagram for the 0-dimensional homology. For the previously mentioned moving window we calculate the L1L^{1} and L2L^{2} norms in an effort to measure outliers in our feature space. Intuitively the L1L^{1} norm tracks large jumps in the feature set, whereas the L2L^{2} norm captures average dependencies over time.

Recurrent neural networks specifically are of great interest here due to its ability to take into account past hedging actions when determining future actions. Since we seek to mimic realistic trading conditions, we can structure our feature set to contain data available up to time tt. A common choice for a cost function is quadratic hedging error [[9](https://arxiv.org/html/2510.16938v1#bib.bib9)]. Intuitively, using this cost function reflects a goal of minimizing PnL spread and bias towards any directional hedging. Our parameterization allows for our network to make more confident hedging decisions, so minimizing PnL spread is of more concern than removing any directional bias.

Our goal now is to create a model that can hedge a cliquet. To start our construction we define a filtered probability space on a finite time horizon. Specifically, we operate on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) where (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0} captures market information at time tt. We also denote anything measurable at time tt with a subscript tt. Our data is generated for 240 time steps with a cliquet cap μ=0.035\mu=0.035. The feature set is created at each time tt and a moving window of size 15 is used to generate the topological features. Since our moving window starts to generate data after 15 time steps, we pad our feature set with zeros to remove any inconsistencies within the sizes of components of ℱ\mathcal{F} and as such choose to ignore the notational difficulties that would arise as a way of clearly defining that.
The core feature set itself consists of the spot price StS\_{t}, realized volatility vtv\_{t} and the cliquet payout ψt\psi\_{t}.

|  |  |  |
| --- | --- | --- |
|  | ψ​(x,t)=max⁡[∑i=20,40,…,ttmin⁡(xixi−1−1,μ),0]\psi(x,t)=\max\bigg[\sum^{t}\_{\begin{subarray}{c}i=20,40,...,t\end{subarray}}\min\!\left(\frac{x\_{i}}{x\_{i-1}}-1,\mu\right),0\bigg] |  |

## 4 Topological Approach

Our approach to creating the topological features previously mentioned can be described as a norm based aggregation of the core feature set. We have a set of features (price, volatility, payout) and we seek to understand the shape of that data. We take that data, embed it in 3-dimensional space and build connections between data points to understand how spread out they are. We quantify this data through ”birth” and ”death” rates [[6](https://arxiv.org/html/2510.16938v1#bib.bib6)] which is essentially an iterative process that determines how far apart each data point is.

To demonstrate improvement via the addition of the topological features, we train 4 models. The models themselves consist of pairwise combinations of batch sizes and features within {20,1000}\{20,1000\} and {n​o​T​D​A,T​D​A}\{no\ TDA,\ TDA\}. The feature set itself consists of the underlying spot price, realized volatility, the payout of the cliquet at time tt and the L1/L2L^{1}/L^{2} norms of the previous 3 features in a rolling window size of 15. The first layer of the network processes the feature set and the previous action separately through unique dense layers of dimension 32, then processes them through a T​a​n​HTanH activation function. This output is then processed through 4 stacked LSTM cells, each of dimension 32. The output is then sent to one final dense layer with dimension 1 to reflect the individual action of delta hedging. This architecture itself draws inspiration from [[13](https://arxiv.org/html/2510.16938v1#bib.bib13)] where our changes come in uniform dimensionality across layers and a lack of a mask to filter hedging instruments(reflects the constant availability of hedging through the spot). Intuitively, the idea behind stacking layers in this manner is to allow the network to learn deeper dependencies as training progresses. Our loss function we seek to minimize is a scaled PnL variance calculation where we denote Ω​(T)\Omega(T) the PnL of hedging at time TT and γ=1000\gamma=1000.

|  |  |  |
| --- | --- | --- |
|  | l​o​s​s=γ​𝕍​[Ω​(T)−ψ​(x,T)]loss=\gamma\mathbb{V}\bigg[\Omega(T)-\psi(x,T)\bigg] |  |

## 5 Examples

Each of the 4 models with their respective batch sizes were trained for ∼\sim5300 epochs. Additionally, each of the 4 models was tested on the same 50,000 generated paths to ensure consistency between comparisons in performance. Our metric for a ”good” hedging model is removing tail risk and minimizing PnL variance. From Figure [3(b)](https://arxiv.org/html/2510.16938v1#S5.F3.sf2 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") [2(b)](https://arxiv.org/html/2510.16938v1#S5.F2.sf2 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") we can see that when batch sizes are increased there is a substantial comparative decrease in PnL variance. In both cases when the topological features are added [2(a)](https://arxiv.org/html/2510.16938v1#S5.F2.sf1 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") [2(b)](https://arxiv.org/html/2510.16938v1#S5.F2.sf2 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") we can see that PnL standard deviation in the batch of 20 goes from 4.2e-02 →\xrightarrow{} 2.5e-02 and in the batch of 1000 it goes from 3.4e-02 →\xrightarrow{} 2.1e-02. Notably, models that utilize minimal batch sizes tend to have wider distributions. In that specific case the models seem to create more tail probability positive PnL scenarios rather than minimize overall variance.
 [3(a)](https://arxiv.org/html/2510.16938v1#S5.F3.sf1 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks").
![[Uncaptioned image]](rolling_average.png)

Figure 1: Average trade size during training using a rolling average with window size 50

Generally average trade sizes tend to move up as training progresses but for the model containing a large batch size plus the topological features, we start to see a divergence from where the rest of the models seem to cluster. The model containing topological features seemingly learns to trade more as training progresses. In deep hedging applications it is not surprising that a network may learn to trade more actively. As noted in [[14](https://arxiv.org/html/2510.16938v1#bib.bib14)], delta hedging in the presence of limited market liquidity can lead to excessive trading. In our setting, however, we observe that hedging error variance declines despite an increase in average trade size. We interpret this as evidence that the network is not simply overtrading, but is making more decisive hedging decisions. The larger trades reflect greater confidence in its hedging policy, with aggressiveness arising from more accurate assessments of when rebalancing meaningfully reduces risk.

![Refer to caption](tda_20.png)


(a) PnL of model using topological features and batch size 20

![Refer to caption](tda_1000.png)


(b) PnL of model using topological features and batch size 1000



![Refer to caption](no_tda_20.png)


(a) PnL of model without topological features and batch size 20

![Refer to caption](no_tda_1000.png)


(b) PnL of model without topological features and batch size 1000

Since the models themselves are all tested on the same training set, we can confidently compare their performances. Our results show that the implementation of topological features not only decreases PnL variance, but allows for smaller batch sizes to achieve similar results. Our data also gives insight into the types of trades being made as well. In chart  [1](https://arxiv.org/html/2510.16938v1#S5.F1 "Figure 1 ‣ 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") we can see that in the case of the 2 models trained with batch sizes of 20, the average trade size is very similar, however in charts  [2(a)](https://arxiv.org/html/2510.16938v1#S5.F2.sf1 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") and  [3(a)](https://arxiv.org/html/2510.16938v1#S5.F3.sf1 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") we can see that the topological features lead to a significant decrease in PnL variance. This shows that the network learns to make more meaningful hedges. We can also see in  [3(b)](https://arxiv.org/html/2510.16938v1#S5.F3.sf2 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") that the PnL standard deviation is 3.4e-02 but when adding the topological features  [2(b)](https://arxiv.org/html/2510.16938v1#S5.F2.sf2 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") the standard deviation drops to 2.1e-02. We can also see the tail-risk PnL outcomes are better under the topological features. Where all PnL outcomes are above -0.2 for  [2(b)](https://arxiv.org/html/2510.16938v1#S5.F2.sf2 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks") and above -0.25 for  [3(b)](https://arxiv.org/html/2510.16938v1#S5.F3.sf2 "In 5 Examples ‣ A Topological Approach to Parameterizing Deep Hedging Networks").

## 6 Conclusion

We proposed a model parameterization that demonstrates comparable hedging performance to models trained with significantly larger batch sizes. Doing so resulted in 10x faster training times. Future work could involve modifying window/batch sizes to find optimal combinations. We experimented with strict rounding masks to simulate a lack of fractional trading availability and did not see much progress, but some improvement to hedging was noted when the topological features were added, so this could also be an avenue of research. Additionally, if we assume batch sizes effect on hedging performance is a convex function it stands to reason that there may exist an optimal batch size besides the ones we tested.

## References

* [1]

  Hans Bühler, Lukas Gonon, Josef Teichmann, and Ben Wood.
  Deep hedging, 2018.
  arXiv preprint arXiv:1802.03042.
* [2]

  Jay Cao, Jacky Chen, John Hull, and Zissis Poulos.
  Deep hedging of derivatives using reinforcement learning, 2021.
  arXiv preprint arXiv:2103.16409.
* [3]

  Alexandre Carbonneau.
  Deep hedging of long-term financial derivatives, 2020.
  arXiv preprint arXiv:2007.15128.
* [4]

  Frédéric Chazal and Bertrand Michel.
  An introduction to topological data analysis: Fundamental and practical aspects for data scientists, 2021.
  arXiv preprint arXiv:1710.04019.
* [5]

  Jacky Chen, Yu Fu, John C. Hull, Zissis Poulos, Zeyu Wang, and Jun Yuan.
  Hedging barrier options using reinforcement learning.
  Technical Report SSRN 4566384, University of Toronto / SSRN, 2023.
* [6]

  Herbert Edelsbrunner, David Letscher, and Afra Zomorodian.
  Topological persistence and simplification.
  In Proceedings of the 41st Annual Symposium on Foundations of Computer Science (FOCS), pages 454–463. IEEE, 2002.
* [7]

  Pascal François, Geneviève Gauthier, Frédéric Godin, and Carlos O. Pérez-Mendoza.
  Deep hedging with options using the implied volatility surface, 2025.
  arXiv preprint arXiv:2504.06208.
* [8]

  Steven L. Heston.
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  The Review of Financial Studies, 6(2):327–343, 1993.
* [9]

  Bernhard Hientzsch.
  Reinforcement learning and deep stochastic optimal control for final quadratic hedging, 2023.
  arXiv preprint arXiv:2401.08600.
* [10]

  Shota Imaki, Kentaro Imajo, Katsuya Ito, Kentaro Minami, and Kei Nakagawa.
  No-transaction band network: A neural network architecture for efficient deep hedging.
  The Journal of Financial Data Science, 5(2):84–99, 2023.
* [11]

  Matteo Maggiolo, Giuseppe Nuti, Miroslav Štrupl, and Oleg Szehr.
  Deep hedging under non-convexity: Limitations and a case for alphazero, 2025.
* [12]

  Oskari Mikkilä and Juho Kanniainen.
  Empirical deep hedging, 2022.
  SSRN Working Paper.
* [13]

  Konrad Mueller, Amira Akkari, Lukas Gonon, and Ben Wood.
  Fast deep hedging with second-order optimization, 2024.
  arXiv preprint arXiv:2410.22568.
* [14]

  Andrei Neagu, Frédéric Godin, Clarence Simard, and Leila Kosseim.
  Deep hedging with market impact, 2024.
  arXiv preprint arXiv:2402.13326.
* [15]

  Kenjiro Oya.
  Deep hedging bermudan swaptions, 2024.
* [16]

  Anish Rai, Buddha Nath Sharma, Salam Rabindrajit Luwang, Md. Nurujjaman, and Sushovan Majhi.
  Identifying extreme events in the stock market: A topological data analysis, 2024.
  arXiv preprint arXiv:2405.16052.