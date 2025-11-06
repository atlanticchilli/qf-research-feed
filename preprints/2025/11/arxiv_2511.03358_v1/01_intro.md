---
authors:
- Alexander Alecio
doc_id: arxiv:2511.03358v1
family_id: arxiv:2511.03358
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain
  robustness
url_abs: http://arxiv.org/abs/2511.03358v1
url_html: https://arxiv.org/html/2511.03358v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alexander Alecio

(Date: November 5, 2025)

###### Abstract.

We consider a model for systemic risk comprising of a system of diffusion processes, interacting through their empirical mean. Each process is subject to a confining double-well potential with some uncertainty in the coefficients, corresponding to fluctuations in height of the potential barrier seperating the two wells. This is equivalent to studying a single McKean-Vlasov SDE with explicit dependence on its moments and, novelly, independently varying additive and multiplicative noise. Such non-linear SDEs are known to possess two phases: stable (ordered) and unstable (disordered). When the potential is purely bistable, the phase changes from stable to unstable when noise intensity is increased past a critical threshold.

With the recent advances in [alecio], it will be shown that the behaviour here is far richer: indeed, depending on the interpretation of the stochastic integral, the system exhibits phase changes that cannot occur in any regime where there is no uncertainty in the potential. Strikingly, this allows for the phenomenon of noise induced stability; situations where more noise can reduce the risk of system failure.

###### Key words and phrases:

Systemic risk, Interacting Particle System, McKean-Vlasov diffusions, phase transitions

###### 2000 Mathematics Subject Classification:

60H30, 60J60, 82C26, 91B26, 91B70

Consider an evolving system of interconnected components that can transition between two states, functioning or failed. If a sufficient number of individual components were to be in the failed state concurrently, the whole system fails; termed ‘systemic failure’. Each component has an intrinsic stability, a quantification of its robustness, that competes with a random perturbation that destabilises their state. Interconnectedness (or cooperation) between components, the degree of which can be varied, works to stabilise individual components, assuming a sufficient number of the rest are in a functioning state. The expected trade-off of increasing interconnectedness is an increase in ‘systemic risk’, the probability of systemic failure; see [ssra] for an overview of systemic risk analytics.

Systemic risk is an important consideration in many fields. The archetypal example from engineering would be a system of interacting components that can cooperate by sharing load, but will sytemically fail if a sufficient number of its constituent components themselves are in the failed state. One tangible realisation are power grids, [pgs]: individual substations may pass demand onto other stations to avoid individual failure, at the risk of total grid failure. Another are banks, which cooperate by lending to one another to prevent default. This linkage is a potential ‘contagion channel’ [lds] as creditor banks are left in a vulnerable position if exposed enough to a defaulting bank. This in turn may lead to further defaults, known as ‘financial contagion’ and documented to have occured in many financial crises [fca, boe, spil].

## 1. Mean-Field Modeling of Systemic Risk

To capture this, a system of nn weakly interacting diffusions was introduced in [ss], where the equation for the risk state (or variable) of component ii is

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | d​Xtn,i=(−V′​(Xtn,i)−θ​(Xtn,i−1n​∑jXtn,j))​d​t+σ​d​BtidX\_{t}^{n,i}=(-V^{{}^{\prime}}(X\_{t}^{n,i})-\theta(X\_{t}^{n,i}-\frac{1}{n}\sum\nolimits\_{j}X\_{t}^{n,j}))dt+\sigma dB\_{t}^{i} |  |

Each component can either be in a functioning or failed state, corresponding to whether its risk state is positive or negative.
Accordingly, the potential VV is taken to be symmetric and with minima at ±1\pm 1, with the two potential wells seperated by a local maxima at 0. With external perturbation, whose strength is controlled by noise intensity parameter σ\sigma, these minima are metastable: the risk states tend to remain in a potential well, but with a non-zero probability of exit in a finite time. The intrinsic stability, resistance of the components to changing risk state, is encoded in the potential VV. Cooperation, the degree of which is controlled by θ>0\theta>0, is expressed through a simple mean reversion mechanism. Systemic failure occurs when a majority of components are themselves in the failed state. Commensurately, as noted in [ss], the natural choice of measure of systemic risk is the mean of the risk states, x¯=1n​∑jXn,j\bar{x}=\frac{1}{n}\sum\_{j}X^{n,j}.

Calculating probabilties of events of x¯\bar{x} is complicated by no closed form forward equation for x¯\bar{x} existing outside of linear or convex potentials. However, it is known, under certain technical conditions, for instance [leo, ohl], that the empirical measure of nn-SDE system ([1](https://arxiv.org/html/2511.03358v1#S1.E1 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) converges on any finite time interval to the solution of the non-linear Fokker Planck equation

|  |  |  |
| --- | --- | --- |
|  | ∂∂t​ρ=∂∂x​((−V′​(x)−θ​(m1−x))​ρ+σ22​∂ρ∂x)\frac{\partial}{\partial t}\rho=\frac{\partial}{\partial x}\Big((-V^{{}^{\prime}}(x)-\theta(m\_{1}-x))\rho+\frac{\sigma^{2}}{2}\frac{\partial\rho}{\partial x}\Big) |  |

which is the concomitant forward equation of the McKean-Vlasov process

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | d​Xt=(−V′​(Xt)−θ​(Xt−m1))​d​t+σ​d​WtdX\_{t}=(-V^{{}^{\prime}}(X\_{t})-\theta(X\_{t}-m\_{1}))dt+\sigma dW\_{t} |  |

where m1=∫x​ρ​𝑑xm\_{1}=\int x\rho dx, to which x¯​(t)\bar{x}(t) converges. This is an example of the ‘propagation of chaos’, [Chaintron\_2022, sznit], effectively generalising the problem into a larger space.

Behaviour stemming from the explicit dependence on moments in the drift in MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) has received much sustained attention, particularly when VV is taken as the simple bistable potential, V=x44−x22V=\frac{x^{4}}{4}-\frac{x^{2}}{2} (the Dawson-Shiino model for seminal papers [dawson, shiino]). This includes convergence in different metrics, Central Limit theorem-type result for the fluctuations of x¯\bar{x} around ∫x​ρ​𝑑x\int x\rho dx, large deviations and (possible) phase transitions and their location, much of which has been extended to arbitrary potentials.

Idealised macroscopic systems forced from thermodynamic equilibrium eventually undergo a continuous symmetry-breaking instability. Like these instabilities, it has been shown by many authors, [alecio, dawson, shiino, tug], that MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) at stationarity demonstrates almost identical phenomenology to a second order phase transition: once the noise intensity σ\sigma is pushed beyond a certain critical threshold, σc\sigma\_{c}, the stable (ordered) phase gives way to the unstable (disordered) phase. The stable phase is characterised by three stationary measures (corresponding to the three extrema of VV), as opposed to the unstable where only one exists. Casting σ\sigma as the control parameter, admissible stationary solutions have the characteristic property 𝔼​(X∞)\mathbb{E}(X\_{\infty}) (the mean of process XtX\_{t} at stationarity) which plays the rôle of order parameter. Plotting these quantities reveals a pitchfork bifurcation.

![Refer to caption](figs/2bif.png)


