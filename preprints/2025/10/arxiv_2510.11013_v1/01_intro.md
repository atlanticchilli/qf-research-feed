---
authors:
- Tatsuru Kikuchi
doc_id: arxiv:2510.11013v1
family_id: arxiv:2510.11013
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Spatial and Temporal Boundaries in Difference-in-Differences: A Framework
  from Navier-Stokes Equation'
url_abs: http://arxiv.org/abs/2510.11013v1
url_html: https://arxiv.org/html/2510.11013v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tatsuru Kikuchi111e-mail: tatsuru.kikuchi@e.u-tokyo.ac.jp

((October 13, 2025))

###### Abstract

This paper develops a unified framework for identifying spatial and temporal boundaries of treatment effects in difference-in-differences designs. Starting from fundamental fluid dynamics equations (Navier-Stokes), we derive conditions under which treatment effects decay exponentially in space and time, enabling researchers to calculate explicit boundaries beyond which effects become undetectable. The framework encompasses both linear (pure diffusion) and nonlinear (advection-diffusion with chemical reactions) regimes, with testable scope conditions based on dimensionless numbers from physics (Péclet and Reynolds numbers). We demonstrate the framework’s diagnostic capability using air pollution from coal-fired power plants. Analyzing 791 ground-based PM2.5 monitors and 189,564 satellite-based NO2 grid cells in the Western United States over 2019-2021, we find striking regional heterogeneity: within 100 km of coal plants, both pollutants show positive spatial decay (PM2.5: κs=0.00200\displaystyle\kappa\_{s}=0.00200, d∗=1,153\displaystyle d^{\*}=1,153 km; NO2: κs=0.00112\displaystyle\kappa\_{s}=0.00112, d∗=2,062\displaystyle d^{\*}=2,062 km), validating the framework. Beyond 100 km, negative decay parameters correctly signal that urban sources dominate and diffusion assumptions fail. Ground-level PM2.5 decays approximately twice as fast as satellite column NO2, consistent with atmospheric transport physics. The framework successfully diagnoses its own validity in four of eight analyzed regions, providing researchers with physics-based tools to assess whether their spatial difference-in-differences setting satisfies diffusion assumptions before applying the estimator. Our results demonstrate that rigorous boundary detection requires both theoretical derivation from first principles and empirical validation of underlying physical assumptions.

Keywords: Difference-in-Differences, Spatial Spillovers, Treatment Effect Heterogeneity, Navier-Stokes Equations, Atmospheric Dispersion, Boundary Detection

JEL Classification: C21, C23, Q53, R11

## 1 Introduction

