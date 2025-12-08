---
authors:
- Paul Glasserman
- Siddharth Hemant Karmarkar
doc_id: arxiv:2512.05301v1
family_id: arxiv:2512.05301
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Differential ML with a Difference
url_abs: http://arxiv.org/abs/2512.05301v1
url_html: https://arxiv.org/html/2512.05301v1
venue: arXiv q-fin
version: 1
year: 2025
---


Paul Glasserman
Siddharth Hemant Karmarkar

Columbia University
Columbia University

pg20@columbia.edu
shk2195@columbia.edu

(November 2025)

###### Abstract

Differential ML (Huge and Savine 2020) is a technique for training neural networks to provide fast approximations to complex simulation-based models for derivatives pricing and risk management. It uses price sensitivities calculated through pathwise adjoint differentiation to reduce pricing and hedging errors. However, for options with discontinuous payoffs, such as digital or barrier options, the pathwise sensitivities are biased, and incorporating them into the loss function can magnify errors. We consider alternative methods for estimating sensitivities and find that they can substantially reduce test errors in prices and in their sensitivities. Using differential labels calculated through the likelihood ratio method expands the scope of Differential ML to discontinuous payoffs. A hybrid method incorporates gamma estimates as well as delta estimates, providing further regularization.

## 1. Introduction

