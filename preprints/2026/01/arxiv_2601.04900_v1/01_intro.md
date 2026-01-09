---
authors:
- Jean-Gabriel Attali
doc_id: arxiv:2601.04900v1
family_id: arxiv:2601.04900
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Uniqueness of invariant measures as a structural property of Markov kernels
url_abs: http://arxiv.org/abs/2601.04900v1
url_html: https://arxiv.org/html/2601.04900v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jean-Gabriel Attali
Affiliation, address. Email: jean-gabriel.attali@devinci.fr

###### Abstract

We identify *indecomposability* as a key measure–theoretic mechanism underlying uniqueness of invariant probability measures for
discrete–time Markov kernels on general state spaces. The argument relies on the
mutual singularity of distinct invariant ergodic measures and on the observation
that uniqueness follows whenever all invariant probability measures are forced
to charge a common reference measure.

Once existence of invariant probability measures is known, indecomposability
alone is sufficient to rule out multiplicity. On standard Borel spaces, this
viewpoint is consistent with the classical theory: irreducibility appears as a
convenient sufficient condition ensuring indecomposability, rather than as a
structural requirement for uniqueness.

The resulting proofs are purely measure–theoretic and do not rely on
recurrence, regeneration, return–time estimates, or regularity assumptions on
the transition kernel.

## 1 Introduction

