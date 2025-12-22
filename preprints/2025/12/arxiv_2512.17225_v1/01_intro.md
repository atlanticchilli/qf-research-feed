---
authors:
- Dimitrios Bachtis
- David S. Berman
- Arabella Schelpe
doc_id: arxiv:2512.17225v1
family_id: arxiv:2512.17225
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Modelling financial time series with ϕ⁴ quantum field theory
url_abs: http://arxiv.org/abs/2512.17225v1
url_html: https://arxiv.org/html/2512.17225v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dimitrios Bachtis
[d.bachtis@qmul.ac.uk](mailto:d.bachtis@qmul.ac.uk)
Centre for Theoretical Physics, Department of Physics and Astronomy,
Queen Mary University of London, London E1 4NS, United Kingdom
  
David S. Berman
[d.s.berman@qmul.ac.uk](mailto:d.s.berman@qmul.ac.uk)
Centre for Theoretical Physics, Department of Physics and Astronomy,
Queen Mary University of London, London E1 4NS, United Kingdom
  
Arabella Schelpe
[cacs2@cantab.net](mailto:cacs2@cantab.net)

(December 19, 2025)

###### Abstract

We use a ϕ4\phi^{4} quantum field theory with inhomogeneous couplings and explicit symmetry-breaking to model an ensemble of financial time series from the S&\&P 500 index. The continuum nature of the ϕ4\phi^{4} theory avoids the inaccuracies that occur in Ising-based models which require a discretization of the time series. We demonstrate this using the example of the 2008 global financial crisis. The ϕ4\phi^{4} quantum field theory is expressive enough to reproduce the higher-order statistics such as the market kurtosis, which can serve as an indicator of possible market shocks. Accurate reproduction of high kurtosis is absent in binarized models. Therefore Ising models, despite being widely employed in econophysics, are incapable of fully representing empirical financial data, a limitation not present in the generalization of the ϕ4\phi^{4} scalar field theory. We then investigate the scaling properties of the ϕ4\phi^{4} machine learning algorithm and extract exponents which govern the behavior of the learned couplings (or weights and biases in ML language) in relation to the number of stocks in the model. Finally, we use our model to forecast the price changes of the AAPL, MSFT, and NVDA stocks. We conclude by discussing how the ϕ4\phi^{4} scalar field theory could be used to build investment strategies and the possible intuitions that the QFT operations of dimensional compactification and renormalization can provide for financial modelling.

††preprint: APS/123-QED

## Introduction.—

Most financial market data is represented by time series, for example describing the evolution of stock prices. The study of financial time series allows one to construct trading, portfolio optimization and risk management strategies, and potentially early warning indicators for major financial events, such as global crises. It is therefore useful to develop methods which provide interpretable insights into the structure of financial time series.

![Refer to caption](fig1.png)


Figure 1:  The disordered ϕ4\phi^{4} scalar field theory in its representation as a complete graph where every distinct pair of fields is connected by a unique edge. The price change of each stock is mapped to a field ϕi\phi\_{i}, and each edge wi​jw\_{ij} extracts correlations between stock ϕi\phi\_{i} and the remaining stocks {ϕj,j∈Λ−i}\{\phi\_{j,j\in\Lambda-i}\}. Inhomogeneous external fields {ai}\{a\_{i}\}, which correspond to external news affecting the price change of a stock, break explicitly and locally the Z2Z\_{2} symmetry, thus biasing the price change to a positive or negative value.

