---
authors:
- Tim J. Boonen
- Wenyuan Li
- Zixiao Quan
doc_id: arxiv:2512.01623v1
family_id: arxiv:2512.01623
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Monopoly Pricing of Weather Index Insurance
url_abs: http://arxiv.org/abs/2512.01623v1
url_html: https://arxiv.org/html/2512.01623v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tim J. Boonen  Wenyuan Li  Zixiao Quan
Department of Statistics and Actuarial Science, School of Computing and Data Science, The University of Hong Kong, Pokfulam Road, Hong Kong, P.R. China. Email: <tjboonen@hku.hk>.Department of Statistics and Actuarial Science, School of Computing and Data Science, The University of Hong Kong, Pokfulam Road, Hong Kong, P.R. China. Email: <wylsaas@hku.hk>.Corresponding author. Department of Statistics and Actuarial Science, School of Computing and Data Science, The University of Hong Kong, Pokfulam Road, Hong Kong, P.R. China. Email: <zixiao.quan@connect.hku.hk>.

###### Abstract

This study models the monopoly pricing of weather index insurance as a Bowley-type sequential game involving a profit-maximizing insurer (leader) and a farmer (follower). The farmer chooses an insurance payoff to minimize a convex distortion risk measure, while the insurer anticipates this best response and selects a premium principle and its parameters to maximize profit net of administrative costs. For the insurer, we adopt three different premium-principle parameterizations: (i) an expected premium with a single risk-loading factor, (ii) a two-parameter distortion premium based on a power transform, and (iii) a fully flexible pricing kernel drawn from the general Choquet integral representation with nondecreasing distortions. For the farmer, we model index payoffs using neural networks and compare solutions under fully connected architectures with those under convolutional neural networks (CNNs).
We solve the game using a penalized bilevel programming algorithm that employs a function-value-gap penalty and delivers convergence guarantees without requiring the lower-level objective to be strongly convex. Based on Iowa’s soybean yields and high-dimensional PRISM weather data, we find that CNN-based designs yield smoother, less noisy payoffs that reduce basis risk and push insurer profits closer to indemnity insurance levels. Moreover, expanding pricing flexibility from a single loading to a two-parameter distortion premium, and ultimately to a flexible pricing kernel, systematically increases equilibrium profits.

Keywords: Index insurance, Bowley solution, bilevel programming, distortion risk measure, convolutional neural networks.

## 1 Introduction

Weather-based risks are one of the most significant challenges faced by agricultural producers worldwide, particularly in regions vulnerable to climate variability and extreme weather events. These risks can lead to substantial financial losses, which threaten the livelihoods of farmers and harm the socioeconomic stability of rural communities. Traditional risk management tools, such as crop indemnity insurance, have been widely adopted to mitigate these financial impacts. However, traditional insurance products often suffer from limitations, which include high administrative costs, moral hazard, and basis risk. To address these challenges, index insurance has emerged as a promising alternative. Index insurance connects insurance payoffs to objective and verifiable weather indices, which reduces the reliance on subjective loss assessments and mitigates moral hazards. Despite its potential, designing index contracts that materially hedge farmer risk while remaining profitable is especially challenging when the relationships between weather indices and crop yield are high-dimensional and nonlinear (schlenker2009nonlinear; rigden2020combined). These challenges are amplified in concentrated markets in which a monopolistic insurer can exert pricing power over contract terms and premium principles.

This paper studies the monopoly pricing of weather index insurance as a sequential game between a profit-maximizing insurer and a risk-averse farmer. We formulate the interaction as a bilevel optimization problem: the farmer faces a stochastic production loss and chooses an insurance payoff to minimize its distortion risk measure; the insurer anticipates this best response and selects a premium principle (and its parameters) to maximize profit net of administrative costs. We begin with two canonical premium principles. The first is the expected premium principle with a risk-loading factor θ\theta. The second is the distortion-based premium principle with a power distortion, which has an additional parameter ρ\rho compared to the expected premium principle. We then further generalize the premium principle to a fully flexible pricing kernel, which is a distortion function in a broad feasible class. On the demand side, we model farmer preferences using distortion risk measures that focus on a convex combination of Conditional Value-at-Risk (CVaR) and expected risk.

Our analysis contributes to the literature on Bowley solutions, which model a leader–follower game between a monopolistic insurer (leader) and a policyholder (follower). Under the Bowley solution, the insurance premium is first set by a chosen premium principle. Given this principle, the policyholder then selects its optimal coverage, which is a functional of this principle. The insurer knows this functional and chooses the premium principle that is optimal for her. In particular, this yields the insurer’s optimal pricing density for insurance contracts and the policyholder’s optimal insurance indemnity function (chan1985reinsurer). Prior works have investigated Bowley solutions under various preferences and pricing assumptions. Some of these have focused on using a profit-maximization objective for the insurer and a distortion risk-minimization objective for the policyholder. For example, cheung2019risk investigate Bowley equilibria under distortion risk measures and general premium principles of a reinsurer (leader) and an insurer (follower). They derive the insurer’s explicit ceded loss and the reinsurer’s pricing functions via a two-step procedure that first minimizes the insurer’s distortion risk measure and then maximizes the reinsurer’s net gain. Both pricing and preferences are modeled through probability distortions, which are related to our use of distortion premium principles on the supply side and distortion risk measures on the demand side. chi2020bowley revisit Bowley with a risk-neutral reinsurer and impose upper bounds on the first two moments of the indemnity. They further relax the assumptions of the expected premium principle in chan1985reinsurer and the distortion premium principle in cheung2019risk, and demonstrate that the monopoly premium can be determined without a specific premium principle. boonen2021bowley also study Bowley solutions under the assumption that the reinsurer adopts a general premium function. A highlight is that their work analyzes Bowley reinsurance solutions under asymmetric information about the type of distortion function that the insurer adopts. The monopolistic reinsurer chooses a premium principle to maximize expected profit while anticipating the insurer’s type-dependent demand. Importantly, unlike the symmetric-information Bowley setting (e.g., cheung2019risk) in which the leader can extract all surplus, asymmetric information prevents full extraction and allows both parties to strictly benefit from the reinsurance contracts. In addition, li2021bowley study the sequential game under the mean-variance premium principle. In their setting, the buyer (follower) maximizes a mean-variance functional of its wealth and the seller (leader) maximizes its expected wealth by choosing the parameter of the mean-variance premium principle. Their findings demonstrate that the seller’s premium parameters change with respect to the buyer’s indemnity. There is also literature that adopts a different objective for the insurer (leader) and the policyholder (follower). For example, chen2024bowley search for the set of Bowley solutions under the setup where the reinsurer minimizes the VaR measure of its risk position instead of maximizing its profit. Besides this, boonen2024bowley analyze Bowley solutions with the policyholder’s objective replaced by expected-utility maximization. It shows that deductibles rise with the safety loading and proves that Bowley outcomes are Pareto dominated, which motivates policy intervention. In addition to this evidence, jiang2025bowley study a Bowley insurance game with mean–variance preferences and a variance-based premium. They find the Bowley solution and show that it is never Pareto optimal, which supports the previous finding that such contracts are inefficient. This line of literature supports our game-theoretic approach in modeling Bowley equilibria. However, the current literature mainly focuses on finding Bowley solutions for indemnity insurance, where the contracts are written on the actual loss incurred. We adopt the concepts of Bowley solutions and apply them to index insurance. We investigate Bowley solutions for index insurance under both the expected premium principle and distortion premium principles with different distortion functions adopted by the policyholder.

We also contribute to a growing actuarial literature that tackles basis risk in index insurance. Past literature has investigated reducing basis risk by using multivariate indices, flexible models to capture the complex relationships between indices and insurance payoff functions, as well as dependence modeling. zhang2019index study optimal index insurance design under the expected-utility maximization framework. They find that the payoff functions can be highly nonlinear and nonmonotonic functions of the index variables, which align the payoff functions better with the actual loss and thus reduce basis risk. They highlight the generality of their model setup and its potential to be applied in various insurance applications. As a result, many research papers adopt the expected utility maximization framework for designing optimal weather index insurance. For example, tan2024flexible use B-spline functions to define the feasible sets of the expected utility maximization problem and a penalty function to avoid overfitting. Besides this, chen2024managing adopt the expected utility maximization framework in the design of weather index insurance and use neural networks (NNs) to model the insurance payoff functions. They propose to use neural networks to better capture the highly nonlinear relationships between the crop production losses and the high-dimensional weather indices. They show that the use of neural networks could reduce basis risk, lower insurance premiums, and improve the farmer’s utility. Our approach builds on theirs as we use convolutional neural networks to further reduce basis risk. Another common way to reduce basis risk is to construct lower-dimensional indices that provide stronger signals of weather conditions. For example, boyd2020design use principal component regression and partial least-squares regression to construct multivariate indices. They show that these constructed indices perform better at correctly determining when payments should be triggered and at reducing the mismatch between the insurance payoff and the actual loss. li2021improved use a dynamic factor model for crop yield prediction, which also builds on the idea of summarizing high-dimensional weather variables using lower-dimensional latent factors and reducing dimensionality to improve prediction accuracy. The improved crop yield predictions could then help insurance pricing. zhu2024deep also focuses on improving crop yield predictions by using factor models. They build a deep factor model with an encoder–decoder structure. The encoder compresses yields into a latent “production index” that captures nonlinear space–time patterns. They then feed weather and economic data into a concatenated network to model and predict this index. The decoder maps the predicted index back to crop yields. Besides this, zhu2018spatial propose Lévy subordinated hierarchical Archimedean copulas, which produce a stronger fit for multiscale spatial dependence and joint extremes. This evidence supports designs that exploit spatiotemporal grids and reinforces the idea that CNN-based indices can be more robust under correlated shocks. This motivates our use of CNNs as an alternative way to model insurance payoff functions. In addition, hybrid product design has also evolved to balance moral hazard with basis risk. fan2023empirical develop a model-based annealing random search and show that it effectively targets tail-risk objectives, which is crucial for lines exposed to catastrophes. Our penalty-based bilevel programming algorithm offers an alternative for large-scale, nonconvex design problems with equilibrium constraints, and fits settings where market power and pricing flexibility affect outcomes.

We solve for the Bowley solutions in our settings using a penalized bilevel programming algorithm, which works even when the lower-level problem is not strongly convex (shen2023penalty). The problem is high-dimensional and not necessarily convex due to weather indices. We model the insurance payoff function with fully connected neural networks and compare it with the payoff functions modeled using CNNs, which preserve the index-by-time grid structure (krizhevsky2012imagenet; chen2024managing). We solve the two-stage game with a function-value-gap penalty. This links a penalized single-level problem to the original bilevel problem under mild assumptions. The result is a practical algorithm with convergence guarantees that scale to large weather–yield data.

Our main findings are as follows. First, the optimal monopoly insurance contract under CVaR consistently exhibits a stop-loss structure. Our model reproduces optimal indemnity contracts consistent with the literature (cai2008optimal); for index insurance, this shape persists, but contains more noise caused by basis risk. Second, CNN-based designs yield smoother, less noisy payoff functions than fully connected neural networks. We show that CNN-based designs are capable of reducing basis risk and pushing insurer profits closer to indemnity insurance levels. Third, insurer pricing responds sharply to farmer risk aversion: increasing the weight on CVaR in the farmer’s distortion measure leads to higher equilibrium loadings and greater profit extraction by the monopolist. Fourth, expanding the insurer’s pricing flexibility from a single risk loading to a two-parameter distortion premium, and then ultimately to a flexible pricing kernel, systematically increases equilibrium profits, which highlights the importance of premium regulation in concentrated markets.

The remainder of the paper proceeds as follows. Section [2](https://arxiv.org/html/2512.01623v1#S2 "2 Problem Formulation ‣ Monopoly Pricing of Weather Index Insurance") formulates the sequential game, introduces the farmer’s distortion risk measures, and the insurer’s premium principles. Section [3](https://arxiv.org/html/2512.01623v1#S3 "3 Model ‣ Monopoly Pricing of Weather Index Insurance") provides theory on the penalized bilevel programming algorithm that we adopt in this study. Section [4](https://arxiv.org/html/2512.01623v1#S4 "4 Data ‣ Monopoly Pricing of Weather Index Insurance") describes the data and neural-network architectures for index insurance design. Section [5](https://arxiv.org/html/2512.01623v1#S5 "5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") reports numerical results, including sensitivity analysis, comparisons of fully connected networks and CNNs, and extensions to two-parameter and general pricing-kernel settings. Section [6](https://arxiv.org/html/2512.01623v1#S6 "6 Conclusion ‣ Monopoly Pricing of Weather Index Insurance") concludes with policy implications and directions for future research.

## 2 Problem Formulation

### 2.1 General Setup

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a probability space such that Ω\Omega is finite and ℱ=2Ω\mathcal{F}=2^{\Omega} is the power σ\sigma-algebra.111This paper considers empirical distributions using numerical methods, and so we use a simplified setting with finitely many states of the world. Many results can be extended to infinite state spaces under standard integrability assumptions, as long as the strategy spaces are finite dimensional. Moreover, denote by ℝ+Ω\mathbb{R}^{\Omega}\_{+} the set of nonnegative random variables on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}).

