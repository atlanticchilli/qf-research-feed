---
authors:
- George Awiakye-Marfo
- Elijah Agbosu
- Victoria Mawuena Barns
- Samuel Asante Gyamerah
doc_id: arxiv:2601.16446v1
family_id: arxiv:2601.16446
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory
  (LSTM) Network'
url_abs: http://arxiv.org/abs/2601.16446v1
url_html: https://arxiv.org/html/2601.16446v1
venue: arXiv q-fin
version: 1
year: 2026
---


George Awiakye-Marfo
Department of Statistics and Actuarial Science, Kwame Nkrumah University of Science and Technology, Kumasi, Ghana
  
Elijah Agbosu11footnotemark: 1
  
Victoria Mawuena Barns11footnotemark: 1
  
Samuel Asante Gyamerah
Department of Mathematics, Toronto Metropolitan University, Toronto, Canada

###### Abstract

Deep learning models are effective for sequential data modeling, yet commonly used activation functions such as ReLU, LeakyReLU, and PReLU often exhibit gradient instability when applied to noisy, non-stationary financial time series. This study introduces BrownianReLU, a stochastic activation function induced by Brownian motion that enhances gradient propagation and learning stability in Long Short-Term Memory (LSTM) networks. Using Monte Carlo simulation, BrownianReLU provides a smooth, adaptive response for negative inputs, mitigating the dying ReLU problem. The proposed activation is evaluated on financial time series from Apple, GCB, and the S&P 500, as well as LendingClub loan data for classification. Results show consistently lower Mean Squared Error and higher R2R^{2} values, indicating improved predictive accuracy and generalization. Although ROC–AUC metric is limited in classification tasks, activation choice significantly affects the trade-off between accuracy and sensitivity, with Brownian ReLU and the selected activation functions yielding practically meaningful performance.

Keywords: Brownian ReLU; Leaky ReLU; Long Short Term Memory; ReLU; PReLU

## 1 Introduction

