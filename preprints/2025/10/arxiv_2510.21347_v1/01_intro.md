---
authors:
- Sina Molavipour
- Alireza M. Javid
- Cassie Ye
- Björn Löfdahl
- Mikhail Nechaev
doc_id: arxiv:2510.21347v1
family_id: arxiv:2510.21347
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks
url_abs: http://arxiv.org/abs/2510.21347v1
url_html: https://arxiv.org/html/2510.21347v1
venue: arXiv q-fin
version: 1
year: 2025
---


Sina Molavipour, Alireza M. Javid, Cassie Ye, Björn Löfdahl, Mikhail Nechaev
[sina.molavipour,alireza.javid,cassie.ye,bjorn.lofdahl,mikhail.nechaev@seb.se](mailto:sina.molavipour,alireza.javid,cassie.ye,bjorn.lofdahl,mikhail.nechaev@seb.se)
SEB Group, Stockholm, Sweden

###### Abstract.

Robust yield curve estimation is crucial in fixed-income markets for accurate instrument pricing, effective risk management, and informed trading strategies. Traditional approaches, including the bootstrapping method and parametric Nelson-Siegel models, often struggle with overfitting or instability issues, especially when underlying bonds are sparse, bond prices are volatile, or contain hard-to-remove noise. In this paper, we propose a neural network-based framework for robust yield curve estimation tailored to small mortgage bond markets. Our model estimates the yield curve independently for each day and introduces a new loss function to enforce smoothness and stability, addressing challenges associated with limited and noisy data. Empirical results on Swedish mortgage bonds demonstrate that our approach delivers more robust and stable yield curve estimates compared to existing methods such as Nelson-Siegel-Svensson (NSS) and Kernel-Ridge (KR). Furthermore, the framework allows for the integration of domain-specific constraints, such as alignment with risk-free benchmarks, enabling practitioners to balance the trade-off between smoothness and accuracy according to their needs.

Yield curve estimation, mortgage bond, neural network

††Workshop on AI Meets Quantitative Finance (held within ICAIF 2025, Singapore, November 2025)

## 1. Introduction

The yield curve is a fundamental building block that underpins the pricing, valuation, and risk measurement of a broad spectrum of financial instruments, including bonds, FRNs, repos, and various structured products. Accurate estimation of the term structure of interest rates, commonly referred to as the yield curve, holds paramount importance for a wide range of stakeholders, including investors, policymakers, and financial institutions. In risk management, yield curves provide essential input for calculating various risk measurements, such as sensitivities and value-at-risk. Different central banks that utilize yield curve information employ Yield Curve Control (YCC) to sell or buy bonds, thereby maintaining the long-term interest rate at the target level to stimulate investments, support the economy, and control inflation. Short-term treasury yields are reflecting market expectations of central banks’ policy changes, such as rate cuts or hikes. Traders rely on yield curve information to decide on trading strategies, such as riding the yield curve to profit from the upward slope in a stable interest rate environment. Yield curves also reflect the overall market condition and expectation. The 10Y−-2Y Treasury yield spread is an indicator of overall market expectations. An inverted yield curve may indicate expectations of lower future interest rates or a potential slowdown in future growth. While yield curve segments range from treasury yields and corporate bond yields to mortgage or covered bond yields, the overall estimation techniques can be horizontally applied regardless of the segments. The yield curve represents spot rates (current market yield) for bonds of different maturities, which can be estimated for a given set of bonds of similar features within a segment. The prominent influence of the yield curve in finance and economics suggests that any inaccuracies in its estimation can propagate into significant mis-pricings, suboptimal risk and trading management strategies, and potentially flawed monetary policy decisions. This establishes a high standard for model accuracy and robustness, thereby motivating the continuous pursuit of advanced estimation methodologies. Analyzing and calibrating the estimated curves and rates are among the main daily routines in financial institutions. It is especially challenging for smaller market caps, with issuances often concentrated around short to mid-term periods and sparser over the long term, such as Swedish covered bonds.

