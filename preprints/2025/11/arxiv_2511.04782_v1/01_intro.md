---
authors:
- Haochun Ma
- Jordan Roulleau-Pasdeloup
doc_id: arxiv:2511.04782v1
family_id: arxiv:2511.04782
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup:
  ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as
  well as seminar participants at École Polytechnique for insightful comments.'
url_abs: http://arxiv.org/abs/2511.04782v1
url_html: https://arxiv.org/html/2511.04782v1
venue: arXiv q-fin
version: 1
year: 2025
---


Haochun Ma


Jordan Roulleau-Pasdeloup

(November 6, 2025)

Depending on the persistence of the underlying Markov chain shock, the standard New Keynesian model predicts starkly different conclusions at the Effective Lower Bound. We clear up this morass by using a truncated Markov chain. We prove that the expectations-driven trap à la Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) doesn’t arise as an equilibrium outcome. In addition, the equilibrium under a truncated Markov chain is guaranteed to be unique, the effect of government spending is positive on consumption and does not switch signs but may grow unbounded —a puzzle.

JEL Codes: E32, E32, E43, E63
  
Keywords: Truncated Markov Chain, Effective Lower Bound, Fiscal Policy

## 1 Introduction

With the Great Recession and the Covid-19 crises, advanced economies have experienced two long-lasting episodes where the Central Bank’s interest rate was stuck at its Effective Lower Bound —henceforth ELB. Given the secular decline in interest rates that have been observed across the board for the same countries, they are bound to experience it again sometime in the near future. Against this backdrop, do we have a reliable framework to think about the effects of policy at the ELB?

In this paper, we argue that the standard New Keynesian (NK) model with the standard shock structure that is often used to understand the mechanisms of policy transmission at the ELB may not be a reliable framework. To understand why, note that ELB episodes in the standard NK model are often modeled as a result of shocks that follow a standard 2-state absorbing Markov chain. This allows one to replicate occasional, but long-lasting ELB episodes as argued in Dordal-i Carreras et al., ([2016](https://arxiv.org/html/2511.04782v1#bib.bib11)). Let us denote by p∈(0,1)p\in(0,1) the probability that this shock returns to its absorbing state every period. Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) shows that there exists a threshold probability p¯\overline{p} such that if 0<p<p¯0<p<\overline{p} then one can end up at the ELB with a sufficiently large negative demand shock. Assuming a perfectly correlated government spending shock, he proves that such a policy crowds private consumption in at the ELB. Using a similar setup but assuming that p¯<p<1\overline{p}<p<1 instead, Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) show that one has two Minimum State Variable (MSV) equilibria, one of which features a binding ELB. They interpret this as a sunspot equilibrium and show that government spending crowds private consumption out. In addition, Ascari & Mavroeidis, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib2)) shows that in that situation, if the underlying shock is too large, no MSV equilibrium exists.

In a seminal paper, Leeper et al., ([2017](https://arxiv.org/html/2511.04782v1#bib.bib22)) study the fiscal multiplier in a rich set of medium scale models without an ELB constraint. They show that the effects of fiscal policy vary a lot from model to model and conclude that this constitutes a morass. We argue that such a morass is present in the standard New Keynesian model with an occasionally binding ELB constraint. As we have seen, the effects of fiscal policy can flip signs depending on the source of the ELB episode, but the same happens for any other policy in that model. Because of this, there have been many attempts to use structural approaches to tease these two situations apart, see Aruoba et al., ([2018](https://arxiv.org/html/2511.04782v1#bib.bib1)) and more recently Cai et al., ([2025](https://arxiv.org/html/2511.04782v1#bib.bib6)). Both find that short run output multipliers crowd consumption out in Japan, but the reverse hold for the U.S. For a long expected duration of the ELB however, Cai et al., ([2025](https://arxiv.org/html/2511.04782v1#bib.bib6)) find that consumption is crowded in even in Japan.

In this paper, we take a different approach and show that truncating the Markov chain results in a framework with consistent policy recommendations.
Following Eggertsson & Woodford, ([2003](https://arxiv.org/html/2511.04782v1#bib.bib16)), we assume that there exists a maximum time period after which the Markov chain has to return to its absorbing state. This shock structure will have a number of interesting properties. First, we show that under such a truncated Markov chain there exists only one MSV equilibrium. As a result, non-existence of an MSV equilibrium never arises in our framework. Therefore, one can consider policy experiments that are well-defined regardless of the degree of persistence or the size of the shock.

Zooming in on fiscal policy, we find that regardless of the persistence level, consumption is crowded in. This is in stark contrast with the conclusions reached in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) for a similar model. To understand why, let us denote by ℓ\ell the maximum duration after which the Markov chain goes back to its absorbing state. In this framework, one can compute in closed form the impact multiplier effect of government spending as a function of ℓ\ell. It turns out that this effect obeys a simple second order recursion of the form ℳ​(ℓ)=a⋅ℳ​(ℓ−1)+b⋅ℳ​(ℓ−2)\mathscr{M}(\ell)=a\cdot\mathscr{M}(\ell-1)+b\cdot\mathscr{M}(\ell-2), where ℳ​(ℓ)\mathscr{M}(\ell) denotes the multiplier effect for a maximum duration of ℓ\ell and where the coefficients a,ba,b are functions of structural parameters. Note that the initial conditions of this recursion are given by the pair ℳ​(1),ℳ​(2)\mathscr{M}(1),\mathscr{M}(2): the effects under a shock that can last at most 1 and 2 periods. We show that the solution studied in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) is indeed a fixed point of this recursion. However, the assumption of p¯<p<1\overline{p}<p<1 coupled with a large enough shock precludes the recursion from converging to its fixed point: it diverges away instead. Thus if one assumes 0<p<p¯0<p<\overline{p} instead, as ℓ→∞\ell\to\infty the recursion converges to its fixed point, which in turn coincides with the constant equilibrium constructed in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)).

Mathematically, one can solve for the recursion and express ℳ​(ℓ)\mathscr{M}(\ell) for a given ℓ\ell as a geometric sum with persistence pp as its main argument. For a large enough demand shock, the coefficients aa and bb will reflect dynamics at the ELB. In that situation, it turns out that the radius of convergence for this geometric series as ℓ→∞\ell\to\infty is given by 0<p<p¯0<p<\overline{p}. In this context, the equilibrium/multiplier constructed in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) reflects the analytical continuation of the geometric series. Strictly speaking, the geometric series is not defined for p>p¯p>\overline{p}, but its analytical continuation is.111As a simple example, the geometric series f​(x)=∑k=0∞xkf(x)=\sum\_{k=0}^{\infty}x^{k} has a radius of convergence of |x|<1|x|<1 meaning that ∑k=0∞xk=1/(1−x)\sum\_{k=0}^{\infty}x^{k}=1/(1-x) if |x|<1|x|<1. For |x|>1|x|>1, the geometric series isn’t well defined anymore but 1/(1−x)1/(1-x) still is, except for x=1x=1. In that sense, 1/(1−x)1/(1-x) is the analytical continuation of f​(x)f(x).

Beyond the mathematical properties, the sign flip for the fiscal multiplier can also be given an intuition using a simple aggregate supply/demand graph. To construct this graph, we need to consider the following experiment. Assume that the Markov chain remains in its low state all the way until the maximum date ℓ\ell. In this context, the economy will settle to a medium run constant equilibrium before eventually returning to its absorbing state immediately at time period ℓ\ell. As ℓ→∞\ell\to\infty, this construction is exactly the one considered in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) and Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)). If the aggregate supply/demand curves only cross once inside/outside the ELB, our method gives the same result as in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) in the limit. If the demand shock is too large so that these two curves do not cross, then our method guarantees that the ELB is binding for any possible duration ℓ\ell. If the curves cross twice, then the outcome depends on the size of the demand shock. If the demand shock is small our method converges on an outcome where the ELB never binds. If the demand shock is large enough instead, there exists a value of ℓ¯\underline{\ell} such that the ELB binds for ℓ≥ℓ¯\ell\geq\underline{\ell}.

This graphical approach also sheds some light on whether the NK model delivers the well known puzzles (see Michaillat & Saez, ([2021](https://arxiv.org/html/2511.04782v1#bib.bib24))) at the ELB. Indeed, it has been shown (see Bilbiie, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib5))) that the NK model displays a bifurcation at the ELB around p¯\overline{p} where it produces unbounded outcomes. Using our method, we show two things. First, p>p¯p>\overline{p} is a necessary but not sufficient condition for the puzzles to arise. We need the underlying demand shock to be large enough in magnitude in addition. If the demand shock is not large enough, then there are no puzzles regardless of the level of persistence. Second, the puzzles arise for a much larger region of the state space. Let us denote by d¯​(p)\overline{d}(p) the minimum value of the demand shock such that the model ends up at the ELB eventually. While in the cited literature the puzzles arise in the vicinity of p¯\overline{p}, in our case these arise in [p¯​ 1]×[d¯​(p)dm​a​x][\overline{p}\ \ 1]\times[\overline{d}(p)\ \ d^{max}], where dm​a​xd^{max} is the maximum value of the shock.

Related Literature—Given the focus on the effects of policy at the ELB, this paper is related to Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)), Christiano et al., ([2011](https://arxiv.org/html/2511.04782v1#bib.bib8)), Woodford, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib32)), Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)), Schmidt, ([2017](https://arxiv.org/html/2511.04782v1#bib.bib29)), Wieland, ([2018](https://arxiv.org/html/2511.04782v1#bib.bib30)), Hills & Nakata, ([2018](https://arxiv.org/html/2511.04782v1#bib.bib21)), Miyamoto et al., ([2018](https://arxiv.org/html/2511.04782v1#bib.bib25)), Wieland, ([2019](https://arxiv.org/html/2511.04782v1#bib.bib31)), Nakata & Schmidt, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib28)) and Bilbiie, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib5)). In particular, we are interested about the existence of an ”expectations-driven” ELB episode that has been studied in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)), Bilbiie, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib5)), Nakata & Schmidt, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib28)), Ascari & Mavroeidis, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib2)), Ascari et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib3)) as well as Murakami et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib26)).

To construct the solution of our model, we borrow from the method developed in Eggertsson & Woodford, ([2003](https://arxiv.org/html/2511.04782v1#bib.bib16)) and more recently Eggertsson et al., ([2021](https://arxiv.org/html/2511.04782v1#bib.bib15)). More specifically and as alluded to before, we rely on an absorbing Markov chain that is truncated in the sense that it is forced to go back to its absorbing state in finite time. As a result, the framework that we use shares some similarities with the one introduced in Woodford, ([2019](https://arxiv.org/html/2511.04782v1#bib.bib33)) in which firms and consumers can only plan for a finite horizon. Typically, this is coupled with an assumption about learning in a backward fashion beyond the planning horizon. This setup has been further studied in Gust et al., ([2022](https://arxiv.org/html/2511.04782v1#bib.bib19), [2024](https://arxiv.org/html/2511.04782v1#bib.bib20)) as well as Dupraz & Marx, ([2025](https://arxiv.org/html/2511.04782v1#bib.bib12)). The assumption of backward learning injects endogenous persistence and thus precludes the derivation of closed form results for this class of models. In contrast, the assumption of truncated Markov chains that we rely on allows us to fully characterize the dynamics of the model after a shock in closed form.

This solution method will lead us to conclude that the expectations-driven episode only happens when ℓ=+∞\ell=+\infty and that the range of parameters that yield a puzzling behavior is much larger than initially thought. Given our focus on these puzzles, we are also related to Eggertsson, ([2010](https://arxiv.org/html/2511.04782v1#bib.bib13)), Carlstrom et al., ([2015](https://arxiv.org/html/2511.04782v1#bib.bib7)), Michaillat & Saez, ([2021](https://arxiv.org/html/2511.04782v1#bib.bib24)), Diba & Loisel, ([2021](https://arxiv.org/html/2511.04782v1#bib.bib10)), Del Negro et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib9)), Gibbs & McClung, ([2023](https://arxiv.org/html/2511.04782v1#bib.bib18)) and Eskelinen et al., ([2024](https://arxiv.org/html/2511.04782v1#bib.bib17)).

This paper is structured as follows. In Section [2](https://arxiv.org/html/2511.04782v1#S2 "2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), we illustrate the morass graphically for a standard New Keynesian model. In Section [3](https://arxiv.org/html/2511.04782v1#S3 "3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), we prove formally and illustrate graphically how the assumption of a truncated Markov chain clears up the morass. In Section [4](https://arxiv.org/html/2511.04782v1#S4 "4 Characterizing Fiscal Policy at the ELB ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), we use our framework to study the effects of fiscal policy at the ELB. We finally conclude in Section [5](https://arxiv.org/html/2511.04782v1#S5 "5 Conclusion ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").

## 2 Picturing the Morass

In order to illustrate the morass both intuitively and graphically, we borrow the framework from Ascari et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib3)). This setup nests the conventional three-equation New Keynesian model as a special case and allows for a class of behavioral models by relaxing the assumption of full-information rational expectations. The model is described by the following equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xt\displaystyle x\_{t} | =mx​x​𝔼t​xt+1−σ​(it−mx​π​𝔼t​πt+1)−dt\displaystyle=m\_{xx}\mathbb{E}\_{t}x\_{t+1}-\sigma(i\_{t}-m\_{x\pi}\mathbb{E}\_{t}\pi\_{t+1})-d\_{t} |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | πt\displaystyle\pi\_{t} | =λ​xt+mπ​π​β​𝔼t​πt+1\displaystyle=\lambda x\_{t}+m\_{\pi\pi}\beta\mathbb{E}\_{t}\pi\_{t+1} |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | it\displaystyle i\_{t} | =max⁡{ψ​πt,−μ}\displaystyle=\max\{\psi\pi\_{t},-\mu\} |  | (3) |

where xtx\_{t} denotes the output gap, iti\_{t} the nominal interest rate, and πt\pi\_{t} the inflation rate. Setting mx​x=mx​π=mπ​π=1m\_{xx}=m\_{x\pi}=m\_{\pi\pi}=1 recovers the standard New Keynesian model. Following Ascari et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib3)) and Eggertsson & Woodford, ([2003](https://arxiv.org/html/2511.04782v1#bib.bib16)), we assume for now that the demand shock dtd\_{t} follows a two-state Markov process governed by the following initial distribution UU, transition matrix 𝐏\mathbf{P} and vector of states SS:

|  |  |  |
| --- | --- | --- |
|  | U=[10]𝐏=[p1−p01]S=[d0]⊤.\displaystyle U=\begin{bmatrix}1&0\end{bmatrix}\quad\mathbf{P}=\begin{bmatrix}p&1-p\\ 0&1\end{bmatrix}\quad S=\begin{bmatrix}d&0\end{bmatrix}^{\top}. |  |

Throughout the paper, we use an uppercase bold font to represent matrices and uppercase to represent vectors while scalars are represented with a lowercase letter. Following the literature, we first guess a solution where xtx\_{t} and πt\pi\_{t} can be written as a linear function of the shock dtd\_{t} and then verify if/when the ELB is binding or not. In practice, this amounts to work with a model where we can write 𝔼t​πt+1=p⋅πt\mathbb{E}\_{t}\pi\_{t+1}=p\cdot\pi\_{t} and likewise for 𝔼t​xt+1\mathbb{E}\_{t}x\_{t+1}. Using this, one can compute the aggregate supply/demand curves of this economy conditional on the initial realization dd. Given that the Taylor principle does not apply at the ELB, we follow the literature and look for an MSV equilibrium. The main question that we seek to answer at this point is: for given values of p,dp,d, how many MSV equilibria are there? We answer that question in the following proposition.

###### Proposition 1.

For a vector [pd][p\ \ d] in [0,1]×[0,dm​a​x][0,1]\times[0,d^{max}], there can be 0, 1 or 2 MSV equilibria. Further, thre exists a pair of thresholds p¯\overline{p} and d¯​(p)\overline{d}(p) such that:

1. 1.

   If p<p¯p<\overline{p}, then there exists only one MSV equilibrium
2. 2.

   If p>p¯p>\overline{p} and d<d¯​(p)d<\overline{d}(p), then there are two MSV equilibria: one where the ELB binds, and one where it does not.
3. 3.

   If p>p¯p>\overline{p} and d>d¯​(p)d>\overline{d}(p), there does not exist any MSV equilibrium.

###### Proof.

This proposition essentially summarizes results that have been established in the existing literature and as a result are relegated to the online Appendix, section A.
∎

These cases have been studied extensively in the literature. Case 1 is the standard one introduced in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) and that has received the most attention, see Christiano et al., ([2011](https://arxiv.org/html/2511.04782v1#bib.bib8)) and Woodford, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib32)) for two prominent examples. Case 2 is the one introduced in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) and that has also received a fair bit of attention, especially to explain the long liquidity traps in Japan. Following the terminology in Ascari & Mavroeidis, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib2)); Ascari et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib3)), we say that the model exhibits incoherence. Case 3 hasn’t received nearly the same degree of attention. Following Ascari & Mavroeidis, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib2)) and Ascari et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib3)), we say that in this case the model exhibits incompleteness. In order to gain some intuition regarding what is happening in all those three cases, we illustrate the underlying aggregate supply/demand curves that give rise to each case in Figure [1](https://arxiv.org/html/2511.04782v1#S2.F1 "Figure 1 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").

![Refer to caption](Figure1_a_0905.png)


(a) Case 1

![Refer to caption](Figure1_b_0905.png)


(b) Case 2

![Refer to caption](Figure1_c_0905.png)


(c) Case 3

Figure 1: AS and AD diagrams corresponding to the three cases in the literature.

In all three panels, there is a minimum level of inflation below which the Central Bank will have no choice but to set the nominal rate to 0. When that happens, the aggregate demand (AD) curve slopes positively because as the nominal rate doesn’t move, the real interest rates moves one for one with the inflation rate: the Central Bank cannot accommodate variations in inflation.
In the first panel, the negative demand shock generates lower inflation and output gap by shifting the aggregate demand curve down. If this shift is large enough, then the two curves cross on the positive sloping part. It can be easily seen that only one MSV equilibrium clears the ”verify” part in the guess-and-verify exercise.

In the second panel, the increased persistence of the underlying shock makes both slopes of aggregate demand larger in magnitude —remember that 𝔼t​xt+1=p⋅xt\mathbb{E}\_{t}x\_{t+1}=p\cdot x\_{t} in that framework. In that case there are two MSV equilibria that clear the ”verify” part in the guess-and-verify exercise. Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) then assume that a sunspot makes the agents coordinate on the one in which the ELB is binding. Note that one can assume without loss of generality that the sunspot is perfectly correlated with the demand shock. If that demand shock is small enough in magnitude, the shift down in AD is small enough to preserve the two crossings. As a result, the ELB equilibrium can be a result of the demand shock as well.

In the third panel, we depict what happens if the shift in aggregate demand is too large in magnitude. In that case, there are no MSV equilibria that clear the ”verify” part in the guess-and-verify exercise. This case has been studied in detail in Ascari & Mavroeidis, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib2)). Potential fixes to avoid that situation from happening can be found in Ascari et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib3)) as well as Murakami et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib26)). The solution that we propose in that paper is largely complimentary to these efforts. The main intuition that we will leverage is that these papers guess and verify whether there exists a constant allocation that is perfectly correlated with the Markov Chain. Using a truncated Markov chain, we show that even though a constant allocation may fail to exist/be unique, a unique time-varying one is guaranteed to exist.

