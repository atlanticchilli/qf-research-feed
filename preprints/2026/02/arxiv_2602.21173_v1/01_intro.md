---
authors:
- Miguel C. Herculano
doc_id: arxiv:2602.21173v1
family_id: arxiv:2602.21173
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Bayesian Parametric Portfolio Policies
url_abs: http://arxiv.org/abs/2602.21173v1
url_html: https://arxiv.org/html/2602.21173v1
venue: arXiv q-fin
version: 1
year: 2026
---


Miguel C. Herculano
Adam Smith Business School, University of Glasgow.
E: [miguel.herculano@glasgow.ac.uk](mailto:miguel.herculano@glasgow.ac.uk).
W: [mcherculano.github.io](https://mcherculano.github.io)

(This Version: February 2026)

Parametric Portfolio Policies (PPP) estimate optimal portfolio weights directly as functions of observable signals by maximizing expected utility, bypassing the need to model asset returns and covariances. However, PPP ignores policy risk. We show that this is consequential, leading to an overstatement of expected utility and an understatement of portfolio risk. We develop Bayesian Parametric Portfolio Policies (BPPP), which place a prior on policy coefficients thereby correcting the decision rule. We derive a general result showing that the utility gap between PPP and BPPP is strictly positive and proportional to posterior parameter uncertainty and signal magnitude. Under a mean–variance approximation, this correction appears as an additional estimation-risk term in portfolio variance, implying that PPP overexposes when signals are strongest and when risk aversion is high. Empirically, in a high-dimensional setting with 242 signals and six factors over 1973–2023, BPPP delivers higher Sharpe ratios, substantially lower turnover, larger investor welfare, and lower tail risk, with advantages that increase monotonically in risk aversion and are strongest during crisis episodes.

Keywords: Portfolio choice; Bayesian decision theory; factor timing; estimation risk.
  
JEL Codes: G11, C11, C52.

## 1 Introduction

A central problem in asset pricing is to translate predictive information into portfolio decisions in a way that is both economically meaningful and empirically robust. Decades of research document that expected returns vary predictably with firm characteristics and macroeconomic signals (Chen and Zimmermann, [2022](https://arxiv.org/html/2602.21173v1#bib.bib2 "Open source cross-sectional asset pricing"); Gu et al., [2020](https://arxiv.org/html/2602.21173v1#bib.bib21 "Empirical asset pricing via machine learning"); Haddad et al., [2020](https://arxiv.org/html/2602.21173v1#bib.bib9 "Factor timing")), yet exploiting such predictability in real time remains challenging. Classic mean-variance approaches require modelling the joint conditional distribution of returns, a task that quickly becomes infeasible in high-dimensional settings and is known to produce unstable weights in finite samples (DeMiguel et al., [2009](https://arxiv.org/html/2602.21173v1#bib.bib5 "Optimal versus naive diversification: how inefficient is the 1/N portfolio strategy?"); Green et al., [2017](https://arxiv.org/html/2602.21173v1#bib.bib6 "The characteristics that provide independent information about average U.S. monthly stock returns")). Parametric Portfolio Policies (PPP), introduced by Brandt et al. ([2009](https://arxiv.org/html/2602.21173v1#bib.bib1 "Parametric portfolio policies: exploiting characteristics in the cross-section of equity returns")), offer an appealing solution. Rather than modelling returns, PPP parameterise portfolio weights directly as functions of observable predictors and estimate policy parameters by maximising average realised utility.

PPP rests on a strong implicit assumption that motivates this paper. Once the policy parameter θ\theta is estimated, the investor behaves as if θ^\hat{\theta} were the true data-generating policy, ignoring the uncertainty surrounding such estimate. We show that this treatment of policy uncertainty is consequential, leading to a systematic overstatement of investor welfare and understatement of portfolio risk. Moreover, these effects are largest when risk aversion is high or signals are strong, exactly when PPP takes its most aggressive positions. We adopt a Bayesian perspective and treat the policy parameter θ\theta as a random variable. Bayesian Parametric Portfolio Policies (BPPP) places a prior on θ\theta and integrates expected utility over the resulting posterior, internalizing policy risk and producing more stable portfolio allocations. Crucially, this stability is not imposed through an ad hoc penalty or constraint. It arises directly from rational investor behaviour under concave utility and uncertain parameters. In a mean-variance approximation, the BPPP correction adds an estimation-risk term to the variance of portfolio returns, shrinking tilts proportionally.

Several aspects of the framework are worth emphasising. First, BPPP nests PPP as the special case of a flat (uninformative) prior, in which the posterior collapses to a point mass at θ^\hat{\theta}. Second, the framework requires no distributional assumptions on returns beyond those already embedded in the utility function. Third, from an empirical viewpoint BPPP accommodates an additional source of information for portfolio construction, via the prior which allows for the inclusion of investor’s ex-ante beliefs about how aggressively the policy should respond to signals.

We evaluate BPPP by using six Fama–French factor portfolios, 242 predictive signals (212 anomaly-based predictors from Chen and Zimmermann ([2022](https://arxiv.org/html/2602.21173v1#bib.bib2 "Open source cross-sectional asset pricing")) and 30 factor-timing signals following Haddad et al. ([2020](https://arxiv.org/html/2602.21173v1#bib.bib9 "Factor timing"))), and an expanding-window out-of-sample exercise from 1973M8 to 2023M12. This high-dimensional environment is precisely the setting where parameter uncertainty is large and the overstatement predicted is most severe. BPPP achieves a gross out-of-sample Sharpe ratio of 1.32, versus 1.05 for PPP and 0.74 for the market benchmark. Under CRRA utility with moderate risk aversion (γ=5\gamma=5), BPPP delivers a certainty-equivalent advantage of 536 basis points per annum relative to the market benchmark, compared with 353 basis points for PPP. The gap widens with risk aversion, at γ=10\gamma=10 the difference is about 255 basis points, consistent with the prediction that the overexposure correction matters most for risk averse investors. Turnover falls materially relative to PPP, and at 50 basis points of transaction costs BPPP retains a net Sharpe near 0.99 versus 0.60 for PPP. The BPPP advantage holds in four of the five complete decades of the sample and in both major crisis episodes (the Great Financial Crisis and Covid). The Bayesian approach also yields portfolios with lower tail risk.

Our paper contributes to several strands of the literature. The classical Bayesian portfolio choice literature (Kandel and Stambaugh, [1996](https://arxiv.org/html/2602.21173v1#bib.bib10 "On the predictability of stock returns: an asset-allocation perspective"); Pástor and Stambaugh, [2000](https://arxiv.org/html/2602.21173v1#bib.bib11 "Comparing asset pricing models: an investment perspective"); Barberis, [2000](https://arxiv.org/html/2602.21173v1#bib.bib31 "Investing for the long run when returns are predictable")) shows that parameter uncertainty leads to more conservative allocations when modelled explicitly, but does so within the framework of return-distribution modelling. We operate entirely within the PPP framework and identify the specific channels that forces conservatism without any distributional assumptions on returns. Our posterior is a Gibbs posterior in the sense of Bissiri et al. ([2016](https://arxiv.org/html/2602.21173v1#bib.bib3 "A general framework for updating belief distributions")), updated by utility rather than likelihood, and PPP emerges as its mode under a flat prior.

Within the PPP literature, Brandt et al. ([2009](https://arxiv.org/html/2602.21173v1#bib.bib1 "Parametric portfolio policies: exploiting characteristics in the cross-section of equity returns")) and related work by Brandt and Santa-Clara ([2006](https://arxiv.org/html/2602.21173v1#bib.bib15 "Dynamic portfolio selection by augmenting the asset space")) treat θ\theta as known with certainty throughout. Our contribution is to relax that assumption within the parametric policy-rule framework and quantify the portfolio implications of policy-parameter uncertainty. This is complementary to broader Bayesian portfolio-choice work such as Garlappi et al. ([2007](https://arxiv.org/html/2602.21173v1#bib.bib12 "Portfolio selection with parameter and model uncertainty: a multi-prior approach")) and Tu and Zhou ([2011](https://arxiv.org/html/2602.21173v1#bib.bib13 "Markowitz meets talmud: a combination of sophisticated and naive diversification strategies")) and others reviewed by Avramov and Zhou ([2010](https://arxiv.org/html/2602.21173v1#bib.bib7 "Bayesian portfolio analysis")), which operates in return-distribution or mean-variance allocation settings rather than PPP policy estimation. The result also complements work on portfolio regularisation (DeMiguel et al., [2009](https://arxiv.org/html/2602.21173v1#bib.bib5 "Optimal versus naive diversification: how inefficient is the 1/N portfolio strategy?"); Koijen et al., [2018](https://arxiv.org/html/2602.21173v1#bib.bib17 "Carry")) by showing that shrinkage in PPP has a decision-theory interpretation rather than being only a statistical convenience. The paper also connects to the factor timing literature (Haddad et al., [2020](https://arxiv.org/html/2602.21173v1#bib.bib9 "Factor timing"); Ilmanen et al., [2021](https://arxiv.org/html/2602.21173v1#bib.bib18 "Factor premia and factor timing: a century of evidence"); Arnott et al., [2019](https://arxiv.org/html/2602.21173v1#bib.bib19 "Alice’s adventures in factorland: three blunders that plague factor investing")) and the high-dimensional asset pricing literature (Green et al., [2017](https://arxiv.org/html/2602.21173v1#bib.bib6 "The characteristics that provide independent information about average U.S. monthly stock returns"); Kozak et al., [2020](https://arxiv.org/html/2602.21173v1#bib.bib20 "Shrinking the cross-section"); Gu et al., [2020](https://arxiv.org/html/2602.21173v1#bib.bib21 "Empirical asset pricing via machine learning")). While those papers focus on signal selection in predicting the Stochastic Discount Factor, we look at the most relevant signals in the context of portfolio decisions by risk averse investors. Our utility-based approach also aligns with the critique in Wang et al. ([2026](https://arxiv.org/html/2602.21173v1#bib.bib33 "Machine learning meets Markowitz")), who argue that the conventional two-stage separation between return forecasting and portfolio optimisation is suboptimal. BPPP avoids that separation by design, directly optimising expected utility over the posterior distribution of policy parameters.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2602.21173v1#S2 "2 Setup and Motivation ‣ Bayesian Parametric Portfolio Policies") sets notation and motivates the exercise. Section [3](https://arxiv.org/html/2602.21173v1#S3 "3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies") develops Bayesian Parametric Portfolio Policies and derives the key proposition; a brief discussion of the estimation procedure is provided at the end of that section, with full details in Appendix [B](https://arxiv.org/html/2602.21173v1#A2 "Appendix B Estimation ‣ Bayesian Parametric Portfolio Policies"). Section [4](https://arxiv.org/html/2602.21173v1#S4 "4 Data ‣ Bayesian Parametric Portfolio Policies") describes the data. Section [5](https://arxiv.org/html/2602.21173v1#S5 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies") presents empirical results. Section [6](https://arxiv.org/html/2602.21173v1#S6 "6 Robustness ‣ Bayesian Parametric Portfolio Policies") reports robustness checks. Section [7](https://arxiv.org/html/2602.21173v1#S7 "7 Conclusion ‣ Bayesian Parametric Portfolio Policies") concludes.

## 2 Setup and Motivation

At each date tt, an investor observes a vector of LL signals ztz\_{t} and chooses portfolio weights wtw\_{t} over KK assets. Portfolio returns realised at t+1t+1 are rp,t+1=wt′​Rt+1r\_{p,t+1}=w\_{t}^{\prime}R\_{t+1}, where Rt+1R\_{t+1} is the vector of gross returns. The investor has time-separable CRRA preferences and, abstracting from intertemporal hedging motives, solves at each date tt

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxwt∈𝒲⁡𝔼t​[U​(rp,t+1)],\displaystyle\max\_{w\_{t}\in\mathcal{W}}\;\mathbb{E}\_{t}\!\left[U(r\_{p,t+1})\right], |  | (1) |

where 𝒲\mathcal{W} is the feasible set and U(.)U(.) is the utility function. Solving this problem directly requires the conditional distribution of Rt+1|ztR\_{t+1}|z\_{t}, which is high-dimensional and difficult to estimate reliably. Brandt et al. ([2009](https://arxiv.org/html/2602.21173v1#bib.bib1 "Parametric portfolio policies: exploiting characteristics in the cross-section of equity returns")) resolve this difficulty by restricting attention to portfolio rules that are explicit functions of observable signals. Weights follow the linear policy rule

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt​(θ)=wb+θ​zt,\displaystyle w\_{t}(\theta)=w\_{b}+\theta z\_{t}, |  | (2) |

where wbw\_{b} is a benchmark allocation (the market portfolio throughout) and
θ∈ℝK×L\theta\in\mathbb{R}^{K\times L} is the policy parameter matrix, normalised to
portfolio-weight scale so that each entry θk​ℓ\theta\_{k\ell} represents the weight response
of asset kk to signal ℓ\ell, and θ​zt\theta z\_{t} is the signal-induced tilt away from
the benchmark.
In this framework, dynamic portfolio choice reduces to estimating θ\theta. Given observations 𝒟T={(Rt+1,zt)}t=1T\mathcal{D}\_{T}=\{(R\_{t+1},z\_{t})\}\_{t=1}^{T}, the PPP investor solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^=arg⁡maxθ⁡1T​∑t=1TU​(wt​(θ)′​Rt+1).\hat{\theta}=\arg\max\_{\theta}\frac{1}{T}\sum\_{t=1}^{T}U\!\left(w\_{t}(\theta)^{\prime}R\_{t+1}\right). |  | (3) |

Equation [3](https://arxiv.org/html/2602.21173v1#S2.E3 "In 2 Setup and Motivation ‣ Bayesian Parametric Portfolio Policies") is a sample analogue of expected utility maximisation over policies, and it has three attractive properties. It delivers state-dependent, implementable portfolio rules, it requires no explicit return distribution, and it scales to large signal spaces.

The formulation of Parametric Portfolio Policies (PPP) treats the policy parameter θ\theta as an unknown but fixed object, estimated by maximising sample average utility. Once a point estimate θ^\hat{\theta} is obtained, portfolio decisions are taken as if this estimate were known with certainty. This plug-in approach is standard in the PPP literature, but it neglects estimation uncertainty in the policy parameters. From a decision-theory perspective, this omission is consequential. Policy parameters are estimated from a finite sample of noisy signals. When LL is large relative to TT, θ^\hat{\theta} is estimated with substantial error. Small perturbations in θ^\hat{\theta} translate linearly into portfolio tilts and can produce large, unstable weight changes from period to period. Excessive turnover and unstable portfolio choices are an expected consequence of estimation risk of PPP. The deeper issue, however, is not merely a finite-sample nuisance. The investor knows that θ\theta is uncertain, yet behaves as if it is not. We formalise the cost of this inconsistency and propose another approach in the next section.

## 3 Bayesian Parametric Portfolio Policies

When θ\theta is uncertain, rational portfolio choice requires integrating expected utility over this uncertainty rather than conditioning on a single estimated policy. We adopt a Bayesian perspective and treat the policy parameter θ\theta as a random variable. Given a prior distribution p​(θ)p(\theta) and the loss function implied by the PPP objective, the posterior distribution of θ\theta is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(θ∣𝒟T)∝exp⁡(∑t=1TU​(π​(zt;θ)′​Rt+1))​p​(θ).\displaystyle p(\theta\mid\mathcal{D}\_{T})\;\propto\;\exp\!\left(\sum\_{t=1}^{T}U\!\left(\pi(z\_{t};\theta)^{\prime}R\_{t+1}\right)\right)p(\theta). |  | (4) |

Rather than updating beliefs through a conventional likelihood, which would require a parametric model for returns, we follow Bissiri et al. ([2016](https://arxiv.org/html/2602.21173v1#bib.bib3 "A general framework for updating belief distributions")) and update using the PPP objective itself as a loss function. Under this formulation, the PPP estimator corresponds to the posterior mode under a flat prior. In contrast, Bayesian Parametric Portfolio Policies (BPPP) explicitly account for the full posterior distribution of θ\theta.
Given the posterior distribution p​(θ∣𝒟T)p(\theta\mid\mathcal{D}\_{T}), the Bayesian investor evaluates portfolio performance by integrating expected utility over parameter uncertainty. Formally, the investor’s objective at time tt can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝔼θ∣𝒟T​[𝔼t​[U​(π​(zt;θ)′​Rt+1)]],\mathbb{E}\_{\theta\mid\mathcal{D}\_{T}}\left[\mathbb{E}\_{t}\left[U\!\left(\pi(z\_{t};\theta)^{\prime}R\_{t+1}\right)\right]\right], |  |

integrating expected utility over both future returns and residual uncertainty about the policy. Portfolio weights are constructed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | wtBPPP=𝔼θ|𝒟T​[wt​(θ)]=wb+𝔼​[θ|𝒟T]​zτ,w\_{t}^{\text{BPPP}}=\mathbb{E}\_{\theta|\mathcal{D}\_{T}}\!\left[w\_{t}(\theta)\right]=w\_{b}+\mathbb{E}[\theta|\mathcal{D}\_{T}]\,z\_{\tau}, |  | (5) |

where the last equality uses the linearity of wτ​(θ)w\_{\tau}(\theta) in θ\theta. In practice, this expectation is approximated via a Laplace approximation averaging around the MAP policy (See Section [B](https://arxiv.org/html/2602.21173v1#A2 "Appendix B Estimation ‣ Bayesian Parametric Portfolio Policies") for further details). This construction highlights the key difference between PPP and BPPP. While PPP selects a single optimal policy and ignores estimation risk, BPPP averages over a distribution of plausible policies.

The Bayesian averaging implicit in BPPP has a clear economic interpretation which forms the basis of the central claim of this paper. Under nonlinear utility, expected utility is a concave function of portfolio returns. As a result, U​(𝔼​[rp])≠𝔼​[U​(rp)]U\!\left(\mathbb{E}[r\_{p}]\right)\neq\mathbb{E}\!\left[U(r\_{p})\right],
and ignoring parameter uncertainty can lead to overly aggressive portfolio choices. More precisely, under concave utility, expected utility is strictly less than the utility evaluated at expected returns. Parameter uncertainty therefore reduces expected utility even if it leaves expected returns unchanged. By integrating utility over the posterior distribution of policy parameters, BPPP internalizes estimation risk and produces more stable portfolio allocations. We formalize this result next.

###### Proposition 1

Define the conditional expected utility of policy θ\theta at date τ\tau as

|  |  |  |
| --- | --- | --- |
|  | Gτ​(θ)=𝔼τ​[U​(wτ​(θ)′​Rτ+1)],G\_{\tau}(\theta)\;=\;\mathbb{E}\_{\tau}\!\left[U\!\left(w\_{\tau}(\theta)^{\prime}R\_{\tau+1}\right)\right], |  |

and let mτ=𝔼​[θ|𝒟Tτ]m\_{\tau}=\mathbb{E}[\theta|\mathcal{D}\_{T\_{\tau}}] denote the posterior mean, Σθ,τ=Var⁡(θ|𝒟Tτ)\Sigma\_{\theta,\tau}=\operatorname{Var}(\theta|\mathcal{D}\_{T\_{\tau}}) the posterior covariance, UU a strictly concave and twice continuously differentiable utility function, where Σθ,τ≠0\Sigma\_{\theta,\tau}\neq 0. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼θ|𝒟Tτ​[Gτ​(θ)]<Gτ​(mτ).\mathbb{E}\_{\theta|\mathcal{D}\_{T\_{\tau}}}\!\left[G\_{\tau}(\theta)\right]\;<\;G\_{\tau}(m\_{\tau}). |  | (6) |

Moreover, to second order in Σθ,τ\Sigma\_{\theta,\tau},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gτ​(mτ)−𝔼θ|𝒟Tτ​[Gτ​(θ)]≈−12​tr⁡(∇θ2Gτ​(mτ)​Σθ,τ)> 0,G\_{\tau}(m\_{\tau})-\mathbb{E}\_{\theta|\mathcal{D}\_{T\_{\tau}}}\!\left[G\_{\tau}(\theta)\right]\;\approx\;-\tfrac{1}{2}\operatorname{tr}\!\left(\nabla^{2}\_{\theta}G\_{\tau}(m\_{\tau})\,\Sigma\_{\theta,\tau}\right)\;>\;0, |  | (7) |

and under a quadratic approximation to UU the difference is proportional to zτ′​Σθ,τ​zτz\_{\tau}^{\prime}\Sigma\_{\theta,\tau}z\_{\tau} and return second moments, hence strictly increasing in ‖zτ‖\|z\_{\tau}\| and in every eigenvalue of Σθ,τ\Sigma\_{\theta,\tau}.

The proof is in Appendix [A](https://arxiv.org/html/2602.21173v1#A1 "Appendix A Proofs and Additional Details ‣ Bayesian Parametric Portfolio Policies").
The proposition has three direct implications, each of which maps to an empirical prediction which forms the basis of our empirical exercise as follows.

(i) PPP overstates expected utility. The PPP investor evaluates Gτ​(θ^)≈Gτ​(mτ)G\_{\tau}(\hat{\theta})\approx G\_{\tau}(m\_{\tau}) and treats this as the expected utility of the implemented policy. Inequality ([6](https://arxiv.org/html/2602.21173v1#S3.E6 "In Proposition 1 ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")) says this number is always too high. The utility that will actually be achieved in expectation is 𝔼θ​[Gτ​(θ)]<Gτ​(mτ)\mathbb{E}\_{\theta}[G\_{\tau}(\theta)]<G\_{\tau}(m\_{\tau}).

(ii) Overexposure is worst precisely when PPP bets hardest. From ([7](https://arxiv.org/html/2602.21173v1#S3.E7 "In Proposition 1 ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")), the utility gap grows with zτ′​Σθ,τ​zτz\_{\tau}^{\prime}\Sigma\_{\theta,\tau}z\_{\tau}, the quadratic form of posterior uncertainty evaluated at the current signal vector. When signals are large in magnitude, PPP generates large tilts *and* faces the largest utility overstatement. The two forces compound, i.e. PPP is most overconfident at exactly the moments it is most aggressive.

(iii) PPP underestimates portfolio risk. Under a mean-variance approximation, the investor’s objective is 𝔼​[rp,τ+1]−γ2​Var⁡(rp,τ+1)\mathbb{E}[r\_{p,\tau+1}]-\frac{\gamma}{2}\operatorname{Var}(r\_{p,\tau+1}). The law of total variance gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var⁡(rp,τ+1)=𝔼θ​[Var⁡(rp,τ+1∣θ)]⏟market risk+zτ′​Σθ,τ​zτ⋅‖μτ+1‖2⏟estimation risk,\displaystyle\operatorname{Var}(r\_{p,\tau+1})\;=\;\underbrace{\mathbb{E}\_{\theta}\!\left[\operatorname{Var}\!\left(r\_{p,\tau+1}\mid\theta\right)\right]}\_{\text{market risk}}\;+\;\underbrace{z\_{\tau}^{\prime}\Sigma\_{\theta,\tau}z\_{\tau}\cdot\|\mu\_{\tau+1}\|^{2}}\_{\text{estimation risk}}, |  | (8) |

where μτ+1=𝔼​τ​[R​τ+1]\mu\_{\tau+1}=\mathbb{E}\tau[R{\tau+1}] is the vector of conditional expected returns. The proof is in Appendix [A](https://arxiv.org/html/2602.21173v1#A1 "Appendix A Proofs and Additional Details ‣ Bayesian Parametric Portfolio Policies"). Notice that PPP ignores the second term. Ignoring parameter uncertainty is therefore equivalent to understating portfolio risk, and the resulting overexposure to signals is an arithmetic consequence of an incomplete objective. In implementation, PPP further approximates the first term using a plug-in policy at θ=mτ\theta=m\_{\tau}. BPPP internalises the estimation-risk term by default, without any ad hoc penalty or constraint.

Two further observations follow directly from Proposition 1. First, the PPP investor solves for optimal policies under the assumption that posterior uncertainty is zero, i.e. Σθ,τ=0\Sigma\_{\theta,\tau}=0. This is the certainty-equivalent approximation to the Bayesian decision rule. Proposition 1 quantifies the cost of this approximation, given by the estimation risk term in Equation [8](https://arxiv.org/html/2602.21173v1#S3.E8 "In 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies"), which grows without bound as L/TL/T increases. In high-dimensional environments, the approximation error is largest.

Second, empirical gains associated to a BPPP ought to be largest for risk averse investors. Because the gap ([7](https://arxiv.org/html/2602.21173v1#S3.E7 "In Proposition 1 ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")) scales with γ\gamma under quadratic approximation, the welfare cost of PPP is strictly increasing in risk aversion. A moderately risk-averse investor (γ=5\gamma=5) suffers a utility overstatement proportional to 52​zτ′​Σθ,τ​zτ\frac{5}{2}z\_{\tau}^{\prime}\Sigma\_{\theta,\tau}z\_{\tau}, while a highly risk-averse investor (γ=10\gamma=10) suffers twice as much.

### 3.1 The role of the Prior

The prior p​(θ)p(\theta) in equation ([4](https://arxiv.org/html/2602.21173v1#S3.E4 "In 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")) encodes the investor’s ex-ante beliefs about how aggressively the policy should respond to signals. In this context, the prior summarises beliefs about the appropriate scale of portfolio tilts rather than a fully specified structural return model. It is worth noting that the prior also governs the posterior variance Σθ,τ\Sigma\_{\theta,\tau} that determines the size of the utility gap in Proposition 1. Our baseline prior at time tt is

|  |  |  |
| --- | --- | --- |
|  | θt∼𝒩​(Mt,ν​I),\theta\_{t}\sim\mathcal{N}(M\_{t},\nu I), |  |

where MtM\_{t} is the prior mean and ν\nu is the effective prior variance. We set Mt=θ^t−1M\_{t}=\hat{\theta}\_{t-1} so the prior penalises deviations from previous policy parameters, mimicking a regular rebalancing procedure by investors. The hyperparameter ν\nu is set from a single economically interpretable quantity, the target-tilt standard deviation δ\delta which defines the investor’s prior belief about the typical magnitude of signal-induced deviations from MtM\_{t}. With LL standardised signals, the variance of the aggregate tilt on asset kk is L​σθ2L\sigma\_{\theta}^{2}, so setting the tilt’s standard deviation to δ\delta gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | σθ=δL.\sigma\_{\theta}=\frac{\delta}{\sqrt{L}}. |  | (9) |

This calibration is dimension-adaptive.111The numerical implementation stores θ\theta at KK times the portfolio-weight scale and computes tilts as θ~​zt/K\tilde{\theta}z\_{t}/K, so the variance of the aggregate tilt is L​σθ~2/K2L\sigma\_{\tilde{\theta}}^{2}/K^{2}. Setting this equal to δ2\delta^{2} gives σθ~=K​δ/L\sigma\_{\tilde{\theta}}=K\delta/\sqrt{L} internally. Since θ=θ~/K\theta=\tilde{\theta}/K, the implied prior standard deviation on the portfolio-weight-scaled parameter is σθ=δ/L\sigma\_{\theta}=\delta/\sqrt{L} as stated, and the KK factors cancel exactly in the MAP and Laplace computations. As LL grows, each individual coefficient is shrunk more tightly at rate 1/L1/\sqrt{L}, keeping the aggregate tilt stable. With L=242L=242 and δ=0.35\delta=0.35, we obtain σθ≈0.0225\sigma\_{\theta}\approx 0.0225. To maintain a meaningful balance between prior and data as the estimation window expands, we scale the effective prior variance by max⁡(T/L,1)\max(T/L,1)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν=σθ2⋅max⁡(TL,1).\nu=\sigma\_{\theta}^{2}\cdot\max\!\left(\frac{T}{L},1\right). |  | (10) |

When T≫LT\gg L the prior is diffuse and data dominate, whereas as T≈LT\approx L the prior retains meaningful weight and prevents overfitting.

Horseshoe prior. The Gaussian prior shrinks all coefficients uniformly. In high-dimensional settings, predictability may instead be concentrated in a small number of signals with the majority being pure noise. To accommodate this possibility, we also estimate a variant using the regularised horseshoe prior of Carvalho et al. ([2010](https://arxiv.org/html/2602.21173v1#bib.bib23 "The horseshoe estimator for sparse signals")) as refined by Piironen and Vehtari ([2017](https://arxiv.org/html/2602.21173v1#bib.bib29 "Sparsity information and regularization in the horseshoe and other shrinkage priors")) and defined as follows

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θt,k,ℓ∣λ~t,k,ℓ,Mt\displaystyle\theta\_{t,k,\ell}\mid\tilde{\lambda}\_{t,k,\ell},M\_{t} | ∼𝒩​(Mt,k,ℓ,λ~t,k,ℓ2),\displaystyle\;\sim\;\mathcal{N}\!\left(M\_{t,k,\ell},\;\tilde{\lambda}\_{t,k,\ell}^{2}\right), |  | (11) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λ~t,k,ℓ2\displaystyle\tilde{\lambda}\_{t,k,\ell}^{2} | =c2​λt,k,ℓ2​τ2c2+λt,k,ℓ2​τ2,\displaystyle\;=\;\frac{c^{2}\lambda\_{t,k,\ell}^{2}\tau^{2}}{c^{2}+\lambda\_{t,k,\ell}^{2}\tau^{2}}, |  |

where τ\tau is a global shrinkage scale, λt,k,ℓ\lambda\_{t,k,\ell} are local scales, cc is the slab scale of the Horseshoe, and σ2\sigma^{2} is residual variance. The global scale is calibrated as in Piironen and Vehtari ([2017](https://arxiv.org/html/2602.21173v1#bib.bib29 "Sparsity information and regularization in the horseshoe and other shrinkage priors"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ0=p0L−p0​σT,\tau\_{0}=\frac{p\_{0}}{L-p\_{0}}\frac{\sigma}{\sqrt{T}}, |  | (12) |

with p0p\_{0} reflecting the prior expectation about the number of signals that carry genuine predictive content. The posterior shrinkage factor for each signal is

|  |  |  |
| --- | --- | --- |
|  | κk,ℓ=11+λ~k,ℓ2​‖zℓ‖2/σ2,\kappa\_{k,\ell}=\frac{1}{1+\tilde{\lambda}\_{k,\ell}^{2}\|z\_{\ell}\|^{2}/\sigma^{2}}, |  |

where κ≈0\kappa\approx 0 means the signal survives and κ≈1\kappa\approx 1 means it is shrunk towards the mean. No coefficient is set exactly to zero, preserving the differentiable structure of the policy rule. Table [1](https://arxiv.org/html/2602.21173v1#S3.T1 "Table 1 ‣ 3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies") summarises the two prior specifications used in the empirical exercise later.

Table 1: Summary of Prior Specifications

| Model | Prior | Key hyperparameter | Shrinkage type |
| --- | --- | --- | --- |
| BPPP | 𝒩​(Mt,ν​I)\mathcal{N}(M\_{t},\nu I) | δ\delta (target tilt SD) | Global, uniform |
| Horseshoe | 𝒩​(Mt,λ~2)\mathcal{N}(M\_{t},\tilde{\lambda}^{2}) | p0p\_{0} (expected signals) | Global-local, adaptive |

* •

  Notes: ν\nu is defined in Equation ([10](https://arxiv.org/html/2602.21173v1#S3.E10 "In 3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")). λ~2\tilde{\lambda}^{2} is the local scale from Equation ([11](https://arxiv.org/html/2602.21173v1#S3.E11 "In 3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")). The Gaussian prior applies uniform shrinkage around Mt=θ^t−1M\_{t}=\hat{\theta}\_{t-1}. The horseshoe prior uses the same MtM\_{t} but adapts shrinkage signal-by-signal through local scales.

The two priors span a spectrum of assumptions about signal sparsity. The Gaussian prior is appropriate when predictability is diffuse, the Horseshoe is appropriate when it is sparse. Comparing them empirically allows us to assess whether the gains from BPPP depend on prior form or arise more broadly from posterior averaging. In this paper, we treat the Gaussian-vs-Horseshoe comparison as evidence on prior misspecification risk rather than a definitive model-selection result. Regardless of the prior chosen, none of these specifications impose hard constraints on the policy, perform variable selection in the frequentist sense, or alter the functional form of the decision rule. Their role is to determine the scale at which portfolio weights react to signals, controlled by Proposition 1’s Σθ,τ\Sigma\_{\theta,\tau}.

Given the posterior in Equation ([4](https://arxiv.org/html/2602.21173v1#S3.E4 "In 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")), portfolio weights are formed by averaging MM draws of θ\theta per Equation ([5](https://arxiv.org/html/2602.21173v1#S3.E5 "In 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")). Draws are obtained via a diagonal Laplace approximation centred at the maximum a posteriori (MAP) estimate, which is computed by L-BFGS-B optimisation of the penalised utility objective. The estimation window starts at T0=120T\_{0}=120 months and grows recursively. At each step the prior mean is set to Mt=θ^t−1M\_{t}=\hat{\theta}\_{t-1}, so the prior anchors the new estimate to the previous period’s policy. The Horseshoe variant replaces the Gaussian prior update with a coordinate-ascent step over the local scales {λk,ℓ}\{\lambda\_{k,\ell}\} and global scale τ\tau. Full algorithmic details are in Appendix [B](https://arxiv.org/html/2602.21173v1#A2 "Appendix B Estimation ‣ Bayesian Parametric Portfolio Policies").

## 4 Data

We use monthly returns on the six Fama–French factors. Market excess return (MKT-RF), size (SMB), value (HML), profitability (RMW), momentum (UMD), and investment (CMA), together with the one-month T-bill rate, downloaded from Professor Ken French’s Data Library. These form the investment universe (K=6K=6). The sample runs from July 1963 to December 2023.

As for predictive signals, we use 212 anomaly-based predictors drawn from the Open Source Asset Pricing database of Chen and Zimmermann ([2022](https://arxiv.org/html/2602.21173v1#bib.bib2 "Open source cross-sectional asset pricing")), constructed from CRSP and Compustat data and chosen for their replicability and breadth across the documented anomaly literature. The remaining 30 are factor-specific signals constructed following Haddad et al. ([2020](https://arxiv.org/html/2602.21173v1#bib.bib9 "Factor timing")), covering time-series momentum, cross-sectional momentum, factor valuation, reversal, and volatility for each factor. This combination of signal types ensures broad coverage of both firm-characteristic and factor-dynamics predictability.

Within each expanding estimation window, signals are standardised to zero mean and unit variance using only in-sample moments, ensuring no look-ahead bias. Missing values are replaced by zero after standardisation (mean imputation on the standardised scale). Predictors available at time tt form portfolio weights at tt, applied to returns realised at t+1t+1. We use an expanding window with an initial training sample of 120 months (1963M7–1973M7) and evaluate performance from 1973M8 onward, yielding 605 monthly out-of-sample observations (1973M8–2023M12). Portfolio rebalancing is monthly.

## 5 Empirical Results

Our empirical setting places the exercise squarely in the environment where Proposition 1 predicts the overexposure correction to be largest. We consider L=242L=242 signals and K=6K=6 assets consisting of the five Fama and French ([2015](https://arxiv.org/html/2602.21173v1#bib.bib30 "A five-factor asset pricing model")) plus momentum factors, therefore deploying the Parametric Portfolio Policy framework of Brandt et al. ([2009](https://arxiv.org/html/2602.21173v1#bib.bib1 "Parametric portfolio policies: exploiting characteristics in the cross-section of equity returns")) in factor space. The empirical results are organised around the three predictions of Proposition 1, that PPP overstates achievable utility, that overexposure is worst when signals are strongest, and that the gap grows with risk aversion. We begin by comparing performance among methods over the full sample. Table [2](https://arxiv.org/html/2602.21173v1#S5.T2 "Table 2 ‣ 5 Empirical Results ‣ Bayesian Parametric Portfolio Policies") reports annualised out-of-sample statistics for all strategies. BPPP achieves a gross Sharpe ratio of 1.32 and PPP 1.05, both above the market benchmark (0.74), mean-variance portfolio (1.04), and simple momentum PPP strategy (0.93), which consists of PPP with a single momentum signal. As shown in Table [3](https://arxiv.org/html/2602.21173v1#S6.T3 "Table 3 ‣ 6.1 Statistical Significance and Spanning Tests ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies"), a circular block-bootstrap Sharpe-difference test rejects equal Sharpe ratios between BPPP and the market at the 1% level. PPP also outperforms significantly, but with lower precision, consistent with noisier coefficient estimates.

Table 2: Out-of-Sample Performance Comparison of Portfolio Strategies

|  | Mean | Vol | Sharpe | MaxDD | VaR 95 | CVaR 95 | Turnover | Skew | Kurt. | Sharpe (net) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (%) | (%) |  | (%) | (%) | (%) |  |  |  |  |
| Benchmark (Mkt) | 11.83 | 16.01 | 0.74 | -50.31 | -7.33 | -10.11 | 0.00 | -0.51 | 1.76 | 0.74 |
| Mean-Variance | 7.12 | 6.87 | 1.04 | -15.74 | -2.70 | -4.44 | 0.39 | -0.39 | 3.12 | 1.03 |
| Simple Mom | 8.93 | 9.57 | 0.93 | -31.67 | -4.16 | -5.95 | 1.26 | -0.49 | 2.40 | 0.92 |
| PPP | 11.15 | 10.64 | 1.05 | -37.21 | -3.76 | -6.09 | 9.54 | 0.30 | 5.37 | 0.96 |
| BPPP | 12.18 | 9.24 | 1.32 | -24.50 | -3.28 | -4.85 | 6.03 | -0.11 | 1.39 | 1.25 |
| Horseshoe | 12.18 | 10.36 | 1.18 | -23.20 | -3.93 | -5.86 | 5.55 | -0.18 | 2.06 | 1.12 |

* •

  Notes: Expanding window, initial training sample 120 months (1963M7), out-of-sample period 1973M8–2023M12. Mean and volatility are annualised. MaxDD is maximum drawdown. VaR and CVaR at 95% denote Value-at-Risk and Conditional Value-at-Risk (Expected Shortfall). Turnover is average one-way per period. Sharpe (net) deducts 10 bps transaction costs per unit of one-way turnover.

By integrating over the posterior distribution of θ\theta, BPPP naturally shrinks extreme policies, dampens the effect of noisy predictors, and produces smoother portfolio dynamics. These effects are particularly pronounced in finite samples and in the presence of portfolio constraints, where estimation error can otherwise translate into excessive turnover and poor downside performance. Importantly, BPPP does not alter the underlying economic signals or the functional form of the policy rule. Instead, it modifies how uncertainty about the policy parameters is incorporated into decision making. In this sense, BPPP represents a principled extension of the PPP framework rather than an alternative modelling approach.

Proposition 1 predicts that PPP overreacts to signals, and this is most visible in turnover. PPP generates average one-way turnover of 9.54 per period, the highest of any active strategy. BPPP reduces this to 6.03 and horseshoe to 5.55. At 10 basis points per unit of one-way turnover, PPP’s net Sharpe falls from 1.05 to 0.96, while BPPP’s falls only from 1.32 to 1.25. At 50 basis points, PPP collapses to 0.60 while BPPP remains near 0.99.

The turnover difference reflects the mechanism of Proposition 1 directly. Because Σθ,τ\Sigma\_{\theta,\tau} is non-negligible relative to T/LT/L, BPPP shrinks tilts in the direction of high signal magnitude. This prevents the over-reaction to large signal realisations that drives PPP’s excessive position changes. Figure [1](https://arxiv.org/html/2602.21173v1#S5.F1 "Figure 1 ‣ 5 Empirical Results ‣ Bayesian Parametric Portfolio Policies") confirms this at the factor level. PPP tilts chase signals, generating high weight volatility. BPPP maintains a more balanced factor exposure and markedly lower time-series weight volatility across all six factors. The return distribution (Figure [A1](https://arxiv.org/html/2602.21173v1#A3.F1 "Figure A1 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies"), left panel) reflects this. PPP exhibits positive skewness (0.30) and heavy kurtosis (5.37) consistent with episodic overexposure, whereas BPPP is near-symmetric (-0.11) with lighter tails (Kurtosis of 1.39).

![Refer to caption](factor_loading_comparison.png)

Figure 1: Factor Exposures by Model

Notes: Left: average portfolio weight on each factor. Right: time-series standard deviation of factor weights. BPPP exhibits substantially lower weight volatility across all factors, consistent with the overexposure correction predicted by Proposition 1.

The mechanism operates at the signal level as well as the factor level. Appendix Figures [A6](https://arxiv.org/html/2602.21173v1#A3.F6 "Figure A6 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies")–[A8](https://arxiv.org/html/2602.21173v1#A3.F8 "Figure A8 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") display heatmaps of the largest signal–factor coefficient pairs by absolute magnitude across PPP, BPPP, and the Horseshoe. Two patterns emerge. First, all three models draw on a common pool of predictive signals. Momentum-related signals from Haddad et al. ([2020](https://arxiv.org/html/2602.21173v1#bib.bib9 "Factor timing")) and valuation-based anomalies from Chen and Zimmermann ([2022](https://arxiv.org/html/2602.21173v1#bib.bib2 "Open source cross-sectional asset pricing")) consistently rank among the most influential across specifications, suggesting that the predictive information in the signal set has systematic structure that each method detects. Second, the scale and dispersion of the largest coefficients differ markedly across methods. PPP concentrates weight on a small number of extreme loadings, a direct reflection of the overfit that Proposition 1 attributes to ignoring Σθ,τ\Sigma\_{\theta,\tau}. BPPP distributes weight more evenly, posterior averaging dilutes the contribution of any single signal realisation, shrinking extreme coefficients without eliminating them. The Horseshoe achieves the most aggressive regularization of large coefficients through its signal-specific local scales, yet, as we discuss below, without inducing the sparsity its design assumes.

The evidence bears directly on the sparse vs. dense debate in the return predictability literature (Kozak et al., [2020](https://arxiv.org/html/2602.21173v1#bib.bib20 "Shrinking the cross-section"); Gu et al., [2020](https://arxiv.org/html/2602.21173v1#bib.bib21 "Empirical asset pricing via machine learning")) and by . Under a sparse model, a small number of signals would carry all predictive information and the remainder would be driven to zero. The horseshoe shrinkage factor κ\kappa is designed precisely to discriminate signals, i.e. κk,ℓ≈0\kappa\_{k,\ell}\approx 0 indicates a surviving signal; κk,ℓ≈1\kappa\_{k,\ell}\approx 1 indicates collapse toward the prior mean. Figure [A5](https://arxiv.org/html/2602.21173v1#A3.F5 "Figure A5 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") shows that the empirical κ\kappa distribution is concentrated near zero throughout the out-of-sample period (final OOS mean ≈0.03\approx 0.03, median ≈0.02\approx 0.02, with 99.6% of coefficients below 0.3). This evidence suggests *dense* predictability, the horseshoe finds no evidence for a small dominant subset of signals. Instead, broad signal ’survival’ characterises the data. The bootstrap stability analysis of Figure [A9](https://arxiv.org/html/2602.21173v1#A3.F9 "Figure A9 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") reinforces this conclusion. Drawing 500 random subsets of 50 signals from the full 242, the distribution of mean absolute horseshoe coefficients is tightly concentrated, confirming that no small cluster of signals is the primary performance driver. This is consistent with Kozak et al. ([2020](https://arxiv.org/html/2602.21173v1#bib.bib20 "Shrinking the cross-section")) and Haddad et al. ([2020](https://arxiv.org/html/2602.21173v1#bib.bib9 "Factor timing")), who argue that factor timing predictability reflects a diffuse combination of many signals rather than a sparse set of dominant predictors. In this environment, the Gaussian prior’s uniform shrinkage is better matched to the structure of the data than the horseshoe’s sparsity assumption, which helps explain BPPP’s outperformance of the horseshoe in our sample. The relative performance of the two prior specifications is therefore informative beyond portfolio statistics. It constitutes out-of-sample evidence on the density structure of return predictability in factor timing.

Next, Proposition 1 identifies the welfare cost of PPP as the utility gap Gτ​(mτ)−𝔼θ​[Gτ​(θ)]G\_{\tau}(m\_{\tau})-\mathbb{E}\_{\theta}[G\_{\tau}(\theta)]. The empirical counterpart of this gap is the difference of certainty-equivalents. Table [A1](https://arxiv.org/html/2602.21173v1#A3.T1 "Table A1 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") reports CE returns under CRRA utility with γ=5\gamma=5. BPPP delivers an annualised CE of 10.52%, corresponding to a difference of 536 basis points relative to the market benchmark. PPP delivers a CE of 8.68%. The 184 basis point gap between BPPP and PPP in CE space is the empirical counterpart of the utility overstatement that Proposition 1 predicts. Empirical CE is computed using the exact CRRA transformation, whereas Proposition 1 uses a second-order mean-variance approximation; the correspondence is therefore economic rather than algebraically exact.

Figure [A2](https://arxiv.org/html/2602.21173v1#A3.F2 "Figure A2 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") maps all strategies in risk-return space. BPPP occupies the north-west of the frontier, combining higher return and lower volatility than PPP and the market benchmark. Figure [A3](https://arxiv.org/html/2602.21173v1#A3.F3 "Figure A3 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") shows cumulative wealth over the full out-of-sample period. With respect to tail risk, the maximum drawdown of PPP (-37.2%) is substantially larger than that of BPPP (-24.5%). This is a direct consequence of overexposure. PPP holds extreme positions precisely when signals are anomalously large, and these are often periods of elevated market stress when large tilts carry the greatest downside. BPPP’s posterior averaging dampens the response to extreme signal realisations, providing asymmetric protection against tail events. Notwithstanding, tail risk as measured by Value-at-Risk is not substantially higher. The spanning regressions in Table [4](https://arxiv.org/html/2602.21173v1#S6.T4 "Table 4 ‣ 6.1 Statistical Significance and Spanning Tests ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") confirm that BPPP generates higher benchmark-orthogonal value. Alpha is 6.86% versus 6.53% for PPP, with higher R2R^{2} (0.61 vs. 0.35), indicating that BPPP maintains meaningful market exposure while adding alpha more efficiently.

## 6 Robustness

This section is organized around five lines of enquiry. First, are performance statistics, in particular risk-adjusted returns of different methods statistically significant and do they represent genuine alpha? Second, is the welfare advantage of BPPP monotonically increasing in risk aversion as Proposition 1 predicts? Third, does the performance gap survive realistic transaction costs? Fourth, is subperiod performance consistent or driven by a episodic differences? Finally, are results sensitive to prior choices and specification.

### 6.1 Statistical Significance and Spanning Tests

A first concern is whether the performance gap between BPPP and benchmarks reported in Table [2](https://arxiv.org/html/2602.21173v1#S5.T2 "Table 2 ‣ 5 Empirical Results ‣ Bayesian Parametric Portfolio Policies") is a statistical artefact of the specific sample choice. We address this with a bootstrap Sharpe-difference test and a market-spanning regression. Table [3](https://arxiv.org/html/2602.21173v1#S6.T3 "Table 3 ‣ 6.1 Statistical Significance and Spanning Tests ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") reports Sharpe-difference tests against the market benchmark following Ledoit and Wolf ([2008](https://arxiv.org/html/2602.21173v1#bib.bib27 "Robust performance hypothesis testing with the Sharpe ratio")). Under this procedure, BPPP rejects the null of equal Sharpe ratio at the 1% level with a tt-statistic of 5.61. The Horseshoe is also strongly significant (t=4.18t=4.18). PPP is significant at the 5% level (t=2.34t=2.34) but with a bootstrap standard error roughly 30% larger than BPPP’s, reflecting the higher sampling variability of its coefficients when estimation risk is ignored. The mean-variance strategy attains marginal significance (t=1.99t=1.99).

Table 3: Bootstrap Sharpe-Difference Tests vs. Market Benchmark

| Portfolio | Sharpe Diff | Bootstrap SE | tt-stat | pp-value |
| --- | --- | --- | --- | --- |
| BPPP | 0.579 | 0.103 | 5.61 | <<0.001∗∗∗ |
| Horseshoe | 0.437 | 0.105 | 4.18 | <<0.001∗∗∗ |
| PPP | 0.309 | 0.132 | 2.34 | 0.019∗∗ |
| Mean-Var | 0.297 | 0.149 | 1.99 | 0.047∗∗ |

* •

  Notes: Null hypothesis: Sharpe ratio equals that of the market. Studentised bootstrap test of Ledoit and Wolf ([2008](https://arxiv.org/html/2602.21173v1#bib.bib27 "Robust performance hypothesis testing with the Sharpe ratio")) with block length ⌊T1/3⌋=8\lfloor T^{1/3}\rfloor=8 months. ∗∗∗, ∗∗, ∗: significant at 1%, 5%, 10%.

The pairwise BPPP vs. PPP Sharpe gap of 0.27 is directionally positive but measured with substantial noise, as both strategies exploit the same signal set and factor universe. The BPPP advantage over PPP reflects a difference in how parameter uncertainty is handled, not access to a fundamentally different information set.

Table 4: Spanning Tests: Alpha and Beta vs. Market Benchmark

| Portfolio | α\alpha (ann. %) | β\beta | tt-stat | pp-value | R2R^{2} |
| --- | --- | --- | --- | --- | --- |
| PPP | 6.53 | 0.39 | 5.27 | <<0.001∗∗∗ | 0.35 |
| BPPP | 6.86 | 0.45 | 8.20 | <<0.001∗∗∗ | 0.61 |
| Mean-Var | 4.26 | 0.24 | 5.20 | <<0.001∗∗∗ | 0.32 |
| Horseshoe | 6.44 | 0.48 | 6.52 | <<0.001∗∗∗ | 0.56 |

* •

  Notes: OLS regression of model excess returns on market excess return. Alpha annualised. tt-stats and pp-values for H0:α=0H\_{0}\!:\alpha=0.

Table [4](https://arxiv.org/html/2602.21173v1#S6.T4 "Table 4 ‣ 6.1 Statistical Significance and Spanning Tests ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") sharpens the interpretation via OLS regressions of excess returns on the market. BPPP generates an annualised alpha of 6.86% (t=8.20t=8.20), above PPP’s 6.53% (t=5.27t=5.27). Two contrasts stand out. First, BPPP’s alpha tt-statistic is 56% larger than PPP’s despite very similar point estimates. The posterior averaging reduces residual volatility, making the alpha estimate much more precise. Second, BPPP has a higher market beta (0.45 versus 0.39 for PPP) and substantially higher R2R^{2} (0.61 versus 0.35). This combination (higher systematic loading with lower residual variance) indicates that BPPP builds market exposure more deliberately. PPP’s lower R2R^{2} reflects the idiosyncratic noise introduced by extreme coefficient estimates that BPPP’s prior dampens. Crucially, BPPP’s outperformance is not achieved by tilting away from market risk. It reflects the more efficient construction of factor tilts around a stable market factor.

### 6.2 Welfare and Risk-Aversion Analysis

One of Proposition 1 predictions is that the utility gap between BPPP and PPP should grow monotonically with γ\gamma because the Jensen’s inequality bound in Equation ([7](https://arxiv.org/html/2602.21173v1#S3.E7 "In Proposition 1 ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")) scales linearly with risk aversion under a quadratic approximation (see Appendix [A](https://arxiv.org/html/2602.21173v1#A1.SSx1 "Proof of Proposition 1 ‣ Appendix A Proofs and Additional Details ‣ Bayesian Parametric Portfolio Policies") for more details). Table [5](https://arxiv.org/html/2602.21173v1#S6.T5 "Table 5 ‣ 6.2 Welfare and Risk-Aversion Analysis ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") provides a direct out-of-sample test.

Table 5: Certainty-Equivalent Returns Under Alternative Risk Aversion

|  | γ=2\gamma=2 | γ=5\gamma=5 | γ=10\gamma=10 |
| --- | --- | --- | --- |
| PPP | 10.51 | 8.68 | 5.58 |
| BPPP | 11.94 | 10.52 | 8.13 |
| Horseshoe | 11.69 | 9.90 | 6.82 |
| Benchmark | 9.62 | 5.15 | −-2.94 |

* •

  Notes: Annualised CE returns (%) under exact CRRA utility with risk aversion γ\gamma. Consistent with Proposition 1, the BPPP advantage over PPP is monotonically increasing in γ\gamma.

The evidence strongly confirms the proposition. At γ=2\gamma=2 the BPPP–PPP CE gap is 142 basis points annually (11.94% versus 10.51%). At γ=5\gamma=5 it rises to 184 basis points (10.52% versus 8.68%). At γ=10\gamma=10 it reaches 255 basis points (8.13% versus 5.58%). The monotone increase is out-of-sample evidence of the overexposure mechanism. As risk aversion rises, the investor weights large negative returns more heavily under the concave utility function, and PPP’s tendency to hold extreme positions exactly during high-signal-magnitude periods carries an increasingly large welfare cost. The Horseshoe lies between BPPP and PPP at all levels of γ\gamma, consistent with its intermediate degree of overexposure correction.

The benchmark CE trajectory is equally instructive. At γ=2\gamma=2 the benchmark delivers a CE of 9.62%, below PPP’s 10.51%. By γ=10\gamma=10, benchmark CE collapses to −-2.94%. Passive factor exposure destroys welfare because the variance penalty swamps the expected return. This provides context for interpreting the BPPP advantage under institutional risk aversion (γ\gamma = 5-10). The active correction for estimation risk is not a marginal refinement but a welfare-determining design choice. At γ\gamma = 5, the performance fee that a benchmark investor would pay to switch to BPPP is 500 basis points per annum (Table [A1](https://arxiv.org/html/2602.21173v1#A3.T1 "Table A1 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") in the appendix), compared with 331 basis points for PPP. The 169 basis-point fee difference is the monetary equivalent of the estimation-risk correction in our sample.

### 6.3 Transaction Costs and Trading Frictions

![Refer to caption](tc_sensitivity.png)

Figure 2: Net Sharpe Ratio vs. Transaction Costs

Notes: Net Sharpe ratios as a function of one-way transaction costs (0–50 bps).

The turnover advantage of BPPP translates directly into a transaction-cost advantage that widens as frictions increase. Figure [2](https://arxiv.org/html/2602.21173v1#S6.F2 "Figure 2 ‣ 6.3 Transaction Costs and Trading Frictions ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") plots net Sharpe ratios for all strategies against one-way transaction costs from 0 to 50 basis points.

At zero cost, BPPP leads PPP by 0.27 Sharpe points (1.32 versus 1.05). Far from narrowing with cost, the gap expands. At 10 bps the difference is 0.29 (1.25 versus 0.96), at 20 bps it is 0.32 (1.19 versus 0.87), at 50 bps it is 0.39 (0.99 versus 0.60). The BPPP–PPP gap is therefore strictly increasing in transaction costs, which is not mechanical. The posterior averaging that corrects overexposure simultaneously reduces the sensitivity of portfolio weights to noisy signal fluctuations, generating more persistent positions and lower rebalancing frequency. The cost advantage is a direct consequence of the same mechanism, reduced overreaction, that generates the gross Sharpe advantage.

For BPPP, the breakeven transaction cost at which the Sharpe falls below the market benchmark’s 0.74 exceeds 50 basis points, i.e., above the full 0–50 bps grid we test. For the Horseshoe, which has even lower turnover (5.55), the breakeven is similarly high.

### 6.4 Subperiod Stability and Crisis Resilience

A second concern is whether results are over-reliant on a few fortuitous subperiods. We assess this along two dimensions. Decade-by-decade analysis and crisis-episode analysis.

![Refer to caption](decade_sharpe_comparison.png)

Figure 3: Sharpe Ratios by Decade

Notes: Annualised Sharpe ratios by complete out-of-sample decade. BPPP outperforms PPP in four of five complete decades. First decade (1963–1972) excluded as it overlaps with the in-sample training window.

Figure [3](https://arxiv.org/html/2602.21173v1#S6.F3 "Figure 3 ‣ 6.4 Subperiod Stability and Crisis Resilience ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") reports Sharpe ratios by decade. BPPP outperforms PPP in four of the five complete decades. The first decade (1973–1982) is the sole exception, with BPPP Sharpe of 0.98 versus PPP’s 0.99, a negligible margin of 0.003 Sharpe points consistent with sampling variation. In all subsequent decades the advantage is unambiguous. The equity bull market of the 1980s, the technology boom and bust of the 1990s, the post-GFC recovery of the 2000s, and the most recent decade. The advantage is largest in the 2003–2012 decade, spanning the Global Financial Crisis, precisely the period where Proposition 1 predicts the largest cost of ignoring Σθ,τ\Sigma\_{\theta,\tau}. Signals were anomalously large and volatile, PPP loaded heavily on them, and the result was the deep drawdown (-37.2%) that BPPP avoided (-24.5%). Across complete decades, BPPP outperforms the market benchmark in all five, while PPP underperforms the benchmark in the most recent decade (2013–2023), confirming that factor timing adds value on average and that the BPPP correction improves robustness over time.

![Refer to caption](rolling_3y_sharpe.png)

Figure 4: Rolling 36-Month Sharpe Ratios

Notes: Rolling 36-month Sharpe ratios, 1973M8–2023M12. PPP (black dashed); BPPP (red solid).

Figure [4](https://arxiv.org/html/2602.21173v1#S6.F4 "Figure 4 ‣ 6.4 Subperiod Stability and Crisis Resilience ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") shows rolling 36-month Sharpe ratios. In calm periods, BPPP and PPP track each other closely. When signals are moderate and estimation error has limited portfolio impact, posterior averaging introduces little change relative to the plug-in estimator. During stress episodes, however, the divergence is pronounced. Both the early-2000s technology correction and the 2008–2009 financial crisis show BPPP maintaining substantially higher rolling Sharpe than PPP. This asymmetry, better performance in bad times, near parity in good times, is evidence of the mechanism in Proposition 1. The Jensen’s inequality gap scales with zτ′​Σθ,τ​zτz\_{\tau}^{\prime}\Sigma\_{\theta,\tau}z\_{\tau}, which is largest when signal magnitudes are extreme, and extreme signal episodes disproportionately coincide with financial crises.

![Refer to caption](crisis_cumulative_returns.png)

Figure 5: Cumulative Wealth During Crisis Episodes

Notes: Cumulative portfolio wealth during the GFC (left, 2006–2011) and COVID (right, 2018–2022). PPP (black dashed); BPPP (red solid).

Figure [5](https://arxiv.org/html/2602.21173v1#S6.F5 "Figure 5 ‣ 6.4 Subperiod Stability and Crisis Resilience ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") zooms into the two major crisis episodes. During the GFC window (2006–2011), BPPP achieves a Sharpe of 0.56 versus 0.33 for PPP, a 71% relative improvement with a materially smaller drawdown. The GFC is a particularly demanding test because factor signal dispersion was unusually high in the pre-crisis period and PPP loaded aggressively on those signals. BPPP’s posterior averaging compressed the tilts, preventing the losses that large leveraged factor positions incurred as the crisis unfolded. During the COVID shock (2018–2022), BPPP leads with 0.89 versus 0.66. The COVID episode differs in character. The signal dislocation was sharper but more transient. The BPPP advantage here reflects faster mean-reversion of portfolio weights after the initial shock, consistent with the reduced sensitivity to large individual signal realisations that posterior averaging produces.

The drawdown profile (Figure [A4](https://arxiv.org/html/2602.21173v1#A3.F4 "Figure A4 ‣ Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies") in the appendix) confirms the picture at the path level. BPPP’s maximum drawdown of -24.5% is 12.7 percentage points smaller than PPP’s -37.2%, and the recovery from the 2008 trough is faster. The normal Q-Q plot in the same figure shows PPP’s return distribution has materially heavier left tails than the normal, while BPPP’s tails are near-Gaussian, consistent with the excess kurtosis of 1.39 versus 5.37 for PPP reported in Table [2](https://arxiv.org/html/2602.21173v1#S5.T2 "Table 2 ‣ 5 Empirical Results ‣ Bayesian Parametric Portfolio Policies"). Together, the crisis and drawdown evidence confirms the third implication of Proposition 1, that PPP systematically understates portfolio risk via the estimation-risk term in Equation ([8](https://arxiv.org/html/2602.21173v1#S3.E8 "In 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")), and the downside consequences are concentrated in exactly the episodes where estimation risk is most consequential.

### 6.5 Prior Sensitivity and Dynamic Prior Mean

The BPPP framework requires two specification choices. The target-tilt standard deviation δ\delta, which governs prior tightness, and whether the prior mean is set dynamically (Mt=θ^t−1M\_{t}=\hat{\theta}\_{t-1}) or held fixed at zero (Mt=0M\_{t}=0), an alternative and legitimate choice. Table [6](https://arxiv.org/html/2602.21173v1#S6.T6 "Table 6 ‣ 6.5 Prior Sensitivity and Dynamic Prior Mean ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies") reports the full sensitivity grid across δ∈{0.35,0.50,0.70,0.90}\delta\in\{0.35,0.50,0.70,0.90\} with both prior-mean settings. The range spans from a tight prior (δ=0.35\delta=0.35, ν≈0.0015\nu\approx 0.0015) to a loose one (δ=0.90\delta=0.90, ν≈0.010\nu\approx 0.010), a roughly sevenfold increase in prior variance.

Table 6: BPPP Prior Sensitivity Study

| δ\delta | Dynamic MtM\_{t} | Sharpe | CE (%) | Turnover | Mean tilt norm | Mean |θ||\theta| |
| --- | --- | --- | --- | --- | --- | --- |
| 0.35 | No | 1.147 | 8.205 | 3.76 | 0.567 | 0.0105 |
| 0.35 | Yes | 1.318 | 10.517 | 6.03 | 0.661 | 0.0263 |
| 0.50 | No | 1.053 | 7.025 | 2.31 | 0.536 | 0.0137 |
| 0.50 | Yes | 1.313 | 9.850 | 5.24 | 0.640 | 0.0346 |
| 0.70 | No | 1.032 | 6.645 | 1.63 | 0.544 | 0.0144 |
| 0.70 | Yes | 1.308 | 9.418 | 4.56 | 0.627 | 0.0418 |
| 0.90 | No | 1.055 | 6.688 | 1.46 | 0.557 | 0.0146 |
| 0.90 | Yes | 1.288 | 9.050 | 4.21 | 0.626 | 0.0518 |

* •

  Notes: BPPP sensitivity across target-tilt standard deviation δ\delta and dynamic-prior-mean setting. “Dynamic MtM\_{t}” sets the prior mean to the previous period’s MAP estimate. Turnover is annualised one-way. Mean |θ||\theta| and mean tilt norm are structural diagnostics.

#### Sensitivity to prior tightness (δ\delta).

Across the static specification, Sharpe ratios range from 1.032 to 1.147 as δ\delta varies from 0.70 to 0.35, a variation of less than 0.12 over a sevenfold change in prior variance. CE returns span 6.6% to 8.2%. The insensitivity is structural. As δ\delta rises from 0.35 to 0.90, mean |θ||\theta| nearly doubles (0.010 to 0.015) and tilt norms also rise. Once the constraints bind regularly, loosening the prior buys coefficient freedom that the portfolio construction step absorbs without converting to proportionally larger active positions. This insensitivity is reassuring since within a broad range, the prior-tightness choice does not materially change the results.

#### The role of the dynamic prior mean.

The dynamic prior mean (Mt=θ^t−1M\_{t}=\hat{\theta}\_{t-1}) has a first-order effect across every value of δ\delta. Switching from static to dynamic adds approximately 0.17–0.28 Sharpe points and 2.3–2.8 percentage points of annualised CE. At the baseline δ=0.35\delta=0.35, the dynamic prior increases Sharpe from 1.147 to 1.318 and CE from 8.2% to 10.5%. This is the largest single performance differential in the sensitivity grid, larger than any choice of δ\delta within either specification.

The economic mechanism is important to understand. When Mt=θ^t−1M\_{t}=\hat{\theta}\_{t-1}, the prior penalises deviations from the investor’s recent coefficient estimate rather than from zero. This anchors each period’s MAP to the previous solution, providing coefficient-level inertia that complements the posterior averaging over policy uncertainty. Specifically, it prevents the MAP from jumping to an extreme solution when a new data point arrives with anomalously large signals, because the prior cost of moving far from θ^t−1\hat{\theta}\_{t-1} is substantial. The result is lower within-period coefficient volatility and smoother portfolio dynamics over time.

The apparent paradox, that turnover is *higher* under the dynamic prior (6.03) than the static one (3.76) at δ=0.35\delta=0.35, resolves on inspection. The static prior (Mt=0M\_{t}=0) strongly attracts the MAP toward the origin in every period, compressing all tilts toward the benchmark and limiting the model’s ability to maintain persistent non-zero positions. The dynamic prior allows the MAP to track a slowly evolving signal environment, maintaining persistent tilts that accumulate across periods. These persistent tilts imply higher coefficient magnitude, higher tilt norms, and higher one-way turnover as positions are adjusted at each rebalancing date. The static specification’s lower turnover therefore reflects over-shrinkage toward zero, a conservative stance that sacrifices the information in persistent signals, rather than efficient portfolio allocation. The CE gap of over 2 percentage points per annum documents the welfare cost of that conservatism.

#### Horseshoe prior specification.

As discussed in Section [5](https://arxiv.org/html/2602.21173v1#S5 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies"), the horseshoe’s underperformance relative to BPPP (Sharpe 1.18 versus 1.32) reflects a prior misalignment. The κ\kappa distribution is concentrated near zero throughout the out-of-sample period, indicating that broad signal survival (not sparse selection) characterises the data. The horseshoe’s sparsity assumption is at odds with the dense predictability structure documented in the signal-level analysis, and the Gaussian prior is the better-calibrated specification for this environment. We treat the prior comparison as empirical evidence on the structure of factor-timing predictability rather than a definitive finding about priors in general, settings with genuinely sparse predictability could favour the horseshoe.

## 7 Conclusion

Parametric Portfolio Policies offer a powerful and flexible framework for dynamic asset allocation, but ignore policy uncertainty. Our key proposition formalises the consequences and shows that, because portfolio weights are linear in policy parameters and utility is concave, PPP systematically overstates achievable expected utility by an amount proportional to parameter uncertainty and signal scale. The correction is not a heuristic. It follows from Jensen’s inequality applied to the posterior distribution of policy parameters.

Bayesian Parametric Portfolio Policies implement a corrected decision rule by integrating expected utility over this posterior. The correction arises by default, requiring no additional modelling of returns, and adds negligible computational cost. The prior controls the scale of posterior uncertainty and the degree of overexposure correction. Tighter priors impose larger corrections, translating into lower turnover and more stable weights.

Our empirical results confirm each prediction of the theory. BPPP delivers a gross Sharpe ratio of 1.32 versus 1.05 for PPP and 0.74 for the market. The certainty-equivalent difference is 536 basis points (BPPP) versus 353 basis points (PPP), a 184 basis point premium that represents the empirical counterpart of the utility overstatement in our key proposition. The gap grows with risk aversion, is largest during crisis episodes, and remains strong across decades (BPPP leads PPP in four of five complete decades). At 50 basis points of transaction costs, BPPP retains a net Sharpe of 0.99 while PPP collapses to 0.60.

A further finding is that the structure of predictability in factor timing appears diffuse rather than sparse. Most of the 242 signals are not strongly shrunk and appear to contribute jointly in our sample, favouring uniform Gaussian shrinkage over the horseshoe’s sparse-signal design. We treat this as robust empirical evidence for this setting, while leaving broader prior-selection comparisons to future work.

Several extensions are natural. Replacing the isotropic Gaussian prior with a structured prior that accounts for cross-signal correlations would allow for more targeted overexposure correction in directions of high uncertainty. Extending BPPP to individual equities would test scalability at much larger KK. Sequential Bayesian updating across windows would allow the posterior to adapt to structural breaks in factor dynamics without restarting from scratch.

## References

* R. D. Arnott, C. R. Harvey, V. Kalesnik, and J. T. Linnainmaa (2019)
  Alice’s adventures in factorland: three blunders that plague factor investing.
  The Journal of Portfolio Management 45 (4),  pp. 18–36.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2019.45.4.018)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* D. Avramov and G. Zhou (2010)
  Bayesian portfolio analysis.
  Annual Review of Financial Economics 2 (1),  pp. 25–47.
  External Links: [Document](https://dx.doi.org/10.1146/annurev-financial-120209-133947)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* N. Barberis (2000)
  Investing for the long run when returns are predictable.
  The Journal of Finance 55 (1),  pp. 225–264.
  External Links: [Document](https://dx.doi.org/10.1111/0022-1082.00205)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p5.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* P. G. Bissiri, C. C. Holmes, and S. G. Walker (2016)
  A general framework for updating belief distributions.
  Journal of the Royal Statistical Society: Series B (Statistical Methodology) 78 (5),  pp. 1103–1130.
  External Links: [Document](https://dx.doi.org/10.1111/rssb.12158)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p5.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§3](https://arxiv.org/html/2602.21173v1#S3.p1.7 "3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies").
* M. W. Brandt, P. Santa-Clara, and R. Valkanov (2009)
  Parametric portfolio policies: exploiting characteristics in the cross-section of equity returns.
  Review of Financial Studies 22 (9),  pp. 3411–3447.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhp003),
  ISSN 08939454
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p1.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§2](https://arxiv.org/html/2602.21173v1#S2.p1.12 "2 Setup and Motivation ‣ Bayesian Parametric Portfolio Policies"),
  [§5](https://arxiv.org/html/2602.21173v1#S5.p1.2 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies").
* M. W. Brandt and P. Santa-Clara (2006)
  Dynamic portfolio selection by augmenting the asset space.
  The Journal of Finance 61 (5),  pp. 2187–2217.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.2006.01055.x)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* C. M. Carvalho, N. G. Polson, and J. G. Scott (2010)
  The horseshoe estimator for sparse signals.
  Biometrika 97 (2),  pp. 465–480.
  External Links: [Document](https://dx.doi.org/10.1093/biomet/asq017)
  Cited by: [§3.1](https://arxiv.org/html/2602.21173v1#S3.SS1.p2.8 "3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies").
* A. Y. Chen and T. Zimmermann (2022)
  Open source cross-sectional asset pricing.
  Critical Finance Review 27 (2),  pp. 207–264.
  Note: Data available at <https://www.openassetpricing.com/>
  Cited by: [Appendix C](https://arxiv.org/html/2602.21173v1#A3.7.6.6.6 "Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p1.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p4.2 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§4](https://arxiv.org/html/2602.21173v1#S4.p2.1 "4 Data ‣ Bayesian Parametric Portfolio Policies"),
  [§5](https://arxiv.org/html/2602.21173v1#S5.p5.1 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies").
* V. DeMiguel, L. Garlappi, and R. Uppal (2009)
  Optimal versus naive diversification: how inefficient is the 1/N portfolio strategy?.
  The Review of Financial Studies 22 (5),  pp. 1915–1953.
  External Links: ISSN 0893-9454,
  [Document](https://dx.doi.org/10.1093/rfs/hhm075)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p1.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* E. F. Fama and K. R. French (2015)
  A five-factor asset pricing model.
  Journal of Financial Economics 116 (1),  pp. 1–22.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2014.10.010)
  Cited by: [§5](https://arxiv.org/html/2602.21173v1#S5.p1.2 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies").
* L. Garlappi, R. Uppal, and T. Wang (2007)
  Portfolio selection with parameter and model uncertainty: a multi-prior approach.
  The Review of Financial Studies 20 (1),  pp. 41–81.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhj003)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* J. Green, J. R. M. Hand, and X. F. Zhang (2017)
  The characteristics that provide independent information about average U.S. monthly stock returns.
  The Review of Financial Studies 30 (12),  pp. 4389–4436.
  External Links: ISSN 0893-9454,
  [Document](https://dx.doi.org/10.1093/rfs/hhx019)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p1.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* S. Gu, B. Kelly, and D. Xiu (2020)
  Empirical asset pricing via machine learning.
  The Review of Financial Studies 33 (5),  pp. 2223–2273.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhaa009)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p1.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§5](https://arxiv.org/html/2602.21173v1#S5.p6.6 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies").
* V. Haddad, S. Kozak, and S. Santosh (2020)
  Factor timing.
  The Review of Financial Studies 33 (5),  pp. 1980–2018.
  External Links: ISSN 0893-9454,
  [Document](https://dx.doi.org/10.1093/rfs/hhaa017)
  Cited by: [Appendix C](https://arxiv.org/html/2602.21173v1#A3.7.6.6.6 "Appendix C Additional Tables and Figures ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p1.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p4.2 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§4](https://arxiv.org/html/2602.21173v1#S4.p2.1 "4 Data ‣ Bayesian Parametric Portfolio Policies"),
  [§5](https://arxiv.org/html/2602.21173v1#S5.p5.1 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies"),
  [§5](https://arxiv.org/html/2602.21173v1#S5.p6.6 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies").
* A. Ilmanen, R. Israel, T. J. Moskowitz, A. K. Thapar, and F. Wang (2021)
  Factor premia and factor timing: a century of evidence.
  Journal of Alternative Investments 24 (3),  pp. 5–24.
  External Links: [Document](https://dx.doi.org/10.3905/jai.2021.1.131)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* S. Kandel and R. F. Stambaugh (1996)
  On the predictability of stock returns: an asset-allocation perspective.
  The Journal of Finance 51 (2),  pp. 385–424.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1996.tb02689.x)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p5.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* R. S. J. Koijen, T. J. Moskowitz, L. H. Pedersen, and E. B. Vrugt (2018)
  Carry.
  Journal of Financial Economics 127 (2),  pp. 197–225.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2017.11.002)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* S. Kozak, S. Nagel, and S. Santosh (2020)
  Shrinking the cross-section.
  Journal of Financial Economics 135 (2),  pp. 271–292.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2019.06.008)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies"),
  [§5](https://arxiv.org/html/2602.21173v1#S5.p6.6 "5 Empirical Results ‣ Bayesian Parametric Portfolio Policies").
* O. Ledoit and M. Wolf (2008)
  Robust performance hypothesis testing with the Sharpe ratio.
  Journal of Empirical Finance 15 (5),  pp. 850–859.
  External Links: [Document](https://dx.doi.org/10.1016/j.jempfin.2008.03.002)
  Cited by: [1st item](https://arxiv.org/html/2602.21173v1#S6.I1.i1.p1.4 "In Table 3 ‣ 6.1 Statistical Significance and Spanning Tests ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies"),
  [§6.1](https://arxiv.org/html/2602.21173v1#S6.SS1.p1.4 "6.1 Statistical Significance and Spanning Tests ‣ 6 Robustness ‣ Bayesian Parametric Portfolio Policies").
* Ľ. Pástor and R. F. Stambaugh (2000)
  Comparing asset pricing models: an investment perspective.
  Journal of Financial Economics 56 (3),  pp. 335–381.
  External Links: [Document](https://dx.doi.org/10.1016/S0304-405X%2800%2900044-1)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p5.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* J. Piironen and A. Vehtari (2017)
  Sparsity information and regularization in the horseshoe and other shrinkage priors.
  Electronic Journal of Statistics 11 (2),  pp. 5018–5051.
  External Links: [Document](https://dx.doi.org/10.1214/17-EJS1337SI)
  Cited by: [§3.1](https://arxiv.org/html/2602.21173v1#S3.SS1.p2.4 "3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies"),
  [§3.1](https://arxiv.org/html/2602.21173v1#S3.SS1.p2.8 "3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies").
* J. Tu and G. Zhou (2011)
  Markowitz meets talmud: a combination of sophisticated and naive diversification strategies.
  Journal of Financial Economics 99 (1),  pp. 204–215.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2010.08.013)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").
* Y. Wang, H. Gao, C. R. Harvey, Y. Liu, and X. Tao (2026)
  Machine learning meets Markowitz.
  Working Paper
  Technical Report 34861, National Bureau of Economic Research.
  External Links: [Document](https://dx.doi.org/10.3386/w34861)
  Cited by: [§1](https://arxiv.org/html/2602.21173v1#S1.p6.1 "1 Introduction ‣ Bayesian Parametric Portfolio Policies").

## Appendix A Proofs and Additional Details

### Proof of Proposition 1

We prove the two claims in turn.

Part 1: Jensen’s inequality bound (Equation [6](https://arxiv.org/html/2602.21173v1#S3.E6 "In Proposition 1 ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")).

Recall that portfolio weights are linear in θ\theta:

|  |  |  |
| --- | --- | --- |
|  | wτ​(θ)=wb+θ​zτ,w\_{\tau}(\theta)=w\_{b}+\theta z\_{\tau}, |  |

so the portfolio return rp,τ+1​(θ)=wτ​(θ)′​Rτ+1r\_{p,\tau+1}(\theta)=w\_{\tau}(\theta)^{\prime}R\_{\tau+1} is linear
in θ\theta for any fixed (zτ,Rτ+1)(z\_{\tau},R\_{\tau+1}). We define

|  |  |  |
| --- | --- | --- |
|  | Gτ​(θ)=𝔼τ​[U​(wτ​(θ)′​Rτ+1)],G\_{\tau}(\theta)=\mathbb{E}\_{\tau}\!\left[U\!\left(w\_{\tau}(\theta)^{\prime}R\_{\tau+1}\right)\right], |  |

where the expectation is taken over the distribution of Rτ+1R\_{\tau+1} conditional on
information at τ\tau. Because rp,τ+1​(θ)r\_{p,\tau+1}(\theta) is linear in θ\theta and UU is strictly concave,
Gτ​(θ)G\_{\tau}(\theta) is strictly concave in θ\theta. Thus, applying Jensen’s inequality to the concave function Gτ​(⋅)G\_{\tau}(\cdot)
and the posterior distribution p​(θ∣𝒟Tτ)p(\theta\mid\mathcal{D}\_{T\_{\tau}}) yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼θ|𝒟Tτ​[Gτ​(θ)]≤Gτ​(𝔼θ|𝒟Tτ​[θ])=Gτ​(m).\mathbb{E}\_{\theta|\mathcal{D}\_{T\_{\tau}}}\!\left[G\_{\tau}(\theta)\right]\;\leq\;G\_{\tau}\!\left(\mathbb{E}\_{\theta|\mathcal{D}\_{T\_{\tau}}}[\theta]\right)\;=\;G\_{\tau}(m). |  |

Since UU is *strictly* concave and Σθ≠0\Sigma\_{\theta}\neq 0, the inequality is strict

|  |  |  |
| --- | --- | --- |
|  | 𝔼θ|𝒟Tτ[Gτ(θ)]<Gτ(m).■\mathbb{E}\_{\theta|\mathcal{D}\_{T\_{\tau}}}\!\left[G\_{\tau}(\theta)\right]\;<\;G\_{\tau}(m).\qquad\blacksquare |  |

Part 2: Second-order approximation (Equation [7](https://arxiv.org/html/2602.21173v1#S3.E7 "In Proposition 1 ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")).

Take a second-order Taylor expansion of Gτ​(θ)G\_{\tau}(\theta) around
θ=m\theta=m which returns

|  |  |  |
| --- | --- | --- |
|  | Gτ​(θ)≈Gτ​(m)+∇θGτ​(m)′​vec​(θ−m)+12​vec​(θ−m)′​∇θ2Gτ​(m)​vec​(θ−m).G\_{\tau}(\theta)\;\approx\;G\_{\tau}(m)+\nabla\_{\theta}G\_{\tau}(m)^{\prime}\,\mathrm{vec}(\theta-m)+\tfrac{1}{2}\,\mathrm{vec}(\theta-m)^{\prime}\,\nabla^{2}\_{\theta}G\_{\tau}(m)\,\mathrm{vec}(\theta-m). |  |

Taking expectations over the posterior p​(θ∣𝒟T)p(\theta\mid\mathcal{D}\_{T}) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼θ|𝒟T​[Gτ​(θ)]\displaystyle\mathbb{E}\_{\theta|\mathcal{D}\_{T}}\!\left[G\_{\tau}(\theta)\right] | ≈Gτ​(m)+∇θGτ​(m)′​𝔼​[vec​(θ−m)]⏟= 0+12​𝔼​[vec​(θ−m)′​∇θ2Gτ​(m)​vec​(θ−m)]\displaystyle\;\approx\;G\_{\tau}(m)+\nabla\_{\theta}G\_{\tau}(m)^{\prime}\,\underbrace{\mathbb{E}[\mathrm{vec}(\theta-m)]}\_{=\,0}+\tfrac{1}{2}\,\mathbb{E}\!\left[\mathrm{vec}(\theta-m)^{\prime}\,\nabla^{2}\_{\theta}G\_{\tau}(m)\,\mathrm{vec}(\theta-m)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Gτ​(m)+12​tr⁡(∇θ2Gτ​(m)​Σθ),\displaystyle\;=\;G\_{\tau}(m)+\tfrac{1}{2}\operatorname{tr}\!\left(\nabla^{2}\_{\theta}G\_{\tau}(m)\,\Sigma\_{\theta}\right), |  |

where the second step uses the trace identity
𝔼​[v′​A​v]=tr⁡(A​𝔼​[v​v′])\mathbb{E}[v^{\prime}Av]=\operatorname{tr}(A\,\mathbb{E}[vv^{\prime}]) together with
𝔼​[vec​(θ−m)​vec​(θ−m)′]=Σθ\mathbb{E}[\mathrm{vec}(\theta-m)\,\mathrm{vec}(\theta-m)^{\prime}]=\Sigma\_{\theta}.
Rearranging yields

|  |  |  |
| --- | --- | --- |
|  | Gτ(m)−𝔼θ|𝒟T[Gτ(θ)]≈−12tr(∇θ2Gτ(m)Σθ).■G\_{\tau}(m)-\mathbb{E}\_{\theta|\mathcal{D}\_{T}}\!\left[G\_{\tau}(\theta)\right]\;\approx\;-\tfrac{1}{2}\operatorname{tr}\!\left(\nabla^{2}\_{\theta}G\_{\tau}(m)\,\Sigma\_{\theta}\right).\qquad\blacksquare |  |

### Proof of the Variance Decomposition

Proof. The portfolio return is
rp,τ+1​(θ)=(wb+θ​zτ)′​Rτ+1r\_{p,\tau+1}(\theta)=\left(w\_{b}+\theta z\_{\tau}\right)^{\prime}R\_{\tau+1}.
Treat θ\theta as random with posterior mean mm and covariance Σθ\Sigma\_{\theta},
independent of the future return Rτ+1R\_{\tau+1} conditional on the information set
𝒟T\mathcal{D}\_{T}.222This conditional independence holds because Rτ+1R\_{\tau+1}
is a future realisation not contained in the estimation sample 𝒟T\mathcal{D}\_{T}.
Apply the law of total variance with respect to the joint processes
(θ,Rτ+1)(\theta,R\_{\tau+1})

|  |  |  |
| --- | --- | --- |
|  | Var⁡(rp,τ+1)=𝔼θ​[VarR⁡(rp,τ+1∣θ)]+Varθ⁡(𝔼R​[rp,τ+1∣θ]).\operatorname{Var}(r\_{p,\tau+1})\;=\;\mathbb{E}\_{\theta}\!\left[\operatorname{Var}\_{R}\!\left(r\_{p,\tau+1}\mid\theta\right)\right]\;+\;\operatorname{Var}\_{\theta}\!\left(\mathbb{E}\_{R}\!\left[r\_{p,\tau+1}\mid\theta\right]\right). |  |

The first term is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼θ​[VarR⁡(rp,τ+1∣θ)]\displaystyle\mathbb{E}\_{\theta}\!\left[\operatorname{Var}\_{R}(r\_{p,\tau+1}\mid\theta)\right] | =𝔼θ​[VarR⁡((wb+θ​zτ)′​Rτ+1)]\displaystyle=\mathbb{E}\_{\theta}\!\left[\operatorname{Var}\_{R}\!\left(\left(w\_{b}+\theta z\_{\tau}\right)^{\prime}R\_{\tau+1}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼θ​[(wb+θ​zτ)′​Ω​(wb+θ​zτ)],\displaystyle=\mathbb{E}\_{\theta}\!\left[\left(w\_{b}+\theta z\_{\tau}\right)^{\prime}\Omega\left(w\_{b}+\theta z\_{\tau}\right)\right], |  |

where Ω=Var⁡(Rτ+1)\Omega=\operatorname{Var}(R\_{\tau+1}). This is the market-risk term in Equation ([8](https://arxiv.org/html/2602.21173v1#S3.E8 "In 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")).

For the second term (estimation risk), write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼R​[rp,τ+1∣θ]\displaystyle\mathbb{E}\_{R}[r\_{p,\tau+1}\mid\theta] | =(wb+θ​zτ)′​μτ+1,μτ+1=𝔼​[Rτ+1].\displaystyle=\left(w\_{b}+\theta z\_{\tau}\right)^{\prime}\mu\_{\tau+1},\quad\mu\_{\tau+1}=\mathbb{E}[R\_{\tau+1}]. |  |

This is linear in θ\theta, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | Varθ⁡(𝔼R​[rp,τ+1∣θ])\displaystyle\operatorname{Var}\_{\theta}\!\left(\mathbb{E}\_{R}[r\_{p,\tau+1}\mid\theta]\right) | =Varθ⁡(zτ′​θ′​μτ+1)\displaystyle=\operatorname{Var}\_{\theta}\!\left(z\_{\tau}^{\prime}\theta^{\prime}\mu\_{\tau+1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μτ+1′​Var⁡(θ​zτ)​μτ+1\displaystyle=\mu\_{\tau+1}^{\prime}\operatorname{Var}(\theta z\_{\tau})\,\mu\_{\tau+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μτ+1′​(zτ′​Σθ​zτ)​IK​μτ+1\displaystyle=\mu\_{\tau+1}^{\prime}\!\left(z\_{\tau}^{\prime}\Sigma\_{\theta}z\_{\tau}\right)I\_{K}\,\mu\_{\tau+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =zτ′​Σθ​zτ⋅‖μτ+1‖2.\displaystyle=z\_{\tau}^{\prime}\Sigma\_{\theta}z\_{\tau}\cdot\|\mu\_{\tau+1}\|^{2}. |  |

The third equality uses the separable covariance structure assumed throughout i.e. Var⁡(θ​zτ)=(zτ′​Σθ​zτ)​IK\operatorname{Var}(\theta z\_{\tau})=\left(z\_{\tau}^{\prime}\Sigma\_{\theta}z\_{\tau}\right)I\_{K}.
This yields the exact estimation-risk term used in Equation ([8](https://arxiv.org/html/2602.21173v1#S3.E8 "In 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies"))

|  |  |  |
| --- | --- | --- |
|  | Varθ⁡(𝔼R​[rp,τ+1∣θ])=zτ′​Σθ​zτ⋅‖μτ+1‖2.\operatorname{Var}\_{\theta}\!\left(\mathbb{E}\_{R}[r\_{p,\tau+1}\mid\theta]\right)=z\_{\tau}^{\prime}\Sigma\_{\theta}z\_{\tau}\cdot\|\mu\_{\tau+1}\|^{2}. |  |

Combining both terms

|  |  |  |
| --- | --- | --- |
|  | Var⁡(rp,τ+1)=𝔼θ​[VarR⁡(rp,τ+1∣θ)]+zτ′​Σθ​zτ⋅‖μτ+1‖2.\operatorname{Var}(r\_{p,\tau+1})=\mathbb{E}\_{\theta}\!\left[\operatorname{Var}\_{R}(r\_{p,\tau+1}\mid\theta)\right]+z\_{\tau}^{\prime}\Sigma\_{\theta}z\_{\tau}\cdot\|\mu\_{\tau+1}\|^{2}. |  |

The first term is market risk integrated over policy uncertainty. The second term is additional variance induced by uncertainty in θ\theta, proportional to the quadratic form
zτ′​Σθ​zτz\_{\tau}^{\prime}\Sigma\_{\theta}z\_{\tau}. PPP sets Σθ=0\Sigma\_{\theta}=0 and therefore ignores
this term entirely, systematically understating portfolio risk whenever
Σθ≠0\Sigma\_{\theta}\neq 0.

## Appendix B Estimation

We solve for θ^t\hat{\theta}\_{t} via maximum a posteriori (MAP) estimation

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^t=arg⁡maxθ⁡{∑s=1TU​(ws​(θ)′​Rs+1)−12​ν​‖θ−Mt‖F2}.\hat{\theta}\_{t}=\arg\max\_{\theta}\left\{\sum\_{s=1}^{T}U\!\left(w\_{s}(\theta)^{\prime}R\_{s+1}\right)-\frac{1}{2\nu}\|\theta-M\_{t}\|\_{F}^{2}\right\}. |  | (13) |

The penalty term in Equation ([13](https://arxiv.org/html/2602.21173v1#A2.E13 "In Appendix B Estimation ‣ Bayesian Parametric Portfolio Policies")) is the log-prior contribution. It shrinks θ^t\hat{\theta}\_{t} toward the prior mean MtM\_{t} with strength 1/ν1/\nu, providing regularisation that reduces estimation variance. The PPP benchmark is the limiting case ν→∞\nu\to\infty, in which the prior is uninformative and estimation risk is ignored as discussed in Proposition 1.

The portfolio return at each in-sample date ss is rp,s=ws​(θ)′​Rs+1r\_{p,s}=w\_{s}(\theta)^{\prime}R\_{s+1}, where ws​(θ)=Π​(wb+θ​zs)w\_{s}(\theta)=\Pi(w\_{b}+\theta z\_{s}) and Π​(⋅)\Pi(\cdot) bounds each position to the feasible set 𝒲\mathcal{W}. Because Π\Pi is piecewise linear and differentiable, we apply the straight-through estimator and pass gradients given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ℒt∂θk,ℓ=∑s=1Tt(1+rp,s)−γ​Rs+1,k​zs,ℓ​ 1​{k∈𝒜s}−θk,ℓ−[Mt]k,ℓν,\frac{\partial\mathcal{L}\_{t}}{\partial\theta\_{k,\ell}}=\sum\_{s=1}^{T\_{t}}(1+r\_{p,s})^{-\gamma}\,R\_{s+1,k}\,z\_{s,\ell}\,\mathbf{1}\!\left\{k\in\mathcal{A}\_{s}\right\}\;-\;\frac{\theta\_{k,\ell}-[M\_{t}]\_{k,\ell}}{\nu}, |  | (14) |

where 𝒜s⊆{1,…,K}\mathcal{A}\_{s}\subseteq\{1,\ldots,K\} denotes the set of assets at date ss and (1+rp,s)−γ=U′​(rp,s)(1+r\_{p,s})^{-\gamma}=U^{\prime}(r\_{p,s}) is the CRRA marginal utility. The full gradient matrix is supplied analytically to standard L-BFGS-B optimization routine, which handles box constraints via projected quasi-Newton steps.

Given θ^t\hat{\theta}\_{t}, we form a diagonal Gaussian approximation to the posterior. The diagonal of the Hessian of the negative log-posterior at θ^t\hat{\theta}\_{t} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | [Ht]k,ℓ=∑s=1Ttγ​(1+rp,s)−(γ+1)​Rs+1,k2​zs,ℓ2​ 1​{k∈𝒜s}+1ν,[H\_{t}]\_{k,\ell}=\sum\_{s=1}^{T\_{t}}\gamma\,(1+r\_{p,s})^{-(\gamma+1)}\,R\_{s+1,k}^{2}\,z\_{s,\ell}^{2}\,\mathbf{1}\!\left\{k\in\mathcal{A}\_{s}\right\}\;+\;\frac{1}{\nu}, |  | (15) |

with posterior variance vk,ℓ=[Ht]k,ℓ−1v\_{k,\ell}=[H\_{t}]\_{k,\ell}^{-1}. We draw MM perturbations and average the implied portfolio weights as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | wτBPPP=1M​∑m=1Mwτ​(θ^t+ϵ(m)),ϵ(m)∼𝒩​(0,diag⁡(vt)),w\_{\tau}^{\text{BPPP}}=\frac{1}{M}\sum\_{m=1}^{M}w\_{\tau}\!\left(\hat{\theta}\_{t}+\epsilon^{(m)}\right),\qquad\epsilon^{(m)}\sim\mathcal{N}\!\left(0,\operatorname{diag}(v\_{t})\right), |  | (16) |

where vtv\_{t} collects all vk,ℓv\_{k,\ell} into a matrix of the same shape as θ\theta. The Laplace approximation requires one MAP optimisation per rebalancing date, followed by MM inexpensive Gaussian draws and linear weight evaluations, keeping the exercise feasible in the high-dimensional setting. Full Bayesian inference via Markov-Chain Monte Carlo is computationally prohibitive when K×LK\times L parameters are updated monthly over a 50-year sample.

Next, weights are projected onto the feasible set 𝒲\mathcal{W} after averaging. All strategies share identical constraints. Individual positions are capped at ±60%\pm 60\% (long or short any single factor) and gross exposure is bounded at 200% of capital. These constraints are the same across PPP and BPPP, so any performance difference reflects estimation-risk correction alone, not differential access to leverage. Both strategies rebalance monthly when conducting the out-of-sample exercise.

The out-of-sample evaluation uses an expanding estimation window with an initial length of T0=120T\_{0}=120 months. At each subsequent rebalancing date tt, all available history up to month tt is used for MAP estimation, with the previous period’s θ^t−1\hat{\theta}\_{t-1} serving as a warm start for L-BFGS-B. The prior variance νt\nu\_{t} follows Equation ([10](https://arxiv.org/html/2602.21173v1#S3.E10 "In 3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")), growing with the window length so that the prior becomes progressively less restrictive as evidence accumulates relative to the signal dimension LL. The prior mean is set to Mt=θ^t−1M\_{t}=\hat{\theta}\_{t-1} throughout (Section [3.1](https://arxiv.org/html/2602.21173v1#S3.SS1 "3.1 The role of the Prior ‣ 3 Bayesian Parametric Portfolio Policies ‣ Bayesian Parametric Portfolio Policies")), so that regularisation penalises deviations from the previous period’s policy rather than from zero. This dynamic prior mean implements Bayesian shrinkage toward the investor’s recent policy experience, providing a natural form of continuity in portfolio construction without hard constraints on turnover.

### B.1 Estimation with a Horseshoe Prior

Estimation alternates MAP updates over (θ,σ2,τ,{λℓ,k})(\theta,\sigma^{2},\tau,\{\lambda\_{\ell,k}\}), using the same portfolio objective and constraint pipeline as PPP and BPPP. The regularised local variance of the horseshoe prior,

|  |  |  |
| --- | --- | --- |
|  | λ~ℓ,k2=c2​λℓ,k2​τ2c2+λℓ,k2​τ2,\tilde{\lambda}\_{\ell,k}^{2}=\frac{c^{2}\lambda\_{\ell,k}^{2}\tau^{2}}{c^{2}+\lambda\_{\ell,k}^{2}\tau^{2}}, |  |

alternatives between harder shrinkage when the product λℓ,k​τ\lambda\_{\ell,k}\tau is small and the slab when it is large. Conditional on the current scales, the θ\theta-step minimises the negative log-posterior

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^t=arg⁡maxθ⁡{U¯​(θ)−12​T​∑k,ℓ(θk,ℓ−Mk,ℓ)2λ~ℓ,k2},\hat{\theta}\_{t}=\arg\max\_{\theta}\left\{\,\bar{U}(\theta)-\frac{1}{2T}\sum\_{k,\ell}\frac{(\theta\_{k,\ell}-M\_{k,\ell})^{2}}{\tilde{\lambda}\_{\ell,k}^{2}}\right\}, |  | (17) |

where U¯​(θ)\bar{U}(\theta) is the sample mean CRRA utility and Mk,ℓM\_{k,\ell} is the prior mean. This step is solved with analytic gradients. Next, three quantities are updated. The residual scale σ2\sigma^{2} is the mean squared residual of the policy-scaled linear predictor against realised returns. The Piironen–Vehtari target,

|  |  |  |
| --- | --- | --- |
|  | τPV=p0L−p0​σT,\tau\_{\mathrm{PV}}=\frac{p\_{0}}{L-p\_{0}}\frac{\sigma}{\sqrt{T}}, |  |

translates the prior belief that roughly p0p\_{0} of the LL signals carry genuine predictive content into a global shrinkage level. The current τ\tau is blended toward this target,

|  |  |  |
| --- | --- | --- |
|  | τ←ρ​τold+(1−ρ)​τPV,\tau\;\leftarrow\;\rho\,\tau\_{\text{old}}+(1-\rho)\,\tau\_{\mathrm{PV}}, |  |

and the local scales are updated as

|  |  |  |
| --- | --- | --- |
|  | λℓ,k2←|θk,ℓ−Mk,ℓ|σ​τ+1,\lambda\_{\ell,k}^{2}\;\leftarrow\;\frac{|\theta\_{k,\ell}-M\_{k,\ell}|}{\sigma\tau}+1, |  |

so signals with large deviations from the prior mean receive less shrinkage. All updates include minor numerical safeguards for stability. Convergence is declared when changes in θ\theta, τ\tau, and λ\lambda all fall below a tolerance.

Prediction follows the same Monte-Carlo averaging as BPPP. Each coefficient is perturbed by a draw from the diagonal Laplace posterior around the MAP,

|  |  |  |
| --- | --- | --- |
|  | ϵk,ℓ(m)∼𝒩​(0,vk,ℓ),vk,ℓ=(1K2​∑scs​rs,k2​zs,ℓ2+1λ~ℓ,k2)−1,\epsilon\_{k,\ell}^{(m)}\sim\mathcal{N}\!\left(0,\,v\_{k,\ell}\right),\qquad v\_{k,\ell}=\left(\frac{1}{K^{2}}\sum\_{s}c\_{s}\,r\_{s,k}^{2}\,z\_{s,\ell}^{2}+\frac{1}{\tilde{\lambda}\_{\ell,k}^{2}}\right)^{-1}, |  |

where cs=−U′′​(1+rp,s)c\_{s}=-U^{\prime\prime}(1+r\_{p,s}) is the CRRA curvature at the MAP portfolio return. Weights are then averaged as in Equation ([16](https://arxiv.org/html/2602.21173v1#A2.E16 "In Appendix B Estimation ‣ Bayesian Parametric Portfolio Policies")). The posterior shrinkage factor for each signal,

|  |  |  |
| --- | --- | --- |
|  | κℓ,k=11+λ~ℓ,k2​‖zℓ‖2/σ2,\kappa\_{\ell,k}=\frac{1}{1+\tilde{\lambda}\_{\ell,k}^{2}\,\|z\_{\ell}\|^{2}/\sigma^{2}}, |  |

measures how far the posterior is from the prior mean.

## Appendix C Additional Tables and Figures

![Refer to caption](posterior_predictive_checks.png)

Figure A1: Return and Weight Distributions by Model

Notes: Left: kernel density estimates of monthly out-of-sample returns. Right: boxplots of factor weights across the out-of-sample period. BPPP produces a narrower weight distribution and a more symmetric, lighter-tailed return distribution than PPP, consistent with the overexposure correction of Proposition 1.



![Refer to caption](efficient_frontier.png)

Figure A2: Portfolio Risk-Return Map (Full Out-of-Sample Period)

Notes: Annualised volatility–return space, 1973–2023. Colour encodes the Sharpe ratio.



![Refer to caption](cumulative_returns_main.png)

Figure A3: Cumulative Returns by Model

Notes: Cumulative portfolio wealth, expanding window, monthly rebalancing, initial training 120 months.



![Refer to caption](drawdown_and_qq.png)

Figure A4: Drawdown and Normal Q-Q: PPP vs. BPPP

Notes: Left: drawdown from peak wealth. Right: normal Q-Q of monthly returns.

![Refer to caption](kappa_distribution.png)


Figure A5: Distribution of Horseshoe Shrinkage Factors

![Refer to caption](theta_heatmap_top_signals_PPP.png)

Figure A6: Top Signal Coefficients Across Models (I)

Notes: Heatmap of the largest signal interactions by absolute coefficient across PPP, BPPP, and Horseshoe.

![Refer to caption](theta_heatmap_top_signals_BPPP.png)

Figure A7: Top Signal Coefficients Across Models (II)

Notes: Heatmap of the largest signal coefficients by absolute coefficient across PPP, BPPP, and Horseshoe.

![Refer to caption](theta_heatmap_top_signals_HS.png)

Figure A8: Top Signal Coefficients Across Models (III)

Notes: Heatmap of the largest signal coefficients by absolute coefficient across PPP, BPPP, and Horseshoe.

![Refer to caption](signal_subset_bootstrap.png)

Figure A9: Signal Subset Stability: Bootstrap Distribution of Mean Horseshoe Coefficients

Notes: Distribution of mean absolute horseshoe coefficient across 500 draws of 50 signals from the full set of 242.

Table A1: Economic Significance: Certainty Equivalents and Performance Fees

| Portfolio | CE annual (%) | CE vs. Market (%) | Perf. Fee (bp) |
| --- | --- | --- | --- |
| BPPP | 10.52 | 5.36 | 500 |
| PPP | 8.68 | 3.53 | 331 |
| Horseshoe | 9.90 | 4.74 | 443 |
| Mean-Var | 6.09 | 0.93 | 89 |
| Benchmark | 5.15 | — | — |

* •

  Notes: CE returns under exact CRRA utility, γ=5\gamma=5. Performance fee: annual bp a benchmark investor would pay to switch to the given strategy.




Table A2: Prior Calibration Under Alternative Target Tilt Standard Deviations

| δ\delta | σθ\sigma\_{\theta} | ν\nu |
| --- | --- | --- |
| 0.20 | 0.0129 | 0.0005 |
| 0.35 | 0.0225 | 0.0015 |
| 0.50 | 0.0321 | 0.0031 |

* •

  Notes: σθ=δ/L\sigma\_{\theta}=\delta/\sqrt{L} and ν=σθ2⋅max⁡(T/L,1)\nu=\sigma\_{\theta}^{2}\cdot\max(T/L,1) with L=242L=242. Baseline: δ=0.35\delta=0.35.

Table A3: Subset of Signals Referenced in the Paper

| Signal | Description | Signal | Description |
| --- | --- | --- | --- |
| Accruals | Accruals | NumEarnIncrease | Earnings-increase streak length |
| AnalystValue | Analyst value | OrgCap | Organizational capital |
| BetaTailRisk | Tail-risk beta | PayoutYield | Payout yield |
| ChAssetTurnover | Change in asset turnover | ProbInformedTrading | Probability of informed trading |
| ChInv | Inventory growth | RIVolSpread | Realized-minus-implied volatility spread |
| ChNNCOA | Change in net noncurrent operating assets | ResidualMomentum | FF3-residual momentum |
| CompositeDebtIssuance | Composite debt issuance | RevenueSurprise | Revenue surprise |
| ConsRecomm | Consensus recommendation | Tax | Taxable income to income |
| CoskewACX | Daily-return coskewness | TotalAccruals | Total accruals |
| DivOmit | Dividend omission | VolumeTrend | Volume trend |
| EarnSupBig | Earnings surprise of large firms | cfp | Operating cash flow to price |
| Herf | Industry concentration (sales Herfindahl) | tang | Tangibility |
| IntMom | Intermediate momentum | Val\_0 | Valuation gap, Mkt |
| InvGrowth | Investment growth | Val\_1 | Valuation gap, SMB |
| MomOffSeason | Off-season long-horizon reversal | Val\_4 | Valuation gap, RMW |
| MomOffSeason06YrPlus | Off-season reversal, yrs 6–10 | Val\_5 | Valuation gap, UMD |
| MomOffSeason16YrPlus | Off-season reversal, yrs 16–20 | Rev\_4 | Reversal signal, RMW |
| MomRev | Momentum/reversal composite | Rev\_5 | Reversal signal, UMD |
| MomSeason11YrPlus | Return seasonality, yrs 11–15 | Vol\_0 | Volatility-timing signal, Mkt |
| NetPayoutYield | Net payout yield | Vol\_2 | Volatility-timing signal, HML |

Notes: The 40 signals listed are the subset of the total 242 signals used for estimation that are shown in the Tables and Figures throughout, those referenced in signal-level graphs (top-20 signal-factor interactions across PPP, BPPP, and Horseshoe). Data are monthly. Signals are standardized in expanding windows using only information available at each date. Estimation sample is 1963M7–2023M12; out-of-sample evaluation is 1973M8–2023M12 after a 120-month initial window. Signals not in the Val/Rev/Vol families are from Chen and Zimmermann ([2022](https://arxiv.org/html/2602.21173v1#bib.bib2 "Open source cross-sectional asset pricing")). Factor-timing signals (Val/Rev/Vol) follow Haddad et al. ([2020](https://arxiv.org/html/2602.21173v1#bib.bib9 "Factor timing")) and are implemented as: for factor kk, Valk,t=−log⁡(Ck,t/exp⁡[160​∑j=059log⁡(Ck,t−j)])\mathrm{Val}\_{k,t}=-\log\!\left(C\_{k,t}/\exp\!\left[\frac{1}{60}\sum\_{j=0}^{59}\log(C\_{k,t-j})\right]\right), Revk,t=−(rk,t−1−136​∑j=035rk,t−j)\mathrm{Rev}\_{k,t}=-(r\_{k,t-1}-\frac{1}{36}\sum\_{j=0}^{35}r\_{k,t-j}), and Volk,t=−σ^k,t(12)\mathrm{Vol}\_{k,t}=-\hat{\sigma}^{(12)}\_{k,t} with σ^k,t(12)=1211​Var^12​(rk,⋅)\hat{\sigma}^{(12)}\_{k,t}=\sqrt{\frac{12}{11}\widehat{\mathrm{Var}}\_{12}(r\_{k,\cdot})}. Here k∈{0,1,2,3,4,5}={Mkt,SMB,HML,CMA,RMW,UMD}k\in\{0,1,2,3,4,5\}=\{\mathrm{Mkt},\mathrm{SMB},\mathrm{HML},\mathrm{CMA},\mathrm{RMW},\mathrm{UMD}\}, and this table uses Val\_0, Val\_1, Val\_4, Val\_5; Rev\_4, Rev\_5; Vol\_0, Vol\_2. Acronyms follow those in the Open Source Asset Pricing Dataset.