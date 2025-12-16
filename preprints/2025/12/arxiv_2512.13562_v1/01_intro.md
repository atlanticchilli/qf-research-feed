---
authors:
- Christian Furrer
- Philipp C. Hornung
doc_id: arxiv:2512.13562v1
family_id: arxiv:2512.13562
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Disability insurance with collective health claims: a mean-field approach'
url_abs: http://arxiv.org/abs/2512.13562v1
url_html: https://arxiv.org/html/2512.13562v1
venue: arXiv q-fin
version: 1
year: 2025
---


Christian Furrer
Department of Mathematical Sciences, University of Copenhagen, Universitetsparken 5, DK-2100 Copenhagen, Denmark
[[furrer@math.ku.dk](mailto:furrer@math.ku.dk)](mailto:)
 and 
Philipp C. Hornung
Department of Mathematical Sciences, University of Copenhagen, Universitetsparken 5, DK-2100 Copenhagen, Denmark
[[pcho@math.ku.dk](mailto:pcho@math.ku.dk)](mailto:)

###### Abstract.

The classic semi-Markov disability model is expanded with individual and collective health claims to improve its explanatory and predictive power – in particular in the context of group experience rating. The inclusion of collective health claims leads to a computationally challenging many-body problem. By adopting a mean-field approach, this many-body problem can be approximated by a non-linear one-body problem, which in turn leads to a transparent pricing method for disability coverages based on a lower-dimensional system of non-linear forward integro-differential equations. In a practice-oriented simulation study, the mean-field approximation clearly stands its ground in comparison to naïve Monte Carlo methods.

Keywords: Group experience rating; non-linear forward equations; semi-Markov model.

## 1. Introduction

Disability insurance plays a vital role in ensuring income stability and supporting part-time employment during periods with reduced earning capacity. In many countries, disability coverages are sold not only directly to individuals, but also as part of a company pension scheme. It is therefore essential for insurers to be able to accurately price such coverages – taking into account the fact that the physical and psychological work environment of each company likely has a substantial effect on the frequency, but also the severity, of disability claims. This suggests the application of group experience rating to disability insurance, which has been explored via an empirical Bayes approach for Markov chains in [Furrer2019, FurrerSoerensenYslas2025]. However, since the frequency of disability claims is rather low and single claims with long durations tend to have a substantial impact on the total loss, such a direct approach to experience rating is greatly challenged. Simply put: It can be near impossible to distinguish between ‘good’ and ‘bad’ companies, since there is just too limited data available.

In this paper, we address the ‘small data’ issue by drawing on three observations. First, disability insurance and health insurance are increasingly, at least in certain countries such as Denmark, sold together. Second, it is reasonable to expect – at least when adjusting for covariates – that there is a relationship between an employees disability frequency and the extent of health claims across all employees; this observation is indirectly based on the assumption that both factors are largely attributable to the physical and psychological working environment. For example, a toxic work culture would lead to increased mental health risk, which would show itself in the form of health claims (consulting a psychologist, etc.) and, later, in actual disability (loss of working capacity due to severe stress). Third and finally, the scope of health insurance data is much more extensive, as this type of insurance is often used on a regular basis. Based on these observations, we formulate a multi-state model for disability insurance with integrated information about health claims.

To be specific, we expand the classic semi-Markov disability model (see [Hoem1972, Helwich2008, Christiansen2012, BuchardtMollerSchmidt2015]) with collective health claims and, for technical reasons, with individual health claims. In the classic model, transition probabilities, expected cash flows, and prospective reserves may efficiently be calculated using Kolmogorov’s integro-differential equations. However, if we denote the number of individuals by nn, the inclusion of collective health claims entails that the computational complexity of the relevant forward equations grows exponentially in nn. Consequently, we adopt the mean-field approach outlined in [Hornung2025] to obtain, as an approximation in the limit n→∞n\to\infty, a lower-dimensional system of non-linear forward integro-differential equations. Furthermore, we briefly address statistical aspects as well as practical implementation.

In general, the insurance liabilities of an individual may depend on the other individuals either through the payments or, as is the case here, because the individuals themselves are dependent. In the area of actuarial multi-state modeling, mean-field approximations have hitherto received the most interest in the former case, see in particular [DjehicheLoefdahl2016]. In light hereof, we believe this paper offers a fresh perspective on the application of mean-field theory to the actuarial field.

The remainder of the paper is organized as follows. In Section [2](https://arxiv.org/html/2512.13562v1#S2 "2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"), we expand the classic semi-Markov disability model with individual and collective health claims. Section [3](https://arxiv.org/html/2512.13562v1#S3 "3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") contains a description of the corresponding mean-field model, including the associated system of non-linear forward integro-differential equations, and proofs of the required convergences. The next two sections are more oriented towards practice. In Section [4](https://arxiv.org/html/2512.13562v1#S4 "4. Practical implementation ‣ Disability insurance with collective health claims: a mean-field approach"), we introduce and briefly discuss a meta-algorithm for solving the relevant system of differential equations, while Section [5](https://arxiv.org/html/2512.13562v1#S5 "5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach") is devoted to a simulation study and the comparison of the mean-field approximation to naïve Monte Carlo methods. The paper concludes with Section [6](https://arxiv.org/html/2512.13562v1#S6 "6. Outlook ‣ Disability insurance with collective health claims: a mean-field approach") in which we offer some extensions and avenues for future work.

## 2. Disability model with health claims

This section is devoted to the expansion of the classic semi-Markov disability model with initially individual health claims and subsequently also collective health claims.

### 2.1. Semi-Markov model

Let (Ω,ℱ,F,P)(\Omega,\mathcal{F},\amsmathbb{F},\amsmathbb{P}) be a filtered probability space satisfying the usual conditions and write F=(ℱt)t≥0\amsmathbb{F}=(\mathcal{F}\_{t})\_{t\geq 0}. The multi-state approach to classic disability insurance considers a non-explosive jump process ZZ on the finite state space 𝒥={1,2,3}\mathcal{J}=\{1,2,3\} according to Figure [1](https://arxiv.org/html/2512.13562v1#S2.F1 "Figure 1 ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"). The initial distribution of ZZ is denoted π\pi. We associate to ZZ a multivariate counting process NN with components Nj​kN\_{jk}, j≠kj\neq k, given by

|  |  |  |
| --- | --- | --- |
|  | Nj​k​(t)=#​{s∈(0,t]:Zs−=j,Zs=k}.\displaystyle N\_{jk}(t)=\#\{s\in(0,t]:Z\_{s-}=j,Z\_{s}=k\}. |  |

In this paper, we consider contractual payments prescribed by a payment process BB given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | B​(d​t)=∑j𝟙{Zt−=j}​bj​(t,Ut−)​d​t+∑j≠kbj​k​(t,Ut−)​Nj​k​(d​t),\displaystyle B(\mathrm{d}t)=\sum\_{j}\mathds{1}\_{\{Z\_{t-}=j\}}b\_{j}(t,U\_{t-})\mathrm{d}t+\sum\_{j\neq k}b\_{jk}(t,U\_{t-})N\_{jk}(\mathrm{d}t), |  |

where UU is the duration process associated with ZZ given by

|  |  |  |
| --- | --- | --- |
|  | Ut=t−sup{s∈[0,t]:Zs≠Zt}​ for ​t>0​ and ​U0=0,\displaystyle U\_{t}=t-\sup\{s\in[0,t]:Z\_{s}\neq Z\_{t}\}\text{ for }t>0\text{ and }U\_{0}=0, |  |

while (t,u)↦bj​(t,u)(t,u)\mapsto b\_{j}(t,u) and (t,u)↦bj​k​(t,u)(t,u)\mapsto b\_{jk}(t,u) are measurable functions that are bounded on compacts and which describe sojourn payment rates and transition payments, respectively.

Active
11


Disabled
22


Dead
33

Figure 1. State space 𝒥={1,2,3}\mathcal{J}=\{1,2,3\} for classic disability insurance. The arrows represent the possible transitions.

Semi-Markov modeling entails the assumption that (Z,U)(Z,U) is Markov, and smooth semi-Markov modeling adds the assumption that the jump times should be absolutely continuous (with respect to the Lebesgue measure). An alternative, but equivalent, formulation is in terms of the compensators of the multivariate counting process, which then should read

|  |  |  |
| --- | --- | --- |
|  | E​[Nj​k​(d​t)|ℱt−]=𝟙{Zt−=j}​μj​k​(t,Ut−)​d​t.\displaystyle\amsmathbb{E}[N\_{jk}(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}]=\mathds{1}\_{\{Z\_{t-}=j\}}\mu\_{jk}(t,U\_{t-})\mathrm{d}t. |  |

The functions (t,u)↦μj​k​(t,u)(t,u)\mapsto\mu\_{jk}(t,u), j≠kj\neq k, are the so-called (duration-dependent) transition rates, which we assume to be measurable and bounded on compacts.

In case of a finite maximal contract time T∈(0,∞)T\in(0,\infty), the state-wise prospective reserves at contract inception, (Vi)i(V\_{i})\_{i}, are defined according to

|  |  |  |
| --- | --- | --- |
|  | Vi=E​[∫0Te−∫0tr​(s)​ds​B​(d​t)|Z0=i],\displaystyle V\_{i}=\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B(\mathrm{d}t)\,\bigg|\,Z\_{0}=i\bigg], |  |

where the deterministic interest rate t↦r​(t)t\mapsto r(t) is a measurable function that is bounded on compacts. If we denote by (Ai)i(A\_{i})\_{i} the state-wise expected accumulated cash flows given by

|  |  |  |
| --- | --- | --- |
|  | Ai​(d​t)=E​[B​(d​t)|Z0=i],\displaystyle A\_{i}(\mathrm{d}t)=\amsmathbb{E}[B(\mathrm{d}t)\,|\,Z\_{0}=i], |  |

then it holds that

|  |  |  |
| --- | --- | --- |
|  | Vi=∫0Te−∫0tr​(s)​ds​Ai​(d​t).\displaystyle V\_{i}=\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}A\_{i}(\mathrm{d}t). |  |

In similar fashion, the portfolio-wide prospective reserve at contract inception VV reads

|  |  |  |
| --- | --- | --- |
|  | V=E​[∫0Te−∫0tr​(s)​ds​B​(d​t)]=∫0Te−∫0tr​(s)​ds​A​(d​t),\displaystyle V=\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B(\mathrm{d}t)\bigg]=\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}A(\mathrm{d}t), |  |

where the portfolio-wide expected accumulated cash flow AA is given by

|  |  |  |
| --- | --- | --- |
|  | A​(d​t)=E​[B​(d​t)].\displaystyle A(\mathrm{d}t)=\amsmathbb{E}[B(\mathrm{d}t)]. |  |

In the following, let

|  |  |  |
| --- | --- | --- |
|  | pi​j​(t,u):=P​(Zt=j,Ut≤u|Z0=i)​ and ​pj​(t,u):=P​(Zt=j,Ut≤u).\displaystyle p\_{ij}(t,u):=\amsmathbb{P}(Z\_{t}=j,U\_{t}\leq u\,|\,Z\_{0}=i)\text{ and }p\_{j}(t,u):=\amsmathbb{P}(Z\_{t}=j,U\_{t}\leq u). |  |

be the transition probabilities and occupation probabilities, respectively. Note that

|  |  |  |
| --- | --- | --- |
|  | pj=∑iπ​(i)​pi​j,A=∑iπ​(i)​Ai,V=∑iπ​(i)​Vi.\displaystyle p\_{j}=\sum\_{i}\pi(i)p\_{ij},\quad A=\sum\_{i}\pi(i)A\_{i},\quad V=\sum\_{i}\pi(i)V\_{i}. |  |

###### Example 2.1.

Consider again a disability annuity with a waiting period of ε≥0\varepsilon\geq 0, corresponding to b2​(t,u)=b​𝟙{u≥ε}b\_{2}(t,u)=b\mathds{1}\_{\{u\geq\varepsilon\}} with b>0b>0, while all other payments are zero.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai​(d​t)\displaystyle A\_{i}(\mathrm{d}t) | =∫0tb​𝟙{u≥ε}​pi​2​(t,d​u)​dt=b​𝟙{t≥ε}​(pi​2​(t,t)−pi​2​(t,ε))​d​t,\displaystyle=\int\_{0}^{t}b\mathds{1}\_{\{u\geq\varepsilon\}}p\_{i2}(t,\mathrm{d}u)\,\mathrm{d}t=b\mathds{1}\_{\{t\geq\varepsilon\}}\big(p\_{i2}(t,t)-p\_{i2}(t,\varepsilon)\big)\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(d​t)\displaystyle A(\mathrm{d}t) | =∫0tb​𝟙{u≥ε}​p2​(t,d​u)​dt=b​𝟙{t≥ε}​(p2​(t,t)−p2​(t,ε))​d​t.\displaystyle=\int\_{0}^{t}b\mathds{1}\_{\{u\geq\varepsilon\}}p\_{2}(t,\mathrm{d}u)\,\mathrm{d}t=b\mathds{1}\_{\{t\geq\varepsilon\}}\big(p\_{2}(t,t)-p\_{2}(t,\varepsilon)\big)\mathrm{d}t. |  |

Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi\displaystyle V\_{i} | =b​∫εTe−∫0tr​(s)​ds​(pi​2​(t,t)−pi​2​(t,ε))​dt,\displaystyle=b\int\_{\varepsilon}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\big(p\_{i2}(t,t)-p\_{i2}(t,\varepsilon)\big)\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V\displaystyle V | =b​∫εTe−∫0tr​(s)​ds​(p2​(t,t)−p2​(t,ε))​dt.\displaystyle=b\int\_{\varepsilon}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\big(p\_{2}(t,t)-p\_{2}(t,\varepsilon)\big)\mathrm{d}t. |  |