The existence and uniqueness of invariant probability measures are central
questions in the study of Markov chains and stochastic dynamical systems.
Existence is commonly obtained through compactness or tightness arguments,
often supported by Lyapunov–type drift conditions.
Uniqueness, by contrast, is most often derived from stronger dynamical
assumptions, such as Harris recurrence, regeneration techniques, or explicit
control of return times to petite or small sets. These ideas form the backbone
of the general theory developed by Meyn and Tweedie [[10](https://arxiv.org/html/2601.04900v1#bib.bib1 "Markov chains and stochastic stability")].

While extremely powerful, recurrence–based approaches intertwine existence,
uniqueness and ergodic convergence within a single framework. In particular,
uniqueness of the invariant probability measure is typically obtained as a
consequence of positive Harris recurrence together with irreducibility or
minorization conditions. As a result, uniqueness is often perceived as a
dynamical property, intrinsically linked to long–term return behaviour. This
paradigm is well illustrated both in the classical literature and in more recent
developments, where Harris–type arguments are refined or revisited in various
directions (see, for instance, Hairer and Mattingly [[8](https://arxiv.org/html/2601.04900v1#bib.bib5 "Yet another look at Harris’ ergodic theorem for Markov chains")], Douc,
Fort and Guillin [[5](https://arxiv.org/html/2601.04900v1#bib.bib6 "Subgeometric rates of convergence of f-ergodic strong Markov processes")]).

However, in several important classes of models—such as non–Feller Markov
chains, discontinuous random dynamical systems, or nonlinear time
series—verifying Harris recurrence may be technically delicate or may require
strong topological assumptions. This difficulty is well documented in the
literature on random iterative models and stochastic difference equations,
where the transition kernel may fail to be continuous and discontinuities may
occur on sets of positive Lebesgue measure (see, for example,
Attali [[2](https://arxiv.org/html/2601.04900v1#bib.bib2 "Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models")], Duflo [[6](https://arxiv.org/html/2601.04900v1#bib.bib7 "Random iterative models")], and references therein). In many
such situations, existence of an invariant probability measure can
nevertheless be established by stability or Lyapunov–type arguments,
independently of any recurrence property.

This observation naturally raises the following question:
*does uniqueness of the invariant probability measure genuinely rely on
recurrence, or is it instead governed by more elementary structural properties
of the Markov kernel?*
From a measure–theoretic viewpoint, the fundamental obstruction to uniqueness
is the presence of nontrivial invariant measurable sets. This idea already
appears, at least implicitly, in early work of Breiman [[3](https://arxiv.org/html/2601.04900v1#bib.bib13 "The strong law of large numbers for a class of markov chains"), [4](https://arxiv.org/html/2601.04900v1#bib.bib14 "Strong ergodicity and the strong law of large numbers")], in the context of ergodic theorems and laws of large numbers for
Markov chains. In the classical theory, however, this structural viewpoint
remains tightly interwoven with dynamical assumptions ensuring ergodic
convergence.

The purpose of the present work is to isolate uniqueness as a *purely structural* problem.
Our main contribution is to identify *indecomposability* as a purely structural condition that prevents nontrivial invariant measurable decompositions and ensures uniqueness of invariant probability measures once existence is known. Indecomposability is defined solely in terms of absorbing measurable sets and does not involve any recurrence, accessibility, or return–time assumption.

On standard Borel spaces, indecomposability is strictly weaker than classical
irreducibility in general. The fact that the two notions coincide
*a posteriori* once existence of an invariant probability measure is
guaranteed should therefore be read as a clarification of the logical
structure: irreducibility is not an additional assumption required for
uniqueness, but a convenient and well–understood sufficient condition ensuring
indecomposability in classical settings.

Once existence of invariant probability measures is known, indecomposability
alone is sufficient to rule out the coexistence of several invariant
probability measures. More precisely, if uniqueness fails, then the state space
admits a nontrivial absorbing measurable subset. The proof relies on the mutual
singularity of distinct invariant ergodic measures and on the observation that
uniqueness follows whenever all invariant probability measures are forced to
charge a common reference measure. This mechanism is entirely
measure–theoretic and does not involve return–time estimates, regeneration
schemes, or regularity assumptions on the transition kernel.

From this perspective, classical irreducibility assumptions do not constitute a
dynamical requirement for uniqueness, but rather provide a transparent way of
making the underlying structural mechanism explicit. Under irreducibility, this
mechanism can be exhibited by introducing a resolvent–type kernel, defined as
a convex combination of the iterates of the original transition kernel. The
resulting one–step positivity property with respect to a σ\sigma–finite
reference measure forces all invariant probability measures to charge the same
measure and therefore enforces uniqueness.

Since every invariant probability measure of the original kernel is also
invariant for the resolvent kernel, uniqueness immediately transfers whenever
existence has been established by independent means. In particular, in the
classes of models considered in [[2](https://arxiv.org/html/2601.04900v1#bib.bib2 "Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models")], where existence follows from
stability arguments rather than recurrence, uniqueness becomes a direct
consequence of the present results.

The aim of this work is therefore not to strengthen classical ergodic theorems,
but to clarify the logical structure underlying uniqueness. From this
perspective, recurrence and regeneration emerge as genuinely dynamical
properties governing convergence and long–term behaviour, while uniqueness
appears as a structural consequence of indecomposability, revealed through a
one–step positivity mechanism acting at the level of invariant measures.

## 2 Main result

Let (E,ℬ)(E,\mathcal{B}) be a standard Borel space and let PP be a discrete-time
Markov kernel on (E,ℬ)(E,\mathcal{B}).

We introduce the structural notion that lies at the core of the uniqueness
mechanism.

###### Definition 1 (Indecomposability).

Let (E,ℬ)(E,\mathcal{B}) be a measurable space and let PP be a Markov kernel on (E,ℬ)(E,\mathcal{B}).
The kernel PP is said to be *indecomposable* if there exist no two disjoint nonempty
measurable sets A,B∈ℬA,B\in\mathcal{B} such that

|  |  |  |
| --- | --- | --- |
|  | P​(x,A)=1for all ​x∈A,P​(x,B)=1for all ​x∈B.P(x,A)=1\quad\text{for all }x\in A,\qquad P(x,B)=1\quad\text{for all }x\in B. |  |

Indecomposability isolates a purely structural obstruction to the uniqueness of invariant probability measures. Classical irreducibility assumptions are not required in what follows; they will only be invoked later as convenient sufficient conditions ensuring indecomposability in standard settings.

###### Remark 2.

Throughout the paper, the term “absorbing” refers to invariance in the forward
sense only, i.e. x∈A⇒P​(x,A)=1x\in A\Rightarrow P(x,A)=1. No backward or symmetric
invariance is assumed.

We first recall a key structural property of invariant ergodic measures. Although the following result can be derived from the ergodic decomposition theorem under standard assumptions, we include a direct proof since our goal is to isolate the measure-theoretic core of the uniqueness mechanism, without relying on convex-analytic or topological arguments on the space of invariant measures.

###### Lemma 3.

Let (E,ℬ)(E,\mathcal{B}) be a standard Borel space and let PP be a Markov kernel on (E,ℬ)(E,\mathcal{B}).
If PP admits two distinct invariant probability measures, then it admits two invariant probability measures that are mutually singular.

###### Proof.

Assume that PP admits two distinct invariant probability measures.
Let μ1\mu\_{1} and μ2\mu\_{2} be two such measures with μ1≠μ2\mu\_{1}\neq\mu\_{2}.
Then there exists a measurable set A∈ℬA\in\mathcal{B} such that
μ1​(A)≠μ2​(A)\mu\_{1}(A)\neq\mu\_{2}(A).

By the ergodic decomposition theorem, every invariant probability measure admits
a representation as a barycenter of invariant ergodic probability measures.
Since μ1≠μ2\mu\_{1}\neq\mu\_{2}, their ergodic decompositions differ, and there exist two
distinct invariant ergodic probability measures ν1\nu\_{1} and ν2\nu\_{2} such that
ν1\nu\_{1} appears with positive weight in the decomposition of μ1\mu\_{1} and ν2\nu\_{2}
appears with positive weight in the decomposition of μ2\mu\_{2}.
Since distinct invariant ergodic probability measures are mutually singular,
this yields two invariant probability measures that are mutually singular.

∎

###### Remark 4.

The singularity of distinct invariant ergodic probability measures, as well as the
extremality of ergodic measures, are classical results, often derived from the
Choquet simplex structure of the set of invariant probability measures; see, e.g.,
[[10](https://arxiv.org/html/2601.04900v1#bib.bib1 "Markov chains and stochastic stability"), [9](https://arxiv.org/html/2601.04900v1#bib.bib15 "Foundations of modern probability")].
The argument above relies only on standard measure–theoretic properties of
invariant measures and does not involve any trajectorywise ergodic theorem.

Lemma [3](https://arxiv.org/html/2601.04900v1#Thmtheorem3 "Lemma 3. ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels") shows that invariant ergodic measures are necessarily
extreme points of the convex set of invariant probability measures. We now record
a complementary observation, showing that ergodicity is automatic under uniqueness.

###### Proposition 5.

Let (E,ℬ)(E,\mathcal{B}) be a measurable space and let PP be a Markov kernel on (E,ℬ)(E,\mathcal{B}).
Assume that PP admits a unique invariant probability measure μ\mu.
Then μ\mu is ergodic, i.e. for any A∈ℬA\in\mathcal{B} such that

|  |  |  |
| --- | --- | --- |
|  | P​1A=1Aμ​-a.s.,P1\_{A}=1\_{A}\quad\mu\text{-a.s.}, |  |

one has μ​(A)∈{0,1}\mu(A)\in\{0,1\}.

###### Proof.

Assume by contradiction that there exists a measurable set A∈ℬA\in\mathcal{B} such that

|  |  |  |
| --- | --- | --- |
|  | P​𝟏A=𝟏Aμ​-a.s.and0<μ​(A)<1.P\mathbf{1}\_{A}=\mathbf{1}\_{A}\quad\mu\text{-a.s.}\qquad\text{and}\qquad 0<\mu(A)<1. |  |

Define two probability measures μ1\mu\_{1} and μ2\mu\_{2} on (E,ℬ)(E,\mathcal{B}) by

|  |  |  |
| --- | --- | --- |
|  | μ1​(B)=μ​(B∩A)μ​(A),μ2​(B)=μ​(B∩Ac)1−μ​(A),B∈ℬ.\mu\_{1}(B)=\frac{\mu(B\cap A)}{\mu(A)},\qquad\mu\_{2}(B)=\frac{\mu(B\cap A^{c})}{1-\mu(A)},\qquad B\in\mathcal{B}. |  |

Since P​𝟏A=𝟏AP\mathbf{1}\_{A}=\mathbf{1}\_{A} μ\mu-a.s. and 0<μ​(A)<10<\mu(A)<1, the measures μ1\mu\_{1} and
μ2\mu\_{2} are well defined invariant probability measures, with disjoint supports.
In particular, μ1≠μ2\mu\_{1}\neq\mu\_{2}, which contradicts the uniqueness assumption.
Therefore μ​(A)∈{0,1}\mu(A)\in\{0,1\} for every A∈ℬA\in\mathcal{B} such that
P​𝟏A=𝟏AP\mathbf{1}\_{A}=\mathbf{1}\_{A} μ\mu-almost surely, and μ\mu is ergodic.
∎

###### Remark 6.

Proposition [5](https://arxiv.org/html/2601.04900v1#Thmtheorem5 "Proposition 5. ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels") shows that ergodicity does not require
any additional assumption beyond uniqueness. In particular, no ergodic decomposition
or convex-analytic argument is needed to identify the invariant measure as ergodic
in the uniqueness regime.

We now turn to the complementary situation where several invariant probability measures
coexist.

###### Corollary 7.

Let (E,ℰ)(E,\mathcal{E}) be a measurable space and let PP be a Markov kernel on (E,ℰ)(E,\mathcal{E}).
If PP admits at least two distinct invariant probability measures, then it admits
two distinct invariant probability measures that are mutually singular.

###### Proof.

Assume that PP admits two distinct invariant probability measures μ1≠μ2\mu\_{1}\neq\mu\_{2}.

If both μ1\mu\_{1} and μ2\mu\_{2} are ergodic, then by Lemma [3](https://arxiv.org/html/2601.04900v1#Thmtheorem3 "Lemma 3. ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels")
they are mutually singular and the conclusion holds.

Otherwise, at least one invariant probability measure is not ergodic.
Without loss of generality, assume that μ1\mu\_{1} is not ergodic.
Then there exists a measurable set A∈ℰA\in\mathcal{E} such that

|  |  |  |
| --- | --- | --- |
|  | P​𝟏A=𝟏Aμ1​-a.s.and0<μ1​(A)<1.P\mathbf{1}\_{A}=\mathbf{1}\_{A}\quad\mu\_{1}\text{-a.s.}\qquad\text{and}\qquad 0<\mu\_{1}(A)<1. |  |

Define the probability measures

|  |  |  |
| --- | --- | --- |
|  | ν1​(B):=μ1​(B∩A)μ1​(A),ν2​(B):=μ1​(B∩Ac)1−μ1​(A),B∈ℰ.\nu\_{1}(B):=\frac{\mu\_{1}(B\cap A)}{\mu\_{1}(A)},\qquad\nu\_{2}(B):=\frac{\mu\_{1}(B\cap A^{c})}{1-\mu\_{1}(A)},\qquad B\in\mathcal{E}. |  |

Since P​𝟏A=𝟏AP\mathbf{1}\_{A}=\mathbf{1}\_{A} μ1\mu\_{1}-almost surely, the measures ν1\nu\_{1} and
ν2\nu\_{2} are invariant probability measures for PP.
Moreover, they have disjoint supports and are therefore mutually singular.
∎

###### Remark 8.

The proof relies only on absolute continuity and invariant sets, together with
standard structural properties of invariant measures.
Ergodicity appears here as extremality within a fixed domination class.

We can now state and prove the main result.

###### Theorem 9 (Uniqueness via indecomposability).

Let PP be a Markov kernel on a standard Borel space (E,ℬ)(E,\mathcal{B}).
If PP is indecomposable, then PP admits at most one invariant probability
measure.

###### Proof.

Assume by contradiction that PP admits two distinct invariant probability measures.
By Corollary [7](https://arxiv.org/html/2601.04900v1#Thmtheorem7 "Corollary 7. ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"), there exist two mutually singular invariant probability measures
μ1\mu\_{1} and μ2\mu\_{2}. Hence there exists A∈ℬ​(E)A\in\mathcal{B}(E) such that

|  |  |  |
| --- | --- | --- |
|  | μ1​(A)=1,μ2​(A)=0.\mu\_{1}(A)=1,\qquad\mu\_{2}(A)=0. |  |

By invariance of μ1\mu\_{1} and μ2\mu\_{2},

|  |  |  |
| --- | --- | --- |
|  | μi​(A)=∫EP​(x,A)​μi​(d​x),i=1,2.\mu\_{i}(A)=\int\_{E}P(x,A)\,\mu\_{i}(dx),\qquad i=1,2. |  |

Since 0≤P​(x,A)≤10\leq P(x,A)\leq 1, it follows that

|  |  |  |
| --- | --- | --- |
|  | P​(x,A)=1μ1​-a.s.,P​(x,A)=0μ2​-a.s.P(x,A)=1\ \ \mu\_{1}\text{-a.s.},\qquad P(x,A)=0\ \ \mu\_{2}\text{-a.s.} |  |

Define

|  |  |  |
| --- | --- | --- |
|  | B1:=⋂n≥0{x∈E:Pn​(x,A)=1}.B\_{1}:=\bigcap\_{n\geq 0}\{x\in E:\;P^{n}(x,A)=1\}. |  |

For every n≥0n\geq 0, invariance yields

|  |  |  |
| --- | --- | --- |
|  | ∫EPn​(x,A)​μ1​(d​x)=μ1​(A)=1,∫EPn​(x,A)​μ2​(d​x)=μ2​(A)=0,\int\_{E}P^{n}(x,A)\,\mu\_{1}(dx)=\mu\_{1}(A)=1,\qquad\int\_{E}P^{n}(x,A)\,\mu\_{2}(dx)=\mu\_{2}(A)=0, |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | μ1​({x:Pn​(x,A)=1})=1,μ2​({x:Pn​(x,A)=1})=0.\mu\_{1}\bigl(\{x:\,P^{n}(x,A)=1\}\bigr)=1,\qquad\mu\_{2}\bigl(\{x:\,P^{n}(x,A)=1\}\bigr)=0. |  |

Taking the intersection over n≥0n\geq 0 gives

|  |  |  |
| --- | --- | --- |
|  | μ1​(B1)=1,μ2​(B1)=0.\mu\_{1}(B\_{1})=1,\qquad\mu\_{2}(B\_{1})=0. |  |

Let x∈B1x\in B\_{1}. For every n≥0n\geq 0,

|  |  |  |
| --- | --- | --- |
|  | 1=Pn+1​(x,A)=∫EPn​(y,A)​P​(x,d​y).1=P^{n+1}(x,A)=\int\_{E}P^{n}(y,A)\,P(x,dy). |  |

Since 0≤Pn​(y,A)≤10\leq P^{n}(y,A)\leq 1, this implies

|  |  |  |
| --- | --- | --- |
|  | P​(x,{y:Pn​(y,A)=1})=1for all ​n≥0.P\bigl(x,\{y:\,P^{n}(y,A)=1\}\bigr)=1\quad\text{for all }n\geq 0. |  |

Taking the intersection over n≥0n\geq 0, we obtain

|  |  |  |
| --- | --- | --- |
|  | P​(x,B1)=1for all ​x∈B1.P(x,B\_{1})=1\qquad\text{for all }x\in B\_{1}. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | B2:=⋂n≥0{x∈E:Pn​(x,Ac)=1}.B\_{2}:=\bigcap\_{n\geq 0}\{x\in E:\;P^{n}(x,A^{c})=1\}. |  |

For every n≥0n\geq 0, invariance yields

|  |  |  |
| --- | --- | --- |
|  | ∫EPn​(x,Ac)​μ2​(d​x)=μ2​(Ac)=1,∫EPn​(x,Ac)​μ1​(d​x)=μ1​(Ac)=0,\int\_{E}P^{n}(x,A^{c})\,\mu\_{2}(dx)=\mu\_{2}(A^{c})=1,\qquad\int\_{E}P^{n}(x,A^{c})\,\mu\_{1}(dx)=\mu\_{1}(A^{c})=0, |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | μ2​({x:Pn​(x,Ac)=1})=1,μ1​({x:Pn​(x,Ac)=1})=0.\mu\_{2}\bigl(\{x:\,P^{n}(x,A^{c})=1\}\bigr)=1,\qquad\mu\_{1}\bigl(\{x:\,P^{n}(x,A^{c})=1\}\bigr)=0. |  |

Taking the intersection over n≥0n\geq 0 gives

|  |  |  |
| --- | --- | --- |
|  | μ2​(B2)=1,μ1​(B2)=0.\mu\_{2}(B\_{2})=1,\qquad\mu\_{1}(B\_{2})=0. |  |

Let x∈B2x\in B\_{2}. For every n≥0n\geq 0,

|  |  |  |
| --- | --- | --- |
|  | 1=Pn+1​(x,Ac)=∫EPn​(y,Ac)​P​(x,d​y).1=P^{n+1}(x,A^{c})=\int\_{E}P^{n}(y,A^{c})\,P(x,dy). |  |

Since 0≤Pn​(y,Ac)≤10\leq P^{n}(y,A^{c})\leq 1, this implies

|  |  |  |
| --- | --- | --- |
|  | P​(x,{y:Pn​(y,Ac)=1})=1for all ​n≥0.P\bigl(x,\{y:\,P^{n}(y,A^{c})=1\}\bigr)=1\quad\text{for all }n\geq 0. |  |

Taking the intersection over n≥0n\geq 0, we obtain

|  |  |  |
| --- | --- | --- |
|  | P​(x,B2)=1for all ​x∈B2.P(x,B\_{2})=1\qquad\text{for all }x\in B\_{2}. |  |

Thus B1B\_{1} and B2B\_{2} are disjoint nontrivial absorbing measurable sets, contradicting the indecomposability of PP.
∎

###### Remark 10.

On a standard Borel space, ϕ\phi–irreducibility in the sense of Meyn–Tweedie is a
strictly stronger property than indecomposability, since ϕ\phi–irreducibility
rules out the existence of nontrivial absorbing measurable sets.
In general, the converse implication does not hold, as indecomposability alone
does not preclude purely transient behavior.
However, if an invariant probability measure exists, the structural decomposition
theory of [[10](https://arxiv.org/html/2601.04900v1#bib.bib1 "Markov chains and stochastic stability"), Section 4.2] implies that indecomposability excludes
the presence of more than one closed communicating class and therefore enforces
irreducibility with respect to a maximal irreducibility measure ψ\psi in the sense
of Meyn–Tweedie. In this sense, indecomposability and ϕ\phi–irreducibility become
equivalent once the existence of an invariant probability measure is guaranteed.
From this perspective, indecomposability identifies a purely structural obstruction
to uniqueness of invariant probability measures, while stronger assumptions—such
as the existence of small or petite sets or additional regularity of the transition
kernel—are only required to address recurrence and ergodic convergence properties.

### 2.1 Quasi–Feller regularity

We now recall the notion of quasi–Feller regularity introduced in [[2](https://arxiv.org/html/2601.04900v1#bib.bib2 "Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models")].
This notion provides a structural framework allowing one to handle transition
kernels that are not Feller by factoring the dynamics through a Feller (or strong
Feller) kernel on an auxiliary space.

###### Definition 11 (Quasi–Feller and Quasi–strong Feller, after [[2](https://arxiv.org/html/2601.04900v1#bib.bib2 "Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models")]).

Let EE be a Polish space and let PP be a Markov transition kernel on EE.
The kernel PP is said to be *quasi–Feller* if there exist

* •

  a Polish space WW,
* •

  a Borel measurable mapping H:E→WH:E\to W such that H​(K)H(K) is compact in WW
  for every compact set K⊂EK\subset E,
* •

  a Markov transition kernel Q:W×ℬ​(E)→[0,1]Q:W\times\mathcal{B}(E)\to[0,1]

satisfying the following properties:

1. (i)

   (Feller property of QQ)
   For every f∈Cb​(E)f\in C\_{b}(E), the function

   |  |  |  |
   | --- | --- | --- |
   |  | Q​f:w↦∫Ef​(y)​Q​(w,d​y)Qf:w\mapsto\int\_{E}f(y)\,Q(w,dy) |  |

   belongs to Cb​(W)C\_{b}(W).
2. (ii)

   (Factorization)
   For every bounded measurable function ff on EE and every x∈Ex\in E,

   |  |  |  |
   | --- | --- | --- |
   |  | P​f​(x)=Q​f​(H​(x)),Pf(x)=Qf(H(x)), |  |

   equivalently,

   |  |  |  |
   | --- | --- | --- |
   |  | P​(x,⋅)=Q​(H​(x),⋅).P(x,\cdot)=Q(H(x),\cdot). |  |
3. (iii)

   (Essential continuity of HH)
   For every invariant probability measure μ\mu of PP, one has

   |  |  |  |
   | --- | --- | --- |
   |  | μ​(DH)=0,\mu(D\_{H})=0, |  |

   where DHD\_{H} denotes the set of discontinuity points of HH.

The kernel PP is said to be *quasi–strong Feller* if, in addition,
the kernel QQ is strong Feller, i.e. for every bounded measurable function
ff on EE, the function Q​fQf is continuous on WW.

This framework strictly generalizes the classical Feller and strong Feller
settings and naturally arises in many non–Feller models with discontinuous
dynamics.

We emphasize that the following theorem provides an independent existence and invariance statement. Although it is not required for the subsequent stability results, it isolates a measure–theoretic regularity condition underlying the quasi–Feller framework.

###### Theorem 12 (Existence and invariance under tightness of iterated kernels).

Let EE be a Polish space and let PP be a Markov transition kernel on EE.
Fix x∈Ex\in E and define the averaged iterates

|  |  |  |
| --- | --- | --- |
|  | νnx:=1n​∑k=0n−1Pk​(x,⋅),n≥1.\nu\_{n}^{x}:=\frac{1}{n}\sum\_{k=0}^{n-1}P^{k}(x,\cdot),\qquad n\geq 1. |  |

Assume that:

1. 1.

   the sequence (νnx)n≥1(\nu\_{n}^{x})\_{n\geq 1} is tight in 𝒫​(E)\mathcal{P}(E);
2. 2.

   (*essential regularity along limit measures*)
   for every weak limit point μ\mu of (νnx)n≥1(\nu\_{n}^{x})\_{n\geq 1} and every
   f∈Cb​(E)f\in C\_{b}(E), there exists a bounded Borel function g:E→ℝg:E\to\mathbb{R} such that

   |  |  |  |
   | --- | --- | --- |
   |  | g=P​fμ​–a.s.andμ​(Dg)=0,g=Pf\quad\mu\text{--a.s.}\qquad\text{and}\qquad\mu(D\_{g})=0, |  |

   where DgD\_{g} denotes the set of discontinuity points of gg.

Then (νnx)(\nu\_{n}^{x}) admits at least one weak limit point, and every such limit point
μ\mu is an invariant probability measure for PP.
In particular, PP admits at least one invariant probability measure.

###### Remark 13.

This condition should be understood as an a priori version of the essential
quasi–Feller principle, stated along limit measures that are not assumed
to be invariant.

###### Proof.

By tightness, there exists a subsequence (nj)j≥1(n\_{j})\_{j\geq 1} such that
νnjx⇒μ\nu\_{n\_{j}}^{x}\Rightarrow\mu for some probability measure μ\mu on EE.
Fix f∈Cb​(E)f\in C\_{b}(E) and let gg be given by assumption (2).

Since gg is bounded Borel and μ​(Dg)=0\mu(D\_{g})=0, the portmanteau theorem yields

|  |  |  |
| --- | --- | --- |
|  | ∫g​𝑑νnjx→j→∞∫g​𝑑μ.\int g\,d\nu\_{n\_{j}}^{x}\xrightarrow[j\to\infty]{}\int g\,d\mu. |  |

Since ff is continuous, we also have

|  |  |  |
| --- | --- | --- |
|  | ∫f​𝑑νnjx→j→∞∫f​𝑑μ.\int f\,d\nu\_{n\_{j}}^{x}\xrightarrow[j\to\infty]{}\int f\,d\mu. |  |

On the other hand, for all n≥1n\geq 1,

|  |  |  |
| --- | --- | --- |
|  | ∫P​f​𝑑νnx−∫f​𝑑νnx=1n​(Pn​f​(x)−f​(x)),\int Pf\,d\nu\_{n}^{x}-\int f\,d\nu\_{n}^{x}=\frac{1}{n}\bigl(P^{n}f(x)-f(x)\bigr), |  |

which converges to 0 as n→∞n\to\infty since ff is bounded.
Passing to the subsequence (nj)(n\_{j}) yields

|  |  |  |
| --- | --- | --- |
|  | limj→∞∫P​f​𝑑νnjx=limj→∞∫f​𝑑νnjx=∫f​𝑑μ.\lim\_{j\to\infty}\int Pf\,d\nu\_{n\_{j}}^{x}=\lim\_{j\to\infty}\int f\,d\nu\_{n\_{j}}^{x}=\int f\,d\mu. |  |

Finally, since g=P​fg=Pf μ\mu–a.s., we have ∫g​𝑑μ=∫P​f​𝑑μ\int g\,d\mu=\int Pf\,d\mu,
and therefore

|  |  |  |
| --- | --- | --- |
|  | ∫P​f​𝑑μ=∫f​𝑑μfor all ​f∈Cb​(E).\int Pf\,d\mu=\int f\,d\mu\qquad\text{for all }f\in C\_{b}(E). |  |

This proves that μ\mu is invariant for PP.
∎

The following example, adapted from Meyn–Tweedie, shows that the regularity condition introduced in Theorem [12](https://arxiv.org/html/2601.04900v1#Thmtheorem12 "Theorem 12 (Existence and invariance under tightness of iterated kernels). ‣ 2.1 Quasi–Feller regularity ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels") may hold even when the quasi–Feller property fails.

###### Example 14 (Essential regularity without quasi-Feller).

Let E=ℝE=\mathbb{R}, let ε∈(0,1)\varepsilon\in(0,1), and let ν\nu be a probability measure
absolutely continuous with respect to Lebesgue measure.
Fix two distinct irrational numbers α≠β\alpha\neq\beta, and define

|  |  |  |
| --- | --- | --- |
|  | T​(x)={α,x∈ℚ,β,x∉ℚ.T(x)=\begin{cases}\alpha,&x\in\mathbb{Q},\\ \beta,&x\notin\mathbb{Q}.\end{cases} |  |

Note that TT is discontinuous at every point, hence DT=ℝD\_{T}=\mathbb{R}.
Define the Markov kernel

|  |  |  |
| --- | --- | --- |
|  | P​(x,A)=(1−ε)​ 1A​(T​(x))+ε​ν​(A),x∈E,A∈ℬ​(E).P(x,A)=(1-\varepsilon)\,\mathbf{1}\_{A}(T(x))+\varepsilon\,\nu(A),\qquad x\in E,\ A\in\mathcal{B}(E). |  |

We first observe that the quasi-Feller property fails.
Indeed, since DT=ℝD\_{T}=\mathbb{R}, we have μ​(DT)=1\mu(D\_{T})=1 for any probability measure μ\mu.
Therefore the condition μ​(DH)=0\mu(D\_{H})=0 required in Definition [11](https://arxiv.org/html/2601.04900v1#Thmtheorem11 "Definition 11 (Quasi–Feller and Quasi–strong Feller, after [2]). ‣ 2.1 Quasi–Feller regularity ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels") cannot be satisfied
for any factorization involving TT, and PP is not quasi-Feller.

We now verify the essential regularity condition of Theorem [12](https://arxiv.org/html/2601.04900v1#Thmtheorem12 "Theorem 12 (Existence and invariance under tightness of iterated kernels). ‣ 2.1 Quasi–Feller regularity ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
Let μ\mu be any weak limit point of the empirical measures
νnx=1n​∑k=1nPk​(x,⋅)\nu\_{n}^{x}=\frac{1}{n}\sum\_{k=1}^{n}P^{k}(x,\cdot).
By Theorem [12](https://arxiv.org/html/2601.04900v1#Thmtheorem12 "Theorem 12 (Existence and invariance under tightness of iterated kernels). ‣ 2.1 Quasi–Feller regularity ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"), μ\mu is an invariant probability measure for PP.
For every x∈Ex\in E,

|  |  |  |
| --- | --- | --- |
|  | P​(x,ℚ)=(1−ε)​𝟏ℚ​(T​(x))+ε​ν​(ℚ)=0,P(x,\mathbb{Q})=(1-\varepsilon)\mathbf{1}\_{\mathbb{Q}}(T(x))+\varepsilon\nu(\mathbb{Q})=0, |  |

since T​(x)∈{α,β}⊂ℝ∖ℚT(x)\in\{\alpha,\beta\}\subset\mathbb{R}\setminus\mathbb{Q} and
ν​(ℚ)=0\nu(\mathbb{Q})=0.
By invariance of μ\mu,

|  |  |  |
| --- | --- | --- |
|  | μ​(ℚ)=∫EP​(x,ℚ)​μ​(d​x)=0.\mu(\mathbb{Q})=\int\_{E}P(x,\mathbb{Q})\,\mu(dx)=0. |  |

Hence T​(x)=βT(x)=\beta holds μ\mu-almost surely.
For any f∈Cb​(E)f\in C\_{b}(E), it follows that

|  |  |  |
| --- | --- | --- |
|  | P​f​(x)=(1−ε)​f​(T​(x))+ε​∫f​𝑑ν=(1−ε)​f​(β)+ε​∫f​𝑑ν,μ​-a.s.Pf(x)=(1-\varepsilon)f(T(x))+\varepsilon\int f\,d\nu=(1-\varepsilon)f(\beta)+\varepsilon\int f\,d\nu,\quad\mu\text{-a.s.} |  |

Thus P​fPf is μ\mu-almost surely equal to the constant function

|  |  |  |
| --- | --- | --- |
|  | g≡(1−ε)​f​(β)+ε​∫f​𝑑ν,g\equiv(1-\varepsilon)f(\beta)+\varepsilon\int f\,d\nu, |  |

which is continuous and satisfies μ​(Dg)=0\mu(D\_{g})=0.
This proves that the essential regularity condition of Theorem [12](https://arxiv.org/html/2601.04900v1#Thmtheorem12 "Theorem 12 (Existence and invariance under tightness of iterated kernels). ‣ 2.1 Quasi–Feller regularity ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels") holds,
while the quasi-Feller property fails.

### 2.2 Almost sure tightness of trajectories

As a preparatory step, we recall a classical criterion ensuring almost sure
tightness of empirical occupation measures.
In the quasi–Feller framework, long–time control of the trajectories is
typically obtained through Lyapunov–Hájek type drift conditions, which imply
that the Markov chain spends an asymptotically negligible proportion of time
outside compact subsets of the state space.

More precisely, under suitable Lyapunov assumptions, the empirical occupation
measures

|  |  |  |
| --- | --- | --- |
|  | Λn​(ω,⋅):=1n​∑k=0n−1δXk​(ω)​(⋅)\Lambda\_{n}(\omega,\cdot)\;:=\;\frac{1}{n}\sum\_{k=0}^{n-1}\delta\_{X\_{k}(\omega)}(\cdot) |  |

are almost surely tight under PxP\_{x}, for every initial condition x∈Ex\in E.

This result is classical and follows from a standard Lyapunov–martingale
argument; see, for instance, [[7](https://arxiv.org/html/2601.04900v1#bib.bib11 "Méthodes récursives aléatoires"), Appendix H] or
[[1](https://arxiv.org/html/2601.04900v1#bib.bib12 "Méthode de stabilité pour des chaînes de markov non fellériennes")]. Since this argument is orthogonal to the main
contribution of the present paper, we do not reproduce the proof here.

### 2.3 Stability via uniqueness

We now combine the tightness property recalled above with the uniqueness result
obtained in Section 2.
Recall that the notion of stability was introduced by
Duflo [[6](https://arxiv.org/html/2601.04900v1#bib.bib7 "Random iterative models")] and refers to almost sure convergence of time averages for
bounded continuous observables.

###### Definition 15 (Stability in the sense of Duflo).

A Markov chain (Xn)n≥0(X\_{n})\_{n\geq 0} is said to be *stable* if there exists a
probability measure μ\mu such that, for every x∈Ex\in E and every
f∈Cb​(E)f\in C\_{b}(E),

|  |  |  |
| --- | --- | --- |
|  | 1n​∑k=0n−1f​(Xk)→n→∞Px​-a.s.∫f​𝑑μ.\frac{1}{n}\sum\_{k=0}^{n-1}f(X\_{k})\;\xrightarrow[n\to\infty]{P\_{x}\text{-a.s.}}\;\int f\,d\mu. |  |

###### Remark 16.

Stability does not imply that the limiting measure μ\mu is invariant.
Counterexamples can be found in [[1](https://arxiv.org/html/2601.04900v1#bib.bib12 "Méthode de stabilité pour des chaînes de markov non fellériennes")].
As shown below, quasi–Feller regularity provides a sufficient structural
condition ensuring invariance, consistently with the essential quasi–Feller
principle stated above.

###### Theorem 17 (Stability under uniqueness).

Assume that:

1. 1.

   the transition kernel PP is quasi–Feller;
2. 2.

   the empirical occupation measures (Λn)(\Lambda\_{n}) are PxP\_{x}–almost surely
   tight for every x∈Ex\in E;
3. 3.

   PP admits a unique invariant probability measure μ\mu.

Then the Markov chain (Xn)n≥0(X\_{n})\_{n\geq 0} is stable in the sense of Duflo.

###### Proof.

The result follows from Theorem H.2 in [[1](https://arxiv.org/html/2601.04900v1#bib.bib12 "Méthode de stabilité pour des chaînes de markov non fellériennes")].
∎

### 2.4 From Duflo stability to positive Harris recurrence

We now explain how a strengthened version of the essential regularity condition
allows one to extend Duflo stability from bounded continuous functions to bounded
Borel functions, without invoking any structural quasi–strong Feller
factorization.

###### Proposition 18 (Ergodic averages under essential strong regularity).

Let (Xn)n≥0(X\_{n})\_{n\geq 0} be a Markov chain on a Polish space EE with transition kernel
PP. Assume that:

1. 1.

   the chain is stable in the sense of Duflo;
2. 2.

   μ\mu is an invariant probability measure for PP;
3. 3.

   (*essential strong regularity*)
   for every bounded Borel function f∈ℬb​(E)f\in\mathcal{B}\_{b}(E), there exists a bounded
   continuous function g∈Cb​(E)g\in C\_{b}(E) such that

   |  |  |  |
   | --- | --- | --- |
   |  | g=P​fμ​–a.s.andμ​(Dg)=0.g=Pf\quad\mu\text{--a.s.}\qquad\text{and}\qquad\mu(D\_{g})=0. |  |

Then, for every bounded Borel function f∈ℬb​(E)f\in\mathcal{B}\_{b}(E) and every x∈Ex\in E,

|  |  |  |
| --- | --- | --- |
|  | 1n​∑k=0n−1f​(Xk)→n→∞Px​-a.s.∫f​𝑑μ.\frac{1}{n}\sum\_{k=0}^{n-1}f(X\_{k})\xrightarrow[n\to\infty]{P\_{x}\text{-a.s.}}\int f\,d\mu. |  |

### 2.5 Harris-recurrence of Essential Feller Transition Kernel

Under Quasi-Feller regularity and assuming that the support of a maximal
irreducibility measure ψ\psi has nonempty interior—together with classical
assumptions ensuring tightness from all initial conditions—positive Harris
recurrence is established in [[2](https://arxiv.org/html/2601.04900v1#bib.bib2 "Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models")] without assuming the existence of
a petite set. Rather, under these hypotheses, the existence of a petite set is
*derived* as an intermediate result, which then allows one to re-enter the
classical Meyn–Tweedie framework *a posteriori*.

In the present setting, essential Feller regularity and tightness ensure the
existence of an invariant probability measure μ\mu. Moreover, the
indecomposability assumption rules out the presence of disjoint absorbing
components and therefore implies ψ\psi-irreducibility for a maximal
irreducibility measure ψ\psi in the sense of Meyn–Tweedie. In this context, the
assumption that supp⁡(ψ)\operatorname{supp}(\psi) has nonempty interior plays exactly
the same role as in [[2](https://arxiv.org/html/2601.04900v1#bib.bib2 "Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models")]: combined with essential Feller regularity,
it allows one to recover the existence of a petite set, and hence to establish
Harris recurrence within the Meyn–Tweedie framework.

Remark.
At this stage, the role of the Meyn–Tweedie framework is to provide an
accessibility and regeneration mechanism through which stability properties can
be upgraded into recurrence properties. It is therefore natural to ask whether
positive Harris recurrence alone already enforces the essential regularity
condition introduced above.

Remark.
Beyond its conceptual interest, the essential regularity framework appears to
cover a broad class of examples encountered in practice. Indeed, many Markov
kernels that fail to satisfy classical Feller or quasi–Feller assumptions arise
from the combination of a highly irregular deterministic component with a
smoothing noise term. In such situations, although standard regularity
properties may be violated, the transition kernel often satisfies the essential
regularity condition along invariant or limit measures. The following example
shows that this conclusion is not universal, even under a strong
Meyn–Tweedie-type minorization condition.

###### Example 19 (Positive Harris recurrence without essential regularity).

Let E=[0,1]E=[0,1] endowed with its Borel σ\sigma–field and let ν\nu denote the
Lebesgue probability measure on EE. Fix ε∈(0,1)\varepsilon\in(0,1).
Let C⊂EC\subset E be a closed set with empty interior and positive Lebesgue
measure (for instance a fat Cantor set). Define the measurable mapping
T:E→{0,1}T:E\to\{0,1\} by

|  |  |  |
| --- | --- | --- |
|  | T​(x)={0,x∈C,1,x∈Cc,T(x)=\begin{cases}0,&x\in C,\\ 1,&x\in C^{c},\end{cases} |  |

and define a Markov transition kernel PP on EE by

|  |  |  |
| --- | --- | --- |
|  | P​(x,A)=(1−ε)​ 1A​(T​(x))+ε​ν​(A),x∈E,A∈ℬ​(E).P(x,A)=(1-\varepsilon)\,\mathbf{1}\_{A}(T(x))+\varepsilon\,\nu(A),\qquad x\in E,\ A\in\mathcal{B}(E). |  |

Harris recurrence.
Since P​(x,⋅)≥ε​ν​(⋅)P(x,\cdot)\geq\varepsilon\nu(\cdot) for all x∈Ex\in E, the chain satisfies
a uniform Doeblin minorization.
In particular, it is ν\nu–irreducible and the whole space EE is a small set in
the sense of Meyn–Tweedie.
As a consequence, the chain is positive Harris recurrent and admits a unique
invariant probability measure π\pi.

Failure of essential regularity.
Let f∈Cb​(E)f\in C\_{b}(E) be such that f​(0)≠f​(1)f(0)\neq f(1). Then

|  |  |  |
| --- | --- | --- |
|  | P​f​(x)=(1−ε)​f​(T​(x))+ε​∫Ef​𝑑ν={a,x∈C,b,x∈Cc,a≠b.Pf(x)=(1-\varepsilon)f(T(x))+\varepsilon\int\_{E}f\,d\nu=\begin{cases}a,&x\in C,\\ b,&x\in C^{c},\end{cases}\qquad a\neq b. |  |

Since CC is closed with empty interior, one has ∂C=C\partial C=C, and therefore
every point of CC is a point of discontinuity of P​fPf. Moreover, the invariant
probability measure π\pi satisfies π≥ε​ν\pi\geq\varepsilon\nu, so that
π​(C)>0\pi(C)>0. Consequently,

|  |  |  |
| --- | --- | --- |
|  | π​(DP​f)>0.\pi(D\_{Pf})>0. |  |

It follows that there exists no bounded Borel function gg such that
g=P​fg=Pf π\pi–almost surely and π​(Dg)=0\pi(D\_{g})=0. Hence the essential regularity
condition fails for this kernel.

###### Remark 20.

This example shows that positive Harris recurrence does not imply essential
regularity, even in a compact state space and under a strong Doeblin-type
minorization.
It illustrates that the Meyn–Tweedie framework and the essential regularity
approach address genuinely distinct aspects of the long–time behavior of
Markov chains: the former focuses on recurrence and regeneration properties,
while the latter is tailored to ergodic properties of time averages.

## 3 Further remarks

###### Remark 21 (A topological interpretation).

In many continuous–state models, the positivity mechanism underlying the
uniqueness results of this paper can be verified through topological support
properties of the transition kernel, providing concrete sufficient conditions
for indecomposability.

For instance, assume that there exists a closed set F⊂EF\subset E such that every
invariant probability measure is supported on FF, and that for all x∈Fx\in F
there exists n≥1n\geq 1 such that the support of Pn​(x,⋅)P^{n}(x,\cdot) has nonempty interior
relative to FF. Then any σ\sigma–finite measure ψ\psi charging open subsets of
FF is necessarily charged by all invariant probability measures. Since distinct
invariant ergodic measures are mutually singular, uniqueness follows from the
impossibility for two such measures to both charge the same reference measure.

Such arguments show that indecomposability, and hence uniqueness, may be
established from topological considerations alone, without requiring full
ϕ\phi–irreducibility on the whole state space.

###### Remark 22 (Uniqueness without recurrence).

The arguments developed in this paper do not rely on any recurrence assumption
for the original Markov kernel. In particular, uniqueness may hold whenever an
invariant probability measure exists, even if the chain is not positive
recurrent.

This contrasts with classical approaches based on Harris recurrence, where
uniqueness is typically obtained together with strong ergodic properties. The
present results show that these notions can be separated: recurrence is a
dynamical property governing long–time returns, while uniqueness emerges here as
a purely structural consequence of indecomposability, revealed through the
one–step positivity mechanism induced by the resolvent kernel.

###### Remark 23 (On geometric convergence under additional contraction assumptions).

The present work deliberately focuses on existence and uniqueness of invariant
probability measures, without addressing quantitative rates of convergence.
Nevertheless, stronger ergodic properties can be recovered under additional
contraction assumptions.

For instance, consider a Markov chain of the form

|  |  |  |
| --- | --- | --- |
|  | Xn+1=f​(Xn)+εn+1,X\_{n+1}=f(X\_{n})+\varepsilon\_{n+1}, |  |

where (εn)n≥1(\varepsilon\_{n})\_{n\geq 1} are i.i.d. random variables whose law admits a
density with respect to Lebesgue measure. Assume that the chain satisfies a
Lyapunov drift condition

|  |  |  |
| --- | --- | --- |
|  | P​V≤α​V+b,α<1,PV\leq\alpha V+b,\qquad\alpha<1, |  |

with relatively compact sublevel sets, and that there exist R>0R>0 and ρ<1\rho<1
such that

|  |  |  |
| --- | --- | --- |
|  | V​(x),V​(y)≤R⟹Wd​(P​(x,⋅),P​(y,⋅))≤ρ​d​(x,y),V(x),V(y)\leq R\quad\Longrightarrow\quad W\_{d}\bigl(P(x,\cdot),P(y,\cdot)\bigr)\leq\rho\,d(x,y), |  |

for some bounded distance dd.

Then the chain converges geometrically fast to its invariant distribution in a
Wasserstein distance associated with dd (possibly after a suitable Lyapunov
weighting). This illustrates that geometric ergodicity relies on a genuine
contraction property, which is logically independent of the uniqueness mechanism
isolated in the present work.

###### Remark 24 (Relation with ergodic decomposition).

Invariant probability measures admit a decomposition into ergodic components,
and distinct invariant ergodic measures are mutually singular. The contribution
of the present work is to show that, under the positivity mechanism induced by the
resolvent kernel, all invariant probability measures are forced to charge a
common σ\sigma–finite reference measure.

This structural constraint prevents the coexistence of several ergodic
components and therefore yields uniqueness. From this perspective, the resolvent
kernel acts as a device that transforms finite–time reachability into a one–step
positivity constraint at the level of invariant measures.

## 4 Conclusion

The main contribution of this paper is to identify *indecomposability* as a
purely structural condition ensuring uniqueness of invariant probability
measures for discrete–time Markov kernels. We show that, on a standard Borel
space, indecomposability alone is sufficient to rule out the coexistence of
several invariant probability measures, independently of any recurrence,
regeneration or ergodic convergence property, provided existence is known.

A key observation is that classical irreducibility assumptions are not essential
for uniqueness in themselves, but rather provide convenient sufficient
conditions for indecomposability. This allows uniqueness to be separated
conceptually from dynamical notions such as Harris recurrence or minorization,
which are traditionally used to derive uniqueness together with convergence
properties.

We further show that, under irreducibility, indecomposability can be enforced
through a resolvent–type kernel. The resolvent transforms finite–time
reachability into a one–step positivity property at the level of invariant
measures, forcing all invariant probability measures to charge a common
σ\sigma–finite reference measure. Since distinct invariant ergodic measures
are mutually singular, this mechanism excludes the possibility of multiple
ergodic components and yields uniqueness without any appeal to return–time
estimates or petite set constructions.

From a broader perspective, the present results clarify the respective roles of
structural and dynamical assumptions in the theory of invariant measures.
Recurrence, regeneration and minorization govern long–term behaviour and
ergodic convergence, while uniqueness emerges here as a structural consequence
of indecomposability. This viewpoint complements the quasi–Feller approach
of [[2](https://arxiv.org/html/2601.04900v1#bib.bib2 "Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models")], which addresses existence and stability for non–Feller
models, and leads to a more modular understanding of invariant probability
measures for a wide class of discrete–time Markov chains, including
discontinuous and non–regular dynamics.

## References

* [1]
  J. Attali (1999)
  Méthode de stabilité pour des chaînes de markov non fellériennes.
  Ph.D. Thesis, Université Paris I Panthéon Sorbonne, (french).
  Cited by: [§2.2](https://arxiv.org/html/2601.04900v1#S2.SS2.p3.1 "2.2 Almost sure tightness of trajectories ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [§2.3](https://arxiv.org/html/2601.04900v1#S2.SS3.1.p1.1 "Proof. ‣ 2.3 Stability via uniqueness ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [Remark 16](https://arxiv.org/html/2601.04900v1#Thmtheorem16.p1.1 "Remark 16. ‣ 2.3 Stability via uniqueness ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [2]
  J. Attali (2004)
  Ergodicity of a certain class of non-feller models: applications to ARCH and Markov switching models.
  ESAIM: Probability and Statistics 8,  pp. 76–86.
  Cited by: [§1](https://arxiv.org/html/2601.04900v1#S1.p3.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [§1](https://arxiv.org/html/2601.04900v1#S1.p9.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [§2.1](https://arxiv.org/html/2601.04900v1#S2.SS1.p1.1 "2.1 Quasi–Feller regularity ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [§2.5](https://arxiv.org/html/2601.04900v1#S2.SS5.p1.1 "2.5 Harris-recurrence of Essential Feller Transition Kernel ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [§2.5](https://arxiv.org/html/2601.04900v1#S2.SS5.p2.4 "2.5 Harris-recurrence of Essential Feller Transition Kernel ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [§4](https://arxiv.org/html/2601.04900v1#S4.p4.1 "4 Conclusion ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [Definition 11](https://arxiv.org/html/2601.04900v1#Thmtheorem11 "Definition 11 (Quasi–Feller and Quasi–strong Feller, after [2]). ‣ 2.1 Quasi–Feller regularity ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [3]
  L. Breiman (1960)
  The strong law of large numbers for a class of markov chains.
  The Annals of Mathematical Statistics 31 (3),  pp. 801–803.
  Cited by: [§1](https://arxiv.org/html/2601.04900v1#S1.p4.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [4]
  L. Breiman (1961)
  Strong ergodicity and the strong law of large numbers.
  Proceedings of the National Academy of Sciences of the USA 47,  pp. 204–207.
  Cited by: [§1](https://arxiv.org/html/2601.04900v1#S1.p4.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [5]
  R. Douc, G. Fort, and A. Guillin (2009)
  Subgeometric rates of convergence of ff-ergodic strong Markov processes.
  Stochastic Processes and their Applications 119 (3),  pp. 897–923.
  Cited by: [§1](https://arxiv.org/html/2601.04900v1#S1.p2.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [6]
  M. Duflo (1997)
  Random iterative models.
  Applications of Mathematics, Springer.
  Cited by: [§1](https://arxiv.org/html/2601.04900v1#S1.p3.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [§2.3](https://arxiv.org/html/2601.04900v1#S2.SS3.p1.1 "2.3 Stability via uniqueness ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [7]
  M. Duflo (1990)
  Méthodes récursives aléatoires.
  Collection Techniques Stochastiques, Masson.
  Cited by: [§2.2](https://arxiv.org/html/2601.04900v1#S2.SS2.p3.1 "2.2 Almost sure tightness of trajectories ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [8]
  M. Hairer and J. C. Mattingly (2011)
  Yet another look at Harris’ ergodic theorem for Markov chains.
  Seminar on Stochastic Analysis, Random Fields and Applications VI 63,  pp. 109–117.
  Cited by: [§1](https://arxiv.org/html/2601.04900v1#S1.p2.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [9]
  O. Kallenberg (2002)
  Foundations of modern probability.
  2 edition, Probability and Its Applications, Springer.
  Cited by: [Remark 4](https://arxiv.org/html/2601.04900v1#Thmtheorem4.p1.1 "Remark 4. ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels").
* [10]
  S. P. Meyn and R. L. Tweedie (2009)
  Markov chains and stochastic stability.
  Second edition, Cambridge University Press.
  Cited by: [§1](https://arxiv.org/html/2601.04900v1#S1.p1.1 "1 Introduction ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [Remark 10](https://arxiv.org/html/2601.04900v1#Thmtheorem10.p1.4 "Remark 10. ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels"),
  [Remark 4](https://arxiv.org/html/2601.04900v1#Thmtheorem4.p1.1 "Remark 4. ‣ 2 Main result ‣ Uniqueness of invariant measures as a structural property of Markov kernels").