Machine learning methods can provide fast approximations to complex derivatives pricing and risk management models. They can be trained based on historical or simulated data. In either case, the standard approach trains a model using a set of spot prices for the underlying assets (and any other market inputs) and the discounted payouts resulting from these initial values under one or more derivatives contracts. These payouts depend on the historical or simulated evolution of the market. In the language of machine learning, the
total payouts are labels; the goal of the machine learning approach is to
develop a fast approximation to the mapping from market inputs to the corresponding
labels. (For general background on machine learning in finance, see Dixon et al. [[3](https://arxiv.org/html/2512.05301v1#bib.bib3)]; for an application to approximating volatilities rather than prices, see Horvath et al. [[4](https://arxiv.org/html/2512.05301v1#bib.bib4)].)

Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] extended this general approach by expanding
the set of labels used for training to include payout *sensitivities* as
well as the payouts themselves. Related ideas have been used in the physics literature (Raissi et al. [[9](https://arxiv.org/html/2512.05301v1#bib.bib9)]), but the financial setting has distinctive features.
Targeting sensitivities in training an approximation addresses two points. First, it should improve the model training process by providing addititional labels to target.
Second, it should improve the sensitivities (Greeks) calculated from the
machine learning approximation, and these risk measures are of paramount
importance in the financial setting. As Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] put it,
“the derivatives of a good approximation are not always a good approximation
of the derivatives.” Their differential machine learning method (DML) seeks to
overcome this limitation.

For their differential labels (the payout sensitivities used in training), Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] use *pathwise* derivatives. Numerical results confirm that, when
applicable, targeting these differential labels reduces pricing errors and yields more accurate delta approximations than standard ML using only payout labels. However, the pathwise method yields biased estimates for derivative contracts with digital or barrier features. (See, e.g., the discussion in Section 7.2.2 of Glasserman [[6](https://arxiv.org/html/2512.05301v1#bib.bib6)].) Targeting biased differential labels can severely magnify errors and undermine the objective of DML.

To address this issue, we expand the set of differential labels for DML beyond pathwise sensitivities through the *likelihood ratio method* (LRM) and a
hybrid method. LRM is applicable even with discontinuous payouts, such as those
resulting from digital or barrier features. Our hybrid method allows extending DML to include second-order (gamma) sensitivities. We validate these ideas through numerical examples.

Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] note in passing that the pathwise method may require “appropriate smoothing.” Smoothing introduces its own bias, and may be complicated to implement with path-dependent discontinuities. We will revisit smoothing in Section [3.3](https://arxiv.org/html/2512.05301v1#S3.SS3 "3.3 Smoothing ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference"). But the main objective of this article is to show that the scope of DML can be expanded through LRM-based differential labels, complementing the use of pathwise estimates, with or without smoothing.

Section [2](https://arxiv.org/html/2512.05301v1#S2 "2. Differential Machine Learning ‣ Differential ML with a Difference") provides background on standard and differential machine learning.
Section [3](https://arxiv.org/html/2512.05301v1#S3 "3. Dealing with Discontinuities ‣ Differential ML with a Difference") illustrates the problem of discontinuous payouts, explains the use of LRM, and tests its performance on examples. Section [4](https://arxiv.org/html/2512.05301v1#S4 "4. Gamma ‣ Differential ML with a Difference") extends the approach to include gamma-regularization.
Our implementation is available at
https://github.com/diff-ml-with-a-difference/options-pricing.

## 2. Differential Machine Learning

### 2.1 Problem Setup and Standard Learning

We generally follow the setting and notation of Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)].
We consider a model specified through a Monte Carlo simulation algorithm, represented by a function hh.
The algorithm takes as input xx, a vector of spot prices (and possibly other market variables),
it applies stochastic inputs ξ\xi, and returns the discounted payout
h​(x,ξ)h(x,\xi). This payout could apply to a portfolio of path-dependent options on multiple underlying assets, priced through a complex model with stochastic volatility and other features captured through the stochastic inputs ξ\xi and the function hh.
The function hh embodies the simulation algorithm and is typically defined only implicitly through a combination of a large number of simpler operations.

The pricing function for this model is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=𝔼​[h​(x,ξ)],f(x)=\mathbb{E}[h(x,\xi)], |  | (1) |

the expectation taken over the stochastic inputs ξ\xi. In principle, the
pricing function can be approximated by averaging over repeated Monte Carlo samples, but this may be prohibitively time-consuming for real-time use.
In such settings, developing a faster approximation that can be trained off-line
becomes attractive.

The standard training data consists of a set of pairs (x(i),y(i))(x^{(i)},y^{(i)}), i=1,…,mi=1,\dots,m, where the x(i)x^{(i)} are spot-price vectors, and the labels y(i)y^{(i)}
are the corresponding payouts y(i)=h​(x(i),ξ(i))y^{(i)}=h(x^{(i)},\xi^{(i)}). The labels
are generated by running the Monte Carlo simulation from x(i)x^{(i)} with
stochastic inputs ξ(i)\xi^{(i)}, which can be done off-line.

A conventional neural network defines a family of functions f^​(x;w)\hat{f}(x;w)
with parameters ww. These parameters are the weights used in the
neural network. They are chosen to approximate
the true pricing function ff by minimizing the empirical mean-squared error (MSE),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒval​(w)=1m​∑i=1m(f^​(x(i);w)−y(i))2,\mathcal{L}\_{\text{val}}(w)=\frac{1}{m}\sum\_{i=1}^{m}\big(\hat{f}(x^{(i)};w)-y^{(i)}\big)^{2}, |  | (2) |

possibly with a regularization penalty.
Once trained, the approximation f^​(x;w)\hat{f}(x;w) can be used for fast
evaluation at new spot prices xx. However, even if
the error in ([2](https://arxiv.org/html/2512.05301v1#S2.E2 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) is small, there is no guarantee that
sensitivities calculated from f^\hat{f} will be close to the sensitivities
for the true pricing function ff.

To help fix ideas, consider the simple example of Black-Scholes option pricing.
The terminal value of the underlying asset is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ST=x​e(r−σ2)​T+σ​T​ξ,S\_{T}=xe^{(r-\sigma^{2})T+\sigma\sqrt{T}\xi}, |  | (3) |

with spot price xx, and ξ\xi having a standard normal distribution.
The discounted payoff of a standard call option is h​(x,ξ)=e−r​T​(ST−K)+h(x,\xi)=e^{-rT}(S\_{T}-K)^{+}.
The training data in this case would take the form (x(i),y(i))(x^{(i)},y^{(i)}),
for some spot prices x(i)x^{(i)} and corresponding payoffs y(i)=h​(x(i),ξ(i))y^{(i)}=h(x^{(i)},\xi^{(i)}). With enough training data and a sufficiently rich network,
the minimizing f^\hat{f} in ([2](https://arxiv.org/html/2512.05301v1#S2.E2 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) will approximate the Black-Scholes
formula, though the formula itself is never used in the training process.
In practice, such an approach is used with models that do not admit closed-form
prices.

In our implementation, we generate kk payoffs y(i,1),…,y(i,k)y^{(i,1)},\dots,y^{(i,k)} from each
input x(i)x^{(i)} and take the label y(i)y^{(i)} to be the average

|  |  |  |  |
| --- | --- | --- | --- |
|  | y(i)=1k​∑j=1ky(i,j).y^{(i)}=\frac{1}{k}\sum\_{j=1}^{k}y^{(i,j)}. |  | (4) |

This reduces the variability in the labels, but it also reduces the number of samples mm we
can process in a fixed amount of computing time. Our numerical results use k=10k=10.

### 2.2 Training Sensitivities with Prices

In DML, each sample (x(i),y(i))(x^{(i)},y^{(i)}) is augmented with a differential label
δ(i)=∇xy(i)\delta^{(i)}=\nabla\_{x}y^{(i)}.
The training objective becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒDML​(w)=1m​∑i=1m(f^​(x(i);w)−y(i))2+λ⋅1m​∑i=1m‖∇xf^​(x(i);w)−δ(i)‖2,\mathcal{L}\_{\text{DML}}(w)=\frac{1}{m}\sum\_{i=1}^{m}\big(\hat{f}(x^{(i)};w)-y^{(i)}\big)^{2}+\lambda\cdot\frac{1}{m}\sum\_{i=1}^{m}\big\|\nabla\_{x}\hat{f}(x^{(i)};w)-\delta^{(i)}\big\|^{2}, |  | (5) |

where λ\lambda balances the value and gradient terms.

The new terms in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) require careful explanation. We will discuss
∇xf^​(x(i);w)\nabla\_{x}\hat{f}(x^{(i)};w) first, and then turn to δ(i)\delta^{(i)}.

Related ideas have been developed in the physics literature under the name of “physics-informed neural networks” (Raissi et al. [[9](https://arxiv.org/html/2512.05301v1#bib.bib9)]). In that setting, physical principles impose a condition on the target function ff of the form D​(f)=0D(f)=0, for some differential operator DD. In place of the second term in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")),
the loss function penalizes deviations ‖D​(f^​(x(i);w))‖2\|D(\hat{f}(x^{(i)};w))\|^{2}.
Our focus is on the proper choice of differential labels δ(i)\delta^{(i)} in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) whereas in the physics-informed setting the corresponding labels are simply zero.

### 2.3 Differentiation through Backpropagation

The gradient ∇xf^​(x;w)\nabla\_{x}\hat{f}(x;w) in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) is the sensitivity of the approximating
function f^\hat{f} with respect to the spot prices xx. When f^\hat{f}
is defined through a feedforward neural network, this gradient
can be calculated very efficiently through backpropagation (see, e.g., Section 6.5 of Goodfellow et al. [[7](https://arxiv.org/html/2512.05301v1#bib.bib7)]), which is a
special case of automatic adjoint differentiation (AAD).

This step is illustrated nicely in Figure 1 of Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)].
Their mathematical specification goes as follows.
Consider a feedforward network with LL layers defined by the equations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | z0\displaystyle z\_{0} | =x,\displaystyle=x, |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | zl\displaystyle z\_{l} | =gl−1​(zl−1)​Wl+bl,l=1,…,L,\displaystyle=g\_{l-1}(z\_{l-1})W\_{l}+b\_{l},\quad l=1,\dots,L, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f^​(x;w)\displaystyle\hat{f}(x;w) | =zL.\displaystyle=z\_{L}. |  | (8) |

Here, ([6](https://arxiv.org/html/2512.05301v1#S2.E6 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) assigns the vector of inputs xx to the initial nodes; step ([7](https://arxiv.org/html/2512.05301v1#S2.E7 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) applies
the elementwise activiation functions gl−1g\_{l-1}, weight matrices WlW\_{l}, and biases blb\_{l} to calculate layer ll from layer l−1l-1; and ([8](https://arxiv.org/html/2512.05301v1#S2.E8 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) outputs that the final result.

Backpropagation differentiates f^​(x;w)\hat{f}(x;w) with respect to the inputs in the reverse direction by setting

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | z¯L\displaystyle\bar{z}\_{L} | =1,\displaystyle=1, |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | z¯l−1\displaystyle\bar{z}\_{l-1} | =(z¯l​Wl⊤)∘gl−1′​(zl−1),l=L,…,1,\displaystyle=(\bar{z}\_{l}W\_{l}^{\top})\circ g^{\prime}\_{l-1}(z\_{l-1}),\quad l=L,\dots,1, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇xf^​(x;w)\displaystyle\nabla\_{x}\hat{f}(x;w) | =z¯0,\displaystyle=\bar{z}\_{0}, |  | (11) |

where ∘\circ denotes elementwise multiplication, and z¯l\bar{z}\_{l} is the
derivative of the output f^​(x;w)\hat{f}(x;w) with respect to zlz\_{l}.
This backward recursion mirrors the forward propagation ([6](https://arxiv.org/html/2512.05301v1#S2.E6 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference"))–([8](https://arxiv.org/html/2512.05301v1#S2.E8 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")), producing sensitivities with a cost comparable to an additional forward pass, independent of input dimension.

By concatenating the forward and backward computations, Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] obtain a *twin network*: one half predicts the value f^​(x)\hat{f}(x), the other its derivatives ∇xf^​(x)\nabla\_{x}\hat{f}(x).
The two share the same parameters and structure, and the composite graph supports joint optimization using the loss in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")).

### 2.4 Differential Labels

Backpropagation computes the gradients ∇xf^​(x;w)\nabla\_{x}\hat{f}(x;w) in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")). It remains to consider the differential labels δ(i)\delta^{(i)}
in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")).

Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] use pathwise differentiation to calculate the
labels

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ(i)=∇xh​(x(i),ξ(i)),\delta^{(i)}=\nabla\_{x}h(x^{(i)},\xi^{(i)}), |  | (12) |

where, as before, hh is the function implicitly defined by the steps of a Monte Carlo algorithm. Equation ([12](https://arxiv.org/html/2512.05301v1#S2.E12 "In 2.4 Differential Labels ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) is called a pathwise derivative because it
is the derivative with the path of stochastic inputs ξ\xi held fixed.

In the Black-Scholes example ([3](https://arxiv.org/html/2512.05301v1#S2.E3 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ=e−r​T​∂x(ST−K)+=𝟙​{ST>K}​e−r​T​STx,\delta=e^{-rT}\partial\_{x}(S\_{T}-K)^{+}=\mathds{1}\{S\_{T}>K\}\frac{e^{-rT}S\_{T}}{x}, |  | (13) |

where we used ∂xST=ST/x\partial\_{x}S\_{T}=S\_{T}/x from ([3](https://arxiv.org/html/2512.05301v1#S2.E3 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")).
The payoff fails to be differentiable at ST=KS\_{T}=K, but this outcome has probability zero, so the pathwise derivative is well-defined. It will often happen that the simulation
algorithm hh fails to be differentiable at certain points, but as long as these points have probability zero, the pathwise derivative is well-defined.

As in prior work, Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] find that the calculation of pathwise sensitivities can be greatly accelerated through AAD. However, it is important to emphasize that there are two entirely separate applications of AAD in Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)]: one computes ∇xf^​(x;w)\nabla\_{x}\hat{f}(x;w) through backpropagation in the neural network; the other computes pathwise derivatives in generating training data as input to the neural network. One can adopt the first application without the second — pathwise derivatives (whether or not calculated through AAD) are not the only source of differential labels. We will argue that for discontinuous payoffs we need different labels.

## 3. Dealing with Discontinuities

To understand what we want from the differential lables δ(i)\delta^{(i)}, it
is helpful to revisit the standard labels y(i)y^{(i)} and the standard loss function ([2](https://arxiv.org/html/2512.05301v1#S2.E2 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")). By the definition of the pricing function ff, the payout labels have the property f​(x(i))=𝔼​[h​(x(i),ξ(i))]=𝔼​[y(i)]f(x^{(i)})=\mathbb{E}[h(x^{(i)},\xi^{(i)})]=\mathbb{E}[y^{(i)}];
the discounted payouts are unbiased estimates of the price. This property
ensures that minimizing ([2](https://arxiv.org/html/2512.05301v1#S2.E2 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) drives the approximation f^\hat{f} close to the true pricing function ff.

In ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")), we similarly want to drive ∇xf^\nabla\_{x}\hat{f} close
to ∇xf\nabla\_{x}f. To this end, we want

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇xf​(x(i))=𝔼​[δ(i)];\nabla\_{x}f(x^{(i)})=\mathbb{E}[\delta^{(i)}]; |  | (14) |

in other words, *we want the differential label to be an unbiased estimate of the true sensitivity*. In the case of pathwise derivatives, ([14](https://arxiv.org/html/2512.05301v1#S3.E14 "In 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) requires

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇x𝔼​[h​(x,ξ)]=𝔼​[∇xh​(x,ξ)].\nabla\_{x}\mathbb{E}[h(x,\xi)]=\mathbb{E}[\nabla\_{x}h(x,\xi)]. |  | (15) |

When this condition fails, targeting a biased differential label in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference"))
steers ∇xf^\nabla\_{x}\hat{f} away from the true value ∇xf\nabla\_{x}f, undermining the objective of DML.

Conditions for ([15](https://arxiv.org/html/2512.05301v1#S3.E15 "In 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) have been widely studied; see the discussion in Section 7.2.2 of Glasserman [[6](https://arxiv.org/html/2512.05301v1#bib.bib6)]. A sufficient condition is that hh be Lipschitz in xx. A simple rule of thumb in practice is that ([15](https://arxiv.org/html/2512.05301v1#S3.E15 "In 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) typically holds when hh is continuous in xx and fails otherwise.

### 3.1 Digital Options

Digital options provide a stark example of this phenomenon.
In the Black-Scholes model ([3](https://arxiv.org/html/2512.05301v1#S2.E3 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")), consider the payoff function

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x,ξ)=e−r​T​𝟙{ST>K}.h(x,\xi)=e^{-rT}\mathds{1}\_{\{S\_{T}>K\}}. |  | (16) |

The event ST=KS\_{T}=K has probability zero, so the pathwise derivative of hh is well-defined. However, the payoff is piecewise constant, so the pathwise derivative is identically equal to zero, resulting in δ(i)≡0\delta^{(i)}\equiv 0,
even though the expected payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=e−r​T​Φ​(log⁡(x/K)+r​Tσ​T−σ​T2)f(x)=e^{-rT}\Phi\left(\frac{\log(x/K)+rT}{\sigma\sqrt{T}}-\frac{\sigma\sqrt{T}}{2}\right) |  | (17) |

is strictly increasing in xx, where Φ\Phi is the standard normal cumulative
distribution function.

We illustrate the consequences of these biased labels through a numerical example, taking r=0r=0, T=1/3T=1/3, and σ=0.20\sigma=0.20.
We give equal weight to the price and delta components of the loss function ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")).
All of our numerical results are based on the code provided by Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)], with relatively minor changes.
111As in Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)], each network has four hidden layers of twenty units each and uses softplus activations. All models are optimized with Adam and a cosine-decay learning rate
schedule between 10−310^{-3} and 10−610^{-6}, using batch sizes of 256–512 for stability.

The left panel of Figure [1](https://arxiv.org/html/2512.05301v1#S3.F1 "Figure 1 ‣ 3.1 Digital Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference") shows results using standard ML based on the loss function ([2](https://arxiv.org/html/2512.05301v1#S2.E2 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) without differential labels. We generate training data by generating m=512m=512 values for the underlying asset and generating k=10k=10 terminal values STS\_{T} from each of these, as in ([4](https://arxiv.org/html/2512.05301v1#S2.E4 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")). After training, we test the approximation by evaluating it at levels of the underlying ranging from 40 to 160. We compare the approximation with the Black-Scholes digital prices and calculate the root mean squared error (RMSE) across these differences.

In the left panel of the figure, the predicted values (from the neural network) are close to the correct values from ([17](https://arxiv.org/html/2512.05301v1#S3.E17 "In 3.1 Digital Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")). In the center panel, we repeat the same procedure but now using the DML objective ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) with the pathwise differential labels, which are identically zero for the digital payoff. The result is a significant failure. The predicted prices are far too high at low spot prices and far too low at high spot prices.
The RMSE, which was 3.86 using standard ML, is now 19.71. As expected, targeting biased estimates of sensitivities steers the approximation far from the true target.
Because the pathwise derivativies are identically zero, by targeting these we produce
an approximation that is too flat.

To address this problem, we apply the likelihood ratio method (LRM), which replaces pathwise derivatives with log-likelihood sensitivities.
Whereas the pathwise method treats the input xx as an argument of the function hh, LRM treats it as a parameter of the distribution of the underlying asset.
(For general background on LRM, see Chapter VII of Asmussen and Glynn [[1](https://arxiv.org/html/2512.05301v1#bib.bib1)] or Section 7.3 of Glasserman [[6](https://arxiv.org/html/2512.05301v1#bib.bib6)].)

Consider, for example, the Black-Scholes setting ([3](https://arxiv.org/html/2512.05301v1#S2.E3 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) with spot price S0=xS\_{0}=x.
For any discounted payoff π​(ST)\pi(S\_{T}), we have

|  |  |  |
| --- | --- | --- |
|  | f​(x)=𝔼​[π​(ST)]=∫0∞π​(s)​p​(s;x)​𝑑s,f(x)=\mathbb{E}[\pi(S\_{T})]=\int\_{0}^{\infty}\pi(s)p(s;x)\,ds, |  |

where p​(s;x)p(s;x) is the lognormal density of STS\_{T} when S0=xS\_{0}=x,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(s;x)=1x​σ​T​φ​(log⁡(s/x)−r​Tσ​T+σ​T2),p(s;x)=\frac{1}{x\sigma\sqrt{T}}\varphi\left(\frac{\log(s/x)-rT}{\sigma\sqrt{T}}+\frac{\sigma\sqrt{T}}{2}\right), |  | (18) |

with φ\varphi the standard normal density.
LRM uses the identity

|  |  |  |
| --- | --- | --- |
|  | f′​(x)=∫0∞[π​(x)​∇xlog⁡p​(s;x)]​p​(x;s)​𝑑s=𝔼​[π​(ST)​∇xlog⁡p​(ST;x)],f^{\prime}(x)=\int\_{0}^{\infty}[\pi(x)\nabla\_{x}\log p(s;x)]p(x;s)\,ds=\mathbb{E}[\pi(S\_{T})\nabla\_{x}\log p(S\_{T};x)], |  |

to arrive at the unbiased estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(ST)​∇xlog⁡p​(ST;x).\pi(S\_{T})\nabla\_{x}\log p(S\_{T};x). |  | (19) |

In the case of ([18](https://arxiv.org/html/2512.05301v1#S3.E18 "In 3.1 Digital Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")), the *score function* ∇xlog⁡p​(ST;x)\nabla\_{x}\log p(S\_{T};x)
evaluates to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇xlog⁡p​(ST;x)=ξx​σ​T,\nabla\_{x}\log p(S\_{T};x)=\frac{\xi}{x\sigma\sqrt{T}}, |  | (20) |

with ξ\xi the same normal random variable used to generate the asset price STS\_{T}
in ([3](https://arxiv.org/html/2512.05301v1#S2.E3 "In 2.1 Problem Setup and Standard Learning ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")).
This approach holds for any payoff π​(⋅)\pi(\cdot).
In the case of a digital option, the unbiased LRM delta estimator reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ^LRM=e−r​T​ 1{ST>K}​ξx​σ​T.\widehat{\Delta}\_{\mathrm{LRM}}=e^{-rT}\,\mathds{1}\_{\{S\_{T}>K\}}\,\frac{\xi}{x\sigma\sqrt{T}}. |  | (21) |

We may therefore use as unbiased differential labels

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ(i)=e−r​T​ 1{ST(i)>K}​ξ(i)x(i)​σ​T,\delta^{(i)}=e^{-rT}\,\mathds{1}\_{\{S^{(i)}\_{T}>K\}}\,\frac{\xi^{(i)}}{x^{(i)}\sigma\sqrt{T}}, |  | (22) |

in place of pathwise derivatives, which are biased for digital options.

It is worth emphasizing that the only change required in differential ML to implement this alternative is to replace the pathwise labels δ(i)\delta^{(i)} (which are identically zero for a digital option) with the LRM labels ([22](https://arxiv.org/html/2512.05301v1#S3.E22 "In 3.1 Digital Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) in ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")). All other steps in the training and application process are unchanged. In particular, derivatives of the resulting approximation f^​(x;w)\hat{f}(x;w) can be evaluated through backpropagation exactly as before.

In the right panel of Figure [1](https://arxiv.org/html/2512.05301v1#S3.F1 "Figure 1 ‣ 3.1 Digital Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference") we see that the LRM differential labels
yield a near-perfect approximation, in contrast to the pathwise labels in the middle panel.
The LRM approximation has an RMSE of 1.01, which is nearly a 20-fold reduction compared to pathwise DML and nearly a 4-fold reduction compared to standard ML.
These correspond to MSE ratios of 400 and 16, respectively.
For a fixed method, MSE is generally inversely proportional to sample size, so the MSE ratios measure roughly how much more training data the other methods would need to match the accuracy of the LRM method.

![Refer to caption](x1.png)


Figure 1: Digital options — predicted vs. target prices under standard, pathwise differential, and LRM differential training, using a sample size of 512 training labels.

Figure [1](https://arxiv.org/html/2512.05301v1#S3.F1 "Figure 1 ‣ 3.1 Digital Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference") compares prices f^​(x;w)\hat{f}(x;w). As already noted, regardless of the method used to train the parameters ww, the approximation can be differentiated using ([9](https://arxiv.org/html/2512.05301v1#S2.E9 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference"))–([11](https://arxiv.org/html/2512.05301v1#S2.E11 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")). We therefore evaluate the error in ∂xf^​(x;w)\partial\_{x}\hat{f}(x;w)
as an approximation to ∂xf​(x)\partial\_{x}f(x). We call this the Delta RMSE to contrast it with the Price RMSE. The Delta RMSE using LRM is 34 times smaller than that for pathwise DML.

### 3.2 Basket Digitals

We turn next to a high-dimensional example. Following Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)], we consider a basket option in the Bachelier model. This setting provides a convenient test case because it allows us to compare neural network approximations against closed-form prices regardless of dimension (since the Gaussian property is preserved by linear combinations). Whereas Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] considered a standard basket call option, we consider a digital payouff.

For a basket with dd assets and weights wiw\_{i}, the payoff is

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(ST,1,…,ST,d)=e−r​T​𝟙{∑i=1dwi​ST,i>K}.\pi(S\_{T,1},\ldots,S\_{T,d})=e^{-rT}\mathds{1}\_{\left\{\sum\_{i=1}^{d}w\_{i}S\_{T,i}>K\right\}}. |  | (23) |

The underlying assets are uncorrelated and evolve according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ST,i=xi+σ​T​ξi,i=1,…,d,ξ∼𝒩​(0,I).S\_{T,i}=x\_{i}+\sigma\sqrt{T}\,\xi\_{i},\;i=1,\dots,d,\qquad\xi\sim\mathcal{N}(0,I). |  | (24) |

The discontinuity now occurs on a (d−1)(d-1)-dimensional hyperplane separating in- and out-of-the-money regions. This hyperplane has probability zero under the Gaussian distribution, so pathwise derivatives ∂π/∂ST,i\partial\pi/\partial S\_{T,i} are well-defined. However, they are identically zero.

The likelihood-ratio gradient estimator remains well-defined in this setting.
Differentiating the log-density with respect to the initial spot xix\_{i} gives the per-asset score

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇xilog⁡p​(ST;x)=ξiσi​T,\nabla\_{x\_{i}}\log p(S\_{T};x)=\frac{\xi\_{i}}{\sigma\_{i}\sqrt{T}}, |  | (25) |

leading to the componentwise LRM delta estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ^LRM(i)=e−r​T​ 1{∑jwj​ST,j>K}​ξiσi​T.\widehat{\Delta}\_{\text{LRM}}^{(i)}=e^{-rT}\,\mathds{1}\_{\{\sum\_{j}w\_{j}S\_{T,j}>K\}}\,\frac{\xi\_{i}}{\sigma\_{i}\sqrt{T}}. |  | (26) |

Following Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)], we estimate the average delta across assets and thus use the average of ([26](https://arxiv.org/html/2512.05301v1#S3.E26 "In 3.2 Basket Digitals ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) over i=1,…,di=1,\dots,d as the differential label. With an equally weighted 20-asset basket, LRM achieves a 7-fold reduction in Price RMSE and 6-fold reduction in Delta RMSE compared to pathwise DML.

### 3.3 Smoothing

Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)] note in passing that application of pathwise differentiation may require “appropriate smoothing.” Smoothing can be helpful in reducing bias, but it does not eliminate bias. Moreoever, the proper degree of smoothing in specific cases is far from obvious, and a suitable approach to smoothing may be unclear in multidimensional problems.

Consider again the simple setting of a digital payoff. The step function at the strike KK can be replaced with a ramp over the interval from K−ϵ/2K-\epsilon/2 to K+ϵ/2K+\epsilon/2. The pathwise method can be applied to this piecewise linear, continuous payoff.
But how should ϵ\epsilon be chosen? Taking ϵ\epsilon too large increases bias; taking it too small increases variance.

Figure [2](https://arxiv.org/html/2512.05301v1#S3.F2 "Figure 2 ‣ 3.3 Smoothing ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")
plots the price RMSE as a percentage of price for a digital option at various levels of ϵ\epsilon, shown as multiples of σ​T\sigma\sqrt{T}. The performance of DML with pathwise derivatives is very sensitive to the choice of ϵ\epsilon. At most values of ϵ\epsilon, it underperforms standard ML; at all values, it underperforms DML with LRM labels.

![Refer to caption](x2.png)


Figure 2: Performance of pathwise ML on a digital option with smoothing is sensitive to smoothing parameter ϵ\epsilon. Results are averaged over 30 replications, each using a training sample size of 1024.

The digital payoff is the simplest case of a discontinuous payoff, yet even here the effective use of smoothing is not obvious. Proper smoothing is even less obvious when discontinuities are path-dependent or dependent on multiple assets.
Moreover, Price RMSE and Delta RMSE may be minimized at different degrees of smoothing.

### 3.4 Barrier Options

Barrier options introduce a discontinuity that depends on the path of the underlying, rather than on the terminal value alone.
We consider a down-and-out call option where the barrier is monitored at an intermediate time T1T\_{1} and the option expires at T2T\_{2}.
The payoff is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(ST1,ST2)=e−r​T​𝟙{ST1>B}​(ST2−K)+,\pi(S\_{T\_{1}},S\_{T\_{2}})=e^{-rT}\mathds{1}\_{\{S\_{T\_{1}}>B\}}(S\_{T\_{2}}-K)^{+}, |  | (27) |

so that the contract is knocked out if the underlying is below the barrier BB
at T1T\_{1}.
In the Black-Scholes setting, the underlying is simulated using

|  |  |  |  |
| --- | --- | --- | --- |
|  | STn+1=STn​exp⁡((r−12​σ2)​(Tn+1−Tn)+σ​Tn+1−Tn​ξn+1),ξn+1∼𝒩​(0,1),S\_{T\_{n+1}}=S\_{T\_{n}}\exp\!\Big((r-\tfrac{1}{2}\sigma^{2})(T\_{n+1}-T\_{n})+\sigma\sqrt{T\_{n+1}-T\_{n}}\,\xi\_{n+1}\Big),\quad\xi\_{n+1}\sim\mathcal{N}(0,1), |  | (28) |

for n=0,1n=0,1, with T0=0T\_{0}=0 and S0=xS\_{0}=x.
The pathwise derivative of ([27](https://arxiv.org/html/2512.05301v1#S3.E27 "In 3.4 Barrier Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) is given by

|  |  |  |
| --- | --- | --- |
|  | ∂xπ​(ST1,ST2)=e−r​T​𝟙{ST1>B,ST2>K}​ST2/x.\partial\_{x}\pi(S\_{T\_{1}},S\_{T\_{2}})=e^{-rT}\mathds{1}\_{\{S\_{T\_{1}}>B,S\_{T\_{2}}>K\}}S\_{T\_{2}}/x. |  |

It reflects the sensitivity of the payoff to ST2S\_{T\_{2}}, but it fails to capture a potential change in 𝟙{ST1>B}\mathds{1}\_{\{S\_{T\_{1}}>B\}} and is therefore biased.
In contrast, the LRM estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ^LRM=π​(ST1,ST2)​ξ1x​σ​T1,\widehat{\Delta}\_{\text{LRM}}=\pi(S\_{T\_{1}},S\_{T\_{2}})\frac{\xi\_{1}}{x\sigma\,\sqrt{T\_{1}}}, |  | (29) |

is unbiased. The LRM factor in ([29](https://arxiv.org/html/2512.05301v1#S3.E29 "In 3.4 Barrier Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) does not depend on ξ2\xi\_{2} or T2T\_{2} because, given ST1S\_{T\_{1}}, the distribution of ST2S\_{T\_{2}} does not depend on the spot price xx.

![Refer to caption](x3.png)


Figure 3: Barrier options — predicted vs. target prices under standard, pathwise, and LRM training, each using a training sample size of 1024, with predictions averaged over 10 replications. RMSEs are computed from averaged predictions.

![Refer to caption](x4.png)


Figure 4: Barrier option deltas — predicted vs. target sensitivities under standard, pathwise, and LRM training, each using a training sample size of 1024, with predictions averaged over 10 replications. RMSEs are computed from averaged predictions.

Figure [3](https://arxiv.org/html/2512.05301v1#S3.F3 "Figure 3 ‣ 3.4 Barrier Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference") compares predicted and target prices under the three training regimes, averaged over 10 independent replications, with the barrier at 85 percent of the spot price.
Differential ML with pathwise labels performs poorly and shows significant bias. LRM achieves a 15-fold reduction in Price RMSE compared with the pathwise method, and a 4-fold improvement over standard ML.

Figure [4](https://arxiv.org/html/2512.05301v1#S3.F4 "Figure 4 ‣ 3.4 Barrier Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference") makes a similar comparison for barrier option deltas.
The standard and pathwise trained methods produce deltas with large errors.
The LRM trained method produces much more accurate deltas.

### 3.5 Discretized Processes

Our examples have relied on the availability of explicit transition densities in the Black-Scholes and Bachelier models. We briefly point out how the scope of LRM extends to more general models.

Consider a model defined by a possibly vector-valued process XtX\_{t} specified through a stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=μ​(Xt)​d​t+σ⊤​(Xt)​d​Wt.dX\_{t}=\mu(X\_{t})\,dt+\sigma^{\top}(X\_{t})\,dW\_{t}. |  | (30) |

In general, the density of XtX\_{t} is unknown. However, such a process is typically simulated through an Euler scheme on a time grid {0,Δ​t,2​Δ​t,…}\{0,\Delta t,2\Delta t,\dots\},
with X0=xX\_{0}=x, and

|  |  |  |
| --- | --- | --- |
|  | Xi+1=Xi+μ​(Xi)​Δ​t+σ⊤​(Xi)​Δ​t​ξi+1,ξi+1∼𝒩​(0,I).X\_{i+1}=X\_{i}+\mu(X\_{i})\Delta t+\sigma^{\top}(X\_{i})\sqrt{\Delta t}\xi\_{i+1},\quad\xi\_{i+1}\sim\mathcal{N}(0,I). |  |

For this discrete-time approximation, the conditional density p​(Xi+1|Xi)p(X\_{i+1}|X\_{i}) of Xi+1X\_{i+1} given XiX\_{i} is Gaussian with mean Xi+μ​(Xi)​Δ​tX\_{i}+\mu(X\_{i})\Delta t and covariance σ​(Xi)​σ⊤​(Xi)​Δ​t\sigma(X\_{i})\sigma^{\top}(X\_{i})\Delta t. The density of the path (x,X1,…,Xn)(x,X\_{1},\dots,X\_{n}) is the product p​(X1|x)​⋯​p​(Xn|Xn−1)p(X\_{1}|x)\cdots p(X\_{n}|X\_{n-1}) of these Gaussian densities. The LRM score function can then be written explicitly by differentiating the log of this product.
(See Section 7.3.4 of Glasserman [[6](https://arxiv.org/html/2512.05301v1#bib.bib6)] for additional details.)
The resulting LRM estimator is unbiased for the Euler scheme: it does not introduce any discretization error beyond that introduced by the Euler scheme itself.
Similar ideas can be applied to other time-discretizations of complicated models.

For small Δ​t\Delta t, the LRM estimator based on the Euler scheme may have large variance. Chen and Glasserman [[2](https://arxiv.org/html/2512.05301v1#bib.bib2)] show that more stable estimates can be obtained by averaging simpler estimates. They show that in the limit as Δ​t→0\Delta t\to 0, this approach recovers Malliavin derivatives calculated from the continuous-time process ([30](https://arxiv.org/html/2512.05301v1#S3.E30 "In 3.5 Discretized Processes ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")).
Malliavin derivatives, as proposed in Fournié et al. [[5](https://arxiv.org/html/2512.05301v1#bib.bib5)], can also be used directly as differential labels, although they are often more difficult to apply.

## 4. Gamma

We now consider further augmenting the loss function to an expression of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒGamma​(w)=1m​∑i=1m[(f^(i)−f(i))2+λ1​‖∇xf^(i)−δ(i)‖2+λ2​‖∇x2f^(i)−γ(i)‖2].\mathcal{L}\_{\text{Gamma}}(w)=\frac{1}{m}\sum\_{i=1}^{m}\Big[(\hat{f}^{(i)}-f^{(i)})^{2}+\lambda\_{1}\|\nabla\_{x}\hat{f}^{(i)}-\delta^{(i)}\|^{2}+\lambda\_{2}\|\nabla\_{x}^{2}\hat{f}^{(i)}-\gamma^{(i)}\|^{2}\Big]. |  | (31) |

The second derivatives ∇x2f^\nabla\_{x}^{2}\hat{f} of the neural network approximation are easy to evaluate using the AAD recursion ([9](https://arxiv.org/html/2512.05301v1#S2.E9 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference"))–([11](https://arxiv.org/html/2512.05301v1#S2.E11 "In 2.3 Differentiation through Backpropagation ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")) with the output zLz\_{L} set equal to ∇xf^\nabla\_{x}\hat{f} rather than f^\hat{f}. The challenge lies in finding unbiased gamma labels γ(i)\gamma^{(i)}.

The pathwise method virtually never provides unbiased gamma estimates. The problem can be seen through the case of a standard call payoff in the Black-Scholes model. Differenting pathwise once yields the pathwise delta in ([13](https://arxiv.org/html/2512.05301v1#S2.E13 "In 2.4 Differential Labels ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")), which is discontinuous in the underlying. A second application of pathwise differentiation would therefore produce biased gamma estimates.

Following the steps leading to ([19](https://arxiv.org/html/2512.05301v1#S3.E19 "In 3.1 Digital Options ‣ 3. Dealing with Discontinuities ‣ Differential ML with a Difference")) yields the following LRM estimator
of gamma,

|  |  |  |
| --- | --- | --- |
|  | π​(ST)​∇x2p​(ST;x)p​(ST;x),\pi(S\_{T})\frac{\nabla^{2}\_{x}p(S\_{T};x)}{p(S\_{T};x)}, |  |

which is broadly applicable. For payoffs without discontinuities, we can also use a hybrid pathwise-LRM estimator, which first differentiates pathwise and then applies LRM to differentiate a second time. In the case of a standard call in the Black-Scholes model, differentiating pathwise once yields ([13](https://arxiv.org/html/2512.05301v1#S2.E13 "In 2.4 Differential Labels ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")).
The resulting expression has an explicit dependence on xx, which can be differentiated directly, and an implicit dependence on xx through the distribution of STS\_{T}, which can captured by applying LRM. The combination yields

|  |  |  |
| --- | --- | --- |
|  | Γ^PW–LR=∂xδ+δ​∇xp​(ST;x)=𝟙​{ST>K}​e−r​T​STx2​(ξσ​T−1).\widehat{\Gamma}\_{\text{PW--LR}}=\partial\_{x}\delta+\delta\nabla\_{x}p(S\_{T};x)=\mathds{1}\{S\_{T}>K\}\frac{e^{-rT}S\_{T}}{x^{2}}\left(\frac{\xi}{\sigma\sqrt{T}}-1\right). |  |

To illustrate, we consider an options portfolio with payoff

|  |  |  |
| --- | --- | --- |
|  | (ST−0.85)+−1.5​(ST−0.9)++0.75​(ST−1.15)+.(S\_{T}-0.85)^{+}-1.5(S\_{T}-0.9)^{+}+0.75(S\_{T}-1.15)^{+}. |  |

We take r=0r=0, T=1/3T=1/3, and σ=0.20\sigma=0.20.
The left panel of Figure [5](https://arxiv.org/html/2512.05301v1#S4.F5 "Figure 5 ‣ 4. Gamma ‣ Differential ML with a Difference") plots the gamma for this portfolio as a function of the spot price S0S\_{0}. The right panel compares RMSEs for gamma estimates using four methods: standard ML (trained only on payouts), Delta-Pathwise and Delta-LRM (trained on payouts and delta labels), and PW-LR, trained on payouts, pathwise delta labels, and PW-LR gamma labels. The pathwise delta labels are unbiased for this problem because the payoffs are continuous.
The two delta-supervised methods give equal weight to the payout and delta components of the loss function ([5](https://arxiv.org/html/2512.05301v1#S2.E5 "In 2.2 Training Sensitivities with Prices ‣ 2. Differential Machine Learning ‣ Differential ML with a Difference")). The PW-LR methods gives 20 percent weight to the gamma component of ([31](https://arxiv.org/html/2512.05301v1#S4.E31 "In 4. Gamma ‣ Differential ML with a Difference")) and 40 percent weight to each of the other two components.
The right panel of Figure [5](https://arxiv.org/html/2512.05301v1#S4.F5 "Figure 5 ‣ 4. Gamma ‣ Differential ML with a Difference") shows that the PW-LR method performs best overall, and is consistent as sample sizes increase.

![Refer to caption](x5.png)
 ![Refer to caption](x6.png)

Figure 5: Left: Gamma of the option portfolio. Right: RMSEs for gamma estimates. The derivative-regularized methods produce smaller errors than standard ML, and PW-LR achieves the smallest errors

## 5. Conclusions

Differential ML is a valuable tool for improving the training of neural network approximations to complex simulation models used for pricing and risk management. It works by targeting price sensitivities as well as prices in the model training process.
It has two potential benefits: regularizing the fit to prices, and improving the accuracy of derivatives calculated from a neural network approximation.

To achieve these benefits, Differential ML requires unbiased differential labels. Pathwise derivatives, used in Huge and Savine [[8](https://arxiv.org/html/2512.05301v1#bib.bib8)], are biased for discontinuous payoffs, such as those with barrier or digital features. Our examples show that this bias can severely degrade the accuracy of this method. We have shown that in these cases, superior performance is attained using differential labels calculated through the likelihood ratio method. A further extension accommodates gamma labels in the training process. The Differential ML framework is sufficiently flexible to incorporate these alternative labels with only minor changes to the implementation.

## References

* [1]

  Asmussen, S., and P. W. Glynn (2007)
  Stochastic Simulation, Springer, New York.
* [2]

  Chen, N., and P. Glasserman (2007)
  Malliavin Greeks without Malliavin calculus,
  Stochastic Processes and their Applications
  117(1), 1689–1723.
* [3]

  Dixon, M., I. Halperin, and P. Bilokon (2020),
  Machine Learning in Finance, Springer Nature, Switzerland.
* [4]

  Horvath, B., A. Muguruza, and M. Tomas (2021),
  Deep learning volatility,
  Quantitative Finance 21(1), 11–27.
* [5]

  Fournié, E., J. M. Lasry, J. Lebuchoux, P. L. Lions, and N. Touzi (1999). Applications of Malliavin calculus to Monte Carlo methods in finance,
  Finance and Stochastics 3(4), 391–412.
* [6]

  Glasserman, P. (2004)
  Monte Carlo Methods in Financial Engineering,
  Springer, New York.
* [7]

  Goodfellow, I., Y. Bengio, and A. Courville (2016)
  Deep Learning, MIT Press.
* [8]

  Huge, B., and A. Savine (2020)
  The shape of things to come, Risk.net,
  October.
* [9]

  Raissi, M., P. Perdikaris, and G. E. Karniadakis (2019)
  Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.
  Journal of Computational Physics 378, 686–707.