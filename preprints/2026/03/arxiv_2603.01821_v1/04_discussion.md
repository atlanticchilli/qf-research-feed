---
authors:
- Jonathan Klinge
- Maren Diane Schmeck
doc_id: arxiv:2603.01821v1
family_id: arxiv:2603.01821
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote
  1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research
  Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors
  thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments
  and fruitful discussions.
url_abs: http://arxiv.org/abs/2603.01821v1
url_html: https://arxiv.org/html/2603.01821v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jonathan Klinge


Maren Diane Schmeck

###### Abstract

We study a dynamic model of a non-life insurance portfolio. The foundation of the model is a compound Poisson process that represents the claims side of the insurer. To introduce clusters of claims appearing, e.g. with catastrophic events, this process is time-changed by a Lévy subordinator. The subordinator is chosen so that it evolves, on average, at the same speed as calendar time, creating a trade-off between intensity and severity.
We show that such a transformation always has a negative impact on the probability of ruin. Despite the expected total claim amount remaining invariant, it turns out that the probability of ruin as a function of the initial capital falls arbitrarily slowly depending on the choice of the subordinator.
  
  
Keywords: Cramér-Lundberg Model, Ruin-Theory, Subordination, Subexponential Distribution, Regular Variation
  
JEL Classification: G22, G33, Q54

## 1 Introduction

