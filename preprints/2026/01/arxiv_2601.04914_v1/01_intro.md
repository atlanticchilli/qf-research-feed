---
authors:
- Jean-Gabriel Attali
doc_id: arxiv:2601.04914v1
family_id: arxiv:2601.04914
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow
  Networks
url_abs: http://arxiv.org/abs/2601.04914v1
url_html: https://arxiv.org/html/2601.04914v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jean-Gabriel Attali
  
De Vinci Higher Education, De Vinci Research Center, Paris, France
  
jean-gabriel.attali@devinci.fr

###### Abstract

We study approximation limits of single-hidden-layer neural networks with analytic
activation functions under global coefficient constraints.
Under uniform ℓ1\ell^{1} bounds, or more generally sub-exponential growth of the
coefficients, we show that such networks generate model classes with strong quantitative
regularity, leading to uniform analyticity of the realized functions.
As a consequence, up to an exponentially small residual term, the error of best network
approximation on generic target functions is bounded from below by the error of best
polynomial approximation.
In particular, networks with analytic
activation functions with controlled coefficients cannot outperform
classical polynomial approximation rates on non-analytic targets.
The underlying rigidity phenomenon extends to smoother, non-analytic activations
satisfying Gevrey-type regularity assumptions, yielding sub-exponential variants of the
approximation barrier.
The analysis is entirely deterministic and relies on a comparison argument combined with
classical Bernstein-type estimates; extensions to higher dimensions are also discussed.

Keywords:
neural networks, analytic activation functions, polynomial approximation,
approximation barriers, Gevrey regularity.

MSC 2020:
41A10, 41A25, 68T07.

## 1 Introduction