Consider a farmer seeking to hedge against weather-related losses. The farmer is faced with a stochastic production loss YY. We construct an index-insurance contract, where the insurance payoff is determined by a function of pp-dimensional vector of weather indices 𝐗=(X1,X2,…,Xp)\mathbf{X}=(X\_{1},X\_{2},...,X\_{p}). The nonnegative insurance payoff function is denoted by I​(𝐗)I(\mathbf{X}) with I:ℝp→ℝ+I:\mathbb{R}^{p}\rightarrow\mathbb{R}\_{+}. The premium is denoted by Π​(I​(𝐗))\Pi(I(\mathbf{X})), which is a function of I​(𝐗)I(\mathbf{X}).

### 2.2 Distortion Function

Both the farmer and the insurer use a transformation of probabilities to evaluate and price random losses. This is used to formulate the optimization problem,
Let 𝒢\mathcal{G} be the class of continuous and nondecreasing functions g:[0,1]→ℝ+g:[0,1]\rightarrow\mathbb{R}\_{+} such that g​(0)=0g(0)=0. For g∈𝒢g\in\mathcal{G}, we can write the distortion risk measure for risk Z∈ℝ+ΩZ\in\mathbb{R}\_{+}^{\Omega} as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0∞g​(ℙ​(Z>z))​𝑑z=∑k=1q−1g​(ℙ​({ω1,…,ωk}))⋅[Z​(ωk)−Z​(ωk+1)]+Z​(ωq),\int\_{0}^{\infty}g(\mathbb{P}(Z>z))dz=\sum\_{k=1}^{q-1}g\left(\mathbb{P}\left(\left\{\omega\_{1},\ldots,\omega\_{k}\right\}\right)\right)\cdot\left[Z\left(\omega\_{k}\right)-Z\left(\omega\_{k+1}\right)\right]+Z\left(\omega\_{q}\right), |  | (1) |

