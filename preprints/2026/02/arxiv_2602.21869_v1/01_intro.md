---
authors:
- Mattia Marzi
- Tiziano Squartini
doc_id: arxiv:2602.21869v1
family_id: arxiv:2602.21869
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Bayesian approach to out-of-sample network reconstruction
url_abs: http://arxiv.org/abs/2602.21869v1
url_html: https://arxiv.org/html/2602.21869v1
venue: arXiv q-fin
version: 1
year: 2026
---


Mattia Marzi
[mattia.marzi@imtlucca.it](mailto:mattia.marzi@imtlucca.it)
IMT School for Advanced Studies, P.zza San Francesco 19, 55100 Lucca (Italy)
INdAM-GNAMPA Istituto Nazionale di Alta Matematica ‘Francesco Severi’, P.le Aldo Moro 5, 00185 Rome (Italy)
  
Tiziano Squartini
IMT School for Advanced Studies, P.zza San Francesco 19, 55100 Lucca (Italy)
Scuola Normale Superiore, P.zza dei Cavalieri 7, 56126 Pisa (Italy)
INdAM-GNAMPA Istituto Nazionale di Alta Matematica ‘Francesco Severi’, P.le Aldo Moro 5, 00185 Rome (Italy)

###### Abstract

Networks underpin systems that range from finance to biology, yet their structure is often only partially observed. Current reconstruction methods typically fit the parameters of a model anew to each snapshot, thus offering no guidance to predict future configurations. Here, we develop a Bayesian approach that uses the information about past network snapshots to inform a prior and predict the subsequent ones, while quantifying uncertainty. Instantiated with a single-parameter fitness model, our method infers link probabilities from node strengths and carries information forward in time. When applied to the Electronic Market for Interbank Deposit across the years 19991999-20122012, our method accurately recovers the number of connections per bank at subsequent times, outperforming probabilistic benchmarks designed for analogous, link prediction tasks. Notably, each predicted snapshot serves as a reliable prior for the next one, thus enabling self-sustained, out-of-sample reconstruction of evolving networks with a minimal amount of additional data.

## INTRODUCTION

### Network reconstruction: a quick overview