Single-hidden-layer neural networks are classical nonlinear approximation tools whose theoretical properties have been extensively studied over the past decades. Early results established their universal approximation capabilities under mild assumptions on the activation function. More refined analyses later showed that, under additional structural assumptions on the target function, such networks may achieve remarkably fast approximation rates.
A prominent example is provided by the theory initiated by Barron [[3](https://arxiv.org/html/2601.04914v1#bib.bib1 "Universal approximation bounds for superpositions of a sigmoidal function")], and earlier related contributions such as Attali and Pag‘es [[1](https://arxiv.org/html/2601.04914v1#bib.bib3 "Approximations of functions by a multilayer perceptron: the random case"), [2](https://arxiv.org/html/2601.04914v1#bib.bib2 "Approximation of functions by a multilayer perceptron: a probabilistic approach")], which show that neural networks can overcome the curse of dimensionality when the target function belongs to a suitable analytic or spectral class. These results crucially rely on global constraints on the network coefficients and on strong regularity properties of the target function itself.
In parallel, classical approximation theory provides sharp minimax bounds for generic smoothness classes such as Lipschitz or Sobolev spaces. These bounds show that, in the absence of additional structure, no approximation method can outperform polynomial rates [[6](https://arxiv.org/html/2601.04914v1#bib.bib4 "Constructive approximation"), [7](https://arxiv.org/html/2601.04914v1#bib.bib5 "Nonlinear approximation")]. This fundamental limitation naturally raises the following question:
*can analyticity of the activation function alone improve approximation rates on generic target functions?*
Before addressing this question, it is important to note that analyticity-based approximation properties depend not only on the activation function but also on the effective control of the network parameters. In particular, uniform analyticity on a fixed complex neighborhood is obtained when the inner parameters remain suitably bounded; more generally, increasing inner parameters lead to shrinking analytic neighborhoods and exponentially small residual terms, as discussed later.
In this work, we provide a negative answer to the above question. We show that analyticity of the activation function, even when combined with uniform ℓ1\ell^{1} bounds on the network coefficients, does not suffice to overcome the classical polynomial approximation barrier on non-analytic target functions. More precisely, we consider single-hidden-layer networks with real-analytic activation functions and uniformly bounded coefficient sums, and we show that the error of best network approximation is bounded from below by the error of best polynomial approximation, up to an exponentially small term. This result should be understood as a rigidity phenomenon for analytic model classes, rather than as a minimax lower bound.
Our results reveal a structural limitation of networks with analytic
activation functions. While analyticity plays a central role in positive approximation results for structured target classes, it also imposes intrinsic constraints on the class of realizable functions. As a consequence, networks with analytic
activation functions cannot adapt to non-analytic features of generic target functions and cannot achieve approximation rates faster than those dictated by classical polynomial approximation theory.
The proof is entirely deterministic and relies on a comparison between best network approximation and best polynomial approximation, combined with classical Bernstein-type estimates for analytic functions. In contrast with probabilistic constructions or random sampling arguments, our approach provides a transparent explanation of why analyticity of the activation function alone cannot bypass minimax approximation barriers. Although the main results are presented for analytic activation functions, the underlying rigidity mechanism extends to smoother, non-analytic activations under quantitative regularity assumptions, such as Gevrey smoothness, leading to sub-exponential variants of the approximation barrier.

###### Remark 1.1.

Throughout the paper, we restrict attention to functions defined on the interval [−1,1][-1,1].
This choice is made for notational convenience only: any compact interval can be reduced to
this setting by an affine change of variables, without affecting approximation rates or
analyticity properties.
Working on [−1,1][-1,1] allows us to use standard Bernstein ellipses and simplifies the presentation.

The paper is organized as follows.
Section 2 introduces the class of analytic activation networks considered throughout
the paper and establishes their basic analytic properties.
Section 3 recalls classical results on polynomial approximation of analytic functions.
The main lower bound is stated and proved in Section 4.
Finally, Section 5 discusses the implications of our results and their relation to
existing approximation theories for neural networks.

## 2 Analytic Activation Networks

In this section, we introduce the class of neural networks considered throughout the paper and establish their basic analytic properties. The framework is entirely deterministic and relies on analyticity of the activation function together with global bounds on the network coefficients.
A key point is that the approximation properties derived below hold in a regime where the analytic regularity of the resulting model class can be quantitatively controlled. In particular, uniform analyticity on a fixed complex neighborhood is obtained under suitable control of the inner parameters; more general parameter growth leads to shrinking analytic neighborhoods, which will be accounted for explicitly in the subsequent estimates.

### 2.1 Model definition

Let φ:ℝ→ℝ\varphi:\mathbb{R}\to\mathbb{R} be a real-analytic function.
We consider single-hidden-layer neural networks of the form

|  |  |  |
| --- | --- | --- |
|  | g​(x)=∑k=1mλk​φ​(αk​x),x∈[−1,1],g(x)=\sum\_{k=1}^{m}\lambda\_{k}\,\varphi(\alpha\_{k}x),\qquad x\in[-1,1], |  |

where m≥1m\geq 1 and λk,αk∈ℝ\lambda\_{k},\alpha\_{k}\in\mathbb{R}.
For a fixed constant C>0C>0, we denote by 𝒩m​(C)\mathcal{N}\_{m}(C) the class of network functions
whose output weights satisfy the uniform ℓ1\ell^{1} constraint

|  |  |  |
| --- | --- | --- |
|  | ∑k=1m|λk|≤C.\sum\_{k=1}^{m}|\lambda\_{k}|\leq C. |  |

We omit bias terms for simplicity.
Their inclusion in expressions of the form φ​(α​x+b)\varphi(\alpha x+b) would not affect any of the
arguments below, as long as the biases remain uniformly bounded.

The analysis relies on the fact that the resulting model class enjoys a controlled analytic
structure.
More precisely, we assume that for each mm there exists a complex neighborhood
Um⊂ℂU\_{m}\subset\mathbb{C} containing the interval [−1,1][-1,1] and a constant Cm>0C\_{m}>0 such that every
function g∈𝒩m​(C)g\in\mathcal{N}\_{m}(C) admits a holomorphic extension to UmU\_{m} satisfying

|  |  |  |
| --- | --- | --- |
|  | supz∈Um|g​(z)|≤Cm.\sup\_{z\in U\_{m}}|g(z)|\leq C\_{m}. |  |

This assumption captures the uniform analyticity properties induced by the activation function
together with the imposed parameter constraints, and constitutes the only structural hypothesis
used in the comparison arguments developed below.

The ℓ1\ell^{1} constraint on the output weights plays a central role in controlling the complexity
of the model.
Such constraints are classical in approximation theory and arise naturally in several contexts,
including Barron-type representations and earlier works on multilayer perceptrons
[[3](https://arxiv.org/html/2601.04914v1#bib.bib1 "Universal approximation bounds for superpositions of a sigmoidal function"), [2](https://arxiv.org/html/2601.04914v1#bib.bib2 "Approximation of functions by a multilayer perceptron: a probabilistic approach")].
Throughout the paper, the constraint is imposed deterministically and uniformly with respect to
the network width mm.

### 2.2 Analytic extension and uniform bounds

A key consequence of analyticity of the activation function is that it imposes strong
regularity constraints on the functions generated by the network.

###### Assumption 2.1 (Analytic extension).

Fix ρ>1\rho>1 and L≥1L\geq 1.
The activation function φ\varphi admits a holomorphic extension to an open neighborhood of
the dilated Bernstein ellipse L​Eρ:={L​z:z∈Eρ}LE\_{\rho}:=\{Lz:z\in E\_{\rho}\}, and we set

|  |  |  |
| --- | --- | --- |
|  | Mρ,L​(φ):=supz∈L​Eρ|φ​(z)|<∞.M\_{\rho,L}(\varphi):=\sup\_{z\in LE\_{\rho}}|\varphi(z)|<\infty. |  |

Under this assumption, the analytic structure of network outputs can be controlled
uniformly.

###### Proposition 2.1 (Uniform analytic control).

Assume φ\varphi satisfies Assumption 2.1.
Let L≥1L\geq 1 and consider network functions

|  |  |  |
| --- | --- | --- |
|  | g​(x)=∑k=1mλk​φ​(αk​x),x∈[−1,1],g(x)=\sum\_{k=1}^{m}\lambda\_{k}\,\varphi(\alpha\_{k}x),\qquad x\in[-1,1], |  |

with ∑k=1m|λk|≤C\sum\_{k=1}^{m}|\lambda\_{k}|\leq C and |αk|≤L|\alpha\_{k}|\leq L for all kk.
Then gg admits a holomorphic extension to EρE\_{\rho} and satisfies

|  |  |  |
| --- | --- | --- |
|  | supz∈Eρ|g​(z)|≤C​Mρ,L​(φ).\sup\_{z\in E\_{\rho}}|g(z)|\leq C\,M\_{\rho,L}(\varphi). |  |

###### Proof.

Let g​(x)=∑k=1mλk​φ​(αk​x)g(x)=\sum\_{k=1}^{m}\lambda\_{k}\,\varphi(\alpha\_{k}x).
Fix z∈Eρz\in E\_{\rho}. Since |αk|≤L|\alpha\_{k}|\leq L, we have αk​z∈L​Eρ\alpha\_{k}z\in LE\_{\rho}.
By Assumption 2.1, φ\varphi is holomorphic on a neighborhood of L​EρLE\_{\rho}; hence
z↦φ​(αk​z)z\mapsto\varphi(\alpha\_{k}z) is holomorphic on EρE\_{\rho}, and

|  |  |  |
| --- | --- | --- |
|  | |φ​(αk​z)|≤supw∈L​Eρ|φ​(w)|=Mρ,L​(φ).|\varphi(\alpha\_{k}z)|\leq\sup\_{w\in LE\_{\rho}}|\varphi(w)|=M\_{\rho,L}(\varphi). |  |

Therefore, by linearity and the ℓ1\ell^{1} bound on the coefficients,

|  |  |  |
| --- | --- | --- |
|  | supz∈Eρ|g​(z)|≤∑k=1m|λk|​supz∈Eρ|φ​(αk​z)|≤(∑k=1m|λk|)​Mρ,L​(φ)≤C​Mρ,L​(φ),\sup\_{z\in E\_{\rho}}|g(z)|\leq\sum\_{k=1}^{m}|\lambda\_{k}|\,\sup\_{z\in E\_{\rho}}|\varphi(\alpha\_{k}z)|\leq\Big(\sum\_{k=1}^{m}|\lambda\_{k}|\Big)\,M\_{\rho,L}(\varphi)\leq C\,M\_{\rho,L}(\varphi), |  |

which proves the claim.
∎

### 2.3 Smooth non-analytic activations: a Gevrey relaxation

The analyticity assumption imposed in the previous sections can be relaxed to a broader
class of infinitely differentiable activation functions, provided that their smoothness
is controlled in a quantitative manner.
In this subsection, we introduce a canonical relaxation based on Gevrey regularity,
which allows one to retain a weakened but still effective form of the polynomial
approximation barrier established for analytic activations.

#### Gevrey regularity.

Let s≥1s\geq 1. A function φ∈C∞​(ℝ)\varphi\in C^{\infty}(\mathbb{R}) is said to belong to the
Gevrey class Gs​(ℝ)G^{s}(\mathbb{R}) if there exist constants Cφ>0C\_{\varphi}>0 and Rφ>0R\_{\varphi}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈ℝ|φ(n)​(t)|≤Cφ​Rφn​(n!)s,∀n≥0.\sup\_{t\in\mathbb{R}}|\varphi^{(n)}(t)|\leq C\_{\varphi}\,R\_{\varphi}^{\,n}\,(n!)^{s},\qquad\forall n\geq 0. |  | (1) |

The case s=1s=1 corresponds, up to constants, to real-analytic functions, while s>1s>1
describes a large family of C∞C^{\infty} but non-analytic functions, including standard
compactly supported mollifiers and smooth activations obtained by regularizing
piecewise linear functions.

Gevrey classes provide a classical quantitative relaxation of analyticity, interpolating between
real-analytic and general C∞C^{\infty} regularity. They play a central role in approximation theory
and the study of sub-exponential approximation rates; see, e.g., Rodino [[9](https://arxiv.org/html/2601.04914v1#bib.bib13 "Linear partial differential operators in gevrey spaces")] or
DeVore and Lorentz [[6](https://arxiv.org/html/2601.04914v1#bib.bib4 "Constructive approximation")].

#### Uniform Gevrey control of network outputs.

We consider single-hidden-layer networks of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | gm​(x)=∑k=1mλk​φ​(αk​x),x∈[−1,1],g\_{m}(x)=\sum\_{k=1}^{m}\lambda\_{k}\,\varphi(\alpha\_{k}x),\qquad x\in[-1,1], |  | (2) |

under the coefficient constraints

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1m|λk|≤Bm,|αk|≤Lm.\sum\_{k=1}^{m}|\lambda\_{k}|\leq B\_{m},\qquad|\alpha\_{k}|\leq L\_{m}. |  | (3) |

###### Proposition 2.2 (Uniform Gevrey control).

Assume that φ∈Gs​(ℝ)\varphi\in G^{s}(\mathbb{R}) satisfies ([1](https://arxiv.org/html/2601.04914v1#S2.E1 "In Gevrey regularity. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks")).
Then every function gmg\_{m} of the form ([2](https://arxiv.org/html/2601.04914v1#S2.E2 "In Uniform Gevrey control of network outputs. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks")) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖gm(n)‖L∞​([−1,1])≤Cφ​Bm​(Rφ​Lm)n​(n!)s,∀n≥0.\|g\_{m}^{(n)}\|\_{L^{\infty}([-1,1])}\leq C\_{\varphi}\,B\_{m}\,(R\_{\varphi}L\_{m})^{n}\,(n!)^{s},\qquad\forall n\geq 0. |  | (4) |

In particular, the family of network outputs is uniformly bounded in the Gevrey class
Gs​([−1,1])G^{s}([-1,1]), with constants depending only on BmB\_{m} and LmL\_{m}.

###### Proof.

Differentiating ([2](https://arxiv.org/html/2601.04914v1#S2.E2 "In Uniform Gevrey control of network outputs. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks")) nn times yields

|  |  |  |
| --- | --- | --- |
|  | gm(n)​(x)=∑k=1mλk​αkn​φ(n)​(αk​x).g\_{m}^{(n)}(x)=\sum\_{k=1}^{m}\lambda\_{k}\,\alpha\_{k}^{\,n}\,\varphi^{(n)}(\alpha\_{k}x). |  |

Using the triangle inequality, the coefficient constraints
([3](https://arxiv.org/html/2601.04914v1#S2.E3 "In Uniform Gevrey control of network outputs. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks")), and the Gevrey bound ([1](https://arxiv.org/html/2601.04914v1#S2.E1 "In Gevrey regularity. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks")), we obtain

|  |  |  |
| --- | --- | --- |
|  | |gm(n)​(x)|≤∑k=1m|λk|​|αk|n​supt∈ℝ|φ(n)​(t)|≤Cφ​Bm​(Rφ​Lm)n​(n!)s,|g\_{m}^{(n)}(x)|\leq\sum\_{k=1}^{m}|\lambda\_{k}|\,|\alpha\_{k}|^{n}\sup\_{t\in\mathbb{R}}|\varphi^{(n)}(t)|\leq C\_{\varphi}\,B\_{m}\,(R\_{\varphi}L\_{m})^{n}\,(n!)^{s}, |  |

uniformly for x∈[−1,1]x\in[-1,1], which proves the claim.
∎

### 2.4 Discussion and relation to analytic and Gevrey frameworks

Proposition [2.1](https://arxiv.org/html/2601.04914v1#S2.Thmtheorem1 "Proposition 2.1 (Uniform analytic control). ‣ 2.2 Analytic extension and uniform bounds ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") and Proposition [2.2](https://arxiv.org/html/2601.04914v1#S2.Thmtheorem2 "Proposition 2.2 (Uniform Gevrey control). ‣ Uniform Gevrey control of network outputs. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") show that, under global ℓ1\ell^{1} constraints,
single-hidden-layer networks generate model classes with strong quantitative
regularity, ranging from uniform analyticity to Gevrey smoothness.
This property is central to the comparison arguments developed in the subsequent
sections.

Related analytic regularity phenomena have already been observed in earlier works on
neural network approximation.
In particular, Attali and Pagès [[2](https://arxiv.org/html/2601.04914v1#bib.bib2 "Approximation of functions by a multilayer perceptron: a probabilistic approach")] studied approximation by
multilayer perceptrons with analytic activation functions and emphasized the strong
regularity induced by analyticity.
Barron-type results [[3](https://arxiv.org/html/2601.04914v1#bib.bib1 "Universal approximation bounds for superpositions of a sigmoidal function")] also rely on global coefficient constraints, but
their conclusions concern approximation on structured target classes rather than
generic functions.

The present work adopts a different perspective.
Rather than exploiting analyticity to derive positive approximation rates, we use it
to identify intrinsic limitations of analytic activation networks on generic target
functions.
The uniform analytic bounds established above will serve as the starting point for the
polynomial comparison arguments developed in Sections 3 and 4.

#### Historical context.

Explicit low-dimensional instances of the rigidity induced by analyticity were already observed
in early works by Attali and Pagès [[1](https://arxiv.org/html/2601.04914v1#bib.bib3 "Approximations of functions by a multilayer perceptron: the random case"), [2](https://arxiv.org/html/2601.04914v1#bib.bib2 "Approximation of functions by a multilayer perceptron: a probabilistic approach")].
In particular, these authors provided an explicit bivariate proof of the convergence of partial
derivatives for Bernstein-type approximants, placing the result in an appendix as a classical
technical ingredient in their analysis of multilayer perceptrons.
From a modern perspective, this argument can be viewed as an early manifestation of the
general rigidity phenomena associated with globally parametrized analytic approximation schemes.

## 3 Polynomial Approximation of Analytic Functions

In this section, we recall classical results on the approximation of analytic functions
by algebraic polynomials.
These results form a cornerstone of approximation theory and will be used as a key
ingredient in the proof of the main lower bound.
Standard references include the works of Bernstein, Timan, DeVore and Lorentz, and
more recent expositions such as [[4](https://arxiv.org/html/2601.04914v1#bib.bib7 "Leçons sur les propriétés extrémales et la meilleure approximation des fonctions analytiques d’une variable réelle"), [10](https://arxiv.org/html/2601.04914v1#bib.bib8 "Theory of approximation of functions of a real variable"), [6](https://arxiv.org/html/2601.04914v1#bib.bib4 "Constructive approximation"), [11](https://arxiv.org/html/2601.04914v1#bib.bib10 "Approximation theory and approximation practice")].

### 3.1 Bernstein ellipses and analytic norms

Let K=[−1,1]K=[-1,1].
For ρ>1\rho>1, denote by EρE\_{\rho} the Bernstein ellipse with foci at ±1\pm 1 and parameter
ρ\rho, defined as the image of the circle {w∈ℂ:|w|=ρ}\{w\in\mathbb{C}:\ |w|=\rho\} under the
Joukowski map

|  |  |  |
| --- | --- | --- |
|  | w↦12​(w+w−1).w\mapsto\tfrac{1}{2}\bigl(w+w^{-1}\bigr). |  |

The ellipse EρE\_{\rho} is a compact subset of ℂ\mathbb{C} containing [−1,1][-1,1].

For a function hh holomorphic on EρE\_{\rho}, we define the associated analytic norm by

|  |  |  |
| --- | --- | --- |
|  | Mρ​(h)=supz∈Eρ|h​(z)|.M\_{\rho}(h)=\sup\_{z\in E\_{\rho}}|h(z)|. |  |

This quantity provides a convenient measure of the strength of analyticity of hh in a
neighborhood of the real interval.

### 3.2 Best polynomial approximation

For a continuous function h∈C​([−1,1])h\in C([-1,1]), we denote by

|  |  |  |
| --- | --- | --- |
|  | Em(h)=inf{∥h−p∥∞:p is a polynomial of degree at most m}E\_{m}(h)=\inf\bigl\{\|h-p\|\_{\infty}:\ p\text{ is a polynomial of degree at most }m\bigr\} |  |

the error of best uniform polynomial approximation of degree at most mm.

If hh is merely continuous, the decay of Em​(h)E\_{m}(h) is typically polynomial and governed
by the smoothness of hh.
In contrast, analyticity of hh implies exponentially fast decay of the approximation
error.

###### Proposition 3.1 (Bernstein-type inequality).

Let ρ>1\rho>1 and let hh be holomorphic on EρE\_{\rho}.
Then there exists a constant Aρ>0A\_{\rho}>0, depending only on ρ\rho, such that

|  |  |  |
| --- | --- | --- |
|  | Em​(h)≤Aρ​Mρ​(h)​ρ−m,m≥1.E\_{m}(h)\leq A\_{\rho}\,M\_{\rho}(h)\,\rho^{-m},\qquad m\geq 1. |  |

This result is classical and can be found in many textbooks on approximation theory;
see for instance [[4](https://arxiv.org/html/2601.04914v1#bib.bib7 "Leçons sur les propriétés extrémales et la meilleure approximation des fonctions analytiques d’une variable réelle"), [10](https://arxiv.org/html/2601.04914v1#bib.bib8 "Theory of approximation of functions of a real variable"), [6](https://arxiv.org/html/2601.04914v1#bib.bib4 "Constructive approximation"), [11](https://arxiv.org/html/2601.04914v1#bib.bib10 "Approximation theory and approximation practice")].

### 3.3 Consequences for analytic model classes

Proposition [4.1](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem1 "Proposition 4.1 (Bernstein inequality). ‣ 4.1 Bernstein ellipses and polynomial approximation ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") shows that any family of functions admitting a uniform
analytic extension to a fixed Bernstein ellipse necessarily enjoys exponentially fast
polynomial approximation.

More precisely, if a class ℱ⊂C​([−1,1])\mathcal{F}\subset C([-1,1]) satisfies

|  |  |  |
| --- | --- | --- |
|  | suph∈ℱMρ​(h)<∞\sup\_{h\in\mathcal{F}}M\_{\rho}(h)<\infty |  |

for some ρ>1\rho>1, then every function in ℱ\mathcal{F} can be approximated uniformly by
polynomials at an exponential rate.

As shown in Section 2, networks with analytic
activation functions with uniformly ℓ1\ell^{1}-bounded
coefficients generate families of functions that satisfy exactly such uniform analytic
bounds.
This observation provides the crucial link between neural network approximation and
classical polynomial approximation and forms the basis of the comparison argument
developed in the next section. From the viewpoint of classical approximation theory, networks with analytic
activation functions with
global coefficient constraints form a precompact family in C([-1,1]).
This observation explains why approximation rates beyond those achieved by polynomial
methods cannot be expected on generic target functions.

#### Remark (Gevrey extension).

Although the results of this section are stated for analytic functions,
classical approximation theory provides analogous estimates for functions
with Gevrey regularity.
In that case, exponential polynomial approximation rates are replaced by
sub-exponential bounds depending on the Gevrey index.
Since our arguments rely only on quantitative polynomial approximation
estimates, the comparison results of Section 4 extend verbatim to the
Gevrey setting introduced in Section 2.3.

## 4 Polynomial approximation barrier

This section establishes a lower bound showing that single-hidden-layer neural networks with
analytic or Gevrey activation functions and globally controlled coefficients remain confined to
classical polynomial approximation regimes on generic target functions. The argument relies on
quantitative regularity of the model class and a direct comparison with best polynomial
approximation.

### 4.1 Bernstein ellipses and polynomial approximation

For ρ>1\rho>1, let EρE\_{\rho} denote the Bernstein ellipse with foci ±1\pm 1. For a function hh
holomorphic on EρE\_{\rho}, define

|  |  |  |
| --- | --- | --- |
|  | Mρ​(h):=supz∈Eρ|h​(z)|.M\_{\rho}(h):=\sup\_{z\in E\_{\rho}}|h(z)|. |  |

The error of best uniform polynomial approximation of degree at most mm is

|  |  |  |
| --- | --- | --- |
|  | Em​(h):=infdeg⁡p≤m‖h−p‖L∞​([−1,1]).E\_{m}(h):=\inf\_{\deg p\leq m}\|h-p\|\_{L^{\infty}([-1,1])}. |  |

###### Proposition 4.1 (Bernstein inequality).

For every ρ>1\rho>1 there exists a constant C​(ρ)>0C(\rho)>0 such that, for all functions hh
holomorphic on EρE\_{\rho},

|  |  |  |
| --- | --- | --- |
|  | Em​(h)≤C​(ρ)​Mρ​(h)​ρ−m,m≥1.E\_{m}(h)\leq C(\rho)\,M\_{\rho}(h)\,\rho^{-m},\qquad m\geq 1. |  |

### 4.2 Analytic activation functions

Let φ:ℝ→ℝ\varphi:\mathbb{R}\to\mathbb{R} be a real-analytic activation function.
For m≥1m\geq 1, consider single-hidden-layer networks of the form

|  |  |  |
| --- | --- | --- |
|  | gm​(x)=∑k=1mλk​φ​(αk​x),x∈[−1,1],g\_{m}(x)=\sum\_{k=1}^{m}\lambda\_{k}\varphi(\alpha\_{k}x),\qquad x\in[-1,1], |  |

under the constraints

|  |  |  |
| --- | --- | --- |
|  | ∑k=1m|λk|≤Bm,|αk|≤Lm.\sum\_{k=1}^{m}|\lambda\_{k}|\leq B\_{m},\qquad|\alpha\_{k}|\leq L\_{m}. |  |

###### Assumption 4.1 (Analytic extension on a Bernstein ellipse).

There exist ρ>1\rho>1 and L≥1L\geq 1 such that φ\varphi admits a holomorphic extension to a
neighborhood of the dilated ellipse L​Eρ:={L​z:z∈Eρ}LE\_{\rho}:=\{Lz:\ z\in E\_{\rho}\}, and

|  |  |  |
| --- | --- | --- |
|  | Mρ,L​(φ):=supw∈L​Eρ|φ​(w)|<∞.M\_{\rho,L}(\varphi):=\sup\_{w\in LE\_{\rho}}|\varphi(w)|<\infty. |  |

###### Lemma 4.1 (Uniform analytic control).

Assume that φ\varphi satisfies Assumption [4.1](https://arxiv.org/html/2601.04914v1#S4.Thmassumption1 "Assumption 4.1 (Analytic extension on a Bernstein ellipse). ‣ 4.2 Analytic activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") and that Lm≤LL\_{m}\leq L.
Then gmg\_{m} admits a holomorphic extension to EρE\_{\rho} and

|  |  |  |
| --- | --- | --- |
|  | Mρ​(gm)≤Bm​Mρ,L​(φ).M\_{\rho}(g\_{m})\leq B\_{m}\,M\_{\rho,L}(\varphi). |  |

###### Proof.

For z∈Eρz\in E\_{\rho} and 1≤k≤m1\leq k\leq m, the bound |αk|≤L|\alpha\_{k}|\leq L implies αk​z∈L​Eρ\alpha\_{k}z\in LE\_{\rho}.
Thus

|  |  |  |
| --- | --- | --- |
|  | |φ​(αk​z)|≤Mρ,L​(φ),|\varphi(\alpha\_{k}z)|\leq M\_{\rho,L}(\varphi), |  |

and

|  |  |  |
| --- | --- | --- |
|  | |gm​(z)|≤∑k=1m|λk|​|φ​(αk​z)|≤Bm​Mρ,L​(φ).|g\_{m}(z)|\leq\sum\_{k=1}^{m}|\lambda\_{k}|\,|\varphi(\alpha\_{k}z)|\leq B\_{m}\,M\_{\rho,L}(\varphi). |  |

∎

###### Proposition 4.2 (Polynomial approximation of analytic network outputs).

Under the assumptions of Lemma [4.1](https://arxiv.org/html/2601.04914v1#S4.Thmlemma1 "Lemma 4.1 (Uniform analytic control). ‣ 4.2 Analytic activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"), there exists C​(ρ)>0C(\rho)>0 such that

|  |  |  |
| --- | --- | --- |
|  | Em​(gm)≤C​(ρ)​Bm​Mρ,L​(φ)​ρ−m.E\_{m}(g\_{m})\leq C(\rho)\,B\_{m}\,M\_{\rho,L}(\varphi)\,\rho^{-m}. |  |

###### Theorem 4.3 (Polynomial approximation barrier: analytic case).

Let φ\varphi satisfy Assumption [4.1](https://arxiv.org/html/2601.04914v1#S4.Thmassumption1 "Assumption 4.1 (Analytic extension on a Bernstein ellipse). ‣ 4.2 Analytic activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"). Then for all
f∈C​([−1,1])f\in C([-1,1]) and all m≥1m\geq 1,

|  |  |  |
| --- | --- | --- |
|  | infgm‖f−gm‖L∞​([−1,1])≥Em​(f)−C​(ρ)​Bm​Mρ,L​(φ)​ρ−m,\inf\_{g\_{m}}\|f-g\_{m}\|\_{L^{\infty}([-1,1])}\geq E\_{m}(f)-C(\rho)\,B\_{m}\,M\_{\rho,L}(\varphi)\,\rho^{-m}, |  |

where the infimum is taken over all networks satisfying the above constraints.

###### Proof.

Let pmp\_{m} be a best polynomial approximant of degree at most mm to gmg\_{m}. Then

|  |  |  |
| --- | --- | --- |
|  | ‖f−gm‖∞≥‖f−pm‖∞−‖gm−pm‖∞≥Em​(f)−Em​(gm).\|f-g\_{m}\|\_{\infty}\geq\|f-p\_{m}\|\_{\infty}-\|g\_{m}-p\_{m}\|\_{\infty}\geq E\_{m}(f)-E\_{m}(g\_{m}). |  |

Apply Proposition [4.2](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem2 "Proposition 4.2 (Polynomial approximation of analytic network outputs). ‣ 4.2 Analytic activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
∎

###### Remark 4.4 (Optimized scaling).

If φ\varphi is holomorphic and bounded only on a strip |ℑ⁡z|<δ|\Im z|<\delta, then gmg\_{m} is
holomorphic on |ℑ⁡z|<δ/Lm|\Im z|<\delta/L\_{m}. Choosing ρm>1\rho\_{m}>1 such that
Eρm⊂{|ℑ⁡z|<δ/Lm}E\_{\rho\_{m}}\subset\{|\Im z|<\delta/L\_{m}\} with ρm=1+c​δ/Lm\rho\_{m}=1+c\,\delta/L\_{m} yields

|  |  |  |
| --- | --- | --- |
|  | Em​(gm)≤A​Bm​exp⁡(−c​mLm),E\_{m}(g\_{m})\leq A\,B\_{m}\,\exp\!\Big(-c\,\frac{m}{L\_{m}}\Big), |  |

and the lower bound of Theorem [4.3](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem3 "Theorem 4.3 (Polynomial approximation barrier: analytic case). ‣ 4.2 Analytic activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") holds with this optimized residual.

### 4.3 Extension to Gevrey activation functions

Let s≥1s\geq 1. A function ψ∈C∞​([−1,1])\psi\in C^{\infty}([-1,1]) belongs to the Gevrey class Gs​([−1,1])G^{s}([-1,1])
if there exist constants Cψ,Rψ>0C\_{\psi},R\_{\psi}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖ψ(n)‖L∞​([−1,1])≤Cψ​Rψn​(n!)s,n≥0.\|\psi^{(n)}\|\_{L^{\infty}([-1,1])}\leq C\_{\psi}\,R\_{\psi}^{\,n}\,(n!)^{s},\qquad n\geq 0. |  |

###### Proposition 4.5 (Polynomial approximation of Gevrey functions).

If h∈Gs​([−1,1])h\in G^{s}([-1,1]), then there exist constants A,c>0A,c>0 such that

|  |  |  |
| --- | --- | --- |
|  | Em​(h)≤A​exp⁡(−c​m1/s),m≥1.E\_{m}(h)\leq A\,\exp\!\big(-c\,m^{1/s}\big),\qquad m\geq 1. |  |

Let φ∈Gs​(ℝ)\varphi\in G^{s}(\mathbb{R}) and consider networks gmg\_{m} as above.

###### Lemma 4.2 (Uniform Gevrey bounds for network outputs).

There exist constants Cφ,Rφ>0C\_{\varphi},R\_{\varphi}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖gm(n)‖L∞​([−1,1])≤Cφ​Bm​(Rφ​Lm)n​(n!)s,n≥0.\|g\_{m}^{(n)}\|\_{L^{\infty}([-1,1])}\leq C\_{\varphi}\,B\_{m}\,(R\_{\varphi}L\_{m})^{n}\,(n!)^{s},\qquad n\geq 0. |  |

###### Proof.

Differentiation yields

|  |  |  |
| --- | --- | --- |
|  | gm(n)​(x)=∑k=1mλk​αkn​φ(n)​(αk​x).g\_{m}^{(n)}(x)=\sum\_{k=1}^{m}\lambda\_{k}\alpha\_{k}^{n}\varphi^{(n)}(\alpha\_{k}x). |  |

Using the coefficient bounds and the Gevrey estimate on φ\varphi gives the result.
∎

###### Theorem 4.6 (Polynomial approximation barrier: Gevrey case).

Let φ∈Gs​(ℝ)\varphi\in G^{s}(\mathbb{R}) with s>1s>1. Then there exist constants A,c>0A,c>0 such that for all
f∈C​([−1,1])f\in C([-1,1]) and all m≥1m\geq 1,

|  |  |  |
| --- | --- | --- |
|  | infgm‖f−gm‖L∞​([−1,1])≥Em​(f)−A​Bm​exp⁡(−c​(m/Lm)1/s).\inf\_{g\_{m}}\|f-g\_{m}\|\_{L^{\infty}([-1,1])}\geq E\_{m}(f)-A\,B\_{m}\,\exp\!\Big(-c\,(m/L\_{m})^{1/s}\Big). |  |

###### Proof.

Proceed as in the analytic case:

|  |  |  |
| --- | --- | --- |
|  | ‖f−gm‖∞≥Em​(f)−Em​(gm).\|f-g\_{m}\|\_{\infty}\geq E\_{m}(f)-E\_{m}(g\_{m}). |  |

Apply Proposition [4.5](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem5 "Proposition 4.5 (Polynomial approximation of Gevrey functions). ‣ 4.3 Extension to Gevrey activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") to gmg\_{m}, using Lemma [4.2](https://arxiv.org/html/2601.04914v1#S4.Thmlemma2 "Lemma 4.2 (Uniform Gevrey bounds for network outputs). ‣ 4.3 Extension to Gevrey activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
∎

###### Remark 4.7 (Extended regularization paradox).

The above results show that the effectiveness of neural network approximation is governed by
the *combined growth* of the output weights and the inner parameters.
In the analytic setting, the residual term in
Theorem [4.3](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem3 "Theorem 4.3 (Polynomial approximation barrier: analytic case). ‣ 4.2 Analytic activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") tends to zero whenever

|  |  |  |
| --- | --- | --- |
|  | log⁡Bm=o​(mLm),\log B\_{m}=o\!\left(\frac{m}{L\_{m}}\right), |  |

in which case the network class remains confined to the same approximation regime as
classical polynomial methods on generic target functions.

More generally, under the Gevrey regularity assumptions of
Theorem [4.6](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem6 "Theorem 4.6 (Polynomial approximation barrier: Gevrey case). ‣ 4.3 Extension to Gevrey activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") with index s>1s>1, the corresponding condition becomes

|  |  |  |
| --- | --- | --- |
|  | log⁡Bm=o​((mLm)1/s),\log B\_{m}=o\!\left(\left(\frac{m}{L\_{m}}\right)^{1/s}\right), |  |

and the exponential residual term is replaced by a sub-exponential one.
In both cases, regularization mechanisms that control only the magnitude of the output
weights are insufficient to guarantee improved approximation power.
As long as the combined growth condition holds, the model class remains locked into an
approximation regime dictated by its quantitative regularity, and cannot adapt efficiently
to non-analytic or non-Gevrey features of generic target functions.

###### Remark 4.8 (Relation with Barron-type weighted constraints).

Barron-type approximation results are based on a weighted variation control of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1m|λk|​‖αk‖≤CB,\sum\_{k=1}^{m}|\lambda\_{k}|\,\|\alpha\_{k}\|\leq C\_{\mathrm{B}}, |  | (5) |

which naturally arises when discretizing an integral representation of the target function.
This constraint differs fundamentally from the uniform bounds considered in the present work,
as it does not impose any *a priori* restriction on the magnitude of the inner parameters
αk\alpha\_{k}.

*Derivative control.*
Under ([5](https://arxiv.org/html/2601.04914v1#S4.E5 "In Remark 4.8 (Relation with Barron-type weighted constraints). ‣ 4.3 Extension to Gevrey activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks")), and assuming that φ\varphi is continuously differentiable
with locally bounded derivative, the associated network function

|  |  |  |
| --- | --- | --- |
|  | g​(x)=∑k=1mλk​φ​(⟨αk,x⟩)g(x)=\sum\_{k=1}^{m}\lambda\_{k}\,\varphi(\langle\alpha\_{k},x\rangle) |  |

admits a uniformly bounded gradient on [−1,1]d[-1,1]^{d}, namely

|  |  |  |
| --- | --- | --- |
|  | ‖∇g‖L∞​([−1,1]d)≤sup|t|≤L​d|φ′​(t)|​∑k=1m|λk|​‖αk‖,L:=maxk⁡‖αk‖.\|\nabla g\|\_{L^{\infty}([-1,1]^{d})}\;\leq\;\sup\_{|t|\leq L\sqrt{d}}|\varphi^{\prime}(t)|\,\sum\_{k=1}^{m}|\lambda\_{k}|\,\|\alpha\_{k}\|,\qquad L:=\max\_{k}\|\alpha\_{k}\|. |  |

In particular, if φ′\varphi^{\prime} is bounded on ℝ\mathbb{R}, the Lipschitz constant of gg is
uniformly controlled by CBC\_{\mathrm{B}}, independently of the network width.
This shows that the Barron-type weighted constraint enforces a strong geometric regularity of
the model class.

*Frequency truncation and effective analyticity.*
More generally, the weighted constraint ([5](https://arxiv.org/html/2601.04914v1#S4.E5 "In Remark 4.8 (Relation with Barron-type weighted constraints). ‣ 4.3 Extension to Gevrey activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks")) allows one to decompose
the network function as

|  |  |  |
| --- | --- | --- |
|  | g=g≤L+r>L,g≤L​(x):=∑‖αk‖≤Lλk​φ​(⟨αk,x⟩),g=g\_{\leq L}+r\_{>L},\qquad g\_{\leq L}(x):=\sum\_{\|\alpha\_{k}\|\leq L}\lambda\_{k}\,\varphi(\langle\alpha\_{k},x\rangle), |  |

for any threshold L>0L>0.
The high-frequency remainder satisfies the uniform bound

|  |  |  |
| --- | --- | --- |
|  | ‖r>L‖∞≤∑‖αk‖>L|λk|​sup|φ|≤CBL​sup|φ|.\|r\_{>L}\|\_{\infty}\leq\sum\_{\|\alpha\_{k}\|>L}|\lambda\_{k}|\,\sup|\varphi|\leq\frac{C\_{\mathrm{B}}}{L}\,\sup|\varphi|. |  |

On the other hand, the truncated part g≤Lg\_{\leq L} admits a holomorphic extension to a complex
neighborhood of [−1,1]d[-1,1]^{d} whose size scales as 1/L1/L.
Classical Bernstein-type estimates for multivariate analytic functions then imply that
g≤Lg\_{\leq L} can be approximated by multivariate polynomials of total degree at most mm with
an error decaying as exp⁡(−c​m/L)\exp(-c\,m/L).

*Interpretation.*
This decomposition shows that Barron-type constructions escape the polynomial approximation
barrier identified in this work by allowing the effective analytic neighborhood to shrink with
the network width through the presence of increasingly large inner parameters.
In this regime, uniform analyticity is lost, and the comparison argument with polynomial
approximation no longer applies.
From this perspective, Barron-type approximation results operate precisely at the boundary of
the analyticity-controlled regime considered here.

### 4.4 Extension to higher dimension

We now extend the previous results to functions defined on the hypercube [−1,1]d[-1,1]^{d}.
Under the same assumptions on the activation function and the coefficient constraints,
network outputs admit holomorphic extensions to suitable polyelliptic neighborhoods of the
domain.

Classical Bernstein-type inequalities for multivariate analytic functions on polyelliptic
domains yield exponential bounds on the best polynomial approximation error; see, e.g.,
[[5](https://arxiv.org/html/2601.04914v1#bib.bib12 "Polynomials and polynomial inequalities"), [8](https://arxiv.org/html/2601.04914v1#bib.bib11 "Approximation theory of the mlp model in neural networks")].

For f∈C​([−1,1]d)f\in C([-1,1]^{d}), we denote by Em(d)​(f)E\_{m}^{(d)}(f) the error of best uniform approximation of
ff by multivariate polynomials of total degree at most mm.

###### Theorem 4.9 (Polynomial approximation barrier in dimension dd).

Let d≥1d\geq 1 and let φ:ℝ→ℝ\varphi:\mathbb{R}\to\mathbb{R} be a real-analytic activation function
admitting a holomorphic extension to a complex neighborhood of the real axis.
For each m≥1m\geq 1, let Bm>0B\_{m}>0 and Lm>0L\_{m}>0, and consider the class

|  |  |  |
| --- | --- | --- |
|  | 𝒩m(d)​(Bm,Lm)={g​(x)=∑k=1mλk​φ​(⟨αk,x⟩):∑k=1m|λk|≤Bm,‖αk‖≤Lm}.\mathcal{N}\_{m}^{(d)}(B\_{m},L\_{m})=\Bigl\{g(x)=\sum\_{k=1}^{m}\lambda\_{k}\,\varphi(\langle\alpha\_{k},x\rangle):\sum\_{k=1}^{m}|\lambda\_{k}|\leq B\_{m},\ \|\alpha\_{k}\|\leq L\_{m}\Bigr\}. |  |

Then there exist constants A,c>0A,c>0, depending only on φ\varphi and dd, such that for all
f∈C​([−1,1]d)f\in C([-1,1]^{d}) and all m≥1m\geq 1,

|  |  |  |
| --- | --- | --- |
|  | infg∈𝒩m(d)​(Bm,Lm)‖f−g‖L∞​([−1,1]d)≥Em(d)​(f)−A​Bm​exp⁡(−c​mLm).\inf\_{g\in\mathcal{N}\_{m}^{(d)}(B\_{m},L\_{m})}\|f-g\|\_{L^{\infty}([-1,1]^{d})}\;\geq\;E\_{m}^{(d)}(f)-A\,B\_{m}\,\exp\!\Big(-c\,\frac{m}{L\_{m}}\Big). |  |

###### Proof.

The proof follows the same strategy as in the one-dimensional case.
Each ridge function x↦φ​(⟨αk,x⟩)x\mapsto\varphi(\langle\alpha\_{k},x\rangle) admits a holomorphic extension
to a complex neighborhood of [−1,1]d[-1,1]^{d} whose size scales as 1/‖αk‖1/\|\alpha\_{k}\|.
As a consequence, every function in 𝒩m(d)​(Bm,Lm)\mathcal{N}\_{m}^{(d)}(B\_{m},L\_{m}) admits a holomorphic
extension to a polyelliptic neighborhood of width proportional to 1/Lm1/L\_{m}, with a uniformly
bounded analytic norm of order BmB\_{m}.

Applying multivariate Bernstein-type inequalities yields an approximation error bounded by
A​Bm​exp⁡(−c​m/Lm)A\,B\_{m}\exp(-c\,m/L\_{m}).
The conclusion follows by comparison with the best polynomial approximation of ff.
∎

###### Remark 4.10 (Comparison with CkC^{k} approximation rates).

For functions in Ck​([−1,1]d)C^{k}([-1,1]^{d}) and not smoother, the error of best uniform approximation by
multivariate polynomials of total degree at most mm cannot decay faster than a polynomial
rate, typically of order m−k/dm^{-k/d}.
If log⁡Bm=o​(m/Lm)\log B\_{m}=o(m/L\_{m}), Theorem [4.9](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem9 "Theorem 4.9 (Polynomial approximation barrier in dimension 𝑑). ‣ 4.4 Extension to higher dimension ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks") shows that analytic activation networks remain
confined to these classical rates on CkC^{k} target functions in dimension dd.

###### Remark 4.11 (On the necessity of coefficient growth).

Escaping the polynomial approximation regime requires either exponential growth of the output
weights or sufficiently fast growth of the inner parameters.
This observation is consistent with the constructive approximation results of
Attali and Pagès [[2](https://arxiv.org/html/2601.04914v1#bib.bib2 "Approximation of functions by a multilayer perceptron: a probabilistic approach")], where the approximation of high-degree polynomials by
single-hidden-layer networks with analytic activations involves coefficients that become
arbitrarily large as the target degree increases.

## 5 Discussion and Perspectives

The main result of this paper identifies a fundamental limitation of single-hidden-layer
neural networks with analytic activation functions and uniformly ℓ1\ell^{1}-bounded
coefficients.
Up to an exponentially small term, the best achievable approximation error on generic
target functions is lower bounded by the error of best polynomial approximation.
This shows that analyticity of the activation function, while central to several
positive approximation results, also induces intrinsic rigidity that prevents
adaptation to non-analytic features.

Our result should be interpreted as complementary to classical Barron-type
approximation theorems.
When the target function itself belongs to a structured analytic class, neural networks
can achieve fast, dimension-independent approximation rates.
In contrast, when no such regularity is assumed on the target, the analytic structure
of the model class becomes a limitation rather than an advantage.
In this sense, analyticity does not provide a universal mechanism to bypass minimax
approximation barriers on generic smoothness classes.

###### Remark 5.1 (Relation with the constructions of Attali–Pagès).

In [[2](https://arxiv.org/html/2601.04914v1#bib.bib2 "Approximation of functions by a multilayer perceptron: a probabilistic approach")], fast (in fact arbitrarily fast) approximation of polynomials by
single-hidden-layer neural networks is achieved through a singular parameter regime.
More precisely, the inner parameters scale as αk=O​(h)\alpha\_{k}=O(h) while the output
coefficients behave as λk=O​(h−p)\lambda\_{k}=O(h^{-p}) when approximating polynomials of degree pp.
As a consequence, the Barron-type quantity
∑k|λk|​‖αk‖\sum\_{k}|\lambda\_{k}|\,\|\alpha\_{k}\| diverges as h→0h\to 0. These constructions therefore fall outside the coefficient-constrained
framework considered in the present work and do not contradict the polynomial approximation
barriers established here.

The analysis developed in this work is entirely deterministic and relies on a direct
comparison between best network approximation and best polynomial approximation.
This approach differs from probabilistic constructions or random feature methods and
highlights the role of analytic continuation and Bernstein-type estimates in
understanding the expressive power of neural networks.
It provides a transparent explanation of why analytic activation functions alone cannot
improve approximation rates on non-analytic targets.

###### Remark 5.2 (Relation with Barron-type assumptions).

Barron-type approximation results control complexity through a *variation* (or weighted
ℓ1\ell^{1}) norm on an integral representation of the network.
In discretized models this corresponds to ℓ1\ell^{1}-type constraints on the output weights,
possibly coupled with weighted controls involving the inner parameters.
For a more detailed discussion and a decomposition explaining how Barron-type constructions
escape the uniform analyticity regime considered here, see Remark [4.8](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem8 "Remark 4.8 (Relation with Barron-type weighted constraints). ‣ 4.3 Extension to Gevrey activation functions ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").

###### Remark 5.3 (Sharpness of the lower bound).

The lower bound established in Theorem 4.3 is sharp for a large class of target functions.
Indeed, whenever the best polynomial approximation error satisfies

|  |  |  |
| --- | --- | --- |
|  | Em​(f)≫rm,E\_{m}(f)\gg r\_{m}, |  |

where rmr\_{m} denotes the residual term appearing in Theorem 4.3 (exponentially small in the
analytic case, or sub-exponentially small in the Gevrey case), one has

|  |  |  |
| --- | --- | --- |
|  | infgm‖f−gm‖L∞​([−1,1])=Em​(f)​(1+o​(1))(m→∞).\inf\_{g\_{m}}\|f-g\_{m}\|\_{L^{\infty}([-1,1])}\;=\;E\_{m}(f)\,(1+o(1))\qquad(m\to\infty). |  |

This includes, in particular, all non-analytic functions in classical smoothness classes
Ck​([−1,1])C^{k}([-1,1]) for which Em​(f)E\_{m}(f) decays at most polynomially.
A canonical example is f​(x)=|x|f(x)=|x|, for which it is well known that

|  |  |  |
| --- | --- | --- |
|  | Em​(f)≍m−1.E\_{m}(f)\asymp m^{-1}. |  |

For such functions, the residual term is negligible and networks with analytic
activation functions under
the coefficient constraints considered here cannot outperform polynomial approximation.

A natural question is whether a similar rigidity phenomenon persists when the activation
function is no longer analytic but still infinitely differentiable.
In general, such an extension is not possible without additional assumptions, since
C∞C^{\infty} functions need not admit any holomorphic extension and may exhibit arbitrarily
slow rates of polynomial approximation.
As a consequence, no uniform approximation barrier comparable to the analytic case can
hold for general C∞C^{\infty} activation functions.

Nevertheless, analogous rigidity effects can be established under stronger quantitative
regularity assumptions, such as Gevrey-type bounds on the growth of derivatives.
In that case, the approximation barrier reflects the corresponding regularity class and
leads to sub-exponential, but still non-adaptive, approximation rates.
This highlights that the phenomenon identified in this work is intrinsically tied to the
analytic structure of the activation function.

Several extensions of the present work can be considered.
First, the comparison argument extends naturally to higher-dimensional settings, where
Bernstein-type estimates for multivariate analytic functions yield analogous polynomial
barriers.
Second, it would be of interest to investigate whether similar limitations persist for
deeper architectures with analytic activations under global coefficient constraints.
Finally, the present results suggest that improved approximation on generic targets
requires either non-analytic activation functions or adaptive mechanisms that allow the
model to escape global analytic regularity constraints.

Overall, our findings contribute to a clearer understanding of the interplay between
activation regularity, model constraints, and approximation power, and help delineate
the precise scope of applicability of analytic neural network models in approximation
theory.

## References

* [1]
  J. Attali and G. Pagès (1995)
  Approximations of functions by a multilayer perceptron: the random case.
  Neural Processing Letters 2 (3),  pp. 20–24.
  Cited by: [§1](https://arxiv.org/html/2601.04914v1#S1.p1.1 "1 Introduction ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§2.4](https://arxiv.org/html/2601.04914v1#S2.SS4.SSS0.Px1.p1.1 "Historical context. ‣ 2.4 Discussion and relation to analytic and Gevrey frameworks ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [2]
  J. Attali and G. Pagès (1997)
  Approximation of functions by a multilayer perceptron: a probabilistic approach.
  Neural Networks 10 (6),  pp. 1069–1080.
  Cited by: [§1](https://arxiv.org/html/2601.04914v1#S1.p1.1 "1 Introduction ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§2.1](https://arxiv.org/html/2601.04914v1#S2.SS1.p4.2 "2.1 Model definition ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§2.4](https://arxiv.org/html/2601.04914v1#S2.SS4.SSS0.Px1.p1.1 "Historical context. ‣ 2.4 Discussion and relation to analytic and Gevrey frameworks ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§2.4](https://arxiv.org/html/2601.04914v1#S2.SS4.p2.1 "2.4 Discussion and relation to analytic and Gevrey frameworks ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [Remark 4.11](https://arxiv.org/html/2601.04914v1#S4.Thmtheorem11.p1.1.1 "Remark 4.11 (On the necessity of coefficient growth). ‣ 4.4 Extension to higher dimension ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [Remark 5.1](https://arxiv.org/html/2601.04914v1#S5.Thmtheorem1.p1.5.5 "Remark 5.1 (Relation with the constructions of Attali–Pagès). ‣ 5 Discussion and Perspectives ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [3]
  A. R. Barron (1993)
  Universal approximation bounds for superpositions of a sigmoidal function.
  IEEE Transactions on Information Theory 39 (3),  pp. 930–945.
  Cited by: [§1](https://arxiv.org/html/2601.04914v1#S1.p1.1 "1 Introduction ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§2.1](https://arxiv.org/html/2601.04914v1#S2.SS1.p4.2 "2.1 Model definition ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§2.4](https://arxiv.org/html/2601.04914v1#S2.SS4.p2.1 "2.4 Discussion and relation to analytic and Gevrey frameworks ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [4]
  S. N. Bernstein (1912)
  Leçons sur les propriétés extrémales et la meilleure approximation des fonctions analytiques d’une variable réelle.
   Gauthier-Villars.
  Cited by: [§3.2](https://arxiv.org/html/2601.04914v1#S3.SS2.p3.1 "3.2 Best polynomial approximation ‣ 3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§3](https://arxiv.org/html/2601.04914v1#S3.p1.1 "3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [5]
  P. Borwein and T. Erdélyi (1995)
  Polynomials and polynomial inequalities.
   Springer.
  Cited by: [§4.4](https://arxiv.org/html/2601.04914v1#S4.SS4.p2.1 "4.4 Extension to higher dimension ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [6]
  R. A. DeVore and G. G. Lorentz (1993)
  Constructive approximation.
   Springer.
  Cited by: [§1](https://arxiv.org/html/2601.04914v1#S1.p1.1 "1 Introduction ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§2.3](https://arxiv.org/html/2601.04914v1#S2.SS3.SSS0.Px1.p2.1 "Gevrey regularity. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§3.2](https://arxiv.org/html/2601.04914v1#S3.SS2.p3.1 "3.2 Best polynomial approximation ‣ 3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§3](https://arxiv.org/html/2601.04914v1#S3.p1.1 "3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [7]
  R. A. DeVore (1998)
  Nonlinear approximation.
  Acta Numerica 7,  pp. 51–150.
  Cited by: [§1](https://arxiv.org/html/2601.04914v1#S1.p1.1 "1 Introduction ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [8]
  A. Pinkus (1999)
  Approximation theory of the mlp model in neural networks.
  Acta Numerica 8,  pp. 143–195.
  Cited by: [§4.4](https://arxiv.org/html/2601.04914v1#S4.SS4.p2.1 "4.4 Extension to higher dimension ‣ 4 Polynomial approximation barrier ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [9]
  L. Rodino (1993)
  Linear partial differential operators in gevrey spaces.
   World Scientific.
  Cited by: [§2.3](https://arxiv.org/html/2601.04914v1#S2.SS3.SSS0.Px1.p2.1 "Gevrey regularity. ‣ 2.3 Smooth non-analytic activations: a Gevrey relaxation ‣ 2 Analytic Activation Networks ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [10]
  A. F. Timan (1963)
  Theory of approximation of functions of a real variable.
   Pergamon Press.
  Cited by: [§3.2](https://arxiv.org/html/2601.04914v1#S3.SS2.p3.1 "3.2 Best polynomial approximation ‣ 3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§3](https://arxiv.org/html/2601.04914v1#S3.p1.1 "3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").
* [11]
  L. N. Trefethen (2013)
  Approximation theory and approximation practice.
   SIAM.
  Cited by: [§3.2](https://arxiv.org/html/2601.04914v1#S3.SS2.p3.1 "3.2 Best polynomial approximation ‣ 3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks"),
  [§3](https://arxiv.org/html/2601.04914v1#S3.p1.1 "3 Polynomial Approximation of Analytic Functions ‣ Analytic Regularity and Approximation Limits of Coefficient-Constrained Shallow Networks").