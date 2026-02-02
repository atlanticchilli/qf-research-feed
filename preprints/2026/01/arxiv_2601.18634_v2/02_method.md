---
authors:
- Zhipeng Huang
- Cornelis W. Oosterlee
doc_id: arxiv:2601.18634v2
family_id: arxiv:2601.18634
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal
  Stopping Problems in Finance'
url_abs: http://arxiv.org/abs/2601.18634v2
url_html: https://arxiv.org/html/2601.18634v2
venue: arXiv q-fin
version: 2
year: 2026
---


Zhipeng Huang
Mathematical Institute, Utrecht University, Postbus 80010, 3508 TA Utrecht, The Netherlands.
Corresponding author: z.huang1@uu.nl
  
Cornelis W. Oosterlee
Mathematical Institute, Utrecht University, Postbus 80010, 3508 TA Utrecht, The Netherlands.

###### Abstract

We propose the Compound BSDE method, a fully forward, deep-learning-based approach for solving a broad class of problems in financial mathematics, including optimal stopping. The method is based on a reformulation of option pricing problems in terms of a system of backward stochastic differential equations (BSDEs), which offers a new perspective on the numerical treatment of compound options and optimal stopping problems such as Bermudan option pricing. Building on the classical deep BSDE method for a single BSDE, we develop an algorithm for compound BSDEs and establish its convergence properties. In particular, we derive an *a posteriori* error estimate for the proposed method. Numerical experiments demonstrate the accuracy and computational efficiency of the approach, and illustrate its effectiveness for high-dimensional option pricing and optimal stopping problems.

Keywords: Compound BSDE method, option pricing, optimal stopping, reflected BSDE.

## 1 Introduction

