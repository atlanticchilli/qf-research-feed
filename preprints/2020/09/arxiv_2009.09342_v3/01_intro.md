---
authors:
- Andrey Itkin
- Dmitry Muravey
doc_id: arxiv:2009.09342v3
family_id: arxiv:2009.09342
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2009.09342] Semi-analytic pricing of double barrier options with time-dependent
  barriers and rebates at hit'
url_abs: http://arxiv.org/abs/2009.09342v3
url_html: https://ar5iv.org/html/2009.09342v3
venue: arXiv q-fin
version: 3
year: 2020
---


Andrey Itkin
1
and Dmitry Muravey
2
  
  
1
Tandon School of Engineering, New York University, 1 Metro Tech Center, 10th floor, Brooklyn NY 11201, USA
  
2
Moscow State University, Moscow, Russia

* We continue a series of papers devoted to construction of semi-analytic solutions for barrier options. These options are written on underlying following some simple one-factor diffusion model, but all the parameters of the model as well as the barriers are time-dependent. We managed to show that these solutions are systematically more efficient for pricing and calibration than, eg., the corresponding finite-difference solvers. In this paper we extend this technique to pricing double barrier options and present two approaches to solving it: the General Integral transform method and the Heat Potential method. Our results confirm that for double barrier options these semi-analytic techniques are also more efficient than the traditional numerical methods used to solve this type of problems.

## Introduction

Classical problems of financial mathematics recently got new attention due to several factors. Among them one could mention:

* •

  Very small or even negative interest rates observed at the market, and also forced by the Federal Reserve for achieving its macroeconomic goals, see, eg., (Itkin et al., [2020a](#bib.bib16)) and reference therein. Therefore. financial models that allow negative rates recently redrew much attention.
* •

  Negative oil prices due to the COVID-19 pandemic and the following economic recession, see (Bouchouev, [2020](#bib.bib1); Farrington and Cesa, [2020](#bib.bib10)).
* •

  Another consequence of the COVID-19 was a huge shift to electronic trading since major options exchanges temporarily closed their floors, and brokers and market makers were adjusting to working from home. That raised the need for real-time tools for fast calculating the option prices and Greeks, (Brogan, [2020](#bib.bib2)).

Those and some other aspects forced the financial society to critically reassess even simple classical one-factor models of mathematical finance, and reanimate some of them, for instance the Ornstein-Uhlenbeck (OU) process, that traditionally have been referred to as defective/ill-posed or problematic. In (Doff, [2020](#bib.bib9)) it is advocated that risk managers could even use Black-Scholes to help drive strategy. Therefore, nowadays, for instance, fast pricing of barrier options even for those simple models could be of an increasing importance. That is what this paper is devoted to as applied to double barrier options.

In what follows we consider these options written on the underlying which temporal dynamics is driven by a simple one-factor diffusion process but with time-dependent coefficients. Also, both barriers are assumed to be time dependent. Finally, when the underlying process hits any of the barriers, the Call option holder gets a rebate-at-hit (different for the upper and lower barriers), and they are also time-dependent. It is important that in this paper we consider only the underlying dynamics whose option pricing problem by using the Feynman-Kac theorem and also some transformations could be reduced to the heat equation. Nevertheless, to the best of our knowledge, even with this simplification a closed-form solution of this problem is yet unknown.

However, we have to mention (Mijatovic, [2010](#bib.bib27)), where a similar problem was solved by using a probabilistic approach to obtain a decomposition of the barrier option price into the corresponding European option price minus the barrier premium for a wide class of payoff functions, barrier functions and linear diffusions (i.e., the drift is constant and the local volatility is a function of the underlying only). For this setting it is shown in (Mijatovic, [2010](#bib.bib27)) that the barrier premium can be expressed as a sum of integrals along the barriers of the option’s delta at the barriers, and that those deltas solve a system of Volterra integral equations of the second kind. This is similar to the idea of the generalized integral transform (GIT) method that we use in this paper, while our setting is more general. Indeed, we allow any diffusion model with time-dependent coefficients and time-dependent barriers and rebates at hit subject to the condition that the pricing partial differential equation (PDE) can be reduced to the heat equation (or, as shown in (Carr et al., [2020](#bib.bib5)) to the Bessel equation). It can also be checked that the pricing PDE in (Mijatovic, [2010](#bib.bib27)) by a simple change of the spatial variable can be transformed to the heat equation.

Our approach advocated in this paper further extends the technique we elaborated in a series of papers which dealt with a similar problem for single barrier options. In (Carr and Itkin, [2020](#bib.bib4)) we developed semi-analytic solutions for the barrier (perhaps, time-dependent) and American options where the underlying stock is driven by a time-dependent OU process with a lognormal drift. This model is equivalent to the familiar Hull-White model in Fixed Income that was separately considered in (Itkin and Muravey, [2020](#bib.bib15)). In all cases the solution was obtained by using the method of heat potentials (HP) and the GIT method. While the HP method is well-known in mathematical physics and engineering, (Tikhonov and Samarskii, [1963](#bib.bib32); Friedman, [1964.](#bib.bib11); Kartashov, [2001](#bib.bib19)), it is less known as applied to finance. The first use of this method in finance is due to (Lipton, [2002](#bib.bib22)) for pricing path-dependent options with curvilinear barriers, and more recently in (Lipton and Kaushansky, [2018](#bib.bib24); Lipton and de Prado, [2020](#bib.bib23)) (also see references therein).

The GIT method is also known in physics, (Kartashov, [1999](#bib.bib18), [2001](#bib.bib19)), but was unknown in finance until the first use in (Carr and Itkin, [2020](#bib.bib4)). It is important, that it solves the problems where the underlying is defined at the domain S∈[0,y​(t)]𝑆0𝑦𝑡S\in[0,y(t)] with S𝑆S being the stock price, and y​(t)𝑦𝑡y(t) being the time-dependent barrier, however, for other domains the solution was unknown even in physics. Then in (Itkin and Muravey, [2020](#bib.bib15)) the GIT solution for the first time was constructed for the domain S∈[y​(t),∞)𝑆𝑦𝑡S\in[y(t),\infty).

Latter this technique was elaborated also for the CIR and CEV models, (Carr et al., [2020](#bib.bib5)), and the Black-Karasinski model, (Itkin et al., [2020a](#bib.bib16)). In particular, in (Carr et al., [2020](#bib.bib5)) the HP method was further generalized to be capable to solving not just the heat but also the Bessel equations, and was called the Bessel potential (BP) method. In (Itkin et al., [2020a](#bib.bib16)) the PDE is also of a special kind. It is a flavor of the time-dependent Schrödinger equation with the unsteady Morse potential (this can be obtained by the change of variables x→−x→𝑥𝑥x\to-x and τ→−i​τ→𝜏i𝜏\tau\to-\mathrm{i}\mkern 1.0mu\tau, i=−1i1\mathrm{i}\mkern 1.0mu=\sqrt{-1}).

To make it rigorous, in this context a semi-analytic solution means that given a model with the time-dependent drift and volatility functions, and also with the time-dependent barriers, we obtain the barrier option price in the explicit (analytic) form as an integral in the time t𝑡t. However, this integral contains yet unknown function Ψ​(t)Ψ𝑡\Psi(t) which solves some Volterra equation of the second kind which also obtained in our papers. Therefore, we think that "semi-analytic" is an appropriate term. Also, in some situations Ψ​(t)Ψ𝑡\Psi(t) can be found analytically, see eg., (Carr and Itkin, [2020](#bib.bib4); Itkin and Muravey, [2020](#bib.bib15)).

In addition to the explicit analytic representation of the solution, another advantage of this approach is computational speed and accuracy. As this is demonstrated in the above cited papers, our method is more efficient than both the backward and forward finite difference (FD) methods while providing better accuracy and stability. To briefly explain this, let us mention that the FD method we used (and this is pretty standard) provides accuracy O​(h2)𝑂superscriptℎ2O(h^{2}) in space and O​(τ2)𝑂superscript𝜏2O(\tau^{2}) in time, where h,τ

ℎ𝜏h,\tau are the corresponding grid steps. Since in our method the solution is represented as a time integral, it can be computed with higher accuracy in time (eg., by using high order quadratures) , while the dependence on the space coordinate x𝑥x is explicit. Contrary, increasing the accuracy for the FD method is not easy (i.e., it significantly increases the complexity of the method, e.g., see (Itkin, [2017](#bib.bib14))). Then the total accuracy is determined by the accuracy of solving the Volterra equation which is also determined by the order of quadratures used to compute the integral in this equation. For instance, using Gaussian quadratures allows small number of nodes and also high accuracy, in more detail see (Itkin and Muravey, [2020](#bib.bib15); Carr et al., [2020](#bib.bib5)).

Also, as mentioned in (Carr et al., [2020](#bib.bib5)), another advantage of our approach is computation of option Greeks. Since the option prices in both the HP and GIT methods are represented in closed form via integrals, the explicit dependence of prices on the model parameters is available and transparent. Therefore, explicit representations of the option Greeks can be obtained by a simple differentiation under the integrals. This means that the values of Greeks can be calculated simultaneously with the prices almost with no increase in time. This is because differentiation under the integrals slightly changes the integrands, and these changes could be represented as changes in weights of the quadrature scheme used to numerically compute the integrals. Since the major computational time has to be spent for computation of densities which contain special functions, they can be saved during the calculation of the prices, and then reused for computation of Greeks.

One can be curious why we need two methods - the HP and GIT, if they are used to solve the same problem and demonstrate the same performance. The answer is kind of elegant. As shown in (Carr et al., [2020](#bib.bib5)), the GIT method produces very accurate results at high strikes and maturities (i.e. where the option price is relatively small) in contrast to the HP method. This can be verified by looking at the exponents under the GIT solution integral which are proportional to the time τ𝜏\tau. Contrary, when the price is higher (short maturities, low strikes) the GIT method is slightly less accurate than the HP method, as the exponents in the HP solution integral are inversely proportional to τ𝜏\tau. Thus, both methods are complementary.

This situation is well investigated for the heat equation with constant coefficients. There exist two representation of the
solution: one - obtained by using the method of images, and the other one - by the Fourier series. Despite
both solutions are equal as the infinite series, their convergence properties are different, (Lipton, [2002](#bib.bib22)).

Going back to the problem considered in this paper, we skip the explicit formulation of the model. Instead we define a wide class of models where pricing double barrier options can be translated to solving the heat equation with time-dependent boundaries (barriers) and time-dependent boundary conditions (rebates-at-hit). Note, that the problems considered in the above cited paper - pricing barrier and American options in the time-dependent OU process, pricing barrier options in the Hull-White model, etc., also fit to this class as this is shown in the corresponding papers. Then we construct the solution by using both the GIT and the HP methods. The latter was already shortly presented in (Itkin and Muravey, [2020](#bib.bib15)), but for the homogeneous boundary conditions. Also, here we present full derivation of the explicit value of the solution spatial gradient uxsubscript𝑢𝑥u\_{x} at the lower x=y​(τ)𝑥𝑦𝜏x=y(\tau) and upper x=z​(τ)𝑥𝑧𝜏x=z(\tau) boundaries. This derivation differs from that in (Lipton and Kaushansky, [2018](#bib.bib24)) (and is closer in sense to (Tikhonov and Samarskii, [1963](#bib.bib32))), but provides a similar result. Also, all the results obtained in this paper are new.

The novelty of the paper is as follows. First, we construct a semi-analytical solution of the heat equation with two arbitrary moving boundaries and arbitrary time-dependent boundary conditions at these boundaries. To the best of authors’ knowledge this problem was not solved yet.

Second, various financial problems, where efficient pricing of double barrier options with rebates at hit is subject of investigation, can be reduced to this setting. As we have mentioned it already in above, they include time-dependent Hull-White and OU models, the time-dependent Black-Scholes model, etc., (Carr and Itkin, [2020](#bib.bib4); Itkin and Muravey, [2020](#bib.bib15); Itkin et al., [2020a](#bib.bib16)). Also, for the CIR and CEV models, where the pricing problem is reduced to solving the Bessel PDE with time-dependent boundaries, the latter can also be solved in a similar manner, (Carr et al., [2020](#bib.bib5)). Also, local volatility models with σ=σ​(x)𝜎𝜎𝑥\sigma=\sigma(x) can be also treated under this setting.

Third, consider a general one-factor model

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=μ​(t,S)​d​t+σ​(t,S)​d​Wt,St​(t=0)=S0.formulae-sequence𝑑subscript𝑆𝑡𝜇𝑡𝑆𝑑𝑡𝜎𝑡𝑆𝑑subscript𝑊𝑡subscript𝑆𝑡𝑡0subscript𝑆0dS\_{t}=\mu(t,S)dt+\sigma(t,S)dW\_{t},\qquad S\_{t}(t=0)=S\_{0}. |  | (1) |

where t>0𝑡0t>0 is the time, Stsubscript𝑆𝑡S\_{t} is the spot price, μ​(t,S)𝜇𝑡𝑆\mu(t,S) is the drift, σ​(t,S)𝜎𝑡𝑆\sigma(t,S) is the volatility of the process, Wtsubscript𝑊𝑡W\_{t} is the standard Brownian motion under the risk-neutral measure. This model can be solved as follows. Let us split the domain of the definition of S𝑆S into N𝑁N intervals, and at every interval i=1,…,N𝑖

1…𝑁i=1,\ldots,N approximate the drift by a linear function of S𝑆S, i.e. μi​(t,S)=ai​(t)+bi​(t)​Ssubscript𝜇𝑖𝑡𝑆subscript𝑎𝑖𝑡subscript𝑏𝑖𝑡𝑆\mu\_{i}(t,S)=a\_{i}(t)+b\_{i}(t)S, and the volatility - by a quadratic function σi​(t,S)=ci​(t)+di​(t)​S+ei​(t)​S2subscript𝜎𝑖𝑡𝑆subscript𝑐𝑖𝑡subscript𝑑𝑖𝑡𝑆subscript𝑒𝑖𝑡superscript𝑆2\sigma\_{i}(t,S)=c\_{i}(t)+d\_{i}(t)S+e\_{i}(t)S^{2}. Then it can be shown that at every interval the corresponding pricing PDE can be transformed to the heat equation with time-dependent boundaries and the boundary conditions. Using continuity of the solution and its gradient at every sub-boundary, this problem can be solved semi-analytically in a similar fashion. In physics this approach is called the method of multilayer heat equation, see, eg., a nice survey in ([Dias,](#bib.bib7) ). In more detail the development of this method as applied to finance will be published elsewhere. Thus, solving (semi-analytically) the heat equation with time-dependent moving boundaries and the boundary conditions is a key element of such a method. Having this method in hands, pricing double barrier options for any financial model of the type Eq. ([1](#Sx1.E1 "Equation 1 ‣ Introduction ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) can be done semi-analytically.

The rest of the paper is organized as follows. Section [1](#S1 "1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit") describes the double barrier pricing problem
for the time-dependent barriers and rebates at hit and shows that it can be reduced to solving inhomogeneous PDE with homogeneous boundary conditions. Section [2](#S2 "2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit") describes in detail the solution of this problem by using the GIT method. We provide two alternative integral representations of the solution - one via the Jacobi theta functions, and the other one - using the Poisson summation formula. Despite these solutions are equal in a sense of infinite series, their convergence properties are different. A system of the Volterra equations for the gradient of the solution at both boundaries is obtained for both representations. Section [3](#S3 "3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit") provides the same development but using the HP method. The final section concludes.

## 1 Statement of the problem

Let us consider a one-factor diffusion model in Eq. ([1](#Sx1.E1 "Equation 1 ‣ Introduction ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) By using a standard argument, to price options written on Stsubscript𝑆𝑡S\_{t} as an underlying, one can apply the Feynman-Kac theorem to obtain the following partial differential equation (PDE) for, eg., the European Call option price

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂C∂t+12​σ2​(t,S)​∂2C∂S2+μ​(t,S)​S​∂C∂S=r​(t)​C.𝐶𝑡12superscript𝜎2𝑡𝑆superscript2𝐶superscript𝑆2𝜇𝑡𝑆𝑆𝐶𝑆𝑟𝑡𝐶\frac{\partial C}{\partial t}+\frac{\displaystyle 1}{\displaystyle 2}\sigma^{2}(t,S)\frac{\partial^{2}C}{\partial S^{2}}+\mu(t,S)S\frac{\partial C}{\partial S}=r(t)C. |  | (2) |

Here in case of Equities we treat Stsubscript𝑆𝑡S\_{t} as the stock price, then r​(t)𝑟𝑡r(t) is the deterministic interest rate. If Stsubscript𝑆𝑡S\_{t} is the stochastic interest rate, then r​(t)𝑟𝑡r(t) in the RHS of Eq. ([2](#S1.E2 "Equation 2 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) should be replaced with S𝑆S.

The Eq. ([2](#S1.E2 "Equation 2 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) should be solved subject to the terminal condition at the option maturity t=T𝑡𝑇t=T

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(T,S)=(S−K)+,𝐶𝑇𝑆superscript𝑆𝐾C(T,S)=(S-K)^{+}, |  | (3) |

where K𝐾K is the option strike, and some boundary conditions. Below in this paper we are concentrated only on double barrier options with moving barriers: the lower barrier at S=L​(t)𝑆𝐿𝑡S=L(t) and the upper barrier at S=H​(t)>L​(t)𝑆𝐻𝑡𝐿𝑡S=H(t)>L(t), so S∈[L​(t),H​(t)]𝑆𝐿𝑡𝐻𝑡S\in[L(t),H(t)].

Our main assumption in this paper is that the PDE in Eq. ([2](#S1.E2 "Equation 2 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) by a series of transformations of the dependent variable C​(S,t)↦U​(x,τ)maps-to𝐶𝑆𝑡𝑈𝑥𝜏C(S,t)\mapsto U(x,\tau) and independent variables S↦x​(t,S),t↦τ​(t,S)formulae-sequencemaps-to𝑆𝑥𝑡𝑆maps-to𝑡𝜏𝑡𝑆S\mapsto x(t,S),\ t\mapsto\tau(t,S) can be reduced to the heat equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂U∂τ=∂2U∂x2,𝑈𝜏superscript2𝑈superscript𝑥2\frac{\partial U}{\partial\tau}=\frac{\partial^{2}U}{\partial x^{2}}, |  | (4) |

which should be solved at the new domain x∈[y​(τ),z​(τ)],τ∈[0,τ​(0,S0)]formulae-sequence𝑥𝑦𝜏𝑧𝜏𝜏0𝜏0subscript𝑆0x\in[y(\tau),z(\tau)],\ \tau\in[0,\tau(0,S\_{0})], subject to the terminal condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(0,x)=U0​(x),𝑈0𝑥subscript𝑈0𝑥U(0,x)=U\_{0}(x), |  | (5) |

and the boundary conditions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U​(τ,y​(τ))𝑈𝜏𝑦𝜏\displaystyle U(\tau,y(\tau)) | =f−​(τ),U​(τ,z​(τ))=f+​(τ).formulae-sequenceabsentsuperscript𝑓𝜏𝑈𝜏𝑧𝜏superscript𝑓𝜏\displaystyle=f^{-}(\tau),\qquad U(\tau,z(\tau))=f^{+}(\tau). |  | (6) |

Here f±​(τ),y​(τ),z​(τ)

superscript𝑓plus-or-minus𝜏𝑦𝜏𝑧𝜏f^{\pm}(\tau),y(\tau),z(\tau) are some continuous functions of time τ𝜏\tau. From the financial point of view the problem in Eq. ([4](#S1.E4 "Equation 4 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), Eq. ([5](#S1.E5 "Equation 5 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), Eq. ([6](#S1.E6 "Equation 6 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) (the ℬℬ{\cal B} problem) could be viewed as a pricing problem for double barrier options with the moving lower y​(τ)𝑦𝜏y(\tau) and upper z​(τ)𝑧𝜏z(\tau) barriers and the rebates f±​(τ)superscript𝑓plus-or-minus𝜏f^{\pm}(\tau) paid at hit, i.e. when the underlying process hits either the lower or the upper barrier.

Note, that many well-known financial models fit this framework. For instance, the time dependent OU process used in (Carr and Itkin, [2020](#bib.bib4)) to model barrier and American options is such an example. Also, the time-dependent Hull-White model considered in (Itkin and Muravey, [2020](#bib.bib15)) for pricing barrier options is another example. The number of models that fit this framework could be significantly expanded if one transforms the original PDE in Eq. ([2](#S1.E2 "Equation 2 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) to its multilayer version. This approach is discussed it detail in (Itkin et al., [2020b](#bib.bib17)) and will be reported elsewhere.

Below we present solution of the ℬℬ{\cal B} problem by using two analytic methods - the GIT and HP methods. As mentioned in Introduction, the methods are complementary in a sense that despite both solutions are equal, their convergence properties are different. In particular, the GIT method is more accurate at high strikes and maturities while the HP method - at low strikes and maturities.

It is worth mentioning that the ℬℬ{\cal B} problem is with inhomogeneous boundary conditions, hence from the very beginning it is useful to transform it to a similar problem but with homogeneous boundary conditions. This could be done by the change of variables

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u​(τ,x)𝑢𝜏𝑥\displaystyle u(\tau,x) | =U​(τ,x)−A​(τ)−B​(τ)​x,absent𝑈𝜏𝑥𝐴𝜏𝐵𝜏𝑥\displaystyle=U(\tau,x)-A(\tau)-B(\tau)x, |  | (7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(τ)𝐴𝜏\displaystyle A(\tau) | =−f+​(τ)​y​(τ)−f−​(τ)​z​(τ)z​(τ)−y​(τ),B​(τ)=f+​(τ)−f−​(τ)z​(τ)−y​(τ),formulae-sequenceabsentsuperscript𝑓𝜏𝑦𝜏superscript𝑓𝜏𝑧𝜏𝑧𝜏𝑦𝜏𝐵𝜏superscript𝑓𝜏superscript𝑓𝜏𝑧𝜏𝑦𝜏\displaystyle=-\frac{f^{+}(\tau)y(\tau)-f^{-}(\tau)z(\tau)}{z(\tau)-y(\tau)},\qquad B(\tau)=\frac{f^{+}(\tau)-f^{-}(\tau)}{z(\tau)-y(\tau)}, |  |

which transforms the PDE in Eq. ([2](#S1.E2 "Equation 2 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) to the inhomogeneous PDE but with the homogeneous boundary conditions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂u∂τ𝑢𝜏\displaystyle\frac{\partial u}{\partial\tau} | =∂2u∂x2+g​(τ,x),absentsuperscript2𝑢superscript𝑥2𝑔𝜏𝑥\displaystyle=\frac{\partial^{2}u}{\partial x^{2}}+g(\tau,x), |  | (8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(τ,x)𝑔𝜏𝑥\displaystyle g(\tau,x) | ≡−A′​(τ)−B′​(τ)​x,(τ,x)∈ℝ+×[y​(τ),z​(τ)],formulae-sequenceabsentsuperscript𝐴′𝜏superscript𝐵′𝜏𝑥𝜏𝑥subscriptℝ𝑦𝜏𝑧𝜏\displaystyle\equiv-A^{\prime}(\tau)-B^{\prime}(\tau)x,\quad(\tau,x)\in\mathbb{R}\_{+}\times[y(\tau),z(\tau)], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(0,x)𝑢0𝑥\displaystyle u(0,x) | =U0​(x)−A​(0)−B​(0)​x≡u0​(x),u​(τ,y​(τ))=u​(τ,z​(τ))=0.formulae-sequenceabsentsubscript𝑈0𝑥𝐴0𝐵0𝑥subscript𝑢0𝑥𝑢𝜏𝑦𝜏𝑢𝜏𝑧𝜏0\displaystyle=U\_{0}(x)-A(0)-B(0)x\equiv u\_{0}(x),\qquad u(\tau,y(\tau))=u(\tau,z(\tau))=0. |  |

## 2 Solution by the GIT method

In this section we solve the problem in Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) by using the GIT method, see (Kartashov, [1999](#bib.bib18); Carr and Itkin, [2020](#bib.bib4); Itkin and Muravey, [2020](#bib.bib15); Itkin et al., [2020a](#bib.bib16)) and references therein. However, as mentioned in (Kartashov, [2001](#bib.bib19)), an analytic solution for the domain with two moving boundaries is yet unknown. Therefore, our solution presented in this Section is new, and it extends the results of (Carr and Itkin, [2020](#bib.bib4)) obtained for the domain [0,y​(τ)]0𝑦𝜏[0,y(\tau)].

In (Carr and Itkin, [2020](#bib.bib4)) the authors used the GIT proposed in (Kartashov, [1999](#bib.bib18)) which is a map
u​(τ,x)↦u¯​(τ,p)maps-to𝑢𝜏𝑥¯𝑢𝜏𝑝u(\tau,x)\mapsto\bar{u}(\tau,p) of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯​(τ,p)=∫0y​(τ)u​(τ,x)​sinh⁡(x​p)​𝑑x,¯𝑢𝜏𝑝superscriptsubscript0𝑦𝜏𝑢𝜏𝑥𝑥𝑝differential-d𝑥\bar{u}(\tau,p)=\int\_{0}^{y(\tau)}u(\tau,x)\sinh(x\sqrt{p})dx, |  | (9) |

where p=a+i​ω𝑝𝑎i𝜔p=a+\mathrm{i}\mkern 1.0mu\omega is a complex number with ℜ⁡(p)≥β>0𝑝𝛽0\Re(p)\geq\beta>0, and −π4<arg⁡(p)<π4𝜋4𝑝𝜋4-\frac{\pi}{4}<\arg\left(\sqrt{p}\right)<\frac{\pi}{4}. Here we proceed with a similar idea by introducing the transform

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯​(τ,p)=∫y​(τ)z​(τ)u​(τ,x)​sinh⁡(p​[x−y​(τ)])​𝑑x.¯𝑢𝜏𝑝superscriptsubscript𝑦𝜏𝑧𝜏𝑢𝜏𝑥𝑝delimited-[]𝑥𝑦𝜏differential-d𝑥{\bar{u}}(\tau,p)=\int\_{y(\tau)}^{z(\tau)}u(\tau,x)\sinh\left(p[x-y(\tau)]\right)dx. |  | (10) |

With a special choice of the lower boundary y​(τ)=0𝑦𝜏0y(\tau)=0 this transform replicates that one in Eq. ([9](#S2.E9 "Equation 9 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) subject to the point that here we use the spectral parameter p𝑝p instead of p𝑝\sqrt{p} as in (Carr and Itkin, [2020](#bib.bib4)).

Since the kernel of Eq. ([10](#S2.E10 "Equation 10 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) is time-dependent it doesn’t make much sense to apply this transform directly to the inhomogeneous heat equation in Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Therefore, we represent the image u¯¯𝑢{\bar{u}} as a difference of two other images

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯=12​(u¯+−u¯−),u¯±​(τ,p)=∫y​(τ)z​(τ)u​(τ,x)​e±p​[x−y​(τ)]​𝑑x.formulae-sequence¯𝑢12subscript¯𝑢subscript¯𝑢subscript¯𝑢plus-or-minus𝜏𝑝superscriptsubscript𝑦𝜏𝑧𝜏𝑢𝜏𝑥superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦𝜏differential-d𝑥{\bar{u}}=\frac{1}{2}({\bar{u}}\_{+}-{\bar{u}}\_{-}),\qquad{\bar{u}}\_{\pm}(\tau,p)=\int\_{y(\tau)}^{z(\tau)}u(\tau,x)e^{\pm p[x-y(\tau)]}dx. |  | (11) |

To determine u¯​(τ,p)¯𝑢𝜏𝑝{\bar{u}}(\tau,p) let us multiply both parts of the first line in Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) by e±p​[x−y​(τ)]superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦𝜏e^{\pm p[x-y(\tau)]} and integrate on x𝑥x. These yield

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∫y​(τ)z​(τ)superscriptsubscript𝑦𝜏𝑧𝜏\displaystyle\int\_{y(\tau)}^{z(\tau)} | ∂u​(τ,x)∂τ​e±p​[x−y​(τ)]​d​x=∂u¯±​(τ,p)∂τ−u​(τ,z​(τ))​e±p​z​(τ)​z′​(τ)+u​(τ,y​(τ))​e±p​y​(τ)​y′​(τ)𝑢𝜏𝑥𝜏superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦𝜏𝑑𝑥subscript¯𝑢plus-or-minus𝜏𝑝𝜏𝑢𝜏𝑧𝜏superscript𝑒plus-or-minus𝑝𝑧𝜏superscript𝑧′𝜏𝑢𝜏𝑦𝜏superscript𝑒plus-or-minus𝑝𝑦𝜏superscript𝑦′𝜏\displaystyle\frac{\partial u(\tau,x)}{\partial\tau}e^{\pm p[x-y(\tau)]}dx=\frac{\partial{\bar{u}}\_{\pm}(\tau,p)}{\partial\tau}-u(\tau,z(\tau))e^{\pm pz(\tau)}z^{\prime}(\tau)+u(\tau,y(\tau))e^{\pm py(\tau)}y^{\prime}(\tau) |  | (12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ±p​y′​(τ)​∫y​(τ)z​(τ)u​(τ,x)​e±p​[x−y​(τ)]​𝑑x=∂u¯±∂τ±p​y′​(τ)​u¯±,plus-or-minus𝑝superscript𝑦′𝜏superscriptsubscript𝑦𝜏𝑧𝜏𝑢𝜏𝑥superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦𝜏differential-d𝑥plus-or-minussubscript¯𝑢plus-or-minus𝜏𝑝superscript𝑦′𝜏subscript¯𝑢plus-or-minus\displaystyle\pm py^{\prime}(\tau)\int\_{y(\tau)}^{z(\tau)}u(\tau,x)e^{\pm p[x-y(\tau)]}dx=\frac{\partial{\bar{u}}\_{\pm}}{\partial\tau}\pm py^{\prime}(\tau){\bar{u}}\_{\pm}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫y​(τ)z​(τ)superscriptsubscript𝑦𝜏𝑧𝜏\displaystyle\int\_{y(\tau)}^{z(\tau)} | ∂2u​(τ,x)∂x2​e±p​[x−y​(τ)]​d​x=[Φ​(τ)−B​(τ)]​e±p​[z​(τ)−y​(τ)]+[Ψ​(τ)+B​(τ)]+p2​u¯±​(τ,p),superscript2𝑢𝜏𝑥superscript𝑥2superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦𝜏𝑑𝑥delimited-[]Φ𝜏𝐵𝜏superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝜏𝑦𝜏delimited-[]Ψ𝜏𝐵𝜏superscript𝑝2subscript¯𝑢plus-or-minus𝜏𝑝\displaystyle\frac{\partial^{2}u(\tau,x)}{\partial x^{2}}e^{\pm p[x-y(\tau)]}dx=\left[\Phi(\tau)-B(\tau)\right]e^{\pm p[z(\tau)-y(\tau)]}+\left[\Psi(\tau)+B(\tau)\right]+p^{2}{\bar{u}}\_{\pm}(\tau,p), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g¯±​(τ,p)subscript¯𝑔plus-or-minus𝜏𝑝\displaystyle\bar{g}\_{\pm}(\tau,p) | ≡∫y​(τ)z​(τ)g​(τ,x)​e±p​[x−y​(τ)]​𝑑x=B′​(τ)p2​(e±p​[z​(τ)−y​(τ)]−1)absentsuperscriptsubscript𝑦𝜏𝑧𝜏𝑔𝜏𝑥superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦𝜏differential-d𝑥superscript𝐵′𝜏superscript𝑝2superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝜏𝑦𝜏1\displaystyle\equiv\int\_{y(\tau)}^{z(\tau)}g(\tau,x)e^{\pm p[x-y(\tau)]}dx=\frac{B^{\prime}(\tau)}{p^{2}}\left(e^{\pm p[z(\tau)-y(\tau)]}-1\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ±1p​[A′​(τ)​(1−e±p​[z​(τ)−y​(τ)])+B′​(τ)​(y​(τ)−z​(τ)​e±p​[z​(τ)−y​(τ)])].plus-or-minus1𝑝delimited-[]superscript𝐴′𝜏1superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝜏𝑦𝜏superscript𝐵′𝜏𝑦𝜏𝑧𝜏superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝜏𝑦𝜏\displaystyle\pm\frac{1}{p}\left[A^{\prime}(\tau)\left(1-e^{\pm p[z(\tau)-y(\tau)]}\right)+B^{\prime}(\tau)\left(y(\tau)-z(\tau)e^{\pm p[z(\tau)-y(\tau)]}\right)\right]. |  |

where terms proportional to u(τ,y(τ)u(\tau,y(\tau) and u(τ,z(τ)u(\tau,z(\tau) vanish due to the boundary conditions in Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), and by definition

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ψ​(τ)=−∂U​(τ,x)∂x|x=y​(τ)Ψ𝜏evaluated-at𝑈𝜏𝑥𝑥𝑥𝑦𝜏\displaystyle\Psi(\tau)=-\frac{\partial U(\tau,x)}{\partial x}\Bigg{|}\_{x=y(\tau)} | Φ​(τ)=∂U​(τ,x)∂x|x=z​(τ).Φ𝜏evaluated-at𝑈𝜏𝑥𝑥𝑥𝑧𝜏\displaystyle\quad\Phi(\tau)=\frac{\partial U(\tau,x)}{\partial x}\Bigg{|}\_{x=z(\tau)}. |  | (13) |

Collecting terms in Eq. ([12](#S2.E12 "Equation 12 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) yields two initial value problems, one for the function u¯+subscript¯𝑢{\bar{u}}\_{+} and the other one - for u¯−subscript¯𝑢{\bar{u}}\_{-}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂u¯±​(τ,p)∂τsubscript¯𝑢plus-or-minus𝜏𝑝𝜏\displaystyle\frac{\partial{\bar{u}}\_{\pm}(\tau,p)}{\partial\tau} | +u¯±​[±p​y′​(τ)−p2]=[Ψ​(τ)+B​(τ)]+[Φ​(τ)−B​(τ)]​e±p​[z​(τ)−y​(τ)]+g¯±​(τ,p),subscript¯𝑢plus-or-minusdelimited-[]plus-or-minus𝑝superscript𝑦′𝜏superscript𝑝2delimited-[]Ψ𝜏𝐵𝜏delimited-[]Φ𝜏𝐵𝜏superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝜏𝑦𝜏subscript¯𝑔plus-or-minus𝜏𝑝\displaystyle+{\bar{u}}\_{\pm}\left[\pm py^{\prime}(\tau)-p^{2}\right]=\left[\Psi(\tau)+B(\tau)\right]+\left[\Phi(\tau)-B(\tau)\right]e^{\pm p[z(\tau)-y(\tau)]}+\bar{g}\_{\pm}(\tau,p), |  | (14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯±​(0,p)subscript¯𝑢plus-or-minus0𝑝\displaystyle{\bar{u}}\_{\pm}(0,p) | =∫y​(0)z​(0)u​(0,x)​e±p​[x−y​(0)]​𝑑x.absentsuperscriptsubscript𝑦0𝑧0𝑢0𝑥superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦0differential-d𝑥\displaystyle=\int\_{y(0)}^{z(0)}u(0,x)e^{\pm p[x-y(0)]}dx. |  |

Each problem in Eq. ([14](#S2.E14 "Equation 14 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) (for the plus and minus signs) can be solved explicitly

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u¯±​(τ,p)subscript¯𝑢plus-or-minus𝜏𝑝\displaystyle{\bar{u}}\_{\pm}(\tau,p) | =ep2​τ​∫y​(0)z​(0)u​(0,x)​e±p​[x−y​(τ)]​𝑑xabsentsuperscript𝑒superscript𝑝2𝜏superscriptsubscript𝑦0𝑧0𝑢0𝑥superscript𝑒plus-or-minus𝑝delimited-[]𝑥𝑦𝜏differential-d𝑥\displaystyle=e^{p^{2}\tau}\int\_{y(0)}^{z(0)}u(0,x)e^{\pm p[x-y(\tau)]}dx |  | (15) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τep2​(τ−s)​[[Φ​(s)−B​(s)]​e±p​[z​(s)−y​(τ)]+(Ψ​(s)+B​(s)+g¯±​(s,p))​e±p​[y​(s)−y​(τ)]]​𝑑s.superscriptsubscript0𝜏superscript𝑒superscript𝑝2𝜏𝑠delimited-[]delimited-[]Φ𝑠𝐵𝑠superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝑠𝑦𝜏Ψ𝑠𝐵𝑠subscript¯𝑔plus-or-minus𝑠𝑝superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏differential-d𝑠\displaystyle+\int\_{0}^{\tau}e^{p^{2}(\tau-s)}\left[\left[\Phi(s)-B(s)\right]e^{\pm p[z(s)-y(\tau)]}+\left(\Psi(s)+B(s)+\bar{g}\_{\pm}(s,p)\right)e^{\pm p[y(s)-y(\tau)]}\right]ds. |  |

Note that the last term in the second integral in Eq. ([15](#S2.E15 "Equation 15 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) can be re-written in a more convenient form

|  |  |  |  |
| --- | --- | --- | --- |
|  | g¯±​(s,p)subscript¯𝑔plus-or-minus𝑠𝑝\displaystyle\bar{g}\_{\pm}(s,p) | e±p​[y​(s)−y​(τ)]=B′​(s)p2​(e±p​[z​(s)−y​(s)]−1)​e±p​[y​(s)−y​(τ)]superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏superscript𝐵′𝑠superscript𝑝2superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝑠𝑦𝑠1superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏\displaystyle e^{\pm p\left[y(s)-y(\tau)\right]}=\frac{B^{\prime}(s)}{p^{2}}\left(e^{\pm p[z(s)-y(s)]}-1\right)e^{\pm p\left[y(s)-y(\tau)\right]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ±1p​[A′​(s)​(1−e±p​[z​(s)−y​(s)])​e±p​[y​(s)−y​(τ)]+B′​(s)​(y​(s)−z​(s)​e±p​[z​(s)−y​(s)])​e±p​[y​(s)−y​(τ)]]plus-or-minus1𝑝delimited-[]superscript𝐴′𝑠1superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝑠𝑦𝑠superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏superscript𝐵′𝑠𝑦𝑠𝑧𝑠superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝑠𝑦𝑠superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏\displaystyle\pm\frac{1}{p}\left[A^{\prime}(s)\left(1-e^{\pm p[z(s)-y(s)]}\right)e^{\pm p\left[y(s)-y(\tau)\right]}+B^{\prime}(s)\left(y(s)-z(s)e^{\pm p[z(s)-y(s)]}\right)e^{\pm p\left[y(s)-y(\tau)\right]}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =B′​(s)p2​(e±p​[z​(s)−y​(τ)]−e±p​[y​(s)−y​(τ)])absentsuperscript𝐵′𝑠superscript𝑝2superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝑠𝑦𝜏superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏\displaystyle=\frac{B^{\prime}(s)}{p^{2}}\left(e^{\pm p[z(s)-y(\tau)]}-e^{\pm p[y(s)-y(\tau)]}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ±1p​[A′​(s)​(e±p​[y​(s)−y​(τ)]−e±p​[z​(s)−y​(τ)])+B′​(s)​(y​(s)​e±p​[y​(s)−y​(τ)]−z​(s)​e±p​[z​(s)−y​(τ)])].plus-or-minus1𝑝delimited-[]superscript𝐴′𝑠superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝑠𝑦𝜏superscript𝐵′𝑠𝑦𝑠superscript𝑒plus-or-minus𝑝delimited-[]𝑦𝑠𝑦𝜏𝑧𝑠superscript𝑒plus-or-minus𝑝delimited-[]𝑧𝑠𝑦𝜏\displaystyle\pm\frac{1}{p}\left[A^{\prime}(s)\left(e^{\pm p[y(s)-y(\tau)]}-e^{\pm p[z(s)-y(\tau)]}\right)+B^{\prime}(s)\left(y(s)e^{\pm p[y(s)-y(\tau)]}-z(s)e^{\pm p[z(s)-y(\tau)]}\right)\right]. |  |

The explicit representation for u¯¯𝑢{\bar{u}} then follows from its definition in Eq. ([11](#S2.E11 "Equation 11 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u¯​(τ,p)¯𝑢𝜏𝑝\displaystyle{\bar{u}}(\tau,p) | =ep2​τ​∫y​(0)z​(0)u​(0,x)​sinh⁡(p​[x−y​(τ)])​𝑑xabsentsuperscript𝑒superscript𝑝2𝜏superscriptsubscript𝑦0𝑧0𝑢0𝑥𝑝delimited-[]𝑥𝑦𝜏differential-d𝑥\displaystyle=e^{p^{2}\tau}\int\_{y(0)}^{z(0)}u(0,x)\sinh\left(p[x-y(\tau)]\right)dx |  | (16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τep2​(τ−s)​[[Φ​(s)−B​(s)]​sinh⁡(p​[z​(s)−y​(τ)])+[Ψ​(s)+B​(s)]​sinh⁡(p​[y​(s)−y​(τ)])+h​(s,p)]​𝑑s,superscriptsubscript0𝜏superscript𝑒superscript𝑝2𝜏𝑠delimited-[]delimited-[]Φ𝑠𝐵𝑠𝑝delimited-[]𝑧𝑠𝑦𝜏delimited-[]Ψ𝑠𝐵𝑠𝑝delimited-[]𝑦𝑠𝑦𝜏ℎ𝑠𝑝differential-d𝑠\displaystyle+\int\_{0}^{\tau}e^{p^{2}(\tau-s)}\left[\left[\Phi(s)-B(s)\right]\sinh\left(p[z(s)-y(\tau)]\right)+\left[\Psi(s)+B(s)\right]\sinh(p[y(s)-y(\tau)])+h(s,p)\right]ds, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(s,p)ℎ𝑠𝑝\displaystyle h(s,p) | =B′​(s)p2​[sinh⁡(p​[z​(s)−y​(τ)])−sinh⁡(p​[y​(s)−y​(τ)])]absentsuperscript𝐵′𝑠superscript𝑝2delimited-[]𝑝delimited-[]𝑧𝑠𝑦𝜏𝑝delimited-[]𝑦𝑠𝑦𝜏\displaystyle=\frac{B^{\prime}(s)}{p^{2}}\left[\sinh(p[z(s)-y(\tau)])-\sinh(p[y(s)-y(\tau)])\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1p​[(A′​(s)+B′​(s)​y​(s))​cosh⁡(p​[y​(s)−y​(τ)])−(A′​(s)+B′​(s)​z​(s))​cosh⁡(p​[z​(s)−y​(τ)])].1𝑝delimited-[]superscript𝐴′𝑠superscript𝐵′𝑠𝑦𝑠𝑝delimited-[]𝑦𝑠𝑦𝜏superscript𝐴′𝑠superscript𝐵′𝑠𝑧𝑠𝑝delimited-[]𝑧𝑠𝑦𝜏\displaystyle+\frac{1}{p}\left[\left(A^{\prime}(s)+B^{\prime}(s)y(s)\right)\cosh(p[y(s)-y(\tau)])-\left(A^{\prime}(s)+B^{\prime}(s)z(s)\right)\cosh(p[z(s)-y(\tau)])\right]. |  |

### 2.1 The inverse transform

General theory of the heat equation tells us that the solution at the space domain a<x<b,a,b∈ℜ−c​o​n​s​tformulae-sequence𝑎𝑥𝑏

𝑎𝑏
𝑐𝑜𝑛𝑠𝑡a<x<b,\ a,b\in\Re-const, can be represented as Fourier series of the form, (Polyanin, [2002](#bib.bib29)))

|  |  |  |
| --- | --- | --- |
|  | u​(τ,x)=∑n=1∞αn​e−π2​n2(b−a)2​τ​sin⁡(π​n​(x−a)b−a)𝑢𝜏𝑥superscriptsubscript𝑛1subscript𝛼𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑏𝑎2𝜏𝜋𝑛𝑥𝑎𝑏𝑎u(\tau,x)=\sum\_{n=1}^{\infty}\alpha\_{n}e^{-\frac{\pi^{2}n^{2}}{(b-a)^{2}}\tau}\sin\left(\frac{\pi n(x-a)}{b-a}\right) |  |

Therefore, by analogy let us look for the inverse transform of u¯¯𝑢{\bar{u}} (which actually is the solution u​(τ,x)𝑢𝜏𝑥u(\tau,x) of Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))) to be a generalized Fourier transform of the form (Carr and Itkin ([2020](#bib.bib4)))

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(τ,x)=∑n=0∞An​(τ)​sin⁡(π​n​x−y​(τ)z​(τ)−y​(τ)),𝑢𝜏𝑥superscriptsubscript𝑛0subscript𝐴𝑛𝜏𝜋𝑛𝑥𝑦𝜏𝑧𝜏𝑦𝜏u(\tau,x)=\sum\_{n=0}^{\infty}A\_{n}(\tau)\sin\left(\pi n\frac{x-y(\tau)}{z(\tau)-y(\tau)}\right), |  | (17) |

where An​(τ)subscript𝐴𝑛𝜏A\_{n}(\tau) are some yet unknown Fourier coefficients (weights). Applying the direct transform in Eq. ([10](#S2.E10 "Equation 10 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) to the series in Eq. ([17](#S2.E17 "Equation 17 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯​(τ,x)=∫y​(τ)z​(τ)∑n=1∞An​(τ)​sin⁡(π​n​x−y​(τ)z​(τ)−y​(τ))​sinh⁡(p​[x−y​(τ)])​d​x.¯𝑢𝜏𝑥superscriptsubscript𝑦𝜏𝑧𝜏superscriptsubscript𝑛1subscript𝐴𝑛𝜏𝜋𝑛𝑥𝑦𝜏𝑧𝜏𝑦𝜏𝑝delimited-[]𝑥𝑦𝜏𝑑𝑥{\bar{u}}(\tau,x)=\int\_{y(\tau)}^{z(\tau)}\sum\_{n=1}^{\infty}A\_{n}(\tau)\sin\left(\pi n\frac{x-y(\tau)}{z(\tau)-y(\tau)}\right)\sinh\left(p[x-y(\tau)]\right)dx. |  | (18) |

Using the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫yzsin⁡(π​n​x−yz−y)​sinh⁡(p​[x−y])​𝑑x=(−1)n+1​π​n​(z−y)​sinh⁡(p​[z−y])n2​π2+p2​(z−y)2,superscriptsubscript𝑦𝑧𝜋𝑛𝑥𝑦𝑧𝑦𝑝delimited-[]𝑥𝑦differential-d𝑥superscript1𝑛1𝜋𝑛𝑧𝑦𝑝delimited-[]𝑧𝑦superscript𝑛2superscript𝜋2superscript𝑝2superscript𝑧𝑦2\int\_{y}^{z}\sin\left(\pi n\frac{x-y}{z-y}\right)\sinh\left(p[x-y]\right)dx=(-1)^{n+1}\frac{\pi n(z-y)\sinh\left(p[z-y]\right)}{n^{2}\pi^{2}+p^{2}(z-y)^{2}}, |  | (19) |

we obtain another representation for u¯¯𝑢{\bar{u}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯​(τ,x)=1l​(τ)​∑n=1∞(−1)n+1​π​n​An​(τ)​sinh⁡(p​l​(τ))[p+i​n​π/l​(τ)]​[p−i​n​π/l​(τ)],l​(τ)=z​(τ)−y​(τ).formulae-sequence¯𝑢𝜏𝑥1𝑙𝜏superscriptsubscript𝑛1superscript1𝑛1𝜋𝑛subscript𝐴𝑛𝜏𝑝𝑙𝜏delimited-[]𝑝i𝑛𝜋𝑙𝜏delimited-[]𝑝i𝑛𝜋𝑙𝜏𝑙𝜏𝑧𝜏𝑦𝜏{\bar{u}}(\tau,x)=\frac{1}{l(\tau)}\sum\_{n=1}^{\infty}\frac{(-1)^{n+1}\pi nA\_{n}(\tau)\sinh\left(pl(\tau)\right)}{\left[p+\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]\left[p-\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]},\qquad l(\tau)=z(\tau)-y(\tau). |  | (20) |

Combining Eq. ([20](#S2.E20 "Equation 20 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and Eq. ([16](#S2.E16 "Equation 16 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) yields the equation for An​(τ)subscript𝐴𝑛𝜏A\_{n}(\tau)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1l​(τ)​∑n=1∞1𝑙𝜏superscriptsubscript𝑛1\displaystyle\frac{1}{l(\tau)}\sum\_{n=1}^{\infty} | (−1)n+1​π​n​An​(τ)[p+i​n​π/l​(τ)]​[p−i​n​π/l​(τ)]=1sinh⁡(p​l​(τ)){ep2​τ∫y​(0)z​(0)u(0,x)sinh(p[x−y(τ)])dx\displaystyle\frac{(-1)^{n+1}\pi nA\_{n}(\tau)}{\left[p+\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]\left[p-\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]}=\frac{1}{\sinh\left(p\,l(\tau)\right)}\Bigg{\{}e^{p^{2}\tau}\int\_{y(0)}^{z(0)}u(0,x)\sinh\left(p[x-y(\tau)]\right)dx |  | (21) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | ∫0τep2​(τ−s)[[Φ(s)−B(s)]sinh(p[z(s)−y(τ)])+[Ψ(s)+B(s)]sinh(p[y(s)−y(τ)])+h(s,p)]ds}.\displaystyle\int\_{0}^{\tau}e^{p^{2}(\tau-s)}\left[\left[\Phi(s)-B(s)\right]\sinh\left(p[z(s)-y(\tau)]\right)+\left[\Psi(s)+B(s)\right]\sinh\left(p[y(s)-y(\tau)]\right)+h(s,p)\right]ds\Bigg{\}}. |  |

The LHS and RHS of Eq. ([21](#S2.E21 "Equation 21 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) as the functions of p𝑝p are analytic in the whole complex plane domain except the poles

|  |  |  |  |
| --- | --- | --- | --- |
|  | pk±=±i​π​k/l​(τ),k=1,2,…,formulae-sequencesuperscriptsubscript𝑝𝑘plus-or-minusplus-or-minusi𝜋𝑘𝑙𝜏𝑘  12…p\_{k}^{\pm}=\pm\mathrm{i}\mkern 1.0mu\pi k/l(\tau),\quad k=1,2,\ldots, |  | (22) |

because h​(s,p)ℎ𝑠𝑝h(s,p) is regular and well-behaved at p→0→𝑝0p\to 0. Also, as this is easy to check, these poles are common for the LHS and RHS of Eq. ([21](#S2.E21 "Equation 21 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). For what follows we need the following residues

|  |  |  |  |
| --- | --- | --- | --- |
|  | Resp=pk±​∑n=1∞1[p+i​n​π/l​(τ)]​[p−i​n​π/l​(τ)]=±l​(τ)2​i​π​k,Resp=pk±1sinh⁡(p​l​(τ))=(−1)kl​(τ).formulae-sequencesubscriptRes𝑝superscriptsubscript𝑝𝑘plus-or-minussuperscriptsubscript𝑛11delimited-[]𝑝i𝑛𝜋𝑙𝜏delimited-[]𝑝i𝑛𝜋𝑙𝜏plus-or-minus𝑙𝜏2i𝜋𝑘subscriptRes𝑝superscriptsubscript𝑝𝑘plus-or-minus1𝑝𝑙𝜏superscript1𝑘𝑙𝜏\operatorname\*{Res}\_{p=p\_{k}^{\pm}}\sum\_{n=1}^{\infty}\frac{1}{\left[p+\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]\left[p-\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]}=\pm\frac{l(\tau)}{2\mathrm{i}\mkern 1.0mu\pi k},\qquad\qquad\operatorname\*{Res}\_{p=p\_{k}^{\pm}}\frac{1}{\sinh\left(p\,l(\tau)\right)}=\frac{(-1)^{k}}{l(\tau)}. |  | (23) |

The Fourier coefficients Ak​(τ)subscript𝐴𝑘𝜏A\_{k}(\tau) can now be found from Eq. ([21](#S2.E21 "Equation 21 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) by applying contour integration on p𝑝p to both sides. We integrate using the contours Lk+,k=1,2,…formulae-sequence

superscriptsubscript𝐿𝑘𝑘
1

2…L\_{k}^{+},\ k=1,2,\ldots, where the integration contours look like it is depicted in Fig. [1](#S2.F1 "Figure 1 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"). Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1l​(τ)​∫Lk+1𝑙𝜏subscriptsuperscriptsubscript𝐿𝑘\displaystyle\frac{1}{l(\tau)}\int\displaylimits\_{L\_{k}^{+}} | ∑n=1∞(−1)n+1​π​n​An​(τ)[p+i​n​π/l​(τ)]​[p−i​n​π/l​(τ)]dp=∫Lk+1sinh⁡(p​l​(τ)){ep2​τ∫y​(0)z​(0)u(0,x)sinh(p[x−y(τ)])dx\displaystyle\sum\_{n=1}^{\infty}\frac{(-1)^{n+1}\pi nA\_{n}(\tau)}{\left[p+\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]\left[p-\mathrm{i}\mkern 1.0mun\pi/l(\tau)\right]}dp=\int\displaylimits\_{L\_{k}^{+}}\frac{1}{\sinh\left(pl(\tau)\right)}\Bigg{\{}e^{p^{2}\tau}\int\_{y(0)}^{z(0)}u(0,x)\sinh\left(p[x-y(\tau)]\right)dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0τep2​(τ−s)[Φ(s)sinh(p[z(s)−y(τ)])+Ψ(s)sinh(p[y(s)−y(τ)])+h(s,p)]ds}dp.\displaystyle+\int\_{0}^{\tau}e^{p^{2}(\tau-s)}\left[\Phi(s)\sinh\left(p[z(s)-y(\tau)]\right)+\Psi(s)\sinh\left(p[y(s)-y(\tau)]\right)+h(s,p)\right]ds\Bigg{\}}dp. |  | (24) |

Figure 1: Contours of integration of Eq. ([21](#S2.E21 "Equation 21 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) in the complex plane p∈ℂ𝑝ℂp\in\mathbb{C} with poles at p1±,p2±,…

superscriptsubscript𝑝1plus-or-minussuperscriptsubscript𝑝2plus-or-minus…p\_{1}^{\pm},p\_{2}^{\pm},\ldots.

Re⁡pRe𝑝\operatorname{Re}pIm⁡pIm𝑝\operatorname{Im}p00∙∙\bullet∙∙\bullet∙∙\bullet∙∙\bullet∙∙\bullet∙∙\bullet⋮⋮\vdots⋮⋮\vdotsp1+superscriptsubscript𝑝1p\_{1}^{+}p1−superscriptsubscript𝑝1p\_{1}^{-}L1+superscriptsubscript𝐿1L\_{1}^{+}p2+superscriptsubscript𝑝2p\_{2}^{+}p2−superscriptsubscript𝑝2p\_{2}^{-}L2+superscriptsubscript𝐿2L\_{2}^{+}pk+superscriptsubscript𝑝𝑘p\_{k}^{+}pk−superscriptsubscript𝑝𝑘p\_{k}^{-}Lk+superscriptsubscript𝐿𝑘L\_{k}^{+}

  

By the Cauchy’s residue theorem each integral in Eq. ([2.1](#S2.Ex19 "2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) is equal to the sum of the corresponding residues that can be computed with the help of Eq. ([23](#S2.E23 "Equation 23 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). This yields the following formula for Ak​(τ)subscript𝐴𝑘𝜏A\_{k}(\tau)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ak​(τ)=2i​l​(τ)​u¯​(τ,i​π​kl​(τ)).subscript𝐴𝑘𝜏2i𝑙𝜏¯𝑢𝜏i𝜋𝑘𝑙𝜏A\_{k}(\tau)=\frac{2}{\mathrm{i}\mkern 1.0mul(\tau)}{\bar{u}}\left(\tau,\mathrm{i}\mkern 1.0mu\frac{\pi k}{l(\tau)}\right). |  | (25) |

With allowance for Eq. ([16](#S2.E16 "Equation 16 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) this can be finally represented as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ak​(τ)subscript𝐴𝑘𝜏\displaystyle A\_{k}(\tau) | =2l​(τ){e−π2​k2l2​(τ)​τ∫y​(0)z​(0)u(0,x)sin(π​kl​(τ)[x−y(τ)])dx\displaystyle=\frac{2}{l(\tau)}\Bigg{\{}e^{-\frac{\pi^{2}k^{2}}{l^{2}(\tau)}\tau}\int\_{y(0)}^{z(0)}u(0,x)\sin\left(\frac{\pi k}{l(\tau)}[x-y(\tau)]\right)dx |  | (26) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​k2l2​(τ)​(τ−s)[[Φ(s)−B(s)]sin(π​kl​(τ)[z(s)−y(τ)])\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}k^{2}}{l^{2}(\tau)}(\tau-s)}\bigg{[}\left[\Phi(s)-B(s)\right]\sin\left(\frac{\pi k}{l(\tau)}[z(s)-y(\tau)]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[Ψ(s)+B(s)]sin(π​kl​(τ)[y(s)−y(τ)])+h1(k,s,τ)]ds},\displaystyle+\left[\Psi(s)+B(s)\right]\sin\left(\frac{\pi k}{l(\tau)}[y(s)-y(\tau)]\right)+h\_{1}(k,s,\tau)\bigg{]}ds\Bigg{\}}, |  |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | h1​(k,s,τ)=−B′​(s)​l2​(τ)π2​k2​[sin⁡(π​kl​(τ)​[z​(s)−y​(τ)])−sin⁡(π​kl​(τ)​[y​(s)−y​(τ)])]subscriptℎ1𝑘𝑠𝜏superscript𝐵′𝑠superscript𝑙2𝜏superscript𝜋2superscript𝑘2delimited-[]𝜋𝑘𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏𝜋𝑘𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏\displaystyle h\_{1}(k,s,\tau)=-\frac{B^{\prime}(s)l^{2}(\tau)}{\pi^{2}k^{2}}\left[\sin\left(\frac{\pi k}{l(\tau)}[z(s)-y(\tau)]\right)-\sin\left(\frac{\pi k}{l(\tau)}[y(s)-y(\tau)]\right)\right] |  | (27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −l​(τ)π​k​[(A′​(s)+B′​(s)​y​(s))​cos⁡(π​kl​(τ)​[y​(s)−y​(τ)])−(A′​(s)+B′​(s)​z​(s))​cos⁡(π​kl​(τ)​[z​(s)−y​(τ)])].𝑙𝜏𝜋𝑘delimited-[]superscript𝐴′𝑠superscript𝐵′𝑠𝑦𝑠𝜋𝑘𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏superscript𝐴′𝑠superscript𝐵′𝑠𝑧𝑠𝜋𝑘𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏\displaystyle-\frac{l(\tau)}{\pi k}\Bigg{[}\left(A^{\prime}(s)+B^{\prime}(s)y(s)\right)\cos\left(\frac{\pi k}{l(\tau)}[y(s)-y(\tau)]\right)-\left(A^{\prime}(s)+B^{\prime}(s)z(s)\right)\cos\left(\frac{\pi k}{l(\tau)}[z(s)-y(\tau)]\right)\Bigg{]}. |  |

Keeping in mind that

|  |  |  |
| --- | --- | --- |
|  | A​(τ)+B​(τ)​y​(τ)=f−​(τ)A​(τ)+B​(τ)​z​(τ)=f+​(τ)formulae-sequence𝐴𝜏𝐵𝜏𝑦𝜏superscript𝑓𝜏𝐴𝜏𝐵𝜏𝑧𝜏superscript𝑓𝜏A(\tau)+B(\tau)y(\tau)=f^{-}(\tau)\qquad A(\tau)+B(\tau)z(\tau)=f^{+}(\tau) |  |

we re-arrange Eq. ([27](#S2.E27 "Equation 27 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | h1​(k,s,τ)=−B′​(s)​l2​(τ)π2​k2​[sin⁡(π​kl​(τ)​[z​(s)−y​(τ)])−sin⁡(π​kl​(τ)​[y​(s)−y​(τ)])]subscriptℎ1𝑘𝑠𝜏superscript𝐵′𝑠superscript𝑙2𝜏superscript𝜋2superscript𝑘2delimited-[]𝜋𝑘𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏𝜋𝑘𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏\displaystyle h\_{1}(k,s,\tau)=-\frac{B^{\prime}(s)l^{2}(\tau)}{\pi^{2}k^{2}}\left[\sin\left(\frac{\pi k}{l(\tau)}[z(s)-y(\tau)]\right)-\sin\left(\frac{\pi k}{l(\tau)}[y(s)-y(\tau)]\right)\right] |  | (28) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −l​(τ)π​k​[((f−)′​(s)−B​(s)​y′​(s))​cos⁡(π​kl​(τ)​[y​(s)−y​(τ)])−((f+)′​(s)−B​(s)​z′​(s))​cos⁡(π​kl​(τ)​[z​(s)−y​(τ)])].𝑙𝜏𝜋𝑘delimited-[]superscriptsuperscript𝑓′𝑠𝐵𝑠superscript𝑦′𝑠𝜋𝑘𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏superscriptsuperscript𝑓′𝑠𝐵𝑠superscript𝑧′𝑠𝜋𝑘𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏\displaystyle-\frac{l(\tau)}{\pi k}\Bigg{[}\left((f^{-})^{\prime}(s)-B(s)y^{\prime}(s)\right)\cos\left(\frac{\pi k}{l(\tau)}[y(s)-y(\tau)]\right)-\left((f^{+})^{\prime}(s)-B(s)z^{\prime}(s)\right)\cos\left(\frac{\pi k}{l(\tau)}[z(s)-y(\tau)]\right)\Bigg{]}. |  |

Substituting this result into Eq. ([17](#S2.E17 "Equation 17 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), we obtain the solution u​(τ,x)𝑢𝜏𝑥u(\tau,x) of the problem Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u(τ,\displaystyle u(\tau, | x)=2l​(τ)∑n=1∞sin(πnx−y​(τ)l​(τ)){e−π2​n2l2​(τ)​τ∫y​(0)z​(0)u(0,ξ)sin(π​nl​(τ)[ξ−y(τ)])dξ\displaystyle x)=\frac{2}{l(\tau)}\sum\_{n=1}^{\infty}\sin\left(\pi n\frac{x-y(\tau)}{l(\tau)}\right)\Bigg{\{}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\int\_{y(0)}^{z(0)}u(0,\xi)\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi |  | (29) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)​[[Φ​(s)−B​(s)]​sin⁡(π​nl​(τ)​[z​(s)−y​(τ)])+[Ψ​(s)+B​(s)]​sin⁡(π​nl​(τ)​[y​(s)−y​(τ)])]​𝑑ssuperscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠delimited-[]delimited-[]Φ𝑠𝐵𝑠𝜋𝑛𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏delimited-[]Ψ𝑠𝐵𝑠𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏differential-d𝑠\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\bigg{[}\left[\Phi(s)-B(s)\right]\sin\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)+\left[\Psi(s)+B(s)\right]\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)\bigg{]}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)h1(n,s,τ)ds}.\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}h\_{1}(n,s,\tau)ds\Bigg{\}}. |  |

This expression can be further simplified, see Appendix [A](#A1 "Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"). Returning back to the original variable U​(τ,x)𝑈𝜏𝑥U(\tau,x) yields the final representation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U​(τ,x)𝑈𝜏𝑥\displaystyle U(\tau,x) | =2l​(τ)∑n=1∞sin(πnx−y​(τ)l​(τ)){e−π2​n2l2​(τ)​τ∫y​(0)z​(0)U(0,ξ)sin(π​nl​(τ)[ξ−y(τ)])dξ\displaystyle=\frac{2}{l(\tau)}\sum\_{n=1}^{\infty}\sin\left(\pi n\frac{x-y(\tau)}{l(\tau)}\right)\Bigg{\{}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\int\_{y(0)}^{z(0)}U(0,\xi)\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi |  | (30) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)[Φ(s)sin(π​nl​(τ)[z(s)−y(τ)])+Ψ(s)sin(π​nl​(τ)[y(s)−y(τ)])\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\Big{[}\Phi(s)\sin\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)+\Psi(s)\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +β(τ,s,n)]ds}+F(τ,x).\displaystyle+\beta(\tau,s,n)\Big{]}ds\Bigg{\}}+F(\tau,x). |  |

where β​(τ,s,n)𝛽𝜏𝑠𝑛\beta(\tau,s,n) and F​(τ,x)𝐹𝜏𝑥F(\tau,x) are defined in Eq. ([A.2](#A1.E2 "Equation A.2 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and Eq. ([A.10](#A1.E10 "Equation A.10 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Also, as can be checked from the definition in Eq. ([A.10](#A1.E10 "Equation A.10 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) that at y​(τ)<x<z​(τ)𝑦𝜏𝑥𝑧𝜏y(\tau)<x<z(\tau) the function F​(τ,x)𝐹𝜏𝑥F(\tau,x) vanishes, and F​(τ,y​(τ))=f−​(τ),F​(τ,z​(τ))=f+​(τ)formulae-sequence𝐹𝜏𝑦𝜏superscript𝑓𝜏𝐹𝜏𝑧𝜏superscript𝑓𝜏F(\tau,y(\tau))=f^{-}(\tau),\ F(\tau,z(\tau))=f^{+}(\tau). Thus, Eq. ([30](#S2.E30 "Equation 30 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) solves the problem in Eq. ([4](#S1.E4 "Equation 4 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) with the initial condition in Eq. ([5](#S1.E5 "Equation 5 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and the boundary conditions in Eq. ([6](#S1.E6 "Equation 6 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")).

It is worth mentioning that the exact same formalism can be developed by using another integral transform

|  |  |  |
| --- | --- | --- |
|  | u¯​(τ,p)=∫y​(τ)z​(τ)sinh⁡(p​[z​(τ)−x])​u​(τ,x)​𝑑x,¯𝑢𝜏𝑝superscriptsubscript𝑦𝜏𝑧𝜏𝑝delimited-[]𝑧𝜏𝑥𝑢𝜏𝑥differential-d𝑥{\bar{u}}(\tau,p)=\int\_{y(\tau)}^{z(\tau)}\sinh\left(p[z(\tau)-x]\right)u(\tau,x)dx, |  |

with the result being same as in Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")).

### 2.2 Connection to the Jacobi theta function

As observed in (Carr and Itkin, [2020](#bib.bib4)), the sums in Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) could be expressed via the Jacobi theta functions of the third kind, (Mumford et al., [1983](#bib.bib28))111Which is not a surprise since it is known that the Jacobi theta functions is the solution of the heat equation with periodic boundary conditions. As applied to the problem considered in this paper, an example is a double barrier option with zero rebate at hit.. Using their definition

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ3​(z,ω)=1+2​∑n=1∞ωn2​cos⁡(2​n​z),subscript𝜃3𝑧𝜔12superscriptsubscript𝑛1superscript𝜔superscript𝑛22𝑛𝑧\theta\_{3}(z,\omega)=1+2\sum\_{n=1}^{\infty}\omega^{n^{2}}\cos\left(2nz\right), |  | (31) |

and the identities

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂θ3​(z,ω)∂z=θ3′​(z,ω)=−4​∑n=1∞n​ωn2​sin⁡(2​n​z).subscript𝜃3𝑧𝜔𝑧superscriptsubscript𝜃3′𝑧𝜔4superscriptsubscript𝑛1𝑛superscript𝜔superscript𝑛22𝑛𝑧\displaystyle\frac{\partial\theta\_{3}(z,\omega)}{\partial z}=\theta\_{3}^{\prime}(z,\omega)=-4\sum\_{n=1}^{\infty}n\omega^{n^{2}}\sin\left(2nz\right). |  | (32) |

we obtain from Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | 4​∑n=1∞e−π2​n2l2​(τ)​τ​sin⁡(n​π​(x−y​(τ))l​(τ))​sin⁡(n​π​(ξ−y​(τ))l​(τ))4superscriptsubscript𝑛1superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑛𝜋𝑥𝑦𝜏𝑙𝜏𝑛𝜋𝜉𝑦𝜏𝑙𝜏\displaystyle 4\sum\_{n=1}^{\infty}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\sin\left(\frac{n\pi(x-y(\tau))}{l(\tau)}\right)\sin\left(\frac{n\pi(\xi-y(\tau))}{l(\tau)}\right) | =θ3​(ϕ−​(x,ξ),ω1)−θ3​(ϕ+​(x,ξ),ω1),absentsubscript𝜃3subscriptitalic-ϕ𝑥𝜉subscript𝜔1subscript𝜃3subscriptitalic-ϕ𝑥𝜉subscript𝜔1\displaystyle=\theta\_{3}(\phi\_{-}(x,\xi),\omega\_{1})-\theta\_{3}(\phi\_{+}(x,\xi),\omega\_{1}), |  | (33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 4​∑n=1∞e−π2​n2l2​(τ)​(τ−s)​sin⁡(n​π​(x−y​(τ))l​(τ))​sin⁡(n​π​(ξ−y​(τ))l​(τ))4superscriptsubscript𝑛1superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝑛𝜋𝑥𝑦𝜏𝑙𝜏𝑛𝜋𝜉𝑦𝜏𝑙𝜏\displaystyle 4\sum\_{n=1}^{\infty}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\sin\left(\frac{n\pi(x-y(\tau))}{l(\tau)}\right)\sin\left(\frac{n\pi(\xi-y(\tau))}{l(\tau)}\right) | =θ3​(ϕ−​(x,ξ),ω2)−θ3​(ϕ+​(x,ξ),ω2),absentsubscript𝜃3subscriptitalic-ϕ𝑥𝜉subscript𝜔2subscript𝜃3subscriptitalic-ϕ𝑥𝜉subscript𝜔2\displaystyle=\theta\_{3}(\phi\_{-}(x,\xi),\omega\_{2})-\theta\_{3}(\phi\_{+}(x,\xi),\omega\_{2}), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 8​∑n=1∞n​e−π2​n2l2​(τ)​(τ−s)​sin⁡(n​π​(x−y​(τ))l​(τ))​cos⁡(n​π​(ξ−y​(τ))l​(τ))8superscriptsubscript𝑛1𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝑛𝜋𝑥𝑦𝜏𝑙𝜏𝑛𝜋𝜉𝑦𝜏𝑙𝜏\displaystyle 8\sum\_{n=1}^{\infty}ne^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\sin\left(\frac{n\pi(x-y(\tau))}{l(\tau)}\right)\cos\left(\frac{n\pi(\xi-y(\tau))}{l(\tau)}\right) | =−(θ3′​(ϕ−​(x,ξ),ω2)+θ3′​(ϕ+​(x,ξ),ω2)).absentsuperscriptsubscript𝜃3′subscriptitalic-ϕ𝑥𝜉subscript𝜔2superscriptsubscript𝜃3′subscriptitalic-ϕ𝑥𝜉subscript𝜔2\displaystyle=-\left(\theta\_{3}^{\prime}(\phi\_{-}(x,\xi),\omega\_{2})+\theta\_{3}^{\prime}(\phi\_{+}(x,\xi),\omega\_{2})\right). |  |

|  |  |  |
| --- | --- | --- |
|  | ω1=e−π2​τl2​(τ),ω2=e−π2​(τ−s)l2​(τ),ϕ−​(x,ξ)=π​(x−ξ)2​l​(τ),ϕ+​(x,ξ)=π​(x+ξ−2​y​(τ))2​l​(τ).formulae-sequencesubscript𝜔1superscript𝑒superscript𝜋2𝜏superscript𝑙2𝜏formulae-sequencesubscript𝜔2superscript𝑒superscript𝜋2𝜏𝑠superscript𝑙2𝜏formulae-sequencesubscriptitalic-ϕ𝑥𝜉𝜋𝑥𝜉2𝑙𝜏subscriptitalic-ϕ𝑥𝜉𝜋𝑥𝜉2𝑦𝜏2𝑙𝜏\omega\_{1}=e^{-\frac{\pi^{2}\tau}{l^{2}(\tau)}},\quad\omega\_{2}=e^{-\frac{\pi^{2}(\tau-s)}{l^{2}(\tau)}},\quad\phi\_{-}(x,\xi)=\frac{\pi(x-\xi)}{2l(\tau)},\quad\phi\_{+}(x,\xi)=\frac{\pi(x+\xi-2y(\tau))}{2l(\tau)}. |  |

With the help of Eq. ([33](#S2.E33 "Equation 33 ‣ 2.2 Connection to the Jacobi theta function ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) the final formula for u​(τ,x)𝑢𝜏𝑥u(\tau,x) simplifies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 2l(τ)[U(τ,x)\displaystyle 2l(\tau)\Big{[}U(\tau,x) | −F(τ,x)]=∫y​(0)z​(0)U(0,ξ)[θ3(ϕ−(x,ξ),ω1)−θ3(ϕ+(x,ξ),ω1)]dξ\displaystyle-F(\tau,x)\Big{]}=\int\_{y(0)}^{z(0)}U(0,\xi)\left[\theta\_{3}(\phi\_{-}(x,\xi),\omega\_{1})-\theta\_{3}(\phi\_{+}(x,\xi),\omega\_{1})\right]d\xi |  | (34) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ{[Ψ(s)−f−(s)y′(s)][θ3(ϕ−(x,y(s)),ω2)−θ3(ϕ+(x,y(s)),ω2)]\displaystyle+\int\_{0}^{\tau}\Bigg{\{}\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\left[\theta\_{3}(\phi\_{-}(x,y(s)),\omega\_{2})-\theta\_{3}(\phi\_{+}(x,y(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[Φ​(s)+f+​(s)​z′​(s)]​[θ3​(ϕ−​(x,z​(s)),ω2)−θ3​(ϕ+​(x,z​(s)),ω2)]delimited-[]Φ𝑠superscript𝑓𝑠superscript𝑧′𝑠delimited-[]subscript𝜃3subscriptitalic-ϕ𝑥𝑧𝑠subscript𝜔2subscript𝜃3subscriptitalic-ϕ𝑥𝑧𝑠subscript𝜔2\displaystyle+\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\left[\theta\_{3}(\phi\_{-}(x,z(s)),\omega\_{2})-\theta\_{3}(\phi\_{+}(x,z(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12[f+(s)[θ3′(ϕ−(x,z(s)),ω2)+θ3′(ϕ+(x,z(s)),ω2)]\displaystyle+\frac{1}{2}\Big{[}f^{+}(s)\left[\theta\_{3}^{\prime}(\phi\_{-}(x,z(s)),\omega\_{2})+\theta\_{3}^{\prime}(\phi\_{+}(x,z(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −f−(s)[θ3′(ϕ−(x,y(s)),ω2)+θ3′(ϕ+(x,y(s)),ω2)]]}ds.\displaystyle-f^{-}(s)\left[\theta\_{3}^{\prime}(\phi\_{-}(x,y(s)),\omega\_{2})+\theta\_{3}^{\prime}(\phi\_{+}(x,y(s)),\omega\_{2})\right]\Big{]}\Bigg{\}}ds. |  |

Note, that if rebates at hit are not paid, the boundary conditions become homogeneous, and all terms proportional to f−​(s)=f+​(s)=0superscript𝑓𝑠superscript𝑓𝑠0f^{-}(s)=f^{+}(s)=0 in Eq. ([34](#S2.E34 "Equation 34 ‣ 2.2 Connection to the Jacobi theta function ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) disappear.

### 2.3 Determining Ψ​(τ)Ψ𝜏\Psi(\tau) and Φ​(τ)Φ𝜏\Phi(\tau)

Taking the derivative in Eq. ([34](#S2.E34 "Equation 34 ‣ 2.2 Connection to the Jacobi theta function ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) with respect to x𝑥x, having in mind that according to Eq. ([32](#S2.E32 "Equation 32 ‣ 2.2 Connection to the Jacobi theta function ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂θ3​(ϕ±​(x,ξ),ω2)∂xsubscript𝜃3subscriptitalic-ϕplus-or-minus𝑥𝜉subscript𝜔2𝑥\displaystyle\frac{\partial\theta\_{3}(\phi\_{\pm}(x,\xi),\omega\_{2})}{\partial x} | =πl​(τ)​∂θ3​(y,ω2)∂y|y=ϕ±​(x,ξ)=πl​(τ)​θ3′​(ϕ±​(x,ξ),ω2),absentevaluated-at𝜋𝑙𝜏subscript𝜃3𝑦subscript𝜔2𝑦𝑦subscriptitalic-ϕplus-or-minus𝑥𝜉𝜋𝑙𝜏superscriptsubscript𝜃3′subscriptitalic-ϕplus-or-minus𝑥𝜉subscript𝜔2\displaystyle=\frac{\pi}{l(\tau)}\frac{\partial\theta\_{3}(y,\omega\_{2})}{\partial y}\Bigg{|}\_{y=\phi\_{\pm}(x,\xi)}=\frac{\pi}{l(\tau)}\theta\_{3}^{\prime}(\phi\_{\pm}(x,\xi),\omega\_{2}), |  | (35) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂2θ3​(ϕ±​(x,ξ),ω2)∂x2superscript2subscript𝜃3subscriptitalic-ϕplus-or-minus𝑥𝜉subscript𝜔2superscript𝑥2\displaystyle\frac{\partial^{2}\theta\_{3}(\phi\_{\pm}(x,\xi),\omega\_{2})}{\partial x^{2}} | =π2l2​(τ)​∂2θ3​(y,ω2)∂y2|y=ϕ±​(x,ξ)=π2l2​(τ)​θ3′′​(ϕ±​(x,ξ),ω2),absentevaluated-atsuperscript𝜋2superscript𝑙2𝜏superscript2subscript𝜃3𝑦subscript𝜔2superscript𝑦2𝑦subscriptitalic-ϕplus-or-minus𝑥𝜉superscript𝜋2superscript𝑙2𝜏superscriptsubscript𝜃3′′subscriptitalic-ϕplus-or-minus𝑥𝜉subscript𝜔2\displaystyle=\frac{\pi^{2}}{l^{2}(\tau)}\frac{\partial^{2}\theta\_{3}(y,\omega\_{2})}{\partial y^{2}}\Bigg{|}\_{y=\phi\_{\pm}(x,\xi)}=\frac{\pi^{2}}{l^{2}(\tau)}\theta\_{3}^{\prime\prime}(\phi\_{\pm}(x,\xi),\omega\_{2}), |  |

and substituting x=y​(τ)𝑥𝑦𝜏x=y(\tau) and x=z​(τ)𝑥𝑧𝜏x=z(\tau), we get a system of Volterra integral equations of the second kind to determine Ψ(τ,Φ(τ)\Psi(\tau,\Phi(\tau)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −2​l2​(τ)π[Ψ(τ)\displaystyle-\frac{2l^{2}(\tau)}{\pi}\Big{[}\Psi(\tau) | +Fx(τ,y(τ))]=∫y​(0)z​(0)U(0,ξ)[θ3′(ϕ−(y(τ),ξ),ω1)−θ3′(ϕ+(y(τ),ξ),ω1)]dξ\displaystyle+F\_{x}(\tau,y(\tau))\Big{]}=\int\_{y(0)}^{z(0)}U(0,\xi)\left[\theta^{\prime}\_{3}(\phi\_{-}(y(\tau),\xi),\omega\_{1})-\theta^{\prime}\_{3}(\phi\_{+}(y(\tau),\xi),\omega\_{1})\right]d\xi |  | (36) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ{[Ψ(s)−f−(s)y′(s)][θ3′(ϕ−(y(τ),y(s)),ω2)−θ3′(ϕ+(y(τ),y(s)),ω2)]\displaystyle+\int\_{0}^{\tau}\Bigg{\{}\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\left[\theta^{\prime}\_{3}(\phi\_{-}(y(\tau),y(s)),\omega\_{2})-\theta^{\prime}\_{3}(\phi\_{+}(y(\tau),y(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[Φ​(s)+f+​(s)​z′​(s)]​[θ3′​(ϕ−​(y​(τ),z​(s)),ω2)−θ3′​(ϕ+​(y​(τ),z​(s)),ω2)]delimited-[]Φ𝑠superscript𝑓𝑠superscript𝑧′𝑠delimited-[]subscriptsuperscript𝜃′3subscriptitalic-ϕ𝑦𝜏𝑧𝑠subscript𝜔2subscriptsuperscript𝜃′3subscriptitalic-ϕ𝑦𝜏𝑧𝑠subscript𝜔2\displaystyle+\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\left[\theta^{\prime}\_{3}(\phi\_{-}(y(\tau),z(s)),\omega\_{2})-\theta^{\prime}\_{3}(\phi\_{+}(y(\tau),z(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​πl​(τ)[f+(s)[θ3′′(ϕ−(y(τ),z(s)),ω2)+θ3′′(ϕ+(y(τ),z(s)),ω2)]\displaystyle+\frac{2\pi}{l(\tau)}\Big{[}f^{+}(s)\left[\theta\_{3}^{\prime\prime}(\phi\_{-}(y(\tau),z(s)),\omega\_{2})+\theta\_{3}^{\prime\prime}(\phi\_{+}(y(\tau),z(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −f−(s)[θ3′′(ϕ−(y(τ),y(s)),ω2)+θ3′′(ϕ+(y(τ),y(s)),ω2)]]}ds.\displaystyle-f^{-}(s)\left[\theta\_{3}^{\prime\prime}(\phi\_{-}(y(\tau),y(s)),\omega\_{2})+\theta\_{3}^{\prime\prime}(\phi\_{+}(y(\tau),y(s)),\omega\_{2})\right]\Big{]}\Bigg{\}}ds. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​l2​(τ)π[Φ(τ)\displaystyle\frac{2l^{2}(\tau)}{\pi}\Big{[}\Phi(\tau) | +Fx(τ,z(τ))]=∫y​(0)z​(0)U(0,ξ)[θ3′(ϕ−(z(τ),ξ),ω1)−θ3′(ϕ+(z(τ),ξ),ω1)]dξ\displaystyle+F\_{x}(\tau,z(\tau))\Big{]}=\int\_{y(0)}^{z(0)}U(0,\xi)\left[\theta^{\prime}\_{3}(\phi\_{-}(z(\tau),\xi),\omega\_{1})-\theta^{\prime}\_{3}(\phi\_{+}(z(\tau),\xi),\omega\_{1})\right]d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ{[Ψ(s)−f−(s)y′(s)][θ3′(ϕ−(z(τ),y(s)),ω2)−θ3′(ϕ+(z(τ),y(s)),ω2)]\displaystyle+\int\_{0}^{\tau}\Bigg{\{}\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\left[\theta^{\prime}\_{3}(\phi\_{-}(z(\tau),y(s)),\omega\_{2})-\theta^{\prime}\_{3}(\phi\_{+}(z(\tau),y(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[Φ​(s)+f+​(s)​z′​(s)]​[θ3′​(ϕ−​(z​(τ),z​(s)),ω2)−θ3′​(ϕ+​(z​(τ),z​(s)),ω2)]delimited-[]Φ𝑠superscript𝑓𝑠superscript𝑧′𝑠delimited-[]subscriptsuperscript𝜃′3subscriptitalic-ϕ𝑧𝜏𝑧𝑠subscript𝜔2subscriptsuperscript𝜃′3subscriptitalic-ϕ𝑧𝜏𝑧𝑠subscript𝜔2\displaystyle+\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\left[\theta^{\prime}\_{3}(\phi\_{-}(z(\tau),z(s)),\omega\_{2})-\theta^{\prime}\_{3}(\phi\_{+}(z(\tau),z(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​πl​(τ)[f+(s)[θ3′′(ϕ−(z(τ),z(s)),ω2)+θ3′′(ϕ+(z(τ),z(s)),ω2)]\displaystyle+\frac{2\pi}{l(\tau)}\Big{[}f^{+}(s)\left[\theta\_{3}^{\prime\prime}(\phi\_{-}(z(\tau),z(s)),\omega\_{2})+\theta\_{3}^{\prime\prime}(\phi\_{+}(z(\tau),z(s)),\omega\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −f−(s)[θ3′′(ϕ−(z(τ),y(s)),ω2)+θ3′′(ϕ+(z(τ),y(s)),ω2)]]}ds.\displaystyle-f^{-}(s)\left[\theta\_{3}^{\prime\prime}(\phi\_{-}(z(\tau),y(s)),\omega\_{2})+\theta\_{3}^{\prime\prime}(\phi\_{+}(z(\tau),y(s)),\omega\_{2})\right]\Big{]}\Bigg{\}}ds. |  |

Also, since the theta function θ3​(z,ω)subscript𝜃3𝑧𝜔\theta\_{3}(z,\omega) solves the heat equation

|  |  |  |
| --- | --- | --- |
|  | ∂θ3​(z,i​t)∂t=14​π​∂2θ3​(z,i​t)∂z2,subscript𝜃3𝑧i𝑡𝑡14𝜋superscript2subscript𝜃3𝑧i𝑡superscript𝑧2\frac{\partial\theta\_{3}(z,\mathrm{i}\mkern 1.0mut)}{\partial t}=\frac{1}{4\pi}\frac{\partial^{2}\theta\_{3}(z,\mathrm{i}\mkern 1.0mut)}{\partial z^{2}}, |  |

the second derivatives with respect to the first argument could be expressed via the first derivatives with respect to the second argument.

However, there exists a problem with the representation in Eq. ([36](#S2.E36 "Equation 36 ‣ 2.3 Determining Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Indeed, using the definition of F​(τ,x)𝐹𝜏𝑥F(\tau,x) in Eq. ([A.10](#A1.E10 "Equation A.10 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) it can be checked that the derivatives Fx​(τ,x)subscript𝐹𝑥𝜏𝑥F\_{x}(\tau,x) do not exist at x=y​(τ)𝑥𝑦𝜏x=y(\tau) and x=z​(τ)𝑥𝑧𝜏x=z(\tau) as they are proportional to the Dirac Delta δ​(0)𝛿0\delta(0). Therefore, in the next Section we attack this problem again using an alternative representation of the solution.

### 2.4 The Poisson summation formula and alternative representations

It is known that for the fixed spatial domain x∈[y​(τ),z​(τ)],y​(τ)=0,z​(τ)=c​o​n​s​tformulae-sequence𝑥𝑦𝜏𝑧𝜏formulae-sequence𝑦𝜏0𝑧𝜏𝑐𝑜𝑛𝑠𝑡x\in[y(\tau),z(\tau)],\ y(\tau)=0,\ z(\tau)=const there exist two representations of the solution of the heat equation: one - obtained by using the method of images, and the other one - by the Fourier series. Both solutions are equal in a sense of infinite series, but their convergence properties are different, see eg., (Lipton, [2002](#bib.bib22)). It turns out that for a curvilinear strip we can also obtain an alternative representation.

The solution u​(τ,x)𝑢𝜏𝑥u(\tau,x) found in Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) already has the form of the Fourier series. However, applicability of the method of images for the problem Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) is not transparent due to time-dependency of the boundaries. Instead, we can find an alternative representation by using the following property known as the Poisson Summation formula, (van der Pol and Bremmer, [1950](#bib.bib33))

###### Proposition 2.1 (Poisson Summation formula).

Let h^​(ν)^ℎ𝜈\hat{h}(\nu) be the Fourier transform of the appropriate function h​(x)ℎ𝑥h(x)

|  |  |  |
| --- | --- | --- |
|  | h^​(ν)=∫−∞∞h​(x)​e−2​π​i​ν​x​𝑑x.^ℎ𝜈superscriptsubscriptℎ𝑥superscript𝑒2𝜋i𝜈𝑥differential-d𝑥\hat{h}(\nu)=\int\_{-\infty}^{\infty}h(x)e^{-2\pi\mathrm{i}\mkern 1.0mu\nu x}dx. |  |

The following identity holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=−∞∞h​(n)=∑k=−∞∞h^​(k).superscriptsubscript𝑛ℎ𝑛superscriptsubscript𝑘^ℎ𝑘\sum\_{n=-\infty}^{\infty}h(n)=\sum\_{k=-\infty}^{\infty}\hat{h}(k). |  | (37) |

###### Proof.

See (van der Pol and Bremmer, [1950](#bib.bib33)).
∎

Applying Eq. ([37](#S2.E37 "Equation 37 ‣ Proposition 2.1 (Poisson Summation formula). ‣ 2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) to the functions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h1​(x)subscriptℎ1𝑥\displaystyle h\_{1}(x) | =e−π2​x22​cos⁡(π​x​α),absentsuperscript𝑒superscript𝜋2superscript𝑥22𝜋𝑥𝛼\displaystyle=e^{-\frac{\pi^{2}x^{2}}{2}}\cos\left(\pi x\alpha\right),\qquad | h^1​(ν)=∫−∞∞e−π2​x22​β−2​π​i​ν​x​cos⁡(π​x​α)​𝑑x,subscript^ℎ1𝜈superscriptsubscriptsuperscript𝑒superscript𝜋2superscript𝑥22𝛽2𝜋i𝜈𝑥𝜋𝑥𝛼differential-d𝑥\displaystyle\hat{h}\_{1}(\nu)=\int\_{-\infty}^{\infty}e^{-\frac{\pi^{2}x^{2}}{2\beta}-2\pi\mathrm{i}\mkern 1.0mu\nu x}\cos\left(\pi x\alpha\right)dx, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h2​(x)subscriptℎ2𝑥\displaystyle h\_{2}(x) | =x​e−π2​x22​β​sin⁡(π​x​α),absent𝑥superscript𝑒superscript𝜋2superscript𝑥22𝛽𝜋𝑥𝛼\displaystyle=xe^{-\frac{\pi^{2}x^{2}}{2\beta}}\sin\left(\pi x\alpha\right),\qquad | h^2​(ν)=∫−∞∞x​e−π2​x22​β−2​π​i​ν​x​sin⁡(π​x​α)​𝑑x,subscript^ℎ2𝜈superscriptsubscript𝑥superscript𝑒superscript𝜋2superscript𝑥22𝛽2𝜋i𝜈𝑥𝜋𝑥𝛼differential-d𝑥\displaystyle\hat{h}\_{2}(\nu)=\int\_{-\infty}^{\infty}xe^{-\frac{\pi^{2}x^{2}}{2\beta}-2\pi\mathrm{i}\mkern 1.0mu\nu x}\sin\left(\pi x\alpha\right)dx, |  |

we obtain the following identities

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑n=−∞∞e−π2​n22​β​cos⁡(π​n​α)superscriptsubscript𝑛superscript𝑒superscript𝜋2superscript𝑛22𝛽𝜋𝑛𝛼\displaystyle\sum\_{n=-\infty}^{\infty}e^{-\frac{\pi^{2}n^{2}}{2\beta}}\cos\left(\pi n\alpha\right) | =2​βπ​e−α2​β2​∑n=−∞∞e−2​n2​β​cosh⁡(2​n​α​β)absent2𝛽𝜋superscript𝑒superscript𝛼2𝛽2superscriptsubscript𝑛superscript𝑒2superscript𝑛2𝛽2𝑛𝛼𝛽\displaystyle=\sqrt{\frac{2\beta}{\pi}}e^{-\frac{\alpha^{2}\beta}{2}}\sum\_{n=-\infty}^{\infty}e^{-2n^{2}\beta}\cosh\left(2n\alpha\beta\right) |  | (38) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =β2​π​∑n=−∞∞[e−β2​(2​n−α)2+e−β2​(2​n+α)2]=2​β2​π​∑n=−∞∞e−β2​(2​n+α)2,absent𝛽2𝜋superscriptsubscript𝑛delimited-[]superscript𝑒𝛽2superscript2𝑛𝛼2superscript𝑒𝛽2superscript2𝑛𝛼22𝛽2𝜋superscriptsubscript𝑛superscript𝑒𝛽2superscript2𝑛𝛼2\displaystyle=\sqrt{\frac{\beta}{2\pi}}\sum\_{n=-\infty}^{\infty}\left[e^{-\frac{\beta}{2}\left(2n-\alpha\right)^{2}}+e^{-\frac{\beta}{2}\left(2n+\alpha\right)^{2}}\right]=2\sqrt{\frac{\beta}{2\pi}}\sum\_{n=-\infty}^{\infty}e^{-\frac{\beta}{2}\left(2n+\alpha\right)^{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=−∞∞π​n​e−π2​n22​β​sin⁡(π​n​α)superscriptsubscript𝑛𝜋𝑛superscript𝑒superscript𝜋2superscript𝑛22𝛽𝜋𝑛𝛼\displaystyle\sum\_{n=-\infty}^{\infty}\pi ne^{-\frac{\pi^{2}n^{2}}{2\beta}}\sin\left(\pi n\alpha\right) | =β3/22​π​∑n=−∞∞e−β2​(2​n+α)2​[α+2​n+(α−2​n)​e4​α​β​n]absentsuperscript𝛽322𝜋superscriptsubscript𝑛superscript𝑒𝛽2superscript2𝑛𝛼2delimited-[]𝛼2𝑛𝛼2𝑛superscript𝑒4𝛼𝛽𝑛\displaystyle=\frac{\beta^{3/2}}{\sqrt{2\pi}}\sum\_{n=-\infty}^{\infty}e^{-\frac{\beta}{2}\left(2n+\alpha\right)^{2}}\left[\alpha+2n+(\alpha-2n)e^{4\alpha\beta n}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =β3/22​π​∑n=−∞∞[e−β2​(2​n+α)2​(α+2​n)+e−β2​(2​n−α)2​(α−2​n)]absentsuperscript𝛽322𝜋superscriptsubscript𝑛delimited-[]superscript𝑒𝛽2superscript2𝑛𝛼2𝛼2𝑛superscript𝑒𝛽2superscript2𝑛𝛼2𝛼2𝑛\displaystyle=\frac{\beta^{3/2}}{\sqrt{2\pi}}\sum\_{n=-\infty}^{\infty}\left[e^{-\frac{\beta}{2}\left(2n+\alpha\right)^{2}}(\alpha+2n)+e^{-\frac{\beta}{2}\left(2n-\alpha\right)^{2}}(\alpha-2n)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​β3/22​π​∑n=−∞∞e−β2​(2​n+α)2​(α+2​n).absent2superscript𝛽322𝜋superscriptsubscript𝑛superscript𝑒𝛽2superscript2𝑛𝛼2𝛼2𝑛\displaystyle=2\frac{\beta^{3/2}}{\sqrt{2\pi}}\sum\_{n=-\infty}^{\infty}e^{-\frac{\beta}{2}\left(2n+\alpha\right)^{2}}(\alpha+2n). |  |

Since each summand in Eq. ([30](#S2.E30 "Equation 30 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) can be represented in the form of the LHS of Eq. ([38](#S2.E38 "Equation 38 ‣ 2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), by using a simple trigonometric formula for the product of sines, we immediately arrive at another form of U​(τ,x)𝑈𝜏𝑥U(\tau,x), see Appendix [B](#A2 "Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(τ,x)𝑈𝜏𝑥\displaystyle U(\tau,x) | =∑n=−∞∞{∫y​(0)z​(0)U(0,ξ)Υn(x,τ|ξ,0)dξ+∫0τ[Φ(s)+f+(s)z′(s)]Υn(x,τ|z(s),s)ds,\displaystyle=\sum\_{n=-\infty}^{\infty}\Bigg{\{}\int\_{y(0)}^{z(0)}U(0,\xi)\Upsilon\_{n}(x,\tau\,|\,\xi,0)d\xi+\int\_{0}^{\tau}\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\Upsilon\_{n}(x,\tau|z(s),s)ds, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0τ[Ψ​(s)−f−​(s)​y′​(s)]​Υn​(x,τ|y​(s),s)​𝑑ssuperscriptsubscript0𝜏delimited-[]Ψ𝑠superscript𝑓𝑠superscript𝑦′𝑠subscriptΥ𝑛𝑥conditional𝜏  𝑦𝑠𝑠differential-d𝑠\displaystyle\qquad+\int\_{0}^{\tau}\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\Upsilon\_{n}(x,\tau\,|\,y(s),s)ds |  | (39) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τf−(s)Λn(x,τ|y(s),s)−f+(s)Λn(x,τ|z(s),s)ds},\displaystyle\qquad+\int\_{0}^{\tau}f^{-}(s)\Lambda\_{n}(x,\tau\,|\,y(s),s)-f^{+}(s)\Lambda\_{n}(x,\tau\,|\,z(s),s)ds\Bigg{\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ΥnsubscriptΥ𝑛\displaystyle\Upsilon\_{n} | (x,τ|ξ,s)=12​π​(τ−s)​[e−(2​n​l​(τ)+x−ξ)24​(τ−s)−e−(2​n​l​(τ)+x+ξ−2​y​(τ))24​(τ−s)],𝑥conditional𝜏  𝜉𝑠12𝜋𝜏𝑠delimited-[]superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉24𝜏𝑠superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉2𝑦𝜏24𝜏𝑠\displaystyle(x,\tau\,|\,\xi,s)=\frac{1}{2\sqrt{\pi(\tau-s)}}\left[e^{-\frac{(2nl(\tau)+x-\xi)^{2}}{4(\tau-s)}}-e^{-\frac{(2nl(\tau)+x+\xi-2y(\tau))^{2}}{4(\tau-s)}}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ΛnsubscriptΛ𝑛\displaystyle\Lambda\_{n} | (x,τ|ξ,s)=x−ξ+2​n​l​(τ)4​π​(τ−s)3​e−(2​n​l​(τ)+x−ξ)24​(τ−s)+x+ξ−2​y​(τ)+2​n​l​(τ)4​π​(τ−s)3​e−(2​n​l​(τ)+x+ξ−2​y​(τ))24​(τ−s).𝑥conditional𝜏  𝜉𝑠𝑥𝜉2𝑛𝑙𝜏4𝜋superscript𝜏𝑠3superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉24𝜏𝑠𝑥𝜉2𝑦𝜏2𝑛𝑙𝜏4𝜋superscript𝜏𝑠3superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉2𝑦𝜏24𝜏𝑠\displaystyle(x,\tau\,|\,\xi,s)=\frac{x-\xi+2nl(\tau)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(2nl(\tau)+x-\xi)^{2}}{4(\tau-s)}}+\frac{x+\xi-2y(\tau)+2nl(\tau)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(2nl(\tau)+x+\xi-2y(\tau))^{2}}{4(\tau-s)}}. |  |

Note that the Fourier series in these expressions usually converge rapidly when n𝑛n grows. Similarly, taking the derivative of this series on x𝑥x provides a convenient way of calculating the corresponding derivative ∂U​(τ,x)∂x𝑈𝜏𝑥𝑥\frac{\partial U(\tau,x)}{\partial x}, ([DLMF,](#bib.bib8) ).

### 2.5 A system of Volterra equations for Ψ​(τ)Ψ𝜏\Psi(\tau) and Φ​(τ)Φ𝜏\Phi(\tau)

In Section [2.4](#S2.SS4 "2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit") we managed to obtain two alternative representations of the solution of the problem, both in a semi-analytical form. These solutions, however, depend on two yet unknown functions gradients Ψ​(τ),Φ​(τ)

Ψ𝜏Φ𝜏\Psi(\tau),\Phi(\tau) that can be found by solving a system of two Volterra equations of the second kind. These equations are obtained by taking the derivative in Eq. ([30](#S2.E30 "Equation 30 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) or Eq. ([2.4](#S2.Ex55 "2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) with respect to x𝑥x and substituting x=y​(τ)𝑥𝑦𝜏x=y(\tau) and x=z​(τ)𝑥𝑧𝜏x=z(\tau) into thus found expressions. However, at least formally there exist a problem with making the last step, because at these boundaries some integrals in the system of the Volterra equations will contain singularities. Below we describe the resolution of these problems.

Let us again consider Eq. ([2.4](#S2.Ex55 "2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). It is easy to see that the functions ∂Υn​(x,τ|ξ,s)∂xsubscriptΥ𝑛𝑥conditional𝜏

𝜉𝑠𝑥\frac{\partial\Upsilon\_{n}(x,\tau|\xi,s)}{\partial x}, ∂Λn​(x,τ|ξ,s)∂xsubscriptΛ𝑛𝑥conditional𝜏

𝜉𝑠𝑥\frac{\partial\Lambda\_{n}(x,\tau|\xi,s)}{\partial x} are regular only if n≠0,x∈[y​(τ),z​(τ)],ξ∈[y​(s),z​(s)],s→τformulae-sequence𝑛0formulae-sequence𝑥𝑦𝜏𝑧𝜏formulae-sequence𝜉𝑦𝑠𝑧𝑠→𝑠𝜏n\neq 0,\ x\in[y(\tau),z(\tau)],\ \xi\in[y(s),z(s)],\ s\to\tau. At n=0𝑛0n=0 functions ∂Υ0​(x,τ|y​(s),s)∂xsubscriptΥ0𝑥conditional𝜏

𝑦𝑠𝑠𝑥\frac{\partial\Upsilon\_{0}(x,\tau|y(s),s)}{\partial x}, ∂Λ0​(x,τ|y​(s),s)∂xsubscriptΛ0𝑥conditional𝜏

𝑦𝑠𝑠𝑥\frac{\partial\Lambda\_{0}(x,\tau|y(s),s)}{\partial x} have a singularity when s→τ,x→y​(τ)formulae-sequence→𝑠𝜏→𝑥𝑦𝜏s\to\tau,\ x\to y(\tau), and functions ∂Υ0​(x,τ|z​(s),s)∂x,∂Λ0​(x,τ|z​(s),s)∂x

subscriptΥ0𝑥conditional𝜏

𝑧𝑠𝑠𝑥subscriptΛ0𝑥conditional𝜏

𝑧𝑠𝑠𝑥\frac{\partial\Upsilon\_{0}(x,\tau|z(s),s)}{\partial x},\frac{\partial\Lambda\_{0}(x,\tau|z(s),s)}{\partial x} - when s→τ,x→z​(τ)formulae-sequence→𝑠𝜏→𝑥𝑧𝜏s\to\tau,\ x\to z(\tau).

Since the functions ∂Υ0(x,τ|y(s),s∂x\frac{\partial\Upsilon\_{0}(x,\tau|y(s),s}{\partial x}, ∂Υ0(x,τ|z(s),s∂x\frac{\partial\Upsilon\_{0}(x,\tau|z(s),s}{\partial x} can be represented as a sum of double-layer potentials with a negative sign, the limiting values

|  |  |  |
| --- | --- | --- |
|  | limx→y​(τ)+0∫0τξ​(s)​∂Υ0​(x,τ|y​(s),s)∂x​𝑑s,limx→z​(τ)−0∫0τξ​(s)​∂Υ0​(x,τ|z​(s),s)∂x​𝑑s  subscript→𝑥𝑦𝜏0superscriptsubscript0𝜏𝜉𝑠subscriptΥ0𝑥conditional𝜏  𝑦𝑠𝑠𝑥differential-d𝑠subscript→𝑥𝑧𝜏0superscriptsubscript0𝜏𝜉𝑠subscriptΥ0𝑥conditional𝜏  𝑧𝑠𝑠𝑥differential-d𝑠\lim\_{x\to y(\tau)+0}\int\_{0}^{\tau}\xi(s)\frac{\partial\Upsilon\_{0}(x,\tau|y(s),s)}{\partial x}ds,\qquad\lim\_{x\to z(\tau)-0}\int\_{0}^{\tau}\xi(s)\frac{\partial\Upsilon\_{0}(x,\tau|z(s),s)}{\partial x}ds |  |

can be computed similar to Eq. ([B.8](#A2.E8 "Equation B.8 ‣ B.1 The limiting values 𝑥→𝑦⁢(𝜏) and 𝑥→𝑧⁢(𝜏) in Eq. () ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")).

Applying Eq. ([73](#S3.E73 "Equation 73 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) to the limits corresponding to ∂Λ0​(x,τ|y​(s),s)∂x,∂Λ0​(x,τ|z​(s),s)∂x

subscriptΛ0𝑥conditional𝜏

𝑦𝑠𝑠𝑥subscriptΛ0𝑥conditional𝜏

𝑧𝑠𝑠𝑥\frac{\partial\Lambda\_{0}(x,\tau|y(s),s)}{\partial x},\frac{\partial\Lambda\_{0}(x,\tau|z(s),s)}{\partial x} yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limx→y​(τ)+0subscript→𝑥𝑦𝜏0\displaystyle\lim\_{x\to y(\tau)+0} | ∫0τf−​(s)​∂Λ0​(x,τ|y​(s),s)∂x​𝑑ssuperscriptsubscript0𝜏superscript𝑓𝑠subscriptΛ0𝑥conditional𝜏  𝑦𝑠𝑠𝑥differential-d𝑠\displaystyle\int\_{0}^{\tau}f^{-}(s)\frac{\partial\Lambda\_{0}(x,\tau|y(s),s)}{\partial x}ds |  | (40) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−f−​(τ)π​τ+∫0τf−​(s)​e−(y​(τ)−y​(s))24​(τ−s)−f−​(τ)2​π​(τ−s)3​𝑑s−∫0τf−​(s)​(y​(τ)−y​(s))2​e−(y​(τ)−y​(s))24​(τ−s)4​π​(τ−s)5​𝑑s,absentsuperscript𝑓𝜏𝜋𝜏superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑒superscript𝑦𝜏𝑦𝑠24𝜏𝑠superscript𝑓𝜏2𝜋superscript𝜏𝑠3differential-d𝑠superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑦𝜏𝑦𝑠2superscript𝑒superscript𝑦𝜏𝑦𝑠24𝜏𝑠4𝜋superscript𝜏𝑠5differential-d𝑠\displaystyle=-\frac{f^{-}(\tau)}{\sqrt{\pi\tau}}+\int\_{0}^{\tau}\frac{f^{-}(s)e^{-\frac{(y(\tau)-y(s))^{2}}{4(\tau-s)}}-f^{-}(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}ds-\int\_{0}^{\tau}f^{-}(s)\frac{(y(\tau)-y(s))^{2}e^{-\frac{(y(\tau)-y(s))^{2}}{4(\tau-s)}}}{4\sqrt{\pi(\tau-s)^{5}}}ds, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→z​(τ)−0subscript→𝑥𝑧𝜏0\displaystyle\lim\_{x\to z(\tau)-0} | ∫0τf+​(s)​∂Λ0​(x,τ|z​(s),s)∂x​𝑑ssuperscriptsubscript0𝜏superscript𝑓𝑠subscriptΛ0𝑥conditional𝜏  𝑧𝑠𝑠𝑥differential-d𝑠\displaystyle\int\_{0}^{\tau}f^{+}(s)\frac{\partial\Lambda\_{0}(x,\tau|z(s),s)}{\partial x}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−f+​(τ)π​τ+∫0τf+​(s)​e−(z​(τ)−z​(s))24​(τ−s)−f+​(τ)2​π​(τ−s)3​𝑑s−∫0τf+​(s)​(z​(τ)−z​(s))2​e−(z​(τ)−z​(s))24​(τ−s)4​π​(τ−s)5​𝑑s.absentsuperscript𝑓𝜏𝜋𝜏superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑒superscript𝑧𝜏𝑧𝑠24𝜏𝑠superscript𝑓𝜏2𝜋superscript𝜏𝑠3differential-d𝑠superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑧𝜏𝑧𝑠2superscript𝑒superscript𝑧𝜏𝑧𝑠24𝜏𝑠4𝜋superscript𝜏𝑠5differential-d𝑠\displaystyle=-\frac{f^{+}(\tau)}{\sqrt{\pi\tau}}+\int\_{0}^{\tau}\frac{f^{+}(s)e^{-\frac{(z(\tau)-z(s))^{2}}{4(\tau-s)}}-f^{+}(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}ds-\int\_{0}^{\tau}f^{+}(s)\frac{(z(\tau)-z(s))^{2}e^{-\frac{(z(\tau)-z(s))^{2}}{4(\tau-s)}}}{4\sqrt{\pi(\tau-s)^{5}}}ds. |  |

Finally, taking the derivative of Eq. ([2.4](#S2.Ex55 "2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) on x𝑥x, setting x=y​(τ)𝑥𝑦𝜏x=y(\tau) and x=z​(τ)𝑥𝑧𝜏x=z(\tau), and using
these expressions, we obtain the following system of the Volterra equations of the second kind for the unknown functions Ψ​(τ),Φ​(τ)

Ψ𝜏Φ𝜏\Psi(\tau),\Phi(\tau)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −Ψ​(τ)Ψ𝜏\displaystyle-\Psi(\tau) | =−f−​(τ)π​τ+∫0τf−(s)e−(y​(τ)−y​(s))24​(τ−s)[1+y′(s)(y(τ)−y(s)))−(y​(τ)−y​(s))22​(τ−s)]−f−(τ)2​π​(τ−s)3​𝑑s\displaystyle=-\frac{f^{-}(\tau)}{\sqrt{\pi\tau}}+\int\_{0}^{\tau}\frac{f^{-}(s)e^{-\frac{(y(\tau)-y(s))^{2}}{4(\tau-s)}}\left[1+y^{\prime}(s)(y(\tau)-y(s)))-\frac{(y(\tau)-y(s))^{2}}{2(\tau-s)}\right]-f^{-}(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}ds |  | (41) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0τΨ​(s)​y​(τ)−y​(s)2​π​(τ−s)3​e−(y​(τ)−y​(s))24​(τ−s)​𝑑s+∫y​(0)z​(0)U​(0,ξ)​υ−​(τ|ξ,0)​𝑑ξsuperscriptsubscript0𝜏Ψ𝑠𝑦𝜏𝑦𝑠2𝜋superscript𝜏𝑠3superscript𝑒superscript𝑦𝜏𝑦𝑠24𝜏𝑠differential-d𝑠superscriptsubscript𝑦0𝑧0𝑈0𝜉superscript𝜐conditional𝜏  𝜉0differential-d𝜉\displaystyle-\int\_{0}^{\tau}\Psi(s)\frac{y(\tau)-y(s)}{2\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(y(\tau)-y(s))^{2}}{4(\tau-s)}}ds+\int\_{y(0)}^{z(0)}U(0,\xi)\upsilon^{-}(\tau\,|\,\xi,0)d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ([Φ​(s)+f+​(s)​z′​(s)]​υ−​(τ|z​(s),s)+[Ψ​(s)−f−​(s)​y′​(s)]​υ0−​(τ|y​(s),s))​𝑑ssuperscriptsubscript0𝜏delimited-[]Φ𝑠superscript𝑓𝑠superscript𝑧′𝑠superscript𝜐conditional𝜏  𝑧𝑠𝑠delimited-[]Ψ𝑠superscript𝑓𝑠superscript𝑦′𝑠subscriptsuperscript𝜐0conditional𝜏  𝑦𝑠𝑠differential-d𝑠\displaystyle+\int\_{0}^{\tau}\left(\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\upsilon^{-}(\tau\,|\,z(s),s)+\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\upsilon^{-}\_{0}(\tau\,|\,y(s),s)\right)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ(f−(s)λ0−(τ,|y(s),s)−f+(s)λ−(τ,|z(s),s))ds,\displaystyle+\int\_{0}^{\tau}\left(f^{-}(s)\lambda^{-}\_{0}(\tau,\,|\,y(s),s)-f^{+}(s)\lambda^{-}(\tau,\,|\,z(s),s)\right)ds, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(τ)Φ𝜏\displaystyle\Phi(\tau) | =f+​(τ)π​τ−∫0τf+​(s)​e−(z​(τ)−z​(s))24​(τ−s)​[1+z′​(s)​(z​(τ)−z​(s))−(z​(τ)−z​(s))22​(τ−s)]−f+​(τ)2​π​(τ−s)3​𝑑sabsentsuperscript𝑓𝜏𝜋𝜏superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑒superscript𝑧𝜏𝑧𝑠24𝜏𝑠delimited-[]1superscript𝑧′𝑠𝑧𝜏𝑧𝑠superscript𝑧𝜏𝑧𝑠22𝜏𝑠superscript𝑓𝜏2𝜋superscript𝜏𝑠3differential-d𝑠\displaystyle=\frac{f^{+}(\tau)}{\sqrt{\pi\tau}}-\int\_{0}^{\tau}\frac{f^{+}(s)e^{-\frac{(z(\tau)-z(s))^{2}}{4(\tau-s)}}\left[1+z^{\prime}(s)(z(\tau)-z(s))-\frac{(z(\tau)-z(s))^{2}}{2(\tau-s)}\right]-f^{+}(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0τΦ​(s)​z​(τ)−z​(s)2​π​(τ−s)3​e−(z​(τ)−z​(s))24​(τ−s)​𝑑s+∫y​(0)z​(0)U​(0,ξ)​υ+​(τ|ξ,0)​𝑑ξsuperscriptsubscript0𝜏Φ𝑠𝑧𝜏𝑧𝑠2𝜋superscript𝜏𝑠3superscript𝑒superscript𝑧𝜏𝑧𝑠24𝜏𝑠differential-d𝑠superscriptsubscript𝑦0𝑧0𝑈0𝜉superscript𝜐conditional𝜏  𝜉0differential-d𝜉\displaystyle-\int\_{0}^{\tau}\Phi(s)\frac{z(\tau)-z(s)}{2\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(z(\tau)-z(s))^{2}}{4(\tau-s)}}ds+\int\_{y(0)}^{z(0)}U(0,\xi)\upsilon^{+}(\tau\,|\,\xi,0)d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ([Φ​(s)+f+​(s)​z′​(s)]​υ0+​(τ|z​(s),s)+[Ψ​(s)−f−​(s)​y′​(s)]​υ+​(τ|y​(s),s)​d​s)superscriptsubscript0𝜏delimited-[]Φ𝑠superscript𝑓𝑠superscript𝑧′𝑠subscriptsuperscript𝜐0conditional𝜏  𝑧𝑠𝑠delimited-[]Ψ𝑠superscript𝑓𝑠superscript𝑦′𝑠superscript𝜐conditional𝜏  𝑦𝑠𝑠𝑑𝑠\displaystyle+\int\_{0}^{\tau}\left(\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\upsilon^{+}\_{0}(\tau\,|\,z(s),s)+\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\upsilon^{+}(\tau\,|\,y(s),s)ds\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ(f−​(s)​λ+​(τ|y​(s),s)−f+​(s)​λ0+​(τ|s))​𝑑s.superscriptsubscript0𝜏superscript𝑓𝑠superscript𝜆conditional𝜏  𝑦𝑠𝑠superscript𝑓𝑠subscriptsuperscript𝜆0conditional𝜏𝑠differential-d𝑠\displaystyle+\int\_{0}^{\tau}\left(f^{-}(s)\lambda^{+}(\tau\,|\,y(s),s)-f^{+}(s)\lambda^{+}\_{0}(\tau\,|\,s)\right)ds. |  |

Here

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | υn​(τ|ξ,s)subscript𝜐𝑛conditional𝜏  𝜉𝑠\displaystyle\upsilon\_{n}(\tau\,|\,\xi,s) | =−y​(τ)−ξ+2​n​l​(τ)2​π​(τ−s)3​e−(y​(τ)−ξ+2​n​l​(τ))24​(τ−s),absent𝑦𝜏𝜉2𝑛𝑙𝜏2𝜋superscript𝜏𝑠3superscript𝑒superscript𝑦𝜏𝜉2𝑛𝑙𝜏24𝜏𝑠\displaystyle=-\frac{y(\tau)-\xi+2nl(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(y(\tau)-\xi+2nl(\tau))^{2}}{4(\tau-s)}}, |  | (42) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λn​(τ|ξ,s)subscript𝜆𝑛conditional𝜏  𝜉𝑠\displaystyle\lambda\_{n}(\tau\,|\,\xi,s) | =e−(y​(τ)−ξ+2​n​l​(τ))24​(τ−s)2​π​(τ−s)3​[1−(y​(τ)−ξ+2​n​l​(τ))22​(τ−s)],absentsuperscript𝑒superscript𝑦𝜏𝜉2𝑛𝑙𝜏24𝜏𝑠2𝜋superscript𝜏𝑠3delimited-[]1superscript𝑦𝜏𝜉2𝑛𝑙𝜏22𝜏𝑠\displaystyle=\frac{e^{-\frac{(y(\tau)-\xi+2nl(\tau))^{2}}{4(\tau-s)}}}{2\sqrt{\pi(\tau-s)^{3}}}\left[1-\frac{(y(\tau)-\xi+2nl(\tau))^{2}}{2(\tau-s)}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ−​(τ|ξ,s)superscript𝜐conditional𝜏  𝜉𝑠\displaystyle\upsilon^{-}(\tau\,|\,\xi,s) | =∑n=−∞∞υn​(τ|ξ,s),υ+​(τ|ξ,s)=∑n=−∞∞υn+12​(τ|ξ,s),formulae-sequenceabsentsuperscriptsubscript𝑛subscript𝜐𝑛conditional𝜏  𝜉𝑠superscript𝜐conditional𝜏  𝜉𝑠superscriptsubscript𝑛subscript𝜐𝑛12conditional𝜏  𝜉𝑠\displaystyle=\sum\_{n=-\infty}^{\infty}\upsilon\_{n}(\tau\,|\,\xi,s),\qquad\upsilon^{+}(\tau\,|\,\xi,s)=\sum\_{n=-\infty}^{\infty}\upsilon\_{n+\frac{1}{2}}(\tau\,|\,\xi,s), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ0−​(τ|s)subscriptsuperscript𝜐0conditional𝜏𝑠\displaystyle\upsilon^{-}\_{0}(\tau\,|\,s) | =∑n=−∞n≠0∞υn​(τ|y​(s),s),υ0+​(τ|s)=∑n=−∞n≠0∞υn+12​(τ|z​(s),s),formulae-sequenceabsentsuperscriptsubscript  𝑛𝑛0subscript𝜐𝑛conditional𝜏  𝑦𝑠𝑠subscriptsuperscript𝜐0conditional𝜏𝑠superscriptsubscript  𝑛𝑛0subscript𝜐𝑛12conditional𝜏  𝑧𝑠𝑠\displaystyle=\sum\_{\begin{subarray}{c}n=-\infty\\ n\neq 0\end{subarray}}^{\infty}\upsilon\_{n}(\tau\,|\,y(s),s),\qquad\upsilon^{+}\_{0}(\tau\,|\,s)=\sum\_{\begin{subarray}{c}n=-\infty\\ n\neq 0\end{subarray}}^{\infty}\upsilon\_{n+\frac{1}{2}}(\tau\,|\,z(s),s), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λ−​(τ|ξ,s)superscript𝜆conditional𝜏  𝜉𝑠\displaystyle\lambda^{-}(\tau\,|\,\xi,s) | =∑n=−∞∞λn​(τ|ξ,s),λ+​(τ|ξ,s)=∑n=−∞∞λn+12​(τ|ξ,s),formulae-sequenceabsentsuperscriptsubscript𝑛subscript𝜆𝑛conditional𝜏  𝜉𝑠superscript𝜆conditional𝜏  𝜉𝑠superscriptsubscript𝑛subscript𝜆𝑛12conditional𝜏  𝜉𝑠\displaystyle=\sum\_{n=-\infty}^{\infty}\lambda\_{n}(\tau\,|\,\xi,s),\qquad\lambda^{+}(\tau\,|\,\xi,s)=\sum\_{n=-\infty}^{\infty}\lambda\_{n+\frac{1}{2}}(\tau\,|\,\xi,s), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λ0−​(τ|s)subscriptsuperscript𝜆0conditional𝜏𝑠\displaystyle\lambda^{-}\_{0}(\tau\,|\,s) | =∑n=−∞n≠0∞λn​(τ|y​(s),s),λ0+​(τ|s)=∑n=−∞n≠0∞λn+12​(τ|z​(s),s).formulae-sequenceabsentsuperscriptsubscript  𝑛𝑛0subscript𝜆𝑛conditional𝜏  𝑦𝑠𝑠subscriptsuperscript𝜆0conditional𝜏𝑠superscriptsubscript  𝑛𝑛0subscript𝜆𝑛12conditional𝜏  𝑧𝑠𝑠\displaystyle=\sum\_{\begin{subarray}{c}n=-\infty\\ n\neq 0\end{subarray}}^{\infty}\lambda\_{n}(\tau\,|\,y(s),s),\qquad\lambda^{+}\_{0}(\tau\,|\,s)=\sum\_{\begin{subarray}{c}n=-\infty\\ n\neq 0\end{subarray}}^{\infty}\lambda\_{n+\frac{1}{2}}(\tau\,|\,z(s),s). |  |

It is worth emphasizing that all summands in Eq. ([41](#S2.E41 "Equation 41 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) are regular. The integrals with respect to the time in the first two lines have weak (integrable) singularities, while other summands are regular.

This system can be further simplified by using Eq. ([71](#S3.E71 "Equation 71 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and reduction to the Lebesgue-Stieltjes integrals

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −Ψ​(τ)Ψ𝜏\displaystyle-\Psi(\tau) | =∫y​(0)z​(0)U​(0,ξ)​υ−​(τ|ξ,0)​𝑑ξabsentsuperscriptsubscript𝑦0𝑧0𝑈0𝜉superscript𝜐conditional𝜏  𝜉0differential-d𝜉\displaystyle=\int\_{y(0)}^{z(0)}U(0,\xi)\upsilon^{-}(\tau\,|\,\xi,0)d\xi |  | (43) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −f−​(τ)π​τ+∫0τf−​(s)−f−​(τ)2​π​(τ−s)3​𝑑s+∫0τ[f−​(s)​d​(η−​(τ|y​(s),s))−f+​(s)​d​(η−​(τ|z​(s),s))]superscript𝑓𝜏𝜋𝜏superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑓𝜏2𝜋superscript𝜏𝑠3differential-d𝑠superscriptsubscript0𝜏delimited-[]superscript𝑓𝑠𝑑superscript𝜂conditional𝜏  𝑦𝑠𝑠superscript𝑓𝑠𝑑superscript𝜂conditional𝜏  𝑧𝑠𝑠\displaystyle-\frac{f^{-}(\tau)}{\sqrt{\pi\tau}}+\int\_{0}^{\tau}\frac{f^{-}(s)-f^{-}(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}ds+\int\_{0}^{\tau}\left[f^{-}(s)d\left(\eta^{-}(\tau\,|\,y(s),s)\right)-f^{+}(s)d\left(\eta^{-}(\tau\,|\,z(s),s)\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0τΨ​(s)​y​(τ)−y​(s)2​π​(τ−s)3​e−(y​(τ)−y​(s))24​(τ−s)​𝑑s+∫0τ[Φ​(s)​υ−​(τ|z​(s),s)+Ψ​(s)​υ0−​(τ|s)]​𝑑ssuperscriptsubscript0𝜏Ψ𝑠𝑦𝜏𝑦𝑠2𝜋superscript𝜏𝑠3superscript𝑒superscript𝑦𝜏𝑦𝑠24𝜏𝑠differential-d𝑠superscriptsubscript0𝜏delimited-[]Φ𝑠superscript𝜐conditional𝜏  𝑧𝑠𝑠Ψ𝑠subscriptsuperscript𝜐0conditional𝜏𝑠differential-d𝑠\displaystyle-\int\_{0}^{\tau}\Psi(s)\frac{y(\tau)-y(s)}{2\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(y(\tau)-y(s))^{2}}{4(\tau-s)}}ds+\int\_{0}^{\tau}\left[\Phi(s)\upsilon^{-}(\tau\,|\,z(s),s)+\Psi(s)\upsilon^{-}\_{0}(\tau\,|\,s)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(τ)Φ𝜏\displaystyle\Phi(\tau) | =∫y​(0)z​(0)U​(0,ξ)​υ+​(τ|ξ,0)​𝑑ξabsentsuperscriptsubscript𝑦0𝑧0𝑈0𝜉superscript𝜐conditional𝜏  𝜉0differential-d𝜉\displaystyle=\int\_{y(0)}^{z(0)}U(0,\xi)\upsilon^{+}(\tau\,|\,\xi,0)d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +f+​(τ)π​τ−∫0τf+​(s)−f+​(τ)2​π​(τ−s)3​𝑑s+∫0τ[f−​(s)​d​(η+​(τ|y​(s),s))−f+​(s)​d​(η+​(τ|z​(s),s))]superscript𝑓𝜏𝜋𝜏superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑓𝜏2𝜋superscript𝜏𝑠3differential-d𝑠superscriptsubscript0𝜏delimited-[]superscript𝑓𝑠𝑑superscript𝜂conditional𝜏  𝑦𝑠𝑠superscript𝑓𝑠𝑑superscript𝜂conditional𝜏  𝑧𝑠𝑠\displaystyle+\frac{f^{+}(\tau)}{\sqrt{\pi\tau}}-\int\_{0}^{\tau}\frac{f^{+}(s)-f^{+}(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}ds+\int\_{0}^{\tau}\left[f^{-}(s)d\left(\eta^{+}(\tau\,|\,y(s),s)\right)-f^{+}(s)d\left(\eta^{+}(\tau\,|\,z(s),s)\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0τΦ​(s)​z​(τ)−z​(s)2​π​(τ−s)3​e−(z​(τ)−z​(s))24​(τ−s)​𝑑s+∫0τ[Φ​(s)​υ0+​(τ|s)+Ψ​(s)​υ+​(τ|y​(s),s)]​𝑑s.superscriptsubscript0𝜏Φ𝑠𝑧𝜏𝑧𝑠2𝜋superscript𝜏𝑠3superscript𝑒superscript𝑧𝜏𝑧𝑠24𝜏𝑠differential-d𝑠superscriptsubscript0𝜏delimited-[]Φ𝑠subscriptsuperscript𝜐0conditional𝜏𝑠Ψ𝑠superscript𝜐conditional𝜏  𝑦𝑠𝑠differential-d𝑠\displaystyle-\int\_{0}^{\tau}\Phi(s)\frac{z(\tau)-z(s)}{2\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(z(\tau)-z(s))^{2}}{4(\tau-s)}}ds+\int\_{0}^{\tau}\left[\Phi(s)\upsilon^{+}\_{0}(\tau\,|\,s)+\Psi(s)\upsilon^{+}(\tau\,|\,y(s),s)\right]ds. |  |

Here the following notation is used

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | η−​(τ|ξ,s)superscript𝜂conditional𝜏  𝜉𝑠\displaystyle\eta^{-}(\tau\,|\,\xi,s) | =−δξ,y​(s)π​(τ−s)+1π​(τ−s)​∑n=−∞∞e−(y​(τ)−ξ+2​n​l​(τ))24​(τ−s),absentsubscript𝛿  𝜉𝑦𝑠𝜋𝜏𝑠1𝜋𝜏𝑠superscriptsubscript𝑛superscript𝑒superscript𝑦𝜏𝜉2𝑛𝑙𝜏24𝜏𝑠\displaystyle=-\frac{\delta\_{\xi,y(s)}}{\sqrt{\pi(\tau-s)}}+\frac{1}{\sqrt{\pi(\tau-s)}}\sum\_{n=-\infty}^{\infty}e^{-\frac{(y(\tau)-\xi+2nl(\tau))^{2}}{4(\tau-s)}}, |  | (44) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | η+​(τ|ξ,s)superscript𝜂conditional𝜏  𝜉𝑠\displaystyle\eta^{+}(\tau\,|\,\xi,s) | =−δξ,z​(s)π​(τ−s)+1π​(τ−s)​∑n=−∞∞e−(y​(τ)−ξ+(2​n+1)​l​(τ))24​(τ−s),absentsubscript𝛿  𝜉𝑧𝑠𝜋𝜏𝑠1𝜋𝜏𝑠superscriptsubscript𝑛superscript𝑒superscript𝑦𝜏𝜉2𝑛1𝑙𝜏24𝜏𝑠\displaystyle=-\frac{\delta\_{\xi,z(s)}}{\sqrt{\pi(\tau-s)}}+\frac{1}{\sqrt{\pi(\tau-s)}}\sum\_{n=-\infty}^{\infty}e^{-\frac{(y(\tau)-\xi+(2n+1)l(\tau))^{2}}{4(\tau-s)}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ−​(τ|ξ,s)superscript𝜐conditional𝜏  𝜉𝑠\displaystyle\upsilon^{-}(\tau\,|\,\xi,s) | =−y​(τ)−ξ+2​n​l​(τ)2​π​(τ−s)3​e−(y​(τ)−ξ+2​n​l​(τ))24​(τ−s),absent𝑦𝜏𝜉2𝑛𝑙𝜏2𝜋superscript𝜏𝑠3superscript𝑒superscript𝑦𝜏𝜉2𝑛𝑙𝜏24𝜏𝑠\displaystyle=-\frac{y(\tau)-\xi+2nl(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(y(\tau)-\xi+2nl(\tau))^{2}}{4(\tau-s)}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ+​(τ|ξ,s)superscript𝜐conditional𝜏  𝜉𝑠\displaystyle\upsilon^{+}(\tau\,|\,\xi,s) | =−y​(τ)−ξ+(2​n+1)​l​(τ)2​π​(τ−s)3​e−(y​(τ)−ξ+(2​n+1)​l​(τ))24​(τ−s),absent𝑦𝜏𝜉2𝑛1𝑙𝜏2𝜋superscript𝜏𝑠3superscript𝑒superscript𝑦𝜏𝜉2𝑛1𝑙𝜏24𝜏𝑠\displaystyle=-\frac{y(\tau)-\xi+(2n+1)l(\tau)}{2\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(y(\tau)-\xi+(2n+1)l(\tau))^{2}}{4(\tau-s)}}, |  |

where δξ,xsubscript𝛿

𝜉𝑥\delta\_{\xi,x} is the Kronecker symbol.

The functions υ,η

𝜐𝜂\upsilon,\eta have the following properties

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lims→τυ0−​(τ|s)subscript→𝑠𝜏subscriptsuperscript𝜐0conditional𝜏𝑠\displaystyle\lim\_{s\to\tau}\upsilon^{-}\_{0}(\tau\,|\,s) | =0,lims→τυ−​(τ|z​(s),s)absent  0subscript→𝑠𝜏superscript𝜐conditional𝜏  𝑧𝑠𝑠\displaystyle=0,\qquad\lim\_{s\to\tau}\upsilon^{-}(\tau\,|\,z(s),s) | =0,absent0\displaystyle=0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lims→τυ+​(τ|y​(s),s)subscript→𝑠𝜏superscript𝜐conditional𝜏  𝑦𝑠𝑠\displaystyle\lim\_{s\to\tau}\upsilon^{+}(\tau\,|\,y(s),s) | =0,lims→τυ0+​(τ|s)absent  0subscript→𝑠𝜏subscriptsuperscript𝜐0conditional𝜏𝑠\displaystyle=0,\qquad\lim\_{s\to\tau}\upsilon^{+}\_{0}(\tau\,|\,s) | =0,absent0\displaystyle=0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lims→τη−​(τ|y​(s),s)subscript→𝑠𝜏superscript𝜂conditional𝜏  𝑦𝑠𝑠\displaystyle\lim\_{s\to\tau}\eta^{-}(\tau\,|\,y(s),s) | =0,lims→τη−​(τ|z​(s),s)absent  0subscript→𝑠𝜏superscript𝜂conditional𝜏  𝑧𝑠𝑠\displaystyle=0,\qquad\lim\_{s\to\tau}\eta^{-}(\tau\,|\,z(s),s) | =0,absent0\displaystyle=0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lims→τη+​(τ|y​(s),s)subscript→𝑠𝜏superscript𝜂conditional𝜏  𝑦𝑠𝑠\displaystyle\lim\_{s\to\tau}\eta^{+}(\tau\,|\,y(s),s) | =0,lims→τη+​(τ|z​(s),s)absent  0subscript→𝑠𝜏superscript𝜂conditional𝜏  𝑧𝑠𝑠\displaystyle=0,\qquad\lim\_{s\to\tau}\eta^{+}(\tau\,|\,z(s),s) | =0.absent0\displaystyle=0. |  |

Again, using the Poisson summation formula yields a few alternative representations of the functions η±​(τ|ξ,s)superscript𝜂plus-or-minusconditional𝜏

𝜉𝑠\eta^{\pm}(\tau\,|\,\xi,s) and υ±​(τ|ξ,s)superscript𝜐plus-or-minusconditional𝜏

𝜉𝑠\upsilon^{\pm}(\tau\,|\,\xi,s) via the Fourier series

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | η−​(τ|ξ,s)superscript𝜂conditional𝜏  𝜉𝑠\displaystyle\eta^{-}(\tau\,|\,\xi,s) | =−𝟏y​(s)−ξπ​(τ−s)+1l​(τ)​[1+2​∑n=1∞e−π2​n2l2​(τ)​(τ−s)​cos⁡(π​n​(ξ−y​(τ))l​(τ))],absentsubscript1𝑦𝑠𝜉𝜋𝜏𝑠1𝑙𝜏delimited-[]12superscriptsubscript𝑛1superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝜋𝑛𝜉𝑦𝜏𝑙𝜏\displaystyle=-\frac{\mathbf{1}\_{y(s)-\xi}}{\sqrt{\pi(\tau-s)}}+\frac{1}{l(\tau)}\left[1+2\sum\_{n=1}^{\infty}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\cos\left(\frac{\pi n(\xi-y(\tau))}{l(\tau)}\right)\right], |  | (45) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | η+​(τ|ξ,s)superscript𝜂conditional𝜏  𝜉𝑠\displaystyle\eta^{+}(\tau\,|\,\xi,s) | =−𝟏ξ−z​(s)π​(τ−s)+1l​(τ)​[1+2​∑n=1∞e−π2​n2l2​(τ)​(τ−s)​(−1)n​cos⁡(π​n​(ξ−y​(τ))l​(τ))],absentsubscript1𝜉𝑧𝑠𝜋𝜏𝑠1𝑙𝜏delimited-[]12superscriptsubscript𝑛1superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠superscript1𝑛𝜋𝑛𝜉𝑦𝜏𝑙𝜏\displaystyle=-\frac{\mathbf{1}\_{\xi-z(s)}}{\sqrt{\pi(\tau-s)}}+\frac{1}{l(\tau)}\left[1+2\sum\_{n=1}^{\infty}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}(-1)^{n}\cos\left(\frac{\pi n(\xi-y(\tau))}{l(\tau)}\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ−​(τ|ξ,s)superscript𝜐conditional𝜏  𝜉𝑠\displaystyle\upsilon^{-}(\tau\,|\,\xi,s) | =2​πl2​(τ)​∑n=1∞n​e−π2​n2l2​(τ)​(τ−s)​sin⁡(π​n​(ξ−y​(τ))l​(τ)),absent2𝜋superscript𝑙2𝜏superscriptsubscript𝑛1𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝜋𝑛𝜉𝑦𝜏𝑙𝜏\displaystyle=\frac{2\pi}{l^{2}(\tau)}\sum\_{n=1}^{\infty}ne^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\sin\left(\frac{\pi n(\xi-y(\tau))}{l(\tau)}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ+​(τ|ξ,s)superscript𝜐conditional𝜏  𝜉𝑠\displaystyle\upsilon^{+}(\tau\,|\,\xi,s) | =2​πl2​(τ)​∑n=1∞n​e−π2​n2l2​(τ)​(τ−s)​(−1)n​sin⁡(π​n​(ξ−y​(τ))l​(τ)).absent2𝜋superscript𝑙2𝜏superscriptsubscript𝑛1𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠superscript1𝑛𝜋𝑛𝜉𝑦𝜏𝑙𝜏\displaystyle=\frac{2\pi}{l^{2}(\tau)}\sum\_{n=1}^{\infty}ne^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}(-1)^{n}\sin\left(\frac{\pi n(\xi-y(\tau))}{l(\tau)}\right). |  |

Finally, using Eq. ([31](#S2.E31 "Equation 31 ‣ 2.2 Connection to the Jacobi theta function ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and Eq. ([33](#S2.E33 "Equation 33 ‣ 2.2 Connection to the Jacobi theta function ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), we obtain another representation of Eq. ([45](#S2.E45 "Equation 45 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) in terms of the Jacobi theta function θ3​(z,ω)subscript𝜃3𝑧𝜔\theta\_{3}(z,\omega)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | η−​(τ|ξ,s)superscript𝜂conditional𝜏  𝜉𝑠\displaystyle\eta^{-}(\tau\,|\,\xi,s) | =−𝟏y​(s)−ξπ​(τ−s)+1l​(τ)​θ3​(ϕ−​(ξ,y​(τ)),ω2),absentsubscript1𝑦𝑠𝜉𝜋𝜏𝑠1𝑙𝜏subscript𝜃3subscriptitalic-ϕ𝜉𝑦𝜏subscript𝜔2\displaystyle=-\frac{\mathbf{1}\_{y(s)-\xi}}{\sqrt{\pi(\tau-s)}}+\frac{1}{l(\tau)}\theta\_{3}\left(\phi\_{-}(\xi,y(\tau)),\omega\_{2}\right), |  | (46) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | η+​(τ|ξ,s)superscript𝜂conditional𝜏  𝜉𝑠\displaystyle\eta^{+}(\tau\,|\,\xi,s) | =−𝟏ξ−z​(s)π​(τ−s)+1l​(τ)​θ3​(ϕ−​(ξ+l​(τ),y​(τ)),ω2),absentsubscript1𝜉𝑧𝑠𝜋𝜏𝑠1𝑙𝜏subscript𝜃3subscriptitalic-ϕ𝜉𝑙𝜏𝑦𝜏subscript𝜔2\displaystyle=-\frac{\mathbf{1}\_{\xi-z(s)}}{\sqrt{\pi(\tau-s)}}+\frac{1}{l(\tau)}\theta\_{3}\left(\phi\_{-}(\xi+l(\tau),y(\tau)),\omega\_{2}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ−​(τ|ξ,s)superscript𝜐conditional𝜏  𝜉𝑠\displaystyle\upsilon^{-}(\tau\,|\,\xi,s) | =−π2​l2​(τ)​θ3′​(ϕ−​(ξ,y​(τ)),ω2),absent𝜋2superscript𝑙2𝜏subscriptsuperscript𝜃′3subscriptitalic-ϕ𝜉𝑦𝜏subscript𝜔2\displaystyle=-\frac{\pi}{2l^{2}(\tau)}\theta^{\prime}\_{3}\left(\phi\_{-}(\xi,y(\tau)),\omega\_{2}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | υ+​(τ|ξ,s)superscript𝜐conditional𝜏  𝜉𝑠\displaystyle\upsilon^{+}(\tau\,|\,\xi,s) | =−π2​l2​(τ)​θ3′​(ϕ−​(ξ+l​(τ),y​(τ)),ω2).absent𝜋2superscript𝑙2𝜏subscriptsuperscript𝜃′3subscriptitalic-ϕ𝜉𝑙𝜏𝑦𝜏subscript𝜔2\displaystyle=-\frac{\pi}{2l^{2}(\tau)}\theta^{\prime}\_{3}\left(\phi\_{-}(\xi+l(\tau),y(\tau)),\omega\_{2}\right). |  |

The formulas Eq. ([44](#S2.E44 "Equation 44 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and Eq. ([45](#S2.E45 "Equation 45 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) are complementary. Since the exponents in Eq. ([46](#S2.E46 "Equation 46 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) are proportional to the difference τ−s𝜏𝑠\tau-s, the Fourier series Eq. ([46](#S2.E46 "Equation 46 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) converge fast if τ−s𝜏𝑠\tau-s is large. Contrary, the exponents in Eq. ([44](#S2.E44 "Equation 44 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) are inversely proportional to τ−s𝜏𝑠\tau-s. Therefore, the series Eq. ([44](#S2.E44 "Equation 44 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) converge fast if τ−s𝜏𝑠\tau-s is small.

## 3 Solution by the HP method

Similar to Section [2](#S2 "2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"), the HP method, (Tikhonov and Samarskii, [1963](#bib.bib32); Friedman, [1964.](#bib.bib11); Kartashov, [2001](#bib.bib19)), can be used to price double barrier options by solving the problem in Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). The idea was first proposed and developed in (Itkin and Muravey, [2020](#bib.bib15)) and is a generalization of the standard HP method for the case of two moving boundaries. Note, that to the best of authors’ knowledge, yet the closed form (or even semi-closed form) solution of this problem was not known in physics, even not mentioning finance. Below we explain our approach paying attention to all intermediate details as the behavior of the solution at the boundaries is not trivial.

Following the main idea of the HP method, let us search for the solution of the ℬℬ{\cal B} problem in Eq. ([4](#S1.E4 "Equation 4 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) Eq. ([6](#S1.E6 "Equation 6 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), Eq. ([5](#S1.E5 "Equation 5 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(τ,x)=q​(τ,x)+12​π​τ​∫y​(0)z​(0)U​(0,x′)​e−(x−x′)24​τ​𝑑x′,𝑈𝜏𝑥𝑞𝜏𝑥12𝜋𝜏superscriptsubscript𝑦0𝑧0𝑈0superscript𝑥′superscript𝑒superscript𝑥superscript𝑥′24𝜏differential-dsuperscript𝑥′U(\tau,x)=q(\tau,x)+\frac{1}{2\sqrt{\pi\tau}}\int\_{y(0)}^{z(0)}U(0,x^{\prime})e^{-\frac{(x-x^{\prime})^{2}}{4\tau}}dx^{\prime}, |  | (47) |

so function q​(τ,x)𝑞𝜏𝑥q(\tau,x) solves a problem with the homogeneous initial condition

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂q​(τ,x)∂τ𝑞𝜏𝑥𝜏\displaystyle\frac{\partial q(\tau,x)}{\partial\tau} | =∂2q​(τ,x)∂x2,absentsuperscript2𝑞𝜏𝑥superscript𝑥2\displaystyle=\frac{\partial^{2}q(\tau,x)}{\partial x^{2}}, |  | (48) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(0,x)𝑞0𝑥\displaystyle q(0,x) | =0,y​(0)<x<z​(0),formulae-sequenceabsent0𝑦0𝑥𝑧0\displaystyle=0,\qquad y(0)<x<z(0), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(τ,y​(τ))𝑞𝜏𝑦𝜏\displaystyle q(\tau,y(\tau)) | =ϕ1​(τ)≡f−​(τ)−12​π​τ​∫y​(0)z​(0)u​(0,x′)​e−(y​(τ)−x′)24​τ​𝑑x′,absentsubscriptitalic-ϕ1𝜏superscript𝑓𝜏12𝜋𝜏superscriptsubscript𝑦0𝑧0𝑢0superscript𝑥′superscript𝑒superscript𝑦𝜏superscript𝑥′24𝜏differential-dsuperscript𝑥′\displaystyle=\phi\_{1}(\tau)\equiv f^{-}(\tau)-\frac{1}{2\sqrt{\pi\tau}}\int\_{y(0)}^{z(0)}u(0,x^{\prime})e^{-\frac{(y(\tau)-x^{\prime})^{2}}{4\tau}}dx^{\prime}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(τ,z​(τ))𝑞𝜏𝑧𝜏\displaystyle q(\tau,z(\tau)) | =ψ1​(τ)≡f+​(τ)−12​π​τ​∫y​(0)z​(0)u​(0,x′)​e−(z​(τ)−x′)24​τ​𝑑x′.absentsubscript𝜓1𝜏superscript𝑓𝜏12𝜋𝜏superscriptsubscript𝑦0𝑧0𝑢0superscript𝑥′superscript𝑒superscript𝑧𝜏superscript𝑥′24𝜏differential-dsuperscript𝑥′\displaystyle=\psi\_{1}(\tau)\equiv f^{+}(\tau)-\frac{1}{2\sqrt{\pi\tau}}\int\_{y(0)}^{z(0)}u(0,x^{\prime})e^{-\frac{(z(\tau)-x^{\prime})^{2}}{4\tau}}dx^{\prime}. |  |

In (Itkin and Muravey, [2020](#bib.bib15)) it is proposed to search for the solution of Eq. ([48](#S3.E48 "Equation 48 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) in the form of a generalized heat potential

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(x,τ)=14​π​∫0τ1(τ−k)3​((x−y​(k))​Ω​(k)​e−(x−y​(k))24​(τ−k)+(x−z​(k))​Θ​(k)​e−(x−z​(k))24​(τ−k))​𝑑k,𝑞𝑥𝜏14𝜋superscriptsubscript0𝜏1superscript𝜏𝑘3𝑥𝑦𝑘Ω𝑘superscript𝑒superscript𝑥𝑦𝑘24𝜏𝑘𝑥𝑧𝑘Θ𝑘superscript𝑒superscript𝑥𝑧𝑘24𝜏𝑘differential-d𝑘q(x,\tau)=\frac{1}{4\sqrt{\pi}}\int\_{0}^{\tau}\frac{1}{\sqrt{(\tau-k)^{3}}}\left((x-y(k))\Omega(k)e^{-\frac{(x-y(k))^{2}}{4(\tau-k)}}+(x-z(k))\Theta(k)e^{-\frac{(x-z(k))^{2}}{4(\tau-k)}}\right)dk, |  | (49) |

where Ω​(k),Θ​(k)

Ω𝑘Θ𝑘\Omega(k),\Theta(k) are the heat potential densities. In other words, the solution is represented as a sum of two heat potentials: one corresponds to the lower barrier, and the other one - to the upper barrier. It is easy to check, that each such a potential solves the heat equation in Eq. ([48](#S3.E48 "Equation 48 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), see (Tikhonov and Samarskii, [1963](#bib.bib32)) as the derivative with respect to τ𝜏\tau of the RHS of Eq. ([49](#S3.E49 "Equation 49 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) can be pulled into the integral since the value of both integrands at k=τ𝑘𝜏k=\tau vanishes.

To find the unknown functions Ω​(k),Θ​(k)

Ω𝑘Θ𝑘\Omega(k),\Theta(k) one can substitute into Eq. ([49](#S3.E49 "Equation 49 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) the values x=y​(τ)𝑥𝑦𝜏x=y(\tau) and x=z​(τ)𝑥𝑧𝜏x=z(\tau), and get a system of two integral equations that the functions Ω​(k),Θ​(k)

Ω𝑘Θ𝑘\Omega(k),\Theta(k) solve. However, it is well-known, (Tikhonov and Samarskii, [1963](#bib.bib32)), that these integrals at x→y​(τ)→𝑥𝑦𝜏x\to y(\tau) and x→z​(τ)→𝑥𝑧𝜏x\to z(\tau) have a discontinuity, but with the finite value at x=y​(τ)±0𝑥plus-or-minus𝑦𝜏0x=y(\tau)\pm 0 and x=z​(τ)±0𝑥plus-or-minus𝑧𝜏0x=z(\tau)\pm 0. To investigate this discontinuity in more detail and derive the value of heat potential integral at the boundary x→y​(τ)±0→𝑥plus-or-minus𝑦𝜏0x\to y(\tau)\pm 0, we consider a problem similar to Eq. ([48](#S3.E48 "Equation 48 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒ​q​(τ,x)ℒ𝑞𝜏𝑥\displaystyle\mathcal{L}q(\tau,x) | =0,(x,τ)∈Ω:[y​(τ),∞)×ℝ+,:formulae-sequenceabsent0𝑥𝜏Ω𝑦𝜏subscriptℝ\displaystyle=0,\qquad(x,\tau)\in\Omega:[y(\tau),\infty)\times\mathbb{R}\_{+}, |  | (50) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(0,x)𝑞0𝑥\displaystyle q(0,x) | =0,y​(0)<x<∞,formulae-sequenceabsent0𝑦0𝑥\displaystyle=0,\quad y(0)<x<\infty, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(τ,y​(τ))𝑞𝜏𝑦𝜏\displaystyle q(\tau,y(\tau)) | =χ​(τ),q​(τ,x)|x→∞=0.formulae-sequenceabsent𝜒𝜏evaluated-at𝑞𝜏𝑥→𝑥0\displaystyle=\chi(\tau),\qquad q(\tau,x)\Big{|}\_{x\to\infty}=0. |  |

with the operator ℒℒ{\cal L} defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=−∂∂τ+σ2​∂2∂x,ℒ𝜏superscript𝜎2superscript2𝑥\mathcal{L}=-\frac{\partial}{\partial\tau}+\sigma^{2}\frac{\partial^{2}}{\partial x}, |  | (51) |

where σ=c​o​n​s​t𝜎𝑐𝑜𝑛𝑠𝑡\sigma=const. Using the HP method, the solution of this problem can be expressed as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q​(τ,x)𝑞𝜏𝑥\displaystyle q(\tau,x) | =∫0τΩ​(k)​x−y​(k)4​σ3​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​𝑑k,absentsuperscriptsubscript0𝜏Ω𝑘𝑥𝑦𝑘4superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle=\int\_{0}^{\tau}\Omega(k)\frac{x-y(k)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk, |  | (52) |

where Ω​(τ)Ω𝜏\Omega(\tau) is the heat potential density, and y​(τ)𝑦𝜏y(\tau) is a smooth curve (the moving boundary).
Our aim below is to derive the value of this integral at x→y​(τ)±0→𝑥plus-or-minus𝑦𝜏0x\to y(\tau)\pm 0, and the gradient ∂q​(τ,x)/∂x𝑞𝜏𝑥𝑥\partial q(\tau,x)/\partial x in the same limit, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(τ)=limx→y​(τ)±0q​(τ,x),ψ​(τ)=limx→y​(τ)±0∂q​(τ,x)∂x.formulae-sequence𝜑𝜏subscript→𝑥plus-or-minus𝑦𝜏0𝑞𝜏𝑥𝜓𝜏subscript→𝑥plus-or-minus𝑦𝜏0𝑞𝜏𝑥𝑥\varphi(\tau)=\lim\_{x\to y(\tau)\pm 0}q(\tau,x),\qquad\psi(\tau)=\lim\_{x\to y(\tau)\pm 0}\frac{\partial q(\tau,x)}{\partial x}. |  | (53) |

### 3.1 The limiting value of φ​(t)𝜑𝑡\varphi(t)

This result is obtained, eg., in (Tikhonov and Samarskii, [1963](#bib.bib32)). Consider a function W​(τ,x)=2​σ2​ϕ​(t)𝑊𝜏𝑥2superscript𝜎2italic-ϕ𝑡W(\tau,x)=2\sigma^{2}\phi(t)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | W​(τ,x)𝑊𝜏𝑥\displaystyle W(\tau,x) | =∫0τΩ​(k)​x−y​(k)2​σ​π​(τ−k)3​e−(y​(τ)−y​(k))24​σ2​(τ−k)​𝑑k.absentsuperscriptsubscript0𝜏Ω𝑘𝑥𝑦𝑘2𝜎𝜋superscript𝜏𝑘3superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle=\int\_{0}^{\tau}\Omega(k)\frac{x-y(k)}{2\sigma\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk. |  | (54) |

Also consider an auxiliary integral

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V~​(τ,x)~𝑉𝜏𝑥\displaystyle\tilde{V}(\tau,x) | =∫0τy′​(k)​Ω​(k)σ​π​(τ−k)​e−(x−y​(k))24​σ2​(τ−k)​𝑑k.absentsuperscriptsubscript0𝜏superscript𝑦′𝑘Ω𝑘𝜎𝜋𝜏𝑘superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle=\int\_{0}^{\tau}\frac{y^{\prime}(k)\Omega(k)}{\sigma\sqrt{\pi(\tau-k)}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk. |  | (55) |

Assume that y​(k)𝑦𝑘y(k) is differentiable. As shown in (Tikhonov and Samarskii, [1963](#bib.bib32)), V~​(τ,x)~𝑉𝜏𝑥\tilde{V}(\tau,x) is continuous along the curve x=y​(τ)𝑥𝑦𝜏x=y(\tau) because it converges uniformly and y′​(k)superscript𝑦′𝑘y^{\prime}(k) is bounded, while W​(τ,x)𝑊𝜏𝑥W(\tau,x) is discontinuous. To show this, first assume that Ω​(τ)=Ω0=c​o​n​s​tΩ𝜏subscriptΩ0𝑐𝑜𝑛𝑠𝑡\Omega(\tau)=\Omega\_{0}=const. Then the difference W0−V~0subscript𝑊0subscript~𝑉0W\_{0}-\tilde{V}\_{0}, where the sub-index 0 means that we use Φ0subscriptΦ0\Phi\_{0} instead of Φ​(τ)Φ𝜏\Phi(\tau) in the definitions Eq. ([54](#S3.E54 "Equation 54 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), Eq. ([55](#S3.E55 "Equation 55 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), can be calculated directly with the change of variables k↦a=(x−y​(k))/(2​σ​τ−k)maps-to𝑘𝑎𝑥𝑦𝑘2𝜎𝜏𝑘k\mapsto a=(x-y(k))/(2\sigma\sqrt{\tau-k})

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | W0−V~0subscript𝑊0subscript~𝑉0\displaystyle W\_{0}-\tilde{V}\_{0} | =12​σ​π​∫0τΩ0​e−(x−y​(k))24​σ2​(τ−k)​[x−y​(k)(τ−k)3/2−2​y′​(k)(τ−k)1/2]​𝑑k=Ω0​2π​∫ζ−ζ+e−a2​𝑑a,absent12𝜎𝜋superscriptsubscript0𝜏subscriptΩ0superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘delimited-[]𝑥𝑦𝑘superscript𝜏𝑘322superscript𝑦′𝑘superscript𝜏𝑘12differential-d𝑘subscriptΩ02𝜋superscriptsubscriptsuperscript𝜁superscript𝜁superscript𝑒superscript𝑎2differential-d𝑎\displaystyle=\frac{1}{2\sigma\sqrt{\pi}}\int\_{0}^{\tau}\Omega\_{0}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}\left[\frac{x-y(k)}{{(\tau-k)^{3/2}}}-\frac{2y^{\prime}(k)}{{(\tau-k)^{1/2}}}\right]dk=\Omega\_{0}\frac{2}{\sqrt{\pi}}\int\_{\zeta^{-}}^{\zeta^{+}}e^{-a^{2}}da, |  | (56) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ−superscript𝜁\displaystyle\zeta^{-} | =x−y​(0)2​σ​τ,ζ+={∞,x>y​(τ),0,x=y​(τ),−∞,x<y​(τ).formulae-sequenceabsent𝑥𝑦02𝜎𝜏superscript𝜁cases𝑥𝑦𝜏0𝑥𝑦𝜏𝑥𝑦𝜏\displaystyle=\frac{x-y(0)}{2\sigma\sqrt{\tau}},\qquad\zeta^{+}=\begin{cases}\infty,&x>y(\tau),\\ 0,&x=y(\tau),\\ -\infty,&x<y(\tau).\end{cases} |  |

Accordingly, at, say x→y​(τ)+0→𝑥𝑦𝜏0x\to y(\tau)+0 we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | [W0​(τ,y​(τ)+0)−W0​(τ,y​(τ))]−[V~0​(τ,y​(τ)+0)−V~0​(τ,y​(τ))]=Ω0​2π​∫0∞e−a2​𝑑a=Ω0.delimited-[]subscript𝑊0𝜏𝑦𝜏0subscript𝑊0𝜏𝑦𝜏delimited-[]subscript~𝑉0𝜏𝑦𝜏0subscript~𝑉0𝜏𝑦𝜏subscriptΩ02𝜋superscriptsubscript0superscript𝑒superscript𝑎2differential-d𝑎subscriptΩ0\left[W\_{0}(\tau,y(\tau)+0)-W\_{0}(\tau,y(\tau))\right]-\left[\tilde{V}\_{0}(\tau,y(\tau)+0)-\tilde{V}\_{0}(\tau,y(\tau))\right]=\Omega\_{0}\frac{2}{\sqrt{\pi}}\int\_{0}^{\infty}e^{-a^{2}}da=\Omega\_{0}. |  | (57) |

Since the function V~0subscript~𝑉0\tilde{V}\_{0} is continuous, the expression in the second square brackets in Eq. ([57](#S3.E57 "Equation 57 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) vanishes, and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | W0​(τ,y​(τ)+0)−W0​(τ,y​(τ))=Ω0.subscript𝑊0𝜏𝑦𝜏0subscript𝑊0𝜏𝑦𝜏subscriptΩ0W\_{0}(\tau,y(\tau)+0)-W\_{0}(\tau,y(\tau))=\Omega\_{0}. |  | (58) |

If Ω​(τ)Ω𝜏\Omega(\tau) is not constant, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(τ,x)=W0​(τ,x)−∫0τx−y​(k)2​σ​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​[Ω​(τ)−Ω​(k)]​𝑑k.𝑊𝜏𝑥subscript𝑊0𝜏𝑥superscriptsubscript0𝜏𝑥𝑦𝑘2𝜎𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘delimited-[]Ω𝜏Ω𝑘differential-d𝑘W(\tau,x)=W\_{0}(\tau,x)-\int\_{0}^{\tau}\frac{x-y(k)}{2\sigma\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}[\Omega(\tau)-\Omega(k)]dk. |  | (59) |

We assume that the boundary y​(τ)𝑦𝜏y(\tau) and the potential density Ω​(k)Ω𝑘\Omega(k) are differentiable functions of their arguments, i.e., at least 𝒞1superscript𝒞1{\cal C}^{1}. Then the integral in Eq. ([59](#S3.E59 "Equation 59 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) has the same singularity as the function V~​(τ,x)~𝑉𝜏𝑥\tilde{V}(\tau,x), converges uniformly, and thus is a continuous function on the curve x=y​(τ)𝑥𝑦𝜏x=y(\tau). This implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(τ,x0+0)−W​(τ,x0)=W0​(τ,x0+0)−W0​(τ,x0)=Ω​(τ),𝑊𝜏subscript𝑥00𝑊𝜏subscript𝑥0subscript𝑊0𝜏subscript𝑥00subscript𝑊0𝜏subscript𝑥0Ω𝜏W(\tau,x\_{0}+0)-W(\tau,x\_{0})=W\_{0}(\tau,x\_{0}+0)-W\_{0}(\tau,x\_{0})=\Omega(\tau), |  | (60) |

and, in particular, this is true for x0=y​(τ)subscript𝑥0𝑦𝜏x\_{0}=y(\tau). In a similar way one can show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(τ,x0−0)=W0​(τ,x0)−Ω​(τ),𝑊𝜏subscript𝑥00subscript𝑊0𝜏subscript𝑥0Ω𝜏W(\tau,x\_{0}-0)=W\_{0}(\tau,x\_{0})-\Omega(\tau), |  | (61) |

Combining these results together, we obtain the final formula for φ​(t)𝜑𝑡\varphi(t)

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(τ)=±Ω​(τ)2​σ2+∫0τΩ​(k)​y​(τ)−y​(k)4​σ3​π​(τ−k)3​e−(y​(τ)−y​(k))24​σ2​(τ−k)​𝑑k.𝜑𝜏plus-or-minusΩ𝜏2superscript𝜎2superscriptsubscript0𝜏Ω𝑘𝑦𝜏𝑦𝑘4superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘\varphi(\tau)=\pm\frac{\Omega(\tau)}{2\sigma^{2}}+\int\_{0}^{\tau}\Omega(k)\frac{y(\tau)-y(k)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk. |  | (62) |

### 3.2 The limiting value of ψ​(t)𝜓𝑡\psi(t)

Using the definition of q​(τ,x)𝑞𝜏𝑥q(\tau,x) in Eq. ([52](#S3.E52 "Equation 52 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) we need an explicit formula for

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ​(τ)=limx→y​(τ)±0∂q​(τ,x)∂x𝜓𝜏subscript→𝑥plus-or-minus𝑦𝜏0𝑞𝜏𝑥𝑥\displaystyle\psi(\tau)=\lim\_{x\to y(\tau)\pm 0}\frac{\partial q(\tau,x)}{\partial x} | =limx→y​(τ)±0∂∂x​∫0τΩ​(k)​x−y​(k)4​σ3​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​𝑑k.absentsubscript→𝑥plus-or-minus𝑦𝜏0𝑥superscriptsubscript0𝜏Ω𝑘𝑥𝑦𝑘4superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle=\lim\_{x\to y(\tau)\pm 0}\frac{\partial}{\partial x}\int\_{0}^{\tau}\Omega(k)\frac{x-y(k)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk. |  | (63) |

However, as shown in Section [3.1](#S3.SS1 "3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"), this integral is discontinuous at x→y​(τ)→𝑥𝑦𝜏x\to y(\tau) (this is an improper Riemann integral of second kind). Hence, we cannot compute ψ​(τ)𝜓𝜏\psi(\tau) directly by taking derivative of q​(τ,x)𝑞𝜏𝑥q(\tau,x) with respect to x𝑥x.

Therefore, to proceed let us represent this integral as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∫0τsuperscriptsubscript0𝜏\displaystyle\int\_{0}^{\tau} | Ω​(k)​x−y​(k)4​σ3​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​d​k=Ω​(τ)​∫0τx−y​(k)4​σ3​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​𝑑kΩ𝑘𝑥𝑦𝑘4superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘𝑑𝑘Ω𝜏superscriptsubscript0𝜏𝑥𝑦𝑘4superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle\Omega(k)\frac{x-y(k)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk=\Omega(\tau)\int\_{0}^{\tau}\frac{x-y(k)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk |  | (64) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ[Ω​(k)−Ω​(τ)]​x−y​(k)4​σ3​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​𝑑k=I1+I2.superscriptsubscript0𝜏delimited-[]Ω𝑘Ω𝜏𝑥𝑦𝑘4superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘subscript𝐼1subscript𝐼2\displaystyle+\int\_{0}^{\tau}[\Omega(k)-\Omega(\tau)]\frac{x-y(k)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk=I\_{1}+I\_{2}. |  |

We showed in Section [3.1](#S3.SS1 "3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit") that the second integral in Eq. ([64](#S3.E64 "Equation 64 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) has the same singularity as the function V~​(τ,x)~𝑉𝜏𝑥\tilde{V}(\tau,x), converges uniformly, and thus is a continuous function on the curve x=y​(τ)𝑥𝑦𝜏x=y(\tau). Then, it is a continuous function for x∈ℜ𝑥x\in\Re. Thus, by the standard theorem of integral calculus we can differentiate this integral by parameter x𝑥x, and the result is continuous in x𝑥x, (Butuzov and Butuzova, [2016](#bib.bib3))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | limx→y​(τ)±0∂∂x​∫0τ[Ω​(k)−Ω​(τ)]​x−y​(k)4​σ3​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​𝑑ksubscript→𝑥plus-or-minus𝑦𝜏0𝑥superscriptsubscript0𝜏delimited-[]Ω𝑘Ω𝜏𝑥𝑦𝑘4superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle\ \lim\_{x\to y(\tau)\pm 0}\frac{\partial}{\partial x}\int\_{0}^{\tau}[\Omega(k)-\Omega(\tau)]\frac{x-y(k)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk |  | (65) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limx→y​(τ)±0∫0τ[Ω​(k)−Ω​(τ)]​e−(x−y​(k))24​σ2​(τ−k)4​σ3​π​(τ−k)3​(1−(x−y​(k))22​σ2​(τ−k))​𝑑kabsentsubscript→𝑥plus-or-minus𝑦𝜏0superscriptsubscript0𝜏delimited-[]Ω𝑘Ω𝜏superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘4superscript𝜎3𝜋superscript𝜏𝑘31superscript𝑥𝑦𝑘22superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle=\lim\_{x\to y(\tau)\pm 0}\int\_{0}^{\tau}[\Omega(k)-\Omega(\tau)]\frac{e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}\left(1-\frac{(x-y(k))^{2}}{2\sigma^{2}(\tau-k)}\right)dk |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0τ[Ω​(k)−Ω​(τ)]​e−(y​(τ)−y​(k))24​σ2​(τ−k)4​σ3​π​(τ−k)3​(1−(y​(τ)−y​(k))22​σ2​(τ−k))​𝑑k.absentsuperscriptsubscript0𝜏delimited-[]Ω𝑘Ω𝜏superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘4superscript𝜎3𝜋superscript𝜏𝑘31superscript𝑦𝜏𝑦𝑘22superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle=\int\_{0}^{\tau}[\Omega(k)-\Omega(\tau)]\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}\left(1-\frac{(y(\tau)-y(k))^{2}}{2\sigma^{2}(\tau-k)}\right)dk. |  |

As far as the first integral I1subscript𝐼1I\_{1} in Eq. ([64](#S3.E64 "Equation 64 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) is concerned, it was already considered in Section [3.1](#S3.SS1 "3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"), and is denoted as W0​(τ,x)/2​σ2subscript𝑊0𝜏𝑥2superscript𝜎2W\_{0}(\tau,x)/2\sigma^{2} in Eq. ([56](#S3.E56 "Equation 56 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Since the integral on a𝑎a in the RHS of Eq. ([56](#S3.E56 "Equation 56 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) can be computed explicitly, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | W0−V~0=Ω0​2π​∫ζ−ζ+e−a2​𝑑a=Ω0​{Erfc​(x−y​(0)2​σ​τ),x>y​(τ),−Erf​(x−y​(0)2​σ​τ),x=y​(τ),−Erfc​(−x−y​(0)2​σ​τ),x<y​(τ).subscript𝑊0subscript~𝑉0subscriptΩ02𝜋superscriptsubscriptsuperscript𝜁superscript𝜁superscript𝑒superscript𝑎2differential-d𝑎subscriptΩ0casesErfc𝑥𝑦02𝜎𝜏𝑥𝑦𝜏Erf𝑥𝑦02𝜎𝜏𝑥𝑦𝜏Erfc𝑥𝑦02𝜎𝜏𝑥𝑦𝜏W\_{0}-\tilde{V}\_{0}=\Omega\_{0}\frac{2}{\sqrt{\pi}}\int\_{\zeta^{-}}^{\zeta^{+}}e^{-a^{2}}da=\Omega\_{0}\begin{cases}\mathrm{Erfc}\left(\frac{x-y(0)}{2\sigma\sqrt{\tau}}\right),&x>y(\tau),\\ -\mathrm{Erf}\left(\frac{x-y(0)}{2\sigma\sqrt{\tau}}\right),&x=y(\tau),\\ -\mathrm{Erfc}\left(-\frac{x-y(0)}{2\sigma\sqrt{\tau}}\right),&x<y(\tau).\end{cases} |  | (66) |

Also, recall that the function V~0​(τ,x)subscript~𝑉0𝜏𝑥\tilde{V}\_{0}(\tau,x) is the continuous function along the curve x=y​(τ)𝑥𝑦𝜏x=y(\tau) as y′​(τ)superscript𝑦′𝜏y^{\prime}(\tau) is bounded, and the integral converges uniformly. Therefore

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂W0∂xsubscript𝑊0𝑥\displaystyle\frac{\partial W\_{0}}{\partial x} | =∂V~0∂x−Ω0​Λ​(τ,x),absentsubscript~𝑉0𝑥subscriptΩ0Λ𝜏𝑥\displaystyle=\frac{\partial\tilde{V}\_{0}}{\partial x}-\Omega\_{0}\Lambda(\tau,x), |  | (67) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(τ,x)Λ𝜏𝑥\displaystyle\Lambda(\tau,x) | ={1σ​π​τ​e−(x−y​(0))24​π​σ2,x>y​(τ),1σ​π​τ​e−(x−y​(0))24​π​σ2,x<y​(τ).absentcases1𝜎𝜋𝜏superscript𝑒superscript𝑥𝑦024𝜋superscript𝜎2𝑥𝑦𝜏1𝜎𝜋𝜏superscript𝑒superscript𝑥𝑦024𝜋superscript𝜎2𝑥𝑦𝜏\displaystyle=\begin{cases}\frac{1}{\sigma\sqrt{\pi\tau}}e^{-\frac{(x-y(0))^{2}}{4\pi\sigma^{2}}},&x>y(\tau),\\ \frac{1}{\sigma\sqrt{\pi\tau}}e^{-\frac{(x-y(0))^{2}}{4\pi\sigma^{2}}},&x<y(\tau).\end{cases} |  |

Thus, Λ​(τ,y​(τ)−0)=Λ​(τ,y​(τ)+0)Λ𝜏𝑦𝜏0Λ𝜏𝑦𝜏0\Lambda(\tau,y(\tau)-0)=\Lambda(\tau,y(\tau)+0), hence the function Λ​(τ,x)Λ𝜏𝑥\Lambda(\tau,x) is differentiable at this point. This implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂W0∂x=−Ω0​∫0τy′​(k)​x−y​(k)2​σ3​π​(τ−k)3​e−(x−y​(k))24​σ2​(τ−k)​𝑑k−Ω0σ​π​τ​e−(x−y​(0))24​σ2​τ.subscript𝑊0𝑥subscriptΩ0superscriptsubscript0𝜏superscript𝑦′𝑘𝑥𝑦𝑘2superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑥𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘subscriptΩ0𝜎𝜋𝜏superscript𝑒superscript𝑥𝑦024superscript𝜎2𝜏\frac{\partial W\_{0}}{\partial x}=-\Omega\_{0}\int\_{0}^{\tau}y^{\prime}(k)\frac{x-y(k)}{2\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(x-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk-\frac{\Omega\_{0}}{\sigma\sqrt{\pi\tau}}e^{-\frac{(x-y(0))^{2}}{4\sigma^{2}\tau}}. |  | (68) |

As it was mentioned, the function V~0​(τ,x)subscript~𝑉0𝜏𝑥\tilde{V}\_{0}(\tau,x) is continuous over the curve x=y​(τ)𝑥𝑦𝜏x=y(\tau). However, its derivative with respect to x𝑥x at x=y​(τ)𝑥𝑦𝜏x=y(\tau) in Eq. ([67](#S3.E67 "Equation 67 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) has a form of the RHS in Eq. ([54](#S3.E54 "Equation 54 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Therefore, according to the result of Section [3.1](#S3.SS1 "3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"), in the limit x→y​(τ)→𝑥𝑦𝜏x\to y(\tau), again using Eq. ([62](#S3.E62 "Equation 62 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→y​(τ)±0∂W0∂x=∓Ω0​y′​(τ)σ2−Ω0​∫0τy′​(k)​y​(τ)−y​(k)2​σ3​π​(τ−k)3​e−(y​(τ)−y​(k))24​σ2​(τ−k)​𝑑k−Ω0σ​π​τ​e−(y​(τ)−y​(0))24​σ2​τ.subscript→𝑥plus-or-minus𝑦𝜏0subscript𝑊0𝑥minus-or-plussubscriptΩ0superscript𝑦′𝜏superscript𝜎2subscriptΩ0superscriptsubscript0𝜏superscript𝑦′𝑘𝑦𝜏𝑦𝑘2superscript𝜎3𝜋superscript𝜏𝑘3superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘differential-d𝑘subscriptΩ0𝜎𝜋𝜏superscript𝑒superscript𝑦𝜏𝑦024superscript𝜎2𝜏\displaystyle\lim\_{x\to y(\tau)\pm 0}\frac{\partial W\_{0}}{\partial x}=\mp\Omega\_{0}\frac{y^{\prime}(\tau)}{\sigma^{2}}-\Omega\_{0}\int\_{0}^{\tau}y^{\prime}(k)\frac{y(\tau)-y(k)}{2\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}dk-\frac{\Omega\_{0}}{\sigma\sqrt{\pi\tau}}e^{-\frac{(y(\tau)-y(0))^{2}}{4\sigma^{2}\tau}}. |  | (69) |

Combining Eq. ([65](#S3.E65 "Equation 65 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and Eq. ([69](#S3.E69 "Equation 69 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) together yields the final result

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ​(τ)𝜓𝜏\displaystyle\psi(\tau) | =∫0τΩ​(k)​e−(y​(τ)−y​(k))24​σ2​(τ−k)4​σ3​π​(τ−k)3​(1−(y​(τ)−y​(k))22​σ2​(τ−k))​𝑑k−Ω​(τ)​f​(τ),absentsuperscriptsubscript0𝜏Ω𝑘superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘4superscript𝜎3𝜋superscript𝜏𝑘31superscript𝑦𝜏𝑦𝑘22superscript𝜎2𝜏𝑘differential-d𝑘Ω𝜏𝑓𝜏\displaystyle=\int\_{0}^{\tau}\Omega(k)\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}\left(1-\frac{(y(\tau)-y(k))^{2}}{2\sigma^{2}(\tau-k)}\right)dk-\Omega(\tau)f(\tau), |  | (70) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(τ)𝑓𝜏\displaystyle f(\tau) | =±y′​(τ)2​σ4+12​σ3​π​τ​e−(y​(τ)−y​(0))24​σ2​τabsentplus-or-minussuperscript𝑦′𝜏2superscript𝜎412superscript𝜎3𝜋𝜏superscript𝑒superscript𝑦𝜏𝑦024superscript𝜎2𝜏\displaystyle=\pm\frac{y^{\prime}(\tau)}{2\sigma^{4}}+\frac{1}{2\sigma^{3}\sqrt{\pi\tau}}e^{-\frac{(y(\tau)-y(0))^{2}}{4\sigma^{2}\tau}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−(y​(τ)−y​(k))24​σ2​(τ−k)4​σ3​π​(τ−k)3​{1+y′​(k)​[y​(τ)−y​(k)]σ2−(y​(τ)−y​(k))22​σ2​(τ−k)}​𝑑k.superscriptsubscript0𝜏superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘4superscript𝜎3𝜋superscript𝜏𝑘31superscript𝑦′𝑘delimited-[]𝑦𝜏𝑦𝑘superscript𝜎2superscript𝑦𝜏𝑦𝑘22superscript𝜎2𝜏𝑘differential-d𝑘\displaystyle+\int\_{0}^{\tau}\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}\left\{1+\frac{y^{\prime}(k)[y(\tau)-y(k)]}{\sigma^{2}}-\frac{(y(\tau)-y(k))^{2}}{2\sigma^{2}(\tau-k)}\right\}dk. |  |

Thus, we proved that the derivative ∂q​(τ,x)/∂x𝑞𝜏𝑥𝑥\partial q(\tau,x)/\partial x is also discontinuous at x=y​(τ)𝑥𝑦𝜏x=y(\tau), and obtained its explicit representation in Eq. ([70](#S3.E70 "Equation 70 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Note, that this derivative should not be confused with the normal (directional) derivative of u​(τ,x)𝑢𝜏𝑥u(\tau,x) which is continuous at x=y​(τ)𝑥𝑦𝜏x=y(\tau). Indeed, the function q𝑞q, as defined in Eq. ([52](#S3.E52 "Equation 52 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), is the double layer heat potential. The claim that this derivative is continuous is commonly referred as the Lyapunov-Tauber theorem of classic potential theory, see (Lyapunov, [1949](#bib.bib26)), and (Guinter, [1967](#bib.bib13); Quaife, [2011](#bib.bib30); Costabel, [1990](#bib.bib6); Kristensson, [2009](#bib.bib21)) and references therein for the extension to the multi-dimensional case.

It is worth mentioning, that the formula for f​(τ)𝑓𝜏f(\tau) can be further simplified. Indeed

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(e−(y​(τ)−y​(k))24​σ2​(τ−k)τ−k)𝑑superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘𝜏𝑘\displaystyle d\left(\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{\sqrt{\tau-k}}\right) | =[e−(y​(τ)−y​(k))24​σ2​(τ−k)2​(τ−k)3−e−(y​(τ)−y​(k))24​σ2​(τ−k)τ−k​(−y′​(k)​(y​(τ)−y​(k))2​σ2​(τ−k)+(y​(τ)−y​(k))24​σ2​(τ−k)2)]​d​kabsentdelimited-[]superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘2superscript𝜏𝑘3superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘𝜏𝑘superscript𝑦′𝑘𝑦𝜏𝑦𝑘2superscript𝜎2𝜏𝑘superscript𝑦𝜏𝑦𝑘24superscript𝜎2superscript𝜏𝑘2𝑑𝑘\displaystyle=\left[\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{2\sqrt{(\tau-k)^{3}}}-\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{\sqrt{\tau-k}}\left(-\frac{y^{\prime}(k)(y(\tau)-y(k))}{2\sigma^{2}(\tau-k)}+\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)^{2}}\right)\right]dk |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−(y​(τ)−y​(k))24​σ2​(τ−k)2​(τ−k)3​(1+y′​(k)​(y​(τ)−y​(k))σ2​(τ−k)−(y​(τ)−y​(k))22​σ2​(τ−k)2)​d​k.absentsuperscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘2superscript𝜏𝑘31superscript𝑦′𝑘𝑦𝜏𝑦𝑘superscript𝜎2𝜏𝑘superscript𝑦𝜏𝑦𝑘22superscript𝜎2superscript𝜏𝑘2𝑑𝑘\displaystyle=\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{2\sqrt{(\tau-k)^{3}}}\left(1+\frac{y^{\prime}(k)(y(\tau)-y(k))}{\sigma^{2}(\tau-k)}-\frac{(y(\tau)-y(k))^{2}}{2\sigma^{2}(\tau-k)^{2}}\right)dk. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−(y​(τ)−y​(k))24​σ2​(τ−k)2​(τ−k)3​(1+y′​(k)​(y​(τ)−y​(k))σ2​(τ−k)−(y​(τ)−y​(k))22​σ2​(τ−k)2)​d​k=d​(e−(y​(τ)−y​(k))24​σ2​(τ−k)−1τ−k)+d​k2​(τ−k)3.superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘2superscript𝜏𝑘31superscript𝑦′𝑘𝑦𝜏𝑦𝑘superscript𝜎2𝜏𝑘superscript𝑦𝜏𝑦𝑘22superscript𝜎2superscript𝜏𝑘2𝑑𝑘𝑑superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘1𝜏𝑘𝑑𝑘2superscript𝜏𝑘3\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{2\sqrt{(\tau-k)^{3}}}\left(1+\frac{y^{\prime}(k)(y(\tau)-y(k))}{\sigma^{2}(\tau-k)}-\frac{(y(\tau)-y(k))^{2}}{2\sigma^{2}(\tau-k)^{2}}\right)dk=d\left(\frac{e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}-1}{\sqrt{\tau-k}}\right)+\frac{dk}{2\sqrt{(\tau-k)^{3}}}. |  | (71) |

Plugging this expression into the formula for f​(τ)𝑓𝜏f(\tau) and integrating yields an alternative representation for f​(τ)𝑓𝜏f(\tau)

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(τ)=±y′​(τ)2​σ4+12​σ3​π​τ+∫0τd​k4​σ3​π​(τ−k)3,𝑓𝜏plus-or-minussuperscript𝑦′𝜏2superscript𝜎412superscript𝜎3𝜋𝜏superscriptsubscript0𝜏𝑑𝑘4superscript𝜎3𝜋superscript𝜏𝑘3f(\tau)=\pm\frac{y^{\prime}(\tau)}{2\sigma^{4}}+\frac{1}{2\sigma^{3}\sqrt{\pi\tau}}+\int\_{0}^{\tau}\frac{dk}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}, |  | (72) |

and for ψ​(τ)𝜓𝜏\psi(\tau), respectively

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ​(τ)𝜓𝜏\displaystyle\psi(\tau) | =−Ω​(τ)​(12​σ3​π​τ±y′​(τ)2​σ4)+∫0τΩ​(k)​e−(y​(τ)−y​(k))24​σ2​(τ−k)−Ω​(τ)4​σ3​π​(τ−k)3​𝑑kabsentΩ𝜏plus-or-minus12superscript𝜎3𝜋𝜏superscript𝑦′𝜏2superscript𝜎4superscriptsubscript0𝜏Ω𝑘superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘Ω𝜏4superscript𝜎3𝜋superscript𝜏𝑘3differential-d𝑘\displaystyle=-\Omega(\tau)\left(\frac{1}{2\sigma^{3}\sqrt{\pi\tau}}\pm\frac{y^{\prime}(\tau)}{2\sigma^{4}}\right)+\int\_{0}^{\tau}\frac{\Omega(k)e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}-\Omega(\tau)}{4\sigma^{3}\sqrt{\pi(\tau-k)^{3}}}dk |  | (73) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0τΩ​(k)​(y​(τ)−y​(k))2​e−(y​(τ)−y​(k))24​σ2​(τ−k)8​σ5​π​(τ−k)5​𝑑k.superscriptsubscript0𝜏Ω𝑘superscript𝑦𝜏𝑦𝑘2superscript𝑒superscript𝑦𝜏𝑦𝑘24superscript𝜎2𝜏𝑘8superscript𝜎5𝜋superscript𝜏𝑘5differential-d𝑘\displaystyle-\int\_{0}^{\tau}\Omega(k)\frac{(y(\tau)-y(k))^{2}e^{-\frac{(y(\tau)-y(k))^{2}}{4\sigma^{2}(\tau-k)}}}{8\sigma^{5}\sqrt{\pi(\tau-k)^{5}}}dk. |  |

The last formula for the particular case σ=1/2𝜎12\sigma=1/\sqrt{2} was also obtained in (Lipton et al., [2019](#bib.bib25)) by using a different method.

### 3.3 A system of Volterra equations

With allowance for the representation obtained in Eq. ([62](#S3.E62 "Equation 62 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), by substituting the limiting values x→y​(τ)→𝑥𝑦𝜏x\to y(\tau) and x→z​(τ)→𝑥𝑧𝜏x\to z(\tau) into Eq. ([49](#S3.E49 "Equation 49 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), we obtain a system of two integral equation for functions Ω​(τ),Θ​(τ)

Ω𝜏Θ𝜏\Omega(\tau),\Theta(\tau)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 2​ϕ1​(τ)2subscriptitalic-ϕ1𝜏\displaystyle 2\phi\_{1}(\tau) | =Ω​(τ)+12​π​∫0τ(Ω​(k)​y​(τ)−y​(k)(τ−k)3/2​e−(y​(τ)−y​(k))24​(τ−k)+Θ​(k)​y​(τ)−z​(k)(τ−k)3/2​e−(y​(τ)−z​(k))24​(τ−k))​𝑑k,absentΩ𝜏12𝜋superscriptsubscript0𝜏Ω𝑘𝑦𝜏𝑦𝑘superscript𝜏𝑘32superscript𝑒superscript𝑦𝜏𝑦𝑘24𝜏𝑘Θ𝑘𝑦𝜏𝑧𝑘superscript𝜏𝑘32superscript𝑒superscript𝑦𝜏𝑧𝑘24𝜏𝑘differential-d𝑘\displaystyle=\Omega(\tau)+\frac{1}{2\sqrt{\pi}}\int\_{0}^{\tau}\left(\Omega(k)\frac{y(\tau)-y(k)}{(\tau-k)^{3/2}}e^{-\frac{(y(\tau)-y(k))^{2}}{4(\tau-k)}}+\Theta(k)\frac{y(\tau)-z(k)}{(\tau-k)^{3/2}}e^{-\frac{(y(\tau)-z(k))^{2}}{4(\tau-k)}}\right)dk, |  | (74) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​ψ1​(τ)2subscript𝜓1𝜏\displaystyle 2\psi\_{1}(\tau) | =−Θ​(τ)+12​π​∫0τ(Ω​(k)​z​(τ)−y​(k)(τ−k)3/2​e−(z​(τ)−y​(k))24​(τ−k)+Θ​(k)​z​(τ)−z​(k)(τ−k)3/2​e−(z​(τ)−z​(k))24​(τ−k))​𝑑k.absentΘ𝜏12𝜋superscriptsubscript0𝜏Ω𝑘𝑧𝜏𝑦𝑘superscript𝜏𝑘32superscript𝑒superscript𝑧𝜏𝑦𝑘24𝜏𝑘Θ𝑘𝑧𝜏𝑧𝑘superscript𝜏𝑘32superscript𝑒superscript𝑧𝜏𝑧𝑘24𝜏𝑘differential-d𝑘\displaystyle=-\Theta(\tau)+\frac{1}{2\sqrt{\pi}}\int\_{0}^{\tau}\left(\Omega(k)\frac{z(\tau)-y(k)}{(\tau-k)^{3/2}}e^{-\frac{(z(\tau)-y(k))^{2}}{4(\tau-k)}}+\Theta(k)\frac{z(\tau)-z(k)}{(\tau-k)^{3/2}}e^{-\frac{(z(\tau)-z(k))^{2}}{4(\tau-k)}}\right)dk. |  |

Each equation in this system is a Volterra equation of the second kind. The system can be solved, eg., by the Variational Iteration Method (VIM), see (Wazwaz, [2011](#bib.bib34)) with a linear complexity by using the Fast Gaussian Transform. Once this is done, the solution of our double barrier problem is found.

It is interesting that the representation of the solution gradient in Eq. ([73](#S3.E73 "Equation 73 ‣ 3.2 The limiting value of 𝜓⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) provides connection between the GIT and HP methods. Indeed, by definition in Eq. ([13](#S2.E13 "Equation 13 ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and also using Eq. ([7](#S1.E7 "Equation 7 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), Eq. ([47](#S3.E47 "Equation 47 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ψ​(τ)Ψ𝜏\displaystyle\Psi(\tau) | =−∂U​(τ,x)∂x|x=y​(τ)absentevaluated-at𝑈𝜏𝑥𝑥𝑥𝑦𝜏\displaystyle=-\frac{\partial U(\tau,x)}{\partial x}\Bigg{|}\_{x=y(\tau)} |  | (75) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∂q​(τ,x)∂x|x=y​(τ)+0+14​π​τ3​∫y​(0)z​(0)U​(0,x′)​(y​(τ)−x′)​e−(y​(τ)−x′)24​τ​𝑑x′,absentevaluated-at𝑞𝜏𝑥𝑥𝑥𝑦𝜏014𝜋superscript𝜏3superscriptsubscript𝑦0𝑧0𝑈0superscript𝑥′𝑦𝜏superscript𝑥′superscript𝑒superscript𝑦𝜏superscript𝑥′24𝜏differential-dsuperscript𝑥′\displaystyle=-\frac{\partial q(\tau,x)}{\partial x}\Bigg{|}\_{x=y(\tau)+0}+\frac{1}{4\sqrt{\pi\tau^{3}}}\int\_{y(0)}^{z(0)}U(0,x^{\prime})(y(\tau)-x^{\prime})e^{-\frac{(y(\tau)-x^{\prime})^{2}}{4\tau}}dx^{\prime}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(τ)Φ𝜏\displaystyle\Phi(\tau) | =∂U​(τ,x)∂τ|x=z​(τ)absentevaluated-at𝑈𝜏𝑥𝜏𝑥𝑧𝜏\displaystyle=\frac{\partial U(\tau,x)}{\partial\tau}\Bigg{|}\_{x=z(\tau)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∂q​(τ,x)∂x|x=z​(τ)−0+14​π​τ3​∫y​(0)z​(0)U​(0,x′)​(z​(τ)−x′)​e−(z​(τ)−x′)24​τ​𝑑x′.absentevaluated-at𝑞𝜏𝑥𝑥𝑥𝑧𝜏014𝜋superscript𝜏3superscriptsubscript𝑦0𝑧0𝑈0superscript𝑥′𝑧𝜏superscript𝑥′superscript𝑒superscript𝑧𝜏superscript𝑥′24𝜏differential-dsuperscript𝑥′\displaystyle=\frac{\partial q(\tau,x)}{\partial x}\Bigg{|}\_{x=z(\tau)-0}+\frac{1}{4\sqrt{\pi\tau^{3}}}\int\_{y(0)}^{z(0)}U(0,x^{\prime})(z(\tau)-x^{\prime})e^{-\frac{(z(\tau)-x^{\prime})^{2}}{4\tau}}dx^{\prime}. |  |

Therefore, once the pair Ω​(τ),Θ​(τ)

Ω𝜏Θ𝜏\Omega(\tau),\Theta(\tau) is known, the other pair Ψ​(τ),Φ​(τ)

Ψ𝜏Φ𝜏\Psi(\tau),\Phi(\tau) can be obtained explicitly from Eq. ([75](#S3.E75 "Equation 75 ‣ 3.3 A system of Volterra equations ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). The opposite is also true, i.e., once the pair Ψ​(τ),Φ​(τ)

Ψ𝜏Φ𝜏\Psi(\tau),\Phi(\tau) is known, the heat potential densities Ω​(τ),Θ​(τ)

Ω𝜏Θ𝜏\Omega(\tau),\Theta(\tau) can be found by solving this system of Volterra equations of the second kind. Thus, both the GIT and HP methods are interchangeable. But as was mentioned in Introduction, despite
both solutions are equal, their convergence properties are different.

## 4 Discussion

In this paper we extend the technique of semi-analytic (or semi-closed form) solutions, developed in (Carr and Itkin, [2020](#bib.bib4); Itkin and Muravey, [2020](#bib.bib15); Carr et al., [2020](#bib.bib5); Itkin et al., [2020a](#bib.bib16); Lipton and Kaushansky, [2018](#bib.bib24); Lipton and de Prado, [2020](#bib.bib23)), to pricing double barrier options and present two approaches to solving it: the General Integral transform method and the Heat Potential method. By semi-analytic solution we mean that first, we need to solve a system of two linear Volterra equations of the second kind, and then the option price is represented as a one-dimensional integral.

Therefore, perhaps the main point is about efficiency and robustness of the proposed approach. As shown in (Carr and Itkin, [2020](#bib.bib4); Itkin and Muravey, [2020](#bib.bib15); Carr et al., [2020](#bib.bib5); Itkin et al., [2020a](#bib.bib16)), from the computational point of view the solution proposed by using the same technique for pricing single barrier options under various models with time-dependent barriers is very efficient and, at least theoretically, of the same complexity, or even faster than the forward finite-difference (FD) method. On the other hand, our approach provides high accuracy in computing the options prices, as this is regulated by quadrature rule used to discretize the integral kernel in Eq. ([36](#S2.E36 "Equation 36 ‣ 2.3 Determining Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) Eq. ([41](#S2.E41 "Equation 41 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))), or in Eq. ([74](#S3.E74 "Equation 74 ‣ 3.3 A system of Volterra equations ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Therefore, the accuracy of the method in x𝑥x space can be easily increased by using high order quadratures. For instance, using the Simpson instead of the trapezoid rule doesn’t affect the complexity of our method but increases the accuracy, while increasing the accuracy for the FD method is not easy (i.e., it significantly increases the complexity of the method, e.g., see (Itkin, [2017](#bib.bib14))).

As applied to pricing double barrier options - the problem considered in this paper, the difference is that instead of a single Volterra equation of the second kind we now have to solve a system of two equations, either in Eq. ([36](#S2.E36 "Equation 36 ‣ 2.3 Determining Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) Eq. ([41](#S2.E41 "Equation 41 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))), or in Eq. ([74](#S3.E74 "Equation 74 ‣ 3.3 A system of Volterra equations ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). This can be done in the same way as for the single barrier problem. The Volterra equation is solved by discretizing the kernel of the integral in time using some quadrature rule which yields a system of linear equations with respect to the discrete values of Ψ​(τ),Φ​(τ)

Ψ𝜏Φ𝜏\Psi(\tau),\Phi(\tau). It can be checked that the matrix of this system is of the form

|  |  |  |
| --- | --- | --- |
|  | 𝐌=(ABCD),𝐌matrix𝐴𝐵𝐶𝐷\displaystyle\mathbf{M}=\begin{pmatrix}A&B\\ C&D\\ \end{pmatrix}, |  |

where A,D

𝐴𝐷A,D are lower triangular matrices with ones on the main diagonal, and B,C

𝐵𝐶B,C are lower triangular matrices with zeros on the main diagonal. Therefore, this system can be solved by a simple Gauss elimination method (by a set of algebraic multiplications and additions) with complexity O​(2​N)𝑂2𝑁O(2N) where N𝑁N is the number of the discretization points in τ𝜏\tau for Ψ​(τ),Φ​(τ)

Ψ𝜏Φ𝜏\Psi(\tau),\Phi(\tau). Alternatively, when using Eq. ([74](#S3.E74 "Equation 74 ‣ 3.3 A system of Volterra equations ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) or Eq. ([41](#S2.E41 "Equation 41 ‣ 2.5 A system of Volterra equations for Ψ⁢(𝜏) and Φ⁢(𝜏) ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), since the kernel is proportional to Gaussians, the discrete sum approximating the integral can be computed with linear complexity O​(2​N)𝑂2𝑁O(2N) using the Fast Gauss Transform, see eg., (Spivak et al., [2010](#bib.bib31)).

Once the vectors Ψ​(τ),Φ​(τ)

Ψ𝜏Φ𝜏\Psi(\tau),\Phi(\tau) (for the GIT method), or Ω​(τ),Θ​(τ)

Ω𝜏Θ𝜏\Omega(\tau),\Theta(\tau) (for the HP method) are found, they can be substituted into Eq. ([34](#S2.E34 "Equation 34 ‣ 2.2 Connection to the Jacobi theta function ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) or Eq. ([2.4](#S2.Ex55 "2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) for the GIT method), or into Eq. ([49](#S3.E49 "Equation 49 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) (for the HP method). Then the final solution is obtained by computing the integral(s) numerically.
Various numerical examples illustrating this technique for a single barrier pricing problem can be found in (Carr and Itkin, [2020](#bib.bib4); Itkin and Muravey, [2020](#bib.bib15); Carr et al., [2020](#bib.bib5); Itkin et al., [2020a](#bib.bib16)). Also, those examples demonstrate that computationally our method is more efficient than both the backward and even forward FD methods (if one uses them to solve this kind of problems), while providing better accuracy and stability.

Somebody could be a bit confused of this terminology, since despite the solution is found explicitly as an integral, the latter depends of the unknown function of time Ψ​(τ)Ψ𝜏\Psi(\tau). In support of this terminology, we can mention that the solution is definitely of a closed form on variable x𝑥x. On variable τ𝜏\tau the integrand explicitly depends on yet unknown function Ψ​(τ)Ψ𝜏\Psi(\tau) which solves the Volterra integral equation of the second kind. However, this equation can be solved with no iterations. Indeed, after the function Ψ​(τ)Ψ𝜏\Psi(\tau) is discretized on some grid in τ𝜏\tau (so now it is represented by a finite vector ψ𝜓\psi), the integral equation reduces to the linear equation for ψ𝜓\psi, with the matrix being low triangular. Thus, the solution can be immediately obtained by a simple Gauss elimination with no iterations. Therefore, this is explicit and as such, the solution is given by a series of algebraic operations (substitutions). The finer is the grid, the closer is the solution to the exact one.

Also, we can make a reference to Lipton and de Prado ([2020](#bib.bib23)); Carr et al. ([2020](#bib.bib5)) where the phrase "semi-closed" was used verbatim. And in Lipton et al. ([2019](#bib.bib25)); Lipton and Kaushansky ([2018](#bib.bib24)) it is called as "semi-analytical" solution. Going back in time, in Kartashov and Lyubov ([1974](#bib.bib20)); Kartashov ([1999](#bib.bib18), [2001](#bib.bib19)) both GIT and HP methods are claimed as analytical. One can also look at Tikhonov and Samarskii ([1963](#bib.bib32)), page 533, subsection 2, which from the very beginning says, "Heat potentials are a convenient analytical device for solving boundary-value problems". Therefore, we think this terminology is appropriate.

Also, as mentioned in (Carr et al., [2020](#bib.bib5)), another advantage of the approach advocated in this paper is computation of option Greeks. Indeed, in both the HP and GIT methods the option prices are represented in an explicit analytic form on x𝑥x (via the integrals on τ𝜏\tau and the auxiliary variable ξ𝜉\xi). This means that an explicit dependence of the option prices on the model parameters is available and transparent. Thus, explicit representations of the option Greeks can be obtained by a simple differentiation under the integrals. This means that the Greek values can be computed simultaneously with the option prices with almost no additional increase in the elapsed time. This is possible because differentiation under the integrals slightly changes the integrands, while these changes could be represented as changes in weights of the quadrature scheme used to compute the integrals.

Also, the integrands in the integral representation of the solution could be treated as a product of some density function and weights. The major computational time is spent for computing the densities as they contain special functions. However, once computed the results can be saved during the calculation of prices, and then reused when computing the Greeks. Therefore, computing Greeks can be done very fast. This is also true eg., for Vega and other Greeks that cannot be computed by the FD method together with prices and require a separate run of the FD machinery. Here we don’t have such a problem as differentiation of the integral representation with respect to the model parameters is done analytically.

Finally, as mentioned in (Itkin and Muravey, [2020](#bib.bib15)), the GIT and HP methods are complementary. In more detail, this means the following. Our experiments showed that performance of both the GIT and HP methods is same. However, the GIT method produces more accurate results at high strikes and maturities (i.e. where the option price is relatively small) in contrast to the HP method which is more accurate at short maturities and low strikes. For the CIR and CEV models this behavior was explained in (Carr et al., [2020](#bib.bib5)), and for the Hull-White model - in (Itkin and Muravey, [2020](#bib.bib15)). Briefly, for the heat equation that we consider in this paper, the exponents in both the HP and GIT integrals are inversely proportional to τ𝜏\tau. However, the GIT integrals contain a difference of two exponents (see the definition of Υn​(x,τ|ξ,s)subscriptΥ𝑛𝑥conditional𝜏

𝜉𝑠\Upsilon\_{n}(x,\tau\,|\,\xi,s) in Eq. ([2.4](#S2.Ex55 "2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) which becomes small at large τ𝜏\tau. On contrary, the HP exponent in Eq. ([49](#S3.E49 "Equation 49 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) tends to 1 at large τ𝜏\tau. Therefore, the convergence properties of two methods are different at large τ𝜏\tau.

This situation is well known for the heat equation with constant coefficients. There exist two representation of the solution: one - obtained by using the method of images, and the other one - by the Fourier series. Despite both solutions are equal as the infinite series, their convergence properties are different.

## Acknowledgments

We are grateful to Alex Lipton for some fruitful discussions. Dmitry Muravey acknowledges support by the Russian Science Foundation under the Grant number 20-68-47030.

## References

* Bouchouev (2020)

  I. Bouchouev.
  Negative oil prices put spotlight on investors.
  *Risk.net*, 2020.
* Brogan (2020)

  R. Brogan.
  Options traders adapt to electronic markets in pandemic, 2020.
  URL
  https://flextrade.com/options-traders-adapt-to-electronic-markets-in-pandemic/.
* Butuzov and Butuzova (2016)

  V.F. Butuzov and M.V. Butuzova.
  *Integrals depending on parameters*.
  Moscow State University, Moscow, 2016.
  in Russian.
* Carr and Itkin (2020)

  P. Carr and A. Itkin.
  Semi-closed form solutions for barrier and American options written
  on a time-dependent Ornstein Uhlenbeck process, March 2020.
  Arxiv:2003.08853.
* Carr et al. (2020)

  P. Carr, A. Itkin, and D. Muravey.
  Semi-closed form prices of barrier options in the time-dependent cev
  and cir models.
  *Journal of Derivatives*, 28(1):26–50,
  2020.
* Costabel (1990)

  M. Costabel.
  Boundary integral operators for the heat equation.
  *Integral Equations and Operator Theory*, 13(4):498–552, 1990.
* (7)

  C.J. Dias.
  A method of recursive images to solve transient heat diffusionin
  multilayer materials.
  85:1075–1083.
* (8)

  DLMF.
  NIST Digital Library of Mathematical Functions.
  http://dlmf.nist.gov/, Release 1.0.28 of 2020-09-15.
  URL http://dlmf.nist.gov/.
  F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider,
  R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and
  M. A. McClain, eds.
* Doff (2020)

  R. Doff.
  Valuing scenarios with real option pricing.
  *Risk.net*, August 2020.
* Farrington and Cesa (2020)

  S. Farrington and M. Cesa.
  Podcast: Kaminski and ronn on negative oil and options pricing.
  *Risk.net*, May 2020.
* Friedman (1964.)

  A. Friedman.
  *Partial Differential Equations of Parabolic Type*.
  Prentice-Hall, New Jersey,, 1964.
* Gradshtein and Ryzhik (2007)

  I.S. Gradshtein and I.M. Ryzhik.
  *Table of Integrals, Series, and Products*.
  Elsevier, 2007.
* Guinter (1967)

  N.M. Guinter.
  *Potential Theory and Its Applications to Basic Problems of
  MathematicalPhysics*.
  Frederick Ungar, New York, 1967.
* Itkin (2017)

  A. Itkin.
  *Pricing Derivatives Under Lévy Models. Modern
  Finite-Difference and Pseudo-Differential Operators Approach.*, volume 12 of
  *Pseudo-Differential Operators*.
  Birkhauser, 2017.
* Itkin and Muravey (2020)

  A. Itkin and D. Muravey.
  Semi-closed form prices of barrier options in the Hull-White model,
  April 2020.
  Arxiv:2004.09591.
* Itkin et al. (2020a)

  A. Itkin, A. Lipton, and D. Muravey.
  From the black-karasinski to the verhulst model to accommodate the
  unconventional fed’s policy, June 2020a.
  URL https://arxiv.org/abs/2006.11976.
* Itkin et al. (2020b)

  A. Itkin, A. Lipton, and D. Muravey.
  Multilayer heat equations: application to finance.
  in preparation, 2020b.
* Kartashov (1999)

  E. M. Kartashov.
  Analytical methods for solution of non-stationary heat conductance
  boundary problems in domains with moving boundaries.
  *Izvestiya RAS, Energetika*, (5):133–185,
  1999.
* Kartashov (2001)

  E.M. Kartashov.
  *Analytical Methods in the Theory of Heat Conduction in Solids*.
  Vysshaya Shkola, Moscow, 2001.
* Kartashov and Lyubov (1974)

  E.M. Kartashov and B. Ya Lyubov.
  Analytical methods in the theory of heat conduction in solids.
  *Izv. Akad. Nauk SSSR, Energ. Trans.*, (6):83–111, 1974.
* Kristensson (2009)

  G. Kristensson.
  Jump conditions for single and doublelayer potentials, 2009.
  file:///C:/AndreyItkin/MyFinance/FinPapers/BK/liter/JumpConditions.pdf.
* Lipton (2002)

  A. Lipton.
  The vol smile problem.
  *Risk*, pages 61–65, February 2002.
* Lipton and de Prado (2020)

  A. Lipton and M.L. de Prado.
  A closed-form solution for optimal mean-reverting trading strategies,
  2020.
  available at
  https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3534445.
* Lipton and Kaushansky (2018)

  A. Lipton and V. Kaushansky.
  On the first hitting time density of an ornstein-uhlenbeck process,
  October 2018.
  URL https://arxiv.org/pdf/1810.02390.pdf.
* Lipton et al. (2019)

  A. Lipton, V. Kaushansky, and C. Reisinger.
  Semi-analytical solution of a McKean-Vlasov equation with feedback
  through hitting boundary.
  *Euro. Jnl of Applied Mathematics*, pages 1–34, 2019.
* Lyapunov (1949)

  A.M. Lyapunov.
  *Works on the theory of potential*.
  Technical and Theoretical State Publishing House, Moscow - Leningrad,
  1949.
  in Russian.
* Mijatovic (2010)

  A. Mijatovic.
  Local time and the pricing of time-dependent barrier options.
  *Finance and Stochastics*, 14(1):13–48,
  2010.
* Mumford et al. (1983)

  D. Mumford, C. Musiliand M. Nori, E. Previato, and M. Stillman.
  *Tata Lectures on Theta*.
  Progress in Mathematics. Birkhäuser Boston, 1983.
  ISBN 9780817631093.
* Polyanin (2002)

  A.D. Polyanin.
  *Handbook of linear partial differential equations for engineers
  and scientists*.
  Chapman & Hall/CRC, 2002.
* Quaife (2011)

  B. Quaife.
  *Fast Integral Equation Methods for the Modified Helmholtz
  Equation*.
  PhD thesis, University of Calgary, 2011.
* Spivak et al. (2010)

  M. Spivak, S.K. Veerapaneni, and L. Greengard.
  The fast generalized gauss transform.
  *SIAM Journal on Scientific Computing*, 32(5):3092–3107, 2010.
* Tikhonov and Samarskii (1963)

  A.N. Tikhonov and A.A. Samarskii.
  *Equations of mathematical physics*.
  Pergamon Press, Oxford, 1963.
* van der Pol and Bremmer (1950)

  B. van der Pol and H. Bremmer.
  *Operational calculus based on the two- sided Laplace integral*.
  Cambridge University Press, Cambridge, UK, 1950.
* Wazwaz (2011)

  A. M. Wazwaz.
  *Linear and Nonlinear Integral Equations*.
  Higher Education Press, Beijing and Springer-Verlag GmbH Berlin
  Heidelberg, 2011.

\appendixpage

## Appendix A Simplification of Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

To simplify Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) we proceed by integrating by parts the last integral in Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

|  |  |  |
| --- | --- | --- |
|  | ∫0τe−π2​n2l2​(τ)​(τ−s)​h1​(n,s,τ)​𝑑s=−B​(τ)​l2​(τ)π2​n2​[sin⁡(π​nl​(τ)​[z​(τ)−y​(τ)])−sin⁡(π​nl​(τ)​[y​(τ)−y​(τ)])]superscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠subscriptℎ1𝑛𝑠𝜏differential-d𝑠𝐵𝜏superscript𝑙2𝜏superscript𝜋2superscript𝑛2delimited-[]𝜋𝑛𝑙𝜏delimited-[]𝑧𝜏𝑦𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦𝜏𝑦𝜏\displaystyle\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}h\_{1}(n,s,\tau)ds=-\frac{B(\tau)l^{2}(\tau)}{\pi^{2}n^{2}}\left[\sin\left(\frac{\pi n}{l(\tau)}[z(\tau)-y(\tau)]\right)-\sin\left(\frac{\pi n}{l(\tau)}[y(\tau)-y(\tau)]\right)\right] |  |
|  |  |  |
| --- | --- | --- |
|  | +B​(0)​l2​(τ)π2​k2​e−π2​n2l2​(τ)​τ​[sin⁡(π​nl​(τ)​[z​(0)−y​(τ)])−sin⁡(π​nl​(τ)​[y​(0)−y​(τ)])]𝐵0superscript𝑙2𝜏superscript𝜋2superscript𝑘2superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏delimited-[]𝜋𝑛𝑙𝜏delimited-[]𝑧0𝑦𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦0𝑦𝜏\displaystyle+\frac{B(0)l^{2}(\tau)}{\pi^{2}k^{2}}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\left[\sin\left(\frac{\pi n}{l(\tau)}[z(0)-y(\tau)]\right)-\sin\left(\frac{\pi n}{l(\tau)}[y(0)-y(\tau)]\right)\right] |  |
|  |  |  |
| --- | --- | --- |
|  | −l​(τ)π​n​[f−​(τ)​cos⁡(π​nl​(τ)​[y​(τ)−y​(τ)])−f+​(τ)​cos⁡(π​nl​(τ)​[z​(τ)−y​(τ)])]𝑙𝜏𝜋𝑛delimited-[]superscript𝑓𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦𝜏𝑦𝜏superscript𝑓𝜏𝜋𝑛𝑙𝜏delimited-[]𝑧𝜏𝑦𝜏\displaystyle-\frac{l(\tau)}{\pi n}\Bigg{[}f^{-}(\tau)\cos\left(\frac{\pi n}{l(\tau)}[y(\tau)-y(\tau)]\right)-f^{+}(\tau)\cos\left(\frac{\pi n}{l(\tau)}[z(\tau)-y(\tau)]\right)\Bigg{]} |  |
|  |  |  |
| --- | --- | --- |
|  | +l​(τ)π​n​e−π2​n2l2​(τ)​τ​[f−​(0)​cos⁡(π​nl​(τ)​[y​(0)−y​(τ)])−f+​(0)​cos⁡(π​nl​(τ)​[z​(0)−y​(τ)])]𝑙𝜏𝜋𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏delimited-[]superscript𝑓0𝜋𝑛𝑙𝜏delimited-[]𝑦0𝑦𝜏superscript𝑓0𝜋𝑛𝑙𝜏delimited-[]𝑧0𝑦𝜏\displaystyle+\frac{l(\tau)}{\pi n}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\Bigg{[}f^{-}(0)\cos\left(\frac{\pi n}{l(\tau)}[y(0)-y(\tau)]\right)-f^{+}(0)\cos\left(\frac{\pi n}{l(\tau)}[z(0)-y(\tau)]\right)\Bigg{]} |  |
|  |  |  |
| --- | --- | --- |
|  | +l2​(τ)π2​n2∫0τB(s)e−π2​n2l2​(τ)​(τ−s)(π2​n2l2​(τ)[sin(π​nl​(τ)[z(s)−y(τ)])−sin(π​nl​(τ)[y(s)−y(τ)])]\displaystyle+\frac{l^{2}(\tau)}{\pi^{2}n^{2}}\int\_{0}^{\tau}B(s)e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\Bigg{(}\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\left[\sin\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)-\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)\right] |  |
|  |  |  |
| --- | --- | --- |
|  | +π​nl​(τ)[z′(s)cos(π​nl​(τ)[z(s)−y(τ)])−y′(s)cos(π​nl​(τ)[y(s)−y(τ)])])ds\displaystyle+\frac{\pi n}{l(\tau)}\left[z^{\prime}(s)\cos\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)-y^{\prime}(s)\cos\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)\right]\Bigg{)}ds |  |
|  |  |  |
| --- | --- | --- |
|  | +l​(τ)π​n​∫0τf−​(s)​e−π2​n2l2​(τ)​(τ−s)​(π2​n2l2​(τ)​cos⁡(π​nl​(τ)​[y​(s)−y​(τ)])−π​nl​(τ)​y′​(s)​sin⁡(π​nl​(τ)​[y​(s)−y​(τ)]))​𝑑s𝑙𝜏𝜋𝑛superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏𝜋𝑛𝑙𝜏superscript𝑦′𝑠𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏differential-d𝑠\displaystyle+\frac{l(\tau)}{\pi n}\int\_{0}^{\tau}f^{-}(s)e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\Bigg{(}\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\cos\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)-\frac{\pi n}{l(\tau)}y^{\prime}(s)\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)\Bigg{)}ds |  |
|  |  |  |
| --- | --- | --- |
|  | −l​(τ)π​n​∫0τf+​(s)​e−π2​n2l2​(τ)​(τ−s)​(π2​n2l2​(τ)​cos⁡(π​nl​(τ)​[y​(s)−y​(τ)])−π​nl​(τ)​z′​(s)​sin⁡(π​nl​(τ)​[y​(s)−y​(τ)]))​𝑑s𝑙𝜏𝜋𝑛superscriptsubscript0𝜏superscript𝑓𝑠superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏𝜋𝑛𝑙𝜏superscript𝑧′𝑠𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏differential-d𝑠\displaystyle-\frac{l(\tau)}{\pi n}\int\_{0}^{\tau}f^{+}(s)e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\Bigg{(}\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\cos\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)-\frac{\pi n}{l(\tau)}z^{\prime}(s)\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)\Bigg{)}ds |  |
|  |  |  |
| --- | --- | --- |
|  | +l​(τ)π​n​∫0τB​(s)​e−π2​n2l2​(τ)​(τ−s)​[y′​(s)​cos⁡(π​nl​(τ)​[y​(s)−y​(τ)])−z′​(s)​cos⁡(π​nl​(τ)​[z​(s)−y​(τ)])]​𝑑s,𝑙𝜏𝜋𝑛superscriptsubscript0𝜏𝐵𝑠superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠delimited-[]superscript𝑦′𝑠𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏superscript𝑧′𝑠𝜋𝑛𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏differential-d𝑠\displaystyle+\frac{l(\tau)}{\pi n}\int\_{0}^{\tau}B(s)e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\Bigg{[}y^{\prime}(s)\cos\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)-z^{\prime}(s)\cos\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)\Bigg{]}ds, |  |

or

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0τsuperscriptsubscript0𝜏\displaystyle\int\_{0}^{\tau} | e−π2​n2l2​(τ)​(τ−s)​h1​(n,s,τ)​d​s=l​(τ)π​n​[(−1)n​f+​(τ)−f−​(τ)]+α​(τ,n)​e−π2​n2l2​(τ)​τ+∫0τe−π2​n2l2​(τ)​(τ−s)​β​(τ,s,n)​𝑑ssuperscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠subscriptℎ1𝑛𝑠𝜏𝑑𝑠𝑙𝜏𝜋𝑛delimited-[]superscript1𝑛superscript𝑓𝜏superscript𝑓𝜏𝛼𝜏𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏superscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝛽𝜏𝑠𝑛differential-d𝑠\displaystyle e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}h\_{1}(n,s,\tau)ds=\frac{l(\tau)}{\pi n}\Bigg{[}(-1)^{n}f^{+}(\tau)-f^{-}(\tau)\Bigg{]}+\alpha(\tau,n)e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\beta(\tau,s,n)ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)​B​(s)​[sin⁡(π​nl​(τ)​[z​(s)−y​(τ)])−sin⁡(π​nl​(τ)​[y​(s)−y​(τ)])]​𝑑s,superscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝐵𝑠delimited-[]𝜋𝑛𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏differential-d𝑠\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}B(s)\left[\sin\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)-\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)\right]ds, |  | (A.1) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | α​(τ,n)𝛼𝜏𝑛\displaystyle\alpha(\tau,n) | =B​(0)​l2​(τ)π2​n2​[sin⁡(π​nl​(τ)​[z​(0)−y​(τ)])−sin⁡(π​nl​(τ)​[y​(0)−y​(τ)])]absent𝐵0superscript𝑙2𝜏superscript𝜋2superscript𝑛2delimited-[]𝜋𝑛𝑙𝜏delimited-[]𝑧0𝑦𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦0𝑦𝜏\displaystyle=\frac{B(0)l^{2}(\tau)}{\pi^{2}n^{2}}\left[\sin\left(\frac{\pi n}{l(\tau)}[z(0)-y(\tau)]\right)-\sin\left(\frac{\pi n}{l(\tau)}[y(0)-y(\tau)]\right)\right] |  | (A.2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +l​(τ)π​n​e−π2​n2l2​(τ)​τ​[f−​(0)​cos⁡(π​nl​(τ)​[y​(0)−y​(τ)])−f+​(0)​cos⁡(π​nl​(τ)​[z​(0)−y​(τ)])],𝑙𝜏𝜋𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏delimited-[]superscript𝑓0𝜋𝑛𝑙𝜏delimited-[]𝑦0𝑦𝜏superscript𝑓0𝜋𝑛𝑙𝜏delimited-[]𝑧0𝑦𝜏\displaystyle+\frac{l(\tau)}{\pi n}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\Bigg{[}f^{-}(0)\cos\left(\frac{\pi n}{l(\tau)}[y(0)-y(\tau)]\right)-f^{+}(0)\cos\left(\frac{\pi n}{l(\tau)}[z(0)-y(\tau)]\right)\Bigg{]}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | β​(τ,s,n)𝛽𝜏𝑠𝑛\displaystyle\beta(\tau,s,n) | =f−​(s)​(π​nl​(τ)​cos⁡(π​nl​(τ)​[y​(s)−y​(τ)])−y′​(s)​sin⁡(π​nl​(τ)​[y​(s)−y​(τ)]))absentsuperscript𝑓𝑠𝜋𝑛𝑙𝜏𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏superscript𝑦′𝑠𝜋𝑛𝑙𝜏delimited-[]𝑦𝑠𝑦𝜏\displaystyle=f^{-}(s)\Bigg{(}\frac{\pi n}{l(\tau)}\cos\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)-y^{\prime}(s)\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)\Bigg{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −f+​(s)​(π​nl​(τ)​cos⁡(π​nl​(τ)​[z​(s)−y​(τ)])−z′​(s)​sin⁡(π​nl​(τ)​[z​(s)−y​(τ)])).superscript𝑓𝑠𝜋𝑛𝑙𝜏𝜋𝑛𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏superscript𝑧′𝑠𝜋𝑛𝑙𝜏delimited-[]𝑧𝑠𝑦𝜏\displaystyle-f^{+}(s)\Bigg{(}\frac{\pi n}{l(\tau)}\cos\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)-z^{\prime}(s)\sin\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)\Bigg{)}. |  |

Now we can transform the whole term

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2l​(τ)​∑n=1∞sin⁡(π​n​x−y​(τ)l​(τ))​∫0τe−π2​n2l2​(τ)​(τ−s)​h1​(n,s,τ)​𝑑s,2𝑙𝜏superscriptsubscript𝑛1𝜋𝑛𝑥𝑦𝜏𝑙𝜏superscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠subscriptℎ1𝑛𝑠𝜏differential-d𝑠\frac{2}{l(\tau)}\sum\_{n=1}^{\infty}\sin\left(\pi n\frac{x-y(\tau)}{l(\tau)}\right)\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}h\_{1}(n,s,\tau)ds, |  | (A.3) |

which appears in Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). For doing that, first let us consider the integral

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫y​(0)z​(0)u​(0,ξ)​sin⁡(π​nl​(τ)​[ξ−y​(τ)])​𝑑ξ,superscriptsubscript𝑦0𝑧0𝑢0𝜉𝜋𝑛𝑙𝜏delimited-[]𝜉𝑦𝜏differential-d𝜉\int\_{y(0)}^{z(0)}u(0,\xi)\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi, |  | (A.4) |

which is also a part of the RHS in Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Recalling that by definition in Eq. ([8](#S1.E8 "Equation 8 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) u​(0,x)=U​(0,x)−A​(0)−B​(0)​x𝑢0𝑥𝑈0𝑥𝐴0𝐵0𝑥u(0,x)=U(0,x)-A(0)-B(0)x, and applying another identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫y​(0)z​(0)[A​(0)+B​(0)​ξ]superscriptsubscript𝑦0𝑧0delimited-[]𝐴0𝐵0𝜉\displaystyle\int\_{y(0)}^{z(0)}\left[A(0)+B(0)\xi\right] | sin(π​nl​(τ)[ξ−y(τ)])dξ=l​(τ)π2​n2{πn(A(0)+B(0)y(0))cos(πn(y(0)−y(τ)l​(τ))\displaystyle\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi=\frac{l(\tau)}{\pi^{2}n^{2}}\Bigg{\{}\pi n(A(0)+B(0)y(0))\cos\left(\frac{\pi n(y(0)-y(\tau)}{l(\tau)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −π​n​[A​(0)+B​(0)​z​(0)]​cos⁡(πn(z(0)−y(τ)l​(τ))\displaystyle-\pi n\left[A(0)+B(0)z(0)\right]\cos\left(\frac{\pi n(z(0)-y(\tau)}{l(\tau)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +B(0)l(τ)[sin(πn(z(0)−y(τ)l​(τ))−sin(πn(y(0)−y(τ)l​(τ)])},\displaystyle+B(0)l(\tau)\left[\sin\left(\frac{\pi n(z(0)-y(\tau)}{l(\tau)}\right)-\sin\left(\frac{\pi n(y(0)-y(\tau)}{l(\tau)}\right]\right)\Bigg{\}}, |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫y​(0)z​(0)u​(0,ξ)​sin⁡(π​nl​(τ)​[ξ−y​(τ)])​𝑑ξ=∫y​(0)z​(0)U​(0,ξ)​sin⁡(π​nl​(τ)​[ξ−y​(τ)])​𝑑ξ−α​(τ,n).superscriptsubscript𝑦0𝑧0𝑢0𝜉𝜋𝑛𝑙𝜏delimited-[]𝜉𝑦𝜏differential-d𝜉superscriptsubscript𝑦0𝑧0𝑈0𝜉𝜋𝑛𝑙𝜏delimited-[]𝜉𝑦𝜏differential-d𝜉𝛼𝜏𝑛\int\_{y(0)}^{z(0)}u(0,\xi)\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi=\int\_{y(0)}^{z(0)}U(0,\xi)\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi-\alpha(\tau,n). |  | (A.5) |

Therefore, the terms proportional to α​(τ,n)𝛼𝜏𝑛\alpha(\tau,n) in Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) are cancelling out. Also, substituting Eq. ([A](#A1.Ex19 "Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) into Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and moving the RHS of Eq. ([A](#A1.Ex19 "Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) into the LHS of Eq. ([29](#S2.E29 "Equation 29 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) results in the change of u​(τ,x)𝑢𝜏𝑥u(\tau,x) to U​(τ,x)𝑈𝜏𝑥U(\tau,x) in the LHS, and cancelling out the terms proportional to B​(s)𝐵𝑠B(s). Finally, introducing the new function F​(τ,x)𝐹𝜏𝑥F(\tau,x)

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(τ,x)=A​(τ)+B​(τ)​x−2π​∑n=1∞(−1)n−1​f+​(τ)+f−​(τ)n​sin⁡(π​nl​(τ)​[x−y​(τ)])𝐹𝜏𝑥𝐴𝜏𝐵𝜏𝑥2𝜋superscriptsubscript𝑛1superscript1𝑛1superscript𝑓𝜏superscript𝑓𝜏𝑛𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏F(\tau,x)=A(\tau)+B(\tau)x-\frac{2}{\pi}\sum\_{n=1}^{\infty}\frac{(-1)^{n-1}f^{+}(\tau)+f^{-}(\tau)}{n}\sin\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right) |  | (A.6) |

we obtain the representation of U​(τ,x)𝑈𝜏𝑥U(\tau,x)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U​(τ,x)𝑈𝜏𝑥\displaystyle U(\tau,x) | =2l​(τ)∑n=1∞sin(πnx−y​(τ)l​(τ)){e−π2​n2l2​(τ)​τ∫y​(0)z​(0)U(0,ξ)sin(π​nl​(τ)[ξ−y(τ)])dξ\displaystyle=\frac{2}{l(\tau)}\sum\_{n=1}^{\infty}\sin\left(\pi n\frac{x-y(\tau)}{l(\tau)}\right)\Bigg{\{}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\int\_{y(0)}^{z(0)}U(0,\xi)\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi |  | (A.7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)[Φ(s)sin(π​nl​(τ)[z(s)−y(τ)])+Ψ(s)sin(π​nl​(τ)[y(s)−y(τ)])\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\Big{[}\Phi(s)\sin\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)+\Psi(s)\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +β(τ,s,n)]ds}+F(τ,x).\displaystyle+\beta(\tau,s,n)\Big{]}ds\Bigg{\}}+F(\tau,x). |  |

Further, using the well-known identities, (Gradshtein and Ryzhik, [2007](#bib.bib12))

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1∞sin⁡k​xk=π−x2,0<x<π,∑k=1∞(−1)k−1​sin⁡k​xk=x2,0<x<π,formulae-sequenceformulae-sequencesuperscriptsubscript𝑘1𝑘𝑥𝑘𝜋𝑥20𝑥𝜋formulae-sequencesuperscriptsubscript𝑘1superscript1𝑘1𝑘𝑥𝑘𝑥20𝑥𝜋\sum\_{k=1}^{\infty}\frac{\sin kx}{k}=\frac{\pi-x}{2},\quad 0<x<\pi,\qquad\sum\_{k=1}^{\infty}(-1)^{k-1}\frac{\sin kx}{k}=\frac{x}{2},\quad 0<x<\pi, |  | (A.8) |

yields the following relationship

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=1∞superscriptsubscript𝑛1\displaystyle\sum\_{n=1}^{\infty} | 2π​n​[(−1)n−1​f+​(τ)+f−​(τ)]​sin⁡(π​n​x−y​(τ)l​(τ))=2π​{π​f+​(τ)2​x−y​(τ)l​(τ)+f−​(τ)2​[π−π​x−y​(τ)l​(τ)]}2𝜋𝑛delimited-[]superscript1𝑛1superscript𝑓𝜏superscript𝑓𝜏𝜋𝑛𝑥𝑦𝜏𝑙𝜏2𝜋𝜋superscript𝑓𝜏2𝑥𝑦𝜏𝑙𝜏superscript𝑓𝜏2delimited-[]𝜋𝜋𝑥𝑦𝜏𝑙𝜏\displaystyle\frac{2}{\pi n}\Bigg{[}(-1)^{n-1}f^{+}(\tau)+f^{-}(\tau)\Bigg{]}\sin\left(\pi n\frac{x-y(\tau)}{l(\tau)}\right)=\frac{2}{\pi}\Bigg{\{}\frac{\pi f^{+}(\tau)}{2}\frac{x-y(\tau)}{l(\tau)}+\frac{f^{-}(\tau)}{2}\left[\pi-\pi\frac{x-y(\tau)}{l(\tau)}\right]\Bigg{\}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =f+​(τ)−f−​(τ)l​(τ)​x+f+​(τ)​y​(τ)−f−​(τ)​z​(τ)l​(τ)=−[A​(τ)+B​(τ)​x],x∈(y​(τ),z​(τ)).formulae-sequenceabsentsuperscript𝑓𝜏superscript𝑓𝜏𝑙𝜏𝑥superscript𝑓𝜏𝑦𝜏superscript𝑓𝜏𝑧𝜏𝑙𝜏delimited-[]𝐴𝜏𝐵𝜏𝑥𝑥𝑦𝜏𝑧𝜏\displaystyle=\frac{f^{+}(\tau)-f^{-}(\tau)}{l(\tau)}x+\frac{f^{+}(\tau)y(\tau)-f^{-}(\tau)z(\tau)}{l(\tau)}=-\left[A(\tau)+B(\tau)x\right],\quad x\in(y(\tau),z(\tau)). |  | (A.9) |

With the help of Eq. ([A](#A1.Ex19 "Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) we arrive at another formula for F​(τ,x)𝐹𝜏𝑥F(\tau,x):

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(τ,x)={f−​(τ),x=y​(τ),0,x∈(y​(τ),z​(τ)),f+​(τ),x=z​(τ).𝐹𝜏𝑥casessuperscript𝑓𝜏𝑥𝑦𝜏0𝑥𝑦𝜏𝑧𝜏superscript𝑓𝜏𝑥𝑧𝜏\displaystyle F(\tau,x)=\begin{cases}f^{-}(\tau),&x=y(\tau),\\ 0,&x\in(y(\tau),z(\tau)),\\ f^{+}(\tau),&x=z(\tau).\end{cases} |  | (A.10) |

Combining Eq. ([A.7](#A1.E7 "Equation A.7 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and Eq. ([A.10](#A1.E10 "Equation A.10 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) together, and taking into account that the Fourier series in Eq. ([A.7](#A1.E7 "Equation A.7 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) is equal to zero if x=y​(τ)𝑥𝑦𝜏x=y(\tau) or x=z​(τ)𝑥𝑧𝜏x=z(\tau), yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(τ,x)={f−​(τ),x=y​(τ),U~​(τ,x),x∈(y​(τ),z​(τ)),f+​(τ),x=z​(τ).𝑈𝜏𝑥casessuperscript𝑓𝜏𝑥𝑦𝜏~𝑈𝜏𝑥𝑥𝑦𝜏𝑧𝜏superscript𝑓𝜏𝑥𝑧𝜏\displaystyle U(\tau,x)=\begin{cases}f^{-}(\tau),&x=y(\tau),\\ \tilde{U}(\tau,x),&x\in(y(\tau),z(\tau)),\\ f^{+}(\tau),&x=z(\tau).\end{cases} |  | (A.11) |

Here the function U~​(τ,x):(y​(τ),z​(τ))×ℝ+→ℝ:~𝑈𝜏𝑥→𝑦𝜏𝑧𝜏subscriptℝℝ\tilde{U}(\tau,x):(y(\tau),z(\tau))\times\mathbb{R}\_{+}\to\mathbb{R} is defined as follows

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U~~𝑈\displaystyle\tilde{U} | (τ,x)=2l​(τ)∑n=1∞sin(πnx−y​(τ)l​(τ)){e−π2​n2l2​(τ)​τ∫y​(0)z​(0)U(0,ξ)sin(π​nl​(τ)[ξ−y(τ)])dξ\displaystyle(\tau,x)=\frac{2}{l(\tau)}\sum\_{n=1}^{\infty}\sin\left(\pi n\frac{x-y(\tau)}{l(\tau)}\right)\Bigg{\{}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\int\_{y(0)}^{z(0)}U(0,\xi)\sin\left(\frac{\pi n}{l(\tau)}[\xi-y(\tau)]\right)d\xi |  | (A.12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)[Φ(s)sin(π​nl​(τ)[z(s)−y(τ)])+Ψ(s)sin(π​nl​(τ)[y(s)−y(τ)])+β(τ,s,n)]ds}.\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\Big{[}\Phi(s)\sin\left(\frac{\pi n}{l(\tau)}[z(s)-y(\tau)]\right)+\Psi(s)\sin\left(\frac{\pi n}{l(\tau)}[y(s)-y(\tau)]\right)+\beta(\tau,s,n)\Big{]}ds\Bigg{\}}. |  |

Note, that for the derivative ∂F​(τ,x)∂x𝐹𝜏𝑥𝑥\frac{\partial F(\tau,x)}{\partial x} we have

|  |  |  |
| --- | --- | --- |
|  | ∂F​(τ,x)∂x=B​(τ)−2l​(τ)​{f+​(τ)​∑n=1∞(−1)n−1​cos⁡(π​nl​(τ)​[x−y​(τ)])+f−​(τ)​∑n=1∞cos⁡(π​nl​(τ)​[x−y​(τ)])}𝐹𝜏𝑥𝑥𝐵𝜏2𝑙𝜏superscript𝑓𝜏superscriptsubscript𝑛1superscript1𝑛1𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏superscript𝑓𝜏superscriptsubscript𝑛1𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏\displaystyle\frac{\partial F(\tau,x)}{\partial x}=B(\tau)-\frac{2}{l(\tau)}\left\{f^{+}(\tau)\sum\_{n=1}^{\infty}(-1)^{n-1}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)+f^{-}(\tau)\sum\_{n=1}^{\infty}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | =f+​(τ)−f−​(τ)l​(τ)−2l​(τ)​{f+​(τ)​∑n=1∞(−1)n−1​cos⁡(π​nl​(τ)​[x−y​(τ)])+f−​(τ)​∑n=1∞cos⁡(π​nl​(τ)​[x−y​(τ)])}absentsuperscript𝑓𝜏superscript𝑓𝜏𝑙𝜏2𝑙𝜏superscript𝑓𝜏superscriptsubscript𝑛1superscript1𝑛1𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏superscript𝑓𝜏superscriptsubscript𝑛1𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏\displaystyle=\frac{f^{+}(\tau)-f^{-}(\tau)}{l(\tau)}-\frac{2}{l(\tau)}\left\{f^{+}(\tau)\sum\_{n=1}^{\infty}(-1)^{n-1}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)+f^{-}(\tau)\sum\_{n=1}^{\infty}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | =2l​(τ)​{f+​(τ)​[12+∑n=1∞(−1)n​cos⁡(π​nl​(τ)​[x−y​(τ)])]−f−​(τ)​[12+∑n=1∞cos⁡(π​nl​(τ)​[x−y​(τ)])]}.absent2𝑙𝜏superscript𝑓𝜏delimited-[]12superscriptsubscript𝑛1superscript1𝑛𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏superscript𝑓𝜏delimited-[]12superscriptsubscript𝑛1𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏\displaystyle=\frac{2}{l(\tau)}\left\{f^{+}(\tau)\left[\frac{1}{2}+\sum\_{n=1}^{\infty}(-1)^{n}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)\right]-f^{-}(\tau)\left[\frac{1}{2}+\sum\_{n=1}^{\infty}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)\right]\right\}. |  |

Applying well known representations for the Dirac delta function δ​(x)𝛿𝑥\delta(x)

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​(z​(τ)−x)𝛿𝑧𝜏𝑥\displaystyle\delta(z(\tau)-x) | =2l​(τ)​[12+∑n=1∞(−1)n​cos⁡(π​nl​(τ)​[x−y​(τ)])],absent2𝑙𝜏delimited-[]12superscriptsubscript𝑛1superscript1𝑛𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏\displaystyle=\frac{2}{l(\tau)}\left[\frac{1}{2}+\sum\_{n=1}^{\infty}(-1)^{n}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​(x−y​(τ))𝛿𝑥𝑦𝜏\displaystyle\delta(x-y(\tau)) | =2l​(τ)​[12+∑n=1∞cos⁡(π​nl​(τ)​[x−y​(τ)])]absent2𝑙𝜏delimited-[]12superscriptsubscript𝑛1𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝜏\displaystyle=\frac{2}{l(\tau)}\left[\frac{1}{2}+\sum\_{n=1}^{\infty}\cos\left(\frac{\pi n}{l(\tau)}[x-y(\tau)]\right)\right] |  |

yields the following formula for the derivative of F​(τ,x)𝐹𝜏𝑥F(\tau,x)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂F​(τ,x)∂x=f+​(τ)​δ​(x−z​(τ))−f−​(τ)​δ​(x−y​(τ)).𝐹𝜏𝑥𝑥superscript𝑓𝜏𝛿𝑥𝑧𝜏superscript𝑓𝜏𝛿𝑥𝑦𝜏\displaystyle\frac{\partial F(\tau,x)}{\partial x}=f^{+}(\tau)\delta(x-z(\tau))-f^{-}(\tau)\delta(x-y(\tau)). |  | (A.13) |

Thus, this derivative is defined only in the sense of distributions.

## Appendix B Transformation of Eq. ([30](#S2.E30 "Equation 30 ‣ 2.1 The inverse transform ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) to Eq. ([2.4](#S2.Ex55 "2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

.

Applying a product-to-sum trigonometric identities to Eq. ([A.12](#A1.E12 "Equation A.12 ‣ Appendix A Simplification of Eq. (29) ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U~(\displaystyle\tilde{U}( | τ,x)=1l​(τ)∑n=1∞{e−π2​n2l2​(τ)​τ∫y​(0)z​(0)U(0,ξ)[cos(π​nl​(τ)[x−ξ])−cos(π​nl​(τ)[x+ξ−2y(τ)])]dξ\displaystyle\tau,x)=\frac{1}{l(\tau)}\sum\_{n=1}^{\infty}\Bigg{\{}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}\tau}\int\_{y(0)}^{z(0)}U(0,\xi)\left[\cos\left(\frac{\pi n}{l(\tau)}[x-\xi]\right)-\cos\left(\frac{\pi n}{l(\tau)}[x+\xi-2y(\tau)]\right)\right]d\xi |  | (B.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)​[Φ​(s)+f+​(s)​z′​(s)]​[cos⁡(π​nl​(τ)​[x−z​(s)])−cos⁡(π​nl​(τ)​[x+z​(s)−2​y​(τ)])]​𝑑ssuperscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠delimited-[]Φ𝑠superscript𝑓𝑠superscript𝑧′𝑠delimited-[]𝜋𝑛𝑙𝜏delimited-[]𝑥𝑧𝑠𝜋𝑛𝑙𝜏delimited-[]𝑥𝑧𝑠2𝑦𝜏differential-d𝑠\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\left[\cos\left(\frac{\pi n}{l(\tau)}[x-z(s)]\right)-\cos\left(\frac{\pi n}{l(\tau)}[x+z(s)-2y(\tau)]\right)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τe−π2​n2l2​(τ)​(τ−s)​[Ψ​(s)−f−​(s)​y′​(s)]​[cos⁡(π​nl​(τ)​[x−y​(s)])−cos⁡(π​nl​(τ)​[x+y​(s)−2​y​(τ)])]​𝑑ssuperscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠delimited-[]Ψ𝑠superscript𝑓𝑠superscript𝑦′𝑠delimited-[]𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝑠𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝑠2𝑦𝜏differential-d𝑠\displaystyle+\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\left[\cos\left(\frac{\pi n}{l(\tau)}[x-y(s)]\right)-\cos\left(\frac{\pi n}{l(\tau)}[x+y(s)-2y(\tau)]\right)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +π​nl​(τ)​∫0τe−π2​n2l2​(τ)​(τ−s)​f−​(s)​[sin⁡(π​nl​(τ)​[x−y​(s)])+sin⁡(π​nl​(τ)​[x+y​(s)−2​y​(τ)])]​𝑑s𝜋𝑛𝑙𝜏superscriptsubscript0𝜏superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠superscript𝑓𝑠delimited-[]𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝑠𝜋𝑛𝑙𝜏delimited-[]𝑥𝑦𝑠2𝑦𝜏differential-d𝑠\displaystyle+\frac{\pi n}{l(\tau)}\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}f^{-}(s)\left[\sin\left(\frac{\pi n}{l(\tau)}[x-y(s)]\right)+\sin\left(\frac{\pi n}{l(\tau)}[x+y(s)-2y(\tau)]\right)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −π​nl​(τ)∫0τe−π2​n2l2​(τ)​(τ−s)f+(s)[sin(π​nl​(τ)[x−z(s)])+sin(π​nl​(τ)[x+z(s)−2y(τ)])]ds},\displaystyle-\frac{\pi n}{l(\tau)}\int\_{0}^{\tau}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}f^{+}(s)\left[\sin\left(\frac{\pi n}{l(\tau)}[x-z(s)]\right)+\sin\left(\frac{\pi n}{l(\tau)}[x+z(s)-2y(\tau)]\right)\right]ds\Bigg{\}}, |  |

Since the functions

|  |  |  |
| --- | --- | --- |
|  | h1​(n)=e−β​n2​cos⁡(α​n),h2​(n)=n​e−β​n2​sin⁡(α​n)formulae-sequencesubscriptℎ1𝑛superscript𝑒𝛽superscript𝑛2𝛼𝑛subscriptℎ2𝑛𝑛superscript𝑒𝛽superscript𝑛2𝛼𝑛h\_{1}(n)=e^{-\beta n^{2}}\cos\left(\alpha n\right),\qquad h\_{2}(n)=ne^{-\beta n^{2}}\sin\left(\alpha n\right) |  |

are even, h2​(0)=0subscriptℎ200h\_{2}(0)=0, and in the first three lines of Eq. ([B.1](#A2.E1 "Equation B.1 ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) we have a difference of cosines, so at n=0𝑛0n=0 the difference vanishes, the series in Eq. ([B.1](#A2.E1 "Equation B.1 ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) can be slightly modified by replacing

|  |  |  |
| --- | --- | --- |
|  | ∑n=1∞hi​(n)=12​∑n=−∞∞hi​(n),i=1,2.formulae-sequencesuperscriptsubscript𝑛1subscriptℎ𝑖𝑛12superscriptsubscript𝑛subscriptℎ𝑖𝑛𝑖  12\sum\_{n=1}^{\infty}h\_{i}(n)=\frac{1}{2}\sum\_{n=-\infty}^{\infty}h\_{i}(n),\quad i=1,2. |  |

Now applying formulas Eq. ([38](#S2.E38 "Equation 38 ‣ 2.4 The Poisson summation formula and alternative representations ‣ 2 Solution by the GIT method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) to Eq. ([B.1](#A2.E1 "Equation B.1 ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and using

|  |  |  |
| --- | --- | --- |
|  | α=x−ξl​(τ),12​β=τl2​(τ),2​β2​π=l​(τ)π​τ,β2​(2​n+α)2=l2​(τ)4​τ​(2​n+x−ξl​(τ))2=(x−ξ+2​n​l​(τ))24​τ,formulae-sequence𝛼𝑥𝜉𝑙𝜏formulae-sequence12𝛽𝜏superscript𝑙2𝜏formulae-sequence2𝛽2𝜋𝑙𝜏𝜋𝜏𝛽2superscript2𝑛𝛼2superscript𝑙2𝜏4𝜏superscript2𝑛𝑥𝜉𝑙𝜏2superscript𝑥𝜉2𝑛𝑙𝜏24𝜏\alpha=\frac{x-\xi}{l(\tau)},\quad\frac{1}{2\beta}=\frac{\tau}{l^{2}(\tau)},\quad 2\sqrt{\frac{\beta}{2\pi}}=\frac{l(\tau)}{\sqrt{\pi\tau}},\quad\frac{\beta}{2}(2n+\alpha)^{2}=\frac{l^{2}(\tau)}{4\tau}\left(2n+\frac{x-\xi}{l(\tau)}\right)^{2}=\frac{(x-\xi+2nl(\tau))^{2}}{4\tau}, |  |

we obtain the following identities

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 12​l​(τ)​∑n=−∞∞e−π2​n2l2​(τ)​(τ−s)​cos⁡(π​nl​(τ)​[x−ξ])12𝑙𝜏superscriptsubscript𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝜋𝑛𝑙𝜏delimited-[]𝑥𝜉\displaystyle\frac{1}{2l(\tau)}\sum\_{n=-\infty}^{\infty}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\cos\left(\frac{\pi n}{l(\tau)}[x-\xi]\right) | =12​π​(τ−s)​∑n=−∞∞e−(x−ξ+2​n​l​(τ))24​(τ−s)absent12𝜋𝜏𝑠superscriptsubscript𝑛superscript𝑒superscript𝑥𝜉2𝑛𝑙𝜏24𝜏𝑠\displaystyle=\frac{1}{2\sqrt{\pi(\tau-s)}}\sum\_{n=-\infty}^{\infty}e^{-\frac{(x-\xi+2nl(\tau))^{2}}{4(\tau-s)}} |  | (B.2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​l​(τ)​∑n=−∞∞e−π2​n2l2​(τ)​(τ−s)​π​nl​(τ)​sin⁡(π​nl​(τ)​[x−ξ])12𝑙𝜏superscriptsubscript𝑛superscript𝑒superscript𝜋2superscript𝑛2superscript𝑙2𝜏𝜏𝑠𝜋𝑛𝑙𝜏𝜋𝑛𝑙𝜏delimited-[]𝑥𝜉\displaystyle\frac{1}{2l(\tau)}\sum\_{n=-\infty}^{\infty}e^{-\frac{\pi^{2}n^{2}}{l^{2}(\tau)}(\tau-s)}\frac{\pi n}{l(\tau)}\sin\left(\frac{\pi n}{l(\tau)}[x-\xi]\right) | =14​π​(τ−s)3​∑n=−∞∞(x−ξ+2​n​l​(τ))​e−(x−ξ+2​n​l​(τ))24​(τ−s).absent14𝜋superscript𝜏𝑠3superscriptsubscript𝑛𝑥𝜉2𝑛𝑙𝜏superscript𝑒superscript𝑥𝜉2𝑛𝑙𝜏24𝜏𝑠\displaystyle=\frac{1}{4\sqrt{\pi(\tau-s)^{3}}}\sum\_{n=-\infty}^{\infty}(x-\xi+2nl(\tau))e^{-\frac{(x-\xi+2nl(\tau))^{2}}{4(\tau-s)}}. |  |

Observe that each term in Eq. ([B.1](#A2.E1 "Equation B.1 ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) can be represented as one of the series in Eq. ([B.2](#A2.E2 "Equation B.2 ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")). Therefore, assuming x∈(y​(τ),z​(τ))𝑥𝑦𝜏𝑧𝜏x\in(y(\tau),z(\tau)), we immediately arrive at the alternative representation for U~​(τ,x)~𝑈𝜏𝑥\tilde{U}(\tau,x)

|  |  |  |  |
| --- | --- | --- | --- |
|  | U~​(τ,x)~𝑈𝜏𝑥\displaystyle\tilde{U}(\tau,x) | =∑n=−∞∞{∫y​(0)z​(0)U(0,ξ)Υn(x,τ|ξ,0)dξ+∫0τ[Φ(s)+f+(s)z′(s)]Υn(x,τ|z(s),s)ds,\displaystyle=\sum\_{n=-\infty}^{\infty}\Bigg{\{}\int\_{y(0)}^{z(0)}U(0,\xi)\Upsilon\_{n}(x,\tau\,|\,\xi,0)d\xi+\int\_{0}^{\tau}\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\Upsilon\_{n}(x,\tau|z(s),s)ds, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0τ[Ψ​(s)−f−​(s)​y′​(s)]​Υn​(x,τ|y​(s),s)​𝑑ssuperscriptsubscript0𝜏delimited-[]Ψ𝑠superscript𝑓𝑠superscript𝑦′𝑠subscriptΥ𝑛𝑥conditional𝜏  𝑦𝑠𝑠differential-d𝑠\displaystyle+\int\_{0}^{\tau}\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\Upsilon\_{n}(x,\tau\,|\,y(s),s)ds |  | (B.3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τf−(s)Λn(x,τ|y(s),s)−f+(s)Λn(x,τ|z(s),s)ds}+F1(τ,x),\displaystyle+\int\_{0}^{\tau}f^{-}(s)\Lambda\_{n}(x,\tau\,|\,y(s),s)-f^{+}(s)\Lambda\_{n}(x,\tau\,|\,z(s),s)ds\Bigg{\}}+F\_{1}(\tau,x), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ΥnsubscriptΥ𝑛\displaystyle\Upsilon\_{n} | (x,τ|ξ,s)=12​π​(τ−s)​[e−(2​n​l​(τ)+x−ξ)24​(τ−s)−e−(2​n​l​(τ)+x+ξ−2​y​(τ))24​(τ−s)],𝑥conditional𝜏  𝜉𝑠12𝜋𝜏𝑠delimited-[]superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉24𝜏𝑠superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉2𝑦𝜏24𝜏𝑠\displaystyle(x,\tau\,|\,\xi,s)=\frac{1}{2\sqrt{\pi(\tau-s)}}\left[e^{-\frac{(2nl(\tau)+x-\xi)^{2}}{4(\tau-s)}}-e^{-\frac{(2nl(\tau)+x+\xi-2y(\tau))^{2}}{4(\tau-s)}}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ΛnsubscriptΛ𝑛\displaystyle\Lambda\_{n} | (x,τ|ξ,s)=x−ξ+2​n​l​(τ)4​π​(τ−s)3​e−(2​n​l​(τ)+x−ξ)24​(τ−s)+x+ξ−2​y​(τ)+2​n​l​(τ)4​π​(τ−s)3​e−(2​n​l​(τ)+x+ξ−2​y​(τ))24​(τ−s).𝑥conditional𝜏  𝜉𝑠𝑥𝜉2𝑛𝑙𝜏4𝜋superscript𝜏𝑠3superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉24𝜏𝑠𝑥𝜉2𝑦𝜏2𝑛𝑙𝜏4𝜋superscript𝜏𝑠3superscript𝑒superscript2𝑛𝑙𝜏𝑥𝜉2𝑦𝜏24𝜏𝑠\displaystyle(x,\tau\,|\,\xi,s)=\frac{x-\xi+2nl(\tau)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(2nl(\tau)+x-\xi)^{2}}{4(\tau-s)}}+\frac{x+\xi-2y(\tau)+2nl(\tau)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(2nl(\tau)+x+\xi-2y(\tau))^{2}}{4(\tau-s)}}. |  |

### B.1 The limiting values x→y​(τ)→𝑥𝑦𝜏x\to y(\tau) and x→z​(τ)→𝑥𝑧𝜏x\to z(\tau) in Eq. ([B](#A2.Ex9 "Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit"))

The Eq. ([B](#A2.Ex9 "Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) provides an alternative representation of the solution U~​(τ,x)~𝑈𝜏𝑥\tilde{U}(\tau,x) of the heat equation in Eq. ([4](#S1.E4 "Equation 4 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) with the initial condition in Eq. ([5](#S1.E5 "Equation 5 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) and the boundary conditions in Eq. ([6](#S1.E6 "Equation 6 ‣ 1 Statement of the problem ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) at the time-dependent domain x∈(y​(τ),z​(τ))𝑥𝑦𝜏𝑧𝜏x\in(y(\tau),z(\tau)) in terms of the Fourier series. In this section we show that the function U~~𝑈\tilde{U} can be analytically continued to the boundary points y​(τ)𝑦𝜏y(\tau) and z​(τ)𝑧𝜏z(\tau), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→y​(τ)+0U~​(τ,x)=f−​(τ),limx→z​(τ)−0U~​(τ,x)=f+​(τ).formulae-sequencesubscript→𝑥𝑦𝜏0~𝑈𝜏𝑥superscript𝑓𝜏subscript→𝑥𝑧𝜏0~𝑈𝜏𝑥superscript𝑓𝜏\lim\_{x\to y(\tau)+0}\tilde{U}(\tau,x)=f^{-}(\tau),\qquad\lim\_{x\to z(\tau)-0}\tilde{U}(\tau,x)=f^{+}(\tau). |  | (B.4) |

It is easy to check that the functions Υn​(x,τ|ξ,s)subscriptΥ𝑛𝑥conditional𝜏

𝜉𝑠\Upsilon\_{n}(x,\tau|\xi,s) and Λn​(x,τ|ξ,s)subscriptΛ𝑛𝑥conditional𝜏

𝜉𝑠\Lambda\_{n}(x,\tau|\xi,s) are regular only if n≠0,x∈[y​(τ),z​(τ)],ξ∈[y​(s),z​(s)],s→τformulae-sequence𝑛0formulae-sequence𝑥𝑦𝜏𝑧𝜏formulae-sequence𝜉𝑦𝑠𝑧𝑠→𝑠𝜏n\neq 0,\ x\in[y(\tau),z(\tau)],\ \xi\in[y(s),z(s)],\ s\to\tau. In this case the following identities hold

|  |  |  |  |
| --- | --- | --- | --- |
|  | lims→τΥn​(x,τ|ξ,s)=0,lims→τΛn​(x,τ|ξ,s)=0,n≠0.formulae-sequencesubscript→𝑠𝜏subscriptΥ𝑛𝑥conditional𝜏  𝜉𝑠0formulae-sequencesubscript→𝑠𝜏subscriptΛ𝑛𝑥conditional𝜏  𝜉𝑠0𝑛0\displaystyle\lim\_{s\to\tau}\Upsilon\_{n}(x,\tau|\xi,s)=0,\qquad\lim\_{s\to\tau}\Lambda\_{n}(x,\tau|\xi,s)=0,\qquad n\neq 0. |  | (B.5) |

At n=0𝑛0n=0 functions Υ0​(x,τ|y​(s),s)subscriptΥ0𝑥conditional𝜏

𝑦𝑠𝑠\Upsilon\_{0}(x,\tau|y(s),s) and Λ0​(x,τ|y​(s),s)subscriptΛ0𝑥conditional𝜏

𝑦𝑠𝑠\Lambda\_{0}(x,\tau|y(s),s) have a singularity when s→τ,x→y​(τ)formulae-sequence→𝑠𝜏→𝑥𝑦𝜏s\to\tau,\ x\to y(\tau), and functions Υ0​(x,τ|z​(s),s)subscriptΥ0𝑥conditional𝜏

𝑧𝑠𝑠\Upsilon\_{0}(x,\tau|z(s),s) and Λ0​(x,τ|z​(s),s)subscriptΛ0𝑥conditional𝜏

𝑧𝑠𝑠\Lambda\_{0}(x,\tau|z(s),s) - when s→τ,x→z​(τ)formulae-sequence→𝑠𝜏→𝑥𝑧𝜏s\to\tau,\ x\to z(\tau). Note, that the singularity of Υ0subscriptΥ0\Upsilon\_{0} is integrable and so weak. Therefore, when calculating a corresponding limit of both parts in Eq. ([B](#A2.Ex9 "Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), for the regular terms we can switch the order of the integration and limit operators, and then use the following properties

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | limx→y​(τ)+0∑n=−∞∞Υn​(x,τ|ξ,s)subscript→𝑥𝑦𝜏0superscriptsubscript𝑛subscriptΥ𝑛𝑥conditional𝜏  𝜉𝑠\displaystyle\lim\_{x\to y(\tau)+0}\sum\_{n=-\infty}^{\infty}\Upsilon\_{n}(x,\tau\,|\,\xi,s) | =0,limx→z​(τ)−0∑n=−∞∞Υn​(x,τ|ξ,s)absent  0subscript→𝑥𝑧𝜏0superscriptsubscript𝑛subscriptΥ𝑛𝑥conditional𝜏  𝜉𝑠\displaystyle=0,\qquad\lim\_{x\to z(\tau)-0}\sum\_{n=-\infty}^{\infty}\Upsilon\_{n}(x,\tau\,|\,\xi,s) | =0,absent0\displaystyle=0, |  | (B.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limx→y​(τ)+0∑n=−∞n≠0Λn​(x,τ|ξ,s)subscript→𝑥𝑦𝜏0subscript  𝑛𝑛0subscriptΛ𝑛𝑥conditional𝜏  𝜉𝑠\displaystyle\lim\_{x\to y(\tau)+0}\sum\_{\begin{subarray}{c}n=-\infty\\ n\neq 0\end{subarray}}\Lambda\_{n}(x,\tau\,|\,\xi,s) | =0,limx→z​(τ)−0∑n=−∞n≠0Λn​(x,τ|ξ,s)absent  0subscript→𝑥𝑧𝜏0subscript  𝑛𝑛0subscriptΛ𝑛𝑥conditional𝜏  𝜉𝑠\displaystyle=0,\qquad\lim\_{x\to z(\tau)-0}\sum\_{\begin{subarray}{c}n=-\infty\\ n\neq 0\end{subarray}}\Lambda\_{n}(x,\tau\,|\,\xi,s) | =0,absent0\displaystyle=0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limx→y​(τ)+0Λ0​(x,τ|z​(s),s)subscript→𝑥𝑦𝜏0subscriptΛ0𝑥conditional𝜏  𝑧𝑠𝑠\displaystyle\lim\_{x\to y(\tau)+0}\Lambda\_{0}(x,\tau\,|\,z(s),s) | =0,limx→z​(τ)−0Λ0​(x,τ|y​(s),s)absent  0subscript→𝑥𝑧𝜏0subscriptΛ0𝑥conditional𝜏  𝑦𝑠𝑠\displaystyle=0,\qquad\lim\_{x\to z(\tau)-0}\Lambda\_{0}(x,\tau\,|\,y(s),s) | =0,absent0\displaystyle=0, |  |

to obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limx→y​(τ)+0U~​(τ,x)subscript→𝑥𝑦𝜏0~𝑈𝜏𝑥\displaystyle\lim\_{x\to y(\tau)+0}\tilde{U}(\tau,x) | =limx→y​(τ)+0∫0τf−​(s)​Λ0​(x,τ|y​(s),s)absentsubscript→𝑥𝑦𝜏0superscriptsubscript0𝜏superscript𝑓𝑠subscriptΛ0𝑥conditional𝜏  𝑦𝑠𝑠\displaystyle=\lim\_{x\to y(\tau)+0}\int\_{0}^{\tau}f^{-}(s)\Lambda\_{0}(x,\tau\,|\,y(s),s) |  | (B.7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→z​(τ)−0U~​(τ,x)subscript→𝑥𝑧𝜏0~𝑈𝜏𝑥\displaystyle\lim\_{x\to z(\tau)-0}\tilde{U}(\tau,x) | =−limx→z​(τ)−0∫0τf+​(s)​Λ0​(x,τ|z​(s),s).absentsubscript→𝑥𝑧𝜏0superscriptsubscript0𝜏superscript𝑓𝑠subscriptΛ0𝑥conditional𝜏  𝑧𝑠𝑠\displaystyle=-\lim\_{x\to z(\tau)-0}\int\_{0}^{\tau}f^{+}(s)\Lambda\_{0}(x,\tau\,|\,z(s),s). |  |

To proceed we need the notion of heat potentials and the results obtained in Section [3](#S3 "3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit") (see also (Tikhonov and Samarskii, [1963](#bib.bib32))). It can be shown that the functions Λ0​(x,τ|y​(s),s)subscriptΛ0𝑥conditional𝜏

𝑦𝑠𝑠\Lambda\_{0}(x,\tau|y(s),s) and Λ0​(x,τ|z​(s),s)subscriptΛ0𝑥conditional𝜏

𝑧𝑠𝑠\Lambda\_{0}(x,\tau|z(s),s) can be represented as a sum of double layer heat potentials. Therefore, we can evaluate the limits Eq. ([B.7](#A2.E7 "Equation B.7 ‣ B.1 The limiting values 𝑥→𝑦⁢(𝜏) and 𝑥→𝑧⁢(𝜏) in Eq. () ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) with the help of Eq. ([53](#S3.E53 "Equation 53 ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), Eq. ([62](#S3.E62 "Equation 62 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")).

In more detail, according to Eq. ([B.7](#A2.E7 "Equation B.7 ‣ B.1 The limiting values 𝑥→𝑦⁢(𝜏) and 𝑥→𝑧⁢(𝜏) in Eq. () ‣ Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) in the explicit form the limits of U~​(τ,x)~𝑈𝜏𝑥\tilde{U}(\tau,x) read

|  |  |  |
| --- | --- | --- |
|  | U~​(τ,y​(τ))=limx→y​(τ)+0∫0τf−​(s)​[x−y​(s)4​π​(τ−s)3​e−(x−y​(s))24​(τ−s)+x−2​y​(τ)+y​(s)4​π​(τ−s)3​e−(x−2​y​(τ)+y​(s))24​(τ−s)]​𝑑s,~𝑈𝜏𝑦𝜏subscript→𝑥𝑦𝜏0superscriptsubscript0𝜏superscript𝑓𝑠delimited-[]𝑥𝑦𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥𝑦𝑠24𝜏𝑠𝑥2𝑦𝜏𝑦𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥2𝑦𝜏𝑦𝑠24𝜏𝑠differential-d𝑠\displaystyle\tilde{U}(\tau,y(\tau))=\lim\_{x\to y(\tau)+0}\int\_{0}^{\tau}f^{-}(s)\left[\frac{x-y(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-y(s))^{2}}{4(\tau-s)}}+\frac{x-2y(\tau)+y(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-2y(\tau)+y(s))^{2}}{4(\tau-s)}}\right]ds, |  |
|  |  |  |
| --- | --- | --- |
|  | U~​(τ,z​(τ))=−limx→z​(τ)−0∫0τf+​(s)​[x−z​(s)4​π​(τ−s)3​e−(x−z​(s))24​(τ−s)+x−2​z​(τ)+z​(s)4​π​(τ−s)3​e−(x−2​z​(τ)+z​(s))24​(τ−s)]​𝑑s.~𝑈𝜏𝑧𝜏subscript→𝑥𝑧𝜏0superscriptsubscript0𝜏superscript𝑓𝑠delimited-[]𝑥𝑧𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥𝑧𝑠24𝜏𝑠𝑥2𝑧𝜏𝑧𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥2𝑧𝜏𝑧𝑠24𝜏𝑠differential-d𝑠\displaystyle\tilde{U}(\tau,z(\tau))=-\lim\_{x\to z(\tau)-0}\int\_{0}^{\tau}f^{+}(s)\left[\frac{x-z(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-z(s))^{2}}{4(\tau-s)}}+\frac{x-2z(\tau)+z(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-2z(\tau)+z(s))^{2}}{4(\tau-s)}}\right]ds. |  |

This can also be re-written in the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U~​(τ,y​(τ))~𝑈𝜏𝑦𝜏\displaystyle\tilde{U}(\tau,y(\tau)) | =limx→y​(τ)+0∫0τf−​(s)​x−y​(s)4​π​(τ−s)3​e−(x−y​(s))24​(τ−s)​𝑑sabsentsubscript→𝑥𝑦𝜏0superscriptsubscript0𝜏superscript𝑓𝑠𝑥𝑦𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥𝑦𝑠24𝜏𝑠differential-d𝑠\displaystyle=\lim\_{x\to y(\tau)+0}\int\_{0}^{\tau}f^{-}(s)\frac{x-y(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-y(s))^{2}}{4(\tau-s)}}ds |  | (B.8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −\displaystyle- | lim2​y​(τ)−x→y​(τ)−0∫0τf−​(s)​2​y​(τ)−x−y​(s)4​π​(τ−s)3​e−(x−2​y​(τ)+y​(s))24​(τ−s)​𝑑s,subscript→2𝑦𝜏𝑥𝑦𝜏0superscriptsubscript0𝜏superscript𝑓𝑠2𝑦𝜏𝑥𝑦𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥2𝑦𝜏𝑦𝑠24𝜏𝑠differential-d𝑠\displaystyle\lim\_{2y(\tau)-x\to y(\tau)-0}\int\_{0}^{\tau}f^{-}(s)\frac{2y(\tau)-x-y(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-2y(\tau)+y(s))^{2}}{4(\tau-s)}}ds, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | U~​(τ,z​(τ))~𝑈𝜏𝑧𝜏\displaystyle\tilde{U}(\tau,z(\tau)) | =−limx→z​(τ)−0∫0τf+​(s)​x−z​(s)4​π​(τ−s)3​e−(x−z​(s))24​(τ−s)​𝑑sabsentsubscript→𝑥𝑧𝜏0superscriptsubscript0𝜏superscript𝑓𝑠𝑥𝑧𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥𝑧𝑠24𝜏𝑠differential-d𝑠\displaystyle=-\lim\_{x\to z(\tau)-0}\int\_{0}^{\tau}f^{+}(s)\frac{x-z(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-z(s))^{2}}{4(\tau-s)}}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | lim2​z​(τ)−x→z​(τ)+0∫0τf+​(s)​2​z​(τ)−x−z​(s)4​π​(τ−s)3​e−(x−2​z​(τ)+z​(s))24​(τ−s)​𝑑s.subscript→2𝑧𝜏𝑥𝑧𝜏0superscriptsubscript0𝜏superscript𝑓𝑠2𝑧𝜏𝑥𝑧𝑠4𝜋superscript𝜏𝑠3superscript𝑒superscript𝑥2𝑧𝜏𝑧𝑠24𝜏𝑠differential-d𝑠\displaystyle\lim\_{2z(\tau)-x\to z(\tau)+0}\int\_{0}^{\tau}f^{+}(s)\frac{2z(\tau)-x-z(s)}{4\sqrt{\pi(\tau-s)^{3}}}e^{-\frac{(x-2z(\tau)+z(s))^{2}}{4(\tau-s)}}ds. |  |

Using Eq. ([62](#S3.E62 "Equation 62 ‣ 3.1 The limiting value of 𝜑⁢(𝑡) ‣ 3 Solution by the HP method ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")), these expressions can be transformed to

|  |  |  |
| --- | --- | --- |
|  | U~​(τ,y​(τ))=f−​(τ)2+f−​(τ)2=f−​(τ),U~​(τ,z​(τ))=f+​(τ)2+f+​(τ)2=f+​(τ).formulae-sequence~𝑈𝜏𝑦𝜏superscript𝑓𝜏2superscript𝑓𝜏2superscript𝑓𝜏~𝑈𝜏𝑧𝜏superscript𝑓𝜏2superscript𝑓𝜏2superscript𝑓𝜏\tilde{U}(\tau,y(\tau))=\frac{f^{-}(\tau)}{2}+\frac{f^{-}(\tau)}{2}=f^{-}(\tau),\qquad\tilde{U}(\tau,z(\tau))=\frac{f^{+}(\tau)}{2}+\frac{f^{+}(\tau)}{2}=f^{+}(\tau). |  |

Since U~​(τ,x)~𝑈𝜏𝑥\tilde{U}(\tau,x) has the same limits as the boundary values of U​(τ,x)𝑈𝜏𝑥U(\tau,x), and at x∈(y​(τ),z​(τ))𝑥𝑦𝜏𝑧𝜏x\in(y(\tau),z(\tau)) we have U~​(τ,x)=U​(τ,x)~𝑈𝜏𝑥𝑈𝜏𝑥\tilde{U}(\tau,x)=U(\tau,x), Eq. ([B](#A2.Ex9 "Appendix B Transformation of Eq. (30) to Eq. () ‣ Semi-analytic pricing of double barrier options with time-dependent barriers and rebates at hit")) allows an alternative form

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(τ,x)𝑈𝜏𝑥\displaystyle U(\tau,x) | =∑n=−∞∞{∫y​(0)z​(0)U(0,ξ)Υn(x,τ|ξ,0)dξ+∫0τ[Φ(s)+f+(s)z′(s)]Υn(x,τ|z(s),s)ds,\displaystyle=\sum\_{n=-\infty}^{\infty}\Bigg{\{}\int\_{y(0)}^{z(0)}U(0,\xi)\Upsilon\_{n}(x,\tau\,|\,\xi,0)d\xi+\int\_{0}^{\tau}\left[\Phi(s)+f^{+}(s)z^{\prime}(s)\right]\Upsilon\_{n}(x,\tau|z(s),s)ds, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τ[Ψ​(s)−f−​(s)​y′​(s)]​Υn​(x,τ|y​(s),s)​𝑑ssuperscriptsubscript0𝜏delimited-[]Ψ𝑠superscript𝑓𝑠superscript𝑦′𝑠subscriptΥ𝑛𝑥conditional𝜏  𝑦𝑠𝑠differential-d𝑠\displaystyle\qquad+\int\_{0}^{\tau}\left[\Psi(s)-f^{-}(s)y^{\prime}(s)\right]\Upsilon\_{n}(x,\tau\,|\,y(s),s)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τf−(s)Λn(x,τ|y(s),s)−f+(s)Λn(x,τ|z(s),s)ds}.\displaystyle\qquad+\int\_{0}^{\tau}f^{-}(s)\Lambda\_{n}(x,\tau\,|\,y(s),s)-f^{+}(s)\Lambda\_{n}(x,\tau\,|\,z(s),s)ds\Bigg{\}}. |  |

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2009.09342)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2009.09342)
[View original  
on arXiv](https://arxiv.org/abs/2009.09342)[►](javascript: void(0))