To sum up the morass in one graph, we now provide a figure that represents which case arises for each value in of [pd][p\ \ d] in [0,1]×[0,dm​a​x][0,1]\times[0,d^{max}] for a standard calibration of the model.222The calibration is given by σ=1.5\sigma=1.5, β=0.99\beta=0.99, ψ=1.183\psi=1.183, λ=0.1\lambda=0.1, mx​x=1m\_{xx}=1, mx​π=1m\_{x\pi}=1, and mπ​π=0.74m\_{\pi\pi}=0.74

![Refer to caption](Figure2_1106_ver2.png)


Figure 2: Regions of MSV Solutions in (p,d)(p,d) space.

This figure shows that all the puzzling behavior of the NK model with standard shocks happens to the right of p¯\overline{p}.333The calibration that we use implies p¯=0.75\overline{p}=0.75, which translates into an expected duration of exactly 1 year for the shock. As a result, virtually all of the efforts to rid the model of its puzzles boil down to finding ways to push p¯\overline{p} to the right. If one manages to push it above one, then the model can be guaranteed to produce a unique MSV solution. We will depart from this literature in several ways.

First, we show that truncating the Markov chain results in a time-varying allocation that converges to a constant allocation as ℓ→∞\ell\to\infty only under some precise circumstances that we clarify. Second, we show that what is happening to the right of p¯\overline{p} at the ELB isn’t different in sign, but only in magnitude. Third and finally, we show that the relevant graph to understand what is happening is about the medium-run dynamics of the model and not the short run.

## 3 Resolving the Morass