Option pricing is a central topic in financial mathematics, especially for derivatives with complex payoff structures, early-exercise features, or high-dimensional underlying dynamics. Over the past decades, a wide range of numerical methods has been developed to address these challenges. Without attempting to provide an exhaustive overview, we mention partial differential equation (PDE) based methods [[1](https://arxiv.org/html/2601.18634v2#bib.bib1), [2](https://arxiv.org/html/2601.18634v2#bib.bib2), [3](https://arxiv.org/html/2601.18634v2#bib.bib3)], Fourier-based techniques such as the COS method [[4](https://arxiv.org/html/2601.18634v2#bib.bib4), [5](https://arxiv.org/html/2601.18634v2#bib.bib5)], and Monte Carlo regression-based approaches [[6](https://arxiv.org/html/2601.18634v2#bib.bib6), [7](https://arxiv.org/html/2601.18634v2#bib.bib7)].

In addition to these approaches, backward stochastic differential equations (BSDEs) [[8](https://arxiv.org/html/2601.18634v2#bib.bib8)] provide a flexible framework for option pricing. Via the Feynman–Kac representation [[9](https://arxiv.org/html/2601.18634v2#bib.bib9)], a pricing problem can be reformulated as a BSDE and solved numerically. A broad class of numerical schemes for BSDEs and forward–backward SDEs (FBSDEs) has been developed and analyzed; see, for example, [[10](https://arxiv.org/html/2601.18634v2#bib.bib10), [11](https://arxiv.org/html/2601.18634v2#bib.bib11), [12](https://arxiv.org/html/2601.18634v2#bib.bib12), [13](https://arxiv.org/html/2601.18634v2#bib.bib13), [14](https://arxiv.org/html/2601.18634v2#bib.bib14), [15](https://arxiv.org/html/2601.18634v2#bib.bib15)]. More recently, machine-learning-based approaches have attracted considerable interest due to their ability to address high-dimensional problems, including the deep BSDE method [[16](https://arxiv.org/html/2601.18634v2#bib.bib16), [17](https://arxiv.org/html/2601.18634v2#bib.bib17)], deep splitting [[18](https://arxiv.org/html/2601.18634v2#bib.bib18)], and deep backward dynamic programming [[19](https://arxiv.org/html/2601.18634v2#bib.bib19)], as well as related variants [[20](https://arxiv.org/html/2601.18634v2#bib.bib20), [21](https://arxiv.org/html/2601.18634v2#bib.bib21), [22](https://arxiv.org/html/2601.18634v2#bib.bib22)].

Reflected BSDEs provide a natural framework for pricing American- and Bermudan-style options; see, for example, [[23](https://arxiv.org/html/2601.18634v2#bib.bib23), [24](https://arxiv.org/html/2601.18634v2#bib.bib24), [25](https://arxiv.org/html/2601.18634v2#bib.bib25), [26](https://arxiv.org/html/2601.18634v2#bib.bib26), [19](https://arxiv.org/html/2601.18634v2#bib.bib19), [27](https://arxiv.org/html/2601.18634v2#bib.bib27)] for numerical methods for solving this type of BSDE. These approaches share a similar philosophy with the least-squares Monte Carlo method [[6](https://arxiv.org/html/2601.18634v2#bib.bib6)]: one simulates the underlying dynamics forward in time and then optimizes backward. In recent contributions [[28](https://arxiv.org/html/2601.18634v2#bib.bib28), [29](https://arxiv.org/html/2601.18634v2#bib.bib29)], a backward variant of the deep BSDE method has been studied, in which the loss functional is replaced by the variance of the YY process at the initial time. Numerical results suggest that this approach may be applicable to Bermudan option pricing. However, the convergence of this method for pricing early-exercise options has not been established in [[29](https://arxiv.org/html/2601.18634v2#bib.bib29)] and remains an open problem.

In this paper, we introduce the Compound BSDE method, a deep-learning-based approach for solving a broad class of option pricing and optimal stopping problems in finance. The main contributions of this work can be summarized as follows:

* •

  We introduce the compound BSDE, a new BSDE formulation with a wide range of financial applications, in particular for option pricing and optimal stopping. The formulation is inspired by the payoff structure of compound options. A detailed discussion of this class of exotic options and their connection to our framework is provided in Section [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance").
* •

  Building on the deep BSDE method, we develop the Compound BSDE method tailored to the new formulation and derive an *a posteriori* error estimate. We emphasize that the resulting algorithm is naturally a *fully forward method* and can be applied directly to optimal stopping problems, in contrast to many existing approaches in the aforementioned literature.
* •

  We present numerical experiments that validate the theoretical results. The results demonstrate that the proposed method achieves accurate prices and hedges for a variety of option types, including Bermudan-style options in high-dimensional settings.

The remainder of the paper is organized as follows. In Section [2](https://arxiv.org/html/2601.18634v2#S2 "2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), we introduce the compound BSDE formulation and the associated numerical method. In Section [3](https://arxiv.org/html/2601.18634v2#S3 "3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), we discuss well-posedness of the formulation and establish convergence of the proposed method. Section [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") explains how the compound BSDE framework can be applied to various option pricing and optimal stopping problems. Numerical results are presented in Section [5](https://arxiv.org/html/2601.18634v2#S5 "5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"). Section [6](https://arxiv.org/html/2601.18634v2#S6 "6 Conclusion ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") concludes the paper.

## 2 The Compound BSDE Method

In this section, we introduce the compound BSDE formulation and the associated numerical method. We begin with a brief review of the deep BSDE method, which serves as an important building block for our approach, and then define the compound BSDE motivated by the structure of compound options.

### 2.1 Review of the deep BSDE method

A backward stochastic differential equation (BSDE) on a finite time horizon [0,T][0,T] is formulated on a filtered probability space
(Ω,ℱ,{ℱt}0≤t≤T,ℙ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{0\leq t\leq T},\mathbb{P}), and typically takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | {𝒳t=𝒳0+∫0tμ​(s,𝒳s)​ds+∫0tσ​(s,𝒳s)​dWs,𝒴t=g​(𝒳T)+∫tTf​(s,𝒳s,𝒴s,𝒵s)​ds−∫tT𝒵s​dWs,\left\{\begin{aligned} \mathcal{X}\_{t}&=\mathcal{X}\_{0}+\int\_{0}^{t}\mu(s,\mathcal{X}\_{s})\,\mathrm{d}s+\int\_{0}^{t}\sigma(s,\mathcal{X}\_{s})\,\mathrm{d}W\_{s},\\ \mathcal{Y}\_{t}&=g(\mathcal{X}\_{T})+\int\_{t}^{T}f(s,\mathcal{X}\_{s},\mathcal{Y}\_{s},\mathcal{Z}\_{s})\,\mathrm{d}s-\int\_{t}^{T}\mathcal{Z}\_{s}\,\mathrm{d}W\_{s},\end{aligned}\right. |  | (2.1) |

where W≔{Wt}0≤t≤TW\coloneqq\{W\_{t}\}\_{0\leq t\leq T} is a Brownian motion, and μ\mu, σ\sigma, gg, and ff are deterministic functions. The solution of ([2.1](https://arxiv.org/html/2601.18634v2#S2.E1 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) is a triple of adapted processes
(𝒳,𝒴,𝒵)≔{(𝒳t,𝒴t,𝒵t)}0≤t≤T(\mathcal{X},\mathcal{Y},\mathcal{Z})\coloneqq\{(\mathcal{X}\_{t},\mathcal{Y}\_{t},\mathcal{Z}\_{t})\}\_{0\leq t\leq T} satisfying appropriate integrability conditions.

The deep BSDE method [[16](https://arxiv.org/html/2601.18634v2#bib.bib16)] approximates the solution of ([2.1](https://arxiv.org/html/2601.18634v2#S2.E1 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) by solving a stochastic optimization problem based on a time discretization. Specifically, it considers

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
|  | inf𝒴t0π,{𝒵tiπ}𝔼​‖g​(𝒳Tπ)−𝒴Tπ‖2,\displaystyle\inf\_{\mathcal{Y}\_{t\_{0}}^{\pi},\{\mathcal{Z}\_{t\_{i}}^{\pi}\}}\quad\mathbb{E}\big\|g(\mathcal{X}\_{T}^{\pi})-\mathcal{Y}\_{T}^{\pi}\big\|^{2}, |  | (2.2a) |
|  | subject to{𝒳ti+1π=𝒳tiπ+b​(ti,𝒳tiπ)​h+σ​(ti,𝒳tiπ)​Δ​Wti,𝒴ti+1π=𝒴tiπ−f​(ti,𝒳tiπ,𝒴tiπ,𝒵tiπ)​h+𝒵tiπ​Δ​Wti,\displaystyle\text{subject to}\left\{\begin{aligned} \mathcal{X}\_{t\_{i+1}}^{\pi}&=\mathcal{X}\_{t\_{i}}^{\pi}+b(t\_{i},\mathcal{X}\_{t\_{i}}^{\pi})h+\sigma(t\_{i},\mathcal{X}\_{t\_{i}}^{\pi})\Delta W\_{t\_{i}},\\[3.0pt] \mathcal{Y}\_{t\_{i+1}}^{\pi}&=\mathcal{Y}\_{t\_{i}}^{\pi}-f(t\_{i},\mathcal{X}\_{t\_{i}}^{\pi},\mathcal{Y}\_{t\_{i}}^{\pi},\mathcal{Z}\_{t\_{i}}^{\pi})h+\mathcal{Z}\_{t\_{i}}^{\pi}\Delta W\_{t\_{i}},\end{aligned}\right. |  | (2.2b) |

where we denote ‖x‖\|x\| the Euclidean norm if xx is a vector or the Frobenius norm if xx is a matrix, Δ​Wti≔Wti+1−Wti\Delta W\_{t\_{i}}\coloneqq W\_{t\_{i+1}}-W\_{t\_{i}} is the Brownian increment, π\pi denotes a uniform partition of [0,T][0,T] with step size hh. The quantities 𝒴t0π\mathcal{Y}\_{t\_{0}}^{\pi} and 𝒵tiπ\mathcal{Z}\_{t\_{i}}^{\pi} are parameterized by neural networks and serve as approximations of 𝒴t0\mathcal{Y}\_{t\_{0}} and 𝒵ti\mathcal{Z}\_{t\_{i}}, respectively. The objective functional ([2.2a](https://arxiv.org/html/2601.18634v2#S2.E2.1 "In 2.2 ‣ 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) acts as the loss function during the training of neural networks, and enforces the terminal condition 𝒴T=g​(𝒳T)\mathcal{Y}\_{T}=g(\mathcal{X}\_{T}).

Two properties of ([2.2](https://arxiv.org/html/2601.18634v2#S2.E2 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) are particularly relevant for our development. First, as noted in [[17](https://arxiv.org/html/2601.18634v2#bib.bib17)], the initial state 𝒳t0π\mathcal{X}\_{t\_{0}}^{\pi} need not be deterministic, but may be any square-integrable random variable. In this case, 𝒴t0π\mathcal{Y}\_{t\_{0}}^{\pi} learns the dependence on the distribution of 𝒳t0π\mathcal{X}\_{t\_{0}}^{\pi} rather than a fixed constant. Second, convergence of the method depends primarily on how small the objective function value is, and does not depend explicitly on 𝒴t0π\mathcal{Y}\_{t\_{0}}^{\pi}. We remark that when 𝒳t0π\mathcal{X}\_{t\_{0}}^{\pi} is random, the backward deep BSDE method of [[29](https://arxiv.org/html/2601.18634v2#bib.bib29)] cannot be applied directly, since the property Var⁡(𝒴0)=0\operatorname{Var}(\mathcal{Y}\_{0})=0 no longer holds.

### 2.2 Motivation: compound options

We now explain the intuition behind the compound BSDE formulation. Consider a simple compound option, namely a call-on-call option. This product can be viewed as a call option (the outer option) whose underlying asset is another call option (the inner option). When the outer option expires at time T1>0T\_{1}>0, the holder has the right to purchase the inner option, which itself expires at a later time T2>T1T\_{2}>T\_{1}, at a specified strike price.

In the BSDE framework ([2.1](https://arxiv.org/html/2601.18634v2#S2.E1 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), the 𝒴\mathcal{Y} process represents the option value. In the current call-on-call setting, this naturally leads to two BSDEs: one describing the value of the inner option and one describing the value of the outer option, coupled at the intermediate time T1T\_{1} through the exercise decision. This idea extends naturally to an MM-fold compound option, where multiple BSDEs are linked at a sequence of intermediate times TjT\_{j} for j=1,2,…​M−1j=1,2,\dots M-1.

### 2.3 Definition of the compound BSDE

We now introduce the compound BSDE formally. Let (Ω,ℱ,{ℱt}0≤t≤T,ℙ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{0\leq t\leq T},\mathbb{P}) be a filtered probability space, where {ℱt}\{\mathcal{F}\_{t}\} is the natural filtration of a d3d\_{3}-dimensional Brownian motion W={Wt}0≤t≤TW=\{W\_{t}\}\_{0\leq t\leq T}. Let M∈ℕM\in\mathbb{N} and 0=T0<T1<⋯<TM=T0=T\_{0}<T\_{1}<\cdots<T\_{M}=T. The MM-fold compound BSDE on [0,T][0,T] is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Xt=X0+∫0tμ​(s,Xs)​ds+∫0tσ​(s,Xs)​dWs,∀t∈[0,T]Y1,t=g1​(XT1,Y2,T1)+∫tT1f1​(s,Xs,Y1,s,Z1,s)​ds−∫tT1Z1,s​dWs,∀t∈[T0,T1]Y2,t=g2​(XT2,Y3,T2)+∫tT2f2​(s,Xs,Y2,s,Z2,s)​ds−∫tT2Z2,s​dWs,∀t∈[T1,T2]⋮YM,t=gM​(XT)+∫tTMfM​(s,Xs,YM,s,ZM,s)​ds−∫tTMZM,s​dWs,∀t∈[TM−1,TM].\left\{\begin{aligned} X\_{t}&=X\_{0}+\int\_{0}^{t}\mu(s,X\_{s})\,\mathrm{d}s+\int\_{0}^{t}\sigma(s,X\_{s})\,\mathrm{d}W\_{s},\quad\forall t\in[0,T]\\ Y\_{1,t}&=g\_{1}(X\_{T\_{1}},Y\_{2,T\_{1}})+\int\_{t}^{T\_{1}}f\_{1}(s,X\_{s},Y\_{1,s},Z\_{1,s})\,\mathrm{d}s-\int\_{t}^{T\_{1}}Z\_{1,s}\,\mathrm{d}W\_{s},\quad\forall t\in[T\_{0},T\_{1}]\\ Y\_{2,t}&=g\_{2}(X\_{T\_{2}},Y\_{3,T\_{2}})+\int\_{t}^{T\_{2}}f\_{2}(s,X\_{s},Y\_{2,s},Z\_{2,s})\,\mathrm{d}s-\int\_{t}^{T\_{2}}Z\_{2,s}\,\mathrm{d}W\_{s},\quad\forall t\in[T\_{1},T\_{2}]\\ &\hskip 34.14322pt\vdots\\ Y\_{M,t}&=g\_{M}(X\_{T})+\int\_{t}^{T\_{M}}f\_{M}(s,X\_{s},Y\_{M,s},Z\_{M,s})\,\mathrm{d}s-\int\_{t}^{T\_{M}}Z\_{M,s}\,\mathrm{d}W\_{s},\quad\forall t\in[T\_{M-1},T\_{M}].\end{aligned}\right. |  | (2.3) |

Here, TjT\_{j} and gjg\_{j} for j=1,…,M−1j=1,\ldots,M-1 are referred to as the *compounding times* and *compounding conditions*, respectively, to distinguish them from the terminal time TMT\_{M} and terminal condition gMg\_{M}. The functions gjg\_{j}, fjf\_{j}, μ\mu, and σ\sigma are all deterministic. The solution to ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), denoted by (X,Y,Z)(X,Y,Z), consists of the ℝd1\mathbb{R}^{d\_{1}}-valued forward process XX and the family of ℝd2×ℝd2×d3\mathbb{R}^{d\_{2}}\times\mathbb{R}^{d\_{2}\times d\_{3}} - valued backward processes {(Yj,t,Zj,t)}j,t\{(Y\_{j,t},Z\_{j,t})\}\_{j,t}, which are adapted and square-integrable. The well-posedness of this system will be discussed in Section [3](https://arxiv.org/html/2601.18634v2#S3 "3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance").

The compound BSDE ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) comprises a single forward SDE coupled with MM backward equations defined on successive time intervals. These equations interact only at the compounding times through the functions gjg\_{j}, which may depend on the unknown values Yj+1,TjY\_{j+1,T\_{j}}. This distinguishes the compound BSDE from a collection of independent BSDEs and requires the system to be treated as a whole. This coupling or compounding structure plays a central role in both the convergence analysis in Section [3](https://arxiv.org/html/2601.18634v2#S3 "3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") and the applications discussed in Section [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance").

### 2.4 The Compound BSDE method

To solve ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) numerically, we rewrite all backward equations in a forward simulation framework and enforce the compounding and terminal conditions by minimizing a joint objective functional. This leads to the Compound BSDE method,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | inf{Yj,Tj−1π},{Zj,tiπ}∑j=1M−1𝔼​‖gj​(XTjπ,Yj+1,Tjπ)−Yj,Tjπ‖2+𝔼​‖gM​(XTMπ)−YM,TMπ‖2\displaystyle\inf\_{\{Y\_{j,T\_{j-1}}^{\pi}\},\ \{Z\_{j,t\_{i}}^{\pi}\}}\quad\sum\_{j=1}^{M-1}\mathbb{E}\|g\_{j}(X\_{T\_{j}}^{\pi},Y\_{j+1,T\_{j}}^{\pi})-Y\_{j,T\_{j}}^{\pi}\|^{2}+\mathbb{E}\|g\_{M}(X\_{T\_{M}}^{\pi})-Y\_{M,T\_{M}}^{\pi}\|^{2} |  | (2.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | s.t. {Xti+1π=Xtiπ+b​(ti,Xtiπ)​h+σ​(ti,Xtiπ)​Δ​Wti,Xt0π=X0Y1,ti+1π=Y1,tiπ−f1​(ti,Xtiπ,Y1,tiπ,Z1,tiπ)​h+Z1,tiπ​Δ​Wti,Y2,ti+1π=Y2,tiπ−f2​(ti,Xtiπ,Y2,tiπ,Z2,tiπ)​h+Z2,tiπ​Δ​Wti,⋮YM,ti+1π=YM,tiπ−fM​(ti,Xtiπ,YM,tiπ,ZM,tiπ)​h+ZM,tiπ​Δ​Wti,\displaystyle\text{s.t. }\left\{\begin{aligned} X\_{t\_{i+1}}^{\pi}&=X\_{t\_{i}}^{\pi}+b\left(t\_{i},X\_{t\_{i}}^{\pi}\right)h+\sigma\left(t\_{i},X\_{t\_{i}}^{\pi}\right)\Delta W\_{t\_{i}},\quad X\_{t\_{0}}^{\pi}=X\_{0}\\ Y\_{1,t\_{i+1}}^{\pi}&=Y\_{1,t\_{i}}^{\pi}-f\_{1}(t\_{i},X\_{t\_{i}}^{\pi},Y\_{1,t\_{i}}^{\pi},Z\_{1,t\_{i}}^{\pi})h+Z\_{1,t\_{i}}^{\pi}\Delta W\_{t\_{i}},\\ Y\_{2,t\_{i+1}}^{\pi}&=Y\_{2,t\_{i}}^{\pi}-f\_{2}(t\_{i},X\_{t\_{i}}^{\pi},Y\_{2,t\_{i}}^{\pi},Z\_{2,t\_{i}}^{\pi})h+Z\_{2,t\_{i}}^{\pi}\Delta W\_{t\_{i}},\\ &\mathmakebox[\widthof{{}={}}][c]{\vdots}\\ Y\_{M,t\_{i+1}}^{\pi}&=Y\_{M,t\_{i}}^{\pi}-f\_{M}(t\_{i},X\_{t\_{i}}^{\pi},Y\_{M,t\_{i}}^{\pi},Z\_{M,t\_{i}}^{\pi})h+Z\_{M,t\_{i}}^{\pi}\Delta W\_{t\_{i}},\end{aligned}\right. |  | (2.5) |

Here, we adopt the same conventions for the norms, the Brownian increments Δ​Wti\Delta W\_{t\_{i}} and the uniform partition π\pi as in the description of the deep BSDE method. The initial values {Yj,Tj−1π}j\{Y\_{j,T\_{j-1}}^{\pi}\}\_{j} and the processes {Zj,tiπ}j,ti\{Z\_{j,t\_{i}}^{\pi}\}\_{j,t\_{i}} are parameterized by neural networks. Moreover, let NjN\_{j} denote the number of time discretization steps for the process Yj,tiπY\_{j,t\_{i}}^{\pi} running on [Tj−1,Tj][T\_{j-1},T\_{j}], for j=1,2,…,Mj=1,2,\ldots,M, so that N1+N2+⋯+NM=NN\_{1}+N\_{2}+\cdots+N\_{M}=N is the total number of time steps. For convenience, we assume that (Tj−Tj−1)/Nj=h(T\_{j}-T\_{j-1})/N\_{j}=h for all jj.

The resulting algorithm is a fully forward method: both the forward SDE and all backward equations are simulated forward in time. In contrast to the classical deep BSDE method, the first M−1M-1 compounding conditions specified by gjg\_{j} are not known, as all these gjg\_{j} may depend on the unknown solution YY itself. Consequently, all MM BSDEs must be learned simultaneously. This simultaneous enforcement of all compounding conditions is the defining feature of the Compound BSDE method.

## 3 Convergence Analysis

In this section, we first address the well-posedness of the compound BSDE formulation ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) and collect the L2L^{2}-regularity properties needed in the convergence analysis. Combining these results with the *a posteriori* error estimate for the deep BSDE method applied to ([2.1](https://arxiv.org/html/2601.18634v2#S2.E1 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), we then obtain a concise convergence proof for the Compound BSDE method ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")).

###### Assumption 1.

The coefficients in ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) satisfy the following conditions.

1. (i).

   The mappings
   b:[0,T]×ℝd1→ℝd1b:[0,T]\times\mathbb{R}^{d\_{1}}\to\mathbb{R}^{d\_{1}},
   σ:[0,T]×ℝd1→ℝd1×d3\sigma:[0,T]\times\mathbb{R}^{d\_{1}}\to\mathbb{R}^{d\_{1}\times d\_{3}},
   fj:[Tj−1,Tj]×ℝd1×ℝd2×ℝd2×d3→ℝd2f\_{j}:[T\_{j-1},T\_{j}]\times\mathbb{R}^{d\_{1}}\times\mathbb{R}^{d\_{2}}\times\mathbb{R}^{d\_{2}\times d\_{3}}\to\mathbb{R}^{d\_{2}} for all jj,
   gM:ℝd1→ℝd2g\_{M}:\mathbb{R}^{d\_{1}}\to\mathbb{R}^{d\_{2}}, and
   gj:ℝd1×ℝd2→ℝd2g\_{j}:\mathbb{R}^{d\_{1}}\times\mathbb{R}^{d\_{2}}\to\mathbb{R}^{d\_{2}} for 1≤j≤M−11\leq j\leq M-1,
   are all deterministic.
2. (ii).

   The functions b​(⋅,0)b(\cdot,0) and σ​(⋅,0)\sigma(\cdot,0) are bounded. Moreover, fj​(⋅,0,0,0)f\_{j}(\cdot,0,0,0) for all jj, gj​(0,0)g\_{j}(0,0) for 1≤j≤M−11\leq j\leq M-1, and gM​(0)g\_{M}(0) are bounded.
3. (iii).

   The functions bb, σ\sigma, fjf\_{j}, and gjg\_{j} for all jj, are uniformly Lipschitz continuous in (x,y,z)(x,y,z).
4. (iv).

   The functions bb, σ\sigma, and fjf\_{j} for all jj, are uniformly 12\tfrac{1}{2}-Hölder continuous in tt.

###### Theorem 3.1.

Let Assumption [1](https://arxiv.org/html/2601.18634v2#Thmassumption1 "Assumption 1. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") hold. Then we have the following.

1. (i).

   The compound BSDE ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) admits a unique adapted solution (X,Y,Z)(X,Y,Z).
2. (ii).

   For each j=1,…,Mj=1,\dots,M, there exists a mapping uju\_{j} such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Yj,t=uj​(t,Xt),t∈[Tj−1,Tj],Y\_{j,t}=u\_{j}(t,X\_{t}),\qquad t\in[T\_{j-1},T\_{j}], |  | (3.1) |

   and uju\_{j} is the viscosity solution to the system of semilinear PDEs, for ℓ=1,2,⋯,d2\ell=1,2,\cdots,d\_{2},

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | {∂tujℓ​(t,x)+12​Tr⁡(σ​σT​(t,x)​∂x2ujℓ​(t,x))+bT​(t,x)​∂xujℓ​(t,x)+fjℓ​(t,x,uj​(t,x),(∂xuj​(t,x))T​σ​(t,x))=0,∀(t,x)∈[Tj−1,Tj)×ℝd1,uj​(Tj,x)=g¯j​(x),∀x∈ℝd1,\left\{\begin{aligned} \partial\_{t}u\_{j}^{\ell}(t,x)&+\frac{1}{2}\operatorname{Tr}\Bigl(\sigma\sigma^{\mathrm{T}}(t,x)\partial\_{x}^{2}u\_{j}^{\ell}(t,x)\Bigr)+b^{\mathrm{T}}(t,x)\partial\_{x}u\_{j}^{\ell}(t,x)\\ &\qquad+f\_{j}^{\ell}\Bigl(t,x,u\_{j}(t,x),(\partial\_{x}u\_{j}(t,x))^{\mathrm{T}}\sigma(t,x)\Bigr)=0,\qquad\forall(t,x)\in[T\_{j-1},T\_{j})\times\mathbb{R}^{d\_{1}},\\ u\_{j}(T\_{j},x)&=\bar{g}\_{j}(x),\qquad\forall x\in\mathbb{R}^{d\_{1}},\end{aligned}\right. |  | (3.2) |

   where g¯M​(x)≔gM​(x)\bar{g}\_{M}(x)\coloneqq g\_{M}(x) and, for 1≤j≤M−11\leq j\leq M-1,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g¯j​(x)≔gj​(x,uj+1​(Tj,x)).\bar{g}\_{j}(x)\coloneqq g\_{j}\bigl(x,u\_{j+1}(T\_{j},x)\bigr). |  | (3.3) |

   Moreover, each uju\_{j} is uniformly Lipschitz in xx, i.e.,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ‖uj​(t,x1)−uj​(t,x2)‖≤C​‖x1−x2‖for all ​t∈[Tj−1,Tj],x1,x2∈ℝd1.\|u\_{j}(t,x\_{1})-u\_{j}(t,x\_{2})\|\leq C\|x\_{1}-x\_{2}\|\qquad\text{for all }t\in[T\_{j-1},T\_{j}],\ x\_{1},x\_{2}\in\mathbb{R}^{d\_{1}}. |  | (3.4) |
3. (iii).

   If we additionally assume that uj∈C1,2​([Tj−1,Tj]×ℝd1,ℝd2)u\_{j}\in C^{1,2}([T\_{j-1},T\_{j}]\times\mathbb{R}^{d\_{1}},\mathbb{R}^{d\_{2}}), then the PDE ([3.2](https://arxiv.org/html/2601.18634v2#S3.E2 "In item (ii). ‣ Theorem 3.1. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) holds in the classical sense, and we have, for all jj,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Yj,t=uj​(t,Xt),Zj,t=(∇xuj​(t,Xt))T​σ​(t,Xt),∀t∈[Tj−1,Tj]Y\_{j,t}=u\_{j}(t,X\_{t}),\quad Z\_{j,t}=(\nabla\_{x}u\_{j}(t,X\_{t}))^{\mathrm{T}}\sigma(t,X\_{t}),\quad\forall t\in[T\_{j-1},T\_{j}] |  | (3.5) |

###### Proof.

We argue backwards in time, starting from j=Mj=M. For j=Mj=M, the terminal condition is g¯M=gM\bar{g}\_{M}=g\_{M}, which is Lipschitz by Assumption [1](https://arxiv.org/html/2601.18634v2#Thmassumption1 "Assumption 1. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"). Existence and uniqueness of the BSDE on [TM−1,TM][T\_{M-1},T\_{M}], as well as the Markovian representation YM,t=uM​(t,Xt)Y\_{M,t}=u\_{M}(t,X\_{t}) with uMu\_{M} a viscosity solution that is Lipschitz in xx, follow from standard BSDE theory; see, for instance, Theorems 5.2.1 and 5.5.8 in [[30](https://arxiv.org/html/2601.18634v2#bib.bib30)].

Assume now that the claim holds for uj+1u\_{j+1}. By the Lipschitz continuity of gjg\_{j} in its arguments and the Lipschitz property of uj+1​(Tj,⋅)u\_{j+1}(T\_{j},\cdot), the induced function g¯j​(⋅)\bar{g}\_{j}(\cdot) is again Lipschitz. Applying the same BSDE well-posedness and Markovian representation result on the interval [Tj−1,Tj][T\_{j-1},T\_{j}] yields existence and uniqueness for (Yj,Zj)(Y\_{j},Z\_{j}) and the corresponding PDE representation. Iterating this argument for j=M−1,M−2,…,1j=M-1,M-2,\dots,1 completes the proof.
∎

Using the well-posedness results, we can further derive L2L^{2}-regularity estimates for the solution (X,Y,Z)(X,Y,Z) of ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) based on classical BSDE theory [[31](https://arxiv.org/html/2601.18634v2#bib.bib31), [30](https://arxiv.org/html/2601.18634v2#bib.bib30)]. To simplify the subsequent analysis, we impose Assumption [2](https://arxiv.org/html/2601.18634v2#Thmassumption2 "Assumption 2. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), which ensures that the process ZZ admits a càdlàg modification. For notational convenience, recall the uniform partition π\pi, we define the projection map π​(t)=ti\pi(t)=t\_{i} for t∈[ti,ti+1)t\in[t\_{i},t\_{i+1}).

###### Assumption 2.

The diffusion coefficient σ​(t,x)\sigma(t,x) in ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) satisfies one of the following conditions: either σ​(t,x)\sigma(t,x) is uniformly Lipschitz continuous in tt, or dimensions d1=d3d\_{1}=d\_{3} and the uniform ellipticity condition σ​(t,x)​σ​(t,x)⊤≥δ​𝐈d1\sigma(t,x)\sigma(t,x)^{\top}\geq\delta\mathbf{I}\_{d\_{1}} holds for some constant δ>0\delta>0.

###### Theorem 3.2 (L2L^{2}-regularity).

Let Assumptions [1](https://arxiv.org/html/2601.18634v2#Thmassumption1 "Assumption 1. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") and [2](https://arxiv.org/html/2601.18634v2#Thmassumption2 "Assumption 2. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") hold, and (X,Y,Z)(X,Y,Z) be the solution to the compound BSDE ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). For each j=1,2,…,Mj=1,2,\dots,M, the jj-th BSDE, together with the associated forward process XtX\_{t} on [Tj−1,Tj][T\_{j-1},T\_{j}], satisfies the following regularity estimate,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈[Tj−1,Tj]𝔼​[‖Xt−Xπ​(t)‖2+‖Yj,t−Yj,π​(t)‖2]+𝔼​[∫Tj−1Tj‖Zj,t−Zj,π​(t)‖2​dt]≤C​h,\sup\_{t\in[T\_{j-1},T\_{j}]}\mathbb{E}\!\left[\left\|X\_{t}-X\_{\pi(t)}\right\|^{2}+\left\|Y\_{j,t}-Y\_{j,\pi(t)}\right\|^{2}\right]+\mathbb{E}\!\left[\int\_{T\_{j-1}}^{T\_{j}}\left\|Z\_{j,t}-Z\_{j,\pi(t)}\right\|^{2}\,\mathrm{d}t\right]\leq Ch, |  | (3.6) |

where CC is a constant independent of the time step size hh.

In what follows, we first present a proof for the deep BSDE method for equations of the form ([2.1](https://arxiv.org/html/2601.18634v2#S2.E1 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), as this will serve as the main building block for establishing our Compound BSDE framework. We note that rigorous analyses of related methods have already been carried out in more complex settings, e.g. coupled forward–backward stochastic differential equations [[17](https://arxiv.org/html/2601.18634v2#bib.bib17), [22](https://arxiv.org/html/2601.18634v2#bib.bib22)], BSDEs with jumps [[32](https://arxiv.org/html/2601.18634v2#bib.bib32)], BSDEs with non-Lipschitz coefficients [[33](https://arxiv.org/html/2601.18634v2#bib.bib33)], and mean-field type equations [[34](https://arxiv.org/html/2601.18634v2#bib.bib34)]. In contrast, our objective here is to provide a streamlined and self-contained proof for the basic case. This allows us to emphasize the essential ideas of our Compound BSDE method, while avoiding many of the technical conditions and complications that arise in the complex setting, particularly those associated with an implicit scheme for the BSDE.

The following assumption forms part of the sufficient conditions for convergence, and we shall further discuss it in a later remark. We also recall that the deep BSDE method ([2.2](https://arxiv.org/html/2601.18634v2#S2.E2 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) is a special case of the Compound BSDE method ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) with M=1M=1, where all the subscripts jj are omitted as they are not needed for M=1M=1. This observation clarifies the use of the assumptions in Theorem [3.3](https://arxiv.org/html/2601.18634v2#S3.Thmtheorem3 "Theorem 3.3 (A posteriori error estimate for the deep BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") below.

###### Assumption 3.

The Lipschitz constants of the driver fjf\_{j} with respect to yy and zz are sufficiently small.

###### Theorem 3.3 (A posteriori error estimate for the deep BSDE method).

Let Assumptions [1](https://arxiv.org/html/2601.18634v2#Thmassumption1 "Assumption 1. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), [2](https://arxiv.org/html/2601.18634v2#Thmassumption2 "Assumption 2. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), and [3](https://arxiv.org/html/2601.18634v2#Thmassumption3 "Assumption 3. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") hold for the BSDE ([2.1](https://arxiv.org/html/2601.18634v2#S2.E1 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). Let (𝒳,𝒴,𝒵)(\mathcal{X},\mathcal{Y},\mathcal{Z}) denote its solution, and let (𝒳π,𝒴π,𝒵π)(\mathcal{X}^{\pi},\mathcal{Y}^{\pi},\mathcal{Z}^{\pi}) generated by the deep BSDE method ([2.2](https://arxiv.org/html/2601.18634v2#S2.E2 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). Then the method satisfies the following *a posteriori* error estimate,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈[0,T]𝔼​[‖𝒳t−𝒳π​(t)π‖2+‖𝒴t−𝒴π​(t)π‖2]+∫0T𝔼​[‖𝒵t−𝒵π​(t)π‖2]​dt≤C​(h+𝔼​‖g​(𝒳T)−𝒴Tπ‖2),\sup\_{t\in[0,T]}\mathbb{E}\Big[\|\mathcal{X}\_{t}-\mathcal{X}\_{\pi(t)}^{\pi}\|^{2}+\|\mathcal{Y}\_{t}-\mathcal{Y}\_{\pi(t)}^{\pi}\|^{2}\Big]+\int\_{0}^{T}\mathbb{E}\Big[\|\mathcal{Z}\_{t}-\mathcal{Z}\_{\pi(t)}^{\pi}\|^{2}\Big]\,\mathrm{d}t\leq C\Big(h+\mathbb{E}\|g(\mathcal{X}\_{T})-\mathcal{Y}\_{T}^{\pi}\|^{2}\Big), |  | (3.7) |

where CC is a constant independent of the step size hh.

If there is no direct access to g​(𝒳T)g(\mathcal{X}\_{T}), it can be replaced by g​(𝒳Tπ)g\!\left(\mathcal{X}\_{T}^{\pi}\right) on the right-hand side of ([3.7](https://arxiv.org/html/2601.18634v2#S3.E7 "In Theorem 3.3 (A posteriori error estimate for the deep BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")).

###### Proof.

For 0≤s≤T0\leq s\leq T, we introduce the following notation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​𝒳s≔𝒳s−𝒳π​(s)π,Δ​𝒴s≔𝒴s−𝒴π​(s)π,Δ​𝒵s≔𝒵s−𝒵π​(s)π,\Delta\mathcal{X}\_{s}\coloneqq\mathcal{X}\_{s}-\mathcal{X}\_{\pi(s)}^{\pi},\qquad\Delta\mathcal{Y}\_{s}\coloneqq\mathcal{Y}\_{s}-\mathcal{Y}\_{\pi(s)}^{\pi},\qquad\Delta\mathcal{Z}\_{s}\coloneqq\mathcal{Z}\_{s}-\mathcal{Z}\_{\pi(s)}^{\pi}, |  | (3.8) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​fs≔f​(s,𝒳s,𝒴s,𝒵s)−f​(π​(s),𝒳π​(s)π,𝒴π​(s)π,𝒵π​(s)π),\Delta f\_{s}\coloneqq f(s,\mathcal{X}\_{s},\mathcal{Y}\_{s},\mathcal{Z}\_{s})-f\bigl(\pi(s),\mathcal{X}\_{\pi(s)}^{\pi},\mathcal{Y}\_{\pi(s)}^{\pi},\mathcal{Z}\_{\pi(s)}^{\pi}\bigr), |  | (3.9) |

where we recall that π​(s)=ti\pi(s)=t\_{i} for s∈[ti,ti+1)s\in[t\_{i},t\_{i+1}).

Let CC denote a generic constant that may change from line to line in the rest of the proof, and let KxK\_{x}, KyK\_{y}, and KzK\_{z} denote the Lipschitz constants of ff with respect to xx, yy, and zz. Applying the Cauchy–Schwarz and Hölder inequalities, together with the Lipschitz continuity of the driver ff, we obtain the following useful estimate related to Δ​fs\Delta f\_{s}. For 0≤i≤N0\leq i\leq N,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​‖∫t0tiΔ​fs​𝑑s‖2\displaystyle\mathbb{E}\left\|\int\_{t\_{0}}^{t\_{i}}\Delta f\_{s}ds\right\|^{2} | ≤T​𝔼​∫t0T(h+Kx2​‖Δ​𝒳s‖2+Ky2​‖Δ​𝒴s‖2+Kz2​‖Δ​𝒵s‖2)​𝑑s\displaystyle\leq T\mathbb{E}\int\_{t\_{0}}^{T}\left(h+K\_{x}^{2}\|\Delta\mathcal{X}\_{s}\|^{2}+K\_{y}^{2}\|\Delta\mathcal{Y}\_{s}\|^{2}+K\_{z}^{2}\|\Delta\mathcal{Z}\_{s}\|^{2}\right)ds |  | (3.10) |
|  |  | ≤T2​h+C​T2​Kx2​h+T​Ky2​𝔼​[∫t0T‖Δ​𝒴s‖2​𝑑s]+T​Kz2​𝔼​[∫t0T‖Δ​𝒵s‖2​𝑑s]\displaystyle\leq T^{2}h+CT^{2}K\_{x}^{2}h+TK\_{y}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Y}\_{s}\|^{2}ds\right]+TK\_{z}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}ds\right] |  |
|  |  | ≤C​h+T​Kz2​𝔼​[∫t0T‖Δ​𝒵s‖2​𝑑s]+T​Ky2​𝔼​[∫t0T2​‖𝒴s−𝒴π​(s)‖2+2​‖𝒴π​(s)−𝒴π​(s)π‖2​d​s]\displaystyle\leq Ch+TK\_{z}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}ds\right]+TK\_{y}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}2\|\mathcal{Y}\_{s}-\mathcal{Y}\_{\pi(s)}\|^{2}+2\|\mathcal{Y}\_{\pi(s)}-\mathcal{Y}\_{\pi(s)}^{\pi}\|^{2}ds\right] |  |
|  |  | ≤C​h+T​Kz2​𝔼​[∫t0T‖Δ​𝒵s‖2​𝑑s]+2​T​Ky2​𝔼​[∫t0T‖𝒴π​(s)−𝒴π​(s)π‖2​𝑑s]\displaystyle\leq Ch+TK\_{z}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}ds\right]+2TK\_{y}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\mathcal{Y}\_{\pi(s)}-\mathcal{Y}\_{\pi(s)}^{\pi}\|^{2}ds\right] |  |
|  |  | ≤C​h+T​Kz2​𝔼​[∫t0T‖Δ​𝒵s‖2​𝑑s]+2​T2​Ky2​max0≤i≤N−1⁡𝔼​[‖𝒴ti−𝒴tiπ‖2].\displaystyle\leq Ch+TK\_{z}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}ds\right]+2T^{2}K\_{y}^{2}\max\_{0\leq i\leq N-1}\mathbb{E}\left[\|\mathcal{Y}\_{t\_{i}}-\mathcal{Y}\_{t\_{i}}^{\pi}\|^{2}\right]. |  |

where we used Theorem [3.2](https://arxiv.org/html/2601.18634v2#S3.Thmtheorem2 "Theorem 3.2 (𝐿²-regularity). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") for the L2L^{2}-regularity of 𝒳\mathcal{X} and 𝒴\mathcal{Y} in the second and forth inequalities, respectively.

Consequently, using Itô isometry and ([3.10](https://arxiv.org/html/2601.18634v2#S3.E10 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), for 0≤i≤N0\leq i\leq N we have,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​‖Δ​𝒴ti‖2\displaystyle\mathbb{E}\|\Delta\mathcal{Y}\_{t\_{i}}\|^{2} | =𝔼​‖Δ​𝒴t0−∫t0tiΔ​fs​ds+∫t0tiΔ​𝒵s​dWs‖2\displaystyle=\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}-\int\_{t\_{0}}^{t\_{i}}\Delta f\_{s}\mathrm{d}s+\int\_{t\_{0}}^{t\_{i}}\Delta\mathcal{Z}\_{s}\mathrm{d}W\_{s}\right\|^{2} |  | (3.11) |
|  |  | ≤3​𝔼​‖Δ​𝒴t0‖2+3​𝔼​‖∫t0tiΔ​fs​ds‖2+3​𝔼​‖∫t0tiΔ​𝒵s​dWs‖2\displaystyle\leq 3\mathbb{E}\|\Delta\mathcal{Y}\_{t\_{0}}\|^{2}+3\mathbb{E}\left\|\int\_{t\_{0}}^{t\_{i}}\Delta f\_{s}\mathrm{d}s\right\|^{2}+3\mathbb{E}\left\|\int\_{t\_{0}}^{t\_{i}}\Delta\mathcal{Z}\_{s}\mathrm{d}W\_{s}\right\|^{2} |  |
|  |  | ≤3​𝔼​‖Δ​𝒴t0‖2+3​(C​h+T​Kz2​𝔼​[∫t0T‖Δ​𝒵s‖2​𝑑s]+2​T2​Ky2​max0≤i≤N−1⁡𝔼​‖Δ​𝒴ti‖2)+3​𝔼​[∫t0ti‖Δ​𝒵s‖2​ds]\displaystyle\leq 3\mathbb{E}\|\Delta\mathcal{Y}\_{t\_{0}}\|^{2}+3\left(Ch+TK\_{z}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}ds\right]+2T^{2}K\_{y}^{2}\max\_{0\leq i\leq N-1}\mathbb{E}\|\Delta\mathcal{Y}\_{t\_{i}}\|^{2}\right)+3\mathbb{E}\left[\int\_{t\_{0}}^{t\_{i}}\|\Delta\mathcal{Z}\_{s}\|^{2}\mathrm{d}s\right] |  |
|  |  | =C​h+3​𝔼​‖Δ​𝒴t0‖2+(3​T​Kz2+3)​𝔼​[∫t0T‖Δ​𝒵s‖2​ds]+6​T2​Ky2​max0≤i≤N−1⁡𝔼​‖Δ​𝒴ti‖2.\displaystyle=Ch+3\mathbb{E}\|\Delta\mathcal{Y}\_{t\_{0}}\|^{2}+(3TK\_{z}^{2}+3)\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}\mathrm{d}s\right]+6T^{2}K\_{y}^{2}\max\_{0\leq i\leq N-1}\mathbb{E}\|\Delta\mathcal{Y}\_{t\_{i}}\|^{2}. |  |

Taking the maximum over 0≤i≤N−10\leq i\leq N-1 on the left-hand side of the above inequality, and assuming that 6​T2​Ky2<16T^{2}K\_{y}^{2}<1, which is ensured when Assumption [3](https://arxiv.org/html/2601.18634v2#Thmassumption3 "Assumption 3. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") holds to a sufficient extent, we can rearrange the terms to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | max0≤i≤N−1⁡𝔼​‖Δ​𝒴ti‖2≤C​h+31−6​T2​Ky2​𝔼​‖Δ​𝒴t0‖2+3​(1+T​Kz2)1−6​T2​Ky2​𝔼​[∫0T‖Δ​𝒵s‖2​ds].\max\_{0\leq i\leq N-1}\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{i}}\right\|^{2}\leq Ch+\frac{3}{1-6T^{2}K\_{y}^{2}}\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}\right\|^{2}+\frac{3\left(1+TK\_{z}^{2}\right)}{1-6T^{2}K\_{y}^{2}}\mathbb{E}\left[\int\_{0}^{T}\left\|\Delta\mathcal{Z}\_{s}\right\|^{2}\mathrm{d}s\right]. |  | (3.12) |

It now remains to bound the second and third terms on the right-hand side of ([3.12](https://arxiv.org/html/2601.18634v2#S3.E12 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) in terms of the objective functional
𝔼​‖g​(𝒳T)−𝒴Tπ‖2\mathbb{E}\bigl\|g(\mathcal{X}\_{T})-\mathcal{Y}\_{T}^{\pi}\bigr\|^{2} used in the deep BSDE method ([2.2](https://arxiv.org/html/2601.18634v2#S2.E2 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). Recall that g​(𝒳T)=𝒴Tg(\mathcal{X}\_{T})=\mathcal{Y}\_{T}, then we can derive

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​‖g​(𝒳T)−𝒴Tπ‖2\displaystyle\mathbb{E}\left\|g(\mathcal{X}\_{T})-\mathcal{Y}\_{T}^{\pi}\right\|^{2} |  | (3.13) |
|  | =\displaystyle= | 𝔼​‖Δ​𝒴t0−∫t0TΔ​fs​ds+∫t0TΔ​𝒵s​dWs‖2\displaystyle\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}-\int\_{t\_{0}}^{T}\Delta f\_{s}\mathrm{d}s+\int\_{t\_{0}}^{T}\Delta\mathcal{Z}\_{s}\mathrm{d}W\_{s}\right\|^{2} |  |
|  | =\displaystyle= | 𝔼​‖Δ​𝒴t0−∫t0TΔ​fs​ds‖2+2​𝔼​[(Δ​𝒴t0−∫t0TΔ​fs​ds)⊤​(∫t0TΔ​𝒵s​dWs)]+𝔼​‖∫t0TΔ​𝒵s​dWs‖2\displaystyle\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}-\int\_{t\_{0}}^{T}\Delta f\_{s}\mathrm{d}s\right\|^{2}+2\mathbb{E}\left[\left(\Delta\mathcal{Y}\_{t\_{0}}-\int\_{t\_{0}}^{T}\Delta f\_{s}\mathrm{d}s\right)^{\top}\left(\int\_{t\_{0}}^{T}\Delta\mathcal{Z}\_{s}\mathrm{d}W\_{s}\right)\right]+\mathbb{E}\left\|\int\_{t\_{0}}^{T}\Delta\mathcal{Z}\_{s}\mathrm{d}W\_{s}\right\|^{2} |  |
|  | =\displaystyle= | 𝔼​‖Δ​𝒴t0−∫t0TΔ​fs​ds‖2−2​𝔼​[(∫t0TΔ​fs​ds)⊤​(∫t0TΔ​𝒵s​dWs)]+𝔼​[∫t0T‖Δ​𝒵s‖2​ds]\displaystyle\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}-\int\_{t\_{0}}^{T}\Delta f\_{s}\mathrm{d}s\right\|^{2}-2\mathbb{E}\left[\left(\int\_{t\_{0}}^{T}\Delta f\_{s}\mathrm{d}s\right)^{\top}\left(\int\_{t\_{0}}^{T}\Delta\mathcal{Z}\_{s}\mathrm{d}W\_{s}\right)\right]+\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}\mathrm{d}s\right] |  |
|  | ≥\displaystyle\geq | (1−ϵ)​𝔼​‖Δ​𝒴t0‖2+(1−ϵ−1−δ−1)​𝔼​‖∫t0TΔ​fs​ds‖2+(1−δ)​𝔼​[∫t0T‖Δ​𝒵s‖2​ds],\displaystyle(1-\epsilon)\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}\right\|^{2}+(1-\epsilon^{-1}-\delta^{-1})\mathbb{E}\left\|\int\_{t\_{0}}^{T}\Delta f\_{s}\mathrm{d}s\right\|^{2}+(1-\delta)\mathbb{E}\left[\int\_{t\_{0}}^{T}\left\|\Delta\mathcal{Z}\_{s}\right\|^{2}\mathrm{d}s\right], |  |

where we use the fact that Δ​𝒴t0\Delta\mathcal{Y}\_{t\_{0}} is independent with WsW\_{s} for s≥0s\geq 0, and the constants ϵ>0\epsilon>0 and δ>0\delta>0 arise from the application of Young’s inequality.

Since our goal is to bound the terms 𝔼​‖Δ​𝒴t0‖2\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}\right\|^{2} and 𝔼​∫t0T‖Δ​𝒵s‖2​ds\mathbb{E}\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}\mathrm{d}s in terms of 𝔼​‖g​(𝒳T)−𝒴Tπ‖2\mathbb{E}\left\|g(\mathcal{X}\_{T})-\mathcal{Y}\_{T}^{\pi}\right\|^{2}, we choose 0<ϵ<10<\epsilon<1 and 0<δ<10<\delta<1 so that the corresponding coefficients are positive. Then, using ([3.10](https://arxiv.org/html/2601.18634v2#S3.E10 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), ([3.12](https://arxiv.org/html/2601.18634v2#S3.E12 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), and noticing that (1−ϵ−1−δ−1)<0(1-\epsilon^{-1}-\delta^{-1})<0, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (1−ϵ−1−δ−1)​𝔼​‖Δ​∫t0Tfs​ds‖2\displaystyle(1-\epsilon^{-1}-\delta^{-1})\mathbb{E}\left\|\Delta\int\_{t\_{0}}^{T}f\_{s}\mathrm{d}s\right\|^{2} |  | (3.14) |
|  | ≥\displaystyle\geq | (1−ϵ−1−δ−1)​(C​h+T​Kz2​𝔼​[∫t0T‖Δ​𝒵s‖2​𝑑s]+2​T2​Ky2​max0≤i≤N−1⁡𝔼​‖Δ​𝒴ti‖2)\displaystyle(1-\epsilon^{-1}-\delta^{-1})\left(Ch+TK\_{z}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}ds\right]+2T^{2}K\_{y}^{2}\max\_{0\leq i\leq N-1}\mathbb{E}\|\Delta\mathcal{Y}\_{t\_{i}}\|^{2}\right) |  |
|  | ≥\displaystyle\geq | (1−ϵ−1−δ−1)(Ch+TKz2𝔼[∫t0T∥Δ𝒵s∥2ds]+2T2Ky2(Ch+31−6​T2​Ky2𝔼∥Δ𝒴t0∥2\displaystyle(1-\epsilon^{-1}-\delta^{-1})\left(Ch+TK\_{z}^{2}\mathbb{E}\left[\int\_{t\_{0}}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}ds\right]+2T^{2}K\_{y}^{2}\left(Ch+\frac{3}{1-6T^{2}K\_{y}^{2}}\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}\right\|^{2}\right.\right. |  |
|  |  | +3​(1+T​Kz2)1−6​T2​Ky2𝔼[∫0T∥Δ𝒵s∥2ds])).\displaystyle\qquad\left.\left.+\frac{3\left(1+TK\_{z}^{2}\right)}{1-6T^{2}K\_{y}^{2}}\mathbb{E}\left[\int\_{0}^{T}\|\Delta\mathcal{Z}\_{s}\|^{2}\mathrm{d}s\right]\right)\right). |  |

Substituting this lower bound into to ([3.13](https://arxiv.org/html/2601.18634v2#S3.E13 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) yields,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​‖g​(𝒳T)−𝒴Tπ‖2\displaystyle\mathbb{E}\left\|g(\mathcal{X}\_{T})-\mathcal{Y}\_{T}^{\pi}\right\|^{2} | ≥(1−ϵ−1−δ−1)​C​h+[1−ϵ+(1−ϵ−1−δ−1)​6​T2​Ky21−6​T2​Ky]​𝔼​‖Δ​𝒴t0‖2\displaystyle\geq(1-\epsilon^{-1}-\delta^{-1})Ch+\left[1-\epsilon+(1-\epsilon^{-1}-\delta^{-1})\frac{6T^{2}K\_{y}^{2}}{1-6T^{2}K\_{y}}\right]\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}\right\|^{2} |  | (3.15) |
|  |  | +[(1−ϵ−1−δ−1)​(T​Kz2+2​T2​Ky2​3+3​T​Kz21−6​T2​Ky2)+1−δ]​𝔼​[∫t0T‖Δ​𝒵s‖2​ds].\displaystyle\quad+\left[(1-\epsilon^{-1}-\delta^{-1})\left(TK\_{z}^{2}+2T^{2}K\_{y}^{2}\frac{3+3TK\_{z}^{2}}{1-6T^{2}K\_{y}^{2}}\right)+1-\delta\right]\mathbb{E}\left[\int\_{t\_{0}}^{T}\left\|\Delta\mathcal{Z}\_{s}\right\|^{2}\mathrm{d}s\right]. |  |

Finally, to obtain the desired estimate, the coefficients in front of
𝔼​∫t0T‖Δ​𝒵s‖2​ds\mathbb{E}\!\int\_{t\_{0}}^{T}\left\|\Delta\mathcal{Z}\_{s}\right\|^{2}\mathrm{d}s
and
𝔼​‖Δ​𝒴t0‖2\mathbb{E}\left\|\Delta\mathcal{Y}\_{t\_{0}}\right\|^{2}
in ([3.15](https://arxiv.org/html/2601.18634v2#S3.E15 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) must be positive. In addition to the conditions
0<ε<10<\varepsilon<1 and 0<δ<10<\delta<1, this leads to the following conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−ϵ−1−δ−1)​(T​Kz2+2​T2​Ky2​3+3​T​Kz21−6​T2​Ky2)+1−δ>0,1−ϵ+(1−ϵ−1−δ−1)​6​T2​Ky21−6​T2​Ky2>0(1-\epsilon^{-1}-\delta^{-1})\left(TK\_{z}^{2}+2T^{2}K\_{y}^{2}\frac{3+3TK\_{z}^{2}}{1-6T^{2}K\_{y}^{2}}\right)+1-\delta>0,\quad 1-\epsilon+(1-\epsilon^{-1}-\delta^{-1})\frac{6T^{2}K\_{y}^{2}}{1-6T^{2}K\_{y}^{2}}>0 |  | (3.16) |

These conditions can, for instance, be satisfied by choosing
ε=δ=12\varepsilon=\delta=\tfrac{1}{2} and requiring

|  |  |  |
| --- | --- | --- |
|  | T​Kz2+2​T2​Ky2​3+3​T​Kz21−6​T2​Ky2<16,TK\_{z}^{2}+2T^{2}K\_{y}^{2}\frac{3+3TK\_{z}^{2}}{1-6T^{2}K\_{y}^{2}}<\frac{1}{6}, |  |

which is clearly achievable when KyK\_{y} and KzK\_{z} are sufficiently small.

We move the negative term (1−ε−1−δ−1)​C​h(1-\varepsilon^{-1}-\delta^{-1})\,Ch in ([3.15](https://arxiv.org/html/2601.18634v2#S3.E15 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) to the left-hand side, and invoke the L2L^{2}-regularity of the forward process 𝒳\mathcal{X} to complete the proof. For the case 𝔼​‖g​(𝒳Tπ)−𝒴Tπ‖2\mathbb{E}\!\left\|g(\mathcal{X}\_{T}^{\pi})-\mathcal{Y}\_{T}^{\pi}\right\|^{2}, the result follows from the triangle inequality together with the Lipschitz continuity of gg.

∎

###### Remark 1.

We note that Assumption [3](https://arxiv.org/html/2601.18634v2#Thmassumption3 "Assumption 3. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") can, in principle, be made fully explicit by deriving concrete upper bounds for the Lipschitz constants KyK\_{y} and KzK\_{z}. However, obtaining optimal or near-optimal bounds in this way leads to a rather involved optimization problem.

Although this is not the main focus of the present paper, we briefly comment on how to set up this optimization problem. From the proof of Theorem [3.3](https://arxiv.org/html/2601.18634v2#S3.Thmtheorem3 "Theorem 3.3 (A posteriori error estimate for the deep BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), the required conditions on KyK\_{y} and KzK\_{z} essentially arise from two sources:
(i) the repeated application of Young’s inequality to control product terms, and
(ii) the sign conditions imposed on certain coefficients to guarantee positivity or negativity where required.

Therefore, one may introduce several auxiliary parameters λi\lambda\_{i}, in addition to ϵ\epsilon and δ\delta, when applying Young’s inequality throughout the proof. This leads to a system of inequalities involving KyK\_{y}, KzK\_{z}, TT, λi\lambda\_{i}, ε\varepsilon, and δ\delta, which must be satisfied simultaneously, or a constrained optimisation problem if we aim to find the largest admissible values of KyK\_{y} and KzK\_{z} and TT.

With these results in place, we are now ready to give a simple proof of our method, which exploits structural properties of the deep BSDE method for a single BSDE, and the Lipschitz continuity of the compounding conditions gjg\_{j}.

###### Theorem 3.4 (Convergence of the Compound BSDE method).

Let Assumptions [1](https://arxiv.org/html/2601.18634v2#Thmassumption1 "Assumption 1. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), [2](https://arxiv.org/html/2601.18634v2#Thmassumption2 "Assumption 2. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), and [3](https://arxiv.org/html/2601.18634v2#Thmassumption3 "Assumption 3. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") hold, and (X,Y,Z)(X,Y,Z) be the solution to ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). Then the approximated solution (Xπ,Yπ,Zπ)(X^{\pi},Y^{\pi},Z^{\pi}) obtained by the Compound BSDE method ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) satisfies the following *a posteriori* error estimate,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supt∈[0,T]𝔼​‖Xt−Xπ​(t)π‖2+∑j=1M(supt∈[Tj−1,Tj]𝔼​‖Yj,t−Yj,π​(t)π‖2+∫Tj−1Tj𝔼​‖Zj,t−Zj,π​(t)π‖2​dt)\displaystyle\sup\_{t\in[0,T]}\mathbb{E}\|X\_{t}-X\_{\pi(t)}^{\pi}\|^{2}+\sum\_{j=1}^{M}\left(\sup\_{t\in[T\_{j-1},T\_{j}]}\mathbb{E}\|Y\_{j,t}-Y\_{j,\pi(t)}^{\pi}\|^{2}+\int\_{T\_{j-1}}^{T\_{j}}\mathbb{E}\|Z\_{j,t}-Z\_{j,\pi(t)}^{\pi}\|^{2}\mathrm{~d}t\right) |  | (3.17) |
|  |  | ≤C​(h+∑j=1M−1𝔼​‖gj​(XTjπ,Yj+1,Tjπ)−Yj,Tjπ‖2+𝔼​‖gM​(XTπ)−YM,Tπ‖2),\displaystyle\hskip 113.81102pt\leq C\left(h+\sum\_{j=1}^{M-1}\mathbb{E}\|g\_{j}(X\_{T\_{j}}^{\pi},Y\_{j+1,T\_{j}}^{\pi})-Y\_{j,T\_{j}}^{\pi}\|^{2}+\mathbb{E}\|g\_{M}(X\_{T}^{\pi})-Y\_{M,T}^{\pi}\|^{2}\right), |  |

where CC is a constant independent of the step size hh.

###### Proof.

We apply Theorem [3.7](https://arxiv.org/html/2601.18634v2#S3.E7 "In Theorem 3.3 (A posteriori error estimate for the deep BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") to the jj-th BSDE in the Compound BSDE formulation ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), for j=1,2,…,M−1j=1,2,\ldots,M-1,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supt∈[Tj−1,Tj](𝔼​‖Xj,t−Xj,π​(t)π‖2+𝔼​‖Yj,t−Yj,π​(t)π‖2)+∫Tj−1Tj𝔼​‖Zj,t−Zj,π​(t)π‖2​dt\displaystyle\sup\_{t\in[T\_{j-1},T\_{j}]}\left(\mathbb{E}\|X\_{j,t}-X\_{j,\pi(t)}^{\pi}\|^{2}+\mathbb{E}\|Y\_{j,t}-Y\_{j,\pi(t)}^{\pi}\|^{2}\right)+\int\_{T\_{j-1}}^{T\_{j}}\mathbb{E}\|Z\_{j,t}-Z\_{j,\pi(t)}^{\pi}\|^{2}\mathrm{~d}t |  | (3.18) |
|  | ≤\displaystyle\leq | C​𝔼​‖Yj,Tjπ−gj​(XTj,Yj+1,Tj)‖2+C​h\displaystyle C\mathbb{E}\|Y\_{j,T\_{j}}^{\pi}-g\_{j}(X\_{T\_{j}},Y\_{j+1,T\_{j}})\|^{2}+Ch |  |
|  | ≤\displaystyle\leq | C​𝔼​‖Yj,Tjπ−gj​(XTjπ,Yj+1,Tjπ)‖2+C​𝔼​‖gj​(XTjπ,Yj+1,Tjπ)−gj​(XTj,Yj+1,Tj)‖2+C​h\displaystyle C\mathbb{E}\|Y\_{j,T\_{j}}^{\pi}-g\_{j}(X\_{T\_{j}}^{\pi},Y\_{j+1,T\_{j}}^{\pi})\|^{2}+C\mathbb{E}\|g\_{j}(X\_{T\_{j}}^{\pi},Y\_{j+1,T\_{j}}^{\pi})-g\_{j}(X\_{T\_{j}},Y\_{j+1,T\_{j}})\|^{2}+Ch |  |
|  | ≤\displaystyle\leq | C​𝔼​‖Yj,Tjπ−gj​(XTjπ,Yj+1,Tjπ)‖2+C​𝔼​‖Yj+1,Tjπ−Yj+1,Tj‖2+C​𝔼​‖XTjπ−XTj‖2+C​h\displaystyle C\mathbb{E}\|Y\_{j,T\_{j}}^{\pi}-g\_{j}(X\_{T\_{j}}^{\pi},Y\_{j+1,T\_{j}}^{\pi})\|^{2}+C\mathbb{E}\|Y\_{j+1,T\_{j}}^{\pi}-Y\_{j+1,T\_{j}}\|^{2}+C\mathbb{E}\|X\_{T\_{j}}^{\pi}-X\_{T\_{j}}\|^{2}+Ch |  |
|  | ≤\displaystyle\leq | C​𝔼​‖Yj,Tjπ−gj​(XTjπ,Yj+1,Tjπ)‖2+C​𝔼​‖Yj+1,Tjπ−Yj+1,Tj‖2+C​h,\displaystyle C\mathbb{E}\|Y\_{j,T\_{j}}^{\pi}-g\_{j}(X\_{T\_{j}}^{\pi},Y\_{j+1,T\_{j}}^{\pi})\|^{2}+C\mathbb{E}\|Y\_{j+1,T\_{j}}^{\pi}-Y\_{j+1,T\_{j}}\|^{2}+Ch, |  |

where CC denote a generic constant that may change from line to line, and we use the triangle inequality in the second inequality to split the term, since we do not have access to Yj+1,TjY\_{j+1,T\_{j}}, which is part of the solution of ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) that needs to be solved for. The remaining derivations follow from the Lipschitz continuity of gjg\_{j} and the L2L^{2}-regularity of the XX process.

For the case j=Mj=M, note that typically we have access to the samples for gM​(XTπ)g\_{M}(X\_{T}^{\pi}) via numerical methods for the SDE of XX, and thus applying Theorem [3.7](https://arxiv.org/html/2601.18634v2#S3.E7 "In Theorem 3.3 (A posteriori error estimate for the deep BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") again gives,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supt∈[TM−1,TM](𝔼​‖XM,t−XM,π​(t)π‖2+𝔼​‖YM,t−YM,π​(t)π‖2)+∫TM−1TM𝔼​‖ZM,t−ZM,π​(t)π‖2​dt\displaystyle\sup\_{t\in[T\_{M-1},T\_{M}]}\left(\mathbb{E}\|X\_{M,t}-X\_{M,\pi(t)}^{\pi}\|^{2}+\mathbb{E}\|Y\_{M,t}-Y\_{M,\pi(t)}^{\pi}\|^{2}\right)+\int\_{T\_{M-1}}^{T\_{M}}\mathbb{E}\|Z\_{M,t}-Z\_{M,\pi(t)}^{\pi}\|^{2}\mathrm{~d}t |  | (3.19) |
|  | ≤\displaystyle\leq | C​(𝔼​‖YM,TMπ−gj​(XTMπ)‖2+h).\displaystyle C\left(\mathbb{E}\|Y\_{M,T\_{M}}^{\pi}-g\_{j}(X\_{T\_{M}}^{\pi})\|^{2}+h\right). |  |

Fixing some 1≤j≤M−21\leq j\leq M-2, we notice that the second term in the last inequality of ([3.18](https://arxiv.org/html/2601.18634v2#S3.E18 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) can be controlled by using the estimate ([3.18](https://arxiv.org/html/2601.18634v2#S3.E18 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) for the (j+1)(j+1)-th BSDE, as this second term in the jj-th case will appear on the left-hand side in the j+1j+1-case. Through a similar recursive argument, all these second terms in the last lines of ([3.18](https://arxiv.org/html/2601.18634v2#S3.E18 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), for j=1,2​⋯,M−1j=1,2\cdots,M-1, will be bounded by the right-hand-side of ([3.19](https://arxiv.org/html/2601.18634v2#S3.E19 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), provided that all the first terms 𝔼​‖Yj,Tjπ−gj​(XTjπ,Yj+1,Tjπ)‖\mathbb{E}\|Y\_{j,T\_{j}}^{\pi}-g\_{j}(X\_{T\_{j}}^{\pi},Y\_{j+1,T\_{j}}^{\pi})\| in ([3.18](https://arxiv.org/html/2601.18634v2#S3.E18 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) can be controlled. Therefore, we only need to keep all these first terms in ([3.18](https://arxiv.org/html/2601.18634v2#S3.E18 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) and the right-hand side in ([3.19](https://arxiv.org/html/2601.18634v2#S3.E19 "In Proof. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), and obtain the desired estimate.

∎

###### Remark 2.

Inspecting the proof, we observe that it is possible to include the ZZ process in gjg\_{j} for 1≤j≤M−11\leq j\leq M-1, in the compound BSDE formulation ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). This extension, however, would require stronger regularity assumptions on the decoupling field associated with the ZZ process; for example, one may assume that the function (∇xuj​(t,Xt))T​σ​(t,Xt)(\nabla\_{x}u\_{j}(t,X\_{t}))^{\mathrm{T}}\sigma(t,X\_{t}) is uniformly Lipschitz continuous in XtX\_{t} for all jj. A rigorous treatment of this extension is left for future research.

## 4 Applications in derivatives pricing

In this section, we illustrate how the compound BSDE formulation ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) and the associated *fully forward* method ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) can be used for option pricing and optimal stopping problems. The key ingredient is the flexibility in the choice of the compounding functions gjg\_{j}. Unlike standard BSDE formulations, where only the terminal condition at TT is prescribed, our framework allows one to impose conditions at intermediate times TjT\_{j} as well. This makes it possible to represent a wide range of payoff structures and early-exercise features within a single template.

We next discuss several representative choices of gjg\_{j} and explain the corresponding pricing or stopping problems.

Case 1: gj​(x,y)=yg\_{j}(x,y)=y for all jj.

With gj​(x,y)=yg\_{j}(x,y)=y, the compound BSDE ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) collapses to a standard BSDE of the form ([2.1](https://arxiv.org/html/2601.18634v2#S2.E1 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), and the method ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) reduces to the classical deep BSDE method ([2.2](https://arxiv.org/html/2601.18634v2#S2.E2 "In 2.1 Review of the deep BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). Indeed, the intermediate loss terms

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖Yj,Tjπ−gj​(Yj+1,Tjπ)‖2=𝔼​‖Yj,Tjπ−Yj+1,Tjπ‖2\mathbb{E}\bigl\|Y\_{j,T\_{j}}^{\pi}-g\_{j}(Y\_{j+1,T\_{j}}^{\pi})\bigr\|^{2}=\mathbb{E}\bigl\|Y\_{j,T\_{j}}^{\pi}-Y\_{j+1,T\_{j}}^{\pi}\bigr\|^{2} |  |

enforce consistency across the sub-intervals; when these terms are small, we have
Yj,Tjπ≈Yj+1,TjπY\_{j,T\_{j}}^{\pi}\approx Y\_{j+1,T\_{j}}^{\pi} for j=1,…,M−1j=1,\dots,M-1.
In that regime, the dominant contribution to the loss is the terminal term

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖YM,TMπ−gM​(XTMπ)‖2,\mathbb{E}\bigl\|Y\_{M,T\_{M}}^{\pi}-g\_{M}(X\_{T\_{M}}^{\pi})\bigr\|^{2}, |  |

which is exactly the deep BSDE objective.

As a canonical example, consider the pricing of a European put option in the Black–Scholes–Merton model under the risk-neutral measure. Let XX follow a geometric Brownian motion and choose
fj​(t,x,y,z)=−r​yf\_{j}(t,x,y,z)=-ry for all jj, where rr is the risk-free rate. With terminal condition gM​(x)=(K−x)+g\_{M}(x)=(K-x)^{+}, the BSDE solution satisfies Yt=V​(t,Xt)Y\_{t}=V(t,X\_{t}) and
Zt=Vx​(t,Xt)⊤​σ​(t,Xt)Z\_{t}=V\_{x}(t,X\_{t})^{\top}\sigma(t,X\_{t}) by the nonlinear Feynman–Kac representation ([3.5](https://arxiv.org/html/2601.18634v2#S3.E5 "In item (iii). ‣ Theorem 3.1. ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), so that the processes (Y,Z)(Y,Z) correspond to the option price and the scaled option delta over the whole time horizon [0,T][0,T], respectively.

Case 2: gj​(x,y)=max⁡(y−Kj,0)g\_{j}(x,y)=\max(y-K\_{j},0) for constants KjK\_{j} and 1≤j≤M−11\leq j\leq M-1.

For gj​(x,y)=(y−Kj)+≡max⁡(y−Kj,0)g\_{j}(x,y)=(y-K\_{j})^{+}\equiv\max(y-K\_{j},0), the compound BSDE ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) can be interpreted as a discrete-time reflection mechanism at the prescribed times TjT\_{j}, with constant thresholds KjK\_{j}. In particular, for j=1,…,M−1j=1,\dots,M-1, the compounding condition

|  |  |  |
| --- | --- | --- |
|  | Yj,Tj=(Yj+1,Tj−Kj)+Y\_{j,T\_{j}}=(Y\_{j+1,T\_{j}}-K\_{j})^{+} |  |

maps the ”next-stage value” Yj+1,TjY\_{j+1,T\_{j}} into the previous stage through a payoff-type nonlinearity.

A natural application is the pricing of compound options. For illustration, consider a call-on-call option with M=2M=2. Let Vcoc​(t,xt)V\_{\mathrm{coc}}(t,x\_{t}) denote the call-on-call option price at (t,xt)(t,x\_{t}) with maturity T1T\_{1}, and let Vc​(t,xt)V\_{\mathrm{c}}(t,x\_{t}) denote the vanilla European call option price at (t,xt)(t,x\_{t}) with maturity T2>T1T\_{2}>T\_{1}. At time T1T\_{1}, the call-on-call option holder may buy the vanilla call by paying the strike K1K\_{1}, hence the holder’s payoff at T1T\_{1} is

|  |  |  |
| --- | --- | --- |
|  | Vcoc​(T1,x)=(Vc​(T1,x)−K1)+.V\_{\mathrm{coc}}(T\_{1},x)=(V\_{\mathrm{c}}(T\_{1},x)-K\_{1})^{+}. |  |

If exercised, the remaining position is the vanilla call with a terminal payoff
Vc​(T2,x)=(XT2−K2)+V\_{\mathrm{c}}(T\_{2},x)=(X\_{T\_{2}}-K\_{2})^{+}.

Compound options also arise naturally as real options in corporate finance, energy investment, and R&D investment. In such settings, a call-on-call represents the right to acquire an investment opportunity at a future date rather than committing immediately. Paying an initial premium preserves the flexibility to invest only if conditions evolve favourably, thereby limiting downside risk while retaining upside potential. This captures the value of waiting, learning, and managerial flexibility under uncertainty.

To apply ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) in the Black–Scholes–Merton framework, we take the same geometric Brownian motion XX and the driver fj​(t,x,y,z)=−r​yf\_{j}(t,x,y,z)=-ry as in Case [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"). Then, by the Feynman–Kac representation, (Y1,Y2)(Y\_{1},Y\_{2}) corresponds to (Vcoc,Vc)(V\_{\mathrm{coc}},V\_{\mathrm{c}}) in the call-on-call example. The same construction extends directly to other compound options and to MM-fold compound options with M≥2M\geq 2; for instance, a put-on-put can be handled by replacing the compounding payoff with gj​(x,y)=(Kj−y)+g\_{j}(x,y)=(K\_{j}-y)^{+} while keeping the dynamics and driver unchanged.

Case 3: gj​(x,y)=max⁡(y,(x−Kj)+)g\_{j}(x,y)=\max\bigl(y,(x-K\_{j})^{+}\bigr) for constants KjK\_{j} and 1≤j≤M−11\leq j\leq M-1.

This choice generalises Case [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") by allowing the compounding condition to incorporate an *immediate exercise value* (x−Kj)+(x-K\_{j})^{+} that depends on the state XTjX\_{T\_{j}}. The resulting condition compares continuation and exercise values at each TjT\_{j}, which is precisely the structure of Bermudan-style optimal stopping.

To see this, consider a Bermudan call option with exercise dates
𝒯≔{Tj:j=1,…,M}\mathcal{T}\coloneqq\{T\_{j}:\,j=1,\dots,M\}.
At each date TjT\_{j}, the option value satisfies the dynamic programming principle

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yj,Tj=max⁡(Yj+1,Tj,(XTj−Kj)+),Y\_{j,T\_{j}}=\max\!\Bigl(Y\_{j+1,T\_{j}},\,(X\_{T\_{j}}-K\_{j})^{+}\Bigr), |  | (4.1) |

where Yj+1,TjY\_{j+1,T\_{j}} represents the continuation value. Therefore, if the loss in ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) is sufficiently small, the compounding conditions enforce ([4.1](https://arxiv.org/html/2601.18634v2#S4.E1 "In 4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) to high accuracy, and the resulting learned solution provides the Bermudan price. An American option can be approached by refining the grid of exercise times, so that the Bermudan approximation becomes accurate.

###### Remark 3.

In light of the above discussion, it is natural to relate our compound BSDE method ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) to the so-called discretely reflected BSDEs [[8](https://arxiv.org/html/2601.18634v2#bib.bib8), [30](https://arxiv.org/html/2601.18634v2#bib.bib30)]. To illustrate this connection, consider the Bermudan option pricing problem described in Case [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") and use the same set 𝒯\mathcal{T}. This problem can be modelled by the following discretely reflected BSDE,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {YTM=gM​(XTM),Y~t=YTj+∫tTjr​Ys​𝑑s−∫tTjZs​𝑑Ws,t∈[Tj−1,Tj),YTj−1=max⁡(Y~Tj−1,(XTj−1−Kj)+)≔ℛj−1​(XTj−1,Y~Tj−1).\left\{\begin{aligned} Y\_{T\_{M}}&=g\_{M}(X\_{T\_{M}}),\\ \widetilde{Y}\_{t}&=Y\_{T\_{j}}+\int\_{t}^{T\_{j}}r\,Y\_{s}\,ds-\int\_{t}^{T\_{j}}Z\_{s}\,dW\_{s},\qquad t\in[T\_{j-1},T\_{j}),\\ Y\_{T\_{j-1}}&=\max\!\Big(\widetilde{Y}\_{T\_{j-1}},(X\_{T\_{j-1}}-K\_{j})^{+}\Big)\;\coloneqq\;\mathcal{R}\_{j-1}\!\big(X\_{T\_{j-1}},\widetilde{Y}\_{T\_{j-1}}\big).\end{aligned}\right. |  | (4.2) |

Such equations are typically solved in a backward manner; see the references discussed in Section [1](https://arxiv.org/html/2601.18634v2#S1 "1 Introduction ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance").

Comparing ([4.2](https://arxiv.org/html/2601.18634v2#S4.E2 "In Remark 3. ‣ 4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) with the compound BSDE formulation ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), we observe that the reflection operator ℛj−1\mathcal{R}\_{j-1} plays essentially the same role as the function gj−1g\_{j-1} in our framework. From this viewpoint, our method can also be interpreted as a numerical scheme for discretely reflected BSDEs of the form ([4.2](https://arxiv.org/html/2601.18634v2#S4.E2 "In Remark 3. ‣ 4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) with Lipschitz ℛj−1\mathcal{R}\_{j-1}. Moreover, the reason why our algorithm can be implemented in a forward training manner becomes clear from this perspective: instead of enforcing the hard constraint via directly computing

|  |  |  |
| --- | --- | --- |
|  | YTj−1=ℛj−1​(XTj−1,Y~Tj−1),Y\_{T\_{j-1}}=\mathcal{R}\_{j-1}\!\big(X\_{T\_{j-1}},\widetilde{Y}\_{T\_{j-1}}\big), |  |

as done, for example, by the max method in [[23](https://arxiv.org/html/2601.18634v2#bib.bib23)], or methods in [[29](https://arxiv.org/html/2601.18634v2#bib.bib29)] [[19](https://arxiv.org/html/2601.18634v2#bib.bib19)], we adopt a relaxed formulation by incorporating this reflection relation into the objective functional.

## 5 Numerical examples

In this section, we examine the accuracy and efficiency of the proposed Compound BSDE method for several option pricing problems. In particular, we include Bermudan-style options in high dimensions.

To assess accuracy, we consider examples under geometric Brownian motion (GBM) dynamics. In this setting, compound options admit analytical formulas, and reliable benchmark methods are available for Bermudan options. Let Xt=(Xt1,…,Xtd1)⊤X\_{t}=(X\_{t}^{1},\dots,X\_{t}^{d\_{1}})^{\top} denote the underlying asset-price vector. Under the risk-neutral measure, we assume that XX follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=diag⁡(Xt)​((r​𝟏d1−q)​d​t+Σ​d​Wt),X0=x0,dX\_{t}=\operatorname{diag}(X\_{t})\bigl((r\mathbf{1}\_{d\_{1}}-q)\,dt+\Sigma\,dW\_{t}\bigr),\qquad X\_{0}=x\_{0}, |  | (5.1) |

where 𝟏d1∈ℝd1\mathbf{1}\_{d\_{1}}\in\mathbb{R}^{d\_{1}} is the vector of ones, rr is the risk-free rate, q=(q1,…,qd1)⊤q=(q\_{1},\dots,q\_{d\_{1}})^{\top} is the vector of continuous dividend yields, Σ∈ℝd1×d1\Sigma\in\mathbb{R}^{d\_{1}\times d\_{1}} is the volatility matrix, and WtW\_{t} is a d1d\_{1}-dimensional standard Brownian motion with independent components and thus d3=d1d\_{3}=d\_{1}. The dimension d1d\_{1} and the parameter choices are specified in each numerical experiment below.

We also investigate the accuracy of the bound in ([3.17](https://arxiv.org/html/2601.18634v2#S3.E17 "In Theorem 3.4 (Convergence of the Compound BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). When a reference (analytical or highly accurate) solution (X,Y,Z)(X,Y,Z) to ([2.3](https://arxiv.org/html/2601.18634v2#S2.E3 "In 2.3 Definition of the compound BSDE ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) is available, we report the following error metrics for the numerical solution (Xπ,Yπ,Zπ)(X^{\pi},Y^{\pi},Z^{\pi}) generated by the Compound BSDE method ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Err⁡(X)≔supt∈[0,T]𝔼​‖Xπ​(t)−Xπ​(t)π‖2,Err⁡(Y)≔sup1≤j≤Msupt∈[Tj−1,Tj]𝔼​‖Yj,π​(t)−Yj,π​(t)π‖2,\displaystyle\operatorname{Err}(X)\coloneqq\sup\_{t\in[0,T]}\mathbb{E}\left\|X\_{\pi(t)}-X\_{\pi(t)}^{\pi}\right\|^{2},\qquad\operatorname{Err}(Y)\coloneqq\sup\_{1\leq j\leq M}\sup\_{t\in[T\_{j-1},T\_{j}]}\mathbb{E}\left\|Y\_{j,{\pi(t)}}-Y\_{j,{\pi(t)}}^{\pi}\right\|^{2}, |  | (5.2) |
|  |  | Err⁡(Z)≔∑j=1M∑ti∈[Tj−1,Tj]𝔼​‖Zj,ti−Zj,tiπ‖2​h,Total​Err≔Err⁡(X)+Err⁡(Y)+Err⁡(Z).\displaystyle\operatorname{Err}(Z)\coloneqq\sum\_{j=1}^{M}\sum\_{t\_{i}\in[T\_{j-1},T\_{j}]}\mathbb{E}\left\|Z\_{j,t\_{i}}-Z\_{j,t\_{i}}^{\pi}\right\|^{2}h,\qquad\operatorname{Total\ Err}\coloneqq\operatorname{Err}(X)+\operatorname{Err}(Y)+\operatorname{Err}(Z). |  |

where the expectation is approximated by the sample mean via Monte Carlo. Since our primary focus is option pricing, we additionally report the mean squared error of the option price and delta at time t=0t=0, together with the corresponding relative mean squared errors obtained by normalising with the mean squared reference quantities.

Regarding implementation, we use a fully connected neural network with two hidden layers, each with 10+d110+d\_{1} neurons, and tanh\tanh activations. The batch size and validation size are both 50005000, corresponding to the number of simulated sample paths used per parameter update. We train with the Adam optimizer and an exponential learning-rate decay schedule with an initial learning rate 0.010.01. All computations are performed in PyTorch 2.4 on a MacBook Pro with an Apple M1 chip and 16 GB RAM. The code for the numerical experiments can be found in the GitHub repository: <https://github.com/zhipeng-huang/thecompoundbsde>.

### 5.1 Plain compound options with M=2M=2

We begin with a simple one-dimensional setting, namely plain compound options with M=2M=2: call-on-call, call-on-put, put-on-call, and put-on-put. Under geometric Brownian motion dynamics and the risk-neutral measure, all four admit analytical formulas; see [[35](https://arxiv.org/html/2601.18634v2#bib.bib35)] for the call-on-call case. Let Vcoc​(t,xt)V\_{\text{coc}}(t,x\_{t}) denote the price of the call-on-call option at current state (t,xt)(t,x\_{t}) for 0≤t<T10\leq t<T\_{1}, with strike prices KjK\_{j} and exercise times TjT\_{j} for j=1,2j=1,2, and we use analogous notation for the other three contracts.

The reference option prices are given by,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vcoc​(t,xt)\displaystyle V\_{\text{coc}}(t,x\_{t}) | =xt​e−q​(T2−t)​Φ2​(a1,b1;P(2))−K2​e−r​(T2−t)​Φ2​(a2,b2;P(2))−K1​e−r​(T1−t)​Φ​(a2),\displaystyle=x\_{t}e^{-q(T\_{2}-t)}\Phi\_{2}(a\_{1},b\_{1};P^{(2)})-K\_{2}e^{-r(T\_{2}-t)}\Phi\_{2}(a\_{2},b\_{2};P^{(2)})-K\_{1}e^{-r(T\_{1}-t)}\Phi(a\_{2}), |  | (5.3) |
|  | Vcop​(t,xt)\displaystyle V\_{\text{cop}}(t,x\_{t}) | =K2​e−r​(T2−t)​Φ2​(a2,−b2;−P(2))−xt​e−q​(T2−t)​Φ2​(a1,−b1;−P(2))−K1​e−r​(T1−t)​Φ​(a2),\displaystyle=K\_{2}e^{-r(T\_{2}-t)}\Phi\_{2}(a\_{2},-b\_{2};-P^{(2)})-x\_{t}e^{-q(T\_{2}-t)}\Phi\_{2}(a\_{1},-b\_{1};-P^{(2)})-K\_{1}e^{-r(T\_{1}-t)}\Phi(a\_{2}), |  |
|  | Vpoc​(t,xt)\displaystyle V\_{\text{poc}}(t,x\_{t}) | =K1​e−r​(T1−t)​Φ​(−a2)−xt​e−q​(T2−t)​Φ2​(−a1,b1;−P(2))+K2​e−r​(T2−t)​Φ2​(−a2,b2;−P(2)),\displaystyle=K\_{1}e^{-r(T\_{1}-t)}\Phi(-a\_{2})-x\_{t}e^{-q(T\_{2}-t)}\Phi\_{2}(-a\_{1},b\_{1};-P^{(2)})+K\_{2}e^{-r(T\_{2}-t)}\Phi\_{2}(-a\_{2},b\_{2};-P^{(2)}), |  |
|  | Vpop​(t,xt)\displaystyle V\_{\text{pop}}(t,x\_{t}) | =K1​e−r​(T1−t)​Φ​(−a2)+xt​e−q​(T2−t)​Φ2​(−a1,−b1;P(2))−K2​e−r​(T2−t)​Φ2​(−a2,−b2;P(2)),\displaystyle=K\_{1}e^{-r(T\_{1}-t)}\Phi(-a\_{2})+x\_{t}e^{-q(T\_{2}-t)}\Phi\_{2}(-a\_{1},-b\_{1};P^{(2)})-K\_{2}e^{-r(T\_{2}-t)}\Phi\_{2}(-a\_{2},-b\_{2};P^{(2)}), |  |

and we shall obtain the corresponding option deltas by directly computing the derivatives with respect to xtx\_{t}, respectively. Here, Φ2​(⋅,⋅;P(2))\Phi\_{2}(\cdot,\cdot;P^{(2)}) is the bivariate standard normal CDF with correlation matrix P(2)P^{(2)}, and Φ\Phi is the univariate standard normal CDF. The remaining quantities are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | a1=ln⁡(xt/K1∗)+(r−q+12​σ2)​(T1−t)σ​T1−t,a2=a1−σ​T1−t,\displaystyle a\_{1}=\frac{\ln(x\_{t}/K\_{1}^{\*})+\left(r-q+\frac{1}{2}\sigma^{2}\right)(T\_{1}-t)}{\sigma\sqrt{T\_{1}-t}},\qquad a\_{2}=a\_{1}-\sigma\sqrt{T\_{1}-t}, |  | (5.4) |
|  |  | b1=ln⁡(xt/K2)+(r−q+12​σ2)​(T2−t)σ​T2−t,b2=b1−σ​T2−t,P12(2)=P21(2)=T1−tT2−t.\displaystyle b\_{1}=\frac{\ln\left(x\_{t}/K\_{2}\right)+\left(r-q+\frac{1}{2}\sigma^{2}\right)(T\_{2}-t)}{\sigma\sqrt{T\_{2}-t}},\qquad b\_{2}=b\_{1}-\sigma\sqrt{T\_{2}-t},\qquad P^{(2)}\_{12}=P^{(2)}\_{21}=\sqrt{\frac{T\_{1}-t}{T\_{2}-t}}. |  |

The constant K1∗K\_{1}^{\*} is the critical underlying level at time T1T\_{1} for which the inner option value equals the strike price K1K\_{1} of the outer option. More precisely, K1∗K\_{1}^{\*} solves

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Vc​(T1,K1∗;T2,K2)=K1,for call-on-call or put-on-call,\displaystyle V\_{\text{c}}(T\_{1},K\_{1}^{\*};T\_{2},K\_{2})=K\_{1},\qquad\text{for call-on-call or put-on-call}, |  | (5.5) |
|  |  | Vp​(T1,K1∗;T2,K2)=K1,for call-on-put or put-on-put,\displaystyle V\_{\text{p}}(T\_{1},K\_{1}^{\*};T\_{2},K\_{2})=K\_{1},\qquad\text{for call-on-put or put-on-put}, |  |

where Vc​(t,xt;T2,K2)V\_{\text{c}}(t,x\_{t};T\_{2},K\_{2}) and Vp​(t,xt;T2,K2)V\_{\text{p}}(t,x\_{t};T\_{2},K\_{2}) denote the Black–Scholes call and put prices at time tt with underlying level xx, strike K2K\_{2} and expires at T2T\_{2}. The root-finding problems in ([5.5](https://arxiv.org/html/2601.18634v2#S5.E5 "In 5.1 Plain compound options with 𝑀=2 ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) are solved efficiently via Brent’s method implemented in SciPy.

To implement ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), we follow Case [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") in Section [4](https://arxiv.org/html/2601.18634v2#S4 "4 Applications in derivatives pricing ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"). Under the risk-neutral measure, we set
f1​(t,x,y,z)=f2​(t,x,y,z)=−r​yf\_{1}(t,x,y,z)=f\_{2}(t,x,y,z)=-ry
and choose gjg\_{j} according to the payoff type. For example, for a *call-on-call* option we take

|  |  |  |
| --- | --- | --- |
|  | g1​(x,y)=(y−K1)+,g2​(x)=(x−K2)+.g\_{1}(x,y)=(y-K\_{1})^{+},\qquad g\_{2}(x)=(x-K\_{2})^{+}. |  |

Analogous choices apply to call-on-put, put-on-call, and put-on-put by changing the outer and inner payoffs.

In our experiments, we use the following parameters and test our method over different N∈{10,20,30,40,50}N\in\{10,20,30,40,50\},

|  |  |  |
| --- | --- | --- |
|  | r=0.03,q=0,Σ=0.2,x0=14,K1=1,K2=14,T1=0.2,T2=0.4.r=0.03,\quad q=0,\quad\Sigma=0.2,\quad x\_{0}=14,\quad K\_{1}=1,\quad K\_{2}=14,\quad T\_{1}=0.2,\quad T\_{2}=0.4. |  |

Table [1](https://arxiv.org/html/2601.18634v2#S5.T1 "Table 1 ‣ 5.1 Plain compound options with 𝑀=2 ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") presents the results for all four plain compound options with N=50N=50. We compare the estimated price and delta at t=0t=0 for j=1j=1, denoted by Y1,0πY\_{1,0}^{\pi} and Δ1,0π\Delta\_{1,0}^{\pi}, with the reference values Y1,0Y\_{1,0} and Δ1,0\Delta\_{1,0} obtained from ([5.3](https://arxiv.org/html/2601.18634v2#S5.E3 "In 5.1 Plain compound options with 𝑀=2 ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) and their analytical derivatives. We recall that the BSDE solution (Y,Z)(Y,Z) coincides with the option price and the appropriately scaled option delta via the Feynman–Kac formula, and we use this relation to recover the delta from ZπZ^{\pi}. The corresponding relative mean squared errors are also reported. Overall, the method produces highly accurate estimates for both price and delta across all four contracts, with relative errors ranging from 1.04×10−31.04\times 10^{-3} down to 3.82×10−73.82\times 10^{-7}.

To assess the bound in ([3.17](https://arxiv.org/html/2601.18634v2#S3.E17 "In Theorem 3.4 (Convergence of the Compound BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), we also compute the pathwise error metrics in ([5.2](https://arxiv.org/html/2601.18634v2#S5.E2 "In 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) for different NN. Figure [1](https://arxiv.org/html/2601.18634v2#S5.F1 "Figure 1 ‣ 5.1 Plain compound options with 𝑀=2 ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") shows the results for two representative contracts: call-on-call and put-on-put. All error metrics decrease approximately at first order in the step size h=T/Nh=T/N: increasing NN from 1010 to 5050 reduces the errors by roughly a factor 55. This behaviour is consistent with the convergence estimate for ([2.4](https://arxiv.org/html/2601.18634v2#S2.E4 "In 2.4 The Compound BSDE method ‣ 2 The Compound BSDE Method ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")). Moreover, the empirical total error (red curve) follows the same trend as the theoretical bound (purple curve), supporting the sharpness of ([3.17](https://arxiv.org/html/2601.18634v2#S3.E17 "In Theorem 3.4 (Convergence of the Compound BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) in this setting.

Table 1: Prices and deltas of four types of plain compound options at t=0t=0.

| Option Types | Y1,0πY\_{1,0}^{\pi} | Y1,0Y\_{1,0} | reMSE | Δ1,0π\Delta\_{1,0}^{\pi} | Δ1,0\Delta\_{1,0} | reMSE |
| --- | --- | --- | --- | --- | --- | --- |
| call-on-call | 0.227 | 0.224 | 1.491e-04 | 0.289 | 0.291 | 5.621e-05 |
| call-on-put | 0.118 | 0.120 | 2.209e-04 | -0.163 | -0.168 | 1.044e-03 |
| put-on-call | 0.432 | 0.430 | 3.029e-05 | -0.270 | -0.272 | 2.987e-05 |
| put-on-put | 0.492 | 0.492 | 3.822e-07 | 0.267 | 0.269 | 5.460e-05 |



![Refer to caption](x1.png)


(a) call-on-call

![Refer to caption](x2.png)


(b) put-on-put

Figure 1: Convergence in NN for plain compound options.

### 5.2 MM-fold compound options

We next consider the MM-fold compound call option for M≥2M\geq 2 in the one-dimensional setting. Compared with the plain case with M=2M=2, the MM-fold structure allows for multiple sequential exercise decisions and is therefore closer to many real-world investment settings, where decisions are made gradually rather than in a single step.

Let Vc(M)​(t,xt)V\_{\text{c}}^{(M)}(t,x\_{t}) denote the price of the MM-fold compound call at current state (t,xt)(t,x\_{t}) for 0≤t<T10\leq t<T\_{1}. As reference values, we use the analytical expressions in [[36](https://arxiv.org/html/2601.18634v2#bib.bib36), [37](https://arxiv.org/html/2601.18634v2#bib.bib37)],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vc(M)​(t,xt)=xt​e−q​(TM−t)​ΦM​(a1,…,aM;P(M))−∑j=1MKj​e−r​(Tj−t)​Φj​(b1,…,bj;P(j)),V\_{\text{c}}^{(M)}(t,x\_{t})=x\_{t}e^{-q(T\_{M}-t)}\,\Phi\_{M}\!\left(a\_{1},\dots,a\_{M};P^{(M)}\right)-\sum\_{j=1}^{M}K\_{j}e^{-r(T\_{j}-t)}\,\Phi\_{j}\!\left(b\_{1},\dots,b\_{j};P^{(j)}\right), |  | (5.6) |

and we obtain the delta by computing the derivative. Here Φj​(⋅;P(j))\Phi\_{j}(\cdot;P^{(j)}) denotes the jj-dimensional standard normal CDF with correlation matrix P(j)P^{(j)}. The parameters are given, for j=1,…,Mj=1,\dots,M, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (P(j))i​ℓ=Ti−tTℓ−t,i<ℓ,\left(P^{(j)}\right)\_{i\ell}=\sqrt{\frac{T\_{i}-t}{T\_{\ell}-t}},\qquad i<\ell, |  | (5.7) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | bj=ln⁡(xt/Kj∗)+(r−q−12​σ2)​(Tj−t)σ​Tj−t,aj=bj+σ​Tj−t.b\_{j}=\frac{\ln(x\_{t}/K\_{j}^{\*})+\left(r-q-\frac{1}{2}\sigma^{2}\right)(T\_{j}-t)}{\sigma\sqrt{T\_{j}-t}},\qquad a\_{j}=b\_{j}+\sigma\sqrt{T\_{j}-t}. |  | (5.8) |

To determine the critical levels, we set KM∗=KMK\_{M}^{\*}=K\_{M}, and determine Kj∗K\_{j}^{\*} recursively by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vc(M−j)​(Tj,Kj∗)=Kj,j=1,2,…,M−1,V\_{\text{c}}^{(M-j)}\!\left(T\_{j},K\_{j}^{\*}\right)=K\_{j},\qquad j=1,2,\dots,M-1, |  | (5.9) |

where Vc(M−j)​(Tj,Kj∗)V\_{\text{c}}^{(M-j)}\!\left(T\_{j},K\_{j}^{\*}\right) is the (M−j)(M-j)-fold compound option price at time TjT\_{j}, with an appropriate sequence of exercise times and strike prices, and in the case M−j=1M-j=1 it reduces to the Black-Scholes call price. We remark that although ([5.9](https://arxiv.org/html/2601.18634v2#S5.E9 "In 5.2 𝑀-fold compound options ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")) can be solved numerically similarly to Subsection [5.1](https://arxiv.org/html/2601.18634v2#S5.SS1 "5.1 Plain compound options with 𝑀=2 ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), the computational cost is high if one aims to compute the option prices over the whole time horizon [0,T][0,T] when MM is large.

We solve the MM-fold call problem for M∈{2,3,4,5}M\in\{2,3,4,5\} using

|  |  |  |
| --- | --- | --- |
|  | r=0.03,q=0,Σ=0.2,x0=5,h=0.05,Kj=1,Tj=j,1≤j≤M,r=0.03,\quad q=0,\quad\Sigma=0.2,\quad x\_{0}=5,\quad h=0.05,\quad K\_{j}=1,\quad T\_{j}=j,\quad 1\leq j\leq M, |  |

and we keep the step size hh fixed across different MM by increasing the total number of time steps NN accordingly.

Table [2](https://arxiv.org/html/2601.18634v2#S5.T2 "Table 2 ‣ 5.2 𝑀-fold compound options ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") summarises the results. The accuracy is comparable to that in Subsection [5.1](https://arxiv.org/html/2601.18634v2#S5.SS1 "5.1 Plain compound options with 𝑀=2 ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") for both price and delta. Moreover, at fixed hh, performance remains essentially stable as MM increases, even though the loss contains more compounding terms. This suggests that, in this regime, the number of compounding conditions is not the main limitation of the method.

Table 2: Prices and deltas of MM-fold compound options with different MM at t=0t=0.

| MM | Y1,0πY\_{1,0}^{\pi} | Y1,0Y\_{1,0} | reMSE | Δ1,0π\Delta\_{1,0}^{\pi} | Δ1,0\Delta\_{1,0} | reMSE |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 3.077 | 3.088 | 1.153e-05 | 0.994 | 1.000 | 3.037e-05 |
| 3 | 2.173 | 2.174 | 2.337e-07 | 0.988 | 0.998 | 1.115e-04 |
| 4 | 1.308 | 1.315 | 2.212e-05 | 0.933 | 0.942 | 9.379e-05 |
| 5 | 0.639 | 0.640 | 7.892e-06 | 0.693 | 0.707 | 4.153e-04 |

### 5.3 Bermudan geometric basket put option

We finally consider a Bermudan-style geometric basket put option. This contract is a standard benchmark for high-dimensional Bermudan pricing, since it can be reduced to an equivalent one-dimensional problem, providing an accurate reference value at modest computational cost.

We compute the reference price and delta by applying a binomial tree with a sufficiently large number of time steps to the equivalent one-dimensional formulation. Under the d1d\_{1}-dimensional GBM dynamics ([5.1](https://arxiv.org/html/2601.18634v2#S5.E1 "In 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")), the geometric average

|  |  |  |
| --- | --- | --- |
|  | X^t≔(∏i=1d1Xti)1/d1\hat{X}\_{t}\coloneqq\left(\prod\_{i=1}^{d\_{1}}X\_{t}^{i}\right)^{1/d\_{1}} |  |

is itself a GBM driven by a one-dimensional Brownian motion {Bt}0≤t≤T\{B\_{t}\}\_{0\leq t\leq T} with parameters

|  |  |  |  |
| --- | --- | --- | --- |
|  | x^0=(∏i=1d1x0i)1/d1,r^=r,q^=1d1​∑i=1d1(qi+12​σi2)−12​σ^2,σ^2=1d12​(∑i,j=1d1σi​σj​ρi​j),\hat{x}\_{0}=\left(\prod\_{i=1}^{d\_{1}}x\_{0}^{i}\right)^{1/d\_{1}},\quad\hat{r}=r,\quad\hat{q}=\frac{1}{d\_{1}}\sum\_{i=1}^{d\_{1}}\!\left(q\_{i}+\frac{1}{2}\sigma\_{i}^{2}\right)-\frac{1}{2}\hat{\sigma}^{2},\quad\hat{\sigma}^{2}=\frac{1}{d\_{1}^{2}}\!\left(\sum\_{i,j=1}^{d\_{1}}\sigma\_{i}\sigma\_{j}\rho\_{ij}\right), |  | (5.10) |

and payoff (K−X^t)+(K-\hat{X}\_{t})^{+} at exercise times. Here ρi​j\rho\_{ij} denotes the correlation coefficient between the ii-th and jj-th components of the original d1d\_{1}-dimensional Brownian motion WW.

To run our compound BSDE method under the risk-neutral measure, we again take fj​(t,x,y,z)=−r​yf\_{j}(t,x,y,z)=-ry and specify the compounding conditions to encode Bermudan exercise:

|  |  |  |
| --- | --- | --- |
|  | gj​(x,y)=max⁡(y,(Kj−(∏i=1d1xi)1/d1)+),gM​(x)=(KM−(∏i=1d1xi)1/d1)+.g\_{j}(x,y)=\max\!\left(y,\ \left(K\_{j}-\left(\prod\_{i=1}^{d\_{1}}x^{i}\right)^{1/d\_{1}}\right)^{+}\right),\qquad g\_{M}(x)=\left(K\_{M}-\left(\prod\_{i=1}^{d\_{1}}x^{i}\right)^{1/d\_{1}}\right)^{+}. |  |

We test the method across different dimensions d1d\_{1} and different numbers of time steps NN. Let 𝒯={0.1,0.2,0.3,0.4,0.5}\mathcal{T}=\{0.1,0.2,0.3,0.4,0.5\} be the set of early exercise dates of the option, and we set ρi​j=0\rho\_{ij}=0 for i≠ji\neq j and use the parameters for the test,

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=0.02,q=0,Σ=diag⁡(0.2⋅𝟏d1),X0=49⋅𝟏d1,Kj=50,Tj=0.1⋅j,M=5r=0.02,\quad q=0,\quad\Sigma=\operatorname{diag}(0.2\cdot\mathbf{1}\_{d\_{1}}),\quad X\_{0}=49\cdot\mathbf{1}\_{d\_{1}},\quad K\_{j}=50,\quad T\_{j}=0.1\cdot j,\quad M=5 |  | (5.11) |

Table [3](https://arxiv.org/html/2601.18634v2#S5.T3 "Table 3 ‣ 5.3 Bermudan geometric basket put option ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") reports prices and deltas at t=0t=0 for varying d1d\_{1} with fixed N=100N=100, while Table [4](https://arxiv.org/html/2601.18634v2#S5.T4 "Table 4 ‣ 5.3 Bermudan geometric basket put option ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") reports results for varying NN with fixed d1=20d\_{1}=20. Due to space constraints, we report the range of the d1d\_{1} components of Δ1,0π\Delta\_{1,0}^{\pi}. Table [3](https://arxiv.org/html/2601.18634v2#S5.T3 "Table 3 ‣ 5.3 Bermudan geometric basket put option ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance") indicates that the method achieves good accuracy for both price and delta up to dimension d1=50d\_{1}=50, with relative errors remaining stable as the dimension increases. In Table [4](https://arxiv.org/html/2601.18634v2#S5.T4 "Table 4 ‣ 5.3 Bermudan geometric basket put option ‣ 5 Numerical examples ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance"), the relative errors for both price and delta decrease as NN increases, which is consistent with the convergence behaviour predicted by ([3.17](https://arxiv.org/html/2601.18634v2#S3.E17 "In Theorem 3.4 (Convergence of the Compound BSDE method). ‣ 3 Convergence Analysis ‣ The Compound BSDE Method: A Fully Forward Method for Option Pricing and Optimal Stopping Problems in Finance")).

Table 3: Results for the Bermudan geometric basket put option over different d1d\_{1} at t=0t=0.

| d1d\_{1} | Y1,0πY\_{1,0}^{\pi} | Y1,0Y\_{1,0} | reMSE | Δ1,0π\Delta\_{1,0}^{\pi} | Δ1,0\Delta\_{1,0} | reMSE |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3.101 | 3.071 | 9.699e-05 | [-0.513, -0.513] | −0.510⋅𝟏d1-0.510\cdot\mathbf{1}\_{d\_{1}} | 3.178e-05 |
| 5 | 1.762 | 1.745 | 9.233e-05 | [-0.122, -0.121] | −0.121⋅𝟏d1-0.121\cdot\mathbf{1}\_{d\_{1}} | 5.673e-05 |
| 10 | 1.446 | 1.432 | 9.943e-05 | [-0.067, -0.066] | −0.066⋅𝟏d1-0.066\cdot\mathbf{1}\_{d\_{1}} | 7.713e-05 |
| 20 | 1.236 | 1.223 | 1.077e-04 | [-0.037, -0.036] | −0.036⋅𝟏d1-0.036\cdot\mathbf{1}\_{d\_{1}} | 2.321e-05 |
| 30 | 1.153 | 1.140 | 1.295e-04 | [-0.026, -0.026] | −0.026⋅𝟏d1-0.026\cdot\mathbf{1}\_{d\_{1}} | 3.413e-05 |
| 40 | 1.105 | 1.095 | 8.627e-05 | [-0.020, -0.020] | −0.020⋅𝟏d1-0.020\cdot\mathbf{1}\_{d\_{1}} | 1.479e-05 |
| 50 | 1.076 | 1.067 | 6.196e-05 | [-0.017, -0.017] | −0.017⋅𝟏d1-0.017\cdot\mathbf{1}\_{d\_{1}} | 3.361e-05 |




Table 4: Results for the Bermudan geometric basket put option over different NN at t=0t=0.

| NN | Y1,0πY\_{1,0}^{\pi} | Y1,0Y\_{1,0} | reMSE | Δ1,0π\Delta\_{1,0}^{\pi} | Δ1,0\Delta\_{1,0} | reMSE |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 1.264 | 1.223 | 1.087e-03 | [-0.037, -0.037] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 2.424e-04 |
| 20 | 1.240 | 1.223 | 1.947e-04 | [-0.037, -0.037] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 1.283e-04 |
| 30 | 1.244 | 1.223 | 2.934e-04 | [-0.037, -0.037] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 7.129e-05 |
| 40 | 1.240 | 1.223 | 1.908e-04 | [-0.037, -0.036] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 5.242e-05 |
| 50 | 1.237 | 1.223 | 1.330e-04 | [-0.037, -0.037] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 7.086e-05 |
| 60 | 1.238 | 1.223 | 1.356e-04 | [-0.037, -0.037] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 5.234e-05 |
| 70 | 1.236 | 1.223 | 1.168e-04 | [-0.037, -0.036] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 3.327e-05 |
| 80 | 1.236 | 1.223 | 1.063e-04 | [-0.037, -0.037] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 9.738e-05 |
| 90 | 1.234 | 1.223 | 7.871e-05 | [-0.037, -0.036] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 3.880e-05 |
| 100 | 1.233 | 1.223 | 6.568e-05 | [-0.037, -0.036] | −0.036⋅𝟏20-0.036\cdot\mathbf{1}\_{20} | 2.171e-05 |

## 6 Conclusion

This paper introduced the compound BSDE formulation and the associated Compound BSDE method, a fully forward deep-learning approach for solving a broad class of pricing and optimal stopping problems in finance. The key idea is to represent multi-stage payoffs and exercise features through compounding conditions at compounding times, so that several BSDEs are coupled or compounded through these conditions and can be learned simultaneously. In contrast to many backward-style schemes for early-exercise products, our method keeps the simulation and the learning direction fully forward and enforces all compounding and terminal conditions through a single objective functional. Under standard Lipschitz and time-regularity assumptions, we established well-posedness of the compound BSDE, together with L2L^{2}-regularity properties that are needed for numerical analysis. Building on an *a posteriori* error estimate for the deep BSDE method for a single BSDE, we derived a corresponding *a posteriori* estimate for the compound method, showing that the discretisation and approximation errors are controlled by the step size and by the training loss. The numerical experiments confirm our theoretical results and demonstrate that the method is capable of handling problems with multiple folds as well as early-exercise features in high-dimensional settings. These results suggest that the compound BSDE perspective provides a unified numerical framework for both multi-stage derivatives and discrete-time optimal stopping problems.

Several directions for future work are natural. First, it would be desirable to relax some technical assumptions such as the Lipschitz continuity of the coefficients and to extend the analysis to more general drivers. Second, incorporating variance reduction techniques, control variates, or problem-adapted network architectures may further reduce training time and improve stability in very high dimensions. Third, extending the framework to models with jumps, stochastic volatility, or path-dependent payoffs would broaden the range of applications and further test the flexibility of the compounding approach. Overall, the compound BSDE method offers a flexible and theoretically grounded route to forward deep-learning solvers for complex pricing and optimal stopping problems.

## Acknowledgments

The first author gratefully acknowledges financial support from the China Scholarship Council (CSC) through a PhD scholarship.

## References

* [1]

  Hoi Ying Wong and Jing Zhao.
  An artificial boundary method for american option pricing under the cev model.
  SIAM Journal on Numerical Analysis, 46(4):2183–2209, 2008.
* [2]

  Peter A Forsyth and Kenneth R Vetzal.
  Quadratic convergence for valuing american options using a penalty method.
  SIAM Journal on Scientific Computing, 23(6):2095–2122, 2002.
* [3]

  Christoph Reisinger and Jan Hendrik Witte.
  On the use of policy iteration as an easy way of pricing american options.
  SIAM Journal on Financial Mathematics, 3(1):459–478, 2012.
* [4]

  Fang Fang and Cornelis W Oosterlee.
  A novel pricing method for european options based on fourier-cosine series expansions.
  SIAM Journal on Scientific Computing, 31(2):826–848, 2009.
* [5]

  Fang Fang and Cornelis W Oosterlee.
  Pricing early-exercise and discrete barrier options by fourier-cosine series expansions.
  Numerische Mathematik, 114(1):27–62, 2009.
* [6]

  Francis A Longstaff and Eduardo S Schwartz.
  Valuing american options by simulation: A simple least-squares approach.
  The review of financial studies, 14(1):113–147, 2001.
* [7]

  Bruno Bouchard and Xavier Warin.
  Monte-carlo valuation of american options: facts and new algorithms to improve existing methods.
  In Numerical Methods in Finance: Bordeaux, June 2010, pages 215–255. Springer, 2012.
* [8]

  Nicole El Karoui, Shige Peng, and Marie Claire Quenez.
  Backward stochastic differential equations in finance.
  Mathematical finance, 7(1):1–71, 1997.
* [9]

  E. Pardoux and S. Peng.
  Backward stochastic differential equations and quasilinear parabolic partial differential equations.
  In Boris L. Rozovskii and Richard B. Sowers, editors, Stochastic Partial Differential Equations and Their Applications, pages 200–217, Berlin, Heidelberg, 1992. Springer Berlin Heidelberg.
* [10]

  Bruno Bouchard and Nizar Touzi.
  Discrete-time approximation and monte-carlo simulation of backward stochastic differential equations.
  Stochastic Processes and their applications, 111(2):175–206, 2004.
* [11]

  Bruno Bouchard, Ivar Ekeland, and Nizar Touzi.
  On the malliavin approach to monte carlo approximation of conditional expectations.
  Finance and Stochastics, 8:45–71, 2004.
* [12]

  Emmanuel Gobet, Jean-Philippe Lemor, and Xavier Warin.
  A regression-based Monte Carlo method to solve backward stochastic differential equations.
  The Annals of Applied Probability, 15(3):2172 – 2202, 2005.
* [13]

  Gilles Pagès, Huyên Pham, and Jacques Printems.
  An optimal markovian quantization algorithm for multidimensional stochastic control problems.
  Stochastic Processes and their Applications, 111(2):245–274, 2004.
* [14]

  Christian Bender and Robert Denk.
  A forward scheme for backward sdes.
  Stochastic processes and their applications, 117(12):1793–1812, 2007.
* [15]

  Christian Bender and Jianfeng Zhang.
  Time discretization and Markovian iteration for coupled FBSDEs.
  The Annals of Applied Probability, 18(1):143–177, February 2008.
* [16]

  Jiequn Han, Arnulf Jentzen, and Weinan E.
  Solving high-dimensional partial differential equations using deep learning.
  Proceedings of the National Academy of Sciences, 115(34):8505–8510, 2018.
* [17]

  Jiequn Han and Jihao Long.
  Convergence of the deep BSDE method for coupled FBSDEs.
  Probability, Uncertainty and Quantitative Risk, 5:1–33, 2020.
* [18]

  Christian Beck, Sebastian Becker, Patrick Cheridito, Arnulf Jentzen, and Ariel Neufeld.
  Deep splitting method for parabolic pdes.
  SIAM Journal on Scientific Computing, 43(5):A3135–A3154, 2021.
* [19]

  Côme Huré, Huyên Pham, and Xavier Warin.
  Deep backward schemes for high-dimensional nonlinear PDEs.
  Mathematics of Computation, 89(324):1547–1579, 2020.
* [20]

  Kristoffer Andersson, Adam Andersson, and Cornelis W Oosterlee.
  Convergence of a robust deep FBSDE method for stochastic control.
  SIAM Journal on Scientific Computing, 45(1):A226–A255, 2023.
* [21]

  Shaolin Ji, Shige Peng, Ying Peng, and Xichuan Zhang.
  Solving stochastic optimal control problem via stochastic maximum principle with deep learning method.
  Journal of Scientific Computing, 93(1):30, 2022.
* [22]

  Balint Negyesi, Zhipeng Huang, and Cornelis W Oosterlee.
  Generalized convergence of the deep bsde method: a step towards fully-coupled fbsdes and applications in stochastic control.
  arXiv preprint arXiv:2403.18552, 2024.
* [23]

  Emmanuel Gobet and Jean-Philippe Lemor.
  Numerical simulation of bsdes using empirical regression methods: theory and practice.
  arXiv preprint arXiv:0806.4447, 2008.
* [24]

  Jean-Francois Chassagneux, Romuald Elie, and Idris Kharroubi.
  Discrete-time approximation of multidimensional bsdes with oblique reflections.
  The Annals of Applied Probability, 22(3):971–1007, 2012.
* [25]

  Jean Mémin, Shi-ge Peng, and Ming-yu Xu.
  Convergence of solutions of discrete reflected backward sde’s and simulations.
  Acta Mathematicae Applicatae Sinica, English Series, 24(1):1–18, 2008.
* [26]

  Bruno Bouchard and Jean-François Chassagneux.
  Discrete-time approximation for continuously and discretely reflected bsdes.
  Stochastic Processes and their Applications, 118(12):2269–2293, 2008.
* [27]

  Balint Negyesi and Cornelis W Oosterlee.
  A deep bsde approach for the simultaneous pricing and delta-gamma hedging of large portfolios consisting of high-dimensional multi-asset bermudan options.
  arXiv preprint arXiv:2502.11706, 2025.
* [28]

  Haojie Wang, Han Chen, Agus Sudjianto, Richard Liu, and Qi Shen.
  Deep learning-based bsde solver for libor market model with application to bermudan swaption pricing and hedging.
  arXiv preprint arXiv:1807.06622, 2018.
* [29]

  Chengfan Gao, Siping Gao, Ruimeng Hu, and Zimu Zhu.
  Convergence of the backward deep BSDE method with applications to optimal stopping problems.
  SIAM J. Financial Mathematics, 14(4):1290–1303, 2023.
* [30]

  Jianfeng Zhang.
  Backward stochastic differential equations.
  Springer, 2017.
* [31]

  Jianfeng Zhang.
  A numerical scheme for bsdes.
  The annals of applied probability, 14(1):459–488, 2004.
* [32]

  Kristoffer Andersson, Alessandro Gnoatto, Marco Patacca, and Athena Picarelli.
  A deep solver for bsdes with jumps.
  SIAM Journal on Financial Mathematics, 16(3):875–911, 2025.
* [33]

  Yifan Jiang and Jinfeng Li.
  Convergence of the deep bsde method for fbsdes with non-lipschitz coefficients.
  Probability, Uncertainty and Quantitative Risk, 6(4):391–408, 2021.
* [34]

  Christoph Reisinger, Wolfgang Stockinger, and Yufei Zhang.
  A posteriori error estimates for fully coupled mckean–vlasov forward-backward sdes.
  IMA Journal of Numerical Analysis, 44(4):2323–2369, 2024.
* [35]

  Robert Geske.
  The valuation of compound options.
  Journal of financial economics, 7(1):63–81, 1979.
* [36]

  Liesbeth Thomassen and Martine Van Wouwe.
  A sensitivity analysis for the n-fold compound option.
  2002.
* [37]

  Danny Cassimon, Peter Jan Engelen, Liesbeth Thomassen, and Martine Van Wouwe.
  The valuation of a nda using a 6-fold compound option.
  Research Policy, 33(1):41–51, 2004.