The estimation of the yield curve has evolved, shifting from flexible, non-parametric methods to more structured, parametric models. Early techniques often relied on spline-based methods—such as quadratic, cubic, exponential, and B-splines (McCulloch, [1971](https://arxiv.org/html/2510.21347v1#bib.bib9), [1975](https://arxiv.org/html/2510.21347v1#bib.bib10)), which provided flexibility and could fit observed data well. However, these methods often led to unstable or irregular shapes, especially at the short and long ends of the curve (Nelson and Siegel, [1987](https://arxiv.org/html/2510.21347v1#bib.bib11)). To address these issues, the Nelson-Siegel (NS) model was introduced in (Nelson and Siegel, [1987](https://arxiv.org/html/2510.21347v1#bib.bib11)), offering a simple parametric form that aimed to capture key properties of a well-behaved yield curve, including smoothness, continuity, and the ability to represent both level and slope changes. Svensson later extended this model by adding more flexibility to the curve’s shape (Svensson, [1994](https://arxiv.org/html/2510.21347v1#bib.bib13)), which is referred to as the Nelson-Siegel-Svensson (NSS) model. Later on, the dynamic Nelson-Siegel (DNS) model extends this framework by modeling the evolution of the yield curve’s underlying factors over time, enabling forecasting and capturing the temporal dynamics of interest rates based on historical data (Diebold and Li, [2006](https://arxiv.org/html/2510.21347v1#bib.bib4); Diebold et al., [2008](https://arxiv.org/html/2510.21347v1#bib.bib5)). In contrast to the NSS method, functional approximation can be achieved through a linear combination of kernel functions and weights, where the functions are determined by solving an error loss function based on bond prices or yield rates. In a recent paper, authors in (Filipovic et al., [2022](https://arxiv.org/html/2510.21347v1#bib.bib6)) introduce a kernel ridge (KR) model and show a closed-form solution by introducing a regularized loss incorporating smoothness of the curve, and argue that the estimates outperform existing parametric and non-parametric methods.

From a machine learning standpoint, estimating the yield curve from bond data can be treated as a functional approximation problem, where feedforward neural networks are known to be effective (Hornik et al., [1989](https://arxiv.org/html/2510.21347v1#bib.bib7)). While neural networks (NN) have been previously used for forecasting the yield curve over time  (Kauffmann et al., [2022](https://arxiv.org/html/2510.21347v1#bib.bib8); Bahaa Aly and El-Masry, [2025](https://arxiv.org/html/2510.21347v1#bib.bib2)), for example by extending the dynamic Nelson-Siegel (DNS) framework, we use neural networks to model the yield curve independently for each day, without relying on temporal dependency across days, as a direct extension of NSS and KR models which has not been attempted in the literature. We demonstrate that core properties of the yield curve—such as smoothness and stability—can be enforced through the design of a novel loss function during training. Our main contributions are:

1. (1)

   We demonstrate that our neural network-based model provides a more robust yield curve estimate compared to the existing methods, such as NSS and KR.
2. (2)

   Our results demonstrate improved stability and reduced sensitivity to noise or fluctuations in bond prices, particularly in a small-data setting such as the Swedish mortgage bond market.
3. (3)

   Our novel loss function enables the integration of domain-specific constraints (e.g., alignment with risk-free benchmarks), while balancing the trade-offs between accuracy and smoothness.

In Section [2](https://arxiv.org/html/2510.21347v1#S2 "2. Preliminaries and related works ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"), we define the problem of yield curve estimation based on a set of underlying bonds and review several standard estimation techniques.
Section [3](https://arxiv.org/html/2510.21347v1#S3 "3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks") presents our proposed neural network architecture and the corresponding loss functions used to regularize training.
In Section [4](https://arxiv.org/html/2510.21347v1#S4 "4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"), we describe our experimental setup. We begin with hyperparameter tuning, followed by an evaluation of our model’s performance in terms of robustness to outliers, day-to-day stability, and the trade-off between smoothness and flexibility in a leave-one-out setup.
Finally, Section [5](https://arxiv.org/html/2510.21347v1#S5 "5. Conclusion ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks") summarizes our findings and outlines potential directions for future research.

## 2. Preliminaries and related works

In this section, we cover some of the known methods for estimating the yield curve. Let y​(t)y(t) be the spot yield rate at maturity time tt, commonly in years. Let f​(t)f(t) denote the forward curve at maturity tt. The yield rate can then be computed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | y​(t)=1t​∫0tf​(τ)​𝑑τ.y(t)=\frac{1}{t}\int\_{0}^{t}f(\tau)d\tau. |  |

In order to estimate the present value of a bond, the face-value and future cashflow payments must be discounted to the present time. Assuming a given yield curve y​(t)y(t), the discount factor at time tt can be calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | d​(t)=e−t​y​(t),d(t)=e^{-ty(t)}, |  |

where we use the notion of continuous compounding, although market practices may vary depending on the instrument. Consider a dataset of MM bonds sold in the market on a given day. The present value of the bond jj with njn\_{j} periodic cashflows can be estimated as:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | p^j=∑i=1nj−1cj(i)​d​(tj(i))+(cj(nj)+Fj)​d​(Tj),j∈1,…,M.\hat{p}\_{j}=\sum\_{i=1}^{n\_{j}-1}c^{(i)}\_{j}d\left(t^{(i)}\_{j}\right)+\left(c^{(n\_{j})}\_{j}+F\_{j}\right)d\left(T\_{j}\right),\qquad j\in{1,\dots,M}. |  |

where tj(i)t\_{j}^{(i)}s are cashflow dates (in years), cj(i)c\_{j}^{(i)} is the cashflow amount at time tj(i)t\_{j}^{(i)}, and FjF\_{j} is the face-value of the bond maturing at Tj=tj(nj)T\_{j}=t\_{j}^{(n\_{j})}. The present value of the bond can then be compared with its currently observed market price pjp\_{j} to evaluate the estimation accuracy of the yield curve y​(t)y(t). In other words, we would want to have ∑j=1M(pj−p^j)=0\sum\_{j=1}^{M}(p\_{j}-\hat{p}\_{j})=0 in an ideal situation. Estimating the yield curve, or equivalently, the discount curve, for this set of equations is non-trivial, and various approaches can be employed. According to ([3](https://arxiv.org/html/2510.21347v1#S2.E3 "Equation 3 ‣ 2. Preliminaries and related works ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")), and the number of bonds observed in the market MM, the problem is under-determined due to having discrete observations for a continuous function, resulting in a non-smooth curve that aims to satisfy this set of constraints. The resulting discrete points require interpolation to create a continuous curve. However, naive interpolation can produce forward curves with negative rates or excessive volatility since we have f​(t)=y​(t)+t​d​y​(t)d​tf(t)=y(t)+t\frac{dy(t)}{dt}.

One of the most fundamental techniques for constructing a zero-coupon yield curve is the bootstrapping method, which enables practitioners to derive appropriate discount rates from observable market bond quotes. The method incrementally builds the yield curve by solving for the implied spot rates sequentially, starting with the bond of the shortest maturity and then using that solution to solve for the bond with the second shortest maturity, and so forth. This recursive structure makes bootstrapping particularly robust when a complete set of liquid bond instruments exists across the desired maturity spectrum. However, real-world limitations such as non-uniform maturities, pricing errors, and liquidity constraints can make the process sensitive to data quality and interpolation methods.

The bootstrapping method is widely used in practice for constructing term structures of interest rates, particularly for risk-free rates such as those derived from government securities or Overnight Index Swaps (OIS). While intuitive and relatively easy to implement, bootstrapping does not enforce smoothness across the curve, which can lead to local irregularities unless post-processing or interpolation (e.g., spline fitting) is applied.

### 2.1. Nelson-Siegel-Svensson

Nelson-Siegel (Nelson and Siegel, [1987](https://arxiv.org/html/2510.21347v1#bib.bib11)) used a parsimonious parametric functional form to model the forward rate:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | fN​S​(t)=β0+β1​e−tλ+β2​tλ​e−tλ,f\_{NS}(t)=\beta\_{0}+\beta\_{1}e^{-\frac{t}{\lambda}}+\beta\_{2}\frac{t}{\lambda}e^{-\frac{t}{\lambda}}, |  |

and accordingly, the yield curve is obtained using ([1](https://arxiv.org/html/2510.21347v1#S2.E1 "Equation 1 ‣ 2. Preliminaries and related works ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")):

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | yNS​(t)=β0+β1​1−e−t/λt/λ+β2​(1−e−t/λt/λ−e−t/λ).y\_{\text{NS}}(t)=\beta\_{0}+\beta\_{1}\frac{1-e^{-t/\lambda}}{t/\lambda}+\beta\_{2}\left(\frac{1-e^{-t/\lambda}}{t/\lambda}-e^{-t/\lambda}\right). |  |

The motivation for this parametric model was to capture the common shapes of the yield curve, including monotonic forms and extreme points in specific parts of the curve. Later, more terms were added to the model by Svensson (Svensson, [1994](https://arxiv.org/html/2510.21347v1#bib.bib13)) to capture more complex behavior in the rates:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | fNSS​(t)=β0+β1​e−t/λ1+β2​(tλ1⋅e−t/λ1)+β3​(tλ2​e−t/λ2),f\_{\text{NSS}}(t)=\beta\_{0}+\beta\_{1}e^{-t/\lambda\_{1}}+\beta\_{2}\left(\frac{t}{\lambda\_{1}}\cdot e^{-t/\lambda\_{1}}\right)+\beta\_{3}\left(\frac{t}{\lambda\_{2}}e^{-t/\lambda\_{2}}\right), |  |

which results in:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (7) |  | yNSS​(t)=\displaystyle y\_{\text{NSS}}(t)= | β0+β1​1−e−t/λ1t/λ1+β2​(1−e−t/λ1t/λ1−e−t/λ1)\displaystyle\beta\_{0}+\beta\_{1}\frac{1-e^{-t/\lambda\_{1}}}{t/\lambda\_{1}}+\beta\_{2}\left(\frac{1-e^{-t/\lambda\_{1}}}{t/\lambda\_{1}}-e^{-t/\lambda\_{1}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (8) |  |  | +β3​(1−e−t/λ2t/λ2−e−t/λ2).\displaystyle+\beta\_{3}\left(\frac{1-e^{-t/\lambda\_{2}}}{t/\lambda\_{2}}-e^{-t/\lambda\_{2}}\right). |  |

Although this model has been extensively applied in finance and banking (Nymand-Andersen, [2018](https://arxiv.org/html/2510.21347v1#bib.bib12); Bolder and Stréliski, [1999](https://arxiv.org/html/2510.21347v1#bib.bib3)), it exhibits several limitations. A well-known issue is the lack of robustness in its estimations. In practical applications, the bond dataset often undergoes cleaning, with bonds being added or removed depending on market conditions. As a result, the estimated yield curves derived from these parsimonious models can vary significantly, particularly in the short/long end of the curve.

### 2.2. Kernel-ridge method

In this approach, the discount function is modeled by kernel functions. In a recent work (Filipovic et al., [2022](https://arxiv.org/html/2510.21347v1#bib.bib6)), the authors show that there is a unique closed-form solution when using this model to optimize the price error while incorporating smoothness conditions in the objective function:

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | mind​∑j=1Mωj​(pj−p^j)2+λ​‖d‖2,\min\_{d}\textstyle\sum\_{j=1}^{M}\omega\_{j}(p\_{j}-\hat{p}\_{j})^{2}+\lambda||d||^{2}, |  |

for some smoothness parameter λ>0\lambda>0, where the norm in the second term is defined by the weighted average of the first and second derivative of d​(⋅)d(\cdot) to ensure the smoothness (see (Filipovic et al., [2022](https://arxiv.org/html/2510.21347v1#bib.bib6))).
Then, by writing the kernel representation for the discount function as below, the optimization problem can be solved:

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | d^​(t)=1+∑l=1Lαl​k​(t,tl).\hat{d}(t)=1+\textstyle\sum\_{l=1}^{L}\alpha\_{l}k(t,t\_{l}). |  |

k​(t,tl)k(t,t\_{l}) are kernel functions that form a RKHS (reproducing kernel Hilbert space). So, the corresponding kernel matrix KK is constructed by Km​l=k​(tm,tl)K\_{ml}=k(t\_{m},t\_{l}). The closed-form solution determines both the weights αl\alpha\_{l} and the KK based on boundary conditions on the smoothness criteria. In this paper, we refer to this method as KR where we set the weights ωj\omega\_{j} as inversely proportional to the squared duration DjD\_{j}, that is ωj=1M​1(Dj​pj)2\omega\_{j}=\frac{1}{M}\frac{1}{(D\_{j}p\_{j})^{2}}, which approximates the mean squared yield fitting error as stated in (Filipovic et al., [2022](https://arxiv.org/html/2510.21347v1#bib.bib6)). We found that this choice of ωj\omega\_{j} results in a smoother yield curve that is less sensitive to sporadic price changes in small-sized markets such as mortgage bonds.

## 3. Neural network estimation

Neural networks are well-studied methods in machine learning and are widely used to estimate complex models due to their approximation power. In this paper, we investigate how neural networks can be used to estimate the yield curve y​(t)y(t), and tailor the objective function to reflect more complex criteria on the obtained curve. We argue that the main advantage of using neural networks is robustness in estimation and their flexibility to handle extra criteria, such as maintaining the economical reasonableness of the curve in various market conditions.

Since the mortgage bond market is commonly less liquid and populated than other markets (particularly in Sweden), the available data for training is relatively limited. Consequently, we adopt simple feed-forward neural network architectures with shallow layers and a small number of neurons to ensure effective parameter training. The quest for the most suitable architecture to achieve the best estimation accuracy is out of the scope of this paper. For a given activation function ϕ(.)\phi(.), our model takes the maturity time tt as input and produces the estimated yield rate y^​(t)\hat{y}(t) at the output layer:

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | y^​(t)=∑i=1Hvi​ϕ​(wi⋅t+bi)+c,\hat{y}(t)=\textstyle\sum\_{i=1}^{H}v\_{i}\phi(w\_{i}\cdot t+b\_{i})+c, |  |

where HH is the number of hidden neurons.

### 3.1. Loss function

There are various ways to explain a “good” yield curve. When constructing yield curves for mortgage-backed securities, analysts must strike a delicate balance between market accuracy and economic plausibility. This trade-off arises from two competing objectives:

1. (1)

   Accuracy: The curve must precisely replicate observed market prices of mortgage bonds to ensure valid risk management calculations and hedge effectiveness. This can also be seen by comparing the yield values with the yield-to-maturity (YTM) of the underlying bonds.
2. (2)

   Economic Reasonableness: The curve must maintain a logical relationship in terms of smoothness and trend with risk-free benchmarks.

The comparison between the present value of bonds and their market prices is a well-established technique for addressing the accuracy of the estimation. This can be reflected in:

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | ℒerror=1M​∑j=1M(pj−p^j)2.\mathcal{L}\_{\text{error}}=\frac{1}{M}\textstyle\sum\_{j=1}^{M}(p\_{j}-\hat{p}\_{j})^{2}. |  |

Additional criteria can guide the estimation toward a more well-behaved yield curve.

A key aspect of conventional methods is the use of relatively smooth functions to model the yield curve. This smoothness can be enforced in the objective function by incorporating derivative terms of the estimated yield curve.
Consider a set of NN ordered fixed maturity grid points t→=[t1,…,tN]\vec{t}=[t\_{1},\dots,t\_{N}]. Then, by computing the slope of the estimated curve at these points, we add the following penalty term to ([12](https://arxiv.org/html/2510.21347v1#S3.E12 "Equation 12 ‣ 3.1. Loss function ‣ 3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")):

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | ℒsmooth=maxi=2,…,N⁡|y^​(ti)−y^​(ti−1)ti−ti−1|.\mathcal{L}\_{\text{smooth}}=\max\_{i=2,\dots,N}|\frac{\hat{y}(t\_{i})-\hat{y}(t\_{i-1})}{t\_{i}-t\_{i-1}}|. |  |

![Refer to caption](Pics/hyperparam-merged.png)


Figure 1. Hyperparameter tuning for learning rate (LR), number of epochs, γ1\gamma\_{1}, and γ2\gamma\_{2} in a falling market (3/6/2024). Left: varying LR and epochs. Center: varying γ2\gamma\_{2}. Right: varying γ1\gamma\_{1}.

Another criterion to consider is the economical reasonableness of the estimated curve in various market conditions. For instance, to evaluate the risk premium of a mortgage bond, it is common practice to compare the bond’s yield to a benchmark yield curve. One widely used benchmark is an OIS (Overnight Index Swap) or RFR (Risk-Free Rate) curve, which is considered nearly risk-free. Unlike mortgage and corporate bond yield curves, OIS/RFR curves have minimal credit risk and liquidity premia. Such curves include the SOFR (Secured Overnight Financing Rate) curve in the U.S. market, the €STR (Euro Short-term Rate) in the Eurozone, and the STINA (SEK Overnight Index Swaps) in the Swedish market. To fulfill this criterion, we introduce the penalty term below:

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | ℒtrend=1N​∑i=2N|(y^​(ti)−y^​(ti−1))−(yOIS​(ti)−yOIS​(ti−1))ti−ti−1|.\mathcal{L}\_{\text{trend}}=\frac{1}{N}\textstyle\sum\_{i=2}^{N}\left|\frac{\left(\hat{y}(t\_{i})-\hat{y}(t\_{i-1})\right)-\left(y\_{\text{\scriptsize OIS}}(t\_{i})-y\_{\text{\scriptsize OIS}}(t\_{i-1})\right)}{t\_{i}-t\_{i-1}}\right|. |  |

By compiling the above penalty terms as the total loss, we have:

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | ℒ=ℒerror+γ1​ℒsmooth+γ2​ℒtrend,\mathcal{L}=\mathcal{L}\_{\text{error}}+\gamma\_{1}\mathcal{L}\_{\text{smooth}}+\gamma\_{2}\mathcal{L}\_{\text{trend}}, |  |

where γ1\gamma\_{1} and γ2\gamma\_{2} are hyperparameters indicating the weight of each penalty term in the overall loss. To train the network, we feed the cashflow dates of each bond to the network and first obtain the estimated spot yield rates. The corresponding discount factors are then computed using ([2](https://arxiv.org/html/2510.21347v1#S2.E2 "Equation 2 ‣ 2. Preliminaries and related works ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")). Then, the loss ℒ\mathcal{L} is calculated, and we update the network’s parameters using backpropagation.
This process is iterated for all bonds in the training set, which is denoted as one epoch. We run this process for a certain number of epochs, which will be tuned as a hyperparameter.

## 4. Experiments

### 4.1. Data & models

In this study, we used mortgage bonds on the Swedish market. Each bond is represented by its market price, cashflow dates, cashflow amounts, and its maturity. Data are collected by the SEB Group’s market risk team and consist of ∼\sim60 bonds per day with a wide spread of maturities between a few weeks and more than 1515 years. In practice, it is expected that the estimated Swedish mortgage yield curve follows the trends of the SEKOIS curve, with extreme points occurring relatively close; therefore, we used the SEKOIS curve as the risk-free benchmark in ([14](https://arxiv.org/html/2510.21347v1#S3.E14 "Equation 14 ‣ 3.1. Loss function ‣ 3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")). To argue the advantages of using our proposed NN-based model, we compare the estimations of the yield curve against the widely used parametric model NSS (Svensson, [1994](https://arxiv.org/html/2510.21347v1#bib.bib13)), and the recent non-parametric KR model (Filipovic et al., [2022](https://arxiv.org/html/2510.21347v1#bib.bib6)).

### 4.2. Hyperparameter selection

The neural network architecture used in our experiments consists of a single-layer network with three neurons and a tanh activation function as per equation ([11](https://arxiv.org/html/2510.21347v1#S3.E11 "Equation 11 ‣ 3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")), which we found to be sufficiently capable for the estimation task. To select the hyperparameters for our model, we examine the effect of varying the learning rate (L​RLR), number of training epochs, and the parameters γ1\gamma\_{1} and γ2\gamma\_{2}.

We investigate the accuracy by computing the root-mean-square error (RMSE) between the bonds’ YTM and the estimated yield at the corresponding maturities:

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | R​M​S​Eytm=1M​∑j=1M(y​(tj)−Y​T​Mj)2,RMSE\_{\text{ytm}}=\sqrt{\frac{1}{M}\textstyle\sum\_{j=1}^{M}{\left(y(t\_{j})-YTM\_{j}\right)^{2}}}, |  |

where tjt\_{j} is the time to maturity of the jj-th bond.

Table 1. RMSEytm{}\_{\text{ytm}} in a falling market, γ1=103\gamma\_{1}=10^{3}, γ2=104\gamma\_{2}=10^{4}

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​R=10−7LR=10^{-7} | L​R=10−8LR=10^{-8} | L​R=10−9LR=10^{-9} |
| epochs=200200 | 0.2110 | 0.1972 | 4.2559 |
| epochs=500500 | 0.2033 | 0.1790 | 3.6105 |
| epochs=10001000 | 0.2929 | 0.1726 | 2.5843 |




Table 2. RMSEytm{}\_{\text{ytm}} in a falling market, L​R=10−8LR=10^{-8}, epochs=103=10^{3}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ2=0\gamma\_{2}=0 | γ2=102\gamma\_{2}=10^{2} | γ2=104\gamma\_{2}=10^{4} | γ2=105\gamma\_{2}=10^{5} |
| γ1=0\gamma\_{1}=0 | 1.9426 | 1.8472 | 0.1486 | 0.2982 |
| γ1=103\gamma\_{1}=10^{3} | 1.3825 | 1.2787 | 0.1726 | 0.2982 |
| γ1=105\gamma\_{1}=10^{5} | 0.2325 | 0.2319 | 0.2306 | 0.1942 |

Figure [1](https://arxiv.org/html/2510.21347v1#S3.F1 "Figure 1 ‣ 3.1. Loss function ‣ 3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks") illustrates the results in a falling market scenario in which we estimate the yield curve using different choices of the hyperparameters. Note that the individual bonds are plotted in each figure in terms of their YTM, which differs from the spot yield shown on the Y-axis. Therefore, the best-fitting curve that passes through all individual bonds’ YTMs does not necessarily lead to the best price accuracy. The associated RMSEytm{}\_{\text{ytm}} values are reported in Tables [1](https://arxiv.org/html/2510.21347v1#S4.T1 "Table 1 ‣ 4.2. Hyperparameter selection ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks") and [2](https://arxiv.org/html/2510.21347v1#S4.T2 "Table 2 ‣ 4.2. Hyperparameter selection ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"). Although increasing γ1\gamma\_{1} leads to a smoother estimated curve (See Figure [1](https://arxiv.org/html/2510.21347v1#S3.F1 "Figure 1 ‣ 3.1. Loss function ‣ 3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")-right), it does not necessarily reduce the RMSE, as evident from Table [2](https://arxiv.org/html/2510.21347v1#S4.T2 "Table 2 ‣ 4.2. Hyperparameter selection ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"). A larger γ2\gamma\_{2} encourages the estimated curve to follow the SEKOIS benchmark more closely, often resulting in a more realistic shape. However, this may cause the model to deviate from market-observed prices, thereby increasing the RMSEytm{}\_{\text{ytm}}.

![Refer to caption](Pics/ALL_robustness_single_merged.png)


Figure 2. Robustness test for NSS, KR, and NN when perturbing the price of a bond with maturity 12.3Y by 3, 5, and 10% increase.

The influence of L​RLR and the number of training epochs is summarized in Table [1](https://arxiv.org/html/2510.21347v1#S4.T1 "Table 1 ‣ 4.2. Hyperparameter selection ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"). The results suggest that at least 500 epochs are required for convergence, and a learning rate of L​R=10−8LR=10^{-8} consistently yields the low RMSEytm{}\_{\text{ytm}} across scenarios. This is further supported by the behavior of the estimated curve with L​R=10−8LR=10^{-8} and 1000 epochs in Figure [1](https://arxiv.org/html/2510.21347v1#S3.F1 "Figure 1 ‣ 3.1. Loss function ‣ 3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"), where the curve remains above SEKOIS and exhibits stable behavior in both the short- and long-term segments. We ultimately select L​R=10−8LR=10^{-8}, 1000 epochs, γ1=103\gamma\_{1}=10^{3}, and γ2=104\gamma\_{2}=10^{4} for the remainder of the experiment in this paper, unless otherwise specified. Although γ1=0\gamma\_{1}=0 results in a lower RMSEytm{}\_{\text{ytm}} as observed in Table [2](https://arxiv.org/html/2510.21347v1#S4.T2 "Table 2 ‣ 4.2. Hyperparameter selection ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"), we strike a balance between low RMSEytm{}\_{\text{ytm}} and desirable curve characteristics in our experiments.

### 4.3. Robustness to outliers

In this section, we compare different methods and evaluate the robustness of their estimated yield curves to the existence of outliers in the dataset. We first perturb the training data, either by changing the bond prices or removing bonds entirely, and then measure the sensitivity of each method using RMSE and maximum absolute difference (MAD) between the original unperturbed yield curve y​(t)y(t) and a reference yield curve y~​(t)\tilde{y}(t) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | R​M​S​Ecurve=1N​∑i=1N(y​(ti)−y~​(ti))2,RMSE\_{\text{curve}}=\sqrt{\frac{1}{N}\textstyle\sum\_{i=1}^{N}{(y(t\_{i})-\tilde{y}(t\_{i}))^{2}}}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | M​A​D=maxt⁡|y​(t)−y~​(t)|,MAD=\max\_{t}|y(t)-\tilde{y}(t)|, |  |

where y~​(t)\tilde{y}(t) is the perturbed yield curve. The maturity grid points tit\_{i} that we use to compute RMSEcurve{}\_{\text{curve}} are: 1D, 1W, 2W, 1M, 2M, 3M, 6M, 9M, 12M, 15M, 18M, 21M, 2Y, 3Y, 4Y, 5Y, 6Y, 7Y, 8Y, 9Y, 10Y, 12Y, 15Y, 20Y, 25Y, 30Y.

First, we visually compare the extent to which the yield curve is affected by different methods when the price of a single bond (with a maturity of approximately 12 years) increases by 3%, 5%, or 10% on a given day. These scenarios test how well the models handle the presence of outliers, for example, when a callable bond is included in the dataset. For each case, we report perturbation RMSEcurve{}\_{\text{curve}} and MAD in bps (basis points) for the case of 10% perturbation and compare our NN with existing methods. The results are shown in Figure [2](https://arxiv.org/html/2510.21347v1#S4.F2 "Figure 2 ‣ 4.2. Hyperparameter selection ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"). The NSS model performs poorly even under small perturbations, particularly at long maturities. Although it can be argued that there are fewer bonds at longer maturities, both the KR and our NN model manage to handle the long tail of the curve more effectively. In the comparison between the KR and NN models, it is evident that our model is superior in handling perturbations across different maturities, indicating that it is more robust when dealing with outliers and noise in the market.

Next, we compare the sensitivity of each method when removing one or more samples from the data. We randomly drop 1, 5, and 10 bonds from the data for a given day and compare RMSEcurve{}\_{\text{curve}} and MAD for each case, averaged over 10 Monte Carlo (MC) simulations. The results are shown in Figure [3](https://arxiv.org/html/2510.21347v1#S4.F3 "Figure 3 ‣ 4.3. Robustness to outliers ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"), where we compare our NN model with KR and NSS (using the same random seed). The NSS model is highly sensitive to the removal of bonds from the estimation. Although the KR model is more robust than the NSS, perturbations in the curve at medium maturities affect the smoothness of the curve and are larger than those in our model, making the NN model more appealing in practice.

![Refer to caption](Pics/ALL_robustness_removal_10_merged_3x3.png)


Figure 3. Robustness test for NSS, KR, and NN when randomly dropping 1, 5, and 10 bonds from the dataset for 10 MC simulations. The solid line is the yield curve estimated using all bonds. The dashed lines show the curves after randomly dropping bonds.

### 4.4. Stability across days

In this section, we demonstrate that NN estimations are less sensitive to changes in bond prices over time. Flexible models, such as high-degree splines, may chase idiosyncratic price movements rather than accurately reflecting accurate rate expectations. Bid-ask spreads in thin markets such as mortgage bonds introduce noise that standard models might misinterpret as rate changes. As a measure of the stability of the curve, over a span of 1 year in history, we calculate:

1. (1)

   RMSEcurve{}\_{\text{curve}} where y~​(t)\tilde{y}(t) is the yield curve of previous day.
2. (2)

   Hit Rate as the percentage of days where RMSEcurve{}\_{\text{curve}}<10<10 bps. A hit rate of >90%>90\% is considered stable for liquid tenors.
3. (3)

   Daily yield rate estimation for maturities 6M, 2Y, and 10Y and comparing with SEKOIS rates.

Figure [4](https://arxiv.org/html/2510.21347v1#S4.F4 "Figure 4 ‣ 4.4. Stability across days ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks") shows the comparison between our NN model with KR and NSS in terms of the difference between today’s curve and the previous day. We use different maturity buckets to illustrate the RMSEcurve{}\_{\text{curve}} in different regimes. For a stable model, it is undesirable to observe large spikes in the calculated RMSEcurve{}\_{\text{curve}}. It is evident that the NN model exhibits smaller spikes and consistently higher hit rates compared to NSS across different maturity buckets, and it outperforms the KR model in hit rate in most experiments.

The comparisons in Figure [5](https://arxiv.org/html/2510.21347v1#S4.F5 "Figure 5 ‣ 4.4. Stability across days ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks") reveal that our model behaves more rationally compared to the risk-free rates for all three maturity examples. For shorter maturity (6M), the corresponding estimated rates using the KR and NSS models fall below the SEKOIS rate on many days, which is not justifiable. For 2Y and 10Y maturities, the models perform similarly, with the NSS model showing occasional spikes, which can be due to the high sensitivity of this model.

![Refer to caption](Pics/ALL_stability_adjacentDays_RMSE_merged_LB.png)


Figure 4. RMSEcurve{}\_{\text{curve}} w.r.t to the previous day along with Hit Rate of RMSE ¡ 10 bps over a period of 1 year.




Table 3. RMSEytm{}\_{\text{ytm}} comparison across maturity buckets and market scenarios.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Flat (3/6/2020) | | | | Rising (1/6/2022) | | | | Falling (3/6/2024) | | | |
| Full | <<2Y | 2Y–10Y | >>10Y | Full | <<2Y | 2Y–10Y | >>10Y | Full | <<2Y | 2Y–10Y | >>10Y |
| NSS | 0.2060 | 0.4163 | 0.0152 | 0.0525 | 0.1332 | 0.2254 | 0.0627 | 0.1585 | 0.1204 | 0.1488 | 0.0992 | 0.1846 |
| KR | 0.0180 | 0.0151 | 0.0125 | 0.0426 | 0.0774 | 0.0572 | 0.0629 | 0.1542 | 0.1296 | 0.1427 | 0.1053 | 0.2390 |
| NN | 0.1564 | 0.2494 | 0.1142 | 0.0871 | 0.2504 | 0.4519 | 0.1273 | 0.1451 | 0.1779 | 0.1058 | 0.1969 | 0.1589 |
| NN (γ1=0\gamma\_{1}=0) | 0.0882 | 0.1260 | 0.0692 | 0.0903 | 0.1431 | 0.2527 | 0.0646 | 0.1402 | 0.1512 | 0.1507 | 0.1519 | 0.1469 |

![Refer to caption](Pics/ALL_stability_tenor_estimate_merged.png)


Figure 5. Stability test when estimating the yield of a specific maturity, namely, 6-month, 2-year, and 10-year, compare to the benchmark SEKOIS rate over a period of 1 year.

### 4.5. Smoothness vs flexibility trade-off

In this section, the two objectives of ”accuracy” and ”economical reasonableness” in Section [3](https://arxiv.org/html/2510.21347v1#S3 "3. Neural network estimation ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks") are revisited in more extensive scenarios.
We consider three different days in history with noticeably different shapes of the SEKOIS curve (market scenarios). To experiment with the out-of-sample performance, we exclude one bond in the training and compute the yield error and price error using the excluded sample. Then leave-one-out (LOO) yield RMSEytm{}\_{\text{ytm}} is calculated on average over 10 Monte Carlo simulations as a measure of pricing accuracy, while the behavior of our estimated curve is compared against the SEKOIS curve and an in-house calibrated curve (at SEB Group) for three different days and compared against existing methods such as KR and NSS (see Figure [6](https://arxiv.org/html/2510.21347v1#S4.F6 "Figure 6 ‣ 4.5. Smoothness vs flexibility trade-off ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks")).
In the example of the rising market (2020-06-03), the KR and NN models have a justified spread relative to the SEKOIS curve and SEB-calibrated curves, while the NSS model performs poorly at short maturities. In the flat market example (2022-06-01), the NN model has the advantage of estimating a smoother curve than the KR model, and more justified rates at the long tail. Finally, in the falling market example (2024-06-03), the NN model shows better estimations compared to KR and NSS, as the KR model falls below the SEKOIS curve at short maturities and the NSS model exhibits unjustifiably increasing rates at the long end. Having a smooth behavior and justified with respect to SEKOIS comes at the price of losing accuracy as indicated in Table [3](https://arxiv.org/html/2510.21347v1#S4.T3 "Table 3 ‣ 4.4. Stability across days ‣ 4. Experiments ‣ Robust Yield Curve Estimation for Mortgage Bonds Using Neural Networks"). When we regularize the loss function less in the NN model (γ1=0\gamma\_{1}=0), the RMSEytm{}\_{\text{ytm}} drops and falls in the same range as other estimators.

![Refer to caption](Pics/smoothness-comparison-shortMaturity_merged.png)


Figure 6. Comparing an example of LOO estimated yield curve for three different days representing a flat, rising, and falling market condition. Dropped bond is chosen from the bucket of ¡2Y maturities.

## 5. Conclusion

We demonstrated that utilizing neural networks for yield curve estimation can provide a more robust and stable estimate, particularly in smaller and relatively less liquid markets, such as the Swedish mortgage bond market. We compared our results against NSS and KR in various market conditions and achieved a smoother curve in all scenarios. This, however, is achieved at the cost of sacrificing the accuracy of the curve in terms of yield RMSE on LOO samples. In this way, NNs provide a framework that allows analysts to tune the model to their specific needs and balance the trade-off between accuracy and economic reasonableness as they see fit. Optimization of the NN architecture is a potential future direction for improving the RMSE of our model. Incorporating temporal data to enable yield curve forecasting using neural networks is another promising area for future research.

## References

* (1)
* Bahaa Aly and El-Masry (2025)

  Tarek Bahaa Aly and
  Ahmed A El-Masry. 2025.
  Yield Curves Prediction Using Artificial Neural
  Network Regression Multitask Learning.
  *Available at SSRN.* (2025).

  <https://ssrn.com/abstract=5200759>
* Bolder and Stréliski (1999)

  David Jamieson Bolder and
  David Stréliski. 1999.
  Yield curve modelling at the bank of canada.
  (1999).
* Diebold and Li (2006)

  Francis X Diebold and
  Canlin Li. 2006.
  Forecasting the term structure of government bond
  yields.
  *Journal of econometrics*
  130, 2 (2006),
  337–364.
* Diebold et al. (2008)

  Francis X Diebold, Canlin
  Li, and Vivian Z Yue. 2008.
  Global yield curve dynamics and interactions: a
  dynamic Nelson–Siegel approach.
  *Journal of Econometrics*
  146, 2 (2008),
  351–363.
* Filipovic et al. (2022)

  Damir Filipovic, Markus
  Pelger, and Ye Ye. 2022.
  Stripping the Discount Curve — a Robust Machine
  Learning Approach.
  *Swiss Finance Institute Research Paper No.
  22-24, Forthcoming, Management Science* (2022).
* Hornik et al. (1989)

  Kurt Hornik, Maxwell B.
  Stinchcombe, and Halbert L. White.
  1989.
  Multilayer feedforward networks are universal
  approximators.
  *Neural Networks* 2
  (1989), 359–366.

  <https://api.semanticscholar.org/CorpusID:2757547>
* Kauffmann et al. (2022)

  Piero C Kauffmann,
  Hellinton H Takada, Ana T Terada, and
  Julio M Stern. 2022.
  Learning forecast-efficient yield curve factor
  decompositions with neural networks.
  *Econometrics* 10,
  2 (2022), 15.
* McCulloch (1971)

  J. Huston McCulloch.
  1971.
  Measuring the Term Structure of Interest Rates.
  *The Journal of Business*
  44, 1 (1971),
  19–31.

  <http://www.jstor.org/stable/2351832>
* McCulloch (1975)

  J Huston McCulloch.
  1975.
  The tax-adjusted yield curve.
  *The Journal of Finance*
  30, 3 (1975),
  811–830.
* Nelson and Siegel (1987)

  Charles R. Nelson and
  Andrew F. Siegel. 1987.
  Parsimonious Modeling of Yield Curves.
  *The Journal of Business*
  60, 4 (1987),
  473–489.
* Nymand-Andersen (2018)

  Per Nymand-Andersen.
  2018.
  *Yield curve modelling and a conceptual
  framework for estimating yield curves: evidence from the European Central
  Bank’s yield curves*.
  Number 27. ECB Statistics Paper.
* Svensson (1994)

  Lars EO Svensson.
  1994.
  Estimating and interpreting forward interest rates:
  Sweden 1992-1994.