In this section we depart from most of the recent literature in that we follow Eggertsson & Woodford, ([2003](https://arxiv.org/html/2511.04782v1#bib.bib16)) as well as Eggertsson et al., ([2021](https://arxiv.org/html/2511.04782v1#bib.bib15)) and consider a truncated Markov chain.

###### Definition 3.1 (Truncated Markov Chain).

We assume a stochastic process for dtd\_{t} with an initial value of dd. Up until ℓ\ell time periods, the process follows a Markov chain with the transition matrix 𝐏\mathbf{P} introduced earlier. If the process is not back to its absorbing state of 0 after ℓ\ell periods, then it is forced to.

###### Corollary 0.1.

In the limit as ℓ→∞\ell\to\infty, the stochastic process boils down to the standard 2-state Markov process used in the literature.

The main difference between the truncated Markov chain and the standard Markov chain used in the literature is that the latter lacks a terminal condition. Indeed, even though this happens with a vanishingly low probability, it is possible that a standard Markov chain remains in its low state for an arbitrarily long period of time. Given the forward-looking nature of the standard NK model, papers in the literature have to consider this case when computing conditional expectations. To say it differently, a Markov chain has a memoryless property. This means that, no matter how long the chain has spent in the low state, the probability to transition to the absorbing is always 1−p1-p.

In contrast, our truncated Markov chain features a well-defined terminal condition. This implies that the model itself has a well-defined terminal condition: the non-stochastic steady state with zero inflation. More precisely, as is well known (see Benhabib et al., ([2001](https://arxiv.org/html/2511.04782v1#bib.bib4))), the standard New Keynesian model features two non-stochastic steady states. We will follow the literature and focus on the well-behaved steady state where the ELB is not binding in the long run. In that context, our objective is to guarantee that, conditional on a demand shock dd in the short run, there is a unique MSV path back to the well-behaved steady state. For context, the equilibrium concept studied in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) has two MSV paths back to steady state.444If one considers the possibility that the economy eventually settles down to the steady state where the ELB is binding as in Ascari & Mavroeidis, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib2)), then there are 4 MSV paths back to steady state.

That terminal condition allows us to use a standard backward induction method. To see why such a terminal condition is crucial, consider our Phillips curve equation ([2](https://arxiv.org/html/2511.04782v1#S2.E2 "Equation 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")). Let us denote π~t\tilde{\pi}\_{t} and x~t\tilde{x}\_{t} inflation and the output gap conditional on the demand shock being in its low state. Notice that, assuming ℓ≥1\ell\geq 1 we can rewrite it as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π~t\displaystyle\tilde{\pi}\_{t} | =λ​x~t+β​mπ​π​𝔼t​πt+1\displaystyle=\lambda\tilde{x}\_{t}+\beta m\_{\pi\pi}\mathbb{E}\_{t}\pi\_{t+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​x~t+β​mπ​π​[p⋅π~t+1+(1−p)⋅0],\displaystyle=\lambda\tilde{x}\_{t}+\beta m\_{\pi\pi}\left[p\cdot\tilde{\pi}\_{t+1}+(1-p)\cdot 0\right], |  |

where we have used the fact that inflation is 0 in the absence of shocks in the well-behaved steady state. For the sake of the argument, assume that the ELB is not binding so that we can write the nominal interest rate as a function of the inflation rate. Repeating the same procedure with the Euler equation, we end up with a system of two equations in four unknowns: π~t,x~t,π~t+1\tilde{\pi}\_{t},\tilde{x}\_{t},\tilde{\pi}\_{t+1} and x~t+1\tilde{x}\_{t+1}. In turn, both π~t+1\tilde{\pi}\_{t+1} and x~t+1\tilde{x}\_{t+1} depend on π~t+2\tilde{\pi}\_{t+2} and x~t+2\tilde{x}\_{t+2} by the same procedure. Because a standard Markov chain can stay in the low state for an arbitrarily long period of time, this process carries on ad infinitum.

In our setup, this doesn’t happen. Assume that the Markov chain has remained in its low state for the ℓ\ell periods t,t+1,…,ℓ−1t,t+1,\dots,\ell-1 and that ℓ>>1\ell>>1. It follows that it will be forced to go back to its absorbing state next period. Therefore, we can write 𝔼t+ℓ−1​πt+ℓ=𝔼t+ℓ−1​ct+ℓ=0\mathbb{E}\_{t+\ell-1}\pi\_{t+\ell}=\mathbb{E}\_{t+\ell-1}c\_{t+\ell}=0, where 𝔼t+ℓ−1\mathbb{E}\_{t+\ell-1} denotes expectations conditional on all information up to time period t+ℓ−1t+\ell-1. In that case, the Euler equation and Phillips curve become:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x~t+ℓ−1\displaystyle\tilde{x}\_{t+\ell-1} | =−σ⋅max⁡{ψ​π~t+ℓ−1,−μ}−d\displaystyle=-\sigma\cdot\max\{\psi\tilde{\pi}\_{t+\ell-1},-\mu\}-d |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π~t+ℓ−1\displaystyle\tilde{\pi}\_{t+\ell-1} | =λ​x~t+ℓ−1.\displaystyle=\lambda\tilde{x}\_{t+\ell-1}. |  | (5) |

Because of the max operator in the equation ([4](https://arxiv.org/html/2511.04782v1#S3.E4 "Equation 4 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")), this is a system of two non-linear equations in two unknowns. Using the fact that equation ([4](https://arxiv.org/html/2511.04782v1#S3.E4 "Equation 4 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) is piecewise linear however, we can show that this system of non-linear equations has a unique solution. We establish this in the following Proposition.

###### Proposition 2.

The system of equations ([4](https://arxiv.org/html/2511.04782v1#S3.E4 "Equation 4 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."))-([5](https://arxiv.org/html/2511.04782v1#S3.E5 "Equation 5 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) has a unique solution for a given value of dd.

###### Proof.

See Appendix [A.1](https://arxiv.org/html/2511.04782v1#S1.SS1 "A.1 Proof of Proposition 2 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").
∎

Intuitively, the proof relies on the fact that one can transform this system of equations into a single piecewise linear equation in x~t+ℓ−1\tilde{x}\_{t+\ell-1}. Then, notice that regardless of whether x~t+ℓ−1≶−μ/(ψ​λ)\tilde{x}\_{t+\ell-1}\lessgtr-\mu/(\psi\lambda), equation ([4](https://arxiv.org/html/2511.04782v1#S3.E4 "Equation 4 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) describes an upward sloping linear function crossing with either a horizontal line or a decreasing linear function. Perhaps more intuitively and in order to tie it back to the aggregate supply/demand graphs that can be found in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)), it is instructive to plot equations ([4](https://arxiv.org/html/2511.04782v1#S3.E4 "Equation 4 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."))-([5](https://arxiv.org/html/2511.04782v1#S3.E5 "Equation 5 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) separately with π~t+ℓ−1\tilde{\pi}\_{t+\ell-1} on the xx axis.

![Refer to caption](Figure3a_v2.png)


(a) d<d¯​(0)d<\bar{d}(0)

![Refer to caption](Figure3b_v2.png)


(b) d>d¯​(0)d>\bar{d}(0)

Figure 3: Aggregate Supply and Demand in Period t+ℓ−1t+\ell-1

The main take-away from Figure [3](https://arxiv.org/html/2511.04782v1#S3.F3 "Figure 3 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") is that, because of the terminal condition, expectations at time t+ℓ−1t+\ell-1 are effectively exogenous.555This is where our setup markedly departs from the one in Woodford, ([2019](https://arxiv.org/html/2511.04782v1#bib.bib33)), in which expectations right at the end of the planning horizon switch to being backward-looking as a function of all the realized history of endogenous variables. The exogeneity of expectations at time t+ℓ−1t+\ell-1 is what buys us the tractability that we leverage to characterize dynamics in closed form later on. This is the reason why, in sharp contrast with the existing literature, the slope of AD at the ELB (to the left of π¯\underline{\pi}) is zero. In our case, there is no automatic feedback between current realizations and expectations that can bend the AD curve back towards the aggregate supply curve at the ELB. Given that a realization of dd will shift the AD curve up or down, there can be only one crossing. In the existing literature, the Markov chain assumption means that, regardless of how long the shock has remained in its low state, it is still expected to be in the same state tomorrow with probability pp.

Importantly, this intuition carries over to all time periods all the way back to the first one where the shock materializes. To see this, note that both x~t+ℓ−1\tilde{x}\_{t+\ell-1} and π~t+ℓ−1\tilde{\pi}\_{t+\ell-1} are linear combinations of exogenous expectations upon exit and the shock dd: as of time period t+ℓ−2t+\ell-2, both are effectively exogenous. As a result, the graphical representation of the allocation at time t+ℓ−2t+\ell-2 will be similar to the one in Figure 3, except that conditional expectations will now be non zero. To see this, note that we can write the conditional expectation of inflation as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝔼t+ℓ−2​πt+ℓ−1=p⋅π~t+ℓ−1+(1−p)⋅0,\displaystyle\mathbb{E}\_{t+\ell-2}\pi\_{t+\ell-1}=p\cdot\tilde{\pi}\_{t+\ell-1}+(1-p)\cdot 0, |  |

which is again effectively exogenous as of time period t+ℓ−2t+\ell-2. The same goes for time periods t+ℓ−3,…,tt+\ell-3,\dots,t assuming again that ℓ>>1\ell>>1. Using the fact that expectations are effectively exogenous considerably simplifies the backward induction process. In turn, it allows us to compute easily the whole path of inflation/output gap for any given value of ℓ\ell. Ideally, we would want to be establish that this path is unique. This is done in the next proposition, which is a generalization of proposition [2](https://arxiv.org/html/2511.04782v1#Thmprop2 "Proposition 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").

###### Proposition 3.

For each value of d∈[0,dm​a​x]d\in[0,d^{max}] and a maximum horizon ℓ\ell, there exists a unique pair of sequences {xt+n,πt+n}n≥0\left\{x\_{t+n},\pi\_{t+n}\right\}\_{n\geq 0} that solves equations ([1](https://arxiv.org/html/2511.04782v1#S2.E1 "Equation 1 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."))-([2](https://arxiv.org/html/2511.04782v1#S2.E2 "Equation 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")).

###### Proof.

See Appendix [A.2](https://arxiv.org/html/2511.04782v1#S1.SS2 "A.2 Proof of Proposition 3 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").
∎

Following the terminology laid out in Ascari & Mavroeidis, ([2022](https://arxiv.org/html/2511.04782v1#bib.bib2)) and Ascari et al., ([2023](https://arxiv.org/html/2511.04782v1#bib.bib3)), Proposition [3](https://arxiv.org/html/2511.04782v1#Thmprop3 "Proposition 3. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") guarantees that, under a truncated Markov chain, there is neither incoherence nor incompleteness. With this result in mind, we now want to characterize these paths. In order to simplify that task, we find it useful to rely on the following assumption on parameters:

###### Assumption 1.

The parameters in equations ([1](https://arxiv.org/html/2511.04782v1#S2.E1 "Equation 1 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."))-([2](https://arxiv.org/html/2511.04782v1#S2.E2 "Equation 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) are such that ψ<mx​πβ​mπ​π\psi<\frac{m\_{x\pi}}{\beta m\_{\pi\pi}}.

This assumption is not standard and needs some justification as a result. To do so, take the model given by equations ([1](https://arxiv.org/html/2511.04782v1#S2.E1 "Equation 1 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."))-([2](https://arxiv.org/html/2511.04782v1#S2.E2 "Equation 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) under the assumption that it stays outside the ELB the whole time. In that case, it can be rewritten in matrix form as follows:

|  |  |  |
| --- | --- | --- |
|  | Y~t=p⋅𝐀​Y~t+1+C⋅d,\displaystyle\tilde{Y}\_{t}=p\cdot\mathbf{A}\tilde{Y}\_{t+1}+C\cdot d, |  |

where the elements of matrix 𝐀\mathbf{A} depend on the structural parameters of the model. Given a terminal value after ℓ\ell periods at time ℓ−1\ell-1, it is straightforward to see that backward induction gives a value for Y~t\tilde{Y}\_{t} that depends on the powers of matrix p⋅𝐀p\cdot\mathbf{A}. Assumption [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") guarantees that the eigenvalues of this matrix are real-valued.

As an aside, note that the standard New Keynesian model is given by mx​π=mπ​π=1m\_{x\pi}=m\_{\pi\pi}=1 and β∼1\beta\sim 1. As a result, assumption [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") implies that the Taylor rule coefficient ψ\psi needs to be lower than 1/β1/\beta: a value that is very close to 1. For most calibrations666Note that calibrations in which ψ<1\psi<1 may not preclude a determinate equilibrium as long as the Central Bank can credibly commit to react more than 1 for 1 with respect to non-fundamental/sunspot shocks. Such a rule can be considered to give a better account of the lag between inflation surging in 2021/2022 and the US Federal Reserve lagging behind. See Nakamura et al., ([2025](https://arxiv.org/html/2511.04782v1#bib.bib27)) for a detailed treatment of these two points. of the standard NK model then, this assumption is violated and the eigenvalues of matrix p⋅𝐀p\cdot\mathbf{A} are complex conjugates. When that is the case, the elements of matrix (p⋅𝐀)n(p\cdot\mathbf{A})^{n} oscillate as a function of nn. In that context, our assumption rules out these oscillations in the values of inflation and output gap along the path.

This assumption can be given a clear economic intuition. It answers the following question: given a value of output gap xtx\_{t}, what is the effect of an increase in expected inflation on the expected real interest rate? From the Phillips curve, for a given output gap we have ∂πt/∂𝔼t​πt+1=β​mπ​π\partial\pi\_{t}/\partial\mathbb{E}\_{t}\pi\_{t+1}=\beta m\_{\pi\pi}. It follows from the Taylor rule that ∂it/∂𝔼t​πt+1=ψ​β​mπ​π\partial i\_{t}/\partial\mathbb{E}\_{t}\pi\_{t+1}=\psi\beta m\_{\pi\pi}. We then get:

|  |  |  |
| --- | --- | --- |
|  | ∂∂𝔼t​πt+1​(it−mx​π​𝔼t​πt+1)=ψ​β​mπ​π−mx​π.\displaystyle\frac{\partial}{\partial\mathbb{E}\_{t}\pi\_{t+1}}(i\_{t}-m\_{x\pi}\mathbb{E}\_{t}\pi\_{t+1})=\psi\beta m\_{\pi\pi}-m\_{x\pi}. |  |

In that context, assumption [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") guarantees that the expected real interest rate decreases after an increase in expected inflation. Ruling out these oscillations considerably simplifies the proofs for us because it prevents the path of inflation to oscillate above and below π¯\underline{\pi}.

Having ruled these oscillations out, we still need to guarantee that the eigenvalues of p⋅𝐀p\cdot\mathbf{A} decay exponentially to ensure that the model is well-behaved in normal times. This requires the following assumption:

###### Assumption 2.

The parameters in equations ([1](https://arxiv.org/html/2511.04782v1#S2.E1 "Equation 1 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."))-([2](https://arxiv.org/html/2511.04782v1#S2.E2 "Equation 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) are such that

|  |  |  |
| --- | --- | --- |
|  | ψ>mx​π+(1−mx​x)​(β​mπ​π−1)λ​σ\displaystyle\psi>m\_{x\pi}+\frac{(1-m\_{xx})(\beta m\_{\pi\pi}-1)}{\lambda\sigma} |  |

Assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") guarantees that the eigenvalues of matrix p⋅𝐀p\cdot\mathbf{A} have a modulus that is strictly less than 1. It can be shown that assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") actually coincides with the Taylor principle. Combined with assumption [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), this assumption gives an interval of values for the Taylor rule coefficient ψ\psi. For values of ψ\psi in this interval the elements of (p⋅𝐀)n(p\cdot\mathbf{A})^{n} decay monotonically and exponentially with nn.

It should be noted that, while assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") is necessary, assumption [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") is made for convenience. We will show numerically in the Appendix that none of our results depend on it. To derive the main result of our paper, we will need the following definition.

###### Definition 3.2.

For the standard New Keynesian model given by equations ([1](https://arxiv.org/html/2511.04782v1#S2.E1 "Equation 1 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."))-([3](https://arxiv.org/html/2511.04782v1#S2.E3 "Equation 3 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) and the truncated Markov chain process for dtd\_{t}, there are three types of possible solution paths.

* •

  If π~t+n​(ℓ)>π¯\tilde{\pi}\_{t+n}(\ell)>\underline{\pi} for all n=0,…,ℓ−1n=0,\dots,\ell-1 we call it a Pure Normal Time solution (PN)
* •

  If π~t+n​(ℓ)≤π¯\tilde{\pi}\_{t+n}(\ell)\leq\underline{\pi} for all n=0,…,ℓ−1n=0,\dots,\ell-1 we call it a Pure ELB solution (PL)
* •

  If there exists a value kk such that π~t+n​(ℓ)≤π¯\tilde{\pi}\_{t+n}(\ell)\leq\underline{\pi} for all n=0,…,kn=0,\dots,k and π~t+n​(ℓ)>π¯\tilde{\pi}\_{t+n}(\ell)>\underline{\pi} for all n=k+1,…,ℓ−1n=k+1,\dots,\ell-1 we call it a Mixed solution (M)

Note that after a realization dtd\_{t}, the effect on inflation will depend on the maximum duration ℓ\ell. As a result, we have made this dependence explicit in Definition [3.2](https://arxiv.org/html/2511.04782v1#S3.Thmdefinition2 "Definition 3.2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). With this definition and our assumptions in hand, we can now state the main results of our paper in the following two propositions.

###### Proposition 4 (pure solutions).

Assume that assumptions [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")-[2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") hold. Then it follows that there exist a strictly decreasing function d¯​(p):(0,1)→ℝ\overline{d}(p):(0,1)\to\mathbb{R} and a threshold p¯∈(0,1)\overline{p}\in(0,1) such that, for a given value of pp

* •

  if d∈[0,d¯​(p)]d\in[0,\overline{d}(p)] then the economy remains in the normal time regime for all time periods and we have limℓ→∞πt​(ℓ)=πtN<∞\lim\_{\ell\to\infty}\pi\_{t}(\ell)=\pi\_{t}^{N}<\infty as well as limℓ→∞xt​(ℓ)=xtN<∞\lim\_{\ell\to\infty}x\_{t}(\ell)=x\_{t}^{N}<\infty
* •

  if d∈(d¯​(0),1]d\in(\overline{d}(0),1] then the economy remains in the ELB regime for all time periods
* •

  if d∈(d¯​(0),1]d\in(\overline{d}(0),1] and p<p¯p<\overline{p}, then both xt​(ℓ)x\_{t}(\ell) and πt​(ℓ)\pi\_{t}(\ell) take on a finite value that we denote xtLx\_{t}^{L} and πtL\pi\_{t}^{L} as ℓ→∞\ell\to\infty. Otherwise, if d∈(d¯​(0),1]d\in(\overline{d}(0),1] and p≥p¯p\geq\overline{p} they diverge to −∞-\infty as ℓ→∞\ell\to\infty.

where we have used superscripts NN and LL to denote the normal times and liquidity trap solutions developed in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)).

###### Proof.

See Appendix [A.3](https://arxiv.org/html/2511.04782v1#S1.SS3 "A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").
∎

The first part of Proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") states that, regardless of the value of pp, if the initial demand shock is not large enough in magnitude, then the ELB will never be a binding constraint. Intuitively speaking, this is the situation depicted in the left panel of Figure [3](https://arxiv.org/html/2511.04782v1#S3.F3 "Figure 3 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). Assuming that the shock is still alive before the maximum date, expectations of being in steady state next period combined with the shift down in AD due to the shock are not enough to drive that economy at the ELB: this is the unique guaranteed outcome from the guess and verify process. Further, the current decrease in inflation and output gap will show up as expectations in the previous period. Once again however, these will not be sufficient to generate a binding ELB. It turns out that it holds for all previous periods.

The Second part of Proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") states that, once again regardless of the value of pp, if the shock is large enough in magnitude, then the ELB will bind in all periods. This is the situation depicted in the right panel of Figure [3](https://arxiv.org/html/2511.04782v1#S3.F3 "Figure 3 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). In contrast with the first part of the proposition, the shift down in AD is enough to make the ELB bind in the previous period. That intuition carries over to all previous periods.

The third part of Proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") further categorizes the pure ELB solution into two distinct sub-regimes. In a pure ELB regime, the dynamics of the economy can be written as follows:

|  |  |  |
| --- | --- | --- |
|  | Y~t=p⋅𝐀∗​Y~t+1+C⋅d+E\displaystyle\tilde{Y}\_{t}=p\cdot\mathbf{A}^{\*}\tilde{Y}\_{t+1}+C\cdot d+E |  |

where matrix 𝐀∗\mathbf{A}^{\*} encodes the fact that the Taylor rule is now passive and EE collects the constant σ​μ\sigma\mu in the Euler equation. In the event that p>p¯p>\overline{p}, at least one of the eigenvalues of 𝐀∗\mathbf{A}^{\*} is larger than 1 in modulus. When that happens, the backward induction algorithm generates an impact effect that is increasing in magnitude with ℓ\ell. In contrast, when p<p¯p<\overline{p} instead, the backward induction algorithm generates an impact effect that is finite and well-defined. In both cases, given a finite value of ℓ\ell, the equilibrium is finite and well-defined.

Note that proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") is tightly linked to the familiar graphs depicted in figure [1](https://arxiv.org/html/2511.04782v1#S2.F1 "Figure 1 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). Indeed, p>p¯p>\overline{p} is equivalent to the path being unstable and the fact that the equilibrium under a standard Markov chain is either non-existent or non-unique. Now that we have covered the pure solutions, we now move on to the characterization of the mixed solutions.

###### Proposition 5 (Mixed solutions).

Assume that assumptions [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")-[2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") hold. Then it follows that there exists a strictly decreasing function d¯​(p):(0,1)→ℝ\overline{d}(p):(0,1)\to\mathbb{R} and a threshold p¯∈(0,1)\overline{p}\in(0,1) such that, for a given value of pp

* •

  if d¯​(p)<d<d¯​(0)\overline{d}(p)<d<\overline{d}(0), then there exists an integer ℓ¯\overline{\ell} such that the ELB binds on impact if ℓ≥ℓ¯\ell\geq\overline{\ell}. If ℓ<ℓ¯\ell<\overline{\ell} instead, the ELB never binds.
* •

  if d¯​(p)<d<d¯​(0)\overline{d}(p)<d<\overline{d}(0) and in addition p<p¯p<\overline{p}, then we have limℓ→∞πt​(ℓ)=πtL\lim\_{\ell\to\infty}\pi\_{t}(\ell)=\pi\_{t}^{L} from Proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") and likewise for xtx\_{t}.
* •

  if d¯​(p)<d<d¯​(0)\overline{d}(p)<d<\overline{d}(0) and in addition p≥p¯p\geq\overline{p}, then we have limℓ→∞πt​(ℓ)=−∞\lim\_{\ell\to\infty}\pi\_{t}(\ell)=-\infty

where, as before, we have used superscripts NN and LL to denote the normal times and liquidity trap solutions developed in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)).

###### Proof.

See Appendix [A.4](https://arxiv.org/html/2511.04782v1#S1.SS4 "A.4 Proof of Proposition 5 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").
∎

The first part of Proposition [5](https://arxiv.org/html/2511.04782v1#Thmprop5 "Proposition 5 (Mixed solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") establishes that, if the shock dd lies between the specified range then whether the ELB binds on impact or not depends on the value of ℓ\ell. For the sake of the argument, assume that the ELB doesn’t bind for the period before the shock vanishes. Given that dd is a negative demand shock, it will result in lower inflation/output gap compared to the non-stochastic steady state. Now think about the period before that. The shock is there by definition, and now there is expected deflation/lower expected output gap. As a result, inflation and the output gap are mechanically lower than the period right after. That goes for the period before, and so and so on. If d<d¯​(p)d<\overline{d}(p), then that backward induction chain results in πtN\pi\_{t}^{N}—see Proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). If d¯​(p)<d<d¯​(0)\overline{d}(p)<d<\overline{d}(0), one can guess a hypothetical normal time solution. However, in that case the backward induction converges to a value of πt\pi\_{t} that is lower than π¯\underline{\pi} and thus violates the guess of a normal time solution.

So we know that if dd is in that range, eventually the expected deflation in the future will percolate back by enough to send the economy at the ELB in the short run. If p<p¯p<\overline{p}, then that process converges to the same value of πtL\pi\_{t}^{L} from Proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). Intuitively, for a finite value of ℓ\ell, the ELB will be binding on impact but the ELB will stop binding before the demand shock reverts to its steady state value. As before, if p≥p¯p\geq\overline{p}, the backward induction process gives a sequence that is diverging to −∞-\infty.

To illustrate these features, we report two experiments in figure [4](https://arxiv.org/html/2511.04782v1#S3.F4 "Figure 4 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). we assume that ℓ\ell takes on a relatively large value of 16, which represents 4 years for a quarterly calibration. Given that this is the maximum number of periods during which the shock can be stuck in its low state, we assume that the shock actually reverts back at time t+3t+3 after 4 quarters or 1 year. We consider two different cases, p<p¯p<\overline{p} (left panel) as well as p>p¯p>\overline{p} (right panel). In both cases, we report actual realized inflation πt+k​(ℓ)\pi\_{t+k}(\ell) alongside the hypothetical path of inflation if the shock were to stay in its low state for the full ℓ\ell periods.

![Refer to caption](mixed_pi_path_stable_extended_v3.png)


(a) p<p¯p<\bar{p}

![Refer to caption](mixed_pi_path_unstable_extended_v3.png)


(b) p>p¯p>\bar{p}

Figure 4: Mixed Solution: Realized Inflation Path for a Four-Quarter Shock with ℓ=16\ell=16

Focusing on the left panel first, we note that for a low realized duration of just one year, the equilibrium path looks similar from the one we would get under a standard Markov chain: inflation looks like it is decreasing on impact to a constant level π\pi and stays there for 4 periods until shooting back up to its steady state of 0 as soon as the shock vanishes. Strictly speaking, this is not what is happening here. Instead, the equilibrium path for inflation is not constant over time. It is clearly apparent that, if the shock were to last for 3 years until time period t+11t+11, the path of inflation would be inching its way up towards 0 and in fact would be above π¯\underline{\pi}. In the existing literature which focuses on the limit as ℓ→∞\ell\to\infty, that slow climb towards 0 never actually happens and what is left is the almost constant path that shows up for the first few periods in figure [4](https://arxiv.org/html/2511.04782v1#S3.F4 "Figure 4 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). In the limit as ℓ=+∞\ell=+\infty, that path actually becomes constant.

One can see immediately that this is not what is happening as soon as p>p¯p>\overline{p}. In that case, the unstable dynamics are such that the economy never settles down to a constant equilibrium in the short or medium run. As ℓ\ell grows larger, the impact effect on inflation grows more and more negative. For the following periods, inflation climbs back up and shoots back to steady state immediately if the shock subsides after less than ℓ\ell periods. The papers in the existing literature do not recover this equilibrium path because they focus on constant allocations.

Taken together, propositions [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") and [5](https://arxiv.org/html/2511.04782v1#Thmprop5 "Proposition 5 (Mixed solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") completely characterize what can happen in this model in the sense that it exhausts all the possibilities for a given triplet p,d,ℓp,d,\ell. In order to visualize these possibilities, we provide a figure that is very close in spirit to Figure [2](https://arxiv.org/html/2511.04782v1#S2.F2 "Figure 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."). In sharp contrast with Figure [2](https://arxiv.org/html/2511.04782v1#S2.F2 "Figure 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") however, we do not flag the number of MSV solutions since there is only one for all parameter configurations. Instead, we flag the type of the solution.

![Refer to caption](Figure5.png)


Figure 5: Types of MSV Solutions in (p,d)(p,d) space for a given ℓ<∞\ell<\infty.

Figure [5](https://arxiv.org/html/2511.04782v1#S3.F5 "Figure 5 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") is a more general version of Figure [2](https://arxiv.org/html/2511.04782v1#S2.F2 "Figure 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") in the sense that it contains it as a special case. Take the top-right region from Figure [2](https://arxiv.org/html/2511.04782v1#S2.F2 "Figure 2 ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") where there is no MSV equilibrium at all. This is because the researchers studying this configuration guess a constant solution and then try to verify it. They find that no solution can verify that guess. Figure [5](https://arxiv.org/html/2511.04782v1#S3.F5 "Figure 5 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") explains why that is the case: there exists a unique solution, but it is both unstable and time-varying. Even though the shock becomes a standard Markov chain as ℓ→∞\ell\to\infty, the solution of the model does not converge to the guessed solution under a Markov chain.

Take now the region where there are two MSV equilibria. In that case, researchers typically choose to focus on the one where the ELB is a binding constraint. There is however no compelling reason why this equilibrium should materialize instead of the one where the ELB doesn’t bind. Our equilibrium construction resolves this issue entirely. Given a triplet p,d,ℓp,d,\ell, one can construct the allocation right before the shock vanishes. If d<d¯​(p)d<\overline{d}(p), then our equilibrium construction picks the pure normal times solution for all values of ℓ\ell. If d>d¯​(p)d>\overline{d}(p) instead, it picks an mixed solution where the ELB binds on impact only if ℓ≥ℓ¯\ell\geq\overline{\ell}.

When there is a unique MSV solution, our equilibrium construction gives the same as ℓ→∞\ell\to\infty. Therefore, discrepancies between our equilibrium construction and the one in the literature only arise if p>p¯p>\overline{p}: the literature finds a stable, constant solution while we find a time-varying, unstable one. As alluded to in the introduction, the standard practice in the literature is to consider an analytical continuation. More precisely, the impact effect of the shock on inflation can be shown to be given by the following expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π~t​(ℓ)\displaystyle\tilde{\pi}\_{t}(\ell) | =V2⊤​[∑i=0ℓ−1(p​𝐀∗)i]​(C⋅d+E)\displaystyle=V\_{2}^{\top}\left[\sum\_{i=0}^{\ell-1}(p\mathbf{A}^{\*})^{i}\right](C\cdot d+E) |  |

where V2=[0 1]⊤V\_{2}=\left[0\ \ 1\right]^{\top}. The radius of convergence for this series is given by ρ​(p​𝐀∗)<1\rho(p\mathbf{A}^{\ast})<1, where ρ​(⋅)\rho(\cdot) denotes the spectral radius (maximum absolute eigenvalue). As ℓ→∞\ell\to\infty, if ρ​(p​𝐀∗)<1\rho(p\mathbf{A}^{\ast})<1 then the matrix geometric series converges to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π~t​(∞)\displaystyle\tilde{\pi}\_{t}(\infty) | =V2⊤​(I−p​𝐀∗)−1​(C⋅d+E)\displaystyle=V\_{2}^{\top}(I-p\mathbf{A}^{\*})^{-1}(C\cdot d+E) |  | (6) |

If ρ​(p​𝐀∗)>1\rho(p\mathbf{A}^{\ast})>1, the matrix geometric series diverges instead. In that context the analytical continuation given by equation ([6](https://arxiv.org/html/2511.04782v1#S3.E6 "Equation 6 ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")) is still well defined as long as det(p​𝐀∗−I)≠0\det(p\mathbf{A}^{\ast}-I)\neq 0. This is where we depart with the existing literature: we choose to keep ℓ\ell finite and work with the geometric sum while the existing literature usually chooses to take ℓ=+∞\ell=+\infty and work with the analytical continuation.777Note that, strictly speaking, Eggertsson & Woodford, ([2003](https://arxiv.org/html/2511.04782v1#bib.bib16)) as well as Eggertsson et al., ([2021](https://arxiv.org/html/2511.04782v1#bib.bib15)) work with a finite value of ℓ\ell as well. However, they usually set a very high value of ℓ\ell in order to closely approximate a Markov chain. We take the view that shocks have a moderate duration ℓ\ell and as a result should not necessarily approximate a pure Markov chain.

Beyond these discrepancies, all the situations that we have highlighted share the same qualitative property: both inflation and the output gap fall on impact. The magnitude may vary across cases, but the decrease is there no matter what. Given the findings reported in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) as well as Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) and all the literature that ensued, the same clearly cannot be said about the effects of fiscal policy depending on whether p≶p¯p\lessgtr\overline{p}. This begs the following question: what does our equilibrium construction predict for the effects of government spending at the ELB? We jump to this issue next.

## 4 Characterizing Fiscal Policy at the ELB

The framework that we have developed in the previous section gives a unique answer to the question: what happens after the economy is hit with a negative demand shock? In that setup, as we have seen, the economy ends up at the ELB if the shock is both large and persistent enough. We do not need to invoke a sunspot for that to happen. Therefore, this framework helps us understand how and under which conditions the economy ends up at the ELB.

Ultimately however, policymakers want to know what to do once they find themselves in that position. In other words, we want to understand the effect of policy in that context. In the existing literature, the standard New Keynesian model only gives mixed recommendations: if the economy is at the ELB because of a mildly persistent demand shock, then increasing government spending will crowd private consumption in. If the economy is at the ELB because there are two MSV equilibria and we pick the one with a binding ELB, then increasing government spending crowds private consumption out. The objective of this section is to show that the framework that we have developed in the previous section does not give mixed recommendations at the ELB: the sign of the effect on consumption never flips.

Before we go on to describe the effects of government spending at the ELB, we first establish some results about the government spending multiplier in a pure normal time regime. Given the result in the previous section, this regime applies if the demand shock is such that d<d¯​(p)d<\overline{d}(p) regardless of the value of pp. Given the presence of government spending, in what follows we will focus our attention on the impact effect on private consumption. Indeed, the government spending multiplier effect on output will be strictly larger/smaller than 1 if and only if the effect on consumption is strictly larger/smaller than 0. In that context, it will be useful to define mgc,R​(ℓ)m^{c,R}\_{g}(\ell) as the impact multiplier effect for a given ℓ\ell and where the regime RR takes values in {P​N,P​L,M}\left\{PN,PL,M\right\}. We characterize the multiplier as a function of ℓ\ell in the following proposition.

###### Proposition 6 (Multiplier in Normal Times).

Assume that assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") holds and that, for a given pp, we have d<d¯​(p)d<\overline{d}(p). Then the impact effect on private consumption mgc,P​N​(ℓ)m^{c,PN}\_{g}(\ell) is such that:

* •

  mgc,P​N​(ℓ)≤0m^{c,PN}\_{g}(\ell)\leq 0 for all ℓ≥1\ell\geq 1
* •

  limℓ→∞mgc,P​N​(ℓ)=mgc,P​N<0\lim\_{\ell\to\infty}m^{c,PN}\_{g}(\ell)=m^{c,PN}\_{g}<0

###### Proof.

Given our focus on the multiplier at the ELB, we relegate this proof to the online Appendix, section B.
∎

The main take-away from Proposition [6](https://arxiv.org/html/2511.04782v1#Thmprop6 "Proposition 6 (Multiplier in Normal Times). ‣ 4 Characterizing Fiscal Policy at the ELB ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") is that, regardless of the maximum duration ℓ\ell, the government spending multiplier on consumption is negative and it converges to the value mgc,P​N<0m^{c,PN}\_{g}<0 that obtains using a standard Markov chain as ℓ→∞\ell\to\infty. As a result, there is no scope for qualitative change888The path towards mgc,P​Nm^{c,PN}\_{g} can take on many different shapes. We give a more detailed characterization in the online appendix. in the sign of the multiplier as a function of ℓ\ell as long as the shock sends the economy in the normal times regime. Judging by the existing literature, that may be different when one considers a demand shock that is large and persistent enough to send the economy in the ELB regime.

For the sake of exposition, we begin by assuming that the demand shock is large enough (d>d¯(0))d>\overline{d}(0)) such that the economy ends up in a pure ELB regime. We characterize the properties of the impact multiplier in the following proposition.

###### Proposition 7 (Pure ELB).

Assume that assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") holds and that d≥d¯​(0)d\geq\overline{d}(0). Then it follows that, regardless of pp, the impact consumption multiplier mgc,P​L​(ℓ)m^{c,PL}\_{g}(\ell) is positive and strictly increasing in ℓ\ell. In addition, for given initial conditions mgc,P​L​(1),mgc,P​L​(2)m^{c,PL}\_{g}(1),m^{c,PL}\_{g}(2), the impact consumption multiplier can be written as the following AR(2) process999where the constant cm∗c^{\*}\_{m} is defined by the time-invariant PL multiplier mgP​L​(∞)m\_{g}^{PL}(\infty) and the coefficients from the characteristic polynomial of p​𝐀∗p\mathbf{\mathbf{A}^{\*}}:

cm∗:=(1−τp∗+δp∗)​mgP​L​(∞)c^{\*}\_{m}\vcentcolon=\left(1-\tau\_{p}^{\*}+\delta\_{p}^{\*}\right)m\_{g}^{PL}(\infty)
In this expression, τp∗=tr⁡(p​𝐀∗)\tau\_{p}^{\*}=\operatorname{tr}(p\mathbf{A}^{\*}) is the trace of the system matrix p​𝐀∗p\mathbf{A}^{\*}, and δp∗=det(p​𝐀∗)\delta\_{p}^{\*}=\det(p\mathbf{A}^{\*}) is its determinant.:

|  |  |  |
| --- | --- | --- |
|  | mgP​L​(ℓ+2)=τp∗​mgP​L​(ℓ+1)−δp∗​mgP​L​(ℓ)+cm∗\displaystyle m\_{g}^{PL}(\ell+2)=\tau\_{p}^{\*}m\_{g}^{PL}(\ell+1)-\delta\_{p}^{\*}m\_{g}^{PL}(\ell)+c^{\*}\_{m} |  |

for ℓ≥1\ell\geq 1. Further, there exists a threshold p¯\overline{p} such that:

* •

  limℓ→∞mgc,P​L​(ℓ)>0\lim\_{\ell\to\infty}m^{c,PL}\_{g}(\ell)>0 if p<p¯p<\overline{p}
* •

  limℓ→∞mgc,P​L​(ℓ)=+∞\lim\_{\ell\to\infty}m^{c,PL}\_{g}(\ell)=+\infty if p≥p¯p\geq\overline{p}

###### Proof.

See Appendix [A.5](https://arxiv.org/html/2511.04782v1#S1.SS5 "A.5 Proof of Proposition 7 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").
∎

The main take-away here is that the consumption multiplier is guaranteed to be positive at the ELB. This is a consequence of our earlier findings in the previous section. Another feature of Proposition [7](https://arxiv.org/html/2511.04782v1#Thmprop7 "Proposition 7 (Pure ELB). ‣ 4 Characterizing Fiscal Policy at the ELB ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") worth flagging is the AR(2) representation for the impact multiplier on consumption that we alluded to in the introduction. It turns out that the solution constructed in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) is a bona fide fixed point of this recursion. However, the fact that ρ​(p​𝐀∗)>1\rho(p\mathbf{A}^{\ast})>1 prevents the AR(2) to converge to that solution: it diverges instead. Using standard methods, one can solve for mgc,P​L​(ℓ)m^{c,PL}\_{g}(\ell) and obtain a geometric sum. As before, the solution considered in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) is the analytical continuation defined outside the convergence radius of the geometric sum. This is the reason why their construction does not arise as an equilibrium in our setup with finite ℓ\ell —even if that ℓ\ell is made to be arbitrarily large. As a result, the result of a crowding-out effect highlighted in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) does not arise here. For the same parameter configuration that was employed in that paper, the effect on private consumption is both positive and growing with ℓ\ell. As a result, for once in Economics the answer is not ”it depends”: a policy maker using this model necessarily concludes that fiscal policy has a positive effect on private consumption at the ELB.

The findings that we have reported so far pertain to the solutions where the economy stays in the same regime (Normal times or ELB) for all time periods. This begs for the following question: what happens for a mixed solution where the economy is at the ELB in the short run and goes back to normal times before the shock is over? In that case, part of the increase in government expenses happens when the economy has left the ELB. As a result, one can expect the impact multiplier effect to depend crucially on ℓ\ell as it can be shown that if that ℓ\ell is large enough this economy spends a comparatively longer time at the ELB. In the following proposition, we describe how different the impact multiplier effect under a mixed solution is compared to a pure solution.

###### Proposition 8.

Assume that assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") holds and that d¯​(p)<d<d¯​(0)\overline{d}(p)<d<\overline{d}(0). Then it follows that there exists a time period NN for which c~t+k\tilde{c}\_{t+k} is outside the ELB regime for k=N+1,…k=N+1,\dots. Given this, the impact multiplier on consumption is such that

* •

  mgc,M​(k)=mgc,P​N​(k)m^{c,M}\_{g}(k)=m^{c,PN}\_{g}(k) for k=0,…,Nk=0,\dots,N.
* •

  there exists a threshold ℓ+\ell^{+} such that mgc,M​(ℓ)>0m^{c,M}\_{g}(\ell)>0 for all ℓ≥ℓ+\ell\geq\ell^{+}.
* •

  limℓ→∞mgc,M​(ℓ)=mgc,P​L​(ℓ)\lim\_{\ell\to\infty}m^{c,M}\_{g}(\ell)=m^{c,PL}\_{g}(\ell) if and only if p<p¯p<\overline{p}, otherwise it diverges to +∞+\infty.

###### Proof.

See Appendix [A.6](https://arxiv.org/html/2511.04782v1#S1.SS6 "A.6 Proof of Proposition 8 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").
∎

In words, for low values of ℓ\ell the multiplier sequence behaves just as the one where the ELB never binds. When ℓ\ell is sufficiently large however, the impact multiplier becomes positive. Eventually, as ℓ\ell becomes arbitrarily large, the multiplier converges to the same sequence as in a pure ELB solution. We depict a typical sequence for a mixed solution in the figure below.

![Refer to caption](Figure6.png)


Figure 6: Illustration of the multiplier dynamics in the mixed regime

By and large, our conclusion at this point is that the graphical depictions that were introduced both in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) and Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) are extremely useful. The one in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) tells us what to expect in terms of multiplier effects when ℓ\ell takes on a large value. The one in Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)) does not give us a multiplier that we can use, but instead it can tell us when the multiplier grows arbitrarily large with ℓ\ell.

## 5 Conclusion

Using a truncated Markov chain, we have shown that one can study the unique path back to the intended steady state in a standard New Keynesian model with an occasionally binding ELB. That shock structure gave us some insights about the results in Eggertsson, ([2011](https://arxiv.org/html/2511.04782v1#bib.bib14)) and Mertens & Ravn, ([2014](https://arxiv.org/html/2511.04782v1#bib.bib23)). The first one arises as a limit of our approach when persistence is low, but the second one doesn’t. In that context, we have found that fiscal policy through higher expenditures unambiguously increases private consumption at the ELB.

The simple framework that we have considered allowed us to prove formally a number of existence and uniqueness results. It also lead us to the conclusion that the range of parameters that injects a puzzle in the model is much larger than commonly believe.

The natural question that arises then is: what would the prevalence of puzzles look like in a more general model that features endogenous persistence in the form of capital accumulation, consumption habit or inflation indexation? We are tackling this issue in ongoing work.

## References

* Aruoba et al., (2018)

  Aruoba, B., Cuba-Borda, P., & Schorfheide, F. (2018).
  Macroeconomic Dynamics Near the ZLB: A Tale of Two Countries.
  The Review of Economic Studies, 85, 87–118.
* Ascari & Mavroeidis, (2022)

  Ascari, G. & Mavroeidis, S. (2022).
  The unbearable lightness of equilibria in a low interest rate environment.
  Journal of Monetary Economics, 127, 1–17.
* Ascari et al., (2023)

  Ascari, G., Mavroeidis, S., & McClung, N. (2023).
  Coherence without rationality at the zero lower bound.
  Journal of Economic Theory, 214, 105745.
* Benhabib et al., (2001)

  Benhabib, J., Schmitt-Grohé, S., & Uribe, M. (2001).
  The perils of taylor rules.
  Journal of Economic Theory, 96(1-2), 40–69.
* Bilbiie, (2022)

  Bilbiie, F. O. (2022).
  Neo-fisherian policies and liquidity traps.
  American Economic Journal: Macroeconomics, 14(4), 378–403.
* Cai et al., (2025)

  Cai, C., Roulleau-Pasdeloup, J., & Zheng, Z. (2025).
  Endogenous persistence at the effective lower bound.
  arXiv preprint arXiv:2501.06473.
* Carlstrom et al., (2015)

  Carlstrom, C. T., Fuerst, T. S., & Paustian, M. (2015).
  Inflation and output in new keynesian models with a transient interest rate peg.
  Journal of Monetary Economics, 76, 230–243.
* Christiano et al., (2011)

  Christiano, L., Eichenbaum, M., & Rebelo, S. (2011).
  When is the government spending multiplier large?
  Journal of Political Economy, 119(1), 78–121.
* Del Negro et al., (2023)

  Del Negro, M., Giannoni, M. P., & Patterson, C. (2023).
  The forward guidance puzzle.
  Journal of Political Economy Macroeconomics, 1(1), 43–79.
* Diba & Loisel, (2021)

  Diba, B. & Loisel, O. (2021).
  Pegging the interest rate on bank reserves: a resolution of new keynesian puzzles and paradoxes.
  Journal of Monetary Economics, 118, 230–244.
* Dordal-i Carreras et al., (2016)

  Dordal-i Carreras, M., Coibion, O., Gorodnichenko, Y., & Wieland, J. (2016).
  Infrequent but long-lived zero-bound episodes and the optimal rate of inflation.
* Dupraz & Marx, (2025)

  Dupraz, S. & Marx, M. (2025).
  Keeping control over boundedly rational expectations.
  Bank de France manuscript.
* Eggertsson, (2010)

  Eggertsson, G. (2010).
  The paradox of toil.
  Technical report, Staff report.
* Eggertsson, (2011)

  Eggertsson, G. B. (2011).
  What fiscal policy is effective at zero interest rates?
  NBER macroeconomics annual, 25(1), 59–112.
* Eggertsson et al., (2021)

  Eggertsson, G. B., Egiev, S. K., Lin, A., Platzer, J., & Riva, L. (2021).
  A toolkit for solving models with a lower bound on interest rates of stochastic duration.
  Review of Economic Dynamics, 41, 121–173.
* Eggertsson & Woodford, (2003)

  Eggertsson, G. B. & Woodford, M. (2003).
  Optimal monetary policy in a liquidity trap.
* Eskelinen et al., (2024)

  Eskelinen, M., Gibbs, C. G., McClung, N., et al. (2024).
  Resolving new keynesian puzzles.
  Technical report, Bank of Finland.
* Gibbs & McClung, (2023)

  Gibbs, C. G. & McClung, N. (2023).
  Does my model predict a forward guidance puzzle?
  Review of Economic Dynamics, 51, 393–423.
* Gust et al., (2022)

  Gust, C., Herbst, E., & López-Salido, D. (2022).
  Short-term planning, monetary policy, and macroeconomic persistence.
  American Economic Journal: Macroeconomics, 14(4), 174–209.
* Gust et al., (2024)

  Gust, C., Herbst, E., & Lopez-Salido, D. (2024).
  Inflation expectations with finite horizon planning.
* Hills & Nakata, (2018)

  Hills, T. S. & Nakata, T. (2018).
  Fiscal Multipliers at the Zero Lower Bound: The Role of Policy Inertia.
  Journal of Money, Credit and Banking, 50, 155–172.
* Leeper et al., (2017)

  Leeper, E. M., Traum, N., & Walker, T. B. (2017).
  Clearing up the fiscal multiplier morass.
  American Economic Review, 107(8), 2409–2454.
* Mertens & Ravn, (2014)

  Mertens, K. R. & Ravn, M. O. (2014).
  Fiscal policy in an expectations-driven liquidity trap.
  The Review of Economic Studies, (pp. 1637–1667).
* Michaillat & Saez, (2021)

  Michaillat, P. & Saez, E. (2021).
  Resolving new keynesian anomalies with wealth in the utility function.
  Review of Economics and Statistics, 103(2), 197–215.
* Miyamoto et al., (2018)

  Miyamoto, W., Nguyen, T. L., & Sergeyev, D. (2018).
  Government Spending Multipliers under the Zero Lower Bound: Evidence from Japan.
  American Economic Journal: Macroeconomics, 10, 247–277.
* Murakami et al., (2023)

  Murakami, D., Shchapov, I., & Zhang, Y. (2023).
  Restoring Existence and Uniqueness at the Effective Lower Bound with Simple Fiscal Policy.
  Technical report, Technical report. working paper.
* Nakamura et al., (2025)

  Nakamura, E., Riblier, V., & Steinsson, J. (2025).
  Beyond the Taylor Rule.
  Technical report, National Bureau of Economic Research.
* Nakata & Schmidt, (2022)

  Nakata, T. & Schmidt, S. (2022).
  Expectations-Driven Liquidity Traps: Implications for Monetary and Fiscal Policy.
  American Economic Journal: Macroeconomics, 14, 68–103.
* Schmidt, (2017)

  Schmidt, S. (2017).
  Fiscal Activism and the Zero Nominal Interest Rate Bound.
  Journal of Money, Credit and Banking, 49, 695–732.
* Wieland, (2018)

  Wieland, J. F. (2018).
  State-Dependence of the Zero Lower Bound Government Spending Multiplier.
  Working Paper, University of California San Diego.
* Wieland, (2019)

  Wieland, J. F. (2019).
  Zero Lower Bound Government Spending Multipliers and Equilibrium Selection.
  Working Paper, University of California San Diego.
* Woodford, (2011)

  Woodford, M. (2011).
  Simple analytics of the government expenditure multiplier.
  American Economic Journal: Macroeconomics, 3(1), 1–35.
* Woodford, (2019)

  Woodford, M. (2019).
  Monetary policy analysis when planning horizons are finite.
  NBER macroeconomics annual, 33(1), 1–50.

## A Appendix

### A.1 Proof of Proposition [2](https://arxiv.org/html/2511.04782v1#Thmprop2 "Proposition 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")

###### Proof.

The proof proceeds by construction. We solve the system for each of the two linear regimes implied by the max\max operator. We then establish the conditions on dd under which each solution is valid and show that these conditions form a partition of the domain of dd, guaranteeing a unique solution. The proof is structured by analyzing two distinct cases.

##### Case 1: Non-binding ELB (ψ​π~t+ℓ−1>−μ\psi\tilde{\pi}\_{t+\ell-1}>-\mu).

In this case, the system is linear and given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~t+ℓ−1\displaystyle\tilde{x}\_{t+\ell-1} | =−σ​ψ​π~t+ℓ−1−d\displaystyle=-\sigma\psi\tilde{\pi}\_{t+\ell-1}-d |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | π~t+ℓ−1\displaystyle\tilde{\pi}\_{t+\ell-1} | =λ​x~t+ℓ−1\displaystyle=\lambda\tilde{x}\_{t+\ell-1} |  |

Substituting the second equation into the first and solving yields the unique solution for this case:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π~t+ℓ−1N\displaystyle\tilde{\pi}\_{t+\ell-1}^{N} | =−λ1+λ​σ​ψ​d\displaystyle=-\frac{\lambda}{1+\lambda\sigma\psi}d |  | (A.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x~t+ℓ−1N\displaystyle\tilde{x}\_{t+\ell-1}^{N} | =−11+λ​σ​ψ​d\displaystyle=-\frac{1}{1+\lambda\sigma\psi}d |  | (A.2) |

This solution is valid if and only if it satisfies the initial condition for this case, ψ​π~t+ℓ−1N>−μ\psi\tilde{\pi}\_{t+\ell-1}^{N}>-\mu. This implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −ψ​λ​d1+λ​σ​ψ>−μ⇒d<μλ​ψ​(1+λ​σ​ψ).-\frac{\psi\lambda d}{1+\lambda\sigma\psi}>-\mu\quad\Rightarrow\quad d<\frac{\mu}{\lambda\psi}(1+\lambda\sigma\psi). |  | (A.3) |

##### Case 2: Binding ELB (ψ​π~t+ℓ−1≤−μ\psi\tilde{\pi}\_{t+\ell-1}\leq-\mu).

In this case, the system is linear and given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~t+ℓ−1\displaystyle\tilde{x}\_{t+\ell-1} | =σ​μ−d\displaystyle=\sigma\mu-d |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | π~t+ℓ−1\displaystyle\tilde{\pi}\_{t+\ell-1} | =λ​x~t+ℓ−1\displaystyle=\lambda\tilde{x}\_{t+\ell-1} |  |

The unique solution for this case is therefore:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π~t+ℓ−1L\displaystyle\tilde{\pi}\_{t+\ell-1}^{L} | =λ​(σ​μ−d)\displaystyle=\lambda(\sigma\mu-d) |  | (A.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x~t+ℓ−1L\displaystyle\tilde{x}\_{t+\ell-1}^{L} | =σ​μ−d\displaystyle=\sigma\mu-d |  | (A.5) |

This solution is valid if and only if it satisfies the condition ψ​π~t+ℓ−1L≤−μ\psi\tilde{\pi}\_{t+\ell-1}^{L}\leq-\mu. This implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​λ​(σ​μ−d)≤−μ⇒d≥σ​μ+μλ​ψ.\psi\lambda(\sigma\mu-d)\leq-\mu\quad\Rightarrow\quad d\geq\sigma\mu+\frac{\mu}{\lambda\psi}. |  | (A.6) |

Let us define the threshold d¯​(1)≡σ​μ+μλ​ψ=μλ​ψ​(1+λ​σ​ψ)\bar{d}(1)\equiv\sigma\mu+\frac{\mu}{\lambda\psi}=\frac{\mu}{\lambda\psi}(1+\lambda\sigma\psi). The conditions for the validity of the solution in each case are therefore d<d¯​(1)d<\bar{d}(1) for the Normal Time regime and d≥d¯​(1)d\geq\bar{d}(1) for the ELB regime. These two conditions are mutually exclusive and exhaustive over the domain of dd. Thus, for any given value of dd, a valid solution exists in one and only one of the two cases. This concludes the proof.
∎

### A.2 Proof of Proposition [3](https://arxiv.org/html/2511.04782v1#Thmprop3 "Proposition 3. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")

###### Lemma 1 (Reversion to Steady State).

Under Assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), if the shock process ends by period t+ℓt+\ell, the unique non-explosive equilibrium path for all subsequent periods is the zero steady state, i.e., X~t+ℓ+k=𝟎2×1\tilde{X}\_{t+\ell+k}=\mathbf{0}\_{2\times 1} for all k≥0k\geq 0.

###### Proof.

Once the shock has ended (for periods j≥t+ℓj\geq t+\ell), we have dj=0d\_{j}=0 and the system becomes deterministic. We define the state vector as Xj≡[x~j,π~j]′X\_{j}\equiv[\tilde{x}\_{j},\tilde{\pi}\_{j}]^{\prime}. The model can then be written in the forward-looking form 𝔼j​Xj+1=J​Xj\mathbb{E}\_{j}X\_{j+1}=JX\_{j}, where J=A1−1​A0J=A\_{1}^{-1}A\_{0}. The eigenvalues of this transition matrix JJ determine the system’s dynamics.

As shown in the main text, the matrix AA in the backward-looking representation Xj=A​Xj+1X\_{j}=AX\_{j+1} is the inverse of JJ. The eigenvalues of AA, ΛA\Lambda\_{A}, are the reciprocals of the eigenvalues of JJ, ΛJ\Lambda\_{J}. Assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") ensures that the eigenvalues of AA are within the unit circle (|ΛA|<1|\Lambda\_{A}|<1), which is the standard Blanchard-Kahn condition.

Equivalently, this implies that the eigenvalues of the forward-looking matrix JJ are all outside the unit circle (|ΛJ|>1|\Lambda\_{J}|>1). For a deterministic system, this means that the only non-explosive path is for the state to be at the steady state, Xj=𝟎2×1X\_{j}=\mathbf{0}\_{2\times 1}. Therefore, once the shock ends, the system immediately and permanently reverts to the zero steady state.
∎

###### Proof.

We prove the uniqueness of the solution path {x~t+k,π~t+k}\{\tilde{x}\_{t+k},\tilde{\pi}\_{t+k}\} for all k≥0k\geq 0. The proof proceeds by backward induction.

##### Base Case.

The induction begins with the terminal period of the shock, k=ℓ−1k=\ell-1. From Lemma [1](https://arxiv.org/html/2511.04782v1#Thmlemma1 "Lemma 1 (Reversion to Steady State). ‣ A.2 Proof of Proposition 3 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), we know that the state of the economy will be zero for all subsequent periods, which uniquely determines the expectations at t+ℓ−1t+\ell-1 to be 𝔼t+ℓ−1​[X~t+ℓ]=0\mathbb{E}\_{t+\ell-1}[\tilde{X}\_{t+\ell}]=0. With these expectations, the system governing (x~t+ℓ−1,π~t+ℓ−1)(\tilde{x}\_{t+\ell-1},\tilde{\pi}\_{t+\ell-1}) is precisely that of Proposition [2](https://arxiv.org/html/2511.04782v1#Thmprop2 "Proposition 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), which has a unique solution. Thus, the base case holds.

##### Inductive Hypothesis.

Assume that for some period kk such that 0<k≤ℓ−10<k\leq\ell-1, the state vector X~t+k\tilde{X}\_{t+k} is uniquely determined.

##### Inductive Step.

We now show that the state vector at the prior period, X~t+k−1\tilde{X}\_{t+k-1}, must also be unique. We proceed by contradiction. Suppose that both the Normal and ELB regimes satisfy their respective verification conditions at time t+k−1t+k-1. Let us define the terms determined by the unique expectations of the state at t+kt+k:

|  |  |  |
| --- | --- | --- |
|  | ℰt+k−1≡λ​p​mx​x​x~t+k+p​(λ​σ​mx​π+mπ​π​β)​π~t+k−λ​d.\mathscr{E}\_{t+k-1}\equiv\lambda pm\_{xx}\tilde{x}\_{t+k}+p(\lambda\sigma m\_{x\pi}+m\_{\pi\pi}\beta)\tilde{\pi}\_{t+k}-\lambda d. |  |

The verification conditions for each regime are:

1. (i)

   Normal regime is valid ⇔ℰt+k−1>−(1+λ​σ​ψ)​μψ\Leftrightarrow\mathscr{E}\_{t+k-1}>-(1+\lambda\sigma\psi)\frac{\mu}{\psi}.
2. (ii)

   ELB regime is valid ⇔ℰt+k−1≤−(1+λ​σ​ψ)​μψ\Leftrightarrow\mathscr{E}\_{t+k-1}\leq-(1+\lambda\sigma\psi)\frac{\mu}{\psi}.

These two conditions are mutually exclusive. It is a contradiction for both to hold simultaneously. Therefore, at most one regime can be valid. Since a solution is guaranteed to exist, the solution at t+k−1t+k-1 must be unique.

##### Conclusion.

By backward induction, the path {X~t+k}k=0ℓ−1\{\tilde{X}\_{t+k}\}\_{k=0}^{\ell-1} is uniquely determined. Combined with the result from Lemma [1](https://arxiv.org/html/2511.04782v1#Thmlemma1 "Lemma 1 (Reversion to Steady State). ‣ A.2 Proof of Proposition 3 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") for k≥ℓk\geq\ell, the solution path is unique for all k≥0k\geq 0. This concludes the proof.
∎

### A.3 Proof of Proposition [4](https://arxiv.org/html/2511.04782v1#Thmprop4 "Proposition 4 (pure solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")

#### Proof of the First Statement (Pure Normal-Time Regime)

We begin by proving the first statement of the proposition: if d∈[0,d¯​(p)]d\in[0,\overline{d}(p)], the economy remains in the normal-time regime for all periods, and the solution path converges to a finite limit as ℓ→∞\ell\to\infty. The proof proceeds by establishing two intermediate results. First, we characterize the dynamics of the hypothetical pure normal-time solution path. Second, we derive the conditions under which this path constitutes a valid equilibrium.

The system of equations for the normal-time regime can be written in matrix form as X~t=𝐀​𝔼t​X~t+1+C​dt\tilde{X}\_{t}=\mathbf{A}\mathbb{E}\_{t}\tilde{X}\_{t+1}+Cd\_{t}, where X~t=[x~t,π~t]′\tilde{X}\_{t}=[\tilde{x}\_{t},\tilde{\pi}\_{t}]^{\prime} and

|  |  |  |
| --- | --- | --- |
|  | 𝐀=11+λ​σ​ψ​(mx​xσ​(mx​π−ψ​β​mπ​π)λ​mx​xλ​σ​mx​π+β​mπ​π),C=−11+λ​σ​ψ​(1λ).\mathbf{A}=\frac{1}{1+\lambda\sigma\psi}\begin{pmatrix}m\_{xx}&\sigma(m\_{x\pi}-\psi\beta m\_{\pi\pi})\\ \lambda m\_{xx}&\lambda\sigma m\_{x\pi}+\beta m\_{\pi\pi}\end{pmatrix},\quad C=\frac{-1}{1+\lambda\sigma\psi}\begin{pmatrix}1\\ \lambda\end{pmatrix}. |  |

Given the truncated Markov process for the shock dt=dd\_{t}=d, which lasts for a maximum of ℓ\ell periods with persistence pp, the solution at time tt can be found by backward induction:

|  |  |  |
| --- | --- | --- |
|  | X~t​(ℓ)=[∑i=0ℓ−1(p​𝐀)i]​C​d.\tilde{X}\_{t}(\ell)=\left[\sum\_{i=0}^{\ell-1}(p\mathbf{A})^{i}\right]Cd. |  |

Our proof relies on the properties of the matrix p​𝐀p\mathbf{A}. Assumptions [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") and [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") ensure two crucial properties: (1) the eigenvalues of AA are real and positive, and (2) the spectral radius of p​𝐀p\mathbf{A} is less than one for all p∈[0,1]p\in[0,1], ensuring stability.101010The proofs that Assumption [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") guarantees real eigenvalues and Assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") ensures a spectral radius less than one are standard but involve detailed algebra. They are deferred to online Appendix, section C for the interested reader.

###### Lemma 2 (Dynamics of the Hypothetical Normal-Time Path).

Under Assumptions [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") and [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), the hypothetical pure normal-time solution path satisfies:

1. (i)

   Monotonicity: The path {X~t+k​(ℓ)}k=0ℓ−1\{\tilde{X}\_{t+k}(\ell)\}\_{k=0}^{\ell-1} is monotonic. The minimum values for both output gap and inflation occur on impact at time tt.
2. (ii)

   Convergence: As the maximum duration ℓ→∞\ell\to\infty, the on-impact solution converges to a finite steady state, which is the standard MSV equilibrium:
   lim\_ℓ→∞ ~X\_t(ℓ) = (I - pA)^-1 C d ≡~X^N.

###### Proof of Lemma [2](https://arxiv.org/html/2511.04782v1#Thmlemma2 "Lemma 2 (Dynamics of the Hypothetical Normal-Time Path). ‣ Proof of the First Statement (Pure Normal-Time Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").

(i) Under Assumption [1](https://arxiv.org/html/2511.04782v1#Thmassumption1 "Assumption 1. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), the term (N−ψ​β​mπ​π)(N-\psi\beta m\_{\pi\pi}) is positive. Since all other parameters are positive, the matrices AA and CC have element-wise sign patterns of ‘+‘ and ‘-‘, respectively. Therefore, the matrix (p​𝐀)(p\mathbf{A}) is element-wise positive, and the vector C​dCd is element-wise negative. The solution X~t​(ℓ)\tilde{X}\_{t}(\ell) is a sum of element-wise negative vectors. Increasing the maximum duration from ℓ\ell to ℓ+1\ell+1 adds another negative term, (p​𝐀)ℓ​C​d(p\mathbf{A})^{\ell}Cd, to the sum, making the solution vector X~t​(ℓ+1)\tilde{X}\_{t}(\ell+1) strictly smaller (more negative) than X~t​(ℓ)\tilde{X}\_{t}(\ell). The solution path’s monotonicity then follows from an index symmetry property, which states that the solution at period t+kt+k for a shock of maximal duration ℓ\ell is equivalent to the on-impact solution for a shock of maximal duration ℓ−k\ell-k.111111Formally, this index symmetry property states that X~t+k​(ℓ)=X~t​(ℓ−k)\tilde{X}\_{t+k}(\ell)=\tilde{X}\_{t}(\ell-k). This result follows directly from the recursive structure of the backward induction solution. A detailed proof can be found in the online Appendix, section C. Thus, the path {π~t+k​(ℓ)}k=0ℓ−1\{\tilde{\pi}\_{t+k}(\ell)\}\_{k=0}^{\ell-1} is lowest at k=0k=0.

(ii) The stability condition from Assumption [2](https://arxiv.org/html/2511.04782v1#Thmassumption2 "Assumption 2. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), ρ​(p​𝐀)<1\rho(p\mathbf{A})<1, ensures that the geometric matrix series converges as ℓ→∞\ell\to\infty. The limit is the standard solution for an infinite geometric series, ∑i=0∞(p​𝐀)i=(I−p​𝐀)−1\sum\_{i=0}^{\infty}(p\mathbf{A})^{i}=(I-p\mathbf{A})^{-1}. This directly yields the stated limit, which corresponds to the time-invariant MSV solution derived in Proposition [1](https://arxiv.org/html/2511.04782v1#Thmprop1 "Proposition 1. ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").
∎

With the dynamics of the hypothetical path established, we now determine when it is a valid equilibrium.

###### Lemma 3 (Validity of the Normal-Time Solution).

The pure normal-time solution is the valid and unique equilibrium if and only if d∈[0,d¯​(p)]d\in[0,\overline{d}(p)].

###### Proof of Lemma [3](https://arxiv.org/html/2511.04782v1#Thmlemma3 "Lemma 3 (Validity of the Normal-Time Solution). ‣ Proof of the First Statement (Pure Normal-Time Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").

For the normal-time solution to be valid, the nominal interest rate must remain above its lower bound for the entire duration of the shock: ψ​π~t+k​(ℓ)>−μ\psi\tilde{\pi}\_{t+k}(\ell)>-\mu for all k∈[0,ℓ−1]k\in[0,\ell-1] and for all possible ℓ≥1\ell\geq 1.

From Lemma [2](https://arxiv.org/html/2511.04782v1#Thmlemma2 "Lemma 2 (Dynamics of the Hypothetical Normal-Time Path). ‣ Proof of the First Statement (Pure Normal-Time Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), we know the inflation path is monotonic and its minimum value occurs at tt (on impact). Therefore, the verification condition for the entire path simplifies to a single condition on the on-impact inflation:

|  |  |  |
| --- | --- | --- |
|  | ψ​π~t​(ℓ)>−μ⇔π~t​(ℓ)>−μψ.\psi\tilde{\pi}\_{t}(\ell)>-\mu\quad\Leftrightarrow\quad\tilde{\pi}\_{t}(\ell)>-\frac{\mu}{\psi}. |  |

Furthermore, we know from Lemma [2](https://arxiv.org/html/2511.04782v1#Thmlemma2 "Lemma 2 (Dynamics of the Hypothetical Normal-Time Path). ‣ Proof of the First Statement (Pure Normal-Time Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") that π~t​(ℓ)\tilde{\pi}\_{t}(\ell) is a decreasing sequence in ℓ\ell that converges from above to its limit π~N\tilde{\pi}^{N}. The tightest possible constraint is therefore the one that must hold in the limit as ℓ→∞\ell\to\infty:

|  |  |  |
| --- | --- | --- |
|  | limℓ→∞π~t​(ℓ)=π~N≥−μψ.\lim\_{\ell\to\infty}\tilde{\pi}\_{t}(\ell)=\tilde{\pi}^{N}\geq-\frac{\mu}{\psi}. |  |

Substituting the expression for the MSV inflation π~N\tilde{\pi}^{N} gives the condition:

|  |  |  |
| --- | --- | --- |
|  | −λ​d(1−p​mx​x)​(1−p​β​mπ​π)+λ​σ​(ψ−p​mx​π)≥−μψ.-\frac{\lambda d}{(1-pm\_{xx})(1-p\beta m\_{\pi\pi})+\lambda\sigma(\psi-pm\_{x\pi})}\geq-\frac{\mu}{\psi}. |  |

Rearranging this inequality for dd yields precisely the threshold from Proposition [1](https://arxiv.org/html/2511.04782v1#Thmprop1 "Proposition 1. ‣ 2 Picturing the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."):

|  |  |  |
| --- | --- | --- |
|  | d≤μλ​ψ​[(1−p​mx​x)​(1−p​β​mπ​π)+λ​σ​(ψ−p​mx​π)]≡d¯​(p).d\leq\frac{\mu}{\lambda\psi}\left[(1-pm\_{xx})(1-p\beta m\_{\pi\pi})+\lambda\sigma(\psi-pm\_{x\pi})\right]\equiv\overline{d}(p). |  |

If d≤d¯​(p)d\leq\overline{d}(p), the limiting inflation value satisfies the constraint. Since the entire sequence {π~t​(ℓ)}ℓ=1∞\{\tilde{\pi}\_{t}(\ell)\}\_{\ell=1}^{\infty} lies above this limit, the constraint is satisfied for all possible shock durations ℓ\ell. By Proposition [3](https://arxiv.org/html/2511.04782v1#Thmprop3 "Proposition 3. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), the solution path is unique.
∎

Combining the results of Lemma [2](https://arxiv.org/html/2511.04782v1#Thmlemma2 "Lemma 2 (Dynamics of the Hypothetical Normal-Time Path). ‣ Proof of the First Statement (Pure Normal-Time Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") and Lemma [3](https://arxiv.org/html/2511.04782v1#Thmlemma3 "Lemma 3 (Validity of the Normal-Time Solution). ‣ Proof of the First Statement (Pure Normal-Time Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") completes the proof of the first statement of the proposition.

#### Proof of the Second and Third Statements (Pure ELB Regime)

We now prove the second and third statements of the proposition, which characterize the equilibrium when the shock is large. The second statement asserts that for d>d¯​(0)d>\overline{d}(0), the economy remains in the ELB regime for all periods. The third statement describes the path’s convergence or divergence depending on the shock’s persistence pp.

In the ELB regime, the system is described by X~t=𝐀∗​𝔼t​X~t+1+C∗​dt+E∗\tilde{X}\_{t}=\mathbf{A}^{\*}\mathbb{E}\_{t}\tilde{X}\_{t+1}+C^{\*}d\_{t}+E^{\*}, where

|  |  |  |
| --- | --- | --- |
|  | 𝐀∗=(mx​xσ​mx​πλ​mx​xλ​σ​mx​π+β​mπ​π),C∗=(−1−λ),E∗=(σ​μλ​σ​μ).\mathbf{A}^{\*}=\begin{pmatrix}m\_{xx}&\sigma m\_{x\pi}\\ \lambda m\_{xx}&\lambda\sigma m\_{x\pi}+\beta m\_{\pi\pi}\end{pmatrix},\quad C^{\*}=\begin{pmatrix}-1\\ -\lambda\end{pmatrix},\quad E^{\*}=\begin{pmatrix}\sigma\mu\\ \lambda\sigma\mu\end{pmatrix}. |  |

For a shock of maximum duration ℓ\ell, the on-impact solution is found by solving the system equilibrium conditions, X~k=p​𝐀∗​X~k+1+(C∗​d+E∗)\tilde{X}\_{k}=p\mathbf{A}^{\*}\tilde{X}\_{k+1}+(C^{\*}d+E^{\*}), using backward induction. In this process, the term (C∗​d+E∗)(C^{\*}d+E^{\*}) acts as a single, constant forcing term present in each period of the shock. Starting from the terminal condition where 𝔼t+ℓ−1​[X~t+ℓ]=0\mathbb{E}\_{t+\ell-1}[\tilde{X}\_{t+\ell}]=0, this recursive substitution naturally yields a simple geometric series:

|  |  |  |
| --- | --- | --- |
|  | X~t​(ℓ)=[∑i=0ℓ−1(p​𝐀∗)i]​(C∗​d+E∗).\tilde{X}\_{t}(\ell)=\left[\sum\_{i=0}^{\ell-1}(p\mathbf{A}^{\*})^{i}\right](C^{\*}d+E^{\*}). |  |

The dynamics of this solution depend critically on the properties of the matrix p​𝐀∗p\mathbf{A}^{\*}. Its eigenvalues are always real, but its stability depends on the persistence pp.121212The proof that the eigenvalues of p​𝐀∗p\mathbf{A}^{\*} are always real is algebraic. The stability condition, ρ​(p​𝐀∗)<1\rho(p\mathbf{A}^{\*})<1, holds if and only if F​(p)≡(1−p​mx​x)​(1−p​β​mπ​π)−p​λ​σ​mx​π>0F(p)\equiv(1-pm\_{xx})(1-p\beta m\_{\pi\pi})-p\lambda\sigma m\_{x\pi}>0. The function F​(p)F(p) is a convex quadratic with F​(0)=1F(0)=1, which defines the threshold p¯∈(0,1)\overline{p}\in(0,1) as its smaller root. See the online Appendix, section C for detailed proofs.

###### Lemma 4 (Dynamics of the Hypothetical ELB Path).

The hypothetical pure ELB solution path satisfies:

1. (i)

   Monotonicity: If d>d¯​(0)d>\overline{d}(0), the path {X~t+k​(ℓ)}k=0ℓ−1\{\tilde{X}\_{t+k}(\ell)\}\_{k=0}^{\ell-1} is monotonic. The minimum values for output gap and inflation occur on impact at time tt.
2. (ii)

   Convergence and Divergence: As the maximum duration ℓ→∞\ell\to\infty, the on-impact solution either converges or diverges:

   * •

     If p<p¯p<\overline{p}, the path converges to a finite steady state: limℓ→∞X~t​(ℓ)=(I−p​𝐀∗)−1​(C∗​d+E∗)≡X~L\lim\_{\ell\to\infty}\tilde{X}\_{t}(\ell)=(I-p\mathbf{A}^{\*})^{-1}(C^{\*}d+E^{\*})\equiv\tilde{X}^{L}.
   * •

     If p≥p¯p\geq\overline{p}, the path diverges to negative infinity: limℓ→∞X~t​(ℓ)→−∞\lim\_{\ell\to\infty}\tilde{X}\_{t}(\ell)\to-\infty component-wise.

###### Proof of Lemma [4](https://arxiv.org/html/2511.04782v1#Thmlemma4 "Lemma 4 (Dynamics of the Hypothetical ELB Path). ‣ Proof of the Second and Third Statements (Pure ELB Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").

(i) The matrix p​𝐀∗p\mathbf{A}^{\*} is element-wise positive. The constant forcing term is (C∗​d+E∗)=(−d+σ​μ)​[1,λ]′(C^{\*}d+E^{\*})=(-d+\sigma\mu)[1,\lambda]^{\prime}. The condition d>d¯​(0)d>\overline{d}(0) (defined below) implies d>σ​μd>\sigma\mu, so the forcing term is element-wise negative. The solution X~t​(ℓ)\tilde{X}\_{t}(\ell) is a sum of strictly negative vectors, and is therefore strictly decreasing in ℓ\ell. Using the same index symmetry property as in the normal-time case, the minimum of the path {X~t+k​(ℓ)}\{\tilde{X}\_{t+k}(\ell)\} occurs at k=0k=0 (time tt).131313The index symmetry claim, X~t+k​(ℓ)=X~t​(ℓ−k)\tilde{X}\_{t+k}(\ell)=\tilde{X}\_{t}(\ell-k), holds for the ELB regime as well, following the same logic as the proof in online Appendix, section C.1.3.

(ii) The convergence of the geometric matrix series ∑(p​𝐀∗)i\sum(p\mathbf{A}^{\*})^{i} depends on its spectral radius, ρ​(p​𝐀∗)\rho(p\mathbf{A}^{\*}). This condition is determined by the shock’s persistence, pp. As shown in the supplementary materials (online Appendix, section C), the stability condition ρ​(p​𝐀∗)<1\rho(p\mathbf{A}^{\*})<1 is equivalent to the inequality F​(p)>0F(p)>0, where F​(p)F(p) is a quadratic in pp:

|  |  |  |
| --- | --- | --- |
|  | F​(p)≡(1−p​mx​x)​(1−p​β​mπ​π)−p​λ​σ​mx​π.F(p)\equiv(1-pm\_{xx})(1-p\beta m\_{\pi\pi})-p\lambda\sigma m\_{x\pi}. |  |

This function is convex with F​(0)=1F(0)=1 and typically crosses zero twice. We define p¯∈(0,1)\overline{p}\in(0,1) as the smaller of these two roots. Thus, the system is stable if and only if p<p¯p<\overline{p}. We analyze the solution’s limit under two cases.

Case 1: p<p¯p<\overline{p} (Convergence). In this case, ρ​(p​𝐀∗)<1\rho(p\mathbf{A}^{\*})<1. By the property of Neumann series for matrices, the infinite sum converges to a finite matrix:

|  |  |  |
| --- | --- | --- |
|  | limℓ→∞∑i=0ℓ−1(p​𝐀∗)i=(I−p​𝐀∗)−1.\lim\_{\ell\to\infty}\sum\_{i=0}^{\ell-1}(p\mathbf{A}^{\*})^{i}=(I-p\mathbf{A}^{\*})^{-1}. |  |

Consequently, the on-impact solution converges to a well-defined, finite vector corresponding to the MSV-ELB equilibrium:

|  |  |  |
| --- | --- | --- |
|  | limℓ→∞X~t​(ℓ)=(I−p​𝐀∗)−1​(C∗​d+E∗).\lim\_{\ell\to\infty}\tilde{X}\_{t}(\ell)=(I-p\mathbf{A}^{\*})^{-1}(C^{\*}d+E^{\*}). |  |

Case 2: p≥p¯p\geq\overline{p} (Divergence). In this case, ρ​(p​𝐀∗)≥1\rho(p\mathbf{A}^{\*})\geq 1. The largest eigenvalue of p​𝐀∗p\mathbf{A}^{\*} is real and greater than or equal to 1, causing the matrix series to diverge. To determine the direction of divergence, we examine the terms of the sum. The matrix p​𝐀∗p\mathbf{A}^{\*} is element-wise positive, and the forcing term (C∗​d+E∗)(C^{\*}d+E^{\*}) is element-wise negative. Therefore, each term in the solution sequence, (p​𝐀∗)i​(C∗​d+E∗)(p\mathbf{A}^{\*})^{i}(C^{\*}d+E^{\*}), is a vector of negative numbers. As ℓ→∞\ell\to\infty, we are adding an infinite number of negative vectors, and the sum diverges. Each component of the solution vector is thus driven to negative infinity:

|  |  |  |
| --- | --- | --- |
|  | limℓ→∞X~t​(ℓ)→−∞component-wise.\lim\_{\ell\to\infty}\tilde{X}\_{t}(\ell)\to-\infty\quad\text{component-wise}. |  |

This case-by-case analysis characterizes the long-run behavior of the hypothetical ELB path. This result is the key to proving the third statement of the proposition, which we will finalize after establishing the path’s validity.
∎

Having characterized the dynamics of the hypothetical ELB path, we now establish the precise conditions on the shock size dd under which this path is the valid and unique equilibrium.

###### Lemma 5 (Validity of the ELB Solution).

If d>d¯​(0)d>\overline{d}(0), the pure ELB solution is the valid and unique equilibrium.

###### Proof of Lemma [5](https://arxiv.org/html/2511.04782v1#Thmlemma5 "Lemma 5 (Validity of the ELB Solution). ‣ Proof of the Second and Third Statements (Pure ELB Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.").

For the ELB solution to be valid, the interest rate rule must select the lower bound in all periods: ψ​π~t+k​(ℓ)≤−μ\psi\tilde{\pi}\_{t+k}(\ell)\leq-\mu for all k∈[0,ℓ−1]k\in[0,\ell-1] and all ℓ≥1\ell\geq 1.

From Lemma [4](https://arxiv.org/html/2511.04782v1#Thmlemma4 "Lemma 4 (Dynamics of the Hypothetical ELB Path). ‣ Proof of the Second and Third Statements (Pure ELB Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), the path {π~t+k​(ℓ)}\{\tilde{\pi}\_{t+k}(\ell)\} is monotonically decreasing as we move backward in time from the shock’s end. This means the highest inflation value (the point most likely to violate the condition) occurs at the last period of the shock, t+ℓ−1t+\ell-1. The verification condition for the entire path thus simplifies to checking this single point:

|  |  |  |
| --- | --- | --- |
|  | ψ​π~t+ℓ−1​(ℓ)≤−μ.\psi\tilde{\pi}\_{t+\ell-1}(\ell)\leq-\mu. |  |

The solution in the final period is independent of ℓ\ell and pp, given by π~t+ℓ−1​(ℓ)=λ​(−d+σ​μ)\tilde{\pi}\_{t+\ell-1}(\ell)=\lambda(-d+\sigma\mu). Substituting this into the inequality gives:

|  |  |  |
| --- | --- | --- |
|  | ψ​λ​(−d+σ​μ)≤−μ.\psi\lambda(-d+\sigma\mu)\leq-\mu. |  |

Rearranging for dd yields the condition for the pure ELB path to be valid. This defines the threshold d¯​(0)\overline{d}(0):

|  |  |  |
| --- | --- | --- |
|  | d≥σ​μ+μλ​ψ≡d¯​(0).d\geq\sigma\mu+\frac{\mu}{\lambda\psi}\equiv\overline{d}(0). |  |

If d>d¯​(0)d>\overline{d}(0), the condition is satisfied at the path’s highest point. By monotonicity, it is satisfied everywhere else. By Proposition [3](https://arxiv.org/html/2511.04782v1#Thmprop3 "Proposition 3. ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments."), the solution is unique. This proves the second statement of Proposition 4.
∎

Combining the results of Lemma [4](https://arxiv.org/html/2511.04782v1#Thmlemma4 "Lemma 4 (Dynamics of the Hypothetical ELB Path). ‣ Proof of the Second and Third Statements (Pure ELB Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") and Lemma [5](https://arxiv.org/html/2511.04782v1#Thmlemma5 "Lemma 5 (Validity of the ELB Solution). ‣ Proof of the Second and Third Statements (Pure ELB Regime) ‣ A.3 Proof of Proposition 4 ‣ A Appendix ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") completes the proof of the second and third statements of the proposition.

### A.4 Proof of Proposition [5](https://arxiv.org/html/2511.04782v1#Thmprop5 "Proposition 5 (Mixed solutions). ‣ 3 Resolving the Morass ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")

###### Proof.

The proof for the mixed-regime case proceeds in two main stages. First, we establish the fundamental properties that any valid mixed solution must possess, particularly its structure and monotonicity. Second, we use these properties to prove the statements of the proposition.

We begin by characterizing the hypothetical mixed-regime path. The following lemma, which is central to the entire proof, shows that any mixed solution has a well-defined structure: a contiguous block of ELB periods followed by a contiguous block of normal-time periods.

###### Lemma 6 (Characterization of the Mixed Solution Path).

For a given shock (p,d,ℓ)(p,d,\ell), a valid mixed solution path {X~t+kM}k=0ℓ−1\{\tilde{X}\_{t+k}^{M}\}\_{k=0}^{\ell-1} must satisfy the following properties:

1. (i)

   Single Switching Point: There exists a unique switching point, meaning the path consists of a block of ELB periods followed by a block of normal-time periods. An N-Z-N or Z-N-Z sequence is not possible.
2. (ii)

   Monotonicity: The path {X~t+kM}k=0ℓ−1\{\tilde{X}\_{t+k}^{M}\}\_{k=0}^{\ell-1} is monotonically decreasing as we move backward in time from the shock’s end (i.e., it decreases in the original proof’s backward index kk).
3. (iii)

   Asymptotic Convergence: If p<p¯p<\overline{p}, the on-impact solution X~tM​(ℓ)\tilde{X}\_{t}^{M}(\ell) converges to the pure ELB steady state as ℓ→∞\ell\to\infty.
4. (iv)

   Asymptotic Divergence: If p≥p¯p\geq\overline{p}, the on-impact solution X~tM​(ℓ)\tilde{X}\_{t}^{M}(\ell) diverges to −∞-\infty as ℓ→∞\ell\to\infty.

###### Proof.

The proof is by induction and is technical. It first establishes that if the Normal-Time guess fails at any period kk, it must also fail for all preceding periods. This rules out an N-Z-N path and proves the single-switching-point property. The monotonicity of the path and its asymptotic behavior then follow from this established structure. The complete, detailed proof is provided in online Appendix, section C.2.1.
∎

With the structural properties of any potential mixed path characterized, we are now equipped to prove the first statement of the proposition.

###### Lemma 7 (Existence of a Mixed Solution and the Duration Threshold).

If the shock size dd satisfies d¯​(p)<d<d¯​(0)\overline{d}(p)<d<\overline{d}(0), there exists a unique integer ℓ¯≥1\overline{\ell}\geq 1 such that the equilibrium path is a pure Normal-Time solution if ℓ<ℓ¯\ell<\overline{\ell} and must be a mixed-regime path with the ELB binding on impact if ℓ≥ℓ¯\ell\geq\overline{\ell}.

###### Proof.

We prove this by analyzing the viability of pure solutions.

1. 1.

   A Pure ELB Solution is Impossible. For a pure ELB path to be valid, the condition d≥d¯​(0)d\geq\overline{d}(0) must hold. Our initial condition is d<d¯​(0)d<\overline{d}(0), which is a contradiction. The path must contain at least one normal-time period.
2. 2.

   Analysis of the Pure Normal-Time (PN) Solution. The on-impact inflation, π~t​(ℓ)\tilde{\pi}\_{t}(\ell), is a monotonically decreasing function of the shock’s duration ℓ\ell. The condition d>d¯​(p)d>\overline{d}(p) implies the limit of this sequence is below the ELB threshold, limℓ→∞π~t​(ℓ)<−μ/ψ\lim\_{\ell\to\infty}\tilde{\pi}\_{t}(\ell)<-\mu/\psi. However, the condition d<d¯​(0)d<\overline{d}(0) ensures that for ℓ=1\ell=1, inflation is above the threshold.

   Since the sequence {π~t​(ℓ)}ℓ=1∞\{\tilde{\pi}\_{t}(\ell)\}\_{\ell=1}^{\infty} starts above the threshold and converges to a value below it, there must exist a unique integer, ℓ¯\overline{\ell}, which is the smallest integer such that π~t​(ℓ¯)≤−μ/ψ\tilde{\pi}\_{t}(\overline{\ell})\leq-\mu/\psi. This leads to two distinct outcomes:

   * •

     If ℓ<ℓ¯\ell<\overline{\ell}: The on-impact inflation π~t​(ℓ)\tilde{\pi}\_{t}(\ell) remains above the threshold. By the path’s monotonicity, the ELB never binds. The equilibrium is a pure Normal-Time solution.
   * •

     If ℓ≥ℓ¯\ell\geq\overline{\ell}: Since π~t​(ℓ)\tilde{\pi}\_{t}(\ell) is a monotonically decreasing sequence, we have π~t​(ℓ)≤π~t​(ℓ¯)≤−μ/ψ\tilde{\pi}\_{t}(\ell)\leq\tilde{\pi}\_{t}(\overline{\ell})\leq-\mu/\psi for all ℓ≥ℓ¯\ell\geq\overline{\ell}. This means the on-impact inflation violates the Normal-Time condition, causing the ELB to bind on impact.

This analysis directly proves the first statement of the proposition. For a shock in the specified range, the solution is pure-normal-time for ℓ<ℓ¯\ell<\overline{\ell}. For ℓ≥ℓ¯\ell\geq\overline{\ell}, a pure PN solution is invalid, and since a pure ELB solution is also impossible, the unique equilibrium must be a mixed-regime path.
∎

The combination of these two lemmas, which characterize the mixed path and establish the conditions for its existence, completes the proof of Proposition 5.
∎

### A.5 Proof of Proposition [7](https://arxiv.org/html/2511.04782v1#Thmprop7 "Proposition 7 (Pure ELB). ‣ 4 Characterizing Fiscal Policy at the ELB ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")

###### Proof.

The proof proceeds by first deriving an analytical expression for the consumption multiplier at the ELB and then analyzing its properties.

##### The Multiplier at the ELB.

Under the condition d≥d¯​(0)d\geq\overline{d}(0), the economy is in the pure ELB regime, so the interest rate is fixed at it=−μi\_{t}=-\mu. The model with government spending gtg\_{t} can be written in matrix form as X~t=𝐀∗​𝔼t​X~t+1+Cg∗​gt+E∗\tilde{X}\_{t}=\mathbf{A}^{\*}\mathbb{E}\_{t}\tilde{X}\_{t+1}+C\_{g}^{\*}g\_{t}+E^{\*}, where X~t=[ct,πt]′\tilde{X}\_{t}=[c\_{t},\pi\_{t}]^{\prime} and

|  |  |  |
| --- | --- | --- |
|  | 𝐀∗=(mx​xσ​mx​πλ​mx​xλ​σ​mx​π+β​mπ​π),Cg∗=(0κ​η​(1−c¯)),E∗=(σ​μλ​σ​μ).\mathbf{A}^{\*}=\begin{pmatrix}m\_{xx}&\sigma m\_{x\pi}\\ \lambda m\_{xx}&\lambda\sigma m\_{x\pi}+\beta m\_{\pi\pi}\end{pmatrix},\quad C\_{g}^{\*}=\begin{pmatrix}0\\ \kappa\eta(1-\bar{c})\end{pmatrix},\quad E^{\*}=\begin{pmatrix}\sigma\mu\\ \lambda\sigma\mu\end{pmatrix}. |  |

For a shock of maximum duration ℓ\ell, the on-impact solution for consumption ct​(ℓ)c\_{t}(\ell) can be found by solving the system backward. The impact multiplier on consumption is given by the partial derivative of ct​(ℓ)c\_{t}(\ell) with respect to gtg\_{t}. This derivative isolates the terms related to Cg∗C\_{g}^{\*}:

|  |  |  |
| --- | --- | --- |
|  | mgc,P​L​(ℓ)≡∂ct​(ℓ)∂gt=e1⊤​[∑i=0ℓ−1(p​𝐀∗)i]​Cg∗,where ​e1⊤=[1,0].m^{c,PL}\_{g}(\ell)\equiv\frac{\partial c\_{t}(\ell)}{\partial g\_{t}}=e\_{1}^{\top}\left[\sum\_{i=0}^{\ell-1}(p\mathbf{A}^{\*})^{i}\right]C\_{g}^{\*},\quad\text{where }e\_{1}^{\top}=[1,0]. |  |

Let 𝐇∗​(ℓ−1)=∑i=0ℓ−1(p​𝐀∗)i\mathbf{H}^{\*}(\ell-1)=\sum\_{i=0}^{\ell-1}(p\mathbf{A}^{\*})^{i}. Substituting Cg∗C\_{g}^{\*} gives:

|  |  |  |
| --- | --- | --- |
|  | mgc,P​L​(ℓ)=e1⊤​𝐇∗​(ℓ−1)​(0κ​η​(1−c¯))=κ​η​(1−c¯)⋅𝐇12∗​(ℓ−1),m^{c,PL}\_{g}(\ell)=e\_{1}^{\top}\mathbf{H}^{\*}(\ell-1)\begin{pmatrix}0\\ \kappa\eta(1-\bar{c})\end{pmatrix}=\kappa\eta(1-\bar{c})\cdot\mathbf{H}^{\*}\_{12}(\ell-1), |  |

where 𝐇12∗​(ℓ−1)\mathbf{H}^{\*}\_{12}(\ell-1) is the (1,2) element of the matrix sum 𝐇∗​(ℓ−1)\mathbf{H}^{\*}(\ell-1). Since κ​η​(1−c¯)>0\kappa\eta(1-\bar{c})>0, the properties of the multiplier are determined entirely by the sequence {𝐇12∗​(ℓ−1)}ℓ=1∞\{\mathbf{H}^{\*}\_{12}(\ell-1)\}\_{\ell=1}^{\infty}.

##### Monotonicity and Positivity.

We first prove that the multiplier is positive and strictly increasing in ℓ\ell.

###### Lemma 8 (Monotonicity and Sign of the ELB Multiplier).

The sequence {mgc,P​L​(ℓ)}ℓ=1∞\{m^{c,PL}\_{g}(\ell)\}\_{\ell=1}^{\infty} is strictly increasing in ℓ\ell. Furthermore, mgc,P​L​(1)=0m^{c,PL}\_{g}(1)=0 and mgc,P​L​(ℓ)>0m^{c,PL}\_{g}(\ell)>0 for all ℓ≥2\ell\geq 2.

###### Proof.

The multiplier is given by mgc,P​L​(ℓ)=κ​η​(1−c¯)⋅𝐇12∗​(ℓ−1)m^{c,PL}\_{g}(\ell)=\kappa\eta(1-\bar{c})\cdot\mathbf{H}^{\*}\_{12}(\ell-1), where 𝐇12∗​(ℓ−1)\mathbf{H}^{\*}\_{12}(\ell-1) is the (1,2) element of the matrix sum 𝐇∗​(ℓ−1)=∑i=0ℓ−1(p​𝐀∗)i\mathbf{H}^{\*}(\ell-1)=\sum\_{i=0}^{\ell-1}(p\mathbf{A}^{\*})^{i}. We prove the required properties by analyzing the sequence {𝐇12∗​(ℓ−1)}ℓ=1∞\{\mathbf{H}^{\*}\_{12}(\ell-1)\}\_{\ell=1}^{\infty}.

##### Positivity.

The matrix 𝐀∗\mathbf{A}^{\*} is element-wise strictly positive. Therefore, for any i≥1i\geq 1, the power (p​𝐀∗)i(p\mathbf{A}^{\*})^{i} is also element-wise strictly positive. The sum 𝐇∗​(ℓ−1)=I+p​𝐀∗+⋯+(p​𝐀∗)ℓ−1\mathbf{H}^{\*}(\ell-1)=I+p\mathbf{A}^{\*}+\dots+(p\mathbf{A}^{\*})^{\ell-1} is the sum of the non-negative identity matrix and (for ℓ≥2\ell\geq 2) strictly positive matrices. Thus, 𝐇∗​(ℓ−1)\mathbf{H}^{\*}(\ell-1) is element-wise strictly positive for all ℓ≥2\ell\geq 2. This implies its (1,2) element 𝐇12∗​(ℓ−1)>0\mathbf{H}^{\*}\_{12}(\ell-1)>0 for ℓ≥2\ell\geq 2. Since mgc,P​L​(1)=0m^{c,PL}\_{g}(1)=0, the multiplier is positive for all ℓ≥2\ell\geq 2.

##### Monotonicity.

To show the sequence is strictly increasing, we examine the difference between consecutive terms. As derived from the definition of the multiplier, this difference is given by:

|  |  |  |
| --- | --- | --- |
|  | mgc,P​L​(ℓ+1)−mgc,P​L​(ℓ)=κ​η​(1−c¯)⋅e1⊤​(p​𝐀∗)ℓ​e2.m^{c,PL}\_{g}(\ell+1)-m^{c,PL}\_{g}(\ell)=\kappa\eta(1-\bar{c})\cdot e\_{1}^{\top}(p\mathbf{A}^{\*})^{\ell}e\_{2}. |  |

The term e1⊤​(p​𝐀∗)ℓ​e2e\_{1}^{\top}(p\mathbf{A}^{\*})^{\ell}e\_{2} is the (1,2) element of the matrix power (p​𝐀∗)ℓ(p\mathbf{A}^{\*})^{\ell}. We need to show this element is strictly positive for all ℓ≥1\ell\geq 1.

The matrix 𝐀∗\mathbf{A}^{\*} is element-wise strictly positive. For the base case ℓ=1\ell=1, the (1,2) element of p​𝐀∗p\mathbf{A}^{\*} is p​σ​mx​πp\sigma m\_{x\pi}, which is strictly positive. For any higher power ℓ>1\ell>1, the matrix (p​𝐀∗)ℓ(p\mathbf{A}^{\*})^{\ell} is the product of element-wise positive matrices, which ensures its (1,2) element is also strictly positive.

Since κ​η​(1−c¯)>0\kappa\eta(1-\bar{c})>0 and e1⊤​(p​𝐀∗)ℓ​e2>0e\_{1}^{\top}(p\mathbf{A}^{\*})^{\ell}e\_{2}>0 for all ℓ≥1\ell\geq 1, the difference mgc,P​L​(ℓ+1)−mgc,P​L​(ℓ)m^{c,PL}\_{g}(\ell+1)-m^{c,PL}\_{g}(\ell) is always positive. Therefore, the multiplier sequence is strictly increasing.
∎

##### Asymptotic Behavior.

The long-run limit of the multiplier depends on the convergence of the matrix series 𝐇∗​(ℓ−1)\mathbf{H}^{\*}(\ell-1).

###### Lemma 9 (Asymptotic Behavior of the ELB Multiplier).

The limit of the multiplier sequence depends on the shock persistence pp relative to the threshold p¯\overline{p}:

* •

  If p<p¯p<\overline{p}, limℓ→∞mgc,P​L​(ℓ)=mgc,P​L​(∞)>0\lim\_{\ell\to\infty}m^{c,PL}\_{g}(\ell)=m^{c,PL}\_{g}(\infty)>0.
* •

  If p≥p¯p\geq\overline{p}, limℓ→∞mgc,P​L​(ℓ)=+∞\lim\_{\ell\to\infty}m^{c,PL}\_{g}(\ell)=+\infty.

###### Proof.

The limit of the multiplier is determined by the limit of the matrix sum. As established in the proof of Proposition 4, this sum converges if and only if the spectral radius ρ​(p​𝐀∗)<1\rho(p\mathbf{A}^{\*})<1, which is true if and only if p<p¯p<\overline{p}.

Case 1: p<p¯p<\overline{p} (Convergence). The matrix series converges, limℓ→∞𝐇∗​(ℓ−1)=(I−p​𝐀∗)−1\lim\_{\ell\to\infty}\mathbf{H}^{\*}(\ell-1)=(I-p\mathbf{A}^{\*})^{-1}. The limiting multiplier is:

|  |  |  |
| --- | --- | --- |
|  | mgc,P​L​(∞)=κ​η​(1−c¯)⋅e1⊤​(I−p​𝐀∗)−1​e2=p​σ​mx​π​κ​η​(1−c¯)(1−p​mx​x)​(1−p​β​mπ​π)−p​λ​σ​mx​π.m^{c,PL}\_{g}(\infty)=\kappa\eta(1-\bar{c})\cdot e\_{1}^{\top}(I-p\mathbf{A}^{\*})^{-1}e\_{2}=\frac{p\sigma m\_{x\pi}\kappa\eta(1-\bar{c})}{(1-pm\_{xx})(1-p\beta m\_{\pi\pi})-p\lambda\sigma m\_{x\pi}}. |  |

Since the system is stable for p<p¯p<\overline{p}, the denominator is positive. The numerator is also positive. Thus, the multiplier converges to a finite positive value.

Case 2: p≥p¯p\geq\overline{p} (Divergence). The spectral radius ρ​(p​𝐀∗)≥1\rho(p\mathbf{A}^{\*})\geq 1, and the matrix series diverges. Since all elements of 𝐀∗\mathbf{A}^{\*} are non-negative, the elements of the sum 𝐇∗​(ℓ−1)\mathbf{H}^{\*}(\ell-1) are non-decreasing in ℓ\ell. The divergence implies that the elements grow without bound. In particular, 𝐇12∗​(ℓ−1)→+∞\mathbf{H}^{\*}\_{12}(\ell-1)\to+\infty. Consequently, the multiplier also diverges: mgc,P​L​(ℓ)→+∞m^{c,PL}\_{g}(\ell)\to+\infty.
∎

The two lemmas above collectively prove all statements of the proposition.
∎

### A.6 Proof of Proposition [8](https://arxiv.org/html/2511.04782v1#Thmprop8 "Proposition 8. ‣ 4 Characterizing Fiscal Policy at the ELB ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.")

###### Proof.

This proof characterizes the government spending multiplier on consumption, mgc,M​(ℓ)m^{c,M}\_{g}(\ell), in the mixed-solution regime where d¯​(p)<d<d¯​(0)\overline{d}(p)<d<\overline{d}(0). We prove the proposition’s three statements in order.

##### Proof of Statement (i).

The first statement follows directly from the proof of Proposition 5. There, we established the existence of a unique integer threshold ℓ¯\overline{\ell} for any shock dd in this range.

* •

  If the shock’s maximum duration ℓ<ℓ¯\ell<\overline{\ell}, the equilibrium path is a pure Normal-Time solution. Therefore, the multiplier in this case is identical to the pure Normal-Time multiplier, mgc,M​(ℓ)=mgc,P​N​(ℓ)m^{c,M}\_{g}(\ell)=m^{c,PN}\_{g}(\ell), which we proved in Proposition [6](https://arxiv.org/html/2511.04782v1#Thmprop6 "Proposition 6 (Multiplier in Normal Times). ‣ 4 Characterizing Fiscal Policy at the ELB ‣ Clearing Up the Effective Lower Bound MorassCorresponding author: Jordan Roulleau-Pasdeloup: ecsjr@nus.edu.sg. We thank Jean-Baptiste Michau, Olivier Loisel, Ivan Shchapov as well as seminar participants at École Polytechnique for insightful comments.") is negative.
* •

  If ℓ≥ℓ¯\ell\geq\overline{\ell}, the equilibrium path is a mixed-solution path, beginning with a phase at the ELB.

This establishes the first statement. The remainder of the proof analyzes the multiplier for the case where ℓ≥ℓ¯\ell\geq\overline{\ell}.

##### The Mixed Multiplier Formula.

For any shock with duration ℓ≥ℓ¯\ell\geq\overline{\ell}, the solution path is mixed. The path is constructed by taking the state vector from the longest possible pure-normal-time path, X~i​n​i​t≡X~tP​N​(ℓ¯−1)\tilde{X}\_{init}\equiv\tilde{X}^{PN}\_{t}(\overline{\ell}-1), and evolving it backward for ℓ−(ℓ¯−1)\ell-(\overline{\ell}-1) periods using the ELB dynamics. This gives the on-impact state vector:

|  |  |  |
| --- | --- | --- |
|  | X~tM​(ℓ)=(p​𝐀∗)ℓ−(ℓ¯−1)​X~i​n​i​t+[∑i=0ℓ−ℓ¯(p​𝐀∗)i]​(Cg∗​gt+E∗).\tilde{X}\_{t}^{M}(\ell)=(p\mathbf{A}^{\*})^{\ell-(\overline{\ell}-1)}\tilde{X}\_{init}+\left[\sum\_{i=0}^{\ell-\overline{\ell}}(p\mathbf{A}^{\*})^{i}\right](C\_{g}^{\*}g\_{t}+E^{\*}). |  |

The on-impact consumption multiplier is the derivative of the first component of this vector with respect to gtg\_{t}. Taking the derivative yields the two components of the multiplier:

|  |  |  |
| --- | --- | --- |
|  | mgc,M​(ℓ)=e1⊤​(p​𝐀∗)ℓ−(ℓ¯−1)​∂X~i​n​i​t∂gt⏟Inheritance Component+e1⊤​[∑i=0ℓ−ℓ¯(p​𝐀∗)i]​Cg∗⏟ELB Component.m^{c,M}\_{g}(\ell)=\underbrace{e\_{1}^{\top}(p\mathbf{A}^{\*})^{\ell-(\overline{\ell}-1)}\frac{\partial\tilde{X}\_{init}}{\partial g\_{t}}}\_{\text{Inheritance Component}}+\underbrace{e\_{1}^{\top}\left[\sum\_{i=0}^{\ell-\overline{\ell}}(p\mathbf{A}^{\*})^{i}\right]C\_{g}^{\*}}\_{\text{ELB Component}}. |  |

The “Inheritance Component” is driven by the (negative) PN multiplier vector from the threshold duration ℓ¯−1\overline{\ell}-1. The “ELB Component” captures the accumulating (positive) effects of spending during the ELB phase. It’s crucial to note that for a given set of model parameters and a specific shock (p,d)(p,d), the threshold ℓ¯\overline{\ell} is a fixed integer. Our analysis examines how the multiplier’s characteristics evolve as the maximum duration of the shock, ℓ\ell, increases and moves past this fixed threshold.

##### Proof of Statement (iii) (Asymptotic Behavior).

The long-run behavior of the multiplier as ℓ→∞\ell\to\infty depends critically on the stability of the ELB dynamics, governed by the threshold p¯\overline{p}.

Case 1: The Stable Regime (p<p¯p<\overline{p}). When the ELB dynamics are stable, we can formally prove the limit by analyzing the two components of the mixed multiplier formula as ℓ→∞\ell\to\infty. The analysis hinges on the stability of the ELB transition matrix, p​𝐀∗p\mathbf{A}^{\*}. The condition for this stable case, p<p¯p<\overline{p}, ensures that the spectral radius of the matrix is less than one, ρ​(p​𝐀∗)<1\rho(p\mathbf{A}^{\*})<1.

This stability has two crucial implications. First, for the Inheritance Component, the matrix power (p​𝐀∗)ℓ−(ℓ¯−1)(p\mathbf{A}^{\*})^{\ell-(\overline{\ell}-1)} converges to the zero matrix as ℓ→∞\ell\to\infty. Since this is multiplied by a fixed, finite vector (the PN multiplier vector at duration ℓ¯−1\overline{\ell}-1), the entire inheritance component vanishes in the limit. Second, for the ELB Component, the same stability condition guarantees that the geometric matrix series ∑i=0ℓ−ℓ¯(p​𝐀∗)i\sum\_{i=0}^{\ell-\overline{\ell}}(p\mathbf{A}^{\*})^{i} converges to the matrix inverse (I−p​𝐀∗)−1(I-p\mathbf{A}^{\*})^{-1}. The limit of the ELB component is therefore precisely the pure ELB multiplier for an infinite-horizon shock, mgc,P​L​(∞)m^{c,PL}\_{g}(\infty).

Combining the limits of the two components-zero for the first and mgc,P​L​(∞)m^{c,PL}\_{g}(\infty) for the second we have formally shown that:

|  |  |  |
| --- | --- | --- |
|  | limℓ→∞mgc,M​(ℓ)=mgc,P​L​(∞)>0.\lim\_{\ell\to\infty}m^{c,M}\_{g}(\ell)=m^{c,PL}\_{g}(\infty)>0. |  |

Case 2: The Unstable Regime (p≥p¯p\geq\overline{p}). This is the more complex case. As ℓ→∞\ell\to\infty, both the negative “Inheritance Component” and the positive “ELB Component” of the multiplier diverge in magnitude, leading to an indeterminate form. To resolve this, we must analyze the full AR(2) structure of the multiplier sequence. For ℓ≥ℓ¯\ell\geq\overline{\ell}, the solution to this process can be expressed as:

|  |  |  |
| --- | --- | --- |
|  | mgc,M​(ℓ)=α∗+B1​r1ℓ−ℓ¯+B2​r2ℓ−ℓ¯m^{c,M}\_{g}(\ell)=\alpha^{\*}+B\_{1}r\_{1}^{\ell-\overline{\ell}}+B\_{2}r\_{2}^{\ell-\overline{\ell}} |  |

where α∗\alpha^{\*} is the (unstable) fixed point, and r1r\_{1}, r2r\_{2} are the real roots (eigenvalues) of the system. In the unstable regime (p≥p¯p\geq\overline{p}), the larger root satisfies r1≥1r\_{1}\geq 1. Since r1>r2r\_{1}>r\_{2}, the long-run behavior of the sequence is dominated by the term with the larger root, B1​r1ℓ−ℓ¯B\_{1}r\_{1}^{\ell-\overline{\ell}}. The core of the proof, detailed in the supplementary appendix, is establishing that the coefficient on this explosive root is strictly positive, B1>0B\_{1}>0. A positive coefficient ensures that the positive, explosive dynamic ultimately dominates the negative dynamic inherited from the normal-time phase. As ℓ→∞\ell\to\infty, the term B1​r1ℓ−ℓ¯B\_{1}r\_{1}^{\ell-\overline{\ell}} grows without bound, driving the entire multiplier sequence with it. Therefore, we conclude that the multiplier diverges to positive infinity:

|  |  |  |
| --- | --- | --- |
|  | limℓ→∞mgc,M​(ℓ)=+∞.\lim\_{\ell\to\infty}m^{c,M}\_{g}(\ell)=+\infty. |  |

This case-by-case analysis proves the third statement of the proposition.

##### Proof of Statement (ii) (The Sign Switch).

This statement follows from combining the results already established. From the proof of statement (i), we know the multiplier sequence begins with negative values, as mgc,M​(ℓ)=mgc,P​N​(ℓ)<0m^{c,M}\_{g}(\ell)=m^{c,PN}\_{g}(\ell)<0 for short durations (ℓ<ℓ¯\ell<\overline{\ell}). Conversely, our analysis for statement (iii) shows that the sequence’s long-run limit is either a finite positive number (if p<p¯p<\overline{p}) or diverges to +∞+\infty.

The crucial link between this negative start and positive end is the path’s shape. As established in the supplementary appendix, the multiplier sequence is strictly monotonically increasing once it enters the mixed-regime phase (for ℓ≥ℓ¯\ell\geq\overline{\ell}). A sequence that starts negative and increases monotonically towards a positive or infinite limit must cross zero exactly once. Therefore, there must exist a unique threshold ℓ+≥ℓ¯\ell^{+}\geq\overline{\ell} such that the multiplier becomes positive for all ℓ≥ℓ+\ell\geq\ell^{+}. This proves the second statement of the proposition.

Having proven all three statements, the proof of the proposition is complete.
∎