if the state space Ω={ω1,…,ωq}\Omega=\left\{\omega\_{1},\ldots,\omega\_{q}\right\} is such that Z​(ω1)≥⋯≥Z​(ωq)Z\left(\omega\_{1}\right)\geq\cdots\geq Z\left(\omega\_{q}\right); see, e.g., de2008second and boonen2015competitive. We use premium principles of the form ([1](https://arxiv.org/html/2512.01623v1#S2.E1 "In 2.2 Distortion Function ‣ 2 Problem Formulation ‣ Monopoly Pricing of Weather Index Insurance")), and we denote such principle as Π^​(Z)\hat{\Pi}(Z). As special cases, we will study the case where gg is linear or when g​(s)=(1+θ)​s1/ρg(s)=(1+\theta)s^{1/\rho} for θ≥0\theta\geq 0 and ρ≥1\rho\geq 1.

Let ρF\rho\_{F} be the distortion risk measure of the farmer, and the distortion risk measure of a loss Z∈ℝ+ΩZ\in\mathbb{R}^{\Omega}\_{+} is given by

|  |  |  |
| --- | --- | --- |
|  | ρF​(Z)=∫0∞gf​(ℙ​(Z>z))​𝑑z,\rho\_{F}(Z)=\int\_{0}^{\infty}g\_{f}(\mathbb{P}(Z>z))dz, |  |

where gfg\_{f} is the distortion function of the farmer. A distortion function is a nondecreasing and concave function g:[0,1]→[0,1]g:[0,1]\rightarrow[0,1] such that g​(0)=0g(0)=0. The class of distortion functions is denoted by 𝒢d\mathcal{G}\_{d}, and, clearly, 𝒢d⊂𝒢\mathcal{G}\_{d}\subset\mathcal{G}.

The assumption of concavity of the distortion function implies aversion to mean-preserving spreads of the corresponding distortion risk measure (yaari1987).
The distortion functions employed in this work for the farmer’s risk measure include: 1. Conditional Value-at-Risk (CVaR). 2. A convex combination of CVaR and expected risk.

#### 2.2.1 Conditional Value at Risk

Conditional Value-at-Risk (CVaR), also known as Expected Shortfall, quantifies the expected value of the loss given that the loss exceeds a specified threshold. Mathematically, for a random variable ZZ and a confidence level α∈(0,1)\alpha\in(0,1), CVaR is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(Z)=11−α​∫α1VaRu​(Z)​𝑑u,\text{CVaR}\_{\alpha}(Z)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\text{VaR}\_{u}(Z)du, |  | (2) |

where VaRα​(Z)\text{VaR}\_{\alpha}(Z) represents the Value-at-Risk at level α\alpha, which is defined as the α\alpha-th quantile of the distribution of ZZ:

|  |  |  |
| --- | --- | --- |
|  | VaRu​(Z)=inf{x∈ℝ:P​(Z≤x)≥u},u∈[0,1].\text{VaR}\_{u}(Z)=\inf\{x\in\mathbb{R}:P(Z\leq x)\geq u\},u\in[0,1]. |  |

For continuous random variables, the CVaR is equal to

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(Z)=E​[Z|Z≥VaRα​(Z)].\text{CVaR}\_{\alpha}(Z)=E[Z|Z\geq\text{VaR}\_{\alpha}(Z)]. |  | (3) |

The risk measure CVaRα\text{CVaR}\_{\alpha} is a distortion risk measure with distortion function g​(s)=min⁡{s1−α,1}g(s)=\min\{\frac{s}{1-\alpha},1\} for s∈[0,1]s\in[0,1] (dhaene2006).

#### 2.2.2 Convex Combination of CVaR and Expected Risk

To manage the trade-off between risk and expected return, we incorporate a convex combination of CVaR and expected risk. This combination is governed by a weight λ∈[0,1]\lambda\in[0,1], which determines the relative importance of CVaR versus expected risk. The convex combination is expressed as ρ​(Z)=λ​𝔼​(Z)+(1−λ)​CVaRα⁡(Z)\rho(Z)=\lambda\,\mathbb{E}(Z)+(1-\lambda)\,\operatorname{CVaR}\_{\alpha}(Z), and the corresponding distortion function is given by g​(s)=λ​s+(1−λ)​min⁡{s/(1−α),1}g(s)=\lambda s+(1-\lambda)\min\{s/(1-\alpha),1\} for s∈[0,1]s\in[0,1]. This places ρ\rho within the distortion-risk-measure framework, yielding an increasing, concave distortion with a kink at s=1−αs=1-\alpha (cheung2017characterizations).

The distortion function g​(s)g(s) is largely linear in the body of the distribution, while adding extra weight to the worst 1−α1-\alpha tail. In the tail region (s≤1−αs\leq 1-\alpha), the slope is λ+(1−λ)/(1−α)\lambda+(1-\lambda)/(1-\alpha), which upweights rare and severe losses. In the body (s>1−αs>1-\alpha), the slope is λ\lambda, recovering mean-like behavior. Thus, λ\lambda controls the appetite for risk: λ→1\lambda\to 1 makes ρ\rho approach the mean, while λ→0\lambda\to 0 makes ρ\rho approach pure CVaR. The parameter α\alpha sets the tail horizon: larger α\alpha focuses on rarer extremes. Because gg is concave, the associated distortion risk measure is coherent (artzner1999) and, in particular, satisfies subadditivity (wang1997).

#### 2.2.3 Power function

The power distortion function g​(s)=s1/ρg(s)=s^{1/\rho} is used to embed a transparent, one-parameter distortion function into insurance and reinsurance pricing by overweighting or underweighting tail probabilities in a controlled way. The parameter ρ\rho governs the shape and thus the attitude toward risk: when ρ>1\rho>1, 1/ρ<11/\rho<1, and gg is concave on [0,1][0,1], so g​(s)≥sg(s)\geq s for s∈(0,1)s\in(0,1). This inflates survival probabilities, raises premiums, and represents a risk-averse tail loading. When ρ<1\rho<1, 1/ρ>11/\rho>1, and the function gg is convex, so g​(s)≤sg(s)\leq s. This downweights tail probabilities, lowers premiums, and corresponds to risk-seeking behavior. At ρ=1\rho=1, gg is linear, and this yields risk-neutral pricing. This distortion is also known as the proportional hazards transform. This distortion function links the premiums to tail risk, which aligns with market-consistent pricing ideas. Compared with Wang’s transform, which distorts probabilities via the (standard) normal CDF, the power form is a simpler alternative within the same distortion-based framework and is convenient when a single parameter, a closed form, and tail emphasis are desired (see, e.g., wang1996premium).

### 2.3 Sequential game

The farmer and the insurer make decisions sequentially: the insurer selects the pricing rule Π\Pi first, and the farmer then chooses the insurance payoff function I​(𝐗)I(\mathbf{X}) after observing the pricing rule. The farmer chooses (𝐗)(\mathbf{X}) to minimize its risk as measured by ρF\rho\_{F}. The insurer chooses the premium function Π​(I​(𝐗))\Pi(I(\mathbf{X})) to maximize its profit, taking into account the farmer’s decisions on the payoff functions for each possible premium function. We express this sequential decision-making problem as a bilevel optimization problem, with the insurer’s objective as the upper problem and the farmer’s objective as the lower problem.

Upper Problem (UP): Insurer

|  |  |  |
| --- | --- | --- |
|  | MaxΠ∈𝒫s⁡Π​(I​(𝐗))−(1+μ)​𝔼​(I​(𝐗)),\operatorname{Max}\_{\Pi\in\mathcal{P}\_{s}}\Pi(I(\mathbf{X}))-(1+\mu)\mathbb{E}(I(\mathbf{X})), |  |

where the feasible set 𝒫s\mathcal{P}\_{s} is a closed and convex subset of the following set:

|  |  |  |
| --- | --- | --- |
|  | 𝒫={Π^:ℝ+Ω→ℝ+∣Π^​(I​(𝐗))=∫0∞gi​(ℙ​(I​(𝐗)>z))​𝑑z,gi∈𝒢}.\mathcal{P}=\left\{\hat{\Pi}:\mathbb{R}^{\Omega}\_{+}\rightarrow\mathbb{R}\_{+}\mid\hat{\Pi}(I(\mathbf{X}))=\int\_{0}^{\infty}g\_{i}(\mathbb{P}(I(\mathbf{X})>z))dz,g\_{i}\in\mathcal{G}\right\}. |  |

Lower Problem (LP): Farmer

|  |  |  |  |
| --- | --- | --- | --- |
|  | minI∈ℐ⁡ρF​(Y−I​(𝐗)+Π​(I​(𝐗))).\min\_{I\in\mathcal{I}}\rho\_{F}\left(Y-I(\mathbf{X})+\Pi(I(\mathbf{X}))\right). |  | (4) |

As special cases of 𝒫s\mathcal{P}\_{s}, we consider

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝒫s​1={Π^:ℝ+Ω→ℝ+∣Π^​(I​(𝐗))=(1+θ)​𝔼​(I​(𝐗)),θ≥0}, or\displaystyle\mathcal{P}\_{s1}=\left\{\hat{\Pi}:\mathbb{R}^{\Omega}\_{+}\rightarrow\mathbb{R}\_{+}\mid\hat{\Pi}(I(\mathbf{X}))=(1+\theta)\mathbb{E}(I(\mathbf{X})),\theta\geq 0\right\},\text{ or} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝒫s​2={Π^:ℝ+Ω→ℝ+∣Π^​(I​(𝐗))=(1+θ)​∫0∞ℙ​(I​(𝐗)>z)1ρ​𝑑z,θ≥0,ρ≥1}.\displaystyle\mathcal{P}\_{s2}=\left\{\hat{\Pi}:\mathbb{R}^{\Omega}\_{+}\rightarrow\mathbb{R}\_{+}\mid\hat{\Pi}(I(\mathbf{X}))=(1+\theta)\int\_{0}^{\infty}\mathbb{P}(I(\mathbf{X})>z)^{\frac{1}{\rho}}dz,\theta\geq 0,\rho\geq 1\right\}. |  |

We denote the first special case of 𝒫s\mathcal{P}\_{s} as 𝒫s​1\mathcal{P}\_{s1} (Problem 1), where we explicitly set the insurer’s pricing rule to the expected premium principle. This means that the insurer selects only the risk-loading factor θ\theta in order to maximize its profit. The second special case of 𝒫s\mathcal{P}\_{s} is denoted by 𝒫s​2\mathcal{P}\_{s2} (Problem 2). In this special case, we adopt the power distortion function for the premium, and the insurer then maximizes its profit by choosing two parameters ρ\rho and θ\theta. In this case, the insurer has more flexibility in its pricing strategy compared with 𝒫s​1\mathcal{P}\_{s1}. We begin by analyzing solutions to these two special cases (Problems 1 and 2). We then generalize the premium principle to the feasible set 𝒫s=𝒫\mathcal{P}\_{s}=\mathcal{P}, and denote this setting as Problem 3, in which we investigate equilibrium solutions under the general pricing function gig\_{i}.

## 3 Model

### 3.1 Neural Network Based Models

The deep-learning models that we propose to obtain the insurance payoffs are fully connected neural networks (NNs) and convolutional neural networks (CNNs). CNNs are a special class of neural networks that incorporate convolution in at least one of their layers. In this study, we compare these two classes of models. NNs process flattened vector inputs; thus, the two-dimensional time-index matrices must be flattened. CNNs are particularly suitable for processing grid-structured data without destroying its two-dimensional structure. This makes CNNs a well-motivated alternative to the traditional fully connected neural networks proposed in chen2024managing.

#### 3.1.1 Fully Connected Neural Networks (NNs)

Neural Networks (NNs) are models composed of interconnected neurons that are organized in layers. Each neuron processes inputs, applies a weight, adds a bias, and passes the result through an activation function. Specifically, the outputs of neurons in one layer serve as inputs to neurons in the subsequent layer. The most common type of NN is the fully connected architecture, which is illustrated in Figure [1](https://arxiv.org/html/2512.01623v1#S3.F1 "Figure 1 ‣ 3.1.1 Fully Connected Neural Networks (NNs) ‣ 3.1 Neural Network Based Models ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance"). This model receives as input an nn-dimensional vector, X=(X1,X2,…,Xn)TX=(X\_{1},X\_{2},\dots,X\_{n})^{T}, and outputs a single prediction yy.

In a deep learning NN architecture, the structure consists of an input layer, an output layer, and DD hidden layers (D>1D>1). The dd-th (d=1,2,…,Dd=1,2,\dots,D) hidden layer, Z(d)=(Z1(d),Z2(d),…,Znd(d))TZ^{(d)}=(Z^{(d)}\_{1},Z^{(d)}\_{2},\dots,Z^{(d)}\_{n\_{d}})^{T}, contains ndn\_{d} neurons. Each neuron in the hidden layer is obtained by applying a nonlinear function, σd−1\sigma\_{d-1}, to the linear combination of the neurons from the previous layer. This is formally expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐙(d)=σd−1​(α(d−1)+𝐖(d−1)​𝐙(d−1)),\mathbf{Z}^{(d)}=\sigma\_{d-1}(\mathbf{\alpha}^{(d-1)}+\mathbf{W}^{(d-1)}\mathbf{Z}^{(d-1)}), |  | (5) |

where:

* •

  W(d−1)W^{(d-1)} is an (lh×lh−1)(l\_{h}\times l\_{h-1})-dimensional weight matrix;
* •

  α(d−1)\alpha^{(d-1)} is a (nd×1)(n\_{d}\times 1)-vector of bias units, capturing intercepts in the model;
* •

  σh−1\sigma\_{h-1} is the activation function, which is typically nonlinear and predefined.

This fully connected structure ensures that neurons between two adjacent layers are pairwise connected.

![Refer to caption](nn_illustration.png)


Figure 1: Illustration of NN structure.

#### 3.1.2 Convolutional Neural Networks (CNNs)

CNNs are a type of deep learning model primarily used for processing structured grid-like data such as images. They automatically and adaptively learn spatial hierarchies of features through layers of convolution, pooling, and fully connected layers. After the breakthrough work by krizhevsky2012imagenet, CNNs became well-known for deep learning models with a larger volume of data.

CNNs offer several key advantages that make them highly effective for handling structured data. First, they use convolutional kernels to efficiently extract local features, which reduces computational complexity and the number of parameters compared to fully connected networks. Second, CNNs adopt weight sharing, where the same set of weights is applied across different regions of the input. This reduces the number of parameters that need to be learned and ensures that the model is robust to small translations or shifts in the input, which is particularly useful for images where features often appear in various locations. Third, CNNs also learn features hierarchically, allowing them to recognize simple patterns like edges in early layers and complex structures like objects in deeper layers. This hierarchical learning allows CNNs to capture both local and global patterns in the data, making them highly effective for complex data. For our study, CNNs are particularly beneficial for processing the index-time matrix as images. The index-time matrix can be reshaped into image-like structures, where each pixel represents a specific location in space and time. Treating the index-time matrix as an image allows CNNs to leverage their unique capabilities.

The construction of CNNs involves four main components: (1) convolutional operation; (2) activation; (3) pooling; and (4) fully connected neural networks. In the convolutional layer, units are organized into feature maps that detect local patterns in the data. These feature maps then pass through a nonlinear activation function. After activation, a max pooling layer is applied to downsample the feature maps by selecting the maximum value within each region. This step reduces the number of parameters, which helps prevent overfitting and makes the model more robust to small shifts in the data. In the final stage of the architecture, the outputs from the convolution, activation, and pooling layers are flattened and combined into fully connected neural-network layers, which then generate the model’s forecast of the insurance payoff I​(X)I(X). Note that the insurance payoffs cannot be negative. Therefore, we use the ReLU (Rectified Linear Unit) activation function (σ​(x)=m​a​x​(x,0)\sigma(x)=max(x,0)) in our model to ensure that the predicted insurance payoffs are nonnegative. The illustration of the CNN structures adopted in this study is shown in Figure [2](https://arxiv.org/html/2512.01623v1#S3.F2 "Figure 2 ‣ 3.1.2 Convolutional Neural Networks (CNNs) ‣ 3.1 Neural Network Based Models ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance").

![Refer to caption](cnn_illustration.png)


Figure 2: Illustration of CNN structure.

### 3.2 Penalized Bilevel Programming

Bilevel optimization plays an increasingly important role in machine learning shen2023penalty and is particularly well-suited for problems with a sequential structure where one level of decision is nested within another. In our problem formulation, the insurer’s decision (from solving the UP problem) depends on the outcome of the farmer’s LP problem. This makes bilevel programming algorithms promising for our study.

In general, the structure of a bilevel programming problem can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ​𝒫:minx,y⁡f​(x,y)​ s.t. ​x∈𝒞,y∈𝒮​(x):=arg⁡miny∈𝒰​(x)⁡h​(x,y),\mathcal{BP}:\min\_{x,y}f(x,y)\text{ s.t. }x\in\mathcal{C},y\in\mathcal{S}(x):=\arg\min\_{y\in\mathcal{U}(x)}h(x,y), |  | (6) |

where 𝒞⊆ℝq\mathcal{C}\subseteq\mathbb{R}^{q} is a nonempty, closed set, and 𝒰​(x)\mathcal{U}(x) and 𝒮​(x)\mathcal{S}(x) are nonempty, closed sets given any x∈𝒞x\in\mathcal{C}. The functions ff and hh are referred to as the upper-level and lower-level objectives, respectively.

The bilevel optimization problem ℬ​𝒫\mathcal{BP} is inherently challenging due to the coupling between the upper-level and lower-level problems through the solution set 𝒮​(x)\mathcal{S}(x). In particular, solving ℬ​𝒫\mathcal{BP} can be extremely difficult when the lower-level function h​(x,⋅)h(x,\cdot) is not strongly convex or is constrained, as traditional implicit gradient methods are unable to handle such cases directly. To address these challenges, recent work has explored penalty-based reformulations of ℬ​𝒫\mathcal{BP}, which transform the bilevel problem into a single-level optimization problem by penalizing certain optimality metrics of the lower-level problem.

The penalty reformulation of ℬ​𝒫\mathcal{BP} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ𝒫γ​p:minx,yFγ(x,y)=f(x,y)+γp(x,y) s.t. x∈𝒞,y∈𝒰(x),\mathcal{BP}\_{\gamma p}:\min\_{x,y}F\_{\gamma}(x,y)=f(x,y)+\gamma p(x,y)\text{ s.t. }x\in\mathcal{C},y\in\mathcal{U}(x), |  | (7) |

where p​(x,y)p(x,y) is a penalty function that measures the distance to the lower-level solution set 𝒮​(x)\mathcal{S}(x). We define a squared-distance-bound function to ensure that p​(x,y)p(x,y) approximates the distance from y to 𝒮​(x)\mathcal{S}(x).

###### Definition 1.

(Squared-distance-bound function). A function p:ℝdx×ℝdy↦ℝp:\mathbb{R}^{d\_{x}}\times\mathbb{R}^{d\_{y}}\mapsto\mathbb{R} is a ρ\rho-squared-distance-bound function if there exists ρ>0\rho>0 such that for any x∈𝒞,y∈𝒰​(x)x\in\mathcal{C},y\in\mathcal{U}(x), it holds:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | p​(x,y)≥0,ρ⋅p​(x,y)≥d𝒮​(x)2​(y),\displaystyle p(x,y)\geq 0,\quad\rho\cdot p(x,y)\geq d\_{\mathcal{S}(x)}^{2}(y), |  | (8) |
|  |  | p​(x,y)=0​ if and only if ​d𝒮​(x)​(y)=0,\displaystyle p(x,y)=0\text{ if and only if }d\_{\mathcal{S}(x)}(y)=0, |  |

where d𝒮​(x)​(y)d\_{\mathcal{S}(x)}(y) is the Euclidean distance from yy to the lower-level solution set 𝒮​(x)\mathcal{S}(x).

Given a squared-distance-bound function p​(x,y)p(x,y), we can define an ϵ\epsilon-approximate version of the bilevel problem ℬ​𝒫\mathcal{BP}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ​𝒫ϵ:minx,y⁡f​(x,y)​ s.t. ​x∈𝒞,y∈𝒰​(x),p​(x,y)≤ϵ.\mathcal{BP}\_{\epsilon}:\min\_{x,y}f(x,y)\text{ s.t. }x\in\mathcal{C},y\in\mathcal{U}(x),p(x,y)\leq\epsilon. |  | (9) |

When ϵ=0\epsilon=0, ℬ​𝒫ϵ\mathcal{BP}\_{\epsilon} recovers the original bilevel problem ℬ​𝒫\mathcal{BP}. For ϵ>0\epsilon>0, ℬ​𝒫ϵ\mathcal{BP}\_{\epsilon} serves as an ϵ\epsilon-approximation of ℬ​𝒫\mathcal{BP}, where the lower-level solution yy is within ϵ\epsilon of the true lower-level solution set 𝒮​(x)\mathcal{S}(x).

shen2023penalty show that, under certain generic conditions on h​(x,y)h(x,y) that hold without the strong convexity of h​(x,y)h(x,y), global (local) solutions of ℬ​𝒫\mathcal{BP} can be approximated by solving ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p}. We follow their approach to establish the relationship between ℬ​𝒫\mathcal{BP}, ℬ​𝒫ϵ\mathcal{BP}\_{\epsilon}, and ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p}.

###### Definition 2.

(Lipschitz continuity). Given L>0L>0, a function ℓ:ℝd↦ℝd′\ell:\mathbb{R}^{d}\mapsto\mathbb{R}^{d^{\prime}} is said to be LL-Lipschitz continuous on 𝒳⊆ℝd\mathcal{X}\subseteq\mathbb{R}^{d} if for any x,x′∈𝒳x,x^{\prime}\in\mathcal{X}, it holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ℓ​(x)−ℓ​(x′)‖≤L​‖x−x′‖.\|\ell(x)-\ell(x^{\prime})\|\leq L\|x-x^{\prime}\|. |  | (10) |

###### Assumption 1 (Lipschitz continuity of upper objective).

There exists a constant LL such that for any x∈𝒞x\in\mathcal{C}, the upper-level objective f​(x,⋅)f(x,\cdot) is LL-Lipschitz continuous on 𝒰​(x)\mathcal{U}(x).

According to ([1](https://arxiv.org/html/2512.01623v1#S2.E1 "In 2.2 Distortion Function ‣ 2 Problem Formulation ‣ Monopoly Pricing of Weather Index Insurance")), our UP problem can be simplified to a linear function of order statistics, which is Lipschitz continuous by linearity. Thus, Assumption [1](https://arxiv.org/html/2512.01623v1#Thmassumption1 "Assumption 1 (Lipschitz continuity of upper objective). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") is satisfied directly. The key result that establishes the relationship between ℬ​𝒫\mathcal{BP}, ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p}, and ℬ​𝒫ϵ\mathcal{BP}\_{\epsilon} is the following theorem, which shows that global and local solutions of the penalized problem ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p} correspond to those of the original bilevel problem ℬ​𝒫\mathcal{BP}.

###### Theorem 1 (General Relation on Global Solutions).

Assume p​(x,y)p(x,y) is a ρ\rho-squared-distance-bound function and Assumption [1](https://arxiv.org/html/2512.01623v1#Thmassumption1 "Assumption 1 (Lipschitz continuity of upper objective). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") holds. Given any ϵ1>0\epsilon\_{1}>0, any global solution of ℬ​𝒫\mathcal{BP} is an ϵ1\epsilon\_{1}-global-minimum point of ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p} with any γ≥γ∗=L2​ρ4​ϵ1−1\gamma\geq\gamma^{\*}=\frac{L^{2}\rho}{4}\epsilon\_{1}^{-1}. Conversely, given ϵ2≥0\epsilon\_{2}\geq 0, if (xγ,yγ)(x\_{\gamma},y\_{\gamma}) achieves an ϵ2\epsilon\_{2}-global-minimum of ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p} with γ>γ∗\gamma>\gamma^{\*}, (xγ,yγ)(x\_{\gamma},y\_{\gamma}) is the global solution of ℬ​𝒫ϵγ\mathcal{BP}\_{\epsilon\_{\gamma}} with some ϵγ≤ϵ1+ϵ2γ−γ∗\epsilon\_{\gamma}\leq\frac{\epsilon\_{1}+\epsilon\_{2}}{\gamma-\gamma^{\*}}.

Theorem [1](https://arxiv.org/html/2512.01623v1#Thmtheorem1 "Theorem 1 (General Relation on Global Solutions). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") implies that solving the penalized problem ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p} can yield an approximate solution to the original bilevel problem ℬ​𝒫\mathcal{BP}. The parameter γ\gamma controls the trade-off between the upper-level objective and the penalty term, which ensures that the solution remains close to the lower-level solution set.

###### Theorem 2 (General Relation on Local Solutions).

Assume p​(x,⋅)p(x,\cdot) is continuous for any x∈𝒞x\in\mathcal{C} and p​(x,y)p(x,y) is a ρ\rho-squared-distance-bound function. Given γ>0\gamma>0, let (xγ,yγ)(x\_{\gamma},y\_{\gamma}) be a local solution of ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p} on 𝒩​((xγ,yγ),r)\mathcal{N}((x\_{\gamma},y\_{\gamma}),r), where 𝒩\mathcal{N} is a circle with a center of (xγ,yγ)(x\_{\gamma},y\_{\gamma}) and a radius rr. Assume f​(xγ,⋅)f(x\_{\gamma},\cdot) is LL-Lipschitz continuous on 𝒩​(yγ,r)\mathcal{N}(y\_{\gamma},r). Assume either one of the following is true:
(i) There exists y¯∈𝒩​(yγ,r)\bar{y}\in\mathcal{N}(y\_{\gamma},r) such that y¯∈𝒰​(xγ)\bar{y}\in\mathcal{U}(x\_{\gamma}) and p​(xγ,y¯)≤ϵp(x\_{\gamma},\bar{y})\leq\epsilon for some ϵ≥0\epsilon\geq 0. Define ϵ¯γ=L2​ργ2+2​ϵ\bar{\epsilon}\_{\gamma}=\frac{L^{2}\rho}{\gamma^{2}}+2\epsilon.
(ii) The set 𝒰​(xγ)\mathcal{U}(x\_{\gamma}) is convex and the function p​(xγ,⋅)p(x\_{\gamma},\cdot) is convex. Define ϵ¯γ=L2​ργ2\bar{\epsilon}\_{\gamma}=\frac{L^{2}\rho}{\gamma^{2}}.

Then (xγ,yγ)(x\_{\gamma},y\_{\gamma}) is a local solution of ℬ​𝒫ϵγ\mathcal{BP}\_{\epsilon\_{\gamma}} with ϵγ≤ϵ¯γ\epsilon\_{\gamma}\leq\bar{\epsilon}\_{\gamma}.

Theorem [2](https://arxiv.org/html/2512.01623v1#Thmtheorem2 "Theorem 2 (General Relation on Local Solutions). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") provides conditions under which a local solution of the penalized problem corresponds to a local solution of the original bilevel problem.

To apply this framework, we select the value-gap penalty, p​(x,y)=h​(x,y)−v​(x)p(x,y)=h(x,y)-v(x), where v​(x):=miny′∈𝒰​(x)⁡h​(x,y′)v(x):=\min\_{y^{\prime}\in\mathcal{U}(x)}h(x,y^{\prime}). In our insurance game, the lower-level objective h​(x,⋅)h(x,\cdot) based on CVaR is polyhedral and convex, but not strongly convex. Therefore, we leverage the property of a weak sharp minimum, which holds for polyhedral convex functions on compact sets.

###### Assumption 2 (Weak Sharp Minimum).

The lower-level objective h​(x,⋅)h(x,\cdot) has the property of a weak sharp minimum on the compact set 𝒰​(x)\mathcal{U}(x). That is, there exists a constant κ>0\kappa>0 such that for any x∈𝒞x\in\mathcal{C} and y∈𝒰​(x)y\in\mathcal{U}(x):

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x,y)−v​(x)≥κ⋅d𝒮​(x)​(y).h(x,y)-v(x)\geq\kappa\cdot d\_{\mathcal{S}(x)}(y). |  | (11) |

This assumption allows us to prove that our chosen penalty function satisfies the squared-distance-bound condition required by Theorems [1](https://arxiv.org/html/2512.01623v1#Thmtheorem1 "Theorem 1 (General Relation on Global Solutions). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") and [2](https://arxiv.org/html/2512.01623v1#Thmtheorem2 "Theorem 2 (General Relation on Local Solutions). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance"). According to ([1](https://arxiv.org/html/2512.01623v1#S2.E1 "In 2.2 Distortion Function ‣ 2 Problem Formulation ‣ Monopoly Pricing of Weather Index Insurance")), our LP objective ([4](https://arxiv.org/html/2512.01623v1#S2.E4 "In 2.3 Sequential game ‣ 2 Problem Formulation ‣ Monopoly Pricing of Weather Index Insurance")) can be simplified to a linear function of order statistics, which has a weak sharp minimum if 𝒰​(x)\mathcal{U}(x) is nonempty. Thus, Assumption [2](https://arxiv.org/html/2512.01623v1#Thmassumption2 "Assumption 2 (Weak Sharp Minimum). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") is satisfied directly.

###### Lemma 1 (Value-Gap as a Squared-Distance Bound).

Under Assumption [2](https://arxiv.org/html/2512.01623v1#Thmassumption2 "Assumption 2 (Weak Sharp Minimum). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance"), if the feasible set 𝒰​(x)\mathcal{U}(x) is compact with a uniform diameter DD, then the value-gap penalty p​(x,y)=h​(x,y)−v​(x)p(x,y)=h(x,y)-v(x) is a ρ\rho-squared-distance-bound with ρ=D/κ\rho=D/\kappa.

###### Proof.

By definition, d𝒮​(x)2​(y)=d𝒮​(x)​(y)⋅d𝒮​(x)​(y)d\_{\mathcal{S}(x)}^{2}(y)=d\_{\mathcal{S}(x)}(y)\cdot d\_{\mathcal{S}(x)}(y). Since y∈𝒰​(x)y\in\mathcal{U}(x) and 𝒮​(x)⊂𝒰​(x)\mathcal{S}(x)\subset\mathcal{U}(x), the distance d𝒮​(x)​(y)d\_{\mathcal{S}(x)}(y) is bounded by the diameter DD of 𝒰​(x)\mathcal{U}(x). Thus, d𝒮​(x)2​(y)≤D⋅d𝒮​(x)​(y)d\_{\mathcal{S}(x)}^{2}(y)\leq D\cdot d\_{\mathcal{S}(x)}(y). From Assumption [2](https://arxiv.org/html/2512.01623v1#Thmassumption2 "Assumption 2 (Weak Sharp Minimum). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance"), we have d𝒮​(x)​(y)≤1κ​(h​(x,y)−v​(x))d\_{\mathcal{S}(x)}(y)\leq\frac{1}{\kappa}(h(x,y)-v(x)). Substituting this yields:
d𝒮​(x)2​(y)≤Dκ​(h​(x,y)−v​(x))d\_{\mathcal{S}(x)}^{2}(y)\leq\frac{D}{\kappa}(h(x,y)-v(x)). Setting ρ=D/κ\rho=D/\kappa and p​(x,y)=h​(x,y)−v​(x)p(x,y)=h(x,y)-v(x), we have ρ⋅p​(x,y)≥d𝒮​(x)2​(y)\rho\cdot p(x,y)\geq d\_{\mathcal{S}(x)}^{2}(y). The other conditions follow from the definitions.
∎

By directly applying Theorems [1](https://arxiv.org/html/2512.01623v1#Thmtheorem1 "Theorem 1 (General Relation on Global Solutions). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance")-[2](https://arxiv.org/html/2512.01623v1#Thmtheorem2 "Theorem 2 (General Relation on Local Solutions). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") with ρ=D/κ\rho=D/\kappa, we get the following specific results for our problem.

###### Proposition 1 (Relation on Global Solutions for the Insurance Game).

Assume Assumptions [1](https://arxiv.org/html/2512.01623v1#Thmassumption1 "Assumption 1 (Lipschitz continuity of upper objective). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") and [2](https://arxiv.org/html/2512.01623v1#Thmassumption2 "Assumption 2 (Weak Sharp Minimum). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") hold. Let p​(x,y)=h​(x,y)−v​(x)p(x,y)=h(x,y)-v(x). Suppose γ≥L​(ρ/2)​δ−1\gamma\geq L\sqrt{(\rho/2)\delta^{-1}} with ρ=D/κ\rho=D/\kappa for some δ>0\delta>0. If (xγ,yγ)(x\_{\gamma},y\_{\gamma}) is a global solution of ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p}, then it is a global solution of ℬ​𝒫ϵγ\mathcal{BP}\_{\epsilon\_{\gamma}} with ϵγ≤δ\epsilon\_{\gamma}\leq\delta.

###### Proposition 2 (Relation on Local Solutions for the Insurance Game).

Assume Assumptions [1](https://arxiv.org/html/2512.01623v1#Thmassumption1 "Assumption 1 (Lipschitz continuity of upper objective). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") and [2](https://arxiv.org/html/2512.01623v1#Thmassumption2 "Assumption 2 (Weak Sharp Minimum). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") hold. For some δ>0\delta>0, let p​(x,y)=h​(x,y)−v​(x)p(x,y)=h(x,y)-v(x) and γ≥L​(3​ρ/2)​δ−1\gamma\geq L\sqrt{(3\rho/2)\delta^{-1}} with ρ=D/κ\rho=D/\kappa. If (xγ,yγ)(x\_{\gamma},y\_{\gamma}) is a local solution of ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p}, it is also a local solution of ℬ​𝒫ϵγ\mathcal{BP}\_{\epsilon\_{\gamma}} with ϵγ≤δ\epsilon\_{\gamma}\leq\delta.

Propositions [1](https://arxiv.org/html/2512.01623v1#Thmproposition1 "Proposition 1 (Relation on Global Solutions for the Insurance Game). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") and [2](https://arxiv.org/html/2512.01623v1#Thmproposition2 "Proposition 2 (Relation on Local Solutions for the Insurance Game). ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance") show the relationship between the penalized problem ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p} and the ϵ\epsilon-approxi-
  
mation ℬ​𝒫ϵγ\mathcal{BP}\_{\epsilon\_{\gamma}}. Specifically, the optimal solution of the penalized problem ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p} is a tight approximation for the original problem ℬ​𝒫\mathcal{BP}. We use a stochastic gradient descent method to optimize ℬ​𝒫γ​p\mathcal{BP}\_{\gamma p}. Due to the nonsmoothness of the objectives (linear order statistics ([1](https://arxiv.org/html/2512.01623v1#S2.E1 "In 2.2 Distortion Function ‣ 2 Problem Formulation ‣ Monopoly Pricing of Weather Index Insurance"))), we need to use the subgradient method based on Danskin’s Theorem.

###### Lemma 2 (Danskin’s Theorem for Subgradients).

If h​(x,y)h(x,y) is continuous, convex in yy for each fixed xx, and continuously differentiable in xx for each fixed yy, and the set 𝒰​(x)\mathcal{U}(x) is compact, then the value function v​(x)=miny∈𝒰​(x)⁡h​(x,y)v(x)=\min\_{y\in\mathcal{U}(x)}h(x,y) is directionally differentiable. A subgradient of v​(x)v(x) can be computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇v​(x)∈conv​{∇xh​(x,y∗)∣y∗∈𝒮​(x)}.\nabla v(x)\in\text{conv}\left\{\nabla\_{x}h(x,y^{\*})\mid y^{\*}\in\mathcal{S}(x)\right\}. |  | (12) |

In particular, for any single solution y∗∈𝒮​(x)y^{\*}\in\mathcal{S}(x), the vector ∇xh​(x,y∗)\nabla\_{x}h(x,y^{\*}) is a valid subgradient of v​(x)v(x).

This justifies our algorithm, V-PBGD (Algorithm [1](https://arxiv.org/html/2512.01623v1#alg1 "Algorithm 1 ‣ 3.2 Penalized Bilevel Programming ‣ 3 Model ‣ Monopoly Pricing of Weather Index Insurance")), which approximates this by first finding an approximate lower-level solution y^k\hat{y}^{k} and then using ∇xh​(xk,y^k)\nabla\_{x}h(x^{k},\hat{y}^{k}) as an estimator for ∇v​(xk)\nabla v(x^{k}).

The core of our approach is to apply a gradient-based method to the penalized objective function Fγ​(x,y)F\_{\gamma}(x,y). This requires computing the gradient of the penalty term p​(x,y)=h​(x,y)−v​(x)p(x,y)=h(x,y)-v(x), which in turn requires a value for ∇v​(x)\nabla v(x), the gradient of the lower-level value function.

A key component of this gradient is ∇v​(x)\nabla v(x). As discussed, the nonsmooth nature of h​(x,y)h(x,y) prevents the use of standard envelope theorems. Instead, we rely on Danskin’s Theorem. For our problem, Danskin’s Theorem states that a subgradient of the value function v​(x)v(x) can be computed as ∇xh​(x,y∗)\nabla\_{x}h(x,y^{\*}), where y∗y^{\*} is any optimal solution to the lower-level problem miny⁡h​(x,y)\min\_{y}h(x,y).

This theoretical foundation allows us to formulate a practical algorithm. In practice, computing the exact y∗y^{\*} at each step is computationally expensive. Therefore, for outer iteration kk and given xkx^{k}, we perform a fixed number TkT\_{k} of inner steps of subgradient descent to approximate the solution to the lower-level problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωt+1(k)=ωt(k)−β​∂yh​(xk,ωt(k)),t=1,…,Tk,\omega^{(k)}\_{t+1}=\omega^{(k)}\_{t}-\beta\,\partial\_{y}h(x^{k},\omega^{(k)}\_{t}),\quad t=1,\ldots,T\_{k}, |  | (13) |

with the inner loop initialized with ω1(k)=yk\omega^{(k)}\_{1}=y^{k}. Note that we use ∂yh\partial\_{y}h to denote a subgradient, as the lower-level objective is nonsmooth. This process yields an approximate lower-level solution y^k=ωTk+1(k)\hat{y}^{k}=\omega^{(k)}\_{T\_{k}+1}. We can then approximate the full penalized gradient at (xk,yk)(x^{k},y^{k}) by using this y^k\hat{y}^{k} to serve as a proxy for the true minimizer y∗y^{\*}. The complete update for (xk,yk)(x^{k},y^{k}) is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (xk+1,yk+1)=ProjZ​((xk,yk)−α​(∇f​(xk,yk)+γ​(∂yh​(xk,yk)−∇xh​(xk,y^k)))),(x^{k+1},y^{k+1})=\text{Proj}\_{Z}\left((x^{k},y^{k})-\alpha\left(\nabla f(x^{k},y^{k})+\gamma(\partial\_{y}h(x^{k},y^{k})-\nabla\_{x}h(x^{k},\hat{y}^{k}))\right)\right), |  | (14) |

where Z=𝒞×ℝdyZ=\mathcal{C}\times\mathbb{R}^{d\_{y}} is the feasible set for the variables, α\alpha is the learning rate, and the gradient term ∇xh​(x,y^k)\nabla\_{x}h(x,\hat{y}^{k}) is interpreted as a vector in the joint (x,y)(x,y) space, with zeros in the yy coordinates. This iterative update process is summarized in Algorithm 1, which we refer to as V-PBGD (Value-function-based Penalty Bilevel Gradient Descent).

Algorithm 1  V-PBGD: Function value gap-based fully first-order PBGD

Select (x1,y1)∈Z=𝒞×ℝdy(x^{1},y^{1})\in Z=\mathcal{C}\times\mathbb{R}^{d\_{y}}. Select step sizes α\alpha, β\beta, constant γ\gamma, iteration numbers TkT\_{k}, and KK.

for k=1k=1 to KK do

Initialize ω1(k)=yk\omega^{(k)}\_{1}=y^{k}.

for t=1t=1 to TkT\_{k} do

Update ωt+1(k)=ωt(k)−β​∇yh​(xk,ωt(k))\omega^{(k)}\_{t+1}=\omega^{(k)}\_{t}-\beta\nabla\_{y}h(x^{k},\omega^{(k)}\_{t}).

end for

Set y^k=ωTk+1(k)\hat{y}^{k}=\omega^{(k)}\_{T\_{k}+1}.

Use y^k\hat{y}^{k} to approximate ∇v​(xk)\nabla v(x^{k}) via ∇xh​(xk,y^k)\nabla\_{x}h(x^{k},\hat{y}^{k}).

Update (xk+1,yk+1)=ProjZ​((xk,yk)−α​(∇f​(xk,yk)+γ​(∇yh​(xk,yk)−∇xh​(xk,y^k))))(x^{k+1},y^{k+1})=\text{Proj}\_{Z}\left((x^{k},y^{k})-\alpha(\nabla f(x^{k},y^{k})+\gamma(\nabla\_{y}h(x^{k},y^{k})-\nabla\_{x}h(x^{k},\hat{y}^{k})))\right).

end for

Output (xK,yK)(x^{K},y^{K})

This algorithm effectively manages the computational challenges of bilevel optimization by utilizing the function value-gap penalty and iteratively resolving the lower-level problem using gradient descent. The convergence analysis of the subgradient method can be found in Theorem 2 of shamir2013stochastic

We follow the construction of the function value-gap penalty p​(x,y)=h​(x,y)−v​(x)p(x,y)=h(x,y)-v(x) and evaluate the penalized gradient using ∇v​(x)=∇xh​(x,y∗)\nabla v(x)=\nabla\_{x}h(x,y^{\*}), where y∗∈𝒮​(x)y^{\*}\in\mathcal{S}(x) is the lower-level problem solution. We then propose the following combined single objective for our first bilevel problem (feasible set 𝒫s​1\mathcal{P}\_{s1}) in searching for optimal insurance strategies:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | minθ,Iθ​(𝐗)−(Π​(Iθ​(𝐗))−(1+μ)​𝔼​(Iθ​(𝐗)))+γ⋅(LP​(Iθ​(𝐗))−LP​(I^θ​(𝐗)))\displaystyle\min\_{\theta,I^{\theta}(\mathbf{X})}-\left(\Pi(I^{\theta}(\mathbf{X}))-(1+\mu)\mathbb{E}\left(I^{\theta}(\mathbf{X})\right)\right)+\gamma\cdot\left(\text{LP}(I^{\theta}(\mathbf{X}))-\text{LP}(\hat{I}^{\theta}(\mathbf{X}))\right) |  | (15) |
|  |  | s.t. |  |
|  |  | I^θ​(𝐗)​ is the solution to the farmer’s LP problem in ([4](https://arxiv.org/html/2512.01623v1#S2.E4 "In 2.3 Sequential game ‣ 2 Problem Formulation ‣ Monopoly Pricing of Weather Index Insurance")).\displaystyle\quad\hat{I}^{\theta}(\mathbf{X})\text{ is the solution to the farmer's LP problem in }\eqref{eq:LP}. |  |

Here:

* •

  LP(Iθ(𝐗))=ρF(Y−Iθ(𝐗)+Π(Iθ(𝐗))\text{LP}(I^{\theta}(\mathbf{X}))=\rho\_{F}\left(Y-I^{\theta}(\mathbf{X})+\Pi({I^{\theta}(\mathbf{X})}\right) with ρF\rho\_{F} being the risk measure for the farmer, IθI^{\theta} is the indemnity function under the risk-loading factor θ\theta, and Π​(Iθ​(𝐗))\Pi({I^{\theta}(\mathbf{X})}) is formulated by the expectation premium principle Π​(I​(𝐗))=(1+θ)​𝔼​(I​(𝐗))\Pi(I(\mathbf{X}))=(1+\theta)\mathbb{E}(I(\mathbf{X}));
* •

  γ>0\gamma>0 is the penalty factor;
* •

  μ≥0\mu\geq 0 is the fixed administrative cost factor.

This formulation ensures that the penalty term promotes the optimality of the lower-level problem while maintaining the structure of the original bilevel objective.

The pseudo-code for our penalized bilevel algorithm for Problem 1 is shown below.

Algorithm 2  Penalty-Based Bilevel Gradient Descent (PBGD) for Problem 1 (feasible set 𝒫s​1\mathcal{P}\_{s1})

Input: Neural networks θn​n\theta\_{nn}, I^n​nθ\hat{I}^{\theta}\_{nn}, and In​nθI^{\theta}\_{nn}; initial learning rate α0\alpha\_{0}, exponential decay factor λ=0.96\lambda=0.96; penalty constant γ\gamma; administrative cost factor μ\mu; number of LP objective iterations NLN\_{L}; number of combined objective iterations NCN\_{C}

for each iteration nC=1,…,NCn\_{C}=1,\ldots,N\_{C} do
⊳\triangleright Inner decay restarts each combined objective iteration

for each LP objective iteration nL=1,…,NLn\_{L}=1,\ldots,N\_{L} do

Assign the weights from In​nθI^{\theta}\_{nn} to I^n​nθ\hat{I}^{\theta}\_{nn};

Compute inner step size αnL(L)←α0⋅λnL=α0⋅0.96nL\alpha^{(L)}\_{n\_{L}}\leftarrow\alpha\_{0}\cdot\lambda^{n\_{L}}=\alpha\_{0}\cdot 0.96^{n\_{L}};

Update I^n​nθ\hat{I}^{\theta}\_{nn} by gradient descent on the LP objective (equation (1)) with step size αnL(L)\alpha^{(L)}\_{n\_{L}};

end for

Compute LP​(I^θ​(𝐗))\text{LP}(\hat{I}^{\theta}(\mathbf{X})) using I^n​nθ\hat{I}^{\theta}\_{nn};

Compute penalty γ⋅(LP​(Iθ​(𝐗))−LP​(I^θ​(𝐗)))\gamma\cdot\left(\text{LP}(I^{\theta}(\mathbf{X}))-\text{LP}(\hat{I}^{\theta}(\mathbf{X}))\right);

Compute combined objective −(Π​(Iθ​(𝐗))−(1+μ)​𝔼​(Iθ​(𝐗)))+γ⋅(LP​(Iθ​(𝐗))−LP​(I^θ​(𝐗)))-\left(\Pi(I^{\theta}(\mathbf{X}))-(1+\mu)\mathbb{E}(I^{\theta}(\mathbf{X}))\right)+\gamma\cdot\left(\text{LP}(I^{\theta}(\mathbf{X}))-\text{LP}(\hat{I}^{\theta}(\mathbf{X}))\right);

Compute outer step size αnC(C)←α0⋅λnC=α0⋅0.96nC\alpha^{(C)}\_{n\_{C}}\leftarrow\alpha\_{0}\cdot\lambda^{n\_{C}}=\alpha\_{0}\cdot 0.96^{n\_{C}};

Update θn​n\theta\_{nn} and In​nθI^{\theta}\_{nn} by gradient descent to minimize the combined objective (equation (14)) with step size αnC(C)\alpha^{(C)}\_{n\_{C}};

end for

Output: Optimal θ\theta and I​(𝐗)I(\mathbf{X}).

The PBGD algorithms for Problems 2 and 3 can be adapted from the above algorithm with some adjustments. For Problem 2, the premium function changes to a distortion premium principle with a power distortion function gi​(s)=s1ρg\_{i}(s)=s^{\frac{1}{\rho}}. This means that the insurer optimizes for two parameters θ\theta and ρ\rho in this case and the combined objective becomes −(Π​(Iθ,ρ​(𝐗))−(1+μ)​𝔼​(Iθ,ρ​(𝐗)))+γ⋅(LP​(Iθ,ρ​(𝐗))−LP​(I^θ,ρ​(𝐗)))-\left(\Pi(I^{\theta,\rho}(\mathbf{X}))-(1+\mu)\mathbb{E}(I^{\theta,\rho}(\mathbf{X}))\right)+\gamma\cdot\left(\text{LP}(I^{\theta,\rho}(\mathbf{X}))-\text{LP}(\hat{I}^{\theta,\rho}(\mathbf{X}))\right). The algorithm then updates for θn​n\theta\_{nn}, ρn​n\rho\_{nn}, and In​nθI^{\theta}\_{nn}. For Problem 3, we use a neural network to model both the insurance payoff function Ig​(𝐗)I^{g}(\mathbf{X}), and the difference in pricing function gi​(s)g\_{i}(s). The algorithm in this case optimizes for gn​ng\_{nn} and In​ngI^{g}\_{nn}.

## 4 Data

### 4.1 Production Loss and Farmer’s Wealth Data

We analyze annual county-level soybean data for Iowa from the National Agricultural Statistics Service (NASS), covering 1940-2023. Iowa accounts for a substantial share of U.S. soybean acreage, and the long historical record enables robust analysis of production losses. To achieve stationarity in yields, we detrend county-level soybean yields using a second-order polynomial in time estimated via robust regression and adjust for heteroscedasticity. Following deng2007there and harri2011relaxing, we normalize historical yields to the 2023 price level so that interannual deviations are comparable over time. This detrending mitigates long-run influences such as climate trends and technological change (e.g., in genetics, management, and equipment), while preserving interannual variability relevant for loss analysis.

Given that the yield data are available only at an annual frequency, the number of historical observations is relatively limited compared with the high-dimensional weather covariates used in this study. To address this limitation, we assume that crop yield losses are homogeneous across time and space. This assumption expands our data set to 3,780 county-years (45 counties ×\times 84 years).

In our analysis, we minimize the risk associated with fluctuations in crop yields by working with production losses rather than raw yields. For each observation nn, we define the loss as the shortfall from the maximum observed yield (max\_yield−yieldn)\text{max\\_yield}-\text{yield}\_{n})), multiplied by a normalized price (pp):

|  |  |  |
| --- | --- | --- |
|  | Yn=(max\_yield−yieldn)×p,n=1,…,3780,Y\_{n}=(\text{max\\_yield}-\text{yield}\_{n})\times p,\quad n=1,\ldots,3780, |  |

where p=1p=1 denotes one price unit. Monetary quantities are expressed in price-indexed units per acre, with the price index normalized to one.

The equilibrium solutions satisfy scale invariance, which is guaranteed by Choquet integral representations. This means that scaling all payoffs by any positive factor scales the objectives but leaves the equilibrium allocations and policies unchanged.

### 4.2 Climate and Weather Index Data

The weather data used in this study are obtained from the PRISM Climate Group,222PRISM is the USDA’s official climatological data set, available at <http://prism.oregonstate.edu/>. which provides detailed monthly meteorological data for the contiguous United States at a 4-km spatial resolution. The data set includes six climate variables: precipitation, maximum and minimum temperatures, maximum and minimum vapor pressure deficits, and dew points, spanning from 1940 to 2023. These variables form a 7​indeces×12​months7~\text{indeces}\times 12~\text{months}-dimensional weather index matrix, which is essential for designing an optimal insurance policy. The weather indices used in this study are summarized in Table [1](https://arxiv.org/html/2512.01623v1#S4.T1 "Table 1 ‣ 4.2 Climate and Weather Index Data ‣ 4 Data ‣ Monopoly Pricing of Weather Index Insurance").

The relationship between weather indices and crop production losses is often nonlinear and complex due to biological and environmental factors (schlenker2009nonlinear; rigden2020combined). Additionally, interactions between weather indices can compound their impact on yield losses. For example, while minimum vapor pressure deficit in October and precipitation in October may not individually influence production losses, their combined effect can create a substantial and nonlinear impact. These complexities highlight the limitations of linear models, which are commonly used in existing index insurance contracts.
This underscores the need for more sophisticated models in insurance design.

Table 1: Weather Indices

| Variable | Description |
| --- | --- |
| pcpnk | Total precipitation (rain and melted snow) for month kk (mm) |
| tmaxk | Daily maximum temperature averaged over all days in month kk (°C) |
| tmink | Daily minimum temperature averaged over all days in month kk (°C) |
| dptk | Daily mean dew point temperature averaged over all days in month kk (°C) |
| vpdmaxk | Daily maximum vapor pressure deficit averaged over all days in month kk (hPa) |
| vpdmink | Daily minimum vapor pressure deficit averaged over all days in month kk (hPa) |
| kk | Calendar month, k=1,2,…,12k=1,2,\ldots,12 for January-December |

Notes. This table summarizes the weather variables available from the PRISM data set. The sample period is from 1940 to 2023.

## 5 Numerical Results

The numerical results presented in this section are structured as follows: Section [5.1.1](https://arxiv.org/html/2512.01623v1#S5.SS1.SSS1 "5.1.1 Fully Connected Neural Networks ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the training and equilibrium results for insurance payoffs, I​(X)I(X), modeled using fully connected NNs. Section [5.1.2](https://arxiv.org/html/2512.01623v1#S5.SS1.SSS2 "5.1.2 Sensitivity Analysis ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") presents a sensitivity analysis using fully connected neural networks, varying the parameters λ\lambda and ρ\rho in the farmer’s distortion functions gf​(s)=λ​s+(1−λ)​min⁡{s1−α,1}g\_{f}(s)=\lambda s+(1-\lambda)\min\left\{\frac{s}{1-\alpha},1\right\} and gf​(s)=s1ρg\_{f}(s)=s^{\frac{1}{\rho}}, respectively. The sensitivity analysis is conducted for both index and indemnity insurance. Section [5.1.3](https://arxiv.org/html/2512.01623v1#S5.SS1.SSS3 "5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") presents training and equilibrium results when CNNs are used to model the insurance payoff function I​(X)I(X). A comparison of the resulting insurance payoff functions I​(X)I(X) is also presented in this section. Section [5.2](https://arxiv.org/html/2512.01623v1#S5.SS2 "5.2 Problem 2 (𝒫_{𝑠⁢2}): Two-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") extends the insurer’s pricing strategy to a two-parameter case, in which the insurer chooses both θ\theta, the risk-loading factor, and ρ\rho in its premium distortion function gi​(s)=s1ρg\_{i}(s)=s^{\frac{1}{\rho}}. Section [5.3](https://arxiv.org/html/2512.01623v1#S5.SS3 "5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") further extends the analysis to a general pricing strategy for the insurer, where neural networks are used to model both the insurance payoff I​(X)I(X) and the insurer’s pricing function gig\_{i}.

### 5.1 Problem 1 (𝒫s​1\mathcal{P}\_{s1}): One-parameter Premium Model

#### 5.1.1 Fully Connected Neural Networks

This section presents the numerical solutions to the bilevel optimization Problem 1 when fully connected NNs are used to model the insurance payoff function. The model validation results used to select the optimal model are shown in Table [2](https://arxiv.org/html/2512.01623v1#S5.T2 "Table 2 ‣ 5.1.1 Fully Connected Neural Networks ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

Table 2: Model Validation of Neural Networks (λ=0\lambda=0).

| Single hidden layer | [8] | | [16] | | [32] | | [64] | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Train | Validation | Train | Validation | Train | Validation | Train | Validation |
| UP Loss | -3.1783 | -3.1485 | -0.0005 | -0.0012 | -0.0597 | -0.0495 | 0.0000 | 0.0000 |
| Penalized Loss | -2.9113 | -5.2283 | 0.0056 | -0.0142 | -0.0936 | 0.0279 | 0.0000 | 0.0000 |
| Multiple hidden layers | [8 - 8] | | [8 - 8 - 8] | | [8 - 8 - 8 - 8] | | [8 - 8 - 8 - 8 - 8] | |
| Train | Validation | Train | Validation | Train | Validation | Train | Validation |
| UP Loss | -3.5495 | -3.6050 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Penalized Loss | -3.6556 | -3.6752 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

Figure [3](https://arxiv.org/html/2512.01623v1#S5.F3 "Figure 3 ‣ 5.1.1 Fully Connected Neural Networks ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the convergence of the UP and LP loss curves for index insurance, where the farmer’s risk measure is gf​(s)=0.5​s+0.5​min⁡{s1−α,1}​with​α=0.8g\_{f}(s)=0.5s+0.5\min\left\{\frac{s}{1-\alpha},1\right\}~\text{with}~\alpha=0.8. The upper-problem loss curve stabilizes around -1.6068, which indicates an equilibrium profit of 1.6068 for the insurer. The lower-problem loss stabilizes around 42.4050, which indicates that the farmer’s risk measure at equilibrium is 42.4050. The weighting parameter λ\lambda between CVaR and the expected risk adjusts the risk appetite of the farmer. A higher λ\lambda leads to less weight assigned to the CVaR component, which means that the farmer is less risk averse than if she had CVaR as its risk measure. The optimal insurance payoff for this case with the convex-combination risk measure is shown in Figure [4(a)](https://arxiv.org/html/2512.01623v1#S5.F4.sf1 "In Figure 4 ‣ 5.1.1 Fully Connected Neural Networks ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). In equilibrium, the optimal risk-loading factor θ∗\theta^{\*} for the insurer is 0.4130, which leads to a profit of 1.6086. The optimal insurance payoff function exhibits a stop-loss pattern. We make a comparison here with indemnity insurance, which is based directly on the loss YY. For indemnity insurance under the same risk measure for the farmer (convex-combination risk measure), the optimal risk-loading factor for the insurer is θ∗=0.2812\theta^{\*}=0.2812, which corresponds to a profit of 2.3633. The payoff function in this case of indemnity insurance is stop-loss, as shown in Figure [4(b)](https://arxiv.org/html/2512.01623v1#S5.F4.sf2 "In Figure 4 ‣ 5.1.1 Fully Connected Neural Networks ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

![Refer to caption](x1.png)


(a) Upper-problem loss

![Refer to caption](x2.png)


(b) Lower-problem loss

Figure 3: Training curves of using NN to model insurance payoff under the farmer’s risk distortion function gf​(s)=0.5​s+0.5​min⁡{s1−α,1}​with​α=0.8g\_{f}(s)=0.5s+0.5\min\left\{\frac{s}{1-\alpha},1\right\}~\text{with}~\alpha=0.8. Figure (a) shows the evolution of the upper-problem loss (negative insurer’s profit) across iterations. Figure (b) depicts the evolution of the lower-problem loss (farmer’s risk measure) across iterations.

In addition, we change the farmer’s risk measure to pure CVaR (λ=0\lambda=0 in the convex-combination risk measure) and investigate the equilibrium solution in this sequential game with a more risk-averse farmer than in the previous case. The insurer’s optimal risk loading in the equilibrium solution is θ∗=0.5500\theta^{\*}=0.5500, which corresponds to a profit of 3.5495. Note that the risk loading θ\theta and profit are higher than in the previous case. The optimal payoff function, which shows a stop-loss pattern, is shown in Figure [4(c)](https://arxiv.org/html/2512.01623v1#S5.F4.sf3 "In Figure 4 ‣ 5.1.1 Fully Connected Neural Networks ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). cai2008optimal show that stop-loss insurance is optimal under the CVaR risk measure, which supports our study. We also compare with indemnity insurance under the same risk measure. The optimal risk loading is θ∗=0.4853\theta^{\*}=0.4853, which corresponds to a profit of 4.8277. The risk loading θ∗\theta^{\*} is lower and the profit is higher for indemnity insurance than for index insurance, which could be caused by the existence of basis risk in index insurance. This outcome is also observed in the previous case of convex-combination risk measure. Moreover, the optimal insurance payoff functions for both types of insurance contracts have similar shapes, but the insurance payoff functions for index insurance have more noise in the payoff patterns compared to those for indemnity insurance. The noise in the index insurance payoff functions is also observed in (chen2024managing).

![Refer to caption](x3.png)


(a)

![Refer to caption](x4.png)


(b)

![Refer to caption](x5.png)


(c)

![Refer to caption](x6.png)


(d)

Figure 4: Comparison of equilibrium solutions under risk measure CVaR and convex combination for Index and indemnity insurance. Figures (a) and (b) show the optimal insurance payoff functions for index and indemnity insurance respectively. The farmer’s risk distortion function adopted in these two figures is the convex combination of CVaR and expected risk gf​(s)=0.5​s+0.5​min⁡{s1−α,1}g\_{f}(s)=0.5s+0.5\min\left\{\frac{s}{1-\alpha},1\right\} with α=0.8\alpha=0.8. Figures (c) and (d) illustrate a different scenario where the farmer’s risk distortion risk measure is CVaR with α=0.8\alpha=0.8.

#### 5.1.2 Sensitivity Analysis

In the first sensitivity analysis, we vary the weighting parameter in the distortion function gf​(s)=λ​s+(1−λ)⋅min⁡{s1−α,1}g\_{f}(s)=\lambda s+(1-\lambda)\cdot\min\{\frac{s}{1-\alpha},1\}. The comparison of insurance coverage for α=0.95\alpha=0.95 and λ=0.1,0.5,0.9\lambda=0.1,0.5,0.9 is shown in Figure [5(a)](https://arxiv.org/html/2512.01623v1#S5.F5.sf1 "In Figure 5 ‣ 5.1.2 Sensitivity Analysis ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). We observe that a higher λ\lambda leads to higher deductibles. The same pattern is consistent for the indemnity insurance shown in Figure [5(b)](https://arxiv.org/html/2512.01623v1#S5.F5.sf2 "In Figure 5 ‣ 5.1.2 Sensitivity Analysis ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

The second sensitivity analysis involves varying the parameter ρ\rho in the distortion function gi​(s)=s1ρg\_{i}(s)=s^{\frac{1}{\rho}} for the premium. We compare the optimal risk-loading factor θ\theta for α=0\alpha=0 and ρ=1.0,1.5,2\rho=1.0,1.5,2. As shown in Figure [5(c)](https://arxiv.org/html/2512.01623v1#S5.F5.sf3 "In Figure 5 ‣ 5.1.2 Sensitivity Analysis ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"), a larger ρ\rho leads to slightly higher deductibles. The same pattern is also observed for the indemnity insurance in Figure [5(d)](https://arxiv.org/html/2512.01623v1#S5.F5.sf4 "In Figure 5 ‣ 5.1.2 Sensitivity Analysis ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). The summary of the optimal risk-loading factor θ∗\theta^{\*} found in the two sensitivity studies is shown in Table [3](https://arxiv.org/html/2512.01623v1#S5.T3 "Table 3 ‣ 5.1.2 Sensitivity Analysis ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). We do not allow a negative loading factor θ\theta in the final solution, as this leads to an arbitrage opportunity for the farmer. If θ\theta would be negative, an arbitrage opportunity would exist since we do not restrict the coverage to be strictly smaller than or equal to the actual loss.

![Refer to caption](x7.png)


(a)

![Refer to caption](x8.png)


(b)

![Refer to caption](x9.png)


(c)

![Refer to caption](x10.png)


(d)

Figure 5: Sensitivity analysis based on λ\lambda and ρ\rho. The impact of λ\lambda on the equilibrium solution for index and indemnity insurance are shown in Figure (a) and (b) respectively. Figure (a) demonstrates the difference in optimal insurance payoff I∗​(𝐗)I^{\*}(\mathbf{X}) when the parameter λ\lambda changes between 0.1, 0.5 and 0.9 in the farmer’s risk distortion function gf​(s)=λ​s+(1−λ)⋅min⁡{s1−α,1}g\_{f}(s)=\lambda s+(1-\lambda)\cdot\min\{\frac{s}{1-\alpha},1\}. Figure (b) shows the same impact of changing λ\lambda on the optimal insurance coverage but on indemnity insurance, where the insurance contract is directly written on the loss YY.
The impact of ρ\rho on insurance payoff function for index and indemnity insurance under insurer’s premium distortion function gi​(s)=s1ρg\_{i}(s)=s^{\frac{1}{\rho}} are shown in Figure (c) and (d), respectively. Figure (c) shows the difference in insurance payoff when ρ\rho changes between 1, 1.5 and 2. Figure (d) shows similar differences in the insurance payoff but for indemnity insurance.




Table 3: Summary of the two sensitivity analyses.

|  | I​(𝐗)I(\mathbf{X}) | | | I​(𝐘)I(\mathbf{Y}) | | |
| --- | --- | --- | --- | --- | --- | --- |
| λ\lambda | 0.1 | 0.5 | 0.9 | 0.1 | 0.5 | 0.9 |
| θ∗\theta^{\*} | 0.7542 | 0.5578 | 0.3068 | 0.6451 | 0.3724 | 0.2591 |
| ρ\rho | 1.0 | 1.5 | 2 | 1.0 | 1.5 | 2 |
| θ∗\theta^{\*} | 1.0181 | 1.0333 | 1.0802 | 0.8796 | 0.9382 | 0.9855 |

#### 5.1.3 Convolutional Neural Networks (CNNs)

This subsection investigates numerical solutions to the same optimization problem (Problem 1) as in the previous subsection, using CNNs to model the insurance payoff function.

Figure [6](https://arxiv.org/html/2512.01623v1#S5.F6 "Figure 6 ‣ 5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the convergence of the loss curves when CNNs are used to model the insurance payoff function, where the farmer’s risk measure is the convex combination of CVaR and expected risk: gf​(s)=0.5​s+0.5​min⁡{s1−α,1}​with​α=0.8g\_{f}(s)=0.5s+0.5\min\left\{\frac{s}{1-\alpha},1\right\}~\text{with}~\alpha=0.8. The upper-problem loss curve stabilizes around -2.2553, indicating an equilibrium profit of 2.2553 for the insurer. The lower-problem loss curve stabilizes around 40.4945, indicating the farmer’s risk measure at equilibrium. The model validation results for CNN models are shown in Table [4](https://arxiv.org/html/2512.01623v1#S5.T4 "Table 4 ‣ 5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

![Refer to caption](x11.png)


(a) UP Loss

![Refer to caption](x12.png)


(b) LP loss

Figure 6: Training curves for using CNNs to model the insurance payoff under the farmer’s risk distortion function gf​(s)=0.5​s+0.5​min⁡{s1−α,1}​with​α=0.8g\_{f}(s)=0.5s+0.5\min\left\{\frac{s}{1-\alpha},1\right\}~\text{with}~\alpha=0.8. Figure (a) shows the evolution of the upper-problem loss (the negative of the insurer’s profit) across iterations. Figure (b) shows the evolution of the lower-problem loss (the farmer’s risk measure) across iterations.




Table 4: Model Validation for Convolutional Neural Networks (λ=0\lambda=0).

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Convolutional  Layers | [16 - 16] | | [32 - 32] | | [16 - 16 - 16] | | [32 - 32- 32] | |
| Training | Validation | Training | Validation | Training | Validation | Training | Validation |
| UP Loss | 0.0000 | 0.0000 | -4.0703 | -4.0801 | 0.0000 | 0.0000 | 0.2473 | 0.2377 |
| Penalized Loss | 0.0000 | 0.0000 | -4.2847 | -3.7446 | 0.0000 | 0.0000 | 2.8403 | 0.8297 |
| Fully connected layers  (single hidden layer) | [8] | | [16] | | [32] | | [64] | |
| Training | Validation | Training | Validation | Training | Validation | Training | Validation |
| UP Loss | -4.2222 | -4.3253 | -4.0660 | -4.1693 | -4.0703 | -4.0801 | -3.6794 | -3.7555 |
| Penalized Loss | -11.2273 | -5.5120 | -3.6540 | -5.2039 | -4.2847 | -3.7446 | -5.1027 | -4.2090 |
| Fully connected layers  (multiple hidden layers) | [32 - 32] | | [32 - 32 - 32] | | [32 - 32 - 32 - 32] | | [32 - 32 - 32 - 32 - 32] | |
| Training | Validation | Training | Validation | Training | Validation | Training | Validation |
| UP Loss | 0.0000 | 0.0000 | -4.0317 | -4.0989 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Penalized Loss | 0.0000 | 0.0000 | -6.0228 | -2.6661 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

Figure [7](https://arxiv.org/html/2512.01623v1#S5.F7 "Figure 7 ‣ 5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") compares the insurance payoff functions I​(𝐗)I(\mathbf{X}) modeled using CNNs under two different risk measures (CVaR and convex combination). Figure [7(a)](https://arxiv.org/html/2512.01623v1#S5.F7.sf1 "In Figure 7 ‣ 5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the case in which the convex combination of CVaR and expected risk is used as the farmer’s risk measure. The optimal risk-loading factor θ∗\theta^{\*} and profit for the insurer in this case are 0.3182 and 2.2553, respectively. Figure [7(b)](https://arxiv.org/html/2512.01623v1#S5.F7.sf2 "In Figure 7 ‣ 5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the scenario in which the farmer’s risk measure is set to CVaR; the optimal risk-loading factor and the insurer’s profit are 0.3961 and 4.0703, respectively. Note that the insurance payoff function modeled using CNNs contains less noise in the payoff patterns than those modeled using NNs, which demonstrates the ability of CNNs to reduce noise and produce more robust models. In addition, the profits obtained using CNNs to model the insurance payoff function are closer to those of indemnity insurance. This outcome holds under both risk measures considered in this study. This is due to the fact that the insurance payoff function modeled using CNNs contains less noise and thus less basis risk. This highlights the potential of CNNs in reducing the basis risk in index insurance pricing strategies and achieving an optimal solution closer to that of indemnity insurance. The differences in the optimal insurance payoff functions can be seen by comparing Figure [4](https://arxiv.org/html/2512.01623v1#S5.F4 "Figure 4 ‣ 5.1.1 Fully Connected Neural Networks ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") for the NNs with Figure [7](https://arxiv.org/html/2512.01623v1#S5.F7 "Figure 7 ‣ 5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). A summary of the equilibrium solutions under the two risk measures and the two modeling strategies for the insurance payoff function is shown in Table [5](https://arxiv.org/html/2512.01623v1#S5.T5 "Table 5 ‣ 5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

Table 5: Summary of Equilibrium Solutions for Bilevel Optimization Problem 1.

| Models | Risk Measure | θ∗\theta^{\*} | | Profit | |
| --- | --- | --- | --- | --- | --- |
| Index | Indemnity | Index | Indemnity |
| NN | Combination | 0.4130 | 0.2812 | 1.6086 | 2.3633 |
| CVaR | 0.5500 | 0.4853 | 3.5495 | 4.8277 |
| CNN | Combination | 0.3182 | 0.2812 | 2.2553 | 2.3633 |
| CVaR | 0.3961 | 0.4853 | 4.0703 | 4.8277 |



![Refer to caption](x13.png)


(a)

![Refer to caption](x14.png)


(b)

Figure 7: Comparison of equilibrium solutions under risk measure CVaR and convex combination with CNN used for modeling insurance payoff. Figure (a) demonstrates the optimal insurance payoff function under farmer’s risk distortion gf​(s)=0.5​s+0.5​min⁡{s1−α,1}g\_{f}(s)=0.5s+0.5\min\left\{\frac{s}{1-\alpha},1\right\} with α=0.8\alpha=0.8. The insurer’s optimal risk loading is θ∗=0.3182\theta^{\*}=0.3182 with a profit of 2.2553 in this case. Figure (b) shows the optimal insurance payoff function under farmer’s risk measure being CVaR. The insurer’s optimal risk loading for this case is θ∗=0.3961\theta^{\*}=0.3961 with a profit of 4.0703.

### 5.2 Problem 2 (𝒫s​2\mathcal{P}\_{s2}): Two-parameter Premium Model

This subsection presents the numerical solutions to the bilevel optimization Problem 2. In this setting, the insurer selects two parameters: risk-loading factor θ\theta and the premium distortion factor ρ\rho in its pricing strategy. The farmer’s risk measure is based on the distortion function gf​(s)=λ​s+(1−λ)⋅min⁡{s1−α,1},with​α=0.8g\_{f}(s)=\lambda s+(1-\lambda)\cdot\min\{\frac{s}{1-\alpha},1\},~\text{with}~\alpha=0.8. We vary the weighting factor λ\lambda between 0.1, 0.5, and 0.7 in this problem to see differences in the equilibrium solutions. The model validation results for selecting the best model for this two-parameter optimization problem are shown in Table [6](https://arxiv.org/html/2512.01623v1#S5.T6 "Table 6 ‣ 5.2 Problem 2 (𝒫_{𝑠⁢2}): Two-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

Table 6: Model Validation for CNN in the two-parameter optimization case (λ=0\lambda=0).

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Convolutional  Layers | [16 - 16] | | [32 - 32] | | [16 - 16 - 16] | | [32 - 32- 32] | |
| Training | Validation | Training | Validation | Training | Validation | Training | Validation |
| UP Loss | 0.0000 | 0.0000 | -7.7488 | -7.9577 | 0.0000 | 0.0000 | -8.2615 | -8.3879 |
| Penalized Loss | 0.0000 | 0.0000 | -6.3389 | -7.3672 | 0.0000 | 0.0000 | -7.1449 | -6.4417 |
| Fully connected layers  (single hidden layer) | [8] | | [16] | | [32] | | [64] | |
| Training | Validation | Training | Validation | Training | Validation | Training | Validation |
| UP Loss | -7.6739 | -7.7602 | -7.5128 | -7.5883 | -7.7870 | -8.1214 | -8.2000 | -8.3904 |
| Penalized Loss | -4.6893 | -8.5636 | -9.2603 | -10.5043 | -8.6762 | -10.6711 | -7.6511 | -9.4009 |
| Fully connected layers  (multiple hidden layers) | [64 - 64] | | [64 - 64 - 64] | | [64 - 64 - 64 - 64] | | [64 - 64 - 64 - 64 - 64] | |
| Training | Validation | Training | Validation | Training | Validation | Training | Validation |
| UP Loss | -8.3950 | -8.5892 | -8.2634 | -8.5726 | -8.0183 | -8.0700 | 0.0000 | 0.0000 |
| Penalized Loss | -16.4543 | -12.8822 | -12.2764 | -5.6959 | -4.2467 | -7.8628 | 0.0000 | 0.0000 |

Note: The optimal model is the one with the lowest validation UP loss given that the absolute difference between validation UP loss and validation penalized loss is below 2.

Figure [8](https://arxiv.org/html/2512.01623v1#S5.F8 "Figure 8 ‣ 5.2 Problem 2 (𝒫_{𝑠⁢2}): Two-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the optimal insurance payoff functions for different values of λ\lambda in the farmer’s risk distortion function gf​(s)=λ​s+(1−λ)​min⁡{s1−α,1}g\_{f}(s)=\lambda s+(1-\lambda)\min\left\{\frac{s}{1-\alpha},1\right\}. For λ=0.1\lambda=0.1, the optimal values for the two parameters are θ∗=0.2237\theta^{\*}=0.2237 and ρ=2.0644\rho=2.0644, which corresponds to a profit of 7.4848.
For λ=0.5\lambda=0.5, the equilibrium solutions are θ∗=0.0758\theta^{\*}=0.0758 and ρ=1.7341\rho=1.7341, which leads to an expected profit of
4.2511. For λ=0.7\lambda=0.7, the equilibrium solutions are θ∗=0.0190\theta^{\*}=0.0190 and ρ=1.5016\rho=1.5016, which corresponds to a profit of 2.1893. The insurance payoff pattern exhibits the limited stop-loss insurance with both a deductible and a maximum benefit. A more risk-averse farmer (λ=0.1\lambda=0.1) leads to larger θ\theta and ρ\rho compared to a less risk-averse farmer (λ=0.7\lambda=0.7) as shown in Figure [8(a)](https://arxiv.org/html/2512.01623v1#S5.F8.sf1 "In Figure 8 ‣ 5.2 Problem 2 (𝒫_{𝑠⁢2}): Two-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") and Figure [8(c)](https://arxiv.org/html/2512.01623v1#S5.F8.sf3 "In Figure 8 ‣ 5.2 Problem 2 (𝒫_{𝑠⁢2}): Two-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). For an even less risk-averse farmer (λ>0.7)\lambda>0.7), there is no insurance.

We compare the solutions for index insurance with those for indemnity insurance. The profits obtained for indemnity insurance are higher for all three values of λ\lambda. A summary of the equilibrium solutions for Problem 2 is shown in Table [7](https://arxiv.org/html/2512.01623v1#S5.T7 "Table 7 ‣ 5.2 Problem 2 (𝒫_{𝑠⁢2}): Two-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

Table 7: Summary of Equilibrium Solutions for Bilevel Optimization Problem 2.

| λ\lambda | θ∗\theta^{\*} | | ρ∗\rho^{\*} | | Expected Profit | |
| --- | --- | --- | --- | --- | --- | --- |
| Index | Indemnity | Index | Indemnity | Index | Indemnity |
| 0.1 | 0.2237 | 0.2761 | 2.0644 | 1.7078 | 7.4848 | 11.3735 |
| 0.5 | 0.0758 | 0.1022 | 1.7341 | 1.5641 | 4.2511 | 6.7666 |
| 0.7 | 0.0190 | 0.0258 | 1.5016 | 1.4565 | 2.1893 | 4.3443 |



![Refer to caption](x15.png)


(a) ES:θ=0.2237\theta=0.2237 and ρ=2.0644\rho=2.0644

![Refer to caption](x16.png)


(b) ES:θ=0.0758\theta=0.0758 and ρ=1.7341\rho=1.7341

![Refer to caption](x17.png)


(c) ES: θ=0.0190\theta=0.0190 and ρ=1.5016\rho=1.5016

![Refer to caption](x18.png)


(d) ES: θ=0.2761\theta=0.2761 and ρ=1.7078\rho=1.7078

![Refer to caption](x19.png)


(e) ES: θ=0.1022\theta=0.1022 and ρ=1.5641\rho=1.5641

![Refer to caption](x20.png)


(f) ES: θ=0.0258\theta=0.0258 and ρ=1.4565\rho=1.4565

Figure 8: Equilibrium solutions under the farmer’s risk distortion function gf​(s)=λ​s+(1−λ)​min⁡{s1−α,1},α=0.8g\_{f}(s)=\lambda s+(1-\lambda)\min\left\{\frac{s}{1-\alpha},1\right\},\alpha=0.8 with different values of λ\lambda and insurer’s profit maximization using two parameters. Figure (a), (b) and (c) show the index insurance payoff functions for λ=0.1,0.5​and​0.7\lambda=0.1,0.5~\text{and}~0.7 respectively in farmer’s risk distortion function. Figures (d), (e) and (f) show the indemnity insurance payoff functions for λ=0.1,0.5​and​0.7\lambda=0.1,0.5~\text{and}~0.7 respectively in farmer’s risk distortion function.

### 5.3 Problem 3 (𝒫s\mathcal{P}\_{s}): General Premium Model

This subsection presents the solutions to Problem 3. In this case, we do not impose any structural form of the premium function and instead, we search for the optimal pricing function gi​(s)g\_{i}(s) for the premium Π^​(I​(𝐗))=∫0∞gi​(ℙ​(I​(𝐗)>z))​𝑑z\hat{\Pi}(I(\mathbf{X}))=\int\_{0}^{\infty}g\_{i}(\mathbb{P}(I(\mathbf{X})>z))dz.

![Refer to caption](x21.png)


(a)

![Refer to caption](x22.png)


(b)

![Refer to caption](x23.png)


(c)

![Refer to caption](x24.png)


(d)

Figure 9: Equilibrium solution under Insurer’s General Pricing Strategy. Figure (a) shows the optimal insurance payoff function when the insurer adopts a general pricing strategy through a premium distortion function gi​(s)g\_{i}(s). The farmer’s risk distortion function adopted here is gf​(s)=0.5​s+0.5​min⁡{s1−α,1}​with​α=0.8g\_{f}(s)=0.5s+0.5\min\left\{\frac{s}{1-\alpha},1\right\}~\text{with}~\alpha=0.8. Figure (b) shows the corresponding optimal pricing function gig\_{i} of the insurer. Figures (c) and (d) show the optimal insurance payoff functions and pricing function obtained for indemnity insurance.

Figure [9](https://arxiv.org/html/2512.01623v1#S5.F9 "Figure 9 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the insurance payoff function and the pricing function gi​(s)g\_{i}(s) obtained in equilibrium. For this case, we search for the optimal pricing function by using the optimal insurance payoff function obtained via CNNs in Section [5.1.3](https://arxiv.org/html/2512.01623v1#S5.SS1.SSS3 "5.1.3 Convolutional Neural Networks (CNNs) ‣ 5.1 Problem 1 (𝒫_{𝑠⁢1}): One-parameter Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") as the initial values. The pricing function is modeled using NNs and the network architecture is selected from Table [8](https://arxiv.org/html/2512.01623v1#S5.T8 "Table 8 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance").

Table 8: Model validation for the general pricing function (Problem 3).

| Single hidden layer | [8] | | [16] | | [32] | | [64] | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Train | Validation | Train | Validation | Train | Validation | Train | Validation |
| UP Loss | -7.4560 | -7.6460 | -4.2022 | -4.1166 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Penalized Loss | -4.3509 | -59.5728 | -2.7396 | -3.1015 | 0.000 | 0.0000 | 0.0000 | 0.0000 |
| Multiple hidden layers | [16 - 16] | | [16 - 16 - 16] | | [16 - 16 - 16 - 16] | | [16 - 16 - 16 - 16 - 16] | |
| Train | Validation | Train | Validation | Train | Validation | Train | Validation |
| UP Loss | -9.2257 | -9.4739 | -9.3566 | -9.5601 | -8.7961 | -8.9043 | -9.0715 | -9.2617 |
| Penalized Loss | -9.1168 | -14.3956 | -9.1887 | -27.2854 | -8.6862 | -6.9138 | -8.9940 | -40.7818 |

Note: The optimal model is the one with the lowest validation UP loss given that the absolute difference between validation UP loss and validation penalized loss is below 2.

Figure [9(a)](https://arxiv.org/html/2512.01623v1#S5.F9.sf1 "In Figure 9 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the optimal index insurance payoff function, and Figure [9(b)](https://arxiv.org/html/2512.01623v1#S5.F9.sf2 "In Figure 9 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") shows the corresponding optimal pricing function. In both figures, the farmer’s risk measure is CVaR. The profit obtained is 8.7961, which is higher than the profits obtained in Problems 1 and 2 under the same risk measure for the farmer (CVaR). The monopolistic insurer has much more freedom in this case and is thus capable of extracting more profit. The optimal solutions under the same farmer’s risk measure for indemnity-based insurance are shown in Figures [9(c)](https://arxiv.org/html/2512.01623v1#S5.F9.sf3 "In Figure 9 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") and [9(d)](https://arxiv.org/html/2512.01623v1#S5.F9.sf4 "In Figure 9 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance"). The optimal insurance payoff function shown in Figure [9(c)](https://arxiv.org/html/2512.01623v1#S5.F9.sf3 "In Figure 9 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") has a deductible close to zero. The optimal pricing kernel shown in Figure [9(d)](https://arxiv.org/html/2512.01623v1#S5.F9.sf4 "In Figure 9 ‣ 5.3 Problem 3 (𝒫_𝑠): General Premium Model ‣ 5 Numerical Results ‣ Monopoly Pricing of Weather Index Insurance") is piecewise linear with a kink at s=0.2s=0.2. The profit obtained in the optimal solution for the indemnity-based insurance is 17.2982. It is interesting to note that the shape of the optimal pricing kernel for the indemnity-based insurance is piecewise linear, while that for the index insurance is smooth and concave. We can verify the results for indemnity-based insurance in this subsection using the techniques in cheung2019risk.

## 6 Conclusion

This study provides a comprehensive analysis of monopoly pricing in weather-index-based insurance. We formulate the pricing problem as a sequential game between a profit-maximizing insurer and a risk-averse farmer and solve it using a penalized bilevel programming algorithm. Moreover, NNs and CNNs are employed to determine the optimal insurance strategy, and it is found that stop-loss insurance emerges as the preferred contract structure, particularly under risk measures such as CVaR. We contribute to the literature by introducing CNNs into index insurance pricing, yielding more robust insurance payoff functions than fully connected NNs. This implies that CNNs can reduce the basis risk in index insurance pricing, enabling the insurer to achieve profits closer to those of an indemnity insurance contract.

Our analysis further reveals the critical role of the farmer’s risk appetite in shaping the market equilibrium. While more risk-averse farmers demand lower deductibles, the monopolistic insurer strategically responds with more aggressive pricing. We show this by comparing equilibrium solutions across three cases with varying degrees of pricing flexibility. When the insurer can optimize either a two-parameter premium (a risk-loading factor θ\theta and a premium distortion parameter ρ\rho) or a general pricing function, it can extract significantly higher profits from more risk-averse farmers.

This paper introduces a deep bilevel programming framework for pricing weather index insurance. It highlights how advanced machine learning and game theory can be applied to effectively analyze the strategic behavior in agricultural markets. Future research could extend this framework to examine how the different market structures, such as duopoly or perfect competition, shape the contract design and farmers’ welfare. Such extensions would provide policymakers and industry stakeholders with important information to manage agricultural risk efficiently.