Network theory is employed to address problems of scientific and societal relevance, from the prediction of epidemic spreading to the identification of early-warning signals of upcoming financial crises [[1](https://arxiv.org/html/2602.21869v1#bib.bib1), [2](https://arxiv.org/html/2602.21869v1#bib.bib2), [3](https://arxiv.org/html/2602.21869v1#bib.bib3), [4](https://arxiv.org/html/2602.21869v1#bib.bib4), [5](https://arxiv.org/html/2602.21869v1#bib.bib5), [6](https://arxiv.org/html/2602.21869v1#bib.bib6), [7](https://arxiv.org/html/2602.21869v1#bib.bib7), [8](https://arxiv.org/html/2602.21869v1#bib.bib8)].

Any dynamical process is strongly affected by the topology of the underlying network; still, data restrictions may prevent it from being fully accessible - in many empirical settings, one can access only aggregate node-level quantities. The inference problem we address here consists in turning the available information into a probability distribution over the unknown network portion, so as to quantify the plausibility of each link.

This inference problem can be addressed by constructing an ensemble of randomized configurations, defined by a set of properties whose value matches the empirical one but whose topology is random under any other respect: these properties, named *constraints* and indicated as 𝐂\mathbf{C}, represent the available information - i.e. the solely employable one to infer any other (inaccessible) property.

A class of models whose popularity has steadily increased over the years is that of Exponential Random Graphs (ERGs) [[9](https://arxiv.org/html/2602.21869v1#bib.bib9), [10](https://arxiv.org/html/2602.21869v1#bib.bib10), [11](https://arxiv.org/html/2602.21869v1#bib.bib11), [12](https://arxiv.org/html/2602.21869v1#bib.bib12), [13](https://arxiv.org/html/2602.21869v1#bib.bib13), [14](https://arxiv.org/html/2602.21869v1#bib.bib14), [15](https://arxiv.org/html/2602.21869v1#bib.bib15)]. ERGs come from constrained Shannon entropy maximization [[16](https://arxiv.org/html/2602.21869v1#bib.bib16), [9](https://arxiv.org/html/2602.21869v1#bib.bib9), [11](https://arxiv.org/html/2602.21869v1#bib.bib11), [17](https://arxiv.org/html/2602.21869v1#bib.bib17)] and belong to the category of canonical approaches, being induced by constraints whose enforced value is required to be matched only on average.

So far, the parameters defining ERGs have been determined by employing the traditional maximum-of-the-likelihood estimation procedure [[18](https://arxiv.org/html/2602.21869v1#bib.bib18), [19](https://arxiv.org/html/2602.21869v1#bib.bib19), [20](https://arxiv.org/html/2602.21869v1#bib.bib20)], a choice dictated by the particularly simple request induced by applying the latter to ERGs: in symbols, ⟨𝐂⟩=𝐂∗\langle\mathbf{C}\rangle=\mathbf{C}^{\*}, with ⟨𝐂⟩\langle\mathbf{C}\rangle indicating the ensemble average of the constraints and 𝐂∗\mathbf{C}^{\*} their empirical value.

Coming to the purpose of reconstructing a graph topology, one of the most effective models is the Undirected Binary Configuration Model (UBCM) [[9](https://arxiv.org/html/2602.21869v1#bib.bib9), [11](https://arxiv.org/html/2602.21869v1#bib.bib11), [12](https://arxiv.org/html/2602.21869v1#bib.bib12), [13](https://arxiv.org/html/2602.21869v1#bib.bib13), [15](https://arxiv.org/html/2602.21869v1#bib.bib15)], induced by the degree sequence {ki}i=1N\{k\_{i}\}\_{i=1}^{N}, with ki=∑j(≠i)ai​jk\_{i}=\sum\_{j(\neq i)}a\_{ij} indicating the number of neighbors of node ii, ai​ja\_{ij} indicating the entry (i,j)(i,j) of the adjacency matrix 𝐀\mathbf{A} of a binary undirected network and NN indicating the total number of nodes. More formally, the UBCM assigns 𝐀\mathbf{A} the factorized probability distribution reading

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀|𝐱)=∏i=1N∏j(>i)pi​jai​j​(1−pi​j)1−ai​j,P(\mathbf{A}|\mathbf{x})=\prod\_{i=1}^{N}\prod\_{j(>i)}p\_{ij}^{a\_{ij}}(1-p\_{ij})^{1-a\_{ij}}, |  | (1) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​j=xi​xj1+xi​xjp\_{ij}=\frac{x\_{i}x\_{j}}{1+x\_{i}x\_{j}} |  | (2) |

and xix\_{i} indicates the Lagrange multiplier associated with kik\_{i}; maximizing the log-likelihood of such a model implies solving the system of equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ki⟩=∑j(≠i)pi​j=ki∗,∀i\langle k\_{i}\rangle=\sum\_{j(\neq i)}p\_{ij}=k\_{i}^{\*},\>\forall\>i |  | (3) |

that, in turn, induces the vector of point-wise estimates hereby indicated with {xi∗}i=1N\{x\_{i}^{\*}\}\_{i=1}^{N}.

### Link prediction as an instance of network reconstruction

Link prediction is an active research line within the broader field of network science. Close in scope to network reconstruction [[21](https://arxiv.org/html/2602.21869v1#bib.bib21)], link prediction targets specific connections, aiming to uncover missing ones and predict those most likely to emerge in the future [[22](https://arxiv.org/html/2602.21869v1#bib.bib22), [23](https://arxiv.org/html/2602.21869v1#bib.bib23), [24](https://arxiv.org/html/2602.21869v1#bib.bib24)]. Such an issue is relevant in many research areas, such as those concerning socio-economic and financial networks: knowing the structure of the commercial partnerships between firms or of the financial exchanges between banks is, in fact, relevant for a number of reasons, such as quantifying the risk associated with the propagation of a shock [[25](https://arxiv.org/html/2602.21869v1#bib.bib25), [26](https://arxiv.org/html/2602.21869v1#bib.bib26), [27](https://arxiv.org/html/2602.21869v1#bib.bib27)]. Link prediction algorithms rank unconnected node pairs on the basis of a *score*: while some methods rely on purely structural information, others admit external information as well.

The simplest framework to carry out link prediction includes the so-called *similarity-based* algorithms: scores, here, are induced by some measure of similarity between nodes; to this aim, *local*, *quasi-local* or *global* information - such as the degree, the degree of common neighbours or the length of paths connecting any two nodes - has been employed [[22](https://arxiv.org/html/2602.21869v1#bib.bib22), [23](https://arxiv.org/html/2602.21869v1#bib.bib23), [24](https://arxiv.org/html/2602.21869v1#bib.bib24)].

A more refined framework includes machine learning approaches [[22](https://arxiv.org/html/2602.21869v1#bib.bib22), [23](https://arxiv.org/html/2602.21869v1#bib.bib23), [24](https://arxiv.org/html/2602.21869v1#bib.bib24)]: specifying a model, here, amounts to learning a function that determines the probability for nodes ii and jj to be connected while taking as inputs two vectors 𝐟i\mathbf{f}\_{i} and 𝐟j\mathbf{f}\_{j} of (structural and/or external) node-specific features and a vector 𝐠i​j\mathbf{g}\_{ij} of (structural or external) edge-specific features.

A third alternative is represented by the so-called *likelihood-based* algorithms, defined by a likelihood function whose maximization provides the probability that any two nodes are connected - to be interpreted as a score for the link existence: this is achieved precisely by assuming that a certain amount of information is accessible, hence treating it as a constraint to account for [[22](https://arxiv.org/html/2602.21869v1#bib.bib22), [23](https://arxiv.org/html/2602.21869v1#bib.bib23), [24](https://arxiv.org/html/2602.21869v1#bib.bib24)]. Such a perspective justifies the interpretation of the link prediction problem as an instance of the network reconstruction one - although network reconstruction usually deals with less information to predict more aggregate properties.

## RESULTS

Let us explicitly notice that the inference scheme we have sketched above has been designed to carry out network reconstruction in an *in-sample* fashion: in other words, the set of probability coefficients {pi​j}i,j=1N\{p\_{ij}\}\_{i,j=1}^{N} is estimated from (the available information concerning) 𝐀∗\mathbf{A}^{\*} to make statements about 𝐀∗\mathbf{A}^{\*} itself. To the best of our knowledge, a genuinely *out-of-sample* formulation of the entropy-based framework for network reconstruction is still missing: the derivation of ERGs, in fact, offers no prescription to propagate the uncertainty affecting a parameter estimation from one snapshot to another, nor to turn past observations into an informative prior about future ones.

### Towards a Bayesian approach

To carry out an out-of-sample network reconstruction, let us, then, move towards a different design, trying to turn the UBCM into a Bayesian model. Bayes’ theorem provides the key relation P​(𝐱|𝐀)​P​(𝐀)=P​(𝐀,𝐱)=P​(𝐀|𝐱)​π​(𝐱)P(\mathbf{x}|\mathbf{A})P(\mathbf{A})=P(\mathbf{A},\mathbf{x})=P(\mathbf{A}|\mathbf{x})\pi(\mathbf{x}) which, in turn, induces the following definition of *posterior distribution*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐱|𝐀)=P​(𝐀|𝐱)​π​(𝐱)P​(𝐀)=P​(𝐀|𝐱)​π​(𝐱)∫P​(𝐀|𝐱)​π​(𝐱)​𝑑𝐱;P(\mathbf{x}|\mathbf{A})=\frac{P(\mathbf{A}|\mathbf{x})\pi(\mathbf{x})}{P(\mathbf{A})}=\frac{P(\mathbf{A}|\mathbf{x})\pi(\mathbf{x})}{\int P(\mathbf{A}|\mathbf{x})\pi(\mathbf{x})d\mathbf{x}}; |  | (4) |

adapting the parameter estimation procedure accordingly would amount to calculating either the *mean* or the *mode* of the posterior distribution, respectively defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝐱|𝐀⟩=∫𝐱​P​(𝐱|𝐀)​𝑑𝐱\langle\mathbf{x}|\mathbf{A}\rangle=\int\mathbf{x}P(\mathbf{x}|\mathbf{A})d\mathbf{x} |  | (5) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱^MAP=arg​max𝐱⁡{P​(𝐱|𝐀)},\hat{\mathbf{x}}\_{\text{MAP}}=\operatorname\*{arg\,max}\_{\mathbf{x}}\{P(\mathbf{x}|\mathbf{A})\}, |  | (6) |

the acronym standing for *maximum-a-posteriori*. Both procedures, however, provide a point-wise estimate solely depending on the observation made at time tt. A better suited instrument seems to be the so-called *posterior predictive distribution* [[28](https://arxiv.org/html/2602.21869v1#bib.bib28)]. Upon calling 𝐀t\mathbf{A}\_{t} the adjacency matrix representing our graph at time tt and 𝐀t+1\mathbf{A}\_{t+1} the adjacency matrix representing our graph at time t+1t+1, it reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)\displaystyle P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) | =∫P​(𝐀t+1,𝐱|𝐀t)​𝑑𝐱\displaystyle=\int P(\mathbf{A}\_{t+1},\mathbf{x}|\mathbf{A}\_{t})d\mathbf{x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫P​(𝐀t+1|𝐱,𝐀t)​P​(𝐱|𝐀t)​𝑑𝐱\displaystyle=\int P(\mathbf{A}\_{t+1}|\mathbf{x},\mathbf{A}\_{t})P(\mathbf{x}|\mathbf{A}\_{t})d\mathbf{x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫P​(𝐀t+1|𝐱)​P​(𝐱|𝐀t)​𝑑𝐱\displaystyle=\int P(\mathbf{A}\_{t+1}|\mathbf{x})P(\mathbf{x}|\mathbf{A}\_{t})d\mathbf{x} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫P​(𝐀t+1|𝐱)​P​(𝐀t|𝐱)​π​(𝐱)P​(𝐀t)​𝑑𝐱,\displaystyle=\int\frac{P(\mathbf{A}\_{t+1}|\mathbf{x})P(\mathbf{A}\_{t}|\mathbf{x})\pi(\mathbf{x})}{P(\mathbf{A}\_{t})}d\mathbf{x}, |  | (7) |

where the chain rule f​(x,y|z)=f​(x|y,z)​f​(y|z)f(x,y|z)=f(x|y,z)f(y|z) has been employed at the second passage and conditional independence has been assumed at the third passage.

The multivariate nature of the formula above, however, makes its resolution cumbersome; moreover, the UBCM is not a viable reconstruction model, as its calibration requires the knowledge of the entire degree sequence per snapshot - a requirement that is hardly satisfied in a realistic scenario. For such a reason, let us look for a simpler, single-parameter model. Our choice, then, turns eq. [Towards a Bayesian approach](https://arxiv.org/html/2602.21869v1#Sx2.Ex1 "Towards a Bayesian approach ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") into

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)\displaystyle P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) | =∫0+∞P​(𝐀t+1|z)​P​(𝐀t|z)​π​(z)P​(𝐀t)​𝑑z,\displaystyle=\int\_{0}^{+\infty}\frac{P(\mathbf{A}\_{t+1}|z)P(\mathbf{A}\_{t}|z)\pi(z)}{P(\mathbf{A}\_{t})}dz, |  | (8) |

where P​(𝐀t)=∫0+∞P​(𝐀t|z)​π​(z)​𝑑zP(\mathbf{A}\_{t})=\int\_{0}^{+\infty}P(\mathbf{A}\_{t}|z)\pi(z)dz. Let us stress that assuming conditional independence simplifies the computation of the formula above, as the dependence of the future snapshot on the past snapshot is established only via zz; moreover, nothing prevents us from considering a varying number of nodes, i.e. NtN\_{t} and Nt+1N\_{t+1} can differ.

Since zz is integrated out, we are left with a probability depending on 𝐀t\mathbf{A}\_{t}, that we know, and on 𝐀t+1\mathbf{A}\_{t+1}, that we want to infer; the problem can be simplified even more upon considering that the marginal (i.e. edge-specific) probability reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | qi​jt+1\displaystyle q\_{ij}^{t+1} | =P​(ai​jt+1=1|𝐀t)=∫0+∞pi​jt+1​(z)​P​(𝐀t|z)​π​(z)P​(𝐀t)​𝑑z,\displaystyle=P(a\_{ij}^{t+1}=1|\mathbf{A}\_{t})=\int\_{0}^{+\infty}p\_{ij}^{t+1}(z)\frac{P(\mathbf{A}\_{t}|z)\pi(z)}{P(\mathbf{A}\_{t})}dz, |  | (9) |

where pi​jt+1p\_{ij}^{t+1} is the probability that the corresponding entry of 𝐀t+1\mathbf{A}\_{t+1}, i.e. ai​jt+1a\_{ij}^{t+1}, is 11 (see also Appendix [A](https://arxiv.org/html/2602.21869v1#AppA "More on the posterior predictive distribution ‣ APPENDIX A. More on the posterior predictive distribution ‣ A Bayesian approach to out-of-sample network reconstruction")).

Such an expression offers us a viable way to carry out our inference exercise, since it allows the following quantities to be evaluated analytically, i.e. the (expected) total number of links, reading

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Lt+1⟩=∑i=1N∑j(>i)qi​jt+1,\langle L\_{t+1}\rangle=\sum\_{i=1}^{N}\sum\_{j(>i)}q\_{ij}^{t+1}, |  | (10) |

the (expected) degree of each node, reading

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨kit+1⟩=∑j(>i)qi​jt+1,∀i\langle k\_{i}^{t+1}\rangle=\sum\_{j(>i)}q\_{ij}^{t+1},\quad\forall\>i |  | (11) |

and the entries of the so-called *confusion matrix*, i.e.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨TPt+1⟩\displaystyle\langle\text{TP}\_{t+1}\rangle | =∑i=1N∑j(>i)ai​jt+1​qi​jt+1,\displaystyle=\sum\_{i=1}^{N}\sum\_{j(>i)}a\_{ij}^{t+1}q\_{ij}^{t+1}, |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨FPt+1⟩\displaystyle\langle\text{FP}\_{t+1}\rangle | =∑i=1N∑j(>i)(1−ai​jt+1)​qi​jt+1,\displaystyle=\sum\_{i=1}^{N}\sum\_{j(>i)}(1-a\_{ij}^{t+1})q\_{ij}^{t+1}, |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨TNt+1⟩\displaystyle\langle\text{TN}\_{t+1}\rangle | =∑i=1N∑j(>i)(1−ai​jt+1)​(1−qi​jt+1),\displaystyle=\sum\_{i=1}^{N}\sum\_{j(>i)}(1-a\_{ij}^{t+1})(1-q\_{ij}^{t+1}), |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨FNt+1⟩\displaystyle\langle\text{FN}\_{t+1}\rangle | =∑i=1N∑j(>i)ai​jt+1​(1−qi​jt+1);\displaystyle=\sum\_{i=1}^{N}\sum\_{j(>i)}a\_{ij}^{t+1}(1-q\_{ij}^{t+1}); |  | (15) |

in words, ⟨TPt+1⟩\langle\text{TP}\_{t+1}\rangle represents the (expected) number of true positives, i.e. the number of correctly recovered connections; ⟨FPt+1⟩\langle\text{FP}\_{t+1}\rangle represents the (expected) number of false positives, i.e. the number of incorrectly recovered connections; ⟨TNt+1⟩\langle\text{TN}\_{t+1}\rangle represents the (expected) number of true negatives, i.e. the number of correctly recovered missing connections; ⟨FNt+1⟩\langle\text{FN}\_{t+1}\rangle represents the (expected) number of false negatives, i.e. the number of incorrectly recovered missing connections.

### The Bayesian Erdös-Rényi Model (BERM)

Let us, now, instantiate our framework with the Erdös-Rényi Model. Its classical formulation reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀|p)=pL​(𝐀)​(1−p)V−L​(𝐀),P(\mathbf{A}|p)=p^{L(\mathbf{A})}(1-p)^{V-L(\mathbf{A})}, |  | (16) |

where V=N​(N−1)/2V=N(N-1)/2 indicates the total number of pairs of nodes. Fully determining it, however, requires the *prior distribution* to be specified: a popular choice is that of considering the *conjugate prior*, introduced to maintain the functional form of the likelihood function. Upon doing so, we are led to expression

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(p|𝐀)\displaystyle P(p|\mathbf{A}) | =P​(𝐀|p)​π​(p)∫01P​(𝐀|p)​π​(p)​𝑑p\displaystyle=\frac{P(\mathbf{A}|p)\pi(p)}{\int\_{0}^{1}P(\mathbf{A}|p)\pi(p)dp} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =pL​(𝐀)+α−1​(1−p)V−L​(𝐀)+β−1B​(L​(𝐀)+α,V−L​(𝐀)+β),\displaystyle=\frac{p^{L(\mathbf{A})+\alpha-1}(1-p)^{V-L(\mathbf{A})+\beta-1}}{\text{B}(L(\mathbf{A})+\alpha,V-L(\mathbf{A})+\beta)}, |  | (17) |

coming from posing

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(p)=pα−1​(1−p)β−1B​(α,β),\displaystyle\pi(p)=\frac{p^{\alpha-1}(1-p)^{\beta-1}}{\text{B}(\alpha,\beta)}, |  | (18) |

where B​(α,β)=∫01pα−1​(1−p)β−1​𝑑p\text{B}(\alpha,\beta)=\int\_{0}^{1}p^{\alpha-1}(1-p)^{\beta-1}dp is the Beta function. As a consequence, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Lt+1=k|𝐀t)\displaystyle P(L\_{t+1}=k|\mathbf{A}\_{t}) | =∫01P​(Lt+1=k|p)​P​(p|𝐀t)​𝑑p\displaystyle=\int\_{0}^{1}P(L\_{t+1}=k|p)P(p|\mathbf{A}\_{t})dp |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01(Vt+1k)​pk​(1−p)Vt+1−k​P​(𝐀t|p)​π​(p)P​(𝐀t)​𝑑p\displaystyle=\int\_{0}^{1}\binom{V\_{t+1}}{k}p^{k}(1-p)^{V\_{t+1}-k}\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =BetaBin​(Vt+1,Lt+α,Vt−Lt+β),\displaystyle=\text{BetaBin}(V\_{t+1},L\_{t}+\alpha,V\_{t}-L\_{t}+\beta), |  | (19) |

where the explicit dependence of the third expression on 𝐀t\mathbf{A}\_{t} has been dropped; in words, the total number of links at time t+1t+1, conditional to the observation of 𝐀t\mathbf{A}\_{t}, obeys a beta-binomial distribution. Since

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨Lt+1|𝐀t⟩\displaystyle\langle L\_{t+1}|\mathbf{A}\_{t}\rangle | =∑k=0Vt+1k​P​(Lt+1=k|𝐀t),\displaystyle=\sum\_{k=0}^{V\_{t+1}}kP(L\_{t+1}=k|\mathbf{A}\_{t}), |  | (20) |

swapping the operations of sum and integration leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Lt+1|𝐀t⟩\displaystyle\langle L\_{t+1}|\mathbf{A}\_{t}\rangle | =∫01∑k=0Vt+1k​P​(Lt+1=k|p)​P​(p|𝐀t)​d​p\displaystyle=\int\_{0}^{1}\sum\_{k=0}^{V\_{t+1}}kP(L\_{t+1}=k|p)P(p|\mathbf{A}\_{t})dp |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Vt+1​∫01p​P​(𝐀t|p)​π​(p)P​(𝐀t)​𝑑p\displaystyle=V\_{t+1}\int\_{0}^{1}p\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp |  | (21) |

and comparing it with eq. [9](https://arxiv.org/html/2602.21869v1#Sx2.E9 "Equation 9 ‣ Towards a Bayesian approach ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") further leads us to recognize that

|  |  |  |  |
| --- | --- | --- | --- |
|  | qt+1\displaystyle q^{t+1} | =∫01p​P​(𝐀t|p)​π​(p)P​(𝐀t)​𝑑p\displaystyle=\int\_{0}^{1}p\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =B​(1+Lt+α,Vt−Lt+β)B​(Lt+α,Vt−Lt+β)\displaystyle=\frac{\text{B}(1+L\_{t}+\alpha,V\_{t}-L\_{t}+\beta)}{\text{B}(L\_{t}+\alpha,V\_{t}-L\_{t}+\beta)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Lt+αVt+α+β\displaystyle=\frac{L\_{t}+\alpha}{V\_{t}+\alpha+\beta} |  | (22) |

(see also Appendix [B](https://arxiv.org/html/2602.21869v1#AppB "The Bayesian Erdös-Rényi Model ‣ APPENDIX B. The Bayesian Erdös-Rényi Model ‣ A Bayesian approach to out-of-sample network reconstruction")).

### The Bayesian Fitness Model (BFM)

The main limitation of the BERM lies in its homogeneity: in other words, all nodes are treated equally. Since different nodes are known to play different roles, according to their structural importance, let us look for a single-parameter model, *heterogeneous in nature.*

A very natural choice is that of considering the variant of the UBCM named density-corrected Gravity Model (dcGM) [[29](https://arxiv.org/html/2602.21869v1#bib.bib29), [30](https://arxiv.org/html/2602.21869v1#bib.bib30), [31](https://arxiv.org/html/2602.21869v1#bib.bib31), [32](https://arxiv.org/html/2602.21869v1#bib.bib32), [33](https://arxiv.org/html/2602.21869v1#bib.bib33), [34](https://arxiv.org/html/2602.21869v1#bib.bib34)], induced by node-specific fitnesses typically identified with the strengths {si}i=1N\{s\_{i}\}\_{i=1}^{N}, where si=∑j(≠i)wi​js\_{i}=\sum\_{j(\neq i)}w\_{ij} and 𝐖\mathbf{W} is the weighted adjacency matrix associated to our graph111For consistency, 𝐀=Θ​(𝐖)\mathbf{A}=\Theta(\mathbf{W}), where Θ​(x)\Theta(x) denotes the Heaviside step function, here defined as Θ​(x)=1\Theta(x)=1 if x>0x>0 and Θ​(x)=0\Theta(x)=0 otherwise, applied element-wise., while solely enforcing (a proxy of) the link density, defined as c=2​L/N​(N−1)=2​∑i=1N∑j(>i)ai​j/N​(N−1)c=2L/N(N-1)=2\sum\_{i=1}^{N}\sum\_{j(>i)}a\_{ij}/N(N-1). More quantitatively, the dcGM is defined by the fitness ansatz xi=z​six\_{i}=\sqrt{z}s\_{i}, turning eq. [2](https://arxiv.org/html/2602.21869v1#Sx1.E2 "Equation 2 ‣ Network reconstruction: a quick overview ‣ INTRODUCTION ‣ A Bayesian approach to out-of-sample network reconstruction") into

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​j=z​si​sj1+z​si​sj;p\_{ij}=\frac{zs\_{i}s\_{j}}{1+zs\_{i}s\_{j}}; |  | (23) |

the only parameter zz is, then, determined by maximizing the log-likelihood ln⁡P​(𝐀|z)=∑i=1N∑j(>i)[ai​j​ln⁡pi​j+(1−ai​j)​ln⁡(1−pi​j)]\ln P(\mathbf{A}|z)=\sum\_{i=1}^{N}\sum\_{j(>i)}[a\_{ij}\ln p\_{ij}+(1-a\_{ij})\ln(1-p\_{ij})], a recipe implying that the only equation to be solved reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨L⟩=∑i=1N∑j(>i)pi​j=∑i=1N∑j(>i)z​si​sj1+z​si​sj=L∗,\langle L\rangle=\sum\_{i=1}^{N}\sum\_{j(>i)}p\_{ij}=\sum\_{i=1}^{N}\sum\_{j(>i)}\frac{zs\_{i}s\_{j}}{1+zs\_{i}s\_{j}}=L^{\*}, |  | (24) |

where L∗L^{\*} and zML∗z^{\*}\_{\text{ML}} respectively indicate the empirical value of the total number of links and the related parameter estimation.

Instantiating the expression in eq. [9](https://arxiv.org/html/2602.21869v1#Sx2.E9 "Equation 9 ‣ Towards a Bayesian approach ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") with the one defining the dcGM leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | qi​jt+1\displaystyle q\_{ij}^{t+1} | =∫0+∞(z​sit+1​sjt+11+z​sit+1​sjt+1)​P​(𝐀t|z)​π​(z)P​(𝐀t)​𝑑z,\displaystyle=\int\_{0}^{+\infty}\left(\frac{zs\_{i}^{t+1}s\_{j}^{t+1}}{1+zs\_{i}^{t+1}s\_{j}^{t+1}}\right)\frac{P(\mathbf{A}\_{t}|z)\pi(z)}{P(\mathbf{A}\_{t})}dz, |  | (25) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀t|z)=∏i=1Nt∏j(>i)(pi​jt)ai​jt​(1−pi​jt)1−ai​jtP(\mathbf{A}\_{t}|z)=\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}(p\_{ij}^{t})^{a\_{ij}^{t}}(1-p\_{ij}^{t})^{1-a\_{ij}^{t}} |  | (26) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​jt=z​sit​sjt1+z​sit​sjt.p\_{ij}^{t}=\frac{zs\_{i}^{t}s\_{j}^{t}}{1+zs\_{i}^{t}s\_{j}^{t}}. |  | (27) |

The rationale that led us to the BFM motivates us to determine π​(z)\pi(z) by adopting the recipe called *empirical prior*: in words, one *i)* estimates zz on each of the snapshots preceding the one under consideration; *ii)* deduces the functional form of π​(z)\pi(z); *iii)* plugs it into the expression of the snapshot to be reconstructed (see also Appendix [C](https://arxiv.org/html/2602.21869v1#AppC "The Bayesian Fitness Model ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction")).

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 1: Top panels: empirical values of the total number of links (red) and node degrees (blue) scattered versus the predicted ones, pooled across the weeks constituting our dataset; the dashed line marks the identity. Middle panels: evolution of the relative error on the total number of links (red) and the average relative error on the nodes degrees (blue), across the weeks constituting our dataset. Bottom panels: evolution of the ⟨TPR⟩\langle\text{TPR}\rangle, the ⟨PPV⟩\langle\text{PPV}\rangle, the ⟨TNR⟩\langle\text{TNR}\rangle and the ⟨ACC⟩\langle\text{ACC}\rangle across the weeks constituting our dataset. The results concerning the BERM are shown on the left while those concerning the BFM are shown on the right: while both models recover the total number of links and achieve a large ⟨ACC⟩\langle\text{ACC}\rangle score, driven by the large value of the ⟨TNR⟩\langle\text{TNR}\rangle, only the BFM is capable of recovering the degree sequence to an acceptable degree of accuracy - as well as more than doubling the other scores.

At this point, one needs to compute qi​jt+1q\_{ij}^{t+1}. A possible choice is that of evaluating the integrand in correspondence of zMAP∗z^{\*}\_{\text{MAP}}, i.e. the value that maximizes the log-posterior ln⁡P​(z|𝐀t)=ln⁡P​(𝐀t|z)+ln⁡π​(z)\ln P(z|\mathbf{A}\_{t})=\ln P(\mathbf{A}\_{t}|z)+\ln\pi(z), a recipe implying that the only equation to be solved reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ln⁡P​(z|𝐀t)∂z=∂ln⁡P​(𝐀t|z)∂z+∂ln⁡π​(z)∂z=0\frac{\partial\ln P(z|\mathbf{A}\_{t})}{\partial z}=\frac{\partial\ln P(\mathbf{A}\_{t}|z)}{\partial z}+\frac{\partial\ln\pi(z)}{\partial z}=0 |  | (28) |

or, more explicitly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1z​[Lt∗−∑i=1Nt∑j(>i)z​sit​sjt1+z​sit​sjt]+∂ln⁡π​(z)∂z=0;\displaystyle\frac{1}{z}\left[L\_{t}^{\*}-\sum\_{i=1}^{N\_{t}}\sum\_{j(>i)}\frac{zs\_{i}^{t}s\_{j}^{t}}{1+zs\_{i}^{t}s\_{j}^{t}}\right]+\frac{\partial\ln\pi(z)}{\partial z}=0; |  | (29) |

although viable, this choice rests upon the assumption that the integrand is peaked around zMAP∗z^{\*}\_{\text{MAP}}; besides, it privileges the likelihood term over the prior - i.e. a system current realization over its history.

To avoid relying on this assumption, and fully account for uncertainty, one is forced to proceed numerically. To this aim, we move to the logarithmic coordinate u=ln⁡zu=\ln z and employ the integration scheme named *Gauss-Hermite quadrature* (see also the Methods section and Appendix [D](https://arxiv.org/html/2602.21869v1#AppD "Numerical integration of the posterior predictive distribution ‣ APPENDIX D. Numerical integration of the posterior predictive distribution ‣ A Bayesian approach to out-of-sample network reconstruction")).

### Out-of-sample network reconstruction of the eMID dataset

Let us, now, test our recipes on the transaction-level data constituting the overnight segment of the Electronic Market for Interbank Deposits (eMID), a screen-based market for unsecured deposits [[35](https://arxiv.org/html/2602.21869v1#bib.bib35), [8](https://arxiv.org/html/2602.21869v1#bib.bib8), [36](https://arxiv.org/html/2602.21869v1#bib.bib36), [37](https://arxiv.org/html/2602.21869v1#bib.bib37)]. Starting from directed, weighted trades (lender, borrower, notional amount), we aggregate transactions within ISO weeks, symmetrize exposures, and then binarize them to obtain weekly undirected snapshots (see also Appendix [E](https://arxiv.org/html/2602.21869v1#AppE "DATA DESCRIPTION ‣ APPENDIX E. DATA DESCRIPTION ‣ A Bayesian approach to out-of-sample network reconstruction")).

The performance of our Bayesian ERGs has been tested on the following properties: the *total number of links*, by comparing

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt+1=∑i=1N∑j(>i)ai​jt+1L\_{t+1}=\sum\_{i=1}^{N}\sum\_{j(>i)}a\_{ij}^{t+1} |  | (30) |

with ⟨Lt+1⟩\langle L\_{t+1}\rangle; the *degree of each node*, by comparing

|  |  |  |  |
| --- | --- | --- | --- |
|  | kit+1=∑j(>i)ai​jt+1,∀ik\_{i}^{t+1}=\sum\_{j(>i)}a\_{ij}^{t+1},\quad\>\forall\>i |  | (31) |

with ⟨kit+1⟩\langle k\_{i}^{t+1}\rangle, ∀i\forall\>i; the *true positive rate* (also known as *recall* or *sensitivity*)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨TPRt+1⟩=⟨TPt+1⟩Lt+1,\langle\text{TPR}\_{t+1}\rangle=\frac{\langle\text{TP}\_{t+1}\rangle}{L\_{t+1}}, |  | (32) |

the *positive predictive value* (also known as *precision*)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨PPVt+1⟩=⟨TPt+1⟩⟨Lt+1⟩,\langle\text{PPV}\_{t+1}\rangle=\frac{\langle\text{TP}\_{t+1}\rangle}{\langle L\_{t+1}\rangle}, |  | (33) |

the *true negative rate* (also known as *specificity*)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨TNRt+1⟩=⟨TNt+1⟩Vt+1−Lt+1\langle\text{TNR}\_{t+1}\rangle=\frac{\langle\text{TN}\_{t+1}\rangle}{V\_{t+1}-L\_{t+1}} |  | (34) |

and the *accuracy*

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ACCt+1⟩=⟨TPt+1⟩+⟨TNt+1⟩Vt+1,\langle\text{ACC}\_{t+1}\rangle=\frac{\langle\text{TP}\_{t+1}\rangle+\langle\text{TN}\_{t+1}\rangle}{V\_{t+1}}, |  | (35) |

quantifying the ability of an algorithm in capturing both the number of true positives and the number of true negatives. We have also approached the problem of reconstructing a network at time t+1t+1, on the basis of the information at time tt, from the perspective of link prediction222Although the related problem of spurious links detection can be approached as well within the same framework, we have ignored it, here.: to this aim, we have considered the top ⟨Lt+1⟩\langle L\_{t+1}\rangle links, i.e. the links characterized by the ⟨Lt+1⟩\langle L\_{t+1}\rangle largest probability coefficients, and checked their position via the *Jaccard Index*, reading

|  |  |  |  |
| --- | --- | --- | --- |
|  | JIt+1=|Et+1pred∩Et+1true||Et+1pred∪Et+1true|,\text{JI}\_{t+1}=\frac{\lvert E^{\text{pred}}\_{t+1}\cap E^{\text{true}}\_{t+1}\rvert}{\lvert E^{\text{pred}}\_{t+1}\cup E^{\text{true}}\_{t+1}\rvert}, |  | (36) |

where EtrueE^{\mathrm{true}} is the ground-truth edge set, with |Etrue|=Lt+1\lvert E^{\mathrm{true}}\rvert=L\_{t+1}. We have also considered the Area Under the Receiver Operating Curve (AUROC), defined as the area under the curve obtained upon scattering the index333Notice that such an index is nothing but the deterministic version of the one defined in eq. [32](https://arxiv.org/html/2602.21869v1#Sx2.E32 "Equation 32 ‣ Out-of-sample network reconstruction of the eMID dataset ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction").

|  |  |  |  |
| --- | --- | --- | --- |
|  | TPRt+1=|Et+1pred∩Et+1true||Et+1true|\text{TPR}\_{t+1}=\frac{\lvert E^{\text{pred}}\_{t+1}\cap E^{\text{true}}\_{t+1}\rvert}{\lvert E^{\text{true}}\_{t+1}\rvert} |  | (37) |

versus the index

|  |  |  |  |
| --- | --- | --- | --- |
|  | FPRt+1=|Et+1pred∩Et+1true¯||Et+1true¯|\text{FPR}\_{t+1}=\frac{\lvert E^{\text{pred}}\_{t+1}\cap\overline{E^{\text{true}}\_{t+1}}\rvert}{\lvert\overline{E^{\text{true}}\_{t+1}}\rvert} |  | (38) |

(where Et+1true¯\overline{E^{\text{true}}\_{t+1}} is the complementary set of Et+1trueE^{\text{true}}\_{t+1}, with |Et+1true¯|=Vt+1−Lt+1\lvert\overline{E^{\text{true}}\_{t+1}}\rvert=V\_{t+1}-L\_{t+1}), as the list of links ranked in decreasing order of the chosen score is gone through: the AUROC quantifies the extent to which a given link prediction algorithm performs better than a random one - i.e. one that flips a coin to classify each non-observed link as either non-existent or missing.

As a first analysis, we have considered the entire dataset, spanning the years 19991999–20122012, at the weekly time scale: the first three years have been used for the initial calibration of the prior; from 20022002 on, we have performed the analysis over the remaining years, letting the prior be updated over a rolling window of three years. As all banks observed at each date are retained, here we have worked with an ‘unbalanced’ panel of nodes - i.e. their number is allowed to vary from snapshot to snapshot. For what concerns the BERM, the empirical prior on p∗p^{\*}, across the initial calibration window, is well described by a beta distribution whose parameters read α≃58.261\alpha\simeq 58.261 and β≃541.543\beta\simeq 541.543 (see fig. [B.2](https://arxiv.org/html/2602.21869v1#Ax2.F2 "Figure B.2 ‣ APPENDIX B. The Bayesian Erdös-Rényi Model ‣ A Bayesian approach to out-of-sample network reconstruction")). For what concerns the BFM, instead, the distribution of the z∗z^{\*} values across the same calibration window is well described by the Gamma distribution π​(z)=zκ−1​e−z/θ/Γ​(κ)​θκ\pi(z)=z^{\kappa-1}e^{-z/\theta}/\Gamma(\kappa)\theta^{\kappa} whose parameters read κ≃27.538\kappa\simeq 27.538 and θ≃0.007\theta\simeq 0.007 - and the Kolmogorov-Smirnov test [[38](https://arxiv.org/html/2602.21869v1#bib.bib38)] confirms it to be the distribution with the smallest number of parameters (only two) not rejected as a plausible parent distribution (see fig. [C.2](https://arxiv.org/html/2602.21869v1#Ax3.F2 "Figure C.2 ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction")). In both cases, the prior is updated by adding each, new, weekly value to it: from this perspective, we register no substantial difference between enriching it with ML or MAP estimates (see also the Methods section).

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 2: Left panel evolution of the TPR, the JI and AUROC across the weeks constituting our dataset. Right panel: ROC curves for all snapshots. The purple one represents the average ROC, obtained by interpolating each snapshot-specific ROC on a common grid of FPR values and averaging the corresponding TPR values. These ranking-based diagnostics are meaningful only for the BFM, inducing a non-trivial ordering of candidate links.

As fig. [1](https://arxiv.org/html/2602.21869v1#Sx2.F1 "Figure 1 ‣ The Bayesian Fitness Model (BFM) ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") shows, both the BERM and the BFM are capable of recovering the total number of links. When coming to the degrees, instead, the BFM recovers their heterogeneity to a substantially better extent: more quantitatively, *i)* the relative error REL=|L−⟨L⟩|/L\text{RE}\_{L}=|L-\langle L\rangle|/L amounts, on average, to ≃0.1\simeq 0.1, under both the BFM and the BERM; *ii)* the average relative error AREk=∑i=1N(|ki−⟨ki⟩|/ki)/N\text{ARE}\_{k}=\sum\_{i=1}^{N}(|k\_{i}-\langle k\_{i}\rangle|/k\_{i})/N is smaller under the BFM than under the BERM.

Although both models achieve a large ACC, amounting, on average, to ≃0.80\simeq 0.80, the BFM doubles the other scores, intended to quantify the ability of a model in recovering the position of connections - and not just that of the missing ones; the explanation of such a result lies in the evidence that the BERM cannot predict too dense configurations, although it is not capable of treating different pairs of nodes in a different way. Figure [2](https://arxiv.org/html/2602.21869v1#Sx2.F2 "Figure 2 ‣ Out-of-sample network reconstruction of the eMID dataset ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") further refines the picture above, by plotting the TPR, the JI and the AUROC for the BFM: while the TPR amounts, on average, to ≃0.40\simeq 0.40, the JI amounts, on average, to ≃0.20\simeq 0.20 - but it should be noticed that the TPR of the Bayesian Fitness Model is twice the one achieved in [[39](https://arxiv.org/html/2602.21869v1#bib.bib39)] by the Directed Binary Configuration Model, implemented to carry out the in-sample version of the same exercise, on the same dataset. We explicitly stress that these ranking-based diagnostics are meaningful only for the BFM, whose heterogeneous set of probability coefficients induces a non-trivial ordering of the candidate links; the BERM, instead, would assign the same score to each pair, therefore inducing a ‘random’ classification.

A simpler version of our analysis (carried out by considering a ‘balanced’ panel of 7373 banks across the weeks of 20022002 - i.e. retaining only the nodes that appear in all snapshots of both the calibration and test period) is described in Appendix [B](https://arxiv.org/html/2602.21869v1#AppB "The Bayesian Erdös-Rényi Model ‣ APPENDIX B. The Bayesian Erdös-Rényi Model ‣ A Bayesian approach to out-of-sample network reconstruction") and Appendix [C](https://arxiv.org/html/2602.21869v1#AppC "The Bayesian Fitness Model ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction").

### Self-sustained inference of the eMID dataset

The previous exercise was carried out by employing 𝐀0\mathbf{A}\_{0} (where t=0t=0 indicates the last week of 20012001) to predict 𝐀1\mathbf{A}\_{1}, 𝐀1\mathbf{A}\_{1} to predict 𝐀2\mathbf{A}\_{2} and so on. Let us, now, test the capability of our inference procedure to *self-sustain* itself, i.e. to operate recursively without accessing any other adjacency matrix beyond the one employed for initialization. In this regime, both the prior on the parameter and the network representation are updated in a fully Bayesian fashion: the empirical prior keeps rolling over a three-year window but each new parameter value is estimated from inferred quantities and the matrix 𝐐t\mathbf{Q}\_{t} replaces 𝐀t\mathbf{A}\_{t} in the predictive step.

More specifically, we still consider the entire dataset by letting the prior roll over a time window of three years but *i)* determine each, new, weekly value of the parameter by solving eq. [29](https://arxiv.org/html/2602.21869v1#Sx2.E29 "Equation 29 ‣ The Bayesian Fitness Model (BFM) ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") where Lt∗L\_{t}^{\*} is replaced by ⟨Lt⟩\langle L\_{t}\rangle, i.e. an estimate itself; *ii)* substitute the generic coefficient qi​jt+1q\_{ij}^{t+1} with the expression

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 3: Left panel: values of the Kullback-Leibler divergence between 𝐀\mathbf{A} and its ensemble average 𝐐\mathbf{Q} scattered versus the values of the Kullback-Leibler divergence between 𝐀\mathbf{A} and its ‘self-sustained’ inferred version 𝐑\mathbf{R}, pooled across the weeks constituting our dataset. Right panel: values of the total number of links (red) and node degrees (blue) predicted by employing 𝐐\mathbf{Q} scattered versus the values predicted by employing 𝐑\mathbf{R}, pooled across the weeks constituting our dataset. Both plots confirm that 𝐐\mathbf{Q} represents a reliable surrogate of 𝐀\mathbf{A} - in fact, so accurate to constitute a valid prior for subsequent inference.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri​jt+1=∫0+∞(z​sit+1​sjt+11+z​sit+1​sjt+1)​P​(𝐐t|z)​π​(z)P​(𝐐t)​𝑑z,r\_{ij}^{t+1}=\int\_{0}^{+\infty}\left(\frac{zs\_{i}^{t+1}s\_{j}^{t+1}}{1+zs\_{i}^{t+1}s\_{j}^{t+1}}\right)\frac{P(\mathbf{Q}\_{t}|z)\pi(z)}{P(\mathbf{Q}\_{t})}dz, |  | (39) |

where 𝐀t\mathbf{A}\_{t} is replaced by 𝐐t\mathbf{Q}\_{t}, again an estimate itself: stated otherwise, we employ 𝐀0\mathbf{A}\_{0} to predict 𝐐1\mathbf{Q}\_{1}, 𝐐1\mathbf{Q}\_{1} to predict 𝐐2\mathbf{Q}\_{2} and so on.

As fig. [3](https://arxiv.org/html/2602.21869v1#Sx2.F3 "Figure 3 ‣ Self-sustained inference of the eMID dataset ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") shows, such a ‘self-sustained’ inference highlights patterns that are very similar to those in fig. [1](https://arxiv.org/html/2602.21869v1#Sx2.F1 "Figure 1 ‣ The Bayesian Fitness Model (BFM) ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction"), an evidence revealing the accuracy of our algorithm to carry out an out-of-sample network reconstruction in presence of very little information (see also Appendix [F](https://arxiv.org/html/2602.21869v1#AppF "Marginal probability induced by the estimated prior ‣ APPENDIX F. Marginal probability induced by the estimated prior ‣ A Bayesian approach to out-of-sample network reconstruction")). To provide a more quantitative assessment of such an agreement, let us scatter the values of the Kullback-Leibler divergence between the adjacency matrix 𝐀\mathbf{A} and its ensemble average 𝐐={qi​j}\mathbf{Q}=\{q\_{ij}\} at time tt, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL(𝐀t||𝐐t)=∑i=1N∑j(>i)ai​jtln(ai​jtqi​jt),D\_{\text{KL}}(\mathbf{A}\_{t}||\mathbf{Q}\_{t})=\sum\_{i=1}^{N}\sum\_{j(>i)}a\_{ij}^{t}\ln\left(\frac{a\_{ij}^{t}}{q\_{ij}^{t}}\right), |  | (40) |

versus the values of the Kullback-Leibler divergence between the adjacency matrix 𝐀\mathbf{A} and its ‘self-sustained’, inferred version 𝐑={ri​j}\mathbf{R}=\{r\_{ij}\} at time tt, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL(𝐀t||𝐑t)=∑i=1N∑j(>i)ai​jtln(ai​jtri​jt);D\_{\text{KL}}(\mathbf{A}\_{t}||\mathbf{R}\_{t})=\sum\_{i=1}^{N}\sum\_{j(>i)}a\_{ij}^{t}\ln\left(\frac{a\_{ij}^{t}}{r\_{ij}^{t}}\right); |  | (41) |

as evident from the figure, the two series of weekly values closely resemble each other. An even more explicit representation of such an agreement is provided in fig. [4](https://arxiv.org/html/2602.21869v1#Sx2.F4 "Figure 4 ‣ Self-sustained inference of the eMID dataset ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction"), depicting the empirical adjacency matrix of the week #​20\#20 of the year 20072007, its ensemble average 𝐐\mathbf{Q} and its ‘self-sustained’ inferred version 𝐑\mathbf{R}.

![Refer to caption](x11.png)

![Refer to caption](x12.png)

![Refer to caption](x13.png)

Figure 4: Left panel: empirical adjacency matrix 𝐀t+1\mathbf{A}\_{t+1} corresponding to the week #​20\#20 of the year 20072007. Middle panel: ensemble average of 𝐀t+1\mathbf{A}\_{t+1}, i.e. 𝐐t+1\mathbf{Q}\_{t+1}. Right panel: ‘self-sustained’, inferred version of 𝐀t+1\mathbf{A}\_{t+1}, i.e. 𝐑t+1\mathbf{R}\_{t+1}. While 𝐐t+1\mathbf{Q}\_{t+1} needs the information provided by 𝐀t\mathbf{A}\_{t}, 𝐑t+1\mathbf{R}\_{t+1} ‘only’ needs the information provided by 𝐐t\mathbf{Q}\_{t}, i.e. an estimate of 𝐀t\mathbf{A}\_{t}. More quantitatively, 2​∑i=1N∑j(>i)|qi​j−ri​j|/N​(N−1)≃0.0062\sum\_{i=1}^{N}\sum\_{j(>i)}|q\_{ij}-r\_{ij}|/N(N-1)\simeq 0.006 and 2​∑i=1N∑j(>i)|ai​j−qi​j|/N​(N−1)≃0.152≃2​∑i=1N∑j(>i)|ai​j−ri​j|/N​(N−1)2\sum\_{i=1}^{N}\sum\_{j(>i)}|a\_{ij}-q\_{ij}|/N(N-1)\simeq 0.152\simeq 2\sum\_{i=1}^{N}\sum\_{j(>i)}|a\_{ij}-r\_{ij}|/N(N-1).

### Out-of-sample versus in-sample reconstruction

A particularly stringent test of our predictive scheme is obtained by contrasting it with an in-sample reconstruction that is allowed to use the quantity that our method must, instead, infer. More specifically, we compare the set of ri​jr\_{ij}s with the set of probability coefficients returned by the dcGM, calibrated by employing the information about the total number of links per (weekly) snapshot. Despite the ‘informational advantage’ of the dcGM, the predictive performances of the two models remain remarkably close: as fig. [5](https://arxiv.org/html/2602.21869v1#Sx3.F5 "Figure 5 ‣ DISCUSSION ‣ A Bayesian approach to out-of-sample network reconstruction") shows, upon averaging over 561561 weekly snapshots we obtain TPR¯Bayes=0.2498\overline{\text{TPR}}\_{\text{Bayes}}=0.2498 versus TPR¯dcGM=0.2494\overline{\text{TPR}}\_{\text{dcGM}}=0.2494, with the Bayesian predictor outperforming the dcGM on the ≃54%\simeq 54\% of snapshots. For what concerns the remaining scores, we have PPV¯Bayes=0.2495\overline{\text{PPV}}\_{\text{Bayes}}=0.2495 versus PPV¯dcGM=0.2494\overline{\text{PPV}}\_{\text{dcGM}}=0.2494, TNR¯Bayes=0.9124\overline{\text{TNR}}\_{\text{Bayes}}=0.9124 versus TNR¯dcGM=0.9122\overline{\text{TNR}}\_{\text{dcGM}}=0.9122 and ACC¯Bayes=0.8429\overline{\text{ACC}}\_{\text{Bayes}}=0.8429 versus ACC¯dcGM=0.8432\overline{\text{ACC}}\_{\text{dcGM}}=0.8432; degree-level errors, instead, remain slightly smaller for the dcGM, with ARE¯kBayes=0.8999\overline{\text{ARE}}\_{k}^{\text{Bayes}}=0.8999 versus ARE¯kdcGM=0.8624\overline{\text{ARE}}\_{k}^{\text{dcGM}}=0.8624 and MREkBayes=14.6836\text{MRE}\_{k}^{\text{Bayes}}=14.6836 versus MREkdcGM=14.6267\text{MRE}\_{k}^{\text{dcGM}}=14.6267, although the Bayesian predictor is still better for a non-negligible fraction of weeks, i.e. on the ≃46%\simeq 46\% of the snapshots.

## DISCUSSION

In the economic and financial domain, reconstruction methods based on Shannon entropy maximization have been widely studied from a frequentist perspective [[21](https://arxiv.org/html/2602.21869v1#bib.bib21), [15](https://arxiv.org/html/2602.21869v1#bib.bib15), [34](https://arxiv.org/html/2602.21869v1#bib.bib34)]. Within such a framework, fitness-based models provide a powerful approach to reconstructing the structure of complex networks from partial information: among them, the dcGM offers a minimal, yet effective, parametrization for estimating link probabilities that combines node-level attributes with a global parameter.

The dcGM accurately captures many structural features of real-world networks but relies on a point-wise, maximum-of-the-likelihood estimation procedure that offers no principled way to incorporate temporal dependencies: in other words, the dcGM can be employed to carry out an *in-sample* network reconstruction.

Building on the approach developed in [[40](https://arxiv.org/html/2602.21869v1#bib.bib40), [41](https://arxiv.org/html/2602.21869v1#bib.bib41), [42](https://arxiv.org/html/2602.21869v1#bib.bib42)], our contribution addresses the problem of carrying out an *out-of-sample* network reconstruction, by presenting a fully Bayesian framework to infer a network structure from a previous observation. As our tests reveal, our reconstruction procedure ‘self-sustains’ itself, each predicted configuration becoming a reliable prior for inference at the subsequent step. In practice, after the lastly observed snapshot is used, no additional topological information is fed into the algorithm and the reconstruction is propagated forward in time solely through the posterior predictive distribution. Such an experiment probes the information-retention capability of the model: prediction errors are allowed to accumulate, while our procedure attempts to reconstruct future configurations at increasingly large temporal distances from the lastly observed topology. Observing that the model remains accurate under these conditions points out its capability of capturing structural regularities.

![Refer to caption](x14.png)


Figure 5: Metric-specific distribution of the improvement of the ‘self-sustained’ Bayesian predictor with respect to the (in-sample) dcGM. For each snapshot and metric mm, we define the score ImI\_{m} in two different ways, i.e. as Im=(mdcGM−mBayes)/|mdcGM|I\_{m}=(m\_{\text{dcGM}}-m\_{\text{Bayes}})/|m\_{\mathrm{dcGM}}| for the AREk\text{ARE}\_{k} and the MREk\text{MRE}\_{k} and as Im=(mBayes−mdcGM)/|mdcGM|I\_{m}=(m\_{\mathrm{Bayes}}-m\_{\mathrm{dcGM}})/|m\_{\mathrm{dcGM}}| for the ⟨TPR⟩\langle\text{TPR}\rangle, the ⟨PPV⟩\langle\text{PPV}\rangle, the ⟨TNR⟩\langle\text{TNR}\rangle and the ⟨ACC⟩\langle\text{ACC}\rangle: in both cases, values above the 0%0\% dashed line indicate that the Bayesian predictor performs better than the (in-sample) dcGM. Each violin plot summarizes the distribution of the improvement, showing that our fully predictive procedure frequently matches, and sometimes exceeds, the in-sample reconstruction calibrated by taking LL as input at each time step.

## METHODS

### Data preprocessing

We analyze the binary undirected representation of eMID across the years 19991999-20122012: weekly snapshots are built from all transactions settled within ISO weeks; self-loops and multi-edges are discarded. For the unbalanced specification, the empirical prior is calibrated on the years 19991999-20012001 while the out-of-sample analysis is performed across the years 20022002-20122012, retaining all the banks that are active in each week. For the balanced specification, discussed in Appendix [B](https://arxiv.org/html/2602.21869v1#AppB "The Bayesian Erdös-Rényi Model ‣ APPENDIX B. The Bayesian Erdös-Rényi Model ‣ A Bayesian approach to out-of-sample network reconstruction") (BERM) and Appendix [C](https://arxiv.org/html/2602.21869v1#AppC "The Bayesian Fitness Model ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction") (BFM), the empirical prior is calibrated on the years 19991999-20012001 and the node set is restricted to the banks that are active in all weekly snapshots from 19991999 to 20022002; the out-of-sample analysis is, then, performed only over the year 20022002. A complete description of the raw records, weekly aggregation, symmetrization and binarization steps is provided in Appendix [E](https://arxiv.org/html/2602.21869v1#AppE "DATA DESCRIPTION ‣ APPENDIX E. DATA DESCRIPTION ‣ A Bayesian approach to out-of-sample network reconstruction").

### Prior calibration

Within each rolling window of three years, we compute a snapshot-specific point estimate for each parameter and, then, fit the empirical prior on the resulting set of values. Such a set is augmented via the jack-knife procedure, i.e. by removing one trading day at a time from each weekly aggregation and repeating the point-estimation step.

For what concerns the BERM, the ML estimate reads p∗=L∗/V∗p^{\*}=L^{\*}/V^{\*}; for what concerns the BFM, instead, the ML estimate is obtained by solving eq. [24](https://arxiv.org/html/2602.21869v1#Sx2.E24 "Equation 24 ‣ The Bayesian Fitness Model (BFM) ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction"): in practice, we solve the corresponding one-dimensional problem via Newton iterations with backtracking, using a tolerance of 10−810^{-8} and a maximum number of 8080 iterations. The corresponding fits on the initial calibration window are shown in Appendix [B](https://arxiv.org/html/2602.21869v1#AppB "The Bayesian Erdös-Rényi Model ‣ APPENDIX B. The Bayesian Erdös-Rényi Model ‣ A Bayesian approach to out-of-sample network reconstruction") for the BERM and in Appendix [C](https://arxiv.org/html/2602.21869v1#AppC "The Bayesian Fitness Model ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction") for the BFM.

### Evaluation of the posterior predictive distribution

Adopting the Beta distribution as a (conjugate) prior allows us to treat the posterior predictive distribution of the BERM analytically.

For what concerns the BFM, instead, the posterior predictive distribution must be evaluated numerically. To this aim, we pose u=ln⁡zu=\ln z and perform the calculation in such a logarithmic coordinate, which maps the original domain (0,+∞)(0,+\infty) onto ℝ\mathbb{R} and prevents numerical overflow when zz becomes large.

A first integration scheme is the one named *Gauss-Hermite quadrature* [[43](https://arxiv.org/html/2602.21869v1#bib.bib43)]: after having ‘gaussianized’ the integrand and evaluated it in correspondence of the posterior mode, the predictive probability reduces to a weighted sum over KK quadrature nodes; for our experiments, we have used K=25K=25.

An alternative integration scheme is the one named *slice sampling* [[44](https://arxiv.org/html/2602.21869v1#bib.bib44)]: it samples the log-posterior MM times without requiring the computation of the normalization constant and providing an estimator that converges to the true distribution as MM increases; for our experiments, M=3000M=3000 values are sampled after a burn-in phase of 600600 steps, thus yielding the estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​jt+1≃1M​∑m=1Meu(m)​sit+1​sjt+11+eu(m)​sit+1​sjt+1.q\_{ij}^{t+1}\simeq\frac{1}{M}\sum\_{m=1}^{M}\frac{e^{u^{(m)}}s\_{i}^{t+1}s\_{j}^{t+1}}{1+e^{u^{(m)}}s\_{i}^{t+1}s\_{j}^{t+1}}. |  | (42) |

While the snapshot-specific computational cost of the first scheme scales as O​(K​N2)O(KN^{2}), the one of the second scheme scales as O​(M​N2)O(MN^{2}): as the Gauss-Hermite quadrature one is computationally cheaper, it is employed as the default method (see also Appendix [D](https://arxiv.org/html/2602.21869v1#AppD "Numerical integration of the posterior predictive distribution ‣ APPENDIX D. Numerical integration of the posterior predictive distribution ‣ A Bayesian approach to out-of-sample network reconstruction")).

## DATA AVAILABILITY

Raw eMID data are subject to restrictions, hence not publicly available. Researchers can access them upon request.

## CODE AVAILABILITY

The Python package named OR4CLE (Out-of-sample bayesian Reconstruction 4 CompLex nEtworks), implementing the algorithms described in the main text, is available on PyPI and at the URL <https://github.com/mattiamarzi/OR4CLE>.

## References

* Colizza *et al.* [2006]
  V. Colizza, A. Barrat, M. Barthélemy, and A. Vespignani, The role of the airline transportation network in the prediction and predictability of global epidemics, [Proc. Natl. Acad. Sci. U.S.A. 103, 2015 (2006)](https://doi.org/10.1073/pnas.0510525103).
* Barrat *et al.* [2008]
  A. Barrat, M. Barthélemy, and A. Vespignani, *Dynamical Processes on Complex Networks* (Cambridge University Press, Cambridge, 2008).
* Newman [2010]
  M. E. J. Newman, *Networks: An Introduction* (Oxford University Press, Oxford, 2010).
* Pastor-Satorras *et al.* [2015]
  R. Pastor-Satorras, C. Castellano, P. Van Mieghem, and A. Vespignani, Epidemic processes in complex networks, [Rev. Mod. Phys. 87, 925 (2015)](https://doi.org/10.1103/RevModPhys.87.925).
* Squartini *et al.* [2013]
  T. Squartini, I. van Lelyveld, and D. Garlaschelli, Early-warning signals of topological collapse in interbank networks, [Sci. Rep. 3, 3357 (2013)](https://doi.org/10.1038/srep03357).
* Battiston *et al.* [2016]
  S. Battiston, J. D. Farmer, A. Flache, D. Garlaschelli, A. G. Haldane, H. Heesterbeek, C. Hommes, C. Jaeger, R. May, and M. Scheffer, Complexity theory and financial regulation, [Science 351, 818 (2016)](https://doi.org/10.1126/science.aad0299).
* Bardoscia *et al.* [2017]
  M. Bardoscia, S. Battiston, F. Caccioli, and G. Caldarelli, Pathways towards instability in financial networks, [Nat. Commun. 8, 14416 (2017)](https://doi.org/10.1038/ncomms14416).
* Macchiati *et al.* [2025]
  V. Macchiati, E. Marchese, P. Mazzarisi, D. Garlaschelli, and T. Squartini, Spectral signatures of structural change in financial networks, [Chaos, Solit. Fractals 193, 116065 (2025)](https://doi.org/10.1016/j.chaos.2025.116065).
* Park and Newman [2004]
  J. Park and M. E. J. Newman, Statistical mechanics of networks, [Phys. Rev. E 70, 066117 (2004)](https://doi.org/10.1103/PhysRevE.70.066117).
* Bianconi [2009]
  G. Bianconi, Entropy of network ensembles, [Phys. Rev. E 79, 036114 (2009)](https://doi.org/10.1103/PhysRevE.79.036114).
* Squartini and Garlaschelli [2011]
  T. Squartini and D. Garlaschelli, Analytical maximum-likelihood method to detect patterns in real networks, [New J. Phys. 13, 083001 (2011)](https://doi.org/10.1088/1367-2630/13/8/083001).
* Fronczak and Fronczak [2012]
  A. Fronczak and P. Fronczak, Statistical mechanics of the international trade network: Structural correlations and modeling, [Phys. Rev. E 85, 056113 (2012)](https://doi.org/10.1103/PhysRevE.85.056113).
* Squartini *et al.* [2015]
  T. Squartini, R. Mastrandrea, and D. Garlaschelli, Unbiased sampling of network ensembles, [New J. Phys. 17, 023052 (2015)](https://doi.org/10.1088/1367-2630/17/2/023052).
* Saracco *et al.* [2015]
  F. Saracco, R. Di Clemente, A. Gabrielli, and T. Squartini, Randomizing bipartite networks: The case of the world trade web, [Sci. Rep. 5, 10595 (2015)](https://doi.org/10.1038/srep10595).
* Cimini *et al.* [2019]
  G. Cimini, T. Squartini, F. Saracco, D. Garlaschelli, A. Gabrielli, and G. Caldarelli, The statistical physics of real-world networks, [Nat. Rev. Phys. 1, 58 (2019)](https://doi.org/10.1038/s42254-018-0002-6).
* Jaynes [1957]
  E. T. Jaynes, Information theory and statistical mechanics, [Phys. Rev. 106, 620 (1957)](https://doi.org/10.1103/PhysRev.106.620).
* Squartini and Garlaschelli [2017]
  T. Squartini and D. Garlaschelli, [*Maximum-Entropy Networks*](https://doi.org/10.1007/978-3-319-69438-2), SpringerBriefs in Complexity (Springer International Publishing, Cham, 2017).
* Garlaschelli and Loffredo [2008]
  D. Garlaschelli and M. I. Loffredo, Maximum likelihood: Extracting unbiased information from complex networks, [Phys. Rev. E 78, 015101 (2008)](https://doi.org/10.1103/PhysRevE.78.015101).
* Vallarano *et al.* [2021]
  N. Vallarano, M. Bruno, E. Marchese, G. Trapani, F. Saracco, G. Cimini, M. Zanon, and T. Squartini, Fast and scalable likelihood maximization for exponential random graph models with local constraints, [Sci. Rep. 11, 15227 (2021)](https://doi.org/10.1038/s41598-021-93830-4).
* Di Vece *et al.* [2023]
  M. Di Vece, D. Garlaschelli, and T. Squartini, Deterministic, quenched, and annealed parameter estimation for heterogeneous network models, [Phys. Rev. E 108, 054301 (2023)](https://doi.org/10.1103/PhysRevE.108.054301).
* Squartini *et al.* [2018]
  T. Squartini, G. Caldarelli, G. Cimini, A. Gabrielli, and D. Garlaschelli, Reconstruction methods for networks: The case of economic and financial systems, [Phys. Rep. 757, 1 (2018)](https://doi.org/10.1016/j.physrep.2018.06.008).
* Zhou [2021]
  T. Zhou, Progresses and challenges in link prediction, [iScience 24, 103217 (2021)](https://doi.org/10.1016/j.isci.2021.103217).
* Lü and Zhou [2011]
  L. Lü and T. Zhou, Link prediction in complex networks: A survey, [Physica A 390, 1150 (2011)](https://doi.org/10.1016/j.physa.2010.11.027).
* Santucci *et al.* [2026]
  F. Santucci, G. Cimini, and T. Squartini, Missing links prediction: comparing machine learning with physics-rooted approaches, arXiv [10.48550/arXiv.2601.23061](https://doi.org/10.48550/arXiv.2601.23061) (2026).
* Bardoscia *et al.* [2021]
  M. Bardoscia, P. Barucca, S. Battiston, F. Caccioli, G. Cimini, D. Garlaschelli, F. Saracco, T. Squartini, and G. Caldarelli, The physics of financial networks, [Nature Reviews Physics 3, 490 (2021)](https://doi.org/10.1038/s42254-021-00322-5).
* Ialongo *et al.* [2022]
  L. N. Ialongo, C. de Valk, E. Marchese, F. Jansen, H. Zmarrou, T. Squartini, and D. Garlaschelli, Reconstructing firm-level interactions in the dutch input–output network from production constraints, [Scientific Reports 12, 11847 (2022)](https://doi.org/10.1038/s41598-022-15714-4).
* Mungo *et al.* [2023]
  L. Mungo, F. Lafond, P. Astudillo-Estévez, and J. D. Farmer, Reconstructing production networks using machine learning, [Journal of Economic Dynamics and Control 148, 104607 (2023)](https://doi.org/10.1016/j.jedc.2023.104607).
* Gelman *et al.* [2013]
  A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B. Rubin, [*Bayesian Data Analysis*](https://doi.org/10.1201/b16018), 3rd ed. (Chapman and Hall/CRC, New York, 2013).
* Cimini *et al.* [2015]
  G. Cimini, T. Squartini, D. Garlaschelli, and A. Gabrielli, Systemic risk analysis on reconstructed economic and financial networks, [Sci. Rep. 5, 15758 (2015)](https://doi.org/10.1038/srep15758).
* Mazzarisi and Lillo [2017]
  P. Mazzarisi and F. Lillo, Methods for reconstructing interbank networks from limited information: A comparison, in [*Econophysics and Sociophysics: Recent Progress and Future Directions*](https://doi.org/10.1007/978-3-319-47705-3_15), New Economic Windows, edited by F. Abergel, B. K. Chakrabarti, A. Ghosh, M. Mitra, M. Patriarca, and A. Vespignani (Springer, Cham, 2017) pp. 201–215.
* Anand *et al.* [2018]
  K. Anand, I. van Lelyveld, Á. Banai, S. Friedrich, R. Garratt, G. Hałaj, J. Fique, I. Hansen, S. M. Jaramillo, H. Lee, J. L. Molina-Borboa, S. Nobili, S. Rajan, D. Salakhova, T. C. Silva, L. Silvestri, and S. R. S. de Souza, The missing links: A global study on uncovering financial network structures from partial data, [J. Financ. Stability 35, 107 (2018)](https://doi.org/10.1016/j.jfs.2017.05.012).
* Lebacher *et al.* [2019]
  M. Lebacher, S. Cook, N. Klein, and G. Kauermann, In search of lost edges: A case study on reconstructing financial networks, [J. Network Theory in Finance 5, 29 (2019)](https://doi.org/10.21314/JNTF.2019.058).
* Ramadiah *et al.* [2020]
  A. Ramadiah, F. Caccioli, and D. Fricke, Reconstructing and stress testing credit networks, [J. Econ. Dyn. Control 111, 103817 (2020)](https://doi.org/10.1016/j.jedc.2019.103817).
* Cimini *et al.* [2021]
  G. Cimini, R. Mastrandrea, and T. Squartini, [*Reconstructing Networks*](https://doi.org/10.1017/9781108771030), Elements in the Structure and Dynamics of Complex Networks (Cambridge Univ. Press, 2021).
* Marzi *et al.* [2026]
  M. Marzi, F. Giuffrida, D. Garlaschelli, and T. Squartini, Reproducing the first and second moments of empirical degree distributions, [Phys. Rev. Res. 8, 013047 (2026)](https://doi.org/10.1103/3vtj-5nlt).
* Iori *et al.* [2008]
  G. Iori, G. D. Masi, O. Precup, G. Gabbi, and G. Caldarelli, A network analysis of the italian overnight money market, [J. Econ. Dyn. Control 32, 259 (2008)](https://doi.org/10.1016/j.jedc.2007.01.032).
* Finger *et al.* [2012]
  K. Finger, D. Fricke, and T. Lux, *Network analysis of the e-MID overnight money market: The informational value of different aggregation levels for intrinsic dynamic processes*, Kiel Working Paper 1782 (Kiel Institute for the World Economy (IfW Kiel), 2012).
* Massey [1951]
  F. J. Massey, The kolmogorov-smirnov test for goodness of fit, [J. Am. Stat. Assoc. 46, 68 (1951)](https://doi.org/10.1080/01621459.1951.10500769).
* Parisi *et al.* [2018]
  F. Parisi, G. Caldarelli, and T. Squartini, Entropy-based approach to missing-links prediction, [Appl. Netw. Sci. 3, 17 (2018)](https://doi.org/10.1007/s41109-018-0073-4).
* Peixoto [2018]
  T. P. Peixoto, Reconstructing networks with unknown and heterogeneous errors, [Phys. Rev. X 8, 041011 (2018)](https://doi.org/10.1103/PhysRevX.8.041011).
* Peixoto [2025]
  T. P. Peixoto, Network reconstruction via the minimum description length principle, [Phys. Rev. X 15, 011065 (2025)](https://doi.org/10.1103/PhysRevX.15.011065).
* Young *et al.* [2020]
  J.-G. Young, G. T. Cantwell, and M. E. J. Newman, Bayesian inference of network structure from unreliable data, [J. Complex Netw. 8, cnaa046 (2020)](https://doi.org/10.1093/comnet/cnaa046).
* Abramowitz and Stegun [1964]
  M. Abramowitz and I. A. Stegun, eds., *Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables*, Applied Mathematics Series, Vol. 55 (National Bureau of Standards, Washington, D.C., 1964).
* Neal [2003]
  R. M. Neal, Slice sampling, [Ann. Statist. 31, 705 (2003)](https://doi.org/10.1214/aos/1056562461).

## ACKNOWLEDGMENTS

MM and TS acknowledge support from the project ‘SoBigData.it - Strengthening the Italian RI for Social Mining and Big Data Analytics’ - IR0000013 - CUP B53C22001760006, financed by European Union - Next Generation EU - National Recovery and Resilience Plan (Piano Nazionale di Ripresa e Resilienza, PNRR) - M4C2 I.3.1; TS acknowledges support from the projects ‘RE-Net: Reconstructing economic networks: from physics to machine learning and back’ - 2022MTBB22, Funded by the European Union Next Generation EU, PNRR Mission 4 Component 2 Investment 1.1, CUP: D53D23002330006; ‘C2T - From Crises to Theory: towards a science of resilience and recovery for economic and financial systems’ - P2022E93B8, Funded by the European Union Next Generation EU, PNRR Mission 4 Component 2 Investment 1.1, CUP: D53D23019330001.

## AUTHOR CONTRIBUTIONS

Study conception and design: MM, TS. Analysis and interpretation of results: MM, TS. Draft manuscript preparation: MM, TS.

## COMPETING INTERESTS

The authors declare no competing interests.

## APPENDIX A. More on the posterior predictive distribution

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)=∫0+∞P​(𝐀t+1|z)​P​(z|𝐀t)​𝑑z=∫0+∞∏i=1N∏j(>i)(pi​jt+1)ai​jt+1​(1−pi​jt+1)1−ai​jt+1​P​(z|𝐀t)​d​zP(\mathbf{A}\_{t+1}|\mathbf{A}\_{t})=\int\_{0}^{+\infty}P(\mathbf{A}\_{t+1}|z)P(z|\mathbf{A}\_{t})dz=\int\_{0}^{+\infty}\prod\_{i=1}^{N}\prod\_{j(>i)}\left(p\_{ij}^{t+1}\right)^{a\_{ij}^{t+1}}\left(1-p\_{ij}^{t+1}\right)^{1-a\_{ij}^{t+1}}P(z|\mathbf{A}\_{t})dz |  | (43) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑ai​jt+1=01(pi​jt+1)ai​jt+1​(1−pi​jt+1)1−ai​jt+1=1,\displaystyle\sum\_{a\_{ij}^{t+1}=0}^{1}\left(p\_{ij}^{t+1}\right)^{a\_{ij}^{t+1}}\left(1-p\_{ij}^{t+1}\right)^{1-a\_{ij}^{t+1}}=1, |  | (44) |

one finds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ai​jt+1|𝐀t⟩\displaystyle\langle a\_{ij}^{t+1}|\mathbf{A}\_{t}\rangle | =∑𝐀t+1ai​jt+1​P​(𝐀t+1|𝐀t)\displaystyle=\sum\_{\mathbf{A}\_{t+1}}a\_{ij}^{t+1}P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑ai​jt+1∑𝐀t+1∖ai​jt+1ai​jt+1​P​(𝐀t+1|𝐀t)\displaystyle=\sum\_{a\_{ij}^{t+1}}\sum\_{\mathbf{A}\_{t+1}\setminus a\_{ij}^{t+1}}a\_{ij}^{t+1}P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =0⋅P​(ai​jt+1=0|𝐀t)+1⋅P​(ai​jt+1=1|𝐀t)\displaystyle=0\cdot P(a\_{ij}^{t+1}=0|\mathbf{A}\_{t})+1\cdot P(a\_{ij}^{t+1}=1|\mathbf{A}\_{t}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =P​(ai​jt+1=1|𝐀t).\displaystyle=P(a\_{ij}^{t+1}=1|\mathbf{A}\_{t}). |  | (45) |

## APPENDIX B. The Bayesian Erdös-Rényi Model

Let us, now, fully illustrate the calculations concerning the Erdös-Rényi Model. Since its classical formulation reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀|p)=pL​(𝐀)​(1−p)V−L​(𝐀),P(\mathbf{A}|p)=p^{L(\mathbf{A})}(1-p)^{V-L(\mathbf{A})}, |  | (46) |

with V=N​(N−1)/2V=N(N-1)/2, enriching it with a conjugate prior amounts to considering the expression

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(p|𝐀)\displaystyle P(p|\mathbf{A}) | =P​(𝐀|p)​π​(p)∫01P​(𝐀|p)​π​(p)​𝑑p=pL​(𝐀)+α−1​(1−p)V−L​(𝐀)+β−1∫01pL​(𝐀)+α−1​(1−p)V−L​(𝐀)+β−1​𝑑p=pL​(𝐀)+α−1​(1−p)V−L​(𝐀)+β−1B​(L​(𝐀)+α,V−L​(𝐀)+β),\displaystyle=\frac{P(\mathbf{A}|p)\pi(p)}{\int\_{0}^{1}P(\mathbf{A}|p)\pi(p)dp}=\frac{p^{L(\mathbf{A})+\alpha-1}(1-p)^{V-L(\mathbf{A})+\beta-1}}{\int\_{0}^{1}p^{L(\mathbf{A})+\alpha-1}(1-p)^{V-L(\mathbf{A})+\beta-1}dp}=\frac{p^{L(\mathbf{A})+\alpha-1}(1-p)^{V-L(\mathbf{A})+\beta-1}}{\text{B}(L(\mathbf{A})+\alpha,V-L(\mathbf{A})+\beta)}, |  | (47) |

coming from posing

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(p)=pα−1​(1−p)β−1B​(α,β),\displaystyle\pi(p)=\frac{p^{\alpha-1}(1-p)^{\beta-1}}{\text{B}(\alpha,\beta)}, |  | (48) |

where B​(α,β)=∫01pα−1​(1−p)β−1​𝑑p\text{B}(\alpha,\beta)=\int\_{0}^{1}p^{\alpha-1}(1-p)^{\beta-1}dp is the Beta function. We can, thus, write

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Lt+1=k|𝐀t)\displaystyle P(L\_{t+1}=k|\mathbf{A}\_{t}) | =∫01P​(Lt+1=k|p)​P​(p|𝐀t)​𝑑p\displaystyle=\int\_{0}^{1}P(L\_{t+1}=k|p)P(p|\mathbf{A}\_{t})dp |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01(Vt+1k)​pk​(1−p)Vt+1−k​P​(p|𝐀t)​𝑑p\displaystyle=\int\_{0}^{1}\binom{V\_{t+1}}{k}p^{k}(1-p)^{V\_{t+1}-k}P(p|\mathbf{A}\_{t})dp |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫01(Vt+1k)​pk​(1−p)Vt+1−k​P​(𝐀t|p)​π​(p)P​(𝐀t)​𝑑p\displaystyle=\int\_{0}^{1}\binom{V\_{t+1}}{k}p^{k}(1-p)^{V\_{t+1}-k}\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp |  | (49) |

and

![Refer to caption](x15.png)

![Refer to caption](x16.png)

![Refer to caption](x17.png)

![Refer to caption](x18.png)

Figure B.1: Top left: histogram of the estimated p∗p^{\*} values across the calibration set consisting of the weeks (augmented via the jack-knife method) constituting the years 19991999-20012001 together with two, fitted PDFs, i.e. a beta distribution (orange line) and a normal distribution (green line); both of them provide a reasonable fit and they are ’saved’ from the Kolmogorov-Smirnov test. Top right: empirical VS predicted PDF of the total number of links (red) and nodes degrees (blue), pooled across the weeks constituting the year 20022002. Bottom left: evolution of the ⟨TPR⟩\langle\text{TPR}\rangle, the ⟨PPV⟩\langle\text{PPV}\rangle, the ⟨TNR⟩\langle\text{TNR}\rangle and the ⟨ACC⟩\langle\text{ACC}\rangle across the weeks constituing the year 20022002. Bottom right: evolution of the relative error on the total number of links (red) and the average relative error on the node degrees (blue), across the weeks constituting the year 20022002.

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀t)=∫01P​(𝐀t|p)​π​(p)​𝑑p=∫01pLt+α−1​(1−p)Vt−Lt+β−1​𝑑p=B​(Lt+α,Vt−Lt+β),\displaystyle P(\mathbf{A}\_{t})=\int\_{0}^{1}P(\mathbf{A}\_{t}|p)\pi(p)dp=\int\_{0}^{1}p^{L\_{t}+\alpha-1}(1-p)^{V\_{t}-L\_{t}+\beta-1}dp=\text{B}(L\_{t}+\alpha,V\_{t}-L\_{t}+\beta), |  | (50) |

where the explicit dependence of the expression above on 𝐀t\mathbf{A}\_{t} has been dropped. Putting everything together, one gets

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Lt+1=k|𝐀t)=(Vt+1k)​∫01pk+Lt+α−1​(1−p)Vt+1+Vt−k−Lt+β−1​𝑑p∫01pLt+α−1​(1−p)Vt−Lt+β−1​𝑑p=(Vt+1k)​B​(k+Lt+α,Vt+1+Vt−k−Lt+β)B​(Lt+α,Vt−Lt+β),\displaystyle P(L\_{t+1}=k|\mathbf{A}\_{t})=\binom{V\_{t+1}}{k}\frac{\int\_{0}^{1}p^{k+L\_{t}+\alpha-1}(1-p)^{V\_{t+1}+V\_{t}-k-L\_{t}+\beta-1}dp}{\int\_{0}^{1}p^{L\_{t}+\alpha-1}(1-p)^{V\_{t}-L\_{t}+\beta-1}dp}=\binom{V\_{t+1}}{k}\frac{\text{B}(k+L\_{t}+\alpha,V\_{t+1}+V\_{t}-k-L\_{t}+\beta)}{\text{B}(L\_{t}+\alpha,V\_{t}-L\_{t}+\beta)}, |  | (51) |

i.e. the total number of links at time t+1t+1, conditional to the observation of 𝐀t\mathbf{A}\_{t}, obeys the beta-binomial distribution BetaBin​(Vt+1,Lt+α,Vt−Lt+β)\text{BetaBin}(V\_{t+1},L\_{t}+\alpha,V\_{t}-L\_{t}+\beta). Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Lt+1|𝐀t⟩=∑k=0Vt+1k​P​(Lt+1=k|𝐀t)=∑k=0Vt+1k​∫01P​(Lt+1=k|p)​P​(p|𝐀t)​𝑑p,\displaystyle\langle L\_{t+1}|\mathbf{A}\_{t}\rangle=\sum\_{k=0}^{V\_{t+1}}kP(L\_{t+1}=k|\mathbf{A}\_{t})=\sum\_{k=0}^{V\_{t+1}}k\int\_{0}^{1}P(L\_{t+1}=k|p)P(p|\mathbf{A}\_{t})dp, |  | (52) |

swapping the operations of sum and integration leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨Lt+1|𝐀t⟩\displaystyle\langle L\_{t+1}|\mathbf{A}\_{t}\rangle | =∫01∑k=0Vt+1k​P​(Lt+1=k|p)​P​(p|𝐀t)​d​p\displaystyle=\int\_{0}^{1}\sum\_{k=0}^{V\_{t+1}}kP(L\_{t+1}=k|p)P(p|\mathbf{A}\_{t})dp |  | (53) |

and recognizing in P​(Lt+1=k|p)P(L\_{t+1}=k|p) a binomial distribution further leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Lt+1|𝐀t⟩\displaystyle\langle L\_{t+1}|\mathbf{A}\_{t}\rangle | =∫01∑k=0Vt+1k​(Vt+1k)​pk​(1−p)Vt+1−k​P​(𝐀t|p)​π​(p)P​(𝐀t)​d​p\displaystyle=\int\_{0}^{1}\sum\_{k=0}^{V\_{t+1}}k\binom{V\_{t+1}}{k}p^{k}(1-p)^{V\_{t+1}-k}\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01Vt+1​p​P​(𝐀t|p)​π​(p)P​(𝐀t)​𝑑p\displaystyle=\int\_{0}^{1}V\_{t+1}p\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Vt+1​∫01p​P​(𝐀t|p)​π​(p)P​(𝐀t)​𝑑p.\displaystyle=V\_{t+1}\int\_{0}^{1}p\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp. |  | (54) |

Comparing the expression above with eq. [9](https://arxiv.org/html/2602.21869v1#Sx2.E9 "Equation 9 ‣ Towards a Bayesian approach ‣ RESULTS ‣ A Bayesian approach to out-of-sample network reconstruction") leads us to name the second factor qt+1q^{t+1}: hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | qt+1=∫01p​P​(𝐀t|p)​π​(p)P​(𝐀t)​𝑑p=∫01p1+Lt+α−1​(1−p)Vt−Lt+β−1​𝑑p∫01pLt+α−1​(1−p)Vt−Lt+β−1​𝑑p=B​(1+Lt+α,Vt−Lt+β)B​(Lt+α,Vt−Lt+β)=Lt+αVt+α+β,\displaystyle q^{t+1}=\int\_{0}^{1}p\frac{P(\mathbf{A}\_{t}|p)\pi(p)}{P(\mathbf{A}\_{t})}dp=\frac{\int\_{0}^{1}p^{1+L\_{t}+\alpha-1}(1-p)^{V\_{t}-L\_{t}+\beta-1}dp}{\int\_{0}^{1}p^{L\_{t}+\alpha-1}(1-p)^{V\_{t}-L\_{t}+\beta-1}dp}=\frac{\text{B}(1+L\_{t}+\alpha,V\_{t}-L\_{t}+\beta)}{\text{B}(L\_{t}+\alpha,V\_{t}-L\_{t}+\beta)}=\frac{L\_{t}+\alpha}{V\_{t}+\alpha+\beta}, |  | (55) |

where we have employed the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(x+1,y)B​(x,y)=Γ​(x+1)​Γ​(y)Γ​(x+y+1)⋅Γ​(x+y)Γ​(x)​Γ​(y)=x​Γ​(x)​Γ​(y)(x+y)​Γ​(x+y)⋅Γ​(x+y)Γ​(x)​Γ​(y)=xx+y.\displaystyle\frac{\text{B}(x+1,y)}{\text{B}(x,y)}=\frac{\Gamma(x+1)\Gamma(y)}{\Gamma(x+y+1)}\cdot\frac{\Gamma(x+y)}{\Gamma(x)\Gamma(y)}=\frac{x\Gamma(x)\Gamma(y)}{(x+y)\Gamma(x+y)}\cdot\frac{\Gamma(x+y)}{\Gamma(x)\Gamma(y)}=\frac{x}{x+y}. |  | (56) |

The performance of the model in reproducing the chosen empirical quantities across the weeks of the year 20022002 is shown in fig. [B.1](https://arxiv.org/html/2602.21869v1#Ax2.F1 "Figure B.1 ‣ APPENDIX B. The Bayesian Erdös-Rényi Model ‣ A Bayesian approach to out-of-sample network reconstruction"). As their number amounts to ≃150\simeq 150, we have implemented the jack-knife method to augment the sample: more specifically, we have removed each day of each week at a time, hence producing 77 weeks of 66 days each out of 11 week of 77 days; upon doing so, we have moved from ≃150\simeq 150 snapshots to ≃1000\simeq 1000 snapshots. Here, we have focused on a balanced panel of N=73N=73 banks.

The performance of the model in reproducing the chosen empirical quantities across the weeks constituting our dataset is, instead, shown in fig. [B.2](https://arxiv.org/html/2602.21869v1#Ax2.F2 "Figure B.2 ‣ APPENDIX B. The Bayesian Erdös-Rényi Model ‣ A Bayesian approach to out-of-sample network reconstruction"). Its right panel deserves to be commented more. First, let us notice that the MREk\text{MRE}\_{k} decreases: this seems to suggest that the network topology is becoming increasingly compatible with such a model - although overly simple. Second, let us notice the bump in correspondence of the year 20082008: this suggests that the crisis reveals itself as an event challenging the model adopted to describe the system under consideration, letting the error associated with the estimates of the degrees rise. Overall, however, the two evidences above confirm the results obtained in analogous papers, i.e. that financial systems somehow ‘lose’ structure after a crisis.

![Refer to caption](x19.png)

![Refer to caption](x20.png)

Figure B.2: Left panel: histogram of the estimated p∗p^{\*} values across the calibration set consisting of the weeks (augmented via the jack-knife method) constituting the years 19991999-20012001 together with two, fitted PDFs, i.e. a beta distribution (orange line) and a normal distribution (green line); both of them provide a reasonable fit, as confirmed by the Kolmogorov-Smirnov test. Right panel: evolution of the relative error on the total number of links (red) and the maximum relative error on the node degrees (cyan), across the weeks constituting our dataset.

## APPENDIX C. The Bayesian Fitness Model

Let us, now, fully illustrate the calculations concerning the Fitness Model. Overall,

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)\displaystyle P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) | =∫0+∞P​(𝐀t+1|z)​P​(z|𝐀t)​𝑑z\displaystyle=\int\_{0}^{+\infty}P(\mathbf{A}\_{t+1}|z)P(z|\mathbf{A}\_{t})dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0+∞P​(𝐀t+1|z)​P​(𝐀t|z)​π​(z)P​(𝐀t)​𝑑z\displaystyle=\int\_{0}^{+\infty}\frac{P(\mathbf{A}\_{t+1}|z)P(\mathbf{A}\_{t}|z)\pi(z)}{P(\mathbf{A}\_{t})}dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0+∞[∏i=1N∏j(>i)(pi​jt+1)ai​jt+1​(1−pi​jt+1)1−ai​jt+1]​[∏i=1N∏j(>i)(pi​jt)ai​jt​(1−pi​jt)1−ai​jt]​π​(z)​𝑑z∫0+∞[∏i=1N∏j(>i)(pi​jt)ai​jt​(1−pi​jt)1−ai​jt]​π​(z)​𝑑z\displaystyle=\frac{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\left(p\_{ij}^{t+1}\right)^{a\_{ij}^{t+1}}\left(1-p\_{ij}^{t+1}\right)^{1-a\_{ij}^{t+1}}\right]\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\left(p\_{ij}^{t}\right)^{a\_{ij}^{t}}\left(1-p\_{ij}^{t}\right)^{1-a\_{ij}^{t}}\right]\pi(z)dz}{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\left(p\_{ij}^{t}\right)^{a\_{ij}^{t}}\left(1-p\_{ij}^{t}\right)^{1-a\_{ij}^{t}}\right]\pi(z)dz} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0+∞[∏i=1N∏j(>i)(pi​jt+11−pi​jt+1)ai​jt+1​(1−pi​jt+1)]​[∏i=1N∏j(>i)(pi​jt1−pi​jt)ai​jt​(1−pi​jt)]​π​(z)​𝑑z∫0+∞[∏i=1N∏j(>i)(pi​jt1−pi​jt)ai​jt​(1−pi​jt)]​π​(z)​𝑑z\displaystyle=\frac{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\left(\frac{p\_{ij}^{t+1}}{1-p\_{ij}^{t+1}}\right)^{a\_{ij}^{t+1}}\left(1-p\_{ij}^{t+1}\right)\right]\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\left(\frac{p\_{ij}^{t}}{1-p\_{ij}^{t}}\right)^{a\_{ij}^{t}}\left(1-p\_{ij}^{t}\right)\right]\pi(z)dz}{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\left(\frac{p\_{ij}^{t}}{1-p\_{ij}^{t}}\right)^{a\_{ij}^{t}}\left(1-p\_{ij}^{t}\right)\right]\pi(z)dz} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0+∞[∏i=1N∏j(>i)(z​sit+1​sjt+1)ai​jt+11+z​sit+1​sjt+1]​[∏i=1N∏j(>i)(z​sit​sjt)ai​jt1+z​sit​sjt]​π​(z)​𝑑z∫0+∞[∏i=1N∏j(>i)(z​sit​sjt)ai​jt1+z​sit​sjt]​π​(z)​𝑑z;\displaystyle=\frac{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t+1}s\_{j}^{t+1}\right)^{a\_{ij}^{t+1}}}{1+zs\_{i}^{t+1}s\_{j}^{t+1}}\right]\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}}{1+zs\_{i}^{t}s\_{j}^{t}}\right]\pi(z)dz}{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}}{1+zs\_{i}^{t}s\_{j}^{t}}\right]\pi(z)dz}; |  | (57) |

in words, predictive reconstruction assumes a shared density scale across tt and t+1t+1, together with conditional independence. The strengths, instead, are allowed to vary over time.

![Refer to caption](x21.png)

![Refer to caption](x22.png)

![Refer to caption](x23.png)

![Refer to caption](x24.png)

Figure C.1: Top left: histogram of the estimated z∗z^{\*} values across the calibration set consisting of the weeks (augmented via the jack-knife method) constituting the years 19991999-20012001 together with three, fitted PDFs, i.e. a gamma distribution (orange line), a normal distribution (red line) and a log-normal distribution (green line); although all of them provide a reasonable fit, the Kolmogorov-Smirnov test only ‘saves’ the gamma distribution. Top right: empirical VS predicted PDF of the total number of links (red) and nodes degrees (blue), pooled across the weeks constituting the year 20022002. Bottom left: evolution of the ⟨TPR⟩\langle\text{TPR}\rangle, the ⟨PPV⟩\langle\text{PPV}\rangle, the ⟨TNR⟩\langle\text{TNR}\rangle and the ⟨ACC⟩\langle\text{ACC}\rangle across the weeks constituting the year 20022002. Bottom right: evolution of the relative error on the total number of links (red) and the average relative error on the node degrees (blue), across the weeks constituting the year 20022002.

Let us notice that the formulas above are valid to analyze a balanced panel of nodes (Nt=Nt+1=NN\_{t}=N\_{t+1}=N); nothing, however, prevents us from considering an unbalanced one: in such a case,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)\displaystyle P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) | =∫0+∞[∏i=1Nt+1∏j(>i)(z​sit+1​sjt+1)ai​jt+11+z​sit+1​sjt+1]​[∏i=1Nt∏j(>i)(z​sit​sjt)ai​jt1+z​sit​sjt]​π​(z)​𝑑z∫0+∞[∏i=1Nt∏j(>i)(z​sit​sjt)ai​jt1+z​sit​sjt]​π​(z)​𝑑z.\displaystyle=\frac{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N\_{t+1}}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t+1}s\_{j}^{t+1}\right)^{a\_{ij}^{t+1}}}{1+zs\_{i}^{t+1}s\_{j}^{t+1}}\right]\left[\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}}{1+zs\_{i}^{t}s\_{j}^{t}}\right]\pi(z)dz}{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}}{1+zs\_{i}^{t}s\_{j}^{t}}\right]\pi(z)dz}. |  | (58) |

![Refer to caption](x25.png)

![Refer to caption](x26.png)

Figure C.2: Left panel: histogram of the estimated z∗z^{\*} values across the calibration set consisting of the weeks (augmented via the jack-knife method) constituting the years 19991999-20012001 together with three, fitted PDFs, i.e. a gamma distribution (orange line), a normal distribution (red line) and a log-normal distribution (red line); although all of them provide a reasonable fit, the Kolmogorov-Smirnov test only ‘saves’ the gamma distribution. Right panel: evolution of the relative error on the total number of links (red) and the maximum relative error on the node degrees (blue), across the weeks constituting our dataset.

The performance of the model in reproducing the chosen empirical quantities across the weeks of the year 20022002 is shown in fig. [C.1](https://arxiv.org/html/2602.21869v1#Ax3.F1 "Figure C.1 ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction"). As their number amounts to ≃150\simeq 150, we have implemented the jack-knife method to augment the sample: more specifically, we have removed each day of each week at a time, hence producing 77 weeks of 66 days each out of 11 week of 77 days; upon doing so, we have moved from ≃150\simeq 150 snapshots to ≃1000\simeq 1000 snapshots. Here, we have focused on a balanced panel of N=73N=73 banks.

The performance of the model in reproducing the chosen empirical quantities across the weeks constituting our dataset is, instead, shown in fig. [C.2](https://arxiv.org/html/2602.21869v1#Ax3.F2 "Figure C.2 ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction"). Its right panel deserves to be commented more. Let us notice the peak in correspondence of the year 20082008: again, the crisis reveals itself as an event challenging the model adopted to describe the system under consideration, letting the error associated with the estimates of the degrees rise.

Let us, now, briefly comment on the possible priors. First, let us carry out a consistency check, by noticing that employing the *deterministic prior* π​(z)=δz,zML∗\pi(z)=\delta\_{z,z^{\*}\_{\text{ML}}} lets the traditional dcGM be recovered. In order to discuss other choices, let us put ourselves in the sparse-case regime, defined by the position pi​j≃z​si​sjp\_{ij}\simeq zs\_{i}s\_{j}: this leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)\displaystyle P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) | ≃∫0+∞[∏i=1Nt+1∏j(>i)(z​sit+1​sjt+1)ai​jt+1]​[∏i=1Nt∏j(>i)(z​sit​sjt)ai​jt]​π​(z)​𝑑z∫0+∞[∏i=1Nt∏j(>i)(z​sit​sjt)ai​jt]​π​(z)​𝑑z\displaystyle\simeq\frac{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N\_{t+1}}\prod\_{j(>i)}\left(zs\_{i}^{t+1}s\_{j}^{t+1}\right)^{a\_{ij}^{t+1}}\right]\left[\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\left(zs\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}\right]\pi(z)dz}{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\left(zs\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}\right]\pi(z)dz} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≃∏i=1Nt+1∏j(>i)(sit+1​sjt+1)ai​jt+1⋅∏i=1Nt∏j(>i)(sit​sjt)ai​jt​∫0+∞zLt+1+Lt​π​(z)​𝑑z∏i=1Nt∏j(>i)(sit​sjt)ai​jt​∫0+∞zLt​π​(z)​𝑑z\displaystyle\simeq\frac{\prod\_{i=1}^{N\_{t+1}}\prod\_{j(>i)}\left(s\_{i}^{t+1}s\_{j}^{t+1}\right)^{a\_{ij}^{t+1}}\cdot\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\left(s\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}\int\_{0}^{+\infty}z^{L\_{t+1}+L\_{t}}\pi(z)dz}{\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\left(s\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}\int\_{0}^{+\infty}z^{L\_{t}}\pi(z)dz} |  | (59) |

that can be further simplified into

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)\displaystyle P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) | =∏i=1Nt+1∏j(>i)(sit+1​sjt+1)ai​jt+1​∫0+∞zLt+1+Lt​π​(z)​𝑑z∫0+∞zLt​π​(z)​𝑑z;\displaystyle=\prod\_{i=1}^{N\_{t+1}}\prod\_{j(>i)}\left(s\_{i}^{t+1}s\_{j}^{t+1}\right)^{a\_{ij}^{t+1}}\frac{\int\_{0}^{+\infty}z^{L\_{t+1}+L\_{t}}\pi(z)dz}{\int\_{0}^{+\infty}z^{L\_{t}}\pi(z)dz}; |  | (60) |

instantiating the formula above with a *uniform prior*, ranging between 0 and z^<+∞\hat{z}<+\infty, leads us to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(𝐀t+1|𝐀t)\displaystyle P(\mathbf{A}\_{t+1}|\mathbf{A}\_{t}) | =∏i=1Nt+1∏j(>i)(sit+1​sjt+1)ai​jt+1⋅z^Lt+1+Lt+1Lt+1+Lt+1⋅Lt+1z^Lt+1≃∏i=1Nt+1∏j(>i)(sit+1​sjt+1)ai​jt+1⋅LtLt+1+Lt⋅z^Lt+1.\displaystyle=\prod\_{i=1}^{N\_{t+1}}\prod\_{j(>i)}\left(s\_{i}^{t+1}s\_{j}^{t+1}\right)^{a\_{ij}^{t+1}}\cdot\frac{\hat{z}^{L\_{t+1}+L\_{t}+1}}{L\_{t+1}+L\_{t}+1}\cdot\frac{L\_{t}+1}{\hat{z}^{L\_{t}+1}}\simeq\prod\_{i=1}^{N\_{t+1}}\prod\_{j(>i)}\left(s\_{i}^{t+1}s\_{j}^{t+1}\right)^{a\_{ij}^{t+1}}\cdot\frac{L\_{t}}{L\_{t+1}+L\_{t}}\cdot\hat{z}^{L\_{t+1}}. |  | (61) |

The marginal probability, instead, reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​jt+1\displaystyle q\_{ij}^{t+1} | =∫0+∞pi​jt+1​(z)​P​(𝐀t|z)​π​(z)P​(𝐀t)​𝑑z\displaystyle=\int\_{0}^{+\infty}p\_{ij}^{t+1}(z)\frac{P(\mathbf{A}\_{t}|z)\pi(z)}{P(\mathbf{A}\_{t})}\,dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≃∫0+∞(z​sit+1​sjt+1)​zLt​π​(z)∫0+∞zLt​π​(z)​𝑑z​𝑑z\displaystyle\simeq\int\_{0}^{+\infty}(zs\_{i}^{t+1}s\_{j}^{t+1})\frac{z^{L\_{t}}\pi(z)}{\int\_{0}^{+\infty}z^{L\_{t}}\pi(z)\,dz}\,dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =sit+1​sjt+1​∫0+∞zLt+1​π​(z)​𝑑z∫0+∞zLt​π​(z)​𝑑z\displaystyle=s\_{i}^{t+1}s\_{j}^{t+1}\frac{\int\_{0}^{+\infty}z^{L\_{t}+1}\pi(z)\,dz}{\int\_{0}^{+\infty}z^{L\_{t}}\pi(z)\,dz} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =sit+1​sjt+1​∫0z^zLt+1​𝑑z∫0z^zLt​𝑑z\displaystyle=s\_{i}^{t+1}s\_{j}^{t+1}\frac{\int\_{0}^{\hat{z}}z^{L\_{t}+1}\,dz}{\int\_{0}^{\hat{z}}z^{L\_{t}}\,dz} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =sit+1​sjt+1⋅Lt+1Lt+2⋅z^,\displaystyle=s\_{i}^{t+1}s\_{j}^{t+1}\cdot\frac{L\_{t}+1}{L\_{t}+2}\cdot\hat{z}, |  | (62) |

an expression confirming that, in the sparse-case regime, a uniform prior affects all the estimates of interest through a common multiplicative factor.

For what concerns the link prediction task, the expression above embodies the so-called *preferential attachment* recipe: since the rank of each link is determined by the (score individuated by the) product of the strengths of the corresponding nodes, such a recipe is independent from the choice of the prior. For what concerns the network reconstruction task, instead, this is no longer true and zz must be numerically evaluated. For consistency with the remainder of the analysis, we adopt the ML recipe, prescribing to solve the equation ∑i=1N∑j(>i)z​si​sj=L∗\sum\_{i=1}^{N}\sum\_{j(>i)}zs\_{i}s\_{j}=L^{\*}: in symbols, zCL∗=L∗/∑i=1N∑j(>i)si​sjz\_{\text{CL}}^{\*}=L^{\*}/\sum\_{i=1}^{N}\sum\_{j(>i)}s\_{i}s\_{j}. The upper bound z^\hat{z} can be determined by identifying the largest zCL∗z\_{\text{CL}}^{\*} value over all snapshots.

The performance of what may be called Bayesian Chung-Lu Model (BCLM) is depicted in fig. [C.3](https://arxiv.org/html/2602.21869v1#Ax3.F3 "Figure C.3 ‣ APPENDIX C. The Bayesian Fitness Model ‣ A Bayesian approach to out-of-sample network reconstruction"): as expected, the BFM outperforms it in reproducing the considered quantities. The worse performance of the BCLM is due to both its functional form and the choice of the prior: the first one does not guarantee that all pi​jp\_{ij}s range between 0 and 11; the second one, instead, requires the knowledge of the total number of links across all snapshots - an amount of information that is ultimately unnecessary, as proven by our exercise about ‘self-sustained’ inference.

![Refer to caption](x27.png)

![Refer to caption](x28.png)

Figure C.3: Performance of the Bayesian Chung-Lu model (BCLM). Left panel: empirical values of the toal number of links (red) and node degrees (blue) scattered versus the corresponding predicted ones, pooled across the weeks constituting our dataset; the dashed line marks the identity. A clear upward bias is visible, with most points lying above the diagonal, indicating that the BCLM tends to overestimate both the total number of links and node degrees. Right panel: evolution of the relative error on the total number of links (red) and the maximum relative error on the node degrees (blue), across the weeks constituing our dataset. Overall, the BCLM yields systematically larger errors than the BFM, thus highlighting the importance of a careful choice of the prior.

## APPENDIX D. Numerical integration of the posterior predictive distribution

Let us start by recalling that the probability distribution of the fitness model reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(𝐀t|z)\displaystyle P(\mathbf{A}\_{t}|z) | =∏i=1Nt∏j(>i)(pi​jt)ai​jt​(1−pi​jt)1−ai​jt=∏i=1Nt∏j(>i)(z​sit​sjt1+z​sit​sjt)ai​jt​(11+z​sit​sjt)1−ai​jt=∏i=1Nt∏j(>i)(z​sit​sjt)ai​jt1+z​sit​sjt;\displaystyle=\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\left(p\_{ij}^{t}\right)^{a\_{ij}^{t}}\left(1-p\_{ij}^{t}\right)^{1-a\_{ij}^{t}}=\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\left(\frac{zs\_{i}^{t}s\_{j}^{t}}{1+zs\_{i}^{t}s\_{j}^{t}}\right)^{a\_{ij}^{t}}\left(\frac{1}{1+zs\_{i}^{t}s\_{j}^{t}}\right)^{1-a\_{ij}^{t}}=\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t}s\_{j}^{t}\right)^{a\_{ij}^{t}}}{1+zs\_{i}^{t}s\_{j}^{t}}; |  | (63) |

its logarithm, then, gives the log-likelihood

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(z)\displaystyle\mathcal{L}(z) | =∑i=1Nt∑j(>i)ai​jt​ln⁡z+∑i=1Nt∑j(>i)ai​jt​ln⁡[sit​sjt]−∑i=1Nt∑j(>i)log⁡[1+z​sit​sjt]\displaystyle=\sum\_{i=1}^{N\_{t}}\sum\_{j(>i)}a\_{ij}^{t}\ln z+\sum\_{i=1}^{N\_{t}}\sum\_{j(>i)}a\_{ij}^{t}\ln[s\_{i}^{t}s\_{j}^{t}]-\sum\_{i=1}^{N\_{t}}\sum\_{j(>i)}\log[1+zs\_{i}^{t}s\_{j}^{t}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Lt​ln⁡z+∑i=1Nt∑j(>i)ai​jt​ln⁡[sit​sjt]−∑i=1Nt∑j(>i)log⁡[1+z​sit​sjt].\displaystyle=L\_{t}\>\ln z+\sum\_{i=1}^{N\_{t}}\sum\_{j(>i)}a\_{ij}^{t}\ln[s\_{i}^{t}s\_{j}^{t}]-\sum\_{i=1}^{N\_{t}}\sum\_{j(>i)}\log[1+zs\_{i}^{t}s\_{j}^{t}]. |  | (64) |

### Log-space formulation

Let us, now, set u=ln⁡zu=\ln z, a transformation mapping the original domain (0,+∞)(0,+\infty) onto ℝ\mathbb{R} and preventing numerical overflow when zz becomes large. In log-space, the expression above becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(u)=Lt​u−∑i=1Nt∑j(>i)ln⁡[1+eu​sit​sjt],\ell(u)=L\_{t}\>u-\sum\_{i=1}^{N\_{t}}\sum\_{j(>i)}\ln[1+e^{u}s\_{i}^{t}s\_{j}^{t}], |  | (65) |

where we have dropped the terms that do not depend on zz. Now, since p​(u|𝐀t)​d​u=p​(z|𝐀t)​d​zp(u|\mathbf{A}\_{t})du=p(z|\mathbf{A}\_{t})dz, one has

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(u|At)=p​(z|𝐀t)​d​zd​u=p​(𝐀t|z)​π​(z)​d​zd​u=P​(𝐀t|eu)​π​(eu)​eu;p(u|A\_{t})=p(z|\mathbf{A}\_{t})\frac{dz}{du}=p(\mathbf{A}\_{t}|z)\pi(z)\frac{dz}{du}=P(\mathbf{A}\_{t}|e^{u})\pi(e^{u})e^{u}; |  | (66) |

hence, the log-posterior reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(u)=ℓ​(u)+ln⁡π​(eu)+ug(u)=\ell(u)+\ln\pi(e^{u})+u |  | (67) |

(where we have dropped the terms that do not depend on uu). The (i,j)(i,j) term of the predictive probability distribution can be, thus, written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​jt+1=∫−∞+∞(eu​sit+1​sjt+11+eu​sit+1​sjt+1)​eg​(u)∫eg​(v)​𝑑v​𝑑u.q\_{ij}^{t+1}=\int\_{-\infty}^{+\infty}\left(\frac{e^{u}s\_{i}^{t+1}s\_{j}^{t+1}}{1+e^{u}s\_{i}^{t+1}s\_{j}^{t+1}}\right)\frac{e^{g(u)}}{\int e^{g(v)}dv}du. |  | (68) |

### Gauss-Hermite quadrature

The Gauss-Hermite quadrature scheme works by posing

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(u)≃g​(u^)−(u−u^)22​σ2,g(u)\simeq g(\hat{u})-\frac{(u-\hat{u})^{2}}{2\sigma^{2}}, |  | (69) |

where u^\hat{u} denotes the mode of g​(u)g(u) and σ2=[−g′′​(u^)]−1\sigma^{2}=[-g^{\prime\prime}(\hat{u})]^{-1} denotes the inverse curvature at the mode. By introducing the rescaled variable x=(u−u^)/(2​σ)x=(u-\hat{u})/(\sqrt{2}\sigma), the (i,j)(i,j) term of the predictive probability distribution becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​jt+1≃∑k=1Kwk​eu^+2​σ​xk​sit+1​sjt+11+eu^+2​σ​xk​sit+1​sjt+1q\_{ij}^{t+1}\simeq\sum\_{k=1}^{K}w\_{k}\frac{e^{\hat{u}+\sqrt{2}\sigma x\_{k}}s\_{i}^{t+1}s\_{j}^{t+1}}{1+e^{\hat{u}+\sqrt{2}\sigma x\_{k}}s\_{i}^{t+1}s\_{j}^{t+1}} |  | (70) |

where {xk,wk}k=1K\{x\_{k},w\_{k}\}\_{k=1}^{K} denote the Gauss-Hermite nodes and weights.

![Refer to caption](x29.png)

![Refer to caption](x30.png)

![Refer to caption](x31.png)

![Refer to caption](x32.png)

Figure D.1: Illustration of one iteration of the ‘slice-sampling’ algorithm applied to the posterior g​(u)g(u). Top left: non-normalized log-posterior and current state u(m)u^{(m)}. Top right: the horizontal ‘slice’ y(m)=g​(u(m))y^{(m)}=g\left(u^{(m)}\right) defines the set {u:g​(u)≥y(m)}\{u:g(u)\geq y^{(m)}\}. Bottom left: initial bracket [L0,R0][L\_{0},R\_{0}] of nominal width ww and enlarged bracket [L,R][L,R] from the stepping-out phase. Bottom right: possible u∗u^{\*} values are drawn from Unif​(L,R)\text{Unif}(L,R) until g​(u∗)≥y(m)g(u^{\*})\geq y^{(m)}, thus yielding the next state u(m+1)u^{(m+1)}. In this example, the prior on z=euz=e^{u} is Gamma​(k,θ)\text{Gamma}(k,\theta), calibrated on the weeks constituting the years 19991999-20012001, and the posterior is computed for the last week of the year 20012001.

### Slice sampling

A complementary integration scheme is represented by slice sampling. Since the normalization constant of the posterior is unknown, direct sampling from p​(u|𝐀t)∝eg​(u)p(u|\mathbf{A}\_{t})\propto e^{g(u)} is not possible: slice sampling, then, introduces an auxiliary variable yy representing a random vertical level below the non-normalized posterior curve eg​(u)e^{g(u)}. At the mm-th iteration, we draw r(m)∼Unif​(0,1)r^{(m)}\sim\text{Unif}(0,1), so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ey(m)=eg​(u(m))​r(m)e^{y^{(m)}}=e^{g\left(u^{(m)}\right)}r^{(m)} |  | (71) |

defines a horizontal ‘slice’ at a random height uniformly distributed between 0 and the current density value eg​(u(m))e^{g\left(u^{(m)}\right)}: the point u(m+1)u^{(m+1)} is, then, drawn uniformly from those whose posterior density lies above this ‘slice’, i.e. from the set

|  |  |  |  |
| --- | --- | --- | --- |
|  | S(m)={u:g​(u)≥y(m)};S^{(m)}=\{u:g(u)\geq y^{(m)}\}; |  | (72) |

the accepted draw lies uniformly within the ‘slice’. Repeating the two-step procedure moves the pair (u(m),y(m))(u^{(m)},y^{(m)}) uniformly within the area under the posterior, so that the marginal samples {u(m)}\{u^{(m)}\} follow the desired distribution. After a burn-in phase, the draws are mapped back to z(m)=eu(m)z^{(m)}=e^{u^{(m)}}. Since

![Refer to caption](x33.png)

![Refer to caption](x34.png)

Figure D.2: Left panel: numerically normalized posterior distribution corresponding to the week #​52\#52 of the year 20012001, superimposed to the histogram of ‘slice-sampled’ draws of uu; the vertical line marks the MAP estimate. Right panel: evolution of the ‘slice-sampling’ chain across iterations (the number of sampled values amounts to M=3000M=3000, after a burn-in phase of 600600 steps), rapidly stabilizing around the higher-density region of the posterior distribution.

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​jt+1=eu​sit+1​sjt+11+eu​sit+1​sjt+1p\_{ij}^{t+1}=\frac{e^{u}s\_{i}^{t+1}s\_{j}^{t+1}}{1+e^{u}s\_{i}^{t+1}s\_{j}^{t+1}} |  | (73) |

and the BFM averages it over the posterior distribution ∝eg​(u)\propto e^{g(u)}, one gets the same expression as in eq. [68](https://arxiv.org/html/2602.21869v1#Ax4.E68 "Equation 68 ‣ Log-space formulation ‣ APPENDIX D. Numerical integration of the posterior predictive distribution ‣ A Bayesian approach to out-of-sample network reconstruction"). Knowing the denominator ∫eg​(v)​𝑑v\int e^{g(v)}dv, representing the (unknown) normalization constant of the posterior, is, however, not necessary, as qi​jt+1q\_{ij}^{t+1} is estimated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​jt+1≃1M​∑m=1Meu(m)​sit+1​sjt+11+eu(m)​sit+1​sjt+1.q\_{ij}^{t+1}\simeq\frac{1}{M}\sum\_{m=1}^{M}\frac{e^{u^{(m)}}s\_{i}^{t+1}s\_{j}^{t+1}}{1+e^{u^{(m)}}s\_{i}^{t+1}s\_{j}^{t+1}}. |  | (74) |

Figure [D.1](https://arxiv.org/html/2602.21869v1#Ax4.F1 "Figure D.1 ‣ Gauss-Hermite quadrature ‣ APPENDIX D. Numerical integration of the posterior predictive distribution ‣ A Bayesian approach to out-of-sample network reconstruction") illustrates the mechanics of one iteration of the so-called ‘slice-sampling’ algorithm applied to the posterior g​(u)g(u): ‘slice-sampling’ scales effectively, as it does not require computing the normalization constant. Figure [D.2](https://arxiv.org/html/2602.21869v1#Ax4.F2 "Figure D.2 ‣ Slice sampling ‣ APPENDIX D. Numerical integration of the posterior predictive distribution ‣ A Bayesian approach to out-of-sample network reconstruction") complements our illustration, showing both the shape of the numerically normalized posterior distribution corresponding to the week #​52\#52 of the year 20012001 and the evolution of the ‘slice-sampling’ chain across iterations.

## APPENDIX E. DATA DESCRIPTION

We employ transaction-level records from the Electronic Market for Interbank Deposits (eMID), a screen-based market for unsecured deposits [[35](https://arxiv.org/html/2602.21869v1#bib.bib35), [8](https://arxiv.org/html/2602.21869v1#bib.bib8), [36](https://arxiv.org/html/2602.21869v1#bib.bib36), [37](https://arxiv.org/html/2602.21869v1#bib.bib37)]. We restrict the analysis to overnight transactions, which account for the vast majority of activity on the platform. Our sample spans trading days from January 19991999 to September 20122012. Each trading day dd defines a weighted, directed matrix 𝐕​(d)\mathbf{V}(d) whose entry vi​j​(d)v\_{ij}(d) equals the total notional amount lent by bank ii to bank jj on day dd, with vi​i​(d)=0v\_{ii}(d)=0. Trading occurs exclusively on business days, so weekends and bank holidays are absent from the raw records.
Throughout the present work, data are aggregated at the weekly level. Weeks correspond to ISO calendar weeks (Monday to Sunday).

Let Δt\Delta\_{t} denote the set of trading days belonging to week tt. Since the number of business days varies across weeks, aggregation is performed over the set of trading days effectively observed within each window. Weekly weights are computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | vi​j(t)=∑d∈Δtvi​j​(d).v\_{ij}^{(t)}=\sum\_{d\in\Delta\_{t}}v\_{ij}(d). |  | (75) |

For each week tt, we restrict the node set to banks that are active during Δt\Delta\_{t}, i.e. involved in at least one transaction in that week. The number of active banks is, therefore, time-dependent. For example, during the period 19991999-20022002, the weekly number of active institutions ranges between 136136 and 197197, with an average close to 163163 banks per week.

Since empirical records are weighted and directed, we construct an undirected exposure matrix by symmetrizing weekly weights as

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi​j(t)=vi​j(t)+vj​i(t),i≠j,w\_{ij}^{(t)}=v\_{ij}^{(t)}+v\_{ji}^{(t)},\quad i\neq j, |  | (76) |

and define the corresponding binary adjacency matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | ai​j(t)=𝟙​{wi​j(t)>0},ai​i(t)=0,a\_{ij}^{(t)}=\mathbbm{1}\{w\_{ij}^{(t)}>0\},\quad a\_{ii}^{(t)}=0, |  | (77) |

so that, in matrix notation, 𝐀t=Θ​[𝐖t>0]\mathbf{A}\_{t}=\Theta[\mathbf{W}\_{t}>0] element-wise. Node strengths are computed from symmetrized weights as

|  |  |  |  |
| --- | --- | --- | --- |
|  | si(t)=∑j(≠i)wi​j(t)s\_{i}^{(t)}=\sum\_{j(\neq i)}w\_{ij}^{(t)} |  | (78) |

and are used as exogenous fitnesses informing the dcGM and related models.

## APPENDIX F. Marginal probability induced by the estimated prior

The key formula to carry out what we called ‘self-sustained’ inference reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ri​jt+1\displaystyle r\_{ij}^{t+1} | =∫0+∞(z​sit+1​sjt+11+z​sit+1​sjt+1)​P​(𝐐t|z)​π​(z)P​(𝐐t)​𝑑z=∫0+∞(z​sit+1​sjt+11+z​sit+1​sjt+1)​[∏i=1Nt∏j(>i)(z​sit​sjt)qi​jt1+z​sit​sjt]​π​(z)​𝑑z∫0+∞[∏i=1Nt∏j(>i)(z​sit​sjt)qi​jt1+z​sit​sjt]​π​(z)​𝑑z,\displaystyle=\int\_{0}^{+\infty}\left(\frac{zs\_{i}^{t+1}s\_{j}^{t+1}}{1+zs\_{i}^{t+1}s\_{j}^{t+1}}\right)\frac{P(\mathbf{Q}\_{t}|z)\pi(z)}{P(\mathbf{Q}\_{t})}dz=\frac{\int\_{0}^{+\infty}\left(\frac{zs\_{i}^{t+1}s\_{j}^{t+1}}{1+zs\_{i}^{t+1}s\_{j}^{t+1}}\right)\left[\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t}s\_{j}^{t}\right)^{q\_{ij}^{t}}}{1+zs\_{i}^{t}s\_{j}^{t}}\right]\pi(z)dz}{\int\_{0}^{+\infty}\left[\prod\_{i=1}^{N\_{t}}\prod\_{j(>i)}\frac{\left(zs\_{i}^{t}s\_{j}^{t}\right)^{q\_{ij}^{t}}}{1+zs\_{i}^{t}s\_{j}^{t}}\right]\pi(z)dz}, |  | (79) |

making it explicit that 𝐐t\mathbf{Q}\_{t} is employed as a prior to infer 𝐑t+1\mathbf{R}\_{t+1}. Figure [F.1](https://arxiv.org/html/2602.21869v1#Ax6.F1 "Figure F.1 ‣ APPENDIX F. Marginal probability induced by the estimated prior ‣ A Bayesian approach to out-of-sample network reconstruction") depicts the reliability of such a procedure in reproducing the ⟨TPR⟩\langle\text{TPR}\rangle, the ⟨PPV⟩\langle\text{PPV}\rangle, the ⟨TNR⟩\langle\text{TNR}\rangle and the ⟨ACC⟩\langle\text{ACC}\rangle across the weeks constituting our dataset. Both ‘self-sustained’ variants reproduce the evolution of the number of links over more than a decade of weekly eMID snapshots (2002-2012), despite receiving no topological information beyond that of the initial calibration period (19991999-20012001); within such a fully self-sustained regime, the BFM achieves a substantially higher accuracy in reproducing the degree sequence as well, whereas the BERM cannot account for degree heterogeneity.

![Refer to caption](x35.png)

![Refer to caption](x36.png)

![Refer to caption](x37.png)

![Refer to caption](x38.png)

Figure F.1: Top panels: evolution of the empirical (yellow) and expected (red) number of links, according to the BERM (left) and the BFM (right). Both ‘self-sustained’ variants reproduce the evolution of the number of links. Bottom panels: performance of the ‘self-sustained’ BERM (left) and BFM (right) in reproducing the ⟨TPR⟩\langle\text{TPR}\rangle, the ⟨PPV⟩\langle\text{PPV}\rangle, the ⟨TNR⟩\langle\text{TNR}\rangle and the ⟨ACC⟩\langle\text{ACC}\rangle across the weeks constituting our dataset. While both achieve a large ⟨ACC⟩\langle\text{ACC}\rangle score, driven by the large value of the ⟨TNR⟩\langle\text{TNR}\rangle, the BFM outperforms the BERM in achieving large ⟨TPR⟩\langle\text{TPR}\rangle and ⟨PPV⟩\langle\text{PPV}\rangle scores.