Insurers today face a wide range of risks that need to be modeled appropriately. On the one hand, there are individual risks and associated individual losses, such as vehicle damage covered by comprehensive motor insurance in the case of an accident. On the other hand, there are natural hazards such as hail, storms, or earthquakes. In these cases, the insurer records cumulative losses arising from many individual claims that occur simultaneously (e.g., hail damaging numerous vehicles at once). Due to climate change, natural catastrophes and their financial consequences have gained increasing relevance, making the modeling of cumulative risks more important than ever.
  
  
Cumulative losses caused by natural disasters have a substantial impact on the insurer’s probability of ruin, as they occur at a single point in time rather than being spread over the duration of the insurance contract, as is typical for independent individual losses. The magnitude of this risk depends not only on climatic conditions, but also on the insurer’s exposure concentration. Portfolios with high exposure to natural hazards and/or a strong geographical concentration are exposed to a higher cumulative risk.
  
  
In this paper, we construct a model that captures the effect of cumulative losses on the probability of ruin. We consider a compound Poisson process describing the insurer’s loss side and introduce a Lévy subordinator that acts as a stochastic time change of this process. This time change allows the base process to “jump” over certain periods, so that what are individual losses in ordinary time may cluster into a large aggregate loss in the time-changed process. The subordinated loss process therefore exhibits random clustering of individual claims. The model extends [[29](#bib.bib1 "A multivariate claim count model for applications in insurance")], though we focus on a different application.
The theory of subordination of Lévy processes has been introduced and studied in [[9](#bib.bib17 "Diffusion equation and stochastic processes")], [[10](#bib.bib16 "Harmonic analysis and the theory of probability")] and developed further. Rich sources on the theory of subordination are, for example, [[26](#bib.bib10 "Lévy processes and infinitely divisible distributions")], [[14](#bib.bib2 "Financial modelling with jump processes")], and [[2](#bib.bib15 "Lévy processes and stochastic calculus")].
Specifically, subordination of compound Poisson processes is examined in [[15](#bib.bib19 "Compound poisson process with a poisson subordinator")], and [[30](#bib.bib12 "Time-changed poisson processes of order k")].
  
  
The economic interpretation of the stochastic time change in our model is straightforward: a large jump of the subordinator corresponds to the occurrence of a major catastrophic event.
To ensure comparability between the subordinated process and the original compound Poisson process, we require the subordinator to run on average at the same speed as calendar time. Consequently, the expected value of the compound Poisson process remains unchanged under subordination. Subordination therefore acts purely as a random distortion of the claim arrival times. Mathematically, time normalization induces a trade-off between jump intensity and jump size such that the expected value remains invariant. In addition, we demonstrate that subordination invariably enlarges the jump size distribution of the compound Poisson process in the sense of stochastic dominance and that, through the clustering of individual jumps, subordination can transform light-tailed jump distributions into heavy-tailed ones. A detailed discussion of heavy-tailed distributions and their subclasses can be found in sources such as [[8](#bib.bib14 "Regular variation")], [[18](#bib.bib13 "An introduction to heavy-tailed and subexponential distributions")], and [[16](#bib.bib6 "Modelling extremal events: for insurance and finance")].
  
  
The paper is organized as follows.
First we show that the subordinated compound Poisson process is again a compound Poisson process with modified intensity and jump distribution. We derive conditions under which the modified jump distribution has light tails, allowing the application of classical Cramér-Lundberg arguments. Nevertheless, we demonstrate that the modified jump distribution always dominates the original distribution in the sense of first-order stochastic dominance. In the light-tailed case we prove, via the Adjustment Coefficient, that subordination asymptotically increases the ruin probability.
  
  
We then turn to the heavy-tailed case and identify conditions under which the modified jump distribution becomes heavy-tailed. Our analysis focuses on subexponential distributions, in particular those with regularly varying tails, and we derive conditions for the subordinated process to inherit these tail properties.
  
  
As mentioned above, several sources address the subordination of Lévy processes, particularly within the actuarial literature. A more recent development in this area is, for example, [[32](#bib.bib25 "Modeling stochastic mortality for joint lives through subordinators")], which studies the valuation of joint-life products and models mortality dependence via stochastically dependent subordinators.
  
Important sources on ruin theory and the Cramér-Lundberg model include, for example, [[25](#bib.bib36 "Stochastic processes for insurance and finance")], [[3](#bib.bib11 "Ruin probabilities")], and [[28](#bib.bib4 "Risk theory")].
  
Although ruin theory is a very old field, dating back to [[24](#bib.bib37 "I. approximerad framställning af sannolikhetsfunktionen. ii. aterförsäkring af kollektivrisker")], it remains an active area of contemporary research. Recent contributions include [[1](#bib.bib21 "Dividend corridors and a ruin constraint")], [[23](#bib.bib22 "Optimality of a refraction strategy in the optimal dividends problem with absolutely continuous controls subject to parisian ruin")], [[12](#bib.bib24 "Cumulative parisian ruin in finite and infinite time horizons for a renewal risk process with exponential claims")], [[20](#bib.bib23 "An excursion theoretic approach to parisian ruin problem")], [[21](#bib.bib32 "Eliciting claims development patterns and costs hidden in backlogs")] and [[33](#bib.bib33 "Ruin probabilities in an erlang risk model with dependence structure based on an independent gamma-distributed time window")]. In [[1](#bib.bib21 "Dividend corridors and a ruin constraint")], an optimal dividend problem is discussed under the condition that the probability of ruin remains sufficiently small. [[23](#bib.bib22 "Optimality of a refraction strategy in the optimal dividends problem with absolutely continuous controls subject to parisian ruin")], [[12](#bib.bib24 "Cumulative parisian ruin in finite and infinite time horizons for a renewal risk process with exponential claims")], and [[20](#bib.bib23 "An excursion theoretic approach to parisian ruin problem")] discuss a weakened concept of ruin, known as Parisian ruin, where ruin only occurs if the surplus process is negative for a sufficiently long period. This concept of ruin is analysed in both the Cramér-Lundberg model and the Sparre Andersen model. [[21](#bib.bib32 "Eliciting claims development patterns and costs hidden in backlogs")] analyzes a claims reservation problem with backlog, while [[33](#bib.bib33 "Ruin probabilities in an erlang risk model with dependence structure based on an independent gamma-distributed time window")] discusses ruin theory under dependency.
On recent research on the Cramér-Lundberg model [[4](#bib.bib26 "Experience rating in the cramér-lundberg model")] should be mentioned. Here, a Cramér-Lundberg model with unknown parameters is considered. [[11](#bib.bib27 "The cramér-lundberg model with a fluctuating number of clients")] analyzes a Cramér-Lundberg model in which the number of insureds is not constant, but each customer has a certain entry rate and random length to stay. Papers dealing specifically with Nat-Cat and Cat Bonds include [[17](#bib.bib39 "The diffusion of complex securities: the case of cat bonds")], [[13](#bib.bib38 "Classical solutions of the backward pide for markov modulated marked point processes and applications to cat bonds")], [[5](#bib.bib31 "Optimal control under uncertainty: application to the issue of cat bonds")], and [[22](#bib.bib30 "Robust indifference valuation of catastrophe bonds")].

## 2 Subordinated Compound Poisson Process

### 2.1   Model

We consider the following model. Let (Ω,ℱ,(ℱt)t∈[0,∞),ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\in[0,\infty)},\mathbb{P}) be a filtered probability space. Let (Nt)t≥0(N\_{t})\_{t\geq 0} be a standard Poisson process with intensity λ\lambda. The claim sizes XiX\_{i} for i∈ℕi\in\mathbb{N}, are independent and identically distributed positive random variables.
  
Consider the compound Poisson process

|  |  |  |
| --- | --- | --- |
|  | Ct=∑i=1NtXi,C\_{t}=\sum\_{i=1}^{N\_{t}}{X\_{i}}, |  |

with Lévy measure νC\nu\_{C} and distribution μt:=ℒ​(Ct|ℙ)\mu^{t}:=\mathcal{L}(C\_{t}|\mathbb{P}) at time t≥0t\geq 0. Additionally we define an independent univariate Lévy subordinator (Λt)t(\Lambda\_{t})\_{t} on (Ω,ℱ,(ℱt)t∈[0,∞),ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\in[0,\infty)},\mathbb{P}) with Lévy triplet (0,νΛ,bΛ)(0,\nu\_{\Lambda},b\_{\Lambda}).
Using these ingredients, we define the main object of our analysis, the subordinated compound Poisson process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt:=CΛt=∑i=1NΛtXi,t≥0.Y\_{t}:=C\_{\Lambda\_{t}}=\sum\_{i=1}^{N\_{\Lambda\_{t}}}X\_{i},\quad t\geq 0. |  | (1) |

  

The following graph (Figure [1](#S2.F1 "Figure 1 ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) provides an economic interpretation of the subordinated process. Due to the stochastic time change and in particular because the subordinator may exhibit jumps, several individual claims get clustered into a single cumulative jump of
(Yt)t≥0(Y\_{t})\_{t\geq 0}. Such a jump can be interpreted as a NatCat-type claim, representing a random aggregate of many underlying losses. The dotted lines describe the time jumps caused by the subordinator.

![Refer to caption](2603.01821v1/Trajectory_1_original_process.png)

![Refer to caption](2603.01821v1/Trajectory_2_Subordinator.png)

![Refer to caption](2603.01821v1/Trajectory_3_subordinated_process.png)

Figure 1: Trajectory of a subordinated compound Poisson process, subordinated by drifted
compound Poisson process

One should notice that (Yt)t≥0(Y\_{t})\_{t\geq 0} is not necessarily adapted to the Filtration (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0}. We therefore define the filtration (𝒢t)t≥0:=(ℱΛt)t≥0(\mathcal{G}\_{t})\_{t\geq 0}:=(\mathcal{F}\_{\Lambda\_{t}})\_{t\geq 0} to ensure that YtY\_{t} is 𝒢t\mathcal{G}\_{t}-measurable for every t∈[0,∞)t\in[0,\infty).
  
  
In this article, we restrict ourselves to Lévy subordinators that satisfy the time normalization condition 𝔼​[Λt]=t\mathbb{E}[\Lambda\_{t}]=t or equivalently 𝔼​[Λ1]=1\mathbb{E}[\Lambda\_{1}]=1. The motivation for this condition is that it ensures that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Yt]=𝔼​[Ct],t≥0,\mathbb{E}[Y\_{t}]=\mathbb{E}[C\_{t}],\quad t\geq 0, |  |

which follows immediately by conditioning. Therefore, the subordinated model remains directly comparable to the baseline model.
  
  
As a first step, we recall the Laplace transform of a Lévy subordinator Λ\Lambda. For any Lévy subordinator, it holds that for any t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​[Λt]​(u):=𝔼​[e−u​Λt]=e−t​ψΛ​(u),\mathcal{L}[\Lambda\_{t}](u):=\mathbb{E}[e^{-u\Lambda\_{t}}]=e^{-t\psi\_{\Lambda}(u)}, |  | (2) |

where the Laplace exponent is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψΛ​(u)=bΛ​u+∫(0,∞)(1−e−u​x)​νΛ​(d​x),u≥0,\psi\_{\Lambda}(u)=b\_{\Lambda}u+\int\_{(0,\infty)}(1-e^{-ux})\nu\_{\Lambda}(dx),\quad u\geq 0, |  | (3) |

for drift bΛb\_{\Lambda} and Lévy measure νΛ\nu\_{\Lambda}; see for instance [[7](#bib.bib3 "Lévy processes")].
  
From [[26](#bib.bib10 "Lévy processes and infinitely divisible distributions")] it is known that YY, as defined above, is again a Lévy process. In fact we show in the following, that YY is even a compound Poisson process, with explicitly known intensity and jump size distribution.
As we were unable to identify a formulation of this result in the literature that matches the compactness required for our purposes, we present it here together with a detailed proof. This result is of fundamental importance for the arguments developed in this paper.

###### Theorem 1.

The process (Yt)t≥0:=(CΛt)t≥0(Y\_{t})\_{t\geq 0}:=(C\_{\Lambda\_{t}})\_{t\geq 0}, defined in ([1](#S2.E1 "Equation 1 ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")), has a compound Poisson representation with intensity ψΛ​(λ)\psi\_{\Lambda}(\lambda) for the Laplace exponent ψΛ\psi\_{\Lambda} of Λ\Lambda and jump size distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | νY​(d​x)ψΛ​(λ),\frac{\nu\_{Y}(dx)}{\psi\_{\Lambda}(\lambda)}, |  | (4) |

where νY\nu\_{Y} is the Lévy measure of YY, which is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | νY​(d​x)=bΛ​νC​(d​x)+∫(0,∞)μt​(d​x)​νΛ​(d​t).\nu\_{Y}(dx)=b\_{\Lambda}\nu\_{C}(dx)+\int\_{(0,\infty)}\mu^{t}(dx)\nu\_{\Lambda}(dt). |  | (5) |

###### Proof.

By Lemma 2.2 in [[29](#bib.bib1 "A multivariate claim count model for applications in insurance")], we know that YY is a Lévy subordinator and has the characteristics

1. 1.

   bY=bΛ​bCb\_{Y}=b\_{\Lambda}b\_{C}
2. 2.

   νY​(B)=bΛ​νC​(B)+∫(0,∞)μt​(B)​νΛ​(d​t),∀B∈ℬ​(ℝ∖{0})\nu\_{Y}(B)=b\_{\Lambda}\nu\_{C}(B)+\int\_{(0,\infty)}{\mu^{t}(B)\nu\_{\Lambda}(dt)},\quad\forall B\in\mathcal{B}(\mathbb{R}\setminus\{0\}).

Here μt:=ℒ​(Ct|ℙ)\mu^{t}:=\mathcal{L}(C\_{t}|\mathbb{P}), for every t≥0t\geq 0. The quantities bΛb\_{\Lambda}, bYb\_{Y} and bCb\_{C} denote the drift of Λ\Lambda, YY and CC, respectively, while νΛ\nu\_{\Lambda}, νY\nu\_{Y} and νC\nu\_{C} denote their Lévy measures.
Since CC is a compound Poisson process, we know that bC=0b\_{C}=0 and therefore bY=0b\_{Y}=0. Hence, the characteristic exponent of the subordinator YY is given by

|  |  |  |
| --- | --- | --- |
|  | ΨY​(u)=∫0∞(ei​u​x−1)​νY​(d​x).\Psi\_{Y}(u)=\int\_{0}^{\infty}\left(e^{iux}-1\right)\nu\_{Y}(dx). |  |

To prove that YY is a compound Poisson process, we have to show that the measure νY\nu\_{Y} is finite. We get

|  |  |  |
| --- | --- | --- |
|  | ∫(0,∞)νY​(d​x)=νY​((0,∞))=bΛ​νC​((0,∞))+∫(0,∞)μt​((0,∞))​νΛ​(d​t).\int\_{(0,\infty)}{\nu\_{Y}(dx)}=\nu\_{Y}((0,\infty))={b\_{\Lambda}\nu\_{C}((0,\infty))}+\int\_{(0,\infty)}\mu^{t}((0,\infty))\nu\_{\Lambda}(dt). |  |

The first part of the addition is straightforward, since X1X\_{1} is positive and νC\nu\_{C} is the Lévy measure of the compound Poisson process CC, which is given by νC​(S)=λ​ℙ​[X1∈S]\nu\_{C}(S)=\lambda\mathbb{P}[X\_{1}\in S] for every S∈ℬ​(ℝ∖{0})S\in\mathcal{B}(\mathbb{R}\setminus\{0\}). Combining this with the second part of the sum, we get

|  |  |  |
| --- | --- | --- |
|  | ∫(0,∞)νY​(d​x)=bΛ​λ+∫0∞ℙ​[Cs>0]​νΛ​(d​s)=bΛ​λ+∫0∞(1−e−λ​s)​νΛ​(d​s)<∞.\int\_{(0,\infty)}{\nu\_{Y}(dx)}=b\_{\Lambda}\lambda+\int\_{0}^{\infty}{\mathbb{P}[C\_{s}>0]}\nu\_{\Lambda}(ds)=b\_{\Lambda}\lambda+\int\_{0}^{\infty}{(1-e^{-\lambda s})\nu\_{\Lambda}(ds)}<\infty. |  |

The finiteness follows from the inequality 1−e−λ​s≤min⁡{λ​s,1}1-e^{-\lambda s}\leq\min\{\lambda s,1\} for all s≥0s\geq 0, which is integrable with respect to νΛ\nu\_{\Lambda}, since Λ\Lambda is a Lévy subordinator. Moreover from the calculation we see that

|  |  |  |
| --- | --- | --- |
|  | ∫(0,∞)νY​(d​x)=ψΛ​(λ),\int\_{(0,\infty)}{\nu\_{Y}(dx)}=\psi\_{\Lambda}(\lambda), |  |

where ψΛ\psi\_{\Lambda} is the Laplace exponent of Λ\Lambda as defined in ([3](#S2.E3 "Equation 3 ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")).
  
Therefore, by normalizing νY\nu\_{Y}, we obtain that YY has characteristic exponent

|  |  |  |
| --- | --- | --- |
|  | ΨY​(u)=ψΛ​(λ)​∫(0,∞)(ei​u​x−1)​νYψΛ​(λ)​(d​x),\Psi\_{Y}(u)=\psi\_{\Lambda}(\lambda)\int\_{(0,\infty)}(e^{iux}-1)\frac{\nu\_{Y}}{\psi\_{\Lambda}(\lambda)}(dx), |  |

which proves that YY is a compound Poisson process with the characteristics specified in the theorem.
∎

Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.") shows that subordination of a compound Poisson process leads again to a compound Poisson process. In addition, the theorem provides the intensity and the severity distribution of the compound Poisson process YY, which can be read directly from its characteristic exponent.
  
For further analysis, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt:=∑i=1NΛtXi​=ℒ​∑j=1N~tZj,∀t>0,Y\_{t}:=\sum\_{i=1}^{N\_{\Lambda\_{t}}}X\_{i}\overset{\mathcal{L}}{=}\sum\_{j=1}^{\tilde{N}\_{t}}Z\_{j},\quad\forall t>0, |  | (6) |

where N~\tilde{N} is a standard Poisson process with intensity ψΛ​(λ)\psi\_{\Lambda}(\lambda), independent of ZjZ\_{j} for every j∈ℕj\in\mathbb{N}. The random variables (Zj)j∈ℕ(Z\_{j})\_{j\in\mathbb{N}} are independent and identically distributed, such that the distribution of Z1Z\_{1} is given by ([4](#S2.E4 "Equation 4 ‣ Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")). Moreover ψΛ\psi\_{\Lambda} is defined as in ([3](#S2.E3 "Equation 3 ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")).
For notational simplicity, we define X∼X1X\sim X\_{1} and write XX instead of X1X\_{1} for a independent copy of X1X\_{1}. Analogously, we define Z∼Z1Z\sim Z\_{1} and write ZZ instead of Z1Z\_{1} for an independent copy ZZ of Z1Z\_{1}.
The distribution of ZZ, as defined in ([4](#S2.E4 "Equation 4 ‣ Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) and ([5](#S2.E5 "Equation 5 ‣ Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) can be interpreted as a mixture distribution of individual jumps of XX and clustered jumps. The first summand in ([5](#S2.E5 "Equation 5 ‣ Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) therefore represents the individual jumps, which follow the distribution of XX, while the latter part represents the jumps clustered by subordination, since clustering can only occur in the case of a jump in Λ\Lambda.
  
Due to the non-explicit structure of the distribution of ZZ and the compound Poisson distribution μt\mu^{t}, there are very few examples in which the distribution of ZZ can be specified explicitly.
A very easy example is the following.

###### Example 1.

Define

|  |  |  |
| --- | --- | --- |
|  | Λt:=12​t+12​Kt,\Lambda\_{t}:=\frac{1}{2}t+\frac{1}{2}K\_{t}, |  |

where (Kt)t(K\_{t})\_{t} is a standard Poisson process with intensity 11. It is evident that Λ\Lambda is time-normalized. Denoting the distribution of ZZ by PZP\_{Z}, it is easy to calculate, that for any B∈ℬ​(ℝ∖{0})B\in\mathcal{B}(\mathbb{R}\setminus\{0\}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψΛ​(λ)​PZ​(B)=12​λ​ℙ​[X∈B]+μ12​(B),\psi\_{\Lambda}(\lambda)P\_{Z}(B)=\frac{1}{2}\lambda\mathbb{P}[X\in B]+\mu^{\frac{1}{2}}(B), |  | (7) |

as in this example, νΛ​(d​t)=𝟙12​(d​t)\nu\_{\Lambda}(dt)=\mathds{1}\_{\frac{1}{2}}(dt), which simplifies the integral in ([5](#S2.E5 "Equation 5 ‣ Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) drastically. In the above, ψΛ​(λ)=1+λ2−exp⁡(−λ2)\psi\_{\Lambda}(\lambda)=1+\frac{\lambda}{2}-\exp(-\frac{\lambda}{2}).
([7](#S2.E7 "Equation 7 ‣ Example 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) illustrates the structure of the distribution of ZZ. If the subordinator does not jump, the jump heights are distributed as XX, and the intensity is given by 12​λ\frac{1}{2}\lambda. If, on the other hand, the subordinator jumps, its jump height in our example is 1/21/2. This means that time jumps by a distance of 1/21/2, and therefore the clustered jump height has distribution μ12\mu^{\frac{1}{2}}, which happens on average once per unit of time. Hence, the distribution of ZZ can be interpreted as a mixed distribution of clustered and original jump heights.

### 2.2   Stochastic Dominance of Subordinated Jump Sizes

Heuristically, one may expect that a claim
ZZ is, in a certain sense, larger than a claim
XX, since
ZZ may involve the clustering of several smaller losses from the base process. We show that this is indeed the case in the following theorem.

###### Theorem 2.

|  |  |  |
| --- | --- | --- |
|  | X≺s​tZ,X\prec\_{st}Z, |  |

where ≺s​t\prec\_{st} denotes first-order stochastic dominance.

###### Proof.

Let y>0y>0, then

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Z>y]​=([4](#S2.E4 "Equation 4 ‣ Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."))​νY​((y,∞))ψΛ​(λ)=bΛ​νC​((y,∞))+∫(0,∞)μt​((y,∞))​νΛ​(d​t)ψΛ​(λ).\mathbb{P}[Z>y]\overset{(\ref{Zdistr})}{=}\frac{\nu\_{Y}((y,\infty))}{\psi\_{\Lambda}(\lambda)}=\frac{b\_{\Lambda}\nu\_{C}((y,\infty))+\int\_{(0,\infty)}\mu^{t}((y,\infty))\nu\_{\Lambda}(dt)}{\psi\_{\Lambda}(\lambda)}. |  |

Since CC is a compound Poisson process, with intensity λ\lambda,

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Z>y]=bΛ​λ​ℙ​[X>y]+∫(0,∞)μt​((y,∞))​νΛ​(d​t)ψΛ​(λ)\mathbb{P}[Z>y]=\frac{b\_{\Lambda}\lambda\mathbb{P}[X>y]+\int\_{(0,\infty)}\mu^{t}((y,\infty))\nu\_{\Lambda}(dt)}{\psi\_{\Lambda}(\lambda)} |  |

|  |  |  |
| --- | --- | --- |
|  | =bΛ​λ​ℙ​[X>y]+∫(0,∞)ℙ​[∑j=1NtXj>y]​νΛ​(d​t)ψΛ​(λ).=\frac{b\_{\Lambda}\lambda\mathbb{P}[X>y]+\int\_{(0,\infty)}\mathbb{P}[\sum\_{j=1}^{N\_{t}}X\_{j}>y]\nu\_{\Lambda}(dt)}{\psi\_{\Lambda}(\lambda)}. |  |

Obviously for any t≥0t\geq 0, {Nt≠0,X1>y}⊂{∑j=1NtXj>y}\{N\_{t}\neq 0,X\_{1}>y\}\subset\{\sum\_{j=1}^{N\_{t}}X\_{j}>y\}. Hence we obtain

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Z>y]≥bΛ​λ​ℙ​[X>y]+∫(0,∞)ℙ​[Nt≠0]​ℙ​[X>y]​νΛ​(d​t)ψΛ​(λ)\mathbb{P}[Z>y]\geq\frac{b\_{\Lambda}\lambda\mathbb{P}[X>y]+\int\_{(0,\infty)}\mathbb{P}[N\_{t}\neq 0]\mathbb{P}[X>y]\nu\_{\Lambda}(dt)}{\psi\_{\Lambda}(\lambda)} |  |

|  |  |  |
| --- | --- | --- |
|  | =bΛ​λ​ℙ​[X>y]+ℙ​[X>y]​∫(0,∞)(1−e−λ​t)​νΛ​(d​t)ψΛ​(λ).=\frac{b\_{\Lambda}\lambda\mathbb{P}[X>y]+\mathbb{P}[X>y]\int\_{(0,\infty)}(1-e^{-\lambda t})\nu\_{\Lambda}(dt)}{\psi\_{\Lambda}(\lambda)}. |  |

By the definition of the Laplace exponent, we know

|  |  |  |
| --- | --- | --- |
|  | =bΛ​λ​ℙ​[X>y]+ℙ​[X>y]​(ψΛ​(λ)−bΛ​λ)ψΛ​(λ)=ℙ​[X>y],=\frac{b\_{\Lambda}\lambda\mathbb{P}[X>y]+\mathbb{P}[X>y](\psi\_{\Lambda}(\lambda)-b\_{\Lambda}\lambda)}{\psi\_{\Lambda}(\lambda)}=\mathbb{P}[X>y], |  |

which provides the statement X≺s​tZX\prec\_{st}Z.
∎

The inequality used in the previous proof is very restrictive if the jump size XX admits a heavy-tailed distribution, because in that case the value CtC\_{t} is often triggered by a single large jump.

![Refer to caption](2603.01821v1/Jump_sizes_after_subord..jpg)


Figure 2: Jump size distribution after subordination

Figure [2](#S2.F2 "Figure 2 ‣ 2.2 Stochastic Dominance of Subordinated Jump Sizes ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.") illustrates the jump size distribution of a subordinated compound Poisson process.
The base process has intensity λ=1\lambda=1 and exponentially distributed jump sizes Xi∼E​x​p​(1)X\_{i}\sim Exp(1) for all i∈ℕi\in\mathbb{N}.
The Lévy subordinator is a compound Poisson process aswell, with drift bΛ=0.2b\_{\Lambda}=0.2, intensity λΛ=0.08\lambda\_{\Lambda}=0.08 and E​x​p​(0.1)Exp(0.1) distributed jump sizes.
Since the subordinator admits large jumps, the clustering effect of jumps in the base process is very strong.
As a result, comparing the jump size distribution of the base process and of the subordinated process, we see that the subordination causes a shift of the mass into the tail.
  
  
First-order stochastic dominance also allows direct conclusions to be drawn about the behaviour of risk measures. As shown in [[6](#bib.bib5 "Stochastic orders and risk measures: consistency and bounds")], first-order stochastic dominance implies that

|  |  |  |
| --- | --- | --- |
|  | ρ​(Z)≥ρ​(X)\rho(Z)\geq\rho(X) |  |

for every monotone and law-invariant risk measure ρ\rho.
  
Accordingly, an increase in risk can be observed under most relevant risk measures. On the other hand, the intensity of the new process is reduced. This interplay will be analysed later.

### 2.3   Heavy- and Light-Tailedness of ZZ

As a next step, we want to gain a deeper understanding of the distribution of ZZ and the effects of subordination to (Ct)t≥0(C\_{t})\_{t\geq 0}. Our goal is to understand the behaviour of the tail of ZZ and to derive conditions under which the jump size ZZ admits a light-tailed distribution. First of all, we compute the Laplace transform of YtY\_{t} for all t>0t>0. Since YY is a Lévy process, it suffices to calculate the Laplace transform of Y1Y\_{1}, which fully characterizes the Laplace transform of the entire process YY.

###### Lemma 1.

The Laplace transform ΨY1\Psi\_{Y\_{1}} of Y1Y\_{1} is given by

|  |  |  |
| --- | --- | --- |
|  | ΨY1​(u)=exp⁡(−ψΛ​(λ​[1−ΨX​(u)])),u≥0\Psi\_{Y\_{1}}(u)=\exp(-\psi\_{\Lambda}(\lambda[1-\Psi\_{X}(u)])),\quad u\geq 0 |  |

where ψΛ\psi\_{\Lambda} is defined as in ([2](#S2.E2 "Equation 2 ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) and ΨX\Psi\_{X} is the Laplace transform of jump size XX.

###### Proof.

Denote the σ\sigma-algebra σ​(Λt,t≥0)\sigma(\Lambda\_{t},t\geq 0) by σ​(Λ)\sigma(\Lambda).
For all u≥0u\geq 0

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΨY1​(u)=𝔼​[exp⁡(−u​CΛ1)]=𝔼​[𝔼​[exp⁡(−u​CΛ1)|σ​(Λ)]]=𝔼​[exp⁡(λ​Λ1​[ΨX​(u)−1])],\Psi\_{Y\_{1}}(u)=\mathbb{E}[\exp(-uC\_{\Lambda\_{1}})]=\mathbb{E}[\mathbb{E}[\exp(-uC\_{\Lambda\_{1}})|\sigma(\Lambda)]]=\mathbb{E}[\exp(\lambda\Lambda\_{1}[\Psi\_{X}(u)-1])], |  | (8) |

where ΨX​(u):=𝔼​[exp⁡(−u​X)]\Psi\_{X}(u):=\mathbb{E}[\exp(-uX)]. Observe that λ​[ΨX​(u)−1]≤0\lambda[\Psi\_{X}(u)-1]\leq 0 for all u≥0u\geq 0, hence we write ([8](#S2.E8 "Equation 8 ‣ Proof. ‣ 2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) as

|  |  |  |
| --- | --- | --- |
|  | =exp⁡(−ψΛ​(λ​[1−ΨX​(u)])).=\exp(-\psi\_{\Lambda}(\lambda[1-\Psi\_{X}(u)])). |  |

∎

Since YY is a Lévy process, we can conclude immediately, that for any t>0t>0

|  |  |  |
| --- | --- | --- |
|  | ΨYt​(u)=exp⁡(−t​ψΛ​(λ​[1−ΨX​(u)])),∀u>0.\Psi\_{Y\_{t}}(u)=\exp(-t\psi\_{\Lambda}(\lambda[1-\Psi\_{X}(u)])),\quad\forall u>0. |  |

As already mentioned in the introduction of this section, we want to analyze the tail behaviour of Y1Y\_{1} and ZZ respectively.
A very common definition for the presence of heavy tails of a given distribution is the non-existence of the moment-generating function at a point u>0u>0. In other words, the presence of heavy tails is defined by the divergence of the Laplace transform at a point u<0u<0. This definition of heavy-tailedness is also used in [[29](#bib.bib1 "A multivariate claim count model for applications in insurance")] and defined for example in Definition 2.2 in [[18](#bib.bib13 "An introduction to heavy-tailed and subexponential distributions")].

###### Definition 1.

A distribution FF on ℝ\mathbb{R} is said to be (right-) heavy-tailed if

|  |  |  |
| --- | --- | --- |
|  | ∫−∞∞eu​x​F​(d​x)=∞,∀u>0.\int\_{-\infty}^{\infty}e^{ux}F(dx)=\infty,\quad\forall u>0. |  |

that is, if FF fails to possess any positive exponential moment.

Throughout the paper, we extend the Laplace exponent defined in ([3](#S2.E3 "Equation 3 ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) to negative arguments whenever this is well defined. In this case, evaluating the Laplace exponent at negative values corresponds to considering exponential moments, i.e. the moment-generating function.
We now formulate the criterion for heavy-tailedness of the distribution of Y1Y\_{1}.

###### Lemma 2.

The distribution of Y1Y\_{1} is heavy-tailed, if and only if the distribution of Λ1\Lambda\_{1} or of XX is heavy-tailed.

###### Proof.

Let u>0u>0. Then, if it exists, the moment-generating function MY1M\_{Y\_{1}} of Y1Y\_{1} can be derived from the Laplace transform of Y1Y\_{1} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | MY1​(u)=exp⁡(−ψΛ​(λ​[1−MX​(u)])),M\_{Y\_{1}}(u)=\exp(-\psi\_{\Lambda}(\lambda[1-M\_{X}(u)])), |  | (9) |

where MXM\_{X} is the moment generating function of XX. For u>0u>0, λ​[1−MX​(u)]\lambda[1-M\_{X}(u)] maps surjectively onto (−∞,0)(-\infty,0), therefore if the distribution of Λ1\Lambda\_{1} is heavy-tailed, i.e. ψΛ​(x)=−∞\psi\_{\Lambda}(x)=-\infty for every x<0x<0, it follows that MY1​(u)=∞M\_{Y\_{1}}(u)=\infty for any u>0u>0, which shows that Y1Y\_{1} is heavy-tailed.
  
On the other hand, let u>0u>0, by ([9](#S2.E9 "Equation 9 ‣ Proof. ‣ 2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) it follows immediately that if XX admits a heavy-tailed distribution, MX​(u)=∞M\_{X}(u)=\infty for any u>0u>0 and so MY1​(u)=∞M\_{Y\_{1}}(u)=\infty, which means that Y1Y\_{1} is heavy-tailed.
  
The other direction of the theorem follows by very similar arguments. Suppose that MY1​(u)=∞M\_{Y\_{1}}(u)=\infty for every u>0u>0. This implies that −ψΛ​(λ​[1−MX​(u)])=∞-\psi\_{\Lambda}(\lambda[1-M\_{X}(u)])=\infty for every u>0u>0. There are two ways this could happen. First, if ψΛ​(u)=−∞\psi\_{\Lambda}(u)=-\infty for every u<0u<0, which implies that 𝔼​[e−u​Λ1]=∞\mathbb{E}[e^{-u\Lambda\_{1}}]=\infty for every u<0u<0, so Λ1\Lambda\_{1} admits a heavy-tailed distribution. Second option is that λ​[1−MX​(u)]=−∞\lambda[1-M\_{X}(u)]=-\infty for any u>0u>0, which immediately implies, that MX​(u)=∞M\_{X}(u)=\infty for every u>0u>0 and therefore XX admits a heavy-tailed distribution.
  
This completes the proof.
∎

The previous proof is similar to the proof of Proposition 2.2 in [[29](#bib.bib1 "A multivariate claim count model for applications in insurance")].
Since YY is a Lévy process, the statement of the preceding lemma extends to all t∈ℝt\in\mathbb{R}.
From the theorem of the previous section, we know that the subordinated process (Yt)t:=(∑k=1NΛtXk)t(Y\_{t})\_{t}:=(\sum\_{k=1}^{N\_{\Lambda\_{t}}}X\_{k})\_{t} has a compound Poisson representation

|  |  |  |
| --- | --- | --- |
|  | Yt∼∑j=1Nt~Zj.Y\_{t}\sim\sum\_{j=1}^{\tilde{N\_{t}}}Z\_{j}. |  |

Hence, the previous lemma provides that ZZ possesses a heavy-tailed distribution if and only if XX or Λ1\Lambda\_{1} has a heavy-tailed distribution, which can be seen through standard arguments as in the proof before.
Moreover, from the results of the preceding section we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z∼νYψΛ​(λ),Z\sim\frac{\nu\_{Y}}{\psi\_{\Lambda}(\lambda)}, |  | (10) |

with νY\nu\_{Y} as in ([5](#S2.E5 "Equation 5 ‣ Theorem 1. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")).

## 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes

In risk theory, when the jumps of the compound Poisson process have light tails, the adjustment coefficient becomes a crucial parameter for quantifying the probability of ruin.
We define the subordinated Cramér-Lundberg model via

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt:=u+c​t−Yt,t≥0.P\_{t}:=u+ct-Y\_{t},\quad t\geq 0. |  | (11) |

As shown above, (Yt)t≥0(Y\_{t})\_{t\geq 0} is again a compound Poisson process, such that the structure in the subordinated Cramér-Lundberg model and the structure in the standard Cramér-Lundberg model is kept the same. In ([11](#S3.E11 "Equation 11 ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")), uu denotes the initial capital, cc is the premium rate and YtY\_{t} models the claims side of the insurer.
  
Throughout the whole paper, we assume that the premium rate cc fulfills the net profit condition, i.e.
  
c>𝔼​[Y1]=ψΛ​(λ)​𝔼​[Z]=λ​𝔼​[X1]c>\mathbb{E}[Y\_{1}]=\psi\_{\Lambda}(\lambda)\mathbb{E}[Z]=\lambda\mathbb{E}[X\_{1}] (see, e.g., [[28](#bib.bib4 "Risk theory")]). Note that the net profit condition depends only on the expectation of YtY\_{t}. Consequently, it remains invariant under subordination with respect to a time-normalized subordinator. This means that the insurer’s fair premium remains unaffected by the subordination.
  
Our main interest in this article lies in the quantification of the ruin probability of the surplus process (Pt)t≥0(P\_{t})\_{t\geq 0}. Formally, this means quantifying the exit probability

|  |  |  |
| --- | --- | --- |
|  | ΨP​(u):=ℙ​[inft>0Pt​<0|​P0=u].\Psi\_{P}(u):=\mathbb{P}\left[\inf\_{t>0}P\_{t}<0|P\_{0}=u\right]. |  |

  

For the main result of this section, we require the following lemma, which shows that the Laplace exponent of a time-normalized Lévy subordinator always lies below the bisector.

###### Lemma 3.

Let (Λt)t(\Lambda\_{t})\_{t} be a time-normalized Lévy subordinator (i.e., 𝔼[Λ1]=1)\mathbb{E}[\Lambda\_{1}]=1), then ψΛ​(u)≤u\psi\_{\Lambda}(u)\leq u for any u∈ℝ+u\in\mathbb{R}\_{+}. Moreover, if ψΛ​(−s)\psi\_{\Lambda}(-s) exists for s>0s>0, then also ψΛ​(−s)≤−s\psi\_{\Lambda}(-s)\leq-s.

###### Proof.

Let (Λt)t(\Lambda\_{t})\_{t} be a time-normalized Lévy subordinator, the Laplace exponent of Λ\Lambda is given by

|  |  |  |
| --- | --- | --- |
|  | ψΛ​(u)=bΛ​u+∫0∞(1−e−u​x)​νΛ​(d​x).\psi\_{\Lambda}(u)=b\_{\Lambda}u+\int\_{0}^{\infty}(1-e^{-ux})\nu\_{\Lambda}(dx). |  |

By the time normalization condition 𝔼​[Λ1]=1\mathbb{E}[\Lambda\_{1}]=1, it holds that

|  |  |  |
| --- | --- | --- |
|  | 1=bΛ+∫0∞x​νΛ​(d​x).1=b\_{\Lambda}+\int\_{0}^{\infty}x\nu\_{\Lambda}(dx). |  |

Therefore we get for u≥0u\geq 0

|  |  |  |
| --- | --- | --- |
|  | ψΛ​(u)=bΛ​u+∫0∞(1−e−u​x)​νΛ​(d​x)≤bΛ​u+∫0∞u​x​ν​(d​x)=u​(bΛ+∫0∞x​νΛ​(d​x))=u.\psi\_{\Lambda}(u)=b\_{\Lambda}u+\int\_{0}^{\infty}(1-e^{-ux})\nu\_{\Lambda}(dx)\leq b\_{\Lambda}u+\int\_{0}^{\infty}ux\nu(dx)=u\left(b\_{\Lambda}+\int\_{0}^{\infty}x\nu\_{\Lambda}(dx)\right)=u. |  |

Suppose that ψΛ​(−s)\psi\_{\Lambda}(-s) exists for s>0s>0, then we can perform the same steps, to show that ψΛ​(−s)≤−s\psi\_{\Lambda}(-s)\leq-s, which proves the statement.
∎

The previous Lemma confirms what one would expect. As we know, the subordinated process YY has a compound Poisson representation with intensity ψΛ​(λ)\psi\_{\Lambda}(\lambda), where λ\lambda is the intensity of the base process CC. The lemma therefore implies that the intensity of YY is lower, than the intensity of CC, i.e. 𝔼​[N~1]≤𝔼​[N1]\mathbb{E}[\tilde{N}\_{1}]\leq\mathbb{E}[N\_{1}], which is a consequence of the clustering in the subordinated process. Moreover the lemma will be useful for the upcoming theorem.

We consider the Cramér-Lundberg process (Pt)t≥0(P\_{t})\_{t\geq 0} as described in ([11](#S3.E11 "Equation 11 ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) and compare PP to the initial risk model

|  |  |  |
| --- | --- | --- |
|  | St:=u+c​t−∑k=1NtXk=u+c​t−Ct.S\_{t}:=u+ct-\sum\_{k=1}^{N\_{t}}X\_{k}=u+ct-C\_{t}. |  |

Here, the time normalization of Λ\Lambda plays a crucial role when comparing PP and SS, since the expected total claim amount remains invariant under time-normalized subordination.
  
In the case of light-tailed jump sizes, classical Cramér-Lundberg theory applies (cf. [[28](#bib.bib4 "Risk theory")], Sections 5.5 and 5.6). We now assume that the moment-generating function of XX and Λ1\Lambda\_{1} exists on a sufficiently large domain. According to Lemma [2](#Thmlem2 "Lemma 2. ‣ 2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."), standard Cramér-Lundberg theory can therefore be applied.
Let MXM\_{X} and MZM\_{Z} be the moment-generating functions of XX and ZZ, respectively. We write RR for the non-trivial solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ​(r)=λ​(MX​(r)−1)−c​r=0\Theta(r)=\lambda\left(M\_{X}(r)-1\right)-cr=0 |  | (12) |

and RΛR\_{\Lambda} for the non-trivial solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΘΛ​(r)=ψΛ​(λ)​(MZ​(r)−1)−c​r=0.\Theta\_{\Lambda}(r)=\psi\_{\Lambda}(\lambda)(M\_{Z}(r)-1)-cr=0. |  | (13) |

Θ\Theta and ΘΛ\Theta\_{\Lambda} are the so-called adjustment functions of the respective Cramér-Lundberg process.
The trivial solutions are obviously given for r=0r=0.
Assuming that the adjustment coefficients RR and RΛR\_{\Lambda} exist and MX′​(R),MZ′​(RΛ)<∞M\_{X}^{\prime}(R),M\_{Z}^{\prime}(R\_{\Lambda})<\infty, by Theorem 5.5 in [[28](#bib.bib4 "Risk theory")], we know that the ruin probability ΨS\Psi\_{S} and ΨP\Psi\_{P} of SS and PP have the asymptotics

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΨS​(u)∼c−λ​𝔼​[X]λ​MX′​(R)−c​e−R​u;ΨP​(u)∼c−λ​𝔼​[X]ψΛ​(λ)​MZ′​(RΛ)−c​e−RΛ​u,u→∞,\Psi\_{S}(u)\sim\frac{c-\lambda\mathbb{E}[X]}{\lambda M\_{X}^{\prime}(R)-c}e^{-Ru};\quad\Psi\_{P}(u)\sim\frac{c-\lambda\mathbb{E}[X]}{\psi\_{\Lambda}(\lambda)M\_{Z}^{\prime}(R\_{\Lambda})-c}e^{-R\_{\Lambda}u},\quad u\to\infty, |  | (14) |

where uu is the initial capital in the portfolio.
We formulate the following.

###### Lemma 4.

Suppose that the moment-generating function of XX exists on [0,x)[0,x). Moreover the moment-generating function of Λ1\Lambda\_{1} exists on [0,l)[0,l), then the moment-generating function of ZZ exists on [0,x∧(λ​[MX​(x)−1]∧l))\left[0,x\wedge(\lambda[M\_{X}(x)-1]\wedge l)\right) and is given by

|  |  |  |
| --- | --- | --- |
|  | MZ​(r)=1−ψΛ​(λ​[1−MX​(r)])ψΛ​(λ).M\_{Z}(r)=1-\frac{\psi\_{\Lambda}\left(\lambda[1-M\_{X}(r)]\right)}{\psi\_{\Lambda}(\lambda)}. |  |

###### Proof.

The existence follows immediately from Lemma [2](#Thmlem2 "Lemma 2. ‣ 2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
From Lemma [1](#Thmlem1 "Lemma 1. ‣ 2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.") we derive, that the moment-generating function of Y1Y\_{1} is given by

|  |  |  |
| --- | --- | --- |
|  | MY1​(r)=exp⁡(−ψΛ​(λ​[1−MX​(r)])).M\_{Y\_{1}}(r)=\exp(-\psi\_{\Lambda}\left(\lambda[1-M\_{X}(r)]\right)). |  |

On the other hand, by the compound Poisson representation of YY, we know that

|  |  |  |
| --- | --- | --- |
|  | MY1​(r)=exp⁡(ψΛ​(λ)​[MZ​(r)−1]).M\_{Y\_{1}}(r)=\exp\left(\psi\_{\Lambda}(\lambda)[M\_{Z}(r)-1]\right). |  |

If the moment-generating function exists in some neighbourhood of 0, it uniquely determines the distribution. Therefore we can combine the two equations and conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | MZ​(r)=1−ψΛ​(λ​[1−MX​(r)])ψΛ​(λ).M\_{Z}(r)=1-\frac{\psi\_{\Lambda}\left(\lambda[1-M\_{X}(r)]\right)}{\psi\_{\Lambda}(\lambda)}. |  | (15) |

The restriction to the interval [0,x∧(λ​[MX​(x)−1]∧l))\left[0,x\wedge(\lambda[M\_{X}(x)-1]\wedge l)\right) follows by ([15](#S3.E15 "Equation 15 ‣ Proof. ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")).
∎

Now we are able to prove the following statement for the light-tailed case. From the following result we can derive the asymptotic behaviour of the ruin probability explicitly.

###### Theorem 3.

Suppose that the adjustment coefficient RR of (St)t≥0(S\_{t})\_{t\geq 0} exists. Let Λ\Lambda be a time-normalized Lévy subordinator, s.t. the adjustment coefficient RΛR\_{\Lambda} for (Pt)t≥0(P\_{t})\_{t\geq 0} exists. Then

|  |  |  |
| --- | --- | --- |
|  | RΛ≤R.R\_{\Lambda}\leq R. |  |

###### Proof.

By ([12](#S3.E12 "Equation 12 ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) the adjustment-equation of RR is given by

|  |  |  |
| --- | --- | --- |
|  | Θ​(r)=λ​(MX​(r)−1)−c​r=0.\Theta(r)=\lambda(M\_{X}(r)-1)-cr=0. |  |

By the previous Lemma and ([13](#S3.E13 "Equation 13 ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")), the adjustment equation associated to PP is given by

|  |  |  |
| --- | --- | --- |
|  | ΘΛ​(r)=−ψΛ​(λ​[1−MX​(r)])−c​r=0.\Theta\_{\Lambda}(r)=-\psi\_{\Lambda}(\lambda[1-M\_{X}(r)])-cr=0. |  |

By Lemma [3](#Thmlem3 "Lemma 3. ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.") it follows, that

|  |  |  |
| --- | --- | --- |
|  | ΘΛ​(r)=−ψΛ​(λ​[1−MX​(r)])−c​r≥−λ​(1−MX​(r))−c​r=λ​(MX​(r)−1)−c​r=Θ​(r).\Theta\_{\Lambda}(r)=-\psi\_{\Lambda}(\lambda[1-M\_{X}(r)])-cr\geq-\lambda(1-M\_{X}(r))-cr=\lambda(M\_{X}(r)-1)-cr=\Theta(r). |  |

It holds, that Θ​(0)=ΘΛ​(0)=0\Theta(0)=\Theta\_{\Lambda}(0)=0. Moreover by the existence of the adjustment coefficient, Θ​(R)=ΘΛ​(RΛ)=0\Theta(R)=\Theta\_{\Lambda}(R\_{\Lambda})=0.
By convexity of Θ\Theta and ΘΛ\Theta\_{\Lambda} (see for example [[28](#bib.bib4 "Risk theory")]) it follows, that RΛ≤RR\_{\Lambda}\leq R with strict inequality unless Λ\Lambda is deterministic.
∎

The theorem shows, that in the subordinated model, the ruin probability ΨP​(u)\Psi\_{P}(u) as a function of the initial capital always decays slower than the ruin probability ΨS​(u)\Psi\_{S}(u) in the initial model. The time normalization here is crucial for ensuring comparability of these two models, as it preserves the expected value of both processes.

![Refer to caption](2603.01821v1/Images/Adjustment_Function_subordinate.png)


Figure 3: The adjustment function for different subordinators

Figure [3](#S3.F3 "Figure 3 ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.") shows the adjustment functions for various time-normalized subordinators. As the base compound Poisson process, we have chosen the intensity λ=2\lambda=2 and exponentially distributed jump heights Xi∼E​x​p​(2)X\_{i}\sim Exp(2). The premium rate is set to c=2.5c=2.5, which clearly satisfies the net profit condition. All considered subordinators are compound Poisson processes with different intensities λΛ\lambda\_{\Lambda}. For simplicity, the jump sizes in the subordinator are also chosen to be exponentially distributed. Due to time normalization, the parameter of the exponentially distributed jump heights in the subordinator are therefore λΛ\lambda\_{\Lambda} as well. As shown in the previous theorem, the non-trivial zero points of the adjustment functions after subordination lie to the left of those of the base process. This implies that the decay of the ruin probability in the subordinated model is significantly slower than the decay of the ruin probability in the initial model (cf. ([14](#S3.E14 "Equation 14 ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."))).

## 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes

The following section is devoted to the case in which the subordinated process has a heavy-tailed jump size distribution. As established in Theorem [2](#Thmlem2 "Lemma 2. ‣ 2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."), this case occurs if we start with heavy-tailed jump size distributions or if the subordinator has a heavy-tailed infinitely divisible distribution. In this chapter, we focus mainly on the class of subexponential distributions. Subexponentiality offers the advantage that in certain situations the asymptotics of the ruin probability can still be quantified well. Particular attention is given to the class of distributions with regularly varying tails, for which Karamata’s Theorem yields explicit asymptotics of the ruin probability. Classical Cramér-Lundberg theory is no longer applicable in this context, since the jump heights lack exponential moments and, consequently, the moment-generating function is not defined.
  
  
We begin by recalling some basic definitions used throughout this section.
For any cumulative distribution function GG with G​(0)=0G(0)=0, we denote by G¯\overline{G} its right tail and for n∈ℕn\in\mathbb{N}, we write G∗nG^{\*n} for the nn-fold convolution of GG.

### 4.1   Preliminary Definitions

###### Definition 2.

A distribution FF with support (0,∞)(0,\infty) is called subexponential, if for all n≥2n\geq 2,

|  |  |  |
| --- | --- | --- |
|  | limx→∞F∗n¯​(x)F¯​(x)=n.\lim\_{x\to\infty}\frac{\overline{F^{\*n}}(x)}{\overline{F}(x)}=n. |  |

We denote the class of subexponential distributions by 𝒮\mathcal{S}.

Another very important definition for this chapter is the following.

###### Definition 3.

1. 1.

   A positive, Lebesgue measurable function LL on (0,∞)(0,\infty) is slowly varying (at ∞\infty) if

   |  |  |  |
   | --- | --- | --- |
   |  | limx→∞L​(t​x)L​(x)= 1,t>0.\lim\_{x\to\infty}\frac{L(t\,x)}{L(x)}\;=\;1,\quad t>0. |  |
2. 2.

   A positive, Lebesgue measurable function hh on (0,∞)(0,\infty) is regularly varying (at ∞\infty) of index α∈ℝ\alpha\in\mathbb{R} if

   |  |  |  |
   | --- | --- | --- |
   |  | limx→∞h​(t​x)h​(x)=tα,t>0.\lim\_{x\to\infty}\frac{h(t\,x)}{h(x)}\;=\;t^{\alpha},\quad t>0. |  |

Clearly, the case of a slowly varying function corresponds to a regularly varying function with the index α=0\alpha=0.
In the following, the cumulative distribution function of Λ1\Lambda\_{1} is denoted by FΛ1F\_{\Lambda\_{1}} and analogously the CDF of XX is denoted by FXF\_{X}, where XX and Λ1\Lambda\_{1} are defined as before. We also write F¯Λ1\overline{F}\_{\Lambda\_{1}} and F¯X\overline{F}\_{X} for the corresponding right tails, i.e.

|  |  |  |
| --- | --- | --- |
|  | F¯Λ1​(x):=1−FΛ1​(x),F¯X​(x):=1−FX​(x).\overline{F}\_{\Lambda\_{1}}(x):=1-F\_{\Lambda\_{1}}(x),\quad\overline{F}\_{X}(x):=1-F\_{X}(x). |  |

Our interest lies in the class of distribution functions whose tail F⋅¯\overline{F\_{\cdot}} is a regularly varying function with some index −α<0-\alpha<0. As shown in [[16](#bib.bib6 "Modelling extremal events: for insurance and finance")], distributions with this property belong to the class 𝒮\mathcal{S}.
In the following, we write f​(x)∼g​(x)f(x)\sim g(x) for functions ff and gg, if

|  |  |  |
| --- | --- | --- |
|  | limx→∞f​(x)g​(x)=1.\lim\_{x\to\infty}\frac{f(x)}{g(x)}=1. |  |

### 4.2   Subexponential Initial Jump Size

First, we consider the case where the subordinator has a light-tailed distribution and XX is subexponential.

###### Theorem 4.

Suppose that Λ1\Lambda\_{1} is time-normalized and light-tailed. Moreover ℒ​(X|ℙ)∈𝒮\mathcal{L}(X|\mathbb{P})\in\mathcal{S}. Then Z∈𝒮Z\in\mathcal{S} and

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Z>x]∼λψΛ​(λ)​ℙ​[X>x].\mathbb{P}[Z>x]\sim\frac{\lambda}{\psi\_{\Lambda}(\lambda)}\mathbb{P}[X>x]. |  |

###### Proof.

Let t>0t>0, ε>0\varepsilon>0. We calculate the expectation

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[eε​NΛt]=𝔼​[𝔼​[eε​NΛt|σ​(Λt)]].\mathbb{E}[e^{\varepsilon N\_{\Lambda\_{t}}}]=\mathbb{E}[\mathbb{E}[e^{\varepsilon N\_{\Lambda\_{t}}}|\sigma(\Lambda\_{t})]]. |  |

Since NN is a standard Poisson process we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | =𝔼​[eλ​Λt​(eε−1)].=\mathbb{E}[e^{\lambda\Lambda\_{t}(e^{\varepsilon}-1)}]. |  | (16) |

Since Λt\Lambda\_{t} is light-tailed for any t≥0t\geq 0, we can choose
ε>0\varepsilon>0 sufficiently small so that the expression in
([16](#S4.E16 "Equation 16 ‣ Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) is finite. Hence NΛtN\_{\Lambda\_{t}} is light-tailed for any t≥0t\geq 0.
  
By Theorem 1 in [[27](#bib.bib7 "Compound sums and subexponentiality")] it follows that for any t>0t>0, the distribution of Yt:=∑i=1NΛtXiY\_{t}:=\sum\_{i=1}^{N\_{\Lambda\_{t}}}X\_{i} belongs to 𝒮\mathcal{S}.
  
Moreover by [[27](#bib.bib7 "Compound sums and subexponentiality")], for x>0,x>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[Yt>x]=ℙ​[∑i=1NΛtXi>x]∼λ​t​ℙ​[X>x].\mathbb{P}[Y\_{t}>x]=\mathbb{P}[\sum\_{i=1}^{N\_{\Lambda\_{t}}}X\_{i}>x]\sim\lambda t\mathbb{P}[X>x]. |  | (17) |

By ([6](#S2.E6 "Equation 6 ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) and Theorem A.3.19. in [[16](#bib.bib6 "Modelling extremal events: for insurance and finance")] it also follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[Yt>x]ℙ​[Z>x]∼ψΛ​(λ)​t.\frac{\mathbb{P}[Y\_{t}>x]}{\mathbb{P}[Z>x]}\sim\psi\_{\Lambda}(\lambda)t. |  | (18) |

Combining ([17](#S4.E17 "Equation 17 ‣ Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) and ([18](#S4.E18 "Equation 18 ‣ Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[Z>x]∼λψΛ​(λ)​ℙ​[X>x].\mathbb{P}[Z>x]\sim\frac{\lambda}{\psi\_{\Lambda}(\lambda)}\mathbb{P}[X>x]. |  | (19) |

By X∈𝒮X\in\mathcal{S}, ([19](#S4.E19 "Equation 19 ‣ Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")), and Lemma A3.15 in [[16](#bib.bib6 "Modelling extremal events: for insurance and finance")] it follows that Z∈𝒮Z\in\mathcal{S},
which proves the statement.
∎

Equation ([19](#S4.E19 "Equation 19 ‣ Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.")) admits a very natural interpretation: on average, λψΛ​(λ)\frac{\lambda}{\psi\_{\Lambda}(\lambda)} claims of the original compound Poisson process with jump size XX are aggregated into a single jump in the subordinated compound Poisson process, whose jump size is ZZ.

### 4.3   Regularly Varying Subordinator

In this subsection we use a Lévy subordinator Λ\Lambda, such that FΛ1¯\overline{F\_{\Lambda\_{1}}} is regularly varying. Due to time normalization, it is necessary that the index −ρ-\rho of the regularly varying tail is smaller than −1-1 to ensure that the expected value of Λ1\Lambda\_{1} exists. We formulate the following.

###### Theorem 5.

Let Λ\Lambda be a time-normalized Lévy subordinator, s.t. FΛ1¯\overline{F\_{\Lambda\_{1}}} is regularly varying with index −ρ<−1-\rho<-1, i.e. FΛ1¯​(x)∼x−ρ​L​(x)\overline{F\_{\Lambda\_{1}}}(x)\sim x^{-\rho}L(x), for some slowly varying LL. Furthermore let FX¯​(x)∈o​(x−ρ​L​(x))\overline{F\_{X}}(x)\in o(x^{-\rho}L(x)), then FZ¯\overline{F\_{Z}} is regularly varying with index −ρ-\rho.

###### Proof.

It holds that for x∈ℕx\in\mathbb{N}

|  |  |  |
| --- | --- | --- |
|  | ℙ​[NΛ1=x]=∫0∞ℙ​[Nr=x]​𝑑FΛ1​(r)=∫0∞(λ​r)xx!​e−λ​r​𝑑FΛ1​(r).\mathbb{P}[N\_{\Lambda\_{1}}=x]=\int\_{0}^{\infty}\mathbb{P}[N\_{r}=x]dF\_{\Lambda\_{1}}(r)=\int\_{0}^{\infty}\frac{(\lambda r)^{x}}{x!}e^{-\lambda r}dF\_{\Lambda\_{1}}(r). |  |

Substituting z:=λ​rz:=\lambda r, we get

|  |  |  |
| --- | --- | --- |
|  | =∫0∞zxx!​e−z​𝑑FΛ1​(zλ)=\int\_{0}^{\infty}\frac{z^{x}}{x!}e^{-z}dF\_{\Lambda\_{1}}(\frac{z}{\lambda}) |  |

for any x∈ℕx\in\mathbb{N}. Therefore NΛ1N\_{\Lambda\_{1}} is mixed Poisson distributed. Defining ℒ​(z):=λρ​L​(z)\mathcal{L}(z):=\lambda^{\rho}L(z), by slow variation of LL

|  |  |  |
| --- | --- | --- |
|  | FΛ1¯​(zλ)∼z−ρ​λρ​L​(zλ)∼z−ρ​ℒ​(z),z→∞.\overline{F\_{\Lambda\_{1}}}(\frac{z}{\lambda})\sim z^{-\rho}\lambda^{\rho}L(\frac{z}{\lambda})\sim z^{-\rho}\mathcal{L}(z),\quad z\to\infty. |  |

By Proposition 8.4 and Corollary 8.5 in [[19](#bib.bib9 "Mixed poisson processes")], it follows that

|  |  |  |
| --- | --- | --- |
|  | ℙ​[NΛ1>z]∼FΛ1¯​(zλ)∼z−ρ​ℒ​(z),z→∞.\mathbb{P}[N\_{\Lambda\_{1}}>z]\sim\overline{F\_{\Lambda\_{1}}}(\frac{z}{\lambda})\sim z^{-\rho}\mathcal{L}(z),\quad z\to\infty. |  |

Since FX¯​(x)∈o​(x−ρ​L​(x))\overline{F\_{X}}(x)\in o(x^{-\rho}L(x)) it holds per definition that

|  |  |  |
| --- | --- | --- |
|  | limx→∞FX¯​(x)​xρ​1L​(x)=0.\lim\_{x\to\infty}\overline{F\_{X}}(x)x^{\rho}\frac{1}{L(x)}=0. |  |

Furthermore we know

|  |  |  |
| --- | --- | --- |
|  | limx→∞ℙ​[NΛ1>x]​xρ​1L​(x)=limx→∞x−ρ​ℒ​(x)​xρ​1L​(x)=λρ.\lim\_{x\to\infty}\mathbb{P}[N\_{\Lambda\_{1}}>x]x^{\rho}\frac{1}{L(x)}=\lim\_{x\to\infty}x^{-\rho}\mathcal{L}(x)x^{\rho}\frac{1}{L(x)}=\lambda^{\rho}. |  |

By Theorem 1.3. in [[31](#bib.bib8 "Regular variation of the tail of a subordinated probability distribution")],

|  |  |  |
| --- | --- | --- |
|  | limz→∞ℙ​[Y1>z]​zρ​1L​(z)=(λ​𝔼​[X])ρ,\lim\_{z\to\infty}\mathbb{P}[Y\_{1}>z]z^{\rho}\frac{1}{L(z)}=(\lambda\mathbb{E}[X])^{\rho}, |  |

which shows that

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Y1>z]∼(λ​𝔼​[X])ρ​z−ρ​L​(z).\mathbb{P}[Y\_{1}>z]\sim(\lambda\mathbb{E}[X])^{\rho}z^{-\rho}L(z). |  |

We conclude by Theorem A3.19. in [[16](#bib.bib6 "Modelling extremal events: for insurance and finance")], that

|  |  |  |
| --- | --- | --- |
|  | FZ¯​(x)∼1ψΛ​(λ)​(λ​𝔼​[X])ρ​z−ρ​L​(z).\overline{F\_{Z}}(x)\sim\frac{1}{\psi\_{\Lambda}(\lambda)}(\lambda\mathbb{E}[X])^{\rho}z^{-\rho}L(z). |  |

∎

In the context of the Cramér-Lundberg model and ruin probabilities, the case of regularly varying tails of the claim size distribution is very comfortable. By applying Karamata´s Theorem, the asymptotics of the ruin probability can be obtained explicitly.

###### Corollary 1.

Let Λ\Lambda be a time-normalized Lévy subordinator, s.t. FΛ1¯​(x)∼x−ρ​L​(x)\overline{F\_{\Lambda\_{1}}}(x)\sim x^{-\rho}L(x) for a slowly varying LL and −ρ<−1-\rho<-1. Furthermore FX¯​(x)∈o​(x−ρ​L​(x))\overline{F\_{X}}(x)\in o(x^{-\rho}L(x)). Consider the subordinated Cramér-Lundberg process

|  |  |  |
| --- | --- | --- |
|  | Pt=u+c​t−∑k=1NΛtXk,P\_{t}=u+ct-\sum\_{k=1}^{N\_{\Lambda\_{t}}}X\_{k}, |  |

then the ruin probability of PtP\_{t} is asymptotically given by

|  |  |  |
| --- | --- | --- |
|  | ΨP​(u)∼1c−λ​𝔼​[X]​1ρ−1​(λ​𝔼​[X])ρ​u−ρ+1​L​(u),u→∞.\Psi\_{P}(u)\sim\frac{1}{c-\lambda\mathbb{E}[X]}\frac{1}{\rho-1}(\lambda\mathbb{E}[X])^{\rho}u^{-\rho+1}L(u),\quad u\to\infty. |  |

###### Proof.

Since FΛ1¯\overline{F\_{\Lambda\_{1}}} is regularly varying with index −ρ<−1-\rho<-1, we know from the previous theorem, that

|  |  |  |
| --- | --- | --- |
|  | FZ¯​(z)∼1ψΛ​(λ)​(λ​𝔼​[X])ρ​z−ρ​L​(z)\overline{F\_{Z}}(z)\sim\frac{1}{\psi\_{\Lambda}(\lambda)}(\lambda\mathbb{E}[X])^{\rho}z^{-\rho}L(z) |  |

for z→∞z\to\infty.
  
The integrated tail of FZ¯\overline{F\_{Z}} is defined by

|  |  |  |
| --- | --- | --- |
|  | FIZ¯​(x):=1𝔼​[Z]​∫x∞FZ¯​(y)​𝑑y.\overline{F\_{I}^{Z}}(x):=\frac{1}{\mathbb{E}[Z]}\int\_{x}^{\infty}\overline{F\_{Z}}(y)dy. |  |

By applying the Karamata’s Theorem, we obtain due to the regular variation of FZ¯\overline{F\_{Z}},

|  |  |  |
| --- | --- | --- |
|  | 1𝔼​[Z]​∫x∞FZ¯​(y)​𝑑y∼1ρ−1​1ψΛ​(λ)​(λ​𝔼​[X])ρ​1𝔼​[Z]​x−ρ+1​L​(x)=1ρ−1​(λ​𝔼​[X])ρ−1​x−ρ+1​L​(x).\frac{1}{\mathbb{E}[Z]}\int\_{x}^{\infty}\overline{F\_{Z}}(y)dy\sim\frac{1}{\rho-1}\frac{1}{\psi\_{\Lambda}(\lambda)}(\lambda\mathbb{E}[X])^{\rho}\frac{1}{\mathbb{E}[Z]}x^{-\rho+1}L(x)=\frac{1}{\rho-1}{(\lambda\mathbb{E}[X])^{\rho-1}}x^{-\rho+1}L(x). |  |

Applying Theorem 1.3.6 in [[16](#bib.bib6 "Modelling extremal events: for insurance and finance")], we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψP​(u)\displaystyle\psi\_{P}(u) | ∼λ​𝔼​[X]c−λ​𝔼​[X]​1ρ−1​(λ​𝔼​[X])ρ−1​u−ρ+1​L​(u)\displaystyle\sim\frac{\lambda\mathbb{E}[X]}{c-\lambda\mathbb{E}[X]}\frac{1}{\rho-1}(\lambda\mathbb{E}[X])^{\rho-1}u^{-\rho+1}L(u) |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1c−λ​𝔼​[X]​1ρ−1​(λ​𝔼​[X])ρ​u−ρ+1​L​(u),u→∞.\displaystyle=\frac{1}{c-\lambda\mathbb{E}[X]}\frac{1}{\rho-1}(\lambda\mathbb{E}[X])^{\rho}u^{-\rho+1}L(u),\quad u\to\infty. |  | (21) |

∎

This result particularly striking. According to the preceding theorem, regular variation is inherited from the subordinator to the jump size ZZ of the subordinated process. Consequently, the asymptotic behaviour of the insurer’s ruin probability can be quantified using Karamata’s Theorem. This represents a risk that an insurer cannot afford to ignore.
  
  
As noted earlier, time-normalized subordination is solely a random change in the timing of loss occurrences and does not alter the expected value. Nevertheless, the probability of ruin can be seriously affected by the clustering of losses (as in Nat-Cat events), even if the individual losses appear very moderate. The following example illustrates this.

###### Example 2.

Let Ct:=∑i=1NtXiC\_{t}:=\sum\_{i=1}^{N\_{t}}X\_{i} be a compound Poisson process with X1∼E​x​p​(1)X\_{1}\sim Exp(1) and 𝔼​[N1]=1\mathbb{E}[N\_{1}]=1. For the subordinator Λ\Lambda we define

|  |  |  |
| --- | --- | --- |
|  | Λt:=0.9​t+∑i=1Nt¯Ki,\Lambda\_{t}:=0.9t+\sum\_{i=1}^{\bar{N\_{t}}}K\_{i}, |  |

where N¯\bar{N} is a Poisson process with intensity 11 and (Kj)j∈ℕ(K\_{j})\_{j\in\mathbb{N}} are i.i.d. positive random variables with K1∼P​a​r​(0.1​ε1+ε,1+ε)K\_{1}\sim Par(\frac{0.1\varepsilon}{1+\varepsilon},1+\varepsilon) for ε>0\varepsilon>0. Here, the first parameter denotes the scale parameter of the Pareto distribution, while the second parameter represents the shape parameter. The parameters are chosen in such a way, that Λ\Lambda fulfills the time normalization assumption, i.e. 𝔼​[Λ1]=1\mathbb{E}[\Lambda\_{1}]=1.
  
We compare the ruin probabilities of

|  |  |  |
| --- | --- | --- |
|  | St:=u+c​t−∑i=1NtXiS\_{t}:=u+ct-\sum\_{i=1}^{N\_{t}}X\_{i} |  |

and

|  |  |  |
| --- | --- | --- |
|  | Pt:=u+c​t−∑i=1NΛtXi.P\_{t}:=u+ct-\sum\_{i=1}^{N\_{\Lambda\_{t}}}X\_{i}. |  |

  

We know by Propostition 1.5 in section X.1 and by Lemma 2.2 in section X.2 in [[3](#bib.bib11 "Ruin probabilities")], that

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Λ1>x]=ℙ​[0.9+∑i=1Nt¯Ki>x]∼ℙ​[∑i=1Nt¯Ki>x]∼ℙ​[K1>x]=(0.1​ε(1+ϵ)​x)1+ε,\mathbb{P}[\Lambda\_{1}>x]=\mathbb{P}[0.9+\sum\_{i=1}^{\bar{N\_{t}}}K\_{i}>x]\sim\mathbb{P}[\sum\_{i=1}^{\bar{N\_{t}}}K\_{i}>x]\sim\mathbb{P}[K\_{1}>x]=\left(\frac{0.1\varepsilon}{(1+\epsilon)x}\right)^{1+\varepsilon}, |  |

for x→∞x\to\infty.
Therefore Λ1\Lambda\_{1} is regularly varying with index −(1+ε)-(1+\varepsilon). By the previous corollary, we have

|  |  |  |
| --- | --- | --- |
|  | ΨP​(u)∼1c−1​1ε​u−ε​(0.1​ε1+ε)1+ε.\Psi\_{P}(u)\sim\frac{1}{c-1}\frac{1}{\varepsilon}u^{-\varepsilon}\left(\frac{0.1\varepsilon}{1+\varepsilon}\right)^{1+\varepsilon}. |  |

Moreover for SS, standard Cramér-Lundberg theory yields

|  |  |  |
| --- | --- | --- |
|  | ΨS​(u)∼1c​e−(1−1c)​u.\Psi\_{S}(u)\sim\frac{1}{c}e^{-(1-\frac{1}{c})u}. |  |

Note that 𝔼​[St]=𝔼​[Pt]\mathbb{E}[S\_{t}]=\mathbb{E}[P\_{t}] for all t≥0t\geq 0. Nevertheless, asymptotic behaviour of the ruin probabilities differs dramatically. For ε>0\varepsilon>0 small, ΨP​(u)\Psi\_{P}(u) exhibits polynomial decay that can be made arbitrarily slow, whereas ΨS​(u)\Psi\_{S}(u) always decays exponentially fast.

## 5 Concluding Remarks

In this paper, we have developed a model capable of incorporating cumulative losses, such as natural catastrophe events, into an insurance portfolio consisting of individual claims. The insurer’s initial loss process was modeled by a compound Poisson process. Nat-Cat losses were then introduced by means of a stochastic time change, which was given by a Lévy subordinator.
The Lévy subordinator was chosen so that it runs as fast as calendar time on average. This time normalization enabled a meaningful quantitative comparison between the subordinated and the initial portfolio, since under this condition the subordination does not alter the expectation of the risk process. Moreover, time normalization ensured that subordination represents purely a random distortion of the claim occurrence times.
Nevertheless, we have shown, that this change in the timing has a substantial impact on the asymptotic behaviour of the ruin probability.
  
  
We proved that the insurer’s time-changed claims process remains a compound Poisson process and derived conditions under which the subordinated process exhibits light-tailed or heavy-tailed jump distributions. We were able to quantify the risk of ruin in both cases. Moreover we have shown that subordination is always bad for the insurer in the case of light tails. In the case of heavy tails our analysis mainly focused on the jump distributions with regularly varying tails. We established conditions under which the subordinated process inherits regular variation and using Karamata’s theorem, obtained asymptotic results for the ruin probability in this case. We have shown that also in the case of regular variation, under very mild conditions, the effect of subordination on the ruin probability is negative.
  
  
As shown in the last section, if we start with an initial model whose jump distribution is light-tailed and apply a time-normalized Lévy subordinator with regularly varying tails, the ruin probability decays only polynomially. Depending on the choice of subordinator, this polynomial decay can be made arbitrarily slow. It is important to note that, without subordination, the initial model always exhibits an exponential decay of the ruin probability. The dramatic difference in the asymptotic behaviour arises from the fact that, in the subordinated model, losses occur in clusters rather than being evenly spread over the insurance horizon, as in the initial model.

## References

* [1]
  H. Albrecher, B. Garcia Flores, and C. Hipp (2025)
  Dividend corridors and a ruin constraint.
  Insurance: Mathematics and Economics 121,  pp. 1–25.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [2]
  D. Applebaum (2009)
  Lévy processes and stochastic calculus.
   Cambridge university press.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [3]
  S. Asmussen and H. Albrecher (2010)
  Ruin probabilities.
  Vol. 14, World scientific.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [Example 2](#Thmexample2.p1.22.1 "Example 2. ‣ 4.3 Regularly Varying Subordinator ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [4]
  M. Averhoff and J. Thøgersen (2025)
  Experience rating in the cramér-lundberg model.
  Insurance: Mathematics and Economics 124,  pp. 103128.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [5]
  N. Baradel (2024)
  Optimal control under uncertainty: application to the issue of cat bonds.
  Insurance: Mathematics and Economics 117,  pp. 16–44.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [6]
  N. Bäuerle and A. Müller (2006)
  Stochastic orders and risk measures: consistency and bounds.
  Insurance: Mathematics and Economics 38 (1),  pp. 132–148.
  Cited by: [§2.2](#S2.SS2.p3.6 "2.2 Stochastic Dominance of Subordinated Jump Sizes ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [7]
  J. Bertoin (1996)
  Lévy processes.
  Vol. 121, Cambridge university press Cambridge.
  Cited by: [§2.1](#S2.SS1.p2.14 "2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [8]
  N. H. Bingham, C. M. Goldie, and J. L. Teugels (1989)
  Regular variation.
  Vol. 27, Cambridge university press.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [9]
  S. Bochner (1949)
  Diffusion equation and stochastic processes.
  Proceedings of the National Academy of Sciences 35 (7),  pp. 368–370.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [10]
  S. Bochner (1955)
  Harmonic analysis and the theory of probability.
  1 edition, University of California Press.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [11]
  P. Braunsteins and M. Mandjes (2023)
  The cramér-lundberg model with a fluctuating number of clients.
  Insurance: Mathematics and Economics 112,  pp. 1–22.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [12]
  E. C.K. Cheung and W. Zhu (2023)
  Cumulative parisian ruin in finite and infinite time horizons for a renewal risk process with exponential claims.
  Insurance: Mathematics and Economics 111,  pp. 84–101.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [13]
  K. Colaneri and R. Frey (2021)
  Classical solutions of the backward pide for markov modulated marked point processes and applications to cat bonds.
  Insurance: Mathematics and Economics 101,  pp. 498–507.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [14]
  R. Cont and P. Tankov (2003)
  Financial modelling with jump processes.
   Chapman and Hall/CRC.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [15]
  A. Di Crescenzo, B. Martinucci, and S. Zacks (2015-06)
  Compound poisson process with a poisson subordinator.
  Journal of Applied Probability 52 (2),  pp. 360–374.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [16]
  P. Embrechts, C. Klüppelberg, and T. Mikosch (2013)
  Modelling extremal events: for insurance and finance.
  Vol. 33, Springer Science & Business Media.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§4.1](#S4.SS1.p2.15 "4.1 Preliminary Definitions ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§4.2](#S4.SS2.1.p1.14 "Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§4.2](#S4.SS2.1.p1.15 "Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§4.3](#S4.SS3.1.p1.12 "Proof. ‣ 4.3 Regularly Varying Subordinator ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§4.3](#S4.SS3.2.p1.6 "Proof. ‣ 4.3 Regularly Varying Subordinator ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [17]
  J. A. Faias and J. Guedes (2020)
  The diffusion of complex securities: the case of cat bonds.
  Insurance: Mathematics and Economics 90,  pp. 46–57.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [18]
  S. Foss, D. Korshunov, S. Zachary, et al. (2011)
  An introduction to heavy-tailed and subexponential distributions.
  Vol. 6, Springer.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§2.3](#S2.SS3.p2.6 "2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [19]
  J. Grandell (1997)
  Mixed poisson processes.
  Vol. 77, CRC Press.
  Cited by: [§4.3](#S4.SS3.1.p1.8 "Proof. ‣ 4.3 Regularly Varying Subordinator ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [20]
  B. Li and X. Zhou (2024)
  An excursion theoretic approach to parisian ruin problem.
  Insurance: Mathematics and Economics 118,  pp. 44–58.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [21]
  F. Lindskog and M. V. Wüthrich (2025)
  Eliciting claims development patterns and costs hidden in backlogs.
  European Actuarial Journal,  pp. 1–39.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [22]
  H. Liu (2025)
  Robust indifference valuation of catastrophe bonds.
  Insurance: Mathematics and Economics 122,  pp. 1–10.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [23]
  F. Locas and J. Renaud (2025)
  Optimality of a refraction strategy in the optimal dividends problem with absolutely continuous controls subject to parisian ruin.
  Insurance: Mathematics and Economics 120,  pp. 189–206.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [24]
  F. Lundberg (1903)
  I. approximerad framställning af sannolikhetsfunktionen. ii. aterförsäkring af kollektivrisker.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [25]
  T. Rolski, H. Schmidli, V. Schmidt, and J. L. Teugels (2009)
  Stochastic processes for insurance and finance.
   John Wiley & Sons.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [26]
  K. Sato (1999)
  Lévy processes and infinitely divisible distributions.
  Vol. 68, Cambridge university press.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§2.1](#S2.SS1.p2.14 "2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [27]
  H. Schmidli (1999)
  Compound sums and subexponentiality.
  Bernoulli 5 (6),  pp. 999 – 1012.
  Cited by: [§4.2](#S4.SS2.1.p1.12 "Proof. ‣ 4.2 Subexponential Initial Jump Size ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [28]
  H. Schmidli (2017)
  Risk theory.
   Springer.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§3](#S3.3.p1.8 "Proof. ‣ 3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§3](#S3.p1.8 "3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§3](#S3.p3.12 "3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§3](#S3.p3.23 "3 Adjustment Coefficient in the Subordinated Model: Light-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [29]
  D. A. Selch and M. Scherer (2018)
  A multivariate claim count model for applications in insurance.
   Springer.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§2.1](#S2.SS1.1.p1.1 "Proof. ‣ 2.1 Model ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§2.3](#S2.SS3.p2.6 "2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions."),
  [§2.3](#S2.SS3.p4.3 "2.3 Heavy- and Light-Tailedness of 𝑍 ‣ 2 Subordinated Compound Poisson Process ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [30]
  A. S. Sengar, A. Maheshwari, and N. Upadhye (2020)
  Time-changed poisson processes of order k.
  Stochastic Analysis and Applications 38 (1),  pp. 124–148.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [31]
  A. Stam (1973)
  Regular variation of the tail of a subordinated probability distribution.
  Advances in Applied Probability 5 (2),  pp. 308–327.
  Cited by: [§4.3](#S4.SS3.1.p1.10 "Proof. ‣ 4.3 Regularly Varying Subordinator ‣ 4 Asymptotic Ruin Probabilities: Heavy-Tailed Jump Sizes ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [32]
  Y. Zhang and P. Brockett (2020)
  Modeling stochastic mortality for joint lives through subordinators.
  Insurance: Mathematics and Economics 95,  pp. 166–172.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").
* [33]
  W. Zhu (2025)
  Ruin probabilities in an erlang risk model with dependence structure based on an independent gamma-distributed time window.
  European Actuarial Journal,  pp. 1–27.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Asymptotics of Ruin Probabilities in a Subordinated Cramér-Lundberg Model1footnote 1footnoteFootnotefootnotesFootnotes1footnote 1Financial support by the German Research Foundation (DFG) [RTG 2865/1 – 492988838] is gratefully acknowledged. The authors thank Alfred Müller, Matthias Scherer and Hanspeter Schmidli for helpful comments and fruitful discussions.").

BETA