A physical system commonly employed to study aspects of finance is the Ising model due to its Z2Z\_{2} symmetry, second-order phase transition, and the binary degrees of freedom which enable a representation of buy and sell dynamics [[1](https://arxiv.org/html/2512.17225v1#bib.bib1), [2](https://arxiv.org/html/2512.17225v1#bib.bib2), [3](https://arxiv.org/html/2512.17225v1#bib.bib3)]. The Ising model has been employed to study financial time series [[4](https://arxiv.org/html/2512.17225v1#bib.bib4), [5](https://arxiv.org/html/2512.17225v1#bib.bib5), [6](https://arxiv.org/html/2512.17225v1#bib.bib6), [7](https://arxiv.org/html/2512.17225v1#bib.bib7)], but it manifests limitations due to the binary degrees of freedom which necessitate a discretization of empirical financial data. The binarization 111We mostly use the term binarization in this paper, to refer to the transformation of continuous return values into (−1,1)(-1,1), although it is commonly referred to less precisely as discretization in the literature. of time series results in loss of crucial information about financial markets, for instance in the reproduction of high-order statistics that can serve as indicators of major financial events.

In this manuscript we propose the ϕ4\phi^{4} quantum field theory, a system with Z2Z\_{2} symmetry and continuous degrees of freedom, to model and forecast empirical financial time series. The ϕ4\phi^{4} field theory is a generalization of the Ising model, and reduces to the Ising model in a mathematical limit. This suggests that the ϕ4\phi^{4} theory should be as
successful as the Ising model, with the additional benefit of being able to model continuous degrees of freedom.
In addition, the ϕ4\phi^{4} theory is a nonlinear system, allowing for more complicated dependencies, while retaining complete interpretability. We investigate if the ϕ4\phi^{4} theory strikes a balance between
simplicity and representational capacity.

We specifically explore whether the ϕ4\phi^{4} quantum field theory can exhibit the advantages of the Ising model, without its limitations. To our knowledge, the ϕ4\phi^{4} scalar field theory has never been implemented to study financial time series. More general ϕn\phi^{n} models have been suggested for portfolio optimization [[9](https://arxiv.org/html/2512.17225v1#bib.bib9)], but without an exploration of the specific capabilities of the simpler restriction to n=4n=4. The ϕ4\phi^{4} theory has been additionally proposed as a multi-agent system of financial markets in Ref. [[10](https://arxiv.org/html/2512.17225v1#bib.bib10)].

We initiate our study by considering time series which include events such as the global financial crisis of 2008 in order to investigate if the disordered ϕ4\phi^{4} model, which is mathematically equivalent to a machine learning algorithm of a Markov random field [[11](https://arxiv.org/html/2512.17225v1#bib.bib11)], is able to faithfully reproduce market statistics that vanish in binarized series.

We then clarify how the ϕ4\phi^{4} machine learning algorithm is described by a set of interpretable weights and biases, in contrast to algorithms such as neural networks with hidden variables which lead to loss of interpretability of results. Consequently, we investigate scaling properties [[12](https://arxiv.org/html/2512.17225v1#bib.bib12)] by extracting exponents which describe the behavior of the weights and biases in relation to the number of stocks present within the S&\&P 500 index.

Finally, we investigate whether the ϕ4\phi^{4} scalar field theory, which is able to directly model the price changes of stocks, can be utilized to forecast time series. Specifically, we employ techniques of probabilistic machine learning pertinent to the sampling of missing degrees of freedom to predict the price changes for the AAPL, MSFT, and NVDA stocks.

We conclude by discussing how the ϕ4\phi^{4} scalar field theory could be employed to establish investment strategies and a framework for financial markets developed within quantum field theory based on the mathematical operations of dimensional compactification and renormalization.

## ϕ4\phi^{4} quantum-field theoretic machine learning.—

We define a discretized and fully disordered ϕ4\phi^{4} theory on a complete graph which is represented by the lattice action:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=−∑i,jwi​j​ϕi​ϕj+∑iμi​ϕi2+∑iλi​ϕi4−∑iai​ϕi,S=-\sum\_{i,j}w\_{ij}\phi\_{i}\phi\_{j}+\sum\_{i}\mu\_{i}\phi\_{i}^{2}+\sum\_{i}\lambda\_{i}\phi\_{i}^{4}-\sum\_{i}a\_{i}\phi\_{i}, |  | (1) |

where wi​jw\_{ij} is an inhomogeneous coupling connecting the ϕi\phi\_{i} and ϕj\phi\_{j} fields, μi\mu\_{i} and λi\lambda\_{i} are the inhomogeneous squared mass and lambda couplings, and aia\_{i} represents an external field that breaks explicitly and locally the Z2Z\_{2} symmetry. We denote the set of all lattice sites as Λ\Lambda and the volume of the system as VV. The ϕ4\phi^{4} scalar field theory is described by a Boltzmann probability distribution of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(ϕ,θ)=exp⁡[−S​(ϕ,θ)]Z,p(\bm{\phi},\theta)=\frac{\exp[-S(\bm{\phi},\theta)]}{Z}, |  | (2) |

where Z=∫−∞∞exp⁡[−S​(ϕ,θ)]​𝑑ϕZ=\int\_{-\infty}^{\infty}\exp[-S(\bm{\phi},\theta)]d\bm{\phi} is the partition function of the system, ϕ\bm{\phi} denotes a configuration comprising the fields {ϕi}\{\phi\_{i}\}, and θ\theta defines the set of the inhomogeneous couplings which are equivalent to learnable variational parameters within a machine learning setting. That is, θ\theta denotes the full set of learnable couplings {wi​j,μi,λi,ai}\{w\_{ij},\mu\_{i},\lambda\_{i},a\_{i}\}. From the perspective of physics, the system discussed herein is simultaneously a ϕ4\phi^{4} glass [[13](https://arxiv.org/html/2512.17225v1#bib.bib13)] and a ϕ4\phi^{4} inhomogeneous external field model. From the perspective of machine learning, the system discussed herein satisfies the Hammersley-Clifford theorem and is therefore a Markov random field [[11](https://arxiv.org/html/2512.17225v1#bib.bib11)]. As such the system possesses all the properties advantageous for machine learning of a Markov random field such as efficient gradient-based training and the applicability of simple and scalable sampling methods. For an illustration of the system, see Fig. [1](https://arxiv.org/html/2512.17225v1#S0.F1 "Figure 1 ‣ Introduction.— ‣ Modelling financial time series with ϕ⁴ quantum field theory").

![Refer to caption](fig2.png)


Figure 2:  Market mean (left) and market kurtosis (right), using a simple moving average of 250250 trading days, versus the trading year. The binarized mean value is normalized to reside between the minimum and maximum values of the original time series.

In this manuscript we map the price changes of stocks to the fields {ϕi}\{\phi\_{i}\} of a ϕ4\phi^{4} theory. A field ϕi\phi\_{i} is considered a random variable whose expectation value represents the price change of a stock ii on a particular day. We consider a different field theory and set of fields {ϕi}\{\phi\_{i}\} for each point in time and the time evolution of the financial system is represented by a time evolution in model space where the parameters of the theories evolve in time.

Our aim is to learn the most accurate set of couplings θ\theta which encode interpretable dependencies among the considered stocks. It is therefore necessary to clarify the role of the inhomogeneous couplings θ\theta using knowledge of the Z2Z\_{2} symmetry.

Specifically, the inhomogeneous edges wi​jw\_{ij} act as a weight and are related to the correlation between the two fields ϕi\phi\_{i} and ϕj\phi\_{j} 222To give some intuition about how these wi​jw\_{ij} differ from correlations, one example of their difference is that a correlation between ii and jj would be absolute, whereas the value of wi​jw\_{ij} is dynamic and will change depending on what set of stocks the model is learnt over.. When wi​j>0w\_{ij}>0 two fields ϕi\phi\_{i} and ϕj\phi\_{j} are positively correlated, giving rise to a ferromagnetic interaction, whereas when wi​j<0w\_{ij}<0 they are negatively correlated and are representative of an antiferromagnetic interaction. In addition, the inhomogeneous coupling aia\_{i} is an external field acting as a bias, which breaks explicitly and locally the symmetry of the system, and biases, depending on its sign, a given field ϕi\phi\_{i} towards a positive or negative value. Finally the inhomogeneous couplings μi\mu\_{i} and λi\lambda\_{i} can be tuned to drive a given field ϕi\phi\_{i} towards either the symmetric or the broken-symmetry phases.

By learning the aforementioned couplings, we are able to extract both internal information, through the set of weights {wi​j}\{w\_{ij}\} which express how the price changes of stocks are correlated with each other, and external information, through the set of biases {ai}\{a\_{i}\} which could express for example how the values of stocks are influenced by external news. We are additionally able to obtain insights into the scaling properties of the ϕ4\phi^{4} model, by investigating how the weights and biases evolve as we increase the lattice volume of the system or, equivalently, increase the number of modelled stocks.

To solve the problem of learning the most accurate values of the couplings θ\theta which accurately represent the coexistence and interaction of a number of stocks, we consider the Kullback-Leibler divergence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | KL(q||p)=∫−∞∞q(ϕ)lnq​(ϕ)p​(ϕ;θ)dϕ≥0,KL(q||p)=\int\_{-\infty}^{\infty}{q(\bm{\phi})}\ln\frac{q(\bm{\phi})}{p(\bm{\phi};\theta)}d\bm{\phi}\geq 0, |  | (3) |

between the Boltzmann probability distribution p​(ϕ,θ)p(\bm{\phi},\theta) of the ϕ4\phi^{4} theory and the empirical probability distribution q​(ϕ)q(\bm{\phi}). The empirical probability distribution q​(ϕ)q(\bm{\phi}) in this case simply comprises the values of the empirical time series at a given point in time. Derivations about the gradient-based approach implemented to minimize the Kullback-Leibler divergence are provided in the Supplemental Material 333See the Supplemental Material at [URL will be inserted by publisher] for definitions, simulation details, and supporting figures.

## Modelling financial time series.—

To illustrate applications of the ϕ4\phi^{4} scalar field theory for empirical financial data, we consider the log-returns for the time series of a subset of V=20V=20 stocks from the S&\&P 500 index. We assume that the subset of stocks forms a market and calculate statistics, such as the market mean and kurtosis. The initial date for the time series is 01/01/2013 and we extend the time series for 20002000 trading days in the past. The selected time range includes various major financial events, such as the global financial crisis of 2008. To smooth out short-term fluctuations, we apply a simple moving average of 250250 days to the data, which corresponds to one trading year. Details and definitions are provided in the Supplemental Material.

To illustrate that the ϕ4\phi^{4} scalar field theory provides advantages to the modelling of empirical time series in comparison to the binary Ising model, we compare statistics from the true empirical data, the ϕ4\phi^{4} model, and a binarized version of the original time series. The results are depicted in Fig. [2](https://arxiv.org/html/2512.17225v1#S0.F2 "Figure 2 ‣ ϕ⁴ quantum-field theoretic machine learning.— ‣ Modelling financial time series with ϕ⁴ quantum field theory"). We observe that the ϕ4\phi^{4} model can faithfully reproduce high-order statistics during major events such as the global financial crisis of 2008. These statistics include the market kurtosis, which can serve as an indicator of financial crises. The results from the ϕ4\phi^{4} model can be directly contrasted to the binarized version of the original time series that the Ising model would be able to reproduce, where information about high-order statistics such as the kurtosis is completely lost.

## Scaling properties and exponents of the learned parameters.—

The set of weights and biases of the ϕ4\phi^{4} scalar field theory are fully interpretable as they encode either direct correlations between the stocks or correspond to external factors (e.g. news). This is in contrast to machine learning algorithms which utilize hidden variables, where insights into interpretability are more intricate to obtain. Consequently, one is able to increase the lattice volume of the system by increasing the number of stocks modelled, in order to investigate scaling properties of the interpretable weights and biases. This implies that one can extract specific information about each market index in the form of exponents that capture properties of the stocks included within it.

To investigate scaling properties we then calculate the mean value of weights ⟨wi​j⟩=1Nwi​j​∑i​jwi​j\langle w\_{ij}\rangle=\frac{1}{N\_{w\_{ij}}}\sum\_{ij}w\_{ij}, and biases ⟨ai⟩=1Nai​∑iai\langle a\_{i}\rangle=\frac{1}{N\_{a\_{i}}}\sum\_{i}a\_{i}, where NN denotes the number of parameters. Since the weights represent dependencies among stocks, the mean value expresses whether a collection of stocks is positively or negatively correlated. The biases, or external fields, break explicitly the Z2Z\_{2} symmetry and their average therefore represents whether a collection of stocks is expected to increase or decrease in value. We then define two exponents kk in relation to the number of stocks VV, or equivalently, the lattice volume VV of the system as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨wi​j⟩∝Vkwi​j,⟨ai⟩∝Vkai.\langle w\_{ij}\rangle\propto V^{k\_{w\_{ij}}},\ \langle a\_{i}\rangle\propto V^{k\_{a\_{i}}}. |  | (4) |

We select V=64V=64 stocks from the S&\&P 500 index and calculate the average of their returns over 2020 years at a fixed point in time: 01/01/2023. By considering a large time range, we smooth out temporary local fluctuations. Details about the selection of subsets of V′=48,32,16V^{\prime}=48,32,16 stocks in order to conduct the scaling calculation are provided in the Supplemental Material.

The results of the finite size scaling analysis are depicted on logarithmic axes in Fig. [3](https://arxiv.org/html/2512.17225v1#S0.F3 "Figure 3 ‣ Scaling properties and exponents of the learned parameters.— ‣ Modelling financial time series with ϕ⁴ quantum field theory"). We observe the emergence of scaling properties for the weights and the biases of the ϕ4\phi^{4} scalar field theory. Specifically, through numerical fits we extract the values of two exponents kwi​j=−0.96​(1)k\_{w\_{ij}}=-0.96(1) and kai=−0.81​(1)k\_{a\_{i}}=-0.81(1). We repeat the calculation for a different date, namely 01/01/2013, and obtain values of kwi​j=−1.11​(4)k\_{w\_{ij}}=-1.11(4) and kai=−0.87​(3)k\_{a\_{i}}=-0.87(3). We remark that analogous calculations of scaling exponents have been conducted before using binarized series and the Ising model [[4](https://arxiv.org/html/2512.17225v1#bib.bib4)].

The results suggest the presence of nontrivial structure in the weights and biases for the considered S&\&P 500 index. It is interesting that the results for the two dates are so similar, and warrants further investigation into how the exponents vary over different time periods. Our initial consideration of a large moving average of 2020 years was to investigate the asymptotic limit, but it may be that the scaling properties for shorter time periods could be exploited in investment strategies.

![Refer to caption](fig3.png)


Figure 3:  Mean values of the weights (top) and biases (bottom) versus the lattice volume VV of the ϕ4\phi^{4} theory or, equivalently, the number of modelled stocks VV from the S&\&P 500 index. The axes are logarithmic.

## Forecasting financial time series.—

Before illustrating the forecasting capabilities of the ϕ4\phi^{4} theory we first consider an easier problem of filling in missing data. We train the model on a dataset comprising the returns for the time series of the AAPL, MSFT and NVDA stocks. We then employ techniques of probabilistic machine learning, pertinent to the sampling of missing degrees of freedom, to predict the price changes of stocks for trading days that are not included in the training dataset.

In more detail, the question we aim to answer for a specific trading day is “If the price change of the AAPL stock is ϕA​A​P​L\phi\_{AAPL}, and the price change of the MSFT stock is ϕM​S​F​T\phi\_{MSFT}, what will the price change ϕN​V​D​A\phi\_{NVDA} of the NVDA stock be?”. In a mathematically formal representation, this question can be expressed in terms of conditional probability distributions as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(ϕN​V​D​A|ϕA​A​P​L,ϕM​S​F​T).p(\phi\_{NVDA}|\phi\_{AAPL},\phi\_{MSFT}). |  | (5) |

The results, obtained by sampling the conditional probability distribution, are depicted in Fig. [4](https://arxiv.org/html/2512.17225v1#S0.F4 "Figure 4 ‣ Forecasting financial time series.— ‣ Modelling financial time series with ϕ⁴ quantum field theory"). We compare the ϕ4\phi^{4} result for the NVDA stock against a baseline prediction RR calculated based on the rescaled mean of the two remnant stocks as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RN​V​D​A=σN​V​D​A2​(ϕA​A​P​LσA​A​P​L+ϕM​S​F​TσM​S​F​T),R\_{NVDA}=\frac{\sigma\_{NVDA}}{2}\Bigg(\frac{\phi\_{AAPL}}{\sigma\_{AAPL}}+\frac{\phi\_{MSFT}}{\sigma\_{MSFT}}\Bigg), |  | (6) |

where σ\sigma corresponds to the standard deviation of a stock in the time window of the training dataset.

We observe approximate agreement with the true data although with inevitable discrepancies since the price change of the stock will also be influenced by other factors, for example momentary news that the algorithm currently has no access to. The mean absolute errors for the ϕ4\phi^{4} result and the rescaled mean prediction are 0.0190.019 and 0.0230.023, respectively. The ϕ4\phi^{4} result performs slightly better, but over too little data to make a firm statement and for the moment we consider the two methods to be of comparable performance. However, importantly, the rescaled mean method can only be employed in cases of highly correlated stocks, whereas we can expect the ϕ4\phi^{4} method to also be applicable to situations with lower correlations. This calculation in its current form cannot be exploited for trading, as the opening times of the predictor and predicted stocks are simultaneous. In order to convert it to a forecasting setup, it could be used on different correlated stocks with disjoint opening times, or by shifting the predicted stock’s returns forward by one time step in the training stage.

![Refer to caption](fig4.png)


Figure 4:  NVDA returns versus the trading day, for the original time series, predictions from the ϕ4\phi^{4} model and a rescaled mean calculation using the simultaneous returns of AAPL and MSFT as predictors. The x axis corresponds to dates for October 2022.

A simpler forecasting set up is to forecast a stock price for the upcoming trading day, based on that stock’s historical returns. To obtain a prediction for the upcoming trading day with the ϕ4\phi^{4} scalar field theory, we consider the case of the AAPL stock, and construct a dataset where each training point comprises the returns ϕi\phi\_{i} of a given trading day ii and the preceding 149 trading days. If we denote future and past trading days with positive or negative subscripts, respectively, and the returns of the current trading day as ϕ0\phi\_{0}, the ϕ4\phi^{4} machine learning algorithm learns a joint probability distribution p​({ϕi,ϕi−1,…,ϕi−149})p(\{\phi\_{i},\phi\_{i-1},\ldots,\phi\_{i-149}\}), where i≤0i\leq 0. One then observes that once the closing price ϕ0\phi\_{0} of a stock is obtained for the current trading day one can utilize the learned weights and biases encoded in the aforementioned joint probability distribution to ask the question “What will the price change ϕ1\phi\_{1} of the AAPL stock be tomorrow, given the price change ϕ0\phi\_{0} today and the price changes ϕi\phi\_{i} of the past 148 trading days?”, or formally, one can sample the conditional probability distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(ϕ1|ϕ0,…,ϕ−148).p(\phi\_{1}|\phi\_{0},\ldots,\phi\_{-148}). |  | (7) |

The results of predicting the closing price for the upcoming trading day in the case of the AAPL stock are depicted in Fig. [5](https://arxiv.org/html/2512.17225v1#S0.F5 "Figure 5 ‣ Forecasting financial time series.— ‣ Modelling financial time series with ϕ⁴ quantum field theory"). To probe the efficiency of the prediction we calculate the mean absolute error, and compare the results against a baseline calculation using linear regression with a rolling window. The comparison of the two algorithms is depicted in Fig. [6](https://arxiv.org/html/2512.17225v1#S0.F6 "Figure 6 ‣ Forecasting financial time series.— ‣ Modelling financial time series with ϕ⁴ quantum field theory") where we observe that the ϕ4\phi^{4} theory performs favorably by resulting in a lower value of the mean absolute error for all window sizes of the linear regression up to at least 400400 days. The effective training window of the ϕ4\phi^{4} model is 230 days and, as can be seen from the plot, the error in the linear regression is comfortably above the ϕ4\phi^{4} model at that window size. Details about the implementation are provided in the Supplemental Material.

![Refer to caption](aaplforecast.png)


Figure 5:  Forecasting of the AAPL returns for the upcoming trading day using the ϕ4\phi^{4} theory with historical AAPL returns as predictor. The x axis corresponds to dates for October 2024.

![Refer to caption](lrphi.png)


Figure 6:  Mean absolute error for the forecasting of AAPL price changes using linear regression versus the rolling window size. The dashed line corresponds to the mean absolute error of the ϕ4\phi^{4} theory, where the statistical uncertainty is comparable with the width of the dashed line.

## Conclusions–

We proposed a disordered ϕ4\phi^{4} quantum field theory, which is mathematically equivalent to a machine learning algorithm of a Markov random field, to model and forecast financial time series.

Specifically, we have shown advantages of the ϕ4\phi^{4} quantum field-theoretic machine learning algorithm in relation to the Ising model by demonstrating that it can reproduce high-order statistics for empirical financial time series, such as the market kurtosis, which can serve as an indicator of financial crises. This crucial information is lost in binarized series reproduced by Ising models. We additionally investigated scaling properties for the S&\&P 500 index by extracting exponents which govern the behavior of the learned weights and biases in relation to the number of stocks. Finally, we employed the ϕ4\phi^{4} scalar field theory to forecast price changes of AAPL, MSFT, and NVDA stocks.

Our initial results show some promise that the ϕ4\phi^{4} model could be used to build investment strategies, for instance by filling in missing data, predicting the price change of a stock in a market with a disjoint opening time or forecasting the price change of an upcoming trading day. We have illustrated improvements in performance over some simple baseline strategies. The purpose of this was to demonstrate that this approach has potential, not yet to present fully formulated investment strategies which could be employed in live trading. We leave to future work further exploration of the model’s capabilities.
The scaling results for the weights and biases of the theory hint at the possibility of uncovering features of market structure, which once more fully explored may be able to be exploited. The external biases could also be specified to enrich the behavior the model can capture. Finally, the model may have sufficient predictive power for more than one day ahead prediction and forecasts a full probability distribution, and so could be used to produce predictions for option prices, or in transaction cost minimizing trajectories [[16](https://arxiv.org/html/2512.17225v1#bib.bib16)].

We remark that one envisages, based on the ϕ4\phi^{4} model, an opportunity to develop a framework for financial markets within quantum field theory. Specifically, the ϕ4\phi^{4} theory discussed herein can be viewed as a dimensionally compactified version of a generalized model. Explicitly, one is able to progressively add dimensions to the system, such as a dimension which corresponds to the time evolution of the series, or an additional dimension that relates stocks positioned within market indices of different countries. These generalized and d-dimensional ϕ4\phi^{4} scalar field theories would then be capable of extracting a set of more sophisticated dependencies. Via a simultaneous application of the mathematical operations of dimensional compactification and renormalization of the learned couplings one would then be able to recover mathematically either the model discussed in this manuscript or one representing intricate dependencies between multiple market indices.

To summarize, we have shown advantages of the ϕ4\phi^{4} quantum field theory, a system that is able to directly model the continuous values of price changes for stocks, in relation to spin models traditionally employed in applications of econophysics which necessitate a binarization of time series and lead to loss of crucial information about the structure of financial markets. As a result, we anticipate merits in the implementation, investigation, and extension of ideas from quantum field theory to the research field of finance.

## Data Availability Statement.—

Code to implement the disordered ϕ4\phi^{4} machine learning algorithm for financial data will be made publicly available with the published manuscript on Ref. 444https://github.com/dbachtis/phi4fin. Data which support the results of this manuscript are available from the authors upon request.

## Acknowledgements.—

The authors acknowledge support from the Science and Technology Facilities
Council (STFC) Consolidated Grant ST/X00063X/1 “Amplitudes, Strings & Duality”. This project has not received commercial funding.

## References

* Krawiecki *et al.* [2002]
  A. Krawiecki, J. A. Hołyst, and D. Helbing, Volatility clustering and
  scaling for financial time series due to attractor bubbling, [Phys. Rev. Lett. 89, 158701 (2002)](https://doi.org/10.1103/PhysRevLett.89.158701).
* Sornette and Zhou [2006]
  D. Sornette and W.-X. Zhou, Importance of positive
  feedbacks and overconfidence in a self-fulfilling ising model of financial
  markets, [Physica A: Statistical Mechanics and its
  Applications 370, 704
  (2006)](https://doi.org/10.1016/j.physa.2006.02.022).
* Chowdhury and Stauffer [1999]
  D. Chowdhury and D. Stauffer, A generalized spin model
  of financial markets, [The European Physical Journal B -
  Condensed Matter and Complex Systems 8, 477 (1999)](https://doi.org/10.1007/s100510050714).
* Borysov *et al.* [2015]
  S. S. Borysov, Y. Roudi, and A. V. Balatsky, U.s. stock market interaction network
  as learned by the boltzmann machine, [The European Physical Journal B 88, 321 (2015)](https://doi.org/10.1140/epjb/e2015-60282-3).
* Zeng *et al.* [2014]
  H.-L. Zeng, R. Lemoy, and M. Alava, Financial interaction networks inferred from
  traded volumes, [Journal of Statistical Mechanics:
  Theory and Experiment 2014, P07008 (2014)](https://doi.org/10.1088/1742-5468/2014/07/P07008).
* ichi Maskawa [2002]
  J. ichi
  Maskawa, Ordered phase and
  non-equilibrium fluctuation in stock market, [Physica A: Statistical Mechanics and its
  Applications 311, 563
  (2002)](https://doi.org/https://doi.org/10.1016/S0378-4371(02)00818-X).
* Bury [2013]
  T. Bury, Statistical pairwise
  interaction model of stock market, [The European Physical Journal B 86, 89 (2013)](https://doi.org/10.1140/epjb/e2013-30598-1).
* Note [1]
  We mostly use the term binarization in this paper, to refer
  to the transformation of continuous return values into (−1,1)(-1,1), although it
  is commonly referred to less precisely as discretization in the
  literature.
* Sornette *et al.* [2000]
  D. Sornette, P. Simonetti, and J. Andersen, ϕq\phi^{q}-field theory
  for portfolio optimization: “fat tails” and nonlinear correlations, [Physics Reports 335, 19 (2000)](https://doi.org/https://doi.org/10.1016/S0370-1573(00)00004-1).
* Bachtis [2024a]
  D. Bachtis, [Lattice ϕ4\phi^{4} field theory as a multi-agent system of financial
  markets](https://arxiv.org/abs/2411.15813) (2024a), [arXiv:2411.15813 [cond-mat.dis-nn]](https://arxiv.org/abs/2411.15813)
  .
* Bachtis *et al.* [2021]
  D. Bachtis, G. Aarts, and B. Lucini, Quantum field-theoretic machine
  learning, [Phys. Rev. D 103, 074510 (2021)](https://doi.org/10.1103/PhysRevD.103.074510).
* Bachtis *et al.* [2024]
  D. Bachtis, G. Biroli,
  A. Decelle, and B. Seoane, Cascade of phase transitions in the training of
  energy-based models, in [*Advances in Neural Information Processing
  Systems*](https://proceedings.neurips.cc/paper_files/paper/2024/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf), Vol. 37, edited by A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (Curran Associates,
  Inc., 2024) pp. 55591–55619.
* Bachtis [2024b]
  D. Bachtis, [Disordered lattice glass ϕ4\phi^{4} quantum field theory](https://arxiv.org/abs/2407.06569) (2024b), [arXiv:2407.06569 [hep-lat]](https://arxiv.org/abs/2407.06569) .
* Note [2]
  To give some intuition about how these wi​jw\_{ij} differ from
  correlations, one example of their difference is that a correlation between
  ii and jj would be absolute, whereas the value of wi​jw\_{ij} is dynamic and
  will change depending on what set of stocks the model is learnt
  over.
* Note [3]
  See the Supplemental Material at [URL will be inserted by
  publisher] for definitions, simulation details, and supporting
  figures.
* Garleanu and Pedersen [2013]
  N. Garleanu and L. Pedersen, Dynamic trading with
  predictable returns and transaction costs, [The Journal of Finance 68, 2309 (2013)](https://doi.org/10.1111/jofi.12080).
* Note [4]
  https://github.com/dbachtis/phi4fin.

![[Uncaptioned image]](x1.png)![[Uncaptioned image]](x2.png)![[Uncaptioned image]](x3.png)![[Uncaptioned image]](x4.png)![[Uncaptioned image]](x5.png)