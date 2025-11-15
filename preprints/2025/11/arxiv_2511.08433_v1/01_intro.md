---
authors:
- Jingyi Cao
- Dongchen Li
- Virginia R. Young
- Bin Zou
doc_id: arxiv:2511.08433v1
family_id: arxiv:2511.08433
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance
  Criterion
url_abs: http://arxiv.org/abs/2511.08433v1
url_html: https://arxiv.org/html/2511.08433v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jingyi Cao
Department of Mathematics and Statistics, York University, Canada. Email: jingyic@yorku.ca
  
Dongchen Li
Department of Mathematics and Statistics, York University, Canada. Email: dcli@yorku.ca
  
Virginia R. Young
Department of Mathematics, University of Michigan, USA. Email: vryoung@umich.edu
  
Bin Zou
Corresponding author. Department of Mathematics, University of Connecticut, USA. Email: bin.zou@uconn.edu

(This version: November 10, 2025
  
Accepted for publication in *SIAM Journal on Control and Optimization*)

###### Abstract

We revisit the optimal dividend problem of de Finetti by adding a variance term to the usual criterion of maximizing the expected discounted dividends paid until ruin,
in a singular control framework. Investors do not like variability in their dividend distribution, and the mean-variance (MV) criterion balances the desire for large expected dividend payments with small variability in those payments.
The resulting MV singular dividend control problem is time-inconsistent, and we follow
a game-theoretic approach to find a time-consistent equilibrium strategy. Our main contribution is a new verification theorem for the novel dividend problem, in which the MV criterion is applied to an integral of the control until ruin, a random time that is endogenous to the problem.
We demonstrate the use of the verification theorem in two cases for which we obtain the equilibrium dividend strategy (semi-)explicitly, and we provide a numerical example to illustrate our results.

MSC2020 codes: 49J40, 49L12, 49N70, 91A23, 91G50

Keywords: Optimal divided problem, mean-variance criterion, singular control, time inconsistency, verification lemma

## 1 Introduction