The following results are standard – see for instance [BuchardtMollerSchmidt2015].

###### Proposition 2.2.

It holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai​(d​t)\displaystyle A\_{i}(\mathrm{d}t) | =∑j∫0t(bj​(t,u)+∑k:k≠jbj​k​(t,u)​μj​k​(t,u))​pi​j​(t,d​u)​dt,\displaystyle=\sum\_{j}\int\_{0}^{t}\Big(b\_{j}(t,u)+\sum\_{k:k\neq j}b\_{jk}(t,u)\mu\_{jk}(t,u)\Big)p\_{ij}(t,\mathrm{d}u)\,\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(d​t)\displaystyle A(\mathrm{d}t) | =∑j∫0t(bj​(t,u)+∑k:k≠jbj​k​(t,u)​μj​k​(t,u))​pj​(t,d​u)​dt.\displaystyle=\sum\_{j}\int\_{0}^{t}\Big(b\_{j}(t,u)+\sum\_{k:k\neq j}b\_{jk}(t,u)\mu\_{jk}(t,u)\Big)p\_{j}(t,\mathrm{d}u)\,\mathrm{d}t. |  |

###### Proposition 2.3.

Let d≥0d\geq 0. It holds almost everywhere on [d,∞)[d,\infty) that

|  |  |  |
| --- | --- | --- |
|  | dd​t​pi​j​(t,t−d)=∑k:k≠j∫0tμk​j​(t,u)​pi​k​(t,d​u)−∫0t−dμj∙​(t,u)​pi​j​(t,d​u)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}p\_{ij}(t,t-d)=\sum\_{k:k\neq j}\int\_{0}^{t}\mu\_{kj}(t,u)p\_{ik}(t,\mathrm{d}u)-\int\_{0}^{t-d}\mu\_{j\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptscriptstyle\bullet$}}}}}}(t,u)p\_{ij}(t,\mathrm{d}u) |  |

with boundary conditions pi​j​(t,0)=𝟙{t=0}​𝟙{i=j}p\_{ij}(t,0)=\mathds{1}\_{\{t=0\}}\mathds{1}\_{\{i=j\}}. It further holds almost everywhere on [d,∞)[d,\infty) that

|  |  |  |
| --- | --- | --- |
|  | dd​t​pj​(t,t−d)=∑k:k≠j∫0tμk​j​(t,u)​pk​(t,d​u)−∫0t−dμj∙​(t,u)​pj​(t,d​u)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}p\_{j}(t,t-d)=\sum\_{k:k\neq j}\int\_{0}^{t}\mu\_{kj}(t,u)p\_{k}(t,\mathrm{d}u)-\int\_{0}^{t-d}\mu\_{j\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptscriptstyle\bullet$}}}}}}(t,u)p\_{j}(t,\mathrm{d}u) |  |

with boundary conditions pj​(t,0)=𝟙{t=0}​π​(j)p\_{j}(t,0)=\mathds{1}\_{\{t=0\}}\pi(j).

###### Remark 2.4.

In light of the reparameterization of Remark [2.6](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") below, Proposition [2.3](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") states that the transition probabilities solve a version of Kolmogorov’s forward equations. In fact, they uniquely solve these equations, confer with [FeinbergMandavaShiryaev2014, FeinbergMandavaShiryaev2022].

###### Remark 2.5.

Note that the occupation probabilities may be calculated directly or by first calculating the transition probabilities and then taking a weighted average with respect to the initial distribution; the latter would of course be more time-consuming. In particular, the occupation probability pjp\_{j} corresponds to the transition probability pi​jp\_{ij} if π​(i)=1\pi(i)=1. This is due to the fact that they have the same evolution forward through time and this evolution does not depend on the initial distribution. We emphasize this at the present time because precisely this property is lost as we turn to mean-field approximations in Section [3](https://arxiv.org/html/2512.13562v1#S3 "3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach").

The terms of the integro-differential equations for the transition probabilities admit an intuitive interpretation. The first term is the aggregate probability mass stemming from paths starting in ii at time zero, transitioning into state kk at some time t−u∈[0,t)t-u\in[0,t), and staying in state kk until transitioning into state jj at exactly time tt (inflow). Similarly, the second term subtracts the probability mass stemming from paths starting in state ii at time zero, transitioning into jj no earlier than time dd (as the duration at time tt should be smaller than t−dt-d), and staying there until transitioning out of state jj at exactly time tt (outflow).

The systems of integro-differential equations of Proposition [2.3](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") can be solved using, for instance, the algorithm presented in Section 3 of [BuchardtMollerSchmidt2015]. Numerical schemes and practical implementation is discussed in greater detail in the latter Section [4](https://arxiv.org/html/2512.13562v1#S4 "4. Practical implementation ‣ Disability insurance with collective health claims: a mean-field approach").

###### Remark 2.6.

The semi-Markov model can be reparameterized, using the process YY given by Yt=t−UtY\_{t}=t-U\_{t}, t≥0t\geq 0, instead of UU. Since UU is the duration since the last jump, YY is the time of the last jump. Therefore, while (Z,U)(Z,U) is a piecewise deterministic process, (Z,Y)(Z,Y) is actually a jump process. This proves mathematically convenient.

In fact, the model (Z,U)(Z,U) with transition rates μj​k\mu\_{jk}, j≠kj\neq k, and transition probabilities pi​jp\_{ij} is equivalent to the model (Z,Y)(Z,Y) with transition rates (t,y)↦μ~j​k​(t,y):=μj​k​(t,t−y)(t,y)\mapsto\widetilde{\mu}\_{jk}(t,y):=\mu\_{jk}(t,t-y), j≠kj\neq k, and transition probabilities p~i​j\tilde{p}\_{ij} given by

|  |  |  |
| --- | --- | --- |
|  | p~i​j(t,d)=P(Zt=j,Yt≥d|Z0=i,Y0=0),0≤d≤t.\displaystyle\widetilde{p}\_{ij}(t,d)=\amsmathbb{P}(Z\_{t}=j,Y\_{t}\geq d\,|\,Z\_{0}=i,Y\_{0}=0),\quad 0\leq d\leq t. |  |

To see this, we may use the definition of YY to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | p~i​j​(t,d)\displaystyle\widetilde{p}\_{ij}(t,d) | =P(Zt=j,Yt≥d|Z0=i,Y0=0)\displaystyle=\amsmathbb{P}(Z\_{t}=j,Y\_{t}\geq d\,|\,Z\_{0}=i,Y\_{0}=0) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =P(Zt=j,Ut≤t−d|Z0=i,U0=0)\displaystyle=\amsmathbb{P}(Z\_{t}=j,U\_{t}\leq t-d\,|\,Z\_{0}=i,U\_{0}=0) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =pi​j​(t,t−d)\displaystyle=p\_{ij}(t,t-d) |  |

for 0≤d≤t0\leq d\leq t. Applying a change of variables, we arrive at a version of Kolmogorov’s forward equations for (Z,Y)(Z,Y):

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​p~i​j​(t,d)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\widetilde{p}\_{ij}(t,d) | =∑k:k≠j∫0tμ~k​j​(t,y)​p~i​k​(t,d​y)−∫dtμ~j∙​(t,y)​p~i​j​(t,d​y),0≤d≤t,\displaystyle=\sum\_{k:k\neq j}\int\_{0}^{t}\widetilde{\mu}\_{kj}(t,y)\widetilde{p}\_{ik}(t,\mathrm{d}y)-\int\_{d}^{t}\widetilde{\mu}\_{j\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptscriptstyle\bullet$}}}}}}(t,y)\widetilde{p}\_{ij}(t,\mathrm{d}y),\quad 0\leq d\leq t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p~i​j​(0,0)\displaystyle\widetilde{p}\_{ij}(0,0) | =𝟙{i=j}.\displaystyle=\mathds{1}\_{\{i=j\}}. |  |

### 2.2. Extension: Individual health claims

It is reasonable to assume that the past number of health insurance claims of an individual is informative about the likelihood of a disability claim. Frequent use of the health insurance policy might predate a disability claim and, similarly, limited or no use might indicate good overall health. While disability claims are rare, health claims are frequent; this makes it particularly attractive to utilize the latter in risk profiling the individual. Therefore, we add to the model a counting process HH describing the number of health insurance claims of the individual. Foremost for notational convenience, we make the simplifying assumption that HH and NN admit no simultaneous jumps. Further, we assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[Nj​k​(d​t)|ℱt−]\displaystyle\amsmathbb{E}[N\_{jk}(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}] | =𝟙{Zt−=j}​μj​k​(t,Ut−,Ht−)​d​t,\displaystyle=\mathds{1}\_{\{Z\_{t-}=j\}}\mu\_{jk}(t,U\_{t-},H\_{t-})\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[H​(d​t)|ℱt−]\displaystyle\amsmathbb{E}[H(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}] | =λZt−​(t,Ut−,Ht−)​d​t.\displaystyle=\lambda\_{Z\_{t-}}(t,U\_{t-},H\_{t-})\mathrm{d}t. |  |

The functions (t,u,h)↦μj​k​(t,u,h)(t,u,h)\mapsto\mu\_{jk}(t,u,h), j≠kj\neq k, are duration- and health-dependent transition rates, which we assume to be measurable and bounded on compacts. The functions (t,u,h)↦λj​(t,u,h)(t,u,h)\mapsto\lambda\_{j}(t,u,h) are health claim hazards of similar nature, which we also assume to be measurable and bounded on compacts. It follows that (Z,U,H)(Z,U,H) is a Markov process.

###### Example 2.7.

In modeling the health claims, a simple choice would be

|  |  |  |
| --- | --- | --- |
|  | E​[H​(d​t)|ℱt−]=λZt−​d​t,\displaystyle\amsmathbb{E}[H(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}]=\lambda\_{Z\_{t-}}\,\mathrm{d}t, |  |

for non-negative constants λj\lambda\_{j}. In this case, HH is a doubly stochastic Poisson process with hazards depending only on the state (active, disabled, and dead) of the individual.

In the following, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​j​(t,u,h):=\displaystyle p\_{ij}(t,u,h):= | P​(Zt=j,Ut≤u,Ht=h|Z0=i),\displaystyle\,\amsmathbb{P}(Z\_{t}=j,U\_{t}\leq u,H\_{t}=h\,|\,Z\_{0}=i), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pj​(t,u,h):=\displaystyle p\_{j}(t,u,h):= | P​(Zt=j,Ut≤u,Ht=h)\displaystyle\,\amsmathbb{P}(Z\_{t}=j,U\_{t}\leq u,H\_{t}=h) |  |

be the transition probabilities and occupation probabilities, respectively. Note that pj=∑iπ​(i)​pi​jp\_{j}=\sum\_{i}\pi(i)p\_{ij}.

###### Example 2.8.

Consider again a disability annuity with a waiting period of ε≥0\varepsilon\geq 0, corresponding to b2​(t,u)=b​𝟙{u≥ε}b\_{2}(t,u)=b\mathds{1}\_{\{u\geq\varepsilon\}} with b>0b>0, while all other payments are zero. In that case, we now have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai​(d​t)\displaystyle A\_{i}(\mathrm{d}t) | =∑h=0∞∫0tb​𝟙{u≥ε}​pi​2​(t,d​u,h)​dt=b​𝟙{t≥ε}​∑h=0∞(pi​2​(t,t,h)−pi​2​(t,ε,h))​d​t,\displaystyle=\sum\_{h=0}^{\infty}\int\_{0}^{t}b\mathds{1}\_{\{u\geq\varepsilon\}}p\_{i2}(t,\mathrm{d}u,h)\,\mathrm{d}t=b\mathds{1}\_{\{t\geq\varepsilon\}}\sum\_{h=0}^{\infty}\big(p\_{i2}(t,t,h)-p\_{i2}(t,\varepsilon,h)\big)\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(d​t)\displaystyle A(\mathrm{d}t) | =∑h=0∞∫0tb​𝟙{u≥ε}​p2​(t,d​u,h)​dt=b​𝟙{t≥ε}​∑h=0∞(p2​(t,t,h)−p2​(t,ε,h))​d​t.\displaystyle=\sum\_{h=0}^{\infty}\int\_{0}^{t}b\mathds{1}\_{\{u\geq\varepsilon\}}p\_{2}(t,\mathrm{d}u,h)\,\mathrm{d}t=b\mathds{1}\_{\{t\geq\varepsilon\}}\sum\_{h=0}^{\infty}\big(p\_{2}(t,t,h)-p\_{2}(t,\varepsilon,h)\big)\mathrm{d}t. |  |

Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi\displaystyle V\_{i} | =b​∫εTe−∫0tr​(s)​ds​∑h=0∞(pi​2​(t,t,h)−pi​2​(t,ε,h))​d​t,\displaystyle=b\int\_{\varepsilon}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\sum\_{h=0}^{\infty}\big(p\_{i2}(t,t,h)-p\_{i2}(t,\varepsilon,h)\big)\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V\displaystyle V | =b​∫εTe−∫0tr​(s)​ds​∑h=0∞(p2​(t,t,h)−p2​(t,ε,h))​d​t.\displaystyle=b\int\_{\varepsilon}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\sum\_{h=0}^{\infty}\big(p\_{2}(t,t,h)-p\_{2}(t,\varepsilon,h)\big)\mathrm{d}t. |  |

Since the payments themselves do not depend on HH, this variable is simply summated out.

The following two propositions expand Propositions [2.2](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") and [2.3](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") to also include individual health claims.

###### Proposition 2.9.

It holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai​(d​t)\displaystyle A\_{i}(\mathrm{d}t) | =∑j∑h=0∞∫0t(bj​(t,u)+∑k:k≠jbj​k​(t,u)​μj​k​(t,u,h))​pi​j​(t,d​u,h)​dt,\displaystyle=\sum\_{j}\sum\_{h=0}^{\infty}\int\_{0}^{t}\Big(b\_{j}(t,u)+\sum\_{k:k\neq j}b\_{jk}(t,u)\mu\_{jk}(t,u,h)\Big)p\_{ij}(t,\mathrm{d}u,h)\,\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(d​t)\displaystyle A(\mathrm{d}t) | =∑j∑h=0∞∫0t(bj​(t,u)+∑k:k≠jbj​k​(t,u)​μj​k​(t,u,h))​pj​(t,d​u,h)​dt.\displaystyle=\sum\_{j}\sum\_{h=0}^{\infty}\int\_{0}^{t}\Big(b\_{j}(t,u)+\sum\_{k:k\neq j}b\_{jk}(t,u)\mu\_{jk}(t,u,h)\Big)p\_{j}(t,\mathrm{d}u,h)\,\mathrm{d}t. |  |

###### Proof.

Referring to the martingale property of differences between the counting processes and their (absolutely continuous) compensators, we find that

|  |  |  |
| --- | --- | --- |
|  | Ai​(d​t)=E​[bZt​(t,Ut)+∑k:k≠ZtbZt​k​(t,Ut)​μZt​k​(t,Ut,Ht)|Z0=i]​d​t.\displaystyle A\_{i}(\mathrm{d}t)=\amsmathbb{E}\Big[b\_{Z\_{t}}(t,U\_{t})+\sum\_{k:k\neq Z\_{t}}b\_{Z\_{t}k}(t,U\_{t})\mu\_{Z\_{t}k}(t,U\_{t},H\_{t})\,\Big|\,Z\_{0}=i\Big]\mathrm{d}t. |  |

Invoking the relevant push-forward measure, the first statement of the proposition is immediate. The second statement is proveable in an identical fashion.
∎

In the following, we adopt the convention that (t,u)↦λj​(t,u,−1)(t,u)\mapsto\lambda\_{j}(t,u,-1) is constantly zero.

###### Proposition 2.10.

Let d≥0d\geq 0. It holds almost everywhere on [d,∞)[d,\infty) that

|  |  |  |
| --- | --- | --- |
|  | dd​t​pi​j​(t,t−d,h)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}p\_{ij}(t,t-d,h) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑k:k≠j∫0tμk​j​(t,u,h)​pi​k​(t,d​u,h)−∫0t−dμj∙​(t,u,h)​pi​j​(t,d​u,h)\displaystyle=\sum\_{k:k\neq j}\int\_{0}^{t}\mu\_{kj}(t,u,h)p\_{ik}(t,\mathrm{d}u,h)-\int\_{0}^{t-d}\mu\_{j\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptscriptstyle\bullet$}}}}}}(t,u,h)p\_{ij}(t,\mathrm{d}u,h) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫0t−dλj​(t,u,h−1)​pi​j​(t,d​u,h−1)−∫0t−dλj​(t,u,h)​pi​j​(t,d​u,h)\displaystyle\quad+\int\_{0}^{t-d}\lambda\_{j}(t,u,h-1)p\_{ij}(t,\mathrm{d}u,h-1)-\int\_{0}^{t-d}\lambda\_{j}(t,u,h)p\_{ij}(t,\mathrm{d}u,h) |  |

with boundary conditions pi​j​(t,0,h)=𝟙{t=0}​𝟙{h=0}​𝟙{i=j}p\_{ij}(t,0,h)=\mathds{1}\_{\{t=0\}}\mathds{1}\_{\{h=0\}}\mathds{1}\_{\{i=j\}}. It further holds almost everywhere on [d,∞)[d,\infty) that

|  |  |  |
| --- | --- | --- |
|  | dd​t​pj​(t,t−d,h)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}p\_{j}(t,t-d,h) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑k:k≠j∫0tμk​j​(t,u,h)​pk​(t,d​u,h)−∫0t−dμj∙​(t,u,h)​pj​(t,d​u,h)\displaystyle=\sum\_{k:k\neq j}\int\_{0}^{t}\mu\_{kj}(t,u,h)p\_{k}(t,\mathrm{d}u,h)-\int\_{0}^{t-d}\mu\_{j\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptscriptstyle\bullet$}}}}}}(t,u,h)p\_{j}(t,\mathrm{d}u,h) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫0t−dλj​(t,u,h−1)​pj​(t,d​u,h−1)−∫0t−dλj​(t,u,h)​pj​(t,d​u,h)\displaystyle\quad+\int\_{0}^{t-d}\lambda\_{j}(t,u,h-1)p\_{j}(t,\mathrm{d}u,h-1)-\int\_{0}^{t-d}\lambda\_{j}(t,u,h)p\_{j}(t,\mathrm{d}u,h) |  |

with boundary conditions pj​(t,0,h)=𝟙{t=0}​𝟙{h=0}​π​(j)p\_{j}(t,0,h)=\mathds{1}\_{\{t=0\}}\mathds{1}\_{\{h=0\}}\pi(j).

###### Proof.

