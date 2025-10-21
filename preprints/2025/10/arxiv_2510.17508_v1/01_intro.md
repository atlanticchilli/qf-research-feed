---
authors:
- Li Shan
- Xi Shen
doc_id: arxiv:2510.17508v1
family_id: arxiv:2510.17508
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations
  L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294)
  and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)
url_abs: http://arxiv.org/abs/2510.17508v1
url_html: https://arxiv.org/html/2510.17508v1
venue: arXiv q-fin
version: 1
year: 2025
---


Li Shan
Corresponding author. Department of Mathematics, Shantou University, Shantou, China. (lishan@stu.edu.cn)
  
Xi Shen
Department of Mathematics, Shantou University, Shantou, China. (24xshen@stu.edu.cn)

###### Abstract

Parallel physical information neural networks (P-PINNs) have been widely used to solve systems with multiple coupled physical fields, such as the coupled Stokes-Darcy equations with Beavers-Joseph-Saffman (BJS) interface conditions. However, excessively high or low physical constants in partial differential equations (PDE) often lead to ill-conditioned loss functions and can even cause the failure of training numerical solutions for PINNs. To solve this problem, we develop a new kind of enhanced parallel PINNs, MF-PINNs, in this article. Our MF-PINNs combines the velocity-pressure form (VP) with the stream-vorticity form (SV) and add them with adjusted weights to the total loss functions. The results of numerical experiments show our MF-PINNs have successfully improved the accuracy of the streamline fields and the pressure fields when kinematic viscosity and permeability tensor range from 10−410^{-4} to 10410^{4}. Thus, our MF-PINNs hold promise for more chaotic PDE systems involving turbulent flows. Additionally, we also explore the best combination of the activation functions and their periodicity. And we also try to set the initial learning rate and design its decay strategies. The code and data associated with this paper are available at <https://github.com/shxshx48716/MF-PINNs.git>.

###### keywords:

Coupled Stokes–Darcy equations, Parallel physical information neural networks, Mixed-Form loss, Periodic activation functions.

## 1 Introduction

