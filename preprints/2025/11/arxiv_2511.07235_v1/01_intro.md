---
authors:
- Erhan Bayraktar
- Qi Feng
- Zecheng Zhang
- Zhaoyu Zhang
doc_id: arxiv:2511.07235v1
family_id: arxiv:2511.07235
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Deep Neural Operator Learning for Probabilistic Models
url_abs: http://arxiv.org/abs/2511.07235v1
url_html: https://arxiv.org/html/2511.07235v1
venue: arXiv q-fin
version: 1
year: 2025
---


Erhan
Bayraktar    Qi Feng
    Zecheng Zhang    Zhaoyu Zhang
Department of
Mathematics, University of Michigan, Ann Arbor, 48109; email: erhan@umich.edu. This author is supported in part the Susan M. Smith Professorship and in part by by the National Science Foundation under grant #DMS-2507940.Department of
Mathematics, Florida State University, Tallahassee, 32306; email: qfeng2@fsu.edu. This author is partially supported by the National Science Foundation under grant #DMS-2420029.Department of Applied Computational Mathematics and Statistics, University of Notre Dame, Notre Dame 46556; zzhang48@nd.edu. This author is partially supported by the Department of Energy DE-SC0025440 Department of
Mathematics, University of California, Los Angeles, CA, 90095;
email: zhaoyu@math.ucla.edu.

###### Abstract

We propose a deep neural-operator framework for a general class of probability models. Under global Lipschitz conditions on the operator over the entire Euclidean space—and for a broad class of probabilistic models—we establish a universal approximation theorem with explicit network-size bounds for the proposed architecture. The underlying stochastic processes are required only to satisfy integrability and general tail-probability conditions. We verify these assumptions for both European and American option-pricing problems within the forward–backward SDE (FBSDE) framework, which in turn covers a broad class of operators arising from parabolic PDEs, with or without free boundaries. Finally, we present a numerical example for a basket of American options, demonstrating that the learned model produces optimal stopping boundaries for new strike prices without retraining.

## 1 Introduction

