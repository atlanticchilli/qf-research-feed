---
authors:
- Ronald Richman
- Mario V. Wüthrich
doc_id: arxiv:2603.11660v1
family_id: arxiv:2603.11660
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: One-Shot Individual Claims Reserving
url_abs: http://arxiv.org/abs/2603.11660v1
url_html: https://arxiv.org/html/2603.11660v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ronald Richman111insureAI, ronaldrichman@gmail.com
  
Mario V. Wüthrich222Department of Mathematics, ETH Zurich,
mario.wuethrich@math.ethz.ch

(Version of )

###### Abstract

Individual claims reserving has not yet become established in actuarial practice. We attribute this to the absence of a satisfactory methodology: existing approaches tend to be either overly complex or insufficiently flexible and robust for practical use.
Building on the classical chain-ladder (CL) method, we introduced a new perspective on individual claims reserving in Richman and Wüthrich [arXiv:2602.15385]. This manuscript has sparked considerable discussion within the actuarial community. The aim of the present paper is to continue and deepen that discussion, with the ultimate goal of advancing toward a new standard for micro-level reserving.

Keywords. Claims reserving, chain-ladder method, individual claims reserving, micro-level reserving, granular reserving, neural networks, Mack’s method.

## 1 Introduction

We recently uploaded an individual claims reserving proposal to arXiv:2602.15385 that addressed many of the shortcomings present in the published micro-reserving literature; see Richman–Wüthrich [[10](#bib.bib10)]. Starting from the classical chain-ladder (CL) method of Mack [[8](#bib.bib8)], we derived an alternative representation of the ultimate claim predictor. This alternative representation motivates a direct estimation of projection-to-ultimate (PtU) factors which allow for a one-shot forecast of the ultimate claims. The approach extends naturally to individual claims reserving for reported but not settled (RBNS) claims, allowing one to incorporate arbitrary input information (including dynamic stochastic covariates) into the estimation procedure of individual RBNS claims reserves.

Our arXiv paper has stimulated substantial discussion of the proposed approach, indicating that this may be a promising way forward for individual claims reserving. It has also been noted that our main CL result is not new, it had previously appeared in the literature by Lorenz–Schmidt [[5](#bib.bib5)]. The purpose of the present manuscript is to address the many points raised in these discussions and to examine the open issues identified, we also refer to Richman–Wüthrich [[10](#bib.bib10), Section 5] for a list of potential next steps.

We begin by summarizing some of the feedback received; an acknowledgement is found at the end of this section.

* •

  “Maybe I am confusing the methods here but for triangles your PtU factors are called grossing-up factors, could that be? (because I think this recursive technique was already used for triangles in the grossing-up method of (Handbook of Loss Reserving, Radtke, p 127))?”; comment by Florian Gerhardt.

This is indeed correct – thank you! We were not aware of the corresponding result of Lorenz–Schmidt [[6](#bib.bib6), page 130]; in fact, this CL result was first published by the same authors [[5](#bib.bib5)] in 1999. Following their theorem in Lorenz–Schmidt [[6](#bib.bib6), page 130], the authors state “…, the grossing up method is irrelevant in practice.” We believe that this assessment is too pessimistic in the era of machine learning. In our view, precisely this structural perspective provides the key to bringing individual claims reserving into practical applications. This is also supported by the following comments that we received:

* •

  “Your comment ’An alternative of building full simulation models for complex claims processes with multiple stochastic covariates and nested projections is not very practical’ is interesting – this is basically what I was working on at the start of my career! Admittedly without a lot of the complexity you could build into it, because it was too computationally intensive back then. But I’m not at all convinced it’s impractical nowadays.”; comment by Chris Dolman.
* •

  “I experimented with a similar idea several years ago and a couple of clients reported back that it worked well. They kept their existing triangle methods to keep the regulator happy but used the individual claim ultimate cost machine learning approach to inform the triangle parameters.”; comment by Colin Priest.
* •

  “I’ve worked on something very similar two years ago. I called it ’Similarity score weighted micro chain ladder’. It also had the same recursive pattern, but predictions of the point to ultimate estimates per claim were made with simple classification techniques to estimate distance measures between the claim to predict with older claims to take a weighted average point to ultimate (as opposed to using a NN for this as in your case). It becomes computationally complex really quickly. One thing I found quite useful for computational efficiency here was to group claims in operational time bands instead of development periods. This works especially well if you have transaction dates in your data.
  In this work we were specifically looking to close the gap between micro reserving and triangle reserving since adoption of micro reserving has been so poor. Great to see you guys also moving into this space.”; comment by Stephan Marais.
* •

  “Wondering if it’s the same idea as in the addendum [to Semenovich [[12](#bib.bib12)]]?
  This is something I looked into originally 10+ years ago. But never got to a satisfactory formulation around doing joint IBNR and IBNER estimation in a single regression model until the method in the addendum.”; comment by Dimitri Semenovich.
* •

  “Did something similar to estimate prob default after 12 months in IFRS9 …”; comment by Willem Ras.
* •

  “This is really interesting work. I think micro reserving is the next step in reserving, not just for improved accuracy, but also for greater flexibility. As soon as data is compressed into a triangle, much of the claim-level information is lost. Parodi’s triangle-free paper [[9](#bib.bib9)] makes this point nicely with the analogy of moving from a high-resolution to a low-resolution picture.
  Working at claim level makes it easier to reflect environmental shifts, such as inflation shocks, detect changes in business mix earlier or generate different views since IBNR is produced from bottom-up.
  But triangles have survived for nearly a century for a reason: they are simple, robust, and hard to fool. So I expect they will stick around for the foreseeable future.”; comment by Claudio Rebelo.

The above feedback is very exciting, and it seems that many colleagues have been considering such or a similar approach. We see our first main contribution in documenting all these similar thoughts and in making the link to the PtU factors in a CL context, which turned out to be the grossing-up method of Lorenz–Schmidt [[6](#bib.bib6)]. Concerning the last remark, (individual) claims reserving data has a natural triangular structure through censoring at the present evaluation date. The present paper illustrates how triangular methods on aggregated data can be refined to be able to operate on individual claim-level information.

There were two main critical points raised above: the computational side (which indeed may be demanding) and the recursive structure (which may be prone to biases). We will come back to these issues in the next bullet points and in our numerical studies below. The proposal in the addendum to Semenovich [[12](#bib.bib12)] starts from a cross-classified Poisson model, which provides a different way of computing the CL reserves; see Hachemeister–Stanard [[2](#bib.bib2)], Kremer [[3](#bib.bib3)] and Mack [[7](#bib.bib7)]. This cross-classified structure presents a more restrictive model from a mathematical perspective, but from a computational viewpoint it circumvents the recursive estimation and forecast structure. This indeed may provide another very promising alternative, i.e., by solving the model estimation by a single maximum likelihood estimation (MLE) procedure.

* •

  “The approach is very interesting and promising, especially, because it does not propose another ML approach, but it is rather thinking about restructuring the data to preform individual claims reserving.”; comment by Christian Lorentzen.
* •

  “Why don’t you start with a GLM instead of the neural network?”; comment by Christian Lorentzen.
* •

  “Sounds interesting. Certainly jumping to ultimate is more interesting and aligned with UW views on variability. Does the model allow one / nn-time step forward projections? Helps S2 reporters with MVM calcs.”; comment by David Menezes.
* •

  “Curious what the advantage is over just building a GBM that samples over the future space for the underlying data and uses the length of the forecast horizon as one of the inputs?”; comment by Alex Rowley.
* •

  “Nice approach for RBNS under CL! Being a fan of generic lightweight neural models, I recommend exploring an additional pathway, further relaxing model assumptions: the use of a (neural) continuous time-to-event framework including interval censoring. In this context IBNR and RBNS can be interpreted as intermediate states between claim occurrence and final settlement. The entire stochastic claim process then becomes fully explicit, with simulation as the tool for deriving all estimates.”; comment by Anne van der Scheer.

The first item of the above list is a perfect summary of our intention, i.e., it is not about a specific model architecture, but rather about how to organize the data. The second item, starting with a generalized linear model (GLM), is an excellent proposal that we should already have considered in our first paper [[10](#bib.bib10)]. Ultimately, any reasonable regression model may work, the specific choice will depend on its purpose, see Shmueli [[13](#bib.bib13)] on ‘To explain or to predict?’, e.g., for cash flow forecasting or mid-year reserving transformer decoders could be useful tools. However, the proposal of starting with a GLM is a very valid one, and one of the exciting findings of the present case study is that even a linear regression model does an excellent job! The linear regression can be computed very efficiently, and therefore, we can even build on an individual claims bootstrap algorithm here to assess model uncertainty.

If we understand correctly, the last two items of the above list are related to the addendum of Semenovich [[12](#bib.bib12)] who proposed a cross-classified Poisson model that can simultaneously deal with incurred but not reported (IBNR) and RBNS claims. Using the cross-classified Poisson structure, the problem can be solved in closed-form using MLE. For more complex architectures, this seems less clear. As explained in our previous paper [[10](#bib.bib10)], we rather prefer to circumvent a simulation extrapolation as this is a topic with its own difficulties. Adding the length of the forecast horizon may be an interesting proposal to shrink the number of necessary regression models. However, at the current stage, it seems not fully aligned with our recursive structure of estimating the PtU factors.

* •

  “One model per accident period seems a lot.”
* •

  “Can this also be used for quarterly (mid-year) reserving?”
* •

  “It would be nice to have a simple IBNR model to be able to compare the results to classical CL.”

We agree that computationally one model per accident/development period can be demanding. However, this is not any different from the CL method because each CL factor needs to be interpreted as ’one model’ in this set-up: note that each CL factor solves a regression problem (without an intercept). In the present paper, we solve everything with linear regression models which can be computed very efficiently.

It allows for quarterly reserving. In fact, the input can be in continuous time, even if the prediction is only on an annual grid. After year 2000, when many insurance companies transitioned from annual to quarterly reporting, they initially used a grossing-up method to complete a partially observed calendar year to receive an end-of-year forecast. Based on this end-of-year forecast they performed a CL or Bornhuetter–Ferguson [[1](#bib.bib1)] method on an annual grid.

Finally, incurred but not reported (IBNR) claim forecasting is a crucial missing piece in our previous work, Richman–Wüthrich [[10](#bib.bib10)], which we are going to tackle in Section [6](#S6 "6 IBNR reserving ‣ One-Shot Individual Claims Reserving"), below.

Organization of this manuscript.

* •

  Section [2](#S2 "2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") revisits the classic CL method. We discuss the transition from the iterative one-period ahead roll-forward extrapolation method to recursive one-shot ultimate claim prediction using the PtU factors. Typically, this is done on aggregated cumulative payments, and we explain its decomposition to individual claims observations. This paves the path to bootstrapping individual claims histories, and we challenge Mack’s [[8](#bib.bib8)] model error estimate by a corresponding individual claims history bootstrap analysis.
* •

  In Section [3](#S3 "3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), we distinguish claims according to their reporting status – resulting in RBNS and IBNR claims. This is a crucial step in individual claims reserving to ensure that PtU factors are estimated on consistent claims cohorts – this is the first step that significantly differs from CL reserving on aggregated claims, and it is the crucial step to prepare for individual claims reserving. This step also provides a novel decomposition of the classical CL reserves into RBNS reserves and IBNR reserves.
* •

  Section [4](#S4 "4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") is our core section. We dive into individual claims reserving for RBNS claims, and interestingly, we see that a linear regression model on the individual claim features can attain an excellent predictive performance.

  + –

    Section [4.1](#S4.SS1 "4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") presents the generic recursive one-shot PtU forecast algorithm for RBNS claims. This is our core tool for individual claims reserving; see Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").
  + –

    Section [4.2](#S4.SS2 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") gives the first real data application of Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"). This application is fully based on linear regression models (and a Markov assumption).
  + –

    Section [4.3](#S4.SS3 "4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") applies an individual claims history bootstrap to the previous individual claims reserving method. This can be done efficiently because all predictive models are based on linear regressions.
  + –

    Section [4.4](#S4.SS4 "4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") challenges the linear regression models with neural networks, with the result that the networks do not provide a significantly better predictive result.
  + –

    Section [4.5](#S4.SS5 "4.5 Transformer architecture ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") analyzes transformer architectures to see whether we can gain predictive power by inputting the entire past claims history (by dropping the Markov assumption). In our small-scale example, the answer is negative, but this should be reconsidered on bigger datasets to receive better answers, i.e., this section rather provides a proof of concept in the sense that transformers can be integrated into the forecast procedure, and they provide stable results.
* •

  In Section [5](#S5 "5 The role of claims incurred ‣ One-Shot Individual Claims Reserving"), we analyze the predictive power of claims incurred information. Our finding is that on a (small) liability insurance dataset, the claims incurred information gives more accurate forecasts than the individual cumulative payment information, in particular, in combination with the claims status information.
* •

  In Section [6](#S6 "6 IBNR reserving ‣ One-Shot Individual Claims Reserving"), we discuss setting the IBNR reserves for late reported claims. This is performed by a simple CL application on the predicted ultimates of RBNS claims.
* •

  Section [7](#S7 "7 Summary ‣ One-Shot Individual Claims Reserving") concludes and gives an outlook.

Acknowledgement. Thank you very much for the numerous and very useful feedback (in alphabetical order):
Chris Dolman,
Florian Gerhardt,
Syed Kirmani,
Christian Lorentzen,
Stephan Marais,
David Menezes,
Colin Priest,
Willem Ras,
Claudio Rebelo,
Alex Rowley,
Dimitri Semenovich,
Anne van der Scheer.

## 2 Chain-ladder method - revisited

We begin by revisiting Mack’s [[8](#bib.bib8)] CL algorithm and its reformulation that leads to the appealing structure for individual claims reserving using machine learning (ML) methods. This gives us the motivation and the basis for all subsequent derivations; for full technical details we refer to Richman–Wüthrich [[10](#bib.bib10)].

### 2.1 Chain-ladder algorithm - recursive one-shot forecast

This section presents the step going from the one-period ahead roll-forward CL extrapolation to the recursive one-shot ultimate claim forecast. For this we define the PtU factor that allows one to gross-up the last observed cumulative payments.

We consider II accident periods and a maximal development delay JJ, throughout J<IJ<I.
Cumulative payments for the claims in accident period i∈{1,…,I}i\in\{1,\ldots,I\} at development delay j∈{0,…,J}j\in\{0,\ldots,J\} are denoted by Ci,jC\_{i,j}, and we assume that these cumulative payments are strictly positive for all indexes (i,j)(i,j); cumulative payments Ci,jC\_{i,j} means that these variables collect all the payments made for accident year ii within the development periods up to period jj.

At calendar time II, we have observed the upper triangle/trapezoid

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟I={Ci,j;i+j≤I, 1≤i≤I, 0≤j≤J},{\cal D}\_{I}=\left\{C\_{i,j};~i+j\leq I,\,1\leq i\leq I,\,0\leq j\leq J\right\}, |  | (2.1) |

this corresponds to the green triangles in Figures [1](#S2.F1 "Figure 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") and [2](#S2.F2 "Figure 2 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving").
The general goal is to predict the ultimate claims Ci,JC\_{i,J} for all accident periods ii with i+J>Ii+J>I, i.e., the accident periods that are not fully developed at time II.

For the CL reserving method, we estimate the so-called CL factors (fj)j=0J−1(f\_{j})\_{j=0}^{J-1} at time II by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^jCL=∑i=1I−(j+1)Ci,j+1∑i=1I−(j+1)Ci,j.\widehat{f}^{\rm CL}\_{j}=\frac{\sum\_{i=1}^{I-(j+1)}C\_{i,j+1}}{\sum\_{i=1}^{I-(j+1)}C\_{i,j}}. |  | (2.2) |

The CL predictors at time II of the ultimate claims for accident periods i>I−Ji>I-J are defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^i,JCL=Ci,I−i​∏j=I−iJ−1f^jCL;\widehat{C}^{\rm CL}\_{i,J}=C\_{i,I-i}\prod\_{j=I-i}^{J-1}\widehat{f}^{\rm CL}\_{j}; |  | (2.3) |

these are the classic CL predictors; see Mack [[8](#bib.bib8)]. Define the projection-to-ultimate (PtU) factors

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^jCL=∏l=jJ−1f^lCL for j∈{0,…,J−1}.\widehat{F}^{\rm CL}\_{j}=\prod\_{l=j}^{J-1}\widehat{f}^{\rm CL}\_{l}\qquad\text{ for $j\in\{0,\ldots,J-1\}$.} |  | (2.4) |

These give the identical CL predictors for i>I−Ji>I-J

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^i,JCL=Ci,I−i​∏j=I−iJ−1f^jCL=Ci,I−i​F^I−iCL.\widehat{C}^{\rm CL}\_{i,J}=C\_{i,I-i}\prod\_{j=I-i}^{J-1}\widehat{f}^{\rm CL}\_{j}=C\_{i,I-i}\,\widehat{F}^{\rm CL}\_{I-i}. |  | (2.5) |

In the actuarial literature, the PtU factors ([2.4](#S2.E4 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) are also called grossing-up factors, making the reserving method in ([2.5](#S2.E5 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) a grossing-up reserving method; see Lorenz–Schmidt [[6](#bib.bib6)].

![Refer to caption](2603.11660v1/CL1.png)


Figure 1: One-period ahead roll-forward extrapolation to predict the ultimate claims Ci,JC\_{i,J} using the observations Ci,I−iC\_{i,I-i}, i>I−Ji>I-J, at time II (for I=7I=7 and J=6J=6); this figure is taken from [[10](#bib.bib10)].

The mechanics of the CL estimation and prediction procedure ([2.3](#S2.E3 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) is illustrated in
Figure [1](#S2.F1 "Figure 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"). It has the following iterative one-period ahead roll-forward structure

|  |  |  |
| --- | --- | --- |
|  | C^i,JCL=Ci,I−i​∏j=I−iJ−1f^jCL=Ci,I−i⋅f^I−iCL⏟I−i→I−i+1⋅f^I−i+1CL⏟I−i→I−i+2⋅…⋅f^J−1CL.\widehat{C}^{\rm CL}\_{i,J}~=~C\_{i,I-i}\prod\_{j=I-i}^{J-1}\widehat{f}^{\rm CL}\_{j}~=~\underbrace{\underbrace{C\_{i,I-i}\cdot\widehat{f}^{\rm CL}\_{I-i}}\_{I-i~\to~I-i+1}\,\cdot\,\widehat{f}^{\rm CL}\_{I-i+1}}\_{I-i~\to~I-i+2}\,\cdot\,\ldots\,\cdot\,\widehat{f}^{\rm CL}\_{J-1}. |  |

It is precisely this iterative one-period ahead roll-forward extrapolation structure that poses significant difficulties in individual claims reserving using ML methods because dealing with such extrapolations of stochastic processes is generally a difficult problem.
This has led to the idea of trying to perform a direct one-shot forecast of the ultimate claim by directly estimating the PtU factor, where ’directly estimating’ means that we do not go through the iterative one-period ahead construction ([2.4](#S2.E4 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")), but we directly estimate the PtU factor in a single computation, see ([2.6](#S2.E6 "In item (b) ‣ Algorithm 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")).
As proved in
Lorenz–Schmidt [[6](#bib.bib6)] and verified in
Richman–Wüthrich [[10](#bib.bib10), Proposition 2.2], this is possible.
Algorithm [1](#algorithm1 "Algorithm 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") gives this one-shot prediction variant
of the CL predictors ([2.3](#S2.E3 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"));
for mathematical details see Richman–Wüthrich [[10](#bib.bib10), Proposition 2.2], and it is illustrated in Figure [2](#S2.F2 "Figure 2 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving").

Algorithm 1  Recursive one-shot CL prediction algorithm.

* (a)

  Initialization for j=Jj=J.
  For the fully settled accident periods i∈{1,…,I−J}i\in\{1,\ldots,I-J\}, initialize the algorithm by C^i,JCL=Ci,J\widehat{C}^{\rm CL}\_{i,J}=C\_{i,J}.
* (b)

  Iteration j→j−1≥0j\to j-1\geq 0. Compute recursively

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | F^j−1CL=∑i=1I−jC^i,JCL∑i=1I−jCi,j−1 and C^I−(j−1),JCL=CI−(j−1),j−1​F^j−1CL.\widehat{F}^{\rm CL}\_{j-1}=\frac{\sum\_{i=1}^{I-j}\widehat{C}^{\rm CL}\_{i,J}}{\sum\_{i=1}^{I-j}C\_{i,j-1}}\qquad\text{ and }\qquad\widehat{C}^{\rm CL}\_{I-(j-1),J}=C\_{I-(j-1),j-1}\,\widehat{F}^{\rm CL}\_{j-1}. |  | (2.6) |

Remark, the predictors ([2.6](#S2.E6 "In item (b) ‣ Algorithm 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) and ([2.3](#S2.E3 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) are identical; see
Richman–Wüthrich [[10](#bib.bib10), Proposition 2.2]. That is,
([2.6](#S2.E6 "In item (b) ‣ Algorithm 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) gives a different representation of
([2.3](#S2.E3 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) which is more appealing in individual claims reserving.

![Refer to caption](2603.11660v1/CL2.png)


Figure 2: Backward (in time) one-shot predictions of the ultimate claims Ci,JC\_{i,J}, i>I−Ji>I-J, using the ‘directly estimated’ PtU factors (F^jCL)j=0J−1(\widehat{F}^{\rm CL}\_{j})\_{j=0}^{J-1} given in ([2.6](#S2.E6 "In item (b) ‣ Algorithm 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")): (left-middle-right) correspond to j−1=J−1=5j-1=J-1=5, j−1=4j-1=4 and j−1=3j-1=3; this figure is taken from [[10](#bib.bib10)].

### 2.2 Individual claims - available data

This section introduces the individual claims and their individual claim histories. We distinguish between cumulative claims and aggregated claims, and we explain the difference between RBNS and IBNR claims.

The cumulative payments Ci,jC\_{i,j} consider aggregated payments over all claims having occurred in accident period ii up to development period jj. We emphasize that we distinguish the meanings

* •

  of cumulative referring to summing payments over development periods jj, and
* •

  of aggregated referring to summing over different individual claims.

We now shift our focus to individual claims modeling.
Assume there are NiN\_{i} claims that occurred in accident period ii. We label these claims by ν=1,…,Ni\nu=1,\ldots,N\_{i}, and we study each of these claims individually.
Denote the reporting delay of the ν\nu-th claim of accident period ii by Ti|ν≥0T\_{i|\nu}\geq 0; the reporting delay is the time difference between the occurrence period ii of the claim and its reporting (notification) period i+Ti|νi+T\_{i|\nu} at the insurance company. Thus, after reporting delay jj, all claims ν\nu with reporting delay Ti|ν≤jT\_{i|\nu}\leq j are reported at the insurance company, and the claims ν\nu with Ti|ν>jT\_{i|\nu}>j are not reported at time i+ji+j.

For a fixed time point II, called evaluation date, we have the following two classes of claims:

* •

  we call the claims that are not reported yet, i+Ti|ν>Ii+T\_{i|\nu}>I, incurred but not reported (IBNR) claims, and
* •

  all other claims, i+Ti|ν≤Ii+T\_{i|\nu}\leq I, are called reported but not settled (RBNS) claims. By convention, RBNS claims include all reported claims, these can be open or closed (settled), as some closed claims may require a re-opening due to late unexpected further claim developments.

As soon as a claim ν\nu is reported (RBNS), the insurance company starts to collect information about this specific claim. E.g., the insurance company can study its individual cumulative payment process given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci,0:J|ν=[Ci,0|ν​ 1{Ti|ν≤0},Ci,1|ν​ 1{Ti|ν≤1},…,Ci,J|ν​ 1{Ti|ν≤J}].C\_{i,0:J|\nu}=\left[C\_{i,0|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq 0\}},\,C\_{i,1|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq 1\}},\ldots,\,C\_{i,J|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq J\}}\right]. |  | (2.7) |

We mask Ci,j|ν=0C\_{i,j|\nu}=0 all IBNR periods j<Ti|νj<T\_{i|\nu}, i.e., before the claim has been reported to the insurance company; one could also use any other mask value. A lower index 0:J generically denotes a sequence that considers the time indexes j=0,…,Jj=0,\ldots,J.

![Refer to caption](2603.11660v1/FigInd1.png)

![Refer to caption](2603.11660v1/FigInd2.png)

Figure 3: (lhs) Individual cumulative payments Ci,j|νC\_{i,j|\nu} in the upper triangle i+j≤Ii+j\leq I (each row is one claim, period i=4i=4 has twice as many claims as i=3i=3), and (rhs) aggregated cumulative claims Ci,jC\_{i,j} in the upper triangle. Late reportings are illustrated by gray bars in the left-hand side figure.

The aggregated cumulative payments Ci,jC\_{i,j} over all claims that have occurred in accident period ii up to development period jj are then computed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci,j=∑ν=1NiCi,j|ν​ 1{Ti|ν≤j}=∑ν:Ti|ν≤jCi,j|ν,C\_{i,j}=\sum\_{\nu=1}^{N\_{i}}C\_{i,j|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq j\}}=\sum\_{\nu:\,T\_{i|\nu}\leq j}C\_{i,j|\nu}, |  | (2.8) |

we are going to use the latter notation as it is more convenient.
Naturally, but importantly for the further understanding, only RBNS claims can have payments, this motivates the expression Ci,j|ν​ 1{Ti|ν≤j}C\_{i,j|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq j\}} in ([2.7](#S2.E7 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) and ([2.8](#S2.E8 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")).

Figure [3](#S2.F3 "Figure 3 ‣ 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") (lhs) indicates individual cumulative payment histories Ci,0|ν,…,Ci,I−i|νC\_{i,0|\nu},\ldots,C\_{i,I-i|\nu} in the (observed) upper triangle – each row corresponds to one claim. The gray bars show late reported claims, e.g., in the first accident period i=1i=1, there is one claim with reporting delay T1|ν=2T\_{1|\nu}=2. Such claims with a reporting lag of 2 periods are missing for the most recent accident periods i=6,7i=6,7, because they are not reported yet, i.e., they are IBNR claims at the evaluation date I=7I=7. The right-hand side of Figure [3](#S2.F3 "Figure 3 ‣ 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") shows its aggregated version Ci,0,…,Ci,I−iC\_{i,0},\ldots,C\_{i,I-i}, see ([2.8](#S2.E8 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")), where all the payments are aggregated within accident periods ii and development periods jj.

The individual payment information ([2.7](#S2.E7 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) is sufficient to compute the CL predictors ([2.3](#S2.E3 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")). However, often there is additional individual claim information available. We denote the process of the additional individual information by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑿i,0:J|ν=[𝑿i,0|ν​ 1{Ti|ν≤0},𝑿i,1|ν​ 1{Ti|ν≤1},…,𝑿i,J|ν​ 1{Ti|ν≤J}],\boldsymbol{X}\_{i,0:J|\nu}=\left[\boldsymbol{X}\_{i,0|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq 0\}},\,\boldsymbol{X}\_{i,1|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq 1\}},\ldots,\,\boldsymbol{X}\_{i,J|\nu}\,\mathds{1}\_{\{T\_{i|\nu}\leq J\}}\right], |  | (2.9) |

where we again use a mask for 𝑿i,j|ν\boldsymbol{X}\_{i,j|\nu} for all IBNR periods j<Ti|νj<T\_{i|\nu}, this corresponds to the gray bars in Figure [3](#S2.F3 "Figure 3 ‣ 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") (lhs). Thus, each claim ν=1,…,Ni\nu=1,\ldots,N\_{i} of accident period ii is described by a claim settlement process (individual claim history)

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞i|ν=(Ci,0:J|ν,𝑿i,0:J|ν).{\cal C}\_{i|\nu}=(C\_{i,0:J|\nu},\boldsymbol{X}\_{i,0:J|\nu}). |  | (2.10) |

The claim settlement components (Ci,j|ν,𝑿i,j|ν)(C\_{i,j|\nu},\boldsymbol{X}\_{i,j|\nu}) before reporting j<Ti|νj<T\_{i|\nu} are masked as IBNR periods, and at the evaluation date II the entries with indexes i+j>Ii+j>I have not been observed yet, because they lie in the future at time II (this is the lower (white) triangle in Figure [3](#S2.F3 "Figure 3 ‣ 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")).

The additional claim features collect any information about the individual claim, e.g.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑿i,j|ν=(reporting delay Ti|νbusiness lineclaims typesettlement delay jclaim status closed/open at delay jclaims incurred at delay jcase reserves at delay j).\boldsymbol{X}\_{i,j|\nu}=\begin{pmatrix}\text{reporting delay $T\_{i|\nu}$}\\ \text{business line}\\ \text{claims type}\\ \text{settlement delay $j$}\\ \text{claim status closed/open at delay $j$}\\ \text{claims incurred at delay $j$}\\ \text{case reserves at delay $j$}\end{pmatrix}. |  | (2.11) |

The first three entries are static covariates that become available at reporting, the fourth component is a deterministic dynamic covariate (it is dynamic but perfectly predictable), and the last three entries are stochastic dynamic covariates. The information in ([2.11](#S2.E11 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) is called tabular, because it considers structured data that has a tabular form. However, the algorithms presented below can also deal with unstructured data, e.g., we could include a medical report into
𝑿i,j|ν\boldsymbol{X}\_{i,j|\nu} – medical reports are also of stochastic dynamic nature.

For the CL method, we started from a fixed time grid, e.g., a monthly, quarterly or an annual grid, with accident period index ii and development delay index jj living on that grid. The algorithms presented below can also deal with continuous time inputs. In that case, we replace the discrete time version
([2.10](#S2.E10 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞i|ν=(Ci,t|ν,𝑿i,t|ν)t∈[0,J],{\cal C}\_{i|\nu}=(C\_{i,t|\nu},\boldsymbol{X}\_{i,t|\nu})\_{t\in[0,J]}, |  | (2.12) |

that is, we keep a discrete time grid for the accident period ii, but the claim settlement process lives in continuous time t∈[0,J]t\in[0,J]. We keep the discrete time in the accident period ii because the algorithms will be recursive in that time index.

### 2.3 Chain-ladder algorithm on individual claims

This section discusses the computation of the CL factors being ratios of two claim cohorts that are not fully consistent. This precisely motivates the step going from total claims reserves to RBNS claims reserves.
Moreover, we represent the CL factor computation as a minimization problem, which is the key to lift the CL factors to regression functions.

The CL algorithm has been computed on aggregated cumulative payments Ci,jC\_{i,j}. Naturally, we can perform the same computations on individual claims.
In view of ([2.8](#S2.E8 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")), the CL factors computed in formula ([2.2](#S2.E2 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) are equally obtained by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^jCL=∑i=1I−(j+1)∑ν:Ti|ν≤j+1Ci,j+1|ν∑i=1I−(j+1)∑ν:Ti|ν≤jCi,j|ν.\widehat{f}^{\rm CL}\_{j}=\frac{\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j+1}}}C\_{i,j+1|\nu}}{\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j}}}C\_{i,j|\nu}}. |  | (2.13) |

There are two points being worth to be raised in this alternative representation. These two points are going to be crucial for our further discussion and understanding.

(1) The first point is that the nominator and the numerator of ([2.13](#S2.E13 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) do not consider the identical claim cohorts. The difference precisely concerns the claims with reporting delay Ti|ν=j+1T\_{i|\nu}=j+1. This can be seen as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^jCL=∑i=1I−(j+1)∑ν:Ti|ν≤jCi,j+1|ν+∑i=1I−(j+1)∑ν:Ti|ν=j+1Ci,j+1|ν∑i=1I−(j+1)∑ν:Ti|ν≤jCi,j|ν.\widehat{f}^{\rm CL}\_{j}=\frac{\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j}}}C\_{i,j+1|\nu}\,+\,\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}=j+1}}}C\_{i,j+1|\nu}}{\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j}}}C\_{i,j|\nu}}. |  | (2.14) |

That is, the CL factors include a margin for late reported (IBNR) claims –
second term in the numerator of ([2.14](#S2.E14 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) –
and therefore these factors cannot serve as predictors on individual RBNS claims because they will lead to biased estimates on these individual RBNS claims, the total bias being of the size of the predicted IBNR claims. To properly account for this, we are going to modify the CL method in Section [3](#S3 "3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), below.

![Refer to caption](2603.11660v1/FigInd3.png)

Figure 4: Individual RBNS vs. IBNR projection.

Figure [4](#S2.F4 "Figure 4 ‣ 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") illustrates this issue for development step j=2→j+1=3j=2\to j+1=3.
If we want to extrapolate the RBNS claims of accident period i=5i=5, the CL factor should only contain the ratio
of claims that have been reported at settlement delay j=2j=2. In Figure [4](#S2.F4 "Figure 4 ‣ 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), this is not the case: there is one claim ν\nu of accident period i=2i=2 with reporting delay Ti|ν=j+1=3T\_{i|\nu}=j+1=3 (gray bar). Therefore, the columns for j=2j=2 and j+1=3j+1=3 do not contain the identical claims, and the corresponding CL ratio ([2.14](#S2.E14 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) accounts for this IBNR claim as well.

(2) The second point we want to emphasize is that the estimator ([2.13](#S2.E13 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"))
can be received as the solution of a weighted square minimization problem. On aggregated claims, this is related to the variance assumption in Mack’s [[8](#bib.bib8)] distribution-free CL model. On individual claims, this needs some care. At the moment, ([2.14](#S2.E14 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) contains IBNR claims at development delay jj being masked by zero, but it also contains RBNS claims that may have individual cumulative payments Ci,j|ν≥0C\_{i,j|\nu}\geq 0 that are equal zero. That is, on aggregated cumulative claims Ci,jC\_{i,j} we have made the assumption of strict positivity, see Section [2.1](#S2.SS1 "2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), but on individual cumulative claims Ci,j|νC\_{i,j|\nu} we do not want to make this assumption as for quite some of these claims the payments may only occur later. To cope with this problem in the estimation procedure, we
select a small positive constant ϵ>0\epsilon>0, and consider the weighted square minimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^jϵ=arg⁡minfj​{∑i=1I−(j+1)∑ν:Ti|ν≤j+1max⁡{Ci,j|ν,ϵ}​(Ci,j+1|νmax⁡{Ci,j|ν,ϵ}−fj)2},\widehat{f}^{\epsilon}\_{j}=\underset{f\_{j}}{\arg\min}\left\{\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,T\_{i|\nu}\leq j+1}\max\{C\_{i,j|\nu},\epsilon\}\left(\frac{C\_{i,j+1|\nu}}{\max\{C\_{i,j|\nu},\epsilon\}}-f\_{j}\right)^{2}\right\}, |  | (2.15) |

where we impute ϵ\epsilon for non-positive and IBNR claims Ti|ν=j+1T\_{i|\nu}=j+1 at settlement delay jj.
The solution to ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^jϵ=∑i=1I−(j+1)∑ν:Ti|ν≤j+1Ci,j+1|ν∑i=1I−(j+1)∑ν:Ti|ν≤j+1max⁡{Ci,j|ν,ϵ}≤f^jCL with f^jϵ↑f^jCL​ for ϵ↓0.\widehat{f}^{\epsilon}\_{j}=\frac{\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,T\_{i|\nu}\leq j+1}C\_{i,j+1|\nu}}{\sum\_{i=1}^{I-(j+1)}\sum\_{\nu:\,T\_{i|\nu}\leq j+1}\max\{C\_{i,j|\nu},\epsilon\}}~\leq~\widehat{f}^{\rm CL}\_{j}\qquad\text{ with }\qquad\widehat{f}^{\epsilon}\_{j}\uparrow\widehat{f}^{\rm CL}\_{j}\text{~ for $\epsilon\downarrow 0$.} |  | (2.16) |

This shows that we can estimate the CL factors from minimization problems. This observation is the key to lift CL reserving to ML methods, namely, fj=fj​(Ci,0:j|ν,𝑿i,0:j|ν)f\_{j}=f\_{j}(C\_{i,0:j|\nu},\boldsymbol{X}\_{i,0:j|\nu}) in ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) can be made dependent on claim covariates
(Ci,0:j|ν,𝑿i,0:j|ν)(C\_{i,0:j|\nu},\boldsymbol{X}\_{i,0:j|\nu}), which opens to door for regression modeling of the CL factors.
Below, we are going to modify this in three ways:

* (1)

  We will use the one-shot ultimate claim forecast variant as outlined in Algorithm [1](#algorithm1 "Algorithm 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"). This will avoid complicated iterative one-step ahead extrapolations.
* (2)

  We will ensure that the claim cohorts considered in the nominator and numerator in ([2.13](#S2.E13 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) are identical, so that the method is suitable for individual RBNS claim prediction without adding a margin for IBNR claims. IBNR claims require a separate treatment.
* (3)

  We will consider alternative objective functions because optimizing ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) on individual claims and for flexible regression functions fj​(Ci,0:j|ν,𝑿i,0:j|ν)f\_{j}(C\_{i,0:j|\nu},\boldsymbol{X}\_{i,0:j|\nu}) may result in stability issues, caused by non-positive (or small) individual cumulative claims Ci,j|νC\_{i,j|\nu}.

Remarks. Making the CL factors fj​(Ci,0:j|ν,𝑿i,0:j|ν)f\_{j}(C\_{i,0:j|\nu},\boldsymbol{X}\_{i,0:j|\nu}) covariate-dependent has already been considered in Wüthrich [[14](#bib.bib14)]. This reference used a one-step ahead roll-forward extrapolation similar to ([2.3](#S2.E3 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")), resulting in the same difficulties as many other proposed methods in the literature. Another interesting variant is that we could replace the weights of IBNR claims in ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) by (premium) exposures giving us a type of incremental loss ratio method for IBNR claims.

### 2.4 Lab: Chain-ladder reserving and individual bootstrap

This section presents our two running examples (accident insurance and liability insurance) that will be revisited throughout the document. We compute their CL reserves, Mack’s prediction uncertainty estimates, and we benchmark Mack’s model error estimates by individual claims history bootstrap estimates, see Table [3](#S2.T3 "Table 3 ‣ 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving").

In this document, we study two small-scale examples. These small-scale examples provide a proof of concept, and generalization to bigger datasets still needs to be confirmed. To be able to perform a proper proof of concept, we select comparably old data such that not only the upper triangles are observed, but in these two datasets also the lower triangles are known. Thus, any method that we develop on the upper triangle can be benchmarked against the ground truth in the lower triangle in our two examples. Of course, this is very useful for providing evidence that our proposals work; generally, the results that require knowledge of the lower triangle are earmarked by an upper index ‡ in this document, see, e.g., Table [3](#S2.T3 "Table 3 ‣ 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), below. We start by presenting the two datasets, these are the same as in Richman–Wüthrich [[10](#bib.bib10)], and we also copy-paste the explaining text from that reference to describe the data.

#### 2.4.1 Accident insurance data

The first dataset considers accident insurance on an annual scale with 5 fully observed accident years, i.e., we have a fully observed 5×55\times 5 square. For model fitting and forecasting, we only use the upper triangle,
as in Figure [2](#S2.F2 "Figure 2 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), and we benchmark the forecasts against the true ultimates which are available here (having also observed the lower triangle).

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
| Claim status Oi,j|ν∈{0,1}O\_{i,j|\nu}\in\{0,1\} for closed/open at the end of period jj | |
| Binary static covariate for work or leisure accident | |
| Calendar month of accident occurrence | |
| Reporting delay in daily units | |

Table 1: Characteristics of accident dataset.

Table [1](#S2.T1 "Table 1 ‣ 2.4.1 Accident insurance data ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") shows the available data. There are 66,639 reported claims with a fully observed development history over the 5×55\times 5 square. Besides the individual cumulative payment process Ci,0:4|νC\_{i,0:4|\nu}, there is information about the claim status process Oi,0:4|νO\_{i,0:4|\nu}, with Oi,j|ν=1O\_{i,j|\nu}=1 meaning that the ν\nu-th claim of accident year ii is open at the end of settlement delay jj, and closed otherwise. Then, there is static information about: work or leisure related accident, the calendar month of the accident and the reporting delay in daily units. For more information we refer to Richman–Wüthrich [[10](#bib.bib10)].

#### 2.4.2 Liability insurance data

The second dataset considers liability insurance. We again have a fully observed 5×55\times 5 square and for model fitting we only use the upper triangle.

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
| Claim status Oi,j|ν∈{0,1}O\_{i,j|\nu}\in\{0,1\} for closed/open at the end of period jj | |
| Claims incurred Ii,j|ν≥0I\_{i,j|\nu}\geq 0 | |
| Binary static covariate for private vs. commercial liability | |
| Calendar month of accident occurrence | |
| Reporting delay in daily units | |

Table 2: Characteristics of liability dataset.

Table [2](#S2.T2 "Table 2 ‣ 2.4.2 Liability insurance data ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") shows the available data of the liability insurance dataset. The main difference to the previous example is that for this dataset there is also a claims incurred process Ii,0:4|νI\_{i,0:4|\nu} available. The claims incurred process is a claims adjuster’s prediction of the individual ultimate claim that is continuously updated when new information arrives, i.e., this is a stochastic process driven by the claims adjuster’s assessments.

#### 2.4.3 Mack’s chain-ladder method and individual bootstrapping

We start with Mack’s [[8](#bib.bib8)] distribution-free CL method. It allows one to compute the CL reserves at the evaluation date II for each accident year i>I−Ji>I-J, given by

|  |  |  |
| --- | --- | --- |
|  | R^iCL=C^i,JCL−Ci,I−i.\widehat{R}^{\rm CL}\_{i}=\widehat{C}^{\rm CL}\_{i,J}-C\_{i,I-i}. |  |

These CL reserves are benchmarked against the true outstanding loss liabilities (OLL), given by
OLLi=Ci,J−Ci,I−i{\rm OLL}\_{i}=C\_{i,J}-C\_{i,I-i}. These true OLL present the ground truth, and they are given in our small-scale examples because we know the lower triangles.
Table [3](#S2.T3 "Table 3 ‣ 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") shows the CL results for the two datasets summed over all accident years ii, and the column ‘Error‡’ gives the total forecast error

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=I−J+1IC^i,JCL−Ci,J.\sum\_{i=I-J+1}^{I}\widehat{C}^{\rm CL}\_{i,J}-C\_{i,J}. |  | (2.17) |

|  | True OLL‡ | CL Reserves | Proc.Unc. | Est.Err. | RMSEP | Error‡ | % RMSEP‡ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Accident dataset |  |  |  |  |  |  |  |
| Mack’s CL model [[8](#bib.bib8)] | 24,212 | 23,064 | 1,429 | 851 | 1,663 | -1,148 | 69% |
| Individual bootstrap | 24,212 | 22,988 | – | 937 | – | -1,224 | – |
| Liability dataset |  |  |  |  |  |  |  |
| Mack’s CL model [[8](#bib.bib8)] | 15,730 | 11,526 | 1,383 | 1,413 | 1,977 | -4,204 | 213% |
| Individual bootstrap | 15,730 | 11,531 | – | 1,201 | – | -4,199 | – |

Table 3: Mack’s CL results on cumulative payments and CL results using an individual claims history bootstrap; the earmarked columns‡ can only be computed because we know the lower triangle in our two examples.

We observe that in both datasets we underestimate the true OLL by -1,148 and -4,204, respectively, see column ‘Error‡’ corresponding to ([2.17](#S2.E17 "In 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")). To assess the magnitude of this underestimation, we additionally compute Mack’s [[8](#bib.bib8)] rooted mean squared error of prediction (RMSEP), given by the square root of
the conditional MSEP

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | msep∑iCi,J|𝒟I⁡(∑iC^i,JCL)\displaystyle\operatorname{msep}\_{\sum\_{i}C\_{i,J}|{\cal D}\_{I}}\left(\sum\nolimits\_{i}\widehat{C}^{\rm CL}\_{i,J}\right) | =\displaystyle= | 𝔼​[(∑i=I−J+1IC^i,JCL−Ci,J)2|𝒟I]\displaystyle{\mathbb{E}}\left[\left.\left(\sum\_{i=I-J+1}^{I}\widehat{C}^{\rm CL}\_{i,J}-C\_{i,J}\right)^{2}\right|{\cal D}\_{I}\right] |  |
|  |  | =\displaystyle= | Var⁡(∑i=I−J+1ICi,J|𝒟I)⏟process uncertainty+(∑i=I−J+1IC^i,JCL−𝔼​[Ci,J|𝒟I])2⏟estimation error,\displaystyle\underbrace{\operatorname{Var}\left(\left.\sum\_{i=I-J+1}^{I}C\_{i,J}\right|{\cal D}\_{I}\right)}\_{\text{\it process uncertainty}}+\underbrace{\left(\sum\_{i=I-J+1}^{I}\widehat{C}^{\rm CL}\_{i,J}-{\mathbb{E}}\left.\left[C\_{i,J}\right|{\cal D}\_{I}\right]\right)^{2}}\_{\text{\it estimation error}}, |  |

where 𝒟I{\cal D}\_{I} refers to the available cumulative payments at time II, see ([2.1](#S2.E1 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")). One of the main achievements of Mack [[8](#bib.bib8)] was to compute/estimate the (rooted) process uncertainty (‘Proc.Unc.’; also called irreducible risk) and the (rooted) estimation error (‘Est.Err.’; also called model error) under suitable CL assumptions. This then provides the RMSEP. The numerical results are presented in columns ‘Proc.Unc.’, ‘Est.Err.’ and ‘RMSEP’ of Table [3](#S2.T3 "Table 3 ‣ 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") – we always show the rooted versions. We observe that the
forecast error ([2.17](#S2.E17 "In 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) makes
1,148/1,663=69%1,148/1,663=69\% of the RMSEP in the accident insurance case, this is a reasonable deviation (less than one RMSEP), and we cannot reject the CL method in this case.
In the liability insurance case, the CL method seems to perform worse,
the forecast error ([2.17](#S2.E17 "In 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) makes
4,204/1,977=213%4,204/1,977=213\% of the RMSEP. This may lead us to doubt the application of the CL algorithm for the liability insurance data.333The RMSEP is on the level of a standard deviation, so we typically check whether it exceeds two standard deviations (RMSEPs) or not.

Next, we present an individual claims history (non-parametric) bootstrap. In our context, a non-parametric bootstrap is useful to assess the (rooted) estimation error ‘Est.Err.’, i.e., it is useful to analyze the model estimation uncertainty term by re-sampling new upper triangles to evaluate the resulting fluctuations in the CL factor estimates. It is not directly possible to assess the process uncertainty term with an individual claims history bootstrap in our set-up. The issue is that only the oldest accident periods i≤I−Ji\leq I-J have observed ultimate claims Ci,JC\_{i,J} (last column of upper triangle/trapezoid, see Figure [4](#S2.F4 "Figure 4 ‣ 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")), and for all other accident periods i=I−J+1,…,Ii=I-J+1,\ldots,I we cannot re-sample (bootstrap) ultimate claims. If the ultimate claim observations
Ci,JC\_{i,J}, i≤I−Ji\leq I-J, are sufficiently rich, we can project those to the more recent accident periods, otherwise we would not recommend the bootstrap to assess the process uncertainty term, but only the (rooted) estimation error ‘Est.Err.’. The (rooted) estimation error ‘Est.Err.’ can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | ∑i=I−J+1IC^i,JCL−𝔼​[Ci,J|𝒟I]=∑i=I−J+1ICi,I−i​(∏j=I−iJ−1f^jCL−∏j=I−iJ−1fj).\sum\_{i=I-J+1}^{I}\widehat{C}^{\rm CL}\_{i,J}-{\mathbb{E}}\left.\left[C\_{i,J}\right|{\cal D}\_{I}\right]=\sum\_{i=I-J+1}^{I}C\_{i,I-i}\left(\prod\_{j=I-i}^{J-1}\widehat{f}\_{j}^{\rm CL}-\prod\_{j=I-i}^{J-1}f\_{j}\right). |  |

For the non-parametric bootstrap, we randomly draw individual claims
Ci,0:I−i|ν=(Ci,j|ν)j=0I−iC\_{i,0:I-i|\nu}=(C\_{i,j|\nu})\_{j=0}^{I-i} with replacement from the upper individual claims triangle, see Figure [4](#S2.F4 "Figure 4 ‣ 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), such that the bootstrap sample has the same size as the original data sample of individual claims – we perform this drawing with replacement simultaneously over all accident periods i∈{1,…,I}i\in\{1,\ldots,I\} which also introduces some volatility across the accident periods. The resulting bootstrap sample is used to re-estimate the CL factors – by first aggregating the individual bootstrapped claims similarly to ([2.8](#S2.E8 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) resulting in bootstrapped aggregated cumulative payments Ci,j∗C\_{i,j}^{\ast}, i+j≤Ii+j\leq I – and these are then used to compute the estimated bootstrapped CL factors (f^j∗)j=0J−1(\widehat{f}\_{j}^{\ast})\_{j=0}^{J-1} similar to ([2.2](#S2.E2 "In 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")). Then, we compute the bootstrapped ultimate claim predictors by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^i,J∗=Ci,I−i​∏j=I−iJ−1f^j∗,\widehat{C}\_{i,J}^{\ast}=C\_{i,I-i}\prod\_{j=I-i}^{J-1}\widehat{f}\_{j}^{\ast}, |  | (2.18) |

note that the basis Ci,I−iC\_{i,I-i} remains fixed, as this corresponds to the conditioning on 𝒟I{\cal D}\_{I} in the RMSEP, i.e., we do not re-simulate the last diagonal of the upper triangle, we only bootstrap in order to assess the estimation uncertainty in the CL factor estimates. Repeating this re-estimation procedure many times, allows us to assess the average and the standard deviation in the bootstrap predictors C^i,J∗\widehat{C}\_{i,J}^{\ast}, the latter being an estimation uncertainty estimate. We report these bootstrap results (received from 1,000 bootstrap samples) on the lines ‘Individual bootstrap’ in Table [3](#S2.T3 "Table 3 ‣ 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"). The average bootstrap prediction is very well aligned with the original CL predictors C^i,JCL\widehat{C}^{\rm CL}\_{i,J}, thus, the bootstrap does not indicate any bias. The magnitude of the bootstrap standard deviation aligns well with the rooted estimation error estimate of Mack [[8](#bib.bib8)], we have a slightly higher value in the accident dataset (937 vs. 851) and a lower value in the liability dataset (1,201 vs. 1,413), but overall the magnitudes align.

In the above non-parametric bootstrap analysis, we resample the entire upper triangle by drawing with replacement. Another interesting analysis would be to re-sample only one selected accident period ii, this would allow one to assess the impact of a single atypical accident period on the entire claims reserves.

## 3 Chain-ladder RBNS reserving

In a preliminary step towards individual claims reserving, we separate RBNS from IBNR claims. A main motivation for this initial step is that there is individual claims information ([2.9](#S2.E9 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) available for RBNS claims, and we try to optimally use this information to predict the individual ultimates Ci,J|νC\_{i,J|\nu} of RBNS claims ν\nu, i+Ti|ν≤Ii+T\_{i|\nu}\leq I. This is not the case for IBNR claims (because they are not reported yet) and only a collective prediction is possible, e.g., based on exposure information.

### 3.1 Chain-ladder RBNS prediction

This section modifies the recursive one-shot CL prediction algorithm, see Algorithm [1](#algorithm1 "Algorithm 1 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), such that it only predicts RBNS claims. This is achieved by considering consistent claim cohorts in extrapolation; see Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving").

The CL predictions C^i,JCL\widehat{C}^{\rm CL}\_{i,J} cover both the RBNS and the IBNR claims. This comes from the fact that we do not consider the identical claims cohorts in the CL factor estimates, the second term in the numerator in ([2.14](#S2.E14 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) corresponds to IBNR claims at development delay jj, see Figure [4](#S2.F4 "Figure 4 ‣ 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"). It is straightforward to correct for this, and to only consider RBNS claims. We give the one-shot PtU factor version in Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), as this is more convenient.

Algorithm 2  Recursive one-shot CL RBNS prediction algorithm.

* (a)

  Initialization for j=Jj=J.
  For the fully settled accident periods i∈{1,…,I−J}i\in\{1,\ldots,I-J\}, initialize the algorithm by setting C^i,J|νRBNS=Ci,J|ν\widehat{C}^{\rm RBNS}\_{i,J|\nu}=C\_{i,J|\nu} for all claims ν=1,…,Ni\nu=1,\ldots,N\_{i}.
* (b)

  Iteration j→j−1≥0j\to j-1\geq 0. Compute recursively

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | F^j−1RBNS=∑i=1I−j∑ν:Ti|ν≤j−1C^i,J|νRBNS∑i=1I−j∑ν:Ti|ν≤j−1Ci,j−1|ν and C^I−(j−1),J|νRBNS=CI−(j−1),j−1|ν​F^j−1RBNS,\widehat{F}^{\rm RBNS}\_{j-1}=\frac{\sum\_{i=1}^{I-j}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j-1}}}\widehat{C}^{\rm RBNS}\_{i,J|\nu}}{\sum\_{i=1}^{I-j}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j-1}}}C\_{i,j-1|\nu}}\qquad\text{ and }\qquad\widehat{C}^{\rm RBNS}\_{I-(j-1),J|\nu}=C\_{I-(j-1),j-1|\nu}\,\widehat{F}^{\rm RBNS}\_{j-1}, |  | (3.1) |

  for all RBNS claims ν\nu at time II, i.e., with TI−(j−1)|ν≤j−1T\_{I-(j-1)|\nu}\leq j-1.

Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") only extrapolates RBNS claims, and it does not add any margins for IBNR claims because the numerator and nominator of the PtU factors F^j−1RBNS\widehat{F}^{\rm RBNS}\_{j-1} consider the identical RBNS claims cohort Ti|ν≤j−1{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j-1}}.

### 3.2 Chain-ladder IBNR prediction

This section provides a partition of the total CL reserves into RBNS and IBNR reserves. This is a natural consequence of the recursive one-shot CL RBNS prediction algorithm presented in the previous section in Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving").

To forecast the IBNR claims, we can provide a similar algorithm. The IBNR reserves will consist of two different
terms in its estimation: (1) terms stemming from claims that are IBNR at time II, and (2) ultimate claims (estimates) that are used for IBNR prediction, but which are RBNS at time II. For this reason, the following paragraphs will use both upper indices IBNR and RBNS.

Initialize
C^i,J|νRBNS=Ci,J|ν\widehat{C}^{\rm RBNS}\_{i,J|\nu}=C\_{i,J|\nu} for all claims ν=1,…,Ni\nu=1,\ldots,N\_{i}
in accident periods i∈{1,…,I−J}i\in\{1,\ldots,I-J\} – all these are RBNS claims at time II. The first recursive step
J→J−1J\to J-1 considers

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^J−1IBNR=∑i=1I−J∑ν:Ti|ν=JC^i,J|νRBNS∑i=1I−J∑ν:Ti|ν≤J−1Ci,J−1|ν.\widehat{F}^{\rm IBNR}\_{J-1}=\frac{\sum\_{i=1}^{I-J}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}=J}}}\widehat{C}^{\rm RBNS}\_{i,J|\nu}}{\sum\_{i=1}^{I-J}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq J-1}}}C\_{i,J-1|\nu}}. |  | (3.2) |

This gives the (aggregated) IBNR claim prediction for accident period
I−(J−1)I-(J-1)

|  |  |  |
| --- | --- | --- |
|  | C^I−(J−1),JIBNR=[∑ν:TI−(J−1)|ν≤J−1CI−(J−1),J−1|ν]​F^J−1IBNR=CI−(J−1),J−1​F^J−1IBNR.\widehat{C}^{{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{\rm IBNR}}}\_{I-(J-1),J}=\left[\sum\_{\nu:\,T\_{I-(J-1)|\nu}\leq J-1}C\_{I-(J-1),J-1|\nu}\right]\widehat{F}^{\rm IBNR}\_{J-1}=C\_{I-(J-1),J-1}\,\widehat{F}^{\rm IBNR}\_{J-1}. |  |

This considers the grossing-up factor from the observed cumulative payments CI−(J−1),J−1C\_{I-(J-1),J-1} to the IBNR prediction for accident period
I−(J−1)I-(J-1). This can recursively be iterated, but the iteration is cumbersome. E.g., the next step
J−1→J−2J-1\to J-2 looks as follows

|  |  |  |
| --- | --- | --- |
|  | F^J−2IBNR=∑i=1I−(J−1)∑ν:Ti|ν=J−1C^i,J|νRBNS+∑i=1I−J∑ν:Ti|ν=JC^i,J|νRBNS+C^I−(J−1),JIBNR∑i=1I−(J−1)∑ν:Ti|ν≤J−2Ci,J−2|ν.\widehat{F}^{\rm IBNR}\_{J-2}=\frac{\sum\_{i=1}^{I-(J-1)}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}=J-1}}}\widehat{C}^{\rm RBNS}\_{i,J|\nu}\,+\,\sum\_{i=1}^{I-J}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}=J}}}\widehat{C}^{\rm RBNS}\_{i,J|\nu}\,+\,\widehat{C}^{{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{\rm IBNR}}}\_{I-(J-1),J}}{\sum\_{i=1}^{I-(J-1)}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq J-2}}}C\_{i,J-2|\nu}}. |  |

The first term in the numerator corresponds to the RBNS ultimate claim prediction of claims reported with delay Ti|ν=J−1T\_{i|\nu}=J-1, the second term to the prediction of the claims reported with delay Ti|ν=JT\_{i|\nu}=J (all these claims are reported at time II), finally, the last term corresponds to the IBNR part corresponding to accident period I−(J−1)I-(J-1). Thus, we complete the upper-right triangle with IBNR predictions, and the missing part of this development rectangle is directly completed with the previous IBNR predictions C^I−(J−1),JIBNR\widehat{C}^{{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{\rm IBNR}}}\_{I-(J-1),J}, so that all IBNR claims in the upper-right square/rectangle are identified.

A much easier way to receive the identical result is to subtract the RBNS ultimate claim predictors from the CL ones, that is, for all accident periods i>I−Ji>I-J we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^i,JIBNR=C^i,JCL−∑ν:Ti|ν≤I−iC^i,J|νRBNS.\widehat{C}^{\rm IBNR}\_{i,J}=\widehat{C}^{\rm CL}\_{i,J}-\sum\_{\nu:\,T\_{i|\nu}\leq I-i}\widehat{C}^{\rm RBNS}\_{i,J|\nu}. |  | (3.3) |

This gives a simple IBNR predictor for all accident periods.

Remark. A similar, though different approach is considered in Schnieper [[11](#bib.bib11)]. The similarity concerns the fact that Schnieper [[11](#bib.bib11)] also considers development ratios of type ([3.2](#S3.E2 "In 3.2 Chain-ladder IBNR prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")), however, Schnieper [[11](#bib.bib11)] uses an external exposure as nominator in ([3.2](#S3.E2 "In 3.2 Chain-ladder IBNR prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")). Extrapolating this in a one-period ahead roll-over fashion is then peformed, this is doable but can be cumbersome (RBNS CL factors get contaminated by IBNR parts – though in a mathematically consistent way). Having a past cumulative payments nominator and turning the problem to the one-shot ultimate prediction version allows us to receive an elegant decomposition ([3.3](#S3.E3 "In 3.2 Chain-ladder IBNR prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")) in our set-up.

### 3.3 Lab: Chain-ladder RBNS and IBNR reserving

This section provides the example how the CL reserves of Table [3](#S2.T3 "Table 3 ‣ 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") can be partioned into RBNS reserves and IBNR reserves. This uses the RBNS Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and the decomposition formula ([3.3](#S3.E3 "In 3.2 Chain-ladder IBNR prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")).

We revisit the two examples introduced in Section [2.4](#S2.SS4 "2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"). We apply Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") to compute the RBNS reserves. The IBNR reserves are then calculated as the differences ([3.3](#S3.E3 "In 3.2 Chain-ladder IBNR prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")). The results are presented in Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving").

|  | True OLL‡ | Reserves | RMSEP | Error‡ | % RMSEP‡ |
| --- | --- | --- | --- | --- | --- |
| Accident dataset |  |  |  |  |  |
| Mack’s CL model [[8](#bib.bib8)] | 24,212 | 23,064 | 1,663 | -1,148 | 69% |
| RBNS CL prediction, Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | 19,735 | 18,959 | – | -774 | – |
| IBNR CL prediction ([3.3](#S3.E3 "In 3.2 Chain-ladder IBNR prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")) | 4,478 | 4,105 | – | -374 | – |
| Liability dataset |  |  |  |  |  |
| Mack’s CL model [[8](#bib.bib8)] | 15,730 | 11,526 | 1,977 | -4,204 | 213% |
| RBNS CL prediction, Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | 11,494 | 8,601 | – | -2,893 | – |
| IBNR CL prediction ([3.3](#S3.E3 "In 3.2 Chain-ladder IBNR prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")) | 4,236 | 2,925 | – | -1,311 | – |

Table 4: Mack’s CL results on cumulative payments split to RBNS and IBNR reserves; the earmarked columns‡ can only be computed because we know the lower triangle in our examples.

From the results in Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") we conclude that the CL method on RBNS claims seems to work very well for the accident insurance dataset. On the liability insurance dataset, the CL method seems to be negatively biased. We are going to refine this assessment in Section [5](#S5 "5 The role of claims incurred ‣ One-Shot Individual Claims Reserving"), below. We use the ‘RBNS CL prediction’ results of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") as benchmarks for all subsequent individual claims reserving methods on RBNS claims.

### 3.4 Individual claims reserving - setting the stage

In theory, we are now fully prepared to dive into individual claims regression modeling. However, we still want to modify the weighted square loss minimization problem ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) because in fine-grained regression problems, the solutions to the weighted square minimization may not be very robust in case max⁡{Ci,j|ν,ϵ}\max\{C\_{i,j|\nu},\epsilon\} is small. This section introduces an unweighted square loss minimization problem, and we verify that the two problems give similar solutions (in the case without covariates). We do this in two steps, see Listings [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving").

Step 1.
To set the stage for individual claims reserving, we first implement a modified version of Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"). Namely, we bring the PtU factor estimation in
([3.1](#S3.E1 "In item (b) ‣ Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")) into a regression form so that it involves a weighted square loss minimization similar to ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")).

Listing 1: Recursive one-shot CL RBNS algorithm with weighted square loss minimization ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")).

[⬇](data:text/plain;base64,IyMgaW5pdGlhbGl6ZSB1bHRpbWF0ZSBjbGFpbXMgd2l0aCBvYnNlcnZlZCBvbmVzIGZvciBhY2NpZGVudCB5ZWFycyBpPD1JMC1KMApjbGFpbXMkWVkgPC0gTkEKY2xhaW1zW3doaWNoKGNsYWltcyRBY2NEYXRlPD1JMC1KMCksXSRZWSA8LSBjbGFpbXNbd2hpY2goY2xhaW1zJEFjY0RhdGU8PUkwLUowKSxdJFVsdGltYXRlCgplcHNpbG9uIDwtIDAuMDAxICMjIGF2b2lkIGRpdmlzaW9uIGJ5IHplcm8KCiMjIGl0ZXJhdGl2ZSBQdFUgYWxnb3JpdGhtIGZvciBSQk5TIHByZWRpY3Rpb24KZm9yIChqIGluIHJldigwOihKMC0xKSkpewogICAgaSA8LSBJMC1qLTEKICAgICMjIyBwcmVwYXJlIGxlYXJuaW5nIGRhdGEgZm9yIEdMTQogICAgc2VsZWN0IDwtIHdoaWNoKChjbGFpbXMkQWNjRGF0ZTw9aSkmKGNsYWltcyRSZXBEZWxheVlZPD1qKSkKICAgIFlZICAgICA8LSBjbGFpbXNbc2VsZWN0LF0kWVkgICAgICMjIGhhcyBiZWVuIGZpbGxlZCBpbiB0aGUgcHJldmlvdXMgbG9vcAogICAgQ0MgICAgIDwtIHBtYXgoZXBzaWxvbiwgdHJpQ0Nbc2VsZWN0LCBwYXN0ZTAoIlgiLGopXSkgICMjIHRoZXNlIGFyZSBjdW11bGF0aXZlIGNhc2hmbG93cwogICAgbGVhcm4gIDwtIGRhdGEuZnJhbWUoY2JpbmQoWVksIENDKSkKICAgICMjIyBwcmVwYXJlIHRlc3QgZGF0YSBmb3IgUHRVIHByb2plY3Rpb24KICAgIHNlbGVjdCA8LSB3aGljaChjbGFpbXMkQWNjRGF0ZT09KGkrMSkpCiAgICBZWSAgICAgPC0gY2xhaW1zW3NlbGVjdCxdJFlZICAgICAjIyBpcyBOL0EKICAgIENDICAgICA8LSB0cmlDQ1tzZWxlY3QsIHBhc3RlMCgiWCIsaildCiAgICB0ZXN0ICAgPC0gZGF0YS5mcmFtZShjYmluZChZWSwgQ0MpKQogICAgIyMjIHBlcmZvcm0gd2VpZ2h0ZWQgc3F1YXJlIGxvc3MgKEcpTE0gLSBpZGVudGl0eS1saW5rIGlzIHVzZWQgCiAgICBnbG0xICAgPC0gZ2xtKFlZL0NDIH4gMSwgc3RhcnQ9MCwgd2VpZ2h0cz1DQywgZGF0YT1sZWFybiwgZmFtaWx5PWdhdXNzaWFuKCkpCiAgICBjbGFpbXNbc2VsZWN0LCBdJFlZIDwtIHRlc3QkQ0MgKiBwcmVkaWN0KGdsbTEsIG5ld2RhdGE9dGVzdCwgdHlwZT1jKCJyZXNwb25zZSIpKQogICAgICAgfQo=)

1## initialize ultimate claims with observed ones for accident years i<=I0-J0

2claims$YY <- NA

3claims[which(claims$AccDate<=I0-J0),]$YY <- claims[which(claims$AccDate<=I0-J0),]$Ultimate

4

5epsilon <- 0.001 ## avoid division by zero

6

7## iterative PtU algorithm for RBNS prediction

8for (j in rev(0:(J0-1))){

9 i <- I0-j-1

10 ### prepare learning data for GLM

11 select <- which((claims$AccDate<=i)&(claims$RepDelayYY<=j))

12 YY <- claims[select,]$YY ## has been filled in the previous loop

13 CC <- pmax(epsilon, triCC[select, paste0("X",j)]) ## these are cumulative cashflows

14 learn <- data.frame(cbind(YY, CC))

15 ### prepare test data for PtU projection

16 select <- which(claims$AccDate==(i+1))

17 YY <- claims[select,]$YY ## is N/A

18 CC <- triCC[select, paste0("X",j)]

19 test <- data.frame(cbind(YY, CC))

20 ### perform weighted square loss (G)LM - identity-link is used

21 glm1 <- glm(YY/CC ~ 1, start=0, weights=CC, data=learn, family=gaussian())

22 claims[select, ]$YY <- test$CC \* predict(glm1, newdata=test, type=c("response"))

23 }

Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") reformulates Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") with the PtU factor computation in ([3.1](#S3.E1 "In item (b) ‣ Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")) replaced by a linear regression (GLM with identity link) and using a weighted square loss minimization ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) for model fitting; see line 21 of Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"). Since RBNS claims can have individual cumulative payments Ci,j−1|νC\_{i,j-1|\nu} being equal to zero, we selected a small positive constant ϵ=0.001\epsilon=0.001 to avoid dividing by zero, see lines 13 and 21 of Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"). The solution of this algorithm gives the identical reserves as Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), up to the
ϵ>0\epsilon>0 correction factor, we also refer to ([2.16](#S2.E16 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")).

| ii | True OLL‡ | RBNS Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | RBNS Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Error‡ | Ind.RMSE‡ |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | 339 | -14 | 1.499 |
| 3 | 1,017 | 1,305 | 1,305 | 288 | 2.956 |
| 4 | 3,102 | 3,099 | 3,099 | -2 | 4.263 |
| 5 | 15,263 | 14,216 | 14,216 | -1,046 | 8.240 |
| Total | 19,735 | 18,959 | 18,959 | -774 |  |

Table 5: Accident insurance: RBNS results of individual claims prediction using Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"); the earmarked columns‡ use the ground truth in the lower triangle.

Table [5](#S3.T5 "Table 5 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") verifies that Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") give the same results. The first column shows the true OLL for each accident years i∈{1,…,5}i\in\{1,\ldots,5\}. Columns
‘RBNS Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")’ and ‘RBNS Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")’ verify that the two algorithms give the same results.
The column ‘Error‡’ shows how the total RBNS forecast error of -774 splits across the different accident years i∈{1,…,5}i\in\{1,\ldots,5\}, see also second line of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving").

The final column ‘Ind.RMSE‡’ of Table [5](#S3.T5 "Table 5 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") will be the quantity of major interest for all subsequent models. It considers the rooted mean square error (RMSE) on an individual claims level, that is, we define the individual average RBNS prediction errors by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ind.RMSEi‡=1∑ν:Ti|ν≤I−i1​∑ν:Ti|ν≤I−i(C^i,J|νRBNS−Ci,J|ν)2 for i≥I−J.\text{Ind.RMSE}^{\ddagger}\_{i}=\sqrt{\frac{1}{\sum\_{\nu:\,T\_{i|\nu}\leq I-i}1}~\sum\_{\nu:\,T\_{i|\nu}\leq I-i}\left(\widehat{C}^{\rm RBNS}\_{i,J|\nu}-C\_{i,J|\nu}\right)^{2}}\qquad\text{ for $i\geq I-J$.} |  | (3.4) |

This is the average prediction accuracy on the individual claims level (measured by the RMSE). Typically, with improved models, we expect these numbers to decrease. Remark that we can compute ([3.4](#S3.E4 "In 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")) in our examples because we know the lower triangle, earmarked by ‡.

Step 2.
Before starting with individual claims reserving, we still modify the algorithm once more. Namely, we want to remove the weighting in the square loss minimization to robustify the prediction algorithm (this also allows us to get rid of the constant ϵ>0\epsilon>0). For this, we replace the weighted square minimization ([2.15](#S2.E15 "In 2.3 Chain-ladder algorithm on individual claims ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) by the following linear regression problem for RBNS reserving

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϑ^j−1=arg⁡minϑ=(ϑ0,ϑ1)⊤∈ℝ2​{∑i=1I−j∑ν:Ti|ν≤j−1(C^i,J|ν−(ϑ0+ϑ1​Ci,j−1|ν))2}.\widehat{\boldsymbol{\vartheta}}\_{j-1}=\underset{\boldsymbol{\vartheta}=(\vartheta\_{0},\vartheta\_{1})^{\top}\in{\mathbb{R}}^{2}}{\arg\min}\left\{\sum\_{i=1}^{I-j}\sum\_{\nu:\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j-1}}}\left(\widehat{C}\_{i,J|\nu}-\left(\vartheta\_{0}+\vartheta\_{1}C\_{i,j-1|\nu}\right)\right)^{2}\right\}. |  | (3.5) |

We add an intercept ϑ0∈ℝ\vartheta\_{0}\in{\mathbb{R}} and drop the weighting (for more robustness).
Naturally, this gives a different solution. We verify in Table [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") that the solution is close to the weighted version. Moreover, using the identity link in the square loss minimization ([3.5](#S3.E5 "In 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"))
implies that the (in-sample) balance property is fulfilled; see Lindholm–Wüthrich [[4](#bib.bib4)]. This is an important property that ensures bias control in our recursive estimation procedure.
The code is provided in Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"); and this is the basic code to dive into regression modeling for RBNS reserving.

Listing 2: Recursive one-shot RBNS reserving algorithm using a Gaussian linear regression ([3.5](#S3.E5 "In 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")).

[⬇](data:text/plain;base64,IyMgaW5pdGlhbGl6ZSB1bHRpbWF0ZSBjbGFpbXMgd2l0aCBvYnNlcnZlZCBvbmVzIGZvciBhY2NpZGVudCB5ZWFycyBpPD1JMC1KMApjbGFpbXMkWVkgPC0gTkEKY2xhaW1zW3doaWNoKGNsYWltcyRBY2NEYXRlPD1JMC1KMCksXSRZWSA8LSBjbGFpbXNbd2hpY2goY2xhaW1zJEFjY0RhdGU8PUkwLUowKSxdJFVsdGltYXRlCgojIyBpdGVyYXRpdmUgUHRVIGFsZ29yaXRobSBmb3IgUkJOUyBwcmVkaWN0aW9uCmZvciAoaiBpbiByZXYoMDooSjAtMSkpKXsKICAgIGkgPC0gSTAtai0xCiAgICAjIyMgcHJlcGFyZSBsZWFybmluZyBkYXRhIGZvciBHTE0KICAgIHNlbGVjdCA8LSB3aGljaCgoY2xhaW1zJEFjY0RhdGU8PWkpJihjbGFpbXMkUmVwRGVsYXlZWTw9aikpCiAgICBZWSAgICAgPC0gY2xhaW1zW3NlbGVjdCxdJFlZICAgICAjIyBoYXMgYmVlbiBmaWxsZWQgaW4gdGhlIHByZXZpb3VzIGxvb3AKICAgIENDICAgICA8LSB0cmlDQ1tzZWxlY3QsIHBhc3RlMCgiWCIsaildICAjIyB0aGVzZSBhcmUgY3VtdWxhdGl2ZSBjYXNoZmxvd3MKICAgIGxlYXJuICA8LSBkYXRhLmZyYW1lKGNiaW5kKFlZLCBDQykpCiAgICAjIyMgcHJlcGFyZSB0ZXN0IGRhdGEgZm9yIFB0VSBwcm9qZWN0aW9uCiAgICBzZWxlY3QgPC0gd2hpY2goY2xhaW1zJEFjY0RhdGU9PShpKzEpKQogICAgWVkgICAgIDwtIGNsYWltc1tzZWxlY3QsXSRZWSAgICAgIyMgaXMgTi9BCiAgICBDQyAgICAgPC0gdHJpQ0Nbc2VsZWN0LCBwYXN0ZTAoIlgiLGopXQogICAgdGVzdCAgIDwtIGRhdGEuZnJhbWUoY2JpbmQoWVksIENDKSkKICAgICMjIyBwZXJmb3JtIHNxdWFyZSBsb3NzIChHKUxNIC0gaWRlbnRpdHktbGluayBpcyB1c2VkIAogICAgZ2xtMiAgIDwtIGdsbShZWSB+IENDLCBkYXRhPWxlYXJuLCBmYW1pbHk9Z2F1c3NpYW4oKSkKICAgIGNsYWltc1tzZWxlY3QsIF0kWVkgPC0gcHJlZGljdChnbG0yLCBuZXdkYXRhPXRlc3QsIHR5cGU9YygicmVzcG9uc2UiKSkKICAgICAgIH0K)

1## initialize ultimate claims with observed ones for accident years i<=I0-J0

2claims$YY <- NA

3claims[which(claims$AccDate<=I0-J0),]$YY <- claims[which(claims$AccDate<=I0-J0),]$Ultimate

4

5## iterative PtU algorithm for RBNS prediction

6for (j in rev(0:(J0-1))){

7 i <- I0-j-1

8 ### prepare learning data for GLM

9 select <- which((claims$AccDate<=i)&(claims$RepDelayYY<=j))

10 YY <- claims[select,]$YY ## has been filled in the previous loop

11 CC <- triCC[select, paste0("X",j)] ## these are cumulative cashflows

12 learn <- data.frame(cbind(YY, CC))

13 ### prepare test data for PtU projection

14 select <- which(claims$AccDate==(i+1))

15 YY <- claims[select,]$YY ## is N/A

16 CC <- triCC[select, paste0("X",j)]

17 test <- data.frame(cbind(YY, CC))

18 ### perform square loss (G)LM - identity-link is used

19 glm2 <- glm(YY ~ CC, data=learn, family=gaussian())

20 claims[select, ]$YY <- predict(glm2, newdata=test, type=c("response"))

21 }



|  |  | RBNS | RBNS | Error‡ | Error‡ | Ind.RMSE‡ | Ind.RMSE‡ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ii | True OLL‡ | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | 337 | -14 | -16 | 1.499 | 1.489 |
| 3 | 1,017 | 1,305 | 1,338 | 288 | 321 | 2.956 | 2.985 |
| 4 | 3,102 | 3,099 | 3,264 | -2 | 163 | 4.263 | 4.262 |
| 5 | 15,263 | 14,216 | 14,137 | -1,046 | -1,126 | 8.240 | 8.218 |
| Total | 19,735 | 18,959 | 19,076 | -774 | -658 |  |  |

Table 6: Accident insurance: RBNS results of individual claims prediction using Listings [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"); the earmarked columns‡ use the ground truth in the lower triangle.

Table [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") compares the results of the algorithms given in Listings [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"). This verifies that the two algorithms provide very similar results. We have a preference for the second algorithm, as it is more robust and easy to extend. In fact, this similarity between the results of Listings [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") should be checked case by case, and on small portfolios with volatile claims it might be violated.

We are now ready: The results of Table [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") serve as benchmark for all subsequent derivations on individual RBNS claims reserving (involving past claims histories).

## 4 Individual ultimate prediction - one-shot micro reserving

We now turn our attention to ML applications for individual RBNS claims reserving.
For this we recall the individual claim settlement process ([2.10](#S2.E10 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")), which is
given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞i|ν=[(Ci,0|ν𝑿i,0|ν)​𝟙{Ti|ν≤0},(Ci,1|ν𝑿i,1|ν)​𝟙{Ti|ν≤1},…,(Ci,J|ν𝑿i,J|ν)​𝟙{Ti|ν≤J}],{\cal C}\_{i|\nu}=\left[\begin{pmatrix}C\_{i,0|\nu}\\ \boldsymbol{X}\_{i,0|\nu}\end{pmatrix}\mathds{1}\_{\{T\_{i|\nu}\leq 0\}},\,\begin{pmatrix}C\_{i,1|\nu}\\ \boldsymbol{X}\_{i,1|\nu}\end{pmatrix}\mathds{1}\_{\{T\_{i|\nu}\leq 1\}},\ldots,\,\begin{pmatrix}C\_{i,J|\nu}\\ \boldsymbol{X}\_{i,J|\nu}\end{pmatrix}\mathds{1}\_{\{T\_{i|\nu}\leq J\}}\right], |  | (4.1) |

all IBNR periods j<Ti|νj<T\_{i|\nu} are masked, and the periods i+j>Ii+j>I have not been observed yet, because they lie in the future at the evaluation date II.

Assumption. We assume that the individual claims processes 𝒞i|ν{\cal C}\_{i|\nu} are independent, and that they are conditionally i.i.d., given the static covariates.

### 4.1 Recursive individual RBNS claims reserving

This section introduces the generic algorithm for recursive one-shot forecasting using general ML regression models.
An important point is the consistent consideration of past information for estimating and forecasting RBNS claims, see
learning sample ([4.2](#S4.E2 "In item (b1) ‣ item (b) ‣ Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")).

In view of Algorithm [2](#algorithm2 "Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")
and Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), it is obvious how to lift these algorithms to general ML regression models for RBNS reserving. Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") gives the generic algorithm. The important point is that one always considers consistent cohorts for PtU factor estimation and projection.
This is indicated by the choice of the learning sample ℒj−1{\cal L}\_{j-1}
in Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), see ([4.2](#S4.E2 "In item (b1) ‣ item (b) ‣ Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")), constraining the inputs by Ti|ν≤j−1T\_{i|\nu}\leq j-1.

Algorithm 3  Generic recursive one-shot PtU forecast algorithm for RBNS claims.

* (a)

  Initialization for j=Jj=J.
  For the fully settled accident periods i∈{1,…,I−J}i\in\{1,\ldots,I-J\}, initialize the algorithm by setting C^i,J|ν=Ci,J|ν\widehat{C}\_{i,J|\nu}=C\_{i,J|\nu} for all claims ν=1,…,Ni\nu=1,\ldots,N\_{i}.
* (b)

  Iteration j→j−1≥0j\to j-1\geq 0.

  + (b1)

    Select the learning sample

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | ℒj−1={(C^i,J|ν,(Ci,l|ν,𝑿i,l|ν)l=0j−1);Ti|ν≤j−1​ and ​i≤I−j}.{\cal L}\_{j-1}=\left\{\left(\widehat{C}\_{i,J|\nu},(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right);\,{\color[rgb]{1,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,1}\pgfsys@color@cmyk@stroke{0}{1}{0}{0}\pgfsys@color@cmyk@fill{0}{1}{0}{0}{T\_{i|\nu}\leq j-1}}\text{ and }i\leq I-j\right\}. |  | (4.2) |
  + (b2)

    Fit a regression model μj−1\mu\_{j-1} on the learning sample ℒj−1{\cal L}\_{j-1} by using

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | (Ci,l|ν,𝑿i,l|ν)l=0j−1↦μj−1​((Ci,l|ν,𝑿i,l|ν)l=0j−1)=𝔼​[C^i,J|ν|(Ci,l|ν,𝑿i,l|ν)l=0j−1].(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}~\mapsto~\mu\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right)={\mathbb{E}}\left[\widehat{C}\_{i,J|\nu}\left|(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right]\right.. |  | (4.3) |
  + (b3)

    Compute the predictions of the RBNS claims ν\nu of accident year I−(j−1)I-(j-1) by

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | C^I−(j−1),J|ν=μj−1​((CI−(j−1),l|ν,𝑿I−(j−1),l|ν)l=0j−1).\widehat{C}\_{I-(j-1),J|\nu}=\mu\_{j-1}\left((C\_{I-(j-1),l|\nu},\boldsymbol{X}\_{I-(j-1),l|\nu})\_{l=0}^{j-1}\right). |  | (4.4) |

###### Remarks 4.1 (Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"))

* •

  Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") is a special case of Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), where the only input information used is the latest individual cumulative payment, see ([3.5](#S3.E5 "In 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")). That is,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | μj−1​((Ci,l|ν,𝑿i,l|ν)l=0j−1)=μj−1​(Ci,j−1|ν).\mu\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right)=\mu\_{j-1}\left(C\_{i,j-1|\nu}\right). |  | (4.5) |

  This makes it obvious how to lift Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") to a general ML forecast algorithm.
* •

  Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") describes one-shot PtU forecasting of RBNS claims. Recursively going from settlement period jj to period j−1j-1, we aim at forecasting the RBNS claims of
  accident periods I−(j−1)I-(j-1), see ([4.4](#S4.E4 "In item (b3) ‣ item (b) ‣ Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")). Since these claims are RBNS claims at time II, they can have a maximal reporting delay of
  Ti|ν≤j−1T\_{i|\nu}\leq j-1. This is then reflected in the learning sample ℒj−1{\cal L}\_{j-1} by setting the corresponding side constraint, see ([4.2](#S4.E2 "In item (b1) ‣ item (b) ‣ Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")). Thus, the learning sample and the forecast problem consider the same side constraint in building their claims cohorts.
* •

  Since we do not know the true ultimate claims Ci,J|νC\_{i,J|\nu} for accident periods i>I−Ji>I-J, we recursively replace them by their
  forecasts C^i,J|ν\widehat{C}\_{i,J|\nu}, see ([4.2](#S4.E2 "In item (b1) ‣ item (b) ‣ Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")). This is completely analogous to the one-shot RBNS prediction ([3.1](#S3.E1 "In item (b) ‣ Algorithm 2 ‣ 3.1 Chain-ladder RBNS prediction ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")).
  Using the tower property for conditional expectation, this is justified as follows

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | (Ci,l|ν,𝑿i,l|ν)l=0j−1↦μj−1​((Ci,l|ν,𝑿i,l|ν)l=0j−1)\displaystyle(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}~\mapsto~\mu\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right) | =\displaystyle= | 𝔼​[Ci,J|ν|(Ci,l|ν,𝑿i,l|ν)l=0j−1]\displaystyle{\mathbb{E}}\left[C\_{i,J|\nu}\left|(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right]\right. |  |
  |  |  | =\displaystyle= | 𝔼​[C^i,J|ν|(Ci,l|ν,𝑿i,l|ν)l=0j−1].\displaystyle{\mathbb{E}}\left[\widehat{C}\_{i,J|\nu}\left|(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right]\right.. |  |

  The latter can be learned from the learning sample ℒj−1{\cal L}\_{j-1} given in ([4.2](#S4.E2 "In item (b1) ‣ item (b) ‣ Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")).
  Recursive iteration completes the forecasting, and it is aligned with Figure [2](#S2.F2 "Figure 2 ‣ 2.1 Chain-ladder algorithm - recursive one-shot forecast ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving").
* •

  From Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") it is obvious that this forecast procedure can deal with any (dynamic) input information, in particular, we can also consider continuous time inputs ([2.12](#S2.E12 "In 2.2 Individual claims - available data ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) and unstructured data.
* •

  In practical applications, the only critical item of this algorithm is its recursive nature. In particular, we need to perform a careful bias control because a bias can easily propagate through the recursive forecast architecture.
  In Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") we consider a Gaussian linear regression problem, and MLE provides the in-sample balance property, thus, it provides an in-sample guarantee of unbiasedness. For more complex ML algorithms we need to enforce this balance property manually, e.g., by a post correction or by regularization, we come back to this in ([4.9](#S4.E9 "In 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")), below.

### 4.2 Lab: Accident insurance example – linear regression

This section gives first explicit examples of the one-shot PtU forecast Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"). It uses a (simple) linear rgression on the available covariates of the last observed period. The first example in Table [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") only considers individual cumulative payments and the claim status, the second example in Table [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") considers all available covariates at time j−1j-1.

We revisit the example of Table [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and we challenge the results by more complex regression models based on Algorithm
[3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").

Listing 3: Recursive one-shot PtU RBNS algorithm including the latest claim status.

[⬇](data:text/plain;base64,IyMgaW5pdGlhbGl6ZSB1bHRpbWF0ZSBjbGFpbXMgd2l0aCBvYnNlcnZlZCBvbmVzIGZvciBhY2NpZGVudCB5ZWFycyBpPD1JMC1KMApjbGFpbXMkWVkgPC0gTkEKY2xhaW1zW3doaWNoKGNsYWltcyRBY2NEYXRlPD1JMC1KMCksXSRZWSA8LSBjbGFpbXNbd2hpY2goY2xhaW1zJEFjY0RhdGU8PUkwLUowKSxdJFVsdGltYXRlCgojIyBpdGVyYXRpdmUgUHRVIGFsZ29yaXRobSBmb3IgUkJOUyBwcmVkaWN0aW9uCmZvciAoaiBpbiByZXYoMDooSjAtMSkpKXsKICAgIGkgPC0gSTAtai0xCiAgICAjIyMgcHJlcGFyZSBsZWFybmluZyBkYXRhIGZvciBHTE0KICAgIHNlbGVjdCA8LSB3aGljaCgoY2xhaW1zJEFjY0RhdGU8PWkpJihjbGFpbXMkUmVwRGVsYXlZWTw9aikpCiAgICBZWSAgICAgPC0gY2xhaW1zW3NlbGVjdCxdJFlZICAgICAjIyBoYXMgYmVlbiBmaWxsZWQgaW4gdGhlIHByZXZpb3VzIGxvb3AKICAgIENDICAgICA8LSB0cmlDQ1tzZWxlY3QsIHBhc3RlMCgiWCIsaildICAjIyB0aGVzZSBhcmUgY3VtdWxhdGl2ZSBjYXNoZmxvd3MKICAgIFN0YXR1cyA8LSB0cmlPT1tzZWxlY3QsIHBhc3RlMCgiWCIsaildICAjIyBjbGFpbSBzdGF0dXMgcHJvY2VzcwogICAgbGVhcm4gIDwtIGRhdGEuZnJhbWUoY2JpbmQoWVksIENDLCBTdGF0dXMpKQogICAgIyMjIHByZXBhcmUgdGVzdCBkYXRhIGZvciBQdFUgcHJvamVjdGlvbgogICAgc2VsZWN0IDwtIHdoaWNoKGNsYWltcyRBY2NEYXRlPT0oaSsxKSkKICAgIFlZICAgICA8LSBjbGFpbXNbc2VsZWN0LF0kWVkgICAgICMjIGlzIE4vQQogICAgQ0MgICAgIDwtIHRyaUNDW3NlbGVjdCwgcGFzdGUwKCJYIixqKV0KICAgIFN0YXR1cyA8LSB0cmlPT1tzZWxlY3QsIHBhc3RlMCgiWCIsaildCiAgICB0ZXN0ICAgPC0gZGF0YS5mcmFtZShjYmluZChZWSwgQ0MsIFN0YXR1cykpCiAgICAjIyMgcGVyZm9ybSBzcXVhcmUgbG9zcyAoRylMTSAtIGlkZW50aXR5LWxpbmsgaXMgdXNlZCAKICAgIGdsbTIgICA8LSBnbG0oWVkgfiBDQypTdGF0dXMsIGRhdGE9bGVhcm4sIGZhbWlseT1nYXVzc2lhbigpKQogICAgY2xhaW1zW3NlbGVjdCwgXSRZWSA8LSBwcmVkaWN0KGdsbTIsIG5ld2RhdGE9dGVzdCwgdHlwZT1jKCJyZXNwb25zZSIpKQogICAgICAgfQo=)

1## initialize ultimate claims with observed ones for accident years i<=I0-J0

2claims$YY <- NA

3claims[which(claims$AccDate<=I0-J0),]$YY <- claims[which(claims$AccDate<=I0-J0),]$Ultimate

4

5## iterative PtU algorithm for RBNS prediction

6for (j in rev(0:(J0-1))){

7 i <- I0-j-1

8 ### prepare learning data for GLM

9 select <- which((claims$AccDate<=i)&(claims$RepDelayYY<=j))

10 YY <- claims[select,]$YY ## has been filled in the previous loop

11 CC <- triCC[select, paste0("X",j)] ## these are cumulative cashflows

12 Status <- triOO[select, paste0("X",j)] ## claim status process

13 learn <- data.frame(cbind(YY, CC, Status))

14 ### prepare test data for PtU projection

15 select <- which(claims$AccDate==(i+1))

16 YY <- claims[select,]$YY ## is N/A

17 CC <- triCC[select, paste0("X",j)]

18 Status <- triOO[select, paste0("X",j)]

19 test <- data.frame(cbind(YY, CC, Status))

20 ### perform square loss (G)LM - identity-link is used

21 glm2 <- glm(YY ~ CC\*Status, data=learn, family=gaussian())

22 claims[select, ]$YY <- predict(glm2, newdata=test, type=c("response"))

23 }

We start by a simple linear regression model that only additionally considers the latest claim status
Oi,j−1|ν∈{0,1}O\_{i,j-1|\nu}\in\{0,1\} in the input information. Thus, we consider whether the ν\nu-th claim of accident period ii is closed or open after settlement delay j−1j-1.
The reason for this choice is that the claim status information is the most important one to forecast whether there are more payments on a given claim.
For the regression function ([4.3](#S4.E3 "In item (b2) ‣ item (b) ‣ Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")), we select a simple linear regression model with an interaction term, that is, we set

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | μj−1​((Ci,l|ν,𝑿i,l|ν)l=0j−1)\displaystyle\mu\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right) | =\displaystyle= | ϑ0+ϑ1​Ci,j−1|ν+ϑ2​Oi,j−1|ν+ϑ3​Ci,j−1|ν​Oi,j−1|ν\displaystyle\vartheta\_{0}+\vartheta\_{1}\,C\_{i,j-1|\nu}+\vartheta\_{2}\,O\_{i,j-1|\nu}+\vartheta\_{3}\,C\_{i,j-1|\nu}\,O\_{i,j-1|\nu} |  | (4.6) |
|  |  | =\displaystyle= | (ϑ0+ϑ2​Oi,j−1|ν)+(ϑ1+ϑ3​Oi,j−1|ν)​Ci,j−1|ν,\displaystyle\left(\vartheta\_{0}+\vartheta\_{2}\,O\_{i,j-1|\nu}\right)+\left(\vartheta\_{1}+\vartheta\_{3}\,O\_{i,j-1|\nu}\right)C\_{i,j-1|\nu}, |  |

for regression parameter (ϑk)k=03∈ℝ4(\vartheta\_{k})\_{k=0}^{3}\in{\mathbb{R}}^{4}.
Basically, this means that open claims are regressed with parameters ϑ0+ϑ2\vartheta\_{0}+\vartheta\_{2} and ϑ1+ϑ3\vartheta\_{1}+\vartheta\_{3}, and closed claims are regressed with parameters ϑ0\vartheta\_{0} and ϑ1\vartheta\_{1}. This is implemented in Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), and the results are shown in Table [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").

|  |  | RBNS | RBNS | Error‡ | Error‡ | Ind.RMSE‡ | Ind.RMSE‡ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ii | True OLL‡ | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | 388 | -14 | 36 | 1.499 | 1.455 |
| 3 | 1,017 | 1,305 | 1,407 | 288 | 390 | 2.956 | 3.012 |
| 4 | 3,102 | 3,099 | 3,285 | -2 | 183 | 4.263 | 4.221 |
| 5 | 15,263 | 14,216 | 15,000 | -1,046 | -263 | 8.240 | 8.135 |
| Total | 19,735 | 18,959 | 20,080 | -774 | 346 |  |  |

Table 7: Accident insurance: RBNS results of individual claims prediction using Listings [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), the latter adds a linear regression on the latest claim status information Oi,j−1|ν∈{0,1}O\_{i,j-1|\nu}\in\{0,1\}, see ([4.6](#S4.E6 "In 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")); the earmarked columns‡ use the ground truth
in the lower triangle.

We observe a significant improvement of the individual claim RMSEs
(column ‘Ind.RMSE‡’, in blue color) except in accident period i=3i=3. This shows that the latest claim status is important information to forecast further payments on a given claim ν\nu. Interestingly, these results (with identity link) outperform the neural network results (with log-link) of Richman–Wüthrich [[10](#bib.bib10), Table 6]. This shows that the network results in that reference can be improved. Our experiments have shown that the identity link leads to better results than the log-link in this accident insurance data example. The identity link does not guarantee non-negativity of ultimate claims, the log-link does not allow ultimate claims to be exactly equal to zero. Thus, both choices have deficiencies and it remains an open problem to improve on this point.

![Refer to caption](2603.11660v1/x1.png)

Figure 5: Claims reserves per accident year i=1,…,5i=1,\ldots,5 and separated by closed and open claims at the evaluation date II using the linear regression ([4.6](#S4.E6 "In 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")).

Figure [5](#S4.F5 "Figure 5 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") illustrates the results
of Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"). It shows the resulting claims reserves per accident year i=1,…,5i=1,\ldots,5 and split according to the claim status Oi,I−i|ν∈{0,1}O\_{i,I-i|\nu}\in\{0,1\} (closed/open) at the evaluation date II. We observe that the claims reserves of
Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") (in orange color) meet the true OLL (in blue color) very well (this is an out-of-sample consideration, evaluating on the ground truth OLL), whereas the CL RBNS method (in yellow color) cannot distinguish between closed and open claims.
This verifies the improvements reported in Table [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").

We extend the regression model given in ([4.6](#S4.E6 "In 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) to include all available information (covariates) of period j−1j-1. That is, we make a Markov assumption and the latest information is again included in a linear regression model (with identity link)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μj−1​((Ci,l|ν,𝑿i,l|ν)l=0j−1)\displaystyle\mu\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right) | =\displaystyle= | μj−1​(Ci,j−1|ν,𝑿i,j−1|ν)\displaystyle\mu\_{j-1}\left(C\_{i,j-1|\nu},\boldsymbol{X}\_{i,j-1|\nu}\right) |  |
|  |  | =\displaystyle= | ϑ0+ϑ1​Ci,j−1|ν+ϑ2​Ci,j−1|ν​Oi,j−1|ν+∑k≥1ϑk+2​Xi,j−1|ν(k),\displaystyle\vartheta\_{0}+\vartheta\_{1}\,C\_{i,j-1|\nu}+\vartheta\_{2}\,C\_{i,j-1|\nu}\,O\_{i,j-1|\nu}+\sum\_{k\geq 1}\vartheta\_{k+2}\,X^{(k)}\_{i,j-1|\nu}, |  |

the last sum considers the components of 𝑿i,j−1|ν\boldsymbol{X}\_{i,j-1|\nu} as a linear regression,
we use dummy coding for the calendar month of the accident date, and the reporting delay is censored at 365 days; see Table [1](#S2.T1 "Table 1 ‣ 2.4.1 Accident insurance data ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving") for the available covariates.
Moreover, we keep the interaction term between the individual cumulative payments Ci,j−1|νC\_{i,j-1|\nu} and the claim status Oi,j−1|νO\_{i,j-1|\nu}. The results are reported in Table [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), and the fitting results of the linear regression model of the last period j−1=0j-1=0 (i.e., i=5i=5) are shown in Listing [4](#LST4 "Listing 4 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"); we comment on this below.

|  |  | RBNS | RBNS | Error‡ | Error‡ | Ind.RMSE‡ | Ind.RMSE‡ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ii | True OLL‡ | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | All covariates | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | All covariates | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | All covariates |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | 374 | -14 | 22 | 1.499 | 1.455 |
| 3 | 1,017 | 1,305 | 1,411 | 288 | 394 | 2.956 | 3.013 |
| 4 | 3,102 | 3,099 | 3,358 | -2 | 256 | 4.263 | 4.221 |
| 5 | 15,263 | 14,216 | 14,965 | -1,046 | -298 | 8.240 | 8.121 |
| Total | 19,735 | 18,959 | 20,108 | -774 | 374 |  |  |

Table 8: Accident insurance: RBNS results of individual claims prediction using Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and the linear regression ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) on all available covariates of settlement period j−1j-1;
the earmarked columns‡ use the ground truth
in the lower triangle.

Comparing Tables [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), we observe a huge similarity between the results, there is only one improvement in
‘Ind.RMSE‡’ for the most recent accident year i=5i=5 (compare blue colors in both tables). This verifies that the individual cumulative payments and the claim status are the most important covariates in this forecast, and the remaining covariates give some further fine-tuning for the most recent accident year. Listing [4](#LST4 "Listing 4 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") shows the regression output of the last linear regression function μ0\mu\_{0}, i.e., for j=0j=0, which is used to extrapolate the most recent accident year i=5i=5. From a quick inspection we conclude that we may drop the input variable ’work or leisure accident’, and all the other variables should remain in the linear regression model.

Listing 4: GLM output of the linear regression function ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) for μ0\mu\_{0} (i.e., j=0j=0, resp., i=5i=5).

[⬇](data:text/plain;base64,Q2FsbDoKZ2xtKGZvcm11bGEgPSBZWSB+IENDICogU3RhdHVzICsgV29ya0xlaXN1cmUgKyBBY2NNb250aCArIAogICAgUmVwRGVsYXksIGZhbWlseSA9IGdhdXNzaWFuKCksIGRhdGEgPSBsZWFybikKCkNvZWZmaWNpZW50czoKICAgICAgICAgICAgICAgIEVzdGltYXRlIFN0ZC4gRXJyb3IgdCB2YWx1ZSBQcig+IXQhKSAgICAKKEludGVyY2VwdCkgICAtMC4yMTk4MzMxICAwLjE3MDQzMTUgIC0xLjI5MCAgMC4xOTcxMSAgICAKQ0MgICAgICAgICAgICAgMS4wNjcyMjIzICAwLjAxMzE3OTAgIDgwLjk3OSAgPCAyZS0xNiAqKioKU3RhdHVzICAgICAgICAgMC42OTIxMzk1ICAwLjA2OTU2ODQgICA5Ljk0OSAgPCAyZS0xNiAqKioKV29ya0xlaXN1cmUgICAtMC4wMjQyNDM2ICAwLjAyMjMyMzggIC0xLjA4NiAgMC4yNzc0OSAgICAKQWNjTW9udGgyICAgICAgMC4wMTQ2ODQ1ICAwLjExMDg0NTIgICAwLjEzMiAgMC44OTQ2MSAgICAKQWNjTW9udGgzICAgICAgMC4wMzk4MTQzICAwLjExMzY5NzUgICAwLjM1MCAgMC43MjYyMSAgICAKQWNjTW9udGg0ICAgICAgMC4xNjQ5ODc5ICAwLjEyMDUzNzcgICAxLjM2OSAgMC4xNzEwOCAgICAKQWNjTW9udGg1ICAgICAgMC4yMjI0NzAzICAwLjExNjI4NzMgICAxLjkxMyAgMC4wNTU3NCAuICAKQWNjTW9udGg2ICAgICAgMC4wODUwOTY3ICAwLjExNjYyNTAgICAwLjczMCAgMC40NjU2MCAgICAKQWNjTW9udGg3ICAgICAgMC4zNDQ5NjY0ICAwLjExOTYzNDYgICAyLjg4MyAgMC4wMDM5MyAqKiAKQWNjTW9udGg4ICAgICAgMC43MDU3NTQ5ICAwLjExNzk5MTkgICA1Ljk4MSAyLjIzZS0wOSAqKioKQWNjTW9udGg5ICAgICAgMC44NjMxMjc1ICAwLjEyNjI1MjggICA2LjgzNyA4LjIyZS0xMiAqKioKQWNjTW9udGgxMCAgICAgMS4xOTkwODk0ICAwLjEzNDgwNjAgICA4Ljg5NSAgPCAyZS0xNiAqKioKQWNjTW9udGgxMSAgICAgMS44NjA2OTAzICAwLjE0Njk4NTEgIDEyLjY1OSAgPCAyZS0xNiAqKioKQWNjTW9udGgxMiAgICAgMi4wMjQwODU3ICAwLjIwODUxMzIgICA5LjcwNyAgPCAyZS0xNiAqKioKUmVwRGVsYXkgICAgICAgMC4wMDQ1NTE1ICAwLjAwMDcxNDggICA2LjM2NyAxLjk0ZS0xMCAqKioKQ0M6U3RhdHVzICAgICAgMC40MTY1MTYyICAwLjAxNDgwOTMgIDI4LjEyNSAgPCAyZS0xNiAqKioKLS0tClNpZ25pZi4gY29kZXM6ICAwICcqKionIDAuMDAxICcqKicgMC4wMSAnKicgMC4wNSAnLicgMC4xICcgJyAxCgooRGlzcGVyc2lvbiBwYXJhbWV0ZXIgZm9yIGdhdXNzaWFuIGZhbWlseSB0YWtlbiB0byBiZSAzMC45OTMzNCkKCiAgICBOdWxsIGRldmlhbmNlOiAzMTQxNjA3ICBvbiA0NTg5OCAgZGVncmVlcyBvZiBmcmVlZG9tClJlc2lkdWFsIGRldmlhbmNlOiAxNDIyMDM2ICBvbiA0NTg4MiAgZGVncmVlcyBvZiBmcmVlZG9tCkFJQzogMjg3ODgxCgpOdW1iZXIgb2YgRmlzaGVyIFNjb3JpbmcgaXRlcmF0aW9uczogMgo=)

1Call:

2glm(formula = YY ~ CC \* Status + WorkLeisure + AccMonth +

3 RepDelay, family = gaussian(), data = learn)

4

5Coefficients:

6 Estimate Std. Error t value Pr(>!t!)

7(Intercept) -0.2198331 0.1704315 -1.290 0.19711

8CC 1.0672223 0.0131790 80.979 < 2e-16 \*\*\*

9Status 0.6921395 0.0695684 9.949 < 2e-16 \*\*\*

10WorkLeisure -0.0242436 0.0223238 -1.086 0.27749

11AccMonth2 0.0146845 0.1108452 0.132 0.89461

12AccMonth3 0.0398143 0.1136975 0.350 0.72621

13AccMonth4 0.1649879 0.1205377 1.369 0.17108

14AccMonth5 0.2224703 0.1162873 1.913 0.05574 .

15AccMonth6 0.0850967 0.1166250 0.730 0.46560

16AccMonth7 0.3449664 0.1196346 2.883 0.00393 \*\*

17AccMonth8 0.7057549 0.1179919 5.981 2.23e-09 \*\*\*

18AccMonth9 0.8631275 0.1262528 6.837 8.22e-12 \*\*\*

19AccMonth10 1.1990894 0.1348060 8.895 < 2e-16 \*\*\*

20AccMonth11 1.8606903 0.1469851 12.659 < 2e-16 \*\*\*

21AccMonth12 2.0240857 0.2085132 9.707 < 2e-16 \*\*\*

22RepDelay 0.0045515 0.0007148 6.367 1.94e-10 \*\*\*

23CC:Status 0.4165162 0.0148093 28.125 < 2e-16 \*\*\*

24---

25Signif. codes: 0 ’\*\*\*’ 0.001 ’\*\*’ 0.01 ’\*’ 0.05 ’.’ 0.1 ’ ’ 1

26

27(Dispersion parameter for gaussian family taken to be 30.99334)

28

29 Null deviance: 3141607 on 45898 degrees of freedom

30Residual deviance: 1422036 on 45882 degrees of freedom

31AIC: 287881

32

33Number of Fisher Scoring iterations: 2

From Listing [4](#LST4 "Listing 4 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") we observe that
the OLL prediction is increasing in the ’accident month’ variable. This makes sense for the most recent accident year, as accident month ’January’ has a 12-months development by the end of the calendar year, and accident month ’December’ only a 1-month development. So, we expected more open payments for later accidents during the calendar year (because they are less developed caused by the accounting year cut-off). The variable ’reporting delay’ also leads to increasing claims, this may be caused by the fact that longer reporting delays correlate with longer waiting periods, and hence larger claims (because they are more severe).

![Refer to caption](2603.11660v1/x2.png)

![Refer to caption](2603.11660v1/x3.png)

Figure 6: (lhs) Claims reserves per accident year i=1,…,5i=1,\ldots,5 and separated by closed and open claims at the evaluation date II, (rhs) claims reserves split w.r.t. the accident month both graphs using the linear regression ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")), see also Listing [4](#LST4 "Listing 4 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").

Figure [6](#S4.F6 "Figure 6 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") shows the resulting claims reserves of the linear regression model ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")), see also Listing [4](#LST4 "Listing 4 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"). The figure on the left-hand side splits the reserves w.r.t. the accident years and the claim status, and on the right-hand side the reserves are split w.r.t. the accident month. We observe that the estimated reserves (in orange color) are well aligned with the true outcomes (in blue color) saying that we have rather accurate forecasts on the different covariate levels. On the other hand, the RBNS CL reserves (in yellow color) cannot cope with this behavior.

### 4.3 Lab: Linear regression bootstrap results

Since the linear regressions of Tables [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") can be computed very fast, this allows us to run an individual claims history bootstrap to analyze model estimation uncertainty. This section presents the bootstrap results for the linear regression case.

The individual claims reserving results of Tables [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") can be computed very fast – each one involves only 4 linear regressions. This makes it feasible to run an individual claims bootstrap analysis, similar to Section [2.4](#S2.SS4 "2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving").

|  |  | Tables [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | | Bootstrap | |
| --- | --- | --- | --- | --- | --- |
|  | True OLL‡ | RBNS | Error‡ | Mean | Est.Err. |
| Cumulative payments, Listing [2](#LST2 "Listing 2 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | 19,735 | 19,076 | -658 | 19,000 | 942 |
| Cumulative payments and claim status, Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | 19,735 | 20,080 | 346 | 19,998 | 955 |
| Cumulative payments and all covariates, formula ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) | 19,735 | 20,108 | 374 | 20,020 | 963 |

Table 9: Bootstrap results (aggregated all claims of all accident years) of the linear regression models using different sets of covariates according to Tables [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").

Completely analogously to Section [2.4](#S2.SS4 "2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), we perform an individual claims history bootstrap analysis, resampling the upper individual claims triangle by drawing with replacement. The selected individual claims are used to compute the bootstrap estimates μ^j−1∗\widehat{\mu}^{\ast}\_{j-1} of the
three regression functions given in ([3.5](#S3.E5 "In 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")) (only individual cumulative payments; Table [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")),
([4.6](#S4.E6 "In 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) (individual cumulative payments and claim status; Table [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) and
([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) (all covariates; Table [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")). These bootstrapped regression functions are then used to complete the lower triangle on the originally observed claims, i.e., similar to ([2.18](#S2.E18 "In 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving")) we extrapolate the real observed upper triangle with the bootstrapped PtU factors. We perform this over 1,000 bootstrap samples (each having the same sample size as the original upper individual claims triangle). The aggregated results over all claims are presented in Table [9](#S4.T9 "Table 9 ‣ 4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), and they are compared to the non-bootstrapped results of Table [6](#S3.T6 "Table 6 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").
We give the following remarks on Table [9](#S4.T9 "Table 9 ‣ 4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"):

* •

  The original RBNS reserves and the bootstrap means are very close (in all three cases the difference is roughly 80). This indicates consistency in the sense that the bootstrap does not collect a major bias.
* •

  The bootstrap ’Est.Err.’ corresponds to the standard deviation in the bootstrapped ultimate claim predictions (aggregated over all claims). This can be interpreted as the average model estimation error, similar to the estimation error in Mack’s [[8](#bib.bib8)] RMSEP formula, see Section [2.4](#S2.SS4 "2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"). This model uncertainty estimate has a similar magnitude as in Table [3](#S2.T3 "Table 3 ‣ 2.4.3 Mack’s chain-ladder method and individual bootstrapping ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving"), indicating that the impact of IBNR claims is negligible in this example on model estimation error (this will be different in the example in Section [5](#S5 "5 The role of claims incurred ‣ One-Shot Individual Claims Reserving"), below). Second, we observe from Table [9](#S4.T9 "Table 9 ‣ 4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") that this error is slightly increasing with model complexity. Thus, more model complexity seems to increase estimation uncertainty in this example.
* •

  The ’Est.Err.’ only accounts for model error and not for process variance (irreducible risk). Nevertheless, the numbers of ’Est.Err.’ in Table [9](#S4.T9 "Table 9 ‣ 4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") dominate the observed forecast errors ‘Error‡’, which implies that these linear regression models cannot be rejected for individual claims RBNS forecasting.

|  | Linear regression model ([4.6](#S4.E6 "In 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")); Table [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | | | | Linear regression model ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")); Table [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Ind.RMSE‡ | Ind.RMSE‡ |  | Bootstrap | Ind.RMSE‡ | Ind.RMSE‡ |  | Bootstrap |
| ii | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | Difference | Est.Err. | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | All covariates | Difference | Est.Err. |
| 2 | 1.499 | 1.455 | -0.044 | 0.031 | 1.499 | 1.455 | -0.044 | 0.048 |
| 3 | 2.956 | 3.012 | 0.056 | 0.049 | 2.956 | 3.013 | 0.057 | 0.086 |
| 4 | 4.263 | 4.221 | -0.042 | 0.058 | 4.263 | 4.221 | -0.042 | 0.110 |
| 5 | 8.240 | 8.135 | -0.105 | 0.077 | 8.240 | 8.121 | -0.119 | 0.154 |

Table 10: Bootstrap results on individual claims in the two linear regression models
([4.6](#S4.E6 "In 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) (payments and claim status) and ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) (all covariates), see also
Tables [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").

We can also analyze the bootstrap results on an individual claims level.
Table [10](#S4.T10 "Table 10 ‣ 4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") presents the results per accident year.
The individual RMSE ‘Ind.RMSE‡’ decreases in accident year i=5i=5 from the model of Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") of 8.240 to 8.135 for the model of Listing [3](#LST3 "Listing 3 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"). This is a decrease of -0.105, the bootstrap standard deviation for this quantity accounting for model uncertainty is 0.077. Thus, in this example the decrease exceeds the size of the model uncertainty. On the other hand, we observe that the value of 0.077 is more than 100 times smaller than the individual RMSE of
8.135. Not surprisingly, this shows that the driver of individual claims uncertainty is irreducible risk, i.e., we are in a typical situation of a low signal-to-noise ratio, and we do not expect very accurate reserves on individual claims, but only on aggregated claims, e.g., aggregated within the accident periods, see Figure [6](#S4.F6 "Figure 6 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"). This low signal-to-noise situation can only be improved by better covariates, e.g., claims incurred or medical reports may be useful to provide more accurate forecasts on individual claims, for instance, making a statement about the expected recovery time after an accident.

### 4.4 Lab: Accident insurance example – feed-forward neural network

This section replaces the linear regression model of Section [4.2](#S4.SS2 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") by a feed-forward neural network, still making the Markov assumption on the input covariates.

The results of Table [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") are based on linear regressions ([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")). We replace these linear regressions by a feed-forward neural network (FNN) architectures μj−1FNN\mu^{\rm FNN}\_{j-1}, for 1≤j≤J1\leq j\leq J, allowing for more modeling flexibility, capturing non-linear terms and allowing for more complex interactions between the covariate components. The specific selected FNN architecture is documented in Table [11](#S4.T11 "Table 11 ‣ 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and the full code is given in Listing [5](#LST5 "Listing 5 ‣ One-Shot Individual Claims Reserving") in the appendix.

| Module | Dimension | #\# Weights | Activation |
| --- | --- | --- | --- |
| Input layer | 6 | – | – |
| 1st hidden layer | 20 | 140 | GELU |
| 2nd hidden layer | 15 | 315 | GELU |
| Output layer | 1 | 16 | identity |

Table 11: Selected FNN architectures μj−1FNN\mu^{\rm FNN}\_{j-1}, for 1≤j≤J1\leq j\leq J, in the accident insurance example.

The remaining modeling parts are very similar to Section [4.2](#S4.SS2 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), only the linear regression part
([4.2](#S4.Ex4 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) is replaced by the FNNs μj−1FNN\mu^{\rm FNN}\_{j-1}, for 1≤j≤J1\leq j\leq J. We use the same covariates, but the accident month enters as a continuous variable and we manually add the interaction term between the cumulative payments and the claim status. The specifications of the stochastic gradient descent fitting procedure are provided in Table [12](#S4.T12 "Table 12 ‣ 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), see also Listing [5](#LST5 "Listing 5 ‣ One-Shot Individual Claims Reserving") in the appendix.

|  |  |
| --- | --- |
| Component | Setting |
| Loss function | mean squared error (MSE) |
| Optimizer | Adam with learning rate 10−310^{-3} |
| Batch size and epochs | 8,192 and 500 |
| Learning-validation split | 9:19:1 |
| Early stopping | reduce learning rate on plateau, factor 0.9, patience 5 |
| Ensembling | 10 network fits with different seeds |

Table 12: Key implementation and hyper-parameters for FNN fitting.

There is one key feature that is worth mentioning, we refer to line 58 of Listing [5](#LST5 "Listing 5 ‣ One-Shot Individual Claims Reserving"). Namely, the linear regression model using the square loss function provides an estimated solution μ^j−1\widehat{\mu}\_{j-1} that satisfies the balance property, i.e., for the MLE estimated linear regression we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1I−j∑ν:Ti|ν≤j−1μ^j−1​((Ci,l|ν,𝑿i,l|ν)l=0j−1)=∑i=1I−j∑ν:Ti|ν≤j−1C^i,J|ν.\sum\_{i=1}^{I-j}\sum\_{\nu:\,T\_{i|\nu}\leq j-1}\widehat{\mu}\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right)=\sum\_{i=1}^{I-j}\sum\_{\nu:\,T\_{i|\nu}\leq j-1}\widehat{C}\_{i,J|\nu}. |  | (4.8) |

This is a consequence of working with the canonical link under the square loss function (in an exponential dispersion family (EDF) setting), and it says that the average estimated model is equal to the average response ([4.8](#S4.E8 "In 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")); see also Lindholm–Wüthrich [[4](#bib.bib4), Proposition 2.6]. This is an in-sample unbiasedness property, and it implies that there are no (obvious) biases that can propagate through the recursive structure (of course, assumed we have stationarity along the accident period axis). Unfortunately, stochastic gradient descent (SGD) fitted models fail to satisfy this balance property. Therefore, we need to enforce it by a post calibration step

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^j−1FNN​(⋅)⟵∑i=1I−j∑ν:Ti|ν≤j−1C^i,J|ν∑i=1I−j∑ν:Ti|ν≤j−1μ^j−1FNN​((Ci,l|ν,𝑿i,l|ν)l=0j−1)​μ^j−1FNN​(⋅).\widehat{\mu}^{\rm FNN}\_{j-1}(\cdot)\quad\longleftarrow\quad\frac{\sum\_{i=1}^{I-j}\sum\_{\nu:\,T\_{i|\nu}\leq j-1}\widehat{C}\_{i,J|\nu}}{\sum\_{i=1}^{I-j}\sum\_{\nu:\,T\_{i|\nu}\leq j-1}\widehat{\mu}^{\rm FNN}\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right)}~\widehat{\mu}^{\rm FNN}\_{j-1}(\cdot). |  | (4.9) |

That is, we apply a multiplicative scaling step to enforce the balance property
([4.8](#S4.E8 "In 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) by the new (scaled) regression function (one could also shift the intercept correspondingly).
This post calibration step ([4.9](#S4.E9 "In 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving")) helps to control a potential bias, as we now have an in-sample unbiased model, for the code see line 58 of Listing [5](#LST5 "Listing 5 ‣ One-Shot Individual Claims Reserving").

|  |  | RBNS | RBNS | Error‡ | Error‡ | Ind.RMSE‡ | Ind.RMSE‡ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ii | True OLL‡ | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | FNN all cov. | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | FNN all cov. | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | FNN all cov. |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | 512 | -14 | 159 | 1.499 | 1.491 |
| 3 | 1,017 | 1,305 | 1,500 | 288 | 484 | 2.956 | 3.017 |
| 4 | 3,102 | 3,099 | 3,399 | -2 | 297 | 4.263 | 4.218 |
| 5 | 15,263 | 14,216 | 15,395 | -1,046 | 132 | 8.240 | 8.114 |
| Total | 19,735 | 18,959 | 20,806 | -774 | 1,072 |  |  |

Table 13: Accident insurance example following up Table [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"): RBNS results of individual claims prediction using Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and a FNN architecture on all available covariates of settlement period j−1j-1;
the earmarked columns‡ use the ground truth
in the lower triangle.

Table [13](#S4.T13 "Table 13 ‣ 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") presents the results of the FNN architectures and they should be compared to the linear regression results of Table
[8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"). The conclusion is simple, the older accident years i=2,3i=2,3 do not benefit from the additional modeling flexibility, mainly because SGD fitting is not as efficient as Fisher’s scoring method to fit a linear regression/GLM. In fact, the out-of-sample validation control triggering early stopping lets the older accident years be worse than in the simple linear regression model. The more recent accident years i=4,5i=4,5 marginally improve compared to the linear regression model, see Tables [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and [13](#S4.T13 "Table 13 ‣ 4.4 Lab: Accident insurance example – feed-forward neural network ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") (blue colors). Here, we benefit from more flexible functional forms compared to the linear regression. However, the improvement is comparably minor, and in view of the computational efficiency (and the explainability) of the linear regression, we give preference to the linear regression model in this accident insurance example.

Naturally, at this stage we could also exploit other ML methods such as gradient boosting machines (GBMs). For the moment, we refrain from doing so.

### 4.5 Transformer architecture

In the last step of the accident insurance example, we lift the regression model to a transformer architecture being able to process the entire past claims history, i.e., we drop the Markov assumption on the input used in the previous section.

The natural next step is to replace the FNN architecture (used in the previous section) by a transformer architecture that allows one to use the entire past claim history

|  |  |  |
| --- | --- | --- |
|  | (Ci,l|ν,𝑿i,l|ν)l=0j−1↦μj−1transf​((Ci,l|ν,𝑿i,l|ν)l=0j−1).(C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}~\mapsto~\mu^{\rm transf}\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right). |  |

Listing [6](#LST6 "Listing 6 ‣ One-Shot Individual Claims Reserving") in the appendix gives the code that we have used to compute the next example (the listing focuses on the differences to Listing [5](#LST5 "Listing 5 ‣ One-Shot Individual Claims Reserving")); we mention that in this transformer architecture we only select “simple” linear embeddings, but this approach could easily accommodate more complex functional forms.
The transformer architecture can be applied to all periods j−1=1,…,J−1j-1=1,\ldots,J-1. For j−1=0j-1=0, we have only one observed past period, and we therefore use the FNN architecture of the previous section. Since there are only the two stochastic dynamic covariates of cumulative payments and claim status, we restrict our next example to these two stochastic processes

|  |  |  |
| --- | --- | --- |
|  | (Ci,l|ν,Oi,l|ν)l=0j−1↦μj−1transf​((Ci,l|ν,Oi,l|ν)l=0j−1),(C\_{i,l|\nu},O\_{i,l|\nu})\_{l=0}^{j-1}~\mapsto~\mu^{\rm transf}\_{j-1}\left((C\_{i,l|\nu},O\_{i,l|\nu})\_{l=0}^{j-1}\right), |  |

and the results of Table [14](#S4.T14 "Table 14 ‣ 4.5 Transformer architecture ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") should be compared to Table [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").

|  |  | RBNS | RBNS | Error‡ | Error‡ | Ind.RMSE‡ | Ind.RMSE‡ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ii | True OLL‡ | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Transformer | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Transformer | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Transformer |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 353 | 339 | 296 | -14 | -57 | 1.499 | 1.533 |
| 3 | 1,017 | 1,305 | 1,338 | 288 | 322 | 2.956 | 3.004 |
| 4 | 3,102 | 3,099 | 3,260 | -2 | 158 | 4.263 | 4.241 |
| 5 | 15,263 | 14,216 | 14,961 | -1,046 | -301 | 8.240 | 8.129 |
| Total | 19,735 | 18,959 | 19,855 | -774 | 122 |  |  |

Table 14: Accident insurance: RBNS results of individual claims prediction using Listings [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and a transformer architecture considering the cumulative payments and claim status history
(Ci,l|ν,Oi,l|ν)l=0j−1(C\_{i,l|\nu},O\_{i,l|\nu})\_{l=0}^{j-1}; the earmarked columns‡ use the ground truth
in the lower triangle.

Comparing the results of Table [7](#S4.T7 "Table 7 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") and
Table [14](#S4.T14 "Table 14 ‣ 4.5 Transformer architecture ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), we conclude that the additional model complexity is not fully justified in our forecast problem. This is likely because we have a rather small dataset (5×55\times 5 triangle) on a comparable coarse time grid. For instance, for accident year i=2i=2, this implies that the input time-series has a total length of 4, i.e., this is not a typically length a transformer architecture brings major benefits. Thus, we have technically verified that this set-up can be implemented and computed, the proof whether it is beneficial to increase predictive performance on bigger datasets still needs to be done.

## 5 The role of claims incurred

This section presents our second example where in addition to individual cumulative payments and the claim status process also individual claims incurred information is available. We study different models to evaluate the explanatory power of these different inputs.

The results in Section [4.2](#S4.SS2 "4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") have highlighted the importance of the claim status process Oi,0:J|νO\_{i,0:J|\nu} for forecasting ultimate claims. This section analyzes the role of claims incurred Ii,0:J|νI\_{i,0:J|\nu} which are individual case estimates set by claims adjusters. For this we consider our second example introduced in Table [2](#S2.T2 "Table 2 ‣ 2.4.2 Liability insurance data ‣ 2.4 Lab: Chain-ladder reserving and individual bootstrap ‣ 2 Chain-ladder method - revisited ‣ One-Shot Individual Claims Reserving").
We build a linear regression model including individual cumulative payments Ci,j−1|νC\_{i,j-1|\nu}, claims incurred Ii,j−1|νI\_{i,j-1|\nu} and the claim status Oi,j−1|νO\_{i,j-1|\nu} of the latest period j−1j-1

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | μj−1​((Ci,l|ν,𝑿i,l|ν)l=0j−1)\displaystyle\mu\_{j-1}\left((C\_{i,l|\nu},\boldsymbol{X}\_{i,l|\nu})\_{l=0}^{j-1}\right) | =\displaystyle= | ϑ0+ϑ1​Ci,j−1|ν+ϑ2​Ii,j−1|ν+ϑ3​Oi,j−1|ν+\displaystyle\vartheta\_{0}+\vartheta\_{1}\,C\_{i,j-1|\nu}+\vartheta\_{2}\,I\_{i,j-1|\nu}+\vartheta\_{3}\,O\_{i,j-1|\nu}+ |  | (5.1) |
|  |  |  | +ϑ4​Ci,j−1|ν​Oi,j−1|ν+ϑ5​Ii,j−1|ν​Oi,j−1|ν.\displaystyle+~\vartheta\_{4}\,C\_{i,j-1|\nu}\,O\_{i,j-1|\nu}+\vartheta\_{5}\,I\_{i,j-1|\nu}\,O\_{i,j-1|\nu}. |  |

This model considers linear terms in individual cumulative payments, claims incurred and claim status, and we also let the claim status interact with the other two inputs.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Model | Ci,j−1|νC\_{i,j-1|\nu} | Ii,j−1|νI\_{i,j-1|\nu} | Oi,j−1|νO\_{i,j-1|\nu} | Ci,j−1|ν​Oi,j−1|νC\_{i,j-1|\nu}\,O\_{i,j-1|\nu} | Ii,j−1|ν​Oi,j−1|νI\_{i,j-1|\nu}\,O\_{i,j-1|\nu} |
| Model C | x |  |  |  |  |
| Model I |  | x |  |  |  |
| Model CO | x |  | x | x |  |
| Model IO |  | x | x |  | x |
| Model CIO | x | x | x | x | x |

Table 15: Liability insurance: RBNS models considering different versions of ([5.1](#S5.E1 "In 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving")).

We consider five different versions of the linear regression function
([5.1](#S5.E1 "In 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving")) by excluding selected terms. The five considered variants are illustrated in Table [15](#S5.T15 "Table 15 ‣ 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving"), the final Model CIO includes all the terms. Each of these models is fitted and we compute the resulting
individual claims RMSEs ’Ind.RMSE‡’ measuring the individual claim forecast against the ground truth individual OLL, see ([3.4](#S3.E4 "In 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")).

|  | Linear regression ([5.1](#S5.E1 "In 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving")) | | | | | FNN |
| --- | --- | --- | --- | --- | --- | --- |
| ii | Model C | Model I | Model CO | Model IO | Model CIO | Model CIO |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 2.628 | 10.066 | 2.612 | 4.781 | 2.571 | 2.633 |
| 3 | 19.964 | 16.748 | 19.794 | 16.481 | 17.749 | 17.076 |
| 4 | 12.489 | 9.791 | 12.339 | 8.559 | 8.794 | 8.510 |
| 5 | 14.290 | 14.402 | 14.268 | 14.138 | 13.872 | 13.786 |

Table 16: Liability insurance: Individual claims RMSEs ‘Ind.RMSE‡’, see ([3.4](#S3.E4 "In 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving")).

The results are presented in Table [16](#S5.T16 "Table 16 ‣ 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving") and we give the following remarks.

* •

  Model C and Model I: We observe that the claims incurred Ii,j−1|νI\_{i,j-1|\nu} seems to have superior predictive power compared to individual cumulative payments Ci,j−1|νC\_{i,j-1|\nu}, except in accident year i=2i=2. A reason for the different behavior in this old accident year may be that the claims incurred estimates have not been continuously updated by the claims adjusters for claims close to settlement. In that case, the payments made give a more accurate forecast.
* •

  Model CO and Model IO: In combination with the claim status information Oi,j−1|νO\_{i,j-1|\nu}, we give preference to the claims incurred information giving more accurate forecasts than the individual cumulative claim version. Again only for the accident year i=2i=2, Model IO does not outperform Model CO, however, the gap has decreased.
* •

  Model CIO: If we combine the two models to Model CIO, we receive a generally strong model, though not in all accident years the best one on individual claims. This indicates that we should include all information, but it also seems that the linear regression structure can be improved. This is verified by the last column where we replace the linear regression models ([5.1](#S5.E1 "In 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving")) by FNNs μj−1FNN\mu\_{j-1}^{\rm FNN} on the identical input information; for the FNN architecture see also Listing [5](#LST5 "Listing 5 ‣ One-Shot Individual Claims Reserving") in the appendix.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | RBNS | RBNS | Error‡ | Error‡ | Ind.RMSE‡ | Ind.RMSE‡ | Bootstrap |
| ii | True OLL‡ | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Model CIO | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Model CIO | Listing [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | Model CIO | Est.Err. |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |
| 2 | 361 | 635 | 442 | 274 | 81 | 2.717 | 2.571 | 0.061 |
| 3 | 3,233 | 1,497 | 1,398 | -1,736 | -1,835 | 19.988 | 17.749 | 0.119 |
| 4 | 3,287 | 2,488 | 2,938 | -799 | -349 | 12.400 | 8.794 | 0.156 |
| 5 | 4,613 | 3,982 | 4,172 | -631 | -440 | 14.901 | 13.872 | 0.216 |
| Total | 11,494 | 8,601 | 8,950 | -2,893 | -2,543 |  |  |  |
| Bootstrap Est.Err. (aggregated claim) | | | | | 886 |  |  |  |

Table 17: Liability insurance: RBNS results of individual claims prediction using Listings [1](#LST1 "Listing 1 ‣ 3.4 Individual claims reserving - setting the stage ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") and
the linear regression Model CIO considering
(Ci,j−1|ν,Ii,j−1|ν,Oi,j−1|ν)(C\_{i,j-1|\nu},I\_{i,j-1|\nu},O\_{i,j-1|\nu}); the earmarked columns‡ use the ground truth
in the lower triangle.

We come back to the RBNS CL predictions given in Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") for the liability insurance data set, and we complement these results with the individual claims reserving results of Table [16](#S5.T16 "Table 16 ‣ 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving") – we select the linear regression model ([5.1](#S5.E1 "In 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving")) called Model CIO. Moreover, we perform an individual claims history bootstrap analysis as described in Section [4.3](#S4.SS3 "4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") – this can be done because linear regression fitting is very fast. We interpret the results of Table [17](#S5.T17 "Table 17 ‣ 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving"):

* •

  The linear regression Model CIO generally improves the results compared to the RBNS CL of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"), saying that the combination of individual cumulative payments, claims incurred and claim status is beneficial to improve forecast accuracy. This is also verified by the individual claims RMSEs in columns ’Ind.RMSE‡’.
* •

  There is a severe under-estimation in accident year i=3i=3. This under-estimation can be traced back to two individual claims that became very large in development periods j=3,4j=3,4, we have already documented this in [[10](#bib.bib10)]. These two ’outliers’ also explain the large value in the individual claims RMSE ’Ind.RMSE‡’. Thus, the model could not capture these two strongly increasing claims (amounting to payments of 1,874), but apart from that the forecasts look very good. PS: These two large claims should not be called ‘outliers’ because they are not data error, but real claims that need to be paid by the insurer.
* •

  The bootstrap analysis provides an overall model estimation uncertainty of 886, which looks reasonable and adding the irreducible risk (not explicitly assessed here) explains the forecast error ’Error‡’ of -2,543 (this includes the two large claims of accident year i=3i=3).
* •

  The last column of Table [17](#S5.T17 "Table 17 ‣ 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving") gives the bootstrap estimation uncertainty on individual claims. Similar to Table [10](#S4.T10 "Table 10 ‣ 4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), we conclude that the by far most dominant term is irreducible risk (low signal-to-noise ratio), but the gap is a bit smaller in this liability insurance example compared to the accident insurance example in Table [10](#S4.T10 "Table 10 ‣ 4.3 Lab: Linear regression bootstrap results ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving"), which may be explained by the additional claims incurred information.

## 6 IBNR reserving

The last missing piece is to compute the IBNR reserves for the claims not reported yet at the evaluation date II.

The last part of the reserving exercise is to predict the IBNR claims. These are not included in the previously computed RBNS reserves.
There are many different ways to do so, and often a frequency-severity model is proposed, see, e.g., Parodi [[9](#bib.bib9)]. The first modeling part of the frequency-severity model predicts the number of IBNR claims, which can be seen as a reporting delay censoring problem. Popular methods for predicting these counts either use aggregate CL type methods or they use methods from survival analysis. This will result in a reporting pattern of the total number of claims NiN\_{i} occurred in period ii, which allows one to predict the number of late reportings. This analysis can also involve an exposure measure, such as premium earned, and additional risk factor information. For the severities, one then studies a cross-classified model having the accident date on one axis and the reporting delay on the other axis. Using the RBNS predictions C^i,J|νRBNS\widehat{C}^{\rm RBNS}\_{i,J|\nu} together with their claim’s reporting delays Ti|νT\_{i|\nu} allows one to predict the sizes of the late reported claims in such a cross-classified model. One can further refine this by contract and claim feature information which results in a proposal similar to the one in the addendum to Semenovich [[12](#bib.bib12)].

We take a simpler approach which is still very accurate for our data. We directly estimate the IBNR amounts with a cross-classified CL model without going through the frequency-severity split. Obviously, this uses less granular data. Consider all RBNS claim predictions C^i,J|νRBNS\widehat{C}^{\rm RBNS}\_{i,J|\nu} of the claims ν\nu being reported by the evaluation date II, i.e., with i+Ti|ν≤Ii+T\_{i|\nu}\leq I. This concerns the claims reported in the upper triangle with ultimate claim forecasts obtained, e.g., by Algorithm [3](#algorithm3 "Algorithm 3 ‣ 4.1 Recursive individual RBNS claims reserving ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving").
Based on this, we build a new upper triangle given by defining the entries

|  |  |  |  |
| --- | --- | --- | --- |
|  | Si,j=∑ν=1NiC^i,J|νRBNS​ 1{Ti|ν=j}=∑ν:Ti|ν=jC^i,J|νRBNS for i+j≤I.S\_{i,j}=\sum\_{\nu=1}^{N\_{i}}\widehat{C}^{\rm RBNS}\_{i,J|\nu}\,\mathds{1}\_{\{T\_{i|\nu}=j\}}\,=\sum\_{\nu:\,T\_{i|\nu}=j}\widehat{C}^{\rm RBNS}\_{i,J|\nu}\qquad\text{ for $i+j\leq I$.} |  | (6.1) |

This is the total predicted claim amount of accident period ii that has been reported with a reporting lag of jj. If we wanted to build a frequency-severity model, we would divide this by the observed number of reported claims with that reporting lag, i.e.,

|  |  |  |
| --- | --- | --- |
|  | Ni,j=∑ν=1Ni𝟙{Ti|ν=j}=∑ν:Ti|ν=j1.N\_{i,j}=\sum\_{\nu=1}^{N\_{i}}\mathds{1}\_{\{T\_{i|\nu}=j\}}\,=\sum\_{\nu:\,T\_{i|\nu}=j}1. |  |

However, for the results below we directly use the data (upper triangle)

|  |  |  |
| --- | --- | --- |
|  | 𝒮I={Si,j;i+j≤I, 1≤i≤I, 0≤j≤J},{\cal S}\_{I}=\left\{S\_{i,j};~i+j\leq I,\,1\leq i\leq I,\,0\leq j\leq J\right\}, |  |

and the lower (IBNR) triangle at time II is forecasted with a simple CL prediction.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | True OLL‡ | Reserves | CL RMSEP | Error‡ | % CL RMSEP‡ |
| Accident dataset |  |  |  |  |  |
| Mack’s CL model [[8](#bib.bib8)] | 24,212 | 23,064 | 1,663 | -1,148 | 69% |
| RBNS CL prediction of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | 19,735 | 18,959 | – | -774 | – |
| IBNR CL prediction of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | 4,478 | 4,105 | – | -374 | – |
| Total (of next two lines) | 24,212 | 24,430 | – | 217 | 13% |
| Individual RBNS of Table [8](#S4.T8 "Table 8 ‣ 4.2 Lab: Accident insurance example – linear regression ‣ 4 Individual ultimate prediction - one-shot micro reserving ‣ One-Shot Individual Claims Reserving") | 19,735 | 20,108 | – | 374 | – |
| IBNR reserving using ([6.1](#S6.E1 "In 6 IBNR reserving ‣ One-Shot Individual Claims Reserving")) | 4,478 | 4,322 | – | -156 | – |
| Liability dataset |  |  |  |  |  |
| Mack’s CL model [[8](#bib.bib8)] | 15,730 | 11,526 | 1,977 | -4,204 | 213% |
| RBNS CL prediction of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | 11,494 | 8,601 | – | -2,893 | – |
| IBNR CL prediction of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving") | 4,236 | 2,925 | – | -1,311 | – |
| Total (of next two lines) | 15,730 | 12,486 | – | -3,244 | 164% |
| Individual RBNS of Table [17](#S5.T17 "Table 17 ‣ 5 The role of claims incurred ‣ One-Shot Individual Claims Reserving") | 11,494 | 8,950 | – | -2,543 | – |
| IBNR reserving using ([6.1](#S6.E1 "In 6 IBNR reserving ‣ One-Shot Individual Claims Reserving")) | 4,236 | 3,536 | – | -700 | – |

Table 18: Mack’s CL results on cumulative payments split to RBNS and IBNR reserves; the earmarked columns‡ can only be computed because we know the lower triangle in our examples.

The results are presented in Table [18](#S6.T18 "Table 18 ‣ 6 IBNR reserving ‣ One-Shot Individual Claims Reserving"), and they are compared to the CL analysis of Table [4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"). From Table [18](#S6.T18 "Table 18 ‣ 6 IBNR reserving ‣ One-Shot Individual Claims Reserving") we observe that in our examples we get IBNR reserves that are very accurate, i.e., more accurate than the ones of Table
[4](#S3.T4 "Table 4 ‣ 3.3 Lab: Chain-ladder RBNS and IBNR reserving ‣ 3 Chain-ladder RBNS reserving ‣ One-Shot Individual Claims Reserving"). In the accident insurance example we lower the prediction error from -374 to -156, and in the liability insurance example from -1,311 to -700. Thus, this simple method performs very well on these two (small-scale) datasets. This also impacts the total RBNS + IBNR reserves, being more accurate than in Mack’s CL model. This completes our numerical examples.

## 7 Summary

Building on our previous paper [[10](#bib.bib10)], we introduced several refinements to the one-shot estimation and prediction procedure based on individual claims histories. An exciting observation in our examples was that linear regressions perform quite well in this one-shot forecasting problem. Since linear regressions can be fitted very fast, this moreover allows one to perform an individual claims history bootstrap to assess model estimation uncertainty.

Our examples are small-scale examples in the sense that they use 5×55\times 5 years observations, and it remains an open question to verify that our proposal also works on bigger data. Another open point is to take care of non-stationarity, e.g., caused by inflation. In our examples, a simple balance property step was sufficient. However, in other situations manual interventions may be necessary to cope with non-stationarity.

* •

  In a next step, bigger data should be studied, and also the impact of longer time-series inputs for forecasting ultimate claims needs to be understood, e.g., using transformer architectures.
* •

  In our examples, an additive regression structure seems to be better than a multiplicative one. The deeper reason for this preference is not entirely clear. Also the role of the claims that are precisely zero needs to be explored, because neither in the additive nor in the multiplicative setting, these can easily be modeled/fitted.
* •

  The one-shot ultimate claim prediction can be complemented by a cash flow pattern for the RBNS reserves, e.g., using a transformer decoder architecture.
* •

  We used one of the most simple approaches to predict IBNR claims. Certainly there are many different ways to enhance this procedure and estimate.

## References

* [1]

  Bornhuetter, R.L., Ferguson, R.E. (1972). The actuary and IBNR.
  Proceedings CAS 59, 181-195.
* [2]

  Hachemeister, C.A., Stanard, J.N. (1975).
  IBNR claims count estimation with static lag functions.
  ASTIN Colloquium 1975, Portimão, Portugal.
* [3]

  Kremer, E. (1985).
  Einführung in die Versicherungsmathematik.
  Vandenhoek & Ruprecht, Göttingen.
* [4]

  Lindholm, M., Wüthrich, M.V. (2025).
  The balance property in insurance pricing.
  Scandinavian Actuarial Journal, in press.
* [5]

  Lorenz, H., Schmidt, K.D. (1999).
  Grossing-up, chain-ladder and marginal-sum estimation.
  Blätter DGVFM 24, 195-200.
* [6]

  Lorenz, H., Schmidt, K.D. (2016).
  Grossing up method.
  In: Handbook on Loss Reserving,
  Radtke, M., Schmidt, K.D., Schnaus, A. (eds.), Springer, 127-131.
* [7]

  Mack, T. (1991).
  A simple parametric model for rating automobile insurance or estimating IBNR claims reserves.
  ASTIN Bulletin - The Journal of the IAA 21/1, 93-109.
* [8]

  Mack, T. (1993). Distribution-free calculation of the standard error of chain ladder reserve estimates.
  ASTIN Bulletin - The Journal of the IAA 23/2, 213-225.
* [9]

  Parodi, P. (2013).
  Triangle-free reserving: a non-traditional framework for estimating reserves and reserve uncertainty.
  British Actuarial Journal 19/1, 168-218.
* [10]

  Richman, R., Wüthrich, M.V. (2026).
  From chain-ladder to individual claims reserving.
  arXiv:2602.15385.
* [11]

  Schnieper, R. (1991).
  Separating true IBNR from IBNER claims.
  ASTIN Bulletin - The Journal of the IAA 21/1, 111-127.
* [12]

  Semenovich, D. (2014).
  A unified approach to reserving and pricing.
  Actuaries Institute, General Insurance Seminar 2014. Private communication.
* [13]

  Shmueli, G. (2010).
  To explain or to predict?
  Statistical Science 25/3, 289-310.
* [14]

  Wüthrich, M.V. (2018).
  Neural networks applied to chain-ladder reserving. European Actuarial Journal 8/2, 407-436.

Listing 5: Recursive one-shot PtU RBNS algorithm: FNN regression.

[⬇](data:text/plain;base64,IyMjIHByZS1wcm9jZXNzaW5nIGNvdmFyaWF0ZXMKbTEgPC0gbWVhbihhcy5tYXRyaXgodHJpQ0NbLHBhc3RlMCgiWCIsIDA6SjApXSksIG5hLnJtPVRSVUUpCnMxIDwtIHNkKGFzLm1hdHJpeCh0cmlDQ1sscGFzdGUwKCJYIiwgMDpKMCldKSwgbmEucm09VFJVRSkKdHJpQ0NbLHBhc3RlMCgiWCIsIDA6SjApXSA8LSAodHJpQ0NbLHBhc3RlMCgiWCIsIDA6SjApXS1tMSkvczEKY2xhaW1zJEFjY01vbnRoICAgICAgICAgICA8LSAoY2xhaW1zJEFjY01vbnRoLTEpLzExCmNsYWltcyRXb3JrTGVpc3VyZSAgICAgICAgPC0gYXMuaW50ZWdlcihjbGFpbXMkV29ya0xlaXN1cmUpLTEKY2xhaW1zJFJlcERlbGF5ICAgICAgICAgICA8LSBwbWluKDM2NSwgY2xhaW1zJFJlcERlbGF5RGF5cykvMzY1CgojIyMgbmV0d29yayBhcmNoaXRlY3R1cmUKRk5OIDwtIGZ1bmN0aW9uKHNlZWQsIHEwKXsKICAgIHRmJGtlcmFzJGJhY2tlbmQkY2xlYXJfc2Vzc2lvbigpOyBzZXQuc2VlZChzZWVkKTsgc2V0X3JhbmRvbV9zZWVkKHNlZWQpCiAgICBEZXNpZ24gICA8LSBsYXllcl9pbnB1dChzaGFwZT1jKHEwWzFdKSwgZHR5cGU9J2Zsb2F0MzInKQogICAgTmV0d29yayA9IERlc2lnbiAlPiUgbGF5ZXJfZGVuc2UodW5pdHM9cTBbMl0sIGFjdGl2YXRpb249J2dlbHUnKSAlPiUKICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyX2RlbnNlKHVuaXRzPXEwWzNdLCBhY3RpdmF0aW9uPSdnZWx1JykgJT4lCiAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcl9kZW5zZSh1bml0cz0xLCBhY3RpdmF0aW9uPSdsaW5lYXInKQogICAga2VyYXNfbW9kZWwoaW5wdXRzPWMoRGVzaWduKSwgb3V0cHV0cz1jKE5ldHdvcmspKQogICAgfQoKIyMjIGluaXRpYWxpemUgdWx0aW1hdGUgY2xhaW1zIHdpdGggb2JzZXJ2ZWQgb25lcwpjbGFpbXMkWVkgPC0gTkEKY2xhaW1zW3doaWNoKGNsYWltcyRBY2NEYXRlPD1JMC1KMCksXSRZWSA8LSBjbGFpbXNbd2hpY2goY2xhaW1zJEFjY0RhdGU8PUkwLUowKSxdJFVsdGltYXRlCgojIyMgcmVjdXJzaXZlIG5ldHdvcmsgZml0dGluZyBhbmQgUHRVIGZvcmVjYXN0aW5nCmZvciAoaiBpbiByZXYoMDooSjAtMSkpKXsKICAgIGkgPC0gSTAtai0xCiAgICAjIyMgcHJlcGFyZSBsZWFybmluZyBhbmQgZm9yZWNhc3QgZGF0YSBmb3IgRk5OCiAgICBzZWxlY3QgIDwtIHdoaWNoKChjbGFpbXMkQWNjRGF0ZTw9aSkmKGNsYWltcyRSZXBEZWxheVlZPD1qKSkKICAgIFlsZWFybjAgPC0gYXMubWF0cml4KGNsYWltc1tzZWxlY3QsXSRZWSkKICAgIG11LmhvbSAgPC0gbWVhbihZbGVhcm4wKQogICAgbXUuc2QgICA8LSBzZChZbGVhcm4wKQogICAgWWxlYXJuICA8LSAoWWxlYXJuMC1tdS5ob20pL211LnNkCiAgICBYbGVhcm4gIDwtIGFzLm1hdHJpeChjYmluZCh0cmlPT1tzZWxlY3QscGFzdGUwKCJYIixqKV0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cmlDQ1tzZWxlY3QscGFzdGUwKCJYIixqKV0qdHJpT09bc2VsZWN0LHBhc3RlMCgiWCIsaildLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2xhaW1zW3NlbGVjdCwiV29ya0xlaXN1cmUiXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNsYWltc1tzZWxlY3QsIlJlcERlbGF5Il0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjbGFpbXNbc2VsZWN0LCJBY2NNb250aCJdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJpQ0Nbc2VsZWN0LHBhc3RlMCgiWCIsaildKSkKICAgIHNlbGVjdCAgPC0gd2hpY2goY2xhaW1zJEFjY0RhdGU9PShpKzEpKQogICAgWHRlc3QgICA8LSBhcy5tYXRyaXgoY2JpbmQodHJpT09bc2VsZWN0LHBhc3RlMCgiWCIsaildLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJpQ0Nbc2VsZWN0LHBhc3RlMCgiWCIsaildKnRyaU9PW3NlbGVjdCxwYXN0ZTAoIlgiLGopXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNsYWltc1tzZWxlY3QsIldvcmtMZWlzdXJlIl0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjbGFpbXNbc2VsZWN0LCJSZXBEZWxheSJdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2xhaW1zW3NlbGVjdCwiQWNjTW9udGhYWCJdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJpQ0Nbc2VsZWN0LHBhc3RlMCgiWCIsaildKSkKICAgICMjIyBuZXR3b3JrIGZpdHRpbmcKICAgIG1vZGVsIDwtIEZOTihzZWVkLCBjKG5jb2woWGxlYXJuKSwgYygyMCwxNSkpKQogICAgYWRhbSA9IG9wdGltaXplcl9hZGFtKGxlYXJuaW5nX3JhdGU9MC4wMDEpCiAgICBtb2RlbCAlPiUgY29tcGlsZShvcHRpbWl6ZXI9YWRhbSwgbG9zcz0ibXNlIikKICAgIHBhdGgxIDwtIHBhc3RlMCgiLi9OZXR3b3Jrcy9GTk5fIixzZWVkLCJfaiIsaiwiLndlaWdodHMuaDUiKQogICAgbW9kZWxfd3JpdGUgPSBjYWxsYmFja19tb2RlbF9jaGVja3BvaW50KHBhdGgxLCBzYXZlX2Jlc3Rfb25seT1ULCBzYXZlX3dlaWdodHNfb25seT1UKQogICAgbGVhcm5fcmF0ZSA9IGNhbGxiYWNrX3JlZHVjZV9scl9vbl9wbGF0ZWF1KGZhY3Rvcj0wLjksIHBhdGllbmNlPTUsIGNvb2xkb3duPTApCiAgICBmaXQgPC0gbW9kZWwgJT4lIGZpdChsaXN0KFhsZWFybiksIFlsZWFybiwgdmFsaWRhdGlvbl9zcGxpdD0wLjEsIGJhdGNoX3NpemU9ODE5MiwgCiAgICAgICAgICAgICAgICAgICAgICAgICBlcG9jaHM9NTAwLCBjYWxsYmFja3M9bGlzdChtb2RlbF93cml0ZSwgbGVhcm5fcmF0ZSksIHNodWZmbGU9VFJVRSkKICAgICMjIyByZXN1bHRzCiAgICBtb2RlbCRsb2FkX3dlaWdodHMocGF0aDEpCiAgICBsZWFybi5OTiA8LSBtdS5ob20gKyBtdS5zZCAqIG1vZGVsICU+JSBwcmVkaWN0KGxpc3QoWGxlYXJuKSwgYmF0Y2hfc2l6ZT0xMF42LCB2ZXJib3NlPTApCiAgICB0ZXN0Lk5OIDwtICBtdS5ob20gKyBtdS5zZCAqIG1vZGVsICU+JSBwcmVkaWN0KGxpc3QoWHRlc3QpLCBiYXRjaF9zaXplPTEwXjYsIHZlcmJvc2U9MCkKICAgIGNsYWltc1t3aGljaChjbGFpbXMkQWNjRGF0ZT09KGkrMSkpLF0kWVkgPC0gc3VtKFlsZWFybjApL3N1bShsZWFybi5OTikgKiB0ZXN0Lk5OCiB9Cg==)

1### pre-processing covariates

2m1 <- mean(as.matrix(triCC[,paste0("X", 0:J0)]), na.rm=TRUE)

3s1 <- sd(as.matrix(triCC[,paste0("X", 0:J0)]), na.rm=TRUE)

4triCC[,paste0("X", 0:J0)] <- (triCC[,paste0("X", 0:J0)]-m1)/s1

5claims$AccMonth <- (claims$AccMonth-1)/11

6claims$WorkLeisure <- as.integer(claims$WorkLeisure)-1

7claims$RepDelay <- pmin(365, claims$RepDelayDays)/365

8

9### network architecture

10FNN <- function(seed, q0){

11 tf$keras$backend$clear\_session(); set.seed(seed); set\_random\_seed(seed)

12 Design <- layer\_input(shape=c(q0[1]), dtype=’float32’)

13 Network = Design %>% layer\_dense(units=q0[2], activation=’gelu’) %>%

14 layer\_dense(units=q0[3], activation=’gelu’) %>%

15 layer\_dense(units=1, activation=’linear’)

16 keras\_model(inputs=c(Design), outputs=c(Network))

17 }

18

19### initialize ultimate claims with observed ones

20claims$YY <- NA

21claims[which(claims$AccDate<=I0-J0),]$YY <- claims[which(claims$AccDate<=I0-J0),]$Ultimate

22

23### recursive network fitting and PtU forecasting

24for (j in rev(0:(J0-1))){

25 i <- I0-j-1

26 ### prepare learning and forecast data for FNN

27 select <- which((claims$AccDate<=i)&(claims$RepDelayYY<=j))

28 Ylearn0 <- as.matrix(claims[select,]$YY)

29 mu.hom <- mean(Ylearn0)

30 mu.sd <- sd(Ylearn0)

31 Ylearn <- (Ylearn0-mu.hom)/mu.sd

32 Xlearn <- as.matrix(cbind(triOO[select,paste0("X",j)],

33 triCC[select,paste0("X",j)]\*triOO[select,paste0("X",j)],

34 claims[select,"WorkLeisure"],

35 claims[select,"RepDelay"],

36 claims[select,"AccMonth"],

37 triCC[select,paste0("X",j)]))

38 select <- which(claims$AccDate==(i+1))

39 Xtest <- as.matrix(cbind(triOO[select,paste0("X",j)],

40 triCC[select,paste0("X",j)]\*triOO[select,paste0("X",j)],

41 claims[select,"WorkLeisure"],

42 claims[select,"RepDelay"],

43 claims[select,"AccMonthXX"],

44 triCC[select,paste0("X",j)]))

45 ### network fitting

46 model <- FNN(seed, c(ncol(Xlearn), c(20,15)))

47 adam = optimizer\_adam(learning\_rate=0.001)

48 model %>% compile(optimizer=adam, loss="mse")

49 path1 <- paste0("./Networks/FNN\_",seed,"\_j",j,".weights.h5")

50 model\_write = callback\_model\_checkpoint(path1, save\_best\_only=T, save\_weights\_only=T)

51 learn\_rate = callback\_reduce\_lr\_on\_plateau(factor=0.9, patience=5, cooldown=0)

52 fit <- model %>% fit(list(Xlearn), Ylearn, validation\_split=0.1, batch\_size=8192,

53 epochs=500, callbacks=list(model\_write, learn\_rate), shuffle=TRUE)

54 ### results

55 model$load\_weights(path1)

56 learn.NN <- mu.hom + mu.sd \* model %>% predict(list(Xlearn), batch\_size=10^6, verbose=0)

57 test.NN <- mu.hom + mu.sd \* model %>% predict(list(Xtest), batch\_size=10^6, verbose=0)

58 claims[which(claims$AccDate==(i+1)),]$YY <- sum(Ylearn0)/sum(learn.NN) \* test.NN

59 }




Listing 6: Recursive one-shot PtU RBNS algorithm: Transformer regression.

[⬇](data:text/plain;base64,IyMjIG5ldHdvcmsgYXJjaGl0ZWN0dXJlClRyYW5zZm9ybWVyIDwtIGZ1bmN0aW9uKHNlZWQsIGlucHV0X3NpemUsIHVuaXRzMCl7CiAgdGYka2VyYXMkYmFja2VuZCRjbGVhcl9zZXNzaW9uKCk7IHNldC5zZWVkKHNlZWQpOyBzZXRfcmFuZG9tX3NlZWQoc2VlZCkKICBEZXNpZ24gPC0gbGF5ZXJfaW5wdXQoc2hhcGU9YyhpbnB1dF9zaXplWzFdLCBpbnB1dF9zaXplWzJdKSwgZHR5cGU9J2Zsb2F0MzInKQogICMKICBSZXByICAgPC0gRGVzaWduICU+JSB0aW1lX2Rpc3RyaWJ1dGVkKGxheWVyX2RlbnNlKHVuaXRzPXVuaXRzMFsxXSkpCiAgcXVlcnkgIDwtIFJlcHIgJT4lIHRpbWVfZGlzdHJpYnV0ZWQobGF5ZXJfZGVuc2UodW5pdHM9dW5pdHMwWzFdKSkKICBrZXkgICAgPC0gUmVwciAlPiUgdGltZV9kaXN0cmlidXRlZChsYXllcl9kZW5zZSh1bml0cz11bml0czBbMV0pKQogIHZhbHVlICA8LSBSZXByICU+JSB0aW1lX2Rpc3RyaWJ1dGVkKGxheWVyX2RlbnNlKHVuaXRzPXVuaXRzMFsxXSkpCiAgIwogIGF0dGVudGlvbl9vdXRwdXQgPC0gbGlzdChxdWVyeSwgdmFsdWUsIGtleSkgJT4lIGxheWVyX2F0dGVudGlvbih1c2Vfc2NhbGU9VFJVRSwgdHJhaW5hYmw9VFJVRSkKICAjCiAgc2tpcF8xIDwtIGxheWVyX2FkZChsaXN0KGF0dGVudGlvbl9vdXRwdXQsIFJlcHIpKQogIHNraXBfMiA8LSBza2lwXzEgJT4lIGxheWVyX2xheWVyX25vcm1hbGl6YXRpb24oKSAlPiUgCiAgICAgICAgICAgICAgICAgICAgICAgdGltZV9kaXN0cmlidXRlZChsYXllcl9kZW5zZSh1bml0cz11bml0czBbMV0pKQogICMKICBGZWF0dXJlcyA8LSBsYXllcl9hZGQobGlzdChza2lwXzIsIHNraXBfMSkpICU+JSBsYXllcl9mbGF0dGVuKCkKICAjCiAgTmV0d29yayA9IEZlYXR1cmVzICU+JSBsYXllcl9kZW5zZSh1bml0cz11bml0czBbMl0sIGFjdGl2YXRpb249J2dlbHUnKSAlPiUKICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyX2RlbnNlKHVuaXRzPXVuaXRzMFszXSwgYWN0aXZhdGlvbj0nZ2VsdScpICU+JQogICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJfZGVuc2UodW5pdHM9MSwgYWN0aXZhdGlvbj0nbGluZWFyJykKICAjCiAga2VyYXNfbW9kZWwoaW5wdXRzID0gYyhEZXNpZ24pLCBvdXRwdXRzID0gYyhOZXR3b3JrKSkKfQoKIyMjIHJlY3Vyc2l2ZSBuZXR3b3JrIGZpdHRpbmcgYW5kIFB0VSBmb3JlY2FzdGluZwouCi4KLgogICAgIyMjIGxlYXJuaW5nIGRhdGEKICAgIHNlbGVjdCAgPC0gd2hpY2goKGNsYWltcyRBY2NEYXRlPD1pKSYoY2xhaW1zJFJlcERlbGF5WVk8PWopKQogICAgWGxlYXJuMCA8LSBhcnJheShOQSwgZGltPWMobGVuZ3RoKHNlbGVjdCksIGorMSwgMykpCiAgICBYbGVhcm4wWywsMV0gPC0gYXMubWF0cml4KHRyaU9PLlhYW3NlbGVjdCxwYXN0ZTAoIlgiLDA6aildKQogICAgWGxlYXJuMFssLDJdIDwtIGFzLm1hdHJpeCh0cmlDQy5YWFtzZWxlY3QscGFzdGUwKCJYIiwwOmopXSp0cmlPTy5YWFtzZWxlY3QscGFzdGUwKCJYIiwwOmopXSkKICAgIFhsZWFybjBbLCwzXSA8LSBhcy5tYXRyaXgodHJpQ0MuWFhbc2VsZWN0LHBhc3RlMCgiWCIsMDpqKV0pCiAgICAjIyMgZm9yZWNhc3QgZGF0YQogICAgc2VsZWN0IDwtIHdoaWNoKGNsYWltcyRBY2NEYXRlPT0oaSsxKSkKICAgIFh0ZXN0IDwtIGFycmF5KE5BLCBkaW09YyhsZW5ndGgoc2VsZWN0KSwgaisxLCAzKSkKICAgIFh0ZXN0WywsMV0gPC0gYXMubWF0cml4KHRyaU9PLlhYW3NlbGVjdCxwYXN0ZTAoIlgiLDA6aildKQogICAgWHRlc3RbLCwyXSA8LSBhcy5tYXRyaXgodHJpQ0MuWFhbc2VsZWN0LHBhc3RlMCgiWCIsMDpqKV0qdHJpT08uWFhbc2VsZWN0LHBhc3RlMCgiWCIsMDpqKV0pCiAgICBYdGVzdFssLDNdIDwtIGFzLm1hdHJpeCh0cmlDQy5YWFtzZWxlY3QscGFzdGUwKCJYIiwwOmopXSkKIC4KIC4KIC4KICAgIGlucHV0X3NpemUgPC0gZGltKFhsZWFybjApWzI6M10KICAgIHVuaXRzMCA8LSBjKDEwLCAxNSwgMTApCiAgICBtb2RlbCA8LSBUcmFuc2Zvcm1lcihzZWVkLCBpbnB1dF9zaXplLCB1bml0czApCiAgIAogCg==)

1### network architecture

2Transformer <- function(seed, input\_size, units0){

3 tf$keras$backend$clear\_session(); set.seed(seed); set\_random\_seed(seed)

4 Design <- layer\_input(shape=c(input\_size[1], input\_size[2]), dtype=’float32’)

5 #

6 Repr <- Design %>% time\_distributed(layer\_dense(units=units0[1]))

7 query <- Repr %>% time\_distributed(layer\_dense(units=units0[1]))

8 key <- Repr %>% time\_distributed(layer\_dense(units=units0[1]))

9 value <- Repr %>% time\_distributed(layer\_dense(units=units0[1]))

10 #

11 attention\_output <- list(query, value, key) %>% layer\_attention(use\_scale=TRUE, trainabl=TRUE)

12 #

13 skip\_1 <- layer\_add(list(attention\_output, Repr))

14 skip\_2 <- skip\_1 %>% layer\_layer\_normalization() %>%

15 time\_distributed(layer\_dense(units=units0[1]))

16 #

17 Features <- layer\_add(list(skip\_2, skip\_1)) %>% layer\_flatten()

18 #

19 Network = Features %>% layer\_dense(units=units0[2], activation=’gelu’) %>%

20 layer\_dense(units=units0[3], activation=’gelu’) %>%

21 layer\_dense(units=1, activation=’linear’)

22 #

23 keras\_model(inputs = c(Design), outputs = c(Network))

24}

25

26### recursive network fitting and PtU forecasting

27.

28.

29.

30 ### learning data

31 select <- which((claims$AccDate<=i)&(claims$RepDelayYY<=j))

32 Xlearn0 <- array(NA, dim=c(length(select), j+1, 3))

33 Xlearn0[,,1] <- as.matrix(triOO.XX[select,paste0("X",0:j)])

34 Xlearn0[,,2] <- as.matrix(triCC.XX[select,paste0("X",0:j)]\*triOO.XX[select,paste0("X",0:j)])

35 Xlearn0[,,3] <- as.matrix(triCC.XX[select,paste0("X",0:j)])

36 ### forecast data

37 select <- which(claims$AccDate==(i+1))

38 Xtest <- array(NA, dim=c(length(select), j+1, 3))

39 Xtest[,,1] <- as.matrix(triOO.XX[select,paste0("X",0:j)])

40 Xtest[,,2] <- as.matrix(triCC.XX[select,paste0("X",0:j)]\*triOO.XX[select,paste0("X",0:j)])

41 Xtest[,,3] <- as.matrix(triCC.XX[select,paste0("X",0:j)])

42 .

43 .

44 .

45 input\_size <- dim(Xlearn0)[2:3]

46 units0 <- c(10, 15, 10)

47 model <- Transformer(seed, input\_size, units0)

BETA