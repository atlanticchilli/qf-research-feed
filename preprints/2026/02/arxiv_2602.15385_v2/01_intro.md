---
authors:
- Ronald Richman
- Mario V. Wüthrich
doc_id: arxiv:2602.15385v2
family_id: arxiv:2602.15385
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: From Chain-Ladder to Individual Claims Reserving
url_abs: http://arxiv.org/abs/2602.15385v2
url_html: https://arxiv.org/html/2602.15385v2
venue: arXiv q-fin
version: 2
year: 2026
---


Ronald Richman111insureAI, ronaldrichman@gmail.com
  
Mario V. Wüthrich222Department of Mathematics, ETH Zurich,
mario.wuethrich@math.ethz.ch

(Revised Version of )

###### Abstract

The chain-ladder (CL) method is the most widely used claims reserving technique in non-life insurance. This manuscript introduces a novel approach to computing the CL reserves based on a fundamental restructuring of the data utilization for the CL prediction procedure. Instead of rolling forward the cumulative claims with estimated CL factors, we estimate multi-period factors that project the latest observations directly to the ultimate claims. This alternative perspective on CL reserving creates a natural pathway for the application of machine learning techniques to individual claims reserving. As a proof of concept, we present a small-scale real data application employing neural networks for individual claims reserving.

Keywords. Claims reserving, chain-ladder method, individual claims reserving, micro-level reserving, granular reserving, neural networks, Mack’s method.

## 0 Addendum