In recent years, deep neural networks (DNNs) have revolutionized the approach to solving complex tasks across diverse fields, including pattern recognition, natural language processing, information retrieval, recommendation systems, medical diagnostics, and financial forecasting. Central to the architecture of neural networks, such as convolutional neural networks (CNNs) and recurrent neural networks (RNNs), is the activation function (AF). This critical component introduces nonlinearity, neural networks to capture and represent intricate relationships in data, which is essential for their success in tackling such multifaceted problems. Activation functions are essential in neural networks for learning and interpreting complex, non-linear relationships between input data and the target output. They enable the network to model intricate functional mappings, making it possible to solve sophisticated problems effectively. Without activation functions, the network would only handle simple linear transformations, significantly limiting its utility [[3](https://arxiv.org/html/2601.16446v1#bib.bib3)]. Over the past years, numerous activation functions have been proposed, varying in computational complexity and performance. The famous nonlinear monotonic activation function usually include the sigmoid function of [[5](https://arxiv.org/html/2601.16446v1#bib.bib5)], this was one of the earliest nonlinear activation functions used in deep learning, mapping all input values to the range (0, 1). The Tanh function [[12](https://arxiv.org/html/2601.16446v1#bib.bib12)] resolved the non-zero-centered output issue of the sigmoid function but, like sigmoid, suffers from vanishing gradients and saturation, limiting its effectiveness in training deep neural networks. Several
improvements have been proposed based on the Sigmoid and Tanh family of activation functions, notably the shifted and scaled sigmoid as used in [[1](https://arxiv.org/html/2601.16446v1#bib.bib1)], the scaled hyperbolic tangent activation function of [[18](https://arxiv.org/html/2601.16446v1#bib.bib18)], the sigmoid-algebraic and triple - state sigmoid activation functions of [[15](https://arxiv.org/html/2601.16446v1#bib.bib15)], the penalised hyperbolic tangent function of [[29](https://arxiv.org/html/2601.16446v1#bib.bib29)] . Other examples include linearly scaled hyperbolic tangent function of [[26](https://arxiv.org/html/2601.16446v1#bib.bib26)], the sigmoid and tanh combination of [[27](https://arxiv.org/html/2601.16446v1#bib.bib27)], the soft-root-sigmoid of [[19](https://arxiv.org/html/2601.16446v1#bib.bib19)], the sigmoid - Gumbel activation function of [[14](https://arxiv.org/html/2601.16446v1#bib.bib14)] among others. These extensions aimed to mitigate the vanishing gradient problem but most of them only provided partial improvements rather than complete solutions.
However, the introduction of the ReLU activation function by [[23](https://arxiv.org/html/2601.16446v1#bib.bib23)] significantly mitigated this issue due to its simplicity and superior performance, leading to its widespread adoption in deep learning applications
as evidenced in various studies e.g . [[16](https://arxiv.org/html/2601.16446v1#bib.bib16)] and [[24](https://arxiv.org/html/2601.16446v1#bib.bib24)]. Nonetheless, ReLU had its own limitations, the non-differentiability at zero, unbounded outputs, and the “dying ReLU" issue, where neurons cease to learn. To overcome these challenges, researchers have developed several modified versions of ReLU. The Leaky ReLu for instance addresses the issue of “dying neurons" in standard ReLU by allowing a small, nonzero gradient for negative inputs instead of outputting zero. This “leak" ensures that neurons remain active and continue to learn for negative inputs, [[21](https://arxiv.org/html/2601.16446v1#bib.bib21)]. Another variant of the ReLU is the Randomised Leaky ReLU of [[28](https://arxiv.org/html/2601.16446v1#bib.bib28)] where the slope of the negative input region is chosen randomly during training. However, the randomised Leaky ReLU (LReLU) struggles with selecting the optimal slope for negative inputs, which can vary depending on the specific problem which the Parametric ReLU (PReLU) of [[8](https://arxiv.org/html/2601.16446v1#bib.bib8)] improves by making the slope for negative inputs a trainable parameter, enabling the model to adaptively learn the best slope during training. Other functions include the bounded ReLU (BReLU) of [[20](https://arxiv.org/html/2601.16446v1#bib.bib20)] which is a modified version of ReLU that restricts the output range to address potential instability caused by ReLU’s unbounded outputs, the Elastic ReLU and Elastic parametric ReLU of [[11](https://arxiv.org/html/2601.16446v1#bib.bib11)], the softplus of [[4](https://arxiv.org/html/2601.16446v1#bib.bib4)] as well as ELU and its variants, [[2](https://arxiv.org/html/2601.16446v1#bib.bib2)]. The mish and swish of [[22](https://arxiv.org/html/2601.16446v1#bib.bib22)] and [[25](https://arxiv.org/html/2601.16446v1#bib.bib25)] respectively were smooth, non-monotonic and differentiable activation functions that incorporates a learnable parameter. This parameter enables the model to automatically optimize and adapt the activation function to the specific task during training, offering flexibility and improving performance. The noisy activation function introduced by [[6](https://arxiv.org/html/2601.16446v1#bib.bib6)] also enhances the optimizer’s ability to explore the parameter space more effectively and accelerates learning by adding stochastic samples from a normal distribution to the activations, these models mimics the uncertainty and stochastic behavior seen in neural activity, For an indepth discussion on activation functions see [[7](https://arxiv.org/html/2601.16446v1#bib.bib7), [17](https://arxiv.org/html/2601.16446v1#bib.bib17)].
On the other hand LSTM introduced by [[10](https://arxiv.org/html/2601.16446v1#bib.bib10)] with its gating mechanisms network was designed to address the key limitation of vanishing gradient in earlier Recurrent Neural Networks (RNNs).It uses a unique architecture with memory cells and gating mechanisms (input, forget, and output gates) that allow the network to retain important information over long periods and selectively forget irrelevant data and effective for remembering long-term dependencies. Although LSTMs somewhat solved the vanishing gradient problem and made it possible to learn and retain long-term dependencies, enabling deep learning models to perform better on sequential tasks. Improved activation functions in LSTM models are sought after to enhance the model’s learning capacity, performance, and stability, addressing various challenges in training and optimizing LSTMs, especially in deep learning tasks involving sequential data.This study introduces Brownian ReLU (Br-ReLU), a modified ReLU activation function incorporating stochastic elements inspired by Brownian motion.

The introduction of Brownian noise into the LSTM network’s activation function is to facilitate smoother gradient flow, potentially improving learning dynamics.
This idea combines the deterministic form of ReLU with randomness from Brownian motion, potentially improving model robustness. We hypothesise that enhanced gating mechanisms using the Br-ReLu would improve the network’s ability to model uncertainty in data, particularly in domains like financial forecasting, climate modeling where stochasticity plays a critical role. We test this new formulation with the closing prices of S&P 500, Apple, Ghana Commercial Bank (GCB) stock data and an LSTM-based classifier for the LendingClub loan data for status prediction. This paper is structured as follows: Section 2 discusses the related works and the model formulation. The results and discussion are presented in Section 3, and we finally conclude in Section 4.

## 2 Activation Functions

We review the relative nonlinear activation functions of Rectified Linear Unit (ReLU), Leaky ReLU, and the parametric ReLU as well as introduce the proposed Brownian ReLU.

### 2.1 ReLU, LReLU, Parametric ReLU and Noisy Activation Functions

* (a)

  The ReLU activation function of [[23](https://arxiv.org/html/2601.16446v1#bib.bib23)] is:

  |  |  |  |
  | --- | --- | --- |
  |  | f​(x)=max⁡(0,x)f(x)=\max(0,x) |  |

  If x>0x>0, f​(x)=xf(x)=x (the function outputs the input directly).
  If x≤0x\leq 0, f​(x)=0f(x)=0 (the function outputs zero).
* (b)

  The Leaky ReLU activation function is given as:

  |  |  |  |
  | --- | --- | --- |
  |  | f​(x)={xif ​x>0α​xif ​x≤0f(x)=\begin{cases}x&\text{if }x>0\\ \alpha x&\text{if }x\leq 0\end{cases} |  |

  Here:
  xx is the input, α\alpha is a small positive constant (e.g., 0.010.01) that determines the slope for x≤0x\leq 0.
  The Leaky ReLU addresses the “dying ReLU" problem by allowing a small, non-zero gradient for negative values of xx, ensuring neurons do not become inactive, [[21](https://arxiv.org/html/2601.16446v1#bib.bib21)]
* (c)

  The parametric ReLU (PReLU) activation function is a variation of the ReLU activation function where the slope for negative inputs is learned during training. It is given as :

  |  |  |  |
  | --- | --- | --- |
  |  | f​(x)={xif ​x>0,α​xif ​x≤0,f(x)=\begin{cases}x&\text{if }x>0,\\ \alpha x&\text{if }x\leq 0,\end{cases} |  |

  where:
    
  xx is the input to the activation function. α\alpha is a learnable parameter that adjusts the slope for negative inputs. It is initialized and updated during training using GD or other optimization algorithms, allowing the network to learn an optimal value for the negative slope. This flexibility allows PReLU to adapt better to specific tasks, potentially improving performance by addressing the “dying ReLU" problem, [[8](https://arxiv.org/html/2601.16446v1#bib.bib8)].
* (d)

  The Gaussian Error Linear Unit (GELU) activation function of [[9](https://arxiv.org/html/2601.16446v1#bib.bib9)] weights inputs by their value rather than gating them as ReLUs do. It is given by:

  |  |  |  |
  | --- | --- | --- |
  |  | GELU​(x)=x⋅Φ​(x),\text{GELU}(x)=x\cdot\Phi(x), |  |

  where Φ​(x)\Phi(x) is the cumulative distribution function (CDF) of the standard normal distribution:

  |  |  |  |
  | --- | --- | --- |
  |  | Φ​(x)=12​[1+erf​(x2)],\Phi(x)=\frac{1}{2}\left[1+\text{erf}\left(\frac{x}{\sqrt{2}}\right)\right], |  |

  and erf​(x)\text{erf}(x) is the error function. This approximation is computationally efficient and commonly used in practice.

### 2.2 Proposed Brownian ReLU (Br-ReLU) Activation Function

The BrownianReLU activation function leverages the stochastic properties of Brownian motion to introduce adaptive nonlinearity into neural networks and make it more adaptive to actual data. However, since standard Brownian motion is not defined over non-negative inputs, its direct applicability to negative inputs is limited, we therefore the employ the symmetry principle of Brownian motion. [[13](https://arxiv.org/html/2601.16446v1#bib.bib13)].
This principle enables the extension of Brownian motion behaviour to negative values through reflection or symmetry.We give the activation function in equation ([1](https://arxiv.org/html/2601.16446v1#S2.E1 "In 2.2 Proposed Brownian ReLU (Br-ReLU) Activation Function ‣ 2 Activation Functions ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network")) below;

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)={xfor ​x>0,−α​B​(|x|)for ​x≤0,f(x)=\begin{cases}x&\text{for }x>0,\\ -\alpha B(|x|)&\text{for }x\leq 0,\end{cases} |  | (1) |

where B​(|x|)∼𝒩​(0,|x|)B(|x|)\sim\mathcal{N}(0,\lvert x\rvert) and α\alpha is a learnable parameter controlling the negative slope, consistent with that of the PReLU activation function.
[[8](https://arxiv.org/html/2601.16446v1#bib.bib8)]. BrownianReLU returns the identity for positive inputs, while for negative inputs it produces a stochastic path, generated through Monte Carlo simulations, as shown in equation ([2](https://arxiv.org/html/2601.16446v1#S2.E2 "In 2.2 Proposed Brownian ReLU (Br-ReLU) Activation Function ‣ 2 Activation Functions ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network")) and illustrated in Figure ([1](https://arxiv.org/html/2601.16446v1#S2.F1 "Figure 1 ‣ 2.2 Proposed Brownian ReLU (Br-ReLU) Activation Function ‣ 2 Activation Functions ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)={xfor ​x>0,−α⋅1M​∑i=1MBk​(|xi|)for ​x≤0,f(x)=\begin{cases}x&\text{for }x>0,\\ -\alpha\cdot\dfrac{1}{M}\sum\limits\_{i=1}^{M}B^{k}(|x\_{i}|)&\text{for }x\leq 0,\end{cases} |  | (2) |

where B​(|x|)∼𝒩​(0,|x|)B(\lvert x\rvert)\sim\mathcal{N}(0,\lvert x\rvert) and MM is the number of sample paths. Figure ([1](https://arxiv.org/html/2601.16446v1#S2.F1 "Figure 1 ‣ 2.2 Proposed Brownian ReLU (Br-ReLU) Activation Function ‣ 2 Activation Functions ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network")), shows the Brownian ReLU activation for some α\alpha and different values of MM.

![Refer to caption](brownian_relu_stability_plot.png)


Figure 1: Illustrative Monte Carlo paths for Br-ReLU Activation Function

It demonstrates the limiting behavior of the Monte Carlo mean path for negative inputs as the number of simulated sample paths increases from 1 to 1000. As M grows, the mean path converges with reduced variance and greater smoothness, consistent with the law of large numbers.

#### 2.2.1 Alpha Adaptation

The adaptation of the parameter α\alpha in Br-ReLU is fundamental in regulating the behavior of the activation function, particularly within the negative input domain. Similarly, we explore the training process of α\alpha in [[8](https://arxiv.org/html/2601.16446v1#bib.bib8)] in the proposed Br-ReLU. This enables the model to adjust the degree of stochastic perturbation applied to negative inputs based on the data distribution.

![Refer to caption](M=200.png)


Figure 2: Varying values of α\alpha at M=200

![Refer to caption](M=500.png)


Figure 3: Varying values of α\alpha at M=500

![Refer to caption](M=1000.png)


Figure 4: Varying values of α\alpha at M=1000

![Refer to caption](M=1500.png)


Figure 5: Varying values of α\alpha at M=1500

Figure 6: Figure showing subfigures 2, 3, 4 and 5

Figure ([6](https://arxiv.org/html/2601.16446v1#S2.F6 "Figure 6 ‣ 2.2.1 Alpha Adaptation ‣ 2.2 Proposed Brownian ReLU (Br-ReLU) Activation Function ‣ 2 Activation Functions ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network")) illustrates the effect of varying alpha with increasing sample sizes M. For values of
M=200,500M=200,500, the Monte Carlo mean path remains relatively noisy, whereas larger M values (1000 and 1500) produce smoother and more stable paths. Across all cases, alpha controls the scaling on the negative input side, with higher values amplifying stochastic fluctuations and smaller values keeping the path closer to zero. We note that when α=0\alpha=0 we obtain the ReLU function.

#### 2.2.2 Gradient computation and parameter optimisation for BrownianReLU

Consider the activation in ([3](https://arxiv.org/html/2601.16446v1#S2.E3 "In 2.2.2 Gradient computation and parameter optimisation for BrownianReLU ‣ 2.2 Proposed Brownian ReLU (Br-ReLU) Activation Function ‣ 2 Activation Functions ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x;α)={xfor ​x>0,−α⋅1M​∑k=1MBk​(|xi|)for ​x≤0,f(x;\alpha)=\begin{cases}x&\text{for }x>0,\\ -\alpha\cdot\dfrac{1}{M}\sum\limits\_{k=1}^{M}B^{k}(|x\_{i}|)&\text{for }x\leq 0,\end{cases} |  | (3) |

where for each input xx the values B(k)​(|x|)B^{(k)}(|x|), k=1,…,Mk=1,\dots,M, are independent draws with
B(k)​(|x|)∼𝒩​(0,|x|)B^{(k)}(|x|)\sim\mathcal{N}(0,|x|) and α∈ℝ\alpha\in\mathbb{R} is a learnable parameter. Let the model output for sample ii be yi=f​(xi;α)y\_{i}=f(x\_{i};\alpha)
and let the Monte Carlo average of the sample be

|  |  |  |
| --- | --- | --- |
|  | bi:=1M​∑k=1MB(k)​(|xi|),so thatf​(xi;α)={x,x>0,−α​bi,xi≤0.b\_{i}\;:=\;\frac{1}{M}\sum\_{k=1}^{M}B^{(k)}(|x\_{i}|)\,,\hskip 14.22636pt\text{so that}\hskip 14.22636ptf(x\_{i};\alpha)=\begin{cases}x,&x>0,\\[6.0pt] -\,\alpha\,b\_{i},&x\_{i}\leq 0.\end{cases} |  |

Again let δi=∂Li/∂yi\delta\_{i}=\partial L\_{i}/\partial y\_{i}, be the gradient at the activation, where LiL\_{i} is the loss for sample ii
Then

|  |  |  |
| --- | --- | --- |
|  | ∂f​(xi;α)∂α={0,x>0,−bi,xi≤0.\frac{\partial f(x\_{i};\alpha)}{\partial\alpha}=\begin{cases}0,&x>0,\\[6.0pt] -\,b\_{i},&x\_{i}\leq 0.\end{cases} |  |

Hence, the contribution per-sample to the gradient of the loss w.r.t. α\alpha is

|  |  |  |
| --- | --- | --- |
|  | ∂Li∂α=δi​∂yi∂α={0,xi>0,−δi​bi,xi≤0.\frac{\partial L\_{i}}{\partial\alpha}=\delta\_{i}\frac{\partial y\_{i}}{\partial\alpha}=\begin{cases}0,&x\_{i}>0,\\[6.0pt] -\,\delta\_{i}\,b\_{i},&x\_{i}\leq 0.\end{cases} |  |

For a minibatch ℬ\mathcal{B} the gradient estimator is the sum over the batch:

|  |  |  |
| --- | --- | --- |
|  | ∂Lℬ∂α=−∑i∈ℬδi​ 1{xi≤0}​bi=−∑i∈ℬδi​ 1{xi≤0}​1M​∑k=1MB(k)​(|xi|).\frac{\partial L\_{\mathcal{B}}}{\partial\alpha}=-\sum\_{i\in\mathcal{B}}\delta\_{i}\,\mathbf{1}\_{\{x\_{i}\leq 0\}}\,b\_{i}=-\sum\_{i\in\mathcal{B}}\delta\_{i}\,\mathbf{1}\_{\{x\_{i}\leq 0\}}\;\frac{1}{M}\sum\_{k=1}^{M}B^{(k)}(|x\_{i}|). |  |

With a learning rate η\eta a simple SGD step can be obatined as;

|  |  |  |
| --- | --- | --- |
|  | α←α+η​∑i∈ℬδi​ 1{xi≤0}​bi=α+η​∑i∈ℬδi​ 1{xi≤0}​(1M​∑k=1MB(k)​(|xi|)).\alpha\leftarrow\alpha+\eta\sum\_{i\in\mathcal{B}}\delta\_{i}\,\mathbf{1}\_{\{x\_{i}\leq 0\}}\,b\_{i}\;=\;\alpha+\eta\sum\_{i\in\mathcal{B}}\delta\_{i}\,\mathbf{1}\_{\{x\_{i}\leq 0\}}\left(\frac{1}{M}\sum\_{k=1}^{M}B^{(k)}(|x\_{i}|)\right). |  |

#### 2.2.3 Training Procedure with BrownianReLU Activation

Input: Training data {(xi,ti)}\{(x\_{i},t\_{i})\}, learning rate η\eta, number of Monte Carlo samples MM

Output: Updated model parameters (including α\alpha)

for each minibatch ℬ\mathcal{B} do

for each input xix\_{i} in ℬ\mathcal{B} do

if xi>0x\_{i}>0 then

yi←xiy\_{i}\leftarrow x\_{i}

else

for k=1k=1 to MM do

Sample B(k)​(|xi|)∼𝒩​(0,|xi|)B^{(k)}(|x\_{i}|)\sim\mathcal{N}(0,|x\_{i}|)

end for

B¯​(|xi|)←1M​∑k=1MB(k)​(|xi|)\bar{B}(|x\_{i}|)\leftarrow\frac{1}{M}\sum\_{k=1}^{M}B^{(k)}(|x\_{i}|)

yi←−α⋅B¯​(|xi|)y\_{i}\leftarrow-\alpha\cdot\bar{B}(|x\_{i}|)

end if

[0.5em]
 end for

[0.5em]
 Compute minibatch loss:
Lℬ=∑i∈ℬL​(yi,ti)L\_{\mathcal{B}}=\sum\_{i\in\mathcal{B}}L(y\_{i},t\_{i})

Backpropagate to compute:
δi=∂Li∂yi\delta\_{i}=\frac{\partial L\_{i}}{\partial y\_{i}}

Compute gradient w.r.t. α\alpha:
∂Lℬ∂α=−∑i∈ℬδi⋅𝟏{xi≤0}​B¯​(|xi|)\frac{\partial L\_{\mathcal{B}}}{\partial\alpha}=-\sum\_{i\in\mathcal{B}}\delta\_{i}\cdot\mathbf{1}\_{\{x\_{i}\leq 0\}}\,\bar{B}(|x\_{i}|)

Update α\alpha:
α←α−η​∂Lℬ∂α\alpha\leftarrow\alpha-\eta\,\frac{\partial L\_{\mathcal{B}}}{\partial\alpha}

Update other network parameters using standard SGD

end for

Algorithm 1 Training Procedure with BrownianReLU Activation

### 2.3 LSTM System Model

We apply the proposed activation on a basic LSTM architecture that consists of three main components: an input layer, a hidden layer, and an output layer. At each time step tt, the input vector xtx\_{t} is fed into the network, the components of the block governed by the following equations.

* (a)

  The forget gate determines what information should be discarded from the cell state.

  |  |  |  |
  | --- | --- | --- |
  |  | ft=σ​(Wf​xt+Uf​ht−1+bf)f\_{t}=\sigma(W\_{f}x\_{t}+U\_{f}h\_{t-1}+b\_{f}) |  |
* (b)

  The input gate controls what information to add to the cell state.

  |  |  |  |
  | --- | --- | --- |
  |  | it=σ​(Wi​xt+Ui​ht−1+bi)i\_{t}=\sigma(W\_{i}x\_{t}+U\_{i}h\_{t-1}+b\_{i}) |  |
* (c)

  The input gate is complemented by a candidate cell state, given as:

  |  |  |  |
  | --- | --- | --- |
  |  | C~t=tanh⁡(Wc​xt+Uc​ht−1+bc)\tilde{C}\_{t}=\tanh(W\_{c}x\_{t}+U\_{c}h\_{t-1}+b\_{c}) |  |
* (d)

  The cell state CtC\_{t} is updated using the forget gate, input gate, and candidate cell state:

  |  |  |  |
  | --- | --- | --- |
  |  | Ct=ft⊙Ct−1+it⊙C~tC\_{t}=f\_{t}\odot C\_{t-1}+i\_{t}\odot\tilde{C}\_{t} |  |

  Where ⊙\odot represents element-wise multiplication.
* (e)

  The output gate determines what information to output from the cell.

  |  |  |  |
  | --- | --- | --- |
  |  | ot=σ​(Wo​xt+Uo​ht−1+bo)o\_{t}=\sigma(W\_{o}x\_{t}+U\_{o}h\_{t-1}+b\_{o}) |  |
* (f)

  Finally, the hidden state hth\_{t} is updated as:

  |  |  |  |
  | --- | --- | --- |
  |  | ht=ot⊙tanh⁡(Ct)h\_{t}=o\_{t}\odot\tanh(C\_{t}) |  |

where; ftf\_{t}, iti\_{t} and oto\_{t} are the functions of the forget, input and output gates respectively. WfW\_{f} and UfU\_{f} are weights applied to the current input xtx\_{t} and previous hidden state ht−1h\_{t-1}, respectively, bfb\_{f} is the bias vector and σ\sigma is the sigmoid activation function. C~t\tilde{C}\_{t} is the candidate cell state, Wi,Wc,Ui,UcW\_{i},W\_{c},U\_{i},U\_{c}, and bi,bcb\_{i},b\_{c} are weights and biases, tanh\tanh is the hyperbolic tangent activation function.
In this study the proposed activation function is applied to the cell state and the hidden state, these are key components in the model [[10](https://arxiv.org/html/2601.16446v1#bib.bib10)]. The equation of the Cell State and the hidden state is now updated to;

|  |  |  |  |
| --- | --- | --- | --- |
|  | C~t=Br-ReLU​(Wx​c​Xt+Wh​c​ht−1+bc)\displaystyle\tilde{C}\_{t}=\text{Br-ReLU}(W\_{xc}X\_{t}+W\_{hc}h\_{t-1}+b\_{c}) |  | (4) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=ot​Br-ReLU​(Ct)\displaystyle h\_{t}=o\_{t}\text{Br-ReLU}(C\_{t}) |  | (5) |

## 3 Numerical Results

Here, we perform a comparison among the various activation functions for the various different datasets notably the Ghana commercial Bank (GCB) stock data, Apple and S&P 500.

### 3.1 Descriptive Statistics

Table [1](https://arxiv.org/html/2601.16446v1#S3.T1 "Table 1 ‣ 3.1 Descriptive Statistics ‣ 3 Numerical Results ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network") presents the mean and variance values for the Apple, GCB, and S&P 500 stock datasets. Amongst the three, the S&P 500 shows the highest mean (0.3545) and variance (0.0626), indicating relatively larger average returns and greater volatility. Apple follows closely with a mean of 0.3267 and variance of 0.0576, showing moderate fluctuations in stock movements. GCB, on the other hand, records the lowest variance (0.0326), suggesting more stable returns.

Table 1: Variance of Apple, GCB, and S&P500 stock dataset

| No. | Data | Mean | Variance |
| --- | --- | --- | --- |
| 1 | Apple | 0.326708 | 0.057563 |
| 2 | S&P500 | 0.354458 | 0.062592 |
| 3 | GCB | 0.341235 | 0.032637 |

### 3.2 Sensitivity Analysis

Table 2: Sensitivity analysis of BrownianReLU sample paths across datasets

| Data | Evaluation Matrix | Evaluation at Different MM | | |
| --- | --- | --- | --- | --- |
|  |  | M=500M=500 | M=1000M=1000 | M=1500M=1500 |
|  | MSE | 0.002122 | 0.003 1620.003\,162 | 0.002 0350.002\,035 |
| Apple | R2R^{2}(Test) | 0.9355 | 0.90360.9036 | 0.93810.9381 |
|  | Epoch | 48 | 4646 | 4949 |
|  | MSE | 0.000284 | 0.000 2750.000\,275 | 0.000 2760.000\,276 |
| GCB | R2R^{2}(Test) | 0.9864 | 0.98690.9869 | 0.98680.9868 |
|  | Epoch | 44 | 4444 | 3636 |
|  | MSE | 0.00038 | 0.000 2320.000\,232 | 0.000 5850.000\,585 |
| SP500 | R2R^{2}(Test) | 0.9829 | 0.98960.9896 | 0.97360.9736 |
|  | Epoch | 50 | 5050 | 5050 |

Table LABEL:tab:sensitivity\_analysis shows the sensitivity analysis of the proposed BrownianReLU activation function across the three datasets: Apple, GCB, and S&P500. The evaluation was based on the mean squared error (MSE), the coefficient of determination on the test set (R2R^{2}), and the number of epochs required for training. Performance was assessed under three different sample path sizes, namely M=500M=500, M=1000M=1000, and M=1500M=1500.For the Apple dataset, MSE values range between 0.002122 and 0.002035, with R2R^{2} values varying from 0.9036 to 0.9381, indicating moderate sensitivity to the choice of MM. The GCB dataset exhibits highly stable behavior, with consistently low MSE values (approximately 0.00028) and R2R^{2} values near 0.987 across all values of MM. On the otherhad, the SP500 dataset shows greater variation: the lowest MSE (0.000232) and highest R2R^{2} (0.9896) occur at M=1000M=1000, while performance declines at M=1500M=1500 with MSE increasing to 0.000585 and R2R^{2} falling to 0.9736 with varying numbers of epochs also differs across datasets. For Apple, convergence occurs between 46 and 49 epochs, while GCB converges within 36–44 epochs. The SP500 dataset, however, consistently requires 50 epochs across all settings. The results suggest that the choice of sample paths (MM) can influence both accuracy and training efficiency, particularly for datasets with higher variability such as S&P500. M=1000M=1000 appears to provide a favorable balance between error minimization and performance generalisation.

### 3.3 Evaluating BrownianReLU Against Standard Activation Functions on Multiple Datasets

Table 3: Comparison of Standard activation functions with Brownian RELU using the Apple dataset

| No. | Activation Function | MSE | R2R^{2}(Train) | R2R^{2}(Test) | Epoch of convergence |
| --- | --- | --- | --- | --- | --- |
| 1 | BrownianReLU | 0.002035 | 0.9903 | 0.9381 | 49 |
| 2 | LeakyReLU | 0.160918 | 0.9543 | 0.5546 | 48 |
| 3 | PReLU | 0.043347 | 0.9904 | 0.7425 | 13 |
| 4 | ReLU | 0.005931 | 0.9881 | 0.3164 | 36 |
| 5 | Tanh | 0.004110 | 0.9592 | 0.7297 | 3 |

Table [3](https://arxiv.org/html/2601.16446v1#S3.T3 "Table 3 ‣ 3.3 Evaluating BrownianReLU Against Standard Activation Functions on Multiple Datasets ‣ 3 Numerical Results ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network") compares the proposed BrownianReLU activation function with the following activation function LeakyReLU, PReLU, ReLU, and Tanh using the Apple dataset. BrownianReLU activation function achieved the lowest MSE (0.002035) and the highest test R2R^{2} (0.9381), indicating superior predictive performance. While PReLU and ReLU performed well during training, their lower test R2R^{2} values suggest weaker generalization. LeakyReLU produced the poorest results with a negative test R2R^{2}, whereas Tanh converged quickly with moderate accuracy.

Table 4: Comparison of Standard activation functions with Brownian RELU using the GCB dataset

| No. | Activation Function | MSE | R2R^{2}(Train) | R2R^{2}(Test) | Epoch of convergence |
| --- | --- | --- | --- | --- | --- |
| 1 | BrownianReLU | 0.000275 | 0.9982 | 0.9869 | 44 |
| 2 | LeakyReLU | 0.000303 | 0.9980 | 0.9855 | 46 |
| 3 | PReLU | 0.000291 | 0.9985 | 0.9861 | 44 |
| 4 | ReLU | 0.000288 | 0.9985 | 0.9862 | 48 |
| 5 | Tanh | 0.000333 | 0.9980 | 0.9841 | 48 |
| 6 | GELU | 0.000387 | 0.9976 | 0.9815 | 50 |

The results in Table [4](https://arxiv.org/html/2601.16446v1#S3.T4 "Table 4 ‣ 3.3 Evaluating BrownianReLU Against Standard Activation Functions on Multiple Datasets ‣ 3 Numerical Results ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network") shows the performance metrics across all models. The result show generally consistent result across all metrics, reflecting the inherent stability of the dataset. Among the compared functions, BrownianReLU recorded the lowest MSE (0.000275) and the highest test R2R^{2} (0.9869), demonstrating a slight yet meaningful improvement in predictive accuracy. Although ReLU and PReLU, Tanh, and GELU exhibited comparable performance, the GELU activation function produced the highest MSE and lowest test R2R^{2}, indicating relatively weaker generalization. Overall, the BrownianReLU showed strong accuracy and stable convergence and hence its effectiveness on the GCB dataset.

Table 5: Comparison of the standard Activation functions to the proposed activation function using the S&P500 dataset

| No. | Activation Function | MSE | R2R^{2}(Train) | R2R^{2}(Test) | Epoch of convergence |
| --- | --- | --- | --- | --- | --- |
| 1 | BrownianReLU | 0.000242 | 0.9973 | 0.9891 | 48 |
| 2 | LeakyReLU | 0.011240 | 0.9380 | 0.4917 | 2 |
| 3 | PReLU | 0.002399 | 0.9965 | 0.8915 | 42 |
| 4 | ReLU | 0.003820 | 0.9964 | 0.8272 | 24 |
| 5 | Tanh | 0.000255 | 0.9972 | 0.9841 | 50 |
| 6 | GELU | 0.012362 | 0.9931 | 0.4426 | 37 |

In Table [5](https://arxiv.org/html/2601.16446v1#S3.T5 "Table 5 ‣ 3.3 Evaluating BrownianReLU Against Standard Activation Functions on Multiple Datasets ‣ 3 Numerical Results ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network") among all models, BrownianReLU achieved the lowest MSE (0.000242) and the highest test R2R^{2} (0.9891), indicating superior predictive accuracy. The Tanh activation also performed competitively, with similar MSE and R2R^{2} values, though it required slightly more epochs to converge. In contrast, LeakyReLU produced the weakest performance, with a much higher MSE (0.011240) closely followed by GELU and a test R2R^{2} of 0.4917 and 0.4426 respectivley, suggesting relatively poorer adaptability to the dataset. PReLU and ReLU showed reasonable results but lagged behind BrownianReLU in both accuracy and stability.

### 3.4 Visual Predictions of BrownianReLU Across Various Datasets.

The following figures illustrate the predictive performance of the proposed BrownianReLU activation function across different financial datasets. Each figure compares the predicted stock price trends of the model with the actual data.

![Refer to caption](apple_prediction.png)


(a) Apple stock prediction

![Refer to caption](gcb_prediction.png)


(b) GCB stock prediction

![Refer to caption](sap_prediction.png)


(c) S&P 500 prediction

Figure 7: Visual predictions of the BrownianReLU model across the Apple, GCB, and S&P 500 datasets.

Across all three datasets, the predicted values closely align with the actual stock movements, indicating the model’s ability to capture nonlinear patterns and dependencies effectively.
For the Apple dataset, the predictions exhibit a smooth fit with slight or minimal deviations, indicating strong learning stability and generalization. In the GCB dataset, the predictions maintain consistent accuracy, suggesting robustness even in relatively low-volatility financial data. The S&P 500 predictions display slightly more fluctuations due to the index’s inherent market complexity, however, the model successfully tracks the major trends and fluctuations, see Figure ([7](https://arxiv.org/html/2601.16446v1#S3.F7 "Figure 7 ‣ 3.4 Visual Predictions of BrownianReLU Across Various Datasets. ‣ 3 Numerical Results ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network")).The results demonstrate that BrownianReLU provides high predictive accuracy across varying market behaviors, validating its effectiveness in handling volatility and long-term dependencies in financial time series and risk analytics.

### 3.5 Classification Performance Analysis

This section evaluates the effect of the various activation functions on the performance of an LSTM-based classifier for loan status prediction. The proposed BrownianReLU is compared with standard activations shown in Table [6](https://arxiv.org/html/2601.16446v1#S3.T6 "Table 6 ‣ 3.5 Classification Performance Analysis ‣ 3 Numerical Results ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network"). Performance is assessed using Accuracy, Precision, Recall, F1-score, and ROC–AUC. Given the inherent class imbalance in loan payment data, emphasis is placed on Recall, F1-score, and ROC–AUC, which more accurately reflect the model’s ability to detect minority-class outcomes.

Table 6: Classification Performance of LSTM with Different Activation Functions

| Activation Function | Accuracy | Precision | Recall | F1-score | ROC–AUC |
| --- | --- | --- | --- | --- | --- |
| BrownianReLU (α=0.014\alpha=0.014) | 0.7261 | 0.1845 | 0.1033 | 0.1324 | 0.5036 |
| BrownianReLU (α=0.464\alpha=0.464) | 0.7250 | 0.2381 | 0.1630 | 0.1935 | 0.5208 |
| BrownianReLU (α=0.480\alpha=0.480) | 0.7624 | 0.1667 | 0.0435 | 0.0690 | 0.5118 |
| BrownianReLU (α=0.925\alpha=0.925) | 0.6667 | 0.2153 | 0.2446 | 0.2290 | 0.5148 |
| BrownianReLU (α=0.944\alpha=0.944) | 0.7802 | 0.1923 | 0.0272 | 0.0476 | 0.5236 |
| ReLU | 0.7030 | 0.2278 | 0.1957 | 0.2105 | 0.5218 |
| LeakyReLU | 0.6634 | 0.2010 | 0.2228 | 0.2113 | 0.5150 |
| PReLU | 0.7767 | 0.2683 | 0.0598 | 0.0978 | 0.5297 |
| tanh | 0.7305 | 0.1919 | 0.1033 | 0.1343 | 0.5222 |
| GELU | 0.6447 | 0.2043 | 0.2609 | 0.2291 | 0.5113 |

Table [6](https://arxiv.org/html/2601.16446v1#S3.T6 "Table 6 ‣ 3.5 Classification Performance Analysis ‣ 3 Numerical Results ‣ Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network") summarizes the classification results obtained across all activation functions. The models achieved moderate predictive performance, with ROC-AUC values ranging approximately between 0.500.50 and 0.530.53, indicating classification performance marginally better than random guessing. Among the BrownianReLU variants, performance varied with the choice of the parameter α\alpha. While BrownianReLU with α=0.944\alpha=0.944 achieves the highest accuracy (0.7802)(0.7802), it exhibits extremely low recall (0.0272)(0.0272) and F1-score (0.0476)(0.0476), suggesting strong bias toward the majority class. Howevr, BrownianReLU with α=0.925\alpha=0.925 provides a more balanced trade-off, achieving a recall of 0.24460.2446, an F1-score of 0.22900.2290, and a ROC–AUC of 0.51480.5148.Standard activation functions show mixed performance. ReLU demonstrates reasonable accuracy but limited recall. LeakyReLU improves sensitivity to minority-class observations, reflected in higher recall and F1-score. PReLU achieves relatively high precision but suffers from low recall. The tanh activation offers a balanced compromise between precision and recall, while GELU achieves the highest recall (0.2609)(0.2609) and F1-score (0.2291)(0.2291) among all standard activations, indicating superior capability in capturing nonlinear relationships in the data.

#### 3.5.1 Interpretation and Implications

The results highlight that higher accuracy does not necessarily imply better classification performance in imbalanced datasets. Activation functions that improve recall and F1-score, such as GELU and well-tuned BrownianReLU variants, are more suitable for credit risk and loan default prediction tasks, where identifying high-risk cases is of greater importance than overall accuracy. Although none of the activation functions yields a substantial improvement in ROC–AUC, the choice of activation significantly affects the balance between accuracy and sensitivity. GELU and selected BrownianReLU configurations provide the most practically meaningful results.

## 4 Conclusion

This study examined the effectiveness of the proposed BrownianReLU activation function within LSTM frameworks for financial time series forecasting and classification, addressing the limitations of conventional activations in modeling noisy and volatile data. Based on normalized and sequenced datasets from Apple, GCB, and the S&P 500, the performance of BrownianReLU was evaluated against ReLU, LeakyReLU, PReLU, and Tanh using Mean Squared Error (MSE), coefficient of determination (R2R^{2}), and epochs to convergence as key metrics.
The results consistently showed that BrownianReLU achieved lower MSE and higher R2R^{2} values across testing datasets, indicating improved forecasting accuracy and stronger generalization. The learnable parameter α\alpha allows dynamic adaptation during training, addressing the dying neuron problem and reducing overfitting through controlled randomness. Visual analyses further confirmed smoother learning curves and enhanced trend-capturing ability. Under classification, although none of the activation functions yielded a substantial improvement in ROC–AUC, the choice of activation significantly affects the balance between accuracy and sensitivity. GELU and selected BrownianReLU configurations provide the most practically meaningful results. The findings demonstrate that BrownianReLU provides a robust and efficient activation mechanism for financial forecasting tasks and classification.

## Acknowledgements

This research has been supported in part by the Faculty of Science at Toronto Metropolitan University.

## References

* Arai and Imamura [2018]

  Hiroko Arai and Hiroshi Imamura.
  Spin-wave coupled spin torque oscillators for artificial neural
  network.
  *Journal of Applied Physics*, 124(15), 2018.
* Clevert [2015]

  Djork-Arné Clevert.
  Fast and accurate deep network learning by exponential linear units
  (elus).
  *arXiv preprint arXiv:1511.07289*, 2015.
* Dubey et al. [2022]

  Shiv Ram Dubey, Satish Kumar Singh, and Bidyut Baran Chaudhuri.
  Activation functions in deep learning: A comprehensive survey and
  benchmark.
  *Neurocomputing*, 503:92–108, 2022.
* Dugas et al. [2000]

  Charles Dugas, Yoshua Bengio, François Bélisle, Claude Nadeau, and
  René Garcia.
  Incorporating second-order functional knowledge for better option
  pricing.
  *Advances in neural information processing systems*, 13, 2000.
* Goodfellow et al. [2016]

  Ian Goodfellow, Yoshua Bengio, Aaron Courville, and Yoshua Bengio.
  *Deep learning*, volume 1.
  MIT press Cambridge, 2016.
* Gulcehre et al. [2016]

  Caglar Gulcehre, Marcin Moczulski, Misha Denil, and Yoshua Bengio.
  Noisy activation functions.
  In *International conference on machine learning*, pages
  3059–3068. PMLR, 2016.
* Hammad [2024]

  MM Hammad.
  Deep learning activation functions: Fixed-shape, parametric,
  adaptive, stochastic, miscellaneous, non-standard, ensemble.
  *arXiv preprint arXiv:2407.11090*, 2024.
* He et al. [2015]

  Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
  Delving deep into rectifiers: Surpassing human-level performance on
  imagenet classification.
  In *Proceedings of the IEEE international conference on computer
  vision*, pages 1026–1034, 2015.
* Hendrycks and Gimpel [2016]

  Dan Hendrycks and Kevin Gimpel.
  Gaussian error linear units (gelus).
  *arXiv preprint arXiv:1606.08415*, 2016.
* Hochreiter [1997]

  S Hochreiter.
  Long short-term memory.
  *Neural Computation MIT-Press*, 1997.
* Jiang et al. [2018]

  Xiaoheng Jiang, Yanwei Pang, Xuelong Li, Jing Pan, and Yinghong Xie.
  Deep neural networks with elastic rectified linear units for object
  recognition.
  *Neurocomputing*, 275:1132–1139, 2018.
* Kalman and Kwasny [1992]

  Barry L Kalman and Stan C Kwasny.
  Why tanh: choosing a sigmoidal function.
  In *[Proceedings 1992] IJCNN International Joint Conference on
  Neural Networks*, volume 4, pages 578–581. IEEE, 1992.
* Karatzas and Shreve [2014]

  Ioannis Karatzas and Steven Shreve.
  *Brownian motion and stochastic calculus*, volume 113.
  springer, 2014.
* Kaytan et al. [2022]

  Mustafa Kaytan, İbrahim Berkan Aydilek, Celaleddin Yeroğlu, and Ali
  Karci.
  Sigmoid-gumbel: Yeni bir hibrit aktivasyon fonksiyonu.
  *Bitlis Eren Üniversitesi Fen Bilimleri Dergisi*,
  11(1):29–45, 2022.
* Koçak and Şiray [2021]

  Yılmaz Koçak and Gülesen Üstündağ Şiray.
  New activation functions for single layer feedforward neural network.
  *Expert Systems with Applications*, 164:113977, 2021.
* Krizhevsky et al. [2012]

  Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton.
  Imagenet classification with deep convolutional neural networks.
  *Advances in neural information processing systems*, 25, 2012.
* Kunc and Kléma [2024]

  Vladimír Kunc and Jiří Kléma.
  Three decades of activations: A comprehensive survey of 400
  activation functions for neural networks.
  *arXiv preprint arXiv:2402.09092*, 2024.
* LeCun et al. [1998]

  Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner.
  Gradient-based learning applied to document recognition.
  *Proceedings of the IEEE*, 86(11):2278–2324, 1998.
* Li and Zhou [2020]

  Dandan Li and Yuan Zhou.
  Soft-root-sign: A new bounded neural activation function.
  In *Pattern Recognition and Computer Vision: Third Chinese
  Conference, PRCV 2020, Nanjing, China, October 16–18, 2020, Proceedings,
  Part III 3*, pages 310–319. Springer, 2020.
* Liew et al. [2016]

  Shan Sung Liew, Mohamed Khalil-Hani, and Rabia Bakhteri.
  Bounded activation functions for enhanced training stability of deep
  neural networks on visual pattern recognition problems.
  *Neurocomputing*, 216:718–734, 2016.
* Maas et al. [2013]

  Andrew L Maas, Awni Y Hannun, Andrew Y Ng, et al.
  Rectifier nonlinearities improve neural network acoustic models.
  In *Proc. icml*, volume 30, page 3. Atlanta, GA, 2013.
* Misra [2019]

  Diganta Misra.
  Mish: A self regularized non-monotonic activation function.
  *arXiv preprint arXiv:1908.08681*, 2019.
* Nair and Hinton [2010]

  Vinod Nair and Geoffrey E Hinton.
  Rectified linear units improve restricted boltzmann machines.
  In *Proceedings of the 27th international conference on machine
  learning (ICML-10)*, pages 807–814, 2010.
* Raj and Kos [2023]

  Ravi Raj and Andrzej Kos.
  An improved human activity recognition technique based on
  convolutional neural network.
  *Scientific Reports*, 13(1):22581, 2023.
* Ramachandran et al. [2017]

  Prajit Ramachandran, Barret Zoph, and Quoc V Le.
  Searching for activation functions.
  *arXiv preprint arXiv:1710.05941*, 2017.
* Roy et al. [2022]

  Swalpa Kumar Roy, Suvojit Manna, Shiv Ram Dubey, and Bidyut Baran Chaudhuri.
  Lisht: Non-parametric linearly scaled hyperbolic tangent activation
  function for neural networks.
  In *International Conference On Computer Vision And Image
  Processing*, pages 462–476. Springer, 2022.
* Vergara Villegas [2020]

  Osslan Osiris Vergara Villegas.
  Study of the effect of combining activation functions in a
  convolutional neural network.
  *Instituto de Ingeniería y Tecnología*, 2020.
* Xu [2015]

  Bing Xu.
  Empirical evaluation of rectified activations in convolutional
  network.
  *arXiv preprint arXiv:1505.00853*, 2015.
* Xu et al. [2016]

  Bing Xu, Ruitong Huang, and Mu Li.
  Revise saturated activation functions.
  *arXiv preprint arXiv:1602.05980*, 2016.