Operator learning [[13](https://arxiv.org/html/2511.07235v1#bib.bib13), [32](https://arxiv.org/html/2511.07235v1#bib.bib32), [35](https://arxiv.org/html/2511.07235v1#bib.bib35), [31](https://arxiv.org/html/2511.07235v1#bib.bib31), [30](https://arxiv.org/html/2511.07235v1#bib.bib30), [42](https://arxiv.org/html/2511.07235v1#bib.bib42)] uses deep neural networks to approximate mappings between functions or function spaces, enabling efficient solutions to a wide range of computational science problems.
For instance, it can learn the mapping from the initial condition of a partial differential equation (PDE) to its corresponding solution.
Another example is to learn the mapping from fine-scale PDE solutions to coarse-scale ones [[21](https://arxiv.org/html/2511.07235v1#bib.bib21), [29](https://arxiv.org/html/2511.07235v1#bib.bib29)], effectively performing model upscaling.
A key advantage of operator learning is its ability to handle parametric PDEs.
For example, when the PDE initial condition is parameterized by free variables, the operator learning framework can learn the mapping between the space formed by all initial conditions and the space of their corresponding solution space.
Once trained, a deep neural operator (DNO) can instantly predict the solution for any new initial condition within the same function space.
Compared to the standard numerical solvers, operator learning offers much faster and more cost-efficient computations.
This approach has been widely applied to inverse PDE problems, where it is often integrated with standard numerical solvers—either providing an initial approximation refined by numerical methods or serving as a rapid surrogate model to accelerate the overall solution process.

Many popular deep neural operators (DNOs) have been proposed [[13](https://arxiv.org/html/2511.07235v1#bib.bib13), [32](https://arxiv.org/html/2511.07235v1#bib.bib32), [35](https://arxiv.org/html/2511.07235v1#bib.bib35), [31](https://arxiv.org/html/2511.07235v1#bib.bib31), [30](https://arxiv.org/html/2511.07235v1#bib.bib30), [42](https://arxiv.org/html/2511.07235v1#bib.bib42)], and operator learning has been successfully applied to solving practical problems [[36](https://arxiv.org/html/2511.07235v1#bib.bib36), [10](https://arxiv.org/html/2511.07235v1#bib.bib10)], making it an important machine learning framework for large-scale computational applications.
Theoretically, the first operator learning framework was proposed in the seminal works [[13](https://arxiv.org/html/2511.07235v1#bib.bib13), [12](https://arxiv.org/html/2511.07235v1#bib.bib12)], where the authors introduced a shallow universal approximation architecture for nonlinear operators. This foundational theory has directly inspired the design of several modern DNOs, such as DeepONet [[35](https://arxiv.org/html/2511.07235v1#bib.bib35)].
Later, operator learning—viewed as a mapping between infinite-dimensional function spaces—has been analyzed in [[9](https://arxiv.org/html/2511.07235v1#bib.bib9), [33](https://arxiv.org/html/2511.07235v1#bib.bib33)], where the approximation error was quantified with respect to the discretization size of the input function, network complexity, and related parameters.
In [[23](https://arxiv.org/html/2511.07235v1#bib.bib23), [24](https://arxiv.org/html/2511.07235v1#bib.bib24)], the authors generalized the framework of several neural operators, including the Fourier Neural Operator (FNO), and analyzed their universal approximation properties in shallow network settings, though without establishing convergence rates.
In [[26](https://arxiv.org/html/2511.07235v1#bib.bib26), [34](https://arxiv.org/html/2511.07235v1#bib.bib34)], the convergence rate of DeepONet was established for a class of PDE operators.
In [[27](https://arxiv.org/html/2511.07235v1#bib.bib27)], the author studied the lower bound of the convergence rate for PCA-Net, with potential generalizations to other DNOs, while an upper bound result for PCA-Net was given in [[25](https://arxiv.org/html/2511.07235v1#bib.bib25)].
Across the existing literature, establishing rigorous convergence rates for general operators—without restricting to specific PDE formulations—remains one of the central theoretical challenges in operator learning.
One notable contribution in this direction is provided by [[34](https://arxiv.org/html/2511.07235v1#bib.bib34)], which unifies various formulations of neural operators and rigorously establishes convergence rates as the network depth and width increase, for general operators not tied to any specific PDE.
Specifically, the total number of trainable parameters to reach ε\displaystyle\varepsilon error in L∞\displaystyle L^{\infty} norm is scaled as ε−ε−d2\displaystyle\varepsilon^{-\varepsilon^{-d\_{2}}}.

However, all the aforementioned studies address deterministic problems on bounded domains, without involving any stochastic processes or probabilistic models.
To the best of our knowledge, the neural operator approach has only recently been extended to Forward–Backward Stochastic Differential Equations (FBSDEs) [[17](https://arxiv.org/html/2511.07235v1#bib.bib17)], which can be applied to solve European-type option pricing problems, and to Dynamic Stackelberg Games [[1](https://arxiv.org/html/2511.07235v1#bib.bib1)]. In this paper, we develop a neural-operator framework under general Lipschitz conditions for broad classes of stochastic processes satisfying integrability and tail-probability assumptions. In particular, we employ our neural operator to address the American option pricing problem and its associated optimal stopping boundary problem. Recently, American option pricing and optimal stopping problems have been investigated using deep neural networks in [[39](https://arxiv.org/html/2511.07235v1#bib.bib39), [28](https://arxiv.org/html/2511.07235v1#bib.bib28), [22](https://arxiv.org/html/2511.07235v1#bib.bib22), [7](https://arxiv.org/html/2511.07235v1#bib.bib7), [8](https://arxiv.org/html/2511.07235v1#bib.bib8), [37](https://arxiv.org/html/2511.07235v1#bib.bib37), [5](https://arxiv.org/html/2511.07235v1#bib.bib5), [18](https://arxiv.org/html/2511.07235v1#bib.bib18), [6](https://arxiv.org/html/2511.07235v1#bib.bib6), [19](https://arxiv.org/html/2511.07235v1#bib.bib19), [20](https://arxiv.org/html/2511.07235v1#bib.bib20)]. Theoretical results on the continuity property of optimal stopping boundary have been investigated in [[40](https://arxiv.org/html/2511.07235v1#bib.bib40)], while a more general Stefan-type problem for partial differential equations (PDEs) with free boundaries has been studied in [[38](https://arxiv.org/html/2511.07235v1#bib.bib38)]. In these existing works, the methods are typically designed for a fixed terminal payoff function, requiring retraining of the network when the terminal function changes. In contrast, by adopting the operator learning perspective, our trained model can directly generate the optimal stopping boundary for a new terminal payoff function without retraining. Our general neural-operator approximation results encompass both European and American options in the FBSDE setting. Through the Feynman–Kac correspondence (and its optimal-stopping/variational-inequality version for American options), the same guarantees apply to the corresponding PDEs and free-boundary PDEs.

The paper is organized as follows. Section [2](https://arxiv.org/html/2511.07235v1#S2 "2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models") states the standing assumptions on the underlying probabilistic models and the conditions imposed on the operators. Section [3](https://arxiv.org/html/2511.07235v1#S3 "3 Deep Operator Learning Architecture ‣ Deep Neural Operator Learning for Probabilistic Models") presents the deep neural operator architecture, including its construction and size bounds. Section [4](https://arxiv.org/html/2511.07235v1#S4 "4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models") establishes a universal approximation theorem for functions, functionals, and operators under these assumptions. Section [5](https://arxiv.org/html/2511.07235v1#S5 "5 European Option Pricing Operator ‣ Deep Neural Operator Learning for Probabilistic Models") and Section [6](https://arxiv.org/html/2511.07235v1#S6 "6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models") verifies that European- and American-style option pricing problems within the FBSDE framework satisfy the assumptions; by the Feynman–Kac representation (and its variational-inequality form for optimal stopping), the theorem then applies to the associated parabolic PDEs, with or without free boundaries. Section [7](https://arxiv.org/html/2511.07235v1#S7 "7 Algorithm ‣ Deep Neural Operator Learning for Probabilistic Models") provides a numerical example for a basket of American options, demonstrating that the learned model produces optimal stopping boundaries for new strike prices without retraining.

## 2 Assumptions

Let
(Ω,ℱ,{ℱt}t∈[0,T],ℙ)\displaystyle(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{P})
be a filtered probability space satisfying the usual conditions and right-continuity. In this paper, we denote

|  |  |  |
| --- | --- | --- |
|  | X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} |  |

such that X0=x\displaystyle X\_{0}=x, as an ℝd1\displaystyle\mathbb{R}^{d\_{1}}-valued adapted process progressively measurable with respect to {ℱt}t∈[0,T]\displaystyle\{\mathcal{F}\_{t}\}\_{t\in[0,T]}.

###### Definition 2.1.

For x∈ℝd\displaystyle x\in\mathbb{R}^{d}, |x|:=∑i=1dxi2\displaystyle|x|:=\sqrt{\sum\_{i=1}^{d}x\_{i}^{2}}, and ‖x‖∞:=max1≤i≤d⁡|xi|.\displaystyle\|x\|\_{\infty}:=\max\_{1\leq i\leq d}|x\_{i}|.

###### Assumption 1.

For any p>0\displaystyle p>0, there exists a constant Cp>0\displaystyle C\_{p}>0, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Xt|p]≤Cp.\displaystyle\displaystyle\mathbb{E}\left[\sup\_{0\leq t\leq T}|X\_{t}|^{p}\right]\leq C\_{p}. |  | (2.1) |

###### Assumption 2.

There exists a constant CT\displaystyle C\_{T} depending on time T\displaystyle T, and a constant c\displaystyle c such that for any r>0\displaystyle r>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(supt∈[0,T]|Xt−x|≥r)≤exp⁡(−c​rαCT).\displaystyle\displaystyle\mathbb{P}\left(\sup\_{t\in[0,T]}|X\_{t}-x|\geq r\right)\leq\exp\left(-\frac{cr^{\alpha}}{C\_{T}}\right). |  | (2.2) |

###### Definition 2.2.

For any r>0\displaystyle r>0, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωr:={x∈ℝd1:|x|≤r}andΩrC:=ℝd1∖Ωr,\displaystyle\displaystyle\Omega\_{r}:=\{x\in\mathbb{R}^{d\_{1}}:|x|\leq r\}\quad\text{and}\quad\Omega\_{r}^{C}:=\mathbb{R}^{d\_{1}}\setminus\Omega\_{r}, |  | (2.3) |

where , and we define the cube correspondingly as follows

|  |  |  |
| --- | --- | --- |
|  | Qr:=[−r,r]d1={x∈ℝd1:‖x‖∞≤r}.Q\_{r}:=[-r,r]^{d\_{1}}\;=\;\left\{x\in\mathbb{R}^{d\_{1}}:\|x\|\_{\infty}\leq r\right\}. |  |

###### Definition 2.3 (Input space 𝒢\displaystyle\mathcal{G}).

Define the input space as below

|  |  |  |
| --- | --- | --- |
|  | 𝒢:={g:ℝd1→ℝ|g(Xt) is progressively measurable and 𝔼[sup0≤s≤T|g(Xs)|2]<∞}.\mathcal{G}:=\left\{g:\mathbb{R}^{d\_{1}}\to\mathbb{R}\ \Big|\ g(X\_{t})\text{ is progressively measurable and }\mathbb{E}\!\left[\sup\_{0\leq s\leq T}|g(X\_{s})|^{2}\right]<\infty\right\}. |  |

The space 𝒢\displaystyle\mathcal{G} is equipped with the norm

|  |  |  |
| --- | --- | --- |
|  | ‖g‖𝒮2:=(𝔼​[sup0≤s≤T|g​(Xs)|2])1/2.\|g\|\_{\mathcal{S}^{2}}:=\left(\mathbb{E}\!\left[\sup\_{0\leq s\leq T}|g(X\_{s})|^{2}\right]\right)^{1/2}. |  |

###### Definition 2.4 (Output space 𝒰\displaystyle\mathcal{U}).

Define the output space as below

|  |  |  |
| --- | --- | --- |
|  | 𝒰:={u:[0,T]×ℝd2→ℝ|u(t,Xt) is progressively measurable and 𝔼[sup0≤s≤T|u(s,Xs)|2]<∞},\mathcal{U}:=\left\{u:[0,T]\times\mathbb{R}^{d\_{2}}\to\mathbb{R}\ \Big|\ u(t,X\_{t})\text{ is progressively measurable and }\mathbb{E}\!\left[\sup\_{0\leq s\leq T}|u(s,X\_{s})|^{2}\right]<\infty\right\}, |  |

with the norm

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖u‖𝒮2:=(𝔼​[sup0≤s≤T|u​(s,Xs)|2])1/2.\displaystyle\displaystyle\|u\|\_{\mathcal{S}^{2}}:=\left(\mathbb{E}\!\left[\sup\_{0\leq s\leq T}|u(s,X\_{s})|^{2}\right]\right)^{1/2}. |  | (2.4) |

###### Remark 2.5.

We denote X=(Xt)t∈[0,T]\displaystyle X=(X\_{t})\_{t\in[0,T]} for a generic stochastic process. Depending on the context, X∈Domain​(𝒢)\displaystyle X\in\text{Domain}(\mathcal{G}) implies Xt∈ℝd1\displaystyle X\_{t}\in\mathbb{R}^{d\_{1}}, while X∈Domain​(𝒰)\displaystyle X\in\text{Domain}(\mathcal{U}) implies Xt∈ℝd2\displaystyle X\_{t}\in\mathbb{R}^{d\_{2}}.

We impose the following polynomial growth condition and Lipschitz condition.

###### Assumption 3.

For any function g∈𝒢\displaystyle g\in\mathcal{G}, and x∈ℝd1\displaystyle x\in\mathbb{R}^{d\_{1}}, there there exists a constant Cg\displaystyle C\_{g}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)≤Cg​(1+|x|p),forp>0.\displaystyle\displaystyle g(x)\leq C\_{g}(1+|x|^{p}),\quad\text{for}\quad p>0. |  | (2.5) |

###### Assumption 4.

Any function g∈𝒢\displaystyle g\in\mathcal{G} is Lipschitz with a Lipschitz constant no more than Lg>0\displaystyle L\_{g}>0:

|  |  |  |
| --- | --- | --- |
|  | |g​(x1)−g​(x2)|≤Lg​|x1−x2|2|g(x\_{1})-g(x\_{2})|\leq L\_{g}|x\_{1}-x\_{2}|\_{2} |  |

for any x1,x2∈ℝd1\displaystyle x\_{1},x\_{2}\in\mathbb{R}^{d\_{1}}.

###### Assumption 5.

Any function u∈𝒰\displaystyle u\in\mathcal{U} is Lipschitz with a Lipschitz constant no more than Lu>0\displaystyle L\_{u}>0:

|  |  |  |
| --- | --- | --- |
|  | |u​(x1)−u​(x2)|≤Lu​|x1−x2|,|u(x\_{1})-u(x\_{2})|\leq L\_{u}|x\_{1}-x\_{2}|, |  |

for any x1,x2∈ℝd2\displaystyle x\_{1},x\_{2}\in\mathbb{R}^{d\_{2}}.

###### Assumption 6.

Assume the operator

|  |  |  |
| --- | --- | --- |
|  | Γ:𝒢⟶𝒰,g⟼u=Γ​(g),\Gamma:\mathcal{G}\longrightarrow\mathcal{U},\qquad g\longmapsto u=\Gamma(g), |  |

from 𝒢\displaystyle\mathcal{G} to 𝒰\displaystyle\mathcal{U} is Lipschitz if : there exists LΓ\displaystyle L\_{\Gamma} such that for any g1,g2∈𝒢\displaystyle g\_{1},g\_{2}\in\mathcal{G}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Γ​(g1)​(Xt)−Γ​(g2)​(Xt)|2]≤LΓ2​𝔼​[sup0≤t≤T|g1​(Xt)−g2​(Xt)|2],∀g1,g2∈𝒢.\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|\Gamma(g\_{1})(X\_{t})-\Gamma(g\_{2})(X\_{t})|^{2}\right]\leq L\_{\Gamma}^{2}\,\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|g\_{1}(X\_{t})-g\_{2}(X\_{t})|^{2}\right],\ \forall g\_{1},g\_{2}\in\mathcal{G}. |  |

or equivalently,

|  |  |  |
| --- | --- | --- |
|  | ‖Γ​(g1)−Γ​(g2)‖S2≤LΓ​‖g1−g2‖S2.\|\Gamma(g\_{1})-\Gamma(g\_{2})\|\_{S^{2}}\leq L\_{\Gamma}\|g\_{1}-g\_{2}\|\_{S^{2}}. |  |

As mentioned in Remark [2.5](https://arxiv.org/html/2511.07235v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), the process X∈\displaystyle X\in Domain(𝒰\displaystyle\mathcal{U}), i.e. Xt∈ℝd2\displaystyle X\_{t}\in\mathbb{R}^{d\_{2}}.

###### Definition 2.6 (Lipschitz functional).

We say a functional 𝖥:𝒱→ℝ\displaystyle\mathsf{F}:\mathcal{V}\rightarrow\mathbb{R}, where 𝒱\displaystyle\mathcal{V} could either be the input space 𝒢\displaystyle\mathcal{G} or the output space 𝒰\displaystyle\mathcal{U} is Lipschitz with Lipschitz constant L𝖥\displaystyle L\_{\mathsf{F}} if

|  |  |  |
| --- | --- | --- |
|  | |𝖥​(v1)−𝖥​(v2)|≤L𝖥​‖v1−v2‖S2,∀v1,v2∈𝒱.|\mathsf{F}(v\_{1})-\mathsf{F}(v\_{2})|\leq L\_{\mathsf{F}}\|v\_{1}-v\_{2}\|\_{S^{2}},\ \forall v\_{1},v\_{2}\in\mathcal{V}. |  |

###### Lemma 2.7 (Theorem 13.7(ii) of [[41](https://arxiv.org/html/2511.07235v1#bib.bib41)]).

Let {Ωk}k=1M\displaystyle\{\Omega\_{k}\}\_{k=1}^{M} be an open cover of a compact smooth manifold ℳ\displaystyle\mathcal{M} . There exists a C∞\displaystyle C^{\infty} partition of unity {ωk}k=1M\displaystyle\{\omega\_{k}\}\_{k=1}^{M} that subordinates to {Ωk}k=1M\displaystyle\{\Omega\_{k}\}\_{k=1}^{M} such that s​u​p​p​o​r​t​(ωk)⊂Ωk\displaystyle support(\omega\_{k})\subset\Omega\_{k} for any k\displaystyle k.

## 3 Deep Operator Learning Architecture

Operator learning aims to approximate mappings between infinite-dimensional function spaces, distinguishing itself from traditional neural networks, which approximate functions directly. Specifically, given a nonlinear operator Γ\displaystyle\Gamma that maps an input function g\displaystyle g to an output function Γ​(g)\displaystyle\Gamma(g), the objective is to learn Γ\displaystyle\Gamma using a neural network architecture.
In this work, the nonlinear operator Γ\displaystyle\Gamma represents a pricing operator, and the goal is to approximate it via a neural network-based approach.
We will use the notations used in [[33](https://arxiv.org/html/2511.07235v1#bib.bib33)], we will define the fully connected ReLU neural network.
we define a feedforward ReLU network q:ℝd1→ℝ\displaystyle{q}:\mathbb{R}^{d\_{1}}\rightarrow\mathbb{R} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(𝐱)=WL⋅ReLU​(WL−1​⋯​ReLU​(W1​x+b1)+⋯+bL−1)+bL,\displaystyle\displaystyle q(\mathbf{x})=W\_{L}\cdot\text{ReLU}\left(W\_{L-1}\cdots\text{ReLU}(W\_{1}x+b\_{1})+\cdots+b\_{L-1}\right)+b\_{L}, |  | (3.1) |

where Wl\displaystyle W\_{l}’s are weight matrices, bl\displaystyle b\_{l}’s are bias vectors, ReLU​(a)=max⁡{a,0}\displaystyle\text{ReLU}(a)=\max\{a,0\} is the rectified linear unit activation (ReLU) applied element-wise, and Ω\displaystyle\Omega is the domain.
We define the network class ℱNN:ℝd1→ℝd2:\displaystyle\mathcal{F}\_{\rm NN}:\mathbb{R}^{d\_{1}}\rightarrow\mathbb{R}^{d\_{2}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱNN(d1,d2,ℒ,𝔭,K,κ,R)={\displaystyle\displaystyle\mathcal{F}\_{\rm NN}(d\_{1},d\_{2},\mathcal{L},\mathfrak{p},K,\kappa,R)=\{ | [q1,q2,…,qd2]⊺∈ℝd2: for each ​k=1,…,d2,\displaystyle\displaystyle[q\_{1},q\_{2},...,q\_{d\_{2}}]^{\intercal}\in\mathbb{R}^{d\_{2}}:\mbox{ for each }k=1,...,d\_{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | qk:ℝd1→ℝ​ is in the form of ([3.1](https://arxiv.org/html/2511.07235v1#S3.E1 "In 3 Deep Operator Learning Architecture ‣ Deep Neural Operator Learning for Probabilistic Models")) with ​ℒ​ layers, width bounded by ​𝔭,\displaystyle\displaystyle q\_{k}:\mathbb{R}^{d\_{1}}\rightarrow\mathbb{R}\mbox{ is in the form of (\ref{eqn\_relu\_net}) with }\mathcal{L}\mbox{ layers, width bounded by }\mathfrak{p}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∥qk∥L∞≤R,∥Wl∥∞,∞≤κ,∥bl∥∞≤κ,∑l=1L∥Wl∥0+∥bl∥0≤K,∀l},\displaystyle\displaystyle\|q\_{k}\|\_{L^{\infty}}\leq R,\ \|W\_{l}\|\_{\infty,\infty}\leq\kappa,\ \|b\_{l}\|\_{\infty}\leq\kappa,\ \sum\_{l=1}^{L}\|W\_{l}\|\_{0}+\|b\_{l}\|\_{0}\leq K,\ \forall l\}, |  | (3.2) |

where
‖q‖L∞​(Ω)=sup𝐱∈Ω|q​(𝐱)|,‖Wl‖∞,∞=maxi,j⁡|Wi,j|,‖b‖∞=maxi⁡|bi|\displaystyle\|q\|\_{L^{\infty}(\Omega)}=\sup\limits\_{\mathbf{x}\in\Omega}|q(\mathbf{x})|,\ \|W\_{l}\|\_{\infty,\infty}=\max\limits\_{i,j}|W\_{i,j}|,\ \|b\|\_{\infty}=\max\limits\_{i}|b\_{i}|,
and ∥⋅∥0\displaystyle\|\cdot\|\_{0} denotes the number of nonzero elements of its argument.
The network class above has input dimension d1\displaystyle d\_{1}, output dimension d2\displaystyle d\_{2}, ℒ\displaystyle\mathcal{L} layers, width 𝔭\displaystyle\mathfrak{p}, and the number of nonzero parameters no larger than K\displaystyle K.
All parameters are bounded by κ\displaystyle\kappa, and each element in the output is bounded by R\displaystyle R.

The objective of operator learning is to construct an operator network Γp​[⋅;θ]\displaystyle\Gamma\_{p}[\cdot;\theta] that approximates Γ\displaystyle\Gamma.
One approximation structure [[13](https://arxiv.org/html/2511.07235v1#bib.bib13), [35](https://arxiv.org/html/2511.07235v1#bib.bib35)] which is widely adopted in designing DNOs is the following.
To better demonstrate the idea of the approximation, we denote y\displaystyle y as the independent variable of the output function of the operator Γ\displaystyle\Gamma, and denote Γ​(g;θ)​(y)\displaystyle\Gamma(g;\theta)(y) as the neural operator approximation to Γ\displaystyle\Gamma, we then have the approximation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(g)​(y)≈Γ​(g;θ)​(y):=∑k=1N1a~k​(𝒈;θ^)​q~k​(y;θ~)\Gamma(g)(y)\approx\Gamma(g;\theta)(y):=\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g};\widehat{\theta})\widetilde{q}\_{k}(y;\widetilde{\theta}) |  | (3.3) |

where g\displaystyle g is the input function with a discretization denoted as 𝒈\displaystyle\bm{g}, Γ​(g)\displaystyle\Gamma(g) is the output function depends on y\displaystyle y, and θ={θ^,θ~}\displaystyle\theta=\{\widehat{\theta},\widetilde{\theta}\} represents the set of trainable parameters of the operator network consisted of a~k\displaystyle\widetilde{a}\_{k} and q~k\displaystyle\widetilde{q}\_{k}.
The framework was first proposed in [[13](https://arxiv.org/html/2511.07235v1#bib.bib13), [12](https://arxiv.org/html/2511.07235v1#bib.bib12)] as a two-layer universal approximation scheme for nonlinear operators.
It was later extended computationally to deep neural network architectures in [[35](https://arxiv.org/html/2511.07235v1#bib.bib35)], and was finally rigorously analyzed in terms of error convergence and generalization in [[34](https://arxiv.org/html/2511.07235v1#bib.bib34)].
Following the terminology widely adopted in recent literature, we use the notation introduced in [[35](https://arxiv.org/html/2511.07235v1#bib.bib35)] to name the substructure of the network.
Specifically, the architecture consists of two components:

* •

  Branch network: a~​(𝐠;θ^)=(a~1​(𝐠;θ^1),…,a~N1​(𝐠;θ^N1))T\displaystyle\widetilde{a}(\mathbf{g};\widehat{\theta})=(\widetilde{a}\_{1}(\mathbf{g};\widehat{\theta}\_{1}),\dots,\widetilde{a}\_{N\_{1}}(\mathbf{g};\widehat{\theta}\_{N\_{1}}))^{T} encode the input function g\displaystyle g and the operator Γ\displaystyle\Gamma.
  Each component a~k:ℝN2→ℝ\displaystyle\widetilde{a}\_{k}:\mathbb{R}^{{N\_{2}}}\rightarrow\mathbb{R} is implemented as a sum of fully connected neural networks.
  Specifically, a~k=∑n=1Han​b~n\displaystyle\widetilde{a}\_{k}=\sum\_{n=1}^{H}a\_{n}\widetilde{b}\_{n}, where N2\displaystyle N\_{2} is the size of the discretization 𝐠\displaystyle\mathbf{g} , H\displaystyle H is the number of basis represented as a network b~n\displaystyle\widetilde{b}\_{n} in a neural network class ℱ2=ℱNN​(N2,1,ℒ2,𝔭2,K2,κ2)\displaystyle\mathcal{F}\_{2}=\mathcal{F}\_{\rm NN}(N\_{2},1,\mathcal{L}\_{2},\mathfrak{p}\_{2},K\_{2},\kappa\_{2}), an\displaystyle a\_{n} are constants.
  The size of the entire network β\displaystyle\beta (containing all b~k\displaystyle\widetilde{b}\_{k}) is specified in Theorem [4.5](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.3 Operator Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models").
* •

  Trunk network: q~​(y;θ~)=(q~1,…,q~N1)\displaystyle\widetilde{q}(y;\widetilde{\theta})=(\widetilde{q}\_{1},...,\widetilde{q}\_{N\_{1}}).
  Here each q~k:ℝd2→ℝ\displaystyle\widetilde{q}\_{k}:\mathbb{R}^{d\_{2}}\rightarrow\mathbb{R} is a network in class ℱ1=ℱNN​(d2,1,ℒ1,𝔭1,K1,κ1)\displaystyle\mathcal{F}\_{1}=\mathcal{F}\_{\rm NN}(d\_{2},1,\mathcal{L}\_{1},\mathfrak{p}\_{1},K\_{1},\kappa\_{1}) with size to be specified in Theorem [4.5](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.3 Operator Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models").

The following lemma from [[44](https://arxiv.org/html/2511.07235v1#bib.bib44)][Proposition 3] shows that a function of the product can be approximated by a network with arbitrary accuracy.

###### Lemma 3.1.

Given M>0\displaystyle M>0 and ε>0\displaystyle\varepsilon>0, there is a ReLU network ×~:ℝ2→ℝ\displaystyle\widetilde{\times}:\mathbb{R}^{2}\rightarrow\mathbb{R} in ℱNN​(2,1,ℒ,𝔭,K,κ,R)\displaystyle\mathcal{F}\_{\rm NN}(2,1,\mathcal{L},\mathfrak{p},K,\kappa,R) such that for any |x|≤M,|y|≤M\displaystyle|x|\leq M,|y|\leq M, we have

|  |  |  |
| --- | --- | --- |
|  | |×~​(x,y)−x​y|<ε.|\widetilde{\times}(x,y)-xy|<\varepsilon. |  |

The network architecture has

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=O​(log⁡ε−1),𝔭=6,K=O​(log⁡ε−1),κ=O​(ε−1),R=M2.\displaystyle\displaystyle\mathcal{L}=O(\log\varepsilon^{-1}),\ \mathfrak{p}=6,\ K=O(\log\varepsilon^{-1}),\ \kappa=O(\varepsilon^{-1}),\ R=M^{2}. |  | (3.4) |

The constant hidden in O\displaystyle O depends on M\displaystyle M.

## 4 Neural scaling of operator learning

### 4.1 Function Approximation

We will first prove the function approximation and establish the convergence rate.
The results will be used in proving the operator approximation Theorem [4.5](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.3 Operator Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models").

###### Theorem 4.1.

Assume Assumptions [1](https://arxiv.org/html/2511.07235v1#Thmassumption1 "Assumption 1. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [4](https://arxiv.org/html/2511.07235v1#Thmassumption4 "Assumption 4. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models") hold.
For any ε>0\displaystyle\varepsilon>0, set r=⌈−2​CTc​log⁡ε4​C0⌉1α\displaystyle r=\left\lceil-\frac{2C\_{T}}{c}\log\frac{\varepsilon}{4C\_{0}}\right\rceil^{\frac{1}{\alpha}} in Assumption [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"),
and set N=C​d1​ε−1/2​(log⁡(ε−1))1α\displaystyle N=C\sqrt{d\_{1}}\varepsilon^{-1/2}(\log(\varepsilon^{-1}))^{\frac{1}{\alpha}}, with constant C\displaystyle C depends on CT,C0,c,Lg\displaystyle C\_{T},C\_{0},c,L\_{g}.
Let {𝐜k}k=1Nd1\displaystyle\{\mathbf{c}\_{k}\}\_{k=1}^{N^{d\_{1}}} be a uniform grid on Qr\displaystyle Q\_{r} (covering Ωr\displaystyle\Omega\_{r}) with spacing 2​r/N\displaystyle 2r/N along each dimension.
There exists a network architecture ℱNN​(d1,1,ℒ,𝔭,K,κ,R)\displaystyle\mathcal{F}\_{\rm NN}(d\_{1},1,\mathcal{L},\mathfrak{p},K,\kappa,R) and networks {q~k}k=1Nd1\displaystyle\{\widetilde{q}\_{k}\}\_{k=1}^{N^{d\_{1}}} with q~k∈ℱNN​(d1,1,ℒ,𝔭,K,κ,R)\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{\rm NN}(d\_{1},1,\mathcal{L},\mathfrak{p},K,\kappa,R) for k=1,…,Nd1\displaystyle k=1,...,N^{d\_{1}}, such that for any g∈𝒢\displaystyle g\in\mathcal{G}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|g​(Xt)−∑k=1Nd1g​(𝐜k)​q~k​(Xt)|2]≤ε.\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|g(X\_{t})-\sum\_{k=1}^{N^{d\_{1}}}g(\mathbf{c}\_{k})\widetilde{q}\_{k}(X\_{t})\Big|^{2}\Big]\leq\varepsilon. |  | (4.1) |

Such a network architecture has

|  |  |  |
| --- | --- | --- |
|  | ℒ=O​(d12​log⁡d1+d12+d12​log⁡(ε−1)+d12+d1​pα​log⁡log⁡(ε−1)),𝔭=O​(1),\displaystyle\displaystyle{\color[rgb]{0,0,0}\mathcal{L}=O\left(d\_{1}^{2}\log d\_{1}+\frac{d\_{1}^{2}+d\_{1}}{2}\log(\varepsilon^{-1})+\frac{d\_{1}^{2}+d\_{1}p}{\alpha}\log\log(\varepsilon^{-1})\right)},\mathfrak{p}=O(1), |  |
|  |  |  |
| --- | --- | --- |
|  | K=O​(d12​log⁡d1+d12+d12​log⁡(ε−1)+d12+d1​pα​log⁡log⁡(ε−1)),\displaystyle\displaystyle K=O\left(d\_{1}^{2}\log d\_{1}+\frac{d\_{1}^{2}+d\_{1}}{2}\log(\varepsilon^{-1})+\frac{d\_{1}^{2}+d\_{1}p}{\alpha}\log\log(\varepsilon^{-1})\right), |  |
|  |  |  |
| --- | --- | --- |
|  | κ=O​(d1−d12​ε−d1+12​(log⁡(ε−1))d1+pα),R=1.\displaystyle\displaystyle{\color[rgb]{0,0,0}\kappa=O(d\_{1}^{-\frac{d\_{1}}{2}}\varepsilon^{-\frac{d\_{1}+1}{2}}(\log(\varepsilon^{-1}))^{\frac{d\_{1}+p}{\alpha}})},R=1. |  |

Here, the network order is determined by the constants CT,C0,c,α,Lg\displaystyle C\_{T},C\_{0},c,\alpha,L\_{g} specified in Assumptions [1](https://arxiv.org/html/2511.07235v1#Thmassumption1 "Assumption 1. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), and [4](https://arxiv.org/html/2511.07235v1#Thmassumption4 "Assumption 4. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), which concern the function g\displaystyle g and process {Xt}0≤t≤T\displaystyle\{X\_{t}\}\_{0\leq t\leq T}. In particular, we denote C0\displaystyle C\_{0} as the upper bound of 𝔼​[sup0≤t≤T|1+|Xt|p|4]1/2\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|1+|X\_{t}|^{p}\Big|^{4}\Big]^{1/2}.

###### Proof.

Recall Ωr\displaystyle\Omega\_{r} and ΩrC\displaystyle\Omega\_{r}^{C} from the Definition [2.2](https://arxiv.org/html/2511.07235v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"). Without loss of generality, we assume that the origin 0∈Ωr\displaystyle 0\in\Omega\_{r}. We then decompose g​(Xt)=g​(Xt)​𝟏Ωr+g​(Xt)​𝟏ΩrC\displaystyle g(X\_{t})=g(X\_{t})\mathbf{1}\_{\Omega\_{r}}+g(X\_{t})\mathbf{1}\_{\Omega\_{r}^{C}}
For the compact domain Ωr⊂Qr\displaystyle\Omega\_{r}\subset Q\_{r}, we apply a partition to Qr\displaystyle Q\_{r} covered by Nd1\displaystyle N^{d\_{1}} subcubes for some N\displaystyle N to be specified later. We first approximate g​(Xt)​𝟏Ωr\displaystyle g(X\_{t})\mathbf{1}\_{\Omega\_{r}} on each cube by a constant function and then assemble them together to get an approximation of {g​(Xt)}0≤t≤T\displaystyle\{g(X\_{t})\}\_{0\leq t\leq T} on Ωr\displaystyle\Omega\_{r}. Denote the centers of the subcubes by {𝐜k}k=1Nd1\displaystyle\{\mathbf{c}\_{k}\}\_{k=1}^{N^{d\_{1}}} with 𝐜k=[ck,1,ck,2,…,ck,d1]⊺\displaystyle\mathbf{c}\_{k}=[c\_{k,1},c\_{k,2},...,c\_{k,d\_{1}}]^{\intercal}.
Let {𝐜k}k=1Nd1\displaystyle\{\mathbf{c}\_{k}\}\_{k=1}^{N^{d\_{1}}} be a uniform grid on Qr\displaystyle Q\_{r} (covering Ωr\displaystyle\Omega\_{r}), so that each 𝐜k∈{−r,−r+2​rN−1,…,r}d1\displaystyle\mathbf{c}\_{k}\in\left\{-r,-r+\frac{2r}{N-1},...,r\right\}^{d\_{1}} for each k\displaystyle k.
Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(a)={1,|a|<1,0,|a|>2,2−|a|,1≤|a|≤2,\displaystyle\displaystyle\psi(a)=\begin{cases}1,|a|<1,\\ 0,|a|>2,\\ 2-|a|,1\leq|a|\leq 2,\end{cases} |  | (4.2) |

with a∈ℝ\displaystyle a\in\mathbb{R}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ𝐜k​(𝐱)=∏j=1d1ψ​(3​(N−1)2​r​(xj−ck,j)),𝐱∈Qr.\displaystyle\displaystyle\phi\_{\mathbf{c}\_{k}}(\mathbf{x})=\prod\_{j=1}^{d\_{1}}\psi\left(\frac{3(N-1)}{2r}(x\_{j}-c\_{k,j})\right),\quad\mathbf{x}\in Q\_{r}. |  | (4.3) |

In this definition, we have supp​(ϕ𝐜k)={𝐱:‖𝐱−𝐜k‖∞≤4​r3​(N−1)}⊂{𝐱:‖𝐱−𝐜k‖∞≤2​r(N−1)}\displaystyle\mathrm{supp\,}(\phi\_{\mathbf{c}\_{k}})=\left\{\mathbf{x}:\|\mathbf{x}-\mathbf{c}\_{k}\|\_{\infty}\leq\frac{4r}{3(N-1)}\right\}\subset\left\{\mathbf{x}:\|\mathbf{x}-\mathbf{c}\_{k}\|\_{\infty}\leq\frac{2r}{(N-1)}\right\} and for the constraint space Ωr\displaystyle\Omega\_{r}, we have

|  |  |  |
| --- | --- | --- |
|  | ‖ϕ𝐜k‖L∞​(Qr)=1,∑k=1Nd1ϕ𝐜k=1.\|\phi\_{\mathbf{c}\_{k}}\|\_{L^{\infty}(Q\_{r})}=1,\quad\sum\_{k=1}^{N^{d\_{1}}}\phi\_{\mathbf{c}\_{k}}=1. |  |

For any g​(Xt)\displaystyle g(X\_{t}) with Xt∈Ωr\displaystyle X\_{t}\in\Omega\_{r}, we construct a piecewise constant approximation as below,

|  |  |  |
| --- | --- | --- |
|  | g¯​(Xt)=∑k=1Nd1g​(𝐜k)​ϕ𝐜k​(Xt),Xt∈Ωr.\bar{g}(X\_{t})=\sum\_{k=1}^{N^{d\_{1}}}g(\mathbf{c}\_{k})\phi\_{\mathbf{c}\_{k}}(X\_{t}),\quad X\_{t}\in\Omega\_{r}. |  |

Based on the decomposition of the domain ℝd1=Ωr∪ΩrC\displaystyle\mathbb{R}^{d\_{1}}=\Omega\_{r}\cup\Omega\_{r}^{C}, for any T≥0\displaystyle T\geq 0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sup0≤t≤T|g​(Xt)−g¯​(Xt)|2]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|g(X\_{t})-\bar{g}(X\_{t})\Big|^{2}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[sup0≤t≤T|g​(Xt)|2​𝟏ΩrC​(Xt)]⏟ℐ1+𝔼​[sup0≤t≤T|g​(Xt)−g¯​(Xt)|2​𝟏Ωr​(Xt)]⏟ℐ2.\displaystyle\displaystyle\underbrace{\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|g(X\_{t})\Big|^{2}\mathbf{1}\_{\Omega\_{r}^{C}}(X\_{t})\Big]}\_{\mathcal{I}\_{1}}+\underbrace{\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|g(X\_{t})-\bar{g}(X\_{t})\Big|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big]}\_{\mathcal{I}\_{2}}. |  |

For the first term ℐ1\displaystyle\mathcal{I}\_{1}, applying the polynomial growth Assumption [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models") for function g\displaystyle g and uniform bound Assumption [1](https://arxiv.org/html/2511.07235v1#Thmassumption1 "Assumption 1. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), and Cauchy-Schwartz inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ1\displaystyle\displaystyle\mathcal{I}\_{1} | =𝔼​[sup0≤t≤T|g​(Xt)|2​𝟏ΩrC​(Xt)]\displaystyle\displaystyle=\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|g(X\_{t})\Big|^{2}\mathbf{1}\_{\Omega\_{r}^{C}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[sup0≤t≤T|g​(Xt)|4]1/2​𝔼​[sup0≤t≤T(𝟏ΩrC​(Xt))2]1/2\displaystyle\displaystyle\leq\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|g(X\_{t})\Big|^{4}\Big]^{1/2}\mathbb{E}\Big[\sup\_{0\leq t\leq T}(\mathbf{1}\_{\Omega\_{r}^{C}}(X\_{t}))^{2}\Big]^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[sup0≤t≤T|1+‖Xt‖p|4]1/2​(ℙ​(sup0≤t≤T|Xt|≥r))1/2\displaystyle\displaystyle\leq\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|1+\|X\_{t}\|^{p}\Big|^{4}\Big]^{1/2}\Big(\mathbb{P}\Big(\sup\_{0\leq t\leq T}|X\_{t}|\geq r\Big)\Big)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C0​(ℙ​(sup0≤t≤T|Xt|≥r))1/2.\displaystyle\displaystyle\leq C\_{0}\Big(\mathbb{P}\Big(\sup\_{0\leq t\leq T}|X\_{t}|\geq r\Big)\Big)^{1/2}. |  |

According to the tail bound Assumption [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), by taking the initial point X0\displaystyle X\_{0} as the center of the domain, and selecting
 r=⌈−2​CTc​log⁡ε4​C0⌉1α\displaystyle r=\left\lceil-\frac{2C\_{T}}{c}\log\frac{\varepsilon}{4C\_{0}}\right\rceil^{\frac{1}{\alpha}},
we get the following bound

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℐ1\displaystyle\displaystyle\mathcal{I}\_{1} | ≤C0​e−c​rα2​CT≤ε4,\displaystyle\displaystyle\leq C\_{0}e^{-\frac{cr^{\alpha}}{2C\_{T}}}\leq\frac{\varepsilon}{4}, |  | (4.4) |

where C0\displaystyle C\_{0} denotes the upper bound of 𝔼​[sup0≤t≤T|1+‖Xt‖p|4]1/2\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|1+\|X\_{t}\|^{p}\Big|^{4}\Big]^{1/2}, which follows from Assumption [1](https://arxiv.org/html/2511.07235v1#Thmassumption1 "Assumption 1. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"). 
For the second term ℐ2\displaystyle\mathcal{I}\_{2}, by applying the partition of unity property ∑k=1Nd1ϕ𝐜k=1\displaystyle\sum\_{k=1}^{N^{d\_{1}}}\phi\_{\mathbf{c}\_{k}}=1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ2=\displaystyle\displaystyle\mathcal{I}\_{2}= | 𝔼​[sup0≤t≤T|∑k=1Nd1[g​(Xt)−g​(𝐜k)]​ϕ𝐜k​(Xt)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|\sum\_{k=1}^{N^{d\_{1}}}[g(X\_{t})-g(\mathbf{c}\_{k})]\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤T(∑k=1Nd1|g​(Xt)−g​(𝐜k)|​|ϕ𝐜k​(Xt)|)2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big(\sum\_{k=1}^{N^{d\_{1}}}|g(X\_{t})-g(\mathbf{c}\_{k})||\phi\_{\mathbf{c}\_{k}}(X\_{t})|\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[sup0≤t≤T(∑k:‖𝐜k−Xt‖∞≤2​r(N−1)|g​(Xt)−g​(𝐜k)|​ϕ𝐜k​(Xt))2​𝟏Ωr​(Xt)],\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big(\sum\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|g(X\_{t})-g(\mathbf{c}\_{k})|\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤T(maxk:‖𝐜k−Xt‖∞≤2​r(N−1)⁡|g​(Xt)−g​(𝐜k)|​(∑k:‖𝐜k−Xt‖∞≤2​r(N−1)ϕ𝐜k​(Xt)))2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big(\max\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|g(X\_{t})-g(\mathbf{c}\_{k})|\Big(\sum\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big)\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤Tmaxk:‖𝐜k−Xt‖∞≤2​r(N−1)⁡|g​(Xt)−g​(𝐜k)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\max\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|g(X\_{t})-g(\mathbf{c}\_{k})|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | (2​r​Lg)2​d1(N−1)2,\displaystyle\displaystyle\frac{(2rL\_{g})^{2}d\_{1}}{(N-1)^{2}}, |  | (4.5) |

where we use the Lipschitz assumption of g\displaystyle g in the last inequality and the uniform bound given {Xt}0≤t≤T∈Ωr\displaystyle\{X\_{t}\}\_{0\leq t\leq T}\in\Omega\_{r}.
Let N=⌈4​d1​log1/α⁡(ε−1)​Lgε⌉+1\displaystyle N=\left\lceil\frac{4\sqrt{d\_{1}}\log^{1/\alpha}(\varepsilon^{-1})L\_{g}}{\sqrt{\varepsilon}}\right\rceil+1, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ2≤ε/4.\displaystyle\displaystyle\mathcal{I}\_{2}\leq\varepsilon/4. |  | (4.6) |

Combining the estimates ([4.4](https://arxiv.org/html/2511.07235v1#S4.E4 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([4.5](https://arxiv.org/html/2511.07235v1#S4.E5 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|g​(Xt)−g¯​(Xt)|2]≤ε2.\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|g(X\_{t})-\bar{g}(X\_{t})\Big|^{2}\Big]\leq\frac{\varepsilon}{2}. |  | (4.7) |

We then show that ϕ𝐜k\displaystyle\phi\_{\mathbf{c}\_{k}} can be approximated by a network with arbitrary accuracy on the compact domain Ωr\displaystyle\Omega\_{r} with a fixed parameter r\displaystyle r. Notice that for a compact domain Ωr\displaystyle\Omega\_{r}, this type of approximation has already been established in [[34](https://arxiv.org/html/2511.07235v1#bib.bib34)]. Since a different norm is employed here, we provide the proof for completeness.
Note that ϕ𝐜k\displaystyle\phi\_{\mathbf{c}\_{k}} is the product of d1\displaystyle d\_{1} functions, each of which is piecewise linear and can be realized by the constant depth ReLU networks.
Let ×~\displaystyle\widetilde{\times} be the network defined in Lemma [3.1](https://arxiv.org/html/2511.07235v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3 Deep Operator Learning Architecture ‣ Deep Neural Operator Learning for Probabilistic Models") with accuracy δ>0\displaystyle\delta>0.
For any 𝐱∈Qr\displaystyle\mathbf{x}\in Q\_{r}, we approximate ϕ𝐜k\displaystyle\phi\_{\mathbf{c}\_{k}} with q~k\displaystyle\widetilde{q}\_{k} defined as follows,

|  |  |  |
| --- | --- | --- |
|  | q~k​(𝐱)=×~​(ψ​(3​(N−1)2​r​(x1−ck,1)),×~​(ψ​(3​(N−1)2​r​(x2−ck,2)),⋯)).\displaystyle\displaystyle\widetilde{q}\_{k}(\mathbf{x})=\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{1}-c\_{k,1})\right),\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{2}-c\_{k,2})\right),\cdot\cdot\cdot\right)\right). |  |

For each k\displaystyle k, define q~k∈ℱNN​(d1,1,ℒ,𝔭,K,κ,R)\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{\rm NN}(d\_{1},1,\mathcal{L},\mathfrak{p},K,\kappa,R) with sizes to be specified later.
For any Xt∈Ωr\displaystyle X\_{t}\in\Omega\_{r} which is equivalent to considering Xt⋅𝟏Ωr\displaystyle X\_{t}\cdot\mathbf{1}\_{\Omega\_{r}}, we may simply take 𝐱∈Ωr\displaystyle\mathbf{x}\in\Omega\_{r}. That is, by viewing 𝐱\displaystyle\mathbf{x} as an arbitrary point in the domain Ωr\displaystyle\Omega\_{r}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |q~k​(𝐱)−ϕ𝐜k​(𝐱)|\displaystyle\displaystyle|\widetilde{q}\_{k}(\mathbf{x})-\phi\_{\mathbf{c}\_{k}}(\mathbf{x})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | |×~​(ψ​(3​(N−1)2​r​(x1−ck,1)),×~​(ψ​(3​(N−1)2​r​(x2−ck,2)),⋯))−ϕ𝐜k​(𝐱)|\displaystyle\displaystyle\left|\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{1}-c\_{k,1})\right),\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{2}-c\_{k,2})\right),\cdot\cdot\cdot\right)\right)-\phi\_{\mathbf{c}\_{k}}(\mathbf{x})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | |×~(ψ(3​(N−1)2​r(x1−ck,1)),×~(ψ(3​(N−1)2​r(x2−ck,2)),⋯))\displaystyle\displaystyle\bigg|\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{1}-c\_{k,1})\right),\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{2}-c\_{k,2})\right),\cdot\cdot\cdot\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −ψ(3​(N−1)2​r(x1−ck,1))×~(ψ(3​(N−1)2​r(x2−ck,2)),⋯)|\displaystyle\displaystyle-\psi\left(\frac{3(N-1)}{2r}(x\_{1}-c\_{k,1})\right)\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{2}-c\_{k,2})\right),\cdot\cdot\cdot\right)\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|ψ​(3​(N−1)2​r​(x1−ck,1))​×~​(ψ​(3​(N−1)2​r​(x2−ck,2)),⋯)−ϕ𝐜k​(𝐱)|\displaystyle\displaystyle+\bigg|\psi\left(\frac{3(N-1)}{2r}(x\_{1}-c\_{k,1})\right)\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{2}-c\_{k,2})\right),\cdot\cdot\cdot\right)-\phi\_{\mathbf{c}\_{k}}(\mathbf{x})\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | δ+ℰ2,\displaystyle\displaystyle\delta+\mathcal{E}\_{2}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ2\displaystyle\displaystyle\mathcal{E}\_{2} | =|ψ​(3​(N−1)2​r​(x1−ck,1))​×~​(ψ​(3​(N−1)2​r​(x2−ck,2)),⋯)−ϕ𝐜k​(𝐱)|\displaystyle\displaystyle=\bigg|\psi\left(\frac{3(N-1)}{2r}(x\_{1}-c\_{k,1})\right)\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{2}-c\_{k,2})\right),\cdot\cdot\cdot\right)-\phi\_{\mathbf{c}\_{k}}(\mathbf{x})\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|ψ​(3​(N−1)2​r​(x1−ck,1))|​|×~​(ψ​(3​(N−1)2​r​(x2−ck,2)),⋯)−∏j=2d1ψ​(3​(N−1)2​r​(xj−ck,j))|\displaystyle\displaystyle=\bigg|\psi\left(\frac{3(N-1)}{2r}(x\_{1}-c\_{k,1})\right)\bigg|\bigg|\widetilde{\times}\left(\psi\left(\frac{3(N-1)}{2r}(x\_{2}-c\_{k,2})\right),\cdot\cdot\cdot\right)-\prod\_{j=2}^{d\_{1}}\psi\left(\frac{3(N-1)}{2r}(x\_{j}-c\_{k,j})\right)\bigg| |  |

Repeat this process to estimate ℰ2,ℰ3,…,ℰd1+1\displaystyle\mathcal{E}\_{2},\mathcal{E}\_{3},...,\mathcal{E}\_{d\_{1}+1}, where ℰd1+1=∏k=1d1ψ​(3​(N−1)2​γ1​(x2−ck,2))−ϕ𝐜k=0\displaystyle\mathcal{E}\_{d\_{1}+1}=\prod\limits\_{k=1}^{d\_{1}}\psi\left(\frac{3(N-1)}{2\gamma\_{1}}(x\_{2}-c\_{k,2})\right)-\phi\_{\mathbf{c}\_{k}}=0.
This implies that ‖ϕ𝐜k−q~k‖L∞​(Ωr)≤d1​δ\displaystyle\|\phi\_{\mathbf{c}\_{k}}-\widetilde{q}\_{k}\|\_{L^{\infty}(\Omega\_{r})}\leq d\_{1}\delta.
Thus, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|ϕ𝐜k​(Xt)−q~k​(Xt)|2​𝟏Ωr​(Xt)]≤d12​δ2.\displaystyle\displaystyle\mathbb{E}\left[\sup\_{0\leq t\leq T}|\phi\_{\mathbf{c}\_{k}}(X\_{t})-\widetilde{q}\_{k}(X\_{t})|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\right]\leq d^{2}\_{1}\delta^{2}. |  |

Applying Cauchy–Schwarz inequality and the Assumption [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​[sup0≤t≤T|∑k=1Nd1g​(𝐜k)​q~k​(Xt)−g¯​(Xt)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\left[\sup\_{0\leq t\leq T}\left|\sum\_{k=1}^{N^{d\_{1}}}g(\mathbf{c}\_{k})\widetilde{q}\_{k}(X\_{t})-\bar{g}(X\_{t})\right|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\right] |  | (4.8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[sup0≤t≤T|∑k=1Nd1g​(𝐜k)​q~k​(Xt)−∑k=1Nd1g​(𝐜k)​ϕ𝐜k​(Xt)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\left[\sup\_{0\leq t\leq T}\left|\sum\_{k=1}^{N^{d\_{1}}}g(\mathbf{c}\_{k})\widetilde{q}\_{k}(X\_{t})-\sum\_{k=1}^{N^{d\_{1}}}g(\mathbf{c}\_{k})\phi\_{\mathbf{c}\_{k}}(X\_{t})\right|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[∑k=1Nd1|g​(𝐜k)|2​sup0≤t≤T∑k=1Nd1|q~k​(Xt)−ϕ𝐜k​(Xt)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\left[\sum\_{k=1}^{N^{d\_{1}}}|g(\mathbf{c}\_{k})|^{2}\sup\_{0\leq t\leq T}\sum\_{k=1}^{N^{d\_{1}}}|\widetilde{q}\_{k}(X\_{t})-\phi\_{\mathbf{c}\_{k}}(X\_{t})|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | d12​N2​d1​Cg2​(1+rp)2​δ2≤ε2,\displaystyle\displaystyle d\_{1}^{2}N^{2d\_{1}}C\_{g}^{2}(1+r^{p})^{2}\delta^{2}\leq\frac{\varepsilon}{2}, |  | (4.9) |

where the last inequality follows from the fact Xt∈Ωr\displaystyle X\_{t}\in\Omega\_{r} and the polynomial growth of g\displaystyle g.
By selecting δ=ε2​d12​N2​d1​Cg2​(1+rp)2=O(d1−d12εd1+12(log(ε−1))−d1+pα\displaystyle\delta=\sqrt{\frac{\varepsilon}{2d\_{1}^{2}N^{2d\_{1}}C\_{g}^{2}(1+r^{p})^{2}}}=O(d\_{1}^{-\frac{d\_{1}}{2}}\varepsilon^{\frac{d\_{1}+1}{2}}\left(\log(\varepsilon^{-1})\right)^{-\frac{d\_{1}+p}{\alpha}} ).
Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sup0≤t≤T|g​(Xt)−∑k=1Nd1g​(𝐜k)​q~k|2]\displaystyle\displaystyle\mathbb{E}\left[\sup\_{0\leq t\leq T}\left|g(X\_{t})-\sum\_{k=1}^{N^{d\_{1}}}g(\mathbf{c}\_{k})\widetilde{q}\_{k}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤T|g​(Xt)−g¯​(Xt)|2]+𝔼​[sup0≤t≤T|g¯​(Xt)−∑k=1Nd1u​(𝐜k)​q~k|2]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\left|g(X\_{t})-\bar{g}(X\_{t})\right|^{2}\Big]+\mathbb{E}\left[\sup\_{0\leq t\leq T}\left|\bar{g}(X\_{t})-\sum\_{k=1}^{N^{d\_{1}}}u(\mathbf{c}\_{k})\widetilde{q}\_{k}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | ε2+ε2=ε.\displaystyle\displaystyle\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon. |  |

The network architecture is then specified in the theorem.
∎

### 4.2 Functional Approximations

###### Theorem 4.2.

Let 𝖥\displaystyle\mathsf{F} be defined in Definition [2.6](https://arxiv.org/html/2511.07235v1#S2.Thmtheorem6 "Definition 2.6 (Lipschitz functional). ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), and assume Assumptions [1](https://arxiv.org/html/2511.07235v1#Thmassumption1 "Assumption 1. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), and [4](https://arxiv.org/html/2511.07235v1#Thmassumption4 "Assumption 4. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models") hold.
For any ε>0\displaystyle\varepsilon>0,
set r=⌈−2​CTc​log⁡ε28​C0​L𝖥2⌉1α+1\displaystyle r=\left\lceil-\frac{2C\_{T}}{c}\log\frac{\varepsilon^{2}}{8C\_{0}L\_{\mathsf{F}}^{2}}\right\rceil^{\frac{1}{\alpha}}+1.
Let {𝐜m}m=1Nδ⊂Qr\displaystyle\{\mathbf{c}\_{m}\}\_{m=1}^{N^{\delta}}\subset Q\_{r} so that {ℬδ​(𝐜m)}m=1Nδ\displaystyle\{\mathcal{B}\_{\delta}(\mathbf{c}\_{m})\}\_{m=1}^{N^{\delta}} is a cover of Qr\displaystyle Q\_{r} for some Nδ>0\displaystyle N^{\delta}>0 to be estimated in Remark [4.4](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem4 "Remark 4.4. ‣ 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"),
and with ball radius δ=C​ε​(L𝖥​Lg)−1​d1−12\displaystyle\delta=C\varepsilon(L\_{\mathsf{F}}L\_{g})^{-1}d\_{1}^{-\frac{1}{2}}, with C\displaystyle C a constant.
Let H=O​(Nδ​ε−Nδ)\displaystyle H=O(\sqrt{N^{\delta}}\varepsilon^{-N^{\delta}}), and set the network ℱNN​(N,1,L,𝔭,K,κ,R)\displaystyle\mathcal{F}\_{\rm NN}(N,1,L,\mathfrak{p},K,\kappa,R)
with

|  |  |  |
| --- | --- | --- |
|  | ℒ=O​((Nδ)2​log⁡(Nδ)+(Nδ)2​log⁡(ε−1)),𝔭=O​(1),K=O​((Nδ)2​log⁡Nδ+(Nδ)2​log⁡(ε−1)),\displaystyle\displaystyle\mathcal{L}=O\left((N^{\delta})^{2}\log(N^{\delta})+(N^{\delta})^{2}\log(\varepsilon^{-1})\right),\mathfrak{p}=O(1),K=O\left((N^{\delta})^{2}\log N^{\delta}+(N^{\delta})^{2}\log(\varepsilon^{-1})\right), |  |
|  |  |  |
| --- | --- | --- |
|  | κ=O​((Nδ)−Nδ2​ε−Nδ−12),R=1.\displaystyle\displaystyle\kappa=O((N^{\delta})^{-\frac{N^{\delta}}{2}}\varepsilon^{\frac{-N^{\delta}-1}{2}}),R=1. |  |

There are
{q~k}k=1H\displaystyle\{\widetilde{q}\_{k}\}\_{k=1}^{H} with q~k∈ℱNN​(Nδ,1,ℒ,𝔭,K,κ,R)\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{\rm NN}(N^{\delta},1,\mathcal{L},\mathfrak{p},K,\kappa,R) for any k\displaystyle k, such that we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | supg∈𝒢|𝖥​g−∑k=1Hak​q~k​(𝒈)|≤ε,\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}|\mathsf{F}g-\sum\_{k=1}^{H}a\_{k}\widetilde{q}\_{k}(\bm{g})|\leq\varepsilon, |  | (4.10) |

where 𝐠=[g​(𝐜1),g​(𝐜2),…,g​(𝐜Nδ)]⊤\displaystyle\bm{g}=[g(\mathbf{c}\_{1}),g(\mathbf{c}\_{2}),...,g(\mathbf{c}\_{N^{\delta}})]^{\top}, ak\displaystyle a\_{k}’s are coefficients depending on 𝖥\displaystyle\mathsf{F}.
The constant hidden in O\displaystyle O and all constants C\displaystyle C depend on the constants L𝖥,Lg,CT,C0,c,α\displaystyle L\_{\mathsf{F}},L\_{g},C\_{T},C\_{0},c,\alpha in the assumptions.

###### Proof.

For r>0\displaystyle r>0, define the cube as before,

|  |  |  |
| --- | --- | --- |
|  | Qr:=[−r,r]d1={x∈ℝd1:‖x‖∞<r},where ​‖x‖∞:=max1≤j≤d⁡|xj|.Q\_{r}:=[-r,r]^{d\_{1}}\;=\;\left\{x\in\mathbb{R}^{d\_{1}}:\|x\|\_{\infty}<r\right\},\qquad\mbox{where }\|x\|\_{\infty}:=\max\_{1\leq j\leq d}|x\_{j}|. |  |

Here r\displaystyle r is chosen so that tail probability is small as we did in the function approximation. Let {Bδ​(ck)}k=1Nδ\displaystyle\{B\_{\delta}(c\_{k})\}\_{k=1}^{N^{\delta}} be a finite cover of Qr\displaystyle Q\_{r} by Nδ\displaystyle N^{\delta} Euclidean balls.
By the Lemma [2.7](https://arxiv.org/html/2511.07235v1#S2.Thmtheorem7 "Lemma 2.7 (Theorem 13.7(ii) of [41]). ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), there exists a partition of unity {wk​(x)}k=1N\displaystyle\{w\_{k}(x)\}\_{k=1}^{N} subordinate to the cover {Bδ​(ck)}k=1Nδ\displaystyle\{B\_{\delta}(c\_{k})\}\_{k=1}^{N^{\delta}}.

For any g∈𝒰\displaystyle g\in\mathcal{U}, define 𝒈=[g​(c1),g​(c2),…,g​(cNδ)]𝖳\displaystyle\bm{g}=[g(c\_{1}),g(c\_{2}),\ldots,g(c\_{N^{\delta}})]^{\mathsf{T}}, and define,

|  |  |  |  |
| --- | --- | --- | --- |
|  | gw​(x)={∑k=1Nδg​(ck)​wk​(x),x∈Ωr,0,x∈ΩrC.\displaystyle\displaystyle g\_{w}(x)=\begin{cases}\displaystyle\sum\_{k=1}^{N^{\delta}}g(c\_{k})\,w\_{k}(x),&x\in\Omega\_{r},\\[3.44444pt] 0,&x\in\Omega\_{r}^{\,C}\,.\end{cases} |  | (4.11) |

Then, similar to the estimates in ([4.7](https://arxiv.org/html/2511.07235v1#S4.E7 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), as Nδ\displaystyle N^{\delta} is the covering number of all d1\displaystyle d\_{1} dimensions, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[supt≤s≤T|g​(Xs)−gw​(Xs)|2]\displaystyle\displaystyle\mathbb{E}\!\left[\sup\_{t\leq s\leq T}\bigl|g(X\_{s})-g\_{w}(X\_{s})\bigr|^{2}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[supt≤s≤T|g​(Xs)|2​𝟏ΩrC​(Xs)]⏟𝒥1+𝔼​[supt≤s≤T|g​(Xs)−gw​(Xs)|2​𝟏Ωr​(Xt)]⏟𝒥2.\displaystyle\displaystyle\underbrace{\mathbb{E}\Big[\sup\_{t\leq s\leq T}\Big|g(X\_{s})\Big|^{2}\mathbf{1}\_{\Omega\_{r}^{C}}(X\_{s})\Big]}\_{\mathcal{J}\_{1}}+\underbrace{\mathbb{E}\Big[\sup\_{t\leq s\leq T}\Big|g(X\_{s})-g\_{w}(X\_{s})\Big|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big]}\_{\mathcal{J}\_{2}}. |  | (4.12) |

Similar to ([4.4](https://arxiv.org/html/2511.07235v1#S4.E4 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥1≤C0​e−c​rα2​CT.\displaystyle\displaystyle\mathcal{J}\_{1}\leq C\_{0}e^{-\frac{cr^{\alpha}}{2C\_{T}}}. |  | (4.13) |

Similar to ([4.5](https://arxiv.org/html/2511.07235v1#S4.E5 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), taking into consideration of the radius of the covering ball being δ\displaystyle\delta, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥2=\displaystyle\displaystyle\mathcal{J}\_{2}= | 𝔼​[supt≤s≤T|∑k=1Nδ[g​(Xs)−g​(𝐜k)]​wk​(Xs)|2​𝟏Ωr​(Xs)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{t\leq s\leq T}\Big|\sum\_{k=1}^{N^{\delta}}[g(X\_{s})-g(\mathbf{c}\_{k})]w\_{k}(X\_{s})\Big|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{s})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[supt≤s≤T(∑k=1Nδ|g​(Xs)−g​(𝐜k)|​|wk​(Xs)|)2​𝟏Ωr​(Xs)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{t\leq s\leq T}\Big(\sum\_{k=1}^{N^{\delta}}|g(X\_{s})-g(\mathbf{c}\_{k})||w\_{k}(X\_{s})|\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{s})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[supt≤s≤T(∑k:‖𝐜k−Xs‖∞≤δ|g​(Xs)−g​(𝐜k)|​wk​(Xs))2​𝟏Ωr​(Xs)],\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{t\leq s\leq T}\Big(\sum\_{k:\|\mathbf{c}\_{k}-X\_{s}\|\_{\infty}\leq\delta}|g(X\_{s})-g(\mathbf{c}\_{k})|w\_{k}(X\_{s})\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{s})\Big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[supt≤s≤T(maxk:‖𝐜k−Xs‖∞≤δ⁡|g​(Xs)−g​(𝐜k)|​(∑k:|𝐜k−Xs|≤δwk​(Xs)))2​𝟏Ωr​(Xs)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{t\leq s\leq T}\Big(\max\_{k:\|\mathbf{c}\_{k}-X\_{s}\|\_{\infty}\leq\delta}|g(X\_{s})-g(\mathbf{c}\_{k})|\Big(\sum\_{k:|\mathbf{c}\_{k}-X\_{s}|\leq\delta}w\_{k}(X\_{s})\Big)\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{s})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[supt≤s≤Tmaxk:‖𝐜k−Xs‖∞≤δ⁡|g​(Xs)−g​(𝐜k)|2​𝟏Ωr​(Xs)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{t\leq s\leq T}\max\_{k:\|\mathbf{c}\_{k}-X\_{s}\|\_{\infty}\leq\delta}|g(X\_{s})-g(\mathbf{c}\_{k})|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{s})\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | (Lg​δ)2​d1.\displaystyle\displaystyle(L\_{g}\delta)^{2}d\_{1}. |  | (4.14) |

From the Lipschitz property of the functional 𝖥\displaystyle\mathsf{F} defined in Definition [2.6](https://arxiv.org/html/2511.07235v1#S2.Thmtheorem6 "Definition 2.6 (Lipschitz functional). ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝖥​(g)−𝖥​(gw)|2\displaystyle\displaystyle\bigl|\mathsf{F}(g)-\mathsf{F}(g\_{w})\bigr|^{2} | ≤L𝖥2​‖g−gw‖S22\displaystyle\displaystyle\leq L\_{\mathsf{F}}^{2}\,\|g-g\_{w}\|\_{S^{2}}^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤L𝖥2​((Lg​δ)2​d1+C0​e−c​rα2​CT)<ε2/4,\displaystyle\displaystyle\leq\;L\_{\mathsf{F}}^{2}\left((L\_{g}\delta)^{2}d\_{1}+\;C\_{0}e^{-\frac{cr^{\alpha}}{2C\_{T}}}\right)\ <\varepsilon^{2}/4, |  | (4.15) |

i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝖥​(g)−𝖥​(gw)|<ε/2,\displaystyle\displaystyle\bigl|\mathsf{F}(g)-\mathsf{F}(g\_{w})\bigr|<\varepsilon/2, |  | (4.16) |

which follows by selecting

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=⌈−2​CTc​log⁡ε28​C0​L𝖥2⌉1α+1,δ=ε2​2​L𝖥​Lg​d112.\displaystyle\displaystyle r=\left\lceil-\frac{2C\_{T}}{c}\log\frac{\varepsilon^{2}}{8C\_{0}L\_{\mathsf{F}}^{2}}\right\rceil^{\frac{1}{\alpha}}+1,\quad\delta=\frac{\varepsilon}{2\sqrt{2}L\_{\mathsf{F}}L\_{g}d\_{1}^{\frac{1}{2}}}. |  | (4.17) |

Now, for any g,g~∈𝒢\displaystyle g,\widetilde{g}\in\mathcal{G}, define gw\displaystyle g\_{w} and g~w\displaystyle\widetilde{g}\_{w} as in ([4.11](https://arxiv.org/html/2511.07235v1#S4.E11 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), and set

|  |  |  |
| --- | --- | --- |
|  | 𝒈=[g​(c1),…,g​(cNδ)]𝖳,𝒈~=[g~​(c1),…,g~​(cNδ)]𝖳.\bm{g}=\bigl[g(c\_{1}),\ldots,g(c\_{N^{\delta}})\bigr]^{\mathsf{T}},\qquad\widetilde{\bm{g}}=\bigl[\widetilde{g}(c\_{1}),\ldots,\widetilde{g}(c\_{N^{\delta}})\bigr]^{\mathsf{T}}. |  |

Define the function h​(𝒈):=𝖥​(gw)\displaystyle h(\bm{g}):=\mathsf{F}(g\_{w}).
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h​(𝒈)−h​(𝒈~)|2\displaystyle\displaystyle|h(\bm{g})-h(\widetilde{\bm{g}})|^{2} | =|𝖥​(gw)−𝖥​(g~w)|2\displaystyle\displaystyle=\bigl|\mathsf{F}(g\_{w})-\mathsf{F}(\widetilde{g}\_{w})\bigr|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L𝖥2​‖gw−g~w‖S22\displaystyle\displaystyle\leq L\_{\mathsf{F}}^{2}\,\|g\_{w}-\widetilde{g}\_{w}\|\_{S^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =L𝖥2​𝔼​[supt≤s≤T(∑k=1Nδ(g​(ck)−g~​(ck))​wk​(Xs))2]\displaystyle\displaystyle=L\_{\mathsf{F}}^{2}\,\mathbb{E}\!\left[\sup\_{t\leq s\leq T}\!\!\Bigl(\sum\_{k=1}^{N^{\delta}}\bigl(g(c\_{k})-\widetilde{g}(c\_{k})\bigr)\,w\_{k}(X\_{s})\Bigr)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L𝖥2​(∑k=1Nδ|g​(ck)−g~​(ck)|2)​𝔼​[supt≤s≤T∑k=1Nδwk​(Xs)2]\displaystyle\displaystyle\leq L\_{\mathsf{F}}^{2}\,\Bigl(\sum\_{k=1}^{N^{\delta}}|g(c\_{k})-\widetilde{g}(c\_{k})|^{2}\Bigr)\,\mathbb{E}\!\left[\sup\_{t\leq s\leq T}\sum\_{k=1}^{N^{\delta}}w\_{k}(X\_{s})^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L𝖥2​(∑k=1Nδ|g​(ck)−g~​(ck)|2)\displaystyle\displaystyle\leq L\_{\mathsf{F}}^{2}\,\,\Bigl(\sum\_{k=1}^{N^{\delta}}|g(c\_{k})-\widetilde{g}(c\_{k})|^{2}\Bigr) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤L𝖥2​|𝒈−𝒈~|2,\displaystyle\displaystyle\leq L\_{\mathsf{F}}^{2}\,\,|\bm{g}-\widetilde{\bm{g}}|^{2}, |  | (4.18) |

where we use the fact that {wk​(x)}k=1Nδ\displaystyle\{w\_{k}(x)\}\_{k=1}^{N^{\delta}} is a partition of unity. Thus we show that h​(𝒈):=𝖥​(gw)\displaystyle h(\bm{g}):=\mathsf{F}(g\_{w}) is a Lipchitz function on 𝒢\displaystyle\mathcal{G} according to ([4.18](https://arxiv.org/html/2511.07235v1#S4.E18 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")).Besides, according to the assumption on 𝖥\displaystyle\mathsf{F} and the definition of h\displaystyle h, h\displaystyle h is bounded.
Also, the domain of h\displaystyle h is bounded by the range of g\displaystyle g.
Consequently, h\displaystyle h satisfies the approximation rate estimate in [[34](https://arxiv.org/html/2511.07235v1#bib.bib34)][Theorem 5], it follows that, for ε>0\displaystyle\varepsilon>0, if we set H=C​Nδ​ε−Nδ\displaystyle H=C\sqrt{N^{\delta}}\varepsilon^{-N^{\delta}} for some C\displaystyle C, then there exists a
network architecture ℱNN​(Nδ,1,ℒ,𝔭,K,κ,R)\displaystyle\mathcal{F}\_{\rm NN}(N^{\delta},1,\mathcal{L},\mathfrak{p},K,\kappa,R) and {q~k}k=1H\displaystyle\{\widetilde{q}\_{k}\}\_{k=1}^{H} with q~k∈ℱNN​(Nδ,1,ℒ,𝔭,K,κ,R)\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{\rm NN}(N^{\delta},1,\mathcal{L},\mathfrak{p},K,\kappa,R) for k=1,…,H\displaystyle k=1,\ldots,H such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supg∈𝒢|𝖥​(gw)−∑k=1Hak​q~k​(𝒈)|≤ε2,\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\left|\mathsf{F}(g\_{w})-\sum\_{k=1}^{H}a\_{k}\widetilde{q}\_{k}(\bm{g})\right|\leq\frac{\varepsilon}{2}, |  | (4.19) |

where ak\displaystyle a\_{k} are constants depending on f\displaystyle f.
Such an architecture has

|  |  |  |
| --- | --- | --- |
|  | ℒ=O​((Nδ)2​log⁡(Nδ)+(Nδ)2​log⁡(ε−1)),𝔭=O​(1),K=O​((Nδ)2​log⁡Nδ+(Nδ)2​log⁡(ε−1)),\displaystyle\displaystyle\mathcal{L}=O\left((N^{\delta})^{2}\log(N^{\delta})+(N^{\delta})^{2}\log(\varepsilon^{-1})\right),\mathfrak{p}=O(1),K=O\left((N^{\delta})^{2}\log N^{\delta}+(N^{\delta})^{2}\log(\varepsilon^{-1})\right), |  |
|  |  |  |
| --- | --- | --- |
|  | κ=O​((Nδ)−Nδ2​ε−Nδ−12),R=1.\displaystyle\displaystyle\kappa=O((N^{\delta})^{-\frac{N^{\delta}}{2}}\varepsilon^{\frac{-N^{\delta}-1}{2}}),R=1. |  |

Finally, We have, for any g∈𝒢\displaystyle g\in\mathcal{G} and 𝒈=[g​(c1),…,g​(cNδ)]⊤\displaystyle\bm{g}=[g(c\_{1}),...,g(c\_{N^{\delta}})]^{\top}

|  |  |  |  |
| --- | --- | --- | --- |
|  | supg∈𝒢|𝖥​(g)−∑k=1Hak​q~k​(𝒈)|≤\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\left|\mathsf{F}(g)-\sum\_{k=1}^{H}a\_{k}\widetilde{q}\_{k}(\bm{g})\right|\leq | supg∈𝒢|𝖥​(g)−h​(𝒈)|+sup𝒈|h​(𝒈)−∑k=1Hak​q~k​(𝒈)|\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\left|\mathsf{F}(g)-h(\bm{g})\right|+\sup\_{\bm{g}}\left|h(\bm{g})-\sum\_{k=1}^{H}a\_{k}\widetilde{q}\_{k}(\bm{g})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | ε2+ε2=ε.\displaystyle\displaystyle\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon. |  |

∎

The next lemma and remark are used to estimate Nδ\displaystyle N^{\delta} and H\displaystyle H.

###### Lemma 4.3.

Let 𝔇=[−γ,γ]d\displaystyle\mathfrak{D}=[-\gamma,\gamma]^{d} for some γ>0\displaystyle\gamma>0. For any δ>0\displaystyle\delta>0, there exists a cover {ℬδ​(𝐜m)}m=1M\displaystyle\{\mathcal{B}\_{\delta}(\mathbf{c}\_{m})\}\_{m=1}^{M} of 𝔇\displaystyle\mathfrak{D} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | M≤C​δ−d,\displaystyle\displaystyle{\color[rgb]{0,0,0}M\leq C\delta^{-d}}, |  | (4.20) |

where C\displaystyle C is a constant depending on γ\displaystyle\gamma and d\displaystyle d.

###### Proof of Lemma [4.3](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models").

By [[14](https://arxiv.org/html/2511.07235v1#bib.bib14), Chapter 2], we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | c≤⌈2​γδ⌉d+7​d​log⁡d≤C​(γδ)d\displaystyle\displaystyle{\color[rgb]{0,0,0}c\leq\left\lceil\frac{2\gamma}{\delta}\right\rceil^{d}+7d\log d\leq C\left(\frac{\gamma}{\delta}\right)^{d}} |  | (4.21) |

for some C\displaystyle C depending on γ\displaystyle\gamma and d\displaystyle d.
∎

###### Remark 4.4.

In this remark, we estimate the number of covering Nδ\displaystyle N^{\delta} and hence the number of basis H\displaystyle H needed.
By Lemma [4.3](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models") and Equation [4.17](https://arxiv.org/html/2511.07235v1#S4.E17 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models") in the proof, it follows that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nδ≤C​(γδ)d1\displaystyle\displaystyle N^{\delta}\leq C\left(\frac{\gamma}{\delta}\right)^{d\_{1}} | ≤C​(−2​CTc)d1α​(log⁡ε28​C0​L𝖥2)d1α​ε−d1​d1d12\displaystyle\displaystyle\leq C(-\frac{2C\_{T}}{c})^{\frac{d\_{1}}{\alpha}}\left(\log\frac{\varepsilon^{2}}{8C\_{0}L\_{\mathsf{F}}^{2}}\right)^{\frac{d\_{1}}{\alpha}}\varepsilon^{-d\_{1}}d\_{1}^{\frac{d\_{1}}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(log⁡(ε−2))d1α​ε−d1,\displaystyle\displaystyle\leq C\left(\log(\varepsilon^{-2})\right)^{\frac{d\_{1}}{\alpha}}\varepsilon^{-d\_{1}}, |  |

where the constant C\displaystyle C depends on CT\displaystyle C\_{T}, c\displaystyle c, C0\displaystyle C\_{0}, α\displaystyle\alpha, L𝖥,Lg\displaystyle L\_{\mathsf{F}},L\_{g} and d1\displaystyle d\_{1}.
Dropping the lower order term in Equation [4.4](https://arxiv.org/html/2511.07235v1#S4.Ex52 "Remark 4.4. ‣ 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"), it follows that

|  |  |  |
| --- | --- | --- |
|  | H=C​(Nδ)12​ε−Nδ=C​ε−d12​ε−ε−d1,\displaystyle\displaystyle H=C(N^{\delta})^{\frac{1}{2}}\varepsilon^{-N^{\delta}}=C\varepsilon^{-\frac{d\_{1}}{2}}\varepsilon^{-\varepsilon^{-d\_{1}}}, |  |

or H=𝒪​(ε−ε−d1)\displaystyle H=\mathcal{O}(\varepsilon^{-\varepsilon^{-d\_{1}}}).

### 4.3 Operator Approximation

###### Theorem 4.5.

[Operator]
Let Assumptions [1](https://arxiv.org/html/2511.07235v1#Thmassumption1 "Assumption 1. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [4](https://arxiv.org/html/2511.07235v1#Thmassumption4 "Assumption 4. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [5](https://arxiv.org/html/2511.07235v1#Thmassumption5 "Assumption 5. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), and [6](https://arxiv.org/html/2511.07235v1#Thmassumption6 "Assumption 6. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models") hold.
For any ε>0\displaystyle\varepsilon>0,
set N1=C​ε−d2\displaystyle N\_{1}=C\varepsilon^{-d\_{2}}, and N2=O​(ε−d1​d2−d1)\displaystyle N\_{2}=O(\varepsilon^{-d\_{1}d\_{2}-d\_{1}}).
Define the network architecture ℱ1=ℱNN​(d2,1,ℒ1,𝔭1,K1,κ1)\displaystyle\mathcal{F}\_{1}=\mathcal{F}\_{\rm NN}(d\_{2},1,\mathcal{L}\_{1},\mathfrak{p}\_{1},K\_{1},\kappa\_{1}) and ℱ2=ℱNN​(N2,1,ℒ2,𝔭2,K2,κ2)\displaystyle\mathcal{F}\_{2}=\mathcal{F}\_{\rm NN}(N\_{2},1,\mathcal{L}\_{2},\mathfrak{p}\_{2},K\_{2},\kappa\_{2}) with

|  |  |  |
| --- | --- | --- |
|  | ℒ1=O​(log⁡(ε−2)),𝔭1=O​(1),K1=O​(log⁡(ε−2)),κ1=O​(ε−d2),R=1,\displaystyle\displaystyle\mathcal{L}\_{1}=O\left(\log(\varepsilon^{-2})\right),\ \mathfrak{p}\_{1}=O(1),\ K\_{1}=O\left(\log(\varepsilon^{-2})\right),\ \kappa\_{1}=O(\varepsilon^{-d\_{2}}),R=1, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ℒ2=O​(N22​log⁡N2+N22​log⁡(ε−d2−1)),𝔭2=O​(N212​ε−N2​d2−N2),\displaystyle\displaystyle\mathcal{L}\_{2}=O\left(N\_{2}^{2}\log N\_{2}+N\_{2}^{2}\log(\varepsilon^{-d\_{2}-1})\right),\ \mathfrak{p}\_{2}=O(N\_{2}^{\frac{1}{2}}\varepsilon^{-N\_{2}d\_{2}-N\_{2}}), |  |
|  |  |  |
| --- | --- | --- |
|  | K2=O​(N212​ε−N2​d2−N2​(N22​log⁡N2+N22​log⁡(ε−d2−1))),\displaystyle\displaystyle K\_{2}=O\left(N\_{2}^{\frac{1}{2}}\varepsilon^{-N\_{2}d\_{2}-N\_{2}}\left(N\_{2}^{2}\log N\_{2}+N\_{2}^{2}\log(\varepsilon^{-d\_{2}-1})\right)\right), |  |
|  |  |  |
| --- | --- | --- |
|  | κ2=O​(N2−N22​ε−N2​d22−N2).\displaystyle\displaystyle\kappa\_{2}=O(N\_{2}^{-\frac{N\_{2}}{2}}\varepsilon^{-\frac{N\_{2}d\_{2}}{2}-N\_{2}}). |  |

For any operator Γ:𝒢→𝒰\displaystyle\Gamma:\mathcal{G}\rightarrow\mathcal{U} satisfying Assumption [6](https://arxiv.org/html/2511.07235v1#Thmassumption6 "Assumption 6. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), there are {q~k}k=1N1\displaystyle\{\widetilde{q}\_{k}\}\_{k=1}^{N\_{1}} with q~k∈ℱ1\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{1} and {a~k}k=1N1\displaystyle\{\widetilde{a}\_{k}\}\_{k=1}^{N\_{1}} with a~k∈ℱ2\displaystyle\widetilde{a}\_{k}\in\mathcal{F}\_{2} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supg∈𝒢𝔼​[sup0≤t≤T|Γ​(g)​(Xt)−∑k=1N1a~k​(𝒈)​q~k​(Xt)|]≤ε.\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq t\leq T}\left|\Gamma(g)(X\_{t})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{t})\right|\bigg]\leq\varepsilon. |  | (4.22) |

###### Proof of Theorem [4.5](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.3 Operator Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models").

By Assumption [5](https://arxiv.org/html/2511.07235v1#Thmassumption5 "Assumption 5. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models") and [6](https://arxiv.org/html/2511.07235v1#Thmassumption6 "Assumption 6. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), Γ​(g)​(⋅)\displaystyle\Gamma(g)(\cdot) satisfies the assumptions of Theorem [4.1](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models").
It follows that, for ε1>0\displaystyle\varepsilon\_{1}>0 which will be specified,
set r=⌈−2​CTc​log⁡ε14​C0⌉1α\displaystyle r=\left\lceil-\frac{2C\_{T}}{c}\log\frac{\varepsilon\_{1}}{4C\_{0}}\right\rceil^{\frac{1}{\alpha}}, and define Qr,Ωr\displaystyle Q\_{r},\Omega\_{r} as in Definition [2.2](https://arxiv.org/html/2511.07235v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"),
there exists a constant N1=C​ε1−d2\displaystyle N\_{1}=C\varepsilon\_{1}^{-d\_{2}} for some constant C\displaystyle C depending on d2,Lg\displaystyle d\_{2},L\_{g} and r\displaystyle r, a network architecture ℱ1=ℱNN​(d2,1,ℒ1,𝔭1,K1,κ1,R1)\displaystyle\mathcal{F}\_{1}=\mathcal{F}\_{\rm NN}(d\_{2},1,\mathcal{L}\_{1},\mathfrak{p}\_{1},K\_{1},\kappa\_{1},R\_{1}) and {q~k}k=1N1\displaystyle\{\widetilde{q}\_{k}\}\_{k=1}^{N\_{1}} with q~k∈ℱ1\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{1}, and {𝐜k}k=1N1⊂Qr\displaystyle\{\mathbf{c}\_{k}\}\_{k=1}^{N\_{1}}\subset Q\_{r} such that for any g∈𝒢\displaystyle g\in\mathcal{G}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Γ​(g)​(Xt)−∑k=1N1Γ​(g)​(𝐜k)​q~k​(Xt)|2]1/2≤ε1.\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq t\leq T}\left|\Gamma(g)(X\_{t})-\sum\_{k=1}^{N\_{1}}\Gamma(g)(\mathbf{c}\_{k})\widetilde{q}\_{k}(X\_{t})\right|^{2}\bigg]^{1/2}\leq\varepsilon\_{1}. |  | (4.23) |

Such a network has size

|  |  |  |
| --- | --- | --- |
|  | ℒ1=O​(log⁡(ε1−2)),𝔭1=O​(1),K1=O​(log⁡(ε1−2)),κ1=O​(ε1−d2).\displaystyle\displaystyle\mathcal{L}\_{1}=O\left(\log(\varepsilon\_{1}^{-2})\right),\ \mathfrak{p}\_{1}=O(1),\ K\_{1}=O\left(\log(\varepsilon\_{1}^{-2})\right),\ \kappa\_{1}=O(\varepsilon\_{1}^{-d\_{2}}). |  |

For each k\displaystyle k, define the functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖥k​(Γ​g):=Γ​g​(𝐜k).\displaystyle\displaystyle\mathsf{F}\_{k}(\Gamma g):=\Gamma g(\mathbf{c}\_{k}). |  | (4.24) |

For any g1,g2∈𝒢\displaystyle g\_{1},g\_{2}\in\mathcal{G}, and the forward process at t\displaystyle t starts at 𝐜k\displaystyle\mathbf{c}\_{k}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | |𝖥k​(Γ​g1)−𝖥k​(Γ​g2)|2\displaystyle\displaystyle|\mathsf{F}\_{k}(\Gamma g\_{1})-\mathsf{F}\_{k}(\Gamma g\_{2})|^{2} |  | (4.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤s≤T|Γ​(g1)​(Xs)−Γ​(g2)​(Xs)|2]\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq s\leq T}|\Gamma(g\_{1})(X\_{s})-\Gamma(g\_{2})(X\_{s})|^{2}\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | LΓ2​𝔼​[sup0≤s≤T|g1​(Xs)−g2​(Xs)|2]\displaystyle\displaystyle L\_{\Gamma}^{2}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}|g\_{1}(X\_{s})-g\_{2}(X\_{s})|^{2}\bigg] |  | (4.26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | LΓ2​‖g1−g2‖S22,\displaystyle\displaystyle L\_{\Gamma}^{2}\|g\_{1}-g\_{2}\|\_{S^{2}}^{2}, |  | (4.27) |

where the last inequality follows from Assumption [6](https://arxiv.org/html/2511.07235v1#Thmassumption6 "Assumption 6. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models").
By Theorem [4.2](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"), for any ε2>0\displaystyle\varepsilon\_{2}>0, there exist N2\displaystyle N\_{2} and H\displaystyle H with values estimated later, and a network architecture ℱ2=ℱNN​(N2,1,ℒ2,𝔭2,K2,κ2,R2)\displaystyle\mathcal{F}\_{2}=\mathcal{F}\_{\rm NN}(N\_{2},1,\mathcal{L}\_{2},\mathfrak{p}\_{2},K\_{2},\kappa\_{2},R\_{2}) with

|  |  |  |
| --- | --- | --- |
|  | ℒ2=O​(N22​log⁡N2+N22​log⁡(ε2−1)),𝔭2=O​(1),K2=O​(N22​log⁡N2+N22​log⁡(ε2−1)),\displaystyle\displaystyle\mathcal{L}\_{2}=O\left(N\_{2}^{2}\log N\_{2}+N\_{2}^{2}\log(\varepsilon\_{2}^{-1})\right),\ \mathfrak{p}\_{2}=O(1),\ K\_{2}=O\left(N\_{2}^{2}\log N\_{2}+N\_{2}^{2}\log(\varepsilon\_{2}^{-1})\right), |  |
|  |  |  |
| --- | --- | --- |
|  | κ2=O​(N2−N22​ε2−N2−1),R=1.\displaystyle\displaystyle\kappa\_{2}=O(N\_{2}^{-\frac{N\_{2}}{2}}\varepsilon\_{2}^{-N\_{2}-1}),R=1. |  |

Such a network architecture gives a network a~k\displaystyle\widetilde{a}\_{k} so that

|  |  |  |
| --- | --- | --- |
|  | supg|𝖥k​(Γ​(g))−a~k​(𝒈)|≤ε2.\displaystyle\displaystyle\sup\_{g}|\mathsf{F}\_{k}(\Gamma(g))-\widetilde{a}\_{k}(\bm{g})|\leq\varepsilon\_{2}. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sup0≤s≤T|∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[sup0≤s≤T|∑k=1N1(𝖥k​(Γ​g)−a~k​(𝒈))​q~k​(Xs)|]\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\left(\mathsf{F}\_{k}(\Gamma g)-\widetilde{a}\_{k}(\bm{g})\right)\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | ∑k=1N1sup𝒈|𝖥k​(Γ​g)−a~k​(𝒈)|=N1​ε2.\displaystyle\displaystyle\sum\_{k=1}^{N\_{1}}\sup\_{\bm{g}}|\mathsf{F}\_{k}(\Gamma g)-\widetilde{a}\_{k}(\bm{g})|=N\_{1}\varepsilon\_{2}. |  | (4.28) |

Applying the Cauchy–Schwarz inequality, using ([4.23](https://arxiv.org/html/2511.07235v1#S4.E23 "In 4.3 Operator Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([4.28](https://arxiv.org/html/2511.07235v1#S4.E28 "In 4.3 Operator Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | supg∈𝒢𝔼​[sup0≤s≤T|Γ​g​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma g(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | supg∈𝒢𝔼​[sup0≤s≤T|Γ​(g)​(Xs)−∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)|]\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma(g)(X\_{s})-\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +supg∈𝒢𝔼​[sup0≤s≤T|∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle+\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | supg∈𝒢𝔼​[sup0≤s≤T|Γ​(g)​(Xs)−∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)|2]1/2\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma(g)(X\_{s})-\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})\right|^{2}\bigg]^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +supg∈𝒢𝔼​[sup0≤s≤T|∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)−∑k=1Na~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle+\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})-\sum\_{k=1}^{N}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | ε1+N1​ε2.\displaystyle\displaystyle\varepsilon\_{1}+N\_{1}\varepsilon\_{2}. |  |

Set ε2=ε1/(2​N1),ε1=ε2\displaystyle\varepsilon\_{2}=\varepsilon\_{1}/(2N\_{1}),\varepsilon\_{1}=\frac{\varepsilon}{2},
it follows that ε2=O​(εd2+1)\displaystyle\varepsilon\_{2}=O(\varepsilon^{d\_{2}+1}), we then have

|  |  |  |
| --- | --- | --- |
|  | supg∈𝒢𝔼​[sup0≤s≤T|Γ​g​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]≤ε.\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma g(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg]\leq\varepsilon. |  |

By Remark [4.4](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem4 "Remark 4.4. ‣ 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"), the resulting network architectures have N2=O​(ε−d1​d2−d1)\displaystyle N\_{2}=O(\varepsilon^{-d\_{1}d\_{2}-d\_{1}}), the number of basis H\displaystyle H needed is then estimated as
H=O​(N212​ε2−N2)=O​(ε−(d2+1)​ε−d1​d2−d1)\displaystyle H=O(N\_{2}^{\frac{1}{2}}\varepsilon\_{2}^{-N\_{2}})=O(\varepsilon^{-(d\_{2}+1)\varepsilon^{-d\_{1}d\_{2}-d\_{1}}}), which determines the width of ℱ2\displaystyle\mathcal{F}\_{2}, which is p2=H\displaystyle p\_{2}=H.
Consequently, the network size estimate follows,

|  |  |  |
| --- | --- | --- |
|  | ℒ2=O​(N22​log⁡N2+N22​log⁡(ε−d2−1)),𝔭2=O​(N212​ε−N2​d2−N2),\displaystyle\displaystyle\mathcal{L}\_{2}=O\left(N\_{2}^{2}\log N\_{2}+N\_{2}^{2}\log(\varepsilon^{-d\_{2}-1})\right),\ \mathfrak{p}\_{2}=O(N\_{2}^{\frac{1}{2}}\varepsilon^{-N\_{2}d\_{2}-N\_{2}}), |  |
|  |  |  |
| --- | --- | --- |
|  | K2=O​(N212​ε−N2​d2−N2​(N22​log⁡N2+N22​log⁡(ε−d2−1))),\displaystyle\displaystyle K\_{2}=O\left(N\_{2}^{\frac{1}{2}}\varepsilon^{-N\_{2}d\_{2}-N\_{2}}\left(N\_{2}^{2}\log N\_{2}+N\_{2}^{2}\log(\varepsilon^{-d\_{2}-1})\right)\right), |  |
|  |  |  |
| --- | --- | --- |
|  | κ2=O​(N2−N22​ε−N2​d22−N2).\displaystyle\displaystyle\kappa\_{2}=O(N\_{2}^{-\frac{N\_{2}}{2}}\varepsilon^{-\frac{N\_{2}d\_{2}}{2}-N\_{2}}). |  |

∎

## 5 European Option Pricing Operator

After proving the universal approximation of the operator, we consider the following applications on European and American type option pricing problems in this section and the next section. The relationship of the functional, operator and the solution of the BSDE is decripted in the following table [5](https://arxiv.org/html/2511.07235v1#S5 "5 European Option Pricing Operator ‣ Deep Neural Operator Learning for Probabilistic Models").

|  |  |  |
| --- | --- | --- |
| Symbol | Meaning | Definition / Norm |
| 𝒢\displaystyle\mathcal{G} | Input space (payoffs) | 𝔼​[sup0≤s≤T|g​(Xs)|2]<∞\displaystyle\displaystyle\mathbb{E}\!\left[\sup\_{0\leq s\leq T}|g(X\_{s})|^{2}\right]<\infty |
| 𝒰\displaystyle\mathcal{U} | Output space (pricing functions) | 𝔼​[sup0≤s≤T|u​(s,Xs)|2]<∞\displaystyle\displaystyle\mathbb{E}\!\left[\sup\_{0\leq s\leq T}|u(s,X\_{s})|^{2}\right]<\infty |
| Γ\displaystyle\Gamma | Pricing operator | Γ:𝒢→𝒰,g↦u=Γ​(g)\displaystyle\Gamma:\mathcal{G}\to\mathcal{U},\quad g\mapsto u=\Gamma(g) |
| 𝖥t,x\displaystyle\mathsf{F}\_{t,x} | Evaluation functional | 𝖥t,x​(u)=u​(t,x)\displaystyle\mathsf{F}\_{t,x}(u)=u(t,x) |
| Yt\displaystyle Y\_{t} | BSDE solution | Yt=(𝖥t,Xt∘Γ)​(g)\displaystyle Y\_{t}=(\mathsf{F}\_{t,X\_{t}}\circ\Gamma)(g) |

### 5.1 European option pricing

Let (Ω,ℱ,{ℱt}t∈[0,T],ℚ)\displaystyle(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{Q}) be a filtered probability space satisfying the usual conditions, carrying a d\displaystyle d-dimensional Brownian motion B=(B1,…,Bd)\displaystyle B=(B^{1},\dots,B^{d}) under the risk-neutral measure ℚ\displaystyle\mathbb{Q}.

The state process Xt∈ℝd1\displaystyle X\_{t}\in\mathbb{R}^{d\_{1}} follows the diffusion

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b​(t,Xt)​d​t+σ​(t,Xt)​d​Bt,X0=x,dX\_{t}=b(t,X\_{t})\,dt+\sigma(t,X\_{t})\,dB\_{t},\quad X\_{0}=x, |  | (5.1) |

where b:[0,T]×ℝd1→ℝd1\displaystyle b:[0,T]\times\mathbb{R}^{d\_{1}}\to\mathbb{R}^{d\_{1}} and σ:[0,T]×ℝd1→ℝd1×d\displaystyle\sigma:[0,T]\times\mathbb{R}^{d\_{1}}\to\mathbb{R}^{d\_{1}\times d} are measurable, locally bounded, and Lipschitz in x\displaystyle x.
Let g:ℝd1→ℝ\displaystyle g:\mathbb{R}^{d\_{1}}\to\mathbb{R} be the terminal payoff, such that g​(XT)∈L2​(ℚ)\displaystyle g(X\_{T})\in L^{2}(\mathbb{Q}).
The price of the European option is

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(t,x)=𝔼ℚ​[exp⁡(−∫tTr​(s,Xs)​𝑑s)​g​(XT)|Xt=x].u(t,x)=\mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int\_{t}^{T}r(s,X\_{s})\,ds\right)\,g(X\_{T})\,\big|\,X\_{t}=x\right]. |  | (5.2) |

where the risk free rate r​(t,Xt)≥0\displaystyle r(t,X\_{t})\geq 0.

Let ℒ\displaystyle\mathcal{L} denote the infinitesimal generator of Xt\displaystyle X\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℒ​ϕ)​(t,x)=∑i=1nbi​(t,x)​∂xiϕ​(t,x)+12​∑i,j=1nai​j​(t,x)​∂xi​xj2ϕ​(t,x).(\mathcal{L}\phi)(t,x)=\sum\_{i=1}^{n}b\_{i}(t,x)\partial\_{x\_{i}}\phi(t,x)+\frac{1}{2}\sum\_{i,j=1}^{n}a\_{ij}(t,x)\partial\_{x\_{i}x\_{j}}^{2}\phi(t,x). |  | (5.3) |

where a​(t,x)=σ​(t,x)​σ​(t,x)⊤\displaystyle a(t,x)=\sigma(t,x)\sigma(t,x)^{\top}.
Then u​(t,x)\displaystyle u(t,x) satisfies the PDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tu+ℒ​u−r​u=0,u​(T,x)=g​(x).\partial\_{t}u+\mathcal{L}u-ru=0,\qquad u(T,x)=g(x). |  | (5.4) |

In addition, from a probablistic point of view, the price process (Yt,Zt)\displaystyle(Y\_{t},Z\_{t}) satisfies the backward stochastic differential equation (BSDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=g​(XT)−∫tTr​(s,Xs)​Ys​𝑑s−∫tTZs​𝑑Bs,Y\_{t}=g(X\_{T})-\int\_{t}^{T}r(s,X\_{s})Y\_{s}\,ds-\int\_{t}^{T}Z\_{s}\,dB\_{s}, |  | (5.5) |

where Yt=u​(t,Xt)\displaystyle Y\_{t}=u(t,X\_{t}) and Zt=σ⊤​(t,Xt)​∇xu​(t,Xt)\displaystyle Z\_{t}=\sigma^{\top}(t,X\_{t})\nabla\_{x}u(t,X\_{t}).

As an example, in the case of Black–Scholes Model, for a single asset Xt\displaystyle X\_{t} with

|  |  |  |
| --- | --- | --- |
|  | d​Xt=Xt​(r​d​t+σ​d​Bt),dX\_{t}=X\_{t}(r\,dt+\sigma\,dB\_{t}), |  |

and payoff g​(XT)\displaystyle g(X\_{T}), the PDE reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tu+12​σ2​x2​ux​x+(r−q)​x​ux−r​u=0,u​(T,x)=g​(x).\partial\_{t}u+\frac{1}{2}\sigma^{2}x^{2}u\_{xx}+(r-q)xu\_{x}-ru=0,\quad u(T,x)=g(x). |  | (5.6) |

###### Theorem 5.1 (Lipschitz continuity of the European pricing operator in S2\displaystyle S^{2}).

Let (Ω,ℱ,{ℱt}t∈[0,T],ℚ)\displaystyle(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{Q}) support a d\displaystyle d-dimensional
Brownian motion B\displaystyle B, and let the state process X\displaystyle X solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b​(t,Xt)​d​t+σ​(t,Xt)​d​Wt,X0=x,\displaystyle\displaystyle dX\_{t}=b(t,X\_{t})\,dt+\sigma(t,X\_{t})\,dW\_{t},\qquad X\_{0}=x, |  | (5.7) |

with b,σ\displaystyle b,\sigma Lipschitz in x\displaystyle x and of linear growth. Let the risk free rate
r​(t,Xt)\displaystyle r(t,X\_{t}) be bounded and nonnegative, with 0≤r​(t,x)≤r¯\displaystyle 0\leq r(t,x)\leq\bar{r}.
For any terminal payoff g:ℝd1→ℝ\displaystyle g:\mathbb{R}^{d\_{1}}\to\mathbb{R} with
𝔼​[|g​(XT)|2]<∞\displaystyle\mathbb{E}[|g(X\_{T})|^{2}]<\infty, let u=ΓE​g\displaystyle u=\Gamma^{E}g denote the (unique) solution to

|  |  |  |
| --- | --- | --- |
|  | ∂tu+ℒ​u−r​u=0,u​(T,⋅)=g​(⋅),\partial\_{t}u+\mathcal{L}u-r\,u=0,\qquad u(T,\cdot)=g(\cdot), |  |

where ℒ\displaystyle\mathcal{L} is the generator of X\displaystyle X.
Set Ytg:=u​(t,Xt)\displaystyle Y^{g}\_{t}:=u(t,X\_{t}) and define the S2\displaystyle S^{2}-norm
‖Y‖S2:=(𝔼​[sup0≤t≤T|Yt|2])1/2\displaystyle\|Y\|\_{S^{2}}:=\big(\mathbb{E}[\sup\_{0\leq t\leq T}|Y\_{t}|^{2}]\big)^{1/2}.

Then for any two terminal payoffs g1,g2\displaystyle g\_{1},g\_{2}, the operator ΓE\displaystyle\Gamma^{E} satisfies the following condition,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|ΓE​(g1)​(t,Xt)−ΓE​(g2)​(t,Xt)|2]≤L​𝔼​[sup0≤t≤T|g1​(t,Xt)−g2​(t,Xt)|2],\mathbb{E}\!\left[\sup\_{0\leq t\leq T}\!\big|\Gamma^{E}(g\_{1})(t,X\_{t})-\Gamma^{E}(g\_{2})(t,X\_{t})\big|^{2}\right]\;\leq\;L\,\mathbb{E}\!\left[\sup\_{0\leq t\leq T}\!\big|g\_{1}(t,X\_{t})-g\_{2}(t,X\_{t})\big|^{2}\right], |  |

with Lipschitz constant L=4​e2​r¯​T\displaystyle L=4e^{2\bar{r}T}. Hence the pricing operator Γ\displaystyle\Gamma is Lipschitz on S2\displaystyle S^{2}.

###### Proof.

By Feynman–Kac, for each g\displaystyle g we have (under ℚ\displaystyle\mathbb{Q})

|  |  |  |
| --- | --- | --- |
|  | ΓE(g):=Ytg=u(t,Xt)=𝔼[exp(−∫tTr(s,Xs)ds)g(XT)|ℱt].\Gamma^{E}(g):=Y^{g}\_{t}=u(t,X\_{t})=\mathbb{E}\!\left[\exp\!\Big(-\!\int\_{t}^{T}r(s,X\_{s})\,ds\Big)\,g(X\_{T})\,\middle|\,\mathcal{F}\_{t}\right]. |  |

Fix g1,g2\displaystyle g\_{1},g\_{2} and write Δ​g:=g1−g2\displaystyle\Delta g:=g\_{1}-g\_{2},
Δ​Yt:=Ytg1−Ytg2\displaystyle\Delta Y\_{t}:=Y^{g\_{1}}\_{t}-Y^{g\_{2}}\_{t}.
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Yt=\displaystyle\displaystyle\Delta Y\_{t}= | 𝔼[exp(−∫tTr(s,Xs)ds)Δg(XT)|ℱt]\displaystyle\displaystyle\mathbb{E}\!\left[\exp\!\Big(-\!\int\_{t}^{T}r(s,X\_{s})\,ds\Big)\,\Delta g(X\_{T})\,\middle|\,\mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | exp(∫0tr(s,Xs)ds)𝔼[exp(−∫0Tr(s,Xs)ds)Δg(XT)|ℱt]\displaystyle\displaystyle\exp\!\Big(\!\int\_{0}^{t}r(s,X\_{s})\,ds\Big)\,\mathbb{E}\!\left[\exp\!\Big(-\!\int\_{0}^{T}r(s,X\_{s})\,ds\Big)\Delta g(X\_{T})\,\middle|\,\mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | exp⁡(∫0tr​(s,Xs)​𝑑s)​Mt,\displaystyle\displaystyle\exp\!\Big(\!\int\_{0}^{t}r(s,X\_{s})\,ds\Big)\,M\_{t}, |  |

where Mt:=𝔼[exp(−∫0Tr(s,Xs)ds)Δg(XT)|ℱt]\displaystyle M\_{t}:=\mathbb{E}\!\left[\exp\!\Big(-\!\int\_{0}^{T}r(s,X\_{s})\,ds\Big)\Delta g(X\_{T})\,\middle|\,\mathcal{F}\_{t}\right] is a square‑integrable
martingale.

Because 0≤r≤r¯\displaystyle 0\leq r\leq\bar{r}, we have
sup0≤t≤Texp⁡(∫0tr​(s,Xs)​𝑑s)≤er¯​T.\displaystyle\sup\_{0\leq t\leq T}\exp\!\big(\!\int\_{0}^{t}r(s,X\_{s})\,ds\big)\leq e^{\bar{r}T}.
Therefore

|  |  |  |
| --- | --- | --- |
|  | sup0≤t≤T|Δ​Yt|≤er¯​T​sup0≤t≤T|Mt|.\sup\_{0\leq t\leq T}|\Delta Y\_{t}|\leq e^{\bar{r}T}\,\sup\_{0\leq t\leq T}|M\_{t}|. |  |

Taking expectations and applying Doob’s inequality for martingales,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Δ​Yt|2]≤\displaystyle\displaystyle\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|\Delta Y\_{t}|^{2}\right]\leq | e2​r¯​T​𝔼​[sup0≤t≤T|Mt|2]\displaystyle\displaystyle e^{2\bar{r}T}\,\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|M\_{t}|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 4​e2​r¯​T​𝔼​[|MT|2]=4​e2​r¯​T​𝔼​[exp⁡(∫0T−2​r​(s,Xs)​d​s)​|Δ​g​(XT)|2].\displaystyle\displaystyle 4e^{2\bar{r}T}\,\mathbb{E}\!\left[|M\_{T}|^{2}\right]=4e^{2\bar{r}T}\,\mathbb{E}\!\left[\exp\!\Big(\!\int\_{0}^{T}-2r(s,X\_{s})\,ds\Big)\,|\Delta g(X\_{T})|^{2}\right]. |  |

Since r≥0\displaystyle r\geq 0, exp⁡(∫0T−2​r​(s,Xs)​d​s)≤1\displaystyle\exp\!\Big(\!\int\_{0}^{T}-2r(s,X\_{s})\,ds\Big)\leq 1 a.s., hence

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Δ​Yt|2]≤4​e2​r¯​T​𝔼​[|Δ​g​(XT)|2]≤4​e2​r¯​T​𝔼​[sup0≤t≤T|Δ​g​(t,Xt)|2].\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|\Delta Y\_{t}|^{2}\right]\leq 4e^{2\bar{r}T}\,\mathbb{E}\!\left[|\Delta g(X\_{T})|^{2}\right]\leq 4e^{2\bar{r}T}\,\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|\Delta g(t,X\_{t})|^{2}\right]. |  |

∎

Next we verify the tail probability Assumption [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"). According to
[[2](https://arxiv.org/html/2511.07235v1#bib.bib2)] and [[11](https://arxiv.org/html/2511.07235v1#bib.bib11)], we have the following estimate.

###### Proposition 5.2.

The solution Xt\displaystyle X\_{t} for
the equation ([5.7](https://arxiv.org/html/2511.07235v1#S5.E7 "In Theorem 5.1 (Lipschitz continuity of the European pricing operator in 𝑆²). ‣ 5.1 European option pricing ‣ 5 European Option Pricing Operator ‣ Deep Neural Operator Learning for Probabilistic Models"))
has the following tail probability,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(supt∈[0,T]|Xt−x0|≥r)≤exp⁡(−c​r2T),\displaystyle\displaystyle\mathbb{P}(\sup\_{t\in[0,T]}|X\_{t}-x\_{0}|\geq r)\leq\exp(-\frac{cr^{2}}{T}), |  | (5.8) |

for some constants c>0\displaystyle c>0, and r>0\displaystyle r>0.

###### Remark 5.3.

For SDEs driven by fractional Brownian motion, such estimates are proved in [[4](https://arxiv.org/html/2511.07235v1#bib.bib4)].
For rough differential equations, the corresponding estimates are established in [[16](https://arxiv.org/html/2511.07235v1#bib.bib16)].

## 6 Deep neural operator for American option pricing and PDE with free boundary

Given a Markov process Xt\displaystyle X\_{t} and exercise payoff g​(t,Xt)\displaystyle g(t,X\_{t}), the price of an American option is the value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(t,x)=supτ∈𝒯t,T𝔼ℚ​[exp⁡(−∫tτr​(s,Xs)​𝑑s)​g​(τ,Xτ)|Xt=x],u(t,x)=\sup\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int\_{t}^{\tau}r(s,X\_{s})\,ds\right)\,g(\tau,X\_{\tau})\Big|X\_{t}=x\right], |  | (6.1) |

where 𝒯t,T\displaystyle\mathcal{T}\_{t,T} is the set of stopping times with values in [t,T]\displaystyle[t,T]. Thanks to [[15](https://arxiv.org/html/2511.07235v1#bib.bib15)], the triple (Y,Z,K)\displaystyle(Y,Z,K) satisfies the *reflected backward SDE*:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Yt\displaystyle Y\_{t} | =g​(T,XT)−∫tTr​(s,Xs)​Ys​𝑑s+KT−Kt−∫tTZs​𝑑Ws,\displaystyle=g(T,X\_{T})-\int\_{t}^{T}r(s,X\_{s})Y\_{s}\,ds+K\_{T}-K\_{t}-\int\_{t}^{T}Z\_{s}\,dW\_{s}, |  | (6.2) |
|  | Yt\displaystyle Y\_{t} | ≥g​(t,Xt),∫0T(Ys−g​(s,Xs))​𝑑Ks=0,\displaystyle\geq g(t,X\_{t}),\quad\int\_{0}^{T}(Y\_{s}-g(s,X\_{s}))\,dK\_{s}=0, |  |

with (Y,Z,K)∈𝒮2×ℋ2×𝒜2\displaystyle(Y,Z,K)\in\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{A}^{2}. Here 𝒮2\displaystyle{\mathcal{S}}^{2} denotes square‑integrable adapted processes, ℋ2\displaystyle\mathcal{H}^{2} is
the predictable processes with square‑integrable norm, and 𝒜2\displaystyle\mathcal{A}^{2}
the increasing, adapted, square‑integrable processes vanishing at 0.

The price u​(t,x)\displaystyle u(t,x) can also be formulated using variational inequality. If u​(t,x)\displaystyle u(t,x) is sufficiently smooth, it satisfies the obstacle problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{∂tu+ℒ​u−r​u+c,g−u}=0,u​(T,x)=g​(T,x).\max\!\left\{\partial\_{t}u+\mathcal{L}u-ru+c,\,g-u\right\}=0,\qquad u(T,x)=g(T,x). |  | (6.3) |

Our resutls thus also provide a deep neural operator approximation for PDE with free boundary.
For the special case of Black–Scholes American Option, a single asset St\displaystyle S\_{t} under the dynamic,

|  |  |  |
| --- | --- | --- |
|  | d​Xt=Xt​(r​d​t+σ​d​Wt).dX\_{t}=X\_{t}(r\,dt+\sigma\,dW\_{t}). |  |

The corresponding PDE becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{∂tu+12​σ2​x2​ux​x+r​x​ux−r​u,g​(x)−u}=0,u​(T,x)=g​(x).\max\!\left\{\partial\_{t}u+\frac{1}{2}\sigma^{2}x^{2}u\_{xx}+rxu\_{x}-ru,\;g(x)-u\right\}=0,\qquad u(T,x)=g(x). |  | (6.4) |

In what follows, we denote by ΓA\displaystyle\Gamma^{A}
the American option pricing operator associated with ([6.1](https://arxiv.org/html/2511.07235v1#S6.E1 "In 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([6.2](https://arxiv.org/html/2511.07235v1#S6.E2 "In 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), equivalently the PDE free-boundary problem ([6.4](https://arxiv.org/html/2511.07235v1#S6.E4 "In 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")). We first show that ΓA\displaystyle\Gamma^{A} satisfies a Lipschitz condition.

###### Theorem 6.1.

Assume that 𝔼​[|sup0≤t≤Tg​(Xt)|2]<∞\displaystyle\mathbb{E}\Big[\Big|\sup\_{0\leq t\leq T}g(X\_{t})\Big|^{2}\Big]<\infty, then we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|ΓA​(g1)t−ΓA​(g2)t|2]≤LΓ​𝔼​[‖g1​(XT)−g2​(XT)‖2]+Cf,g1,g2​(𝔼​[|(g1−g2)T∗|2])1/2,\mathbb{E}\left[\sup\_{0\leq t\leq T}|\Gamma^{A}(g\_{1})\_{t}-\Gamma^{A}(g\_{2})\_{t}|^{2}\right]\leq L\_{\Gamma}\mathbb{E}\left[\|g\_{1}(X\_{T})-g\_{2}(X\_{T})\|^{2}\right]+C\_{f,g\_{1},g\_{2}}(\mathbb{E}\left[|(g\_{1}-g\_{2})^{\*}\_{T}|^{2}\right])^{1/2}, |  |

where we denote ΓA​(gi)t=Yti\displaystyle\Gamma^{A}(g\_{i})\_{t}=Y^{i}\_{t} as the solution for ([6.2](https://arxiv.org/html/2511.07235v1#S6.E2 "In 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) with terminal and boundary function gi\displaystyle g\_{i}.

###### Proof.

According to [[45](https://arxiv.org/html/2511.07235v1#bib.bib45)][Theorem 6.2.3] with same generator f​(Y,Z)=r​Y\displaystyle f(Y,Z)=rY in the BSDE ([6.2](https://arxiv.org/html/2511.07235v1#S6.E2 "In 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), we first have the following estimates,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|ΓA​(g1)t−ΓA​(g2)t|2]≤LΓ​𝔼​[‖g1​(XT)−g2​(XT)‖2]+C​(I1+I2)​𝔼​[(sup0≤t≤T|g1​(Xt)−g2​(Xt)|)2]1/2≤[LΓ+C​(I1+I2)]​(𝔼​[(sup0≤t≤T|g1​(Xt)−g2​(Xt)|)2])1/2,\begin{split}\mathbb{E}\left[\sup\_{0\leq t\leq T}|\Gamma^{A}(g\_{1})\_{t}-\Gamma^{A}(g\_{2})\_{t}|^{2}\right]&\leq L\_{\Gamma}\mathbb{E}[\|g\_{1}(X\_{T})-g\_{2}(X\_{T})\|^{2}]\\ &+C(I\_{1}+I\_{2})\mathbb{E}[(\sup\_{0\leq t\leq T}|g\_{1}(X\_{t})-g\_{2}(X\_{t})|)^{2}]^{1/2}\\ &\leq[L\_{\Gamma}+C(I\_{1}+I\_{2})](\mathbb{E}[(\sup\_{0\leq t\leq T}|g\_{1}(X\_{t})-g\_{2}(X\_{t})|)^{2}])^{1/2},\end{split} |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ii:=𝔼[|gi(XT)|2+(∫0T|fti(0,0)|dt)2+|(sup0≤t≤T(gi(Xt))+|2].I\_{i}:=\mathbb{E}[|g\_{i}(X\_{T})|^{2}+(\int\_{0}^{T}|f^{i}\_{t}(0,0)|dt)^{2}+|(\sup\_{0\leq t\leq T}(g\_{i}(X\_{t}))^{+}|^{2}]. |  | (6.5) |

Denote Cg1,g2\displaystyle C\_{g\_{1},g\_{2}} as the constant depending on g1,g2,LΓ,f\displaystyle g\_{1},g\_{2},L\_{\Gamma},f, we conclude the proof.
∎

### 6.1 Operator approximation for American option pricing operator

In this section, we generalize the operator approximation framework from Section [4](https://arxiv.org/html/2511.07235v1#S4 "4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models") to encompass a wider class of operators. The extension is based on a Lipschitz assumption motivated by Theorem [6.1](https://arxiv.org/html/2511.07235v1#S6.Thmtheorem1 "Theorem 6.1. ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models"), which naturally arises in the study of American option pricing problems, reflected FBSDEs, and PDEs with free boundary conditions.

###### Assumption 7.

Assume the operator

|  |  |  |
| --- | --- | --- |
|  | ΓA:𝒢⟶𝒰,g⟼u=ΓA​(g),\Gamma^{A}:\mathcal{G}\longrightarrow\mathcal{U},\qquad g\longmapsto u=\Gamma^{A}(g), |  |

from 𝒢\displaystyle\mathcal{G} to 𝒰\displaystyle\mathcal{U} is Lipschitz if : there exists LΓA\displaystyle L\_{\Gamma^{A}} such that for any g1,g2∈𝒢\displaystyle g\_{1},g\_{2}\in\mathcal{G}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sup0≤t≤T|ΓA​(g1)​(Xt)−ΓA​(g2)​(Xt)|2]\displaystyle\displaystyle\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|\Gamma^{A}(g\_{1})(X\_{t})-\Gamma^{A}(g\_{2})(X\_{t})|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | LΓA2​(𝔼​[sup0≤t≤T|g1​(Xt)−g2​(Xt)|2]+(𝔼​[sup0≤t≤T|g1​(Xt)−g2​(Xt)|2])1/2).\displaystyle\displaystyle L\_{\Gamma\_{A}}^{2}\left(\,\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|g\_{1}(X\_{t})-g\_{2}(X\_{t})|^{2}\right]+\left(\mathbb{E}\!\left[\sup\_{0\leq t\leq T}|g\_{1}(X\_{t})-g\_{2}(X\_{t})|^{2}\right]\right)^{1/2}\right). |  |

for all g1,g2∈𝒢\displaystyle g\_{1},g\_{2}\in\mathcal{G}.
Or equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ΓA​(g1)−ΓA​(g2)‖S22≤LΓA2​(‖g1−g2‖S2+‖g1−g2‖S22).\displaystyle\displaystyle\|\Gamma^{A}(g\_{1})-\Gamma^{A}(g\_{2})\|\_{S^{2}}^{2}\leq L\_{\Gamma\_{A}}^{2}(\|g\_{1}-g\_{2}\|\_{S^{2}}+\|g\_{1}-g\_{2}\|\_{S^{2}}^{2}). |  | (6.6) |

For notation simplicity, we denote ‖g1−g2‖S21,2:=‖g1−g2‖S2+‖g1−g2‖S22\displaystyle\|g\_{1}-g\_{2}\|\_{S^{2}}^{1,2}:=\|g\_{1}-g\_{2}\|\_{S^{2}}+\|g\_{1}-g\_{2}\|\_{S^{2}}^{2}.

We next prove the operator approximation under Assumption [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models").

###### Theorem 6.2.

[American Option Pricing Operator]
Let Assumptions [1](https://arxiv.org/html/2511.07235v1#Thmassumption1 "Assumption 1. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [2](https://arxiv.org/html/2511.07235v1#Thmassumption2 "Assumption 2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), [4](https://arxiv.org/html/2511.07235v1#Thmassumption4 "Assumption 4. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), and [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models") hold.
For any ε>0\displaystyle\varepsilon>0,
set N=O​(ε−2​d2)\displaystyle N=O\left(\varepsilon^{-2d\_{2}}\right), and Nδ=O​(ε−4​d1​d2−2​d1)\displaystyle N^{\delta}=O(\varepsilon^{-4d\_{1}d\_{2}-2d\_{1}}).
Define the network architecture ℱ1=ℱNN​(d2,1,L1,p1,K1,κ1,R1)\displaystyle\mathcal{F}\_{1}=\mathcal{F}\_{\rm NN}(d\_{2},1,L\_{1},p\_{1},K\_{1},\kappa\_{1},R\_{1}) and ℱ2=ℱNN​(Nδ,1,L2,p2,K2,κ2,R2)\displaystyle\mathcal{F}\_{2}=\mathcal{F}\_{\rm NN}(N^{\delta},1,L\_{2},p\_{2},K\_{2},\kappa\_{2},R\_{2}) with

|  |  |  |
| --- | --- | --- |
|  | ℒ1=O​((12​d2+2​d22)​log⁡(ε1−2)),𝔭1=O​(1),K1=O​((12​d2+2​d22)​log⁡(ε1−2)),κ1=O​(ε1−2​d2),R1=1.\displaystyle\displaystyle\mathcal{L}\_{1}=O\left((\frac{1}{2}d\_{2}+2d\_{2}^{2})\log(\varepsilon\_{1}^{-2})\right),\mathfrak{p}\_{1}=O(1),\ K\_{1}=O\left((\frac{1}{2}d\_{2}+2d\_{2}^{2})\log(\varepsilon\_{1}^{-2})\right),\kappa\_{1}=O\left(\varepsilon\_{1}^{-2d\_{2}}\right),R\_{1}=1. |  |

and,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2\displaystyle\displaystyle\mathcal{L}\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε−(2​d2+1)+Nδ​log⁡(r~)),𝔭2=O​(ε2−(4​d1−2)​Nδ),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon^{-(2d\_{2}+1)}+N^{\delta}\log(\widetilde{r})\right),\mathfrak{p}\_{2}=O(\varepsilon\_{2}^{-(4d\_{1}-2)N^{\delta}}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K2\displaystyle\displaystyle K\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε−2​(d2+1)+Nδ​log⁡(r~)),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon^{-2(d\_{2}+1)}+N^{\delta}\log(\widetilde{r})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | κ2\displaystyle\displaystyle\kappa\_{2} | =O​(ε−Nδ​(2​d2+1)),R2=1,\displaystyle\displaystyle=O(\varepsilon^{-N^{\delta}(2d\_{2}+1)}),R\_{2}=1, |  |

where r~\displaystyle\widetilde{r} is a constant.
For any operator ΓA:𝒢→𝒰\displaystyle\Gamma^{A}:\mathcal{G}\rightarrow\mathcal{U} satisfying Assumption [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models"), there are {q~k}k=1N1\displaystyle\{\widetilde{q}\_{k}\}\_{k=1}^{N\_{1}} with q~k∈ℱ1\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{1} and {a~k}k=1N1\displaystyle\{\widetilde{a}\_{k}\}\_{k=1}^{N\_{1}} with a~k∈ℱ2\displaystyle\widetilde{a}\_{k}\in\mathcal{F}\_{2} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supg∈𝒢𝔼​[sup0≤t≤T|ΓA​(g)​(Xt)−∑k=1N1a~k​(𝒈)​q~k​(Xt)|]≤ε.\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq t\leq T}\left|\Gamma^{A}(g)(X\_{t})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{t})\right|\bigg]\leq\varepsilon. |  | (6.7) |

###### Proof of Theorem [6.2](https://arxiv.org/html/2511.07235v1#S6.Thmtheorem2 "Theorem 6.2. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models").

We reproduce the function, functional and operator approximation under the new Assumption [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models").

Step 1 (function approximation): We first prove the function approximation under Assumption [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models") which is the building block for the rest of the proof. Following the proof of Theorem [4.1](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"), the only difference is that we need to estimate ℐ2\displaystyle\mathcal{I}\_{2} in the proof of Theorem [4.1](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"), which now has the following form due to the new Assumption [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models").
In specific, the function approximation for the function ΓA​(g)\displaystyle\Gamma^{A}(g) following the proof of Theorem [4.1](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models") has the following form,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sup0≤t≤T|ΓA​(g)​(Xt)−∑k=1Nd2ΓA​(g)​(𝐜k)​ϕ𝐜k​(Xt)|2]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|\Gamma^{A}(g)(X\_{t})-\sum\_{k=1}^{N^{d\_{2}}}\Gamma^{A}(g)(\mathbf{c}\_{k})\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big|^{2}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[sup0≤t≤T|ΓA​(g)​(Xt)|2​𝟏ΩrC​(Xt)]⏟ℐ1A+𝔼​[sup0≤t≤T|ΓA​(g)​(Xt)−∑k=1Nd2ΓA​(g)​(𝐜k)​ϕ𝐜k​(Xt)|2​𝟏Ωr​(Xt)]⏟ℐ2A.\displaystyle\displaystyle\underbrace{\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|\Gamma^{A}(g)(X\_{t})\Big|^{2}\mathbf{1}\_{\Omega\_{r}^{C}}(X\_{t})\Big]}\_{\mathcal{I}\_{1}^{A}}+\underbrace{\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|\Gamma^{A}(g)(X\_{t})-\sum\_{k=1}^{N^{d\_{2}}}\Gamma^{A}(g)(\mathbf{c}\_{k})\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big]}\_{\mathcal{I}\_{2}^{A}}. |  |

The estimate of ℐ1A\displaystyle\mathcal{I}\_{1}^{A} follows the same as in ([4.4](https://arxiv.org/html/2511.07235v1#S4.E4 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")). For the second term ℐ2A\displaystyle\mathcal{I}\_{2}^{A}, reproducing the estimates in ([4.5](https://arxiv.org/html/2511.07235v1#S4.E5 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")) under Assumption [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models") for the function ΓA​(g)∈𝒰\displaystyle\Gamma^{A}(g)\in\mathcal{U}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ2A=\displaystyle\displaystyle\mathcal{I}\_{2}^{A}= | 𝔼​[sup0≤t≤T|∑k=1Nd2[ΓA​(g)​(Xt)−ΓA​(g)​(𝐜k)]​ϕ𝐜k​(Xt)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big|\sum\_{k=1}^{N^{d\_{2}}}[\Gamma^{A}(g)(X\_{t})-\Gamma^{A}(g)(\mathbf{c}\_{k})]\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤T(∑k=1Nd2|ΓA​(g)​(Xt)−ΓA​(g)​(𝐜k)|​|ϕ𝐜k​(Xt)|)2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big(\sum\_{k=1}^{N^{d\_{2}}}|\Gamma^{A}(g)(X\_{t})-\Gamma^{A}(g)(\mathbf{c}\_{k})||\phi\_{\mathbf{c}\_{k}}(X\_{t})|\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[sup0≤t≤T(∑k:‖𝐜k−Xt‖∞≤2​r(N−1)|ΓA​(g)​(Xt)−ΓA​(g)​(𝐜k)|​ϕ𝐜k​(Xt))2​𝟏Ωr​(Xt)],\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big(\sum\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|\Gamma^{A}(g)(X\_{t})-\Gamma^{A}(g)(\mathbf{c}\_{k})|\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤T(maxk:‖𝐜k−Xt‖∞≤2​r(N−1)⁡|ΓA​(g)​(Xt)−ΓA​(g)​(𝐜k)|​(∑k:‖𝐜k−Xt‖∞≤2​r(N−1)ϕ𝐜k​(Xt)))2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\Big(\max\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|\Gamma^{A}(g)(X\_{t})-\Gamma^{A}(g)(\mathbf{c}\_{k})|\Big(\sum\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}\phi\_{\mathbf{c}\_{k}}(X\_{t})\Big)\Big)^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤Tmaxk:‖𝐜k−Xt‖∞≤2​r(N−1)⁡|ΓA​(g)​(Xt)−ΓA​(g)​(𝐜k)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\max\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|\Gamma^{A}(g)(X\_{t})-\Gamma^{A}(g)(\mathbf{c}\_{k})|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤t≤Tmaxk:‖𝐜k−Xt‖∞≤2​r(N−1)⁡|ΓA​(g)​(Xt)−ΓA​(g)​(𝐜k)|2​𝟏Ωr​(Xt)]\displaystyle\displaystyle\mathbb{E}\Big[\sup\_{0\leq t\leq T}\max\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|\Gamma^{A}(g)(X\_{t})-\Gamma^{A}(g)(\mathbf{c}\_{k})|^{2}\mathbf{1}\_{\Omega\_{r}}(X\_{t})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | LΓA2(𝔼[sup0≤t≤Tmaxk:‖𝐜k−Xt‖∞≤2​r(N−1)|g(Xt)−g(𝐜k)|2]\displaystyle\displaystyle L\_{\Gamma^{A}}^{2}\left(\,\mathbb{E}\!\left[\sup\_{0\leq t\leq T}\max\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|g(X\_{t})-g(\mathbf{c}\_{k})|^{2}\right]\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(𝔼[sup0≤t≤Tmaxk:‖𝐜k−Xt‖∞≤2​r(N−1)|g(Xt)−g(𝐜k)|2])1/2)\displaystyle\displaystyle\quad\left.+\left(\mathbb{E}\!\left[\sup\_{0\leq t\leq T}\max\_{k:\|\mathbf{c}\_{k}-X\_{t}\|\_{\infty}\leq\frac{2r}{(N-1)}}|g(X\_{t})-g(\mathbf{c}\_{k})|^{2}\right]\right)^{1/2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | LΓA2​((2​r​Lg)2​d2(N−1)2+((2​r​Lg)2​d2(N−1)2)1/2)\displaystyle\displaystyle L\_{\Gamma^{A}}^{2}\left(\frac{(2rL\_{g})^{2}d\_{2}}{(N-1)^{2}}+\left(\frac{(2rL\_{g})^{2}d\_{2}}{(N-1)^{2}}\right)^{1/2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | C​LΓA2​2​r​Lg​d21/2(N−1)≤14×ε124,\displaystyle\displaystyle CL\_{\Gamma^{A}}^{2}\frac{2rL\_{g}d\_{2}^{1/2}}{(N-1)}\leq\frac{1}{4}\times\frac{\varepsilon\_{1}^{2}}{4}, |  | (6.8) |

where we use the Lipschitz assumption of ΓA\displaystyle\Gamma^{A} from Assumption ([7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), and ((2​r​Lg)2​d2(N−1)2)1/2\displaystyle\left(\frac{(2rL\_{g})^{2}d\_{2}}{(N-1)^{2}}\right)^{1/2} is the dominating term since (2​r​Lg)2​d2(N−1)2<1\displaystyle\frac{(2rL\_{g})^{2}d\_{2}}{(N-1)^{2}}<1 by choosing ε1\displaystyle\varepsilon\_{1} to be sufficiently small. Following the same idea and estimate in ([4.6](https://arxiv.org/html/2511.07235v1#S4.E6 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), in order to get the desired estimate in ([6.11](https://arxiv.org/html/2511.07235v1#S6.E11 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), we make the following selection.

Up to a constant c\displaystyle c change, for ε1>0\displaystyle\varepsilon\_{1}>0 which will be specified,
set r=⌈−2​CTc​log⁡ε1216​C0⌉1α\displaystyle r=\left\lceil-\frac{2C\_{T}}{c}\log\frac{\varepsilon\_{1}^{2}}{16C\_{0}}\right\rceil^{\frac{1}{\alpha}}, and define Qr,Ωr\displaystyle Q\_{r},\Omega\_{r} as in Definition [2.2](https://arxiv.org/html/2511.07235v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"),
there exists a constant N=O​(r​Lg​d112​ε1−2)\displaystyle N=O\left(rL\_{g}d\_{1}^{\frac{1}{2}}\varepsilon\_{1}^{-2}\right) following from the designed estiamtes in ([6.8](https://arxiv.org/html/2511.07235v1#S6.E8 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), for some constant C\displaystyle C depending on d2,Lg\displaystyle d\_{2},L\_{g} and r\displaystyle r, a network architecture ℱ1=ℱNN​(d2,1,ℒ1,𝔭1,K1,κ1,R1)\displaystyle\mathcal{F}\_{1}=\mathcal{F}\_{\rm NN}(d\_{2},1,\mathcal{L}\_{1},\mathfrak{p}\_{1},K\_{1},\kappa\_{1},R\_{1}) and {q~k}k=1N1\displaystyle\{\widetilde{q}\_{k}\}\_{k=1}^{N\_{1}} with q~k∈ℱ1\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{1}, and {𝐜k}k=1N1⊂Qr\displaystyle\{\mathbf{c}\_{k}\}\_{k=1}^{N\_{1}}\subset Q\_{r} such that for any g∈𝒢\displaystyle g\in\mathcal{G},
we separate the estimates into the following two parts,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔼​[sup0≤t≤T|ΓA​(g)​(Xt)−∑k=1N1ΓA​(g)​(𝐜k)​q~k​(Xt)|2])1/2≤ε1/2.\displaystyle\displaystyle\left(\mathbb{E}\bigg[\sup\_{0\leq t\leq T}\left|\Gamma^{A}(g)(X\_{t})-\sum\_{k=1}^{N\_{1}}\Gamma^{A}(g)(\mathbf{c}\_{k})\widetilde{q}\_{k}(X\_{t})\right|^{2}\bigg]\right)^{1/2}\leq\varepsilon\_{1}/2. |  | (6.9) |

For the ease of the notation, we denote N1=C​Nd2\displaystyle N\_{1}=CN^{d\_{2}} for some constant C\displaystyle C.
Since ε1/2<1\displaystyle\varepsilon\_{1}/2<1, this further implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|ΓA​(g)​(Xt)−∑k=1N1ΓA​(g)​(𝐜k)​q~k​(Xt)|2]≤ε12/4≤ε1/2.\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq t\leq T}\left|\Gamma^{A}(g)(X\_{t})-\sum\_{k=1}^{N\_{1}}\Gamma^{A}(g)(\mathbf{c}\_{k})\widetilde{q}\_{k}(X\_{t})\right|^{2}\bigg]\leq\varepsilon\_{1}^{2}/4\leq\varepsilon\_{1}/2. |  | (6.10) |

Combining the above two estimates, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ΓA​(g)−∑k=1N1ΓA​(g)​(𝐜k)​q~k‖𝒮21,2≤ε1.\displaystyle\displaystyle\|\Gamma^{A}(g)-\sum\_{k=1}^{N\_{1}}\Gamma^{A}(g)(\mathbf{c}\_{k})\widetilde{q}\_{k}\|\_{\mathcal{S}\_{2}}^{1,2}\leq\varepsilon\_{1}. |  | (6.11) |

According to Theorem [4.1](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"), and the relations between ([6.9](https://arxiv.org/html/2511.07235v1#S6.E9 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([6.10](https://arxiv.org/html/2511.07235v1#S6.E10 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), the network size ℱ1\displaystyle\mathcal{F}\_{1} will be determined by the estimate in ([6.10](https://arxiv.org/html/2511.07235v1#S6.E10 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")).
Since the Lipschitz assumption is not used in ([4.9](https://arxiv.org/html/2511.07235v1#S4.E9 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), following the same estimate in ([4.9](https://arxiv.org/html/2511.07235v1#S4.E9 "In 4.1 Function Approximation ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")) and r=O​((log⁡(ε1−2))1α),N=O​(r​Lg​d112​ε1−2)\displaystyle r=O\left((\log(\varepsilon\_{1}^{-2}))^{\frac{1}{\alpha}}\right),N=O\left(rL\_{g}d\_{1}^{\frac{1}{2}}\varepsilon\_{1}^{-2}\right) estimates,
we have δ=O​(d1−d22−1​ε112+2​d2​(log⁡ε1−2)−p+d2α)\displaystyle\delta=O\left(d\_{1}^{-\frac{d\_{2}}{2}-1}\varepsilon\_{1}^{\frac{1}{2}+2d\_{2}}(\log\varepsilon\_{1}^{-2})^{-\frac{p+d\_{2}}{\alpha}}\right).
Such a network has size,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ1\displaystyle\displaystyle\mathcal{L}\_{1} | =O​((12​d2+2​d22)​log⁡(ε1−2)),𝔭1=O​(1),K1=O​((12​d2+2​d22)​log⁡(ε1−2)),\displaystyle\displaystyle=O\left((\frac{1}{2}d\_{2}+2d\_{2}^{2})\log(\varepsilon\_{1}^{-2})\right),\mathfrak{p}\_{1}=O(1),\ K\_{1}=O\left((\frac{1}{2}d\_{2}+2d\_{2}^{2})\log(\varepsilon\_{1}^{-2})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | κ1\displaystyle\displaystyle\kappa\_{1} | =O​(ε1−2​d2),R1=1.\displaystyle\displaystyle=O\left(\varepsilon\_{1}^{-2d\_{2}}\right),R\_{1}=1. |  |

Step 2 (functional approximation): For each k\displaystyle k, define the functional induced by the operator ΓA\displaystyle\Gamma^{A} as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖥k​(ΓA​(g))=ΓA​(g)​(𝐜k).\displaystyle\displaystyle\mathsf{F}\_{k}(\Gamma^{A}(g))=\Gamma^{A}(g)(\mathbf{c}\_{k}). |  | (6.12) |

For any g1,g2∈𝒢\displaystyle g\_{1},g\_{2}\in\mathcal{G}, and the forward process at t\displaystyle t starts at 𝐜k\displaystyle\mathbf{c}\_{k}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |𝖥k​(ΓA​(g1))−𝖥k​(ΓA​(g2))|2\displaystyle\displaystyle|\mathsf{F}\_{k}(\Gamma^{A}(g\_{1}))-\mathsf{F}\_{k}(\Gamma^{A}(g\_{2}))|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | 𝔼​[sup0≤s≤T|ΓA​(g1)​(Xs)−ΓA​(g2)​(Xs)|2]\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq s\leq T}|\Gamma^{A}(g\_{1})(X\_{s})-\Gamma^{A}(g\_{2})(X\_{s})|^{2}\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | LΓA2​(𝔼​[sup0≤s≤T|g1​(Xs)−g2​(Xs)|2]+(𝔼​[sup0≤s≤T|g1​(Xs)−g2​(Xs)|2])1/2)\displaystyle\displaystyle L\_{\Gamma^{A}}^{2}\left(\mathbb{E}\bigg[\sup\_{0\leq s\leq T}|g\_{1}(X\_{s})-g\_{2}(X\_{s})|^{2}\bigg]+\left(\mathbb{E}\bigg[\sup\_{0\leq s\leq T}|g\_{1}(X\_{s})-g\_{2}(X\_{s})|^{2}\bigg]\right)^{1/2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | LΓA2​‖g1−g2‖S21,2,\displaystyle\displaystyle L\_{\Gamma^{A}}^{2}\|g\_{1}-g\_{2}\|\_{S^{2}}^{1,2}, |  | (6.13) |

where the last inequality follows from Assumption [7](https://arxiv.org/html/2511.07235v1#Thmassumption7 "Assumption 7. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models").
Recall the function gw​(x)\displaystyle g\_{w}(x) defined in ([4.11](https://arxiv.org/html/2511.07235v1#S4.E11 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")),
for the functional 𝖥\displaystyle\mathsf{F} induced by the American option pricing operator ΓA\displaystyle\Gamma^{A}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝖥​(g)−𝖥​(gw)|2\displaystyle\displaystyle\bigl|\mathsf{F}(g)-\mathsf{F}(g\_{w})\bigr|^{2} | ≤LΓA2​‖g−gw‖S21,2\displaystyle\displaystyle\leq L\_{\Gamma^{A}}^{2}\,\|g-g\_{w}\|\_{S^{2}}^{1,2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤LΓA2​‖g−gw‖S22+LΓA​‖g−gw‖S21,\displaystyle\displaystyle\leq L\_{\Gamma^{A}}^{2}\,\|g-g\_{w}\|\_{S^{2}}^{2}+L\_{\Gamma^{A}}\,\|g-g\_{w}\|\_{S^{2}}^{1}, |  |

which is equivalent to

|  |  |  |
| --- | --- | --- |
|  | |𝖥​(g)−𝖥​(gw)|≤(LΓA2​‖g−gw‖S22+LΓA​‖g−gw‖S21)1/2,\displaystyle\displaystyle\bigl|\mathsf{F}(g)-\mathsf{F}(g\_{w})\bigr|\leq(L\_{\Gamma^{A}}^{2}\,\|g-g\_{w}\|\_{S^{2}}^{2}+L\_{\Gamma^{A}}\,\|g-g\_{w}\|\_{S^{2}}^{1})^{1/2}, |  |

where we assume that ΓA2≤ΓA\displaystyle\Gamma\_{A}^{2}\leq\Gamma\_{A} to ease the computation which, up to a constant change, does not change the order of the radius size. (Similarly, ΓA≤ΓA2\displaystyle\Gamma\_{A}\leq\Gamma\_{A}^{2} implies similar computations).
Following the idea to the derivation of ([6.11](https://arxiv.org/html/2511.07235v1#S6.E11 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) from ([6.9](https://arxiv.org/html/2511.07235v1#S6.E9 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([6.10](https://arxiv.org/html/2511.07235v1#S6.E10 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), up to a constant, for any ε2>0\displaystyle\varepsilon\_{2}>0, we can pick r\displaystyle r such that LΓA2​‖g−gw‖S22≤ε2464≤ε228\displaystyle L\_{\Gamma\_{A}}^{2}\,\|g-g\_{w}\|\_{S^{2}}^{2}\leq\frac{\varepsilon\_{2}^{4}}{64}\leq\frac{\varepsilon\_{2}^{2}}{8}, which thus implies LΓA​‖g−gw‖S21≤ε228\displaystyle L\_{\Gamma^{A}}\|g-g\_{w}\|\_{S^{2}}^{1}\leq\frac{\varepsilon\_{2}^{2}}{8}, and the following estimate

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |𝖥​(g)−𝖥​(gw)|\displaystyle\displaystyle\bigl|\mathsf{F}(g)-\mathsf{F}(g\_{w})\bigr| | ≤(ε228+ε228)1/2≤ε2/2.\displaystyle\displaystyle\leq(\frac{\varepsilon\_{2}^{2}}{8}+\frac{\varepsilon\_{2}^{2}}{8})^{1/2}\leq\varepsilon\_{2}/2. |  | (6.14) |

Thus, LΓA2​‖g−gw‖S22≤ε2464\displaystyle L\_{\Gamma\_{A}}^{2}\,\|g-g\_{w}\|\_{S^{2}}^{2}\leq\frac{\varepsilon\_{2}^{4}}{64} determines the following parameters, following ([4.13](https://arxiv.org/html/2511.07235v1#S4.E13 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), ([4.14](https://arxiv.org/html/2511.07235v1#S4.E14 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([4.15](https://arxiv.org/html/2511.07235v1#S4.E15 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | r2=⌈−2​CTc​log⁡ε24128​C0​L𝖥2⌉1α+1,δ2=C​ε228​2​L𝖥​Lg​d112,\displaystyle\displaystyle r\_{2}=\left\lceil-\frac{2C\_{T}}{c}\log\frac{\varepsilon\_{2}^{4}}{128C\_{0}L\_{\mathsf{F}}^{2}}\right\rceil^{\frac{1}{\alpha}}+1,\quad\delta\_{2}=\frac{C\varepsilon\_{2}^{2}}{8\sqrt{2}L\_{\mathsf{F}}L\_{g}d\_{1}^{\frac{1}{2}}}, |  | (6.15) |

where C\displaystyle C is a constant.
Now, for any g,g~∈𝒢\displaystyle g,\widetilde{g}\in\mathcal{G}, define gw\displaystyle g\_{w} and g~w\displaystyle\widetilde{g}\_{w} as in ([4.11](https://arxiv.org/html/2511.07235v1#S4.E11 "In 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models")), and set

|  |  |  |
| --- | --- | --- |
|  | 𝒈=[g​(c1),…,g​(cNδ)]𝖳,𝒈~=[g~​(c1),…,g~​(cNδ)]𝖳.\bm{g}=\bigl[g(c\_{1}),\ldots,g(c\_{N^{\delta}})\bigr]^{\mathsf{T}},\qquad\widetilde{\bm{g}}=\bigl[\widetilde{g}(c\_{1}),\ldots,\widetilde{g}(c\_{N^{\delta}})\bigr]^{\mathsf{T}}. |  |

Define the function h​(𝒈):=𝖥​(gw)\displaystyle h(\bm{g}):=\mathsf{F}(g\_{w}). According to ([6.12](https://arxiv.org/html/2511.07235v1#S6.E12 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([6.1](https://arxiv.org/html/2511.07235v1#S6.Ex26 "6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h​(𝒈)−h​(𝒈~)|2\displaystyle\displaystyle|h(\bm{g})-h(\widetilde{\bm{g}})|^{2} | =|𝖥​(gw)−𝖥​(g~w)|2\displaystyle\displaystyle=\bigl|\mathsf{F}(g\_{w})-\mathsf{F}(\widetilde{g}\_{w})\bigr|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤LΓA2​‖gw−g~w‖S21,2\displaystyle\displaystyle\leq L\_{\Gamma\_{A}}^{2}\,\|g\_{w}-\widetilde{g}\_{w}\|\_{S^{2}}^{1,2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =LΓA2​𝔼​[supt≤s≤T(∑k=1Nδ(g​(ck)−g~​(ck))​wk​(Xs))2]\displaystyle\displaystyle=L\_{\Gamma\_{A}}^{2}\,\mathbb{E}\!\left[\sup\_{t\leq s\leq T}\!\!\Bigl(\sum\_{k=1}^{N^{\delta}}\bigl(g(c\_{k})-\widetilde{g}(c\_{k})\bigr)\,w\_{k}(X\_{s})\Bigr)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +LΓA2​(𝔼​[supt≤s≤T(∑k=1Nδ(g​(ck)−g~​(ck))​wk​(Xs))2])1/2\displaystyle\displaystyle+L\_{\Gamma\_{A}}^{2}\,\left(\mathbb{E}\!\left[\sup\_{t\leq s\leq T}\!\!\Bigl(\sum\_{k=1}^{N^{\delta}}\bigl(g(c\_{k})-\widetilde{g}(c\_{k})\bigr)\,w\_{k}(X\_{s})\Bigr)^{2}\right]\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤LΓA2​(∑k=1Nδ|g​(ck)−g~​(ck)|2)​𝔼​[supt≤s≤T∑k=1Nδwk​(Xs)2]\displaystyle\displaystyle\leq L\_{\Gamma\_{A}}^{2}\,\Bigl(\sum\_{k=1}^{N^{\delta}}|g(c\_{k})-\widetilde{g}(c\_{k})|^{2}\Bigr)\,\mathbb{E}\!\left[\sup\_{t\leq s\leq T}\sum\_{k=1}^{N^{\delta}}w\_{k}(X\_{s})^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +LΓA2​(∑k=1Nδ|g​(ck)−g~​(ck)|2)1/2​𝔼​[supt≤s≤T∑k=1Nδwk​(Xs)2]1/2\displaystyle\displaystyle+L\_{\Gamma\_{A}}^{2}\,\Bigl(\sum\_{k=1}^{N^{\delta}}|g(c\_{k})-\widetilde{g}(c\_{k})|^{2}\Bigr)^{1/2}\,\mathbb{E}\!\left[\sup\_{t\leq s\leq T}\sum\_{k=1}^{N^{\delta}}w\_{k}(X\_{s})^{2}\right]^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤LΓA2​(∑k=1Nδ|g​(ck)−g~​(ck)|2+(∑k=1Nδ|g​(ck)−g~​(ck)|2)1/2)\displaystyle\displaystyle\leq L\_{\Gamma\_{A}}^{2}\,\,\Bigl(\sum\_{k=1}^{N^{\delta}}|g(c\_{k})-\widetilde{g}(c\_{k})|^{2}+\left(\sum\_{k=1}^{N^{\delta}}|g(c\_{k})-\widetilde{g}(c\_{k})|^{2}\right)^{1/2}\Bigr) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤LΓA2​(|𝒈−𝒈~|2+|𝒈−𝒈~|),\displaystyle\displaystyle\leq L\_{\Gamma\_{A}}^{2}(|\bm{g}-\widetilde{\bm{g}}|^{2}+|\bm{g}-\widetilde{\bm{g}}|), |  | (6.16) |

which is equivalent to

|  |  |  |
| --- | --- | --- |
|  | |h​(𝒈)−h​(𝒈~)|≤LΓA​(|𝒈−𝒈~|2+|𝒈−𝒈~|)1/2.\displaystyle\displaystyle|h(\bm{g})-h(\widetilde{\bm{g}})|\leq L\_{\Gamma\_{A}}(|\bm{g}-\widetilde{\bm{g}}|^{2}+|\bm{g}-\widetilde{\bm{g}}|)^{1/2}. |  |

By Assumption [3](https://arxiv.org/html/2511.07235v1#Thmassumption3 "Assumption 3. ‣ 2 Assumptions ‣ Deep Neural Operator Learning for Probabilistic Models"), we have the bound of function g\displaystyle g on Qr\displaystyle Q\_{r} as below,

|  |  |  |
| --- | --- | --- |
|  | g​(x)≤Cg​(1+|x|p)≤Cg​(1+|r2|p):=r~,x∈Qr2.g(x)\leq C\_{g}(1+|x|^{p})\leq C\_{g}(1+|r\_{2}|^{p}):=\widetilde{r},\quad x\in Q\_{r\_{2}}. |  |

Similarly, according to our definition in ([6.12](https://arxiv.org/html/2511.07235v1#S6.E12 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), h\displaystyle h is also bounded above. Applying Lemma [6.3](https://arxiv.org/html/2511.07235v1#S6.Thmtheorem3 "Lemma 6.3. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models") (which is proved below), we claim that for 12​ε2>0\displaystyle\frac{1}{2}\varepsilon\_{2}>0
the function (functional) h​(𝒈)=𝖥​(gw)\displaystyle h(\bm{g})=\mathsf{F}(g\_{w}) can be approximated by a network ℱ2=ℱNN​(Nδ,1,ℒ2,𝔭2,K2,κ2,R2)\displaystyle\mathcal{F}\_{2}=\mathcal{F}\_{\rm NN}(N^{\delta},1,\mathcal{L}\_{2},\mathfrak{p}\_{2},K\_{2},\kappa\_{2},R\_{2}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2\displaystyle\displaystyle\mathcal{L}\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε2−1+Nδ​log⁡(r~)),𝔭2=O​(1),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon\_{2}^{-1}+N^{\delta}\log(\widetilde{r})\right),\mathfrak{p}\_{2}=O(1), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K2\displaystyle\displaystyle K\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε2−1+Nδ​log⁡(r~)),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon\_{2}^{-1}+N^{\delta}\log(\widetilde{r})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | κ2\displaystyle\displaystyle\kappa\_{2} | =O​(ε2−Nδ),R2=1.\displaystyle\displaystyle=O(\varepsilon\_{2}^{-N^{\delta}}),R\_{2}=1. |  |

That is

|  |  |  |  |
| --- | --- | --- | --- |
|  | supg∈U|𝖥​(gw)−∑k=1N2h​(𝒈k)​q~k|≤12​ε2,\displaystyle\displaystyle\sup\_{g\in U}\left|\mathsf{F}(g\_{w})-\sum\_{k=1}^{N\_{2}}h({\bm{g}}\_{k})\widetilde{q}\_{k}\right|\leq\frac{1}{2}\varepsilon\_{2}, |  | (6.17) |

where N2=NNδ\displaystyle N\_{2}=N^{N^{\delta}}, with N=O​(Nδ​ε2−2)\displaystyle N=O(\sqrt{N^{\delta}}\varepsilon\_{2}^{-2}).
Combining the above estimates in ([6.14](https://arxiv.org/html/2511.07235v1#S6.E14 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([6.17](https://arxiv.org/html/2511.07235v1#S6.E17 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), such a network architecture gives a network a~k\displaystyle\widetilde{a}\_{k} so that

|  |  |  |
| --- | --- | --- |
|  | supg|𝖥k​(Γ​(g))−a~k​(𝒈)|≤ε2.\displaystyle\displaystyle\sup\_{g}|\mathsf{F}\_{k}(\Gamma(g))-\widetilde{a}\_{k}(\bm{g})|\leq\varepsilon\_{2}. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sup0≤s≤T|∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | 𝔼​[sup0≤s≤T|∑k=1N1(𝖥k​(Γ​g)−a~k​(𝒈))​q~k​(Xs)|]\displaystyle\displaystyle\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\left(\mathsf{F}\_{k}(\Gamma g)-\widetilde{a}\_{k}(\bm{g})\right)\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | ∑k=1N1sup𝒈|𝖥k​(Γ​g)−a~k​(𝒈)|=N1​ε2.\displaystyle\displaystyle\sum\_{k=1}^{N\_{1}}\sup\_{\bm{g}}|\mathsf{F}\_{k}(\Gamma g)-\widetilde{a}\_{k}(\bm{g})|=N\_{1}\varepsilon\_{2}. |  | (6.18) |

Step 3 (American pricing operator approximation):
Applying the Cauchy–Schwarz inequality, using ([6.11](https://arxiv.org/html/2511.07235v1#S6.E11 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) and ([6.18](https://arxiv.org/html/2511.07235v1#S6.E18 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | supg∈𝒢𝔼​[sup0≤s≤T|ΓA​g​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma^{A}g(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | supg∈𝒢𝔼​[sup0≤s≤T|ΓA​(g)​(Xs)−∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)|]\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma^{A}(g)(X\_{s})-\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +supg∈𝒢𝔼​[sup0≤s≤T|∑k=1N1𝖥k​(ΓA​g)​q~k​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle+\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma^{A}g)\widetilde{q}\_{k}(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | supg∈𝒢𝔼​[sup0≤s≤T|ΓA​(g)​(Xs)−∑k=1N1𝖥k​(ΓA​g)​q~k​(Xs)|2]1/2\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma^{A}(g)(X\_{s})-\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma^{A}g)\widetilde{q}\_{k}(X\_{s})\right|^{2}\bigg]^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +supg∈𝒢𝔼​[sup0≤s≤T|∑k=1N1𝖥k​(ΓA​g)​q~k​(Xs)−∑k=1Na~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle+\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma^{A}g)\widetilde{q}\_{k}(X\_{s})-\sum\_{k=1}^{N}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | supg∈𝒢‖ΓA​(g)−∑k=1N1ΓA​(g)​(𝐜k)​q~k‖𝒮21,2+supg∈𝒢𝔼​[sup0≤s≤T|∑k=1N1𝖥k​(Γ​g)​q~k​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\|\Gamma^{A}(g)-\sum\_{k=1}^{N\_{1}}\Gamma^{A}(g)(\mathbf{c}\_{k})\widetilde{q}\_{k}\|\_{\mathcal{S}\_{2}}^{1,2}+\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\sum\_{k=1}^{N\_{1}}\mathsf{F}\_{k}(\Gamma g)\widetilde{q}\_{k}(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | ε1+N1​ε2.\displaystyle\displaystyle\varepsilon\_{1}+N\_{1}\varepsilon\_{2}. |  |

Set ε2=ε1/(2​N1),ε1=ε2\displaystyle\varepsilon\_{2}=\varepsilon\_{1}/(2N\_{1}),\varepsilon\_{1}=\frac{\varepsilon}{2},
or ε2=O​(ε2​d2+1​(log⁡ε−2)−d2α​d1−d22)\displaystyle\varepsilon\_{2}=O\left(\varepsilon^{2d\_{2}+1}(\log\varepsilon^{-2})^{-\frac{d\_{2}}{\alpha}}d\_{1}^{-\frac{d\_{2}}{2}}\right),
we then have

|  |  |  |
| --- | --- | --- |
|  | supg∈𝒢𝔼​[sup0≤s≤T|ΓA​g​(Xs)−∑k=1N1a~k​(𝒈)​q~k​(Xs)|]≤ε.\displaystyle\displaystyle\sup\_{g\in\mathcal{G}}\mathbb{E}\bigg[\sup\_{0\leq s\leq T}\left|\Gamma^{A}g(X\_{s})-\sum\_{k=1}^{N\_{1}}\widetilde{a}\_{k}(\bm{g})\widetilde{q}\_{k}(X\_{s})\right|\bigg]\leq\varepsilon. |  |

Consequently, the network size is estimated to be,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2\displaystyle\displaystyle\mathcal{L}\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε−(2​d2+1)+Nδ​log⁡(r~)),𝔭2=O​(ε2−(4​d1−2)​Nδ),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon^{-(2d\_{2}+1)}+N^{\delta}\log(\widetilde{r})\right),\mathfrak{p}\_{2}=O(\varepsilon\_{2}^{-(4d\_{1}-2)N^{\delta}}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K2\displaystyle\displaystyle K\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε−2​(d2+1)+Nδ​log⁡(r~)),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon^{-2(d\_{2}+1)}+N^{\delta}\log(\widetilde{r})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | κ2\displaystyle\displaystyle\kappa\_{2} | =O​(ε−Nδ​(2​d2+1)),R2=1.\displaystyle\displaystyle=O(\varepsilon^{-N^{\delta}(2d\_{2}+1)}),R\_{2}=1. |  |

By Lemma [4.3](https://arxiv.org/html/2511.07235v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Functional Approximations ‣ 4 Neural scaling of operator learning ‣ Deep Neural Operator Learning for Probabilistic Models"), and equation [6.15](https://arxiv.org/html/2511.07235v1#S6.E15 "In 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models"),

|  |  |  |
| --- | --- | --- |
|  | Nδ≤C​(log⁡ε2−4)d1α​ε2−2​d1​d1d12.\displaystyle\displaystyle N^{\delta}\leq C(\log\varepsilon\_{2}^{-4})^{\frac{d\_{1}}{\alpha}}\varepsilon\_{2}^{-2d\_{1}}d\_{1}^{\frac{d\_{1}}{2}}. |  |

Substitute back to ε\displaystyle\varepsilon, we have Nδ=O​(ε−4d1d2−2d1))\displaystyle N^{\delta}=O(\varepsilon^{-4d\_{1}d\_{2}-2d\_{1})}).
It follows that N2=O​(ε−(4​d2−2)​ε−4​d1​d2−2​d1)\displaystyle N\_{2}=O(\varepsilon^{-(4d\_{2}-2)\varepsilon^{-4d\_{1}d\_{2}-2d\_{1}}}).

∎

###### Lemma 6.3.

Let Qr~=[−r~,r~]Nδ\displaystyle Q\_{\widetilde{r}}=[-\widetilde{r},\widetilde{r}]^{N^{\delta}}, 𝐠=[g1,…,gNδ]𝖳∈Qr~\displaystyle\bm{g}=\bigl[g\_{1},\ldots,g\_{N^{\delta}}\bigr]^{\mathsf{T}}\in Q\_{\widetilde{r}} and β𝐠=supg∈Qr~|h​(g)|\displaystyle\beta\_{\bm{g}}=\sup\_{g\in Q\_{\widetilde{r}}}|h(g)|.
Assume function h:Qr~→ℝ\displaystyle h:Q\_{\widetilde{r}}\rightarrow\mathbb{R}, with Nδ\displaystyle N^{\delta} as an integer and some constant r~\displaystyle\widetilde{r}, and h\displaystyle h satisfies the following assumption,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h​(g)−h​(g~)|≤L​(|g−g~|2+|g−g~|)1/2,g,g~∈Qr~,\displaystyle\displaystyle|h(g)-h(\widetilde{g})|\leq L(|g-\widetilde{g}|^{2}+|g-\widetilde{g}|)^{1/2},g,\widetilde{g}\in Q\_{\widetilde{r}}, |  | (6.19) |

where L\displaystyle L is a constant.
For ε2>0\displaystyle\varepsilon\_{2}>0, there exist N2\displaystyle N\_{2}, {𝐠k}k=1N2⊂Qr~\displaystyle\{\bm{g}\_{k}\}\_{k=1}^{N\_{2}}\subset Q\_{\widetilde{r}}, and a network ℱ2=ℱNN​(Nδ,1,ℒ2,𝔭2,K2,κ2,R2)\displaystyle\mathcal{F}\_{2}=\mathcal{F}\_{\rm NN}(N^{\delta},1,\mathcal{L}\_{2},\mathfrak{p}\_{2},K\_{2},\kappa\_{2},R\_{2}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2\displaystyle\displaystyle\mathcal{L}\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε2−1+Nδ​log⁡(r~)),𝔭2=O​(1),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon\_{2}^{-1}+N^{\delta}\log(\widetilde{r})\right),\mathfrak{p}\_{2}=O(1), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K2\displaystyle\displaystyle K\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε2−1+Nδ​log⁡(r~)),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon\_{2}^{-1}+N^{\delta}\log(\widetilde{r})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | κ2\displaystyle\displaystyle\kappa\_{2} | =O​(ε2−Nδ),R=1,\displaystyle\displaystyle=O(\varepsilon\_{2}^{-N^{\delta}}),R=1, |  |

such that

|  |  |  |
| --- | --- | --- |
|  | supg∈Qr~|h​(g)−∑k=1N2h​(𝒈k)​q~k|≤ε2,\displaystyle\displaystyle\sup\_{g\in Q\_{\widetilde{r}}}\left|h(g)-\sum\_{k=1}^{N\_{2}}h({\bm{g}}\_{k})\widetilde{q}\_{k}\right|\leq\varepsilon\_{2}, |  |

where N2=NNδ\displaystyle N\_{2}=N^{N^{\delta}}, with N=O​(Nδ​ε2−2)\displaystyle N=O(\sqrt{N^{\delta}}\varepsilon\_{2}^{-2}).

###### Proof of Lemma.

Let us partition Qr~\displaystyle Q\_{\widetilde{r}} into NNδ\displaystyle N^{N^{\delta}} subcubes for some N\displaystyle N to be specified later, and Nδ\displaystyle N^{\delta} follows the Theorem [6.2](https://arxiv.org/html/2511.07235v1#S6.Thmtheorem2 "Theorem 6.2. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models").
Let {𝒈k}k=1NNδ\displaystyle\{\bm{g}\_{k}\}\_{k=1}^{N^{N^{\delta}}} be a uniform grid on Qr~\displaystyle Q\_{\widetilde{r}} so that each 𝒈k∈{−r~,−r~+2​r~N−1,…,r~}Nδ\displaystyle\bm{g}\_{k}\in\left\{-\widetilde{r},-\widetilde{r}+\frac{2\widetilde{r}}{N-1},...,\widetilde{r}\right\}^{N^{\delta}} for each k\displaystyle k.
Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(a)={1,|a|<1,0,|a|>2,2−|a|,1≤|a|≤2,\displaystyle\displaystyle\psi(a)=\begin{cases}1,|a|<1,\\ 0,|a|>2,\\ 2-|a|,1\leq|a|\leq 2,\end{cases} |  | (6.20) |

with a∈ℝ\displaystyle a\in\mathbb{R}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ𝒈k​(𝐱)=∏j=1Nδψ​(3​(N−1)2​r~​(xj−gk,j)).\displaystyle\displaystyle\phi\_{\bm{g}\_{k}}(\mathbf{x})=\prod\_{j=1}^{N^{\delta}}\psi\left(\frac{3(N-1)}{2\widetilde{r}}(x\_{j}-g\_{k,j})\right). |  | (6.21) |

In this definition, we have supp​(ϕ𝒈k)={𝐱:‖𝐱−𝒈k‖∞≤4​r~3​(N−1)}⊂{𝐱:‖𝐱−𝒈k‖∞≤2​r~(N−1)}\displaystyle\mathrm{supp\,}(\phi\_{\bm{g}\_{k}})=\left\{\mathbf{x}:\|\mathbf{x}-\bm{g}\_{k}\|\_{\infty}\leq\frac{4\widetilde{r}}{3(N-1)}\right\}\subset\left\{\mathbf{x}:\|\mathbf{x}-\bm{g}\_{k}\|\_{\infty}\leq\frac{2\widetilde{r}}{(N-1)}\right\} and

|  |  |  |
| --- | --- | --- |
|  | maxk⁡ϕ𝒈k=1,∑k=1NNδϕ𝒈k=1.\max\_{k}\phi\_{\bm{g}\_{k}}=1,\quad\sum\_{k=1}^{N^{N^{\delta}}}\phi\_{\bm{g}\_{k}}=1. |  |

We construct a piecewise constant approximation to h\displaystyle h as

|  |  |  |
| --- | --- | --- |
|  | h¯​(𝐱)=∑k=1NNδh​(𝒈k)​ϕ𝒈k​(𝐱).\bar{h}(\mathbf{x})=\sum\_{k=1}^{N^{N^{\delta}}}h(\bm{g}\_{k})\phi\_{\bm{g}\_{k}}(\mathbf{x}). |  |

It follows that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h​(𝒈)−h¯​(𝒈)|=\displaystyle\displaystyle|h(\bm{g})-\bar{h}(\bm{g})|= | |∑k=1NNδϕ𝒈k​(𝐱)​(h​(𝒈)−h​(𝒈k))|\displaystyle\displaystyle\left|\sum\_{k=1}^{N^{N^{\delta}}}\phi\_{\bm{g}\_{k}}(\mathbf{x})(h(\bm{g})-h(\bm{g}\_{k}))\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | ∑k=1NNδϕ𝒈k​(𝐱)​|h​(𝒈)−h​(𝒈k)|\displaystyle\displaystyle\sum\_{k=1}^{N^{N^{\delta}}}\phi\_{\bm{g}\_{k}}(\mathbf{x})|h(\bm{g})-h(\bm{g}\_{k})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle\displaystyle= | ∑k:‖𝒈k−𝐱‖∞≤2​r~(N−1)ϕ𝒈k​(𝐱)​|(h​(𝐱)−h​(𝒈k))|\displaystyle\displaystyle\sum\_{k:\|\bm{g}\_{k}-\mathbf{x}\|\_{\infty}\leq\frac{2\widetilde{r}}{(N-1)}}\phi\_{\bm{g}\_{k}}(\mathbf{x})|(h(\mathbf{x})-h(\bm{g}\_{k}))| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | maxk:‖𝒈k−𝐱‖∞≤2​r~(N−1)⁡|(h​(𝐱)−h​(𝒈k))|​(∑k:‖𝒈k−𝐱‖∞≤2​r~(N−1)ϕ𝒈k​(𝐱))\displaystyle\displaystyle\max\_{k:\|\bm{g}\_{k}-\mathbf{x}\|\_{\infty}\leq\frac{2\widetilde{r}}{(N-1)}}|(h(\mathbf{x})-h(\bm{g}\_{k}))|\left(\sum\_{k:\|\bm{g}\_{k}-\mathbf{x}\|\_{\infty}\leq\frac{2\widetilde{r}}{(N-1)}}\phi\_{\bm{g}\_{k}}(\mathbf{x})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | maxk:‖𝒈k−𝐱‖∞≤2​r~(N−1)⁡|(h​(𝐱)−h​(𝒈k))|\displaystyle\displaystyle\max\_{k:\|\bm{g}\_{k}-\mathbf{x}\|\_{\infty}\leq\frac{2\widetilde{r}}{(N-1)}}|(h(\mathbf{x})-h(\bm{g}\_{k}))| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | LΓA​((2​Nδ​r~N−1)2+(2​Nδ​r~N−1))12<ε22,\displaystyle\displaystyle L\_{\Gamma\_{A}}\left(\left(\frac{2\sqrt{N^{\delta}}\widetilde{r}}{N-1}\right)^{2}+\left(\frac{2\sqrt{N^{\delta}}\widetilde{r}}{N-1}\right)\right)^{\frac{1}{2}}<\frac{\varepsilon\_{2}}{2}, |  | (6.22) |

where the last line follows from the Assumption [6.19](https://arxiv.org/html/2511.07235v1#S6.E19 "In Lemma 6.3. ‣ 6.1 Operator approximation for American option pricing operator ‣ 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models").
Setting N=C​LΓA2​ε2−2​(Nδ)12​r~\displaystyle N=CL\_{\Gamma\_{A}}^{2}\varepsilon\_{2}^{-2}(N^{\delta})^{\frac{1}{2}}\widetilde{r},
where C\displaystyle C is a constant.
Now we adopt neural network with structure q~k∈ℱ2\displaystyle\widetilde{q}\_{k}\in\mathcal{F}\_{2} to be specified later to approximate ϕ𝒈k\displaystyle\phi\_{{\bm{g}}\_{k}} such that ‖ϕ𝒈k−q~k‖L∞​(Qr~)≤Nδ​δ~\displaystyle\|\phi\_{{\bm{g}}\_{k}}-\widetilde{q}\_{k}\|\_{L^{\infty}(Q\_{\widetilde{r}})}\leq N^{\delta}\widetilde{\delta}, with δ~\displaystyle\widetilde{\delta} to be specified later.
We hence have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∑k=1NNδh​(𝒈k)​q~k−h¯‖L∞​(Qr~)≤\displaystyle\displaystyle\left\|\sum\_{k=1}^{N^{N^{\delta}}}h({\bm{g}}\_{k})\widetilde{q}\_{k}-\bar{h}\right\|\_{L^{\infty}(Q\_{\widetilde{r}})}\leq | ∑k=1NNδ|h​(𝒈k)|​‖q~k−ϕ𝒈k‖L∞​(Qr~)\displaystyle\displaystyle\sum\_{k=1}^{N^{N^{\delta}}}|h({\bm{g}}\_{k})|\|\widetilde{q}\_{k}-\phi\_{{\bm{g}}\_{k}}\|\_{L^{\infty}(Q\_{\widetilde{r}})} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\displaystyle\leq | Nδ​NNδ​β𝒈​δ~.\displaystyle\displaystyle N^{\delta}N^{N^{\delta}}\beta\_{\bm{g}}\widetilde{\delta}. |  | (6.23) |

Now set δ~=C​ε2Nδ​NNδ​β𝒈\displaystyle\widetilde{\delta}=C\frac{\varepsilon\_{2}}{N^{\delta}N^{N^{\delta}}\beta\_{\bm{g}}}, where C\displaystyle C is a constant.
Consequently the network has an architecture, ℱ2=ℱNN​(Nδ,1,ℒ2,𝔭2,K2,κ2,R2)\displaystyle\mathcal{F}\_{2}=\mathcal{F}\_{\rm NN}(N^{\delta},1,\mathcal{L}\_{2},\mathfrak{p}\_{2},K\_{2},\kappa\_{2},R\_{2}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2\displaystyle\displaystyle\mathcal{L}\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε2−1+Nδ​log⁡(r~)),𝔭2=O​(1),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon\_{2}^{-1}+N^{\delta}\log(\widetilde{r})\right),\mathfrak{p}\_{2}=O(1), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K2\displaystyle\displaystyle K\_{2} | =O​((Nδ+12​(Nδ)2)​log⁡(Nδ)+(2​(Nδ)2+Nδ)​log⁡ε2−1+Nδ​log⁡(r~)),\displaystyle\displaystyle=O\left((N^{\delta}+\frac{1}{2}(N^{\delta})^{2})\log(N^{\delta})+(2(N^{\delta})^{2}+N^{\delta})\log\varepsilon\_{2}^{-1}+N^{\delta}\log(\widetilde{r})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | κ2\displaystyle\displaystyle\kappa\_{2} | =O​(ε2−Nδ),R2=1,\displaystyle\displaystyle=O(\varepsilon\_{2}^{-N^{\delta}}),R\_{2}=1, |  |

here the hidden constant depends on LΓA\displaystyle L\_{\Gamma\_{A}} and β𝒈\displaystyle\beta\_{\bm{g}}.
∎

## 7 Algorithm

A unifying view to solve a basket of American options has been studied in
[[3](https://arxiv.org/html/2511.07235v1#bib.bib3)] by using one unified Snell envelope. In this section, we use the proposed deep neural operator to solve this basket of American options problem. In particular, we are able to provide the exercise boundary for new strike prices within the range of our training sets. The precise training process and model specification is presented below.

In the following numerical example, we train a deep operator neural network to obtain the pricing operator of Bermudan put option. Then we plot the exercise boundaries for various terminal payoff functions in Figure [1](https://arxiv.org/html/2511.07235v1#S7.F1 "Figure 1 ‣ 7 Algorithm ‣ Deep Neural Operator Learning for Probabilistic Models").

The ground-truth training data are produced by a fully implicit finite-difference discretization of the Black–Scholes American pricing PDE in log-price variables on a uniform grid, closely following standard references on PDE methods for options [[43](https://arxiv.org/html/2511.07235v1#bib.bib43)].

Under the risk–neutral measure, the price of an American option with strike K\displaystyle K, volatility σ>0\displaystyle\sigma>0, and risk–free rate r>0\displaystyle r>0 satisfies the Black–Scholes PDE with free boundary as in ([6.4](https://arxiv.org/html/2511.07235v1#S6.E4 "In 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models"))
with terminal condition u​(T,x)=gk​(x)=max⁡(K−x,0).\displaystyle u(T,x)=g\_{k}(x)=\max(K-x,0).

The space–time grid is given by xj=xmin+j​Δ​x\displaystyle x\_{j}=x\_{\min}+j\Delta x for j=0,…,Nx−1\displaystyle j=0,\dots,N\_{x}-1 and tn=n​Δ​t\displaystyle t\_{n}=n\Delta t for n=0,…,Nt\displaystyle n=0,\dots,N\_{t}, with Δ​x=(xmax−xmin)/(Nx−1)\displaystyle\Delta x=(x\_{\max}-x\_{\min})/(N\_{x}-1), Δ​t=T/Nt\displaystyle\Delta t=T/N\_{t}. In our numerical example, we set the risk-free interest rate r=0.1\displaystyle r=0.1, the volatility σ=0.2\displaystyle\sigma=0.2, the time to maturity T=1\displaystyle T=1, Nt=50\displaystyle N\_{t}=50 and Nx=300\displaystyle N\_{x}=300. The price interval is chosen wide enough to contain the early-exercise region for all strikes in the training range: with Kmin=90\displaystyle K\_{\min}=90 and Kmax=120\displaystyle K\_{\max}=120, we take xmin=Kmin/2=45\displaystyle x\_{\min}=K\_{\min}/2=45 and xmax=1.5​Kmax=180\displaystyle x\_{\max}=1.5K\_{\max}=180.

We first perform a log transformation such that let y=ln⁡x\displaystyle y=\ln x and define v​(y,t):=u​(x,t)=u​(ey,t)\displaystyle v(y,t):=u(x,t)=u(e^{y},t). Then

|  |  |  |
| --- | --- | --- |
|  | ux=1x​vy,ux​x=1x2​(vy​y−vy),u\_{x}=\frac{1}{x}v\_{y},\qquad u\_{xx}=\frac{1}{x^{2}}\left(v\_{yy}-v\_{y}\right), |  |

and ([6.4](https://arxiv.org/html/2511.07235v1#S6.E4 "In 6 Deep neural operator for American option pricing and PDE with free boundary ‣ Deep Neural Operator Learning for Probabilistic Models")) becomes the constant–coefficient convection–diffusion equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tv+12​σ2​vy​y+μ​vy−r​v=0,μ:=r−12​σ2.\partial\_{t}v+\frac{1}{2}\sigma^{2}v\_{yy}+\mu\,v\_{y}-rv=0,\qquad\mu:=r-\tfrac{1}{2}\sigma^{2}. |  | (7.1) |

Denote vjn≈v​(yj,tn)\displaystyle v\_{j}^{n}\approx v(y\_{j},t\_{n}).
Use centered differences in space at time level n\displaystyle n:

|  |  |  |
| --- | --- | --- |
|  | vy​(yj,tn)≈vj+1n−vj−1n2​Δ​y,vy​y​(yj,tn)≈vj+1n−2​vjn+vj−1nΔ​y2.v\_{y}(y\_{j},t\_{n})\approx\frac{v\_{j+1}^{n}-v\_{j-1}^{n}}{2\Delta y},\qquad v\_{yy}(y\_{j},t\_{n})\approx\frac{v\_{j+1}^{n}-2v\_{j}^{n}+v\_{j-1}^{n}}{\Delta y^{2}}. |  |

The finite difference algorithm runs backward in time from tNt=T\displaystyle t\_{N\_{t}}=T to t0=0\displaystyle t\_{0}=0, the fully implicit step

|  |  |  |  |
| --- | --- | --- | --- |
|  | vjn−vjn+1Δ​t+12​σ2​vj+1n−2​vjn+vj−1nΔ​x2+μ​vj+1n−vj−1n2​Δ​x−r​vjn=0.\frac{v\_{j}^{n}-v\_{j}^{n+1}}{\Delta t}+\frac{1}{2}\sigma^{2}\frac{v\_{j+1}^{n}-2v\_{j}^{n}+v\_{j-1}^{n}}{\Delta x^{2}}+\mu\frac{v\_{j+1}^{n}-v\_{j-1}^{n}}{2\Delta x}-rv\_{j}^{n}=0. |  | (7.2) |

After rearranging into matrix form, and enforcing the free boundary condition, (v)n\displaystyle(v)^{n} are obtained from (v)n+1\displaystyle(v)^{n+1}.

Our approach uses operator learning for Bermudan-style put options. From sampled space–time values of option prices, we train a neural operator that, given a payoff function, reconstructs the full price surface and thereby recovers the optimal exercise (stopping) boundary.

Let Γ\displaystyle\Gamma denote the pricing operator that maps a payoff gk\displaystyle g\_{k} to its price surface uk\displaystyle u\_{k}. On a grid {xj}j=1Nx×{tn}n=1Nt\displaystyle\{x\_{j}\}\_{j=1}^{N\_{x}}\times\{t\_{n}\}\_{n=1}^{N\_{t}},

|  |  |  |
| --- | --- | --- |
|  | uk​(xj,tn)=Γ​gk​(xj,tn).u\_{k}(x\_{j},t\_{n})=\Gamma g\_{k}(x\_{j},t\_{n}). |  |

The neural operator Γθ\displaystyle\Gamma\_{\theta} with parameters θ\displaystyle\theta is trained to approximate the pricing operator by minimizing the empirical mean-squared error

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ)=1K​Nt​Nx​∑k=1K∑j=1Nx∑n=1Nt|Γθ​gk​(xj,tn)−uk​(xj,tn)|2.\mathcal{L}(\theta)=\frac{1}{K\,N\_{t}\,N\_{x}}\sum\_{k=1}^{K}\sum\_{j=1}^{N\_{x}}\sum\_{n=1}^{N\_{t}}\bigl|\Gamma\_{\theta}g\_{k}(x\_{j},t\_{n})-u\_{k}(x\_{j},t\_{n})\bigr|^{2}. |  | (7.3) |

This optimization ensures that the operator network learns an accurate mapping from input payoff functions to their corresponding option price surfaces. Our algorithm is capable of computing the exercise boundary for any strike price between 90 and 120. We select six payoff functions with different strike prices and present their corresponding exercise boundaries in the Figure [1](https://arxiv.org/html/2511.07235v1#S7.F1 "Figure 1 ‣ 7 Algorithm ‣ Deep Neural Operator Learning for Probabilistic Models"). Once trained, the learned operator Γθ\displaystyle\Gamma\_{\theta} can be utilized to recover the entire exercise boundary from the approximated solution surface.

![[Uncaptioned image]](figures/Strike90.png)

![[Uncaptioned image]](figures/Strike96.png)

![[Uncaptioned image]](figures/Strike101.png)

![[Uncaptioned image]](figures/Strike107.png)



![Refer to caption](figures/Strike113.png)

![Refer to caption](figures/Strike117.png)

Figure 1: Exercise boundaries for American put options.

## References

* [1]

  Guillermo Alvarez, Ibrahim Ekren, Anastasis Kratsios, and Xuwei Yang.
  Neural operators can play dynamic stackelberg games.
  arXiv preprint arXiv:2411.09644, 2024.
* [2]

  Robert Azencott.
  Formule de taylor stochastique et développement asymptotique
  d’intégrales de feynmann.
  In Séminaire de Probabilités XVI, 1980/81
  Supplément: Géométrie Différentielle Stochastique, pages
  237–285. Springer, 2006.
* [3]

  Peter Bank and Hans Föllmer.
  American options, multi–armed bandits, and optimal consumption
  plans: A unifying view.
  In Paris-Princeton Lectures on Mathematical Finance 2002, pages
  1–42. Springer, 2003.
* [4]

  Fabrice Baudoin, Eulalia Nualart, Cheng Ouyang, and Samy Tindel.
  On probability laws of solutions to differential systems driven by a
  fractional brownian motion.
  Ann. Probab., 44(4):2554–2590, 2016.
* [5]

  Christian Bayer, Paul P Hager, Sebastian Riedel, and John Schoenmakers.
  Optimal stopping with signatures.
  The Annals of Applied Probability, 33(1):238–273, 2023.
* [6]

  Erhan Bayraktar, Qi Feng, and Zhaoyu Zhang.
  Deep signature algorithm for multidimensional path-dependent options.
  SIAM Journal on Financial Mathematics, 15(1):194–214, 2024.
* [7]

  Sebastian Becker, Patrick Cheridito, and Arnulf Jentzen.
  Deep optimal stopping.
  Journal of Machine Learning Research, 20(74):1–25, 2019.
* [8]

  Sebastian Becker, Patrick Cheridito, Arnulf Jentzen, and Timo Welti.
  Solving high-dimensional optimal stopping problems using deep
  learning.
  European Journal of Applied Mathematics, 32(3):470–514, 2021.
* [9]

  Kaushik Bhattacharya, Bamdad Hosseini, Nikola B Kovachki, and Andrew M Stuart.
  Model reduction and neural networks for parametric pdes.
  The SMAI journal of computational mathematics, 7:121–157,
  2021.
* [10]

  Cristian Bodnar, Wessel P Bruinsma, Ana Lucic, Megan Stanley, Anna Allen,
  Johannes Brandstetter, Patrick Garvan, Maik Riechert, Jonathan A Weyn, Haiyu
  Dong, et al.
  A foundation model for the earth system.
  Nature, pages 1–8, 2025.
* [11]

  Fabienne Castell.
  Asymptotic expansion of stochastic flows.
  Probability theory and related fields, 96(2):225–239, 1993.
* [12]

  Tianping Chen and Hong Chen.
  Approximations of continuous functionals by neural networks with
  application to dynamic systems.
  IEEE Transactions on Neural networks, 4(6):910–918, 1993.
* [13]

  Tianping Chen and Hong Chen.
  Universal approximation to nonlinear operators by neural networks
  with arbitrary activation functions and its application to dynamical systems.
  IEEE Transactions on Neural Networks, 6(4):911–917, 1995.
* [14]

  John Horton Conway and Neil James Alexander Sloane.
  Sphere packings, lattices and groups, volume 290.
  Springer Science & Business Media, 2013.
* [15]

  Nicole El Karoui, Christophe Kapoudjian, Etienne Pardoux, Shige Peng, and
  Marie-Claire Quenez.
  Reflected solutions of backward sde’s, and related obstacle problems
  for pde’s.
  the Annals of Probability, 25(2):702–737, 1997.
* [16]

  Qi Feng and Xuejing Zhang.
  Taylor expansions and castell estimates for solutions of stochastic
  differential equations driven by rough paths.
  Journal of Stochastic Analysis, 1(2):4, 2020.
* [17]

  Takashi Furuya and Anastasis Kratsios.
  Simultaneously solving fbsdes with neural operators of logarithmic
  depth, constant width, and sub-linear rank.
  arXiv preprint arXiv:2410.14788, 2024.
* [18]

  Chengfan Gao, Siping Gao, Ruimeng Hu, and Zimu Zhu.
  Convergence of the backward deep bsde method with applications to
  optimal stopping problems.
  SIAM Journal on Financial Mathematics, 14(4):1290–1303, 2023.
* [19]

  Lukas Gonon.
  Deep neural network expressivity for optimal stopping problems.
  Finance and Stochastics, 28(3):865–910, 2024.
* [20]

  Calypso Herrera, Florian Krach, Pierre Ruyssen, and Josef Teichmann.
  Optimal stopping via randomized neural networks.
  Frontiers of Mathematical Finance, 3(1):31–77, 2024.
* [21]

  Amanda A Howard, Mauro Perego, George E Karniadakis, and Panos Stinis.
  Multifidelity deep operator networks.
  arXiv preprint arXiv:2204.09157, 2022.
* [22]

  Côme Huré, Huyên Pham, and Xavier Warin.
  Deep backward schemes for high-dimensional nonlinear pdes.
  Mathematics of Computation, 89(324):1547–1579, 2020.
* [23]

  Nikola Kovachki, Samuel Lanthaler, and Siddhartha Mishra.
  On universal approximation and error bounds for fourier neural
  operators.
  Journal of Machine Learning Research, 22(290):1–76, 2021.
* [24]

  Nikola Kovachki, Zongyi Li, Burigede Liu, Kamyar Azizzadenesheli, Kaushik
  Bhattacharya, Andrew Stuart, and Anima Anandkumar.
  Neural operator: Learning maps between function spaces with
  applications to pdes.
  Journal of Machine Learning Research, 24(89):1–97, 2023.
* [25]

  Samuel Lanthaler.
  Operator learning with pca-net: upper and lower complexity bounds.
  Journal of Machine Learning Research, 24(318):1–67, 2023.
* [26]

  Samuel Lanthaler, Siddhartha Mishra, and George E Karniadakis.
  Error estimates for deeponets: A deep learning framework in infinite
  dimensions.
  Transactions of Mathematics and Its Applications, 6(1):tnac001,
  2022.
* [27]

  Samuel Lanthaler and Andrew M Stuart.
  The parametric complexity of operator learning.
  IMA Journal of Numerical Analysis, page draf028, 2025.
* [28]

  Bernard Lapeyre and Jérôme Lelong.
  Neural network regression for bermudan option pricing.
  Monte Carlo Methods and Applications, 27(3):227–247, 2021.
* [29]

  Wing Tat Leung, Guang Lin, and Zecheng Zhang.
  Nh-pinn: Neural homogenization-based physics-informed neural network
  for multiscale problems.
  Journal of Computational Physics, 470:111539, 2022.
* [30]

  Zongyi Li, Daniel Zhengyu Huang, Burigede Liu, and Anima Anandkumar.
  Fourier neural operator with learned deformations for pdes on general
  geometries.
  Journal of Machine Learning Research, 24(388):1–26, 2023.
* [31]

  Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik
  Bhattacharya, Andrew Stuart, and Anima Anandkumar.
  Fourier neural operator for parametric partial differential
  equations.
  arXiv preprint arXiv:2010.08895, 2020.
* [32]

  Guang Lin, Christian Moya, and Zecheng Zhang.
  B-deeponet: An enhanced bayesian deeponet for solving noisy
  parametric pdes using accelerated replica exchange sgld.
  Journal of Computational Physics, 473:111713, 2023.
* [33]

  Hao Liu, Haizhao Yang, Minshuo Chen, Tuo Zhao, and Wenjing Liao.
  Deep nonparametric estimation of operators between infinite
  dimensional spaces.
  Journal of Machine Learning Research, 25(24):1–67, 2024.
* [34]

  Hao Liu, Zecheng Zhang, Wenjing Liao, and Hayden Schaeffer.
  Neural scaling laws of deep relu and deep operator network: A
  theoretical study.
  arXiv preprint arXiv:2410.00357, 2024.
* [35]

  Lu Lu, Pengzhan Jin, Guofei Pang, Zhongqiang Zhang, and George Em Karniadakis.
  Learning nonlinear operators via deeponet based on the universal
  approximation theorem of operators.
  Nature Machine Intelligence, 3(3):218–229, 2021.
* [36]

  Jaideep Pathak, Shashank Subramanian, Peter Harrington, Sanjeev Raja, Ashesh
  Chattopadhyay, Morteza Mardani, Thorsten Kurth, David Hall, Zongyi Li, Kamyar
  Azizzadenesheli, et al.
  Fourcastnet: A global data-driven high-resolution weather model using
  adaptive fourier neural operators.
  arXiv preprint arXiv:2202.11214, 2022.
* [37]

  A Max Reppen, H Mete Soner, and Valentin Tissot-Daguette.
  Neural optimal stopping boundary.
  arXiv preprint arXiv:2205.04595, 2022.
* [38]

  Mykhaylo Shkolnikov, H Mete Soner, and Valentin Tissot-Daguette.
  Deep level-set method for stefan problems.
  Journal of Computational Physics, 503:112828, 2024.
* [39]

  Justin Sirignano and Konstantinos Spiliopoulos.
  Dgm: A deep learning algorithm for solving partial differential
  equations.
  Journal of computational physics, 375:1339–1364, 2018.
* [40]

  H Mete Soner and Valentin Tissot-Daguette.
  Stopping times of boundaries: Relaxation and continuity.
  SIAM Journal on Control and Optimization, 63(4):2835–2855,
  2025.
* [41]

  Loring W Tu.
  Manifolds.
  In An Introduction to Manifolds, pages 47–83. Springer, 2011.
* [42]

  Jindong Wang and Wenrui Hao.
  Laplacian eigenfunction-based neural operator for learning nonlinear
  reaction–diffusion dynamics.
  Journal of Computational Physics, page 114400, 2025.
* [43]

  Paul Wilmott, Sam Howison, and Jeff Dewynne.
  The Mathematics of Financial Derivatives: A Student
  Introduction.
  Cambridge University Press, 1995.
* [44]

  Dmitry Yarotsky.
  Error bounds for approximations with deep relu networks.
  Neural networks, 94:103–114, 2017.
* [45]

  Jianfeng Zhang and Jianfeng Zhang.
  Backward stochastic differential equations.
  Springer, 2017.