After uploading the first version of this manuscript to arXiv, Florian Gerhardt (thank you very much!) pointed out that our main result had already been established on page 130 of Lorenz–Schmidt [[13](https://arxiv.org/html/2602.15385v2#bib.bib13)], where the approach is referred to as the grossing up method. Following the theorem in that reference, the authors remark that “…, the grossing up method is irrelevant in practice.” We believe that this assessment is too pessimistic in the era of machine learning. In our view, precisely this structural perspective may provide the key to bringing individual claims reserving into practical application. For this reason, we have chosen to leave the paper essentially unchanged, in the hope of convincing the reader that this approach offers a promising direction for future research.

## 1 Introduction

About a decade ago, research of individual claims reserving utilizing machine learning (ML) techniques began to emerge. Since then, numerous methods and models have been proposed, including regression trees, gradient boosting machines, and neural networks. Nevertheless, the area of individual claims reserving remains predominantly a research domain and has not yet achieved a widespread adoption in industry practice. Schneider–Schwab [[18](https://arxiv.org/html/2602.15385v2#bib.bib18)] write: “Typically, newer models which consider richer data on individual claims are either parametric or use machine learning techniques. However, none have become a gold standard, and advances are still needed.”
We attribute this fact to various challenges. First, it is difficult to find publicly available individual claims data. This clearly hinders research in this area of actuarial science. Second, individual claims data is censored, low-frequency and of a complex time-series structure. It is generally difficult to build good predictive models for such problems.
Third, the claims reserving problem is a multi-period forecasting problem. However, often, the underlying algorithms are only trained for performing one-period ahead forecasts. Naturally, a tweak is required to work around this problem going from one- to multi-period forecasts.
Fourth, the implementation and structure of the proposed individual claims reserving methods is rather complex and often specific to a certain claims reserving situation, for instance, every insurance company collects historic data of a slightly different nature (and format). This makes it difficult to benchmark the different methods. Moreover, the proposed approaches often need extended hyper-parameter tuning, e.g., to avoid biases, this leaves the question open whether the proposed method easily generalizes to other claims reserving situations (in a broader sense).

This paper introduces a fundamentally novel approach which we envision as a transformative step toward the widespread adoption of individual claims reserving across the insurance industry. This transformative step is not about a specific ML architecture, but our core idea is to reorganize historical individual claims data for direct multi-period forecasting. The main step is to reformulate the foundational chain-ladder (CL) reserving algorithm so that one can perform multi-period model fitting and forecasting. Once this step is fully understood, adapting this idea to ML methods is straightforward.
We will explain this in detail, after outlining the present state of the field of individual claims reserving using ML methods.

We observe four main techniques to cope with the multi-period forecasting problem in individual claims reserving:

(1) The multi-period forecasting is performed by a recursive one-period forecast procedure using past observations as inputs. Rolling this recursive procedure into the future, missing observed inputs are replaced by their forecasts. This is the first and most popular method used for multi-period forecasting; for literature in individual claims reserving see, e.g., De Felice–Moriconi [[5](https://arxiv.org/html/2602.15385v2#bib.bib5)] and Chaoubi et al. [[4](https://arxiv.org/html/2602.15385v2#bib.bib4)]. We briefly explain why this procedure may be problematic. Consider observations (Y1,…,Yt)(Y\_{1},\ldots,Y\_{t}) to forecast a next response Yt+1Y\_{t+1} at time t≥1t\geq 1. The natural forecast is given by

|  |  |  |
| --- | --- | --- |
|  | (Y1,…,Yt)↦Y^t+1:=𝔼​[Yt+1|Y1,…,Yt].(Y\_{1},\ldots,Y\_{t})~\mapsto~\widehat{Y}\_{t+1}:={\mathbb{E}}\left[\left.Y\_{t+1}\right|Y\_{1},\ldots,Y\_{t}\right]. |  |

One period later, at time t+1t+1, we have collected
observations (Y1,…,Yt+1)(Y\_{1},\ldots,Y\_{t+1}) and we build the next forecast of response Yt+1Y\_{t+1}
by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Y1,…,Yt+1)↦Y^t+2=𝔼​[Yt+2|Y1,…,Yt+1].(Y\_{1},\ldots,Y\_{t+1})~\mapsto~\widehat{Y}\_{t+2}={\mathbb{E}}\left[\left.Y\_{t+2}\right|Y\_{1},\ldots,Y\_{t+1}\right]. |  | (1.1) |

This gives a natural recursive one-period ahead forecast algorithm. The main difficulty in applying it in practice is that the observation Yt+1Y\_{t+1} is not available at time tt, and we cannot roll this algorithm into the future. The simple solution to this problem is to impute the prediction Y^t+1\widehat{Y}\_{t+1} for the missing observation Yt+1Y\_{t+1}, that is, we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Y1,…,Yt,Y^t+1)↦Y^t+2†:=𝔼​[Yt+2|Y1,…,Yt,Y^t+1].(Y\_{1},\ldots,Y\_{t},\widehat{Y}\_{t+1})~\mapsto~\widehat{Y}^{\dagger}\_{t+2}:={\mathbb{E}}\left[Y\_{t+2}\left|Y\_{1},\ldots,Y\_{t},\widehat{Y}\_{t+1}\right]\right.. |  | (1.2) |

However, in general, this proposal of multi-period forecasting is inappropriate. We give an example. Assume that all responses are binary, Yt∈{0,1}Y\_{t}\in\{0,1\}, t≥1t\geq 1. Thus, the conditional expectation in ([1.1](https://arxiv.org/html/2602.15385v2#S1.E1 "In 1 Introduction ‣ From Chain-Ladder to Individual Claims Reserving")) is based on binary observations
(Y1,…,Yt,Yt+1)∈{0,1}t+1(Y\_{1},\ldots,Y\_{t},Y\_{t+1})\in\{0,1\}^{t+1}, and so is the ML model that is trained to approximate the forecast ([1.1](https://arxiv.org/html/2602.15385v2#S1.E1 "In 1 Introduction ‣ From Chain-Ladder to Individual Claims Reserving")). However, the forecast
Y^t+1∈[0,1]\widehat{Y}\_{t+1}\in[0,1] imputed in ([1.2](https://arxiv.org/html/2602.15385v2#S1.E2 "In 1 Introduction ‣ From Chain-Ladder to Individual Claims Reserving")) can take any value in the unit interval, e.g.,
Y^t+1=0.46\widehat{Y}\_{t+1}=0.46, and the forecast model ([1.1](https://arxiv.org/html/2602.15385v2#S1.E1 "In 1 Introduction ‣ From Chain-Ladder to Individual Claims Reserving")) does not know how to deal with this input value, because it has never seen a value different from zero or one before (because it only learned to deal with binary inputs).

(2) A workaround of the problem discussed in item (1) is to learn a full simulation model from which one can simulate Yt+1Y\_{t+1}, given Y1,…,YtY\_{1},\ldots,Y\_{t}. This then allows one to perform a Monte Carlo simulation extrapolation. This is the solution applied, e.g., in
Wüthrich [[21](https://arxiv.org/html/2602.15385v2#bib.bib21)] and Delong et al. [[6](https://arxiv.org/html/2602.15385v2#bib.bib6)]. The main disadvantage of this approach clearly is that we need an accurate simulation model. If the responses YtY\_{t} contain, e.g., claims payments, claims incurred and other stochastic processes, this is clearly beyond our modeling capabilities.

(3) The works of Kuo [[9](https://arxiv.org/html/2602.15385v2#bib.bib9), [10](https://arxiv.org/html/2602.15385v2#bib.bib10)] present sequence-to-sequence forecasting methods, and the approach presented by Gabrielli [[7](https://arxiv.org/html/2602.15385v2#bib.bib7)] uses a rather similar technique. These approaches mask missing observations, and the predictive model learns to perform forecasting under incomplete information, e.g., it tries to directly predict Yt+2Y\_{t+2}, given (Y1,…,Yt)(Y\_{1},\ldots,Y\_{t}), by learning from all available information. This is a very suitable proposal. In practical applications, the main difficulty of this approach lies in controlling and mitigating potential biases during model training. Our proposal possesses this problem too, but we will see that expert intervention is rather easy in our approach.

(4) Finally, an other option is to directly predict the ultimate claims from the available information. There are two approaches in the literature that consider this option. The first one is related to survival analysis that properly accounts for censored information. This has been considered, e.g., in Lopez et al. [[12](https://arxiv.org/html/2602.15385v2#bib.bib12), [11](https://arxiv.org/html/2602.15385v2#bib.bib11)], Bladt–Pittarello [[2](https://arxiv.org/html/2602.15385v2#bib.bib2)], Hiabu et al. [[8](https://arxiv.org/html/2602.15385v2#bib.bib8)] or Turcotte–Shi [[20](https://arxiv.org/html/2602.15385v2#bib.bib20)]. The second method of a direct ultimate claim prediction uses reinforcement learning to optimally update the forecast based on the incoming information; see Avanzi et al. [[1](https://arxiv.org/html/2602.15385v2#bib.bib1)]

Our proposal aligns with option (4) of directly forecasting the ultimate claims, but the construction of our ultimate claim predictor is rather different from the two proposals above. Our starting point is the classic CL method.
Usually, the CL method is rather accurate on aggregate claims – verified by its successful use over many decades – and the CL method is very simple in its use, not very prone to biases, easy to handle and easy to manipulate by expert knowledge. Our main contribution is to restructure the estimation of the CL factors. This reshapes the estimation procedure such that it can naturally be extended to ML methods on individual claims. Thus, our contribution is this novel representation of the CL estimation and not the ML method itself. In fact, to keep things simple we select an elementary neural network architecture in our example. We believe that our proposal widely opens the door for a natural pathway of ML applications to individual claims reserving. A few immediate advantageous over the existing methods are the following: (i) Our proposal can deal with any sort of stochastic dynamic covariates such as claims incurred or multiple payment processes of several injured people. (ii) It is a natural next step beyond the CL algorithm. This means that the basis is the CL method and our approach can easily be regularized using the CL predictor to control for biases. (iii) It can easily be extended to cash-flow forecasting in the sense of sequence-to-sequence methods as stated in item (3) above. In summary, the main advantage of starting from a CL structure is that the CL results give the guardrails for the ML predictions.

A limitation that we should mention is that our proposal only considers
reported but not settled (RBNS) claims. This is common to most research in individual claims reserving, i.e., claims need to be reported so that their individual claims history is available for the use of the prediction of their further development. Incurred but not reported (IBNR) claims need to be forecast in addition, e.g., by a suitable frequency-severity reserving model.

Organization of the manuscript.
In Section [2](https://arxiv.org/html/2602.15385v2#S2 "2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"), we revisit Mack’s CL model [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)], and we present our main technical results that gives an alternative version of estimating the CL reserves. Section [3](https://arxiv.org/html/2602.15385v2#S3 "3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving") takes this alternative version to present a natural extension to individual claims reserving.
In Section [4](https://arxiv.org/html/2602.15385v2#S4 "4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"), we study two small-scale real data examples that serve as proof of concept of our proposal. Finally, in Section
[5](https://arxiv.org/html/2602.15385v2#S5 "5 Summary and next steps ‣ From Chain-Ladder to Individual Claims Reserving") we conclude and we give a list of next steps to lift this proposal to its full power for individual claims reserving. The mathematical proofs are given in the appendix.

## 2 Chain-ladder method

### 2.1 Mack’s distribution-free chain-ladder model

We start by revisiting Mack’s distribution-free CL model [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)]. Denote cumulative payments for claims in accident period i∈{1,…,I}i\in\{1,\ldots,I\} and with development delay j∈{0,…,J}j\in\{0,\ldots,J\} by Ci,jC\_{i,j}, and assume that these cumulative payments are strictly positive for all pairs (i,j)(i,j). Assume I>JI>J, i.e., at least one accident period is fully observed (developed), and the goal is to predict the ultimate claims Ci,JC\_{i,J} of accident periods i>I−Ji>I-J at time II.

###### Model Assumptions 2.1 (CL model)

The cumulative payment processes (Ci,j)0≤j≤J(C\_{i,j})\_{0\leq j\leq J} of different accident periods i∈{1,…,I}i\in\{1,\ldots,I\} are independent.
There exist positive parameters (fj)j=0J−1(f\_{j})\_{j=0}^{J-1} and (σj2)j=0J−1(\sigma^{2}\_{j})\_{j=0}^{J-1}
such that for all i∈{1,…,I}i\in\{1,\ldots,I\} and j∈{0,…,J−1}j\in\{0,\ldots,J-1\} the following holds

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Ci,j+1|Ci,0,…,Ci,j]\displaystyle{\mathbb{E}}\left[\left.C\_{i,j+1}\right|C\_{i,0},\ldots,C\_{i,j}\right] | =\displaystyle= | fj​Ci,j,\displaystyle f\_{j}\,C\_{i,j}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​(Ci,j+1|Ci,0,…,Ci,j)\displaystyle{\rm Var}\left(\left.C\_{i,j+1}\right|C\_{i,0},\ldots,C\_{i,j}\right) | =\displaystyle= | σj2​Ci,j.\displaystyle\sigma^{2}\_{j}\,C\_{i,j}. |  |

An easy consequence of these assumptions is that one can compute the conditionally expected ultimate claims Ci,JC\_{i,J} of accident periods i>I−Ji>I-J at time II as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Ci,J|Ci,0,…,Ci,I−i]=Ci,I−i​∏l=I−iJ−1fl,{\mathbb{E}}\left[\left.C\_{i,J}\right|C\_{i,0},\ldots,C\_{i,I-i}\right]=C\_{i,I-i}\prod\_{l=I-i}^{J-1}f\_{l}, |  | (2.1) |

where Ci,0,…,Ci,I−iC\_{i,0},\ldots,C\_{i,I-i} are the cumulative payments of accident period ii that are observed at time II, i.e., the cumulative payments Ci,jC\_{i,j} with indices i+j≤Ii+j\leq I. This reflects the observed upper triangle333The shape of the observed cumulative payments (Ci,j)i+j≤I(C\_{i,j})\_{i+j\leq I}, is a triangle for I=J+1I=J+1 and it is a trapezoid for I>J+1I>J+1. To simplify language we generally speak about triangles, even if the shape is a trapezoid. This is common practice in claims reserving. at time II.

To apply the CL method for reserving, there remains the estimation of the (unknown) CL factors (fj)j=0J−1(f\_{j})\_{j=0}^{J-1}. At time II, these CL factors are commonly estimated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^j=∑i=1I−j−1Ci,j+1∑i=1I−j−1Ci,j.\widehat{f}\_{j}=\frac{\sum\_{i=1}^{I-j-1}C\_{i,j+1}}{\sum\_{i=1}^{I-j-1}C\_{i,j}}. |  | (2.2) |

This motivates the CL predictors for accident periods i>I−Ji>I-J at time II

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^i,J=Ci,I−i​∏l=I−iJ−1f^l.\widehat{C}\_{i,J}=C\_{i,I-i}\prod\_{l=I-i}^{J-1}\widehat{f}\_{l}. |  | (2.3) |

This is the classic CL predictor. It is unbiased for the (conditionally) expected ultimate claim; see Mack [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)] and Wüthrich–Merz [[23](https://arxiv.org/html/2602.15385v2#bib.bib23), Lemma 3.3].
We next give a different representation of the CL predictor C^i,J\widehat{C}\_{i,J}, i>I−Ji>I-J, and this will pave the way to individual claims reserving utilizing ML techniques.

### 2.2 Recursive chain-ladder factor estimation

We can interpret the prediction in ([2.3](https://arxiv.org/html/2602.15385v2#S2.E3 "In 2.1 Mack’s distribution-free chain-ladder model ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")) as a forward-path estimation of the conditionally expected ultimate claim ([2.1](https://arxiv.org/html/2602.15385v2#S2.E1 "In 2.1 Mack’s distribution-free chain-ladder model ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")). This can be seen as follows

|  |  |  |
| --- | --- | --- |
|  | C^i,J=Ci,I−i​∏l=I−iJ−1f^l=Ci,I−i⋅f^I−i⏟I−i→I−i+1⋅f^I−i+1⏟I−i→I−i+2⋅…⋅f^J−1.\widehat{C}\_{i,J}~=~C\_{i,I-i}\prod\_{l=I-i}^{J-1}\widehat{f}\_{l}~=~\underbrace{\underbrace{C\_{i,I-i}\cdot\widehat{f}\_{I-i}}\_{I-i~\to~I-i+1}\,\cdot\,\widehat{f}\_{I-i+1}}\_{I-i~\to~I-i+2}\,\cdot\,\ldots\,\cdot\,\widehat{f}\_{J-1}. |  |

Thus, this is a step-wise (one-period ahead) roll forward extrapolation of Ci,I−iC\_{i,I-i} using the CL factor estimates (f^l)l=I−iJ−1(\widehat{f}\_{l})\_{l=I-i}^{J-1} – this is precisely the meaning of chain-ladder extrapolation, see Figure [1](https://arxiv.org/html/2602.15385v2#S2.F1 "Figure 1 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving").

![Refer to caption](CL1.png)


Figure 1: Step-wise roll forward (chain-ladder) extrapolation to predict the ultimate claims Ci,JC\_{i,J} using observations Ci,I−iC\_{i,I-i}, i>I−Ji>I-J, at time II (for I=7I=7 and J=6J=6).

We now give a different, recursive version that provides us with the same CL predictor by performing a one-shot ultimate prediction. Define the projection-to-ultimate (PtU) factors as follows

|  |  |  |
| --- | --- | --- |
|  | Fj:=∏l=jJ−1fl for j∈{0,…,J−1}.F\_{j}:=\prod\_{l=j}^{J-1}f\_{l}\qquad\text{ for $j\in\{0,\ldots,J-1\}$.} |  |

Naturally, the following identity holds

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Ci,J|Ci,0,…,Ci,I−i]=Ci,I−i​∏l=I−iJ−1fl=Ci,I−i​FI−i.{\mathbb{E}}\left[\left.C\_{i,J}\right|C\_{i,0},\ldots,C\_{i,I-i}\right]~=~C\_{i,I-i}\prod\_{l=I-i}^{J-1}f\_{l}~=~C\_{i,I-i}\,F\_{I-i}. |  |

The novel approach that we propose is to directly estimate these PtU factors (Fj)j=0J−1(F\_{j})\_{j=0}^{J-1}.
For this, we begin by introducing a new notation for the ultimate claims that are fully observed at time II, this will simplify the notation in the recursion below. Set

|  |  |  |
| --- | --- | --- |
|  | C^i,J∗=Ci,J for all i∈{1,…,I−J}.\widehat{C}^{\*}\_{i,J}=C\_{i,J}\qquad\text{ for all $i\in\{1,\ldots,I-J\}$.} |  |

We emphasize that these variables are all observed at time II; they correspond to the fully developed accident periods at time II.

(a) Initialization.
We perform the estimation procedure of the PtU factors (Fj)j=0J−1(F\_{j})\_{j=0}^{J-1} recursively starting from the upper-right corner of the claims reserving triangle.
We estimate the PtU factor of the last development period j=J−1j=J-1 by

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^J−1=f^J−1=∑i=1I−JC^i,J∗∑i=1I−JCi,J−1 and C^I−J+1,J∗=CI−J+1,J−1​F^J−1.\widehat{F}\_{J-1}=\widehat{f}\_{J-1}=\frac{\sum\_{i=1}^{I-J}\widehat{C}^{\*}\_{i,J}}{\sum\_{i=1}^{I-J}C\_{i,J-1}}\qquad\text{ and }\qquad\widehat{C}^{\*}\_{I-J+1,J}=C\_{I-J+1,J-1}\,\widehat{F}\_{J-1}. |  | (2.4) |

(b) Iteration. The estimation is extrapolated recursively from j+1→jj+1\to j by setting

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^j=∑i=1I−j−1C^i,J∗∑i=1I−j−1Ci,j and C^I−j,J∗=CI−j,j​F^j,\widehat{F}\_{j}=\frac{\sum\_{i=1}^{I-j-1}\widehat{C}^{\*}\_{i,J}}{\sum\_{i=1}^{I-j-1}C\_{i,j}}\qquad\text{ and }\qquad\widehat{C}^{\*}\_{I-j,J}=C\_{I-j,j}\,\widehat{F}\_{j}, |  | (2.5) |

for j∈{0,…,J−2}j\in\{0,\ldots,J-2\}.

![Refer to caption](CL2.png)


Figure 2: Backward extrapolation to predict the ultimate claims Ci,JC\_{i,J}, i>I−Ji>I-J, using the estimated PtU factor estimates (F^j)j=0J−1(\widehat{F}\_{j})\_{j=0}^{J-1}: (left-middle-right) correspond to j=J−1=5j=J-1=5, j=4j=4 and j=3j=3.

The estimation of the forecast process ([2.4](https://arxiv.org/html/2602.15385v2#S2.E4 "In 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"))-([2.5](https://arxiv.org/html/2602.15385v2#S2.E5 "In 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")) starts in the upper-right corner of the claims reserving triangle j=J−1j=J-1, see Figure [2](https://arxiv.org/html/2602.15385v2#S2.F2 "Figure 2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"). Then it moves recursively j+1→jj+1\to j along the last observed diagonal to the most recent accident period i=Ii=I (j=0j=0) by directly predicting the ultimate claims using ([2.5](https://arxiv.org/html/2602.15385v2#S2.E5 "In 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")).

###### Proposition 2.2

C^i,J∗=C^i,J\widehat{C}^{\*}\_{i,J}=\widehat{C}\_{i,J} for all accident periods i∈{I−J+1,…,I}i\in\{I-J+1,\ldots,I\}.

The proof of this proposition is given in the appendix, and this is the result proved in Lorenz–Schmidt [[13](https://arxiv.org/html/2602.15385v2#bib.bib13)].

The exciting fact stated in Proposition [2.2](https://arxiv.org/html/2602.15385v2#S2.Thmtheo2 "Proposition 2.2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving") is that both algorithms – the step-wise roll forward CL extrapolation of Figure [1](https://arxiv.org/html/2602.15385v2#S2.F1 "Figure 1 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving") and the backward extrapolation of Figure [2](https://arxiv.org/html/2602.15385v2#S2.F2 "Figure 2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving") – lead to the identical CL reserves. We give some remarks.

* •

  Both algorithms shown in Figures [1](https://arxiv.org/html/2602.15385v2#S2.F1 "Figure 1 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving") and [2](https://arxiv.org/html/2602.15385v2#S2.F2 "Figure 2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving") use the identical information and they provide the identical forecasts. We can view this as an optimal use of triangular information because every observed cumulative payment Ci,jC\_{i,j}, i+j≤Ii+j\leq I, is used whenever it is appropriate. This is different, e.g., from the bootstrap of individual claims histories of Rosenlund [[17](https://arxiv.org/html/2602.15385v2#bib.bib17)] who bases his model learning procedure only on claims with fully observed trajectories.
* •

  The claims reserving problem is a typical situation of censored observations, with the additional difficulty that different (censored) observations have different maturity. This gives the close connection to survival analysis. We mention the Kaplan–Meier weighting method considered in Lopez et al. [[12](https://arxiv.org/html/2602.15385v2#bib.bib12), [11](https://arxiv.org/html/2602.15385v2#bib.bib11)] to correct for censored claims information, although the method in these references is not directly applicable to claims reserving because cumulative claims payments are assumed to be proportional to time to settlement. Other survival analysis papers of a similar nature are Hiabu et al. [[8](https://arxiv.org/html/2602.15385v2#bib.bib8)] – this paper considers survival analysis for IBNR prediction using a CL forward path – and Bladt–Pittarello [[2](https://arxiv.org/html/2602.15385v2#bib.bib2)] use the Aalen–Johansen estimator in a multi-state process on a finite state space.

### 2.3 Chain-ladder RBNS reserving

The ultimate claim predictions C^i,J\widehat{C}\_{i,J} of the CL algorithm cover both the RBNS and the IBNR claims.
Our first modification is to only predict ultimates of RBNS claims at time II; by RBNS claim we denote any reported claim at time II which can either be a closed or an open one (i.e., we allow for re-openings in this definition).
We label individual claims by ν\nu, separately for each occurrence period i∈{1,…,I}i\in\{1,\ldots,I\}.
Let Ci,j|νC\_{i,j|\nu} denote the cumulative payments of the ν\nu-th claim of occurrence period ii after development period jj (since occurrence). We can then write for the aggregate cumulative payments

|  |  |  |
| --- | --- | --- |
|  | Ci,j=∑ν:Ti|ν≤jCi,j|ν,C\_{i,j}=\sum\_{\nu:\,T\_{i|\nu}\leq j}C\_{i,j|\nu}, |  |

where the sum runs over all claims ν\nu of accident period ii that are reported at time i+ji+j, and
Ti|ν∈{0,…,J}T\_{i|\nu}\in\{0,\ldots,J\} denotes the reporting delay of the ν\nu-th claim of accident period ii.

The reported claims at time II are characterized by i+Ti|ν≤Ii+T\_{i|\nu}\leq I and the IBNR claims by
i+Ti|ν>Ii+T\_{i|\nu}>I. We now focus on RBNS reserves that only involve reported claims. For this we define a version of the PtU factor estimates (F^j(r))j=0J−1(\widehat{F}^{(r)}\_{j})\_{j=0}^{J-1} that only consider the reported claims in the corresponding periods.

(a) Initialization. We set C^i,J|ν(r)=Ci,J|ν\widehat{C}^{(r)}\_{i,J|\nu}=C\_{i,J|\nu} for all claims ν\nu with accident dates i≤I−Ji\leq I-J; these claims are fully developed.
We then initialize for j=J−1j=J-1

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^J−1(r)=∑i=1I−J∑ν:Ti|ν≤J−1C^i,J|ν(r)∑i=1I−J∑ν:Ti|ν≤J−1Ci,J−1|ν and C^I−J+1,J|ν(r)=CI−J+1,J−1|ν​F^J−1(r),\widehat{F}^{(r)}\_{J-1}=\frac{\sum\_{i=1}^{I-J}\sum\_{\nu:\,T\_{i|\nu}\leq J-1}\widehat{C}^{(r)}\_{i,J|\nu}}{\sum\_{i=1}^{I-J}\sum\_{\nu:\,T\_{i|\nu}\leq J-1}C\_{i,J-1|\nu}}\qquad\text{ and }\qquad\widehat{C}^{(r)}\_{I-J+1,J|\nu}=C\_{I-J+1,J-1|\nu}\,\widehat{F}^{(r)}\_{J-1}, |  | (2.6) |

for all reported claims ν\nu of accident period I−J+1I-J+1, i.e., with reporting delay TI−J+1|ν≤J−1T\_{I-J+1|\nu}\leq J-1. The PtU factor estimate F^J−1(r)\widehat{F}^{(r)}\_{J-1}
only considers claims that have a reporting delay less or equal to J−1J-1, thus, in the numerator and the nominator of the PtU factor estimate F^J−1(r)\widehat{F}^{(r)}\_{J-1} we consider the identical cohort of reported claims.
Thus, this is a consistent consideration of reported claims extrapolation.

(b) Iteration.
This is recursively extended from j+1→j∈{0,…,J−2}j+1\to j\in\{0,\ldots,J-2\} by setting

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^j(r)=∑i=1I−j−1∑ν:Ti|ν≤jC^i,J|ν(r)∑i=1I−j−1∑ν:Ti|ν≤jCi,j|ν and C^I−j,J|ν(r)=CI−j,j|ν​F^j(r),\widehat{F}^{(r)}\_{j}=\frac{\sum\_{i=1}^{I-j-1}\sum\_{\nu:\,T\_{i|\nu}\leq j}\widehat{C}^{(r)}\_{i,J|\nu}}{\sum\_{i=1}^{I-j-1}\sum\_{\nu:\,T\_{i|\nu}\leq j}C\_{i,j|\nu}}\qquad\text{ and }\qquad\widehat{C}^{(r)}\_{I-j,J|\nu}=C\_{I-j,j|\nu}\,\widehat{F}^{(r)}\_{j}, |  | (2.7) |

for all reported claims ν\nu of accident period I−jI-j, i.e., with reporting delay TI−j|ν≤jT\_{I-j|\nu}\leq j.
Again, in the numerator and the nominator of the PtU factor estimate F^J−1(r)\widehat{F}^{(r)}\_{J-1} we consider the identical cohort of reported claims ν\nu, i.e., with Ti|ν≤jT\_{i|\nu}\leq j.
We can also interpret this of having a moving
target

|  |  |  |
| --- | --- | --- |
|  | ∑ν:Ti|ν≤jC^i,J|ν(r),\sum\_{\nu:\,T\_{i|\nu}\leq j}\widehat{C}^{(r)}\_{i,J|\nu}, |  |

in the numerators of ([2.7](https://arxiv.org/html/2602.15385v2#S2.E7 "In 2.3 Chain-ladder RBNS reserving ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")) as this claims cohort is decreasing for decreasing jj due increasingly many IBNR claims Ti|ν>jT\_{i|\nu}>j for decreasing jj.

We would like to highlight the similarity of our proposal to Schnieper’s model [[19](https://arxiv.org/html/2602.15385v2#bib.bib19)], although the estimation procedures differ. Schnieper’s model separates RBNS from IBNR claims similarly to our PtU estimation, but Schnieper’s estimation of the development factors contains reserves for IBNR claims (once they are reported), whereas our estimation procedure ([2.7](https://arxiv.org/html/2602.15385v2#S2.E7 "In 2.3 Chain-ladder RBNS reserving ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")) fixes the claims cohort and projects it directly to its ultimates C^i,J|ν(r)\widehat{C}^{(r)}\_{i,J|\nu} without including reserves for additional late reported claims.

## 3 Individual ultimate prediction using machine learning

The recursive formulas ([2.6](https://arxiv.org/html/2602.15385v2#S2.E6 "In 2.3 Chain-ladder RBNS reserving ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"))-([2.7](https://arxiv.org/html/2602.15385v2#S2.E7 "In 2.3 Chain-ladder RBNS reserving ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")) give the intuition for how the CL method can be extended to an individual claims ML method using any available input information. Denote the settlement process of claim ν\nu of accident period ii by 𝒞i|ν:=(Ci,l|ν,𝑿i,l|ν)l=0J{\cal C}\_{i|\nu}:=(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J},
where (𝑿i,l|ν)l=0J(\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J} can be any claims feature process that may involve static covariates that are known at reporting (like claim type or business line), deterministic dynamic covariates (like settlement delay) and stochastic dynamic covariates (like claims incurred process or claim status process for open/closed claims).
We emphasize that this latter information typically is not fully known at time II for RBNS claims with accident dates i>I−Ji>I-J as it stochastically evolves into the future, and one may want to consider its stochastic modeling and prediction as well. The exciting fact about our method presented below is that extrapolation of the claims feature process is not necessary!

### 3.1 Recursive individual claims reserving

Assumption. We assume that the individual claims processes 𝒞i|ν{\cal C}\_{i|\nu} are independent, and that they are conditionally i.i.d., given the static covariates known at reporting.

To comply with the previous assumption it may require to adjust some of the dynamic quantities with inflation indices (e.g., payments, incurred and case reserves). For late reported RBNS claims, we mask the covariate process part of (𝑿i,l|ν)l=0J(\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J} that refers to time periods j<Ti|νj<T\_{i|\nu} before reporting.

We now present a recursive forecast procedure for individual claims that in its methodology is equivalent to ([2.6](https://arxiv.org/html/2602.15385v2#S2.E6 "In 2.3 Chain-ladder RBNS reserving ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"))-([2.7](https://arxiv.org/html/2602.15385v2#S2.E7 "In 2.3 Chain-ladder RBNS reserving ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")).

(a) Initialization. We start with accident period I−J+1I-J+1 or, equivalently, development period j=J−1j=J-1. For all claims ν\nu that have occurred in accident periods i≤I−Ji\leq I-J, the stochastic processes 𝒞i|ν=(Ci,l|ν,𝑿i,l|ν)l=0J{\cal C}\_{i|\nu}=(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J} are fully observed, and we aim at predicting the ultimates CI−(J−1),J|νC\_{I-(J-1),J|\nu} of all claims in the next accident period I−J+1I-J+1. These claims are reported at time II, thus, they have reporting delay TI−(J−1)|ν≤J−1T\_{I-(J-1)|\nu}\leq J-1, and we have observed their claims histories (CI−(J−1),l|ν,𝑿I−(J−1),l|ν)l=0J−1(C\_{I-(J-1),l|\nu},\boldsymbol{X}\_{I-(J-1),l|\nu})\_{l=0}^{J-1}.

To bring the learning data into the same shape, we are only allowed to consider those claims that have been reported before settlement delay JJ. This gives us the learning data to perform the initial learning step

|  |  |  |
| --- | --- | --- |
|  | ℒJ−1={(Ci,J|ν,(Ci,l|ν,𝑿i,l|ν)l=0J−1);i≤I−J​ and ​Ti|ν≤J−1}.{\cal L}\_{J-1}=\left\{\left(C\_{i,J|\nu},(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J-1}\right);\,i\leq I-J\text{ and }T\_{i|\nu}\leq J-1\right\}. |  |

Based on this learning data ℒJ−1{\cal L}\_{J-1}, we build the regression function

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ci,l|ν,𝑿i,l|ν)l=0J−1↦μJ−1​((Ci,l|ν,𝑿i,l|ν)l=0J−1)=𝔼​[Ci,J|ν|(Ci,l|ν,𝑿i,l|ν)l=0J−1].(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J-1}~\mapsto~\mu\_{J-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J-1}\right)={\mathbb{E}}\left[C\_{i,J|\nu}\left|(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{J-1}\right]\right.. |  | (3.1) |

This regression function μJ−1​(⋅)\mu\_{J-1}(\cdot) describes the forecast step J−1→JJ-1\to J, and it allows us to predict the ultimates for the claims ν\nu of accident period i=I−J+1i=I-J+1, with observed claims histories
(CI−J+1,l|ν,𝑿I−J+1,l|ν)l=0J−1(C\_{I-J+1,l|\nu},\boldsymbol{X}\_{I-J+1,l|\nu})\_{l=0}^{J-1}. In particular, we can compute the forecast (assuming stationary along the occurrence period axis ii)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C^I−(J−1),J|ν\displaystyle\widehat{C}\_{I-(J-1),J|\nu} | :=\displaystyle:= | μJ−1​((CI−(J−1),l|ν,𝑿I−(J−1),l|ν)l=0J−1)\displaystyle\mu\_{J-1}\left((C\_{I-(J-1),l|\nu},\boldsymbol{X}\_{I-(J-1),l|\nu})\_{l=0}^{J-1}\right) |  |
|  |  | =\displaystyle= | 𝔼​[CI−(J−1),J|ν|(CI−(J−1),l|ν,𝑿I−(J−1),l|ν)l=0J−1].\displaystyle{\mathbb{E}}\left[C\_{I-(J-1),J|\nu}\left|(C\_{I-(J-1),l|\nu},\boldsymbol{X}\_{I-(J-1),l|\nu})\_{l=0}^{J-1}\right]\right.. |  |

We append these predictions to the observed claims histories for accident period I−J+1I-J+1

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞^I−(J−1)|ν:=((CI−(J−1),l|ν,𝑿I−(J−1),l|ν)l=0J−1,C^I−(J−1),J|ν).\widehat{\cal C}\_{I-(J-1)|\nu}:=\left((C\_{I-(J-1),l|\nu},\boldsymbol{X}\_{I-(J-1),l|\nu})\_{l=0}^{J-1},\,\widehat{C}\_{I-(J-1),J|\nu}\right). |  | (3.2) |

This initializes the recursion, and it reflects the figure on the left-hand side
of Figure [2](https://arxiv.org/html/2602.15385v2#S2.F2 "Figure 2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving").

(b) Iteration. We recursively extend this from j+1→j∈{0,…,J−2}j+1\to j\in\{0,\ldots,J-2\} or, equivalently, to accident period I−jI-j. The stochastic processes 𝒞i|ν{\cal C}\_{i|\nu} are fully observed for accident periods i≤I−Ji\leq I-J, and for accident periods I−(J−1)≤i≤I−(j+1)I-(J-1)\leq i\leq I-(j+1), we have partially observed claims histories 𝒞^i|ν\widehat{\cal C}\_{i|\nu} including an appended ultimate claim forecast C^i,J|ν\widehat{C}\_{i,J|\nu}. The goal is to extend this to the claims ν\nu of accident period I−jI-j, which have a reporting delay TI−j|ν≤jT\_{I-j|\nu}\leq j and observed claims histories (CI−j,l|ν,𝑿I−j,l|ν)l=0j(C\_{I-j,l|\nu},\boldsymbol{X}\_{I-j,l|\nu})\_{l=0}^{j} at time II.

We select the learning dataset such that it aligns with the maximal reporting lag of the RBNS claims of accident period I−jI-j at time II to build consistent claims cohorts

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ℒj\displaystyle{\cal L}\_{j} | =\displaystyle= | {(Ci,J|ν,(Ci,l|ν,𝑿i,l|ν)l=0j);i≤I−J​ and ​Ti|ν≤j}\displaystyle\left\{\left(C\_{i,J|\nu},(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right);\,i\leq I-J\text{ and }T\_{i|\nu}\leq j\right\} |  | (3.3) |
|  |  |  | ∪{(C^i,J|ν,(Ci,l|ν,𝑿i,l|ν)l=0j);I−(J−1)≤i≤I−(j+1)​ and ​Ti|ν≤j}.\displaystyle\cup\,\left\{\left(\widehat{C}\_{i,J|\nu},(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right);\,I-(J-1)\leq i\leq I-(j+1)\text{ and }T\_{i|\nu}\leq j\right\}.\qquad |  |

Based on this learning data ℒJ−1{\cal L}\_{J-1}, we build the regression function, which for the fully developed claims of accident periods i≤I−Ji\leq I-J considers

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ci,l|ν,𝑿i,l|ν)l=0j↦μj​((Ci,l|ν,𝑿i,l|ν)l=0j)=𝔼​[Ci,J|ν|(Ci,l|ν,𝑿i,l|ν)l=0j],(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}~\mapsto~\mu\_{j}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right)={\mathbb{E}}\left[C\_{i,J|\nu}\left|(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right]\right., |  | (3.4) |

this predicts from development period j→Jj\to J. For the claims of accident periods
I−(J−1)≤i≤I−(j+1)I-(J-1)\leq i\leq I-(j+1) we use the modified version

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (Ci,l|ν,𝑿i,l|ν)l=0j↦μj​((Ci,l|ν,𝑿i,l|ν)l=0j)\displaystyle(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}~\mapsto~\mu\_{j}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right) | =\displaystyle= | 𝔼​[Ci,J|ν|(Ci,l|ν,𝑿i,l|ν)l=0j]\displaystyle{\mathbb{E}}\left[C\_{i,J|\nu}\left|(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right]\right. |  | (3.5) |
|  |  | =\displaystyle= | 𝔼​[C^i,J|ν|(Ci,l|ν,𝑿i,l|ν)l=0j],\displaystyle{\mathbb{E}}\left[\widehat{C}\_{i,J|\nu}\left|(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right]\right., |  |

the last step uses the tower property of conditional expectation. The latter can be learned from the second line of the learning sample ℒj{\cal L}\_{j} given in ([3.3](https://arxiv.org/html/2602.15385v2#S3.E3 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")).
Using this learned regression function μj​(⋅)\mu\_{j}(\cdot), given in ([3.4](https://arxiv.org/html/2602.15385v2#S3.E4 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving"))-([3.5](https://arxiv.org/html/2602.15385v2#S3.E5 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")), we forecast the ultimate claims of accident period I−jI-j by

|  |  |  |
| --- | --- | --- |
|  | C^I−j,J|ν:=μj​((CI−j,l|ν,𝑿I−j,l|ν)l=0j)=𝔼​[CI−j,J|ν|(CI−j,l|ν,𝑿I−j,l|ν)l=0j].\displaystyle\widehat{C}\_{I-j,J|\nu}:=\mu\_{j}\left((C\_{I-j,l|\nu},\boldsymbol{X}\_{I-j,l|\nu})\_{l=0}^{j}\right)={\mathbb{E}}\left[C\_{I-j,J|\nu}\left|(C\_{I-j,l|\nu},\boldsymbol{X}\_{I-j,l|\nu})\_{l=0}^{j}\right]\right.. |  |

This ultimate claim forecast is appended to the available claims histories

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞^I−j|ν:=((CI−j,l|ν,𝑿I−j,l|ν)l=0j,C^I−j,J|ν).\widehat{\cal C}\_{I-j|\nu}:=\left((C\_{I-j,l|\nu},\boldsymbol{X}\_{I-j,l|\nu})\_{l=0}^{j},\,\widehat{C}\_{I-j,J|\nu}\right). |  | (3.6) |

Recursive iteration completes the ultimate claim forecasting, precisely reflecting the philosophy of Section [2.2](https://arxiv.org/html/2602.15385v2#S2.SS2 "2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"). This is illustrated by the middle and the right-hand side figures of Figure [2](https://arxiv.org/html/2602.15385v2#S2.F2 "Figure 2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving").

###### Remarks 3.1

* •

  Crucially, the above algorithm can deal with any dynamic stochastic covariates without their extrapolation.
* •

  The above algorithm is not about a certain ML architecture, but it is rather about how the data is organized to perform the one-shot ultimate prediction. The input (𝑿i,l|ν)l=0j(\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j} can be of any (reasonable) form, it can include stochastic dynamic covariates, it can involve textual data like medical reports, but it can also include information at a higher time frequency, i.e., the forecasting frequency periods j≥0j\geq 0 can also deal with continuously arriving information (𝑿i,l|ν)l∈[0,j](\boldsymbol{X}\_{i,l|\nu})\_{l\in[0,j]}. At this stage the choice of the ML architecture will become important as it needs to be able to deal with the formats of the inputs.
* •

  In practical applications, the only critical item of this algorithm is its recursive nature. In ([3.2](https://arxiv.org/html/2602.15385v2#S3.E2 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")) and ([3.6](https://arxiv.org/html/2602.15385v2#S3.E6 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")) we append the estimated ultimate claim of a given accident period i=I−(j+1)i=I-(j+1) to the observations, in order to be able to learn the one of the next accident period i+1=I−ji+1=I-j. This recursive nature has the disadvantage that if one accident period has a biased estimate, this bias will propagate through the following accident period estimates. Therefore, it is very important to correct for biases whenever possible.
* •

  This recursive algorithm uses the observed data in the same efficient way as the CL method, this is motivated by the result of Proposition [2.2](https://arxiv.org/html/2602.15385v2#S2.Thmtheo2 "Proposition 2.2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"). In particular, we simultaneously learn from fully developed but also from non-settled claims, such that always all relevant information is considered for prediction. The trade-off of this optimal use of information is the bias-control mentioned in the previous item.

## 4 Real data examples

We present two small scale real data examples. The first one considers accident insurance and the second one liability insurance. These two examples serve as a proof of concept, and they are neither meant to solve the most complex claims reserving problem, nor do they use the latest most fancy ML techniques, see second item of Remarks [3.1](https://arxiv.org/html/2602.15385v2#S3.Thmtheo1 "Remarks 3.1 ‣ 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving"). As mentioned, our main contribution is the optimal use of triangular data for one-shot ultimate claim prediction which leads to our key result of Proposition [2.2](https://arxiv.org/html/2602.15385v2#S2.Thmtheo2 "Proposition 2.2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"). This widely opens the door for individual claims reserving, and in our final Section [5](https://arxiv.org/html/2602.15385v2#S5 "5 Summary and next steps ‣ From Chain-Ladder to Individual Claims Reserving"), below, we highlight potential next steps.

To further strengthen our proposal, we select two examples for which also the lower triangle is known. This allows us to benchmark our forecasts against the true outcomes. Naturally, this requires that we restrict ourselves to older accident periods as the most recent accident period considered needs to be fully developed to be able to benchmark it against the ground truth.

### 4.1 Description of data

#### 4.1.1 Accident insurance data

We use an accident insurance dataset on an annual scale with 5 fully observed accident years, i.e., we have a fully observed 5×55\times 5 square. For model fitting and forecasting, we only use the upper triangle,
as in Figure [2](https://arxiv.org/html/2602.15385v2#S2.F2 "Figure 2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"), and we benchmark the forecasts against the true ultimates which are available here (having also observed the lower triangle).

|  |  |
| --- | --- |
| Characteristic |  |
| Time scale | calendar years |
| Number of accident years | 5 |
| Number of development years | 5 |
| Number of reported claims | 66,639 |
| Data description | |
| --- | --- |
| Annual individual cumulative payments Ci,j|νC\_{i,j|\nu} | |
| Claim status Oi,j|ν∈{0,1}O\_{i,j|\nu}\in\{0,1\} for closed/open | |
| Binary static covariate for work or leisure accident | |
| Calendar month of accident | |
| Reporting delay in daily units | |

Table 1: Characteristics of accident dataset.

Table [1](https://arxiv.org/html/2602.15385v2#S4.T1 "Table 1 ‣ 4.1.1 Accident insurance data ‣ 4.1 Description of data ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") shows the available data of the accident insurance dataset. There are 66,639 reported claims with a fully observed development history over the 5×55\times 5 square. Besides the individual cumulative payment process (Ci,j|ν)j(C\_{i,j|\nu})\_{j}, there is information about the claim status process (Oi,j|ν)j(O\_{i,j|\nu})\_{j}, with Oi,j|ν=1O\_{i,j|\nu}=1 meaning that the ν\nu-th claim of accident year ii is open at the end of settlement delay jj, and closed otherwise. Then, there is static information about: work or leisure related accident, the calendar month of the accident and the reporting delay in daily units. We collect all this static and dynamic covariate information in the claims feature process (𝑿i,j|ν)j(\boldsymbol{X}\_{i,j|\nu})\_{j}, see Section [3](https://arxiv.org/html/2602.15385v2#S3 "3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving").

We give some remarks on the available covariates. The claim status process (Oi,j|ν)j(O\_{i,j|\nu})\_{j} is stochastic dynamic. Typically, for closed claims Oi,j|ν=0O\_{i,j|\nu}=0 we do not expect further payments beyond settlement delay jj and the cumulative payment process should remain constant in these further periods. However, claims can be re-opened for further (unexpected) claims developments. Our method also reserves for these (potential) payments.
Typically, work or leisure related accidents are different, e.g., a bank employee cannot have a skiing accident during work hours. The calendar month will distinguish summer from winter activities (biking vs. skiing accidents). Finally, the reporting delay is important to infer the waiting period of the insurance contract, e.g., if the contract has a waiting period of 3 months, then daily allowance is only paid after this waiting period. Typically, the waiting period is positively correlated with the reporting delay.

#### 4.1.2 Liability insurance data

The second dataset considers liability insurance (excluding motor liability). We again have a fully observed 5×55\times 5 square and for model fitting we only use the upper triangle.

|  |  |
| --- | --- |
| Characteristic |  |
| Time scale | calendar years |
| Number of accident years | 5 |
| Number of development years | 5 |
| Number of reported claims | 21,991 |
| Data description | |
| --- | --- |
| Annual individual cumulative payments Ci,j|νC\_{i,j|\nu} | |
| Claim status Oi,j|ν∈{0,1}O\_{i,j|\nu}\in\{0,1\} for closed/open | |
| Claim incurred Ii,j|ν≥0I\_{i,j|\nu}\geq 0 | |
| Binary static covariate for private vs. commercial liability | |
| Calendar month of accident | |
| Reporting delay in daily units | |

Table 2: Characteristics of liability dataset.

Table [2](https://arxiv.org/html/2602.15385v2#S4.T2 "Table 2 ‣ 4.1.2 Liability insurance data ‣ 4.1 Description of data ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") shows the available data of the liability insurance dataset. The main difference to the previous example is that for this dataset there is also a claims incurred process (Ii,j|ν)j(I\_{i,j|\nu})\_{j} available. The claims incurred process is a claims adjuster’s prediction of the individual ultimate claim that is constantly updated when new information becomes available, i.e., this is a stochastic process driven by the claims adjuster’s assessments. Additionally, there is the case reserve process
(Ri,j|ν)j(R\_{i,j|\nu})\_{j} available by computing Ri,j|ν=Ii,j|ν−Ci,j|νR\_{i,j|\nu}=I\_{i,j|\nu}-C\_{i,j|\nu}.

### 4.2 Forecast model

#### 4.2.1 Network architecture

Next, we select the regression functions (μj)j=0J−1(\mu\_{j})\_{j=0}^{J-1}; we refer to ([3.1](https://arxiv.org/html/2602.15385v2#S3.E1 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")) and ([3.4](https://arxiv.org/html/2602.15385v2#S3.E4 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving"))-([3.5](https://arxiv.org/html/2602.15385v2#S3.E5 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")).
In our two small scale examples we have I=5I=5 and J=4J=4, thus, we only need 4 regression functions (μj)j=03(\mu\_{j})\_{j=0}^{3} in each of the two examples. We give a crude proposal that clearly allows for modification and improvement for bigger and refined datasets, see also Remarks [3.1](https://arxiv.org/html/2602.15385v2#S3.Thmtheo1 "Remarks 3.1 ‣ 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving") and the discussion in Section [5](https://arxiv.org/html/2602.15385v2#S5 "5 Summary and next steps ‣ From Chain-Ladder to Individual Claims Reserving"). Namely, we model all 4 regression functions (μj)j=03(\mu\_{j})\_{j=0}^{3} by separate networks. Hence, we have to learn 4 different networks for each of the two examples. Another simplification that we make is the following Markov assumption

|  |  |  |  |
| --- | --- | --- | --- |
|  | μj​((Ci,l|ν,𝑿i,l|ν)l=0j)=μj​(Ci,j|ν,𝑿i,j|ν).\mu\_{j}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right)=\mu\_{j}\left(C\_{i,j|\nu},\boldsymbol{X}\_{i,j|\nu}\right). |  | (4.1) |

That is, we do not consider the entire individual claims history (Ci,l|ν,𝑿i,l|ν)l=0j(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}, but we assume that it is sufficient to know the last state (Ci,j|ν,𝑿i,j|ν)(C\_{i,j|\nu},\boldsymbol{X}\_{i,j|\nu}).

A natural choice for μj\mu\_{j} under the Markov assumption ([4.1](https://arxiv.org/html/2602.15385v2#S4.E1 "In 4.2.1 Network architecture ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) is a feed-forward neural network (FNN) architecture; we will use the FNN notation and terminology of Wüthrich–Merz [[24](https://arxiv.org/html/2602.15385v2#bib.bib24)], and for a broader introduction to networks we also refer to that reference. If the Markov assumption ([4.1](https://arxiv.org/html/2602.15385v2#S4.E1 "In 4.2.1 Network architecture ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) fails to hold, then a natural candidate for μj\mu\_{j} is a Transformer architecture with an integrated CLS token for input encoding; see Richman et al. [[15](https://arxiv.org/html/2602.15385v2#bib.bib15)].

| Module | Dimension | #\# Weights | Activation |
| --- | --- | --- | --- |
| Input layer | 5 | – | – |
| 1st hidden layer | 20 | 120 | tanh\tanh |
| 2nd hidden layer | 15 | 315 | tanh\tanh |
| 3rd hidden layer | 10 | 160 | tanh\tanh |
| Output layer | 1 | 11 | exp\exp |

Table 3: Selected FNN architecture μjFNN\mu^{\rm FNN}\_{j}, for 1≤j≤J−11\leq j\leq J-1, in the accident insurance example.

We select identical plain-vanilla FNN architectures

|  |  |  |
| --- | --- | --- |
|  | (Ci,j|ν,𝑿i,j|ν)↦μjFNN​(Ci,j|ν,𝑿i,j|ν)=exp⁡(𝒛j(3:1)​(Ci,j|ν,𝑿i,j|ν)),(C\_{i,j|\nu},\boldsymbol{X}\_{i,j|\nu})~\mapsto~\mu^{\rm FNN}\_{j}(C\_{i,j|\nu},\boldsymbol{X}\_{i,j|\nu})=\exp\left(\boldsymbol{z}\_{j}^{(3:1)}(C\_{i,j|\nu},\boldsymbol{X}\_{i,j|\nu})\right), |  |

for all development periods j=0,…,3j=0,\ldots,3. These FNN architectures μjFNN\mu^{\rm FNN}\_{j} consider FNNs 𝒛j(3:1)\boldsymbol{z}\_{j}^{(3:1)} with 3 hidden layers with number of neurons given by (20,15,10)(20,15,10) in the 3 hidden layers. The explicit specifications are shown in Table [3](https://arxiv.org/html/2602.15385v2#S4.T3 "Table 3 ‣ 4.2.1 Network architecture ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"), and this results in FNNs with 606 weights to be fitted in the case of the accident insurance dataset for every j=0,…,3j=0,\ldots,3. Since under the Markov assumption ([4.1](https://arxiv.org/html/2602.15385v2#S4.E1 "In 4.2.1 Network architecture ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")), the input has always the same dimension, we use the identical FNN architecture for all regression functions (μjFNN)j=03(\mu^{\rm FNN}\_{j})\_{j=0}^{3}, only their weights will differ (after model fitting). For an explicit implementation of this architecture we refer to Wüthrich–Merz [[24](https://arxiv.org/html/2602.15385v2#bib.bib24), Listing 7.1], only the part involving the volume in that reference needs to be dropped because here we only have unit exposures.

We select the same FNN architecture also for the liability insurance dataset. In this second dataset we have an input dimension of 7 (additionally considering claims incurred and case reserves). This results in 160 weights in the first hidden layer and a FNN architecture of totally having 646 weights.

#### 4.2.2 Data pre-processing and model fitting

We are almost ready now to fit these four FNNs (μjFNN)j=03(\mu^{\rm FNN}\_{j})\_{j=0}^{3} for both examples. There remains the input pre-processing and the selection of the fitting procedure. Typically, inputs (Ci,j|ν,𝑿i,j|ν)(C\_{i,j|\nu},\boldsymbol{X}\_{i,j|\nu}) should be standardized to receive an efficient stochastic gradient descent (SGD) fitting procedure. The individual cumulative payments are considered on the log-scale and they are standardized by

|  |  |  |
| --- | --- | --- |
|  | C~i,j|ν←log⁡(max⁡{1,Ci,j|ν})−m^s^.\widetilde{C}\_{i,j|\nu}~\leftarrow~\frac{\log\left(\max\{1,C\_{i,j|\nu}\}\right)-\widehat{m}}{\widehat{s}}. |  |

where m^\widehat{m} and s^\widehat{s} are the empirical mean and standard deviation of log⁡(max⁡{1,Ci,j|ν})\log(\max\{1,C\_{i,j|\nu}\}) over all available cumulative payments Ci,j|νC\_{i,j|\nu} simultaneously in all accident years ii, for all claims ν\nu and in all development periods jj.

In the case of the liability dataset, we apply the same transformation to claims incurred Ii,j|νI\_{i,j|\nu}, and we apply the standardization to the case reserves Ri,j|νR\_{i,j|\nu} without going to the log-scale.

Furthermore, the claim status Oi,j|ν∈{0,1}O\_{i,j|\nu}\in\{0,1\} does not require pre-processing. The binary static covariates are mapped to {0,1}\{0,1\}, the calendar month c​m∈{1,…,12}cm\in\{1,\ldots,12\} is scaled to [0,1][0,1] by transforming it to (c​m−1)/11(cm-1)/11, and the reporting delay is censored at 365 days, mapped to the log-scale and being scaled to [0,1][0,1] as for the calender month.
This provides us with the pre-processed input (C~i,j|ν,𝑿~i,j|ν)(\widetilde{C}\_{i,j|\nu},\widetilde{\boldsymbol{X}}\_{i,j|\nu}) which is used to forecast the corresponding ultimate claim

|  |  |  |
| --- | --- | --- |
|  | (C~i,j|ν,𝑿~i,j|ν)↦C^i,J|νFNN=μjFNN​(C~i,j|ν,𝑿~i,j|ν).(\widetilde{C}\_{i,j|\nu},\widetilde{\boldsymbol{X}}\_{i,j|\nu})~\mapsto~\widehat{C}^{\rm FNN}\_{i,J|\nu}=\mu\_{j}^{\rm FNN}\left(\widetilde{C}\_{i,j|\nu},\widetilde{\boldsymbol{X}}\_{i,j|\nu}\right). |  |

These FNN regression functions are learned recursively as described in
Section [3](https://arxiv.org/html/2602.15385v2#S3 "3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving"), see also Figure [2](https://arxiv.org/html/2602.15385v2#S2.F2 "Figure 2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"). For fitting, we apply the SGD algorithm with early stopping using the hyper-parameter specification as reported in Table [4](https://arxiv.org/html/2602.15385v2#S4.T4 "Table 4 ‣ 4.2.2 Data pre-processing and model fitting ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving").

|  |  |
| --- | --- |
| Component | Setting |
| Loss function | mean squared error (MSE) |
| Optimizer | Adam with learning rate 10−310^{-3} |
| Batch size and epochs | 4,096 and 1,000 |
| Learning-validation split | 9:19:1 |
| Early stopping | reduce learning rate on plateau, factor 0.9, patience 5 |
| Ensembling | 10 network fits with different seeds |

Table 4: Key implementation hyper-parameters for FNN fitting.

#### 4.2.3 Bias control

In the forecast procedure, we install one special feature that is very crucial in bias control. Assuming stationarity along the accident year axis for given static features, there should not be any trend in the ultimate claim predictions, of course, this also means that inflation-adjusted quantities are considered.

It is a well-known fact that SGD fitting with early stopping leads to biased models, see, e.g., Wüthrich [[22](https://arxiv.org/html/2602.15385v2#bib.bib22)]. We fix this by ensuring that the balance property holds, by shifting the prediction by the size of the observed in-sample bias. That is,
we fit the FNN architecture on the learning data ℒj{\cal L}\_{j} using an early stopped SGD providing us with the fitted FNN architecture μ^jFNN​(⋅)\widehat{\mu}\_{j}^{\rm FNN}(\cdot).
A balance corrected predictive version thereof is obtained by setting

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^jbc−FNN​(⋅)=∑i≤I−J∑νCi,J|ν+∑I−(J−1)≤i≤I−(j+1)∑νC^i,J|ν∑i≤I−(j+1)∑νμ^jFNN​((Ci,l|ν,𝑿i,l|ν)l=0j)​μ^jFNN​(⋅).\widehat{\mu}\_{j}^{{\rm bc-FNN}}(\cdot)=\frac{\sum\_{i\leq I-J}\sum\_{\nu}C\_{i,J|\nu}+\sum\_{I-(J-1)\leq i\leq I-(j+1)}\sum\_{\nu}\widehat{C}\_{i,J|\nu}}{\sum\_{i\leq I-(j+1)}\sum\_{\nu}\widehat{\mu}\_{j}^{\rm FNN}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right)}\,\widehat{\mu}\_{j}^{\rm FNN}(\cdot). |  | (4.2) |

This gives a multiplicative correction to align the average in-sample prediction with the average observed (estimated) response; note that this is again of a recursive nature.

We give two further features that may help to improve the predictive models.

* •

  Because network fitting involves many elements of randomness, e.g., the initialization of the SGD algorithm, we always ensemble over 10 balance corrected predictors ([4.2](https://arxiv.org/html/2602.15385v2#S4.E2 "In 4.2.3 Bias control ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) being received from the same SGD algorithm but with different seeds for initialization; see Richman–Wüthrich [[16](https://arxiv.org/html/2602.15385v2#bib.bib16)].
* •

  The fitting procedure can be regularized using expert knowledge, e.g., if we have a strong prediction from the CL or the Bornhuetter–Ferguson [[3](https://arxiv.org/html/2602.15385v2#bib.bib3)] method, we can use this prediction to regularize the learned FNN predictor
  μ^jFNN​(⋅)\widehat{\mu}\_{j}^{\rm FNN}(\cdot). This can be done on an individual claims level, but also for more coarse claims cohorts.

### 4.3 Results

#### 4.3.1 Chain-ladder results

We start by reporting the classic CL results of Mack [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)] on cumulative payments. This will set the benchmark for all subsequent methods.

|  | True OLL | CL reserves | RMSEP | Error | in % |
| --- | --- | --- | --- | --- | --- |
| Accident |  |  |  |  |  |
| Mack’s CL model [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)] | 24,212 | 23,064 | 1,663 | -1,148 | 69% |
| RBNS CL method | 19,733 | 18,959 |  | -774 |  |
| Liability |  |  |  |  |  |
| Mack’s CL model [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)] | 15,730 | 11,526 | 1,977 | -4,204 | 213% |
| RBNS CL method | 11,494 | 8,601 |  | -2,893 |  |

Table 5: Mack’s CL results on cumulative payments and CL RBNS reserves for both datasets of accident and liability insurance.

In Table [5](https://arxiv.org/html/2602.15385v2#S4.T5 "Table 5 ‣ 4.3.1 Chain-ladder results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") we report Mack’s CL reserves and Mack’s rooted mean squared error of prediction (RMSEP), which is a measure of the prediction uncertainty of the CL reserves. In case of accident insurance the CL reserves are 23,064 and the RMSEP is 1,663. Since in these examples we also know the lower triangle, we can benchmark these results against the true outstanding loss liabilities (OLL), i.e., the difference between the true ultimate claims Ci,J|νC\_{i,J|\nu} and the payments Ci,I−i|νC\_{i,I-i|\nu} already done at time II. In the case of accident insurance, the true OLL are 24,212 and the CL reserves underestimate the true liabilities by -1,148, which amounts to 69% of the RMSEP. Thus, this underestimation is below one RMSEP, and it can well be explained by irreducible risk and parameter estimation uncertainty. We conclude that the CL method seems to work well for the accident insurance dataset.

For the liability insurance example, the situation is different. From Table [5](https://arxiv.org/html/2602.15385v2#S4.T5 "Table 5 ‣ 4.3.1 Chain-ladder results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") we note that the CL method underestimates the true OLL by 213% of Mack’s RMSEP, in statistical terms one would reject the CL model in this case because the true outcome is not within two standard deviations (RMSEPs) of the prediction.

Mack’s CL model [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)] gives a prediction for RBNS and IBNR claims because it does not distinguish w.r.t. the claims reporting pattern.
Using the method presented in Section [2.3](https://arxiv.org/html/2602.15385v2#S2.SS3 "2.3 Chain-ladder RBNS reserving ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving"), we compute the RBNS reserves, we coin it ‘RBNS CL method’ in Table [5](https://arxiv.org/html/2602.15385v2#S4.T5 "Table 5 ‣ 4.3.1 Chain-ladder results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"). We observe that the prediction errors generally decrease (over-proportionally) compared to the decline in reserves, which indicates that part of the underestimation problem is due to IBNR claims.

We will use these ‘RBNS CL method’ results of Table [5](https://arxiv.org/html/2602.15385v2#S4.T5 "Table 5 ‣ 4.3.1 Chain-ladder results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") to benchmark all further individual claims reserving methods (which only consider RBNS claims at time II).

#### 4.3.2 Accident insurance: Individual claims reserving results

We now perform individual claims reserving using the FNN architectures
(μjFNN)j=03(\mu^{\rm FNN}\_{j})\_{j=0}^{3} being fitted as described above.
The results are reported in Table [6](https://arxiv.org/html/2602.15385v2#S4.T6 "Table 6 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving").

| ii | True OLL | RBNS CL | FNN | CL Error | FNN Error | CL Ind RMSE | FNN Ind RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | 173 | -14 | -180 | 1.499 | 2.575 |
| 3 | 1,017 | 1,305 | 1,262 | 288 | 246 | 2.956 | 2.954 |
| 4 | 3,102 | 3,099 | 3,290 | -2 | 189 | 4.263 | 4.248 |
| 5 | 15,263 | 14,216 | 14,712 | -1,046 | -551 | 8.240 | 8.177 |
| Total | 19,735 | 18,959 | 19,437 | -774 | -296 |  |  |

Table 6: Accident insurance: Results of individual claims prediction using the fitted FNN architectures (μjFNN)j=03(\mu^{\rm FNN}\_{j})\_{j=0}^{3}.

The column ‘FNN’ shows the individual claims prediction results using the fitted and balance-corrected FNN architectures (μ^jbc−FNN)j=03(\widehat{\mu}^{\rm bc-FNN}\_{j})\_{j=0}^{3} and the inputs as described in Table [1](https://arxiv.org/html/2602.15385v2#S4.T1 "Table 1 ‣ 4.1.1 Accident insurance data ‣ 4.1 Description of data ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"). Generally, we observe that these FNN predictions are closer to the true OLL than the RBNS CL forecasts (columns ‘CL Error’ vs. ’FNN Error’), indicating that indeed one can effectively learn by including the additional features given in Table [1](https://arxiv.org/html/2602.15385v2#S4.T1 "Table 1 ‣ 4.1.1 Accident insurance data ‣ 4.1 Description of data ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"). The total prediction error is -296 which is only 1.5% of the total true OLL; this should also be compared to the RMSEP of 1,663 in Mack’s model [[14](https://arxiv.org/html/2602.15385v2#bib.bib14)], see Table [5](https://arxiv.org/html/2602.15385v2#S4.T5 "Table 5 ‣ 4.3.1 Chain-ladder results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"), indicating that we have an excellent forecast from the individual claims model.

The last two columns of Table [6](https://arxiv.org/html/2602.15385v2#S4.T6 "Table 6 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") report the rooted mean squared errors (RMSE) between the forecasts (RBNS CL/FNN) and the true OLL on an individual claims level. We generally, observe a decreasing individual prediction error, except for accident year i=2i=2, where we only predict one single period ahead. Thus, this individual claims reserving method leads to more accurate reserves on an individual claims level.
The decreased values still have a similar magnitude, which indicates that the dominating uncertainty component is irreducible risk (pure randomness) and the systematic effects that we can learn from the covariates live on a smaller scale – low signal-to-noise ratio based on the available information – which is common in many actuarial applications. This will further be discussed w.r.t. the results of Table [7](https://arxiv.org/html/2602.15385v2#S4.T7 "Table 7 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"), below.

The critical part of recursive claims reserving methods is that such methods are prone to biases. E.g., if we overestimate accident period i=2i=2, then this overestimation will propagate (in an alleviated manner) through the subsequent accident periods i≥3i\geq 3 through the recursive structure of the estimation procedure. For this reason, potential biases need careful consideration, and the fitting procedure may require regularization, as described in Section [4.2.3](https://arxiv.org/html/2602.15385v2#S4.SS2.SSS3 "4.2.3 Bias control ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"). Our next goal is to check whether the bias control (balance correction) presented in ([4.2](https://arxiv.org/html/2602.15385v2#S4.E2 "In 4.2.3 Bias control ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) is effective.

Because in our example we know the true lower triangle, we can directly backtest for the bias problem – note that in any reasonable real-world application this is not possible because the lower triangle is unknown (otherwise we would not need to predict it), but we perform this analysis here to verify that our proposal indeed works. The propagated bias problem comes from the fact that later periods use estimates of earlier periods in their fitting procedure, see ([3.6](https://arxiv.org/html/2602.15385v2#S3.E6 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")), or more generally in the learning data
ℒj{\cal L}\_{j} we have responses and inputs, see ([3.3](https://arxiv.org/html/2602.15385v2#S3.E3 "In 3.1 Recursive individual claims reserving ‣ 3 Individual ultimate prediction using machine learning ‣ From Chain-Ladder to Individual Claims Reserving")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | (C^i,J|ν,(Ci,l|ν,𝑿i,l|ν)l=0j),\left(\widehat{C}\_{i,J|\nu},(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right), |  | (4.3) |

for I−(J−1)≤i≤I−(j+1)I-(J-1)\leq i\leq I-(j+1) and Ti|ν≤jT\_{i|\nu}\leq j.
This reflects the recursive estimation nature that has been used to compute the FNN results of Table [6](https://arxiv.org/html/2602.15385v2#S4.T6 "Table 6 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"). To verify the effectiveness of our proposal ([4.2](https://arxiv.org/html/2602.15385v2#S4.E2 "In 4.2.3 Bias control ‣ 4.2 Forecast model ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) of the bias control, we use in a second fitting attempt the true ultimate claims which are available in our unusual set-up of knowing the lower triangle. That is, we replace in the learning data ℒj{\cal L}\_{j} the items ([4.3](https://arxiv.org/html/2602.15385v2#S4.E3 "In 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) during the fitting procedure by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ci,J|ν,(Ci,l|ν,𝑿i,l|ν)l=0j).\left(C\_{i,J|\nu},(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j}\right). |  | (4.4) |

Because this no longer leads to a recursive estimation procedure (the responses are fully observed in this training procedure), this forecast process cannot lead to a propagating bias problem. We use the identical FNN architecture as above and we fit these FNNs using the learning data composed of ([4.4](https://arxiv.org/html/2602.15385v2#S4.E4 "In 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")). The results are reported in Table [7](https://arxiv.org/html/2602.15385v2#S4.T7 "Table 7 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"), and because ([4.4](https://arxiv.org/html/2602.15385v2#S4.E4 "In 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) is not available in any real-world application, we set the corresponding results in square brackets.

| ii | True OLL | RBNS CL | FNN | CL Error | FNN Error | CL Ind RMSE | FNN Ind RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | [173] | -14 | [-180] | 1.499 | [2.575] |
| 3 | 1,017 | 1,305 | [1,421] | 288 | [404] | 2.956 | [3.006] |
| 4 | 3,102 | 3,099 | [3,183] | -2 | [81] | 4.263 | [4.223] |
| 5 | 15,263 | 14,216 | [14,581] | -1,046 | [-682] | 8.240 | [8.212] |
| Total | 19,735 | 18,959 | [19,358] | -774 | [-377] |  |  |

Table 7: Accident insurance: Results of individual claims prediction using the true ultimate claims for model fitting.

Comparing the individual claims reserving FNN results of Tables
[6](https://arxiv.org/html/2602.15385v2#S4.T6 "Table 6 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") and [7](https://arxiv.org/html/2602.15385v2#S4.T7 "Table 7 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"), we observe a huge similarity, meaning that the information with estimated responses ([4.3](https://arxiv.org/html/2602.15385v2#S4.E3 "In 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) and the one with true responses ([4.4](https://arxiv.org/html/2602.15385v2#S4.E4 "In 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")) lead to almost the identical results, both concerning the total estimation error ‘FNN Error’ against the true OLL as well as the errors on individual claims levels (last column ‘FNN Ind RMSE’ of Tables [6](https://arxiv.org/html/2602.15385v2#S4.T6 "Table 6 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") and [7](https://arxiv.org/html/2602.15385v2#S4.T7 "Table 7 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")). This also verifies that the main uncertainty driver is irreducible risk (low signal-to-noise ratio based on the available information), and not missing precision of the ultimate claims prediction in ([4.3](https://arxiv.org/html/2602.15385v2#S4.E3 "In 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")). Of course, in a next step one may try to integrate the entire individual claims histories, collect more individual claims information, e.g., medical reports in accident insurance, and this may further decrease prediction error on an individual claims level.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 3: (lhs) Reserves per accident year i=1,…,5i=1,\ldots,5 and separated by closed and open claims at time II, (rhs) per accident calendar month c​m∈{1,…,12}cm\in\{1,\ldots,12\}.

As a concluding analysis on the accident insurance dataset, we discuss the two plots shown in Figure [3](https://arxiv.org/html/2602.15385v2#S4.F3 "Figure 3 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"). The graph on the left-hand side shows the partition of the reserves w.r.t. accident year 1≤i≤I=51\leq i\leq I=5 and separated by closed and open claims at time II. The blue bars show the true OLLs, the yellow bars the CL predictions, and the orange bars the individual claims FNN forecasts. The individual FNN forecasts closely follow the true OLLs, thus, we seem to accurately capture the true OLLs, and we also correctly distinguish closed from open claims. It is also nice to see that indeed, there are quite some payments on closed claims (re-openings). The CL method, of course, cannot discriminate between closed and open claims, as the CL method does not consider a claim status label.

The right-hand side of Figure [3](https://arxiv.org/html/2602.15385v2#S4.F3 "Figure 3 ‣ 4.3.2 Accident insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") shows the reserves split by the accident month label. Also here we see a close alignment of individual claims FNN forecasts and true OLLs, generally having increasing reserves per accident month. This is explained by the fact that the payment data is considered on a calendar year grid, a January claim being more mature than a December claim, leading to generally lower reserves for early calendar months, but to receive the full picture, and should still complete this analysis by the different claim types in the different seasons; this information is not available here.

#### 4.3.3 General insurance: Individual claims reserving results

Table [8](https://arxiv.org/html/2602.15385v2#S4.T8 "Table 8 ‣ 4.3.3 General insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") shows our second example of the liability insurance dataset. The interpretation of the results is rather similar to the accident insurance example.

| ii | True OLL | RBNS CL | FNN | CL Error | FNN Error | CL Ind RMSE | FNN Ind RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 361 | 635 | 761 | 274 | 400 | 2.717 | 4.483 |
| 3 | 3,233 | 1,497 | 1,743 | -1,736 | -1,491 | 19.988 | 18.574 |
| 4 | 3,287 | 2,488 | 2,963 | -799 | -324 | 12.400 | 11.704 |
| 5 | 4,613 | 3,982 | 4,038 | -631 | -575 | 14.901 | 13.907 |
| Total | 11,494 | 8,602 | 9,505 | -2,892 | -1,894 |  |  |

Table 8: Liability insurance: Results of individual claims prediction using the fitted FNN architectures (μjFNN)j=03(\mu^{\rm FNN}\_{j})\_{j=0}^{3}.

The reason for giving this second example is that additionally there is claims incurred Ii,j|νI\_{i,j|\nu} available here. We use this claim incurred information as input in 𝑿i,j|ν\boldsymbol{X}\_{i,j|\nu}, together with the resulting case reserves Ri,j|ν=Ii,j|ν−Ci,j|νR\_{i,j|\nu}=I\_{i,j|\nu}-C\_{i,j|\nu}. Interestingly, this has a very positive effect on the individual claims prediction error (last column of Table [8](https://arxiv.org/html/2602.15385v2#S4.T8 "Table 8 ‣ 4.3.3 General insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving")), especially in the most recent accident year i=5i=5. Intuitively it is clear that after the first development period j=0j=0, the cumulative payments Ci,0|νC\_{i,0|\nu} may not be very predictive for the ultimate claims prediction in this long-tailed business line. In this example the claims incurred estimates of the claims’ adjusters are of good quality to improve individual claim prediction. Interestingly, for more mature accident years, there is less advantage in possessing claims incurred information. The reason may be two fold, either cumulative payments and claim status carry sufficient information in more developed years, or the quality of claims incurred is insufficient in more developed accident years (maybe due to a lack of continuous improvements/updates by claims’ adjusters).

Table [9](https://arxiv.org/html/2602.15385v2#S4.T9 "Table 9 ‣ 4.3.3 General insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") shows the results if we remove the claims incurred information from the inputs 𝑿i,j|ν\boldsymbol{X}\_{i,j|\nu}. The biggest change in ‘FNN Ind RMSE’ is indeed observed for the most recent accident year i=5i=5, which supports that claims incurred is important information for the least developed claims.

| ii | True OLL | RBNS CL | FNN | CL Error | FNN Error | CL Ind Err | FNN Ind Error |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 361 | 635 | 503 | 274 | 142 | 2.717 | 5.072 |
| 3 | 3,233 | 1,497 | 1,664 | -1,736 | -1,569 | 19.988 | 20.079 |
| 4 | 3,287 | 2,488 | 2,644 | -799 | -643 | 12.400 | 12.026 |
| 5 | 4,613 | 3,982 | 5,028 | -631 | 415 | 14.901 | 14.282 |
| Total | 11,494 | 8,602 | 9,839 | -2,892 | -1,655 |  |  |

Table 9: Liability insurance: Results of individual claims prediction where we drop the claims incurred information from the inputs.

In view of Tables [8](https://arxiv.org/html/2602.15385v2#S4.T8 "Table 8 ‣ 4.3.3 General insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving") and [9](https://arxiv.org/html/2602.15385v2#S4.T9 "Table 9 ‣ 4.3.3 General insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"), the bad performance of the RBNS CL method and partly of the individual claims reserving method can be traced back to accident year i=3i=3. Analyzing this accident year in more detail, we find two individual claims that caused payments of 1,874 in development periods j=3,4j=3,4, thus, two claims evolve to severe ones, which could not be anticipated by the systematic structure (covariates), but which needs to be attributed to the irreducible risk part. This also explains the large values in the two columns ‘Ind RSME’ in Table [8](https://arxiv.org/html/2602.15385v2#S4.T8 "Table 8 ‣ 4.3.3 General insurance: Individual claims reserving results ‣ 4.3 Results ‣ 4 Real data examples ‣ From Chain-Ladder to Individual Claims Reserving"). Note that we considered all claims in our analysis – in some literature large losses are discarded for a more stable fitting, see, e.g., Schneider–Schwab [[18](https://arxiv.org/html/2602.15385v2#bib.bib18), Section 3.1]; this removal simplifies modeling and analysis, but it is incorrect from a material point of view because these large claims are cost drivers that need to be borne by the insurer. Naturally, this large idiosyncratic part is not covered by the loss reserves (expected values), and it will trigger the solvency capital in a stand-alone view.

## 5 Summary and next steps

We presented a novel way of computing the CL reserves by a recursive direct one-shot estimation and prediction procedure. This was achieved by restructuring the data and estimation procedure. This novel representation widely opens the door the ML applications on more granular individual claims data. In fact, this representation is suitable for any kind of input data, and due to the one-shot prediction approach it does not require to extrapolate the stochastic dynamic covariates, the latter being the main obstacle in most of the individual claims reserving methods. This barrier is now removed and we expect fast major developments in this field.

Another major advantage of our proposal over most other ML proposals is that we start from the familiar, well-proven chain-ladder method, the reserving actuaries are very familiar with. This allows one to easily use the chain-ladder predictions as guardrails to regularize the individual claims predictions staying close to the chain-ladder reserves.

The main weakness of our proposal is the fact that it is a recursive procedure. Recursive methods are prone to propagating biases, which needs careful control in each step of the recursion. We presented the (simple) balance property approach for bias control, but being within a chain-ladder framework we can also envisage to control biases by classical chain-ladder predictions.

* •

  Our main contribution is the recursive one-shot estimation and prediction procedure that enables the step from going from the classic chain-ladder method to individual claims reserving. Our (simple) example was rather meant as a proof of concept on a small data example using plain-vanilla neural networks. Naturally, there is huge potential (but also work to be done) to refine the machine learning method used to the specific individual claims reserving data selected, be it a neural network, a gradient boosting machine or other machine learning tools.
* •

  Naturally, the choice of the loss function plays a crucial role in model fitting. Our choice of the mean squared error can clearly be improved so that the predictive model is improved over all ranges of the claim sizes, aiming at having accurate predictions both on large and small claims.
* •

  We have encountered some difficulties in modeling so-called zero claims, i.e., claims that can be closed without any payments. Our output activation function in the network architecture was the exponential one. This constrains predictions to strictly positive values. This point clearly needs more engineering to able to capture more effectively zero claims, especially those that have been closed already over several periods.
* •

  For our small scale example we imposed a Markov modeling assumption on the individual claims history, which implies that only the latest observation is relevant for prediction. Clearly this should be lifted to a model that includes the entire claims history. The straightforward next step is to employ a Transformer architecture including a CLS token for time-series data encoding. This allows for a data-driven decision about the validity of the Markov assumption.
* •

  For bias control we used probably the simplest method of balance correction. Clearly, there is more research necessary to prove its effectiveness and one should explore other methods.
* •

  At the moment, we fit a different network for every accident period considered. Clearly, we should ask for a more economic modeling, and hopefully different accident periods can share parts of the machine learning structure. However, it is not immediately clear how this can be achieved because of the fact that the algorithm is of a recursive nature that needs a careful bias control.
* •

  Our proposal considers a one-shot prediction of the ultimate claim. Naturally the same technology can also be used for a one-shot prediction of the entire future claim payment process. In machine learning jargon, this will require a sequence-to-sequence forecasting approach.
* •

  We only consider closed and reported but not settled (RBNS) claims. We still need to take care of incurred but not reported (IBNR) claims. This will require a downstream model likely being based on a frequency-severity decomposition. For the frequency forecasting the same one-shot prediction approach could work, however, rather in a sequence-to-sequence forecasting structure because we care about the specific reporting pattern.

## References

* [1]

  Avanzi, B., Richman, R., Wong, B., Wüthrich, M.V., Xie, Y. (2026).
  Reinforcement learning for micro-level claims reserving.
  arXiv:2601.07637.
* [2]

  Bladt, M., Pittarello, G. (2025).
  Individual claims reserving using the Aalen–Johansen estimator.
  ASTIN Bulletin - The Journal of the IAA 55/1, 29-49.
* [3]

  Bornhuetter, R.L., Ferguson, R.E. (1972). The actuary and IBNR.
  Proceedings CAS 59, 181-195.
* [4]

  Chaoubi, I., Besse, C., Cossette, H., Côté, M.-P. (2023).
  Micro-level reserving for general insurance claims using a long short-term memory network.
  Applied Stochastic Models in Business and Industry 39/3, 382-407.
* [5]

  De Felice, M., Moriconi, F. (2019).
  Claim watching and individual claims reserving using classification and regression trees.
  Risks 7/4, 102.
* [6]

  Delong, Ł., Lindholm, M., Wüthrich, M.V. (2022).
  Collective reserving using individual claims data.
  Scandinavian Actuarial Journal 2022/1, 1-28.
* [7]

  Gabrielli, A. (2021).
  An individual claims reserving model for reported claims.
  European Actuarial Journal 11/2, 541-577.
* [8]

  Hiabu, M., Hofman, E.D., Pitarello, G. (2023).
  A machine learning approach based on survival analysis for IBNR frequencies in non-life reserving.
  arXiv:2312.14549.
* [9]

  Kuo, K. (2019).
  DeepTriangle: a deep learning approach to loss reserving.
  Risks 7/3, article 97.
* [10]

  Kuo, K. (2020).
  Individual claims forecasting with Bayesian mixture density networks.
  arXiv:2003.02453v1.
* [11]

  Lopez, O., Milhaud, X. (2021).
  Individual reserving and nonparametric estimation of claim amounts subject to large reporting delays.
  Scandinavian Actuarial Journal 2021/1, 34-53.
* [12]

  Lopez, O., Milhaud, X., Thérond, P.-E. (2019).
  A tree-based algorithm adapted to microlevel reserving and long development claims.
  ASTIN Bulletin - The Journal of the IAA 49/3, 741-762.
* [13]

  Lorenz, H., Schmidt, K.D. (2016).
  Grossing up method.
  In: Handbook on Loss Reserving,
  Radtke, M., Schmidt, K.D., Schnaus, A. (eds.), Springer, 127-131.
* [14]

  Mack, T. (1993). Distribution-free calculation of the standard error of chain ladder reserve estimates.
  ASTIN Bulletin - The Journal of the IAA 23/2, 213-225.
* [15]

  Richman, R., Scognamiglio, S., Wüthrich, M.V. (2025).
  The credibility transformer.
  European Actuarial Journal 15/2, 345-379.
* [16]

  Richman, R., Wüthrich, M.V. (2020).
  Nagging predictors.
  Risks 8/3, article 83.
* [17]

  Rosenlund, S. (2012).
  Bootstrapping individual claim histories.
  ASTIN Bulletin - The Journal of the IAA 42/1, 291-324.
* [18]

  Schneider, J.C., Schwab, B. (2025).
  Advancing loss reserving: a hybrid neural network approach for individual claim development prediction.
  Journal of Risk and Insurance 92/2, 389-423.
* [19]

  Schnieper, R. (1991).
  Separating true IBNR from IBNER claims.
  ASTIN Bulletin - The Journal of the IAA 21/1, 111-127.
* [20]

  Turcotte, R., Shi, P. (2026).
  Individual loss reserving for multi-coverage insurance.
  ASTIN Bulletin - The Journal of the IAA 56/2, to appear.
* [21]

  Wüthrich, M.V. (2018).
  Machine learning in individual claims reserving.
  Scandinavian Actuarial Journal 2018/6, 465-480.
* [22]

  Wüthrich, M.V. (2020).
  Bias regularization in neural network models for general insurance pricing.
  European Actuarial Journal 10/1, 179-202.
* [23]

  Wüthrich, M.V., Merz, M. (2008).
  Stochastic Claims Reserving Methods in Insurance. Wiley.
* [24]

  Wüthrich, M.V., Merz, M. (2023).
  Statistical Foundations of Actuarial Learning and its Applications.
  Springer.

## Appendix A Proof

Proof of Proposition [2.2](https://arxiv.org/html/2602.15385v2#S2.Thmtheo2 "Proposition 2.2 ‣ 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving").
It suffices to prove that F^j=∏l=jJ−1f^l\widehat{F}\_{j}=\prod\_{l=j}^{J-1}\widehat{f}\_{l} for all j∈{0,…,J−1}j\in\{0,\ldots,J-1\}. The proof goes by induction. Initialization. For J−1J-1, the claim follows from ([2.4](https://arxiv.org/html/2602.15385v2#S2.E4 "In 2.2 Recursive chain-ladder factor estimation ‣ 2 Chain-ladder method ‣ From Chain-Ladder to Individual Claims Reserving")).

Induction step. Now we consider the step j+1→j∈{0,…,J−2}j+1\to j\in\{0,\ldots,J-2\}. Assume
F^k=∏l=kJ−1f^l\widehat{F}\_{k}=\prod\_{l=k}^{J-1}\widehat{f}\_{l} holds for all k∈{j+1,…,J−1}k\in\{j+1,\ldots,J-1\}.
We have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F^j\displaystyle\widehat{F}\_{j} | =\displaystyle= | ∑i=1I−j−1C^i,J∗∑i=1I−j−1Ci,j=∑i=1I−j−1Ci,j+1∑i=1I−j−1Ci,j​∑i=1I−j−1C^i,J∗∑i=1I−j−1Ci,j+1\displaystyle\frac{\sum\_{i=1}^{I-j-1}\widehat{C}^{\*}\_{i,J}}{\sum\_{i=1}^{I-j-1}C\_{i,j}}~=~\frac{\sum\_{i=1}^{I-j-1}C\_{i,j+1}}{\sum\_{i=1}^{I-j-1}C\_{i,j}}\frac{\sum\_{i=1}^{I-j-1}\widehat{C}^{\*}\_{i,J}}{\sum\_{i=1}^{I-j-1}C\_{i,j+1}} |  |
|  |  | =\displaystyle= | f^j​∑i=1I−j−2C^i,J∗+C^I−j−1,J∗∑i=1I−j−2Ci,j+1+CI−j−1,j+1\displaystyle\widehat{f}\_{j}~\frac{\sum\_{i=1}^{I-j-2}\widehat{C}^{\*}\_{i,J}+\widehat{C}^{\*}\_{I-j-1,J}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}+C\_{I-j-1,j+1}} |  |
|  |  | =\displaystyle= | f^j​[∑i=1I−j−2C^i,J∗∑i=1I−j−2Ci,j+1+CI−j−1,j+1+C^I−j−1,J∗∑i=1I−j−2Ci,j+1+CI−j−1,j+1]\displaystyle\widehat{f}\_{j}\left[\frac{\sum\_{i=1}^{I-j-2}\widehat{C}^{\*}\_{i,J}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}+C\_{I-j-1,j+1}}+\frac{\widehat{C}^{\*}\_{I-j-1,J}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}+C\_{I-j-1,j+1}}\right] |  |
|  |  | =\displaystyle= | f^j​[∑i=1I−j−2Ci,j+1∑i=1I−j−2Ci,j+1+CI−j−1,j+1​∑i=1I−j−2C^i,J∗∑i=1I−j−2Ci,j+1+CI−j−1,j+1∑i=1I−j−2Ci,j+1+CI−j−1,j+1​C^I−j−1,J∗CI−j−1,j+1]\displaystyle\widehat{f}\_{j}\left[\frac{\sum\_{i=1}^{I-j-2}C\_{i,j+1}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}+C\_{I-j-1,j+1}}\frac{\sum\_{i=1}^{I-j-2}\widehat{C}^{\*}\_{i,J}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}}+\frac{C\_{I-j-1,j+1}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}+C\_{I-j-1,j+1}}\frac{\widehat{C}^{\*}\_{I-j-1,J}}{C\_{I-j-1,j+1}}\right] |  |
|  |  | =\displaystyle= | f^j​[∑i=1I−j−2Ci,j+1∑i=1I−j−2Ci,j+1+CI−j−1,j+1​F^j+1+CI−j−1,j+1∑i=1I−j−2Ci,j+1+CI−j−1,j+1​F^j+1]\displaystyle\widehat{f}\_{j}\left[\frac{\sum\_{i=1}^{I-j-2}C\_{i,j+1}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}+C\_{I-j-1,j+1}}\,\widehat{F}\_{j+1}+\frac{C\_{I-j-1,j+1}}{\sum\_{i=1}^{I-j-2}C\_{i,j+1}+C\_{I-j-1,j+1}}\,\widehat{F}\_{j+1}\right] |  |
|  |  | =\displaystyle= | f^j​F^j+1=∏l=jJ−1f^l.\displaystyle\widehat{f}\_{j}\,\widehat{F}\_{j+1}~=~\prod\_{l=j}^{J-1}\widehat{f}\_{l}. |  |

This completes the proof.

□\Box