Figure 1. Bifurcation diagrams of (left) the Dawson-Shiino model with a classic pitchfork shape, and (right) the model with uncertain robustness (parameters as inscribed), introduced in section [2](https://arxiv.org/html/2511.03358v1#S2 "2. The Mean-Field Model with Uncertain Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")

As to potential and drift choice, it was recently shown in [alecio] that MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) has identical phase structure for a broad class symmetric bistable potentials, increasing drift and reversion-type cooperation.

Heuristically, the mechanism of this change is simple. In the stable phase the cooperative terms dominate, and probability mass is concentrated, settling in a single potential well. As noise intensity is increased, the mass outside the well increases relatively and the mean approaches 0. At this point, the potential barrier is overwhelmed and the other well is equally filled, and these solution fold into the symmetric stationary measure at σc\sigma\_{c}. (While the symmetric stationary measure exists in the stable phase of MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")), its basin of attraction comprises only symmetric initial conditions [alecio2], so can be ignored). The potential well in which the empirical mean x¯\bar{x} is located is identified as the system state.

On the other hand, nn-SDE system ([1](https://arxiv.org/html/2511.03358v1#S1.E1 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) has a unique stationary measure irrespective of parameters. While x¯​(t)\bar{x}(t) will remain close to ∫x​ρ​𝑑x\int x\rho dx by the convergence result, in the stable phase there is a non-zero probability of a system state transition: x¯​(t)\bar{x}(t) transitioning to the other state in finite time, which decreases as n→∞n\rightarrow\infty. Extensive numerical testing in [ss, gomes] has validated this, with x¯​(t)\bar{x}(t) remaining in one state for increasing duration as nn increases over a fixed time period. In the unstable phase, transitions between the symmetric wells/states become so common, the mean is 0.

For transitions between states to be meaningful then, σ\sigma must be fixed in order for the system to be in the stable state, as reasoned in [ss]. [ss] proceeds to study systems with component dependent cooperation intensities and the probability of system state transition, or systemic risk, using large deviation results of [dawgart] along with various linearisations. They were able to show increased cooperation can lower the risk of an individual component failing, but with the risk of systemic failure, in accord with empirical observation, providing further corroboration this choice of this model and cooperation mechanism.

## 2. The Mean-Field Model with Uncertain Stability

In this work, we consider a simple, though ultimately non-trivial, modification to the intrinsic stability. As a starting point, consider VV taken from parametric family of symmetric bistable potentials x44−a​x22\frac{x^{4}}{4}-a\frac{x^{2}}{2}, a>0a>0. As aa increases, so does the height of the potential barrier between states.

In [ss], the system’s stability is intuitively identified to be the resistance of x¯​(t)\bar{x}(t) to changing state. This is
dependent on the stability of individual components at the microscopic level, equivalently their resistance to the stochastic perturbation changing their state, which is itself a function of aggregating factors such as the size of the potential barrier between risk states, aa and strength of cooperative terms, θ\theta, see for instance [gardiner, hangi, PGDiff]

Lifting these ideas to the macroscopic level, MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) is stable if it is in the stable phase, and so ∫x​ρ≠0\int x\rho\neq 0 and distinct system states exist. The system becomes more stable with respect to a change in parameter if the size of its stable phase (range of noise strength σ\sigma such that MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) is in the stable phase) increases. This definition is first proposed in [ss, p.157]. That this definition is in accord with the microscopic was shown in [alecio], which demonstrated that the system becomes more stable as the aggregating factor of cooperation strength θ\theta increases. The same result will be presented here for aa.

Suppose now there is some uncertainty in the height of the potential barrier between the risk states, by replacing aa with a stochastic process driven by an independent Wiener process for each component: a→a+σm​d​Bt(2,i)a\rightarrow a+\sigma\_{m}dB^{(2,i)}\_{t}. This could represent an incomplete state of knowledge of the implicit stability of individual agents, but can also be physically motivated. Returning to our original examples, the robustness of industrial components can be undermined by thermal fluctuations, which can be represented stochastically. Banks remain solvent when their liabilities are outweighed by their assets. These assets will be invested and their value dependent on market forces; downward movements can leave banks vulnerable to failure; asset price contagion [bsc2, bsc]. In this case, the risk state is a measure of their liabilities and aa the initial value of their assets, with the diversity of fluctuations reflecting the differing assets each bank holds.

Replacing σ\sigma with σa\sigma\_{a}, and substituting for aa in ([1](https://arxiv.org/html/2511.03358v1#S1.E1 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")), the associated MV-SDE is

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | d​Xt=(a​Xt−Xt3−θ​(Xt−m1))​d​t+σa​d​Bt(1)+σm​Xt∘νd​Bt(2)dX\_{t}=\big(aX\_{t}-X\_{t}^{3}-\theta(X\_{t}-m\_{1})\big)dt+\sigma\_{a}dB\_{t}^{(1)}+\sigma\_{m}X\_{t}\circ\_{\nu}dB\_{t}^{(2)} |  |

The stochastic integral of the second Wiener process is open to multiple interpretations. This is denoted by ∘ν\circ\_{\nu} with ν∈[0,1]\nu\in[0,1], determining where the value of the integrand is sampled in the limiting Riemann sums. It is well known that the lack of regularity of the Wiener process leads to entirely different values of the integral, for non-trivial integrand. The most commonly used stochastic integrals - Klimontovich, Stratonovich and Itô - correspond to ν={0,12,1}\nu=\{0,\frac{1}{2},1\}. (The Itô integral will also be denoted by omitting the ∘\circ) Realisations of these stochastic integrals are known to occur in nature, [PesceGiuseppe2013Stin]. Aside from empirical observation, factors influencing choice of ν\nu are considered in Section [4](https://arxiv.org/html/2511.03358v1#S4 "4. Noise Induced Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness").

In this work it will be shown that, while the straightforward competition of total noise to aggregating factors remains, increasing the total noise by increasing the multiplicative noise, representing increased uncertainity in components robustness, has a far more varied effect. It can destabilise the system, as might be expected, but can be a neutral factor or even influence an unstable system back into stability, so-called noise induced stability.

## 3. Mathematical Formulation

MV-SDE ([3](https://arxiv.org/html/2511.03358v1#S2.E3 "In 2. The Mean-Field Model with Uncertain Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) is equivalent in law to

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | d​Xt=(a​Xt−Xt3+Xt−θ​(Xt−m1))​d​t+σa2+σm2​Xt2∘νd​WtdX\_{t}=\big(aX\_{t}-X\_{t}^{3}+X\_{t}-\theta(X\_{t}-m\_{1})\big)dt+\sqrt{\sigma\_{a}^{2}+\sigma\_{m}^{2}X^{2}\_{t}}\circ\_{\nu}dW\_{t} |  |

In terms of the Itô stochastic integral, MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) is

|  |  |  |
| --- | --- | --- |
|  | d​Xt=(a​Xt−Xt3+(1−ν)​σm2​Xt−θ​(Xt−m1))​d​t+σa2+σm2​Xt2​d​WtdX\_{t}=\big(aX\_{t}-X\_{t}^{3}+(1-\nu)\sigma\_{m}^{2}X\_{t}-\theta(X\_{t}-m\_{1})\big)dt+\sqrt{\sigma\_{a}^{2}+\sigma\_{m}^{2}X^{2}\_{t}}dW\_{t} |  |

As phase transitions and stability are entirely discernible from the law of the process, MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) is the fundamental object of study in this work.

The concomitant Fokker-Planck equation is

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | ∂∂t​ρ=∂∂x​((−x+x3−(1−ν)​σm2​x−θ​(m1−x))​ρ+12​(σm2​x2+σa2)​∂ρ∂x)\frac{\partial}{\partial t}\rho=\frac{\partial}{\partial x}\Big((-x+x^{3}-(1-\nu)\sigma\_{m}^{2}x-\theta(m\_{1}-x))\rho+\frac{1}{2}(\sigma\_{m}^{2}x^{2}+\sigma\_{a}^{2})\frac{\partial\rho}{\partial x}\Big) |  |

This specific model was first introduced in [Multinoise], with ν=12\nu=\frac{1}{2}, and has been the subject of recent interest in [agp].

Directly integrating ([5](https://arxiv.org/html/2511.03358v1#S3.E5 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")), the general form of the stationary measure is

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | ρ0=exp⁡(a−θ−ν​σm2+σa2σm2σm2​log⁡(1+σm2σa2​x2)+2​θ​μσa​σm​arctan⁡σm​xσa−x2σm2)\rho\_{0}=\exp\big(\frac{a-\theta-\nu\sigma\_{m}^{2}+\frac{\sigma\_{a}^{2}}{\sigma\_{m}^{2}}}{\sigma\_{m}^{2}}\log(1+\frac{\sigma\_{m}^{2}}{\sigma\_{a}^{2}}x^{2})+\frac{2\theta\mu}{\sigma\_{a}\sigma\_{m}}\arctan{\frac{\sigma\_{m}x}{\sigma\_{a}}}-\frac{x^{2}}{\sigma\_{m}^{2}}\big) |  |

where m1=∫x​ρ​[m1]​𝑑xm\_{1}=\int x\rho[m\_{1}]dx. These correspond to the roots of the self-consistency function

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | F​(ν,σa,σm,a,θ)​[μ]=∫(x−μ)​ρ0​(ν,σa,σm,a,θ)​[μ]​𝑑xF(\nu,\sigma\_{a},\sigma\_{m},a,\theta)[\mu]=\int(x-\mu)\rho\_{0}(\nu,\sigma\_{a},\sigma\_{m},a,\theta)[\mu]dx |  |

which is a more appealing form for technical reasons [alecio]. The roots of F​[μ]F[\mu] are not necessarily unique, translating to multiple admissible stationary measures.

![Refer to caption](figs/bfpanoply.png)


Figure 2. Panel of bifurcation diagrams, parameters inscribed. Left to right, top to bottom: 1→3→11\rightarrow 3\rightarrow 1, 1→1\rightarrow, 1→31\rightarrow 3 and 3→13\rightarrow 1 for (ν,σa)(\nu,\,\sigma\_{a}) as inscribed

The following results, adapted from [alecio], expatiate the relationship between phase and self-consistency function FF of MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")), sketching FF on rays in (σa,σm)(\sigma\_{a},\sigma\_{m})-space, where the multiplicative and additive noise increase in intensity in fixed ratio σm=k​σa\sigma\_{m}=k\sigma\_{a}, with varying aa and θ\theta. The interested reader can investigate their technical underpinning and precise conditions in [alecio], with any pertinent additional information relegated to Appendix [B](https://arxiv.org/html/2511.03358v1#A2 "Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness").

For MV-SDEs with elliptic drifts of the form σ​k​(Xt)​d​Wt\sigma k(X\_{t})dW\_{t} it was shown in [alecio] there can only be 1 or 3 stationary measures, demarcating the stable and unstable phase. Its direct analogue can be concluded for MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) including, crucially, that the stability of MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) directly corresponds to the sign of Fμ′​(ν,σa,σm,a,θ)​[0]F^{{}^{\prime}}\_{\mu}(\nu,\sigma\_{a},\sigma\_{m},a,\theta)[0].

###### Proposition 1 ([alecio] Proposition 3.3).

MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) has two phases, stable and unstable, characterised by possessing 3 (respectively 1) stationary measures. It is in the stable phase iff Fμ′​[0]>0F^{{}^{\prime}}\_{\mu}[0]>0

The next shows the aggregating factors work, as for MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")), to make MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) more stable:

###### Proposition 2 ([alecio]).

If σm=k​σa\sigma\_{m}=k\sigma\_{a}, MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) is more stable as aa or θ\theta increases.

###### Proof.

Appendix [B](https://arxiv.org/html/2511.03358v1#A2 "Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")
∎

The last concerns the phase structure, with the Itô integral. The rigidity of the phase structure, stable to unstable (or 3→13\rightarrow 1 in shorthand), is a characteristic feature of MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) with symmetric potential and diffusion.

###### Proposition 3 ([alecio] Proposition 3.5).

If σm=k​σa\sigma\_{m}=k\sigma\_{a} and ν=1\nu=1, MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) will transition from the stable to unstable phase (3→1)(3\rightarrow 1) as σa\sigma\_{a} increases.

![Refer to caption](figs/bfpanoply1.png)


Figure 3. Bifurcation Diagrams for a≤0a\leq 0. Top At a=0a=0 a stable phase exists so long as ν=1\nu=1. Bottom Stable phase, and lack thereof, above and below the threshold. Note 10≊3.16\sqrt{10}\approxeq 3.16

It is both the noise interpretation and uncertainty in components’ robustness (equivalently, the ability to vary both multiplicative and additive noise out of ratio) that diversifies this phase structure, underpinning the results of this work. As an example, for some range of ν\nu, multiplicative noise can make the system more stable, as the next section will show.

## 4. Noise Induced Stability

This section will the effect of multiplicative noise on phase structure of MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")). Particularly, it will be shown that, depending on ν\nu, increased multiplicative noise can actually transition the system to the stable phase and its presence can even permit the existence of a stable phase where none can exist without.

A clear example of the latter, and one the results of [alecio] are particularly well disposed to study, is when θ\theta is varied for fixed (σa,σm)(\sigma\_{a},\sigma\_{m}).
If the potential is bistable, the phase structure is not altered by multiplicative noise: by Proposition [2](https://arxiv.org/html/2511.03358v1#Thmproposition2 "Proposition 2 ([alecio]). ‣ 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness"), MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) will be stable for sufficiently large θ\theta, regardless of (σa,σm)(\sigma\_{a},\sigma\_{m}).
Contrastingly, if the potential were convex, and ν=1\nu=1, there is only one phase. It will be demonstrated that multiplicative noise can induce a stable phase, which could not otherwise exist.

Concretely, consider MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) again with the potential V′=x3−a​xV^{{}^{\prime}}=x^{3}-ax, where now a∈ℝa\in\mathbb{R}. If a>0a>0, the potential is bistable and Proposition [2](https://arxiv.org/html/2511.03358v1#Thmproposition2 "Proposition 2 ([alecio]). ‣ 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness") applies. When a≤0a\leq 0, the three extrema merge, forming one minima at 0.
It is known that the number of stationary measures is dependent on the number of extrema. Indeed, it is straightforward to retool the results of the second section of [alecio] to achieve

###### Theorem 1 ([alecio] Theorem 2.12).

Suppose ν=1\nu=1, and V′V^{{}^{\prime}} has NN roots, all simple. Then there exists θc\theta\_{c} such that for θ>θc\theta>\theta\_{c} MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) has NN stationary measures.

In fact, for any convex potential in the presence of additive noise (or for a more general diffusion with the Itô integral) there is a unique stationary measure and consequently one phase, see also [malrieu].

With multiplicative noise and non-Itô integral (ν≠1\nu\neq 1), V′V^{{}^{\prime}} is augmented by the integral correction term (1−ν)​σm2​x(1-\nu)\sigma\_{m}^{2}x, with extensive ramifications. As before, for sufficiently small θ\theta and large σa\sigma\_{a}, it can be shown the stationary measure is unique. However, applying Theorem [1](https://arxiv.org/html/2511.03358v1#Thmtheorem1 "Theorem 1 ([alecio] Theorem 2.12). ‣ 4. Noise Induced Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness") to V′=x3−a​x−(1−ν)​σm2​xV^{{}^{\prime}}=x^{3}-ax-(1-\nu)\sigma\_{m}^{2}x at a=0a=0, any level of multiplicative noise allows for stable phase with a phase change (unstable to stable) as θ\theta is increased. Similarly for a<0a<0 the same result holds so long as (1−ν)​σm2>−a(1-\nu)\sigma\_{m}^{2}>-a.

It is tempting, then, to conclude that multiplicative noise is always a stabilising influence, given that it deepens the potential wells. In fact, multiplicative noise also increases the weight of the tails of the stationary measure(s), which is destabilising. It is the competition between these two elements that will be the subject of the sequel, by study of Fμ′​[0]F^{{}^{\prime}}\_{\mu}[0]. As Proposition [2](https://arxiv.org/html/2511.03358v1#Thmproposition2 "Proposition 2 ([alecio]). ‣ 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness") establishes their effect, unless otherwise stated, aa and θ\theta are set to unity in the following. σc\sigma\_{c} denotes the critical temperature of the Dawson-Shiino model, MV-SDE ([2](https://arxiv.org/html/2511.03358v1#S1.E2 "In 1. Mean-Field Modeling of Systemic Risk ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) with the simple bistable potential.

| Phase Portrait Summary | | | | |
| --- | --- | --- | --- | --- |
| ν\nu | ν>ν1\nu>\nu\_{1} | ν1>ν>ν2\nu\_{1}>\nu>\nu\_{2} | ν2>ν>ν3\nu\_{2}>\nu>\nu\_{3} | ν3>ν>0\nu\_{3}>\nu>0 |
| σa\sigma\_{a} | 3→13\rightarrow 1 | 3→3\rightarrow | 3→3\rightarrow | 3→3\rightarrow |
| increasing | 1→1\rightarrow | 3→13\rightarrow 1 | 1→31\rightarrow 3 | 1→31\rightarrow 3 |
| ↓\downarrow |  | 1→3→11\rightarrow 3\rightarrow 1 | 1→3→11\rightarrow 3\rightarrow 1 | 1→1\rightarrow |
|  |  | 1→1\rightarrow | 1→1\rightarrow |  |
|  | σm\sigma\_{m} increasing →\rightarrow | | | |

Table 1: Phase Transition Summary. Correspondence to figure [5](https://arxiv.org/html/2511.03358v1#S6.F5 "Figure 5 ‣ 6. Acknowelgement ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness") described below the figure

In Figure [5](https://arxiv.org/html/2511.03358v1#S6.F5 "Figure 5 ‣ 6. Acknowelgement ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness"), a panel of contour graphs of Fμ′​[0]F\_{\mu}^{{}^{\prime}}[0], is presented, with the phase transition contour Fμ′=0F^{{}^{\prime}}\_{\mu}=0, for a representative range of ν\nu. The phase changes for increasing σm\sigma\_{m}, are presented in Table 1.

From Proposition [3](https://arxiv.org/html/2511.03358v1#Thmproposition3 "Proposition 3 ([alecio] Proposition 3.5). ‣ 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness"), with Itô noise the set {(σa,σm):Fμ′​[0]>0}\{(\sigma\_{a},\sigma\_{m}):F^{{}^{\prime}}\_{\mu}[0]>0\} is star shaped about the origin. Broadly, as ν\nu decreases, phase transition contour, parameterised by σm\sigma\_{m}, moves away from the origin. The critical change is that below ν1\nu\_{1}, the shape begins to change, from decreasing to increasing before decreasing, as σm\sigma\_{m} increases. Below ν3\nu\_{3}, it is increasing.

###### Proposition 4 (Asymptotic Properties of Fμ′​(ν,σa,σm)​[μ]F^{{}^{\prime}}\_{\mu}(\nu,\sigma\_{a},\sigma\_{m}){[}\mu{]}: σm↓0\sigma\_{m}\downarrow 0 ).

Let GG be the self-consistency function and mim\_{i} the ithi^{\mathrm{th}} moment of the Dawson-Shiino model.

1. (1)

   limσm↓0Fμ′​(ν,σa,σm)​[0]=G′​(σa)​[0]\lim\limits\_{\sigma\_{m}\downarrow 0}F^{{}^{\prime}}\_{\mu}(\nu,\sigma\_{a},\sigma\_{m})[0]=G^{{}^{\prime}}(\sigma\_{a})[0]
2. (2)

   limσm↓0∂Fμ′∂σm2​(ν,σa,σm)=m8−m103​σa4+m6−m43​σa2−(1−θ)​m6−m8σa4+m2−ν​(m4−m6σa2+m2)\lim\limits\_{\sigma\_{m}\downarrow 0}\frac{\partial F^{{}^{\prime}}\_{\mu}}{\partial\sigma^{2}\_{m}}(\nu,\sigma\_{a},\sigma\_{m})=\frac{m\_{8}-m\_{10}}{3\sigma\_{a}^{4}}+\frac{m\_{6}-m\_{4}}{3\sigma\_{a}^{2}}-(1-\theta)\frac{m\_{6}-m\_{8}}{\sigma\_{a}^{4}}+m\_{2}-\nu(\frac{m\_{4}-m\_{6}}{\sigma\_{a}^{2}}+m\_{2})

###### Proof.

Appendix [B](https://arxiv.org/html/2511.03358v1#A2 "Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")
∎

By the first point of the above proposition, the phase transition contour must emanate from (σa,0)(\sigma\_{a},0). Further, knowing that ∂G′∂σa​(σc)<0\frac{\partial G^{{}^{\prime}}}{\partial\sigma\_{a}}(\sigma\_{c})<0 by Proposition 3.5 of [alecio], the sign of the gradient of the phase transition contour is equal to that of limσm↓0∂Fμ′∂σm2​(ν,σc,σm)\lim\limits\_{\sigma\_{m}\downarrow 0}\frac{\partial F^{{}^{\prime}}\_{\mu}}{\partial\sigma^{2}\_{m}}(\nu,\sigma\_{c},\sigma\_{m}) by the chain rule. This was determined as a function of the first 5 even moments of the stationary distribution of the Dawson-Shiino model in the second point of Proposition [4](https://arxiv.org/html/2511.03358v1#Thmproposition4 "Proposition 4 (Asymptotic Properties of 𝐹^'_𝜇⁢(𝜈,𝜎_𝑎,𝜎_𝑚)⁢[𝜇]: 𝜎_𝑚↓0 ). ‣ 4. Noise Induced Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness"). In Appendix [B](https://arxiv.org/html/2511.03358v1#A2 "Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness"), this was simplified to 12​(12−ν)​(1−m2)\frac{1}{2}(\frac{1}{2}-\nu)(1-m\_{2}), a decreasing function in ν\nu that becomes positive at ν=0.5\nu=0.5. See Figure [4](https://arxiv.org/html/2511.03358v1#S4.F4 "Figure 4 ‣ 4. Noise Induced Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness") for this sign change’s dependence on θ\theta.

![Refer to caption](figs/figcor2.png)


Figure 4. Left Gradient of the phase transition contour at (σc,0)(\sigma\_{c},0) against θ\theta for Itô, Stratonovich and Klimontovich noise. The roots at θ=1\theta=1 for ν=0.5\nu=0.5 has been recovered and those for ν=0\nu=0 and ν=1\nu=1 displayed. For θ\theta above ∼0.72\sim 0.72 for some range of ν\nu, noise induced stabilisation can be observed. It always occurs (regardless of ν\nu) for θ≳2.1\theta\gtrsim 2.1. Right the self-consistency function for MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) displaying a 1→3→11\rightarrow 3\rightarrow 1 phase change.

In the case that at the critical temperature, there is sufficient scale separation that the coefficient process a+σm​d​Wt2a+\sigma\_{m}dW\_{t}^{2} can be averaged out, the phase transition contour would be perpendicular to the σa\sigma\_{a} axis, suggesting the choice of Stratonovich noise, ν=0.5\nu=0.5 for very small σm\sigma\_{m}.

Consequently, for ν>0.5\nu>0.5 and σa\sigma\_{a} sufficiently close to σc\sigma\_{c}, the system will transition from unstable to unstable, (1→3)(1\rightarrow 3), and noise induced stabilisation occurs. Whether it returns to instability depends on the properties of Fμ′​[0]F^{{}^{\prime}}\_{\mu}[0] as σm\sigma\_{m} is increased. It can be expected that the limit limσm↑∞Fμ′​[0]\lim\limits\_{\sigma\_{m}\uparrow\infty}F^{{}^{\prime}}\_{\mu}[0] is dependent on ν\nu.
Indeed, the multiplicand (1+x2)−ν(1+x^{2})^{-\nu} in ρ0\rho\_{0} dominates in the limit, by decreasing the relative weight of the tails with ν\nu.

###### Proposition 5 (Further Asymptotic Properties of Fμ′​(ν,σa,σm)​[μ]F^{{}^{\prime}}\_{\mu}(\nu,\sigma\_{a},\sigma\_{m}){[}\mu{]}: σm↑∞\sigma\_{m}\uparrow\infty ).

If ν>0.5\nu>0.5, limσm→∞Fμ′​(ν,σa,σm)<0\lim\limits\_{\sigma\_{m}\rightarrow\infty}F^{{}^{\prime}}\_{\mu}(\nu,\sigma\_{a},\sigma\_{m})<0.
  
Else if ν≤0.5\nu\leq 0.5, ∃σcν\exists\,\sigma\_{c}^{\nu} s.t for σa>σcν,\sigma\_{a}>\sigma\_{c}^{\nu}, limσm→∞Fμ′​(ν,σa,σm)<0\lim\limits\_{\sigma\_{m}\rightarrow\infty}F^{{}^{\prime}}\_{\mu}(\nu,\sigma\_{a},\sigma\_{m})<0
  
and for σa<σcν,\sigma\_{a}<\sigma\_{c}^{\nu}, limσm↑∞Fμ′​(ν,σa,σm)>0\lim\limits\_{\sigma\_{m}\uparrow\infty}F^{{}^{\prime}}\_{\mu}(\nu,\sigma\_{a},\sigma\_{m})>0

###### Proof.

Appendix [B](https://arxiv.org/html/2511.03358v1#A2 "Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")
∎

In Appendix [B](https://arxiv.org/html/2511.03358v1#A2 "Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness"), the sign of the limit was numerically determined in ([18](https://arxiv.org/html/2511.03358v1#A2.E18 "In B.3. Proposition 5 ‣ Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")). The value of σa\sigma\_{a} at which it changes sign is

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | σa=π​Γ​(1−ν)Γ​(1/2−ν)\sigma\_{a}=\frac{\pi\Gamma(1-\nu)}{\Gamma(1/2-\nu)} |  |

which is a decreasing function in ν\nu, with a root at ν=0.5\nu=0.5. With this, and the previous determination that the phase transition contour is tangential to the σa\sigma\_{a} axis at the same value of ν\nu, ν3=0.5\nu\_{3}=0.5.

Solving ([8](https://arxiv.org/html/2511.03358v1#S4.E8 "In 4. Noise Induced Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) at σa=σc\sigma\_{a}=\sigma\_{c} yields ν≊0.28\nu\approxeq 0.28. For ν\nu below this, the phase transition 3→13\rightarrow 1 cannot exist for σa<σc\sigma\_{a}<\sigma\_{c}. Therefore ν2≊0.28\nu\_{2}\approxeq 0.28

By similar reasoning, for 0.28<ν<0.50.28<\nu<0.5 and σa\sigma\_{a} greater than but sufficiently close to σc\sigma\_{c}, the line of constant σa\sigma\_{a} must intersect the contour at least twice, corresponding to the phase change 1→3→11\rightarrow 3\rightarrow 1: unstable to stable, returning to unstable again (see Figure [2](https://arxiv.org/html/2511.03358v1#S3.F2 "Figure 2 ‣ 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness"), top left graph). ν1\nu\_{1} is in fact less than 0.28 as the asymptote of the phase transition contour is still smaller than its peak. This was determined numerically to be ν1≊0.11\nu\_{1}\approxeq 0.11. Below this point the contour is seen to be strictly increasing, limiting possible phase changes further.

## 5. Conclusions

In this work an MV-SDE with bistable drift, with additive and, novelly, multiplicative noise has been studied.
After a brief review of systemic risk, following [ss], a MV-SDE (Dawson-Shiino) model derived from a interacting diffusion model of systemic risk of interconnected components is presented. A range of scenarios where uncertainty in the robustness of the components may occur is discussed, and a novel MV-SDE model is derived.

For this model, the results have demonstrated the existence phase changes that cannot occur in the Dawson-Shiino model, that stem directly from varying noise interpretations and uncertainty in the robustness of components. Of particular interest, for a range of θ\theta a noise induced stability phenomenon was observed. Namely, if the additive noise σa\sigma\_{a} is set greater than, but sufficiently close to the critical temperature σc\sigma\_{c} of the limiting Dawson-Shiino model and an appropriate noise interpretation chosen, increasing multiplicative noise σm\sigma\_{m} will push the system into the stable phase. It will remain there, or re-enter the unstable phase depending again on ν\nu.

A potential future are of inquiry would be whether similar noise induced stability can be seen in MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) with a multi-well potential, see section 4 of [alecio]

## 6. Acknowelgement

The initial idea to study MV-SDE ([4](https://arxiv.org/html/2511.03358v1#S3.E4 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) numerically was Prof. G.A Pavliotis’.

![Refer to caption](figs/comp.png)


Figure 5. Panel of contour diagrams of F′​(ν,⋅,⋅)​[0]F^{{}^{\prime}}(\nu,\cdot,\cdot){[}0{]} for increasing ν\nu, green positive, blue negative. The phase transition contour intersects the σa\sigma\_{a} axis at σc\sigma\_{c}. Graph ν={0.75,1}\nu=\{0.75,1\} corresponds to column 4, ν=0.49\nu=0.49 and ν=0.35\nu=0.35 column 3, ν=0.2\nu=0.2 column 2 and ν=0\nu=0 column 1 of Table 1

## Appendix A Formal Identification of the Limit

Given the exchangeability and weak interaction between particles (inversely proportional to the number of particles), it seems reasonable to impose as an ansatz that the particles are identically and independently distributed, ρn≈∏l=1nρ​(xl,t)=ρ⊗n\rho\_{n}\approx\prod\_{l=1}^{n}\rho(x\_{l},t)=\rho^{\otimes n} as for nn sufficiently large.

The associated Fokker-Planck equation for the nn-particle system is

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | ∂ρN∂t=∑i=1N∂∂xi​(V′​(xi)+θ​(xi−1N​∑j=1Nxj))​ρN+∑i=1N∂2∂xi2​(σa2+σm2​xi22)​ρN\frac{\partial\rho\_{N}}{\partial t}=\sum\_{i=1}^{N}\frac{\partial}{\partial x\_{i}}\big(V^{\prime}(x\_{i})+\theta(x\_{i}-\frac{1}{N}\sum\_{j=1}^{N}x\_{j})\big)\rho\_{N}+\sum\_{i=1}^{N}\frac{\partial^{2}}{\partial x\_{i}^{2}}\big(\frac{\sigma\_{a}^{2}+\sigma\_{m}^{2}x\_{i}^{2}}{2}\big)\rho\_{N} |  |

To find a closed expression for ρ​(xi)=∫\iρN\rho(x\_{i})=\int\_{\backslash i}\rho^{N}, we integrate ([9](https://arxiv.org/html/2511.03358v1#A1.E9 "In Appendix A Formal Identification of the Limit ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) over all indices but the it​h\mathrm{i}^{th} - denoted as \i\backslash i.

Consider first the the terms deriving from the drift:

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | ∫\i∑i=1N∂∂xi​(V′​(xi)+θ​(xi−1N​∑j=1Nxj))​ρN=∂∂xi​∫\i(V′​(xi)+θ​(xi−1N​∑j=1Nxj))​ρN+∑\i∂∂xj​(V′​(xj)+θ​(xj−1N​∑k=1Nxk))​ρi​j​(xi,xj)|xj=−∞∞\begin{split}\int\_{\backslash i}\sum\_{i=1}^{N}\frac{\partial}{\partial x\_{i}}\big(V^{\prime}(x\_{i})+\theta(x\_{i}-\frac{1}{N}\sum\_{j=1}^{N}x\_{j})\big)\rho\_{N}=\frac{\partial}{\partial x\_{i}}\int\_{\backslash i}\big(V^{\prime}(x\_{i})+\theta(x\_{i}-\frac{1}{N}\sum\_{j=1}^{N}x\_{j})\big)\rho\_{N}\\ +\sum\_{\backslash i}\frac{\partial}{\partial x\_{j}}\big(V^{\prime}(x\_{j})+\theta(x\_{j}-\frac{1}{N}\sum\_{k=1}^{N}x\_{k})\big)\rho\_{ij}(x\_{i},x\_{j})|\_{x\_{j}=-\infty}^{\qquad\infty}\end{split} |  |

where we assume the both ρN\rho\_{N} and its first derivative with respect to all its variables decays to 0 sufficiently fast to annihilate all the terms in the second line and sufficient smoothness of ρN\rho^{N} to commute the integral and derivate. We can simplify the remaining term as follows.

|  |  |  |
| --- | --- | --- |
|  | ∂∂xi​(V′​(xi)​ρi+θ​(1−1N)​(xi+∫xi​ρi)​ρi)\frac{\partial}{\partial x\_{i}}\Big(V^{\prime}(x\_{i})\rho\_{i}+\theta(1-\frac{1}{N})\big(x\_{i}+\int x\_{i}\rho\_{i}\big)\rho\_{i}\Big) |  |

where we have used that ∫xi​ρi=∫xj​ρj\int x\_{i}\rho\_{i}=\int x\_{j}\rho\_{j} for any i,ji,j. Upon taking the limit N→∞N\rightarrow\infty we get:

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | ∂∂xi​(V′​(xi)+θ​(xi+∫xi​ρi))​ρi\frac{\partial}{\partial x\_{i}}\Big(V^{\prime}(x\_{i})+\theta\Big(x\_{i}+\int x\_{i}\rho\_{i})\Big)\rho\_{i} |  |

As for the second term, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | 12​∫\xi∑j∂2∂xj2​σ2​(xj)​ρN=∂2∂xi2​σ2​(xi)2​ρi+∑\i∂∂xj​σ2​(xj)2​ρi​j​(xi,xj)|xj=−∞∞\begin{split}\frac{1}{2}\int\_{\backslash x\_{i}}\sum\_{j}\frac{\partial^{2}}{\partial x\_{j}^{2}}\sigma^{2}(x\_{j})\rho^{N}=\\ \frac{\partial^{2}}{\partial x\_{i}^{2}}\frac{\sigma^{2}(x\_{i})}{2}\rho\_{i}+\sum\_{\backslash i}\frac{\partial}{\partial x\_{j}}\frac{\sigma^{2}(x\_{j})}{2}\rho\_{ij}(x\_{i},x\_{j})|\_{x\_{j}=-\infty}^{\qquad\infty}\end{split} |  |

The assumptions above are strong enough to ensure all the terms in the last sum are null. Adding the remaining term to ([11](https://arxiv.org/html/2511.03358v1#A1.E11 "In Appendix A Formal Identification of the Limit ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")), renaming ρi\rho\_{i} as ρ\rho we get ([5](https://arxiv.org/html/2511.03358v1#S3.E5 "In 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) as desired. An almost identical calculation can be done in the presence of non-Itô noise, for a suitable correction in the drift.
[infe]

![Refer to caption](figs/3db.png)


Figure 6. Panel of Bifurcation diagrams for ν\nu as inscribed

## Appendix B Proofs

### B.1. Proposition [2](https://arxiv.org/html/2511.03358v1#Thmproposition2 "Proposition 2 ([alecio]). ‣ 3. Mathematical Formulation ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")

It can be shown at a root of Fμ′​[0]F^{{}^{\prime}}\_{\mu}[0], the derivative with respect to θ\theta or aa must be positive, similarly to Proposition 3.5 [alecio]. Then, like Proposition 3.8 of [alecio], the interval(s) on which Fμ′​(σa,k​σm)​[0]>0F^{{}^{\prime}}\_{\mu}(\sigma\_{a},k\sigma\_{m})[0]>0 must be increasing.

### B.2. Proposition [4](https://arxiv.org/html/2511.03358v1#Thmproposition4 "Proposition 4 (Asymptotic Properties of 𝐹^'_𝜇⁢(𝜈,𝜎_𝑎,𝜎_𝑚)⁢[𝜇]: 𝜎_𝑚↓0 ). ‣ 4. Noise Induced Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")

The idea here is to expand the self-consistency equation, paying close attention to their radius of convergence, whilst recovering the Shiino-Dawson symmetric stationary measure. The radius of convergence of both arctan⁡σm​x\arctan\sigma\_{m}x and log⁡(1+σm​x)\log(1+\sigma\_{m}x) are finite, limiting the domain of the resulting integral:

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | 2​∫01σm2exp⁡(−x42​σa2)​((x−x3)+σm2​(1−ν)​x)​(x−σm2​x33​σa2+…)​(1+σm2σa2​(x63−ν​x2)+…)​𝑑x2\int\_{0}^{\frac{1}{\sigma\_{m}^{2}}}\exp(-\frac{x^{4}}{2\sigma\_{a}^{2}})((x-x^{3})+\sigma\_{m}^{2}(1-\nu)x)(x-\frac{\sigma\_{m}^{2}x^{3}}{3\sigma\_{a}^{2}}+\dots)(1+\frac{\sigma\_{m}^{2}}{\sigma\_{a}^{2}}(\frac{x^{6}}{3}-\nu x^{2})+\dots)dx |  |

On (1σm2,∞)(\frac{1}{\sigma\_{m}^{2}},\infty) the above integral is dominated by k​exp⁡(−σm2)k\exp(-\sigma\_{m}^{2})
Consequently, integral ([13](https://arxiv.org/html/2511.03358v1#A2.E13 "In B.2. Proposition 4 ‣ Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) can be extended to ∞\infty, yielding the following expression in the moments of ρ0\rho\_{0}, to order σm2\sigma\_{m}^{2}

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | (m2−m4)+σm2​(m8−m103​σa4+m6−m43​σa2−(1−θ)​m6−m8σa4+m2−ν​(m4−m6σa2+m2))+σm4​(…)(m\_{2}-m\_{4})+\sigma\_{m}^{2}\Big(\frac{m\_{8}-m\_{10}}{3\sigma\_{a}^{4}}+\frac{m\_{6}-m\_{4}}{3\sigma\_{a}^{2}}-(1-\theta)\frac{m\_{6}-m\_{8}}{\sigma\_{a}^{4}}+m\_{2}-\nu(\frac{m\_{4}-m\_{6}}{\sigma\_{a}^{2}}+m\_{2})\Big)+\sigma\_{m}^{4}(\dots) |  |

where a factor of σa2\sigma\_{a}^{2} has been eliminated. Using the moment hierarchy [dawson] of the symmetric stationary measure, ([14](https://arxiv.org/html/2511.03358v1#A2.E14 "In B.2. Proposition 4 ‣ Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) can be written entirely in terms of σa\sigma\_{a} and m2m\_{2}, see ([20](https://arxiv.org/html/2511.03358v1#A3.E20 "In Appendix C Moment Hierarchy of the Dawson-Shiino model ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) and Appendix [C](https://arxiv.org/html/2511.03358v1#A3 "Appendix C Moment Hierarchy of the Dawson-Shiino model ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness") for its derivation.

The 𝒪​(1)\mathcal{O}(1) term is just the self-consistency equation of the Dawson-Shiino model, and so is 0 at σa=σc\sigma\_{a}=\sigma\_{c}. For θ=1\theta=1, at the critical temperature ([14](https://arxiv.org/html/2511.03358v1#A2.E14 "In B.2. Proposition 4 ‣ Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) is

|  |  |  |
| --- | --- | --- |
|  | 12​(12−ν)​(1−m2)\frac{1}{2}(\frac{1}{2}-\nu)(1-m\_{2}) |  |

where m2=m2​(σcθ=1)≊0.457m\_{2}=m\_{2}(\sigma\_{c}^{\theta=1})\approxeq 0.457. This is a decreasing function in ν\nu with a root ν=12\nu=\frac{1}{2}.

### B.3. Proposition [5](https://arxiv.org/html/2511.03358v1#Thmproposition5 "Proposition 5 (Further Asymptotic Properties of 𝐹^'_𝜇⁢(𝜈,𝜎_𝑎,𝜎_𝑚)⁢[𝜇]: 𝜎_𝑚↑∞ ). ‣ 4. Noise Induced Stability ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")

Using the approach of [alecio], we rewrite Fμ′F^{{}^{\prime}}\_{\mu} as

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | 4σm​σa​∫ℝ+arctan⁡(σmσa​x)​(x​(1+σm2​(1−ν))−x3)​ρs​t\frac{4}{\sigma\_{m}\sigma\_{a}}\int\_{\mathbb{R^{+}}}\arctan(\frac{\sigma\_{m}}{\sigma\_{a}}x)\big(x(1+\sigma\_{m}^{2}(1-\nu))-x^{3}\big)\rho\_{st} |  |

This form is useful for σm<<1\sigma\_{m}<<1. For σm>>1\sigma\_{m}>>1 the substitution y=σm​xσay=\frac{\sigma\_{m}x}{\sigma\_{a}} yields a far more lucid expression,

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | 4​σaσm3​∫ℝ+arctan⁡(y)​(y​(1+σm2​(1−ν))−y3​σa2σm2)​(1+y2)−νexp⁡(σa2σm4​(log⁡(1+y2)−y2))​d​x\begin{split}\frac{4\sigma\_{a}}{\sigma\_{m}^{3}}\int\_{\mathbb{R^{+}}}\arctan(y)\big(y(1+\sigma\_{m}^{2}(1-\nu))-y^{3}\frac{\sigma\_{a}^{2}}{\sigma\_{m}^{2}}\big)(1+y^{2})^{-\nu}\\ \exp(\frac{\sigma\_{a}^{2}}{\sigma\_{m}^{4}}(\log(1+y^{2})-y^{2}))dx\end{split} |  |

If we can approximate arctan⁡(x)\arctan(x) and log⁡(x)\log(x) with power series, we can evaluate the resulting expression with the following formula.
With y≠−1y\neq-1 and x>0x>0

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | ∫x∞xy​exp⁡(−σa2​x2σm4)​𝑑x=12​σa−y−1​σm2​y+2​Γ​(y+12,σa2​x2σm4)≊12​σa−y−1​σm2​y+2​(Γ​(y+12)−2​(σa​x)y+1y+1​σm−2​y−2+𝒪​(σm−6−2​y))\begin{split}\int\_{x}^{\infty}x^{y}\exp(-\frac{\sigma\_{a}^{2}x^{2}}{\sigma\_{m}^{4}})dx=\frac{1}{2}\sigma\_{a}^{-y-1}\sigma\_{m}^{2y+2}\Gamma(\frac{y+1}{2},\frac{\sigma\_{a}^{2}x^{2}}{\sigma\_{m}^{4}})\approxeq\\ \frac{1}{2}\sigma\_{a}^{-y-1}\sigma\_{m}^{2y+2}\Big(\Gamma(\frac{y+1}{2})-\frac{2(\sigma\_{a}x)^{y+1}}{y+1}\sigma\_{m}^{-2y-2}+\mathcal{O}(\sigma\_{m}^{-6-2y})\Big)\end{split} |  |

where Γ​(x,y)\Gamma(x,y) is the incomplete Gamma function, [absteg].

For ν<0.5\nu<0.5 we derive the the asymptotic expansion of Fμ′F^{{}^{\prime}}\_{\mu} in σm\sigma\_{m} as follows. The difference of the integral over the entire real line and {|x|>1}\{|x|>1\} becomes negligible as σm\sigma\_{m} tends to ∞\infty. On this reduced domain, (1+x2)−ν∼x−2​ν(1+x^{2})^{-\nu}\sim x^{-2\nu}, (1+x2)−1σm4∼1(1+x^{2})^{-\frac{1}{\sigma\_{m}^{4}}}\sim 1 and arctan⁡(x)∼1−1x−13​x3\arctan(x)\sim 1-\frac{1}{x}-\frac{1}{3x^{3}}.

Substituting into equation ([16](https://arxiv.org/html/2511.03358v1#A2.E16 "In B.3. Proposition 5 ‣ Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) and using equation ([17](https://arxiv.org/html/2511.03358v1#A2.E17 "In B.3. Proposition 5 ‣ Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")) to evaluate the resulting expression, in expanding in powers of σm\sigma\_{m}:

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | 0.σm6−4​ν+σa2​ν−2​[π2​Γ​(1−ν)+σa​(Γ​(32−ν)−(1−ν)​Γ​(12−ν))]​σm4−4​ν+𝒪​(σm2−4​ν)0.\sigma\_{m}^{6-4\nu}+\sigma\_{a}^{2\nu-2}[\frac{\pi}{2}\Gamma(1-\nu)+\sigma\_{a}\big(\Gamma(\frac{3}{2}-\nu)-(1-\nu)\Gamma(\frac{1}{2}-\nu)\big)]\sigma\_{m}^{4-4\nu}+\mathcal{O}(\sigma\_{m}^{2-4\nu}) |  |

This changes sign when

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | σa=−π2​Γ​(1−ν)Γ​(3/2−ν)−(1−ν)​Γ​(1/2−ν)=π​Γ​(1−ν)Γ​(1/2−ν)\sigma\_{a}=-\frac{\frac{\pi}{2}\Gamma(1-\nu)}{\Gamma(3/2-\nu)-(1-\nu)\Gamma(1/2-\nu)}=\frac{\pi\Gamma(1-\nu)}{\Gamma(1/2-\nu)} |  |

a strictly decreasing function in ν\nu, with range [π,0][\sqrt{\pi},0]. When ν≊0.28\nu\approxeq 0.28 this occurs at σc\sigma\_{c}.

## Appendix C Moment Hierarchy of the Dawson-Shiino model

As noted in [dawson], the moments of the stationary measures of the Dawson-Shiino model can be found by solving the moment evolution equation. For the the symmetric stationary solution

|  |  |  |
| --- | --- | --- |
|  | m2​p=(1−θ)​m2​p−2+12​(2​p−3)​σa2​m2​p−4m\_{2p}=(1-\theta)m\_{2p-2}+\frac{1}{2}(2p-3)\sigma\_{a}^{2}m\_{2p-4} |  |

In terms of the m2m\_{2}, the first 5 even moments are:

|  |  |  |
| --- | --- | --- |
|  | m4=m2​(1−θ)+σa22m\_{4}=m\_{2}\left(1-\theta\right)+\frac{\sigma\_{a}^{2}}{2} |  |

|  |  |  |
| --- | --- | --- |
|  | m6=m2​(3​σa22+θ2−2​θ+1)−σa2​θ2+σa22m\_{6}=m\_{2}\left(\frac{3\sigma\_{a}^{2}}{2}+\theta^{2}-2\theta+1\right)-\frac{\sigma\_{a}^{2}\theta}{2}+\frac{\sigma\_{a}^{2}}{2} |  |

|  |  |  |
| --- | --- | --- |
|  | m8=m2​(−4​σa2​θ+4​σa2−θ3+3​θ2−3​θ+1)+5​σa44+σa2​θ22−σa2​θ+σa22m\_{8}=m\_{2}\left(-4\sigma\_{a}^{2}\theta+4\sigma\_{a}^{2}-\theta^{3}+3\theta^{2}-3\theta+1\right)+\frac{5\sigma\_{a}^{4}}{4}+\frac{\sigma\_{a}^{2}\theta^{2}}{2}-\sigma\_{a}^{2}\theta+\frac{\sigma\_{a}^{2}}{2} |  |

|  |  |  |
| --- | --- | --- |
|  | m10=m2​(21​σa44+15​σa2​θ22−15​σa2​θ+15​σa22+θ4−4​θ3+6​θ2−4​θ+1)−3​σa4​θ+3​σa4−σa2​θ32+3​σa2​θ22−3​σa2​θ2+σa22\begin{split}m\_{10}=m\_{2}\left(\frac{21\sigma\_{a}^{4}}{4}+\frac{15\sigma\_{a}^{2}\theta^{2}}{2}-15\sigma\_{a}^{2}\theta+\frac{15\sigma\_{a}^{2}}{2}+\theta^{4}-4\theta^{3}+6\theta^{2}-4\theta+1\right)\\ -3\sigma\_{a}^{4}\theta+3\sigma\_{a}^{4}-\frac{\sigma\_{a}^{2}\theta^{3}}{2}+\frac{3\sigma\_{a}^{2}\theta^{2}}{2}-\frac{3\sigma\_{a}^{2}\theta}{2}+\frac{\sigma\_{a}^{2}}{2}\end{split} |  |

Substituting into ([14](https://arxiv.org/html/2511.03358v1#A2.E14 "In B.2. Proposition 4 ‣ Appendix B Proofs ‣ Noise induced Stability of a Mean-Field model of Systemic Risk with uncertain robustness")):

|  |  |  |  |
| --- | --- | --- | --- |
| (20) |  | m2​(ν2−14+θ2​νσa2−θ26​σa2−θ​νσa2+θ12​σa2+112​σa2+θ46​σa4−θ32​σa4+θ22​σa4−θ6​σa4)−θ​ν2+5​θ24+124−θ312​σa2+θ26​σa2−θ12​σa2\begin{split}m\_{2}\left(\frac{\nu}{2}-\frac{1}{4}+\frac{\theta^{2}\nu}{\sigma\_{a}^{2}}-\frac{\theta^{2}}{6\sigma\_{a}^{2}}-\frac{\theta\nu}{\sigma\_{a}^{2}}+\frac{\theta}{12\sigma\_{a}^{2}}+\frac{1}{12\sigma\_{a}^{2}}+\frac{\theta^{4}}{6\sigma\_{a}^{4}}-\frac{\theta^{3}}{2\sigma\_{a}^{4}}+\frac{\theta^{2}}{2\sigma\_{a}^{4}}-\frac{\theta}{6\sigma\_{a}^{4}}\right)\\ -\frac{\theta\nu}{2}+\frac{5\theta}{24}+\frac{1}{24}-\frac{\theta^{3}}{12\sigma\_{a}^{2}}+\frac{\theta^{2}}{6\sigma\_{a}^{2}}-\frac{\theta}{12\sigma\_{a}^{2}}\end{split} |  |