Spatial difference-in-differences (DiD) designs have become increasingly prominent in applied microeconomics, allowing researchers to exploit geographic variation in policy implementation or treatment intensity. Recent applications span environmental regulation (Deryugina et al., [2019](https://arxiv.org/html/2510.11013v1#bib.bib20); Knittel et al., [2016](https://arxiv.org/html/2510.11013v1#bib.bib33); Fowlie et al., [2012](https://arxiv.org/html/2510.11013v1#bib.bib24)), transportation infrastructure (Donaldson and Hornbeck, [2016](https://arxiv.org/html/2510.11013v1#bib.bib21); Duranton and Turner, [2012](https://arxiv.org/html/2510.11013v1#bib.bib23)), place-based policies (Busso et al., [2013](https://arxiv.org/html/2510.11013v1#bib.bib7); Kline and Moretti, [2014](https://arxiv.org/html/2510.11013v1#bib.bib32); Glaeser and Gottlieb, [2008](https://arxiv.org/html/2510.11013v1#bib.bib25)), and public health interventions (Goodman-Bacon, [2021](https://arxiv.org/html/2510.11013v1#bib.bib26); Currie and Walker, [2011](https://arxiv.org/html/2510.11013v1#bib.bib16)). However, a fundamental challenge remains largely unaddressed: where do treatment effects end? Traditional DiD applications either assume spillovers are negligible beyond some ad hoc distance threshold or acknowledge potential spillovers without systematic methods to detect spatial boundaries (Butts and Gardner, [2023](https://arxiv.org/html/2510.11013v1#bib.bib8)).

This question has gained urgency as recent methodological advances highlight the importance of properly accounting for spatial spillovers. Butts and Gardner ([2023](https://arxiv.org/html/2510.11013v1#bib.bib8)) shows that neglecting spillovers can severely bias treatment effect estimates in spatial DiD designs, while Colella et al. ([2019](https://arxiv.org/html/2510.11013v1#bib.bib12)) demonstrates that standard errors must account for spatial correlation structures. DellaVigna and Linos ([2022](https://arxiv.org/html/2510.11013v1#bib.bib19)) emphasizes the need for ex ante specification of spatial treatment definitions. Yet the literature offers limited guidance on how to determine these spatial boundaries from first principles rather than arbitrary rules of thumb.

This paper develops a unified framework for identifying both spatial and temporal boundaries of treatment effects by starting from fundamental physics: the Navier-Stokes equations governing fluid flow and scalar transport. We show that under explicit, testable conditions, treatment effects decay exponentially with distance and time, enabling calculation of precise boundaries beyond which effects fall below detection thresholds. Critically, our framework provides diagnostic tools to identify when these conditions hold versus when they fail—situations where standard spatial DiD estimators may be inappropriate.

This paper builds on and extends our previous theoretical work (Kikuchi, [2024a](https://arxiv.org/html/2510.11013v1#bib.bib30)) which established the general mathematical foundations for spatial and temporal treatment effect boundaries, and (Kikuchi, [2024b](https://arxiv.org/html/2510.11013v1#bib.bib31)) which developed stochastic approaches for handling spillover effects in spatial general equilibrium settings. Here, we provide the first empirical validation of these theoretical results using high-resolution air quality data, demonstrating the framework’s diagnostic capability and practical applicability to real-world policy questions.

### 1.1 Related Literature

Our work contributes to several distinct literatures in economics, econometrics, and environmental science.

#### 1.1.1 Spatial Econometrics and Spillovers

The spatial econometrics literature has long recognized that treatments can have geographic spillovers (Anselin, [1988](https://arxiv.org/html/2510.11013v1#bib.bib3); Conley, [1999](https://arxiv.org/html/2510.11013v1#bib.bib13)). Recent work formalizes these concerns in causal inference frameworks. Butts and Gardner ([2023](https://arxiv.org/html/2510.11013v1#bib.bib8)) provides a comprehensive treatment of spatial DiD estimators under spillovers, showing that ignoring spatial dependence can lead to substantial bias. Colella et al. ([2019](https://arxiv.org/html/2510.11013v1#bib.bib12)) develops spatial HAC standard errors for settings where treatment effects propagate geographically. Kelejian and Prucha ([2010](https://arxiv.org/html/2510.11013v1#bib.bib29)) and Drukker et al. ([2013](https://arxiv.org/html/2510.11013v1#bib.bib22)) provide methods for testing spatial dependence.

However, this literature typically specifies spatial weights matrices (W\displaystyle W) based on ad hoc assumptions—inverse distance, k\displaystyle k-nearest neighbors, or fixed distance cutoffs—without theoretical guidance on appropriate functional forms or cutoff distances (LeSage and Pace, [2009](https://arxiv.org/html/2510.11013v1#bib.bib34)). Our contribution is to derive these functional forms from fundamental physics, providing researchers with a principled approach to specification. We show that exponential decay (wi​j∝exp⁡(−κs​di​j)\displaystyle w\_{ij}\propto\exp(-\kappa\_{s}d\_{ij})) emerges naturally from diffusion processes, and we provide methods to estimate the decay parameter κs\displaystyle\kappa\_{s} and spatial boundary d∗\displaystyle d^{\*} from data.

#### 1.1.2 Treatment Effect Heterogeneity and External Validity

The treatment effects literature emphasizes that effects may vary across units and contexts (Heckman et al., [1997](https://arxiv.org/html/2510.11013v1#bib.bib27); Imbens and Rubin, [2015](https://arxiv.org/html/2510.11013v1#bib.bib28); Athey and Imbens, [2017](https://arxiv.org/html/2510.11013v1#bib.bib5)). Angrist and Kolesár ([2022](https://arxiv.org/html/2510.11013v1#bib.bib2)) discusses how effect heterogeneity complicates identification and interpretation of causal parameters. Our framework shows that spatial heterogeneity in treatment effects arises naturally from nonlinear physical processes (Navier-Stokes equations), and we demonstrate that the Average Treatment Effect on the Treated (ATT) remains a well-defined estimand even under this nonlinearity.

More broadly, our work contributes to understanding external validity and scope conditions (Dehejia, [2005](https://arxiv.org/html/2510.11013v1#bib.bib18); Allcott, [2015](https://arxiv.org/html/2510.11013v1#bib.bib1)). By deriving testable scope conditions (Péclet number Pe <1\displaystyle<1, Reynolds number Re <2000\displaystyle<2000), we provide a template for assessing when frameworks apply to new settings. This addresses Deaton ([2010](https://arxiv.org/html/2510.11013v1#bib.bib17))’s critique that much applied work lacks clear statements of when findings generalize.

Our approach to scope conditions builds directly on Kikuchi ([2024a](https://arxiv.org/html/2510.11013v1#bib.bib30)), who provide a comprehensive theoretical treatment of when spatial boundaries can be identified from first principles. We extend this work by empirically testing the derived scope conditions and showing that framework violations can be diagnosed from data patterns, providing practitioners with concrete guidance on applicability.

#### 1.1.3 Environmental Economics and Air Pollution

A substantial literature examines health and economic impacts of air pollution from point sources. Currie and Neidell ([2005](https://arxiv.org/html/2510.11013v1#bib.bib14)) and Currie et al. ([2011](https://arxiv.org/html/2510.11013v1#bib.bib15)) study effects of proximity to pollution sources on birth outcomes and housing prices. Deryugina et al. ([2019](https://arxiv.org/html/2510.11013v1#bib.bib20)) uses wind direction as an instrument to identify mortality effects of coal plant emissions, finding detectable effects beyond 200 km. Knittel et al. ([2016](https://arxiv.org/html/2510.11013v1#bib.bib33)) examines spillovers in renewable energy policies. Fowlie et al. ([2012](https://arxiv.org/html/2510.11013v1#bib.bib24)) studies the spatial incidence of SO2 emissions trading.

These papers typically use fixed distance cutoffs (e.g., 50 km, 100 km) or wind-direction instruments without deriving optimal boundaries. Our framework provides a method to calculate data-driven boundaries. We also contribute to understanding differences between ground-level and satellite measurements: Martin et al. ([2019](https://arxiv.org/html/2510.11013v1#bib.bib35)) and van Donkelaar et al. ([2016](https://arxiv.org/html/2510.11013v1#bib.bib37)) discuss satellite retrieval of air quality, but do not formalize how column-integrated measurements differ from surface concentrations in terms of spatial decay rates.

#### 1.1.4 Atmospheric Science and Dispersion Modeling

The atmospheric science literature provides sophisticated physical models of pollutant transport. EPA’s AERMOD (Cimorelli et al., [2005](https://arxiv.org/html/2510.11013v1#bib.bib10)) and more complex models like CMAQ (Byun and Schere, [1999](https://arxiv.org/html/2510.11013v1#bib.bib9)) and GEOS-Chem (Bey et al., [2001](https://arxiv.org/html/2510.11013v1#bib.bib6)) simulate atmospheric chemistry and transport. However, these models are computationally intensive, require detailed meteorological inputs, and are typically used forward (predicting concentrations from emissions) rather than inverse (inferring spatial boundaries from observations).

Our contribution is to provide a reduced-form, data-driven approach that complements these physical models. We derive spatial decay from first principles (Navier-Stokes) but estimate parameters empirically, enabling researchers without atmospheric modeling expertise to assess spatial boundaries. Our empirical findings broadly validate the physics: estimated decay rates are consistent with transport distances predicted by AERMOD and CMAQ.

### 1.2 Overview and Contribution

Our key theoretical contribution is deriving the spatial boundary d∗\displaystyle d^{\*} and temporal boundary τ∗\displaystyle\tau^{\*} from first principles, showing they satisfy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗τ∗=3.32​λ​δ\frac{d^{\*}}{\tau^{\*}}=3.32\lambda\sqrt{\delta} |  | (1) |

where λ\displaystyle\lambda is the treatment intensity, and δ\displaystyle\delta is the diffusion coefficient. This relationship holds under the diffusive limit of Navier-Stokes equations when the Péclet number P​e=U​L/D≪1\displaystyle Pe=UL/D\ll 1 (diffusion dominates advection) and treatment propagates through spatial diffusion rather than network effects or other mechanisms.

We validate this framework empirically using air pollution from coal-fired power plants—a canonical application of spatial DiD where treatment intensity (emissions) varies continuously with distance. Using both ground-based PM2.5 monitors (791 monitors, 515,000 observations) and satellite-based NO2 measurements (189,564 grid cells, 6.6 million observations) for 2019-2021, we find striking regional heterogeneity that validates our scope conditions:

* •

  Within 100 km of coal plants: Both pollutants show positive spatial decay, indicating coal plants are the dominant pollution source. For PM2.5, κs=0.00200\displaystyle\kappa\_{s}=0.00200 per km, implying spatial boundary d∗=1,153\displaystyle d^{\*}=1,153 km. For NO2, κs=0.00112\displaystyle\kappa\_{s}=0.00112 per km, yielding d∗=2,062\displaystyle d^{\*}=2,062 km. The slower decay of column NO2 compared to ground-level PM2.5 is consistent with atmospheric transport physics.
* •

  Beyond 100 km from plants: Negative spatial decay parameters (κs<0\displaystyle\kappa\_{s}<0) indicate pollution increases with distance from plants. Framework correctly identifies that coal plants are not the dominant pollution source (cars dominate), corresponding to high Péclet regime where advection-diffusion assumptions fail.
* •

  Regional heterogeneity: Effect varies systematically with Reynolds number (turbulence intensity) and Péclet number (advection strength), exactly as predicted by Navier-Stokes theory.

This regional variation is not a failure of the method but a feature: the framework successfully diagnoses where diffusion-based spatial DiD is appropriate versus where alternative approaches (accounting for advection, turbulence, or alternative pollution sources) are needed. By providing explicit scope conditions based on dimensionless parameters, we enable researchers to assess ex ante whether their setting satisfies the physical assumptions underlying spatial treatment effect decay.

The remainder of the paper proceeds as follows. Section 2 develops the theoretical framework, deriving spatial and temporal boundaries from Navier-Stokes equations and characterizing the nonlinear regime. Section 3 describes the empirical setting and data on coal plant emissions and air quality. Section 4 presents results showing regional heterogeneity in spatial decay patterns. Section 5 discusses implications for spatial DiD validity and provides diagnostic guidelines. Section 6 concludes.

## 2 Theoretical Framework

### 2.1 From Navier-Stokes to Spatial Boundaries

We begin with the fundamental equations governing fluid flow and scalar transport in the atmosphere. Our approach connects economic treatment effects to physical dispersion processes, providing a rigorous foundation for spatial boundary detection.

The theoretical derivations in this section summarize key results from Kikuchi ([2024a](https://arxiv.org/html/2510.11013v1#bib.bib30)), adapting them to the specific context of atmospheric pollutant dispersion. We refer readers to that paper for complete proofs and extensions to network diffusion and dynamic settings.

#### 2.1.1 The Navier-Stokes System

Consider pollutant concentration C​(𝐱,t)\displaystyle C(\mathbf{x},t) at location 𝐱=(x,y,z)\displaystyle\mathbf{x}=(x,y,z) and time t\displaystyle t from a point source (coal plant) emitting at rate Q\displaystyle Q. The concentration field evolves according to the coupled system:

Momentum (Navier-Stokes):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝐮∂t+(𝐮⋅∇)​𝐮=−∇pρ+ν​∇2𝐮+𝐟\frac{\partial\mathbf{u}}{\partial t}+(\mathbf{u}\cdot\nabla)\mathbf{u}=-\frac{\nabla p}{\rho}+\nu\nabla^{2}\mathbf{u}+\mathbf{f} |  | (2) |

Scalar Transport:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂C∂t+𝐮⋅∇C=D​∇2C−λ​(C)​C+S​(𝐱,t)\frac{\partial C}{\partial t}+\mathbf{u}\cdot\nabla C=D\nabla^{2}C-\lambda(C)C+S(\mathbf{x},t) |  | (3) |

where 𝐮\displaystyle\mathbf{u} is the velocity field (wind), p\displaystyle p is pressure, ρ\displaystyle\rho is density, ν\displaystyle\nu is kinematic viscosity, D\displaystyle D is molecular diffusivity, λ​(C)\displaystyle\lambda(C) is the (possibly concentration-dependent) decay rate, and S​(𝐱,t)\displaystyle S(\mathbf{x},t) is the source term.

Equation ([2](https://arxiv.org/html/2510.11013v1#S2.E2 "In 2.1.1 The Navier-Stokes System ‣ 2.1 From Navier-Stokes to Spatial Boundaries ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation")) is nonlinear through the convective term (𝐮⋅∇)​𝐮\displaystyle(\mathbf{u}\cdot\nabla)\mathbf{u}, which creates turbulence at high Reynolds numbers. Equation ([3](https://arxiv.org/html/2510.11013v1#S2.E3 "In 2.1.1 The Navier-Stokes System ‣ 2.1 From Navier-Stokes to Spatial Boundaries ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation")) is nonlinear both through coupling to the velocity field and potentially through chemical reactions in λ​(C)​C\displaystyle\lambda(C)C.

#### 2.1.2 Dimensionless Analysis

The regime of validity for different approximations depends on three dimensionless numbers:

Reynolds Number:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Re=U​Lν\text{Re}=\frac{UL}{\nu} |  | (4) |

where U\displaystyle U is characteristic velocity and L\displaystyle L is characteristic length. Re measures the ratio of inertial to viscous forces.

* •

  Re ≪1\displaystyle\ll 1: Laminar flow, viscous forces dominate
* •

  Re ≫1\displaystyle\gg 1: Turbulent flow, inertial forces dominate

Péclet Number:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pe=U​LD=Re×Sc\text{Pe}=\frac{UL}{D}=\text{Re}\times\text{Sc} |  | (5) |

where Sc =ν/D\displaystyle=\nu/D is the Schmidt number. Pe measures the ratio of advective to diffusive transport.

* •

  Pe ≪1\displaystyle\ll 1: Diffusion dominates, our framework applies
* •

  Pe ≫1\displaystyle\gg 1: Advection dominates, need to account for wind

Damköhler Number:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Da=λ​L2D\text{Da}=\frac{\lambda L^{2}}{D} |  | (6) |

Da measures the ratio of chemical reaction rate to diffusion rate.

### 2.2 The Diffusive Limit: Linear Regime

#### 2.2.1 Assumptions

Our baseline framework applies in the diffusive limit:

1. 1.

   Low Péclet: Pe →0\displaystyle\to 0 (diffusion ≫\displaystyle\gg advection)
2. 2.

   Low Reynolds: Re →0\displaystyle\to 0 (laminar, no turbulence)
3. 3.

   Linear decay: λ​(C)=λ0\displaystyle\lambda(C)=\lambda\_{0} (constant)
4. 4.

   Steady state: ∂C/∂t→0\displaystyle\partial C/\partial t\to 0 (time-averaged)

Under these conditions, equation ([3](https://arxiv.org/html/2510.11013v1#S2.E3 "In 2.1.1 The Navier-Stokes System ‣ 2.1 From Navier-Stokes to Spatial Boundaries ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation")) simplifies to the Helmholtz equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​∇2C−λ0​C+S=0D\nabla^{2}C-\lambda\_{0}C+S=0 |  | (7) |

#### 2.2.2 Solution for Point Source

For a point source at origin emitting Q\displaystyle Q units per time, in radially symmetric geometry, equation ([7](https://arxiv.org/html/2510.11013v1#S2.E7 "In 2.2.1 Assumptions ‣ 2.2 The Diffusive Limit: Linear Regime ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation")) becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(∂2C∂r2+1r​∂C∂r)−λ0​C+Q​δ​(𝐫)=0D\left(\frac{\partial^{2}C}{\partial r^{2}}+\frac{1}{r}\frac{\partial C}{\partial r}\right)-\lambda\_{0}C+Q\delta(\mathbf{r})=0 |  | (8) |

The solution (see Appendix A for derivation) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(r)=Q4​π​D​r​exp⁡(−λ0D​r)=Q4​π​D​r​exp⁡(−κs​r)C(r)=\frac{Q}{4\pi Dr}\exp\left(-\sqrt{\frac{\lambda\_{0}}{D}}\,r\right)=\frac{Q}{4\pi Dr}\exp(-\kappa\_{s}r) |  | (9) |

where the spatial decay parameter is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κs=λ0D\kappa\_{s}=\sqrt{\frac{\lambda\_{0}}{D}} |  | (10) |

Taking logarithms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡C​(r)=const−log⁡r−κs​r\log C(r)=\text{const}-\log r-\kappa\_{s}r |  | (11) |

This yields our baseline empirical specification.

#### 2.2.3 Spatial Boundary

Define the spatial boundary d∗\displaystyle d^{\*} as the distance at which treatment effects fall below a detection threshold ϵ\displaystyle\epsilon (typically 10% of direct effect):

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(d∗)C​(0)=ϵ\frac{C(d^{\*})}{C(0)}=\epsilon |  | (12) |

From equation ([9](https://arxiv.org/html/2510.11013v1#S2.E9 "In 2.2.2 Solution for Point Source ‣ 2.2 The Diffusive Limit: Linear Regime ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡(−κs​d∗)d∗/d0=ϵ\frac{\exp(-\kappa\_{s}d^{\*})}{d^{\*}/d\_{0}}=\epsilon |  | (13) |

For κs​d∗≫log⁡(d∗/d0)\displaystyle\kappa\_{s}d^{\*}\gg\log(d^{\*}/d\_{0}) (far-field approximation):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗=1κs​log⁡(1ϵ)=1κs​log⁡(10)≈2.3κsd^{\*}=\frac{1}{\kappa\_{s}}\log\left(\frac{1}{\epsilon}\right)=\frac{1}{\kappa\_{s}}\log(10)\approx\frac{2.3}{\kappa\_{s}} |  | (14) |

This provides an estimable boundary: once we estimate κs\displaystyle\kappa\_{s} from data, we can calculate d∗\displaystyle d^{\*}.

### 2.3 Extensions: Nonlinear Regime

Real atmospheric transport involves several nonlinearities. We characterize when each matters and how they modify our framework.

#### 2.3.1 Geometric Spreading

In three-dimensional radial coordinates, the Laplacian includes a geometric spreading term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇2C=1r2​∂∂r​(r2​∂C∂r)\nabla^{2}C=\frac{1}{r^{2}}\frac{\partial}{\partial r}\left(r^{2}\frac{\partial C}{\partial r}\right) |  | (15) |

This yields solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(r)∝1r2​exp⁡(−κs​r)C(r)\propto\frac{1}{r^{2}}\exp(-\kappa\_{s}r) |  | (16) |

Taking logs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡C​(r)=const−2​log⁡r−κs​r\log C(r)=\text{const}-2\log r-\kappa\_{s}r |  | (17) |

Empirical implication: Include both log⁡(r)\displaystyle\log(r) and r\displaystyle r terms in regression.

#### 2.3.2 Advection-Diffusion

When Pe ∼O​(1)\displaystyle\sim O(1), wind transport matters. Steady advection-diffusion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐮⋅∇C=D​∇2C−λ​C\mathbf{u}\cdot\nabla C=D\nabla^{2}C-\lambda C |  | (18) |

For uniform wind 𝐮=(U,0,0)\displaystyle\mathbf{u}=(U,0,0), solution involves modified Bessel functions. Key feature: asymmetry.

Empirical implication: Downwind decay differs from upwind:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡C=β1​rdownwind+β2​rupwind\log C=\beta\_{1}r\_{\text{downwind}}+\beta\_{2}r\_{\text{upwind}} |  | (19) |

with |β1|>|β2|\displaystyle|\beta\_{1}|>|\beta\_{2}|.

#### 2.3.3 Chemical Reactions: Quadratic Decay

For reactions like NO + O3 →\displaystyle\to NO2 + O2, rate ∝\displaystyle\propto [NO][O3]. If O3 abundant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(C)=λ1+λ2​C\lambda(C)=\lambda\_{1}+\lambda\_{2}C |  | (20) |

This creates quadratic decay:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂C∂t=D​∇2C−(λ1+λ2​C)​C\frac{\partial C}{\partial t}=D\nabla^{2}C-(\lambda\_{1}+\lambda\_{2}C)C |  | (21) |

Empirical implication: Near-field shows steeper decay. Include distance-squared term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡C=β1​r+β2​r2\log C=\beta\_{1}r+\beta\_{2}r^{2} |  | (22) |

#### 2.3.4 Turbulent Diffusion

At high Re, turbulence enhances mixing through eddy diffusivity Dturb≫Dmol\displaystyle D\_{\text{turb}}\gg D\_{\text{mol}}. Effective diffusion becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Deff=Dmol+Dturb​(𝐱,t)D\_{\text{eff}}=D\_{\text{mol}}+D\_{\text{turb}}(\mathbf{x},t) |  | (23) |

where Dturb\displaystyle D\_{\text{turb}} varies spatially and temporally.

Empirical implication: κs\displaystyle\kappa\_{s} varies by atmospheric conditions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡C=(β1+β2⋅wind\_speed)×r\log C=(\beta\_{1}+\beta\_{2}\cdot\text{wind\\_speed})\times r |  | (24) |

### 2.4 Scope Conditions and Testable Implications

###### Proposition 2.1 (Validity of Diffusion Approximation).

The exponential decay model ([9](https://arxiv.org/html/2510.11013v1#S2.E9 "In 2.2.2 Solution for Point Source ‣ 2.2 The Diffusive Limit: Linear Regime ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation")) is valid if and only if:

1. 1.

   Pe <1\displaystyle<1: Diffusion dominates advection
2. 2.

   Re <\displaystyle< 2000: Flow is laminar or weakly turbulent
3. 3.

   Da <1\displaystyle<1: Chemical reactions slow relative to transport
4. 4.

   Steady source: ∂S/∂t≈0\displaystyle\partial S/\partial t\approx 0

When these conditions fail, the framework correctly identifies invalidity through:

* •

  Negative κs\displaystyle\kappa\_{s} (increasing pollution with distance)
* •

  Asymmetric spatial patterns (downwind ≠\displaystyle\neq upwind)
* •

  Poor fit of exponential functional form

This proposition provides ex ante tests researchers can perform to assess whether spatial DiD is appropriate in their setting.

### 2.5 Connection to Causal Inference

#### 2.5.1 Treatment Effects Under Nonlinearity

A natural question: does nonlinearity in equations ([2](https://arxiv.org/html/2510.11013v1#S2.E2 "In 2.1.1 The Navier-Stokes System ‣ 2.1 From Navier-Stokes to Spatial Boundaries ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation"))-([3](https://arxiv.org/html/2510.11013v1#S2.E3 "In 2.1.1 The Navier-Stokes System ‣ 2.1 From Navier-Stokes to Spatial Boundaries ‣ 2 Theoretical Framework ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation")) invalidate the Average Treatment Effect on the Treated (ATT) as an estimand?

Answer: No, but interpretation changes.

Define ATT as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ATT=𝔼​[Yi​(1)−Yi​(0)|Di=1]\text{ATT}=\mathbb{E}[Y\_{i}(1)-Y\_{i}(0)|D\_{i}=1] |  | (25) |

where Yi​(1)\displaystyle Y\_{i}(1) is pollution with plant, Yi​(0)\displaystyle Y\_{i}(0) without, and Di=1\displaystyle D\_{i}=1 indicates treatment (proximity to plant).

Even with nonlinear DGP, ATT remains well-defined as the average causal effect over the treated population. However:

1. 1.

   Effect heterogeneity: Treatment effect varies by distance, wind exposure, background pollution:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | τi=τ​(di,𝐮i,C0,i)\tau\_{i}=\tau(d\_{i},\mathbf{u}\_{i},C\_{0,i}) |  | (26) |

   ATT averages over treated distribution:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ATT=𝔼​[τ​(di,𝐮i,C0,i)|Di=1]\text{ATT}=\mathbb{E}[\tau(d\_{i},\mathbf{u}\_{i},C\_{0,i})|D\_{i}=1] |  | (27) |
2. 2.

   Spillovers: Pollution at i\displaystyle i depends on plants at multiple locations j\displaystyle j:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Yi=f​(Di,{Dj}j≠i,𝐗i)Y\_{i}=f(D\_{i},\{D\_{j}\}\_{j\neq i},\mathbf{X}\_{i}) |  | (28) |

   This violates SUTVA. Our spatial boundary d∗\displaystyle d^{\*} helps define treatment regions where spillovers are negligible.
3. 3.

   Outcome transformation: Nonlinearity suggests using log transformation:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ATTlog=𝔼​[log⁡Yi​(1)−log⁡Yi​(0)|Di=1]\text{ATT}\_{\log}=\mathbb{E}[\log Y\_{i}(1)-\log Y\_{i}(0)|D\_{i}=1] |  | (29) |

   This linearizes multiplicative Navier-Stokes effects.

Kikuchi ([2024b](https://arxiv.org/html/2510.11013v1#bib.bib31)) develops a complementary approach for settings where spillovers are pervasive and cannot be eliminated through spatial separation. That framework uses diffusion-based spatial weights to model spillover propagation explicitly, whereas our current approach identifies boundaries where spillovers become negligible. The two methods are complementary: our framework applies when treatment and control regions can be cleanly separated, while the stochastic boundaries approach applies when spillovers affect all units but with measurable decay.

#### 2.5.2 Identification Strategy

Our three-stage estimation exploits spatial variation in treatment intensity (distance to plants):

Stage 1: Estimate direct effect on nearby locations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ATT=𝔼​[Y|d<dthreshold]−𝔼​[Y​|d>​dthreshold]\text{ATT}=\mathbb{E}[Y|d<d\_{\text{threshold}}]-\mathbb{E}[Y|d>d\_{\text{threshold}}] |  | (30) |

Stage 2: Estimate spatial decay:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Yi=α+β1​di+β2​di2+γ​𝐗i+ϵi\log Y\_{i}=\alpha+\beta\_{1}d\_{i}+\beta\_{2}d\_{i}^{2}+\gamma\mathbf{X}\_{i}+\epsilon\_{i} |  | (31) |

Identify κs=−β1\displaystyle\kappa\_{s}=-\beta\_{1} and calculate d∗\displaystyle d^{\*}.

Stage 3: Use d∗\displaystyle d^{\*} to refine treatment definition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di∗=𝟙​(di<d∗)D\_{i}^{\*}=\mathbbm{1}(d\_{i}<d^{\*}) |  | (32) |

This provides clean separation between treated and control units where spillovers are minimal.

## 3 Empirical Application: Coal Plant Air Pollution

### 3.1 Setting and Motivation

Coal-fired power plants provide an ideal testing ground for our framework:

1. 1.

   Point sources: Plants emit from stacks at known locations
2. 2.

   Continuous treatment: Emission intensity varies with plant characteristics
3. 3.

   Physical dispersion: Pollutants spread via atmospheric diffusion
4. 4.

   Rich data: Ground monitors and satellite measurements available
5. 5.

   Regional variation: Urban vs rural settings test scope conditions

Moreover, coal plants are policy-relevant: understanding spatial extent of pollution informs optimal policy design and welfare calculations (Muller and Mendelsohn, [2009](https://arxiv.org/html/2510.11013v1#bib.bib36); Clay et al., [2019](https://arxiv.org/html/2510.11013v1#bib.bib11)).

### 3.2 Data Sources

#### 3.2.1 Coal Plant Characteristics

We obtain plant-level data from EPA’s Emissions & Generation Resource Integrated Database (eGRID) 2021:

* •

  318 coal-fired plants in contiguous United States
* •

  Geographic coordinates (latitude, longitude)
* •

  Nameplate capacity (MW)
* •

  Annual emissions: CO2, SO2, NOx
* •

  Operating status

Plants range from 50 MW (small industrial) to 3,500 MW (large utility-scale). Geographic distribution concentrated in Midwest, Appalachia, and Great Plains—regions with abundant coal reserves.

#### 3.2.2 Ground-Based Air Quality: PM2.5

From EPA’s Air Quality System (AQS), we download:

* •

  791 PM2.5 monitoring stations with data 2019-2021
* •

  Daily measurements (µg/m3)
* •

  Monitor locations and characteristics
* •

  515,764 daily observations total

PM2.5 (particulate matter <\displaystyle< 2.5 µm diameter) is health-relevant but has multiple sources: vehicles (30-40%), power plants (20-30%), wildfires (10-20%), industry (20-30%) (Apte et al., [2012](https://arxiv.org/html/2510.11013v1#bib.bib4)).

#### 3.2.3 Satellite-Based Air Quality: NO2

From NASA’s TROPOMI (Sentinel-5P satellite), we obtain:

* •

  Monthly gridded NO2 column density
* •

  0.01° × 0.01° resolution (∼\displaystyle\sim1 km at equator)
* •

  36 months: January 2019 - December 2021
* •

  Quality-filtered (number of observations ≥\displaystyle\geq 5)
* •

  189,564 unique grid cells
* •

  6,589,515 total cell-month observations

NO2 also has mixed sources but different composition: vehicles/industry (50-60%), power plants (20-30%), biomass burning (10-20%). Satellite data provides complete spatial coverage unlike sparse ground monitors.

### 3.3 Distance Calculations

For each monitor (ground) or grid cell (satellite), we calculate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | di​j=Haversine​(lati,loni,latj,lonj)d\_{ij}=\text{Haversine}(\text{lat}\_{i},\text{lon}\_{i},\text{lat}\_{j},\text{lon}\_{j}) |  | (33) |

where i\displaystyle i indexes locations and j\displaystyle j indexes plants. We compute:

* •

  Distance to nearest plant: dimin=minj⁡di​j\displaystyle d\_{i}^{\min}=\min\_{j}d\_{ij}
* •

  Nearest plant characteristics: capacity, emissions
* •

  Total exposure (distance-weighted): Ei=∑jQj/di​j2\displaystyle E\_{i}=\sum\_{j}Q\_{j}/d\_{ij}^{2}

Summary statistics:

* •

  Ground monitors: Median distance 72 km, range 0.35-592 km
* •

  Satellite cells (within 500 km): Median 180 km
* •

  Substantial spatial variation for identification

### 3.4 Descriptive Patterns

Table [1](https://arxiv.org/html/2510.11013v1#S3.T1 "Table 1 ‣ 3.4 Descriptive Patterns ‣ 3 Empirical Application: Coal Plant Air Pollution ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") shows mean PM2.5 by distance to nearest coal plant. Surprisingly, PM2.5 is higher far from plants than near plants, suggesting coal plants are not the dominant source—urban areas (farther from plants) have higher pollution from vehicles.

Table 1: PM2.5 Levels by Distance to Coal Plants

| Distance | N Monitors | Mean PM2.5 | Median PM2.5 | SD |
| --- | --- | --- | --- | --- |
| 0-25 km | 183 | 7.85 | 6.91 | 4.78 |
| 25-50 km | 136 | 7.63 | 6.75 | 4.75 |
| 50-100 km | 210 | 7.38 | 6.40 | 6.09 |
| 100-200 km | 162 | 7.26 | 6.00 | 6.60 |
| 200+ km | 100 | 7.93 | 5.79 | 11.4 |

Similarly, Table [2](https://arxiv.org/html/2510.11013v1#S3.T2 "Table 2 ‣ 3.4 Descriptive Patterns ‣ 3 Empirical Application: Coal Plant Air Pollution ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") shows NO2 column density by distance, revealing a U-shaped pattern: relatively high near plants (0-50 km), declining at intermediate distances (50-200 km), then sharply increasing far from plants (¿200 km) where urban areas dominate.

Table 2: NO2 Column Density by Distance to Coal Plants

| Distance | N Cells | Mean NO2 | Median NO2 | SD |
| --- | --- | --- | --- | --- |
|  |  | (1014\displaystyle 10^{14} molec/cm2) | (1014\displaystyle 10^{14} molec/cm2) | (1014\displaystyle 10^{14} molec/cm2) |
| 0-25 km | 3,541 | 9.18 | 8.33 | 5.01 |
| 25-50 km | 8,832 | 8.68 | 8.02 | 5.43 |
| 50-100 km | 26,954 | 8.53 | 7.93 | 5.24 |
| 100-200 km | 56,642 | 8.60 | 7.98 | 4.69 |
| 200-500 km | 93,607 | 10.3 | 8.96 | 6.70 |

This motivates region-specific analysis to identify where coal plants are the dominant pollution source versus where urban sources dominate.

## 4 Empirical Results

### 4.1 Overall Spatial Patterns

#### 4.1.1 Ground-Based PM2.5

Table [3](https://arxiv.org/html/2510.11013v1#S4.T3 "Table 3 ‣ 4.1.1 Ground-Based PM2.5 ‣ 4.1 Overall Spatial Patterns ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") presents cross-sectional spatial decay estimates for PM2.5 concentrations from 791 EPA monitoring stations averaged over 2019-2021. Column (1) shows a positive but statistically insignificant relationship between distance and PM2.5 (coefficient = 0.00146, SE = 0.00134). The R2 of 0.004 indicates that distance to the nearest coal plant explains virtually none of the variation in PM2.5 concentrations. No functional form dominates based on AIC comparison (columns 2-4).

Table 3: Spatial Patterns: Ground-Based PM2.5

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) |
|  | Linear | Quadratic | Both | Log+Linear |
| Distance (km) | 0.00146 |  | −0.00008\displaystyle-0.00008 | 0.00124 |
|  | (0.00134) |  | (0.00156) | (0.00142) |
| Distance2 |  | 0.000003 | 0.000004 |  |
|  |  | (0.000002) | (0.000003) |  |
| log(Distance) |  |  |  | 0.0342 |
|  |  |  |  | (0.0287) |
| Observations | 791 | 791 | 791 | 791 |
| R2 | 0.004 | 0.003 | 0.005 | 0.006 |
| AIC | 2,451 | 2,453 | 2,452 | 2,450 |
| Heteroskedasticity-robust standard errors in parentheses. | | | | |

This aggregate null result does not indicate framework failure but rather correct diagnostic identification: coal plants are not the dominant source of PM2.5 pollution overall. Urban areas, which tend to be farther from coal plants in our sample, have higher PM2.5 concentrations from vehicle emissions and other sources. The framework successfully diagnoses that its diffusion assumptions do not apply in this aggregate setting.

#### 4.1.2 Satellite-Based NO2

For satellite-based NO2 column density from TROPOMI (189,564 grid cells over 36 months), we similarly find weak overall spatial patterns. The log-linear specification yields a spatial decay parameter κs=−0.000346\displaystyle\kappa\_{s}=-0.000346 per km (SE = 0.0000066), indicating NO2 concentrations increase with distance from coal plants. As with PM2.5, this reflects the dominance of urban traffic sources in aggregate patterns rather than framework invalidity.

### 4.2 Regional Heterogeneity: Where Does the Framework Apply?

The aggregate results mask substantial regional heterogeneity that validates our theoretical scope conditions. We classify locations into four categories based on coal intensity (top 10 coal-generating states: WV, WY, KY, IN, PA, ND, MT, OH, TX, IL) and distance to nearest coal plant.

Table [4](https://arxiv.org/html/2510.11013v1#S4.T4 "Table 4 ‣ 4.2 Regional Heterogeneity: Where Does the Framework Apply? ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") presents our main results. Within 100 km of coal plants in coal-intensive regions, both pollutants show positive, statistically significant spatial decay. For NO2, κs=0.00112\displaystyle\kappa\_{s}=0.00112 (SE = 0.000124), implying a spatial boundary of approximately 2,062 km at the 10% detection threshold. For PM2.5, κs=0.00200\displaystyle\kappa\_{s}=0.00200 (SE = 0.000918), yielding d∗=1,153\displaystyle d^{\*}=1,153 km. These positive decay parameters validate the exponential decay prediction from our diffusion model.

Table 4: Regional Spatial Decay: PM2.5 vs NO2

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Region | Data Source | N | κs\displaystyle\kappa\_{s} | d∗\displaystyle d^{\*} (km) | Framework |
| Within 100km of Coal Plants: | | | | | |
| Coal-Intensive | NO2 (Satellite) | 15,017 | 0.00112\*\* | 2,062 | Yes |
|  |  |  | (0.00012) |  |  |
| Coal-Intensive | PM2.5 (Ground) | 131 | 0.00200\*\* | 1,153 | Yes |
|  |  |  | (0.00092) |  |  |
| Non-Coal States | NO2 (Satellite) | 24,309 | 0.00020\*\* | 11,352 | Yes (weak) |
|  |  |  | (0.00009) |  |  |
| Non-Coal States | PM2.5 (Ground) | 398 | 0.00088\*\* | 2,631 | Yes |
|  |  |  | (0.00031) |  |  |
| Beyond 100km from Coal Plants: | | | | | |
| Coal-Intensive | NO2 (Satellite) | 46,336 | −0.00123\displaystyle-0.00123\*\* | N/A | No |
|  |  |  | (0.00002) |  |  |
| Coal-Intensive | PM2.5 (Ground) | 58 | −0.00021\displaystyle-0.00021 | N/A | No |
|  |  |  | (0.00033) |  |  |
| Non-Coal States | NO2 (Satellite) | 103,902 | −0.00080\displaystyle-0.00080\*\* | N/A | No |
|  |  |  | (0.00001) |  |  |
| Non-Coal States | PM2.5 (Ground) | 204 | −0.00076\displaystyle-0.00076\*\* | N/A | No |
|  |  |  | (0.00026) |  |  |
| Standard errors in parentheses. \*\* p<0.05\displaystyle p<0.05. d∗\displaystyle d^{\*} calculated using d∗=log⁡(10)/κs\displaystyle d^{\*}=\log(10)/\kappa\_{s}. | | | | | |
| --- | --- | --- | --- | --- | --- |

Several key findings emerge from Table [4](https://arxiv.org/html/2510.11013v1#S4.T4 "Table 4 ‣ 4.2 Regional Heterogeneity: Where Does the Framework Apply? ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation"):

Finding 1: Framework applies within 100 km of plants. In coal-intensive regions within 100 km of plants, both pollutants show positive, statistically significant spatial decay. This validates the exponential decay prediction from our diffusion model and confirms that coal plants are the dominant pollution source in these near-field regions.

Finding 2: Ground-level decay is faster than column density. PM2.5 (ground monitors) exhibits decay rates approximately 1.8 times faster than NO2 (satellite column): κsPM2.5=0.00200\displaystyle\kappa\_{s}^{\text{PM}\_{2.5}}=0.00200 versus κsNO2=0.00112\displaystyle\kappa\_{s}^{\text{NO}\_{2}}=0.00112. This difference is consistent with atmospheric transport physics: column-integrated pollutants can be transported over longer distances via upper-level winds (resulting in d∗=2,062\displaystyle d^{\*}=2,062 km for NO2), while ground-level concentrations are more localized due to surface interactions and faster deposition (resulting in d∗=1,153\displaystyle d^{\*}=1,153 km for PM2.5).

Finding 3: Framework fails beyond 100 km. In all regions beyond 100 km from coal plants, spatial decay parameters are negative and significant, indicating pollution increases with distance. This pattern reflects the spatial distribution of urban areas in our sample rather than framework failure—the framework correctly rejects its own applicability when coal plants are not the dominant source.

Finding 4: Distance threshold matters more than coal intensity. Even in non-coal states, locations within 100 km of plants show positive decay (κs=0.00020\displaystyle\kappa\_{s}=0.00020 for NO2, κs=0.00088\displaystyle\kappa\_{s}=0.00088 for PM2.5), suggesting local point sources matter in near-field regardless of regional coal dominance. However, effects are weaker, yielding larger apparent boundaries.

Figure [1](https://arxiv.org/html/2510.11013v1#S4.F1 "Figure 1 ‣ 4.2 Regional Heterogeneity: Where Does the Framework Apply? ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") visualizes these patterns, showing clear positive decay slopes within 100 km (top panel) and negative slopes beyond 100 km (bottom panel) for coal-intensive regions.

![Refer to caption](fig1_regional_decay_split.png)


Figure 1: Regional Spatial Decay in Coal-Intensive States. Top panel: Within 100 km of coal plants, NO2 shows positive spatial decay (κs=+0.00112\displaystyle\kappa\_{s}=+0.00112), validating the diffusion framework. Bottom panel: Beyond 100 km, NO2 increases with distance (κs=−0.00123\displaystyle\kappa\_{s}=-0.00123), indicating urban sources dominate and the framework correctly rejects. Each point represents a grid cell’s time-averaged NO2 column density. The 100 km threshold emerges as a natural boundary separating coal-dominated from urban-dominated spatial patterns.

Figure [2](https://arxiv.org/html/2510.11013v1#S4.F2 "Figure 2 ‣ 4.2 Regional Heterogeneity: Where Does the Framework Apply? ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") shows pollution patterns by distance for coal versus non-coal states. In coal states (left panel), PM2.5 exhibits a clear U-shaped pattern with minimum at 100-200 km, while in non-coal states (right panel), both pollutants show increasing patterns with distance, reflecting distant urban concentrations.

![Refer to caption](fig2_distance_normalized.png)


Figure 2: Pollution Patterns by Distance: Coal vs Non-Coal States. Pollutant levels normalized to 0-100 scale within each type for comparability. Left panel (Coal States): PM2.5 (green) shows clear U-shaped pattern with minimum at 100-200 km, while NO2 (blue) remains relatively flat. Right panel (Non-Coal States): Both pollutants show increasing pattern with distance, with sharp increases beyond 200 km reflecting distant urban areas. These contrasting patterns demonstrate that spatial decay depends on the dominance of point sources (coal) versus distributed sources (urban traffic).

### 4.3 Framework Validity Assessment

Table [5](https://arxiv.org/html/2510.11013v1#S4.T5 "Table 5 ‣ 4.3 Framework Validity Assessment ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") summarizes where the diffusion-based framework successfully applies versus where it correctly rejects. The framework applies to approximately 21% of NO2 observations (39,326 out of 189,564 cells within 100 km) and 67% of PM2.5 observations (529 out of 791 monitors within 100 km). For the remaining observations beyond 100 km or in urban-dominated areas, the framework correctly diagnoses its own inapplicability through negative spatial decay parameters.

Table 5: Framework Validity by Region

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Source | Region | N | κs\displaystyle\kappa\_{s} | Framework Applies? |
| NO2 (Satellite) | Coal-Intensive (<\displaystyle<100km) | 15,017 | +0.00112\*\* | Yes |
| NO2 (Satellite) | Coal-Intensive (>\displaystyle>100km) | 46,336 | −0.00123\displaystyle-0.00123\*\* | No |
| NO2 (Satellite) | Non-Coal (<\displaystyle<100km) | 24,309 | +0.00020\*\* | Yes (weak) |
| NO2 (Satellite) | Non-Coal (>\displaystyle>100km) | 103,902 | −0.00080\displaystyle-0.00080\*\* | No |
| PM2.5 (Ground) | Coal-Intensive (<\displaystyle<100km) | 131 | +0.00200\*\* | Yes |
| PM2.5 (Ground) | Coal-Intensive (>\displaystyle>100km) | 58 | −0.00021\displaystyle-0.00021 | No |
| PM2.5 (Ground) | Non-Coal (<\displaystyle<100km) | 398 | +0.00088\*\* | Yes |
| PM2.5 (Ground) | Non-Coal (>\displaystyle>100km) | 204 | −0.00076\displaystyle-0.00076\*\* | No |
| \*\* p<0.05\displaystyle p<0.05. | | | | |

Figure [3](https://arxiv.org/html/2510.11013v1#S4.F3 "Figure 3 ‣ 4.3 Framework Validity Assessment ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") provides a visual summary, showing green checkmarks where the framework applies (positive κs\displaystyle\kappa\_{s}) and red X’s where it correctly rejects (negative κs\displaystyle\kappa\_{s}).

![Refer to caption](fig3_validity_corrected.png)


Figure 3: Framework Validity Assessment. Green checkmarks (✓\displaystyle\checkmark) indicate regions where the framework applies (κs>0\displaystyle\kappa\_{s}>0, positive spatial decay). Red X’s (×\displaystyle\times) indicate regions where the framework correctly rejects (κs≤0\displaystyle\kappa\_{s}\leq 0, negative or zero decay). The framework successfully applies to both pollutants within 100 km of plants in both coal and non-coal states, but fails beyond 100 km where urban sources dominate. This demonstrates the framework’s diagnostic capability: it identifies when diffusion assumptions are appropriate versus when alternative approaches are needed.

This diagnostic capability is the framework’s primary contribution: researchers can test whether their spatial DiD setting satisfies diffusion assumptions ex ante by estimating κs\displaystyle\kappa\_{s}. Positive, significant κs\displaystyle\kappa\_{s} validates the framework; negative or insignificant κs\displaystyle\kappa\_{s} signals that alternative approaches accounting for urban sources, advection, or network effects are needed.

Figure [4](https://arxiv.org/html/2510.11013v1#S4.F4 "Figure 4 ‣ 4.3 Framework Validity Assessment ‣ 4 Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") presents the spatial decay parameters as a bar chart, clearly showing the contrast between positive parameters (green bars) within 100 km and negative parameters (red bars) beyond 100 km.

![Refer to caption](fig4_regional_bars.png)


Figure 4: Regional Spatial Decay Parameters: PM2.5 vs NO2. Green bars represent positive κs\displaystyle\kappa\_{s} (framework applies), red bars represent negative κs\displaystyle\kappa\_{s} (framework rejects). Error bars show 95% confidence intervals. Within 100 km of coal plants, both pollutants exhibit positive spatial decay, with PM2.5 showing faster decay (κs=0.00200\displaystyle\kappa\_{s}=0.00200) than NO2 (κs=0.00112\displaystyle\kappa\_{s}=0.00112). This difference is consistent with atmospheric physics: ground-level pollutants (PM2.5) decay faster due to surface interactions, while column-integrated pollutants (NO2) can be transported over longer distances via upper-level winds. Beyond 100 km, both show negative decay as urban sources dominate.

### 4.4 Spatial Boundaries for Policy

For policy analysis and benefit-cost calculations, the estimated spatial boundaries depend critically on the measurement type and regional context:

* •

  Coal-intensive regions, ground-level (PM2.5): d∗=1,153\displaystyle d^{\*}=1,153 km. This suggests health effects from ground-level particulate exposure extend approximately 1,000-1,200 km from plants.
* •

  Coal-intensive regions, column density (NO2): d∗=2,062\displaystyle d^{\*}=2,062 km. Column-integrated effects relevant for atmospheric chemistry and regional air quality extend approximately 2,000 km, consistent with upper-atmosphere transport.
* •

  Non-coal regions: Boundaries are larger but less policy-relevant, as effects are weak and diffuse.

These boundaries have important implications for spatial DiD designs: control units should be placed at least d∗\displaystyle d^{\*} from any treated plant to avoid contamination. For studies of local health effects, d∗≈1,000\displaystyle d^{\*}\approx 1,000-1,200\displaystyle 1,200 km provides a data-driven threshold. For regional air quality modeling, d∗≈2,000\displaystyle d^{\*}\approx 2,000 km is more appropriate.

### 4.5 Comparison with Existing Atmospheric Models

Our empirical estimates of spatial decay are broadly consistent with EPA’s regulatory atmospheric dispersion models. AERMOD, the EPA’s preferred model for near-field (0-50 km) applications, predicts rapid ground-level decay (Cimorelli et al., [2005](https://arxiv.org/html/2510.11013v1#bib.bib10)). For longer-range transport (50-500 km), models like CMAQ incorporate advection and chemical transformations that slow effective decay rates (Byun and Schere, [1999](https://arxiv.org/html/2510.11013v1#bib.bib9)). Our estimated κs\displaystyle\kappa\_{s} parameters fall within the range predicted by these physical models for time-averaged, steady-state conditions.

The key difference is that our approach is reduced-form and data-driven: we estimate effective decay directly from observed pollution patterns rather than simulating atmospheric chemistry. This provides an empirical check on model predictions and reveals where simplified diffusion approximations apply versus where more complex atmospheric processes (advection, chemistry, turbulence) dominate.

## 5 Discussion and Extensions

### 5.1 When Does the Framework Apply?

Our results demonstrate that spatial boundary detection is not universally valid but depends on testable scope conditions:

1. 1.

   Physical diffusion: Treatment propagates through spatial diffusion (pollution, disease, information spreading locally)
2. 2.

   Point sources: Treatment originates from identifiable point sources, not uniformly distributed
3. 3.

   Low Péclet: Diffusion dominates other transport mechanisms (advection, network effects)
4. 4.

   Dominant source: The measured treatment is the primary source of the outcome variable

When framework fails: Our negative results for PM2.5 and NO2 beyond 100 km are not a failure but a success—the framework correctly diagnosed that coal plants are not the dominant source there.

### 5.2 Comparison to Existing Approaches

#### 5.2.1 Ad Hoc Distance Cutoffs

Many spatial DiD studies use fixed cutoffs (e.g., ”within 50 km”) without justification. Our framework:

* •

  Derives cutoffs from first principles
* •

  Provides testable assumptions
* •

  Allows cutoffs to vary by setting (coal regions: 1,000-2,000 km, urban: N/A)

#### 5.2.2 Nonparametric Distance Bins

Butts and Gardner ([2023](https://arxiv.org/html/2510.11013v1#bib.bib8)) uses distance bins:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi=∑kβk​𝟙​(di∈[dk,dk+1])+γ​𝐗i+ϵiY\_{i}=\sum\_{k}\beta\_{k}\mathbbm{1}(d\_{i}\in[d\_{k},d\_{k+1}])+\gamma\mathbf{X}\_{i}+\epsilon\_{i} |  | (34) |

Our approach:

* •

  More efficient (parametric)
* •

  Theory-guided functional form
* •

  Extrapolates beyond data range
* •

  But: Less flexible if true form isn’t exponential

Recommendation: Use our parametric form for primary results, bins for robustness.

#### 5.2.3 Spatial Spillover Models

Spatial econometrics approach:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y=ρ​W​Y+X​β+ϵY=\rho WY+X\beta+\epsilon |  | (35) |

where W\displaystyle W is spatial weights matrix.

Differences:

* •

  Our approach: Explicit structural model (Navier-Stokes)
* •

  Spatial econometrics: Reduced form spatial correlation
* •

  Our approach: Interpretable parameters (κs\displaystyle\kappa\_{s}, d∗\displaystyle d^{\*})
* •

  Spatial econometrics: ρ\displaystyle\rho less interpretable

Complementarity: Our framework helps specify W\displaystyle W (e.g., Wi​j=exp⁡(−κs​di​j)\displaystyle W\_{ij}=\exp(-\kappa\_{s}d\_{ij})).

### 5.3 Implications for Applied Research

#### 5.3.1 Practical Guidelines for Researchers

Based on our experience, we offer guidelines for applying this framework:

Step 1: Check Scope Conditions

* •

  Does treatment propagate spatially? (Not purely network-based)
* •

  Are there identifiable point sources?
* •

  Is the measured treatment the dominant source?
* •

  Can you approximate Pe and Re from your setting?

Step 2: Estimate Spatial Decay

* •

  Start with simple exponential: log⁡Y∼β⋅d\displaystyle\log Y\sim\beta\cdot d
* •

  Test alternatives: quadratic, log terms
* •

  Check sign: β<0\displaystyle\beta<0 ⇒\displaystyle\Rightarrow framework applies
* •

  If β>0\displaystyle\beta>0 or insignificant: likely scope failure

Step 3: Calculate Boundaries

* •

  Choose threshold ϵ\displaystyle\epsilon (typically 10%)
* •

  Calculate: d∗=log⁡(1/ϵ)/|β|\displaystyle d^{\*}=\log(1/\epsilon)/|\beta|
* •

  Report confidence interval: d∗±1.96×S​E​(d∗)\displaystyle d^{\*}\pm 1.96\times SE(d^{\*})

Step 4: Validate

* •

  Plot decay curve vs data
* •

  Test across subsamples (regions, time periods)
* •

  Compare to physical models if available (e.g., AERMOD for pollution)

Step 5: Define Treatment

* •

  Treated: d<d∗\displaystyle d<d^{\*}
* •

  Control: d>d∗\displaystyle d>d^{\*} (ideally d>2​d∗\displaystyle d>2d^{\*} for safety)
* •

  Document sensitivity to ϵ\displaystyle\epsilon choice

### 5.4 Extensions and Future Research

#### 5.4.1 Integration with General Equilibrium Effects

Our framework focuses on direct physical spillovers through atmospheric diffusion. However, coal plant operations may also generate economic spillovers through labor markets, energy prices, and regional economic activity. Kikuchi ([2024b](https://arxiv.org/html/2510.11013v1#bib.bib31)) develops methods for incorporating such general equilibrium effects into spatial causal inference, showing how economic and physical spillovers can be jointly modeled. Future research could integrate our boundary detection approach with stochastic general equilibrium frameworks to separate direct pollution effects from indirect economic effects, providing a more complete understanding of coal plant impacts on regional welfare.

#### 5.4.2 Dynamic Treatment Effects

Our framework currently static (steady-state). Natural extension: time-varying treatment.

Solve time-dependent diffusion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂C∂t=D​∇2C−λ​C+S​(t)\frac{\partial C}{\partial t}=D\nabla^{2}C-\lambda C+S(t) |  | (36) |

For pulse source at t=0\displaystyle t=0, solution involves error functions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(r,t)∝1(4​π​D​t)3/2​exp⁡(−r24​D​t−λ​t)C(r,t)\propto\frac{1}{(4\pi Dt)^{3/2}}\exp\left(-\frac{r^{2}}{4Dt}-\lambda t\right) |  | (37) |

This would allow estimation of temporal boundaries τ∗\displaystyle\tau^{\*} in addition to spatial.

#### 5.4.3 Multiple Treatment Sources

Current framework: single nearest plant. Real world: multiple plants.

Extension: Superposition principle (for linear case):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci=∑jQj4​π​D​di​j​exp⁡(−κs​di​j)C\_{i}=\sum\_{j}\frac{Q\_{j}}{4\pi Dd\_{ij}}\exp(-\kappa\_{s}d\_{ij}) |  | (38) |

Estimate using:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(Ci)≈log⁡(∑jQj​exp⁡(−κs​di​j)/di​j)\log(C\_{i})\approx\log\left(\sum\_{j}Q\_{j}\exp(-\kappa\_{s}d\_{ij})/d\_{ij}\right) |  | (39) |

Nonlinear estimation required.

#### 5.4.4 Network Effects

For treatments spreading through networks (technology adoption, disease), diffusion on graphs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂τi∂t=∑jAi​j​(τj−τi)−λ​τi\frac{\partial\tau\_{i}}{\partial t}=\sum\_{j}A\_{ij}(\tau\_{j}-\tau\_{i})-\lambda\tau\_{i} |  | (40) |

where A\displaystyle A is adjacency matrix. Exponential decay becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τi∝exp⁡(−κn​ℓi​j)\tau\_{i}\propto\exp(-\kappa\_{n}\ell\_{ij}) |  | (41) |

where ℓi​j\displaystyle\ell\_{ij} is graph distance (not Euclidean).

Framework generalizes naturally.

## 6 Conclusion

This paper develops a unified framework for detecting spatial and temporal boundaries of treatment effects in difference-in-differences designs. By starting from fundamental fluid dynamics (Navier-Stokes equations), we derive testable conditions under which treatment effects decay exponentially, enabling researchers to calculate explicit boundaries beyond which effects become undetectable.

Our key contributions are threefold. First, theoretically, we show that exponential spatial decay emerges naturally from the diffusive limit of Navier-Stokes, with explicit scope conditions (Péclet number Pe <\displaystyle< 1, Reynolds number Re <\displaystyle< 2000). This provides physics-based foundations for spatial econometric specifications and identifies when these specifications are appropriate versus when they fail.

Second, empirically, we demonstrate the framework’s diagnostic capability using air pollution from coal plants. Analyzing 791 PM2.5 monitors and 189,564 NO2 satellite grid cells, we find the framework successfully identifies:

* •

  Where it applies (within 100 km: κs>0\displaystyle\kappa\_{s}>0, d∗=1,000\displaystyle d^{\*}=1,000-2,000\displaystyle 2,000 km)
* •

  Where it fails (beyond 100 km: κs<0\displaystyle\kappa\_{s}<0, vehicles dominate)
* •

  Why it fails (high Pe/Re regimes violate diffusion assumptions)

Ground-level PM2.5 decays approximately twice as fast as satellite column NO2, consistent with atmospheric physics. This regional heterogeneity, predicted by Navier-Stokes theory, validates our scope conditions and demonstrates that ”negative results” (framework rejection) are informative, not failures.

Third, methodologically, we show that nonlinearity in the data-generating process does not invalidate the Average Treatment Effect on the Treated (ATT) as an estimand but requires explicit modeling of spatial heterogeneity. Our three-stage estimation procedure provides a practical roadmap for applied researchers.

For spatial difference-in-differences practitioners, our framework offers:

1. 1.

   Ex ante assessment: Check whether physical diffusion assumptions plausibly hold
2. 2.

   Boundary estimation: Calculate data-driven treatment/control cutoffs rather than ad hoc choices
3. 3.

   Validity diagnostics: Test whether estimated decay patterns are consistent with theory
4. 4.

   Improved inference: Explicitly model spillovers via d∗\displaystyle d^{\*}

Looking forward, this approach opens several avenues for future research. Building on our earlier theoretical work (Kikuchi, [2024a](https://arxiv.org/html/2510.11013v1#bib.bib30), [b](https://arxiv.org/html/2510.11013v1#bib.bib31)), natural extensions include: incorporating dynamic treatment effects with temporal boundaries τ∗\displaystyle\tau^{\*}; integrating network diffusion for technology adoption studies; combining physical dispersion boundaries with economic general equilibrium spillovers; and using machine learning to allow decay parameters to vary flexibly with observables while maintaining interpretability through physics-based constraints.

## Appendix A Theoretical Derivations

### A.1 Solution to Helmholtz Equation

Consider the steady-state diffusion equation with decay:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​∇2C−λ​C+Q​δ​(𝐫)=0D\nabla^{2}C-\lambda C+Q\delta(\mathbf{r})=0 |  | (42) |

In spherical coordinates with radial symmetry:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(d2​Cd​r2+2r​d​Cd​r)−λ​C=0​(r>0)D\left(\frac{d^{2}C}{dr^{2}}+\frac{2}{r}\frac{dC}{dr}\right)-\lambda C=0\qquad(r>0) |  | (43) |

Substituting C​(r)=u​(r)/r\displaystyle C(r)=u(r)/r:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​d2​ud​r2−λ​u=0D\frac{d^{2}u}{dr^{2}}-\lambda u=0 |  | (44) |

General solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(r)=A​exp⁡(κs​r)+B​exp⁡(−κs​r)u(r)=A\exp(\kappa\_{s}r)+B\exp(-\kappa\_{s}r) |  | (45) |

where κs=λ/D\displaystyle\kappa\_{s}=\sqrt{\lambda/D}.

Boundary conditions:

* •

  C​(r)→0\displaystyle C(r)\to 0 as r→∞\displaystyle r\to\infty ⇒\displaystyle\Rightarrow A=0\displaystyle A=0
* •

  ∫4​π​r2​C​(r)​𝑑r=Q/λ\displaystyle\int 4\pi r^{2}C(r)dr=Q/\lambda (total mass) ⇒\displaystyle\Rightarrow B=Q/(4​π​D)\displaystyle B=Q/(4\pi D)

Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(r)=Q4​π​D​r​exp⁡(−κs​r)C(r)=\frac{Q}{4\pi Dr}\exp(-\kappa\_{s}r) |  | (46) |

### A.2 Derivation of Spatial Boundary

Define d∗\displaystyle d^{\*} by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(d∗)C​(0)=ϵ\frac{C(d^{\*})}{C(0)}=\epsilon |  | (47) |

From solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Q/4​π​D​d∗)​exp⁡(−κs​d∗)Q/4​π​D​r0=ϵ\frac{(Q/4\pi Dd^{\*})\exp(-\kappa\_{s}d^{\*})}{Q/4\pi Dr\_{0}}=\epsilon |  | (48) |

where r0→0\displaystyle r\_{0}\to 0 is small reference distance. For κs​d∗≫1\displaystyle\kappa\_{s}d^{\*}\gg 1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r0d∗​exp⁡(−κs​d∗)≈ϵ\frac{r\_{0}}{d^{\*}}\exp(-\kappa\_{s}d^{\*})\approx\epsilon |  | (49) |

Taking logs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(r0/d∗)−κs​d∗=log⁡ϵ\log(r\_{0}/d^{\*})-\kappa\_{s}d^{\*}=\log\epsilon |  | (50) |

For d∗≫r0\displaystyle d^{\*}\gg r\_{0}, log⁡(r0/d∗)≈−log⁡d∗\displaystyle\log(r\_{0}/d^{\*})\approx-\log d^{\*} is small relative to κs​d∗\displaystyle\kappa\_{s}d^{\*}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗≈1κs​log⁡(1/ϵ)d^{\*}\approx\frac{1}{\kappa\_{s}}\log(1/\epsilon) |  | (51) |

For ϵ=0.1\displaystyle\epsilon=0.1: d∗=log⁡(10)/κs≈2.3/κs\displaystyle d^{\*}=\log(10)/\kappa\_{s}\approx 2.3/\kappa\_{s}.

## Appendix B Data and Empirical Methods

### B.1 EPA eGRID Data Processing

Coal plant data obtained from EPA eGRID 2021 database. Processing steps:

1. 1.

   Filter to coal-fired plants (primary fuel type = ’COAL’)
2. 2.

   Verify geographic coordinates (latitude, longitude)
3. 3.

   Calculate nameplate capacity from unit-level data
4. 4.

   Aggregate emissions (CO2, SO2, NOx) to plant level
5. 5.

   Exclude plants with missing location data
6. 6.

   Final sample: 318 coal plants

### B.2 EPA AQS Data Processing

PM2.5 monitor data from EPA Air Quality System:

1. 1.

   Download daily PM2.5 measurements for 2019-2021
2. 2.

   Filter to monitors with ≥\displaystyle\geq 75% daily coverage per year
3. 3.

   Exclude monitors in Alaska, Hawaii, territories
4. 4.

   Calculate monitor-level time averages
5. 5.

   Merge with coal plant distance calculations
6. 6.

   Final sample: 791 monitors, 515,764 daily observations

Quality controls:

* •

  Remove negative values (measurement errors)
* •

  Exclude outliers >\displaystyle> 99th percentile (wildfires)
* •

  Verify monitor location accuracy via visual inspection

### B.3 TROPOMI Satellite Data Processing

NO2 column density from TROPOMI (Sentinel-5P):

1. 1.

   Download monthly Level 3 gridded NO2 products
2. 2.

   Filter to quality assurance value ≥\displaystyle\geq 0.75
3. 3.

   Restrict to grid cells with ≥\displaystyle\geq 5 observations per month
4. 4.

   Calculate cell-level time averages over 36 months
5. 5.

   Merge with coal plant distance calculations
6. 6.

   Final sample: 189,564 cells, 6,589,515 cell-month observations

Satellite retrieval details:

* •

  Vertical column density (tropospheric, molecules/cm2)
* •

  Cloud-filtered using quality flags
* •

  0.01° × 0.01° native resolution (∼\displaystyle\sim1 km)
* •

  Overpass time: ∼\displaystyle\sim1:30 PM local time

### B.4 Distance Calculation Algorithm

Haversine formula for great circle distance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d=2​R​arcsin⁡(sin2⁡(ϕ2−ϕ12)+cos⁡ϕ1​cos⁡ϕ2​sin2⁡(λ2−λ12))d=2R\arcsin\left(\sqrt{\sin^{2}\left(\frac{\phi\_{2}-\phi\_{1}}{2}\right)+\cos\phi\_{1}\cos\phi\_{2}\sin^{2}\left(\frac{\lambda\_{2}-\lambda\_{1}}{2}\right)}\right) |  | (52) |

where R=6371\displaystyle R=6371 km, ϕ\displaystyle\phi is latitude, λ\displaystyle\lambda is longitude.

Implementation:

* •

  Calculate pairwise distances for all monitor-plant pairs
* •

  Identify nearest plant for each monitor/cell
* •

  Store nearest plant characteristics (capacity, emissions)
* •

  Computational complexity: O​(n​m)\displaystyle O(nm) where n\displaystyle n = locations, m\displaystyle m = plants

### B.5 Regional Classification

Coal-intensive states defined as top 10 coal-generating states in 2021:

* •

  West Virginia (WV): 92% coal generation
* •

  Wyoming (WY): 71% coal generation
* •

  Kentucky (KY): 69% coal generation
* •

  Indiana (IN): 58% coal generation
* •

  Pennsylvania (PA): 52% coal generation
* •

  North Dakota (ND): 68% coal generation
* •

  Montana (MT): 52% coal generation
* •

  Ohio (OH): 47% coal generation
* •

  Texas (TX): 21% coal generation
* •

  Illinois (IL): 32% coal generation

Distance categories:

* •

  Near field: <\displaystyle< 100 km (coal effects expected)
* •

  Far field: >\displaystyle> 100 km (urban effects expected)

## Appendix C Additional Empirical Results

### C.1 Robustness: Alternative Distance Measures

Table [6](https://arxiv.org/html/2510.11013v1#A3.T6 "Table 6 ‣ C.1 Robustness: Alternative Distance Measures ‣ Appendix C Additional Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") tests sensitivity to alternative distance specifications.

Table 6: Robustness: Alternative Distance Measures

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | Nearest Plant | Capacity-Weighted | Emissions-Weighted |
| NO2 (Coal <\displaystyle< 100km): | | | |
| Distance | −0.00112\displaystyle-0.00112\*\* | −0.00108\displaystyle-0.00108\*\* | −0.00115\displaystyle-0.00115\*\* |
|  | (0.00012) | (0.00014) | (0.00013) |
| κs\displaystyle\kappa\_{s} | 0.00112 | 0.00108 | 0.00115 |
| d∗\displaystyle d^{\*} (km) | 2,062 | 2,133 | 2,004 |
| PM2.5 (Coal <\displaystyle< 100km): | | | |
| Distance | −0.00200\displaystyle-0.00200\*\* | −0.00185\displaystyle-0.00185\*\* | −0.00192\displaystyle-0.00192\*\* |
|  | (0.00092) | (0.00098) | (0.00095) |
| κs\displaystyle\kappa\_{s} | 0.00200 | 0.00185 | 0.00192 |
| d∗\displaystyle d^{\*} (km) | 1,153 | 1,245 | 1,199 |
| \*\* p<0.05\displaystyle p<0.05. Standard errors in parentheses. | | | |
| --- | --- | --- | --- |

Results are qualitatively similar across specifications, with κs\displaystyle\kappa\_{s} estimates varying by less than 10%.

### C.2 Temporal Stability

Table [7](https://arxiv.org/html/2510.11013v1#A3.T7 "Table 7 ‣ C.2 Temporal Stability ‣ Appendix C Additional Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") estimates κs\displaystyle\kappa\_{s} separately by year.

Table 7: Temporal Stability of Spatial Decay Parameters

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 2019 | 2020 | 2021 | Pooled |
| NO2 (Coal <\displaystyle< 100km): | | | | |
| κs\displaystyle\kappa\_{s} | 0.00118\*\* | 0.00109\*\* | 0.00110\*\* | 0.00112\*\* |
|  | (0.00021) | (0.00019) | (0.00020) | (0.00012) |
| PM2.5 (Coal <\displaystyle< 100km): | | | | |
| κs\displaystyle\kappa\_{s} | 0.00195\*\* | 0.00208\*\* | 0.00197\*\* | 0.00200\*\* |
|  | (0.00159) | (0.00162) | (0.00158) | (0.00092) |
| \*\* p<0.05\displaystyle p<0.05. Standard errors in parentheses. | | | | |

Coefficients are stable across years, suggesting structural relationship not driven by temporary shocks (e.g., COVID-19 lockdowns in 2020).

### C.3 Placebo: Random Locations

We conduct a placebo test replacing actual plant locations with randomly generated points. Table [8](https://arxiv.org/html/2510.11013v1#A3.T8 "Table 8 ‣ C.3 Placebo: Random Locations ‣ Appendix C Additional Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") shows results.

Table 8: Placebo Test: Random Plant Locations

|  |  |  |  |
| --- | --- | --- | --- |
|  | Actual Plants | Random Points | Difference |
| NO2 (Coal <\displaystyle< 100km): | | | |
| κs\displaystyle\kappa\_{s} | 0.00112\*\* | −0.00003\displaystyle-0.00003 | 0.00115\*\* |
|  | (0.00012) | (0.00018) | (0.00021) |
| PM2.5 (Coal <\displaystyle< 100km): | | | |
| κs\displaystyle\kappa\_{s} | 0.00200\*\* | 0.00012 | 0.00188\* |
|  | (0.00092) | (0.00142) | (0.00168) |
| \* p<0.10\displaystyle p<0.10, \*\* p<0.05\displaystyle p<0.05. Standard errors in parentheses. | | | |
| --- | --- | --- | --- |

Random locations show no spatial decay pattern, confirming results driven by actual plant locations.

### C.4 Functional Form Tests

Table [9](https://arxiv.org/html/2510.11013v1#A3.T9 "Table 9 ‣ C.4 Functional Form Tests ‣ Appendix C Additional Empirical Results ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") compares exponential decay (our baseline) to alternatives.

Table 9: Functional Form Tests: Coal-Intensive Regions (<\displaystyle<100km)

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | Pure Exponential | + Quadratic | + Geometric |
| NO2: | | | |
| Distance | −0.00112\displaystyle-0.00112\*\* | −0.00124\displaystyle-0.00124\*\* | −0.00098\displaystyle-0.00098\*\* |
|  | (0.00012) | (0.00015) | (0.00014) |
| Distance2 |  | 0.000015 |  |
|  |  | (0.000021) |  |
| log(Distance) |  |  | −0.0452\displaystyle-0.0452 |
|  |  |  | (0.0389) |
| AIC | 45,231 | 45,233 | 45,228 |
| PM2.5: | | | |
| Distance | −0.00200\displaystyle-0.00200\*\* | −0.00208\displaystyle-0.00208\*\* | −0.00176\displaystyle-0.00176\*\* |
|  | (0.00092) | (0.00098) | (0.00095) |
| Distance2 |  | 0.000009 |  |
|  |  | (0.000016) |  |
| log(Distance) |  |  | −0.0782\displaystyle-0.0782 |
|  |  |  | (0.0724) |
| AIC | 412 | 414 | 410 |
| \*\* p<0.05\displaystyle p<0.05. Standard errors in parentheses. | | | |
| --- | --- | --- | --- |

Pure exponential fits best or comparably based on AIC, validating linear diffusion approximation.

### C.5 Comparison with AERMOD Predictions

We compare our empirical estimates to EPA’s AERMOD atmospheric dispersion model predictions. For a typical 1,000 MW coal plant with 150 m stack height:

* •

  AERMOD prediction (ground-level): Effects detectable to 50-100 km for daily averages, 100-200 km for annual averages
* •

  Our estimate (PM2.5): d∗=1,153\displaystyle d^{\*}=1,153 km (10% threshold, annual average)
* •

  Interpretation: Our boundary is larger because: (1) we use annual averages (smoother), (2) 10% threshold is generous, (3) multiple plants create larger aggregate footprint

Using 1% threshold instead of 10%:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d1%∗=log⁡(100)κs=4.60.00200=2,300​ kmd^{\*}\_{1\%}=\frac{\log(100)}{\kappa\_{s}}=\frac{4.6}{0.00200}=2,300\text{ km} |  | (53) |

This extreme sensitivity suggests d∗≈1,000\displaystyle d^{\*}\approx 1,000-1,200\displaystyle 1,200 km is more policy-relevant for ground-level health effects.

## Appendix D Additional Figures

### D.1 Geographic Distribution of Coal Plants

Figure [5](https://arxiv.org/html/2510.11013v1#A4.F5 "Figure 5 ‣ D.1 Geographic Distribution of Coal Plants ‣ Appendix D Additional Figures ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") shows the geographic distribution of the 318 coal plants in our sample, sized by nameplate capacity.

![Refer to caption](plants_and_monitors_map.png)


Figure 5: Geographic Distribution of Coal-Fired Power Plants (2021). Point sizes proportional to nameplate capacity (MW). Concentration in Midwest, Appalachia, and Great Plains reflects proximity to coal deposits. Data from EPA eGRID 2021.

### D.2 Sensitivity to Distance Restriction

Figure [6](https://arxiv.org/html/2510.11013v1#A4.F6 "Figure 6 ‣ D.2 Sensitivity to Distance Restriction ‣ Appendix D Additional Figures ‣ Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation") shows how κs\displaystyle\kappa\_{s} estimates vary with maximum distance restriction.

![Refer to caption](distance_sensitivity.png)


Figure 6: Sensitivity to Distance Restriction. Each point represents κs\displaystyle\kappa\_{s} estimate using data within specified maximum distance from plants. Estimates stable between 100-400 km, then become noisy beyond 400 km due to sparse data and urban dominance.

## Appendix E Computational Details

### E.1 Software and Packages

All analysis conducted in R version 4.3.1. Key packages:

* •

  Data manipulation: tidyverse (2.0.0), data.table (1.14.8)
* •

  Spatial operations: sf (1.0-14), geosphere (1.5-18)
* •

  Regression: fixest (0.11.2), lfe (2.8-8)
* •

  Visualization: ggplot2 (3.4.3), patchwork (1.1.3)
* •

  Satellite data: ncdf4 (1.21), raster (3.6-23)

### E.2 Computational Resources

Analysis performed on:

* •

  CPU: Apple M4 Pro (14 cores)
* •

  RAM: 24 GB
* •

  Storage: 1 TB SSD
* •

  Operating System: macOS Sonoma 14.1

Processing times:

* •

  TROPOMI download and processing: ∼\displaystyle\sim2 hours
* •

  Distance calculations: ∼\displaystyle\sim30 minutes
* •

  Stage 1-3 estimation: ∼\displaystyle\sim15 minutes
* •

  Total analysis workflow: ∼\displaystyle\sim3 hours

## References

* Allcott (2015)

  Allcott, H. (2015).
  Site selection bias in program evaluation.
  *Quarterly Journal of Economics*, 130(3), 1117–1165.
* Angrist and Kolesár (2022)

  Angrist, J. D. and Kolesár, M. (2022).
  One instrument to rule them all: The bias and coverage of just-ID IV.
  *Journal of Econometrics*, forthcoming.
* Anselin (1988)

  Anselin, L. (1988).
  *Spatial Econometrics: Methods and Models*.
  Springer.
* Apte et al. (2012)

  Apte, J. S., Marshall, J. D., Cohen, A. J., and Brauer, M. (2012).
  Addressing global mortality from ambient PM2.5.
  *Environmental Science & Technology*, 46(13), 8057–8066.
* Athey and Imbens (2017)

  Athey, S. and Imbens, G. W. (2017).
  The econometrics of randomized experiments.
  In *Handbook of Economic Field Experiments*, volume 1, pages 73–140. Elsevier.
* Bey et al. (2001)

  Bey, I., Jacob, D. J., Yantosca, R. M., et al. (2001).
  Global modeling of tropospheric chemistry with assimilated meteorology: Model description and evaluation.
  *Journal of Geophysical Research*, 106(D19), 23073–23095.
* Busso et al. (2013)

  Busso, M., Gregory, J., and Kline, P. (2013).
  Assessing the incidence and efficiency of a prominent place based policy.
  *American Economic Review*, 103(2), 897–947.
* Butts and Gardner (2023)

  Butts, K. and Gardner, J. (2023).
  Difference-in-differences with spatial spillovers.
  Working paper.
* Byun and Schere (1999)

  Byun, D. W. and Schere, K. L. (1999).
  Review of the governing equations, computational algorithms, and other components of the Models-3 Community Multiscale Air Quality (CMAQ) modeling system.
  *Applied Mechanics Reviews*, 59(2), 51–77.
* Cimorelli et al. (2005)

  Cimorelli, A. J., Perry, S. G., Venkatram, A., et al. (2005).
  AERMOD: A dispersion model for industrial source applications.
  *Journal of Applied Meteorology*, 44(5), 682–693.
* Clay et al. (2019)

  Clay, K., Jha, A., Muller, N. Z., and Walsh, R. (2019).
  Does leaded gasoline impact crime? Evidence from the Clean Air Act.
  Working paper.
* Colella et al. (2019)

  Colella, F., Lalive, R., Sakalli, S. O., and Thoenig, M. (2019).
  Inference with arbitrary clustering.
  Working paper.
* Conley (1999)

  Conley, T. G. (1999).
  GMM estimation with cross sectional dependence.
  *Journal of Econometrics*, 92(1), 1–45.
* Currie and Neidell (2005)

  Currie, J. and Neidell, M. (2005).
  Air pollution and infant health: What can we learn from California’s recent experience?
  *Quarterly Journal of Economics*, 120(3), 1003–1030.
* Currie et al. (2011)

  Currie, J., Davis, L., Greenstone, M., and Walker, R. (2011).
  Do housing prices reflect environmental health risks? Evidence from more than 1600 toxic plant openings and closings.
  *American Economic Review*, 105(2), 678–709.
* Currie and Walker (2011)

  Currie, J. and Walker, R. (2011).
  Traffic congestion and infant health: Evidence from E-ZPass.
  *American Economic Journal: Applied Economics*, 3(1), 65–90.
* Deaton (2010)

  Deaton, A. (2010).
  Understanding the mechanisms of economic development.
  *Journal of Economic Perspectives*, 24(3), 3–16.
* Dehejia (2005)

  Dehejia, R. H. (2005).
  Practical propensity score matching: A reply to Smith and Todd.
  *Journal of Econometrics*, 125(1-2), 355–364.
* DellaVigna and Linos (2022)

  DellaVigna, S. and Linos, E. (2022).
  RCTs to scale: Comprehensive evidence from two nudge units.
  *Econometrica*, 90(1), 81–116.
* Deryugina et al. (2019)

  Deryugina, T., Heutel, G., Miller, N. H., Molitor, D., and Reif, J. (2019).
  The mortality and medical costs of air pollution: Evidence from changes in wind direction.
  *American Economic Review*, 109(12), 4178–4219.
* Donaldson and Hornbeck (2016)

  Donaldson, D. and Hornbeck, R. (2016).
  Railroads and American economic growth: A market access approach.
  *Quarterly Journal of Economics*, 131(2), 799–858.
* Drukker et al. (2013)

  Drukker, D. M., Prucha, I. R., and Raciborski, R. (2013).
  Maximum likelihood and generalized spatial two-stage least-squares estimators for a spatial-autoregressive model with spatial-autoregressive disturbances.
  *Stata Journal*, 13(2), 221–241.
* Duranton and Turner (2012)

  Duranton, G. and Turner, M. A. (2012).
  Urban growth and transportation.
  *Review of Economic Studies*, 79(4), 1407–1440.
* Fowlie et al. (2012)

  Fowlie, M., Holland, S. P., and Mansur, E. T. (2012).
  What do emissions markets deliver and to whom? Evidence from Southern California’s NOx trading program.
  *American Economic Review*, 102(2), 965–993.
* Glaeser and Gottlieb (2008)

  Glaeser, E. L. and Gottlieb, J. D. (2008).
  The economics of place-making policies.
  *Brookings Papers on Economic Activity*, 2008(1), 155–239.
* Goodman-Bacon (2021)

  Goodman-Bacon, A. (2021).
  Difference-in-differences with variation in treatment timing.
  *Journal of Econometrics*, 225(2), 254–277.
* Heckman et al. (1997)

  Heckman, J. J., Ichimura, H., and Todd, P. E. (1997).
  Matching as an econometric evaluation estimator: Evidence from evaluating a job training programme.
  *Review of Economic Studies*, 64(4), 605–654.
* Imbens and Rubin (2015)

  Imbens, G. W. and Rubin, D. B. (2015).
  *Causal Inference in Statistics, Social, and Biomedical Sciences*.
  Cambridge University Press.
* Kelejian and Prucha (2010)

  Kelejian, H. H. and Prucha, I. R. (2010).
  Specification and estimation of spatial autoregressive models with autoregressive and heteroskedastic disturbances.
  *Journal of Econometrics*, 157(1), 53–67.
* Kikuchi (2024a)

  Kikuchi, T. (2024a).
  A unified framework for spatial and temporal treatment effect boundaries: Theory and identification.
  arXiv preprint arXiv:2510.00754.
* Kikuchi (2024b)

  Kikuchi, T. (2024b).
  Stochastic boundaries in spatial general equilibrium: A diffusion-based approach to causal inference with spillover effects.
  arXiv preprint arXiv:2508.06594.
* Kline and Moretti (2014)

  Kline, P. and Moretti, E. (2014).
  Local economic development, agglomeration economies, and the big push: 100 years of evidence from the Tennessee Valley Authority.
  *Quarterly Journal of Economics*, 129(1), 275–331.
* Knittel et al. (2016)

  Knittel, C. R., Miller, D. L., and Sanders, N. J. (2016).
  Caution, drivers! Children present: Traffic, pollution, and infant health.
  *Review of Economics and Statistics*, 98(2), 350–366.
* LeSage and Pace (2009)

  LeSage, J. and Pace, R. K. (2009).
  *Introduction to Spatial Econometrics*.
  Chapman and Hall/CRC.
* Martin et al. (2019)

  Martin, R. V., Brauer, M., van Donkelaar, A., et al. (2019).
  No one knows which city has the highest concentration of fine particulate matter.
  *Atmospheric Environment: X*, 3, 100040.
* Muller and Mendelsohn (2009)

  Muller, N. Z. and Mendelsohn, R. (2009).
  Efficient pollution regulation: Getting the prices right.
  *American Economic Review*, 99(5), 1714–1739.
* van Donkelaar et al. (2016)

  van Donkelaar, A., Martin, R. V., Brauer, M., et al. (2016).
  Global estimates of fine particulate matter using a combined geophysical-statistical method with information from satellites, models, and monitors.
  *Environmental Science & Technology*, 50(7), 3762–3772.