Stokes-Darcy coupling models arise in several applications, such as interaction between surface and groundwater flows, oil reservoirs in vuggy porous media, and industrial filtrations. In mathematical modeling, the Stokes and Darcy equations are employed to describe free fluid flows and porous media seepage, respectively. Additional equations are introduced to comply with physical laws, such as mass conservation, normal stress balance, and the BJS conditions [[1](https://arxiv.org/html/2510.17508v1#bib.bibx1)].

The rapid advancement of artificial intelligence has increased the applications for deep neural networks, such as PINNs [[2](https://arxiv.org/html/2510.17508v1#bib.bibx2)], as a new approach for solving PDE. Moreover, parallel PINNs and region decomposition strategies [[3](https://arxiv.org/html/2510.17508v1#bib.bibx3), [4](https://arxiv.org/html/2510.17508v1#bib.bibx4), [5](https://arxiv.org/html/2510.17508v1#bib.bibx5), [6](https://arxiv.org/html/2510.17508v1#bib.bibx6), [7](https://arxiv.org/html/2510.17508v1#bib.bibx7), [8](https://arxiv.org/html/2510.17508v1#bib.bibx8), [9](https://arxiv.org/html/2510.17508v1#bib.bibx9)] use multiple GPUs to train multiple neural networks in parallel. Above, all of these methods are designed to handle coupled models with multiple physical fields and media, including the coupled Stokes-Darcy system. Compared with traditional numerical methods, finite difference method, finite element method, finite volume method, spectral method, etc., PINNs offer several advantages for coupled systems: (i)\mathit{(i)} no need for mesh generation; (𝑖𝑖)\mathit{(ii)} handling boundary conditions more flexibly; (𝑖𝑖𝑖)\mathit{(iii)} multi-scale systems of overdetermined equations; (𝑖𝑣)\mathit{(iv)} enriched interpolation (activation) functional spaces. However, how to mitigate the gradient competition between multi-objective loss functions and accurately capture the frequency of PDEs remains an open research question.

The current research for balancing gradient competition between boundary errors and PDE errors is as follows: second-order optimization perspective, a new quasi-Newton method [[10](https://arxiv.org/html/2510.17508v1#bib.bibx10)] ; dual cone gradient descent [[11](https://arxiv.org/html/2510.17508v1#bib.bibx11)] ; neural tangent kernel theory [[12](https://arxiv.org/html/2510.17508v1#bib.bibx12), [13](https://arxiv.org/html/2510.17508v1#bib.bibx13)] ; multi-magnitude PINNs [[14](https://arxiv.org/html/2510.17508v1#bib.bibx14)] ; conflict-free inverse gradients [[15](https://arxiv.org/html/2510.17508v1#bib.bibx15)] , etc. Several studies have discretized equation systems to solve the coupling among the multiple physical fields: semi implicit method for pressure linked equations (SIMPLE) [[17](https://arxiv.org/html/2510.17508v1#bib.bibx17)] ; component-consistent
pressure correction [[18](https://arxiv.org/html/2510.17508v1#bib.bibx18)], etc. Few experiments have studied the gradient competition between coupled equations [[16](https://arxiv.org/html/2510.17508v1#bib.bibx16)], etc. In brief, these methods have explored various approaches to correct the ill-conditioned numerical formats and have achieved favorable improvements. Thus, we try to develop a new type of PINNs, MF-PINNs, which decouples the equations and rebalances the loss functions to mitigate the gradient competition among different physical quantities.

Recently, a wide variety of operator mappings have been widely applied to PINNs. For instance, adaptive activation functions strategies [[19](https://arxiv.org/html/2510.17508v1#bib.bibx19)], Fourier feature PINNs (FFPINNs) [[20](https://arxiv.org/html/2510.17508v1#bib.bibx20)], DNN for approximating nonlinear operators [[21](https://arxiv.org/html/2510.17508v1#bib.bibx21), [22](https://arxiv.org/html/2510.17508v1#bib.bibx22)], etc. Besides, several studies have revealed the basic logic to make improvements, such as decomposition based DNN [[23](https://arxiv.org/html/2510.17508v1#bib.bibx23)] based on the Frequency Principle [[24](https://arxiv.org/html/2510.17508v1#bib.bibx24)] , etc. In all, these theories and approaches enhance the fitting and generalization capabilities of PINNs by developing the operators mappings. Hence, we aim to identify the proper periods of all multiple physical fields and construct a proper neural operator basis adaptive to the problem in order to improve accuracy and reduce extra computational costs.

Plenty of research has been devoted to developing optimal strategies for learning rate scheduling to improve PINNs. For example, physics-constrained neural networks with the minimax architecture [[25](https://arxiv.org/html/2510.17508v1#bib.bibx25)], residual adaptive networks [[26](https://arxiv.org/html/2510.17508v1#bib.bibx26)], preprocessing for weights and bias [[27](https://arxiv.org/html/2510.17508v1#bib.bibx27)], etc. Consequently, we aim to develop stable and universal learning rate decay strategies for improving.

In order to solve these problems above, we first explain why the traditional PINNs sometimes fail to converge to the analytical solutions under extreme physical constants. Then, we innovate a new kind of enhanced PINNs, MF-PINNs. We decouple the multiple physics fields of the Stokes-Darcy equations and add mixed-form equations into the loss functions. These improvements create well-conditioned loss functions for PINNs and mitigate gradient competition between muiltiple physical fields. Besides, we research the impact of the periodicity of activation functions and apply a fast and universal learning rate decay strategy for training PINNs.

The organization of this paper is as follows: In Section [2](https://arxiv.org/html/2510.17508v1#S2 "2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we introduce the coupled Stokes-Darcy model and decouple the velocity and pressure fields. In Section [3](https://arxiv.org/html/2510.17508v1#S3 "3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we present the traditional parallel PINNs and apply the multi-scale operator-decoupled equations to develop MF-PINNs. In Section [4](https://arxiv.org/html/2510.17508v1#S4 "4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we conduct numerical experiments to validate the effectiveness of our MF-PINNs and provide a detailed analysis based on the results. In Section [5](https://arxiv.org/html/2510.17508v1#S5 "5 Conclusions and prospects ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we summarize several key suggestions for training PINNs.

## 2 Physical modeling

To begin with, we define a symbolic declaration in Section [2.1](https://arxiv.org/html/2510.17508v1#S2.SS1 "2.1 Symbol declaration ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Next, the coupled Stokes-Darcy system is established by physics laws in Section [2.2](https://arxiv.org/html/2510.17508v1#S2.SS2 "2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Furthermore, we decouple the velocity and pressure in Section [2.3](https://arxiv.org/html/2510.17508v1#S2.SS3 "2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").

### 2.1 Symbol declaration

1. 1.

   The subscript ss means the Stokes system and the subscript dd means the Darcy system. And the subscript N​NNN represents a numerical solution of PINNs.
2. 2.

   The Ω\Omega represents a given domain with boundary ∂Ω\partial\Omega, and Γ\Gamma represents a certain subset of ∂Ω\partial\Omega. The μ​(Ω)\mu(\Omega) represents the measurement of the region Ω\Omega. The 𝐧s\mathbf{n}\_{s} and 𝐧d\mathbf{n}\_{d} respectively represent the outward normal vectors of the domain. The 𝝉\boldsymbol{\tau} represents the tangential vector. Their relationships are as follows:

   |  |  |  |
   | --- | --- | --- |
   |  | Ω=Ωs∪Ωd,Γ=∂Ωs∩∂Ωd,Γs=∂Ωs∖Γ,Γd=∂Ωd∖Γ.\displaystyle\Omega=\Omega\_{s}\cup\Omega\_{d},\Gamma=\partial\Omega\_{s}\cap\partial\Omega\_{d},\Gamma\_{s}=\partial\Omega\_{s}\setminus\Gamma,\Gamma\_{d}=\partial\Omega\_{d}\setminus\Gamma. |  |
3. 3.

   The bolded vector 𝐮=[u,v]T\mathbf{u}=\left[u,v\right]^{T} in 2D or 𝐮=[u1,u2,u3]T\mathbf{u}=\left[u\_{1},u\_{2},u\_{3}\right]^{T} in 3D stands for the velocity field and the components paired with the Cartesian coordinates, xx, yy, and zz. Similarly, the Ψ\Psi in 2D or the 𝚿=[Ψ1,Ψ2,Ψ3]T\mathbf{\Psi}=\left[\Psi\_{1},\Psi\_{2},\Psi\_{3}\right]^{T} in 3D stands for Streamline field. The 𝝎=[ω1,ω2,ω3]T\boldsymbol{\omega}=\left[\omega\_{1},\omega\_{2},\omega\_{3}\right]^{T} in 3D represents the vorticity field. And the unbold scalar pp represents the pressure field.
4. 4.

   In a 3D steady flow the streamline field is the family of curves 𝚿\mathbf{\Psi} and its rotation is the velocity field, ∇×𝚿=𝐮\nabla\times\mathbf{\Psi}=\mathbf{u}. The vorticity 𝝎\boldsymbol{\omega} is the rotation of the velocity field 𝐮\mathbf{u}, 𝝎=∇×𝐮\boldsymbol{\omega}=\nabla\times\mathbf{u}. It measures the local rotation of fluid.
5. 5.

   The 𝕂\mathbb{K} represents an n-dimensional matrix, and it is a constant. The 𝕀\mathbb{I} represents the identity matrix. The 𝟏=[1,⋯,1]\mathbf{1}=\left[1,\cdots,1\right] is a row vector of shape 1×n1\times n in nD. Its every element is 11.
6. 6.

   The symbol ∘\circ denotes the composite functions (mappings), and it means composite functions (mappings) are performed from right to left. The order of differential operators is the same.
7. 7.

   The symbol ∥⋅∥2\left\|\cdot\right\|\_{2} represents the Euclidean norm of a matrix or vector. The e​r​r​L2err\mathit{L}\_{2} means the relative Euclidean norm.
8. 8.

   The x ≫\gg y or x ≪\ll y respectively means that x is much higher than or much lower than y.
9. 9.

   θ\theta is the adaptive parameter of the activation functions. Furthermore, aa and bb are respectively adaptive parameters of the parallel PINNs in the Stokes and Darcy domains.

### 2.2 The velocity-pressure form of the Stokes-Darcy system

Here, we introduce the equations of the coupled Stokes-Darcy equations in the VP form [[28](https://arxiv.org/html/2510.17508v1#bib.bibx28)] in the following four parts and Fig. [1](https://arxiv.org/html/2510.17508v1#S2.F1 "Fig. 1 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").
  
Stokes’ law

The steady incompressible Stokes equations describe the motion of viscous fluids when the inertial forces are negligible compared to the viscous forces:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |
|  | −∇⋅𝒯​(𝐮s,ps)\displaystyle-\nabla\cdot\mathcal{T}(\mathbf{u}\_{s},p\_{s}) | =𝐟s,\displaystyle=\mathbf{f}\_{s}, |  | 𝐱∈Ωs,\displaystyle\mathbf{x}\in\Omega\_{s}, |  | (1a) |
|  | ∇⋅𝐮s\displaystyle\nabla\cdot\mathbf{u}\_{s} | =0,\displaystyle=0, |  | 𝐱∈Ωs,\displaystyle\mathbf{x}\in\Omega\_{s}, |  | (1b) |
|  | 𝐮s\displaystyle\mathbf{u}\_{s} | =𝐠Γs,\displaystyle=\mathbf{g}\_{\Gamma\_{s}}, |  | 𝐱∈Γs,\displaystyle\mathbf{x}\in\Gamma\_{s}, |  | (1c) |

where 𝐮s\mathbf{u}\_{s} represents the fluid velocity, psp\_{s} represents the kinematic pressure, 𝐟s\mathbf{f}\_{s} represents the external force (homogeneous or inhomogeneous term), ν>0\nu>0 represents the kinematic viscosity of the fluid, 𝒯​(𝐮s,ps)=2​ν​𝒟​(𝐮s)−ps​𝕀\mathcal{T}(\mathbf{u}\_{s},p\_{s})=2\nu\mathcal{D}(\mathbf{u}\_{s})-p\_{s}\mathbb{I} represents the stress tensor, and 𝒟​(𝐮s)=(∇𝐮s+(∇𝐮s)T)/2\mathcal{D}(\mathbf{u}\_{s})=(\nabla\mathbf{u}\_{s}+(\nabla\mathbf{u}\_{s})^{T})/2 represents the deformation tensor. The ([1a](https://arxiv.org/html/2510.17508v1#S2.E1.1 "In 1 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) could be simplified as ∇ps−ν​Δ​𝐮s=𝐟s\nabla p\_{s}-\nu\Delta\mathbf{u}\_{s}=\mathbf{f}\_{s} when the Stokes fluid is incompressible embodied in ([1b](https://arxiv.org/html/2510.17508v1#S2.E1.2 "In 1 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).

Darcy’s Law

The steady incompressible Darcy equations describe fluid flow within the porous medium:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |
|  | ν​𝕂−1​𝐮d+∇pd\displaystyle\nu\mathbb{K}^{-1}\mathbf{u}\_{d}+\nabla p\_{d} | =𝐟d,\displaystyle=\mathbf{f}\_{d}, |  | 𝐱∈Ωd,\displaystyle\mathbf{x}\in\Omega\_{d}, |  | (2a) |
|  | ∇⋅𝐮d\displaystyle\nabla\cdot\mathbf{u}\_{d} | =0,\displaystyle=0, |  | 𝐱∈Ωd,\displaystyle\mathbf{x}\in\Omega\_{d}, |  | (2b) |
|  | 𝐮d⋅𝐧d\displaystyle\mathbf{u}\_{d}\cdot\mathbf{n}\_{d} | =𝐠Γd,\displaystyle=\mathbf{g}\_{\Gamma\_{d}}, |  | 𝐱∈Γd,\displaystyle\mathbf{x}\in\Gamma\_{d}, |  | (2c) |

where 𝐮d\mathbf{u}\_{d} represents the fluid velocity, pdp\_{d} represents the dynamic pressure, 𝐟d\mathbf{f}\_{d} represents the external force source term, and permeability tensor 𝕂\mathbb{K} represents a positive symmetric tensor. Although tensor 𝕂\mathbb{K} may vary, it usually keeps 𝕂=κ​𝕀\mathbb{K}=\kappa\mathbb{I}.

Interface conditions

The well-known Beavers-Joseph-Saffman boundary conditions describe the flow characteristics at the interface between the free-flow region of Stokes equation and the porous medium region of Darcy equation:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | |
|  | 𝐮s⋅𝐧s+𝐮d⋅𝐧d\displaystyle\mathbf{u}\_{s}\cdot\mathbf{n}\_{s}+\mathbf{u}\_{d}\cdot\mathbf{n}\_{d} | =0,\displaystyle=0, |  | 𝐱∈Γ,\displaystyle\mathbf{x}\in\Gamma, |  | (3a) |
|  | 2​ν​𝐧s⋅𝒟​(𝐮s)⋅𝐧s−ps+pd\displaystyle 2\nu\mathbf{n}\_{s}\cdot\mathcal{D}(\mathbf{u}\_{s})\cdot\mathbf{n}\_{s}-p\_{s}+p\_{d} | =gΓ1,\displaystyle=g\_{\Gamma\_{1}}, |  | 𝐱∈Γ,\displaystyle\mathbf{x}\in\Gamma, |  | (3b) |
|  | 2​𝐧s⋅𝒟​(𝐮s)⋅𝝉+α​𝕂−1/2​𝐮s⋅𝝉\displaystyle 2\mathbf{n}\_{s}\cdot\mathcal{D}(\mathbf{u}\_{s})\cdot\boldsymbol{\tau}+\alpha\mathbb{K}^{-1/2}\mathbf{u}\_{s}\cdot\boldsymbol{\tau} | =gΓ2,\displaystyle=g\_{\Gamma\_{2}}, |  | 𝐱∈Γ,\displaystyle\mathbf{x}\in\Gamma, |  | (3c) |

where the parameter α\alpha is a constant affected by the friction.

The first equation ([3a](https://arxiv.org/html/2510.17508v1#S2.E3.1 "In 3 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) stands for the continuity of normal velocity to keep the mass conservation, the second equation ([3b](https://arxiv.org/html/2510.17508v1#S2.E3.2 "In 3 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) stands for the continuity of normal stress to keep the equilibrium condition, and the last equation ([3c](https://arxiv.org/html/2510.17508v1#S2.E3.3 "In 3 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) stands for frictional effects at the interface in order to keep the tangential velocity slip condition [[1](https://arxiv.org/html/2510.17508v1#bib.bibx1)], as is shown in Fig. [1](https://arxiv.org/html/2510.17508v1#S2.F1 "Fig. 1 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").

Pressure conditions

The pressure is non-unique due to an additional constant hidden in this system, because ps−pdp\_{s}-p\_{d} and (ps+C)−(pd+C)(p\_{s}+C)-(p\_{d}+C) are equivalent in ([3b](https://arxiv.org/html/2510.17508v1#S2.E3.2 "In 3 ‣ 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")). Thus, we could add ([4](https://arxiv.org/html/2510.17508v1#S2.E4 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) to fix the reference frame of the pressure field:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∫Ωsps​𝑑Ωs+∫Ωdpd​𝑑Ωd)/(μ​(Ωs)+μ​(Ωd))=Cp,𝐱∈Ωs​o​r​𝐱∈Ωd.\displaystyle\left(\int\_{\Omega\_{s}}p\_{s}\,d{\Omega\_{s}}+\int\_{\Omega\_{d}}p\_{d}\,d{\Omega\_{d}}\right)\Big/\left(\mu(\Omega\_{s})+\mu(\Omega\_{d})\right)=C\_{p},\quad\mathbf{x}\in\Omega\_{s}\,\,\,or\,\,\,\mathbf{x}\in\Omega\_{d}. |  | (4) |

![Refer to caption](x1.png)


Fig. 1: This cartoon overviews the coupled Stokes-Darcy model with the BJS interface conditions.

### 2.3 The stream-vorticity form of the Stokes-Darcy system

Below we would infer the decoupled form of SV form of Stokes-Darcy equations [[29](https://arxiv.org/html/2510.17508v1#bib.bibx29)].

###### Theorem 1.

The streamline field 𝚿s\mathbf{\Psi}\_{s} and pressure field psp\_{s} of steady Stokes equations could be decoupled as the form ℒ1​(𝚿s,𝐟s)=0\mathcal{L}\_{1}(\mathbf{\Psi}\_{s},\mathbf{f}\_{s})=0 and ℒ2​(ps,𝐟s)=0\mathcal{L}\_{2}(p\_{s},\mathbf{f}\_{s})=0. The ℒ1​(𝚿s,𝐟s)=0\mathcal{L}\_{1}(\mathbf{\Psi}\_{s},\mathbf{f}\_{s})=0 is a fourth-order equation without psp\_{s} and ℒ2​(ps,𝐟s)=0\mathcal{L}\_{2}(p\_{s},\mathbf{f}\_{s})=0 is an elliptic equation without 𝚿s\mathbf{\Psi}\_{s}.

###### Proof.

We note the rotation of streamline field ∇×𝚿s\nabla\times\mathbf{\Psi}\_{s} and gradient of pressure field ∇ps\nabla p\_{s} of Stokes equation are coupled by the kinematic viscosity ν\nu in ([1](https://arxiv.org/html/2510.17508v1#S2.E1 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).
We could apply differential operators 𝟏⋅∇×\mathbf{1}\cdot\nabla\times and ∇⋅\nabla\cdot to both sides of ([1](https://arxiv.org/html/2510.17508v1#S2.E1 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")). Hence, we could get ([5](https://arxiv.org/html/2510.17508v1#Sx4.EGx6 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | ℒ1​(𝚿s,𝐟s)\displaystyle\mathcal{L}\_{1}(\mathbf{\Psi}\_{s},\mathbf{f}\_{s}) | =𝟏⋅∇×∇ps⏞Gradient has no Rotation.−   1⋅∇×(𝐟s+ν​Δ​(∇×𝚿s))=0,\displaystyle=\!\!\!\!\!\!\overbrace{\mathbf{1}\cdot\nabla\times\nabla p\_{s}}^{\text{{Gradient} has no {Rotation}.}}\!\!\!\!\!\!-\,\,\,\mathbf{1}\cdot\nabla\times(\mathbf{f}\_{s}+\nu\Delta(\nabla\times\mathbf{\Psi}\_{s}))\,\,\,=0, |  | (5a) |
|  | ℒ2​(ps,𝐟s)\displaystyle\mathcal{L}\_{2}(p\_{s},\mathbf{f}\_{s}) | =∇⋅(−ν​Δ​(∇×𝚿s))⏟Rotation has no Divergence.+∇⋅∇ps⏟Δ​ps−∇⋅𝐟s=0.\displaystyle=\,\,\,\underbrace{\nabla\cdot(-\nu\Delta(\nabla\times\mathbf{\Psi}\_{s}))}\_{\text{{Rotation} has no {Divergence}.}}\,\,\,+\,\,\,\underbrace{\nabla\cdot\nabla p\_{s}}\_{\Delta\mathit{p\_{s}}}\,\,\,-\,\,\,\nabla\cdot\mathbf{f}\_{s}\,\,\,=0. |  | (5b) |

For example, if we apply differential operators 𝟏⋅∇×\mathbf{1}\cdot\nabla\times to both sides of ([1](https://arxiv.org/html/2510.17508v1#S2.E1 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) in 3D, we will notice ([6](https://arxiv.org/html/2510.17508v1#S2.E6 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇×∇ps=[0−∂∂z∂∂y∂∂z0−∂∂x−∂∂y∂∂x0]​[∂∂x∂∂y∂∂z]​ps=𝟎.\displaystyle\nabla\times\nabla p\_{s}=\begin{bmatrix}0&-\frac{\partial}{\partial z}&\frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}&0&-\frac{\partial}{\partial x}\\ -\frac{\partial}{\partial y}&\frac{\partial}{\partial x}&0\end{bmatrix}\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}p\_{s}=\mathbf{0}. |  | (6) |

And finally we could get ([7](https://arxiv.org/html/2510.17508v1#S2.E7 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ1​(𝚿s,𝐟s)=−[0−∂∂z∂∂y∂∂z0−∂∂x−∂∂y∂∂x0]​([fs​1fs​2fs​3]+ν​(∂2∂x2+∂2∂y2+∂2∂z2)​[0−∂∂z∂∂y∂∂z0−∂∂x−∂∂y∂∂x0]​[𝚿s​1𝚿s​2𝚿s​3])=𝟎.\displaystyle\mathcal{L}\_{1}(\mathbf{\Psi}\_{s},\mathbf{f}\_{s})=-\begin{bmatrix}0&-\frac{\partial}{\partial z}&\frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}&0&-\frac{\partial}{\partial x}\\ -\frac{\partial}{\partial y}&\frac{\partial}{\partial x}&0\end{bmatrix}\left(\begin{bmatrix}f\_{s1}\\ f\_{s2}\\ f\_{s3}\end{bmatrix}+\nu\left(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\right)\begin{bmatrix}0&-\frac{\partial}{\partial z}&\frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}&0&-\frac{\partial}{\partial x}\\ -\frac{\partial}{\partial y}&\frac{\partial}{\partial x}&0\end{bmatrix}\begin{bmatrix}\mathbf{\Psi}\_{s1}\\ \mathbf{\Psi}\_{s2}\\ \mathbf{\Psi}\_{s3}\end{bmatrix}\right)=\mathbf{0}. |  | (7) |

If we apply differential operators ∇⋅\nabla\cdot to both sides of ([1](https://arxiv.org/html/2510.17508v1#S2.E1 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) in 3D, we will notice ([8](https://arxiv.org/html/2510.17508v1#S2.E8 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | −ν​∇⋅∇×Δ​𝚿s=−ν​(∂2∂x2+∂2∂y2+∂2∂z2)​[∂∂x∂∂y∂∂z]T​[0−∂∂z∂∂y∂∂z0−∂∂x−∂∂y∂∂x0]​[𝚿s​1𝚿s​2𝚿s​3]=0.\displaystyle-\nu\nabla\cdot\nabla\times\Delta\mathbf{\Psi}\_{s}=-\nu\left(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\right)\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}^{T}\begin{bmatrix}0&-\frac{\partial}{\partial z}&\frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}&0&-\frac{\partial}{\partial x}\\ -\frac{\partial}{\partial y}&\frac{\partial}{\partial x}&0\end{bmatrix}\begin{bmatrix}\mathbf{\Psi}\_{s1}\\ \mathbf{\Psi}\_{s2}\\ \mathbf{\Psi}\_{s3}\end{bmatrix}=0. |  | (8) |

And finally we could get ([9](https://arxiv.org/html/2510.17508v1#S2.E9 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ2​(ps,𝐟s)=[∂∂x∂∂y∂∂z]T​[∂∂x∂∂y∂∂z]​ps−[∂∂x∂∂y∂∂z]T​[f1f2f3]=(∂2∂x2+∂2∂y2+∂2∂z2)​ps−[∂∂x∂∂y∂∂z]T​[fs​1fs​2fs​3]=0.\displaystyle\mathcal{L}\_{2}(p\_{s},\mathbf{f}\_{s})=\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}^{T}\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}p\_{s}-\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}^{T}\begin{bmatrix}f\_{1}\\ f\_{2}\\ f\_{3}\end{bmatrix}=\left(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\right)p\_{s}-\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}^{T}\begin{bmatrix}f\_{s1}\\ f\_{s2}\\ f\_{s3}\end{bmatrix}=0. |  | (9) |

We notice using Cramer’s rule to solve for the partial derivative of ([1](https://arxiv.org/html/2510.17508v1#S2.E1 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) could result in ([5](https://arxiv.org/html/2510.17508v1#Sx4.EGx6 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")), but the indefinite integral only determines the original function with an additional constant. So ([1](https://arxiv.org/html/2510.17508v1#S2.E1 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) are sufficient but unnecessary conditions for ([5](https://arxiv.org/html/2510.17508v1#Sx4.EGx6 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")). A 2D case can be derived from a 3D one.
∎

###### Theorem 2.

The streamline field 𝚿d\mathbf{\Psi}\_{d} and pressure field pdp\_{d} of steady Darcy equations could be decoupled as the form ℒ3​(𝚿d,𝐟d)=0\mathcal{L}\_{3}(\mathbf{\Psi}\_{d},\mathbf{f}\_{d})=0 and ℒ4​(pd,𝐟d)=0\mathcal{L}\_{4}(p\_{d},\mathbf{f}\_{d})=0. The ℒ3​(𝚿d,𝐟d)=0\mathcal{L}\_{3}(\mathbf{\Psi}\_{d},\mathbf{f}\_{d})=0 is a fourth-order equation without pdp\_{d} and ℒ4​(pd,𝐟d)=0\mathcal{L}\_{4}(p\_{d},\mathbf{f}\_{d})=0 is a equation without 𝚿d\mathbf{\Psi}\_{d}.

###### Proof.

We note that the rotation of streamline field ∇×𝚿d\nabla\times\mathbf{\Psi}\_{d} and gradient of pressure field ∇pd\nabla p\_{d} of the Darcy equation are coupled by the permeability and Reynolds number ratio ν​𝕂−1\nu\mathbb{K}^{-1} in ([2](https://arxiv.org/html/2510.17508v1#S2.E2 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).
We could apply differential operators 𝟏⋅∇×\mathbf{1}\cdot\nabla\times and ∇⋅𝕂\nabla\cdot\mathbb{K} to both sides of ([2](https://arxiv.org/html/2510.17508v1#S2.E2 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")). Hence, we could get ([10](https://arxiv.org/html/2510.17508v1#S2.E10 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | ℒ3​(𝚿d,𝐟d)\displaystyle\mathcal{L}\_{3}(\mathbf{\Psi}\_{d},\mathbf{f}\_{d}) | =   1⋅∇×(ν​𝕂−1​∇×𝚿d−𝐟d)+𝟏⋅∇×∇pd⏞Gradient has no Rotation.=0,\displaystyle=\,\,\,\mathbf{1}\cdot\nabla\times(\nu\mathbb{K}^{-1}\nabla\times\mathbf{\Psi}\_{d}-\mathbf{f}\_{d})\,\,\,+\!\!\!\!\!\!\overbrace{\mathbf{1}\cdot\nabla\times\nabla p\_{d}}^{\text{{Gradient} has no {Rotation}.}}\!\!\!\!\!\!=0, |  | (10a) |
|  | ℒ4​(pd,𝐟d)\displaystyle\mathcal{L}\_{4}(p\_{d},\mathbf{f}\_{d}) | =ν​∇⋅𝕂​𝕂−1​∇×𝚿d⏟Rotation has no Divergence.+∇⋅𝕂​(∇pd−𝐟d)=0.\displaystyle=\underbrace{\nu\nabla\cdot\mathbb{K}\mathbb{K}^{-1}\nabla\times\mathbf{\Psi}\_{d}}\_{\text{{Rotation} has no {Divergence}.}}+\,\,\,\nabla\cdot\mathbb{K}(\nabla p\_{d}-\mathbf{f}\_{d})\,\,\,=0. |  | (10b) |

For example, if we apply differential operators 𝟏⋅∇×\mathbf{1}\cdot\nabla\times to both sides of ([2](https://arxiv.org/html/2510.17508v1#S2.E2 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) in 3D, we will notice ([11](https://arxiv.org/html/2510.17508v1#S2.E11 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇×∇pd=[0−∂∂z∂∂y∂∂z0−∂∂x−∂∂y∂∂x0]​[∂∂x∂∂y∂∂z]​pd=𝟎.\displaystyle\nabla\times\nabla p\_{d}=\begin{bmatrix}0&-\frac{\partial}{\partial z}&\frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}&0&-\frac{\partial}{\partial x}\\ -\frac{\partial}{\partial y}&\frac{\partial}{\partial x}&0\end{bmatrix}\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}p\_{d}=\mathbf{0}. |  | (11) |

And finally we could get ([12](https://arxiv.org/html/2510.17508v1#S2.E12 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ3​(𝚿d,𝐟d)=ν​[0−∂∂z∂∂y∂∂z0−∂∂x−∂∂y∂∂x0]​([k11k12k13k21k22k23k31k32k33]−1​[𝚿d​1𝚿d​2𝚿d​3]−[fd​1fd​2fd​3])=0.\displaystyle\mathcal{L}\_{3}(\mathbf{\Psi}\_{d},\mathbf{f}\_{d})=\nu\begin{bmatrix}0&-\frac{\partial}{\partial z}&\frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}&0&-\frac{\partial}{\partial x}\\ -\frac{\partial}{\partial y}&\frac{\partial}{\partial x}&0\end{bmatrix}\left(\begin{bmatrix}k\_{11}&k\_{12}&k\_{13}\\ k\_{21}&k\_{22}&k\_{23}\\ k\_{31}&k\_{32}&k\_{33}\end{bmatrix}^{-1}\begin{bmatrix}\mathbf{\Psi}\_{d1}\\ \mathbf{\Psi}\_{d2}\\ \mathbf{\Psi}\_{d3}\end{bmatrix}-\begin{bmatrix}f\_{d1}\\ f\_{d2}\\ f\_{d3}\end{bmatrix}\right)=0. |  | (12) |

In a similar way, if we apply differential operators ∇⋅\nabla\cdot to both sides of ([2](https://arxiv.org/html/2510.17508v1#S2.E2 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) in 3D, we will notice ([13](https://arxiv.org/html/2510.17508v1#S2.E13 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν​∇⋅𝕂​𝕂−1​∇×𝚿d=ν​[∂∂x∂∂y∂∂z]T​[k11k12k13k21k22k23k31k32k33]​[k11k12k13k21k22k23k31k32k33]−1​[0−∂∂z∂∂y∂∂z0−∂∂x−∂∂y∂∂x0]​[𝚿d​1𝚿d​2𝚿d​3]=0.\displaystyle\nu\nabla\cdot\mathbb{K}\mathbb{K}^{-1}\nabla\times\mathbf{\Psi}\_{d}=\nu\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}^{T}\begin{bmatrix}k\_{11}&k\_{12}&k\_{13}\\ k\_{21}&k\_{22}&k\_{23}\\ k\_{31}&k\_{32}&k\_{33}\end{bmatrix}\begin{bmatrix}k\_{11}&k\_{12}&k\_{13}\\ k\_{21}&k\_{22}&k\_{23}\\ k\_{31}&k\_{32}&k\_{33}\end{bmatrix}^{-1}\begin{bmatrix}0&-\frac{\partial}{\partial z}&\frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}&0&-\frac{\partial}{\partial x}\\ -\frac{\partial}{\partial y}&\frac{\partial}{\partial x}&0\end{bmatrix}\begin{bmatrix}\mathbf{\Psi}\_{d1}\\ \mathbf{\Psi}\_{d2}\\ \mathbf{\Psi}\_{d3}\end{bmatrix}=0. |  | (13) |

And finally we could get ([14](https://arxiv.org/html/2510.17508v1#S2.E14 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ4​(pd,𝐟d)=ν​[∂∂x∂∂y∂∂z]T​[k11k12k13k21k22k23k31k32k33]​([∂∂x∂∂y∂∂z]​pd−[fd​1fd​2fd​3])=𝟎.\displaystyle\mathcal{L}\_{4}(p\_{d},\mathbf{f}\_{d})=\nu\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}^{T}\begin{bmatrix}k\_{11}&k\_{12}&k\_{13}\\ k\_{21}&k\_{22}&k\_{23}\\ k\_{31}&k\_{32}&k\_{33}\end{bmatrix}\left(\begin{bmatrix}\frac{\partial}{\partial x}\\ \frac{\partial}{\partial y}\\ \frac{\partial}{\partial z}\end{bmatrix}p\_{d}-\begin{bmatrix}f\_{d1}\\ f\_{d2}\\ f\_{d3}\end{bmatrix}\right)=\mathbf{0}. |  | (14) |

We notice using Cramer’s rule to solve for the partial derivative of ([2](https://arxiv.org/html/2510.17508v1#S2.E2 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) could result in ([10](https://arxiv.org/html/2510.17508v1#S2.E10 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")), but the indefinite integral only determines the original function with an additional constant. So ([2](https://arxiv.org/html/2510.17508v1#S2.E2 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) are sufficient but unnecessary conditions for ([10](https://arxiv.org/html/2510.17508v1#S2.E10 "In 2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")). A 2D case can be derived from a 3D one.
∎

## 3 Algorithm framework

First of all, we list the numerical solution forms of DNN and PINNS in Section [3.1](https://arxiv.org/html/2510.17508v1#S3.SS1 "3.1 Numerical solutions of DNN ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Secondly, we explain how PINNs solves the coupled Stokes-Darcy equations in Section [3.2](https://arxiv.org/html/2510.17508v1#S3.SS2 "3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Thirdly, we construct improved loss functions by using VP form equations and SV form equations from Section [2.3](https://arxiv.org/html/2510.17508v1#S2.SS3 "2.3 The stream-vorticity form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") to alleviate gradient competition in Section [3.2.1](https://arxiv.org/html/2510.17508v1#S3.SS2.SSS1 "3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Lastly, we adopt several training strategies to accelerate converging and improve stability in Section [3.3](https://arxiv.org/html/2510.17508v1#S3.SS3 "3.3 Activation functions with high-frequency features ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") and Section [3.4](https://arxiv.org/html/2510.17508v1#S3.SS4 "3.4 Optimizer and learning rate decay ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").

### 3.1 Numerical solutions of DNN

DNN could be formed by the composition of multiple nonlinear and linear mappings belonging to undetermined weights and bias. In other words, PINNs could be regarded as a kind of numerical solutions (NN solutions) composed of various functions ([15](https://arxiv.org/html/2510.17508v1#S3.E15 "In 3.1 Numerical solutions of DNN ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | uN​N​(𝐱,𝐰,𝐛)=∑n=1Nmwm,n​ℱm−1,n​(⋯​∑n=1N2w2,n​ℱ1,n​(∑n=1N1w1,n​xn+b1,n)+b2,n​⋯)+bm,n,\displaystyle\hskip-28.45274ptu\_{NN}(\mathbf{x},\mathbf{w},\mathbf{b})=\sum\_{n=1}^{N\_{m}}w\_{m,n}\mathcal{F}\_{m-1,n}\left(\cdots\sum\_{n=1}^{N\_{2}}w\_{2,n}\mathcal{F}\_{1,n}(\sum\_{n=1}^{N\_{1}}w\_{1,n}x\_{n}+b\_{1,n})+b\_{2,n}\cdots\right)+b\_{m,n}, |  | (15) |

where Θ={wm,n,bm,n}m=1,2,⋯,M\Theta=\{w\_{m,n},b\_{m,n}\}\_{m=1,2,\cdots,M} are undetermined parameters groups of the PINNs solutions, wm,nw\_{m,n} is the nt​hn^{th} weight of the mt​hm^{th} linear layer, bm,nb\_{m,n} is the nt​hn^{th} bia of the mt​hm^{th} linear layer and ℱm,n\mathcal{F}\_{m,n} is the nt​hn^{th} activation function paired with the mt​hm^{th} linear layer.

This feature endows PINNs with several advantages — extensive fitting capabilities [[31](https://arxiv.org/html/2510.17508v1#bib.bibx31)], rapid computing [[32](https://arxiv.org/html/2510.17508v1#bib.bibx32)], various well-proposed function spaces, and superior generalization and transfer learning performance for extrapolation [[33](https://arxiv.org/html/2510.17508v1#bib.bibx33)]. In the Stokes-Darcy problems, we had better select sufficient smooth activation functions like tanh, sigmoid, sin ∈C∞\in C^{\infty} or Pn​[x]​(n>1)P^{n}[x](n>1), but we could not select ReLU ∈C0\in C^{0} and its family [[34](https://arxiv.org/html/2510.17508v1#bib.bibx34)].

### 3.2 Physical information drives optimization

A significant work for PINNs is that we need to design the total loss function 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta) based on the boundary conditions and equations in order to induce PINNs solutions ([15](https://arxiv.org/html/2510.17508v1#S3.E15 "In 3.1 Numerical solutions of DNN ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) to converge to analytical solutions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐱fs,Θ)=1Nfs​∑n=1Nfs‖−ν​∇×Δ​𝚿s​N​N​(𝐱nfs)+∇ps​N​N​(𝐱nfs)−𝐟s​(𝐱nfs)‖22,\displaystyle\hskip 0.0pt\mathcal{J}(\mathbf{x}\_{f\_{s}},\Theta)=\frac{1}{N\_{f\_{s}}}\sum\_{n=1}^{N\_{f\_{s}}}\left\|-\nu\nabla\times\Delta\mathbf{\Psi}\_{sNN}(\mathbf{x}\_{n}^{f\_{s}})+\nabla p\_{sNN}(\mathbf{x}\_{n}^{f\_{s}})-\mathbf{f}\_{s}(\mathbf{x}\_{n}^{f\_{s}})\right\|\_{2}^{2}, |  | (16) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐱fd,Θ)=1Nfd​∑n=1Nfd‖ν​𝕂−1​∇×𝚿d​N​N​(𝐱nfd)+∇pd​N​N​(𝐱nfd)−𝐟d​(𝐱nfd)‖22,\displaystyle\hskip 0.0pt\mathcal{J}(\mathbf{x}\_{f\_{d}},\Theta)=\frac{1}{N\_{f\_{d}}}\sum\_{n=1}^{N\_{f\_{d}}}\left\|\nu\mathbb{K}^{-1}\nabla\times\mathbf{\Psi}\_{dNN}(\mathbf{x}\_{n}^{f\_{d}})+\nabla p\_{dNN}(\mathbf{x}\_{n}^{f\_{d}})-\mathbf{f}\_{d}(\mathbf{x}\_{n}^{f\_{d}})\right\|\_{2}^{2}, |  | (17) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐱Γ,Θ)=1NΓ​∑n=1Nu​Γ[∥∇×𝚿s​N​N(𝐱nΓ)⋅𝐧s+∇×𝚿d​N​N(𝐱nΓ)⋅𝐧d∥22+‖2​ν​𝐧s⋅𝒟​(∇×𝚿s​N​N​(𝐱nΓ))⋅𝐧s−ps​N​N​(𝐱nΓ)+pd​N​N​(𝐱nΓ)−gΓ1​(𝐱nΓ)‖22+∥2𝐧s⋅𝒟(∇×𝚿s​N​N(𝐱nΓ))⋅𝝉+α𝕂−1/2∇×𝚿s​N​N(𝐱nΓ)⋅τ−gΓ2(𝐱nΓ)∥22],\displaystyle\begin{aligned} \mathcal{J}(\mathbf{x}\_{\Gamma},\Theta)=\frac{1}{N\_{\Gamma}}\sum\_{n=1}^{N\_{u\Gamma}}&\left[\left\|\nabla\times\mathbf{\Psi}\_{sNN}(\mathbf{x}\_{n}^{\Gamma})\cdot\mathbf{n}\_{s}+\nabla\times\mathbf{\Psi}\_{dNN}(\mathbf{x}\_{n}^{\Gamma})\cdot\mathbf{n}\_{d}\right\|\_{2}^{2}\right.\\ &+\left\|2\nu\mathbf{n}\_{s}\cdot\mathcal{D}(\nabla\times\mathbf{\Psi}\_{sNN}(\mathbf{x}\_{n}^{\Gamma}))\cdot\mathbf{n}\_{s}-p\_{sNN}(\mathbf{x}\_{n}^{\Gamma})+p\_{dNN}(\mathbf{x}\_{n}^{\Gamma})-g\_{\Gamma\_{1}}(\mathbf{x}\_{n}^{\Gamma})\right\|\_{2}^{2}\\ &\left.+\left\|2\mathbf{n}\_{s}\cdot\mathcal{D}(\nabla\times\mathbf{\Psi}\_{sNN}(\mathbf{x}\_{n}^{\Gamma}))\cdot\boldsymbol{\tau}+\alpha\mathbb{K}^{-1/2}\nabla\times\mathbf{\Psi}\_{sNN}(\mathbf{x}\_{n}^{\Gamma})\cdot\tau-g\_{\Gamma\_{2}}(\mathbf{x}\_{n}^{\Gamma})\right\|\_{2}^{2}\right],\end{aligned} |  | (18) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐱us,Θ)=1Nus​∑n=1Nus‖∇×𝚿s​N​N​(𝐱nus)−𝐠Γs​(𝐱nus)‖22,\displaystyle\hskip 0.0pt\mathcal{J}(\mathbf{x}\_{u\_{s}},\Theta)=\frac{1}{N\_{u\_{s}}}\sum\_{n=1}^{N\_{u\_{s}}}\left\|\nabla\times\mathbf{\Psi}\_{sNN}(\mathbf{x}\_{n}^{u\_{s}})-\mathbf{g}\_{\Gamma\_{s}}(\mathbf{x}\_{n}^{u\_{s}})\right\|\_{2}^{2}, |  | (19) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐱ud,Θ)=1Nud​∑n=1Nud‖∇×𝚿d​N​N​(𝐱nud)⋅𝐧d−𝐠Γd​(𝐱nud)‖22,\displaystyle\hskip 0.0pt\mathcal{J}(\mathbf{x}\_{u\_{d}},\Theta)=\frac{1}{N\_{u\_{d}}}\sum\_{n=1}^{N\_{u\_{d}}}\left\|\nabla\times\mathbf{\Psi}\_{dNN}(\mathbf{x}\_{n}^{u\_{d}})\cdot\mathbf{n}\_{d}-\mathbf{g}\_{\Gamma\_{d}}(\mathbf{x}\_{n}^{u\_{d}})\right\|\_{2}^{2}, |  | (20) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐱,Θ)=λfs​𝒥​(𝐱fs,Θ)+λfd​𝒥​(𝐱fd,Θ)+λΓ​𝒥​(𝐱Γ,Θ)+λus​𝒥​(𝐱us,Θ)+λud​𝒥​(𝐱ud,Θ),\displaystyle\mathcal{J}(\mathbf{x},\Theta)=\lambda\_{f\_{s}}\mathcal{J}(\mathbf{x}\_{f\_{s}},\Theta)+\lambda\_{f\_{d}}\mathcal{J}(\mathbf{x}\_{f\_{d}},\Theta)+\lambda\_{\Gamma}\mathcal{J}(\mathbf{x}\_{\Gamma},\Theta)+\lambda\_{u\_{s}}\mathcal{J}(\mathbf{x}\_{u\_{s}},\Theta)+\lambda\_{u\_{d}}\mathcal{J}(\mathbf{x}\_{u\_{d}},\Theta), |  | (21) |

where ([16](https://arxiv.org/html/2510.17508v1#S3.E16 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) stands for the loss of the Stokes equation, ([17](https://arxiv.org/html/2510.17508v1#S3.E17 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) stands for the loss of the Darcy equation, ([18](https://arxiv.org/html/2510.17508v1#S3.E18 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) stands for the loss on the coupled interface, ([19](https://arxiv.org/html/2510.17508v1#S3.E19 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) and ([20](https://arxiv.org/html/2510.17508v1#S3.E20 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) respectively stand for the loss on the boundary conditions of the Stokes equation and the Darcy equation, and different coefficients λ\lambda stand for the difference in importance of the five loss functions in different PINNs.

Finally, we add the five loss functions with different coefficients λ\lambda to get the total loss function ([21](https://arxiv.org/html/2510.17508v1#S3.E21 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")). Therefore, based on [[31](https://arxiv.org/html/2510.17508v1#bib.bibx31)] and [[35](https://arxiv.org/html/2510.17508v1#bib.bibx35)], we could conclude:

###### Theorem 3.

For any ε>0\varepsilon>0, there exists a wide and deep enough neural network ℱN​N​(𝐱,Θ)=(𝚿N​N,∇pN​N)\mathcal{F}\_{NN}(\mathbf{x},\Theta)=(\mathbf{\Psi}\_{NN},\nabla p\_{NN}) with sufficiently large degrees of freedom D​O​FΘDOF\_{\Theta} to make:

|  |  |  |
| --- | --- | --- |
|  | minΘ​𝒥​(𝐱,Θ)=𝒥​(𝐱,Θ^)<ε.\underset{\Theta}{\mbox{min}}\mathcal{J}(\mathbf{x},\Theta)=\mathcal{J}(\mathbf{x},\hat{\Theta})<\varepsilon. |  |

Moreover, the following error bounds hold:

|  |  |  |
| --- | --- | --- |
|  | ‖∇×𝚿N​N​(𝐱,Θ^)−𝐮​(𝐱)‖2<C1​εn1,\left\|\nabla\times\mathbf{\Psi}\_{NN}(\mathbf{x},\hat{\Theta})-\mathbf{u}(\mathbf{x})\right\|\_{2}<C\_{1}\varepsilon^{n\_{1}}, |  |

|  |  |  |
| --- | --- | --- |
|  | ‖∇pN​N​(𝐱,Θ^)−∇p​(𝐱)‖2<C2​εn2,\left\|\nabla p\_{NN}(\mathbf{x},\hat{\Theta})-\nabla p(\mathbf{x})\right\|\_{2}<C\_{2}\varepsilon^{n\_{2}}, |  |

where C1C\_{1} and C2C\_{2} are known constants, and n1n\_{1} and n2n\_{2} are positive integers.

Remarking on Section [2.2](https://arxiv.org/html/2510.17508v1#S2.SS2 "2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we consider that the pressure field of the PINNs numerical solutions, ps​N​Np\_{sNN} and pd​N​Np\_{dNN}, differ from the analytical solutions, psp\_{s} and pdp\_{d} by a constant CpC\_{p}. Thus, we set bias = ’False’ for the last linear layer, and we developed ([22](https://arxiv.org/html/2510.17508v1#S3.E22 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) and ([23](https://arxiv.org/html/2510.17508v1#S3.E23 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) to correct pN​N​sp\_{NNs} and pN​N​dp\_{NNd} based on ([4](https://arxiv.org/html/2510.17508v1#S2.E4 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")), after updating the weights and bias per epoch.

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∑m=1Ns(ps​N​N​(𝐱m,Θ^)−ps​(𝐱m))+∑n=1Nd(pd​N​N​(𝐱n,Θ^)−pd​(𝐱n)))/(Ns+Nd)≈Cp​N​N−Cp,𝐱∈Ωs∪Ωd.\displaystyle\left(\sum\_{m=1}^{N\_{s}}\left(p\_{sNN}(\mathbf{x}\_{m},\hat{\Theta})-p\_{s}(\mathbf{x}\_{m})\right)+\sum\_{n=1}^{N\_{d}}\left(p\_{dNN}(\mathbf{x}\_{n},\hat{\Theta})-p\_{d}(\mathbf{x}\_{n})\right)\right)\Big/(N\_{s}+N\_{d})\approx C\_{pNN}-C\_{p},\,\mathbf{x}\in\Omega\_{s}\cup\Omega\_{d}. |  | (22) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | p~N​N​(𝐱,Θ^)=pN​N​(𝐱,Θ^)−Cp​N​N+Cp,\displaystyle\widetilde{p}\_{NN}(\mathbf{x},\hat{\Theta})=p\_{NN}(\mathbf{x},\hat{\Theta})-C\_{pNN}+C\_{p}, |  | (23) |

![Refer to caption](x2.png)
  


Fig. 2: This cartoon shows how we combine the VP form and the SV form and design the total new loss function with appropriate weights in the Darcy domain.

#### 3.2.1 Gradient competition and MF-PINNs

Gradient competition may be a potential risk to the training of PINNs. If we directly construct the loss function in Section [3.2](https://arxiv.org/html/2510.17508v1#S3.SS2 "3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") for the Stokes-Darcy system, it may lead to the failure of PINNs training, possibily. A major reason why PINNs might fail is that extreme high or low constants (κ\kappa, ν\nu, etc.) in the multi-objective loss functions ([21](https://arxiv.org/html/2510.17508v1#S3.E21 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) may create competition in the gradients. What’s worse, the PINNs with such ill-conditioned loss functions may lead to the fact that some physical quantities have sufficient accuracy, but the optimization direction of other physical quantities is opposite to the optimal point, as is shown in Fig. [2](https://arxiv.org/html/2510.17508v1#S3.F2 "Fig. 2 ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").

The following are the potential risks for PINNs in Stokes-Darcy system:

1. 1.

   ν≫1\nu\gg 1 or ν≪1\nu\ll 1 may cause the gradient competition between 𝐮s\mathbf{u}\_{s} and psp\_{s}.
2. 2.

   ν/κ≫1\nu/\kappa\gg 1 or ν/κ≪1\nu/\kappa\ll 1 may cause the gradient competition between 𝐮d\mathbf{u}\_{d} and pdp\_{d}.
3. 3.

   ν≫ν/κ\nu\gg\nu/\kappa or ν≪ν/κ\nu\ll\nu/\kappa may cause the gradient competition between the Stokes system and the Darcy system.
4. 4.

   Extreme gradient may cause the gradient competition in total loss among the boundary, the interface, and the inner points.
5. 5.

   ν≫1\nu\gg 1 may cause the gradient exploration for the loss of the inner points during backward.

For example, if we chose ν=1\nu=1 and 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I}, the ratio of the updating gradients of ∇×𝚿d​N​N\nabla\times\mathbf{\Psi}\_{dNN} and ∇pd​N​N\nabla p\_{dNN} would be approximately 104:110^{4}:1. These choices
may result in ∇pd​N​N\nabla p\_{dNN} being very insignificant compared to ∇×𝚿d​N​N\nabla\times\mathbf{\Psi}\_{dNN}, and the loss function ([17](https://arxiv.org/html/2510.17508v1#S3.E17 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) may improperly become an ill-conditioned form ([24](https://arxiv.org/html/2510.17508v1#S3.E24 "In 3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐱fd,Θ)=1Nfd​∑n=1Nfd‖𝟏𝟎𝟒​∇×𝚿d​N​N​(𝐱nfd)+∇pd​N​N​(𝐱nfd)−𝐟d​(𝐱nfd)‖22≈1Nfd​∑n=1Nfd‖𝟏𝟎𝟒​∇×𝚿d​N​N​(𝐱nfd)−𝐟d​(𝐱nfd)‖22.\displaystyle\begin{aligned} \hskip 0.0pt\mathcal{J}(\mathbf{x}\_{f\_{d}},\Theta)&=\frac{1}{N\_{f\_{d}}}\sum\_{n=1}^{N\_{f\_{d}}}\left\|\mathbf{10^{4}}\nabla\times\mathbf{\Psi}\_{dNN}(\mathbf{x}\_{n}^{f\_{d}})+\nabla p\_{dNN}(\mathbf{x}\_{n}^{f\_{d}})-\mathbf{f}\_{d}(\mathbf{x}\_{n}^{f\_{d}})\right\|\_{2}^{2}\\ &\approx\frac{1}{N\_{f\_{d}}}\sum\_{n=1}^{N\_{f\_{d}}}\left\|\mathbf{10^{4}}\nabla\times\mathbf{\Psi}\_{dNN}(\mathbf{x}\_{n}^{f\_{d}})-\mathbf{f}\_{d}(\mathbf{x}\_{n}^{f\_{d}})\right\|\_{2}^{2}.\end{aligned} |  | (24) |

As a terrible result, ∇pd​N​N\nabla p\_{dNN} neither is trained nor converges to ∇pd\nabla p\_{d} by mistake in Fig. [2](https://arxiv.org/html/2510.17508v1#S3.F2 "Fig. 2 ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). We could infer that the error function of ∇×𝚿d​N​N\nabla\times\mathbf{\Psi}\_{dNN} approaches its minimum point, but the error function of ∇pd​N​N\nabla p\_{dNN} may be very far from that one in value. Finally, we could validate this inference in the following numerical experiments in Section [4.3](https://arxiv.org/html/2510.17508v1#S4.SS3 "4.3 Numerical examples ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").

To deal with these problems, we innovate the Mixed-Form PINNs (MF-PINNs). It is a kind of enhanced PINNs to deal with ill-conditioned loss functions under extreme physical constants. As shown in Fig. [2](https://arxiv.org/html/2510.17508v1#S3.F2 "Fig. 2 ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), our MF-PINNs redesign the coefficients of SV form and combine it with VP form ([21](https://arxiv.org/html/2510.17508v1#S3.E21 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) to get the new total loss functions ([27](https://arxiv.org/html/2510.17508v1#S3.E27 "In 3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥~​(𝐱fs,Θ)=𝒥​(𝐱fs,Θ)m​a​x​(ν,1)+1ν​‖ℒ1​(𝚿s​N​N,𝐟s)‖22+ν​‖ℒ2​(ps​N​N,𝐟s)‖22=𝒥​(𝐱fs,Θ)m​a​x​(ν,1)+1ν​Nfs​∑n=1Nfs‖ν​∇×∇×Δ​𝚿s​N​N​(𝐱nfs)+∇×𝐟s​(𝐱nfs)‖22+νNfs​∑n=1Nfs‖Δ​p𝑠𝑁𝑁​(𝐱nfs)−∇⋅𝐟s​(𝐱nfs)‖22,\displaystyle\begin{aligned} \hskip 0.0pt&\widetilde{\mathcal{J}}(\mathbf{x}\_{f\_{s}},\Theta)=\frac{\mathcal{J}(\mathbf{x}\_{f\_{s}},\Theta)}{max(\nu,1)}+\frac{1}{\nu}\left\|\mathcal{L}\_{1}(\mathbf{\Psi}\_{sNN},\mathbf{f}\_{s})\right\|\_{2}^{2}+\nu\left\|\mathcal{L}\_{2}(p\_{sNN},\mathbf{f}\_{s})\right\|\_{2}^{2}\\ &=\frac{\mathcal{J}(\mathbf{x}\_{f\_{s}},\Theta)}{max(\nu,1)}+\frac{1}{\nu N\_{f\_{s}}}\sum\_{n=1}^{N\_{f\_{s}}}\left\|\nu\nabla\times\nabla\times\Delta\mathbf{\Psi}\_{sNN}(\mathbf{x}\_{n}^{f\_{s}})+\nabla\times\mathbf{f}\_{s}(\mathbf{x}\_{n}^{f\_{s}})\right\|\_{2}^{2}+\frac{\nu}{N\_{f\_{s}}}\sum\_{n=1}^{N\_{f\_{s}}}\left\|{\Delta\mathit{p\_{sNN}(\mathbf{x}\_{n}^{f\_{s}})}}-\nabla\cdot\mathbf{f}\_{s}(\mathbf{x}\_{n}^{f\_{s}})\right\|\_{2}^{2},\end{aligned} |  | (25) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥~​(𝐱fd,Θ)=𝒥​(𝐱fd,Θ)m​a​x​(ν,1)+κν​‖ℒ3​(𝚿d​N​N,𝐟d)‖22+νκ​‖ℒ4​(pd​N​N,𝐟d)‖22=𝒥​(𝐱fd,Θ)m​a​x​(ν,1)+κν​Nfd​∑n=1Nfd‖νκ​∇×∇×𝚿d​N​N​(𝐱nfd)−∇×𝐟d​(𝐱nfd)‖22+νκ​Nfd​∑n=1Nfd‖Δ​pd​N​N​(𝐱nfd)−∇⋅𝐟d​(𝐱nfd)‖22,\displaystyle\begin{aligned} \hskip 0.0pt&\widetilde{\mathcal{J}}(\mathbf{x}\_{f\_{d}},\Theta)=\frac{\mathcal{J}(\mathbf{x}\_{f\_{d}},\Theta)}{max(\nu,1)}+\frac{\kappa}{\nu}\left\|\mathcal{L}\_{3}(\mathbf{\Psi}\_{dNN},\mathbf{f}\_{d})\right\|\_{2}^{2}+\frac{\nu}{\kappa}\left\|\mathcal{L}\_{4}(p\_{dNN},\mathbf{f}\_{d})\right\|\_{2}^{2}\\ &=\frac{\mathcal{J}(\mathbf{x}\_{f\_{d}},\Theta)}{max(\nu,1)}+\frac{\kappa}{\nu N\_{f\_{d}}}\sum\_{n=1}^{N\_{f\_{d}}}\left\|\frac{\nu}{\kappa}\nabla\times\nabla\times\mathbf{\Psi}\_{dNN}(\mathbf{x}\_{n}^{f\_{d}})-\nabla\times\mathbf{f}\_{d}(\mathbf{x}\_{n}^{f\_{d}})\right\|\_{2}^{2}+\frac{\nu}{\kappa N\_{f\_{d}}}\sum\_{n=1}^{N\_{f\_{d}}}\left\|\Delta p\_{dNN}(\mathbf{x}\_{n}^{f\_{d}})-\nabla\cdot\mathbf{f}\_{d}(\mathbf{x}\_{n}^{f\_{d}})\right\|\_{2}^{2},\end{aligned} |  | (26) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥~​(𝐱,Θ)=λfs​𝒥~​(𝐱fs,Θ)+λfd​𝒥~​(𝐱fd,Θ)+λΓ​𝒥​(𝐱Γ,Θ)+λus​𝒥​(𝐱us,Θ)+λud​𝒥​(𝐱ud,Θ),\displaystyle\widetilde{\mathcal{J}}(\mathbf{x},\Theta)=\lambda\_{f\_{s}}\widetilde{\mathcal{J}}(\mathbf{x}\_{f\_{s}},\Theta)+\lambda\_{f\_{d}}\widetilde{\mathcal{J}}(\mathbf{x}\_{f\_{d}},\Theta)+\lambda\_{\Gamma}\mathcal{J}(\mathbf{x}\_{\Gamma},\Theta)+\lambda\_{u\_{s}}\mathcal{J}(\mathbf{x}\_{u\_{s}},\Theta)+\lambda\_{u\_{d}}\mathcal{J}(\mathbf{x}\_{u\_{d}},\Theta), |  | (27) |

where the coefficients 1/ν1/\nu and ν\nu assigned to ℒ1​(𝚿s​N​N,𝐟s)\mathcal{L}\_{1}(\mathbf{\Psi}\_{sNN},\mathbf{f}\_{s}) and ℒ2​(ps​N​N,𝐟s)\mathcal{L}\_{2}(p\_{sNN},\mathbf{f}\_{s}) alleviate the gradient competition between 𝚿s​N​N\mathbf{\Psi}\_{sNN} and ps​N​Np\_{sNN} for ([25](https://arxiv.org/html/2510.17508v1#S3.E25 "In 3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")), the coefficients κ/ν\kappa/\nu and ν/κ\nu/\kappa assigned to ℒ3​(𝚿d​N​N,𝐟d)\mathcal{L}\_{3}(\mathbf{\Psi}\_{dNN},\mathbf{f}\_{d}) and ℒ4​(pd​N​N,𝐟d)\mathcal{L}\_{4}(p\_{dNN},\mathbf{f}\_{d}) alleviate the gradient competition between 𝚿d​N​N\mathbf{\Psi}\_{dNN} and pd​N​Np\_{dNN} for ([26](https://arxiv.org/html/2510.17508v1#S3.E26 "In 3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")), and additionally, we multiply ([21](https://arxiv.org/html/2510.17508v1#S3.E21 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) by the coefficient 1/m​a​x​(ν,1)1/max(\nu,1) to prevent the gradient explosion during backward because ν\nu may be much greater than 11.

As an ideal result, these skills of our MF-PINNs could not only alleviate the gradient competition among different physical quantities, but also accelerate the convergence of PINNs numerical solutions during per epoch. Therefore, our MF-PINNs makes it possible to precisely solve each physical field under extreme physical constants. Next, We would compare the differences between our MF-PINNs and several other PINNs models in Section [3.5](https://arxiv.org/html/2510.17508v1#S3.SS5 "3.5 Algorithm design ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), and verify the effectiveness of our MF-PINNs under extreme physical constants in Section [4](https://arxiv.org/html/2510.17508v1#S4 "4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").

In addition, we could only apply the differential operator to the unmodified loss functions by the automatic differentiation technique. So we have no need to deduce the detailed form [26](https://arxiv.org/html/2510.17508v1#S3.E26 "In 3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") of the decoupled equations in programming.

![Refer to caption](x3.png)


Fig. 3: This picture illustrates the framework of our MF-PINNs for solving coupled Stokes-Darcy Problems.

### 3.3 Activation functions with high-frequency features

PINNs with Fourier features is a way to solve multi-frequency PDE problems. Thus, we improve the activation functions of the first nonlinear layer of NNs for embedding high-frequency features. In detail, we replace ℱ1,n​(𝐰𝐱+b)=𝑡𝑎𝑛ℎ​(θ​(𝐰𝐱+b))\mathcal{F}\_{1,n}\left(\mathbf{w}\mathbf{x}+b\right)=\mathit{tanh}\left(\theta\left(\mathbf{w}\mathbf{x}+b\right)\right) as ℱ~1,n​(𝐰𝐱+b)=𝑡𝑎𝑛ℎ​(𝑠𝑖𝑛​(2​π​θ​(𝐰𝐱+b)/T))\mathcal{\widetilde{F}}\_{1,n}\left(\mathbf{w}\mathbf{x}+b\right)=\mathit{tanh}\left(\mathit{sin}\left(2\pi\theta\left(\mathbf{w}\mathbf{x}+b\right)/\mathit{T}\right)\right) in Fig. [3](https://arxiv.org/html/2510.17508v1#S3.F3 "Fig. 3 ‣ 3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), where the physical periodicity TiT\_{i} can be obtained from the non-homogeneous term 𝐟\mathbf{f} or the boundary conditions 𝐠Γ\mathbf{g}\_{\Gamma}. Then we choose the common multiple of the period TT as the period of the first activation function.

In Section [4](https://arxiv.org/html/2510.17508v1#S4 "4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we would verify that our improvement not only enhances the fitting ability and extension capability of PINNs but also keeps them easy to code and train without consuming additional computing resources.

### 3.4 Optimizer and learning rate decay

In this section, we introduced the combination of optimizers we used, Adam & L-BFGS, and the learning rate decay strategy we design. In the following Section [4.3](https://arxiv.org/html/2510.17508v1#S4.SS3 "4.3 Numerical examples ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we would verify the effect of the learning rate decay strategy we designed.

The Adam optimizer is widely used in deep learning tasks, especially for initial processing of large datasets and complex models. However, results from Adam may not always be sufficiently precise. Hence, we would use Adam optimizer in the early stage of training PINNs (from 1s​t1^{st} to 7000t​h7000^{th} epochs), and we also design the adaptive interval learning rate decay strategy for Adam. We adopt ReduceLROnPlateau and set Initial\_LR\_Adam = 10-3, threshold = 10-4, factor = 10-1, patience = 102, cooldown = 102, while the rest are default.

L-BFGS is a highly efficient quasi-Newton optimization algorithm, and it does well in handling large-scale datasets and high-dimensional parameter spaces. L-BFGS achieves a higher order of convergence, but it requires that the parameter groups be sufficiently close to the optimal points. Therefore, we would use the L-BFGS optimizer in the later stage of training PINNs (from 7001s​t7001^{st} to 10000t​h10000^{th} epochs), and we also design the adaptive interval learning rate decay strategy for L-BFGS. We adopt ReduceLROnPlateau and set Initial\_LR\_L-BFGS = 10-1, threshold = 10-3, factor = 10-1, patience = 10, cooldown = 102, while the rest are default.

### 3.5 Algorithm design

In this section, we list several optimization algorithms. Their performance would be compared in the following numerical examples of Section [4](https://arxiv.org/html/2510.17508v1#S4 "4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"):

* •

  AS-DNN : We use the Deep Neural Networks to fit the Analytical Solutions ([29](https://arxiv.org/html/2510.17508v1#S4.E29 "In 4.3 Numerical examples ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) directly. Therefore, the AS-DNN could display the maximal fitting capability of PINNs in theory. Next, we will use AS-DNN to compare with several PINNs with unsupervised learning in the fixed size of NNs and common input data.
* •

  PINNs : We design the loss functions 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta) directly, without adding any weight. That is λfs=λfd=λud=λud=λΓ=1\lambda\_{f\_{s}}=\lambda\_{f\_{d}}=\lambda\_{u\_{d}}=\lambda\_{u\_{d}}=\lambda\_{\Gamma}=1 for ([21](https://arxiv.org/html/2510.17508v1#S3.E21 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).
* •

  AT-PINNs : We take examples from the Sharp-PINNs [[31](https://arxiv.org/html/2510.17508v1#bib.bibx31)] to alternately train parallel PINNs. In detail, we alternately train different loss functions paired with different region-decomposed NNs, respectively. That is, λfs=λus=λΓ=1,λfd=λud=0\lambda\_{f\_{s}}=\lambda\_{u\_{s}}=\lambda\_{\Gamma}=1,\lambda\_{f\_{d}}=\lambda\_{u\_{d}}=0 for updating argument Θs⫋Θ\Theta\_{s}\subsetneqq\Theta of the Stokes system and λfd=λud=λΓ=1,λfs=λus=0\lambda\_{f\_{d}}=\lambda\_{u\_{d}}=\lambda\_{\Gamma}=1,\lambda\_{f\_{s}}=\lambda\_{u\_{s}}=0 for updating argument Θd⫋Θ\Theta\_{d}\subsetneqq\Theta of the Darcy system in ([21](https://arxiv.org/html/2510.17508v1#S3.E21 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")). What’s more, we change the loss functions (region-decomposed NNs) every 100100 epochs during the Adam training stage. But there is no change during the L-BFGS training stage.
* •

  MW-PINNs [[36](https://arxiv.org/html/2510.17508v1#bib.bibx36)] : We design the 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta) based on their different importance, which could be quantitatively described as appropriate ratios. An appropriate group of Multiple Weights is λfs=λus=1/v,λfd=λud=κ/v,λΓ=1\lambda\_{f\_{s}}=\lambda\_{u\_{s}}=1/v,\lambda\_{f\_{d}}=\lambda\_{u\_{d}}=\kappa/v,\lambda\_{\Gamma}=1 for ([21](https://arxiv.org/html/2510.17508v1#S3.E21 "In 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).
* •

  MF-PINNs (Ours) : We have derived the VP form and SV form of both Stokes and Darcy equations by using the automatic differential operators. Next, we apply multiple weights for the new total loss sfunction 𝒥~​(𝐱,Θ)\widetilde{\mathcal{J}}(\mathbf{x},\Theta) with Mixed Forms. The multiple weights are λus=λud=102,λfd=κ,λfs=λΓ=1\lambda\_{u\_{s}}=\lambda\_{u\_{d}}=10^{2},\lambda\_{f\_{d}}=\kappa,\lambda\_{f\_{s}}=\lambda\_{\Gamma}=1 for ([27](https://arxiv.org/html/2510.17508v1#S3.E27 "In 3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).

## 4 Numerical test

### 4.1 Model parameter

In this section, we list the parameters and size of the NNs for our experiments. Here are some notifications:

1. 1.

   We divide the 127×127127\times 127 square grids with the same size in the Stokes and Darcy domains respectively, and then we input the coordinates of the cell grid nodes as labeled data into the PINNs. We notice that there are 128128 points shared on the interface shared by the Stokes domain and the Darcy domain.
2. 2.

   We use parallel PINNs to solve the coupled Stokes-Darcy equations. Both parallel PINNs have 44 hidden layers × 70\times\,70 neurons. All kinds of PINNs in our article use the same neural networks with the same size. And the strategies for the activation functions are shown in Section [3.3](https://arxiv.org/html/2510.17508v1#S3.SS3 "3.3 Activation functions with high-frequency features ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), unless we have special statements in the following ablation experiments.
3. 3.

   In Table [1](https://arxiv.org/html/2510.17508v1#S4.T1 "Table 1 ‣ 4.1 Model parameter ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we apply the optimizer paired with the adaptive learning rate strategies in Section [3.4](https://arxiv.org/html/2510.17508v1#S3.SS4 "3.4 Optimizer and learning rate decay ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") to the specified number of epochs.
4. 4.

   All the experiments in this article are under the same configuration – CPU:16 vCPU AMD EPYC 9K84 96-Core Processor, GPU: H20-NVLink(96GB).

Table 1: This table lists several significant parameters of the PINNs.

|  |  |  |  |
| --- | --- | --- | --- |
| Data Size | Neurons | Training Optimizer | Activation Function |
| Nf​s=Nf​d=15876N\_{fs}=N\_{fd}=15876 | Input : 2×[2]×[70]2\times[2]\times[70] | Adam for 70007000 epochs |  |
| NΓs=NΓd=380N\_{\Gamma\_{s}}=N\_{\Gamma\_{d}}=380 | Hidden : 2×[70]×[70]×42\times[70]\times[70]\times 4 | Initial LR : 10−310^{-3} | 𝑡𝑎𝑛ℎ​(x)\mathit{tanh(x)} or |
| NΓ=126N\_{\Gamma}=126 | Output : 2×[70]×[2]2\times[70]\times[2]\, (No Bias) | L-BFGS for 30003000 epochs | 𝑡𝑎𝑛ℎ∘𝑠𝑖𝑛​(2​π​xT)\mathit{tanh}\circ\mathit{sin}(\frac{2\pi\mathit{x}}{\mathit{T}}) |
| N=32640N=32640 | Total Parameters : 4046040460 | Initial LR : 10−110^{-1} |  |

### 4.2 Metrics for error

We use the relative Euclidean norm (e​r​r​ℒ2err\mathcal{L}\_{2}) to assess the accuracy of the PINNs. Inspired by the finite volume method, we could replace the continuous equations u​(x)u(x) in the tiny neighborhood as the function value at the paired point u​(xi)u(x\_{i}) to estimate the e​r​r​ℒ2err\mathcal{L}\_{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | e​r​r​ℒ2​(u)=‖uN​N−u‖2‖u‖2≈∑i=1N|uN​N​(xi)−u​(xi)|2∑i=1N|u​(xi)|2,\displaystyle err\mathcal{L}\_{2}\left(u\right)=\frac{\left\|u\_{NN}-u\right\|\_{2}}{\left\|u\right\|\_{2}\,}\approx\frac{\sqrt{\sum\_{i=1}^{N}\left|u\_{NN}(x\_{i})-u(x\_{i})\right|^{2}}}{\sqrt{\sum\_{i=1}^{N}\left|u(x\_{i})\right|^{2}}}, |  | (28) |

where the NN represents the number of points of a specific category in the PINNs training process, the uu represents the analytical solutions, the uN​Nu\_{NN} represents PINNs numerical solutions of specific physical quantities, and the x∈Ωx\in\Omega represents a specific point.

### 4.3 Numerical examples

We focus on the coupled Stokes-Darcy problem with the discontinuous BJS interface, so we use analytical solutions ([29](https://arxiv.org/html/2510.17508v1#S4.E29 "In 4.3 Numerical examples ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")) of [[36](https://arxiv.org/html/2510.17508v1#bib.bibx36)] for different kinds of PINNs. Among them, the non-homogeneous term 𝐟\mathbf{f} and the boundary condition 𝐠Γ\mathbf{g}\_{\Gamma} are naturally determined by the analytical solutions ([29](https://arxiv.org/html/2510.17508v1#S4.E29 "In 4.3 Numerical examples ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐮s=(usvs)=(−sin2⁡(π​x)​sin⁡(π​y)​cos⁡(π​y)sin⁡(π​x)​cos⁡(π​x)​sin2⁡(π​y)),𝐮d=(udvd)=(12​sin⁡(2​π​x)​cos⁡(2​π​y)−12​cos⁡(2​π​x)​sin⁡(2​π​y)),ps=pd=sin⁡(π​x)​cos⁡(π​y),\displaystyle\begin{aligned} \mathbf{u}\_{s}&=\begin{pmatrix}u\_{s}\\ v\_{s}\end{pmatrix}=\begin{pmatrix}-\sin^{2}(\pi x)\sin(\pi y)\cos(\pi y)\\ \sin(\pi x)\cos(\pi x)\sin^{2}(\pi y)\end{pmatrix},\mathbf{u}\_{d}=\begin{pmatrix}u\_{d}\\ v\_{d}\end{pmatrix}=\begin{pmatrix}\frac{1}{2}\sin(2\pi x)\cos(2\pi y)\\ -\frac{1}{2}\cos(2\pi x)\sin(2\pi y)\end{pmatrix},\\ p\_{s}&=p\_{d}=\sin(\pi x)\cos(\pi y),\end{aligned} |  | (29) |

We set that the Stokes domain is Ωs=[0,1]×[0,1]\Omega\_{s}=[0,1]\times[0,1] , while the Darcy domain is Ωd=[0,1]×[−1,0]\Omega\_{d}=[0,1]\times[-1,0]. And we set α=1\alpha=1 and Cp=0C\_{p}=0.
So the period of the velocity fields and pressure fields are T𝐮=1,Tp=2T\_{\mathbf{u}}=1,T\_{p}=2, respectively, as well as the interface is Γ=[0,1]×{0}\Gamma=[0,1]\times\{0\}. Besides, we explore how various combinations of 𝕂​(𝕂=κ​𝕀)\mathbb{K}(\mathbb{K}=\kappa\mathbb{I}) and ν\nu affect the ability of different kinds of PINNs.

### 4.4 Analysis of numerical results

#### 4.4.1 Alleviate the gradient competition

Next we will analyse the numerial results.

Firstly, we analyze the result of several algorithms under 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I} and ν=1\nu=1, because ν/κ≫1\nu/\kappa\gg 1 leads to gradient competition among udu\_{d}, vdv\_{d}, pdp\_{d}, and ν/κ≫ν\nu/\kappa\gg\nu leads to gradient competition between Stokes and Darcy equations in Section [3.5](https://arxiv.org/html/2510.17508v1#S3.SS5 "3.5 Algorithm design ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). We could draw the following conclusions:

![Refer to caption](x4.png)


(a)

![Refer to caption](x5.png)


(b)

![Refer to caption](x6.png)


(c)

![Refer to caption](x7.png)


(d)

Fig. 4: These images (a)-(d) compare the abilities of PINNs and AT-PINNs. The dashed gray line means that we end up using the Adam optimizer and then use the L-BFGS optimizer. By row: PINNs, AT-PINNs; By column: 𝐿𝑜𝑠𝑠\mathit{Loss} , e​r​r​ℒ2err\mathcal{L}\_{2}.

* •

  In Fig. [4](https://arxiv.org/html/2510.17508v1#S4.F4 "Fig. 4 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), we could observe that the gradient update of pdp\_{d} is too tiny, so this fact causes the baseline PINNs to ignore the training of pdp\_{d}, while the training of udu\_{d} and vdv\_{d} is perfect. In other words, the total loss 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta) converges to zero and ud​N​Nu\_{dNN} and vd​N​Nv\_{dNN} converge to udu\_{d} and vdv\_{d}, respectively. Results are e​r​r​ℒ2​(ud)=0.05929%err\mathcal{L}\_{2}(u\_{d})=0.05929\% and e​r​r​ℒ2​(vd)=0.07349%err\mathcal{L}\_{2}(v\_{d})=0.07349\%. But ps​N​Np\_{sNN} and pd​N​Np\_{dNN} do not converge to psp\_{s} and pdp\_{d} at all. Results are e​r​r​ℒ2​(ps)=104.1%err\mathcal{L}\_{2}(p\_{s})=104.1\% and e​r​r​ℒ2​(pd)=135.4%err\mathcal{L}\_{2}(p\_{d})=135.4\%. These results verify our inference of Section [3.2.1](https://arxiv.org/html/2510.17508v1#S3.SS2.SSS1 "3.2.1 Gradient competition and MF-PINNs ‣ 3.2 Physical information drives optimization ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").
* •

  The AT-PINNs aims to decouple the Stokes and Darcy equations. During the early training stage, the regional decomposed PINNs are trained alternately by using different total loss 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta) in Section [3.5](https://arxiv.org/html/2510.17508v1#S3.SS5 "3.5 Algorithm design ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Compared with the baseline PINNs, the AT-PINNs accelerates training by reducing the number of parameters that updates at each epoch, and it saves much time. However, in Fig. [4](https://arxiv.org/html/2510.17508v1#S4.F4 "Fig. 4 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), AT-PINNs may lead to suboptimal outcomes, such as e​r​r​ℒ2​(us)=104.4%,e​r​r​ℒ2​(vs)=153.3%,e​r​r​ℒ2​(ps)=104.9%err\mathcal{L}\_{2}(u\_{s})=104.4\%,err\mathcal{L}\_{2}(v\_{s})=153.3\%,err\mathcal{L}\_{2}(p\_{s})=104.9\% and e​r​r​ℒ2​(pd)=121.6%err\mathcal{L}\_{2}(p\_{d})=121.6\%. This is because Adam must rely on historical gradient data for updating and AT-PINNs does not handle the coupling conditions on the interface.

![Refer to caption](x8.png)


(a)

![Refer to caption](x9.png)


(b)

![Refer to caption](x10.png)


(c)

![Refer to caption](x11.png)


(d)

Fig. 5: These images (a)-(d) compare the abilities of MW-PINNs and our MF-PINNs. The dashed grey line means that we end up using the Adam optimizer and then use the L-BFGS optimizer. By row: MW-PINNs, MF-PINNs; By column: 𝐿𝑜𝑠𝑠\mathit{Loss} , e​r​r​ℒ2err\mathcal{L}\_{2}.

* •

  The MW-PINNS make full use of different weights, 1/κ1/\kappa and ν/κ\nu/\kappa, to assemble the total loss 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta). Compared with the baseline PINNs, the MW-PINNs successfully mitigate the gradient competition between the Stokes and Darcy equations caused by ν/κ≫ν\nu/\kappa\gg\nu. These evidences are e​r​r​ℒ2​(us)=7.819%,e​r​r​ℒ2​(vs)=6.679%,e​r​r​ℒ2​(ud)=0.1832%err\mathcal{L}\_{2}(u\_{s})=7.819\%,err\mathcal{L}\_{2}(v\_{s})=6.679\%,err\mathcal{L}\_{2}(u\_{d})=0.1832\% and e​r​r​ℒ2​(vd)=0.2491%err\mathcal{L}\_{2}(v\_{d})=0.2491\%. However, the gradient competition among udu\_{d}, vdv\_{d} and pdp\_{d} caused by ν/κ≫1\nu/\kappa\gg 1 could not be mitigated. The evidence is that the e​r​r​ℒ2​(pd)err\mathcal{L}\_{2}(p\_{d}) does not decrease in the early training stage of L-BFGS, and pd​N​Np\_{dNN} does not converge to the pdp\_{d} finally in Fig. [5](https://arxiv.org/html/2510.17508v1#S4.F5 "Fig. 5 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Results are
  e​r​r​ℒ2​(ps)=91.52%err\mathcal{L}\_{2}(p\_{s})=91.52\% and e​r​r​ℒ2​(pd)=151.6%err\mathcal{L}\_{2}(p\_{d})=151.6\%.
* •

  Compared with the MW-PINNs, our MF-PINNs mitigates the gradient competition among udu\_{d}, vdv\_{d} and pdp\_{d} caused by ν/κ≫1\nu/\kappa\gg 1 and between the Stokes and Darcy equations caused by ν/κ≫v\nu/\kappa\gg v as is shown in Fig. [5](https://arxiv.org/html/2510.17508v1#S4.F5 "Fig. 5 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Results are e​r​r​ℒ2​(us)=0.4324%,e​r​r​ℒ2​(vs)=0.5342%,e​r​r​ℒ2​(ps)=4.789%,e​r​r​ℒ2​(ud)=0.04768%,e​r​r​ℒ2​(vd)=0.04825%err\mathcal{L}\_{2}(u\_{s})=0.4324\%,err\mathcal{L}\_{2}(v\_{s})=0.5342\%,err\mathcal{L}\_{2}(p\_{s})=4.789\%,err\mathcal{L}\_{2}(u\_{d})=0.04768\%,err\mathcal{L}\_{2}(v\_{d})=0.04825\% and e​r​r​ℒ2​(pd)=13.91%err\mathcal{L}\_{2}(p\_{d})=13.91\%. Our Fig. [6](https://arxiv.org/html/2510.17508v1#S4.F6 "Fig. 6 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") and Fig. [7](https://arxiv.org/html/2510.17508v1#S4.F7 "Fig. 7 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") show the prediction, truth and error of all the physical fields. These images show the advantages of our MF-PINNs for all the physical fields under extreme κ=10−4\kappa=10^{-4} and ν=1\nu=1. Additionally, Fig. [8](https://arxiv.org/html/2510.17508v1#S4.F8 "Fig. 8 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") shows the interface of all the physical fields between the Stokes and Darcy domains, and they validate the ability of our MF-PINNs to handle coupled systems.

![Refer to caption](x12.png)


(a)

![Refer to caption](x13.png)


(b)

![Refer to caption](x14.png)


(c)

![Refer to caption](x15.png)


(d)

![Refer to caption](x16.png)


(e)

![Refer to caption](x17.png)


(f)

Fig. 6: These images (a)-(f) show the ability of our MF-PINNs to predict the velocity fields of the coupled Stokes-Darcy equations, under 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I} and ν=1\nu=1. In these images, the colorful lines stand for the streamlines, the arrows stand for the direction of velocity, and the colorbars stand for the value of velocity. By row: Stokes domain, Darcy domain; By column: MF-PINNs numerical solutions, analytical solutions, absolute error.



![Refer to caption](x18.png)


(a)

![Refer to caption](x19.png)


(b)

![Refer to caption](x20.png)


(c)

![Refer to caption](x21.png)


(d)

![Refer to caption](x22.png)


(e)

![Refer to caption](x23.png)


(f)

Fig. 7: These images (a)-(f) show the ability of our MF-PINNs to predict the pressure fields of the coupled Stokes-Darcy equations, under 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I} and ν=1\nu=1. By row: Stokes domain, Darcy domain; By column: MF-PINNs numerical solutions, analytical solutions, absolute error.



![Refer to caption](x24.png)


(a)

![Refer to caption](x25.png)


(b)

![Refer to caption](x26.png)


(c)

![Refer to caption](x27.png)


(d)

![Refer to caption](x28.png)


(e)

![Refer to caption](x29.png)


(f)

Fig. 8: These images (a)-(f) show the absolute error between our MF-PINNs numerical solutions and analytical solutions in the interface, under 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I} and ν=1\nu=1. We notice that the constant becomes 2π\frac{2}{\pi} in ([4](https://arxiv.org/html/2510.17508v1#S2.E4 "In 2.2 The velocity-pressure form of the Stokes-Darcy system ‣ 2 Physical modeling ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)")).
By row: Stokes domain, Darcy domain; By column: x direction of velocity field, y direction of velocity field, pressure field.

Secondly, we consider the performance of MF-PINNs in Table [2](https://arxiv.org/html/2510.17508v1#S4.T2 "Table 2 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") under 𝕂=κ​𝕀,κ⩽1\mathbb{K}=\kappa\mathbb{I},\kappa\leqslant 1 and ν⩽1\nu\leqslant 1. We could therefore make the following deductions:

1. 1.

   Our MF-PINNs could effectively train the velocity fields under extreme cases, like the group κ=1,ν=10−4\kappa=1,\nu=10^{-4}. Similarly, our MF-PINNs could effectively train the pressure fields under the group κ=10−4,ν=1\kappa=10^{-4},\nu=1. On the opposite side, neither baseline PINNs, MW-PINNs, nor AT-PINNs could not alleviate the problem of gradient competition of velocity fields and pressure fields, even though MW-PINNs could balance the training of physical fields between the Stokes and Darcy domains better than baseline PINNs.
2. 2.

   Compared with other PINNs models, our MF-PINNs could also handle the gradient competition of each physical field effectively, in other extreme cases, like the group κ=10−2,ν=1\kappa=10^{-2},\nu=1, the group κ=1,ν=10−2\kappa=1,\nu=10^{-2}, the group κ=10−4,ν=10−2\kappa=10^{-4},\nu=10^{-2} and the group κ=10−2,ν=10−4\kappa=10^{-2},\nu=10^{-4}.
3. 3.

   However, compared with the MW-PINNs, the performance of our MF-PINNs seems not ideal under the group κ=10−4,ν=10−4\kappa=10^{-4},\nu=10^{-4}. Therefore, we hope to find several more reasonable combinations of coefficients for the new total loss 𝒥~​(𝐱,Θ)\widetilde{\mathcal{J}}(\mathbf{x},\Theta).
4. 4.

   The performances of baseline PINNs and MW-PINNs are very similar under common cases, like the group κ=1,ν=1\kappa=1,\nu=1 and the group κ=10−2,ν=10−2\kappa=10^{-2},\nu=10^{-2}. Our MF-PINNs performs better, but it requires much more time.
5. 5.

   Besides, AT-PINNs does save a lot of time, but the performance of AT-PINNs is clearly inferior to that of baseline PINNs under most groups of 𝕂=κ​𝕀,κ⩽1\mathbb{K}=\kappa\mathbb{I},\kappa\leqslant 1 and ν⩽1\nu\leqslant 1.
6. 6.

   Among these several kinds of PINNs, the errors of MW-PINNs and our MF-PINNs are closer to that of AS-DNN. This fact reflects that our MF-PINNs is closer to the maximum fitting ability of NN under the size of data and most groups of 𝕂=κ​𝕀,κ⩽1\mathbb{K}=\kappa\mathbb{I},\kappa\leqslant 1 and ν⩽1\nu\leqslant 1.

Table 2: 
This table lists the performance of different kinds of PINNs under different combinations of 𝕂\mathbb{K} and ν\nu values ( 𝕂=κ​𝕀,κ⩽1\mathbb{K}=\kappa\mathbb{I},\kappa\leqslant 1 and ν⩽1\nu\leqslant 1 ).

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Arguments | Algorithm | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐬)\mathbf{err\mathcal{L}\_{2}\left(u\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐬)\mathbf{err\mathcal{L}\_{2}\left(v\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐬)\mathbf{err\mathcal{L}\_{2}\left(p\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐝)\mathbf{err\mathcal{L}\_{2}\left(u\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐝)\mathbf{err\mathcal{L}\_{2}\left(v\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐝)\mathbf{err\mathcal{L}\_{2}\left(p\_{d}\right)} | Time |
| NULL | AS-DNN | 6.179×10−36.179\times 10^{-3} | 6.479×10−36.479\times 10^{-3} | 2.855×10−32.855\times 10^{-3} | 5.251×10−35.251\times 10^{-3} | 5.063×10−35.063\times 10^{-3} | 3.432×10−33.432\times 10^{-3} | 602s |
|  | PINNs | 1.012×1001.012\times 10^{0} | 9.191×10−19.191\times 10^{-1} | 3.486×10−4¯\underline{3.486\times 10^{-4}} | 1.009×100¯\underline{1.009\times 10^{0}} | 1.009×100¯\underline{1.009\times 10^{0}} | 2.946×10−4¯\underline{2.946\times 10^{-4}} | 1177s |
| κ=1\kappa=1 | AT-PINNs | 1.318×1001.318\times 10^{0} | 1.066×1001.066\times 10^{0} | 4.974×10−44.974\times 10^{-4} | 1.081×1001.081\times 10^{0} | 1.045×1001.045\times 10^{0} | 6.130×10−36.130\times 10^{-3} | 1161s |
| ν=10−4\nu=10^{-4} | MW-PINNs | 1.187×10−1¯\underline{1.187\times 10^{-1}} | 1.119×10−1¯\underline{1.119\times 10^{-1}} | 6.542×10−46.542\times 10^{-4} | 1.073×1001.073\times 10^{0} | 1.085×1001.085\times 10^{0} | 6.564×10−46.564\times 10^{-4} | 1948s |
|  | MF-PINNs ↑\uparrow | 1.096×𝟏𝟎−𝟐\mathbf{1.096\times 10^{-2}} | 1.513×𝟏𝟎−𝟐\mathbf{1.513\times 10^{-2}} | 1.935×𝟏𝟎−𝟒\mathbf{1.935\times 10^{-4}} | 8.094×𝟏𝟎−𝟐\mathbf{8.094\times 10^{-2}} | 6.349×𝟏𝟎−𝟐\mathbf{6.349\times 10^{-2}} | 2.101×𝟏𝟎−𝟒\mathbf{2.101\times 10^{-4}} | 2505s |
|  | PINNs | 2.001×10−12.001\times 10^{-1} | 1.974×10−11.974\times 10^{-1} | 1.041×1001.041\times 10^{0} | 5.929×10−4¯\underline{5.929\times 10^{-4}} | 7.349×10−4¯\underline{7.349\times 10^{-4}} | 1.354×1001.354\times 10^{0} | 2161s |
| κ=10−4\kappa=10^{-4} | AT-PINNs | 1.044×1001.044\times 10^{0} | 1.533×1001.533\times 10^{0} | 1.049×1001.049\times 10^{0} | 6.862×10−16.862\times 10^{-1} | 7.032×10−17.032\times 10^{-1} | 1.216×100¯\underline{1.216\times 10^{0}} | 918s |
| ν=1\nu=1 | MW-PINNs | 7.819×10−2¯\underline{7.819\times 10^{-2}} | 6.679×10−2¯\underline{6.679\times 10^{-2}} | 9.152×10−1¯\underline{9.152\times 10^{-1}} | 1.832×10−31.832\times 10^{-3} | 2.491×10−32.491\times 10^{-3} | 1.516×1001.516\times 10^{0} | 2294s |
|  | MF-PINNs ↑\uparrow | 4.324×𝟏𝟎−𝟑\mathbf{4.324\times 10^{-3}} | 5.342×𝟏𝟎−𝟑\mathbf{5.342\times 10^{-3}} | 4.789×𝟏𝟎−𝟐\mathbf{4.789\times 10^{-2}} | 4.768×𝟏𝟎−𝟒\mathbf{4.768\times 10^{-4}} | 4.825×𝟏𝟎−𝟒\mathbf{4.825\times 10^{-4}} | 1.393×𝟏𝟎−𝟏\mathbf{1.393\times 10^{-1}} | 3174s |
|  | PINNs | 1.475×10−2¯\underline{1.475\times 10^{-2}} | 2.036×10−2¯\underline{2.036\times 10^{-2}} | 7.736×10−4¯\underline{7.736\times 10^{-4}} | 9.943×10−19.943\times 10^{-1} | 9.944×10−19.944\times 10^{-1} | 3.217×10−43.217\times 10^{-4} | 1216s |
| κ=1\kappa=1 | AT-PINNs | 1.543×10−11.543\times 10^{-1} | 1.908×10−11.908\times 10^{-1} | 5.487×10−35.487\times 10^{-3} | 1.001×1001.001\times 10^{0} | 1.008×1001.008\times 10^{0} | 1.063×10−21.063\times 10^{-2} | 1141s |
| ν=10−2\nu=10^{-2} | MW-PINNs | 2.407×10−22.407\times 10^{-2} | 2.887×10−22.887\times 10^{-2} | 1.438×10−31.438\times 10^{-3} | 9.704×10−1¯\underline{9.704\times 10^{-1}} | 9.634×10−1¯\underline{9.634\times 10^{-1}} | 2.192×𝟏𝟎−𝟒\mathbf{2.192\times 10^{-4}} | 1322s |
|  | MF-PINNs ↑\uparrow | 1.324×𝟏𝟎−𝟐\mathbf{1.324\times 10^{-2}} | 1.878×𝟏𝟎−𝟐\mathbf{1.878\times 10^{-2}} | 6.918×𝟏𝟎−𝟒\mathbf{6.918\times 10^{-4}} | 1.430×𝟏𝟎−𝟐\mathbf{1.430\times 10^{-2}} | 1.418×𝟏𝟎−𝟐\mathbf{1.418\times 10^{-2}} | 2.343×10−4¯\underline{2.343\times 10^{-4}} | 2588s |
|  | PINNs | 4.832×10−24.832\times 10^{-2} | 3.718×10−23.718\times 10^{-2} | 6.949×10−16.949\times 10^{-1} | 1.587×10−21.587\times 10^{-2} | 5.930×10−25.930\times 10^{-2} | 1.115×1001.115\times 10^{0} | 2498s |
| κ=10−2\kappa=10^{-2} | AT-PINNs | 1.187×10−11.187\times 10^{-1} | 2.764×10−12.764\times 10^{-1} | 8.793×10−18.793\times 10^{-1} | 5.022×10−15.022\times 10^{-1} | 4.878×10−14.878\times 10^{-1} | 1.127×1001.127\times 10^{0} | 1014s |
| ν=1\nu=1 | MW-PINNs | 2.544×10−2¯\underline{2.544\times 10^{-2}} | 2.474×10−2¯\underline{2.474\times 10^{-2}} | 3.713×10−1¯\underline{3.713\times 10^{-1}} | 1.167×10−2¯\underline{1.167\times 10^{-2}} | 2.743×10−2¯\underline{2.743\times 10^{-2}} | 5.375×10−1¯\underline{5.375\times 10^{-1}} | 1347s |
|  | MF-PINNs ↑\uparrow | 7.157×𝟏𝟎−𝟑\mathbf{7.157\times 10^{-3}} | 7.467×𝟏𝟎−𝟑\mathbf{7.467\times 10^{-3}} | 1.356×𝟏𝟎−𝟏\mathbf{1.356\times 10^{-1}} | 2.905×𝟏𝟎−𝟑\mathbf{2.905\times 10^{-3}} | 5.332×𝟏𝟎−𝟑\mathbf{5.332\times 10^{-3}} | 1.633×𝟏𝟎−𝟏\mathbf{1.633\times 10^{-1}} | 3077s |
|  | PINNs | 1.974×10−11.974\times 10^{-1} | 1.984×10−11.984\times 10^{-1} | 1.636×10−11.636\times 10^{-1} | 1.290×10−21.290\times 10^{-2} | 1.475×10−21.475\times 10^{-2} | 3.103×10−13.103\times 10^{-1} | 2191s |
| κ=10−4\kappa=10^{-4} | AT-PINNs | 6.896×10−16.896\times 10^{-1} | 9.729×10−19.729\times 10^{-1} | 1.312×10−11.312\times 10^{-1} | 1.601×10−11.601\times 10^{-1} | 1.678×10−11.678\times 10^{-1} | 6.870×10−16.870\times 10^{-1} | 1283s |
| ν=10−2\nu=10^{-2} | MW-PINNs | 2.229×10−2¯\underline{2.229\times 10^{-2}} | 2.405×10−2¯\underline{2.405\times 10^{-2}} | 1.267×10−1¯\underline{1.267\times 10^{-1}} | 7.705×𝟏𝟎−𝟑\mathbf{7.705\times 10^{-3}} | 1.197×10−2¯\underline{1.197\times 10^{-2}} | 2.178×10−1¯\underline{2.178\times 10^{-1}} | 1712s |
|  | MF-PINNs ↑\uparrow | 7.766×𝟏𝟎−𝟑\mathbf{7.766\times 10^{-3}} | 1.219×𝟏𝟎−𝟐\mathbf{1.219\times 10^{-2}} | 8.323×𝟏𝟎−𝟐\mathbf{8.323\times 10^{-2}} | 8.133×10−3¯\underline{8.133\times 10^{-3}} | 8.496×𝟏𝟎−𝟑\mathbf{8.496\times 10^{-3}} | 1.425×𝟏𝟎−𝟏\mathbf{1.425\times 10^{-1}} | 2373s |
|  | PINNs | 1.140×1001.140\times 10^{0} | 1.064×1001.064\times 10^{0} | 3.098×10−4¯\underline{3.098\times 10^{-4}} | 1.012×1001.012\times 10^{0} | 1.016×1001.016\times 10^{0} | 2.902×𝟏𝟎−𝟒\mathbf{2.902\times 10^{-4}} | 1172s |
| κ=10−2\kappa=10^{-2} | AT-PINNs | 1.477×1001.477\times 10^{0} | 1.319×1001.319\times 10^{0} | 6.653×10−46.653\times 10^{-4} | 1.024×1001.024\times 10^{0} | 1.022×1001.022\times 10^{0} | 7.349×10−37.349\times 10^{-3} | 1187s |
| ν=10−4\nu=10^{-4} | MW-PINNs | 6.285×10−2¯\underline{6.285\times 10^{-2}} | 9.743×10−2¯\underline{9.743\times 10^{-2}} | 3.850×10−43.850\times 10^{-4} | 9.711×10−1¯\underline{9.711\times 10^{-1}} | 9.658×10−1¯\underline{9.658\times 10^{-1}} | 4.748×10−4¯\underline{4.748\times 10^{-4}} | 1988s |
|  | MF-PINNs ↑\uparrow | 5.531×𝟏𝟎−𝟑\mathbf{5.531\times 10^{-3}} | 7.903×𝟏𝟎−𝟑\mathbf{7.903\times 10^{-3}} | 2.608×𝟏𝟎−𝟒\mathbf{2.608\times 10^{-4}} | 1.082×𝟏𝟎−𝟏\mathbf{1.082\times 10^{-1}} | 1.106×𝟏𝟎−𝟏\mathbf{1.106\times 10^{-1}} | 2.491×10−32.491\times 10^{-3} | 2519s |
|  | PINNs | 1.034×1001.034\times 10^{0} | 1.033×1001.033\times 10^{0} | 1.170×𝟏𝟎−𝟑\mathbf{1.170\times 10^{-3}} | 1.919×𝟏𝟎−𝟐\mathbf{1.919\times 10^{-2}} | 1.578×𝟏𝟎−𝟐\mathbf{1.578\times 10^{-2}} | 1.063×𝟏𝟎−𝟑\mathbf{1.063\times 10^{-3}} | 1434s |
| κ=10−4\kappa=10^{-4} | AT-PINNs | 1.007×1001.007\times 10^{0} | 1.084×1001.084\times 10^{0} | 4.226×10−34.226\times 10^{-3} | 2.147×10−12.147\times 10^{-1} | 2.141×10−12.141\times 10^{-1} | 1.189×10−21.189\times 10^{-2} | 1147s |
| ν=10−4\nu=10^{-4} | MW-PINNs ↑\uparrow | 8.132×10−2¯\underline{8.132\times 10^{-2}} | 1.949×10−1¯\underline{1.949\times 10^{-1}} | 3.466×10−3¯\underline{3.466\times 10^{-3}} | 7.448×10−2¯\underline{7.448\times 10^{-2}} | 7.802×10−2¯\underline{7.802\times 10^{-2}} | 9.472×10−3¯\underline{9.472\times 10^{-3}} | 1885s |
|  | MF-PINNs | 1.706×𝟏𝟎−𝟐\mathbf{1.706\times 10^{-2}} | 2.491×𝟏𝟎−𝟐\mathbf{2.491\times 10^{-2}} | 2.063×10−22.063\times 10^{-2} | 4.968×10−14.968\times 10^{-1} | 5.293×10−15.293\times 10^{-1} | 7.171×10−27.171\times 10^{-2} | 2698s |
|  | PINNs ↑\uparrow | 4.067×10−3¯\underline{4.067\times 10^{-3}} | 4.663×10−3¯\underline{4.663\times 10^{-3}} | 5.480×𝟏𝟎−𝟒\mathbf{5.480\times 10^{-4}} | 5.531×10−3¯\underline{5.531\times 10^{-3}} | 6.937×10−3¯\underline{6.937\times 10^{-3}} | 2.785×𝟏𝟎−𝟒\mathbf{2.785\times 10^{-4}} | 1206s |
| κ=10−2\kappa=10^{-2} | AT-PINNs | 1.521×10−11.521\times 10^{-1} | 2.441×10−12.441\times 10^{-1} | 1.436×10−21.436\times 10^{-2} | 8.583×10−18.583\times 10^{-1} | 8.000×10−18.000\times 10^{-1} | 2.668×10−22.668\times 10^{-2} | 1220s |
| ν=10−2\nu=10^{-2} | MW-PINNs | 1.295×10−21.295\times 10^{-2} | 1.169×10−21.169\times 10^{-2} | 9.049×10−4¯\underline{9.049\times 10^{-4}} | 1.422×10−21.422\times 10^{-2} | 8.422×10−38.422\times 10^{-3} | 4.918×10−4¯\underline{4.918\times 10^{-4}} | 1339s |
|  | MF-PINNs | 1.720×𝟏𝟎−𝟑\mathbf{1.720\times 10^{-3}} | 2.579×𝟏𝟎−𝟑\mathbf{2.579\times 10^{-3}} | 1.110×10−31.110\times 10^{-3} | 5.286×𝟏𝟎−𝟑\mathbf{5.286\times 10^{-3}} | 5.136×𝟏𝟎−𝟑\mathbf{5.136\times 10^{-3}} | 3.200×10−33.200\times 10^{-3} | 2589s |
|  | PINNs | 2.283×10−22.283\times 10^{-2} | 2.172×10−2¯\underline{2.172\times 10^{-2}} | 1.073×10−11.073\times 10^{-1} | 7.982×10−3¯\underline{7.982\times 10^{-3}} | 8.275×10−3¯\underline{8.275\times 10^{-3}} | 2.437×10−22.437\times 10^{-2} | 1320s |
| κ=1\kappa=1 | AT-PINNs | 3.108×10−23.108\times 10^{-2} | 8.320×10−28.320\times 10^{-2} | 1.946×10−11.946\times 10^{-1} | 9.185×10−19.185\times 10^{-1} | 8.696×10−18.696\times 10^{-1} | 8.420×10−28.420\times 10^{-2} | 1199s |
| ν=1\nu=1 | MW-PINNs | 2.006×10−2¯\underline{2.006\times 10^{-2}} | 2.291×10−22.291\times 10^{-2} | 1.061×10−1¯\underline{1.061\times 10^{-1}} | 1.074×10−21.074\times 10^{-2} | 9.551×10−39.551\times 10^{-3} | 1.015×10−2¯\underline{1.015\times 10^{-2}} | 1326s |
|  | MF-PINNs ↑\uparrow | 3.181×𝟏𝟎−𝟑\mathbf{3.181\times 10^{-3}} | 2.764×𝟏𝟎−𝟑\mathbf{2.764\times 10^{-3}} | 1.725×𝟏𝟎−𝟐\mathbf{1.725\times 10^{-2}} | 4.606×𝟏𝟎−𝟑\mathbf{4.606\times 10^{-3}} | 4.361×𝟏𝟎−𝟑\mathbf{4.361\times 10^{-3}} | 3.805×𝟏𝟎−𝟑\mathbf{3.805\times 10^{-3}} | 3168s |

The bold marks the lowest error of each physical quantity in each arguments group, while the underline marks the second-lowest error of each physical quantity in each arguments group. The upward arrows ↑\uparrow mark the relatively best methods under the same parameters.

Thirdly, we consider the performance of MF-PINNs in Table [3](https://arxiv.org/html/2510.17508v1#S4.T3 "Table 3 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") under the groups 𝕂=κ​𝕀,κ⩾1\mathbb{K}=\kappa\mathbb{I},\kappa\geqslant 1 and ν⩾1\nu\geqslant 1. Consequently, we could draw the following conclusions:

1. 1.

   Our MF-PINNs could effectively train the velocity fields under extreme cases, like the group κ=1,ν=104\kappa=1,\nu=10^{4}. Similarly, our MF-PINNs could effectively train the pressure fields under group κ=104,ν=1\kappa=10^{4},\nu=1. On the opposite side, it seems that MW-PINNs has few improvements compared to baseline PINNs. What’s worse, neither the baseline PINNs, MW-PINNs nor AT-PINNs could not alleviate the problem of gradient competition.
2. 2.

   Compared with other PINNs models, our MF-PINNs could also handle the gradient competition of each physical field effectively, under other complex cases, like the group κ=102,ν=1\kappa=10^{2},\nu=1, the group κ=1,ν=102\kappa=1,\nu=10^{2}, the group κ=104,ν=102\kappa=10^{4},\nu=10^{2} and the group κ=102,ν=104\kappa=10^{2},\nu=10^{4}.
3. 3.

   Our MF-PINNs performs better than MW-PINNs, while MW-PINNs performs better than baseline PINNs under the group κ=104,ν=104\kappa=10^{4},\nu=10^{4} and the group κ=102,ν=102\kappa=10^{2},\nu=10^{2}.
4. 4.

   In the cases of the group κ=104,ν=104\kappa=10^{4},\nu=10^{4} and group κ=102,ν=102\kappa=10^{2},\nu=10^{2}, the performance of our MF-PINNs is better than that of MW-PINNs. And in the cases of the group κ=1,ν=1\kappa=1,\nu=1, the performance of MW-PINNs is like that of baseline PINNs.
5. 5.

   Besides, AT-PINNs is quick to stop training, but the results of AT-PINNs are not as good as the baseline PINNs obviously under the group 𝕂=κ​𝕀,κ⩾1\mathbb{K}=\kappa\mathbb{I},\kappa\geqslant 1 and the group ν⩾1\nu\geqslant 1.
6. 6.

   Among these several kinds of PINNs, the errors of MW-PINNs and our MF-PINNs are closer to that of AS-DNN. This fact reflects that our MF-PINNs is closer to the maximum fitting ability of NN under the size of data and most groups 𝕂=κ​𝕀,κ⩾1\mathbb{K}=\kappa\mathbb{I},\kappa\geqslant 1 and ν⩾1\nu\geqslant 1.

Table 3: 
This table lists the performance of different kinds of PINNs under different combinations of 𝕂\mathbb{K} and ν\nu values ( 𝕂=κ​𝕀,κ⩾1\mathbb{K}=\kappa\mathbb{I},\kappa\geqslant 1 and ν⩾1\nu\geqslant 1 ).

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Arguments | Algorithm | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐬)\mathbf{err\mathcal{L}\_{2}\left(u\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐬)\mathbf{err\mathcal{L}\_{2}\left(v\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐬)\mathbf{err\mathcal{L}\_{2}\left(p\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐝)\mathbf{err\mathcal{L}\_{2}\left(u\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐝)\mathbf{err\mathcal{L}\_{2}\left(v\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐝)\mathbf{err\mathcal{L}\_{2}\left(p\_{d}\right)} | Time |
| NULL | AS-DNN | 5.441×10−35.441\times 10^{-3} | 6.615×10−36.615\times 10^{-3} | 4.039×10−34.039\times 10^{-3} | 4.736×10−34.736\times 10^{-3} | 4.576×10−34.576\times 10^{-3} | 2.921×10−32.921\times 10^{-3} | 611s |
|  | PINNs | 8.506×10−18.506\times 10^{-1} | 8.465×10−18.465\times 10^{-1} | 4.544×1004.544\times 10^{0} | 3.615×10−2¯\underline{3.615\times 10^{-2}} | 3.317×10−2¯\underline{3.317\times 10^{-2}} | 4.385×1004.385\times 10^{0} | 2671s |
| κ=1\kappa=1 | AT-PINNs | 1.546×1001.546\times 10^{0} | 1.275×1001.275\times 10^{0} | 5.273×1005.273\times 10^{0} | 1.881×10−11.881\times 10^{-1} | 2.014×10−12.014\times 10^{-1} | 5.498×1005.498\times 10^{0} | 1820s |
| ν=104\nu=10^{4} | MW-PINNs | 3.252×10−1¯\underline{3.252\times 10^{-1}} | 5.312×10−1¯\underline{5.312\times 10^{-1}} | 2.262×100¯\underline{2.262\times 10^{0}} | 1.165×10−11.165\times 10^{-1} | 5.557×10−25.557\times 10^{-2} | 1.803×100¯\underline{1.803\times 10^{0}} | 3806s |
|  | MF-PINNs ↑\uparrow | 2.336×𝟏𝟎−𝟏\mathbf{2.336\times 10^{-1}} | 3.984×𝟏𝟎−𝟏\mathbf{3.984\times 10^{-1}} | 6.628×𝟏𝟎−𝟏\mathbf{6.628\times 10^{-1}} | 1.686×𝟏𝟎−𝟐\mathbf{1.686\times 10^{-2}} | 1.702×𝟏𝟎−𝟐\mathbf{1.702\times 10^{-2}} | 2.950×𝟏𝟎−𝟏\mathbf{2.950\times 10^{-1}} | 4387s |
|  | PINNs | 2.438×10−2¯\underline{2.438\times 10^{-2}} | 2.837×10−2¯\underline{2.837\times 10^{-2}} | 1.230×10−1¯\underline{1.230\times 10^{-1}} | 1.006×1001.006\times 10^{0} | 1.008×1001.008\times 10^{0} | 4.523×10−2¯\underline{4.523\times 10^{-2}} | 1422s |
| κ=104\kappa=10^{4} | AT-PINNs | 5.280×10−25.280\times 10^{-2} | 1.611×10−11.611\times 10^{-1} | 2.974×10−12.974\times 10^{-1} | 1.022×1001.022\times 10^{0} | 1.024×10−1¯\underline{1.024\times 10^{-1}} | 2.209×10−12.209\times 10^{-1} | 1263s |
| ν=1\nu=1 | MW-PINNs | 4.604×10−24.604\times 10^{-2} | 7.590×10−27.590\times 10^{-2} | 2.603×10−12.603\times 10^{-1} | 1.003×100¯\underline{1.003\times 10^{0}} | 1.012×1001.012\times 10^{0} | 7.821×10−27.821\times 10^{-2} | 1726s |
|  | MF-PINNs ↑\uparrow | 2.814×𝟏𝟎−𝟑\mathbf{2.814\times 10^{-3}} | 2.205×𝟏𝟎−𝟑\mathbf{2.205\times 10^{-3}} | 1.433×𝟏𝟎−𝟐\mathbf{1.433\times 10^{-2}} | 6.335×𝟏𝟎−𝟑\mathbf{6.335\times 10^{-3}} | 6.114×𝟏𝟎−𝟑\mathbf{6.114\times 10^{-3}} | 5.755×𝟏𝟎−𝟒\mathbf{5.755\times 10^{-4}} | 3821s |
|  | PINNs | 3.235×10−13.235\times 10^{-1} | 4.478×10−14.478\times 10^{-1} | 3.944×1003.944\times 10^{0} | 7.348×10−27.348\times 10^{-2} | 5.276×10−2¯\underline{5.276\times 10^{-2}} | 2.985×1002.985\times 10^{0} | 2695s |
| κ=1\kappa=1 | AT-PINNs | 3.406×10−13.406\times 10^{-1} | 8.945×10−18.945\times 10^{-1} | 2.954×1002.954\times 10^{0} | 8.897×10−18.897\times 10^{-1} | 6.241×10−16.241\times 10^{-1} | 1.451×1011.451\times 10^{1} | 1871s |
| ν=102\nu=10^{2} | MW-PINNs | 7.680×10−2¯\underline{7.680\times 10^{-2}} | 7.207×10−2¯\underline{7.207\times 10^{-2}} | 1.621×100¯\underline{1.621\times 10^{0}} | 7.186×10−2¯\underline{7.186\times 10^{-2}} | 1.047×10−11.047\times 10^{-1} | 2.315×100¯\underline{2.315\times 10^{0}} | 2508s |
|  | MF-PINNs ↑\uparrow | 1.500×𝟏𝟎−𝟐\mathbf{1.500\times 10^{-2}} | 1.123×𝟏𝟎−𝟐\mathbf{1.123\times 10^{-2}} | 8.136×𝟏𝟎−𝟏\mathbf{8.136\times 10^{-1}} | 6.666×𝟏𝟎−𝟑\mathbf{6.666\times 10^{-3}} | 6.114×𝟏𝟎−𝟑\mathbf{6.114\times 10^{-3}} | 7.706×𝟏𝟎−𝟏\mathbf{7.706\times 10^{-1}} | 5637s |
|  | PINNs | 2.688×10−2¯\underline{2.688\times 10^{-2}} | 2.561×10−2¯\underline{2.561\times 10^{-2}} | 1.331×10−1¯\underline{1.331\times 10^{-1}} | 9.958×10−19.958\times 10^{-1} | 9.982×10−19.982\times 10^{-1} | 3.174×10−23.174\times 10^{-2} | 1368s |
| κ=102\kappa=10^{2} | AT-PINNs | 5.010×10−25.010\times 10^{-2} | 1.061×10−11.061\times 10^{-1} | 2.061×10−12.061\times 10^{-1} | 1.012×1001.012\times 10^{0} | 1.024×1001.024\times 10^{0} | 8.993×10−28.993\times 10^{-2} | 1205s |
| ν=1\nu=1 | MW-PINNs | 3.121×10−23.121\times 10^{-2} | 2.564×10−22.564\times 10^{-2} | 1.447×10−11.447\times 10^{-1} | 9.306×10−1¯\underline{9.306\times 10^{-1}} | 9.325×10−1¯\underline{9.325\times 10^{-1}} | 2.012×10−2¯\underline{2.012\times 10^{-2}} | 1440s |
|  | MF-PINNs ↑\uparrow | 4.673×𝟏𝟎−𝟑\mathbf{4.673\times 10^{-3}} | 6.455×𝟏𝟎−𝟑\mathbf{6.455\times 10^{-3}} | 2.765×𝟏𝟎−𝟐\mathbf{2.765\times 10^{-2}} | 2.337×𝟏𝟎−𝟑\mathbf{2.337\times 10^{-3}} | 2.512×𝟏𝟎−𝟑\mathbf{2.512\times 10^{-3}} | 1.268×𝟏𝟎−𝟐\mathbf{1.268\times 10^{-2}} | 3500s |
|  | PINNs | 4.119×10−14.119\times 10^{-1} | 8.610×10−18.610\times 10^{-1} | 1.924×1001.924\times 10^{0} | 1.000×100¯\underline{1.000\times 10^{0}} | 1.000×1001.000\times 10^{0} | 1.624×1001.624\times 10^{0} | 2337s |
| κ=104\kappa=10^{4} | AT-PINNs | 4.804×10−14.804\times 10^{-1} | 6.985×10−16.985\times 10^{-1} | 1.334×1011.334\times 10^{1} | 1.002×1001.002\times 10^{0} | 9.732×10−1¯\underline{9.732\times 10^{-1}} | 1.334×1011.334\times 10^{1} | 1774s |
| ν=102\nu=10^{2} | MW-PINNs | 5.641×10−2¯\underline{5.641\times 10^{-2}} | 5.177×10−2¯\underline{5.177\times 10^{-2}} | 1.126×100¯\underline{1.126\times 10^{0}} | 1.003×1001.003\times 10^{0} | 9.970×10−19.970\times 10^{-1} | 6.557×𝟏𝟎−𝟐\mathbf{6.557\times 10^{-2}} | 2058s |
|  | MF-PINNs ↑\uparrow | 1.369×𝟏𝟎−𝟐\mathbf{1.369\times 10^{-2}} | 1.061×𝟏𝟎−𝟐\mathbf{1.061\times 10^{-2}} | 9.956×𝟏𝟎−𝟏\mathbf{9.956\times 10^{-1}} | 6.484×𝟏𝟎−𝟐\mathbf{6.484\times 10^{-2}} | 6.555×𝟏𝟎−𝟐\mathbf{6.555\times 10^{-2}} | 7.649×10−1¯\underline{7.649\times 10^{-1}} | 7396s |
|  | PINNs | 3.098×1003.098\times 10^{0} | 1.106×1001.106\times 10^{0} | 8.637×1008.637\times 10^{0} | 1.000×1001.000\times 10^{0} | 1.000×1001.000\times 10^{0} | 8.553×1008.553\times 10^{0} | 2144s |
| κ=102\kappa=10^{2} | AT-PINNs | 2.433×1002.433\times 10^{0} | 1.333×1001.333\times 10^{0} | 2.095×100¯\underline{2.095\times 10^{0}} | 1.014×1001.014\times 10^{0} | 1.047×1001.047\times 10^{0} | 1.883×1011.883\times 10^{1} | 2770s |
| ν=104\nu=10^{4} | MW-PINNs | 2.047×100¯\underline{2.047\times 10^{0}} | 8.288×10−1¯\underline{8.288\times 10^{-1}} | 6.471×1006.471\times 10^{0} | 1.290×𝟏𝟎−𝟏\mathbf{1.290\times 10^{-1}} | 1.352×𝟏𝟎−𝟏\mathbf{1.352\times 10^{-1}} | 6.482×100¯\underline{6.482\times 10^{0}} | 2805s |
|  | MF-PINNs ↑\uparrow | 2.906×𝟏𝟎−𝟏\mathbf{2.906\times 10^{-1}} | 1.882×𝟏𝟎−𝟏\mathbf{1.882\times 10^{-1}} | 3.701×𝟏𝟎−𝟏\mathbf{3.701\times 10^{-1}} | 1.464×10−1¯\underline{1.464\times 10^{-1}} | 1.539×10−1¯\underline{1.539\times 10^{-1}} | 1.477×𝟏𝟎−𝟏\mathbf{1.477\times 10^{-1}} | 4014s |
|  | PINNs | 1.408×1001.408\times 10^{0} | 1.565×1001.565\times 10^{0} | 4.623×1004.623\times 10^{0} | 1.000×1001.000\times 10^{0} | 1.000×1001.000\times 10^{0} | 3.257×1003.257\times 10^{0} | 3072s |
| κ=104\kappa=10^{4} | AT-PINNs | 1.562×1001.562\times 10^{0} | 1.455×1001.455\times 10^{0} | 2.027×1002.027\times 10^{0} | 2.262×1002.262\times 10^{0} | 3.733×1003.733\times 10^{0} | 1.929×1011.929\times 10^{1} | 2547s |
| ν=104\nu=10^{4} | MW-PINNs | 3.484×10−1¯\underline{3.484\times 10^{-1}} | 5.449×𝟏𝟎−𝟏\mathbf{5.449\times 10^{-1}} | 1.286×100¯\underline{1.286\times 10^{0}} | 7.459×10−1¯\underline{7.459\times 10^{-1}} | 9.900×10−1¯\underline{9.900\times 10^{-1}} | 4.087×10−1¯\underline{4.087\times 10^{-1}} | 2837s |
|  | MF-PINNs ↑\uparrow | 2.000×𝟏𝟎−𝟏\mathbf{2.000\times 10^{-1}} | 6.306×10−1¯\underline{6.306\times 10^{-1}} | 4.114×𝟏𝟎−𝟏\mathbf{4.114\times 10^{-1}} | 1.689×𝟏𝟎−𝟏\mathbf{1.689\times 10^{-1}} | 1.697×𝟏𝟎−𝟏\mathbf{1.697\times 10^{-1}} | 2.032×𝟏𝟎−𝟏\mathbf{2.032\times 10^{-1}} | 3995s |
|  | PINNs | 1.900×10−11.900\times 10^{-1} | 1.147×1001.147\times 10^{0} | 3.038×1003.038\times 10^{0} | 1.012×1001.012\times 10^{0} | 2.336×1002.336\times 10^{0} | 2.990×1002.990\times 10^{0} | 1904s |
| κ=102\kappa=10^{2} | AT-PINNs | 8.916×10−18.916\times 10^{-1} | 8.958×10−18.958\times 10^{-1} | 2.961×1002.961\times 10^{0} | 1.904×1001.904\times 10^{0} | 1.227×1001.227\times 10^{0} | 2.152×1002.152\times 10^{0} | 2272s |
| ν=102\nu=10^{2} | MW-PINNs | 6.667×10−2¯\underline{6.667\times 10^{-2}} | 4.141×10−2¯\underline{4.141\times 10^{-2}} | 7.902×10−1¯\underline{7.902\times 10^{-1}} | 8.544×10−2¯\underline{8.544\times 10^{-2}} | 6.701×10−2¯\underline{6.701\times 10^{-2}} | 4.041×10−1¯\underline{4.041\times 10^{-1}} | 2285s |
|  | MF-PINNs ↑\uparrow | 2.014×𝟏𝟎−𝟐\mathbf{2.014\times 10^{-2}} | 1.450×𝟏𝟎−𝟐\mathbf{1.450\times 10^{-2}} | 3.157×𝟏𝟎−𝟏\mathbf{3.157\times 10^{-1}} | 5.781×𝟏𝟎−𝟐\mathbf{5.781\times 10^{-2}} | 5.812×𝟏𝟎−𝟐\mathbf{5.812\times 10^{-2}} | 5.913×𝟏𝟎−𝟐\mathbf{5.913\times 10^{-2}} | 6679s |
|  | PINNs | 2.867×10−22.867\times 10^{-2} | 2.729×10−22.729\times 10^{-2} | 1.478×10−11.478\times 10^{-1} | 1.335×10−21.335\times 10^{-2} | 1.652×10−21.652\times 10^{-2} | 4.096×10−24.096\times 10^{-2} | 1324s |
| κ=1\kappa=1 | AT-PINNs | 4.077×10−24.077\times 10^{-2} | 8.280×10−28.280\times 10^{-2} | 2.055×10−12.055\times 10^{-1} | 8.397×10−18.397\times 10^{-1} | 8.074×10−18.074\times 10^{-1} | 8.716×10−28.716\times 10^{-2} | 1255s |
| ν=1\nu=1 | MW-PINNs | 1.725×10−2¯\underline{1.725\times 10^{-2}} | 2.180×10−2¯\underline{2.180\times 10^{-2}} | 7.160×10−2¯\underline{7.160\times 10^{-2}} | 1.207×10−2¯\underline{1.207\times 10^{-2}} | 1.160×10−2¯\underline{1.160\times 10^{-2}} | 2.102×10−2¯\underline{2.102\times 10^{-2}} | 1420s |
|  | MF-PINNs ↑\uparrow | 2.996×𝟏𝟎−𝟑\mathbf{2.996\times 10^{-3}} | 2.524×𝟏𝟎−𝟑\mathbf{2.524\times 10^{-3}} | 1.936×𝟏𝟎−𝟐\mathbf{1.936\times 10^{-2}} | 2.919×𝟏𝟎−𝟑\mathbf{2.919\times 10^{-3}} | 3.026×𝟏𝟎−𝟑\mathbf{3.026\times 10^{-3}} | 1.608×𝟏𝟎−𝟑\mathbf{1.608\times 10^{-3}} | 3329s |

The bold marks the lowest error of each physical quantity in each arguments group, while the underline marks the second-lowest error of each physical quantity in each arguments group. The upward arrows ↑\uparrow mark the relatively best methods under the same parameters.

#### 4.4.2 Ablation experiments for MF-PINNs

To verify the effect of other improvements for MF-PINNs, we conduct the following ablation experiments.

Firstly, we conduct several experiments on different combinations of activation functions. Table [4](https://arxiv.org/html/2510.17508v1#S4.T4 "Table 4 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") lists the results of the different combinations of activation functions. All the experiments adopt MF-PINNs under the group 𝕂=10−4​𝕀,ν=1\mathbb{K}=10^{-4}\mathbb{I},\nu=1. Thus, we could draw the following conclusions:

1. 1.

   The smoothness of R​e​L​U​(θ​x)ReLU(\theta\textbf{x}) is too limited, and it could not be used in Stokes-Darcy problems, unless it is replaced by S​o​f​t​p​l​u​s​(θ​x)Softplus(\theta\textbf{x}), S​w​i​s​h​(θ​x)Swish(\theta\textbf{x}), etc.
2. 2.

   The adaptive t​a​n​h​(θ​x)tanh(\theta\textbf{x}) converges faster than s​i​g​m​o​i​d​(θ​x)sigmoid(\theta\textbf{x}), while it seems that the effects of adaptive s​i​g​m​o​i​d​(θ​x)sigmoid(\theta\textbf{x}) are much better than t​a​n​h​(θ​x)tanh(\theta\textbf{x}) in our MF-PINNs.
3. 3.

   The adaptive s​i​n​(2​π​θ​x/T)sin(2\pi\theta\textbf{x}/T) is quite effective for high-frequency problems, but it may not be the best choice for low-frequency problems. In addition, if the parameter 2​π​θ/T2\pi\theta/T is too large, like s​i​n​(2​π​θ​x)sin(2\pi\theta\textbf{x}) in this case, it may be very risky to cause gradient explosion during backwarding.
4. 4.

   The pre-positioned Fourier feature layers are one of the effective ways for our MF-PINNs. Furthermore, accurate periodic characteristics are quite crucial for training PINNs. For example, the performance of t​a​n​h​(θ)∘s​i​n​(𝐱)tanh(\theta)\circ sin(\mathbf{x}) would not be as suitable as that of t​a​n​h​(θ)∘s​i​n​(π​𝐱)tanh(\theta)\circ sin(\pi\mathbf{x}) in this case.
5. 5.

   In this case, it is obvious to see the period of the velocity fields and pressure fields, T𝐮=1,Tp=2T\_{\mathbf{u}}=1,T\_{p}=2. Hence, the least common multiple of their periods is T=2T=2, and the periods of Fourier feature operators had better be several integer multiples of T=2T=2. In Table [4](https://arxiv.org/html/2510.17508v1#S4.T4 "Table 4 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), the performance of t​a​n​h​(θ)∘s​i​n​(π​𝐱)tanh(\theta)\circ sin(\pi\mathbf{x}) is not as effective as t​a​n​h​(θ)∘s​i​n​(2​π​𝐱)tanh(\theta)\circ sin(2\pi\mathbf{x}) for our MF-PINNs. And this difference is especially reflected in the error of pressure field, e​r​r​ℒ2​(p)err\mathcal{L}\_{2}\left(p\right).

Table 4: This table shows that different combinations of activation functions (AF) lead to changing accuracy of our MF-PINNs under group 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I}, ν=1\nu=1.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| First AF | Other AF | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐬)\mathbf{err\mathcal{L}\_{2}\left(u\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐬)\mathbf{err\mathcal{L}\_{2}\left(v\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐬)\mathbf{err\mathcal{L}\_{2}\left(p\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐝)\mathbf{err\mathcal{L}\_{2}\left(u\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐝)\mathbf{err\mathcal{L}\_{2}\left(v\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐝)\mathbf{err\mathcal{L}\_{2}\left(p\_{d}\right)} | Time |
| R​e​L​U​(θ​𝐱)ReLU(\theta\mathbf{x}) | R​e​L​U​(θ​𝐱)ReLU(\theta\mathbf{x}) | I​n​fInf | I​n​fInf | I​n​fInf | I​n​fInf | I​n​fInf | I​n​fInf | 4582s |
| S​o​f​t​p​l​u​s​(θ​𝐱)Softplus(\theta\mathbf{x}) | S​o​f​t​p​l​u​s​(θ​𝐱)Softplus(\theta\mathbf{x}) | 1.731×10−21.731\times 10^{-2} | 1.954×10−21.954\times 10^{-2} | 7.732×10−17.732\times 10^{-1} | 2.629×10−32.629\times 10^{-3} | 2.708×10−32.708\times 10^{-3} | 2.372×1002.372\times 10^{0} | 7477s |
| s​i​g​m​o​i​d​(θ​𝐱)sigmoid(\theta\mathbf{x}) | s​i​g​m​o​i​d​(θ​𝐱)sigmoid(\theta\mathbf{x}) | 2.811×10−22.811\times 10^{-2} | 2.745×10−22.745\times 10^{-2} | 1.630×10−11.630\times 10^{-1} | 6.859×10−46.859\times 10^{-4} | 6.695×10−46.695\times 10^{-4} | 2.299×10−1¯\underline{2.299\times 10^{-1}} | 5652s |
| t​a​n​h​(θ​𝐱)tanh(\theta\mathbf{x}) | t​a​n​h​(θ​𝐱)tanh(\theta\mathbf{x}) | 4.287×𝟏𝟎−𝟑\mathbf{4.287\times 10^{-3}} | 4.367×𝟏𝟎−𝟑\mathbf{4.367\times 10^{-3}} | 8.676×10−18.676\times 10^{-1} | 9.146×10−49.146\times 10^{-4} | 1.072×10−31.072\times 10^{-3} | 1.371×1001.371\times 10^{0} | 3756s |
| s​i​n​(θ​𝐱)sin(\theta\mathbf{x}) | s​i​n​(θ​𝐱)sin(\theta\mathbf{x}) | 6.273×10−36.273\times 10^{-3} | 6.381×10−3¯\underline{6.381\times 10^{-3}} | 8.854×10−18.854\times 10^{-1} | 1.817×10−31.817\times 10^{-3} | 1.869×10−31.869\times 10^{-3} | 1.384×1001.384\times 10^{0} | 3616s |
| s​i​n​(π​θ​𝐱)sin(\pi\theta\mathbf{x}) | s​i​n​(π​θ​𝐱)sin(\pi\theta\mathbf{x}) | 6.999×10−36.999\times 10^{-3} | 7.427×10−37.427\times 10^{-3} | 1.137×10−1¯\underline{1.137\times 10^{-1}} | 4.568×𝟏𝟎−𝟒\mathbf{4.568\times 10^{-4}} | 4.304×𝟏𝟎−𝟒\mathbf{4.304\times 10^{-4}} | 2.303×10−12.303\times 10^{-1} | 3652s |
| s​i​n​(2​π​θ​𝐱)sin(2\pi\theta\mathbf{x}) | s​i​n​(2​π​θ​𝐱)sin(2\pi\theta\mathbf{x}) | 1.000×1001.000\times 10^{0} | 1.000×1001.000\times 10^{0} | 1.179×1011.179\times 10^{1} | 2.911×10−12.911\times 10^{-1} | 2.885×10−12.885\times 10^{-1} | 1.179×1011.179\times 10^{1} | 2359s |
| |  | | --- | | tanh(θ)∘tanh(\theta)\circ | | s​i​n​(𝐱)sin(\mathbf{x}) | | t​a​n​h​(θ​𝐱)tanh(\theta\mathbf{x}) | 5.218×10−35.218\times 10^{-3} | 6.560×10−36.560\times 10^{-3} | 1.231×1001.231\times 10^{0} | 6.244×10−46.244\times 10^{-4} | 1.081×10−31.081\times 10^{-3} | 1.907×1001.907\times 10^{0} | 4424s |
| |  | | --- | | tanh(θ)∘tanh(\theta)\circ | | s​i​n​(π​𝐱)sin(\pi\mathbf{x}) | | t​a​n​h​(θ​𝐱)tanh(\theta\mathbf{x}) | 8.621×10−38.621\times 10^{-3} | 9.590×10−39.590\times 10^{-3} | 2.326×10−12.326\times 10^{-1} | 7.893×10−47.893\times 10^{-4} | 7.703×10−47.703\times 10^{-4} | 3.653×10−13.653\times 10^{-1} | 3163s |
| |  | | --- | | tanh(θ)∘tanh(\theta)\circ | | s​i​n​(2​π​𝐱)sin(2\pi\mathbf{x}) | | t​a​n​h​(θ​𝐱)tanh(\theta\mathbf{x}) | 4.964×10−3¯\underline{4.964\times 10^{-3}} | 6.485×10−36.485\times 10^{-3} | 6.737×𝟏𝟎−𝟐\mathbf{6.737\times 10^{-2}} | 4.964×10−4¯\underline{4.964\times 10^{-4}} | 4.927×10−4¯\underline{4.927\times 10^{-4}} | 1.068×𝟏𝟎−𝟐\mathbf{1.068\times 10^{-2}} | 3662s |

The bold marks the lowest error of each physical quantity, while the underline marks the second-lowest error of each physical quantity. The term Time refers to the total time record taken for 1000010000 epochs.

Secondly, we use the adaptive activation function strategy for our MF-PINNs to accelerate converging according to Section [3.3](https://arxiv.org/html/2510.17508v1#S3.SS3 "3.3 Activation functions with high-frequency features ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"). Fig. [9](https://arxiv.org/html/2510.17508v1#S4.F9 "Fig. 9 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") shows the dynamic change of the adaptive parameters a,ba,b during the training process. The activation functions ℱs=t​a​n​h​(0.7240​x)\mathcal{F}\_{s}=tanh(0.7240x) and ℱd=t​a​n​h​(0.9394​x)\mathcal{F}\_{d}=tanh(0.9394x) are suitable for this particular example under the group 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I}, ν=1\nu=1.

![Refer to caption](x30.png)


(a)

![Refer to caption](x31.png)


(b)



Fig. 9: These two pictures show the training process of our MF-PINNs under 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I} and ν=1\nu=1. The dashed grey line means we end up using the Adam optimizer and then use the L-BFGS optimizer. (a) the dynamic change of adaptive parameters aa and bb of the adaptive activation functions. (b) the dynamic change of learning rate.

Lastly, we verify the effect of the adaptive strategy for learning rate decay via ReduceLROnPlateau we adopted in Section [3.4](https://arxiv.org/html/2510.17508v1#S3.SS4 "3.4 Optimizer and learning rate decay ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") under group 𝕂=10−4​𝕀,ν=1\mathbb{K}=10^{-4}\mathbb{I},\nu=1. Furthermore, we could draw the following conclusions:

1. 1.

   In Fig. [9](https://arxiv.org/html/2510.17508v1#S4.F9 "Fig. 9 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), at the beginning of training during Adam and L-BFGS stages, we set high initial learning rates in Table [1](https://arxiv.org/html/2510.17508v1#S4.T1 "Table 1 ‣ 4.1 Model parameter ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") to accelerate uN​Nu\_{NN} to converge effectively. Consequently, the e​r​r​ℒ2err\mathcal{L}\_{2} of group Adam: 10−3\,10^{-3} and L-BFGS:  10−1\,10^{-1} is generally lower than that of group Adam : 10−3:\,10^{-3} and L-BFGS:  10−3\,10^{-3}.
2. 2.

   Midway through training, we make the learning rate adaptively decay. This work avoids uN​Nu\_{NN} oscillating around the optimal point uu because of a relatively high learning rate.
   The evidence is obvious as follows:

   1. (a)

      In Table [5](https://arxiv.org/html/2510.17508v1#S4.T5 "Table 5 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), the group with the adaptive learning rate decay strategy for the Adam optimizer has a lower error. This is because the strategy for the Adam has a higher training efficiency, and it brings the parameter group closer to the optimal point when the optimizer is changed to L-BFGS.
   2. (b)

      In Table [5](https://arxiv.org/html/2510.17508v1#S4.T5 "Table 5 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), although the pressure fields are easy to be ignored, the groups with the adaptive learning rate decay strategy for the L-BFGS could perform more outstandingly.
   3. (c)

      In Fig. [5](https://arxiv.org/html/2510.17508v1#S4.F5 "Fig. 5 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), the total loss 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta) oscillates violently and the phenomenon, loss spikes, keep appearing. So it causes the error of MF-PINNs to increases rather than decreases. After adjusting the learning rate of the Adam optimizer from 10−310^{-3} to 10−410^{-4} at the 3718t​h3718^{th} epoch in Fig. [9](https://arxiv.org/html/2510.17508v1#S4.F9 "Fig. 9 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), the total loss oscillations are mitigated, and the e​r​r​ℒ2​(ud)err\mathcal{L}\_{2}(u\_{d}) and e​r​r​ℒ2​(vd)err\mathcal{L}\_{2}(v\_{d}) begin to decrease steadily again in Fig. [5](https://arxiv.org/html/2510.17508v1#S4.F5 "Fig. 5 ‣ 4.4.1 Alleviate the gradient competition ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)").
3. 3.

   In Table [5](https://arxiv.org/html/2510.17508v1#S4.T5 "Table 5 ‣ 4.4.2 Ablation experiments for MF-PINNs ‣ 4.4 Analysis of numerical results ‣ 4 Numerical test ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)"), the groups without any strategy for decaying the learning rate of L-BFGS require more epochs to stop the oscillation. This trouble means more time and computing resources are consumed. At the end of training of L-BFGS, the learning rate decreases adaptively, interval by interval. When the learning rate decreases to 10−810^{-8}, 𝒥​(𝐱,Θ)\mathcal{J}(\mathbf{x},\Theta) and e​r​r​ℒ2err\mathcal{L}\_{2} barely change in value. Hence, we could infer that uN​N​(𝐱,Θ)u\_{NN}(\mathbf{x},\Theta) has nearly enough reached the optimal point u​(𝐱,Θ¯)u(\mathbf{x},\overline{\Theta}).

These facts prove that the strategies we have defined in Section [3.4](https://arxiv.org/html/2510.17508v1#S3.SS4 "3.4 Optimizer and learning rate decay ‣ 3 Algorithm framework ‣ A Mixed-Form PINNs (MF-PINNs) for Solving the Coupled Stokes-Darcy Equations L. Shan is supported by Guangdong Basic and Applied Basic Research Foundation (2024A1515010294) and STU Scientifc Research Initiation Grant (NTF25007T,NTF21006)") are very necessary and highly efficient for training PINNs.

Table 5: This table shows how different initial learning rates (I-LR) and learning rate decay strategies (LRD) affect the accuracy of our MF-PINNs under the group 𝕂=10−4​𝕀\mathbb{K}=10^{-4}\mathbb{I}, ν=1\nu=1. If all the e​r​r​ℒ2err\mathcal{L}\_{2} no longer oscillate later, we approximately consider that the PINNs solutions converge at the nt​hn^{th} epoch (CE) during the L-BFGS stage.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I-LR | LRD-A | LRD-L | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐬)\mathbf{err\mathcal{L}\_{2}\left(u\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐬)\mathbf{err\mathcal{L}\_{2}\left(v\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐬)\mathbf{err\mathcal{L}\_{2}\left(p\_{s}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐮𝐝)\mathbf{err\mathcal{L}\_{2}\left(u\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐯𝐝)\mathbf{err\mathcal{L}\_{2}\left(v\_{d}\right)} | 𝐞𝐫𝐫​ℒ𝟐​(𝐩𝐝)\mathbf{err\mathcal{L}\_{2}\left(p\_{d}\right)} | CE | Time |
| Adam: | ✗ | ✗ | 1.195×10−2¯\underline{1.195\times 10^{-2}} | 2.209×10−2¯\underline{2.209\times 10^{-2}} | 1.365×10−1¯\underline{1.365\times 10^{-1}} | 1.565×10−3¯\underline{1.565\times 10^{-3}} | 1.805×10−31.805\times 10^{-3} | 2.375×10−12.375\times 10^{-1} | ⩾3000t​h\geqslant 3000^{th} | 10027s |
| 10−310^{-3} | ✔ | ✗ | 3.866×10−23.866\times 10^{-2} | 5.955×10−25.955\times 10^{-2} | 2.540×10−12.540\times 10^{-1} | 4.406×10−34.406\times 10^{-3} | 4.718×10−34.718\times 10^{-3} | 2.473×10−12.473\times 10^{-1} | ⩾2989t​h\geqslant 2989^{th} | 3827s |
| L-BFGS: | ✗ | ✔ | 1.459×10−21.459\times 10^{-2} | 4.341×10−24.341\times 10^{-2} | 3.221×10−13.221\times 10^{-1} | 1.764×10−31.764\times 10^{-3} | 1.757×10−3¯\underline{1.757\times 10^{-3}} | 4.602×10−14.602\times 10^{-1} | 1611t​h1611^{th} | 6161s |
| 10−310^{-3} | ✔ | ✔ | 4.154×10−24.154\times 10^{-2} | 7.835×10−27.835\times 10^{-2} | 2.726×10−12.726\times 10^{-1} | 3.950×10−33.950\times 10^{-3} | 4.466×10−34.466\times 10^{-3} | 2.116×10−1¯\underline{2.116\times 10^{-1}} | 1s​t1^{st} | 2017s |
| Adam: | ✗ | ✗ | 5.596×10−35.596\times 10^{-3} | 7.626×10−37.626\times 10^{-3} | 1.972×10−11.972\times 10^{-1} | 2.516×𝟏𝟎−𝟒\mathbf{2.516\times 10^{-4}} | 2.596×𝟏𝟎−𝟒\mathbf{2.596\times 10^{-4}} | 2.858×10−12.858\times 10^{-1} | ⩾3000t​h\geqslant 3000^{th} | 6131s |
| 10−310^{-3} | ✔ | ✗ | 4.200×10−34.200\times 10^{-3} | 4.270×10−34.270\times 10^{-3} | 1.537×10−11.537\times 10^{-1} | 2.603×10−42.603\times 10^{-4} | 2.741×10−42.741\times 10^{-4} | 2.275×10−12.275\times 10^{-1} | ⩾3000t​h\geqslant 3000^{th} | 5198s |
| L-BFGS: | ✗ | ✔ | 5.690×10−35.690\times 10^{-3} | 6.345×10−36.345\times 10^{-3} | 3.532×10−13.532\times 10^{-1} | 4.785×10−44.785\times 10^{-4} | 5.433×10−45.433\times 10^{-4} | 5.927×10−15.927\times 10^{-1} | 597t​h597^{th} | 3086s |
| 10−110^{-1} | ✔ | ✔ | 2.715×𝟏𝟎−𝟑\mathbf{2.715\times 10^{-3}} | 3.103×𝟏𝟎−𝟑\mathbf{3.103\times 10^{-3}} | 5.404×𝟏𝟎−𝟐\mathbf{5.404\times 10^{-2}} | 4.959×10−44.959\times 10^{-4} | 6.254×10−46.254\times 10^{-4} | 6.951×𝟏𝟎−𝟐\mathbf{6.951\times 10^{-2}} | 569t​h569^{th} | 3365s |

The underline marks the minimum error of the former group, while the bold marks the minimum error of the latter group.

## 5 Conclusions and prospects

In this paper, we conclude that extreme physical constants always produce ill-conditional numerical formulations in conventional methods. To improve PINNs, we conclude with the following suggestions.

1. 1.

   From the perspective of physical laws:

   1. (a)

      The multiple physics fields are usually coupled through physical constants, such as Reynolds number, permeability tensor, etc. When they are either extremely high or low, they may lead to gradient competition between the multiple physics fields and failed training for conventional PINNs.
   2. (b)

      For the problems above, our MF-PINNs decouples the velocity field and the pressure field by combining the VP form and the SV form. This improvement could effectively alleviate the gradient competition among multiple physics fields.
   3. (c)

      At present, the idea of decoupling must rely on the linear differential operators in the equations. However, it may be uncertain to generalize it to other more complex systems or models, such as Euler’s equations, compressible flows, and shock waves.
2. 2.

   From the perspective of the activation functions and training parallel PINNs:

   1. (a)

      It is necessary to select activation functions with sufficient smoothness, because they directly determine whether the PINNs numerical solutions are well-defined or not.
   2. (b)

      We could obtain the physical periodicity from the boundary conditions and non-homogeneous terms. The period of the activation functions had better be integer multiples of the original problem. Otherwise, the opposite operation may waste many computing resources.
   3. (c)

      We conclude that different activation functions are effective for different problems, and combining different types of activation functions may improve the abilities of PINNs. For example, the t​a​n​htanh is suitable for discontinuity problems, while the s​i​nsin is appropriate for high-frequency problems.
   4. (d)

      We find that increasing the initial learning rate of L-BFGS appropriately and using adaptive strategies for learning rate decay are important to our MF-PINNs.

Though our MOD-PINNS overcomes some shortcomings in this paper, we have to admit that it has not been studied and applied further. How to select the optimal weights for different equation forms in loss functions? Could our MF-PINNs have the potential to solve complex turbulence hidden in Navier-Stokes systems, when the Reynolds numbers are extremely high or low? These topics are worth further exploring and studying.

## CRediT authorship contribution statement

Li Shan: Conceptualization, Methodology, Investigation, Writing – review & editing, Supervision, Project administration, Funding acquisition. Xi Shen: Methodology, Visualization, Coding, Validation, Writing - original draft preparation.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request. The code and data associated with this paper are available at <https://github.com/shxshx48716/MF-PINNs.git>.

## Acknowledgements

The authors of this paper gratefully acknowledge Prof. J. Zhao of Capital Normal University for his expert guidance on methodology and reviewing of the entire manuscript.

## References

* [1]

  [G.S. Beavers , D.D. Joseph, Boundary conditions at a naturally permeable wall. J. Fluid Mech. 1967, 30, 197-207.](https://doi.org/10.1017/S0022112067001375)
* [2]

  [M. Raissi , P. Perdikaris, G.E. Karniadakis, Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. J. Comput. Phys. 2019, 378, 686–707.](https://doi.org/10.1016/j.jcp.2018.10.045)
* [3]

  [A.D. Jagtap, E. Kharazmi, G.E. Karniadakis, Conservative physics-informed neural networks on discrete domains for conservation laws: Applications to forward and inverse problems. Comput. Methods Appl. Mech. Eng. 2020, 365, 113028.](https://10.1016/j.cma.2023.114903)
* [4]

  [K. Shukla, A.D. Jagtap, G.E. Karniadakis, Parallel physics-informed neural networks via domain decomposition. J. Comput. Phys. 2021, 447, 110683.](https://doi.org/10.1016/j.jcp.2021.110683)
* [5]

  [A. Kumar Sarma, S. Roy, C. Annavarapu, P. Roy, S. Jagannathan, Interface PINNs (I-PINNs): A physics-informed neural networks framework for interface problems, Comput. Methods Appl. Mech. Eng., 2024, 429, 117135.](https://doi.org/10.1016/j.cma.2024.117135)
* [6]

  [N. Chen, L. Sergio ,R. Ma, A. Chen,C. Cui , PF-PINNs: Physics-informed neural networks for solving coupled Allen-Cahn and Cahn-Hilliard phase field equations, J. Comput. Phys., 2025, 529, 113843.](https://doi.org/10.1016/j.jcp.2025.113843)
* [7]

  [R. Mattey, S. Ghosh, A novel sequential method to train physics informed neural networks for Allen Cahn and Cahn Hilliard equations, Comput. Methods Appl. Mech. Eng., 2022, 390, 114474.](https://doi.org/10.1016/j.cma.2021.114474)
* [8]

  [H. Li, H. Fan, Z. Tan, Two novel discontinuity-removing PINNs for solving variable coefficient elliptic interface problems on curved surfaces, Comput. Methods Appl. Mech. Eng., 2025, 435, 117637.](https://doi.org/10.1016/j.cma.2024.117637)
* [9]

  [A.D. Jagtap, G.E. Karniadakis, Extended physics-informed neural networks (XPINNs): A generalized space-time domain decomposition based deep learning framework for nonlinear partial differential equations. Commun. Comput. Phys. 2020, 28, 2002–2041.](https://10.4208/cicp.oa-2020-0164)
* [10]

  [S. Wang, A.K. Bhartari, B. Li, P. Perdikaris, Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective, arXiv preprint arXiv:2502.00604, 2025.](https://doi.org/10.48550/arXiv.2502.00604)
* [11]

  [Y. Hwang, D. Lim, Dual Cone Gradient Descent for Training Physics-Informed Neural Networks, arXiv preprint arXiv:2409.18426, 2024.](https://doi.org/10.48550/arXiv.2409.18426)
* [12]

  [S. Wang, X. Yu, P. Perdikaris, When and why PINNs fail to train: A neural tangent kernel perspective, J. Comput. Phys., 2022, 449, 110768.](https://doi.org/10.1016/j.jcp.2021.110768)
* [13]

  [A. Bonfanti, G. Bruno, C. Cipriani, The Challenges of the Nonlinear Regime for Physics-Informed Neural Networks, arXiv preprint arXiv:2402.03864, 2024.](https://doi.org/10.48550/arXiv.2402.03864)
* [14]

  [Y. Wang, Y. Yao, J. Guo, Z. Gao, A practical PINN framework for multi-scale problems with multi-magnitude loss terms, J. Comput. Phys., 2024, 510, 113112.](https://doi.org/10.1016/j.jcp.2024.113112)
* [15]

  [Q. Liu, M. Chu, N. Thuerey, ConFIG: Towards Conflict-free Training of Physics Informed Neural Networks, arXiv preprint arXiv:2408.11104, 2025.](https://doi.org/10.48550/arXiv.2408.11104)
* [16]

  [N. Chen, C. Cui, R. Ma, A. Chen, S. Wang , Sharp-PINNs: staggered hard-constrained physics-informed neural networks for phase field modelling of corrosion, arXiv preprint arXiv:2502.11942, 2025.](https://doi.org/10.48550/arXiv.2502.11942)
* [17]

  [S.V. Patankar, D.B. Spalding, A calculation procedure for heat, mass and momentum transfer in three-dimensional parabolic flows. In Numerical Prediction of Flow, Heat Transfer, Turbulence and Combustion; Patankar S.V., Pollard A., Singhal A.K., Vanka S.P., Eds.; Pergamon: Oxford, UK, 1983, 54-73.](https://doi.org/10.1016/B978-0-08-030937-8.50013-1)
* [18]

  [C.H. Lan, Y.D. Wu, The component-consistent pressure correction projection method for the incompressible Navier-Stokes equations, Comput. Math. Appl., 1996, 31(8), 1-21.](https://doi.org/10.1016/0898-1221(96)00057-0)
* [19]

  [A.D. Jagtap, K. Kawaguchi, G.E. Karniadakis, Adaptive activation functions accelerate convergence in deep and physics-informed neural networks, J. Comput. Phys., 2020, 404, 109136.](https://doi.org/10.1016/j.jcp.2019.109136)
* [20]

  [S. Wang, H. Wang, P. Perdikaris, On the eigenvector bias of Fourier feature networks: From regression to solving multi-scale PDEs with physics-informed neural networks, Comput. Methods Appl. Mech. Eng., 2021, 384, 113938.](https://doi.org/10.1016/j.cma.2021.113938)
* [21]

  [S. Cai, Z. Wang, L. Lu, T.A. Zaki, G.E. Karniadakis, DeepM & Mnet: Inferring the electroconvection multiphysics fields based on operator approximation by neural networks, J. Comput. Phys., 2021, 436, 110296.](https://doi.org/10.1016/j.jcp.2021.110296)
* [22]

  [Z. Mao, L. Lu, O. Marxen, T.A. Zaki, G.E. Karniadakis, DeepM & Mnet for hypersonics: Predicting the coupled flow and finite-rate chemistry behind a normal shock using neural-network approximation of operators, J. Comput. Phys., 2021, 447, 110698.](https://doi.org/10.1016/j.jcp.2021.110698)
* [23]

  [X. Li, J. Wu, X. Tai, J. Xu, Y.G. Wang, Solving a class of multi-scale elliptic PDEs by Fourier-based mixed physics informed neural networks, J. Comput. Phys., 2024, 508, 113012.](https://doi.org/10.1016/j.jcp.2024.113012)
* [24]

  [Z.Q. Xu, Y. Zhang, T. Luo, Y. Xiao, Z. Ma, Frequency Principle: Fourier Analysis Sheds Light on Deep Neural Networks, Commun. Comput. Phys., 2019, 26(5), 1485-1511.](https://doi.org/10.4208/cicp.OA-2020-0085)
* [25]

  [D. Liu, Y. Wang, A Dual-Dimer method for training physics-constrained neural networks with minimax architecture, Neural Networks, 2021, 136, 112-125.](https://doi.org/10.1016/j.neunet.2020.12.028)
* [26]

  [S. Wang, B. Li, Y. Chen, P. Perdikaris, PirateNets: Physics-informed Deep Learning with Residual Adaptive Networks, Journal of Machine Learning Research, 2024, 25, 1-51.](https://jmlr.org/papers/volume25/24-0313/24-0313)
* [27]

  [S. Xu, Y. Dai, C. Yan, Z. Sun, R. Huang, D. Guo, G. Yang, On the preprocessing of physics-informed neural networks: How to better utilize data in fluid mechanics, J. Comput. Phys., 2025, 528, 113837.](https://doi.org/10.1016/j.jcp.2025.113837)
* [28]

  [C. Qiu, J. Hou, Y. Xia, L. Shan, A high order ensemble algorithm for dual-porosity-Navier–Stokes flows. J. Comput. Phys. 2025, 529, 113833.](https://doi.org/10.1016/j.jcp.2025.113833)
* [29]

  [M. Lai, P. Wenston, Bivariate Spline Method for Numerical Solution of Steady State Navier–Stokes Equations over Polygons in Stream Function Formulation. Numer. Methods Partial Differ. Equ. 2000, 16(2), 147–173.](https://doi.org/10.1002/(SICI)1098-2426(200003)16:2<147::AID-NUM2>3.0.CO;2-9)
* [30]

  [J. Zhao, W. Zhu, B. Zhang, Y. Yang, The stabilized nonconforming virtual element method for the Darcy–Stokes problem, Commun. Nonlinear Sci. Numer. Simul., 2024, 138, 108252.](https://doi.org/10.1016/j.cnsns.2024.108252)
* [31]

  [K. Hornik, Approximation capabilities of multilayer feedforward networks, Neural Networks, 1991, 4(2), 251-257.](https://doi.org/10.1016/0893-6080(91)90009-T)
* [32]

  [X. Meng, R. Xie, J. Liao, X. Shen, S. Yang, A cost-effective over-temperature alarm system for cold chain delivery. J. Food Eng. 2024, 368, 111914.](https://doi.org/10.1016/j.jfoodeng.2023.111914)
* [33]

  [Y. Wang, Y. Yao, Z. Gao, An extrapolation-driven network architecture for physics-informed deep learning, Neural Networks, 2025, 183, 106998.](https://doi.org/10.1016/j.neunet.2024.106998)
* [34]

  [J. He, L. Li, J. Xu, C. Zheng, ReLU Deep Neural Networks and Linear Finite Elements. Journal Comput. Math. 2020, 38(3), 502–527.](https://doi.org/10.4208/jcm.1901-m2018-0160)
* [35]

  [J. Yue, J. Li, Efficient coupled deep neural networks for the time-dependent coupled Stokes-Darcy problems. Appl. Math. Comput. 2023, 437, 127514.](https://doi.org/10.1016/j.amc.2022.127514)
* [36]

  [R. Pu, X. Feng, Physics-Informed Neural Networks for Solving Coupled Stokes–Darcy Equation. Entropy 2022, 24, 1106.](https://doi.org/10.3390/e24081106)