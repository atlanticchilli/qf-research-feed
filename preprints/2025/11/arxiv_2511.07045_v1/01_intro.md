---
authors:
- John Armstrong
- Cristin Buescu
- James Dalby
- Rohan Hobbs
doc_id: arxiv:2511.07045v1
family_id: arxiv:2511.07045
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Machine-learning a family of solutions to an optimal pension investment problem
url_abs: http://arxiv.org/abs/2511.07045v1
url_html: https://arxiv.org/html/2511.07045v1
venue: arXiv q-fin
version: 1
year: 2025
---


John Armstrong, Cristin Buescu, James Dalby, Rohan Hobbs

###### Abstract

We use a neural network to identify the optimal solution
to a family of optimal investment problems, where the parameters determining
an investor’s risk and consumption preferences are given as inputs to the neural network in addition to economic variables. This is used to develop a practical tool that can be used to explore how pension outcomes vary with preference parameters. We use a Black-Scholes economic model so that we may validate the accuracy of network using a classical and provably convergent numerical method
developed using the duality approach.

## Introduction

The von Neumann–Morgenstern utility theorem implies that, under mild assumptions, an individual’s preferences at a single time can be represented by an expected utility [[31](https://arxiv.org/html/2511.07045v1#bib.bib31)].
Nevertheless, even if one accepts that utility functions provide the best available tool to model preferences, it remains difficult to identify an
individual’s preferences and this is a recurring criticism in the literature [[1](https://arxiv.org/html/2511.07045v1#bib.bib1), [28](https://arxiv.org/html/2511.07045v1#bib.bib28), [30](https://arxiv.org/html/2511.07045v1#bib.bib30)].
When considering an investor’s preferences over
time, the space of possible preferences is still larger. We
seek to provide a practical tool to assist
in identifying a reasonable approximation to an investor’s preferences
for the purpose of pension investment.

A standard practical approach taken when providing guidance on Defined Contribution (DC) investments is to
give a
questionnaire to identify risk preferences [[11](https://arxiv.org/html/2511.07045v1#bib.bib11)].
A pension professional designing products
can provide a menu of options to potential
customers and use tools such as a risk questionnaire to
advise them on the best selection from this menu. It
is in developing this menu of options that utility functions
can provide a useful framework. They allow preferences
to be operationalised mathematically and then used
to identify coherent investment strategies. Designs that are not based
on optimization may even prove to be stochastically dominated by other strategies
and this is clearly undesirable.

Our goal in this paper
is to write a tool a pension professional might use in order
to identify good candidate gain functions. It allows the pensions professional to
vary the parameters within a family of utility functions and quickly view the resulting outcomes. They can then
use their professional expertise to perform the
subjective task of matching these outcomes to investors.
Utility-function inference from behaviour has been studied mathematically [[13](https://arxiv.org/html/2511.07045v1#bib.bib13), [14](https://arxiv.org/html/2511.07045v1#bib.bib14)], but we do not seek to do anything more sophisticated than
inferring utility-functions by selecting from a menu of options.

To produce an appropriate set of choices we first need a sufficiently rich family of gain functions to capture the key differences between different types of investor while remaining easy to interpret. We require gain functions that capture preferences for consumption over time, while allowing individuals to distinguish between their risk-aversion and the diminishing marginal utility of consumption at any given point in time (which we call satiation). This distinction is necessary to resolve many asset pricing puzzles [[8](https://arxiv.org/html/2511.07045v1#bib.bib8), [7](https://arxiv.org/html/2511.07045v1#bib.bib7), [9](https://arxiv.org/html/2511.07045v1#bib.bib9)]. Epstein–Zin preferences, exhibit these features and offer analytically tractable solutions that can often be analysed with full rigour [[18](https://arxiv.org/html/2511.07045v1#bib.bib18), [17](https://arxiv.org/html/2511.07045v1#bib.bib17), [21](https://arxiv.org/html/2511.07045v1#bib.bib21)]. However, the positive homogeneity of such utility functions can produce some unrealistic solutions [[6](https://arxiv.org/html/2511.07045v1#bib.bib6)]. This motivates us to sacrifice analyticity and use a preference model given by Exponential Kihlstrom–Mirman preferences (also used in this context in [[4](https://arxiv.org/html/2511.07045v1#bib.bib4)]). Although general Kihlstrom–Mirman preferences
are not time consistent in the sense of [[22](https://arxiv.org/html/2511.07045v1#bib.bib22)] the exponential case without discounting that we are using is time consistent. This can be used
to provide a justification for restricting attention to
preferences of this form [[12](https://arxiv.org/html/2511.07045v1#bib.bib12)].

The specific problem we solve is optimal investment with
idiosyncratic risk insured using a tontine structure. There is extensive literature on tontines, see [[25](https://arxiv.org/html/2511.07045v1#bib.bib25)] for an extensive review of both the history of tontines and more recent literature. Other works of note would be: [[26](https://arxiv.org/html/2511.07045v1#bib.bib26)] who look at optimal investment with a bond-only tontine or [[10](https://arxiv.org/html/2511.07045v1#bib.bib10)] who study a pooled annuity fund that utilizes the tontine mechanism. Although tontines have been studied heavily, the literature on the optimal control approach to making best use of a tontine is surprisingly limited. The problem is solved for power utility in [[29](https://arxiv.org/html/2511.07045v1#bib.bib29)]
for Epstein–Zin utility and with systematic longevity risk in [[2](https://arxiv.org/html/2511.07045v1#bib.bib2)].

We will identify the optimal investment and consumption strategies by using a machine-learning approach. The central
task of solving optimal control problems by machine learning is well studie, see for example [[20](https://arxiv.org/html/2511.07045v1#bib.bib20), [15](https://arxiv.org/html/2511.07045v1#bib.bib15)] and [[19](https://arxiv.org/html/2511.07045v1#bib.bib19)] for a recent survey of this fast-moving field.
We have consciously chosen the most direct approach
of a forward method because we believe this will be the simplest for industry
to understand and adapt to their needs without complex mathematics. Backward methods may be more efficient and scale better for higher-dimensional problems.

The preference model used in this paper is studied in [[5](https://arxiv.org/html/2511.07045v1#bib.bib5)] also using
machine-learning methods, but under the assumption that the parameters of the utility function were fixed. The
contribution of this paper is to extend this by solving for multiple utility functions simultaneously. Learning optimal controls across a range of objective function parameters has been done before [[23](https://arxiv.org/html/2511.07045v1#bib.bib23)], but is more challenging for us because of scaling issues with our utility function. We resolve this by using additional neural networks to scale the utility function given the preference parameters. This is the central contribution of our paper.

We have chosen to perform the optimization using a simple Black–Scholes model
to focus attention on the issue of the parameterization of the utility function.
This has the additional advantage that we can solve the optimal investment problem using
alternative numerical methods and so validate the success of our approach.
The second contribution of our paper is
to validate the numerical method for our preference model using a provably convergent scheme that exploits duality.

## 1 Discrete-time investment problem

We consider an optimal investment and consumption problem set within a Black-Scholes framework. The dynamics of the risky asset price, denoted SS, follow a geometric Brownian motion described by

|  |  |  |
| --- | --- | --- |
|  | d​St=μ​St​d​t+σ​St​d​Wt,\mathrm{d}S\_{t}=\mu S\_{t}\mathrm{d}t+\sigma S\_{t}\,\mathrm{d}W\_{t}, |  |

where μ∈ℝ\mu\in\mathbb{R} represents the drift, σ∈ℝ+\sigma\in\mathbb{R}\_{+} the volatility and WW a standard Brownian motion. Investment and consumption decisions are assumed to be made at discrete intervals, defined by the set 𝒯:={0,δ​t,2​δ​t,…,T}{\cal T}:=\{0,\delta t,2\delta t,\ldots,T\} for some time-step δ​t\delta t and final time TT. Between these times, investments are made following a fixed-weight strategy. Let πt\pi\_{t} be the proportion of wealth allocated to the risky asset at time t∈𝒯t\in{\cal T}. This proprtion is maintained throughout the interval [t,t+δ​t)[t,t+\delta t) with the remainder of the portfolio allocated to a risk-free asset, growing at a constant rate rr. The wealth evolves according to the stochastic differential equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ws=ws​(πt​μ+(1−πt)​r)​d​s+ws​πt​σ​d​Ws.\mathrm{d}w\_{s}=w\_{s}(\pi\_{t}\mu+(1-\pi\_{t})r)\mathrm{d}s+w\_{s}\pi\_{t}\sigma\,\mathrm{d}W\_{s}. |  | (1) |

on the interval [wt,wt+δ​t)[w\_{t},w\_{t+\delta t}). We denote the limit from the left of wealth at the end of the period by w(t+δ​t)−w\_{(t+\delta t)-}.
Applying Itô’s lemma gives the log wealth process

|  |  |  |
| --- | --- | --- |
|  | d​(log⁡(ws))=(πt​μ+(1−πt)​r−12​(πt​σ)2)​d​s+πt​σ​d​Ws.\mathrm{d}(\log(w\_{s}))=\left(\pi\_{t}\mu+(1-\pi\_{t})r-\frac{1}{2}(\pi\_{t}\sigma)^{2}\right)\mathrm{d}s+\pi\_{t}\sigma\mathrm{d}W\_{s}. |  |

This yields the expression

|  |  |  |
| --- | --- | --- |
|  | log⁡(w(t+δ​t)−)−log⁡(wt)=(πt​μ+(1−πt)​r−12​(πt​σ)2)​δ​t+πt​σ​(Wt+δ​t−Wt).\log(w\_{(t+\delta t)-})-\log(w\_{t})=\left(\pi\_{t}\mu+(1-\pi\_{t})r-\frac{1}{2}(\pi\_{t}\sigma)^{2}\right)\delta t+\pi\_{t}\sigma(W\_{t+\delta t}-W\_{t}). |  |

For simplicity and simulation, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵt:=Wt+δ​t−Wtδ​t,\epsilon\_{t}:=\frac{W\_{t+\delta t}-W\_{t}}{\sqrt{\delta t}}, |  | (2) |

so ϵt\epsilon\_{t} is distributed according to standard normal. Thus we are able to simulate the log wealth process using the Gaussian increments ϵt\epsilon\_{t}, and this log simulation, combined with the fixed-weight strategies, automatically ensures that strategies that put one into debt are removed.

To obtain wtw\_{t} from wt−w\_{t-}, we incorporate contributions, consumption and longevity payments via the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt=η​st​𝟙t<tRA+(1−ct​𝟙t≥tRA)​(1+P∞,t​𝟙t>tRA)​wt−,w\_{t}=\eta s\_{t}\mathbbm{1}\_{t<t\_{\mathrm{RA}}}+(1-c\_{t}\mathbbm{1}\_{t\geq t\_{\mathrm{RA}}})(1+P\_{\infty,t}\mathbbm{1}\_{t>t\_{\mathrm{RA}}})w\_{t-}, |  | (3) |

where the first term describes the fraction, η\eta, of an individuals salary, sts\_{t}, that is contributed before retirement (tRAt\_{\mathrm{RA}} is the time of retirement) and the second term removes the consumption, ct​wt−c\_{t}w\_{t-}, and adds on any longevity payment, P∞,t​wt−P\_{\infty,t}w\_{t-}, that one may receive in retirement. The longevity payment satisfies

|  |  |  |
| --- | --- | --- |
|  | P∞,t​wt−:=(pt1−pt)​wt−,P\_{\infty,t}w\_{t-}:=\left(\frac{p\_{t}}{1-p\_{t}}\right)w\_{t-}, |  |

where ptp\_{t} is the probability of dying in year tt, given you were alive in year t−1t-1. The infinity in the subscript is there to signify the size of the fund is infinite, and we use it to maintain notation with our other papers. The longevity payment can be achieved using a tontine structure, for a discussion of how this can be implemented in practice see [[5](https://arxiv.org/html/2511.07045v1#bib.bib5)].

The optimization procedure is based on a stylized gain function which
we call Exponential Khilstrom-Mirman utility [[5](https://arxiv.org/html/2511.07045v1#bib.bib5)]. Specifically, the agents seek to maximise

|  |  |  |
| --- | --- | --- |
|  | U​(C):=𝔼​(−exp​(−α​∑j=tRAj<τu​(Cj)​δ​t)),U(C):=\mathbb{E}\left(-\text{exp}\left(-\alpha\sum\_{j=t\_{\text{RA}}}^{j<\tau}u(C\_{j})\delta t\right)\right), |  |

where α>0\alpha>0 is a risk aversion parameter, τ\tau is the individual’s time of death and δ​t\delta t defines the time step between consumption decisions. The function u​(Ct,a)u(C\_{t},a) is given by

|  |  |  |
| --- | --- | --- |
|  | u​(Ct):=Ctρρ−aρρ,u(C\_{t}):=\frac{C\_{t}^{\rho}}{\rho}-\frac{a^{\rho}}{\rho}, |  |

where ρ\rho is a satiation parameter, aa is the adequacy level and CtC\_{t} defines the individual’s consumption amount (consumption proportion multiplied by current wealth) relative to their final salary at a time point tt. In order to compute the gain function, we assume that consumption and individual longevity risk are independent. We also assume there is no systematic longevity risk and that the probability an individual dies in a given year ss is given by p¯s\overline{p}\_{s}. So, we compute

|  |  |  |
| --- | --- | --- |
|  | U=−𝔼Invest​[∑s=tRATp¯s​exp​(−α​∑t=tRAsu​(Ct,a)​δ​t)].U=-\mathbb{E}\_{\mathrm{Invest}}\left[\sum\_{s=t\_{\mathrm{RA}}}^{T}\overline{p}\_{s}\,\text{exp}\left(-\alpha\sum\_{t=t\_{\mathrm{RA}}}^{s}u(C\_{t},a)\delta t\right)\right]. |  |

In this formula, 𝔼Invest{\mathbb{E}}\_{\mathrm{Invest}} denotes the expectation across investment scenarios
and so excludes the mortality component of our probability model, which is accounted for by the term p¯s{\overline{p}}\_{s}. TT is the maximum time of death, which is finite for the mortality model we are using. If we generate NN investment scenarios and label the consumption in each case c(j)c^{(j)} with 1≤j≤N1\leq j\leq N, we may estimate the gain function using

|  |  |  |
| --- | --- | --- |
|  | U^:=−1N​∑j=1N[∑s=tRATp¯s​exp​(−α​∑t=tRAsu​(Ct(j))​δ​t)].\hat{U}:=-\frac{1}{N}\sum\_{j=1}^{N}\left[\sum\_{s=t\_{\mathrm{RA}}}^{T}\overline{p}\_{s}\,\text{exp}\left(-\alpha\sum\_{t=t\_{\mathrm{RA}}}^{s}u(C\_{t}^{(j)})\delta t\right)\right]. |  |

## 2 Training the Fixed Parameter Network

Due to the inhomogeneous gain function, solving the optimization using classical techniques is reasonably computationally expensive (it takes several minutes for the decumulation-only problem with a single fixed set of parameter values), and will become infeasible if one uses richer economic models. It is also requires considerable programming if one changes economic model or loss function. For these reasons, we a neural network to solve the problem numerically. For this Black–Scholes model, we take the standard Gaussians ϵt\epsilon\_{t} in equation ([2](https://arxiv.org/html/2511.07045v1#S1.E2 "In 1 Discrete-time investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) as the input to the recurrent neural network that we train. Since we use a gated recurrent unit (GRU), we also include the time points. Note that we use years as time points in our simulation, so we set δ​t=1\delta t=1. While training and evaluating a fixed parameter network, the gain function parameters α\alpha, ρ\rho and aa remain fixed throughout, across scenarios. We have a visual representation of the network architecture in Figure [1](https://arxiv.org/html/2511.07045v1#S2.F1 "Figure 1 ‣ 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem").

![Refer to caption](varying_parameter_paper/RNN_for_varying_params_paper.drawio.png)

Figure 1: Architecture for the Recurrent Neural Network. The arrows are purely for demonstrative purposes and all the layers are dense. The label ‘FF’ denotes a feedforward layer.

The neural network outputs an investment strategy πtθ\pi\_{t}^{\theta} and a consumption strategy ctθc\_{t}^{\theta} (both as proportions) at each time step.
The superscript θ\theta indicates the dependence of this strategy on the neural network’s parameter values, and so
changes as the network is trained.
If the time tt is less than the time of retirement, then the consumption strategy is simply ignored. We take these strategies for the whole time period t∈[0,T]t\in[0,T], and compute our loss function. Since neural networks seek to minimize their loss function, we take the loss function to be the (logarithm of the) negative of the gain function. Sparing some detail and computations outlined in [[5](https://arxiv.org/html/2511.07045v1#bib.bib5)], we compute the loss function of the network to equal

|  |  |  |  |
| --- | --- | --- | --- |
|  | L=log⁡(∑s=1Nexp⁡(log⁡(∑t=tRATexp⁡(log⁡(p~t)−α​∑j=tRAtu​(Cj(s))​δ​t))))−log⁡(N),L=\log\left(\sum^{N}\_{s=1}\exp\left(\log\left(\sum\_{t=t\_{\text{RA}}}^{T}\exp\left(\log(\tilde{p}\_{t})-\alpha\sum^{t}\_{j=t\_{\text{RA}}}u(C\_{j}^{(s)})\delta t\right)\right)\right)\right)\\ -\log(N), |  | (4) |

where NN is the number of scenarios across which we average, TT is the maximum lifetime and p¯t\bar{p}\_{t} is the probability an individual dies in a given year tt after retirement. We compute this expression using the logsumexp function to reduce excessive rounding errors and ensure numerical stability.

As a reference point for the success of training, we plot a graph of the percentiles of the replacement ratio of an individual across many scenarios. The replacement ratio is defined to be the ratio of pension payments to index-linked final salary. Essentially, it shows the consumption of an individual, relative to their final salary and adjusted for by inflation. As such, it can be considered as a direct consequence of the consumption and investment strategies, and so it can be taken as a way of comparing and thus rating the strategies. For further details on replacement ratios, see [[5](https://arxiv.org/html/2511.07045v1#bib.bib5)], and for plots of the actual investment and consumption strategies see Appendix [B](https://arxiv.org/html/2511.07045v1#A2 "Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem").

We use the parameters in Table [1](https://arxiv.org/html/2511.07045v1#S2.T1 "Table 1 ‣ 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem"), which we will call the default parameters from hereafter, and the trained network produces strategies that lead to the outcomes in Figure [2](https://arxiv.org/html/2511.07045v1#S2.F2 "Figure 2 ‣ 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem").

| Parameters | Value |
| --- | --- |
| α\alpha | 5×10−55\times 10^{-5} |
| ρ\rho | -2 |
| aa | 0.4 |

Table 1: Default fixed-parameter values used to train the ‘fixed-parameter’ network.



![Refer to caption](varying_parameter_paper/fixed_parameter_plot.png)

Figure 2: Retirement outcome deciles for the ‘fixed-parameter’ trained neural network.

## 3 Verification of the optimal strategy

As a test of the validity of our network
we compare the results obtained using a provably
convergent classical algorithm.
In Appendix [C](https://arxiv.org/html/2511.07045v1#A3 "Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem") we use a duality
approach to derive a numerical algorithm for
solving the decumulation-only problem with discrete-time consumption
and continuous-time investment. As is well-known,
in complete markets it is easier to prove rigorous results for duality methods
than for primal methods. Proofs using primal approaches typically require restrictive
growth conditions or more delicate arguments. See [[16](https://arxiv.org/html/2511.07045v1#bib.bib16)] for
an explanation of the challenges of primal methods and a review of the literature. Our algorithm proceeds by using a duality method to solve the
problem when consumption is restricted to one-period. We then solve the discrete-time consumption, continuous-time investment problem recursively.

We considered a solution to have achieved reasonable accuracy for investment purposes if the value of the expected utility is within 1% of the standard error of the utility. In Figure [3](https://arxiv.org/html/2511.07045v1#S3.F3 "Figure 3 ‣ 3 Verification of the optimal strategy ‣ Machine-learning a family of solutions to an optimal pension investment problem") we plot the outcome from our neural
network against a solution of the decumulation only
problem obtained using the method of [C](https://arxiv.org/html/2511.07045v1#A3 "Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"). Not only are the plots similar, but the neural network is within 1% of the utility with its predictions. It does this across various different
tested gain function parameters.
The neural network is, of course, able to compute the result much faster. The classical method takes several minutes
to run even though this is just a one-dimensional problem.

![Refer to caption](varying_parameter_paper/neural_network_decumulation_vs_convergent.png)

Figure 3: Comparison of retirement outcomes for the neural network approach compared to the provably convergent method in a decumulation only setting.

We were also able to validate our approach for the decumulation problem with power-utility problem and discrete-time consumption and continuous-time investment using the analytic solution of [[2](https://arxiv.org/html/2511.07045v1#bib.bib2)], Theorem 2.2.

We have tested that the method is also capable of producing good strategies in richer economic models, but we will defer more detailed discussion to another paper.

## 4 Issues with a Naive Method of Training the Neural Network

We now proceed to training an RNN within the problem discussed in section [2](https://arxiv.org/html/2511.07045v1#S2 "2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem") across a range of gain function parameters, rather than for a fixed set. Note that the parameters that we will allow to vary are the risk aversion parameter, the satiation parameter and the adequacy level in the loss function in [4](https://arxiv.org/html/2511.07045v1#S2.E4 "In 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem").

A naive approach to learning optimal strategies for various parameter combinations would be to randomly sample values from an acceptable range for each parameter in each scenario and include them as inputs to the RNN. They would also therefore be used in the computation of the loss function. This would in theory allow the network to train on a varied set of gain functions, minimising the loss across all of them. However, the principal issue with this method arises from the loss function itself. Since we employ an exponential gain function, the loss values can vary significantly across differing parameter values. As a result, when averaging the loss function across scenarios, certain parameter combinations can dominate as they provide more extreme utility values with more extreme variance. This in turn leads to excessive focus on reducing the loss of these specific scenarios, which distorts training, preventing the network from learning an accurate solution across all parameter combinations.

We test the success of training using this naive method by comparing the trained RNN’s prediction for fixed parameter values against the results obtained when training the fixed-parameter RNN with the corresponding parameter values. The naive method performs so poorly that the expected utility from its strategy is practically incomparable to that of the fixed-parameter RNN across differing gain function parameters.

## 5 Two Alternative Architectures

We now introduce two alternative architectures that overcome the high-variance issues outlined in section [4](https://arxiv.org/html/2511.07045v1#S4 "4 Issues with a Naive Method of Training the Neural Network ‣ Machine-learning a family of solutions to an optimal pension investment problem"), and learn optimal strategies effectively across a wide range of parameter values. These approaches both use separate neural networks to modify the loss function of the main RNN, such that the loss value for each scenario is scaled for the given parameter combination. In this sense, the variance of the loss function is normalized, allowing the main RNN to train effectively across the entire parameter space. Note that from here onward the ‘main’ RNN is the network learning the optimal investment and consumption strategies and the architecture is the same as in Figure [1](https://arxiv.org/html/2511.07045v1#S2.F1 "Figure 1 ‣ 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem"), except that the input dimension is increased by one in order to accommodate the parameters as inputs.

The problem we need to address is that the appropriate scale for the problem depends on the parameter values. The two methods we introduce here differ in how these scaling factors are produced.

We also considered the possibility of scaling
the networks by computing a certainty-equivalent value for
our loss functions to ensure the value is comparable across
different parameter ranges. However, the computation of
a certainty-equivalent is not analytically tractable for our gain function and numerical root-finding methods come with their own challenges when the scale of the problem is unknown. As a result we felt that designing an algorithm using this approach would be more complex than scaling based on the observed mean and variance and was likely to be less effective.

### 5.1 A Two-Step Iterative Algorithm

In this method, we use a two-step iterative algorithm that makes use of a secondary neural network, called the ‘scaling’ network, to estimate the scaling factors. In short, the main RNN is trained to minimize a scaled loss function using the current estimates from the scaling network. Once trained, this RNN is then used to generate data under the unscaled loss, which is used to update the scaling network. This iterative, alternating procedure allows the two networks to improve each other: the scaling network enables more stable and effective training of the RNN, while the improved RNN provides better data for refining the scaling estimates.

We will use an index i=0,1,2,…i=0,1,2,\ldots as our iteration counter. At each iteration, we will assume that we have the function σi:𝒫i→ℝ\sigma\_{i}:{\mathcal{P}\_{i}}\to{\mathbb{R}} which estimates the standard deviation of the utility function, conditioned on the parameter values p∈𝒫ip\in{\mathcal{P}\_{i}}. Here, pp denotes the triplet (α,ρ,a\alpha,\rho,a). To initialize the algorithm we define

|  |  |  |
| --- | --- | --- |
|  | σ0​(p)=1.\sigma\_{0}(p)=1. |  |

The first step in each iteration is to train an RNN to learn an approximate optimal investment and consumption strategy

|  |  |  |
| --- | --- | --- |
|  | fi:(𝒫i)N×(ℐ)N→(𝒪)N.f\_{i}:({\mathcal{P}\_{i}})^{N}\times({\cal I})^{N}\to({\cal O})^{N}. |  |

Define the log utility for each scenario, conditional on a given parameter set pp, as

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(p,s)=log⁡(∑t=0Texp⁡(log⁡(p~t)−α​∑j=0tup​(cj(s))​δ​t)).v(p,s)=\log\left(\sum\_{t=0}^{T}\exp\left(\log(\tilde{p}\_{t})-\alpha\sum^{t}\_{j=0}u\_{p}(c\_{j}^{(s)})\delta t\right)\right). |  | (5) |

The subscript pp in upu\_{p} highlights the dependency of the uu on the parameter set.
The RNN learns the strategy fif\_{i} by minimizing the following scaled loss function:

|  |  |  |
| --- | --- | --- |
|  | ℓi​(p,σi​(p))=log⁡(∑s=1Nexp⁡(v​(p,s))σi​(p))−log⁡(N).\ell\_{i}(p,\sigma\_{i}(p))=\log\left(\sum\_{s=1}^{N}\frac{\exp\left(v(p,s)\right)}{\sigma\_{i}(p)}\right)-\log(N). |  |

We compute this using the log-sum-exp function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓi​(p,σi​(p))=log⁡(∑s=1Nexp⁡[v​(p,s)−log⁡(σi​(p))])−log⁡(N).\ell\_{i}(p,\sigma\_{i}(p))=\log\left(\sum\_{s=1}^{N}\exp\left[v(p,s)-\log\left(\sigma\_{i}(p)\right)\right]\right)-\log(N). |  | (6) |

Again, we do this to reduce excessive rounding errors when computing the average across scenarios.

Next, we train a separate neural network, the ‘scaling network’, to estimate the standard deviation of the utility function conditional on the parameters. That is, exp⁡(v​(p,s))\exp(v(p,s)), evaluated using the strategy fif\_{i} and conditioned on the parameter values p∈𝒫i+1p\in\mathcal{P}\_{i+1}. This network, trained using supervised learning, learns the mapping σi+1​(p):𝒫i+1→ℝ+\sigma\_{i+1}(p):\mathcal{P}\_{i+1}\to\mathbb{R}\_{+}. The training dataset consists of 50,00050,000 samples of parameter combinations along with the corresponding empirical standard deviations of the loss function (computed using the current strategy fif\_{i}). The parameters are the inputs and the standard deviations are the labels. If 𝒫i+1\mathcal{P}\_{i+1} is a richer set of parameters than 𝒫i\mathcal{P}\_{i}, then the strategy fif\_{i} essentially extrapolates its learned function across the whole parameter set.

Once this training is complete, we have the new scaling network and thus the new scaling factors, and so we increment the iteration counter and repeat the process using the updated estimates of σi+1​(p)\sigma\_{i+1}(p).

In practice, we found that only three full iterations of this process were necessary to solve our problem with sufficient accuracy. The final RNN, using the strategy f3f\_{3} from the fourth iteration, was used as our end result. In each of the iterations, we increased the size of the parameter space such that 𝒫3⊃𝒫2⊃𝒫1\mathcal{P}\_{3}\supset\mathcal{P}\_{2}\supset\mathcal{P}\_{1} (=𝒫0=\mathcal{P}\_{0}), and full details can be found in Appendix [A](https://arxiv.org/html/2511.07045v1#A1 "Appendix A Neural Network Architecture Details ‣ Machine-learning a family of solutions to an optimal pension investment problem"). As such, when producing the loss function data needed to train the scaling network for the next iteration, the trained RNN simply extrapolated its predictions from the smaller space 𝒫i−1\mathcal{P}\_{i-1} to the full range 𝒫i\mathcal{P}\_{i}.

Figure [4a](https://arxiv.org/html/2511.07045v1#S5.F4.sf1 "In Figure 4 ‣ 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem") illustrates the impact of this alternative architecture on training outcomes. Once again, we used the parameters in Table [1](https://arxiv.org/html/2511.07045v1#S2.T1 "Table 1 ‣ 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem") as input to the trained network.

![Refer to caption](varying_parameter_paper/comaprison_varying_with_fixed_plot.png)


a

![Refer to caption](varying_parameter_paper/comparison_simulatenous_scaling_with_fixed.png)


b

Figure 4: Panel ([4a](https://arxiv.org/html/2511.07045v1#S5.F4.sf1 "In Figure 4 ‣ 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows retirement outcomes for the RNN produced by the ‘two-step iterative method as compared to the fixed parameter network. Panel ([4b](https://arxiv.org/html/2511.07045v1#S5.F4.sf2 "In Figure 4 ‣ 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the same comparison but between the RNN from the ‘one-step’ algorithm and the fixed parameter network.

Figure [4a](https://arxiv.org/html/2511.07045v1#S5.F4.sf1 "In Figure 4 ‣ 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem") demonstrates the improved ability of the network to generalize across a wide range of parameters. The similarities between this new method’s strategies and the fixed parameter RNN’s strategies are corroborated by Figure [11](https://arxiv.org/html/2511.07045v1#A2.F11 "Figure 11 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem") in the Appendix. Notably, the differences in strategy are largest in the later years, where survival probabilities are minimal, and hence the contribution to the loss function is negligible. Furthermore, the expected utility obtained by the varying-parameter network is within 1% of a standard error of the value obtained by the fixed-parameter network for this default set of parameters. Since training a number of fixed parameter networks would be time consuming, we only tested on two other parameter combinations, the edge cases, where the optimal solutions differ the most. Specifically, these cases are described by an individual who is more easily satiated and highly risk averse111(α,ρ,a)=(0.2,−2,0.4)(\alpha,\rho,a)=(0.2,-2,0.4), or an individual who is less easily satiated and is almost risk neutral222(α,ρ,a)=(5×10−5,−0.1,0.4)(\alpha,\rho,a)=(5\times 10^{-5},-0.1,0.4). The varying-parameter network was also within 1% under these parameters.

### 5.2 A One-Step Algorithm

The second method we introduce also leverages multiple neural networks to scale the loss function, but, unlike the two-step iterative approach, the networks are trained simultaneously, side-by-side. This allows the main RNN to learn the optimal strategy across the entire range of parameter values far more efficiently.

Again, the main difficulty here is estimating the standard deviation of the loss function for a given set of parameter values, to obtain the appropriate scaling for the loss function. To address this, we introduce two auxiliary networks. The first network, the ‘mean-estimating network’, estimates the expectation of the main loss function conditional on parameter values and the strategy produced by the main RNN. The second, the ‘scaling network’, predicts the conditional variance of the loss, using the error from the mean estimate as input to its loss function. We then use this scaling factor exactly as before in ([6](https://arxiv.org/html/2511.07045v1#S5.E6 "In 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem")) to scale the main RNN’s loss.

The mean network is trained by minimizing the average squared difference between the utility from each scenario and its predicted mean, μθ​(p)\mu\_{\theta}(p). The scaling network is then trained to predict the variance by minimizing the squared difference between these squared errors and its output, σθ2​(p)\sigma^{2}\_{\theta}(p). For numerical stability, we again use logarithms, taking the outputs of both networks as the logarithms of the mean and variance. We therefore obtain the following loss functions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lμ​(p)\displaystyle L\_{\mu}(p) | =log⁡(∑s=1Nexp⁡(log⁡((exp⁡(v​(p,s))−exp⁡(log⁡(μθ​(p))))2)⏟ds2​ (log squared differences)))−log⁡(N),\displaystyle=\log\Bigg(\sum\_{s=1}^{N}\exp\bigg(\underbrace{\log\bigg(\big(\exp(v(p,s))-\exp(\log(\mu\_{\theta}(p)))\big)^{2}\bigg)}\_{d\_{s}^{2}\text{ (log squared differences)}}\bigg)\Bigg)-\log(N), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡(1N​∑s=1N(exp⁡(v​(p,s))−μθ​(p))2),\displaystyle=\log\Bigg(\frac{1}{N}\sum\_{s=1}^{N}\big(\exp(v(p,s))-\mu\_{\theta}(p)\big)^{2}\Bigg), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lσ​(p)\displaystyle L\_{\sigma}(p) | =log⁡(∑s=1Nexp⁡(log⁡((exp⁡(ds2)−exp⁡(log⁡(σθ2​(p))))2)))−log⁡(N),\displaystyle=\log\Bigg(\sum\_{s=1}^{N}\exp\bigg(\log\bigg(\big(\exp(d\_{s}^{2})-\exp(\log(\sigma\_{\theta}^{2}(p)))\big)^{2}\bigg)\bigg)\Bigg)-\log(N), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡(1N​∑s=1N(exp⁡(ds2)−σθ2​(p))2),\displaystyle=\log\Bigg(\frac{1}{N}\sum\_{s=1}^{N}\big(\exp(d\_{s}^{2})-\sigma^{2}\_{\theta}(p)\big)^{2}\Bigg), |  |

where v​(p,s)v(p,s) is defined in ([5](https://arxiv.org/html/2511.07045v1#S5.E5 "In 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem")). For
numerical stability, the squared differences are computed using the identity

|  |  |  |
| --- | --- | --- |
|  | log⁡((ea−eb)2)=2​[max⁡(a,b)+log1​p⁡(−emin⁡(a,b)−max⁡(a,b))]\log\left((e^{a}-e^{b})^{2}\right)=2\left[\,\max(a,b)+\log\_{1\text{p}}\bigl(-e^{\min(a,b)-\max(a,b)}\bigr)\right] |  |

where log1​p⁡(x):=log⁡(1+x)\log\_{1\text{p}}(x):=\log(1+x).

The training procedure jointly optimizes all three networks using the mean and scaling network losses defined above as well as the main RNN’s scaled loss, analogous to ([6](https://arxiv.org/html/2511.07045v1#S5.E6 "In 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem")). At each step of training (each gradient update), all three networks make a prediction given the dataset and parameters. The main RNN’s consumption and investment strategy, along with the scaling network output, log⁡(σθ2​(p))\log(\sigma\_{\theta}^{2}(p)), are used as input into the main RNN’s (scaled) loss function. The two auxiliary networks’ losses are computed using the (unscaled) log utilities from the main RNN, as per the loss functions Lμ​(p)L\_{\mu}(p) and Lσ​(p)L\_{\sigma}(p) respectively. Finally, all three networks’ parameters are updated using the corresponding gradients from their loss functions. The full training procedure is given in Algorithm [1](https://arxiv.org/html/2511.07045v1#alg1 "Algorithm 1 ‣ 5.2 A One-Step Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem"):

Algorithm 1  Joint Optimization Training Procedure

Initialize: dataset 𝒟\mathcal{D}, parameters 𝒫\mathcal{P}, network parameters θRNN,θμ,θσ\theta\_{\text{RNN}},\theta\_{\mu},\theta\_{\sigma}, number of epochs EE, and split 𝒟\mathcal{D} into batches BB

for epoch in range EE do

for batch in BB do

1. 1.

   Sample scenarios s∈𝒟s\in\mathcal{D} and parameters p∈𝒫p\in\mathcal{P} from the batch
2. 2.

   (πtθ,ctθ)t=1T←RNN​(s,p)(\pi\_{t}^{\theta},c\_{t}^{\theta})\_{t=1}^{T}\leftarrow\text{RNN}(s,p)
3. 3.

   log⁡(μθ​(p))←MeanNN​(p)\log(\mu\_{\theta}(p))\leftarrow\text{MeanNN}(p)
4. 4.

   log⁡(σθ2​(p))←ScalingNN​(p)\log(\sigma\_{\theta}^{2}(p))\leftarrow\text{ScalingNN}(p)
5. 5.

   Compute wealth process from (πtθ,ctθ)t=1T(\pi\_{t}^{\theta},c\_{t}^{\theta})\_{t=1}^{T} to get consumption amounts (Ct)t=tRAT(C\_{t})\_{t=t\_{\text{RA}}}^{T} in retirement.
6. 6.

   Input the consumption amounts and the scaling factor into the scaled RNN loss ℓ​(p,σθ​(p))\ell(p,\sigma\_{\theta}(p)), and store unscaled log utilities v​(p,s)v(p,s)
7. 7.

   Compute mean-estimating network loss Lμ​(p)L\_{\mu}(p) using stored v​(p,s)v(p,s) and store log squared differences ds2d^{2}\_{s}
8. 8.

   Compute scaling network loss Lσ​(p)L\_{\sigma}(p) using stored log squared differences ds2d^{2}\_{s}
9. 9.

   Update θRNN,θμ,θσ\theta\_{\text{RNN}},\theta\_{\mu},\theta\_{\sigma} using gradients

end for

end for

In this method, training is performed across the full parameter range, equivalent to 𝒫3\mathcal{P}\_{3}, removing the need for iterations through larger parameter sets to improve accuracy. This increases the efficiency of the algorithm, requiring at most a fifth of the runtime that the two-step iterative algorithm requires.

Figure [4b](https://arxiv.org/html/2511.07045v1#S5.F4.sf2 "In Figure 4 ‣ 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem") illustrates the success of the training procedure. We can also see the similarities in the consumption and investment strategies in Figure [12](https://arxiv.org/html/2511.07045v1#A2.F12 "Figure 12 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem"). This method produces a network that achieves a utility within 1% of a standard error of the fixed network for these default parameters. The network also achieves an expected utility of within 1% of a standard error of the fixed parameter network for the two edge cases described previously. Not only does this show the success of this architecture, but it also shows that it is at least as effective as the two-step iterative approach and is more efficient in reaching accurate solutions.

## 6 Allowing for Real-Time Comparisons

The primary objective of training this varying-parameter network was to enable real-time comparisons of retirement outcomes, allowing users to explore and select their preferred investment and consumption strategies.

Although the varying-parameter networks generate predictions over the full parameter range without requiring further training, it remains time-consuming to simulate sufficient stratetgy outcomes to produce a fan diagram of outcomes. To address this issue, we train an additional feed-forward neural network, referred to as the ‘replacement-ratio percentile’ network. This network approximates the mapping from percentile, input parameters, and time point to the corresponding replacement ratio, as predicted by the principal RNN. Specifically, let ℐ:={1,2,…,9}\mathcal{I}:=\{1,2,\ldots,9\} denote the set of percentiles. Then the replacement-ratio percentile network learns the mapping

|  |  |  |
| --- | --- | --- |
|  | g:𝒫×ℐ×𝒯→ℝ,g:\mathcal{P}\times\mathcal{I}\times\mathcal{T}\to\mathbb{R}, |  |

which returns the value of the ii-th percentile at time tt, corresponding to the replacement ratio produced by the optimal strategy obtained from the principal network. The training was performed in a supervised environment and the dataset was generated by randomly sampling 50,00050,000 combinations of parameters and passing them through the principal RNN to obtain the corresponding nine percentiles for each input. Each percentile contains 5656 time points to account for each year from retirement until the last time point an individual may still be alive. We can see in Figure [5](https://arxiv.org/html/2511.07045v1#S6.F5 "Figure 5 ‣ 6 Allowing for Real-Time Comparisons ‣ Machine-learning a family of solutions to an optimal pension investment problem") the accuracy of this network in mimicking the principal network.

![Refer to caption](varying_parameter_paper/graph_network_plot.png)

Figure 5: Retirement outcomes for the replacement-ratio percentile neural network compared to the main RNN.

The replacement-ratio percentile network produces an almost identical output to the principal RNN. The replacement-ratio percentile network is also able to produce the plot in approximately 1/3 of a second, more than 10 times faster than recalculating by Monte Carlo. This allowed us to create
a far more interactive and responsive user interface.

## 7 Sensitivity Analysis of Optimal Strategies

The ability to learn the optimal strategy across a range of parameter values allows us to perform sensitivity analysis with respect to the parameters. Unless otherwise stated, all parameters are kept constant as specified in Table [1](https://arxiv.org/html/2511.07045v1#S2.T1 "Table 1 ‣ 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem"). We will analyse the outcomes in retirement and the strategies themselves. The plots for outcomes will be included in this section, but the full plots of the strategies will be included in Appendix [B](https://arxiv.org/html/2511.07045v1#A2 "Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem").

We begin by examining how retirement outcomes vary with the risk-aversion parameter, α\alpha. Figures [6a](https://arxiv.org/html/2511.07045v1#S7.F6.sf1 "In Figure 6 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem") & [6b](https://arxiv.org/html/2511.07045v1#S7.F6.sf2 "In Figure 6 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem") below illustrate how the outcomes differ relative to this parameter. Note that the strategies we have been examining so far are already quite risky, so the low risk aversion strategies we look at now are not drastically different.

![Refer to caption](varying_parameter_paper/high_risk_aversion_plot.png)


a

![Refer to caption](varying_parameter_paper/low_risk_aversion_plot.png)


b

Figure 6: Comparison of retirement outcomes for different values of α\alpha. We have subfigure ([6a](https://arxiv.org/html/2511.07045v1#S7.F6.sf1 "In Figure 6 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with α=0.01\alpha=0.01 (high risk aversion) and subfigure ([6b](https://arxiv.org/html/2511.07045v1#S7.F6.sf2 "In Figure 6 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with α=10−7\alpha=10^{-7} (low risk aversion).

As expected, increasing the risk aversion parameter leads to more conservative investment behavior during the accumulation phase. Specifically, individuals with higher risk aversion allocate a lower proportion to the risky asset, resulting in narrower spreads between replacement-ratio percentiles. This conservative strategy typically yields lower replacement ratios at retirement but provides greater protection in adverse market scenarios. In terms of consumption strategies, less risk-averse individuals tend to consume more, reflecting a reduced concern for the depletion of their funds. On the contrary, the more risk averse individuals fear the prospect of running out of funds and so are less likely to consume as much in retirement.

We can also consider the affect the satiation parameter, ρ\rho, has on retirement outcomes. Figures [7a](https://arxiv.org/html/2511.07045v1#S7.F7.sf1 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem") & [7b](https://arxiv.org/html/2511.07045v1#S7.F7.sf2 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem") provide an illustration.

![Refer to caption](varying_parameter_paper/more_easily_satiated_plot.png)


a

![Refer to caption](varying_parameter_paper/less_easily_satiated_plot.png)


b

Figure 7: Comparison of retirement outcomes for different values of ρ\rho. We have Subfigure ([7a](https://arxiv.org/html/2511.07045v1#S7.F7.sf1 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with ρ=−2.0\rho=-2.0 (more easily satiated) and Subfigure ([7b](https://arxiv.org/html/2511.07045v1#S7.F7.sf2 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with ρ=−0.1\rho=-0.1 (less easily satiated).

Note that ρ=−2.0\rho=-2.0 is the default value for the parameter in the strategies we have looked at before. Again, the figures show that the outcomes follow an intuitive pattern. When ρ=−2.0\rho=-2.0, the individual becomes satiated much more quickly. As a result, an individual will reduce their investment in the risky asset during the accumulation period in comparison, as they do not seek such a high replacement ratio in retirement. This is what leads to the tighter percentiles that can be seen in Figure [7a](https://arxiv.org/html/2511.07045v1#S7.F7.sf1 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"), and by the opposite reasoning, why the looser percentiles can be seen in Figure [7b](https://arxiv.org/html/2511.07045v1#S7.F7.sf2 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"). Within the consumption strategy, ρ=−2.0\rho=-2.0 induces reduced overall consumption throughout retirement, since the individual is more satisfied with the amount they are consuming. In contrast, when ρ=−0.1\rho=-0.1, the individual remains far from satiated and therefore tends to seek to consume more throughout retirement.

The impact of the adequacy parameter is much harder to see than the other two parameters. To understand its effect, we examine the behaviour with extremely high risk aversion (α=0.2)(\alpha=0.2). Let VadequateV^{\text{adequate}} be the level of funds at retirement that allow an individual to to consume at the adequacy level for the whole of their retirement if they invest in risk-free bonds. If a highly risk-averse individual has more than VadequateV^{\text{adequate}} at retirement, their strategy will approximate consuming all funds above VadequateV^{\text{adequate}} in the first year and consume at the adequacy level thereafter. This is because this is the only risk-free strategy available. If they have less than VadequateV^{\text{adequate}} funds, the situation is reversed. An individual who is risk averse will choose to reduce consumption initially below the level they could sustain for the whole of retirement in order to reduce their risk levels later in retirement.
This is illustrated in
Figure [8](https://arxiv.org/html/2511.07045v1#S7.F8 "Figure 8 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"), where we deploy the provably convergent numerical scheme outlined in Section [3](https://arxiv.org/html/2511.07045v1#S3 "3 Verification of the optimal strategy ‣ Machine-learning a family of solutions to an optimal pension investment problem").

![Refer to caption](varying_parameter_paper/c++_high_risk_high_wealth_adequacy_plot.png)


a

![Refer to caption](varying_parameter_paper/c++_high_risk_low_wealth_adequacy_plot.png)


b

Figure 8: Comparison of retirement outcomes using the provably convergent numerical method from Section [3](https://arxiv.org/html/2511.07045v1#S3 "3 Verification of the optimal strategy ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for highly risk averse individuals in decumulation only. We have Subfigure ([8a](https://arxiv.org/html/2511.07045v1#S7.F8.sf1 "In Figure 8 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with high initial wealth and Subfigure ([8b](https://arxiv.org/html/2511.07045v1#S7.F8.sf2 "In Figure 8 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with low initial wealth.

This explains the importance of adequacy in the decumulation phase. If one considers accumulation, as we have done throughout this dissertation, a highly risk averse individual will invest almost entirely in the risk-free asset during accumulation. This results in an essentially deterministic level of income at retirement, and their consumption throughout retirement will again be determined by whether this is greater or less than VadequateV^{\text{adequate}}.

When we view the optimal strategies computed using machine learning, this pattern is somewhat obscured by the fact it is very difficult to train the network to find the optimal strategy over the age of about 100 as consumption after this age has only a negligible effect upon utility. The optimal strategies computed using machine learning for decumulation-only are shown in panels ([9a](https://arxiv.org/html/2511.07045v1#S7.F9.sf1 "In Figure 9 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([9b](https://arxiv.org/html/2511.07045v1#S7.F9.sf2 "In Figure 9 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) in Figure [9](https://arxiv.org/html/2511.07045v1#S7.F9 "Figure 9 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem") and the corresponding accumulation problem in panel ([9c](https://arxiv.org/html/2511.07045v1#S7.F9.sf3 "In Figure 9 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")). Notice that both decumulation-only strategies differ from the optimum shown in Figure [8](https://arxiv.org/html/2511.07045v1#S7.F8 "Figure 8 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"). The utility values of the low initial wealth problem are equal within 1%, but the machine learning solution to the high initial wealth problem is not as close to the other numerical method. This is due to the fact that we are using extreme parameters and the gain function becomes hard to compute numerically in these regions. In the accumulation problem, an individual with this level of risk aversion never reaches a wealth above VadequateV^{\text{adequate}}. As a result, we do not observe the pattern of high initial consumption followed by consumption at the adequacy level. If the individual’s contribution rate (or salary) were sufficiently high, wealth would exceed VadequateV^{\text{adequate}} and this behaviour would then emerge. Such contribution rates are, however, somewhat unrealistic in practice.

![Refer to caption](varying_parameter_paper/NN_high_initial_wealth_adequacy_plot.png)


a

![Refer to caption](varying_parameter_paper/NN_low_initial_wealth_adequacy_plot.png)


b

![Refer to caption](varying_parameter_paper/NN_accumulation_adequacy_plot.png)


c

Figure 9: Comparison of retirement outcomes when using the neural network for highly risk averse individuals. For the decumulation only setting, we have Subfigure ([9a](https://arxiv.org/html/2511.07045v1#S7.F9.sf1 "In Figure 9 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with high initial wealth and Subfigure ([9b](https://arxiv.org/html/2511.07045v1#S7.F9.sf2 "In Figure 9 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with low initial wealth. For an accumulation problem, we have Subfigure ([9c](https://arxiv.org/html/2511.07045v1#S7.F9.sf3 "In Figure 9 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem")).

If we use realistic values for the risk-aversion parameter, the impact of the adequacy parameter becomes much harder to see. When realistic parameter values are chosen, adjusting the parameter has little visual impact on the optimal strategy. Both the choice of risk-aversion and the choice of adequacy break the positive homogeneity of the problem and it seems that one can use either varying adequacy levels or exponential risk-aversion to avoid the unreasonable strategies found in [[2](https://arxiv.org/html/2511.07045v1#bib.bib2)] using homogeneous Epstein–Zin preferences.

## 8 Conclusions

We have created a tool which allows pensions to be designed by choosing a family of loss functions and then tuning the
parameters interactively.

We have shown how to overcome the issue of the high variance of an exponential utility function for varied parameters when learning the optimal control in a given setting. We expect
that this architecture could be re-used for more general loss functions and richer economic models.

## References

* [1]

  S. N. Afriat.
  The construction of utility functions from expenditure data.
  International Economic Review, 8(1):67–77, 1967.
* [2]

  J. Armstrong, C. Buescu, and J. Dalby.
  Optimal post-retirement investment and consumption under longevity risk in collective funds.
  Scandinavian Actuarial Journal, 2025.
* [3]

  John Armstrong.
  Classifying markets up to isomorphism.
  arXiv preprint arXiv:1810.03546, 2018.
* [4]

  John Armstrong and Cristin Buescu.
  Collectivised pension investment with exponential kihlstrom–mirman preferences, 2019.
* [5]

  John Armstrong, James Dalby, and Rohan Hobbs.
  Collective defined contribution schemes without intergenerational cross-subsidies, 2025.
* [6]

  John Armstrong and James Luke Dalby.
  Optimal mutual insurance against systematic longevity risk.
  Scandinavian Actuarial Journal, 0(0):1–19, 2025.
* [7]

  Ravi Bansal.
  Long-run risks and financial markets.
  Review, 89(Jul):283–300, None 2007.
* [8]

  Ravi Bansal and Amir Yaron.
  Risks for the long run: A potential resolution of asset pricing puzzles.
  The Journal of Finance, 59(4):1481–1509, 2004.
* [9]

  Luca Benzoni, Pierre Collin-Dufresne, and Robert S. Goldstein.
  Explaining asset pricing puzzles associated with the 1987 market crash.
  Journal of Financial Economics, 101(3):552–573, September 2011.
* [10]

  Thomas Bernhardt and Catherine Donnelly.
  Modern tontine with bequest: Innovation in pooled annuity products.
  Insurance: Mathematics and Economics, 86:168–188, 2019.
* [11]

  David P. Blake, Mel Duffield, Ian Tonks, Alistair Haig, Dean Blower, and Laura MacPhee.
  Grouping individual investment preferences in retirement savings: A cluster analysis of a USS members risk attitude survey.
  Discussion Paper PI-2003, Pensions Institute, City, University of London, February 2020.
* [12]

  Antoine Bommier.
  Uncertain lifetime and intertemporal choice: risk aversion as a rationale for time discounting.
  International Economic Review, 47(4):1223–1246, 2006.
* [13]

  Alexander M. G. Cox, David Hobson, and Jan Obloj.
  Utility theory front to back - inferring utility from agents’ choices, 2012.
* [14]

  Marta Grzeskiewicz.
  Uncovering utility functions from observed outcomes, 2025.
* [15]

  Jiequn Han et al.
  Deep learning approximation for stochastic control problems.
  arXiv preprint arXiv:1611.07422, 2016.
* [16]

  Martin Herdegen, David Hobson, and Joseph Jerome.
  An elementary approach to the merton problem.
  Mathematical Finance, 31(4):1218–1239, 2021.
* [17]

  Martin Herdegen, David Hobson, and Joseph Jerome.
  The infinite-horizon investment-consumption problem for epstein-zin stochastic differential utility. ii.
  Finance and Stochastics, 27(1):159–188, January 2023.
* [18]

  Martin Herdegen, David G. Hobson, and Joseph Jerome.
  The infinite horizon investment-consumption problem for epstein-zin stochastic differential utility. i : Foundations.
  Finance and Stochastics, 27:127–158, January 2023.
* [19]

  Ruimeng Hu and Mathieu Lauriere.
  Recent developments in machine learning methods for stochastic control and games.
  arXiv preprint arXiv:2303.10257, 2023.
* [20]

  Côme Huré, Huyên Pham, Achref Bachouch, and Nicolas Langrené.
  Deep neural networks algorithms for stochastic control problems on finite horizon: convergence analysis.
  SIAM Journal on Numerical Analysis, 59(1):525–557, 2021.
* [21]

  Holger Kraft, Thomas Seiferling, and Frank Thomas Seifried.
  Optimal consumption and investment with epstein–zin recursive utility.
  Finance and Stochastics, 21(1):187–226, 2017.
* [22]

  David M Kreps and Evan L Porteus.
  Temporal resolution of uncertainty and dynamic choice theory.
  Econometrica, pages 185–200, 1978.
* [23]

  L. Leal, M. Lauriere, and C.-A. Lehalle.
  Learning a functional control for high-frequency finance.
  Quantitative Finance, 22(11):1973–1987, 2022.
* [24]

  David G Luenberger.
  Optimization by vector space methods.
  John Wiley & Sons, 1997.
* [25]

  Moshe A. Milevsky.
  King William’s Tontine: Why the Retirement Annuity of the Future Should Resemble its Past.
  Cambridge University Press, 2015.
* [26]

  Moshe A. Milevsky and Thomas S. Salisbury.
  Optimal retirement income tontines.
  Insurance: Mathematics and Economics, 64:91–105, 2015.
* [27]

  Ralph Tyrell Rockafellar.
  Convex Analysis.
  Princeton University Press, 2015.
* [28]

  P. A. Samuelson.
  A note on the pure theory of consumer’s behaviour.
  Economica, 5(17):61–71, 1938.
* [29]

  Michael Z Stamos.
  Optimal consumption and portfolio choice for pooled annuity funds.
  Insurance: Mathematics and Economics, 43(1):56–68, 2008.
* [30]

  Hal R. Varian.
  The nonparametric approach to demand analysis.
  Econometrica, 50(4):945–973, 1982.
* [31]

  John von Neumann, Oskar Morgenstern, and Ariel Rubinstein.
  Theory of Games and Economic Behavior (60th Anniversary Commemorative Edition).
  Princeton University Press, 1944.

## Appendix A Neural Network Architecture Details

Our code is written in Python using the Tensorflow package.

### A.1 RNN Architecture

The main RNN’s used in the fixed-parameter method, and both the one and two step iterative methods are identical aside from the inputs. We mark in brackets the additional inputs to the varying-parameter networks. The networks consist of six layers:

* •

  The first input layer has two (five) nodes, representing: the Gaussian increments and the time points (and the three parameter values).
* •

  The second layer is a dense layer with 8080 nodes and a ReLU activation function.
* •

  The third layer is a gated recurrent unit (GRU) with 2525 nodes. This is the recurrent layer in our network. The activation function is the hyperbolic tangent function and the recurrent activation function is sigmoid. The GRU ensures that the network returns an output at each time point.
* •

  The fourth and fifth layers are identical to the second layer.
* •

  The final output layer has two nodes, which represent the proportion of wealth to invest in the risky asset and the proportion of wealth to consume. We use the linear activation function for both outputs, and perform a transformation of the consumption proportion so that it remains in the interval [0,1][0,1]. We obtain investment and consumption decisions in each year of our simulation as a result of the GRU.

We used the Adam optimizer with an initial learning rate of 0.0010.001. Each time, training was carried out over 500500 epochs, each consisting of 131,072131,072 scenarios with a batch size of 4,0964,096. A validation set of 10,00010,000 separately generated scenarios was evaluated at the end of each epoch. We use a large number of epochs and simply extract the weights for which the validation and training loss was least.

### A.2 The Scaling Network

The ‘scaling’ network in both methods is a feedforward neural network with a much simpler architecture. The mean estimating network in the one-step iterative method also has the same architecture. They consist of an input layer of three nodes, that takes the three parameter values and three hidden layers each with 6464 nodes. All of the hidden layers use the ReLU activation function. The output layer has one node, representing predictions for standard deviation (mean in the case of the mean estimating network) of the loss function. The output layer uses the linear activation function since we take the scaling factors as logarithms.

For the one-step method, these networks are trained in the same loop as the main RNN, and so have the same training parameters as the main RNN.

For the two-step iterative method, training consisted of 100100 epochs, where the training data was 80%80\% of the 50,00050,000 data points and the validation data was the remainder. We use a batch size of 1,0001,000 and the mean-square-error loss function. We use the Adam optimizer with an initial learning rate of 0.0010.001. We break up the parameter sets for each iteration. The smallest parameter ranges 𝒫0=𝒫1\mathcal{P}\_{0}=\mathcal{P}\_{1}, used for training the first ‘scaling’ network, is given by Table [2](https://arxiv.org/html/2511.07045v1#A1.T2 "Table 2 ‣ A.2 The Scaling Network ‣ Appendix A Neural Network Architecture Details ‣ Machine-learning a family of solutions to an optimal pension investment problem").

| Parameters | Min | Max |
| --- | --- | --- |
| α\alpha | 10−510^{-5} | 10−410^{-4} |
| ρ\rho | −2-2 | −1-1 |
| aa | 0.20.2 | 0.70.7 |

Table 2: The smaller parameter range used to train the first iteration scaling network in the two-step iterative algorithm.

The parameter range 𝒫2\mathcal{P}\_{2}, used for training the second ‘scaling’ network, is given in Table [3](https://arxiv.org/html/2511.07045v1#A1.T3 "Table 3 ‣ A.2 The Scaling Network ‣ Appendix A Neural Network Architecture Details ‣ Machine-learning a family of solutions to an optimal pension investment problem").

| Parameters | Min | Max |
| --- | --- | --- |
| α\alpha | 10−610^{-6} | 10−310^{-3} |
| ρ\rho | −2-2 | −0.1-0.1 |
| aa | 0.20.2 | 1.01.0 |

Table 3: The second parameter range used to train the second scaling network in the two-step iterative algorithm.

The full parameter range 𝒫3\mathcal{P}\_{3}, used for training the third ‘scaling’ network, is given in Table [4](https://arxiv.org/html/2511.07045v1#A1.T4 "Table 4 ‣ A.2 The Scaling Network ‣ Appendix A Neural Network Architecture Details ‣ Machine-learning a family of solutions to an optimal pension investment problem").

| Parameters | Min | Max |
| --- | --- | --- |
| α\alpha | 10−710^{-7} | 10−210^{-2} |
| ρ\rho | −2-2 | −0.1-0.1 |
| aa | 0.10.1 | 1.01.0 |

Table 4: The third parameter range used to train the third scaling network in the two-step iterative algorithm.

### A.3 Replacement Ratio Percentile Network

The replacement ratio percentile network is a feedforward neural network. It consists of an input layer with five nodes, to represent the time point, the percentile and the three varying parameters. So the replacement ratio percentile network learns the value of the replacement ratio for a given time point, in a given percentile, for a given set of parameters. There are three hidden layers consisting of 64 nodes, all with the ReLU activation function. The output layer has a single node as the network only makes one prediction per data point. The output layer is governed by the sigmoid activation function since we transform both inputs and outputs to the interval [0,1][0,1].

We follow the same training procedure as with the ‘scaling’ network in the two-step iterative approach, but note that we obtain a larger data set since each data point consists of nine percentiles, each 5656 time points long. This therefore means we only need 5050 epochs to find the minimum.

## Appendix B Strategy Plots to Match Outcome Plots

Here, we show the strategy produced by the respective networks to produce the outcome plots in the main text of the paper.

![Refer to caption](varying_parameter_paper/fixed_parameter_consumption_proportion.png)


a

![Refer to caption](varying_parameter_paper/fixed_parameter_investment_proportion.png)


b

Figure 10: Panel ([10a](https://arxiv.org/html/2511.07045v1#A2.F10.sf1 "In Figure 10 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the consumption strategy for the outcomes plotted in Figure [2](https://arxiv.org/html/2511.07045v1#S2.F2 "Figure 2 ‣ 2 Training the Fixed Parameter Network ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for the fixed-parameter RNN. Panel ([10b](https://arxiv.org/html/2511.07045v1#A2.F10.sf2 "In Figure 10 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the corresponding investment strategy.



![Refer to caption](varying_parameter_paper/comaprison_strategies_varying_with_fixed_plot.png)

Figure 11: Consumption and investment strategies for the outcomes plotted in Figure [4a](https://arxiv.org/html/2511.07045v1#S5.F4.sf1 "In Figure 4 ‣ 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for the two-step iterative approach as compared to the fixed network.



![Refer to caption](varying_parameter_paper/comparison_simultaneous_scaling_strategies.png)

Figure 12: Consumption and investment strategies for the outcomes plotted in Figure [4b](https://arxiv.org/html/2511.07045v1#S5.F4.sf2 "In Figure 4 ‣ 5.1 A Two-Step Iterative Algorithm ‣ 5 Two Alternative Architectures ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for the one-step approach as compared to the fixed network.



![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/high_risk_aversion_consumption_strategy.png)


a

![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/high_risk_aversion_investment_strategy.png)


b

Figure 13: Panel ([13a](https://arxiv.org/html/2511.07045v1#A2.F13.sf1 "In Figure 13 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the consumption strategy for the outcomes plotted in Figure [6a](https://arxiv.org/html/2511.07045v1#S7.F6.sf1 "In Figure 6 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for high risk aversion. Panel ([13b](https://arxiv.org/html/2511.07045v1#A2.F13.sf2 "In Figure 13 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the corresponding investment strategy.



![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/low_risk_aversion_consumption_strategy.png)


a

![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/low_risk_aversion_investment_strategy.png)


b

Figure 14: Panel ([14a](https://arxiv.org/html/2511.07045v1#A2.F14.sf1 "In Figure 14 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the consumption strategy for the outcomes plotted in Figure [6b](https://arxiv.org/html/2511.07045v1#S7.F6.sf2 "In Figure 6 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for low risk aversion. Panel ([14b](https://arxiv.org/html/2511.07045v1#A2.F14.sf2 "In Figure 14 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the corresponding investment strategy.



![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/more_easily_satiated_consumption_strategy.png)


a

![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/more_easily_satiated_investment_strategy.png)


b

Figure 15: Panel ([15a](https://arxiv.org/html/2511.07045v1#A2.F15.sf1 "In Figure 15 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the consumption strategy for the outcomes plotted in Figure [7a](https://arxiv.org/html/2511.07045v1#S7.F7.sf1 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for more easily satiated preferences. Panel ([15b](https://arxiv.org/html/2511.07045v1#A2.F15.sf2 "In Figure 15 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the corresponding investment strategy.



![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/less_easily_satiated_consumption_strategy.png)


a

![Refer to caption](varying_parameter_paper/strategy_plots_same_y_axis/less_easily_satiated_investment_strategy.png)


b

Figure 16: Panel ([16a](https://arxiv.org/html/2511.07045v1#A2.F16.sf1 "In Figure 16 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the consumption strategy for the outcomes plotted in Figure [7b](https://arxiv.org/html/2511.07045v1#S7.F7.sf2 "In Figure 7 ‣ 7 Sensitivity Analysis of Optimal Strategies ‣ Machine-learning a family of solutions to an optimal pension investment problem"), for less easily satiated preferences. Panel ([16b](https://arxiv.org/html/2511.07045v1#A2.F16.sf2 "In Figure 16 ‣ Appendix B Strategy Plots to Match Outcome Plots ‣ Machine-learning a family of solutions to an optimal pension investment problem")) shows the corresponding investment strategy.

## Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem

Recall that the dynamics of ww are determined by equations ([1](https://arxiv.org/html/2511.07045v1#S1.E1 "In 1 Discrete-time investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([3](https://arxiv.org/html/2511.07045v1#S1.E3 "In 1 Discrete-time investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).
We define an admissible control
to be a progressively measurable process ((Ct)t∈𝒯,(πt)t∈[0,T])((C\_{t})\_{t\in{\cal T}},(\pi\_{t})\_{t\in[0,T]}) such that wt−≥0w\_{t-}\geq 0
and wt≥0w\_{t}\geq 0 for all time.
We write 𝒜{\cal A} for the set of admissible controls.

Our objective is to compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | v:=sup(C,π)∈𝒜U​(C),v:=\sup\_{(C,\pi)\in{\cal A}}U(C), |  | (7) |

and to find (C,π)(C,\pi) achieving (or if necessary, approximating) this supremum.

Our strategy is to solve the one-period problem using a duality method which will
allow us to identify the solution with minimal assumptions on the form of our utility
function. To simplify the duality argument, we use the theory of isomorphic markets to recast the problem in a particularly simple form. Having obtained this solution, we
will recursively solve the multi-period problem.
Our goal in this appendix is to give
all details needed to implement the resulting algorithm and a proof of its convergence.

### C.1 Solution to the one-period problem

Write 𝒜w,t{\cal A}\_{w,t} for the admissible consumption-investment
strategies that start with wealth ww at time tt.
Define the value function vv, as
a function of initial wealth, ww at time t1∈𝒯t\_{1}\in{\cal T} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt​(w)\displaystyle v\_{t}(w) | :=supC,π∈𝒜w,t𝔼​(−exp⁡(−α​∑j∈𝒯,t≤j<τu​(Cj)​δ​t))\displaystyle:=\sup\_{{C,\pi}\in{\cal A}\_{w,t}}\mathbb{E}\left(-\exp\left(-\alpha\sum\_{j\in{\cal T},\,{t\leq j<\tau}}u(C\_{j})\delta t\right)\right) |  |

To make the limits in the sum easier to read, we will write the sum
using the following integral notation

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt​(w)\displaystyle v\_{t}(w) | =supC,π∈𝒜w,t𝔼​(−exp⁡(−α​∫tτu​(Cs)​d𝒯​(s))).\displaystyle=\sup\_{{C,\pi}\in{\cal A}\_{w,t}}\mathbb{E}\left(-\exp\left(-\alpha\int\_{t}^{\tau}u(C\_{s})\mathrm{d}{\cal T}(s)\right)\right). |  |

Given vtv\_{t}, we wish to compute vt−δ​tv\_{t-\delta t}, we will then be able
to recursively compute vtv\_{t} for all t∈𝒯t\in{\cal T}. Our next theorem
shows how to compute vt−δ​tv\_{t-\delta t}, but
in order to state our results concisely we first make the following definitions.

###### Definition C.1.

Let f:ℝ→ℝ∪{±∞}f:\mathbb{R}\to\mathbb{R}\cup\{\pm\infty\} be concave and increasing. Define

|  |  |  |
| --- | --- | --- |
|  | f†​(p):ℝ>0→ℝf^{\dagger}(p):\mathbb{R}\_{>0}\to\mathbb{R} |  |

by

|  |  |  |
| --- | --- | --- |
|  | f†​(p)=inf{x∣p∈∂f​(x)}f^{\dagger}(p)=\inf\{x\mid p\in\partial f(x)\} |  |

where ∂f​(x)\partial f(x) is the sub-differential of ff at xx.

For sufficiently regular
functions uu, we have f†=(f′)−1f^{\dagger}=(f^{\prime})^{-1}, or, equivalently, f†f^{\dagger}
is the derivative of the Legendre transform of uu.

###### Definition C.2.

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(z):=Φ​(M+Φ−1​(z)),Q(z):=\Phi\left(M+\Phi^{-1}(z)\right), |  | (8) |

where Φ\Phi is the cumulative distribution function of the
standard normal distribution and

|  |  |  |
| --- | --- | --- |
|  | M:=|μ−r|​δ​tσ.M:=\frac{\left|\mu-r\right|\sqrt{\delta t}}{\sigma}. |  |

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | qBSA​(z)=d​Qd​z.q^{A}\_{\mathrm{BS}}(z)=\frac{\mathrm{d}Q}{\mathrm{d}z}. |  | (9) |

As we will show in Lemma [C.5](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem") below, the quantity qBSA​(z)q^{A}\_{\mathrm{BS}}(z) can be related to the pricing kernel of the Black–Scholes model.

We may now state the following result which allows us to solve the one period problem.

###### Proposition C.3.

Suppose that t1=t0+δ​tt\_{1}=t\_{0}+\delta t and that v​(w):=vt1​(w)v(w):=v\_{t\_{1}}(w) is known, concave and increasing
for w>0w>0, equal to −∞-\infty for w≤0w\leq 0,
and satisfies v​(w)≤0v(w)\leq 0. Define st=(1−pt)s\_{t}=(1-p\_{t}) for t∈𝒯t\in{\cal T}, so sts\_{t} denotes the survival
probability over the period [t,t+δ​t)[t,t+\delta t).

1. (a)

   vt0​(w)v\_{t\_{0}}(w) is itself concave and increasing for w>0w>0, equal to −∞-\infty for w≤0w\leq 0
   and satisfies v​(w)≤0v(w)\leq 0.
2. (b)

   For each η>0\eta>0 define a function on
   fη:(0,1)→ℝ≥0f^{\eta}:(0,1)\to\mathbb{R}\_{\geq 0} by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | fη​(s)=v†​(η​e−r​δ​t​qBSA​(s)).f^{\eta}(s)=v^{\dagger}\left(\eta e^{-r\delta t}q^{A}\_{\mathrm{BS}}(s)\right). |  | (10) |

   Define Cη∈ℝ≥0C^{\eta}\in\mathbb{R}\_{\geq 0} by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Cη=u†​(−ηδ​t​(−1+st0​∫01(1+v​(fη​(s)))​ds)−1).C^{\eta}=u^{\dagger}\left(-\frac{\eta}{\delta t}\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f^{\eta}(s)))\,\mathrm{d}s\right)^{-1}\right). |  | (11) |

   Define wηw^{\eta} by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | wη=Cη+st0​∫01e−r​δ​t​qBSA​(s)​fη​(s).w^{\eta}=C^{\eta}+s\_{t\_{0}}\int\_{0}^{1}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(s)f^{\eta}(s). |  | (12) |

   If there exists ηwt0\eta\_{w\_{t\_{0}}} such that wηwt0=wt0w^{\eta\_{w\_{t\_{0}}}}=w\_{t\_{0}} then we have

   |  |  |  |
   | --- | --- | --- |
   |  | vt0​(wt0)=exp⁡(−u​(γηX0)​δ​t)​(−1+st0​∫01(1+v​(fηwt0​(s)))​ds)v\_{t\_{0}}(w\_{t\_{0}})=\exp(-u(\gamma^{\eta\_{X\_{0}}})\delta t)\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f^{\eta\_{w\_{t\_{0}}}}(s)))\,\mathrm{d}s\right) |  |

   and Cηwt0C^{\eta\_{w\_{t\_{0}}}} is the optimal consumption at time t0t\_{0}.

Part [(a)](https://arxiv.org/html/2511.07045v1#A3.I1.i1 "item (a) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem") is trivial. For example the
statement about concavity follows from [[24](https://arxiv.org/html/2511.07045v1#bib.bib24)] Proposition 8.3.1.
The proof strategy for Part [(b)](https://arxiv.org/html/2511.07045v1#A3.I1.i2 "item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem") is as follows:

1. (i)

   Use the dynamic programming principle to obtain a recursive formulation of the problem. This is done in Lemma [C.4](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem4 "Lemma C.4. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")
2. (ii)

   Reduce the continuous time investment problem of the recursion step to a calculus of variations problem using the classification of one-period complete markets. This is done in Lemma [C.6](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem6 "Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem").
3. (iii)

   Solve the resulting calculus of variations problem. This is done in Lemma [C.7](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem7 "Lemma C.7. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem").

Let us first see how to compute
vt0​(X0)v\_{t\_{0}}(X\_{0}) as the solution to a one period optimal investment problem.

###### Lemma C.4.

Assume the conditions of Proposition [C.3](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem3 "Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem").
Let 𝒜wt0,t0,t1{\cal A}\_{w\_{t\_{0}},t\_{0},t\_{1}} denote the set of pairs (Ct0,π)(C\_{t\_{0}},\pi)
where π\pi is an admissible investment strategy for the period [t0,t1][t\_{0},t\_{1}] and Ct0∈ℝC\_{t\_{0}}\in\mathbb{R} is the consumption at time t0t\_{0}
and satisfies Ct0<wt0C\_{t\_{0}}<w\_{t\_{0}}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt0​(wt0):=supCt0,α∈𝒜wt0,t0,t1{exp⁡(−u​(Ct0)​δ​t)​(−1+st0​𝔼​(1+vt1​(wt1(Ct0,π))))}\begin{split}v\_{t\_{0}}(w\_{t\_{0}}):=\sup\_{{C\_{t\_{0}},\alpha}\in{\cal A}\_{w\_{t\_{0}},t\_{0},t\_{1}}}\Big\{\exp\left(-u(C\_{t\_{0}})\delta t\right)\left(-1+s\_{t\_{0}}\mathbb{E}\left(1+v\_{t\_{1}}(w^{(C\_{t\_{0}},\pi)}\_{t\_{1}})\right)\right)\Big\}\end{split} |  | (13) |

where wt1(Ct0,π)w^{(C\_{t\_{0}},\pi)}\_{t\_{1}} is the value obtained by
following the investment strategy π\pi from t0t\_{0} to t1t\_{1}
with an initial wealth of st−1​(wt0−Ct0)s\_{t}^{-1}(w\_{t\_{0}}-C\_{t\_{0}}).

###### Proof.

We calculate

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt0​(wt0)\displaystyle v\_{t\_{0}}(w\_{t\_{0}}) | =supC,π∈𝒜wt0,t0{𝔼(−exp(−u(Ct0)δt)ℙ(τ<t1∣τ≥t0))\displaystyle=\sup\_{{C,\pi}\in{\cal A}\_{w\_{t\_{0}},t\_{0}}}\Big\{\mathbb{E}\left(-\exp\left(-u(C\_{t\_{0}})\delta t\right)\mathbb{P}(\tau<t\_{1}\mid\tau\geq t\_{0})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼(−exp(−u(Ct0)δt−∫t1τu(Ct)d𝒯(t))∣τ≥t1)ℙ(τ≥t1∣τ≥t0)}\displaystyle\quad\quad\quad+\mathbb{E}\left(-\exp\left(-u(C\_{t\_{0}})\delta t-\int\_{t\_{1}}^{\tau}u(C\_{t})\,\mathrm{d}{\cal T}(t)\right)\mid\tau\geq t\_{1}\right)\mathbb{P}(\tau\geq t\_{1}\mid\tau\geq t\_{0})\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supC,π∈𝒜wt0,t0{−(1−st0)exp(−u(Ct0)δt)\displaystyle=\sup\_{{C,\pi}\in{\cal A}\_{w\_{t\_{0}},t\_{0}}}\Big\{-(1-s\_{t\_{0}})\exp\left(-u(C\_{t\_{0}})\delta t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +st0exp(−u(Ct0)δt)𝔼(−exp(−∫t1τu(Ct)d𝒯(t))∣τ≥t1)}\displaystyle\quad\quad\quad+s\_{t\_{0}}\exp(-u(C\_{t\_{0}})\delta t)\mathbb{E}\left(-\exp\left(-\int\_{t\_{1}}^{\tau}u(C\_{t})\,\mathrm{d}{\cal T}(t)\right)\mid\tau\geq t\_{1}\right)\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supγ,π∈𝒜wt0,t0{exp(−u(Ct0)δt)×\displaystyle=\sup\_{{\gamma,\pi}\in{\cal A}\_{w\_{t\_{0}},t\_{0}}}\Bigg\{\exp\left(-u(C\_{t\_{0}})\delta t\right)\times |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (−1+st0𝔼(1−exp(−∫t1τu(Ct)d𝒯(t))∣τ≥t1))}\displaystyle\quad\quad\quad\left(-1+s\_{t\_{0}}\mathbb{E}\left(1-\exp\left(-\int\_{t\_{1}}^{\tau}u(C\_{t})\,\mathrm{d}{\cal T}(t)\right)\mid\tau\geq t\_{1}\right)\right)\Bigg\} |  |

The result now follows by the dynamic
programming principle.
∎

Equation ([13](https://arxiv.org/html/2511.07045v1#A3.E13 "In Lemma C.4. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) is a one-period investment problem in a complete market.
Complete one-period markets are classified
in [[3](https://arxiv.org/html/2511.07045v1#bib.bib3)]. This allows us to find
a more convenient, but isomorphic, representation
of our market.
For complete one-period markets, we may
say that two markets are isomorphic if they have the same
risk-free rate and if there is a map which acts as a
probability space isomorphism for both the ℙ\mathbb{P} and ℚ\mathbb{Q}
measures simultaneously.

Let ΩA\Omega^{A} be the probability space given by [0,1]×[0,1][0,1]\times[0,1]
equipped with the Lebesgue measure. Let qA:[0,1]→ℝ>0q^{A}:[0,1]\to\mathbb{R}\_{>0} be a
measurable function of integral 11. We may define an
abstract financial market
(ΩA,qA,r)(\Omega^{A},q^{A},r) whose assets consist of random variables ff
(representing the payoff of the asset)
defined on ΩA\Omega^{A}. The cost of asset ff is given by

|  |  |  |
| --- | --- | --- |
|  | PA​(f):=∫[0,1]×[0,1]e−r​δ​t​f​(x,y)​qA​(x)​dx​dyP^{A}(f):=\int\_{[0,1]\times[0,1]}e^{-r\delta t}f(x,y)\,q^{A}(x)\,\mathrm{d}x\,\mathrm{d}y |  |

if this integral exists. Assets of positively infinite or undefined cost
cannot be purchased. Assets of infinitely negative cost can
be purchased at any price. The AA in our superscripts
stands for abstract. Notice that in this abstract market
the random variable UU defined by U​(x,y)=xU(x,y)=x is uniform
in the ℙA\mathbb{P}^{A} measure and has density qAq^{A} in the ℚA\mathbb{Q}^{A} measure.

###### Lemma C.5.

As a one period market, the Black–Scholes–Merton market
from time t0t\_{0} to time t1t\_{1}
is isomorphic to the market (ΩA,qBSA,r)(\Omega^{A},q^{A}\_{\mathrm{BS}},r).

We defer the proof to appendix [D](https://arxiv.org/html/2511.07045v1#A4 "Appendix D Proof of Lemma C.5 ‣ Machine-learning a family of solutions to an optimal pension investment problem").

Having found a simple isomorphic representative of our market, we can rewrite
the equation ([13](https://arxiv.org/html/2511.07045v1#A3.E13 "In Lemma C.4. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) in terms of the abstract market ΩA\Omega^{A}.

###### Lemma C.6.

Assume the conditions of Proposition [C.3](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem3 "Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem").
The value function vt0​(wt0)v\_{t\_{0}}(w\_{t\_{0}}) can be calculated by
solving the optimisation problem

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | maximizeC∈ℝ,f∈L0​[0,1]\displaystyle\underset{C\in\mathbb{R},f\in L^{0}[0,1]}{\mathrm{maximize}} |  | exp⁡(−u​(C)​δ​t)​(−1+st0​∫01(1+v​(f​(s)))​ds)\displaystyle\exp(-u(C)\delta t)\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f(s)))\,\mathrm{d}s\right) |  | (14) |
|  |  | subject to |  | C+st0​∫01e−r​δ​t​qBSA​(s)​f​(s)​ds≤wt0.\displaystyle C+s\_{t\_{0}}\int\_{0}^{1}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(s)f(s)\,\mathrm{d}s\leq w\_{t\_{0}}. |  |

taking v=vt1v=v\_{t\_{1}}.

###### Proof.

Let us write (Ct0,f)(C\_{t\_{0}},f) for a pair of a consumption
Ct0∈ℝC\_{t\_{0}}\in\mathbb{R} and an
investment f∈L0​(ΩA)f\in L^{0}(\Omega^{A}).
We denote by ℬwt0{\cal B}\_{w\_{t\_{0}}} the set
of consumptions and investments that are available with
a budget of wt0{w\_{t\_{0}}}

|  |  |  |
| --- | --- | --- |
|  | ℬwt0={(Ct0,f)∈ℝ×L0​(ΩA)∣γt0+st0​PBSA​(f)≤X0}.{\cal B}\_{w\_{t\_{0}}}=\{(C\_{t\_{0}},f)\in\mathbb{R}\times L^{0}(\Omega^{A})\mid\gamma\_{t\_{0}}+s\_{t\_{0}}P^{A}\_{\mathrm{BS}}(f)\leq X\_{0}\}. |  |

If we also write

|  |  |  |
| --- | --- | --- |
|  | Ut0A​(Ct0,f):=exp⁡(−u​(Ct0)​δ​t)​(−1+st0​∫[0,1]×[0,1](1+vt1​(f​(x,y)))​dx​dy)\begin{split}U^{A}\_{t\_{0}}(C\_{t\_{0}},f):=&\exp(-u(C\_{t\_{0}})\delta t)\left(-1+s\_{t\_{0}}\int\_{[0,1]\times[0,1]}\,(1+v\_{t\_{1}}(f(x,y)))\,\mathrm{d}x\,\mathrm{d}y\right)\end{split} |  |

to accord with equation ([13](https://arxiv.org/html/2511.07045v1#A3.E13 "In Lemma C.4. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")),
then the fact that our markets are isomorphic allows
us to deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt0​(wt0):=sup(C,f)∈ℬwt0UA​(Ct0,f).v\_{t\_{0}}(w\_{t\_{0}}):=\sup\_{(C,f)\in{\cal B}\_{w\_{t\_{0}}}}U^{A}(C\_{t\_{0}},f). |  | (15) |

Since vt1v\_{t\_{1}} is assumed to be concave we may average an
investment f​(x,y)f(x,y) over the factor yy to obtain a new investment
f¯\overline{f} which achieves a higher value for the gain
function UAU^{A}. Thus we may restrict our attention
to investments f​(x,y)f(x,y) which depend only upon xx. The result follows.
∎

Note that an investment f∈L1f\in L^{1} for this abstract market
model corresponds to a derivative with payoff given by
the random variable f​(Fd​ℚd​ℙ​(d​ℚd​ℙ))f(F\_{\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}}(\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}})) in the original Black–Scholes–Merton market (or indeed in any isomorphic market). This derivative can then be replicated by delta hedging
in the Black–Scholes–Merton market. So the solution to the
abstract investment problem ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
can be straightforwardly mapped to a solution of the original problem.

###### Lemma C.7.

Assume the conditions and definitions of Proposition [C.3](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem3 "Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"). If an ηwt0\eta\_{w\_{t\_{0}}} exists with wηwt0=wt0w^{\eta\_{w\_{t\_{0}}}}=w\_{t\_{0}},
then the solution of ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) is given by fηwt0f^{\eta\_{w\_{t\_{0}}}}
and γηwt0\gamma^{\eta\_{w\_{t\_{0}}}}.

###### Proof.

We will now solve ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) using
the method of Lagrange multipliers. We define a vector space V=ℝ⊕L0​([0,1])⊕ℝV=\mathbb{R}\oplus L^{0}([0,1])\oplus\mathbb{R}
For λ∈ℝ\lambda\in\mathbb{R},
we define the Lagrangian
L:V→ℝL:V\to\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(C,f,λ):=exp⁡(−u​(C)​δ​t)​(−1+st0​∫01(1+v​(f​(s)))​ds)+λ​(−X0+C+st0​∫01e−r​δ​t​qBSA​(s)​f​(s)​ds).\begin{split}L(C,f,\lambda):=&\exp(-u(C)\delta t)\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f(s)))\,\mathrm{d}s\right)\\ &+\lambda\left(-X\_{0}+C+s\_{t\_{0}}\int\_{0}^{1}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(s)f(s)\,\mathrm{d}s\right).\end{split} |  | (16) |

Computing the directional derivatives of L​(C,f)L(C,f) we find the following
necessary and sufficient conditions for (C,f)(C,f) to be a saddle point of L​(γ,f,λ)L(\gamma,f,\lambda)
for the given λ\lambda. Firstly

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0∈−∂u​(C)​δ​t​exp⁡(−u​(C)​δ​t)​(−1+st0​∫01(1+v​(f​(s)))​ds)+λ0\in-\partial u(C)\delta t\exp(-u(C)\delta t)\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f(s)))\,\mathrm{d}s\right)+\lambda |  | (17) |

where ∂u​(C)\partial u(C) is the subdifferential of uu at CC.
Secondly

|  |  |  |
| --- | --- | --- |
|  | 0=∫01(exp⁡(−u​(C)​δ​t)​st0​(∂v)​(f​(s))+λ​st0​e−r​δ​t​qBSA​(s))​g​(s)​ds.0=\int\_{0}^{1}\left(\exp(-u(C)\delta t)s\_{t\_{0}}(\partial v)(f(s))+\lambda s\_{t\_{0}}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(s)\right)g(s)\,\mathrm{d}s. |  |

The integral is well-defined since ∂v\partial v will
be single-valued almost everywhere.
This must hold for all g​(s)g(s) so this is equivalent to requiring

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∂v)​(f​(z))=−λ​exp⁡(u​(C)​δ​t)​st0​e−r​δ​t​qBSA​(z).(\partial v)(f(z))=-\lambda\exp(u(C)\delta t)s\_{t\_{0}}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(z). |  | (18) |

for almost all z∈(0,1)z\in(0,1).

If the Kuhn-Tucker
conditions ([17](https://arxiv.org/html/2511.07045v1#A3.E17 "In C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([18](https://arxiv.org/html/2511.07045v1#A3.E18 "In C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
are satisfied, ((C,f),λ)((C,f),\lambda) will be a saddle point of the Lagrangian.
The theory of Lagrange multipliers (see [[27](https://arxiv.org/html/2511.07045v1#bib.bib27)] Theorem 28.3)
now shows that if we can
find (C,f)(C,f) satisfying the Kuhn–Tucker conditions ([17](https://arxiv.org/html/2511.07045v1#A3.E17 "In C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
and ([18](https://arxiv.org/html/2511.07045v1#A3.E18 "In C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) then this will yield a maximizer
for the problem ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) in the case
where the initial budget satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt0=C+st0​∫01e−r​δ​t​qBSA​(s)​f​(s)​ds.w\_{t\_{0}}=C+s\_{t\_{0}}\int\_{0}^{1}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(s)f(s)\,\mathrm{d}s. |  | (19) |

We remark that the theory of Lagrange multipliers given in [[27](https://arxiv.org/html/2511.07045v1#bib.bib27)] is
stated in terms of finite-dimensional spaces. We may, nevertheless, apply it
by noting that if (C,f)(C,f) satisfies the Kuhn–Tucker conditions yet
is not a maximizer then there must be some direction
in which we can perturb (C,f)(C,f) to obtain a higher value for the gain. We may
now apply the finite-dimensional theory to the vector space generated by this perturbation
to obtain a contradiction.

The result now follows by introducing a variable

|  |  |  |
| --- | --- | --- |
|  | η:=−λ​exp⁡(u​(C)​δ​t)\eta:=-\lambda\exp(u(C)\delta t) |  |

to simplify the equations.
∎

This completes the proof of Proposition [C.3](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem3 "Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem").

The outstanding difficulty is proving that an η\eta solving wη=wt0w^{\eta}=w\_{t\_{0}} exists.
One might attempt to use general duality theory to do this. Theorem 8.3.1 of [[24](https://arxiv.org/html/2511.07045v1#bib.bib24)]
ensures that so long as wt0w\_{t\_{0}} is chosen to satisfy the Slater condition we can guarantee
the existence of a λ\lambda minimizing the dual problem. However, this theorem does not
guarantee the existence of a maximizer for the primal problem. As a result, even if one knows
the value of λ\lambda it is still unclear whether a solution to ([17](https://arxiv.org/html/2511.07045v1#A3.E17 "In C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
and ([18](https://arxiv.org/html/2511.07045v1#A3.E18 "In C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) exists. When one introduces the variable η\eta, this ensures
that CηC^{\eta} and fηf^{\eta} are well-defined once η\eta is known and so the problem
shifts to finding the correct value of η\eta. We will resolve this issue in
the cases of interest using a continuity argument in the next section.

### C.2 Numerical approximation of the multi-period problem

The results of the previous section immediately suggests a numerical method for
solving our investment problems with exponential utility.

We define the minimum acceptable consumption to be

|  |  |  |
| --- | --- | --- |
|  | Cmin:=inf{C∈ℝ∣u​(C)>−∞}.C\_{\min}:=\inf\{C\in\mathbb{R}\mid u(C)>-\infty\}. |  |

In addition to the previous assumptions that uu is concave and increasing, we assume

|  |  |  |  |
| --- | --- | --- | --- |
|  | u†​ is continuous on ​(0,∞)u^{\dagger}\text{ is continuous on }(0,\infty) |  | (20) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→0u†​(p)=∞.\lim\_{p\to 0}u^{\dagger}(p)=\infty. |  | (21) |

We note that our assumption that uu is concave and increasing also ensures that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞u†​(p)=Cmin.\lim\_{p\to\infty}u^{\dagger}(p)=C\_{\min}. |  | (22) |

###### Algorithm C.8.

Choose a grid of points
𝒳={x1,x2​…,xN}{\cal X}=\{x\_{1},x\_{2}\ldots,x\_{N}\} on which we will approximate the value function vtv\_{t}.
We will write v~t\tilde{v}\_{t} for our approximate value function.
This will be a concave increasing
piecewise linear function equal to −∞-\infty on (−∞,x1)(-\infty,x\_{1}), linear on [xi,xi+1][x\_{i},x\_{i+1}]
and constant on [xN,∞)[x\_{N},\infty). We will simply need
to store the values v~t​(xi){\tilde{v}}\_{t}(x\_{i}) at the grid points.

To avoid numerical overflow issues we define a function
ℓ​(x):=−log⁡(−x)\ell(x):=-\log(-x) and store the values ℓ​(v~t​(xi))\ell(\tilde{v}\_{t}(x\_{i}))
at each grid point rather than storing v~t​(xi)\tilde{v}\_{t}(x\_{i}) itself.

1. (i)

   Choose the values at the final time point T−δ​tT-\delta t by

   |  |  |  |
   | --- | --- | --- |
   |  | v~T−δ​t​(xi):=vT−δ​t​(xi)=−exp⁡(−u​(xi)​δ​t).\tilde{v}\_{T-\delta t}(x\_{i}):=v\_{T-\delta t}(x\_{i})=-\exp(-u(x\_{i})\delta t). |  |

   Or equivalently

   |  |  |  |
   | --- | --- | --- |
   |  | ℓ​(v~T−δ​t​(xi))=ℓ​(vT−δ​t​(xi))=u​(xi)​δ​t.\ell(\tilde{v}\_{T-\delta t}(x\_{i}))=\ell(v\_{T-\delta t}(x\_{i}))=u(x\_{i})\delta t. |  |
2. (ii)

   Suppose that v~t\tilde{v}\_{t} is known. Set
   v~t−δ​t​(xi)\tilde{v}\_{t-\delta t}(x\_{i}) to be the solution of ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
   with vt1=v~tv\_{t\_{1}}=\tilde{v}\_{t} and initial budget xix\_{i}. We describe in detail how
   to solve this problem in Proposition [C.10](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem10 "Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem") below.

Since vT−δ​tv\_{T-\delta t} is concave and increasing and
v~T−δ​t\tilde{v}\_{T-\delta t} is piecewise linear v~T−δ​t​(w)≤vT−δ​t​(w)\tilde{v}\_{T-\delta t}(w)\leq v\_{T-\delta t}(w). Let v^t​(w)\hat{v}\_{t}(w)
be defined to be the solution of ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
with vt1=v~tv\_{t\_{1}}=\tilde{v}\_{t} and initial budget ww. We see
that v~T−δ​t​(w)≤v^T−δ​t​(w)≤vT−δ​t​(w)\tilde{v}\_{T-\delta t}(w)\leq\hat{v}\_{T-\delta t}(w)\leq v\_{T-\delta t}(w).

Let
𝒳1⊆𝒳2⊆𝒳3​…{\cal X}\_{1}\subseteq{\cal X}\_{2}\subseteq{\cal X}\_{3}\ldots
be an increasing sequence of grids
with 𝒳∞:=∪j=1∞𝒳i{\cal X}\_{\infty}:=\cup\_{j=1}^{\infty}{\cal X}\_{i} being dense
in (0,∞)(0,\infty). Write v~tj\tilde{v}^{j}\_{t}
for the approximations with respect to 𝒳i{\cal X}\_{i}.
We see by repeating the argument above that v~tj​(w)≤vt​(w)\tilde{v}^{j}\_{t}(w)\leq v\_{t}(w) at all points w∈(0,∞)w\in(0,\infty).
Hence we may define

|  |  |  |
| --- | --- | --- |
|  | v~t​(w)=limj→∞v~tj​(w).\tilde{v}\_{t}(w)=\lim\_{j\to\infty}\tilde{v}^{j}\_{t}(w). |  |

###### Theorem C.9 (Convergence of Algorithm [C.8](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem8 "Algorithm C.8. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).

Define

|  |  |  |
| --- | --- | --- |
|  | Wmin,t=sup{w∣vt​(w)=−∞}.W\_{\min,t}=\sup\{w\mid v\_{t}(w)=-\infty\}. |  |

For w>Wmin,tw>W\_{\min,t} we have

|  |  |  |
| --- | --- | --- |
|  | v~t​(w)=vt​(w).\tilde{v}\_{t}(w)=v\_{t}(w). |  |

###### Proof.

Let 𝒱{\cal V} denote the space of concave, increasing functions v​(w)v(w) which satisfy v​(w)=−∞v(w)=-\infty for w<0w<0 and where v​(w)v(w) is bounded above by 0.
For two adjacent times t0,t1=t0+δ​tt\_{0},t\_{1}=t\_{0}+\delta t in our grid
we define a solution function ϕt0,t1,w:𝒱→ℝ\phi\_{t\_{0},t\_{1},w}:{\cal V}\to\mathbb{R} by
setting

|  |  |  |
| --- | --- | --- |
|  | ϕt0,t1,w​(vt1)\phi\_{t\_{0},t\_{1},w}(v\_{t\_{1}}) |  |

to equal the supremum in ([13](https://arxiv.org/html/2511.07045v1#A3.E13 "In Lemma C.4. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")). By composing these
solution functions in the obvious way, we obtain a solution function ϕt0,t1,w\phi\_{t\_{0},t\_{1},{w}}
for any times in the grid with t0≤t1t\_{0}\leq t\_{1}.

We define a corresponding minimum budget as follows:

|  |  |  |
| --- | --- | --- |
|  | Wmin,t0,t1​(v)=sup{w∣ϕt0,t1,w​(v)=∞}.W\_{\min,t\_{0},t\_{1}}(v)=\sup\{w\mid\phi\_{t\_{0},t\_{1},w}(v)=\infty\}. |  |

Let t0,t1t\_{0},t\_{1} be adjacent times in the grid.
Given v∈𝒱v\in{\cal V} with ϕt0,t1,w​(v)\phi\_{t\_{0},t\_{1},w}(v) finite,
let (Ct0,π)∈𝒜w,t0,t1(C\_{t\_{0}},\pi)\in{\cal A}\_{w,t\_{0},t\_{1}}
be a maximizing strategy for the problem ([13](https://arxiv.org/html/2511.07045v1#A3.E13 "In Lemma C.4. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) with vt1=vv\_{t\_{1}}=v.
Suppose v′∈𝒱v^{\prime}\in{\cal V}. We have

|  |  |  |
| --- | --- | --- |
|  | |exp(−u(Ct0)δt)(−1+st0𝔼(1+v(w1(Ct0,α))))−exp(−u(γt0)δt)(−1+st0𝔼(1+v′(w1(γt0,α))))|≤A​exp⁡(−uγt0)​‖v−v′‖∞\Big|\exp\left(-u(C\_{t\_{0}})\delta t\right)\left(-1+s\_{t\_{0}}\mathbb{E}\left(1+v(w^{(C\_{t\_{0}},\alpha)}\_{1})\right)\right)-\\ \exp\left(-u(\gamma\_{t\_{0}})\delta t\right)\left(-1+s\_{t\_{0}}\mathbb{E}\left(1+v^{\prime}(w^{(\gamma\_{t\_{0}},\alpha)}\_{1})\right)\right)\Big|\\ \leq A\exp(-u\_{\gamma\_{t\_{0}}})\|v-v^{\prime}\|\_{\infty} |  |

for some constant AA.
Hence for any ϵ>0\epsilon>0 we can find δ1>0\delta\_{1}>0 such that ‖v−v′‖∞<δ1\|v-v^{\prime}\|\_{\infty}<\delta\_{1} implies

|  |  |  |
| --- | --- | --- |
|  | ϕt0,t1,w​(v′)≥ϕt0,t1,w​(v)−ϵ.\phi\_{t\_{0},t\_{1},w}(v^{\prime})\geq\phi\_{t\_{0},t\_{1},w}(v)-\epsilon. |  |

We have shown ϕt0,t1,w\phi\_{t\_{0},t\_{1},w} is lower semi-continuous in the sup\sup norm for adjacent
times t0t\_{0} and t1t\_{1}. It follows that ϕt0,t1,w\phi\_{t\_{0},t\_{1},w} is lower semi-continuous for all t0<t1t\_{0}<t\_{1}.

Given v∈𝒱v\in{\cal V} and h∈ℝh\in\mathbb{R}, define the translation

|  |  |  |
| --- | --- | --- |
|  | vh​(x)={v​(x−h)x−h≥0−∞x−h<0.=min⁡{v​(x−h),(supv)​𝟏x−h<0}v\_{h}(x)=\begin{cases}v(x-h)&x-h\geq 0\\ -\infty&x-h<0.\end{cases}=\min\{v(x-h),(\sup v){\bf 1}\_{x-h<0}\} |  |

Define ft0,t1,w,v​(h)=ϕt0,t1,w​(vh)f\_{t\_{0},t\_{1},w,v}(h)=\phi\_{t\_{0},t\_{1},w}(v\_{h}). The function v​(x,h)=vh​(x)v(x,h)=v\_{h}(x)
is concave.
Hence ft0,t1,w,vf\_{t\_{0},t\_{1},w,v}
is concave as a function of hh. If w>Wmin,t0,t1​(v)w>W\_{\min,t\_{0},t\_{1}}(v) then
0∈ri⁡ft0,t1,w,v0\in\operatorname{ri}f\_{t\_{0},t\_{1},w,v}, where ri⁡f\operatorname{ri}f denotes the relative interior of ff. Hence
ft0,t1,w,vf\_{t\_{0},t\_{1},w,v} is continuous in hh at 0.

Combining this with the lower semi-continuity result, we see that if w>Wmin,t0,t1​(v)w>W\_{\min,t\_{0},t\_{1}}(v)
then given ϵ>0\epsilon>0, we can find δ1>0\delta\_{1}>0 and δ2>0\delta\_{2}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ϕt0,t1,w​(vδ1​(x)−δ2)≥ϕt0,t1,w​(v)−ϵ.\phi\_{t\_{0},t\_{1},w}(v\_{\delta\_{1}}(x)-\delta\_{2})\geq\phi\_{t\_{0},t\_{1},w}(v)-\epsilon. |  |

Let us write vϵ​(x)v\_{\epsilon}(x) for the function vδ1​(x)−δ2v\_{\delta\_{1}}(x)-\delta\_{2}. Given a function ff
let us write Γf\Gamma\_{f} for the hypograph of ff, that is to say the set of points on or below the graph. We have Γv⊇Γvϵ\Gamma\_{v}\supseteq\Gamma\_{v\_{\epsilon}}. For any function v′∈𝒱v^{\prime}\in{\cal V} satisfying
Γv⊇Γv′⊇Γvϵ\Gamma\_{v}\supseteq\Gamma\_{v^{\prime}}\supseteq\Gamma\_{v\_{\epsilon}} we will have

|  |  |  |
| --- | --- | --- |
|  | ϕt0,t1,w​(v)≥ϕt0,t1,w​(v′)≥ϕt0,t1,w​(vϵ)≥ϕt0,t1,w​(v)−ϵ.\phi\_{t\_{0},t\_{1},w}(v)\geq\phi\_{t\_{0},t\_{1},w}(v^{\prime})\geq\phi\_{t\_{0},t\_{1},w}(v\_{\epsilon})\geq\phi\_{t\_{0},t\_{1},w}(v)-\epsilon. |  |

since it is clear that Γv⊇Γv′\Gamma\_{v}\supseteq\Gamma\_{v^{\prime}} implies ϕt0,t1,w​(v)≥ϕt0,t1,w​(v′)\phi\_{t\_{0},t\_{1},w}(v)\geq\phi\_{t\_{0},t\_{1},w}(v^{\prime}). Note that we can always find a piecewise linear approximation
between Γv\Gamma\_{v} and Γvϵ\Gamma\_{v\_{\epsilon}}.

Given a value for ϵ0\epsilon\_{0}, we may inductively extend this to a sequence of
positive ϵt{\epsilon\_{t}} for t∈𝒯t\in{\cal T}
such that if our approximation v~t\tilde{v}\_{t} satisfies
Γvt⊇Γv~t​Γ(vt)ϵt\Gamma\_{v\_{t}}\supseteq\Gamma\_{\tilde{v}\_{t}}\Gamma\_{(v\_{t})\_{\epsilon\_{t}}}
then it will automatically satisfy
Γvt−δ​t⊇Γv~t−δ​t⊇Γ(vt)ϵt−δ​t\Gamma\_{v\_{t-\delta t}}\supseteq\Gamma\_{\tilde{v}\_{t-\delta t}}\supseteq\Gamma\_{(v\_{t})\_{\epsilon\_{t-\delta t}}}.
By choosing a sufficiently fine grid we can ensure this condition is satisfied at time T−δ​tT-\delta t.
By further refinements we may ensure that it is satisfied at all times.
∎

Let us now describe in full detail how to
solve ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
given that vt1v\_{t\_{1}} is of the form used in our algorithm.
In Proposition [C.10](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem10 "Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"), we will give the formulae
necessary to solve the problem on a computer in a format that addresses
numerical overflow issues. Terms on the left hand side of the equations in the Proposition
should be stored in computer memory and can be computed without overflow issues from the terms on the right. We use infinite values for some terms as a convenient shorthand, terms such as an exponential of −∞-\infty should be interpreted in the obvious way.

To store probability values we define a bijection L:[0,1]→ℝ∪{±∞}L:[0,1]\to\mathbb{R}\cup\{\pm\infty\}
by

|  |  |  |
| --- | --- | --- |
|  | L​(u)={log⁡(2​u)u≤0.5−log⁡(2−2​u)u>0.5.L(u)=\begin{cases}\log(2u)&u\leq 0.5\\ -\log(2-2u)&u>0.5.\end{cases} |  |

We note that the GNU scientific library contains a function gsl\_sf\_log\_erfc
which computes the logarithm of the complementary error function which we can then use to compute L​(Φ)L(\Phi).

We define a function

|  |  |  |
| --- | --- | --- |
|  | u~​(y)=log⁡(u†​(ey)).\tilde{u}(y)=\log(u^{\dagger}(e^{y})). |  |

For the specific functional form

|  |  |  |
| --- | --- | --- |
|  | u​(x)={a​(x−x0)n+bx≥0−∞otherwiseu(x)=\begin{cases}a(x-x\_{0})^{n}+b&x\geq 0\\ -\infty&\text{otherwise}\end{cases} |  |

which we will use in our numerical examples, we may compute
u~\tilde{u} without experiencing
overflow errors using the formulae

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u~0​(p)\displaystyle\tilde{u}\_{0}(p) | :=1n−1​(p−log⁡(a​n)),\displaystyle:=\frac{1}{n-1}(p-\log(a\,n)), |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u~​(y)\displaystyle\tilde{u}(y) | ={log⁡(eu~0​(p))x0=0log⁡(eu~0​(p)+elog⁡(x0))x0>0log⁡(eu~0​(p)−elog⁡(−x0))u~0​(p)>log⁡(−x0)​ and ​x0<0−∞u~0​(p)≤log⁡(−x0)​ and ​x0<0.\displaystyle=\begin{cases}\log(e^{\tilde{u}\_{0}(p)})&x\_{0}=0\\ \log(e^{\tilde{u}\_{0}(p)}+e^{\log(x\_{0})})&x\_{0}>0\\ \log(e^{\tilde{u}\_{0}(p)}-e^{\log(-x\_{0})})&\tilde{u}\_{0}(p)>\log(-x\_{0})\text{ and }x\_{0}<0\\ -\infty&\tilde{u}\_{0}(p)\leq\log(-x\_{0})\text{ and }x\_{0}<0.\end{cases} |  | (24) |

We note the standard approach to computing the log of sums and differences of exponentials
without overflow issues should be used when evaluating
expressions such as this.

###### Proposition C.10.

Let vv be a concave, non-positive, increasing function
which is linear between grid points in 𝒳={x1,x2,…​xN}{\cal X}=\{x\_{1},x\_{2},\ldots x\_{N}\}
with xix\_{i} strictly increasing. Suppose also that vv is equal
to −∞-\infty on (−∞,x1)(-\infty,x\_{1}) and constant on (xN,∞)(x\_{N},\infty).
Suppose that u†u^{\dagger} is continuous and
satisfies equations ([20](https://arxiv.org/html/2511.07045v1#A3.E20 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([21](https://arxiv.org/html/2511.07045v1#A3.E21 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).

Define a decreasing sequence of points log⁡(pi)\log(p\_{i}) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(pi)={∞i=0log⁡(e−ℓ​(v​(xi))−e−ℓ​(v​(xi+1)))−log⁡(xi+1−xi)0<i<N−∞i=N.\log(p\_{i})=\begin{cases}\infty&i=0\\ \log(e^{-\ell(v(x\_{i}))}-e^{-\ell(v(x\_{i+1}))})-\log(x\_{i+1}-x\_{i})&0<i<N\\ -\infty&i=N.\end{cases} |  | (25) |

For a given value of log⁡η\log\eta, define L​(Uiη)L(U^{\eta}\_{i}) and L​(Qiη)L(Q^{\eta}\_{i}) for 0<i<N0<i<N by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L​(Uiη)\displaystyle L(U^{\eta}\_{i}) | =L​(Φ​(−12​M+1M​(log⁡(η)−r​δ​t−log⁡(pi)))),\displaystyle=L\left(\Phi\left(-\frac{1}{2}M+\frac{1}{M}\left(\log(\eta)-r\delta t-\log(p\_{i})\right)\right)\right), |  | (26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L​(Qiη)\displaystyle L(Q^{\eta}\_{i}) | =L​(Φ​(12​M+1M​(log⁡(η)−r​δ​t−log⁡(pi)))).\displaystyle=L\left(\Phi\left(\frac{1}{2}M+\frac{1}{M}\left(\log(\eta)-r\delta t-\log(p\_{i})\right)\right)\right). |  | (27) |

Define L​(U0η)=L​(Q0η)=−∞L(U^{\eta}\_{0})=L(Q^{\eta}\_{0})=-\infty and L​(UNη)=L​(QNη)=∞L(U^{\eta}\_{N})=L(Q^{\eta}\_{N})=\infty.
We may then define the quantity AηA^{\eta} by

|  |  |  |
| --- | --- | --- |
|  | Aη=log⁡(elog⁡(1−st0)+∑i=1Nelog⁡(st0)+log⁡(−v​(xi))+log⁡(elog⁡Uiη−elog⁡Ui−1η)).A^{\eta}=\log\left(e^{\log(1-s\_{t\_{0}})}+\sum\_{i=1}^{N}e^{\log(s\_{t\_{0}})+\log(-v(x\_{i}))+\log\left(e^{\log U^{\eta}\_{i}}-e^{\log U^{\eta}\_{i-1}}\right)}\right). |  |

We then have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(Cη)=u~​(log⁡(η)−log⁡(δ​t)−Aη)\log(C^{\eta})=\tilde{u}(\log(\eta)-\log(\delta t)-A^{\eta}) |  | (28) |

where CηC^{\eta} is as defined in ([11](https://arxiv.org/html/2511.07045v1#A3.E11 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).
We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(wη)=log⁡(elog⁡(Cη)+∑i=1Nelog⁡(st0)−r​δ​t+log⁡(xi)+log⁡(elog⁡Qiη−elog⁡Qi−1η))\log(w^{\eta})=\log\left(e^{\log(C^{\eta})}+\sum\_{i=1}^{N}e^{\log(s\_{t\_{0}})-r\delta t+\log(x\_{i})+\log\left(e^{\log Q^{\eta}\_{i}}-e^{\log Q^{\eta}\_{i-1}}\right)}\right) |  | (29) |

and wηw^{\eta} depends continuously upon η\eta.
If wt0>st0​e−r​δ​t​x1+γminw\_{t\_{0}}>s\_{t\_{0}}e^{-r\delta t}x\_{1}+\gamma\_{\min},
we may find the value of ηwt0\eta\_{w\_{t\_{0}}} by finding
log⁡(η)\log(\eta) such that log⁡(wη)=log⁡(wt0)\log(w^{\eta})=\log(w\_{t\_{0}}).
We then have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(v​(t0,wt0))=u​(γη)​δ​t−Aη.\displaystyle\ell(v(t\_{0},w\_{t\_{0}}))=u(\gamma^{\eta})\delta t-A^{\eta}. |  | (30) |

If wt0<st0​e−r​δ​t​x1w\_{t\_{0}}<s\_{t\_{0}}e^{-r\delta t}x\_{1}, the maximum in ([14](https://arxiv.org/html/2511.07045v1#A3.E14 "In Lemma C.6. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) is −∞-\infty which is achieved by the negative consumption γ=wt0−st0​e−r​δ​t​x1\gamma=w\_{t\_{0}}-s\_{t\_{0}}e^{-r\delta t}x\_{1}.

###### Proof.

Corresponding to ([25](https://arxiv.org/html/2511.07045v1#A3.E25 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) we have a decreasing sequence of points pip\_{i} given
by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi={∞i=0v​(xi+1)−v​(xi)xi+1−xi0<i<N0i=N.p\_{i}=\begin{cases}\infty&i=0\\ \frac{v(x\_{i+1})-v(x\_{i})}{x\_{i+1}-x\_{i}}&0<i<N\\ 0&i=N.\end{cases} |  | (31) |

We will then have

|  |  |  |
| --- | --- | --- |
|  | v†​(p)=∑i=1Nxi​𝟏[pi,pi−1)​(p).v^{\dagger}(p)=\sum\_{i=1}^{N}x\_{i}{\bf 1}\_{[p\_{i},p\_{i-1})}(p). |  |

From ([10](https://arxiv.org/html/2511.07045v1#A3.E10 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))

|  |  |  |
| --- | --- | --- |
|  | fη​(u)=∑i=1Nxi​𝟏[pi,pi−1)​(η​e−r​δ​t​qBSA​(u)).f^{\eta}(u)=\sum\_{i=1}^{N}x\_{i}{\bf 1}\_{[p\_{i},p\_{i-1})}\left(\eta e^{-r\delta t}q^{A}\_{\mathrm{BS}}(u)\right). |  |

Hence we will be able to deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | fη​(U)=∑i=1Nxi​𝟏(Ui−1η,Uiη]​(U)f^{\eta}(U)=\sum\_{i=1}^{N}x\_{i}{\bf 1}\_{(U^{\eta}\_{i-1},U^{\eta}\_{i}]}\left(U\right) |  | (32) |

if we can show ([26](https://arxiv.org/html/2511.07045v1#A3.E26 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) ensures that

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​st0​e−r​δ​t​qBSA​(Uiη)=pi.\eta s\_{t\_{0}}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(U^{\eta}\_{i})=p\_{i}. |  | (33) |

Writing ϕ\phi for the pdf of the standard normal we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | qBSA​(u)\displaystyle q^{A}\_{\mathrm{BS}}(u) | =ϕ​(M+Φ−1​(u))ϕ​(Φ−1​(u))\displaystyle=\frac{\phi(M+\Phi^{-1}(u))}{\phi(\Phi^{-1}(u))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(12​(Φ−1​(u)2−(M+Φ−1​(u))2))\displaystyle=\exp\left(\frac{1}{2}(\Phi^{-1}(u)^{2}-(M+\Phi^{-1}(u))^{2})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(−12​M2−M​Φ−1​(u)).\displaystyle=\exp\left(-\frac{1}{2}M^{2}-M\Phi^{-1}(u)\right). |  |

Hence equation ([33](https://arxiv.org/html/2511.07045v1#A3.E33 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uiη=Φ​(−12​M−1M​log⁡(1η​er​δ​t​pi)).U^{\eta}\_{i}=\Phi\left(-\frac{1}{2}M-\frac{1}{M}\log\left(\frac{1}{\eta}e^{r\delta t}p\_{i}\right)\right). |  | (34) |

for 0<i<N0<i<N, which will hold due to our definition ([26](https://arxiv.org/html/2511.07045v1#A3.E26 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).
From ([11](https://arxiv.org/html/2511.07045v1#A3.E11 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([32](https://arxiv.org/html/2511.07045v1#A3.E32 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cη\displaystyle C^{\eta} | =u†​(−ηδ​t​(−1+st0​∫01(1+v​(∑i=1Nxi​𝟏(Ui−1η,Uiη]​(s)))​ds)−1)\displaystyle=u^{\dagger}\left(-\frac{\eta}{\delta t}\left(-1+s\_{t\_{0}}\int\_{0}^{1}\left(1+v\left(\sum\_{i=1}^{N}x\_{i}{\bf 1}\_{(U^{\eta}\_{i-1},U^{\eta}\_{i}]}(s)\right)\right)\,\mathrm{d}s\right)^{-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =u†​(−ηδ​t​(−1+st0​∫01(1+∑i=1Nv​(xi)​𝟏(Ui−1η,Uiη]​(s))​ds)−1)\displaystyle=u^{\dagger}\left(-\frac{\eta}{\delta t}\left(-1+s\_{t\_{0}}\int\_{0}^{1}\left(1+\sum\_{i=1}^{N}v(x\_{i}){\bf 1}\_{(U^{\eta}\_{i-1},U^{\eta}\_{i}]}(s)\right)\,\mathrm{d}s\right)^{-1}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =u†​(−ηδ​t​(−1+st0​(1+∑i=1Nv​(xi)​(Uiη−Ui−1η)))−1).\displaystyle=u^{\dagger}\left(-\frac{\eta}{\delta t}\left(-1+s\_{t\_{0}}\left(1+\sum\_{i=1}^{N}v(x\_{i})(U^{\eta}\_{i}-U^{\eta}\_{i-1})\right)\right)^{-1}\right). |  | (35) |

Equation ([28](https://arxiv.org/html/2511.07045v1#A3.E28 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) follows immediately.

Use ([12](https://arxiv.org/html/2511.07045v1#A3.E12 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([8](https://arxiv.org/html/2511.07045v1#A3.E8 "In Definition C.2. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) to see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | wη\displaystyle w^{\eta} | =Cη+st0​∑i=1N∫Ui−1ηUiηe−r​δ​t​qBSA​(s)​xi​ds\displaystyle=C^{\eta}+s\_{t\_{0}}\sum\_{i=1}^{N}\int\_{U^{\eta}\_{i-1}}^{U^{\eta}\_{i}}e^{-r\delta t}q^{A}\_{\mathrm{BS}}(s)x\_{i}\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Cη+st0​∑i=1Ne−r​δ​t​xi​(Q​(Uiη)−Q​(Ui−1η))\displaystyle=C^{\eta}+s\_{t\_{0}}\sum\_{i=1}^{N}e^{-r\delta t}x\_{i}(Q(U^{\eta}\_{i})-Q(U^{\eta}\_{i-1})) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Cη+st0∑i=1Ne−r​δ​txi(Qiη−Qi−1η))\displaystyle=C^{\eta}+s\_{t\_{0}}\sum\_{i=1}^{N}e^{-r\delta t}x\_{i}(Q^{\eta}\_{i}-Q^{\eta}\_{i-1})) |  | (36) |

The last line follows directly from our definitions of QQ, UiηU^{\eta}\_{i} and QiηQ^{\eta}\_{i}.
We now see that equation ([36](https://arxiv.org/html/2511.07045v1#A3.E36 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) is equivalent to
([29](https://arxiv.org/html/2511.07045v1#A3.E29 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).

Our explicit formula, ([34](https://arxiv.org/html/2511.07045v1#A3.E34 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")), for CηC^{\eta} shows that it depends continuously η\eta given the assumption ([20](https://arxiv.org/html/2511.07045v1#A3.E20 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).
It then follows from equation ([36](https://arxiv.org/html/2511.07045v1#A3.E36 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) that wηw^{\eta} depends continuously on η\eta.
Lemmas ([C.11](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem11 "Lemma C.11. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([C.13](https://arxiv.org/html/2511.07045v1#A3.Ex68 "Lemma C.13. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) below then establish
that we can solve for η\eta in wη=wt0w^{\eta}=w\_{t\_{0}} under the conditions of the proposition.

The value function
is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t0,wη)\displaystyle v(t\_{0},w^{\eta}) | =exp⁡(−u​(Cη)​δ​t)​(−1+st0​∫01(1+v​(∑i=1Nxi​𝟏(Ui−1η,Uiη]​(s)))​ds)\displaystyle=\exp(-u(C^{\eta})\delta t)\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(\sum\_{i=1}^{N}x\_{i}{\bf 1}\_{(U^{\eta}\_{i-1},U^{\eta}\_{i}]}\left(s\right)))\,\mathrm{d}s\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(−u​(Cη)​δ​t)​(−1+st0​(1+∑i=1Nv​(xi)​(Uiη−Ui−1η)))\displaystyle=\exp(-u(C^{\eta})\delta t)\left(-1+s\_{t\_{0}}(1+\sum\_{i=1}^{N}v(x\_{i})(U^{\eta}\_{i}-U^{\eta}\_{i-1}))\right) |  |

and so ([30](https://arxiv.org/html/2511.07045v1#A3.E30 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) also follows.
∎

###### Lemma C.11.

Under the assumptions of Proposition [C.10](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem10 "Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"),

|  |  |  |
| --- | --- | --- |
|  | limη→0wη=∞.\lim\_{\eta\to 0}w^{\eta}=\infty. |  |

###### Proof.

Our assumptions on vv ensure that

|  |  |  |
| --- | --- | --- |
|  | −1+st0​∫01(1+v​(fη​(s)))​ds≤−1+st0<0.-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f^{\eta}(s)))\,\mathrm{d}s\leq-1+s\_{t\_{0}}<0. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | 0>(−1+st0​∫01(1+v​(fη​(s))))−1<1−1+st0.0>\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f^{\eta}(s)))\right)^{-1}<\frac{1}{-1+s\_{t\_{0}}}. |  |

It now follows from our equation ([21](https://arxiv.org/html/2511.07045v1#A3.E21 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) coupled with equation ([11](https://arxiv.org/html/2511.07045v1#A3.E11 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
that

|  |  |  |
| --- | --- | --- |
|  | limη→0Cη=∞.\lim\_{\eta\to 0}C^{\eta}=\infty. |  |

The result now follows from ([12](https://arxiv.org/html/2511.07045v1#A3.E12 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).
∎

###### Lemma C.12.

Under the assumptions of Proposition [C.10](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem10 "Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"),

|  |  |  |
| --- | --- | --- |
|  | limη→∞Cη=Cmin.\lim\_{\eta\to\infty}C^{\eta}=C\_{\min}. |  |

###### Proof.

Our assumptions on vv ensure that

|  |  |  |
| --- | --- | --- |
|  | (−1+st0​∫01(1+v​(fη​(s)))​ds)−1\left(-1+s\_{t\_{0}}\int\_{0}^{1}(1+v(f^{\eta}(s)))\,\mathrm{d}s\right)^{-1} |  |

is bounded. Hence using the expression ([11](https://arxiv.org/html/2511.07045v1#A3.E11 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
combined with assumption ([22](https://arxiv.org/html/2511.07045v1#A3.E22 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) we find Cη→0C^{\eta}\to 0
as η→∞\eta\to\infty.
∎

###### Lemma C.13.

Under the assumptions of Proposition [C.10](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem10 "Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"),

|  |  |  |
| --- | --- | --- |
|  | limη→∞wη=γmin+st0​e−r​δ​t​x1.\lim\_{\eta\to\infty}w^{\eta}=\gamma\_{\min}+s\_{t\_{0}}e^{-r\delta t}x\_{1}. |  |

###### Proof.

Define

|  |  |  |
| --- | --- | --- |
|  | p∗=inf∂v​(x1).p^{\*}=\inf\partial v(x\_{1}). |  |

For η>0\eta>0, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | sη∗=qBSA​(p∗​η−1​er​t),s^{\*}\_{\eta}=q^{A}\_{\mathrm{BS}}(p^{\*}\eta^{-1}e^{rt}), |  | (37) |

which ensures that

|  |  |  |  |
| --- | --- | --- | --- |
|  | s≥s∗⇔η​er​t​qBSA​(s)<p⋆.s\geq s^{\*}\iff\eta e^{rt}q^{A}\_{\mathrm{BS}}(s)<p^{\star}. |  | (38) |

We compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01qBSA​(s)​fη​(s)​ds\displaystyle\int\_{0}^{1}q^{A}\_{\mathrm{BS}}(s)f^{\eta}(s)\mathrm{d}s | =∫01qBSA​(s)​v†​(η​e−r​t​qBSA​(s))​ds\displaystyle=\int\_{0}^{1}q^{A}\_{\mathrm{BS}}(s)v^{\dagger}(\eta e^{-rt}q^{A}\_{\mathrm{BS}}(s))\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0sη∗qBSA​(s)​v†​(η​e−r​t​qBSA​(s))​ds\displaystyle=\int\_{0}^{s^{\*}\_{\eta}}q^{A}\_{\mathrm{BS}}(s)v^{\dagger}(\eta e^{-rt}q^{A}\_{\mathrm{BS}}(s))\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1η​e−r​t​∫sη∗1η​e−r​t​qBSA​(s)​v†​(η​e−r​t​qBSA​(s))​ds\displaystyle\qquad+\frac{1}{\eta e^{-rt}}\int\_{s^{\*}\_{\eta}}^{1}\eta e^{-rt}\,q^{A}\_{\mathrm{BS}}(s)v^{\dagger}(\eta e^{-rt}q^{A}\_{\mathrm{BS}}(s))\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫0sη∗qBSA​(s)​x1​ds\displaystyle\leq\int\_{0}^{s^{\*}\_{\eta}}q^{A}\_{\mathrm{BS}}(s)x\_{1}\,\mathrm{d}s |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1η​e−r​t​∫sη∗1η​e−r​t​qBSA​(s)​v†​(η​e−r​t​qBSA​(s))​ds\displaystyle\qquad+\frac{1}{\eta e^{-rt}}\int\_{s^{\*}\_{\eta}}^{1}\eta e^{-rt}\,q^{A}\_{\mathrm{BS}}(s)v^{\dagger}(\eta e^{-rt}q^{A}\_{\mathrm{BS}}(s))\,\mathrm{d}s |  | (39) |

We note that p∈∂v​(v†​(p))p\in\partial v(v^{\dagger}(p)).
By the definition of the subdifferential at v†​(p)v^{\dagger}(p)

|  |  |  |
| --- | --- | --- |
|  | v​(x)≤v​(v†​(p))+p​(x−v†​(p)).v(x)\leq v(v^{\dagger}(p))+p(x-v^{\dagger}(p)). |  |

Rearranging yields

|  |  |  |
| --- | --- | --- |
|  | p​v†​(p)≤p​x+v​(v†​(p))−v​(x).pv^{\dagger}(p)\leq px+v(v^{\dagger}(p))-v(x). |  |

Using the fact vv is increasing and substituting x1x\_{1} for xx we find that for all pp

|  |  |  |
| --- | --- | --- |
|  | p​v†​(p)≤p​x1+v​(xN)−v​(x1).pv^{\dagger}(p)\leq px\_{1}+v(x\_{N})-v(x\_{1}). |  |

Using this inequality in ([39](https://arxiv.org/html/2511.07045v1#A3.E39 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) we find

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01qBSA​(s)​fη​(s)​ds\displaystyle\int\_{0}^{1}q^{A}\_{\mathrm{BS}}(s)f^{\eta}(s)\mathrm{d}s | ≤∫0sη∗qBSA​(s)​x1​ds\displaystyle\leq\int\_{0}^{s^{\*}\_{\eta}}q^{A}\_{\mathrm{BS}}(s)x\_{1}\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1η​e−r​t​∫sη∗1(η​e−r​t​qBSA​(s)​x1+v​(xN)−v​(x1))​ds\displaystyle\qquad+\frac{1}{\eta e^{-rt}}\int\_{s^{\*}\_{\eta}}^{1}(\eta e^{-rt}\,q^{A}\_{\mathrm{BS}}(s)x\_{1}+v(x\_{N})-v(x\_{1}))\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫0sη∗qBSA​(s)​x1​ds\displaystyle\leq\int\_{0}^{s^{\*}\_{\eta}}q^{A}\_{\mathrm{BS}}(s)x\_{1}\,\mathrm{d}s |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1η​e−r​t​∫sη∗1(p∗​x1+v​(xN)−v​(x1))​ds.\displaystyle\qquad+\frac{1}{\eta e^{-rt}}\int\_{s^{\*}\_{\eta}}^{1}(p^{\*}x\_{1}+v(x\_{N})-v(x\_{1}))\,\mathrm{d}s. |  | (41) |

by ([38](https://arxiv.org/html/2511.07045v1#A3.E38 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")). From ([37](https://arxiv.org/html/2511.07045v1#A3.E37 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))

|  |  |  |
| --- | --- | --- |
|  | limη→∞sη∗=1.\lim\_{\eta\to\infty}s^{\*}\_{\eta}=1. |  |

We may therefore take the limit of the inequality ([41](https://arxiv.org/html/2511.07045v1#A3.E41 "In C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem"))
to find

|  |  |  |
| --- | --- | --- |
|  | lim infη>0∫01qBSA​(s)​fη​(s)​ds≤x1.\liminf\_{\eta>0}\int\_{0}^{1}q^{A}\_{\mathrm{BS}}(s)f^{\eta}(s)\mathrm{d}s\leq x\_{1}. |  |

Using this, Lemma [C.12](https://arxiv.org/html/2511.07045v1#A3.Ex66 "Lemma C.12. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem") and the definition of wηw^{\eta} in
equation ([12](https://arxiv.org/html/2511.07045v1#A3.E12 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) we find

|  |  |  |
| --- | --- | --- |
|  | lim infη>0wη≤Cmin+st0​e−r​δ​t​x1.\liminf\_{\eta>0}w^{\eta}\leq C\_{\min}+s\_{t\_{0}}e^{-r\delta t}x\_{1}. |  |

From ([11](https://arxiv.org/html/2511.07045v1#A3.E11 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) and ([12](https://arxiv.org/html/2511.07045v1#A3.E12 "In item (b) ‣ Proposition C.3. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) one sees that, on the other hand,
for all η>0\eta>0 we have

|  |  |  |
| --- | --- | --- |
|  | wη≥Cmin+st0​e−r​δ​t​x1.w^{\eta}\geq C\_{\min}+s\_{t\_{0}}e^{-r\delta t}x\_{1}. |  |

The result follows.
∎

###### Remark C.14.

We note that that if we follow the optimal investment
strategy at time tt, then the optimal investment strategy will result
in a wealth at time t+δ​tt+\delta t which takes values in the grid {x1,…,xn}\{x\_{1},\ldots,x\_{n}\}.
We may then approximate the value function on the space-time grid
{x1,…​xn}×{0,δ​t,2​δ​t,…,T}\{x\_{1},\ldots x\_{n}\}\times\{0,\delta t,2\delta t,\ldots,T\}.
One can then obtain a simulation of the optimal strategy by first simulating
the stock price on the time grid and then computing the corresponding dynamics
of xtx\_{t} in the grid {x1,…​xn}\{x\_{1},\ldots x\_{n}\} using this approximation to the value
function. Since the wealth process never leaves a fixed space-time grid, we can use
the same approximation of the value function for all the scenarios.

###### Remark C.15.

When implementing this algorithm we notice that many values
of UiηU\_{i}^{\eta} will be extremely close to either 0 or 1, and so including
these terms will have a negligible effect on the values of the sums
in the equations ([28](https://arxiv.org/html/2511.07045v1#A3.E28 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")), ([29](https://arxiv.org/html/2511.07045v1#A3.E29 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")).
Financially this is equivalent to ignoring extreme events of
very low probability where the
ℙ\mathbb{P} and ℚ\mathbb{Q} disagree by a large amount. Since our payoff functions ff
take values in 𝒳{\cal X}, and so are bounded and positive, ignoring
these extreme events will have no material impact upon either the price or the expected utility.
The value we chose in our numerical calculations was ϵ=10−10​max⁡|v​(xi)|−1\epsilon=10^{-10}\max{|v(x\_{i})|}^{-1}.

This can be used to speed up the algorithm. When
calculating wηw^{\eta}, choose some small ϵ\epsilon and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | imin\displaystyle i\_{\min} | :=max⁡{1}∪{i∣Ui<ϵ}\displaystyle:=\max\{1\}\cup\{i\mid U\_{i}<\epsilon\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | imax\displaystyle i\_{\max} | :=min⁡{N}∪{i∣Ui>1−ϵ}.\displaystyle:=\min\{N\}\cup\{i\mid U\_{i}>1-\epsilon\}. |  |

To compute these values and the values of UiU\_{i},
first use the method of bisection to find some
i∗i^{\*} where ϵ<Ui∗<1−ϵ\epsilon<U\_{i^{\*}}<1-\epsilon. Then compute the values of UiU\_{i}
from i∗i^{\*} down to imini\_{\min}, stopping when Ui<ϵU\_{i}<\epsilon. Similarly compute the values of UiU\_{i} from i∗i^{\*} up to imaxi\_{\max}, stopping when Ui>1−ϵU\_{i}>1-\epsilon.
No other values of UiU\_{i} outside the range imin−1≤i≤imaxi\_{\min-1}\leq i\leq i\_{\max} are then needed in the computation of wηw^{\eta}.

When computing the values of the sums in ([28](https://arxiv.org/html/2511.07045v1#A3.E28 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")), ([29](https://arxiv.org/html/2511.07045v1#A3.E29 "In Proposition C.10. ‣ C.2 Numerical approximation of the multi-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")) use indices running from imini\_{\min} to imaxi\_{\max} rather than form 11 to nn.

## Appendix D Proof of Lemma [C.5](https://arxiv.org/html/2511.07045v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.1 Solution to the one-period problem ‣ Appendix C A convergent algorithm for the discrete-consumption, continuous-investment problem ‣ Machine-learning a family of solutions to an optimal pension investment problem")

###### Proof.

If μ=r\mu=r, then the result is trivial. We will consider
the case μ>r\mu>r, the case μ<r\mu<r is similar.

The classification of complete markets already shows that
the Black–Scholes–Merton market over the time period [t0,t1][t\_{0},t\_{1}]
is isomorphic to a
market of this form for an appropriate choice of qAq^{A}
which we will call qBSAq^{A}\_{\mathrm{BS}}. Let
d​ℚd​ℙ\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}} denote the Radon–Nikodym derivative
of the measures ℚ\mathbb{Q} and ℙ\mathbb{P} in the Black–Scholes–Merton market.
Let Fd​ℚd​ℙF\_{\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}} denote the ℙ\mathbb{P}-measure distribution
function of the Radon–Nikodym derivative.
The classification theorem moreover gives us
an isomorphism
for both the ℙ\mathbb{P} and ℚ\mathbb{Q} measures which maps the uniformly distributed random variable U′:=Fd​ℚd​ℙ​(d​Qd​P)U^{\prime}:=F\_{\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}}(\frac{\mathrm{d}Q}{\mathrm{d}P})
to UU. In particular this tells us that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0wqBSA​(s)​ds=ℙℚA​(U≤w)=ℙℚ​(Fd​ℚd​ℙ​(U′≤w))\int\_{0}^{w}q^{A}\_{\mathrm{BS}}(s)\mathrm{d}s=\mathbb{P}\_{\mathbb{Q}^{A}}(U\leq w)=\mathbb{P}\_{\mathbb{Q}}(F\_{\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}}(U^{\prime}\leq w)) |  | (42) |

Differentiating this, we may obtain an expression for qBSAq^{A}\_{\mathrm{BS}}.

The ℙ\mathbb{P} measure distribution function of the log stock price, zt1=log⁡(St1)z\_{t\_{1}}=\log(S\_{t\_{1}}) given the log stock price zt1z\_{t\_{1}}
in the Black–Scholes–Merton model is

|  |  |  |
| --- | --- | --- |
|  | p​(z)=12​π​σ​δ​t​exp⁡(−(z−(zt0+(μ−12​σ2)​δ​t))22​σ2​δ​t).p(z)=\frac{1}{\sqrt{2\pi\sigma\delta t}}\exp\left(-\frac{(z-(z\_{t\_{0}}+(\mu-\frac{1}{2}\sigma^{2})\delta t))^{2}}{2\sigma^{2}\delta t}\right). |  |

Similarly the
ℚ\mathbb{Q} measure distribution function of zt1z\_{t\_{1}} is

|  |  |  |
| --- | --- | --- |
|  | q​(z)=12​π​σ​δ​t​exp⁡(−(z−(zt0+(r−12​σ2)​δ​t))22​σ2​δ​t).q(z)=\frac{1}{\sqrt{2\pi\sigma\delta t}}\exp\left(-\frac{(z-(z\_{t\_{0}}+(r-\frac{1}{2}\sigma^{2})\delta t))^{2}}{2\sigma^{2}\delta t}\right). |  |

The standard computation of the ℚ\mathbb{Q} measure using Girsanov’s theorem
shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚd​ℙ​(z)\displaystyle\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}(z) | =q​(z)p​(z).\displaystyle=\frac{q(z)}{p(z)}. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚd​ℙ​(z)\displaystyle\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}(z) | =exp⁡(−(z−(zt0+(r−12​σ2)​δ​t))2−(z−(zt0+(μ−12​σ2)​δ​t))22​σ2​δ​t).\displaystyle=\exp\left(-\frac{(z-(z\_{t\_{0}}+(r-\frac{1}{2}\sigma^{2})\delta t))^{2}-(z-(z\_{t\_{0}}+(\mu-\frac{1}{2}\sigma^{2})\delta t))^{2}}{2\sigma^{2}\delta t}\right). |  |

Note that the term in side the exp\exp is linear in zz, so d​ℚd​ℙ\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}
is decreasing. Hence
U′​(z)U^{\prime}(z) is decreasing, and we recall that U′U^{\prime} is uniformly distributed. Hence, U′​(z)=1−Fz​(z)U^{\prime}(z)=1-F\_{z}(z) where FzF\_{z} is the ℙ\mathbb{P}-measure
distribution function of ztz\_{t}. But conditioned on zt0z\_{t\_{0}}, zt1z\_{t\_{1}} is normally distributed with mean μ−12​σ2\mu-\tfrac{1}{2}\sigma^{2} and
standard deviation σ​δ​t\sigma\sqrt{\delta t}. Hence

|  |  |  |
| --- | --- | --- |
|  | zt1=zt0+(μ−12​σ2)​δ​t+σ​δ​t​Φ−1​(U′)z\_{t\_{1}}=z\_{t\_{0}}+(\mu-\tfrac{1}{2}\sigma^{2})\delta t+\sigma\sqrt{\delta t}\,\Phi^{-1}(U^{\prime}) |  |

where Φ\Phi is the inverse distribution function of the standard normal
distribution.

We now compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙℚ​(U′≤w)\displaystyle\mathbb{P}\_{\mathbb{Q}}(U^{\prime}\leq w) | =ℙℚ​(zt1≤zt0+(μ−12​σ2)​δ​t+σ​δ​t​Φ−1​(w))\displaystyle=\mathbb{P}\_{\mathbb{Q}}(z\_{t\_{1}}\leq z\_{t\_{0}}+(\mu-\tfrac{1}{2}\sigma^{2})\delta t+\sigma\sqrt{\delta t}\Phi^{-1}(w)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙℚ​(zt1≤zt0+(r−12​σ2)​δ​t+(μ−r)​δ​t+σ​δ​t​Φ−1​(w)).\displaystyle=\mathbb{P}\_{\mathbb{Q}}(z\_{t\_{1}}\leq z\_{t\_{0}}+(r-\tfrac{1}{2}\sigma^{2})\delta t+(\mu-r)\delta t+\sigma\sqrt{\delta t}\Phi^{-1}(w)). |  |

Since zt1z\_{t\_{1}} is normally distributed in the ℚ\mathbb{Q} measure with
mean r−12​σ2r-\tfrac{1}{2}\sigma^{2} and standard deviation σ​δ​t\sigma\sqrt{\delta t}
we find

|  |  |  |
| --- | --- | --- |
|  | ℙℚ​(U′≤w)=Φ​(|(μ−r)​δ​tσ|+Φ−1​(w)).\mathbb{P}\_{\mathbb{Q}}(U^{\prime}\leq w)=\Phi\left(\left|\frac{(\mu-r)\sqrt{\delta t}}{\sigma}\right|+\Phi^{-1}(w)\right). |  |

Combining this with ([42](https://arxiv.org/html/2511.07045v1#A4.E42 "In Appendix D Proof of Lemma C.5 ‣ Machine-learning a family of solutions to an optimal pension investment problem")), we get the result.
∎