The optimal dividend problem is a classic topic in actuarial and financial mathematics that aims to find the best strategy for a company to distribute dividends to its shareholders. In a seminal work, de Finetti [[18](https://arxiv.org/html/2511.08433v1#bib.bib18)] proposes to maximize the expected discounted dividend payments up to the company’s ruin time. This objective balances the trade-off between paying out dividends earlier and retaining earnings to ensure future growth and maintain financial stability, and it is arguably the most popular criterion in the study of optimal dividends. However, as argued in Avanzi [[5](https://arxiv.org/html/2511.08433v1#bib.bib5)] (p.239), “variability in dividend payments is not well received in the markets,” and de Finetti’s criterion does *not* penalize variability. This motivates us to incorporate a variance term to penalize dividend variability and consider a mean-variance (MV) criterion for finding the optimal dividend strategy.

We consider a dividend-paying company and model its surplus by a Brownian motion with drift, the so-called diffusion model in risk theory (see Grandell [[22](https://arxiv.org/html/2511.08433v1#bib.bib22)]).111The diffusion model is a popular choice in the optimal dividend problems; see Asmussen and Taksar [[4](https://arxiv.org/html/2511.08433v1#bib.bib4)] and Taksar [[33](https://arxiv.org/html/2511.08433v1#bib.bib33)] for earlier works and Albrecher et al. [[2](https://arxiv.org/html/2511.08433v1#bib.bib2)] and Guan and Xu [[29](https://arxiv.org/html/2511.08433v1#bib.bib29)] for more recent contributions. In particular, Cohen and Young [[16](https://arxiv.org/html/2511.08433v1#bib.bib16)] show that if the company uses the optimal strategy under the diffusion approximation but for the scaled Cramér-Lundberg risk model, then doing so is ε\varepsilon-optimal, and they specify the order of ε\varepsilon relative to the scaling factor. Let D={Dt}t≥0D=\{D\_{t}\}\_{t\geq 0} denote the company’s dividend strategy, in which DtD\_{t} is the cumulative amount of dividends paid up to time tt.
We adopt the singular control framework and do not restrict dividend payments to be absolutely continuous, resulting in a singular control problem. Given a dividend strategy DD, define τ:=τ​(D)\tau:=\tau(D) to be the first time when the company’s surplus XX reaches zero or less, referred to as the *ruin time*; let YtY\_{t} denote the total dividends paid between tt and τ\tau, discounted at a constant rate ρ>0\rho>0, that is, Yt=∫tτe−ρ​(s−t)​dDsY\_{t}=\int\_{t}^{\tau}\,\mathrm{e}^{-\rho(s-t)}\mathrm{d}D\_{s}. In the classical setup of de Finetti, the goal is to find an optimal dividend strategy that maximizes 𝔼x,t​(Yt)\mathbb{E}\_{x,t}(Y\_{t}), the conditional expectation of YtY\_{t} given the initial surplus Xt−=x≥0X\_{t^{-}}=x\geq 0. As motivated above, we propose an MV objective, namely, J​(x,t;D)=𝔼x,t​(Yt)−γ2​𝕍x,t​(Yt)J(x,t;D)=\mathbb{E}\_{x,t}(Y\_{t})-\frac{\gamma}{2}\mathbb{V}\_{x,t}(Y\_{t}),222While MV preferences are among the most popular criteria in decision making, an alternative choice is the mean-standard deviation (MSD) J~​(x,t;D):=𝔼x,t​(Yt)−γ2​𝕍x,t​(Yt)\tilde{J}(x,t;D):=\mathbb{E}\_{x,t}(Y\_{t})-\frac{\gamma}{2}\sqrt{\mathbb{V}\_{x,t}(Y\_{t})}. Note that MSD preferences satisfy the scale-invariance property (that is, J~​(x,t;α​D)=α​J~​(x,t;D)\tilde{J}(x,t;\alpha D)=\alpha\tilde{J}(x,t;D) for all α≥0\alpha\geq 0), which is desirable in some applications (see, for instance, Bayraktar et al. [[6](https://arxiv.org/html/2511.08433v1#bib.bib6)] for an equilibrium stopping problem under MSD).
in which γ>0\gamma>0 regulates the penalty on the variability in dividend payments and can be interpreted as a risk aversion parameter. Note that the limiting case of γ→0+\gamma\to 0^{+} reduces to de Finetti’s model.

It is well known that dynamic MV optimization problems, such as the above MV dividend problem, are time-inconsistent (see, for instance, Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)]).333Let {us∗|{x,t}}s≥t\{u^{\*}\_{s}|\_{\{x,t\}}\}\_{s\geq t} denote the “optimal” strategy of an optimization problem obtained under the initial condition Xt−=x≥0X\_{t^{-}}=x\geq 0 for all feasible (x,t)(x,t). This dynamic problem is called time-inconsistent if us∗|{x1,t1}≠us∗|{x2,t2}u\_{s}^{\*}|\_{\{x\_{1},t\_{1}\}}\neq u\_{s}^{\*}|\_{\{x\_{2},t\_{2}\}} holds for some s>t2>t1s>t\_{2}>t\_{1} and feasible x1x\_{1},
in which x2=Xt2−∗|{x1,t1}x\_{2}=X^{\*}\_{t\_{2}^{-}}|\_{\{x\_{1},t\_{1}\}} is the state process at time t2−t\_{2}^{-} under the strategy {us∗|{x1,t1}}t1≤t<t2\{u^{\*}\_{s}|\_{\{x\_{1},t\_{1}\}}\}\_{t\_{1}\leq t<t\_{2}}.
In this work, we follow the game-theoretic approach to seek an equilibrium dividend strategy (see Definition [2.2](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). To that end, we first develop and prove a verification theorem (Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) that is tailored to our MV dividend problem and differs from those in the literature. Next, we apply this theorem to obtain the equilibrium strategies in two distinctive scenarios, large γ\gamma and small γ\gamma (risk aversion). To be precise, when γ\gamma exceeds a threshold, we show that the equilibrium strategy is to pay out the entire surplus and declare bankruptcy immediately (Theorem [4.1](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). This result is consistent with intuition because a sufficiently large γ\gamma imposes a big penalty on the variance of dividend payments YtY\_{t}, and the strategy of paying out all surplus yields a zero variance. When γ\gamma is sufficiently small, we show that the equilibrium strategy is a time-independent barrier strategy with a strictly positive barrier x~\tilde{x} (Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")); that is, given the initial surplus Xt−=xX\_{t^{-}}=x, the company pays out a lump sum dividend of max⁡{x−x~,0}\max\{x-\tilde{x},0\} at time tt, and thereafter pays dividends so that the resulting surplus is reflected at the barrier x~\tilde{x}.

Finding an equilibrium solution of the time-inconsistent MV dividend singular control problem stated above is new to the time-inconsistent control literature. We are aware of only three papers that study time-inconsistent singular control problems: Liang et al. [[31](https://arxiv.org/html/2511.08433v1#bib.bib31)], Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)], and Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)]. Liang et al. [[31](https://arxiv.org/html/2511.08433v1#bib.bib31)] study an optimal reinsurance problem for an insurer, and the singular control is irreversible reinsurance coverage; in their paper, time inconsistency arises from *non-exponential discounting* in the objective (see, for instance, Section 5 in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)]).
Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)] extend the model in Liang et al. [[31](https://arxiv.org/html/2511.08433v1#bib.bib31)] to a Stackelberg reinsurance game and assume that both the insurer and reinsurer are endowed with MV preferences.
Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] solve an MV portfolio optimization problem with proportional transaction costs in a standard Black-Scholes market. Apart from the obvious difference in the optimization problem itself, our paper also differs from those in defining the admissible strategies and, later, equilibrium strategies. We outline the key points below and refer the reader to Remark [2.1](https://arxiv.org/html/2511.08433v1#S2.Thmremark1 "Remark 2.1. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") for a detailed discussion.
Liang et al. [[31](https://arxiv.org/html/2511.08433v1#bib.bib31)] and Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)] define admissible strategies by partitioning the feasible region into the continuation and intervention regions; but, both Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] and this paper define admissible strategies in a more standard way (see Definition [2.1](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). On the other hand, Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] impose additional α\alpha-Hölder continuity assumptions (with α∈(0,1]\alpha\in(0,1]) on the spike perturbations and define equilibrium in the order of εα\varepsilon^{\alpha}; by comparison, we follow the standard first-order (ε\varepsilon) condition as in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)]. The key to achieving the standard weak equilibrium is the estimate in ([3](https://arxiv.org/html/2511.08433v1#S3.Ex53 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), which allows us to bound the error term by o​(ε)o(\varepsilon).

In the standard MV literature, the objective is in the form of 𝔼x,t​(XT)−γ2​𝕍x,t​(XT)\mathbb{E}\_{x,t}(X\_{T})-\frac{\gamma}{2}\mathbb{V}\_{x,t}(X\_{T}), in which XTX\_{T} is the controlled state process at the terminal time TT. For instance, both Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)] and Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] follow this standard setup and assume TT is a fixed constant horizon (XTX\_{T} is replaced by ln⁡XT\ln X\_{T} in Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)]);
the majority of the research on time-inconsistent MV classical control problems also adopts this setup (see, for instance, Björk et al. [[11](https://arxiv.org/html/2511.08433v1#bib.bib11)]).444For such a setup, because the MV objective only depends on the terminal state XTX\_{T} through its distribution μ​(⋅)\mu(\cdot),
the original MV problem can be reformulated as a control problem of McKean-Vlasov type (MKV problem) over the (infinite-dimensional) *distribution space*. The new MKV problem is time-consistent in the time-distribution space (t,μ)(t,\mu), and one may apply a McKean–Vlasov version of the dynamic programming approach to characterize the optimal value function v​(t,μ)v(t,\mu); see Ismail and Pham [[26](https://arxiv.org/html/2511.08433v1#bib.bib26)] for a nice implementation of this method to MV portfolio optimization problems. However, it is not straightforward to apply this approach to our MV dividend problem, because the MV criterion is applied to YtY\_{t}, an integral of controls over an endogenously determined, random time τ\tau.
Landriault et al. [[30](https://arxiv.org/html/2511.08433v1#bib.bib30)] study MV investment problems over a random horizon TT, but they assume that this random TT is *independent* of the state process XX and control.
However, the MV objective in this paper involves Yt=∫tτe−ρ​(s−t)​dDsY\_{t}=\int\_{t}^{\tau}\,\mathrm{e}^{-\rho(s-t)}\mathrm{d}D\_{s}, which is an *integral* of the dividend payments from the current time to the ruin time τ\tau; note that τ\tau is *endogenously* dependent on the company’s dividend strategy and surplus process, a striking difference from the exogenous random horizon in Landriault et al. [[30](https://arxiv.org/html/2511.08433v1#bib.bib30)].
Kronborg and Steffensen [[28](https://arxiv.org/html/2511.08433v1#bib.bib28)] apply the MV objective to the terminal wealth XTX\_{T} and an integral of intertemporal consumption (a classical control) over a finite horizon [t,T][t,T]; by comparison, YtY\_{t} is an integral of dividends (a singular control) over a random horizon [t,τ][t,\tau]. Because of the “natural” boundary at TT, the equilibrium value function in Kronborg and Steffensen [[28](https://arxiv.org/html/2511.08433v1#bib.bib28)] takes the linear-quadratic form (see Proposition 3.1 therein); this ansatz plays an important role in finding (explicit) solutions. Note that this form of solution is similar to that of standard MV problems involving *only* the terminal wealth (see Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)] and Björk et al. [[11](https://arxiv.org/html/2511.08433v1#bib.bib11)]). However, we do not have an *a priori* guess for the form of the value function VV in this paper; in fact, VV will not be of linear-quadratic form globally (see V​(x)V(x) over x<x~x<\tilde{x} in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). Regarding the equilibrium consumption c∗c^{\*} (under constant risk aversion), Kronborg and Steffensen [[28](https://arxiv.org/html/2511.08433v1#bib.bib28)] show that it is a bang-bang control and only depends on whether the risk-free rate is greater than the discount rate, but is *independent* of the state process XX. By comparison, the equilibrium dividend strategy D∗D^{\*} in this paper is of barrier type and explicitly depends on the surplus XX; note that the same conclusion holds under the classical control framework in Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)].
The integral form of YtY\_{t} in our MV objective significantly complicates the study and leads to an extended system of Hamilton-Jacobi-Bellman (HJB) equations that is different from the systems in related works (see Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)] and Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] for singular control and Björk et al. [[11](https://arxiv.org/html/2511.08433v1#bib.bib11)] and Landriault et al. [[30](https://arxiv.org/html/2511.08433v1#bib.bib30)] for classical control). In particular, we remark that our MV objective is *not* a special case of the general MV framework proposed in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)] (see their objective in equation (39)). Because of this integral form over an endogenously determined random horizon, the HJB system in this work involves three functions: the (equilibrium) value function VV, the first moment function G​(x,t)=𝔼x,t​(Yt∗)G(x,t)=\mathbb{E}\_{x,t}(Y\_{t}^{\*}), and the second moment function H​(x,t)=𝔼x,t​((Yt∗)2)H(x,t)=\mathbb{E}\_{x,t}\big((Y\_{t}^{\*})^{2}\big); see equations ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"))-([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) in Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"). But for the standard MV setup of terminal XTX\_{T}, the extend HJB system only involves VV and GG, but not HH (see, for instance, Theorem 3.1 in Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)]).

This paper also contributes to the literature on optimal dividends.
Although MV preferences are well adopted in portfolio selection problems (see Björk et al. [[11](https://arxiv.org/html/2511.08433v1#bib.bib11)], Landriault et al. [[30](https://arxiv.org/html/2511.08433v1#bib.bib30)], and Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)]), they are rarely used in the study of optimal dividend problems. To the best of our knowledge, this is the first paper that solves a singular dividend control problem under MV preferences. By comparison, Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] study an MV dividend problem under the classical control framework,555The dividend strategy in Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] is Dt=θt​d​tD\_{t}=\theta\_{t}\,\mathrm{d}t for some bounded dividend rate 0≤θt≤m0\leq\theta\_{t}\leq m for all t≥0t\geq 0, as in Section 2 of Asmussen and Taksar [[4](https://arxiv.org/html/2511.08433v1#bib.bib4)]. If the dividend rate process is further required to be non-decreasing, this is referred to as a ratcheting constraint; see Angoshtari et al. [[3](https://arxiv.org/html/2511.08433v1#bib.bib3)], Albrecher et al. [[2](https://arxiv.org/html/2511.08433v1#bib.bib2)], and Guan and Xu [[29](https://arxiv.org/html/2511.08433v1#bib.bib29)].
and this paper differs from that one in at least three aspects: (1) the definition of equilibrium strategies (see the last point in Remark [2.1](https://arxiv.org/html/2511.08433v1#S2.Thmremark1 "Remark 2.1. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), (2) the verification lemma (see Remark [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmremark1 "Remark 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), and (3) the main results (see Remark [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmremark2 "Remark 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). Interestingly, a numerical example in Section [5](https://arxiv.org/html/2511.08433v1#S5 "5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") suggests that the barrier equilibrium strategy of the classical control problem in Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] converges to its counterpart of the singular control problem in this paper, as the maximum dividend rate goes to infinity (see Figure [7](https://arxiv.org/html/2511.08433v1#S5.F7 "Figure 7 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).
As mentioned earlier, time inconsistency might also arise from non-exponential discounting, and related studies on optimal dividend include Chen et al. [[13](https://arxiv.org/html/2511.08433v1#bib.bib13), [14](https://arxiv.org/html/2511.08433v1#bib.bib14)], Zhu et al. [[35](https://arxiv.org/html/2511.08433v1#bib.bib35)], Zhou and Jin [[36](https://arxiv.org/html/2511.08433v1#bib.bib36)], and Christensen and Lindensjö [[15](https://arxiv.org/html/2511.08433v1#bib.bib15)], among many others. Please see Albrecher and Thonhauser [[1](https://arxiv.org/html/2511.08433v1#bib.bib1)] and Avanzi [[5](https://arxiv.org/html/2511.08433v1#bib.bib5)] for an overview of the research questions on optimal dividend problems.

The rest of this paper is organized as follows. Section [2](https://arxiv.org/html/2511.08433v1#S2 "2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") presents the model and main problem. We develop and prove the verification theorem in Section [3](https://arxiv.org/html/2511.08433v1#S3 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") and apply it to obtain equilibrium dividend strategies in Section [4](https://arxiv.org/html/2511.08433v1#S4 "4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"). We conduct a numerical analysis in Section [5](https://arxiv.org/html/2511.08433v1#S5 "5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion").
Finally, Section [6](https://arxiv.org/html/2511.08433v1#S6 "6 Conclusions ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") concludes the study.

## 2 Model

We fix a filtered probability space (Ω,ℱ,𝔽=(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},\mathbb{F}=(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}), in which the filtration 𝔽\mathbb{F} is generated by a standard one-dimensional Brownian motion B=(Bt)t≥0B=(B\_{t})\_{t\geq 0}. We consider a company that pays dividends to its shareholders and let DtD\_{t} denote the *cumulative* amount of dividends paid up to time tt; we call D={Dt}t≥0D=\{D\_{t}\}\_{t\geq 0} a dividend strategy. We model the company’s uncontrolled surplus by a drifted Brownian motion (see, for instance, Asmussen and Taksar [[4](https://arxiv.org/html/2511.08433v1#bib.bib4)]). As such, given a dividend strategy DD, the company’s controlled surplus X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} follows the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=a​d​t+b​d​Bt−d​Dt,\displaystyle\mathrm{d}X\_{t}=a\,\mathrm{d}t+b\,\mathrm{d}B\_{t}-\mathrm{d}D\_{t}, |  | (2.1) |

in which aa and bb are positive constants, with X0>0X\_{0}>0. Define the company’s ruin time by τ:=inf{t≥0:Xt≤0}\tau:=\inf\{t\geq 0:X\_{t}\leq 0\}. Let YtY\_{t} denote the total dividends paid between time tt and ruin time τ\tau under strategy DD, discounted at a constant rate ρ>0\rho>0, that is,666Throughout this paper, all integrals include the possible jumps at the left end point; for example, YtY\_{t} in ([2.2](https://arxiv.org/html/2511.08433v1#S2.E2 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) equals Δ​Dt+∫t+τe−ρ​(s−t)​dDs\Delta D\_{t}+\int\_{t^{+}}^{\tau}\,\mathrm{e}^{-\rho(s-t)}\,\mathrm{d}D\_{s}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=∫tτe−ρ​(s−t)​dDs,0≤t<τ.Y\_{t}=\int\_{t}^{\tau}\mathrm{e}^{-\rho(s-t)}\,\mathrm{d}D\_{s},\qquad 0\leq t<\tau. |  | (2.2) |

We set Yt=0Y\_{t}=0 for all t≥τt\geq\tau.
It is obvious that XX, τ\tau, and YtY\_{t} all depend on the company’s dividend strategy DD, and a more precision notation is to write XDX^{D}, τD\tau^{D}, and YtDY\_{t}^{D}, but we often suppress this dependence for notational simplicity.

Following the literature on time-inconsistent control problems (see, for instance, Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)] and Björk et al. [[11](https://arxiv.org/html/2511.08433v1#bib.bib11)] on regular controls and Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] on singular controls), we focus on (Markov) feedback controls in the form of Dt=𝒟​(𝒳𝓉−,𝓉)D\_{t}=\mathpzc{D}(X\_{t^{-}},t) for some deterministic function 𝒟\mathpzc{D}. We define admissible dividend strategies below.

###### Definition 2.1.

A dividend strategy D=(Dt)t≥0D=(D\_{t})\_{t\geq 0} is called admissible if (1)(1) there exists a Borel-measurable, deterministic function 𝒟:ℝ+2→ℝ+\mathpzc{D}:\mathbb{R}\_{+}^{2}\to\mathbb{R}\_{+} such that Dt=𝒟​(𝒳𝓉−,𝓉)D\_{t}=\mathpzc{D}(X\_{t^{-}},t), in which XX satisfies ([2.1](https://arxiv.org/html/2511.08433v1#S2.E1 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) under the strategy DD; (2)(2) DD is non-decreasing over time; (3)(3) Δ​Dt:=Dt−Dt−≤Xt−\Delta D\_{t}:=D\_{t}-D\_{t^{-}}\leq X\_{t^{-}} ((that is, the company cannot pay more in dividends that it owns)); (4)(4) Dt=DτD\_{t}=D\_{\tau} for all t≥τt\geq\tau ((that is, there are no dividend payments after ruin)); and (5)(5) YtY\_{t} in ([2.2](https://arxiv.org/html/2511.08433v1#S2.E2 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is square integrable for all t≥0t\geq 0.

Note that the above definition trivially generalizes from a starting time of 0 to an arbitrary starting time t≥0t\geq 0 (assuming t<τt<\tau); let 𝒜t\mathcal{A}\_{t} denote the set of all admissible strategies D=(Ds)s≥tD=(D\_{s})\_{s\geq t} for every t≥0t\geq 0.
With a slight abuse of notation, we use DD to denote both the deterministic function 𝒟\mathpzc{D} and the dividend strategy induced by it via Dt=𝒟​(𝒳𝓉−,𝓉)D\_{t}=\mathpzc{D}(X\_{t^{-}},t).

As argued in Section [1](https://arxiv.org/html/2511.08433v1#S1 "1 Introduction ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), we assume that the manager of the company penalizes variability in dividend payments by their variance and applies the MV criterion when choosing the company’s dividend strategy. In particular, the manager’s (dynamic) objective function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(x,t;D)=𝔼x,t​(Yt)−γ2​𝕍x,t​(Yt),D∈𝒜t,\displaystyle J(x,t;D)=\mathbb{E}\_{x,t}(Y\_{t})-\dfrac{\gamma}{2}\,\mathbb{V}\_{x,t}(Y\_{t}),\quad D\in\mathcal{A}\_{t}, |  | (2.3) |

in which γ>0\gamma>0 is the risk aversion parameter. In ([2.3](https://arxiv.org/html/2511.08433v1#S2.E3 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), 𝔼x,t\mathbb{E}\_{x,t} and 𝕍x,t\mathbb{V}\_{x,t} denote expectation and variance, respectively, conditional on Xt−=x≥0X\_{t^{-}}=x\geq 0, that is, before any possible lump-sum dividend payments at time tt. If we set γ=0\gamma=0, then the objective JJ in ([2.3](https://arxiv.org/html/2511.08433v1#S2.E3 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) reduces to the one proposed by de Finetti [[18](https://arxiv.org/html/2511.08433v1#bib.bib18)] and used in many follow-up works (see Albrecher and Thonhauser [[1](https://arxiv.org/html/2511.08433v1#bib.bib1)]).

Because of the variance term in ([2.3](https://arxiv.org/html/2511.08433v1#S2.E3 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), maximizing J​(x,t;D)J(x,t;D) for all (x,t)∈ℝ+(x,t)\in\mathbb{R}\_{+} leads to a time-inconsistent control problem. We follow an intrapersonal game approach, as in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)], and seek a time-consistent equilibrium dividend strategy D∗D^{\*}.
The definition of an equilibrium strategy under a singular control framework is different from its counterpart under a classical (or regular) control framework in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)]. Below, we formally define D∗D^{\*}, and it is similar to the definition of equilibrium in Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)]; for a different definition, see Liang et al. [[31](https://arxiv.org/html/2511.08433v1#bib.bib31)] and Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)].

###### Definition 2.2.

Fix an arbitrary initial time t≥0t\geq 0 and an initial surplus Xt−=x>0X\_{t-}=x>0 and assume that ruin has not occurred by time tt. Let D∗=(Ds∗)s≥t∈𝒜tD^{\*}=(D^{\*}\_{s})\_{s\geq t}\in\mathcal{A}\_{t} be an admissible dividend strategy and denote its associated surplus, ruin time, and discounted dividend payments by X∗:=XD∗X^{\*}:=X^{D^{\*}}, τ∗:=τD∗\tau^{\*}:=\tau^{D^{\*}}, and Yt∗:=YtD∗Y\_{t}^{\*}:=Y\_{t}^{D^{\*}}, respectively.
For a positive number ε\varepsilon, a non-negative number d∈[0,x]d\in[0,x], and a non-decreasing, continuous function δ\delta ((of time only)) satisfying δ​(t+ε)−δ​(t)=O​(ε)\delta(t+\varepsilon)-\delta(t)=O(\varepsilon) as ε→0\varepsilon\to 0, define a perturbed strategy Dε=(Dsε)s≥tD^{\varepsilon}=(D^{\varepsilon}\_{s})\_{s\geq t} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dsε={Dt−∗+d+∫t+s∧τdδ​(u),t≤s<(t+ε)∧τ,D(t+ε)−ε+∫t+εsdDu∗,s≥(t+ε)∧τ.D^{\varepsilon}\_{s}=\begin{cases}D^{\*}\_{t^{-}}+d+\int\_{t^{+}}^{s\wedge\tau}\,\mathrm{d}\delta(u),&\quad t\leq s<(t+\varepsilon)\wedge\tau,\vskip 5.0pt\\ D^{\varepsilon}\_{(t+\varepsilon)^{-}}+\int\_{t+\varepsilon}^{s}\mathrm{d}D^{\*}\_{u},&\quad s\geq(t+\varepsilon)\wedge\tau.\end{cases} |  | (2.4) |

in which τ:=τDε\tau:=\tau^{D^{\varepsilon}} is the ruin time under the perturbed strategy DεD^{\varepsilon}, and ∫t+εsdDu∗=Δ​Dt+ε∗+∫(t+ε)+sdDu∗\int\_{t+\varepsilon}^{s}\mathrm{d}D^{\*}\_{u}=\Delta D^{\*}\_{t+\varepsilon}+\int\_{(t+\varepsilon)^{+}}^{s}\mathrm{d}D^{\*}\_{u}.
The strategy D∗D^{\*} is said to be a time-consistent equilibrium dividend strategy if, for all (x,t)∈ℝ+2(x,t)\in\mathbb{R}\_{+}^{2}, d∈[0,x]d\in[0,x], and δ\delta functions that satisfy the above conditions,

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infε→0+J​(x,t;D∗)−J​(x,t;Dε)ε≥0,\liminf\_{\varepsilon\to 0^{+}}\,\dfrac{J(x,t;D^{\*})-J(x,t;D^{\varepsilon})}{\varepsilon}\geq 0, |  | (2.5) |

and the equilibrium value function VV equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x,t)=J​(x,t;D∗).V(x,t)=J(x,t;D^{\*}). |  | (2.6) |

We end this section with a technical remark on the definition of the equilibrium strategies D∗D^{\*} above and a discussion on the existence, (non)uniqueness, and “optimality” of equilibria.

###### Remark 2.1.

The definition of DεD^{\varepsilon} in ([2.4](https://arxiv.org/html/2511.08433v1#S2.E4 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is largely inspired by Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] who also study a time-inconsistent singular control problem, and it shares the same idea as in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)] under the regular control framework.
In Definition [2.2](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), we only require δ​(t+ε)−δ​(t)=O​(ε)\delta(t+\varepsilon)-\delta(t)=O(\varepsilon), and the denominator in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is ε\varepsilon, the first order of the error ε\varepsilon. However, Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] assume that δ\delta is α\alpha-Hölder continuous for some α∈(0,1]\alpha\in(0,1], and the corresponding denominator is εα\varepsilon^{\alpha}. To our understanding, the “small” terms in Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] are *not* of order o​(ε)o(\varepsilon), and that is why they impose the additional assumption of α\alpha-Hölder continuity and change the denominator from ε\varepsilon to εα\varepsilon^{\alpha} ((see Definition 2 therein)). We can relax their assumption because after carefully collecting all the integral terms of δ\delta with order O​(ε)O(\varepsilon), the summation is of a definite sign ((“negative” in ([3](https://arxiv.org/html/2511.08433v1#S3.Ex53 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")))), which allows us to prove the inequality in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).
Although we assume that δ\delta is a deterministic, univariate function of time only, we can easily generalize to allowing perturbations in the form of δs:=δ​(Xs,s)\delta\_{s}:=\delta(X\_{s},s) for some bivariate function δ\delta, as long as δ​(Xt+ε,t+ε)−δ​(x−d,t)=O​(ε)\delta(X\_{t+\varepsilon},t+\varepsilon)-\delta(x-d,t)=O(\varepsilon) holds uniformly. Under that extension, the class of δ\delta would be large enough to incorporate the ((bounded)) *dividend-rate* case. Indeed, let θ​(Xs,s)∈[0,m]\theta(X\_{s},s)\in[0,m] be the dividend rate paid at time s∈(t,t+ε)s\in(t,t+\varepsilon); then, ∫t+t+εdδ​(Xu,u)=∫t+t+εe−ρ​(s−t)​θ​(Xs,s)​ds=O​(ε)\int\_{t^{+}}^{t+\varepsilon}\mathrm{d}\delta(X\_{u},u)=\int\_{t^{+}}^{t+\varepsilon}\mathrm{e}^{-\rho(s-t)}\theta(X\_{s},s)\,\mathrm{d}s=O(\varepsilon), and we can easily choose θs\theta\_{s} so that δ\delta is *not* α\alpha-Hölder continuous, versus the requirement in Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)].

Careful readers will notice that the only singular perturbation over [t,t+ε)[t,t+\varepsilon) occurs at time tt in the definition of DεD^{\varepsilon} in ([2.4](https://arxiv.org/html/2511.08433v1#S2.E4 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). It is straightforward to extend from one jump at time tt to a countable number of jumps over [t,t+ε)[t,t+\varepsilon), but this requires the additional assumption of ∑s∈(t,t+ε)Δ​Dsε=o​(ε)\sum\_{s\in(t,t+\varepsilon)}\,\Delta D\_{s}^{\varepsilon}=o(\varepsilon). Note that Liang et al. [[31](https://arxiv.org/html/2511.08433v1#bib.bib31)] impose exactly the same assumption in their definition ((see Definition 2.2​(c)2.2(c), p. 3217)3217).777The assumption of ∑s∈(t,t+ε)Δ​Dsε=o​(ε)\sum\_{s\in(t,t+\varepsilon)}\,\Delta D\_{s}^{\varepsilon}=o(\varepsilon) seems to be required in Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)] as well, even though they write O​(ε)O(\varepsilon) instead of o​(ε)o(\varepsilon) (see Definition 2.5(c), p.172).

By Definition [2.1](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), if ruin has occurred before time tt or Xt−≤0X\_{t-}\leq 0, we have J​(x,t;D)=0J(x,t;D)=0 for all D∈𝒜tD\in\mathcal{A}\_{t}. Therefore, to avoid such trivial scenarios, we assume, without loss of generality, that x>0x>0 and ruin has not occurred by time tt in Definition [2.2](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion").

Recall that Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] adopt the classical control framework and require admissible dividend strategies to be absolutely continuous. As such, the perturbed strategy DεD^{\varepsilon} therein does *not* allow singular jumps, which is equivalent to setting d≡0d\equiv 0 in ([2.4](https://arxiv.org/html/2511.08433v1#S2.E4 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). In addition, they assume a *linear* form for δ\delta functions to define perturbed strategies DsεD\_{s}^{\varepsilon}, which, under our notation, yields Dsε=Dt∗+∫tεc​duD\_{s}^{\varepsilon}=D\_{t}^{\*}+\int\_{t}^{\varepsilon}\,c\,\mathrm{d}u for an arbitrary positive constant cc ((less than the maximum dividend rate)). Apparently, the perturbed strategies considered in Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] are special cases of ([2.4](https://arxiv.org/html/2511.08433v1#S2.E4 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), which allows not only singular jumps d>0d>0 but also general forms for δ\delta functions.

Our definition of the equilibrium strategy in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is the so-called *weak equilibrium*, and it is inspired by the popular approach introduced in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)]. However, one potential drawback of such an approach is that the first-order condition ((FOC)) in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is only a necessary condition to characterize equilibrium, and if the FOC holds with equality, there might exist counterexamples in which J​(x,t;Dε)−J​(x,t;D∗)>0J(x,t;D^{\varepsilon})-J(x,t;D^{\*})>0 for some small ε\varepsilon, contracting the concept of equilibrium. To address this issue, different notions of equilibrium have been proposed in the literature; see Huang and Zhou [[25](https://arxiv.org/html/2511.08433v1#bib.bib25)] and He and Jiang [[24](https://arxiv.org/html/2511.08433v1#bib.bib24)] for time-inconsistent control problems, and Bayraktar et al. [[7](https://arxiv.org/html/2511.08433v1#bib.bib7)] and Bayraktar et al. [[8](https://arxiv.org/html/2511.08433v1#bib.bib8)] for time-inconsistent stopping problems. In this paper, we choose the notion of weak equilibrium because it requires minimal assumptions on the model, and for MV problems, weak equilibria can be characterized by the extended HJB equations ((see Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") below)). By comparison, stronger notions of equilibria require more restrictive assumptions on the model, and they may fail to exist ((see, for instance, Section 4.4 in He and Jiang [[25](https://arxiv.org/html/2511.08433v1#bib.bib25)])). Thus, a weak equilibrium is often the first choice when studying a time-inconsistent control or stopping problem, and one proceeds to stronger notions only when there is a good understanding of weak equilibria. As mentioned in the Introduction, the research on time-inconsistent singular control problems is in its early stage, and it is, thus, not surprising that several recent papers ((see Liang et al. [[31](https://arxiv.org/html/2511.08433v1#bib.bib31)], Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)], Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)], and Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)])) all choose the notion of weak equilibrium.
∎

###### Remark 2.2.

As nicely noted in Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)], for all time-inconsistent control problems over a finite, discrete-time horizon, equilibrium strategies, defined similar to the one in Definition [2.1](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), always exist and can be obtained by backward recursion, which in turn implies the uniqueness of the equilibrium value function VV ((although there may exist multiple equilibrium strategies achieving the same V)V). However, the existence result is highly nontrivial for the infinite horizon case, due to the lack of natural boundaries, which is shared by our random horizon setup. In addition, uniqueness on VV may fail on infinite horizon time-inconsistent problems, and there are concrete examples in the literature that admit multiple equilibria. For instance, Example 3.13.1 in Landriault et al. [[30](https://arxiv.org/html/2511.08433v1#bib.bib30)] shows that there exist multiple linear equilibrium strategies, each yielding a different VV, for their MV investment problems over an exponentially distributed random horizon. For the same reason, there is no guarantee on the uniqueness of the equilibrium value function VV defined by ([2.6](https://arxiv.org/html/2511.08433v1#S2.E6 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). ∎

## 3 Verification theorem

In this section, we prove a verification theorem for the equilibrium value function VV in ([2.6](https://arxiv.org/html/2511.08433v1#S2.E6 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and the corresponding equilibrium strategy D∗D^{\*}. We define a differential operator ℳ\mathcal{M} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​ϕ​(x,t)=∂tϕ​(x,t)+a​∂xϕ​(x,t)+12​b2​∂x​xϕ​(x,t),\displaystyle\mathcal{M}\phi(x,t)=\partial\_{t}\phi(x,t)+a\,\partial\_{x}\phi(x,t)+\dfrac{1}{2}\,b^{2}\partial\_{xx}\phi(x,t), |  | (3.1) |

in which ϕ∈𝒞2,1​(ℝ+2)\phi\in\mathcal{C}^{2,1}(\mathbb{R}\_{+}^{2}) and ∂⋅ϕ\partial\_{\cdot}\phi denotes the corresponding partial derivative of ϕ\phi. Because the following verification theorem is relatively new in the literature, we provide its proof in full detail.

###### Theorem 3.1.

Let V~\widetilde{V}, GG, and HH be three functions, all mapping from (x,t)∈ℝ+2(x,t)\in\mathbb{R}\_{+}^{2} to ℝ\mathbb{R}. Define the pay region P\mathrm{P} and no-transaction region NT\mathrm{NT}, respectively, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P={(x,t)∈ℝ+2:∂xV~​(x,t)=1} and NT=ℝ+2\P.\mathrm{P}=\big\{(x,t)\in\mathbb{R}\_{+}^{2}:\partial\_{x}\widetilde{V}(x,t)=1\big\}\quad\text{ and }\quad\mathrm{NT}=\mathbb{R}\_{+}^{2}\backslash\mathrm{P}. |  | (3.2) |

Suppose that V~\widetilde{V}, GG, and HH satisfy the following conditions:

* 1.1.

  V~\widetilde{V}, GG, and H∈𝒞2,1​(ℝ+2)H\in\mathcal{C}^{2,1}(\mathbb{R}\_{+}^{2}), except that G​(⋅,t)G(\cdot,t) and H​(⋅,t)H(\cdot,t) might only be 𝒞1\mathcal{C}^{1} along a specific path x=x~​(t)x=\tilde{x}(t) for all t≥0t\geq 0, with both left and right second derivatives.
* 2.2.

  GG and HH satisfy regularity conditions such that the stochastic integrals in ([3](https://arxiv.org/html/2511.08433v1#S3.Ex1 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3](https://arxiv.org/html/2511.08433v1#S3.Ex7 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) have zero ((conditional)) expectation and lims→∞𝔼x,t​(e−ρ​(s−t)​ϕ​(Xs,s))=0\lim\_{s\to\infty}\,\mathbb{E}\_{x,t}\big(\mathrm{e}^{-\rho(s-t)}\,\phi(X\_{s},s)\big)=0 for ϕ=G,H\phi=G,H.
* 3.3.

  For all (x,t)∈ℝ+2(x,t)\in\mathbb{R}\_{+}^{2}, V~\widetilde{V}, GG, and HH jointly solve the extended HJB system:

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | max⁡{ℳ​V~−γ2​ℳ​G2+γ​G⋅ℳ​G−ρ​G+γ​ρ​(H−G2), 1−∂xV~}\displaystyle\max\left\{\mathcal{M}\widetilde{V}-\dfrac{\gamma}{2}\,\mathcal{M}G^{2}+\gamma G\cdot\mathcal{M}G-\rho G+\gamma\rho\big(H-G^{2}\big),\;1-\partial\_{x}\widetilde{V}\right\} | =0,\displaystyle=0, |  | (3.3) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | (ℳ​G​(x,t)−ρ​G​(x,t))​𝟙{(x,t)∈NT}+(1−∂xG​(x,t))​𝟙{(x,t)∈P}\displaystyle\big(\mathcal{M}G(x,t)-\rho G(x,t)\big)\mathds{1}\_{\{(x,t)\in\mathrm{NT}\}}+\big(1-\partial\_{x}G(x,t)\big)\mathds{1}\_{\{(x,t)\in\mathrm{P}\}} | =0,\displaystyle=0, |  | (3.4) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | (ℳ​H​(x,t)−2​ρ​H​(x,t))​𝟙{(x,t)∈NT}+(2​G​(x,t)−∂xH​(x,t))​𝟙{(x,t)∈P}\displaystyle\big(\mathcal{M}H(x,t)-2\rho H(x,t)\big)\mathds{1}\_{\{(x,t)\in\mathrm{NT}\}}+\big(2G(x,t)-\partial\_{x}H(x,t)\big)\mathds{1}\_{\{(x,t)\in\mathrm{P}\}} | =0,\displaystyle=0, |  | (3.5) |

  in which the argument (x,t)(x,t) is suppressed in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), with the boundary conditions

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | V~​(0,t)=G​(0,t)=H​(0,t)=0,for all ​t≥0.\displaystyle\widetilde{V}(0,t)=G(0,t)=H(0,t)=0,\quad\text{for all }t\geq 0. |  | (3.6) |

  In addition, there exists an admissible dividend strategy D∗=(Ds∗)s≥tD^{\*}=(D\_{s}^{\*})\_{s\geq t} that solves the Skorokhod reflection problem

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | {d​Xs∗=a​d​s+b​d​Bs−d​Ds∗,with ​Xt−∗=x,(Xs∗,s)∈NT¯,Ds∗=Dt−∗+∫ts 1{(x,t)∈P}​dDu∗,\displaystyle\begin{cases}\mathrm{d}X\_{s}^{\*}=a\,\mathrm{d}s+b\,\mathrm{d}B\_{s}-\mathrm{d}D\_{s}^{\*},&\text{with }X\_{t^{-}}^{\*}=x,\\ (X\_{s}^{\*},s)\in\overline{\mathrm{NT}},&\\ D\_{s}^{\*}=D\_{t^{-}}^{\*}+\int\_{t}^{s}\,\mathds{1}\_{\{(x,t)\in\mathrm{P}\}}\,\mathrm{d}D\_{u}^{\*},&\end{cases} |  | (3.7) |

  for all s≥ts\geq t, in which NT¯\overline{\mathrm{NT}} denotes the closure of NT\mathrm{NT} in ([3.2](https://arxiv.org/html/2511.08433v1#S3.E2 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

Then, V~\widetilde{V} is an equilibrium value function defined in ([2.6](https://arxiv.org/html/2511.08433v1#S2.E6 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), and D∗D^{\*} is a time-consistent equilibrium dividend strategy. Moreover, GG and HH have the representations

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(x,t)=𝔼x,t​(Yt∗)andH​(x,t)=𝔼x,t​((Yt∗)2),\displaystyle G(x,t)=\mathbb{E}\_{x,t}\left(Y\_{t}^{\*}\right)\quad\text{and}\quad H(x,t)=\mathbb{E}\_{x,t}\big(\left(Y\_{t}^{\*}\right)^{2}\big), |  | (3.8) |

in which Y∗Y^{\*} is the discounted dividends under D∗D^{\*}; thus, V​(x,t)=G​(x,t)−γ2​(H​(x,t)−G2​(x,t))V(x,t)=G(x,t)-\frac{\gamma}{2}\left(H(x,t)-G^{2}(x,t)\right).

Before we prove Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), we provide some intuition for the results. Assume that a lump-sum dividend payment is optimal at (x,t)(x,t); then, the amount to be paid equals arg​supd≥0⁡V​(x−d,t)+d\operatorname\*{arg\,sup}\_{d\geq 0}\,V(x-d,t)+d, which motivates the definition of the “pay region” P\mathrm{P} in ([3.2](https://arxiv.org/html/2511.08433v1#S3.E2 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). For the “no-transaction region” NT\mathrm{NT}, the value function satisfies a standard differential equation, namely, ℳ​V−γ2​ℳ​G2+γ​G⋅ℳ​G−ρ​G+γ​ρ​(H−G2)=0\mathcal{M}V-\frac{\gamma}{2}\mathcal{M}G^{2}+\gamma G\cdot\mathcal{M}G-\rho G+\gamma\rho\big(H-G^{2}\big)=0. Together, they explain the variational inequality in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) satisfied by VV. Similarly, both GG and HH are characterized separately for (x,t)∈P(x,t)\in\mathrm{P} and (x,t)∈NT(x,t)\in\mathrm{NT}, leading to ([3.4](https://arxiv.org/html/2511.08433v1#S3.E4 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), respectively.
Based on the partition of P\mathrm{P} and NT\mathrm{NT}, we know that if (x,t)∈Po(x,t)\in\mathrm{P}^{o} (interior of P\mathrm{P}), then the manager should immediately pay dividends to reach the boundary of the “no-transaction region” NT\mathrm{NT} or pay out all of xx in dividends if ∂NT\partial\mathrm{NT} (the boundary of NT\mathrm{NT}) is unreachable.888If ∂NT\partial\mathrm{NT} is unreachable from P\mathrm{P}, which could occur if (0,x]⊂P(0,x]\subset\mathrm{P} for some x>0x>0, then Δ​Dt∗=Xt−=x\Delta D^{\*}\_{t}=X\_{t^{-}}=x, and ruin occurs immediately.
Thereafter, the interventions are of “local-time type,” as described by the third equation in ([3.7](https://arxiv.org/html/2511.08433v1#S3.E7 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), to keep the company’s surplus within the no-transaction region (that is, (Xs∗,s)∈NT¯(X\_{s}^{\*},s)\in\overline{\mathrm{NT}}). Similar to Liang and Luo [[32](https://arxiv.org/html/2511.08433v1#bib.bib32)], the state-time space is divided into two regions (see ([3.2](https://arxiv.org/html/2511.08433v1#S3.E2 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) here and (3.1)–(3.2) therein), but Dai et al. [[17](https://arxiv.org/html/2511.08433v1#bib.bib17)] further separate the pay region P\mathrm{P} into “buy” and “sell” regions in their transaction costs model because buying and selling the risky asset incur costs at different rates.

###### Proof.

Suppose that V~\widetilde{V}, GG, and HH satisfy the conditions of this theorem, and suppose there exists a solution D∗∈𝒜tD^{\*}\in\mathcal{A}\_{t} to the Skorokhod reflection problem in ([3.7](https://arxiv.org/html/2511.08433v1#S3.E7 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). We prove the theorem in four steps.

Step 1. We show that if GG solves ([3.4](https://arxiv.org/html/2511.08433v1#S3.E4 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) with G​(0,t)=0G(0,t)=0, then G​(x,t)=𝔼x,t​(Yt∗)G(x,t)=\mathbb{E}\_{x,t}(Y\_{t}^{\*}) in ([3.8](https://arxiv.org/html/2511.08433v1#S3.E8 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

Fix (x,t)∈ℝ+2(x,t)\in\mathbb{R}\_{+}^{2} and a positive number k>tk>t.
By applying Itô’s formula to e−ρ⁣(⋅−t)​G​(X⋅∗,⋅)\mathrm{e}^{-\rho(\cdot-t)}G(X^{\*}\_{\cdot},\cdot), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | e−ρ​((τ∗∧k)−t)​G​(Xτ∗∧k∗,τ∗∧k)=G​(x,t)+∫tτ∗∧ke−ρ​(s−t)​(ℳ​G​(Xs∗,s)−ρ​G​(Xs∗,s))​ds\displaystyle\mathrm{e}^{-\rho((\tau^{\*}\wedge k)-t)}G(X^{\*}\_{\tau^{\*}\wedge k},\tau^{\*}\wedge k)=G(x,t)+\int\_{t}^{\tau^{\*}\wedge k}\mathrm{e}^{-\rho(s-t)}\big(\mathcal{M}G(X^{\*}\_{s},s)-\rho G(X^{\*}\_{s},s)\big)\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫tτ∗∧ke−ρ​(s−t)​∂xG​(Xs∗,s)​d​Ds∗,c+∫tτ∗∧ke−ρ​(s−t)​b​∂xG​(Xs∗,s)​d​Bs\displaystyle\quad-\int\_{t}^{\tau^{\*}\wedge k}\mathrm{e}^{-\rho(s-t)}\partial\_{x}G(X^{\*}\_{s},s)\,\mathrm{d}D^{\*,c}\_{s}+\int\_{t}^{\tau^{\*}\wedge k}\mathrm{e}^{-\rho(s-t)}b\,\partial\_{x}G(X^{\*}\_{s},s)\,\mathrm{d}B\_{s} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∑s∈[t,τ∗∧k]e−ρ​(s−t)​(G​(Xs−∗−Δ​Ds∗,s)−G​(Xs−∗,s)),\displaystyle\quad+\sum\_{s\in[t,\tau^{\*}\wedge k]}\mathrm{e}^{-\rho(s-t)}\big(G(X^{\*}\_{s^{-}}-\Delta D\_{s}^{\*},s)-G(X^{\*}\_{s^{-}},s)\big), |  | (3.9) |

in which D∗,cD^{\*,c} is the continuous part of D∗D^{\*}. The first integral in ([3](https://arxiv.org/html/2511.08433v1#S3.Ex1 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) equals 0 because (Xs∗,s)∈NT¯(X^{\*}\_{s},s)\in\overline{\mathrm{NT}} for all s>ts>t, on which ℳ​G−ρ​G=0\mathcal{M}G-\rho G=0 by ([3.4](https://arxiv.org/html/2511.08433v1#S3.E4 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).
The above discussion implies that a lump-sum dividend (Δ​Ds∗>0\Delta D^{\*}\_{s}>0) is only possible at the initial time tt when (x,t)∈Po(x,t)\in\mathrm{P}^{o};999The subsequent analysis follows even without explicitly using this result (that is, temporarily allowing Δ​Ds∗>0\Delta D\_{s}^{\*}>0 for s>ts>t). In that case, note Ds∗=Ds∗,c+∑u∈[t,s]Δ​Du∗D\_{s}^{\*}=D^{\*,c}\_{s}+\sum\_{u\in[t,s]}\,\Delta D^{\*}\_{u}.
in that case, we have G​(x−Δ​Dt∗,t)−G​(x,t)=∫0Δ​Dt∗∂xG​(Xt−∗−u,t)⋅𝟙{(Xt−∗,t)∈Po}​d​u=Δ​Dt∗⋅𝟙{(Xt−∗,t)∈Po}G(x-\Delta D\_{t}^{\*},t)-G(x,t)=\int\_{0}^{\Delta D\_{t}^{\*}}\,\partial\_{x}G(X^{\*}\_{t^{-}}-u,t)\cdot\mathds{1}\_{\{(X^{\*}\_{t^{-}},t)\in\mathrm{P}^{o}\}}\mathrm{d}u=\Delta D\_{t}^{\*}\cdot\mathds{1}\_{\{(X^{\*}\_{t^{-}},t)\in\mathrm{P}^{o}\}} because ∂xG=1\partial\_{x}G=1 on Po⊂P\mathrm{P}^{o}\subset\mathrm{P}. By using this result, we get

|  |  |  |
| --- | --- | --- |
|  | −∫tτ∗∧ke−ρ​(s−t)​∂xG​(Xs∗,s)​d​Ds∗,c+∑s∈[t,τ∗∧k]e−ρ​(s−t)​(G​(Xs−∗−Δ​Ds∗,s)−G​(Xs−∗,s))\displaystyle-\int\_{t}^{\tau^{\*}\wedge k}\mathrm{e}^{-\rho(s-t)}\partial\_{x}G(X^{\*}\_{s},s)\,\mathrm{d}D^{\*,c}\_{s}+\sum\_{s\in[t,\tau^{\*}\wedge k]}\mathrm{e}^{-\rho(s-t)}\big(G(X^{\*}\_{s^{-}}-\Delta D\_{s}^{\*},s)-G(X^{\*}\_{s^{-}},s)\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =−∫tτ∗∧ke−ρ​(s−t)​∂xG​(Xs∗,s)​d​Ds∗,c−Δ​Dt∗=−∫tτ∗∧ke−ρ​(s−t)​dDs∗,\displaystyle=-\int\_{t}^{\tau^{\*}\wedge k}\mathrm{e}^{-\rho(s-t)}\partial\_{x}G(X^{\*}\_{s},s)\,\mathrm{d}D^{\*,c}\_{s}-\Delta D\_{t}^{\*}=-\int\_{t}^{\tau^{\*}\wedge k}\mathrm{e}^{-\rho(s-t)}\,\mathrm{d}D^{\*}\_{s}, |  |

in which the last equality uses ∂xG=1\partial\_{x}G=1 on {d​Ds∗,c>0}⊂P\{\mathrm{d}D^{\*,c}\_{s}>0\}\subset\mathrm{P} and Ds∗=Ds∗,c+Δ​Dt∗D^{\*}\_{s}=D^{\*,c}\_{s}+\Delta D^{\*}\_{t}.

Next, we take conditional expectation on both sides of ([3](https://arxiv.org/html/2511.08433v1#S3.Ex1 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and use the above results, Condition 2 in the theorem, and G​(0,t)=0G(0,t)=0 to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(x,t)\displaystyle G(x,t) | =𝔼x,t​(∫tτ∗∧ke−ρ​(s−t)​dDs∗)+e−ρ​(k−t)​G​(Xk∗,k)⋅𝟙{τ∗>k},\displaystyle=\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau^{\*}\wedge k}\mathrm{e}^{-\rho(s-t)}\mathrm{d}D^{\*}\_{s}\bigg)+\mathrm{e}^{-\rho(k-t)}G(X^{\*}\_{k},k)\cdot\mathds{1}\_{\{\tau^{\*}>k\}}, |  |

which yields the desired assertion by sending k→∞k\to\infty and using Condition 2.

Step 2. We show that if HH solves ([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) with H​(0,t)=0H(0,t)=0, then H​(x,t)=𝔼x,t​((Yt∗)2)H(x,t)=\mathbb{E}\_{x,t}\big((Y\_{t}^{\*})^{2}\big) in ([3.8](https://arxiv.org/html/2511.08433v1#S3.E8 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) holds.

Fix (x,t)∈ℝ+2(x,t)\in\mathbb{R}\_{+}^{2} and assume that ruin has not occurred by time tt. Define a sequence of stopping times {ηn}n=1,2,…\{\eta\_{n}\}\_{n=1,2,\dots} by ηn:=inf{s≥t:Xs∗≥n}\eta\_{n}:=\inf\{s\geq t:X\_{s}^{\*}\geq n\}. For a fixed k>tk>t, denote τn,k=τ∗∧k∧ηn\tau\_{n,k}=\tau^{\*}\wedge k\wedge\eta\_{n}; define functions G^\hat{G} and H^\hat{H} by

|  |  |  |
| --- | --- | --- |
|  | G^​(x,t)=e−ρ​t​G​(x,t),andH^​(x,t)=e−2​ρ​t​H​(x,t).\hat{G}(x,t)=\mathrm{e}^{-\rho t}G(x,t),\quad\hbox{and}\quad\hat{H}(x,t)=\mathrm{e}^{-2\rho t}H(x,t). |  |

By applying Itô’s formula to G^​(X⋅∗,⋅)\hat{G}(X^{\*}\_{\cdot},\cdot) as in Step 1, we deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | G^​(Xs∗,s)=∫sτn,ke−ρ​u​dDu∗−∫sτn,kb​∂^x​G​(Xu∗,u)​dBu+G^​(Xτn,k∗,τn,k).\hat{G}(X^{\*}\_{s},s)=\int\_{s}^{\tau\_{n,k}}\mathrm{e}^{-\rho u}\,\mathrm{d}D^{\*}\_{u}-\int\_{s}^{\tau\_{n,k}}b\,\hat{\partial}\_{x}G(X^{\*}\_{u},u)\,\mathrm{d}B\_{u}+\hat{G}(X^{\*}\_{\tau\_{n,k}},\tau\_{n,k}). |  | (3.10) |

It follows from ([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3.6](https://arxiv.org/html/2511.08433v1#S3.E6 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) that H^\hat{H} solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​H^​(x,t)​𝟙{(x,t)∈NT}+(2​e−ρ​t​G^​(x,t)−∂xH^​(x,t))​𝟙{(x,t)∈P}=0,H^​(0,t)=0.\mathcal{M}\hat{H}(x,t)\mathds{1}\_{\{(x,t)\in\mathrm{NT}\}}+\big(2\mathrm{e}^{-\rho t}\hat{G}(x,t)-\partial\_{x}\hat{H}(x,t)\big)\mathds{1}\_{\{(x,t)\in\mathrm{P}\}}=0,\quad\hat{H}(0,t)=0. |  | (3.11) |

By applying Itô’s formula to H^​(X⋅∗,⋅)\hat{H}(X^{\*}\_{\cdot},\cdot) and using the results from Step 1, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^​(Xτn,k∗,τn,k)\displaystyle\hat{H}(X^{\*}\_{\tau\_{n,k}},\tau\_{n,k}) | =H^​(x,t)+∫tτn,kℳ​H^​(Xs∗,s)​ds+∫tτn,kb​∂xH^​(Xs∗,s)​d​Bs\displaystyle=\hat{H}(x,t)+\int\_{t}^{\tau\_{n,k}}\mathcal{M}\hat{H}(X^{\*}\_{s},s)\,\mathrm{d}s+\int\_{t}^{\tau\_{n,k}}b\,\partial\_{x}\hat{H}(X^{\*}\_{s},s)\,\mathrm{d}B\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫tτn,k∂xH^​(Xs∗,s)​d​Ds∗,c+∑s∈[t,τn,k](H^​(Xs−∗−Δ​Ds∗,s)−H^​(Xs−∗,s))\displaystyle\quad-\int\_{t}^{\tau\_{n,k}}\partial\_{x}\hat{H}(X^{\*}\_{s},s)\,\mathrm{d}D^{\*,c}\_{s}+\sum\_{s\in[t,\tau\_{n,k}]}\left(\hat{H}(X^{\*}\_{s^{-}}-\Delta D^{\*}\_{s},s)-\hat{H}(X^{\*}\_{s^{-}},s)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =H^​(x,t)+∫tτn,kℳ​H^​(Xs∗,s)​ds+∫tτn,kb​∂xH^​(Xs∗,s)​d​Bs\displaystyle=\hat{H}(x,t)+\int\_{t}^{\tau\_{n,k}}\mathcal{M}\hat{H}(X^{\*}\_{s},s)\,\mathrm{d}s+\int\_{t}^{\tau\_{n,k}}b\,\partial\_{x}\hat{H}(X^{\*}\_{s},s)\,\mathrm{d}B\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫tτn,k∂xH^​(Xs∗,s)​d​Ds∗+(∂xH^​(x,t)​Δ​Dt∗+H^​(x−Δ​Dt∗,t)−H^​(x,t))​𝟙{(x,t)∈Po}\displaystyle\quad-\int\_{t}^{\tau\_{n,k}}\partial\_{x}\hat{H}(X^{\*}\_{s},s)\,\mathrm{d}D^{\*}\_{s}+\left(\partial\_{x}\hat{H}(x,t)\Delta D^{\*}\_{t}+\hat{H}(x-\Delta D^{\*}\_{t},t)-\hat{H}(x,t)\right)\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =H^​(x,t)+∫tτn,kb​∂xH^​(Xs∗,s)​d​Bs−∫tτn,k2​e−ρ​s​G^​(Xs∗,s)​dDs∗\displaystyle=\hat{H}(x,t)+\int\_{t}^{\tau\_{n,k}}b\,\partial\_{x}\hat{H}(X^{\*}\_{s},s)\,\mathrm{d}B\_{s}-\int\_{t}^{\tau\_{n,k}}2\mathrm{e}^{-\rho s}\hat{G}(X^{\*}\_{s},s)\,\mathrm{d}D^{\*}\_{s} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(2​e−ρ​t​G^​(x,t)​Δ​Dt∗+H^​(x−Δ​Dt∗,t)−H^​(x,t))​𝟙{(x,t)∈Po},\displaystyle\quad+\left(2\mathrm{e}^{-\rho t}\hat{G}(x,t)\Delta D^{\*}\_{t}+\hat{H}(x-\Delta D^{\*}\_{t},t)-\hat{H}(x,t)\right)\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}}, |  | (3.12) |

in which we use ℳ​H^=0\mathcal{M}\hat{H}=0 on NT\mathrm{NT} and ∂xH^=2​e−ρ​t​G^\partial\_{x}\hat{H}=2\mathrm{e}^{-\rho t}\hat{G} on P\mathrm{P}; recall that Xs−∗−Xs∗=Δ​Ds∗>0X^{\*}\_{s^{-}}-X^{\*}\_{s}=\Delta D^{\*}\_{s}>0 if and only if s=ts=t and (x,t)∈Po(x,t)\in\mathrm{P}^{o}.
To analyze H^​(x−Δ​Dt∗,t)−H^​(x,t)\hat{H}(x-\Delta D^{\*}\_{t},t)-\hat{H}(x,t) when (x,t)∈Po(x,t)\in\mathrm{P}^{o}, note that for all z∈[x−Δ​Dt∗,x]z\in[x-\Delta D^{\*}\_{t},x], (z,t)∈P(z,t)\in\mathrm{P}, and given Xt−=zX\_{t^{-}}=z, there is an immediate lump-sum payment of size z−(x−Δ​Dt∗)z-(x-\Delta D^{\*}\_{t}) at time tt, implying
G​(z,t)=𝔼z,t​(Yt∗)=𝔼x−Δ​Dt∗,t​(Yt∗)+(z−(x−Δ​Dt∗))G(z,t)=\mathbb{E}\_{z,t}(Y\_{t}^{\*})=\mathbb{E}\_{x-\Delta D^{\*}\_{t},t}(Y^{\*}\_{t})+\big(z-(x-\Delta D^{\*}\_{t})\big).
Using these results, along with ([3.11](https://arxiv.org/html/2511.08433v1#S3.E11 "In 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^​(x−Δ​Dt∗,t)−H^​(x,t)\displaystyle\hat{H}(x-\Delta D^{\*}\_{t},t)-\hat{H}(x,t) | =−∫x−Δ​Dt∗x∂xH^​(z,t)​d​z=−2​e−ρ​t​∫x−Δ​Dt∗xG^​(z,t)​dz\displaystyle=-\int\_{x-\Delta D^{\*}\_{t}}^{x}\partial\_{x}\hat{H}(z,t)\,\mathrm{d}z=-2\mathrm{e}^{-\rho t}\int\_{x-\Delta D^{\*}\_{t}}^{x}\hat{G}(z,t)\,\mathrm{d}z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−2​e−2​ρ​t​∫x−Δ​Dt∗x(𝔼x−Δ​Dt∗,t​(Yt∗)+(z−(x−Δ​Dt∗)))​dz\displaystyle=-2\mathrm{e}^{-2\rho t}\int\_{x-\Delta D^{\*}\_{t}}^{x}\left(\mathbb{E}\_{x-\Delta D^{\*}\_{t},t}(Y^{\*}\_{t})+\big(z-(x-\Delta D^{\*}\_{t})\big)\right)\mathrm{d}z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−2​e−2​ρ​t​(Δ​Dt∗⋅𝔼x−Δ​Dt∗,t​(Yt∗)+12​(Δ​Dt∗)2)\displaystyle=-2\mathrm{e}^{-2\rho t}\left(\Delta D^{\*}\_{t}\cdot\mathbb{E}\_{x-\Delta D^{\*}\_{t},t}(Y^{\*}\_{t})+\dfrac{1}{2}\,(\Delta D^{\*}\_{t})^{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−e−2​ρ​t​(2​Δ​Dt∗⋅𝔼x,t​(∫tτ∗e−ρ​(s−t)​dDs∗−Δ​Dt∗)+(Δ​Dt∗)2)\displaystyle=-\mathrm{e}^{-2\rho t}\left(2\Delta D^{\*}\_{t}\cdot\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau^{\*}}\mathrm{e}^{-\rho(s-t)}\,\mathrm{d}D^{\*}\_{s}-\Delta D^{\*}\_{t}\bigg)+(\Delta D^{\*}\_{t})^{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−e−2​ρ​t​(2​Δ​Dt∗⋅𝔼x,t​(∫tτ∗e−ρ​(s−t)​dDs∗)−(Δ​Dt∗)2).\displaystyle=-\mathrm{e}^{-2\rho t}\left(2\Delta D^{\*}\_{t}\cdot\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau^{\*}}\mathrm{e}^{-\rho(s-t)}\,\mathrm{d}D^{\*}\_{s}\bigg)-(\Delta D^{\*}\_{t})^{2}\right).\hskip 50.00008pt |  | (3.13) |

Then, combining ([3](https://arxiv.org/html/2511.08433v1#S3.Ex7 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) with ([3.10](https://arxiv.org/html/2511.08433v1#S3.E10 "In 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3](https://arxiv.org/html/2511.08433v1#S3.Ex12 "3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and taking conditional expectations imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^​(x,t)\displaystyle\hat{H}(x,t) | =𝔼x,t​(H^​(Xτn,k∗,τn,k))+2​𝔼x,t​(∫tτn,ke−ρ​s​(∫sτn,ke−ρ​u​dDu∗)​dDs∗)\displaystyle=\mathbb{E}\_{x,t}\Big(\hat{H}(X^{\*}\_{\tau\_{n,k}},\tau\_{n,k})\Big)+2\,\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau\_{n,k}}\mathrm{e}^{-\rho s}\left(\int\_{s}^{\tau\_{n,k}}\mathrm{e}^{-\rho u}\mathrm{d}D^{\*}\_{u}\right)\mathrm{d}D^{\*}\_{s}\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​𝔼x,t​(G^​(Xτn,k∗,τn,k)​(∫tτn,ke−ρ​s​dDs∗−e−ρ​t​Δ​Dt∗⋅𝟙{(x,t)∈Po}))\displaystyle\quad+2\,\mathbb{E}\_{x,t}\bigg(\hat{G}(X^{\*}\_{\tau\_{n,k}},\tau\_{n,k})\bigg(\int\_{t}^{\tau\_{n,k}}\mathrm{e}^{-\rho s}\mathrm{d}D^{\*}\_{s}-\mathrm{e}^{-\rho t}\Delta D^{\*}\_{t}\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}}\bigg)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e−2​ρ​t​(Δ​Dt∗)2​ 1{(x,t)∈Po},\displaystyle\quad-\mathrm{e}^{-2\rho t}(\Delta D^{\*}\_{t})^{2}\,\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}}, |  |

in which we have used the fact that G^\hat{G} and H^\hat{H} are at least 𝒞1\mathcal{C}^{1} with respect to xx, and 0<Xs∗≤n0<X\_{s}^{\*}\leq n for all s∈[t,τn,k]s\in[t,\tau\_{n,k}] to deduce that all stochastic integrals involved above have zero expectations.

The growth conditions on GG and HH imply that as n→∞n\to\infty and k→∞k\to\infty, 𝔼x,t​(H^​(Xτn,k∗,τn,k))→0\mathbb{E}\_{x,t}\big(\hat{H}(X^{\*}\_{\tau\_{n,k}},\tau\_{n,k})\big)\to 0 and 𝔼x,t​(G^​(Xτn,k∗,τn,k))→0\mathbb{E}\_{x,t}\big(\hat{G}(X^{\*}\_{\tau\_{n,k}},\tau\_{n,k})\big)\to 0; also, τn,k→τ∗\tau\_{n,k}\to\tau^{\*}, and the monotone convergence theorem applies. Therefore, upon sending n→∞n\to\infty and k→∞k\to\infty, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^​(x,t)\displaystyle\hat{H}(x,t) | =2​𝔼x,t​(∫tτ∗e−ρ​s​(∫sτ∗e−ρ​u​dDu∗)​dDs∗)−e−2​ρ​t​(Δ​Dt∗)2⋅𝟙{(x,t)∈Po}\displaystyle=2\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau^{\*}}\mathrm{e}^{-\rho s}\left(\int\_{s}^{\tau^{\*}}\mathrm{e}^{-\rho u}\mathrm{d}D^{\*}\_{u}\right)\mathrm{d}D^{\*}\_{s}\bigg)-\mathrm{e}^{-2\rho t}(\Delta D^{\*}\_{t})^{2}\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​𝔼x,t​(∫t+τ∗e−ρ​s​(∫sτ∗e−ρ​u​dDu∗)​dDs∗)+2​e−ρ​t​Δ​Dt∗​𝔼x,t​(∫tτ∗e−ρ​u​dDu∗)⋅𝟙{(x,t)∈Po}\displaystyle=2\mathbb{E}\_{x,t}\bigg(\int\_{t^{+}}^{\tau^{\*}}\mathrm{e}^{-\rho s}\left(\int\_{s}^{\tau^{\*}}\mathrm{e}^{-\rho u}\mathrm{d}D^{\*}\_{u}\right)\mathrm{d}D^{\*}\_{s}\bigg)+2\mathrm{e}^{-\rho t}\Delta D^{\*}\_{t}\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau^{\*}}\mathrm{e}^{-\rho u}\mathrm{d}D^{\*}\_{u}\bigg)\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e−2​ρ​t​(Δ​Dt∗)2⋅𝟙{(x,t)∈Po}\displaystyle\quad-\mathrm{e}^{-2\rho t}(\Delta D^{\*}\_{t})^{2}\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​𝔼x,t​(∫tτ∗e−ρ​s​(∫sτ∗e−ρ​u​dDu∗,c)​dDs∗,c)\displaystyle=2\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau^{\*}}\mathrm{e}^{-\rho s}\left(\int\_{s}^{\tau^{\*}}\mathrm{e}^{-\rho u}\mathrm{d}D^{\*,c}\_{u}\right)\mathrm{d}D^{\*,c}\_{s}\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​e−ρ​t​Δ​Dt∗​𝔼x,t​(∫tτ∗e−ρ​u​dDu∗,c+e−ρ​t​Δ​Dt∗⋅𝟙{(x,t)∈Po})⋅𝟙{(x,t)∈Po}\displaystyle\quad+2\mathrm{e}^{-\rho t}\Delta D^{\*}\_{t}\,\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau^{\*}}\mathrm{e}^{-\rho u}\mathrm{d}D^{\*,c}\_{u}+\mathrm{e}^{-\rho t}\Delta D^{\*}\_{t}\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}}\bigg)\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e−2​ρ​t​(Δ​Dt∗)2⋅𝟙{(x,t)∈Po}\displaystyle\quad-\mathrm{e}^{-2\rho t}(\Delta D^{\*}\_{t})^{2}\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼x,t​((∫tτ∗e−ρ​s​dDs∗,c+e−ρ​t​Δ​Dt∗⋅𝟙{(x,t)∈Po})2)\displaystyle=\mathbb{E}\_{x,t}\bigg(\bigg(\int\_{t}^{\tau^{\*}}\,\mathrm{e}^{-\rho s}\,\mathrm{d}D^{\*,c}\_{s}+\mathrm{e}^{-\rho t}\Delta D^{\*}\_{t}\cdot\mathds{1}\_{\{(x,t)\in\mathrm{P}^{o}\}}\bigg)^{2}\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼x,t​((∫tτ∗e−ρ​s​dDs∗)2)=𝔼x,t​((Yt∗)2),\displaystyle=\mathbb{E}\_{x,t}\bigg(\bigg(\int\_{t}^{\tau^{\*}}\,\mathrm{e}^{-\rho s}\,\mathrm{d}D^{\*}\_{s}\bigg)^{2}\bigg)=\mathbb{E}\_{x,t}\big(\left(Y\_{t}^{\*}\right)^{2}\big), |  |

thereby, proving the result in ([3.8](https://arxiv.org/html/2511.08433v1#S3.E8 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

Step 3. We show that if V~\widetilde{V} solves ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) with V~​(0,t)=0\widetilde{V}(0,t)=0, then V~​(x,t)=J​(x,t;D∗)\widetilde{V}(x,t)=J(x,t;D^{\*}).

First, we consider (x,t)∈NT(x,t)\in\mathrm{NT}; in this case, the first term in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) equals 0. Using this identity, along with ([3.4](https://arxiv.org/html/2511.08433v1#S3.E4 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​(V~​(x,t)−γ2​G2​(x,t))\displaystyle\mathcal{M}\Big(\widetilde{V}(x,t)-\dfrac{\gamma}{2}\,G^{2}(x,t)\Big) | =−γ​G​(x,t)​ℳ​G​(x,t)+ρ​G​(x,t)−γ​ρ​(H​(x,t)−G2​(x,t))\displaystyle=-\gamma G(x,t)\mathcal{M}G(x,t)+\rho G(x,t)-\gamma\rho\big(H(x,t)-G^{2}(x,t)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ρ​G​(x,t)−γ​ρ​H​(x,t)=ℳ​(G​(x,t)−γ2​H​(x,t)).\displaystyle=\rho G(x,t)-\gamma\rho H(x,t)=\mathcal{M}\Big(G(x,t)-\dfrac{\gamma}{2}\,H(x,t)\Big). |  |

We, then, apply similar arguments as in Step 1 to V~​(x,t)−γ2​G2​(x,t)\widetilde{V}(x,t)-\frac{\gamma}{2}\,G^{2}(x,t) and G​(x,t)−γ2​H​(x,t)G(x,t)-\frac{\gamma}{2}\,H(x,t) and use the above equality, the transversality condition, and V~​(0,t)−γ2​G2​(0,t)=0=G​(0,t)−γ2​H​(0,t)\widetilde{V}(0,t)-\frac{\gamma}{2}\,G^{2}(0,t)=0=G(0,t)-\frac{\gamma}{2}H(0,t) to conclude that V~​(x,t)=G​(x,t)−γ2​(H​(x,t)−G2​(x,t))=𝔼x,t​(Yt∗)−γ2​𝕍x,t​(Yt∗)=J​(x,t;D∗)\widetilde{V}(x,t)=G(x,t)-\frac{\gamma}{2}(H(x,t)-G^{2}(x,t))=\mathbb{E}\_{x,t}(Y\_{t}^{\*})-\frac{\gamma}{2}\mathbb{V}\_{x,t}(Y\_{t}^{\*})=J(x,t;D^{\*}).

Next, we consider (x,t)∈P(x,t)\in\mathrm{P}; in this case, ∂xV~​(x,t)=∂xG​(x,t)=1\partial\_{x}\widetilde{V}(x,t)=\partial\_{x}G(x,t)=1 and ∂xH​(x,t)=2​G​(x,t)\partial\_{x}H(x,t)=2G(x,t). As such,

|  |  |  |
| --- | --- | --- |
|  | ∂x(V~​(x,t)−γ2​G2​(x,t))=1−γ​G​(x,t)=∂x(G​(x,t)−γ2​H​(x,t)),\partial\_{x}\Big(\widetilde{V}(x,t)-\dfrac{\gamma}{2}\,G^{2}(x,t)\Big)=1-\gamma G(x,t)=\partial\_{x}\Big(G(x,t)-\dfrac{\gamma}{2}\,H(x,t)\Big), |  |

which, along with the boundary condition, confirms V~​(x,t)=J​(x,t;D∗)\widetilde{V}(x,t)=J(x,t;D^{\*}) for this case.

Therefore, for all (x,t)∈ℝ+2(x,t)\in\mathbb{R}\_{+}^{2}, V~​(x,t)=J​(x,t;D∗)\widetilde{V}(x,t)=J(x,t;D^{\*}) holds as desired.

Step 4. We show that if D∗∈𝒜tD^{\*}\in\mathcal{A}\_{t} solves ([3.7](https://arxiv.org/html/2511.08433v1#S3.E7 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), then D∗D^{\*} is an equilibrium dividend strategy.

To that end, define the perturbed strategy DεD^{\varepsilon} as in ([2.4](https://arxiv.org/html/2511.08433v1#S2.E4 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), and we want to prove that the limit in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) holds. Recall that d∈[0,x]d\in[0,x] is the lump-sum payment at tt under DεD^{\varepsilon}. First, assume d=xd=x, and ruin occurs immediately at tt under DεD^{\varepsilon}, resulting in J​(x,t;Dε)=xJ(x,t;D^{\varepsilon})=x. Because V​(0,t)=0V(0,t)=0 and ∂xV​(x,t)≥1\partial\_{x}V(x,t)\geq 1, it follows that V​(x,t)≥x=J​(x,t;Dε)V(x,t)\geq x=J(x,t;D^{\varepsilon}) for all (x,t)(x,t), and, thus, the limit in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) holds when d=xd=x.

Given the above analysis, we assume d<xd<x in the remainder of this step; we also write X:=XDεX:=X^{D^{\varepsilon}}, Yt:=YtDεY\_{t}:=Y\_{t}^{D^{\varepsilon}}, and τ:=τDε\tau:=\tau^{D^{\varepsilon}} for notational simplicity in the proof.
By definition, J​(x,t;Dε)=𝔼x,t​(Yt)−γ2​𝔼x,t​(Yt2)+γ2​(𝔼x,t​(Yt))2J(x,t;D^{\varepsilon})=\mathbb{E}\_{x,t}(Y\_{t})-\frac{\gamma}{2}\mathbb{E}\_{x,t}\big(Y\_{t}^{2}\big)+\frac{\gamma}{2}\big(\mathbb{E}\_{x,t}(Y\_{t})\big)^{2}; in what follows, we analyze each of the three terms in J​(x,t;Dε)J(x,t;D^{\varepsilon}) by expanding them to order o​(ε)o(\varepsilon).
To start, we recall an important result on finite-time ruin probabilities (see, for instance, Appendix in Grandell [[22](https://arxiv.org/html/2511.08433v1#bib.bib22)])

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙx,t​(τ>t+ε)∼1−b​εx​exp⁡(−12​ε​(xb)2)=1+o​(ε);\displaystyle\mathbb{P}\_{x,t}\big(\tau>t+\varepsilon\big)\sim 1-\frac{b\sqrt{\varepsilon}}{x}\,\exp\left(-\frac{1}{2\varepsilon}\left(\frac{x}{b}\right)^{2}\right)=1+o(\varepsilon); |  | (3.14) |

with this result, we can omit 𝟙{τ>t+ε}\mathds{1}\_{\{\tau>t+\varepsilon\}} in the following derivations.
For convenience, in the derivation below, we introduce

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Gt\displaystyle G\_{t} | :=G​(x−d,t),\displaystyle:=G(x-d,t), | Ht\displaystyle H\_{t} | :=H​(x−d,t);\displaystyle:=H(x-d,t); |  | (3.15) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 𝐈ρ\displaystyle\mathbf{I}\_{\rho} | :=∫t+t+εe−ρ​(s−t)​dδ​(s),\displaystyle:=\int\_{t^{+}}^{t+\varepsilon}\mathrm{e}^{-\rho(s-t)}\mathrm{d}\delta(s), | 𝐈ϕ\displaystyle\mathbf{I}\_{\phi} | :=𝔼x,t​(∫t+t+ε∂xϕ​(Xs,s)​d​δ​(s)),ϕ∈𝒞1,1​(ℝ+2).\displaystyle:=\mathbb{E}\_{x,t}\left(\int\_{t^{+}}^{t+\varepsilon}\partial\_{x}\phi(X\_{s},s)\mathrm{d}\delta(s)\right),\;\phi\in\mathcal{C}^{1,1}(\mathbb{R}\_{+}^{2}). |  | (3.16) |

Recall from Definition [2.2](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") that δ\delta is a non-decreasing, continuous function over [t,t+ε)[t,t+\varepsilon), satisfying δ​(t+ε)−δ​(t)=O​(ε)\delta(t+\varepsilon)-\delta(t)=O(\varepsilon) as ε→0\varepsilon\to 0. As such, for ε\varepsilon small enough, 𝐈ρ\mathbf{I}\_{\rho} can be approximated by

|  |  |  |
| --- | --- | --- |
|  | 𝐈ρ=∫t+t+ε1​dδ​(s)+o​(ε)=𝐈ϕ+o​(ε), with ​ϕ​(x,s)≡x.\displaystyle\mathbf{I}\_{\rho}=\int\_{t^{+}}^{t+\varepsilon}1\,\mathrm{d}\delta(s)+o(\varepsilon)=\mathbf{I}\_{\phi}+o(\varepsilon),\text{ with }\phi(x,s)\equiv x. |  |

Now using the fact that ϕ\phi is at least 𝒞1\mathcal{C}^{1} for any of ϕ=x,G\phi=x,G, or HH, the following estimates hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐈ϕ=C​ε+o​(ε) and 𝐈ϕ​𝐈ϕ′=C′​ε2+o​(ε2),ϕ,ϕ′=x,G,H,\displaystyle\mathbf{I}\_{\phi}=\mathrm{C}\varepsilon+o(\varepsilon)\quad\text{ and }\quad\mathbf{I}\_{\phi}\mathbf{I}\_{\phi^{\prime}}=\mathrm{C}^{\prime}\varepsilon^{2}+o(\varepsilon^{2}),\quad\phi,\phi^{\prime}=x,G,H, |  | (3.17) |

for some positive constants C\mathrm{C} and C′\mathrm{C}^{\prime} that might depend on ϕ\phi and ϕ′\phi^{\prime}. Note that the latter result allows us to safely drop terms involving 𝐈ϕ​𝐈ϕ′\mathbf{I}\_{\phi}\mathbf{I}\_{\phi^{\prime}} if we truncate at the order o​(ε)o(\varepsilon).

First, we analyze 𝔼x,t​(Yt)\mathbb{E}\_{x,t}(Y\_{t}) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x,t​(Yt)\displaystyle\mathbb{E}\_{x,t}(Y\_{t}) | =𝔼x,t​(∫tτe−ρ​(s−t)​dDsε)=𝔼x,t​(d+∫t+t+εe−ρ​(s−t)​dδ​(s)+∫t+ετe−ρ​(s−t)​dDs∗)\displaystyle=\mathbb{E}\_{x,t}\bigg(\int\_{t}^{\tau}\mathrm{e}^{-\rho(s-t)}\mathrm{d}D^{\varepsilon}\_{s}\bigg)=\mathbb{E}\_{x,t}\bigg(d+\int\_{t^{+}}^{t+\varepsilon}\mathrm{e}^{-\rho(s-t)}\mathrm{d}\delta(s)+\int\_{t+\varepsilon}^{\tau}\mathrm{e}^{-\rho(s-t)}\mathrm{d}D^{\*}\_{s}\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d+𝐈ρ+𝔼x,t​(e−ρ​ε​𝟙{τ>t+ε}​𝔼Xt+ε,t+ε​(∫t+ετ∗e−ρ​(s−(t+ε))​dDs∗))+o​(ε)\displaystyle=d+\mathbf{I}\_{\rho}+\mathbb{E}\_{x,t}\bigg(\mathrm{e}^{-\rho\varepsilon}\mathds{1}\_{\{\tau>t+\varepsilon\}}\,\mathbb{E}\_{X\_{t+\varepsilon},t+\varepsilon}\bigg(\int\_{t+\varepsilon}^{\tau^{\*}}\mathrm{e}^{-\rho(s-(t+\varepsilon))}\mathrm{d}D^{\*}\_{s}\bigg)\bigg)+o(\varepsilon) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d+𝐈ρ+(1−ρ​ε)​𝔼x,t​(G​(Xt+ε,t+ε))+o​(ε)\displaystyle=d+\mathbf{I}\_{\rho}+(1-\rho\varepsilon)\,\mathbb{E}\_{x,t}\big(G(X\_{t+\varepsilon},t+\varepsilon)\big)+o(\varepsilon) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d+𝐈ρ+(1−ρε)𝔼x,t(G(x,t)+∫t+t+εℳG(Xs,s)ds+∫t+t+εb∂xG(Xs,s)dBs\displaystyle=d+\mathbf{I}\_{\rho}+(1-\rho\varepsilon)\,\,\mathbb{E}\_{x,t}\bigg(G(x,t)+\int\_{t^{+}}^{t+\varepsilon}\mathcal{M}G(X\_{s},s)\,\mathrm{d}s+\int\_{t^{+}}^{t+\varepsilon}b\,\partial\_{x}G(X\_{s},s)\,\mathrm{d}B\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫t+t+ε∂xG(Xs,s)dδ(s)+G(x−d,t)−G(x,t))+o(ε)\displaystyle\quad-\int\_{t^{+}}^{t+\varepsilon}\,\partial\_{x}G(X\_{s},s)\,\mathrm{d}\delta(s)+G(x-d,t)-G(x,t)\bigg)+o(\varepsilon) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d+Gt+ε​(ℳ​Gt−ρ​Gt)+𝐈ρ−𝐈G+o​(ε).\displaystyle=d+G\_{t}+\varepsilon\big(\mathcal{M}G\_{t}-\rho G\_{t}\big)+\mathbf{I}\_{\rho}-\mathbf{I}\_{G}+o(\varepsilon). |  |

Next, we consider 𝔼x,t​((Yt)2)\mathbb{E}\_{x,t}\big((Y\_{t})^{2}\big); by using the Itô’s expansion for G​(Xt+ε,t+ε)G(X\_{t+\varepsilon},t+\varepsilon) and H​(Xt+ε,t+ε)H(X\_{t+\varepsilon},t+\varepsilon) as above, along with ([3.8](https://arxiv.org/html/2511.08433v1#S3.E8 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3.14](https://arxiv.org/html/2511.08433v1#S3.E14 "In 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x,t​(Yt2)\displaystyle\mathbb{E}\_{x,t}\big(Y\_{t}^{2}\big) | =𝔼x,t​[(d+𝐈ρ+∫t+ετe−ρ​(s−t)​dDs∗)2]\displaystyle=\mathbb{E}\_{x,t}\bigg[\Big(d+\mathbf{I}\_{\rho}+\int\_{t+\varepsilon}^{\tau}\mathrm{e}^{-\rho(s-t)}\mathrm{d}D^{\*}\_{s}\Big)^{2}\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d2+𝐈ρ2+e−2​ρ​ε​𝔼x,t​(H​(Xt+ε,t+ε))+2​d​𝐈ρ\displaystyle=d^{2}+\mathbf{I}\_{\rho}^{2}+\mathrm{e}^{-2\rho\varepsilon}\,\mathbb{E}\_{x,t}\big(H(X\_{t+\varepsilon},t+\varepsilon)\big)+2d\mathbf{I}\_{\rho} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​(d+𝐈ρ)​e−ρ​ε​𝔼x,t​(G​(Xt+ε,t+ε))+o​(ε)\displaystyle\quad+2(d+\mathbf{I}\_{\rho})\mathrm{e}^{-\rho\varepsilon}\,\mathbb{E}\_{x,t}\big(G(X\_{t+\varepsilon},t+\varepsilon)\big)+o(\varepsilon) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d2+𝐈ρ2+(1−2​ρ​ε)​(Ht+ε​ℳ​Ht−𝐈H)+2​d​𝐈ρ\displaystyle=d^{2}+\mathbf{I}\_{\rho}^{2}+(1-2\rho\varepsilon)\big(H\_{t}+\varepsilon\,\mathcal{M}H\_{t}-\mathbf{I}\_{H}\big)+2d\mathbf{I}\_{\rho} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​(d+𝐈ρ)​(1−ρ​ε)​(Gt+ε​ℳ​Gt−𝐈G)+o​(ε)\displaystyle\quad+2(d+\mathbf{I}\_{\rho})(1-\rho\varepsilon)\big(G\_{t}+\varepsilon\,\mathcal{M}G\_{t}-\mathbf{I}\_{G}\big)+o(\varepsilon) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d2+𝐈ρ2+Ht+ε​(ℳ​Ht−2​ρ​Ht)−𝐈H+2​d​𝐈ρ\displaystyle=d^{2}+\mathbf{I}\_{\rho}^{2}+H\_{t}+\varepsilon\left(\mathcal{M}H\_{t}-2\rho H\_{t}\right)-\mathbf{I}\_{H}+2d\mathbf{I}\_{\rho} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​d​(Gt+ε​(ℳ​Gt−ρ​Gt))+2​𝐈ρ​Gt−2​d​𝐈G−2​𝐈ρ​𝐈G+o​(ε).\displaystyle\quad+2d\big(G\_{t}+\varepsilon\left(\mathcal{M}G\_{t}-\rho G\_{t}\right)\big)+2\mathbf{I}\_{\rho}G\_{t}-2d\mathbf{I}\_{G}-2\mathbf{I}\_{\rho}\mathbf{I}\_{G}+o(\varepsilon). |  |

We proceed to analyze the third term (𝔼x,t​(Yt))2\big(\mathbb{E}\_{x,t}(Y\_{t})\big)^{2}. By using the results about 𝔼x,t​(Yt)\mathbb{E}\_{x,t}(Y\_{t}), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔼x,t​(Yt))2\displaystyle\big(\mathbb{E}\_{x,t}(Y\_{t})\big)^{2} | =(d+Gt+ε​(ℳ​Gt−ρ​Gt)+𝐈ρ−𝐈G+o​(ε))2\displaystyle=\big(d+G\_{t}+\varepsilon\big(\mathcal{M}G\_{t}-\rho G\_{t}\big)+\mathbf{I}\_{\rho}-\mathbf{I}\_{G}+o(\varepsilon)\big)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(d+Gt)2+2​ε​(d+Gt)​(ℳ​Gt−ρ​Gt)+2​(d+Gt)​(𝐈ρ−𝐈G)+(𝐈ρ−𝐈G)2+o​(ε).\displaystyle=(d+G\_{t})^{2}+2\varepsilon(d+G\_{t})(\mathcal{M}G\_{t}-\rho G\_{t})+2(d+G\_{t})(\mathbf{I}\_{\rho}-\mathbf{I}\_{G})+(\mathbf{I}\_{\rho}-\mathbf{I}\_{G})^{2}+o(\varepsilon). |  |

By combining the analysis of the three terms above and using the approximation 𝐈ρ=𝐈x+o​(ε)\mathbf{I}\_{\rho}=\mathbf{I}\_{x}+o(\varepsilon), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(x,t;Dε)\displaystyle J(x,t;D^{\varepsilon}) | =d+Gt+ε​(ℳ​Gt−ρ​Gt)\displaystyle=d+G\_{t}+\varepsilon\big(\mathcal{M}G\_{t}-\rho G\_{t}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​(d2+(Ht+ε​(ℳ​Ht−2​ρ​Ht))+2​d​(Gt+ε​(ℳ​Gt−ρ​Gt)))\displaystyle\quad-\frac{\gamma}{2}\big(d^{2}+\big(H\_{t}+\varepsilon(\mathcal{M}H\_{t}-2\rho H\_{t})\big)+2d\big(G\_{t}+\varepsilon\left(\mathcal{M}G\_{t}-\rho G\_{t}\right)\big)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +γ2​((d+Gt)2+2​ε​(d+Gt)​(ℳ​Gt−ρ​Gt))\displaystyle\quad+\frac{\gamma}{2}\left((d+G\_{t})^{2}+2\varepsilon(d+G\_{t})(\mathcal{M}G\_{t}-\rho G\_{t})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​(𝐈ρ2−𝐈H+2​d​𝐈ρ+2​𝐈ρ​Gt−2​d​𝐈G−2​𝐈ρ​𝐈G)\displaystyle\quad-\frac{\gamma}{2}\left(\mathbf{I}\_{\rho}^{2}-\mathbf{I}\_{H}+2d\mathbf{I}\_{\rho}+2\mathbf{I}\_{\rho}G\_{t}-2d\mathbf{I}\_{G}-2\mathbf{I}\_{\rho}\mathbf{I}\_{G}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +γ2​(2​(d+Gt)​(𝐈ρ−𝐈G)+(𝐈ρ−𝐈G)2)+𝐈ρ−𝐈G+o​(ε)\displaystyle\quad+\frac{\gamma}{2}\left(2(d+G\_{t})(\mathbf{I}\_{\rho}-\mathbf{I}\_{G})+(\mathbf{I}\_{\rho}-\mathbf{I}\_{G})^{2}\right)+\mathbf{I}\_{\rho}-\mathbf{I}\_{G}+o(\varepsilon) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d+(Gt−γ2​(Ht−Gt2))+ε​(1+γ​Gt)​(ℳ​Gt−ρ​Gt)−γ2​ε​(ℳ​Ht−2​ρ​Ht)\displaystyle=d+\left(G\_{t}-\frac{\gamma}{2}\left(H\_{t}-G\_{t}^{2}\right)\right)+\varepsilon(1+\gamma G\_{t})(\mathcal{M}G\_{t}-\rho G\_{t})-\frac{\gamma}{2}\varepsilon(\mathcal{M}H\_{t}-2\rho H\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝐈x−𝐈G−γ​Gt​𝐈G+γ2​𝐈H+o​(ε).\displaystyle\quad+\mathbf{I}\_{x}-\mathbf{I}\_{G}-\gamma G\_{t}\mathbf{I}\_{G}+\frac{\gamma}{2}\mathbf{I}\_{H}+o(\varepsilon). |  |

Note from the proof of Step 3 that G−γ2​(H−G2)=V~G-\frac{\gamma}{2}\left(H-G^{2}\right)=\widetilde{V}. Using the definition of 𝐈ϕ\mathbf{I}\_{\phi}, with ϕ=x,G,H\phi=x,G,H, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐈x−𝐈G−γ​Gt​𝐈G+γ2​𝐈H\displaystyle\mathbf{I}\_{x}-\mathbf{I}\_{G}-\gamma G\_{t}\mathbf{I}\_{G}+\frac{\gamma}{2}\mathbf{I}\_{H} | =∫t+t+ε(1−∂xG−γ​G​∂xG+γ2​∂xH)|(Xs,s)​d​δ​(s)+o​(ε)\displaystyle=\int\_{t^{+}}^{t+\varepsilon}\left(1-\partial\_{x}G-\gamma G\partial\_{x}G+\frac{\gamma}{2}\partial\_{x}H\right)\Big|\_{(X\_{s},s)}\,\mathrm{d}\delta(s)+o(\varepsilon) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫t+t+ε(1−∂xV~​(Xs,s))​dδ​(s)+o​(ε)≤o​(ε),\displaystyle=\int\_{t^{+}}^{t+\varepsilon}\left(1-\partial\_{x}\widetilde{V}(X\_{s},s)\right)\mathrm{d}\delta(s)+o(\varepsilon)\leq o(\varepsilon), |  | (3.18) |

in which the last inequality follows from 1−∂xV~≤01-\partial\_{x}\widetilde{V}\leq 0 in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).
Therefore, by using the above estimate and the identity of V~\widetilde{V}, we further reduce J​(x,t;Dε)J(x,t;D^{\varepsilon}) to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J​(x,t;Dε)\displaystyle J(x,t;D^{\varepsilon}) | =d+V~t+ε​(ℳ​V~t−γ2​ℳ​Gt2+γ​Gt​ℳ​Gt−ρ​Gt+γ​ρ​(Ht−Gt2))+o​(ε)\displaystyle=d+\widetilde{V}\_{t}+\varepsilon\left(\mathcal{M}\widetilde{V}\_{t}-\frac{\gamma}{2}\mathcal{M}G^{2}\_{t}+\gamma G\_{t}\mathcal{M}G\_{t}-\rho G\_{t}+\gamma\rho\big(H\_{t}-G^{2}\_{t}\big)\right)+o(\varepsilon) |  | (3.19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤d+V~t+o​(ε)\displaystyle\leq d+\widetilde{V}\_{t}+o(\varepsilon) |  | (3.20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =V~​(x,t)+(d−∫x−dx∂xV~​(z,t)​d​z)+o​(ε)\displaystyle=\widetilde{V}(x,t)+\left(d-\int\_{x-d}^{x}\,\partial\_{x}\widetilde{V}(z,t)\,\mathrm{d}z\right)+o(\varepsilon) |  | (3.21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤V~​(x,t)+o​(ε)=J​(x,t;D∗)+o​(ε),\displaystyle\leq\widetilde{V}(x,t)+o(\varepsilon)=J(x,t;D^{\*})+o(\varepsilon), |  | (3.22) |

in which V~t:=V~​(x−d,t)\widetilde{V}\_{t}:=\widetilde{V}(x-d,t), and the two inequalities follow from ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

Finally, we conclude that the desired limit result in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) holds.
∎

###### Remark 3.1.

Because both this paper and Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] seek equilibrium strategies for MV dividend problems from a game-theoretic perspective, their verification lemmas and proofs share certain similarities. However, there are also major differences, which we now describe. In Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), the feasible region is partitioned into the pay region and no-transaction region, and all related functions (V(V, GG, and H)H) are characterized separately in these two regions; the value function VV satisfies an HJB-variational inequality equation in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), which appears because of the singular-control framework. By comparison, each corresponding function in Theorem 2.32.3 of Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] is characterized by one second-order PDE over the entire region, and the value function VV therein satisfies a standard HJB equation. Regarding the equilibrium strategies, D∗D^{\*} in this paper is obtained as a solution of the associated Skorokhold reflection problem in ([3.7](https://arxiv.org/html/2511.08433v1#S3.E7 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), but D∗D^{\*} in Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] is the maximizer of the HJB equation of VV. The difference in their proofs lies on the technical side and mainly originates from their differences concerning the definition of perturbed strategies ((see Remark [2.1](https://arxiv.org/html/2511.08433v1#S2.Thmremark1 "Remark 2.1. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"))). In particular, it takes a delicate and involved analysis to study the performance of the perturbed strategy DεD^{\varepsilon} here in Step 44, which eventually yields the desired first-order inequality in ([2.5](https://arxiv.org/html/2511.08433v1#S2.E5 "In Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). ∎

## 4 Equilibrium dividend strategies

In this section, we apply the verification theorem (Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) to derive the equilibrium dividend strategy D∗D^{\*} in (semi)closed form for large γ\gamma (risk aversion) and small γ\gamma.

To begin, we review the special case of γ=0\gamma=0; note that the objective JJ in ([2.3](https://arxiv.org/html/2511.08433v1#S2.E3 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) becomes 𝔼x,t​(Yt)\mathbb{E}\_{x,t}(Y\_{t}), and the corresponding optimal dividend problem is time-consistent and has been solved in the literature. For instance, Theorem 2.2 and Lemma 2.3 in Taksar [[33](https://arxiv.org/html/2511.08433v1#bib.bib33)] show that the optimal strategy is a barrier strategy with a strictly positive barrier x~\tilde{x} (because a>0a>0), and the value function is concave and obtained explicitly in a two-piece form separated by the barrier x~\tilde{x}.
We hypothesize that for small positive γ\gamma, a similar result holds. However, for γ\gamma large enough, the penalty on the variation of dividend payments should “force” the manager to pay the entire surplus and declare bankruptcy (yielding a zero variance). We formally verify this latter hypothesis in the next theorem.

###### Theorem 4.1.

If the following condition holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ≥2​ab2,\gamma\geq\dfrac{2a}{b^{2}}, |  | (4.1) |

then an equilibrium dividend strategy is to pay out all of surplus as dividends immediately ((that is, Dt∗=Xt−=xD\_{t}^{\*}=X\_{t^{-}}=x and τ∗=t)\tau^{\*}=t), and we have V​(x,t)=G​(x,t)≡xV(x,t)=G(x,t)\equiv x and H​(x,t)≡x2H(x,t)\equiv x^{2} for all x≥0x\geq 0.

###### Proof.

Suppose inequality ([4.1](https://arxiv.org/html/2511.08433v1#S4.E1 "In Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) holds; we consider the strategy of paying all dividends immediately (and thereby ruining immediately). This strategy is clearly admissible by Definition [2.1](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), and it implies that the pay region is P=ℝ+2\mathrm{P}=\mathbb{R}\_{+}^{2} and Yt=xY\_{t}=x. As such, it follows from ([3.8](https://arxiv.org/html/2511.08433v1#S3.E8 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) that G​(x,t)≡xG(x,t)\equiv x and H​(x,t)≡x2H(x,t)\equiv x^{2}, and they satisfy the related HJB equations in ([3.4](https://arxiv.org/html/2511.08433v1#S3.E4 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). Given GG and HH, we obtain the (candidate) value function by V​(x,t)=G​(x,t)−γ2​(H​(x,t)−G2​(x,t))≡xV(x,t)=G(x,t)-\frac{\gamma}{2}(H(x,t)-G^{2}(x,t))\equiv x, which implies that 1−∂xV≤01-\partial\_{x}V\leq 0 holds with equality, and the boundary condition in ([3.6](https://arxiv.org/html/2511.08433v1#S3.E6 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is satisfied. It remains to show that the first variational inequality in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is true for all x∈ℝ+x\in\mathbb{R}\_{+}. To that end, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​V−γ2​ℳ​G2+γ​G​ℳ​G−ρ​G+γ​ρ​(H−G2)=a−γ2​b2−ρ​x,\displaystyle\mathcal{M}V-\dfrac{\gamma}{2}\,\mathcal{M}G^{2}+\gamma G\mathcal{M}G-\rho G+\gamma\rho\big(H-G^{2}\big)=a-\dfrac{\gamma}{2}\,b^{2}-\rho x, |  | (4.2) |

which is non-positive for all x≥0x\geq 0 when ([4.1](https://arxiv.org/html/2511.08433v1#S4.E1 "In Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) holds. Thus, VV, GG, and HH satisfy the conditions of Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), and paying out all of surplus as dividends is an equilibrium strategy.
∎

We next prove a non-trivial result for small risk aversion γ\gamma and confirm the earlier hypothesis that a barrier strategy is an equilibrium dividend strategy. For convenience, define

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | r1\displaystyle r\_{1} | =1b2​[−a+a2+2​ρ​b2]>0,\displaystyle=\dfrac{1}{b^{2}}\left[-a+\sqrt{a^{2}+2\rho b^{2}}\right]>0, | r2\displaystyle r\_{2} | =1b2​[−a−a2+2​ρ​b2]<0,\displaystyle=\dfrac{1}{b^{2}}\left[-a-\sqrt{a^{2}+2\rho b^{2}}\right]<0, |  | (4.3) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | r3\displaystyle r\_{3} | =1b2​[−a+a2+4​ρ​b2]>0,\displaystyle=\dfrac{1}{b^{2}}\left[-a+\sqrt{a^{2}+4\rho b^{2}}\right]>0, | r4\displaystyle r\_{4} | =1b2​[−a−a2+4​ρ​b2]<0.\displaystyle=\dfrac{1}{b^{2}}\left[-a-\sqrt{a^{2}+4\rho b^{2}}\right]<0. |  | (4.4) |

###### Theorem 4.2.

There exists an ε∈(0,2​ab2)\varepsilon\in(0,\frac{2a}{b^{2}}) such that for all γ∈(0,ε)\gamma\in(0,\varepsilon), equation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =r12​er1​x−r22​er2​xr1​er1​x−r2​er2​x+γ{1+er1​x−er2​xr1​er1​x−r2​er2​x(r12​er1​x−r22​er2​xr1​er1​x−r2​er2​x−r32​er3​x−r42​er4​xr3​er3​x−r4​er4​x)}=:f(x,γ)\displaystyle=\dfrac{r\_{1}^{2}\mathrm{e}^{r\_{1}x}-r\_{2}^{2}\mathrm{e}^{r\_{2}x}}{r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x}}+\gamma\left\{1+\dfrac{\mathrm{e}^{r\_{1}x}-\mathrm{e}^{r\_{2}x}}{r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x}}\left(\dfrac{r\_{1}^{2}\mathrm{e}^{r\_{1}x}-r\_{2}^{2}\mathrm{e}^{r\_{2}x}}{r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x}}-\dfrac{r\_{3}^{2}\mathrm{e}^{r\_{3}x}-r\_{4}^{2}\mathrm{e}^{r\_{4}x}}{r\_{3}\mathrm{e}^{r\_{3}x}-r\_{4}\mathrm{e}^{r\_{4}x}}\right)\right\}=:f(x,\gamma)\qquad |  | (4.5) |

admits a unique positive solution, denoted by x~\tilde{x}. If (1)(1) γ<ε\gamma<\varepsilon, and (2)(2) VV in ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is strictly concave over [0,x~)[0,\tilde{x}), then a
barrier strategy, with constant barrier x~\tilde{x}, is an equilibrium strategy D∗D^{\*}, with P=[x~,∞)×ℝ+\mathrm{P}=[\tilde{x},\infty)\times\mathbb{R}\_{+} and NT=[0,x~)×ℝ+\mathrm{NT}=[0,\tilde{x})\times\mathbb{R}\_{+}. Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(x)=𝔼x​(Y0∗)={C1​(er1​x−er2​x),x<x~,C1​(er1​x~−er2​x~)+(x−x~),x≥x~,\displaystyle G(x)=\mathbb{E}\_{x}(Y\_{0}^{\*})=\begin{cases}C\_{1}\big(\mathrm{e}^{r\_{1}x}-\mathrm{e}^{r\_{2}x}\big),&\quad x<\tilde{x},\\ C\_{1}\big(\mathrm{e}^{r\_{1}\tilde{x}}-\mathrm{e}^{r\_{2}\tilde{x}}\big)+(x-\tilde{x}),&\quad x\geq\tilde{x},\end{cases} |  | (4.6) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(x)=𝔼x​[(Y0∗)2]={C3​(er3​x−er4​x),x<x~,C3​(er3​x~−er4​x~)+2​C1​(er1​x~−er2​x~)​(x−x~)+(x−x~)2,x≥x~,\displaystyle H(x)=\mathbb{E}\_{x}\big[(Y^{\*}\_{0})^{2}\big]=\begin{cases}C\_{3}\big(\mathrm{e}^{r\_{3}x}-\mathrm{e}^{r\_{4}x}\big),&\quad x<\tilde{x},\\ C\_{3}\big(\mathrm{e}^{r\_{3}\tilde{x}}-\mathrm{e}^{r\_{4}\tilde{x}}\big)+2C\_{1}\big(\mathrm{e}^{r\_{1}\tilde{x}}-\mathrm{e}^{r\_{2}\tilde{x}}\big)(x-\tilde{x})+(x-\tilde{x})^{2},&\quad x\geq\tilde{x},\end{cases} |  | (4.7) |

in which

|  |  |  |  |
| --- | --- | --- | --- |
|  | C1=1r1​er1​x~−r2​er2​x~>0 and C3=2​(er1​x~−er2​x~)(r1​er1​x~−r2​er2​x~)​(r3​er3​x~−r4​er4​x~)>0,\displaystyle C\_{1}=\dfrac{1}{r\_{1}\mathrm{e}^{r\_{1}\tilde{x}}-r\_{2}\mathrm{e}^{r\_{2}\tilde{x}}}>0\quad\text{ and }\quad C\_{3}=\dfrac{2\big(\mathrm{e}^{r\_{1}\tilde{x}}-\mathrm{e}^{r\_{2}\tilde{x}}\big)}{\left(r\_{1}\mathrm{e}^{r\_{1}\tilde{x}}-r\_{2}\mathrm{e}^{r\_{2}\tilde{x}}\right)\left(r\_{3}\mathrm{e}^{r\_{3}\tilde{x}}-r\_{4}\mathrm{e}^{r\_{4}\tilde{x}}\right)}>0, |  | (4.8) |

and the corresponding value function equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)=G​(x)−γ2​(H​(x)−G2​(x)).\displaystyle V(x)=G(x)-\frac{\gamma}{2}\left(H(x)-G^{2}(x)\right). |  | (4.9) |

###### Proof.

Because the problem is time-homogeneous, we expect the value function VV to be time-independent, along with GG and HH. For this reason, we set time equal to 0 and suppress the time argument in the analysis; also, we write ϕ′\phi^{\prime} and ϕ′′\phi^{\prime\prime} to denote the first and second derivative (with respect to xx) for ϕ=V,G\phi=V,G, or HH.
We hypothesize that a time-independent barrier strategy, with a constant barrier x~>0\tilde{x}>0, is an equilibrium dividend strategy D∗D^{\*} (in the sense of Definition [2.2](https://arxiv.org/html/2511.08433v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). Specifically, this strategy dictates the manager of the company to pay (x−x~)​𝟙x≥x~(x-\tilde{x})\mathds{1}\_{x\geq\tilde{x}} in dividends at time 0 (with initial surplus X0−=x≥0X\_{0^{-}}=x\geq 0) and thereafter pay dividends in order to keep the surplus Xt∗∈[0,x~]X\_{t}^{\*}\in[0,\tilde{x}] for all t>0t>0. Since the barrier strategy D∗D^{\*} is time-independent, we write the pay region as P=[x~,∞)\mathrm{P}=[\tilde{x},\infty) and the no-transaction region as NT=[0,x~)\mathrm{NT}=[0,\tilde{x}) associated with D∗D^{\*} in the proof.

With the above hypothesis, we proceed to solve for GG and HH based on whether x∈NTx\in\mathrm{NT} or x∈Px\in\mathrm{P}.
First, assume x∈NTx\in\mathrm{NT}, that is, x<x~x<\tilde{x}. In this case, by ([3.4](https://arxiv.org/html/2511.08433v1#S3.E4 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), GG solves the boundary-value problem,
−ρ​G​(x)+a​G′​(x)+12​b2​G′′​(x)=0-\rho G(x)+aG^{\prime}(x)+\frac{1}{2}\,b^{2}G^{\prime\prime}(x)=0, with G​(0)=0G(0)=0,
whose solution equals the first expression in ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). Similarly, using ([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) for HH, we solve −2​ρ​H​(x)+a​H′​(x)+12​b2​H′′​(x)=0-2\rho H(x)+aH^{\prime}(x)+\frac{1}{2}\,b^{2}H^{\prime\prime}(x)=0, given H​(0)=0H(0)=0,
and obtain the first expression for HH in ([4.7](https://arxiv.org/html/2511.08433v1#S4.E7 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

Next, assume x∈Px\in\mathrm{P}, that is, x≥x~x\geq\tilde{x}. In this case, our ansatz strategy implies that the company immediately pays a lump-sum dividend of x−x~x-\tilde{x}. By the continuity of GG and using G′​(x)=1G^{\prime}(x)=1, we arrive at the second expression of GG in ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). Next, ([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) implies H′​(x)=2​G​(x)H^{\prime}(x)=2G(x), and using this result leads to the second expression of HH in ([4.7](https://arxiv.org/html/2511.08433v1#S4.E7 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

The two positive constants C1C\_{1} and C3C\_{3} in ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([4.7](https://arxiv.org/html/2511.08433v1#S4.E7 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) are yet to be determined. To determine them, we use the condition that G,H∈𝒞2​(ℝ+)G,H\in\mathcal{C}^{2}(\mathbb{R}\_{+}), except possibly at x=x~x=\tilde{x} where they must be 𝒞1\mathcal{C}^{1}. This motivates us to impose the “smooth pasting” condition: G′​(x~−)=G′​(x~+)G^{\prime}(\tilde{x}^{-})=G^{\prime}(\tilde{x}^{+}) and H′​(x~−)=H′​(x~+)H^{\prime}(\tilde{x}^{-})=H^{\prime}(\tilde{x}^{+}),
from which we obtain C1C\_{1} and C3C\_{3} as in ([4.8](https://arxiv.org/html/2511.08433v1#S4.E8 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

With GG and HH obtained in ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([4.7](https://arxiv.org/html/2511.08433v1#S4.E7 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), respectively, we immediately obtain the candidate value function VV by ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")); note that the barrier x~>0\tilde{x}>0 (appearing in ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), ([4.7](https://arxiv.org/html/2511.08433v1#S4.E7 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), and ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"))) is unknown from the ansatz.
To determine x~\tilde{x}, we impose the condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | V′′​(x~−):=limx↑x~V′′​(x)=0.\displaystyle V^{\prime\prime}(\tilde{x}^{-}):=\lim\_{x\uparrow\tilde{x}}V^{\prime\prime}(x)=0. |  | (4.10) |

By using ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([4.7](https://arxiv.org/html/2511.08433v1#S4.E7 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), we verify that V′′​(x~+):=limx↓x~V′′​(x)=0V^{\prime\prime}(\tilde{x}^{+}):=\lim\_{x\downarrow\tilde{x}}V^{\prime\prime}(x)=0 holds automatically. Therefore, with ([4.10](https://arxiv.org/html/2511.08433v1#S4.E10 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), we have V′′​(x~)=0V^{\prime\prime}(\tilde{x})=0, and it further implies V∈𝒞2​(ℝ+)V\in\mathcal{C}^{2}(\mathbb{R}\_{+}) because the continuity of VV and V′V^{\prime} follows from that of GG, G′G^{\prime}, HH, and H′H^{\prime}.
To obtain a finer condition for ([4.10](https://arxiv.org/html/2511.08433v1#S4.E10 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), we compute: for all x<x~x<\tilde{x},

|  |  |  |  |
| --- | --- | --- | --- |
|  | V′′​(x)\displaystyle V^{\prime\prime}(x) | =r1​er1​x−r2​er2​xr1​er1​x~−r2​er2​x~⋅{r12​er1​x−r22​er2​xr1​er1​x−r2​er2​x+γ[r1​er1​x−r2​er2​xr1​er1​x~−r2​er2​x~+(er1​x−er2​x)​(r12​er1​x−r22​er2​x)(r1​er1​x~−r2​er2​x~)​(r1​er1​x−r2​er2​x)\displaystyle=\dfrac{r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x}}{r\_{1}\mathrm{e}^{r\_{1}\tilde{x}}-r\_{2}\mathrm{e}^{r\_{2}\tilde{x}}}\cdot\Bigg\{\dfrac{r\_{1}^{2}\mathrm{e}^{r\_{1}x}-r\_{2}^{2}\mathrm{e}^{r\_{2}x}}{r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x}}+\gamma\bigg[\dfrac{r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x}}{r\_{1}\mathrm{e}^{r\_{1}\tilde{x}}-r\_{2}\mathrm{e}^{r\_{2}\tilde{x}}}+\dfrac{(\mathrm{e}^{r\_{1}x}-\mathrm{e}^{r\_{2}x})(r\_{1}^{2}\mathrm{e}^{r\_{1}x}-r\_{2}^{2}\mathrm{e}^{r\_{2}x})}{(r\_{1}\mathrm{e}^{r\_{1}\tilde{x}}-r\_{2}\mathrm{e}^{r\_{2}\tilde{x}})(r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x})} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(er1​x~−er2​x~)​(r32​er3​x−r42​er4​x)(r3​er3​x~−r4​er3​x~)​(r1​er1​x−r2​er2​x)]}=:r1​er1​x−r2​er2​xr1​er1​x~−r2​er2​x~⋅g(x,x~),\displaystyle\qquad\qquad-\dfrac{(\mathrm{e}^{r\_{1}\tilde{x}}-\mathrm{e}^{r\_{2}\tilde{x}})(r\_{3}^{2}\mathrm{e}^{r\_{3}x}-r\_{4}^{2}\mathrm{e}^{r\_{4}x})}{(r\_{3}\mathrm{e}^{r\_{3}\tilde{x}}-r\_{4}\mathrm{e}^{r\_{3}\tilde{x}})(r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x})}\bigg]\Bigg\}=:\dfrac{r\_{1}\mathrm{e}^{r\_{1}x}-r\_{2}\mathrm{e}^{r\_{2}x}}{r\_{1}\mathrm{e}^{r\_{1}\tilde{x}}-r\_{2}\mathrm{e}^{r\_{2}\tilde{x}}}\cdot g(x,\tilde{x}), |  | (4.11) |

which shows that V′′​(x~−)=0V^{\prime\prime}(\tilde{x}^{-})=0 in ([4.10](https://arxiv.org/html/2511.08433v1#S4.E10 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is equivalent to f​(x~,γ)=0f(\tilde{x},\gamma)=0 in ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")).

To study the solvability of ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), we treat the right side of ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) as a function of xx and γ\gamma and denote it by f​(x,γ)f(x,\gamma). For every fixed γ\gamma satisfying γ<2​a/b2\gamma<2a/b^{2}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(0,γ)=γ−2​ab2<0 and limx→∞f​(x,γ)=r1+γ​(2−r3r1)>0,\displaystyle f(0,\gamma)=\gamma-\dfrac{2a}{b^{2}}<0\quad\text{ and }\quad\lim\_{x\to\infty}f(x,\gamma)=r\_{1}+\gamma\left(2-\dfrac{r\_{3}}{r\_{1}}\right)>0, |  | (4.12) |

in which the second inequality follows from 2​r1>r32r\_{1}>r\_{3} by their definitions in ([4.3](https://arxiv.org/html/2511.08433v1#S4.E3 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([4.4](https://arxiv.org/html/2511.08433v1#S4.E4 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). As such, combining with the fact that f​(⋅,γ)f(\cdot,\gamma) is continuous over ℝ+\mathbb{R}\_{+}, f​(x,γ)=0f(x,\gamma)=0 admits at least one positive solution xγx\_{\gamma} for all γ∈(0,2​a/b2)\gamma\in(0,2a/b^{2}). To obtain the uniqueness result, we first set γ=0\gamma=0 and verify that f​(x,0)=0f(x,0)=0 has a unique positive solution, x0x\_{0} (by using ([4.12](https://arxiv.org/html/2511.08433v1#S4.E12 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and verifying ∂xf​(x,0)>0\partial\_{x}f(x,0)>0). Moreover, by a tedious calculation, we deduce ∂xf​(x,γ)|(x0,0)∝−r1​r2​(r1−r2)2​e(r1+r2)​x0>0\partial\_{x}f(x,\gamma)|\_{(x\_{0},0)}\propto-r\_{1}r\_{2}(r\_{1}-r\_{2})^{2}\,\mathrm{e}^{(r\_{1}+r\_{2})x\_{0}}>0. Therefore, by the implicit function theorem, there exists a small ε∈(0,2​ab2)\varepsilon\in(0,\frac{2a}{b^{2}}) such that ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) has a unique positive solution x~:=xγ\tilde{x}:=x\_{\gamma} (that is, f​(xγ,γ)=0f(x\_{\gamma},\gamma)=0) for all γ<ε\gamma<\varepsilon. (Recall that we assumed γ<2​ab2\gamma<\frac{2a}{b^{2}} to obtain f​(0,γ)<0f(0,\gamma)<0 in ([4.12](https://arxiv.org/html/2511.08433v1#S4.E12 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")); therefore, we impose an upper bound of 2​ab2\frac{2a}{b^{2}} on ε\varepsilon.)

By construction, GG in ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and HH in ([4.7](https://arxiv.org/html/2511.08433v1#S4.E7 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) satisfy all the conditions of Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), and the candidate barrier strategy is admissible and solves the Skorokhod reflection problem ([3.7](https://arxiv.org/html/2511.08433v1#S3.E7 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) with X0−=xX\_{0^{-}}=x and NT=[0,x~)×ℝ+\mathrm{NT}=[0,\tilde{x})\times\mathbb{R}\_{+} (see, for instance, Lemma 4.1 in Wang and Zou [[34](https://arxiv.org/html/2511.08433v1#bib.bib34)]). The remaining task is to verify that VV satisfies the HJB variational equation in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and that the partition in ([3.2](https://arxiv.org/html/2511.08433v1#S3.E2 "In Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is consistent with VV.
Because 1−V′​(x)=01-V^{\prime}(x)=0 on P\mathrm{P} by ([3.4](https://arxiv.org/html/2511.08433v1#S3.E4 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) and ([3.5](https://arxiv.org/html/2511.08433v1#S3.E5 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), the strict concavity of VV in Condition (3) implies that 1−V′​(x)<01-V^{\prime}(x)<0 for all x∈NTx\in\mathrm{NT}.

Finally, by applying Theorem [3.1](https://arxiv.org/html/2511.08433v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), all the results in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") follow as desired.
∎

###### Remark 4.1.

The first condition in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") explicitly requires small γ\gamma.
We claim that the second condition ((that is, VV in ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) is strictly concave over [0,x~))[0,\tilde{x})) also requires small γ\gamma (γ≤2​ab2(\gamma\leq\frac{2a}{b^{2}}, to be precise)). To prove our claim, we argue by contradiction and choose a γ>2​ab2\gamma>\frac{2a}{b^{2}}; suppose γ\gamma is such that f​(x,γ)=0f(x,\gamma)=0 has a unique solution x~\tilde{x}.
For such a γ\gamma, we have f​(0,γ)>0f(0,\gamma)>0 and limx→∞f​(x,γ)>0\lim\_{x\to\infty}f(x,\gamma)>0. From the continuity of f​(⋅,γ)f(\cdot,\gamma) and uniqueness of x~\tilde{x}, we deduce f​(x,γ)>0f(x,\gamma)>0 for all x≠x~x\neq\tilde{x}. This, along with ([4.11](https://arxiv.org/html/2511.08433v1#S4.E11 "In 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), implies that g​(x,x~)>0g(x,\tilde{x})>0 for all x≠x~x\neq\tilde{x}, which in turn yields V′′​(x)>0V^{\prime\prime}(x)>0 over [0,x~)[0,\tilde{x}), contradicting the strictly concavity of VV.
Numerical analysis in the next section further suggests that there exists an upper bound γ¯<ε≤2​ab2\bar{\gamma}<\varepsilon\leq\frac{2a}{b^{2}} such that both conditions in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") hold. As a consequence, when γ>2​ab2\gamma>\frac{2a}{b^{2}}, Theorem [4.1](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") shows that paying the entire surplus immediately is an equilibrium strategy; when γ≤γ¯\gamma\leq\bar{\gamma}, Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") shows that a barrier strategy with a constant barrier x~\tilde{x} is an equilibrium strategy. However, for intermediate level risk aversion γ∈(γ¯,2​ab2)\gamma\in(\bar{\gamma},\frac{2a}{b^{2}}), finding equilibrium strategies remains an open question. ∎

###### Remark 4.2.

In this remark, we first compare our results in Theorems [4.1](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") and [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") with those in Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)]. In their paper, the model must satisfy a key inequality ((equation (3.3))(3.3)) first, and, then, when risk aversion is small enough, a barrier strategy is an equilibrium strategy ((see Theorem 3.2 in that paper)); if the inequality fails, Theorem 3.33.3 therein shows that paying dividends at the maximum rate is an equilibrium strategy, but again for *small* risk aversion. By comparison, paying out all surplus in Theorem [4.1](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") is an equilibrium strategy for *large*, not small, risk aversion; moreover, a similar inequality is *not* needed for either theorem here. Recall that Condition (2)(2) in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") helps verify 1−V′​(x)<01-V^{\prime}(x)<0 for all x∈NTx\in\mathrm{NT}, which arises from the variational inequality in ([3.3](https://arxiv.org/html/2511.08433v1#S3.E3 "In item 3. ‣ Theorem 3.1. ‣ 3 Verification theorem ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), but a similar condition is *not* needed in Theorem 3.23.2 of Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] because they adopt the classical control framework and the value function only needs to satisfy an ((extended)) HJB equation ((see equation (2.3)(2.3) in that paper)).

Under the same diffusion model as ours in ([2.1](https://arxiv.org/html/2511.08433v1#S2.E1 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), Grandits et al. [[23](https://arxiv.org/html/2511.08433v1#bib.bib23)] investigate the optimal dividend strategy that maximizes the expected exponential utility of total dividends paid up to the ruin time, maxD⁡𝔼​[U​(∫tτe−ρ​s​dDs)]\max\_{D}\mathbb{E}[U(\int\_{t}^{\tau}\mathrm{e}^{-\rho s}\mathrm{d}D\_{s})], in which U​(x)=(1−e−γ​x)/γU(x)=(1-\mathrm{e}^{-\gamma x})/\gamma. They show that when γ≥2​ab2\gamma\geq\frac{2a}{b^{2}}, the optimal strategy is to pay out the entire surplus immediately, which aligns with our finding in Theorem [4.1](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"). When γ<2​ab2\gamma<\frac{2a}{b^{2}}, and assuming the existence of a positive solution b​(t)b(t) to a certain integral equation ((equation (25))(25)), the barrier strategy with time-dependent barrier b​(t)b(t) is an optimal strategy, which resembles our result in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"). The reason that their barrier is time-dependent is that future dividends are discounted to time 0 in their time-tt value function ((equation 12)12); the same setup is also used in Eisenberg and Krühner [[19](https://arxiv.org/html/2511.08433v1#bib.bib19)].
Gerber and Shiu [[21](https://arxiv.org/html/2511.08433v1#bib.bib21)] provide a detailed study on the distribution of Y0=∫0τe−ρ​s​dDsY\_{0}=\int\_{0}^{\tau}\,\mathrm{e}^{-\rho s}\,\mathrm{d}D\_{s} under barrier strategies, but they do not attempt to solve for the optimal barrier. ∎

## 5 Numerical examples

When risk aversion is large enough (γ≥2​ab2\gamma\geq\frac{2a}{b^{2}}), Theorem [4.1](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") shows that paying all of surplus immediately (Dt∗=xD^{\*}\_{t}=x) is an equilibrium strategy, and the corresponding value function is V​(x)=xV(x)=x. However, for small γ\gamma, the results in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") are less explicit; thus, the first objective of this section is to offer more insights via a detailed numerical analysis. To that end, we set a=1a=1 (surplus drift), b=0.25b=0.25 (surplus volatility), and ρ=0.2\rho=0.2 (discount rate). When γ=0\gamma=0, the unique barrier x~\tilde{x} is given by (see equation (2.25) in Taksar [[33](https://arxiv.org/html/2511.08433v1#bib.bib33)])

|  |  |  |
| --- | --- | --- |
|  | x~=b2a2+2​ρ​b2​ln⁡a2+2​ρ​b2+aa2+2​ρ​b2−a(=0.3141),\displaystyle\tilde{x}=\frac{b^{2}}{\sqrt{a^{2}+2\rho b^{2}}}\,\ln\frac{\sqrt{a^{2}+2\rho b^{2}}+a}{\sqrt{a^{2}+2\rho b^{2}}-a}\;(=0.3141), |  |

and the value function VV equals GG in ([4.6](https://arxiv.org/html/2511.08433v1#S4.E6 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) with the above x~\tilde{x}. In this case, VV is strictly concave over the NT region and linear over the Pay region.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1: f​(x,0.15)f(x,0.15) in ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) (left) and V′′​(x)V^{\prime\prime}(x) defined via ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) (right) when γ=0.15\gamma=0.15

For the given parameter values, our numerical algorithm finds a unique positive root x~\tilde{x} to ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) for all γ<32(=2​ab2)\gamma<32\,(=\frac{2a}{b^{2}}). However, upon substituting x~\tilde{x} into the expression of VV in ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), we find that VV is strictly concave over [0,x~)[0,\tilde{x}) only for γ≤0.1397\gamma\leq 0.1397. (Strict concavity is required by Condition (2) in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion").) For instance, if we set γ=0.15\gamma=0.15, then the unique root is x~=0.3244\tilde{x}=0.3244, but Figure [1](https://arxiv.org/html/2511.08433v1#S5.F1 "Figure 1 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") clearly shows that V′′​(x)>0V^{\prime\prime}(x)>0 when xx is near 0. On the other hand, consider γ=40>2​ab2\gamma=40>\frac{2a}{b^{2}}; Figure [2](https://arxiv.org/html/2511.08433v1#S5.F2 "Figure 2 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") shows that f​(x,40)=0f(x,40)=0 has two positive roots, x~1=0.0624\tilde{x}\_{1}=0.0624 and x~2=0.4222\tilde{x}\_{2}=0.4222, and plots their corresponding VVs defined by ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) for x~=x~1,x~2\tilde{x}=\tilde{x}\_{1},\,\tilde{x}\_{2}, neither of which is concave over [0,x~)[0,\tilde{x}). To echo our earlier comment from Remark [4.1](https://arxiv.org/html/2511.08433v1#S4.Thmremark1 "Remark 4.1. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), paying out full surplus is an equilibrium strategy for all γ≥2​ab2=32\gamma\geq\frac{2a}{b^{2}}=32; a barrier strategy with barrier x~\tilde{x} is an equilibrium strategy for all γ≤γ¯=0.1397\gamma\leq\bar{\gamma}=0.1397. But, for intermediate values γ∈(0.1397,32)\gamma\in(0.1397,32), finding equilibrium strategies remains an open question.

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 2: f​(x,40)f(x,40) in ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) (left) and the corresponding VVs in ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) when γ=40\gamma=40

Given the above results, we now consider small γ≤0.1397\gamma\leq 0.1397 and plot the unique positive root x~:=x~​(γ)\tilde{x}:=\tilde{x}(\gamma) as a function of γ\gamma over this range. The left panel of Figure [3](https://arxiv.org/html/2511.08433v1#S5.F3 "Figure 3 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") shows that x~\tilde{x} is an increasing function of γ\gamma, and we explain this finding as follows: when γ\gamma increases, the penalty on dividend variability increases, but since γ\gamma remains small, barrier strategies are still equilibrium strategies; the combined effect, then, drives the manager to set a higher barrier for paying dividends to reduce the variance. The right panel of Figure [3](https://arxiv.org/html/2511.08433v1#S5.F3 "Figure 3 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") verifies that f​(⋅,γ=0.13)=0f(\cdot,\gamma=0.13)=0 has a unique root at x~=0.3232\tilde{x}=0.3232 when γ=0.13\gamma=0.13 (note that f​(⋅,γ)f(\cdot,\gamma) is strictly increasing).

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 3: The barrier x~\tilde{x} as a function of γ\gamma (left) and f​(x,0.13)f(x,0.13) in ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) when γ=0.13\gamma=0.13 (right)

Next, we compute the equilibrium value function VV in ([4.9](https://arxiv.org/html/2511.08433v1#S4.E9 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")) for three different risk aversion levels, γ=0.01,0.06\gamma=0.01,0.06, and 0.130.13, and plot their graphs as a function of xx in Figure [4](https://arxiv.org/html/2511.08433v1#S5.F4 "Figure 4 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"). The left panel verifies the strict concavity of VV over [0,x~)[0,\tilde{x}), while the right panel shows that VV, viewed as a function of γ\gamma, is decreasing. We expect VV to decrease with respect to γ\gamma because of the form of the objective function JJ in ([2.3](https://arxiv.org/html/2511.08433v1#S2.E3 "In 2 Model ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), and it is satisfying to see our intuition born out in Figure [4](https://arxiv.org/html/2511.08433v1#S5.F4 "Figure 4 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion").

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 4: The value function V​(x)V(x) (left) and its zoom-in for x∈(0.1,0.4)x\in(0.1,0.4) (right)

Recall that the equilibrium consumption strategy in Kronborg and Steffensen [[28](https://arxiv.org/html/2511.08433v1#bib.bib28)] is of a bang-bang type, depending solely on the order between the risk-free rate and the discount rate ρ\rho, and it is independent of the state process. This motivates us to study the impact of ρ\rho on our results. In particular, we study how ρ\rho affects the upper bound γ¯\bar{\gamma} (Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") requires γ≤γ¯\gamma\leq\bar{\gamma}) and the barrier x~:=x~​(ρ)\tilde{x}:=\tilde{x}(\rho) for a given small risk aversion γ=0.1396\gamma=0.1396. We first observe a technical result that the upper bound on risk aversion, γ¯\bar{\gamma}, in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") increases with respect to ρ\rho. The right panel shows that the (unique) barrier x~\tilde{x} decreases as ρ\rho increases, indicating that when the discount rate is higher (that is, the manager is less patient), larger dividends are paid out earlier.

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 5: Impact of the discount rate ρ\rho on the maximum allowed risk aversion γ¯\bar{\gamma} (left) and the barrier x~\tilde{x} under γ=0.1396\gamma=0.1396 (right)

We proceed to study how the model parameters aa and bb in the diffusion surplus influence the barrier x~\tilde{x} given by ([4.5](https://arxiv.org/html/2511.08433v1#S4.E5 "In Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")). Again, we focus on the cases of small risk aversion γ\gamma in which Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") applies, and note that the admissible range of γ\gamma is implicitly determined by the model parameters. Here, we present results for γ=0.11\gamma=0.11 in Figure [6](https://arxiv.org/html/2511.08433v1#S5.F6 "Figure 6 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), under which all conditions of Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") are satisfied over the range of aa and bb considered. Together with Figure [3](https://arxiv.org/html/2511.08433v1#S5.F3 "Figure 3 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") (left panel) and Figure [5](https://arxiv.org/html/2511.08433v1#S5.F5 "Figure 5 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") (left panel), these results indicate that the barrier x~\tilde{x} varies continuously with respect to γ\gamma, ρ\rho, aa and bb, as long as the assumptions of Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") hold.

![Refer to caption](x11.png)

![Refer to caption](x12.png)

Figure 6: Impact of the drift aa (left) and volatility bb (right) on the barrier x~\tilde{x} when γ=0.11\gamma=0.11

Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] study a similar MV dividend problem under the classical control framework and seek an equilibrium dividend *rate* strategy, subject to a maximum payout rate d¯>0\bar{d}>0. For a fixed (feedback) dividend rate strategy 𝒹\mathpzc{d}, the cumulative dividend DtD\_{t} is given by

|  |  |  |
| --- | --- | --- |
|  | Dt=∫0t∧τ𝒹​(𝒳𝓈,𝓈)​d𝓈.\displaystyle D\_{t}=\int\_{0}^{t\wedge\tau}\mathpzc{d}(X\_{s},s)\mathrm{d}s. |  |

They show that, for sufficiently small risk aversion γ\gamma (along with conditions ensuring the uniqueness of a positive solution x¯\bar{x} to a nonlinear equation), a barrier strategy 𝒹∗​(𝓍)=𝒹¯​ 1𝓍>𝓍¯\mathpzc{d}^{\*}(x)=\bar{d}\,\mathds{1}\_{{x>\bar{x}}} is an equilibrium strategy; this result is parallel to ours in Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), in which x~\tilde{x} is the unique barrier. To examine the connections between two different frameworks (singular control versus classical control), we set the same parameters for aa, bb, and ρ\rho as above and compute the two barriers x~\tilde{x} and x¯\bar{x} (for the latter, we consider d¯∈[0,50]\bar{d}\in[0,50]). We plot their graphs when γ=0\gamma=0 (left panel) and γ=0.13\gamma=0.13 (right panel) in Figure [7](https://arxiv.org/html/2511.08433v1#S5.F7 "Figure 7 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"). We observe that, as the maximum dividend rate d¯\bar{d} increases, the corresponding barrier x¯\bar{x} in Cao et al. [[12](https://arxiv.org/html/2511.08433v1#bib.bib12)] converges to x~\tilde{x} of this paper. In fact, when γ=0\gamma=0, Jeanblanc-Picqué and Shiryaev [[27](https://arxiv.org/html/2511.08433v1#bib.bib27)] prove that as d¯→∞\bar{d}\to\infty, the *optimal* barrier of the bounded-rate problem converges to that of the singular control problem. Our numerical results suggest that this convergence holds for *equilibrium strategies* when γ\gamma is small.

![Refer to caption](x13.png)

![Refer to caption](x14.png)

Figure 7: The barriers for the classical control and singular control problems when γ=0\gamma=0 (left) and γ=0.13\gamma=0.13 (right)

## 6 Conclusions

In this paper, we studied a novel singular control, time-inconsistent dividend problem, and the objective is to optimize the MV criterion of the integral of all discounted dividends paid until ruin time, an endogenous stopping time.
We proved a new verification theorem that characterizes equilibrium dividend strategies and their corresponding value functions to this problem.
We, then, used the verification theorem to prove two results in which we obtain equilibrium dividend strategies (semi-)explicitly: one for large values of risk aversion γ\gamma (specifically, γ≥2​ab2\gamma\geq\frac{2a}{b^{2}}), and one for small values of γ\gamma (namely, γ<ε≤2​ab2\gamma<\varepsilon\leq\frac{2a}{b^{2}}, subject to Condition (2) of Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), in which ε\varepsilon depends upon the parameters of the model). Numerical experiments show that the maximum γ\gamma satisfying both conditions of Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), denoted by γ¯\bar{\gamma}, is strictly less than 2​ab2\frac{2a}{b^{2}}. Thus, finding equilibrium dividend strategies when γ¯<γ<2​ab2\bar{\gamma}<\gamma<\frac{2a}{b^{2}} remains an open question.

For future work, one direction is to allow investment or capital injection strategies, in addition to dividend control, in the model (see Albrecher and Thonhauser [[1](https://arxiv.org/html/2511.08433v1#bib.bib1)]). Recall that we study dividend control problems up to the ruin time in this work; however, there are alternative definitions of “ruin” (see Section 5 in Avanzi [[5](https://arxiv.org/html/2511.08433v1#bib.bib5)]), and it will be interesting to revisit our problem under such alternative definitions.
In this paper, we chose the notion of weak equilibrium (see Björk and Murgoci [[10](https://arxiv.org/html/2511.08433v1#bib.bib10)]), and several recent papers pointed out its potential drawback and proposed different notions of equilibrium, such as strong equilibrium (see, for instance, Bayraktar et al. [[7](https://arxiv.org/html/2511.08433v1#bib.bib7)], Bayraktar et al. [[8](https://arxiv.org/html/2511.08433v1#bib.bib8)], and He and Jiang [[24](https://arxiv.org/html/2511.08433v1#bib.bib24)]). To the best of our knowledge, time-inconsistent singular control problems under the notion of strong equilibrium have not been studied before. Our numerical experiments show that the barrier x~\tilde{x} varies continuously with respect to the model parameters (see Figures [3](https://arxiv.org/html/2511.08433v1#S5.F3 "Figure 3 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), [5](https://arxiv.org/html/2511.08433v1#S5.F5 "Figure 5 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion"), and [6](https://arxiv.org/html/2511.08433v1#S5.F6 "Figure 6 ‣ 5 Numerical examples ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion")), when the conditions of Theorem [4.2](https://arxiv.org/html/2511.08433v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Equilibrium dividend strategies ‣ Equilibrium Strategies for Singular Dividend Control Problems under the Mean-Variance Criterion") hold; however, an *analytical* study of the stability of equilibria (as in Bayraktar et al. [[9](https://arxiv.org/html/2511.08433v1#bib.bib9)]) remains an open question, and we leave it for future research.

Acknowledgments. We thank the corresponding editor, Professor Erhan Bayraktar, and anonymous associate editor and reviewers for their valuable comments. The first and second authors acknowledge the financial support from the Natural Sciences and Engineering Research Council of Canada, grants 05061 and 04958, respectively. The third author thanks the Cecil J. and Ethel M. Nesbitt Professorship for the financial support of her research.

## References

* [1]
   Albrecher, Hansjörg and Stefan Thonhauser (2009). Optimality results for dividend problems in insurance. Revista de la Real Academia de Ciencias Exactas, Fisicas y Naturales, 103(2), 295-320.
* [2]
   Albrecher, Hansjörg, Pablo Azcue, and Nora Muler (2022). Optimal ratcheting of dividends in a Brownian risk model. SIAM Journal on Financial Mathematics, 13(3), 657-701.
* [3]
   Angoshtari, Bahman, Erhan Bayraktar, and Virginia R. Young (2019). Optimal dividend distribution under drawdown and ratcheting constraints on dividend rates. SIAM Journal on Financial Mathematics, 10(2), 547-577.
* [4]
   Asmussen, Soren and Michael Taksar (1997). Controlled diffusion models for optimal dividend pay-out. Insurance: Mathematics and Economics, 20(1), 1-15.
* [5]
   Avanzi, Benjamin (2009). Strategies for dividend distribution: A review. North American Actuarial Journal, 13(2), 217-251.
* [6]
   Bayraktar, Erhan, Jingjie Zhang, and Zhou Zhou (2019). Time consistent stopping for the mean-standard deviation problem—The discrete time case. SIAM Journal on Financial Mathematics, 10(2), 667-697.
* [7]
   Bayraktar, Erhan, Jingjie Zhang, and Zhou Zhou (2021). Equilibrium concepts for time‐inconsistent stopping problems in continuous time. Mathematical Finance, 31(1), 508-530.
* [8]
   Bayraktar, Erhan, Zhenhua Wang, and Zhou Zhou (2023). Equilibria of time‐inconsistent stopping for one‐dimensional diffusion processes. Mathematical Finance, 33(3), 797-841.
* [9]
   Bayraktar, Erhan, Zhenhua Wang, and Zhou Zhou (2023). Stability of equilibria in time-inconsistent stopping problems. SIAM Journal on Control and Optimization, 61(2), 674-696.
* [10]
   Björk, Tomas and Agatha Murgoci (2010). A general theory of Markovian time inconsistent stochastic control problems. Working paper, available at SSRN 1694759.
* [11]
   Björk, Tomas, Agatha Murgoci, and Xun Yu Zhou (2014). Mean-variance portfolio optimization with state-dependent risk aversion. Mathematical Finance, 24(1), 1-24.
* [12]
   Cao, Jingyi, Dongchen Li, Virginia R. Young, and Bin Zou (2025). Equilibrium mean-variance dividend rate strategies. SIAM Journal on Financial Mathematics, 16(3), SC64-SC75.
* [13]
   Chen, Shumin, Zhongfei Li, and Yan Zeng (2014). Optimal dividend strategies with time-inconsistent preferences. Journal of Economic Dynamics and Control, 46, 150-172.
* [14]
   Chen, Shumin, Zhongfei Li, and Yan Zeng (2018). Optimal dividend strategy for a general diffusion process with time-inconsistent preferences and ruin penalty. SIAM Journal on Financial Mathematics, 9(1), 274-314.
* [15]
   Christensen, Sören and Kristoffer Lindensjö (2022). Moment-constrained optimal dividends: precommitment and consistent planning. Advances in Applied Probability, 54(2), 404-432.
* [16]
   Cohen, Asaf and Virginia R. Young (2021). Optimal dividend problem: Asymptotic analysis. SIAM Journal on Financial Mathematics, 12(1), 29-46.
* [17]
   Dai, Min, Yanwei Jia, and Hanqing Jin (2024). Dynamic mean-variance portfolio selection with transaction costs. Working paper, available at SSRN: <https://ssrn.com/abstract=4958481>.
* [18]
   De Finetti, Bruno (1957). Su un’impostazione alternativa della teoria collettiva del rischio. Transactions of the XVth International Congress of Actuaries, 2(1), 433-443.
* [19]
   Eisenberg, Julia and Krühner, Paul (2023). Measuring the suboptimality of dividend controls in a Brownian risk model. Advances in Applied Probability, 55(4), 1442-1472.
* [20]
   Fleming, Wendell H. and H. Mete Soner (2006). Controlled Markov Processes and Viscosity Solutions, second edition, Springer.
* [21]
   Gerber, Hans U. and Elias SW Shiu (2004). Optimal dividends: analysis with Brownian motion. North American Actuarial Journal, 8(1), 1-20.
* [22]
   Grandell, Jan (1991). Aspects of Risk Theory. Springer-Verlag, New York.
* [23]
   Grandits, Peter, Friedrich Hubalek, Walter Schachermayer, and Mislav Žigo (2007). Optimal expected exponential utility of dividend payments in a Brownian risk model. Scandinavian Actuarial Journal, 2, 73 -107.
* [24]
   He, Xue Dong and Zhao Li Jiang (2021). On the equilibrium strategies for time-inconsistent problems in continuous time. SIAM Journal on Control and Optimization, 59(5), 3860-3886.
* [25]
   Huang, Yu-Jui and Zhou Zhou (2021). Strong and weak equilibria for time-inconsistent stochastic control in continuous time. Mathematics of Operations Research, 46(2), 428-451.
* [26]
   Ismail, Amine and Huyên Pham (2019). Robust Markowitz mean‐variance portfolio selection under ambiguous covariance matrix. Mathematical Finance, 29(1), 174-207.
* [27]
   Jeanblanc-Picqué, Monique and Albert N. Shiryaev (1995). Optimization of the flow of dividends. Russian Mathematical Surveys, 50(2), 257.
* [28]
   Kronborg, Morten Tolver and Mogens Steffensen (2015). Inconsistent investment and consumption problems. Applied Mathematics and Optimization, 71, 473-515.
* [29]
   Guan, Chonghu and Zuo Quan Xu (2024). Optimal ratcheting of dividend payout under Brownian motion surplus. SIAM Journal on Control and Optimization, 62(5), 2590-2620.
* [30]
   Landriault, David, Bin Li, Danping Li, and Virginia R. Young (2018). Equilibrium strategies for the mean-variance investment problem over a random horizon. SIAM Journal on Financial Mathematics, 9(3), 1046-1073.
* [31]
   Liang, Zongxia, Xiaodong Luo, and Fengyi Yuan (2024). Equilibria for time-inconsistent singular control problems. SIAM Journal on Control and Optimization, 62(6), 3213-3238.
* [32]
   Liang, Zongxia and Xiaodong Luo (2025). Stackelberg reinsurance and premium decisions with MV criterion and irreversibility. SIAM Journal on Financial Mathematics, 16(1), 167-199.
* [33]
   Taksar, Michael I. (2000). Optimal risk and dividend distribution control models for an insurance company. Mathematical Methods of Operations Research, 51, 1-42.
* [34]
   Wang, Gu and Bin Zou (2021). Optimal fee structure of variable annuities. Insurance: Mathematics and Economics, 101, 587-601.
* [35]
   Zhu, Jinxia, Tak Kuen Siu, and Hailiang Yang (2020). Singular dividend optimization for a linear diffusion model with time-inconsistent preferences. European Journal of Operational Research, 285(1), 66-80.
* [36]
   Zhou, Zhou and Zhuo Jin (2020). Optimal equilibrium barrier strategies for time-inconsistent dividend problems in discrete time. Insurance: Mathematics and Economics, 94, 100-108.