The second statement of the proposition follows, for instance, from the first statement and the identity pj=∑iπ​(i)​pi​jp\_{j}=\sum\_{i}\pi(i)p\_{ij}. To prove the first statement, we consider the trivariate process (Z,Y,H)(Z,Y,H) with YY defined according to Yt=t−UtY\_{t}=t-U\_{t}, t≥0t\geq 0; this is a a Markov jump process. By definition, the compensators of the counting processes associated with (Z,Y,H)(Z,Y,H) are predictable w.r.t. the information generated by themselves, and thus by Theorem 4.8.1 of [Jacobsen2006], the distribution of (Z,Y,H)(Z,Y,H) is fully characterized by these compensators. Consequently, we may invoke (7.17) on p. 151 in [Jacobsen2006] to obtain a system of integro-differential equations which, after a change of variable similar to Remark [2.6](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"), yields the desired result.
∎

###### Remark 2.11.

In light of the reparameterization utilized in the proof, Proposition [2.10](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2.2. Extension: Individual health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") states that the transition probabilities solve a version of Kolmogorov’s forward equations. In fact, they uniquely solve these equations, confer with [FeinbergMandavaShiryaev2014, FeinbergMandavaShiryaev2022].

###### Remark 2.12.

Note that the occupation probabilities may be calculated directly or by first calculating the transition probabilities and then taking a weighted average with respect to the initial distribution. In particular, the occupation probability pjp\_{j} corresponds to the transition probability pi​jp\_{ij} if π​(i)=1\pi(i)=1. This is due to the fact that they have the same evolution forward through time and this evolution does not depend on the initial distribution. We emphasize this once again because precisely this property is lost as we turn to mean-field approximations in Section [3](https://arxiv.org/html/2512.13562v1#S3 "3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach").

The addition of individual health claims has not hurt the intuitive interpretation of the terms of the integro-differential equations. The first line is concerned with jumps of ZZ, while the second line is concerned with jumps of HH; this split is possible since simultaneous jumps were disallowed – otherwise, two additional terms would be necessary. The two terms of the first line are similar to before, but with an added requirement of HH having reached state hh strictly before time tt. The two terms of the second line are new. The first term adds the aggregate probability mass stemming from paths for which the hh’th health claim occurs at time tt (inflow), while the second term subtracts the aggregate probability mass stemming from path for which the (h+1)(h+1)’th health claim occurs at time tt (outflow).

The systems of integro-differential equations of Proposition [2.3](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") can, for instance, be solved by adapting the algorithm presented in Section 3 of  [BuchardtMollerSchmidt2015]. Compared to the situation without individual health claims, the procedure would have to be used for every triplet (i,j,h)(i,j,h) rather than only every pair (i,j)(i,j). In practice, one must choose a cut-off KHK\_{H}, calculate the transition probabilities for h=0,…,KHh=0,\ldots,K\_{H}, and perhaps extrapolate for h>KHh>K\_{H}. Numerical schemes and practical implementation is discussed in greater detail in the latter Section [4](https://arxiv.org/html/2512.13562v1#S4 "4. Practical implementation ‣ Disability insurance with collective health claims: a mean-field approach").

### 2.3. Extension: Collective health claims

So far, we have only considered a single individual – implicitly assuming individuals to be independent. However, one could easily imagine this to not be the case. There is of course the obvious example of events and trends that impact society as a whole, such as pandemics and climate change, but also technological and medical advancements. However, as explained in the introduction, we rather have the example of company level insurance plans and collective health claims in mind. Dependence between individuals here stems from the fact that each employee is affected by the same physical and psychological work environment. If the insurance plan contains both disability and health coverage, aggregate information about health claims, which are much more extensive than disability claims, could serve as a reasonable predictor of, for example, the disability rate.

To formalize a model able to capture the stylized facts, we consider n∈Nn\in\amsmathbb{N} individuals, each with an associated trivariate process Xℓ,n=(Zℓ,n,Uℓ,n,Hℓ,n)X^{\ell,n}=(Z^{\ell,n},U^{\ell,n},H^{\ell,n}). Foremost for notational convenience, we make the additional simplifying assumption that H1,n,N1,n,…,Hn,n,Nn,nH^{1,n},N^{1,n},\ldots,H^{n,n},N^{n,n} admit no simultaneous jumps. We denote by EE the state space of each Xℓ,nX^{\ell,n}, that is E=𝒥×[0,∞)×N0E=\mathcal{J}\times[0,\infty)\times\amsmathbb{N}\_{0}, and consider a measurable function g:E↦Rdg:E\mapsto\amsmathbb{R}^{d}, d∈Nd\in\amsmathbb{N}, satisfying the linear growth condition

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | ∥g​(x)∥≤C​(1+∥x∥),\displaystyle\lVert g(x)\rVert\leq C(1+\lVert x\rVert), |  |

for some C>0C>0. Based hereon, we define the averaged process νn\nu^{n} according to

|  |  |  |
| --- | --- | --- |
|  | νtn=1n​∑ℓ=1ng​(Xtℓ,n),\displaystyle\nu\_{t}^{n}=\frac{1}{n}\sum\_{\ell=1}^{n}g(X\_{t}^{\ell,n}), |  |

and we assume that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.3) |  | E​[Nj​kℓ,n​(d​t)|ℱt−]\displaystyle\amsmathbb{E}[N\_{jk}^{\ell,n}(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}] | =𝟙{Zt−ℓ,n=j}​μj​k​(t,Ut−ℓ,n,Ht−ℓ,n,νt−n)​d​t,\displaystyle=\mathds{1}\_{\{Z\_{t-}^{\ell,n}=j\}}\mu\_{jk}(t,U\_{t-}^{\ell,n},H\_{t-}^{\ell,n},\nu\_{t-}^{n})\mathrm{d}t, |  |
|  | E​[Hℓ,n​(d​t)|ℱt−]\displaystyle\amsmathbb{E}[H^{\ell,n}(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}] | =λZt−ℓ,n​(t,Ut−ℓ,n,Ht−ℓ,n,νt−n)​d​t.\displaystyle=\lambda\_{Z\_{t-}^{\ell,n}}(t,U\_{t-}^{\ell,n},H\_{t-}^{\ell,n},\nu\_{t-}^{n})\mathrm{d}t. |  |

The functions (t,u,h,y)↦μj​k​(t,u,h,y)(t,u,h,y)\mapsto\mu\_{jk}(t,u,h,y), j≠kj\neq k, are duration-, health- as well as collective-dependent transition rates, which we assume to be measurable and bounded on compacts. The functions (t,u,h,y)↦λj​(t,u,h,y)(t,u,h,y)\mapsto\lambda\_{j}(t,u,h,y) are health claim hazards of similar nature, which we also assume to be measurable and bounded on compacts.

###### Example 2.13.

As a concrete example of how the function gg might be chosen in practice, consider g​(z,u,h)=hg(z,u,h)=h. In this case,

|  |  |  |
| --- | --- | --- |
|  | νtn=1n​∑ℓ=1nHtℓ,n.\displaystyle\nu\_{t}^{n}=\frac{1}{n}\sum\_{\ell=1}^{n}H\_{t}^{\ell,n}. |  |

Consequently, the transition rate from the active to the disabled state may now depend on the average number of health insurance claims.

If the individuals have the same initial distribution, meaning πℓ,n\pi^{\ell,n} does not depend on ℓ\ell, then ([2.3](https://arxiv.org/html/2512.13562v1#S2.E3 "In 2.3. Extension: Collective health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach")) entails that the individuals are actually identically distributed. However, they are in general no longer independent and the Markov property holds neither for Xℓ,nX^{\ell,n} or νn\nu^{n} nor (Xℓ,n,νn)(X^{\ell,n},\nu^{n}); only the high-dimensional process Xn:=(X1,n,…,Xn,n)X^{n}:=(X^{1,n},\ldots,X^{n,n}) is always Markov. If we may think of νn\nu^{n} as an external process driving Z1,nZ^{1,n}, which in the context of Example [2.13](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem13 "Example 2.13. ‣ 2.3. Extension: Collective health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") would be the case if Hℓ,nH^{\ell,n} is locally independent of Zℓ,nZ^{\ell,n}, confer with [Aalen1987], computational simplifications could surface. It is the (causal) interaction between disabilities and health claims on a collective level that especially complicate the computational aspects.

The fact that XnX^{n} is a Markov process signifies, at least in principle, that transition probabilities and other quantities of interest may be computed by solving (high-dimensional) systems of integro-differential equations. However, even if we disregard health claims and duration effects, the computational complexity grows exponentially in nn. Thus, already for moderate nn, say n=50n=50, such a direct approach has to be abandoned. Monte Carlo methods constitute an alternative, but are rather slow and should, therefore, only be used as a kind of last resort.

In the next section, we explore an attractive alternative: mean-field approximations, where the process νn\nu^{n} is replaced by its mean, restoring the independence between individuals as well as the computational tractability.

## 3. Mean-field approximation

The idea behind mean-field approximations is to replace averages by mean values – noting that as n→∞n\to\infty, the average of nn exchangeable random variables convergens to their mean. Specifically, we want to replace the averaged process νn\nu^{n} in ([2.3](https://arxiv.org/html/2512.13562v1#S2.E3 "In 2.3. Extension: Collective health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach")) by its mean. The advantage of such an approximation would be the replacement of the high-dimensional nn-individual model by a one-individual limiting model, the so-called mean-field model.

### 3.1. Setup and mean-field convergence

The mean-field model corresponding to the nn-individual model of Subsection [2.3](https://arxiv.org/html/2512.13562v1#S2.SS3 "2.3. Extension: Collective health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") is given by the distribution-dependent trivariate process X¯=(Z¯,U¯,H¯)\bar{X}=(\bar{Z},\bar{U},\bar{H}), where U¯\bar{U} is the duration process associated with Z¯\bar{Z} and H¯\bar{H} is a counting process, with the following characteristics. First, and foremost for notational convenience, we assume that H¯\bar{H} and N¯\bar{N}, where N¯\bar{N} is the multivariate counting process associated with Z¯\bar{Z}, admit no simultaneous jumps. Further, we assume that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.1) |  | E​[N¯j​k​(d​t)|ℱt−]\displaystyle\amsmathbb{E}[\bar{N}\_{jk}(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}] | =𝟙{Z¯t−=j}​μj​k​(t,U¯t−,H¯t−,v​(t−))​d​t,\displaystyle=\mathds{1}\_{\{\bar{Z}\_{t-}=j\}}\mu\_{jk}\big(t,\bar{U}\_{t-},\bar{H}\_{t-},v(t-)\big)\mathrm{d}t, |  |
|  | E​[H¯​(d​t)|ℱt−]\displaystyle\amsmathbb{E}[\bar{H}(\mathrm{d}t)\,|\,\mathcal{F}\_{t-}] | =λZ¯t−​(t,U¯t−,H¯t−,v​(t−))​d​t,\displaystyle=\lambda\_{\bar{Z}\_{t-}}\big(t,\bar{U}\_{t-},\bar{H}\_{t-},v(t-)\big)\mathrm{d}t, |  |

where t↦v​(t):=E​[g​(X¯t)]t\mapsto v(t):=\amsmathbb{E}[g(\bar{X}\_{t})]. It is apparent that the empirical average νn\nu^{n} has been replaced by its expectation vv. Instead of depending on other individuals, the predictable compensators of an individual now depend on the distribution of the process X¯\bar{X} through the mean vv. This has certain mathematical implications, some of which are beneficial and some of which are not, as we shall soon demonstrate. The type of convergence that lies behind a mean-field approximation relates to the notion of chaosticity, which in the mean-field literature carries the following definition.

###### Definition 3.1.

Let the measurable space (S,𝒮)(S,\mathcal{S}) be standard Borel, and let Q\amsmathbb{Q} be a probability measure on (S,𝒮)(S,\mathcal{S}). Then a sequence of exchangeable probability measures (Qn)n∈N(\amsmathbb{Q}\_{n})\_{n\in\amsmathbb{N}}, with each Qn\amsmathbb{Q}\_{n} defined on the product space (Sn,⊗ℓ=1n𝒮)(S^{n},\otimes\_{\ell=1}^{n}\mathcal{S}), is said to be *Q\amsmathbb{Q}-chaotic* if

|  |  |  |
| --- | --- | --- |
|  | ∀k∈N:Qnk→wk⊗ℓ=1kQ,\displaystyle\forall k\in\amsmathbb{N}:\quad\amsmathbb{Q}\_{n}^{k}\overset{\text{wk}}{\to}\otimes\_{\ell=1}^{k}\amsmathbb{Q}, |  |

where Qnk(⋅):=Qn(⋅×Sn−k)\amsmathbb{Q}\_{n}^{k}(\,\cdot\,):=\amsmathbb{Q}\_{n}(\,\cdot\times S^{n-k}) for k<nk<n.

###### Remark 3.2.

As a gentle reminder to the reader, if Qn\amsmathbb{Q}\_{n} describes the distribution of random variables (Y1,n,…,Yn,n)(Y^{1,n},\ldots,Y^{n,n}), then Qn\amsmathbb{Q}\_{n} (or the random variables themselves) is said to be exchangeable if

|  |  |  |
| --- | --- | --- |
|  | (Y1,n,…,Y1,n)​=d​(Yσ​(1),n,…,Yσ​(n),n)\displaystyle(Y^{1,n},\ldots,Y^{1,n})\overset{\text{d}}{=}(Y^{\sigma(1),n},\ldots,Y^{\sigma(n),n}) |  |

for all permutations σ:{1,…,n}↦{1,…,n}\sigma:\{1,\ldots,n\}\mapsto\{1,\ldots,n\}. Intuitively, the joint distribution of the individuals is unchanged when the individuals are reordered and, consequently, all individuals must share the same marginal distribution. Note that independent and identically distributed random variables are automatically exchangeable.

Chaosticity, as Definition [3.1](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") reveals, entails that the individuals become asymptotically independent in the following manner: any fixed number of individuals become independent as the overall number of individuals goes to infinity.

In the following, we consider the processes X¯,X1,n\bar{X},X^{1,n}, …, Xn,nX^{n,n} as random variables taking values in the Skorokhod space D([0,T]:E)\amsmathbb{D}([0,T]:E) equipped with the Borel σ\sigma-algebra generated by the J1J\_{1}-topology; this is a standard Borel space. Let Qn:=Xn​(P)\amsmathbb{Q}\_{n}:=X^{n}(\amsmathbb{P}) and Q¯:=X¯​(P)\bar{\amsmathbb{Q}}:=\bar{X}(\amsmathbb{P}). We want to show that the sequence (Qn)n∈N(\amsmathbb{Q}\_{n})\_{n\in\amsmathbb{N}} is Q¯\bar{\amsmathbb{Q}}-chaotic; this is what is understood by ‘mean-field convergence’.

So far, we have refrained from restricting the initial distribution of XnX^{n} and X¯\bar{X}. By definition, U0ℓ,n=H0ℓ,n=U¯0=H¯0=0U^{\ell,n}\_{0}=H^{\ell,n}\_{0}=\bar{U}\_{0}=\bar{H}\_{0}=0. The minimal condition would thus be to assume π\pi-chaosticity of (Z01,n,…,Z0n,n)​(P)(Z^{1,n}\_{0},\ldots,Z^{n,n}\_{0})(\amsmathbb{P}) for some π\pi, which is the assumption we adopt in the remainder of this section. Note that if the individuals are independent and identically distributed at time zero, then this minimal condition is automatically satisfied with π=π1,1\pi=\pi^{1,1}.

The following conditions on the transition rates, the health claim hazards, and the averaging function gg are sufficient to ensure the desired mean-field convergence. For just the existence and uniqueness of the mean-field model, less may do. Furthermore, even for the convergence of the nn-individual to the mean-field model, we expect the Lipschitz conditions in the duration argument to be circumventable by carefully exploiting the distinctive pure jump nature of the processes involved. However, such further technical investigations are outside the scope of this paper.

###### Condition 1.

2. a)

   The transition rates (t,u,h,v)↦μj​k​(t,u,h,v)(t,u,h,v)\mapsto\mu\_{jk}(t,u,h,v), j≠kj\neq k, and the hazards (t,u,h,v)↦λj​(t,u,h,v)(t,u,h,v)\mapsto\lambda\_{j}(t,u,h,v) are bounded and satisfy the following Lipschitz conditions:There exist non-negative constants Cj​kC\_{jk} and CjC\_{j} such that, for all u1,u2∈[0,T]u\_{1},u\_{2}\in[0,T], all y1,y2∈Rdy\_{1},y\_{2}\in\amsmathbb{R}^{d}, and all h∈N0h\in\amsmathbb{N}\_{0}, it holds that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |μj​k​(t,u1,h,y1)−μj​k​(t,u2,h,y2)|\displaystyle\lvert\mu\_{jk}(t,u\_{1},h,y\_{1})-\mu\_{jk}(t,u\_{2},h,y\_{2})\rvert | ≤Cj​k​(|u1−u2|+∥y1−y2∥),\displaystyle\leq C\_{jk}\big(\lvert u\_{1}-u\_{2}\rvert+\lVert y\_{1}-y\_{2}\rVert\big), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |λj​(t,u1,h,y1)−λj​(t,u2,h,y2)|\displaystyle\lvert\lambda\_{j}(t,u\_{1},h,y\_{1})-\lambda\_{j}(t,u\_{2},h,y\_{2})\rvert | ≤Cj​(|u1−u2|+∥y1−y2∥).\displaystyle\leq C\_{j}\big(\lvert u\_{1}-u\_{2}\rvert+\lVert y\_{1}-y\_{2}\rVert\big). |  |
3. b)

   The averaging function (z,u,h)↦g​(z,u,h)(z,u,h)\mapsto g(z,u,h), in addition to the linear growth condition of ([2.2](https://arxiv.org/html/2512.13562v1#S2.E2 "In 2.3. Extension: Collective health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach")), satisfies the following Lipschitz condition: There exists a non-negative constant CgC\_{g} such that, for all u1,u2∈[0,T]u\_{1},u\_{2}\in[0,T], all z∈𝒥z\in\mathcal{J}, and all h∈N0h\in\amsmathbb{N}\_{0}, it holds that

   |  |  |  |
   | --- | --- | --- |
   |  | ∥g​(z,u1,h)−g​(z,u2,h)∥≤Cg​|u1−u2|.\displaystyle\lVert g(z,u\_{1},h)-g(z,u\_{2},h)\rVert\leq C\_{g}\big\lvert u\_{1}-u\_{2}\big\rvert. |  |

###### Remark 3.3.

Let 𝒫1​(E)\mathcal{P}\_{1}(E) denote all Borel probability measure on EE having finite first moment, and let W1W\_{1} denote the Wasserstein 11-distance on 𝒫1​(E)\mathcal{P}\_{1}(E). Condition [1](https://arxiv.org/html/2512.13562v1#Thmcondition1 "Condition 1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") is sufficient to ensure that (t,u,h,ρ)↦μj​k​(t,u,h,∫Eg​dρ)(t,u,h,\rho)\mapsto\mu\_{jk}(t,u,h,\int\_{E}g\,\mathrm{d}\rho), j≠kj\neq k, and (t,u,h,ρ)↦λj​(t,u,h,∫Eg​dρ)(t,u,h,\rho)\mapsto\lambda\_{j}(t,u,h,\int\_{E}g\,\mathrm{d}\rho) are bounded and satisfy the following Lipschitz conditions: There exist non-negative constants Cj​kC\_{jk} and CjC\_{j} such that, for all u1,u2∈[0,T]u\_{1},u\_{2}\in[0,T], all ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}\_{1}(E), and all h∈N0h\in\amsmathbb{N}\_{0}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |μj​k​(t,u1,h,∫Eg​dρ1)−μj​k​(t,u2,h,∫Eg​dρ2)|\displaystyle\bigg\lvert\mu\_{jk}\Big(t,u\_{1},h,\int\_{E}g\,\mathrm{d}\rho\_{1}\Big)-\mu\_{jk}\Big(t,u\_{2},h,\int\_{E}g\,\mathrm{d}\rho\_{2}\Big)\bigg\rvert | ≤Cj​k​(|u1−u2|+W1​(ρ1,ρ2)),\displaystyle\leq C\_{jk}\big(\lvert u\_{1}-u\_{2}\rvert+W\_{1}(\rho\_{1},\rho\_{2})\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |λj​(t,u1,h,∫Eg​dρ1)−λj​(t,u2,h,∫Eg​dρ2)|\displaystyle\bigg\lvert\lambda\_{j}\Big(t,u\_{1},h,\int\_{E}g\,\mathrm{d}\rho\_{1}\Big)-\lambda\_{j}\Big(t,u\_{2},h,\int\_{E}g\,\mathrm{d}\rho\_{2}\Big)\bigg\rvert | ≤Cj​(|u1−u2|+W1​(ρ1,ρ2)).\displaystyle\leq C\_{j}\big(\lvert u\_{1}-u\_{2}\rvert+W\_{1}(\rho\_{1},\rho\_{2})\big). |  |

This is the Lipschitz condition that is actually exploited to verify the existence and uniqueness of the mean-field model and to establish the desired mean-field convergence.

Due to Condition [1](https://arxiv.org/html/2512.13562v1#Thmcondition1 "Condition 1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"), we have conveniently and firmly positioned ourselves within the general mean-field theory, see for instance [Hornung2025]. Consequently, we immediately obtain the following result, which confirms the desired mean-field convergence and establishes the mean-field model as an approximation to the nn-individual model.

###### Theorem 3.4.

Suppose that Condition [1](https://arxiv.org/html/2512.13562v1#Thmcondition1 "Condition 1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") is met. Then the mean-field model exists and is unique. Further, with Qn:=Xn​(P)\amsmathbb{Q}\_{n}:=X^{n}(\amsmathbb{P}) and Q¯:=X¯​(P)\bar{\amsmathbb{Q}}:=\bar{X}(\amsmathbb{P}), it holds that (Qn)n∈N(\amsmathbb{Q}\_{n})\_{n\in\amsmathbb{N}} is Q¯\bar{\amsmathbb{Q}}-chaotic.

###### Proof.

We adopt the reparameterization of Remark [2.6](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") for both Xℓ,nX^{\ell,n} and X¯\bar{X}. This yields the following systems of integral equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ztℓ,n=∑k(k−Zt−ℓ,n)​Nkℓ,n​(d​t),d​Ytℓ,n\displaystyle\mathrm{d}Z^{\ell,n}\_{t}=\sum\_{k}\big(k-Z^{\ell,n}\_{t-}\big)N^{\ell,n}\_{k}(\mathrm{d}t),\hskip 5.69054pt\mathrm{d}Y^{\ell,n}\_{t} | =(t−Yt−ℓ,n)​∑kNkℓ,n​(d​t),d​Htℓ,n=d​Htℓ,n,\displaystyle=(t-Y^{\ell,n}\_{t-})\sum\_{k}N^{\ell,n}\_{k}(\mathrm{d}t),\hskip 5.69054pt\mathrm{d}H^{\ell,n}\_{t}=\mathrm{d}H^{\ell,n}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Z¯t=∑k(k−Z¯t−)​N¯k​(d​t),d​Y¯t\displaystyle\mathrm{d}\bar{Z}\_{t}=\sum\_{k}\big(k-\bar{Z}\_{t-}\big)\bar{N}\_{k}(\mathrm{d}t),\hskip 5.69054pt\mathrm{d}\bar{Y}\_{t} | =(t−Y¯t−)​∑kN¯k​(d​t),d​H¯t=d​H¯t,\displaystyle=(t-\bar{Y}\_{t-})\sum\_{k}\bar{N}\_{k}(\mathrm{d}t),\hskip 5.69054pt\mathrm{d}\bar{H}\_{t}=\mathrm{d}\bar{H}\_{t}, |  |

where Nkℓ,n:=∑jNj​kℓ,nN^{\ell,n}\_{k}:=\sum\_{j}N^{\ell,n}\_{jk} and N¯k:=∑jN¯j​k\bar{N}\_{k}:=\sum\_{j}\bar{N}\_{jk}. Propositions 5.7 and 6.6 of [Hornung2025] show that Condition [1](https://arxiv.org/html/2512.13562v1#Thmcondition1 "Condition 1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") is sufficient for the validity of Theorem 2.6 and 3.5 of [Hornung2025], with the former ensuring the existence and uniqueness of the mean-field model and the latter confirming the postulated chaosticity.
∎

We conclude this subsection with a brief discussion on regular conditional distributions in mean-field models. If YY is an ordinary Markov process, then it is completely described by its initial distribution and its transition probabilities. In particular, we may determine its occupation probabilities by integrating the transition probabilities with respect to the initial distribution or, vice versa, we may determine the initial distribution via disintegration of the occupation probabilities with respect to the transition probabilities. In other words, changing the initial distribution only affects the occupation probabilities – not the transition probabilities; confer also with the discussions in Section [2.1](https://arxiv.org/html/2512.13562v1#S2.SS1 "2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach").

In a mean-field model, the transition probabilities depend on the initial distribution, so changing the initial distribution affects not only the occupation probabilities, but also the transition probabilities. This means that caution should be exercised when interpreting conditional expectations such as E​[h​(X¯)|Z¯0=i]\amsmathbb{E}[h(\bar{X})\,|\,\bar{Z}\_{0}=i] for some suitably regular function hh. This expectation represents integration with respect to a regular conditional distribution of X¯\bar{X} given Z¯0\bar{Z}\_{0}, that is it involves the transition probabilities of X¯\bar{X}, which depend on the limiting initial distribution π\pi.

### 3.2. Actuarial applications

The contractual payments remain on the form ([2.1](https://arxiv.org/html/2512.13562v1#S2.E1 "In 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach")), meaning we consider Bℓ,nB^{\ell,n} and B¯\bar{B} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bℓ,n​(d​t)\displaystyle B^{\ell,n}(\mathrm{d}t) | =∑j𝟙{Zt−ℓ,n=j}​bj​(t,Ut−ℓ,n)​d​t+∑j≠kbj​k​(t,Ut−ℓ,n)​Nj​kℓ,n​(d​t),\displaystyle=\sum\_{j}\mathds{1}\_{\{Z^{\ell,n}\_{t-}=j\}}b\_{j}(t,U^{\ell,n}\_{t-})\mathrm{d}t+\sum\_{j\neq k}b\_{jk}(t,U^{\ell,n}\_{t-})N^{\ell,n}\_{jk}(\mathrm{d}t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B¯​(d​t)\displaystyle\bar{B}(\mathrm{d}t) | =∑j𝟙{Z¯t−=j}​bj​(t,U¯t−)​d​t+∑j≠kbj​k​(t,U¯t−)​N¯j​k​(d​t).\displaystyle=\sum\_{j}\mathds{1}\_{\{\bar{Z}\_{t-}=j\}}b\_{j}(t,\bar{U}\_{t-})\mathrm{d}t+\sum\_{j\neq k}b\_{jk}(t,\bar{U}\_{t-})\bar{N}\_{jk}(\mathrm{d}t). |  |

Recall that (t,u)↦bj​(t,u)(t,u)\mapsto b\_{j}(t,u) and (t,u)↦bj​k​(t,u)(t,u)\mapsto b\_{jk}(t,u) are measurable functions that are bounded on compacts. To transfer the mean-field convergence of Theorem [3.4](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"), additional technical conditions are required. It should be stressed, however, that these conditions hardly exclude any contracts encountered in the real world.

###### Condition 2.

2. a)

   The payment rates (t,u)↦bj​(t,u)(t,u)\mapsto b\_{j}(t,u) are piecewise continuous on diagonals, meaning for each non-negative τ\tau the functions t↦bj​(t,t−τ)t\mapsto b\_{j}(t,t-\tau) have at most countable numbers of discontinuities.
3. b)

   The transition payments (t,u)↦bj​k​(t,u)(t,u)\mapsto b\_{jk}(t,u) are absolutely continuous with respect to the two-dimensional Lebesgue measure.

The following results provide an actuarial perspective on Theorem [3.4](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"), illuminating how the weak convergence of state processes give rise to laws of large numbers that substantiate the use of mean-field approximations for, among other things, reserving purposes.

###### Proposition 3.5.

Suppose that Conditions [1](https://arxiv.org/html/2512.13562v1#Thmcondition1 "Condition 1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") and [2](https://arxiv.org/html/2512.13562v1#Thmcondition2 "Condition 2. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") are met. It then holds that

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1n∫0Te−∫0tr​(s)​ds​Bℓ,n​(d​t)​→L2​E​[∫0Te−∫0tr​(s)​ds​B¯​(d​t)].\displaystyle\frac{1}{n}\sum\_{\ell=1}^{n}\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{\ell,n}(\mathrm{d}t)\overset{L^{\!2}}{\to}\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\bar{B}(\mathrm{d}t)\bigg]. |  |

###### Proof.

Condition [2](https://arxiv.org/html/2512.13562v1#Thmcondition2 "Condition 2. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") is sufficient in order for B¯\bar{B}, viewed as a Borel mapping from D([0,T]:E)\amsmathbb{D}([0,T]:E) into R\amsmathbb{R}, to be Q¯\bar{\amsmathbb{Q}}-almost surely continuous, where Q¯:=X¯​(P)\bar{\amsmathbb{Q}}:=\bar{X}(\amsmathbb{P}). The desired result then follows from Theorem [3.4](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") and Proposition 6.4 of [Hornung2025].
∎

###### Corollary 3.6.

Suppose that Conditions [1](https://arxiv.org/html/2512.13562v1#Thmcondition1 "Condition 1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") and [2](https://arxiv.org/html/2512.13562v1#Thmcondition2 "Condition 2. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") are met. It then holds that

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1n∫0Te−∫0tr​(s)​ds​Bℓ,n​(d​t)​→𝑝​E​[∫0Te−∫0tr​(s)​ds​B¯​(d​t)].\displaystyle\frac{1}{n}\sum\_{\ell=1}^{n}\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{\ell,n}(\mathrm{d}t)\overset{p}{\to}\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\bar{B}(\mathrm{d}t)\bigg]. |  |

Furthermore, if π​(i)>0\pi(i)>0, then

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1n𝟙{Z0ℓ,n=i}​∫0Te−∫0tr​(s)​ds​Bℓ,n​(d​t)1n​∑ℓ=1n𝟙{Z0ℓ,n=i}​→𝑝​E​[∫0Te−∫0tr​(s)​ds​B¯​(d​t)|Z¯0=i].\displaystyle\frac{\frac{1}{n}\sum\_{\ell=1}^{n}\mathds{1}\_{\{Z^{\ell,n}\_{0}=i\}}\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{\ell,n}(\mathrm{d}t)}{\frac{1}{n}\sum\_{\ell=1}^{n}\mathds{1}\_{\{Z^{\ell,n}\_{0}=i\}}}\overset{p}{\to}\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\bar{B}(\mathrm{d}t)\,\bigg|\,\bar{Z}\_{0}=i\bigg]. |  |

###### Proof.

Since L2L^{\!2}-convergence implies convergence in probability, the first statement is a trivial consequence of Proposition [3.5](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach").
The second statement follows from Proposition 6.4 of [Hornung2025].
∎

The limits appearing in Proposition [3.5](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") and Corollary [3.6](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem6 "Corollary 3.6. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") are so-called mean-field prospective reserves. The state-wise prospective mean-field prospective reserves at contract inception, (V¯i)i(\bar{V}\_{i})\_{i}, are defined according to

|  |  |  |
| --- | --- | --- |
|  | V¯i=E​[∫0Te−∫0tr​(s)​ds​B¯​(d​t)|Z¯0=i],\displaystyle\bar{V}\_{i}=\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\bar{B}(\mathrm{d}t)\,\bigg|\,\bar{Z}\_{0}=i\bigg], |  |

while the portfolio-wide prospective mean-field reserve at contract inception V¯\bar{V} reads

|  |  |  |
| --- | --- | --- |
|  | V¯=E​[∫0Te−∫0tr​(s)​ds​B¯​(d​t)].\displaystyle\bar{V}=\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\bar{B}(\mathrm{d}t)\bigg]. |  |

If we denote by (A¯i)i(\bar{A}\_{i})\_{i} the so-called state-wise mean-field accumulated cash flows, which are given by

|  |  |  |
| --- | --- | --- |
|  | A¯i​(d​t)=E​[B¯​(d​t)|Z¯0=i],\displaystyle\bar{A}\_{i}(\mathrm{d}t)=\amsmathbb{E}[\bar{B}(\mathrm{d}t)\,|\,\bar{Z}\_{0}=i], |  |

then it holds that

|  |  |  |
| --- | --- | --- |
|  | V¯i=∫0Te−∫0tr​(s)​ds​A¯i​(d​t).\displaystyle\bar{V}\_{i}=\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\bar{A}\_{i}(\mathrm{d}t). |  |

In similar fashion, with A¯\bar{A} the mean-field accumulated cash flow given by

|  |  |  |
| --- | --- | --- |
|  | A¯​(d​t)=E​[B¯​(d​t)],\displaystyle\bar{A}(\mathrm{d}t)=\amsmathbb{E}[\bar{B}(\mathrm{d}t)], |  |

it holds that

|  |  |  |
| --- | --- | --- |
|  | V¯=∫0Te−∫0tr​(s)​ds​A¯​(d​t).\displaystyle\bar{V}=\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}\bar{A}(\mathrm{d}t). |  |

These prospective reserves and expected cash flows should be seen in comparison to those of the nn-individual model, namely (Vi1,n)i(V^{1,n}\_{i})\_{i}, V1,nV^{1,n}, (Ai1,n)i(A^{1,n}\_{i})\_{i}, and A1,nA^{1,n} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi1,n=E​[∫0Te−∫0tr​(s)​ds​B1,n​(d​t)|Z01,n=i],\displaystyle V^{1,n}\_{i}=\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{1,n}(\mathrm{d}t)\,\bigg|\,Z^{1,n}\_{0}=i\bigg], | V1,n=E​[∫0Te−∫0tr​(s)​ds​B1,n​(d​t)],\displaystyle\quad V^{1,n}=\amsmathbb{E}\bigg[\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{1,n}(\mathrm{d}t)\bigg], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai1,n​(d​t)=E​[B1,n​(d​t)|Z01,n=i],\displaystyle A^{1,n}\_{i}(\mathrm{d}t)=\amsmathbb{E}[B^{1,n}(\mathrm{d}t)\,|\,Z^{1,n}\_{0}=i], | A1,n​(d​t)=E​[B1,n​(d​t)],\displaystyle\quad A^{1,n}(\mathrm{d}t)=\amsmathbb{E}[B^{1,n}(\mathrm{d}t)], |  |

and satisfying

|  |  |  |
| --- | --- | --- |
|  | Vi1,n=∫0Te−∫0tr​(s)​ds​Ai1,n​(d​t),V1,n=∫0Te−∫0tr​(s)​ds​A1,n​(d​t).\displaystyle V^{1,n}\_{i}=\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}A^{1,n}\_{i}(\mathrm{d}t),\quad V^{1,n}=\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}A^{1,n}(\mathrm{d}t). |  |

The following proposition establishes the mean-field cash flows and reserves and viable approximations of their nn-individual counterparts.

###### Proposition 3.7.

Suppose that Conditions [1](https://arxiv.org/html/2512.13562v1#Thmcondition1 "Condition 1. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") and [2](https://arxiv.org/html/2512.13562v1#Thmcondition2 "Condition 2. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") are met. It then holds that

|  |  |  |
| --- | --- | --- |
|  | V1,n→V¯,Vi1,n→V¯i.\displaystyle V^{1,n}\to\bar{V},\quad V^{1,n}\_{i}\to\bar{V}\_{i}. |  |

Furthermore, for t≥0t\geq 0 it holds that

|  |  |  |
| --- | --- | --- |
|  | A1,n​(t)−A1,n​(0)→A¯​(t)−A¯​(0),Ai1,n​(t)−Ai1,n​(0)→A¯i​(t)−A¯i​(0).\displaystyle A^{1,n}(t)-A^{1,n}(0)\to\bar{A}(t)-\bar{A}(0),\quad A^{1,n}\_{i}(t)-A^{1,n}\_{i}(0)\to\bar{A}\_{i}(t)-\bar{A}\_{i}(0). |  |

###### Proof.

The argument for the expected cash flows is similar to that of the reserves, so we focus on the latter. Condition [2](https://arxiv.org/html/2512.13562v1#Thmcondition2 "Condition 2. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") is sufficient in order for the payments, viewed as Borel mappings from D([0,T]:E)\amsmathbb{D}([0,T]:E) into R\amsmathbb{R}, to be almost surely continuous. The desired result for the portfolio-wide reserves then follows from Theorem [3.4](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") and Proposition 6.3 of [Hornung2025]. Now note that the weak convergence of Theorem [3.4](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") can actually be lifted to regular conditional distributions, confer with Theorem 4.3 of [Hornung2025], whereby the desired result for state-wise reserves follows.
∎

Having formally verified the usefulness of the mean-field model, we now discuss how to calculate mean-field cash flows and reserves. To this end, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | p¯i​j​(t,u,h):=\displaystyle\bar{p}\_{ij}(t,u,h):= | P​(Z¯t=j,U¯t≤u,H¯t=h|Z¯0=i),\displaystyle\,\amsmathbb{P}(\bar{Z}\_{t}=j,\bar{U}\_{t}\leq u,\bar{H}\_{t}=h\,|\,\bar{Z}\_{0}=i), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p¯j​(t,u,h):=\displaystyle\bar{p}\_{j}(t,u,h):= | P​(Z¯t=j,U¯t≤u,H¯t=h)\displaystyle\,\amsmathbb{P}(\bar{Z}\_{t}=j,\bar{U}\_{t}\leq u,\bar{H}\_{t}=h) |  |

be the mean-field transition probabilities and occupation probabilities, respectively. Note that, with π\pi the limiting initial distribution,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | p¯j=∑iπ​(i)​p¯i​j,A¯=∑iπ​(i)​A¯i,V¯=∑iπ​(i)​V¯i.\displaystyle\bar{p}\_{j}=\sum\_{i}\pi(i)\bar{p}\_{ij},\quad\bar{A}=\sum\_{i}\pi(i)\bar{A}\_{i},\quad\bar{V}=\sum\_{i}\pi(i)\bar{V}\_{i}. |  |

The following two proposition expands Proposition [2.2](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") to not only include individual health claims, but also mean-field effects. It should be compared to Proposition [2.9](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem9 "Proposition 2.9. ‣ 2.2. Extension: Individual health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach").

###### Proposition 3.8.

It holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | A¯i​(d​t)\displaystyle\bar{A}\_{i}(\mathrm{d}t) | =∑j∑h=0∞∫0t(bj​(t,u)+∑k:k≠jbj​k​(t,u)​μj​k​(t,u,h,v​(t)))​p¯i​j​(t,d​u,h)​dt,\displaystyle=\sum\_{j}\sum\_{h=0}^{\infty}\int\_{0}^{t}\Big(b\_{j}(t,u)+\sum\_{k:k\neq j}b\_{jk}(t,u)\mu\_{jk}\big(t,u,h,v(t)\big)\Big)\bar{p}\_{ij}(t,\mathrm{d}u,h)\,\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A¯​(d​t)\displaystyle\bar{A}(\mathrm{d}t) | =∑j∑h=0∞∫0t(bj​(t,u)+∑k:k≠jbj​k​(t,u)​μj​k​(t,u,h,v​(t)))​p¯j​(t,d​u,h)​dt,\displaystyle=\sum\_{j}\sum\_{h=0}^{\infty}\int\_{0}^{t}\Big(b\_{j}(t,u)+\sum\_{k:k\neq j}b\_{jk}(t,u)\mu\_{jk}\big(t,u,h,v(t)\big)\Big)\bar{p}\_{j}(t,\mathrm{d}u,h)\,\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t)\displaystyle v(t) | =∑j∑h=0∞∫0tg​(j,u,h)​p¯j​(t,d​u,h)=∑iπ​(i)​∑j∑h=0∞∫0tg​(j,u,h)​p¯i​j​(t,d​u,h).\displaystyle=\sum\_{j}\sum\_{h=0}^{\infty}\int\_{0}^{t}g(j,u,h)\bar{p}\_{j}(t,\mathrm{d}u,h)=\sum\_{i}\pi(i)\sum\_{j}\sum\_{h=0}^{\infty}\int\_{0}^{t}g(j,u,h)\bar{p}\_{ij}(t,\mathrm{d}u,h). |  |

###### Proof.

The core argument is exactly the same as in the proof of Proposition [2.9](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem9 "Proposition 2.9. ‣ 2.2. Extension: Individual health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach").
∎

It is worth noting that the calculation of mean-field accumulated cash flows, and therefore also mean-field reserves, is thus no more involved than the calculation of expected accumulated cash flows and reserves in the one-individual model – if occupation and transition probabilities are readily available and intermediaries such as vv are easy to calculate.

###### Example 3.9.

Continuing Example [2.13](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem13 "Example 2.13. ‣ 2.3. Extension: Collective health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") with g​(z,u,h)=hg(z,u,h)=h, it follows that

|  |  |  |
| --- | --- | --- |
|  | v​(t)=∑j∑h=0∞h​p¯j​(t,t,h)=∑iπ​(i)​∑j∑h=0∞h​p¯i​j​(t,t,h),\displaystyle v(t)=\sum\_{j}\sum\_{h=0}^{\infty}h\bar{p}\_{j}(t,t,h)=\sum\_{i}\pi(i)\sum\_{j}\sum\_{h=0}^{\infty}h\bar{p}\_{ij}(t,t,h), |  |

which is rather straightforward to calculate based on the mean-field occupation or transition probabilities.

Let us begin by exploring the calculation of the mean-field occupation probabilities. In the following, we adopt the convention that (t,u,v)↦λj​(t,u,−1,v)(t,u,v)\mapsto\lambda\_{j}(t,u,-1,v) is constantly zero.

###### Proposition 3.10.

Let d≥0d\geq 0. It holds almost everywhere on [d,∞)[d,\infty) that

|  |  |  |
| --- | --- | --- |
|  | dd​t​p¯j​(t,t−d,h)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\bar{p}\_{j}(t,t-d,h) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑k:k≠j∫0tμk​j​(t,u,h,v​(t))​p¯k​(t,d​u,h)−∫0t−dμj∙​(t,u,h,v​(t))​p¯j​(t,d​u,h)\displaystyle=\sum\_{k:k\neq j}\int\_{0}^{t}\mu\_{kj}\big(t,u,h,v(t)\big)\bar{p}\_{k}(t,\mathrm{d}u,h)-\int\_{0}^{t-d}\mu\_{j\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptscriptstyle\bullet$}}}}}}\big(t,u,h,v(t)\big)\bar{p}\_{j}(t,\mathrm{d}u,h) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫0t−dλj​(t,u,h−1,v​(t))​p¯j​(t,d​u,h−1)−∫0t−dλj​(t,u,h,v​(t))​p¯j​(t,d​u,h)\displaystyle\quad+\int\_{0}^{t-d}\lambda\_{j}\big(t,u,h-1,v(t)\big)\bar{p}\_{j}(t,\mathrm{d}u,h-1)-\int\_{0}^{t-d}\lambda\_{j}\big(t,u,h,v(t)\big)\bar{p}\_{j}(t,\mathrm{d}u,h) |  |

with boundary conditions p¯j​(t,0,h)=𝟙{t=0}​𝟙{h=0}​π​(j)\bar{p}\_{j}(t,0,h)=\mathds{1}\_{\{t=0\}}\mathds{1}\_{\{h=0\}}\pi(j).

###### Proof.

Adopting the reparameterization and change of variables from Remark [2.6](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"), the result follows from Proposition 2.9 of [Hornung2025], which yields a forward equation for (Z¯,Y¯,H¯)(\bar{Z},\bar{Y},\bar{H}).
∎

Contrary to the second part of Proposition [2.10](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2.2. Extension: Individual health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"), the forward equation for the mean-field occupation probabilities is non-linear since the transition rates and health claim hazards depend on vv (in a possibly non-linear fashion) and vv is a function of the occupation probabilities themselves, confer with Proposition [3.8](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"). As a consequence, we can no longer be completely assured that the equations admit a unique solution. The practical consequence is that the actuary must be particularly vigilant regarding a solution’s mathematical characteristics and concrete impact.

Furthermore, the non-linearity of the equations gives reason to handle the mean-field transition probabilities with additional care. In the one-individual model, confer with Remark [2.5](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"), the evolution in time of the occupation and transition probabilities was identical and, hence, we could calculate the transition probabilities using the same equations as for the occupation probabilities, but with changed initial conditions (from π​(j)\pi(j) to 𝟙{i=j}\mathds{1}\_{\{i=j\}}). However, as we discussed briefly at the end of Subsection [3.1](https://arxiv.org/html/2512.13562v1#S3.SS1 "3.1. Setup and mean-field convergence ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"), in the mean-field model the evolution in time depends on the initial distribution through vv. The intuition is as follows. The mean-field occupation probabilities (p¯j)j(\bar{p}\_{j})\_{j} represent the occupation probabilities for a typical individual in a very large group of identically distributed individuals, who all have initial distribution π\pi and all depend on each other through the group average. Thus changing the initial distribution π\pi not only corresponds to changing the initial distribution of one individual, but it also corresponds to changing the initial distribution of the entire group and thus the group average. Or, in other words, trying to equate occupation probabilities from equations with different initial conditions corresponds to equating the occupation probabilities of two individuals with different initial conditions, but also from two different groups!

In summary, we cannot calculate the mean-field transition probabilities by simply changing the initial (or boundary) conditions. However, if we treat vv, which depends on the occupation probabilities, as fixed, we may actually calculate the mean-field transition probabilities in the usual manner.

###### Proposition 3.11.

Let d≥0d\geq 0. It holds almost everywhere on [d,∞)[d,\infty) that

|  |  |  |
| --- | --- | --- |
|  | dd​t​p¯i​j​(t,t−d,h)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\bar{p}\_{ij}(t,t-d,h) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑k:k≠j∫0tμk​j​(t,u,h,v​(t))​p¯i​j​(t,d​u,h)−∫0t−dμj∙​(t,u,h,v​(t))​p¯i​j​(t,d​u,h)\displaystyle=\sum\_{k:k\neq j}\int\_{0}^{t}\mu\_{kj}\big(t,u,h,v(t)\big)\bar{p}\_{ij}(t,\mathrm{d}u,h)-\int\_{0}^{t-d}\mu\_{j\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.65}{$\scriptscriptstyle\bullet$}}}}}}\big(t,u,h,v(t)\big)\bar{p}\_{ij}(t,\mathrm{d}u,h) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫0t−dλj​(t,u,h−1,v​(t))​p¯i​j​(t,d​u,h−1)−∫0t−dλj​(t,u,h,v​(t))​p¯i​j​(t,d​u,h)\displaystyle\quad+\int\_{0}^{t-d}\lambda\_{j}\big(t,u,h-1,v(t)\big)\bar{p}\_{ij}(t,\mathrm{d}u,h-1)-\int\_{0}^{t-d}\lambda\_{j}\big(t,u,h,v(t)\big)\bar{p}\_{ij}(t,\mathrm{d}u,h) |  |

with boundary conditions p¯i​j​(t,0,h)=𝟙{t=0}​𝟙{h=0}​𝟙{i=j}\bar{p}\_{ij}(t,0,h)=\mathds{1}\_{\{t=0\}}\mathds{1}\_{\{h=0\}}\mathds{1}\_{\{i=j\}}.

###### Proof.

Adopting the reparameterization and change of variables from Remark [2.6](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.1. Semi-Markov model ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"), the result follows from Proposition 2.8 of [Hornung2025], which yields a forward equation for (Z¯,Y¯,H¯)(\bar{Z},\bar{Y},\bar{H}).
∎

The intuition behind these linearized forward equations is as follows. Imagine a very large group of MM individuals of which all but one have initial distribution π\pi, while the remaining individual has a degenerate initial distribution, say this individual’s initial state is almost surely ii. Since the individuals solely depend on each other through their group average, and the contribution of one individual to this average is negligible as M→∞M\to\infty, we may still replace the average by vv – also when calculating the occupation probabilities of the remaining individual. However, for this individual the occupation probabilities now correspond to the mean-field transition probabilities (p¯i​j)j(\bar{p}\_{ij})\_{j}.

Collecting results leaves us with two ways of calculating the mean-field transition probabilities. Either we first determine the mean-field occupation probabilities by solving the non-linear forward equations from Proposition [3.10](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"), use these to calculate vv, and then finally find the mean-field transition probabilities by solving the linearized forward equations from Proposition [3.11](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem11 "Proposition 3.11. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"). Alternatively, we recall that

|  |  |  |
| --- | --- | --- |
|  | v​(t)=∑iπ​(i)​∑j∑h=0∞∫0tg​(j,u,h)​p¯i​j​(t,d​u,h),\displaystyle v(t)=\sum\_{i}\pi(i)\sum\_{j}\sum\_{h=0}^{\infty}\int\_{0}^{t}g(j,u,h)\bar{p}\_{ij}(t,\mathrm{d}u,h), |  |

consider the forward equations from Proposition [3.11](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem11 "Proposition 3.11. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") as non-linear, and solve these directly. If one is only interested in the mean-field transition probabilities (p¯i​j)j(\bar{p}\_{ij})\_{j} for a specific ii, the first method is to be preferred. Otherwise, neither method is inherently superior to the other and, in any case, for both methods the non-linearity entails that we may no longer be absolutely certain that the resulting solution is unique.

### 3.3. Statistical aspects

For most practical purposes, estimates of the (collective-dependent) health claims hazards (t,u,h,y)↦λj​(t,u,h,y)(t,u,h,y)\mapsto\lambda\_{j}(t,u,h,y) and transition rates (t,u,h,y)↦μj​k​(t,u,h,y)(t,u,h,y)\mapsto\mu\_{jk}(t,u,h,y), j≠kj\neq k, are required. If only a single collective is observed, identifiability of the collective effect may become particularly challenging. However, as briefly described in the introduction , we have the example of company level insurance plans in mind – with the insurer signing contracts with several (relatively independent) companies. In the following, we therefore outline how estimates may be obtained in the presence of multiple, mutually independent, groups; for notational convenience, we omit the inclusion of individual- and company-level covariates.

We begin by considering a single company consisting of nn employees observed in the interval [0,Rn][0,R^{n}], with RnR^{n} a common random time describing right-censoring of the company. Subject to classic assumptions, including independent right-censoring, the partial log-likelihoods

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡{ℒ}\displaystyle\log\{\mathcal{L}\} | =∑ℓ=1n∫0Rnlog⁡{λZt−ℓ,n​(t,Ut−ℓ,n,Ht−ℓ,n,νt−n)}​Hℓ,n​(d​t)\displaystyle=\sum\_{\ell=1}^{n}\int\_{0}^{R^{n}}\log\!\big\{\lambda\_{Z^{\ell,n}\_{t-}}\big(t,U\_{t-}^{\ell,n},H\_{t-}^{\ell,n},\nu\_{t-}^{n}\big)\big\}H^{\ell,n}(\mathrm{d}t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑ℓ=1n∫0RnλZt−ℓ,n​(t,Ut−ℓ,n,Ht−ℓ,n,νt−n)​dt,\displaystyle\quad-\sum\_{\ell=1}^{n}\int\_{0}^{R^{n}}\lambda\_{Z^{\ell,n}\_{t-}}\big(t,U\_{t-}^{\ell,n},H\_{t-}^{\ell,n},\nu\_{t-}^{n}\big)\,\mathrm{d}t, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡{ℒj​k}\displaystyle\log\{\mathcal{L}\_{jk}\} | =∑ℓ=1n∫0Rnlog⁡{μj​k​(t,Ut−ℓ,n,Ht−ℓ,n,νt−n)}​Nj​kℓ,n​(d​t)\displaystyle=\sum\_{\ell=1}^{n}\int\_{0}^{R^{n}}\log\!\big\{\mu\_{jk}\big(t,U\_{t-}^{\ell,n},H\_{t-}^{\ell,n},\nu\_{t-}^{n}\big)\big\}N^{\ell,n}\_{jk}(\mathrm{d}t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑ℓ=1n∫0Rnμj​k​(t,Ut−ℓ,n,Ht−ℓ,n,νt−n)​𝟙{Zt−ℓ,n=j}​dt,\displaystyle\quad-\sum\_{\ell=1}^{n}\int\_{0}^{R^{n}}\mu\_{jk}\big(t,U\_{t-}^{\ell,n},H\_{t-}^{\ell,n},\nu\_{t-}^{n}\big)\mathds{1}\_{\{Z^{\ell,n}\_{t-}=j\}}\,\mathrm{d}t, |  |

offer a reasonable starting point for inference, confer with Section III.4 in [AndersenBorganGillKeiding1993].

In the presence of multiple, mutually independent, companies, the relevant partial log-likelihoods are simply sums of the each company’s contribution. Temporarily discretizing the transition rates and health claims hazards using a grid with time, duration, etc., usually produces a good approximation, and the resulting expressions correspond to Poisson likelihoods with occurrences and exposures as one might expect. Therefore, estimates of health claims hazards and transition rates may be obtained non-parametrically, semi-parametrically, or parametrically using standard techniques for occurrence and exposure data.

## 4. Practical implementation

The expected accumulated cash flows and prospective reserves may be computed from the transition and occupation probabilities via numerical integration and, for instance, using the trapezoidal rule. It is the computaton of probabilities based on forward integro-differential equations that requires special attention. In the following, we briefly describe how the meta-algorithm of [BuchardtMollerSchmidt2015] can be adapted to be fit for purpose for the task at hand. We focus on the system of Proposition [3.10](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"); the other systems of integro-differential equations are, ultimately, special cases or of significantly less sophistication.

Obviously, p¯j​(t,t−d,h)=0\bar{p}\_{j}(t,t-d,h)=0 for d>td>t and p¯j​(t,t−d,h)=p¯j​(t,t,h)\bar{p}\_{j}(t,t-d,h)=\bar{p}\_{j}(t,t,h) for d<0d<0. We therefore for η>0\eta>0 with T/η∈NT/\eta\in\amsmathbb{N} consider the discretization 𝒟\mathcal{D} of {(t,d,h)∈[0,T]2×N0:d≤t}\{(t,d,h)\in[0,T]^{2}\times\amsmathbb{N}\_{0}:d\leq t\} consisting of points (η​m,η​n,h)(\eta m,\eta n,h) for n,m,h∈N0n,m,h\in\amsmathbb{N}\_{0} with n≤m≤T/ηn\leq m\leq T/\eta.

The goal is to calculate (p¯j)j(\bar{p}\_{j})\_{j} on 𝒟\mathcal{D}. This first involves selecting a cut-off KHK\_{H} and for all jj equating p¯j​(⋅,⋅,h)\bar{p}\_{j}(\cdot,\cdot,h) with zero for h>KHh>K\_{H}. To select the cut-off, one may look for a deterministic constant λ~\tilde{\lambda} which uniformly bounds the health claims hazards on [0,T][0,T], and then for an error threshold err>0\text{err}>0 select KH=inf{K∈N0:P​(H~>K)<err}K\_{H}=\inf\{K\in\amsmathbb{N}\_{0}:\amsmathbb{P}(\tilde{H}>K)<\text{err}\}, where H~∼Poisson​(λ~​T)\tilde{H}\sim\text{Poisson}(\tilde{\lambda}T). Next, one can apply the following meta-algorithm:

Initial stage (0). The boundary conditions yield the values p¯j​(0,0,h)=𝟙{h=0}​π​(j)\bar{p}\_{j}(0,0,h)=\mathds{1}\_{\{h=0\}}\pi(j) for all jj and all hh.

Subsequent stages (m+1m+1). The non-linear integro-differential equations of Proposition [3.10](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") together with the formula for vv of Proposition [3.8](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") may be used to calculate

|  |  |  |
| --- | --- | --- |
|  | p¯j​(η​(m+1),η​(m+1)−d,h)\displaystyle\bar{p}\_{j}(\eta(m+1),\eta(m+1)-d,h) |  |
|  |  |  |
| --- | --- | --- |
|  | for all ​j​ and all ​h​ and ​d∈{0,η,η​2,…,η​(m+1)}\displaystyle\text{for all }j\text{ and all }h\text{ and }d\in\{0,\eta,\eta 2,\ldots,\eta(m+1)\} |  |

based on

|  |  |  |
| --- | --- | --- |
|  | p¯j​(η​m,η​m−d,h)​ for all ​j​ and all ​h​ and ​d∈{0,η,η​2,…,η​m}\displaystyle\bar{p}\_{j}(\eta m,\eta m-d,h)\text{ for all }j\text{ and all }h\text{ and }d\in\{0,\eta,\eta 2,\ldots,\eta m\} |  |

and the boundary conditions

|  |  |  |
| --- | --- | --- |
|  | p¯j​(η​(m+1),0,h)=0​ for all ​j​ and all ​h.\displaystyle\bar{p}\_{j}(\eta(m+1),0,h)=0\text{ for all }j\text{ and all }h. |  |

This can be done using for instance Euler steps, taking care of the integrals via the trapezoidal rule. Efficiency may be gained by storing and reusing computations related to the integrals.

The sequence of stages for m=0,1,2,3m=0,1,2,3 is illustrated in Figure [2](https://arxiv.org/html/2512.13562v1#S4.F2 "Figure 2 ‣ 4. Practical implementation ‣ Disability insurance with collective health claims: a mean-field approach"), which mirrors Figure 2 in [BuchardtMollerSchmidt2015]. The time complexity given a cut-off KHK\_{H} is of the same order as in the classic semi-Markov disability model, but differs by about a factor of KHK\_{H}.

ttddBoundary conditionsp¯j​(η​3,0,h)=0\bar{p}\_{j}(\eta 3,0,h)=0p¯j​(η​3,η,h)\bar{p}\_{j}(\eta 3,\eta,h)p¯j​(η​3,η​2,h)\bar{p}\_{j}(\eta 3,\eta 2,h)p¯j​(η​3,η​3,h)\bar{p}\_{j}(\eta 3,\eta 3,h)0η\etaη​2\eta 2η​3\eta 30η\etaη​2\eta 2η​3\eta 3

Figure 2. Illustration of a sequence of stages in the meta-algorithm.

## 5. Simulation study

The purpose of this section is to assess the quality of the mean-field approximation through a practice-oriented simulation study. In Subsection [5.1](https://arxiv.org/html/2512.13562v1#S5.SS1 "5.1. Setup ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach"), we outline the specific model and its connection to practice. Subsection [5.2](https://arxiv.org/html/2512.13562v1#S5.SS2 "5.2. Main results ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach") concerns the quality of mean-field reserves compared to a naïve Monte Carlo approach. Finally, Subsection [5.3](https://arxiv.org/html/2512.13562v1#S5.SS3 "5.3. Further findings ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach") presents some additional insights on the nature and the convergence of the mean-field approximation.

### 5.1. Setup

In order to specify a concrete model, we must specify the initial distribution, transition rates (t,u,h,y)↦μj​k​(t,u,h,y)(t,u,h,y)\mapsto\mu\_{jk}(t,u,h,y), j≠kj\neq k, health claims hazards (t,u,h,y)↦λj​(t,u,h,y)(t,u,h,y)\mapsto\lambda\_{j}(t,u,h,y), and the function gg. For the initial distribution, we assume for simplicity that individuals are independent and active at time zero. For the health claims hazards, we follow Example [2.7](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem7 "Example 2.7. ‣ 2.2. Extension: Individual health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") and choose λj​(t,u,h,y)≡λj\lambda\_{j}(t,u,h,y)\equiv\lambda\_{j} with parameter values

|  |  |  |
| --- | --- | --- |
|  | λ1=0.2,λ2=0.3,λ3=0,\displaystyle\lambda\_{1}=0.2,\quad\lambda\_{2}=0.3,\quad\lambda\_{3}=0, |  |

implying in particular that health claims are 50%50\,\% more likely while disabled than active. For the transition rates, we choose

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ12​(t,y)\displaystyle\mu\_{12}(t,y) | =e−9.55+0.24​(t+45)−0.0046​(t+45)2+0.000036​(t+45)3​eβ​min⁡{11+t​(y+ζ1)−ζ1,ζ0},\displaystyle=e^{-9.55+0.24(t+45)-0.0046(t+45)^{2}+0.000036(t+45)^{3}}e^{\beta\min\!\big\{\frac{1}{1+t}(y+\zeta\_{1})-\zeta\_{1},\zeta\_{0}\big\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ13​(t)\displaystyle\mu\_{13}(t) | =0.0005+105.52+0.038​(t+45)−10,\displaystyle=0.0005+10^{5.52+0.038(t+45)-10}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ21​(t,u)\displaystyle\mu\_{21}(t,u) | =e2.11−0.039​(t+45)−1.44​u,\displaystyle=e^{2.11-0.039(t+45)-1.44u}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ23​(t,u)\displaystyle\mu\_{23}(t,u) | =0.0005+105.52+0.038​(t+45)−10+e−2.79−0.23​u.\displaystyle=0.0005+10^{5.52+0.038(t+45)-10}+e^{-2.79-0.23u}. |  |

In particular, solely the disability rate depends on the collective and solely the recovery rate and the disability mortality depend on duration. The collective effect on the disability rate is included via the term

|  |  |  |
| --- | --- | --- |
|  | β​min⁡{11+t​(y+ζ1)−ζ1,ζ0}\displaystyle\beta\min\!\Big\{\frac{1}{1+t}(y+\zeta\_{1})-\zeta\_{1},\zeta\_{0}\Big\} |  |

with parameter values

|  |  |  |
| --- | --- | --- |
|  | β=2,ζ1=0.1,ζ0=0.4.\displaystyle\beta=2,\quad\zeta\_{1}=0.1,\quad\zeta\_{0}=0.4. |  |

Finally, we follow Examples [2.13](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem13 "Example 2.13. ‣ 2.3. Extension: Collective health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach") and [3.9](https://arxiv.org/html/2512.13562v1#S3.Thmtheorem9 "Example 3.9. ‣ 3.2. Actuarial applications ‣ 3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach") and choose g​(z,u,h)≡hg(z,u,h)\equiv h, meaning that the dependence on the collective stems only from the average of health claims. This corresponds to the average and expectation

|  |  |  |
| --- | --- | --- |
|  | νtn=1n​∑ℓ=1nHtℓ,n,v​(t)=∑j∑h=0∞h​p¯1​j​(t,t,h)\displaystyle\nu^{n}\_{t}=\frac{1}{n}\sum\_{\ell=1}^{n}H^{\ell,n}\_{t},\quad v(t)=\sum\_{j}\sum\_{h=0}^{\infty}h\bar{p}\_{1j}(t,t,h) |  |

for the nn-individual and mean-field model, respectively.

The collective health claims influence the disability rate μ12\mu\_{12} by means of a credibility factor, taking into account time passed. Inserting y=νny=\nu^{n}, we identify the term

|  |  |  |
| --- | --- | --- |
|  | 11+t​(νtn+ζ1)=tt+1​νtnt+1t+1​ζ1\displaystyle\frac{1}{1+t}(\nu^{n}\_{t}+\zeta\_{1})=\frac{t}{t+1}\frac{\nu^{n}\_{t}}{t}+\frac{1}{t+1}\zeta\_{1} |  |

as a credibility formula between the collective rate νtn/t\nu^{n}\_{t}/t and a baseline ζ1\zeta\_{1}. Consequently,

|  |  |  |
| --- | --- | --- |
|  | 11+t​(νtn+ζ1)−ζ1\displaystyle\frac{1}{1+t}(\nu^{n}\_{t}+\zeta\_{1})-\zeta\_{1} |  |

yields the deviation from the baseline. At time zero, where no collective information is available, all weight is placed on the baseline ζ1\zeta\_{1}. As time passes – and more and more information becomes available – more and more weight is based on the collective rate νtn/t\nu^{n}\_{t}/t. However, by introducing a maximum positive deviation given by the parameter ζ0\zeta\_{0}, we ensure that in no case can the deviation exceed ζ0\zeta\_{0}. (This has the technical benefit of ensuring the transition rate to be bounded.) Finally, the parameter β\beta controls the influence of health claims on the disability rate.

The parametrizations mirror forms seen in practice, and the parameter values are chosen to obtain rates which are reasonable for an individual of age 4545 years. Select parameter values are collected in Table [1](https://arxiv.org/html/2512.13562v1#S5.T1 "Table 1 ‣ 5.1. Setup ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach"). It is worth noting that the baseline ζ1\zeta\_{1} is chosen quite low compared to the health claims rates λ1\lambda\_{1}, λ2\lambda\_{2}, λ3\lambda\_{3}.

| Parameter | Value | Description |
| --- | --- | --- |
| λ1\lambda\_{1} | 0.2 | Health claims rate, active |
| λ2\lambda\_{2} | 0.3 | Health claims rate, disabled |
| λ3\lambda\_{3} | 0 | Health claims rate, dead |
| ζ1\zeta\_{1} | 0.1 | Collective health claims effect, baseline |
| ζ0\zeta\_{0} | 0.5 | Collective health claims effect, maximum |
| β\beta | 2 | Collective health claims effect, influence |

Table 1. Select parameter values for the simulation study.

Following Example [2.8](https://arxiv.org/html/2512.13562v1#S2.Thmtheorem8 "Example 2.8. ‣ 2.2. Extension: Individual health claims ‣ 2. Disability model with health claims ‣ Disability insurance with collective health claims: a mean-field approach"), the contractual payments correspond to a disability annuity with a waiting period. That is, we consider

|  |  |  |
| --- | --- | --- |
|  | d​Btℓ,n=𝟙(Zt−ℓ,n=2)​b2​(t,Utℓ,n)​d​t\displaystyle\mathrm{d}B\_{t}^{\ell,n}=\mathds{1}\_{(Z\_{t-}^{\ell,n}=2)}b\_{2}(t,U\_{t}^{\ell,n})\mathrm{d}t |  |

with b2​(t,u)=𝟙(u≥ε)​bb\_{2}(t,u)=\mathds{1}\_{(u\geq\varepsilon)}b. We choose b=1b=1 and ε=0.25\varepsilon=0.25, the latter corresponding to the rather common waiting period of three months. Finally, we choose r=0.01r=0.01 and T=25T=25.

### 5.2. Main results

Since solving the forward integro-differential equations for the nn-individual model is not computationally feasible for n≫1n\gg 1, we mainly consider two ways of calculating the reserve V1,nV^{1,n}:

1. (1)

   By means of a naïve Monte Carlo method, repeatedly simulating the nn-individual model
2. (2)

   Employing the mean-field approximation V¯≈V1,n\bar{V}\approx V^{1,n} and solving the resulting non-linear integro-differential equations.

In the naïve Monte Carlo method, we repeatedly sample paths of the process Xn=(X1,n,…,Xn,n)X^{n}=(X^{1,n},\ldots,X^{n,n}) via inhomogeneous Poisson processes using the by now classic acceptance-rejection method described in [LewisShedler1979]. Denoting the samples by m=1,…,Mm=1,\ldots,M, this yields the estimate

|  |  |  |
| --- | --- | --- |
|  | 1M​∑m=1M(1n​∑ℓ=1n∫0Te−∫0tr​(s)​ds​Bℓ,n,m​(d​t)),\displaystyle\frac{1}{M}\sum\_{m=1}^{M}\bigg(\frac{1}{n}\sum\_{\ell=1}^{n}\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{\ell,n,m}(\mathrm{d}t)\bigg)\!, |  |

which for n≫0n\gg 0 should have substantially lower variance than the neonatal estimate

|  |  |  |
| --- | --- | --- |
|  | 1M​∑m=1M∫0Te−∫0tr​(s)​ds​B1,n,m​(d​t)\displaystyle\frac{1}{M}\sum\_{m=1}^{M}\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{1,n,m}(\mathrm{d}t) |  |

due to chaosticity.

To solve the integro-differential equations, compute the expected accumulated cash flows, and finally calculate the reserves, we adopted the implementation outlined in Section [4](https://arxiv.org/html/2512.13562v1#S4 "4. Practical implementation ‣ Disability insurance with collective health claims: a mean-field approach"). In particular, we employed the Euler method and, for numerical integration, the trapezoidal rule. Throughout, we used a step length of 0.010.01 and a cut-off KH=20K\_{H}=20, having verified that shortening the step length or increasing the cut-off does not appear to significantly alter results. For n>1n>1 we only consider the mean-field approximation. For n=1n=1 we also consider the one-individual model, yielding the ‘true’ value for the reserve.

| nn | Mean-field | Monte Carlo | True |
| --- | --- | --- | --- |
| 1 | 1.6294 | 1.6473 | 1.6681 |
| 2 | 1.6294 | 1.6506 | — |
| 5 | 1.6294 | 1.6610 | — |
| 25 | 1.6294 | 1.6329 | — |
| 50 | 1.6294 | 1.6305 | — |
| 100 | 1.6294 | 1.6288 | — |

Table 2. Reserves V1,nV^{1,n} computed using the mean-field approximation and a naïve Monte Carlo method (with sample size M=40,000M=40,000), respectively, for n=1,2,5,25,50,100n=1,2,5,25,50,100.

We present our main results in Table [2](https://arxiv.org/html/2512.13562v1#S5.T2 "Table 2 ‣ 5.2. Main results ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach"); for the Monte Carlo method, a large sample size of M=40,000M=40,000 is chosen. The first observation is that that both the mean-field approximation and the Monte Carlo estimate deviate substantially from the true value for the one-individual model. While this is to be expected from the mean-field approximation, and indicates that the collective effect on the disability rate is non-negligible, it also signifies that the Monte Carlo estimate has not converged for n=1n=1. For n=2,5n=2,5 we continue to see substantial differences between the mean-field approximation and the Monte Carlo estimates, while for n=25,50,100n=25,50,100 the differences are less pronounced. The seemingly increased stability of the Monte Carlo estimates for larger nn are due to the aforementioned chaosticity-induced variance reduction.

The deviations between the mean-field approximation and the Monte Carlo estimates could indicate that the mean-field approximation is somewhat poor, that the Monte Carlo estimate has yet to fully converge, or both. Table [3](https://arxiv.org/html/2512.13562v1#S5.T3 "Table 3 ‣ 5.2. Main results ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach") contains statistics for 5050 repeated applications of the naïve Monte Carlo method with n=2,5,25n=2,5,25. The quantiles and the standard deviations both indicate substantial variance in the Monte Carlo estimates, and for n=5,25n=5,25 the mean-field approximation is contained in the empirical 90%90\,\% confidence intervals. This both confirms that M=40,000M=40,000 does not suffice to ensure the convergence of the Monte Carlo estimates and that the mean-field approximation constitutes a necessary, and rather efficient, alternative already for moderate nn.

| nn | Second lowest | Average | Second highest | Standard deviation |
| --- | --- | --- | --- | --- |
| 2 | 1.6322 | 1.6510 | 1.6734 | 0.0122 |
| 5 | 1.6268 | 1.6431 | 1.6610 | 0.0087 |
| 25 | 1.6260 | 1.6329 | 1.6392 | 0.0035 |

Table 3. Statistics for 5050 repeated applications of the naïve Monte Carlo method to estimate V1,nV^{1,n} with n=2,5,25n=2,5,25.

### 5.3. Further findings

The reserve in the one-individual model is about 2.38%2.38\,\% larger than the mean-field reserve. This is because in the one-individual model, the effect of health claims on the disability rate is calculated based only on the health claims history of a single individual, meaning that the (likely) occurrence of just one health claim causes the disability rate to spike quite violently upwards, confer also with Figure [3](https://arxiv.org/html/2512.13562v1#S5.F3 "Figure 3 ‣ 5.3. Further findings ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach"). Since this is not similarly counteracted by downwards movements, there is a larger probability of disability in the one-individual model compared to the mean-field approximation and consequently also a larger reserve.

The mean-field convergence implies that νn→v\nu^{n}\to v as n→∞n\to\infty. This convergence is neatly illustrated in Figure [5](https://arxiv.org/html/2512.13562v1#S5.F5 "Figure 5 ‣ 5.3. Further findings ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach"), which mirrors Figure [3](https://arxiv.org/html/2512.13562v1#S5.F3 "Figure 3 ‣ 5.3. Further findings ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach"), but has n=5,25,100n=5,25,100 rather than n=1n=1. Substantial deviations in disability rate appear even for n=25n=25.

![Refer to caption](x1.png)


Figure 3. Disability rate (left) and credibility formula (right) for a single realization of the one-individual model (y=ν1y=\nu^{1}) with the mean-field approximation (y=vy=v) and the baseline (y=ζ1y=\zeta\_{1}).

![Refer to caption](x2.png)


Figure 4. Histograms of average present values for n=5,25,50,100n=5,25,50,100; as nn increases, a clear bell curve emerges.

![Refer to caption](x3.png)


Figure 5. For n=5,25,100n=5,25,100 disability rates (left) and credibility formulas (right) for a single realization of the nn-individual model (y=νny=\nu^{n}) with the mean-field approximation (y=vy=v) and the baseline (y=ζ1y=\zeta\_{1}).

To assess the quality of the convergence, we may additionally study histograms of the average present values

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1n∫0Te−∫0tr​(s)​ds​Bℓ,n,m​(d​t)\displaystyle\frac{1}{n}\sum\_{\ell=1}^{n}\int\_{0}^{T}e^{-\int\_{0}^{t}r(s)\,\mathrm{d}s}B^{\ell,n,m}(\mathrm{d}t) |  |

for m=1,…,Mm=1,\ldots,M, where M=40,000M=40,000. The resulting histograms for n=5,25,50,100n=5,25,50,100 can be found in Figure [4](https://arxiv.org/html/2512.13562v1#S5.F4 "Figure 4 ‣ 5.3. Further findings ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach"). For n≥50n\geq 50 the clear shape of a bell curve emerges, which would seem to indicate that besides the laws of large numbers already covered in Section [3](https://arxiv.org/html/2512.13562v1#S3 "3. Mean-field approximation ‣ Disability insurance with collective health claims: a mean-field approach"), a central limit theorem might also hold. Proposition 6.5 in [Hornung2025] confirms exactly such a central limit theorem, but subject to a covariance condition that is difficult to verify theoretically. Figure [4](https://arxiv.org/html/2512.13562v1#S5.F4 "Figure 4 ‣ 5.3. Further findings ‣ 5. Simulation study ‣ Disability insurance with collective health claims: a mean-field approach") offers empirical support for the conjecture that, in this specific model, the condition is met.

## 6. Outlook

Throughout, we have made the assumption that the group of insured is closed – that is, members do not leave and new members do not join. This is not realistic for the application we have in mind, where group members constitute employees and the group a specific employer. To capture such policyholder behavior and sampling effects, one can expand the state-space to encompass group entries and exits. This poses no added difficulty for the mean-field theory or for likelihood-based estimation, except that one may have to adjust ν\nu to the situation at hand. Such adjustments, and other alternative choices of ν\nu, constitute an interesting avenue for future work. Having expanded the state-space, the prospective reserve will in general depend on the entry and exit rates through the average vv, since entries and exits may affect the overall group composition. By pricing under the assumption that the entry and exit rates are zero, one first and foremost makes the case that historical data are representative for future developments.

In this paper, we focus on valuation at contract inception by firmly placing ourselves at initial time t0=0t\_{0}=0 in the calculation of reserves, and we make the simplifying assumption that U0ℓ,n=H0ℓ,n=0U^{\ell,n}\_{0}=H^{\ell,n}\_{0}=0 and thus U¯0=H¯0=0\bar{U}\_{0}=\bar{H}\_{0}=0. To establish mean-field convergence, we only needed the assumption of π\pi-chaosticity for (Z01,n,…,Z0n,n)​(P)(Z^{1,n}\_{0},\ldots,Z^{n,n}\_{0})(\amsmathbb{P}) for some π\pi. If we instead place ourselves at initial time t0>0t\_{0}>0, the values Ut0ℓ,nU^{\ell,n}\_{t\_{0}}, Ht0ℓ,nH^{\ell,n}\_{t\_{0}}, U¯t0\bar{U}\_{t\_{0}}, and H¯t0\bar{H}\_{t\_{0}} are random. However, if everything develops according to the stipulated model, the empirical distribution of (Xt01,n,…,Xt0n,n)(X^{1,n}\_{t\_{0}},\ldots,X^{n,n}\_{t\_{0}}) will be X¯t0​(P)\bar{X}\_{t\_{0}}(\amsmathbb{P})-chaotic, confer with Proposition 2.2 of [Sznitman1991] and Proposition 1.4 of [Kallenberg2005]. In this case, the entire set of results for, implicitly, t0=0t\_{0}=0 also applies to t0>0t\_{0}>0. For further discussion of such matters, confer with Section 6 in [Hornung2025].

## Acknowledgments

Both authors have carried out this research in association with the project frame InterAct.

## Disclosure statement

The expressed opinions are attributable solely to us and do not necessarily reflect the views of any of our past, current, and future employers.